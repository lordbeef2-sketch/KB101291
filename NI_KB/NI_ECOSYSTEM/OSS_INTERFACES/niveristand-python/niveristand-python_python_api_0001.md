# NI PYTHON API DIGEST: niveristand-python

<!--NI_PYTHON_API_SNAPSHOT repo=ni/niveristand-python commit=9ced536d3414f04a8b6b9315ce4c71b879d02a96 -->

<!--NI_PYTHON_API repo=niveristand-python path=examples/basic_rt_sequence_examples.py -->
## PYTHON MODULE: examples/basic_rt_sequence_examples.py

### `def add_two_numbers(x, y)`

### `def call_add_two_numbers_test()`

### `def run_add_two_numbers_tests()`

### `def array_operations()`


    Shows operations you can perform with array data types in a real-time sequence.

    An array can hold multiple values of the same data type. You cannot have arrays of arrays.
    Use arrays to pass buffers of data for playback or storage.

    Returns:
        float: sum of all values in the array.

    

### `def measure_elapsed_time()`


    Shows different ways to measure elapsed time in a sequence.

    You can measure time in milliseconds, microseconds, or seconds.

    Returns:
        int: time, in milliseconds, it took to run this sequence.

    

### `def state_machine_example()`

### `def run_non_deterministic(func)`

Run the sequence in a non-deterministic way.

    This function will execute the RT Sequence on the host using the public ClientAPI
    that is already available to VeriStand users. It will communicate to the gateway to
    set and get channel values.

    If using a python IDE, it's possible to debug this function as any other python function,
    so setting breakpoints, stepping into and over statements, etc., will work as expected.
    

### `def run_deterministic(func)`

Compile the sequence and run it deterministically inside the VeriStand engine.

    As the actual sequence won't be executed by python, debugging won't be available. Also, only
    functions marked as @nivs_rt_sequence will be accepted.
    

<!--NI_PYTHON_API repo=niveristand-python path=examples/engine_demo/engine_demo_advanced.py -->
## PYTHON MODULE: examples/engine_demo/engine_demo_advanced.py

### `def engine_demo_advanced(desired_rpm, actual_rpm, engine_temp)`

Turns on the engine, sets it to the desired rpm, and monitors the engine temperature.

### `def run_engine_demo_advanced()`

Run the engine_demo_advanced example.

    To handle a condition that stops a task (such as, the engine temperature rising above a safe value),
    use a try/finally block.

    Regardless of the result of the execution, the finally block can be used to safely shut down the engine.
    

### `def run_deterministic()`

### `def run_non_deterministic()`

<!--NI_PYTHON_API repo=niveristand-python path=examples/engine_demo/engine_demo_basic.py -->
## PYTHON MODULE: examples/engine_demo/engine_demo_basic.py

### `def engine_demo_basic(engine_power, desired_rpm)`

Turn on the engine, set the desired_rpm to the passed value for 20 seconds, and shut down the engine.

    You must access parameters through their ".value" property.
    

### `def run_engine_demo()`

Sets up channel references and calls the actual test.

### `def run_non_deterministic()`

Runs the sequence non-deterministically.

    This function executes the RT Sequence on the host using the public ClientAPI
    that installs with VeriStand. This function communicates with the gateway to set and get channel values.

    If you use a Python integrated developer environment (IDE),
    you can debug this function like a normal Python function.
    

### `def run_deterministic()`

Compiles the sequence and runs it deterministically inside the VeriStand engine.

    You cannot use debugging tools at this stage because VeriStand executes the sequence, not Python.
    If you do not mark the functions as @nivs_rt_sequence, Python will raise a :any:`niveristand.errors.VeristandError`.
    

<!--NI_PYTHON_API repo=niveristand-python path=examples/engine_demo/test_engine_set_points.py -->
## PYTHON MODULE: examples/engine_demo/test_engine_set_points.py

### `def set_engine_power(on_off)`

Turns the engine on or off.

### `def measure_set_point_response(setpoint, timeout, tolerance)`

Sets the desired rpm to the specified setpoint and wait until the signal settles.

    The tolerance is used to create upper and lower boundaries for the signal.
    Returns the amount of time it takes the signal to settle or timeout.
    

### `def inbounds_check(test_value, upper, lower)`

Returns True if lower <= value <= upper.

    Performs an inbounds check.
    

### `def test_run_engine_set_points_profile_deterministic()`

### `def test_run_engine_set_points_python()`

<!--NI_PYTHON_API repo=niveristand-python path=examples/legacy_basic_reconnect.py -->
## PYTHON MODULE: examples/legacy_basic_reconnect.py

- `GATEWAY = 'localhost'`

- `TARGET = 'Controller'`

- `SINE_WAVE = 'Aliases/SineWave'`

- `LOOP_RATE = 'Targets/Controller/System Channels/Actual Loop Rate'`

### `def sleep()`

<!--NI_PYTHON_API repo=niveristand-python path=examples/legacy_mix.py -->
## PYTHON MODULE: examples/legacy_mix.py

### `def mix_legacy_and_rtseq_run()`

Combines the legacy API with Python real-time sequences to run a deterministic test.

<!--NI_PYTHON_API repo=niveristand-python path=examples/sdf_deploy_with_deploy_option.py -->
## PYTHON MODULE: examples/sdf_deploy_with_deploy_option.py

### `def sdf_deploy_with_deploy_option()`

Use legacy API to deploy a system definition along with deploy option.

<!--NI_PYTHON_API repo=niveristand-python path=examples/sysdef_example.py -->
## PYTHON MODULE: examples/sysdef_example.py

### MODULE DOCSTRING

Create an empty system definition.

### `def main(filepath=None)`

The main portion of the script.

### `def get_asset(filename: str) -> str`

Returns the path to an asset for this example.

### `def create_system_definition(filepath: str, ip_address: str='localhost') -> SystemDefinition`

Creates the system definition.

### `def add_daq(system_definition: SystemDefinition)`

Adds a DAQ device to the system definition.

### `def add_can(system_definition: SystemDefinition)`

Adds the CAN section to the system definition.

### `def add_lin(system_definition: SystemDefinition)`

Adds a LIN section to the system definition.

### `def add_models(system_definition: SystemDefinition)`

Adds models to the system definition.

### `def add_remaining(system_definition: SystemDefinition)`

Add other items to the system definition.

### `def save_system_definition(system_definition: SystemDefinition)`

Saves the system definition.

<!--NI_PYTHON_API repo=niveristand-python path=setup.py -->
## PYTHON MODULE: setup.py

### MODULE DOCSTRING

Setup module for NI VeriStand.

### `def get_version(name)`

Calculate a version number.

### `def read_contents(file_to_read)`

Read a file in this folder.

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/__init__.py -->
## PYTHON MODULE: src/niveristand/__init__.py

- `__all__ = ['ErrorCode', 'NivsParam', 'nivs_rt_sequence', 'run_py_as_rtseq', 'save_py_as_rtseq', 'VeriStandSdfError', 'XMLVersionInfo']`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_auto_generated_classes.py -->
## PYTHON MODULE: src/niveristand/_auto_generated_classes.py

### MODULE DOCSTRING

Module for NationalInstruments.VeriStand.

### `class _staticproperty(staticmethod)`

#### `def __get__(self, *_)`

### `class _DotNetBase()`

#### `def __eq__(self, other) -> bool`

#### `def __repr__(self) -> str`

#### `def _custom_repr(self) -> str`

### `class _DotNetEnum(_DotNetBase)`

#### `def __repr__(self) -> str`

#### `def __str__(self) -> str`

#### `def __int__(self) -> int`

### `def _is_iterable(arg: Any) -> bool`

### `def _unwrap(out_params: Dict[Optional[Tuple[str, ...]], Tuple[int, Any]], *args: Tuple[Any]) -> Iterable[Any]`

### `def _wrap(one_or_many_args: Union[Any, Tuple[Any]]) -> Union[Any, Tuple[Any]]`

### `class VeriStandSdfError(Exception)`

Represents NI VeriStand error information, including an integer error code and a string error message. Error objects are immutable once created.

#### `def __str__(self) -> str`

#### `def __init__(self, code: int, message: str)`

#### `def __init__(self, code: ErrorCode, message: str)`

#### `def __init__(self, code: int, message: str, resolved_error: str)`

#### `def __init__(self, code: ErrorCode, message: str, resolved_error: str)`

#### `def __init__(self)`

#### `def __init__(self, code: int)`

#### `def __init__(self, code: ErrorCode)`

#### `def __init__(self, e: System.Exception)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def code(self) -> int`

Gets the error code for the current instance of <see cref="T:NationalInstruments.VeriStand.Error" /> and returns it as an integer.

#### `def message(self) -> str`

Gets the error message and returns it as a string.

#### `def is_error(self) -> bool`

Gets a Boolean value indicating whether the <see cref="T:NationalInstruments.VeriStand.Error" /> object contains an error state.

#### `def resolved_error_message(self) -> str`

Gets the resolved error message. The resolved error message provides error information for non-LabVIEW applications.

#### `def is_defined_error_code(self) -> bool`

Gets a Boolean value indicating whether or not the integer error code is defined in the <see cref="T:NationalInstruments.VeriStand.ErrorCode" /> enumeration.

#### `def error_code(self) -> ErrorCode`

Gets the <see cref="T:NationalInstruments.VeriStand.ErrorCode" /> enumeration for the current <see cref="T:NationalInstruments.VeriStand.Error" />. If the integer error code is not defined in <see cref="T:NationalInstruments.VeriStand.ErrorCode" />, returns the UnexpectedError enumeration.

#### `def to_string(self) -> str`

#### `def to_string(self, *args)`

### `class ErrorCode(_DotNetEnum)`

Defines the types of error codes that NI VeriStand can return.

#### `def __init__(self, *args)`

Create a new instance.

#### `def SUCCESS() -> ErrorCode`

#### `def LAB_VIEW_MATHEMATICS_VI_BRACKET_PROBLEM() -> ErrorCode`

#### `def LAB_VIEW_MATHEMATICS_VI_BEGINNING_BRACKET_PROBLEM() -> ErrorCode`

#### `def LAB_VIEW_MATHEMATICS_VI_END_BRACKET_PROBLEM() -> ErrorCode`

#### `def FILE_VERSION_UNSUPPORTED() -> ErrorCode`

#### `def SERVICE_CONFIGURATION_FILE() -> ErrorCode`

#### `def UNEXPECTED_ERROR() -> ErrorCode`

#### `def FUNCTION_NOT_SUPPORTED() -> ErrorCode`

#### `def FAILED_SERVER_CONNECTION() -> ErrorCode`

#### `def INVALID_FILE() -> ErrorCode`

#### `def NOT_DEPLOYED() -> ErrorCode`

#### `def COMPONENT_NOT_AVAILABLE() -> ErrorCode`

#### `def NO_SYSTEM_DEFINITION_LOADED() -> ErrorCode`

#### `def INVALID_CONFIGURATION_PASSWORD() -> ErrorCode`

#### `def HOST_RUNNING_DIFFERENT_SYSTEM_DEFINITION() -> ErrorCode`

#### `def SYSTEM_DEFINITION_ALREADY_ACTIVE() -> ErrorCode`

#### `def EMPTY_PASSWORD() -> ErrorCode`

#### `def SYSTEM_DEFINITION_DEPLOYMENT_TIMEOUT() -> ErrorCode`

#### `def SYSTEM_DEFINITION_DEPLOYMENT_FAILURE() -> ErrorCode`

#### `def NODE_NOT_FOUND() -> ErrorCode`

#### `def TIMEOUT() -> ErrorCode`

#### `def CHANNEL_NOT_READABLE() -> ErrorCode`

#### `def CHANNEL_NOT_WRITABLE() -> ErrorCode`

#### `def CHANNEL_CANNOT_BE_FAULTED() -> ErrorCode`

#### `def TARGET_INVALID() -> ErrorCode`

#### `def TARGET_DISABLED() -> ErrorCode`

#### `def MODEL_DIMENSION_MISMATCH() -> ErrorCode`

#### `def CHANNEL_MAPPINGS_SIZE_MISMATCH() -> ErrorCode`

#### `def NOT_A_CHANNEL() -> ErrorCode`

#### `def NOT_A_WAVEFORM() -> ErrorCode`

#### `def WAVEFORM_DATA_TYPE_MISMATCH() -> ErrorCode`

#### `def INVALID_STREAM_CONDITION_FOR_DATA_TYPE() -> ErrorCode`

#### `def CHANNEL_NODE_REMOVED() -> ErrorCode`

#### `def NODE_NOT_FOUND_DURING_COMPILE() -> ErrorCode`

#### `def CHANNEL_LENGTH_MISMATCH() -> ErrorCode`

#### `def CHANNEL_NOT_SCALABLE() -> ErrorCode`

#### `def NO_PROJECT_OPEN() -> ErrorCode`

#### `def STIMULUS_PROFILE_SESSION_LOCKED() -> ErrorCode`

#### `def SEQUENCE_NOT_FOUND_IN_SESSION() -> ErrorCode`

#### `def SESSION_NOT_DEPLOYED() -> ErrorCode`

#### `def SESSION_ALREADY_DEPLOYED() -> ErrorCode`

#### `def RTSEQ_PARAMETER_ASSIGNMENT_PARAMETER_DOES_NOT_EXIST() -> ErrorCode`

#### `def BY_REFERENCE_PARAMETER_VALUE_NOT_ASSIGNED() -> ErrorCode`

#### `def SEQUENCE_COMPILE_ERROR() -> ErrorCode`

#### `def RTSEQ_PARAMETER_ASSIGNMENT_INVALID_DATA_TYPE() -> ErrorCode`

#### `def MODEL_PARAMETER_FILE_PARSE_ERROR() -> ErrorCode`

#### `def NUMBER_OF_COEFFICIENTS_OUT_OF_RANGE() -> ErrorCode`

#### `def DUPLICATE_LOG_SESSION_NAME() -> ErrorCode`

#### `def LOG_SESSION_NOT_FOUND() -> ErrorCode`

#### `def NOT_ENOUGH_DYNAMIC_DATA_SHARING_SPACE() -> ErrorCode`

#### `def TARGET_MISSING_DATA_SHARING_DEVICE() -> ErrorCode`

#### `def LOG_TRIGGER_CONDITION_SYNTAX_ERROR() -> ErrorCode`

#### `def SERVER_PORT_ALREADY_IN_USE() -> ErrorCode`

#### `def NOT_AN_INLINE_CUSTOM_DEVICE() -> ErrorCode`

#### `def PARAMETER_NOT_FOUND() -> ErrorCode`

#### `def INVALID_DAQ_PLUGIN_FILE() -> ErrorCode`

#### `def DUPLICATE_CHANNEL_ALIAS_MAPPINGS() -> ErrorCode`

#### `def MISMATCHED_LENGTHS() -> ErrorCode`

#### `def INCOMPATIBLE_MODEL() -> ErrorCode`

#### `def UNSUPPORTED_MODEL_ARCHITECTURE() -> ErrorCode`

#### `def UNSUPPORTED_FMU_KIND() -> ErrorCode`

#### `def NON_POSITIVE_STEP_SIZE() -> ErrorCode`

#### `def UNSUPPORTED_FMI_VERSION() -> ErrorCode`

#### `def UNSUPPORTED_VS_MODEL_VERSION() -> ErrorCode`

#### `def UNMAPPED_ALIAS() -> ErrorCode`

#### `def CANNOT_ADD_VS_MODEL_IN_SYSTEM_EXPLORER() -> ErrorCode`

#### `def CANNOT_ADD_NI_VS_ECU_NW_IN_SYSTEM_EXPLORER() -> ErrorCode`

#### `def EMPTY_NODE_NAME() -> ErrorCode`

#### `def NODE_ALREADY_EXISTS_BY_NAME() -> ErrorCode`

#### `def INPUT_PARAMETER_INVALID() -> ErrorCode`

#### `def NO_ACTION_REQUIRED() -> ErrorCode`

#### `def INCORRECT_LOG_FILE_NAME() -> ErrorCode`

#### `def DOWNLOAD_FILE_ERROR() -> ErrorCode`

#### `def TARGET_DISCONNECTED() -> ErrorCode`

#### `def GATEWAY_NOT_ON_LOCALHOST() -> ErrorCode`

#### `def CHANNEL_GROUP_NOT_FOUND_IN_LOG_FILE() -> ErrorCode`

#### `def CHANNEL_NOT_FOUND_IN_LOG_FILE() -> ErrorCode`

#### `def DEPENDENCIES_CYCLE() -> ErrorCode`

#### `def STI_FILE_ERROR() -> ErrorCode`

#### `def SLSC_CHASSIS_LOAD_FAILED() -> ErrorCode`

#### `def ELECTRICAL_ERROR_NOT_HANDLED() -> ErrorCode`

#### `def MODEL_NOT_FOUND() -> ErrorCode`

#### `def INVALID_SIGNAL_INDEX() -> ErrorCode`

#### `def NOT_SCALAR_SIGNAL() -> ErrorCode`

#### `def TARGET_RUNNING_CONNECTED_TO_A_DIFFERENT_GATEWAY() -> ErrorCode`

#### `def NO_SPACE_TO_DEPLOY_SEQUENCE() -> ErrorCode`

### `class XMLVersionInfo(_DotNetBase)`

Provides and configures version data for an XML file, including the major, minor, fix, and build version of the XML file.

#### `def __init__(self, major: int, minor: int, fix: int, build: int)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def major(self) -> int`

Gets or sets the major version number for the current XML file.

#### `def major(self, value: int)`

Gets or sets the major version number for the current XML file.

#### `def minor(self) -> int`

Gets or sets the minor version number for the current XML file.

#### `def minor(self, value: int)`

Gets or sets the minor version number for the current XML file.

#### `def fix(self) -> int`

Gets or sets the fix number for the current XML file.

#### `def fix(self, value: int)`

Gets or sets the fix number for the current XML file.

#### `def build(self) -> int`

Gets or sets the build number for the current XML file.

#### `def build(self, value: int)`

Gets or sets the build number for the current XML file.

#### `def to_string(self) -> str`

#### `def to_string(self, *args)`

#### `def equals(self, obj: Any) -> bool`

#### `def equals(self, other: XMLVersionInfo) -> bool`

#### `def equals(self, *args)`

#### `def get_hash_code(self) -> int`

#### `def get_hash_code(self, *args)`

#### `def clone(self) -> Any`

#### `def clone(self, *args)`

#### `def compare_to(self, other: Any) -> int`

#### `def compare_to(self, other: XMLVersionInfo) -> int`

#### `def compare_to(self, *args)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_decorators.py -->
## PYTHON MODULE: src/niveristand/_decorators.py

### `def nivs_rt_sequence(func)`

### `class NivsParam()`


    Describes a parameter passed down to a function.

    Args:
        param_name(str): Name of the parameter as it is found in the function definition.
        default_elem: Default value and type. Refer to :ref:`api_datatypes_page` for valid values.
        by_value(bool): Specifies whether to pass a parameter by value or by reference. Set to True to pass by value.
                        Set to False to pass by reference.
                        Refer to :any:`NivsParam.BY_REF` or :any:`NivsParam.BY_VALUE` for details.

    

#### `def __init__(self, param_name, default_elem, by_value)`

#### `def __call__(self, func)`

### `def _set_rtseq_attrs(func, ret_func)`

### `def _reconstruct_args(f, args, new_param)`

### `def task(mt)`


    Marks a nested function-definition as a task inside a :func:`niveristand.library.multitask`.

    Args:
        mt: the parent :func:`niveristand.library.multitask`

    Use this function as a decorator.
    Refer to :func:`niveristand.library.multitask` for more details on using tasks.

    

- `_VALID_DECORATORS = {nivs_rt_sequence.__name__: nivs_rt_sequence, NivsParam.__name__: NivsParam, task.__name__: task}`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_internal.py -->
## PYTHON MODULE: src/niveristand/_internal.py

### `def base_assembly_path()`

### `def _get_install_path()`

### `def _getdevconfig()`

### `def dummy()`


    Do nothing because you're just a dummy.

    This dummy can be used by any module that imports internal to get rid of PEP8 errors about
    an import not being used. This internal module takes care of loading C# references, so most
    times it will only be imported but not actually used.
    

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/assign_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/assign_transformer.py

### `def assign_transformer(node, resources)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/attribute_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/attribute_transformer.py

### `def attribute_transformer(node, resources)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/augassign_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/augassign_transformer.py

### `def augassign_transformer(node, resources)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/binaryoperator_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/binaryoperator_transformer.py

### `def binaryoperator_transformer(node, resources)`

### `def _operator(ast_operator)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/booloperator_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/booloperator_transformer.py

### `def booloperator_transformer(node, resources)`

### `def _operator(ast_operator)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/break_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/break_transformer.py

### `def break_transformer(node, resources)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/call_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/call_transformer.py

### `def call_transformer(node, resources)`

### `def _transform_datatype_non_scalar(node, resources)`

### `def _transform_data_type_scalar(node)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/compareoperator_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/compareoperator_transformer.py

### `def compareoperator_transformer(node, resources)`

### `def _operator(ast_operator)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/constant_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/constant_transformer.py

### `def constant_transformer(node, resources)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/custom_generate_error.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/custom_generate_error.py

### `def custom_generate_error(node, resources)`

### `def _validate_restrictions(node)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/custom_localhost_wait.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/custom_localhost_wait.py

### `def custom_localhost_wait(node, resources)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/custom_math_log.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/custom_math_log.py

### `def custom_math_log(node, resources)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/custom_nivs_yield.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/custom_nivs_yield.py

### `def custom_nivs_yield(node, resources)`

### `def _validate_node()`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/custom_stop_task.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/custom_stop_task.py

### `def custom_stop_task(node, resources)`

### `def _validate_restrictions(node)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/default_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/default_transformer.py

### `def default_transformer(node, resources)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/exp_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/exp_transformer.py

### `def exp_transformer(node, resources)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/for_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/for_transformer.py

### `def for_transformer(node, resources)`

### `def _validate_restrictions(node)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/functiondef_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/functiondef_transformer.py

### `def functiondef_transformer(node, resources)`

### `def _init_args(node, resources)`

### `def _decorator_to_arg(node, resources)`

### `def _validate_restrictions(node)`

### `def _raise_if_invalid_decorator(attribute)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/if_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/if_transformer.py

### `def if_transformer(node, resources)`

### `def _validate_restrictions(node)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/ifexp_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/ifexp_transformer.py

### `def ifexp_transformer(node, resources)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/index_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/index_transformer.py

### `def index_transformer(node, resources)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/list_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/list_transformer.py

### `def list_transformer(node, resources)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/module_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/module_transformer.py

### `def module_transformer(node, resources)`

### `def _has_rtseq_decorator(func_node)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/name_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/name_transformer.py

### `def name_transformer(node, resources)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/nameconstant_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/nameconstant_transformer.py

### `def nameconstant_transformer(node, resources)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/num_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/num_transformer.py

### `def num_transformer(node, resources)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/pass_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/pass_transformer.py

### `def pass_transformer(node, resources)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/return_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/return_transformer.py

### `def return_transformer(node, resources)`

### `def _validate_restrictions(node)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/subscript_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/subscript_transformer.py

### `def subscript_transformer(node, resources)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/transformers.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/transformers.py

- `TRANSFORMERS = {'Default': default_transformer.default_transformer, ast.Assign.__name__: assign_transformer.assign_transformer, ast.Attribute.__name__: attribute_transformer.attribute_transformer, ast.AugAssign.__name__: augassign_transformer.augassign_transformer, ast.BinOp.__name__: binaryoperator_transformer.binaryoperator_transformer, ast.BoolOp.__name__: booloperator_transformer.booloperator_transformer, ast.Break.__name__: break_transformer.break_transformer, ast.Call.__name__: call_transformer.call_transformer, ast.Compare.__name__: compareoperator_transformer.compareoperator_transformer, ast.Expr.__name__: exp_transformer.exp_transformer, ast.For.__name__: for_transformer.for_transformer, ast.FunctionDef.__name__: functiondef_transformer.functiondef_transformer, ast.If.__name__: if_transformer.if_transformer, ast.IfExp.__name__: ifexp_transformer.ifexp_transformer, ast.Index.__name__: index_transformer.index_transformer, ast.List.__name__: list_transformer.list_transformer, ast.Module.__name__: module_transformer.module_transformer, ast.Name.__name__: name_transformer.name_transformer, ast.Pass.__name__: pass_transformer.pass_transformer, ast.Return.__name__: return_transformer.return_transformer, ast.Subscript.__name__: subscript_transformer.subscript_transformer, ast.Try.__name__: try_transformer.try_transformer, ast.UnaryOp.__name__: unaryoperator_transformer.unaryoperator_transformer, ast.While.__name__: while_transformer.while_transformer, ast.With.__name__: with_transformer.with_transformer}`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/try_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/try_transformer.py

### `def try_transformer(node, resources)`

### `def except_transformer(node, resources)`

### `def _validate_restrictions(node)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/unaryoperator_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/unaryoperator_transformer.py

### `def unaryoperator_transformer(node, resources)`

### `def _operator(ast_operator)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/unittests/test_attribute_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/unittests/test_attribute_transformer.py

### `def test_datatype_value_works()`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/unittests/test_functiondef_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/unittests/test_functiondef_transformer.py

### `def functiondef_with_default(i=1)`

### `def functiondef_with_args(*args)`

### `def functiondef_with_kwargs(**kwargs)`

### `def functiondef_nested()`

### `def invalid_decorator(func)`

### `class InvalidDecoratorClass()`

#### `def __call__(self, f)`

#### `def invalid_decorator_as_attribute(func)`

### `def functiondef_invalid_decorator()`

### `def functiondef_invalid_decorator2()`

### `def functiondef_invalid_decorator3()`

### `def idfunc(val)`

### `def test_functiondef_transformer_fails(func)`

### `def _fail_function_helper(func)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/unittests/test_nameconstant_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/unittests/test_nameconstant_transformer.py

### `def test_true_node_returns_true_string()`

### `def test_false_node_returns_false_string()`

### `def test_none_node_throws()`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/utils.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/utils.py

### `class Resources()`

#### `def __init__(self, rtseq, alias)`

#### `def get_rtseq(self)`

#### `def set_current_block(self, block)`

#### `def get_current_block(self)`

#### `def add_variable(self, py_name, py_value, rtseq_name)`

#### `def has_variable(self, variable_name)`

#### `def get_variable_rtseq_name(self, variable_name)`

#### `def get_variable_py_name(self, rtseq_var_name)`

#### `def get_variable_py_value(self, variable_name)`

#### `def add_referenced_sequence(self, referenced)`

#### `def get_dependency_pkg(self)`

#### `def set_dependency_pkg(self, pkg)`

#### `def add_channel_ref(self, variable_name, channel_name, rtseq_var_name, channel_is_vector)`

#### `def has_channel_ref(self, rtseq_name)`

#### `def get_channel_ref_rtseq_name_from_channel_name(self, channel_name)`

#### `def get_all_channel_refs(self)`

#### `def add_parameter(self, param_name, default_value, by_value)`

#### `def get_parameters(self)`

#### `def update_parameter(self, param_name, default_value, by_value)`

### `def _py_param_name_to_rtseq_param_name(name)`

### `class _Variable()`

#### `def __init__(self, py_value, rtseq_name)`

### `class _Parameter()`

#### `def __init__(self, rtseq_name, default_value, by_value)`

### `class _ChannelReference()`

#### `def __init__(self, channel_name, rtseq_name, channel_is_vector)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/validations.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/validations.py

### `def raise_if_try_in_node_body(statements)`

### `def ast_try()`

### `def check_if_any_in_block(ast_node, block)`

### `def check_if_looks_like_doc_block(node)`

### `def raise_if_invalid_bool_operand(node, resources)`

### `def raise_if_invalid_if_test(node)`

### `def raise_if_invalid_invert_operand(node, resources)`

### `def raise_if_negative_binary_operator_operand(node, resources)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/while_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/while_transformer.py

### `def while_transformer(node, resources)`

### `def _validate_restrictions(node, resources)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/py2rtseq/with_transformer.py -->
## PYTHON MODULE: src/niveristand/_translation/py2rtseq/with_transformer.py

### `def with_transformer(node, resources)`

### `def _validate_multitask(node)`

### `def _validate_task(node, mt_name)`

### `def _get_name_without_namespace_from_node(node)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/unittests/test_is_node_ast_nameconstant.py -->
## PYTHON MODULE: src/niveristand/_translation/unittests/test_is_node_ast_nameconstant.py

### `def test_str_0_check_returns_false_bool()`

### `def test_str_1_check_returns_false_bool()`

### `def test_str_true_check_returns_false_bool()`

### `def test_str_false_check_returns_false_bool()`

### `def test_str_none_check_returns_false_bool()`

### `def test_str_empty_check_returns_false_bool()`

### `def test_int_0_check_returns_false_bool()`

### `def test_int_1_check_returns_false_bool()`

### `def test_float_0_check_returns_false_bool()`

### `def test_float_1_check_returns_false_bool()`

### `def test_complex_1_check_returns_false_bool()`

### `def test_complex_2_3_check_returns_false_bool()`

### `def test_true_check_returns_true_bool()`

### `def test_false_check_returns_true_bool()`

### `def test_none_check_returns_true_bool()`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/unittests/test_is_node_ast_num.py -->
## PYTHON MODULE: src/niveristand/_translation/unittests/test_is_node_ast_num.py

### `def test_true_check_returns_false_bool()`

### `def test_false_check_returns_false_bool()`

### `def test_none_check_returns_false_bool()`

### `def test_str_0_check_returns_false_bool()`

### `def test_str_1_check_returns_false_bool()`

### `def test_str_true_check_returns_false_bool()`

### `def test_str_false_check_returns_false_bool()`

### `def test_str_none_check_returns_false_bool()`

### `def test_str_empty_check_returns_false_bool()`

### `def test_int_0_check_returns_true_bool()`

### `def test_int_1_check_returns_true_bool()`

### `def test_float_0_check_returns_true_bool()`

### `def test_float_1_check_returns_true_bool()`

### `def test_complex_1_check_returns_true_bool()`

### `def test_complex_2_3_check_returns_true_bool()`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/unittests/test_is_node_ast_str.py -->
## PYTHON MODULE: src/niveristand/_translation/unittests/test_is_node_ast_str.py

### `def test_true_check_returns_false_bool()`

### `def test_false_check_returns_false_bool()`

### `def test_none_check_returns_false_bool()`

### `def test_int_check_returns_false_bool()`

### `def test_float_check_returns_false_bool()`

### `def test_str_true_check_returns_true_bool()`

### `def test_str_false_check_returns_true_bool()`

### `def test_str_none_check_returns_true_bool()`

### `def test_str_0_check_returns_true_bool()`

### `def test_str_1_check_returns_true_bool()`

### `def test_str_empty_check_returns_true_bool()`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/_translation/utils.py -->
## PYTHON MODULE: src/niveristand/_translation/utils.py

### `def generic_ast_node_transform(node, resources)`

### `def get_value_from_node(node, resources)`

### `def get_element_value(node)`

### `def get_variable_name_from_node(node)`

### `def get_channel_name(node)`

### `def is_node_ast_str(node)`

### `def is_node_ast_num(node)`

### `def is_node_ast_nameconstant(node)`

### `def get_value_from_str_node(node)`

### `def get_value_from_num_node(node)`

### `def get_value_from_nameconstant_node(node)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/clientapi/__init__.py -->
## PYTHON MODULE: src/niveristand/clientapi/__init__.py

- `__all__ = ['BooleanValue', 'BooleanValueArray', 'ChannelReference', 'DoubleValue', 'DoubleValueArray', 'I32Value', 'I32ValueArray', 'I64Value', 'I64ValueArray', 'U32Value', 'U32ValueArray', 'U64Value', 'U64ValueArray', 'VectorChannelReference', 'ErrorAction', 'RealTimeSequence', 'StimulusProfileState']`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/clientapi/_datatypes/__init__.py -->
## PYTHON MODULE: src/niveristand/clientapi/_datatypes/__init__.py

- `__all__ = ['ArrayType', 'BooleanValue', 'BooleanValueArray', 'ChannelReference', 'VectorChannelReference', 'DataType', 'DoubleValue', 'DoubleValueArray', 'I32Value', 'I32ValueArray', 'I64Value', 'I64ValueArray', 'U32Value', 'U32ValueArray', 'U64Value', 'U64ValueArray', 'VALID_TYPES']`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/clientapi/_datatypes/rtprimitives.py -->
## PYTHON MODULE: src/niveristand/clientapi/_datatypes/rtprimitives.py

### `def get_class_by_name(name)`

### `def is_supported_data_type(name)`

### `def is_supported_return_type(name)`

### `def is_scalar_type(name)`

### `def is_array_type(name)`

### `def is_channel_ref_type(name)`

### `class DataType(object)`


    Use as base class for all VeriStand datatypes.

    Args:
        value: initial value. Note: Actual value and type depends on subclass.
        description(str): a description of the value. For documentation purposes only.
        units(str): units represented by this value. For documentation purposes only.

    Raises:
        :class:`TypeError`: if an invalid value is used to initialize an instance.

    This class is not meant to be instantiated.

    

#### `def __init__(self, value, description='', units='')`

#### `def __str__(self)`

#### `def _to_data_value(self, value)`

#### `def _is_compatible_with_datatype(other)`

#### `def _is_integer_type(other)`

#### `def _is_valid_assign_type(other)`

#### `def __add__(self, other)`

#### `def __radd__(self, other)`

#### `def __sub__(self, other)`

#### `def __rsub__(self, other)`

#### `def __mul__(self, other)`

#### `def __rmul__(self, other)`

#### `def __divmod__(self, other)`

#### `def __rdivmod__(self, other)`

#### `def __floordiv__(self, other)`

#### `def __rfloordiv__(self, other)`

#### `def __truediv__(self, other)`

#### `def __rtruediv__(self, other)`

#### `def __div__(self, other)`

#### `def __rdiv__(self, other)`

#### `def __pow__(self, power, modulo=None)`

#### `def __rpow__(self, other)`

#### `def __mod__(self, other)`

#### `def __rmod__(self, other)`

#### `def __and__(self, other)`

#### `def __rand__(self, other)`

#### `def __or__(self, other)`

#### `def __ror__(self, other)`

#### `def __xor__(self, other)`

#### `def __rxor__(self, other)`

#### `def __lshift__(self, other)`

#### `def __rlshift__(self, other)`

#### `def __rshift__(self, other)`

#### `def __rrshift__(self, other)`

#### `def __eq__(self, other)`

#### `def __ne__(self, other)`

#### `def __gt__(self, other)`

#### `def __ge__(self, other)`

#### `def __lt__(self, other)`

#### `def __inv__(self)`

#### `def __invert__(self)`

#### `def __le__(self, other)`

#### `def value(self)`

#### `def value(self, newvalue)`

### `class ArrayType(DataType)`

#### `def _to_data_value(self, value)`

#### `def __getitem__(self, key)`

#### `def __setitem__(self, key, value)`

### `class ChannelReference(DataType)`


    Creates a new scalar channel reference.

    Creates a new reference to a scalar channel and specifies which channel assignment to map the new channel reference
    to. You can specify a channel by its alias or by the path to the channel in the system definition. For example:
    Targets/Controller/System Channels/Model Count.
    

#### `def __init__(self, value, description='', units='')`

#### `def value(self)`

#### `def value(self, newvalue)`

#### `def _to_data_value(self, value)`

### `class VectorChannelReference(ArrayType)`


    Creates a new vector channel reference.

    Creates a new reference to a vector channel and specifies which channel assignment to map the new channel reference
    to. You can specify a channel by its alias or by the path to the channel in the system definition. For example:
    Targets/Controller/System Channels/Model Count.
    

#### `def value(self)`

#### `def _to_data_value(self, value)`

#### `def __getitem__(self, key)`

### `class BooleanValue(DataType)`

Creates a new boolean value reference.

#### `def _to_data_value(self, value)`

### `class BooleanValueArray(ArrayType)`

Creates a new reference to an array of :class:`BooleanValue`.

#### `def value(self)`

#### `def _to_data_value(self, value)`

### `class DoubleValue(DataType)`

Creates a new floating-point value reference.

#### `def _to_data_value(self, value)`

### `class DoubleValueArray(ArrayType)`

Creates a new reference to an array of :class:`DoubleValue`.

#### `def value(self)`

#### `def _to_data_value(self, value)`

### `class I32Value(DataType)`

Creates a new, signed 32-bit integer value reference.

#### `def _to_data_value(self, value)`

### `class I32ValueArray(ArrayType)`

Creates a new reference to an array of :class:`I32Value`.

#### `def value(self)`

#### `def _to_data_value(self, value)`

### `class I64Value(DataType)`

Creates a new, signed 64-bit integer value reference.

#### `def _to_data_value(self, value)`

### `class I64ValueArray(ArrayType)`

Creates a new reference to an array of :class:`I64Value`.

#### `def value(self)`

#### `def _to_data_value(self, value)`

### `class U32Value(DataType)`

Creates a new, unsigned 32-bit integer value reference.

#### `def _to_data_value(self, value)`

### `class U32ValueArray(ArrayType)`

Creates a new reference to an array of :class:`U32Value`.

#### `def value(self)`

#### `def _to_data_value(self, value)`

### `class U64Value(DataType)`

Creates a new, unsigned 64-bit integer value reference.

#### `def _to_data_value(self, value)`

### `class U64ValueArray(ArrayType)`

Creates a new reference to an array of :class:`U64Value`.

#### `def value(self)`

#### `def _to_data_value(self, value)`

- `VALID_TYPES = {ArrayType.__name__: ArrayType, BooleanValue.__name__: BooleanValue, BooleanValueArray.__name__: BooleanValueArray, ChannelReference.__name__: ChannelReference, DoubleValue.__name__: DoubleValue, DoubleValueArray.__name__: DoubleValueArray, I32Value.__name__: I32Value, I32ValueArray.__name__: I32ValueArray, I64Value.__name__: I64Value, I64ValueArray.__name__: I64ValueArray, U32Value.__name__: U32Value, U32ValueArray.__name__: U32ValueArray, U64Value.__name__: U64Value, U64ValueArray.__name__: U64ValueArray, VectorChannelReference.__name__: VectorChannelReference}`

- `VALID_RETURN_TYPES = {BooleanValue.__name__: BooleanValue, DoubleValue.__name__: DoubleValue, I32Value.__name__: I32Value, I64Value.__name__: I64Value, U32Value.__name__: U32Value, U64Value.__name__: U64Value}`

- `VALID_ARRAY_TYPES = {BooleanValueArray.__name__: BooleanValueArray, DoubleValueArray.__name__: DoubleValueArray, I32ValueArray.__name__: I32ValueArray, I64Value.__name__: I64ValueArray, U32ValueArray.__name__: U32ValueArray, U64ValueArray.__name__: U64ValueArray, VectorChannelReference.__name__: VectorChannelReference}`

- `CHANNEL_REF_TYPES = {ChannelReference.__name__: ChannelReference, VectorChannelReference.__name__: VectorChannelReference}`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/clientapi/_dotnetclasswrapperbase.py -->
## PYTHON MODULE: src/niveristand/clientapi/_dotnetclasswrapperbase.py

### `class _DotNetClassWrapperBase(object)`



    The base class for all the classes that wrap around a VeriStand public api C# class.

    Args:
        dot_net_instance (): a C# instance of the wrapped C# class.

    

#### `def __init__(self, dot_net_instance)`

#### `def dot_net_instance(self)`


        Gets the C# instance of the wrapped C# class.

        Returns:
            (): The C# instance of the wrapped C# class

        

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/clientapi/_error.py -->
## PYTHON MODULE: src/niveristand/clientapi/_error.py

### `class _Error(_DotNetClassWrapperBase)`



    Represents NI VeriStand error information, including an integer error code and a string error message.

    Args:
        dot_net_instance (NationalInstruments.VeriStand.Error):  the C# instance to wrap around.

    

#### `def __init__(self, dot_net_instance)`

#### `def error_code(self)`


        Gets the VeriStand specific ErrorCode.

        Returns:
            (int): the VeriStand specific error code

        

#### `def is_error(self)`


        Gets a Boolean value indicating whether the Error object contains an error state.

        Returns:
            (bool): True if the Error contains an error state.

        

#### `def resolved_error_message(self)`


        Gets the resolved error message.

        The resolved error message provides error information for non-LabVIEW applications.

        Returns:
            (str): The resolved error message for the current Error.

        

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/clientapi/_factory.py -->
## PYTHON MODULE: src/niveristand/clientapi/_factory.py

### `class _Factory(_DotNetClassWrapperBase)`


    Provides access to the NI VeriStand system and the various interfaces available in the Execution API.

    Any code you write using this API must include a Factory constructor to access NI VeriStand.

    

#### `def __init__(self)`

#### `def get_existing_stimulus_profile_session(self, gateway_ip_address, session_id)`


        Gets an instance that implements StimulusProfileSession interface.

        The instance can be used to automate the execution of an already deployed Stimulus Profile Session.

        Args:
            gateway_ip_address(str): Specifies the IP address of the VeriStand Gateway.
            session_id(str): Specifies the Session ID of the deployed Stimulus Profile Session.

        Returns:
            niveristand.clientapi._stimulusprofilesession._StimulusProfileSession : A StimulusProfileSession instance

        

#### `def get_new_stimulus_profile_session(self, gateway_ip_address, name, sequences, description)`


        Gets an instance that implements StimulusProfileSession interface.

        The instance can be used to automate the execution of an already deployed Stimulus Profile Session.

        Args:
            gateway_ip_address(str): Specifies the IP address of the VeriStand Gateway.
            name(str): Specifies the name of the Stimulus Profile Session.
            sequences([niveristand.clientapi._sequencecallinfo._SequenceCallInfo]): Specifies the sequences to execute
             in the Stimulus Profile Session.
            description(str): Specifies a description for the Stimulus Profile Session.

        Returns:
            niveristand.clientapi._stimulusprofilesession._StimulusProfileSession : A StimulusProfileSession instance.

        

#### `def get_workspace2(self, gateway_ip_address)`


        Gets an instance that implements the Workspace2 interface.

        The instance can be used use to manage connections between the VeriStand Gateway and one or more targets,
         to start and stop data logging operations, and to configure events for error and status notifications.
          This method allows you to specify the IP address of the VeriStand Gateway.

        Args:
            gateway_ip_address (str): Specifies the IP address of the VeriStand Gateway.

        Returns:
            niveristand.clientapi._workspace2._Workspace2: A Workspace2 instance.

        

#### `def get_localhost_workspace2(self)`


        Gets an instance that implements the Workspace2 interface.

        The instance can be used to manage connections between the VeriStand Gateway and one or more targets, to start
         and stop data logging operations, and to configure events for error and status notifications. This method
         assumes that the VeriStand Gateway is running on the localhost.

        Returns:
            niveristand.clientapi._workspace2._Workspace2: A Workspace2 instance.

        

### `class _DefaultGatewayFactory(object)`


    Provides access to the NI VeriStand system and the various interfaces available in the Execution API.

    All the instances that are created by this class are using the gateway at a default ip address. Any code you write
     using this API must include a Factory constructor to access NI VeriStand.

    

#### `def set_default_gateway_ip_address(cls, gateway_ip_address)`


        Sets the default ip address of the gateway.

        This ip address is to be used by work sessions that do not explicitly specify it for every operation.

        Args:
            gateway_ip_address (str): The default ip address of the VeriStand gateway.

        

#### `def get_default_gateway_ip_address(cls)`


        Gets the default ip address of the gateway.

        This ip address is to be used by default by work sessions that do not explicitly specify it for every operation.

        Returns:
            str: The default ip adderess of the VeriStand gateway.

        

#### `def get_new_stimulus_profile_session(cls, name, sequences, description)`


        Gets an instance that implements StimulusProfileSession interface.

        The instance can be used to automate the execution of an already deployed Stimulus Profile Session.

        Args:
            name(str): Specifies the name of the Stimulus Profile Session.
            sequences([niveristand.clientapi._sequencecallinfo._SequenceCallInfo]): Specifies the sequences to execute
             in the Stimulus Profile Session.
            description(str): Specifies a description for the Stimulus Profile Session.

        Returns:
            niveristand.clientapi._stimulusprofilesession._StimulusProfileSession : A StimulusProfileSession instance.

        

#### `def get_workspace2(cls)`


        Gets an instance that implements the Workspace2 interface.

        The instance can be used use to manage connections between the VeriStand Gateway and one or more targets,
         to start and stop data logging operations, and to configure events for error and status notifications.
          This method allows you to specify the IP address of the VeriStand Gateway.

        Returns:
            niveristand.clientapi._workspace2._Workspace2: A Workspace2 instance.

        

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/clientapi/_nodeinfo.py -->
## PYTHON MODULE: src/niveristand/clientapi/_nodeinfo.py

### `class _NodeInfo(_DotNetClassWrapperBase)`


    Provides information about and configures a node in the system definition file.

    Args:
        dot_net_instance (NationalInstruments.VeriStand.ClientAPI.NodeInfo): the C# instance to wrap around.

    

#### `def __init__(self, dot_net_instance)`

#### `def channel_row_dimension(self)`


        Gets the number of rows in a channel node value.

        Returns:
            int: The number of rows in a channel node value.

        

#### `def channel_column_dimension(self)`


        Gets the number of columns in a channel node value.

        Returns:
            int: The number of columns in a channel node value.

        

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/clientapi/_realtimesequencedefinitionapi/erroraction.py -->
## PYTHON MODULE: src/niveristand/clientapi/_realtimesequencedefinitionapi/erroraction.py

### `class ErrorAction(Enum)`

Actions you can take when calling :func:`niveristand.library.generate_error`.

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/clientapi/_sequencecallinfo.py -->
## PYTHON MODULE: src/niveristand/clientapi/_sequencecallinfo.py

### `class _SequenceCallInfoFactory(object)`

Factory class to create niveristand.clientapi._sequencecallinfo._SequenceCallInfo instances.

#### `def __init__(self)`

#### `def create(sequence_path, target, parameters, debug, timeout)`


        Creates an instance of niveristand.clientapi._sequencecallinfo._SequenceCallInfo class.

        Args:
            sequence_path (str): The file path of the sequence file to execute.
            target (str): The name of the target on which to execute the sequence.
            parameters (list[niveristand.clientapi._sequenceparameterassignmentinfo._SequenceParameterAssignmentInfo]):
             The parameter assignments for the sequence.
            debug (bool): Whether the sequence executes in debug mode.
            timeout (float): The timeout in milliseconds within which the sequence must complete each time step.

        Returns:
            niveristand.clientapi._sequencecallinfo._SequenceCallInfo: Newly created instance.

        

### `class _SequenceCallInfo(_DotNetClassWrapperBase)`


    Provides information about a stimulus profile sequence.

    Args:
        dot_net_instance (NationalInstruments.VeriStand.ClientAPI.SequenceCallInfo): the C# instance to wrap around.

    

#### `def __init__(self, dot_net_instance)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/clientapi/_sequenceparameterassignmentinfo.py -->
## PYTHON MODULE: src/niveristand/clientapi/_sequenceparameterassignmentinfo.py

### `class _SequenceParameterAssignmentInfoFactory(object)`


    Factory class.

    Creates niveristand.clientapi._sequenceparameterassignmentinfo._SequenceParameterAssignmentInfo instances.

    

#### `def __init__(self)`

#### `def create(parameter_name, value)`


        Creates an instance.

        The instance is of type niveristand.clientapi._sequenceparameterassignmentinfo._SequenceParameterAssignmentInfo.

        Args:
            parameter_name (): The name of the parameter.
            value (niveristand.clientapi.DataType): The value of the parameter.

        Returns:
            niveristand.clientapi._sequenceparameterassignmentinfo._SequenceParameterAssignmentInfo: Newly created
             instance.

        

### `class _SequenceParameterAssignmentInfo(_DotNetClassWrapperBase)`


    Provides information about an input parameter of a real-time sequence.

    Args:
        dot_net_instance (NationalInstruments.VeriStand.ClientAPI.SequenceParameterAssignmentInfo): the C# instance to
         wrap around.

    

#### `def __init__(self, dot_net_instance)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/clientapi/_stimulusprofilesession.py -->
## PYTHON MODULE: src/niveristand/clientapi/_stimulusprofilesession.py

### `class _StimulusProfileSession(_DotNetClassWrapperBase)`


    Interface to control and monitor Stimulus Profile Session execution.

    Args:
        dot_net_instance (NationalInstruments.VeriStand.ClientAPI.StimulusProfileSessionImpl): the C# instance to wrap.
         around.

    

#### `def __init__(self, dot_net_instance)`

#### `def __getitem__(self, item)`


        Gets a reference to the sequence specified by the qualified sequence name in the Stimulus Profile Session.

        Args:
            item (str): The sequence for which to get the reference.

        Returns:
            niveristand.clientapi._stimulusprofilesession._SequenceControl: Sequence control reference.

        

#### `def deploy(self, auto_start)`


        Deploys the Stimulus Profile Session.

        Args:
            auto_start (bool): If True, starts sequences immediately upon deploy. If False, waits for an external Run
             command.

        Returns:
            str: The ID of the Stimulus profile session.

        

#### `def undeploy(self)`


        Undeploys the Stimulus Profile Session.

        Returns:
            None:

        

### `class _SequenceControl(_DotNetClassWrapperBase)`


    Automates and monitors the execution of a sequence in a stimulus profile session.

    Args:
        dot_net_instance (NationalInstruments.VeriStand.ClientAPI.SequenceControl): the C# instance to wrap.

    

#### `def __init__(self, dot_net_instance)`

#### `def register_sequence_complete_event_handler(self, handler)`


        Register callback for when a sequence completes execution.

        Args:
            handler (method): The callback function.

        Returns:
            None:

        

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/clientapi/_systemdefinitionchannelresource.py -->
## PYTHON MODULE: src/niveristand/clientapi/_systemdefinitionchannelresource.py

### `class _SystemDefinitionChannelResourceFactory(object)`


    Factory class.

    Creates niveristand.clientapi._systemdefinitionchannelresource._SystemDefinitionChannelResource instances.

    

#### `def __init__(self)`

#### `def create(channel)`


        Creates an instance.

        The instance is of type niveristand.clientapi._systemdefinitionchannelresource._SystemDefinitionChannelResource.

        Args:
            channel (str): The channel to map the data resource to in the system definition file.

        Returns:
            niveristand.clientapi._systemdefinitionchannelresource._SystemDefinitionChannelResource: The newly created
             instance.

        

### `class _SystemDefinitionChannelResource(_DotNetClassWrapperBase)`


    Represents a data resource mapped to a system definition channel.

    Args:
        dot_net_instance (NationalInstruments.VeriStand.ClientAPI.SystemDefinitionChannelResource): the C# instance to
         wrap around.

    

#### `def __init__(self, dot_net_instance)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/clientapi/_workspace2.py -->
## PYTHON MODULE: src/niveristand/clientapi/_workspace2.py

### `class _Workspace2(_DotNetClassWrapperBase)`


    Class to perform basic workspace operations, such as getting, setting, and logging channel data.

    Args:
        dot_net_instance (NationalInstruments.VeriStand.ClientAPI.WorkspaceImpl): the C# instance to wrap around.

    

#### `def __init__(self, dot_net_instance)`

#### `def get_channel_vector_values(self, channel)`


        Gets the vector values of a channel on the target.

        Args:
            channel (): The name of the channel. You must enter the full path to the channel as specified in the system
             definition file.

        Returns:
            int: The number of rows in the vector array.
            int: The number of columns in the vector array.
            [float]: The vector values.

        

#### `def get_multiple_system_nodes_data(self, names)`


        Gets information about multiple nodes in the system definition file.

        Args:
            names ([str]): The names of the nodes. You must enter the full path to each node as specified in the system
             definition file.

        Returns:
            niveristand.clientapi._nodeinfo._NodeInfo: Information about the nodes.

        

#### `def get_single_channel_value(self, name)`


        Gets the value of a single channel on the target.

        Args:
            name (str): The name of the channel. You must enter the full path to the channel as specified in the system
             definition file.

        Returns:
            float: The value of the specified channel.

        

#### `def set_channel_vector_values(self, channel, new_values)`


        Sets the vector values of a channel on the target.

        Args:
            channel (str): The name of the channel. You must enter the full path to the channel as specified in the
             system definition file.
            new_values (List[float]): The vector values. This parameter expects a 1D array. If the channel expects
             two-dimensional data, convert the 2D channel data into a 1D array before passing it to this method.

        

#### `def set_single_channel_value(self, name, new_val)`


        Sets the value of a single channel on the target.

        Args:
            name (str): The name of the channel. You must enter the full path to the channel as specified in the system
             definition file.
            new_val (float): The value to set.

        Returns:
            None:

        

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/clientapi/realtimesequence.py -->
## PYTHON MODULE: src/niveristand/clientapi/realtimesequence.py

### `class RealTimeSequence()`


    A real-time sequence that can run on the VeriStand Engine.

    Args:
        top_level_func: the function to transform.
        rtseq_pkg(:class:`RealTimeSequencePackage`): the containing package in case you want to add this sequence to a
                                                    library.
        target: The name of the target on which to deploy or run the real-time sequence.
         If None, the default target is used.

    Raises:
        :class:`niveristand.errors.TranslateError`: if translation fails.
        :class:`niveristand.errors.VeristandError`: if compilation fails.

    

#### `def __init__(self, top_level_func, rtseq_pkg=None, target=None)`

#### `def run(self, rtseq_params={})`


        Runs the sequence on the globally configured VeriStand Engine.

        Args:
            rtseq_params (Dict[str, niveristand.clientapi._datatypes.rtprimitives.DoubleValue]):  the parameters to be
             passed to the RT sequence.

        Returns:
            niveristand.clientapi.stimulusprofileapi.StimulusProfileState: Stimulus profile session state.

        Deploys and runs the sequence without waiting for the sequence to finish. Use the returned
        :class:`StimulusProfileState` to wait for the sequence to complete and obtain the return value.

        For a simpler use case, refer to :func:`niveristand.realtimesequencetools.run_py_as_rtseq`

        

#### `def save(self, path=None)`


        Saves this sequence to disk.

        Args:
            path(Optional[str]): path to the location you want to save the sequence file.

        Returns:
            path you specify in **path**.

        All dependencies required for deployment of this sequence save to the same path.
        If you do not specify a path in **path**, this sequence saves to the location where you last saved the object.
        If you did not previously save the object, it saves to a temporary folder.

        For a simpler use case, refer to :func:`niveristand.realtimesequencetools.save_py_as_rtseq`

        

#### `def _transform(self)`

#### `def _update_references(self)`

#### `def _update_parameters(self, param_list)`

#### `def _update_channel_refs(self, channel_ref_list)`

#### `def _build_file_name(self)`

#### `def get_reference(self)`

#### `def __str__(self)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/clientapi/realtimesequencedefinition.py -->
## PYTHON MODULE: src/niveristand/clientapi/realtimesequencedefinition.py

### `def add_local_variable(rt_seq, name, value)`

### `def add_assignment(block, dest_name, source_name)`

### `def add_expression(block, expression)`

### `def add_yield(block)`

### `def add_if_else(block, test_condition)`

### `def add_for_loop(block, loop_variable, iterations)`

### `def add_foreach_loop(block, loop_variable, iterations)`

### `def add_while(block, test_condition)`

### `def add_multi_task(block)`

### `def add_task(multi_task, name)`

### `def create_real_time_sequence()`

### `def add_return_variable(rtseq, name, default_value)`

### `def add_generate_error(block, code, message, action)`

### `def add_stop_task(block, taskname)`

### `def save_real_time_sequence(rtseq, filepath)`

### `def _create_unique_lv_name(name)`

### `def to_channel_ref_name(name)`

### `def _get_channel_node_info(name, node_info_list)`

### `def run_rt_sequence(rt_sequence_path, rtseq_params, target=None)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/clientapi/realtimesequencepkg.py -->
## PYTHON MODULE: src/niveristand/clientapi/realtimesequencepkg.py

### `class RealTimeSequencePkg(collections.abc.MutableMapping)`

#### `def __init__(self)`

#### `def save_all(self, path)`

#### `def save_referenced(self, path, referencer)`

#### `def add_referenced_sequence(self, referencer, referenced_sequence)`

#### `def get_referenced(self, referencer)`

#### `def __len__(self)`

#### `def __getitem__(self, item)`

#### `def _obj_to_key(self, item)`

#### `def _try_resolve(self, item)`

#### `def __contains__(self, item)`

#### `def append(self, new)`

#### `def count(self)`

#### `def __iter__(self)`

#### `def __setitem__(self, key, value)`

#### `def __delitem__(self, key)`

#### `def __reversed__(self)`

#### `def __index__(self)`

#### `def extend(self)`

#### `def insert(self)`

#### `def pop(self, key, default=object())`

#### `def remove(self)`

#### `def sort(self)`

#### `def __add__(self, other)`

#### `def __radd__(self, other)`

#### `def __iadd__(self, other)`

#### `def __mul__(self, other)`

#### `def __imul__(self, other)`

#### `def __rmul__(self, other)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/clientapi/rtsequencedefinitionutils.py -->
## PYTHON MODULE: src/niveristand/clientapi/rtsequencedefinitionutils.py

### `def compile_rtseq(rtseq)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/clientapi/stimulusprofileapi.py -->
## PYTHON MODULE: src/niveristand/clientapi/stimulusprofileapi.py

### `class StimulusProfileState(object)`

Contains the execution state of a real-time sequence.

#### `def __init__(self, session)`

#### `def last_error(self)`


        Returns the last error generated by the sequence.

        Returns:
            :class:`niveristand.errors.SequenceError`: final error the sequence generated.

        

#### `def ret_val(self)`


        Returns the return value of the sequence.

        Returns:
            (bool, int, float): the return value of the sequence.

        

#### `def completion_state(self)`


        Returns the state after running.

        Returns:
            :class:`CompletionState`: state after the operation runs to completion. `None` if unfinished.

        

#### `def session(self)`


        Returns the session you created to execute this sequence.

        Returns:
            a session connected to the VeriStand Engine.

        

#### `def _sequence_complete_event_handler(self, source, args)`

#### `def wait_for_result(self)`


        Waits for the sequence to finish running.

        Returns:
            the value returned by the VeriStand Engine after this sequence runs.

        

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/customdevice/__init__.py -->
## PYTHON MODULE: src/niveristand/customdevice/__init__.py

### MODULE DOCSTRING

Module for NationalInstruments.VeriStand.CustomDevice.

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/customdevice/_auto_generated_classes.py -->
## PYTHON MODULE: src/niveristand/customdevice/_auto_generated_classes.py

### MODULE DOCSTRING

Module for NationalInstruments.VeriStand.CustomDevice.

### `class _staticproperty(staticmethod)`

#### `def __get__(self, *_)`

### `class _DotNetBase()`

#### `def __eq__(self, other) -> bool`

#### `def __repr__(self) -> str`

#### `def _custom_repr(self) -> str`

### `class _DotNetEnum(_DotNetBase)`

#### `def __repr__(self) -> str`

#### `def __str__(self) -> str`

#### `def __int__(self) -> int`

### `def _is_iterable(arg: Any) -> bool`

### `def _unwrap(out_params: Dict[Optional[Tuple[str, ...]], Tuple[int, Any]], *args: Tuple[Any]) -> Iterable[Any]`

### `def _wrap(one_or_many_args: Union[Any, Tuple[Any]]) -> Union[Any, Tuple[Any]]`

### `class PathType(_DotNetEnum)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def ABSOLUTE() -> PathType`

#### `def TO_BASE() -> PathType`

#### `def TO_COMMON_DOC_DIR() -> PathType`

#### `def TO_APPLICATION_DATA_DIR() -> PathType`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/daqplugin/__init__.py -->
## PYTHON MODULE: src/niveristand/daqplugin/__init__.py

### MODULE DOCSTRING

Module for NationalInstruments.VeriStand.DAQPlugin.

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/daqplugin/_auto_generated_classes.py -->
## PYTHON MODULE: src/niveristand/daqplugin/_auto_generated_classes.py

### MODULE DOCSTRING

Module for NationalInstruments.VeriStand.DAQPlugin.

### `class _staticproperty(staticmethod)`

#### `def __get__(self, *_)`

### `class _DotNetBase()`

#### `def __eq__(self, other) -> bool`

#### `def __repr__(self) -> str`

#### `def _custom_repr(self) -> str`

### `class _DotNetEnum(_DotNetBase)`

#### `def __repr__(self) -> str`

#### `def __str__(self) -> str`

#### `def __int__(self) -> int`

### `def _is_iterable(arg: Any) -> bool`

### `def _unwrap(out_params: Dict[Optional[Tuple[str, ...]], Tuple[int, Any]], *args: Tuple[Any]) -> Iterable[Any]`

### `def _wrap(one_or_many_args: Union[Any, Tuple[Any]]) -> Union[Any, Tuple[Any]]`

### `class ValueDataType(_DotNetEnum)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def STRING() -> ValueDataType`

#### `def ENUM() -> ValueDataType`

#### `def DOUBLE() -> ValueDataType`

#### `def U64() -> ValueDataType`

#### `def U32() -> ValueDataType`

#### `def U16() -> ValueDataType`

#### `def I64() -> ValueDataType`

#### `def I32() -> ValueDataType`

#### `def I16() -> ValueDataType`

#### `def BOOLEAN() -> ValueDataType`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/errors.py -->
## PYTHON MODULE: src/niveristand/errors.py

### `class VeristandError(Exception)`


    The base class for all VeriStandErrors.

    Note: This class generates a :class:`VeristandError` if a more specific error cannot be determined.
    

### `class TranslateError(VeristandError)`

Raised if a Python function fails to translate to a VeriStand real-time sequence.

### `class UnexpectedError(VeristandError)`

Raised if the state of the operation can not be determined.

### `class VeristandNotImplementedError(VeristandError)`

Raised to indicate this functionality is not yet available.

#### `def __init__(self)`

Throw Generic exception for things that are not implemented yet.

### `class _StopTaskException(Exception)`

### `class RunError(VeristandError)`

Raised at the end of execution if an RT sequence called :any:`generate_error`.

#### `def __init__(self, error)`

#### `def get_all_errors(self)`


        Generates a list of all errors reported during execution.

        Returns:
            List(:class:`SequenceError`): all errors generated during execution.

        

#### `def RunErrorFactory(cls, error)`

### `class RunFailedError(RunError)`


    Raised by :any:`run_py_as_rtseq` to report that the sequence failed.

    This error is raised when a real-time sequence executes successfully,
    but :any:`generate_error` was called with :any:`ErrorAction.ContinueSequenceExecution`.
    

#### `def __init__(self, error)`

### `class RunAbortedError(RunError)`


    Raised by :any:`run_py_as_rtseq` to report that the sequence failed.

    This error is raised when a real-time sequence executes successfully,
    but :any:`generate_error` was called with :any:`ErrorAction.StopSequence` or :any:`ErrorAction.AbortSequence`.
    

#### `def __init__(self, error)`

### `class SequenceError(VeristandError)`

Raised by :any:`generate_error` to report a sequence failure.

#### `def __init__(self, error_code, message, error_action)`

#### `def inner_error(self)`


        Returns the error generated before the most recent error, if any, or `None`.

        Returns:
            :any:`SequenceError`: the previous error generated by this sequence.

        Real-time sequences report only the last error the sequence generates. If you want to see a list of all the
        inner errors, use :any:`RunError.get_all_errors`.

        

#### `def inner_error(self, value)`

#### `def is_fatal(self)`


        Returns whether or not any error causes the sequence to stop.

        Returns:
            bool: True if the error is :any:`ErrorAction.AbortSequence` or :any:`ErrorAction.StopSequence`, false if
            the error is :any:`ErrorAction.ContinueSequenceExecution`.

        

#### `def should_raise(self)`


        Determines whether or not this error raises an exception.

        Returns:
            bool: False if the error is :any:`ErrorAction.ContinueSequenceExecution` with an error code of 0. Otherwise,
            this function returns True.

        

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/legacy/NIVeriStand.py -->
## PYTHON MODULE: src/niveristand/legacy/NIVeriStand.py

### MODULE DOCSTRING


NI VeriStand Python API.

C-Python code wrapper of NI VeriStand client API.


### `def LaunchNIVeriStand()`

Launch NI VeriStand.exe from the installed location.

### `def WaitForNIVeriStandReady(address='localhost', secondsTimeout=120)`

### `def _ConvertMATRIXTO1DARRVAL_(values)`

### `class NIVeriStandException(Exception)`

NI VeriStand exception.

#### `def __init__(self, errcode, errstring)`

#### `def errorcode(self)`

Return the error code.

#### `def message(self)`

Return a formatted message of the error.

#### `def __str__(self)`

#### `def __repr__(self)`

### `def _RaiseException_(errorObject)`

### `def _Convert1DARRVALTOMATRIX_(rowDim, colDim, data)`

### `def _ConvertMATRIXARRToDataArray_(matArr)`

### `def _ConvertListParamToTuple_(param)`

### `class PySystemState()`


    The State of the NI VeriStand.exe.

    Idle indicate there is no workspace configuration file deployed
    Active indicate there is a workspace configuration file deployed
    

### `def CreateLogChannel(channel_path)`

### `def CreateLogInfo()`

### `class PyLogInfoTriggerType()`

Priority of an alarm.

### `def SetLogInfoTrigger(logInfo, triggerType)`

### `def SetLogInfoChannels(logInfo, logChannelList)`

### `class Workspace()`

Interface that controls the running state of the system and accesses the channels in the system.

#### `def __init__(self)`

#### `def GetEngineState(self)`

Returns the current state of the system.

#### `def RunWorkspaceFile(self, file, launchworkspacewindow, deploysystemdefinition, timeout, username, password)`

Runs the workspace configuration file you specify.

        Raises an error if you call this function while a configuration is already running.
        You must stop all running configurations before you call this function.
        If this function times out, check to see if the deployment process took longer than expected
        and caused the operation to timeout. Use the GetEngineState function to check the status of the system.
        

#### `def StopWorkspaceFile(self, password)`

Stops the execution of the currently running configuration.

#### `def LockWorkspaceFile(self, old_password, new_password)`


        Locks the configuration that is currently running.

        This function will only succeed if a configuration is currently running.
        If this configuration was locked previously, you must enter the previous password in `old_password`.
        

#### `def UnlockWorkspaceFile(self, password)`

Unlocks the currently running configuration.

#### `def GetSingleChannelValue(self, name)`

Acquires the value of the channel you specify.

#### `def GetMultipleChannelValues(self, names)`

Acquires values from the channels you specify.

#### `def GetChannelVectorValues(self, name)`

Acquires the vector value of the channel you specify.

#### `def SetSingleChannelValue(self, name, value)`

Sets the value for the channel you specify.

#### `def SetMultipleChannelValues(self, names, values)`

Sets the value(s) for the channels you specify.

#### `def SetChannelVectorValues(self, name, values)`


        Sets the starting parameter vector value for the channel you specify.

        The value you specify in `values` must be a matrix data type.
        

#### `def GetMultipleSystemNodesData(self, names)`

Acquires data from the nodes you specify.

#### `def GetSystemNodeChildren(self, name)`

Acquires a list of all the child nodes nested under the node you specify.

#### `def GetSystemNodeChannelList(self, name)`


        Acquires all channels of the node you specify.

        If you want to acquire all the channels in the system, enter "" as the node name.
        

#### `def GetAliasList(self)`

Acquires all the aliases of a system.

#### `def _NetSystemStateToPy_(self, net)`

#### `def _ConvertNodeInfoToDictionary_(self, nodeInfo)`

### `class Workspace2(Workspace)`

Interface that controls the running state of the system and accesses the channels in the system.

#### `def __init__(self, gatewayIPAddress=None)`

#### `def GetSystemState(self)`

Returns the current state of the system.

#### `def ConnectToSystem(self, systemdefinition_file, deploy, timeout, calibration_file='', filtered_targets=None)`

Connects the VeriStand Gateway to one or more targets running on the System Definition file you specify.

#### `def ReconnectToSystem(self, target, deploy, calibration_file, timeout)`

Reconnects the VeriStand Gateway to a target within the system definition file used by the Gateway.            You can also redeploy the system definition file.

#### `def DisconnectFromSystem(self, password, undeploy_system_definition)`

Disconnects the VeriStand Gateway from the targets.

#### `def LockConnection(self, old_password, new_password)`


        Locks the current VeriStand Gateway connection.

        If the connection was locked previously, you must enter the previous password in `old_password`.
        

#### `def UnlockConnection(self, password)`

Unlocks the current VeriStand Gateway connection.

#### `def StartDataLogging(self, configuration_name, logInfo)`

Starts logging data to the configuration you specify.

#### `def StopDataLogging(self, configuration_name)`

Terminates data logging for the configuration you specify.

#### `def SetChannelValues(self, channels, newValues)`

Sets the value for the channels you specify.

        The `newValues` parameter accepts scalar, vector, and matrix data types.
        

### `class PyAlarmPriority()`

Priority of an alarm.

### `class PyAlarmState()`

State of an alarm in the engine.

### `class PyAlarmMode()`


    Specifies the mode of an alarm when triggered.

    Normal mode - triggers the alarm and runs the associated script.
    Indicate mode - only triggers the alarm.
    

### `class Alarm()`

Interface that queries information on a configured alarm.

#### `def __init__(self, name, target=None, gatewayIPAddress=None)`

#### `def GetAlarmData(self, timeout)`

Acquires the alarm data.

#### `def SetAlarmData(self, alarmDict)`


        Sets the alarm data.

        DEPRECATED function. This function does not support the Priority Number field.
        Use SetAlarmData2() instead.
        

#### `def SetAlarmData2(self, alarmDict)`

Modifies an alarm in the system.

#### `def SetEnabledState(self, enabled)`

Enables or disables the current alarm.

#### `def SetAlarmMode(self, mode)`

Changes the mode of this alarm. See PyAlarmMode for possible values.

#### `def _NetAlarmPriorityToPy_(self, net)`

#### `def _PyAlarmPriorityToNet_(self, py)`

#### `def _NetAlarmStateToPy_(self, net)`

#### `def _PyAlarmStateToNet_(self, py)`

#### `def _NetAlarmModeToPy_(self, net)`

#### `def _PyAlarmModeToNet_(self, py)`

#### `def _ConvertAlarmToDictionary_(self, alarm)`

#### `def _ConvertDictionaryToAlarm_(self, alarm)`

#### `def _ConvertDictionaryToAlarm2_(self, alarm)`

### `class AlarmManager()`

Interface that acquires information on the state of the server alarm.

#### `def __init__(self)`

#### `def GetAlarmList(self)`

Acquires a list of names of all the alarms configured in the system.

#### `def GetAlarmsStatus(self)`

Acquires a list of alarms organized by status (high, medium, and low).

#### `def GetMultipleAlarmsData(self, alarms, timeout)`

Acquires information about a list of alarms.

### `class AlarmManager2()`

Interface that acquires information on the state of the server alarm.

#### `def __init__(self, gateway_ip_address=None)`

#### `def GetAlarmList(self, target)`

Acquires a list of names of all the alarms configured in the system.

#### `def GetAlarmsStatus(self, target)`

Acquires a list of alarms organized by status (high, medium, and low).

#### `def GetMultipleAlarmsData(self, target, alarms, timeout)`

Acquires information about a list of alarms.

### `class PyModelState()`

Represents the state of a model.

### `class PyModelCommand()`

Changes the state of the model.

### `class Model()`

Interface that acquires information on a specific model running on the system.

#### `def __init__(self, name, target=None, gatewayIPAddress=None)`

#### `def GetModelExecutionState(self)`

Acquires the execution time and state of the model.

#### `def SetModelExecutionState(self, command)`


        Changes the current state of the model on the server.

        This is a request operation on the server.
        Even if this function executes successfully, the model state may remain unchanged in some cases.
        See PyModelState for command values.
        

#### `def SaveModelState(self, filepath)`

Saves the current model state to the path on the target you specify in `filepath`.

#### `def RestoreModelState(self, filepath)`

Restores the state of a model running on the target. Specify the path to the model file in `filepath`.

#### `def _NetModelStateToPy_(self, net)`

#### `def _PyModelStateToNet_(self, py)`

### `class ModelManager()`

Interface that queries information on the models configured in the system.

#### `def __init__(self)`

#### `def GetModelList(self)`

Returns a list of all models configured in the system.

#### `def GetParametersList(self)`

Returns a list of all parameters in the system.

#### `def GetSingleParameterValue(self, name)`

Acquires the value of the parameter you specify.

#### `def GetMultipleParameterValues(self, names)`

Acquires the value(s) of the parameters you specify.

#### `def GetParameterVectorValues(self, name)`

Acquires the vector values of the parameter you specify.

#### `def SetSingleParameterValue(self, name, value)`

Sets the value of the parameter you specify.

#### `def SetMultipleParameterValues(self, names, values)`

Sets the value(s) of the parameters you specify.

#### `def SetParameterVectorValues(self, name, values)`


        Sets a vector value for a parameter.

        The value you specify in `value` must be a matrix data type.
        

### `class ModelManager2(ModelManager)`

Interface that queries information on the models configured in the system.

#### `def __init__(self, gateway_ip_address=None)`

#### `def GetModelList(self, target)`

Returns a list of models on the target you specify.

#### `def GetParametersList(self, target)`

Returns a list of all parameters in the target you specify.

#### `def GetSingleParameterValue(self, target, name)`

Acquires the value of the parameter you specify.

#### `def GetMultipleParameterValues(self, target, names)`

Acquires the value(s) of the parameters you specify.

#### `def GetParameterVectorValues(self, target, name)`

Acquires the vector values of the parameter you specify.

#### `def SetSingleParameterValue(self, target, name, value)`

Sets the value of the parameter you specify.

#### `def SetMultipleParameterValues(self, target, names, values)`

Sets the value of the parameter(s) you specify.

#### `def SetParameterVectorValues(self, target, name, values)`

Set a parameter vector values.

        Values are expected to be a matrix type.
        

#### `def SetParameterValues(self, target, names, matrixArr)`


        Sets the vector value of the parameter(s) you specify.

        The value you specify in `matrixArr` must be a matrix data type.
        Sample usage ModelManager2.SetParameterValues("target1",["1By3Param","2By3Param"],[[[1,2,3]],[[1,2,3],[4,5,6]]])
        

#### `def UpdateParametersFromFile(self, target, parameterfiles)`

Update a set of parameters specified in the parameter files.

### `class ChannelFaultManager()`

Interface that institutes software value forcing on the system.

#### `def __init__(self, gatewayIPAddress=None)`

#### `def GetFaultList(self)`

Acquires a list of all currently faulted channels.

#### `def GetFaultValue(self, name)`

Acquires the fault value of a channel you specify.

#### `def SetFaultValue(self, name, value)`

Sets the fault value of the channel you specify.

#### `def ClearFault(self, name)`

Removes the channel you specify from the fault list.

#### `def ClearAllFaults(self)`

Clears all faults.

### `class PyStimulusState()`

Represents the state of the stimulus generation server.

### `class PyStimulusResult()`

Represents the result of the stimulus generation.

### `class Stimulus()`

#### `def __init__(self)`

#### `def __del__(self)`

#### `def ReserveStimulusProfileManager(self)`


        Creates a task that reserves the stimulus generation server.

        This task prevents other clients from interrupting the stimulus generation process.
        

#### `def UnreserveStimulusProfileManager(self)`

Destroys the task that reserves the stimulus generation server. Frees the server for other clients to use.

#### `def GetStimulusProfileManagerState(self)`

Returns the state of the stimulus generation component.

#### `def RunStimulusProfile(self, testfile, baselogpath, timeout, autostart, stopondisconnect)`

Starts the stimulus generation you defined in the test file.

#### `def StopStimulusProfile(self)`

Stops the stimulus generation.

#### `def GetStimulusProfileFile(self)`

Acquires the current stimulus definition file.

#### `def GetStimulusProfileResult(self)`


        Acquires the result of stimulus generation test.

        Only the table test produces a test file of the result.
        

#### `def _NetStimulusStateToPy_(self, net)`

#### `def _NetStimulusResultToPy_(self, net)`

### `class Stimulus2(Stimulus)`

Automates the execution of stimulus profiles.

#### `def __init__(self, gatewayIPAddress=None)`

#### `def __del__(self)`

#### `def RunStimulusProfile(self, testfile, baselogpath, timeout, autostart, stopondisconnect, parameterfiles=())`

Starts the stimulus generation you defined in the test file.

### `class MacroRecorder()`

#### `def __init__(self)`

#### `def StartRecording(self)`

#### `def StopRecording(self)`

#### `def ResumeRecording(self)`

#### `def SaveMacro(self, file)`

#### `def GetCommandLines(self)`

### `class PyMacroPlayerState()`

Represents the state of the macro player.

### `class PyMacroPlayerMode()`

Represents the replay mode of the macro player.

### `class MacroPlayer()`

#### `def __init__(self, gatewayIPAddress=None)`

#### `def LoadMacro(self, file)`

Loads a workspace macro.

#### `def PlayState(self)`

Acquires the current play state.

#### `def PlayMacro(self, mode)`

Replays the loaded macro.

#### `def Wait(self)`

#### `def PausePlaying(self)`

#### `def ResumePlaying(self)`

#### `def StopPlaying(self)`

#### `def GetCommandLines(self)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/library/__init__.py -->
## PYTHON MODULE: src/niveristand/library/__init__.py

- `__all__ = ['abstime', 'arraysize', 'clearfault', 'clearlasterror', 'deltat', 'deltatus', 'fault', 'fix', 'generate_error', 'getlasterror', 'iteration', 'localhost_wait', 'multitask', 'nivs_yield', 'quotient', 'recip', 'rand', 'rem', 'ramp', 'sawtooth_wave', 'sine_wave', 'square_wave', 'triangle_wave', 'uniform_white_noise_wave', 'seqtime', 'seqtimeus', 'stop_task', 'task', 'tickcountms', 'tickcountus', 'wait', 'wait_until_next_ms_multiple', 'wait_until_next_us_multiple', 'wait_until_settled']`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/library/_tasks.py -->
## PYTHON MODULE: src/niveristand/library/_tasks.py

### `def get_scheduler()`

### `def multitask()`


    Creates a multitask context for branching execution.

    Refer to :func:`niveristand.library.multitask` for more details on branching execution.
    

### `def nivs_yield()`


    Yields execution from this task or block to the next.

    Refer to :func:`niveristand.library.multitask` for more details on yielding to other tasks.
    

### `class _MultiTaskInfo(object)`

#### `def __init__(self)`

#### `def add_func(self, func)`

#### `def finished(self)`

#### `def get_unique_task_name(cls)`

### `class _IterationCounter(object)`

#### `def __init__(self)`

#### `def inc(self)`

#### `def count(self)`

#### `def finished(self)`

#### `def finished(self, value)`

### `class _Task(object)`

#### `def __init__(self, func, parent=None, iteration_counter=None)`

#### `def start(self)`

#### `def parent(self)`

#### `def thread(self)`

#### `def iteration_counter(self)`

#### `def is_stopped(self)`

#### `def is_stopping(self)`

#### `def wait_for_turn(self)`

#### `def signal_to_run(self)`

#### `def move_to_ready(self)`

#### `def mark_stopped(self)`

#### `def stop_task(self)`

#### `def error(self)`

#### `def error(self, error)`

#### `def __repr__(self)`

#### `def __str__(self)`

### `class _Scheduler(object)`

#### `def get_scheduler(cls)`

#### `def __init__(self)`

#### `def _can_sched(self)`

#### `def sched(self)`

#### `def thread_yielded(self)`

#### `def register_task_at_top(self, task)`

#### `def register_task(self, task)`

#### `def _register_task_core(self, task, at_top)`

#### `def task_finished(self, task)`

#### `def create_and_register_task_for_top_level(self)`

#### `def get_task_for_curr_thread(self)`

#### `def try_get_task_for_curr_thread(self)`

#### `def get_task_by_name(self, taskname)`

### `def stop_task(task_function)`


    Stops the task you specify.

    Args:
        task_function:  task function you want to stop. You must have previously declared the task function inside
                        a :func:`multitask` context.


    Refer to :func:`niveristand.library.multitask` for more details on stopping tasks.

    

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/library/primitives.py -->
## PYTHON MODULE: src/niveristand/library/primitives.py

### `def abstime()`


    Returns the current date and time, in seconds, relative to the operating system's epoc.

    **Note**: Only available for RT sequences.
    

### `def arraysize(x)`


    Returns the number of elements in x, where x is an array.

    Args:
        x: the array for which you want to get the number of elements.

    Returns:
        int: the size of the array. If **x** is not an array, this function returns 0.


    

### `def clearfault(x)`


    Clears all faults set on channel x.

    Args:
        x: the channel you want to clear faults on.

    Channel `x` must be a reference to a channel and should not be a reference to a local variable.
    If `channel` references a local variable, :func:`clearfault` performs no operation.

    **Note**: Only available for RT sequences.

    

### `def clearlasterror()`


    Clears the last error set by :func:`generate_error`.

    **Note**: Only available for RT sequences.
    

### `def deltat()`


    Returns the duration, in seconds, of the current system timestep.

    To perform equality or comparison operations, use `deltatus`.

    **Note**: In Python Mode, this function always returns `0.01` for a rate of 100Hz.
    

### `def deltatus()`


    Returns the duration, in microseconds, of the current system timestep.

    **Note**: In Python Mode, this function always returns `10,000` for a rate of 100Hz.
    

### `def fault(channel, value)`


    Faults `channel` with `value`.

    Args:
        channel: channel to fault.
        value(float): value to fault the channel.

    `channel` must be a reference to a channel and should not be a reference to a local variable.
    If `channel` references a local variable, :func:`fault` performs no operation.

    **Note**: Only available for RT sequences.

    

### `def fix(x)`


    Rounds x to the nearest integer between x and zero.

    Args:
        x(float): value you want to round.

    Returns:
        (float): floating-point representation of the rounded value.

    **Note**: Only available for RT sequences.

    

### `def getlasterror()`


    Returns the numeric error code of the last error set by :func:`generate_error`.

    **Note**: Only available for RT sequences.
    

### `def iteration()`


    Returns the number of iterations since the current top-level sequence started.

    Returns:
        int: iteration count.

    

### `def quotient(x, y)`


    Returns floor(x/y), the number of times y evenly divides into x.

    Args:
        x: dividend.
        y: divisor.

    Returns:
        int: integer quotient of x/y


    

### `def rand(x)`


    Returns a random floating-point number between 0 and the maximum value.

    Args:
        x(float): maximum value.

    Returns:
        float: random number between 0 and `x`

    

### `def recip(x)`


    Returns 1/x.

    Args:
        x: divisor.

    **Note**: Only available for RT sequences.

    

### `def rem(x, y)`


    Returns the remainder of x/y, when the quotient is rounded to the nearest integer.

    Args:
        x(float): dividend.
        y(float): divisor.

    

### `def seqtime()`


    Returns the number of elapsed seconds since the epoch.

    Returns:
        float: time, in seconds, since the epoch.

    To perform equality or comparison operations, use `seqtimeus` instead.

    

### `def seqtimeus()`


    Returns the elapsed time, in microseconds, since the epoch.

    Returns:
        int: elapsed time, in microseconds, as reported by the system clock.

    

### `def tickcountms()`


    Returns the current value of the milliseconds counter.

    Returns:
        int: time, in milliseconds, as reported by the high-precision counter (if available).

    

### `def tickcountus()`


    Returns the current value of the microseconds counter.

    Returns:
        int: time, in microseconds, as reported by the high-precision counter (if available).

    

### `def localhost_wait(amount=0.1)`


    Waits for channel values to update.

    Args:
        amount(float): time, in seconds, this function waits for channel values to update.

    When running in the VeriStand Engine, this function is ignored as channels are always up to date.

    

### `def generate_error(code, message, action)`


    Generates an error to report test failure.

    Args:
        code(int): error code to display.
        message(str): error string to display.
        action(:class:`niveristand.clientapi.ErrorAction`): action to perform.

    Returns:
        If action is Continue, returns the generated error.

    

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/library/timing.py -->
## PYTHON MODULE: src/niveristand/library/timing.py

### `def wait(duration)`


    Waits the duration, in seconds, you specify.

    Args:
        duration (:any:`DoubleValue`): time, in seconds, this function waits. You may specify fractions of seconds.

    Returns:
        float: actual seconds waited.

    This wait is non-blocking, so other tasks will run while this wait executes.

    

### `def wait_until_next_ms_multiple(ms_multiple)`


    Waits until the next millisecond multiple of the number you specify in `ms_multiple`.

    Args:
        ms_multiple(:any:`I64Value`): the millisecond multiple to wait until.

    Returns:
        int: actual milliseconds waited.

    This wait is non-blocking, so other tasks will run while this wait executes.

    

### `def wait_until_next_us_multiple(us_multiple)`


    Waits until the next microsecond multiple of the number you specify in `us_multiple`.

    Args:
        us_multiple(:any:`I64Value`): the microsecond multiple to wait until.

    Returns:
        int: actual microseconds waited.

    This wait is non-blocking, so other tasks will run while this wait executes.

    

### `def wait_until_settled(signal, upper_limit, lower_limit, settle_time, timeout)`


    Waits until `signal` settles for the amount of time you specify in `settle_time`.

    Args:
        signal(:any:`DoubleValue`): value to monitor.
        upper_limit(:any:`DoubleValue`): maximum value of the settle range.
        lower_limit(:any:`DoubleValue`): minimum value of the settle range.
        settle_time(:any:`DoubleValue`): time, in seconds, `signal` must stay inside the settle range.
        timeout(:any:`DoubleValue`): seconds to wait before the function times out.

    Returns:
        bool:

        True: The signal failed to settle before the operation timed out.
        False: The signal settled before the operation timed out.


    This wait is non-blocking, so other tasks will run while this wait executes.

    

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/library/waveforms.py -->
## PYTHON MODULE: src/niveristand/library/waveforms.py

### `def ramp(ramp_out, init_value, final_value, duration)`


    Ramps a variable from an initial value to an ending value over the duration you specify.

    Args:
        ramp_out(:any:`DoubleValue`): variable you want to ramp.
        init_value(:any:`DoubleValue`): starting value.
        final_value(:any:`DoubleValue`): ending value.
        duration(:any:`DoubleValue`): time, in seconds, you want the ramp to take.

    

### `def sawtooth_wave(wave_out, amplitude, freq, phase, bias, duration)`


    Plays a sawtooth wave with the parameters you specify.

    Args:
        wave_out(:any:`DoubleValue`): variable onto which the sawtooth wave plays.
        amplitude(:any:`DoubleValue`): amplitude of the sawtooth wave.
        freq(:any:`DoubleValue`): frequency, in Hz, of the sawtooth wave.
        phase(:any:`DoubleValue`): phase, in degrees, of the sawtooth wave.
        bias(:any:`DoubleValue`): offset to add to the sawtooth wave.
        duration(:any:`DoubleValue`): duration, in seconds, to play the sawtooth wave.

    

### `def sine_wave(wave_out, amplitude, freq, phase, bias, duration)`


    Plays a sine wave with the parameters you specify.

    Args:
        wave_out(:any:`DoubleValue`): variable onto which the sine wave plays.
        amplitude(:any:`DoubleValue`): amplitude of the sine wave.
        freq(:any:`DoubleValue`): frequency, in Hz, of the sine wave.
        phase(:any:`DoubleValue`): phase, in degrees, of the sine wave.
        bias(:any:`DoubleValue`): offset to add to the sine wave.
        duration(:any:`DoubleValue`): duration, in seconds, to play the sine wave.

    

### `def square_wave(wave_out, amplitude, freq, phase, bias, duty_cycle, duration)`


    Plays a square wave with the parameters you specify.

    Args:
        wave_out(:any:`DoubleValue`): variable onto which the square wave plays.
        amplitude(:any:`DoubleValue`): amplitude of the square wave.
        freq(:any:`DoubleValue`): frequency, in Hz, of the square wave.
        phase(:any:`DoubleValue`): phase, in degrees, of the square wave.
        bias(:any:`DoubleValue`): offset to add to the square wave.
        duty_cycle(:any:`DoubleValue`): percentage of time the square wave remains high versus low over one period.
        duration(:any:`DoubleValue`): time, in seconds, to play the square wave.

    

### `def triangle_wave(wave_out, amplitude, freq, phase, bias, duration)`


    Plays a triangle wave with the parameters you specify.

    Args:
        wave_out(:any:`DoubleValue`): variable onto which the triangle wave plays.
        amplitude(:any:`DoubleValue`): amplitude of the triangle wave.
        freq(:any:`DoubleValue`): frequency, in Hz, of the triangle wave.
        phase(:any:`DoubleValue`): phase, in degrees, of the triangle wave.
        bias(:any:`DoubleValue`): offset to add to the triangle wave.
        duration(:any:`DoubleValue`): duration, in seconds, to play the triangle wave.

    

### `def uniform_white_noise_wave(wave_out, amplitude, seed, duration)`


    Plays a uniform white noise wave with the parameters you specify.

    Args:
        wave_out(:any:`DoubleValue`): variable onto which the white noise wave plays.
        amplitude(:any:`DoubleValue`): amplitude of the white noise wave.
        seed(:any:`I32Value`): seed for random number generator.
        duration(:any:`DoubleValue`): duration, in seconds, to play the white noise wave.

    

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/realtimesequencetools.py -->
## PYTHON MODULE: src/niveristand/realtimesequencetools.py

### `def run_py_as_rtseq(toplevelfunc, rtseq_params={}, target=None)`


    Runs a Python function as an RT sequence in the VeriStand Engine.

    Args:
        toplevelfunc: the Python function to run.
        rtseq_params (Dict[str, niveristand.clientapi._datatypes.rtprimitives.DoubleValue]):  the parameters to be
         passed to the RT sequence.
        target: The name of the target on which to deploy or run the real-time sequence.
         If None, the default target is used.

    Returns:
        Union[float, None]:
        The numeric value returned by the real-time sequence execution.

    Raises:
        :any:`TranslateError`: if the function is not successfully translated.
        :any:`RunAbortedError`: if this function calls :any:`generate_error` with an action of Abort or Stop.
        :any:`RunFailedError`: if this function calls :any:`generate_error` with a Continue action.

    

### `def save_rtseq_as_py(toplevelseq, srcfolder, destfolder)`

### `def save_py_as_rtseq(toplevelfunc, dest_folder)`


    Saves a Python function as an RT sequence that is compatible with the Stimulus Profile Editor.

    Args:
        toplevelfunc: the Python function you want to save.
        dest_folder[str]: the folder you want to save the sequence and all its dependencies in.

    Returns:
        The full path to the main sequence file.

    Raises:
        :class:`niveristand.errors.TranslateError`: if the function is not successfully translated.

    

### `def validate_py_as_rtseq(toplevelobj)`

### `def run_rtseq(toplevelseq, destfolder)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/systemdefinitionapi/__init__.py -->
## PYTHON MODULE: src/niveristand/systemdefinitionapi/__init__.py

### MODULE DOCSTRING

Module for NationalInstruments.VeriStand.SystemDefinitionAPI.

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/systemdefinitionapi/_auto_generated_classes.py -->
## PYTHON MODULE: src/niveristand/systemdefinitionapi/_auto_generated_classes.py

### MODULE DOCSTRING

Module for NationalInstruments.VeriStand.SystemDefinitionAPI.

### `class _staticproperty(staticmethod)`

#### `def __get__(self, *_)`

### `class _DotNetBase()`

#### `def __eq__(self, other) -> bool`

#### `def __repr__(self) -> str`

#### `def _custom_repr(self) -> str`

### `class _DotNetEnum(_DotNetBase)`

#### `def __repr__(self) -> str`

#### `def __str__(self) -> str`

#### `def __int__(self) -> int`

### `def _is_iterable(arg: Any) -> bool`

### `def _unwrap(out_params: Dict[Optional[Tuple[str, ...]], Tuple[int, Any]], *args: Tuple[Any]) -> Iterable[Any]`

### `def _wrap(one_or_many_args: Union[Any, Tuple[Any]]) -> Union[Any, Tuple[Any]]`

### `class AcquisitionMode(_DotNetEnum)`

Defines the acquisition mode of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTask" />.

#### `def __init__(self, *args)`

Create a new instance.

#### `def FINITE() -> AcquisitionMode`

#### `def CONTINUOUS() -> AcquisitionMode`

### `class AcquisitionUnits(_DotNetEnum)`

Defines whether the size of acquisitions is represented as samples per channel or time, in seconds.

#### `def __init__(self, *args)`

Create a new instance.

#### `def SAMPLES() -> AcquisitionUnits`

#### `def SECONDS() -> AcquisitionUnits`

### `class ActionOnNew(_DotNetEnum)`

Defines the location to which to log data when a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> begins a new acquisition.

#### `def __init__(self, *args)`

Create a new instance.

#### `def NEW_GROUP() -> ActionOnNew`

#### `def NEW_FILE() -> ActionOnNew`

### `class AlarmMode(_DotNetEnum)`

The action that occurs when the alarm is triggered on the target.

#### `def __init__(self, *args)`

Create a new instance.

#### `def NORMAL() -> AlarmMode`

#### `def INDICATE_ONLY() -> AlarmMode`

### `class AlarmPriority(_DotNetEnum)`

This enumeration is deprecated in NI VeriStand 2011 and later. Use the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> property instead.
            <para>
            Setting this enumeration to Low, Medium, or High automatically sets the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> to 25, 15, or 5, respectively.</para>

#### `def __init__(self, *args)`

Create a new instance.

#### `def LOW() -> AlarmPriority`

#### `def MEDIUM() -> AlarmPriority`

#### `def HIGH() -> AlarmPriority`

### `class AlarmState(_DotNetEnum)`

The state of an alarm on the target.

#### `def __init__(self, *args)`

Create a new instance.

#### `def DISABLED() -> AlarmState`

#### `def ENABLED() -> AlarmState`

### `class AlarmingStepFunction(_DotNetEnum)`

The function of an alarm running on the target.

#### `def __init__(self, *args)`

Create a new instance.

#### `def ADJUST_SETTINGS() -> AlarmingStepFunction`

#### `def ENABLE_ALARM() -> AlarmingStepFunction`

#### `def DISABLE_ALARM() -> AlarmingStepFunction`

#### `def RESET_ALARM_EXIT_SUBROUTINE() -> AlarmingStepFunction`

#### `def DISABLE_ALARM_EXIT_SUBROUTINE() -> AlarmingStepFunction`

#### `def RESET_ALARM() -> AlarmingStepFunction`

### `class BaseNode(_DotNetBase)`

Represents generic nodes in the system definition and provides access to options and configuration settings that all nodes support.

#### `def __init__(self, *args)`

Create a new instance.

#### `def base_node_type(self) -> BaseNodeType`

Gets a reference to the internal representation of this node.

#### `def name(self) -> str`

Gets the name of this node. To rename a node, use the <see cref="M:NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNode.RenameNode(System.String)" crefType="Unqualified" /> method.

#### `def node_path(self) -> str`

Gets the path to the node within the system definition file.

#### `def node_id(self) -> int`

Gets the ID of this node.

#### `def log_file_producer(self) -> bool`

Gets a value indicating whether the node is a log file producer

#### `def description(self) -> str`

Gets or sets the description of this node.

#### `def description(self, value: str)`

Gets or sets the description of this node.

#### `def type_guid(self) -> str`

Gets the GUID associated with the node.
            Attempts to set the GUID of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNode" crefType="Unqualified" /> will generate an exception.

#### `def type_guid(self, value: str)`

Gets the GUID associated with the node.
            Attempts to set the GUID of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNode" crefType="Unqualified" /> will generate an exception.

#### `def get_parent(self) -> Tuple[bool, BaseNode]`

#### `def get_parent(self, *args)`

#### `def get_children(self) -> Sequence[BaseNode]`

#### `def get_children(self, *args)`

#### `def find_children_by_guid(self, type_guid: str) -> Sequence[BaseNode]`

#### `def find_children_by_guid(self, *args)`

#### `def find_first_child_with_name(self, name: str, deep_hierarchy: bool) -> Tuple[bool, BaseNode]`

#### `def find_first_child_with_name(self, *args)`

#### `def find_node_by_path(self, nodepath: str) -> Tuple[bool, BaseNode]`

#### `def find_node_by_path(self, *args)`

#### `def get_document_root(self) -> Root`

#### `def get_document_root(self, *args)`

#### `def get_document_path(self) -> str`

#### `def get_document_path(self, *args)`

#### `def remove_node(self) -> bool`

#### `def remove_node(self, *args)`

#### `def rename_node(self, new_name: str) -> bool`

#### `def rename_node(self, *args)`

#### `def get_node_errors(self)`

#### `def get_node_errors(self, *args)`

#### `def equals(self, obj: Any) -> bool`

#### `def equals(self, *args)`

#### `def get_hash_code(self) -> int`

#### `def get_hash_code(self, *args)`

#### `def _custom_repr(self) -> str`

### `class CANIOMode(_DotNetEnum)`

I/O Mode used by the interface when transmitting a CAN frame.

#### `def __init__(self, *args)`

Create a new instance.

#### `def STANDARD() -> CANIOMode`

#### `def FD() -> CANIOMode`

#### `def FDBRS() -> CANIOMode`

### `class CANTransceiverType(_DotNetEnum)`

The transceiver type of an NI-XNET CAN port.

#### `def __init__(self, *args)`

Create a new instance.

#### `def HS() -> CANTransceiverType`

#### `def LS() -> CANTransceiverType`

#### `def SW() -> CANTransceiverType`

### `class CANTransmitOrderType(_DotNetEnum)`

The order in which the CAN interface transmits frames from the internal queue.

#### `def __init__(self, *args)`

Create a new instance.

#### `def AS_SUBMITTED() -> CANTransmitOrderType`

#### `def BY_IDENTIFIER() -> CANTransmitOrderType`

### `class CDChannel_Type(_DotNetEnum)`

Specifies the type (<format type="monospace">Input</format> or <format type="monospace">Output</format>) of a custom device channel.

#### `def __init__(self, *args)`

Create a new instance.

#### `def INPUT() -> CDChannel_Type`

#### `def OUTPUT() -> CDChannel_Type`

### `class CDDriverExecMode(_DotNetEnum)`

Specifies the execution mode, or device type, of a custom device. The execution mode defines how the device interacts with the VeriStand Engine.

#### `def __init__(self, *args)`

Create a new instance.

#### `def ASYNCHRONOUS() -> CDDriverExecMode`

#### `def INLINE_HW_INTERFACE() -> CDDriverExecMode`

#### `def INLINE_MODEL_INTERFACE() -> CDDriverExecMode`

#### `def INLINE_TIMING_AND_SYNC() -> CDDriverExecMode`

#### `def ASYNCHRONOUS_TIMING_AND_SYNC() -> CDDriverExecMode`

### `class CDLoopType(_DotNetEnum)`

Specifies the type of loop in which an asynchronous custom device executes.

#### `def __init__(self, *args)`

Create a new instance.

#### `def WHILE_LOOP() -> CDLoopType`

#### `def TIMED_LOOP() -> CDLoopType`

### `class CDTimeLoopPriority(_DotNetEnum)`

Specifies the priority of the Timed Loop that an asynchronous custom device with a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CDLoopType" crefType="Unqualified" /> of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.CDLoopType.TimedLoop" crefType="Unqualified" /> executes in. If you want to wire this value to the input terminal of a Timed Loop in LabVIEW, you must first convert it to a positive integer between 1 and 65,535.

#### `def __init__(self, *args)`

Create a new instance.

#### `def LOW() -> CDTimeLoopPriority`

#### `def MEDIUM() -> CDTimeLoopPriority`

#### `def HIGH() -> CDTimeLoopPriority`

### `class ChannelNames(_DotNetEnum)`

Specifies how the names of DAQ channels appear in log files this task creates and in the list of available triggers.

#### `def __init__(self, *args)`

Create a new instance.

#### `def PHYSICAL_CHANNEL() -> ChannelNames`

#### `def SYSTEM_DEFINITION() -> ChannelNames`

### `class CommunicationProtocol(_DotNetEnum)`

Protocol used by the virtual ECU Network Cluster to communicate with the real ECU network.

#### `def __init__(self, *args)`

Create a new instance.

#### `def CAN() -> CommunicationProtocol`

#### `def LIN() -> CommunicationProtocol`

#### `def ETHERNET() -> CommunicationProtocol`

### `class ConditionStepComparison(_DotNetEnum)`

The condition to use when comparing <format type="italics">Variable</format> and <format type="italics">Value</format> in a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Condition" crefType="Unqualified" /> step.

#### `def __init__(self, *args)`

Create a new instance.

#### `def GREATER() -> ConditionStepComparison`

#### `def LESS() -> ConditionStepComparison`

#### `def EQUAL() -> ConditionStepComparison`

#### `def NOT_EQUAL() -> ConditionStepComparison`

#### `def GREATER_OR_EQUAL() -> ConditionStepComparison`

#### `def LESS_OR_EQUAL() -> ConditionStepComparison`

### `class CustomDeviceBase(BaseNode)`

Defines a base class for NI VeriStand custom devices.

#### `def __init__(self, *args)`

Create a new instance.

#### `def rename_node(self, new_name: str, force_rename: bool) -> bool`

#### `def rename_node(self, *args)`

#### `def get_boolean_property(self, name: str) -> Tuple[bool, bool]`

#### `def get_boolean_property(self, *args)`

#### `def get_u16_property(self, name: str) -> Tuple[bool, int]`

#### `def get_u16_property(self, *args)`

#### `def get_u32_property(self, name: str) -> Tuple[bool, int]`

#### `def get_u32_property(self, *args)`

#### `def get_u32_array_property(self, name: str) -> Tuple[bool, Sequence[int]]`

#### `def get_u32_array_property(self, *args)`

#### `def get_u64_property(self, name: str) -> Tuple[bool, int]`

#### `def get_u64_property(self, *args)`

#### `def get_i32_property(self, name: str) -> Tuple[bool, int]`

#### `def get_i32_property(self, *args)`

#### `def get_i32_array_property(self, name: str) -> Tuple[bool, Sequence[int]]`

#### `def get_i32_array_property(self, *args)`

#### `def get_double_property(self, name: str) -> Tuple[bool, float]`

#### `def get_double_property(self, *args)`

#### `def get_double_array_property(self, name: str) -> Tuple[bool, Sequence[float]]`

#### `def get_double_array_property(self, *args)`

#### `def get_string_property(self, name: str) -> Tuple[bool, str]`

#### `def get_string_property(self, *args)`

#### `def get_binary_string_property(self, name: str) -> Tuple[bool, Sequence[int]]`

#### `def get_binary_string_property(self, *args)`

#### `def get_string_array_property(self, name: str) -> Tuple[bool, Sequence[str]]`

#### `def get_string_array_property(self, *args)`

#### `def get_dependent_node_property_basenode(self, name: str) -> Tuple[bool, BaseNode]`

#### `def get_dependent_node_property_basenode(self, *args)`

#### `def get_dependent_node_property_str(self, name: str) -> Tuple[bool, str]`

#### `def get_dependent_node_property_str(self, *args)`

#### `def get_dependent_file_property(self, name: str) -> Tuple[bool, DependentFile]`

#### `def get_dependent_file_property(self, *args)`

#### `def get_dictionary_property(self, name: str) -> Tuple[bool, Dictionary]`

#### `def get_dictionary_property(self, *args)`

#### `def get_dictionary_array_property(self, name: str) -> Tuple[bool, Sequence[Dictionary]]`

#### `def get_dictionary_array_property(self, *args)`

#### `def get_variant_property(self, name: str) -> Tuple[bool, Sequence[int], Sequence[int]]`

#### `def get_variant_property(self, *args)`

#### `def set_boolean_property(self, name: str, value: bool) -> bool`

#### `def set_boolean_property(self, *args)`

#### `def set_u16_property(self, name: str, value: int) -> bool`

#### `def set_u16_property(self, *args)`

#### `def set_u32_property(self, name: str, value: int) -> bool`

#### `def set_u32_property(self, *args)`

#### `def set_u32_array_property(self, name: str, value: Sequence[int]) -> bool`

#### `def set_u32_array_property(self, *args)`

#### `def set_u64_property(self, name: str, value: int) -> bool`

#### `def set_u64_property(self, *args)`

#### `def set_i32_property(self, name: str, value: int) -> bool`

#### `def set_i32_property(self, *args)`

#### `def set_i32_array_property(self, name: str, value: Sequence[int]) -> bool`

#### `def set_i32_array_property(self, *args)`

#### `def set_double_property(self, name: str, value: float) -> bool`

#### `def set_double_property(self, *args)`

#### `def set_double_array_property(self, name: str, value: Sequence[float]) -> bool`

#### `def set_double_array_property(self, *args)`

#### `def set_string_property(self, name: str, value: str) -> bool`

#### `def set_string_property(self, *args)`

#### `def set_binary_string_property(self, name: str, value: Sequence[int]) -> bool`

#### `def set_binary_string_property(self, *args)`

#### `def set_string_array_property(self, name: str, value: Sequence[str]) -> bool`

#### `def set_string_array_property(self, *args)`

#### `def set_dependent_node_property(self, name: str, value: BaseNode) -> bool`

#### `def set_dependent_node_property(self, name: str, dep_node_path: str) -> bool`

#### `def set_dependent_node_property(self, *args)`

#### `def set_dependent_file_property(self, name: str, value: DependentFile) -> bool`

#### `def set_dependent_file_property(self, *args)`

#### `def set_dictionary_property(self, name: str, value: Dictionary) -> bool`

#### `def set_dictionary_property(self, *args)`

#### `def set_dictionary_array_property(self, name: str, value: Sequence[Dictionary]) -> bool`

#### `def set_dictionary_array_property(self, *args)`

#### `def set_variant_property(self, name: str, type: Sequence[int], value: Sequence[int]) -> bool`

#### `def set_variant_property(self, *args)`

#### `def get_property_names(self) -> Sequence[str]`

#### `def get_property_names(self, *args)`

#### `def get_property_type(self, property_name: str) -> Tuple[bool, PropertyContent]`

#### `def get_property_type(self, *args)`

#### `def remove_property(self, name: str) -> bool`

#### `def remove_property(self, *args)`

#### `def move_node_to(self, parent_type: CustomDeviceBase) -> bool`

#### `def move_node_to(self, *args)`

#### `def remove_error(self, error_id: str)`

#### `def remove_error(self, *args)`

#### `def report_error(self, error_id: str, is_error: bool, err_code: int, message: str)`

#### `def report_error(self, *args)`

#### `def set_log_file_producer_flag(self, is_log_file_producer: bool)`

#### `def set_log_file_producer_flag(self, *args)`

### `class CustomDeviceSection(CustomDeviceBase)`

Represents a section under a custom device. Sections are not required in custom devices, but provide a way to organize custom device channels into a logical hierarchy.

#### `def __init__(self, name: str, guid: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def add_custom_device_section_if_not_found(self, name: str, guid: str) -> Tuple[CustomDeviceSection, bool]`

#### `def add_custom_device_section_if_not_found(self, *args)`

#### `def add_custom_device_channel_if_not_found(self, name: str, guid: str) -> Tuple[CustomDeviceChannel, bool]`

#### `def add_custom_device_channel_if_not_found(self, *args)`

#### `def add_custom_device_waveform_if_not_found(self, name: str, guid: str, data_type: WaveformTypeDataType) -> Tuple[CustomDeviceWaveform, bool]`

#### `def add_custom_device_waveform_if_not_found(self, *args)`

#### `def add_output_underflow_count_channel(self, name: str) -> CustomDeviceChannel`

#### `def add_output_underflow_count_channel(self, *args)`

#### `def add_input_overflow_count_channel(self, name: str) -> CustomDeviceChannel`

#### `def add_input_overflow_count_channel(self, *args)`

#### `def add_error_channel(self, name: str) -> CustomDeviceChannel`

#### `def add_error_channel(self, *args)`

### `class CustomDeviceWaveform(CustomDeviceBase)`

Represents a waveform in a custom device.

#### `def __init__(self, name: str, guid: str, data_type: WaveformTypeDataType)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def units(self) -> str`

Gets or sets the units associated with a CustomDeviceWaveform. Units can be any string that makes sense for your custom device.

#### `def units(self, value: str)`

Gets or sets the units associated with a CustomDeviceWaveform. Units can be any string that makes sense for your custom device.

#### `def data_type(self) -> WaveformTypeDataType`

Gets or sets the data type associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceWaveform" /> class.

#### `def data_type(self, value: WaveformTypeDataType)`

Gets or sets the data type associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceWaveform" /> class.

### `class DAQAnalogChannelType(_DotNetEnum)`

Specifies the measurement type of an analog DAQ channel.

#### `def __init__(self, *args)`

Create a new instance.

#### `def VOLTAGE() -> DAQAnalogChannelType`

#### `def CURRENT() -> DAQAnalogChannelType`

#### `def OTHER() -> DAQAnalogChannelType`

### `class DAQCM_Active_Edge(_DotNetEnum)`

Specifies the edge on which the sample clock pulses to acquire or generate samples.

#### `def __init__(self, *args)`

Create a new instance.

#### `def RISING() -> DAQCM_Active_Edge`

#### `def FALLING() -> DAQCM_Active_Edge`

### `class DAQCM_Clock_Source(_DotNetEnum)`

Specifies the source of the sample clock.

#### `def __init__(self, *args)`

Create a new instance.

#### `def ONBOARD10_M_HZ_CLOCK() -> DAQCM_Clock_Source`

#### `def PFI_0() -> DAQCM_Clock_Source`

#### `def PFI_1() -> DAQCM_Clock_Source`

#### `def PFI_2() -> DAQCM_Clock_Source`

#### `def PFI_3() -> DAQCM_Clock_Source`

#### `def PFI_4() -> DAQCM_Clock_Source`

#### `def PFI_5() -> DAQCM_Clock_Source`

#### `def PFI_6() -> DAQCM_Clock_Source`

#### `def PFI_7() -> DAQCM_Clock_Source`

#### `def PFI_8() -> DAQCM_Clock_Source`

#### `def PFI_9() -> DAQCM_Clock_Source`

#### `def PFI_10() -> DAQCM_Clock_Source`

#### `def PFI_11() -> DAQCM_Clock_Source`

#### `def PFI_12() -> DAQCM_Clock_Source`

#### `def PFI_13() -> DAQCM_Clock_Source`

#### `def PFI_14() -> DAQCM_Clock_Source`

#### `def PFI_15() -> DAQCM_Clock_Source`

#### `def RTSI_PXI_TRIG_0() -> DAQCM_Clock_Source`

#### `def RTSI_PXI_TRIG_1() -> DAQCM_Clock_Source`

#### `def RTSI_PXI_TRIG_2() -> DAQCM_Clock_Source`

#### `def RTSI_PXI_TRIG_3() -> DAQCM_Clock_Source`

#### `def RTSI_PXI_TRIG_4() -> DAQCM_Clock_Source`

#### `def RTSI_PXI_TRIG_5() -> DAQCM_Clock_Source`

#### `def RTSI_PXI_TRIG_6() -> DAQCM_Clock_Source`

#### `def RTSI_PXI_TRIG_7() -> DAQCM_Clock_Source`

### `class DAQCM_Export_Clk_On_Line(_DotNetEnum)`

Specifies the line that receives the pulse from the sample clock.

#### `def __init__(self, *args)`

Create a new instance.

#### `def DEFAULT_RTSI_PXI_TRIG_0() -> DAQCM_Export_Clk_On_Line`

#### `def PFI_0() -> DAQCM_Export_Clk_On_Line`

#### `def PFI_1() -> DAQCM_Export_Clk_On_Line`

#### `def PFI_2() -> DAQCM_Export_Clk_On_Line`

#### `def PFI_3() -> DAQCM_Export_Clk_On_Line`

#### `def PFI_4() -> DAQCM_Export_Clk_On_Line`

#### `def PFI_5() -> DAQCM_Export_Clk_On_Line`

#### `def PFI_6() -> DAQCM_Export_Clk_On_Line`

#### `def PFI_7() -> DAQCM_Export_Clk_On_Line`

#### `def PFI_8() -> DAQCM_Export_Clk_On_Line`

#### `def PFI_9() -> DAQCM_Export_Clk_On_Line`

#### `def PFI_10() -> DAQCM_Export_Clk_On_Line`

#### `def PFI_11() -> DAQCM_Export_Clk_On_Line`

#### `def PFI_12() -> DAQCM_Export_Clk_On_Line`

#### `def PFI_13() -> DAQCM_Export_Clk_On_Line`

#### `def PFI_14() -> DAQCM_Export_Clk_On_Line`

#### `def PFI_15() -> DAQCM_Export_Clk_On_Line`

#### `def RTSI_PXI_TRIG_0() -> DAQCM_Export_Clk_On_Line`

#### `def RTSI_PXI_TRIG_1() -> DAQCM_Export_Clk_On_Line`

#### `def RTSI_PXI_TRIG_2() -> DAQCM_Export_Clk_On_Line`

#### `def RTSI_PXI_TRIG_3() -> DAQCM_Export_Clk_On_Line`

#### `def RTSI_PXI_TRIG_4() -> DAQCM_Export_Clk_On_Line`

#### `def RTSI_PXI_TRIG_5() -> DAQCM_Export_Clk_On_Line`

#### `def RTSI_PXI_TRIG_6() -> DAQCM_Export_Clk_On_Line`

#### `def RTSI_PXI_TRIG_7() -> DAQCM_Export_Clk_On_Line`

### `class DAQCM_Export_Sample_Clock(_DotNetEnum)`

Specifies the sample clock to export.

#### `def __init__(self, *args)`

Create a new instance.

#### `def AI_SAMPLE_CLOCK() -> DAQCM_Export_Sample_Clock`

#### `def AO_SAMPLE_CLOCK() -> DAQCM_Export_Sample_Clock`

### `class DAQCM_Export_StartTrigger_On_Line(_DotNetEnum)`

Specifies the line that exports the Start Trigger.

#### `def __init__(self, *args)`

Create a new instance.

#### `def NONE() -> DAQCM_Export_StartTrigger_On_Line`

#### `def PFI_0() -> DAQCM_Export_StartTrigger_On_Line`

#### `def PFI_1() -> DAQCM_Export_StartTrigger_On_Line`

#### `def PFI_2() -> DAQCM_Export_StartTrigger_On_Line`

#### `def PFI_3() -> DAQCM_Export_StartTrigger_On_Line`

#### `def PFI_4() -> DAQCM_Export_StartTrigger_On_Line`

#### `def PFI_5() -> DAQCM_Export_StartTrigger_On_Line`

#### `def PFI_6() -> DAQCM_Export_StartTrigger_On_Line`

#### `def PFI_7() -> DAQCM_Export_StartTrigger_On_Line`

#### `def PFI_8() -> DAQCM_Export_StartTrigger_On_Line`

#### `def PFI_9() -> DAQCM_Export_StartTrigger_On_Line`

#### `def PFI_10() -> DAQCM_Export_StartTrigger_On_Line`

#### `def PFI_11() -> DAQCM_Export_StartTrigger_On_Line`

#### `def PFI_12() -> DAQCM_Export_StartTrigger_On_Line`

#### `def PFI_13() -> DAQCM_Export_StartTrigger_On_Line`

#### `def PFI_14() -> DAQCM_Export_StartTrigger_On_Line`

#### `def PFI_15() -> DAQCM_Export_StartTrigger_On_Line`

#### `def RTSI_PXI_TRIG_0() -> DAQCM_Export_StartTrigger_On_Line`

#### `def RTSI_PXI_TRIG_1() -> DAQCM_Export_StartTrigger_On_Line`

#### `def RTSI_PXI_TRIG_2() -> DAQCM_Export_StartTrigger_On_Line`

#### `def RTSI_PXI_TRIG_3() -> DAQCM_Export_StartTrigger_On_Line`

#### `def RTSI_PXI_TRIG_4() -> DAQCM_Export_StartTrigger_On_Line`

#### `def RTSI_PXI_TRIG_5() -> DAQCM_Export_StartTrigger_On_Line`

#### `def RTSI_PXI_TRIG_6() -> DAQCM_Export_StartTrigger_On_Line`

#### `def RTSI_PXI_TRIG_7() -> DAQCM_Export_StartTrigger_On_Line`

### `class DAQCM_Export_Start_Trigger(_DotNetEnum)`

Specifies the start trigger to export.

#### `def __init__(self, *args)`

Create a new instance.

#### `def AI_START_TRIGGER() -> DAQCM_Export_Start_Trigger`

#### `def AO_START_TRIGGER() -> DAQCM_Export_Start_Trigger`

### `class DAQCM_Slope(_DotNetEnum)`

Specifies the edge on which to trigger the device.

#### `def __init__(self, *args)`

Create a new instance.

#### `def RISING() -> DAQCM_Slope`

#### `def FALLING() -> DAQCM_Slope`

### `class DAQCM_Trigger_Line(_DotNetEnum)`

Specifies the line that triggers the acquisition or generation of samples.

#### `def __init__(self, *args)`

Create a new instance.

#### `def NONE() -> DAQCM_Trigger_Line`

#### `def PFI_0() -> DAQCM_Trigger_Line`

#### `def PFI_1() -> DAQCM_Trigger_Line`

#### `def PFI_2() -> DAQCM_Trigger_Line`

#### `def PFI_3() -> DAQCM_Trigger_Line`

#### `def PFI_4() -> DAQCM_Trigger_Line`

#### `def PFI_5() -> DAQCM_Trigger_Line`

#### `def PFI_6() -> DAQCM_Trigger_Line`

#### `def PFI_7() -> DAQCM_Trigger_Line`

#### `def PFI_8() -> DAQCM_Trigger_Line`

#### `def PFI_9() -> DAQCM_Trigger_Line`

#### `def PFI_10() -> DAQCM_Trigger_Line`

#### `def PFI_11() -> DAQCM_Trigger_Line`

#### `def PFI_12() -> DAQCM_Trigger_Line`

#### `def PFI_13() -> DAQCM_Trigger_Line`

#### `def PFI_14() -> DAQCM_Trigger_Line`

#### `def PFI_15() -> DAQCM_Trigger_Line`

#### `def RTSI_PXI_TRIG_0() -> DAQCM_Trigger_Line`

#### `def RTSI_PXI_TRIG_1() -> DAQCM_Trigger_Line`

#### `def RTSI_PXI_TRIG_2() -> DAQCM_Trigger_Line`

#### `def RTSI_PXI_TRIG_3() -> DAQCM_Trigger_Line`

#### `def RTSI_PXI_TRIG_4() -> DAQCM_Trigger_Line`

#### `def RTSI_PXI_TRIG_5() -> DAQCM_Trigger_Line`

#### `def RTSI_PXI_TRIG_6() -> DAQCM_Trigger_Line`

#### `def RTSI_PXI_TRIG_7() -> DAQCM_Trigger_Line`

### `class DAQConversionRate(_DotNetEnum)`

Specifies the rate used to run the analog-digital converters (ADCs) on a DAQ device.

#### `def __init__(self, *args)`

Create a new instance.

#### `def DEFAULT() -> DAQConversionRate`

#### `def MAXIMUM() -> DAQConversionRate`

### `class DAQCounterCountMode(_DotNetEnum)`

Specifies the mode of the count direction.

#### `def __init__(self, *args)`

Create a new instance.

#### `def UP() -> DAQCounterCountMode`

#### `def DOWN() -> DAQCounterCountMode`

#### `def EXTERNALLY_CONTROLLED() -> DAQCounterCountMode`

### `class DAQCounterDecoding(_DotNetEnum)`

Specifies the method used to count and interpret the pulses the encoder generates on signal A and signal B. <format type="bold">Decoding1X</format>, <format type="bold">Decoding2X</format>, and <format type="bold">Decoding4X</format> are valid for quadrature encoders only.

#### `def __init__(self, *args)`

Create a new instance.

#### `def DECODING1_X() -> DAQCounterDecoding`

#### `def DECODING2_X() -> DAQCounterDecoding`

#### `def DECODING4_X() -> DAQCounterDecoding`

#### `def DECODING_PULSE_COUNTING() -> DAQCounterDecoding`

### `class DAQCounterEdge(_DotNetEnum)`

Specifies the mode the counter uses to count the edge.

#### `def __init__(self, *args)`

Create a new instance.

#### `def FALLING() -> DAQCounterEdge`

#### `def RISING() -> DAQCounterEdge`

### `class DAQCounterType(_DotNetEnum)`

Specifies the type of task the DAQ counter performs.

#### `def __init__(self, *args)`

Create a new instance.

#### `def FREQUENCY_MEASUREMENT() -> DAQCounterType`

#### `def PERIOD_MEASUREMENT() -> DAQCounterType`

#### `def COUNT_UP_DOWN() -> DAQCounterType`

#### `def POSITION_MEASUREMENT() -> DAQCounterType`

#### `def OTHER() -> DAQCounterType`

### `class DAQCounterZIndexMode(_DotNetEnum)`

Specifies the states at which signal A and signal B must be while signal Z is high for the device to reset the measurement. If signal Z is never high while signal A and signal B are high, for example, you must choose a phase other than <format type="bold">AHighBHigh</format>. When signal Z transitions to high and how long it stays high varies from encoder to encoder. Refer to the documentation for the encoder to determine the timing of signal Z with respect to signal A and signal B.

#### `def __init__(self, *args)`

Create a new instance.

#### `def A_HIGH_B_HIGH() -> DAQCounterZIndexMode`

#### `def A_HIGH_B_LOW() -> DAQCounterZIndexMode`

#### `def A_LOW_B_HIGH() -> DAQCounterZIndexMode`

#### `def A_LOW_B_LOW() -> DAQCounterZIndexMode`

### `class DAQDataChannelType(_DotNetEnum)`

Specifies the type of data channel in a DAQ measurement <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQSectionType" /> section.

#### `def __init__(self, *args)`

Create a new instance.

#### `def FREQUENCY() -> DAQDataChannelType`

#### `def DUTY_CYCLE() -> DAQDataChannelType`

### `class DAQDeviceInputConfiguration(_DotNetEnum)`

Specifies the input terminal configuration to apply to the device channels.

#### `def __init__(self, *args)`

Create a new instance.

#### `def DEFAULT() -> DAQDeviceInputConfiguration`

#### `def RSE() -> DAQDeviceInputConfiguration`

#### `def NRSE() -> DAQDeviceInputConfiguration`

#### `def DIFFERENTIAL() -> DAQDeviceInputConfiguration`

#### `def PSEUDODIFFERENTIAL() -> DAQDeviceInputConfiguration`

### `class DAQMeasurementType(_DotNetEnum)`

Specifies the measurement type of a DAQ channel.

#### `def __init__(self, *args)`

Create a new instance.

#### `def ANALOG_INPUT_VOLTAGE() -> DAQMeasurementType`

#### `def ANALOG_INPUT_CURRENT() -> DAQMeasurementType`

#### `def ANALOG_INPUT_TEMPERATURE_THERMOCOUPLE() -> DAQMeasurementType`

#### `def ANALOG_INPUT_TEMPERATURE_THERMISTOR_VEX() -> DAQMeasurementType`

#### `def ANALOG_INPUT_TEMPERATURE_THERMISTOR_IEX() -> DAQMeasurementType`

#### `def ANALOG_INPUT_TEMPERATURE_RTD() -> DAQMeasurementType`

#### `def ANALOG_INPUT_STRAIN_GAGE() -> DAQMeasurementType`

#### `def ANALOG_INPUT_ACCELEROMETER() -> DAQMeasurementType`

#### `def ANALOG_INPUT_BRIDGE() -> DAQMeasurementType`

#### `def ANALOG_INPUT_FORCE() -> DAQMeasurementType`

#### `def ANALOG_INPUT_PRESSURE() -> DAQMeasurementType`

#### `def ANALOG_INPUT_TORQUE() -> DAQMeasurementType`

#### `def ANALOG_INPUT_POSITION_LVDT() -> DAQMeasurementType`

#### `def ANALOG_INPUT_POSITION_RVDT() -> DAQMeasurementType`

#### `def ANALOG_OUTPUT_VOLTAGE() -> DAQMeasurementType`

#### `def ANALOG_OUTPUT_CURRENT() -> DAQMeasurementType`

#### `def DIGITAL_INPUT() -> DAQMeasurementType`

#### `def DIGITAL_OUTPUT() -> DAQMeasurementType`

#### `def COUNTER_INPUT_COUNT_EDGES() -> DAQMeasurementType`

#### `def COUNTER_INPUT_FREQUENCY() -> DAQMeasurementType`

#### `def COUNTER_INPUT_PERIOD() -> DAQMeasurementType`

#### `def COUNTER_INPUT_POSITION_LINEAR_ENCODER() -> DAQMeasurementType`

#### `def COUNTER_INPUT_PULSE_MEASUREMENT() -> DAQMeasurementType`

#### `def COUNTER_OUTPUT_PULSE_GENERATION() -> DAQMeasurementType`

#### `def USER_DEFINED() -> DAQMeasurementType`

### `class DAQTrigger(_DotNetBase)`

Provides an <see langword="abstract" /> base class for different types of triggers you can use to configure a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> to start acquiring under certain conditions.

#### `def __init__(self, *args)`

Create a new instance.

#### `def trigger_type(self) -> TriggerType`

Gets the type of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTrigger" />.

### `class DAQTriggerAnalogEdge(DAQTrigger)`

Represents an analog edge trigger that can configure a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> to start acquiring under certain conditions.

#### `def __init__(self, source: str, slope: DirectionType, level: float)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def source(self) -> str`

Gets or sets the name of a virtual channel or terminal that is the source of the analog signal used as the trigger.

#### `def source(self, value: str)`

Gets or sets the name of a virtual channel or terminal that is the source of the analog signal used as the trigger.

#### `def slope(self) -> DirectionType`

Gets or sets the direction of a signal slope that causes a trigger when the signal crosses the threshold <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogEdge.Level" />.

#### `def slope(self, value: DirectionType)`

Gets or sets the direction of a signal slope that causes a trigger when the signal crosses the threshold <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogEdge.Level" />.

#### `def level(self) -> float`

Gets or sets the threshold value, in the units of the measurement, at which to start acquiring samples. Set the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogEdge.Slope" /> to specify on which type of slope this level causes the task to start acquiring data.

#### `def level(self, value: float)`

Gets or sets the threshold value, in the units of the measurement, at which to start acquiring samples. Set the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogEdge.Slope" /> to specify on which type of slope this level causes the task to start acquiring data.

### `class DAQTriggerAnalogWindow(DAQTrigger)`

Represents an analog window trigger that can configure a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> to start acquiring under certain conditions.

#### `def __init__(self, source: str, window_top: float, window_bottom: float, window_condition: WindowConditionType)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def source(self) -> str`

Gets or sets the name of a virtual channel or terminal that is the source of the analog signal used as the trigger.

#### `def source(self, value: str)`

Gets or sets the name of a virtual channel or terminal that is the source of the analog signal used as the trigger.

#### `def window_condition(self) -> WindowConditionType`

Gets or sets whether the task starts acquiring samples when the signal enters the window between <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogWindow.WindowBottom" /> and <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogWindow.WindowTop" /> or when it leaves the window.

#### `def window_condition(self, value: WindowConditionType)`

Gets or sets whether the task starts acquiring samples when the signal enters the window between <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogWindow.WindowBottom" /> and <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggerAnalogWindow.WindowTop" /> or when it leaves the window.

#### `def window_top(self) -> float`

Gets or sets the upper limit of the window, in the units of the measurement.

#### `def window_top(self, value: float)`

Gets or sets the upper limit of the window, in the units of the measurement.

#### `def window_bottom(self) -> float`

Gets or sets the lower limit of the window, in the units of the measurement.

#### `def window_bottom(self, value: float)`

Gets or sets the lower limit of the window, in the units of the measurement.

### `class DAQTriggerDigitalEdge(DAQTrigger)`

Represents a digital edge trigger that can configure a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> to start acquiring under certain conditions.

#### `def __init__(self, source: str, edge: DirectionType)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def source(self) -> str`

Gets or sets the name of a terminal that is the source of the digital signal used as the trigger.

#### `def source(self, value: str)`

Gets or sets the name of a terminal that is the source of the digital signal used as the trigger.

#### `def edge(self) -> DirectionType`

Gets or sets on which type of edge of the digital signal to start acquiring samples.

#### `def edge(self, value: DirectionType)`

Gets or sets on which type of edge of the digital signal to start acquiring samples.

### `class DAQTriggerNone(DAQTrigger)`

Represents a disabled <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTrigger" />.

#### `def __init__(self)`

#### `def __init__(self, *args)`

Create a new instance.

### `class DAQTriggerSoftware(DAQTrigger)`

Represents a software trigger that can configure a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> to start acquiring under certain conditions.

#### `def __init__(self)`

#### `def __init__(self, *args)`

Create a new instance.

### `class DataLoggingFilterType(_DotNetEnum)`

Specifies the type of filtering applied to a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" /> under an NI-XNET port.

#### `def __init__(self, *args)`

Create a new instance.

#### `def LOG_ENTIRE_BUS_TRAFFIC() -> DataLoggingFilterType`

#### `def EXCLUDE_FRAME_I_DS() -> DataLoggingFilterType`

#### `def INCLUDE_FRAME_I_DS() -> DataLoggingFilterType`

### `class DataLoggingOperationType(_DotNetEnum)`

Specifies the action taken when a trigger condition is met.

#### `def __init__(self, *args)`

Create a new instance.

#### `def CONTINUE_LOGGING_IN_NEW_FILE() -> DataLoggingOperationType`

#### `def STOP_LOGGING() -> DataLoggingOperationType`

### `class DataLoggingTriggerType(_DotNetEnum)`

Specifies the type of trigger used to start or stop logging data to a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" />.

#### `def __init__(self, *args)`

Create a new instance.

#### `def START_LOGGING_ON_NON_ZERO() -> DataLoggingTriggerType`

#### `def START_LOGGING_ON_ZERO() -> DataLoggingTriggerType`

#### `def ENABLE_LOGGING_WHEN_TRIGGER_IS_ZERO() -> DataLoggingTriggerType`

#### `def ENABLE_LOGGING_WHEN_TRIGGER_IS_NON_ZERO() -> DataLoggingTriggerType`

### `class Delimiter(_DotNetEnum)`

Defines the delimiter of the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFile" crefType="PartiallyQualified" />.

#### `def __init__(self, *args)`

Create a new instance.

#### `def TAB() -> Delimiter`

#### `def EQUALS() -> Delimiter`

#### `def COMMA() -> Delimiter`

### `class DependentFile(_DotNetBase)`

Represents a dependent file, which can be any file that another node requires. For example, model files, bitfiles, and VIs that make up custom devices can all be dependent files.

#### `def __init__(self, file_path: str, version: str, force_download: bool, rt_destination: str, supported_target: str, md5: str)`

#### `def __init__(self, file_path: str, type: DependentFileType, version: str, force_download: bool, rt_destination: str, supported_target: str, md5: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def path(self) -> str`

Gets the path to the file on the host computer.

#### `def type(self) -> DependentFileType`

Gets whether the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DependentFile.Path" crefType="Unqualified" /> to the dependent file is absolute or relative to another directory.

#### `def version(self) -> str`

Gets or sets version information for the dependent file.

#### `def version(self, value: str)`

Gets or sets version information for the dependent file.

#### `def force_download(self) -> bool`

Gets or sets whether the file is set to force-download to the target.

#### `def force_download(self, value: bool)`

Gets or sets whether the file is set to force-download to the target.

#### `def rt_destination(self) -> str`

Gets or sets the destination path, including the filename, for the file on the target. This property must be an absolute path.

#### `def rt_destination(self, value: str)`

Gets or sets the destination path, including the filename, for the file on the target. This property must be an absolute path.

#### `def supported_target(self) -> str`

Gets or sets the target operating system(s) to which the file is deployed.

#### `def supported_target(self, value: str)`

Gets or sets the target operating system(s) to which the file is deployed.

#### `def md5(self) -> str`

Gets or sets the MD5 message-digest for the file.

#### `def md5(self, value: str)`

Gets or sets the MD5 message-digest for the file.

#### `def set_path(self, file_path: str, sdf_path: str)`

#### `def set_path(self, *args)`

#### `def get_absolute_path(self, base_absolute_path: str) -> str`

#### `def get_absolute_path(self, *args)`

### `class DependentFileType(_DotNetEnum)`

Specifies the type of path used for the location of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DependentFile" crefType="Unqualified" />.

#### `def __init__(self, *args)`

Create a new instance.

#### `def ABSOLUTE() -> DependentFileType`

#### `def RELATIVE() -> DependentFileType`

#### `def TO_COMMON_DOC_DIR() -> DependentFileType`

#### `def TO_APP_DATA_DIR() -> DependentFileType`

### `class Dictionary(_DotNetBase)`

Represents a dictionary, which is an associative array. You can set dictionaries as values for <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDevice" crefType="Unqualified" /> and <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.TimingAndSyncDevice" crefType="Unqualified" /> items.

#### `def __init__(self)`

#### `def __init__(self, to_copy: Dictionary)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def count(self) -> int`

Gets the total number of key/value pairs in a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Dictionary" crefType="Unqualified" />.

#### `def elem(self) -> Sequence[DictionaryElement]`

Gets all the elements in the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Dictionary" crefType="Unqualified" />.

#### `def add_boolean(self, name: str, value: bool) -> bool`

#### `def add_boolean(self, *args)`

#### `def add_boolean_array(self, name: str, value: Sequence[bool]) -> bool`

#### `def add_boolean_array(self, *args)`

#### `def add_u16(self, name: str, value: int) -> bool`

#### `def add_u16(self, *args)`

#### `def add_u16_array(self, name: str, value: Sequence[int]) -> bool`

#### `def add_u16_array(self, *args)`

#### `def add_u32(self, name: str, value: int) -> bool`

#### `def add_u32(self, *args)`

#### `def add_u32_array(self, name: str, value: Sequence[int]) -> bool`

#### `def add_u32_array(self, *args)`

#### `def add_u64(self, name: str, value: int) -> bool`

#### `def add_u64(self, *args)`

#### `def add_u64_array(self, name: str, value: Sequence[int]) -> bool`

#### `def add_u64_array(self, *args)`

#### `def add_i16(self, name: str, value: int) -> bool`

#### `def add_i16(self, *args)`

#### `def add_i16_array(self, name: str, value: Sequence[int]) -> bool`

#### `def add_i16_array(self, *args)`

#### `def add_i32(self, name: str, value: int) -> bool`

#### `def add_i32(self, *args)`

#### `def add_i32_array(self, name: str, value: Sequence[int]) -> bool`

#### `def add_i32_array(self, *args)`

#### `def add_i64(self, name: str, value: int) -> bool`

#### `def add_i64(self, *args)`

#### `def add_i64_array(self, name: str, value: Sequence[int]) -> bool`

#### `def add_i64_array(self, *args)`

#### `def add_double(self, name: str, value: float) -> bool`

#### `def add_double(self, *args)`

#### `def add_double_array(self, name: str, value: Sequence[float]) -> bool`

#### `def add_double_array(self, *args)`

#### `def add_string(self, name: str, value: str) -> bool`

#### `def add_string(self, *args)`

#### `def add_string_array(self, name: str, value: Sequence[str]) -> bool`

#### `def add_string_array(self, *args)`

#### `def clear(self)`

#### `def clear(self, *args)`

#### `def get_boolean(self, name: str) -> Tuple[bool, bool]`

#### `def get_boolean(self, *args)`

#### `def get_boolean_array(self, name: str) -> Tuple[bool, Sequence[bool]]`

#### `def get_boolean_array(self, *args)`

#### `def get_u16(self, name: str) -> Tuple[bool, int]`

#### `def get_u16(self, *args)`

#### `def get_u16_array(self, name: str) -> Tuple[bool, Sequence[int]]`

#### `def get_u16_array(self, *args)`

#### `def get_u32(self, name: str) -> Tuple[bool, int]`

#### `def get_u32(self, *args)`

#### `def get_u32_array(self, name: str) -> Tuple[bool, Sequence[int]]`

#### `def get_u32_array(self, *args)`

#### `def get_u64(self, name: str) -> Tuple[bool, int]`

#### `def get_u64(self, *args)`

#### `def get_u64_array(self, name: str) -> Tuple[bool, Sequence[int]]`

#### `def get_u64_array(self, *args)`

#### `def get_i16(self, name: str) -> Tuple[bool, int]`

#### `def get_i16(self, *args)`

#### `def get_i16_array(self, name: str) -> Tuple[bool, Sequence[int]]`

#### `def get_i16_array(self, *args)`

#### `def get_i32(self, name: str) -> Tuple[bool, int]`

#### `def get_i32(self, *args)`

#### `def get_i32_array(self, name: str) -> Tuple[bool, Sequence[int]]`

#### `def get_i32_array(self, *args)`

#### `def get_i64(self, name: str) -> Tuple[bool, int]`

#### `def get_i64(self, *args)`

#### `def get_i64_array(self, name: str) -> Tuple[bool, Sequence[int]]`

#### `def get_i64_array(self, *args)`

#### `def get_double(self, name: str) -> Tuple[bool, float]`

#### `def get_double(self, *args)`

#### `def get_double_array(self, name: str) -> Tuple[bool, Sequence[float]]`

#### `def get_double_array(self, *args)`

#### `def get_string(self, name: str) -> Tuple[bool, str]`

#### `def get_string(self, *args)`

#### `def get_string_array(self, name: str) -> Tuple[bool, Sequence[str]]`

#### `def get_string_array(self, *args)`

#### `def remove_element(self, key: str) -> bool`

#### `def remove_element(self, *args)`

### `class DictionaryElement(_DotNetBase)`

Represents an element, or a key/value pair, in a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Dictionary" crefType="Unqualified" />.

#### `def __init__(self, to_copy: DictionaryElement)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def item(self) -> Any`

Gets or sets a reference to a value of a dictionary element.

#### `def item(self, value: Any)`

Gets or sets a reference to a value of a dictionary element.

#### `def key(self) -> str`

Gets or sets the key, or name, of a dictionary element.

#### `def key(self, value: str)`

Gets or sets the key, or name, of a dictionary element.

### `class DirectionType(_DotNetEnum)`

Defines the direction of a signal slope or edge that causes a trigger.

#### `def __init__(self, *args)`

Create a new instance.

#### `def RISING() -> DirectionType`

#### `def FALLING() -> DirectionType`

### `class EdgeType(_DotNetEnum)`

Defines the edge type of the sample clock.

#### `def __init__(self, *args)`

Create a new instance.

#### `def RISING() -> EdgeType`

#### `def FALLING() -> EdgeType`

### `class FDISOMode(_DotNetEnum)`

Specifies whether the interface is working in the ISO CAN FD standard (ISO standard 11898-1:2015)
            or non-ISO CAN FD standard (Bosch CAN FD 1.0 specification). Two ports using different standards
            (ISO CAN FD vs. non-ISO CAN FD) cannot communicate with each other.

#### `def __init__(self, *args)`

Create a new instance.

#### `def ISO() -> FDISOMode`

#### `def NON_ISO() -> FDISOMode`

#### `def ISO_LEGACY() -> FDISOMode`

### `class FileLimitationType(_DotNetEnum)`

Specifies the type of limit used to stop logging incoming frame data to an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" />.

#### `def __init__(self, *args)`

Create a new instance.

#### `def FOOTPRINT() -> FileLimitationType`

#### `def TIME() -> FileLimitationType`

### `class FileType(_DotNetEnum)`

Specifies the file type of an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" />.

#### `def __init__(self, *args)`

Create a new instance.

#### `def TDMS() -> FileType`

#### `def NCL() -> FileType`

### `class FramePhaseType(_DotNetEnum)`

Specifies whether to reset the timer of a software cyclic trigger after each transmission of an outgoing frame.

#### `def __init__(self, *args)`

Create a new instance.

#### `def UNCHANGED() -> FramePhaseType`

#### `def RESET() -> FramePhaseType`

### `class FrameTriggerType(_DotNetEnum)`

Specifies a condition that a trigger channel must meet to trigger transmission of an outgoing frame.

#### `def __init__(self, *args)`

Create a new instance.

#### `def CHANNEL_VALUE_CHANGE() -> FrameTriggerType`

#### `def TRIGGER_CHANNEL_NOT_ZERO() -> FrameTriggerType`

#### `def CHANNEL_VALUE_CHANGE_OR_TRIGGER_CHANNEL_NOT_ZERO() -> FrameTriggerType`

#### `def TRIGGER_CHANNEL_ANY_VALUE_CHANGE() -> FrameTriggerType`

#### `def CHANNEL_VALUE_CHANGE_OR_TRIGGER_CHANNEL_ANY_VALUE_CHANGE() -> FrameTriggerType`

### `class FrameType(_DotNetEnum)`

Specifies the type of a CAN or FlexRay frame.

#### `def __init__(self, *args)`

Create a new instance.

#### `def CAN_DATA_FRAME() -> FrameType`

#### `def CAN_REMOTE_FRAME() -> FrameType`

#### `def FLEX_RAY_DATA_FRAME() -> FrameType`

#### `def FLEX_RAY_NULL_FRAME() -> FrameType`

### `class GlobalParameterScopes(_DotNetEnum)`

Specifies whether global parameters in a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Model" /> share their values with other models.

#### `def __init__(self, *args)`

Create a new instance.

#### `def TARGET() -> GlobalParameterScopes`

#### `def MODEL() -> GlobalParameterScopes`

### `class GlobalSequenceCommand(_DotNetEnum)`

Specifies the command for all running sequences.

#### `def __init__(self, *args)`

Create a new instance.

#### `def STOP_ALL() -> GlobalSequenceCommand`

#### `def ABORT_ALL() -> GlobalSequenceCommand`

#### `def STOP_GROUP() -> GlobalSequenceCommand`

### `class ICANConfiguration(_DotNetBase)`

Represents the configuration for CAN communication.

#### `def __init__(self, *args)`

Create a new instance.

#### `def io_mode(self) -> CANIOMode`

Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANIOMode" />.

#### `def io_mode(self, value: CANIOMode)`

Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANIOMode" />.

#### `def xnet_interface(self) -> str`

Gets or sets the XNET Interface to be used to connect to the real network.

#### `def xnet_interface(self, value: str)`

Gets or sets the XNET Interface to be used to connect to the real network.

#### `def baud_rate(self) -> int`

Gets or sets the CAN baud rate.

#### `def baud_rate(self, value: int)`

Gets or sets the CAN baud rate.

#### `def brs_baud_rate(self) -> int`

Gets or sets the CAN-BRS baud rate.

#### `def brs_baud_rate(self, value: int)`

Gets or sets the CAN-BRS baud rate.

#### `def transceiver_type(self) -> CANTransceiverType`

Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransceiverType" />.

#### `def transceiver_type(self, value: CANTransceiverType)`

Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransceiverType" />.

#### `def fdiso_mode(self) -> FDISOMode`

Gets or sets the CAN <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FDISOMode" />.

#### `def fdiso_mode(self, value: FDISOMode)`

Gets or sets the CAN <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FDISOMode" />.

### `class IChannel(_DotNetBase)`

An interface defining system definition channel behavior

#### `def __init__(self, *args)`

Create a new instance.

#### `def data_source(self) -> BaseNode`

Gets or sets the source channel that maps to the current channel and provides it data.

#### `def data_source(self, value: BaseNode)`

Gets or sets the source channel that maps to the current channel and provides it data.

#### `def column_dimensions(self) -> int`

Gets the number of columns in the channel value.

#### `def row_dimensions(self) -> int`

Gets the number of rows in the channel value.

#### `def units(self) -> str`

Gets or sets the units associated with the channel. This can be any arbitrary string.

#### `def units(self, value: str)`

Gets or sets the units associated with the channel. This can be any arbitrary string.

#### `def is_readable(self) -> bool`

Gets a value indicating whether the channel is readable.

#### `def is_writable(self) -> bool`

Gets a value indicating whether the channel is writable.

#### `def scale_units(self) -> str`

Gets the units of the scale associated with the channel.

#### `def remove_data_source(self)`

#### `def remove_data_source(self, *args)`

#### `def get_value_table(self) -> Tuple[bool, Sequence[str], Sequence[float]]`

#### `def get_value_table(self, *args)`

### `class IECUNetworkClusterConfiguration(_DotNetBase)`

Interface for an ECU network cluster configuration.

#### `def __init__(self, *args)`

Create a new instance.

#### `def cluster_name(self) -> str`

Gets or sets the name of the ECU Network Cluster.

#### `def cluster_name(self, value: str)`

Gets or sets the name of the ECU Network Cluster.

#### `def time_step(self) -> float`

Gets or sets the time interval between two successive network steps where frames are exchanged between real and virtual ECUs.

#### `def time_step(self, value: float)`

Gets or sets the time interval between two successive network steps where frames are exchanged between real and virtual ECUs.

#### `def protocol(self) -> CommunicationProtocol`

Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CommunicationProtocol" /> used by the ECU network cluster.

#### `def protocol(self, value: CommunicationProtocol)`

Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CommunicationProtocol" /> used by the ECU network cluster.

#### `def virtual_ecu_toolchain(self) -> VirtualECUToolchain`

Gets or sets the name of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.VirtualECUToolchain" /> that was used to build virtual ECUs.

#### `def virtual_ecu_toolchain(self, value: VirtualECUToolchain)`

Gets or sets the name of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.VirtualECUToolchain" /> that was used to build virtual ECUs.

#### `def can_configuration(self) -> ICANConfiguration`

Represents the protocol specific configuration when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.ECUNetworkCluster.Protocol" /> is set to CAN.

#### `def lin_configuration(self) -> ILINConfiguration`

Represents the protocol specific configuration when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.ECUNetworkCluster.Protocol" /> is set to LIN.

#### `def ethernet_configuration(self) -> IEthernetConfiguration`

Represents the protocol specific configuration when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.ECUNetworkCluster.Protocol" /> is set to Ethernet.

#### `def add_virtual_ecu(self, virtual_ecu_name: str)`

#### `def add_virtual_ecu(self, *args)`

#### `def remove_virtual_ecu(self, virtual_ecu_name: str)`

#### `def remove_virtual_ecu(self, *args)`

#### `def get_virtual_ec_us(self) -> Sequence[str]`

#### `def get_virtual_ec_us(self, *args)`

### `class IEthernetConfiguration(_DotNetBase)`

Represents the configuration for Ethernet communication.

#### `def __init__(self, *args)`

Create a new instance.

#### `def xnet_interface(self) -> str`

Gets or sets the XNET Interface to be used to connect to the real network.

#### `def xnet_interface(self, value: str)`

Gets or sets the XNET Interface to be used to connect to the real network.

#### `def add_virtual_ecumac_address(self, virtual_ecumac_address: str)`

#### `def add_virtual_ecumac_address(self, *args)`

#### `def remove_virtual_ecumac_address(self, virtual_ecumac_address: str)`

#### `def remove_virtual_ecumac_address(self, *args)`

#### `def get_virtual_ecumac_addresses(self) -> Sequence[str]`

#### `def get_virtual_ecumac_addresses(self, *args)`

### `class ILINConfiguration(_DotNetBase)`

Represents the configuration for LIN communication.

#### `def __init__(self, *args)`

Create a new instance.

#### `def xnet_interface(self) -> str`

Gets or sets the XNET Interface to be used to connect to the real network.

#### `def xnet_interface(self, value: str)`

Gets or sets the XNET Interface to be used to connect to the real network.

#### `def baud_rate(self) -> int`

Gets or sets the LIN baud rate.

#### `def baud_rate(self, value: int)`

Gets or sets the LIN baud rate.

#### `def add_virtual_tx_frame_id(self, virtual_tx_frame_id: int)`

#### `def add_virtual_tx_frame_id(self, *args)`

#### `def remove_virtual_tx_frame_id(self, virtual_tx_frame_id: int)`

#### `def remove_virtual_tx_frame_id(self, *args)`

#### `def get_virtual_tx_frame_i_ds(self) -> Sequence[int]`

#### `def get_virtual_tx_frame_i_ds(self, *args)`

### `class LUTValue(_DotNetBase)`

Represents a pair of values in a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.LookupTable" /> scale: a pre-scaled value and the corresponding scaled value.

#### `def __init__(self)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def pre_scaled(self) -> float`

Gets or sets the pre-scaled LUTValue.

#### `def pre_scaled(self, value: float)`

Gets or sets the pre-scaled LUTValue.

#### `def scaled(self) -> float`

Gets or sets the scaled LUTValue.

#### `def scaled(self, value: float)`

Gets or sets the scaled LUTValue.

### `class LogMode(_DotNetEnum)`

The logging mode that determines whether components in the NI VeriStand system can read data as you log it.

#### `def __init__(self, *args)`

Create a new instance.

#### `def LOG() -> LogMode`

#### `def LOG_AND_READ() -> LogMode`

### `class ModelCommandState(_DotNetEnum)`

Specifies the current state of the model.

#### `def __init__(self, *args)`

Create a new instance.

#### `def START() -> ModelCommandState`

#### `def PAUSE() -> ModelCommandState`

#### `def RESET() -> ModelCommandState`

#### `def SAVE() -> ModelCommandState`

#### `def RESTORE() -> ModelCommandState`

### `class NodeIDUtil(_DotNetBase)`

Provides methods for converting node IDs, or pointers, to nodes in a system definition file into item references to the same node.

#### `def __init__(self)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def id_to_base_node(node_id: int) -> BaseNode`

#### `def id_to_base_node(*args)`

#### `def id_to_custom_device_base(node_id: int) -> CustomDeviceBase`

#### `def id_to_custom_device_base(*args)`

#### `def id_to_custom_device_channel(node_id: int) -> CustomDeviceChannel`

#### `def id_to_custom_device_channel(*args)`

#### `def id_to_custom_device_waveform(node_id: int) -> CustomDeviceWaveform`

#### `def id_to_custom_device_waveform(*args)`

#### `def id_to_custom_device_section(node_id: int) -> CustomDeviceSection`

#### `def id_to_custom_device_section(*args)`

#### `def id_to_custom_device(node_id: int) -> CustomDevice`

#### `def id_to_custom_device(*args)`

#### `def id_to_timing_sync_device(node_id: int) -> TimingAndSyncDevice`

#### `def id_to_timing_sync_device(*args)`

### `class PXIBackplaneReferenceClock(_DotNetEnum)`

Specifies the PXI chassis backplane reference clock.

#### `def __init__(self, *args)`

Create a new instance.

#### `def AUTOMATIC() -> PXIBackplaneReferenceClock`

#### `def NONE() -> PXIBackplaneReferenceClock`

#### `def CLK10() -> PXIBackplaneReferenceClock`

#### `def CLK100() -> PXIBackplaneReferenceClock`

### `class ParameterAccess(_DotNetEnum)`

Defines the parameter access mode on the engine. The user can select to access only the imported parameters or all the parameters from the models.

#### `def __init__(self, *args)`

Create a new instance.

#### `def ONLY_IMPORTED_PARAMETERS() -> ParameterAccess`

#### `def ANY_PARAMETER() -> ParameterAccess`

### `class ReflectiveMemoryDataChannelAccessType(_DotNetEnum)`

Specifies the access type (read or write) of a data channel on a reflective memory device.

#### `def __init__(self, *args)`

Create a new instance.

#### `def READ() -> ReflectiveMemoryDataChannelAccessType`

#### `def WRITE() -> ReflectiveMemoryDataChannelAccessType`

### `class ReflectiveMemoryDataChannelDataType(_DotNetEnum)`

Specifies the data type of a data channel on a reflective memory device.

#### `def __init__(self, *args)`

Create a new instance.

#### `def U_INT8() -> ReflectiveMemoryDataChannelDataType`

#### `def INT8() -> ReflectiveMemoryDataChannelDataType`

#### `def U_INT16() -> ReflectiveMemoryDataChannelDataType`

#### `def INT16() -> ReflectiveMemoryDataChannelDataType`

#### `def U_INT32() -> ReflectiveMemoryDataChannelDataType`

#### `def INT32() -> ReflectiveMemoryDataChannelDataType`

#### `def U_INT64() -> ReflectiveMemoryDataChannelDataType`

#### `def INT64() -> ReflectiveMemoryDataChannelDataType`

#### `def DOUBLE() -> ReflectiveMemoryDataChannelDataType`

### `class ReflectiveMemoryInterruptType(_DotNetEnum)`

Specifies the type of interrupt a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemory" crefType="Unqualified" /> device sends or receives.

#### `def __init__(self, *args)`

Create a new instance.

#### `def LINK_RESET_INTERRUPT() -> ReflectiveMemoryInterruptType`

#### `def NETWORK_INTERRUPT1() -> ReflectiveMemoryInterruptType`

#### `def NETWORK_INTERRUPT2() -> ReflectiveMemoryInterruptType`

#### `def NETWORK_INTERRUPT3() -> ReflectiveMemoryInterruptType`

#### `def NETWORK_INIT_INTERRUPT() -> ReflectiveMemoryInterruptType`

### `class ReplayBehavior(_DotNetEnum)`

Specifies whether and how frames in a data replay file on an NI-XNET CAN port are filtered.

#### `def __init__(self, *args)`

Create a new instance.

#### `def REPLAY_ENTIRE_FILE() -> ReplayBehavior`

#### `def EXCLUDE_FRAME_I_DS() -> ReplayBehavior`

#### `def INCLUDE_FRAME_I_DS() -> ReplayBehavior`

### `class Root(BaseNode)`

Represents the root node of the system definition.

#### `def __init__(self, *args)`

Create a new instance.

#### `def version(self) -> str`

Gets or sets the system definition file version number.

#### `def version(self, value: str)`

Gets or sets the system definition file version number.

#### `def creator(self) -> str`

Gets or sets the user account name of the system definition file creator.

#### `def creator(self, value: str)`

Gets or sets the user account name of the system definition file creator.

#### `def creation_date(self) -> float`

Gets or sets the creation date of the system definition file.

#### `def creation_date(self, value: float)`

Gets or sets the creation date of the system definition file.

#### `def delete_channel_mappings(self, channel_path_destinations: Sequence[str])`

#### `def delete_channel_mappings(self, *args)`

#### `def add_channel_mappings(self, channel_path_sources: Sequence[str], channel_path_destinations: Sequence[str]) -> bool`

#### `def add_channel_mappings(self, *args)`

#### `def get_channel_mappings(self) -> Tuple[Sequence[str], Sequence[str]]`

#### `def get_channel_mappings(self, *args)`

#### `def clear_channel_mappings(self)`

#### `def clear_channel_mappings(self, *args)`

#### `def get_targets(self) -> Targets`

#### `def get_targets(self, *args)`

#### `def refresh_node_dependencies(self)`

#### `def refresh_node_dependencies(self, *args)`

#### `def get_aliases(self) -> Aliases`

#### `def get_aliases(self, *args)`

#### `def get_scales(self) -> Scales`

#### `def get_scales(self, *args)`

#### `def get_system_mappings(self) -> SystemMappings`

#### `def get_system_mappings(self, *args)`

#### `def get_data_sharing_network(self) -> DataSharingNetwork`

#### `def get_data_sharing_network(self, *args)`

#### `def get_system_initialization(self) -> SystemInitialization`

#### `def get_system_initialization(self, *args)`

### `class SampleMode(_DotNetEnum)`

Whether the AI acquisition is single-point or buffered.

#### `def __init__(self, *args)`

Create a new instance.

#### `def SINGLE_POINT() -> SampleMode`

#### `def WAVEFORM() -> SampleMode`

### `class ScaleType(_DotNetEnum)`

This enumeration is used to select the Scale Type.

#### `def __init__(self, *args)`

Create a new instance.

#### `def POLYNOMIAL() -> ScaleType`

#### `def THERMOCOUPLE() -> ScaleType`

#### `def LOOKUP_TABLE() -> ScaleType`

### `class Section(BaseNode)`

Represents a section or node in the system definition. A section represents any node that contains additional nodes.

#### `def __init__(self, *args)`

Create a new instance.

### `class SetVariableStepFunction(_DotNetEnum)`

Specifies the function to use on <format type="italics">Value1</format> and <format type="italics">Value2</format> of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable" crefType="Unqualified" /> procedure step.

#### `def __init__(self, *args)`

Create a new instance.

#### `def NONE() -> SetVariableStepFunction`

#### `def ADD() -> SetVariableStepFunction`

#### `def SUBTRACT() -> SetVariableStepFunction`

#### `def MULTIPLY() -> SetVariableStepFunction`

#### `def DIVIDE() -> SetVariableStepFunction`

### `class SignalBasedFrame(Section)`

Represents a signal format frame under an NI-XNET LIN, FlexRay, or CAN port.

#### `def __init__(self, name: str, id: int, owning_database: Database, cluster_name: str, payload_length: int, start_time_offset: float, enable64_bit: bool, signal_names: Sequence[str])`

#### `def __init__(self, *args)`

Create a new instance.

#### `def transmit_trigger(self) -> FrameTriggerType`

Gets the trigger type (channel value change, trigger channel not zero, and so on) specified for an event-triggered frame.

#### `def phase(self) -> FramePhaseType`

Gets or sets whether to reset the timer after <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.TransmitTime" crefType="Unqualified" /> elapses when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.EnableSoftwareCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />.

#### `def phase(self, value: FramePhaseType)`

Gets or sets whether to reset the timer after <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.TransmitTime" crefType="Unqualified" /> elapses when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.EnableSoftwareCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />.

#### `def frame_type(self) -> FrameType`

Gets or sets the frame type (CAN data, CAN remote, FlexRay data, or FlexRay null) of a frame under a CAN or FlexRay port.

#### `def frame_type(self, value: FrameType)`

Gets or sets the frame type (CAN data, CAN remote, FlexRay data, or FlexRay null) of a frame under a CAN or FlexRay port.

#### `def id(self) -> int`

Gets or sets the identifier number for the frame. For LIN frames, this is the frame ID. For CAN frames, this is the Arbitration ID. For FlexRay frames, this is the Slot ID in which the frame is sent.

#### `def id(self, value: int)`

Gets or sets the identifier number for the frame. For LIN frames, this is the frame ID. For CAN frames, this is the Arbitration ID. For FlexRay frames, this is the Slot ID in which the frame is sent.

#### `def payload_length(self) -> int`

Gets or sets the number of bytes in the payload of the frame.

#### `def payload_length(self, value: int)`

Gets or sets the number of bytes in the payload of the frame.

#### `def md5(self) -> Sequence[int]`

Gets the MD5 message digest for the frame.

#### `def start_time_offset(self) -> float`

Gets or sets the amount of time that elapses between the session start and the transmission of the first frame.

#### `def start_time_offset(self, value: float)`

Gets or sets the amount of time that elapses between the session start and the transmission of the first frame.

#### `def enable64_bit(self) -> bool`

Gets or sets whether U64 bitfield representation is enabled for the frame.

#### `def enable64_bit(self, value: bool)`

Gets or sets whether U64 bitfield representation is enabled for the frame.

#### `def owning_database(self) -> BaseNode`

Gets or sets a reference to the XNET database that contains the frame.

#### `def owning_database(self, value: BaseNode)`

Gets or sets a reference to the XNET database that contains the frame.

#### `def cluster_name(self) -> str`

Gets or sets the name of the cluster in the XNET database that contains the frame.

#### `def cluster_name(self, value: str)`

Gets or sets the name of the cluster in the XNET database that contains the frame.

#### `def database_alias(self) -> str`

Gets or sets the alias for the XNET database that contains the frame.

#### `def database_alias(self, value: str)`

Gets or sets the alias for the XNET database that contains the frame.

#### `def disabled(self) -> bool`

Gets whether transmission of the outgoing frame is disabled.

#### `def disable_channel(self) -> BaseNode`

Gets a reference to the disable channel for the frame. A disable channel disables transmission of an outgoing frame when the value of the disable channel is non-zero.

#### `def trigger_channel(self) -> BaseNode`

Gets a reference to the channel that is checked for a non-zero value when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.EnableFrameCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />.

#### `def enable_software_cyclic_trigger(self) -> bool`

Gets or sets whether a software cyclic trigger, which transmits outgoing frames at regular intervals specified by <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.TransmitTime" crefType="Unqualified" />, is enabled for the frame.

#### `def enable_software_cyclic_trigger(self, value: bool)`

Gets or sets whether a software cyclic trigger, which transmits outgoing frames at regular intervals specified by <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.TransmitTime" crefType="Unqualified" />, is enabled for the frame.

#### `def enable_frame_cyclic_trigger(self) -> bool`

Gets or sets whether a frame cyclic trigger, which transmits outgoing frames when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.TriggerChannel" crefType="Unqualified" /> has a non-zero value, is enabled for the frame.

#### `def enable_frame_cyclic_trigger(self, value: bool)`

Gets or sets whether a frame cyclic trigger, which transmits outgoing frames when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.TriggerChannel" crefType="Unqualified" /> has a non-zero value, is enabled for the frame.

#### `def transmit_time(self) -> float`

Gets or sets the interval, in seconds, at which a software cyclic trigger transmits outgoing frames when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.EnableSoftwareCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />.

#### `def transmit_time(self, value: float)`

Gets or sets the interval, in seconds, at which a software cyclic trigger transmits outgoing frames when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame.EnableSoftwareCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />.

#### `def create_multiplexer(self, multiplexer_value: int) -> Multiplexer`

#### `def create_multiplexer(self, multiplexer_value: int, signal_name: str) -> Multiplexer`

#### `def create_multiplexer(self, *args)`

#### `def create_mode(self, multiplexer_value: int, signal_name: str, description: str, units: str, default_value: float) -> Mode`

#### `def create_mode(self, *args)`

#### `def create_signal_based_signal(self, name: str, description: str, units: str, default_value: float) -> SignalBasedSignal`

#### `def create_signal_based_signal(self, *args)`

#### `def create_frame_information(self) -> FrameInformation`

#### `def create_frame_information(self, *args)`

#### `def create_frame_faulting(self, create_skip_cyclic_frames: bool, create_transmit_time: bool) -> FrameFaulting`

#### `def create_frame_faulting(self, *args)`

#### `def create_automatic_frame_processing(self) -> AutomaticFrameProcessing`

#### `def create_automatic_frame_processing(self, *args)`

#### `def enable_transmission(self)`

#### `def enable_transmission(self, *args)`

#### `def disable_transmission(self, disable_channel: BaseNode)`

#### `def disable_transmission(self, *args)`

#### `def set_transmit_trigger(self, trigger_type: FrameTriggerType, trigger_channel: BaseNode)`

#### `def set_transmit_trigger(self, *args)`

#### `def get_multiplexer(self) -> Multiplexer`

#### `def get_multiplexer(self, *args)`

#### `def get_mode_list(self) -> Sequence[Mode]`

#### `def get_mode_list(self, *args)`

#### `def get_signal_based_signal_list(self) -> Sequence[SignalBasedSignal]`

#### `def get_signal_based_signal_list(self, *args)`

#### `def get_frame_information(self) -> FrameInformation`

#### `def get_frame_information(self, *args)`

#### `def get_frame_faulting(self) -> FrameFaulting`

#### `def get_frame_faulting(self, *args)`

#### `def get_automatic_frame_processing(self) -> AutomaticFrameProcessing`

#### `def get_automatic_frame_processing(self, *args)`

### `class SimulationModels(Section)`

Represents the <format type="bold">Simulation Models</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Target" crefType="Unqualified" />, which contains any models you import and information about the order in which they execute.

#### `def __init__(self, *args)`

Create a new instance.

#### `def apply_parameter_file(self) -> bool`

Gets or sets a value indicating whether to apply the parameter values defined in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFile" /> when you deploy a system definition file.

#### `def apply_parameter_file(self, value: bool)`

Gets or sets a value indicating whether to apply the parameter values defined in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFile" /> when you deploy a system definition file.

#### `def parameter_file_delimiter(self) -> Delimiter`

Gets or sets the delimiter used to separate parameter-value pairs in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFile" />.

#### `def parameter_file_delimiter(self, value: Delimiter)`

Gets or sets the delimiter used to separate parameter-value pairs in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFile" />.

#### `def parameter_access(self) -> ParameterAccess`

Gets or sets the flag used to allow or deny reading and writing non-imported parameters.

#### `def parameter_access(self, value: ParameterAccess)`

Gets or sets the flag used to allow or deny reading and writing non-imported parameters.

#### `def parameter_file_allow_temp_variable(self) -> bool`

Gets or sets a value indicating whether the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFile" /> allows temporary variables. Temporary variables are always local to the file in which you define them.

#### `def parameter_file_allow_temp_variable(self, value: bool)`

Gets or sets a value indicating whether the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFile" /> allows temporary variables. Temporary variables are always local to the file in which you define them.

#### `def parameter_file(self) -> str`

Gets or sets the parameter calibration <format type="monospace">.txt</format> file to apply when you deploy a system definition file.

#### `def parameter_file(self, value: str)`

Gets or sets the parameter calibration <format type="monospace">.txt</format> file to apply when you deploy a system definition file.

#### `def parameter_alias_file(self) -> str`

Gets or sets the parameter alias file to use with the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFile" />.

#### `def parameter_alias_file(self, value: str)`

Gets or sets the parameter alias file to use with the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels.ParameterFile" />.

#### `def remove_parameter_alias_file(self)`

#### `def remove_parameter_alias_file(self, *args)`

#### `def get_models(self) -> Models`

#### `def get_models(self, *args)`

#### `def get_execution_order(self) -> ExecutionOrder`

#### `def get_execution_order(self, *args)`

### `class SinglePoint(Section)`

Represents the <format type="bold">Single-Point</format> section under an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Incoming" crefType="Unqualified" /> section of an NI-XNET CAN, LIN, or FlexRay port. When you import single-point frames, NI VeriStand reads the most recent value received for the frame.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_signal_based_frame_list(self) -> Sequence[SignalBasedFrame]`

#### `def get_signal_based_frame_list(self, *args)`

#### `def get_raw_data_based_frame_list(self) -> Sequence[RawDataBasedFrame]`

#### `def get_raw_data_based_frame_list(self, *args)`

#### `def add_signal_based_frame(self, signal_based_frame: SignalBasedFrame) -> bool`

#### `def add_signal_based_frame(self, *args)`

#### `def add_raw_data_based_frame(self, raw_data_based_frame: RawDataBasedFrame) -> bool`

#### `def add_raw_data_based_frame(self, *args)`

### `class Sporadic(Section)`

Represents the <format type="bold">Sporadic</format> section that contains outgoing, sporadic frames under an NI-XNET LIN port.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_signal_based_frame_list(self) -> Sequence[SignalBasedFrame]`

#### `def get_signal_based_frame_list(self, *args)`

#### `def get_raw_data_based_frame_list(self) -> Sequence[RawDataBasedFrame]`

#### `def get_raw_data_based_frame_list(self, *args)`

#### `def add_signal_based_frame(self, signal_based_frame: SignalBasedFrame) -> bool`

#### `def add_signal_based_frame(self, *args)`

#### `def add_raw_data_based_frame(self, raw_data_based_frame: RawDataBasedFrame) -> bool`

#### `def add_raw_data_based_frame(self, *args)`

### `class Stimulus(Section)`

Represents the <format type="bold">Stimulus</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Target" crefType="Unqualified" />, which contains the stimulus generators available in the Legacy Stimulus Profile Editor.

#### `def __init__(self, *args)`

Create a new instance.

#### `def max_gen_maps(self) -> int`

Gets or sets the maximum number of stimulus generator mappings across the entire system.

#### `def max_gen_maps(self, value: int)`

Gets or sets the maximum number of stimulus generator mappings across the entire system.

#### `def max_steps(self) -> int`

Gets or sets the maximum number of steps a stimulus generator can contain. Set this value to a number that is larger than the number of steps in the longest generator script.

#### `def max_steps(self, value: int)`

Gets or sets the maximum number of steps a stimulus generator can contain. Set this value to a number that is larger than the number of steps in the longest generator script.

#### `def auxilliary_buffer_size(self) -> int`

Gets or sets the size of the auxiliary buffer. The auxiliary buffer stores multi-point playback data in comma-separated value (CSV), files. Set this buffer size to a number that matches or exceeds the number of data points in the CSV file you want to play back. The auxiliary buffer size is shared by all active stimulus generators, so all generators can have up to Auxiliary Buffer Size total in data points for playback.

#### `def auxilliary_buffer_size(self, value: int)`

Gets or sets the size of the auxiliary buffer. The auxiliary buffer stores multi-point playback data in comma-separated value (CSV), files. Set this buffer size to a number that matches or exceeds the number of data points in the CSV file you want to play back. The auxiliary buffer size is shared by all active stimulus generators, so all generators can have up to Auxiliary Buffer Size total in data points for playback.

#### `def analysis_buffer_size(self) -> int`

Gets or sets the size of the analysis buffer. The analysis buffer stores the expected result values for a table test. Set this value to a number that matches or exceeds the number of expected result values in a given table test.

#### `def analysis_buffer_size(self, value: int)`

Gets or sets the size of the analysis buffer. The analysis buffer stores the expected result values for a table test. Set this value to a number that matches or exceeds the number of expected result values in a given table test.

#### `def analysis_result_size(self) -> int`

Gets or sets the size of the analysis failure result buffer. The analysis failure result buffer stores the failure results for a table test. Set this value to a number that meets or exceeds the maximum number of failures you expect to occur in the table test.

#### `def analysis_result_size(self, value: int)`

Gets or sets the size of the analysis failure result buffer. The analysis failure result buffer stores the failure results for a table test. Set this value to a number that meets or exceeds the maximum number of failures you expect to occur in the table test.

#### `def set_generator_count(self, count: int) -> bool`

#### `def set_generator_count(self, *args)`

#### `def get_generator_list(self) -> Sequence[Generator]`

#### `def get_generator_list(self, *args)`

### `class SystemChannels(Section)`

Represents the <format type="bold">System Channels</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Target" crefType="Unqualified" />, which contains a variety of channels that monitor the state and condition of various aspects of the system.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_system_channels(self) -> Sequence[SystemChannel]`

#### `def get_system_channels(self, *args)`

### `class SystemDefinition(_DotNetBase)`

Represents a system definition file, which contains configuration settings for the VeriStand Engine. This class is the base class for configuring system definitions through this API.

#### `def __init__(self, name: str, description: str, creator: str, version: str, target_name: str, target_type: str, filepath: str)`

#### `def __init__(self, nivssdf_file: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def version(self) -> Tuple[int, int, int, int]`

Gets the version number of the system definition file.

#### `def document_type(self) -> DocumentType`

The DocumentType for this SystemDefinition

#### `def root(self) -> Root`

Gets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Root" crefType="Unqualified" /> node of the system definition file.

#### `def save_system_definition_file(self, filepath: str) -> Tuple[bool, str]`

#### `def save_system_definition_file(self) -> Tuple[bool, str]`

#### `def save_system_definition_file(self, *args)`

### `class SystemDefinitionExtensions(_DotNetBase)`

Extension methods to assist with manipulating the SystemDefinition

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_parent(base_node: BaseNode) -> BaseNode`

#### `def get_parent(base_node_type: BaseNodeType) -> BaseNodeType`

#### `def get_parent(*args)`

#### `def is_self_or_ancestor_of(base_node: BaseNode, potential_child: BaseNode) -> bool`

#### `def is_self_or_ancestor_of(base_node_type: BaseNodeType, potential_child: BaseNodeType) -> bool`

#### `def is_self_or_ancestor_of(*args)`

#### `def get_descendant_channels(base_node: BaseNode) -> Iterable[BaseNode]`

#### `def get_descendant_channels(base_nodes: Iterable[BaseNode], inclusion_filter: Callable[[IChannel], bool]) -> Iterable[BaseNode]`

#### `def get_descendant_channels(base_node: BaseNode, inclusion_filter: Callable[[IChannel], bool]) -> Iterable[BaseNode]`

#### `def get_descendant_channels(base_node: BaseNode, inclusion_filter: Callable[[IChannel], bool], recurse_predicate: Callable[[BaseNode], bool]) -> Iterable[BaseNode]`

#### `def get_descendant_channels(base_node_type: BaseNodeType, inclusion_filter: Callable[[BaseNodeType], bool]) -> Iterable[BaseNodeType]`

#### `def get_descendant_channels(base_node_type: BaseNodeType, inclusion_filter: Callable[[BaseNodeType], bool], recurse_predicate: Callable[[BaseNodeType], bool]) -> Iterable[BaseNodeType]`

#### `def get_descendant_channels(*args)`

#### `def is_deprecated(node: BaseNode) -> bool`

#### `def is_deprecated(base_node_type: BaseNodeType) -> bool`

#### `def is_deprecated(*args)`

### `class SystemInitialization(Section)`

Represents the <format type="bold">System Initialization</format> section of the system definition, which contains information about the order that multiple targets deploy relative to each other.

#### `def __init__(self, *args)`

Create a new instance.

#### `def auto_start(self) -> bool`

Gets or sets whether the system runs the system definition file automatically after a target reboots or waits for a user to redeploy the file.

#### `def auto_start(self, value: bool)`

Gets or sets whether the system runs the system definition file automatically after a target reboots or waits for a user to redeploy the file.

### `class SystemMappings(Section)`

Represents the <format type="bold">System Mappings</format> section of the system definition, which stores information about how source channels within the system definition map to destination channels. Destination channels store the mapping information.

#### `def __init__(self, *args)`

Create a new instance.

### `class Target(BaseNode)`

Represents a target in the system definition.

#### `def __init__(self, name: str, target_type: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def username_property_string() -> str`

#### `def password_property_string() -> str`

#### `def timing_source_daq_settings(self) -> TimingSourceSettingsOptions`

Gets or sets the timing source setting for the DAQ device that is timing the Primary Control Loop. This property is only valid if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Target.ControlLoopTimingSource" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource.DAQTiming" crefType="Unqualified" />.

#### `def timing_source_daq_settings(self, value: TimingSourceSettingsOptions)`

Gets or sets the timing source setting for the DAQ device that is timing the Primary Control Loop. This property is only valid if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Target.ControlLoopTimingSource" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource.DAQTiming" crefType="Unqualified" />.

#### `def execution_mode(self) -> TargetExecutionMode`

Gets or sets the execution mode (parallel or low latency) of the loops of the VeriStand Engine.

#### `def execution_mode(self, value: TargetExecutionMode)`

Gets or sets the execution mode (parallel or low latency) of the loops of the VeriStand Engine.

#### `def control_loop_timing_source(self) -> TargetControlLoopTimingSource`

Gets the timing source for the Primary Control Loop.

#### `def daq_timing_device(self) -> DAQDevice`

Gets or sets the DAQ device that serves as the timing source for the Primary Control Loop (PCL). This property is only valid if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Target.ControlLoopTimingSource" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource.DAQTiming" crefType="Unqualified" />.

#### `def custom_timing_device(self) -> CustomDevice`

Gets or sets the custom device that serves as the timing source for the Primary Control Loop (PCL). This property is only valid if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Target.ControlLoopTimingSource" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource.CustomDeviceTiming" crefType="Unqualified" />.

#### `def daq_digital_lines_decimation(self) -> int`

Gets or sets how frequently the Primary Control Loop (PCL) reads and writes DAQ digital line values. The DIO Loop, which receives and sends these values from and to the PCL, executes at a rate of 100Hz. If you set the PCL to execute at a rate faster than 100Hz, use this property to specify a higher decimation value and reduce the frequency with which the PCL reads and writes the digital line values.

#### `def daq_digital_lines_decimation(self, value: int)`

Gets or sets how frequently the Primary Control Loop (PCL) reads and writes DAQ digital line values. The DIO Loop, which receives and sends these values from and to the PCL, executes at a rate of 100Hz. If you set the PCL to execute at a rate faster than 100Hz, use this property to specify a higher decimation value and reduce the frequency with which the PCL reads and writes the digital line values.

#### `def daq_digital_lines_rate(self) -> float`

Gets or sets how frequently the Primary Control Loop (PCL) reads and writes DAQ digital line values.
            The DIO Loop, which receives and sends these values from and to the PCL, executes at this rate and cannot be faster than the PCL loop.

#### `def daq_digital_lines_rate(self, value: float)`

Gets or sets how frequently the Primary Control Loop (PCL) reads and writes DAQ digital line values.
            The DIO Loop, which receives and sends these values from and to the PCL, executes at this rate and cannot be faster than the PCL loop.

#### `def disable_target(self) -> bool`

Gets or sets the Boolean flag indicating whether a target is disabled.

#### `def disable_target(self, value: bool)`

Gets or sets the Boolean flag indicating whether a target is disabled.

#### `def operating_system(self) -> str`

Gets or sets the operating system of the target.

#### `def operating_system(self, value: str)`

Gets or sets the operating system of the target.

#### `def ip_address(self) -> str`

Gets or sets the IP address of the target.

#### `def ip_address(self, value: str)`

Gets or sets the IP address of the target.

#### `def username(self) -> str`

Gets or sets the username for the target.

#### `def username(self, value: str)`

Gets or sets the username for the target.

#### `def password(self) -> str`

Gets or sets the password for the target.

#### `def password(self, value: str)`

Gets or sets the password for the target.

#### `def fpga_scan_interface_mode(self) -> int`

Gets or sets the interface mode for the NI Scan Engine on RT targets. You can use this property to override the current settings of the NI Scan Engine, which can be useful for certain C Series modules, such as NI 986x series devices. <format type="bold">(Windows)</format> This setting has no effect on Windows targets.

#### `def fpga_scan_interface_mode(self, value: int)`

Gets or sets the interface mode for the NI Scan Engine on RT targets. You can use this property to override the current settings of the NI Scan Engine, which can be useful for certain C Series modules, such as NI 986x series devices. <format type="bold">(Windows)</format> This setting has no effect on Windows targets.

#### `def target_timing_mode(self) -> TargetTimingMode`

Gets or sets the timing mode for the target.  When an FPGA serves as the Primary Control Loop timing source, the mode affects certain performance characteristics of the system.

#### `def target_timing_mode(self, value: TargetTimingMode)`

Gets or sets the timing mode for the target.  When an FPGA serves as the Primary Control Loop timing source, the mode affects certain performance characteristics of the system.

#### `def primary_control_loop_processor(self) -> int`

Gets or sets the processor on which to execute the Primary Control Loop (PCL).

#### `def primary_control_loop_processor(self, value: int)`

Gets or sets the processor on which to execute the Primary Control Loop (PCL).

#### `def data_processing_loop_processor(self) -> int`

Gets or sets the processor on which to execute the Data Processing Loop. -2 is any available processor. If you specify an invalid processor, the loop executes on the first available processor.

#### `def data_processing_loop_processor(self, value: int)`

Gets or sets the processor on which to execute the Data Processing Loop. -2 is any available processor. If you specify an invalid processor, the loop executes on the first available processor.

#### `def data_processing_loop_decimation(self) -> int`

Gets or sets the execution rate of the Data Processing Loop (DPL). A value of 1 specifies that the DPL reads values on every iteration of the Primary Control Loop (PCL). You can specify a value higher than 1 to read PCL values less frequently and increase system execution.

#### `def data_processing_loop_decimation(self, value: int)`

Gets or sets the execution rate of the Data Processing Loop (DPL). A value of 1 specifies that the DPL reads values on every iteration of the Primary Control Loop (PCL). You can specify a value higher than 1 to read PCL values less frequently and increase system execution.

#### `def maximum_streamed_channels(self) -> int`

Gets or sets the maximum number of channels that the VeriStand Engine can stream to the host.

#### `def maximum_streamed_channels(self, value: int)`

Gets or sets the maximum number of channels that the VeriStand Engine can stream to the host.

#### `def filter_daq_errors(self) -> bool`

Gets or sets whether to filter errors from NI-DAQmx function calls. Set this property to <see langword="true" /> if you do not want the system to shut down when an NI-DAQ device reports an error.

#### `def filter_daq_errors(self, value: bool)`

Gets or sets whether to filter errors from NI-DAQmx function calls. Set this property to <see langword="true" /> if you do not want the system to shut down when an NI-DAQ device reports an error.

#### `def filter_watchdog_errors(self) -> bool`

Gets or sets whether to filter errors reported by the timing watchdog. For example, if you set the Primary Control Loop to execute at a high rate and your system contains large or complex models, the watchdog reports an error if the models cannot execute quickly enough to keep up with the Primary Control Loop. Set this property to <see langword="true" /> if you want NI VeriStand to ignore these errors.

#### `def filter_watchdog_errors(self, value: bool)`

Gets or sets whether to filter errors reported by the timing watchdog. For example, if you set the Primary Control Loop to execute at a high rate and your system contains large or complex models, the watchdog reports an error if the models cannot execute quickly enough to keep up with the Primary Control Loop. Set this property to <see langword="true" /> if you want NI VeriStand to ignore these errors.

#### `def target_rate(self) -> float`

Gets or sets the execution rate of the target in hertz.

#### `def target_rate(self, value: float)`

Gets or sets the execution rate of the target in hertz.

#### `def timeout(self) -> float`

Gets or sets the amount of time to wait for a start trigger from the DAQ device before timing out. This property is only valid if the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Target.ControlLoopTimingSource" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource.DAQTiming" crefType="Unqualified" />.

#### `def timeout(self, value: float)`

Gets or sets the amount of time to wait for a start trigger from the DAQ device before timing out. This property is only valid if the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Target.ControlLoopTimingSource" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource.DAQTiming" crefType="Unqualified" />.

#### `def daq_timeout(self) -> int`

Gets the amount of time to wait for a DAQ device to transfer data before timing out. This property is only valid of the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Target.ControlLoopTimingSource" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.TargetControlLoopTimingSource.DAQTiming" crefType="Unqualified" />.

#### `def timed_loop_sleep_time(self) -> int`

Gets the amount of time in microseconds the Primary Control Loop (PCL) sleeps after each tick. NI VeriStand ignores this value if the master timing device has an external timing source.

#### `def deployment_group(self) -> int`

Gets or sets the deployment group to which a target belongs.

#### `def deployment_group(self, value: int)`

Gets or sets the deployment group to which a target belongs.

#### `def warmup_time_ms(self) -> int`

Gets or sets the amount of time the system waits before considering late flags. You can set a warm-up time to give the system time to allocate and manage resources.

#### `def warmup_time_ms(self, value: int)`

Gets or sets the amount of time the system waits before considering late flags. You can set a warm-up time to give the system time to allocate and manage resources.

#### `def data_rate(self) -> float`

Gets or sets the rate for updating channel values in the Send Communication Loop.

#### `def data_rate(self, value: float)`

Gets or sets the rate for updating channel values in the Send Communication Loop.

#### `def set_control_loop_timing_source_to_automatic(self) -> bool`

#### `def set_control_loop_timing_source_to_automatic(self, *args)`

#### `def set_control_loop_timing_source_to_daq(self, daq_device_name: str, daq_timeout: int, timed_loop_sleep_time: int) -> bool`

#### `def set_control_loop_timing_source_to_daq(self, *args)`

#### `def set_control_loop_timing_source_to_custom_device(self, custom_device_name: str) -> bool`

#### `def set_control_loop_timing_source_to_custom_device(self, *args)`

#### `def get_system_channels(self) -> SystemChannels`

#### `def get_system_channels(self, *args)`

#### `def get_hardware(self) -> Hardware`

#### `def get_hardware(self, *args)`

#### `def get_stimulus(self) -> Stimulus`

#### `def get_stimulus(self, *args)`

#### `def get_simulation_models(self) -> SimulationModels`

#### `def get_simulation_models(self, *args)`

#### `def get_alarms(self) -> Alarms`

#### `def get_alarms(self, *args)`

#### `def get_procedures(self) -> Procedures`

#### `def get_procedures(self, *args)`

#### `def get_custom_devices(self) -> CustomDevices`

#### `def get_custom_devices(self, *args)`

#### `def get_user_channels(self) -> UserChannels`

#### `def get_user_channels(self, *args)`

#### `def get_calculated_channels(self) -> CalculatedChannels`

#### `def get_calculated_channels(self, *args)`

#### `def get_xnet_databases(self) -> XNETDatabases`

#### `def get_xnet_databases(self, *args)`

### `class TargetControlLoopTimingSource(_DotNetEnum)`

Specifies the timing source for the system. The timing source times the system by sending ticks to the Primary Control Loop.

#### `def __init__(self, *args)`

Create a new instance.

#### `def AUTOMATIC_TIMING() -> TargetControlLoopTimingSource`

#### `def DAQ_TIMING() -> TargetControlLoopTimingSource`

#### `def CUSTOM_DEVICE_TIMING() -> TargetControlLoopTimingSource`

### `class TargetExecutionMode(_DotNetEnum)`

Specifies the execution mode for the loops of the VeriStand Engine.

#### `def __init__(self, *args)`

Create a new instance.

#### `def PARALLEL() -> TargetExecutionMode`

#### `def LOW_LATENCY() -> TargetExecutionMode`

### `class TargetTimingMode(_DotNetEnum)`

The timing mode of the target.

#### `def __init__(self, *args)`

Create a new instance.

#### `def AUTO() -> TargetTimingMode`

#### `def WAIT_ON_INTERRUPT() -> TargetTimingMode`

#### `def WAIT_ON_DMA_READ() -> TargetTimingMode`

### `class Targets(BaseNode)`

Represents the <format type="bold">Targets</format> section of the system definition, which contains all the targets you configure.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_target_list(self) -> Sequence[Target]`

#### `def get_target_list(self, *args)`

#### `def add_target(self, target: Target) -> bool`

#### `def add_target(self, *args)`

### `class TaskType(_DotNetEnum)`

This enumeration is used to select the Task Type.

#### `def __init__(self, *args)`

Create a new instance.

#### `def ANALOG_INPUT() -> TaskType`

### `class TemperatureUnit(_DotNetEnum)`

Defines the Temperature Unit of the thermocouple.

#### `def __init__(self, *args)`

Create a new instance.

#### `def CELSIUS() -> TemperatureUnit`

#### `def FAHRENHEIT() -> TemperatureUnit`

#### `def KELVIN() -> TemperatureUnit`

#### `def RANKINE() -> TemperatureUnit`

### `class ThermocoupleCJCType(_DotNetEnum)`

Defines the CJC type.

#### `def __init__(self, *args)`

Create a new instance.

#### `def IC_SENSOR() -> ThermocoupleCJCType`

#### `def THERMISTOR() -> ThermocoupleCJCType`

#### `def TEMPERATURE() -> ThermocoupleCJCType`

#### `def NI9211() -> ThermocoupleCJCType`

#### `def NI9213() -> ThermocoupleCJCType`

#### `def NI9219() -> ThermocoupleCJCType`

#### `def NI9214() -> ThermocoupleCJCType`

### `class ThermocoupleType(_DotNetEnum)`

Defines the thermocouple type.

#### `def __init__(self, *args)`

Create a new instance.

#### `def B() -> ThermocoupleType`

#### `def E() -> ThermocoupleType`

#### `def J() -> ThermocoupleType`

#### `def K() -> ThermocoupleType`

#### `def R() -> ThermocoupleType`

#### `def S() -> ThermocoupleType`

#### `def T() -> ThermocoupleType`

#### `def N() -> ThermocoupleType`

### `class TimingAndSync(Section)`

Represents the <format type="bold">Timing and Sync</format> section of the system definition, which contains all configured timing and sync devices.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_timing_and_sync_device_list(self) -> Sequence[TimingAndSyncDevice]`

#### `def get_timing_and_sync_device_list(self, *args)`

#### `def add_timing_and_sync_device(self, timing_and_sync_device: TimingAndSyncDevice) -> bool`

#### `def add_timing_and_sync_device(self, *args)`

### `class TimingSourceSettingsOptions(_DotNetEnum)`

Specifies the DAQ timing source setting for the Primary Control Loop when the PCL timing source is set to DAQ.

#### `def __init__(self, *args)`

Create a new instance.

#### `def CONTROL_LOOP_FROM_TASK() -> TimingSourceSettingsOptions`

#### `def SIGNAL_FROM_TASK__SAMPLE_COMPLETE() -> TimingSourceSettingsOptions`

### `class TriggerType(_DotNetEnum)`

Defines the type of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTrigger" />.

#### `def __init__(self, *args)`

Create a new instance.

#### `def NONE() -> TriggerType`

#### `def ANALOG_EDGE() -> TriggerType`

#### `def ANALOG_WINDOW() -> TriggerType`

#### `def DIGITAL_EDGE() -> TriggerType`

#### `def SOFTWARE() -> TriggerType`

### `class Unconditional(Section)`

Represents the <format type="bold">Unconditional</format> section that contains outgoing, unconditional frames under an NI-XNET LIN port.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_signal_based_frame_list(self) -> Sequence[SignalBasedFrame]`

#### `def get_signal_based_frame_list(self, *args)`

#### `def get_raw_data_based_frame_list(self) -> Sequence[RawDataBasedFrame]`

#### `def get_raw_data_based_frame_list(self, *args)`

#### `def add_signal_based_frame(self, signal_based_frame: SignalBasedFrame) -> bool`

#### `def add_signal_based_frame(self, *args)`

#### `def add_raw_data_based_frame(self, raw_data_based_frame: RawDataBasedFrame) -> bool`

#### `def add_raw_data_based_frame(self, *args)`

### `class UserChannels(Section)`

Represents the <format type="bold">User Channels</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Target" crefType="Unqualified" />, which contains any user channels you configure. User channels store a single value, and can be variables in procedures, stimulus profiles, and so on.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_user_channel_list(self) -> Sequence[UserChannel]`

#### `def get_user_channel_list(self, deep: bool) -> Sequence[UserChannel]`

#### `def get_user_channel_list(self, *args)`

#### `def get_user_channel_folder_list(self) -> Sequence[UserChannelsFolder]`

#### `def get_user_channel_folder_list(self, deep: bool) -> Sequence[UserChannelsFolder]`

#### `def get_user_channel_folder_list(self, *args)`

#### `def add_user_channel(self, channel: UserChannel) -> bool`

#### `def add_user_channel(self, *args)`

#### `def add_user_channels_folder(self, folder: UserChannelsFolder) -> bool`

#### `def add_user_channels_folder(self, *args)`

#### `def add_new_user_channel(self, name: str, description: str, units: str, default_value: float) -> UserChannel`

#### `def add_new_user_channel(self, *args)`

#### `def add_new_user_channels_folder(self, name: str, description: str) -> UserChannelsFolder`

#### `def add_new_user_channels_folder(self, *args)`

### `class UserChannelsFolder(Section)`

Represents a folder under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.UserChannels" crefType="Unqualified" /> section of a target. Folders simply organize user channels into logical groups.

#### `def __init__(self, name: str, description: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_user_channel_list(self) -> Sequence[UserChannel]`

#### `def get_user_channel_list(self, deep: bool) -> Sequence[UserChannel]`

#### `def get_user_channel_list(self, *args)`

#### `def get_user_channel_folder_list(self) -> Sequence[UserChannelsFolder]`

#### `def get_user_channel_folder_list(self, deep: bool) -> Sequence[UserChannelsFolder]`

#### `def get_user_channel_folder_list(self, *args)`

#### `def add_user_channel(self, channel: UserChannel) -> bool`

#### `def add_user_channel(self, *args)`

#### `def add_user_channels_folder(self, folder: UserChannelsFolder) -> bool`

#### `def add_user_channels_folder(self, *args)`

#### `def add_new_user_channel(self, name: str, description: str, units: str, default_value: float) -> UserChannel`

#### `def add_new_user_channel(self, *args)`

#### `def add_new_user_channels_folder(self, name: str, description: str) -> UserChannelsFolder`

#### `def add_new_user_channels_folder(self, *args)`

### `class Utilities(_DotNetBase)`

Class that provides a way to perform various common operations within the system definition, such as stripping paths, converting data types, and creating channel mappings.

#### `def __init__(self)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def current_version() -> VersionType`

Gets the current version information for the system definition file.

#### `def serialize_slsc(filepath: str, node: BaseNodeType)`

#### `def serialize_slsc(*args)`

#### `def deserialize_slsc(filepath: str, base_node: BaseNodeType)`

#### `def deserialize_slsc(*args)`

#### `def reset_all_identifiers(base_node_type: BaseNodeType)`

#### `def reset_all_identifiers(*args)`

#### `def date_time_to_double(date_time: System.DateTime) -> float`

#### `def date_time_to_double(*args)`

#### `def double_to_date_time(total_seconds: float) -> System.DateTime`

#### `def double_to_date_time(*args)`

#### `def version_type_to_version(versiontype: VersionType) -> Tuple[int, int, int, int]`

#### `def version_type_to_version(*args)`

#### `def get_localized_name_by_guid(guid: str) -> str`

#### `def get_localized_name_by_guid(*args)`

#### `def resolve_path_type(root_path: str, file_path: str) -> DependentFileType`

#### `def resolve_path_type(*args)`

#### `def strip_path(path: str) -> Tuple[str, str]`

#### `def strip_path(*args)`

#### `def get_filename(path: str) -> str`

#### `def get_filename(*args)`

#### `def build_path(path: str, relative: str) -> str`

#### `def build_path(*args)`

#### `def rt_main_path() -> str`

#### `def rt_main_path(*args)`

#### `def data_replay_rt_path() -> str`

#### `def data_replay_rt_path(*args)`

#### `def relative_afp_ini_path() -> str`

#### `def relative_afp_ini_path(*args)`

#### `def afp_rt_path() -> str`

#### `def afp_rt_path(*args)`

#### `def path_type_pair_to_absolute_path(path: str, type: PathType) -> str`

#### `def path_type_pair_to_absolute_path(path: str, type: DependentFilePropertyType, base_path: str) -> str`

#### `def path_type_pair_to_absolute_path(*args)`

#### `def strip_path_if_in_llb(file_path: str) -> str`

#### `def strip_path_if_in_llb(*args)`

#### `def add_mapping(source: Channel, destination: Channel)`

#### `def add_mapping(*args)`

#### `def clear_mapping(destination: Channel)`

#### `def clear_mapping(*args)`

#### `def auto_map_channels(source_node: BaseNode, destination_node: BaseNode) -> Iterable[System.Collections.Generic.KeyValuePair[NationalInstruments.VeriStand.SystemDefinitionAPI.IChannel, NationalInstruments.VeriStand.SystemDefinitionAPI.IChannel]]`

#### `def auto_map_channels(source_node: BaseNode, destination_node: BaseNode, comparer: System.IEqualityComparer) -> Iterable[System.Collections.Generic.KeyValuePair[NationalInstruments.VeriStand.SystemDefinitionAPI.IChannel, NationalInstruments.VeriStand.SystemDefinitionAPI.IChannel]]`

#### `def auto_map_channels(source_node: BaseNode, destination_node: BaseNode, comparer: System.IEqualityComparer, inclusion_filter: Callable[[IChannel], bool]) -> Iterable[System.Collections.Generic.KeyValuePair[NationalInstruments.VeriStand.SystemDefinitionAPI.IChannel, NationalInstruments.VeriStand.SystemDefinitionAPI.IChannel]]`

#### `def auto_map_channels(source_node: BaseNode, destination_node: BaseNode, comparer: System.IEqualityComparer, inclusion_filter: Callable[[IChannel], bool], recurse_predicate: Callable[[BaseNode], bool]) -> Iterable[System.Collections.Generic.KeyValuePair[NationalInstruments.VeriStand.SystemDefinitionAPI.IChannel, NationalInstruments.VeriStand.SystemDefinitionAPI.IChannel]]`

#### `def auto_map_channels(*args)`

#### `def default_auto_map_recursion_filter(node: BaseNode) -> bool`

#### `def default_auto_map_recursion_filter(*args)`

#### `def find_name_matches(source_channels: Iterable[IChannel], destination_channels: Iterable[IChannel], comparer: System.IEqualityComparer) -> Iterable[System.Collections.Generic.KeyValuePair[NationalInstruments.VeriStand.SystemDefinitionAPI.IChannel, NationalInstruments.VeriStand.SystemDefinitionAPI.IChannel]]`

#### `def find_name_matches(*args)`

#### `def create_base_node_from_system_storage_node(storage_node: BaseNodeType) -> BaseNode`

#### `def create_base_node_from_system_storage_node(*args)`

### `class ValueSource(_DotNetBase)`

Represents the source of a channel value as a constant or a channel.

#### `def __init__(self, constant: float)`

#### `def __init__(self, channel: BaseNode)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def is_constant(self) -> bool`

#### `def channel(self) -> BaseNode`

#### `def constant(self) -> float`

### `class VirtualECUToolchain(_DotNetEnum)`

Toolchain that was used to build virtual ECUs.

#### `def __init__(self, *args)`

Create a new instance.

#### `def SILVER() -> VirtualECUToolchain`

### `class Waveform(BaseNode)`

Represents a waveform in the system definition. This is a base class for more specific waveform classes, including hardware waveforms, custom device waveforms, and so on.

#### `def __init__(self, *args)`

Create a new instance.

#### `def units(self) -> str`

Gets or sets the units associated with the waveform. This can be any arbitrary string.

#### `def units(self, value: str)`

Gets or sets the units associated with the waveform. This can be any arbitrary string.

#### `def data_type(self) -> WaveformTypeDataType`

Gets or sets the data type associated with the waveform.

#### `def data_type(self, value: WaveformTypeDataType)`

Gets or sets the data type associated with the waveform.

### `class WindowConditionType(_DotNetEnum)`

Defines the signal condition that causes a window trigger.

#### `def __init__(self, *args)`

Create a new instance.

#### `def ENTERING_WINDOW() -> WindowConditionType`

#### `def LEAVING_WINDOW() -> WindowConditionType`

### `class XNET(Section)`

Represents the <format type="bold">NI-XNET</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Chassis" crefType="Unqualified" />, which contains any <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CAN" crefType="Unqualified" />, <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.LIN" crefType="Unqualified" />, or <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRay" crefType="Unqualified" /> devices you configure.

#### `def __init__(self, *args)`

Create a new instance.

#### `def decimation(self) -> int`

Gets or sets the processing rate for inline incoming and outgoing frames of an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNET" crefType="Unqualified" /> device, which NI VeriStand uses to calculate the decimation factor (decimation factor = Primary Control Loop rate/processing rate). This value determines how many iterations of the Primary Control Loop occur between calls to the device.

#### `def decimation(self, value: int)`

Gets or sets the processing rate for inline incoming and outgoing frames of an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNET" crefType="Unqualified" /> device, which NI VeriStand uses to calculate the decimation factor (decimation factor = Primary Control Loop rate/processing rate). This value determines how many iterations of the Primary Control Loop occur between calls to the device.

#### `def enable_xnet(self)`

#### `def enable_xnet(self, *args)`

#### `def disable_xnet(self)`

#### `def disable_xnet(self, *args)`

#### `def get_can(self) -> CAN`

#### `def get_can(self, *args)`

#### `def get_flex_ray(self) -> FlexRay`

#### `def get_flex_ray(self, *args)`

#### `def get_lin(self) -> LIN`

#### `def get_lin(self, *args)`

### `class XNETDatabases(Section)`

Represents the <format type="bold">XNET Databases</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Target" crefType="Unqualified" />, which contains any XNET Databases you add to the system definition to run <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNET" crefType="Unqualified" /> devices.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_database_list(self) -> Sequence[Database]`

#### `def get_database_list(self, *args)`

#### `def add_database(self, database: Database) -> bool`

#### `def add_database(self, *args)`

### `class XNETTermination(_DotNetEnum)`

Configures onboard termination for the XNET port. Termination behavior differs depending on the type of device you are using (CAN, FlexRay, or LIN).

#### `def __init__(self, *args)`

Create a new instance.

#### `def OFF() -> XNETTermination`

#### `def ON() -> XNETTermination`

### `class Alarm(Section)`

Represents an alarm, which notifies the user that the value of a particular channel has gone outside a specified range of values. Alarms also can trigger the execution of a specified procedure.

#### `def __init__(self, name: str, description: str, alarm_source: Channel, upper_limit: ValueSource, lower_limit: ValueSource, alarm_action: Procedure, mode: AlarmMode, default_state: AlarmState, group_number: int, priority_number: int, delay: float, trip_message: str)`

#### `def __init__(self, name: str, description: str, alarm_source: Channel, upper_limit: ValueSource, lower_limit: ValueSource, alarm_action: Procedure, mode: AlarmMode, default_state: AlarmState, group_number: int, priority_number: int, delay: float, trip_message: str, auto_reset_alarm: bool, require_alarm_acknowledgement: bool)`

#### `def __init__(self, name: str, description: str, alarm_source: Channel, upper_limit: float, lower_limit: float, alarm_action: Procedure, mode: AlarmMode, default_state: AlarmState, priority: AlarmPriority, delay: float, trip_message: str)`

#### `def __init__(self, name: str, description: str, alarm_source: Channel, upper_limit: float, lower_limit: BaseNode, alarm_action: Procedure, mode: AlarmMode, default_state: AlarmState, priority: AlarmPriority, delay: float, trip_message: str)`

#### `def __init__(self, name: str, description: str, alarm_source: Channel, upper_limit: BaseNode, lower_limit: float, alarm_action: Procedure, mode: AlarmMode, default_state: AlarmState, priority: AlarmPriority, delay: float, trip_message: str)`

#### `def __init__(self, name: str, description: str, alarm_source: Channel, upper_limit: BaseNode, lower_limit: BaseNode, alarm_action: Procedure, mode: AlarmMode, default_state: AlarmState, priority: AlarmPriority, delay: float, trip_message: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def mode(self) -> AlarmMode`

Gets or sets the mode of the alarm (<format type="monospace">Normal</format> or <format type="monospace">IndicateOnly</format>).

#### `def mode(self, value: AlarmMode)`

Gets or sets the mode of the alarm (<format type="monospace">Normal</format> or <format type="monospace">IndicateOnly</format>).

#### `def priority_number(self) -> int`

Gets or sets the priority of an alarm running on the target. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31.

#### `def priority_number(self, value: int)`

Gets or sets the priority of an alarm running on the target. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31.

#### `def group_number(self) -> int`

Gets or sets the number of the group to which an alarm belongs.

#### `def group_number(self, value: int)`

Gets or sets the number of the group to which an alarm belongs.

#### `def priority(self) -> AlarmPriority`

This property is deprecated in NI VeriStand 2011 and later. Use the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> property instead.
            <para>
            Setting this property to <format type="monospace">Low</format>, <format type="monospace">Medium</format>, or <format type="monospace">High</format> automatically sets the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> to 25, 15, or 5, respectively.</para>

#### `def priority(self, value: AlarmPriority)`

This property is deprecated in NI VeriStand 2011 and later. Use the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> property instead.
            <para>
            Setting this property to <format type="monospace">Low</format>, <format type="monospace">Medium</format>, or <format type="monospace">High</format> automatically sets the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> to 25, 15, or 5, respectively.</para>

#### `def default_state(self) -> AlarmState`

Gets or sets the default state (<format type="monospace">Disabled</format> or <format type="monospace">Enabled</format>) of the alarm.

#### `def default_state(self, value: AlarmState)`

Gets or sets the default state (<format type="monospace">Disabled</format> or <format type="monospace">Enabled</format>) of the alarm.

#### `def auto_reset_alarm(self) -> bool`

Gets or sets the reset behavior of the alarm. This property defines whether the alarm automatically resets when the channel is back in range, as opposed to being reset by a procedure.

#### `def auto_reset_alarm(self, value: bool)`

Gets or sets the reset behavior of the alarm. This property defines whether the alarm automatically resets when the channel is back in range, as opposed to being reset by a procedure.

#### `def require_alarm_acknowledgement(self) -> bool`

Gets or sets the acknowledgement behavior of the alarm. This property defines whether the alarm must be manually acknowledged before it can reset. Otherwise, alarm is automatically acknowledged when the channel is back in range.

#### `def require_alarm_acknowledgement(self, value: bool)`

Gets or sets the acknowledgement behavior of the alarm. This property defines whether the alarm must be manually acknowledged before it can reset. Otherwise, alarm is automatically acknowledged when the channel is back in range.

#### `def delay(self) -> float`

Gets or sets the amount of time to wait before triggering the alarm.

#### `def delay(self, value: float)`

Gets or sets the amount of time to wait before triggering the alarm.

#### `def alarm_source(self) -> BaseNode`

Gets or sets the channel to monitor for alarm conditions.

#### `def alarm_source(self, value: BaseNode)`

Gets or sets the channel to monitor for alarm conditions.

#### `def upper_limit_is_constant(self) -> int`

Gets whether the upper limit value of the alarm is specified by a constant or a channel.

#### `def upper_limit_constant(self) -> float`

Gets the constant that determines the upper limit value of the alarm. If the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.AlarmSource" crefType="Unqualified" /> exceeds this limit, the alarm is triggered.

#### `def lower_limit_is_constant(self) -> int`

Gets whether the lower limit value of the alarm is specified by a constant or a channel.

#### `def lower_limit_constant(self) -> float`

Gets the constant value that determines the lower limit value of the alarm. If the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.AlarmSource" crefType="Unqualified" /> falls below this limit, the alarm is triggered.

#### `def upper_limit_channel(self) -> BaseNode`

Gets the channel that determines the upper limit value of the alarm. If the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.AlarmSource" crefType="Unqualified" /> exceeds this limit, the alarm is triggered.

#### `def lower_limit_channel(self) -> BaseNode`

Gets the channel that determines the lower limit value of the alarm. If the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.AlarmSource" crefType="Unqualified" /> falls below this limit, the alarm is triggered.

#### `def alarm_action(self) -> BaseNode`

Gets or sets the procedure to initiate when the alarm conditions are met.

#### `def alarm_action(self, value: BaseNode)`

Gets or sets the procedure to initiate when the alarm conditions are met.

#### `def trip_message(self) -> str`

Gets or sets the message to display when the alarm is tripped.

#### `def trip_message(self, value: str)`

Gets or sets the message to display when the alarm is tripped.

#### `def set_upper_limit(self, upper_limit: float)`

#### `def set_upper_limit(self, upper_limit: BaseNode)`

#### `def set_upper_limit(self, limit: ValueSource)`

#### `def set_upper_limit(self, *args)`

#### `def set_lower_limit(self, lower_limit: float)`

#### `def set_lower_limit(self, lower_limit: BaseNode)`

#### `def set_lower_limit(self, limit: ValueSource)`

#### `def set_lower_limit(self, *args)`

#### `def add_alarm_status_channel(self) -> bool`

#### `def add_alarm_status_channel(self, *args)`

#### `def get_alarm_status_channel(self) -> AlarmStatus`

#### `def get_alarm_status_channel(self, *args)`

### `class AlarmFolder(Section)`

Represents an alarm folder, which organizes alarms under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarms" crefType="Unqualified" /> section.

#### `def __init__(self, name: str, description: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_alarm_list(self) -> Sequence[Alarm]`

#### `def get_alarm_list(self, deep: bool) -> Sequence[Alarm]`

#### `def get_alarm_list(self, *args)`

#### `def get_alarm_folder_list(self) -> Sequence[AlarmFolder]`

#### `def get_alarm_folder_list(self, deep: bool) -> Sequence[AlarmFolder]`

#### `def get_alarm_folder_list(self, *args)`

#### `def add_alarm(self, alarm: Alarm) -> bool`

#### `def add_alarm(self, *args)`

#### `def add_alarm_folder(self, folder: AlarmFolder) -> bool`

#### `def add_alarm_folder(self, *args)`

#### `def add_new_alarm(self, name: str, description: str, alarm_source: Channel, upper_limit: ValueSource, lower_limit: ValueSource, alarm_action: Procedure, mode: AlarmMode, default_state: AlarmState, group_number: int, priority_number: int, delay: float, trip_message: str) -> Alarm`

#### `def add_new_alarm(self, *args)`

#### `def add_new_alarm_folder(self, name: str, description: str) -> AlarmFolder`

#### `def add_new_alarm_folder(self, *args)`

### `class Alarms(Section)`

Represents the <format type="bold">Alarms</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Target" crefType="Unqualified" />, which contains any configured <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm" crefType="Unqualified" /> and <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmFolder" crefType="Unqualified" /> objects.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_alarm_list(self) -> Sequence[Alarm]`

#### `def get_alarm_list(self, deep: bool) -> Sequence[Alarm]`

#### `def get_alarm_list(self, *args)`

#### `def get_alarm_folder_list(self) -> Sequence[AlarmFolder]`

#### `def get_alarm_folder_list(self, deep: bool) -> Sequence[AlarmFolder]`

#### `def get_alarm_folder_list(self, *args)`

#### `def add_alarm(self, alarm: Alarm) -> bool`

#### `def add_alarm(self, *args)`

#### `def add_alarm_folder(self, folder: AlarmFolder) -> bool`

#### `def add_alarm_folder(self, *args)`

#### `def add_new_alarm(self, name: str, description: str, alarm_source: Channel, upper_limit: float, lower_limit: float, alarm_action: Procedure, mode: AlarmMode, default_state: AlarmState, priority: AlarmPriority, delay: float, trip_message: str) -> Alarm`

#### `def add_new_alarm(self, name: str, description: str, alarm_source: Channel, upper_limit: float, lower_limit: BaseNode, alarm_action: Procedure, mode: AlarmMode, default_state: AlarmState, priority: AlarmPriority, delay: float, trip_message: str) -> Alarm`

#### `def add_new_alarm(self, name: str, description: str, alarm_source: Channel, upper_limit: BaseNode, lower_limit: float, alarm_action: Procedure, mode: AlarmMode, default_state: AlarmState, priority: AlarmPriority, delay: float, trip_message: str) -> Alarm`

#### `def add_new_alarm(self, name: str, description: str, alarm_source: Channel, upper_limit: BaseNode, lower_limit: BaseNode, alarm_action: Procedure, mode: AlarmMode, default_state: AlarmState, priority: AlarmPriority, delay: float, trip_message: str) -> Alarm`

#### `def add_new_alarm(self, name: str, description: str, alarm_source: Channel, upper_limit: ValueSource, lower_limit: ValueSource, alarm_action: Procedure, mode: AlarmMode, default_state: AlarmState, group_number: int, priority_number: int, delay: float, trip_message: str) -> Alarm`

#### `def add_new_alarm(self, *args)`

#### `def add_new_alarm_folder(self, name: str, description: str) -> AlarmFolder`

#### `def add_new_alarm_folder(self, *args)`

### `class Alias(BaseNode, IChannel)`

Represents an alias, which defines an alternate name for a channel in a system definition file. You can use the alias name, rather than the full channel path, in the <format type="bold">Workspace</format> window and Stimulus Profile Editor.

#### `def __init__(self, name: str, description: str, linked_channel_path: str)`

#### `def __init__(self, name: str, description: str, linked_channel_reference: Channel)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def linked_channel(self) -> BaseNode`

Gets or sets the channel that the alias represents.

#### `def linked_channel(self, value: BaseNode)`

Gets or sets the channel that the alias represents.

### `class AliasFolder(Section)`

Represents a folder under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Aliases" crefType="Unqualified" /> section of the system definition. Folders simply organize aliases into logical groups.

#### `def __init__(self, name: str, description: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_aliases_list(self) -> Sequence[Alias]`

#### `def get_aliases_list(self, deep: bool) -> Sequence[Alias]`

#### `def get_aliases_list(self, *args)`

#### `def get_alias_folder_list(self) -> Sequence[AliasFolder]`

#### `def get_alias_folder_list(self, deep: bool) -> Sequence[AliasFolder]`

#### `def get_alias_folder_list(self, *args)`

#### `def add_alias(self, alias: Alias) -> bool`

#### `def add_alias(self, *args)`

#### `def add_alias_folder(self, folder: AliasFolder) -> bool`

#### `def add_alias_folder(self, *args)`

#### `def add_new_alias_by_path(self, name: str, description: str, linked_channel_path: str) -> Alias`

#### `def add_new_alias_by_path(self, *args)`

#### `def add_new_alias_by_reference(self, name: str, description: str, linked_channel_reference: Channel) -> Alias`

#### `def add_new_alias_by_reference(self, *args)`

#### `def add_new_alias_folder(self, name: str, description: str) -> AliasFolder`

#### `def add_new_alias_folder(self, *args)`

### `class Aliases(Section)`

Represents the <format type="bold">Aliases</format> section of the system definition, which contains <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Alias" crefType="Unqualified" /> objects that define names you can use in place of full channel paths.

#### `def __init__(self, *args)`

Create a new instance.

#### `def delete_unmapped_aliases(self)`

#### `def delete_unmapped_aliases(self, *args)`

#### `def import_aliases_from_file(self, file_path: str, inclusion_filter: Callable[[str], bool])`

#### `def import_aliases_from_file(self, *args)`

#### `def export_aliases_to_file(self, file_path: str, inclusion_filter: Callable[[IChannel], bool], recurse_predicate: Callable[[BaseNode], bool])`

#### `def export_aliases_to_file(self, *args)`

#### `def get_aliases_list(self) -> Sequence[Alias]`

#### `def get_aliases_list(self, deep: bool) -> Sequence[Alias]`

#### `def get_aliases_list(self, *args)`

#### `def get_alias_folder_list(self) -> Sequence[AliasFolder]`

#### `def get_alias_folder_list(self, deep: bool) -> Sequence[AliasFolder]`

#### `def get_alias_folder_list(self, *args)`

#### `def add_alias(self, alias: Alias) -> bool`

#### `def add_alias(self, *args)`

#### `def add_alias_folder(self, folder: AliasFolder) -> bool`

#### `def add_alias_folder(self, *args)`

#### `def add_new_alias_by_path(self, name: str, description: str, linked_channel_path: str) -> Alias`

#### `def add_new_alias_by_path(self, *args)`

#### `def add_new_alias_by_reference(self, name: str, description: str, linked_channel_reference: Channel) -> Alias`

#### `def add_new_alias_by_reference(self, *args)`

#### `def add_new_alias_folder(self, name: str, description: str) -> AliasFolder`

#### `def add_new_alias_folder(self, *args)`

### `class AutomaticFrameProcessing(Section)`

Represents an <format type="bold">Automatic Frame Processing</format> section under an outgoing frame of an NI-XNET CAN port. The <format type="bold">Automatic Frame Processing</format> section contains <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CRC" crefType="Unqualified" /> and <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Counter" crefType="Unqualified" /> channels.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_crc(self) -> CRC`

#### `def get_crc(self, *args)`

#### `def get_counter(self) -> Counter`

#### `def get_counter(self, *args)`

### `class CAN(Section)`

Represents the <format type="bold">CAN</format> section under <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNET" crefType="Unqualified" /> in the system definition.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_can_port_list(self) -> Sequence[CANPort]`

#### `def get_can_port_list(self, *args)`

#### `def add_can_port(self, can_port: CANPort) -> bool`

#### `def add_can_port(self, *args)`

### `class CANInterfaceChannels(Section)`

Represents the <format type="bold">Interface</format> section under an NI-XNET CAN port. This section contains the port-specific channel that controls the port's sleep mode and channels which provide status information.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_communication_state_channel(self) -> Channel`

#### `def get_communication_state_channel(self, *args)`

#### `def get_fault_channel(self) -> Channel`

#### `def get_fault_channel(self, *args)`

#### `def get_last_error_channel(self) -> Channel`

#### `def get_last_error_channel(self, *args)`

#### `def get_last_error_timestamp_channel(self) -> Channel`

#### `def get_last_error_timestamp_channel(self, *args)`

#### `def get_receive_error_counter_channel(self) -> Channel`

#### `def get_receive_error_counter_channel(self, *args)`

#### `def get_sleep_mode_channel(self) -> SleepMode`

#### `def get_sleep_mode_channel(self, *args)`

#### `def get_transceiver_error_channel(self) -> Channel`

#### `def get_transceiver_error_channel(self, *args)`

#### `def get_transmit_error_counter_channel(self) -> Channel`

#### `def get_transmit_error_counter_channel(self, *args)`

#### `def add_sleep_mode_channel(self, sleep_mode: SleepMode) -> bool`

#### `def add_sleep_mode_channel(self, *args)`

#### `def create_communication_state_channel(self) -> Channel`

#### `def create_communication_state_channel(self, *args)`

#### `def create_fault_channel(self) -> Channel`

#### `def create_fault_channel(self, *args)`

#### `def create_last_error_channel(self) -> Channel`

#### `def create_last_error_channel(self, *args)`

#### `def create_last_error_timestamp_channel(self) -> Channel`

#### `def create_last_error_timestamp_channel(self, *args)`

#### `def create_receive_error_counter_channel(self) -> Channel`

#### `def create_receive_error_counter_channel(self, *args)`

#### `def create_transceiver_error_channel(self) -> Channel`

#### `def create_transceiver_error_channel(self, *args)`

#### `def create_transmit_error_counter_channel(self) -> Channel`

#### `def create_transmit_error_counter_channel(self, *args)`

### `class CANPort(Section)`

Represents a port under the NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CAN" crefType="Unqualified" /> section.

#### `def __init__(self, name: str, port_number: int, linked_database: Database, cluster_name: str, baud_rate: int)`

#### `def __init__(self, name: str, port_number: int, linked_database: Database, cluster_name: str, baud_rate: int, fd_baud_rate: int)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def port_number(self) -> int`

Gets or sets the physical address of the CAN port.

#### `def port_number(self, value: int)`

Gets or sets the physical address of the CAN port.

#### `def linked_database(self) -> BaseNode`

Gets or sets the XNET database associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort" crefType="Unqualified" />.

#### `def linked_database(self, value: BaseNode)`

Gets or sets the XNET database associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort" crefType="Unqualified" />.

#### `def baud_rate_bitfield(self) -> int`

Gets or sets the baud rate bitfield of the CAN port.

#### `def baud_rate_bitfield(self, value: int)`

Gets or sets the baud rate bitfield of the CAN port.

#### `def baud_rate(self) -> int`

Gets or sets the baud rate of the CAN port.

#### `def baud_rate(self, value: int)`

Gets or sets the baud rate of the CAN port.

#### `def fd_baud_rate_bitfield(self) -> int`

Gets or sets the FD baud rate bitfield of the CAN port.

#### `def fd_baud_rate_bitfield(self, value: int)`

Gets or sets the FD baud rate bitfield of the CAN port.

#### `def fd_baud_rate(self) -> int`

Gets or sets the FD baud rate of the CAN port.

#### `def fd_baud_rate(self, value: int)`

Gets or sets the FD baud rate of the CAN port.

#### `def fdiso_mode(self) -> FDISOMode`

Gets or sets the FD ISO mode of the CAN port.

#### `def fdiso_mode(self, value: FDISOMode)`

Gets or sets the FD ISO mode of the CAN port.

#### `def cluster_name(self) -> str`

Gets or sets the name of the cluster in <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort.LinkedDatabase" crefType="Unqualified" /> that is associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort" crefType="Unqualified" />.

#### `def cluster_name(self, value: str)`

Gets or sets the name of the cluster in <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort.LinkedDatabase" crefType="Unqualified" /> that is associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort" crefType="Unqualified" />.

#### `def incoming_rate(self) -> int`

Gets or sets the processing rate for incoming frames in hertz.

#### `def incoming_rate(self, value: int)`

Gets or sets the processing rate for incoming frames in hertz.

#### `def outgoing_rate(self) -> int`

Gets or sets the processing rate for outgoing frames in hertz.

#### `def outgoing_rate(self, value: int)`

Gets or sets the processing rate for outgoing frames in hertz.

#### `def echo(self) -> bool`

Gets or sets whether sessions contain frames that the interface transmits. If <see langword="true" />, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session.

#### `def echo(self, value: bool)`

Gets or sets whether sessions contain frames that the interface transmits. If <see langword="true" />, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session.

#### `def input_stream_queue_size(self) -> int`

Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored.

#### `def input_stream_queue_size(self, value: int)`

Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored.

#### `def can_bus_off(self) -> bool`

Gets or sets whether the CAN bus is recovered if it switches off due to a physical fault on the bus.

#### `def can_bus_off(self, value: bool)`

Gets or sets whether the CAN bus is recovered if it switches off due to a physical fault on the bus.

#### `def can_bus_off_rate(self) -> int`

Gets or sets the bit rate at which to check the state of the CAN bus (active or off).

#### `def can_bus_off_rate(self, value: int)`

Gets or sets the bit rate at which to check the state of the CAN bus (active or off).

#### `def afpini_file(self) -> str`

Gets the name of the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort.AFPBinaryFile" crefType="Unqualified" /> used for automatic frame processing.

#### `def afp_binary_file(self) -> DependentFile`

Gets the binary (<format type="monospace">.ini</format>) file used for automatic frame processing.

#### `def afp_global_data(self) -> Sequence[int]`

Gets the global data used for automatic frame processing.

#### `def inline_incoming(self) -> bool`

Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL.

#### `def inline_incoming(self, value: bool)`

Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL.

#### `def inline_outgoing(self) -> bool`

Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL.

#### `def inline_outgoing(self, value: bool)`

Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL.

#### `def disabled(self) -> bool`

Gets or sets whether the port is disabled.

#### `def disabled(self, value: bool)`

Gets or sets whether the port is disabled.

#### `def termination(self) -> XNETTermination`

Gets or sets the onboard <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination" crefType="Unqualified" />.

#### `def termination(self, value: XNETTermination)`

Gets or sets the onboard <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination" crefType="Unqualified" />.

#### `def transceiver_type(self) -> CANTransceiverType`

Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransceiverType" crefType="Unqualified" /> for the port. Transceivers can be high-speed (<format type="monospace">HS</format>), low-speed (<format type="monospace">LS</format>), or single wire (<format type="monospace">SW</format>).

#### `def transceiver_type(self, value: CANTransceiverType)`

Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransceiverType" crefType="Unqualified" /> for the port. Transceivers can be high-speed (<format type="monospace">HS</format>), low-speed (<format type="monospace">LS</format>), or single wire (<format type="monospace">SW</format>).

#### `def transmit_order_type(self) -> CANTransmitOrderType`

Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransmitOrderType" crefType="Unqualified" /> for the port. You can transmit frames to the CAN bus <format type="monospace">AsSubmitted</format> or <format type="monospace">ByIdentifier</format>.

#### `def transmit_order_type(self, value: CANTransmitOrderType)`

Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANTransmitOrderType" crefType="Unqualified" /> for the port. You can transmit frames to the CAN bus <format type="monospace">AsSubmitted</format> or <format type="monospace">ByIdentifier</format>.

#### `def input_stream_read_time(self) -> float`

Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read.  After this amount of time has elapsed, any frames available from the hardware will be read.

#### `def input_stream_read_time(self, value: float)`

Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read.  After this amount of time has elapsed, any frames available from the hardware will be read.

#### `def get_incoming(self) -> Incoming`

#### `def get_incoming(self, *args)`

#### `def get_outgoing(self) -> Outgoing`

#### `def get_outgoing(self, *args)`

#### `def get_interface_section(self) -> CANInterfaceChannels`

#### `def get_interface_section(self, *args)`

#### `def create_interface_section(self) -> CANInterfaceChannels`

#### `def create_interface_section(self, *args)`

#### `def remove_automatic_frame_processing(self)`

#### `def remove_automatic_frame_processing(self, *args)`

#### `def remove986x_support(self)`

#### `def remove986x_support(self, *args)`

#### `def set986x_support(self, file: DependentFile, rio_port_number: int)`

#### `def set986x_support(self, *args)`

#### `def set_automatic_frame_processing(self, ini_file_name: str, binary_file_path: str, global_data: Sequence[int])`

#### `def set_automatic_frame_processing(self, *args)`

### `class CRC(Section)`

Represents the <format type="bold">CRC</format> section under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.AutomaticFrameProcessing" crefType="Unqualified" /> section of an outgoing frame of an NI-XNET CAN port. This feature performs a cyclic redundancy check.

#### `def __init__(self, *args)`

Create a new instance.

#### `def max_afp_length(self) -> int`

Gets or sets the maximum AFP (automatic frame processing) length, which corresponds to the order of the generator polynomial for CRC.

#### `def max_afp_length(self, value: int)`

Gets or sets the maximum AFP (automatic frame processing) length, which corresponds to the order of the generator polynomial for CRC.

#### `def index_crc(self) -> int`

Gets or sets the index of the CRC within the frame.

#### `def index_crc(self, value: int)`

Gets or sets the index of the CRC within the frame.

#### `def afp_data(self) -> Sequence[int]`

Gets or sets an array of data used to configure the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CRC" crefType="Unqualified" /> feature of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.AutomaticFrameProcessing" crefType="Unqualified" />.

#### `def afp_data(self, value: Sequence[int])`

Gets or sets an array of data used to configure the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CRC" crefType="Unqualified" /> feature of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.AutomaticFrameProcessing" crefType="Unqualified" />.

#### `def use_alternate_channel(self) -> bool`

Gets whether the <format type="italics">AlternateChannel</format> specified by <see cref="M:NationalInstruments.VeriStand.SystemDefinitionAPI.CRC.SetAlternateChannel(NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNode)" crefType="Unqualified" /> is used to trigger writing data.

#### `def alternate_channel(self) -> BaseNode`

Gets the channel used to trigger writing data when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.CRC.UseAlternateChannel" crefType="Unqualified" /> is <see langword="true" />.

#### `def remove_alternate_channel(self)`

#### `def remove_alternate_channel(self, *args)`

#### `def set_alternate_channel(self, alternate_channel: BaseNode)`

#### `def set_alternate_channel(self, *args)`

### `class CalculatedChannelFolder(Section)`

Represents a folder under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannels" crefType="Unqualified" /> section of the system definition. Folders simply organize CalculatedChannels into logical groups.

#### `def __init__(self, name: str, description: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_calculated_channels_list(self) -> Sequence[CalculatedChannel]`

#### `def get_calculated_channels_list(self, deep: bool) -> Sequence[CalculatedChannel]`

#### `def get_calculated_channels_list(self, *args)`

#### `def get_calculated_channel_folder_list(self) -> Sequence[CalculatedChannelFolder]`

#### `def get_calculated_channel_folder_list(self, deep: bool) -> Sequence[CalculatedChannelFolder]`

#### `def get_calculated_channel_folder_list(self, *args)`

#### `def add_calculated_channel(self, calculated_channel: CalculatedChannel) -> bool`

#### `def add_calculated_channel(self, *args)`

#### `def add_calculated_channel_folder(self, folder: CalculatedChannelFolder) -> bool`

#### `def add_calculated_channel_folder(self, *args)`

### `class CalculatedChannels(Section)`

Represents the <format type="bold">Calculated Channels</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Target" crefType="Unqualified" />. This section contains <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannel" crefType="Unqualified" /> objects that perform calculations on other channels in the system.

#### `def __init__(self, *args)`

Create a new instance.

#### `def reorder_channel_list(self, channels: Sequence[CalculatedChannel]) -> bool`

#### `def reorder_channel_list(self, *args)`

#### `def get_ordered_channel_list(self) -> Sequence[CalculatedChannel]`

#### `def get_ordered_channel_list(self, *args)`

#### `def get_calculated_channel_folder_list(self) -> Sequence[CalculatedChannelFolder]`

#### `def get_calculated_channel_folder_list(self, deep: bool) -> Sequence[CalculatedChannelFolder]`

#### `def get_calculated_channel_folder_list(self, *args)`

#### `def add_calculated_channel_folder(self, folder: CalculatedChannelFolder) -> bool`

#### `def add_calculated_channel_folder(self, *args)`

#### `def get_calculated_channel_list(self) -> Sequence[CalculatedChannel]`

#### `def get_calculated_channel_list(self, *args)`

#### `def add_calculated_channel(self, calculated_channel: CalculatedChannel) -> bool`

#### `def add_calculated_channel(self, *args)`

#### `def add_formula(self, formula: Formula) -> bool`

#### `def add_formula(self, *args)`

#### `def add_maximum(self, maximum: Maximum) -> bool`

#### `def add_maximum(self, *args)`

#### `def add_minimum(self, minimum: Minimum) -> bool`

#### `def add_minimum(self, *args)`

#### `def add_lowpass_filter(self, lowpass_filter: LowpassFilter) -> bool`

#### `def add_lowpass_filter(self, *args)`

#### `def add_peak_and_valley(self, peak_and_valley: PeakAndValley) -> bool`

#### `def add_peak_and_valley(self, *args)`

#### `def add_acceleration(self, acceleration: Acceleration) -> bool`

#### `def add_acceleration(self, *args)`

#### `def add_average(self, average: Average) -> bool`

#### `def add_average(self, *args)`

#### `def add_conditional(self, conditional: Conditional) -> bool`

#### `def add_conditional(self, *args)`

### `class Channel(BaseNode, IChannel)`

Represents a channel in the system definition. This is a base class for more specific channel classes, including hardware channels, system channels, user channels, calculated channels, and so on.

#### `def __init__(self, node: BaseNodeType)`

#### `def __init__(self, node: ChannelType)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def k_readable() -> int`

#### `def k_writable() -> int`

#### `def k_faultable() -> int`

#### `def k_scalable() -> int`

#### `def scale(self) -> Scale`

Gets or sets the value of the scale property on the channel.

#### `def scale(self, value: Scale)`

Gets or sets the value of the scale property on the channel.

#### `def bit_fields(self) -> int`

Gets a bitfield mask that is set on the channel.

#### `def default_value(self) -> Sequence[float]`

Gets the default value of the channel.

### `class Chassis(Section)`

Represents a chassis, which contains any NI-DAQ devices, reflective memory devices, NI FPGA targets, NI-XNET devices, and timing and sync devices you add.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def clear_chassis_master_device(self)`

#### `def clear_chassis_master_device(self, *args)`

#### `def set_chassis_master_to_daq(self, daq_name: str, clk_src: DAQCM_Clock_Source, active_edge: DAQCM_Active_Edge, export_clk: DAQCM_Export_Sample_Clock, export_clk_to_line: DAQCM_Export_Clk_On_Line, trigger_line: DAQCM_Trigger_Line, trigger_slope: DAQCM_Slope, start_trigger: DAQCM_Export_Start_Trigger, start_trigger_line: DAQCM_Export_StartTrigger_On_Line) -> bool`

#### `def set_chassis_master_to_daq(self, *args)`

#### `def set_chassis_master_to_fpga(self, fpga_name: str) -> bool`

#### `def set_chassis_master_to_fpga(self, *args)`

#### `def set_chassis_master_to_timing_and_sync(self, timing_and_sync_name: str) -> bool`

#### `def set_chassis_master_to_timing_and_sync(self, *args)`

#### `def get_timing_and_sync(self) -> TimingAndSync`

#### `def get_timing_and_sync(self, *args)`

#### `def get_daq(self) -> DAQ`

#### `def get_daq(self, *args)`

#### `def get_fpga(self) -> FPGA`

#### `def get_fpga(self, *args)`

#### `def get_xnet(self) -> XNET`

#### `def get_xnet(self, *args)`

#### `def get_data_sharing(self) -> DataSharing`

#### `def get_data_sharing(self, *args)`

### `class Command(Section)`

Represents a parent class for the different <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Procedure" crefType="Unqualified" /> command types.

#### `def __init__(self, *args)`

Create a new instance.

### `class Condition(Command)`

Represents a <format type="bold">Condition</format> step that you can add to a procedure. The <format type="bold">Condition</format> step executes a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.GotoLabel" crefType="Unqualified" /> step based on the comparison of a constant value or channel value.

#### `def __init__(self, name: str, description: str, variable: BaseNode, comparison: ConditionStepComparison, value: float, goto_label: Command)`

#### `def __init__(self, name: str, description: str, variable: BaseNode, comparison: ConditionStepComparison, value: BaseNode, goto_label: Command)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def comparison(self) -> ConditionStepComparison`

Gets or sets the condition to use when comparing <format type="italics">Variable</format> and <format type="italics">Value</format>.

#### `def comparison(self, value: ConditionStepComparison)`

Gets or sets the condition to use when comparing <format type="italics">Variable</format> and <format type="italics">Value</format>.

#### `def value_constant(self) -> float`

Gets the constant value that is compared to <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Condition.Variable" crefType="Unqualified" />.

#### `def value_is_constant(self) -> bool`

Gets whether the value compared to <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Condition.Variable" crefType="Unqualified" /> is determined by a channel or by a constant.

#### `def goto_label(self) -> BaseNode`

Gets or sets the procedure step to go to if the condition is met.

#### `def goto_label(self, value: BaseNode)`

Gets or sets the procedure step to go to if the condition is met.

#### `def variable(self) -> BaseNode`

Gets or sets the channel against which to test the condition.

#### `def variable(self, value: BaseNode)`

Gets or sets the channel against which to test the condition.

#### `def value_channel(self) -> BaseNode`

Gets the channel that specifies the value that is compared to <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Condition.Variable" crefType="Unqualified" />.

#### `def set_value(self, value: float)`

#### `def set_value(self, value: BaseNode)`

#### `def set_value(self, *args)`

### `class Counter(Section)`

Represents the <format type="bold">Counter</format> section under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.AutomaticFrameProcessing" crefType="Unqualified" /> section of an outgoing frame of an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANPort" crefType="Unqualified" />. This feature increments specific bits every time the frame is transmitted across the bus.

#### `def __init__(self, *args)`

Create a new instance.

#### `def max_afp_length(self) -> int`

Gets or sets the maximum AFP (automatic frame processing) length, which corresponds to the order of the generator polynomial for CRC.

#### `def max_afp_length(self, value: int)`

Gets or sets the maximum AFP (automatic frame processing) length, which corresponds to the order of the generator polynomial for CRC.

#### `def index_counter(self) -> int`

Gets or sets the index of the counter within the frame.

#### `def index_counter(self, value: int)`

Gets or sets the index of the counter within the frame.

#### `def afp_data(self) -> Sequence[int]`

Gets or sets an array of data used to configure the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Counter" crefType="Unqualified" /> feature of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.AutomaticFrameProcessing" crefType="Unqualified" />.

#### `def afp_data(self, value: Sequence[int])`

Gets or sets an array of data used to configure the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Counter" crefType="Unqualified" /> feature of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.AutomaticFrameProcessing" crefType="Unqualified" />.

#### `def use_alternate_channel(self) -> bool`

Gets whether the <format type="italics">AlternateChannel</format> specified by <see cref="M:NationalInstruments.VeriStand.SystemDefinitionAPI.Counter.SetAlternateChannel(NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNode)" crefType="Unqualified" /> is used to trigger writing data.

#### `def alternate_channel(self) -> BaseNode`

Gets the channel used to trigger writing data when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Counter.UseAlternateChannel" crefType="Unqualified" /> is <see langword="true" />.

#### `def remove_alternate_channel(self)`

#### `def remove_alternate_channel(self, *args)`

#### `def set_alternate_channel(self, alternate_channel: BaseNode)`

#### `def set_alternate_channel(self, *args)`

### `class CustomDevice(CustomDeviceSection)`

Represents a custom device in NI VeriStand.

#### `def __init__(self, name: str, guid: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def timed_loop_priority(self) -> CDTimeLoopPriority`

Gets or sets the priority (<format type="monospace">High</format>, <format type="monospace">Low</format>, or <format type="monospace">Medium</format>) of the Timed Loop in which an asynchronous custom device runs. This property only applies to asynchronous custom devices that run in Timed Loops.

#### `def timed_loop_priority(self, value: CDTimeLoopPriority)`

Gets or sets the priority (<format type="monospace">High</format>, <format type="monospace">Low</format>, or <format type="monospace">Medium</format>) of the Timed Loop in which an asynchronous custom device runs. This property only applies to asynchronous custom devices that run in Timed Loops.

#### `def loop_type(self) -> CDLoopType`

Gets or sets the type of loop (<format type="monospace">TimedLoop</format> or <format type="monospace">WhileLoop</format>) in which the custom device runs. This property only applies to asynchronous custom devices.

#### `def loop_type(self, value: CDLoopType)`

Gets or sets the type of loop (<format type="monospace">TimedLoop</format> or <format type="monospace">WhileLoop</format>) in which the custom device runs. This property only applies to asynchronous custom devices.

#### `def driver_vi_execution_mode(self) -> CDDriverExecMode`

Gets or sets the execution mode of the custom device, such as if it runs inline with the Primary Control Loop or asynchronously.

#### `def driver_vi_execution_mode(self, value: CDDriverExecMode)`

Gets or sets the execution mode of the custom device, such as if it runs inline with the Primary Control Loop or asynchronously.

#### `def device_enabled_state(self) -> bool`

Gets or sets the state (enabled or disabled) of the custom device.
            
             The effect of setting this property will not be visible in System Explorer. Many custom devices provide an alternate TypeGUID and associated glyph to indicate whether the custom device is disabled.

#### `def device_enabled_state(self, value: bool)`

Gets or sets the state (enabled or disabled) of the custom device.
            
             The effect of setting this property will not be visible in System Explorer. Many custom devices provide an alternate TypeGUID and associated glyph to indicate whether the custom device is disabled.

#### `def version(self) -> str`

Gets or sets information stored with a custom device, such as version information. You can read this string to determine whether to update device dependencies or, if you are migrating a custom device to a new version of NI VeriStand, to determine whether to run mutation code.

#### `def version(self, value: str)`

Gets or sets information stored with a custom device, such as version information. You can read this string to determine whether to update device dependencies or, if you are migrating a custom device to a new version of NI VeriStand, to determine whether to run mutation code.

#### `def use_device_clock(self) -> bool`

Gets or sets whether the Timed Loop in which an asynchronous custom device runs is synchronized with the Primary Control Loop (PCL) timing source. This property only applies to asynchronous custom devices that run in Timed Loops.

#### `def use_device_clock(self, value: bool)`

Gets or sets whether the Timed Loop in which an asynchronous custom device runs is synchronized with the Primary Control Loop (PCL) timing source. This property only applies to asynchronous custom devices that run in Timed Loops.

#### `def decimation(self) -> int`

Gets or sets the decimation factor for the custom device, which determines how many iterations of the Primary Control Loop (PCL) occur between calls to the custom device.

#### `def decimation(self, value: int)`

Gets or sets the decimation factor for the custom device, which determines how many iterations of the Primary Control Loop (PCL) occur between calls to the custom device.

#### `def fifo_source_depth(self) -> int`

Gets or sets the depth of the FIFO at the source. This property defines the size of the buffer for incoming data. This property only applies to asynchronous custom devices.

#### `def fifo_source_depth(self, value: int)`

Gets or sets the depth of the FIFO at the source. This property defines the size of the buffer for incoming data. This property only applies to asynchronous custom devices.

#### `def fifo_sink_depth(self) -> int`

Gets or sets the depth of the FIFO at the sink. This property defines the size of the buffer for outgoing data. This property only applies to asynchronous custom devices.

#### `def fifo_sink_depth(self, value: int)`

Gets or sets the depth of the FIFO at the sink. This property defines the size of the buffer for outgoing data. This property only applies to asynchronous custom devices.

#### `def get_custom_device_channel_list(self) -> Sequence[CustomDeviceChannel]`

#### `def get_custom_device_channel_list(self, *args)`

#### `def get_custom_device_waveform_list(self) -> Sequence[CustomDeviceWaveform]`

#### `def get_custom_device_waveform_list(self, *args)`

#### `def get_custom_device_section_list(self) -> Sequence[CustomDeviceSection]`

#### `def get_custom_device_section_list(self, *args)`

#### `def get_dependencies(self) -> Sequence[DependentFile]`

#### `def get_dependencies(self, *args)`

#### `def get_driver_vi_for_owner_target_type(self) -> DependentFile`

#### `def get_driver_vi_for_owner_target_type(self, *args)`

#### `def get_driver_v_is(self) -> Sequence[DependentFile]`

#### `def get_driver_v_is(self, *args)`

#### `def get_timing_source_init_v_is(self) -> Sequence[DependentFile]`

#### `def get_timing_source_init_v_is(self, *args)`

#### `def add_dependencies(self, dependencies: Sequence[DependentFile])`

#### `def add_dependencies(self, *args)`

#### `def set_driver_v_is(self, driver_v_is: Sequence[DependentFile])`

#### `def set_driver_v_is(self, *args)`

#### `def set_timing_source_init_v_is(self, timing_source_init_v_is: Sequence[DependentFile])`

#### `def set_timing_source_init_v_is(self, *args)`

#### `def reset_dependencies(self)`

#### `def reset_dependencies(self, *args)`

### `class CustomDeviceChannel(CustomDeviceBase, IChannel)`

Represents a channel in a custom device.

#### `def __init__(self, name: str, guid: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def type(self) -> CDChannel_Type`

Gets or sets whether a custom device channel is an input or output channel. Only input channels are writable.

#### `def type(self, value: CDChannel_Type)`

Gets or sets whether a custom device channel is an input or output channel. Only input channels are writable.

#### `def faultable(self) -> bool`

Gets or sets whether a custom device channel is faultable, meaning the VeriStand Engine can fault the channel using software fault insertion.

#### `def faultable(self, value: bool)`

Gets or sets whether a custom device channel is faultable, meaning the VeriStand Engine can fault the channel using software fault insertion.

#### `def scalable(self) -> bool`

Gets or sets whether a custom device channel can be calibrated or scaled into specific engineering units.

#### `def scalable(self, value: bool)`

Gets or sets whether a custom device channel can be calibrated or scaled into specific engineering units.

#### `def default_value(self) -> float`

Gets or sets the default value for a custom device channel.

#### `def default_value(self, value: float)`

Gets or sets the default value for a custom device channel.

#### `def scale(self) -> Scale`

Gets or sets the value of the scale property on the channel.

#### `def scale(self, value: Scale)`

Gets or sets the value of the scale property on the channel.

#### `def bit_fields(self) -> int`

For internal use only. Stores various channel settings, such as its type, default value, whether it is faultable or scalable, and so on. Use the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceChannel.DefaultValue" crefType="Unqualified" />, <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceChannel.Faultable" crefType="Unqualified" />, <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceChannel.Scalable" crefType="Unqualified" />, and <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.CustomDeviceChannel.Type" crefType="Unqualified" /> properties to get the information the bit field contains.

#### `def set_value_table(self, names: Sequence[str], values: Sequence[float])`

#### `def set_value_table(self, *args)`

### `class CustomDevices(Section)`

Represents the top-level <format type="bold">Custom Devices</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Target" crefType="Unqualified" />. This section contains all the custom devices (except timing and sync devices) that you add to the system definition.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_custom_device_list(self) -> Sequence[CustomDevice]`

#### `def get_custom_device_list(self, *args)`

#### `def add_custom_device(self, custom_device: CustomDevice) -> bool`

#### `def add_custom_device(self, *args)`

### `class Cyclic(Section)`

Represents the <format type="bold">Cyclic</format> section that contains outgoing cyclic frames under an NI-XNET CAN or FlexRay port. Use cyclic frames when you want data changes to arrive at other ECUs within a well-defined deadline.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_signal_based_frame_list(self) -> Sequence[SignalBasedFrame]`

#### `def get_signal_based_frame_list(self, *args)`

#### `def get_raw_data_based_frame_list(self) -> Sequence[RawDataBasedFrame]`

#### `def get_raw_data_based_frame_list(self, *args)`

#### `def add_signal_based_frame(self, signal_based_frame: SignalBasedFrame) -> bool`

#### `def add_signal_based_frame(self, *args)`

#### `def add_raw_data_based_frame(self, raw_data_based_frame: RawDataBasedFrame) -> bool`

#### `def add_raw_data_based_frame(self, *args)`

### `class CyclicEvent(Section)`

Represents the <format type="bold">CyclicEvent</format> section that contains outgoing cyclic/event frames under an NI-XNET CAN port. Use cyclic/event frames when you want data changes to arrive at other ECUs within a well-defined deadline with the additional ability to send frames on demand.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_signal_based_frame_list(self) -> Sequence[SignalBasedFrame]`

#### `def get_signal_based_frame_list(self, *args)`

#### `def get_raw_data_based_frame_list(self) -> Sequence[RawDataBasedFrame]`

#### `def get_raw_data_based_frame_list(self, *args)`

#### `def add_signal_based_frame(self, signal_based_frame: SignalBasedFrame) -> bool`

#### `def add_signal_based_frame(self, *args)`

#### `def add_raw_data_based_frame(self, raw_data_based_frame: RawDataBasedFrame) -> bool`

#### `def add_raw_data_based_frame(self, *args)`

### `class DAQ(Section)`

Represents the <format type="bold">DAQ</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Chassis" crefType="Unqualified" /> in the system definition. This section contains all the DAQ devices you add under the chassis.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_device_list(self) -> Sequence[DAQDevice]`

#### `def get_device_list(self, *args)`

#### `def get_tasks(self) -> DAQTasks`

#### `def get_tasks(self, *args)`

#### `def add_device(self, device: DAQDevice) -> bool`

#### `def add_device(self, *args)`

### `class DAQAnalogInputs(Section)`

Represents an <format type="bold">Analog Input</format> section under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice" crefType="Unqualified" />, which contains all <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQAnalogInput" crefType="Unqualified" /> channels you add for the device.

#### `def __init__(self, *args)`

Create a new instance.

#### `def sample_mode(self) -> SampleMode`

Gets or sets whether the acquisition is single-point or buffered.

#### `def sample_mode(self, value: SampleMode)`

Gets or sets whether the acquisition is single-point or buffered.

#### `def waveform_analog_input_task(self) -> DAQTaskAI`

Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> associated with the buffered acquisition.

#### `def waveform_analog_input_task(self, value: DAQTaskAI)`

Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> associated with the buffered acquisition.

#### `def is_slow_background_convert_enabled(self) -> bool`

Gets whether the Slow Background Convert configuration is enabled.

#### `def slow_background_convert_rate(self) -> float`

Gets the Slow Background Convert sample rate.

#### `def get_analog_input_list(self) -> Sequence[DAQAnalogInput]`

#### `def get_analog_input_list(self, *args)`

#### `def get_waveform_analog_input_list(self) -> Sequence[DAQWaveformAnalogInput]`

#### `def get_waveform_analog_input_list(self, *args)`

#### `def add_analog_input(self, analog_input: DAQAnalogInput) -> bool`

#### `def add_analog_input(self, *args)`

#### `def add_waveform_analog_input(self, waveform_analog_input: DAQWaveformAnalogInput) -> bool`

#### `def add_waveform_analog_input(self, *args)`

#### `def slow_background_convert_mode(self, enable: bool, rate: float)`

#### `def slow_background_convert_mode(self, *args)`

### `class DAQAnalogOutputs(Section)`

Represents an <format type="bold">Analog Output</format> section under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice" crefType="Unqualified" />, which contains all <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQAnalogOutput" crefType="Unqualified" /> channels you add for the device.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_analog_output_list(self) -> Sequence[DAQAnalogOutput]`

#### `def get_analog_output_list(self, *args)`

#### `def add_analog_output(self, analog_output: DAQAnalogOutput) -> bool`

#### `def add_analog_output(self, *args)`

### `class DAQChannel(Channel, IChannel)`

Provides an abstract base class for implementing DAQ device channels and their measurement types based on DAQ plug-in XML files.

#### `def __init__(self, *args)`

Create a new instance.

#### `def plugin_guid(self) -> str`

Gets the GUID that corresponds to the type of measurement or generation the channel performs.

#### `def measurement_type(self) -> DAQMeasurementType`

Gets the type of measurement or generation the DAQ channel performs.

#### `def get_double_property(self, property_name: str) -> float`

#### `def get_double_property(self, *args)`

#### `def get_u64_property(self, property_name: str) -> int`

#### `def get_u64_property(self, *args)`

#### `def get_u32_property(self, property_name: str) -> int`

#### `def get_u32_property(self, *args)`

#### `def get_u16_property(self, property_name: str) -> int`

#### `def get_u16_property(self, *args)`

#### `def get_i64_property(self, property_name: str) -> int`

#### `def get_i64_property(self, *args)`

#### `def get_i32_property(self, property_name: str) -> int`

#### `def get_i32_property(self, *args)`

#### `def get_i16_property(self, property_name: str) -> int`

#### `def get_i16_property(self, *args)`

#### `def get_boolean_property(self, property_name: str) -> bool`

#### `def get_boolean_property(self, *args)`

#### `def get_string_property(self, property_name: str) -> str`

#### `def get_string_property(self, *args)`

#### `def get_enum_property(self, property_name: str) -> Tuple[str, int]`

#### `def get_enum_property(self, *args)`

#### `def get_properties(self) -> Tuple[Sequence[str], Sequence[ValueDataType]]`

#### `def get_properties(self, *args)`

#### `def reset_property_values(self)`

#### `def reset_property_values(self, *args)`

#### `def set_double_property(self, property_name: str, value: float)`

#### `def set_double_property(self, *args)`

#### `def set_u64_property(self, property_name: str, value: int)`

#### `def set_u64_property(self, *args)`

#### `def set_u32_property(self, property_name: str, value: int)`

#### `def set_u32_property(self, *args)`

#### `def set_u16_property(self, property_name: str, value: int)`

#### `def set_u16_property(self, *args)`

#### `def set_i64_property(self, property_name: str, value: int)`

#### `def set_i64_property(self, *args)`

#### `def set_i32_property(self, property_name: str, value: int)`

#### `def set_i32_property(self, *args)`

#### `def set_i16_property(self, property_name: str, value: int)`

#### `def set_i16_property(self, *args)`

#### `def set_boolean_property(self, property_name: str, value: bool)`

#### `def set_boolean_property(self, *args)`

#### `def set_string_property(self, property_name: str, value: str)`

#### `def set_string_property(self, *args)`

#### `def set_enum_property(self, property_name: str, enum_string: str)`

#### `def set_enum_property(self, property_name: str, value: int)`

#### `def set_enum_property(self, *args)`

### `class DAQCounter(DAQChannel, IChannel)`

Represents a DAQ counter channel.

#### `def __init__(self, name: str, index: int, plugin_guid: str)`

#### `def __init__(self, name: str, index: int, plugin_guid: str, initial_value: float)`

#### `def __init__(self, name: str, index: int, measurement_type: DAQMeasurementType)`

#### `def __init__(self, name: str, index: int, measurement_type: DAQMeasurementType, initial_value: float)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def default_terminal() -> str`

#### `def initial_value(self) -> float`

Gets or sets the initial value of the counter channel.

#### `def initial_value(self, value: float)`

Gets or sets the initial value of the counter channel.

#### `def data_task(self) -> DAQCounterType`

Gets the type of task the counter performs (frequency measurement, period measurement, count up/down, or position measurement).

#### `def counter(self) -> str`

Gets the counter channel number.

#### `def downcast(self) -> DAQCounter`

#### `def downcast(self, *args)`

#### `def set_counter_index(self, index: int) -> bool`

#### `def set_counter_index(self, *args)`

### `class DAQCounters(Section)`

Represents a <format type="bold">Counter</format> section under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice" crefType="Unqualified" />, which contains all <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter" crefType="Unqualified" /> channels you add for the device.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_counter_list(self) -> Sequence[DAQCounter]`

#### `def get_counter_list(self, *args)`

#### `def get_counter_outputs(self) -> Sequence[DAQCounterOutput]`

#### `def get_counter_outputs(self, *args)`

#### `def get_counter_inputs(self) -> Sequence[DAQCounterInput]`

#### `def get_counter_inputs(self, *args)`

#### `def add_counter(self, counter: DAQCounter) -> bool`

#### `def add_counter(self, *args)`

#### `def add_counter_input(self, counter: DAQCounterInput) -> bool`

#### `def add_counter_input(self, *args)`

#### `def add_counter_output(self, counter: DAQCounterOutput) -> bool`

#### `def add_counter_output(self, *args)`

### `class DAQDIOPort(Section)`

Represents a DAQ DIO port, which contains <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDigitalInput" crefType="Unqualified" /> and/or <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDigitalOutput" crefType="Unqualified" /> channels.

#### `def __init__(self, port_number: int, inverted: bool)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def inverted(self) -> bool`

Gets or sets whether the digital lines are inverted.

#### `def inverted(self, value: bool)`

Gets or sets whether the digital lines are inverted.

#### `def get_digital_inputs(self) -> Sequence[DAQDigitalInput]`

#### `def get_digital_inputs(self, *args)`

#### `def get_digital_outputs(self) -> Sequence[DAQDigitalOutput]`

#### `def get_digital_outputs(self, *args)`

#### `def add_digital_input(self, digital_input: DAQDigitalInput) -> bool`

#### `def add_digital_input(self, *args)`

#### `def add_digital_output(self, digital_output: DAQDigitalOutput) -> bool`

#### `def add_digital_output(self, *args)`

### `class DAQDevice(Section)`

Represents a DAQ device.

#### `def __init__(self, name: str, description: str, input_configuration: DAQDeviceInputConfiguration)`

#### `def __init__(self, name: str, description: str, input_configuration: DAQDeviceInputConfiguration, num_ai_channels: int, num_ao_channels: int, num_di_channels: int, num_do_channels: int, port_width: int)`

#### `def __init__(self, name: str, description: str, input_configuration: DAQDeviceInputConfiguration, num_ai_channels: int, num_ao_channels: int, num_di_channels: int, num_do_channels: int, port_width: int, counter_types: Sequence[DAQCounterType], num_internal_channels: int)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def backplane_reference_clock(self) -> PXIBackplaneReferenceClock`

Sets or gets the reference clock on the PXI/PXIe chassis backplane to which the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice" /> synchronizes its timing.

#### `def backplane_reference_clock(self, value: PXIBackplaneReferenceClock)`

Sets or gets the reference clock on the PXI/PXIe chassis backplane to which the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice" /> synchronizes its timing.

#### `def product_id(self) -> int`

Public, always writable version of DAQ Product ID
            DAQ Product ID is the unique numeric identifier for a DAQ device.

#### `def product_id(self, value: int)`

Public, always writable version of DAQ Product ID
            DAQ Product ID is the unique numeric identifier for a DAQ device.

#### `def product_category(self) -> int`

Public, always writable version of DAQ Product Category.
            Unique identifier for each DAQ Product category.

#### `def product_category(self, value: int)`

Public, always writable version of DAQ Product Category.
            Unique identifier for each DAQ Product category.

#### `def product_name(self) -> str`

Public, always writable version of DAQ Product Name.

#### `def product_name(self, value: str)`

Public, always writable version of DAQ Product Name.

#### `def input_configuration(self) -> DAQDeviceInputConfiguration`

Gets or sets the input terminal configuration applied to device channels.

#### `def input_configuration(self, value: DAQDeviceInputConfiguration)`

Gets or sets the input terminal configuration applied to device channels.

#### `def daq_conversion_rate_option(self) -> DAQConversionRate`

Gets or sets the rate used to run the analog-digital converters on the DAQ device.

#### `def daq_conversion_rate_option(self, value: DAQConversionRate)`

Gets or sets the rate used to run the analog-digital converters on the DAQ device.

#### `def turn_off_hw_timed_single_point_ai(self) -> bool`

Gets or sets whether hardware-timed single-point support is disabled for analog input tasks.

#### `def turn_off_hw_timed_single_point_ai(self, value: bool)`

Gets or sets whether hardware-timed single-point support is disabled for analog input tasks.

#### `def port_width(self) -> int`

Gets or sets the total number of lines per port.

#### `def port_width(self, value: int)`

Gets or sets the total number of lines per port.

#### `def turn_off_hw_timed_single_point_ao(self) -> bool`

Gets or sets whether hardware-timed single-point support is disabled for analog output tasks.

#### `def turn_off_hw_timed_single_point_ao(self, value: bool)`

Gets or sets whether hardware-timed single-point support is disabled for analog output tasks.

#### `def create_analog_inputs(self) -> DAQAnalogInputs`

#### `def create_analog_inputs(self, mode: SampleMode) -> DAQAnalogInputs`

#### `def create_analog_inputs(self, *args)`

#### `def create_analog_outputs(self) -> DAQAnalogOutputs`

#### `def create_analog_outputs(self, *args)`

#### `def create_counters(self) -> DAQCounters`

#### `def create_counters(self, *args)`

#### `def create_digital_inputs(self) -> DAQDigitalInputs`

#### `def create_digital_inputs(self, *args)`

#### `def create_digital_outputs(self) -> DAQDigitalOutputs`

#### `def create_digital_outputs(self, *args)`

#### `def create_scxi_chassis(self) -> SCXIChassis`

#### `def create_scxi_chassis(self, *args)`

#### `def create_internal_channels(self) -> DAQInternalChannels`

#### `def create_internal_channels(self, *args)`

#### `def populate_device(self, num_ai_channels: int, num_ao_channels: int, num_di_channels: int, num_do_channels: int, port_width: int)`

#### `def populate_device(self, num_ai_channels: int, num_ao_channels: int, num_di_channels: int, num_do_channels: int, port_width: int, counter_types: Sequence[DAQCounterType], num_internal_channels: int)`

#### `def populate_device(self, *args)`

#### `def get_analog_input_section(self) -> DAQAnalogInputs`

#### `def get_analog_input_section(self, *args)`

#### `def get_analog_output_section(self) -> DAQAnalogOutputs`

#### `def get_analog_output_section(self, *args)`

#### `def get_counter_section(self) -> DAQCounters`

#### `def get_counter_section(self, *args)`

#### `def get_digital_input_section(self) -> DAQDigitalInputs`

#### `def get_digital_input_section(self, *args)`

#### `def get_digital_output_section(self) -> DAQDigitalOutputs`

#### `def get_digital_output_section(self, *args)`

#### `def get_scxi_chassis_section(self) -> SCXIChassis`

#### `def get_scxi_chassis_section(self, *args)`

#### `def get_internal_channels_section(self) -> DAQInternalChannels`

#### `def get_internal_channels_section(self, *args)`

### `class DAQDigitalInput(DAQChannel, IChannel)`

Represents a DAQ digital input channel.

#### `def __init__(self, name: str, digital_line: int, port_number: int, plugin_guid: str)`

#### `def __init__(self, name: str, digital_line: int, port_number: int, initial_value: bool, plugin_guid: str)`

#### `def __init__(self, name: str, digital_line: int, port_number: int, measurement_type: DAQMeasurementType)`

#### `def __init__(self, name: str, digital_line: int, port_number: int, initial_value: bool, measurement_type: DAQMeasurementType)`

#### `def __init__(self, name: str, initial_value: bool, digital_line: int, port_number: int)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def inital_value(self) -> bool`

Gets or sets the initial value of the digital input channel.

#### `def inital_value(self, value: bool)`

Gets or sets the initial value of the digital input channel.

#### `def digital_line(self) -> int`

Gets or sets the digital line for the channel.

#### `def digital_line(self, value: int)`

Gets or sets the digital line for the channel.

#### `def port_number(self) -> int`

Gets or sets the port to which the channel belongs.

#### `def port_number(self, value: int)`

Gets or sets the port to which the channel belongs.

#### `def is_scxi(self) -> bool`

Gets whether the channel belongs to an SCXI module.

### `class DAQDigitalInputs(Section)`

Represents a <format type="bold">Digital Input</format> section under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice" crefType="Unqualified" />, which contains the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDIOPort" crefType="Unqualified" /> ports for <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDigitalInput" crefType="Unqualified" /> channels.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_dio_ports(self) -> Sequence[DAQDIOPort]`

#### `def get_dio_ports(self, *args)`

#### `def add_dio_port(self, dio_port: DAQDIOPort) -> bool`

#### `def add_dio_port(self, *args)`

### `class DAQDigitalOutput(DAQChannel, IChannel)`

Represents a DAQ digital output channel.

#### `def __init__(self, name: str, digital_line: int, port_number: int, plugin_guid: str)`

#### `def __init__(self, name: str, digital_line: int, port_number: int, initial_value: bool, plugin_guid: str)`

#### `def __init__(self, name: str, digital_line: int, port_number: int, measurement_type: DAQMeasurementType)`

#### `def __init__(self, name: str, digital_line: int, port_number: int, initial_value: bool, measurement_type: DAQMeasurementType)`

#### `def __init__(self, name: str, initial_value: bool, digital_line: int, port_number: int)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def inital_value(self) -> bool`

Gets or sets the initial value of the digital output channel.

#### `def inital_value(self, value: bool)`

Gets or sets the initial value of the digital output channel.

#### `def digital_line(self) -> int`

Gets or sets the digital line for the channel.

#### `def digital_line(self, value: int)`

Gets or sets the digital line for the channel.

#### `def port_number(self) -> int`

Gets or sets the port to which the channel belongs.

#### `def port_number(self, value: int)`

Gets or sets the port to which the channel belongs.

#### `def is_scxi(self) -> bool`

Gets whether the channel belongs to an SCXI module.

### `class DAQDigitalOutputs(Section)`

Represents a <format type="bold">Digital Output</format> section under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice" crefType="Unqualified" />, which contains the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDIOPort" crefType="Unqualified" /> ports for <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDigitalOutput" crefType="Unqualified" /> channels.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_dio_ports(self) -> Sequence[DAQDIOPort]`

#### `def get_dio_ports(self, *args)`

#### `def add_dio_port(self, dio_port: DAQDIOPort) -> bool`

#### `def add_dio_port(self, *args)`

### `class DAQFrequencyMeasurement(DAQCounter, IChannel)`

Represents a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter" crefType="Unqualified" /> channel with the frequency measurement task type.

#### `def __init__(self, name: str, description: str, index: int, default_value: float, maximum: float, minimum: float, edge: DAQCounterEdge)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def edge(self) -> DAQCounterEdge`

Gets or sets the edge on which to count (rising or falling).

#### `def edge(self, value: DAQCounterEdge)`

Gets or sets the edge on which to count (rising or falling).

#### `def input_terminal(self) -> str`

Gets or sets the input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used.

#### `def input_terminal(self, value: str)`

Gets or sets the input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used.

#### `def max(self) -> float`

Gets or sets the maximum value of the channel in hertz.

#### `def max(self, value: float)`

Gets or sets the maximum value of the channel in hertz.

#### `def min(self) -> float`

Gets or sets the minimum value of the channel in hertz.

#### `def min(self, value: float)`

Gets or sets the minimum value of the channel in hertz.

### `class DAQInternalChannel(Channel, IChannel)`

Represents a DAQ internal channel.

#### `def __init__(self, name: str, default_value: float)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def low_level(self) -> float`

Gets or sets the minimum value of the channel.

#### `def low_level(self, value: float)`

Gets or sets the minimum value of the channel.

#### `def high_level(self) -> float`

Gets or sets the maximum value of the channel.

#### `def high_level(self, value: float)`

Gets or sets the maximum value of the channel.

#### `def channel(self) -> str`

Gets or sets the physical name for the channel.

#### `def channel(self, value: str)`

Gets or sets the physical name for the channel.

### `class DAQInternalChannels(Section)`

Represents an <format type="bold">Internal Channels</format> section under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice" crefType="Unqualified" />, which contains any <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQInternalChannel" crefType="Unqualified" /> objects to add to the device.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_internal_channel_list(self) -> Sequence[DAQInternalChannel]`

#### `def get_internal_channel_list(self, *args)`

#### `def add_internal_channel(self, internal_channel: DAQInternalChannel) -> bool`

#### `def add_internal_channel(self, *args)`

### `class DAQLogging(Section)`

Represents the <format type="bold">Logging</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" />.

#### `def __init__(self, *args)`

Create a new instance.

#### `def use_task_as_filename(self) -> bool`

Gets or sets a value indicating whether to use the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTask" /> name from the system definition as the base of log filenames.

#### `def use_task_as_filename(self, value: bool)`

Gets or sets a value indicating whether to use the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTask" /> name from the system definition as the base of log filenames.

#### `def filename_base(self) -> str`

Gets or sets the base string used in log filenames. Use this property when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.UseTaskAsFilename" /> is <see langword="false" /> to specify a filename base other than the task name.

#### `def filename_base(self, value: str)`

Gets or sets the base string used in log filenames. Use this property when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.UseTaskAsFilename" /> is <see langword="false" /> to specify a filename base other than the task name.

#### `def log_directory(self) -> str`

Gets or sets the directory in which to save log files on the target.

#### `def log_directory(self, value: str)`

Gets or sets the directory in which to save log files on the target.

#### `def timestamp_filename(self) -> bool`

Gets or sets a value indicating whether to append timestamps to the log filenames.

#### `def timestamp_filename(self, value: bool)`

Gets or sets a value indicating whether to append timestamps to the log filenames.

#### `def action_on_new(self) -> ActionOnNew`

Gets or sets the location to log data when the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> begins a new acquisition.

#### `def action_on_new(self, value: ActionOnNew)`

Gets or sets the location to log data when the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> begins a new acquisition.

#### `def use_task_as_group_name(self) -> bool`

Gets or sets a value indicating whether to use the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTask" /> name from the system definition as the group name under which data is logged in the TDMS file.

#### `def use_task_as_group_name(self, value: bool)`

Gets or sets a value indicating whether to use the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTask" /> name from the system definition as the group name under which data is logged in the TDMS file.

#### `def group_name(self) -> str`

Gets or sets the group name to which the task logs data in the TDMS file. Use this property when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.UseTaskAsGroupName" /> is <see langword="false" /> to specify a group name other than the task name.

#### `def group_name(self, value: str)`

Gets or sets the group name to which the task logs data in the TDMS file. Use this property when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.UseTaskAsGroupName" /> is <see langword="false" /> to specify a group name other than the task name.

#### `def logging_enabled(self) -> bool`

Gets or sets a value indicating whether the Logging Enabled <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskCommand" /> channel is allowed to start and stop logging. Note that this property does not toggle logging; the Logging Enabled channel toggles logging.

#### `def logging_enabled(self, value: bool)`

Gets or sets a value indicating whether the Logging Enabled <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskCommand" /> channel is allowed to start and stop logging. Note that this property does not toggle logging; the Logging Enabled channel toggles logging.

#### `def logging_mode(self) -> LogMode`

Gets or sets whether data is available to components in the NI VeriStand system while you log it.  This property valid only if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.LoggingEnabled" /> is <see langword="true" />.

#### `def logging_mode(self, value: LogMode)`

Gets or sets whether data is available to components in the NI VeriStand system while you log it.  This property valid only if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.LoggingEnabled" /> is <see langword="true" />.

#### `def span_multiple_files(self) -> bool`

Gets or sets a value indicating whether to create a new log file when you reach the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.SamplesPerFile" /> limit.

#### `def span_multiple_files(self, value: bool)`

Gets or sets a value indicating whether to create a new log file when you reach the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.SamplesPerFile" /> limit.

#### `def samples_per_file(self) -> int`

Gets or sets a limit to the number of samples per channel to log to the current file when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.SpanMultipleFiles" /> is <see langword="true" />. This property not active if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.SpanMultipleFiles" /> is <see langword="false" /> because NI VeriStand logs to the current file without limiting the number of samples.

#### `def samples_per_file(self, value: int)`

Gets or sets a limit to the number of samples per channel to log to the current file when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.SpanMultipleFiles" /> is <see langword="true" />. This property not active if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging.SpanMultipleFiles" /> is <see langword="false" /> because NI VeriStand logs to the current file without limiting the number of samples.

#### `def get_logging_enabled_channel(self) -> DAQTaskCommand`

#### `def get_logging_enabled_channel(self, *args)`

#### `def get_start_new_file_channel(self) -> DAQTaskCommand`

#### `def get_start_new_file_channel(self, *args)`

### `class DAQPeriodMeasurement(DAQCounter, IChannel)`

Represents a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter" crefType="Unqualified" /> channel with the period measurement task type.

#### `def __init__(self, name: str, description: str, index: int, default_value: float, maximum: float, minimum: float, edge: DAQCounterEdge)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def edge(self) -> DAQCounterEdge`

Gets or sets the edge on which to count (rising or falling).

#### `def edge(self, value: DAQCounterEdge)`

Gets or sets the edge on which to count (rising or falling).

#### `def input_terminal(self) -> str`

Gets or sets the input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used.

#### `def input_terminal(self, value: str)`

Gets or sets the input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used.

#### `def max(self) -> float`

Gets or sets the maximum value of the channel in seconds.

#### `def max(self, value: float)`

Gets or sets the maximum value of the channel in seconds.

#### `def min(self) -> float`

Gets or sets the minimum value of the channel in seconds.

#### `def min(self, value: float)`

Gets or sets the minimum value of the channel in seconds.

### `class DAQPositionMeasurement(DAQCounter, IChannel)`

Represents a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter" crefType="Unqualified" /> channel with the position measurement task type.

#### `def __init__(self, name: str, description: str, index: int, default_value: float, decoding: DAQCounterDecoding, z_index_mode: DAQCounterZIndexMode)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def decoding(self) -> DAQCounterDecoding`

Gets or sets the method used to count and interpret the pulses the encoder generates on signal A and signal B.

#### `def decoding(self, value: DAQCounterDecoding)`

Gets or sets the method used to count and interpret the pulses the encoder generates on signal A and signal B.

#### `def z_index_mode(self) -> DAQCounterZIndexMode`

Gets or sets the states at which signal A and signal B must be while signal Z is high for the device to reset the measurement.

#### `def z_index_mode(self, value: DAQCounterZIndexMode)`

Gets or sets the states at which signal A and signal B must be while signal Z is high for the device to reset the measurement.

#### `def a_input_terminal(self) -> str`

Gets or sets the A input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used.

#### `def a_input_terminal(self, value: str)`

Gets or sets the A input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used.

#### `def b_input_terminal(self) -> str`

Gets or sets the B input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used.

#### `def b_input_terminal(self, value: str)`

Gets or sets the B input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used.

#### `def z_input_terminal(self) -> str`

Gets or sets the Z input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used.

#### `def z_input_terminal(self, value: str)`

Gets or sets the Z input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used.

### `class DAQSectionType(Section)`

Represents a generic DAQ data section.

#### `def __init__(self, *args)`

Create a new instance.

#### `def plugin_guid(self) -> str`

Gets the GUID specifying DAQPlugin XML/Measurement Type.

#### `def measurement_type(self) -> DAQMeasurementType`

Gets the enum specifying DAQ Measurement Type.

#### `def data_channels(self) -> Sequence[Channel]`

Gets all registered data channels for a measurement type.

#### `def get_double_property(self, property_name: str) -> float`

#### `def get_double_property(self, *args)`

#### `def get_u64_property(self, property_name: str) -> int`

#### `def get_u64_property(self, *args)`

#### `def get_u32_property(self, property_name: str) -> int`

#### `def get_u32_property(self, *args)`

#### `def get_u16_property(self, property_name: str) -> int`

#### `def get_u16_property(self, *args)`

#### `def get_i64_property(self, property_name: str) -> int`

#### `def get_i64_property(self, *args)`

#### `def get_i32_property(self, property_name: str) -> int`

#### `def get_i32_property(self, *args)`

#### `def get_i16_property(self, property_name: str) -> int`

#### `def get_i16_property(self, *args)`

#### `def get_boolean_property(self, property_name: str) -> bool`

#### `def get_boolean_property(self, *args)`

#### `def get_string_property(self, property_name: str) -> str`

#### `def get_string_property(self, *args)`

#### `def get_enum_property(self, property_name: str) -> Tuple[str, int]`

#### `def get_enum_property(self, *args)`

#### `def get_properties(self) -> Tuple[Sequence[str], Sequence[ValueDataType]]`

#### `def get_properties(self, *args)`

#### `def reset_property_values(self)`

#### `def reset_property_values(self, *args)`

#### `def set_double_property(self, property_name: str, value: float)`

#### `def set_double_property(self, *args)`

#### `def set_u64_property(self, property_name: str, value: int)`

#### `def set_u64_property(self, *args)`

#### `def set_u32_property(self, property_name: str, value: int)`

#### `def set_u32_property(self, *args)`

#### `def set_u16_property(self, property_name: str, value: int)`

#### `def set_u16_property(self, *args)`

#### `def set_i64_property(self, property_name: str, value: int)`

#### `def set_i64_property(self, *args)`

#### `def set_i32_property(self, property_name: str, value: int)`

#### `def set_i32_property(self, *args)`

#### `def set_i16_property(self, property_name: str, value: int)`

#### `def set_i16_property(self, *args)`

#### `def set_boolean_property(self, property_name: str, value: bool)`

#### `def set_boolean_property(self, *args)`

#### `def set_string_property(self, property_name: str, value: str)`

#### `def set_string_property(self, *args)`

#### `def set_enum_property(self, property_name: str, enum_string: str)`

#### `def set_enum_property(self, property_name: str, value: int)`

#### `def set_enum_property(self, *args)`

#### `def get_data_channel(self, type: DAQDataChannelType) -> Channel`

#### `def get_data_channel(self, *args)`

### `class DAQTask(Section)`

Provides an <see langword="abstract" /> base class for different types of tasks you can assign to DAQ channels.

#### `def __init__(self, *args)`

Create a new instance.

#### `def task_type(self) -> TaskType`

Gets the task type.

### `class DAQTaskAI(DAQTask)`

Represents a DAQmx task you can assign to one or more DAQ analog input channels to configure timing properties, triggers, and logging.

#### `def __init__(self, name: str, rate: float, mode: AcquisitionMode)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def rate(self) -> float`

Gets or sets the sampling rate, in samples per channel per second, or Hz.

#### `def rate(self, value: float)`

Gets or sets the sampling rate, in samples per channel per second, or Hz.

#### `def acquisition_mode(self) -> AcquisitionMode`

Gets or sets the type of acquisition the task performs.

#### `def acquisition_mode(self, value: AcquisitionMode)`

Gets or sets the type of acquisition the task performs.

#### `def automatic_read_size(self) -> bool`

Gets or sets a value indicating whether to automatically determine the size of read operations that make up an acquisition.

#### `def automatic_read_size(self, value: bool)`

Gets or sets a value indicating whether to automatically determine the size of read operations that make up an acquisition.

#### `def read_samples(self) -> int`

Gets or sets the requested number of samples per channel to read at a time. This property is valid if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.AutomaticReadSize" /> is <see langword="false" />.

#### `def read_samples(self, value: int)`

Gets or sets the requested number of samples per channel to read at a time. This property is valid if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.AutomaticReadSize" /> is <see langword="false" />.

#### `def read_time(self) -> float`

Gets or sets the number of seconds to read at a time. This property is valid if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.AutomaticReadSize" /> is <see langword="false" />.

#### `def read_time(self, value: float)`

Gets or sets the number of seconds to read at a time. This property is valid if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.AutomaticReadSize" /> is <see langword="false" />.

#### `def read_units(self) -> AcquisitionUnits`

Gets or sets whether the task uses <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.ReadTime" /> or <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.ReadSamples" /> as the read size. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> that do not automatically determine the read size.

#### `def read_units(self, value: AcquisitionUnits)`

Gets or sets whether the task uses <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.ReadTime" /> or <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI.ReadSamples" /> as the read size. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> that do not automatically determine the read size.

#### `def acquisition_samples(self) -> int`

Gets or sets the total number of samples per channel to acquire. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> that perform finite acquisitions.

#### `def acquisition_samples(self, value: int)`

Gets or sets the total number of samples per channel to acquire. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> that perform finite acquisitions.

#### `def acquisition_time(self) -> float`

Gets or sets the total number of seconds to acquire data. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> that perform finite acquisitions.

#### `def acquisition_time(self, value: float)`

Gets or sets the total number of seconds to acquire data. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> that perform finite acquisitions.

#### `def acquisition_units(self) -> AcquisitionUnits`

Gets or sets whether the task uses time in seconds or number of samples as the size of the acquisitions it performs. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> that perform finite acquisitions.

#### `def acquisition_units(self, value: AcquisitionUnits)`

Gets or sets whether the task uses time in seconds or number of samples as the size of the acquisitions it performs. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" /> that perform finite acquisitions.

#### `def clock_source(self) -> str`

Gets or sets the source terminal of the sample clock that you want to control acquisition timing.  An empty string corresponds to the default onboard clock of the device.

#### `def clock_source(self, value: str)`

Gets or sets the source terminal of the sample clock that you want to control acquisition timing.  An empty string corresponds to the default onboard clock of the device.

#### `def active_edge(self) -> EdgeType`

Gets or sets the type of edge in the pulses of the sample clock that cause the task to acquire samples: rising or falling.

#### `def active_edge(self, value: EdgeType)`

Gets or sets the type of edge in the pulses of the sample clock that cause the task to acquire samples: rising or falling.

#### `def channel_names(self) -> ChannelNames`

Gets or sets a value that indicates how the names of AI channels appear in log files that this task creates.

#### `def channel_names(self, value: ChannelNames)`

Gets or sets a value that indicates how the names of AI channels appear in log files that this task creates.

#### `def get_logging(self) -> DAQLogging`

#### `def get_logging(self, *args)`

#### `def get_triggers(self) -> DAQTriggers`

#### `def get_triggers(self, *args)`

#### `def get_task_enabled_channel(self) -> DAQTaskCommand`

#### `def get_task_enabled_channel(self, *args)`

#### `def get_devices(self) -> Sequence[DAQDevice]`

#### `def get_devices(self, *args)`

### `class DAQTaskCommand(Channel, IChannel)`

Represents one of the channels under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" />, <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggers" />, or <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQLogging" /> sections. Task command channels control the execution of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" />.

#### `def __init__(self, *args)`

Create a new instance.

#### `def initial_value(self) -> bool`

Gets or sets a value indicating whether the channel is initially enabled or disabled.

#### `def initial_value(self, value: bool)`

Gets or sets a value indicating whether the channel is initially enabled or disabled.

### `class DAQTasks(Section)`

Represents the <format type="bold">Waveform Tasks</format> section in a system definition. This section contains <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTask" /> objects.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_task_list(self) -> Sequence[DAQTask]`

#### `def get_task_list(self, *args)`

#### `def add_task(self, task: DAQTask) -> bool`

#### `def add_task(self, *args)`

#### `def reorder_task_list(self, tasks: Sequence[DAQTask]) -> bool`

#### `def reorder_task_list(self, *args)`

### `class DAQTriggers(Section)`

Represents the <format type="bold">Triggers</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def start_trigger(self) -> DAQTrigger`

Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTrigger" /> that serves as the start trigger for current instance of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" />.

#### `def start_trigger(self, value: DAQTrigger)`

Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTrigger" /> that serves as the start trigger for current instance of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" />.

#### `def reference_trigger(self) -> DAQTrigger`

Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTrigger" /> that serves as the reference trigger for current instance of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" />.

#### `def reference_trigger(self, value: DAQTrigger)`

Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTrigger" /> that serves as the reference trigger for current instance of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTaskAI" />.

#### `def pretrigger_samples(self) -> int`

Gets or sets the number of samples per channel prior to the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggers.ReferenceTrigger" /> to include in the acquisition that begins when the trigger occurs.

#### `def pretrigger_samples(self, value: int)`

Gets or sets the number of samples per channel prior to the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggers.ReferenceTrigger" /> to include in the acquisition that begins when the trigger occurs.

#### `def pretrigger_time(self) -> float`

Gets or sets the length of time, in seconds, prior to the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggers.ReferenceTrigger" /> to include in the acquisition that begins when the trigger occurs.

#### `def pretrigger_time(self, value: float)`

Gets or sets the length of time, in seconds, prior to the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggers.ReferenceTrigger" /> to include in the acquisition that begins when the trigger occurs.

#### `def pretrigger_units(self) -> AcquisitionUnits`

Gets or sets whether the task uses samples or seconds of time as the size of the pre-trigger acquisition it performs. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTrigger" /> that serve as the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggers.ReferenceTrigger" /> for the task.

#### `def pretrigger_units(self, value: AcquisitionUnits)`

Gets or sets whether the task uses samples or seconds of time as the size of the pre-trigger acquisition it performs. This property is valid for instances of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTrigger" /> that serve as the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTriggers.ReferenceTrigger" /> for the task.

#### `def get_retriggerable_channel(self) -> DAQTaskCommand`

#### `def get_retriggerable_channel(self, *args)`

#### `def get_start_trigger_channel(self) -> DAQTaskCommand`

#### `def get_start_trigger_channel(self, *args)`

### `class DAQWaveform(Waveform)`

Represents a generic DAQ waveform.

#### `def __init__(self, *args)`

Create a new instance.

#### `def plugin_guid(self) -> str`

Gets the GUID specifying DAQPlugin XML/Measurement Type.

#### `def measurement_type(self) -> DAQMeasurementType`

Gets the enum specifying DAQ Measurement Type.

#### `def get_double_property(self, property_name: str) -> float`

#### `def get_double_property(self, *args)`

#### `def get_u64_property(self, property_name: str) -> int`

#### `def get_u64_property(self, *args)`

#### `def get_u32_property(self, property_name: str) -> int`

#### `def get_u32_property(self, *args)`

#### `def get_u16_property(self, property_name: str) -> int`

#### `def get_u16_property(self, *args)`

#### `def get_i64_property(self, property_name: str) -> int`

#### `def get_i64_property(self, *args)`

#### `def get_i32_property(self, property_name: str) -> int`

#### `def get_i32_property(self, *args)`

#### `def get_i16_property(self, property_name: str) -> int`

#### `def get_i16_property(self, *args)`

#### `def get_boolean_property(self, property_name: str) -> bool`

#### `def get_boolean_property(self, *args)`

#### `def get_string_property(self, property_name: str) -> str`

#### `def get_string_property(self, *args)`

#### `def get_enum_property(self, property_name: str) -> Tuple[str, int]`

#### `def get_enum_property(self, *args)`

#### `def get_properties(self) -> Tuple[Sequence[str], Sequence[ValueDataType]]`

#### `def get_properties(self, *args)`

#### `def reset_property_values(self)`

#### `def reset_property_values(self, *args)`

#### `def set_double_property(self, property_name: str, value: float)`

#### `def set_double_property(self, *args)`

#### `def set_u64_property(self, property_name: str, value: int)`

#### `def set_u64_property(self, *args)`

#### `def set_u32_property(self, property_name: str, value: int)`

#### `def set_u32_property(self, *args)`

#### `def set_u16_property(self, property_name: str, value: int)`

#### `def set_u16_property(self, *args)`

#### `def set_i64_property(self, property_name: str, value: int)`

#### `def set_i64_property(self, *args)`

#### `def set_i32_property(self, property_name: str, value: int)`

#### `def set_i32_property(self, *args)`

#### `def set_i16_property(self, property_name: str, value: int)`

#### `def set_i16_property(self, *args)`

#### `def set_boolean_property(self, property_name: str, value: bool)`

#### `def set_boolean_property(self, *args)`

#### `def set_string_property(self, property_name: str, value: str)`

#### `def set_string_property(self, *args)`

#### `def set_enum_property(self, property_name: str, enum_string: str)`

#### `def set_enum_property(self, property_name: str, value: int)`

#### `def set_enum_property(self, *args)`

### `class DAQWaveformAnalogInput(DAQWaveform)`

Represents a DAQ analog input waveform used in a buffered acquisition.

#### `def __init__(self, name: str, channel: int, plugin_guid: str)`

#### `def __init__(self, name: str, channel: int, measurement_type: DAQMeasurementType)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def channel(self) -> int`

Gets or sets the channel number.

#### `def channel(self, value: int)`

Gets or sets the channel number.

#### `def low_level(self) -> float`

Gets or sets the minimum value of the channel.

#### `def low_level(self, value: float)`

Gets or sets the minimum value of the channel.

#### `def high_level(self) -> float`

Gets or sets the maximum value of the channel.

#### `def high_level(self, value: float)`

Gets or sets the maximum value of the channel.

### `class DataFileError(Channel, IChannel)`

Represents the <format type="bold">Error</format> channel associated with a raw frame data logging file or data replay file under an NI-XNET port.

#### `def __init__(self, *args)`

Create a new instance.

### `class DataFileReplay(Section)`

Represents a data replay file, which is a raw frame data logging (TDMS or NCL) file that you replay onto a CAN bus.

#### `def __init__(self, name: str, path: str, tdms_group_name: str, tdms_channel_name: str)`

#### `def __init__(self, name: str, path: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def behavior(self) -> ReplayBehavior`

Gets or sets whether and how frames in the data replay file are filtered.

#### `def behavior(self, value: ReplayBehavior)`

Gets or sets whether and how frames in the data replay file are filtered.

#### `def tdms_group_name(self) -> str`

Gets or sets the name of the group in a TDMS file that contains the logged data for replay.

#### `def tdms_group_name(self, value: str)`

Gets or sets the name of the group in a TDMS file that contains the logged data for replay.

#### `def tdms_channel_name(self) -> str`

Gets or sets the name of the channel in a TDMS file that contains the logged data for replay.

#### `def tdms_channel_name(self, value: str)`

Gets or sets the name of the channel in a TDMS file that contains the logged data for replay.

#### `def path(self) -> DependentFile`

Gets or sets the path to the replay file on disk.

#### `def path(self, value: DependentFile)`

Gets or sets the path to the replay file on disk.

#### `def frame_cache_size(self) -> int`

Gets or sets the number of frames cached during replay.

#### `def frame_cache_size(self, value: int)`

Gets or sets the number of frames cached during replay.

#### `def loop_rate(self) -> int`

Gets or sets the rate in hertz at which the frames to send in the outgoing queue are updated. This property does not affect the actual update rate of frames on the CAN bus.

#### `def loop_rate(self, value: int)`

Gets or sets the rate in hertz at which the frames to send in the outgoing queue are updated. This property does not affect the actual update rate of frames on the CAN bus.

#### `def frame_i_ds(self) -> Sequence[str]`

Gets or sets the IDs of the frames in the log file that are included or excluded from the file replay when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataFileReplay.Behavior" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.ReplayBehavior.ExcludeFrameIDs" crefType="Unqualified" /> or <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.ReplayBehavior.IncludeFrameIDs" crefType="Unqualified" />.

#### `def frame_i_ds(self, value: Sequence[str])`

Gets or sets the IDs of the frames in the log file that are included or excluded from the file replay when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataFileReplay.Behavior" crefType="Unqualified" /> is <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.ReplayBehavior.ExcludeFrameIDs" crefType="Unqualified" /> or <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.ReplayBehavior.IncludeFrameIDs" crefType="Unqualified" />.

#### `def trigger_channel(self) -> BaseNode`

Gets or sets the channel used to trigger replay. Replay begins as soon as the value of this channel becomes non-zero. If desired, you can select or configure a channel that triggers multiple replays of the file.

#### `def trigger_channel(self, value: BaseNode)`

Gets or sets the channel used to trigger replay. Replay begins as soon as the value of this channel becomes non-zero. If desired, you can select or configure a channel that triggers multiple replays of the file.

#### `def get_data_file_error(self) -> DataFileError`

#### `def get_data_file_error(self, *args)`

#### `def get_data_file_status(self) -> DataFileStatus`

#### `def get_data_file_status(self, *args)`

### `class DataFileStatus(Channel, IChannel)`

Represents the <format type="bold">Status</format> channel associated with a raw frame data logging file or data replay file under an NI-XNET port.

#### `def __init__(self, *args)`

Create a new instance.

### `class DataLoggingFile(Section)`

Represents a raw frame data logging (TDMS or NCL) file under an NI-XNET port. You can use raw frame data logging files to record incoming frame data during an NI-XNET session.

#### `def __init__(self, name: str, filename: str, destination: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def data_logging_file_type(self) -> FileType`

Gets or sets the file type of an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" />. Log files can be TDMS or NCL files.

#### `def data_logging_file_type(self, value: FileType)`

Gets or sets the file type of an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" />. Log files can be TDMS or NCL files.

#### `def tdms_group_name(self) -> str`

Gets or sets the name of the group in the TDMS file to log data to.

#### `def tdms_group_name(self, value: str)`

Gets or sets the name of the group in the TDMS file to log data to.

#### `def tdms_channel_name(self) -> str`

Gets or sets the name of the channel in the TDMS file to log data to.

#### `def tdms_channel_name(self, value: str)`

Gets or sets the name of the channel in the TDMS file to log data to.

#### `def limit_type(self) -> FileLimitationType`

Gets or sets the criteria to use to stop logging data to the current file. When the limit you specify occurs, NI VeriStand either stops logging completely or continues logging in a new file, depending on the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.Operation" crefType="Unqualified" />.

#### `def limit_type(self, value: FileLimitationType)`

Gets or sets the criteria to use to stop logging data to the current file. When the limit you specify occurs, NI VeriStand either stops logging completely or continues logging in a new file, depending on the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.Operation" crefType="Unqualified" />.

#### `def trigger_type(self) -> DataLoggingTriggerType`

Gets or sets the type of trigger to use to start or stop data logging.

#### `def trigger_type(self, value: DataLoggingTriggerType)`

Gets or sets the type of trigger to use to start or stop data logging.

#### `def filter(self) -> DataLoggingFilterType`

Gets or sets whether and how to filter the logged frames.

#### `def filter(self, value: DataLoggingFilterType)`

Gets or sets whether and how to filter the logged frames.

#### `def operation(self) -> DataLoggingOperationType`

Gets or sets the action to take when a trigger condition is met.

#### `def operation(self, value: DataLoggingOperationType)`

Gets or sets the action to take when a trigger condition is met.

#### `def buffer_time(self) -> float`

Gets or sets the buffer time of the log file in seconds. Frames read will be added to the buffer until the specified amount of time has elapsed, at which point all buffered data will be written to the file.  If the buffer is partially full when a file is finished, the remaining data in the buffer will be written to the file.  If the buffer time is set to 0, data will be immediately written to the file when read.

#### `def buffer_time(self, value: float)`

Gets or sets the buffer time of the log file in seconds. Frames read will be added to the buffer until the specified amount of time has elapsed, at which point all buffered data will be written to the file.  If the buffer is partially full when a file is finished, the remaining data in the buffer will be written to the file.  If the buffer time is set to 0, data will be immediately written to the file when read.

#### `def destination(self) -> str`

Gets or sets the destination for a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" /> on disk.

#### `def destination(self, value: str)`

Gets or sets the destination for a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" /> on disk.

#### `def filename(self) -> str`

Gets or sets the filename of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" />.

#### `def filename(self, value: str)`

Gets or sets the filename of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile" crefType="Unqualified" />.

#### `def retriggerable(self) -> bool`

Gets or sets whether logging can be retriggered after a stop. If <see langword="true" />, logging begins again when the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.TriggerChannel" crefType="Unqualified" /> reaches the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.TriggerType" crefType="Unqualified" />.

#### `def retriggerable(self, value: bool)`

Gets or sets whether logging can be retriggered after a stop. If <see langword="true" />, logging begins again when the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.TriggerChannel" crefType="Unqualified" /> reaches the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.TriggerType" crefType="Unqualified" />.

#### `def limit_value(self) -> int`

Gets or sets the value used to determine when to stop logging data to the current log file. This property can represent a size in kilobytes or a time in seconds, depending on the file's <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.LimitType" crefType="Unqualified" />.

#### `def limit_value(self, value: int)`

Gets or sets the value used to determine when to stop logging data to the current log file. This property can represent a size in kilobytes or a time in seconds, depending on the file's <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.LimitType" crefType="Unqualified" />.

#### `def number_of_bytes_to_read(self) -> int`

Gets or sets the maximum number of raw bytes to read. This number does not represent the number of frames to read. CAN and LIN frames are always 24 bytes long. FlexRay frames vary in length.

#### `def number_of_bytes_to_read(self, value: int)`

Gets or sets the maximum number of raw bytes to read. This number does not represent the number of frames to read. CAN and LIN frames are always 24 bytes long. FlexRay frames vary in length.

#### `def trigger_channel(self) -> BaseNode`

The channel to watch for the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.TriggerType" crefType="Unqualified" />.

#### `def trigger_channel(self, value: BaseNode)`

The channel to watch for the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.TriggerType" crefType="Unqualified" />.

#### `def frame_i_ds(self) -> Sequence[str]`

Gets or sets the frame IDs in the XNET database cluster to either include in or exclude from data logging. Use this property when you configure a <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.Filter" crefType="Unqualified" /> for the data logging file.

#### `def frame_i_ds(self, value: Sequence[str])`

Gets or sets the frame IDs in the XNET database cluster to either include in or exclude from data logging. Use this property when you configure a <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.DataLoggingFile.Filter" crefType="Unqualified" /> for the data logging file.

#### `def get_data_file_error(self) -> DataFileError`

#### `def get_data_file_error(self, *args)`

#### `def get_data_file_status(self) -> DataFileStatus`

#### `def get_data_file_status(self, *args)`

### `class DataReplay(Section)`

Represents the <format type="bold">Data Replay</format> section under an NI-XNET CAN port, which contains any <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataFileReplay" crefType="Unqualified" /> files you want to replay onto the CAN bus.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_data_file_replay_list(self) -> Sequence[DataFileReplay]`

#### `def get_data_file_replay_list(self, *args)`

#### `def add_data_file_replay(self, data_file_replay: DataFileReplay) -> bool`

#### `def add_data_file_replay(self, *args)`

### `class DataSharing(Section)`

Represents the <format type="bold">Data Sharing</format> section under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Chassis" crefType="Unqualified" />. This section contains any reflective memory devices you add to the system definition.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_reflective_memory(self) -> ReflectiveMemory`

#### `def get_reflective_memory(self, *args)`

#### `def add_reflective_memory(self, name: str) -> bool`

#### `def add_reflective_memory(self, *args)`

### `class DataSharingNetwork(Section)`

Represents the <format type="bold">Data Sharing Network</format> section of the system definition, under which you can add and configure a reflective memory network. You can only configure one reflective memory network per system definition.

#### `def __init__(self, *args)`

Create a new instance.

#### `def dynamic_data_size(self) -> int`

Gets or sets the number of channels in reflective memory to reserve for dynamically mapping channel data at run-time. For example, in a distributed system, if target A needs to access data provided by a channel on target B at run-time, the targets require a channel in reflective memory that target B can copy data to and target A can read data from.

#### `def dynamic_data_size(self, value: int)`

Gets or sets the number of channels in reflective memory to reserve for dynamically mapping channel data at run-time. For example, in a distributed system, if target A needs to access data provided by a channel on target B at run-time, the targets require a channel in reflective memory that target B can copy data to and target A can read data from.

#### `def get_reflective_memory_network(self) -> ReflectiveMemoryNetwork`

#### `def get_reflective_memory_network(self, *args)`

#### `def add_reflective_memory_network(self, name: str) -> bool`

#### `def add_reflective_memory_network(self, *args)`

### `class Database(Section)`

Represents an XNET database. XNET databases can be CANdb (<format type="monospace">.dbc</format>), NI-CAN (<format type="monospace">.ncd</format>), LDF (<format type="monospace">.ldf</format>), or FIBEX (<format type="monospace">.xml</format>) files.

#### `def __init__(self, name: str, md5: str)`

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def md5(self) -> Sequence[int]`

Gets the MD5 message-digest for the database as a byte array.

### `class Dwell(Command)`

Represents a <format type="bold">Dwell</format> step that you add to a procedure. The <format type="bold">Dwell</format> step suspends the procedure by the amount of time you specify.

#### `def __init__(self, name: str, description: str, dwell_time: float)`

#### `def __init__(self, name: str, description: str, dwell_time: BaseNode)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def dwell_time_constant(self) -> float`

Gets the constant value that determines the amount of time to suspend the procedure.

#### `def dwell_time_channel(self) -> BaseNode`

Gets the channel whose value determines the amount of time to suspend the procedure.

#### `def dwell_time_is_constant(self) -> int`

Gets whether the amount of time to suspend the procedure is determined by a constant value or by a channel value.

#### `def set_dwell_time(self, dwell_time: float)`

#### `def set_dwell_time(self, dwell_time: BaseNode)`

#### `def set_dwell_time(self, *args)`

### `class DynamicSignal(Channel, IChannel)`

Represents a dynamic signal contained in a multiplexed frame. NI VeriStand organizes dynamic signals under <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Mode" crefType="Unqualified" /> nodes.

#### `def __init__(self, *args)`

Create a new instance.

#### `def md5(self) -> Sequence[int]`

Gets the MD5 message-digest for the signal.

### `class End(Command)`

Represents an <format type="bold">End</format> step that you can add to a procedure. The <format type="bold">End</format> step stops the procedure.

#### `def __init__(self, name: str, description: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class EventTriggered(Section)`

Represents the <format type="bold">Event Triggered</format> section under an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Outgoing" crefType="Unqualified" /> section of an NI-XNET CAN or FlexRay port.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_signal_based_frame_list(self) -> Sequence[SignalBasedFrame]`

#### `def get_signal_based_frame_list(self, *args)`

#### `def get_raw_data_based_frame_list(self) -> Sequence[RawDataBasedFrame]`

#### `def get_raw_data_based_frame_list(self, *args)`

#### `def add_signal_based_frame(self, signal_based_frame: SignalBasedFrame) -> bool`

#### `def add_signal_based_frame(self, *args)`

#### `def add_raw_data_based_frame(self, raw_data_based_frame: RawDataBasedFrame) -> bool`

#### `def add_raw_data_based_frame(self, *args)`

### `class Execution(Section)`

Represents the <format type="bold">Execution</format> section under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Model" crefType="Unqualified" />. This section contains channels that get and set execution details of the model, such as its current status and the amount of time that has elapsed since it began executing.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_model_command(self) -> ModelCommand`

#### `def get_model_command(self, *args)`

#### `def get_model_status(self) -> ModelStatus`

#### `def get_model_status(self, *args)`

#### `def get_model_time(self) -> ModelTime`

#### `def get_model_time(self, *args)`

### `class ExecutionOrder(Section)`

Represents the <format type="bold">Execution Order</format> section under <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels" crefType="Unqualified" />, which contains information about the order that your models execute relative to each other in the VeriStand Engine.

#### `def __init__(self, *args)`

Create a new instance.

### `class ExitSubroutine(Command)`

Represents an <format type="bold">Exit Subroutine</format> step that you can add to a procedure. The <format type="bold">Exit Subroutine</format> step is typically used in procedures that are called from other procedures by a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CallProcedure" crefType="Unqualified" /> step. The <format type="bold">Exit Subroutine</format> step stops the current procedure and returns to the calling procedure.

#### `def __init__(self, name: str, description: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class FPGA(Section)`

Represents the <format type="bold">FPGA</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Chassis" crefType="Unqualified" /> in the system definition. This section contains all the FPGA devices you add under the chassis.

#### `def __init__(self, *args)`

Create a new instance.

#### `def add_fpga_device(self, fpga_config_file: str) -> FPGADevice`

#### `def add_fpga_device(self) -> FPGADevice`

#### `def add_fpga_device(self, *args)`

#### `def get_fpga_device_list(self) -> Sequence[FPGADevice]`

#### `def get_fpga_device_list(self, *args)`

### `class FPGACategory(Section)`

Represents a section under an FPGA device. Sections organize channels according to type. For example, <format type="bold">Input<entity value="raquo" />Analog</format>, <format type="bold">Output<entity value="raquo" />Digital</format>, and so on.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_category_list(self) -> Sequence[FPGACategory]`

#### `def get_category_list(self, *args)`

#### `def get_channel_list(self) -> Sequence[FPGAChannel]`

#### `def get_channel_list(self, *args)`

### `class FPGAChannel(Channel, IChannel)`

Represents a channel of an FPGA device.

#### `def __init__(self, *args)`

Create a new instance.

#### `def initial_value(self) -> float`

Gets or sets the initial value of the FPGA channel.

#### `def initial_value(self, value: float)`

Gets or sets the initial value of the FPGA channel.

#### `def channel_bit_offset(self) -> int`

Gets the bit offset of the FPGA channel in the DMA packet.

#### `def fxpiwl(self) -> int`

Gets the integer word length of a fixed-point FPGA channel.

#### `def fxpwl(self) -> int`

Gets the word length of a fixed-point FPGA channel.

#### `def offset(self) -> float`

Gets or sets the offset of the FPGA channel.

#### `def offset(self, value: float)`

Gets or sets the offset of the FPGA channel.

#### `def packet_index(self) -> int`

Gets the index of the packet in the DMA FIFO that defines the channel.

#### `def period_pwm(self) -> int`

Gets or sets the pulse width modulation (PWM) period for an output channel.

#### `def period_pwm(self, value: int)`

Gets or sets the pulse width modulation (PWM) period for an output channel.

#### `def representation(self) -> int`

Gets the data type of the FPGA channel as it is represented in the DMA packet.

#### `def scaling(self) -> float`

Gets or sets the scaling value applied to a channel.

#### `def scaling(self, value: float)`

Gets or sets the scaling value applied to a channel.

### `class FPGADICategory(FPGACategory)`

Represents the <format type="bold">Input<entity value="raquo" />Digital</format> section under an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FPGADevice" crefType="Unqualified" />.

#### `def __init__(self, *args)`

Create a new instance.

### `class FPGADOCategory(FPGACategory)`

Represents the <format type="bold">Output<entity value="raquo" />Digital</format> section under an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FPGADevice" crefType="Unqualified" />.

#### `def __init__(self, *args)`

Create a new instance.

### `class FPGADevice(Section)`

Represents an FPGA target under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FPGA" crefType="Unqualified" /> section.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def read_packets(self) -> int`

Gets the number of DMA read packets.

#### `def write_packets(self) -> int`

Gets the number of DMA write packets.

#### `def fpga_config_file(self) -> DependentFile`

Gets the FPGA configuration file used to define the FPGA target.

#### `def fpga_bitfile(self) -> DependentFile`

Gets the name of the FPGA bitfile used for the FPGA target.

#### `def latest_refresh(self) -> str`

Gets a timestamp indicating the last date and time that the FPGA configuration file, which specifies the content of the DMA FIFOs and how the device appears in System Explorer, was refreshed. Refreshing the configuration file essentially re-creates the device.

#### `def change_rio_address(self, address_number: int) -> bool`

#### `def change_rio_address(self, *args)`

#### `def get_category_list(self) -> Sequence[FPGACategory]`

#### `def get_category_list(self, *args)`

### `class FPGADigitalInput(FPGAChannel, IChannel)`

Represents an FPGA digital input channel.

#### `def __init__(self, *args)`

Create a new instance.

### `class FPGADigitalOutput(FPGAChannel, IChannel)`

Represents an FPGA digital output channel.

#### `def __init__(self, *args)`

Create a new instance.

### `class FPGAPWMInCategory(FPGACategory)`

Represents the <format type="bold">Input<entity value="raquo" />PWM</format> section under an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FPGADevice" crefType="Unqualified" />.

#### `def __init__(self, *args)`

Create a new instance.

### `class FPGAPWMInput(FPGAChannel, IChannel)`

Represents an FPGA PWM input channel.

#### `def __init__(self, *args)`

Create a new instance.

### `class FPGAPWMOutCategory(FPGACategory)`

Represents the <format type="bold">Output<entity value="raquo" />PWM</format> section under an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FPGADevice" crefType="Unqualified" />.

#### `def __init__(self, *args)`

Create a new instance.

### `class FPGAPWMOutput(FPGAChannel, IChannel)`

Represents an FPGA PWM output channel.

#### `def __init__(self, *args)`

Create a new instance.

### `class FinishedFiles(Channel, IChannel)`

Represents a <format type="bold">Finished Files</format> channel associated with an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.RawFrameDataLogging" crefType="Unqualified" /> file. This channel stores the number of completed log files for the current session of the VeriStand Engine. You can use this channel to determine when a file is ready for use by other processes.

#### `def __init__(self, *args)`

Create a new instance.

### `class FlexRay(Section)`

Represents the <format type="bold">FlexRay</format> section under <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNET" crefType="Unqualified" /> in the system definition.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_flex_ray_port_list(self) -> Sequence[FlexRayPort]`

#### `def get_flex_ray_port_list(self, *args)`

#### `def add_flex_ray_port(self, flex_ray_port: FlexRayPort) -> bool`

#### `def add_flex_ray_port(self, *args)`

### `class FlexRayInterfaceChannels(Section)`

Represents the <format type="bold">Interface</format> section under an NI-XNET FlexRay port. This section contains the port-specific channels which provide status information.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_poc_state_channel(self) -> Channel`

#### `def get_poc_state_channel(self, *args)`

#### `def get_clock_correction_failed_channel(self) -> Channel`

#### `def get_clock_correction_failed_channel(self, *args)`

#### `def get_passive_to_active_count_channel(self) -> Channel`

#### `def get_passive_to_active_count_channel(self, *args)`

#### `def get_channel_a_sleep_channel(self) -> Channel`

#### `def get_channel_a_sleep_channel(self, *args)`

#### `def get_channel_b_sleep_channel(self) -> Channel`

#### `def get_channel_b_sleep_channel(self, *args)`

#### `def get_fault_channel(self) -> Channel`

#### `def get_fault_channel(self, *args)`

#### `def get_fault_code_channel(self) -> Channel`

#### `def get_fault_code_channel(self, *args)`

#### `def create_poc_state_channel(self) -> Channel`

#### `def create_poc_state_channel(self, *args)`

#### `def create_clock_correction_failed_channel(self) -> Channel`

#### `def create_clock_correction_failed_channel(self, *args)`

#### `def create_passive_to_active_count_channel(self) -> Channel`

#### `def create_passive_to_active_count_channel(self, *args)`

#### `def create_channel_a_sleep_channel(self) -> Channel`

#### `def create_channel_a_sleep_channel(self, *args)`

#### `def create_channel_b_sleep_channel(self) -> Channel`

#### `def create_channel_b_sleep_channel(self, *args)`

#### `def create_fault_channel(self) -> Channel`

#### `def create_fault_channel(self, *args)`

#### `def create_fault_code_channel(self) -> Channel`

#### `def create_fault_code_channel(self, *args)`

### `class FlexRayPort(Section)`

Represents a port under an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRay" crefType="Unqualified" /> device.

#### `def __init__(self, name: str, port_number: int, linked_database: Database, cluster_name: str, baud_rate: int)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def disabled(self) -> bool`

Gets or sets whether the port is disabled.

#### `def disabled(self, value: bool)`

Gets or sets whether the port is disabled.

#### `def termination(self) -> XNETTermination`

Gets or sets the onboard <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination" crefType="Unqualified" />. This setting applies to both FlexRay communication channels (A and B) on each FlexRay interface.

#### `def termination(self, value: XNETTermination)`

Gets or sets the onboard <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination" crefType="Unqualified" />. This setting applies to both FlexRay communication channels (A and B) on each FlexRay interface.

#### `def input_stream_read_time(self) -> float`

Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read.  After this amount of time has elapsed, any frames available from the hardware will be read.

#### `def input_stream_read_time(self, value: float)`

Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read.  After this amount of time has elapsed, any frames available from the hardware will be read.

#### `def enable_passive_to_active(self) -> int`

Corresponds to the `Interface:FlexRay:Allow Passive to Active` property for the FlexRay port.

#### `def enable_passive_to_active(self, value: int)`

Corresponds to the `Interface:FlexRay:Allow Passive to Active` property for the FlexRay port.

#### `def port_number(self) -> int`

Gets or sets the physical address of the FlexRay port.

#### `def port_number(self, value: int)`

Gets or sets the physical address of the FlexRay port.

#### `def linked_database(self) -> BaseNode`

Gets or sets the XNET database associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRayPort" crefType="Unqualified" />.

#### `def linked_database(self, value: BaseNode)`

Gets or sets the XNET database associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRayPort" crefType="Unqualified" />.

#### `def baud_rate(self) -> int`

Gets or sets the baud rate that all cluster nodes use.

#### `def baud_rate(self, value: int)`

Gets or sets the baud rate that all cluster nodes use.

#### `def cluster_name(self) -> str`

Gets or sets the name of the cluster in <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRayPort.LinkedDatabase" crefType="Unqualified" /> that is associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRayPort" crefType="Unqualified" />.

#### `def cluster_name(self, value: str)`

Gets or sets the name of the cluster in <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRayPort.LinkedDatabase" crefType="Unqualified" /> that is associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRayPort" crefType="Unqualified" />.

#### `def enable_cold_start(self) -> bool`

Gets or sets whether the FlexRay interface operates as a cold-start node on the cluster.

#### `def enable_cold_start(self, value: bool)`

Gets or sets whether the FlexRay interface operates as a cold-start node on the cluster.

#### `def key_slot(self) -> int`

Gets or sets the FlexRay slot number from which the XNET FlexRay interface transmits a startup frame during the process of integration with other cluster nodes.

#### `def key_slot(self, value: int)`

Gets or sets the FlexRay slot number from which the XNET FlexRay interface transmits a startup frame during the process of integration with other cluster nodes.

#### `def incoming_rate(self) -> int`

Gets or sets the processing rate for incoming frames in hertz.

#### `def incoming_rate(self, value: int)`

Gets or sets the processing rate for incoming frames in hertz.

#### `def outgoing_rate(self) -> int`

Gets or sets the processing rate for outgoing frames in hertz.

#### `def outgoing_rate(self, value: int)`

Gets or sets the processing rate for outgoing frames in hertz.

#### `def echo(self) -> bool`

Gets or sets whether sessions contain frames that the interface transmits. If <see langword="true" />, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session.

#### `def echo(self, value: bool)`

Gets or sets whether sessions contain frames that the interface transmits. If <see langword="true" />, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session.

#### `def input_stream_queue_size(self) -> int`

Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored.

#### `def input_stream_queue_size(self, value: int)`

Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored.

#### `def inline_incoming(self) -> bool`

Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL.

#### `def inline_incoming(self, value: bool)`

Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL.

#### `def inline_outgoing(self) -> bool`

Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL.

#### `def inline_outgoing(self, value: bool)`

Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL.

#### `def get_interface_section(self) -> FlexRayInterfaceChannels`

#### `def get_interface_section(self, *args)`

#### `def create_interface_section(self) -> FlexRayInterfaceChannels`

#### `def create_interface_section(self, *args)`

#### `def get_incoming(self) -> Incoming`

#### `def get_incoming(self, *args)`

#### `def get_outgoing(self) -> Outgoing`

#### `def get_outgoing(self, *args)`

### `class FrameFaulting(Section)`

Represents a <format type="bold">Frame Faulting</format> section under an outgoing cyclic frame of an NI-XNET CAN port. This section contains channels you can use to configure the transmission of cyclic frames.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_skip_cyclic_frames(self) -> SkipCyclicFrames`

#### `def get_skip_cyclic_frames(self, *args)`

#### `def get_transmit_time(self) -> TransmitTime`

#### `def get_transmit_time(self, *args)`

### `class FrameID(Channel, IChannel)`

Represents a <format type="bold">Frame ID</format> channel under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FrameInformation" crefType="Unqualified" /> section of an incoming, raw data format NI-XNET frame. This channel contains the ID number that identifies the frame.

#### `def __init__(self, *args)`

Create a new instance.

#### `def id(self) -> int`

Gets the ID number of the current incoming frame.

### `class FrameInformation(Section)`

Represents a <format type="bold">Frame Information</format> section under an incoming NI-XNET frame. This section contains channels that store information about the frame, such as the timestamp at which it was received and the ID number of the current frame.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_receive_time(self) -> ReceiveTime`

#### `def get_receive_time(self, *args)`

#### `def get_time_difference(self) -> TimeDifference`

#### `def get_time_difference(self, *args)`

#### `def get_frame_id(self) -> FrameID`

#### `def get_frame_id(self, *args)`

### `class Generator(Section)`

Represents a stimulus generator in the Legacy Stimulus Profile Editor, which produces simulated real-world signals that stimulus profiles use to perform tests on a system.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_stimulus_channel_list(self) -> Sequence[StimulusChannel]`

#### `def get_stimulus_channel_list(self, *args)`

### `class GotoLabel(Command)`

Represents a <format type="bold">Goto Label</format> step that you can add to a procedure. When this step executes, the procedure jumps to the step specified by <see cref="M:NationalInstruments.VeriStand.SystemDefinitionAPI.GotoLabel.Label" crefType="Unqualified" />.

#### `def __init__(self, name: str, description: str, label: BaseNode)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def label(self) -> BaseNode`

Gets or sets the procedure step to execute when the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.GotoLabel" crefType="Unqualified" /> step is executed.

#### `def label(self, value: BaseNode)`

Gets or sets the procedure step to execute when the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.GotoLabel" crefType="Unqualified" /> step is executed.

### `class Hardware(Section)`

Represents the <format type="bold">Hardware</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Target" crefType="Unqualified" />, which contains any chassis you add.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_chassis_list(self) -> Sequence[Chassis]`

#### `def get_chassis_list(self, *args)`

#### `def get_slsc(self) -> SLSC`

#### `def get_slsc(self, *args)`

#### `def add_chassis(self, chassis: Chassis) -> bool`

#### `def add_chassis(self, *args)`

#### `def add_new_chassis(self, name: str) -> Chassis`

#### `def add_new_chassis(self, *args)`

### `class Incoming(Section)`

Represent the <format type="bold">Incoming</format> section under an NI-XNET CAN, LIN, or FlexRay ports, which contains any incoming frames and data logging files .

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_single_point(self) -> SinglePoint`

#### `def get_single_point(self, *args)`

#### `def get_raw_frame_data_logging(self) -> RawFrameDataLogging`

#### `def get_raw_frame_data_logging(self, *args)`

### `class Inport(Channel, IChannel)`

Represents a model inport, or input.

#### `def __init__(self, *args)`

Create a new instance.

#### `def initial_value(self) -> Union[System.Array[System.Double], Sequence[Sequence[float]]]`

Gets or sets the initial value of the model inport.

#### `def initial_value(self, value: Union[System.Array[System.Double], Sequence[Sequence[float]]])`

Gets or sets the initial value of the model inport.

#### `def index(self) -> int`

Gets the index of the inport in the inport vector (array).

### `class Inports(Section)`

Represents the top-level <format type="bold">Inports</format> section under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Model" crefType="Unqualified" />. This section contains all the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Inport" crefType="Unqualified" /> and <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.InportGroup" crefType="Unqualified" /> objects for the model.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_inports(self) -> Sequence[Inport]`

#### `def get_inports(self, deep: bool) -> Sequence[Inport]`

#### `def get_inports(self, *args)`

#### `def get_inport_groups(self) -> Sequence[InportGroup]`

#### `def get_inport_groups(self, *args)`

### `class InputOverflowChannel(CustomDeviceChannel, IChannel)`

Represents an input overflow count channel, which tracks the number of times the system fails to write data to an asynchronous custom device because the FIFO is full. A single custom device can have only one input overflow count channel.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class LIN(Section)`

Represents the <format type="bold">LIN</format> section under <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNET" crefType="Unqualified" /> in the system definition.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_lin_port_list(self) -> Sequence[LINPort]`

#### `def get_lin_port_list(self, *args)`

#### `def add_lin_port(self, lin_port: LINPort) -> bool`

#### `def add_lin_port(self, *args)`

### `class LINInterfaceChannels(Section)`

Represents the <format type="bold">Interface</format> section under an NI-XNET LIN port. This section contains the port-specific channels which provide status information.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_communication_state_channel(self) -> Channel`

#### `def get_communication_state_channel(self, *args)`

#### `def get_fault_channel(self) -> Channel`

#### `def get_fault_channel(self, *args)`

#### `def get_fault_code_channel(self) -> Channel`

#### `def get_fault_code_channel(self, *args)`

#### `def get_last_error_channel(self) -> Channel`

#### `def get_last_error_channel(self, *args)`

#### `def get_last_error_expected_channel(self) -> Channel`

#### `def get_last_error_expected_channel(self, *args)`

#### `def get_last_error_identifier_channel(self) -> Channel`

#### `def get_last_error_identifier_channel(self, *args)`

#### `def get_last_error_received_channel(self) -> Channel`

#### `def get_last_error_received_channel(self, *args)`

#### `def get_last_error_timestamp_channel(self) -> Channel`

#### `def get_last_error_timestamp_channel(self, *args)`

#### `def get_sleep_channel(self) -> Channel`

#### `def get_sleep_channel(self, *args)`

#### `def get_transceiver_ready_channel(self) -> Channel`

#### `def get_transceiver_ready_channel(self, *args)`

#### `def create_communication_state_channel(self) -> Channel`

#### `def create_communication_state_channel(self, *args)`

#### `def create_fault_channel(self) -> Channel`

#### `def create_fault_channel(self, *args)`

#### `def create_fault_code_channel(self) -> Channel`

#### `def create_fault_code_channel(self, *args)`

#### `def create_last_error_channel(self) -> Channel`

#### `def create_last_error_channel(self, *args)`

#### `def create_last_error_expected_channel(self) -> Channel`

#### `def create_last_error_expected_channel(self, *args)`

#### `def create_last_error_identifier_channel(self) -> Channel`

#### `def create_last_error_identifier_channel(self, *args)`

#### `def create_last_error_received_channel(self) -> Channel`

#### `def create_last_error_received_channel(self, *args)`

#### `def create_last_error_timestamp_channel(self) -> Channel`

#### `def create_last_error_timestamp_channel(self, *args)`

#### `def create_sleep_channel(self) -> Channel`

#### `def create_sleep_channel(self, *args)`

#### `def create_transceiver_state_channel(self) -> Channel`

#### `def create_transceiver_state_channel(self, *args)`

### `class LINPort(Section)`

Represents a port under an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.LIN" crefType="Unqualified" /> device.

#### `def __init__(self, name: str, port_number: int, linked_database: Database, cluster_name: str, baud_rate: int, lin_schedules: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def disabled(self) -> bool`

Gets or sets whether the port is disabled.

#### `def disabled(self, value: bool)`

Gets or sets whether the port is disabled.

#### `def termination(self) -> XNETTermination`

Gets or sets the onboard <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination" crefType="Unqualified" />. You can select <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination.Off" crefType="Unqualified" /> (disabled) and <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination.On" crefType="Unqualified" /> (enabled).

#### `def termination(self, value: XNETTermination)`

Gets or sets the onboard <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination" crefType="Unqualified" />. You can select <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination.Off" crefType="Unqualified" /> (disabled) and <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.XNETTermination.On" crefType="Unqualified" /> (enabled).

#### `def input_stream_read_time(self) -> float`

Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read.  After this amount of time has elapsed, any frames available from the hardware will be read.

#### `def input_stream_read_time(self, value: float)`

Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read.  After this amount of time has elapsed, any frames available from the hardware will be read.

#### `def port_number(self) -> int`

Gets or sets the physical address of the LIN port.

#### `def port_number(self, value: int)`

Gets or sets the physical address of the LIN port.

#### `def linked_database(self) -> BaseNode`

Gets or sets the XNET database associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort" crefType="Unqualified" />.

#### `def linked_database(self, value: BaseNode)`

Gets or sets the XNET database associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort" crefType="Unqualified" />.

#### `def baud_rate(self) -> int`

Gets or sets the baud rate that all cluster nodes use.

#### `def baud_rate(self, value: int)`

Gets or sets the baud rate that all cluster nodes use.

#### `def cluster_name(self) -> str`

Gets or sets the name of the cluster in <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort.LinkedDatabase" crefType="Unqualified" /> that is associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort" crefType="Unqualified" />.

#### `def cluster_name(self, value: str)`

Gets or sets the name of the cluster in <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort.LinkedDatabase" crefType="Unqualified" /> that is associated with the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort" crefType="Unqualified" />.

#### `def lin_schedules(self) -> str`

Gets or sets the names of all the available LIN schedules.

#### `def lin_schedules(self, value: str)`

Gets or sets the names of all the available LIN schedules.

#### `def incoming_rate(self) -> int`

Gets or sets the processing rate for outgoing frames in hertz.

#### `def incoming_rate(self, value: int)`

Gets or sets the processing rate for outgoing frames in hertz.

#### `def outgoing_rate(self) -> int`

Gets or sets the processing rate for outgoing frames in hertz.

#### `def outgoing_rate(self, value: int)`

Gets or sets the processing rate for outgoing frames in hertz.

#### `def echo(self) -> bool`

Gets or sets whether sessions contain frames that the interface transmits. If <see langword="true" />, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session.

#### `def echo(self, value: bool)`

Gets or sets whether sessions contain frames that the interface transmits. If <see langword="true" />, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session.

#### `def input_stream_queue_size(self) -> int`

Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored.

#### `def input_stream_queue_size(self, value: int)`

Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored.

#### `def is_master(self) -> bool`

Gets or sets whether the port is the master for the network. A LIN network always consists of one master and several slaves. The master transmits the schedule for frame headers, which are remote requests for specific frame IDs.

#### `def is_master(self, value: bool)`

Gets or sets whether the port is the master for the network. A LIN network always consists of one master and several slaves. The master transmits the schedule for frame headers, which are remote requests for specific frame IDs.

#### `def inline_incoming(self) -> bool`

Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL.

#### `def inline_incoming(self, value: bool)`

Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL.

#### `def inline_outgoing(self) -> bool`

Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL.

#### `def inline_outgoing(self, value: bool)`

Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL.

#### `def get_interface_section(self) -> LINInterfaceChannels`

#### `def get_interface_section(self, *args)`

#### `def create_interface_section(self) -> LINInterfaceChannels`

#### `def create_interface_section(self, *args)`

#### `def get_incoming(self) -> Incoming`

#### `def get_incoming(self, *args)`

#### `def get_outgoing(self) -> Outgoing`

#### `def get_outgoing(self, *args)`

#### `def get_lin_scheduler(self) -> LINScheduler`

#### `def get_lin_scheduler(self, *args)`

### `class LINScheduler(Channel, IChannel)`

Represents the <format type="bold">LIN Scheduler</format> channel under an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort" crefType="Unqualified" />. The LIN Scheduler specifies which schedule to use to determine when to transmit frames. This channel is only valid if the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort" crefType="Unqualified" /> to which is belongs is configured as the master port (<see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.LINPort.IsMaster" crefType="PartiallyQualified" /> is <see langword="true" />).

#### `def __init__(self, *args)`

Create a new instance.

#### `def units(self) -> str`

Gets the units associated with the LIN Scheduler channel.

#### `def active_schedule(self) -> str`

Gets or sets the name of the active LIN schedule.

#### `def active_schedule(self, value: str)`

Gets or sets the name of the active LIN schedule.

#### `def set_active_schedule(self, lin_schedules: Sequence[str], active_schedule_index: int) -> bool`

#### `def set_active_schedule(self, lin_schedules: Sequence[str], active_schedule: str) -> bool`

#### `def set_active_schedule(self, *args)`

### `class Mode(Section)`

Represents a <format type="bold">Mode</format> section under a signal format NI-XNET CAN frame. The <format type="bold">Mode</format> section organizes dynamic (multiplexed) signals according to their mode values.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_dynamic_signal(self) -> DynamicSignal`

#### `def get_dynamic_signal(self, *args)`

#### `def get_all_dynamic_signals(self) -> Sequence[DynamicSignal]`

#### `def get_all_dynamic_signals(self, *args)`

#### `def get_mode_information(self) -> ModeInformation`

#### `def get_mode_information(self, *args)`

#### `def create_mode_information(self) -> ModeInformation`

#### `def create_mode_information(self, *args)`

#### `def add_dynamic_signal(self, signal_name: str, description: str, units: str, default_value: float) -> bool`

#### `def add_dynamic_signal(self, *args)`

### `class ModeInformation(Section)`

Represents a <format type="bold">Mode Information</format> section under an NI-XNET CAN multiplexer mode. This section contains channels that store information about the mode, such as the timestamp at which it was received.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_receive_time(self) -> ModeReceiveTime`

#### `def get_receive_time(self, *args)`

#### `def get_time_difference(self) -> ModeTimeDifference`

#### `def get_time_difference(self, *args)`

### `class ModeReceiveTime(Channel, IChannel)`

Represents the <format type="bold">Mode Receive Time</format> channel for an incoming NI-XNET CAN multiplexer mode. This channel contains the most recent timestamp at which the mode was received.

#### `def __init__(self, *args)`

Create a new instance.

#### `def remove_node(self) -> bool`

#### `def remove_node(self, *args)`

### `class ModeTimeDifference(Channel, IChannel)`

Represents the <format type="bold">Mode Time Difference</format> channel for an incoming NI-XNET CAN multiplexer mode. This channel stores the difference between the two most recent <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ModeReceiveTime" /> timestamps.

#### `def __init__(self, *args)`

Create a new instance.

### `class Model(Section)`

Represents a model, which is a mathematical representation of a real-world system. A model responds to stimuli by producing outputs in a way that emulates the behavior of the modeled item. Models contain inputs and outputs that send and receive data. Models contain parameters you can manipulate and signals whose values you can view. For example, a model that generates a sine wave contains parameters that adjust the amplitude and frequency of the sine wave. You can view the value of the sine wave using the model signal.

#### `def __init__(self, name: str, description: str, model_path: str, processor: int, decimation: int, initial_state: int, segment_vectors: bool, import_parameters: bool, parameter_regular_expression: str, global_parameter_scope: GlobalParameterScopes, import_signals: bool, signal_regular_expression: str, import_only_named_signals: bool, ni_veri_stand_server_port: int)`

#### `def __init__(self, name: str, description: str, model_path: str, processor: int, decimation: int, initial_state: int, segment_vectors: bool, import_parameters: bool, parameter_regular_expression: str, import_signals: bool, signal_regular_expression: str, import_only_named_signals: bool)`

#### `def __init__(self, name: str, description: str, model_path: str, processor: int, decimation: int, initial_state: int, segment_vectors: bool, import_parameters: bool, parameter_regular_expression: str, import_signals: bool, signal_regular_expression: str, import_only_named_signals: bool, ni_veri_stand_server_port: int)`

#### `def __init__(self, name: str, description: str, model_path: str, processor: int, decimation: int, initial_state: int, segment_vectors: bool, import_parameters: bool, import_signals: bool)`

#### `def __init__(self, name: str, description: str, model_path: str, processor: int, decimation: int, initial_state: int, segment_vectors: bool, import_parameters: bool, import_signals: bool, ni_veri_stand_server_port: int)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def automatic_processor_value() -> int`

#### `def load_success(self) -> bool`

Gets whether NI VeriStand loaded the model successfully.

#### `def global_parameter_scope(self) -> GlobalParameterScopes`

Gets or sets whether global parameters in the current model share their values with other models on the same target.

#### `def global_parameter_scope(self, value: GlobalParameterScopes)`

Gets or sets whether global parameters in the current model share their values with other models on the same target.

#### `def model_execution_group(self) -> int`

Gets or sets the model execution group

#### `def model_execution_group(self, value: int)`

Gets or sets the model execution group

#### `def model_descriptor(self) -> IModelDescriptor`

Gets the model descriptor

#### `def base_rate(self) -> float`

Gets the base rate of the model in microseconds.

#### `def dll_size(self) -> int`

Gets the size, in bytes, of the compiled version of the model (<format type="monospace">.dll</format> file).

#### `def dll_timestamp(self) -> float`

Gets the time at which the model DLL was compiled.

#### `def model_bitness(self) -> int`

Gets the bitness of the compiled model (32- or 64-bit).

#### `def decimation(self) -> int`

Gets or sets the decimation applied to the Primary Control Loop rate to determine the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Model.BaseRate" crefType="Unqualified" /> of the model.

#### `def decimation(self, value: int)`

Gets or sets the decimation applied to the Primary Control Loop rate to determine the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Model.BaseRate" crefType="Unqualified" /> of the model.

#### `def model_timestamp(self) -> float`

Gets the time at which the model was last saved.

#### `def processor(self) -> int`

Gets or sets the processor on which the Model Execution Loop executes. -2 (AutomaticProcessorValue) automatically assigns the processor to <entity value="quot" />any available<entity value="quot" />.

#### `def processor(self, value: int)`

Gets or sets the processor on which the Model Execution Loop executes. -2 (AutomaticProcessorValue) automatically assigns the processor to <entity value="quot" />any available<entity value="quot" />.

#### `def show_unnamed_signals(self) -> bool`

Gets whether signals without names are visible.

#### `def user_rate(self) -> float`

<para>THIS PROPERTY IS OBSOLETE in NI VeriStand 2011 SP1 and later. Use <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Model.BaseRate" crefType="Unqualified" /> instead.</para>
            Gets the user rate of the model.

#### `def segment_vectors(self) -> bool`

Gets information about whether or not vector inputs, outputs, parameters, and signals were split up into scalar channels when the model was loaded.

#### `def md5(self) -> str`

Gets the MD5 message-digest for the model.

#### `def ni_veri_stand_server_port(self) -> int`

Gets or sets the network port that the model uses for communication via TCP. This property only applies to uncompiled models from The MathWorks, Inc. Simulink<entity value="reg" /> software. DLLs and <format type="monospace">.lvmodel</format> files do not require a network port.

#### `def ni_veri_stand_server_port(self, value: int)`

Gets or sets the network port that the model uses for communication via TCP. This property only applies to uncompiled models from The MathWorks, Inc. Simulink<entity value="reg" /> software. DLLs and <format type="monospace">.lvmodel</format> files do not require a network port.

#### `def dll_path(self) -> DependentFile`

Gets a reference to the compiled version of the model (<format type="monospace">.dll</format> file).

#### `def model_path(self) -> DependentFile`

Gets a reference to the uncompiled model file.

#### `def file_version(self) -> str`

Gets the model version

#### `def model_generation_toolchain_version(self) -> str`

Version of the tool that was used to generate the model

#### `def model_author(self) -> str`

Author of the model

#### `def target_platforms(self) -> Sequence[str]`

Target platforms supported by the model

#### `def product_name(self) -> str`

Gets the product name

#### `def internal_name(self) -> str`

Gets the internal name

#### `def company_name(self) -> str`

Gets the company name

#### `def legal_copyright(self) -> str`

Gets the legal copyright

#### `def file_description(self) -> str`

Gets the file description

#### `def get_section_with_all_parameters(self) -> ModelParameters`

#### `def get_section_with_all_parameters(self, *args)`

#### `def get_section_with_all_signals(self) -> ModelSignals`

#### `def get_section_with_all_signals(self, *args)`

#### `def reload_model_from_path(self, new_path: str, segment_vectors: bool) -> Sequence[str]`

#### `def reload_model_from_path(self, new_path: str) -> Sequence[str]`

#### `def reload_model_from_path(self, *args)`

#### `def rename_node(self, new_name: str) -> bool`

#### `def rename_node(self, *args)`

#### `def get_model_details(self) -> System.Collections.Generic.Dictionary[System.String, System.String]`

#### `def get_model_details(self, *args)`

#### `def import_parameters(self, parameters: Iterable[ModelParameter]) -> bool`

#### `def import_parameters(self, *args)`

#### `def import_signals(self, signals: Iterable[ModelSignal]) -> bool`

#### `def import_signals(self, *args)`

#### `def remove_parameters(self, parameters: Iterable[ModelParameter])`

#### `def remove_parameters(self, *args)`

#### `def remove_signals(self, signals: Iterable[ModelSignal])`

#### `def remove_signals(self, *args)`

#### `def get_execution_section(self) -> Execution`

#### `def get_execution_section(self, *args)`

#### `def get_inports_section(self) -> Inports`

#### `def get_inports_section(self, *args)`

#### `def get_outports_section(self) -> Outports`

#### `def get_outports_section(self, *args)`

#### `def get_parameters_section(self) -> ModelParameters`

#### `def get_parameters_section(self, *args)`

#### `def get_signals_section(self) -> ModelSignals`

#### `def get_signals_section(self, *args)`

### `class ModelCommand(Channel, IChannel)`

Represents a <format type="bold">Model Command</format> channel, which you can use to send commands to the model running on the target.

#### `def __init__(self, *args)`

Create a new instance.

#### `def initial_state(self) -> ModelCommandState`

Gets or sets the initial execution state of the model.

#### `def initial_state(self, value: ModelCommandState)`

Gets or sets the initial execution state of the model.

### `class ModelDefaultGroup(Section)`

Represents a parent class for the different types of sub-folders and sections a model can have.

#### `def __init__(self, *args)`

Create a new instance.

### `class ModelParameter(Channel, IChannel)`

Represents a model parameter.

#### `def __init__(self, parameter: ModelParamType, expression: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def model_path(self) -> str`

Gets the symbolic path to the parameter within the model.

#### `def expression(self) -> str`

Gets the expression of the model parameter.

#### `def index(self) -> int`

Gets the index of the model parameter.

### `class ModelParameterGroup(ModelDefaultGroup)`

Represents a sub-section of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ModelParameters" crefType="Unqualified" /> section of a model. Parameter groups provide organization within the model.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_model_parameter_groups(self) -> Sequence[ModelParameterGroup]`

#### `def get_model_parameter_groups(self, *args)`

#### `def get_parameters(self) -> Sequence[ModelParameter]`

#### `def get_parameters(self, deep: bool) -> Sequence[ModelParameter]`

#### `def get_parameters(self, *args)`

#### `def add_model_parameter_group(self, model_parameter_group: ModelParameterGroup) -> bool`

#### `def add_model_parameter_group(self, *args)`

#### `def add_model_parameter(self, model_parameter: ModelParameter) -> bool`

#### `def add_model_parameter(self, *args)`

#### `def add_model_parameters(self, model_parameters: Sequence[ModelParameter]) -> bool`

#### `def add_model_parameters(self, *args)`

### `class ModelParameters(Section)`

Represents the top-level <format type="bold">Parameters</format> section under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Model" crefType="Unqualified" />. This section contains all the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ModelParameter" crefType="Unqualified" /> and <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ModelParameterGroup" crefType="Unqualified" /> objects under the model.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_parameters(self) -> Sequence[ModelParameter]`

#### `def get_parameters(self, deep: bool) -> Sequence[ModelParameter]`

#### `def get_parameters(self, *args)`

#### `def get_model_parameter_groups(self) -> Sequence[ModelParameterGroup]`

#### `def get_model_parameter_groups(self, *args)`

#### `def add_parameter(self, parameter: ModelParameter) -> bool`

#### `def add_parameter(self, *args)`

#### `def add_parameters(self, model_parameters: Sequence[ModelParameter]) -> bool`

#### `def add_parameters(self, *args)`

#### `def add_model_parameter_group(self, model_parameter_group: ModelParameterGroup) -> bool`

#### `def add_model_parameter_group(self, *args)`

### `class ModelSignal(Channel, IChannel)`

Represents a model signal.

#### `def __init__(self, signal: ModelSignalType)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def index(self) -> int`

Gets the index of the model signal.

#### `def model_path(self) -> str`

Gets the symbolic path to the parameter within the model.

#### `def path(self) -> str`

Gets the path to the model that contains the signal.

### `class ModelSignalGroup(ModelDefaultGroup)`

Represents a sub-section of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSignals" crefType="Unqualified" /> section of a model. Signal groups provide organization within the model.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_model_signal_groups(self) -> Sequence[ModelSignalGroup]`

#### `def get_model_signal_groups(self, *args)`

#### `def get_signals(self) -> Sequence[ModelSignal]`

#### `def get_signals(self, deep: bool) -> Sequence[ModelSignal]`

#### `def get_signals(self, *args)`

#### `def add_model_signal_group(self, model_signal_group: ModelSignalGroup) -> bool`

#### `def add_model_signal_group(self, *args)`

#### `def add_model_signal(self, model_signal: ModelSignal) -> bool`

#### `def add_model_signal(self, *args)`

### `class ModelSignals(Section)`

Represents the top-level <format type="bold">Signal</format> section under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Model" crefType="Unqualified" />. This section contains all the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSignal" crefType="Unqualified" /> and <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSignalGroup" crefType="Unqualified" /> objects under the model.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_signals(self) -> Sequence[ModelSignal]`

#### `def get_signals(self, deep: bool) -> Sequence[ModelSignal]`

#### `def get_signals(self, *args)`

#### `def get_model_signal_groups(self) -> Sequence[ModelSignalGroup]`

#### `def get_model_signal_groups(self, *args)`

#### `def add_signal(self, signal: ModelSignal) -> bool`

#### `def add_signal(self, *args)`

#### `def add_model_signal_group(self, model_signal_group: ModelSignalGroup) -> bool`

#### `def add_model_signal_group(self, *args)`

### `class ModelStatus(Channel, IChannel)`

Represents a <format type="bold">Model Status</format> channel, which you can use to get information about the current status of the model running on the target.

#### `def __init__(self, *args)`

Create a new instance.

### `class ModelTime(Channel, IChannel)`

Represents a <format type="bold">Model Time</format> channel, which you can use to get information about the current running time, in seconds, of the model running on the target.

#### `def __init__(self, *args)`

Create a new instance.

### `class Models(Section)`

Represents the <format type="bold">Models</format> section under <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SimulationModels" crefType="Unqualified" />. This section contains any compiled or uncompiled models you add to the system definition. NI VeriStand supports importing <format type="monospace">.dll</format>, <format type="monospace">.mdl</format>, and <format type="monospace">.lvmodel</format> file types.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_models(self) -> Sequence[Model]`

#### `def get_models(self, *args)`

#### `def add_model(self, model: Model) -> bool`

#### `def add_model(self, *args)`

### `class Multiplexer(Channel, IChannel)`

Represents a multiplexer signal under an NI-XNET signal format CAN frame. The multiplexer signal defines an area within the frame to contain different <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DynamicSignal" crefType="Unqualified" /> signals.

#### `def __init__(self, *args)`

Create a new instance.

#### `def multiplexer_value(self) -> int`

Gets or sets the value of a multiplexer signal, which defines the dynamic signals to transmit in a given frame.

#### `def multiplexer_value(self, value: int)`

Gets or sets the value of a multiplexer signal, which defines the dynamic signals to transmit in a given frame.

### `class Outgoing(Section)`

Represents the <format type="bold">Outgoing</format> section under an NI-XNET CAN, LIN, or FlexRay port, which contains any outgoing frames and data replay files.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_event_triggered(self) -> EventTriggered`

#### `def get_event_triggered(self, *args)`

#### `def get_cyclic(self) -> Cyclic`

#### `def get_cyclic(self, *args)`

#### `def get_cyclic_event(self) -> CyclicEvent`

#### `def get_cyclic_event(self, *args)`

#### `def get_data_replay(self) -> DataReplay`

#### `def get_data_replay(self, *args)`

#### `def get_sporadic(self) -> Sporadic`

#### `def get_sporadic(self, *args)`

#### `def get_unconditional(self) -> Unconditional`

#### `def get_unconditional(self, *args)`

### `class Outport(Channel, IChannel)`

Represents a model outport, or output.

#### `def __init__(self, *args)`

Create a new instance.

#### `def initial_value(self) -> Union[System.Array[System.Double], Sequence[Sequence[float]]]`

Gets or sets the initial value of the model outport.

#### `def initial_value(self, value: Union[System.Array[System.Double], Sequence[Sequence[float]]])`

Gets or sets the initial value of the model outport.

#### `def index(self) -> int`

Gets the index number of the outport in the outport vector (array).

### `class OutportGroup(ModelDefaultGroup)`

Represents a sub-section of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Outports" crefType="Unqualified" /> section of a model. Outport groups provide organization within the model.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_outport_groups(self) -> Sequence[OutportGroup]`

#### `def get_outport_groups(self, *args)`

#### `def get_outports(self) -> Sequence[Outport]`

#### `def get_outports(self, deep: bool) -> Sequence[Outport]`

#### `def get_outports(self, *args)`

### `class Outports(Section)`

Represents the top-level <format type="bold">Outports</format> section under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Model" crefType="Unqualified" />. This section contains all the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Outport" crefType="Unqualified" /> and <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.OutportGroup" crefType="Unqualified" /> objects for the model.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_outports(self) -> Sequence[Outport]`

#### `def get_outports(self, deep: bool) -> Sequence[Outport]`

#### `def get_outports(self, *args)`

#### `def get_outport_groups(self) -> Sequence[OutportGroup]`

#### `def get_outport_groups(self, *args)`

### `class OutputUnderflowChannel(CustomDeviceChannel, IChannel)`

Represents an output underflow count channel, which tracks the number of times the system fails to read data from an asynchronous custom device because there is no data to read. A single custom device can have only one output underflow count channel.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class PendingFrames(Channel, IChannel)`

Represents a <format type="bold">Pending Frames</format> channel associate with an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataFileReplay" crefType="Unqualified" /> file. This channel stores the number of frames in the outgoing transmission queue of the current NI-XNET streaming session. You can use this channel to determine whether data is replaying as expected.

#### `def __init__(self, *args)`

Create a new instance.

### `class Procedure(Section)`

Represents a procedure, which determines a set of actions that the VeriStand Engine executes. You can configure procedures to run in response to an alarm, when called from another procedure, or on startup.

#### `def __init__(self, name: str, description: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def reorder_command_list(self, commands: Sequence[Command]) -> bool`

#### `def reorder_command_list(self, *args)`

#### `def get_command_list(self) -> Sequence[Command]`

#### `def get_command_list(self, *args)`

#### `def add_command(self, command: Command) -> bool`

#### `def add_command(self, *args)`

#### `def add_new_alarming(self, name: str, description: str, priority: AlarmPriority, default_state: AlarmState, alarm: BaseNode, delay: float, procedure: BaseNode, alarm_channel: BaseNode, upper_limit: float, lower_limit: float) -> bool`

#### `def add_new_alarming(self, name: str, description: str, priority: AlarmPriority, default_state: AlarmState, alarm: BaseNode, delay: float, procedure: BaseNode, alarm_channel: BaseNode, upper_limit: float, lower_limit: BaseNode) -> bool`

#### `def add_new_alarming(self, name: str, description: str, priority: AlarmPriority, default_state: AlarmState, alarm: BaseNode, delay: float, procedure: BaseNode, alarm_channel: BaseNode, upper_limit: BaseNode, lower_limit: float) -> bool`

#### `def add_new_alarming(self, name: str, description: str, priority: AlarmPriority, default_state: AlarmState, alarm: BaseNode, delay: float, procedure: BaseNode, alarm_channel: BaseNode, upper_limit: BaseNode, lower_limit: BaseNode) -> bool`

#### `def add_new_alarming(self, name: str, description: str, function: AlarmingStepFunction, alarm: BaseNode) -> bool`

#### `def add_new_alarming(self, *args)`

#### `def add_new_call_procedure(self, name: str, description: str, procedure: Procedure) -> bool`

#### `def add_new_call_procedure(self, *args)`

#### `def add_new_condition(self, name: str, description: str, variable: BaseNode, comparison: ConditionStepComparison, value: float, goto_label: Command) -> bool`

#### `def add_new_condition(self, name: str, description: str, variable: BaseNode, comparison: ConditionStepComparison, value: BaseNode, goto_label: Command) -> bool`

#### `def add_new_condition(self, *args)`

#### `def add_new_dwell(self, name: str, description: str, dwell_time: float) -> bool`

#### `def add_new_dwell(self, name: str, description: str, dwell_time: BaseNode) -> bool`

#### `def add_new_dwell(self, *args)`

#### `def add_new_end(self, name: str, description: str) -> bool`

#### `def add_new_end(self, *args)`

#### `def add_new_exit_subroutine(self, name: str, description: str) -> bool`

#### `def add_new_exit_subroutine(self, *args)`

#### `def add_new_goto_label(self, name: str, description: str, label: Command) -> bool`

#### `def add_new_goto_label(self, *args)`

#### `def add_new_set_multiple_variables(self, name: str, description: str, channels: Sequence[BaseNode], values: Sequence[float]) -> bool`

#### `def add_new_set_multiple_variables(self, *args)`

#### `def add_new_set_variable(self, name: str, description: str, variable: BaseNode, value: float) -> bool`

#### `def add_new_set_variable(self, name: str, description: str, variable: BaseNode, value: BaseNode) -> bool`

#### `def add_new_set_variable(self, name: str, description: str, variable: BaseNode, function: SetVariableStepFunction, value1: float, value2: float) -> bool`

#### `def add_new_set_variable(self, name: str, description: str, variable: BaseNode, function: SetVariableStepFunction, value1: float, value2: BaseNode) -> bool`

#### `def add_new_set_variable(self, name: str, description: str, variable: BaseNode, function: SetVariableStepFunction, value1: BaseNode, value2: float) -> bool`

#### `def add_new_set_variable(self, name: str, description: str, variable: BaseNode, function: SetVariableStepFunction, value1: BaseNode, value2: BaseNode) -> bool`

#### `def add_new_set_variable(self, *args)`

#### `def add_new_real_time_sequence_command(self, name: str, description: str, sequence_command: GlobalSequenceCommand, wait_for_sequences_to_complete: bool, wait_timeout: float, abort_sequences_on_timeout: bool) -> RealTimeSequenceCommand`

#### `def add_new_real_time_sequence_command(self, name: str, description: str, sequence_command: GlobalSequenceCommand, wait_for_sequences_to_complete: bool, wait_timeout: float, abort_sequences_on_timeout: bool, group_number: int) -> RealTimeSequenceCommand`

#### `def add_new_real_time_sequence_command(self, *args)`

### `class Procedures(Section)`

Represents the <format type="bold">Procedures</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Target" crefType="Unqualified" />, which contains all the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Procedure" crefType="Unqualified" /> objects you configure.

#### `def __init__(self, *args)`

Create a new instance.

#### `def startup_procedure(self) -> Procedure`

Gets or sets a value indicating the procedure that runs on startup.

#### `def startup_procedure(self, value: Procedure)`

Gets or sets a value indicating the procedure that runs on startup.

#### `def reorder_procedure_list(self, procedures: Sequence[Procedure]) -> bool`

#### `def reorder_procedure_list(self, *args)`

#### `def get_procedures_list(self) -> Sequence[Procedure]`

#### `def get_procedures_list(self, *args)`

#### `def add_procedure(self, procedure: Procedure) -> bool`

#### `def add_procedure(self, *args)`

### `class RawDataBasedChannel(Channel, IChannel)`

Represents a raw data format channel under an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame" crefType="Unqualified" />.

#### `def __init__(self, *args)`

Create a new instance.

#### `def default_value(self) -> float`

Gets or sets the default value of the channel.

#### `def default_value(self, value: float)`

Gets or sets the default value of the channel.

#### `def start_bit(self) -> int`

Gets or sets the start bit, or the least significant signal bit position in the frame payload. This value determines the signal starting point in the frame.

#### `def start_bit(self, value: int)`

Gets or sets the start bit, or the least significant signal bit position in the frame payload. This value determines the signal starting point in the frame.

#### `def number_of_bits(self) -> int`

Gets or sets the number of bits the signal uses in the frame payload.

#### `def number_of_bits(self, value: int)`

Gets or sets the number of bits the signal uses in the frame payload.

#### `def enable64_bit(self) -> bool`

Gets or sets whether U64 bitfield representation is enabled for the frame.

#### `def enable64_bit(self, value: bool)`

Gets or sets whether U64 bitfield representation is enabled for the frame.

### `class RawDataBasedFrame(Section)`

Represents a raw data format frame of an NI-XNET CAN, LIN, or FlexRay device.

#### `def __init__(self, name: str, id: int, owning_database: Database, cluster_name: str, payload_length: int, start_time_offset: float, enable64_bit: bool, signal_names: Sequence[str])`

#### `def __init__(self, *args)`

Create a new instance.

#### `def transmit_trigger(self) -> FrameTriggerType`

Gets the trigger type (channel value change, trigger channel not zero, and so on) specified for an event-triggered frame.

#### `def phase(self) -> FramePhaseType`

Gets or sets whether to reset the timer after the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.TransmitTime" crefType="Unqualified" /> elapses when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.EnableSoftwareCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />.

#### `def phase(self, value: FramePhaseType)`

Gets or sets whether to reset the timer after the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.TransmitTime" crefType="Unqualified" /> elapses when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.EnableSoftwareCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />.

#### `def frame_type(self) -> FrameType`

Gets or sets the frame type (CAN data, CAN remote, FlexRay data, or FlexRay null) of a frame under a CAN or FlexRay port.

#### `def frame_type(self, value: FrameType)`

Gets or sets the frame type (CAN data, CAN remote, FlexRay data, or FlexRay null) of a frame under a CAN or FlexRay port.

#### `def id(self) -> int`

Gets or sets the identifier number for the frame. For LIN frames, this is the frame ID. For CAN frames, this is the Arbitration ID. For FlexRay frames, this is the Slot ID in which the frame is sent.

#### `def id(self, value: int)`

Gets or sets the identifier number for the frame. For LIN frames, this is the frame ID. For CAN frames, this is the Arbitration ID. For FlexRay frames, this is the Slot ID in which the frame is sent.

#### `def payload_length(self) -> int`

Gets or sets the number of bytes in the payload of the frame.

#### `def payload_length(self, value: int)`

Gets or sets the number of bytes in the payload of the frame.

#### `def md5(self) -> Sequence[int]`

Gets the MD5 message digest for the frame.

#### `def start_time_offset(self) -> float`

Gets or sets the amount of time that elapses between the session start and the transmission of the first frame.

#### `def start_time_offset(self, value: float)`

Gets or sets the amount of time that elapses between the session start and the transmission of the first frame.

#### `def enable64_bit(self) -> bool`

Gets or sets whether U64 bitfield representation is enabled for the frame.

#### `def enable64_bit(self, value: bool)`

Gets or sets whether U64 bitfield representation is enabled for the frame.

#### `def owning_database(self) -> BaseNode`

Gets or sets a reference to the XNET database that contains the frame.

#### `def owning_database(self, value: BaseNode)`

Gets or sets a reference to the XNET database that contains the frame.

#### `def cluster_name(self) -> str`

Gets or sets the name of the cluster in the XNET database that contains the frame.

#### `def cluster_name(self, value: str)`

Gets or sets the name of the cluster in the XNET database that contains the frame.

#### `def database_alias(self) -> str`

Gets or sets the alias for the XNET database that contains the frame.

#### `def database_alias(self, value: str)`

Gets or sets the alias for the XNET database that contains the frame.

#### `def disabled(self) -> bool`

Gets whether transmission of the outgoing frame is disabled.

#### `def enable_software_cyclic_trigger(self) -> bool`

Gets or sets whether a software cyclic trigger, which transmits outgoing frames at regular intervals specified by <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.TransmitTime" crefType="Unqualified" />, is enabled for the frame.

#### `def enable_software_cyclic_trigger(self, value: bool)`

Gets or sets whether a software cyclic trigger, which transmits outgoing frames at regular intervals specified by <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.TransmitTime" crefType="Unqualified" />, is enabled for the frame.

#### `def enable_frame_cyclic_trigger(self) -> bool`

Gets or sets whether a frame cyclic trigger, which transmits outgoing frames when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.TriggerChannel" crefType="Unqualified" /> has a non-zero value, is enabled for the frame.

#### `def enable_frame_cyclic_trigger(self, value: bool)`

Gets or sets whether a frame cyclic trigger, which transmits outgoing frames when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.TriggerChannel" crefType="Unqualified" /> has a non-zero value, is enabled for the frame.

#### `def disable_channel(self) -> BaseNode`

Gets a reference to the disable channel for the frame. A disable channel disables transmission of an outgoing frame when the value of the disable channel is non-zero.

#### `def trigger_channel(self) -> BaseNode`

Gets a reference to the channel that is checked for a non-zero value when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.EnableFrameCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />.

#### `def transmit_time(self) -> float`

Gets or sets the interval, in seconds, at which a software cyclic trigger transmits outgoing frames when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.EnableSoftwareCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />.

#### `def transmit_time(self, value: float)`

Gets or sets the interval, in seconds, at which a software cyclic trigger transmits outgoing frames when <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.RawDataBasedFrame.EnableSoftwareCyclicTrigger" crefType="Unqualified" /> is <see langword="true" />.

#### `def create_raw_data_based_channel(self, start_bit: int, number_of_bits: int) -> RawDataBasedChannel`

#### `def create_raw_data_based_channel(self, *args)`

#### `def create_frame_information(self, create_time_information_channels: bool, create_frame_id: bool) -> FrameInformation`

#### `def create_frame_information(self, *args)`

#### `def create_frame_faulting(self, create_skip_cyclic_frames: bool, create_transmit_time: bool) -> FrameFaulting`

#### `def create_frame_faulting(self, *args)`

#### `def create_automatic_frame_processing(self) -> AutomaticFrameProcessing`

#### `def create_automatic_frame_processing(self, *args)`

#### `def disable_transmission_trigger(self)`

#### `def disable_transmission_trigger(self, *args)`

#### `def enable_transmission_trigger(self, disable_channel: BaseNode)`

#### `def enable_transmission_trigger(self, *args)`

#### `def set_transmit_trigger(self, trigger_type: FrameTriggerType, trigger_channel: BaseNode)`

#### `def set_transmit_trigger(self, *args)`

#### `def get_raw_data_based_channel_list(self) -> Sequence[RawDataBasedChannel]`

#### `def get_raw_data_based_channel_list(self, *args)`

#### `def get_frame_information(self) -> FrameInformation`

#### `def get_frame_information(self, *args)`

#### `def get_frame_faulting(self) -> FrameFaulting`

#### `def get_frame_faulting(self, *args)`

#### `def get_automatic_frame_processing(self) -> AutomaticFrameProcessing`

#### `def get_automatic_frame_processing(self, *args)`

### `class RawFrameDataLogging(Section)`

Represents the <format type="bold">Raw Frame Data Logging</format> section under an NI-XNET CAN, LIN, or FlexRay port.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_data_logging_file_list(self) -> Sequence[DataLoggingFile]`

#### `def get_data_logging_file_list(self, *args)`

#### `def add_data_logging_file(self, data_logging_file: DataLoggingFile) -> bool`

#### `def add_data_logging_file(self, *args)`

### `class RealTimeSequenceCommand(Command)`

A procedure command for commanding real-time sequences.

#### `def __init__(self, name: str, sequence_command: GlobalSequenceCommand, wait_for_sequences_to_complete: bool, wait_timeout: float, abort_sequences_on_timeout: bool)`

#### `def __init__(self, name: str, sequence_command: GlobalSequenceCommand, wait_for_sequences_to_complete: bool, wait_timeout: float, abort_sequences_on_timeout: bool, group_number: int)`

#### `def __init__(self)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def sequence_command(self) -> GlobalSequenceCommand`

Gets or sets a value indicating the global command to apply to all running real-time sequences.

#### `def sequence_command(self, value: GlobalSequenceCommand)`

Gets or sets a value indicating the global command to apply to all running real-time sequences.

#### `def wait_for_sequences_to_complete(self) -> bool`

Gets or sets a value indicating whether to wait for all active sequences to complete execution.

#### `def wait_for_sequences_to_complete(self, value: bool)`

Gets or sets a value indicating whether to wait for all active sequences to complete execution.

#### `def abort_sequences_on_timeout(self) -> bool`

Gets or sets a value indicating whether to abort all active sequences if the sequence command times out waiting for them to complete.

#### `def abort_sequences_on_timeout(self, value: bool)`

Gets or sets a value indicating whether to abort all active sequences if the sequence command times out waiting for them to complete.

#### `def wait_timeout(self) -> float`

Gets or sets a value indicating the maximum amount of time in seconds to wait for all active sequences to complete execution.

#### `def wait_timeout(self, value: float)`

Gets or sets a value indicating the maximum amount of time in seconds to wait for all active sequences to complete execution.

#### `def group_number(self) -> int`

Gets or sets a value indicating the group number for the sequence to stop.

#### `def group_number(self, value: int)`

Gets or sets a value indicating the group number for the sequence to stop.

### `class ReceiveTime(Channel, IChannel)`

Represents the <format type="bold">Receive Time</format> channel for an incoming NI-XNET CAN, LIN, or FlexRay frame. This channel contains the most recent timestamp at which the frame was received.

#### `def __init__(self, *args)`

Create a new instance.

#### `def initial_value(self) -> float`

Gets or sets the initial value of the <format type="bold">Receive Time</format> channel.

#### `def initial_value(self, value: float)`

Gets or sets the initial value of the <format type="bold">Receive Time</format> channel.

#### `def remove_node(self) -> bool`

#### `def remove_node(self, *args)`

### `class ReflectiveMemory(Section)`

Represents a reflective memory device under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DataSharing" crefType="Unqualified" /> section of the system definition. A reflective memory device is a target on a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryNetwork" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def visa_resource(self) -> str`

Gets or sets the VISA resource name for the device as it appears in Measurement <entity value="amp" /> Automation Explorer (MAX).

#### `def visa_resource(self, value: str)`

Gets or sets the VISA resource name for the device as it appears in Measurement <entity value="amp" /> Automation Explorer (MAX).

#### `def generate_interrupt(self) -> bool`

Gets whether interrupts are enabled for the reflective memory device.

#### `def interrupt_all_nodes(self) -> bool`

Gets whether the device sends interrupt signals to all nodes on the reflective memory network.

#### `def interrupt_target_node(self) -> int`

Gets the decimal ID of the target node to which the reflective memory device sends interrupts.

#### `def interrupt_type(self) -> int`

Gets the type of interrupt the reflective memory device generates.

#### `def interrupt_data_constant(self) -> bool`

Gets whether the data included in the interrupt packet is a constant value.

#### `def interrupt_constant_data(self) -> int`

Gets the constant value that is the data included in the interrupt packet.

#### `def interrupt_channel_data(self) -> BaseNode`

Gets the channel that provides the data included in the interrupt packet.

#### `def disable_interrupt(self)`

#### `def disable_interrupt(self, *args)`

#### `def enable_interrupt(self, type: ReflectiveMemoryInterruptType, interrupt_constant_value: int)`

#### `def enable_interrupt(self, type: ReflectiveMemoryInterruptType, interrupt_channel: BaseNode)`

#### `def enable_interrupt(self, interrupt_target_node: int, type: ReflectiveMemoryInterruptType, interrupt_constant_value: int)`

#### `def enable_interrupt(self, interrupt_target_node: int, type: ReflectiveMemoryInterruptType, interrupt_channel: BaseNode)`

#### `def enable_interrupt(self, *args)`

#### `def get_information_channels(self) -> ReflectiveMemoryInformationChannels`

#### `def get_information_channels(self, *args)`

#### `def get_data_channels(self) -> ReflectiveMemoryDataChannels`

#### `def get_data_channels(self, *args)`

### `class ReflectiveMemoryDataChannel(Channel, IChannel)`

Represents a data channel under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemory" crefType="Unqualified" /> device.

#### `def __init__(self, name: str, description: str, memory_address: int, data_type: ReflectiveMemoryDataChannelDataType, initial_value: float, type: ReflectiveMemoryDataChannelAccessType)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def initial_value(self) -> float`

Gets or sets the initial value of a reflective memory data channel.

#### `def initial_value(self, value: float)`

Gets or sets the initial value of a reflective memory data channel.

#### `def type(self) -> ReflectiveMemoryDataChannelAccessType`

Gets or sets the access type (<format type="monospace">Read</format> or <format type="monospace">Write</format>) of a reflective memory data channel.

#### `def type(self, value: ReflectiveMemoryDataChannelAccessType)`

Gets or sets the access type (<format type="monospace">Read</format> or <format type="monospace">Write</format>) of a reflective memory data channel.

#### `def data_type(self) -> ReflectiveMemoryDataChannelDataType`

Gets or sets the data type of a reflective memory data channel.

#### `def data_type(self, value: ReflectiveMemoryDataChannelDataType)`

Gets or sets the data type of a reflective memory data channel.

#### `def memory_address(self) -> int`

Gets or sets the address for the data channel in reflective memory.

#### `def memory_address(self, value: int)`

Gets or sets the address for the data channel in reflective memory.

### `class ReflectiveMemoryDataChannels(Section)`

Represents the top-level <format type="bold">Data Channels</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemory" crefType="Unqualified" /> device. This section contains all the data channels for the device, as well as sub-folders that you can use to organize the channels.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_data_channels(self) -> Sequence[ReflectiveMemoryDataChannel]`

#### `def get_data_channels(self, *args)`

#### `def get_folders(self) -> Sequence[ReflectiveMemoryFolder]`

#### `def get_folders(self, *args)`

#### `def add_data_channel(self, reflective_memory_data_channel: ReflectiveMemoryDataChannel) -> bool`

#### `def add_data_channel(self, *args)`

#### `def add_folder(self, reflective_memory_folder: ReflectiveMemoryFolder) -> bool`

#### `def add_folder(self, *args)`

### `class ReflectiveMemoryFolder(Section)`

Represents a folder under a reflective memory device. Folders can contain data channels or additional sub-folders.

#### `def __init__(self, name: str, description: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_data_channels(self) -> Sequence[ReflectiveMemoryDataChannel]`

#### `def get_data_channels(self, *args)`

#### `def get_folders(self) -> Sequence[ReflectiveMemoryFolder]`

#### `def get_folders(self, *args)`

#### `def add_data_channel(self, reflective_memory_data_channel: ReflectiveMemoryDataChannel) -> bool`

#### `def add_data_channel(self, *args)`

#### `def add_folder(self, reflective_memory_folder: ReflectiveMemoryFolder) -> bool`

#### `def add_folder(self, *args)`

### `class ReflectiveMemoryInformationChannels(Section)`

Represents the <format type="bold">Information Channels</format> section under a reflective memory device.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_ring_read_late_count(self) -> ReflectiveMemoryRingReadLateCount`

#### `def get_ring_read_late_count(self, *args)`

#### `def get_write_late_count(self) -> ReflectiveMemoryWriteLateCount`

#### `def get_write_late_count(self, *args)`

### `class ReflectiveMemoryNetwork(Section)`

Represents the reflective memory network that <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemory" crefType="Unqualified" /> devices use to share data. A single system definition can have only one reflective memory network.

#### `def __init__(self, *args)`

Create a new instance.

#### `def start_memory_address(self) -> int`

Gets or sets the start address in reflective memory that NI VeriStand can use. Use this property together with <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryNetwork.MaximumEndMemoryAddress" crefType="Unqualified" /> to specify the maximum amount of reflected memory allocated to NI VeriStand.

#### `def start_memory_address(self, value: int)`

Gets or sets the start address in reflective memory that NI VeriStand can use. Use this property together with <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryNetwork.MaximumEndMemoryAddress" crefType="Unqualified" /> to specify the maximum amount of reflected memory allocated to NI VeriStand.

#### `def maximum_end_memory_address(self) -> int`

Gets or sets the maximum end address in reflective memory that NI VeriStand can use. Use this property together with <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryNetwork.StartMemoryAddress" crefType="Unqualified" /> to specify the maximum amount of reflected memory allocated to NI VeriStand.

#### `def maximum_end_memory_address(self, value: int)`

Gets or sets the maximum end address in reflective memory that NI VeriStand can use. Use this property together with <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryNetwork.StartMemoryAddress" crefType="Unqualified" /> to specify the maximum amount of reflected memory allocated to NI VeriStand.

#### `def export_memory_table(self) -> bool`

Gets or sets whether the memory table that NI VeriStand creates at compile time is exported to a text file.

#### `def export_memory_table(self, value: bool)`

Gets or sets whether the memory table that NI VeriStand creates at compile time is exported to a text file.

#### `def export_memory_table_file(self) -> Sequence[int]`

Gets or sets the file path for the text file to export the memory table to at compile time if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryNetwork.ExportMemoryTable" crefType="Unqualified" /> is <see langword="true" />.

#### `def export_memory_table_file(self, value: Sequence[int])`

Gets or sets the file path for the text file to export the memory table to at compile time if <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryNetwork.ExportMemoryTable" crefType="Unqualified" /> is <see langword="true" />.

### `class ReflectiveMemoryRingReadLateCount(Channel, IChannel)`

Represents a <format type="bold">Ring Read Late Count</format> channel of a reflective memory device. This channel increments any time the device is not able to read a section of data from reflective memory because the section was still getting written to by another device. If this channel increments, the section of invalid data was not copied to the local channels.

#### `def __init__(self, *args)`

Create a new instance.

### `class ReflectiveMemoryWriteLateCount(Channel, IChannel)`

Represents a <format type="bold">Node Write Late Count</format> channel of a reflective memory device. This channel increments any time the device is not able to write data to the reflective memory network because a new iteration of the Primary Control Loop started before the write operation was complete. In this situation, the PCL does not write or read any data for the iteration where the write operation failed to complete.

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXIChassis(Section)`

Represents an SCXI chassis under a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDevice" crefType="Unqualified" />.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_scxi_modules(self) -> Sequence[SCXIModule]`

#### `def get_scxi_modules(self, *args)`

#### `def add_scxi_module(self, scxi_module: SCXIModule) -> bool`

#### `def add_scxi_module(self, *args)`

### `class SCXIModule(Section)`

Represents an SCXI module under an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str, type_guid: str, num_internal_channels: int)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def scxi_module_type(self) -> str`

Gets the type of the SCXI module.

#### `def get_analog_inputs(self) -> Sequence[DAQAnalogInput]`

#### `def get_analog_inputs(self, *args)`

#### `def get_analog_outputs(self) -> Sequence[DAQAnalogOutput]`

#### `def get_analog_outputs(self, *args)`

#### `def get_dio_ports(self) -> Sequence[DAQDIOPort]`

#### `def get_dio_ports(self, *args)`

### `class SLSC(Section)`

Represents the <format type="bold">SLSC</format> section of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Hardware" />.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_slsc_chassis_list(self) -> Sequence[SLSCChassis]`

#### `def get_slsc_chassis_list(self, *args)`

#### `def export_configuration(self, filepath: str)`

#### `def export_configuration(self, *args)`

#### `def import_configurations(self, filepath: str)`

#### `def import_configurations(self, *args)`

#### `def add_slsc_chassis(self, slsc_chassis: SLSCChassis)`

#### `def add_slsc_chassis(self, *args)`

### `class SLSCChassis(Section)`

Represents the <format type="bold">SLSCChassis</format> section of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SLSC" />.

#### `def __init__(self, name: str, chassis_type: SLSCChassis.SLSCChassisType)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def chassis_id(self) -> str`

Gets or sets the name or the IP address of the SLSCChassis.

#### `def chassis_id(self, value: str)`

Gets or sets the name or the IP address of the SLSCChassis.

#### `def username(self) -> str`

Gets or sets the username for the SLSCChassis.

#### `def username(self, value: str)`

Gets or sets the username for the SLSCChassis.

#### `def password(self) -> str`

Gets or sets the password for the SLSCChassis.

#### `def password(self, value: str)`

Gets or sets the password for the SLSCChassis.

#### `def chassis_type(self) -> str`

Gets the type of the SLSCChassis.

#### `def chassis_id_type(self) -> SLSCChassis.SLSCChassisIDType`

Gets or sets the mode how the cahssis is defined

#### `def chassis_id_type(self, value: SLSCChassis.SLSCChassisIDType)`

Gets or sets the mode how the cahssis is defined

#### `def export_configuration(self, filepath: str)`

#### `def export_configuration(self, *args)`

#### `def get_chassis_channels_section(self) -> SLSCChassisChannels`

#### `def get_chassis_channels_section(self, *args)`

#### `def get_modules_section(self) -> SLSCModules`

#### `def get_modules_section(self, *args)`

### `class SLSCChassisChannel(Channel, IChannel)`

Represents the <format type="bold">SLSC chassis channel</format> node of a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCChassisChannelSection" />.

#### `def __init__(self, *args)`

Create a new instance.

### `class SLSCChassisChannelSection(Section)`

Represents the <format type="bold">SLSC chassis channel category</format> section of an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCChassis" />.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_slsc_chassis_channel_list(self) -> Sequence[SLSCChassisChannel]`

#### `def get_slsc_chassis_channel_list(self, *args)`

### `class SLSCChassisChannels(Section)`

Represents the <format type="bold">SLSCChassisChannels</format> section of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCChassis" />.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_chassis_channel_sections(self) -> Sequence[SLSCChassisChannelSection]`

#### `def get_chassis_channel_sections(self, *args)`

### `class SLSCModuleCustomDevice(CustomDevice)`

Represents an SLSC module custom device.

#### `def __init__(self, name: str, guid: str, slot_number: int)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def slot_number(self) -> int`

The slot number of the SLSC chassis with which the custom device is associated.

#### `def remove_node(self) -> bool`

#### `def remove_node(self, *args)`

### `class SLSCModules(Section)`

Represents the <format type="bold">SLSCModules</format> section of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SLSCChassis" />.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_module(self, slot_number: int) -> SLSCModuleCustomDevice`

#### `def get_module(self, *args)`

#### `def set_module(self, slot_number: int, custom_device: SLSCModuleCustomDevice) -> bool`

#### `def set_module(self, *args)`

### `class Scale(Section)`

Defines a base class for different types of scales allowed in system definition files. You can create scales to convert from the pre-scaled units measured by a hardware channel to the scaled units associated with a transducer or actuator.

#### `def __init__(self, *args)`

Create a new instance.

#### `def scale_type(self) -> ScaleType`

Gets the scale type.

#### `def scale_unit(self) -> str`

Gets or sets the scale unit. This can be any arbitrary string.

#### `def scale_unit(self, value: str)`

Gets or sets the scale unit. This can be any arbitrary string.

### `class ScaleFolder(Section)`

Represents a folder under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Scales" /> section of the system definition. Folders simply organize scales into logical groups.

#### `def __init__(self, name: str, description: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_scale_list(self) -> Sequence[Scale]`

#### `def get_scale_list(self, deep: bool) -> Sequence[Scale]`

#### `def get_scale_list(self, *args)`

#### `def get_scale_folder_list(self) -> Sequence[ScaleFolder]`

#### `def get_scale_folder_list(self, deep: bool) -> Sequence[ScaleFolder]`

#### `def get_scale_folder_list(self, *args)`

#### `def create_scale(self, name: str, type: ScaleType) -> Scale`

#### `def create_scale(self, *args)`

#### `def add_scale(self, scale: Scale) -> bool`

#### `def add_scale(self, *args)`

#### `def add_scale_folder(self, folder: ScaleFolder) -> bool`

#### `def add_scale_folder(self, *args)`

#### `def add_new_scale_folder(self, name: str, description: str) -> bool`

#### `def add_new_scale_folder(self, *args)`

### `class Scales(Section)`

Represents the <format type="bold">Scales</format> section of the system definition, which contains <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Scale" /> objects. Use scales to convert from the pre-scaled units measured by a hardware channel to the scaled units associated with a transducer or actuator.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_scale_list(self) -> Sequence[Scale]`

#### `def get_scale_list(self, deep: bool) -> Sequence[Scale]`

#### `def get_scale_list(self, *args)`

#### `def get_scale_folder_list(self) -> Sequence[ScaleFolder]`

#### `def get_scale_folder_list(self, deep: bool) -> Sequence[ScaleFolder]`

#### `def get_scale_folder_list(self, *args)`

#### `def create_scale(self, name: str, type: ScaleType) -> Scale`

#### `def create_scale(self, *args)`

#### `def add_scale(self, scale: Scale) -> bool`

#### `def add_scale(self, *args)`

#### `def add_scale_folder(self, folder: ScaleFolder) -> bool`

#### `def add_scale_folder(self, *args)`

#### `def add_new_scale_folder(self, name: str, description: str) -> bool`

#### `def add_new_scale_folder(self, *args)`

### `class SetMultipleVariables(Command)`

Represents a <format type="bold">Set Multiple Variables</format> step that you can add to a procedure. This step sets the values of multiple channels to constant values.

#### `def __init__(self, name: str, description: str, channels: Sequence[BaseNode], values: Sequence[float])`

#### `def __init__(self, *args)`

Create a new instance.

#### `def channels(self) -> Sequence[BaseNode]`

Gets or sets the channels to set to the specified values.

#### `def values(self) -> Sequence[float]`

Gets the values to which this step sets the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetMultipleVariables.Channels" crefType="Unqualified" />.

#### `def set_channels_and_values(self, channels: Sequence[BaseNode], values: Sequence[float])`

#### `def set_channels_and_values(self, *args)`

### `class SetVariable(Command)`

Represents a <format type="bold">Set Variable</format> step that you can add to a procedure.  This step sets a channel, <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Variable" crefType="Unqualified" />, to a certain value. The value can be a constant or the result of a calculation using a <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Function" crefType="Unqualified" /> you specify.

#### `def __init__(self, name: str, description: str, variable: BaseNode, value: float)`

#### `def __init__(self, name: str, description: str, variable: BaseNode, value: BaseNode)`

#### `def __init__(self, name: str, description: str, variable: BaseNode, function: SetVariableStepFunction, value1: float, value2: float)`

#### `def __init__(self, name: str, description: str, variable: BaseNode, function: SetVariableStepFunction, value1: float, value2: BaseNode)`

#### `def __init__(self, name: str, description: str, variable: BaseNode, function: SetVariableStepFunction, value1: BaseNode, value2: float)`

#### `def __init__(self, name: str, description: str, variable: BaseNode, function: SetVariableStepFunction, value1: BaseNode, value2: BaseNode)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def function(self) -> SetVariableStepFunction`

Gets or sets the function (add, subtract, multiply, or divide) to use on the two values that determine the value to set on the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Variable" crefType="Unqualified" /> channel.

#### `def function(self, value: SetVariableStepFunction)`

Gets or sets the function (add, subtract, multiply, or divide) to use on the two values that determine the value to set on the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Variable" crefType="Unqualified" /> channel.

#### `def value1_constant(self) -> float`

Gets the constant value of <format type="italics">Value1</format> in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Function" crefType="Unqualified" /> operation.

#### `def value2_constant(self) -> float`

Gets the constant value of <format type="italics">Value2</format> in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Function" crefType="Unqualified" /> operation.

#### `def value1_is_constant(self) -> bool`

Gets whether the value of <format type="italics">Value1</format> in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Function" crefType="Unqualified" /> operation is specified by a constant or a channel.

#### `def value2_is_constant(self) -> bool`

Gets whether the value of <format type="italics">Value2</format> in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Function" crefType="Unqualified" /> operation is specified by a constant or a channel.

#### `def variable(self) -> BaseNode`

Gets or sets the channel in the system whose value the <format type="bold">Set Variable</format> step sets.

#### `def variable(self, value: BaseNode)`

Gets or sets the channel in the system whose value the <format type="bold">Set Variable</format> step sets.

#### `def value1_channel(self) -> BaseNode`

Gets the channel that determines the value of <format type="italics">Value1</format> in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Function" crefType="Unqualified" /> operation.

#### `def value2_channel(self) -> BaseNode`

Gets the channel that determines the value of <format type="italics">Value2</format> in the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SetVariable.Function" crefType="Unqualified" /> operation.

#### `def set_value1(self, value1: float) -> bool`

#### `def set_value1(self, value1: BaseNode) -> bool`

#### `def set_value1(self, *args)`

#### `def set_value2(self, value2: float) -> bool`

#### `def set_value2(self, value2: BaseNode) -> bool`

#### `def set_value2(self, *args)`

### `class SignalBasedSignal(Channel, IChannel)`

Represents a signal format signal under an NI-XNET <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SignalBasedFrame" crefType="Unqualified" />.

#### `def __init__(self, *args)`

Create a new instance.

#### `def md5(self) -> Sequence[int]`

Gets the MD5 message-digest for the signal.

### `class SkipCyclicFrames(Channel, IChannel)`

Represents the <format type="bold">Skip Cyclic Frames</format> channel under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FrameFaulting" crefType="Unqualified" /> section of an outgoing cyclic frame of an NI-XNET CAN port. This channel specifies to skip transmission of a specified number of cyclic frames across the CAN bus when a specified trigger channel has a non-zero value.

#### `def __init__(self, *args)`

Create a new instance.

#### `def skip_n_cycles(self) -> float`

Gets or sets the number cycles for which to skip transmission of the frame across the bus. For each skipped cycle, a frame value is dequeued and the skip count is decremented. When the skip count decrements to zero, subsequent cyclic transmissions resume.

#### `def skip_n_cycles(self, value: float)`

Gets or sets the number cycles for which to skip transmission of the frame across the bus. For each skipped cycle, a frame value is dequeued and the skip count is decremented. When the skip count decrements to zero, subsequent cyclic transmissions resume.

#### `def trigger_channel(self) -> BaseNode`

Gets or sets the trigger channel to watch for a non-zero value. Skipping frame transmission begins when this channel value becomes non-zero and stops when the skip count specified by <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SkipCyclicFrames.SkipNCycles" crefType="Unqualified" /> decrements to zero.

#### `def trigger_channel(self, value: BaseNode)`

Gets or sets the trigger channel to watch for a non-zero value. Skipping frame transmission begins when this channel value becomes non-zero and stops when the skip count specified by <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.SkipCyclicFrames.SkipNCycles" crefType="Unqualified" /> decrements to zero.

### `class SleepMode(Channel, IChannel)`

Represents a <format type="bold">Transceiver State</format>, or Sleep Mode, channel under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CANInterfaceChannels" crefType="Unqualified" /> section of an NI-XNET CAN port. This channel controls the sleep mode option on the CAN port. A port in sleep mode does not transmit data until you release sleep mode or until the port receives an incoming frame.

#### `def __init__(self, trigger_node: str)`

#### `def __init__(self, name: str, trigger_node: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def trigger_channel(self) -> BaseNode`

Gets or sets the channel that triggers sleep mode on an NI-XNET CAN port. If the value of this channel is non-zero, sleep mode is enabled. If the value is zero, sleep mode is disabled.

#### `def trigger_channel(self, value: BaseNode)`

Gets or sets the channel that triggers sleep mode on an NI-XNET CAN port. If the value of this channel is non-zero, sleep mode is enabled. If the value is zero, sleep mode is disabled.

### `class StimulusChannel(Channel, IChannel)`

Represents a stimulus channel of  a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Generator" crefType="Unqualified" />.

#### `def __init__(self, *args)`

Create a new instance.

#### `def units(self) -> str`

Gets the units associated with the stimulus channel.

### `class SystemChannel(Channel, IChannel)`

Represents a system channel under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SystemChannels" crefType="Unqualified" /> section. System channels monitor the state and condition of various aspects of the system.

#### `def __init__(self, *args)`

Create a new instance.

#### `def units(self) -> str`

Gets the units associated with the channel.

### `class ThermocoupleScale(Scale)`

Represents a thermocouple <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Scale" />, which converts raw values from a thermocouple to Kelvins or degrees Celsius, Fahrenheit, or Rankine.

#### `def __init__(self, name: str)`

#### `def __init__(self, name: str, thermocouple_type: ThermocoupleType, thermocouple_cjc_type: ThermocoupleCJCType, temperature_unit: TemperatureUnit, thermocouple_cjc_source: BaseNode)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def thermocouple_type(self) -> ThermocoupleType`

Gets or sets the type of thermocouple in use.

#### `def thermocouple_type(self, value: ThermocoupleType)`

Gets or sets the type of thermocouple in use.

#### `def thermocouple_cjc_type(self) -> ThermocoupleCJCType`

Gets or sets the type of device the thermocouple uses to perform cold-junction compensation.

#### `def thermocouple_cjc_type(self, value: ThermocoupleCJCType)`

Gets or sets the type of device the thermocouple uses to perform cold-junction compensation.

#### `def temperature_unit(self) -> TemperatureUnit`

Gets or sets the units of the scaled temperature values: Kelvins or degrees Celsius, Fahrenheit, or Rankine.

#### `def temperature_unit(self, value: TemperatureUnit)`

Gets or sets the units of the scaled temperature values: Kelvins or degrees Celsius, Fahrenheit, or Rankine.

#### `def thermocouple_cjc_source(self) -> BaseNode`

Gets or sets the channel that serves as the source of cold-junction compensation for the ThermocoupleScale.

#### `def thermocouple_cjc_source(self, value: BaseNode)`

Gets or sets the channel that serves as the source of cold-junction compensation for the ThermocoupleScale.

### `class TimeDifference(Channel, IChannel)`

Represents the <format type="bold">Time Difference</format> channel for an incoming NI-XNET CAN, LIN, or FlexRay frame. This channel stores the difference between the two most recent <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.ReceiveTime" crefType="Unqualified" /> timestamps.

#### `def __init__(self, *args)`

Create a new instance.

#### `def initial_value(self) -> float`

Gets or sets the initial value of the <format type="bold">Time Difference</format> channel. This property only represents an initial value for the channel, and does not actually enhance or delay frame transmission.

#### `def initial_value(self, value: float)`

Gets or sets the initial value of the <format type="bold">Time Difference</format> channel. This property only represents an initial value for the channel, and does not actually enhance or delay frame transmission.

### `class TimeStepDuration(Channel, IChannel)`

Represents a <format type="bold">Time Step Duration</format> channel, which you can use to get information about the duration, in microseconds, of the last time step of the model running on the target.

#### `def __init__(self, *args)`

Create a new instance.

### `class TimingAndSyncDevice(CustomDevice)`

Represents a timing and sync device, which is a custom device that can drive the RTSI 0 line and synchronize all the hardware I/O devices in the system.

#### `def __init__(self, name: str, guid: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def is_rtsi0_capable(self) -> bool`

Gets or sets whether the timing and sync device is capable of driving the RTSI 0 line, which is a digital line that sends a clock signal that synchronizes all hardware I/O devices in the system.

#### `def is_rtsi0_capable(self, value: bool)`

Gets or sets whether the timing and sync device is capable of driving the RTSI 0 line, which is a digital line that sends a clock signal that synchronizes all hardware I/O devices in the system.

### `class TransmitTime(Channel, IChannel)`

Represents a <format type="bold">Transmit Time</format> under the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FrameFaulting" crefType="Unqualified" /> section of an outgoing cyclic frame of an NI-XNET CAN port. This channel specifies the amount of time that must elapse between subsequent transmissions of the cyclic frame.

#### `def __init__(self, *args)`

Create a new instance.

#### `def transmit_time_value(self) -> float`

Gets or sets the constant value to use as the transmit time, in seconds.

#### `def transmit_time_value(self, value: float)`

Gets or sets the constant value to use as the transmit time, in seconds.

#### `def use_trigger_channel(self) -> bool`

Gets whether the <format type="bold">Transmit Time</format>  channel is using a trigger channel to get the transmit time value.

#### `def trigger_channel(self) -> BaseNode`

Gets a reference to the trigger channel the <format type="bold">Transmit Time</format> channel is using to get its value.

#### `def remove_trigger_channel(self)`

#### `def remove_trigger_channel(self, *args)`

#### `def set_trigger_channel(self, trigger_channel: BaseNode)`

#### `def set_trigger_channel(self, *args)`

### `class UserChannel(Channel, IChannel)`

Represents a user channel, which stores a single value. You can use user channels as variables in procedures, stimulus profiles, and so on.

#### `def __init__(self, name: str, description: str, units: str, default_value: float)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def initial_value(self) -> float`

Gets or sets the initial value of the user channel.

#### `def initial_value(self, value: float)`

Gets or sets the initial value of the user channel.

### `class VirtualECU(Model)`

Represents a virtual ECU as a specialized type of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Model" /> and inherits all the capabilities of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Model" />.
            Virtual ECUs within the same network cluster are automatically connected to each other and to real ECUs via an XNET interface.

#### `def __init__(self, name: str, description: str, virtual_ecu_path: str, processor: int, decimation: int, initial_state: int, segment_vectors: bool, import_parameters: bool, import_signals: bool)`

#### `def __init__(self, name: str, description: str, virtual_ecu_path: str, processor: int, decimation: int, initial_state: int, segment_vectors: bool, import_parameters: bool, parameter_regular_expression: str, import_signals: bool, signal_regular_expression: str, import_only_named_signals: bool)`

#### `def __init__(self, name: str, description: str, virtual_ecu_path: str, processor: int, decimation: int, initial_state: int, segment_vectors: bool, import_parameters: bool, parameter_regular_expression: str, global_parameter_scope: GlobalParameterScopes, import_signals: bool, signal_regular_expression: str, import_only_named_signals: bool)`

#### `def __init__(self, *args)`

Create a new instance.

### `class AlarmStatus(Channel, IChannel)`

A channel that indicates the current status of an alarm

#### `def __init__(self, *args)`

Create a new instance.

### `class Alarming(Command)`

Represents an <format type="bold">Alarm Command</format>, or Alarming, step that you can add to a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Procedure" crefType="Unqualified" />. This step performs the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarming.Function" crefType="Unqualified" /> on the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarming.Alarm" crefType="Unqualified" /> when the step executes.

#### `def __init__(self, name: str, description: str, priority_number: int, default_state: AlarmState, alarm: BaseNode, delay: float, procedure: BaseNode, alarm_source: BaseNode, upper_limit: ValueSource, lower_limit: ValueSource)`

#### `def __init__(self, name: str, description: str, priority: AlarmPriority, default_state: AlarmState, alarm: BaseNode, delay: float, procedure: BaseNode, alarm_channel: BaseNode, upper_limit: float, lower_limit: float)`

#### `def __init__(self, name: str, description: str, priority: AlarmPriority, default_state: AlarmState, alarm: BaseNode, delay: float, procedure: BaseNode, alarm_channel: BaseNode, upper_limit: float, lower_limit: BaseNode)`

#### `def __init__(self, name: str, description: str, priority: AlarmPriority, default_state: AlarmState, alarm: BaseNode, delay: float, procedure: BaseNode, alarm_channel: BaseNode, upper_limit: BaseNode, lower_limit: float)`

#### `def __init__(self, name: str, description: str, priority: AlarmPriority, default_state: AlarmState, alarm: BaseNode, delay: float, procedure: BaseNode, alarm_channel: BaseNode, upper_limit: BaseNode, lower_limit: BaseNode)`

#### `def __init__(self, name: str, description: str, function: AlarmingStepFunction, alarm: BaseNode)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def function(self) -> AlarmingStepFunction`

Gets or sets the function that the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarming" crefType="Unqualified" /> step performs on the alarm.

#### `def function(self, value: AlarmingStepFunction)`

Gets or sets the function that the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarming" crefType="Unqualified" /> step performs on the alarm.

#### `def priority_number(self) -> int`

Gets or sets the priority of an alarm running on the target. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31.

#### `def priority_number(self, value: int)`

Gets or sets the priority of an alarm running on the target. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31.

#### `def priority(self) -> AlarmPriority`

This property is deprecated in NI VeriStand 2011 and later. Use the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> property instead.
            <para>
            Setting this property to <format type="monospace">Low</format>, <format type="monospace">Medium</format>, or <format type="monospace">High</format> automatically sets the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> to 25, 15, or 5, respectively.</para>

#### `def priority(self, value: AlarmPriority)`

This property is deprecated in NI VeriStand 2011 and later. Use the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> property instead.
            <para>
            Setting this property to <format type="monospace">Low</format>, <format type="monospace">Medium</format>, or <format type="monospace">High</format> automatically sets the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.PriorityNumber" crefType="Unqualified" /> to 25, 15, or 5, respectively.</para>

#### `def default_state(self) -> AlarmState`

Gets or sets the default state (<format type="monospace">Disabled</format> or <format type="monospace">Enabled</format>) of the alarm.

#### `def default_state(self, value: AlarmState)`

Gets or sets the default state (<format type="monospace">Disabled</format> or <format type="monospace">Enabled</format>) of the alarm.

#### `def delay(self) -> float`

Gets or sets the amount of time to wait before triggering the alarm.

#### `def delay(self, value: float)`

Gets or sets the amount of time to wait before triggering the alarm.

#### `def upper_limit_constant(self) -> float`

Gets the constant that determines the high limit value of the alarm. If the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.AlarmSource" crefType="Unqualified" /> exceeds this limit, the alarm is triggered.

#### `def lower_limit_constant(self) -> float`

Gets the constant that determines the low limit value of the alarm. If the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.AlarmSource" crefType="Unqualified" /> falls below this limit, the alarm is triggered.

#### `def upper_limit_is_constant(self) -> bool`

Gets information about whether the high limit value of the alarm is determined by a channel or by a constant.

#### `def lower_limit_is_constant(self) -> bool`

Gets information about whether the low limit value of the alarm is determined by a channel or by a constant.

#### `def using_tripped_alarm(self) -> bool`

Gets information about whether the step is using the tripped alarm.

#### `def alarm(self) -> BaseNode`

Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm" crefType="Unqualified" /> on which to perform the step <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarming.Function" crefType="Unqualified" />.

#### `def alarm(self, value: BaseNode)`

Gets or sets the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm" crefType="Unqualified" /> on which to perform the step <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarming.Function" crefType="Unqualified" />.

#### `def alarm_channel(self) -> BaseNode`

Gets or sets the channel to monitor for alarm conditions.

#### `def alarm_channel(self, value: BaseNode)`

Gets or sets the channel to monitor for alarm conditions.

#### `def procedure(self) -> BaseNode`

Gets or sets the procedure to initiate when the alarm conditions are met.

#### `def procedure(self, value: BaseNode)`

Gets or sets the procedure to initiate when the alarm conditions are met.

#### `def upper_limit_channel(self) -> BaseNode`

Gets the channel that determines the upper limit value of the alarm. If the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.AlarmSource" crefType="Unqualified" /> exceeds this limit, the alarm is triggered.

#### `def lower_limit_channel(self) -> BaseNode`

Gets the channel that determines the lower limit value of the alarm. If the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Alarm.AlarmSource" crefType="Unqualified" /> falls below this limit, the alarm is triggered.

#### `def set_upper_limit(self, upper_limit: float)`

#### `def set_upper_limit(self, upper_limit: BaseNode)`

#### `def set_upper_limit(self, upper_limit: ValueSource)`

#### `def set_upper_limit(self, *args)`

#### `def set_lower_limit(self, lower_limit: float)`

#### `def set_lower_limit(self, lower_limit: BaseNode)`

#### `def set_lower_limit(self, lower_limit: ValueSource)`

#### `def set_lower_limit(self, *args)`

#### `def use_tripped_alarm(self)`

#### `def use_tripped_alarm(self, *args)`

### `class CalculatedChannel(Channel, IChannel)`

Represents a calculated channel, which produces new values based on calculations performed on other channels in the system definition.

#### `def __init__(self, *args)`

Create a new instance.

#### `def formula() -> int`

#### `def maximum() -> int`

#### `def minimum() -> int`

#### `def lowpass_filter() -> int`

#### `def peak_and_valley() -> int`

#### `def acceleration() -> int`

#### `def average() -> int`

#### `def conditional() -> int`

#### `def calculated_channel_type(self) -> int`

Gets the type of the calculated channel.

#### `def downcast(self) -> CalculatedChannel`

#### `def downcast(self, *args)`

### `class CallProcedure(Command)`

Represents a <format type="bold">Call Procedure</format> step that you can add to a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Procedure" crefType="Unqualified" />. The <format type="bold">Call Procedure</format> step calls a procedure when the step executes.

#### `def __init__(self, name: str, description: str, procedure: BaseNode)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def procedure(self) -> BaseNode`

Gets or sets the procedure to call when this step executes.

#### `def procedure(self, value: BaseNode)`

Gets or sets the procedure to call when this step executes.

### `class Conditional(CalculatedChannel, IChannel)`

Represents a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannel" crefType="Unqualified" /> with the conditional function. The conditional function uses an if/else statement to check the channel you specify for the condition you specify and return the appropriate value.

#### `def __init__(self, name: str, description: str, comparison_mode: int, x_value: BaseNode, y_value: float, w_value: float, z_value: float)`

#### `def __init__(self, name: str, description: str, comparison_mode: int, x_value: BaseNode, y_value: float, w_value: float, z_value: BaseNode)`

#### `def __init__(self, name: str, description: str, comparison_mode: int, x_value: BaseNode, y_value: float, w_value: BaseNode, z_value: float)`

#### `def __init__(self, name: str, description: str, comparison_mode: int, x_value: BaseNode, y_value: float, w_value: BaseNode, z_value: BaseNode)`

#### `def __init__(self, name: str, description: str, comparison_mode: int, x_value: BaseNode, y_value: BaseNode, w_value: float, z_value: float)`

#### `def __init__(self, name: str, description: str, comparison_mode: int, x_value: BaseNode, y_value: BaseNode, w_value: float, z_value: BaseNode)`

#### `def __init__(self, name: str, description: str, comparison_mode: int, x_value: BaseNode, y_value: BaseNode, w_value: BaseNode, z_value: float)`

#### `def __init__(self, name: str, description: str, comparison_mode: int, x_value: BaseNode, y_value: BaseNode, w_value: BaseNode, z_value: BaseNode)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def greater() -> int`

#### `def less() -> int`

#### `def equal() -> int`

#### `def not_equal() -> int`

#### `def greater_or_equal() -> int`

#### `def less_or_equal() -> int`

#### `def and_() -> int`

#### `def or_() -> int`

#### `def y_constant_value(self) -> float`

Gets the constant value of <format type="italics">Y</format> in the formula: If (<format type="italics">X</format> compare <format type="italics">Y</format>), then <format type="italics">W</format>. Else, <format type="italics">Z</format>.

#### `def w_constant_value(self) -> float`

Gets the constant value of <format type="italics">W</format> in the formula: If (<format type="italics">X</format> compare <format type="italics">Y</format>), then <format type="italics">W</format>. Else, <format type="italics">Z</format>.

#### `def z_constant_value(self) -> float`

Gets the constant value of <format type="italics">Z</format> in the formula: If (<format type="italics">X</format> compare <format type="italics">Y</format>), then <format type="italics">W</format>. Else, <format type="italics">Z</format>.

#### `def y_channel_value(self) -> BaseNode`

Gets the channel that specifies the value of <format type="italics">Y</format> in the formula: If (<format type="italics">X</format> compare <format type="italics">Y</format>), then <format type="italics">W</format>. Else, <format type="italics">Z</format>.

#### `def w_channel_value(self) -> BaseNode`

Gets the channel that specifies the value of <format type="italics">W</format> in the formula: If (<format type="italics">X</format> compare <format type="italics">Y</format>), then <format type="italics">W</format>. Else, <format type="italics">Z</format>.

#### `def z_channel_value(self) -> BaseNode`

Gets the channel that specifies the value of <format type="italics">Z</format> in the formula: If (<format type="italics">X</format> compare <format type="italics">Y</format>), then <format type="italics">W</format>. Else, <format type="italics">Z</format>.

#### `def comparison_mode(self) -> int`

Gets or sets the type of comparison to use for the condition.

#### `def comparison_mode(self, value: int)`

Gets or sets the type of comparison to use for the condition.

#### `def x_channel(self) -> BaseNode`

Gets or sets the channel to check for the comparison condition. This channel is the value of <format type="italics">X</format> in the formula: If (<format type="italics">X</format> compare <format type="italics">Y</format>), then <format type="italics">W</format>. Else, <format type="italics">Z</format>.

#### `def x_channel(self, value: BaseNode)`

Gets or sets the channel to check for the comparison condition. This channel is the value of <format type="italics">X</format> in the formula: If (<format type="italics">X</format> compare <format type="italics">Y</format>), then <format type="italics">W</format>. Else, <format type="italics">Z</format>.

#### `def set_y_value(self, y_value: float)`

#### `def set_y_value(self, y_value: BaseNode)`

#### `def set_y_value(self, *args)`

#### `def set_w_value(self, w_value: float)`

#### `def set_w_value(self, w_value: BaseNode)`

#### `def set_w_value(self, *args)`

#### `def set_z_value(self, z_value: float)`

#### `def set_z_value(self, z_value: BaseNode)`

#### `def set_z_value(self, *args)`

### `class DAQAnalogInput(DAQChannel, IChannel)`

Represents a DAQ analog input channel.

#### `def __init__(self, name: str, channel: int, plugin_guid: str)`

#### `def __init__(self, name: str, channel: int, plugin_guid: str, initial_value: float)`

#### `def __init__(self, name: str, channel: int, measurement_type: DAQMeasurementType)`

#### `def __init__(self, name: str, channel: int, measurement_type: DAQMeasurementType, initial_value: float)`

#### `def __init__(self, name: str, units: str, initial_value: float, low_level: float, high_level: float, channel: int, channel_type: DAQAnalogChannelType)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def initial_value(self) -> float`

Gets or sets the initial value of the analog input channel.

#### `def initial_value(self, value: float)`

Gets or sets the initial value of the analog input channel.

#### `def channel_type(self) -> DAQAnalogChannelType`

Gets or sets the measurement type of the channel (<format type="monospace">Current</format> or <format type="monospace">Voltage</format>).

#### `def channel_type(self, value: DAQAnalogChannelType)`

Gets or sets the measurement type of the channel (<format type="monospace">Current</format> or <format type="monospace">Voltage</format>).

#### `def channel(self) -> int`

Gets or sets the channel number.

#### `def channel(self, value: int)`

Gets or sets the channel number.

#### `def low_level(self) -> float`

Gets or sets the minimum value of the channel.

#### `def low_level(self, value: float)`

Gets or sets the minimum value of the channel.

#### `def high_level(self) -> float`

Gets or sets the maximum value of the channel.

#### `def high_level(self, value: float)`

Gets or sets the maximum value of the channel.

#### `def is_scxi(self) -> bool`

Gets whether the channel belongs to an SCXI module.

#### `def scxi_module_type(self) -> str`

Gets the specific type of SCXI module to which the channel belongs.

### `class DAQAnalogOutput(DAQChannel, IChannel)`

Represents a DAQ analog output channel.

#### `def __init__(self, name: str, channel: int, plugin_guid: str)`

#### `def __init__(self, name: str, channel: int, plugin_guid: str, initial_value: float)`

#### `def __init__(self, name: str, channel: int, measurement_type: DAQMeasurementType)`

#### `def __init__(self, name: str, channel: int, measurement_type: DAQMeasurementType, initial_value: float)`

#### `def __init__(self, name: str, units: str, initial_value: float, low_level: float, high_level: float, channel: int, channel_type: DAQAnalogChannelType)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def initial_value(self) -> float`

Gets or sets the initial value of the analog output channel.

#### `def initial_value(self, value: float)`

Gets or sets the initial value of the analog output channel.

#### `def channel_type(self) -> DAQAnalogChannelType`

Gets or sets the measurement type of the channel (<format type="monospace">Current</format> or <format type="monospace">Voltage</format>).

#### `def channel_type(self, value: DAQAnalogChannelType)`

Gets or sets the measurement type of the channel (<format type="monospace">Current</format> or <format type="monospace">Voltage</format>).

#### `def channel(self) -> int`

Gets or sets the channel number.

#### `def channel(self, value: int)`

Gets or sets the channel number.

#### `def low_level(self) -> float`

Gets or sets the minimum value of the channel.

#### `def low_level(self, value: float)`

Gets or sets the minimum value of the channel.

#### `def high_level(self) -> float`

Gets or sets the maximum value of the channel.

#### `def high_level(self, value: float)`

Gets or sets the maximum value of the channel.

#### `def is_scxi(self) -> bool`

Gets whether the channel belongs to an SCXI module.

#### `def scxi_module_type(self) -> str`

Gets the specific type of SCXI module to which the channel belongs.

### `class DAQCountUpDown(DAQCounter, IChannel)`

Represents a <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter" crefType="Unqualified" /> channel with the count up/down task type.

#### `def __init__(self, name: str, description: str, index: int, default_value: float, count_direction: DAQCounterCountMode, edge: DAQCounterEdge, reset_variable: BaseNode)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def count_direction(self) -> DAQCounterCountMode`

Gets or sets the direction of the count (up, down, or externally controlled).

#### `def count_direction(self, value: DAQCounterCountMode)`

Gets or sets the direction of the count (up, down, or externally controlled).

#### `def edge(self) -> DAQCounterEdge`

Gets or sets the edge on which to count (rising or falling).

#### `def edge(self, value: DAQCounterEdge)`

Gets or sets the edge on which to count (rising or falling).

#### `def input_terminal(self) -> str`

Gets or sets the input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used.

#### `def input_terminal(self, value: str)`

Gets or sets the input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used.

#### `def reset_variable(self) -> BaseNode`

Gets or sets the channel whose value the counter must reach before it resets.

#### `def reset_variable(self, value: BaseNode)`

Gets or sets the channel whose value the counter must reach before it resets.

### `class DAQCounterInput(DAQSectionType)`

Initializes a new instance of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterInput" /> class.

#### `def __init__(self, *args)`

Create a new instance.

### `class DAQCounterOutput(DAQSectionType)`

Initializes a new instance of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterOutput" /> class.

#### `def __init__(self, *args)`

Create a new instance.

### `class DAQPulseGeneration(DAQCounterOutput)`

Represents a DAQ Counter measurement section of input channels.

#### `def __init__(self, name: str, description: str, index: int)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def counter(self) -> str`

Gets the counter channel number.

#### `def output_terminal(self) -> str`

Gets or sets the output terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used.

#### `def output_terminal(self, value: str)`

Gets or sets the output terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used.

#### `def set_counter_index(self, index: int)`

#### `def set_counter_index(self, *args)`

#### `def get_data_channel(self, type: DAQDataChannelType) -> Channel`

#### `def get_data_channel(self, *args)`

### `class DAQPulseMeasurement(DAQCounterInput)`

Represents a DAQ Counter measurement section of input channels.

#### `def __init__(self, name: str, description: str, index: int)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def counter(self) -> str`

Gets the counter channel number.

#### `def input_terminal(self) -> str`

Gets or sets the input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used.

#### `def input_terminal(self, value: str)`

Gets or sets the input terminal for the counter.
            A value of <see cref="F:NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounter.DefaultTerminal" />
            indicates the default terminal will be used.

#### `def set_counter_index(self, index: int)`

#### `def set_counter_index(self, *args)`

#### `def get_data_channel(self, type: DAQDataChannelType) -> Channel`

#### `def get_data_channel(self, *args)`

### `class ECUNetworkCluster(Model, IECUNetworkClusterConfiguration)`

Represents an ECU network cluster as a specialized type of <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Model" />. Use the ECU network cluster to configure the communication between
            <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.VirtualECU" /> and an XNET device.

#### `def __init__(self, name: str, description: str, ecu_network_cluster_path: str, processor: int, decimation: int, initial_state: int)`

#### `def __init__(self, *args)`

Create a new instance.

### `class FPGAAICategory(FPGACategory)`

Represents the <format type="bold">Input<entity value="raquo" />Analog</format> section under an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FPGADevice" crefType="Unqualified" />.

#### `def __init__(self, *args)`

Create a new instance.

### `class FPGAAOCategory(FPGACategory)`

Represents the <format type="bold">Output<entity value="raquo" />Analog</format> section under an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.FPGADevice" crefType="Unqualified" />.

#### `def __init__(self, *args)`

Create a new instance.

### `class FPGAAnalogInput(FPGAChannel, IChannel)`

Represents an FPGA analog input channel.

#### `def __init__(self, *args)`

Create a new instance.

### `class FPGAAnalogOutput(FPGAChannel, IChannel)`

Represents an FPGA analog output channel.

#### `def __init__(self, *args)`

Create a new instance.

### `class Formula(CalculatedChannel, IChannel)`

Represents a calculated channel with the formula function. This function calculates the result of a formula you specify.

#### `def __init__(self, name: str, description: str, formula: str, variable_names: Sequence[str], variables: Sequence[BaseNode])`

#### `def __init__(self, name: str, description: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def formula_string(self) -> str`

Gets the formula for which the channel calculates the result.

#### `def set_formula(self, formula: str, variable_names: Sequence[str], variables: Sequence[BaseNode])`

#### `def set_formula(self, *args)`

#### `def reset_formula(self)`

#### `def reset_formula(self, *args)`

### `class InportGroup(ModelDefaultGroup)`

Represents a sub-section of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Inports" crefType="Unqualified" /> section of a model. Inport groups provide organization within the model.

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_inport_groups(self) -> Sequence[InportGroup]`

#### `def get_inport_groups(self, *args)`

#### `def get_inports(self) -> Sequence[Inport]`

#### `def get_inports(self, deep: bool) -> Sequence[Inport]`

#### `def get_inports(self, *args)`

### `class LookupTable(Scale)`

Represents a lookup table <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Scale" />, which maps an array of pre-scaled values to an array of corresponding scaled values.

#### `def __init__(self, name: str)`

#### `def __init__(self, name: str, lookup_table_values: Sequence[LUTValue], scale_unit: str)`

#### `def __init__(self, node: BaseNodeType)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def lookup_table_values(self) -> Sequence[LUTValue]`

Gets or sets the values of the LookupTable scale.

#### `def lookup_table_values(self, value: Sequence[LUTValue])`

Gets or sets the values of the LookupTable scale.

### `class LowpassFilter(CalculatedChannel, IChannel)`

Represents a calculated channel with the <format type="bold">Lowpass Filter</format> function. This function applies a lowpass Butterworth filter to the value of the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.LowpassFilter.ChannelToFilter" crefType="Unqualified" />.

#### `def __init__(self, name: str, description: str, channel_to_filter: Channel, low_cutoff_frequency: float, filter_order: int)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def channel_to_filter(self) -> BaseNode`

Gets or sets the channel to which to apply the filter.

#### `def channel_to_filter(self, value: BaseNode)`

Gets or sets the channel to which to apply the filter.

#### `def filter_order(self) -> int`

Gets or sets the order of the filter. Increasing the value of this property causes the transition between the passband and the stopband to become steeper. However, as the filter order increases, the filter becomes more unstable.

#### `def filter_order(self, value: int)`

Gets or sets the order of the filter. Increasing the value of this property causes the transition between the passband and the stopband to become steeper. However, as the filter order increases, the filter becomes more unstable.

#### `def low_cutoff_frequency(self) -> float`

Gets or sets the low cutoff frequency, in hertz.

#### `def low_cutoff_frequency(self, value: float)`

Gets or sets the low cutoff frequency, in hertz.

### `class Maximum(CalculatedChannel, IChannel)`

Represents a calculated channel with the <format type="bold">Maximum</format> function. This function compares two values (<format type="italics">x</format> and <format type="italics">y</format>) and returns the larger value.

#### `def __init__(self, name: str, description: str, x_value: float, y_value: float)`

#### `def __init__(self, name: str, description: str, x_value: float, y_value: BaseNode)`

#### `def __init__(self, name: str, description: str, x_value: BaseNode, y_value: float)`

#### `def __init__(self, name: str, description: str, x_value: BaseNode, y_value: BaseNode)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def x_is_constant(self) -> bool`

Gets whether the value of <format type="italics">x</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format> is specified by a constant or a channel.

#### `def y_is_constant(self) -> bool`

Gets whether the value of <format type="italics">y</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format> is specified by a constant or a channel.

#### `def y_constant_value(self) -> float`

Gets the constant value of <format type="italics">y</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format>. regardless of whether <format type="italics">x</format> is a constant or a channel.

#### `def x_constant_value(self) -> float`

Gets the constant value of <format type="italics">x</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format>, regardless of whether <format type="italics">x</format> is a constant or a channel.

#### `def x_channel_value(self) -> BaseNode`

Gets the channel that specifies the value of <format type="italics">x</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format>.

#### `def y_channel_value(self) -> BaseNode`

Gets the channel that specifies the value of <format type="italics">y</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format>.

#### `def set_x_value(self, x_value: float)`

#### `def set_x_value(self, x_value: BaseNode)`

#### `def set_x_value(self, *args)`

#### `def set_y_value(self, y_value: float)`

#### `def set_y_value(self, y_value: BaseNode)`

#### `def set_y_value(self, *args)`

### `class Minimum(CalculatedChannel, IChannel)`

Represents a calculated channel with the <format type="bold">Minimum</format> function. This function compares two values (<format type="italics">x</format> and <format type="italics">y</format>) and returns the smaller value.

#### `def __init__(self, name: str, description: str, x_value: float, y_value: float)`

#### `def __init__(self, name: str, description: str, x_value: float, y_value: BaseNode)`

#### `def __init__(self, name: str, description: str, x_value: BaseNode, y_value: float)`

#### `def __init__(self, name: str, description: str, x_value: BaseNode, y_value: BaseNode)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def x_is_constant(self) -> bool`

Gets whether the value of <format type="italics">x</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format> is specified by a constant or a channel.

#### `def y_is_constant(self) -> bool`

Gets whether the value of <format type="italics">y</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format> is specified by a constant or a channel.

#### `def y_constant_value(self) -> float`

Gets the constant value of <format type="italics">y</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format>. regardless of whether <format type="italics">x</format> is a constant or a channel.

#### `def x_constant_value(self) -> float`

Gets the constant value of <format type="italics">x</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format>, regardless of whether <format type="italics">x</format> is a constant or a channel.

#### `def x_channel_value(self) -> BaseNode`

Gets the channel that specifies the value of <format type="italics">x</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format>.

#### `def y_channel_value(self) -> BaseNode`

Gets the channel that specifies the value of <format type="italics">y</format> in the comparison of <format type="italics">x</format> and <format type="italics">y</format>.

#### `def set_x_value(self, x_value: float)`

#### `def set_x_value(self, x_value: BaseNode)`

#### `def set_x_value(self, *args)`

#### `def set_y_value(self, y_value: float)`

#### `def set_y_value(self, y_value: BaseNode)`

#### `def set_y_value(self, *args)`

### `class PeakAndValley(CalculatedChannel, IChannel)`

Represents a calculated channel with the <format type="bold">Peak <entity value="amp" /> Valley</format> function. This function calculates the peak, valley, and offset of a cyclical waveform on the channel you specify. The calculated channel stores the peak value, and the channels you specify when you configure the calculated channel store the valley and offset values.

#### `def __init__(self, name: str, description: str, channel_to_analyze: BaseNode, channel_for_valley: BaseNode, channel_for_offset: BaseNode, reset: int, hysteresis: float)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def channel_to_analyze(self) -> BaseNode`

Gets or sets the channel for which to calculate the peak, valley, and offset.

#### `def channel_to_analyze(self, value: BaseNode)`

Gets or sets the channel for which to calculate the peak, valley, and offset.

#### `def channel_for_valley(self) -> BaseNode`

Gets or sets the channel on which to store the valley value.

#### `def channel_for_valley(self, value: BaseNode)`

Gets or sets the channel on which to store the valley value.

#### `def channel_for_offset(self) -> BaseNode`

Gets or sets the channel on which to store the offset value.

#### `def channel_for_offset(self, value: BaseNode)`

Gets or sets the channel on which to store the offset value.

#### `def hysteresis(self) -> float`

Gets or sets the amount by which the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley.ChannelToAnalyze" crefType="Unqualified" /> must exceed the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley.Reset" crefType="Unqualified" /> value for the calculation to reset.

#### `def hysteresis(self, value: float)`

Gets or sets the amount by which the value of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley.ChannelToAnalyze" crefType="Unqualified" /> must exceed the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley.Reset" crefType="Unqualified" /> value for the calculation to reset.

#### `def reset(self) -> int`

Gets or sets the value at which to reset the calculation. If the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley.ChannelToAnalyze" crefType="Unqualified" /> surpasses this value by more than the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley.Hysteresis" crefType="Unqualified" />, the calculation resets.

#### `def reset(self, value: int)`

Gets or sets the value at which to reset the calculation. If the <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley.ChannelToAnalyze" crefType="Unqualified" /> surpasses this value by more than the specified <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.PeakAndValley.Hysteresis" crefType="Unqualified" />, the calculation resets.

### `class PolynomialScale(Scale)`

Represents a polynomial <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.Scale" />, which converts values using a polynomial equation with up to ten coefficients.

#### `def __init__(self, name: str)`

#### `def __init__(self, name: str, polynomial_coeff: Sequence[float], reverse_polynomial_coeff: Sequence[float], scale_unit: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def polynomial_coeff(self) -> Sequence[float]`

Gets or sets the forward coefficients of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.PolynomialScale" />.

#### `def polynomial_coeff(self, value: Sequence[float])`

Gets or sets the forward coefficients of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.PolynomialScale" />.

#### `def reverse_polynomial_coeff(self) -> Sequence[float]`

Gets or sets the reverse coefficients of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.PolynomialScale" />.

#### `def reverse_polynomial_coeff(self, value: Sequence[float])`

Gets or sets the reverse coefficients of the <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.PolynomialScale" />.

### `class SCXI1100(SCXIModule)`

Represents an SCXI-1100 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1102(SCXIModule)`

Represents an SCXI-1102 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1102B(SCXIModule)`

Represents an SCXI-1102B module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1102C(SCXIModule)`

Represents an SCXI-1102C module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1104(SCXIModule)`

Represents an SCXI-1104 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1104C(SCXIModule)`

Represents an SCXI-1104C module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1112(SCXIModule)`

Represents an SCXI-1112 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1120(SCXIModule)`

Represents an SCXI-1120 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1120D(SCXIModule)`

Represents an SCXI-1120D module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1121(SCXIModule)`

Represents an SCXI-1121 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1122(SCXIModule)`

Represents an SCXI-1122 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1124(SCXIModule)`

Represents an SCXI-1124 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1125(SCXIModule)`

Represents an SCXI-1125 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1126(SCXIModule)`

Represents an SCXI-1126 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1127(SCXIModule)`

Represents an SCXI-1127 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1128(SCXIModule)`

Represents an SCXI-1128 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1140(SCXIModule)`

Represents an SCXI-1140 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1141(SCXIModule)`

Represents an SCXI-1141 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1142(SCXIModule)`

Represents an SCXI-1142 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1143(SCXIModule)`

Represents an SCXI-1143 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1160(SCXIModule)`

Represents an SCXI-1160 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1161(SCXIModule)`

Represents an SCXI-1161 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1162(SCXIModule)`

Represents an SCXI-1162 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1162HV(SCXIModule)`

Represents an SCXI-1162HV module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1163(SCXIModule)`

Represents an SCXI-1163 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1163R(SCXIModule)`

Represents an SCXI-1163R module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1190(SCXIModule)`

Represents an SCXI-1190 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1191(SCXIModule)`

Represents an SCXI-1191 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1192(SCXIModule)`

Represents an SCXI-1192 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1520(SCXIModule)`

Represents an SCXI-1520 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1530(SCXIModule)`

Represents an SCXI-1530 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1531(SCXIModule)`

Represents an SCXI-1531 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1540(SCXIModule)`

Represents an SCXI-1540 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class SCXI1581(SCXIModule)`

Represents an SCXI-1581 module that you can add to an <see cref="T:NationalInstruments.VeriStand.SystemDefinitionAPI.SCXIChassis" crefType="Unqualified" />.

#### `def __init__(self, name: str)`

#### `def __init__(self, *args)`

Create a new instance.

### `class Acceleration(CalculatedChannel, IChannel)`

Represents a calculated channel with the acceleration function.

#### `def __init__(self, name: str, description: str, units: str, channel_to_analyze: BaseNode, channel_for_velocity: BaseNode)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def velocity_channel(self) -> BaseNode`

Gets or sets the channel on which to store the velocity of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Acceleration.XChannel" crefType="Unqualified" />.

#### `def velocity_channel(self, value: BaseNode)`

Gets or sets the channel on which to store the velocity of <see cref="P:NationalInstruments.VeriStand.SystemDefinitionAPI.Acceleration.XChannel" crefType="Unqualified" />.

#### `def x_channel(self) -> BaseNode`

Gets or sets the channel for which to calculate the acceleration.

#### `def x_channel(self, value: BaseNode)`

Gets or sets the channel for which to calculate the acceleration.

### `class Average(CalculatedChannel, IChannel)`

Represents a calculated channel with the average function. The average function calculates the average value of the channel you specify every <format type="italics">n</format> points.

#### `def __init__(self, name: str, description: str, number_of_points: int, channel_to_average: Channel)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def channel_to_average(self) -> BaseNode`

Gets or sets the channel for which to calculate the average value.

#### `def channel_to_average(self, value: BaseNode)`

Gets or sets the channel for which to calculate the average value.

#### `def number_of_points(self) -> int`

Gets or sets the number of points of data to include in the average.

#### `def number_of_points(self, value: int)`

Gets or sets the number of points of data to include in the average.

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/systemdefinitionapi/fpga_support/__init__.py -->
## PYTHON MODULE: src/niveristand/systemdefinitionapi/fpga_support/__init__.py

### MODULE DOCSTRING

Module for NationalInstruments.VeriStand.SystemDefinitionAPI.FPGA_Support.

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/systemdefinitionapi/fpga_support/_auto_generated_classes.py -->
## PYTHON MODULE: src/niveristand/systemdefinitionapi/fpga_support/_auto_generated_classes.py

### MODULE DOCSTRING

Module for NationalInstruments.VeriStand.SystemDefinitionAPI.FPGA_Support.

### `class _staticproperty(staticmethod)`

#### `def __get__(self, *_)`

### `class _DotNetBase()`

#### `def __eq__(self, other) -> bool`

#### `def __repr__(self) -> str`

#### `def _custom_repr(self) -> str`

### `class _DotNetEnum(_DotNetBase)`

#### `def __repr__(self) -> str`

#### `def __str__(self) -> str`

#### `def __int__(self) -> int`

### `def _is_iterable(arg: Any) -> bool`

### `def _unwrap(out_params: Dict[Optional[Tuple[str, ...]], Tuple[int, Any]], *args: Tuple[Any]) -> Iterable[Any]`

### `def _wrap(one_or_many_args: Union[Any, Tuple[Any]]) -> Union[Any, Tuple[Any]]`

### `class FPGACategory(_DotNetBase)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def name(self) -> str`

#### `def description(self) -> str`

#### `def symbol(self) -> str`

#### `def categories(self) -> Sequence[FPGACategory]`

#### `def channels(self) -> Sequence[FPGAChannel]`

#### `def to_string(self) -> str`

#### `def to_string(self, *args)`

#### `def _custom_repr(self) -> str`

### `class FPGAChannel(_DotNetBase)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def name(self) -> str`

#### `def category(self) -> str`

#### `def symbol(self) -> str`

#### `def description(self) -> str`

#### `def unit(self) -> str`

#### `def initial_value(self) -> float`

#### `def packet_index(self) -> int`

#### `def bit_offset(self) -> int`

#### `def representation(self) -> int`

#### `def scaling(self) -> float`

#### `def scaling_offset(self) -> float`

#### `def fxpwl(self) -> int`

#### `def fxpiwl(self) -> int`

#### `def period_pwm(self) -> int`

#### `def data_offset(self) -> int`

#### `def is_write(self) -> bool`

#### `def to_string(self) -> str`

#### `def to_string(self, *args)`

#### `def _custom_repr(self) -> str`

### `class FPGALoader(_DotNetBase)`

#### `def __init__(self, file_path: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def version(self) -> float`

#### `def bit_file(self) -> str`

#### `def read_packets(self) -> int`

#### `def write_packets(self) -> int`

#### `def categories(self) -> Sequence[FPGACategory]`

#### `def to_string(self) -> str`

#### `def to_string(self, *args)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/systemdefinitionapi/modelsupport/__init__.py -->
## PYTHON MODULE: src/niveristand/systemdefinitionapi/modelsupport/__init__.py

### MODULE DOCSTRING

Module for NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/systemdefinitionapi/modelsupport/_auto_generated_classes.py -->
## PYTHON MODULE: src/niveristand/systemdefinitionapi/modelsupport/_auto_generated_classes.py

### MODULE DOCSTRING

Module for NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.

### `class _staticproperty(staticmethod)`

#### `def __get__(self, *_)`

### `class _DotNetBase()`

#### `def __eq__(self, other) -> bool`

#### `def __repr__(self) -> str`

#### `def _custom_repr(self) -> str`

### `class _DotNetEnum(_DotNetBase)`

#### `def __repr__(self) -> str`

#### `def __str__(self) -> str`

#### `def __int__(self) -> int`

### `def _is_iterable(arg: Any) -> bool`

### `def _unwrap(out_params: Dict[Optional[Tuple[str, ...]], Tuple[int, Any]], *args: Tuple[Any]) -> Iterable[Any]`

### `def _wrap(one_or_many_args: Union[Any, Tuple[Any]]) -> Union[Any, Tuple[Any]]`

### `class IModelDescriptor(_DotNetBase)`

Holds information from the model descriptor

#### `def __init__(self, *args)`

Create a new instance.

#### `def model_name(self) -> str`

Name of the model

#### `def model_generation_toolchain_version(self) -> Tuple[int, int, int, int]`

Version of the tool that was used to generate the model

#### `def model_version(self) -> Tuple[int, int, int, int]`

Version of the model

#### `def author(self) -> str`

Model author

#### `def model_description(self) -> str`

Description of the model

#### `def target_platforms(self) -> Iterable[str]`

Target platforms supported by the model

### `class ModelParamType(_DotNetBase)`

RESERVED FOR INTERNAL USE. Wraps model parameter information.

#### `def __init__(self, idx: int, id: str, name: str, type: int, dims: Sequence[int], value: Sequence[float])`

#### `def __init__(self, idx: int, id: str, name: str, type: int, dims: Sequence[int], value: Sequence[float], enum_value_table: Sequence[Tuple[str, int]], enum_class_name: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def idx(self) -> int`

#### `def id(self) -> str`

#### `def name(self) -> str`

#### `def data_type(self) -> int`

#### `def enum_class_name(self) -> str`

#### `def dims(self) -> Sequence[int]`

RESERVED FOR INTERNAL USE.

#### `def value(self) -> Sequence[float]`

RESERVED FOR INTERNAL USE.

#### `def enum_value_table(self) -> Sequence[Tuple[str, int]]`

EnumValueTable for parameters

#### `def enum_value_table(self, value: Sequence[Tuple[str, int]])`

EnumValueTable for parameters

#### `def _custom_repr(self) -> str`

### `class ModelPortType(_DotNetBase)`

RESERVED FOR INTERNAL USE. Wraps model port information.

#### `def __init__(self, name: str, index: int, task_id: int, is_input: bool, dims: Sequence[int])`

#### `def __init__(self, name: str, index: int, task_id: int, is_input: bool, dims: Sequence[int], enum_value_table: Sequence[Tuple[str, int]], enum_class_name: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def name(self) -> str`

#### `def index(self) -> int`

#### `def task_id(self) -> int`

#### `def is_input(self) -> bool`

#### `def enum_class_name(self) -> str`

#### `def dims(self) -> Sequence[int]`

RESERVED FOR INTERNAL USE.

#### `def enum_value_table(self) -> Sequence[Tuple[str, int]]`

EnumValueTable for inports and outports

#### `def enum_value_table(self, value: Sequence[Tuple[str, int]])`

EnumValueTable for inports and outports

#### `def _custom_repr(self) -> str`

### `class ModelSignalType(_DotNetBase)`

RESERVED FOR INTERNAL USE. Wraps signal info from a model.

#### `def __init__(self, idx: int, id: str, name: str, block_name: str, port_number: int, datatype: int, dims: Sequence[int])`

#### `def __init__(self, idx: int, id: str, name: str, block_name: str, port_number: int, datatype: int, dims: Sequence[int], enum_value_table: Sequence[Tuple[str, int]], enum_class_name: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def idx(self) -> int`

#### `def id(self) -> str`

#### `def name(self) -> str`

#### `def block_name(self) -> str`

#### `def data_type(self) -> int`

#### `def port_number(self) -> int`

#### `def enum_class_name(self) -> str`

#### `def dims(self) -> Sequence[int]`

RESERVED FOR INTERNAL USE.

#### `def enum_value_table(self) -> Sequence[Tuple[str, int]]`

EnumValueTable for signals

#### `def enum_value_table(self, value: Sequence[Tuple[str, int]])`

EnumValueTable for signals

#### `def _custom_repr(self) -> str`

### `class VsModelEnumTypeDefinitionItems(_DotNetBase)`

VsModelEnumTypeDefinitionItems type

#### `def __init__(self)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def enum_values(self) -> Sequence[int]`

Enum Values for the enum

#### `def enum_values(self, value: Sequence[int])`

Enum Values for the enum

#### `def enum_names(self) -> Sequence[str]`

Enum name for the enum

#### `def enum_names(self, value: Sequence[str])`

Enum name for the enum

### `class VsModelFeatureSet(_DotNetBase)`

Provides information about supported features of a specific version of .vsmodel

#### `def __init__(self, vsmodel_version: str)`

#### `def __init__(self, vsmodel_version: System.Version)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def first_released_vs_model_addon_version_string() -> str`

The first released VsModel addon version as string

#### `def highest_supported_vs_model_addon_version_string() -> str`

Highest supported VsModel addon version as string

#### `def supports_non_virtual_bus(self) -> bool`

Indicates whether the vsmodel has support for non virtual buses

#### `def generated_using_latest_addon_version(self) -> bool`

Indicates whether the vsmodel was built with the latest VsModel addon

#### `def supports_signals(self) -> bool`

Indicates whether the vsmodel has support for signals

### `class VsModelItemBaseType(_DotNetBase)`

Class containing information about a model item type. The item can be input, output or parameter

#### `def __init__(self)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def name(self) -> str`

Name of the element

#### `def name(self, value: str)`

Name of the element

#### `def data_type(self) -> str`

Model item data type

#### `def data_type(self, value: str)`

Model item data type

#### `def c_api_type(self) -> str`

Type used by Simulink in the generated C code

#### `def c_api_type(self, value: str)`

Type used by Simulink in the generated C code

#### `def dimensions(self) -> Any`

Model item dimensions

#### `def dimensions(self, value: Any)`

Model item dimensions

#### `def elements(self) -> Sequence[VsModelElement]`

Model item elements - has content when the item is Bus

#### `def elements(self, value: Sequence[VsModelElement])`

Model item elements - has content when the item is Bus

#### `def enum_class_name(self) -> str`

Model item EnumClassName

#### `def enum_class_name(self, value: str)`

Model item EnumClassName

#### `def is_valid(self) -> bool`

#### `def is_valid(self, *args)`

#### `def is_supported_fixed_point_type(self) -> bool`

#### `def is_supported_fixed_point_type(self, *args)`

#### `def _custom_repr(self) -> str`

### `class VsModelItemType(VsModelItemBaseType)`

Model item type

#### `def __init__(self)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def unit(self) -> str`

Model item unit

#### `def unit(self, value: str)`

Model item unit

### `class VsModelJsonFileDescriptor(_DotNetBase)`

Class containing information for deserializing the VsModel descriptor JSON file

#### `def __init__(self)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def version(self) -> str`

Model version

#### `def version(self, value: str)`

Model version

#### `def model_name(self) -> str`

Model name

#### `def model_name(self, value: str)`

Model name

#### `def metadata(self) -> VsModelMetadata`

Model metadata

#### `def metadata(self, value: VsModelMetadata)`

Model metadata

#### `def inports(self) -> Sequence[VsModelInport]`

Inport list

#### `def inports(self, value: Sequence[VsModelInport])`

Inport list

#### `def outports(self) -> Sequence[VsModelOutport]`

Outport list

#### `def outports(self, value: Sequence[VsModelOutport])`

Outport list

#### `def parameters(self) -> Sequence[VsModelParameter]`

Parameter list

#### `def parameters(self, value: Sequence[VsModelParameter])`

Parameter list

#### `def signals(self) -> Sequence[VsModelSignal]`

Signals list

#### `def signals(self, value: Sequence[VsModelSignal])`

Signals list

#### `def enum_type_definitions(self) -> System.Collections.Generic.IReadOnlyDictionary[System.String, NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelEnumTypeDefinitionItems]`

EnumTypeDefinitions dictionary

#### `def enum_type_definitions(self, value: System.Collections.Generic.IReadOnlyDictionary[System.String, NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelEnumTypeDefinitionItems])`

EnumTypeDefinitions dictionary

### `class VsModelJsonFileDescriptorUtilities(_DotNetBase)`

Utility methods for VsModelJsonFileDescriptor

#### `def __init__(self, *args)`

Create a new instance.

#### `def get_dimensions(dimensions: Any) -> Sequence[int]`

#### `def get_dimensions(*args)`

#### `def is_scalar(dimensions: Any) -> bool`

#### `def is_scalar(*args)`

### `class VsModelMetadata(_DotNetBase)`

VsModel metadata

#### `def __init__(self)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def slx_file_path(self) -> str`

.slx file path

#### `def slx_file_path(self, value: str)`

.slx file path

#### `def simulink_release(self) -> str`

Simulink release

#### `def simulink_release(self, value: str)`

Simulink release

#### `def simulink_version(self) -> str`

Simulink version

#### `def simulink_version(self, value: str)`

Simulink version

#### `def release_description(self) -> str`

Simulink release descripton

#### `def release_description(self, value: str)`

Simulink release descripton

#### `def author(self) -> str`

Model file author

#### `def author(self, value: str)`

Model file author

#### `def description(self) -> str`

Model description

#### `def description(self, value: str)`

Model description

#### `def model_version(self) -> str`

Model version

#### `def model_version(self, value: str)`

Model version

#### `def time_step(self) -> str`

Model time step

#### `def time_step(self, value: str)`

Model time step

#### `def target_platforms(self) -> Sequence[str]`

Target platform the model was compiled for

#### `def target_platforms(self, value: Sequence[str])`

Target platform the model was compiled for

#### `def bitness(self) -> int`

Model bitness

#### `def bitness(self, value: int)`

Model bitness

#### `def number_of_sample_times(self) -> int`

Number of sample times

#### `def number_of_sample_times(self, value: int)`

Number of sample times

#### `def external_mode(self) -> str`

External mode setting: on or off

#### `def external_mode(self, value: str)`

External mode setting: on or off

### `class VsModelParameter(VsModelItemType)`

Parameter type

#### `def __init__(self)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def default_value(self) -> Any`

Default value

#### `def default_value(self, value: Any)`

Default value

### `class VsModelSignal(VsModelItemType)`

Signal type

#### `def __init__(self)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def block_path(self) -> str`

Name of the source block for the signal.

#### `def block_path(self, value: str)`

Name of the source block for the signal.

#### `def port_number(self) -> int`

Port number of the block that is the source of the signal.

#### `def port_number(self, value: int)`

Port number of the block that is the source of the signal.

#### `def signal_label(self) -> str`

Name of the signal

#### `def signal_label(self, value: str)`

Name of the signal

#### `def is_connected_to_virtual_bus(self) -> bool`

Whether the signal is connected to a virtual bus.

#### `def is_connected_to_virtual_bus(self, value: bool)`

Whether the signal is connected to a virtual bus.

### `class FmuModelDescriptor(IModelDescriptor)`

#### `def __init__(self, model_path: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def target_platforms(self) -> Iterable[str]`

#### `def target_platforms(self, value: Iterable[str])`

#### `def fmi_version(self) -> str`

FMI version

#### `def fmi_version(self, value: str)`

FMI version

#### `def generation_tool(self) -> str`

Model generation tool

#### `def generation_tool(self, value: str)`

Model generation tool

#### `def fmu_file_size(self) -> int`

Model file size

### `class VsModelDescriptorExtended(VsModelJsonFileDescriptor, IModelDescriptor)`

VsModel descriptor containing both information needed for deserialization and other vsmodel properties

#### `def __init__(self)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def enum_value_table_by_enum_class_name(self) -> dict[str, Sequence[Tuple[str, int]]]`

EnumValueTable by enum class name of the model

#### `def enum_value_table_by_enum_class_name(self, value: dict[str, Sequence[Tuple[str, int]]])`

EnumValueTable by enum class name of the model

#### `def deserialize_from(stream_reader: System.IO.StreamReader) -> VsModelDescriptorExtended`

#### `def deserialize_from(*args)`

### `class VsModelElement(VsModelItemBaseType)`

Element type

#### `def __init__(self)`

#### `def __init__(self, *args)`

Create a new instance.

### `class VsModelInportOutportType(VsModelItemType)`

Inport and Outports type

#### `def __init__(self)`

#### `def __init__(self, *args)`

Create a new instance.

### `class VsModelOutport(VsModelInportOutportType)`

Outport type

#### `def __init__(self)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def is_connected_to_virtual_bus(self) -> bool`

Whether the outport is connected to a virtual bus.

#### `def is_connected_to_virtual_bus(self, value: bool)`

Whether the outport is connected to a virtual bus.

### `class VsModelInport(VsModelInportOutportType)`

Inport type

#### `def __init__(self)`

#### `def __init__(self, *args)`

Create a new instance.

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/systemdefinitionapi/modelsupport/virtualecusupport/__init__.py -->
## PYTHON MODULE: src/niveristand/systemdefinitionapi/modelsupport/virtualecusupport/__init__.py

### MODULE DOCSTRING

Module for NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/systemdefinitionapi/modelsupport/virtualecusupport/_auto_generated_classes.py -->
## PYTHON MODULE: src/niveristand/systemdefinitionapi/modelsupport/virtualecusupport/_auto_generated_classes.py

### MODULE DOCSTRING

Module for NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.

### `class _staticproperty(staticmethod)`

#### `def __get__(self, *_)`

### `class _DotNetBase()`

#### `def __eq__(self, other) -> bool`

#### `def __repr__(self) -> str`

#### `def _custom_repr(self) -> str`

### `class _DotNetEnum(_DotNetBase)`

#### `def __repr__(self) -> str`

#### `def __str__(self) -> str`

#### `def __int__(self) -> int`

### `def _is_iterable(arg: Any) -> bool`

### `def _unwrap(out_params: Dict[Optional[Tuple[str, ...]], Tuple[int, Any]], *args: Tuple[Any]) -> Iterable[Any]`

### `def _wrap(one_or_many_args: Union[Any, Tuple[Any]]) -> Union[Any, Tuple[Any]]`

### `class CANConfiguration(ICANConfiguration)`

#### `def __init__(self)`

#### `def __init__(self, other: ICANConfiguration)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def connect_to_real_network(self) -> bool`

Value indicating whether to connect to the real network.

#### `def connect_to_real_network(self, value: bool)`

Value indicating whether to connect to the real network.

#### `def use_database(self) -> bool`

Value indicating whether to use a database.

#### `def use_database(self, value: bool)`

Value indicating whether to use a database.

#### `def database_alias(self) -> str`

Database alias value.

#### `def database_alias(self, value: str)`

Database alias value.

### `class Constants(_DotNetBase)`

Contains constants for VirtualECU

#### `def __init__(self, *args)`

Create a new instance.

#### `def ecu_network_cluster_file_extension() -> str`

### `class ECUNetworkClusterConfiguration(IECUNetworkClusterConfiguration)`

Class for serializing and de-serializing ECU network cluster configuration.

#### `def __init__(self)`

#### `def __init__(self, other: IECUNetworkClusterConfiguration)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def version(self) -> str`

Version of the json file.

#### `def version(self, value: str)`

Version of the json file.

#### `def database_path(self) -> str`

Database path.

#### `def database_path(self, value: str)`

Database path.

#### `def virtual_ecu_list(self) -> Sequence[str]`

Virtual ECUs that have been added to the cluster.

#### `def virtual_ecu_list(self, value: Sequence[str])`

Virtual ECUs that have been added to the cluster.

#### `def lin_master_model_linux_path(self) -> str`

LIN Master Model path.

#### `def lin_master_model_linux_path(self, value: str)`

LIN Master Model path.

#### `def svb_configuration(self) -> SVBConfiguration`

Represents the configuration for Synopsys Virtual Bus (SVB).

#### `def svb_configuration(self, value: SVBConfiguration)`

Represents the configuration for Synopsys Virtual Bus (SVB).

#### `def serialize_to(self, cluster_configuration_file_path: str)`

#### `def serialize_to(self, *args)`

#### `def try_deserialize_from(model_path: str) -> Tuple[bool, IECUNetworkClusterConfiguration]`

#### `def try_deserialize_from(*args)`

#### `def deserialize_from(file_path: str) -> IECUNetworkClusterConfiguration`

#### `def deserialize_from(*args)`

### `class EthernetConfiguration(IEthernetConfiguration)`

#### `def __init__(self)`

#### `def __init__(self, other: IEthernetConfiguration)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def connect_to_real_network(self) -> bool`

Value indicating whether to connect to the real network.

#### `def connect_to_real_network(self, value: bool)`

Value indicating whether to connect to the real network.

#### `def virtual_ecumac_addresses(self) -> Sequence[str]`

Virtual ECU MAC Addresses.

#### `def virtual_ecumac_addresses(self, value: Sequence[str])`

Virtual ECU MAC Addresses.

### `class LINConfiguration(ILINConfiguration)`

#### `def __init__(self)`

#### `def __init__(self, other: ILINConfiguration)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def connect_to_real_network(self) -> bool`

Value indicating whether to connect to the real network.

#### `def connect_to_real_network(self, value: bool)`

Value indicating whether to connect to the real network.

#### `def use_database(self) -> bool`

Value indicating whether to use a database.

#### `def use_database(self, value: bool)`

Value indicating whether to use a database.

#### `def database_alias(self) -> str`

Database alias value.

#### `def database_alias(self, value: str)`

Database alias value.

#### `def virtual_tx_frame_i_ds(self) -> Sequence[int]`

Virtual transmission frame IDs.

#### `def virtual_tx_frame_i_ds(self, value: Sequence[int])`

Virtual transmission frame IDs.

### `class SVBConfiguration(_DotNetBase)`

#### `def __init__(self)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def rx_fifo_capacity(self) -> int`

#### `def rx_fifo_capacity(self, value: int)`

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/systemstorage/__init__.py -->
## PYTHON MODULE: src/niveristand/systemstorage/__init__.py

### MODULE DOCSTRING

Module for NationalInstruments.VeriStand.SystemStorage.

<!--NI_PYTHON_API repo=niveristand-python path=src/niveristand/systemstorage/_auto_generated_classes.py -->
## PYTHON MODULE: src/niveristand/systemstorage/_auto_generated_classes.py

### MODULE DOCSTRING

Module for NationalInstruments.VeriStand.SystemStorage.

### `class _staticproperty(staticmethod)`

#### `def __get__(self, *_)`

### `class _DotNetBase()`

#### `def __eq__(self, other) -> bool`

#### `def __repr__(self) -> str`

#### `def _custom_repr(self) -> str`

### `class _DotNetEnum(_DotNetBase)`

#### `def __repr__(self) -> str`

#### `def __str__(self) -> str`

#### `def __int__(self) -> int`

### `def _is_iterable(arg: Any) -> bool`

### `def _unwrap(out_params: Dict[Optional[Tuple[str, ...]], Tuple[int, Any]], *args: Tuple[Any]) -> Iterable[Any]`

### `def _wrap(one_or_many_args: Union[Any, Tuple[Any]]) -> Union[Any, Tuple[Any]]`

### `class BaseNodeType(_DotNetBase)`

Base class for all nodes in the tree. All actual nodes in the tree is a specialized type of this base class.

#### `def __init__(self, node_name: str, type_guid: str)`

#### `def __init__(self, to_copy: BaseNodeType)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def node_path_array(self) -> Sequence[str]`

Get the node path of the node as path array.

#### `def node_path(self) -> str`

Get the node path of the node as a string.

#### `def errors_array(self) -> Sequence[ErrorEntry]`

#### `def errors_array(self, value: Sequence[ErrorEntry])`

#### `def bfs_enumerator(self) -> System.IEnumerator[NationalInstruments.VeriStand.SystemStorage.BaseNodeType]`

Return a Breath First Search enumerator. This enumerator iterates through all children of
            then node directly before diving into the hierarchy. For leaf type nodes it will return only itself.

#### `def dfs_enumerator(self) -> System.IEnumerator[NationalInstruments.VeriStand.SystemStorage.BaseNodeType]`

Return a Depth First Search enumerator. This enumerator iterates into the hiearchy of the
            first children it found.

#### `def child_only_enumerator(self) -> System.IEnumerator[NationalInstruments.VeriStand.SystemStorage.BaseNodeType]`

Return enumerator that allow user to enumerate through the children of this node only.

#### `def child_only_object_enumerator(self) -> System.Collections.IEnumerator`

Return non generic enumerator that allow user to enumerate through the children of this node only.

#### `def trav_parent_enumerator(self) -> System.IEnumerator[NationalInstruments.VeriStand.SystemStorage.BaseNodeType]`

Return enumerator that allow user to enumerate through the parent.

#### `def id(self) -> int`

ID

#### `def id(self, value: int)`

ID

#### `def temp_properties(self) -> Sequence[PropertyType]`

#### `def temp_properties(self, value: Sequence[PropertyType])`

#### `def description(self) -> str`

#### `def description(self, value: str)`

#### `def properties(self) -> Sequence[PropertyType]`

#### `def properties(self, value: Sequence[PropertyType])`

#### `def errors(self) -> Sequence[ErrorEntry]`

#### `def errors(self, value: Sequence[ErrorEntry])`

#### `def name(self) -> str`

#### `def name(self, value: str)`

#### `def type_guid(self) -> str`

#### `def type_guid(self, value: str)`

#### `def identifier(self) -> System.Guid`

#### `def identifier(self, value: System.Guid)`

#### `def add_error(self, key: str, is_error: bool, err_code: int, message: str)`

#### `def add_error(self, *args)`

#### `def remove_error(self, key: str)`

#### `def remove_error(self, *args)`

#### `def remove_all_error(self)`

#### `def remove_all_error(self, *args)`

#### `def duplicate_public_errors(self, other_node: BaseNodeType)`

#### `def duplicate_public_errors(self, *args)`

#### `def get_all_errors(self) -> Sequence[ErrorEntry]`

#### `def get_all_errors(self, *args)`

#### `def on_collection_changed(self, e: System.Collections.Specialized.NotifyCollectionChangedEventArgs)`

#### `def on_collection_changed(self, *args)`

#### `def compare_to(self, obj: Any) -> int`

#### `def compare_to(self, other: BaseNodeType) -> int`

#### `def compare_to(self, *args)`

#### `def to_string(self) -> str`

#### `def to_string(self, *args)`

#### `def dispose(self)`

#### `def dispose(self, *args)`

#### `def get_node_type(self) -> NodeType`

#### `def get_node_type(self, *args)`

#### `def get_node_children(self, deep: bool, mode: TraversalMode) -> Sequence[BaseNodeType]`

#### `def get_node_children(self, *args)`

#### `def get_sorted_node_children(self, deep_traversal: bool, natural_sort: bool, guids_to_skip_child_sort: Sequence[str]) -> Sequence[BaseNodeType]`

#### `def get_sorted_node_children(self, deep_traversal: bool, natural_sort: bool, guids_to_skip_child_sort: Sequence[str], leaf_filter: ITraverseNodeFilter, branch_filter: ITraverseNodeFilter) -> Sequence[BaseNodeType]`

#### `def get_sorted_node_children(self, *args)`

#### `def find_node_in_array(self, list: Sequence[BaseNodeType]) -> int`

#### `def find_node_in_array(self, *args)`

#### `def filter_base_node_types(self, list: Sequence[BaseNodeType], filter: ITraverseNodeFilter) -> Sequence[BaseNodeType]`

#### `def filter_base_node_types(self, *args)`

#### `def is_reference_same_object(self, node_to_compare: BaseNodeType) -> bool`

#### `def is_reference_same_object(self, *args)`

#### `def rename_node(self, new_name: str) -> bool`

#### `def rename_node(self, *args)`

#### `def is_node_relative(self, node_to_check: BaseNodeType) -> bool`

#### `def is_node_relative(self, *args)`

#### `def accept(self, visitor: IVisitor)`

#### `def accept(self, visitor_inspection: IVisitorWithInspection) -> IInspectorResult`

#### `def accept(self, *args)`

#### `def get_node_root(self) -> RootType`

#### `def get_node_root(self, *args)`

#### `def get_parent(self) -> Tuple[bool, BaseNodeType]`

#### `def get_parent(self, *args)`

#### `def get_duplicate_reference(self) -> BaseNodeType`

#### `def get_duplicate_reference(self, *args)`

#### `def find_node(self, id: int) -> Tuple[bool, BaseNodeType]`

#### `def find_node(self, path: Sequence[str]) -> Tuple[bool, BaseNodeType]`

#### `def find_node(self, *args)`

#### `def find_first_child_node_with_name(self, name: str) -> Tuple[bool, BaseNodeType]`

#### `def find_first_child_node_with_name(self, *args)`

#### `def find_node_match_guid(self, guid: str, recurse: bool) -> Sequence[BaseNodeType]`

#### `def find_node_match_guid(self, guid: str) -> BaseNodeType`

#### `def find_node_match_guid(self, guids: Sequence[str], recurse: bool) -> Tuple[Sequence[BaseNodeType], str]`

#### `def find_node_match_guid(self, *args)`

#### `def find_nodesby_guid(self, guids: Sequence[str], recurse: bool, traversal_mode: TraversalMode) -> Tuple[bool, Sequence[BaseNodeType]]`

#### `def find_nodesby_guid(self, *args)`

#### `def find_guid_up(self, guid: str) -> Tuple[bool, BaseNodeType]`

#### `def find_guid_up(self, guid: Sequence[str]) -> Tuple[bool, BaseNodeType, str]`

#### `def find_guid_up(self, *args)`

#### `def remove_node(self)`

#### `def remove_node(self, for_reuse: bool)`

#### `def remove_node(self, *args)`

#### `def move_node_to(self, new_parent: BaseNodeType) -> bool`

#### `def move_node_to(self, *args)`

#### `def attached_child_node(self, node_to_attached: BaseNodeType) -> bool`

#### `def attached_child_node(self, *args)`

#### `def get_node_properties(self) -> Tuple[Sequence[str], Sequence[PropertyContent]]`

#### `def get_node_properties(self, *args)`

#### `def get_node_property_type(self, name: str) -> Tuple[bool, PropertyContent]`

#### `def get_node_property_type(self, *args)`

#### `def get_all_properties_with_type(self, prop_type: PropertyContent) -> Sequence[str]`

#### `def get_all_properties_with_type(self, *args)`

#### `def has_node_property(self, name: str) -> Tuple[bool, PropertyContent]`

#### `def has_node_property(self, *args)`

#### `def clear_properties(self)`

#### `def clear_properties(self, *args)`

#### `def duplicate_properties(self, other_node: BaseNodeType)`

#### `def duplicate_properties(self, *args)`

#### `def set_string_property(self, name: str, value: str) -> bool`

#### `def set_string_property(self, *args)`

#### `def set_binary_string_property(self, name: str, value: Sequence[int]) -> bool`

#### `def set_binary_string_property(self, *args)`

#### `def set_boolean_property(self, name: str, value: bool) -> bool`

#### `def set_boolean_property(self, *args)`

#### `def set_i32_property(self, name: str, value: int) -> bool`

#### `def set_i32_property(self, *args)`

#### `def set_i16_property(self, name: str, value: int) -> bool`

#### `def set_i16_property(self, *args)`

#### `def set_i64_property(self, name: str, value: int) -> bool`

#### `def set_i64_property(self, *args)`

#### `def set_u32_property(self, name: str, value: int) -> bool`

#### `def set_u32_property(self, *args)`

#### `def set_u16_property(self, name: str, value: int) -> bool`

#### `def set_u16_property(self, *args)`

#### `def set_double_property(self, name: str, value: float) -> bool`

#### `def set_double_property(self, *args)`

#### `def set_u64_property(self, name: str, value: int) -> bool`

#### `def set_u64_property(self, *args)`

#### `def set_variant_property(self, name: str, type: Sequence[int], data: Sequence[int]) -> bool`

#### `def set_variant_property(self, *args)`

#### `def set_double_array_property(self, name: str, data: Sequence[float]) -> bool`

#### `def set_double_array_property(self, *args)`

#### `def set_boolean_array_property(self, name: str, data: Sequence[bool]) -> bool`

#### `def set_boolean_array_property(self, *args)`

#### `def set_u64_array_property(self, name: str, data: Sequence[int]) -> bool`

#### `def set_u64_array_property(self, *args)`

#### `def set_u32_array_property(self, name: str, data: Sequence[int]) -> bool`

#### `def set_u32_array_property(self, *args)`

#### `def set_u16_array_property(self, name: str, data: Sequence[int]) -> bool`

#### `def set_u16_array_property(self, *args)`

#### `def set_i64_array_property(self, name: str, data: Sequence[int]) -> bool`

#### `def set_i64_array_property(self, *args)`

#### `def set_i32_array_property(self, name: str, data: Sequence[int]) -> bool`

#### `def set_i32_array_property(self, *args)`

#### `def set_i16_array_property(self, name: str, data: Sequence[int]) -> bool`

#### `def set_i16_array_property(self, *args)`

#### `def set_string_array_property(self, name: str, data: Sequence[str]) -> bool`

#### `def set_string_array_property(self, *args)`

#### `def set_dictionary_property(self, name: str, data: DictionaryProperty) -> bool`

#### `def set_dictionary_property(self, *args)`

#### `def set_dictionary_array_property(self, name: str, data: Sequence[DictionaryProperty]) -> bool`

#### `def set_dictionary_array_property(self, *args)`

#### `def set_dependent_file_value(self, name: str, file_path: str, type: DependentFilePropertyType, version: str, force_download: bool, rt_dest: str, supported_target: str, md5: str) -> bool`

#### `def set_dependent_file_value(self, *args)`

#### `def set_dependent_node_value(self, name: str, node: BaseNodeType) -> bool`

#### `def set_dependent_node_value(self, name: str, node_path: str) -> bool`

#### `def set_dependent_node_value(self, *args)`

#### `def set_data_source_value(self, name: str, node: BaseNodeType) -> bool`

#### `def set_data_source_value(self, name: str, node_path: str) -> bool`

#### `def set_data_source_value(self, *args)`

#### `def get_string_property(self, name: str) -> Tuple[bool, str]`

#### `def get_string_property(self, *args)`

#### `def get_binary_string_property(self, name: str) -> Tuple[bool, Sequence[int]]`

#### `def get_binary_string_property(self, *args)`

#### `def get_boolean_property(self, name: str) -> Tuple[bool, bool]`

#### `def get_boolean_property(self, *args)`

#### `def get_i32_property(self, name: str) -> Tuple[bool, int]`

#### `def get_i32_property(self, *args)`

#### `def get_i16_property(self, name: str) -> Tuple[bool, int]`

#### `def get_i16_property(self, *args)`

#### `def get_i64_property(self, name: str) -> Tuple[bool, int]`

#### `def get_i64_property(self, *args)`

#### `def get_u32_property(self, name: str) -> Tuple[bool, int]`

#### `def get_u32_property(self, *args)`

#### `def get_u16_property(self, name: str) -> Tuple[bool, int]`

#### `def get_u16_property(self, *args)`

#### `def get_double_property(self, name: str) -> Tuple[bool, float]`

#### `def get_double_property(self, *args)`

#### `def get_u64_property(self, name: str) -> Tuple[bool, int]`

#### `def get_u64_property(self, *args)`

#### `def get_variant_value(self, name: str) -> Tuple[bool, Sequence[int], Sequence[int]]`

#### `def get_variant_value(self, *args)`

#### `def get_double_array_property(self, name: str) -> Tuple[bool, Sequence[float]]`

#### `def get_double_array_property(self, *args)`

#### `def get_boolean_array_property(self, name: str) -> Tuple[bool, Sequence[bool]]`

#### `def get_boolean_array_property(self, *args)`

#### `def get_u64_array_property(self, name: str) -> Tuple[bool, Sequence[int]]`

#### `def get_u64_array_property(self, *args)`

#### `def get_u32_array_property(self, name: str) -> Tuple[bool, Sequence[int]]`

#### `def get_u32_array_property(self, *args)`

#### `def get_u16_array_property(self, name: str) -> Tuple[bool, Sequence[int]]`

#### `def get_u16_array_property(self, *args)`

#### `def get_i64_array_property(self, name: str) -> Tuple[bool, Sequence[int]]`

#### `def get_i64_array_property(self, *args)`

#### `def get_i32_array_property(self, name: str) -> Tuple[bool, Sequence[int]]`

#### `def get_i32_array_property(self, *args)`

#### `def get_i16_array_property(self, name: str) -> Tuple[bool, Sequence[int]]`

#### `def get_i16_array_property(self, *args)`

#### `def get_string_array_property(self, name: str) -> Tuple[bool, Sequence[str]]`

#### `def get_string_array_property(self, *args)`

#### `def get_dictionary_property(self, name: str) -> Tuple[bool, DictionaryProperty]`

#### `def get_dictionary_property(self, *args)`

#### `def get_dictionary_array_property(self, name: str) -> Tuple[bool, Sequence[DictionaryProperty]]`

#### `def get_dictionary_array_property(self, *args)`

#### `def get_dependent_node_value_str(self, name: str) -> Tuple[bool, str]`

#### `def get_dependent_node_value_str(self, *args)`

#### `def get_dependent_node_value_basenodetype(self, name: str) -> Tuple[bool, BaseNodeType]`

#### `def get_dependent_node_value_basenodetype(self, *args)`

#### `def get_data_source_node_value_str(self, name: str) -> Tuple[bool, str]`

#### `def get_data_source_node_value_str(self, *args)`

#### `def get_data_source_node_value_basenodetype(self, name: str) -> Tuple[bool, BaseNodeType]`

#### `def get_data_source_node_value_basenodetype(self, *args)`

#### `def get_dependent_file_value(self, name: str) -> Tuple[bool, str, DependentFilePropertyType, str, bool, str, str, str]`

#### `def get_dependent_file_value(self, *args)`

#### `def remove_property(self, name: str) -> bool`

#### `def remove_property(self, *args)`

#### `def clone(self) -> BaseNodeType`

#### `def clone(self, *args)`

#### `def shallow_copy(self) -> BaseNodeType`

#### `def shallow_copy(self, *args)`

#### `def deep_copy(self) -> BaseNodeType`

#### `def deep_copy(self, *args)`

#### `def start_monitoring_dependent(self, dependent: BaseNodeType, id: str)`

#### `def start_monitoring_dependent(self, *args)`

#### `def stop_monitoring_dependent(self, dependent: BaseNodeType, id: str)`

#### `def stop_monitoring_dependent(self, *args)`

#### `def get_observing_nodes(self) -> Iterable[BaseNodeType]`

#### `def get_observing_nodes(self, *args)`

#### `def notify_observing_nodes(self, arg: OnNodeChangeEventArgs)`

#### `def notify_observing_nodes(self, *args)`

#### `def get_enumerator(self) -> System.Collections.IEnumerator`

#### `def get_enumerator(self, *args)`

#### `def _custom_repr(self) -> str`

### `class PropertyContent(_DotNetEnum)`

Type of specialized item that can be contained inside a single propertytype.

#### `def __init__(self, *args)`

Create a new instance.

#### `def K_STRING() -> PropertyContent`

#### `def K_BOOL() -> PropertyContent`

#### `def K_I32() -> PropertyContent`

#### `def K_U32() -> PropertyContent`

#### `def K_DOUBLE() -> PropertyContent`

#### `def K_U64() -> PropertyContent`

#### `def K_VARIANT() -> PropertyContent`

#### `def K_DEPENDENTFILE() -> PropertyContent`

#### `def K_DEPENDENTNODE() -> PropertyContent`

#### `def K_DATASOURCENODE() -> PropertyContent`

#### `def K_U16() -> PropertyContent`

#### `def K_DBLARR() -> PropertyContent`

#### `def K_U32_ARR() -> PropertyContent`

#### `def K_I32_ARR() -> PropertyContent`

#### `def K_STRINGARR() -> PropertyContent`

#### `def K_DICTIONARY() -> PropertyContent`

#### `def K_DICTIONARYARR() -> PropertyContent`

#### `def K_BINARYSTRING() -> PropertyContent`

#### `def K_I16() -> PropertyContent`

#### `def K_I64() -> PropertyContent`

#### `def K_BOOLARR() -> PropertyContent`

#### `def K_U64_ARR() -> PropertyContent`

#### `def K_U16_ARR() -> PropertyContent`

#### `def K_I64_ARR() -> PropertyContent`

#### `def K_I16_ARR() -> PropertyContent`

### `class WaveformTypeDataType(_DotNetEnum)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def DOUBLE() -> WaveformTypeDataType`

#### `def COMPLEX_DOUBLE() -> WaveformTypeDataType`

### `class DocumentType(_DotNetBase)`

Document class that handle serializing the document.

#### `def __init__(self)`

#### `def __init__(self, filepath: str)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def no_namespace_schema_location(self) -> str`

#### `def no_namespace_schema_location(self, value: str)`

#### `def project_version() -> Tuple[int, int, int, int]`

#### `def schema_uri() -> str`

#### `def storage_watcher(self) -> SystemStorageWatcher`

#### `def document_file_path(self) -> str`

Access the document file path.

#### `def document_file_path(self, value: str)`

Access the document file path.

#### `def md5_checksum(self) -> str`

#### `def md5_checksum(self, value: str)`

#### `def version(self) -> VersionType`

#### `def version(self, value: VersionType)`

#### `def content(self) -> DocumentTypeContent`

#### `def content(self, value: DocumentTypeContent)`

#### `def item(self) -> BaseNodeType`

#### `def item(self, value: BaseNodeType)`

#### `def dispose(self)`

#### `def dispose(self, *args)`

#### `def save_system_storage_file(self) -> Tuple[bool, str]`

#### `def save_system_storage_file(self, filepath: str) -> Tuple[bool, str]`

#### `def save_system_storage_file(self, *args)`

#### `def load_system_storage_file(self, filepath: str, schemapath: str) -> Tuple[bool, str]`

#### `def load_system_storage_file(self, filepath: str, schemapath: str, version_to_mutate: Sequence[XMLVersionInfo], xslst_file_paths: Sequence[str]) -> Tuple[bool, str]`

#### `def load_system_storage_file(self, *args)`

#### `def load_project_xml_file(self, filepath: str) -> Tuple[bool, str, bool]`

#### `def load_project_xml_file(self, *args)`

#### `def get_system_definition_file_path(project_file_path: str) -> str`

#### `def get_system_definition_file_path(*args)`

#### `def set_content(self, node: BaseNodeType)`

#### `def set_content(self, *args)`

#### `def get_duplicate_reference(self) -> DocumentType`

#### `def get_duplicate_reference(self, *args)`

#### `def read_version_info(version_tag: str, file_path: str) -> XMLVersionInfo`

#### `def read_version_info(*args)`

### `class VersionType(_DotNetBase)`

#### `def __init__(self)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def major(self) -> int`

#### `def major(self, value: int)`

#### `def minor(self) -> int`

#### `def minor(self, value: int)`

#### `def fix(self) -> int`

#### `def fix(self, value: int)`

#### `def build(self) -> int`

#### `def build(self, value: int)`

### `class DependentFilePropertyType(_DotNetEnum)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def ABSOLUTE() -> DependentFilePropertyType`

#### `def RELATIVE() -> DependentFilePropertyType`

#### `def TO_COMMON_DOC_DIR() -> DependentFilePropertyType`

#### `def TO_APPLICATION_DATA_DIR() -> DependentFilePropertyType`

### `class ErrorEntry(_DotNetBase)`

ErrorEntry represent an error on the basenodetype.

#### `def __init__(self)`

#### `def __init__(self, key: str, is_error: bool, code: int, msg: str)`

#### `def __init__(self, to_copy: ErrorEntry)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def message(self) -> str`

#### `def message(self, value: str)`

#### `def key(self) -> str`

#### `def key(self, value: str)`

#### `def is_error(self) -> bool`

#### `def is_error(self, value: bool)`

#### `def code(self) -> int`

#### `def code(self, value: int)`

#### `def clone(self) -> ErrorEntry`

#### `def clone(self, *args)`

#### `def equals(self, other: ErrorEntry) -> bool`

#### `def equals(self, obj: Any) -> bool`

#### `def equals(self, *args)`

#### `def get_hash_code(self) -> int`

#### `def get_hash_code(self, *args)`

### `class PropertyType(_DotNetBase)`

This class represent a single property of a BaseNodeType.
            The class contains a name of the property and the actual property value.

#### `def __init__(self)`

#### `def __init__(self, to_copy: PropertyType)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def type(self) -> PropertyContent`

Akin to reflection method to return the actual property type.

#### `def item(self) -> Any`

#### `def item(self, value: Any)`

#### `def name(self) -> str`

#### `def name(self, value: str)`

#### `def clone(self) -> PropertyType`

#### `def clone(self, *args)`

#### `def dispose(self)`

#### `def dispose(self, *args)`

#### `def _custom_repr(self) -> str`

### `class NodeType(_DotNetEnum)`

Type of actual node.

#### `def __init__(self, *args)`

Create a new instance.

#### `def K_BASE() -> NodeType`

#### `def K_ALIAS() -> NodeType`

#### `def K_CHANNEL() -> NodeType`

#### `def K_SECTION() -> NodeType`

#### `def K_TARGET() -> NodeType`

#### `def K_TARGETSECTION() -> NodeType`

#### `def K_ROOT() -> NodeType`

#### `def K_WAVEFORM() -> NodeType`

#### `def K_PARAMETER() -> NodeType`

### `class TraversalMode(_DotNetEnum)`

Type of enumeration that is supported when we are traversing the tree of nodes.

#### `def __init__(self, *args)`

Create a new instance.

#### `def K_BFS() -> TraversalMode`

#### `def K_DFS() -> TraversalMode`

#### `def K_CHILDONLY() -> TraversalMode`

#### `def K_UP() -> TraversalMode`

### `class ITraverseNodeFilter(_DotNetBase)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def check_with_filter(self, node: BaseNodeType) -> bool`

#### `def check_with_filter(self, *args)`

### `class IVisitor(_DotNetBase)`

For every type element in the tree declare a visit function for it.

#### `def __init__(self, *args)`

Create a new instance.

#### `def visit(self, element: BaseNodeType)`

#### `def visit(self, element: ChannelType)`

#### `def visit(self, element: SectionType)`

#### `def visit(self, element: AliasType)`

#### `def visit(self, element: ParameterType)`

#### `def visit(self, element: TargetType)`

#### `def visit(self, element: RootType)`

#### `def visit(self, element: TargetSectionsType)`

#### `def visit(self, *args)`

### `class IVisitorWithInspection(_DotNetBase)`

For every type element in the tree declare a visit function for it.
             This is a variant of the visitor function where we allow an object
             to be returned by the visitor class so the caller can do some post-processing
             based on the object value.
             This allows postwalk operation on the tree.

#### `def __init__(self, *args)`

Create a new instance.

#### `def visit(self, element: BaseNodeType) -> IInspectorResult`

#### `def visit(self, element: ChannelType) -> IInspectorResult`

#### `def visit(self, element: SectionType) -> IInspectorResult`

#### `def visit(self, element: AliasType) -> IInspectorResult`

#### `def visit(self, element: ParameterType) -> IInspectorResult`

#### `def visit(self, element: TargetType) -> IInspectorResult`

#### `def visit(self, element: RootType) -> IInspectorResult`

#### `def visit(self, element: TargetSectionsType) -> IInspectorResult`

#### `def visit(self, *args)`

### `class IInspectorResult(_DotNetBase)`

The generic return value that the IVisitorWithInspection support.

#### `def __init__(self, *args)`

Create a new instance.

#### `def result(self) -> Any`

#### `def result(self, *args)`

### `class RootType(BaseNodeType)`

Specialized class that denotes a root of the tree storage.

#### `def __init__(self, node_name: str, type_guid: str)`

#### `def __init__(self, to_copy: RootType)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def target_sections(self) -> TargetSectionsType`

#### `def target_sections(self, value: TargetSectionsType)`

#### `def section(self) -> Sequence[SectionType]`

#### `def section(self, value: Sequence[SectionType])`

#### `def get_owning_document_file_path(self) -> str`

#### `def get_owning_document_file_path(self, *args)`

#### `def refresh_node_dependencies(self)`

#### `def refresh_node_dependencies(self, *args)`

#### `def set_target_section(self, new_target_section: TargetSectionsType) -> bool`

#### `def set_target_section(self, new_target_section: TargetSectionsType, relink: bool) -> bool`

#### `def set_target_section(self, *args)`

#### `def add_multiple_section_type(self, new_nodes: Sequence[SectionType], op: DuplicateOp) -> bool`

#### `def add_multiple_section_type(self, *args)`

#### `def reorder_section_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool`

#### `def reorder_section_type_child_nodes(self, *args)`

#### `def get_section_type_child_nodes(self) -> Sequence[BaseNodeType]`

#### `def get_section_type_child_nodes(self, *args)`

### `class BaseCustomNodeProperty(_DotNetBase)`

Base Class for Property Type that encapsulate basic data type. This
            allow for the class to automatically register the owning BaseNodeType
            to changes that happened to the encapsulated data type.

#### `def __init__(self)`

#### `def __init__(self, to_copy: BaseCustomNodeProperty)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def dispose(self)`

#### `def dispose(self, *args)`

#### `def clone(self) -> BaseCustomNodeProperty`

#### `def clone(self, *args)`

### `class DictionaryProperty(BaseCustomNodeProperty)`

Dictionary property implementation implement cloneable so we can clone property savely.

#### `def __init__(self)`

#### `def __init__(self, to_copy: DictionaryProperty)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def count(self) -> int`

#### `def elem(self) -> Sequence[DictionaryElement]`

#### `def elem(self, value: Sequence[DictionaryElement])`

#### `def clear(self)`

#### `def clear(self, *args)`

#### `def remove_element(self, key: str) -> bool`

#### `def remove_element(self, *args)`

#### `def add_string(self, name: str, value: str) -> bool`

#### `def add_string(self, *args)`

#### `def add_boolean(self, name: str, value: bool) -> bool`

#### `def add_boolean(self, *args)`

#### `def add_i32(self, name: str, value: int) -> bool`

#### `def add_i32(self, *args)`

#### `def add_i16(self, name: str, value: int) -> bool`

#### `def add_i16(self, *args)`

#### `def add_i64(self, name: str, value: int) -> bool`

#### `def add_i64(self, *args)`

#### `def add_u32(self, name: str, value: int) -> bool`

#### `def add_u32(self, *args)`

#### `def add_u16(self, name: str, value: int) -> bool`

#### `def add_u16(self, *args)`

#### `def add_double(self, name: str, value: float) -> bool`

#### `def add_double(self, *args)`

#### `def add_u64(self, name: str, value: int) -> bool`

#### `def add_u64(self, *args)`

#### `def add_arr_double(self, name: str, value: Sequence[float]) -> bool`

#### `def add_arr_double(self, *args)`

#### `def add_arr_boolean(self, name: str, value: Sequence[bool]) -> bool`

#### `def add_arr_boolean(self, *args)`

#### `def add_arr_u64(self, name: str, value: Sequence[int]) -> bool`

#### `def add_arr_u64(self, *args)`

#### `def add_arr_u32(self, name: str, value: Sequence[int]) -> bool`

#### `def add_arr_u32(self, *args)`

#### `def add_arr_u16(self, name: str, value: Sequence[int]) -> bool`

#### `def add_arr_u16(self, *args)`

#### `def add_arr_i64(self, name: str, value: Sequence[int]) -> bool`

#### `def add_arr_i64(self, *args)`

#### `def add_arr_i32(self, name: str, value: Sequence[int]) -> bool`

#### `def add_arr_i32(self, *args)`

#### `def add_arr_i16(self, name: str, value: Sequence[int]) -> bool`

#### `def add_arr_i16(self, *args)`

#### `def add_arr_string(self, name: str, value: Sequence[str]) -> bool`

#### `def add_arr_string(self, *args)`

#### `def get_string(self, name: str) -> Tuple[bool, str]`

#### `def get_string(self, *args)`

#### `def get_bool(self, name: str) -> Tuple[bool, bool]`

#### `def get_bool(self, *args)`

#### `def get_i32(self, name: str) -> Tuple[bool, int]`

#### `def get_i32(self, *args)`

#### `def get_i16(self, name: str) -> Tuple[bool, int]`

#### `def get_i16(self, *args)`

#### `def get_i64(self, name: str) -> Tuple[bool, int]`

#### `def get_i64(self, *args)`

#### `def get_u32(self, name: str) -> Tuple[bool, int]`

#### `def get_u32(self, *args)`

#### `def get_u16(self, name: str) -> Tuple[bool, int]`

#### `def get_u16(self, *args)`

#### `def get_double(self, name: str) -> Tuple[bool, float]`

#### `def get_double(self, *args)`

#### `def get_u64(self, name: str) -> Tuple[bool, int]`

#### `def get_u64(self, *args)`

#### `def get_arr_double(self, name: str) -> Tuple[bool, Sequence[float]]`

#### `def get_arr_double(self, *args)`

#### `def get_arr_boolean(self, name: str) -> Tuple[bool, Sequence[bool]]`

#### `def get_arr_boolean(self, *args)`

#### `def get_arr_u64(self, name: str) -> Tuple[bool, Sequence[int]]`

#### `def get_arr_u64(self, *args)`

#### `def get_arr_u32(self, name: str) -> Tuple[bool, Sequence[int]]`

#### `def get_arr_u32(self, *args)`

#### `def get_arr_u16(self, name: str) -> Tuple[bool, Sequence[int]]`

#### `def get_arr_u16(self, *args)`

#### `def get_arr_i64(self, name: str) -> Tuple[bool, Sequence[int]]`

#### `def get_arr_i64(self, *args)`

#### `def get_arr_i32(self, name: str) -> Tuple[bool, Sequence[int]]`

#### `def get_arr_i32(self, *args)`

#### `def get_arr_i16(self, name: str) -> Tuple[bool, Sequence[int]]`

#### `def get_arr_i16(self, *args)`

#### `def get_arr_string(self, name: str) -> Tuple[bool, Sequence[str]]`

#### `def get_arr_string(self, *args)`

### `class OnNodeChangeEventArgs(_DotNetBase)`

Event data that get send when the node change argument is fired.

#### `def __init__(self, action: str, data: Sequence[int])`

#### `def __init__(self, *args)`

Create a new instance.

#### `def k_deleted() -> str`

#### `def k_error() -> str`

#### `def k_no_error() -> str`

#### `def k_property_changed() -> str`

#### `def k_collection_changed() -> str`

#### `def m_action(self) -> str`

public field to access the action

#### `def m_data(self) -> Sequence[int]`

public field to access the generic data field.

### `class ChannelType(BaseNodeType)`

Specialized class to denote the channel type of the tree storage.

#### `def __init__(self, node_name: str, type_guid: str)`

#### `def __init__(self, to_copy: ChannelType)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def is_readable(self) -> bool`

field to indicate if channel is readable

#### `def is_writable(self) -> bool`

field to indicate if channel is writable

#### `def is_faultable(self) -> bool`

field to indicate if channel is faultable

#### `def is_scalable(self) -> bool`

field to indicate if channel is scalable

#### `def data_length(self) -> int`

return the data length of the channel.

#### `def default_value(self) -> Sequence[float]`

#### `def default_value(self, value: Sequence[float])`

#### `def row_dim(self) -> int`

#### `def row_dim(self, value: int)`

#### `def col_dim(self) -> int`

#### `def col_dim(self, value: int)`

#### `def units(self) -> str`

#### `def units(self, value: str)`

#### `def bit_fields(self) -> int`

#### `def bit_fields(self, value: int)`

#### `def is_under_target(self, target_to_check: TargetType) -> bool`

#### `def is_under_target(self, *args)`

#### `def get_value_table(channel: ChannelType) -> Tuple[bool, Sequence[str], Sequence[float]]`

#### `def get_value_table(*args)`

#### `def set_value_table(channel: ChannelType, names: Sequence[str], values: Sequence[float])`

#### `def set_value_table(*args)`

### `class SystemStorageWatcher(_DotNetBase)`

Public class to abstract the actual watcher node internals.

#### `def __init__(self, *args)`

Create a new instance.

#### `def k_system_storage_watcher_dependentid() -> str`

#### `def error_count(self) -> int`

Gets the current error count

#### `def has_modification(self) -> bool`

#### `def error_in_system(self) -> Sequence[BaseNodeType]`

#### `def has_any_error(self) -> bool`

#### `def reset_modification_flag(self)`

#### `def reset_modification_flag(self, *args)`

#### `def fire_count_event(self)`

#### `def fire_count_event(self, *args)`

#### `def supress_notification(self)`

#### `def supress_notification(self, *args)`

#### `def unsupress_notification(self)`

#### `def unsupress_notification(self, *args)`

#### `def is_node_in_error_collection(self, node: BaseNodeType) -> bool`

#### `def is_node_in_error_collection(self, *args)`

#### `def dispose(self)`

#### `def dispose(self, *args)`

### `class DocumentTypeContent(_DotNetEnum)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def DEFINITION() -> DocumentTypeContent`

#### `def EXPORT() -> DocumentTypeContent`

#### `def SLSC() -> DocumentTypeContent`

### `class SectionType(BaseNodeType)`

Specialized node that implement Section

#### `def __init__(self, node_name: str, type_guid: str)`

#### `def __init__(self, to_copy: SectionType)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def section(self) -> Sequence[SectionType]`

#### `def section(self, value: Sequence[SectionType])`

#### `def channel(self) -> Sequence[ChannelType]`

#### `def channel(self, value: Sequence[ChannelType])`

#### `def alias(self) -> Sequence[AliasType]`

#### `def alias(self, value: Sequence[AliasType])`

#### `def parameter(self) -> Sequence[ParameterType]`

#### `def parameter(self, value: Sequence[ParameterType])`

#### `def waveform(self) -> Sequence[WaveformType]`

#### `def waveform(self, value: Sequence[WaveformType])`

#### `def attached_child_node_without_check(self, node: BaseNodeType)`

#### `def attached_child_node_without_check(self, *args)`

#### `def add_multiple_section_type(self, new_nodes: Sequence[SectionType], op: DuplicateOp) -> bool`

#### `def add_multiple_section_type(self, *args)`

#### `def reorder_section_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool`

#### `def reorder_section_type_child_nodes(self, *args)`

#### `def get_section_type_child_nodes(self) -> Sequence[BaseNodeType]`

#### `def get_section_type_child_nodes(self, *args)`

#### `def add_multiple_channel_type(self, new_nodes: Sequence[ChannelType], op: DuplicateOp) -> bool`

#### `def add_multiple_channel_type(self, *args)`

#### `def reorder_channel_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool`

#### `def reorder_channel_type_child_nodes(self, *args)`

#### `def get_channel_type_child_nodes(self) -> Sequence[BaseNodeType]`

#### `def get_channel_type_child_nodes(self, *args)`

#### `def add_multiple_alias_type(self, new_nodes: Sequence[AliasType], op: DuplicateOp) -> bool`

#### `def add_multiple_alias_type(self, *args)`

#### `def reorder_alias_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool`

#### `def reorder_alias_type_child_nodes(self, *args)`

#### `def get_alias_type_child_nodes(self) -> Sequence[BaseNodeType]`

#### `def get_alias_type_child_nodes(self, *args)`

#### `def add_multiple_parameter_type(self, new_nodes: Sequence[ParameterType], op: DuplicateOp) -> bool`

#### `def add_multiple_parameter_type(self, *args)`

#### `def reorder_parameter_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool`

#### `def reorder_parameter_type_child_nodes(self, *args)`

#### `def get_parameter_type_child_nodes(self) -> Sequence[BaseNodeType]`

#### `def get_parameter_type_child_nodes(self, *args)`

#### `def add_multiple_waveform_type(self, new_nodes: Sequence[WaveformType], op: DuplicateOp) -> bool`

#### `def add_multiple_waveform_type(self, *args)`

#### `def reorder_waveform_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool`

#### `def reorder_waveform_type_child_nodes(self, *args)`

#### `def get_waveform_type_child_nodes(self) -> Sequence[BaseNodeType]`

#### `def get_waveform_type_child_nodes(self, *args)`

### `class AliasType(BaseNodeType)`

Specialized class to denote the alias type of the tree storage.

#### `def __init__(self, node_name: str, type_guid: str)`

#### `def __init__(self, to_copy: AliasType)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def resolve_alias_reference(self) -> BaseNodeType`

Gets the referenced channel.

### `class ParameterType(BaseNodeType)`

Specialized class to denote the parameter type of the tree storage.

#### `def __init__(self, node_name: str, type_guid: str)`

#### `def __init__(self, to_copy: ParameterType)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def row_dim(self) -> int`

#### `def row_dim(self, value: int)`

#### `def col_dim(self) -> int`

#### `def col_dim(self, value: int)`

### `class TargetType(BaseNodeType)`

Specialized node that implement Target

#### `def __init__(self, node_name: str, type_guid: str)`

#### `def __init__(self, to_copy: TargetType)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def dfs_object_enumerator(self) -> System.Collections.IEnumerator`

Return a non generic Depth First Search enumerator. This enumerator iterates into the hiearchy of the
            first children it found.

#### `def section(self) -> Sequence[SectionType]`

#### `def section(self, value: Sequence[SectionType])`

#### `def add_multiple_section_type(self, new_nodes: Sequence[SectionType], op: DuplicateOp) -> bool`

#### `def add_multiple_section_type(self, *args)`

#### `def reorder_section_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool`

#### `def reorder_section_type_child_nodes(self, *args)`

#### `def get_section_type_child_nodes(self) -> Sequence[BaseNodeType]`

#### `def get_section_type_child_nodes(self, *args)`

### `class TargetSectionsType(BaseNodeType)`

Specialized node that implement TargetSections

#### `def __init__(self, node_name: str, type_guid: str)`

#### `def __init__(self, to_copy: TargetSectionsType)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def target(self) -> Sequence[TargetType]`

#### `def target(self, value: Sequence[TargetType])`

#### `def add_multiple_target_type(self, new_nodes: Sequence[TargetType], op: DuplicateOp) -> bool`

#### `def add_multiple_target_type(self, *args)`

#### `def reorder_target_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool`

#### `def reorder_target_type_child_nodes(self, *args)`

#### `def get_target_type_child_nodes(self) -> Sequence[BaseNodeType]`

#### `def get_target_type_child_nodes(self, *args)`

### `class DuplicateOp(_DotNetEnum)`

Operations possible when adding nodes and duplicates are found.

#### `def __init__(self, *args)`

Create a new instance.

#### `def ASSERT() -> DuplicateOp`

#### `def RENAME() -> DuplicateOp`

#### `def UNIQUE_ONLY() -> DuplicateOp`

### `class DictionaryElement(_DotNetBase)`

Dictionary Element implementation implement cloneable so we can clone Dictionary Element savely.

#### `def __init__(self, to_copy: DictionaryElement)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def item(self) -> Any`

#### `def item(self, value: Any)`

#### `def key(self) -> str`

#### `def key(self, value: str)`

#### `def clone(self) -> DictionaryElement`

#### `def clone(self, *args)`

### `class WaveformType(BaseNodeType)`

Specialized class to denote the waveform type of the tree storage.

#### `def __init__(self, node_name: str, type_guid: str, data_type: WaveformTypeDataType)`

#### `def __init__(self, to_copy: WaveformType)`

#### `def __init__(self, *args)`

Create a new instance.

#### `def data_type(self) -> WaveformTypeDataType`

#### `def data_type(self, value: WaveformTypeDataType)`

#### `def units(self) -> str`

#### `def units(self, value: str)`

<!--NI_PYTHON_API repo=niveristand-python path=tests/legacy/test_legacy_alarm2_api.py -->
## PYTHON MODULE: tests/legacy/test_legacy_alarm2_api.py

- `TEST_ID = 12234`

### `def test_alarm2_api()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/legacy/test_legacy_alarm_api.py -->
## PYTHON MODULE: tests/legacy/test_legacy_alarm_api.py

- `TEST_ID = 12234`

### `def test_alarm_api()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/legacy/test_legacy_calc_channel.py -->
## PYTHON MODULE: tests/legacy/test_legacy_calc_channel.py

### `def test_calculated_channel_legacy()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/legacy/test_legacy_calc_channel_formula.py -->
## PYTHON MODULE: tests/legacy/test_legacy_calc_channel_formula.py

### `def test_calculated_channel_formula_legacy()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/legacy/test_legacy_calc_channel_latch.py -->
## PYTHON MODULE: tests/legacy/test_legacy_calc_channel_latch.py

### `def test_calculated_channel_latch_legacy()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/legacy/test_legacy_calc_channel_unit.py -->
## PYTHON MODULE: tests/legacy/test_legacy_calc_channel_unit.py

- `TEST_RESULT = 0`

- `TEST_COMMENT = ''`

### `def test_calculated_channel_ut_legacy()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/legacy/test_legacy_custom_devices.py -->
## PYTHON MODULE: tests/legacy/test_legacy_custom_devices.py

### `def _test_device(workspace, base_name, multiplier)`

### `def test_custom_devices_legacy()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/legacy/test_legacy_expected_profile_failures.py -->
## PYTHON MODULE: tests/legacy/test_legacy_expected_profile_failures.py

### `def wait_for_test(stimulus, wait_time)`

### `def run_test(workspace, stimulus, test_name, wait_time)`

### `def test_expected_profile_failures_legacy()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/legacy/test_legacy_fault_api.py -->
## PYTHON MODULE: tests/legacy/test_legacy_fault_api.py

### `def sleep()`

### `def test_fault_api_legacy()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/legacy/test_legacy_model_manager2_api.py -->
## PYTHON MODULE: tests/legacy/test_legacy_model_manager2_api.py

- `TEST_ID = 1122`

### `def test_model_manager2_legacy()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/legacy/test_legacy_model_manager_api.py -->
## PYTHON MODULE: tests/legacy/test_legacy_model_manager_api.py

- `TEST_ID = 1122`

### `def test_model_manager_legacy()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/legacy/test_legacy_procedures.py -->
## PYTHON MODULE: tests/legacy/test_legacy_procedures.py

- `TEST_ID = 3000`

### `def test_procedures_legacy()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/legacy/test_legacy_reconnect_to_system.py -->
## PYTHON MODULE: tests/legacy/test_legacy_reconnect_to_system.py

### `def test_reconnect_to_system()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/legacy/test_legacy_stimulus_api.py -->
## PYTHON MODULE: tests/legacy/test_legacy_stimulus_api.py

- `TEST_ID = 123213`

### `def test_stimulus_api_legacy()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/legacy/test_legacy_stimulus_step.py -->
## PYTHON MODULE: tests/legacy/test_legacy_stimulus_step.py

### `def wait_for_test(stimulus, wait_time)`

### `def run_test(workspace, stimulus, test_name, wait_time)`

### `def test_stimulus_steps_legacy()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/legacy/test_legacy_workspace2_api.py -->
## PYTHON MODULE: tests/legacy/test_legacy_workspace2_api.py

- `TEST_ID = 124123`

### `def test_workspace2_api()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/legacy/test_legacy_workspace_api.py -->
## PYTHON MODULE: tests/legacy/test_legacy_workspace_api.py

### `def test_workspace_api()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/sdf_api/test_sdf_api.py -->
## PYTHON MODULE: tests/sdf_api/test_sdf_api.py

### MODULE DOCSTRING

Tests the generated python code.

### `def test_no_public_constructor_raises_value_error()`

Runs the test described in the title.

### `def test_incorrect_constructor_args_raises_type_error()`

Runs the test described in the title.

### `def test_const_field_returns_expected_value()`

Runs the test described in the title.

### `def test_static_field_returns_expected_value()`

Runs the test described in the title.

### `def test_instance_field_returns_expected_value()`

Runs the test described in the title.

### `def test_static_property_returns_expected_value()`

Runs the test described in the title.

### `def test_instance_property_returns_expected_value()`

Runs the test described in the title.

### `def test_instance_property_setter_sets_the_value()`

Runs the test described in the title.

### `def test_static_method_returns_expected_value()`

Runs the test described in the title.

### `def test_instance_method_returns_expected_value()`

Runs the test described in the title.

### `def test_eq_type()`

Runs the test described in the title.

### `def test_eq_enum()`

Runs the test described in the title.

### `def test_eq_enum_none_value()`

Runs the test described in the title.

### `def test_repr_type()`

Runs the test described in the title.

### `def test_str_type()`

Runs the test described in the title.

### `def test_repr_enum()`

Runs the test described in the title.

### `def test_str_enum()`

Runs the test described in the title.

### `def test_int_enum()`

Runs the test described in the title.

### `def test_property_returns_python_enum_repr_does_not_raise_error()`

Runs the test described in the title.

### `def test_property_returns_python_enum_with_proper_repr()`

Runs the test described in the title.

<!--NI_PYTHON_API repo=niveristand-python path=tests/sdf_api/test_sdf_api__out_param_types.py -->
## PYTHON MODULE: tests/sdf_api/test_sdf_api__out_param_types.py

### MODULE DOCSTRING

Tests the generated python code all different `out` types.

### `def test_out_bool_param()`

Runs the test described in the title.

### `def test_out_double_param()`

Runs the test described in the title.

### `def test_out_uint16_param()`

Runs the test described in the title.

### `def test_out_uint32_param()`

Runs the test described in the title.

### `def test_out_uint64_param()`

Runs the test described in the title.

### `def test_out_int16_param()`

Runs the test described in the title.

### `def test_out_int32_param()`

Runs the test described in the title.

### `def test_out_int64_param()`

Runs the test described in the title.

### `def test_out_str_param()`

Runs the test described in the title.

### `def test_differs_only_by_out_str()`

Runs the test described in the title.

### `def _assert_dictionary_array(expected_array: Sequence[Any], actual_result: Tuple[bool, Any])`

### `def test_out_sequence_of_bool_param()`

Runs the test described in the title.

### `def test_out_sequence_of_double_param()`

Runs the test described in the title.

### `def test_out_sequence_of_uint16_param()`

Runs the test described in the title.

### `def test_out_sequence_of_uint32_param()`

Runs the test described in the title.

### `def test_out_sequence_of_uint64_param()`

Runs the test described in the title.

### `def test_out_sequence_of_int16_param()`

Runs the test described in the title.

### `def test_out_sequence_of_int32_param()`

Runs the test described in the title.

### `def test_out_sequence_of_int64_param()`

Runs the test described in the title.

### `def test_out_sequence_of_str_param()`

Runs the test described in the title.

### `def test_out_BaseNode_param()`

Runs the test described in the title.

<!--NI_PYTHON_API repo=niveristand-python path=tests/sdf_api/test_sdf_api__overloads.py -->
## PYTHON MODULE: tests/sdf_api/test_sdf_api__overloads.py

### MODULE DOCSTRING

Tests the generated python code for method overload resolution.

### `def test_out_empty_sequence_resolves()`

Runs the test described in the title.

### `def test_error_out_parameter_given_success_condition_does_not_throw()`

Runs the test described in the title.

### `def test_error_out_parameter_given_error_condition_throws_error()`

Runs the test described in the title.

### `def _add_new_alarm(target: Target)`

### `def test_add_new_alarm_given_success_condition_does_not_throw()`

Runs the test described in the title.

### `def test_add_new_alarm_given_error_condition_throws_error()`

Runs the test described in the title.

### `def test_non_final_out_error_param()`

Runs the test described in the title.

### `def test_get_node_errors_given_success_condition_returns_empty_list()`

Runs the test described in the title.

### `def test_get_node_errors_given_error_condition_throws_error()`

Runs the test described in the title.

### `def test_method_overload_only_differs_by_str_out_parameter_false_case()`

Runs the test described in the title.

### `def test_method_overload_only_differs_by_str_out_parameter_true_case()`

Runs the test described in the title.

### `def test_method_overload_only_differs_by_BaseNode_out_parameter_false_case()`

Runs the test described in the title.

### `def test_method_overload_only_differs_by_BaseNode_out_parameter_true_case()`

Runs the test described in the title.

<!--NI_PYTHON_API repo=niveristand-python path=tests/sdf_api/test_sdf_api__overloads__save_sdf.py -->
## PYTHON MODULE: tests/sdf_api/test_sdf_api__overloads__save_sdf.py

### MODULE DOCSTRING

Tests the generated python code for method overload resolution.

### `def test_save_system_definition_file_same_filename()`

Runs the test described in the title.

### `def test_save_system_definition_file_different_filename()`

Runs the test described in the title.

<!--NI_PYTHON_API repo=niveristand-python path=tests/sdf_api/test_sdf_api__unwrap.py -->
## PYTHON MODULE: tests/sdf_api/test_sdf_api__unwrap.py

### MODULE DOCSTRING

Tests the generated python code for AB#2359562: Unwrap wrapped types...

### `def test_property_settter_enum_passed()`

Runs the test described in the title.

### `def test_property_setter_does_not_unwrap_primitive_element()`

Runs the test described in the title.

### `def test_property_setter_unwraps_veristand_elements()`

Runs the test described in the title.

### `def test_property_setter_unwraps_to_dotnet_generic_list_of_veristand_elements()`

Runs the test described in the title.

### `def test_property_setter_unwraps_sequence_of_veristand_elements()`

Runs the test described in the title.

### `def test_property_setter_passes_empty_sequence_of_veristand_elements()`

Runs the test described in the title.

### `def test_property_setter_passes_2d_dotnet_array()`

Runs the test described in the title.

### `def test_property_setter_2d_array_given_sequence_raises_type_error()`

Runs the test described in the title.

### `def test_method_enum_passed()`

Runs the test described in the title.

### `def test_method_unwraps_only_veristand_elements()`

Runs the test described in the title.

### `def test_method_unwraps_sequence_of_veristand_elements()`

Runs the test described in the title.

### `def test_method_unwraps_ienumerable_of_veristand_elements()`

Runs the test described in the title.

### `def test_method_passes_empty_sequence_of_veristand_elements()`

Runs the test described in the title.

### `def test_constructor_enum_passed()`

Runs the test described in the title.

### `def test_constructor_mix_of_primitive_and_veristand_types_are_properly_passed()`

Runs the test described in the title.

### `def test_constructor_does_not_unwrap_primitive_element()`

Runs the test described in the title.

### `def test_constructor_unwraps_sequence_of_veristand_elements()`

Runs the test described in the title.

### `def test_constructor_passes_empty_sequence_of_veristand_elements()`

Runs the test described in the title.

### `def test_constructor_unwraps_four_tuple_version()`

Runs the test described in the title.

### `def test_constructor_does_not_unwrap_four_tuple_if_not_version()`

Runs the test described in the title.

<!--NI_PYTHON_API repo=niveristand-python path=tests/sdf_api/test_sdf_api__wrap.py -->
## PYTHON MODULE: tests/sdf_api/test_sdf_api__wrap.py

### MODULE DOCSTRING

Tests the generated python code for return value wrapping.

### `def test_enum_returns_its_value()`

Runs the test described in the title.

### `def test_nested_enum_returns_its_value()`

Runs the test described in the title.

### `def test_property_base_type_return_value_returns_derived_type()`

Runs the test described in the title.

### `def test_property_sequence_of_base_type_return_value_returns_derived_types()`

Runs the test described in the title.

### `def test_property_return_of_primitive_element_is_not_wrapped()`

Runs the test described in the title.

### `def test_property_return_of_sequence_of_primitive_elements_none_are_wrapped()`

Runs the test described in the title.

### `def test_property_return_of_sequence_of_veristand_elements_all_are_wrapped()`

Runs the test described in the title.

### `def test_property_returns_python_enum()`

Runs the test described in the title.

### `def test_property_returns_version()`

Runs the test described in the title.

### `def test_property_returns_2d_array()`

Runs the test described in the title.

### `def test_method_base_type_return_value_returns_derived_type()`

Runs the test described in the title.

### `def test_method_sequence_of_base_type_return_value_returns_derived_types()`

Runs the test described in the title.

### `def test_method_return_of_primitive_element_is_not_wrapped()`

Runs the test described in the title.

### `def test_method_return_of_veristand_element_is_wrapped()`

Runs the test described in the title.

### `def test_method_return_of_sequence_of_primitive_elements_none_are_wrapped()`

Runs the test described in the title.

### `def test_method_return_of_sequence_of_veristand_elements_all_are_wrapped()`

Runs the test described in the title.

### `def test_method_void_return_primitive_out_only_out_returned()`

Runs the test described in the title.

### `def test_method_return_of_ienumerable_of_veristand_elements_all_are_wrapped()`

Runs the test described in the title.

### `def test_method_returns_version()`

Runs the test described in the title.

<!--NI_PYTHON_API repo=niveristand-python path=tests/setup/test_run_sequence.py -->
## PYTHON MODULE: tests/setup/test_run_sequence.py

### `def simple()`

### `def test_run_simple()`

### `def test_call_assert_helper()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/setup/test_validatesetup.py -->
## PYTHON MODULE: tests/setup/test_validatesetup.py

### `def _inc(x)`

### `def test_pass()`

Just make sure asserts work.

### `def test_pythonnetworks()`

### `def test_binariesfound()`

### `def test_getinstalledbinariespath()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_arithmetic_shift_left.py -->
## PYTHON MODULE: tests/test_arithmetic_shift_left.py

### `def _return_constant()`

### `def arithmetic_shift_left_simple_numbers()`

### `def arithmetic_shift_left_num_nivsdatatype()`

### `def arithmetic_shift_left_nivsdatatype_nivsdatatype()`

### `def arithmetic_shift_left_nivsdatatype_nivsdatatype1()`

### `def arithmetic_shift_left_nivsdatatype_nivsdatatype2()`

### `def arithmetic_shift_left_nivsdatatype_nivsdatatype3()`

### `def arithmetic_shift_left_multiple_types()`

### `def arithmetic_shift_left_multiple_types1()`

### `def arithmetic_shift_left_use_rtseq()`

### `def arithmetic_shift_left_use_rtseq1()`

### `def arithmetic_shift_left_use_rtseq2()`

### `def arithmetic_shift_left_use_rtseq3()`

### `def arithmetic_shift_left_use_rtseq4()`

### `def arithmetic_shift_left_use_rtseq5()`

### `def arithmetic_shift_left_with_parentheses()`

### `def arithmetic_shift_left_with_parentheses1()`

### `def arithmetic_shift_left_with_parentheses2()`

### `def arithmetic_shift_left_variables()`

### `def arithmetic_shift_left_variables1()`

### `def arithmetic_shift_left_variable_variable()`

### `def arithmetic_shift_left_variable_variable1()`

### `def arithmetic_shift_left_variable_rtseq()`

### `def arithmetic_shift_left_variable_rtseq1()`

### `def arithmetic_shift_left_to_channel_ref()`

### `def arithmetic_shift_left_binary_unary()`

### `def arithmetic_shift_left_augassign_number()`

### `def arithmetic_shift_left_augassign_nivsdatatype()`

### `def arithmetic_shift_left_augassign_nivsdatatype1()`

### `def arithmetic_shift_left_augassign_nivsdatatype2()`

### `def arithmetic_shift_left_augassign_nivsdatatype3()`

### `def arithmetic_shift_left_augassign_nivsdatatype4()`

### `def arithmetic_shift_left_augassign_variable()`

### `def arithmetic_shift_left_augassign_variable1()`

### `def arithmetic_shift_left_augassign_variable2()`

### `def arithmetic_shift_left_augassign_variable3()`

### `def arithmetic_shift_left_augassign_variable4()`

### `def arithmetic_shift_left_augassign_rtseq()`

### `def arithmetic_shift_left_augassign_parentheses()`

### `def arithmetic_shift_left_augassign_channel_ref()`

### `def arithmetic_shift_left_invalid_variables()`

### `def arithmetic_shift_left_invalid_variables1()`

### `def arithmetic_shift_left_to_None()`

### `def arithmetic_shift_left_invalid_rtseq_call()`

### `def arithmetic_shift_left_complex_expr()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_arithmetic_shift_right.py -->
## PYTHON MODULE: tests/test_arithmetic_shift_right.py

### `def _return_constant()`

### `def arithmetic_shift_right_simple_numbers()`

### `def arithmetic_shift_right_num_nivsdatatype()`

### `def arithmetic_shift_right_nivsdatatype_nivsdatatype()`

### `def arithmetic_shift_right_nivsdatatype_nivsdatatype1()`

### `def arithmetic_shift_right_nivsdatatype_nivsdatatype2()`

### `def arithmetic_shift_right_nivsdatatype_nivsdatatype3()`

### `def arithmetic_shift_right_multiple_types()`

### `def arithmetic_shift_right_multiple_types1()`

### `def arithmetic_shift_right_use_rtseq()`

### `def arithmetic_shift_right_use_rtseq1()`

### `def arithmetic_shift_right_use_rtseq2()`

### `def arithmetic_shift_right_use_rtseq3()`

### `def arithmetic_shift_right_use_rtseq4()`

### `def arithmetic_shift_right_use_rtseq5()`

### `def arithmetic_shift_right_with_parentheses()`

### `def arithmetic_shift_right_with_parentheses1()`

### `def arithmetic_shift_right_with_parentheses2()`

### `def arithmetic_shift_right_variables()`

### `def arithmetic_shift_right_variables1()`

### `def arithmetic_shift_right_variable_variable()`

### `def arithmetic_shift_right_variable_variable1()`

### `def arithmetic_shift_right_variable_rtseq()`

### `def arithmetic_shift_right_variable_rtseq1()`

### `def arithmetic_shift_right_to_channel_ref()`

### `def arithmetic_shift_right_binary_unary()`

### `def arithmetic_shift_right_augassign_number()`

### `def arithmetic_shift_right_augassign_nivsdatatype()`

### `def arithmetic_shift_right_augassign_nivsdatatype1()`

### `def arithmetic_shift_right_augassign_nivsdatatype2()`

### `def arithmetic_shift_right_augassign_nivsdatatype3()`

### `def arithmetic_shift_right_augassign_nivsdatatype4()`

### `def arithmetic_shift_right_augassign_variable()`

### `def arithmetic_shift_right_augassign_variable1()`

### `def arithmetic_shift_right_augassign_variable2()`

### `def arithmetic_shift_right_augassign_variable3()`

### `def arithmetic_shift_right_augassign_variable4()`

### `def arithmetic_shift_right_augassign_rtseq()`

### `def arithmetic_shift_left_augassign_parentheses()`

### `def arithmetic_shift_right_augassign_channel_ref()`

### `def arithmetic_shift_right_invalid_variables()`

### `def arithmetic_shift_right_invalid_variables1()`

### `def arithmetic_shift_right_to_None()`

### `def arithmetic_shift_right_invalid_rtseq_call()`

### `def arithmetic_shift_right_complex_expr()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_binaryop_add.py -->
## PYTHON MODULE: tests/test_binaryop_add.py

### `def _return_constant()`

### `def add_simple_numbers()`

### `def add_num_nivsdatatype()`

### `def add_nivsdatatype_nivsdatatype()`

### `def add_nivsdatatype_nivsdatatype1()`

### `def add_nivsdatatype_nivsdatatype2()`

### `def add_nivsdatatype_nivsdatatype3()`

### `def add_multiple_types()`

### `def add_multiple_types1()`

### `def add_use_rtseq()`

### `def add_use_rtseq1()`

### `def add_use_rtseq2()`

### `def add_use_rtseq3()`

### `def add_use_rtseq4()`

### `def add_use_rtseq5()`

### `def add_with_parentheses()`

### `def add_with_parentheses1()`

### `def add_with_parentheses2()`

### `def add_variables()`

### `def add_variables1()`

### `def add_variable_variable()`

### `def add_variable_variable1()`

### `def add_variable_rtseq()`

### `def add_variable_rtseq1()`

### `def add_to_channel_ref()`

### `def add_binary_unary()`

### `def add_with_multiple_plus()`

### `def add_with_multiple_plus1()`

### `def add_binary_unary_sequence()`

### `def add_complex_expr()`

### `def aug_add_simple_numbers()`

### `def aug_add_num_nivsdatatype()`

### `def aug_add_use_rtseq()`

### `def aug_add_with_parentheses()`

### `def aug_add_variables()`

### `def aug_add_to_channel_ref()`

### `def aug_add_unary()`

### `def add_invalid_variables()`

### `def add_invalid_variables1()`

### `def add_to_None()`

### `def add_invalid_rtseq_call()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_binaryop_div.py -->
## PYTHON MODULE: tests/test_binaryop_div.py

### `def _return_constant()`

### `def div_simple_numbers()`

### `def div_num_nivsdatatype()`

### `def div_nivsdatatype_nivsdatatype()`

### `def div_nivsdatatype_nivsdatatype1()`

### `def div_nivsdatatype_nivsdatatype2()`

### `def div_nivsdatatype_nivsdatatype3()`

### `def div_multiple_types()`

### `def div_multiple_types1()`

### `def div_use_rtseq()`

### `def div_use_rtseq1()`

### `def div_use_rtseq2()`

### `def div_use_rtseq3()`

### `def div_use_rtseq4()`

### `def div_use_rtseq5()`

### `def div_with_parentheses()`

### `def div_with_parentheses1()`

### `def div_with_parentheses2()`

### `def div_variables()`

### `def div_variables1()`

### `def div_variable_variable()`

### `def div_variable_variable1()`

### `def div_variable_rtseq()`

### `def div_variable_rtseq1()`

### `def div_with_channel_ref()`

### `def div_binary_unary()`

### `def div_complex_expr()`

### `def aug_div_simple_numbers()`

### `def aug_div_num_nivsdatatype()`

### `def aug_div_use_rtseq()`

### `def aug_div_with_parentheses()`

### `def aug_div_variables()`

### `def aug_div_to_channel_ref()`

### `def aug_div_unary()`

### `def div_invalid_variables()`

### `def div_invalid_variables1()`

### `def div_with_None()`

### `def div_invalid_rtseq_call()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_binaryop_modulo.py -->
## PYTHON MODULE: tests/test_binaryop_modulo.py

### `def _return_constant()`

### `def modulo_simple_numbers()`

### `def modulo_num_nivsdatatype()`

### `def modulo_nivsdatatype_nivsdatatype()`

### `def modulo_nivsdatatype_nivsdatatype1()`

### `def modulo_nivsdatatype_nivsdatatype2()`

### `def modulo_nivsdatatype_nivsdatatype3()`

### `def modulo_multiple_types()`

### `def modulo_multiple_types1()`

### `def modulo_use_rtseq()`

### `def modulo_use_rtseq1()`

### `def modulo_use_rtseq2()`

### `def modulo_use_rtseq3()`

### `def modulo_use_rtseq4()`

### `def modulo_use_rtseq5()`

### `def modulo_with_parentheses()`

### `def modulo_with_parentheses1()`

### `def modulo_with_parentheses2()`

### `def modulo_with_parentheses3()`

### `def modulo_with_parentheses4()`

### `def modulo_with_parentheses5()`

### `def modulo_with_parentheses6()`

### `def modulo_with_parentheses7()`

### `def modulo_variables()`

### `def modulo_variables1()`

### `def modulo_variable_variable()`

### `def modulo_variable_variable1()`

### `def modulo_variable_rtseq()`

### `def modulo_variable_rtseq1()`

### `def modulo_with_channel_ref()`

### `def modulo_binary_unary()`

### `def modulo_complex_expr()`

### `def aug_modulo_simple_numbers()`

### `def aug_modulo_num_nivsdatatype()`

### `def aug_modulo_use_rtseq()`

### `def aug_modulo_with_parentheses()`

### `def aug_modulo_variables()`

### `def aug_modulo_to_channel_ref()`

### `def aug_modulo_unary()`

### `def modulo_invalid_variables()`

### `def modulo_invalid_variables1()`

### `def modulo_with_None()`

### `def modulo_invalid_rtseq_call()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_binaryop_mult.py -->
## PYTHON MODULE: tests/test_binaryop_mult.py

### `def _return_constant()`

### `def mult_simple_numbers()`

### `def mult_num_nivsdatatype()`

### `def mult_nivsdatatype_nivsdatatype()`

### `def mult_nivsdatatype_nivsdatatype1()`

### `def mult_nivsdatatype_nivsdatatype2()`

### `def mult_nivsdatatype_nivsdatatype3()`

### `def mult_multiple_types()`

### `def mult_multiple_types1()`

### `def mult_use_rtseq()`

### `def mult_use_rtseq1()`

### `def mult_use_rtseq2()`

### `def mult_use_rtseq3()`

### `def mult_use_rtseq4()`

### `def mult_use_rtseq5()`

### `def mult_with_parentheses()`

### `def mult_with_parentheses1()`

### `def mult_with_parentheses2()`

### `def mult_variables()`

### `def mult_variables1()`

### `def mult_variable_variable()`

### `def mult_variable_variable1()`

### `def mult_variable_rtseq()`

### `def mult_variable_rtseq1()`

### `def mult_with_channel_ref()`

### `def mult_binary_unary()`

### `def mult_complex_expr()`

### `def aug_mult_simple_numbers()`

### `def aug_mult_num_nivsdatatype()`

### `def aug_mult_use_rtseq()`

### `def aug_mult_with_parentheses()`

### `def aug_mult_variables()`

### `def aug_mult_to_channel_ref()`

### `def aug_mult_unary()`

### `def mult_invalid_variables()`

### `def mult_invalid_variables1()`

### `def mult_with_None()`

### `def mult_invalid_rtseq_call()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_binaryop_pow.py -->
## PYTHON MODULE: tests/test_binaryop_pow.py

### `def _return_constant()`

### `def exp_simple_numbers()`

### `def exp_num_nivsdatatype()`

### `def exp_nivsdatatype_nivsdatatype()`

### `def exp_nivsdatatype_nivsdatatype1()`

### `def exp_nivsdatatype_nivsdatatype2()`

### `def exp_nivsdatatype_nivsdatatype3()`

### `def exp_use_rtseq()`

### `def exp_use_rtseq1()`

### `def exp_use_rtseq2()`

### `def exp_use_rtseq3()`

### `def exp_use_rtseq4()`

### `def exp_use_rtseq5()`

### `def exp_with_parentheses()`

### `def exp_with_parentheses1()`

### `def exp_with_parentheses2()`

### `def exp_variables()`

### `def exp_variables1()`

### `def exp_variable_variable()`

### `def exp_variable_variable1()`

### `def exp_variable_rtseq()`

### `def exp_variable_rtseq1()`

### `def exp_with_channel_ref()`

### `def exp_binary_unary()`

### `def exp_complex_expr()`

### `def aug_exp_simple_numbers()`

### `def aug_exp_num_nivsdatatype()`

### `def aug_exp_use_rtseq()`

### `def aug_exp_with_parentheses()`

### `def aug_exp_variables()`

### `def aug_exp_to_channel_ref()`

### `def aug_exp_unary()`

### `def exp_invalid_variables()`

### `def exp_invalid_variables1()`

### `def exp_with_None()`

### `def exp_invalid_rtseq_call()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_binaryop_sub.py -->
## PYTHON MODULE: tests/test_binaryop_sub.py

### `def _return_constant()`

### `def sub_simple_numbers()`

### `def test_sub_simple_numbers()`

### `def sub_num_nivsdatatype()`

### `def sub_nivsdatatype_nivsdatatype()`

### `def sub_nivsdatatype_nivsdatatype1()`

### `def sub_nivsdatatype_nivsdatatype2()`

### `def sub_nivsdatatype_nivsdatatype3()`

### `def sub_multiple_types()`

### `def sub_multiple_types1()`

### `def sub_use_rtseq()`

### `def sub_use_rtseq1()`

### `def sub_use_rtseq2()`

### `def sub_use_rtseq3()`

### `def sub_use_rtseq4()`

### `def sub_use_rtseq5()`

### `def sub_with_parentheses()`

### `def sub_with_parentheses1()`

### `def sub_with_parentheses2()`

### `def sub_variables()`

### `def sub_variables1()`

### `def sub_variable_variable()`

### `def sub_variable_variable1()`

### `def sub_variable_rtseq()`

### `def sub_variable_rtseq1()`

### `def sub_to_channel_ref()`

### `def sub_binary_unary()`

### `def sub_binary_unary_sequence()`

### `def sub_complex_expr()`

### `def aug_sub_simple_numbers()`

### `def aug_sub_num_nivsdatatype()`

### `def aug_sub_use_rtseq()`

### `def aug_sub_with_parentheses()`

### `def aug_sub_variables()`

### `def aug_sub_to_channel_ref()`

### `def aug_sub_unary()`

### `def sub_invalid_variables()`

### `def sub_invalid_variables1()`

### `def sub_from_None()`

### `def sub_invalid_rtseq_call()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_bitwise_and.py -->
## PYTHON MODULE: tests/test_bitwise_and.py

### `def _return_constant()`

### `def bitwise_and_simple_numbers()`

### `def bitwise_and_num_nivsdatatype()`

### `def bitwise_and_nivsdatatype_nivsdatatype()`

### `def bitwise_and_nivsdatatype_nivsdatatype1()`

### `def bitwise_and_nivsdatatype_nivsdatatype2()`

### `def bitwise_and_nivsdatatype_nivsdatatype3()`

### `def bitwise_and_multiple_types()`

### `def bitwise_and_multiple_types1()`

### `def bitwise_and_use_rtseq()`

### `def bitwise_and_use_rtseq1()`

### `def bitwise_and_use_rtseq2()`

### `def bitwise_and_use_rtseq3()`

### `def bitwise_and_with_parentheses()`

### `def bitwise_and_with_parentheses1()`

### `def bitwise_and_with_parentheses2()`

### `def bitwise_and_variables()`

### `def bitwise_and_variables1()`

### `def bitwise_and_variable_variable()`

### `def bitwise_and_variable_variable1()`

### `def bitwise_and_variable_rtseq()`

### `def bitwise_and_variable_rtseq1()`

### `def bitwise_and_to_channel_ref()`

### `def bitwise_and_binary_unary()`

### `def bitwise_and_complex_expr()`

### `def aug_bitwise_and_simple_numbers()`

### `def aug_bitwise_and_num_nivsdatatype()`

### `def aug_bitwise_and_use_rtseq()`

### `def aug_bitwise_and_with_parentheses()`

### `def aug_bitwise_and_variables()`

### `def aug_bitwise_and_to_channel_ref()`

### `def aug_bitwise_and_unary()`

### `def bitwise_and_invalid_variables()`

### `def bitwise_and_invalid_variables1()`

### `def bitwise_and_to_None()`

### `def bitwise_and_invalid_rtseq_call()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_bitwise_or.py -->
## PYTHON MODULE: tests/test_bitwise_or.py

### `def _return_constant()`

### `def bitwise_or_simple_numbers()`

### `def bitwise_or_num_nivsdatatype()`

### `def bitwise_or_nivsdatatype_nivsdatatype()`

### `def bitwise_or_nivsdatatype_nivsdatatype1()`

### `def bitwise_or_nivsdatatype_nivsdatatype2()`

### `def bitwise_or_nivsdatatype_nivsdatatype3()`

### `def bitwise_or_multiple_types()`

### `def bitwise_or_multiple_types1()`

### `def bitwise_or_use_rtseq()`

### `def bitwise_or_use_rtseq1()`

### `def bitwise_or_use_rtseq2()`

### `def bitwise_or_use_rtseq3()`

### `def bitwise_or_with_parentheses()`

### `def bitwise_or_with_parentheses1()`

### `def bitwise_or_with_parentheses2()`

### `def bitwise_or_variables()`

### `def bitwise_or_variables1()`

### `def bitwise_or_variable_variable()`

### `def bitwise_or_variable_variable1()`

### `def bitwise_or_variable_rtseq()`

### `def bitwise_or_variable_rtseq1()`

### `def bitwise_or_to_channel_ref()`

### `def bitwise_or_binary_unary()`

### `def bitwise_or_complex_expr()`

### `def aug_bitwise_or_simple_numbers()`

### `def aug_bitwise_or_num_nivsdatatype()`

### `def aug_bitwise_or_use_rtseq()`

### `def aug_bitwise_or_with_parentheses()`

### `def aug_bitwise_or_variables()`

### `def aug_bitwise_or_to_channel_ref()`

### `def aug_bitwise_or_unary()`

### `def bitwise_or_invalid_variables()`

### `def bitwise_or_invalid_variables1()`

### `def bitwise_or_to_None()`

### `def bitwise_or_invalid_rtseq_call()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_bitwise_xor.py -->
## PYTHON MODULE: tests/test_bitwise_xor.py

### `def _return_constant()`

### `def bitwise_xor_simple_numbers()`

### `def bitwise_xor_num_nivsdatatype()`

### `def bitwise_xor_nivsdatatype_nivsdatatype()`

### `def bitwise_xor_nivsdatatype_nivsdatatype1()`

### `def bitwise_xor_nivsdatatype_nivsdatatype2()`

### `def bitwise_xor_nivsdatatype_nivsdatatype3()`

### `def bitwise_xor_multiple_types()`

### `def bitwise_xor_multiple_types1()`

### `def bitwise_xor_use_rtseq()`

### `def bitwise_xor_use_rtseq1()`

### `def bitwise_xor_use_rtseq2()`

### `def bitwise_xor_use_rtseq3()`

### `def bitwise_xor_with_parentheses()`

### `def bitwise_xor_with_parentheses1()`

### `def bitwise_xor_with_parentheses2()`

### `def bitwise_xor_variables()`

### `def bitwise_xor_variables1()`

### `def bitwise_xor_variable_variable()`

### `def bitwise_xor_variable_variable1()`

### `def bitwise_xor_variable_rtseq()`

### `def bitwise_xor_variable_rtseq1()`

### `def bitwise_xor_to_channel_ref()`

### `def bitwise_xor_binary_unary()`

### `def bitwise_xor_complex_expr()`

### `def aug_bitwise_xor_simple_numbers()`

### `def aug_bitwise_xor_num_nivsdatatype()`

### `def aug_bitwise_xor_use_rtseq()`

### `def aug_bitwise_xor_with_parentheses()`

### `def aug_bitwise_xor_variables()`

### `def aug_bitwise_xor_to_channel_ref()`

### `def aug_bitwise_xor_unary()`

### `def bitwise_xor_invalid_variables()`

### `def bitwise_xor_invalid_variables1()`

### `def bitwise_xor_to_None()`

### `def bitwise_xor_invalid_rtseq_call()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_builtin_math_functions.py -->
## PYTHON MODULE: tests/test_builtin_math_functions.py

### `def _return_constant()`

### `def abs_simple_number()`

### `def abs_nivsdatatype_value()`

### `def abs_nivsdatatype()`

### `def abs_nivsdatatype1()`

### `def abs_nivsdatatype2()`

### `def abs_nivsdatatype3()`

### `def abs_nivsdatatype4()`

### `def abs_nivsdatatype5()`

### `def abs_variable_double()`

### `def abs_variable_i32()`

### `def abs_variable_i64()`

### `def abs_variable_u32()`

### `def abs_variable_u64()`

### `def abs_variable_boolean()`

### `def abs_channel_ref()`

### `def abs_call_rtseq()`

### `def abs_expr()`

### `def abs_expr_parentheses()`

### `def abs_ifexpr()`

### `def abs_builtin()`

### `def acos_double()`

### `def acosh_double()`

### `def asin_double()`

### `def asinh_double()`

### `def atan_double()`

### `def atan2_double()`

### `def atanh_double()`

### `def ceil_double()`

### `def ceil_double_negative()`

### `def cos_double()`

### `def cosh_double()`

### `def exp_double()`

### `def expm1_double()`

### `def floor_double()`

### `def hypot_double()`

### `def isnan_double()`

### `def ln_double()`

### `def lnp1_double()`

### `def log_double()`

### `def log10_double()`

### `def log2_double()`

### `def max_double()`

### `def min_double()`

### `def mod_double()`

### `def pow_double()`

### `def round_double()`

### `def sin_double()`

### `def sinh_double()`

### `def sqrt_double()`

### `def tan_double()`

### `def tanh_double()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_builtin_veristand_functions.py -->
## PYTHON MODULE: tests/test_builtin_veristand_functions.py

### `def call_abstime()`

### `def call_arraysize()`

### `def call_clearfault()`

### `def call_clearlasterror()`

### `def call_deltat()`

### `def call_deltatus()`

### `def call_fault()`

### `def call_fix()`

### `def call_getlasterror()`

### `def call_iteration()`

### `def call_quotient()`

### `def call_recip()`

### `def call_rem()`

### `def call_seqtime()`

### `def call_seqtimeus()`

### `def call_tickcountms()`

### `def call_tickcountus()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_call_nested_rtsequence.py -->
## PYTHON MODULE: tests/test_call_nested_rtsequence.py

### `def nested_sequence()`

### `def call_nested_sequence_after()`

### `def call_nested_sequence_before()`

### `def call_nested_sequence_twice()`

### `def call_complex_nested_sequences()`

### `def idfunc(val)`

### `def test_run_py_as_rts(func_name)`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_channel_refs.py -->
## PYTHON MODULE: tests/test_channel_refs.py

### `def test_channel_ref_type_string()`

### `def test_channel_ref_setter()`

### `def test_channel_ref_return()`

### `def test_channel_ref_run()`

### `def test_channel_ref_run_python()`

### `def test_channel_ref_invalid_channel_set()`

### `def test_channel_ref_invalid_channel_get()`

### `def test_channel_ref_invalid_channel_transform()`

### `def test_channel_ref_array_type_string()`

### `def test_channel_ref_array_setter()`

### `def test_channel_ref_array_return()`

### `def test_channel_ref_for_vector_channel()`

### `def test_channel_ref_array_run()`

### `def test_channel_ref_array_run_python()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_compare_equal.py -->
## PYTHON MODULE: tests/test_compare_equal.py

### `def _return_constant()`

### `def equal_bool_builtins()`

### `def equal_bool_builtins1()`

### `def equal_bool_builtins2()`

### `def equal_bool_builtins3()`

### `def equal_simple_numbers()`

### `def equal_num_nivsdatatype()`

### `def equal_nivsdatatype_nivsdatatype()`

### `def equal_nivsdatatype_nivsdatatype1()`

### `def equal_nivsdatatype_nivsdatatype2()`

### `def equal_nivsdatatype_nivsdatatype3()`

### `def equal_multiple_types()`

### `def equal_multiple_types1()`

### `def equal_use_rtseq()`

### `def equal_use_rtseq1()`

### `def equal_use_rtseq2()`

### `def equal_use_rtseq3()`

### `def equal_use_rtseq4()`

### `def equal_use_rtseq5()`

### `def equal_with_parentheses()`

### `def equal_with_parentheses1()`

### `def equal_with_parentheses2()`

### `def equal_variables()`

### `def equal_variables1()`

### `def equal_variable_variable()`

### `def equal_variable_variable1()`

### `def equal_variable_variable2()`

### `def equal_variable_rtseq()`

### `def equal_variable_rtseq1()`

### `def equal_to_channel_ref()`

### `def equal_binary_unary()`

### `def equal_with_multiple_comparators()`

### `def equal_complex_expr()`

### `def equal_invalid_variables()`

### `def equal_invalid_variables1()`

### `def equal_to_None()`

### `def equal_invalid_rtseq_call()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_compare_greater.py -->
## PYTHON MODULE: tests/test_compare_greater.py

### `def _return_constant()`

### `def greater_simple_numbers()`

### `def greater_nivsdatatype_num()`

### `def greater_num_nivsdatatype()`

### `def greater_nivsdatatype_nivsdatatype()`

### `def greater_nivsdatatype_nivsdatatype1()`

### `def greater_nivsdatatype_nivsdatatype2()`

### `def greater_nivsdatatype_nivsdatatype3()`

### `def greater_multiple_types()`

### `def greater_multiple_types1()`

### `def greater_use_rtseq()`

### `def greater_use_rtseq1()`

### `def greater_use_rtseq2()`

### `def greater_use_rtseq3()`

### `def greater_use_rtseq4()`

### `def greater_use_rtseq5()`

### `def greater_with_parentheses()`

### `def greater_variables()`

### `def greater_variables1()`

### `def greater_variable_variable()`

### `def greater_variable_variable1()`

### `def greater_variable_rtseq()`

### `def greater_variable_rtseq1()`

### `def greater_to_channel_ref()`

### `def greater_binary_unary()`

### `def greater_with_multiple_comparators()`

### `def greater_complex_expr()`

### `def greater_invalid_variables()`

### `def greater_invalid_variables1()`

### `def greater_to_None()`

### `def greater_invalid_rtseq_call()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_compare_greater_equal.py -->
## PYTHON MODULE: tests/test_compare_greater_equal.py

### `def _return_constant()`

### `def greater_eq_simple_numbers()`

### `def greater_eq_nivsdatatype_num()`

### `def greater_eq_num_nivsdatatype()`

### `def greater_eq_nivsdatatype_nivsdatatype()`

### `def greater_eq_nivsdatatype_nivsdatatype1()`

### `def greater_eq_nivsdatatype_nivsdatatype2()`

### `def greater_eq_nivsdatatype_nivsdatatype3()`

### `def greater_eq_multiple_types()`

### `def greater_eq_multiple_types1()`

### `def greater_eq_use_rtseq()`

### `def greater_eq_use_rtseq1()`

### `def greater_eq_use_rtseq2()`

### `def greater_eq_use_rtseq3()`

### `def greater_eq_use_rtseq4()`

### `def greater_eq_use_rtseq5()`

### `def greater_eq_with_parentheses()`

### `def greater_eq_variables()`

### `def greater_eq_variables1()`

### `def greater_eq_variable_variable()`

### `def greater_eq_variable_variable1()`

### `def greater_eq_variable_rtseq()`

### `def greater_eq_variable_rtseq1()`

### `def greater_eq_to_channel_ref()`

### `def greater_eq_binary_unary()`

### `def greater_eq_with_multiple_comparators()`

### `def greater_eq_complex_expr()`

### `def greater_eq_invalid_variables()`

### `def greater_eq_invalid_variables1()`

### `def greater_eq_to_None()`

### `def greater_eq_invalid_rtseq_call()`

### `def gt_equal_simple_numbers()`

### `def gt_equal_num_nivsdatatype()`

### `def gt_equal_nivsdatatype_nivsdatatype()`

### `def gt_equal_nivsdatatype_nivsdatatype1()`

### `def gt_equal_nivsdatatype_nivsdatatype2()`

### `def gt_equal_nivsdatatype_nivsdatatype3()`

### `def gt_equal_multiple_types()`

### `def gt_equal_multiple_types1()`

### `def gt_equal_use_rtseq()`

### `def gt_equal_use_rtseq1()`

### `def gt_equal_use_rtseq2()`

### `def gt_equal_use_rtseq3()`

### `def gt_equal_use_rtseq4()`

### `def gt_equal_use_rtseq5()`

### `def gt_equal_with_parentheses()`

### `def gt_equal_with_parentheses1()`

### `def gt_equal_variables()`

### `def gt_equal_variables1()`

### `def gt_equal_variable_variable()`

### `def gt_equal_variable_variable1()`

### `def gt_equal_variable_variable2()`

### `def gt_equal_variable_rtseq()`

### `def gt_equal_variable_rtseq1()`

### `def gt_equal_to_channel_ref()`

### `def gt_equal_binary_unary()`

### `def gt_equal_with_multiple_comparators()`

### `def gt_equal_complex_expr()`

### `def gt_equal_invalid_variables()`

### `def gt_equal_invalid_variables1()`

### `def gt_equal_to_None()`

### `def gt_equal_invalid_rtseq_call()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_compare_inequality.py -->
## PYTHON MODULE: tests/test_compare_inequality.py

### `def _return_constant()`

### `def notequal_bool_builtins()`

### `def notequal_bool_builtins1()`

### `def notequal_bool_builtins2()`

### `def notequal_bool_builtins3()`

### `def notequal_simple_numbers()`

### `def notequal_num_nivsdatatype()`

### `def notequal_nivsdatatype_nivsdatatype()`

### `def notequal_nivsdatatype_nivsdatatype1()`

### `def notequal_nivsdatatype_nivsdatatype2()`

### `def notequal_nivsdatatype_nivsdatatype3()`

### `def notequal_multiple_types()`

### `def notequal_multiple_types1()`

### `def notequal_use_rtseq()`

### `def notequal_use_rtseq1()`

### `def notequal_use_rtseq2()`

### `def notequal_use_rtseq3()`

### `def notequal_use_rtseq4()`

### `def notequal_use_rtseq5()`

### `def notequal_with_parentheses()`

### `def notequal_with_parentheses1()`

### `def notequal_with_parentheses2()`

### `def notequal_variables()`

### `def notequal_variables1()`

### `def notequal_variable_variable()`

### `def notequal_variable_variable1()`

### `def notequal_variable_variable2()`

### `def notequal_variable_rtseq()`

### `def notequal_variable_rtseq1()`

### `def notequal_to_channel_ref()`

### `def notequal_binary_unary()`

### `def notequal_with_multiple_comparators()`

### `def notequal_complex_expr()`

### `def notequal_invalid_variables()`

### `def notequal_invalid_variables1()`

### `def notequal_to_None()`

### `def notequal_invalid_rtseq_call()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_compare_less.py -->
## PYTHON MODULE: tests/test_compare_less.py

### `def _return_constant()`

### `def less_simple_numbers()`

### `def less_nivsdatatype_num()`

### `def less_num_nivsdatatype()`

### `def less_nivsdatatype_nivsdatatype()`

### `def less_nivsdatatype_nivsdatatype1()`

### `def less_nivsdatatype_nivsdatatype2()`

### `def less_nivsdatatype_nivsdatatype3()`

### `def less_multiple_types()`

### `def less_multiple_types1()`

### `def less_use_rtseq()`

### `def less_use_rtseq1()`

### `def less_use_rtseq2()`

### `def less_use_rtseq3()`

### `def less_use_rtseq4()`

### `def less_use_rtseq5()`

### `def less_with_parentheses()`

### `def less_variables()`

### `def less_variables1()`

### `def less_variable_variable()`

### `def less_variable_variable1()`

### `def less_variable_rtseq()`

### `def less_variable_rtseq1()`

### `def less_to_channel_ref()`

### `def less_binary_unary()`

### `def less_with_multiple_comparators()`

### `def less_complex_expr()`

### `def less_invalid_variables()`

### `def less_invalid_variables1()`

### `def less_to_None()`

### `def less_invalid_rtseq_call()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_compare_less_equal.py -->
## PYTHON MODULE: tests/test_compare_less_equal.py

### `def _return_constant()`

### `def less_eq_simple_numbers()`

### `def less_eq_nivsdatatype_num()`

### `def less_eq_num_nivsdatatype()`

### `def less_eq_nivsdatatype_nivsdatatype()`

### `def less_eq_nivsdatatype_nivsdatatype1()`

### `def less_eq_nivsdatatype_nivsdatatype2()`

### `def less_eq_nivsdatatype_nivsdatatype3()`

### `def less_eq_multiple_types()`

### `def less_eq_multiple_types1()`

### `def less_eq_use_rtseq()`

### `def less_eq_use_rtseq1()`

### `def less_eq_use_rtseq2()`

### `def less_eq_use_rtseq3()`

### `def less_eq_use_rtseq4()`

### `def less_eq_use_rtseq5()`

### `def less_eq_with_parentheses()`

### `def less_eq_variables()`

### `def less_eq_variables1()`

### `def less_eq_variable_variable()`

### `def less_eq_variable_variable1()`

### `def less_eq_variable_rtseq()`

### `def less_eq_variable_rtseq1()`

### `def less_eq_to_channel_ref()`

### `def less_eq_binary_unary()`

### `def less_eq_with_multiple_comparators()`

### `def less_eq_complex_expr()`

### `def less_eq_invalid_variables()`

### `def less_eq_invalid_variables1()`

### `def less_eq_to_None()`

### `def less_eq_invalid_rtseq_call()`

### `def lt_equal_simple_numbers()`

### `def lt_equal_num_nivsdatatype()`

### `def lt_equal_nivsdatatype_nivsdatatype()`

### `def lt_equal_nivsdatatype_nivsdatatype1()`

### `def lt_equal_nivsdatatype_nivsdatatype2()`

### `def lt_equal_nivsdatatype_nivsdatatype3()`

### `def lt_equal_multiple_types()`

### `def lt_equal_multiple_types1()`

### `def lt_equal_use_rtseq()`

### `def lt_equal_use_rtseq1()`

### `def lt_equal_use_rtseq2()`

### `def lt_equal_use_rtseq3()`

### `def lt_equal_use_rtseq4()`

### `def lt_equal_use_rtseq5()`

### `def lt_equal_with_parentheses()`

### `def lt_equal_with_parentheses1()`

### `def lt_equal_variables()`

### `def lt_equal_variables1()`

### `def lt_equal_variable_variable()`

### `def lt_equal_variable_variable1()`

### `def lt_equal_variable_variable2()`

### `def lt_equal_variable_rtseq()`

### `def lt_equal_variable_rtseq1()`

### `def lt_equal_to_channel_ref()`

### `def lt_equal_binary_unary()`

### `def lt_equal_with_multiple_comparators()`

### `def lt_equal_complex_expr()`

### `def lt_equal_invalid_variables()`

### `def lt_equal_invalid_variables1()`

### `def lt_equal_to_None()`

### `def lt_equal_invalid_rtseq_call()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_conditional.py -->
## PYTHON MODULE: tests/test_conditional.py

### `def if_pass()`

### `def if_else_pass()`

### `def if_invalid_boolean()`

### `def if_invalid_boolean_const()`

### `def if_invalid_boolean_var()`

### `def if_elif_pass()`

### `def if_nested()`

### `def if_one_statement()`

### `def if_multiple_statements()`

### `def if_condition_variable()`

### `def if_condition_equal_operator()`

### `def if_condition_identity_operator()`

### `def if_condition_identity_not_operator()`

### `def _returns_true()`

### `def if_condition_function_call()`

### `def if_condition_complex_expression()`

### `def if_elif_condition_complex_expression()`

### `def if_try_catch_fails()`

### `def if_try_finally_fails()`

### `def if_else_try_finally_fails()`

### `def if_elif_try_finally_fails()`

### `def if_return_fails()`

### `def if_else_return_fails()`

### `def if_elif_return_fails()`

### `def if_funcdef_fails()`

### `def if_else_funcdef_fails()`

### `def if_elif_funcdef_fails()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_datatypes.py -->
## PYTHON MODULE: tests/test_datatypes.py

### `def boolean_type()`

### `def boolean_type1()`

### `def boolean_type2()`

### `def boolean_type3()`

### `def boolean_type_run()`

### `def boolean_type1_run()`

### `def boolean_type2_run()`

### `def boolean_type3_run()`

### `def illegal_boolean_type()`

### `def double_type()`

### `def double_type1()`

### `def double_type_run()`

### `def double_type1_run()`

### `def illegal_double_type()`

### `def int32_type()`

### `def int32_type1()`

### `def int32_type_run()`

### `def int32_type1_run()`

### `def illegal_int32_type()`

### `def int32_overflow_error()`

### `def int64_type()`

### `def int64_type1()`

### `def int64_type_run()`

### `def int64_type1_run()`

### `def illegal_int64_type()`

### `def int64_overflow_error()`

### `def uint32_type()`

### `def uint32_type1()`

### `def uint32_type_run()`

### `def uint32_type1_run()`

### `def illegal_uint32_type()`

### `def uint32_overflow_error()`

### `def uint64_type()`

### `def uint64_type1()`

### `def uint64_type_run()`

### `def uint64_type1_run()`

### `def illegal_uint64_type()`

### `def uint64_overflow_error()`

### `def boolean_type_negative()`

### `def double_type_negative()`

### `def int32_type_negative()`

### `def int64_type_negative()`

### `def uint32_type_negative()`

### `def uint64_type_negative()`

### `def boolean_type_negative_run()`

### `def double_type_negative_run()`

### `def int32_type_negative_run()`

### `def int64_type_negative_run()`

### `def uint32_type_negative_run()`

### `def uint64_type_negative_run()`

### `def boolean_array_one_element()`

### `def boolean_array_type()`

### `def boolean_array_empty()`

### `def boolean_array_one_element_run()`

### `def boolean_array_type_run()`

### `def boolean_array_invalid_type()`

### `def boolean_array_invalid_type1()`

### `def double_array_one_element()`

### `def double_array_type()`

### `def double_array_empty()`

### `def double_array_one_element_run()`

### `def double_array_type_run()`

### `def double_array_invalid_type()`

### `def double_array_invalid_type1()`

### `def int32_array_one_element()`

### `def int32_array_type()`

### `def int32_array_empty()`

### `def int32_array_one_element_run()`

### `def int32_array_type_run()`

### `def int32_array_invalid_type()`

### `def int32_array_invalid_type1()`

### `def int64_array_one_element()`

### `def int64_array_type()`

### `def int64_array_empty()`

### `def int64_array_one_element_run()`

### `def int64_array_type_run()`

### `def int64_array_invalid_type()`

### `def int64_array_invalid_type1()`

### `def uint32_array_one_element()`

### `def uint32_array_type()`

### `def uint32_array_empty()`

### `def uint32_array_one_element_run()`

### `def uint32_array_type_run()`

### `def uint32_array_invalid_type()`

### `def uint32_array_invalid_type1()`

### `def uint32_array_negative_values()`

### `def uint64_array_one_element()`

### `def uint64_array_type()`

### `def uint64_array_one_element_run()`

### `def uint64_array_type_run()`

### `def uint64_array_empty()`

### `def uint64_array_invalid_type()`

### `def uint64_array_invalid_type1()`

### `def uint64_array_negative_values()`

### `def invalid_return_type()`

### `def int32_max_value()`

### `def int32_max_value_overflow()`

### `def int64_max_value()`

### `def int64_max_value_overflow()`

### `def uint32_max_value()`

### `def uint32_max_value_overflow()`

### `def uint64_max_value()`

### `def uint64_max_value_overflow()`

### `def int32_array_overflow()`

### `def int64_array_overflow()`

### `def uint32_array_overflow()`

### `def uint64_array_overflow()`

### `def idfunc(val)`

### `def test_transform(func_name, params)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, expected_result)`

### `def test_check_all_tested()`

### `def test_python_only_boolean()`

### `def test_python_only_double()`

### `def test_python_only_i32()`

### `def test_python_only_i64()`

### `def test_python_only_u32()`

### `def test_python_only_u64()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_docstrings.py -->
## PYTHON MODULE: tests/test_docstrings.py

### `def docstring_func_single_line()`

Single-line doc.

### `def docstring_func_parameters(arg1, arg2)`

Test parameters docstring.

    :param arg1: first argument
    :param arg2: second argument
    

### `def docstring_func_multi_line()`

Begin doc.

    This is more doc
    that is in multiple strings.
    

### `def docstring_func_in_code()`

Begin doc.

    This is more doc
    that is in multiple strings.
    

### `def docstring_try()`

Begin doc.

    This is more doc
    that is in multiple strings.
    

### `def docstring_multitask()`

Test multitask docstring.

### `def docstring_try_inside()`

Begin doc.

    This is more doc
    that is in multiple strings.
    

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_for_loop.py -->
## PYTHON MODULE: tests/test_for_loop.py

### `def _return_constant()`

### `def _increment_param_by_ref(param)`

### `def for_loop_variable_array()`

### `def for_loop_variable_array1()`

### `def for_loop_modify_collection()`

### `def for_loop_modify_elements()`

### `def for_loop_constant_array()`

### `def for_loop_range()`

### `def for_loop_range_with_start()`

### `def for_loop_range_with_step()`

### `def for_loop_range_with_variable()`

### `def for_loop_range_with_channel_ref()`

### `def for_loop_range_with_call()`

### `def for_loop_iterate_on_array()`

### `def for_loop_else()`

### `def nested_for_loop()`

### `def nested_for_loop_body()`

### `def looping_over_invalid_var()`

### `def for_return_in_body()`

### `def for_try_in_body()`

### `def for_funcdef_in_body()`

### `def _average(array)`

### `def call_average()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_generate_error.py -->
## PYTHON MODULE: tests/test_generate_error.py

### `def _gen_stop()`

### `def _gen_abort()`

### `def _gen_continue()`

### `def generate_error_simple()`

### `def generate_continue()`

### `def _generate_continue_no_fail()`

### `def generate_stop()`

### `def generate_abort()`

### `def generate_continue_mt()`

### `def generate_stop_mt()`

### `def generate_abort_mt()`

### `def generate_continue_subroutine()`

### `def generate_continue_subroutine1()`

### `def generate_stop_subroutine()`

### `def generate_stop_subroutine1()`

### `def generate_abort_subroutine()`

### `def generate_abort_subroutine1()`

### `def invalid_error_code()`

### `def invalid_error_message()`

### `def invalid_error_action()`

### `def generate_multiple_errors()`

### `def generate_multiple_errors1()`

### `def generate_multiple_errors2()`

### `def idfunc(val)`

### `def test_gen_continue_no_fail()`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_ifexpression.py -->
## PYTHON MODULE: tests/test_ifexpression.py

### `def _returns_true()`

### `def ifexp_bool_test_bool_assign()`

### `def ifexp_bool_test_int_assign()`

### `def ifexp_bool_test_int_assign1()`

### `def ifexp_bool_test_nivstype_assign()`

### `def ifexp_nivsbool_test_nivstype_assign()`

### `def ifexp_nivsbool_test_nivstype_assign1()`

### `def ifexp_nivsboolvar_test_int_assign()`

### `def ifexp_nivsboolvar_test_int_assign1()`

### `def ifexp_expression_test_int_assign()`

### `def ifexp_expression_test_int_assign1()`

### `def ifexp_nested_ifexp()`

### `def ifexp_rtseq_test()`

### `def ifexp_rtseq_test_rtseq_assign()`

### `def ifexp_rtseq_test_rtseq_assign1()`

### `def ifexp_bool_test_expression_assign()`

### `def ifexp_bool_test_expression_assign1()`

### `def aug_ifexp_bool_test_expression_assign()`

### `def ifexp_invalid_int_test()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_logical_and.py -->
## PYTHON MODULE: tests/test_logical_and.py

### `def _return_true()`

### `def logical_and_simple_numbers()`

### `def logical_and_simple_numbers1()`

### `def logical_and_nivsdatatype_double()`

### `def logical_and_nivsdatatype_int32()`

### `def logical_and_nivsdatatype_int64()`

### `def logical_and_nivsdatatype_bool()`

### `def logical_and_multiple_types()`

### `def logical_and_multiple_types1()`

### `def logical_and_variables_redefined()`

### `def logical_and_variables1()`

### `def logical_and_rtseq()`

### `def logical_and_rtseq1()`

### `def logical_and_parentheses()`

### `def logical_and_unary()`

### `def logical_and_invalid_variables()`

### `def logical_and_invalid_variables1()`

### `def logical_and_None()`

### `def logical_and_invalid_rtseq_call()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_logical_not.py -->
## PYTHON MODULE: tests/test_logical_not.py

### `def _return_true()`

### `def logical_not_simple_numbers()`

### `def logical_not_simple_numbers1()`

### `def logical_not_nivsdatatype_double()`

### `def logical_not_nivsdatatype_double1()`

### `def logical_not_nivsdatatype_int32()`

### `def logical_not_nivsdatatype_int64()`

### `def logical_not_bool()`

### `def logical_not_bool1()`

### `def logical_not_variables()`

### `def logical_not_rtseq()`

### `def logical_not_parentheses()`

### `def logical_not_unary()`

### `def logical_not_sequence()`

### `def logical_not_invalid_variables()`

### `def logical_not_None()`

### `def logical_not_invalid_rtseq_call()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_logical_or.py -->
## PYTHON MODULE: tests/test_logical_or.py

### `def _return_true()`

### `def logical_or_simple_numbers()`

### `def logical_or_nivsdatatype_double()`

### `def logical_or_nivsdatatype_int32()`

### `def logical_or_nivsdatatype_int64()`

### `def logical_or_nivsdatatype_bool()`

### `def logical_or_multiple_types()`

### `def logical_or_multiple_types1()`

### `def logical_or_variables_redefined()`

### `def logical_or_variables1()`

### `def logical_or_rtseq()`

### `def logical_or_rtseq1()`

### `def logical_or_parentheses()`

### `def logical_or_unary()`

### `def logical_or_invalid_variables()`

### `def logical_or_invalid_variables1()`

### `def logical_or_None()`

### `def logical_or_invalid_rtseq_call()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_multitask.py -->
## PYTHON MODULE: tests/test_multitask.py

### `def _increase_param_by_ref(param)`

### `def _subseq_with_multitask(param)`

### `def multitask_pass()`

### `def multitask_access_local()`

### `def multitask_blocks_until_done()`

### `def multitask_nested()`

### `def multitask_task_with_yield()`

### `def multitask_tasks_with_different_iter_count()`

### `def multitask_nested_validate_order()`

### `def multitask_multiple_in_sequence_validate_order()`

### `def multitask_call_subroutine_params_by_ref()`

### `def multitask_call_subroutine_with_multitask()`

### `def multitask_duplicate_name_fails()`

### `def multitask_redefine_var_fails()`

### `def multitask_return_fails()`

### `def multitask_stmt_fails()`

### `def multitask_with_param_fails()`

### `def multitask_task_with_param_fails()`

### `def multitask_return_in_task_fails()`

### `def multitask_funcdef_in_task_fails()`

### `def multitask_no_var_name_fails()`

### `def multitask_wrong_var_name_fails()`

### `def multitask_task_multi_dec_fails()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_run_multiple_top_level_seqs()`

### `def test_run_multiple_top_level_seqs_in_parallel()`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_rtseqpkg.py -->
## PYTHON MODULE: tests/test_rtseqpkg.py

### `def empty_func()`

### `def returns_one()`

### `def calls_another()`

### `def two_levels_deep()`

### `def test_rtseqpkg_create_empty()`

### `def test_rtseqpkg_append_module()`

### `def test_rtseqpkg_append_func()`

### `def test_rtseqpkg_index_returns_RealTimeSequence()`

### `def test_rtseqpkg_can_iterate()`

### `def test_rtseqpkg_append_dup_doesnt_append()`

### `def test_rtseqpkg_contains()`

### `def test_save_all_module()`

### `def test_rtseq_with_deps()`

### `def test_rtseq_with_deps_multiple_times()`

### `def test_rtseq_with_deps_multiple_times_diff_folder()`

### `def test_rtseq_several_calls()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_runpyasrtseq.py -->
## PYTHON MODULE: tests/test_runpyasrtseq.py

### `def return_var()`

### `def _increment(a)`

### `def sub_routine_caller()`

### `def invalid_sequence()`

### `def return_void()`

### `def generate_error_continue()`

### `def generate_error_stop()`

### `def generate_error_abort()`

### `def idfunc(val)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_not_wait_to_complete()`

### `def test_run_multiple_top_level_seqs()`

### `def test_run_multiple_top_level_seqs_in_parallel()`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_saveasrtseq.py -->
## PYTHON MODULE: tests/test_saveasrtseq.py

### `def test_save_creates_file()`

### `def test_save_invalid_folder_throws()`

### `def _save_debug_helper(func)`

Save a sequence so it can be inspected manually.

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_stop_taks.py -->
## PYTHON MODULE: tests/test_stop_taks.py

### `def _invalid()`

### `def _return_param_plus_1(param)`

### `def stop_task_simple()`

### `def stop_task_invalid_task_name()`

### `def stop_task_invalid_task_name1()`

### `def stop_task_in_try()`

### `def stop_task_complex()`

### `def stop_task_call_subroutine()`

### `def stop_task_call_subroutine1()`

### `def stop_task_call_subroutine2()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_subroutine_call.py -->
## PYTHON MODULE: tests/test_subroutine_call.py

### `def _return_constant()`

### `def finite_recursion(x)`

### `def circular_call_a()`

### `def circular_call_b()`

### `def _return_parameter(param)`

### `class FunkyDecorator()`

#### `def __init__(self, a, b)`

#### `def __call__(self, f)`

### `def return_parameter_invalid_decorator(param)`

### `def _return_param_wrong_param_name_pure_python(param)`

### `def return_parameter_with_decorator_wrong_name(param)`

### `def _return_parameter_with_decorator(param)`

### `def _return_parameter_with_decorator_by_ref(param)`

### `def _return_parameter_with_decorator_inverted(param)`

### `def _return_by_ref_in_z_sqrt_of_square_x_plus_square_y(x, y, z)`

### `def _return_arr_element(param)`

### `def _return_arr_element_plus1_by_ref(param)`

### `def _return_parameter_plus1_by_ref(param)`

### `def _return_parameter_plus1_by_value(param)`

### `def _return_parameter_plus1_by_ref_bool(param)`

### `def _return_parameter_plus1_by_value_bool(param)`

### `def _increment_constant_passed_by_ref(param)`

### `def _return_parameter_with_built_in_function_name(mod)`

### `def call_increment_constant_passed_by_ref()`

### `def call_return_constant_as_assignment()`

### `def call_return_constant_as_expr()`

### `def call_return_parameter()`

### `def call_parameter_nivsdatatype()`

### `def call_parameter_nivsdatatype_by_value()`

### `def call_parameter_nivsdatatype_by_value_untouched_orig()`

### `def call_parameter_nivsdatatype_by_ref_bool_ref()`

### `def call_parameter_nivsdatatype_by_value_bool_ref()`

### `def call_parameter_builtin_math()`

### `def call_parameter_array_elem()`

### `def call_parameter_array_elem_by_ref()`

### `def call_parameter_with_decorator_diff_param_type_by_value()`

### `def call_parameter_with_decorator_diff_param_type_by_ref()`

### `def call_parameter_with_decorator()`

### `def call_parameter_with_decorator_inverted()`

### `def call_parameter_with_many_decorators()`

### `def call_parameter_send_channel_ref_by_value()`

### `def call_parameter_send_channel_ref_by_ref()`

### `def recursive_call()`

### `def invalid_call()`

### `def call_return_parameter_with_built_in_function_name()`

### `def test_param_wrong_name_python()`

### `def constant_passed_by_ref_is_not_actually_by_ref()`

### `def _increment_constant_passed_by_ref_without_rt_decorator(param)`

### `def test_constant_passed_by_ref_without_rt_decorator()`

### `def test_object_passed_by_ref_without_rt_decorator()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_subscript.py -->
## PYTHON MODULE: tests/test_subscript.py

### `def _return_constant()`

### `def _return_param_plus_one(param)`

### `def _modify_param(param)`

### `def number_subscript()`

### `def rtseq_call_subscript()`

### `def subscript_in_subscript()`

### `def operator_in_subscript()`

### `def operator_in_subscript1()`

### `def assign_subscript()`

### `def assign_subscript1()`

### `def assign_subscript2()`

### `def assign_subscript3()`

### `def assign_subroutine_return()`

### `def modify_array()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_timing.py -->
## PYTHON MODULE: tests/test_timing.py

### `def wait_nivstype()`

### `def wait_const()`

### `def wait_multitask()`

### `def wait_const_negative()`

### `def _return_one()`

### `def wait_subseq_call()`

### `def wait_until_next_ms()`

### `def wait_until_next_us()`

### `def wait_until_settled_multitask()`

### `def wait_until_settled_timeout()`

### `def wait_wrong_param_type()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_skipped(func_name, params, reason)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_top_level_rtseq_params.py -->
## PYTHON MODULE: tests/test_top_level_rtseq_params.py

### `def func1(p)`

### `def func2(p)`

### `def test_run_py_as_rtseq_numeric_param()`

### `def test_run_py_as_rtseq_channel_reference_param()`

### `def test_run_py_as_rtseq_invalid_extra_parameter()`

### `def test_run_py_as_rtseq_missing_by_ref_parameter()`

### `def test_run_py_as_rtseq_missing_by_value_parameter()`

### `def test_run_py_as_rtseq_wrong_parameter_data_type()`

### `def test_realtimesequence_numeric_param()`

### `def test_realtimesequence_channel_reference_param()`

### `def test_realtimesequence_invalid_extra_parameter()`

### `def test_realtimesequence_missing_by_ref_parameter()`

### `def test_realtimesequence_missing_by_value_parameter()`

### `def test_realtimesequence_wrong_parameter_data_type()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_transformpy2rtseq.py -->
## PYTHON MODULE: tests/test_transformpy2rtseq.py

### `def test_transform_invalid_function_fails()`

### `def test_transform_func_without_decorator_fails()`

### `def test_transform_empty()`

### `def test_transform_empty_with_two_decorators()`

### `def test_transform_simple_local_assignment()`

### `def test_transform_pi_assign_to_local()`

### `def test_untyped_declarations_fail()`

### `def test_return_var()`

### `def test_return_var_value()`

### `def test_undeclared_variable_fail()`

### `def test_return_named_type()`

### `def test_return_primitive_num()`

### `def test_return_var_pi()`

### `def test_return_untyped_symbol()`

### `def test_multiple_returns()`

### `def test_return_not_last()`

### `def test_default_value_bool_true()`

### `def test_default_value_bool_false()`

### `def test_boolean_array_return_type()`

### `def test_double_array_return_type()`

### `def test_a_value_value_assignment()`

### `def test_a_value_value_assign_to()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_try_finally.py -->
## PYTHON MODULE: tests/test_try_finally.py

### `def _sub_rt_seq(param)`

### `def try_simple()`

### `def try_second_statement()`

### `def return_in_try()`

### `def return_in_finally()`

### `def try_complex_body()`

### `def try_in_try()`

### `def try_in_if()`

### `def try_in_else()`

### `def try_in_while()`

### `def try_in_for()`

### `def call_subroutine_with_try()`

### `def try_with_except()`

### `def try_with_orelse()`

### `def try_in_task()`

### `def try_in_multitask()`

### `def try_in_multitask1()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_unary_invert.py -->
## PYTHON MODULE: tests/test_unary_invert.py

### `def _returns_zero()`

### `def invert_bool()`

### `def invert_bool_var()`

### `def invert_int32()`

### `def invert_int32_1()`

### `def invert_int32_2()`

### `def invert_int32_limit()`

### `def invert_int32_4()`

### `def invert_int32_var()`

### `def invert_int32_var_1()`

### `def invert_int32_var_2()`

### `def invert_int32_var_limit()`

### `def invert_int32_var_4()`

### `def invert_int64()`

### `def invert_int64_1()`

### `def invert_int64_2()`

### `def invert_int64_out_of_spe_range()`

### `def invert_int64_4()`

### `def invert_int64_var()`

### `def invert_int64_var_1()`

### `def invert_int64_var_2()`

### `def invert_int64_var_out_of_spe_range()`

### `def invert_int64_var_4()`

### `def invert_int64_multiple()`

### `def invert_int64_multiple1()`

### `def invert_int32_multiple()`

### `def invert_int32_multiple1()`

### `def invert_parentheses()`

### `def invert_rtseq()`

### `def invert_double()`

### `def invert_double_var()`

### `def invert_invalid_variables()`

### `def invert_invalid_variables1()`

### `def invert_with_None()`

### `def invert_invalid_rtseq_call()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_while.py -->
## PYTHON MODULE: tests/test_while.py

### `def while_pass()`

### `def while_break()`

### `def while_else_pass_fails()`

### `def while_invalid_boolean()`

### `def while_invalid_boolean_const()`

### `def while_invalid_boolean_var()`

### `def while_nested()`

### `def while_one_statement()`

### `def while_multiple_statements()`

### `def while_condition_variable()`

### `def while_condition_equal_operator()`

### `def while_condition_identity_operator()`

### `def while_condition_identity_not_operator()`

### `def _returns_true_if_less_than_5(x)`

### `def while_condition_function_call()`

### `def while_condition_complex_expression()`

### `def while_try_catch_fail()`

### `def while_try_finally_fail()`

### `def while_funcdef_fail()`

### `def while_return_fail()`

### `def while_false()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/test_yield.py -->
## PYTHON MODULE: tests/test_yield.py

### `def yield_single()`

### `def yield_many()`

### `def yield_in_while()`

### `def yield_multitask()`

### `def yield_as_parameter_fail()`

### `def yield_as_operator_fails()`

### `def idfunc(val)`

### `def test_transform(func_name, params, expected_result)`

### `def test_runpy(func_name, params, expected_result)`

### `def test_run_py_as_rts(func_name, params, expected_result)`

### `def test_run_in_VM(func_name, params, expected_result)`

### `def test_failures(func_name, params, expected_result)`

### `def test_check_all_tested()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/testutilities/astutils.py -->
## PYTHON MODULE: tests/testutilities/astutils.py

### `def pretty_print_ast(obj, graphical=False)`

### `class AstPrinter(object)`

#### `def __init__(self, topnode)`

#### `def print_all(self)`

#### `def print_node(self, node)`

#### `def print_with_indentation(self, msg)`

#### `def increment_indent(self)`

#### `def decrement_indent(self, msg=None)`

### `class AstGUIPrinter(AstPrinter)`

#### `def __init__(self, topnode)`

#### `def print_all(self)`

#### `def print_with_indentation(self, msg)`

#### `def increment_indent(self)`

#### `def decrement_indent(self, msg=None)`

<!--NI_PYTHON_API repo=niveristand-python path=tests/testutilities/configutilities.py -->
## PYTHON MODULE: tests/testutilities/configutilities.py

### `def getbinariesfolder()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/testutilities/logging_helpers.py -->
## PYTHON MODULE: tests/testutilities/logging_helpers.py

### `def enable_console_logging(log=None, level=logging.DEBUG)`

<!--NI_PYTHON_API repo=niveristand-python path=tests/testutilities/rtseqrunner.py -->
## PYTHON MODULE: tests/testutilities/rtseqrunner.py

### `def _check_can_run_local()`

### `def run_rtseq_local(filepath, channel_names=[], channel_values=[], deltat=1)`

### `def assert_run_python_equals_rtseq(func, expected)`

### `def run_rtseq_in_VM(func, deltat=1)`

<!--NI_PYTHON_API repo=niveristand-python path=tests/testutilities/testfunctions.py -->
## PYTHON MODULE: tests/testutilities/testfunctions.py

### `def func_without_decorator()`

### `def empty_func()`

### `def empty_func_with_double_decorator()`

### `def simple_local_assignment()`

### `def simple_float_local_assignment()`

### `def simple_assign_pi()`

### `def assign_untyped()`

### `def return_var()`

### `def return_var_value()`

### `def return_var_invalid_value()`

### `def return_named_type()`

### `def return_primitive_num()`

### `def return_var_pi()`

### `def return_untyped_symbol()`

### `def return_true()`

### `def return_false()`

### `def return_boolean_array()`

### `def return_double_array()`

### `def multiple_returns()`

### `def return_not_last()`

### `def channel_ref_type_string()`

### `def channel_ref_setter()`

### `def channel_ref_return()`

### `def channel_ref_validate_getter()`

### `def channel_ref_invalid_channel_set()`

### `def channel_ref_invalid_channel_get()`

### `def channel_ref_invalid_channel_transform()`

### `def channel_ref_array_type_string()`

### `def channel_ref_array_setter()`

### `def channel_ref_array_return()`

### `def channel_ref_for_vector_channel()`

### `def channel_ref_array_validate_getter()`

### `def a_value_value_assignment()`

### `def a_value_value_assign_to()`

<!--NI_PYTHON_API repo=niveristand-python path=tests/testutilities/validation.py -->
## PYTHON MODULE: tests/testutilities/validation.py

### `def test_validate(testmodule)`

### `def _validate_special_lists_are_subsets_of_overall_lists(test_lists, special_list_name, overall_list_name)`
