# NI PYTHON API DIGEST: python_labview_automation

<!--NI_PYTHON_API_SNAPSHOT repo=ni/python_labview_automation commit=5078abb312e17ae90f588ee4b398146a943cec06 -->

<!--NI_PYTHON_API repo=python_labview_automation path=labview_automation/__init__.py -->
## PYTHON MODULE: labview_automation/__init__.py

- `__all__ = ['client', 'labview']`

<!--NI_PYTHON_API repo=python_labview_automation path=labview_automation/client.py -->
## PYTHON MODULE: labview_automation/client.py

### `class Error(Exception)`


    Class for errors which occur while calling a LabVIEW VI
    

#### `def __init__(self, code, source, message)`

### `class LabVIEWClient(object)`


    This class is a simple wrapper around TCP methods that communicate with the
    LabVIEW Listener component
    

#### `def __init__(self, address, port=2552)`


        :param address: Address of the remote computer running the LVListener
                        eg. 10.2.13.32
        :param port: Port of the remote computer LVListener is listening on
                     (default: 2552)
        

#### `def __enter__(self)`

#### `def __exit__(self, type, value, tb)`

#### `def _check_for_error(self, return_dict)`


        Checks for an error being returned in the recieved dictionary.
        Raises an error if the status is true.
        

#### `def run_vi_synchronous(self, vi_path, control_values, run_options=0, open_frontpanel=False, indicator_names=[])`


        :param vi_path: Absolute path of the VI to run on the remote computer
        :param control_values: Dictionary of the control values to set on the
                               target VI
        :param run_options: Int to specify the LabVIEW run options for the
                            target VI
        :param open_frontpanel: Boolean that specifies whether to open front
                                panel of target VI
        :param indicator_names: Optional list of strings that specifies the
                                names of indicators to return. Returns all
                                indicators if an empty list is specified.
        

#### `def describe_error(self, error)`


        Sends a message to LabVIEW to describe an error.

        :param error: Dictionary containing 'source', 'status', and 'code'
        

#### `def set_controls(self, project_path, target_name, vi_path, control_values, ignore_nonexistent_controls=False)`


        Sets controls on a VI under a specified target of a specified project
        without running the VI. Leaves front panel of the VI open.

        :param project_path: Absolute path of the project which contains the VI
                             to set controls on
        :param target_name: Name of the target in the project which contains
                            the VI to set controls on
        :param vi_path: Absolute path of the target VI to set controls on
        :param control_values: Dictionary of the control values to set on the
                               target VI
        :param ignore_nonexistent_controls: Boolean that specifies whether to
                                            ignore errors if control_values
                                            contain controls that don't exist
                                            in the target VI
        

#### `def get_indicators(self, project_path, target_name, vi_path, indicator_names)`


        Get the specified indicators of a VI under a specified target of a
        specified project without running the VI.

        :param project_path: Absolute path of the project which contains the VI
                             to get the indicators value
        :param target_name: Name of the target in the project which contains
                            the VI to get the indicators values
        :param vi_path: Absolute path of the target VI to get indicators values
        :param indicator_names: List of indicator names of which to get values
        

#### `def _recv_dict(self)`

#### `def _send_dict(self, msg)`

<!--NI_PYTHON_API repo=python_labview_automation path=labview_automation/labview.py -->
## PYTHON MODULE: labview_automation/labview.py

### `class Error(Exception)`

### `class TimeoutError(Error)`

### `class LVINIError(Error)`

### `class NotStartedError(Error)`

### `class ServerConfiguration(object)`

#### `def __init__(self, start, port, log_path, error_log_path, tcp_timeout_s)`

#### `def start(self)`

#### `def port(self)`

#### `def log_path(self)`

#### `def error_log_path(self)`

#### `def tcp_timeout_s(self)`

### `class _LVOptions(object)`


    Class for convenience in setting LabVIEW Ini tokens.
    

#### `def __init__(self)`

#### `def get_dict(self)`

### `class LabVIEW(object)`


    Class to control an instance of LabVIEW such as starting or killing it,
    changing ini settings and so forth.
    

#### `def __init__(self, host='localhost', version=None, bitness=None, start_with_server=True, server_port=2552, server_log_path=None, server_error_log_path=None, server_tcp_timeout_s=60)`


        Args:
            version (string): The version of LabVIEW to control.  If
                unspecified the active version will be used and bitness will
                be ignored.
            bitness (string): Can be either x86 or x64.  Used to specify the
                copy to be controlled.  If both version and bitness are None,
                the active version will be used.  If version is not None then
                this will prefer x86.
        

#### `def server_cfg(self)`

#### `def path(self)`

#### `def executable(self)`

#### `def client(self)`


        Returns the LabVIEW Client for this instance.
        

#### `def disable_dialogs(self)`

#### `def disable_ni_error_reporting(self)`

#### `def add_to_search_path(self, path, append=False)`

#### `def set_number_of_execution_threads(self, number_of_threads)`

#### `def enable_vi_server(self)`

#### `def copy_to_labview_dir(self, source, relative_destination)`

#### `def start(self, wait_until_open=True, timeout_s=900)`

#### `def restart(self, wait_until_open=True, timeout_s=900)`

#### `def start_with_args(self, args)`

#### `def is_running(self)`

#### `def memory_usage(self)`

#### `def wait_until_server_loaded(self, timeout_s=900, port=2552)`


        This function will wait until the LabVIEW server is loaded on the local
        machine.

        :param timeout_s: How long to wait for the LabVIEW server to load.
            Default is 15 minutes (900 seconds).
        :raises TimeoutError: Raised when timeout exceeded while waiting
        

#### `def kill(self, timeout_s=None)`

### `class LabVIEWHelpers(object)`

#### `def is_os_64bit(self)`

#### `def get_labview_paths(self)`


        Get the local absolute paths for all version of LabVIEW development
        environment installed

        :return: Array of strings each indicating the root LV install directory
        

#### `def _get_labview_paths_windows(self)`

#### `def _open_windows_native_key(self, key, sub_key)`


        Opens a windows registry key using the OS bitness-based version of the
        registry view.
        This method eventually calls the _winreg.OpenKey() method.

        This is useful because if we're running a 32-bit python interpreter, by
        default _winreg accesses the 32-bit registry view. This is a problem on
        64-bit OSes as it limits us to registries of 32-bit applications.
        

#### `def get_active_labview_path(self)`


        Get the local absolute path for the active version of LabVIEW
        # TODO: This needs to be fixed to deal with both 32 and 64 bit
        LabVIEW for the same version installed at the same time.  It favors
        64 bit in this case.

        :return: String indicating the root LV install directory
        

#### `def _get_active_labview_windows(self)`

#### `def get_listener_vi_path(self)`

#### `def start_process(self, args)`


        Starts a process using Popen and returns its pid.
        

#### `def _get_process(self, pid, executable)`


        This function attempts to retrieve the psutil.Process for the launched
        version of LabVIEW.

        There is a possibility that the previously launched process
        has closed and a new process with the same pid has been launched,
        this will do a basic check for this by making sure the pid is
        the same LabVIEW exe, there is a very remote chance that LabVIEW
        has relaunched with the same pid, but this seems to be so
        remote and usually irrelevant to our use-cases anyway that I'm
        allowing it here.

        Returns:
            psutil.Process if exists, None otherwise
        

#### `def process_is_running(self, pid, executable)`

#### `def get_process_memory_usage(self, pid, executable)`

#### `def kill_process(self, pid, executable, timeout=None)`

#### `def copy_tree(self, source, destination)`

#### `def make_writable(directory)`

#### `def create_temp_ini(self, options={})`

### `class RemoteLabVIEWHelpers(object)`

#### `def __init__(self, host)`

#### `def is_os_64bit(self)`

#### `def get_labview_paths(self)`

#### `def get_active_labview_path(self)`

#### `def get_listener_vi_path(self)`

#### `def start_process(self, args)`

#### `def process_is_running(self, pid, executable)`

#### `def get_process_memory_usage(self, pid, executable)`

#### `def kill_process(self, pid, executable, timeout=None)`

#### `def copy_tree(self, source, destination)`

#### `def make_writable(self, directory)`

#### `def create_temp_ini(self, tokens=[])`
