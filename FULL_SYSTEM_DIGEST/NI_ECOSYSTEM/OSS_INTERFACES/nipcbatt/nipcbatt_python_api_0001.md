# NI PYTHON API DIGEST: nipcbatt

<!--NI_PYTHON_API_SNAPSHOT repo=ni/nipcbatt commit=a26fcd38af55e0286aacff6cdc44bf53b2041111 -->

<!--NI_PYTHON_API repo=nipcbatt path=scripts/clean_dll_files.py -->
## PYTHON MODULE: scripts/clean_dll_files.py

### MODULE DOCSTRING

Cleans the dll files present in python src folders

<!--NI_PYTHON_API repo=nipcbatt path=scripts/create_venvs_tree.py -->
## PYTHON MODULE: scripts/create_venvs_tree.py

### MODULE DOCSTRING

Script that should be used to create venvs tree near src folder

<!--NI_PYTHON_API repo=nipcbatt path=scripts/filesystem_utils.py -->
## PYTHON MODULE: scripts/filesystem_utils.py

### MODULE DOCSTRING

Defines a set of filesystem utility functions

### `def safe_copy_dll_file(dlls_source_folder_path: str, dlls_destination_folder_path: str, dll_file_name: str)`

Copies dll file from a given source folder into a destination folder.

    Args:
        dlls_source_folder_path (str): source folder from where dll file should be copied.
        dlls_destination_folder_path (str): destination folder where dll files
        should be copied into.
        dll_file_name (str): name of the dll file
    

<!--NI_PYTHON_API repo=nipcbatt path=scripts/install_vscode_extensions.py -->
## PYTHON MODULE: scripts/install_vscode_extensions.py

### MODULE DOCSTRING

Script that should be used to install visual code extensions 
for python development during PBCATT project

- `EXTENSIONS_FILE_NAME = 'vscode.extensions.txt'`

### `def main()`

Executes vscode extensions installation from vscode.extensions.txt

<!--NI_PYTHON_API repo=nipcbatt path=scripts/label_pyproject_with_build_number.py -->
## PYTHON MODULE: scripts/label_pyproject_with_build_number.py

### MODULE DOCSTRING

Script that should be used to label pyproject file with build number

- `PROJECT_TOML_FILE_NAME = 'pyproject.toml'`

- `PROJECT_PY_ENTRY_NAME_PROJECT = 'project'`

- `PROJECT_PY_ENTRY_NAME_VERSION = 'version'`

### `def transform_toml_pkg_version(build_number: int, pyproject_file_path: str)`

Parses pyproject.toml and replaces last digit of version entry with build number

    Args:
        build_number (int): build counter value to write into pyproject file
        pyproject_file_path (str): path into pyproject file to add build number into it
    

### `def label_pyproject(build_number: int) -> None`

Applies build number labeling to project toml file.

    Args:
        build_number (int): build counter value
    

<!--NI_PYTHON_API repo=nipcbatt path=scripts/label_pyproject_with_platform_architecture.py -->
## PYTHON MODULE: scripts/label_pyproject_with_platform_architecture.py

### MODULE DOCSTRING

Script that should be used to label pyproject file with specific plateform architecture

- `PROJECT_TOML_FILE_NAME = 'pyproject.toml'`

- `PROJECT_PY_ENTRY_NAME_PROJECT = 'project'`

- `PROJECT_PY_ENTRY_NAME_BDIST_WHEEL = ('tool', 'distutils', 'bdist_wheel')`

- `PROJECT_PY_ENTRY_NAME_BDIST_WHEEL_PLAT_NAME = 'plat-name'`

- `PROJECT_PY_ENTRY_NAME_SETUP_TOOLS_PACKAGE_DATA = ('tool', 'setuptools', 'package-data')`

- `PROJECT_PY_ENTRY_NAME_SETUP_TOOLS_PACKAGE_DATA_PCBATT_ANALYSIS = 'pcbatt_analysis'`

- `PLATFORM_TAG_WIN32 = 'win32'`

- `PLATFORM_TAG_WIN_AMD64 = 'win_amd64'`

- `SUPPORTED_PLATFORM_TAGS = [PLATFORM_TAG_WIN32, PLATFORM_TAG_WIN_AMD64]`

- `SUPPORTED_PLATFORM_TAGS_DLL_PATHS = {PLATFORM_TAG_WIN32: [f'{PLATFORM_TAG_WIN32}/NI.*.dll'], PLATFORM_TAG_WIN_AMD64: [f'{PLATFORM_TAG_WIN_AMD64}/NI.*.dll']}`

### `def transform_toml_pkg_plateform_architecture(plateform_architecture_tag: str, pyproject_file_path: str)`

Parses pyproject.toml and replaces plat-name entry

    Args:
        plateform_architecture_tag (str): platform architecture tag to write into pyproject file
        pyproject_file_path (str): path into pyproject file to add platform architecture tag into it
    

### `def label_pyproject(plateform_architecture_tag: str) -> None`

Applies plateform architecture tag labeling to project toml file.

    Args:
        plateform_architecture_tag (str): architecture tag value
    

<!--NI_PYTHON_API repo=nipcbatt path=scripts/list_supported_venvs.py -->
## PYTHON MODULE: scripts/list_supported_venvs.py

### MODULE DOCSTRING

Lists venvs variables environment

<!--NI_PYTHON_API repo=nipcbatt path=scripts/prepare_package_win32.py -->
## PYTHON MODULE: scripts/prepare_package_win32.py

### MODULE DOCSTRING

Builds x86 native DLLs then copies them into python src structure

<!--NI_PYTHON_API repo=nipcbatt path=scripts/prepare_package_win_amd64.py -->
## PYTHON MODULE: scripts/prepare_package_win_amd64.py

### MODULE DOCSTRING

Builds x64 native DLLs then copies them into python src structure

<!--NI_PYTHON_API repo=nipcbatt path=scripts/run_unittests.py -->
## PYTHON MODULE: scripts/run_unittests.py

### MODULE DOCSTRING

Provides unit tests execution script.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/__init__.py -->
## PYTHON MODULE: src/nipcbatt/__init__.py

### MODULE DOCSTRING

Provides a set of modules built on top of nidaqmx to perform PCBA electrical tests.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/__init__.py

### MODULE DOCSTRING

Provides a set of measurement analysis modules using LabVIEW libraries 
and python written functions

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/_pcbatt_analysis_internal/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/_pcbatt_analysis_internal/__init__.py

### MODULE DOCSTRING

Provides private modules of pcbatt_analysis package

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/_pcbatt_analysis_internal/_analysis_library_info.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/_pcbatt_analysis_internal/_analysis_library_info.py

### MODULE DOCSTRING

Provides private functions of analysis_library_info module.

- `NATIVE_FUNCTION_GET_LIBRARY_VERSION = 'NI_PCBATT_InteropApi_LabVIEW_Analysis_GetLibraryVersion'`

- `NATIVE_FUNCTION_IS_LABVIEW_RUNTIME_AVAILABLE = 'NI_PCBATT_InteropApi_LabVIEW_Analysis_IsLvRuntimeAvailable'`

- `NATIVE_FUNCTION_ARE_TRACES_ENABLED = 'NI_PCBATT_InteropApi_LabVIEW_Analysis_AreTracesEnabled'`

- `NATIVE_FUNCTION_ENABLE_TRACES = 'NI_PCBATT_InteropApi_LabVIEW_Analysis_EnableTraces'`

### `def get_labview_analysis_traces_folder_path_impl() -> str`

Calls function 'NI_PCBATT_InteropApi_LabVIEW_Analysis_GetTracesFolderPath' located in DLL
    'NI.PCBATT.InteropApi.dll'

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: Occurs when function call to
        'NI_PCBATT_InteropApi_LabVIEW_Analysis_GetTracesFolderPath' fails for some reason.
    

### `def call_interop_api_labview_analysis_enable_traces(traces_status: bool) -> None`

Calls function 'NI_PCBATT_InteropApi_LabVIEW_Analysis_EnableTraces' located in DLL
    'NI.PCBATT.InteropApi.dll'

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: Occurs when function call to
        'NI_PCBATT_InteropApi_LabVIEW_Analysis_EnableTraces' fails for some reason.
    

### `def call_interop_api_labview_analysis_are_traces_enabled() -> bool`

Calls function 'NI_PCBATT_InteropApi_LabVIEW_Analysis_AreTracesEnabled' located in DLL
    'NI.PCBATT.InteropApi.dll'

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: Occurs when function call to
        'NI_PCBATT_InteropApi_LabVIEW_Analysis_AreTracesEnabled' fails for some reason.
    

### `def call_interop_api_labview_analysis_lv_runtime_available()`

Calls function 'NI_PCBATT_InteropApi_LabVIEW_Analysis_IsLvRuntimeAvailable' located in DLL
    'NI.PCBATT.InteropApi.dll'

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: Occurs when function call to
        'NI_PCBATT_InteropApi_LabVIEW_Analysis_IsLvRuntimeAvailable' fails for some reason.
    

### `def call_interop_api_labview_analysis_get_library_version()`

Calls function 'NI_PCBATT_InteropApi_LabVIEW_Analysis_GetLibraryVersion' located in DLL
       'NI.PCBATT.InteropApi.dll'

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: Occurs when function call to
        'NI_PCBATT_InteropApi_LabVIEW_Analysis_GetLibraryVersion' fails for some reason.

    Returns:
        tuple[Any, int, int, int, int]: status code and library version numbers.
    

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/_pcbatt_analysis_internal/_analysis_library_interop.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/_pcbatt_analysis_internal/_analysis_library_interop.py

### MODULE DOCSTRING

Provides private module of native interop helper functions

### `def load_windows_shared_library_entries(native_library_path: str) -> CDLL`

Load content of DLL file into CDLL object

    Args:
        native_library_path (str): path into window file dll.

    Raises:
        PCBATTAnalysisLoadNativeLibraryFailedException: Occurs when loading
        of shared library fails for some reason.

    Returns:
        CDLL: An object holding windows shared library entries.
    

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/analysis_library_exceptions.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/analysis_library_exceptions.py

### MODULE DOCSTRING

Defines a set of exceptions that can be raised by analysis module.

### `class PCBATTAnalysisException(Exception)`

Defines base class for all exception raised by nipcatt.pcbatt_analysis modules.

#### `def __init__(self, message: str)`

### `class PCBATTAnalysisLoadNativeLibraryFailedException(PCBATTAnalysisException)`

Defines exception raised by nipcatt.pcbatt_analysis modules,
    when loading native library file fails for any reason.

### `class PCBATTAnalysisCallNativeLibraryFailedException(PCBATTAnalysisException)`

Defines exception raised by nipcatt.pcbatt_analysis modules,
    when calling native library function fails for any reason.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/analysis_library_info.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/analysis_library_info.py

### MODULE DOCSTRING

Defines pcbatt analysis library information elements.

### `def get_labview_analysis_traces_folder_path() -> str`

Gets the path of traces produced by analysis library.

    Returns:
        str: string path.
    

### `def is_labview_runtime_available() -> bool`

Indicates if current machine has labview runtime available.

    Returns:
        bool: True, labview runtime is available elsewhere it returns False.
    

### `def are_traces_enabled() -> bool`

Indicates whether current analysis library traces are enabled or not.

    Returns:
        bool: True, traces are enabled elsewhere it returns False.
    

### `def enable_traces(traces_status: bool) -> None`

Forces current analysis library to produce traces.

    Args:
        trace_status (bool): True, verbose traces are recorded, False, no traces are recorded.
    

### `def get_labview_analysis_available_functions_names_list() -> list[str]`

Gets the list of exported labview functions.

### `def get_labview_analysis_library_version_numbers() -> tuple[int, int, int, int]`

Gets the version information elements of labview analysis library.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/analysis_library_interop.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/analysis_library_interop.py

### MODULE DOCSTRING

Provides a set of function helpers for native interop usage.

### `def get_native_libraries_folder_name_for_windows() -> str`

Gets the name of folder containing native libraries when running
       on windows operating system.

    Raises:
        RuntimeError: Occurs when executing envrionment is not supported by current
        analysis library.

    Returns:
        str: folder name containing native libraries, win_amd64 or win32.
    

### `def load_interop_api_library_entries() -> CDLL`

Loads content of 'NI.PCBATT.InteropApi.dll' into a CDLL object
       that can be used to perform dynamic function invokation.

    Raises:
        PCBATTAnalysisLoadNativeLibraryFailedException:
        occurs when loading interop api entries fails for some reason.
    

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/analysis_library_messages.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/analysis_library_messages.py

### MODULE DOCSTRING

Defines analysis library different kinds of messages.

### `class AnalysisLibraryExceptionMessage()`

Defines analysis library exceptions messages content.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/common/base_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/common/base_types.py

### MODULE DOCSTRING

Holds base types of the package nipcbatt.pcbatt_analysis

### `class AnalysisLibraryElement()`

Defines base class of analysis library elements.

#### `def __repr__(self) -> str`

Called when repr() is invoked on the `AnalysisLibraryElement`object

        Returns:
            str: JSON string representing the object.
        

#### `def __str__(self) -> str`

Called when str() is invoked on the `AnalysisLibraryElement`object

        Returns:
            str: line string representing the object.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/common/common_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/common/common_types.py

### MODULE DOCSTRING

Holds common types of the package nipcbatt.pcbatt_analysis

### `class SpectrumPhaseUnit(IntEnum)`

Defines all supported phase units of `fft spectrum processing`

### `class SpectrumAmplitudeType(IntEnum)`

Defines all supported amplitude kinds of `fft spectrum processing`

### `class AmplitudePhaseSpectrum(AnalysisLibraryElement)`

Defines Amplitude and phase spectrum processing results,
    amplitude can be `PEAK` or `RMS`

#### `def __init__(self, f0: float, df: float, frequencies_amplitudes: numpy.ndarray[float], spectrum_amplitude_type: SpectrumAmplitudeType, spectrum_amplitude_unit_is_db: bool, frequencies_phases: numpy.ndarray[float], spectrum_phase_unit: SpectrumPhaseUnit) -> None`

Initialize an instance of `AmplitudePhaseSpectrum`.

        Args:
            f0 (`float`): start frequency of the spectrum.
            df (`float`): frequency resolution of the spectrum.
            frequencies_amplitudes (`numpy.ndarray[float]`): amplitudes of the spectrum.
            spectrum_amplitude_type (`SpectrumAmplitudeType`): spectrum amplitude type.
            spectrum_amplitude_unit_is_db (`bool`): spectrum amplitude is expressed as gain (db).
            frequencies_phases (`numpy.ndarray[float]`):phases of the spectrum.
            spectrum_phase_unit(`SpectrumPhaseUnit`): unit of the spectrum phases.

        Raises:
            ValueError: occurs when input arrays `frequencies_amplitudes`,
            `frequencies_phases` are none or empty.
            occurs when `f0` is less than zero, `df` is less or equal zero.
            occurs when `frequencies_amplitudes` and `frequencies_phases` have not same size.
        

#### `def spectrum_start_frequency(self) -> float`

Gets spectrum start frequency.

        Returns:
            float: start element of the frequency range.
        

#### `def spectrum_frequency_resolution(self) -> float`

Gets spectrum frequency resolution.

        Returns:
            float: resolution of the frequency range.
        

#### `def spectrum_frequencies(self) -> numpy.ndarray[float]`

Gets the array of frequencies axis of spectrum.

        Returns:
            `numpy.ndarray[float]`: X axis of the spectrum.
        

#### `def spectrum_amplitudes(self) -> numpy.ndarray[float]`

Gets the array of amplitude axis of the spectrum.

        Returns:
            `numpy.ndarray[float]`: Y axis of the amplitude spectrum.
        

#### `def spectrum_phases(self) -> numpy.ndarray[float]`

Gets the array of phases axis of the spectrum.

        Returns:
            `numpy.ndarray[float]`: Y axis of the phase spectrum.
        

#### `def spectrum_amplitude_unit_is_db(self) -> bool`

Gets a boolean indicating if spectrum amplitudes are expressed in db.

        Returns:
            bool: True if amplitudes are expressed in db.
        

#### `def spectrum_amplitude_type(self) -> SpectrumAmplitudeType`

Gets an enumeration value indicating kind of the spectrum amplitudes,
        `RMS` or `PEAK`.

        Returns:
            SpectrumAmplitudeType:
            `RMS`, spectrum amplitudes are RMS amplitude ie complexe magnitude,
            `PEAK` spectrum amplitudes are PEAK amplitude ie sqrt(2) * RMS amplitude
        

#### `def spectrum_phase_unit(self) -> SpectrumPhaseUnit`

Gets an enumeration value indicating unit of the spectrum phases.

        Returns:
            SpectrumPhaseUnit: `RADIAN` or `DEGREE`
        

### `class WaveformTone(AnalysisLibraryElement)`

Defines waveform tone characteristics.

#### `def __init__(self, frequency: float, amplitude: float, phase_radians: float) -> None`

Initialize an instance of `WaveformTone`.

        Raises:
            ValueError: occurs when frequency is less or equal zero,
                and occurs when amplitude is less or equal zero.

        Args:
            frequency (float): tone frequency, must be greater than zero.
            amplitude (float): tone amplitude, must be greater than zero.
            phase_radians (float): tone phase, in radians.
        

#### `def frequency(self) -> float`

Gets the frequency of the tone.

#### `def amplitude(self) -> float`

Gets the amplitude of the tone.

#### `def phase_radians(self) -> float`

Gets waveform tone phase expressed in radian

#### `def phase_degrees(self) -> float`

Gets waveform tone phase expressed in degree

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_analysis/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/waveform_analysis/__init__.py

### MODULE DOCSTRING

Provides a set of waveform analysis modules using LabVIEW libraries 
and python written functions

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_analysis/_waveform_analysis_internal/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/waveform_analysis/_waveform_analysis_internal/__init__.py

### MODULE DOCSTRING

Provides private modules of waveform analysis package

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_analysis/_waveform_analysis_internal/_amplitude_and_levels_analysis.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/waveform_analysis/_waveform_analysis_internal/_amplitude_and_levels_analysis.py

### MODULE DOCSTRING

Private module that provides a set of helper functions 
   for nipcbatt.pcbatt_analysis.amplitude_and_levels_analysis module.

### `def labview_get_last_error_message_impl() -> str`

Gets last error message hold by labview Amplitude and Levels VI.

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: Occurs when native function call fails
        for some reason.

    Returns:
        str: empty string when no error occured, elsewhere not empty string.
    

### `def labview_process_single_waveform_amplitude_and_levels_impl(waveform_samples: numpy.ndarray[numpy.float64], waveform_sampling_period_seconds: float, amplitude_and_levels_processing_method: int, histogram_size: int) -> tuple[float, float, float]`

Invokes native library Amplitude and Levels processing LabVIEW VI

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: Occurs when native dll call fails for some reason.

    Returns:
        tuple[float, float, float]: Tuple gathering, amplitude, high state and low state levels.
    

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_analysis/_waveform_analysis_internal/_dc_rms_analysis.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/waveform_analysis/_waveform_analysis_internal/_dc_rms_analysis.py

### MODULE DOCSTRING

Private module that provides a set of helper functions 
   for nipcbatt.pcbatt_analysis.dc_rms_analysis module.

### `def labview_get_last_error_message_impl() -> str`

Gets last error message hold by labview DC-RMS VI.

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: occurs when native call fails for some reason.

    Returns:
        str: last error message
    

### `def labview_process_single_waveform_dc_rms_impl(waveform_samples: numpy.ndarray[numpy.float64], waveform_sampling_period_seconds: float, dc_rms_processing_window: int) -> tuple[float, float]`

Invokes native library DC-RMS processing LabVIEW VI.

    Args:
        dc_rms_processing_window (int): 0 for Rectangular, 1 for Hann or 2 for LowSideLobe.
        waveform_samples (numpy.ndarray[float]): An array of 64bites floating points
        that will be passed to native code library.
        waveform_sampling_period_seconds (float): Sampling period of the input array of samples.

    Returns:
        tuple[float, float]: DC value and RMS value gathered in a tuple.
    

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_analysis/_waveform_analysis_internal/_frequency_domain_analysis.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/waveform_analysis/_waveform_analysis_internal/_frequency_domain_analysis.py

### MODULE DOCSTRING

Private module that provides a set of helper functions 
   for nipcbatt.pcbatt_analysis.frequency_domain_analysis module.

### `def labview_multiple_tones_measurement_get_last_error_message_impl() -> str`

Gets LabVIEW VI last error message.

### `def labview_fft_spectrum_amplitude_phase_get_last_error_message_impl() -> str`

Gets LabVIEW VI last error message.

### `def labview_process_single_waveform_amplitude_phase_spectrum_impl(waveform_samples: numpy.ndarray[numpy.float64], waveform_sampling_period_seconds: float, spectrum_amplitude_must_be_db: bool, spectrum_amplitude_type: SpectrumAmplitudeType, spectrum_phase_unit: SpectrumPhaseUnit, fft_spectrum_window: int, fft_spectrum_window_advanced_parameter: float=None) -> AmplitudePhaseSpectrum`

Processes amplitude phase spectrum of a given waveform samples using LabVIEW VI

    Args:
        waveform_samples (`numpy.ndarray[numpy.float64]`): samples of the waveform to process.
        waveform_sampling_period_seconds (`float`): sampling period of the waveform to process.
        spectrum_amplitude_must_be_db (`bool`): amplitudes of the spectrum should
        be expressed as db gain, instead of nominal unit.
        spectrum_amplitude_type (`FftSpectrumAmplitudeType`): can be `RMS` or `PEAK`.
        spectrum_phase_unit (`FftSpectrumPhaseUnit`): can be `RADIAN` or `DEGREE`.
        fft_spectrum_window (`FftSpectrumWindow`): fft processing window.
        fft_spectrum_window_advanced_parameter (`float`): advanced parameter value,
        only used when selected window is `KAISER`, `DOLPH_TCHEBYCHEV` or `GAUSSIAN`.

    Raises:
        PCBATTAnalysisException:
            Occurs when multiple tones processing fails for some reason.

    Returns:
        AmplitudePhaseSpectrum: An object that holds result of fft spectrum
        processing result using LabVIEW VI.
    

### `def labview_process_single_waveform_multiple_tones_impl(waveform_samples: numpy.ndarray[numpy.float64], waveform_sampling_period_seconds: float, tones_selection_threshold: float, tones_max_count: int, tones_sorting_mode: int) -> tuple[list[WaveformTone], SpectrumAmplitudeType]`

Processes multiple tones of a given waveform samples using LabVIEW VI

    Args:
        waveform_samples (`numpy.ndarray[numpy.float64]`): samples of the waveform to process.
        waveform_sampling_period_seconds (`float`): sampling period of the waveform to process.
        tones_selection_threshold (`float`): minimum amplitude peak of tone to be selected.
        tones_max_count (`int`): maximum tones count to extract from analyzed waveform.
        tones_sorting_mode (`TonesSortingMode`): sorting of the output tones list.

    Raises:
        PCBATTAnalysisException:
            Occurs when multiple tones processing fails for some reason.

    Returns:
        MultipleTonesMeasurementResult: An object that holds result of multiple tones
        processing result using LabVIEW VI.
    

### `def labview_process_single_waveform_multiple_tones_and_amplitude_phase_spectrum_impl(waveform_samples: numpy.ndarray[numpy.float64], waveform_sampling_period_seconds: float, spectrum_amplitude_must_be_db: bool, spectrum_phase_unit: SpectrumPhaseUnit, fft_spectrum_window: int, tones_sorting_mode: int, tones_selection_threshold_peak_amplitude: float, tones_max_count: int=None, fft_spectrum_window_advanced_parameter: float=None)`

Processes amplitude phase spectrum of a given waveform samples using LabVIEW VI

    Args:
        waveform_samples (`numpy.ndarray[numpy.float64]`): samples of the waveform to process.
        waveform_sampling_period_seconds (`float`): sampling period of the waveform to process.
        spectrum_amplitude_must_be_db (`bool`): amplitudes of the spectrum should
        be expressed as db gain, instead of nominal unit.
        spectrum_phase_unit (`FftSpectrumPhaseUnit`): can be `RADIAN` or `DEGREE`.
        fft_spectrum_window (`FftSpectrumWindow`): fft processing window.
        fft_spectrum_window_advanced_parameter (`float`): advanced parameter value,
        only used when selected window is `KAISER`, `DOLPH_TCHEBYCHEV` or `GAUSSIAN`.
        tones_selection_threshold_peak_amplitude (`float`): minimum amplitude peak of tone to be selected.
        tones_max_count (`int`): maximum tones count to extract from analyzed waveform,
        when not set, all tones will be extracted.

    Raises:
        PCBATTAnalysisException:
            Occurs when frequency domain processing fails for some reason.

    Returns:
        FrequencyDomainProcessingResult: An object that holds result of fft spectrum
        processing result and multiple tones processing result using LabVIEW VIs.
    

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_analysis/_waveform_analysis_internal/_pulse_analog_analysis.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/waveform_analysis/_waveform_analysis_internal/_pulse_analog_analysis.py

### MODULE DOCSTRING

Private module that provides a set of helper functions 
   for nipcbatt.pcbatt_analysis.pulse_analog_analysis module.

### `def labview_get_last_error_message_impl() -> str`

Gets last error message hold by labview Pulse Measurements VI.

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: Occurs when native function call fails
        for some reason.

    Returns:
        str: empty string when no error occured, elsewhere not empty string.
    

### `def labview_process_single_waveform_pulse_measurements_ref_levels_absolute_export_all_impl(waveform_samples: numpy.ndarray[numpy.float64], waveform_sampling_period_seconds: float, pulse_number: int, processing_polarity: int, reference_levels: TuplePulseReferenceLevels) -> TuplePulseResultsExportAll`

Invokes native library Pulse Measurements processing LabVIEW VI

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException:
            Occurs when native dll call fails for some reason.

    Returns:
        PulseResultsExportAll: Tuple gathering, exported all pulse measurement results.
    

### `def labview_process_single_waveform_pulse_measurements_ref_levels_relative_export_all_impl(waveform_samples: numpy.ndarray[numpy.float64], waveform_sampling_period_seconds: float, pulse_number: int, processing_polarity: int, amplitude_and_levels_processing_method: int, amplitude_and_levels_processing_histogram_size: int, reference_levels: TuplePulseReferenceLevels) -> TuplePulseResultsExportAll`

Invokes native library Pulse Measurements processing LabVIEW VI

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException:
            Occurs when native dll call fails for some reason.

    Returns:
        PulseResultsExportAll: Tuple gathering, exported all pulse measurement results.
    

### `def labview_process_single_waveform_pulse_measurements_ref_levels_absolute_export_no_periodicity_impl(waveform_samples: numpy.ndarray[numpy.float64], waveform_sampling_period_seconds: float, pulse_number: int, processing_polarity: int, reference_levels: TuplePulseReferenceLevels) -> TuplePulseResultsExportIgnorePeriodicity`

Invokes native library Pulse Measurements processing LabVIEW VI

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException:
            Occurs when native dll call fails for some reason.

    Returns:
        PulseResultsExportAll: Tuple gathering, exported all pulse measurement results.
    

### `def labview_process_single_waveform_pulse_measurements_ref_levels_relative_export_no_periodicity_impl(waveform_samples: numpy.ndarray[numpy.float64], waveform_sampling_period_seconds: float, pulse_number: int, processing_polarity: int, amplitude_and_levels_processing_method: int, amplitude_and_levels_processing_histogram_size: int, reference_levels: TuplePulseReferenceLevels) -> TuplePulseResultsExportIgnorePeriodicity`

Invokes native library Pulse Measurements processing LabVIEW VI

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException:
            Occurs when native dll call fails for some reason.

    Returns:
        TuplePulseResultsExportIgnorePeriodicity: Tuple gathering, exported all pulse measurement results.
    

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_analysis/amplitude_and_levels_analysis.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/waveform_analysis/amplitude_and_levels_analysis.py

### MODULE DOCSTRING

Provides Amplitude And Levels analysis tools

### `class AmplitudeAndLevelsProcessingResult(AnalysisLibraryElement)`

Defines Amplitude and Levels processing results

#### `def __init__(self, amplitude: float, high_state_level: float, low_state_level: float) -> None`

Initialize an instance of Amplitude and Levels processing result.

        Args:
            amplitude (float): Amplitude value obtained after processing waveform.
            high_state_level (float): High state level obtained after processing waveform.
            low_state_level (float): Low state level obtained after processing waveform.
        

#### `def amplitude(self) -> float`

Gets amplitude value obtained after processing waveform.

        Returns:
            float: amplitude is the difference between high state level and low state level.
        

#### `def high_state_level(self) -> float`

Gets high state level value obtained after processing waveform.

        Returns:
            float: High state level value.
        

#### `def low_state_level(self) -> float`

Gets low state level value obtained after processing waveform.

        Returns:
            float: Low state level value.
        

### `class AmplitudeAndLevelsProcessingMethod(IntEnum)`

Defines Amplitude and levels processing method

### `class LabViewAmplitudeAndLevels(AnalysisLibraryElement)`

Provides Amplitude and Levels processing based on LabVIEW Amplitude and Levels VI

#### `def get_last_error_message() -> str`

Gets the message content of the last occurred error of
        `Amplitude and levels` processing labview VI.

        Returns:
            str: Empty string when no error occured, elsewhere not empty string.
        

#### `def process_single_waveform_amplitude_and_levels(waveform_samples: numpy.ndarray[numpy.float64], waveform_sampling_period_seconds: float, amplitude_and_levels_processing_method: AmplitudeAndLevelsProcessingMethod, histogram_size: int) -> AmplitudeAndLevelsProcessingResult`

Processes amplitude and levels of a given waveform samples using LabVIEW VI

        Args:
            waveform_samples (numpy.ndarray[numpy.float64]): samples of the waveform to process.
            waveform_sampling_period_seconds (float): sampling period of the waveform to process.
            amplitude_and_levels_processing_method (AmplitudeAndLevelsProcessingMethod):
                amplitude and levels processing method.
            histogram_size (int):
                histogram bins count that will be used when labview decides to use histogram method.

        Raises:
            PCBATTAnalysisException:
                Occurs when amplitude and levels processing fails for some reason.

        Returns:
            AmplitudeAndLevelsProcessingResult: An object that holds result of amplitude and levels
            processing result using LabVIEW VI.
        

#### `def process_multiple_waveforms_amplitude_and_levels(waveforms_samples: Iterable[numpy.ndarray[numpy.float64]], waveforms_sampling_period_seconds: float, amplitude_and_levels_processing_method: AmplitudeAndLevelsProcessingMethod, histogram_size: int) -> Iterable[AmplitudeAndLevelsProcessingResult]`

Processes amplitude and levels of given waveforms samples provided as iterable object using LabVIEW VI

        Args:
            waveforms_samples (Iterable[numpy.ndarray[numpy.float64]]): iterable of single waveforms.
            waveforms_sampling_period_seconds (float): common sampling rate of all waveforms.
            amplitude_and_levels_processing_method (AmplitudeAndLevelsProcessingMethod): amplitude and levels processing method.
            histogram_size (int): histogram bins count that will be used when labview decides to use histogram method.

        Raises:
            PCBATTAnalysisException:
                Occurs when amplitude and levels processing fails for some reason.

        Returns:
            Iterable[AmplitudeAndLevelsProcessingResult]: An iterable of objects that hold result of
            amplitude and levels processing of each input waveform using LabVIEW VI.

        Yields:
            Iterator[Iterable[AmplitudeAndLevelsProcessingResult]]: objects that hold result of
            amplitude and levels processing of each input waveform using LabVIEW VI.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_analysis/dc_rms_analysis.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/waveform_analysis/dc_rms_analysis.py

### MODULE DOCSTRING

Provides DC-RMS analysis tools

### `class DcRmsProcessingResult(AnalysisLibraryElement)`

Defines DC-RMS processing results

#### `def __init__(self, dc_value: float, rms_value: float) -> None`

Initialize an instance of DC-RMS processing result.

        Args:
            dc_value (float): DC value obtained after processing waveform.
            rms_value (float): RMS value obtained after processing waveform.
        

#### `def dc_value(self) -> float`

Gets DC value obtained after processing waveform.

        Returns:
            float: DC value.
        

#### `def rms_value(self) -> float`

Gets RMS value obtained after processing waveform.

        Returns:
            float: RMS value.
        

### `class DcRmsProcessingWindow(IntEnum)`

Defines DC-RMS processing window

### `class LabViewBasicDcRms(AnalysisLibraryElement)`

Provides DC-RMS processing based on LabVIEW Basic DC-RMS VI

#### `def get_last_error_message() -> str`

Gets the message content of the last occured error of
        DC-RMS processing labview VI.

        Returns:
            str: Empty string when no error occured, elsewhere not empty string.
        

#### `def process_single_waveform_dc_rms(waveform_samples: numpy.ndarray[numpy.float64], waveform_sampling_period_seconds: float, dc_rms_processing_window: DcRmsProcessingWindow) -> DcRmsProcessingResult`

Processes DC-RMS of a given waveform samples using LabVIEW VI.

        Args:
            waveform_samples (numpy.ndarray[numpy.float64]): single waveform samples.
            waveforms_sampling_period_seconds (float): sampling rate of the single waveform.
            dc_rms_processing_window (DcRmsProcessingWindow): DC-RMS processing window.

        Returns:
            DcRmsProcessingResult: An object that holds result of DC-RMS
            processing result using LabVIEW VI.
        

#### `def process_multiple_waveforms_dc_rms(waveforms_samples: Iterable[numpy.ndarray[numpy.float64]], waveforms_sampling_period_seconds: float, dc_rms_processing_window: DcRmsProcessingWindow) -> Iterable[DcRmsProcessingResult]`

Processes DC-RMS of given waveforms samples provided as iterable object using LabVIEW VI

        Args:
            waveforms_samples (Iterable[numpy.ndarray[numpy.float64]]): iterable of single waveforms
            waveforms_sampling_period_seconds (float): common sampling rate of all waveforms
            dc_rms_processing_window (DcRmsProcessingWindow): DC-RMS processing window

        Returns:
            Iterable[DcRmsProcessingResult]: An iterable of objects that hold result of
            DC-RMS processing of each input waveform using LabVIEW VI.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_analysis/frequency_domain_analysis.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/waveform_analysis/frequency_domain_analysis.py

### MODULE DOCSTRING

Provides frequency domain analysis tools

### `class LabViewTonesSortingMode(IntEnum)`

Defines how should be sorted tone analysis results.

### `class LabViewFftSpectrumWindow(IntEnum)`

Defines all supported signal `fft processing` time windows.

### `class MultipleTonesProcessingResult(AnalysisLibraryElement)`

Defines multiple tones processing results

#### `def __init__(self, detected_tones: list[WaveformTone], amplitude_type: SpectrumAmplitudeType) -> None`

Initializes an instance of `MultipleTonesProcessingResult`

        Args:
            detected_tones (`list[WaveformTone]`): list of waveform tones.
            amplitude_type (`SpectrumAmplitudeType`): amplitude type of the waveform tones.

        Raises:
            ValueError: Occurs when input `detected_tones` list is none.
        

#### `def detected_tones(self) -> list[WaveformTone]`

Gets the list of the tones detected in analyzed waveform.

        Returns:
            list[WaveformTone]: list of waveform tones.
        

#### `def amplitude_type(self) -> SpectrumAmplitudeType`

Gets the kind amplitudes of the tones detected in analyzed waveform.

        Returns:
            SpectrumAmplitudeType: amplitude type `RMS` or `PEAK`.
        

### `class MultipleTonesAmplitudePhaseSpectrumProcessingResult(AnalysisLibraryElement)`

Defines multiple tones and spectrum processing results

#### `def __init__(self, multiple_tones_result: MultipleTonesProcessingResult, amplitude_phase_spectrum: AmplitudePhaseSpectrum) -> None`

Initialize an instance of `MultipleTonesAmplitudePhaseSpectrumProcessingResult`.

        Args:
            multiple_tones_result (`MultipleTonesProcessingResult`):
                holds multiple tones processing results.
            amplitude_phase_spectrum (`AmplitudePhaseSpectrum`):
                holds fft spectrum processing results.

        Raises:
            ValueError: Occurs when input `multiple_tones_result` or
            `amplitude_phase_spectrum` are none.
        

#### `def multiple_tones_result(self) -> MultipleTonesProcessingResult`

Gets multiple tones processing results of analyzed waveform.

        Returns:
            MultipleTonesProcessingResult: multiple tones processing result.
        

#### `def amplitude_phase_spectrum(self) -> AmplitudePhaseSpectrum`

Gets fft spectrum processing results of analyzed waveform.

        Returns:
            AmplitudePhaseSpectrum: fft spectrum processing result.
        

### `class LabViewFrequencyDomainProcessing(AnalysisLibraryElement)`

Defines frequency domain analysis functions such
    fft spectrum and multiple tones processing.

#### `def process_single_waveform_multiple_tones_and_amplitude_phase_spectrum(waveform_samples: numpy.ndarray[numpy.float64], waveform_sampling_period_seconds: float, spectrum_amplitude_must_be_db: bool, spectrum_phase_unit: SpectrumPhaseUnit, fft_spectrum_window: LabViewFftSpectrumWindow, tones_sorting_mode: LabViewTonesSortingMode, tones_selection_threshold_peak_amplitude: float, tones_max_count: int=None, fft_spectrum_window_advanced_parameter: float=None) -> MultipleTonesAmplitudePhaseSpectrumProcessingResult`

Processes `RMS` amplitude phase spectrum of a given waveform samples using LabVIEW VI

        Args:
            waveform_samples (`numpy.ndarray[numpy.float64]`): samples of the waveform to process.
            waveform_sampling_period_seconds (`float`): sampling period of the waveform to process.
            spectrum_amplitude_must_be_db (`bool`): amplitudes of the spectrum should
            be expressed as db gain, instead of nominal unit.
            spectrum_phase_unit (`FftSpectrumPhaseUnit`): can be `RADIAN` or `DEGREE`.
            fft_spectrum_window (`LabViewFftSpectrumWindow`): fft processing window.
            fft_spectrum_window_advanced_parameter (`float`): advanced parameter value,
            only used when selected window is `KAISER`, `DOLPH_TCHEBYCHEV` or `GAUSSIAN`.
            tones_selection_threshold_peak_amplitude (`float`): minimum amplitude peak of tone to be selected.
            tones_max_count (`int`): maximum tones count to extract from analyzed waveform,
            when not set, all tones will be extracted.

        Raises:
            PCBATTAnalysisException:
                Occurs when frequency domain processing fails for some reason.

        Returns:
            FrequencyDomainProcessingResult: An object that holds result of fft spectrum
            processing result and multiple tones processing result using LabVIEW VIs.
        

### `class LabViewFftSpectrumAmplitudePhase(AnalysisLibraryElement)`

Provides Amplitude/Phase spectrum processing based on
    `LabVIEW FFT Spectrum Magnitude Phase VI`

#### `def get_last_error_message() -> str`

Gets the message content of the last occurred error of
        ``FFT Spectrum Magnitude and Phase`` labview VI.

        Returns:
            str: Empty string when no error occurred, elsewhere not empty string.
        

#### `def process_single_waveform_amplitude_phase_spectrum(waveform_samples: numpy.ndarray[numpy.float64], waveform_sampling_period_seconds: float, spectrum_amplitude_must_be_db: bool, spectrum_amplitude_type: SpectrumAmplitudeType, spectrum_phase_unit: SpectrumPhaseUnit, fft_spectrum_window: LabViewFftSpectrumWindow, fft_spectrum_window_advanced_parameter: float=None) -> AmplitudePhaseSpectrum`

Processes amplitude phase spectrum of a given waveform samples using LabVIEW VI

        Args:
            waveform_samples (`numpy.ndarray[numpy.float64]`): samples of the waveform to process.
            waveform_sampling_period_seconds (`float`): sampling period of the waveform to process.
            spectrum_amplitude_must_be_db (`bool`): amplitudes of the spectrum should
            be expressed as db gain, instead of nominal unit.
            spectrum_amplitude_type (`FftSpectrumAmplitudeType`): can be `RMS` or `PEAK`.
            spectrum_phase_unit (`FftSpectrumPhaseUnit`): can be `RADIAN` or `DEGREE`.
            fft_spectrum_window (`FftSpectrumWindow`): fft processing window.
            fft_spectrum_window_advanced_parameter (`float`): advanced parameter value,
            only used when selected window is `KAISER`, `DOLPH_TCHEBYCHEV` or `GAUSSIAN`.

        Raises:
            PCBATTAnalysisException:
                Occurs when multiple tones processing fails for some reason.

        Returns:
            AmplitudePhaseSpectrum: An object that holds result of fft spectrum
            processing result using LabVIEW VI.
        

### `class LabViewMultipleTonesMeasurement(AnalysisLibraryElement)`

Provides multiple tones processing based on
    `LabVIEW Multiple Tone Information VI`

#### `def get_last_error_message() -> str`

Gets the message content of the last occurred error of
        ``Multiple Tones Measurements`` labview VI.

        Returns:
            str: Empty string when no error occurred, elsewhere not empty string.
        

#### `def process_single_waveform_multiple_tones(waveform_samples: numpy.ndarray[numpy.float64], waveform_sampling_period_seconds: float, tones_selection_threshold: float, tones_max_count: int, tones_sorting_mode: LabViewTonesSortingMode) -> MultipleTonesProcessingResult`

Processes multiple tones of a given waveform samples using LabVIEW VI

        Args:
            waveform_samples (`numpy.ndarray[numpy.float64]`): samples of the waveform to process.
            waveform_sampling_period_seconds (`float`): sampling period of the waveform to process.
            tones_selection_threshold (`float`): minimum amplitude peak of tone to be selected.
            tones_max_count (`int`): maximum tones count to extract from analyzed waveform.
            tones_sorting_mode (`TonesSortingMode`): sorting of the output tones list.

        Raises:
            PCBATTAnalysisException:
                Occurs when multiple tones processing fails for some reason.

        Returns:
            MultipleTonesMeasurementResult: An object that holds result of multiple tones
            processing result using LabVIEW VI.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_analysis/pulse_analog_analysis.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/waveform_analysis/pulse_analog_analysis.py

### MODULE DOCSTRING

Provides pulse analog analysis tools

### `class WaveformPeriodicityAnalogProcessingResult(AnalysisLibraryElement)`

Defines pulse periodicity related measurements analog processing results

#### `def __init__(self, period: float, duty_cycle: float) -> None`

Initialize an instance of waveform periodicty processing result.

        Args:
            period (float): period value obtained after processing waveform.
            duty_cycle (float): duty cycle value obtained after processing waveform,
                expressed as ratio [0,1].
        

#### `def period(self) -> float`

Gets period value obtained after processing waveform.

        Returns:
            float: period value.
        

#### `def frequency(self) -> float`

Gets frequency value obtained after processing waveform.

        Returns:
            float: period value.
        

#### `def duty_cycle(self) -> float`

Gets duty cycle value obtained after processing waveform expressed as ratio in [0,1].

        Returns:
            float: duty cycle ratio value.
        

#### `def duty_cycle_percent(self) -> float`

Gets duty cycle value obtained after processing waveform expressed as percentage.

        Returns:
            float: duty cycle ratio value.
        

### `class PulseAnalogProcessingResult(AnalysisLibraryElement)`

Defines pulse measurements analog processing results

#### `def __init__(self, pulse_center: float, pulse_duration: float, pulse_reference_level_high: float, pulse_reference_level_middle: float, pulse_reference_level_low: float, period: float=None, duty_cycle: float=None) -> None`

Initialize an instance of pulse analog processing result.

        Args:
            pulse_center (float): pulse center is defined as (Tr+Tf)/2
            pulse_duration (float): pulse duration is the time difference in seconds between
                the first two mid ref level crossings of the analyzed pulse,
                pulse duration is also known as pulse width.
            pulse_reference_level_high (float):
                absolute high reference level used to evaluate pulse center.
            pulse_reference_level_middle (float):
                absolute middle reference level used to evaluate pulse center.
            pulse_reference_level_low (float):
                absolute low reference level used to evaluate pulse center.
            period (float, optional):
                time between adjacent mid ref level crossings the same direction in seconds.
                Defaults to None.
            duty_cycle (float, optional): fraction of period according to analyzed pulse.
                Defaults to None.
        

#### `def pulse_center(self) -> float`

Gets center date obtained after processing waveform pulse.

        Returns:
            float: Pulse center date expressed in seconds.
        

#### `def pulse_duration(self) -> float`

Gets pulse width obtained after processing waveform pulse.

        Returns:
            float: Pulse width expressed in seconds.
        

#### `def pulse_reference_level_high(self) -> float`

Gets high reference level used when processed waveform pulse.

        Returns:
            float: High reference level value.
        

#### `def pulse_reference_level_middle(self) -> float`

Gets middle reference level used when processed waveform pulse.

        Returns:
            float: Middle reference level value.
        

#### `def pulse_reference_level_low(self) -> float`

Gets low reference level used when processed waveform pulse.

        Returns:
            float: Low reference level value.
        

#### `def waveform_periodicity_processing_result(self) -> Optional[WaveformPeriodicityAnalogProcessingResult]`

Gets periodicity analysis results obtained when processed waveform pulses, can be None.

        Returns:
            Optional[WaveformPeriodicityAnalogProcessingResult]:
                periodicity analysis results obtained when processed waveform
        

### `class PulseAnalogProcessingPolarity(IntEnum)`

Defines pulse analog processing polarity.

### `class PulseAnalogProcessingReferenceLevelsUnit(IntEnum)`

Defines pulse analog processing reference levels unit.

### `class PulseAnalogProcessingExportMode(IntEnum)`

Defines labview pulse processing export mode.

### `class PulseAnalogProcessingReferenceLevels(AnalysisLibraryElement)`

Defines reference levels that will be used to locate pulse when
    analyzing waveform.
    

#### `def __init__(self, reference_level_high: float, reference_level_middle: float, reference_level_low: float)`

#### `def reference_level_high(self) -> float`

Gets high reference level used when processed waveform pulse.

        Returns:
            float: High reference level value.
        

#### `def reference_level_middle(self) -> float`

Gets middle reference level used when processed waveform pulse.

        Returns:
            float: Middle reference level value.
        

#### `def reference_level_low(self) -> float`

Gets low reference level used when processed waveform pulse.

        Returns:
            float: Low reference level value.
        

### `class PulseAnalogMeasurementPercentLevelsSettings(AnalysisLibraryElement)`

Defines settings to use when reference levels
    required for pulse analysis are expressed as percentage.

#### `def __init__(self, amplitude_and_levels_processing_method: AmplitudeAndLevelsProcessingMethod, histogram_size: int) -> None`

Initialize an instance of `PulseAnalogMeasurementPercentLevelsSettings`.

        Args:
            amplitude_and_levels_processing_method (AmplitudeAndLevelsProcessingMethod):
                Amplitude and levels processing method.
            histogram_size (int):
                Number of bins of the histogram when amplitude and levels processing choose to use
                histogram based algorithm.
        

#### `def amplitude_and_levels_processing_method(self) -> int`

Gets method that will be used when processing waveform states.

        Returns:
            int: Amplitude and levels processing method.
        

#### `def histogram_size(self) -> int`

Gets histogram size, ie, bins count, that will be used when processing waveform states.

        Returns:
            int: histogram bins count.
        

### `class LabViewPulseAnalogMeasurements(AnalysisLibraryElement)`

Provides pulse analog processing based on ``LabVIEW Pulse Measurements`` VI

#### `def get_last_error_message() -> str`

Gets the message content of the last occured error of
        ``Pulse Measurements`` labview VI.

        Returns:
            str: Empty string when no error occured, elsewhere not empty string.
        

#### `def process_single_waveform_multiple_pulse_measurements(waveform_samples: numpy.ndarray[numpy.float64], waveform_sampling_period_seconds: float, waveform_t0: float, export_mode: PulseAnalogProcessingExportMode, processing_polarity: PulseAnalogProcessingPolarity, reference_levels_unit: PulseAnalogProcessingReferenceLevelsUnit, reference_levels: PulseAnalogProcessingReferenceLevels, percent_levels_settings: Optional[PulseAnalogMeasurementPercentLevelsSettings]) -> Iterable[PulseAnalogProcessingResult]`

Processes multiple pulse measurements of a
        given single waveform samples using LabVIEW VI.

        Args:
            waveform_samples (numpy.ndarray[numpy.float64]): single waveform samples.
            waveform_sampling_period_seconds (float): sampling rate of the single waveform
            waveform_t0 (float): waveform start date t0.
            export_mode (PulseAnalogProcessingExportMode):
                pulse analysis results exportation mode.
            processing_polarity (PulseAnalogProcessingPolarity):
                pulse polarity that will be analyzed (high or low),
                when high, rising edge crossing middle level
                    then falling edge crossing middle level are analyzed,
                when low, falling edge crossing middle level
                    then rising edge crossing middle level are analyzed.
            reference_levels_unit (PulseAnalogProcessingReferenceLevelsUnit):
                unit of the reference levels.
            reference_levels (PulseAnalogProcessingReferenceLevels):
                reference levels that will be used to delimit pulse phases in waveform.
            percent_levels_settings (Optional[PulseAnalogMeasurementPercentLevelsSettings]):
                state settings when reference levels unit is percent, igonred if absolute.

        Raises:
            ValueError:
                Occurs when one of provided input arguments is invalid.
            PCBATTAnalysisException:
                Occurs when analysis fails for some reason.

        Returns:
            Iterable[PulseAnalogProcessingResult]: an object that holds multiple results of pulse
            processing result using LabVIEW VI.
        

#### `def process_single_waveform_pulse_measurements(waveform_samples: numpy.ndarray[numpy.float64], waveform_sampling_period_seconds: float, waveform_t0: float, pulse_number: int, export_mode: PulseAnalogProcessingExportMode, processing_polarity: PulseAnalogProcessingPolarity, reference_levels_unit: PulseAnalogProcessingReferenceLevelsUnit, reference_levels: PulseAnalogProcessingReferenceLevels, percent_levels_settings: Optional[PulseAnalogMeasurementPercentLevelsSettings]) -> PulseAnalogProcessingResult`

Processes pulse measurements of a given single waveform samples using LabVIEW VI.

        Args:
            waveform_samples (numpy.ndarray[numpy.float64]): single waveform samples.
            waveform_sampling_period_seconds (float): sampling rate of the single waveform
            waveform_t0 (float): waveform start date t0.
            pulse_number (int): index of the pulse that will be analyzed (starts from 1).
            export_mode (PulseAnalogProcessingExportMode):
                pulse analysis results exportation mode.
            processing_polarity (PulseAnalogProcessingPolarity):
                pulse polarity that will be analyzed (high or low),
                when high, rising edge crossing middle level
                    then falling edge crossing middle level are analyzed,
                when low, falling edge crossing middle level
                    then rising edge crossing middle level are analyzed.
            reference_levels_unit (PulseAnalogProcessingReferenceLevelsUnit):
                unit of the reference levels.
            reference_levels (PulseAnalogProcessingReferenceLevels):
                reference levels that will be used to delimit pulse phases in waveform.
            percent_levels_settings (Optional[PulseAnalogMeasurementPercentLevelsSettings]):
                state settings when reference levels unit is percent, igonred if absolute.

        Raises:
            ValueError:
                Occurs when one of provided input arguments is invalid.
            PCBATTAnalysisException:
                Occurs when analysis fails for some reason.

        Returns:
            PulseAnalogProcessingResult: An object that holds result of pulse
            processing result using LabVIEW VI.
        

#### `def process_multiple_waveforms_pulse_measurements(waveforms_samples: Iterable[numpy.ndarray[numpy.float64]], waveforms_sampling_period_seconds: float, waveforms_t0: Iterable[float], pulse_number: int, export_mode: PulseAnalogProcessingExportMode, processing_polarity: PulseAnalogProcessingPolarity, reference_levels_unit: PulseAnalogProcessingReferenceLevelsUnit, reference_levels: PulseAnalogProcessingReferenceLevels, percent_levels_settings: Optional[PulseAnalogMeasurementPercentLevelsSettings]) -> Iterable[PulseAnalogProcessingResult]`

Processes pulse measurement of a given multiple waveforms samples using LabVIEW VI.

        Args:
            waveforms_samples (Iterable[numpy.ndarray[numpy.float64]]): multiple waveforms samples.
            waveforms_sampling_period_seconds (float): common sampling rate of all waveforms.
            waveforms_t0 (Iterable[float]): for each waveform start date t0.
            pulse_number (int): index of the pulse that will be analyzed (starts from 1).
            export_mode (PulseAnalogProcessingExportMode): pulse analysis results exportation mode.
            processing_polarity (PulseAnalogProcessingPolarity): pulse polarity that will
                be analyzed (high or low).
            reference_levels_unit (PulseAnalogProcessingReferenceLevelsUnit):
                unit of the reference levels.
            reference_levels (PulseAnalogProcessingReferenceLevels):
                reference levels that will be used to delimit pulse phases in waveforms.
            percent_levels_settings (Optional[PulseAnalogMeasurementPercentLevelsSettings]):
                state settings when reference levels unit is percent, igonred if absolute.

        Returns:
            Iterable[PulseAnalogProcessingResult]: An iterable of objects that hold result of
            pulse measurements processing of each input waveform using LabVIEW VI.

        Raises:
            ValueError:
                Occurs when one of provided input arguments is invalid.
            PCBATTAnalysisException:
                Occurs when analysis fails for some reason.

        Yields:
            Iterator[Iterable[PulseAnalogProcessingResult]]: objects that hold result of
            pulse measurements processing of each input waveform using LabVIEW VI.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_creation/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/waveform_creation/__init__.py

### MODULE DOCSTRING

Provides a set of waveform creation modules using python written functions

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_creation/_waveform_creation_internal/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/waveform_creation/_waveform_creation_internal/__init__.py

### MODULE DOCSTRING

Provides private modules of waveform creation package

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_creation/_waveform_creation_internal/_multitones_waveform.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/waveform_creation/_waveform_creation_internal/_multitones_waveform.py

### MODULE DOCSTRING

Private module that provides a set of helper functions 
   for `multitones_waveform` module.

### `def create_multitones_waveform_impl(amplitude: float, waveform_tones: list[WaveformTone], samples_count: int, sampling_rate: float, amplitude_normalization_threshold: float=1e-06) -> numpy.ndarray[numpy.float64]`

Creates samples of a multitones waveform described through its characteristics.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_creation/_waveform_creation_internal/_sine_waveform.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/waveform_creation/_waveform_creation_internal/_sine_waveform.py

### MODULE DOCSTRING

Private module that provides a set of helper functions
   for `sine_waveform` module.

### `def create_cosine_waveform_impl(amplitude: float, frequency: float, phase: float, offset: float, samples_count: int, sampling_rate: float) -> numpy.ndarray[numpy.float64]`

Creates samples of a cosine waveform described through its characteristics.

### `def create_sine_waveform_impl(amplitude: float, frequency: float, phase: float, offset: float, samples_count: int, sampling_rate: float) -> numpy.ndarray[numpy.float64]`

Creates samples of a sine waveform described through its characteristics.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_creation/_waveform_creation_internal/_square_waveform.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/waveform_creation/_waveform_creation_internal/_square_waveform.py

### MODULE DOCSTRING

Private module that provides a set of helper functions 
   for `square_waveform` module.

### `def create_square_waveform_impl(amplitude: float, frequency: float, duty_cycle: float, phase: float, offset: float, samples_count: int, sampling_rate: float) -> numpy.ndarray[numpy.float64]`

Creates samples of a square waveform described through its characteristics.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_creation/multitones_waveform.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/waveform_creation/multitones_waveform.py

### MODULE DOCSTRING

Provides multiple tones waveform creation API.

### `def create_multitones_waveform(multitones_amplitude: float, waveform_tones: list[WaveformTone], samples_count: int, sampling_rate: float, amplitude_normalization_threshold: float=1e-06) -> numpy.ndarray[numpy.float64]`

Creates samples of a multi-tones waveform described through its characteristics.

    Args:
        multitones_amplitude (float): amplitude of the multi-tones waveform,
        must be greater than zero.
        waveform_tones (list[WaveformTone]): describes the distribution of tones
        that will be contained in the created waveform.
        samples_count (int): number of samples that will be created for the multi-tones waveform.
        sampling_rate (float): sampling rate of the multi-tones waveform.
        amplitude_normalization_threshold(float): when waveform maximum is greater than it,
            normalization of the amplitude is applied to match input `multitones_amplitude`.

    Raises:
        PCBATTAnalysisException: occurs when waveform creation fails for some reason.
        ValueError: occurs when samples_count is less or equal zero,
            when sampling_rate is less or equal zero,
            and when amplitude_normalization_threshold is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: samples constituting created multi-tones waveform.
    

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_creation/sine_waveform.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/waveform_creation/sine_waveform.py

### MODULE DOCSTRING

Provides sine waveform creation API.

### `def create_cosine_waveform(amplitude: float, frequency: float, phase: float, offset: float, samples_count: int, sampling_rate: float) -> numpy.ndarray[numpy.float64]`

Creates samples of a sine waveform described through its characteristics, using math.cos.

    Args:
        amplitude (float): amplitude of the sinusoid, must be greater than zero.
        frequency (float): frequency of the sinusoid, must be greater than zero.
        phase (float): phase of the sinusoid, will be rounded modulo 2*PI.
        offset (float): vertical offset of the sinusoid, will be used to translated y-axis values.
        samples_count (int): number of samples that will be created for the sinusoid.
        sampling_rate (float): sampling rate of the sinusoid.

    Raises:
        PCBATTAnalysisException: occurs when waveform creation fails for some reason.
        ValueError: occurs when amplitude is less or equal zero,
            occurs when frequency is less or equal zero,
            occurs when samples_count is less or equal zero,
            occurs when sampling_rate is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: samples constituting created sine waveform.
    

### `def create_sine_waveform(amplitude: float, frequency: float, phase: float, offset: float, samples_count: int, sampling_rate: float) -> numpy.ndarray[numpy.float64]`

Creates samples of a sine waveform described through its characteristics, using math.sin.

    Args:
        amplitude (float): amplitude of the sinusoid, must be greater than zero.
        frequency (float): frequency of the sinusoid, must be greater than zero.
        phase (float): phase of the sinusoid, will be rounded modulo 2*PI.
        offset (float): vertical offset of the sinusoid, will be used to translated y-axis values.
        samples_count (int): number of samples that will be created for the sinusoid.
        sampling_rate (float): sampling rate of the sinusoid.

    Raises:
        PCBATTAnalysisException: occurs when waveform creation fails for some reason.
        ValueError: occurs when amplitude is less or equal zero,
            occurs when frequency is less or equal zero,
            occurs when samples_count is less or equal zero,
            and occurs when sampling_rate is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: samples constituting created sine waveform.
    

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_creation/square_waveform.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/waveform_creation/square_waveform.py

### MODULE DOCSTRING

Provides square waveform creation API.

### `def create_square_waveform(amplitude: float, frequency: float, duty_cycle: float, phase: float, offset: float, samples_count: int, sampling_rate: float) -> numpy.ndarray[numpy.float64]`

Creates samples of a square waveform described through its characteristics.

    Args:
        amplitude (float): amplitude of the square wave, must be greater than zero.
        frequency (float): frequency of the square wave, must be greater than zero.
        duty_cycle (float): duty cycle of the square wave, must be in [0,1].
        phase (float): phase of the square wave, will be rounded modulo 2*PI.
        offset (float): vertical offset of the square wave,
        will be used to translated y-axis values.
        samples_count (int): number of samples that will be created for the square wave.
        sampling_rate (float): sampling rate of the square wave.

    Raises:
        PCBATTAnalysisException: occurs when waveform creation fails for some reason.
        ValueError: occurs when amplitude is less or equal zero,
            occurs when `frequency` is less or equal zero,
            occurs when `samples_count` is less or equal zero,
            and occurs when `sampling_rate` is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: samples constituting created square waveform.
    

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_transformation/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/waveform_transformation/__init__.py

### MODULE DOCSTRING

Provides a set of waveform transformation modules using python written functions

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_transformation/_waveform_transformation_internal/_scale_and_offset_waveform.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/waveform_transformation/_waveform_transformation_internal/_scale_and_offset_waveform.py

### MODULE DOCSTRING

Private module that provides a set of helper functions
   for `scale_and_offset_waveform` module.

### `def scale_and_apply_offset_impl(waveform_samples: numpy.ndarray[numpy.float64], scale_factor: float, offset: float) -> numpy.ndarray[numpy.float64]`

Implementation of scale and offset waveform.

### `def scale_and_apply_offset_inplace_impl(waveform_samples: numpy.ndarray[numpy.float64], scale_factor: float, offset: float) -> numpy.ndarray[numpy.float64]`

Implementation of scale and offset waveform in place.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_analysis/waveform_transformation/scale_and_offset_waveform.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_analysis/waveform_transformation/scale_and_offset_waveform.py

### MODULE DOCSTRING

Provides scale and offset waveform transformation API.

### `def scale(waveform_samples: numpy.ndarray[numpy.float64], scale_factor: float) -> numpy.ndarray[numpy.float64]`

Applies a scale factor to given waveform samples, and returns new samples.

    Raises:
        PCBATTAnalysisException: occurs when waveform transformation fails for some reason.
        ValueError: occurs when `scale_factor` is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: new samples constituting transformed waveform.
    

### `def apply_offset(waveform_samples: numpy.ndarray[numpy.float64], offset: float) -> numpy.ndarray[numpy.float64]`

Applies a vertical offset to given waveform samples, and returns new samples.

    Raises:
        PCBATTAnalysisException: occurs when waveform transformation fails for some reason.

    Returns:
        numpy.ndarray[numpy.float64]: new samples constituting transformed waveform.
    

### `def scale_inplace(waveform_samples: numpy.ndarray[numpy.float64], scale_factor: float) -> numpy.ndarray[numpy.float64]`

Applies a scale factor to given waveform samples, and returns modified samples.

    Raises:
        PCBATTAnalysisException: occurs when waveform transformation fails for some reason.
        ValueError: occurs when `scale_factor` is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: modified input samples constituting transformed waveform.
    

### `def apply_offset_inplace(waveform_samples: numpy.ndarray[numpy.float64], offset: float) -> numpy.ndarray[numpy.float64]`

Applies a vertical offset to given waveform samples, and returns modified samples.

    Raises:
        PCBATTAnalysisException: occurs when waveform transformation fails for some reason.
        ValueError: occurs when `scale_factor` is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: modified input samples constituting transformed waveform.
    

### `def scale_and_apply_offset(waveform_samples: numpy.ndarray[numpy.float64], scale_factor: float, offset: float) -> numpy.ndarray[numpy.float64]`

Applies a scale factor and vertical offset to given waveform samples,
    and returns new samples.

    Raises:
        PCBATTAnalysisException: occurs when waveform transformation fails for some reason.
        ValueError: occurs when `scale_factor` is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: new samples constituting transformed waveform.
    

### `def scale_and_apply_offset_inplace(waveform_samples: numpy.ndarray[numpy.float64], scale_factor: float, offset: float) -> numpy.ndarray[numpy.float64]`

Applies a scale factor and vertical offset to given waveform samples,
    and returns modified samples.

    Raises:
        PCBATTAnalysisException: occurs when waveform transformation fails for some reason.
        ValueError: occurs when `scale_factor` is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: modified input samples constituting transformed waveform.
    

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/__init__.py

### MODULE DOCSTRING

Contains all automation tests using nipcbatt.library.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/action_button_tests/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/action_button_tests/__init__.py

### MODULE DOCSTRING

Includes files for running aciton button test sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/action_button_tests/action_button_main_sequence.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/action_button_tests/action_button_main_sequence.py

### MODULE DOCSTRING

Main Sequence for executing Action Button Test

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/action_button_tests/action_button_test.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/action_button_tests/action_button_test.py

### MODULE DOCSTRING

Example demonstrates DC-RMS Voltage Measurements by performing button actions 
   (generating DC Voltages) on specific test points

- `BUTTON_CHANNEL = 'TS_ButtonEnable0'`

- `DC_RMS_VOLTAGE_TEST_POINT_CHANNEL = 'TP_LineOut0:1'`

- `DEFAULT_FILEPATH = 'C:\\Windows\\Temp\\action_button_test_results.txt'`

### `def setup(button_channel=BUTTON_CHANNEL, voltage_channel=DC_RMS_VOLTAGE_TEST_POINT_CHANNEL)`

Creates the necessary objects for the simulation and measurement of the action button

### `def main(button_instance: daq.DcVoltageGeneration, dc_rms_voltage_test_point: daq.DcRmsVoltageMeasurement, write_to_file=True, filepath=DEFAULT_FILEPATH)`

If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path is C:\Windows\Temp\action_button_test_results.txt
    

### `def cleanup(button_instance, dc_rms_voltage_test_point)`

Closes out the created objects used in the generation and measurement

### `def action_button_test(button_channel=BUTTON_CHANNEL, voltage_channel=DC_RMS_VOLTAGE_TEST_POINT_CHANNEL, write_to_file=True, filepath=DEFAULT_FILEPATH)`

Execute all steps in the sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/action_button_tests/turn_off_all_ao_channels.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/action_button_tests/turn_off_all_ao_channels.py

### MODULE DOCSTRING

This example resets all configured Analog output channels to 0 volts

- `ANALOG_OUT_CHANNELS = 'Sim_PC_basedDAQ/ao0:3'`

- `RANGE_PARAMETERS = daq.DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS`

### `def power_down_all_ao_channels(channel_names=ANALOG_OUT_CHANNELS, parameters=RANGE_PARAMETERS)`

Turn off configured AO channels by configuring to 0V

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/audio_tests/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/audio_tests/__init__.py

### MODULE DOCSTRING

Contains files for audio test sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/audio_tests/audio_filter_check.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/audio_tests/audio_filter_check.py

### MODULE DOCSTRING

Example demonstrates Frequency domain measurements(extraction of tones) of captured 
   Analog(Audio) signal generated by Analog Output(generates multi tones) module 
   with Hardware Trigger

- `GEN_CHANNEL = 'TS_AudioLineIn0'`

- `MEAS_CHANNEL = 'TP_AudioLineOut0'`

- `DEFAULT_FILEPATH = 'C:\\Windows\\Temp\\audio_filter_check_test_results.txt'`

### `def setup()`

Creates the necessary objects for signal generation and measurement

### `def main(generation_instance: daq.SignalVoltageGeneration, measurement_instance: daq.FrequencyDomainMeasurement, write_to_file=True, filepath=DEFAULT_FILEPATH)`

If you wish to write your results to a file use the following commands
    Make sure the write_to_file option is set to True when calling audio_test()
    Change the file path to desired location on your drive
    The default file path is C:\Windows\Temp\audio_filter_check_test_results.txt

### `def cleanup(generation_instance, measurement_instance)`

Closes out the created objects used in the generation and measurement

### `def audio_filter_check(write_to_file=True, filepath=DEFAULT_FILEPATH)`

Execute all steps in the sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/audio_tests/audio_line_check.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/audio_tests/audio_line_check.py

### MODULE DOCSTRING

Example demonstrates Frequency domain measurements(extraction of tones) of captured
   Analog(Audio) signal generated by Analog Output(generates sine wave tones) module 
   with Hardware Trigger

- `GEN_CHANNEL = 'TS_AudioLineIn0'`

- `MEAS_CHANNEL = 'TP_AudioLineOut0'`

- `DEFAULT_FILEPATH = 'C:\\Windows\\Temp\\audio_line_check_test_results.txt'`

### `def setup()`

Creates the necessary objects for signal generation and measurement

### `def main(generation_instance: daq.SignalVoltageGeneration, measurement_instance: daq.FrequencyDomainMeasurement, write_to_file=True, filepath=DEFAULT_FILEPATH)`

If you wish to write your results to a file use the following commands
    Make sure the write_to_file option is set to True when calling audio_test()
    Change the file path to desired location on your drive
    The default file path is C:\Windows\Temp\audio_line_check_test_results.txt

### `def cleanup(generation_instance, measurement_instance)`

Closes out the created objects used in the generation and measurement

### `def audio_line_check(write_to_file=True, filepath=DEFAULT_FILEPATH)`

Execute all steps in the sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/audio_tests/audio_test_main_sequence.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/audio_tests/audio_test_main_sequence.py

### MODULE DOCSTRING

Main sequence for executing audio test sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/audio_tests/turn_off_all_ao_channels.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/audio_tests/turn_off_all_ao_channels.py

### MODULE DOCSTRING

This example resets all configured Analog output channels to 0 volts

- `ANALOG_OUT_CHANNELS = 'Sim_PC_basedDAQ/ao0:3'`

- `RANGE_PARAMETERS = daq.DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS`

### `def power_down_all_ao_channels(channel_names=ANALOG_OUT_CHANNELS, parameters=RANGE_PARAMETERS)`

Turn off configured AO channels by configuring to 0V

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/communication_tests/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/communication_tests/__init__.py

### MODULE DOCSTRING

Contains all files necessary to run communication sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/communication_tests/communication_test_main_sequence.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/communication_tests/communication_test_main_sequence.py

### MODULE DOCSTRING

Main sequence for executing communication test sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/communication_tests/i2c_comm_test.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/communication_tests/i2c_comm_test.py

### MODULE DOCSTRING

Example demonstrates simple read and write data operations through I2C protocol
communication using NI 845x Device

- `DEVICE_ID = 'DeviceA'`

- `SESSION_NUMBER = 0`

- `DEFAULT_FILEPATH = 'C:\\Windows\\Temp\\i2c_comm_test_results.txt'`

### `def setup()`

Creates and initializes I2C communication objects

### `def main(reader: communications.I2cReadCommunication, writer: communications.I2cWriteCommunication, write_to_file: bool)`

If you wish to write your results to a file use the following commands
    Make sure the write_to_file option is set to True when calling i2c_comm_test()
    Change the file path to desired location on your drive
    The default file path is C:\Windows\Temp\i2c_comm_test_results.txt

### `def cleanup(reader: communications.I2cReadCommunication, writer: communications.I2cWriteCommunication)`

Closes out the created objects used in the communication

### `def i2c_comm_test()`

Execute all steps in the sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/communication_tests/serial_comm_test.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/communication_tests/serial_comm_test.py

### MODULE DOCSTRING

Example demonstrates simple read and write data operations through Serial COM port

- `DEVICE_ID = 'DeviceB'`

- `SESSION_NUMBER = 0`

- `DEFAULT_FILEPATH = 'C:\\Windows\\Temp\\serial_comm_test_results.txt'`

### `def setup()`

Creates and initializes serial communication object

### `def main(resource: communications.SerialCommunication, write_to_file: bool)`

If you wish to write your results to a file use the following commands
    Make sure the write_to_file option is set to True when calling i2c_comm_test()
    Change the file path to desired location on your drive
    The default file path is C:\Windows\Temp\serial_comm_test_results.txt

### `def cleanup(resource: communications.SerialCommunication)`

Closes out the created objects used in the communication

### `def serial_comm_test()`

Execute all steps in the sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/communication_tests/spi_comm_test.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/communication_tests/spi_comm_test.py

### MODULE DOCSTRING

Example demonstrates simple read and write data operations through SPI 
   protocol communication using NI 845x Device 

- `DEVICE_ID = 'DeviceA'`

- `SESSION_NUMBER = 0`

- `DEFAULT_FILEPATH = 'C:\\Windows\\Temp\\spi_comm_test_results.txt'`

### `def setup()`

Creates and initializes SPI communication objects

### `def main(reader: communications.SpiReadCommunication, writer: communications.SpiWriteCommunication, write_to_file: bool)`

If you wish to write your results to a file use the following commands
    Make sure the write_to_file option is set to True when calling spi_comm_test()
    Change the file path to desired location on your drive
    The default file path is C:\Windows\Temp\spi_comm_test_results.txt

### `def cleanup(reader: communications.SpiReadCommunication, writer: communications.SpiWriteCommunication)`

Closes out the created objects used in the communication

### `def spi_comm_test()`

Execute all steps in the sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/digital_io_tests/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/digital_io_tests/__init__.py

### MODULE DOCSTRING

Contains files for digital test automation

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/digital_io_tests/digital_clock_test.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/digital_io_tests/digital_clock_test.py

### MODULE DOCSTRING

Demonstrates digital clock generation and frequency measurement through 
   counter-based measurements using Digital IO lines or Modules.

- `OUTPUT_TERMINAL = '/Sim_PC_basedDAQ/PFI7'`

- `GEN_PHYSICAL_CHANNEL_COUNTER = 'Sim_PC_basedDAQ/ctr3'`

- `INPUT_TERMINAL = '/Simulated_Core/PFI3'`

- `MEAS_PHYSICAL_CHANNEL_COUNTER = 'Simulated_Core/ctr1'`

- `DEFAULT_FILEPATH = 'C:\\Windows\\Temp\\digital_clock_test_results.txt'`

### `def setup(output_terminal=OUTPUT_TERMINAL, gen_counter_channel=GEN_PHYSICAL_CHANNEL_COUNTER, input_terminal=INPUT_TERMINAL, meas_counter_channel=MEAS_PHYSICAL_CHANNEL_COUNTER)`

Creates the necessary objects for the generation and measurement of digital clock

### `def main(generation_instance: daq.DigitalClockGeneration, measurement_instance: daq.DigitalFrequencyMeasurement, write_to_file: True, filepath=DEFAULT_FILEPATH)`

If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path is C:\Windows\Temp\digital_clock_test_results.txt

### `def cleanup(generation_instance: daq.DigitalClockGeneration, measurement_instance: daq.DigitalFrequencyMeasurement)`

Closes out the created objects used in the generation and measurement

### `def digital_clock_test(generation_output_channel=OUTPUT_TERMINAL, generation_counter_channel=GEN_PHYSICAL_CHANNEL_COUNTER, measurement_input_channel=INPUT_TERMINAL, measurement_counter_channel=MEAS_PHYSICAL_CHANNEL_COUNTER, write_to_file=True, filepath=DEFAULT_FILEPATH)`

Execute all steps in the sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/digital_io_tests/digital_count_events_hw_timed.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/digital_io_tests/digital_count_events_hw_timed.py

### MODULE DOCSTRING

This example demonstrates digital pattern generation and digital edge count measurement through
   counter-based measurements using Digital IO Lines or Modules. Digital edge counting is 
   performed at Hardware timed using with Trigger to create a measurement window for 
   fixed duration

- `GENERATION_CHANNEL = 'TS_DIn1'`

- `SESSION_NUMBER = 0`

- `INPUT_TERMINAL = '/Sim_PC_basedDAQ/PFI0'`

- `EDGE_COUNTER = 'Sim_PC_basedDAQ/ctr0'`

- `COUNTER_TIMER = 'Sim_PC_basedDAQ/ctr1'`

- `DEFAULT_FILEPATH = 'C:\\Windows\\Temp\\digital_edge_count_hw_timed_test_results.txt'`

### `def setup()`

Creates the necessary objects for the generation and measurement of digital edge count

### `def main(generation_instance: daq.DynamicDigitalPatternGeneration, measurement_instance: daq.DigitalEdgeCountMeasurementUsingHardwareTimer, write_to_file=True, filepath=DEFAULT_FILEPATH)`

If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path is C:\Windows\Temp\digital_edge_count_hw_timed_test_results.txt

### `def cleanup(generation_instance: daq.DynamicDigitalPatternGeneration, measurement_instance: daq.DigitalEdgeCountMeasurementUsingHardwareTimer)`

Closes out the created objects used in the generation and measurement

### `def digital_count_events_sw_timed_test(write_to_file=True, filepath=DEFAULT_FILEPATH)`

Execute all steps in the sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/digital_io_tests/digital_count_events_sw_timed.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/digital_io_tests/digital_count_events_sw_timed.py

### MODULE DOCSTRING

This example demonstrates digital pulse generation and digital edge count measurement through 
   counter-based measurements using Core Digital IO Modules. Digital edge counting is performed 
   at Software timed using an external wait

- `OUTPUT_TERMINAL = '/Sim_PC_basedDAQ/PFI7'`

- `GEN_PHYSICAL_CHANNEL_COUNTER = 'Sim_PC_basedDAQ/ctr3'`

- `INPUT_TERMINAL = '/Simulated_Core/PFI3'`

- `EDGE_COUNTER = 'Simulated_Core/ctr1'`

- `DEFAULT_FILEPATH = 'C:\\Windows\\Temp\\digital_edge_count_sw_timed_test_results.txt'`

### `def setup(output_terminal=OUTPUT_TERMINAL, gen_counter_channel=GEN_PHYSICAL_CHANNEL_COUNTER, input_terminal=INPUT_TERMINAL, edge_count_channel=EDGE_COUNTER)`

Creates the necessary objects for the generation and measurement of digital edge count

### `def main(generation_instance: daq.DigitalPulseGeneration, measurement_instance: daq.DigitalEdgeCountMeasurementUsingSoftwareTimer, write_to_file=True, filepath=DEFAULT_FILEPATH)`

If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path is C:\Windows\Temp\digital_edge_count_sw_timed_test_results.txt

### `def cleanup(generation_instance: daq.DigitalPulseGeneration, measurement_instance: daq.DigitalEdgeCountMeasurementUsingSoftwareTimer)`

Closes out the created objects used in the generation and measurement

### `def digital_count_events_sw_timed_test(generation_output_channel=OUTPUT_TERMINAL, generation_counter_channel=GEN_PHYSICAL_CHANNEL_COUNTER, measurement_input_channel=INPUT_TERMINAL, edge_counter=EDGE_COUNTER, write_to_file=True, filepath=DEFAULT_FILEPATH)`

Execute all steps in the sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/digital_io_tests/digital_io_main_sequence.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/digital_io_tests/digital_io_main_sequence.py

### MODULE DOCSTRING

Main sequence for executing Digital IO Test

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/digital_io_tests/digital_pattern_test.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/digital_io_tests/digital_pattern_test.py

### MODULE DOCSTRING

This example demonstrates the digital pattern generation and capture using digital input and 
   output modules with trigger for synchronization

- `GENERATION_CHANNEL = 'TS_DIn0:1'`

- `MEASUREMENT_CHANNEL = 'TP_DOut2:3'`

- `DEFAULT_FILEPATH = 'C:\\Windows\\Temp\\digital_pattern_test_results.txt'`

### `def setup(generation_channel=GENERATION_CHANNEL, measurement_channel=MEASUREMENT_CHANNEL)`

Creates the necessary objects for the generation and measurement of digital patterns

### `def main(generation_instance: daq.DynamicDigitalPatternGeneration, measurement_instance: daq.DynamicDigitalPatternMeasurement, write_to_file=True, filepath=DEFAULT_FILEPATH)`

If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path is C:\Windows\Temp\digital_pattern_test_results.txt

### `def cleanup(generation_instance: daq.DynamicDigitalPatternGeneration, measurement_instance: daq.DynamicDigitalPatternMeasurement)`

Closes out the created objects used in the generation and measurement

### `def digital_pattern_test(generation_channel=GENERATION_CHANNEL, measurement_channel=MEASUREMENT_CHANNEL, write_to_file=True, filepath=DEFAULT_FILEPATH)`

Execute all steps in the sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/digital_io_tests/digital_pwm_test.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/digital_io_tests/digital_pwm_test.py

### MODULE DOCSTRING

This example demonstrates digital pulse generation and digital edge count measurement through 
   counter-based measurements using Core Digital IO Modules. Digital edge counting is performed 
   at Software timed using an external wait

- `OUTPUT_TERMINAL = '/Sim_PC_basedDAQ/PFI7'`

- `GEN_PHYSICAL_CHANNEL_COUNTER = 'Sim_PC_basedDAQ/ctr3'`

- `INPUT_TERMINAL = '/Simulated_Core/PFI3'`

- `MEAS_PHYSICAL_CHANNEL_COUNTER = 'Simulated_Core/ctr1'`

- `COUNTER_TIMER = ''`

- `DEFAULT_FILEPATH = 'C:\\Windows\\Temp\\digital_pwm_test_results.txt'`

### `def setup(output_terminal=OUTPUT_TERMINAL, gen_counter_channel=GEN_PHYSICAL_CHANNEL_COUNTER, input_terminal=INPUT_TERMINAL, meas_counter_channel=MEAS_PHYSICAL_CHANNEL_COUNTER)`

Creates the necessary objects for the generation and measurement of PWM

### `def main(generation_instance: daq.DigitalPulseGeneration, measurement_instance: daq.DigitalPwmMeasurement, write_to_file: True, filepath=DEFAULT_FILEPATH)`

If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path is C:\Windows\Temp\digital_pwm_test_results.txt
    

### `def cleanup(generation_instance: daq.DigitalPulseGeneration, measurement_instance: daq.DigitalPwmMeasurement)`

Closes out the created objects used in the generation and measurement

### `def digital_pwm_test(generation_output_channel=OUTPUT_TERMINAL, generation_counter_channel=GEN_PHYSICAL_CHANNEL_COUNTER, measurement_input_channel=INPUT_TERMINAL, measurement_counter_channel=MEAS_PHYSICAL_CHANNEL_COUNTER, write_to_file=True, filepath=DEFAULT_FILEPATH)`

Execute all steps in the sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/digital_io_tests/digital_state_test.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/digital_io_tests/digital_state_test.py

### MODULE DOCSTRING

This example demonstrates how to set Digital High & Low states using digital output modules and 
   measure the digital states of test points using digital input modules

- `GENERATION_CHANNEL = 'TS_DIn0:1'`

- `MEASUREMENT_CHANNEL = 'TP_DOut2:3'`

- `DEFAULT_FILEPATH = 'C:\\Windows\\Temp\\digital_state_test_results.txt'`

### `def setup(generation_channel=GENERATION_CHANNEL, measurement_channel=MEASUREMENT_CHANNEL)`

Creates the necessary objects for the generation and measurement of digital states

### `def main(generation_instance: daq.StaticDigitalStateGeneration, measurement_instance: daq.StaticDigitalStateMeasurement, write_to_file=True, filepath=DEFAULT_FILEPATH)`

If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path is C:\Windows\Temp\digital_state_test_results.txt
    

### `def cleanup(generation_instance: daq.StaticDigitalStateGeneration, measurement_instance: daq.StaticDigitalStateMeasurement)`

Closes out the created objects used in the generation and measurement

### `def digital_state_test(generation_channel=GENERATION_CHANNEL, measurement_channel=MEASUREMENT_CHANNEL, write_to_file=True, filepath=DEFAULT_FILEPATH)`

Execute all steps in the sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/digital_io_tests/turn_off_all_do_channels.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/digital_io_tests/turn_off_all_do_channels.py

### MODULE DOCSTRING

This example resets all configured Digital output channels voltage to 0 Volts

- `DIGITAL_OUT_CHANNELS = 'Sim_PC_basedDAQ/port0/line0:7'`

### `def power_down_all_do_channels()`

Set digital state to LOW on all digital output channels

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/LED_Tests/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/LED_Tests/__init__.py

### MODULE DOCSTRING

Includes files for running LED Test sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/LED_Tests/analog_pwm_test.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/LED_Tests/analog_pwm_test.py

### MODULE DOCSTRING

Demonstrates Analog PWM Signal Generation and Time Domain Measurement using 
   AO and AI channels or Modules

- `OUTPUT_TERMINAL = 'TS_PWM_LED0'`

- `INPUT_TERMINAL = 'TP_PWM_LED0'`

- `DIGITAL_TRIGGER_SOURCE = '/Sim_PC_basedDAQ/ao/StartTrigger'`

- `DEFAULT_FILEPATH = 'C:\\Windows\\Temp\\Analog_PWM_Test.txt'`

### `def setup(output_terminal=OUTPUT_TERMINAL, input_terminal=INPUT_TERMINAL, file_path=DEFAULT_FILEPATH)`

Creates necessary objects for the generation of Analog PWM siganl and
    Time Domain Measurement

### `def main(svg: daq.SignalVoltageGeneration, tdvm: daq.TimeDomainMeasurement, digital_trigger_source=DIGITAL_TRIGGER_SOURCE)`

### `def cleanup(svg: daq.SignalVoltageGeneration, tdvm: daq.TimeDomainMeasurement)`

### `def analog_pwm_test(generation_output_channel=OUTPUT_TERMINAL, measurement_input_channel=INPUT_TERMINAL, trigger_source=DIGITAL_TRIGGER_SOURCE)`

Executes all steps in the sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/LED_Tests/analog_voltage_measurement_test.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/LED_Tests/analog_voltage_measurement_test.py

### MODULE DOCSTRING

Demonstrates DC RMS Voltage Measurement using AI lines

- `INPUT_TERMINAL = 'Sim_PC_basedDAQ/ai1'`

- `DEFAULT_FILEPATH = 'C:\\Windows\\Temp\\DRVM_test.txt'`

### `def setup(input_terminal=INPUT_TERMINAL, file_path=DEFAULT_FILEPATH)`

Creates the necessary objects for measurement of Voltage

### `def main(drvm: daq.DcRmsVoltageMeasurement)`

### `def cleanup(drvm: daq.DcRmsVoltageMeasurement)`

### `def analog_voltage_measurement(generation_input_channel=INPUT_TERMINAL)`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/LED_Tests/led_test_main_sequence.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/LED_Tests/led_test_main_sequence.py

### MODULE DOCSTRING

Main sequence for Analog PWM test

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/LED_Tests/turn_off_all_ao_channels.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/LED_Tests/turn_off_all_ao_channels.py

### MODULE DOCSTRING

This example resets all configured Analog output channels to 0 volts

- `ANALOG_OUT_CHANNELS = 'Sim_PC_basedDAQ/ao0'`

- `RANGE_PARAMETERS = daq.DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS`

### `def power_down_all_ao_channels(channel_names=ANALOG_OUT_CHANNELS, parameters=RANGE_PARAMETERS)`

Turn off configured AO channels by configuring to 0V

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/microphone_tests/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/microphone_tests/__init__.py

### MODULE DOCSTRING

Includes files for running Microphone Test sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/microphone_tests/microphone_main_sequence.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/microphone_tests/microphone_main_sequence.py

### MODULE DOCSTRING

Main Sequence for executing Microphone Test

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/microphone_tests/microphone_test.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/microphone_tests/microphone_test.py

### MODULE DOCSTRING

This example demonstrates Sine Wave Generation and Frequency Domain 
   Measurement using AO and AI channels or Modules

- `SIGNAL_VOLTAGE_GEN_CHANNEL = 'TS_Speaker0'`

- `FREQ_DOMAIN_MEAS_CHANNEL = 'TP_MIC0:2'`

- `DIGITAL_STATRT_TRIGGER = '/Sim_PC_basedDAQ/ao/StartTrigger'`

- `DEFAULT_FILEPATH = 'C:\\Windows\\Temp\\Signal_Generation_and_Frequency_Domain_Analysis.txt'`

### `def setup(svg_channel=SIGNAL_VOLTAGE_GEN_CHANNEL, fdvm_channel=FREQ_DOMAIN_MEAS_CHANNEL, file_path=DEFAULT_FILEPATH)`

Creates the necessary objects for generation of sine wave and Frequency
    Domain Measurement

### `def main(microphone_instance: daq.SignalVoltageGeneration, freq_domain_meas_test_point: daq.FrequencyDomainMeasurement, digital_start_trigger=DIGITAL_STATRT_TRIGGER)`

### `def cleanup(microphone_instance: daq.SignalVoltageGeneration, freq_domain_meas_test_point: daq.TimeDomainMeasurement)`

### `def signal_voltage_generation_and_measurement(generation_channel=SIGNAL_VOLTAGE_GEN_CHANNEL, measurement_channel=FREQ_DOMAIN_MEAS_CHANNEL)`

Execute all steps in the sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/microphone_tests/turn_off_all_ao_channels.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/microphone_tests/turn_off_all_ao_channels.py

### MODULE DOCSTRING

This example resets all configured Analog output channels to 0 volts

- `ANALOG_OUT_CHANNELS = 'Sim_PC_basedDAQ/ao0'`

- `RANGE_PARAMETERS = daq.DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS`

### `def power_down_all_ao_channels(channel_names=ANALOG_OUT_CHANNELS, parameters=RANGE_PARAMETERS)`

Turn off configured AO channels by configuring to 0V

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/power_supply_tests/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/power_supply_tests/__init__.py

### MODULE DOCSTRING

Includes files for running power supply test sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/power_supply_tests/power_down_all_power_channels.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/power_supply_tests/power_down_all_power_channels.py

### MODULE DOCSTRING

This example resets and closes configured Power channels

- `POWER_CHANNEL = 'Simulated_power/power'`

- `CONFIGURATION = daq.DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_CONFIGURATION`

### `def power_down_all_power_channels(channel_name=POWER_CHANNEL, config: daq.PowerSupplySourceAndMeasureConfiguration=CONFIGURATION)`

Configure power channel with default parameters and close

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/power_supply_tests/power_supply_main_sequence.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/power_supply_tests/power_supply_main_sequence.py

### MODULE DOCSTRING

Main Sequence for executing Power Supply Tests

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/power_supply_tests/power_supply_test_with_trigger.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/power_supply_tests/power_supply_test_with_trigger.py

### MODULE DOCSTRING

This example demostrates Power Supply Source(VDD) and Time Domain Analysis of 
Measured Analog input voltage in TestPoints. Data capture in Analog Input(TP) starts when 
the Trigger is sent from Power Supply after starting the source.

- `POWER_CHANNEL = 'Simulated_power/power'`

- `ANALOG_INPUT_CHANNEL = 'TP_Power0:2'`

- `DEFAULT_FILEPATH = 'C:\\Windows\\Temp\\power_supply_test_with_trigger_results.txt'`

### `def setup(power_channel=POWER_CHANNEL, measurement_channel=ANALOG_INPUT_CHANNEL)`

Creates the necessary objects for the generation and measurement of the power supply

### `def main(power_supply_test_source_instance: daq.PowerSupplySourceAndMeasure, analog_input_test_point_instance: daq.TimeDomainMeasurement, write_to_file=True, filepath=DEFAULT_FILEPATH)`

Note to run with Hardware: Review the configurations and update the trigger configurations

### `def cleanup(power_supply_test_source_instance: daq.PowerSupplySourceAndMeasure, analog_input_test_point_instance: daq.TimeDomainMeasurement)`

Closes out the created objects used in the generation and measurement

### `def power_supply_test_with_trigger(power_channel=POWER_CHANNEL, measurement_channel=ANALOG_INPUT_CHANNEL, write_to_file=True, filepath=DEFAULT_FILEPATH)`

Execute all steps in the sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/power_supply_tests/power_supply_test_without_trigger.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/power_supply_tests/power_supply_test_without_trigger.py

### MODULE DOCSTRING

This example demonstrates Power Supply source and Voltage Measurement without trigger

- `POWER_CHANNEL = 'Simulated_power/power'`

- `ANALOG_INPUT_CHANNEL = 'TP_Power0:2'`

- `DEFAULT_FILEPATH = 'C:\\Windows\\Temp\\power_supply_test_without_trigger_results.txt'`

### `def setup(power_channel=POWER_CHANNEL, voltage_channel=ANALOG_INPUT_CHANNEL)`

Creates the necessary objects for the generation and measurement of the power supply

### `def main(power_supply_test_source_instance: daq.PowerSupplySourceAndMeasure, analog_input_test_point_instance: daq.DcRmsVoltageMeasurement, write_to_file=True, filepath=DEFAULT_FILEPATH)`

Note to run with Hardware: Review the configurations and update the trigger configurations

### `def cleanup(power_supply_test_source_instance: daq.PowerSupplySourceAndMeasure, analog_input_test_point_instance: daq.DcRmsVoltageMeasurement)`

Closes out the created objects used in the generation and measurement

### `def power_supply_test_without_trigger(power_channel=POWER_CHANNEL, voltage_channel=ANALOG_INPUT_CHANNEL, write_to_file=True, filepath=DEFAULT_FILEPATH)`

Execute all steps in the sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/sensor_tests/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/sensor_tests/__init__.py

### MODULE DOCSTRING

Includes files for running Sensor Test sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/sensor_tests/rtd_test.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/sensor_tests/rtd_test.py

### MODULE DOCSTRING

Demonstrates temprature measurement using RTD using AI lines or Modules

- `INPUT_TERMINAL = 'TP_RTD'`

- `DEFAULT_FILEPATH = 'C:\\Windows\\Temp\\RTD_test.txt'`

### `def setup(input_terminal=INPUT_TERMINAL, file_path=DEFAULT_FILEPATH)`

Creates the necessary objects for the measurement of Temprature

### `def main(trtdm: daq.TemperatureMeasurementUsingRtd, input_terminal=INPUT_TERMINAL)`

### `def cleanup(trtdm: daq.TemperatureMeasurementUsingRtd)`

### `def rtd_test(measurement_input_channel=INPUT_TERMINAL)`

Execute all steps in the sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/sensor_tests/sensor_tests_main_sequence.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/sensor_tests/sensor_tests_main_sequence.py

### MODULE DOCSTRING

Main sequence forr executing the Sensor Test

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/sensor_tests/thermistor_test_cdaq.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/sensor_tests/thermistor_test_cdaq.py

### MODULE DOCSTRING

Demonstrates DC Voltage Generation using AO lines or Modules and Temprature
   measurement with Thermistor using AI lines or Modules of cDAQ

- `OUTPUT_TERMINAL = 'TS_THEX'`

- `INPUT_TERMINAL = 'TP_TH0'`

- `DEFAULT_FILEPATH = 'C:\\Windows\\Temp\\Thermistor_test_cDAQ.txt'`

### `def setup(output_terminal=OUTPUT_TERMINAL, input_terminal=INPUT_TERMINAL, file_path=DEFAULT_FILEPATH)`

Creates the necessary objects for DC voltage generation
    and the Temprature Measurement

### `def main(drvg: daq.DcVoltageGeneration, ttr: daq.TemperatureMeasurementUsingThermistor, input_terminal=INPUT_TERMINAL)`

### `def cleanup(drvg: daq.DcVoltageGeneration, ttr: daq.TemperatureMeasurementUsingThermistor)`

### `def thermistor_test_cdaq(generation_output_channel=OUTPUT_TERMINAL, measurement_input_channel=INPUT_TERMINAL)`

Execute all the steps in sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/sensor_tests/thermistor_test_testscale.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/sensor_tests/thermistor_test_testscale.py

### MODULE DOCSTRING

Demonstrates Voltage Generation using Power Module and Temprature 
   measurement with Thermistor using AI lines or Modules of Testscale

- `OUTPUT_TERMINAL = 'Simulated_Power/power'`

- `INPUT_TERMINAL = 'TP_TH2'`

- `DEFAULT_FILEPATH = 'C:\\Windows\\Temp\\Thermistor_test_TestScale.txt'`

### `def setup(output_terminal=OUTPUT_TERMINAL, input_terminal=INPUT_TERMINAL, file_path=DEFAULT_FILEPATH)`

Creates the necessary objects for voltage generation
    and the Temprature Measurement

### `def main(pssm: daq.PowerSupplySourceAndMeasure, ttr: daq.TemperatureMeasurementUsingThermistor, input_terminal=INPUT_TERMINAL)`

### `def cleanup(ttr: daq.TemperatureMeasurementUsingThermistor, pssm: daq.PowerSupplySourceAndMeasure)`

### `def thermistor_test_testscale(generation_output_channel=OUTPUT_TERMINAL, measurement_input_channel=INPUT_TERMINAL)`

Execute all the steps in sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/sensor_tests/thermocouple_test.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/sensor_tests/thermocouple_test.py

### MODULE DOCSTRING

Demonstrates temprature measurement using Thermocouple using AI lines or Modules

- `INPUT_TERMINAL = 'TP_TC'`

- `COLD_JUNCTION_CHANNEL = 'Simulated_cDAQ_9217/ai0'`

- `DEFAULT_FILEPATH = 'C:\\Windows\\Temp\\Thermocouple_test.txt'`

### `def setup(input_terminal=INPUT_TERMINAL, cold_junction_terminal=COLD_JUNCTION_CHANNEL, file_path=DEFAULT_FILEPATH)`

Creates the necessary objects for the measurement of Temprature

### `def main(ttcm: daq.TemperatureMeasurementUsingThermocouple, input_terminal=INPUT_TERMINAL, cold_junction_terminal=COLD_JUNCTION_CHANNEL)`

### `def cleanup(ttcm: daq.TemperatureMeasurementUsingThermocouple)`

### `def thermocouple_test(generation_input_channel=INPUT_TERMINAL, cold_input_channel=COLD_JUNCTION_CHANNEL)`

Execute all steps in the sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/sensor_tests/turn_off_all_ao_channels.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/sensor_tests/turn_off_all_ao_channels.py

### MODULE DOCSTRING

This example resets all configured Analog output channels to 0 volts

- `ANALOG_OUT_CHANNELS = 'Simulated_cDAQ_9263/ao0'`

- `RANGE_PARAMETERS = daq.DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS`

### `def power_down_all_ao_channels(channel_names=ANALOG_OUT_CHANNELS, parameters=RANGE_PARAMETERS)`

Turn off configured AO channels by configuring to 0V

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/sensor_tests/turn_off_power_channels.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/sensor_tests/turn_off_power_channels.py

### MODULE DOCSTRING

This example resets all the configured Power Channels to 0 volts and 0 amps

- `OUTPUT_TERMINAL = 'Simulated_Power/power'`

### `def setup(output_terminal=OUTPUT_TERMINAL)`

Creates the necessary objects for voltage generation

### `def main(pssm: daq.PowerSupplySourceAndMeasure)`

Sets up the volatge and current to be generated.

### `def cleanup(pssm: daq.PowerSupplySourceAndMeasure)`

### `def close_power_supply(generation_output_channel=OUTPUT_TERMINAL)`

Executes all steps in Sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/synchronization_tests/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/synchronization_tests/__init__.py

### MODULE DOCSTRING

Contains files used for automation testing of pcbatt synchronization classes

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/synchronization_tests/digital_clock_generation_and_pwm_measurement.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/synchronization_tests/digital_clock_generation_and_pwm_measurement.py

### MODULE DOCSTRING

This example demonstrates generation of Digital Clock signal using Digital Clock Generation 
   Library and measurement of the same signal using Digital PWM Measurement Library

- `PHYSICAL_CHANNEL_OUT = '/Sim_PC_basedDAQ/ctr0'`

- `OUTPUT_TERMINAL = '/Sim_PC_basedDAQ/PFI0'`

- `PHYSICAL_CHANNEL_IN = '/Sim_PC_basedDAQ1/ctr0'`

- `INPUT_TERMINAL = '/Sim_PC_basedDAQ1/PFI0'`

- `GLOBAL_CHANNEL_COUNTER = ''`

- `DEFAULT_FILEPATH = 'C:\\Windows\\Temp\\digital_clock_generation_and_pwm_measurement_results.txt'`

### `def setup(output_terminal=OUTPUT_TERMINAL, gen_counter_channel=PHYSICAL_CHANNEL_OUT, input_terminal=INPUT_TERMINAL, meas_counter_channel=PHYSICAL_CHANNEL_IN)`

Creates the necessary objects for the generation and measurement of digital clock

### `def main(generation_instance: daq.DigitalClockGeneration, measurement_instance: daq.DigitalPwmMeasurement, write_to_file: True, filepath=DEFAULT_FILEPATH)`

If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path is C:\Windows\Temp\digital_clock_generation_and_pwm_measurement_results.txt
    

### `def cleanup(generation_instance: daq.DigitalClockGeneration, measurement_instance: daq.DigitalPwmMeasurement)`

Closes out the created objects used in the generation and measurement

### `def digital_clock_generation_and_pwm_measurement(generation_output_channel=OUTPUT_TERMINAL, generation_counter_channel=PHYSICAL_CHANNEL_OUT, measurement_input_channel=INPUT_TERMINAL, measurement_counter_channel=PHYSICAL_CHANNEL_IN, write_to_file=True, filepath=DEFAULT_FILEPATH)`

Execute all steps in the sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/synchronization_tests/dynamic_digital_pattern_generation_and_measurement.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/synchronization_tests/dynamic_digital_pattern_generation_and_measurement.py

### MODULE DOCSTRING

This example demonstrates synchronization using Dynamic Digital Pattern Generation Library to 
   generate Digital Pattern from one Backplane and capture it using Dynamic Digital Pattern 
   Measuerment library in another Backplane

- `GENERATION_CHANNEL = 'TS_Digital0,TS_Digital1'`

- `MEASUREMENT_CHANNEL = 'TP_Digital2,TP_Digital3'`

- `SAMPLE_CLOCK_LINE = '/Sim_PC_basedDAQ/PFI0'`

- `START_TRIGGER_LINE = '/Sim_PC_basedDAQ/PFI1'`

- `DEFAULT_FILEPATH = 'C:\\Windows\\Temp\\dynamic_digital_pattern_generation_and_measurement_results.txt'`

### `def setup(generation_channel=GENERATION_CHANNEL, measurement_channel=MEASUREMENT_CHANNEL)`

Creates the necessary objects for the generation and measurement of digital patterns

### `def main(generation_instance: daq.DynamicDigitalPatternGeneration, measurement_instance: daq.DynamicDigitalPatternMeasurement, write_to_file=True, filepath=DEFAULT_FILEPATH)`

If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path for the results of this sequence is:
    C:\Windows\Temp\dynamic_digital_pattern_generation_and_measurement_results.txt

### `def cleanup(generation_instance: daq.DynamicDigitalPatternGeneration, measurement_instance: daq.DynamicDigitalPatternMeasurement, sync_signals: daq.SynchronizationSignalRouting)`

Closes out the created objects used in the generation and measurement.

### `def dynamic_digital_pattern_generation_and_measurement(generation_channel=GENERATION_CHANNEL, measurement_channel=MEASUREMENT_CHANNEL, write_to_file=True, filepath=DEFAULT_FILEPATH)`

Execute all steps in the sequence.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/synchronization_tests/signal_voltage_and_time_domain_measure.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/synchronization_tests/signal_voltage_and_time_domain_measure.py

### MODULE DOCSTRING

This example demonstrates synchronization using Signal Voltage Generation Library to generate 
   a Analog Sine waveform from one Backplane and capture it using Time Domain Measuerment 
   library in another Backplane

- `SIGNAL_CHANNEL = 'TS_Analog0'`

- `ANALOG_INPUT_CHANNEL = 'TP_Analog1'`

- `SAMPLE_CLOCK_LINE = '/Sim_PC_basedDAQ/PFI0'`

- `START_TRIGGER_LINE = '/Sim_PC_basedDAQ/PFI1'`

- `DEFAULT_FILEPATH = 'C:\\Windows\\Temp\\signal_voltage_and_time_domain_measurement_results.txt'`

### `def setup(signal_channel=SIGNAL_CHANNEL, measurement_channel=ANALOG_INPUT_CHANNEL)`

Creates the necessary objects for the generation and measurement of the signal

### `def main(generation_instance: daq.SignalVoltageGeneration, measurement_instance: daq.TimeDomainMeasurement, write_to_file=True, filepath=DEFAULT_FILEPATH)`

Note to run with Hardware: Review the Configurations & update the Sample Clock Source
    and Digital Start Trigger Settings based on NI MAX and Setup Connections

### `def cleanup(generation_instance: daq.SignalVoltageGeneration, measurement_instance: daq.TimeDomainMeasurement, sync_signals: daq.SynchronizationSignalRouting)`

Closes out the created objects used in the generation and measurement

### `def signal_voltage_and_time_domain_measurement(generation_channel=SIGNAL_CHANNEL, measurement_channel=ANALOG_INPUT_CHANNEL, write_to_file=True, filepath=DEFAULT_FILEPATH)`

Execute all steps in the sequence

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/synchronization_tests/synchronization_main_sequence.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/synchronization_tests/synchronization_main_sequence.py

### MODULE DOCSTRING

Main Sequence for executing Power Supply Tests

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/synchronization_tests/turn_off_all_ao_channels.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/synchronization_tests/turn_off_all_ao_channels.py

### MODULE DOCSTRING

This example resets all configured Analog output channels to 0 volts

- `ANALOG_OUT_CHANNELS = 'Sim_PC_basedDAQ/ao0:3'`

- `RANGE_PARAMETERS = daq.DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS`

### `def power_down_all_ao_channels(channel_names=ANALOG_OUT_CHANNELS, parameters=RANGE_PARAMETERS)`

Turn off configured AO channels by configuring to 0V

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_automation/synchronization_tests/turn_off_all_do_channels.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_automation/synchronization_tests/turn_off_all_do_channels.py

### MODULE DOCSTRING

This example resets all configured Digital output channels voltage to 0 Volts

- `DIGITAL_OUT_CHANNELS = 'Sim_PC_basedDAQ/port0/line0:7'`

### `def power_down_all_do_channels()`

Set digital state to LOW on all digital output channels

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_communication_library/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_communication_library/__init__.py

### MODULE DOCSTRING

Provides a set of protocol based communciation modules using python written functions

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_communication_library/_ni_845x_internal/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_communication_library/_ni_845x_internal/__init__.py

### MODULE DOCSTRING

Provides private modules related to ni 845x communication protocols

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_communication_library/_ni_845x_internal/_ni_845x_functions.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_communication_library/_ni_845x_internal/_ni_845x_functions.py

### MODULE DOCSTRING

Private module that provides a set of ni-845x functions
used in pcbatt_communication library modules.

### `class _Ni845xFunctionsNames()`

Constants defining NI-845X functions names

- `NI_845X_DLL = 'Ni845x.dll'`

- `MAX_BYTE_VALUE = 255`

- `WRITE_INSTRUCTION = 2`

- `READ_INSTRUCTION = 3`

- `FIRST_FOUR_BYTES_MASK = 15`

### `def ni_845x_open_impl(device_name: str) -> int`

Opens the specific NI-845x device.

    Args:
        device_name (str): The name of the device to be opened.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xOpen` function from `ni845x.dll`.
    

### `def ni_845x_close_impl(device_handle: int)`

Closes a previously opened device.

    Args:
        device_handle (int):
            The device handle to be closed.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xClose` function from `ni845x.dll`.
    

### `def ni_845x_device_lock_impl(device_handle: int)`

Locks NI 845x devices for access by a single thread.

    Args:
        device_handle (int):
            The device handle to be locked.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xDeviceLock`
            function from `ni845x.dll`.
    

### `def ni_845x_device_unlock_impl(device_handle: int)`

Unlocks NI 845x devices.

    Args:
        device_handle (int):
            The device handle to be unlocked.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xUnlock` function from `ni845x.dll`.
    

### `def ni_845x_set_io_voltage_level_impl(device_handle: int, voltage_level: Ni845xVoltageLevel)`

Modifies the voltage output from a DIO port on an NI 845x device.

    Args:
        device_handle (int):
            The device handle returned from `ni_845x_open`.
        voltage_level (_Ni845xVoltageLevel):
            The desired voltage level.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xSetIoVoltageLevel`
            function from `ni845x.dll`.
    

### `def ni_845x_set_timeout_impl(device_handle: int, timeout_milliseconds: int)`

Modifies the global timeout for operations when using an NI 845x device.

    Args:
        device_handle (int):
            The device handle returned from `ni_845x_open`.
        timeout_milliseconds (int):
            The timeout value in milliseconds.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xSetTimeout`
            function from `ni845x.dll`.
    

### `def ni_845x_find_device_impl() -> DevicesFindResultData`

Finds an NI 845x device and returns the total number of NI 845x devices present.

    Returns:
        DevicesFindResultData: Tuple representing
            the name of the first device found,
            the handle identifying this search session (this handle is used as an input in
            ni845xFindDeviceNext and ni845xCloseFindDeviceHandle)
            and the total number of NI-845x devices found in the system.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xFindDevice`
            function from `ni845x.dll`.
    

### `def ni_845x_find_device_next_impl(find_device_handle: int) -> str`

Finds subsequent devices after `ni845xFindDevice` has been called.

    Args:
        find_device_handle (int):
            The device handle returned from `ni845xFindDevice`.

    Returns:
        str: The name of the next NI-845x device found.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xFindDeviceNext`
            function from `ni845x.dll`.
    

### `def ni_845x_close_find_device_handle_impl(find_device_handle: int)`

Closes the handles created by `ni845xFindDevice`.

        Args:
            find_device_handle (int):
                The find device handle to be closed.
    (
        Raises:
            PCBATTCommunicationException:
                Raised when an error occured while calling `ni845xCloseFindDeviceHandle`
                function from `ni845x.dll`.
    

### `def ni_845x_i2c_configuration_open_impl() -> int`

Creates a new NI-845x I2C configuration.

    Returns:
        int:
            The configuration handle.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xI2cConfigurationOpen`
            function from `ni845x.dll`.
    

### `def ni_845x_i2c_configuration_close_impl(configuration_handle: int)`

Closes an I2C I/O configuration.

    Args:
        configuration_handle (int):
            The configuration handle.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xI2cConfigurationClose`
            function from `ni845x.dll`.
    

### `def ni_845x_spi_configuration_open_impl() -> int`

Creates a new NI-845x SPI configuration.

    Returns:
        int:
            The configuration handle.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xSpiConfigurationOpen`
            function from `ni845x.dll`.
    

### `def ni_845x_spi_configuration_close_impl(configuration_handle: int)`

Closes an SPI configuration.

    Args:
        configuration_handle (int):
            The configuration handle.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xSpiConfigurationClose`
            function from `ni845x.dll`.
    

### `def ni_845x_i2c_read_impl(device_handle: int, configuration_handle: int, read_data_array: numpy.ndarray)`

Reads an array of data from an I2C slave device.

    Args:
        device_handle (int):
            The device handle returned from `ni845xOpen`.
        configuration_handle (int):
            The configuration handle.
        read_data_array (numpy.ndarray):
            A numpy array that receives the data read from I2C device.

    Raises:
        TypeError:
            raised if the type of numpy array is not `numpy.ubyte`.
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xI2cRead` function from `ni845x.dll`.
    

### `def ni_845x_i2c_write_impl(device_handle: int, configuration_handle: int, write_data_array: numpy.ndarray)`

Writes an array of data to an I2C slave device.

    Args:
        device_handle (int):
            The device handle returned from `ni_845x_open`.
        configuration_handle (int):
            The configuration handle.
        write_data_array (numpy.ndarray):
            A numpy array containing the data to be written to I2C device.

    Raises:
        TypeError:
            raised if the type of numpy array is not `numpy.ubyte`.
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xI2cWrite` function from `ni845x.dll`.
    

### `def ni_845x_i2c_write_read_impl(device_handle: int, configuration_handle: int, write_data_array: numpy.ndarray, read_data_array: numpy.ndarray)`

Performs a write followed by read (combined format) on an I2C slave device.

    Args:
        device_handle (int):
            The device handle returned from `ni_845x_open`.
        configuration_handle (int):
            The configuration handle.
        write_data_array (numpy.ndarray):
            A numpy array containing the data to be written to I2C device.
        read_data_array (numpy.ndarray):
            A numpy array that receives the data read from I2C device.

    Raises:
        TypeError:
            raised if the type of numpy array is not `numpy.ubyte`.
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xI2cWriteRead`
            function from `ni845x.dll`.
    

### `def ni_845x_spi_write_read_impl(device_handle: int, configuration_handle: int, write_data_array: numpy.ndarray, read_data_array: numpy.ndarray)`

Exchanges an array of data with an SPI slave device.

    Args:
        device_handle (int):
            The device handle returned from `ni845xOpen`.
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.
        write_data_array (numpy.ndarray):
            A numpy array containing the data to be written to SPI device.
        read_data_array (numpy.ndarray):
            A numpy array that receives the data read from SPI device.

    Raises:
        TypeError:
            raised if the type of numpy array is not `numpy.ubyte`.
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xSpiWriteRead`
            function from `ni845x.dll`.
    

### `def ni_845x_i2c_set_pullup_enable_impl(device_handle: int, pullup_status: Ni845xPullupStatus)`

Enables or disables the onboard pullup resistors for I2C operations.

    Args:
        device_handle (int):
            The device handle returned from `ni_845x_open`.
        pullup_status (_Ni845xPullupStatus):
            The status for the pullup resistors.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xI2cSetPullupEnable`
            function from `ni845x.dll`.
    

### `def ni_845x_i2c_configuration_set_address_impl(configuration_handle: int, address: int)`

Sets the configuration's I2C slave address.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xI2cConfigurationOpen`.
        address (int):
            Specifies the address of the I2C Slave device.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xI2cConfigurationSetAddress` function from `ni845x.dll`.
    

### `def ni_845x_i2c_configuration_set_clock_rate_impl(configuration_handle: int, clock_rate_kilohertz: int)`

Sets the configuration clock rate in kilohertz.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xI2cConfigurationOpen`.
        clock_rate_kilohertz (int):
            Specifies the I2C clock rate in kilohertz.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xI2cConfigurationSetClockRate` function from `ni845x.dll`.
    

### `def ni_845x_i2c_configuration_set_addressing_type_impl(configuration_handle: int, addressing_type: Ni845xI2cAddressingType)`

Sets the configuration addressing type.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xI2cConfigurationOpen`.
        addressing_type (_Ni845xI2cAddressingType):
            The addressing scheme to use when addressing
            the I2C slave device this configuration describes.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xI2cConfigurationSetAddressSize` function from `ni845x.dll`.
    

### `def ni_845x_i2c_configuration_set_ack_poll_timeout_impl(configuration_handle: int, timeout_milliseconds: int)`

Sets the configuration ACK poll timeout in milliseconds.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xI2cConfigurationOpen`.
        timeout_milliseconds (int):
            Specifies the I2C ACK poll timeout in milliseconds.
            When this value is zero, ACK polling is disabled.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xI2cConfigurationSetAckPollTimeout` function from `ni845x.dll`.
    

### `def ni_845x_i2c_configuration_get_address_impl(configuration_handle: int) -> int`

Retrieves the configuration address.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xI2cConfigurationOpen`.

    Returns:
        int: The configuration address

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xI2cConfigurationGetAddress` function from `ni845x.dll`.
    

### `def ni_845x_i2c_configuration_get_clock_rate_impl(configuration_handle: int) -> int`

Retrieves the configuration clock rate in kilohertz.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xI2cConfigurationOpen`.

    Returns:
        int: The clock rate in kilohertz.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xI2cConfigurationGetClockRate` function from `ni845x.dll`.
    

### `def ni_845x_i2c_configuration_get_addressing_type_impl(configuration_handle: int) -> Ni845xI2cAddressingType`

Retrieves the configuration addressing type.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xI2cConfigurationOpen`.

    Returns:
        Ni845xI2cAddressingType: the configuration addressing type.
    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xI2cConfigurationGetAddressSize` function from `ni845x.dll`.
    

### `def ni_845x_i2c_configuration_get_ack_poll_timeout_impl(configuration_handle: int) -> int`

Retrieves the configuration ACK poll timeout in milliseconds.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xI2cConfigurationOpen`.

    Returns:
        int: The ACK poll timeout, in milliseconds.
    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xI2cConfigurationGetAckPollTimeout` function from `ni845x.dll`.
    

### `def ni_845x_spi_configuration_set_chip_select_impl(configuration_handle: int, chip_select: int)`

Sets the configuration chip select.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.
        chip_select (int):
            The chip select line for this configuration.
    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xSpiConfigurationSetChipSelect` function from `ni845x.dll`.
    

### `def ni_845x_spi_configuration_set_clock_rate_impl(configuration_handle: int, clock_rate_kilohertz: int)`

Sets the configuration clock rate in kilohertz.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.
        clock_rate_kilohertz (int):
            Specifies the SPI clock rate in kilohertz.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xSpiConfigurationSetClockRate` function from `ni845x.dll`.
    

### `def ni_845x_spi_configuration_set_clock_phase_impl(configuration_handle: int, clock_phase: SpiConfigurationClockPhase)`

Sets the configuration clock phase.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.
        clock_phase (SpiConfigurationClockPhase):
            The positioning of the data bits relative to the clock edges for the SPI Port.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xSpiConfigurationSetClockPhase` function from `ni845x.dll`.
    

### `def ni_845x_spi_configuration_set_clock_polarity_impl(configuration_handle: int, clock_polarity: SpiConfigurationClockPolarity)`

Sets the configuration clock polarity.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.
        clock_polarity (SpiConfigurationClockPolarity):
            The clock line idle state for the SPI Port (clock polarity).

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xSpiConfigurationSetClockPolarity` function from `ni845x.dll`.
    

### `def ni_845x_spi_configuration_get_chip_select_impl(configuration_handle: int) -> int`

Retrieves the configuration chip select value.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.

    Returns:
        int: The chip select.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xSpiConfigurationGetChipSelect` function from `ni845x.dll`.
    

### `def ni_845x_spi_configuration_get_clock_rate_impl(configuration_handle: int) -> int`

Retrieves the configuration clock rate in kilohertz.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.

    Returns:
        int: The clock rate in kilohertz.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xSpiConfigurationGetClockRate` function from `ni845x.dll`.
    

### `def ni_845x_spi_configuration_get_clock_phase_impl(configuration_handle: int) -> SpiConfigurationClockPhase`

Retrieves the configuration clock phase.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.

    Returns:
        SpiConfigurationClockPhase:
            The positioning of the data bits relative to
            the clock edges for the SPI Port (clock phase).

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xSpiConfigurationSetClockPhase` function from `ni845x.dll`.
    

### `def ni_845x_spi_configuration_get_clock_polarity_impl(configuration_handle: int) -> SpiConfigurationClockPolarity`

Retrieves the configuration clock polarity.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.

    Returns:
        SpiConfigurationClockPolarity:
            The clock line idle state for the SPI Port (clock polarity).

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xSpiConfigurationGetClockPolarity` function from `ni845x.dll`.
    

### `def invoke_ni_845x_function(function_name: str, *args)`

Invokes a function from `ni845x.dll`.

    Args:
        function_name (str): the name of function from `ni845x.dll`.

    Raises:
        ValueError:
            Raised if `function_name` is None, empty or whitespace.
        PCBATTCommunicationException:
            Raised if `function_name` does not exist.
            Raised when an error occured while calling
            the function with `function_name` from `ni845x.dll`.
    

### `def is_ni_845x_installed() -> bool`

Checks whether NI-845x drivers are installed on local system.

### `def ni_845x_device_exists() -> bool`

Checks whether at least a NI-845x device is present on local system.

### `def convert_memory_address_to_data_bytes_array(memory_address: int, address_type: DataMemoryAddressType, address_endianness: DataMemoryAddressEndianness) -> List[int]`

Convert the memory address to an array of bytes used for
    device communication.

    Args:
        memory_address (int):
            The address where data are stored in device memory.
        address_type (DataMemoryAddressType):
            The type of address in device memory.
        address_endianness (DataMemoryAddressEndianness):
            The address endianness.

    Returns:
        List[int]: The array of bytes.
    

### `def create_command_for_spi_read_communication_impl(memory_address: int, address_type: DataMemoryAddressType, address_endianness: DataMemoryAddressEndianness, number_of_bytes_to_read: int) -> List[int]`

Create an array of data bytes representing
    the read command used during SPI communication.

    Args:
        memory_address (int):
            The address where data are stored in device memory.
        address_type (DataMemoryAddressType):
            The type of address in device memory.
        address_endianness (DataMemoryAddressEndianness):
            The address endianness.
        number_of_bytes_to_read:
            The number of bytes to read.
    Returns:
        List[int]: The created array.
    

### `def create_command_for_spi_write_communication_impl(memory_address: int, address_type: DataMemoryAddressType, address_endianness: DataMemoryAddressEndianness, number_of_bytes_to_write: int) -> List[int]`

Create an array of data bytes representing
    the write command used during SPI communication.

    Args:
        memory_address (int):
            The address where data are stored in device memory.
        address_type (DataMemoryAddressType):
            The type of address in device memory.
        address_endianness (DataMemoryAddressEndianness):
            The address endianness.
        number_of_bytes_to_write:
            The number of bytes to write.

    Returns:
        List[int]: The created array.
    

### `def _get_status_description(status: int) -> str`

Converts a status code into a descriptive string.

    Args:
        status (int): Status code returned from an NI-845x function from `ni845x.dll`.

    Returns:
        str: The description of the status code.
    

### `def _get_handle_type() -> Union[c_uint32, c_uint64]`

Retrieves the type of handle used by NI-845x functions
    according to the platform on which the Python executable runs..

### `def _create_one_byte_array(memory_address: int) -> List[int]`

creates an array with one byte element.

    Args:
        value (int): the value to add in the array.

    Returns:
        List[int]: The created array.
    

### `def _create_two_bytes_array_little_endian(memory_address: int) -> List[int]`

creates an array with two bytes with little endianness.

    Args:
        memory_address (int): the value to add in the array.

    Returns:
        List[int]: The created array.
    

### `def _create_two_bytes_array_big_endian(memory_address: int) -> List[int]`

creates an array with two bytes with big endianness.

    Args:
        memory_address (int): the value to add in the array.

    Returns:
        List[int]: The created array.
    

### `def _compute_spi_communication_command(command_code: int, memory_address: int, address_type: DataMemoryAddressType) -> int`

Computes the value of command used for SPI communications

    Args:
        command_code (int): The code of the command.
        memory_address (int):
            The address where data are stored in device memory.
        address_type (DataMemoryAddressType):
            The type of address in device memory.

    Returns:
        int: the computed value for the command.
    

### `def _create_ni_845x_functions_arguments_types(handle_type: Union[c_uint32, c_uint64]) -> Dict[str, List[Type]]`

Creates a dictionary containing the names of functions with the list of types of arguments.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_communication_library/ni_845x_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_communication_library/ni_845x_data_types.py

### MODULE DOCSTRING

Defines datatypes related to NI-845x modules.

### `class DataMemoryAddressType(IntEnum)`

Defines on which the size, in bytes,
    the memory address of the communication device is addressed.

### `class DataMemoryAddressEndianness(IntEnum)`

Defines the endianness of the memory address
    in a device communication using I2C/SPI protocols.

### `class Ni845xPullupStatus(IntEnum)`

Defines the status of pullup resistor.

### `class Ni845xI2cAddressingType(IntEnum)`

Defines the addressing type used for configuration of I2C communication.

### `class Ni845xVoltageLevel(IntEnum)`

Defines the voltage levels supported by NI-845x devices.

### `class SpiConfigurationClockPhase(IntEnum)`

Defines the clock phase used for configuration of SPI communication.

### `class SpiConfigurationClockPolarity(IntEnum)`

Defines the clock polarity used for configuration of SPI communication.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_communication_library/ni_845x_devices.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_communication_library/ni_845x_devices.py

### MODULE DOCSTRING

Provides communication with NI-845x devices.

### `class Ni845xDevicesHandler()`

Defines methods used to handle NI-845x devices.

#### `def __init__(self) -> None`

Default initialization of new `Ni845xI2cDevicesHandler` object

#### `def is_initialized(self) -> bool`

_summary_

        Returns:
            bool: _description_
        

#### `def open(self, device_name: str)`

Opens the specific NI-845x device.

        Args:
            device_name (str): The name of the device to be opened.

        Raises:
            PCBATTLibraryException:
                Raised when an error occured while calling `ni845xOpen` function from `ni845x.dll`
        

#### `def close(self)`

Closes a previously opened device.

        Raises:
            PCBATTLibraryException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xClose` function from `ni845x.dll`
        

#### `def lock(self)`

Locks the device for access by a single thread.

        Raises:
            PCBATTLibraryException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xLock` function from `ni845x.dll`
        

#### `def unlock(self)`

Unlocks the device.

        Raises:
            PCBATTLibraryException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xUnlock` function from `ni845x.dll`
        

#### `def set_input_output_voltage_level(self, voltage_level: Ni845xVoltageLevel)`

Sets the I/O voltage level supported by the device.

        Args:
            voltage_level (Ni845xVoltageLevel): The voltage level.

        Raises:
            PCBATTLibraryException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xSetIoVoltageLevel` function from `ni845x.dll`
        

#### `def set_timeout(self, timeout_milliseconds: int)`

_summary_

        Args:
            timeout_milliseconds (int): _description_

        Raises:
            PCBATTLibraryException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xSetTimeout` function from `ni845x.dll`
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_communication_library/ni_845x_i2c_communication_devices.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_communication_library/ni_845x_i2c_communication_devices.py

### MODULE DOCSTRING

Provides I2C communication with NI-845x devices.

### `class Ni845xI2cDevicesHandler(Ni845xDevicesHandler)`

Defines handler on I2C communication devices.

#### `def __init__(self) -> None`

Default initialization of new `Ni845xI2cDevicesHandler` object.

#### `def close(self)`

Closes a previously opened device.

        Raises:
            PCBATTCommunicationException:
                Raised when an error occured while calling `ni845xClose` function from `ni845x.dll`
        

#### `def configuration(self)`

Gets an instance of `Ni845xI2cConfiguration` used to configure I2C communication.

#### `def read_data(self, number_of_bytes_to_read: int) -> numpy.ndarray[numpy.ubyte]`

Reads a collection of data bytes from an I2C slave device.

        Args:
            number_of_bytes_to_read (int): The number of bytes to read.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xI2cRead` function from `ni845x.dll`

        Returns:
            numpy.ndarray[numpy.ubyte]: A `numpy.ndarray`
            of bytes containing data that have been read.
        

#### `def write_data(self, data_bytes_to_be_written: numpy.ndarray[numpy.ubyte])`

Writes a collection of data bytes to an I2C slave device.

        Args:
            data_bytes_to_be_written (numpy.ndarray[numpy.ubyte]): The number of bytes to write.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                the type of numpy array is not `numpy.ubyte` or
                an error occured while calling `ni845xI2cRead` function from `ni845x.dll`
        

#### `def write_and_read_data(self, data_bytes_to_be_written: numpy.ndarray[numpy.ubyte], number_of_bytes_to_read: int) -> numpy.ndarray[numpy.ubyte]`

Performs a write followed by read (combined format) on an I2C slave device.

        Args:
            data_bytes_to_be_written (numpy.ndarray[numpy.ubyte]): The number of bytes to write.
            number_of_bytes_to_read (int): The number of bytes to read.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xI2cWriteRead` function from `ni845x.dll`

        Returns:
            numpy.ndarray[numpy.ubyte]: A `numpy.ndarray`
            of bytes containing data that have been read.
        

#### `def enable_pullup_resistors(self, enable: bool)`

Enable or disables the on-board pullup resistors for I2C operations.

        Args:
            enable (bool):
               `False`: Pullup resistors are disabled.
               `True`: Pullup resistors are enabled.


        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xI2cSetPullupEnable`
                function from `ni845x.dll`
        

### `class Ni845xI2cConfiguration()`

Defines methods used to configure I2C communication on a I2C device.

#### `def __init__(self, configuration_handle: int) -> None`

Initializes an instance of
        `Ni845xI2cConfiguration` with specific values.

        Args:
            configuration_handle (int): The configuration handle.
        

#### `def address(self) -> int`

Gets the configuration address.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xI2cConfigurationGetAddress`
                function from `ni845x.dll`

        Returns:
            int: The configuration address.
        

#### `def address(self, val: int)`

Sets the configuration's I2C slave address.

        Args:
            val (int): Specifies the address of the I2C Slave device.
        

#### `def clock_rate_kilohertz(self) -> int`

Gets the clock rate of the configuration.

        Raises:
            PCBATTCommunicationException:
                Raised when
                an error occured while calling `ni845xI2cConfigurationGetClockRate`
                function from `ni845x.dll`

        Returns:
            int: The configuration address.
        

#### `def clock_rate_kilohertz(self, val: int)`

Sets the clock rate of the configuration.

        Args:
            val (int): Specifies the I2C clock rate in kilohertz.

        Raises:
            PCBATTCommunicationException:
                Raised when
                an error occured while calling `ni845xI2cConfigurationSetClockRate`
                function from `ni845x.dll`
        

#### `def addressing_type(self) -> Ni845xI2cAddressingType`

Gets the type of address used for configuration.

        Raises:
            PCBATTCommunicationException:
                Raised when
                an error occured while calling `ni845xI2cConfigurationGetAddressSize`
                function from `ni845x.dll`

        Returns:
            int: the type of address used for configuration.
        

#### `def addressing_type(self, val: Ni845xI2cAddressingType)`

Sets the type of address used for configuration.

        Args:
            val (int): the type of address used for configuration.

        Raises:
            PCBATTCommunicationException:
                Raised when
                an error occured while calling `ni845xI2cConfigurationSnoetAddressSize`
                function from `ni845x.dll`
        

#### `def ack_poll_timeout_milliseconds(self) -> int`

Gets the I2C ACK (acknowledge) polling timeout in milliseconds.
           When this value is zero, ACK polling is disabled.
           Otherwise, the read or write procedures call ACK polling
           until an acknowledge (ACK) is detected or the timeout is reached.

        Raises:
            PCBATTCommunicationException:
                Raised when
                an error occured while calling `ni845xI2cConfigurationGetAckPollTimeout`
                function from `ni845x.dll`

        Returns:
            int: The I2C ACK (acknowledge) polling timeout in milliseconds.
        

#### `def ack_poll_timeout_milliseconds(self, val: int)`

Sets the I2C ACK (acknowledge) polling timeout in milliseconds.
           When this value is zero, ACK polling is disabled.
           Otherwise, the read or write procedures call ACK polling
           until an acknowledge (ACK) is detected or the timeout is reached.

        Args:
            val (int): the I2C ACK (acknowledge) polling timeout in milliseconds.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_communication_library/ni_845x_spi_communication_devices.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_communication_library/ni_845x_spi_communication_devices.py

### MODULE DOCSTRING

Provides SPI communication with NI-845x devices.

### `class Ni845xSpiDevicesHandler(Ni845xDevicesHandler)`

Defines handler on SPI devices.

#### `def __init__(self) -> None`

Default initialization of new `Ni845xSpiDevicesHandler` object

#### `def close(self)`

Closes a previously opened device.

        Raises:
            PCBATTCommunicationException:
                Raised when an error occured while calling `ni845xClose` function from `ni845x.dll`
        

#### `def configuration(self)`

Gets an instance of `` used to configure I2C communication.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before.
        

#### `def write_and_read_data(self, data_bytes_to_be_written: numpy.ndarray[numpy.ubyte], number_of_bytes_to_read: int) -> numpy.ndarray[numpy.ubyte]`

Performs a write followed by read (combined format) on an SPI slave device.

        Args:
            data_bytes_to_be_written (numpy.ndarray[numpy.ubyte]): The number of bytes to write.
            number_of_bytes_to_read (int): The number of bytes to read.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xSpiWriteRead` function from `ni845x.dll`

        Returns:
            numpy.ndarray[numpy.ubyte]: A `numpy.ndarray`
            of bytes containing data that have been read.
        

### `class Ni845xSpiConfiguration()`

Defines methods used to configure SPI communication on a SPI device.

#### `def __init__(self, configuration_handle: int) -> None`

Initializes an instance of
        `Ni845xI2cConfiguration` with specific values.

        Args:
            configuration_handle (int): The configuration handle.
        

#### `def chip_select(self) -> int`

Gets the chip select value for SPI configuration.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xSpiConfigurationSetChipSelect`
                function from `ni845x.dll`

        Returns:
            int: The configuration address.
        

#### `def chip_select(self, val: int)`

Sets the chip select value for SPI configuration.

        Args:
            val (int): the chip select value for SPI configuration.
        

#### `def clock_rate_kilohertz(self) -> int`

Gets the clock rate of the SPI configuration.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xSpiConfigurationGetClockRate`
                function from `ni845x.dll`

        Returns:
            int: the clock rate of the SPI configuration.
        

#### `def clock_rate_kilohertz(self, val: int)`

Sets the clock rate of the SPI configuration.

        Args:
            val (int): the clock rate of the SPI configuration.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xSpiConfigurationSetClockRate`
                function from `ni845x.dll`
        

#### `def clock_phase(self) -> SpiConfigurationClockPhase`

Gets the clock phase value for SPI configuration.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xSpiConfigurationGetClockPhase`
                function from `ni845x.dll`

        Returns:
            SpiConfigurationClockPhase: The configuration address.
        

#### `def clock_phase(self, val: SpiConfigurationClockPhase)`

Sets the clock phase value for SPI configuration.

        Args:
            val (int): the clock phase value for SPI configuration.
        

#### `def clock_polarity(self) -> SpiConfigurationClockPolarity`

Gets the clock polarity value for SPI configuration.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xSpiConfigurationGetClockPolarity`
                function from `ni845x.dll`

        Returns:
            int: The clock polarity value for SPI configuration.
        

#### `def clock_polarity(self, val: SpiConfigurationClockPolarity)`

Sets the clock polarity value for SPI configuration.

        Args:
            val (int): the clock polarity value for SPI configuration.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_communication_library/pcbatt_communication_exceptions.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_communication_library/pcbatt_communication_exceptions.py

### MODULE DOCSTRING

Defines a set of exceptions that can be raised by pcbatt communication module

### `class PCBATTCommunicationException(Exception)`

Defines base class for all exception raised by
    nipcatt.pcbatt_communication_library package.

#### `def __init__(self, message: str)`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_communication_library/pcbatt_communication_messages.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_communication_library/pcbatt_communication_messages.py

### MODULE DOCSTRING

Module containing message strings.

### `class PCBATTCommunicationExceptionMessages()`

Messages used in exception classes.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_ft_demo_test_sequence/animation_and_sound_user_input_test.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_ft_demo_test_sequence/animation_and_sound_user_input_test.py

### MODULE DOCSTRING

Animation and Sound User Input Test

### `class AnimationAndSoundUserInputTest()`

#### `def __init__(self)`

#### `def setup(self)`

#### `def initialize_push_user_button(self, channel_expression: str) -> None`

#### `def initialize_tp_tweeter(self, channel_expression: str) -> None`

#### `def initialize_leds_pattern(self, channel_expression: str) -> None`

#### `def main(self)`

#### `def configure_tweeter_meas(self) -> None`

#### `def configure_dig_pattern(self) -> None`

#### `def turn_on_dut_user_button(self) -> None`

#### `def wait_for_500_ms_seconds_push_button(self) -> None`

#### `def turn_off_dut_user_button(self) -> None`

#### `def measure_and_check_leds_pattern(self) -> None`

#### `def fetch_tweeter_sound(self) -> None`

#### `def cleanup(self) -> None`

#### `def close_tweeter_meas(self) -> None`

#### `def close_leds_pattern(self) -> None`

#### `def close_push_button(self) -> None`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_ft_demo_test_sequence/audio_filter_test.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_ft_demo_test_sequence/audio_filter_test.py

### MODULE DOCSTRING

Audio Filter Test

### `class AudioFilterTest()`

#### `def __init__(self)`

#### `def setup(self) -> None`

#### `def initialize_multi_tone_audio_signal_gen(self) -> None`

#### `def initialize_audio_meas(self) -> None`

#### `def main(self) -> None`

#### `def configure_audio_meas(self) -> None`

#### `def send_multi_tone_audio_signal(self) -> None`

#### `def measure_tone(self) -> None`

#### `def cleanup(self) -> None`

#### `def close_multi_tone_audio_signal_gen(self) -> None`

#### `def close_audio_meas(self) -> None`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_ft_demo_test_sequence/limit_exception.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_ft_demo_test_sequence/limit_exception.py

### `class LimitException(BaseException)`

#### `def __init__(self, called_class: str, called_method: str, test: str, lower_limit: float, upper_limit: float, unit: str, value: float) -> None`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_ft_demo_test_sequence/pcba_ft_demo_test_sequence.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_ft_demo_test_sequence/pcba_ft_demo_test_sequence.py

### MODULE DOCSTRING


PCBA FT Demo Test Sequences demonstrates testing of PCBA DUTs using PCIe DAQ and TestScale Hardware. 
These example sequences can be executed in hardware simulation using the Python pcbatt 
measurement libraries and can be built off of for a custom sequencer.

Limits suggested will return a FAIL test with DAQ simulation and they need to be changed 
to match your physical hardware.


### `class MainSequence()`

Sequence for testing different systems

#### `def __init__(self) -> None`

#### `def main(self) -> None`

Main method

#### `def cleanup(self) -> None`

turn everything off

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_ft_demo_test_sequence/power_diagnostics.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_ft_demo_test_sequence/power_diagnostics.py

### MODULE DOCSTRING

Power Diagnostics

### `class PowerDiagnostics()`

#### `def __init__(self)`

#### `def setup(self) -> None`

#### `def initialize_power_supply(self) -> None`

#### `def initialize_dc_regulator_tps(self) -> None`

#### `def main(self) -> None`

#### `def power_on_and_measure_startup_max_current(self) -> None`

#### `def measure_idle_power_consumption(self) -> None`

#### `def measure_dc_regulator_voltages(self) -> None`

#### `def cleanup(self) -> None`

#### `def close_power_supply(self) -> None`

#### `def close_dc_regulators_meas(self) -> None`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_ft_demo_test_sequence/reset_and_self_test.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_ft_demo_test_sequence/reset_and_self_test.py

### MODULE DOCSTRING

Reset and Self-Test

### `class ResetAndSelfTest()`

#### `def __init__(self) -> None`

#### `def setup(self) -> None`

#### `def initialize_reset_button(self) -> None`

#### `def initialize_led_status(self) -> None`

#### `def main(self) -> None`

#### `def turn_on_dut_reset_button(self) -> None`

#### `def wait_for_100_ms_seconds_in_reset_enabled_state(self) -> None`

#### `def turn_off_dut_reset_button(self) -> None`

#### `def get_start_time(self) -> None`

#### `def wait_led_activity(self) -> None`

#### `def led_state_status(self) -> None`

#### `def get_current_time(self) -> None`

#### `def dut_elasped_time_validation_or_timeout(self) -> None`

#### `def cleanup(self) -> None`

#### `def close_led_status(self) -> None`

#### `def close_reset_button(self) -> None`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_ft_demo_test_sequence/turn_off_all_ao_channels.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_ft_demo_test_sequence/turn_off_all_ao_channels.py

### MODULE DOCSTRING

Turn Off all AO Channels

### `class TurnOffAllAOChannels()`

#### `def __init__(self) -> None`

#### `def setup(self) -> None`

#### `def dc_voltage_generation_initialize_ao_channels(self) -> None`

#### `def main(self) -> None`

#### `def dc_voltage_generation_configure_initiate_and_sources_dc_voltage(self) -> None`

#### `def cleanup(self) -> None`

#### `def dc_voltage_generation_close_ao_channels(self) -> None`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/__init__.py

### MODULE DOCSTRING

Provides nipcbatt library of measurement, generation and communication modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/common/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/common/__init__.py

### MODULE DOCSTRING

Provides nipcbatt library common modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/common/common_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/common/common_data_types.py

### MODULE DOCSTRING

Defines datatypes that are common to all pcba test toolkit building blocks.

- `MAXIMUM_NUMBER_OF_DIMENSIONS_IN_NUMPY_ARRAY = 2`

### `class MeasurementExecutionType(Enum)`

Defines the way the measurement is executed.

### `class MeasurementAnalysisRequirement(Enum)`

Defines the way analysis is proceeded during measurement.

### `class SampleTimingEngine(Enum)`

Defines which timing engine to use for the task.

### `class StartTriggerType(Enum)`

Define the types used for start trigger during measurement.

### `class MeasurementOptions(PCBATestToolkitData)`

Defines the options for execution of measurement.

#### `def __init__(self, execution_option: MeasurementExecutionType, measurement_analysis_requirement: MeasurementAnalysisRequirement) -> None`

Used to initialize an instance of `MeasurementOptions`.

        Args:
            execution_option (MeasurementExecutionType):
               The type of measurement execution selected by user.
            measurement_analysis_requirement (MeasurementAnalysisRequirement):
               The measurement analysis requirement selected by user.
        

#### `def execution_option(self) -> MeasurementExecutionType`

Gets the type of measurement execution selected by user.

#### `def measurement_analysis_requirement(self) -> MeasurementAnalysisRequirement`

Gets the measurement analysis requirement selected by user.

### `class SampleClockTimingParameters(PCBATestToolkitData)`

Defines the settings of sample clock timing for measurement.

#### `def __init__(self, sample_clock_source: str, sampling_rate_hertz: int, number_of_samples_per_channel: int, sample_timing_engine: SampleTimingEngine) -> None`

Used to initialize an instance of `SampleClockTimingParameters`.

        Args:
            sample_clock_source (str): The source of the clock.
            sampling_rate_hertz (int): The sampling rate (in Hz).
            number_of_samples_per_channel (int): The number of samples per channel.
            sample_timing_engine (SampleTimingEngine): The engine for sample timing.

        Raises:
            ValueError:
                Raised if `sample_clock_source` is None or empty or white space,
                if `sampling_rate_hertz` is less than or equal to zero.
        

#### `def sample_clock_source(self) -> str`

Gets the source of the clock.

#### `def sampling_rate_hertz(self) -> int`

Gets the sampling rate (in Hz).

#### `def number_of_samples_per_channel(self) -> int`

Gets the number of samples per channel.

#### `def sample_timing_engine(self) -> SampleTimingEngine`

Gets the engine for sample timing.

### `class DynamicDigitalPatternTimingParameters(PCBATestToolkitData)`

Defines the settings of sample clock edge for measurement.

#### `def __init__(self, sample_clock_source: str='OnboardClock', sampling_rate_hertz: float=10000.0, number_of_samples_per_channel: int=50, active_edge: nidaqmx.constants.Edge=nidaqmx.constants.Edge.RISING) -> None`

Used to initialize an instance of `DynamicDigitalPatternTimingParameters`.

        Args:
            sample_clock_source (str): The source of the clock.
            sampling_rate_hertz (float): The sampling rate (in Hz).
            number_of_samples_per_channel (int): The number of samples per channel.
            active_edge (nidaqmx.constants.Edge): The `nidaqmx.constants.Edge` value that specifies on which edge
            of a digital pulse to start acquiring samples.

        Raises:
            ValueError:
                Raised if `sample_clock_source` is None or empty or white space,
                if `sampling_rate_hertz` is None or less than zero,
                if 'number_of_samples_per_channel' is None or less than zero,
                if 'active_edge' is None.
        

#### `def sample_clock_source(self) -> str`

Gets the source of the clock.

#### `def sampling_rate_hertz(self) -> float`

Gets the sampling rate (in Hz).

#### `def number_of_samples_per_channel(self) -> int`

Gets the number of samples per channel.

#### `def active_edge(self) -> nidaqmx.constants.Edge`

Gets the engine for sample timing.

### `class DigitalStartTriggerParameters(PCBATestToolkitData)`

Defines the settings of triggers for measurement.

#### `def __init__(self, trigger_select: StartTriggerType, digital_start_trigger_source: str, digital_start_trigger_edge: nidaqmx.constants.Edge) -> None`

Initializes an instance of `DigitalStartTriggerParameters`.

        Args:
            trigger_select (StartTriggerType): The type of trigger
            digital_start_trigger_source (str): The source of digital start trigger.
            digital_start_trigger_edge (nidaqmx.constants.Edge):
                The `nidaqmx.constants.Edge` value that specifies on which edge
                of a digital pulse to start acquiring or generating samples.

        Raises:
            ValueError:
                Raised if `digital_start_trigger_source` is None or empty or white space.
        

#### `def trigger_select(self) -> StartTriggerType`

Gets the type of trigger.

#### `def digital_start_trigger_source(self) -> str`

Gets the source of digital start trigger.

#### `def digital_start_trigger_edge(self) -> nidaqmx.constants.Edge`

Gets the `nidaqmx.constants.Edge` value
        that specifies on which edge
        of a digital pulse to start acquiring or generating samples.

### `class MeasurementData(PCBATestToolkitData)`

Defines the data captured for measurement.

#### `def __init__(self, data_samples: numpy.ndarray) -> None`

Initializes an instance of `MeasurementData`.

        Args:
            samples (numpy.ndarray):
                The array containing the samples captured for measurement.
        Raises:
            ValueError:
                Raised when `samples` is None or empty.
        

#### `def __eq__(self, value_to_compare: object) -> bool`

instances equality.

        Args:
            value_to_compare (object): the instance of `MeasurementData` to compare.

        Returns:
            bool: True if equals to `value_to_compare`.
        

#### `def samples_per_channel(self) -> Iterable[numpy.ndarray[numpy.float64]]`

Gets a iterable instance on the samples array per channel.

### `class AnalogWaveform(PCBATestToolkitData)`

Define the structure of a waveform.

#### `def __init__(self, channel_name: str, delta_time_seconds: float, samples: numpy.ndarray[float]) -> None`

Used to initialize an instance of `AnalogWaveform`.

        Args:
            channel_name (str): The name of physical channel where samples were captured from.
            delta_time_seconds (float): The time between two samples (in seconds).
            samples (numpy.ndarray): The array of samples.

        Raises:
            ValueError: raised if `channel_name` is None or empty or white space
            or if `delta_time_seconds` if less than or equal to zero
            or if `samples` is none or empty.
        

#### `def __eq__(self, value_to_compare: object) -> bool`

instances equality.

        Args:
            value_to_compare (object): the instance of `AnalogWaveform` to compare.

        Returns:
            bool: True if equals to `value_to_compare`.
        

#### `def channel_name(self) -> str`

Gets the name of physical channel where samples were captured from.

#### `def delta_time_seconds(self) -> float`

Gets the time between two samples (in seconds).

#### `def samples(self) -> numpy.ndarray[float]`

Gets the array of samples.

### `class AmplitudeSpectrum(PCBATestToolkitData)`

Defines the structure of a frequency spectrum.

#### `def __init__(self, channel_name: str, spectrum_start_frequency_hertz: float, spectrum_frequency_resolution_hertz: float, amplitudes: numpy.ndarray[float]) -> None`

Used to initialize an instance of `AmplitudeSpectrum`.

        Args:
            channel_name (`str`): The name of physical channel where samples were captured from.
            spectrum_start_frequency_hertz (`float`):
                The frequency of start of spectrum, expressed in Hertz.
            spectrum_frequency_resolution_hertz (`float`):
                The frequency interval between two amplitude values, expressed in Hertz.
            amplitudes (`numpy.ndarray[float]`): The array of amplitudes.

        Raises:
            ValueError: raised if `channel_name` is None or empty or white space
            or if `spectrum_frequency_resolution_hertz` if less than or equal to zero
            or if `amplitudes` is None or empty.
        

#### `def __eq__(self, value_to_compare: object) -> bool`

instances equality.

        Args:
            value_to_compare (object): the instance of `AmplitudeSpectrum` to compare.

        Returns:
            bool: True if equals to `value_to_compare`.
        

#### `def channel_name(self) -> str`

Gets the name of physical channel where samples were captured from.

#### `def spectrum_frequency_resolution_hertz(self) -> float`

Gets the frequency interval between two amplitude values, expressed in Hertz.

#### `def spectrum_start_frequency_hertz(self) -> float`

Gets the frequency of start of spectrum, expressed in Hertz.

#### `def amplitudes(self) -> numpy.ndarray[float]`

Gets the array of amplitudes.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/common/helper_functions.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/common/helper_functions.py

### MODULE DOCSTRING

Various helper functions usable by any module

### `def format_with_si_prefix(measured_value: float, total_digits: int) -> tuple[str, str]`

Formats a value in engineering notation with an SI prefix.

    Args:
        measured_value: The numerical value to format.
        total_digits: Total number of significant digits to display.

    Returns:
        tuple: (formatted_number, si_prefix)
            - formatted_number: The scaled value as a string with appropriate decimal places.
            - si_prefix: The SI prefix symbol (e.g., 'k', 'M', 'u', 'm') or exponential notation.

    How it works:
        1. Convert measured_value to scientific notation.
        2. Transform to engineering notation (exponent divisible by 3).
        3. Scale the mantissa accordingly to match engineering exponent.
        4. Determine decimal places needed to maintain significant figures.
        5. Map engineering exponent to SI prefix (m, k, M, G, etc.).
        6. Return formatted number and SI prefix.
    

### `def digital_ramp_pattern_generator(number_of_samples: int=None, number_of_digital_lines: int=None)`

Generates Ramp based Digital Output Data couting from 0 upto (2^N)-1 where "N" represents the
    Number of Digital Lines.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/communications/__init__.py

### MODULE DOCSTRING

Provides commnuncations modules for pcbatt

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/common/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/communications/common/__init__.py

### MODULE DOCSTRING

Provides common data types and functions for communication building blocks.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/common/communication_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/communications/common/communication_data_types.py

### MODULE DOCSTRING

Defines datatypes that are common to communication building blocks based on I2C/SPI protocols.

### `class MemoryAddressParameters(PCBATestToolkitData)`

Defines the settings used to specify data
    memory address format in communication device.

#### `def __init__(self, memory_address: int, address_type: DataMemoryAddressType, address_endianness: DataMemoryAddressEndianness)`

Initializes an instance of
        `MemoryAddressSettings` with specific values.

        Args:
            memory_address (int):
                The address where data are stored in device memory.
            address_type (DataMemoryAddressType):
                The type of address in device memory.
            address_endianness (DataMemoryAddressEndianness):
                The address endianness.
        

#### `def memory_address(self) -> int`

Gets the address where data are stored in device memory.

#### `def address_type(self) -> DataMemoryAddressType`

Gets the type of address in device memory.

#### `def address_endianness(self) -> DataMemoryAddressEndianness`

Gets the address endianness.

### `class MemoryPageCharacteristics(PCBATestToolkitData)`

Characteristics of a page in the device memory.
    A page is a sub-collection of the data bytes
    starting at specific index in the data collection and a specific length.

#### `def __init__(self, index_in_data_bytes_array: int, number_of_bytes_in_page: int, data_memory_address: int) -> None`

Initializes an instance of
        `MemoryPageCharacteristics` with specific values.

        Args:
            index_in_data_bytes_array (int):
                The index of first byte of the page in the data bytes array.
            number_of_bytes_in_page (int):
                The number of data bytes in a page.
            data_memory_address (int):
                The address value where the page will be stored.

        Raises:
            ValueError:
                Raised when
                `index_in_data_bytes_array` is negative,
                `number_of_bytes_in_page` is negative or equal to zero,
                `data_memory_address` is negative.
        

#### `def index_in_data_bytes_array(self) -> int`

Gets the index of first byte of the page in the data collection.

#### `def number_of_bytes_in_page(self) -> int`

Gets The number of data bytes in a page.

#### `def data_memory_address(self) -> int`

Gets The address value where the page will be stored.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/common/communication_functions.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/communications/common/communication_functions.py

### MODULE DOCSTRING

Defines functions that are common to communication building blocks based on I2C/SPI protocols.

### `def create_command_for_i2c_communications(address_parameters: MemoryAddressParameters) -> numpy.ndarray[numpy.ubyte]`

Creates an array of data bytes
    representing the command for I2C communications.

    Args:
        address_parameters (MemoryAddressParameters):
            An instance of `MemoryAddressParameters` representing the address for device access.

    Returns:
        numpy.ndarray[numpy.ubyte]: The array of bytes representing the command.
    

### `def create_command_for_spi_read_communication(address_parameters: MemoryAddressParameters, number_of_bytes_to_read: int) -> numpy.ndarray[numpy.ubyte]`

Creates an array of data bytes
    representing the command for SPI read communication.

    Args:
        address_parameters (MemoryAddressParameters):
            An instance of `MemoryAddressParameters` representing the address for device access.
        number_of_bytes_to_read (int):
            The number of bytes to read from SPI device.

    Returns:
        numpy.ndarray[numpy.ubyte]: The array of bytes representing the command.
    

### `def create_command_for_spi_write_communication(address_parameters: MemoryAddressParameters, number_of_bytes_to_write: int) -> numpy.ndarray[numpy.ubyte]`

Creates an array of data bytes
    representing the instruction for SPI write communication.

    Args:
        address_parameters (MemoryAddressParameters):
            An instance of `MemoryAddressParameters` representing the address for device access.
        number_of_bytes_for_access (int):
            The number of bytes to write to SPI device.

    Returns:
        numpy.ndarray[numpy.ubyte]: The array of bytes representing the instruction.
    

### `def compute_pages_characteristics(data_memory_start_address: int, number_of_bytes_to_write: int, number_of_bytes_per_page: int) -> List[MemoryPageCharacteristics]`

Computes the list of contiguous pages that will contain data bytes to write to device.

    Args:
        data_memory_start_address (int):
            The address where data bytes will be written.
            This is also the address of the first page.
        number_of_bytes_to_write (int):
            The total number of bytes to write to device.
        number_of_bytes_per_page (int):
            The number of bytes in a memory page.
    Returns:
        List[MemoryPageCharacteristics]:
            A list of `MemoryPageCharacteristics` representing
            the zone of memory pages where data will be written.
    

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/i2c_communications/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/communications/i2c_communications/__init__.py

### MODULE DOCSTRING

Provides nipcbatt library I2C communication modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_communication_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_communication_constants.py

### MODULE DOCSTRING

 Constants data types for I2C communications.

### `class ConstantsForI2cCommunication()`

Constants used for I2C communication.

- `DEFAULT_I2C_DEVICE_PARAMETERS = I2cDeviceParameters(enable_i2c_pullup_resistor=ConstantsForI2cCommunication.DEFAULT_ENABLE_I2C_PULLUP_RESISTOR, voltage_level=ConstantsForI2cCommunication.DEFAULT_VOLTAGE_LEVEL)`

- `DEFAULT_I2C_COMMUNICATION_PARAMETERS = I2cCommunicationParameters(device_address=ConstantsForI2cCommunication.DEFAULT_DEVICE_ADDRESS, addressing_type=ConstantsForI2cCommunication.DEFAULT_ADDRESSING_TYPE, clock_rate_kilohertz=ConstantsForI2cCommunication.DEFAULT_CLOCK_RATE_KILOHERTZ, ack_poll_timeout_milliseconds=ConstantsForI2cCommunication.DEFAULT_ACK_POLL_TIMEOUT_MILLISECONDS)`

- `DEFAULT_I2C_READ_PARAMETERS = I2cReadParameters(number_of_bytes_to_read=ConstantsForI2cCommunication.DEFAULT_NUMBER_OF_BYTES_TO_READ, memory_address_parameters=MemoryAddressParameters(memory_address=ConstantsForI2cCommunication.DEFAULT_MEMORY_ADDRESS, address_type=ConstantsForI2cCommunication.DEFAULT_MEMORY_ADDRESS_TYPE, address_endianness=ConstantsForI2cCommunication.DEFAULT_MEMORY_ADDRESS_ENDIANNESS))`

- `DEFAULT_I2C_WRITE_PARAMETERS = I2cWriteParameters(number_of_bytes_per_page=ConstantsForI2cCommunication.DEFAULT_NUMBER_OF_BYTES_PER_PAGE, delay_between_page_write_operations_milliseconds=ConstantsForI2cCommunication.DEFAULT_DELAY_BETWEEN_PAGE_WRITE_OPERATIONS_MILLISECONDS, data_to_be_written=numpy.zeros(shape=1, dtype=numpy.ubyte), memory_address_parameters=MemoryAddressParameters(memory_address=ConstantsForI2cCommunication.DEFAULT_MEMORY_ADDRESS, address_type=ConstantsForI2cCommunication.DEFAULT_MEMORY_ADDRESS_TYPE, address_endianness=ConstantsForI2cCommunication.DEFAULT_MEMORY_ADDRESS_ENDIANNESS))`

- `DEFAULT_I2C_READ_COMMUNICATION_CONFIGURATION = I2cReadCommunicationConfiguration(device_parameters=DEFAULT_I2C_DEVICE_PARAMETERS, communication_parameters=DEFAULT_I2C_COMMUNICATION_PARAMETERS, read_parameters=DEFAULT_I2C_READ_PARAMETERS)`

- `DEFAULT_I2C_WRITE_COMMUNICATION_CONFIGURATION = I2cWriteCommunicationConfiguration(device_parameters=DEFAULT_I2C_DEVICE_PARAMETERS, communication_parameters=DEFAULT_I2C_COMMUNICATION_PARAMETERS, write_parameters=DEFAULT_I2C_WRITE_PARAMETERS)`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_data_types.py

### MODULE DOCSTRING

 I2C communication data types 

### `class I2cDeviceParameters(PCBATestToolkitData)`

Defines the parameters used to configure I2C device for communications.

#### `def __init__(self, enable_i2c_pullup_resistor: bool, voltage_level: Ni845xVoltageLevel)`

Initializes an instance of
        `I2cDeviceParameters` with specific values.

        Args:
            enable_i2c_pullup_resistor (bool):
                A boolean value that indicates whether
                the on-board pullup resistors for I2C operations are enabled.
            voltage_level (Ni845xVoltageLevel):
                The `Ni845xVoltageLevel` value
                representing the voltage level of signal
                sent or received during I2C communications.
        

#### `def enable_i2c_pullup_resistor(self) -> bool`

Gets whether the on-board pullup resistors for I2C operations are enabled.

#### `def voltage_level(self) -> Ni845xVoltageLevel`

Gets the `Ni845xVoltageLevel` value.

### `class I2cCommunicationParameters(PCBATestToolkitData)`

Defines the parameters used to configure I2C communications.

#### `def __init__(self, device_address: int, addressing_type: Ni845xI2cAddressingType, clock_rate_kilohertz: int, ack_poll_timeout_milliseconds: int)`

Initializes an instance of
        `I2cCommunicationParameters` with specific values.

        Args:
            device_address (int):
                The address of the device.
            addressing_type (Ni845xI2cAddressingType):
                The addressing type used for configuration of I2C communication.
            clock_rate_kilohertz (int):
                The clock rate to apply to the device communication, in kilohertz.
            ack_poll_timeout_milliseconds (int):
                The I2C ACK (acknowledge) polling timeout
                to apply to the device communication, in milliseconds.

        Raises:
            ValueError:
                Raised when
                `device_address` is negative,
                `clock_rate_kilohertz` is negative or equal to zero,
                `ack_poll_timeout_milliseconds` is negative.
        

#### `def device_address(self) -> int`

Gets the address of the device.

#### `def addressing_type(self) -> Ni845xI2cAddressingType`

Gets the addressing type used for configuration of I2C communication.

#### `def clock_rate_kilohertz(self) -> int`

Gets the clock rate to apply to the device communication.

#### `def ack_poll_timeout_milliseconds(self) -> int`

Gets the I2C ACK (acknowledge) polling timeout
        to apply to the device communication, in milliseconds.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_read_communication.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_read_communication.py

### MODULE DOCSTRING

 Defines class used for I2C read communication on PCB points. 

### `class I2cReadCommunication(BuildingBlockUsingNi845xI2cDevice)`

Defines a way that allows you to perform a read operation from I2C device.

#### `def initialize(self, device_name: str)`

Initializes the communication with the specific NI 845x device.

        Args:
            device_name (str): The name of a communication device.
        

#### `def close(self)`

Closes communication procedure and releases internal resources.

#### `def configure_and_read_data(self, configuration: I2cReadCommunicationConfiguration) -> I2cReadCommunicationData`

Configures and performs read operation according to specific configuration parameters.

        Args:
            configuration (I2cReadCommunicationConfiguration):
                An instance of `I2cReadCommunicationConfiguration`,
                encapsulating parameters used to configure communication.

        Returns:
            I2cReadCommunicationData:
                An instance of `I2cReadCommunicationData`, encapsulating the data bytes read.
        

#### `def configure_device_for_i2c_communications(self, parameters: I2cDeviceParameters) -> None`

Configures the device for I2C communications.

        Args:
            parameters (I2cDeviceParameters):
                A `I2cDeviceParameters` object used to configure the device for I2C communications.
        

#### `def configure_i2c_communication(self, parameters: I2cCommunicationParameters) -> None`

Configures the I2C communication.

        Args:
            parameters (I2cCommunicationParameters):
                A `I2cCommunicationParameters` object used to configure I2C communications.
        

#### `def read_data(self, parameters: I2cReadParameters) -> I2cReadCommunicationData`

Reads data bytes from an I2C device.

        Args:
            parameters (I2cReadParameters):
                A `I2cReadParameters` object used
                to perform read operations on I2C device.

        Returns:
            I2cReadCommunicationData:
                An instance of `I2cReadCommunicationData`, encapsulating the data bytes read.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_read_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_read_data_types.py

### MODULE DOCSTRING

 I2C read communication data types 

### `class I2cReadParameters(PCBATestToolkitData)`

Defines the parameters used to perform read operations on I2C device.

#### `def __init__(self, number_of_bytes_to_read: int, memory_address_parameters: MemoryAddressParameters)`

Initializes an instance of
        `I2cReadParameters` with specific values.

        Args:
            number_of_bytes_to_read (int):
                The number of bytes to read.
            memory_address_parameters (MemoryAddressParameters):
                An instance of `MemoryAddressParameters` that specifies
                the format of memory address.

        Raises:
            ValueError:
                Raised when
                `number_of_bytes_to_read` is negative or equal to zero,
                `memory_address_parameters` is None.
        

#### `def number_of_bytes_to_read(self) -> int`

Gets thhe number of bytes to read.

#### `def memory_address_parameters(self) -> MemoryAddressParameters`

Gets an instance of `MemoryAddressParameters` that specifies
        the format of memory address.

### `class I2cReadCommunicationConfiguration(PCBATestToolkitData)`

Defines parameters used for configuration of the I2C Read communication.

#### `def __init__(self, device_parameters: I2cDeviceParameters, communication_parameters: I2cCommunicationParameters, read_parameters: I2cReadParameters)`

Initializes an instance of
        `I2cReadCommunicationConfiguration` with specific values.

        Args:
            device_parameters (I2cDeviceParameters):
                An instance of `I2cDeviceParameters` that represents
                the parameters used for settings of I2C device for communications.
            communication_parameters (I2cCommunicationParameters):
                An instance of `I2CCommunicationParameters` that represents
                the parameters used for settings of I2C communication.
            read_parameters (I2cReadParameters):
                An instance of `I2cReadParameters` that represents
                the parameters used for settings of I2C Read communication.

        Raises:
            ValueError:
                Raised when
                `device_parameters` is None,
                `communication_parameters` is None,
                `communication_read_parameters` is None.
        

#### `def device_parameters(self) -> I2cDeviceParameters`

Gets an instance of `I2cDeviceParameters` that represents
        the parameters used for settings of I2C device for communications.

#### `def communication_parameters(self) -> I2cCommunicationParameters`

Gets an instance of `I2cCommunicationParameters` that represents
        the parameters used for settings of I2C communication.

#### `def read_parameters(self) -> I2cReadParameters`

Gets an instance of `I2cReadParameters` that represents
        the parameters used for settings of I2C Read communication.

### `class I2cReadCommunicationData(PCBATestToolkitData)`

Defines data obtained after I2C read communication on I2C device.

#### `def __init__(self, data_bytes_read: numpy.ndarray[numpy.ubyte])`

Initializes an instance of
        `I2cReadCommunicationData` with specific values.

        Args:
            data_bytes_read (numpy.ndarray):
                The array of data bytes read from I2C Device.

        Raises:
            ValueError:
                Raised when `data_bytes_read` is None or empty,
        

#### `def __eq__(self, value_to_compare: object) -> bool`

instances equality.

        Args:
            value_to_compare (object): the instance of `I2CReadCommunicationData` to compare.

        Returns:
            bool: True if equals to `value_to_compare`.
        

#### `def data_bytes_read(self) -> numpy.ndarray[numpy.ubyte]`

Gets the array of data bytes read from I2C Device.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_write_communication.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_write_communication.py

### MODULE DOCSTRING

 Defines class used for I2C write communication on PCB points. 

### `class I2cWriteCommunication(BuildingBlockUsingNi845xI2cDevice)`

Defines a way that allows you to perform a write operation to I2C device,

#### `def initialize(self, device_name: str)`

Initializes the communication with the specific NI 845x device.

        Args:
            device_name (str): The name of a communication device.
        

#### `def close(self)`

Closes communication procedure and releases internal resources.

#### `def configure_and_write_data(self, configuration: I2cWriteCommunicationConfiguration) -> None`

Defines class used for I2C write communication on PCB points.

        Args:
            configuration (I2cWriteCommunicationConfiguration):
                An instance of `I2cWriteCommunicationConfiguration`,
                encapsulating parameters used to configure communication.
        

#### `def configure_device_for_i2c_communications(self, parameters: I2cDeviceParameters) -> None`

Configures the device for I2C communications.

        Args:
            parameters (I2cDeviceParameters):
                A `I2cDeviceParameters` object used to configure the device for I2C communications.
        

#### `def configure_i2c_communication(self, parameters: I2cCommunicationParameters) -> None`

Configures the I2C communication.

        Args:
            parameters (I2cCommunicationParameters):
                A `I2cCommunicationParameters` object used to configure I2C communications.
        

#### `def write_data(self, parameters: I2cWriteParameters) -> None`

Reads data bytes from an I2C device.

        Args:
            parameters (I2cWriteParameters):
                A `I2cWriteParameters` object used
                to perform read operations on I2C device.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_write_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/communications/i2c_communications/i2c_write_data_types.py

### MODULE DOCSTRING

 I2C communication data types 

### `class I2cWriteParameters(PCBATestToolkitData)`

Defines the parameters used to perform write operations on I2C device.

#### `def __init__(self, number_of_bytes_per_page: int, delay_between_page_write_operations_milliseconds: int, data_to_be_written: numpy.ndarray[numpy.ubyte], memory_address_parameters: MemoryAddressParameters)`

Initializes an instance of
        `I2cWriteParameters` with specific values.

        Args:
            number_of_bytes_per_page (int):
                The number of bytes per page.
            delay_between_page_write_operations_milliseconds (int):
                The delay time between two page write operations, in ms.
            data_to_be_written (numpy.ndarray[numpy.ubyte]):
                A numpy array containing the data to be written to I2C device.
            memory_address_parameters (MemoryAddressParameters):
                An instance of `MemoryAddressParameters` that specifies
                the format of memory address.

        Raises:
            TypeError:
                raised if the type of numpy array is not `numpy.ubyte`.
            ValueError:
                Raised when
                `number_of_bytes_per_page` is negative or equal to zero,
                `delay_between_page_write_operations_milliseconds` is negative,
                `memory_address_parameters` is None.
        

#### `def __eq__(self, value_to_compare: object) -> bool`

instances equality.

        Args:
            value_to_compare (object): the instance of `I2cWriteParameters` to compare.

        Returns:
            bool: True if equals to `value_to_compare`.
        

#### `def number_of_bytes_per_page(self) -> int`

Gets the number of bytes per page.

#### `def delay_between_page_write_operations_milliseconds(self) -> int`

Gets the delay time between two page write operations, in ms.

#### `def data_to_be_written(self) -> numpy.ndarray[numpy.ubyte]`

Gets the numpy array containing the data to be written to I2C device.

#### `def memory_address_parameters(self) -> MemoryAddressParameters`

Gets an instance of `MemoryAddressParameters` that specifies
        the format of memory address.

### `class I2cWriteCommunicationConfiguration(PCBATestToolkitData)`

Defines parameters used for configuration of the I2C Write communication.

#### `def __init__(self, device_parameters: I2cDeviceParameters, communication_parameters: I2cCommunicationParameters, write_parameters: I2cWriteParameters)`

Initializes an instance of
        `I2cWriteCommunicationConfiguration` with specific values.

        Args:
            device_parameters (I2cDeviceParameters):
                An instance of `I2cDeviceParameters` that represents
                the parameters used for settings of I2C device for communications.
            communication_parameters (I2cCommunicationParameters):
                An instance of `I2cCommunicationParameters` that represents
                the parameters used for settings of I2C communication.
            write_parameters (I2cWriteParameters):
                An instance of `I2cWriteParameters` that represents
                the parameters used for settings of I2C Write communication.

        Raises:
            ValueError:
                Raised when
                `device_parameters` is None,
                `communication_parameters` is None,
                `write_parameters` is None.
        

#### `def device_parameters(self) -> I2cDeviceParameters`

Gets an instance of `I2cDeviceParameters` that represents
        the parameters used for settings of I2C device for communications.

#### `def communication_parameters(self) -> I2cCommunicationParameters`

Gets an instance of `I2cCommunicationParameters` that represents
        the parameters used for settings of I2C communication.

#### `def write_parameters(self) -> I2cWriteParameters`

Gets an instance of `I2cWriteParameters` that represents
        the parameters used for settings of I2C Write communication.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/serial_communications/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/communications/serial_communications/__init__.py

### MODULE DOCSTRING

Provides nipcbatt library serial communication modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/serial_communications/serial_communication.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/communications/serial_communications/serial_communication.py

### MODULE DOCSTRING

 Defines class used for serial communication on serial devices. 

### `class SerialCommunication(BuildingBlockUsingVisa)`

Defines a way that allows you to perform operations on serial device.

#### `def initialize(self, serial_device_name: str)`

Initializes the communication with the specific serial device.

        Args:
            serial_device_name (str): The name of a serial device.
        

#### `def close(self)`

Closes communication procedure and releases internal resources.

#### `def configure_then_send_command_and_receive_response(self, configuration: SerialCommunicationConfiguration) -> SerialCommunicationData`

Configures then performs serial communication operations
        according to specific configuration parameters.

        Args:
            configuration (SerialCommunicationConfiguration):
                An instance of `SerialCommunicationConfiguration`,
                encapsulating parameters used to configure communication.

        Returns:
            SerialCommunicationData:
                An instance of `SerialCommunicationData`
                encapsulating the received response.
        

#### `def configure_serial_communication(self, parameters: SerialCommunicationParameters)`

Configures the serial communication.

        Args:
            parameters (SerialCommunicationParameters):
                A `SerialCommunicationParameters` object used
                to configure the device for serial communications.
        

#### `def send_command_and_receive_response(self, command_to_send: str) -> str`

Sends a command to a serial device and receive response from it.

        Args:
            command_to_send (str): The string representing the command to send.

        Returns:
            str: The response sent back by the serial communication.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/serial_communications/serial_communication_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/communications/serial_communications/serial_communication_constants.py

### MODULE DOCSTRING

 Constants data types for serial communications.

### `class ConstantsForSerialCommunication()`

Constants used for serial communication.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/serial_communications/serial_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/communications/serial_communications/serial_data_types.py

### MODULE DOCSTRING

 Serial communication data types 

### `class SerialCommunicationParameters(PCBATestToolkitData)`

Defines the parameters used to configure serial device for communications.

#### `def __init__(self, data_rate_bauds: int, number_of_bits_in_data_frame: int, delay_before_receive_response_milliseconds: int, parity: pyvisa.constants.Parity, stop_bits: pyvisa.constants.StopBits, flow_control: pyvisa.constants.ControlFlow)`

Initializes an instance of
        `SerialCommunicationParameters` with specific values.

        Args:
            data_rate_bauds (int):
                The baud rate of the communication.
            number_of_bits_in_data_frame (int):
                The number of data bits contained in each frame
                (4, 5, 6, 7, or 8).
            delay_before_receive_response (int):
                The delay time that occurs after the send of command
                and before the reception of response.
            parity (pyvisa.constants.Parity):
                The `pyvisa.constants.Parity` value representing
                the parity used with every frame transmitted and received.
            stop_bits (pyvisa.constants.StopBits):
                The `pyvisa.constants.StopBits` value representing
                the number of stop bits used to indicate the end of a frame.
            flow_control (pyvisa.constants.ControlFlow):
                The `pyvisa.constants.ControlFlow` value representing
                the flow control mechanism(s) used by the serial communication.

        Raises:
            ValueError:
                Raised when
                `data_rate_bauds` is negative or equal to zero,
                `number_of_bits_in_data_frame` is lower than 4 or greater than 8,
                `delay_before_receive_response_milliseconds` is negative or equal to zero.
        

#### `def data_rate_bauds(self) -> int`

Gets the baud rate of the communication.

#### `def number_of_bits_in_data_frame(self) -> int`

Gets the number of data bits contained in each frame
        (4, 5, 6, 7, or 8).

#### `def delay_before_receive_response_milliseconds(self) -> int`

Gets the delay time that occurs after the send of command
        and before the reception of response.

#### `def parity(self) -> pyvisa.constants.Parity`

Gets the `pyvisa.constants.Parity` value representing
        the parity used with every frame transmitted and received.

#### `def stop_bits(self) -> pyvisa.constants.StopBits`

Gets the `pyvisa.constants.StopBits` value representing
        the number of stop bits used to indicate the end of a frame.

#### `def flow_control(self) -> pyvisa.constants.ControlFlow`

Gets the `pyvisa.constants.ControlFlow` value representing
        the flow control mechanism(s) used by the serial communication.

### `class SerialCommunicationConfiguration(PCBATestToolkitData)`

Defines parameters used for configuration of the serial communication.

#### `def __init__(self, communication_parameters: SerialCommunicationParameters, command_to_send: str)`

Initializes an instance of
        `SerialCommunicationConfiguration` with specific values.

        Args:
            communication_parameters (SerialCommunicationParameters):
                An instance of `SerialCommunicationParameters`
                that represents the parameters used for settings of serial communication.
            command_to_send (str):
                The string representing the command to send.

        Raises:
            ValueError:
                Raised when
                `communication_parameters` is None,
                `command_to_send` is None or empty or whitespace.
        

#### `def communication_parameters(self) -> SerialCommunicationParameters`

Gets the instance of `SerialCommunicationParameters`
        that represents the parameters used for settings of serial communication.

#### `def command_to_send(self) -> str`

Gets the string representing the command to send.

### `class SerialCommunicationData(PCBATestToolkitData)`

Defines data obtained after serial communication on serial device.

#### `def __init__(self, received_response: str)`

Initializes an instance of
        `SerialCommunicationData` with specific values.

        Args:
            received_response (str):
                The received response after serial communication.

        Raises:
            ValueError:
                Raised when
                `received_response` is None or empty or whitespace.
        

#### `def received_response(self) -> str`

Gets the received response after serial communication.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/spi_communications/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/communications/spi_communications/__init__.py

### MODULE DOCSTRING

Provides nipcbatt library SPI communication modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/spi_communications/spi_communication_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/communications/spi_communications/spi_communication_constants.py

### MODULE DOCSTRING

 Constants data types for SPI communications.

### `class ConstantsForSpiCommunication()`

Constants used for SPI communication.

- `DEFAULT_SPI_DEVICE_PARAMETERS = SpiDeviceParameters(voltage_level=ConstantsForSpiCommunication.DEFAULT_VOLTAGE_LEVEL)`

- `DEFAULT_SPI_COMMUNICATION_PARAMETERS = SpiCommunicationParameters(chip_select=ConstantsForSpiCommunication.DEFAULT_CHIP_SELECT, clock_rate_kilohertz=ConstantsForSpiCommunication.DEFAULT_CLOCK_RATE_KILOHERTZ, clock_phase=ConstantsForSpiCommunication.DEFAULT_CLOCK_PHASE, clock_polarity=ConstantsForSpiCommunication.DEFAULT_CLOCK_POLARITY)`

- `DEFAULT_SPI_READ_PARAMETERS = SpiReadParameters(number_of_bytes_to_read=ConstantsForSpiCommunication.DEFAULT_NUMBER_OF_BYTES_TO_READ, memory_address_parameters=MemoryAddressParameters(memory_address=ConstantsForSpiCommunication.DEFAULT_MEMORY_ADDRESS, address_type=ConstantsForSpiCommunication.DEFAULT_MEMORY_ADDRESS_TYPE, address_endianness=ConstantsForSpiCommunication.DEFAULT_MEMORY_ADDRESS_ENDIANNESS))`

- `DEFAULT_SPI_WRITE_PARAMETERS = SpiWriteParameters(number_of_bytes_per_page=ConstantsForSpiCommunication.DEFAULT_NUMBER_OF_BYTES_PER_PAGE, delay_between_page_write_operations_milliseconds=ConstantsForSpiCommunication.DEFAULT_DELAY_BETWEEN_PAGE_WRITE_OPERATIONS_MILLISECONDS, data_to_be_written=numpy.zeros(shape=1, dtype=numpy.ubyte), memory_address_parameters=MemoryAddressParameters(memory_address=ConstantsForSpiCommunication.DEFAULT_MEMORY_ADDRESS, address_type=ConstantsForSpiCommunication.DEFAULT_MEMORY_ADDRESS_TYPE, address_endianness=ConstantsForSpiCommunication.DEFAULT_MEMORY_ADDRESS_ENDIANNESS))`

- `DEFAULT_SPI_READ_COMMUNICATION_CONFIGURATION = SpiReadCommunicationConfiguration(device_parameters=DEFAULT_SPI_DEVICE_PARAMETERS, communication_parameters=DEFAULT_SPI_COMMUNICATION_PARAMETERS, read_parameters=DEFAULT_SPI_READ_PARAMETERS)`

- `DEFAULT_SPI_WRITE_COMMUNICATION_CONFIGURATION = SpiWriteCommunicationConfiguration(device_parameters=DEFAULT_SPI_DEVICE_PARAMETERS, communication_parameters=DEFAULT_SPI_COMMUNICATION_PARAMETERS, write_parameters=DEFAULT_SPI_WRITE_PARAMETERS)`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/spi_communications/spi_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/communications/spi_communications/spi_data_types.py

### MODULE DOCSTRING

 SPI communication data types 

### `class SpiDeviceParameters(PCBATestToolkitData)`

Defines the parameters used to configure SPI device for communications.

#### `def __init__(self, voltage_level: Ni845xVoltageLevel)`

Initializes an instance of
        `SpiDeviceParameters` with specific values.

        Args:
            voltage_level (Ni845xVoltageLevel):
                The `Ni845xVoltageLevel` value
                representing the voltage level of signal
                sent or received during SPI communications.
        

#### `def voltage_level(self) -> Ni845xVoltageLevel`

Gets the `Ni845xVoltageLevel` value.

### `class SpiCommunicationParameters(PCBATestToolkitData)`

Defines the parameters used to configure SPI communications.

#### `def __init__(self, chip_select: int, clock_rate_kilohertz: int, clock_phase: SpiConfigurationClockPhase, clock_polarity: SpiConfigurationClockPolarity)`

Initializes an instance of
        `SpiCommunicationParameters` with specific values.

        Args:
            chip_select (int):
                The chip select value for SPI configuration.
            clock_rate_kilohertz (int):
                The clock rate to apply to the device communication, in kilohertz.
            clock_phase (SpiConfigurationClockPhase):
                The SpiConfigurationClockPhase value representing
                the clock phase value for SPI configuration.
            clock_polarity (SpiConfigurationClockPolarity):
                The SpiConfigurationClockPolarity value representing
                the clock polarity value for SPI configuration.

        Raises:
            ValueError:
                Raised when
                `chip_select` is negative,
                `clock_rate_kilohertz` is negative or equal to zero,
        

#### `def chip_select(self) -> int`

Gets the chip select value for SPI configuration.

#### `def clock_rate_kilohertz(self) -> int`

Gets the clock rate to apply to the device communication.

#### `def clock_phase(self) -> SpiConfigurationClockPhase`

Gets the SpiConfigurationClockPhase value representing
        the clock phase value for SPI configuration.

#### `def clock_polarity(self) -> SpiConfigurationClockPolarity`

Gets the SpiConfigurationClockPhase value representing
        the clock polarity value for SPI configuration.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/spi_communications/spi_read_communication.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/communications/spi_communications/spi_read_communication.py

### MODULE DOCSTRING

 Defines class used for SPI read communication on PCB points. 

### `class SpiReadCommunication(BuildingBlockUsingNi845xSpiDevice)`

Defines a way that allows you to perform a read operation from SPI device.

#### `def initialize(self, device_name: str)`

Initializes the communication with the specific NI 845x device.

        Args:
            device_name (str): The name of a communication device.
        

#### `def close(self)`

Closes communication procedure and releases internal resources.

#### `def configure_and_read_data(self, configuration: SpiReadCommunicationConfiguration) -> SpiReadCommunicationData`

Configures and performs read operation according to specific configuration parameters.

        Args:
            configuration (SpiReadCommunicationConfiguration):
                An instance of `SpiReadCommunicationConfiguration`,
                encapsulating parameters used to configure communication.

        Returns:
            SpiReadCommunicationData:
                An instance of `SpiReadCommunicationData`, encapsulating the data bytes read.
        

#### `def configure_device_for_spi_communications(self, parameters: SpiDeviceParameters) -> None`

Configures the device for SPI communications.

        Args:
            parameters (SpiDeviceParameters):
                A `SpiDeviceParameters` object used to configure the device for SPI communications.
        

#### `def configure_spi_communication(self, parameters: SpiCommunicationParameters) -> None`

Configures the SPI communication.

        Args:
            parameters (SpiCommunicationParameters):
                A `SpiCommunicationParameters` object used to configure SPI communications.
        

#### `def read_data(self, parameters: SpiReadParameters) -> SpiReadCommunicationData`

Reads data bytes from an SPI device.

        Args:
            parameters (SpiReadParameters):
                A `SpiReadParameters` object used
                to perform read operations on Spi device.

        Returns:
            SpiReadCommunicationData:
                An instance of `SpiReadCommunicationData`, encapsulating the data bytes read.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/spi_communications/spi_read_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/communications/spi_communications/spi_read_data_types.py

### MODULE DOCSTRING

 SPI communication data types 

### `class SpiReadParameters(PCBATestToolkitData)`

Defines the settings used to perform read operations on SPI device.

#### `def __init__(self, number_of_bytes_to_read: int, memory_address_parameters: MemoryAddressParameters)`

Initializes an instance of
        `SpiReadParameters` with specific values.

        Args:
            number_of_bytes_to_read (int):
                The number of bytes to read.
            memory_address_parameters (MemoryAddressParameters):
                An instance of `MemoryAddressParameters` that specifies
                the format of memory address.

        Raises:
            ValueError:
                Raised when
                `number_of_bytes_per_page` is negative or equal to zero,
                `memory_address_parameters` is None.
        

#### `def number_of_bytes_to_read(self) -> int`

Gets the number of bytes to read.

#### `def memory_address_parameters(self) -> MemoryAddressParameters`

Gets an instance of `MemoryAddressParameters` that specifies
        the format of memory address.

### `class SpiReadCommunicationConfiguration(PCBATestToolkitData)`

Defines parameters used for configuration of the SPI Read communication.

#### `def __init__(self, device_parameters: SpiDeviceParameters, communication_parameters: SpiCommunicationParameters, read_parameters: SpiReadParameters)`

Initializes an instance of
        `SpiReadCommunicationConfiguration` with specific values.

        Args:
            device_parameters (SpiDeviceParameters):
                An instance of `SpiDeviceParameters` that represents
                the parameters used for settings of SPI device for communications.
            communication_parameters (SpiCommunicationParameters):
                An instance of `SPICommunicationParameters` that represents
                the parameters used for settings of SPI communication.
            read_parameters (SpiReadParameters):
                An instance of `SpiReadParameters` that represents
                the parameters used for settings of SPI Read communication.

        Raises:
            ValueError:
                Raised when
                `device_parameters` is None,
                `communication_parameters` is None,
                `communication_read_parameters` is None.
        

#### `def device_parameters(self) -> SpiDeviceParameters`

Gets an instance of `SpiDeviceParameters` that represents
        the parameters used for settings of SPI device for communications.

#### `def communication_parameters(self) -> SpiCommunicationParameters`

Gets an instance of `SpiCommunicationParameters` that represents
        the parameters used for settings of SPI communication.

#### `def read_parameters(self) -> SpiReadParameters`

Gets an instance of `SpiReadParameters` that represents
        the parameters used for settings of SPI Read communication.

### `class SpiReadCommunicationData(PCBATestToolkitData)`

Defines data obtained after SPI read communication on SPI device.

#### `def __init__(self, data_bytes_read: numpy.ndarray[numpy.ubyte])`

Initializes an instance of
        `SpiReadCommunicationData` with specific values.

        Args:
            data_bytes_read (numpy.ndarray):
                The array of data bytes read from SPI Device.

        Raises:
            ValueError:
                Raised when `data_bytes_read` is None or empty,
        

#### `def __eq__(self, value_to_compare: object) -> bool`

instances equality.

        Args:
            value_to_compare (object): the instance of `SpiReadCommunicationData` to compare.

        Returns:
            bool: True if equals to `value_to_compare`.
        

#### `def data_bytes_read(self) -> numpy.ndarray[numpy.ubyte]`

Gets the array of data bytes read from SPI Device.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/spi_communications/spi_write_communication.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/communications/spi_communications/spi_write_communication.py

### MODULE DOCSTRING

 Defines class used for SPI write communication on PCB points. 

### `class SpiWriteCommunication(BuildingBlockUsingNi845xSpiDevice)`

Defines a way that allows you to perform a write operation to SPI device,

#### `def initialize(self, device_name: str)`

Initializes the communication with the specific NI 845x device.

        Args:
            device_name (str): The name of a communication device.
        

#### `def close(self)`

Closes communication procedure and releases internal resources.

#### `def configure_and_write_data(self, configuration: SpiWriteCommunicationConfiguration) -> None`

Defines class used for SPI write communication on PCB points.

        Args:
            configuration (SpiWriteCommunicationConfiguration):
                An instance of `SpiWriteCommunicationConfiguration`,
                encapsulating parameters used to configure communication.
        

#### `def configure_device_for_spi_communications(self, parameters: SpiDeviceParameters) -> None`

Configures the device for SPI communications.

        Args:
            parameters (SpiDeviceParameters):
                A `SpiDeviceParameters` object used to configure the device for SPI communications.
        

#### `def configure_spi_communication(self, parameters: SpiCommunicationParameters) -> None`

Configures the SPI communication.

        Args:
            parameters (SpiCommunicationParameters):
                A `SpiCommunicationParameters` object used to configure SPI communications.
        

#### `def write_data(self, parameters: SpiWriteParameters) -> None`

Reads data bytes from an SPI device.

        Args:
            parameters (SpiWriteParameters):
                A `SpiWriteParameters` object used
                to perform read operations on SPI device.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/spi_communications/spi_write_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/communications/spi_communications/spi_write_data_types.py

### MODULE DOCSTRING

 SPI communication data types 

### `class SpiWriteParameters(PCBATestToolkitData)`

Defines the settings used to perform write operations on SPI device.

#### `def __init__(self, number_of_bytes_per_page: int, delay_between_page_write_operations_milliseconds: int, data_to_be_written: numpy.ndarray[numpy.ubyte], memory_address_parameters: MemoryAddressParameters)`

Initializes an instance of
        `SpiWriteParameters` with specific values.

        Args:
            number_of_bytes_per_page (int):
                The number of bytes per page.
            delay_between_page_write_operations_milliseconds (int):
                The delay time between two page write operations, in ms.
            data_to_be_written (numpy.ndarray[numpy.ubyte]):
                A numpy array containing the data to be written to SPI device.
            memory_address_parameters (MemoryAddressParameters):
                An instance of `MemoryAddressParameters` that specifies
                the format of memory address.

        Raises:
            TypeError:
                raised if the type of numpy array is not `numpy.ubyte`.
            ValueError:
                Raised when
                `number_of_bytes_per_page` is negative or equal to zero,
                `delay_between_page_write_operations_milliseconds` is negative,
                `memory_address_parameters` is None.
        

#### `def __eq__(self, value_to_compare: object) -> bool`

instances equality.

        Args:
            value_to_compare (object): the instance of `SpiWriteParameters` to compare.

        Returns:
            bool: True if equals to `value_to_compare`.
        

#### `def number_of_bytes_per_page(self) -> int`

Gets the number of bytes per page.

#### `def delay_between_page_write_operations_milliseconds(self) -> int`

Gets the delay time between two page write operations, in ms.

#### `def data_to_be_written(self) -> numpy.ndarray[numpy.ubyte]`

Gets the numpy array containing the data to be written to SPI device.

#### `def memory_address_parameters(self) -> MemoryAddressParameters`

Gets an instance of `MemoryAddressParameters` that specifies
        the format of memory address.

### `class SpiWriteCommunicationConfiguration(PCBATestToolkitData)`

Defines parameters used for configuration of the SPI Write communication.

#### `def __init__(self, device_parameters: SpiDeviceParameters, communication_parameters: SpiCommunicationParameters, write_parameters: SpiWriteParameters)`

Initializes an instance of
        `SpiWriteCommunicationConfiguration` with specific values.

        Args:
            device_parameters (SpiDeviceParameters):
                An instance of `SpiDeviceParameters` that represents
                the parameters used for settings of SPI device for communications.
            communication_parameters (SpiCommunicationParameters):
                An instance of `SpiCommunicationParameters` that represents
                the parameters used for settings of SPI communication.
            write_parameters (SpiWriteParameters):
                An instance of `SpiWriteParameters` that represents
                the parameters used for settings of SPI Write communication.

        Raises:
            ValueError:
                Raised when
                `device_parameters` is None,
                `communication_parameters` is None,
                `write_parameters` is None.
        

#### `def device_parameters(self) -> SpiDeviceParameters`

Gets an instance of `SpiDeviceParameters` that represents
        the parameters used for settings of SPI device for communications.

#### `def communication_parameters(self) -> SpiCommunicationParameters`

Gets an instance of `SpiCommunicationParameters` that represents
        the parameters used for settings of SPI communication.

#### `def write_parameters(self) -> SpiWriteParameters`

Gets an instance of `SpiWriteParameters` that represents
        the parameters used for settings of SPI Write communication.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/__init__.py

### MODULE DOCSTRING

Provides nipcbatt library of measurement, generation and modules uaing DAQ hardware

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/common/voltage_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/common/voltage_constants.py

### MODULE DOCSTRING

 Constants data types for Voltage Measurements.

### `class ConstantsForVoltageMeasurement()`

Constants used for Voltage measurement

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/common/voltage_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/common/voltage_data_types.py

### MODULE DOCSTRING

Defines datatypes that are common to DC-RMS Voltage,
   Frequency Domain and Time Domain Measurements.

### `class VoltageRangeAndTerminalParameters(PCBATestToolkitData)`

Defines the parameters used to configure terminal
    of all channels for DC-RMS Voltage measurement.

#### `def __init__(self, terminal_configuration: nidaqmx.constants.TerminalConfiguration, range_min_volts: float, range_max_volts: float) -> None`

Initializes an instance of `VoltageRangeAndTerminalParameters` with specific values.

        Args:
            terminal_configuration (nidaqmx.constants.TerminalConfiguration):
                The input terminal configuration parameter.
            range_min_volts (float):
                The minimum value expected for the measurement on the channel.
            range_max_volts (float):
                The maximum value expected for the measurement on the channel.
        

#### `def terminal_configuration(self) -> nidaqmx.constants.TerminalConfiguration`


        :class:`nidaqmx.constants.TerminalConfiguration`:
            Gets the input terminal configuration parameter.
        

#### `def range_min_volts(self) -> float`


        :type:`float`: Gets the minimum value expected for the measurement on the channel.
        

#### `def range_max_volts(self) -> float`


        :type:`float`: Gets the maximum value expected for the measurement on the channel.
        

### `class VoltageMeasurementChannelAndTerminalRangeParameters(PCBATestToolkitData)`

Defines the parameters used to configure channels for DC-RMS Voltage measurement.

#### `def __init__(self, channel_name: str, channel_parameters: VoltageRangeAndTerminalParameters) -> None`

Initializes an instance of `VoltageMeasurementChannelAndTerminalRangeParameters`
           with specific values.

        Args:
            channel_name (str):
                The name of the channel to configure.
            channel_parameters (VoltageRangeAndTerminalParameters):
                An instance of `VoltageRangeAndTerminalParameters` that specifies
                the parameters used to configure the channel.
        

#### `def channel_name(self) -> str`


        :type:`str`: Gets the name of the channel to configure.
        

#### `def channel_parameters(self) -> VoltageRangeAndTerminalParameters`


        :class:`VoltageRangeAndTerminalParameters`:
            Gets an instance of `VoltageRangeAndTerminalParameters` that specifies
            the parameters used to configure the channel.
        

### `class VoltageGenerationChannelParameters(PCBATestToolkitData)`

Defines the parameters used to configure terminal of all channels for Voltage Generation

#### `def __init__(self, range_min_volts: float, range_max_volts: float) -> None`

Initializes an instance of `VoltageGenerationChannelParameters` with specific values.

        Args:
            range_min_volts (float):
                Specifies the minimum voltage you expect to generate.
            range_max_volts (float):
                Specifies the maximum voltage you expect to generate.

        Raises:
            ValueError:
                Raised when `range_min_volts' is greater than or equal to `range_max_volts`.
        

#### `def range_min_volts(self) -> float`


        :type:`float`: Gets the minimum voltage you expect to generate on the channels.
        

#### `def range_max_volts(self) -> float`


        :type:`float`: Gets the maximum voltage you expect to generate on the channels.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dc_rms_current_measurements/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/dc_rms_current_measurements/__init__.py

### MODULE DOCSTRING

Provides nipcbatt library DC-RMS current measurement modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dc_rms_current_measurements/dc_rms_current_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/dc_rms_current_measurements/dc_rms_current_constants.py

### MODULE DOCSTRING

 Constants data types for DC-RMS Current  Measurements.

### `class ConstantsForDcRmsCurrentMeasurement()`

Constants used for Current measurement

- `DEFAULT_DC_RMS_CURRENT_MEASUREMENT_TERMINAL_RANGE_PARAMETERS = DcRmsCurrentMeasurementTerminalRangeParameters(terminal_configuration=ConstantsForDcRmsCurrentMeasurement.DEFAULT_AI_TERMINAL_CONFIGURATION, range_min_amperes=ConstantsForDcRmsCurrentMeasurement.DEFAULT_CURRENT_RANGE_MINIMUM_AMPERES, range_max_amperes=ConstantsForDcRmsCurrentMeasurement.DEFAULT_CURRENT_RANGE_MAXIMUM_AMPERES, shunt_resistor_ohms=ConstantsForDcRmsCurrentMeasurement.DEFAULT_EXTERNAL_SHUNT_RESISTOR_VALUE_OHMS)`

- `DEFAULT_DC_RMS_CURRENT_MEASUREMENT_OPTIONS = MeasurementOptions(execution_option=ConstantsForDcRmsCurrentMeasurement.DEFAULT_EXECUTION_TYPE, measurement_analysis_requirement=ConstantsForDcRmsCurrentMeasurement.DEFAULT_MEASUREMENT_ANALYSIS_REQUIREMENT)`

- `DEFAULT_DC_RMS_CURRENT_SAMPLE_CLOCK_TIMING_PARAMETERS = SampleClockTimingParameters(sample_clock_source=ConstantsForDcRmsCurrentMeasurement.DEFAULT_SAMPLE_CLOCK_SOURCE, sampling_rate_hertz=ConstantsForDcRmsCurrentMeasurement.DEFAULT_SAMPLING_RATE_HERTZ, number_of_samples_per_channel=ConstantsForDcRmsCurrentMeasurement.DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL, sample_timing_engine=ConstantsForDcRmsCurrentMeasurement.DEFAULT_SAMPLE_TIMING_ENGINE)`

- `DEFAULT_DC_RMS_CURRENT_DIGITAL_START_TRIGGER_PARAMETERS = DigitalStartTriggerParameters(trigger_select=ConstantsForDcRmsCurrentMeasurement.DEFAULT_TRIGGER_TYPE, digital_start_trigger_source=ConstantsForDcRmsCurrentMeasurement.DEFAULT_DIGITAL_START_TRIGGER_SOURCE, digital_start_trigger_edge=ConstantsForDcRmsCurrentMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE)`

- `DEFAULT_DC_RMS_CURRENT_MEASUREMENT_CONFIGURATION = DcRmsCurrentMeasurementConfiguration(global_channel_parameters=DEFAULT_DC_RMS_CURRENT_MEASUREMENT_TERMINAL_RANGE_PARAMETERS, specific_channels_parameters=[], measurement_options=DEFAULT_DC_RMS_CURRENT_MEASUREMENT_OPTIONS, sample_clock_timing_parameters=DEFAULT_DC_RMS_CURRENT_SAMPLE_CLOCK_TIMING_PARAMETERS, digital_start_trigger_parameters=DEFAULT_DC_RMS_CURRENT_DIGITAL_START_TRIGGER_PARAMETERS)`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dc_rms_current_measurements/dc_rms_current_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/dc_rms_current_measurements/dc_rms_current_data_types.py

### MODULE DOCSTRING

 DC-RMS current data types 

### `class DcRmsCurrentMeasurementTerminalRangeParameters(PCBATestToolkitData)`

Defines the parameters used to configure terminal of all channels for DC-RMS Current measurement

#### `def __init__(self, terminal_configuration: nidaqmx.constants.TerminalConfiguration, range_min_amperes: float, range_max_amperes: float, shunt_resistor_ohms: float) -> None`

Initializes an instance of `DcRmsCurrentMeasurementTerminalRangeParameters` with specific values.

        Args:
            terminal_configuration (nidaqmx.constants.TerminalConfiguration):
                The settings of the terminal for all the current channels.
            range_min_amperes (float):
                The minimum current value im amperes expected for the measurement on the channel.
            range_max_amperes (float):
                The maximum current value in amperes expected for the measurement on the channel.
            shunt_resistor_ohms (float):
                The value in ohms of the external shunt resistor.

        Raises:
            ValueError when,
                    the value of `terminal_configuration` is set to None,
                    when `range_min_amperes` is greater or equal to `range_max_amperes`,
                    when `shunt_resistor_ohms` value is less than 'MINIMUM_ALLOWED_SHUNT_RESISTOR_VALUE_OHMS'.
        

#### `def terminal_configuration(self) -> nidaqmx.constants.TerminalConfiguration`


        :class:`nidaqmx.constants.TerminalConfiguration`:
            Gets the input terminal configuration parameter.
        

#### `def range_min_amperes(self) -> float`


        :type:`float`: Gets the minimum value expected for the measurement on the channel.
        

#### `def range_max_amperes(self) -> float`


        :type:`float`: Gets the maximum value expected for the measurement on the channel.
        

#### `def shunt_resistor_ohms(self) -> float`


        :type:`float`: Gets the value in ohms of an external shunt resistor.
        

### `class DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(PCBATestToolkitData)`

Defines the parameters used to configure channels for DC-RMS Current measurement.

#### `def __init__(self, channel_name: str, channel_parameters: DcRmsCurrentMeasurementTerminalRangeParameters) -> None`

Initializes an instance of `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters`
           with specific values.

        Args:
            channel_name (str):
                The name of the channel to configure.
            channel_parameters (DcRmsCurrentMeasurementTerminalRangeParameters):
                An instance of `DcRmsCurrentMeasurementTerminalRangeParameters` that specifies
                the parameters used to configure the channel.

        Raises:
            ValueError when,
                    the value of `channel_name` is set to None or empty or whitespace,
                    when `channel_parameters` is None.
        

#### `def channel_name(self) -> str`


        :type:`str`: Gets the name of the channel to configure.
        

#### `def channel_parameters(self) -> DcRmsCurrentMeasurementTerminalRangeParameters`


        :class:`DcRmsCurrentMeasurementTerminalRangeParameters`:
            Gets an instance of `DcRmsCurrentMeasurementTerminalRangeParameters` that specifies
            the parameters used to configure the channel.
        

### `class DcRmsCurrentMeasurementConfiguration(PCBATestToolkitData)`

Defines parameters used for configuration of the DC-RMS current measurement.

#### `def __init__(self, global_channel_parameters: DcRmsCurrentMeasurementTerminalRangeParameters, specific_channels_parameters: List[DcRmsCurrentMeasurementChannelAndTerminalRangeParameters], measurement_options: MeasurementOptions, sample_clock_timing_parameters: SampleClockTimingParameters, digital_start_trigger_parameters: DigitalStartTriggerParameters) -> None`

Initializes an instance of
        `DcRmsCurrentMeasurementConfiguration` with specific values.

        Args:
            global_channel_parameters (DcRmsCurrentMeasurementTerminalRangeParameters):
                The settings of terminal for all channels.
            specific_channels_parameters (DcRmsCurrentMeasurementChannelAndTerminalRangeParameters):
                The list of instances of `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters` used to configure channels.
            measurement_options (MeasurementOptions):
                An instance of `MeasurementOptions` that represents the settings of options used for execution.
            sample_clock_timing_parameters (SampleClockTimingParameters):
                An instance of `SampleClockTimingParameters` that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters` that represents the settings of triggers.

        Raises:
            TypeError:
                Raised when `specific_channels_parameters`
                contains objects that are not type of `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters`.
            ValueError:
                Raised when `global_channel_parameters` is None,
                `specific_channels_parameters` is None,
                `measurement_options` is None,
                `sample_clock_timing_parameters` is None,
                `digital_start_trigger_parameters` is None,
        

#### `def global_channel_parameters(self) -> DcRmsCurrentMeasurementTerminalRangeParameters`


        :class:`DcRmsCurrentMeasurementTerminalRangeParameters`:
            Gets the settings of terminal for all channels.

#### `def specific_channels_parameters(self) -> List[DcRmsCurrentMeasurementChannelAndTerminalRangeParameters]`


        :class:`List[DcRmsCurrentMeasurementChannelAndTerminalRangeParameters]`:
            Gets the list of instances of
            `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters` used to configure channels.
        

#### `def measurement_options(self) -> MeasurementOptions`


        :class:`MeasurementOptions`:
            Gets a `MeasurementOptions` instance
            that represents the settings of options used for execution.
        

#### `def sample_clock_timing_parameters(self) -> SampleClockTimingParameters`


        :class:`SampleClockTimingParameters`:
            Gets a `SampleClockTimingParameters` instance
            that represents the settings of timing.
        

#### `def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters`


        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        

### `class DcRmsCurrentMeasurementResultData(PCBATestToolkitData)`

Defines the result values computed during analysis procedure for DC-RMS Current measurement.

#### `def __init__(self, waveforms: list[AnalogWaveform], acquisition_duration_seconds: float, dc_values_amperes: list[float], rms_values_amperes: list[float]) -> None`

Initializes an instance of
        `DcRmsCurrentMeasurementResultData` with specific values.

        Args:
            waveforms (List[AnalogWaveform]):
                The list of waveforms acquired from channels defined for measurement and used to compute DC-RMS current.
            acquisition_duration_seconds (float):
                The duration of acquisition of samples for each configured channel.
            dc_values_amperes (List[float]):
                The list of DC value of the current computed for all configured channels, expressed in amperes.
            rms_values_amperes (List[float]):
                The list of RMS value of the current computed for all configured channels, expressed in amperes.

        Raises:
            TypeError when,
                `waveforms` containes objects that are not `AnalogWaveform',
                `dc_values_amperes` contains objects that are not `float',
                `rms_values_amperes` contains objects that are not `float'.
            ValueError when,
                `waveforms` is None.
        

#### `def waveforms(self) -> List[AnalogWaveform]`


        :class:`List[AnalogWaveform]`:
            Gets the list of waveforms acquired from channels defined
            for measurement and used to compute DC-RMS current.
        

#### `def acquisition_duration_seconds(self) -> float`


        :type:`float`:
            Gets the duration of acquisition of samples for each configured channel.
        

#### `def dc_values_amperes(self) -> List[float]`


        :class:`List[float]`:
            Gets the list of DC current computed for all configured channels, expressed in amperes.
        

#### `def rms_values_amperes(self) -> List[float]`


        :class:`List[float]`:
            Gets the list of RMS current computed for all configured channels, expressed in amperes.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dc_rms_current_measurements/dc_rms_current_measurement.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/dc_rms_current_measurements/dc_rms_current_measurement.py

### MODULE DOCSTRING

 Defines class used for DC-RMS Current measurement on PCB points.

### `class DcRmsCurrentMeasurement(BuildingBlockUsingDAQmx)`

Defines a way that allows you to perform DC and RMS current measurements on PCB points.

#### `def initialize(self, analog_input_channel_expression: str, use_specific_channel: bool=False)`

Initializes the measurement with the specific channels

        Args:
            analog_input_channel_expression (str):
                Expression representing the name of a physical channel,
                or a global channel in DAQ System.
        

#### `def close(self)`

Closes measurement procedure and releases internal resources.

#### `def configure_and_measure(self, configuration: DcRmsCurrentMeasurementConfiguration) -> Union[None, DcRmsCurrentMeasurementResultData]`

Configures and/or performs a measurement
           according to specific configuration parameters.

        Args:
        configuration (DcRmsCurrentMeasurementConfiguration): An instance of
            `DcRmsCurrentMeasurementConfiguration` used to configure the measurement.

        Returns:
            DcRmsCurrentMeasurementResultData | None:
              An instance of `DcRmsCurrentMeasurementResultData`
              or `None` if no measure was performed.
        

#### `def configure_all_channels(self, parameters: DcRmsCurrentMeasurementTerminalRangeParameters) -> None`

Configures all channels for DC-RMS Current measurement.

        Args:
            parameters (DcRmsCurrentMeasurementTerminalRangeParameters):
                An instance of `DcRmsCurrentMeasurementTerminalRangeParameters`
                used to configure the channels.
        

#### `def configure_specific_channel(self, parameters: DcRmsCurrentMeasurementChannelAndTerminalRangeParameters) -> None`

Configures the range and terminal configurations
           for specific channels used for DC-RMS current measurement.

        Args:
            parameters (DcRmsCurrentMeasurementChannelAndTerminalRangeParameters):
                An instance of `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters`
            used to configure the channels.
        

#### `def configure_timing(self, parameters: SampleClockTimingParameters)`

Configures the timing characteristics used for Current measurements.
        Args:
            parameters (SampleClockTimingParameters):
            An instance of `SampleClockTimingParameters`
            used to configure the timing.
        

#### `def configure_trigger(self, parameters: DigitalStartTriggerParameters)`

Configure the characteristics of triggers used for Current measurements.

        Args:
            parameters (DigitalStartTriggerParameters):
            An instance of `DigitalStartTriggerParameters`
            used to configure the channels.
        

#### `def acquire_data_for_measurement_analysis(self) -> MeasurementData`

Acquires Data from DAQ channel for measurement of Current.

        Returns:
            MeasurementData: An instance of `MeasurementData`
            that specifies the data acquired from DAQ channels.
        

#### `def analyze_measurement_data(self, measurement_data: MeasurementData, measurement_analysis_requirement: MeasurementAnalysisRequirement) -> DcRmsCurrentMeasurementResultData`

Proceeds to the analysis of DC and RMS current from the measurement data.

        Args:
            data (MeasurementData):
                An instance of `MeasurementData`
                that specifies the data acquired from DAQ channels.
            measurement_analysis_requirement (MeasurementAnalysisRequirement):
                An instance of 'MeasurementAnalysisRequirement' that specifies
                whether to Skip Analysis or Proceed to Analysis.

        Returns:
            DcRmsCurrentMeasurementResultData:
            An instance of `DcRmsCurrentMeasurementResultData`
            that specifies the measurement results.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dc_rms_voltage_measurements/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/dc_rms_voltage_measurements/__init__.py

### MODULE DOCSTRING

Provides nipcbatt library DC-RMS voltage measurement modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dc_rms_voltage_measurements/dc_rms_voltage_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/dc_rms_voltage_measurements/dc_rms_voltage_constants.py

### MODULE DOCSTRING

 Constants data types for DC-RMS Voltage  Measurements.

### `class ConstantsForDcRmsVoltageMeasurement()`

Constants used for Voltage measurement

- `DEFAULT_DC_RMS_VOLTAGE_RANGE_AND_TERMINAL_PARAMETERS = VoltageRangeAndTerminalParameters(terminal_configuration=ConstantsForVoltageMeasurement.DEFAULT_AI_TERMINAL_CONFIGURATION, range_min_volts=ConstantsForVoltageMeasurement.DEFAULT_VOLTAGE_MINIMUM_VALUE_VOLTS, range_max_volts=ConstantsForVoltageMeasurement.DEFAULT_VOLTAGE_MAXIMUM_VALUE_VOLTS)`

- `DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_OPTIONS = MeasurementOptions(execution_option=ConstantsForVoltageMeasurement.DEFAULT_EXECUTION_TYPE, measurement_analysis_requirement=ConstantsForVoltageMeasurement.DEFAULT_MEASUREMENT_ANALYSIS_REQUIREMENT)`

- `DEFAULT_DC_RMS_VOLTAGE_SAMPLE_CLOCK_TIMING_PARAMETERS = SampleClockTimingParameters(sample_clock_source=ConstantsForVoltageMeasurement.DEFAULT_SAMPLE_CLOCK_SOURCE, sampling_rate_hertz=ConstantsForVoltageMeasurement.DEFAULT_SAMPLING_RATE_HERTZ, number_of_samples_per_channel=ConstantsForVoltageMeasurement.DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL, sample_timing_engine=ConstantsForVoltageMeasurement.DEFAULT_SAMPLE_TIMING_ENGINE)`

- `DEFAULT_DC_RMS_VOLTAGE_DIGITAL_START_TRIGGER_PARAMETERS = DigitalStartTriggerParameters(trigger_select=ConstantsForVoltageMeasurement.DEFAULT_TRIGGER_TYPE, digital_start_trigger_source=ConstantsForVoltageMeasurement.DEFAULT_DIGITAL_START_TRIGGER_SOURCE, digital_start_trigger_edge=ConstantsForVoltageMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE)`

- `DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION = DcRmsVoltageMeasurementConfiguration(global_channel_parameters=DEFAULT_DC_RMS_VOLTAGE_RANGE_AND_TERMINAL_PARAMETERS, specific_channels_parameters=[], measurement_options=DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_OPTIONS, sample_clock_timing_parameters=DEFAULT_DC_RMS_VOLTAGE_SAMPLE_CLOCK_TIMING_PARAMETERS, digital_start_trigger_parameters=DEFAULT_DC_RMS_VOLTAGE_DIGITAL_START_TRIGGER_PARAMETERS)`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dc_rms_voltage_measurements/dc_rms_voltage_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/dc_rms_voltage_measurements/dc_rms_voltage_data_types.py

### MODULE DOCSTRING

 DC-RMS Voltage data types 

### `class DcRmsVoltageMeasurementConfiguration(PCBATestToolkitData)`

Defines parameters used for configuration of DC-RMS voltage measurement.

#### `def __init__(self, global_channel_parameters: VoltageRangeAndTerminalParameters, specific_channels_parameters: List[VoltageMeasurementChannelAndTerminalRangeParameters], measurement_options: MeasurementOptions, sample_clock_timing_parameters: SampleClockTimingParameters, digital_start_trigger_parameters: DigitalStartTriggerParameters) -> None`

Initializes an instance of
        `DcRmsVoltageMeasurementConfiguration` with specific values.

        Args:
            global_channel_parameters (VoltageRangeAndTerminalParameters):
                The settings of terminal for all channels.
            specific_channels_parameters (List[VoltageMeasurementChannelAndTerminalRangeParameters]):
                The list of instances of `VoltageMeasurementChannelAndTerminalRangeParameters` used to configure channels.
            measurement_options (MeasurementOptions):
                An instance of `MeasurementOptions` that represents the settings of options used for execution.
            sample_clock_timing_parameters (SampleClockTimingParameters):
                An instance of `SampleClockTimingParameters` that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters` that represents the settings of triggers.

        Raises:
            TypeError:
                Raised when `specific_channels_parameters`
                contains objects that are not type of `VoltageMeasurementChannelAndTerminalRangeParameters`.
            ValueError:
                Raised when
                `specific_channels_parameters` is None,
                `global_channel_parameters` is None,
                `measurement_options` is None,
                `sample_clock_timing_parameters` is None,
                `digital_start_trigger_parameters` is None.
        

#### `def global_channel_parameters(self) -> VoltageRangeAndTerminalParameters`


        :class:`VoltageRangeAndTerminalParameters`:
            Gets the settings of terminal for all channels.

#### `def specific_channels_parameters(self) -> List[VoltageMeasurementChannelAndTerminalRangeParameters]`


        :class:`List[VoltageMeasurementChannelAndTerminalRangeParameters]`:
            Gets the list of instances of
            `VoltageMeasurementChannelAndTerminalRangeParameters` used to configure channels.
        

#### `def measurement_options(self) -> MeasurementOptions`


        :class:`MeasurementOptions`:
            Gets a `MeasurementOptions` instance
            that represents the settings of options used for execution.
        

#### `def sample_clock_timing_parameters(self) -> SampleClockTimingParameters`


        :class:`SampleClockTimingParameters`:
            Gets a `SampleClockTimingParameters` instance
            that represents the settings of timing.
        

#### `def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters`


        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        

### `class DcRmsVoltageMeasurementResultData(PCBATestToolkitData)`

Defines voltage DC-RMS results obtained after waveform analysis.

#### `def __init__(self, waveforms: List[AnalogWaveform], acquisition_duration_seconds: float, dc_values_volts: List[float], rms_values_volts: List[float]) -> None`

Initializes an instance of
        `DcRmsVoltageMeasurementResultData` with specific values.

        Args:
            waveforms (List[AnalogWaveform]):
                The list of waveforms acquired from channels defined for measurement and used to compute DC-RMS voltage.
            acquisition_duration_seconds (float):
                The duration of acquisition of samples for each configured channel.
            dc_values_volts (List[float]):
                The list of DC voltages computed for all configured channels, expressed in Volts.
            rms_values_volts (List[float]):
                The list of RMS voltages computed for all configured channels, expressed in Volts.

        Raises:
            ValueError:
                Raised when `waveforms` is None or empty.
            TypeError:
                Raised when `waveforms` contains objects that are not `AnalogWaveform`,
                `dc_values_volts` contains objects that are not `float`,
                `rms_values_volts` contains objects that are not `float`
        

#### `def waveforms(self) -> List[AnalogWaveform]`


        :class:`List[AnalogWaveform]`:
            Gets the list of waveforms acquired from channels defined
            for measurement and used to compute DC-RMS voltage.
        

#### `def acquisition_duration_seconds(self) -> float`


        :type:`float`:
            Gets the duration of acquisition of samples for each configured channel.
        

#### `def dc_values_volts(self) -> List[float]`


        :class:`List[float]`:
            Gets the list of DC voltages computed for all configured channels, expressed in Volts.
        

#### `def rms_values_volts(self) -> List[float]`


        :class:`List[float]`:
            Gets the list of RMS voltages computed for all configured channels, expressed in Volts.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dc_rms_voltage_measurements/dc_rms_voltage_measurement.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/dc_rms_voltage_measurements/dc_rms_voltage_measurement.py

### MODULE DOCSTRING

 Defines class used for DC-RMS Voltage measurement on PCB points.

### `class DcRmsVoltageMeasurement(BuildingBlockUsingDAQmx)`

Defines a way that allows you to perform DC-RMS voltage measurements on PCB points.

#### `def initialize(self, analog_input_channel_expression: str)`

Initializes the measurement with the specific channels

        Args:
            analog_input_channel_expression (str):
                Expression representing the name of a physical channel,
                or a global channel in DAQ System.
        

#### `def close(self)`

Closes measurement procedure and releases internal resources.

#### `def configure_and_measure(self, configuration: DcRmsVoltageMeasurementConfiguration) -> Union[None, DcRmsVoltageMeasurementResultData]`

Configures and/or performs a measurement
           according to specific configuration parameters.

        Args:
            configuration (DcRmsVoltageMeasurementConfiguration):
            A instance of `DcRmsVoltageMeasurementConfiguration` used to configure the measurement.

        Returns:
            DcRmsVoltageMeasurementResultData | None: An instance of `DcRmsVoltageMeasurementResultData`
              or `None` if no measure was performed.
        

#### `def configure_all_channels(self, parameters: VoltageRangeAndTerminalParameters)`

Configures all channels used for voltage measurements.

        Args:
            parameters (VoltageRangeAndTerminalParameters):
            An instance of `VoltageRangeAndTerminalParameters` used to configure the channels.
        

#### `def configure_specific_channel(self, parameters: VoltageMeasurementChannelAndTerminalRangeParameters)`

Configures the specific channels used for voltage measurements.

        Args:
            parameters (VoltageMeasurementChannelAndTerminalRangeParameters):
            An instance of `VoltageMeasurementChannelAndTerminalRangeParameters`
            used to configure the channels.

        If the user provides Global Virtual Channel name in Initialize(),
        then he/she has to provide the Virtual channel name in Specific channel parameters as well.

        Similarly, if the user provides Physical channel name in Initialize(),
        then he/she has to provide the Physical channel name in Specific channel parameters.
        

#### `def configure_timing(self, parameters: SampleClockTimingParameters)`

Configures the timing characteristics used for voltage measurements.

        Args:
            parameters (SampleClockTimingParameters):
            An instance of `SampleClockTimingParameters`
            used to configure the timing.
        

#### `def configure_trigger(self, parameters: DigitalStartTriggerParameters)`

Configure the characteristics of triggers used for voltage measurements.

        Args:
            parameters (DigitalStartTriggerParameters):
            An instance of `DigitalStartTriggerParameters`
            used to configure the channels.
        

#### `def acquire_data_for_measurement_analysis(self) -> MeasurementData`

Acquires Data from DAQ channel for measurement of voltage.

        Returns:
            MeasurementData: An instance of `MeasurementData`
            that specifies the data acquired from DAQ channels.
        

#### `def analyze_measurement_data(self, measurement_data: MeasurementData, measurement_analysis_requirement: MeasurementAnalysisRequirement) -> DcRmsVoltageMeasurementResultData`

Proceeds to the analysis of DC Voltages from the measurement.

        Args:
             data (MeasurementData):
                An instance of `MeasurementData`
                that specifies the data acquired from DAQ channels.
            measurement_analysis_requirement (MeasurementAnalysisRequirement):
                An instance of 'MeasurementAnalysisRequirement' that specifies
                whether to Skip Analysis or Proceed to Analysis.

        Returns:
            DcRmsVoltageMeasurementResultData:
            An instance of `DcRmsVoltageMeasurementResultData`
            that specifies the measurement results.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dc_voltage_generations/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/dc_voltage_generations/__init__.py

### MODULE DOCSTRING

Provides nipcbatt library DC voltage generation modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dc_voltage_generations/dc_voltage_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/dc_voltage_generations/dc_voltage_data_types.py

### MODULE DOCSTRING

 DC Voltage data types 

### `class DcVoltageGenerationConfiguration(PCBATestToolkitData)`

Defines parameters used for configuration of DC Voltage generation.

#### `def __init__(self, voltage_generation_range_parameters: VoltageGenerationChannelParameters, output_voltages: List[float]) -> None`

Initializes an instance of `DcVoltageGenerationConfiguration` with specific values.

        Args:
            voltage_generation_range_parameters (VoltageGenerationChannelParameters):
                The settings of the terminal for all channel for DC voltage generation.
            output_voltages (List[float]):
                specifies the actual output voltage to generate on the selected channel(s).
                Each element of the array corresponds to a channel in the task.
                The order of the channels in the array corresponds to the order in which you add the channels to the task in the Initialize method.

        Raises:
            ValueError:
                If the input `voltage_generation_range_parameters' does not contain a valid object.
                If the input `output_voltages' is an empty array.
        

#### `def voltage_generation_range_parameters(self) -> VoltageGenerationChannelParameters`


        :class:`VoltageGenerationChannelParameters`:
            Gets an instance of `VoltageGenerationChannelParameters'
            that represents the terminal settings for all channel for DC voltage generation.
        

#### `def output_voltages(self) -> List[float]`


        :class:`List[float]`:
            Gets the list of output voltages to be generated at the selected channel(s).
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dc_voltage_generations/dc_voltage_generation.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/dc_voltage_generations/dc_voltage_generation.py

### MODULE DOCSTRING

 Defines class used for generation of DC voltage on PCB points. 

### `class DcVoltageGeneration(BuildingBlockUsingDAQmx)`

Defines a way for the user to configure the Analog Output pins for DC voltage generation.

#### `def initialize(self, analog_output_channel_expression: str)`

Initializes the DC voltage generation with the specific channels.

        Args:
            analog_output_channel_expression (str):
                Expression representing the name of an analog output physical channel,
                or a global channel in DAQ System.
        

#### `def configure_all_channels(self, parameters: VoltageGenerationChannelParameters) -> None`

Configures all analog output channels for DC Voltage generation.

        Args:
            parameters (VoltageGenerationChannelParameters):
                An instance of `VoltageGenerationChannelParameters' used to configure the channels.
        

#### `def generate_voltage(self, output_voltages: List[float]) -> None`

Generates voltage at the DAQ channel.

        Args:
            output_voltages (List[float]):
                specifies the actual output voltage to generate on the selected channel(s).
                Each element of the array corresponds to a channel in the task.
                The order of the channels in the array corresponds to the order
                in which the channels have been added to the task in the initialize method.

        Raises:
            ValueError:
                If the `output_voltages` is an ampty array.
                If the size of `output_voltages` does not match with the number of channels in the Task.
        

#### `def configure_and_generate(self, configuration: DcVoltageGenerationConfiguration) -> None`

Configures and generates the DC Voltages according to the specific configuration.

        Args:
            configuration (DcVoltageGenerationConfiguration):
                An instance of 'DcVoltageGenerationConfiguration` used to configure the generation of DC voltage.

        Returns:
            None.
        

#### `def close(self)`

Stops and closes the generation task and releases the internal resources.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dc_voltage_generations/dc_voltage_generation_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/dc_voltage_generations/dc_voltage_generation_constants.py

### MODULE DOCSTRING

Constants for DC voltage generation data types.

### `class ConstantsForDcVoltageGeneration()`

Constants used as Initial and defauls values for DC Voltage generation configuration

- `DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS = VoltageGenerationChannelParameters(range_min_volts=ConstantsForDcVoltageGeneration.DEFAULT_RANGE_MIN_VOLTS, range_max_volts=ConstantsForDcVoltageGeneration.DEFAULT_RANGE_MAX_VOLTS)`

- `DEFAULT_DC_VOLTAGE_GENERATION_CONFIGURATION = DcVoltageGenerationConfiguration(voltage_generation_range_parameters=DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS, output_voltages=ConstantsForDcVoltageGeneration.DEFAULT_OUTPUT_VOLTAGES)`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_clock_generations/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/digital_clock_generations/__init__.py

### MODULE DOCSTRING

Provides nipcbatt library digital clock generation modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_clock_generations/digital_clock_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/digital_clock_generations/digital_clock_constants.py

### MODULE DOCSTRING

Constant data types used in digital clock generation

### `class ConstantsForDigitalClockGeneration()`

Constants used in digital clock generation

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_clock_generations/digital_clock_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/digital_clock_generations/digital_clock_data_types.py

### MODULE DOCSTRING

 digital clock data types 

### `class DigitalClockGenerationCounterChannelParameters(PCBATestToolkitData)`

Defines the values to be used to set on the digital clock counter channel

#### `def __init__(self, frequency_hertz: float, duty_cycle_ratio: float) -> None`

Creates an instance of DigitalClockGenerationCounterChannelParameters

        Args:
            frequency_hertz (float): The intended frequency to generate
            duty_cycle_ratio (float): Intended high time % of clock cycle
        

#### `def frequency_hertz(self) -> float`


        :type:'float': Gets the frequency to generate
        

#### `def duty_cycle_ratio(self) -> float`


        :type:float: Gets the duty cycle to generate
        

### `class DigitalClockGenerationTimingParameters(PCBATestToolkitData)`

Defines the timing values to be used in digital clock generation

#### `def __init__(self, clock_duration_seconds: float) -> None`

Creates an instance of DigitalClockGenerationTimingParameters

        Args:
            clock_duration_seconds (float): Clock generation time in seconds
        

#### `def clock_duration_seconds(self) -> float`


        :type:float: Gets the length of the duration of the signal
        

### `class DigitalClockGenerationConfiguration(PCBATestToolkitData)`

Defines values to be used in a digital clock generation configuration

#### `def __init__(self, counter_channel_parameters: DigitalClockGenerationCounterChannelParameters, timing_parameters: DigitalClockGenerationTimingParameters) -> None`

Creates an instance of DigitalClockGenerationConfiguration

        Args:
            counter_channel_parameters (DigitalClockGenerationCounterChannelParameters): An
                instance of DigitalClockGenerationCounterChannelParameters
            timing_parameters (DigitalClockGenerationTimingParameters): An instance of
                DigitalClockGenerationTimingParameters
        

#### `def counter_channel_parameters(self) -> DigitalClockGenerationCounterChannelParameters`


        :type:DigitalClockGenerationCounterChannelParameters: An instance of
            DigitalClockGenerationCounterChannelParameters
        

#### `def timing_parameters(self) -> DigitalClockGenerationTimingParameters`


        :type: DigitalClockGenerationTimingParameters: An instance of
            DigitalClockGenerationTimingParameters
        

### `class DigitalClockGenerationData(PCBATestToolkitData)`

Defines the data that was actually used during digital clock generation

#### `def __init__(self, timebase_frequency_hertz: float, actual_clock_frequency_hertz: float, actual_clock_duty_cycle_ratio: float, actual_clock_duration_seconds: float) -> None`

Creates an instance of DigitalClockGenerationData

        Args:
            timebase_frequency_hertz (float): The timebase used during generation
            actual_clock_frequency_hertz (float): Actual clock frequency used during generation
            actual_clock_duty_cycle_ratio (float): Actual duty cycle used during generation
            actual_clock_duration_seconds (float): Actual clock duration implemented in generation
        

#### `def timebase_frequency_hertz(self) -> float`


        :type:float:
        

#### `def actual_clock_frequency_hertz(self) -> float`


        :type:float
        

#### `def actual_clock_duty_cycle_ratio(self) -> float`


        :type:float
        

#### `def actual_clock_duration_seconds(self) -> float`


        :type:float
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_clock_generations/digital_clock_generation.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/digital_clock_generations/digital_clock_generation.py

### MODULE DOCSTRING

Use this class to generate a digital clock

### `class DigitalClockGeneration(BuildingBlockUsingDAQmx)`

Used to output a digital clock to the hardware

    Args:
        BuildingBlockUsingDAQmx: Base class for all testscale modules
    

#### `def initialize(self, counter_channel_expression: str, output_terminal_name: str)`

_summary_

        Args:
            counter_channel_expression (str): Physical channel of counter to use
            output_terminal_name (str): Terminal on which the signal is measured
        

#### `def configure_counter_channel(self, parameters: DigitalClockGenerationCounterChannelParameters) -> None`

Configures the counter channel used for digital clock generation

        Args:
            parameters (DigitalClockGenerationCounterChannelParameters): An instance
            of DigitalClockGenerationCounterChannelParameters containg frequency
            and duty cycle data
        

#### `def configure_timing(self, parameters: DigitalClockGenerationTimingParameters) -> None`

Defines timing settings used in digital clock generation

        Args:
            parameters (DigitalClockGenerationTimingParameters): Contains
            duration settings used for generation
        

#### `def generate(self, timing: DigitalClockGenerationTimingParameters) -> DigitalClockGenerationData`

Starts the clock signal generation

        Returns:
            DigitalClockGenerationData: Contains the settings that
            were actually written to the instrument
        

#### `def configure_and_generate(self, configuration: DigitalClockGenerationConfiguration)`

Generates a digital clock to the hardware based on the configuration provided

        Args:
            configuration (DigitalClockGenerationConfiguration): A instance of
            DigitalClockGenerationConfiguration containing the settings to be used
        

#### `def close(self)`

_summary_

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_edge_count_measurements/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/digital_edge_count_measurements/__init__.py

### MODULE DOCSTRING

Provides nipcbatt library digital edge counting modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_edge_count_measurements/digital_edge_count_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/digital_edge_count_measurements/digital_edge_count_constants.py

### MODULE DOCSTRING

Constants used in digital edge count measurement

### `class ConstantsForDigitalEdgeCountMeasurement()`

Constants used in digital edge count measurement

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_edge_count_measurements/digital_edge_count_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/digital_edge_count_measurements/digital_edge_count_data_types.py

### MODULE DOCSTRING

  digital edge count data types 

### `class DigitalEdgeCountMeasurementCounterChannelParameters(PCBATestToolkitData)`

Defines the settings counter channel edge for measurement.

#### `def __init__(self, edge_type: nidaqmx.constants.Edge=ConstantsForDigitalEdgeCountMeasurement.DEFAULT_EDGE) -> None`

Used to initialize an instance of `DigitalEdgeCountMeasurementCounterChannelParameters`.

        Args:
            edge_type (nidaqmx.constants.Edge): The `nidaqmx.constants.Edge` value that specifies on which edge
            of a digital pulse the counter increments.

        Raises:
            ValueError:
                if 'active_edge' is None.
        

#### `def edge_type(self) -> nidaqmx.constants.Edge`

Gets the edge type for counter.

### `class DigitalEdgeCountMeasurementTimingParameters(PCBATestToolkitData)`

Defines the timing settings for edge count measurement.

#### `def __init__(self, edge_counting_duration: float=0.1) -> None`

Used to initialize an instance of `DigitalEdgeCountMeasurementTimingParameters`.

        Args:
            edge_counting_duration (float): The value that specifies the duration of edge count measurement.

        Raises:
            ValueError:
                if 'edge_counting_duration' is less than zero and None.
        

#### `def edge_counting_duration(self) -> float`

Gets the duration for edge count measurement.

### `class DigitalEdgeCountHardwareTimerConfiguration(PCBATestToolkitData)`

Defines a configuration for hardware timer digital edge count measurement

#### `def __init__(self, measurement_options: MeasurementOptions, counter_channel_parameters: DigitalEdgeCountMeasurementCounterChannelParameters, timing_parameters: DigitalEdgeCountMeasurementTimingParameters, trigger_parameters: DigitalStartTriggerParameters) -> None`

Initializes an instance of
        `DigitalEdgeCountHardwareTimerConfiguration`.

        Args:
            measurement_options (MeasurementOptions):
                The type of measurement options selected by user.
            counter_channel_parameters (DigitalEdgeCountMeasurementCounterChannelParameters):
                An instance of `DigitalEdgeCountMeasurementCounterChannelParameters` that represents the settings of edge_type.
            timing_parameters (DigitalEdgeCountMeasurementTimingParameters):
                An instance of 'DigitalEdgeCountMeasurementTimingParameters' that represents the duration of edge count measurement.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters` that represents the settings of triggers.

        Raises:
            ValueError:
                'measurement_options' is None,
                `counter_channel_parameters` is None,
                'timing_parameters' is None or less than zero,
                `trigger_parameters` is None,
        

#### `def measurement_options(self) -> MeasurementOptions`


        :class:`MeasurementExecutionType`:
            Gets the type of measurement execution selected by user.
        

#### `def counter_channel_parameters(self) -> DigitalEdgeCountMeasurementCounterChannelParameters`


        :class:`DigitalEdgeCountMeasurementCounterChannelParameters`:
            Gets a `DigitalEdgeCountMeasurementCounterChannelParameters` instance
            that represents the settings of edge_type to be counted.
        

#### `def timing_parameters(self) -> DigitalEdgeCountMeasurementTimingParameters`


        :class:`DigitalEdgeCountMeasurementTimingParameters`:
            Gets a `DigitalEdgeCountMeasurementTimingParameters` instance
            that represents the settings of the time duration in which number of edges to be counted.
        

#### `def trigger_parameters(self) -> DigitalStartTriggerParameters`


        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        

### `class DigitalEdgeCountSoftwareTimerConfiguration(PCBATestToolkitData)`

Defines a configuration for software timer digital edge count measurement

#### `def __init__(self, measurement_options: MeasurementOptions, counter_channel_parameters: DigitalEdgeCountMeasurementCounterChannelParameters, timing_parameters: DigitalEdgeCountMeasurementTimingParameters) -> None`

Initializes an instance of
        `DynamicDigitalPatternMeasurementConfiguration`.

        Args:
            measurement_options (MeasurementOptions):
                The type of measurement options selected by user.
            counter_channel_parameters (DigitalEdgeCountMeasurementCounterChannelParameters):
                An instance of `DigitalEdgeCountMeasurementCounterChannelParameters` that represents the settings of edge_type.
            timing_parameters (DigitalEdgeCountMeasurementTimingParameters):
                An instance of 'DigitalEdgeCountMeasurementTimingParameters' that represents the duration of edge count measurement.

        Raises:
            ValueError:
                'measurement_options' is None,
                `counter_channel_parameters` is None,
                'timing_parameters' is None or less than zero,
        

#### `def measurement_options(self) -> MeasurementOptions`


        :class:`MeasurementExecutionType`:
            Gets the type of measurement execution selected by user.
        

#### `def counter_channel_parameters(self) -> DigitalEdgeCountMeasurementCounterChannelParameters`


        :class:`DigitalEdgeCountMeasurementCounterChannelParameters`:
            Gets a `DigitalEdgeCountMeasurementCounterChannelParameters` instance
            that represents the settings of edge_type to be counted.
        

#### `def timing_parameters(self) -> DigitalEdgeCountMeasurementTimingParameters`


        :class:`DigitalEdgeCountMeasurementTimingParameters`:
            Gets a `DigitalEdgeCountMeasurementTimingParameters` instance
            that represents the settings of the time duration in which number of edges to be counted.
        

### `class DigitalEdgeCountMeasurementResultData(PCBATestToolkitData)`

Defines the values returned from the digital edge count measurement

#### `def __init__(self, edge_count: int, edge_type: nidaqmx.constants.Edge) -> None`

Initializes an instance of 'DigitalEdgeCountMeasurementResultData'
        with specific values

        Args:
            edge_count: int
           edge_type: nidaqmx.constants.Edge

        Raises: ValueError when,
            1) edge_count is None
            2) edge_count is less than zero
            3) edge_type is None
        

#### `def edge_count(self) -> int`


        :type:'int': Edge count data captured from the measurement
        

#### `def edge_type(self) -> nidaqmx.constants.Edge`


        :type:'nidaqmx.constants.Edge': Data captured from the measurement
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_edge_count_measurements/digital_edge_count_measurement_using_hardware_timer.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/digital_edge_count_measurements/digital_edge_count_measurement_using_hardware_timer.py

### MODULE DOCSTRING

Use this class to measure digital edge count using hardware timer

### `class DigitalEdgeCountMeasurementUsingHardwareTimer(BuildingBlockUsingDAQmx)`

class for performing digital edge count measurement using hardware timer

    Args:
        BuildingBlockUsingDAQmx (_type_): Parent class for all PCBATT classes
    

#### `def initialize(self, measurement_channel_expression: str, measurement_input_terminal_name: str, timer_channel_expression: str) -> None`

Creates an instance of DigitalEdgeCountMeasurementUsingHardwareTimer class

        Args:
            measurement_channel_expression (str): specifies the counter resource needed for Edge counting operation.
            measurement_input_terminal_name (str): specifies the input terminal on which to look for digital events / edges.
            timer_channel_expression (str): specifies the counter resource needed for Timer task.
        

#### `def configure_and_measure(self, configuration: DigitalEdgeCountHardwareTimerConfiguration) -> Union[None, DigitalEdgeCountMeasurementResultData]`

Configures and/or performs a measurement
           according to specific configuration parameters.

        Args:
            configuration (DigitalEdgeCountHardwareTimerConfiguration):
            A instance of `DigitalEdgeCountHardwareTimerConfiguration` used to configure the measurement.

        Returns:
            DigitalEdgeCountMeasurementResultData | None: An instance of `DigitalEdgeCountMeasurementResultData`
            or `None` if no measure was performed.
        

#### `def configure_counter_channel(self, parameters: DigitalEdgeCountMeasurementCounterChannelParameters)`

Configures the counter channel parameter for digital edge count measurement.

        Args:
            parameters (DigitalEdgeCountMeasurementCounterChannelParameters):
            An instance of `DigitalEdgeCountMeasurementCounterChannelParameters` used to configure the counter channel parameter.
        

#### `def configure_timing(self, parameters: DigitalEdgeCountMeasurementTimingParameters)`

Configures the edge counting duration for digital edge count measurement.

        Args:
            parameters (DigitalEdgeCountMeasurementTimingParameters):
            An instance of `DigitalEdgeCountMeasurementTimingParameters` used to configure the edge count duration.
        

#### `def configure_trigger(self, parameters: DigitalStartTriggerParameters)`

Configure the characteristics of triggers used for digital edge count measurements.

        Args:
            parameters (DigitalStartTriggerParameters):
            An instance of `DigitalStartTriggerParameters` used to configure the channels.
        

#### `def acquire_data_for_measurement_analysis(self)`

Acquires Data from DAQ channel for measurement of digital edge count.

        Returns:
            DigitalEdgeCountMeasurementResultData:
            An instance of `DigitalEdgeCountMeasurementResultData` that specifies the data acquired from DAQ channels.
        

#### `def close(self)`

Closes the task and returns the hardware resources

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_edge_count_measurements/digital_edge_count_measurement_using_software_timer.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/digital_edge_count_measurements/digital_edge_count_measurement_using_software_timer.py

### MODULE DOCSTRING

Use this class to measure digital edge count using software timer

### `class DigitalEdgeCountMeasurementUsingSoftwareTimer(BuildingBlockUsingDAQmx)`

class for performing digital edge count measurement using software timer

    Args:
        BuildingBlockUsingDAQmx (_type_): Parent class for all PCBATT classes
    

#### `def initialize(self, measurement_channel_expression: str, measurement_input_terminal_name: str) -> None`

Creates an instance of DigitalEdgeCountMeasurementUsingSoftwareTimer class

        Args:
            measurement_channel_expression (str): specifies the counter resource needed for Edge counting operation.
            measurement_input_terminal_name (str): specifies the input terminal on which to look for digital events/edges.
        

#### `def configure_and_measure(self, configuration: DigitalEdgeCountSoftwareTimerConfiguration) -> Union[None, DigitalEdgeCountMeasurementResultData]`

Configures and/or performs a measurement
           according to specific configuration parameters.

        Args:
            configuration (DigitalEdgeCountSoftwareTimerConfiguration):
            A instance of `DigitalEdgeCountSoftwareTimerConfiguration` used to configure the measurement.

        Returns:
            DigitalEdgeCountMeasurementResultData | None: An instance of `DigitalEdgeCountMeasurementResultData`
            or `None` if no measure was performed.
        

#### `def configure_counter_channel(self, parameters: DigitalEdgeCountMeasurementCounterChannelParameters)`

Configures the counter channel parameter for digital edge count measurement.

        Args:
            parameters (DigitalEdgeCountMeasurementCounterChannelParameters):
            An instance of `DigitalEdgeCountMeasurementCounterChannelParameters` used to configure the counter channel parameter.
        

#### `def configure_timing(self, parameters: DigitalEdgeCountMeasurementTimingParameters)`

Configures the edge counting duration for digital edge count measurement.

        Args:
            parameters (DigitalEdgeCountMeasurementTimingParameters):
            An instance of `DigitalEdgeCountMeasurementTimingParameters` used to configure the edge count duration.
        

#### `def acquire_data_for_measurement_analysis(self, configuration: DigitalEdgeCountSoftwareTimerConfiguration)`

Acquires Data from DAQ channel for measurement of digital edge count.

        Returns:
            DigitalEdgeCountMeasurementResultData:
            An instance of `DigitalEdgeCountMeasurementResultData` that specifies the data acquired from DAQ channels.
        

#### `def close(self)`

Closes the task and returns the hardware resources

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_frequency_measurements/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/digital_frequency_measurements/__init__.py

### MODULE DOCSTRING

Provides nipcbatt library digital frequency measurement modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_frequency_measurements/digital_frequency_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/digital_frequency_measurements/digital_frequency_constants.py

### MODULE DOCSTRING

Constant datatypes for use in digital frequency measurement

### `class ConstantsForDigitalFrequencyMeasurement()`

Constants used in digital frequency measurement

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_frequency_measurements/digital_frequency_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/digital_frequency_measurements/digital_frequency_data_types.py

### MODULE DOCSTRING

 Digital Frequency Measurement data types 

### `class DigitalFrequencyRangeParameters(PCBATestToolkitData)`

Defines the values used to establish the frequency range

#### `def __init__(self, frequency_minimum_value_hertz: float, frequency_maximum_value_hertz: float) -> None`

Initializes an instance of 'DigitalFrequencyRangeParameters'
           with specific values

        Args:
            frequency_minimum_value_hertz (float):
                The minimum value in the frequency range
            frequency_maximum_vlaue_hertz (float):
                The maximum value in the frequency range

        Raises: ValueError when,
            1) The value of frequency_minimum_value_hertz is None or is <= 0
            2) The value of frequency_maximum_vlue_hertz is None or is <= 0
        

#### `def frequency_minimum_value_hertz(self) -> float`


        :type:'float': Gets the minimum frquency in the range
        

#### `def frequency_maximum_value_hertz(self) -> float`


        :type:'float': Gets the maximum frquency in the range
        

### `class DigitalFrequencyMeasurementCounterChannelParameters(PCBATestToolkitData)`

Defines the values for frequency counter channels

#### `def __init__(self, range_parameters: DigitalFrequencyRangeParameters, input_divisor_for_frequency_measurement: int, measurement_duration_seconds: float) -> None`

Initializes an instance of DigitalFrequencyMeasurementCounterChannelParameters

        Args:
            range_parameters (DigitalFrequencyRangeParameters): frequency range used in
              measurement. Defined by min frequency and max frequency.
            input_divisor_for_frequency_measurement (float): Divisor used for measurements
            measurement_duration_seconds (float): Length of capture

        Raises: ValueError when,
            1) The value of frequency_minimum_value_hertz is None or <= 0
            2) The value of frequency_maximum_value_hertz is None or <= 0
            3) The value of input_divisor_for_frequency_measurement is None or <= 4
            4) The value of measurement_duration_seconds is None or <= 0
        

#### `def range_parameters(self) -> DigitalFrequencyRangeParameters`


        :type:'DigitalFrequencyRangeParameters': Holds the frequency range
        

#### `def input_divisor_for_frequency_measurement(self) -> int`


        :type:'int': The divisor used for measuring frequency
        

#### `def measurement_duration_seconds(self) -> float`


        :type:'float': The duration of the measurement in seconds
        

### `class DigitalFrequencyMeasurementConfiguration(PCBATestToolkitData)`

Defines the values used in the creation of a Digital Frequency Measurement

#### `def __init__(self, counter_channel_configuration_parameters: DigitalFrequencyMeasurementCounterChannelParameters) -> None`

Initializes an instance of 'DigitalFrequencyMeasurementConfiguration'
           with specific values

        Args:
            configuration_parameters: An instance of
            'DigitalFrequencyMeasurementCounterChannelParameters'

        Raises: ValueError when,
            1) The value of configuration_parameters is None
        

#### `def counter_channel_configuration_parameters(self) -> DigitalFrequencyMeasurementCounterChannelParameters`


        :type:'DigitalFrequencyMeasurementCounterChannelParameters': Holds the
        configuration parameters used for this measurement
        

### `class DigitalFrequencyMeasurementResultData()`

Defines the values inside a digital frequency result

#### `def __init__(self, frequency: float)`

Instantiates a DigitalFrequencyMeasurementResultData object
           with the value provided in the frequency argument

        Args:
            frequency (float): The measured digital frequency

        Raises:
            ValueError when the frequency is None or <= 0
        

#### `def frequency(self) -> float`


        :type:'float': The frequency captured in the measurement
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_frequency_measurements/digital_frequency_measurement.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/digital_frequency_measurements/digital_frequency_measurement.py

### MODULE DOCSTRING

Defines class used for digital frequency measurement

### `class DigitalFrequencyMeasurement(BuildingBlockUsingDAQmx)`

This class is used to perform digital frequency meausrements
    Args:
        BuildingBlockUsingDAQmx: Parent class for all modules
    

#### `def initialize(self, channel_expression: str, input_terminal_name: str)`

Creates a DigitalFrequencyMeasurement object with the
           given arguments

        Args:
            channel_expression (str): Channels to acquire
            input_terminal_name (str): Terminal to acquire
        

#### `def close(self)`

Ends measurement process and releases internal resources

#### `def configure_and_measure(self, configuration: DigitalFrequencyMeasurementConfiguration)`

Configures and/or performs a digital frequency measurement
           according to specific configuration parameters.

        Args:
            configuration (DigitalFrequencyMeasurementConfiguration): An instance of
            `DigitalFrequencyMeasurementConfiguration` used to configure the measurement.

        Returns:
            DigitalFrequencyMeasurementResultData: An instance of
            `DigitalFrequencyMeasurementResultData`or `None` if no measure was performed.
        

#### `def configure_counter_channel(self, parameters: DigitalFrequencyMeasurementCounterChannelParameters) -> None`

Configures a counter channel according to specific configuration parameters.

        Args:
        parameters (DigitalFrequencyMeasurementCounterChannelParameters): An instance of
            `DigitalFrequencyMeasurementCounterChannelParameters` used to configure the
             counter channel.
        

#### `def acquire_data_for_measurement_analysis(self) -> float`

Acquires Data from DAQ channel for measurement of digital frequency.

        Args: None

        Returns:
            float: A digital frequency measurement result
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_pulse_generations/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/digital_pulse_generations/__init__.py

### MODULE DOCSTRING

Provides nipcbatt library digital pulse generation modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_pulse_generations/digital_pulse_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/digital_pulse_generations/digital_pulse_constants.py

### MODULE DOCSTRING

Constants used in digital pulse generation

### `class ConstantsForDigitalPulseGeneration()`

Constants used in digital pulse generation

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_pulse_generations/digital_pulse_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/digital_pulse_generations/digital_pulse_data_types.py

### MODULE DOCSTRING

 Digital pulse data types 

### `class DigitalPulseGenerationCounterChannelParameters(PCBATestToolkitData)`

Defines the counter channel parameters used for digital pulse generation

#### `def __init__(self, pulse_idle_state: nidaqmx.constants.Level=ConstantsForDigitalPulseGeneration.DEFAULT_FREQUENCY_GENERATION_UNIT, low_time_seconds: float=0.01, high_time_seconds: float=0.01) -> None`

Creates an instance of DigitalPulseGenerationCounterChannelParameters

        Args:
            pulse_idle_state (Constant state): The intended idle state of the generation
            low_time_seconds (float): The intended duration of the low time of the pulse
            high_time_seconds (float): The intended duration of the high time of the pulse
        

#### `def pulse_idle_state(self) -> nidaqmx.constants.Level`


        :type:'nidaqmx.constants.Level': The idle state of the pulse generation
        

#### `def low_time_seconds(self) -> float`


        :type:float: The low time of the pulse
        

#### `def high_time_seconds(self) -> float`


        :type:float: The high time of the pulse
        

### `class DigitalPulseGenerationTimingParameters(PCBATestToolkitData)`

Defines the pulses count used in digital pulse generation

#### `def __init__(self, pulses_count: int) -> None`

Creates an instance of DigitalPulseGenerationTimingParameters

        Args: pulses_count (int): The number of pulses to generate
        

#### `def pulses_count(self) -> int`


        :type:int: Gets the number of pulses to generate
        

### `class DigitalPulseGenerationConfiguration(PCBATestToolkitData)`

Defines a configuration for digital pulse generation

#### `def __init__(self, counter_channel_parameters: DigitalPulseGenerationCounterChannelParameters, timing_parameters: DigitalPulseGenerationTimingParameters) -> None`

Creates an instance of DigitalPulseGenerationConfiguration

        Args:
            counter_channel_parameters:
                An valid instance of DigitalPulseGenerationCounterChannelParameters
            timing_parameters:
                An valid instance of DigitalPulseGenerationTimingParameters
        

#### `def counter_channel_parameters(self) -> DigitalPulseGenerationCounterChannelParameters`


        :type:DigitalPulseGenerationCounterChannelParameters: The instance of
            DigitalPulseGenerationCounterChannelParameters used for digital pulse generation
        

#### `def timing_parameters(self) -> DigitalPulseGenerationTimingParameters`


        :type:DigitalPulseGenerationTimingParameters: The instance of
            DigitalPulseGenerationTimingParameters used for digital pulse generation
        

### `class DigitalPulseGenerationData(PCBATestToolkitData)`

Returns the values actually written to the hardware

#### `def __init__(self, timebase_frequency_hertz: float, actual_pulse_train_duration_seconds: float, actual_pulse_low_time_seconds: float, actual_pulse_high_time_seconds: float) -> None`

Creates an instance of DigitalPulseGenerationData

#### `def timebase_frequency_hertz(self) -> float`


        :type:float: The timebase frequecy used to generate the pulse(s)
        

#### `def actual_pulse_train_duration_seconds(self) -> float`


        :type:float: The actual pulse train duration written to the hardware
        

#### `def actual_pulse_low_time_seconds(self) -> float`


        :type:float: The actual pulse low time written to the hardware
        

#### `def actual_pulse_high_time_seconds(self) -> float`


        :type:float: The actual pulse high time written to the hardware
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_pulse_generations/digital_pulse_generation.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/digital_pulse_generations/digital_pulse_generation.py

### MODULE DOCSTRING

Implementation of Digital Pulse Generation for TestScale and CompactDAQ

### `class DigitalPulseGeneration(BuildingBlockUsingDAQmx)`

Use this class for digital pulse generation

    Args:
        BuildingBlockUsingDAQmx (_type_): _description_
    

#### `def initialize(self, channel_expression: str, output_terminal_name: str) -> None`

_summary_

        Args:
            channel_expression (str): Physical channel
            output_terminal_name (str): Channel to write
        

#### `def configure_counter_channel(self, parameters: DigitalPulseGenerationCounterChannelParameters) -> None`

Configuration of the digital channel used for pulse generations

        Args:
            parameters (DigitalPulseGenerationCounterChannelParameters): A valid instance
                of DigitalPulseGenerationCounterChannelParameters
        

#### `def configure_timing(self, parameters: DigitalPulseGenerationTimingParameters) -> None`

Configuration of pulse generation timing

        Args:
            parameters (DigitalPulseGenerationTimingParameters): A valid instance
                of DigitalPulseGenerationTimingParameters
        

#### `def generate(self, parameters: DigitalPulseGenerationTimingParameters) -> DigitalPulseGenerationData`

Generate digital pulse(s)

        Returns:
            DigitalPulseGenerationData: A valid instance of DigitalPulseGenerationData
        

#### `def configure_and_generate(self, configuration: DigitalPulseGenerationConfiguration) -> DigitalPulseGenerationData`

Configuration of instruments and process to generation

        Args:
            configuration (DigitalPulseGenerationConfiguration): A valid instance
                of DigitalPulseGenerationConfiguration

        Returns:
            DigitalPulseGenerationData: The values written to hardware
        

#### `def close(self)`

Stops and closes the DAQ task

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_pwm_measurements/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/digital_pwm_measurements/__init__.py

### MODULE DOCSTRING

Provides nipcbatt library digital pwm measurement modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_pwm_measurements/digital_pwm_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/digital_pwm_measurements/digital_pwm_constants.py

### MODULE DOCSTRING

Constant datatypes for use in digital frequency measurement

### `class ConstantsForDigitalPwmMeasurement()`

Constants used in digital pwm measurement

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_pwm_measurements/digital_pwm_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/digital_pwm_measurements/digital_pwm_data_types.py

### MODULE DOCSTRING

 digital PWM data types 

### `class DigitalPwmMeasurementRangeParameters(PCBATestToolkitData)`

Defines the range between minimum and maximum pulse width

#### `def __init__(self, semi_period_minimum_value_seconds: float=2e-08, semi_period_maximum_value_seconds: float=42.949672) -> None`

Initializes an instance of 'DigitalPwmMeasurementRangeParameters'
           with the values provided in the arguments

        Args:
            semi_period_minimum_value_seconds (float):
                Minimum length of pwm semi-period
            semi_period_maximum_value_seconds (float):
                Maximum length of pwm semi-period

        Raises: ValueError when,
            1) The value of semi_period_minimum_value_seconds is less than or equal to zero
            2) The value of semi_period_maximum_value_seconds is less than or eqaul to zero
            3) semi_period_maximum_value_seconds < semi_period_minimum_value_seconds
        

#### `def semi_period_minimum_value_seconds(self) -> float`


        :type:'float': Gets the minimum semi period value in seconds
        

#### `def semi_period_maximum_value_seconds(self) -> float`


        :type:'float': Gets the minimum semi period value in seconds
        

### `class DigitalPwmMeasurementTimingParameters(PCBATestToolkitData)`

Defines the desired number of cycles to capture

#### `def __init__(self, semi_period_counter_wanted_cycles_count: int=2) -> None`

Initializes an instance of 'DigitalPwmMeasurementTimingParameters'
           with the values provided in the arguments

        Args:
            semi_period_counter_wanted_cycles_count(int):
                The desired number of cycles to capture

        Raises: ValueError when,
            1) The value of semi_period_counter_wanted_cycles_count is less than zero
            2) The value of semi_period_maximum_value_seconds is more than 2147483647
            3) The value of semi_period_counter_wanted_cycles_count does not exist (null)
        

#### `def semi_period_counter_wanted_cycles_count(self) -> int`


        :type:'int': Gets the desired number of cycles to capture
        

### `class DigitalPwmMeasurementCounterChannelParameters(PCBATestToolkitData)`

Holds all of the parameters for creating a PWM measurement

#### `def __init__(self, range_parameters: DigitalPwmMeasurementRangeParameters, timing_parameters: DigitalPwmMeasurementTimingParameters, semi_period_counter_starting_edge: nidaqmx.constants.Edge=ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE) -> None`

Initializes an instance of 'DigitalPwmMeasurementCounterChannelParameters'
           with the values provided in the arguments

        Args:
            range_parameters(DigitalPwmMeasurementRangeParameters):
                An instance of DigitalPwmMeasurementRangeParameters
            timing_parameters(DigitalPwmMeasurementTimingParameters):
                An instance of DigitalPwmMeasurementTimingParameters
            semi_period_counter_starting_edge:
                Constant value representing the starting edge

        Raises: ValueError when,
            1) The value of range_parameters is None
            2) The value of timing_parameters is None
            3) The value of semi_period_counter_starting_edge is None

#### `def range_parameters(self) -> DigitalPwmMeasurementRangeParameters`


        :type:DigitalPwmMeasurementRangeParamters: The range parameters of the measurement
        

#### `def timing_parameters(self) -> DigitalPwmMeasurementTimingParameters`


        :type:DigitalPwmMeasurementTimingParameters: The timing parameters of the measurement
        

#### `def semi_period_counter_starting_edge(self) -> int`


        :type:Constant int:The starting edge for the measurement
        

### `class DigitalPwmMeasurementConfiguration(PCBATestToolkitData)`

Defines values for the configuration of a digital pwm measurement

#### `def __init__(self, parameters: DigitalPwmMeasurementCounterChannelParameters, measurement_option: MeasurementExecutionType=MeasurementExecutionType.CONFIGURE_AND_MEASURE) -> None`

Creates an instance of DigitalPwmMeasurementConfiguration

        Args:
            parameters (DigitalPwmMeasurementCounterChannelParameters):
                A valid instance of DigitalPwmMeasurementCounterChannelParameters
            measurement_options (MeasurementExecutionType):
                A valid instance of MeasurementExecutionType
        

#### `def parameters(self) -> DigitalPwmMeasurementCounterChannelParameters`


        :type:DigitalPwmMeasurementCounterChannelParameters: Contains data
        range and timing parameters
        

#### `def measurement_option(self) -> MeasurementExecutionType`


        :type:MeasurmentExecutionType: Contains the type of execution
        

### `class DigitalPwmMeasurementData(PCBATestToolkitData)`

Defines the values returned from the capture

#### `def __init__(self, data: np.ndarray) -> None`

Initializes an instance of 'DigitalPwmMeasurementData'
        with specific values

        Args:
            data: Numpy ndarray

        Raises: ValueError when,
            1) data is empty
            2) data is None
        

#### `def data(self) -> np.ndarray`


        :type:'numpy.ndarray': Data captured from the measurement
        

### `class DigitalPwmMeasurementResultData(PCBATestToolkitData)`

Defines the values returned by a digital PWM measurement

#### `def __init__(self, actual_cycles_count: int, duty_cycle: float, period_duration: float, frequency: float, high_state_duration: float, low_state_duration: float) -> None`

Initializes an instance of 'DigitalPwmMeasurementResultData'
           with specific values

        Args:
            actual_cycles_count (int):
                The actual number of cycles measured
            duty_cycle (float):
                The measured duty cycle within the pwm measurement
            period_duration(float):
                The length of each period
            frequency(float):
                The measured frequency
            high_state_duration(float):
                The length of the high state
            low_state_duration(float):
                The length of the low state

        Raises: ValueError when,
            1) The value of actual_cycles_count is None or is < 0
            2) The value of duty_cycle is None or is < 0
            3) The value of period duration is None or is < 0
            4) The value of frequency is None or is < 0
            5) The value of high_state_duration is None or is < 0
            6) THe value of low_state_duration is None or is < 0
        

#### `def actual_cycles_count(self) -> int`


        :type:'int': Gets the number of cycles
        

#### `def duty_cycle(self) -> float`


        :type:'float': Gets the measured duty cycle
        

#### `def period_duration(self) -> float`


        :type:'float': Gets the length of the period
        

#### `def frequency(self) -> float`


        :type:'float': Gets the measured frequency
        

#### `def high_state_duration(self) -> float`


        :type:'float': Gets the length of the high state
        

#### `def low_state_duration(self) -> float`


        :type:'float': Gets the length of the low state
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_pwm_measurements/digital_pwm_measurement.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/digital_pwm_measurements/digital_pwm_measurement.py

### MODULE DOCSTRING

Use this class for digital pulse width modulation measurement

### `class DigitalPwmMeasurement(BuildingBlockUsingDAQmx)`

Class for performing a digital pulse width modulation measurement

    Args:
        BuildingBlockUsingDAQmx (_type_): Parent class for all PCBATT classes
    

#### `def initialize(self, channel_expression: str, input_terminal_name: str) -> None`

Creates an instance of the DigitalPwmMeasurement class

        Args:
            channel_expression (str): The physical channel being measured
            input_terminal_name (str): The name of the paticular input terminal
        

#### `def configure_counter_channel(self, parameters: DigitalPwmMeasurementCounterChannelParameters) -> None`

This method uses the semi_period values within the
            DigitalPwmMeasurementCounterChannelParameters argument provided to set
            the configuration for the counter channel

        Args:
            parameters (DigitalPwmMeasurementCounterChannelParameters):
                An instance of DigitalPwmMeasurementCounterChannelParameters
                with correct values
        

#### `def configure_timing(self, parameters: DigitalPwmMeasurementTimingParameters) -> None`

This method uses the cycles count within the DigitalPwmMeasurementTimingParameters
            argument to set the value in the task

        Args:
            parameters (DigitalPwmMeasurementTimingParameters):
                An instance of DigitalPwmMeasurementTimingParameters containing
                a valid value for semi_period_wounter_wanted_cycles_count
        

#### `def acquire_data_for_measurement_analysis(self) -> DigitalPwmMeasurementData`

Acquires data from the hardware and prepares it for analysis

        Returns:
            DigitalPwmMeasurementData: Numpy array of data to be processed

#### `def analyze_measurement_data(self, measurement_data: DigitalPwmMeasurementData) -> DigitalPwmMeasurementResultData`

This method analyzes the input data and prepares a
           DigitalPwmMeasurementResultData object which contains
           all of the measurements of interest

        Args:
            measurement_data (DigitalPwmMeasurementData): An instance of
            DigitalPwmMeasurementData with valid data

        Returns:
            DigitalPwmMeasurementResultData: Contains the data of interest
            from the PWM measurement
        

#### `def configure_and_measure(self, configuration: DigitalPwmMeasurementConfiguration) -> DigitalPwmMeasurementResultData`

Main method to create and execute a digital pwm measurement

        Args:
            configuration (DigitalPwmMeasurementConfiguration): An instance
            of DigitalPwmMeasurementConfiguration

        Returns:
            DigitalPwmMeasurementResultData:
        

#### `def close(self)`

_summary_

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_generations/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_generations/__init__.py

### MODULE DOCSTRING

Provides nipcbatt library dynamic digital pattern generation modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_generations/dynamic_digital_pattern_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_generations/dynamic_digital_pattern_constants.py

### MODULE DOCSTRING

Constants used in dynamic digital pattern generation

### `class ConstantsForDynamicDigitalPatternGeneration()`

Constants used for dynamic digital pattern generation

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_generations/dynamic_digital_pattern_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_generations/dynamic_digital_pattern_data_types.py

### MODULE DOCSTRING

 Dynamic digital pattern data types 

### `class DynamicDigitalStartTriggerParameters(PCBATestToolkitData)`

Defines parameters for dynamic digital pattern trigger start

#### `def __init__(self, digital_start_trigger_source: str, digital_start_trigger_edge: nidaqmx.constants.Edge=ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE, trigger_type: nidaqmx.constants.TriggerType=ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_TYPE) -> None`

Creates an instance of DynamicDigitalStartTriggerParameters

        Args:
            digital_start_trigger_source (str): The phyiscal line to obtain the trigger
            digital_start_trigger_edge (nidaqmx.constants.Edge, optional): The edge on which to trigger.
                Defaults to ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE.
            trigger_type (nidaqmx.constants.TriggerType, optional): The type of trigger being used.
                Defaults to ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_TYPE.
        

#### `def digital_start_trigger_source(self) -> str`


        :type:str: The source of the digital start trigger
        

#### `def digital_start_trigger_edge(self) -> nidaqmx.constants.Edge`


        :type:nidaqmx.constants.Edge: The edge on which to trigger
        

#### `def trigger_type(self) -> nidaqmx.constants.TriggerType`


        :type:nidaqmx.constants.TriggerType: The type of trigger used
        

### `class DynamicDigitalPatternGenerationData(PCBATestToolkitData)`

Contains the data returned from dynamic digital pattern generation

#### `def __init__(self, generation_time_seconds: float) -> None`

Creates an instance of DynamicDigitalPatternGenerationData

        Args:
            generation_time_seconds (float): The length of the generation time in seconds
        

#### `def generation_time_seconds(self) -> float`


        :type:float: The length of the generation time in seconds
        

### `class DynamicDigitalPatternGenerationConfiguration(PCBATestToolkitData)`

Contains the parameters for configuration of digital pattern generation

#### `def __init__(self, timing_parameters: DynamicDigitalPatternTimingParameters, digital_start_trigger_parameters: DynamicDigitalStartTriggerParameters, pulse_signal: np.ndarray) -> None`

Creates an instance of DynamicDigitalPatternGenerationConfiguration

        Args:
            timing_parameters (DynamicDigitalPatternTimingParameters): A valid instance
                of DynamicDigitalPatternTimingParameters
            digital_start_trigger_parameters (DynamicDigitalStartTriggerParameters): A
                valid instance of DynamicDigitalStartTriggerParameters
        

#### `def timing_parameters(self) -> DynamicDigitalPatternTimingParameters`


        :type:DynamicDigitalPatternTimingParameters
        

#### `def digital_start_trigger_parameters(self) -> DynamicDigitalStartTriggerParameters`


        :type: DynamicDigitalStartTriggerParameters
        

#### `def pulse_signal(self) -> np.ndarray`


        :type: Numpy array
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_generations/dynamic_digital_pattern_generation.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_generations/dynamic_digital_pattern_generation.py

### MODULE DOCSTRING

 _summary_ 

### `class DynamicDigitalPatternGeneration(SynchronizationSignalRouting)`

Use this class to generate dynamic digital patterns

#### `def initialize(self, channel_expression: str)`

Initializes a dynamic digital pattern generation sequence

        Args:
            channel_expression (str): The channel to generate on
        

#### `def configure_timing(self, parameters: DynamicDigitalPatternTimingParameters) -> None`

This method configures the timing of the generation

        Args:
            parameters (DynamicDigitalPatternTimingParameters): A valid instance
                of DynamicDigitalPatternTimingParameters
        

#### `def configure_trigger(self, parameters: DynamicDigitalStartTriggerParameters) -> None`

This method configures the trigger of the generation

        Args:
            parameters (DynamicDigitalStartTriggerParameters): A valid instance of
                DynamicDigitalStartTriggerParameters
        

#### `def generate(self, pulse_signal: np.ndarray) -> float`

Generates the dynamic digital pattern

        Args:
            pulse_signal (np.ndarray): Numpy array of (shape=(number_of_channels), dtype=numpy.uint32)

        Returns:
            float: The total generation time
        

#### `def configure_and_generate(self, configuration: DynamicDigitalPatternGenerationConfiguration) -> DynamicDigitalPatternGenerationData`

_summary_

        Args:
            configuration (DynamicDigitalPatternGenerationConfiguration): An
                instance of DynamicDigitalPatternGenerationConfiguration

        Returns:
            An instance of DynamicDigitalPatternGenerationData
        

#### `def close(self)`

_summary_

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_measurements/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_measurements/__init__.py

### MODULE DOCSTRING

Provides nipcbatt library dynamic digital pattern measurement modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_measurements/dynamic_digital_pattern_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_measurements/dynamic_digital_pattern_constants.py

### MODULE DOCSTRING

Constants used in dynamic digital pattern measurement

### `class ConstantsForDynamicDigitalPatternMeasurement()`

Constants used in dynamic didgital pattern measurement

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_measurements/dynamic_digital_pattern_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_measurements/dynamic_digital_pattern_data_types.py

### MODULE DOCSTRING

 Dynamic digital pattern data types 

### `class DynamicDigitalPatternMeasurementConfiguration(PCBATestToolkitData)`

Defines a configuration for dynamic digital pattern measurement

#### `def __init__(self, measurement_options: MeasurementOptions, timing_parameters: DynamicDigitalPatternTimingParameters, trigger_parameters: DigitalStartTriggerParameters) -> None`

Initializes an instance of
        `DynamicDigitalPatternMeasurementConfiguration`.

        Args:
            measurement_options (MeasurementOptions):
                The type of measurement options selected by user.
            timing_parameters (DynamicDigitalPatternTimingParameters):
                An instance of `DynamicDigitalPatternTimingParameters` that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters` that represents the settings of triggers.

        Raises:
            ValueError:
                'measurement_options' is None,
                `timing_parameters` is None,
                `trigger_parameters` is None,
        

#### `def measurement_options(self) -> MeasurementOptions`


        :class:`MeasurementExecutionType`:
            Gets the type of measurement execution selected by user.
        

#### `def timing_parameters(self) -> DynamicDigitalPatternTimingParameters`


        :class:`DynamicDigitalPatternTimingParameters`:
            Gets a `DynamicDigitalPatternTimingParameters` instance
            that represents the settings of timing.
        

#### `def trigger_parameters(self) -> DigitalStartTriggerParameters`


        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        

### `class DynamicDigitalPatternMeasurementResultData(PCBATestToolkitData)`

Defines the values returned from the capture

#### `def __init__(self, daq_digital_waveform_from_port: np.ndarray, waveforms: np.ndarray) -> None`

Initializes an instance of 'DynamicDigitalPatternMeasurementData'
        with specific values

        Args:
            daq_digital_waveform_from_port: Numpy ndarray
            waveforms: Numpy ndarray

        Raises: ValueError when,
            1) daq_digital_waveform_from_port is empty
            2) daq_digital_waveform_from_port is None
            3) waveforms is empty
            4) waveforms is none
        

#### `def daq_digital_waveform_from_port(self) -> np.ndarray`


        :type:'numpy.ndarray': Data captured from the measurement
        

#### `def waveforms(self) -> np.ndarray`


        :type:'numpy.ndarray': Data captured from the measurement
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_measurements/dynamic_digital_pattern_measurement.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_measurements/dynamic_digital_pattern_measurement.py

### MODULE DOCSTRING

Use this class to measure dynamic digital pattern from a system

### `class DynamicDigitalPatternMeasurement(BuildingBlockUsingDAQmx)`

class for performing dynamic digital pattern measurement

    Args:
        BuildingBlockUsingDAQmx (_type_): Parent class for all PCBATT classes
    

#### `def initialize(self, channel_expression: str) -> None`

Creates an instance of DynamicDigitalPatternMeasurement class

        Args:
            channel_expression (str): The name of the lines/port where the data will be measured
        

#### `def close(self)`

Closes the task and returns the hardware resources

#### `def configure_and_measure(self, configuration: DynamicDigitalPatternMeasurementConfiguration) -> Union[None, DynamicDigitalPatternMeasurementResultData]`

Configures and/or performs a measurement
           according to specific configuration parameters.

        Args:
            configuration (DynamicDigitalPatternMeasurementConfiguration):
            A instance of `DynamicDigitalPatternMeasurementConfiguration` used to configure the measurement.

        Returns:
            DynamicDigitalPatternMeasurementResultData | None: An instance of `DynamicDigitalPatternMeasurementResultData`
            or `None` if no measure was performed.
        

#### `def configure_timing(self, parameters: DynamicDigitalPatternTimingParameters)`

Configures the timing parameters for dynamic digital pattern measurement.

        Args:
            parameters (DynamicDigitalPatternTimingParameters):
            An instance of `DynamicDigitalPatternTimingParameters` used to configure the timing.
        

#### `def configure_trigger(self, parameters: DigitalStartTriggerParameters)`

Configure the characteristics of triggers used for dynamic digital pattern measurements.

        Args:
            parameters (DigitalStartTriggerParameters):
            An instance of `DigitalStartTriggerParameters` used to configure the channels.
        

#### `def acquire_data_for_measurement_analysis(self)`

Acquires Data from DAQ channel for measurement of dynamic digital pattern

        Returns:
            MeasurementData:
            An instance of `MeasurementData` that specifies the data acquired from DAQ channels.
        

#### `def analyze_measurement_data(self, measurement_data: MeasurementData) -> DynamicDigitalPatternMeasurementResultData`

Proceeds to the analysis of Digital port data from the measurement.

        Args:
            measurement_data (MeasurementData):
            An instance of `MeasurementData`
            that specifies the data acquired from DAQ channels.

        Returns:
            DynamicDigitalPatternMeasurementResultData:
            An instance of `DynamicDigitalPatternMeasurementResultData`
            that specifies the measurement results.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/frequency_domain_measurements/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/frequency_domain_measurements/__init__.py

### MODULE DOCSTRING

Provides nipcbatt library frequency domain measurement modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/frequency_domain_measurements/frequency_domain_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/frequency_domain_measurements/frequency_domain_constants.py

### MODULE DOCSTRING

 Constants data types for Frequency domain Measurements.

### `class ConstantsForFrequencyDomainMeasurement()`

Constants used for Frequency Domain measurement

- `DEFAULT_FREQUENCY_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS = VoltageRangeAndTerminalParameters(terminal_configuration=ConstantsForVoltageMeasurement.DEFAULT_AI_TERMINAL_CONFIGURATION, range_min_volts=ConstantsForVoltageMeasurement.DEFAULT_VOLTAGE_MINIMUM_VALUE_VOLTS, range_max_volts=ConstantsForVoltageMeasurement.DEFAULT_VOLTAGE_MAXIMUM_VALUE_VOLTS)`

- `DEFAULT_FREQUENCY_DOMAIN_MEASUREMENT_OPTIONS = MeasurementOptions(execution_option=ConstantsForVoltageMeasurement.DEFAULT_EXECUTION_TYPE, measurement_analysis_requirement=ConstantsForVoltageMeasurement.DEFAULT_MEASUREMENT_ANALYSIS_REQUIREMENT)`

- `DEFAULT_FREQUENCY_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS = SampleClockTimingParameters(sample_clock_source=ConstantsForVoltageMeasurement.DEFAULT_SAMPLE_CLOCK_SOURCE, sampling_rate_hertz=ConstantsForVoltageMeasurement.DEFAULT_SAMPLING_RATE_HERTZ, number_of_samples_per_channel=ConstantsForVoltageMeasurement.DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL, sample_timing_engine=ConstantsForVoltageMeasurement.DEFAULT_SAMPLE_TIMING_ENGINE)`

- `DEFAULT_FREQUENCY_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS = DigitalStartTriggerParameters(trigger_select=ConstantsForVoltageMeasurement.DEFAULT_TRIGGER_TYPE, digital_start_trigger_source=ConstantsForVoltageMeasurement.DEFAULT_DIGITAL_START_TRIGGER_SOURCE, digital_start_trigger_edge=ConstantsForVoltageMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE)`

- `DEFAULT_FREQUENCY_DOMAIN_MEASUREMENT_CONFIGURATION = FrequencyDomainMeasurementConfiguration(global_channel_parameters=DEFAULT_FREQUENCY_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS, specific_channels_parameters=[], measurement_options=DEFAULT_FREQUENCY_DOMAIN_MEASUREMENT_OPTIONS, sample_clock_timing_parameters=DEFAULT_FREQUENCY_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS, digital_start_trigger_parameters=DEFAULT_FREQUENCY_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS)`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/frequency_domain_measurements/frequency_domain_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/frequency_domain_measurements/frequency_domain_data_types.py

### MODULE DOCSTRING

 Frequency domain data types 

### `class FrequencyDomainMeasurementConfiguration(PCBATestToolkitData)`

Defines parameters used for configuration of Time domain measurement.

#### `def __init__(self, global_channel_parameters: VoltageRangeAndTerminalParameters, specific_channels_parameters: List[VoltageMeasurementChannelAndTerminalRangeParameters], measurement_options: MeasurementOptions, sample_clock_timing_parameters: SampleClockTimingParameters, digital_start_trigger_parameters: DigitalStartTriggerParameters) -> None`

Initializes an instance of
        `FrequencyDomainMeasurementConfiguration` with specific values.

        Args:
            global_channel_parameters (VoltageRangeAndTerminalParameters):
                The settings of terminal for all channels.
            specific_channels_parameters (List[VoltageMeasurementChannelAndTerminalRangeParameters]):
                The list of instances of `VoltageMeasurementChannelAndTerminalRangeParameters` used to configure channels.
            measurement_options (MeasurementOptions):
                An instance of `MeasurementOptions` that represents the settings of options used for execution.
            sample_clock_timing_parameters (SampleClockTimingParameters):
                An instance of `SampleClockTimingParameters` that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters` that represents the settings of triggers.

        Raises:
            TypeError:
                Raised when `specific_channels_parameters`
                contains objects that are not type of VoltageMeasurementChannelAndTerminalRangeParameters.
            ValueError:
                Raised when `global_channel_parameters` is None,
                `specific_channels_parameters` is None,
                `measurement_options` is None,
                `sample_clock_timing_parameters` is None,
                `digital_start_trigger_parameters` is None,
        

#### `def global_channel_parameters(self) -> VoltageRangeAndTerminalParameters`


        :class:`VoltageRangeAndTerminalParameters`:
            Gets the settings of terminal for all channels.

#### `def specific_channels_parameters(self) -> List[VoltageMeasurementChannelAndTerminalRangeParameters]`


        :class:`List[VoltageMeasurementChannelAndTerminalRangeParameters]`:
            Gets the list of instances of
            `VoltageMeasurementChannelAndTerminalRangeParameters` used to configure channels.
        

#### `def measurement_options(self) -> MeasurementOptions`


        :class:`MeasurementOptions`:
            Gets a `MeasurementOptions` instance
            that represents the settings of options used for execution.
        

#### `def sample_clock_timing_parameters(self) -> SampleClockTimingParameters`


        :class:`SampleClockTimingParameters`:
            Gets a `SampleClockTimingParameters` instance
            that represents the settings of timing.
        

#### `def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters`


        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        

### `class MultipleTonesMeasurementResultData(PCBATestToolkitData)`

Defines multiple tones measurement results obtained after waveform analysis.

#### `def __init__(self, tones_frequencies_hertz: List[float], tones_amplitudes_volts: List[float]) -> None`

Initializes an instance of "MultipleTonesMeasurementResultData" with specific values.

        Args:
            tones_frequencies_hertz (List[float]):
                A list of frequencies of detected tones for all analyzed waveforms.
            tones_amplitudes_volts (List[float]):
                A list of voltage peak amplitudes of detected tones for all analyzed waveforms.

        Raises:
            TypeError: Raised when,
                `tones_frequencies_hertz` containes objects that are not `float',
                `tones_amplitudes_volts` contains objects that are not `float'.

            ValueError: Raised when,
                `tones_frequencies_hertz` is None,
                `tones_amplitudes_volts` is None,
                `tones_frequencies_hertz` and `tones_amplitudes_volts` lists have different lengths.
        

#### `def tones_frequencies_hertz(self) -> List[float]`


        :class:`List[float]`:
        Gets a List containing detected tones frequencies of all analyzed waveform.
        

#### `def tones_amplitudes_volts(self) -> List[float]`


        :class:`List[float]`:
        Gets a list containing detected tones peak amplitudes of all analyzed waveform.
        

### `class FrequencyDomainMeasurementResultData(PCBATestToolkitData)`

Defines frequency domain measurement results obtained after waveform analysis.

#### `def __init__(self, waveforms: List[AnalogWaveform], magnitude_rms: List[AmplitudeSpectrum], magnitude_peak: List[AmplitudeSpectrum], detected_tones: List[MultipleTonesMeasurementResultData]) -> None`

Initializes an instance of "FrequencyDomainMeasurementResultData" with specific values.

        Args:
            waveforms (List[AnalogWaveform]):
                A list of `AnalogWaveform` acquired from channels defined for measurement.
            magnitude_rms (List[AmplitudeSpectrum]):
                A list of `AmplitudeSpectrum` representing the frequency domain measurement RMS computed on all channels.
            magnitude_peak (List[AmplitudeSpectrum]):
                A list of `AmplitudeSpectrum` representing the frequency domain measurement Peak to Peak computed on all channels.
            detected_tones (List[MultipleTonesMeasurementResultData]):
                A list of `MultipleTonesMeasurementResultData` representing the detected tones in the waveform.

        Raises:
            TypeError: Raised when,
                `waveforms` contains objects that are not `AnalogWaveform`,
                `magnitude_rms' contains objects that are not 'AmplitudeSpectrum`,
                `magnitude_peak` contains objects that are not 'AmplitudeSpectrum`,
                `detected_tones` contains objects that are not `MultipleTonesMeasurementResultData`

            ValueError: Raised when,
                `waveforms` is None or empty.
        

#### `def waveforms(self) -> List[AnalogWaveform]`


        :class:`List[AnalogWaveform]`:
            Gets the list of waveforms acquired from channels defined
            for measurement and used to compute frequency domain results.
        

#### `def magnitude_rms(self) -> List[AmplitudeSpectrum]`


        :calss: List[AmplitudeSpectrum]:
            Gets an array of RMS based spectrums computed for each channel waveform in `waveforms`.
        

#### `def magnitude_peak(self) -> List[AmplitudeSpectrum]`


        :calss: List[AmplitudeSpectrum]:
            Gets an array of Peak to Peak based spectrums computed for each channel waveform in `waveforms`.
        

#### `def detected_tones(self) -> List[MultipleTonesMeasurementResultData]`


        :calss: List[MultipleTonesMeasurementResultData]:
            Gets an array of multiple tones analysis results for each waveform contained in `waveforms`.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/frequency_domain_measurements/frequency_domain_measurement.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/frequency_domain_measurements/frequency_domain_measurement.py

### MODULE DOCSTRING

  Defines class used for Frequency domain measurement on PCB points. 

### `class FrequencyDomainMeasurement(BuildingBlockUsingDAQmx)`

Defines a way that allows you to perform Frequency domain measurement on PCB points.

#### `def initialize(self, analog_input_channel_expression: str)`

Initializes the measurement with the specific channels

        Args:
            analog_input_channel_expression (str):
                Expression representing the name of a physical channel,
                or a global channel in DAQ System.
        

#### `def close(self)`

Closes measurement procedure and releases internal resources.

#### `def configure_and_measure(self, configuration: FrequencyDomainMeasurementConfiguration) -> Union[None, FrequencyDomainMeasurementResultData]`

Configures and/or performs a measurement
           according to specific configuration parameters.

        Args:
            configuration (FrequencyDomainMeasurementConfiguration): An instance of
            `FrequencyDomainMeasurementConfiguration` used to configure the measurement.

        Returns:
            FrequencyDomainMeasurementResultData | None:
                An instance of `FrequencyDomainMeasurementResultData`
                or `None` if no measure was performed.
        

#### `def configure_all_channels(self, parameters: VoltageRangeAndTerminalParameters)`

Configures all channels used for voltage measurements.

        Args:
            parameters (VoltageRangeAndTerminalParameters):
            An instance of `VoltageRangeAndTerminalParameters` used to configure the channels.
        

#### `def configure_specific_channel(self, parameters: VoltageMeasurementChannelAndTerminalRangeParameters)`

Configures the specific channels used for voltage measurements.

        Args:
            parameters (VoltageMeasurementChannelAndTerminalRangeParameters):
            An instance of `VoltageMeasurementChannelAndTerminalRangeParameters`
            used to configure the channels.

        If the user provides Global Virtual Channel name in Initialize(),
        then he/she has to provide the Virtual channel name in Specific channel parameters as well.

        Similarly, if the user provides Physical channel name in Initialize(),
        then he/she has to provide the Physical channel name in Specific channel parameters.
        

#### `def configure_timing(self, parameters: SampleClockTimingParameters)`

Configures the timing characteristics used for voltage measurements.

        Args:
            parameters (SampleClockTimingParameters):
            An instance of `SampleClockTimingParameters`
            used to configure the timing.
        

#### `def configure_trigger(self, parameters: DigitalStartTriggerParameters)`

Configure the characteristics of triggers used for voltage measurements.

        Args:
            parameters (DigitalStartTriggerParameters):
            An instance of `DigitalStartTriggerParameters`
            used to configure the channels.
        

#### `def acquire_data_for_measurement_analysis(self) -> MeasurementData`

Acquires Data from DAQ channel for measurement of voltage.

        Returns:
            MeasurementData: An instance of `MeasurementData`
            that specifies the data acquired from DAQ channels.
        

#### `def analyze_measurement_data(self, measurement_data: MeasurementData, measurement_analysis_requirement: MeasurementAnalysisRequirement) -> FrequencyDomainMeasurementResultData`

Proceeds to the analysis of Voltages from the measurement.

        Args:
            data (MeasurementData):
                An instance of `MeasurementData`
                that specifies the data acquired from DAQ channels.
            measurement_analysis_requirement (MeasurementAnalysisRequirement):
                An instance of 'MeasurementAnalysisRequirement' that specifies
                whether to Skip Analysis or Proceed to Analysis.

        Returns:
            FrequencyDomainMeasurementResultData:
            An instance of `FrequencyDomainMeasurementResultData`
            that specifies the measurement results.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/power_supply_source_and_measurements/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/power_supply_source_and_measurements/__init__.py

### MODULE DOCSTRING

Provides nipcbatt library power source and measurement modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/power_supply_source_and_measurements/power_supply_source_and_measure.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/power_supply_source_and_measurements/power_supply_source_and_measure.py

### MODULE DOCSTRING

Defines class used for power supply source and measurement of voltage, current and power.

### `class PowerSupplySourceAndMeasure(BuildingBlockUsingDAQmx)`

Defines a way that allows you to configure and perform power supply using a source and measure resulting voltage and current.

    Args:
        BuildingBlockUsingDAQmx (_type_): _description_
    

#### `def initialize(self, power_channel_name: str)`

Initializes the Power source and measurement with the specific channel

        Args:
            power_channel_name (str): Expression representing the name of a physical channel,
            or a global channel or the name of registered settings in DAQ System.
        

#### `def close(self)`

Closes the measurement process and releases the internal resources

#### `def configure_and_measure(self, configuration: PowerSupplySourceAndMeasureConfiguration) -> PowerSupplySourceAndMeasureResultData`


        Configures and/or performs a measurement according to specific configuration parameters.

        Args:
            configuration (PowerSupplySourceAndMeasureConfiguration):
            A instance of `PowerSupplySourceAndMeasureConfiguration`
            used to configure the measurement.

        Returns:
            _type_: An instance of `PowerSupplySourceAndMeasureResultData
            ` or `None` if no measure was performed.
        

#### `def configure_all_channels(self, parameters: PowerSupplySourceAndMeasureTerminalParameters)`

Configures all channels used for power supply source and measure measurements.

        Args:
            parameters (PowerSupplySourceAndMeasureTerminalParameters):
            An instance of `PowerSupplySourceAndMeasureTerminalParameters`
            used to configure the channels.
        

#### `def configure_timing(self, parameters: SampleClockTimingParameters)`

Configure the timing characteristics used for Power supply sourcing and measurement.

        Args:
            parameters (SampleClockTimingParameters):
            An instance of `SampleClockTimingParameters`
            used to configure the timing.
        

#### `def configure_trigger(self, parameters: DigitalStartTriggerParameters)`

Configure the characteristics of triggers used for Power supply sourcing and measurement.

        Args:
            parameters (DigitalStartTriggerParameters):
            An instance of `DigitalStartTriggerParameters`
            used to configure the channels.
        

#### `def acquire_data_for_measurement_analysis(self) -> PowerSupplySourceAndMeasureData`

Acquires the voltage and current data from the DAQ channel
        for measurement of Power supply.

        Returns:
            PowerSupplySourceAndMeasureData: An instance of `PowerSupplySourceAndMeasureData`
            that contains array of voltage and current samples acquired from DAQ channels.
        

#### `def analyze_measurement_data(self, measurement_data: PowerSupplySourceAndMeasureData, measurement_analysis_requirement: MeasurementAnalysisRequirement) -> PowerSupplySourceAndMeasureResultData`

Calls the analysis function for Power source and measure measurements.

        Args:
            data (PowerSupplySourceAndMeasureData):
                An instance of `PowerSupplySourceAndMeasureData`
                that specifies the voltage and current data acquired from DAQ channels.
            measurement_analysis_requirement (MeasurementAnalysisRequirement):
                An instance of 'MeasurementAnalysisRequirement' that specifies
                whether to Skip Analysis or Proceed to Analysis.

        Returns:
            PowerSupplySourceAndMeasureResultData:
                An instance of `PowerSupplySourceAndMeasureResultData`
                that specifies the measurement results.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/power_supply_source_and_measurements/power_supply_source_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/power_supply_source_and_measurements/power_supply_source_constants.py

### MODULE DOCSTRING

Constants for default values for Power Supply Source Measurements

### `class ConstantsForPowerSupplySourceMeasurement()`

Constants used for Power Supply measurements

- `DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_TERMINAL_PARAMETERS = PowerSupplySourceAndMeasureTerminalParameters(voltage_setpoint_volts=ConstantsForPowerSupplySourceMeasurement.DEFAULT_VOLTAGE_SETPOINT_VOLTS, current_setpoint_amperes=ConstantsForPowerSupplySourceMeasurement.DEFAULT_CURRENT_SETPOINT_AMPERES, power_sense=ConstantsForPowerSupplySourceMeasurement.DEFAULT_REMOTE_SENSE, idle_output_behaviour=ConstantsForPowerSupplySourceMeasurement.DEFAULT_IDLE_OUTPUT_BEHAVIOUR, enable_output=ConstantsForPowerSupplySourceMeasurement.DEFAULT_OUTPUT_ENABLE)`

- `DEFAULT_POWER_SUPPLY_MEASUREMENT_OPTIONS = MeasurementOptions(execution_option=ConstantsForPowerSupplySourceMeasurement.DEFAULT_EXECUTION_TYPE, measurement_analysis_requirement=ConstantsForPowerSupplySourceMeasurement.DEFAULT_MEASUREMENT_ANALYSIS_REQUIREMENT)`

- `DEFAULT_POWER_SUPPLY_SAMPLE_CLOCK_TIMING_PARAMETERS = SampleClockTimingParameters(sample_clock_source=ConstantsForPowerSupplySourceMeasurement.DEFAULT_SAMPLE_CLOCK_SOURCE, sampling_rate_hertz=ConstantsForPowerSupplySourceMeasurement.DEFAULT_SAMPLING_RATE_HERTZ, number_of_samples_per_channel=ConstantsForPowerSupplySourceMeasurement.DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL, sample_timing_engine=ConstantsForPowerSupplySourceMeasurement.DEFAULT_SAMPLE_TIMING_ENGINE)`

- `DEFAULT_POWER_SUPPLY_DIGITAL_START_TRIGGER_PARAMETERS = DigitalStartTriggerParameters(trigger_select=ConstantsForPowerSupplySourceMeasurement.DEFAULT_TRIGGER_TYPE, digital_start_trigger_source=ConstantsForPowerSupplySourceMeasurement.DEFAULT_DIGITAL_START_TRIGGER_SOURCE, digital_start_trigger_edge=ConstantsForPowerSupplySourceMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE)`

- `DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_CONFIGURATION = PowerSupplySourceAndMeasureConfiguration(terminal_parameters=DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_TERMINAL_PARAMETERS, measurement_options=DEFAULT_POWER_SUPPLY_MEASUREMENT_OPTIONS, sample_clock_timing_parameters=DEFAULT_POWER_SUPPLY_SAMPLE_CLOCK_TIMING_PARAMETERS, digital_start_trigger_parameters=DEFAULT_POWER_SUPPLY_DIGITAL_START_TRIGGER_PARAMETERS)`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/power_supply_source_and_measurements/power_supply_source_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/power_supply_source_and_measurements/power_supply_source_data_types.py

### MODULE DOCSTRING

 Power supply source data types 

### `class PowerSupplySourceAndMeasureTerminalParameters(PCBATestToolkitData)`

Defines parameters used for configuration of Power source and measurements

#### `def __init__(self, voltage_setpoint_volts: float, current_setpoint_amperes: float, power_sense: nidaqmx.constants.Sense, idle_output_behaviour: nidaqmx.constants.PowerIdleOutputBehavior, enable_output: bool) -> None`

Initializes an instance of `PowerSupplySourceAndMeasureTerminalParameters'
        with specific values

        Args:
            voltage_setpoint_volts (float):
                The constant output voltage, in volts, to be set for the terminal.
            current_setpoint_amperes (float):
                The constant output current, in amperes, to be set for the terminal.
            power_sense (nidaqmx.constants.Sense):
                Specifies whether to use local or remote sense to sense the output voltage.
            idle_output_behaviour (nidaqmx.constants.PowerIdleOutputBehavior):
                Specifies whether to disable the output or
                maintain the existing value after the task is uncommitted.
            enable_output (bool):
                Specifies whether to enable or disable power module output.
        

#### `def voltage_setpoint_volts(self) -> float`


        :type:`float`:Gets the output voltage setpoint in volts for the terminal
        

#### `def current_setpoint_amperes(self) -> float`


        :type:`float`:Gets the output current setpoint in amperes for the terminal
        

#### `def power_sense(self) -> nidaqmx.constants.Sense`


        :class:`nidaqmx.constants.Sense`:
            Gets the remote sense value configured for the power measurement
        

#### `def idle_output_behaviour(self) -> nidaqmx.constants.PowerIdleOutputBehavior`


        :class:`nidaqmx.constants.PowerIdleOutputBehavior`:
            Gets the idle output behaviour value configured for the power channels
        

#### `def enable_output(self) -> bool`


        :type:`bool`:Gets if the output is enabled or disabled
        

### `class PowerSupplySourceAndMeasureConfiguration(PCBATestToolkitData)`

Defines parameters used for configuration of Power measurements

#### `def __init__(self, terminal_parameters: PowerSupplySourceAndMeasureTerminalParameters, measurement_options: MeasurementOptions, sample_clock_timing_parameters: SampleClockTimingParameters, digital_start_trigger_parameters: DigitalStartTriggerParameters) -> None`

Initializes an instance of
        `PowerSupplySourceAndMeasureConfiguration` with specific values.

        Args:
            terminal_parameters (PowerSupplySourceAndMeasureTerminalParameters)
                The settings of terminal for all Power channels.
            measurement_options (MeasurementOptions):
                An instance of `MeasurementOptions` that represents
                the settings of options used for execution.
            sample_clock_timing_parameters (SampleClockTimingParameters):
                An instance of `SampleClockTimingParameters`
                that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters`
                that represents the settings of triggers.
        

#### `def terminal_parameters(self) -> PowerSupplySourceAndMeasureTerminalParameters`


        :class: `PowerSupplySourceAndMeasureTerminalParameters`:
            Gets the settings of Power terminal for all the channels.
        

#### `def measurement_options(self) -> MeasurementOptions`


        :class:`MeasurementOptions`:
            Gets a `MeasurementOptions` instance
            that represents the settings of options used for execution.
        

#### `def sample_clock_timing_parameters(self) -> SampleClockTimingParameters`


        :class:`SampleClockTimingParameters`:
            Gets a `SampleClockTimingParameters` instance
            that represents the settings of timing.
        

#### `def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters`


        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        

### `class PowerSupplySourceAndMeasureResultData(PCBATestToolkitData)`

Defines the result values computed after analysing
    voltage and current waveforms from Power Supply Source.

#### `def __init__(self, voltage_waveform: AnalogWaveform, current_waveform: AnalogWaveform, max_voltage_level_volts: float, max_current_level_amperes: float, max_power_level_watts: float, average_power_value_watts: float, acquisition_duration_seconds: float) -> None`

Constructor that initializes
        a new object of PowerSupplySourceAndMeasureResultData with specific values.

        Args:
            voltage_waveform (AnalogWaveform):
                A collection of samples representing the voltage values captured in the waveform.
            current_waveform (AnalogWaveform):
                A collection of samples representing the current values captured in the waveform.
            max_voltage_level_volts (float):
                The maximum voltage level value (in Volts).
            max_current_level_amperes (float):
                The maximum current level value (in Amperes).
            max_power_level_watts (float):
                The maximum power level value (in Watts).
            average_power_value_watts (float):
                The average power value (in Watts).
            acquisition_duration_seconds (float):
                The total acquisition time by the instrument in seconds.
        

#### `def voltage_waveform(self) -> AnalogWaveform`


        :class:`AnalogWaveform`:
            Gets the voltage waveforms acquired from channels defined
            for measurement and used to compute power measurements.
        

#### `def current_waveform(self) -> AnalogWaveform`


        :class:`AnalogWaveform`:
            Gets the current waveforms acquired from channels defined
            for measurement and used to compute power measurements.
        

#### `def max_voltage_level_volts(self) -> float`


        :type:`float`:
            Gets the maximum voltage level value (in Volts).
        

#### `def max_current_level_amperes(self) -> float`


        :type:`float`:
            Gets the maximum current level value (in Amperes).
        

#### `def max_power_level_watts(self) -> float`


        :type:`float`:
            Gets the maximum power level value (in Watts).
        

#### `def average_power_value_watts(self) -> float`


        :type:`float`:
            Gets the average power value (in Watts).
        

#### `def acquisition_duration_seconds(self) -> float`


        :type:`float`:
            Gets the duration of acquisition of samples for each of the power channel.
        

### `class PowerSupplySourceAndMeasureData(PCBATestToolkitData)`


    Defines the voltage and current waveform acquired from power channels.
    

#### `def __init__(self, source_name: str, voltage_samples: numpy.ndarray, current_samples: numpy.ndarray, sampling_rate_hertz: int)`

Initializes an instance of `PowerSupplySourceAndMeasureData`
           with specific values.

        Args:
            source_name (str): The name of channel on which waveform was captured.
            voltage_samples (numpy.ndarray): A collection of samples
            representing the voltage values captured in the waveform.
            Note: argument cannot be None or an empty array.

            current_samples (numpy.ndarray): A collection of samples
            representing the current values captured in the waveform.
            Note: argument cannot be None or an empty array.

            sampling_rate_hertz (int): The sampling rate (in Hz).
            Note: argument cannot be None or zero.

            voltage_samples, current_samples, and sampling_rate_hertz ca
        

#### `def source_name(self) -> str`


        :type:`str`: Gets the name of channel on which waveform was captured.
        

#### `def voltage_samples(self) -> numpy.ndarray`


        :class:`numpy.ndarray`:
            Gets the array of samples from the voltage waveform.
        

#### `def current_samples(self) -> numpy.ndarray`


        :class:`numpy.ndarray`:
            Gets the array of samples from the current waveform.
        

#### `def sampling_rate_hertz(self) -> int`

Gets the sampling rate (in Hz).

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/signal_voltage_generations/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/signal_voltage_generations/__init__.py

### MODULE DOCSTRING

Provides nipcbatt library signal voltage generation modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/signal_voltage_generations/signal_voltage_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/signal_voltage_generations/signal_voltage_data_types.py

### MODULE DOCSTRING

 Signal Voltage Generation data types 

### `class ToneParameters(PCBATestToolkitData)`

Defines the settings of a tone used to generate a signal.

#### `def __init__(self, tone_frequency_hertz: float, tone_amplitude_volts: float, tone_phase_radians: float) -> None`

Initializes an instance of `ToneParameters` with specific values.

        Args:
            tone_frequency_hertz (float):
                The frequency value of the tone, in Hertz
            tone_amplitude_volts (float):
                The amplitude value of the tone, in Volts
            tone_phase_radians (float):
                The phase value of the tone, in Radians
        

#### `def tone_frequency_hertz(self) -> float`

Gets the frequency value of the tone, in Hertz.

#### `def tone_amplitude_volts(self) -> float`

Gets the amplitude value of the tone, in Volts

#### `def tone_phase_radians(self) -> float`

Gets the phase value of the tone, in Radians.

### `class SignalVoltageGenerationTimingParameters(PCBATestToolkitData)`

Defines the settings of sample clock timing for signal voltage generation.

#### `def __init__(self, sample_clock_source: str, sampling_rate_hertz: int, generated_signal_duration_seconds: float) -> None`

Used to initialize an instance of `SampleClockTimingParameters`.

        Args:
            sample_clock_source (str): The source of the clock.
            sampling_rate_hertz (int): The sampling rate (in Hz).
            generated_signal_duration_seconds (float):
                The duration in seconds for which the signal needs to be generated.

        Raises:
            ValueError:
                Raised if `sample_clock_source` is None or empty or white space,
                if `sampling_rate_hertz` is less than or equal to zero.
                If the `generated_signal_duration_seconds' is less than or equal to zero.
        

#### `def sample_clock_source(self) -> str`

Gets the source of the clock.

#### `def sampling_rate_hertz(self) -> int`

Gets the sampling rate (in Hz).

#### `def generated_signal_duration_seconds(self) -> float`

Gets the duration of the generated signal voltage.

### `class SignalVoltageGenerationSineWaveParameters(PCBATestToolkitData)`

Defines the parameters used to configure generation of sine wave signal voltage.

#### `def __init__(self, generated_signal_offset_volts: float, generated_signal_tone_parameters: ToneParameters) -> None`

Initializes an instance of `SignalVoltageGenerationSineWaveParameters` with specific values.

        Args:
            generated_signal_offset_volts (float):
                The offset of the generated signal voltage.
            generated_signal_tone_parameters (ToneParameters):
                The tone settings of the generated signal.

        Raises:
            ValueError:
                if the `generated_signal_tone_parameters' is None
        

#### `def generated_signal_offset_volts(self) -> float`

Gets the offset of the generated signal voltage.

#### `def generated_signal_tone_parameters(self) -> ToneParameters`

Gets the tone settings of the generated signal

### `class SignalVoltageGenerationSquareWaveParameters(PCBATestToolkitData)`

Defines the parameters used to configure generation of square wave signal voltage.

#### `def __init__(self, generated_signal_offset_volts: float, generated_signal_frequency_hertz: float, generated_signal_amplitude_volts: float, generated_signal_duty_cycle_percent: float, generated_signal_phase_radians: float) -> None`

Initializes an instance of `SignalVoltageGenerationSquareWaveParameters` with specific values.

        Args:
            generated_signal_offset_volts (float):
                The offset of the generated signal voltage in volts.
            generated_signal_frequency_hertz (float):
                The frequency value of the square wave, in Hertz
            generated_signal_amplitude_volts (float):
                The amplitude value of the square wave, in volts
            generated_signal_duty_cycle_percent (float):
                The duty cycle of the square wave, in percent.
            generated_signal_phase_radians(float):
                The phase value of the square wave, in radians

        Raises:
            ValueError:
                If the value of `generated_signal_frequency_hertz` is less than or equal to 0
                If the value of `generated_signal_amplitude_volts` is less than or equal to 0
                If the value of `generated_signal_duty_cycle_percent` is not between 0 and 100
        

#### `def generated_signal_offset_volts(self) -> float`

Gets the offset of the generated signal voltage.

#### `def generated_signal_frequency_hertz(self) -> float`

Gets the frequency value of the square wave, in Hertz.

#### `def generated_signal_amplitude_volts(self) -> float`

Gets the amplitude value of the square wave, in Volts.

#### `def generated_signal_duty_cycle_percent(self) -> float`

Gets the duty cycle of the square wave, in percent.

#### `def generated_signal_phase_radians(self) -> float`

Gets the phase value of the square wave, in radians.

### `class SignalVoltageGenerationMultipleTonesWaveParameters(PCBATestToolkitData)`

Defines the parameters used to configure generation of (multi-tone)
    signal voltage with one or more sine waves (sum of sinusoid).

#### `def __init__(self, generated_signal_offset_volts: float, generated_signal_amplitude_volts: float, multiple_tones_parameters: List[ToneParameters]) -> None`

Initializes an instance of `SignalVoltageGenerationMultipleTonesWaveParameters`
         with specific values.

        Args:
            generated_signal_offset_volts (float):
                The offset of the generated signal voltage.
            generated_signal_amplitude_volts (float):
                The Amplitude value used to rescale the resulted sine wave.
            multiple_tones_parameters (List[ToneParameters]):
                The List of `ToneParameters` representing the settings of each
                 sine wave in generated signal voltage.

        Raises:
            ValueError:
                If the `generated_signal_amplitude_volts' is less than or equal to zero.
                if the `generated_signal_tone_parameters' is None or empty List
        

#### `def generated_signal_offset_volts(self) -> float`

Gets the offset of the generated signal voltage.

#### `def generated_signal_amplitude_volts(self) -> float`

Gets the Amplitude value used to rescale the resulted sine wave.

#### `def multiple_tones_parameters(self) -> List[ToneParameters]`

Gets the List `ToneSettings` representing the settings of
        each sine wave in generated signal voltage.

### `class SignalVoltageGenerationSineWaveConfiguration(PCBATestToolkitData)`

Defines the parameters used for configuration of sine wave signal generation

#### `def __init__(self, voltage_generation_range_parameters: VoltageGenerationChannelParameters, waveform_parameters: SignalVoltageGenerationSineWaveParameters, timing_parameters: SignalVoltageGenerationTimingParameters, digital_start_trigger_parameters: DigitalStartTriggerParameters) -> None`

Initializes an instance of
        `SignalVoltageGenerationSineWaveConfiguration` with specific values.

        Args:
            voltage_generation_range_parameters (VoltageGenerationChannelParameters):
                An instance of `VoltageGenerationChannelParameters' used to configure the channels.
            waveform_parameters (SignalVoltageGenerationSineWaveParameters):
                An instance of `SignalVoltageGenerationSineWaveParameters`
                used to configure the generation of sine wave signal voltage.
            timing_parameters (SignalVoltageGenerationTimingParameters):
                An instance of SignalVoltageGenerationTimingParameters that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters` that represents the settings of triggers.
        

#### `def voltage_generation_range_parameters(self) -> VoltageGenerationChannelParameters`


        :class:`VoltageGenerationChannelParameters`:
            Gets an instance of `VoltageGenerationChannelParameters'
            that represents the terminal settings for all channel for signal voltage generation.
        

#### `def waveform_parameters(self) -> SignalVoltageGenerationSineWaveParameters`


        :class:`SignalVoltageGenerationSineWaveParameters`:
            Gets an instance of `SignalVoltageGenerationSineWaveParameters`
            used to configure the generation of sine wave signal voltage.
        

#### `def timing_parameters(self) -> SignalVoltageGenerationTimingParameters`


        :class:`SignalVoltageGenerationTimingParameters`:
            Gets a `SignalVoltageGenerationTimingParameters` instance
            that represents the settings of timing.
        

#### `def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters`


        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        

### `class SignalVoltageGenerationSquareWaveConfiguration(PCBATestToolkitData)`

Defines the parameters used for configuration of square wave signal generation

#### `def __init__(self, voltage_generation_range_parameters: VoltageGenerationChannelParameters, waveform_parameters: SignalVoltageGenerationSquareWaveParameters, timing_parameters: SignalVoltageGenerationTimingParameters, digital_start_trigger_parameters: DigitalStartTriggerParameters) -> None`

Initializes an instance of
        `SignalVoltageGenerationSquareWaveConfiguration` with specific values.

        Args:
            voltage_generation_range_parameters (VoltageGenerationChannelParameters):
                An instance of `VoltageGenerationChannelParameters' used to configure the channels.
            waveform_parameters (SignalVoltageGenerationSquareWaveParameters):
                An instance of `SignalVoltageGenerationSquareWaveParameters`
                used to configure the generation of square wave signal voltage.
            timing_parameters (SignalVoltageGenerationTimingParameters):
                An instance of SignalVoltageGenerationTimingParameters that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters` that represents the settings of triggers.
        

#### `def voltage_generation_range_parameters(self) -> VoltageGenerationChannelParameters`


        :class:`VoltageGenerationChannelParameters`:
            Gets an instance of `VoltageGenerationChannelParameters'
            that represents the terminal settings for all channel for signal voltage generation.
        

#### `def waveform_parameters(self) -> SignalVoltageGenerationSquareWaveParameters`


        :class:`SignalVoltageGenerationSquareWaveParameters`:
            Gets an instance of `SignalVoltageGenerationSquareWaveParameters`
            used to configure the generation of square wave signal voltage.
        

#### `def timing_parameters(self) -> SignalVoltageGenerationTimingParameters`


        :class:`SignalVoltageGenerationTimingParameters`:
            Gets a `SignalVoltageGenerationTimingParameters` instance
            that represents the settings of timing.
        

#### `def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters`


        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        

### `class SignalVoltageGenerationMultipleTonesConfiguration(PCBATestToolkitData)`

Defines the parameters used for configuration of multi-tone sine wave signal generation

#### `def __init__(self, voltage_generation_range_parameters: VoltageGenerationChannelParameters, waveform_parameters: SignalVoltageGenerationMultipleTonesWaveParameters, timing_parameters: SignalVoltageGenerationTimingParameters, digital_start_trigger_parameters: DigitalStartTriggerParameters) -> None`

Initializes an instance of
        `SignalVoltageGenerationMultipleTonesConfiguration` with specific values.

        Args:
            voltage_generation_range_parameters (VoltageGenerationChannelParameters):
                An instance of `VoltageGenerationChannelParameters' used to configure the channels.
            waveform_parameters (SignalVoltageGenerationMultipleTonesWaveParameters):
                An instance of `SignalVoltageGenerationMultipleTonesWaveParameters`
                used to configure the generation of sine wave signal voltage.
            timing_parameters (SignalVoltageGenerationTimingParameters):
                An instance of `SignalVoltageGenerationTimingParameters` that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters` that represents the settings of triggers.
        

#### `def voltage_generation_range_parameters(self) -> VoltageGenerationChannelParameters`


        :class:`VoltageGenerationChannelParameters`:
            Gets an instance of `VoltageGenerationChannelParameters'
            that represents the terminal settings for all channel for signal voltage generation.
        

#### `def waveform_parameters(self) -> SignalVoltageGenerationMultipleTonesWaveParameters`


        :class:`SignalVoltageGenerationMultipleTonesWaveParameters`:
            Gets an instance of `SignalVoltageGenerationMultipleTonesWaveParameters`
            used to configure the generation of multi-tone sine wave signal voltage.
        

#### `def timing_parameters(self) -> SignalVoltageGenerationTimingParameters`


        :class:`SignalVoltageGenerationTimingParameters`:
            Gets a `SignalVoltageGenerationTimingParameters` instance
            that represents the settings of timing.
        

#### `def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters`


        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/signal_voltage_generations/signal_voltage_generation.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/signal_voltage_generations/signal_voltage_generation.py

### MODULE DOCSTRING

Defines class used for generation of signal voltage on PCB points.

### `class SignalVoltageGeneration(SynchronizationSignalRouting)`

Provides a way that allows you to generate signal voltage and apply it into PCB points.

#### `def initialize(self, channel_expression: str)`

Initializes the analog output channels and obtains
        the Daqmx Task for signal voltage generation.

        Args:
            channel_expression (str):
                Expression representing the name of an analog output physical channel,
                or a global channel in DAQ System.
        

#### `def configure_all_channels(self, parameters: VoltageGenerationChannelParameters) -> None`

Configures all analog output channels for Signal Voltage generation.

        Args:
            parameters (VoltageGenerationChannelParameters):
            An instance of `VoltageGenerationChannelParameters` used
            to configure the analog output channels.
        

#### `def configure_timing(self, parameters: SignalVoltageGenerationTimingParameters)`

Configures the timing characteristics used for Current measurements.

        Args:
            parameters (SampleClockTimingParameters): An instance of `SampleClockTimingParameters`
                used to configure the timing.
        

#### `def _get_generated_signal_samples_count(self, sampling_rate_hertz, generated_signal_duration_seconds) -> int`

Calculates the number of samples that will be in the generated signal

#### `def configure_trigger(self, parameters: DigitalStartTriggerParameters)`

Configure the characteristics of triggers used for Current measurements.

        Args:
            parameters (DigitalStartTriggerParameters):
            An instance of `DigitalStartTriggerParameters`
            used to configure the channels.
        

#### `def generate_voltage_sine_waveform(self, signal_parameters: SignalVoltageGenerationSineWaveParameters, timing_parameters: SignalVoltageGenerationTimingParameters) -> None`

Generates a signal that is a sine wave according to `signal_parameters`.

        Args:
            signal_parameters (SignalVoltageGenerationSineWaveParameters):
                An instance of `SignalVoltageGenerationSineWaveParameters`
                used to configure the signal to generate.
            timing_parameters (SignalVoltageGenerationTimingParameters):
                An instance of `SignalVoltageGenerationTimingParameters` used
                to configure the sample rate and duration of the signal to be generated.
        

#### `def generate_voltage_square_waveform(self, signal_parameters: SignalVoltageGenerationSquareWaveParameters, timing_parameters: SignalVoltageGenerationTimingParameters) -> None`

Creates a signal that is a square wave.

        Args:
            signal_parameters (SignalVoltageGenerationSquareWaveParameters):
                An instance of `SignalVoltageGenerationSquareWaveParameters`
                used to configure the signal to generate.
            timing_parameters (SignalVoltageGenerationTimingParameters):
                An instance of `SignalVoltageGenerationTimingParameters` used
                to configure the sample rate and duration of the signal to be generated.
        

#### `def generate_voltage_multi_tones_waveform(self, signal_parameters: SignalVoltageGenerationMultipleTonesWaveParameters, timing_parameters: SignalVoltageGenerationTimingParameters) -> None`

Generates a signal that contains sum of multiple sine waves at different tones
        (amplitudes and frequencies).

        Args:
            signal_parameters (SignalVoltageGenerationMultipleTonesWaveParameters):
                An instance of `SignalVoltageGenerationMultipleTonesWaveParameters`
                    used to configure the signal to generate.
            timing_parameters (SignalVoltageGenerationTimingParameters):
                An instance of `SignalVoltageGenerationTimingParameters` used
                to configure the sample rate and duration of the signal to be generated.
        

#### `def configure_and_generate_sine_waveform(self, configuration: SignalVoltageGenerationSineWaveConfiguration) -> None`

Configures and generates the Sine wave according to the specific configuration.

        Args:
            configuration (SignalVoltageGenerationSineWaveConfiguration):
                An instance of `SignalVoltageGenerationSineWaveConfiguration`
                used to configure the generation of single tone sine voltage signal at the channel.
        

#### `def configure_and_generate_square_waveform(self, configuration: SignalVoltageGenerationSquareWaveConfiguration) -> None`

Configures and generates a Square wave voltage signal according
        to the specific configuration.

        Args:
            configuration (SignalVoltageGenerationSquareWaveConfiguration):
                An instance of `SignalVoltageGenerationSquareWaveConfiguration`
                used to configure the generation of square wave voltage signal at the channel.
        

#### `def configure_and_generate_multiple_tones_waveform(self, configuration: SignalVoltageGenerationMultipleTonesConfiguration) -> None`

Configures and generates a multi-tone sine wave voltage signal according
        to the specific configuration.

        Args:
            configuration (SignalVoltageGenerationMultipleTonesConfiguration):
                An instance of `SignalVoltageGenerationMultipleTonesConfiguration`
                used to configure the generation of multi-tones voltage waveform at the channel.
        

#### `def close(self)`

Closes generation procedure and releases internal resources.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/signal_voltage_generations/signal_voltage_generation_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/signal_voltage_generations/signal_voltage_generation_constants.py

### MODULE DOCSTRING

 Constants data types for Signal Voltage Generation Data types.

### `class ConstantsForSignalVoltageGeneration()`

Constants used for signal voltage generation.

- `DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS = VoltageGenerationChannelParameters(range_min_volts=ConstantsForSignalVoltageGeneration.DEFAULT_RANGE_MIN_VOLTS, range_max_volts=ConstantsForSignalVoltageGeneration.DEFAULT_RANGE_MAX_VOLTS)`

- `DEFAULT_TONE_PARAMETERS = ToneParameters(tone_frequency_hertz=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_FREQUENCY_HERTZ, tone_amplitude_volts=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_AMPLITUDE_VOLTS, tone_phase_radians=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_PHASE_RADIANS)`

- `DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_PARAMETERS = SignalVoltageGenerationSineWaveParameters(generated_signal_offset_volts=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_OFFSET_VOLTS, generated_signal_tone_parameters=DEFAULT_TONE_PARAMETERS)`

- `DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS = SignalVoltageGenerationTimingParameters(sample_clock_source=ConstantsForSignalVoltageGeneration.DEFAULT_SAMPLE_CLOCK_SOURCE, sampling_rate_hertz=ConstantsForSignalVoltageGeneration.DEFAULT_SAMPLING_RATE_HERTZ, generated_signal_duration_seconds=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_DURATION_SECONDS)`

- `DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS = DigitalStartTriggerParameters(trigger_select=ConstantsForSignalVoltageGeneration.DEFAULT_TRIGGER_TYPE, digital_start_trigger_source=ConstantsForSignalVoltageGeneration.DEFAULT_DIGITAL_START_TRIGGER_SOURCE, digital_start_trigger_edge=ConstantsForSignalVoltageGeneration.DEFAULT_DIGITAL_START_TRIGGER_EDGE)`

- `DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_CONFIGURATION = SignalVoltageGenerationSineWaveConfiguration(voltage_generation_range_parameters=DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS, waveform_parameters=DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_PARAMETERS, timing_parameters=DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS, digital_start_trigger_parameters=DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS)`

- `DEFAULT_SIGNAL_VOLTAGE_GENERATION_SQUARE_WAVE_PARAMETERS = SignalVoltageGenerationSquareWaveParameters(generated_signal_amplitude_volts=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_AMPLITUDE_VOLTS, generated_signal_offset_volts=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_OFFSET_VOLTS, generated_signal_frequency_hertz=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_FREQUENCY_HERTZ, generated_signal_duty_cycle_percent=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_DUTY_CYCLE_PERCENT, generated_signal_phase_radians=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_PHASE_RADIANS)`

- `DEFAULT_SQUARE_WAVE_GENERATION_CONFIGURATION = SignalVoltageGenerationSquareWaveConfiguration(voltage_generation_range_parameters=DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS, waveform_parameters=DEFAULT_SIGNAL_VOLTAGE_GENERATION_SQUARE_WAVE_PARAMETERS, timing_parameters=DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS, digital_start_trigger_parameters=DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS)`

- `DEFAULT_MULTI_TONE_GENERATION_PARAMETERS = SignalVoltageGenerationMultipleTonesWaveParameters(generated_signal_offset_volts=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_OFFSET_VOLTS, generated_signal_amplitude_volts=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_AMPLITUDE_VOLTS, multiple_tones_parameters=[ToneParameters(tone_frequency_hertz=100, tone_amplitude_volts=1.0, tone_phase_radians=0), ToneParameters(tone_frequency_hertz=200, tone_amplitude_volts=0.5, tone_phase_radians=0.1)])`

- `DEFAULT_MULTI_TONE_GENERATION_CONFIGURATION = SignalVoltageGenerationMultipleTonesConfiguration(voltage_generation_range_parameters=DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS, waveform_parameters=DEFAULT_MULTI_TONE_GENERATION_PARAMETERS, timing_parameters=DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS, digital_start_trigger_parameters=DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS)`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/static_digital_state_generations/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/static_digital_state_generations/__init__.py

### MODULE DOCSTRING

Provides nipcbatt library static digital state generation modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/static_digital_state_generations/static_digital_state_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/static_digital_state_generations/static_digital_state_data_types.py

### MODULE DOCSTRING

 Static Digital State Generation data types

### `class StaticDigitalStateGenerationConfiguration(PCBATestToolkitData)`

Defines the values used in the creation of Static Digital State Configuration

#### `def __init__(self, data_to_write: List[bool]) -> None`

Initializes an instance of 'StaticDigitalStateGenerationConfiguration
           with specific values.

        Args:
            data_to_write (array of boolean):
                The boolean state of each channel to write to the hardware
        

#### `def data_to_write(self) -> List[bool]`


        :type: array of 'bool': Holds the state of the write values to the DO channels
        

### `class StaticDigitalStateGenerationData(PCBATestToolkitData)`

Defines the values used in the production of Static Digital State Generation Data

#### `def __init__(self, channel_identifiers: List[str]) -> None`

Initializes an instance of StaticDigitalStateGenerationData with specific values.

        Args:
            channel_identifiers (array of string):
                The list of channels to which the data to write is written
        

#### `def channel_identifiers(self) -> List[str]`


        :type: array of 'str': Holds the names of the digital output channels to write to
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/static_digital_state_generations/static_digital_state_generation.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/static_digital_state_generations/static_digital_state_generation.py

### MODULE DOCSTRING

Use this class to generate digital states to output on system

### `class StaticDigitalStateGeneration(BuildingBlockUsingDAQmx)`

This class represents the set of static digital states
       the user wishes to write to digital output lines

    Args:
        BuildingBlockUsingDAQmx (_type_): _description_
    

#### `def initialize(self, channel_expression: str)`

Initializes the task to prepare for generation

        Args:
            channel_expression (str): The name of the lines/port
            where the data will be written
        

#### `def close(self)`

Closes the task and returns the hardware resource

#### `def configure_and_generate(self, configuration: StaticDigitalStateGenerationConfiguration) -> StaticDigitalStateGenerationData`

Uses the configuration provided to generate the digital
           states on the hardware

        Args:
            configuration (StaticDigitalStateGenerationConfiguration): An
            instance of an object that contains the states to generate

        Returns:
            StaticDigitalStateGenerationData: Contains an array of strings
            describing the lines that were written to
        

#### `def generate_digital_states(self, output_states: List[bool]) -> StaticDigitalStateGenerationData`

This method takes the states the user wishes to generate
           and creates a StaticDigitalStateGenerationData object

        Args:
            output_states (List[bool]): The list of digital states
            to be generated

        Returns:
            StaticDigitalStateGenerationData: An array of strings
            describing the lines that were written to
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/static_digital_state_measurements/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/static_digital_state_measurements/__init__.py

### MODULE DOCSTRING

Provides nipcbatt library static digital state measurement modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/static_digital_state_measurements/static_digital_state_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/static_digital_state_measurements/static_digital_state_data_types.py

### MODULE DOCSTRING

Static digital state  data types

### `class StaticDigitalStateMeasurementResultData(PCBATestToolkitData)`

Defines parameters used for configuration of static digital state measurements

#### `def __init__(self, digital_states: List[bool], channel_identifiers: List[str]) -> None`

Initializes an instance of `StaticDigitalStateMeasurementResultData'
        with specific values

        Args:
            digital_states (array of boolean):
                The boolean state of each corresponding channel in the measurement
            channel_identifiers (array of string):
                The channel ID of each channel in the measurement
        

#### `def digital_states(self) -> List[bool]`


        :type: array of 'bool': Holds the state of each channel
        

#### `def channel_identifiers(self) -> List[str]`

:type: array of 'str': Identifies each channel

#### `def states_per_channels(self) -> Dict[str, bool]`

:type: dictionary of 'str', 'bool' pairs
            maps each channel to its current state

        Returns:
            Dict[str, bool]: mapping of channel to digital state
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/static_digital_state_measurements/static_digital_state_measurement.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/static_digital_state_measurements/static_digital_state_measurement.py

### MODULE DOCSTRING

 _summary_ 

### `class StaticDigitalStateMeasurement(BuildingBlockUsingDAQmx)`

Defines the means for creating, configuring, and measuring
    the static digital state of a series of digital lines

    Args:
        BuildingBlockUsingDAQmx (_type_): _description_
    

#### `def initialize(self, channel_expression: str)`

Initializes Digital input channels for static digital measurements for
        a DAQmx Task

        Args:
            channel_expression (str): Digital input channels to read off of the
            DAQmx task
        

#### `def close(self)`

Closes the measurement process and releases the internal resources

#### `def configure_and_measure(self) -> StaticDigitalStateMeasurementResultData`

Configures and executes a measurement according to the current configuration parameters.

        Args:

        Returns:
            An instance of `StaticDigitalStateMeasurementResultData
            ` or `None` if no measure was performed.
        

#### `def acquire_data_for_measurement_analysis(self) -> StaticDigitalStateMeasurementResultData`

Processes digital data acquistion for measurement analysis

        Args:

        Returns:
            An instance of StaticDigitalStateMeasurementResultData

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/synchronizations/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/synchronizations/__init__.py

### MODULE DOCSTRING

Provides nipcbatt library synchronization signal routing modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/synchronizations/synchronization_signal_routing.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/synchronizations/synchronization_signal_routing.py

### MODULE DOCSTRING

 Defines class used for routing of synchronization signal.

### `class SynchronizationSignalRouting(BuildingBlockUsingDAQmx)`

Defines a way that allows you to route synchronization signal
    (sample clock or start trigger) to specific terminal.

#### `def route_sample_clock_signal_to_terminal(self, terminal_name: str)`

Routes sample clock signal to the specified terminal.

        Args:
            terminal_name (str):
            The name of the terminal where the signal is routed.
        

#### `def route_start_trigger_signal_to_terminal(self, terminal_name: str)`

Routes start trigger signal to the specified terminal.

        Args:
            terminal_name (str):
            The name of the terminal where the signal is routed.
        

#### `def close(self)`

Closes signal routing procedure.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/temperature_measurements/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/temperature_measurements/__init__.py

### MODULE DOCSTRING

Provides nipcbatt library temperature measurement modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_constants.py

### MODULE DOCSTRING

 Constants data types for Temperature measurements.

### `class ConstantsForTemperatureMeasurement()`

Constants used for Temperature measurements

### `class ConstantsForTemperatureMeasurementUsingRtd()`

Constants used for Temperature measurement using RTD

### `class ConstantsForTemperatureMeasurementUsingThermistor()`

Constants used for Temperature measurement using Thermistor

### `class ConstantsForTemperatureMeasurementUsingThermocouple()`

Constants used for Temperature measurement using Thermocouple

- `DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS = TemperatureRtdMeasurementTerminalParameters(temperature_minimum_value_celsius_degrees=ConstantsForTemperatureMeasurement.DEFAULT_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES, temperature_maximum_value_celsius_degrees=ConstantsForTemperatureMeasurement.DEFAULT_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES, current_excitation_value_amperes=ConstantsForTemperatureMeasurementUsingRtd.DEFAULT_CURRENT_EXCITATION_VALUE_AMPERES, sensor_resistance_ohms=ConstantsForTemperatureMeasurementUsingRtd.DEFAULT_SENSOR_RESISTANCE_OHMS, rtd_type=ConstantsForTemperatureMeasurementUsingRtd.DEFAULT_RTD_TYPE, excitation_source=ConstantsForTemperatureMeasurementUsingRtd.DEFAULT_EXCITATION_SOURCE, resistance_configuration=ConstantsForTemperatureMeasurementUsingRtd.DEFAULT_RESISTANCE_CONFIGURATION, adc_timing_mode=ConstantsForTemperatureMeasurementUsingRtd.DEFAULT_ADC_TIMING_MODE)`

- `DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS = SampleClockTimingParameters(sample_clock_source=ConstantsForTemperatureMeasurement.DEFAULT_SAMPLE_CLOCK_SOURCE, sampling_rate_hertz=ConstantsForTemperatureMeasurement.DEFAULT_SAMPLING_RATE_HERTZ, number_of_samples_per_channel=ConstantsForTemperatureMeasurement.DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL, sample_timing_engine=ConstantsForTemperatureMeasurement.DEFAULT_SAMPLE_TIMING_ENGINE)`

- `DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS = DigitalStartTriggerParameters(trigger_select=ConstantsForTemperatureMeasurement.DEFAULT_TRIGGER_TYPE, digital_start_trigger_source=ConstantsForTemperatureMeasurement.DEFAULT_DIGITAL_START_TRIGGER_SOURCE, digital_start_trigger_edge=ConstantsForTemperatureMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE)`

- `DEFAULT_TEMPERATURE_RTD_MEASUREMENT_CONFIGURATION = TemperatureRtdMeasurementConfiguration(global_channel_parameters=DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS, specific_channels_parameters=[], measurement_execution_type=MeasurementExecutionType.CONFIGURE_AND_MEASURE, sample_clock_timing_parameters=DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS, digital_start_trigger_parameters=DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS)`

- `DEFAULT_COEFFICIENTS_STEINHART_HART_PARAMETERS = CoefficientsSteinhartHartParameters(coefficient_steinhart_hart_a=ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_COEFFICIENT_STAINHART_HART_A, coefficient_steinhart_hart_b=ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_COEFFICIENT_STAINHART_HART_B, coefficient_steinhart_hart_c=ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_COEFFICIENT_STAINHART_HART_C)`

- `DEFAULT_BETA_OEFFICIENT_AND_SENSOR_RESISTANCE_PARAMETERS = BetaCoefficientAndSensorResistanceParameters(coefficient_steinhart_hart_beta_kelvins=ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_COEFFICIENT_STAINHART_HART_BETA_KELVINS, sensor_resistance_ohms=ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_THERMISTOR_SENSOR_RESISTANCE_OHMS)`

- `DEFAULT_TEMPERATURE_THERMISTOR_RANGE_AND_TERMINAL_PARAMETERS = TemperatureThermistorRangeAndTerminalParameters(terminal_configuration=ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_AI_TERMINAL_CONFIGURATION, temperature_minimum_value_celsius_degrees=ConstantsForTemperatureMeasurement.DEFAULT_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES, temperature_maximum_value_celsius_degrees=ConstantsForTemperatureMeasurement.DEFAULT_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES, voltage_excitation_value_volts=ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_VOLTAGE_EXCITATION_VALUE_VOLTS, thermistor_resistor_ohms=ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_THERMISTOR_RESISTOR_OHMS, steinhart_hart_equation_option=ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_STEINHART_HART_EQUATION_OPTION, coefficients_steinhart_hart_parameters=DEFAULT_COEFFICIENTS_STEINHART_HART_PARAMETERS, beta_coefficient_and_sensor_resistance_parameters=DEFAULT_BETA_OEFFICIENT_AND_SENSOR_RESISTANCE_PARAMETERS)`

- `DEFAULT_TEMPERATURE_THERMISTOR_MEASUREMENT_CONFIGURATION = TemperatureThermistorMeasurementConfiguration(global_channel_parameters=DEFAULT_TEMPERATURE_THERMISTOR_RANGE_AND_TERMINAL_PARAMETERS, specific_channels_parameters=[], measurement_execution_type=MeasurementExecutionType.CONFIGURE_AND_MEASURE, sample_clock_timing_parameters=DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS, digital_start_trigger_parameters=DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS)`

- `DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS = TemperatureThermocoupleMeasurementTerminalParameters(temperature_minimum_value_celsius_degrees=ConstantsForTemperatureMeasurementUsingThermocouple.DEFAULT_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES, temperature_maximum_value_celsius_degrees=ConstantsForTemperatureMeasurementUsingThermocouple.DEFAULT_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES, thermocouple_type=ConstantsForTemperatureMeasurementUsingThermocouple.DEFAULT_THERMOCOUPLE_TYPE, cold_junction_compensation_temperature=ConstantsForTemperatureMeasurementUsingThermocouple.DEFAULT_COLD_JUNCTION_COMPENSATION_TEMPERATURE, perform_auto_zero_mode=ConstantsForTemperatureMeasurementUsingThermocouple.DEFAULT_ENABLE_AUTOZERO, auto_zero_mode=ConstantsForTemperatureMeasurementUsingThermocouple.DEFAULT_AUTOZERO_MODE)`

- `DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_CONFIGURATION = TemperatureThermocoupleMeasurementConfiguration(global_channel_parameters=DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS, specific_channels_parameters=[], measurement_execution_type=MeasurementExecutionType.CONFIGURE_AND_MEASURE, sample_clock_timing_parameters=DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS, digital_start_trigger_parameters=DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS)`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_data_types.py

### MODULE DOCSTRING

 Temperature data types

### `class TemperatureRtdMeasurementTerminalParameters(PCBATestToolkitData)`

Defines the parameters used to configure terminal
    of all channels for temperature measurement using RTD.

#### `def __init__(self, temperature_minimum_value_celsius_degrees: float, temperature_maximum_value_celsius_degrees: float, current_excitation_value_amperes: float, sensor_resistance_ohms: float, rtd_type: nidaqmx.constants.RTDType, excitation_source: nidaqmx.constants.ExcitationSource, resistance_configuration: nidaqmx.constants.ResistanceConfiguration, adc_timing_mode: nidaqmx.constants.ADCTimingMode) -> None`

Initializes an instance of `TemperatureRtdMeasurementTerminalParameters`
           with specific values.

        Args:
            temperature_minimum_value_celsius_degrees (float):
                The minimum value expected from the measurement, expressed in °C.
            temperature_maximum_value_celsius_degrees (float):
                The maximum value expected from the measurement, expressed in °C.
            current_excitation_value_amperes (float): The amount of excitation
                to supply to the sensor, in Amperes.
                Refer to the sensor documentation to determine this value.
            sensor_resistance_ohms (float): The sensor resistance, in Ohms,
                at 0 degree Celsius (also called R0).
            rtd_type (nidaqmx.constants.RTDType):
                The type of `RTD <https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/measfunds/rtdtypes.html>`
                connected to the channel.
            excitation_source (nidaqmx.constants.ExcitationSource): The source of excitation.
            resistance_configuration (nidaqmx.constants.ResistanceConfiguration): The mode
                that represents the number of `wires <https://en.wikipedia.org/wiki/Resistance_thermometer#Wiring_configurations>`
                to use for resistive measurements.
            adc_timing_mode (nidaqmx.constants.ADCTimingMode): The
                `ADC Timing Mode <https://www.ni.com/docs/en-US/bundle/ni-daqmx-properties/page/daqmxprop/attr29f9.html>`.

        Raises:
            ValueError:
                Raised when `temperature_minimum_value_celsius_degrees'
                is greater than or equal to `temperature_maximum_value_celsius_degrees`.
        

#### `def temperature_minimum_value_celsius_degrees(self) -> float`


        :type:`float`: Gets the minimum value expected from the measurement, expressed in °C.
        

#### `def temperature_maximum_value_celsius_degrees(self) -> float`


        :type:`float`: Gets the minimum value expected from the measurement, expressed in °C.
        

#### `def current_excitation_value_amperes(self) -> float`


        :type:`float`: Gets the amount of excitation to supply to the sensor, in Amperes.
        

#### `def sensor_resistance_ohms(self) -> float`


        :type:`float`: Gets the sensor resistance, in Ohms,
                at 0 degree Celsius (also called R0).
        

#### `def rtd_type(self) -> nidaqmx.constants.RTDType`


        :type:`float`: Gets the type of
            `RTD <https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/measfunds/rtdtypes.html>`
            connected to the channel.
        

#### `def excitation_source(self) -> nidaqmx.constants.ExcitationSource`


        :type:`float`: Gets the source of excitation.
        

#### `def resistance_configuration(self) -> nidaqmx.constants.ResistanceConfiguration`


        :type:`float`: Gets the mode
            that represents the number of
            `wires <https://en.wikipedia.org/wiki/Resistance_thermometer#Wiring_configurations>`
            to use for resistive measurements.
        

#### `def adc_timing_mode(self) -> nidaqmx.constants.ADCTimingMode`


        :type:`float`: Gets the `ADC Timing Mode
            <https://www.ni.com/docs/en-US/bundle/ni-daqmx-properties/page/daqmxprop/attr29f9.html>`.
        

### `class TemperatureRtdMeasurementChannelParameters(PCBATestToolkitData)`

Defines the parameters used to configure channels for temperature measurement using RTD.

#### `def __init__(self, channel_name: str, sensor_resistance_ohms: float, current_excitation_value_amperes: float, rtd_type: nidaqmx.constants.RTDType, resistance_configuration: nidaqmx.constants.ResistanceConfiguration, excitation_source: nidaqmx.constants.ExcitationSource) -> None`

_summary_

        Args:
            channel_name (str):
                The name of the channel to configure.
            sensor_resistance_ohms (float): The sensor resistance, in Ohms,
                at 0 degree Celsius (also called R0).
            current_excitation_value_amperes (float): The amount of excitation
                to supply to the sensor, in Amperes.
                Refer to the sensor documentation to determine this value.
            rtd_type (nidaqmx.constants.RTDType):
                The type of `RTD <https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/measfunds/rtdtypes.html>`
                connected to the channel.
            resistance_configuration (nidaqmx.constants.ResistanceConfiguration): The mode
                that represents the number of
                `wires <https://en.wikipedia.org/wiki/Resistance_thermometer#Wiring_configurations>`
                to use for resistive measurements.
            excitation_source (nidaqmx.constants.ExcitationSource): The source of excitation.

        Raises:
            ValueError:
                Raised when `channel_name` is None or empty or whitespace.
        

#### `def channel_name(self) -> str`


        :type:`str`: Gets the name of the channel to configure.
        

#### `def sensor_resistance_ohms(self) -> float`


        :type:`float`: Gets the sensor resistance, in Ohms,
                at 0 degree Celsius (also called R0).
        

#### `def current_excitation_value_amperes(self) -> float`


        :type:`float`: Gets the amount of excitation to supply to the sensor, in Amperes.
        

#### `def rtd_type(self) -> nidaqmx.constants.RTDType`


        :type:`float`: Gets the type of
            `RTD <https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/measfunds/rtdtypes.html>`
            connected to the channel.
        

#### `def resistance_configuration(self) -> nidaqmx.constants.ResistanceConfiguration`


        :type:`float`: Gets the mode
            that represents the number of
            `wires <https://en.wikipedia.org/wiki/Resistance_thermometer#Wiring_configurations>`
            to use for resistive measurements.
        

#### `def excitation_source(self) -> nidaqmx.constants.ExcitationSource`


        :type:`float`: Gets the source of excitation.
        

### `class TemperatureRtdMeasurementConfiguration(PCBATestToolkitData)`

Defines parameters used for configuration of Temperature measurement using RTD.

#### `def __init__(self, global_channel_parameters: TemperatureRtdMeasurementTerminalParameters, specific_channels_parameters: List[TemperatureRtdMeasurementChannelParameters], measurement_execution_type: MeasurementExecutionType, sample_clock_timing_parameters: SampleClockTimingParameters, digital_start_trigger_parameters: DigitalStartTriggerParameters) -> None`

Initializes an instance of
        `TemperatureRtdMeasurementConfiguration` with specific values.

        Args:
            global_channel_parameters (TemperatureRtdMeasurementTerminalParameters):
                The settings of terminal for all channels.
            specific_channels_parameters (List[TemperatureRtdMeasurementChannelParameters]):
                The list of instances of `TemperatureRtdMeasurementChannelParameters`
                used to configure channels.
            measurement_execution_type (MeasurementExecutionType):
                The type of measurement execution selected by user.
            sample_clock_timing_parameters (SampleClockTimingParameters):
                An instance of `SampleClockTimingParameters` that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters`
                that represents the settings of triggers.

        Raises:
            TypeError:
                Raised when `specific_channels_parameters`
                contains objects that are not type of TemperatureRtdMeasurementChannelParameters.
            ValueError:
                Raised when `global_channel_parameters` is None,
                `specific_channels_parameters` is None,
                `sample_clock_timing_parameters` is None,
                `digital_start_trigger_parameters` is None,
        

#### `def global_channel_parameters(self) -> TemperatureRtdMeasurementTerminalParameters`


        :class:`TemperatureRtdMeasurementChannelParameters`:
            Gets the settings of terminal for all channels.

#### `def specific_channels_parameters(self) -> List[TemperatureRtdMeasurementChannelParameters]`


        :class:`List[VoltageMeasurementChannelAndTerminalRangeParameters]`:
            Gets the list of instances of
            `TemperatureRtdMeasurementChannelParameters` used to configure channels.
        

#### `def measurement_execution_type(self) -> MeasurementExecutionType`


        :class:`MeasurementExecutionType`:
            Gets the type of measurement execution selected by user.
        

#### `def sample_clock_timing_parameters(self) -> SampleClockTimingParameters`


        :class:`SampleClockTimingParameters`:
            Gets a `SampleClockTimingParameters` instance
            that represents the settings of timing.
        

#### `def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters`


        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        

### `class SteinhartHartEquationOption(Enum)`

Defines the option of to use coefficients
    in Steinhart-Hart equation used during channels configuration.

### `class CoefficientsSteinhartHartParameters(PCBATestToolkitData)`

Defines the parameters used to configure coefficients of
    the <Steinhart-Hart https://en.wikipedia.org/wiki/Thermistor#Steinhart.E2.80.93Hart_equation>
    for Temperature measurements.

#### `def __init__(self, coefficient_steinhart_hart_a: float, coefficient_steinhart_hart_b: float, coefficient_steinhart_hart_c: float) -> None`

Initializes an instance of
        `CoefficientsSteinhartHartParameters` with specific values.

        Args:
            coefficient_steinhart_hart_a (float): The A coefficient in the
            `Steinhart-Hart <https://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation>` equation.
            coefficient_steinhart_hart_b (float): The B coefficient in the
            `Steinhart-Hart <https://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation>` equation.
            coefficient_steinhart_hart_c (float): The C coefficient in the
            `Steinhart-Hart <https://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation>` equation.
        

#### `def coefficient_steinhart_hart_a(self) -> float`


        :type:`float`:
            Gets the A coefficient in the
            `Steinhart-Hart <https://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation>` equation.
        

#### `def coefficient_steinhart_hart_b(self) -> float`


        :type:`float`:
            Gets the B coefficient in the
            `Steinhart-Hart <https://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation>` equation.
        

#### `def coefficient_steinhart_hart_c(self) -> float`


        :type:`float`:
            Gets the C coefficient in the
            `Steinhart-Hart <https://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation>` equation.
        

### `class BetaCoefficientAndSensorResistanceParameters(PCBATestToolkitData)`

Defines the parameters for coefficients
    (`β coefficient <https://en.wikipedia.org/wiki/Thermistor#B_or_.CE.B2_parameter_equation>` and sensor resistance)
    of Steinhart-Hart equation.

#### `def __init__(self, coefficient_steinhart_hart_beta_kelvins: float, sensor_resistance_ohms: float) -> None`

Initializes an instance of
        `BetaCoefficientAndSensorResistanceParameters` with specific values.

        Args:
            coefficient_steinhart_hart_beta_kelvins (float):
            The `β coefficient <https://en.wikipedia.org/wiki/Thermistor#B_or_.CE.B2_parameter_equation>`
            used with the Steinhart-Hart equation, in Kelvins.
            Coefficients A, B and C of the equation are computed from this coefficient.
            sensor_resistance_ohms (float):
            The sensor resistance, in Ohms, at 25 degrees Celsius (298.15 Kelvins).
            Coefficients A, B and C of the equation are computed from this coefficient.
        

#### `def coefficient_steinhart_hart_beta_kelvins(self) -> float`


        :type:`float`:
            Gets the `β coefficient <https://en.wikipedia.org/wiki/Thermistor#B_or_.CE.B2_parameter_equation>`
            used with the Steinhart-Hart equation, in Kelvins.
            Coefficients A, B and C of the equation are computed from this coefficient.
        

#### `def sensor_resistance_ohms(self) -> float`


        :type:`float`:
            Gets the sensor resistance, in Ohms, at 25 degrees Celsius (298.15 Kelvins).
            Coefficients A, B and C of the equation are computed from this coefficient.
        

### `class TemperatureThermistorRangeAndTerminalParameters(PCBATestToolkitData)`

Defines the parameters used to configure terminal
    of all channels for temperature measurement using Thermistor.

#### `def __init__(self, terminal_configuration: nidaqmx.constants.TerminalConfiguration, temperature_minimum_value_celsius_degrees: float, temperature_maximum_value_celsius_degrees: float, voltage_excitation_value_volts: float, thermistor_resistor_ohms: float, steinhart_hart_equation_option: SteinhartHartEquationOption, coefficients_steinhart_hart_parameters: CoefficientsSteinhartHartParameters, beta_coefficient_and_sensor_resistance_parameters: BetaCoefficientAndSensorResistanceParameters) -> None`

Initializes an instance of
        `TemperatureThermistorRangeAndTerminalParameters` with specific values.

        Args:
            terminal_configuration (nidaqmx.constants.TerminalConfiguration):
                The input terminal configuration parameter.
            temperature_minimum_value_celsius_degrees (float):
                The minimum value expected from the measurement, expressed in °C.
            temperature_maximum_value_celsius_degrees (float):
                The maximum value expected from the measurement, expressed in °C.
            voltage_excitation_value_volts (float):
                The amount of voltage excitation to supply to the sensor, expressed in Volts.
                Refer to the sensor documentation to determine this value.
            thermistor_resistor_ohms (float):
                The reference resistor for the
                `thermistor <https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/measfunds/thermistors.html>`
                if you use voltage excitation, in Ohms.
            steinhart_hart_equation_option (SteinhartHartEquationOption):
                The option used to compute coefficients of Steinhart-Hart equation.
            coefficients_steinhart_hart_parameters (CoefficientsSteinhartHartParameters):
                An instance of `CoefficientsSteinhartHartParameters`
                representing the coefficients of the SteinHart-Hart equation.
            beta_coefficient_and_sensor_resistance_parameters (BetaCoefficientAndSensorResistanceParameters):
                An instance of `BetaCoefficientAndSensorResistanceParameters`
                representing the coefficients
                (`β coefficient <https://en.wikipedia.org/wiki/Thermistor#B_or_.CE.B2_parameter_equation>` and sensor resistance)
                of Steinhart-Hart equation.

        Raises:
            ValueError:
                Raised when `temperature_minimum_value_celsius_degrees`
                is greater than or equal to `temperature_maximum_value_celsius_degrees`,
                `coefficients_steinhart_hart_parameters` is None
                and `steinhart_hart_equation_option` is equal to
                `SteinhartHartEquationOption.USE_STEINHART_HART_COEFFICIENTS`,
                `beta_coefficient_and_sensor_resistance_parameters` is None
                and `steinhart_hart_equation_option` is equal to
                `SteinhartHartEquationOption.USE_COEFFICIENT_BETA_AND_SENSOR_RESISTANCE`.
        

#### `def terminal_configuration(self) -> nidaqmx.constants.TerminalConfiguration`


        :class:`nidaqmx.constants.TerminalConfiguration`:
            Gets the input terminal configuration parameter.
        

#### `def temperature_minimum_value_celsius_degrees(self) -> float`


        :type:`float`:
            Gets the minimum value expected from the measurement, expressed in °C.
        

#### `def temperature_maximum_value_celsius_degrees(self) -> float`


        :type:`float`:
            Gets the maximum value expected from the measurement, expressed in °C.
        

#### `def voltage_excitation_value_volts(self) -> float`


        :type:`float`:
            Gets the amount of voltage excitation to supply to the sensor, expressed in Volts.
            Refer to the sensor documentation to determine this value.
        

#### `def thermistor_resistor_ohms(self) -> float`


        :type:`float`:
            Gets the reference resistor for the
            `thermistor <https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/measfunds/thermistors.html>`
            if you use voltage excitation, in Ohms.
        

#### `def steinhart_hart_equation_option(self) -> SteinhartHartEquationOption`


        :class:`SteinhartHartEquationOption`:
            Gets the option used to compute coefficients of Steinhart-Hart equation.
        

#### `def coefficients_steinhart_hart_parameters(self) -> CoefficientsSteinhartHartParameters`


        :class:`CoefficientsSteinhartHartParameters`:
            Gets an instance of `CoefficientsSteinhartHartParameters`
            representing the coefficients of the SteinHart-Hart equation.
        

#### `def beta_coefficient_and_sensor_resistance_parameters(self)`


        :class:`BetaCoefficientAndSensorResistanceParameters`:
            Gets an instance of `BetaCoefficientAndSensorResistanceParameters`
            representing the coefficients
            (`β coefficient <https://en.wikipedia.org/wiki/Thermistor#B_or_.CE.B2_parameter_equation>` and sensor resistance)
            of Steinhart-Hart equation.
        

### `class TemperatureThermistorChannelRangeAndTerminalParameters(PCBATestToolkitData)`

Defines settings for channel and terminal used to configure temperature measurement based on thermistor.

#### `def __init__(self, channel_name: str, channel_parameters: TemperatureThermistorRangeAndTerminalParameters) -> None`

Initializes an instance of
        `TemperatureThermistorChannelRangeAndTerminalParameters` with specific values.

        Args:
            channel_name (str):
                The name of the channel to configure.
            channel_parameters (TemperatureThermistorRangeAndTerminalParameters): The settings of the channel.

        Raises:
            ValueError:
                Raised when `channel_name` is None or empty or whitespace,
                `channel_parameters` is None.
        

#### `def channel_name(self) -> str`


        :type:`str`:
            Gets the name of the channel to configure.
        

#### `def channel_parameters(self) -> TemperatureThermistorRangeAndTerminalParameters`


        :class:`TemperatureThermistorRangeAndTerminalParameters`:
            Gets the settings of the channel.
        

### `class TemperatureThermistorMeasurementConfiguration(PCBATestToolkitData)`

Defines parameters used for configuration of Temperature measurement using Thermistor.

#### `def __init__(self, global_channel_parameters: TemperatureThermistorRangeAndTerminalParameters, specific_channels_parameters: List[TemperatureThermistorChannelRangeAndTerminalParameters], measurement_execution_type: MeasurementExecutionType, sample_clock_timing_parameters: SampleClockTimingParameters, digital_start_trigger_parameters: DigitalStartTriggerParameters) -> None`

Initializes an instance of
        `TemperatureRtdMeasurementConfiguration` with specific values.

        Args:
            global_channel_parameters (TemperatureThermistorMeasurementTerminalParameters):
                The settings of terminal for all channels.
            specific_channels_parameters (List[TemperatureThermistorChannelRangeAndTerminalParameters]):
                The list of instances of `TemperatureThermistorChannelRangeAndTerminalParameters`
                used to configure channels.
            measurement_execution_type (MeasurementExecutionType):
                The type of measurement execution selected by user.
            sample_clock_timing_parameters (SampleClockTimingParameters):
                An instance of `SampleClockTimingParameters` that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters`
                that represents the settings of triggers.

        Raises:
            TypeError:
                Raised when `specific_channels_parameters`
                contains objects that are not type of TemperatureThermistorChannelRangeAndTerminalParameters.
            ValueError:
                Raised when `global_channel_parameters` is None,
                `specific_channels_parameters` is None,
                `sample_clock_timing_parameters` is None,
                `digital_start_trigger_parameters` is None,
        

#### `def global_channel_parameters(self) -> TemperatureThermistorRangeAndTerminalParameters`


        :class:`TemperatureThermistorRangeAndTerminalParameters`:
            Gets the settings of terminal for all channels.
        

#### `def specific_channels_parameters(self) -> List[TemperatureThermistorChannelRangeAndTerminalParameters]`


        :class:`List[TemperatureThermistorChannelRangeAndTerminalParameters]`:
            Gets the list of instances of `TemperatureThermistorChannelRangeAndTerminalParameters`
            used to configure channels.
        

#### `def measurement_execution_type(self) -> MeasurementExecutionType`


        :class:`MeasurementExecutionType`:
            Gets the type of measurement execution selected by user.
        

#### `def sample_clock_timing_parameters(self) -> SampleClockTimingParameters`


        :class:`SampleClockTimingParameters`:
            Gets a `SampleClockTimingParameters` instance
            that represents the settings of timing.
        

#### `def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters`


        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        

### `class TemperatureThermocoupleMeasurementTerminalParameters(PCBATestToolkitData)`

Defines the parameters used to configure terminal
    of all channels for temperature measurement using Thermocouple.

#### `def __init__(self, temperature_minimum_value_celsius_degrees: float, temperature_maximum_value_celsius_degrees: float, thermocouple_type: nidaqmx.constants.ThermocoupleType, cold_junction_compensation_temperature: float, perform_auto_zero_mode: bool, auto_zero_mode: nidaqmx.constants.AutoZeroType) -> None`

Initializes an instance of
        `TemperatureThermocoupleMeasurementTerminalParameters` with specific values.

        Args:
            temperature_minimum_value_celsius_degrees (float):
                The minimum value expected from the measurement, expressed in °C.
            temperature_maximum_value_celsius_degrees (float):
                The maximum value expected from the measurement, expressed in °C.
            thermocouple_type (nidaqmx.constants.ThermocoupleType):
                Enum for ThermocoupleType: (B,E,J,K,N,R,S,T);
                Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.ThermocoupleType
            cold_junction_compensation_temperature (float):
                Specifies the temperature of the cold junction, expressed in °C;
                if cold_junction_compensation_source is set as 'CONSTANT_USER_VALUE'.
            perform_auto_zero_mode (bool):
                The option used to Enable or Disable Auto zero mode.
            auto_zero_mode (nidaqmx.constants.AutoZeroType):
                The option to set when to perform an auto zero during acquisition.
                Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.AutoZeroType


        Raises:
            ValueError:
                Raised when `temperature_minimum_value_celsius_degrees`
                is greater than or equal to `temperature_maximum_value_celsius_degrees`,
                `temperature_minimum_value_celsius_degrees` is None or not float,
                `temperature_maximum_value_celsius_degrees` is None or not float,
                `thermocouple_type` is None,
                'cold_junction_compensation_temperature' is None or not float,
                'perform_auto_zero_mode' is None,
                if 'perform_auto_zero_mode' is True and 'auto_zero_mode' is None.

        

#### `def temperature_minimum_value_celsius_degrees(self) -> float`


        :type:`float`:
            Gets the minimum value expected from the measurement, expressed in °C.
        

#### `def temperature_maximum_value_celsius_degrees(self) -> float`


        :type:`float`:
            Gets the maximum value expected from the measurement, expressed in °C.
        

#### `def thermocouple_type(self) -> nidaqmx.constants.ThermocoupleType`


        :type:`nidaqmx.constants.ThermocoupleType`:
            Enum for ThermocoupleType: (B,E,J,K,N,R,S,T);
            Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.ThermocoupleType
        

#### `def cold_junction_compensation_temperature(self) -> float`


        :type:`float`:
           Cold junction compensation temperature, expressed in °C.
        

#### `def perform_auto_zero_mode(self) -> bool`


        :class:`bool`:
            The option used to Enable or Disable Auto zero mode.
        

#### `def auto_zero_mode(self) -> nidaqmx.constants.AutoZeroType`


        :class:`nidaqmx.constants.AutoZeroType`:
            The option to set when to perform an auto zero during acquisition.
                Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.AutoZeroType
        

### `class TemperatureThermocoupleRangeAndTerminalParameters(PCBATestToolkitData)`

Defines the parameters used to configure terminal
    of all channels for temperature measurement using Thermocouple.

#### `def __init__(self, temperature_minimum_value_celsius_degrees: float, temperature_maximum_value_celsius_degrees: float, thermocouple_type: nidaqmx.constants.ThermocoupleType, cold_junction_compensation_source: nidaqmx.constants.CJCSource, cold_junction_compensation_temperature: float, cold_junction_compensation_channel_name: str, perform_auto_zero_mode: bool, auto_zero_mode: nidaqmx.constants.AutoZeroType) -> None`

Initializes an instance of
        `TemperatureThermocoupleRangeAndTerminalParameters` with specific values.

        Args:
            temperature_minimum_value_celsius_degrees (float):
                The minimum value expected from the measurement, expressed in °C.
            temperature_maximum_value_celsius_degrees (float):
                The maximum value expected from the measurement, expressed in °C.
            thermocouple_type (nidaqmx.constants.ThermocoupleType):
                Enum for ThermocoupleType: (B,E,J,K,N,R,S,T);
                Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.ThermocoupleType
            cold_junction_compensation_source (nidaqmx.constants.CJCSource):
                Specify the source for cold junction compensation: [CONSTANT_USER_VALUE, SCANNABLE_CHANNEL, BUILT_IN]
                Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.CJCSource
            cold_junction_compensation_temperature (float):
                Specifies the temperature of the cold junction, expressed in °C;
                if cold_junction_compensation_source is set as 'CONSTANT_USER_VALUE'.
            cold_junction_compensation_channel_name (str):
                Specifies the channel that acquires the temperature of the thermocouple cold-junction
                if cold_junction_compensation_source is set as 'SCANNABLE_CHANNEL'.
            perform_auto_zero_mode (bool):
                The option used to Enable or Disable Auto zero mode.
            auto_zero_mode (nidaqmx.constants.AutoZeroType):
                The option to set when to perform an auto zero during acquisition.
                Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.AutoZeroType


        Raises:
            ValueError:
                Raised when `temperature_minimum_value_celsius_degrees`
                is greater than or equal to `temperature_maximum_value_celsius_degrees`,
                `temperature_minimum_value_celsius_degrees` is None or not float,
                `temperature_maximum_value_celsius_degrees` is None or not float,
                `thermocouple_type` is None,
                'cold_junction_compensation_source' is None,
                if cold_junction_compensation_source==CONSTANT_USER_VALUE, then
                    'cold_junction_compensation_temperature' is None or not float,
                if cold_junction_compensation_source==SCANNABLE_CHANNEL, then
                    'cold_junction_compensation_channel_name' is None, empty or whitespace,
                'perform_auto_zero_mode' is None,
                if 'perform_auto_zero_mode' is True and 'auto_zero_mode' is None.

        

#### `def temperature_minimum_value_celsius_degrees(self) -> float`


        :type:`float`:
            Gets the minimum value expected from the measurement, expressed in °C.
        

#### `def temperature_maximum_value_celsius_degrees(self) -> float`


        :type:`float`:
            Gets the maximum value expected from the measurement, expressed in °C.
        

#### `def thermocouple_type(self) -> nidaqmx.constants.ThermocoupleType`


        :type:`nidaqmx.constants.ThermocoupleType`:
            Enum for ThermocoupleType: (B,E,J,K,N,R,S,T);
            Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.ThermocoupleType
        

#### `def cold_junction_compensation_source(self) -> nidaqmx.constants.CJCSource`


        :type:`nidaqmx.constants.CJCSource`:
           Cold junction compensation Source.
           Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.CJCSource
        

#### `def cold_junction_compensation_temperature(self) -> float`


        :type:`float`:
           Cold junction compensation temperature, expressed in °C.
        

#### `def cold_junction_compensation_channel_name(self) -> str`


        :type:`str`:
           Specify the channel to use for Cold junction compensation.
        

#### `def perform_auto_zero_mode(self) -> bool`


        :class:`bool`:
            The option used to Enable or Disable Auto zero mode.
        

#### `def auto_zero_mode(self) -> nidaqmx.constants.AutoZeroType`


        :class:`nidaqmx.constants.AutoZeroType`:
            The option to set when to perform an auto zero during acquisition.
                Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.AutoZeroType
        

### `class TemperatureThermocoupleChannelRangeAndTerminalParameters(PCBATestToolkitData)`

Defines settings for channel and terminal used to configure temperature measurement based on thermocouple.

#### `def __init__(self, channel_name: str, channel_parameters: TemperatureThermocoupleRangeAndTerminalParameters) -> None`

Initializes an instance of
        `TemperatureThermocoupleChannelRangeAndTerminalParameters` with specific values.

        Args:
            channel_name (str):
                The name of the channel to configure.
            channel_parameters (TemperatureThermocoupleRangeAndTerminalParameters): The settings of the channel.

        Raises:
            ValueError:
                Raised when `channel_name` is None or empty or whitespace,
                `channel_parameters` is None.
        

#### `def channel_name(self) -> str`


        :type:`str`:
            Gets the name of the channel to configure.
        

#### `def channel_parameters(self) -> TemperatureThermocoupleRangeAndTerminalParameters`


        :class:`TemperatureThermocoupleRangeAndTerminalParameters`:
            Gets the settings of the channel.
        

### `class TemperatureThermocoupleMeasurementConfiguration(PCBATestToolkitData)`

Defines parameters used for configuration of Temperature measurement using Thermocouple.

#### `def __init__(self, global_channel_parameters: TemperatureThermocoupleMeasurementTerminalParameters, specific_channels_parameters: List[TemperatureThermocoupleChannelRangeAndTerminalParameters], measurement_execution_type: MeasurementExecutionType, sample_clock_timing_parameters: SampleClockTimingParameters, digital_start_trigger_parameters: DigitalStartTriggerParameters) -> None`

Initializes an instance of
        `TemperatureThermocoupleMeasurementConfiguration` with specific values.

        Args:
            global_channel_parameters (TemperatureThermocoupleMeasurementTerminalParameters):
                The settings of terminal for all channels.
            specific_channels_parameters (List[TemperatureThermocoupleChannelRangeAndTerminalParameters]):
                The list of instances of `TemperatureThermocoupleChannelRangeAndTerminalParameters`
                used to configure channels.
            measurement_execution_type (MeasurementExecutionType):
                The type of measurement execution selected by user.
            sample_clock_timing_parameters (SampleClockTimingParameters):
                An instance of `SampleClockTimingParameters` that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters`
                that represents the settings of triggers.

        Raises:
            TypeError:
                Raised when `specific_channels_parameters`
                contains objects that are not type of TemperatureThermocoupleChannelRangeAndTerminalParameters.
            ValueError:
                Raised when `global_channel_parameters` is None,
                `specific_channels_parameters` is None,
                `sample_clock_timing_parameters` is None,
                `digital_start_trigger_parameters` is None,
        

#### `def global_channel_parameters(self) -> TemperatureThermocoupleMeasurementTerminalParameters`


        :class:`TemperatureThermocoupleMeasurementTerminalParameters`:
            Gets the settings of terminal for all channels.
        

#### `def specific_channels_parameters(self) -> List[TemperatureThermocoupleChannelRangeAndTerminalParameters]`


        :class:`List[TemperatureThermocoupleChannelRangeAndTerminalParameters]`:
            Gets the list of instances of `TemperatureThermocoupleChannelRangeAndTerminalParameters`
            used to configure channels.
        

#### `def measurement_execution_type(self) -> MeasurementExecutionType`


        :class:`MeasurementExecutionType`:
            Gets the type of measurement execution selected by user.
        

#### `def sample_clock_timing_parameters(self) -> SampleClockTimingParameters`


        :class:`SampleClockTimingParameters`:
            Gets a `SampleClockTimingParameters` instance
            that represents the settings of timing.
        

#### `def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters`


        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        

### `class TemperatureMeasurementResultData(PCBATestToolkitData)`

Defines voltage temperature results obtained after waveform analysis.

#### `def __init__(self, waveforms: List[AnalogWaveform], acquisition_duration_seconds: float, average_temperatures_celsius_degrees: List[float], average_temperatures_kelvin: List[float]) -> None`

Initializes an instance of
           `TemperatureMeasurementResultData` with specific values.

        Args:
            waveforms (List[AnalogWaveform]):
                The list of waveforms acquired from channels defined for measurement
                and used to compute temperature.
            acquisition_duration_seconds (float):
                The duration of acquisition of samples for each configured channel.
            average_temperatures_celsius_degrees (List[float]):
                The list of average temperatures computed for each configured channel,
                expressed in celsius degrees.
            average_temperatures_kelvin (List[float]):
                The list of average temperatures computed for each configured channel,
                expressed in kelvin.

        Raises:
            ValueError:
                Raised when `waveforms` is None or empty,
                `average_temperatures_celsius` is None or empty,
                `average_temperatures_kelvin` is None or empty,
            TypeError:
                Raised when `waveforms` contains objects that are not `AnalogWaveform`,
                `acquisition_duration_seconds' is None,
                If the `acquisition_duration_seconds' is less than or equal to zero,
                `average_temperatures_celsius_degrees` contains objects that are not `float`,
                `average_temperatures_kelvin` contains objects that are not `float`
        

#### `def waveforms(self) -> List[AnalogWaveform]`


        :class:`List[AnalogWaveform]`:
            Gets list of waveforms acquired from channels defined for measurement
            and used to compute temperature.
        

#### `def acquisition_duration_seconds(self) -> float`


        :type:`float`:
            Gets the duration of acquisition of samples for each configured channel.
        

#### `def average_temperatures_celsius_degrees(self) -> List[float]`


        :class:`List[float]`:
            Gets the list of average temperatures computed for each configured channel,
            expressed in celsius degrees.
        

#### `def average_temperatures_kelvin(self) -> List[float]`


        :class:`List[float]`:
            Gets the list of average temperatures computed for each configured channel,
            expressed in kelvins.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_measurement.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_measurement.py

### MODULE DOCSTRING

Defines class with common methods used for temperature measurements on PCB points.

### `class TemperatureMeasurement(BuildingBlockUsingDAQmx)`

Defines a way that allows you to perform Temperature measurements on PCB points.

#### `def close(self)`

Closes measurement procedure and releases internal resources.

#### `def configure_timing(self, parameters: SampleClockTimingParameters)`

Configures the timing characteristics used for temperature measurements.

        Args:
            parameters (SampleClockTimingParameters):
            An instance of `SampleClockTimingParameters`
            used to configure the timing.
        

#### `def configure_trigger(self, parameters: DigitalStartTriggerParameters)`

Configure the characteristics of triggers used for temperature measurements.

        Args:
            parameters (DigitalStartTriggerParameters):
            An instance of `DigitalStartTriggerParameters`
            used to configure the channels.
        

#### `def acquire_data_for_measurement_analysis(self) -> MeasurementData`

Acquires Data from DAQ channel for measurement of temperature.

        Returns:
            MeasurementData: An instance of `MeasurementData`
            that specifies the data acquired from DAQ channels.
        

#### `def analyze_measurement_data(self, measurement_data: MeasurementData) -> TemperatureMeasurementResultData`

Proceeds to the analysis of temperatures from the measurement.

        Args:
            measurement_data (MeasurementData): An instance of `MeasurementData`
            that specifies the data acquired from DAQ channels.

        Returns:
            TemperatureMeasurementResultData:
            An instance of `TemperatureMeasurementResultData`
            that specifies the measurement results.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_measurement_using_rtd.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_measurement_using_rtd.py

### MODULE DOCSTRING

Defines class used for temperature measurement using RTD on PCB points.

### `class TemperatureMeasurementUsingRtd(TemperatureMeasurement)`

Defines a way that allows you to perform Temperature measurements using RTD on PCB points.

#### `def initialize(self, channel_expression: str)`

Initializes the measurement with the specific channels

        Args:
            channel_expression (str):
                Expression representing the name of a physical channel,
                or a global channel in DAQ System.
        

#### `def configure_and_measure(self, configuration: TemperatureRtdMeasurementConfiguration)`

Configures and/or performs a measurement
           according to specific configuration parameters.

        Args:
            configuration (TemperatureRtdMeasurementConfiguration):
            A instance of `TemperatureRtdMeasurementConfiguration`
            used to configure the measurement.

        Returns:
            TemperatureMeasurementResultData | None:
            An instance of `TemperatureMeasurementResultData`
            or `None` if no measure was performed.
        

#### `def configure_all_channels(self, parameters: TemperatureRtdMeasurementTerminalParameters)`

Configures all channels used for temperature measurements using RTD.

        Args:
            parameters (TemperatureRtdMeasurementTerminalParameters):
            An instance of `TemperatureRtdMeasurementTerminalParameters`
            used to configure the channels.
        

#### `def configure_specific_channel(self, parameters: TemperatureRtdMeasurementChannelParameters)`

Configures the specific channels used for temperature measurements using RTD.

        Args:
            parameters (TemperatureRtdMeasurementChannelParameters):
            An instance of `TemperatureRtdMeasurementChannelParameters`
            used to configure the channels.

        If the user provides Global Virtual Channel name in Initialize(),
        then he/she has to provide the Virtual channel name in Specific channel parameters as well.

        Similarly, if the user provides Physical channel name in Initialize(),
        then he/she has to provide the Physical channel name in Specific channel parameters.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_measurement_using_thermistor.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_measurement_using_thermistor.py

### MODULE DOCSTRING

Defines class used for temperature measurement using Thermistor on PCB points.

### `class TemperatureMeasurementUsingThermistor(TemperatureMeasurement)`

Defines a way that allows you to perform Temperature measurements
    using Thermistor on PCB points.

#### `def initialize(self, channel_expression: str)`

Initializes the measurement with the specific channels
        Args:
            channel_expression (str):
                Expression representing the name of a physical channel,
                or a global channel in DAQ System.
        

#### `def configure_and_measure(self, configuration: TemperatureThermistorMeasurementConfiguration)`

Configures and/or performs a measurement
           according to specific configuration parameters.

        Args:
            configuration (TemperatureRtdMeasurementConfiguration):
            A instance of `TemperatureRtdMeasurementConfiguration`
            used to configure the measurement.

        Returns:
            TemperatureMeasurementResultData | None:
            An instance of `TemperatureMeasurementResultData`
            or `None` if no measure was performed.
        

#### `def configure_all_channels(self, parameters: TemperatureThermistorRangeAndTerminalParameters)`

Configures all channels used for temperature measurements using a Thermistor.

        Args:
            parameters (TemperatureThermistorRangeAndTerminalParameters):
            An instance of `TemperatureThermistorRangeAndTerminalParameters`
            used to configure the channels.
        

#### `def configure_specific_channel(self, parameters: TemperatureThermistorChannelRangeAndTerminalParameters)`

Configures the specific channels used for temperature measurements using a Thermistor.

        Args:
            parameters (TemperatureThermistorChannelRangeAndTerminalParameters):
            An instance of `TemperatureThermistorChannelRangeAndTerminalParameters`
            used to configure the channels.

        If the user provides Global Virtual Channel name in Initialize(),
        then he/she has to provide the Virtual channel name in Specific channel parameters as well.

        Similarly, if the user provides Physical channel name in Initialize(),
        then he/she has to provide the Physical channel name in Specific channel parameters.
        

#### `def _compute_steinhart_hart_coefficients_from_parameters(self, parameters: TemperatureThermistorRangeAndTerminalParameters) -> CoefficientsSteinhartHartParameters`

#### `def _compute_steinhart_hart_coefficients(self, coefficient_steinhart_hart_beta_kelvins: float, sensor_resistance_ohms: float) -> CoefficientsSteinhartHartParameters`

Computes coefficients of Steinhart-Hart equation.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_measurement_using_thermocouple.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_measurement_using_thermocouple.py

### MODULE DOCSTRING

Defines class used for temperature measurement using Thermocouple on PCB points.

### `class TemperatureMeasurementUsingThermocouple(TemperatureMeasurement)`

Defines a way that allows you to perform Temperature measurements
    using Thermocouple on PCB points.

#### `def initialize(self, channel_expression: str, cold_junction_compensation_channel: str, cold_junction_compensation_source=nidaqmx.constants.CJCSource.BUILT_IN)`

Initializes the measurement with the specific channels
        Args:
            channel_expression (str):
                Expression representing the name of a physical channel,
                or a global channel in DAQ System.
            cold_junction_compensation_channel (str):
                Expression representing channel for cold junction compensation when 'cold_junction_compensation_source'
                is specified as 'nidaqmx.constants.CJCSource.SCANNABLE_CHANNEL'.
            cold_junction_compensation_source (nidaqmx.constants.CJCSource):
                Specify the source for cold junction compensation: [CONSTANT_USER_VALUE, SCANNABLE_CHANNEL, BUILT_IN]
                Default value is set as BUILT_IN.
        

#### `def configure_and_measure(self, configuration: TemperatureThermocoupleMeasurementConfiguration)`

Configures and/or performs a measurement
           according to specific configuration parameters.

        Args:
            configuration (TemperatureThermocoupleMeasurementConfiguration):
            A instance of `TemperatureThermocoupleMeasurementConfiguration`
            used to configure the measurement.

        Returns:
            TemperatureMeasurementResultData | None:
            An instance of `TemperatureMeasurementResultData`
            or `None` if no measure was performed.
        

#### `def configure_all_channels(self, parameters: TemperatureThermocoupleMeasurementTerminalParameters)`

Configures all channels used for temperature measurements using a Thermocouple.

        Args:
            parameters (TemperatureThermocoupleMeasurementTerminalParameters):
            An instance of `TemperatureThermocoupleMeasurementTerminalParameters`
            used to configure the channels.
        

#### `def configure_specific_channel(self, parameters: TemperatureThermocoupleChannelRangeAndTerminalParameters)`

Configures the specific channels used for temperature measurements using a Thermocouple.

        Args:
            parameters (TemperatureThermocoupleChannelRangeAndTerminalParameters):
            An instance of `TemperatureThermocoupleChannelRangeAndTerminalParameters`
            used to configure the channels.

        If the user provides Global Virtual Channel name in Initialize(),
        then he/she has to provide the Virtual channel name in Specific channel parameters as well.

        Similarly, if the user provides Physical channel name in Initialize(),
        then he/she has to provide the Physical channel name in Specific channel parameters.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/time_domain_measurements/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/time_domain_measurements/__init__.py

### MODULE DOCSTRING

Provides nipcbatt library time domain measurement modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/time_domain_measurements/time_domain_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/time_domain_measurements/time_domain_constants.py

### MODULE DOCSTRING

 Constants data types for Time domain Measurements.

### `class ConstantsForTimeDomainMeasurement()`

Constants used for Time Domain measurement

- `DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS = VoltageRangeAndTerminalParameters(terminal_configuration=ConstantsForVoltageMeasurement.DEFAULT_AI_TERMINAL_CONFIGURATION, range_min_volts=ConstantsForVoltageMeasurement.DEFAULT_VOLTAGE_MINIMUM_VALUE_VOLTS, range_max_volts=ConstantsForVoltageMeasurement.DEFAULT_VOLTAGE_MAXIMUM_VALUE_VOLTS)`

- `DEFAULT_TIME_DOMAIN_MEASUREMENT_OPTIONS = MeasurementOptions(execution_option=ConstantsForVoltageMeasurement.DEFAULT_EXECUTION_TYPE, measurement_analysis_requirement=ConstantsForVoltageMeasurement.DEFAULT_MEASUREMENT_ANALYSIS_REQUIREMENT)`

- `DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS = SampleClockTimingParameters(sample_clock_source=ConstantsForVoltageMeasurement.DEFAULT_SAMPLE_CLOCK_SOURCE, sampling_rate_hertz=ConstantsForVoltageMeasurement.DEFAULT_SAMPLING_RATE_HERTZ, number_of_samples_per_channel=ConstantsForVoltageMeasurement.DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL, sample_timing_engine=ConstantsForVoltageMeasurement.DEFAULT_SAMPLE_TIMING_ENGINE)`

- `DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS = DigitalStartTriggerParameters(trigger_select=ConstantsForVoltageMeasurement.DEFAULT_TRIGGER_TYPE, digital_start_trigger_source=ConstantsForVoltageMeasurement.DEFAULT_DIGITAL_START_TRIGGER_SOURCE, digital_start_trigger_edge=ConstantsForVoltageMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE)`

- `DEFAULT_TIME_DOMAIN_MEASUREMENT_CONFIGURATION = TimeDomainMeasurementConfiguration(global_channel_parameters=DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS, specific_channels_parameters=[], measurement_options=DEFAULT_TIME_DOMAIN_MEASUREMENT_OPTIONS, sample_clock_timing_parameters=DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS, digital_start_trigger_parameters=DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS)`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/time_domain_measurements/time_domain_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/time_domain_measurements/time_domain_data_types.py

### MODULE DOCSTRING

 Time Domain data types 

### `class TimeDomainMeasurementConfiguration(PCBATestToolkitData)`

Defines parameters used for configuration of Time domain measurement.

#### `def __init__(self, global_channel_parameters: VoltageRangeAndTerminalParameters, specific_channels_parameters: List[VoltageMeasurementChannelAndTerminalRangeParameters], measurement_options: MeasurementOptions, sample_clock_timing_parameters: SampleClockTimingParameters, digital_start_trigger_parameters: DigitalStartTriggerParameters) -> None`

Initializes an instance of
        `TimeDomainMeasurementConfiguration` with specific values.

        Args:
            global_channel_parameters (VoltageRangeAndTerminalParameters):
                The settings of terminal for all channels.
            specific_channels_parameters (List[VoltageMeasurementChannelAndTerminalRangeParameters]):
                The list of instances of `VoltageMeasurementChannelAndTerminalRangeParameters` used to configure channels.
            measurement_options (MeasurementOptions):
                An instance of `MeasurementOptions` that represents the settings of options used for execution.
            sample_clock_timing_parameters (SampleClockTimingParameters):
                An instance of `SampleClockTimingParameters` that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters` that represents the settings of triggers.

        Raises:
            TypeError:
                Raised when `specific_channels_parameters`
                contains objects that are not type of VoltageMeasurementChannelAndTerminalRangeParameters.
            ValueError:
                Raised when `global_channel_parameters` is None,
                `specific_channels_parameters` is None,
                `measurement_options` is None,
                `sample_clock_timing_parameters` is None,
                `digital_start_trigger_parameters` is None,
        

#### `def global_channel_parameters(self) -> VoltageRangeAndTerminalParameters`


        :class:`VoltageRangeAndTerminalParameters`:
            Gets the settings of terminal for all channels.

#### `def specific_channels_parameters(self) -> List[VoltageMeasurementChannelAndTerminalRangeParameters]`


        :class:`List[VoltageMeasurementChannelAndTerminalRangeParameters]`:
            Gets the list of instances of
            `VoltageMeasurementChannelAndTerminalRangeParameters` used to configure channels.
        

#### `def measurement_options(self) -> MeasurementOptions`


        :class:`MeasurementOptions`:
            Gets a `MeasurementOptions` instance
            that represents the settings of options used for execution.
        

#### `def sample_clock_timing_parameters(self) -> SampleClockTimingParameters`


        :class:`SampleClockTimingParameters`:
            Gets a `SampleClockTimingParameters` instance
            that represents the settings of timing.
        

#### `def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters`


        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        

### `class TimeDomainMeasurementResultData(PCBATestToolkitData)`

Defines voltage Time domain measurement results obtained after waveform analysis.

#### `def __init__(self, waveforms: List[AnalogWaveform], acquisition_duration_seconds: float, mean_dc_voltage_values_volts: List[float], vpp_amplitudes_volts: List[float], voltage_waveforms_frequencies_hertz: List[float], voltage_waveforms_periods_seconds: List[float], voltage_waveforms_duty_cycles_percent: List[float]) -> None`

Initializes an instance of
        `TimeDomainMeasurementResultData` with specific values.

        Args:
            waveforms (List[AnalogWaveform]):
                The list of waveforms acquired from channels defined for measurement and used to compute DC-RMS voltage.
            acquisition_duration_seconds (float):
                The duration of acquisition of samples for each configured channel.
            mean_dc_voltage_values_volts (List[float]):
                The list of mean DC voltages computed for all configured channels, expressed in Volts.
            vpp_amplitudes_volts (List[float]):
                The list of peak to peak voltage amplitudes computed for all configured channels, expressed in Volts.
            voltage_waveforms_frequencies_hertz (List[float]):
                The list of voltage waveforms frequencies computed for all configured channels, expressed in Hertz.
            voltage_waveforms_periods_seconds (List[float]):
                The list of voltage waveforms periods computed for all configured channels, expressed in seconds.
            voltage_waveforms_duty_cycles_percent (List[float]):
                The list of voltage waveforms duty cycles computed for all configured channels, expressed in %.

        Raises:
            TypeError:
                Raised when `waveforms` contains objects that are not `AnalogWaveform`,
                `mean_dc_voltage_values_volts` contains objects that are not `float`,
                `vpp_amplitudes_volts` contains objects that are not `float`,
                `voltage_waveforms_frequencies_hertz` contains objects that are not `float`,
                `voltage_waveforms_periods_seconds` contains objects that are not `float`,
                `voltage_waveforms_duty_cycles_percent` contains objects that are not `float`.
            ValueError:
                Raised when `waveforms` is None or empty.
        

#### `def waveforms(self) -> List[AnalogWaveform]`


        :class:`List[AnalogWaveform]`:
            Gets the list of waveforms acquired from channels defined
            for measurement and used to compute time domain results.
        

#### `def acquisition_duration_seconds(self) -> float`


        :type:`float`:
            Gets the duration of acquisition of samples for each configured channel.
        

#### `def mean_dc_voltage_values_volts(self) -> List[float]`


        :class:`List[float]`:
            Gets the list of mean DC voltages computed for all configured channels, expressed in Volts.
        

#### `def vpp_amplitudes_volts(self) -> List[float]`


        :class:`List[float]`:
            Gets the list of peak to peak voltage amplitudes computed for all configured channels, expressed in Volts.
        

#### `def voltage_waveforms_frequencies_hertz(self) -> List[float]`


        :class:`List[float]`:
            Gets the list of voltage waveforms frequencies computed for all configured channels, expressed in Hertz.
        

#### `def voltage_waveforms_periods_seconds(self) -> List[float]`


        :class:`List[float]`:
            Gets the list of voltage waveforms periods computed for all configured channels, expressed in seconds.
        

#### `def voltage_waveforms_duty_cycles_percent(self) -> List[float]`


        :class:`List[float]`:
            Gets the list of voltage waveforms duty cycles computed for all configured channels, expressed in %.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/time_domain_measurements/time_domain_measurement.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/daq/time_domain_measurements/time_domain_measurement.py

### MODULE DOCSTRING

 Defines class used for Time domain measurement on PCB points.

- `DEFAULT_NUMERIC_RESULT_VALUE = 0.0`

### `class TimeDomainMeasurement(BuildingBlockUsingDAQmx)`

Defines a way that allows you to perform Time domain measurements on PCB points.

#### `def initialize(self, analog_input_channel_expression: str)`

Initializes the measurement with the specific channels

        Args:
            analog_input_channel_expression (str):
                Expression representing the name of a physical channel,
                or a global channel in DAQ System.
        

#### `def close(self)`

Closes measurement procedure and releases internal resources.

#### `def configure_and_measure(self, configuration: TimeDomainMeasurementConfiguration)`

Configures and/or performs a measurement according to specific configuration parameters.

        Args:
            configuration (TimeDomainMeasurementConfiguration):
            A instance of `TimeDomainMeasurementConfiguration` used to configure the measurement.

        Returns:
            TimeDomainMeasurementResultData | None: An instance of `TimeDomainMeasurementResultData`
              or `None` if no measure was performed.
        

#### `def configure_all_channels(self, parameters: VoltageRangeAndTerminalParameters)`

Configures all channels used for voltage measurements.

        Args:
            parameters (VoltageRangeAndTerminalParameters):
            An instance of `VoltageRangeAndTerminalParameters` used to configure the channels.
        

#### `def configure_specific_channel(self, parameters: VoltageMeasurementChannelAndTerminalRangeParameters)`

Configures the specific channels used for voltage measurements.

        Args:
            parameters (VoltageMeasurementChannelAndTerminalRangeParameters):
            An instance of `VoltageMeasurementChannelAndTerminalRangeParameters`
            used to configure the channels.

        If the user provides Global Virtual Channel name in Initialize(),
        then he/she has to provide the Virtual channel name in Specific channel parameters as well.

        Similarly, if the user provides Physical channel name in Initialize(),
        then he/she has to provide the Physical channel name in Specific channel parameters.
        

#### `def configure_timing(self, parameters: SampleClockTimingParameters) -> None`

Configures the timing characteristics used for time domain measurements.

        Args:
            parameters:An instance of `SampleClockTimingParameters` used to configure the timing.
        

#### `def configure_trigger(self, parameters: DigitalStartTriggerParameters) -> None`

Configures the characteristics of triggers used for time domain measurements.

        Args:
            parameters (DigitalStartTriggerParameters): An instance of
            `DigitalStartTriggerParameters` used to
        configure the channels.
        

#### `def acquire_data_for_measurement_analysis(self) -> MeasurementData`

Acquires Data from DAQ channel for measurement of voltage.

        Returns:
            MeasurementData: An instance of `MeasurementData`
            that specifies the data acquired from DAQ channels.
        

#### `def analyze_measurement_data(self, measurement_data: MeasurementData, measurement_analysis_requirement: MeasurementAnalysisRequirement) -> TimeDomainMeasurementResultData`

Proceeds to the analysis of Voltages from the measurement.

        Args:
            data (MeasurementData):
                An instance of `MeasurementData`
                that specifies the data acquired from DAQ channels.
            measurement_analysis_requirement (MeasurementAnalysisRequirement):
                An instance of 'MeasurementAnalysisRequirement' that specifies
                whether to Skip Analysis or Proceed to Analysis.

        Returns:
            TimeDomainMeasurementResultData:
                An instance of `TimeDomainMeasurementResultData`
                that specifies the measurement results.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dcpower/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dcpower/__init__.py

### MODULE DOCSTRING

Contains SMU modules for pcbatt library.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dcpower/common/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dcpower/common/__init__.py

### MODULE DOCSTRING

Provides common helper functions for DC power operations.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dcpower/common/common_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dcpower/common/common_data_types.py

### MODULE DOCSTRING

Common data types shared across DC power source and measure operations.

### `class MeasurementExecutionType(Enum)`

Defines the execution type for DC source and measure operations.

### `class SourceTriggerBehavior(Enum)`

Defines the source trigger behavior enum.

### `class ExportEvent(Enum)`

Defines the export event enum.

### `class EventSignalToExport(Enum)`

Defines the NI-DCPower event or trigger signal to route to an output terminal enum.

    Each member's value is the corresponding NI-DCPower channel attribute name,
    used with ``setattr`` to configure the output terminal for that signal.
    

### `class ExecutionSettings()`

Defines execution settings for a DC source and measure operation.

#### `def __init__(self, execution_type: MeasurementExecutionType, skip_analysis: bool) -> None`

Initializes the execution settings.

        Args:
            execution_type (MeasurementExecutionType):
                The execution type having values:
                - ``CONFIGURE_SOURCE_AND_MEASURE``,
                - ``CONFIGURE_ONLY``,
                - ``START_SOURCE_ONLY``, or
                - ``MEASURE_ONLY``.
            skip_analysis (bool):
                When ``True``, post-measurement analysis is skipped.
        

#### `def execution_type(self) -> MeasurementExecutionType`

Gets the measurement execution type.

        Returns:
            MeasurementExecutionType: The configured execution type.
        

#### `def skip_analysis(self) -> bool`

Gets whether post-measurement analysis is skipped.

        Returns:
            bool: ``True`` if analysis is skipped;
            ``False`` if full analysis is performed.
        

### `class TimingParameters()`

Defines timing settings for DC source and measure operations.

#### `def __init__(self, source_delay: float, aperture_time: float, transient_response: nidcpower.TransientResponse) -> None`

Initializes the timing parameters.

        Args:
            source_delay (float):
                Defines source delay in seconds.
            aperture_time (float):
                Defines aperture time in seconds.
            transient_response (nidcpower.TransientResponse):
                Defines the transient response.
        

#### `def source_delay(self) -> float`

Gets the source delay.

        Returns:
            float: The source delay in seconds.
        

#### `def aperture_time(self) -> float`

Gets the aperture time.

        Returns:
            float: The aperture time in seconds.
        

#### `def transient_response(self) -> nidcpower.TransientResponse`

Gets the transient response setting.

        Returns:
            nidcpower.TransientResponse: The transient response mode.
        

### `class TriggerParameters()`

Defines trigger parameters and event signal routing settings for
    a DC source operation.
    

#### `def __init__(self, source_trigger_behavior: SourceTriggerBehavior, start_source_name: str, export_event: ExportEvent, event_signal_to_export: EventSignalToExport, output_event_signal_terminal: str) -> None`

Initializes the trigger parameters.

        Args:
            source_trigger_behavior (SourceTriggerBehavior):
                Configures source trigger behavior.
            start_source_name (str):
                Configures the start source name.
                Ignored when ``source_trigger_behavior`` is ``Disable_Source_Trigger``.
            export_event (ExportEvent):
                Configures export event.
            event_signal_to_export (EventSignalToExport):
                Configures the event signal to export.
                Ignored when ``export_event`` is ``NONE``.
            output_event_signal_terminal (str):
                The output terminal name to which the event signal is routed.
                Ignored when ``export_event`` is ``NONE``.
        

#### `def source_trigger_behavior(self) -> SourceTriggerBehavior`

Gets the source trigger behavior.

        Returns:
            SourceTriggerBehavior: Configures source trigger behavior.
        

#### `def start_source_name(self) -> str`

Gets the start source name.

        Returns:
            str: The start source name.
        

#### `def export_event(self) -> ExportEvent`

Gets the export event setting.

        Returns:
            ExportEvent: Configures export event.
        

#### `def event_signal_to_export(self) -> EventSignalToExport`

Gets the event signal to export.

        Returns:
            EventSignalToExport: Configures the event signal to export.
        

#### `def output_event_signal_terminal(self) -> str`

Gets the output event signal terminal.

        Returns:
            str: Configures the output event signal terminal.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dcpower/common/helper_function.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dcpower/common/helper_function.py

### MODULE DOCSTRING

Helper functions for DC power instrument operations.

- `_SI_PREFIXES = {-24: 'y', -21: 'z', -18: 'a', -15: 'f', -12: 'p', -9: 'n', -6: 'u', -3: 'm', 0: '', 3: 'k', 6: 'M', 9: 'G', 12: 'T', 15: 'P', 18: 'E'}`

### `def format_si_fixed_decimals(value: float, unit: str, decimal_places: int=3) -> str`

Formats a numeric value in SI engineering notation with a fixed number of decimal places.

    Scales the value to engineering notation (exponent divisible by 3),
    applies the matching SI prefix, and appends the unit directly without a space.

    Args:
        value (float):
            The numeric value to format.
        unit (str):
            The unit string to append (e.g., ``"A"``, ``"W"``, ``"Ohm"``).
        decimal_places (int):
            Number of digits after the decimal point. Defaults to ``3``.

    Returns:
        str: Formatted string with SI prefix and unit attached.

    Examples:
        ``format_si_fixed_decimals(0.000958775, "A")`` → ``"958.775uA"``

        ``format_si_fixed_decimals(9.696e-5, "W")`` → ``"96.960uW"``

        ``format_si_fixed_decimals(105.477, "Ohm")`` → ``"105.477Ohm"``

        ``format_si_fixed_decimals(0.0, "V")`` → ``"0.000V"``
    

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dcpower/dc_cc_source_and_measure/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dcpower/dc_cc_source_and_measure/__init__.py

### MODULE DOCSTRING

Provides DC current source and measure functionality using SMU and PPS.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dcpower/dc_cc_source_and_measure/dc_cc_source_and_measure.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dcpower/dc_cc_source_and_measure/dc_cc_source_and_measure.py

### MODULE DOCSTRING

Defines class used for DC constant current source and measurement on PCB points.

- `_APERTURE_TIME_UNSUPPORTED_MODELS = frozenset({'NI PXI-4110', 'NI PXI-4130', 'NI PXI-4131A', 'NI PXIe-4154'})`

### `class DCCurrentSourceAndMeasure(BuildingBlockUsingNIDCPower)`

Defines a way that allows you to source DC current and perform measurements on PCB points.

#### `def initialize(self, resource_name: str)`

Initializes the NI DC Power session with the specified resource.

        Opens a new NI-DCPower session, resets the channel, configures
        the source mode to single-point, and sets the output function to DC current.
        Also initializes the ``_execution_settings`` and ``_measurement_results``
        instance dictionaries with ``NaN`` defaults so that state persists across the
        separated ``CONFIGURE_ONLY``, ``START_SOURCE_ONLY``, and ``MEASURE_ONLY`` calls.

        Args:
            resource_name (str): NI-DCPower resource name, e.g. ``"PPS1/0"``.
        

#### `def enable_output(self, enable_output: bool) -> None`

Enables or disables the output of the channel.

        Args:
            enable_output (bool): True to enable output, False to disable.
        

#### `def close(self)`

Resets the channel and closes the NI-DCPower session, releasing all resources.

#### `def configure_and_measure(self, configuration: DCCurrentSourceAndMeasureParameters) -> DCCurrentSourceAndMeasureResultData`

Configures and/or measures DC current. Behavior is set by ``execution_settings``.

        Behavior is controlled by the ``execution_settings`` :
        To source and measure all in one function call:
        - CONFIGURE_SOURCE_AND_MEASURE

        Or use separated steps calls to execute the same flow but sequentially with:
        - CONFIGURE_ONLY
        - START_SOURCE_ONLY
        - MEASURE_ONLY


        Args:
            configuration (DCCurrentSourceAndMeasureParameters): Channel, timing,
                trigger, and execution settings.

        Returns:
            DCCurrentSourceAndMeasureResultData: Hardware execution settings and
                measurement results held in instance state (``_execution_settings`` and
                ``_measurement_results``). Fields not populated by the current execution
                type retain the values set during ``initialize`` (``NaN`` by default).
        

#### `def configure_range_and_terminal(self, current_channel_settings: CurrentChannelSettings) -> None`

Configures the current level, voltage limit, and their respective ranges on the channel.

        Args:
            current_channel_settings (CurrentChannelSettings): Channel settings to apply.
        

#### `def configure_timing_settings(self, timing_parameters: TimingParameters, execution_settings: dict) -> None`

Configures aperture time and transient response based on the instrument model.

        PXIe-4112/4113: aperture time only. PXI-4110/4130/4131A/4154: neither supported
        (``Aperture Time (Sec)`` set to ``NaN``). All other models: both supported.

        Args:
            timing_parameters (TimingParameters): Aperture time and transient response to apply.
            execution_settings (dict): Updated in-place; ``NaN`` set for unsupported models.
        

#### `def configure_trigger_settings(self, trigger_parameters: TriggerParameters) -> None`

Configures source trigger input and event signal routing.

        - ``Start_Source_Trigger``: source waits for a digital edge on ``start_source_name``.
        - ``Route_Event``: exports ``event_signal_to_export`` to ``output_event_signal_terminal``.
        - Not supported on all devices (e.g. NI PXI-4110 raises ``DriverError``).

        Args:
            trigger_parameters (TriggerParameters): Trigger and event routing settings.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dcpower/dc_cc_source_and_measure/dc_cc_source_and_measure_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dcpower/dc_cc_source_and_measure/dc_cc_source_and_measure_constants.py

### MODULE DOCSTRING

Constants for DC constant current source and measure operations.

### `class ConstantsForDCCurrentSourceAndMeasure()`

Default scalar constants for DC current source and measure operations.

- `DEFAULT_DC_CC_EXECUTION_SETTINGS = ExecutionSettings(execution_type=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_EXECUTION_TYPE, skip_analysis=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_SKIP_ANALYSIS)`

- `DEFAULT_DC_CC_CHANNEL_SETTINGS = CurrentChannelSettings(current_level=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_CURRENT_LEVEL_AMPERES, current_level_range=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_CURRENT_LEVEL_RANGE_AMPERES, voltage_limit=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_VOLTAGE_LIMIT_VOLTS, voltage_limit_range=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_VOLTAGE_LIMIT_RANGE_VOLTS, sensing=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_SENSING, enable_output=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_ENABLE_OUTPUT)`

- `DEFAULT_DC_CC_TIMING_PARAMETERS = TimingParameters(source_delay=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_SOURCE_DELAY_SECONDS, aperture_time=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_APERTURE_TIME_SECONDS, transient_response=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_TRANSIENT_RESPONSE)`

- `DEFAULT_DC_CC_TRIGGER_PARAMETERS = TriggerParameters(source_trigger_behavior=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_SOURCE_TRIGGER_BEHAVIOR, start_source_name=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_START_SOURCE_NAME, export_event=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_EXPORT_EVENT, event_signal_to_export=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_EVENT_SIGNAL_TO_EXPORT, output_event_signal_terminal=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_OUTPUT_EVENT_SIGNAL_TERMINAL)`

- `DEFAULT_DC_CC_SOURCE_AND_MEASURE_PARAMETERS = DCCurrentSourceAndMeasureParameters(current_channel_settings=DEFAULT_DC_CC_CHANNEL_SETTINGS, execution_settings=DEFAULT_DC_CC_EXECUTION_SETTINGS, timing_parameters=DEFAULT_DC_CC_TIMING_PARAMETERS, trigger_parameters=DEFAULT_DC_CC_TRIGGER_PARAMETERS)`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dcpower/dc_cc_source_and_measure/dc_cc_source_and_measure_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dcpower/dc_cc_source_and_measure/dc_cc_source_and_measure_data_types.py

### MODULE DOCSTRING

Data types used for DC constant current source and measurement on PCB points.

- `__all__ = ['EventSignalToExport', 'ExecutionSettings', 'ExportEvent', 'MeasurementExecutionType', 'SourceTriggerBehavior', 'TimingParameters', 'TriggerParameters', 'CurrentChannelSettings', 'DCCurrentSourceAndMeasureParameters', 'DCCurrentSourceAndMeasureResultData']`

### `class CurrentChannelSettings()`

Defines the current level, voltage limit, sensing, and output enable
    settings for a channel.
    

#### `def __init__(self, current_level: float, current_level_range: float, voltage_limit: float, voltage_limit_range: float, sensing: nidcpower.Sense, enable_output: bool) -> None`

Initializes the current channel settings.

        Args:
            current_level (float):
                The DC current level to source, in amperes.
            current_level_range (float):
                The current level range setting, in amperes.
            voltage_limit (float):
                The voltage limit for the output, in volts.
            voltage_limit_range (float):
                The voltage limit range setting, in volts.
            sensing (nidcpower.Sense):
                The sensing mode (``LOCAL`` or ``REMOTE``) for voltage measurement.
            enable_output (bool):
                Whether the channel output is enabled.
        

#### `def current_level(self) -> float`

Gets the DC current level to source.

        Returns:
            float: The current level in amperes.
        

#### `def current_level_range(self) -> float`

Gets the current level range.

        Returns:
            float: The current level range in amperes.
        

#### `def voltage_limit(self) -> float`

Gets the voltage limit for the output.

        Returns:
            float: The voltage limit in volts.
        

#### `def voltage_limit_range(self) -> float`

Gets the voltage limit range.

        Returns:
            float: The voltage limit range in volts.
        

#### `def sensing(self) -> nidcpower.Sense`

Gets the sensing mode.

        Returns:
            nidcpower.Sense: The sensing mode (``LOCAL`` or ``REMOTE``).
        

#### `def enable_output(self) -> bool`

Gets whether output is enabled.

        Returns:
            bool: ``True`` if the output is enabled, ``False`` otherwise.
        

### `class DCCurrentSourceAndMeasureParameters(PCBATestToolkitData)`

Defines the full configuration for DC constant current source and measure operation.

#### `def __init__(self, current_channel_settings: CurrentChannelSettings, execution_settings: ExecutionSettings, timing_parameters: TimingParameters, trigger_parameters: TriggerParameters) -> None`

Initializes the DC current source and measure parameters.

        Args:
            current_channel_settings (CurrentChannelSettings):
                Current level, voltage limit, sensing mode, and output enable settings.
            execution_settings (ExecutionSettings):
                Execution mode and analysis control settings.
            timing_parameters (TimingParameters):
                Source delay, aperture time, and transient response settings.
            trigger_parameters (TriggerParameters):
                Source trigger input and event signal routing settings.
        

#### `def current_channel_settings(self) -> CurrentChannelSettings`

Gets the current channel settings.

        Returns:
            CurrentChannelSettings: Configures the current level, voltage limit,
            sensing, and output enable settings.
        

#### `def execution_settings(self) -> ExecutionSettings`

Gets the execution settings.

        Returns:
            ExecutionSettings: Configures the execution mode and skip analysis settings.
        

#### `def timing_parameters(self) -> TimingParameters`

Gets the timing parameters.

        Returns:
            TimingParameters: Configures the source delay, aperture time, and transient
            response settings.
        

#### `def trigger_parameters(self) -> TriggerParameters`

Gets the trigger parameters.

        Returns:
            TriggerParameters: Configures the source trigger input and event signal
            routing settings.
        

### `class DCCurrentSourceAndMeasureResultData(PCBATestToolkitData)`

Defines the results obtained from a DC constant current source and measure operation.

#### `def __init__(self, execution_settings: dict, measurement_results: dict) -> None`

Initializes the DC current source and measure result data.

        Args:
            execution_settings (dict):
                Dictionary containing the applied hardware settings including current level,
                ranges, aperture time, device model, and output function.
                Fields are ``math.nan`` when configuration is not performed.
            measurement_results (dict):
                Dictionary containing the measured values including voltage, current,
                compliance state, power, and resistance.
                Fields are ``math.nan``/``False`` when measurement is not performed.
        

#### `def execution_settings(self) -> dict`

Gets the applied hardware execution settings.

        Returns:
            dict: Applied hardware settings including current level, ranges, aperture time,
                device model, and output function.
        

#### `def measurement_results(self) -> dict`

Gets the measurement results.

        Returns:
            dict: Measured values including voltage, current, compliance state, power,
                and resistance.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dcpower/dc_cv_source_and_measure/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dcpower/dc_cv_source_and_measure/__init__.py

### MODULE DOCSTRING

Provides DC voltage source and measure functionality using SMU and PPS.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dcpower/dc_cv_source_and_measure/dc_cv_source_and_measure.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dcpower/dc_cv_source_and_measure/dc_cv_source_and_measure.py

### MODULE DOCSTRING

Defines class used for DC constant voltage source and measurement on PCB points.

- `_APERTURE_TIME_UNSUPPORTED_MODELS = frozenset({'NI PXI-4110', 'NI PXI-4130', 'NI PXI-4131A', 'NI PXIe-4154'})`

### `class DCVoltageSourceAndMeasure(BuildingBlockUsingNIDCPower)`

Defines a way that allows you to source DC voltage and perform measurements on PCB points.

#### `def initialize(self, resource_name: str)`

Initializes the NI DC Power session with the specified resource.

        Opens a new NI-DCPower session, resets the channel, configures
        the source mode to single-point, and sets the output function to DC voltage.
        Also initializes the ``_execution_settings`` and ``_measurement_results``
        instance dictionaries with ``NaN`` defaults so that state persists across the
        separated ``CONFIGURE_ONLY``, ``START_SOURCE_ONLY``, and ``MEASURE_ONLY`` calls.

        Args:
            resource_name (str): NI-DCPower resource name, e.g. ``"PPS1/0"``.
        

#### `def enable_output(self, enable_output: bool) -> None`

Enables or disables the output of the channel.

        Args:
            enable_output (bool): True to enable output, False to disable.
        

#### `def close(self)`

Resets the channel and closes the NI-DCPower session, releasing all resources.

#### `def configure_and_measure(self, configuration: DCVoltageSourceAndMeasureParameters) -> DCVoltageSourceAndMeasureResultData`

Configures and/or measures DC voltage. Behavior is set by ``execution_settings``.

        Behavior is controlled by the ``execution_settings`` :
        To source and measure all in one function call:
        - CONFIGURE_SOURCE_AND_MEASURE

        Or use separated steps calls to execute the same flow but sequentially with:
        - CONFIGURE_ONLY
        - START_SOURCE_ONLY
        - MEASURE_ONLY


        Args:
            configuration (DCVoltageSourceAndMeasureParameters): Channel, timing,
                trigger, and execution settings.

        Returns:
            DCVoltageSourceAndMeasureResultData: Hardware execution settings and
                measurement results held in instance state (``_execution_settings`` and
                ``_measurement_results``). Fields not populated by the current execution
                type retain the values set during ``initialize`` (``NaN`` by default).
        

#### `def configure_range_and_terminal(self, voltage_channel_settings: VoltageChannelSettings) -> None`

Configures the voltage level, current limit, and their respective ranges on the channel.

        Args:
            voltage_channel_settings (VoltageChannelSettings): Channel settings to apply.
        

#### `def configure_timing_settings(self, timing_parameters: TimingParameters, execution_settings: dict) -> None`

Configures aperture time and transient response based on the instrument model.

        PXIe-4112/4113: aperture time only. PXI-4110/4130/4131A/4154: neither supported
        (``Aperture Time (Sec)`` set to ``NaN``). All other models: both supported.

        Args:
            timing_parameters (TimingParameters): Aperture time and transient response to apply.
            execution_settings (dict): Updated in-place; ``NaN`` set for unsupported models.
        

#### `def configure_trigger_settings(self, trigger_parameters: TriggerParameters) -> None`

Configures source trigger input and event signal routing.

        - ``Start_Source_Trigger``: source waits for a digital edge on ``start_source_name``.
        - ``Route_Event``: exports ``event_signal_to_export`` to ``output_event_signal_terminal``.
        - Not supported on all devices (e.g. NI PXI-4110 raises ``DriverError``).

        Args:
            trigger_parameters (TriggerParameters): Trigger and event routing settings.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dcpower/dc_cv_source_and_measure/dc_cv_source_and_measure_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dcpower/dc_cv_source_and_measure/dc_cv_source_and_measure_constants.py

### MODULE DOCSTRING

Constants for DC constant voltage source and measure operations.

### `class ConstantsForDCVoltageSourceAndMeasure()`

Default scalar constants for DC voltage source and measure operations.

- `DEFAULT_DC_CV_EXECUTION_SETTINGS = ExecutionSettings(execution_type=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_EXECUTION_TYPE, skip_analysis=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_SKIP_ANALYSIS)`

- `DEFAULT_DC_CV_CHANNEL_SETTINGS = VoltageChannelSettings(voltage_level=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_VOLTAGE_LEVEL_VOLTS, voltage_level_range=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_VOLTAGE_LEVEL_RANGE_VOLTS, current_limit=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_CURRENT_LIMIT_AMPERES, current_limit_range=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_CURRENT_LIMIT_RANGE_AMPERES, sensing=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_SENSING, enable_output=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_ENABLE_OUTPUT)`

- `DEFAULT_DC_CV_TIMING_PARAMETERS = TimingParameters(source_delay=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_SOURCE_DELAY_SECONDS, aperture_time=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_APERTURE_TIME_SECONDS, transient_response=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_TRANSIENT_RESPONSE)`

- `DEFAULT_DC_CV_TRIGGER_PARAMETERS = TriggerParameters(source_trigger_behavior=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_SOURCE_TRIGGER_BEHAVIOR, start_source_name=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_START_SOURCE_NAME, export_event=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_EXPORT_EVENT, event_signal_to_export=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_EVENT_SIGNAL_TO_EXPORT, output_event_signal_terminal=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_OUTPUT_EVENT_SIGNAL_TERMINAL)`

- `DEFAULT_DC_CV_SOURCE_AND_MEASURE_PARAMETERS = DCVoltageSourceAndMeasureParameters(voltage_channel_settings=DEFAULT_DC_CV_CHANNEL_SETTINGS, execution_settings=DEFAULT_DC_CV_EXECUTION_SETTINGS, timing_parameters=DEFAULT_DC_CV_TIMING_PARAMETERS, trigger_parameters=DEFAULT_DC_CV_TRIGGER_PARAMETERS)`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dcpower/dc_cv_source_and_measure/dc_cv_source_and_measure_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dcpower/dc_cv_source_and_measure/dc_cv_source_and_measure_data_types.py

### MODULE DOCSTRING

Data types used for DC constant voltage source and measurement on PCB points.

- `__all__ = ['EventSignalToExport', 'ExecutionSettings', 'ExportEvent', 'MeasurementExecutionType', 'SourceTriggerBehavior', 'TimingParameters', 'TriggerParameters', 'VoltageChannelSettings', 'DCVoltageSourceAndMeasureParameters', 'DCVoltageSourceAndMeasureResultData']`

### `class VoltageChannelSettings()`

Defines the voltage level, current limit, sensing, and output enable
    settings for a channel.
    

#### `def __init__(self, voltage_level: float, voltage_level_range: float, current_limit: float, current_limit_range: float, sensing: nidcpower.Sense, enable_output: bool) -> None`

Initializes the voltage channel settings.

        Args:
            voltage_level (float):
                The DC voltage level to source, in volts.
            voltage_level_range (float):
                The voltage level range setting, in volts.
            current_limit (float):
                The current limit for the output, in amperes.
            current_limit_range (float):
                The current limit range setting, in amperes.
            sensing (nidcpower.Sense):
                The sensing mode (``LOCAL`` or ``REMOTE``) for voltage measurement.
            enable_output (bool):
                Whether the channel output is enabled.
        

#### `def voltage_level(self) -> float`

Gets the DC voltage level to source.

        Returns:
            float: The voltage level in volts.
        

#### `def voltage_level_range(self) -> float`

Gets the voltage level range.

        Returns:
            float: The voltage level range in volts.
        

#### `def current_limit(self) -> float`

Gets the current limit for the output.

        Returns:
            float: The current limit in amperes.
        

#### `def current_limit_range(self) -> float`

Gets the current limit range.

        Returns:
            float: The current limit range in amperes.
        

#### `def sensing(self) -> nidcpower.Sense`

Gets the sensing mode.

        Returns:
            nidcpower.Sense: The sensing mode (``LOCAL`` or ``REMOTE``).
        

#### `def enable_output(self) -> bool`

Gets whether output is enabled.

        Returns:
            bool: ``True`` if the output is enabled, ``False`` otherwise.
        

### `class DCVoltageSourceAndMeasureParameters(PCBATestToolkitData)`

Defines the full configuration for DC constant voltage source and measure operation.

#### `def __init__(self, voltage_channel_settings: VoltageChannelSettings, execution_settings: ExecutionSettings, timing_parameters: TimingParameters, trigger_parameters: TriggerParameters) -> None`

Initializes the DC voltage source and measure parameters.

        Args:
            voltage_channel_settings (VoltageChannelSettings):
                Voltage level, current limit, sensing mode, and output enable settings.
            execution_settings (ExecutionSettings):
                Execution mode and analysis control settings.
            timing_parameters (TimingParameters):
                Source delay, aperture time, and transient response settings.
            trigger_parameters (TriggerParameters):
                Source trigger input and event signal routing settings.
        

#### `def voltage_channel_settings(self) -> VoltageChannelSettings`

Gets the voltage channel settings.

        Returns:
            VoltageChannelSettings: Configures the voltage level, current limit,
            sensing, and output enable settings.
        

#### `def execution_settings(self) -> ExecutionSettings`

Gets the execution settings.

        Returns:
            ExecutionSettings: Configures the execution mode and skip analysis settings.
        

#### `def timing_parameters(self) -> TimingParameters`

Gets the timing parameters.

        Returns:
            TimingParameters: Configures the source delay, aperture time, and transient
            response settings.
        

#### `def trigger_parameters(self) -> TriggerParameters`

Gets the trigger parameters.

        Returns:
            TriggerParameters: Configures the source trigger input and event signal
            routing settings.
        

### `class DCVoltageSourceAndMeasureResultData(PCBATestToolkitData)`

Defines the results obtained from a DC constant voltage source and measure operation.

#### `def __init__(self, execution_settings: dict, measurement_results: dict) -> None`

Initializes the DC voltage source and measure result data.

        Args:
            execution_settings (dict):
                Dictionary containing the applied hardware settings including voltage level,
                ranges, aperture time, device model, and output function.
                Fields are ``math.nan`` when configuration is not performed.
            measurement_results (dict):
                Dictionary containing the measured values including voltage, current,
                compliance state, power, and resistance.
                Fields are ``math.nan``/``False`` when measurement is not performed.
        

#### `def execution_settings(self) -> dict`

Gets the applied hardware execution settings.

        Returns:
            dict: Applied hardware settings including voltage level, ranges, aperture time,
                device model, and output function.
        

#### `def measurement_results(self) -> dict`

Gets the measurement results.

        Returns:
            dict: Measured values including voltage, current, compliance state, power,
                and resistance.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dmm/__init__.py

### MODULE DOCSTRING

Contains DMM modules for pcbatt library.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/common/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dmm/common/__init__.py

### MODULE DOCSTRING

Provides common data types, constants, and helper functions for DMM measurements.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/common/common_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dmm/common/common_data_types.py

### MODULE DOCSTRING

Common data types for DMM measurements.

### `class ResolutionInDigits(Enum)`

Defines the resolution settings for DMM measurements.

### `class Slope(Enum)`

Defines the slope settings for DMM measurements.

### `class TriggerParameters()`

Parameters for configuring trigger settings in DMM measurements.

#### `def __init__(self, trigger_source: nidmm.TriggerSource, trigger_delay: float, slope: Slope, enable_trigger: bool) -> None`

Initializes the trigger parameters.

        Args:
            trigger_source (nidmm.TriggerSource):
                The trigger source for the measurement.
            trigger_delay (float):
                The delay in seconds between the trigger and the start of measurement.
            slope (Slope):
                The trigger slope (rising or falling edge).
            enable_trigger (bool):
                Whether triggering is enabled for the measurement.
        

#### `def trigger_source(self) -> nidmm.TriggerSource`

Gets the trigger source.

        Returns:
            nidmm.TriggerSource: The trigger source for the measurement.
        

#### `def trigger_delay(self) -> float`

Gets the trigger delay.

        Returns:
            float: The delay in seconds between trigger and measurement start.
        

#### `def trigger_slope(self) -> Slope`

Gets the trigger slope.

        Returns:
            Slope: The trigger slope (rising or falling edge).
        

#### `def enable_trigger(self) -> bool`

Gets whether triggering is enabled.

        Returns:
            bool: True if triggering is enabled, False otherwise.
        

### `class TimingParameters()`

Parameters for configuring timing settings in DMM measurements.

#### `def __init__(self, aperture_time_seconds: float, settle_time_seconds: float) -> None`

Initializes the timing parameters.

        Args:
            aperture_time_seconds (float):
                The aperture time in seconds for the measurement.
            settle_time_seconds (float):
                The settle time in seconds before taking a measurement.
        

#### `def aperture_time_seconds(self) -> float`

Gets the aperture time.

        Returns:
            float: The aperture time in seconds.
        

#### `def settle_time_seconds(self) -> float`

Gets the settle time.

        Returns:
            float: The settle time in seconds.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/common/constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dmm/common/constants.py

### MODULE DOCSTRING

Constants for DMM measurements.

### `class ConstantsForDcRmsMeasurements()`

Encapsulates the constants for DMM measurements.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/common/helper_functions.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dmm/common/helper_functions.py

### MODULE DOCSTRING

Helper functions and classes for DMM measurement operations.

### `class RangeAndMeasurementFunctionParameters()`

Extracts measurement function and range from enum values with tuple format.

#### `def __init__(self, range_function: Enum)`

Initialize with an enum that has tuple values (function, range).

        Args:
            range_function: Enum with value as (nidmm.Function, float)
        

#### `def measurement_function(self) -> nidmm.Function`

Returns the measurement function extracted from the enum.

        Returns:
            nidmm.Function: The measurement function
        

#### `def range_value(self) -> float`

Returns the range value extracted from the enum.

        Returns:
            float: The measurement range value
        

### `class FormatMeasurement()`

Formats measurement results based on resolution in digits.

#### `def format_with_si_prefix(measured_value: float, total_digits: int) -> tuple[str, str]`

Formats a value in engineering notation with SI prefix.

        Args:
            measured_value: The numerical value to format
            total_digits: Total number of significant digits to display

        Returns:
            tuple: (formatted_number, si_prefix)
                - formatted_number: The scaled value as a string with appropriate decimal places
                - si_prefix: The SI prefix symbol (e.g., 'k', 'M', 'u', 'm') or exponential notation
        

#### `def measurement(resolution_in_digits: float, measured_value: float, measurement_function: nidmm.Function=None) -> dict`

Formats the measurement value according to the specified resolution.

        Args:
            resolution_in_digits: Resolution in digits (e.g., 6.5 for 6.5 digit resolution)
            measured_value: The measured value to format
            measurement_function: Optional nidmm.Function to append appropriate unit

        Returns:
            dict: Dictionary containing:
                - 'Formatted_Measurement': Human-readable string with SI prefix and unit
                - 'Measured_Value': Original raw measured value
                - 'Unit': Base unit symbol
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/dc_rms_current_measurements/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dmm/dc_rms_current_measurements/__init__.py

### MODULE DOCSTRING

Provides DC and RMS current measurement functionality using DMM.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/dc_rms_current_measurements/dc_rms_current_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dmm/dc_rms_current_measurements/dc_rms_current_constants.py

### MODULE DOCSTRING

Constants for DC-RMS Current Measurements.

### `class ConstantsForDcRmsCurrentMeasurements()`

Constants used for Current measurement.

- `DEFAULT_DC_RMS_CURRENT_EXECUTION_TYPE = ConstantsForDcRmsMeasurements.DEFAULT_EXECUTION_TYPE`

- `DEFAULT_DC_RMS_CURRENT_MEASUREMENT_PARAMETERS = DcRmsCurrentMeasurementFunctionParameters(measurement_function=ConstantsForDcRmsCurrentMeasurements.RANGE_AND_FUNCTION, resolution_in_digits=ConstantsForDcRmsMeasurements.DEFAULT_RESOLUTION_IN_DIGITS)`

- `DEFAULT_DC_RMS_CURRENT_TIMING_PARAMETERS = TimingParameters(aperture_time_seconds=ConstantsForDcRmsMeasurements.DEFAULT_APERTURE_TIME_SECONDS, settle_time_seconds=ConstantsForDcRmsMeasurements.DEFAULT_SETTLE_TIME_SECONDS)`

- `DEFAULT_DC_RMS_CURRENT_AC_MIN_FREQUENCY = ConstantsForDcRmsMeasurements.DEFAULT_AC_MIN_FREQUENCY`

- `DEFAULT_DC_RMS_CURRENT_TRIGGER_PARAMETERS = TriggerParameters(trigger_source=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_SOURCE, trigger_delay=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_DELAY, slope=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_SLOPE, enable_trigger=ConstantsForDcRmsMeasurements.DEFAULT_ENABLE_TRIGGER)`

- `DEFAULT_DC_RMS_CURRENT_MEASUREMENT_CONFIGURATION = DcRmsCurrentMeasurementConfiguration(execution_type=DEFAULT_DC_RMS_CURRENT_EXECUTION_TYPE, measurement_function_parameters=DEFAULT_DC_RMS_CURRENT_MEASUREMENT_PARAMETERS, trigger_parameters=DEFAULT_DC_RMS_CURRENT_TRIGGER_PARAMETERS, timing_parameters=DEFAULT_DC_RMS_CURRENT_TIMING_PARAMETERS, ac_min_frequency=DEFAULT_DC_RMS_CURRENT_AC_MIN_FREQUENCY)`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/dc_rms_current_measurements/dc_rms_current_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dmm/dc_rms_current_measurements/dc_rms_current_data_types.py

### MODULE DOCSTRING

DC-RMS current data types.

### `class CurrentRangeAndFunctions(Enum)`

Defines the measurement function and range settings for current measurement.

### `class DcRmsCurrentMeasurementFunctionParameters()`

Defines parameters used for configuration of DC-RMS current measurement.

#### `def __init__(self, measurement_function: CurrentRangeAndFunctions, resolution_in_digits: ResolutionInDigits) -> None`

Initializes measurement function parameters.

        Args:
            measurement_function (CurrentRangeAndFunctions):
                The current measurement function and range setting.
            resolution_in_digits (ResolutionInDigits):
                The measurement resolution in digits.
        

#### `def measurement_function(self) -> CurrentRangeAndFunctions`

Gets the current measurement function and range setting.

        Returns:
            CurrentRangeAndFunctions: The configured current range and function.
        

#### `def resolution_in_digits(self) -> ResolutionInDigits`

Gets the measurement resolution in digits.

        Returns:
            ResolutionInDigits: The configured resolution setting.
        

### `class DcRmsCurrentMeasurementConfiguration(PCBATestToolkitData)`

Defines configuration parameters for current DC-RMS measurements.

#### `def __init__(self, execution_type: MeasurementExecutionType, measurement_function_parameters: DcRmsCurrentMeasurementFunctionParameters, trigger_parameters: TriggerParameters, timing_parameters: TimingParameters, ac_min_frequency: float) -> None`

Initializes the current measurement configuration.

        Args:
            execution_type (MeasurementExecutionType):
                Specifies whether to configure only, measure only, or both configure and measure.
            measurement_function_parameters (DcRmsCurrentMeasurementFunctionParameters):
                The measurement function settings including current range and resolution.
            trigger_parameters (TriggerParameters):
                Trigger configuration including source, delay, and enable/disable settings.
            timing_parameters (TimingParameters):
                Timing settings including aperture time and settle time.
            ac_min_frequency (float):
                Minimum frequency for AC current measurements in Hz (ignored for DC measurements).
        

#### `def execution_type(self) -> MeasurementExecutionType`

Gets the measurement execution type.

        Returns:
            MeasurementExecutionType: The execution mode (configure only, measure only, or both).
        

#### `def trigger_parameters(self) -> TriggerParameters`

Gets the trigger configuration parameters.

        Returns:
            TriggerParameters: The trigger settings for the measurement.
        

#### `def measurement_function_parameters(self) -> DcRmsCurrentMeasurementFunctionParameters`

Gets the measurement function parameters.

        Returns:
            DcRmsCurrentMeasurementFunctionParameters: The current range, function,
            and resolution settings.
        

#### `def timing_parameters(self) -> TimingParameters`

Gets the timing configuration parameters.

        Returns:
            TimingParameters: The aperture time and settle time settings.
        

#### `def ac_min_frequency(self) -> float`

Gets the minimum AC frequency setting.

        Returns:
            float: The minimum frequency for AC current measurements.
        

### `class DcRmsCurrentMeasurementResultData(PCBATestToolkitData)`

Defines current DC-RMS results obtained from DMM DC-RMS Current Measurement.

#### `def __init__(self, dmm_execution_settings: dict, measurement: Union[dict, None]) -> None`

Initializes the current measurement result data.

        Args:
            dmm_execution_settings (dict):
                Dictionary containing the DMM configuration used during measurement.
            measurement (dict | None):
                Dictionary containing the measurement results,
                or None if only configuration was performed.
        

#### `def dmm_execution_settings(self) -> dict`

Gets the DMM execution settings used during the measurement.

        Returns:
            dict: Dictionary with labeled keys and values including units for each setting.
        

#### `def measurement(self) -> Union[dict, None]`

Gets the measurement result data.

        Returns:
            dict | None: Dictionary containing 'Measured_Value', 'Unit', and
                'Formatted_Measurement' keys, or None if only configuration was performed.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/dc_rms_current_measurements/dc_rms_current_measurement.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dmm/dc_rms_current_measurements/dc_rms_current_measurement.py

### MODULE DOCSTRING

Defines class used for DC-RMS current measurement on PCB points.

### `class DcRmsCurrentMeasurement(BuildingBlockUsingNIDMM)`

Defines a way that allows you to perform DC-RMS current measurements on PCB points.

#### `def initialize(self, dmm_resource_name: str, powerline_frequency: float)`

Initializes the DMM session with the specific resource name and powerline frequency.

        Args:
            dmm_resource_name (str):
                The resource name of the DMM device to use for measurements.
            powerline_frequency (float):
                The powerline frequency in Hz.
        

#### `def configure_and_measure(self, configuration: DcRmsCurrentMeasurementConfiguration) -> Union[DcRmsCurrentMeasurementResultData, None]`

Configures and/or performs a measurement according to specific configuration parameters.

        Args:
            configuration (DcRmsCurrentMeasurementConfiguration):
                An instance of `DcRmsCurrentMeasurementConfiguration` used to configure
                the measurement.

        Returns:
            DcRmsCurrentMeasurementResultData | None: An instance of
                `DcRmsCurrentMeasurementResultData` containing DMM execution settings
                and the measured current value, or None if only configuration was performed.
        

#### `def close(self)`

Closes measurement procedure and releases internal resources.

#### `def configure_measurement_function(self, parameters: DcRmsCurrentMeasurementFunctionParameters)`

Configures the measurement function settings for the DMM.

        Args:
            parameters (DcRmsCurrentMeasurementFunctionParameters):
                An instance of `DcRmsCurrentMeasurementFunctionParameters` containing the
                measurement function type (DC/AC current) and resolution in digits to configure.
        

#### `def configure_trigger(self, parameters: TriggerParameters)`

Configure the characteristics of triggers used for current measurements.

        Args:
            parameters (TriggerParameters):
                An instance of `TriggerParameters` containing trigger source,
                trigger delay, slope, and enable/disable flag.
        

#### `def configure_timing(self, parameters: TimingParameters)`

Configures the timing characteristics used for current measurements.

        Args:
            parameters (TimingParameters):
                An instance of `TimingParameters` containing aperture time and
                settle time settings.
        

#### `def acquire_measurement(self, resolution_in_digits: float) -> DcRmsCurrentMeasurementResultData`

Acquires and formats the measurement result data.

        Args:
            resolution_in_digits (float):
                The resolution in digits used for formatting the measured value.

        Returns:
            DcRmsCurrentMeasurementResultData:
                An instance of `DcRmsCurrentMeasurementResultData` containing:
                - dmm_execution_settings: Dictionary with keys 'Function', 'Range',
                  'Digits_Resolution', 'Aperture_Time(s)', 'Settle_Time(s)',
                  'Minimum_Frequency(Hz)', 'Absolute_Resolution',
                  'Input_Resistance(Ohm)', and 'Auto_Range_Value'
                - measurement: Dictionary with keys 'Measured_Value', 'Unit', and
                  'Formatted_Measurement'
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/dc_rms_voltage_measurements/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dmm/dc_rms_voltage_measurements/__init__.py

### MODULE DOCSTRING

Provides DC and RMS voltage measurement functionality using DMM.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/dc_rms_voltage_measurements/dc_rms_voltage_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dmm/dc_rms_voltage_measurements/dc_rms_voltage_constants.py

### MODULE DOCSTRING

Constants for DC-RMS Voltage Measurements.

### `class ConstantsForDcRmsVoltageMeasurements()`

Constants used for Voltage measurement.

- `DEFAULT_DC_RMS_VOLTAGE_EXECUTION_TYPE = ConstantsForDcRmsMeasurements.DEFAULT_EXECUTION_TYPE`

- `DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_PARAMETERS = DcRmsVoltageMeasurementFunctionParameters(measurement_function=ConstantsForDcRmsVoltageMeasurements.RANGE_AND_FUNCTION, resolution_in_digits=ConstantsForDcRmsMeasurements.DEFAULT_RESOLUTION_IN_DIGITS)`

- `DEFAULT_DC_RMS_VOLTAGE_TIMING_PARAMETERS = TimingParameters(aperture_time_seconds=ConstantsForDcRmsMeasurements.DEFAULT_APERTURE_TIME_SECONDS, settle_time_seconds=ConstantsForDcRmsMeasurements.DEFAULT_SETTLE_TIME_SECONDS)`

- `DEFAULT_DC_RMS_VOLTAGE_AC_MIN_FREQUENCY = ConstantsForDcRmsMeasurements.DEFAULT_AC_MIN_FREQUENCY`

- `DEFAULT_DC_RMS_VOLTAGE_TRIGGER_PARAMETERS = TriggerParameters(trigger_source=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_SOURCE, trigger_delay=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_DELAY, slope=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_SLOPE, enable_trigger=ConstantsForDcRmsMeasurements.DEFAULT_ENABLE_TRIGGER)`

- `DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION = DcRmsVoltageMeasurementConfiguration(execution_type=DEFAULT_DC_RMS_VOLTAGE_EXECUTION_TYPE, measurement_function_parameters=DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_PARAMETERS, trigger_parameters=DEFAULT_DC_RMS_VOLTAGE_TRIGGER_PARAMETERS, timing_parameters=DEFAULT_DC_RMS_VOLTAGE_TIMING_PARAMETERS, ac_min_frequency=DEFAULT_DC_RMS_VOLTAGE_AC_MIN_FREQUENCY)`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/dc_rms_voltage_measurements/dc_rms_voltage_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dmm/dc_rms_voltage_measurements/dc_rms_voltage_data_types.py

### MODULE DOCSTRING

DC-RMS voltage data types.

### `class VoltageRangeAndFunctions(Enum)`

Defines the measurement function and range settings for voltage measurement.

### `class DcRmsVoltageMeasurementFunctionParameters(PCBATestToolkitData)`

Defines parameters used for configuration of DC-RMS voltage measurement.

#### `def __init__(self, measurement_function: VoltageRangeAndFunctions, resolution_in_digits: ResolutionInDigits) -> None`

Initializes measurement function parameters.

        Args:
            measurement_function (VoltageRangeAndFunctions):
                The voltage measurement function and range setting.
            resolution_in_digits (ResolutionInDigits):
                The measurement resolution in digits.
        

#### `def measurement_function(self) -> VoltageRangeAndFunctions`

Gets the voltage measurement function and range setting.

        Returns:
            VoltageRangeAndFunctions: The configured voltage range and function.
        

#### `def resolution_in_digits(self) -> ResolutionInDigits`

Gets the measurement resolution in digits.

        Returns:
            ResolutionInDigits: The configured resolution setting.
        

### `class DcRmsVoltageMeasurementConfiguration(PCBATestToolkitData)`

Defines configuration parameters for voltage DC-RMS measurements.

#### `def __init__(self, execution_type: MeasurementExecutionType, measurement_function_parameters: DcRmsVoltageMeasurementFunctionParameters, trigger_parameters: TriggerParameters, timing_parameters: TimingParameters, ac_min_frequency: float) -> None`

Initializes the voltage measurement configuration.

        Args:
            execution_type (MeasurementExecutionType):
                Specifies whether to configure only, measure only, or both configure and measure.
            measurement_function_parameters (DcRmsVoltageMeasurementFunctionParameters):
                The measurement function settings including voltage range and resolution.
            trigger_parameters (TriggerParameters):
                Trigger configuration including source, delay, and enable/disable settings.
            timing_parameters (TimingParameters):
                Timing settings including aperture time and settle time.
            ac_min_frequency (float):
                Minimum frequency for AC voltage measurements in Hz (ignored for DC measurements).
        

#### `def execution_type(self) -> MeasurementExecutionType`

Gets the measurement execution type.

        Returns:
            MeasurementExecutionType: The execution mode (configure only, measure only, or both).
        

#### `def trigger_parameters(self) -> TriggerParameters`

Gets the trigger configuration parameters.

        Returns:
            TriggerParameters: The trigger settings for the measurement.
        

#### `def measurement_function_parameters(self) -> DcRmsVoltageMeasurementFunctionParameters`

Gets the measurement function parameters.

        Returns:
            DcRmsVoltageMeasurementFunctionParameters: The voltage range, function,
            and resolution settings.
        

#### `def timing_parameters(self) -> TimingParameters`

Gets the timing configuration parameters.

        Returns:
            TimingParameters: The aperture time and settle time settings.
        

#### `def ac_min_frequency(self) -> float`

Gets the minimum AC frequency setting.

        Returns:
            float: The minimum frequency for AC voltage measurements.
        

### `class DcRmsVoltageMeasurementResultData(PCBATestToolkitData)`

Defines voltage DC-RMS results obtained from DMM DC-RMS Voltage Measurement.

#### `def __init__(self, dmm_execution_settings: dict, measurement: Union[dict, None]) -> None`

Initializes the voltage measurement result data.

        Args:
            dmm_execution_settings (dict):
                Dictionary containing the DMM configuration used during measurement.
            measurement (dict | None):
                Dictionary containing the measurement results,
                or None if only configuration was performed.
        

#### `def dmm_execution_settings(self) -> dict`

Gets the DMM execution settings used during the measurement.

        Returns:
            dict: Dictionary with labeled keys and values including units for each setting.
        

#### `def measurement(self) -> Union[dict, None]`

Gets the measurement result data.

        Returns:
            dict | None: Dictionary containing 'Measured_Value', 'Unit', and
                'Formatted_Measurement' keys, or None if only configuration was performed.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/dc_rms_voltage_measurements/dc_rms_voltage_measurement.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dmm/dc_rms_voltage_measurements/dc_rms_voltage_measurement.py

### MODULE DOCSTRING

Defines class used for DC-RMS Voltage measurement on PCB points.

### `class DcRmsVoltageMeasurement(BuildingBlockUsingNIDMM)`

Defines a way that allows you to perform DC-RMS voltage measurements on PCB points.

#### `def initialize(self, dmm_resource_name: str, powerline_frequency: float)`

Initializes the DMM session with the specific resource name and powerline frequency.

        Args:
            dmm_resource_name (str):
                The resource name of the DMM device to use for measurements.
            powerline_frequency (float):
                The powerline frequency in Hz.
        

#### `def configure_and_measure(self, configuration: DcRmsVoltageMeasurementConfiguration) -> Union[DcRmsVoltageMeasurementResultData, None]`

Configures and/or performs a measurement according to specific configuration parameters.

        Args:
            configuration (DcRmsVoltageMeasurementConfiguration):
                An instance of `DcRmsVoltageMeasurementConfiguration` used to configure
                the measurement.

        Returns:
            DcRmsVoltageMeasurementResultData | None: An instance of
                `DcRmsVoltageMeasurementResultData` containing DMM execution settings
                and the measured voltage value, or None if only configuration was performed.
        

#### `def close(self)`

Closes measurement procedure and releases internal resources.

#### `def configure_measurement_function(self, parameters: DcRmsVoltageMeasurementFunctionParameters)`

Configures the measurement function settings for the DMM.

        Args:
            parameters (DcRmsVoltageMeasurementFunctionParameters):
                An instance of `DcRmsVoltageMeasurementFunctionParameters` containing the
                measurement function type (DC/AC voltage) and resolution in digits to configure.
        

#### `def configure_trigger(self, parameters: TriggerParameters)`

Configure the characteristics of triggers used for voltage measurements.

        Args:
            parameters (TriggerParameters):
                An instance of `TriggerParameters` containing trigger source,
                trigger delay, slope, and enable/disable flag.
        

#### `def configure_timing(self, parameters: TimingParameters)`

Configures the timing characteristics used for voltage measurements.

        Args:
            parameters (TimingParameters):
                An instance of `TimingParameters` containing aperture time and
                settle time settings.
        

#### `def acquire_measurement(self, resolution_in_digits: float) -> DcRmsVoltageMeasurementResultData`

Acquires and formats the measurement result data.

        Args:
            resolution_in_digits (float):
                The resolution in digits used for formatting the measured value.

        Returns:
            DcRmsVoltageMeasurementResultData:
                An instance of `DcRmsVoltageMeasurementResultData` containing:
                - dmm_execution_settings: Dictionary with keys 'Function', 'Range',
                  'Digits_Resolution', 'Aperture_Time(s)', 'Settle_Time(s)',
                  'Minimum_Frequency(Hz)', 'Absolute_Resolution',
                  'Input_Resistance(Ohm)', and 'Auto_Range_Value'
                - measurement: Dictionary with keys 'Measured_Value', 'Unit', and
                  'Formatted_Measurement'
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/mixed_measurements/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dmm/mixed_measurements/__init__.py

### MODULE DOCSTRING

Provides mixed measurement functionality using DMM.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/mixed_measurements/mixed_measurement.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dmm/mixed_measurements/mixed_measurement.py

### MODULE DOCSTRING

Defines class used for mixed measurement on PCB points.

### `class MixedMeasurement(BuildingBlockUsingNIDMM)`

Defines a way that allows you to perform mixed measurements on PCB points.

#### `def initialize(self, dmm_resource_name: str, powerline_frequency: float)`

Initializes the DMM session with the specific resource name and powerline frequency.

        Args:
            dmm_resource_name (str):
                The resource name of the DMM device to use for measurements.
            powerline_frequency (float):
                The powerline frequency in Hz.
        

#### `def configure_and_measure(self, configuration: MixedMeasurementConfiguration) -> Union[MixedMeasurementResultData, None]`

Configures and/or performs a measurement according to specific configuration parameters.

        Args:
            configuration (MixedMeasurementConfiguration):
                An instance of `MixedMeasurementConfiguration` used to configure
                the measurement.

        Returns:
            MixedMeasurementResultData | None: An instance of
                `MixedMeasurementResultData` containing DMM execution settings
                and the measured value, or None if only configuration was performed.
        

#### `def close(self)`

Closes measurement procedure and releases internal resources.

#### `def configure_measurement_function(self, parameters: MixedMeasurementFunctionParameters)`

Configures the measurement function settings for the DMM.

        Args:
            parameters (MixedMeasurementFunctionParameters):
                An instance of `MixedMeasurementFunctionParameters` containing the
                measurement function type and resolution in digits to configure.
        

#### `def configure_trigger(self, parameters: TriggerParameters)`

Configure the characteristics of triggers used for mixed measurements.

        Args:
            parameters (TriggerParameters):
                An instance of `TriggerParameters` containing trigger source,
                trigger delay, slope, and enable/disable flag.
        

#### `def configure_timing(self, parameters: TimingParameters)`

Configures the timing characteristics used for mixed measurements.

        Args:
            parameters (TimingParameters):
                An instance of `TimingParameters` containing aperture time and
                settle time settings.
        

#### `def acquire_measurement(self, resolution_in_digits: float) -> MixedMeasurementResultData`

Acquires and formats the measurement result data.

        Args:
            resolution_in_digits (float):
                The resolution in digits used for formatting the measured value.

        Returns:
            MixedMeasurementResultData:
                An instance of `MixedMeasurementResultData` containing:
                - dmm_execution_settings: Dictionary with keys 'Function', 'Range',
                  'Digits_Resolution', 'Aperture_Time(s)', 'Settle_Time(s)',
                  'Minimum_Frequency(Hz)', 'Absolute_Resolution',
                  'Input_Resistance(Ohm)', and 'Auto_Range_Value'
                - measurement: Dictionary with keys 'Measured_Value', 'Unit', and
                  'Formatted_Measurement'
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/mixed_measurements/mixed_measurement_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dmm/mixed_measurements/mixed_measurement_constants.py

### MODULE DOCSTRING

Constants for Mixed Measurements.

### `class ConstantsForMixedMeasurements()`

Constants used for Mixed measurement.

- `DEFAULT_MIXED_EXECUTION_TYPE = ConstantsForDcRmsMeasurements.DEFAULT_EXECUTION_TYPE`

- `DEFAULT_MIXED_MEASUREMENT_PARAMETERS = MixedMeasurementFunctionParameters(measurement_function=ConstantsForMixedMeasurements.RANGE_AND_FUNCTION, resolution_in_digits=ConstantsForDcRmsMeasurements.DEFAULT_RESOLUTION_IN_DIGITS)`

- `DEFAULT_MIXED_TIMING_PARAMETERS = TimingParameters(aperture_time_seconds=ConstantsForDcRmsMeasurements.DEFAULT_APERTURE_TIME_SECONDS, settle_time_seconds=ConstantsForDcRmsMeasurements.DEFAULT_SETTLE_TIME_SECONDS)`

- `DEFAULT_MIXED_AC_MIN_FREQUENCY = ConstantsForDcRmsMeasurements.DEFAULT_AC_MIN_FREQUENCY`

- `DEFAULT_MIXED_TRIGGER_PARAMETERS = TriggerParameters(trigger_source=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_SOURCE, trigger_delay=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_DELAY, slope=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_SLOPE, enable_trigger=ConstantsForDcRmsMeasurements.DEFAULT_ENABLE_TRIGGER)`

- `DEFAULT_MIXED_MEASUREMENT_CONFIGURATION = MixedMeasurementConfiguration(execution_type=DEFAULT_MIXED_EXECUTION_TYPE, measurement_function_parameters=DEFAULT_MIXED_MEASUREMENT_PARAMETERS, trigger_parameters=DEFAULT_MIXED_TRIGGER_PARAMETERS, timing_parameters=DEFAULT_MIXED_TIMING_PARAMETERS, ac_min_frequency=DEFAULT_MIXED_AC_MIN_FREQUENCY)`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/mixed_measurements/mixed_measurement_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dmm/mixed_measurements/mixed_measurement_data_types.py

### MODULE DOCSTRING

Mixed measurement data types.

### `class MixedRangeAndFunctions(Enum)`

Defines the measurement function and range settings for mixed measurement.

### `class MixedMeasurementFunctionParameters()`

Defines parameters used for configuration of mixed measurement.

#### `def __init__(self, measurement_function: MixedRangeAndFunctions, resolution_in_digits: ResolutionInDigits) -> None`

Initializes measurement function parameters.

        Args:
            measurement_function (MixedRangeAndFunctions):
                The mixed measurement function and range setting.
            resolution_in_digits (ResolutionInDigits):
                The measurement resolution in digits.
        

#### `def measurement_function(self) -> MixedRangeAndFunctions`

Gets the mixed measurement function and range setting.

        Returns:
            MixedRangeAndFunctions: The configured mixed range and function.
        

#### `def resolution_in_digits(self) -> ResolutionInDigits`

Gets the measurement resolution in digits.

        Returns:
            ResolutionInDigits: The configured resolution setting.
        

### `class MixedMeasurementConfiguration(PCBATestToolkitData)`

Defines configuration parameters for mixed measurements.

#### `def __init__(self, execution_type: MeasurementExecutionType, measurement_function_parameters: MixedMeasurementFunctionParameters, trigger_parameters: TriggerParameters, timing_parameters: TimingParameters, ac_min_frequency: float) -> None`

Initializes the mixed measurement configuration.

        Args:
            execution_type (MeasurementExecutionType):
                Specifies whether to configure only, measure only, or both configure and measure.
            measurement_function_parameters (MixedMeasurementFunctionParameters):
                The measurement function settings including mixed range and resolution.
            trigger_parameters (TriggerParameters):
                Trigger configuration including source, delay, and enable/disable settings.
            timing_parameters (TimingParameters):
                Timing settings including aperture time and settle time.
            ac_min_frequency (float):
                Minimum frequency for AC Voltage, Current measurements in Hz
                (ignored for DC measurements).
        

#### `def execution_type(self) -> MeasurementExecutionType`

Gets the measurement execution type.

        Returns:
            MeasurementExecutionType: The execution mode (configure only, measure only, or both).
        

#### `def trigger_parameters(self) -> TriggerParameters`

Gets the trigger configuration parameters.

        Returns:
            TriggerParameters: The trigger settings for the measurement.
        

#### `def measurement_function_parameters(self) -> MixedMeasurementFunctionParameters`

Gets the measurement function parameters.

        Returns:
            MixedMeasurementFunctionParameters: The mixed range, function,
            and resolution settings.
        

#### `def timing_parameters(self) -> TimingParameters`

Gets the timing configuration parameters.

        Returns:
            TimingParameters: The aperture time and settle time settings.
        

#### `def ac_min_frequency(self) -> float`

Gets the minimum AC frequency setting.

        Returns:
            float: The minimum frequency for AC voltage, current measurements.
        

### `class MixedMeasurementResultData(PCBATestToolkitData)`

Defines mixed measurement results obtained from DMM mixed measurement.

#### `def __init__(self, dmm_execution_settings: dict, measurement: Union[dict, None]) -> None`

Initializes the mixed measurement result data.

        Args:
            dmm_execution_settings (dict):
                Dictionary containing the DMM configuration used during measurement.
            measurement (dict | None):
                Dictionary containing the measurement results,
                or None if only configuration was performed.
        

#### `def dmm_execution_settings(self) -> dict`

Gets the DMM execution settings used during the measurement.

        Returns:
            dict: Dictionary with labeled keys and values including units for each setting.
        

#### `def measurement(self) -> Union[dict, None]`

Gets the measurement result data.

        Returns:
            dict | None: Dictionary containing 'Measured_Value', 'Unit', and
                'Formatted_Measurement' keys, or None if only configuration was performed.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/resistance_measurements/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dmm/resistance_measurements/__init__.py

### MODULE DOCSTRING

Provides resistance measurement functionality using DMM.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/resistance_measurements/resistance_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dmm/resistance_measurements/resistance_constants.py

### MODULE DOCSTRING

Constants for Resistance Measurements.

### `class ConstantsForDcRmsResistanceMeasurements()`

Constants used for Resistance measurement.

- `DEFAULT_RESISTANCE_EXECUTION_TYPE = ConstantsForDcRmsMeasurements.DEFAULT_EXECUTION_TYPE`

- `DEFAULT_RESISTANCE_MEASUREMENT_PARAMETERS = ResistanceMeasurementFunctionParameters(measurement_function=ConstantsForDcRmsResistanceMeasurements.RANGE_AND_FUNCTION, resolution_in_digits=ConstantsForDcRmsMeasurements.DEFAULT_RESOLUTION_IN_DIGITS)`

- `DEFAULT_RESISTANCE_TIMING_PARAMETERS = TimingParameters(aperture_time_seconds=ConstantsForDcRmsMeasurements.DEFAULT_APERTURE_TIME_SECONDS, settle_time_seconds=ConstantsForDcRmsMeasurements.DEFAULT_SETTLE_TIME_SECONDS)`

- `DEFAULT_RESISTANCE_TRIGGER_PARAMETERS = TriggerParameters(trigger_source=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_SOURCE, trigger_delay=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_DELAY, enable_trigger=ConstantsForDcRmsMeasurements.DEFAULT_ENABLE_TRIGGER, slope=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_SLOPE)`

- `DEFAULT_RESISTANCE_MEASUREMENT_CONFIGURATION = ResistanceMeasurementConfiguration(execution_type=DEFAULT_RESISTANCE_EXECUTION_TYPE, measurement_function_parameters=DEFAULT_RESISTANCE_MEASUREMENT_PARAMETERS, trigger_parameters=DEFAULT_RESISTANCE_TRIGGER_PARAMETERS, timing_parameters=DEFAULT_RESISTANCE_TIMING_PARAMETERS)`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/resistance_measurements/resistance_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dmm/resistance_measurements/resistance_data_types.py

### MODULE DOCSTRING

Resistance measurement data types.

### `class ResistanceRangeAndFunctions(Enum)`

Defines the measurement function and range settings for resistance measurement.

### `class ResistanceMeasurementFunctionParameters()`

Defines parameters used for configuration of resistance measurement.

#### `def __init__(self, measurement_function: ResistanceRangeAndFunctions, resolution_in_digits: ResolutionInDigits) -> None`

Initializes measurement function parameters.

        Args:
            measurement_function (ResistanceRangeAndFunctions):
                The resistance measurement function and range setting.
            resolution_in_digits (ResolutionInDigits):
                The measurement resolution in digits.
        

#### `def measurement_function(self) -> ResistanceRangeAndFunctions`

Gets the resistance measurement function and range setting.

        Returns:
            ResistanceRangeAndFunctions: The configured resistance range and function.
        

#### `def resolution_in_digits(self) -> ResolutionInDigits`

Gets the measurement resolution in digits.

        Returns:
            ResolutionInDigits: The configured resolution setting.
        

### `class ResistanceMeasurementConfiguration(PCBATestToolkitData)`

Defines configuration parameters for resistance measurements.

#### `def __init__(self, execution_type: MeasurementExecutionType, measurement_function_parameters: ResistanceMeasurementFunctionParameters, trigger_parameters: TriggerParameters, timing_parameters: TimingParameters) -> None`

Initializes the resistance measurement configuration.

        Args:
            execution_type (MeasurementExecutionType):
                Specifies whether to configure only, measure only, or both configure and measure.
            measurement_function_parameters (ResistanceMeasurementFunctionParameters):
                The measurement function settings including resistance range and resolution.
            trigger_parameters (TriggerParameters):
                Trigger configuration including source, delay, and enable/disable settings.
            timing_parameters (TimingParameters):
                Timing settings including aperture time and settle time.
        

#### `def execution_type(self) -> MeasurementExecutionType`

Gets the measurement execution type.

        Returns:
            MeasurementExecutionType: The execution mode (configure only, measure only, or both).
        

#### `def trigger_parameters(self) -> TriggerParameters`

Gets the trigger configuration parameters.

        Returns:
            TriggerParameters: The trigger settings for the measurement.
        

#### `def measurement_function_parameters(self) -> ResistanceMeasurementFunctionParameters`

Gets the measurement function parameters.

        Returns:
            ResistanceMeasurementFunctionParameters: The resistance range, function,
            and resolution settings.
        

#### `def timing_parameters(self) -> TimingParameters`

Gets the timing configuration parameters.

        Returns:
            TimingParameters: The aperture time and settle time settings.
        

### `class ResistanceMeasurementResultData(PCBATestToolkitData)`

Defines resistance measurement results obtained from DMM Resistance Measurement.

#### `def __init__(self, dmm_execution_settings: dict, measurement: Union[dict, None]) -> None`

Initializes the resistance measurement result data.

        Args:
            dmm_execution_settings (dict):
                Dictionary containing the DMM configuration used during measurement.
            measurement (dict | None):
                Dictionary containing the measurement results,
                or None if only configuration was performed.
        

#### `def dmm_execution_settings(self) -> dict`

Gets the DMM execution settings used during the measurement.

        Returns:
            dict: Dictionary with labeled keys and values including units for each setting.
        

#### `def measurement(self) -> Union[dict, None]`

Gets the measurement result data.

        Returns:
            dict | None: Dictionary containing 'Measured_Value', 'Unit', and
                'Formatted_Measurement' keys, or None if only configuration was performed.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/resistance_measurements/resistance_measurement.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dmm/resistance_measurements/resistance_measurement.py

### MODULE DOCSTRING

Defines class used for resistance measurement on PCB points.

### `class DcRmsResistanceMeasurement(BuildingBlockUsingNIDMM)`

Defines a way that allows you to perform resistance measurements on PCB points.

#### `def initialize(self, dmm_resource_name: str, powerline_frequency: float)`

Initializes the DMM session with the specific resource name and powerline frequency.

        Args:
            dmm_resource_name (str):
                The resource name of the DMM device to use for measurements.
            powerline_frequency (float):
                The powerline frequency in Hz (typically 50.0 or 60.0).
        

#### `def configure_and_measure(self, configuration: ResistanceMeasurementConfiguration) -> Union[ResistanceMeasurementResultData, None]`

Configures and/or performs a measurement according to specific configuration parameters.

        Args:
            configuration (ResistanceMeasurementConfiguration):
                An instance of `ResistanceMeasurementConfiguration` used to configure
                the measurement.

        Returns:
            ResistanceMeasurementResultData | None: An instance of
                `ResistanceMeasurementResultData` containing DMM execution settings
                and the measured resistance value, or None if only configuration was performed.
        

#### `def close(self)`

Closes measurement procedure and releases internal resources.

#### `def configure_measurement_function(self, parameters: ResistanceMeasurementFunctionParameters)`

Configures the measurement function settings for the DMM.

        Args:
            parameters (ResistanceMeasurementFunctionParameters):
                An instance of `ResistanceMeasurementFunctionParameters` containing the measurement
                function type (2-wire/4-wire resistance) and resolution in digits to configure.
        

#### `def configure_trigger(self, parameters: TriggerParameters)`

Configure the characteristics of triggers used for resistance measurements.

        Args:
            parameters (TriggerParameters):
                An instance of `TriggerParameters` containing trigger source,
                trigger delay, slope, and enable/disable flag.
        

#### `def configure_timing(self, parameters: TimingParameters)`

Configures the timing characteristics used for resistance measurements.

        Args:
            parameters (TimingParameters):
                An instance of `TimingParameters` containing aperture time and
                settle time settings.
        

#### `def acquire_measurement(self, resolution_in_digits: float) -> ResistanceMeasurementResultData`

Acquires and formats the measurement result data.

        Args:
            resolution_in_digits (float):
                The resolution in digits used for formatting the measured value.

        Returns:
            ResistanceMeasurementResultData:
                An instance of `ResistanceMeasurementResultData` containing:
                - dmm_execution_settings: Dictionary with keys 'Function', 'Range',
                  'Digits_Resolution', 'Aperture_Time(s)', 'Settle_Time(s)',
                  'Minimum_Frequency(Hz)', 'Absolute_Resolution',
                  'Input_Resistance(Ohm)', and 'Auto_Range_Value'
                - measurement: Dictionary with keys 'Measured_Value', 'Unit', and
                  'Formatted_Measurement'
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm_scan/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dmm_scan/__init__.py

### MODULE DOCSTRING

Contains classes used in dmm scan.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm_scan/dmm_scan_pmps_16V_15C.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/dmm_scan/dmm_scan_pmps_16V_15C.py

### MODULE DOCSTRING

Defines class used for DMM Scan using PXI Mux and PXI Shunt

### `class ScanResources(NamedTuple)`

This class exists to be the return type of the initialize method of DmmScanPMPS.
       It contains 2 initialized switch sessions and an initialized dmm session

    Args:
        NamedTuple: Built-in datatype to hold abstract tuples
    

### `class MeasurementResult(NamedTuple)`

This class is the return type of the configure_and_measure method of DmmScanPMPS.
       It contains:
        sessions: The references to the switch and dmm sessions used in the measurement
        scan_time: The total elapsed time of the scan.
        formatted_measurements: The list of all completed DMM measurements.
        execution_settings: The list of execution settings used in each measurement.
        raw_measurements: The list of raw measurements captured during the scan

    Args:
        NamedTuple: Built-in datatype to hold abstract tuples

    

### `class DmmScanPMPS(BuildingBlockUsingNIDMM, BuildingBlockUsingNISWITCH)`

This class represents the set of properties and methods needed
       to complete a scan of different measurements using a DMM
       and various switch configurations

    Args:
        BuildingBlockUsingNISWITCH: The NI-SWITCH building block
        BuildingBlockUsingNIDMM: The NI-DMM building block
    

#### `def initialize(self, mux_resource_name='Sim_MUX', mux_topology_name='2527/2-Wire Dual 16x1 Mux', shunt_resource_name='Sim_SHUNT', shunt_topology_name='2568/31-SPST', dmm_resource_name='Sim_DMM', powerline_freq=50, close_all_shunts=True) -> ScanResources`

Initializes the switch and dmm objects to be used in the dmm scan

        Args:
            mux_resource_name (str): The name of the mux resource. Defaults to "Sim_MUX".
            mux_topology_name (str): The name of the mux topology. Defaults to "2527/2-Wire Dual 16x1 Mux".
            shunt_resource_name (str): The name of the shunt resource. Defaults to "Sim_SHUNT".
            shunt_topology_name (str): The name of the shunt topology. Defaults to "2568/31-SPST".
            dmm_resource_name (str): The name of the dmm resource. Defaults to "Sim_DMM".
            powerline_freq (int): The power grid frequency. Defaults to 50.
            close_all_shunts (bool): If True, all shunt paths will be closed. Defaults to True.

        Returns:
            ScanResources: A tuple of two initialized switch sessions and one initialized dmm session
        

#### `def configure_and_measure(self, resource_handles: ScanResources, scan_configuration: list, verbose=True) -> MeasurementResult`

This method executes a complete scan across every measurement which is
           provided in the scan_configuration input parameter.

        Args:
            resource_handles (ScanResources): The two switch sessions and dmm session to use.
            scan_configuration (list): Populate this list with every measurement you
              wish to make during the scan.
            verbose (bool): If True, this will print out all of the measurement results
              from the scan. Pass False if you do not wish to print results to console. Defaults to True.

        Returns:
            MeasurementResult: The results of all measurements, including sessions, scan time,
              formatted measurements, execution settings, and raw measurements.
        

#### `def close(self, resource_handles: ScanResources) -> None`

This method disconnects, closes, and releases the resources.

        Args:
            resource_handles (ScanResources): Contains the session handles used in the scan.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/switch/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/switch/__init__.py

### MODULE DOCSTRING

Contains switch modules for pcbatt library.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/switch/static_digital_path_generations/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/switch/static_digital_path_generations/__init__.py

### MODULE DOCSTRING

Provides nipcbatt static digital path generation modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/switch/static_digital_path_generations/static_digital_path_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/switch/static_digital_path_generations/static_digital_path_data_types.py

### MODULE DOCSTRING

These data types are used when implementing digital path generation

### `class StaticDigitalPathGenerationChannelParameters(PCBATestToolkitData)`

Defines the channel value names assigned for the switch connection

#### `def __init__(self, channel_one: str, channel_two: str) -> None`

Creates an instance of StaticDigitalPathGenerationChannelParameters

        Args:
            channel_one (str): The name of the first channel
            channel_two (str): The name of the second channel
        

#### `def channel_one(self) -> str`


        :type:'str': Returns the name of channel one
        

#### `def channel_two(self) -> str`


        :type:'str': Returns the name of channel two
        

### `class StaticDigitalPathGenerationStateParameters(PCBATestToolkitData)`

Creates an instance of StaticDigitalPathGenerationStateParameters

#### `def __init__(self, connect: bool) -> None`

Defines whether to disconnect or connect a particular path

        Args:
            connect(bool): Indicates whether to make or break a given connection
        

#### `def connect(self) -> bool`


        :type:'boolean': Gets the boolean value to write
        

### `class StaticDigitalPathGenerationTimingParameters(PCBATestToolkitData)`

Creates an instance of StaticDigitalPathGenerationTimingParameters

#### `def __init__(self, max_debounce_wait: int=5000)`

Defines the maximum wait for debounce time

        Args:
            max_debounce_wait (int): The maximum time to wait for debounce
        

#### `def max_debounce_wait(self) -> int`


        :type:int
        

### `class StaticDigitalPathGenerationTerminalAndStateSettings(PCBATestToolkitData)`

Creates an instance of StaticDigitalPathGenerationTerminalAndStateSettings

#### `def __init__(self, channel_parameters: StaticDigitalPathGenerationChannelParameters, connection_state: StaticDigitalPathGenerationStateParameters)`

Aggragates channel and timing parameters into a single class

        Args:
            channel_parameters (StaticDigitalPathGenerationChannelParameters): The channels
                involved in the connection
            timing_parameters (StaticDigitalPathGenerationStateParameters): The connection
                state to be implemented
        

#### `def channel_parameters(self) -> StaticDigitalPathGenerationChannelParameters`


        :type: StaticDigitalPathGenerationChannelParameters
        

#### `def connection_state(self) -> StaticDigitalPathGenerationStateParameters`


        :type: StaticDigitalPathGenerationStateParameters
        

### `class StaticDigitalPathGenerationModuleCharacteristics(PCBATestToolkitData)`

Defines the max voltage and current characteristics of the switch

#### `def __init__(self, max_dc_voltage: float, max_ac_voltage: float, max_switching_dc_current: float, max_switching_ac_current: float) -> None`

Creates an instance of StaticDigitalPathGenerationModuleCharacteristics

        Args:
            max_dc_voltage (float): The rated maximum DC voltage of the topology
            max_ac_voltage (float): The rated maximum AC voltage of the topology
            max_switching_dc_current (float): The rated maximum DC switching current of the topology
            max_switching_ac_current (float): The rated maximum AC switching current of the topology
        

#### `def max_dc_voltage(self) -> float`


        :type:'float': Returns the max DC voltage for the topology
        

#### `def max_ac_voltage(self) -> float`


        :type:'float': Returns the max AC voltage for the topology
        

#### `def max_switching_dc_current(self) -> float`


        :type:'float': Returns the max dc switching current
        

#### `def max_switching_ac_current(self) -> float`


        :type:'float': Returns the max ac switching current
        

### `class StaticDigitalPathGenerationConfiguration(PCBATestToolkitData)`

Contains the ultimate configuration used in path generation

#### `def __init__(self, terminal_and_state_settings: StaticDigitalPathGenerationTerminalAndStateSettings, timing_settings: StaticDigitalPathGenerationTimingParameters) -> None`

Creates an instance of StaticDigitalPathGenerationConfiguration

        Args:
            terminal_state_settings (StaticDigitalPathGenerationTerminalAndStateSettings):
                A populated instance of StaticDigitalPathGenerationTerminalAndStateSettings
            timing_settings (StaticDigitalPathGenerationTimingParameters):
                A populated instance of StaticDigitalPathTimingParameters
        

#### `def terminal_and_state_settings(self) -> StaticDigitalPathGenerationTerminalAndStateSettings`


        :type: StaticDigitalPathGenerationTerminalAndStateSettings
        

#### `def timing_settings(self) -> StaticDigitalPathGenerationTimingParameters`


        :type: StaticDigitalPathGenerationTimingParameters
        

### `class StaticDigitalPathGenerationPathStatus(PCBATestToolkitData)`

Defines the status of the path

#### `def __init__(self, path_status: niswitch.PathCapability) -> None`

Creates an instance of StaticDigitalPathGenerationPathStatus

        Args:
            path_status (str): Displays whether or not the switch path is available
        

#### `def path_status(self) -> niswitch.PathCapability`


        :type:'string': Returns the availability of the path for the given connections
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library/switch/static_digital_path_generations/static_digital_path_generation.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library/switch/static_digital_path_generations/static_digital_path_generation.py

### MODULE DOCSTRING

Use this class to connect switch paths in a test fixture

### `class StaticDigitalPathGeneration(BuildingBlockUsingNISWITCH)`

This class represents the set of digital path connections the
       user wishes to create on the switch matrix

    Args:
        BuildingBlockUsingNISWITCH: The NI-SWITCH building block
    

#### `def initialize(self, switch_resource_name: str, topology_name: str, reset_device: bool=True, simulate: bool=False) -> StaticDigitalPathGenerationModuleCharacteristics`

Initializes the session to prepare for path generation

        Args:
            switch_resource_name (str): The name of the switch
            resource to be used
        

#### `def close(self)`

Disconnects all channels, closes the session and returns the resource

#### `def configure_and_generate(self, configuration=StaticDigitalPathGenerationConfiguration) -> StaticDigitalPathGenerationPathStatus`

Creates the connections defined within the terminal and state settings
        and generates a path status indicating if the operation was succesful

        Args:
             StaticDigitalPathGenerationConfiguration: Contains both the channel and state to employ

         Returns: A StaticDigitalPathGenerationPathStatus object containing the path status
        

#### `def display_status(self, status: StaticDigitalPathGenerationPathStatus) -> None`

Takes in a StaticDigitalPathGenerationPathStatus object and
           prints the contents in human-readable format based on the status

        Args:
            path_status (StaticDigitalPathGenerationPathStatus): A populated
            StaticDigitalPathGenerationPathStatus object
        

#### `def display_module_characteristics(self, chararteristics: StaticDigitalPathGenerationModuleCharacteristics) -> None`

Takes in a StaticDigitalPathGenerationModuleCharacteristics object
           and prints the contents in human-readble format

        Args:
            chararteristics (StaticDigitalPathGenerationModuleCharacteristics): A
            populated StaticDigitalPathGenerationModuleCharacteristics object
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library_core/daq/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library_core/daq/__init__.py

### MODULE DOCSTRING

Provides nipcbatt core library modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library_core/daq/_mock_daqmx/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library_core/daq/_mock_daqmx/__init__.py

### MODULE DOCSTRING

Initialization of _mock_daqmx modules package

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library_core/daq/_mock_daqmx/_mock_daqmx_constants.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library_core/daq/_mock_daqmx/_mock_daqmx_constants.py

### MODULE DOCSTRING

Constants for mock implementation of nidaqmx.

### `class _ConstantsForMockDAQmx(Enum)`

Constants used mock implementation of nidaqmx.

- `_DAQMX_ATTRIBUTES = {6271: _ConstantsForMockDAQmx.CHANNEL_TYPE, 6343: _ConstantsForMockDAQmx.COUNT_EDGES_TERM, 6306: _ConstantsForMockDAQmx.FREQ_TERM, 6320: _ConstantsForMockDAQmx.SEMI_PERIOD_TERM, 6369: _ConstantsForMockDAQmx.PULSE_TERM, 1687: _ConstantsForMockDAQmx.COUNT_EDGES_ACTIVE_EDGE, 1945: _ConstantsForMockDAQmx.FREQ_STARTING_EDGE, 8958: _ConstantsForMockDAQmx.SEMI_PERIOD_STARTING_EDGE, 324: _ConstantsForMockDAQmx.MEAS_METHOD, 325: _ConstantsForMockDAQmx.MEAS_TIME, 327: _ConstantsForMockDAQmx.DIVISOR, 6305: _ConstantsForMockDAQmx.UNITS, 6301: _ConstantsForMockDAQmx.MIN_VAL, 6300: _ConstantsForMockDAQmx.MAX_VAL, 4472: _ConstantsForMockDAQmx.PULSE_FREQ, 4470: _ConstantsForMockDAQmx.PULSE_DUTY_CYC, 6338: _ConstantsForMockDAQmx.CTR_TIME_BASE_RATE, 4464: _ConstantsForMockDAQmx.IDLE_STATE, 6331: _ConstantsForMockDAQmx.PULSE_LOW_TIME, 6330: _ConstantsForMockDAQmx.PULSE_HIGH_TIME, 4247: _ConstantsForMockDAQmx.TERMINAL_CONFIG, 12763: _ConstantsForMockDAQmx.POWER_SENSE, 12760: _ConstantsForMockDAQmx.PWR_IDLE_OUTPUT_BEHAVIOR, 10745: _ConstantsForMockDAQmx.ADC_TIMING_MODE, 6132: _ConstantsForMockDAQmx.CURRENT_EXCIT_SOURCE, 6273: _ConstantsForMockDAQmx.RESISTANCE_CONFIG, 6134: _ConstantsForMockDAQmx.EXCIT_VOLTAGE_OR_CURRENT, 6110: _ConstantsForMockDAQmx.MIN_VAL, 6109: _ConstantsForMockDAQmx.MAX_VAL, 6131: _ConstantsForMockDAQmx.EXT_SHUNT_RESISTOR_VAL, 12756: _ConstantsForMockDAQmx.VOLTAGE_SETPOINT, 12757: _ConstantsForMockDAQmx.CURRENT_SETPOINT, 6133: _ConstantsForMockDAQmx.EXCIT_VAL, 4144: _ConstantsForMockDAQmx.R_0, 4146: _ConstantsForMockDAQmx.RTD_TYPE, 6345: _ConstantsForMockDAQmx.THRMSTR_A, 6347: _ConstantsForMockDAQmx.THRMSTR_B, 6346: _ConstantsForMockDAQmx.THRMSTR_C, 4193: _ConstantsForMockDAQmx.R_1, 12758: _ConstantsForMockDAQmx.OUTPUT_ENABLE, 4864: _ConstantsForMockDAQmx.SAMP_QUANT_SAMP_PER_CHAN, 4880: _ConstantsForMockDAQmx.SAMP_PER_CHAN, 4932: _ConstantsForMockDAQmx.RATE, 10790: _ConstantsForMockDAQmx.SAMP_TIMING_ENGINE, 4487: _ConstantsForMockDAQmx.MIN_VAL, 4486: _ConstantsForMockDAQmx.MAX_VAL, 6389: _ConstantsForMockDAQmx.CHANNEL_NAME, 6286: _ConstantsForMockDAQmx.TERMINAL_CONFIG}`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library_core/daq/_mock_daqmx/_mock_daqmx_interpreters.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library_core/daq/_mock_daqmx/_mock_daqmx_interpreters.py

### MODULE DOCSTRING

Provides mock version of nidaqmx interpreter and a set of interpreter classes related to Measurements.

### `class _MockInterpreter(LibraryInterpreter)`

The interpreter defines methods used for interactions with DAQmx.
    During call of methods related to DAQmx (from Task, AIChannelCollection, Timing,...),
    a call of the interpreter occurs.
    Example when calling the method `add_ai_voltage_chan` of AIChannelCollection, the method
    `create_ai_voltage_chan` of the interpreter is called.
    

#### `def __init__(self)`

#### `def create_task(self, session_name)`

Called when the task is about to be created.

#### `def get_task_attribute_string(self, task, attribute)`

Called when invoke properties `nidaqmx.Task.name` or `nidaqmx.Task.channel_names`.

#### `def get_task_attribute_uint32(self, task, attribute)`

Called when invoke properties `nidaqmx.Task.number_of_channels`.

#### `def get_read_attribute_string(self, task, attribute)`

Called when invoke property `nidaqmx.Task.in_stream.channels_to_read`.

#### `def get_read_attribute_uint32(self, task, attribute)`

Called when invoke property `nidaqmx.Task.in_stream.di_num_booleans_per_chan`

#### `def get_write_attribute_uint32(self, task, attribute)`

Called when invoke properties of `nidaqmx._task_modules.out_stream.OutStream`.

#### `def get_system_info_attribute_string(self, attribute)`

Called when invoke property nidaqmx.system.System.local().global_channels

#### `def get_chan_attribute_int32(self, task, channel: str, attribute)`

Called when invoke properties of `nidaqmx._task_modules.channels.channel.Channel`
        and its inherited classes (AIChannel, AOChannel, DIChannel,
        DOChannel, CIChannel and COChannel).
        

#### `def get_chan_attribute_double(self, task, channel, attribute)`

Called when invoke properties of `nidaqmx._task_modules.channels.channel.Channel`
        and its inherited classes (AIChannel, AOChannel, DIChannel,
        DOChannel, CIChannel and COChannel).
        

#### `def get_chan_attribute_string(self, task, channel, attribute)`

Called when invoke properties of `nidaqmx._task_modules.channels.channel.Channel`
        and its inherited classes (AIChannel, AOChannel, DIChannel,
        DOChannel, CIChannel and COChannel).
        

#### `def get_timing_attribute_uint64(self, task, attribute)`

Called when invoke properties of `nidaqmx._task_modules.timing.Timing`.

#### `def get_timing_attribute_uint32(self, task, attribute)`

Called when invoke properties of `nidaqmx._task_modules.timing.Timing`.

#### `def get_timing_attribute_int32(self, task, attribute)`

Called when invoke properties of `nidaqmx._task_modules.timing.Timing`.

#### `def get_timing_attribute_double(self, task, attribute)`

Called when invoke properties of `nidaqmx._task_modules.timing.Timing`.

#### `def set_timing_attribute_uint32(self, task, attribute, value)`

Called when invoke properties of `nidaqmx._task_modules.timing.Timing`.

#### `def set_timing_attribute_int32(self, task, attribute, value)`

Called when invoke properties of `nidaqmx._task_modules.timing.Timing`.

#### `def set_timing_attribute_uint64(self, task, attribute, value)`

Called when invoke properties of `nidaqmx._task_modules.timing.Timing`.

#### `def set_chan_attribute_string(self, task, channel, attribute, value)`

Called when invoke properties of `nidaqmx._task_modules.channels.channel.Channel`
        and its inherited classes (AIChannel, AOChannel, DIChannel,
        DOChannel, CIChannel and COChannel).
        

#### `def set_chan_attribute_int32(self, task, channel, attribute, value)`

Called when invoke properties of `nidaqmx._task_modules.channels.channel.Channel`
        and its inherited classes (AIChannel, AOChannel, DIChannel,
        DOChannel, CIChannel and COChannel).
        

#### `def set_chan_attribute_uint32(self, task, channel, attribute, value)`

Called when invoke properties of `nidaqmx._task_modules.channels.channel.Channel`
        and its inherited classes (AIChannel, AOChannel, DIChannel,
        DOChannel, CIChannel and COChannel).
        

#### `def set_chan_attribute_double(self, task, channel, attribute, value)`

Called when invoke properties of `nidaqmx._task_modules.channels.channel.Channel`
        and its inherited classes (AIChannel, AOChannel, DIChannel,
        DOChannel, CIChannel and COChannel).
        

#### `def set_chan_attribute_bool(self, task, channel, attribute, value)`

Called when invoke properties of `nidaqmx._task_modules.channels.channel.Channel`
        and its inherited classes (AIChannel, AOChannel, DIChannel,
        DOChannel, CIChannel and COChannel).
        

#### `def create_ai_voltage_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, custom_scale_name)`

Called when method
        `nidaqmx._task_modules.ai_channel_collection.AIChannelCollection.add_ai_voltage_chan`
        is called.

#### `def create_ai_current_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, shunt_resistor_loc, ext_shunt_resistor_val, custom_scale_name)`

Called when method
        `nidaqmx._task_modules.ai_channel_collection.AIChannelCollection.add_ai_current_chan`
        is called.

#### `def create_ai_power_chan(self, task, physical_channel, voltage_setpoint, current_setpoint, output_enable, name_to_assign_to_channel)`

Called when method
        `nidaqmx._task_modules.ai_channel_collection.AIChannelCollection.add_ai_power_chan`
        is called.

#### `def create_airtd_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, rtd_type, resistance_config, current_excit_source, current_excit_val, r_0)`

Called when method
        `nidaqmx._task_modules.ai_channel_collection.AIChannelCollection.add_ai_rtd_chan`
        is called.

#### `def create_ai_thrmstr_chan_vex(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, resistance_config, voltage_excit_source, voltage_excit_val, a, b, c, r_1)`

Called when method
        `nidaqmx._task_modules.ai_channel_collection.AIChannelCollection.add_ai_thrmstr_chan_vex`
        is called.

#### `def create_ao_voltage_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, custom_scale_name)`

Called when method
        `nidaqmx._task_modules.ao_channel_collection.AOChannelCollection.add_ao_voltage_chan`
        is called.

#### `def create_di_chan(self, task, lines, name_to_assign_to_lines, line_grouping)`

Called when method
        `nidaqmx._task_modules.di_channel_collection.DIChannelCollection.add_di_chan`
        is called.

#### `def create_do_chan(self, task, lines, name_to_assign_to_lines, line_grouping)`

Called when method
        `nidaqmx._task_modules.do_channel_collection.DOChannelCollection.add_do_chan`
        is called.

#### `def create_ci_count_edges_chan(self, task, counter, name_to_assign_to_channel, edge, initial_count, count_direction)`

Called when method
        `nidaqmx._task_modules.ci_channel_collection.CIChannelCollection.add_ci_count_edges_chan`
        is called.

#### `def create_ci_freq_chan(self, task, counter, name_to_assign_to_channel, min_val, max_val, units, edge, meas_method, meas_time, divisor, custom_scale_name)`

Called when method
        `nidaqmx._task_modules.ci_channel_collection.CIChannelCollection.add_ci_freq_chan`
        is called.

#### `def create_ci_semi_period_chan(self, task, counter, name_to_assign_to_channel, min_val, max_val, units, custom_scale_name)`

Called when method
        `nidaqmx._task_modules.ci_channel_collection.CIChannelCollection.add_ci_semi_period_chan`
        is called.

#### `def create_co_pulse_chan_freq(self, task, counter, name_to_assign_to_channel, units, idle_state, initial_delay, freq, duty_cycle)`

Called when method
        `nidaqmx._task_modules.co_channel_collection.COChannelCollection.add_co_pulse_chan_freq`
        is called.

#### `def create_co_pulse_chan_time(self, task, counter, name_to_assign_to_channel, units, idle_state, initial_delay, low_time, high_time)`

Called when method
        `nidaqmx._task_modules.co_channel_collection.COChannelCollection.add_co_pulse_chan_time`
        is called.

#### `def cfg_samp_clk_timing(self, task, rate, source, active_edge, sample_mode, samps_per_chan)`

Called when method
        `nidaqmx._task_modules.timing.Timing.cfg_samp_clk_timing`
        is called.

#### `def cfg_implicit_timing(self, task, sample_mode, samps_per_chan)`

Called when method 'nidaqmx._task_modules.timing.Timing.cfg_implicit_timing'
        is called

#### `def reset_timing_attribute(self, task, attribute)`

#### `def stop_task(self, task)`

Called when method `nidaqmx.Task.stop` is called.

#### `def start_task(self, task)`

Called when method `nidaqmx.Task.start` is called.

#### `def clear_task(self, task)`

Called when method `nidaqmx.Task.close` is called.

#### `def task_control(self, task, action)`

Called when method `nidaqmx.Task.control` is called.

#### `def cfg_dig_edge_start_trig(self, task, trigger_source, trigger_edge)`

Called when method
        `nidaqmx._task_modules.triggering.start_trigger.StartTrigger.cfg_dig_edge_start_trig`
        is called.

#### `def cfg_anlg_edge_start_trig(self, task, trigger_source, trigger_slope, trigger_level)`

Called when method
        `nidaqmx._task_modules.triggering.start_trigger.StartTrigger.cfg_anlg_edge_start_trig`
        is called.

#### `def disable_start_trig(self, task)`

Called when method
        `nidaqmx._task_modules.triggering.start_trigger.StartTrigger.disable_start_trig`
        is called.

#### `def read_analog_f64(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

Reads data samples (float64) from channel(s) defined in task.

#### `def read_power_f64(self, task, num_samps_per_chan, timeout, fill_mode, read_voltage_array, read_current_array)`

Reads voltage and current samples (float64) from channel(s) defined in task.

#### `def read_counter_f64(self, task, num_samps_per_chan, timeout, read_array)`

Reads counter samples (float64) from channel(s) defined in task.

#### `def read_counter_f64_ex(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

Reads counter samples (float64) from channel(s) defined in task.

#### `def read_counter_scalar_f64(self, task, timeout)`

Reads counter sample (float64) from channel(s) defined in task.

#### `def read_counter_u32(self, task, num_samps_per_chan, timeout, read_array)`

Reads counter samples (uint32) from channel(s) defined in task.

#### `def read_counter_u32_ex(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

Reads counter samples (uint32) from channel(s) defined in task.

#### `def read_counter_scalar_u32(self, task, timeout)`

Reads counter sample (uint32) from channel(s) defined in task.

#### `def read_ctr_freq(self, task, num_samps_per_chan, timeout, interleaved, read_array_frequency, read_array_duty_cycle)`

Reads frequency samples from channel(s) defined in task.

#### `def read_ctr_freq_scalar(self, task, timeout)`

Reads frequency sample from channel(s) defined in task.

#### `def read_ctr_time(self, task, num_samps_per_chan, timeout, interleaved, read_array_high_time, read_array_low_time)`

Reads low time and high time samples from channel(s) defined in task.

#### `def read_ctr_time_scalar(self, task, timeout)`

Reads low time and high time sample from channel(s) defined in task.

#### `def read_digital_u8(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

Reads data samples (uint8) from channel(s) defined in task.

#### `def read_digital_u16(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

Reads data samples (uint16) from channel(s) defined in task.

#### `def read_digital_u32(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

Reads data samples (uint32) from channel(s) defined in task.

#### `def read_digital_lines(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

Reads data samples from channel(s) defined in task.

#### `def write_analog_f64(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

Writes data samples (float64) to channel(s) defined in task.

#### `def write_digital_u8(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

Writes data samples (uint8) to channel(s) defined in task.

#### `def write_digital_u16(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

Writes data samples (uint16) to channel(s) defined in task.

#### `def write_digital_u32(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

Writes data samples (uint32) to channel(s) defined in task.

#### `def write_digital_scalar_u32(self, task, auto_start, timeout, value)`

Writes data samples to channel(s) defined in task.

#### `def write_digital_lines(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

Writes data samples to lines in channel(s) defined in task.

#### `def write_ctr_freq_scalar(self, task, auto_start, timeout, frequency, duty_cycle)`

Writes sample to channel defined in task

#### `def write_ctr_time_scalar(self, _handle, auto_start, timeout, high_time, low_time)`

Writes sample to channel defined in task

#### `def wait_until_task_done(self, task, time_to_wait)`

Waits until the task has completed its action.

#### `def export_signal(self, task, signal_id, output_terminal) -> None`

Exports the clock or trigger signal to the specified terminal

#### `def _get_attribute_value_from_channel_settings(self, channel_expression, attribute)`

Retrieves value of specific attribute of channel(s) defined in channel expression

#### `def _set_attribute_value_to_channel_settings(self, channel_expression, attribute, value)`

Retrieves value to specific attribute of channel(s) defined in channel expression

#### `def _retrieve_attribute_value_from_first_channel(self, attribute: int)`

#### `def _assign_attribute_value_to_channels(self, attribute: int, value: Any)`

#### `def _assign_attribute_value_to_channels(channels: Dict[str, Dict], attribute: int, value: Any)`

#### `def _retrieve_attribute_value_from_channel(channels: Dict[str, Dict], channel_name: str, attribute: int)`

#### `def _retrieve_attribute_value(attributes: Dict[str, Any], attribute: int)`

#### `def _assign_attribute_value_to_channel(channels: Dict[str, Dict], channel_name: str, attribute: int, value: Any)`

#### `def _assign_attribute_value(attributes: Dict[str, Any], attribute: int, value: Any)`

### `class _ConstantsForMockInterpreters(Enum)`

### `class _InterpreterDcRmsCurrentMeasurement(_MockInterpreter)`

Defines interpreter used for DC-RMS Voltage Measurement.

#### `def read_analog_f64(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

### `class _InterpreterDcRmsVoltageMeasurement(_MockInterpreter)`

Defines interpreter used for DC-RMS Voltage Measurement.

#### `def read_analog_f64(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

### `class _InterpreterPowerSupplySourceAndMeasure(_MockInterpreter)`

Defines interpreter used for Power Supply Source And Measure.

#### `def read_power_f64(self, task, num_samps_per_chan, timeout, fill_mode, read_voltage_array, read_current_array)`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library_core/daq/_mock_daqmx/_mock_daqmx_task.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library_core/daq/_mock_daqmx/_mock_daqmx_task.py

### MODULE DOCSTRING

Simulation of DAQmx implementation.

### `class _MockSystem(nidaqmx.system.system.System)`

Defines methods used to discover mock instruments.

#### `def __init__(self, interpreter)`

#### `def local(interpreter)`


        nidaqmx.system.system.System: Represents the local DAQmx system.
        

### `class _MockTask(nidaqmx.Task)`

Defines methods used to simulate instruments though DAQmx tasks.

#### `def __init__(self, new_task_name='', *, interpreter=None)`

#### `def close(self)`


        Clears the task.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library_core/daq/_mock_daqmx/_mock_daqmx_utilities.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library_core/daq/_mock_daqmx/_mock_daqmx_utilities.py

### MODULE DOCSTRING

Provides a set of higher order function utilities related to daqmx.

### `def _replace_daqmx(interpreter_class: Type)`

Substitutes mock version of nidaqmx in Building block class.

    Args:
        interpreter_class (Type): Class of interpreter to use in mock version.
    

### `def _replace_daqmx_if_not_installed(interpreter_class: Type)`

Substitutes mock version of nidaqmx in Building block class
    if nidaqmx in not installed on local system.
    Args:
        interpreter_class (Type): Class of interpreter to use in mock version.
    

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library_core/daq/pcbatt_building_blocks.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library_core/daq/pcbatt_building_blocks.py

### MODULE DOCSTRING

Defines the base classes used by PCBA Test Toolkit building blocks

### `class BuildingBlockUsingInstrument(ABC)`

Defines the base methods for initialization and release

#### `def __init__(self, *args, **kwargs)`

Constructor that initializes instrument.

#### `def __enter__(self)`

Magic method called when 'with' is called.

#### `def __exit__(self, exception_type, exception_value, exception_traceback)`

Magic method called at end of 'with' is call block.

#### `def __del__(self)`

Destructor that calls _close() method.

#### `def _instrument_factory(cls)`

Initializes the instrument.

        Raises:
            NotImplementedError: raised when cleared directly.
        

#### `def _initialize(self, *args, **kwargs)`

#### `def _close(self)`

#### `def _invoke(self, method_name: str, *args, **kwargs)`

### `class BuildingBlockUsingNISWITCH(BuildingBlockUsingInstrument)`

Defines building block that uses NI-SWITCH for switch matrix routing

#### `def _instrument_factory(cls) -> Optional[niswitch.Session]`

Creates a placeholder for an NI-SWITCH session

        Returns:
            Optional[niswitch.Session]: None until user calls initialize() to open the session
        

#### `def is_session_initialized(self) -> bool`

 Checks if an NI-SWITCH session has been opened.

        Returns:
            bool: True if the NI-SWITCH session is open
        

#### `def session(self) -> niswitch.Session`

Defines the instance of the NI_SWITCH session.
        
        Returns:
            niswitch.Session: the type of instrument
        

### `class BuildingBlockUsingNIDMM(BuildingBlockUsingInstrument)`

Defines building block that uses NI-DMM for instrument measurements.

#### `def _instrument_factory(cls) -> Optional[nidmm.Session]`

Creates a placeholder for an NI-DMM session.

        Returns:
            Optional[nidmm.Session]: None until initialize() opens the session.
        

#### `def is_session_initialized(self) -> bool`

Checks whether an NI-DMM session has been opened.

        Returns:
            bool: True if the NI-DMM session is open.
        

#### `def session(self) -> nidmm.Session`

Defines the instance of the NI-DMM session.

        Returns:
            nidmm.Session: the instrument session.

        Raises:
            PCBATTLibraryException: if the session has not been initialized.
        

### `class BuildingBlockUsingNIDCPower(BuildingBlockUsingInstrument)`

Defines building block that uses NI-DCPower for DC power sourcing and measurement.

#### `def _instrument_factory(cls) -> Optional[nidcpower.Session]`

Creates a placeholder for an NI-DCPower session.

        Returns:
            Optional[nidcpower.Session]: None until initialize() opens the session.
        

#### `def is_session_initialized(self) -> bool`

Checks whether an NI-DCPower session has been opened.

        Returns:
            bool: True if the NI-DCPower session is open.
        

#### `def session(self) -> nidcpower.Session`

Defines the instance of the NI-DCPower session.

        Returns:
            nidcpower.Session: the instrument session.

        Raises:
            PCBATTLibraryException: if the session has not been initialized.
        

### `class BuildingBlockUsingDAQmx(BuildingBlockUsingInstrument)`

Defines Building block that uses DAQmx task for instrument management.

#### `def _instrument_factory(cls) -> nidaqmx.Task`

Creates a DAQmx task instance.
        Returns:
            nidaqmx.Task: the type of instrument.
        

#### `def is_task_initialized(self) -> bool`

Checks whether the task is initialized.

        Returns:
            bool: True, if the task is initialized with channel(s)
        

#### `def task(self) -> nidaqmx.Task`

Defines the instance of DAQmx task.

        Returns:
            nidaqmx.Task: the type of instrument.
        

#### `def contains_only_global_virtual_channels(self, channel_expression: str) -> bool`

Check whether the channel expression contains
           only global virtual channels defined in NI MAX.
        Args:
            channel_expression (str): the channel expression

        Returns:
            bool: True if the channel expression
            only contains global virtual channels defined in NI MAX.
        

#### `def _daqmx_local_system(cls) -> nidaqmx.system.System`

Gets the local DAQmx system.

        Returns:
            nidaqmx.system.System: The instance of the local DAQmx system.
        

#### `def verify_measurement_type(self, measurement_type: nidaqmx.constants.UsageTypeAI)`

Verifies the DAQ handler channels are compatible with the measurement type.

        Args:
            measurement_type (nidaqmx.constants.UsageTypeAI): type of the measurement.
        

#### `def verify_generation_type(self, generation_type: nidaqmx.constants.UsageTypeAO)`

Verifies the DAQ handler channels are compatible with the generation type.

        Args:
            generation_type (nidaqmx.constants.UsageTypeAI): type of the generation.
        

#### `def add_global_channels(self, global_channel_expression: str)`

Add global channels (defined in the channel expression)
        to the DAQmx task.

        Args:
            global_channel_expression (str):
                Expression representing the name of
                a global channel in DAQ System.
        

### `class BuildingBlockUsingNi845xI2cDevice(BuildingBlockUsingInstrument)`

Defines building block that uses NI-845x devices handler for I2C communication.

#### `def _instrument_factory(cls) -> Ni845xI2cDevicesHandler`

Creates a NI-845x I2C device handler.
        Returns:
            Ni845xI2cDevicesHandler: the type of instrument.
        

#### `def is_devices_handler_initialized(self) -> bool`

Checks whether the device handler is initialized.

        Returns:
            bool: True, if the device handler is initalized.
        

#### `def devices_handler(self) -> Ni845xI2cDevicesHandler`

Defines the instance of devices handler.

        Returns:
            Ni845xI2cDevicesHandler: the type of instrument.
        

### `class BuildingBlockUsingNi845xSpiDevice(BuildingBlockUsingInstrument)`

Defines building block that uses NI-845x devices handler for SPI communication.

#### `def _instrument_factory(cls) -> Ni845xSpiDevicesHandler`

Creates a NI 845x device handler.
        Returns:
            Ni845xSpiDevicesHandler: the type of instrument.
        

#### `def is_devices_handler_initialized(self) -> bool`

Checks whether the devices handler is initialized.

        Returns:
            bool: True, if the devices handler is initalized.
        

#### `def devices_handler(self) -> Ni845xSpiDevicesHandler`

Defines the instance of device handler.

        Returns:
            Ni845xSpiDevicesHandler: the type of instrument.
        

### `class BuildingBlockUsingVisa(BuildingBlockUsingInstrument)`

Defines Building block that uses
    serial device handler (NI-VISA) for instrument management.

#### `def __init__(self, *args, **kwargs)`

#### `def _instrument_factory(cls) -> pyvisa.ResourceManager`

Creates a NI-VISA resource manager.
        Returns:
            pyvisa.ResourceManager: the type of resource manager.
        

#### `def is_serial_device_handler_initialized(self) -> bool`

Checks whether the serial device handler is initialized.

        Returns:
            bool: True, if the serial device handler is initialized.
        

#### `def serial_device_handler(self) -> pyvisa.resources.SerialInstrument`

Defines the instance of device handler.

        Returns:
            pyvisa.resources.SerialInstrument: the type of instrument.
        

#### `def open_serial_device(self, serial_device_name: str)`

Opens a serial device with the specific name.

        Args:
            serial_device_name (str): The name of the serial device.
        

#### `def close_serial_device(self)`

Closes the serial device.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library_core/pcbatt_data_types.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library_core/pcbatt_data_types.py

### MODULE DOCSTRING

Defines the base classes used by PCBA Test Toolkit data types

### `class PCBATestToolkitData()`

Base class that defines methods for all building block data.

#### `def __repr__(self) -> str`

Called when repr() is invoked on the `PCBATestToolkitData`object

        Returns:
            str: The string representing the object.
        

#### `def __str__(self) -> str`

Called when str() is invoked on the `PCBATestToolkitData`object

        Returns:
            str: The string representing the object.
        

#### `def __eq__(self, value_to_compare: object) -> bool`

instances equality.

        Args:
            value_to_compare (object): the instance of `PCBATestToolkitData` to compare.

        Returns:
            bool: True if equals to `value_to_compare`
                (e.g. all properties defined in self object are equal to those of value_to_compare).
        

#### `def _to_json_representation(self) -> str`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library_core/pcbatt_library_exceptions.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library_core/pcbatt_library_exceptions.py

### MODULE DOCSTRING

Defines the exceptions that can be raised during execution of PCBA Test Toolkit

### `class PCBATTLibraryException(Exception)`

Defines base class for all exception raised by
    `nipcatt.pcbatt_library` and `nipcatt.pcbatt_library_core` modules.

#### `def __init__(self, message: str)`

### `class PCBATTLibraryChannelNotCompatibleWithMeasurementException(PCBATTLibraryException)`

Raised if the global virtual channels are not compatible with the type of measurement.

#### `def __init__(self, measurement_type: nidaqmx.constants.UsageTypeAI) -> None`

Initializes an instance of `PCBATTLibraryChannelNotCompatibleWithMeasurementException`.

        Args:
            measurement_type (nidaqmx.constants.UsageTypeAI): The type of measurement.
        

### `class PCBATTLibraryChannelNotCompatibleWithGenerationException(PCBATTLibraryException)`

Raised if the global virtual channels are not compatible with the type of generation.

#### `def __init__(self, measurement_type: nidaqmx.constants.UsageTypeAO) -> None`

Initializes an instance of `PCBATTLibraryChannelNotCompatibleWithGenerationException`.

        Args:
            measurement_type (nidaqmx.constants.UsageTypeAO): The type of generation.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_library_core/pcbatt_library_messages.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_library_core/pcbatt_library_messages.py

### MODULE DOCSTRING

Module containing message strings.

### `class PCBATTLibraryExceptionMessages()`

Messages used in exception classes.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/__init__.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_utilities/__init__.py

### MODULE DOCSTRING

Provides a set of utilities modules

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/csv_utilities.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_utilities/csv_utilities.py

### MODULE DOCSTRING

Provides a set of csv related routines.

### `def export_signal_to_csv_file(signal_csv_file_path: str, signal_samples: Iterable[float], signal_sampling_rate: float, x_axis_name: str, y_axis_name: str)`

Exports a sequence of float elements into a csv file as a signal.

    Args:
        signal_csv_file_path (str): path where csv file will be placed.
        signal_samples (Iterable[float]): content of the second column.
        signal_sampling_rate (float): sampling rate of the signal,
            will be used to infere content of the second column.
        x_axis_name (str): name of the first column.
        y_axis_name (str): name of the second column.
    Raises:
        ValueError: is raised when one of the provided
            argument is not supported.
    

### `def export_columns_to_csv_file(csv_file_path: str, column1_data: Iterable[float], column2_data: Iterable[float], column1_name: str, column2_name: str)`

Exports two columns of float elements into a csv file.

    Args:
        csv_file_path (str): path where csv file will be placed.
        column1_data (Iterable[float]): content of the first column.
        column2_data (Iterable[float]): content of the second column.
        column1_name (str): name of the first column.
        column2_name (str): name of the second column.
    Raises:
        ValueError: is raised when one of the provided
            argument is not supported.
    

### `def import_from_csv_file_2d_array(csv_file_path: str, header_is_present: bool, column_delimiter=';') -> tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64]]`

Imports from a csv file located at a given path a 2D array.

    Args:
        csv_file_path (str): path of the csv file.
        header_is_present (bool): indicates if csv file headers are present.

    Raises:
        ValueError: is raised when provided file path does not exist.
        IOError: is raised when csv file parsing fails for some reason.
        TypeError:
            is raised when csv file parsing succeeded but data conversion into 2D array fails.

    Returns:
        tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64]]:
            tuple first array represents first column of the csv file
            tuple second array represents second column of the csv file.
    

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/file_utilities.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_utilities/file_utilities.py

### MODULE DOCSTRING

 Provides a set of file utilities routines.

### `def write_lines(text_file_path: str, text_file_encoding: str, text_lines: Iterable[str])`

Writes lines into a text file, input example ["line1", "line2", "line3"].

    Args:
        text_file_path (str): text file path.
        text_file_encoding (str): text file encoding.
        text_lines (Iterable[str]): text file lines.

    Raises:
        ValueError: occurs when one of the input arguments is None or empty string.
        IOError: occurs when reading text file fails for some reason.
    

### `def read_lines(text_file_path: str, text_file_encoding: str) -> Iterable[str]`

Reads lines of a text file in a lazy way.

    Args:
        text_file_path (str): text file path.
        text_file_encoding (str): text file encoding.

    Raises:
        ValueError: occurs when one of the input arguments is None or empty string.
        IOError: occurs when reading text file fails for some reason.

    Returns:
        Iterable[str]: text file lines.

    Yields:
        Iterator[Iterable[str]]: text file lines exposed through iterator.
    

### `def file_exists(relative_or_absolute_file_path: str) -> bool`

Checks if a file exists.

    Raises:
        ValueError: occurs when one of the input arguments is None or empty string.
    

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/functional_utilities.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_utilities/functional_utilities.py

### MODULE DOCSTRING

 Provides a set of higher order function utilities routines.

### `def repeat(times: int)`

Returns a function which is repeated execution of inner function
       provided as argument.
    Args:
        times (int): number of times, function will be repeated.
    

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/guard_utilities.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_utilities/guard_utilities.py

### MODULE DOCSTRING

 Provides a set of guard function utilities routines.

### `class Guard()`

Defines some methods used to validate arguments of functions.

#### `def all_elements_are_of_same_type(input_list: list, expected_type: Type)`

Asserts that all elements of the the list are of same type.

        Args:
            input_list (List): The list to validate.
            expected_type (Type): The expected type.

        Raises:
            TypeError: Raised when some elements in the list are not of the expected type.
        

#### `def is_not_none(instance: object, instance_name: str)`

Asserts that the object is not None.

#### `def is_not_int(value, value_name: str)`

Ensures value is not an integer

#### `def is_float(value, value_name: str)`

Ensures value is a float

#### `def is_int(value, value_name: str)`

Ensures value is an integer

#### `def is_not_float(value, value_name: str)`

Ensures value is not a float

#### `def is_greater_than_zero(value, value_name: str)`

Asserts that the value is greater than zero.

#### `def is_greater_than_or_equal_to_zero(value, value_name: str)`

Asserts that the value is greater than or equal to zero.

#### `def is_less_than_zero(value, value_name: str)`

Asserts that the value is less than to zero.

#### `def is_less_than_or_equal_to_zero(value, value_name: str)`

Asserts that the value is less than or equal to zero.

#### `def is_less_than(value, expected_greater_value, value_name: str)`

Asserts that the value is less than expected greater value.

#### `def is_less_than_or_equal_to(value, expected_greater_value, value_name: str)`

Asserts that the value is less than expected greater value.

#### `def is_greater_than(value, expected_smaller_value, value_name: str)`

Asserts that the value is greater than expected smaller value.

#### `def is_greater_than_or_equal_to(value, expected_smaller_value, value_name: str)`

Asserts that the value is greater than or equal to expected smaller value.

#### `def is_not_empty(iterable_instance: Iterable, instance_name: str)`

Asserts that the iterable object is not empty.

#### `def is_not_none_nor_empty_nor_whitespace(value: str, value_name: str)`

Asserts that the str object is empty.

#### `def size_is_greater_or_equal_than(iterable_instance: Iterable, size: int, iterable_name: str)`

Asserts that the iterable object has enough elements.

#### `def size_is_less_than_or_equal(iterable_instance: Iterable, size: int, iterable_name: str)`

Asserts that the iterable object does contains
        less than the specific size.

#### `def have_same_size(first_iterable_instance: Iterable, first_iterable_name: str, second_iterable_instance: Iterable, second_iterable_name: str)`

Asserts that both iterable objects have same size.

#### `def is_within_limits_included(value, lower_limit, upper_limit, value_name: str)`

Asserts that the value is not within the specified limits including the limit values

#### `def is_within_limits_excluded(value, lower_limit, upper_limit, value_name: str)`

Asserts that the value is not within the specified limits excluding the limit values

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/iterable_utilities.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_utilities/iterable_utilities.py

### MODULE DOCSTRING

 Provides a set of iterable related utilities routines.

### `def count(iterable_element: Iterable) -> tuple[int, Iterable]`

Counts the number of elements is hold by an iterable,
        input iterable should be no more used after a call to this function.

    Args:
        iterable_element (Iterable): input iterable elements count.

    Returns:
        tuple[int, Iterable]: number of elements contained in the input
            iterable and new iterable replacing the input one.
    

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/native_interop_utilities.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_utilities/native_interop_utilities.py

### MODULE DOCSTRING

Provides a set of utilities functions related to native functions.

- `FUNCTION_CALL_FAILED_ARGS_2 = "Call of function '{}' failed ({})"`

- `FILE_NOT_FOUND_ARGS_1 = "file '{}' not found"`

### `class _StdCallFuncPtr(_CFunctPtr)`

Defines a pointer to a callable that supports standard calling convention.

### `class _CdeclFuncPtr(_CFunctPtr)`

Defines a pointer to a callable that supports C calling convention (Cdecl).

### `def load_stcall_win_dll(dll_path: str) -> WinDLL`

Loads a windows dll library with standard calling convention.

    Args:
        dll_path (str): the path of the dll.

    Raises:
        FileNotFoundError:
            Raised when an error occured while loading the dll.
        OSError:
            Raised when dll has invalid format.
    

### `def load_cdecl_dll(dll_path: str) -> CDLL`

Loads a dll with cdecl convention.

    Args:
        dll_path (str): The path of the dll.

    Raises:
        FileNotFoundError:
            Raised when an error occured while loading the dll.
        OSError:
            Raised when dll has invalid format.
    

### `def create_native_stdcall_win_function(dll_path: str, function_name: str, return_value_type: Type, arguments_types: List[Type]) -> _StdCallFuncPtr`

Creates a pointer on a native function from a win stdcall dll.

    Args:
        dll_path (str): The path of the dll.
        function_name (str): The name of the function.
        return_value_type (Type): The type of the object the function should return.
        arguments_types (List[Type]): A list of types for arguments.

    Raises:
        AttributeError:
            Raised the function is not defined in the library.
        FileNotFoundError:
            Raised when dll was not found.

    Returns:
        StdCallFuncPtr: the pointer to a callable object function retrieved from the library.
    

### `def create_native_cdecl_function(dll_path: str, function_name: str, return_value_type: Type, arguments_types: List[Type]) -> _CdeclFuncPtr`

Creates a pointer on a native function from a dll with cdecl convention.

    Args:
        dll_path (str): The path of the dll.
        function_name (str): The name of the function.
        return_value_type (Type): The type of the object the function should return.
        arguments_types (List[Type]): A list of types for arguments.

    Raises:
        AttributeError:
            Raised the function is not defined in the library.
        FileNotFoundError:
            Raised when dll was not found.

    Returns:
        _CdeclFuncPtr: the pointer to a callable object function retrieved from the library.
    

### `def check_dll_availability(relative_or_absolute_dll_path: str)`

Checks a dll file exist when path is absolute,
    elsewhere, the function resolves an absolute path by looking up system path variables
    then it checks the existence of resolved path.

    Args:
        relative_or_absolute_dll_path (str): The path of the dll (absolute or relative).

    Raises:
        FileNotFoundError:
            Raised the dll is not found.
    

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/numeric_utilities.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_utilities/numeric_utilities.py

### MODULE DOCSTRING

Provides a set of numeric related utilities functions.

### `def from_percent_to_decimal_ratio(percent: float) -> float`

Computes decimal ration of a given percentage value, for example 50%
    returns 0.5.

    Args:
        percent: percentage value to convert to ratio.

    Returns:
        float: for example 10  returns 0.1, 100 returns 1 and  0 returns 0

    Raises:
        ValueError: Occurs when input percent is less than zero.
    

### `def percent_of(percent: float, value: float) -> float`

Computes percent ratio of a given value.

    Args:
        percent (float): Percentage ratio to compute.
        value (float): Value for which percent ration is needed.

    Returns:
        float: for example (10 , 100) -> 10
    Raises:
        ValueError: Occurs when input percent is less than zero.
    

### `def absolute_value(value: float) -> float`

Computes absolute value of a given value.

    Args:
        value (float): Value for which absolute value is needed.

    Returns:
        float: for example -10 -> 10
    

### `def invert_value(value: float)`

Computes invert value of a given value.

    Args:
        value (float): Value for which invert value is needed.

    Returns:
        float: for example 0.5 -> 2
    Raises:
        ValueError: Occurs when input value equals zero.
    

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/os_utilities.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_utilities/os_utilities.py

### MODULE DOCSTRING

 Provides a set of operating system utilities routines.

### `def get_env_variable_paths() -> List[str]`

Enumerates paths described in the 'Path' environment variable.

### `def is_path_absolute(path: str) -> bool`

Checks is a path is absolute (containing root path).

    Args:
        path (str): the path of file or folder.

    Returns:
        bool: `True` if the path is absolute.
    

### `def combine_path_components(path: str, *path_components: str) -> str`

Appends path components to a specific path.

    Args:
        path (str): the path on which path are appended.
        *path_components (str): contains path components to add.
    Returns:
        str: the conbined path.
    

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/pcbatt_logger.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_utilities/pcbatt_logger.py

### MODULE DOCSTRING

 Implementation of PcbattLogger 

### `class PcbattLogger()`


    Class for logging inputs and outputs of methods.
    The goal is to log most informations without slowing down the caller.
    

#### `def __init__(self, file: str, methods: List[str]=None)`


        Initializes the PcbattLogger with a file path.
        methods default values is ['configure_and_measure', 'configure_and_generate']

        Args:
            file (str): The file path where the logs will be stored.
            methods (List[str], optional): List of methods to log. Defaults values : ['configure_and_measure', 'configure_and_generate'].
        

#### `def _logger_txt(module, original_method, self, configuration)`


        A static method to log inputs and outputs of methods into txt format.

        Args:
            module: The module whose method is being logged.
            original_method: The original method to call.
            configuration: The input configuration passed to the method.
            self: The PcbattLogger instance.

        Returns:
            The result returned by the original method.
        

#### `def _logger_csv(module, original_method, self, configuration)`


        A static method to log inputs and outputs of methods into csv format.
        This method is just an example how to log in different format and needs modifications.

        Args:
            module: The module whose method is being logged.
            original_method: The original method being called.
            configuration: The input configuration passed to the method.
            self: The PcbattLogger instance.

        Returns:
            The result returned by the original method.
        

#### `def _monkey_patch(self, module)`


        A method to monkey patch module methods for logging.

        Args:
            module: The module to be patched.
        

#### `def attach(self, module)`


        Attaches a module to log its method calls.

        Args:
            module: The module to be attached.
        

#### `def remove(self, module)`


        Removes a module from logging.

        Args:
            module: The module to be removed.
        

#### `def set_file(self, file: str)`


        Sets the file path for logging.

        Args:
            file (str): The file path where the logs will be stored.
        

#### `def get_modules(self) -> List[str]`


        Retrieves the names of all attached modules.

        Returns:
            List[str]: The names of all attached modules.
        

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/platform_utilities.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_utilities/platform_utilities.py

### MODULE DOCSTRING

Defines a set of platform related utilities functions.

### `def is_python_windows_32bits() -> bool`

Indicates if current python interpreter is running on windows os
    and if it is 32 bits architecture.

    Returns:
        Boolean: True if python is running 32 bits architecture on windows os
    

### `def is_python_windows_64bits() -> bool`

Indicates if current python interpreter is running on windows os
    and if it is 64 bits architecture.

    Returns:
        Boolean: True if python is running 64 bits architecture on windows os
    

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/plotter.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_utilities/plotter.py

### `def graph_plot(y: list, x=[], title='', ylabel='', xlabel='', save_fig=False)`

### `def plot_two(y1: list, y2: list, x1=[], title1='', ylabel1='', xlabel1='', x2=[], title2='', ylabel2='', xlabel2='', stitle='', save_fig=False)`

### `def plot_three(y1: list, y2: list, y3: list, x1=[], title1='', ylabel1='', xlabel1='', x2=[], title2='', ylabel2='', xlabel2='', x3=[], title3='', ylabel3='', xlabel3='', stitle='', save_fig=False)`

### `def plot_four(y1: list, y2: list, y3: list, y4: list, x1=[], title1='', ylabel1='', xlabel1='', x2=[], title2='', ylabel2='', xlabel2='', x3=[], title3='', ylabel3='', xlabel3='', x4=[], title4='', ylabel4='', xlabel4='', stitle='', save_fig=False)`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/reflection_utilities.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_utilities/reflection_utilities.py

### MODULE DOCSTRING

 Provides a set of reflection utilities functions.

### `def substitute_method(cls: Type, method: Callable, method_name: str)`

Replaces the specific method of a class by a specific function (Callable).
       This function must have self as first argument.
    Args:
        cls (Type): The class on which the method is replaced.
        method (Callable): the function to substitute.
        method_name (str): the name of the method to replace.
    

### `def enumerate_properties(instance: object) -> Iterable[Tuple]`

Enumerates properties defined in instance

    Args:
        instance (object): the object on which properties are enumerated.

    Returns:
        iterator with a sequence of tuples containing the name of property and its value.
    

### `def convert_for_json_serialization(value: object) -> Union[int, float, bool, str, list, dict]`

Converts an instance for JSON serialization.

    Args:
        value (object): the value to convert.

    Returns:
        Union[int, float, bool, str, dict]:
            if value is an Enum, returns a string with its name and its value;
            if value is str, int, float or bool, returns the value itself;
            if value is a list, return a list of JSON representation of each item;
            if value is a class containing properties,
            returns a dictionary with property names and values.
    

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/save_traces.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_utilities/save_traces.py

### MODULE DOCSTRING


Save environment config, inputs and outputs from pcbatt


### `def save_traces(config: Union[daq.DcRmsCurrentMeasurementConfiguration, daq.DcRmsVoltageMeasurementConfiguration, daq.PowerSupplySourceAndMeasureConfiguration, daq.TimeDomainMeasurementConfiguration, daq.TemperatureRtdMeasurementConfiguration, daq.TemperatureThermistorMeasurementConfiguration], file_name: str, result_data: Union[daq.DcRmsCurrentMeasurementResultData, daq.DcRmsVoltageMeasurementResultData, daq.PowerSupplySourceAndMeasureResultData, daq.TimeDomainMeasurementResultData, daq.TemperatureMeasurementResultData]=None, sampling_rate: int=10000, unit: str='Amplitude')`


    This method is use to save any types of confiuration and result_data from nipcbatt
    the file are stored in a folder called results one folder above the caller
    it creates a folder with the date month-day-year_hour-minute-seconde
    it stores all waveforms in different csv files and the rest in a txt

    Args:
        config (Any Configuration): Configuration from nipcbatt
        file_name (str): name use to save the traces
        result_data (Any ResultData, optional): Result data from nipcbatt. Defaults to None.
        sampling_rate (int, optional): sampling rate. Defaults to 10000.
        unit (str, optional): unit use for the waveforms. Defaults to 'Amplitude'.
    

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/845x_examples/I2C.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/845x_examples/I2C.py

### MODULE DOCSTRING

 This example demonstrates use of LM75 I2C Temperature sensor for taking 
    temperature measurements using USB-8452 device 

### `def check_input()`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/cDAQ_examples/cDAQ_TRTD.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/cDAQ_examples/cDAQ_TRTD.py

### MODULE DOCSTRING

Standalone for TemperatureMeasurementUsingRtd.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/cDAQ_examples/cDAQ_TTCM.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/cDAQ_examples/cDAQ_TTCM.py

### MODULE DOCSTRING

Standalone for TemperatureMeasurementUsingThermocouple.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cc_source_and_measure/custom_dc_cc_source_and_measure.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cc_source_and_measure/custom_dc_cc_source_and_measure.py

### MODULE DOCSTRING

DC constant current source and measure example with custom input parameters.

### `def main()`

Configures and executes DC CC source and measure using custom parameters.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cc_source_and_measure/dc_cc_source_and_measure_in_loop.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cc_source_and_measure/dc_cc_source_and_measure_in_loop.py

### MODULE DOCSTRING

DC constant current source and measure example running in a loop.

### `def main()`

Configures DC CC source once, then measures repeatedly in a loop.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cc_source_and_measure/default_dc_cc_source_and_measure.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cc_source_and_measure/default_dc_cc_source_and_measure.py

### MODULE DOCSTRING

DC constant current source and measure example with default input parameters.

### `def main()`

Configures and executes DC CC source and measure using default constants.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cv_source_and_measure/custom_dc_cv_source_and_measure.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cv_source_and_measure/custom_dc_cv_source_and_measure.py

### MODULE DOCSTRING

DC constant voltage source and measure example with custom input parameters.

### `def main()`

Configures and executes DC CV source and measure using custom parameters.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cv_source_and_measure/dc_cv_source_and_measure_in_loop.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cv_source_and_measure/dc_cv_source_and_measure_in_loop.py

### MODULE DOCSTRING

DC constant voltage source and measure example running in a loop.

### `def main()`

Configures DC CV source once, then measures repeatedly in a loop.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cv_source_and_measure/default_dc_cv_source_and_measure.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cv_source_and_measure/default_dc_cv_source_and_measure.py

### MODULE DOCSTRING

DC constant voltage source and measure example with default input parameters.

### `def main()`

Configures and executes DC CV source and measure using default constants.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_current_measurement/current_measurement_in_loop.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_current_measurement/current_measurement_in_loop.py

### MODULE DOCSTRING

DMM DC-RMS Current measurement in loop example with custom input parameters.

### `def main()`

Configures and executes custom DMM DC-RMS current measurement with logging.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_current_measurement/custom_dc_rms_current_measurement.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_current_measurement/custom_dc_rms_current_measurement.py

### MODULE DOCSTRING

DMM DC-RMS Current measurement example with custom input parameters.

### `def main()`

Configures and executes custom DMM DC-RMS current measurement with logging.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_current_measurement/default_dc_rms_current_measurement.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_current_measurement/default_dc_rms_current_measurement.py

### MODULE DOCSTRING

DMM DC-RMS Current measurement example with default input parameters.

### `def main()`

Configures and executes default DMM DC-RMS current measurement with logging.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_voltage_measurement/custom_dc_rms_voltage_measurement.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_voltage_measurement/custom_dc_rms_voltage_measurement.py

### MODULE DOCSTRING

DMM DC-RMS Voltage measurement example with custom input parameters.

### `def main()`

Configures and executes custom DMM DC-RMS voltage measurement with logging.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_voltage_measurement/default_dc_rms_voltage_measurement.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_voltage_measurement/default_dc_rms_voltage_measurement.py

### MODULE DOCSTRING

DMM DC-RMS Voltage measurement example with default input parameters.

### `def main()`

Configures and executes default DMM DC-RMS voltage measurement with logging.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_voltage_measurement/PXI_HW_trigger_delay_voltage_measurement.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_voltage_measurement/PXI_HW_trigger_delay_voltage_measurement.py

### MODULE DOCSTRING

Signal Voltage Generation connected to DMM DC-RMS Voltage Measurement.

### `def main()`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_voltage_measurement/voltage_measurement_in_loop.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_voltage_measurement/voltage_measurement_in_loop.py

### MODULE DOCSTRING

DMM DC-RMS Voltage measurement in loop example with custom input parameters.

### `def main()`

Configures and executes custom DMM DC-RMS voltage measurement with logging.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_examples/mixed_measurement/custom_mixed_measurement.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/DMM_examples/mixed_measurement/custom_mixed_measurement.py

### MODULE DOCSTRING

DMM Mixed measurement example with custom input parameters.

### `def main()`

Configures and executes custom DMM mixed measurement with logging.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_examples/mixed_measurement/default_mixed_measurement.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/DMM_examples/mixed_measurement/default_mixed_measurement.py

### MODULE DOCSTRING

Mixed measurement example with default input parameters.

### `def main()`

Configures and executes default Mixed measurement with logging.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_examples/resistance_measurement/custom_resistance_measurement.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/DMM_examples/resistance_measurement/custom_resistance_measurement.py

### MODULE DOCSTRING

Resistance measurement example with custom input parameters.

### `def main()`

Configures and executes custom resistance measurement with logging.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_examples/resistance_measurement/default_resistance_measurement.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/DMM_examples/resistance_measurement/default_resistance_measurement.py

### MODULE DOCSTRING

Resistance measurement example with default input parameters.

### `def main()`

Configures and executes default resistance measurement with logging.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_SCAN_examples/dmm_loop_scan_pmps_example.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/DMM_SCAN_examples/dmm_loop_scan_pmps_example.py

### MODULE DOCSTRING

This example executes a DMM Scan in a loop 5 times with a 2 second
   delay between iterations. Each iteration scans 3 voltage and 3 current
   measurements and prints the results.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_SCAN_examples/dmm_scan_pmps_example.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/DMM_SCAN_examples/dmm_scan_pmps_example.py

### MODULE DOCSTRING

This example executes a DMM Scan to obtain 3 voltage, 3 current
   measurement. It returns both the formatted and the raw measurements.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_SCAN_examples/dmm_two_scan_pmps_example.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/DMM_SCAN_examples/dmm_two_scan_pmps_example.py

### MODULE DOCSTRING

This example executes a DMM Scan to obtain 3 voltage, 3 current
   measurement. It returns both the formatted and the raw measurements.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_SDSG_SDSM.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_SDSG_SDSM.py

### MODULE DOCSTRING

Static Digital State Generation and Measurement

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_SVG_DRVM.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_SVG_DRVM.py

### `class Generation_type(Enum)`

### `class Waveform_type(Enum)`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_SVG_FDVM.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_SVG_FDVM.py

### `class Generation_type(Enum)`

### `class Waveform_type(Enum)`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_SVG_TDVM.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_SVG_TDVM.py

### `class Generation_type(Enum)`

### `class Waveform_type(Enum)`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_SVG_TDVM_RSS.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_SVG_TDVM_RSS.py

### `class Generation_type(Enum)`

### `class Waveform_type(Enum)`

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/SWITCH_examples/default_ni_switch_generation.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/SWITCH_examples/default_ni_switch_generation.py

### MODULE DOCSTRING

 NI-SWITCH generation with default input parameters 

### `def main()`

Configures and executes default NI SWITCH generation with logging.

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/SWITCH_examples/switch_validate_path_status.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/SWITCH_examples/switch_validate_path_status.py

### MODULE DOCSTRING

 Validates that the path capability between points is detected and reported correctly 

<!--NI_PYTHON_API repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/TestScale_examples/TS_PSSM_to_TDVM.py -->
## PYTHON MODULE: src/nipcbatt/pcbatt_validation_examples/TestScale_examples/TS_PSSM_to_TDVM.py

### MODULE DOCSTRING

PSSM to TDVM

<!--NI_PYTHON_API repo=nipcbatt path=tests/__init__.py -->
## PYTHON MODULE: tests/__init__.py

### MODULE DOCSTRING

 Provides a set of unit tests for nipcbatt and its dependencies, see requirements.txt 

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for nipcbatt package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_analysis_tests/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for nipcbatt.pcbatt_analysis package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/common/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_analysis_tests/common/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for nipcbatt.pcbatt_analysis.common package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/common/test_common_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_analysis_tests/common/test_common_types.py

### MODULE DOCSTRING

Defines unit tests related to nipcbatt.pcbatt_analysis.common_types module.

### `class TestSpectrumAmplitudeType(unittest.TestCase)`

Provides unit tests of `SpectrumAmplitudeType` class.

    Args:
        unittest (TestCase): test cases fixture.
    

#### `def setUpClass(cls)`

#### `def test_spectrum_amplitude_type_integer_values(self, case_name: str, actual_enum_value: SpectrumAmplitudeType, expected_int_value: int)`

Test of enum `SpectrumAmplitudeType` integer values

### `class TestSpectrumPhaseUnit(unittest.TestCase)`

Provides unit tests of `SpectrumPhaseUnit` class.

    Args:
        unittest (TestCase): test cases fixture.
    

#### `def setUpClass(cls)`

#### `def test_spectrum_phase_unit_integer_values(self, case_name: str, actual_enum_value: SpectrumPhaseUnit, expected_int_value: int)`

Test of pcbatt_analysis.frequency_domain_analysis.FftSpectrumPhaseUnit integer values

### `class TestAmplitudePhaseSpectrum(unittest.TestCase)`

Provides unit tests of `AmplitudePhaseSpectrum` class.

    Args:
        unittest (TestCase): test cases fixture.
    

#### `def setUpClass(cls)`

#### `def test_amplitude_phase_spectrum(self, case_name: str, expected_amplitude_type: SpectrumAmplitudeType, expected_amplitude_is_db: bool, expected_phase_unit: SpectrumPhaseUnit)`

Test of `AmplitudePhaseSpectrum` class constructor.

### `class TestWaveformTone(unittest.TestCase)`

Defines a test fixture that checks
    `WaveformTone` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_waveform_tone(self)`

Tests if an instance of `WaveformTone`
        is created with the specific values.
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/test_analysis_library_info.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_analysis_tests/test_analysis_library_info.py

### MODULE DOCSTRING

Defines unit tests related to nipcbatt.pcbatt_analysis.library_info module.

### `class TestAnalysisLibraryInfo(unittest.TestCase)`

Defines a test fixture that checks function of module
    `pcbatt_analysis.library_info`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_get_labview_analysis_traces_folder_path(self)`

Test of pcbatt_analysis.library_info.get_labview_analysis_traces_folder_path

#### `def test_enable_traces(self)`

Test of pcbatt_analysis.library_info.enable_traces

#### `def test_are_traces_enabled(self)`

Test of pcbatt_analysis.library_info.are_traces_enabled

#### `def test_is_labview_runtime_available(self)`

Test of pcbatt_analysis.library_info.is_labview_runtime_available

#### `def test_get_labview_analysis_library_version_numbers(self)`

Test of pcbatt_analysis.library_info.get_labview_analysis_library_version

#### `def test_get_labview_analysis_available_functions_names_list(self)`

Test of pcbatt_analysis.library_info.get_supported_labview_functions_names_list

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_analysis/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_analysis/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for nipcbatt.pcbatt_analysis.waveform_analysis package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_analysis/test_amplitude_and_levels_analysis.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_analysis/test_amplitude_and_levels_analysis.py

### MODULE DOCSTRING

Defines unit tests related to nipcbatt.pcbatt_analysis.amplitude_and_levels_analysis module.

### `class TestAmplitudeAndLevelsProcessingResult(unittest.TestCase)`

Defines a test fixture that checks class AmplitudeAndLevelsProcessingResult of module
    `pcbatt_analysis.amplitude_and_levels_analysis`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_amplitude_and_levels_processing_result(self)`

Test of pcbatt_analysis.amplitude_and_levels_analysis.AmplitudeAndLevelsProcessingResult
        class constructor

### `class TestLabViewAmplitudeAndLevels(unittest.TestCase)`

Provides unit tests of LabViewAmplitudeAndLevels class.

    Args:
        unittest (TestCase): test cases fixture.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_get_last_error_message_returns_empty_string(self)`

Test of pcbatt_analysis.amplitude_and_levels_analysis.LabViewAmplitudeAndLevels
        get_last_error_message method when there is no error

#### `def test_process_single_waveform_amplitude_and_levels_auto_select_method_emv_trace(self)`

Test of pcbatt_analysis.amplitude_and_levels.LabViewAmplitudeAndLevels
        process_single_waveform_amplitude_and_levels method using auto select analysis strategy
        using emv 106 Khz waveform.
        

#### `def test_process_single_waveform_amplitude_and_levels_auto_select_method(self)`

Test of pcbatt_analysis.amplitude_and_levels.LabViewAmplitudeAndLevels
        process_single_waveform_amplitude_and_levels method using auto select analysis strategy.
        

#### `def test_process_single_waveform_amplitude_and_levels_histogram_method(self)`

Test of pcbatt_analysis.amplitude_and_levels.LabViewAmplitudeAndLevels
        process_single_waveform_amplitude_and_levels method using histogram analysis strategy.
        

#### `def test_process_single_waveform_amplitude_and_levels_peak_method(self)`

Test of pcbatt_analysis.amplitude_and_levels.LabViewAmplitudeAndLevels
        process_single_waveform_amplitude_and_levels method using peak analysis strategy.
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_analysis/test_dc_rms_analysis.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_analysis/test_dc_rms_analysis.py

### MODULE DOCSTRING

Defines unit tests related to nipcbatt.pcbatt_analysis.dc_rms_analysis module.

### `class TestDcRmsProcessingResult(unittest.TestCase)`

Defines a test fixture that checks class DcRmsProcessingResult of module
    `pcbatt_analysis.dc_rms_analysis`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_dc_rms_processing_result(self)`

Test of pcbatt_analysis.dc_rms_analysis.DcRmsProcessingResults class constructor

### `class TestLabViewBasicDcRms(unittest.TestCase)`

Provides unit tests of LabViewBasicDcRms class.

    Args:
        unittest (TestCase): test cases fixture.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_get_last_error_message_returns_empty_string(self)`

Test of pcbatt_analysis.dc_rms_analysis.LabViewDcRms
        get_last_error_message method when there is no error

#### `def test_process_single_waveform_dc_rms_lsl_window(self)`

Test of pcbatt_analysis.dc_rms_analysis.LabViewDcRms
        process_single_waveform_dc_rms method using low side lobe window

#### `def test_process_single_waveform_dc_rms_hann_window(self)`

Test of pcbatt_analysis.dc_rms_analysis.LabViewDcRms
        process_single_waveform_dc_rms method using hann window

#### `def test_process_single_waveform_dc_rms_rectangular_window(self)`

Test of pcbatt_analysis.dc_rms_analysis.LabViewDcRms
        process_single_waveform_dc_rms method using rectangular window

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_analysis/test_frequency_domain_analysis.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_analysis/test_frequency_domain_analysis.py

### MODULE DOCSTRING

Defines unit tests related to nipcbatt.pcbatt_analysis.frequency_domain_analysis module.

### `class TestLabViewFftSpectrumWindow(unittest.TestCase)`

Provides unit tests of `FftSpectrumWindow` class.

    Args:
        unittest (TestCase): test cases fixture.
    

#### `def setUpClass(cls)`

#### `def test_labview_fft_spectrum_window_integer_values(self, case_name: str, actual_enum_value: LabViewFftSpectrumWindow, expected_int_value: int)`

Test of `LabViewFftSpectrumWindow` integer values

### `class TestMultipleTonesProcessingResult(unittest.TestCase)`

Provides unit tests of `MultipleTonesProcessingResult` class.

    Args:
        unittest (TestCase): test cases fixture.
    

#### `def setUpClass(cls)`

#### `def test_multiple_tones_processing_result_single_tone_waveform(self, case_name: str, expected_amplitude_type: SpectrumAmplitudeType, expected_amplitude_value: float, expected_frequency_value: float, expected_phase_degrees: float)`

Test of AmplitudePhaseSpectrum class constructor.

### `class TestMultipleTonesAmplitudePhaseSpectrumProcessingResult(unittest.TestCase)`

Provides unit tests of `MultipleTonesAmplitudePhaseSpectrumProcessingResult` class.

    Args:
        unittest (TestCase): test cases fixture.
    

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_multiple_tones_amplitude_phase_spectrum_processing_result(self)`

Test of `MultipleTonesAmplitudePhaseSpectrumProcessingResult` class constructor.

### `class TestLabViewFrequencyDomainProcessing(unittest.TestCase)`

Provides unit tests of `FrequencyDomainProcessing` class.

    Args:
        unittest (TestCase): test cases fixture.
    

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_process_single_waveform_multiple_tones_and_amplitude_phase_spectrum_square_waveform(self)`

Test of `LabViewFrequencyDomainProcessing`
        `process_single_waveform_multiple_tones_and_amplitude_phase_spectrum`
        method when there is no error

#### `def test_process_single_waveform_multiple_tones_and_amplitude_phase_spectrum_modulated_waveform_amplitude_is_db(self)`

Test of `LabViewFrequencyDomainProcessing`
        `process_single_waveform_multiple_tones_and_amplitude_phase_spectrum` method when there is no error
        

### `class TestLabViewFftSpectrumAmplitudePhase(unittest.TestCase)`

Provides unit tests of `LabViewFftSpectrumAmplitudePhase` class.

    Args:
        unittest (TestCase): test cases fixture.
    

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_get_last_error_message_returns_empty_string(self)`

Test of `LabViewFftSpectrumAmplitudePhase`
        get_last_error_message method when there is no error

#### `def test_process_single_waveform_magnitude_phase_spectrum_single_tone_waveform(self, case_name: str, amplitude_type: SpectrumAmplitudeType)`

Test of `LabViewFftSpectrumAmplitudePhase`
        `process_single_waveform_amplitude_phase_spectrum` method when there is no error
        

#### `def test_process_single_waveform_magnitude_phase_spectrum_square_waveform(self, case_name: str, amplitude_type: SpectrumAmplitudeType)`

Test of `LabViewFftSpectrumAmplitudePhase`
        `process_single_waveform_amplitude_phase_spectrum` method when there is no error
        

### `class TestLabViewMultipleTonesMeasurement(unittest.TestCase)`

Provides unit tests of `LabViewMultipleTonesMeasurement` class.

    Args:
        unittest (TestCase): test cases fixture.
    

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_get_last_error_message_returns_empty_string(self)`

Test of `LabViewMultipleTonesMeasurement`
        get_last_error_message method when there is no error

#### `def test_process_single_waveform_multiple_tones_square_waveform(self)`

Test of `LabViewMultipleTonesMeasurement`
        process_single_waveform_multiple_tones method when there is no error

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_analysis/test_pulse_analog_analysis.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_analysis/test_pulse_analog_analysis.py

### MODULE DOCSTRING

Defines unit tests related to nipcbatt.pcbatt_analysis.pulse_analog_analysis module.

### `class TestPulseAnalogProcessingReferenceLevels(unittest.TestCase)`

Defines a test fixture that checks class `PulseAnalogProcessingReferenceLevels` of module
    `pcbatt_analysis.waveform_analysis.pulse_analog_analysis`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_pulse_analog_processing_reference_levels(self)`

Test of `pcbatt_analysis.pulse_analog_analysis.PulseAnalogProcessingReferenceLevels`
        class constructor

### `class TestWaveformPeriodicityAnalogProcessingResult(unittest.TestCase)`

Defines a test fixture that checks class `PulsePeriodicityAnalogProcessingResult` of module
    `pcbatt_analysis.waveform_analysis.pulse_analog_analysis`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_waveform_periodicity_analog_processing_result(self)`

Test of `pcbatt_analysis.pulse_analog_analysis.WaveformPeriodicityAnalogProcessingResult`
        class constructor

#### `def test_waveform_periodicity_analog_processing_result_invalid_inputs(self)`

Test of `pcbatt_analysis.pulse_analog_analysis.WaveformPeriodicityAnalogProcessingResult`
        class constructor

### `class TestPulseAnalogMeasurementPercentLevelsSettings(unittest.TestCase)`

Defines a test fixture that checks class
        `PulseAnalogMeasurementPercentLevelsSettings` of module
        `pcbatt_analysis.waveform_analysis.pulse_analog_analysis`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_pulse_analog_measurement_percent_levels_settings_invalid_inputs(self)`

Test of
        `pcbatt_analysis.pulse_analog_analysis.PulseAnalogMeasurementPercentLevelsSettings`
        class constructor
        

#### `def test_pulse_analog_measurement_percent_levels_settings(self)`

Test of
        `pcbatt_analysis.pulse_analog_analysis.PulseAnalogMeasurementPercentLevelsSettings`
        class constructor
        

### `class TestPulseAnalogProcessingResult(unittest.TestCase)`

Defines a test fixture that checks class PulseAnalogProcessingResult of module
    `pcbatt_analysis.waveform_analysis.pulse_analog_analysis`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_pulse_analog_processing_result(self)`

Test of `pcbatt_analysis.pulse_analog_analysis.PulseAnalogProcessingResult`
        class constructor

#### `def test_pulse_analog_processing_result_invalid_inputs(self)`

Test of `pcbatt_analysis.pulse_analog_analysis.PulseAnalogProcessingResult`
        class constructor

### `class TestLabViewPulseAnalogMeasurements(unittest.TestCase)`

Provides unit tests of
    `pcbatt_analysis.pulse_analog_analysis.LabViewPulseAnalogMeasurements` class.

    Args:
        unittest (TestCase): test cases fixture.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_get_last_error_message_returns_empty_string(self)`

Test of ``pcbatt_analysis.pulse_analog_analysis.LabViewPulseAnalogMeasurements
        get_last_error_message`` method when there is no error

#### `def test_process_single_waveform_multiple_pulse_measurements_export_all_relative_percent_reference_levels(self)`

Test of
        `LabViewPulseAnalogMeasurements.process_single_waveform_multiple_pulse_measurements` method.
        

#### `def test_process_single_waveform_pulse_measurements_export_all_relative_percent_reference_levels(self)`

Test of
        `LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements` method.
        

#### `def test_process_single_waveform_pulse_measurements_ignore_periodicity_analysis_relative_percent_reference_levels(self)`

Test of
        `LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements` method.
        

#### `def test_process_single_waveform_pulse_measurements_ignore_periodicity_analysis_absolute_reference_levels(self)`

Test of
        `LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements` method.
        

#### `def test_process_single_waveform_pulse_measurements_export_all_absolute_reference_levels(self)`

Test of
        `LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements` method.
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_creation/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_creation/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for 
nipcbatt.pcbatt_analysis.waveform_creation package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_creation/test_multitones_waveform.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_creation/test_multitones_waveform.py

### MODULE DOCSTRING

Provides unit tests related to multitones_waveform.py module

### `class TestMultitonesWaveform(unittest.TestCase)`

Defines a test fixture that checks creation functions of module
    `multitones_waveform`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_create_multitones_waveform_single_tone(self)`

Test of `multitones_waveform.create_multitones_waveform` function

#### `def test_create_multitones_waveform_multiple_harmonics(self)`

Test of `multitones_waveform.create_multitones_waveform` function

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_creation/test_sine_waveform.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_creation/test_sine_waveform.py

### MODULE DOCSTRING

Provides unit tests related to sine_waveform.py module

### `class TestSineWaveform(unittest.TestCase)`

Defines a test fixture that checks creation functions of module
    `sine_waveform`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_create_cosine_waveform(self, case_name: str, expected_amplitude: float, expected_frequency: float, expected_phase: float, expected_offset: float, expected_sampling_rate: float, expected_waveform_duration_seconds: float)`

Test of `sin_waveform.create_cosine_waveform` function

#### `def test_create_sine_waveform(self, case_name: str, expected_amplitude: float, expected_frequency: float, expected_phase: float, expected_offset: float, expected_sampling_rate: float, expected_waveform_duration_seconds: float)`

Test of `sin_waveform.create_sine_waveform` function

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_creation/test_square_waveform.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_creation/test_square_waveform.py

### MODULE DOCSTRING

Provides unit tests related to square_waveform.py module

### `class TestSquareWaveform(unittest.TestCase)`

Defines a test fixture that checks creation functions of module
    `square_waveform`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_create_square_waveform(self, case_name: str, expected_amplitude: float, expected_frequency: float, expected_duty_cycle: float, expected_phase: float, expected_offset: float, expected_sampling_rate: float, expected_waveform_duration_seconds: float, expected_waveform_max: float, expected_waveform_min: float)`

Test of `square_waveform.create_square_waveform` function

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_transformation/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_transformation/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for 
nipcbatt.pcbatt_analysis.waveform_transformation package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_transformation/test_scale_and_offset_waveform.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_transformation/test_scale_and_offset_waveform.py

### MODULE DOCSTRING

Provides unit tests related to square_waveform.py module

### `class TestScaleAndOffsetWaveform(unittest.TestCase)`

Defines a test fixture that checks transformation functions of module
    `scale_and_offset_waveform`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_scale_and_apply_offset_linear_function(self, case_name: str, expected_scale_factor: float, expected_offset: float)`

Test of `scale_and_offset_waveform.scale_and_apply_offset` function

#### `def test_scale_and_apply_offset_inplace_linear_function(self, case_name: str, expected_scale_factor: float, expected_offset: float)`

Test of `scale_and_offset_waveform.scale_and_apply_offset_inplace` function

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_communication_library_tests/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_communication_library_tests/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for nipcbatt.pcbatt_communication_library package.

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_communication_library_tests/_ni_845x_internal/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_communication_library_tests/_ni_845x_internal/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for nipcbatt.pcbatt_communication_library._ni_845x_internal package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_communication_library_tests/_ni_845x_internal/test_ni_845x_functions.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_communication_library_tests/_ni_845x_internal/test_ni_845x_functions.py

### MODULE DOCSTRING

This module provides unit tests for functions defined in
nipcbatt.pcbatt_communication_library._ni_845x_internal._ni_845x_functions module.

### `def _is_ni_845x_installed()`

### `class TestInvokeNi845xFunction(unittest.TestCase)`

Defines a test fixture that checks
    `_invoke_ni_845x_function` function is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_invoke_ni_845x_function_fails_if_function_name(self, test_name, function_name)`

unit test of _get_function_from_native_library.

#### `def test_invoke_ni_845x_function_fails_if_function_name_does_not_exist(self)`

unit test of _get_function_from_native_library.

### `class TestI2cConfiguration(unittest.TestCase)`

Defines a test fixture that checks
    functions related to I2C configuration are ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_ni_845x_i2c_configuration_open_should_not_fail(self)`

unit test of ni_845x_i2c_configuration_open.

#### `def test_ni_845x_spi_configuration_open_should_not_fail(self)`

unit test of ni_845x_spi_configuration_open.

#### `def test_ni_845x_i2c_configuration_set_address_should_not_fail(self)`

unit test of ni_845x_i2c_configuration_set_address.

#### `def test_ni_845x_i2c_configuration_set_clock_rate_should_not_fail(self)`

unit test of ni_845x_i2c_configuration_set_clock_rate.

#### `def test_ni_845x_i2c_configuration_set_addressing_type_should_not_fail(self)`

unit test of ni_845x_i2c_configuration_set_addressing_type.

#### `def test_ni_845x_i2c_configuration_set_ack_poll_timeout_should_not_fail(self)`

unit test of ni_845x_i2c_configuration_set_ack_poll_timeout.

### `class TestSpiConfiguration(unittest.TestCase)`

Defines a test fixture that checks
    functions related to SPI configuration are ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_ni_845x_spi_configuration_set_chip_select_should_not_fail(self)`

unit test of ni_845x_spi_configuration_set_chip_select.

#### `def test_ni_845x_spi_configuration_set_clock_rate_should_not_fail(self)`

unit test of ni_845x_spi_configuration_set_clock_rate.

#### `def test_ni_845x_spi_configuration_set_clock_phase_should_not_fail(self, test_name: str, clock_phase: SpiConfigurationClockPhase)`

unit test of ni_845x_spi_configuration_set_clock_phase.

#### `def test_ni_845x_spi_configuration_set_clock_polarity_should_not_fail(self, test_name: str, clock_polarity: SpiConfigurationClockPolarity)`

unit test of ni_845x_spi_configuration_set_clock_polarity.

### `class TestConvertMemoryAddressToDataBytesArray(unittest.TestCase)`

Defines a test fixture that checks
    function `convert_memory_address_to_data_bytes_array` is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_convert_memory_address_to_data_bytes_array(self, test_case_name: str, memory_address: int, address_type: DataMemoryAddressType, address_endianness: DataMemoryAddressEndianness, expected_bytes_array: List[int])`

unit test of convert_memory_address_to_data_bytes_array.

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_core_tests/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_core_tests/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for nipcbatt.pcbatt_core package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_core_tests/test_pcbatt_building_blocks.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_core_tests/test_pcbatt_building_blocks.py

### MODULE DOCSTRING

This module provides unit tests of module pcbatt_building_blocks
   present in package pcbatt_core located in src.

### `class TestInstrument()`

Defines the instrument used in TestAbstractBuildingBlockUsingInstrument fixture

#### `def close(self)`

### `class ChildClassForTests(BuildingBlockUsingInstrument)`

chlid class of BuildingBlockUsingInstrument
     that defines minimum required implementations

    Args:
        BuildingBlockUsingInstrument: Base class from which this class inherits.
    

#### `def is_instrument_initialized(self) -> bool`

Checks whether the instance of TestInstrument is initialized.

        Returns:
            bool: True, if the instance of TestInstrument is initialized.
        

#### `def instrument(self) -> TestInstrument`

Defines the instance of TestInstrument.

        Returns:
            TestInstrument: the type of instrument.
        

#### `def name(self)`

#### `def _instrument_factory(cls) -> TestInstrument`

Creates an instance of TestInstrument.
        Returns:
            TestInstrument: the type of instrument.
        

#### `def close(self)`

### `class ChildClassInitWithIntFloat(ChildClassForTests)`

Chlid class of ChildClassForTests(BuildingBlockUsingInstrument).
     It uses initialization with an int argument and a string argument.

    Args:
        ChildClassForTests: Base class from which this class inherits.
    

#### `def initialize(self, int_param: int, str_param: str)`

Initializes the building block with specific values.

        Args:
            int_param (int): the int argument
            str_param (str): the string argument
        

### `class ChildClassInitWithVarious(ChildClassForTests)`

Chlid class of ChildClassForTests(BuildingBlockUsingInstrument).
       It uses initialization with variatic argument(s).

    Args:
        ChildClassForTests: Base class from which this class inherits.
    

#### `def initialize(self, *args, **kwnargs)`

Initializes the building block with variatic arguments.

### `class ChannelNames(ChildClassForTests)`

x

#### `def __init__(self, n)`

### `class ChannelsToRead(ChildClassForTests)`

x

#### `def __init__(self, n)`

### `class Task(ChildClassForTests)`

x

#### `def __init__(self)`

#### `def _calculate_num_samps_per_chan(self, one)`

#### `def _raise_invalid_write_num_chans_error(self, one, two)`

### `class Name(ChildClassForTests)`

x

#### `def name(self)`

### `class DIChannel(ChildClassForTests)`

x

#### `def __iter__(self)`

#### `def __next__(self)`

#### `def __init__(self)`

#### `def add_di_chan(self, ch_exp, two, three)`

### `class OStream(ChildClassForTests)`

#### `def __init__(self)`

### `class MockDAQmxTask(nidaqmx.Task)`

defines methods used to simulate instruments though DAQmx.

    Args:
        nidaqmx.Task: the class from which this class inherits.
    

#### `def __init__(self, new_task_name='', *, grpc_options=None)`

Does not call Task.__init__ (it requires DAQmx to be installed).

#### `def in_stream(self)`

#### `def number_of_channels(self)`

#### `def out_stream(self)`

#### `def close(self)`

Closes the task (does nothing).

#### `def __del__(self)`

Called when the instance is deleted (does nothing).

#### `def channels(self)`

#### `def channel_names(self)`

#### `def do_channels(self)`

#### `def ci_channels(self)`

#### `def set_num_channels(self, n)`

#### `def di_channels(self)`

#### `def timing(self)`

### `class TestBuildingBlockUsingInstrument(unittest.TestCase)`

Defines a test fixture that checks child classes of
    BuildingBlockUsingInstrument are ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_child_initalization_without_arguments(self)`

#### `def test_child_instrument(self)`

#### `def test_child_initalization_with_fixed_arguments(self)`

#### `def test_child_initialazation_with_various_arguments(self)`

### `def instrument_factory() -> MockDAQmxTask`

Creates an instance of MockDAQmxTask.

### `class BuildingBlockUsingDAQmxForTests(BuildingBlockUsingDAQmx)`

Chlid class of BuildingBlockUsingDAQmx(BuildingBlockUsingInstrument).

    Args:
        BuildingBlockUsingDAQmx: Base class from which this class inherits.
    

#### `def initialize(self)`

Initializes the building block with specific values.

#### `def close(self)`

Closes the building block and releases its internal resources.

### `class TestBuildingBlockUsingDAQmx(unittest.TestCase)`

Defines a test fixture that checks child classes of BuildingBlockUsingDAQmx are ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_child_initalization_without_arguments(self)`

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/__init__.py

### MODULE DOCSTRING

Provides a set of integration tests for nipcbatt.pcbatt_library package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_current_measurements/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_current_measurements/__init__.py

### MODULE DOCSTRING

Provides a set of integration tests for nipcbatt.pcbatt_library.dc_rms_current_measurements package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_current_measurements/test_integration_dc_rms_current_measurement.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_current_measurements/test_integration_dc_rms_current_measurement.py

### MODULE DOCSTRING

This module provides test of integration of DcRmsCurrentMeasurement.

### `class TestIntegrationDcRmsCurrentMeasurement(unittest.TestCase)`

Defines a test fixture that checks the integration of
    `DcRmsCurrentMeasurement` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_integration_dc_rms_current_measurement_configure_only(self)`

Integration test of
        nipcbatt.pcbatt_library.dc_rms_current_measurements.dc_rms_current_measurement.DcRmsCurrentMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY

#### `def test_integration_dc_rms_current_measurement_configure_only_and_measure_only(self)`

Integration test of
        daq.pcbatt_library.dc_rms_current_measurements.dc_rms_current_measurement.DcRmsCurrentMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY

#### `def test_integration_dc_rms_current_measurement_configure_and_measure(self)`

Integration test of
        daq.pcbatt_library.dc_rms_current_measurements.dc_rms_current_measurement.DcRmsCurrentMeasurement
        with MeasurementExecutionType.CONFIGURE_AND_MEASURE.
        

#### `def test_integration_dc_rms_current_measurement_full_sequence_in_loop(self)`

Integration test of
        daq.pcbatt_library.dc_rms_current_measurements.dc_rms_current_measurement.DcRmsCurrentMeasurement
        to be called in a loop.
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_current_measurements/test_integration_dmm_dcrms_current_measurements.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_current_measurements/test_integration_dmm_dcrms_current_measurements.py

### MODULE DOCSTRING

This module provides test of integration of DMM DC RMS current generation

### `class TestIntegrationDmmDcRmsCurrentMeasurement(unittest.TestCase)`

Definte a test fixture that check the integration of 
    'DmmDCRmsCurrent'
    
    Args:
        unittest.TestCase: Base class from which this class inherits
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_initialize_configure_measure_close_dc(self)`

Happy path: DC current configure & measure.

#### `def test_initialize_and_close_is_idempotent(self)`

Tests if class methods are idempotent

#### `def test_configure_only_returns_none(self)`

Ensures configure only returns none

#### `def test_measure_only_reads_and_wraps(self)`

Ensure measure only reads

#### `def test_configure_measure_ac(self)`

AC current measurement should apply ac_min_frequency.

#### `def test_trigger_disabled(self)`

Trigger disabled should force IMMEDIATE trigger.

#### `def test_multiple_ranges_and_resolutions(self)`

Verify several measurement function parameters work.

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_voltage_measurements/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_voltage_measurements/__init__.py

### MODULE DOCSTRING

Provides a set of integration tests for nipcbatt.pcbatt_library.dc_rms_voltage_measurements package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_voltage_measurements/test_integration_dc_rms_voltage_measurement.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_voltage_measurements/test_integration_dc_rms_voltage_measurement.py

### MODULE DOCSTRING

This module provides test of integration of DcRmsVoltageMeasurement.

### `class TestIntegrationDcRmsVoltageMeasurement(unittest.TestCase)`

Defines a test fixture that checks the integration of
    `DcRmsVoltageMeasurement` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_integration_dc_rms_voltage_measurement_configure_only(self)`

Integration test of
        daq.pcbatt_library.dc_rms_voltage_measurements.dc_rms_voltage_measurement.DcRmsVoltageMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY

#### `def test_integration_dc_rms_voltage_measurement_configure_and_measure(self)`

Integration test of
        nipcbatt.pcbatt_library.dc_rms_voltage_measurements.dc_rms_voltage_measurement.DcRmsVoltageMeasurement
        with MeasurementExecutionType.CONFIGURE_AND_MEASURE

#### `def test_integration_dc_rms_voltage_measurement_configure_only_and_measure_only(self)`

Integration test of
        daq.pcbatt_library.dc_rms_voltage_measurements.dc_rms_voltage_measurement.DcRmsVoltageMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_voltage_measurements/test_integration_dmm_dcrms_voltage_measurements.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_voltage_measurements/test_integration_dmm_dcrms_voltage_measurements.py

### MODULE DOCSTRING

This module provides test of integration of DMM DC RMS voltage generation

### `class TestIntegrationDmmDcRmsVoltageMeasurement(unittest.TestCase)`

Definte a test fixture that check the integration of 
    'DmmDCRmsVoltage'
    
    Args:
        unittest.TestCase: Base class from which this class inherits
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_configure_only_dc_voltage(self)`

CONFIGURE_ONLY should not perform a measurement.

#### `def test_measure_only_dc_voltage(self)`

MEASURE_ONLY should read and return a result.

#### `def test_configure_and_measure_dc_voltage_trigger_disabled(self)`

Trigger disabled forces IMMEDIATE and -1.0 delay.

#### `def test_configure_and_measure_ac_voltage(self)`

AC voltage measurement should apply ac_min_frequency and slope.

#### `def test_multiple_voltage_ranges_and_resolutions(self)`

Exercise several voltage ranges and a common resolution.

#### `def test_voltage_initialize_and_close_is_idempotent(self)`

Initialize then close twice to ensure no error and powerline is set.

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_voltage_generations/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_voltage_generations/__init__.py

### MODULE DOCSTRING

Provides a set of integration tests for nipcbatt.pcbatt_library.dc_voltage_generations package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_voltage_generations/test_integration_dc_voltage_generation.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_voltage_generations/test_integration_dc_voltage_generation.py

### MODULE DOCSTRING

This module provides test of integration of DcVoltageGeneration.

### `class TestIntegrationDcVoltageGeneration(unittest.TestCase)`

Defines a test fixture that checks the integration of
    `DcVoltageGeneration` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_dc_voltage_generation_generate_only(self)`

Checks if class `DcVoltageGeneration' can generate with just the initial configurations

#### `def test_dc_voltage_generation_generate_voltage_with_configure_and_generate_in_loop(self)`

Checks if class `DcVoltageGeneration' can configure and generate when they are called one after the other.

#### `def test_dc_voltage_generation_generate_voltage_with_incorrect_output_voltages(self)`

Checks if class `DcVoltageGeneration' throws expected error when called with invalid output_voltages

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_clock_generations/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_clock_generations/__init__.py

### MODULE DOCSTRING

Provides a set of integration tests for nipcbatt.pcbatt_library.digital_clock_generations package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_clock_generations/test_integration_digital_clock_generation.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_clock_generations/test_integration_digital_clock_generation.py

### MODULE DOCSTRING

This module provides test of integration of DigitalClockGeneration.

- `CHANNEL = 'NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/ctr0'`

- `TERMINAL = '/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0'`

### `class TestIntegrationDigitalClockGeneration(unittest.TestCase)`

Defines a test fixture to verify the integration of the
       'DigitalClockGeneration' class

    Args:
        unittest.TestCase: Base class of the unittest framework
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_integration_digital_clock_generation_counter_channel_expression_is_empty(self)`

Integration test ensuring that is channel expression
        is empty then initialize() catches the error
        

#### `def test_integration_digital_clock_generation_counter_channel_expression_is_none(self)`

Integration test ensuring that is channel expression
        is null then initialize() catches the error
        

#### `def test_integration_digital_clock_generation_output_terminal_is_empty(self)`

Integration test ensuring that if terminal
        is empty then initialize() catches the error
        

#### `def test_integration_digital_clock_generation_output_terminal_is_none(self)`

Integration test ensuring that if terminal
        is null then initialize() catches the error
        

#### `def test_integration_digital_clock_generation_configure_counter_only(self)`

Integration test of Digital Clock Generation that ensure an instance
        of DigitalClockGeneration is successfully initialized and configured
        when given correct inputs

#### `def test_integration_digital_clock_generation_configure_and_measure(self)`

Integration test of Digital Frequency Measurement that ensures
        a DigitalClockGeneration isntance is successfully returned
        when given the necessary inputs
        

#### `def test_integration_digital_clock_generation_negative_vales(self)`

Integration test of Digital Frequency Measurement that ensures
        a DigitalClockGeneration instantiation fails if given a negative
        value for any parameter
        

#### `def test_integration_digital_clock_generation_duty_cycle(self)`

Integration test of Digital Frequency Measurement that ensures
        a DigitalClockGeneration instantiation fails if given a value
        greater than 1.0 or is provided for duty cycle
        

#### `def test_integration_digital_clock_generation_zero_duration(self)`

Integration test of Digital Frequency Measurement that ensures
        a DigitalClockGeneration instantiation fails if given a value
        of 0 for duration
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_edge_count_measurements/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_edge_count_measurements/__init__.py

### MODULE DOCSTRING

Provides a set of integration tests 
for nipcbatt.pcbatt_library.digital_edge_count_measurements package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_edge_count_measurements/test_integration_digital_edge_count_measurement.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_edge_count_measurements/test_integration_digital_edge_count_measurement.py

### MODULE DOCSTRING

This module provides test of integration of DigitalEdgeCountMeasurementUsingSoftwareTimer
   and DigitalEdgeCountMeasurementUsingHardwareTimer.

### `class TestIntegrationDigitalEdgeCountMeasurement(unittest.TestCase)`

Defines a test fixture that checks the integration of
    `DigitalEdgeCountMeasurementUsingHardwareTimer` and
    'DigitalEdgeCountMeasurementUsingSoftwareTimer' classes.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_integration_test_digital_edge_count_measurement_using_hardware_timer_channel_expression_empty(self)`

Integration test ensuring that if channel expression is empty then
        initialize() catches the error

#### `def test_integration_test_digital_edge_count_measurement_using_hardware_timer_channel_expression_is_none(self)`

Integration test ensuring that if channel expression is None then
        initialize() catches the error

#### `def test_integration_test_digital_edge_count_measurement_using_hardware_timer_input_terminal_empty(self)`

Integration test ensuring that if measurement_input_terminal_name is empty then
        initialize() catches the error

#### `def test_integration_test_digital_edge_count_measurement_using_hardware_timer_input_terminal_is_none(self)`

Integration test ensuring that if measurement_input_terminal_name is None then
        initialize() catches the error

#### `def test_integration_test_digital_edge_count_measurement_using_hardware_timer_timer_channel_expression_empty(self)`

Integration test ensuring that if timer channel expression is empty then
        initialize() catches the error

#### `def test_integration_test_digital_edge_count_measurement_using_hardware_timer_timer_channel_expression_is_none(self)`

Integration test ensuring that if channel expression is None then
        initialize() catches the error

#### `def test_integration_test_digital_edge_count_measurement_using_hardware_timer_configure_only(self)`

Integration test of
        daq.pcbatt_library.digital_edge_count_measurements.test_digital_edge_count_measurement_using_hardware_timer.
        DigitalEdgeCountMeasurementUsingHardwareTimer with MeasurementExecutionType.CONFIGURE_ONLY
        

#### `def test_integration_test_digital_edge_count_measurement_using_hardware_timer_configure_and_measure(self)`

Integration test of
        daq.pcbatt_library.digital_edge_count_measurements.test_digital_edge_count_measurement_using_hardware_timer.
        DigitalEdgeCountMeasurementUsingHardwareTimer with MeasurementExecutionType.CONFIGURE_AND_MEASURE
        

#### `def test_integration_test_digital_edge_count_measurement_using_hardware_timer_configure_only_and_measure_only(self)`

Integration test of
        daq.pcbatt_library.digital_edge_count_measurements.test_digital_edge_count_measurement_using_hardware_timer.
        DigitalEdgeCountMeasurementUsingHardwareTimer with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY

#### `def test_integration_test_digital_edge_count_measurement_using_software_timer_channel_expression_empty(self)`

Integration test ensuring that if channel expression is empty then
        initialize() catches the error

#### `def test_integration_test_digital_edge_count_measurement_using_software_timer_channel_expression_is_none(self)`

Integration test ensuring that if channel expression is None then
        initialize() catches the error

#### `def test_integration_test_digital_edge_count_measurement_using_software_timer_input_terminal_empty(self)`

Integration test ensuring that if channel expression is empty then
        initialize() catches the error

#### `def test_integration_test_digital_edge_count_measurement_using_software_timer_input_terminal_is_none(self)`

Integration test ensuring that if channel expression is None then
        initialize() catches the error

#### `def test_integration_test_digital_edge_count_measurement_using_software_timer_configure_only(self)`

Integration test of
        daq.pcbatt_library.digital_edge_count_measurements.test_digital_edge_count_measurement_using_software_timer.
        DigitalEdgeCountMeasurementUsingSoftwareTimer with MeasurementExecutionType.CONFIGURE_ONLY
        

#### `def test_integration_test_digital_edge_count_measurement_using_software_timer_configure_and_measure(self)`

Integration test of
        daq.pcbatt_library.digital_edge_count_measurements.test_digital_edge_count_measurement_using_software_timer.
        DigitalEdgeCountMeasurementUsingSoftwareTimer with MeasurementExecutionType.CONFIGURE_AND_MEASURE
        

#### `def test_integration_test_digital_edge_count_measurement_using_software_timer_configure_only_and_measure_only(self)`

Integration test of
        daq.pcbatt_library.digital_edge_count_measurements.test_digital_edge_count_measurement_using_software_timer.
        DigitalEdgeCountMeasurementUsingSoftwareTimer with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_frequency_measurements/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_frequency_measurements/__init__.py

### MODULE DOCSTRING

Provides a set of integration tests 
for nipcbatt.pcbatt_library.digital_frequency_measurements package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_frequency_measurements/test_integration_digital_frequency_measurement.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_frequency_measurements/test_integration_digital_frequency_measurement.py

### MODULE DOCSTRING

This module provides test of integration of DigitalFrequencyMeasurement.

- `CHANNEL = 'NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/ctr0'`

- `TERMINAL = '/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0'`

### `class TestIntegrationDigitalFrequencyMeasurement(unittest.TestCase)`

Defines a test fixture to verify the integration of the
       'DigitalFrequencyMeasurment' class

    Args:
        unittest.TestCase: Base class of the unittest framework
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_integration_digital_frequency_measurement_channel_expression_is_empty(self)`

Integration test ensuring that is channel expression
        is empty then initialize() catches the error
        

#### `def test_integration_digital_frequency_measurement_channel_expression_is_none(self)`

Integration test ensuring that is channel expression
        is null then initialize() catches the error
        

#### `def test_integration_digital_frequency_measurement_input_terminal_is_empty(self)`

Integration test ensuring that is input terminal
        is empty then initialize() catches the error
        

#### `def test_integration_digital_frequency_measurement_input_terminal_is_none(self)`

Integration test ensuring that is input terminal
        is null then initialize() catches the error
        

#### `def test_integration_digital_frequency_measurement_configure_counter_channel_only(self)`

Integration test of Digital Frequency Measurement that ensures
        a DigitalFrequencyMeasurement is successfully configured
        when given the necessary inputs
        

#### `def test_integration_digital_frequency_measurement_configure_and_measure(self)`

Integration test of Digital Frequency Measurement that ensures
        a DigitalFrequencyMeasurementResultData is successfully returned
        when given the necessary inputs
        

#### `def test_integration_digital_frequency_measurement_negative_frequency(self)`

Integration test of Digital Frequency Measurement that ensures
        an error is thrown when a negative minimum frequency is used
        

#### `def test_integration_digital_frequency_measurement_zero_divisor(self)`

Integration test of Digital Frequency Measurement that ensures
        an error is thrown when 0 is used for the input divisor
        

#### `def test_integration_digital_frequency_measurement_zero_duration(self)`

Integration test of Digital Frequency Measurement that ensures
        an error is thrown when 0 is used for the measurement duration
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_pulse_generations/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_pulse_generations/__init__.py

### MODULE DOCSTRING

Provides a set of integration tests
for nipcbatt.pcbatt_library.digital_pulse_generations package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_pulse_generations/test_integration_digital_pulse_generation.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_pulse_generations/test_integration_digital_pulse_generation.py

### MODULE DOCSTRING

This module provides test of integration of DigitalPulseGeneration.

- `CHANNEL = 'NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/ctr0'`

- `TERMINAL = '/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0'`

### `class TestIntegrationDigitalPulseGeneration(unittest.TestCase)`

Defines a test fixture to verify the integration of the
       'DigitalPulseGeneration' class

    Args:
        unittest (_type_): _description_
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_integration_digital_pulse_generation_channel_expression_empty(self)`

Integration test ensuring that if channel expression is empty then
        initialize() catches the error

#### `def test_integration_digital_pulse_generation_channel_expression_is_none(self)`

Integration test ensuring that if channel expression is None then
        initialize() catches the error

#### `def test_integration_digital_pulse_generation_terminal_empty(self)`

Integration test ensuring that if input terminal
        is empty then initialize() catches the error
        

#### `def test_integration_digital_pulse_generation_terminal_is_none(self)`

Integration test ensuring that if input terminal
        is null then initialize() catches the error
        

#### `def test_integration_digital_pulse_generation_configure_and_generate(self)`

Integration test of Digital Pulse Generation that ensures an instance
        of DigitalPulseGeneration is successfully executed when configure
        and measure is performed

#### `def test_integration_digital_pulse_generation_negative_values(self)`

Integration test of Digital Pulse Generation that ensures
        a DigitalPulseGeneration instantiation fails if given a negative
        value for any parameter
        

#### `def test_integration_digital_pulse_generation_no_idle_state_defined(self)`

Integration test of Digital Pulse Generation that ensures an instance
        of DigitalPulseGeneration is successfully executed when the user does not
        define an idle state with otherwise valid data

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_pwm_measurements/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_pwm_measurements/__init__.py

### MODULE DOCSTRING

Provides a set of integration tests
for nipcbatt.pcbatt_library.digital_pwm_measurements package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_pwm_measurements/test_integration_digital_pwm_measurement.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_pwm_measurements/test_integration_digital_pwm_measurement.py

### MODULE DOCSTRING

This module provides test of integration of DigitalPwmMeasurement.

- `CHANNEL = 'NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/ctr0'`

- `TERMINAL = '/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0'`

### `class TestIntegrationDigitalPwmMeasurement(unittest.TestCase)`

Defines a test fixture to verify the integration of the
       'DigitalPwmMeasurment' class

    Args:
        unittest.TestCase: Base class of the unittest framework
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_integration_digital_pwm_measurement_channel_expression_empty(self)`

Integration test ensuring that if channel expression
        is empty then initialize() catches the error
        

#### `def test_integration_digital_pwm_measurement_channel_expression_is_none(self)`

Integration test ensuring that if channel expression
        is null then initialize() catches the error
        

#### `def test_integration_digital_pwm_measurement_input_terminal_empty(self)`

Integration test ensuring that if input terminal
        is empty then initialize() catches the error
        

#### `def test_integration_digital_pwm_measurement_input_terminal_is_none(self)`

Integration test ensuring that if input terminal
        is null then initialize() catches the error
        

#### `def test_integration_digital_pwm_measurement_configure_only(self)`

Integration test of Digital PWM Measurement that ensures an instance
        of DigitalPwmMeasurement is successfully initialized and configured
        given correct inputs

#### `def test_integration_digital_pwm_measurement_measure_only(self)`

Integration test of Digital PWM measurement that ensures an instance
        of DigitalPwmMeasurement is successfully executed when measure only
        is selected as the execution option

#### `def test_integration_digital_pwm_measurement_both_configure_and_measure(self)`

Integration test of Digital PWM measurement that ensures an instance
        of DigitalPwmMeasurement is successfully executed when both configure
        and measure is selected as the execution option

#### `def test_integration_digital_pwm_negative_values(self)`

Integration test of Digital Pwm measurement that ensures
        a DigitalPwmMeasurement instantiation fails if given a negative
        value for any parameter
        

#### `def test_integration_digital_pwm_measurement_no_edge_defined(self)`

Integration test of Digital PWM measurement that ensures an instance
        of DigitalPwmMeasurement is successfully executed when the user does not
        define an edge

#### `def test_integration_digital_pwm_measurement_no_cycles_defined(self)`

Integration test of Digital PWM measurement that ensures an instance
        of DigitalPwmMeasurement is successfully executed when the user does not
        define a value for cycles

#### `def test_integration_digital_pwm_measurement_no_execution_type_defined(self)`

Integration test of Digital PWM measurement that ensures an instance
        of DigitalPwmMeasurement is successfully executed when the user does not
        define a value for execution type

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dmm_scan/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dmm_scan/__init__.py

### MODULE DOCSTRING

Provides integration tests for DMM Scan functionality.

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dmm_scan/test_integration_dmm_scan_pmps_16V_15C.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dmm_scan/test_integration_dmm_scan_pmps_16V_15C.py

### MODULE DOCSTRING

This module provides comprehensive integration tests for DmmScanPMPS complete workflow.

### `class TestIntegrationDmmScanPMPSWorkflow(unittest.TestCase)`

Defines a test fixture that checks the complete DmmScanPMPS workflow.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

Set up test fixtures.

#### `def tearDown(self)`

Tear down test fixtures.

#### `def setUpClass(cls)`

Set up class-level fixtures.

#### `def tearDownClass(cls)`

Tear down class-level fixtures.

#### `def test_integration_complete_scan_workflow_with_single_measurement(self, mock_dmm_class, mock_switch_class)`

Integration test verifying complete scan workflow with single measurement.

#### `def test_integration_scan_with_multiple_channels(self, mock_dmm_class, mock_switch_class)`

Integration test verifying scan with multiple channels.

#### `def test_integration_scan_with_voltage_measurement(self, mock_dmm_class, mock_switch_class)`

Integration test verifying scan with voltage measurements.

### `class TestIntegrationDmmScanPMPSScanConfiguration(unittest.TestCase)`

Defines a test fixture for testing scan configuration handling.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

Set up test fixtures.

#### `def tearDown(self)`

Tear down test fixtures.

#### `def setUpClass(cls)`

Set up class-level fixtures.

#### `def tearDownClass(cls)`

Tear down class-level fixtures.

#### `def test_integration_scan_configuration_with_mixed_ranges(self, mock_dmm_class, mock_switch_class)`

Integration test with mixed voltage ranges in single scan.

### `class TestIntegrationDmmScanPMPSWithVerboseOutput(unittest.TestCase)`

Defines a test fixture for testing DmmScanPMPS with verbose output.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

Set up test fixtures.

#### `def tearDown(self)`

Tear down test fixtures.

#### `def setUpClass(cls)`

Set up class-level fixtures.

#### `def tearDownClass(cls)`

Tear down class-level fixtures.

#### `def test_integration_scan_with_verbose_output(self, mock_dmm_class, mock_switch_class)`

Integration test verifying verbose output during scan.

### `class TestIntegrationDmmScanPMPSWithShuntHandling(unittest.TestCase)`

Defines a test fixture for testing DmmScanPMPS with shunt handling.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

Set up test fixtures.

#### `def tearDown(self)`

Tear down test fixtures.

#### `def setUpClass(cls)`

Set up class-level fixtures.

#### `def tearDownClass(cls)`

Tear down class-level fixtures.

#### `def test_integration_scan_with_current_channels_and_shunt_handling(self, mock_dmm_class, mock_switch_class)`

Integration test verifying shunt handling for current channels (16+).

#### `def test_integration_scan_with_mixed_voltage_and_current_channels(self, mock_dmm_class, mock_switch_class)`

Integration test with mixed voltage and current channels in one scan.

### `class TestIntegrationDmmScanPMPSPerformance(unittest.TestCase)`

Defines a test fixture for performance characteristics of DmmScanPMPS.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

Set up test fixtures.

#### `def tearDown(self)`

Tear down test fixtures.

#### `def setUpClass(cls)`

Set up class-level fixtures.

#### `def tearDownClass(cls)`

Tear down class-level fixtures.

#### `def test_integration_scan_returns_valid_timing_information(self, mock_dmm_class, mock_switch_class)`

Integration test verifying scan returns valid timing information.

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dynamic_digital_pattern_generations/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dynamic_digital_pattern_generations/__init__.py

### MODULE DOCSTRING

Provides a set of integration tests for 
   nipcbatt.pcbatt_library.dynamic_digital_pattern_generations package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dynamic_digital_pattern_generations/test_integration_dynamic_digital_pattern_generation.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dynamic_digital_pattern_generations/test_integration_dynamic_digital_pattern_generation.py

### MODULE DOCSTRING

This module provides test of integration of DynamicDigitalPatternGeneration.

- `CHANNEL = 'TS1_DIO/port0/line0:7'`

- `CLOCK_SOURCE = 'OnboardClock'`

- `TRIGGER_SOURCE = '/TS1_Core/PFI0'`

### `class TestIntegrationDynamicDigitalPatternGeneration(unittest.TestCase)`

Defines a test fixture to verify the integration of the
       'DynamicDigitalPatternGeneration' class

    Args:
        unittest: Base class for all tests
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_integration_dynamic_digital_pattern_gen_channel_expression_empty(self)`

Integration test ensuring that if channel expression is empty then
        initialize() catches the error

#### `def test_integration_dynamic_digital_pattern_gen_channel_expression_is_none(self)`

Integration test ensuring that if channel expression
        is null then initialize() catches the error
        

#### `def test_integration_dynamic_digital_pattern_gen_configure_and_measure(self)`

Integration test of Dynamic Digital Pattern Generation that ensures an instance
        of DynamicDigitalPatternGeneration is successfully executed when configure
        and measure is performed

#### `def test_integration_dynamic_digital_pattern_rate_not_float(self)`

Integration test of Dynamic Digital Pattern Generation that ensures an instance
        of DynamicDigitalPatternGeneration is not created if the given sample
        rate is not a float

#### `def test_integration_dynamic_digital_pattern_rate_negative(self)`

Integration test of Dynamic Digital Pattern Generation that ensures an instance
        of DynamicDigitalPatternGeneration is not created if the given sample
        rate is a negative number

#### `def test_integration_dynamic_digital_pattern_signal_empty(self)`

Integration test of Dynamic Digital Pattern Generation that ensures an instance
        of DynamicDigitalPatternGeneration is not created if the given signal is an empty
        array

#### `def test_integration_dynamic_digital_pattern_signal_none(self)`

Integration test of Dynamic Digital Pattern Generation that ensures an instance
        of DynamicDigitalPatternGeneration is not created if the given signal is an empty
        array

#### `def test_integration_dynamic_digital_pattern_signal_wrong_shape(self)`

Integration test of Dynamic Digital Pattern Generation that ensures an instance
        of DynamicDigitalPatternGeneration is not created if the given signal is the
        wrong shape

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dynamic_digital_pattern_measurements/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dynamic_digital_pattern_measurements/__init__.py

### MODULE DOCSTRING

Provides a set of integration tests for 
   nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dynamic_digital_pattern_measurements/test_integration_dynamic_digital_pattern_measurement.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dynamic_digital_pattern_measurements/test_integration_dynamic_digital_pattern_measurement.py

### MODULE DOCSTRING

This module provides test of integration of DynamicDigitalPatternMeasurement.

### `class TestIntegrationDynamicDigitalPatternMeasurement(unittest.TestCase)`

Defines a test fixture that check the integration of the
       'DynamicDigitalPatternMeasurement' class

    Args:
        unittest.TestCase: Base class of the unittest framework
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_integration_dynamic_digital_pattern_meas_channel_expression_empty(self)`

Integration test ensuring that if channel expression is empty then
        initialize() catches the error

#### `def test_integration_dynamic_digital_pattern_meas_channel_expression_is_none(self)`

Integration test ensuring that if channel expression
        is null then initialize() catches the error
        

#### `def test_integration_test_dynamic_digital_pattern_measurement_configure_only(self)`

Integration test of
        nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements.dynamic_digital_pattern_measurement.
        DynamicDigitalPatternMeasurement with MeasurementExecutionType.CONFIGURE_ONLY
        

#### `def test_integration_test_dynamic_digital_pattern_measurement_configure_and_measure(self)`

Integration test of
        nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements.dynamic_digital_pattern_measurement.
        DynamicDigitalPatternMeasurement with MeasurementExecutionType.CONFIGURE_AND_MEASURE
        

#### `def test_integration_test_dynamic_digital_pattern_measurement_configure_only_and_measure_only(self)`

Integration test of
        nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements.dynamic_digital_pattern_measurement.
        DynamicDigitalPatternMeasurement with MeasurementExecutionType.MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/frequency_domain_measurements/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/frequency_domain_measurements/__init__.py

### MODULE DOCSTRING

Provides a set of integration tests for 
   nipcbatt.pcbatt_library.frequency_domain_measurements package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/frequency_domain_measurements/test_integration_frequency_domain_measurement.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/frequency_domain_measurements/test_integration_frequency_domain_measurement.py

### MODULE DOCSTRING

This module provides test of integration of FrequencyDomainMeasurement.

### `class TestIntegrationFrequencyDomainMeasurement(unittest.TestCase)`

Defines a test fixture that checks the integration of
    `FrequencyDomainMeasurement` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_integration_frequency_domain_measurement_configure_only(self)`

Integration test of
        nipcbatt.pcbatt_library.frequency_domain_measurements.frequency_domain_measurement.FrequencyDomainMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY

#### `def test_integration_frequency_domain_measurement_configure_and_measure(self)`

Integration test of
        nipcbatt.pcbatt_library.frequency_domain_measurements.frequency_domain_measurement.FrequencyDomainMeasurement
        with MeasurementExecutionType.CONFIGURE_AND_MEASURE

#### `def test_integration_frequency_domain_measurement_configure_only_and_measure_only(self)`

Integration test of
        nipcbatt.pcbatt_library.frequency_domain_measurements.frequency_domain_measurement.FrequencyDomainMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY

#### `def test_integration_time_domain_measurement_configure_only_and_measure_only_in_loop(self)`

Integration test of
        nipcbatt.pcbatt_library.time_domain_measurements.time_domain_measurement.TimeDomainMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/i2c_communications/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/i2c_communications/__init__.py

### MODULE DOCSTRING

Provides a set of integration tests for 
   nipcbatt.pcbatt_library.i2c_communications package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/i2c_communications/test_integration_i2c_read_communication.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/i2c_communications/test_integration_i2c_read_communication.py

### MODULE DOCSTRING

This module provides test of integration of I2CReadCommunication.

### `class TestIntegrationI2cReadCommunication(unittest.TestCase)`

Defines a test fixture that checks the integration of
    `I2cReadCommunication` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_integration_i2c_read_communication(self)`

Integration test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_read_communication.I2cReadCommunication
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/i2c_communications/test_integration_i2c_write_communication.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/i2c_communications/test_integration_i2c_write_communication.py

### MODULE DOCSTRING

This module provides test of integration of I2CWriteCommunication.

### `class TestIntegrationI2cWriteCommunication(unittest.TestCase)`

Defines a test fixture that checks the integration of
    `I2cWriteCommunication` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_integration_i2c_write_communication(self)`

Integration test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_communication.I2cWriteCommunication
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/mixed_measurement/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/mixed_measurement/__init__.py

### MODULE DOCSTRING

Provides a set of integration tests for nipcbatt.pcbatt_library.mixed_measurements package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/mixed_measurement/test_integration_dmm_mixed_measurement.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/mixed_measurement/test_integration_dmm_mixed_measurement.py

### MODULE DOCSTRING

This module provides integration tests for DMM mixed measurement.

### `class TestIntegrationMixedMeasurement(unittest.TestCase)`

Defines integration checks for `dmm.MixedMeasurement`.

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def _create_initialized_uut(self) -> dmm.MixedMeasurement`

#### `def test_initialize_configure_measure_close_dc_voltage(self)`

Happy path: DC voltage mixed measurement configure and measure.

#### `def test_configure_only_returns_none(self)`

Ensures CONFIGURE_ONLY execution returns None.

#### `def test_measure_only_reads_and_wraps_result(self)`

Ensures MEASURE_ONLY returns mixed measurement result data.

#### `def test_ac_measurement_applies_ac_min_frequency(self)`

AC measurement path should apply configured AC minimum frequency.

#### `def test_multiple_mixed_ranges(self)`

Verifies mixed measurement with multiple function/range settings.

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/power_supply_source_and_measurements/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/power_supply_source_and_measurements/__init__.py

### MODULE DOCSTRING

Provides a set of integration tests for 
   nipcbatt.pcbatt_library.power_supply_source_and_measurements package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/power_supply_source_and_measurements/test_integration_power_supply_source_and_measure.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/power_supply_source_and_measurements/test_integration_power_supply_source_and_measure.py

### MODULE DOCSTRING

This module provides test of integration of PowerSupplySourceAndMeasure check.

### `class TestIntegrationPowerSupplySourceAndMeasureMeasurement(unittest.TestCase)`

Defines a test fixture that checks the integration of
    `PowerSupplySourceAndMeasure` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_integration_power_supply_and_source_measurement_configure_only(self)`

Integration test of
        nipcbatt.pcbatt_library.power_supply_source_and_measurements.power_supply_source_and_measure.PowerSupplySourceAndMeasure
         with MeasurementExecutionType.CONFIGURE_ONLY

#### `def test_integration_power_supply_and_source_measurement_configure_only_measure_only(self)`

Integration test of
        nipcbatt.pcbatt_library.power_supply_source_and_measurements.power_supply_source_and_measure.PowerSupplySourceAndMeasure
         with MeasurementExecutionType.CONFIGURE_ONLY and MeasurementExecutionType.MEASURE_ONLY
        

#### `def test_integration_power_supply_and_source_measurement_configure_and_measure(self)`

Integration test of
        nipcbatt.pcbatt_library.power_supply_source_and_measurements.power_supply_source_and_measure.PowerSupplySourceAndMeasure
         with MeasurementExecutionType.CONFIGURE_AND_MEASURE
        

#### `def test_integration_power_supply_and_source_measurement_full_sequence_in_loop(self)`

Integration test of
        nipcbatt.pcbatt_library.power_supply_source_and_measurements.power_supply_source_and_measure.PowerSupplySourceAndMeasure
        for initialize, configure and measure and close to be called in loop with the same context.
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/resistance_measurments/test_dmm_resistance_measurements.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/resistance_measurments/test_dmm_resistance_measurements.py

### MODULE DOCSTRING

This module provides test of integration of DMM resistance measurement

### `class TestIntegrationDmmResistanceMeasurement(unittest.TestCase)`

Definte a test fixture that check the integration of 
    'DmmDCRmsVoltage'
    
    Args:
        unittest.TestCase: Base class from which this class inherits
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_configure_only_resistance(self)`

CONFIGURE_ONLY should not perform a measurement.

#### `def test_measure_only_resistance(self)`

MEASURE_ONLY should read and return a result.

#### `def test_configure_and_measure_resistance_2w_trigger_disabled(self)`

Trigger disabled forces IMMEDIATE and -1.0 delay.

#### `def test_configure_and_measure_resistance_4w_trigger_enabled(self)`

4-wire resistance with trigger enabled uses provided source/delay and slope.

#### `def test_multiple_resistance_ranges_and_resolutions(self)`

Exercise several 2W and 4W resistance ranges with a common resolution.

#### `def test_resistance_initialize_and_close_is_idempotent(self)`

Initialize then close twice to ensure no error and powerline is set.

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/serial_communications/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/serial_communications/__init__.py

### MODULE DOCSTRING

Provides a set of integration tests for 
   nipcbatt.pcbatt_library.serial_communications package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/serial_communications/test_integration_serial_communication.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/serial_communications/test_integration_serial_communication.py

### MODULE DOCSTRING

This module provides test of integration of SerialCommunication.

### `class TestIntegrationSerialCommunication(unittest.TestCase)`

Defines a test fixture that checks the integration of
    `SerialCommunication` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_integration_serial_communication(self)`

Integration test of
        nipcbatt.pcbatt_library.serial_communications.serial_communication.SerialCommunication
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/signal_voltage_generations/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/signal_voltage_generations/__init__.py

### MODULE DOCSTRING

Provides a set of integration tests for 
   nipcbatt.pcbatt_library.signal_voltage_generations package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/signal_voltage_generations/test_integration_signal_voltage_generation.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/signal_voltage_generations/test_integration_signal_voltage_generation.py

### MODULE DOCSTRING

This module provides test of integration of SignalVoltageGeneration.

### `class TestIntegrationSignalVoltageGeneration(unittest.TestCase)`

Defines a test fixture that checks the integration of
    `SignalVoltageGeneration` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_signal_voltage_generation_generate_only(self)`

Checks if class `SignalVoltageGeneration' can generate
        with just the initial configurations

#### `def test_signal_voltage_generation_configure_and_generate_in_loop(self)`

Checks if class `SignalVoltageGeneration' can configure and generate
        when they are called one after the other.

#### `def test_signal_voltage_generation_for_configure_and_generate_sine_wave(self)`

Checks if class `SignalVoltageGeneration' can configure and generate sine wave.

#### `def test_signal_voltage_generation_for_configure_and_generate_square_wave(self)`

Checks if class `SignalVoltageGeneration' can configure and generate square wave.

#### `def test_signal_voltage_generation_for_configure_and_generate_multiple_tones_sine_signal(self)`

Checks if class `SignalVoltageGeneration' can configure and generate
        multiple tones signal.

#### `def test_signal_voltage_generation_route_sample_clock_signal_to_terminal(self)`

Checks if class `SignalVoltageGeneration' can configure and export the
        sample clock signal to the specified terminal

#### `def test_signal_voltage_generation_route_digital_trigger_signal_to_terminal(self)`

Checks if class `SignalVoltageGeneration' can configure and export the
        digital trigger signal to the specified terminal

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/spi_communications/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/spi_communications/__init__.py

### MODULE DOCSTRING

Provides a set of integration tests for 
   nipcbatt.pcbatt_library.spi_communications package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/spi_communications/test_integration_spi_read_communication.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/spi_communications/test_integration_spi_read_communication.py

### MODULE DOCSTRING

This module provides test of integration of SpiReadCommunication.

### `class TestIntegrationSpiReadCommunication(unittest.TestCase)`

Defines a test fixture that checks the integration of
    `SpiReadCommunication` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_integration_spi_read_communication(self)`

Integration test of
        communications.pcbatt_library.spi_communications.spi_read_communication.SpiReadCommunication
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/spi_communications/test_integration_spi_write_communication.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/spi_communications/test_integration_spi_write_communication.py

### MODULE DOCSTRING

This module provides test of integration of SpiWriteCommunication.

### `class TestIntegrationSpiWriteCommunication(unittest.TestCase)`

Defines a test fixture that checks the integration of
    `SpiWriteCommunication` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_integration_spi_write_communication(self)`

Integration test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_communication.SpiWriteCommunication
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_path_generations/test_integration_static_digital_path_generation.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_path_generations/test_integration_static_digital_path_generation.py

### MODULE DOCSTRING

This module provide test of integration of StaticDigitalPathGeneration

### `class TestIntegrationStaticDigitalPathGeneration(unittest.TestCase)`

Definte a test fixture that chceck the integration of 
    'StaticDigitalPathGneration'
    
    Args:
        unittest.TestCase: Base class from which this class inherits
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_static_digital_path_initialize_generate_close(self)`

Checks happy path -- initialize/close are called without incident

#### `def test_bank1_ch20_to_com1_connect_disconnect(self)`

Bank 1 happy path: ch20 <-> com1 connect, then disconnect.

#### `def test_reject_channel_to_channel(self)`

Mux cannot short two inputs: ch0 <-> ch1 should result in PATH_UNSUPPORTED.

#### `def test_reject_cross_bank_common_mismatch(self)`

Channel must route to its bank common: ch3 <-> com1 should be unsupported.

#### `def test_topology_change_requires_reset_then_succeeds(self)`


        If the device is on a different topology, reset_device=False should fail.
        Then reset_device=True should succeed. If already matching, skip the first part.
        

#### `def test_idempotent_connect_disconnect(self)`

Calling connect/disconnect for the same pair repeatedly should be harmless.

#### `def test_multiple_sequential_routes_single_session(self)`

Connect/disconnect several valid pairs sequentially in one session.

#### `def test_zero_debounce_is_accepted(self)`

Zero debounce should be accepted (as 'no wait' or driver default).

#### `def test_disconnect_without_prior_connect(self)`

Disconnecting a non-existent path throw an error.

#### `def test_error_on_repeated_close(self)`

Calling close twice without initialize should throw an error.

#### `def test_sdpg_case1(self)`

Executes the first test defined in the SDPG Cases Individual Test Plan

#### `def test_sdpg_case2(self)`

Executes the second test defined in the SDPG Cases Individual Test Plan

#### `def test_sdpg_case3(self)`

Executes the third test defined in the SDPG Cases Individual Test Plan

#### `def test_sdpg_case4(self)`

Executes the fourth test defined in the SDPG Cases Individual Test Plan

#### `def test_sdpg_case5(self)`

Executes the fifth test defined in the SDPG Cases Individual Test Plan

#### `def test_sdpg_case6(self)`

Executes the sixth test defined in the SDPG Cases Individual Test Plan

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_state_generations/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_state_generations/__init__.py

### MODULE DOCSTRING

Provides a set of integration tests for 
   nipcbatt.pcbatt_library.static_digital_state_generations package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_state_generations/test_integration_static_digital_state_generation.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_state_generations/test_integration_static_digital_state_generation.py

### MODULE DOCSTRING

This module provides test of integration of StaticDigitalStateGeneration.

### `class TestIntegrationStaticDigitalStateGeneration(unittest.TestCase)`

Defines a test fixture to verify the integration of the
       'StaticDigitalStateGeneration' class

    Args:
        unittest.TestCase: Base class of the unittest framework
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_integration_num_channels_8(self)`

Integration test ensuring the module creates the correct output
        when given 8 channels of data to write
        

#### `def test_integration_num_channels_23(self)`

Integration test ensuring the module creates the correct output
        when given 23 channels of data to write
        

#### `def test_integration_channel_expression_is_empty(self)`

Integration test ensuring that is channel expression
        is empty then initialize() catches the error
        

#### `def test_integration_channel_expression_is_none(self)`

Integration test ensuring that is channel expression
        is null then initialize() catches the error
        

#### `def test_integration_channel_expression_port(self)`

Integration test ensuring that the channel expression
        value consisting of only 'port' with channel
        designated will throw an error
        

#### `def test_integration_channel_expression_only_instrument(self)`

Integration test that channel expression value of only 'port'
        without channels designated throws an error
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_state_measurements/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_state_measurements/__init__.py

### MODULE DOCSTRING

Provides a set of integration tests for 
   nipcbatt.pcbatt_library.static_digital_state_measurements package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_state_measurements/test_integration_static_digital_state_measurement.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_state_measurements/test_integration_static_digital_state_measurement.py

### MODULE DOCSTRING

This module provides test of integration of StaticDigitalStateMeasurement.

### `class TestIntegrationStaticDigitalStateMeasurement(unittest.TestCase)`

Defines a test fixture that check the integration of the
       'StaticDigitalStateMeasurement' class

    Args:
        unittest.TestCase: Base class of the unittest framework
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_integration_num_channels_and_num_data_len_9(self)`

Integration test ensuring that the module creates
        the correct output object in terms of numbers of
        channels and the associated data, both of length 8
        

#### `def test_integration_num_channels_and_num_data_len_5(self)`

Integration test ensuring that the module creates
        the correct output object in terms of numbers of
        channels and the associated data, both of length 5
        

#### `def test_integration_channel_expression_is_none(self)`

Integration test ensuring that if channel expression is None
        then initialize() properly catches this error
        

#### `def test_integration_channel_expression_is_empty(self)`

Integration test ensuring that if channel expression is empty
        then initialize() properly catches this error
        

#### `def test_integration_channel_expression_port(self)`

Integration test ensuring that channel expression value
        of only 'port' without channels designated throws the proper error
        

#### `def test_integration_channel_expression_only_instrument(self)`

Integration test ensuring that channel expression value
        of only 'port' without channels designated throws the proper error
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/temperature_measurements/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/temperature_measurements/__init__.py

### MODULE DOCSTRING

Provides a set of integration tests for 
   nipcbatt.pcbatt_library.temperature_measurements package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/temperature_measurements/test_integration_temperature_measurement_using_rtd.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/temperature_measurements/test_integration_temperature_measurement_using_rtd.py

### MODULE DOCSTRING

This module provides test of integration of TemperatureMeasurementUsingRtd.

### `class TestIntegrationTemperatureMeasurementUsingRtd(unittest.TestCase)`

Defines a test fixture that checks the integration of
    `TemperatureMeasurementUsingRtd` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_integration_temperature_measurement_using_rtd_configure_only(self)`

Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_rtd.TemperatureMeasurementUsingRtd
        with MeasurementExecutionType.CONFIGURE_ONLY

#### `def test_integration_temperature_measurement_using_rtd_configure_and_measure(self)`

Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_rtd.TemperatureMeasurementUsingRtd
        with MeasurementExecutionType.CONFIGURE_AND_MEASURE

#### `def test_integration_temperature_measurement_using_rtd_configure_only_and_measure_only(self)`

Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_rtd.TemperatureMeasurementUsingRtd
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY

#### `def test_integration_temperature_measurement_using_rtd_configure_only_and_measure_only_in_loop(self)`

Integration test of
        nipcbatt.pcbatt_library.time_domain_measurements.time_domain_measurement.TimeDomainMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/temperature_measurements/test_integration_temperature_measurement_using_thermistor.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/temperature_measurements/test_integration_temperature_measurement_using_thermistor.py

### MODULE DOCSTRING

This module provides test of integration of TemperatureMeasurementUsingThermistor.

- `TEMPERATURE_THERMISTOR_RANGE_AND_TERMINAL_PARAMETERS_WITH_BETA_COEFFICIENT = nipcbatt.TemperatureThermistorRangeAndTerminalParameters(terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE, temperature_minimum_value_celsius_degrees=0.0, temperature_maximum_value_celsius_degrees=100.0, voltage_excitation_value_volts=6.0, thermistor_resistor_ohms=9980, steinhart_hart_equation_option=nipcbatt.SteinhartHartEquationOption.USE_COEFFICIENT_BETA_AND_SENSOR_RESISTANCE, coefficients_steinhart_hart_parameters=nipcbatt.DEFAULT_COEFFICIENTS_STEINHART_HART_PARAMETERS, beta_coefficient_and_sensor_resistance_parameters=nipcbatt.BetaCoefficientAndSensorResistanceParameters(coefficient_steinhart_hart_beta_kelvins=3720.0, sensor_resistance_ohms=10000.0))`

- `TEMPERATURE_THERMISTOR_RANGE_AND_TERMINAL_PARAMETERS_WITH_COEFFICIENTS = nipcbatt.TemperatureThermistorRangeAndTerminalParameters(terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE, temperature_minimum_value_celsius_degrees=0.0, temperature_maximum_value_celsius_degrees=100.0, voltage_excitation_value_volts=6.0, thermistor_resistor_ohms=9980, steinhart_hart_equation_option=nipcbatt.SteinhartHartEquationOption.USE_STEINHART_HART_COEFFICIENTS, coefficients_steinhart_hart_parameters=nipcbatt.CoefficientsSteinhartHartParameters(coefficient_steinhart_hart_a=0.001295361, coefficient_steinhart_hart_b=0.0002343159, coefficient_steinhart_hart_c=1.018703e-07), beta_coefficient_and_sensor_resistance_parameters=nipcbatt.DEFAULT_BETA_OEFFICIENT_AND_SENSOR_RESISTANCE_PARAMETERS)`

### `class TestIntegrationTemperatureMeasurementUsingRtd(unittest.TestCase)`

Defines a test fixture that checks the integration of
    `TemperatureMeasurementUsingRtd` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_integration_temperature_measurement_using_thermistor_configure_only(self)`

Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_thermistor.TemperatureMeasurementUsingThermistor
        with MeasurementExecutionType.CONFIGURE_ONLY

#### `def test_integration_temperature_measurement_using_thermistor_configure_and_measure(self)`

Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_thermistor.TemperatureMeasurementUsingThermistor
        with MeasurementExecutionType.CONFIGURE_AND_MEASURE

#### `def test_integration_time_domain_measurement_configure_only_and_measure_only(self)`

Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_thermistor.TemperatureMeasurementUsingThermistor
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY

#### `def test_integration_time_domain_measurement_configure_only_and_measure_only_with_beta_coefficient(self)`

Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_thermistor.TemperatureMeasurementUsingThermistor
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY

#### `def test_integration_time_domain_measurement_configure_only_and_measure_only_with_coefficients(self)`

Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_thermistor.TemperatureMeasurementUsingThermistor
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY

#### `def test_integration_time_domain_measurement_configure_only_and_measure_only_in_loop(self)`

Integration test of
        nipcbatt.pcbatt_library.time_domain_measurements.time_domain_measurement.TimeDomainMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/temperature_measurements/test_integration_temperature_measurement_using_thermocouple.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/temperature_measurements/test_integration_temperature_measurement_using_thermocouple.py

### MODULE DOCSTRING

This module provides test of integration of TemperatureMeasurementUsingThermocouple.

### `class TestIntegrationTemperatureMeasurementUsingThermocouple(unittest.TestCase)`

Defines a test fixture that checks the integration of
    `TemperatureMeasurementUsingThermocouple` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_integration_temperature_measurement_using_thermocouple_channel_expression_empty(self)`

Integration test ensuring that if channel expression is empty then
        initialize() catches the error

#### `def test_integration_temperature_measurement_using_thermocouple_channel_expression_is_none(self)`

Integration test ensuring that if channel expression is None then
        initialize() catches the error

#### `def test_integration_temperature_measurement_using_thermocouple_cjc_source_is_none(self)`

Integration test ensuring that if cjc source
        is None then initialize() catches the error
        

#### `def test_integration_temperature_measurement_using_thermocouple_cjc_channel_is_none(self)`

Integration test ensuring that if cjc_channel is null when cjc_source is set to SCANNABLE_CHANNEL,
        then initialize() catches the error
        

#### `def test_integration_temperature_measurement_using_thermocouple_cjc_channel_is_empty(self)`

Integration test ensuring that if cjc_channel is empty when cjc_source is set to SCANNABLE_CHANNEL,
        then configure_and_measure() catches the error
        

#### `def test_integration_temperature_measurement_using_thermocouple_cjc_value_is_none(self)`

Integration test ensuring that if cjc_value is None when cjc_source is set to CONSTANT_USER_VALUE,
        then configure_and_measure() catches the error
        

#### `def test_integration_temperature_measurement_using_thermocouple_configure_only(self)`

Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_thermocouple.
        TemperatureMeasurementUsingthermocouple with MeasurementExecutionType.CONFIGURE_ONLY
        

#### `def test_integration_temperature_measurement_using_thermocouple_configure_and_measure(self)`

Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_thermocouple.
        TemperatureMeasurementUsingthermocouple with MeasurementExecutionType.CONFIGURE_AND_MEASURE
        

#### `def test_integration_temperature_measurement_using_thermocouple_configure_only_and_measure_only(self)`

Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_thermocouple.
        TemperatureMeasurementUsingthermocouple with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY

#### `def test_integration_temperature_measurement_using_thermocouple_configure_only_and_measure_only_in_loop(self)`

Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_thermocouple.
        TemperatureMeasurementUsingthermocouple with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/time_domain_measurements/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/time_domain_measurements/__init__.py

### MODULE DOCSTRING

Provides a set of integration tests for 
   nipcbatt.pcbatt_library.time_domain_measurements package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/time_domain_measurements/test_integration_time_domain_measurement.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_integration_tests/time_domain_measurements/test_integration_time_domain_measurement.py

### MODULE DOCSTRING

This module provides test of integration of TimeDomainMeasurement.

### `class TestIntegrationTimeDomainMeasurement(unittest.TestCase)`

Defines a test fixture that checks the integration of
    `TimeDomainMeasurement` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_integration_time_domain_measurement_configure_only(self)`

Integration test of
        nipcbatt.pcbatt_library.time_domain_measurements.time_domain_measurement.TimeDomainMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY

#### `def test_integration_time_domain_measurement_configure_and_measure(self)`

Integration test of
        nipcbatt.pcbatt_library.time_domain_measurements.time_domain_measurement.TimeDomainMeasurement
        with MeasurementExecutionType.CONFIGURE_AND_MEASURE

#### `def test_integration_time_domain_measurement_configure_only_and_measure_only(self)`

Integration test of
        nipcbatt.pcbatt_library.time_domain_measurements.time_domain_measurement.TimeDomainMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY

#### `def test_integration_time_domain_measurement_configure_only_and_measure_only_in_loop(self)`

Integration test of
        nipcbatt.pcbatt_library.time_domain_measurements.time_domain_measurement.TimeDomainMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for nipcbatt.pcbatt_library package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/common/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/common/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for nipcbatt.pcbatt_library.common package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/common/test_common_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/common/test_common_data_types.py

### MODULE DOCSTRING

This module provides common data types check.

### `class TestMeasurementOptions(unittest.TestCase)`

Defines a test fixture that checks
    `MeasurementOptions` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_measurement_options(self)`

Unit test of nipcbatt.pcbatt_library.common.common_data_types.MeasurementOptions.

### `class TestSampleClockTimingParameters(unittest.TestCase)`

Defines a test fixture that checks
    `SampleClockTimingParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_sample_clock_timing_parameters_init_fails_when_sample_clock_source_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SampleClockTimingParameters.

#### `def test_sample_clock_timing_parameters_init_fails_when_sample_clock_source_is_empty(self)`

Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SampleClockTimingParameters.

#### `def test_sample_clock_timing_parameters_init_fails_when_sample_clock_source_is_whitespace(self)`

Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SampleClockTimingParameters.

#### `def test_sample_clock_timing_parameters_init_fails_when_sampling_rate_hertz_is_less_than_zero(self)`

Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SampleClockTimingParameters.

#### `def test_sample_clock_timing_parameters(self)`

Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SampleClockTimingParameters.

### `class TestDigitalStartTriggerParameters(unittest.TestCase)`

Defines a test fixture that checks
    `DigitalStartTriggerParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_digital_start_trigger_parameters_init_should_not_fail_if_trigger_select_is_no_trigger(self)`

Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.DigitalStartTriggerParameters.
        

#### `def test_digital_start_trigger_parameters(self)`

Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.DigitalStartTriggerParameters.
        

### `class TestMeasurementData(unittest.TestCase)`

Defines a test fixture that checks
    `MeasurementData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_measurement_data_init_fails_when_samples_is_none(self)`

Unit test of nipcbatt.pcbatt_library.common.common_data_types.MeasurementData.

#### `def test_measurement_data_init_fails_when_samples_is_empty(self)`

Unit test of nipcbatt.pcbatt_library.common.common_data_types.MeasurementData.

#### `def test_measurement_data_fails_if_the_array_has_more_than_two_dimensions(self)`

Unit test of nipcbatt.pcbatt_library.common.common_data_types.MeasurementData.

#### `def test_measurement_data(self)`

Unit test of nipcbatt.pcbatt_library.common.common_data_types.MeasurementData.

### `class TestAnalogWaveform(unittest.TestCase)`

Defines a test fixture that checks
    `AnalogWaveform` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_analog_waveform_init_fails_when_channel_name_is_none(self)`

Unit test of nipcbatt.pcbatt_library.common.common_data_types.AnalogWaveform.

#### `def test_analog_waveform_init_fails_when_channel_name_is_empty(self)`

Unit test of nipcbatt.pcbatt_library.common.common_data_types.AnalogWaveform.

#### `def test_analog_waveform_init_fails_when_channel_name_is_whitespace(self)`

Unit test of nipcbatt.pcbatt_library.common.common_data_types.AnalogWaveform.

#### `def test_analog_waveform_init_fails_when_delta_time_seconds_is_less_than_or_equal_to_zero(self)`

Unit test of nipcbatt.pcbatt_library.common.common_data_types.AnalogWaveform.

#### `def test_analog_waveform_init_fails_when_samples_is_none(self)`

Unit test of nipcbatt.pcbatt_library.common.common_data_types.AnalogWaveform.

#### `def test_analog_waveform_init_fails_when_samples_is_empty(self)`

Unit test of nipcbatt.pcbatt_library.common.common_data_types.AnalogWaveform.

#### `def test_analog_waveform(self)`

Unit test of nipcbatt.pcbatt_library.common.common_data_types.AnalogWaveform.

### `class TestAmplitudeSpectrum(unittest.TestCase)`

Defines a test fixture that checks
    `AmplitudeSpectrum` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_amplitude_spectrum_init_fails_when_channel_name_is_none(self)`

Unit test of nipcbatt.pcbatt_library.common.common_data_types.AmplitudeSpectrum.

#### `def test_amplitude_spectrum_init_fails_when_channel_name_is_empty(self)`

Unit test of nipcbatt.pcbatt_library.common.common_data_types.AmplitudeSpectrum.

#### `def test_amplitude_spectrum_init_fails_when_channel_name_is_whitespace(self)`

Unit test of nipcbatt.pcbatt_library.common.common_data_types.AmplitudeSpectrum.

#### `def test_amplitude_spectrum_init_fails_when_spectrum_frequency_resolution_hertz_is_less_than_or_equal_to_zero(self)`

Unit test of nipcbatt.pcbatt_library.common.common_data_types.AmplitudeSpectrum.

#### `def test_amplitude_spectrum_init_fails_when_amplitudes_is_none(self)`

Unit test of nipcbatt.pcbatt_library.common.common_data_types.AmplitudeSpectrum.

#### `def test_amplitude_spectrum_init_fails_when_amplitudes_is_empty(self)`

Unit test of nipcbatt.pcbatt_library.common.common_data_types.AmplitudeSpectrum.

#### `def test_amplitude_spectrum(self)`

Unit test of nipcbatt.pcbatt_library.common.common_data_types.AmplitudeSpectrum.

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/common/test_communication_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/common/test_communication_data_types.py

### MODULE DOCSTRING

This module provides communication data types check.

### `class TestMemoryAddressParameters(unittest.TestCase)`

Defines a test fixture that checks
    `MemoryAddressParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_memory_address_parameters(self)`

Unit test of
        nipcbatt.pcbatt_library.common.communication_data_types.MemoryAddressParameters.
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/common/test_communication_functions.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/common/test_communication_functions.py

### MODULE DOCSTRING

This module provides communication functions check.

### `class TestComputePagesCharacteristics(unittest.TestCase)`

Defines a test fixture that checks
    function `compute_pages_characteristics` is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_compute_pages_characteristics(self, test_case_name: str, memory_start_address: int, number_of_bytes_to_write: int, number_of_bytes_per_page: int, expected_pages_characteristics: List[communications.MemoryPageCharacteristics])`

unit test of compute_pages_characteristics.

### `class TestCreateArrayForSpiReadInstruction(unittest.TestCase)`

Defines a test fixture that checks
    function `create_array_for_spi_read_instruction` is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_create_array_for_spi_read_instruction(self, test_case_name: str, memory_address: int, address_type: nipcbatt.DataMemoryAddressType, address_endianness: nipcbatt.DataMemoryAddressEndianness, number_of_byte_to_read: int, expected_bytes_array: List[int])`

unit test of create_array_for_spi_read_instruction.

### `class TestCreateArrayForSpiWriteInstruction(unittest.TestCase)`

Defines a test fixture that checks
    function `create_array_for_spi_write_instruction` is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_create_array_for_spi_write_instruction(self, test_case_name: str, memory_address: int, address_type: nipcbatt.DataMemoryAddressType, address_endianness: nipcbatt.DataMemoryAddressEndianness, number_of_bytes_to_write: int, expected_bytes_array: List[int])`

unit test of create_array_for_spi_write_instruction.

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/common/test_voltage_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/common/test_voltage_data_types.py

### MODULE DOCSTRING

This module provides voltage data types check.

### `class TestVoltageRangeAndTerminalParameters(unittest.TestCase)`

Defines a test fixture that checks
    `VoltageRangeAndTerminalParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_voltage_range_and_terminal_parameters(self)`

### `class TestVoltageMeasurementChannelAndTerminalRangeParameters(unittest.TestCase)`

Defines a test fixture that checks
    `VoltageMeasurementChannelAndTerminalRangeParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_voltage_measurement_channel_and_terminal_range_parameters(self)`

### `class TestVoltageGenerationChannelParameters(unittest.TestCase)`

Defines a test fixture that checks
    `VoltageGenerationChannelParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_voltage_generation_channel_parameters(self)`

#### `def test_voltage_generation_channel_parameters_with_invalid_inputs(self)`

Tests if the instance creation with invalid parameters throws exception as expected

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_current_measurements/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_current_measurements/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for nipcbatt.pcbatt_library.dc_rms_current_measurements package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_current_measurements/test_dc_rms_current_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_current_measurements/test_dc_rms_current_data_types.py

### MODULE DOCSTRING

This module provides DC-RMS current datatypes check.

### `class TestDcRmsCurrentMeasurementTerminalRangeParameters(unittest.TestCase)`

Defines a test fixture that checks
    `DcRmsCurrentMeasurementTerminalRangeParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_dc_rms_current_measurement_terminal_range_parameters(self)`

Tests if an instance of `DcRmsCurrentMeasurementTerminalRangeParameters`
        is created with the specific values.
        

#### `def test_dc_rms_current_measurement_terminal_range_invalid_parameters(self)`

Tests if the instance creation with invalid parameters throws exception as expected

### `class TestDcRmsCurrentMeasurementChannelAndTerminalRangeParameters(unittest.TestCase)`

Defines a test fixture that checks
    `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_dc_rms_curren_measurement_channel_and_terminal_range_parameters(self)`

Tests if an instance of `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters`
        is created with the specific values.
        

#### `def test_dc_rms_curren_measurement_channel_and_terminal_range_parameters_with_invalid_channel_name(self)`

Tests if the expected value or type error is thrown when creating an instance of
        `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters` with invalid values
        for channel_name string.
        

#### `def test_dc_rms_curren_measurement_channel_and_terminal_range_parameters_when_channel_parameters_is_none(self)`

Tests if the expected value or type error is thrown when creating an instance of
        `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters` when channel_parameters is none.
        

### `class TestDcRmsCurrentMeasurementConfiguration(unittest.TestCase)`

Defines a test fixture that checks
    `DcRmsCurrentMeasurementConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_dc_rms_current_measurement_configuration(self)`

Tests if an instance of `DcRmsCurrentMeasurementConfiguration`
        is created with the specific values.
        

#### `def test_dc_rms_current_measurement_configuration_with_invalid_values_for_specific_channel_parameters(self)`

Test if expected error is thrown when creating an instance
        of `DcRmsCurrentMeasurementConfiguration`
        with invalid values for specific_channel_parameters

#### `def test_dc_rms_current_measurement_configuration_when_global_channel_parameters_is_none(self)`

Test if expected error is thrown when creating an instance
        of `DcRmsCurrentMeasurementConfiguration`
        with global_channel_parameters is set to None

#### `def test_dc_rms_current_measurement_configuration_when_measurement_options_is_none(self)`

Test if expected error is thrown
        when creating an instance of `DcRmsCurrentMeasurementConfiguration`
        when measurement_options is None

#### `def test_dc_rms_current_measurement_configuration_when_sample_clock_timing_parameters_is_none(self)`

Test if expected error is thrown when creating an instance of
        `DcRmsCurrentMeasurementConfiguration`
        when sample_clock_timing_parameters is None

#### `def test_dc_rms_current_measurement_configuration_when_digital_start_trigger_parameters_is_none(self)`

Test if expected error is thrown
        when creating an instance of `DcRmsCurrentMeasurementConfiguration`
        when digital_start_trigger_parameters is None

### `class TestDcRmsCurrentMeasurementResultData(unittest.TestCase)`

Defines a test fixture that checks
    `DcRmsCurrentMeasurementResultData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_dc_rms_current_measurement_result_data(self)`

Tests if an instance of `DcRmsCurrentMeasurementResultData`
        is created with the specific values.
        

#### `def test_dc_rms_current_measurement_result_data_when_waveforms_is_none(self)`

Tests if expected error is thrown when creating an instance of
        `DcRmsCurrentMeasurementResultData` with waveform as none.
        

#### `def test_dc_rms_current_measurement_result_data_when_waveforms_has_item_not_of_type_analogwaveform(self)`

Tests if expected error is thrown when creating an instance of
        `DcRmsCurrentMeasurementResultData` when waveform has an item
        that is not of type `AnalogWaveform`.
        

#### `def test_dc_rms_current_measurement_result_data_when_dc_values_amperes_has_item_not_of_type_float(self)`

Tests if expected error is thrown when creating an instance of
        `DcRmsCurrentMeasurementResultData` when dc_values_amperes
        has an item that is not of type float.
        

#### `def test_dc_rms_current_measurement_result_data_when_rms_values_amperes_has_item_not_of_type_float(self)`

Tests if expected error is thrown when creating an instance of
        `DcRmsCurrentMeasurementResultData` when rms_values_amperes
        has an item that is not of type float.
        

#### `def test_dc_rms_current_measurement_result_data_when_waveforms_and_rms_values_amperes_have_different_lengths(self)`

Tests if expected error is thrown when creating an instance of
        `DcRmsCurrentMeasurementResultData` when waveforms list and
        rms_values_amperes have list have different lengths
        

#### `def test_dc_rms_current_measurement_result_data_when_waveforms_and_dc_values_amperes_have_different_lengths(self)`

Tests if expected error is thrown when creating an instance of
        `DcRmsCurrentMeasurementResultData` when waveforms list and
        dc_values_amperes have list have different lengths
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_current_measurements/test_dc_rms_current_measurement.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_current_measurements/test_dc_rms_current_measurement.py

### MODULE DOCSTRING

This module provides DcRmsCurrentMeasurement check.

### `class TestDcRmsCurrentMeasurement(unittest.TestCase)`

Defines a test fixture that checks
    `DcRmsCurrentMeasurement` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_dc_rms_current_measurement(self)`

Tests for the proper flow of DC-RMS Current Measurement

#### `def test_dc_rms_current_measurement_analysis_with_empty_data(self)`

Tests if calling analyze_measurement_data
        with None as measure_data input raises Attribute error as expected.

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_current_measurements/test_dmm_dc_rms_current_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_current_measurements/test_dmm_dc_rms_current_data_types.py

### MODULE DOCSTRING

 Performs unit tests ensuring the integrity of the datatypes used in 
    DMM-based DC-RMS measurements 

### `class TestDMMDcRmsCurrent(unittest.TestCase)`

Defines a test fixture that ensures the data types of the 
        dmm.DcRmsCurrentMeasurement class are created correctly
        
        Args:
            unittest.TestCase: Base class from which this class inherits
        

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_enum_members_shape_and_types(self)`

Tests the creation of different type and shapes of enums

#### `def test_function_params_basic_construction_and_properties(self)`

Create a DcRmsCurrentMeasurementFunctionParameters and verify properties.

#### `def test_properties_are_effectively_read_only(self)`

Attempting to assign to properties should raise AttributeError.

#### `def test_basic_construction_and_properties(self)`

Create params and verify properties return the same objects.

#### `def test_construct_for_every_current_range_enum_value(self)`

Iterate all CurrentRangeAndFunctions, instantiate params, and verify.

#### `def test_dcrms_meas_config_properties_are_read_only(self)`

Ensure all function properties are read only

#### `def test_identity_of_references(self)`

Make sure the same object is returned, not a copy

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_voltage_measurements/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_voltage_measurements/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for nipcbatt.pcbatt_library.dc_rms_voltage_measurements package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_voltage_measurements/test_dc_rms_voltage_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_voltage_measurements/test_dc_rms_voltage_data_types.py

### MODULE DOCSTRING

This module provides DC-RMS voltage datatypes check.

### `class TestDcRmsVoltageMeasurementConfiguration(unittest.TestCase)`

Defines a test fixture that checks
    `DcRmsVoltageMeasurementConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_dc_rms_voltage_measurement_configuration_init_fails_when_global_channel_parameters_is_none(self)`

unit test of DcRmsVoltageMeasurementConfiguration.

#### `def test_dc_rms_voltage_measurement_configuration_init_fails_when_specific_channels_parameters_is_none(self)`

unit test of DcRmsVoltageMeasurementConfiguration.

#### `def test_dc_rms_voltage_measurement_configuration_init_fails_when_specific_channels_parameters_contains_invalid_objects(self)`

unit test of DcRmsVoltageMeasurementConfiguration.

#### `def test_dc_rms_voltage_measurement_configuration_init_fails_when_measurement_options_is_none(self)`

unit test of DcRmsVoltageMeasurementConfiguration.

#### `def test_dc_rms_voltage_measurement_configuration_init_fails_when_sample_clock_timing_parameters_is_none(self)`

unit test of DcRmsVoltageMeasurementConfiguration.

#### `def test_dc_rms_voltage_measurement_configuration_init_fails_when_digital_start_trigger_parameters_is_none(self)`

unit test of DcRmsVoltageMeasurementConfiguration.

#### `def test_dc_rms_voltage_measurement_configuration(self)`

unit test of DcRmsVoltageMeasurementConfiguration.

### `class TestDcRmsVoltageMeasurementResultData(unittest.TestCase)`

Defines a test fixture that checks
    `DcRmsVoltageMeasurementResultData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_dc_rms_voltage_measurement_result_data_init_fails_when_waveforms_is_none(self)`

unit test of DcRmsVoltageMeasurementResultData.

#### `def test_dc_rms_voltage_measurement_result_data_init_fails_when_waveforms_is_empty(self)`

unit test of DcRmsVoltageMeasurementResultData.

#### `def test_dc_rms_voltage_measurement_result_data_init_fails_when_waveforms_contains_invalid_objects(self)`

unit test of DcRmsVoltageMeasurementResultData.

#### `def test_dc_rms_voltage_measurement_result_data_init_fails_when_dc_values_volts_is_none(self)`

unit test of DcRmsVoltageMeasurementResultData.

#### `def test_dc_rms_voltage_measurement_result_data_init_fails_when_dc_values_volts_is_empty(self)`

unit test of DcRmsVoltageMeasurementResultData.

#### `def test_dc_rms_voltage_measurement_result_data_init_fails_when_dc_values_volts_contains_invalid_objects(self)`

unit test of DcRmsVoltageMeasurementResultData.

#### `def test_dc_rms_voltage_measurement_result_data_init_fails_when_rms_values_volts_is_none(self)`

unit test of DcRmsVoltageMeasurementResultData.

#### `def test_dc_rms_voltage_measurement_result_data_init_fails_when_rms_values_volts_is_empty(self)`

unit test of DcRmsVoltageMeasurementResultData.

#### `def test_dc_rms_voltage_measurement_result_data_init_fails_when_rms_values_volts_contains_invalid_objects(self)`

unit test of DcRmsVoltageMeasurementResultData.

#### `def test_dc_rms_voltage_measurement_result_data(self)`

unit test of DcRmsVoltageMeasurementResultData.

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_voltage_measurements/test_dc_rms_voltage_measurement.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_voltage_measurements/test_dc_rms_voltage_measurement.py

### MODULE DOCSTRING

This module provides DcRmsVoltageMeasurement check.

### `class TestDcRmsVoltageMeasurement(unittest.TestCase)`

Defines a test fixture that checks
    `DcRmsVoltageMeasurement` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_dc_rms_voltage_measurement(self)`

Checks if class DcRmsVoltageMeasurement is ready to use

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_voltage_measurements/test_dmm_dc_rms_voltage_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/dc_rms_voltage_measurements/test_dmm_dc_rms_voltage_data_types.py

### MODULE DOCSTRING

 Performs unit tests ensuring the integrity of the datatypes used in 
    DMM-based DC-RMS voltage measurements 

### `class TestDMMDcRmsVoltage(unittest.TestCase)`

Defines a test fixture that ensures the enums are created 
        correctly
        
        Args:
            unittest.TestCase: Base class from which this class inherits
        

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_enum_members_shape_and_types(self)`

Tests the creation of different type and shapes of enums

#### `def test_properties_are_effectively_read_only(self)`

Attempting to assign to properties should raise AttributeError.

#### `def test_basic_construction_and_properties(self)`

Create params and verify properties return the same objects.

#### `def test_construct_for_every_voltage_range_enum_value(self)`

Iterate all VoltageRangeAndFunctions, instantiate params, and verify.

#### `def test_dcrms_meas_config_properties_are_read_only(self)`

Ensure all function properties are read only

#### `def test_identity_of_references(self)`

Make sure the same object is returned, not a copy

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dc_voltage_generations/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/dc_voltage_generations/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for nipcbatt.pcbatt_library.dc_voltage_generations package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dc_voltage_generations/test_dc_voltage_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/dc_voltage_generations/test_dc_voltage_data_types.py

### MODULE DOCSTRING

This module provides DC Voltage data types check.

### `class TestDcVoltageGenerationConfiguration(unittest.TestCase)`

Defines a test fixture that checks
    'DcVoltageGenerationConfiguration' class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_dc_voltage_generation_configuration(self)`

Tests if the instance of `DcVoltageGenerationConfiguration` is created as expected

#### `def test_dc_voltage_generation_configuration_with_empty_channel_parameters(self)`

Tests if the Value error is raised when tried to create an
        instance of `DcVoltageGenerationConfiguration` with empty channel parameters

#### `def test_dc_voltage_generation_configuration_with_empty_output_voltages(self)`

Tests if the Value error is raised when tried to create an
        instance of `DcVoltageGenerationConfiguration` with empty output_voltages array
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dc_voltage_generations/test_dc_voltage_generation.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/dc_voltage_generations/test_dc_voltage_generation.py

### MODULE DOCSTRING

This module provides DcVoltageGeneration check.

### `class TestDcVoltageGeneration(unittest.TestCase)`

Defines a test fixture that checks
    `DcVoltageGeneration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_dc_voltage_generation(self)`

Checks if class `DcVoltageGeneration' is ready for use

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_clock_generations/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/digital_clock_generations/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for nipcbatt.pcbatt_library.digital_clock_generations package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_clock_generations/test_digital_clock_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/digital_clock_generations/test_digital_clock_data_types.py

### MODULE DOCSTRING

This module provides digital clock data types check.

### `class TestDigitalClockGenerationDataTypes(unittest.TestCase)`

Defines a test fixture to unsure the data types class used for digital clock
       generation are ready to use.

    Args:
        unittest.testCase: Parent class of the unittest framework
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_digital_clock_generation_timing_parameters(self)`

Tests if an instance of DigitalClockGenerationTimingParameters is
        created with specific values

#### `def test_digital_clock_generation_timing_parameters_with_invalid_data(self)`

Tests if an instance of DigitalClockGenerationTimingParameters throws
        an error if given invalid data

#### `def test_digital_clock_generation_counter_channel_parameters(self)`

Tests if an instance of DigitalClockGenerationCounterChannelParameters
        is produced with specfic values

#### `def test_digital_clock_generation_counter_channel_parameters_with_invalid_data(self)`

Tests if an attempted instance of DigitalClockGenerationCounterChannelParameters
        throws an error when given incorrect values

#### `def test_digital_clock_generation_configuration(self)`

Tests if an instance of DigitalClockGenerationConfiguration is
        successfully created when given the proper arugments

#### `def test_digital_clock_generation_configuration_with_invalid_data(self)`

Tests if instantiaion of DigitalClockGenerationConfiguration fails
        when given invalid data

#### `def test_digital_clock_generation_data(self)`

Test if an instance of DigitalClockGenerationData is created
        successfully when given the proper values

#### `def test_digital_clock_generation_with_invalid_data(self)`

Ensures that the attempted creation of an instance of
        DigitalClockGenerationData with invalid data throws an error

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_clock_generations/test_digital_clock_generation.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/digital_clock_generations/test_digital_clock_generation.py

### MODULE DOCSTRING

This module provides DigitalClockGeneration check.

### `class TestDigitalClockGeneration(unittest.TestCase)`

Defines a test fixture that ensures the class 'DigitalClockGeneration' is
       correct and ready to use

    Args:
        unittest.TestCase: Base class for unit tests which is inherited
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_digital_clock_generation(self)`

Checks if class 'DigitalClockGeneration' is ready to use

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_edge_count_measurements/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/digital_edge_count_measurements/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for nipcbatt.pcbatt_library.digital_edge_count_measurements package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_edge_count_measurements/test_digital_edge_count_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/digital_edge_count_measurements/test_digital_edge_count_data_types.py

### MODULE DOCSTRING

This module provides DigitalEdgeCountMeasurementUsingSoftwareTimer
   and DigitalEdgeCountMeasurementUsingHardwareTimer Datatypes check.

### `class TestDynamicDigitalEdgeCountMeasuremntDataTypes(unittest.TestCase)`

Defines a test fixture that checks
    `DigitalEdgeCountMeasuremntDataTypes` class is ready to use.

    Args:
         unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_digital_edge_count_measurement_counter_channel_parameter_init_fails_when_edge_type_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_data_types.DigitalEdgeCountMeasurementCounterChannelParameters.
        

#### `def test_digital_edge_count_measurement_counter_channel_parameter(self)`

Tests if the instance of `DigitalEdgeCountMeasurementCounterChannelParameters`
        is created as expected

#### `def test_digital_edge_count_measurement_timing_parameter_init_fails_when_edge_counting_duration_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_data_types.DigitalEdgeCountMeasurementTimingParameters.
        

#### `def test_digital_edge_count_measurement_timing_parameter_init_fails_when_edge_counting_duration_is_less_than_zero(self)`

Unit test of
        nipcbatt.pcbatt_library.nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_data_types.DigitalEdgeCountMeasurementTimingParameters.
        

#### `def test_digital_edge_count_measurement_timing_parameter(self)`

Tests if the instance of `DigitalEdgeCountMeasurementTimingParameters`
        is created as expected

#### `def test__digital_edge_count_hardware_timer_configuration(self)`

Tests if the instance of `DigitalEdgeCountHardwareTimerConfiguration`
        is created as expected

#### `def test__digital_edge_count_software_timer_configuration(self)`

Tests if the instance of `DigitalEdgeCountSoftwareTimerConfiguration`
        is created as expected

#### `def test_digital_edge_count_hardware_timer_configuration_with_invalid_parameters(self)`

Tests if the instance creation with invalid parameters throws exception as expected

#### `def test_digital_edge_count_software_timer_configuration_with_invalid_parameters(self)`

Tests if the instance creation with invalid parameters throws exception as expected

#### `def test_digital_edge_count_measurement_result_data_init_fails_when_edge_count_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_data_types.DigitalEdgeCountMeasurementResultData.
        

#### `def test_digital_edge_count_measurement_result_data_init_fails_when_edge_count_is_less_than_zero(self)`

Unit test of
        nipcbatt.pcbatt_library.nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_data_types.DigitalEdgeCountMeasurementResultData.
        

#### `def test_digital_edge_count_measurement_result_data_init_fails_when_edge_type_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_data_types.DigitalEdgeCountMeasurementResultData.
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_edge_count_measurements/test_digital_edge_count_measurement.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/digital_edge_count_measurements/test_digital_edge_count_measurement.py

### MODULE DOCSTRING

This module provides DigitalEdgeCountMeasurementUsingSoftwareTimer
   and DigitalEdgeCountMeasurementUsingHardwareTimer check.

### `class TestDigitalEdgeCountMeasurement(unittest.TestCase)`

Defines a test fixture that ensures the class'DigitalEdgeCountMeasurementUsingHardwareTimer'  or
    'DigitalEdgeCountMeasurementUsingHardwareTimer' is correct and ready to use,

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_digital_edge_count_measurement_using_hardware_timer(self)`

Checks if class 'DigitalEdgeCountMeasurementUsingHardwareTimer' is ready for use

#### `def test_digital_edge_count_measurement_using_software_timer(self)`

Checks if class 'DigitalEdgeCountMeasurementUsingSoftwareTimer' is ready for use

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_frequency_measurements/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/digital_frequency_measurements/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for nipcbatt.pcbatt_library.digital_frequency_measurements package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_frequency_measurements/test_digital_frequency_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/digital_frequency_measurements/test_digital_frequency_data_types.py

### MODULE DOCSTRING

This module provides digital frequency data types check.

### `class TestDigitalFrequencyRangeParameters(unittest.TestCase)`

Defines a test fixture that checks
    `DigitalFrequencyRangeParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_digital_frequency_range_parameters(self)`

Tests if an instance of `DigitalFrequencyRangeParameters`
        is created with the specific values.
        

#### `def test_digital_frequency_range_parameters_with_invalid_data(self)`

Tests if an instance of `DigitalFrequencyRangeParameters`
        is created with the invalid values.
        

#### `def test_digital_frequency_measurement_configuration(self)`

Tests if an instance of DigitalFrequencyMeasurementConfiguration
        is created successfully when given correct input
        

#### `def test_digital_frequency_measurement_configuration_with_invalid_data(self)`

Tests if an instance of DigitalFrequencyMeasurementConfiguration
        throws errors during instantiation when given incorrect input
        

#### `def test_digital_frequency_measurement_counter_channel_parameters(self)`

Tests if an instance of DigitalFrequencyMeasurementCounterChannelParameters
        is created successfully when given correct input
        

#### `def test_digital_frequency_measurement_counter_channel_parameters_with_invalid_data(self)`

Tests if an instance of DigitalFrequencyMeasurementCounterChannelParameters
        throws errors when given incorrect input
        

#### `def test_digital_frequency_measurement_result_data(self)`

Tests if an instance of DigitalFrequencyMeasurementResultData
        is generated correctly when given correct data
        

#### `def test_digital_frequency_measurement_result_data_with_invalid_data(self)`

Tests if an instance of DigitalFrequencyMeasurementResultData
        throws an error when given incorrect data
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_frequency_measurements/test_digital_frequency_measurement.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/digital_frequency_measurements/test_digital_frequency_measurement.py

### MODULE DOCSTRING

This module provides DigitalFrequencyMeasurement check.

### `class TestDigitalFrequencyMeasurement(unittest.TestCase)`

Defines a test fixture that ensures the class
       'DigitalFrequencyMeasurement' is correct
       and ready to use

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_digital_frequency_measurement(self)`

Checks if class 'DigitalFrequencyMeasurement' is ready to use

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_pulse_generations/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/digital_pulse_generations/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for nipcbatt.pcbatt_library.digital_pulse_generations package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_pulse_generations/test_digital_pulse_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/digital_pulse_generations/test_digital_pulse_data_types.py

### MODULE DOCSTRING

This module provides Digital pulse data types check.

### `class TestDigitalPulseGenerationDataTypes(unittest.TestCase)`

Defines a test fixture to test the data types used in
       digital pulse generation

    Args:
        unittest.TestCase: Base class from which this class inherits
    

#### `def test_digital_pulse_counter_channel_parameters(self)`

Tests if an instance of 'DigitalPulseGenerationCounterChannelParameters
        is created when given correct values

#### `def test_digital_pulse_generation_counter_channel_parameters_invalid(self)`

Ensures an instance of DigitalPulseGenerationCounterChannel parameters
        is not generated when given invalid values

#### `def test_digital_pulse_generation_timing_parameters(self)`

Tests if an instance of DigitalPulseGenerationTimingParameters
        is created successfully when given valid parameters

#### `def test_digital_pulse_generation_timing_parameters_invalid(self)`

Ensures an instance of DigitalPulseGenerationTimingParameters
        is not created when given invalid parameters

#### `def test_digital_pulse_generation_configuration(self)`

Ensures an instance of DigitalPulseGenerationConfiguration is
        created when given correct parameters

#### `def test_digital_pulse_generation_configuration_invalid_params(self)`

Ensures that the creation of an instance of
        DigitalPusleGenerationConfiguration fails when given
        invalid data

#### `def test_digital_pulse_generation_data(self)`

Tests if an instance of DigitalPulseGenerationData is correctly
        created when given correct input

#### `def test_digital_pulse_generation_data_invalid(self)`

Ensures an instance of DigitalPulseGenerationData is not created
        when given invalid parameters

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_pulse_generations/test_digital_pulse_generation.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/digital_pulse_generations/test_digital_pulse_generation.py

### MODULE DOCSTRING

This module provides DigitalPulseGeneration check.

- `CHANNEL = 'Sim_PXIeDAQ/ctr0'`

- `TERMINAL = '/Sim_PXIeDAQ/PFI0'`

### `class TestDigitalPulseGeneration(unittest.TestCase)`

Defines a test fixture that ensures the class 'DigitalPulseGeneration' is
       correct and readhy to use

    Args:
        unittest.TestCase: Base class from which this class inherits
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_digital_pulse_generation(self)`

Checks if class DigitalPulseGneration is ready to use

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_pwm_measurements/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/digital_pwm_measurements/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for nipcbatt.pcbatt_library.digital_pwm_measurements package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_pwm_measurements/test_digital_pwm_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/digital_pwm_measurements/test_digital_pwm_data_types.py

### MODULE DOCSTRING

This module provides digital PWM data types check.

### `class TestDigitalPwmMeasurementDataTypes(unittest.TestCase)`

Defines a test fixture to unsure the data types class used for digital PWM
       measurement are ready to use.

    Args:
        unittest.testCase: Parent class of the unittest framework

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_dpwmm_range_parameters(self)`

Tests if an instance of DigitalPwmMeasurementRangeParameters is
        created when given correct values

#### `def test_dpwmm_range_parameters_invalid_input(self)`

Ensures an instance of DigitalPwmMeasurementRangeParameters is
        not created when given invalid values

#### `def test_dpwmm_timing_parameters(self)`

Tests if an instance of DigitalPwmMeasurementTimingParameters is
        created when given correct values

#### `def test_dpwmm_timing_parameters_invalid_input(self)`

Ensures an instance of DigitalPwmMeasurementTimingParameters is
        not created when given invalid values

#### `def test_dpwmm_counter_channel_parameters(self)`

Tests if an instance of DigitalPwmMeasurementCounterChannelParameters is
        created when given correct values

#### `def test_dpwmm_counter_channel_parameters_invalid_data(self)`

Ensures an instance of DigitalPwmMeasurementCounterChannelParameters is
        not created when given invalid values

#### `def test_dpwmm_data(self)`

Tests if an instance of DigitalPwmMeasurementData is
        created when given correct values

#### `def test_dpwmm_data_invalid_input(self)`

Ensures an instance of DigitalPwmMeasurementCounterChannelParameters is
        not created when given invalid values

#### `def test_dpwmm_result_data(self)`

Tests if an instance of DigitalPwmMeasurementResultData is
        created when given correct values

#### `def test_dpwmm_result_data_invalid_input(self)`

Tests if an instance of DigitalPwmMeasurementResultData is
        created when given correct values

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/digital_pwm_measurements/test_digital_pwm_measurement.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/digital_pwm_measurements/test_digital_pwm_measurement.py

### MODULE DOCSTRING

This module provides DigitalPwmMeasurement check.

### `class TestDigitalPwmMeasurement(unittest.TestCase)`

Defines a test fixutre that ensure the class 'DigitalPwmMeasurement'
       is correct and ready to use

    Args:
        unittest.TestCase: Base class of the Python unittest framework
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_digital_pwm_measurement(self)`

Checks if class 'DigitalPwmMeasurement' is ready to use

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dmm_scan/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/dmm_scan/__init__.py

### MODULE DOCSTRING

Provides unit tests for DMM Scan functionality.

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dmm_scan/test_dmm_scan_pmps_16V_15C.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/dmm_scan/test_dmm_scan_pmps_16V_15C.py

### MODULE DOCSTRING

This module provides comprehensive unit tests for DmmScanPMPS class and data types.

### `class TestScanResources(unittest.TestCase)`

Defines a test fixture that checks `ScanResources` NamedTuple is correctly structured.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

Set up test fixtures.

#### `def tearDown(self)`

Tear down test fixtures.

#### `def setUpClass(cls)`

Set up class-level fixtures.

#### `def tearDownClass(cls)`

Tear down class-level fixtures.

#### `def test_scan_resources_is_named_tuple(self)`

Unit test verifying that ScanResources is a NamedTuple.

#### `def test_scan_resources_has_required_fields(self)`

Unit test verifying that ScanResources has all required fields.

#### `def test_scan_resources_field_access(self)`

Unit test verifying that ScanResources fields can be accessed correctly.

### `class TestMeasurementResult(unittest.TestCase)`

Defines a test fixture that checks `MeasurementResult` NamedTuple is correctly structured.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

Set up test fixtures.

#### `def tearDown(self)`

Tear down test fixtures.

#### `def setUpClass(cls)`

Set up class-level fixtures.

#### `def tearDownClass(cls)`

Tear down class-level fixtures.

#### `def test_measurement_result_is_named_tuple(self)`

Unit test verifying that MeasurementResult is a NamedTuple.

#### `def test_measurement_result_has_required_fields(self)`

Unit test verifying that MeasurementResult has all required fields.

#### `def test_measurement_result_field_access(self)`

Unit test verifying that MeasurementResult fields can be accessed correctly.

#### `def test_measurement_result_with_sample_data(self)`

Unit test verifying MeasurementResult with realistic sample data.

### `class TestDmmScanPMPSInitialization(unittest.TestCase)`

Defines a test fixture that checks DmmScanPMPS initialization.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

Set up test fixtures.

#### `def tearDown(self)`

Tear down test fixtures.

#### `def setUpClass(cls)`

Set up class-level fixtures.

#### `def tearDownClass(cls)`

Tear down class-level fixtures.

#### `def test_dmm_scan_pmps_can_be_instantiated(self)`

Unit test verifying that DmmScanPMPS can be instantiated.

#### `def test_dmm_scan_pmps_is_instance_of_building_blocks(self)`

Unit test verifying that DmmScanPMPS inherits from building block classes.

#### `def test_dmm_scan_pmps_has_initialize_method(self)`

Unit test verifying that DmmScanPMPS has initialize method.

#### `def test_dmm_scan_pmps_has_configure_and_measure_method(self)`

Unit test verifying that DmmScanPMPS has configure_and_measure method.

#### `def test_dmm_scan_pmps_has_close_method(self)`

Unit test verifying that DmmScanPMPS has close method.

### `class TestDmmScanPMPSInitializeMethod(unittest.TestCase)`

Defines a test fixture for testing DmmScanPMPS.initialize() method.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

Set up test fixtures.

#### `def tearDown(self)`

Tear down test fixtures.

#### `def setUpClass(cls)`

Set up class-level fixtures.

#### `def tearDownClass(cls)`

Tear down class-level fixtures.

#### `def test_initialize_returns_scan_resources(self, mock_dmm, mock_switch)`

Unit test verifying that initialize() returns ScanResources.

#### `def test_initialize_with_default_parameters(self, mock_dmm, mock_switch)`

Unit test verifying initialize() works with default parameters.

#### `def test_initialize_with_close_all_shunts_false(self, mock_dmm, mock_switch)`

Unit test verifying initialize() with close_all_shunts=False.

### `class TestDmmScanPMPSCloseMethod(unittest.TestCase)`

Defines a test fixture for testing DmmScanPMPS.close() method.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

Set up test fixtures.

#### `def tearDown(self)`

Tear down test fixtures.

#### `def setUpClass(cls)`

Set up class-level fixtures.

#### `def tearDownClass(cls)`

Tear down class-level fixtures.

#### `def test_close_method_calls_close_on_all_resources(self)`

Unit test verifying close() calls close on all resource handles.

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_generations/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_generations/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for 
   nipcbatt.pcbatt_library.dynamic_digital_pattern_generations package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_generations/test_dynamic_digital_pattern_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_generations/test_dynamic_digital_pattern_data_types.py

### MODULE DOCSTRING

This module provides Dynamic digital pattern data types check.

- `CHANNEL = 'NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/port0/line0'`

- `CLOCK_SOURCE = '/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0'`

- `TRIGGER_SOURCE = '/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0'`

### `class TestDynamicDigitalPatternGenerationDataTypes(unittest.TestCase)`

Defines a test fixture to test the datatypes used in dynamic digital
       pulse generation

    Args:
        unittest: The unittest class from which all tests inherit
    

#### `def test_dynamic_digital_start_trigger_parameters(self)`

Ensures a valid instance of DynamicDigitalStartTriggerParameters
        is created when given valid parameters

#### `def test_dynamic_digital_start_trigger_parameters_invalid(self)`

Ensures an instance of DynamicDigitalStartTriggerParameters is not
        created when given invalid parameters

#### `def test_dynamic_digital_pattern_generation_data(self)`

Ensures that a valid instance of DynamicDigitalPatternGenerationData
        is created when given valid parameters

#### `def test_dynamic_digital_pattern_generation_data_invalid(self)`

Ensures that an instance of DynamicDigitalPatternGenerationData is
        not created when given invalid parameters

#### `def test_dynamic_digital_pattern_generation_configuration(self)`

Ensures an instance of DynamicDigitalPatternGenerationConfiguration
        is created when given valid parameters

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_generations/test_dynamic_digital_pattern_generation.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_generations/test_dynamic_digital_pattern_generation.py

### MODULE DOCSTRING

This module provides DynamicDigitalPatternGeneration check.

- `CHANNEL = 'Sim_PXIeDAQ/port0/line0:7'`

- `CLOCK_SOURCE = 'OnboardClock'`

- `TRIGGER_SOURCE = '/Sim_PXIeDAQ/PFI0'`

### `class TestDynamicDigitalPatternGeneration(unittest.TestCase)`

Defines a test fixture that ensures the class 'DynamicDigitalPatternGeneration' is
       correct and ready to use

    Args:
        unittest.TestCase: Base class from which this class inherits
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_dynamic_digital_pattern_generation(self)`

Checks if class DynamicDigitalPatternGeneration is ready to use

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_measurements/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_measurements/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for 
   nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_measurements/test_dynamic_digital_pattern_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_measurements/test_dynamic_digital_pattern_data_types.py

### MODULE DOCSTRING

This module provides Dynamic digital pattern data types check.

### `class TestDynamicDigitalPatternMeasurementDataTypes(unittest.TestCase)`

Defines a test fixture that checks
    `DynamicDigitalPatternMeasurementDataTypes` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_dynamic_digital_pattern_measurement_configuration(self)`

Tests if the instance of `DynamicDigitalPatternMeasurementConfiguration`
        is created as expected

#### `def test_dynamic_digital_pattern_measurement_configuration_with_invalid_parameters(self)`

Tests if the instance creation with invalid parameters throws exception as expected

#### `def test_dynamic_digital_pattern_measurement_result_data_init_fails_when_waveforms_is_none(self)`

unit test of DynamicDigitalPatternMeasurementResultData.

#### `def test_dynamic_digital_pattern_measurement_result_data_init_fails_when_waveforms_is_empty(self)`

unit test of DynamicDigitalPatternMeasurementResultData.

#### `def test_dynamic_digital_pattern_measurement_result_data_init_fails_when_daq_digital_waveform_from_port_is_none(self)`

unit test of DynamicDigitalPatternMeasurementResultData.

#### `def test_dynamic_digital_pattern_measurement_result_data_init_fails_when_daq_digital_waveform_from_port_is_empty(self)`

unit test of DynamicDigitalPatternMeasurementResultData.

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_measurements/test_dynamic_digital_pattern_measurement.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/dynamic_digital_pattern_measurements/test_dynamic_digital_pattern_measurement.py

### MODULE DOCSTRING

This module provides DynamicDigitalPatternMeasurement check.

### `class TestDynamicDigitalPatternMeasurement(unittest.TestCase)`

Defines a test fixture that ensures the class'DynamicDigitalPatternMeasurement' is correct
       and ready to use

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_dynamic_digital_pattern_measurement(self)`

Checks if class 'DynamicDigitalPatternMeasurement' is ready for use

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/frequency_domain_measurements/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/frequency_domain_measurements/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for 
   nipcbatt.pcbatt_library.frequency_domain_measurements package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/frequency_domain_measurements/test_frequency_domain_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/frequency_domain_measurements/test_frequency_domain_data_types.py

### MODULE DOCSTRING

This module provides Frequency domain data types check.

### `class TestFrequencyDomainMeasurementConfiguration(unittest.TestCase)`

Defines a test fixture that checks
    `TimeDomainMeasurementConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_frequency_domain_measurement_configuration_init_fails_when_global_channel_parameters_is_none(self)`

unit test of FrequencyDomainMeasurementConfiguration.

#### `def test_frequency_domain_measurement_configuration_init_fails_when_specific_channels_parameters_is_none(self)`

unit test of FrequencyDomainMeasurementConfiguration.

#### `def test_frequency_domain_measurement_configuration_init_fails_when_measurement_options_is_none(self)`

unit test of FrequencyDomainMeasurementConfiguration.

#### `def test_frequency_domain_measurement_configuration_init_fails_when_sample_clock_timing_parameters_is_none(self)`

unit test of FrequencyDomainMeasurementConfiguration.

#### `def test_frequency_domain_measurement_configuration_init_fails_when_digital_start_trigger_parameters_is_none(self)`

unit test of FrequencyDomainMeasurementConfiguration.

#### `def test_frequency_domain_measurement_configuration(self)`

unit test of FrequencyDomainMeasurementConfiguration.

### `class TestMultipleTonesMeasurementResultData(unittest.TestCase)`

Defines a test fixture that checks
    `MultipleTonesMeasurementResultData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def __init__(self, methodName: str='runTest') -> None`

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_multiple_tones_measurement_result_data_for_value_error(self)`

Tests if expected ValueError in thrown when inputs are None

#### `def test_multiple_tones_measurement_result_data_for_type_error(self)`

Tests if expected TypeError in thrown when inputs are None

#### `def test_multiple_tones_measurement_result_data_with_input_lists_of_different_lengths(self)`

Tests if expected ValueError in thrown when the two input lists have different length.

#### `def test_multiple_tones_measurement_result_data(self)`

Test for proper functioning of TestMultipleTonesMeasurementResultData

### `class TestFrequencyDomainMeasurementResultData(unittest.TestCase)`

Defines a test fixture that checks
    `FrequencyDomainMeasurementResultData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def __init__(self, methodName: str='runTest') -> None`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def setUp(self)`

Creates some common test data to be used in different test methods.

#### `def tearDown(self)`

#### `def test_frequency_domain_measurement_result_data_for_invalid_values_for_waveforms(self)`

Unit test to check if `FrequencyDomainMeasurementResultData` throws Value Error
        for invalid values for `waveforms` input.

#### `def test_frequency_domain_measurement_result_data_for_invalid_values_for_detected_tones(self)`

Tests if expected error is thrown when creating instance of
        `FrequencyDomainMeasurementResultData' with invalid values for `detected_tones`.
        

#### `def test_frequency_domain_measurement_result_data_for_invalid_values_for_magnitude_rms(self)`

Tests if expected error is thrown when creating instance of
        `FrequencyDomainMeasurementResultData' with invalid values for `magnitude_rms`.
        

#### `def test_frequency_domain_measurement_result_data_for_invalid_values_for_magnitude_peak(self)`

Tests if expected error is thrown when creating instance of
        `FrequencyDomainMeasurementResultData' with invalid values for `magnitude_peak`.
        

#### `def test_frequency_domain_measurement_result_data_with_waveforms_and_magnitude_rms_are_of_different_lengths(self)`

Tests if expected error is thrown when creating instance of
        `FrequencyDomainMeasurementResultData'
        with diffrent list size for`waveforms` and `magnitude_rms`
        

#### `def test_frequency_domain_measurement_result_data_with_waveforms_and_magnitude_peak_are_of_different_lengths(self)`

Tests if expected error is thrown when creating instance
        of `FrequencyDomainMeasurementResultData'
        with diffrent list size for`waveforms` and `magnitude_peak`
        

#### `def test_frequency_domain_measurement_result_data_with_waveforms_and_detected_tones_are_of_different_lengths(self)`

Tests if expected error is thrown when creating instance of
        `FrequencyDomainMeasurementResultData'
        with diffrent list size for`waveforms` and `detected_tones`
        

#### `def test_frequency_domain_measurement_result_data(self)`

Test for proper functioning of `FrequencyDomainMeasurementResultData` class

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/frequency_domain_measurements/test_frequency_domain_measurement.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/frequency_domain_measurements/test_frequency_domain_measurement.py

### MODULE DOCSTRING

This module provides FrequencyDomainMeasurement check.

### `class TestFrequencyDomainMeasurement(unittest.TestCase)`

Defines a test fixture that checks
    `FrequencyDomainMeasurement` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_frequency_domain_measurement(self)`

Checks if class FrequencyDomainMeasurement is ready to use

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for 
   nipcbatt.pcbatt_library.i2c_communications package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/test_i2c_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/test_i2c_data_types.py

### MODULE DOCSTRING

This module provides I2C data types check.

### `class TestI2cDeviceParameters(unittest.TestCase)`

Defines a test fixture that checks
    `I2cDeviceParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_i2c_device_parameters(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_data_types.I2cDeviceParameters.
        

### `class TestI2cCommunicationParameters(unittest.TestCase)`

Defines a test fixture that checks
    `I2cCommunicationParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_i2c_communication_parameters_init_fails_when_device_address_is_less_than_zero(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_data_types.I2cCommunicationParameters.
        

#### `def test_i2c_communication_parameters_init_fails_when_ack_poll_timeout_milliseconds_is_less_than_zero(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_data_types.I2cCommunicationParameters.
        

#### `def test_i2c_communication_parameters_init_fails_when_clock_rate_kilohertz_is_equal_to_zero(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_data_types.I2cCommunicationParameters.
        

#### `def test_i2c_communication_parameters_init_fails_when_clock_rate_kilohertz_is_less_than_zero(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_data_types.I2cCommunicationParameters.
        

#### `def test_i2c_communication_parameters(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_data_types.I2cCommunicationParameters.
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/test_i2c_read_communication.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/test_i2c_read_communication.py

### MODULE DOCSTRING

This module provides I2CReadCommunication check.

### `class TestI2cReadCommunication(unittest.TestCase)`

Defines a test fixture that checks the `I2cReadCommunication` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_i2c_read_communication(self)`

Unit test of
        communications.pcbatt_library.i2c_communications.i2c_read_communication.I2cReadCommunication
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/test_i2c_read_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/test_i2c_read_data_types.py

### MODULE DOCSTRING

This module provides I2C read communication data types check.

### `class TestI2cReadParameters(unittest.TestCase)`

Defines a test fixture that checks
    `I2cReadParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_i2c_read_parameters_init_fails_when_memory_address_parameters_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types.I2cReadParameters.
        

#### `def test_i2c_read_parameters_init_fails_when_number_of_bytes_to_read_is_equal_to_zero(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types.I2cReadParameters.
        

#### `def test_i2c_read_parameters_init_fails_when_number_of_bytes_to_read_is_less_than_zero(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types.I2cReadParameters.
        

#### `def test_i2c_read_parameters(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types.I2cReadParameters.
        

### `class TestI2cReadCommunicationConfiguration(unittest.TestCase)`

Defines a test fixture that checks
    `I2cReadCommunicationConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_i2c_read_communication_configuration_init_fails_when_device_parameters_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types.I2cReadCommunicationConfiguration.
        

#### `def test_i2c_read_communication_configuration_init_fails_when_communication_parameters_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types.I2cReadCommunicationConfiguration.
        

#### `def test_i2c_read_communication_configuration_init_fails_when_read_parameters_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types.I2cReadCommunicationConfiguration.
        

#### `def test_i2c_read_communication_configuration(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types.I2cReadCommunicationConfiguration.
        

### `class TestI2cReadCommunicationData(unittest.TestCase)`

Defines a test fixture that checks
    `TestI2cReadCommunicationData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_i2c_read_communication_data_init_fails_when_data_bytes_read_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types.I2cReadCommunicationData.
        

#### `def test_i2c_read_communication_data_init_fails_when_data_bytes_read_is_empty(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types.I2cReadCommunicationData.
        

#### `def test_i2c_read_communication_data(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types.I2cReadCommunicationData.
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/test_i2c_write_communication.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/test_i2c_write_communication.py

### MODULE DOCSTRING

This module provides I2CWriteCommunication check.

### `class TestI2cWriteCommunication(unittest.TestCase)`

Defines a test fixture that checks the `I2cWriteCommunication` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_i2c_write_communication(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_communication.I2cWriteCommunication
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/test_i2c_write_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/i2c_communications/test_i2c_write_data_types.py

### MODULE DOCSTRING

This module provides I2C write communication data types check.

### `class TestI2cWriteParameters(unittest.TestCase)`

Defines a test fixture that checks
    `I2cWriteParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_i2c_write_parameters_init_fails_when_memory_address_parameters_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteParameters.
        

#### `def test_i2c_write_parameters_init_fails_when_data_to_be_written_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteParameters.
        

#### `def test_i2c_write_parameters_init_fails_when_data_to_be_written_is_empty(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteParameters.
        

#### `def test_i2c_write_parameters_init_fails_when_number_of_bytes_per_page_is_less_than_zero(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteParameters.
        

#### `def test_i2c_write_parameters_init_fails_when_number_of_bytes_per_page_is_equal_to_zero(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteParameters.
        

#### `def test_i2c_write_parameters_init_fails_when_delay_between_page_write_operations_milliseconds_is_less_than_zero(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteParameters.
        

#### `def test_i2c_write_parameters(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteParameters.
        

### `class TestI2cWriteCommunicationConfiguration(unittest.TestCase)`

Defines a test fixture that checks
    `I2cWriteCommunicationConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_i2c_write_communication_configuration_init_fails_when_device_parameters_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteCommunicationConfiguration.
        

#### `def test_i2c_write_communication_configuration_init_fails_when_communication_parameters_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteCommunicationConfiguration.
        

#### `def test_i2c_write_communication_configuration_init_fails_when_write_parameters_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteCommunicationConfiguration.
        

#### `def test_i2c_write_communication_configuration(self)`

Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteCommunicationConfiguration.
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/mixed_measurements/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/mixed_measurements/__init__.py

### MODULE DOCSTRING

Provides Unit tests for mixed measurements in the pcbatt_library.

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/mixed_measurements/test_mixed_measurement.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/mixed_measurements/test_mixed_measurement.py

### MODULE DOCSTRING

This module provides MixedMeasurement check.

### `class TestMixedMeasurement(unittest.TestCase)`

Defines a test fixture that checks
    `MixedMeasurement` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_mixed_measurement(self)`

Checks if class MixedMeasurement is ready to use

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/nidcpower/dc_cc_source_and_measure/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/nidcpower/dc_cc_source_and_measure/__init__.py

### MODULE DOCSTRING

Provides Unit tests for dc cc source and measurements in the pcbatt_library.

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/nidcpower/dc_cc_source_and_measure/test_dc_cc_source_and_measure.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/nidcpower/dc_cc_source_and_measure/test_dc_cc_source_and_measure.py

### MODULE DOCSTRING

This module provides DC constant current source and measure data types unit tests.

### `class TestMeasurementExecutionType(unittest.TestCase)`

Defines a test fixture that checks
    `MeasurementExecutionType` enum is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_measurement_execution_type_members(self)`

Checks MeasurementExecutionType enum has expected members and values.

### `class TestSourceTriggerBehavior(unittest.TestCase)`

Defines a test fixture that checks
    `SourceTriggerBehavior` enum is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_source_trigger_behavior_members(self)`

Checks SourceTriggerBehavior enum has expected members and values.

### `class TestExportEvent(unittest.TestCase)`

Defines a test fixture that checks
    `ExportEvent` enum is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_export_event_members(self)`

Checks ExportEvent enum has expected members and values.

### `class TestEventSignalToExport(unittest.TestCase)`

Defines a test fixture that checks
    `EventSignalToExport` enum is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_event_signal_to_export_members(self)`

Checks EventSignalToExport enum has expected members and values.

### `class TestExecutionSettings(unittest.TestCase)`

Defines a test fixture that checks
    `ExecutionSettings` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_execution_settings(self)`

Checks ExecutionSettings construction and property getters.

#### `def test_execution_settings_configure_only(self)`

Checks ExecutionSettings with CONFIGURE_ONLY execution type.

### `class TestCurrentChannelSettings(unittest.TestCase)`

Defines a test fixture that checks
    `CurrentChannelSettings` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_current_channel_settings_remote_sensing(self)`

Checks CurrentChannelSettings construction and property getters with REMOTE sensing.

#### `def test_current_channel_settings_local_sensing_output_disabled(self)`

Checks CurrentChannelSettings with LOCAL sensing and output disabled.

### `class TestTimingParameters(unittest.TestCase)`

Defines a test fixture that checks
    `TimingParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_timing_parameters(self)`

Checks TimingParameters construction and property getters.

#### `def test_timing_parameters_fast_transient(self)`

Checks TimingParameters with FAST transient response.

### `class TestTriggerParameters(unittest.TestCase)`

Defines a test fixture that checks
    `TriggerParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_trigger_parameters_with_trigger_enabled(self)`

Checks TriggerParameters with source trigger enabled and event routing.

#### `def test_trigger_parameters_with_trigger_disabled(self)`

Checks TriggerParameters with source trigger disabled and no event routing.

### `class TestDCCurrentSourceAndMeasureParameters(unittest.TestCase)`

Defines a test fixture that checks
    `DCCurrentSourceAndMeasureParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_dc_current_source_and_measure_parameters(self)`

Checks DCCurrentSourceAndMeasureParameters construction and property getters.

### `class TestDCCurrentSourceAndMeasureResultData(unittest.TestCase)`

Defines a test fixture that checks
    `DCCurrentSourceAndMeasureResultData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_dc_current_source_and_measure_result_data(self)`

Checks DCCurrentSourceAndMeasureResultData construction and property getters.

#### `def test_dc_current_source_and_measure_result_data_with_nan_values(self)`

Checks DCCurrentSourceAndMeasureResultData with NaN values when no measurement is performed.

#### `def test_dc_current_source_and_measure_result_data_compliance_reached(self)`

Checks DCCurrentSourceAndMeasureResultData when compliance limit is reached.

### `class TestConstantsForDCCurrentSourceAndMeasure(unittest.TestCase)`

Defines a test fixture that checks
    `ConstantsForDCCurrentSourceAndMeasure` and default instances are ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_default_execution_settings(self)`

Checks DEFAULT_DC_CC_EXECUTION_SETTINGS has expected default values.

#### `def test_default_channel_settings(self)`

Checks DEFAULT_DC_CC_CHANNEL_SETTINGS has expected default values.

#### `def test_default_timing_parameters(self)`

Checks DEFAULT_DC_CC_TIMING_PARAMETERS has expected default values.

#### `def test_default_trigger_parameters(self)`

Checks DEFAULT_DC_CC_TRIGGER_PARAMETERS has expected default values.

#### `def test_default_source_and_measure_parameters(self)`

Checks DEFAULT_DC_CC_SOURCE_AND_MEASURE_PARAMETERS has expected default sub-objects.

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/nidcpower/dc_cv_source_and_measure/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/nidcpower/dc_cv_source_and_measure/__init__.py

### MODULE DOCSTRING

Provides Unit tests for dc cv source and Smeasurements in the pcbatt_library.

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/nidcpower/dc_cv_source_and_measure/test_dc_cv_source_and_measure.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/nidcpower/dc_cv_source_and_measure/test_dc_cv_source_and_measure.py

### MODULE DOCSTRING

This module provides DC constant voltage source and measure data types unit tests.

### `class TestMeasurementExecutionType(unittest.TestCase)`

Defines a test fixture that checks
    `MeasurementExecutionType` enum is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_measurement_execution_type_members(self)`

Checks MeasurementExecutionType enum has expected members and values.

### `class TestSourceTriggerBehavior(unittest.TestCase)`

Defines a test fixture that checks
    `SourceTriggerBehavior` enum is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_source_trigger_behavior_members(self)`

Checks SourceTriggerBehavior enum has expected members and values.

### `class TestExportEvent(unittest.TestCase)`

Defines a test fixture that checks
    `ExportEvent` enum is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_export_event_members(self)`

Checks ExportEvent enum has expected members and values.

### `class TestEventSignalToExport(unittest.TestCase)`

Defines a test fixture that checks
    `EventSignalToExport` enum is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_event_signal_to_export_members(self)`

Checks EventSignalToExport enum has expected members and values.

### `class TestExecutionSettings(unittest.TestCase)`

Defines a test fixture that checks
    `ExecutionSettings` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_execution_settings(self)`

Checks ExecutionSettings construction and property getters.

#### `def test_execution_settings_configure_only(self)`

Checks ExecutionSettings with CONFIGURE_ONLY execution type.

### `class TestVoltageChannelSettings(unittest.TestCase)`

Defines a test fixture that checks
    `VoltageChannelSettings` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_voltage_channel_settings(self)`

Checks VoltageChannelSettings construction and property getters.

#### `def test_voltage_channel_settings_local_sensing(self)`

Checks VoltageChannelSettings with LOCAL sensing and output disabled.

### `class TestTimingParameters(unittest.TestCase)`

Defines a test fixture that checks
    `TimingParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_timing_parameters(self)`

Checks TimingParameters construction and property getters.

#### `def test_timing_parameters_fast_transient(self)`

Checks TimingParameters with FAST transient response.

### `class TestTriggerParameters(unittest.TestCase)`

Defines a test fixture that checks
    `TriggerParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_trigger_parameters_with_trigger_enabled(self)`

Checks TriggerParameters with source trigger enabled and event routing.

#### `def test_trigger_parameters_with_trigger_disabled(self)`

Checks TriggerParameters with source trigger disabled and no event routing.

### `class TestDCVoltageSourceAndMeasureParameters(unittest.TestCase)`

Defines a test fixture that checks
    `DCVoltageSourceAndMeasureParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_dc_voltage_source_and_measure_parameters(self)`

Checks DCVoltageSourceAndMeasureParameters construction and property getters.

### `class TestDCVoltageSourceAndMeasureResultData(unittest.TestCase)`

Defines a test fixture that checks
    `DCVoltageSourceAndMeasureResultData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_dc_voltage_source_and_measure_result_data(self)`

Checks DCVoltageSourceAndMeasureResultData construction and property getters.

#### `def test_dc_voltage_source_and_measure_result_data_with_nan_values(self)`

Checks DCVoltageSourceAndMeasureResultData with NaN values when no measurement is performed.

### `class TestConstantsForDCVoltageSourceAndMeasure(unittest.TestCase)`

Defines a test fixture that checks
    `ConstantsForDCVoltageSourceAndMeasure` and default instances are ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_default_execution_settings(self)`

Checks DEFAULT_DC_CV_EXECUTION_SETTINGS has expected default values.

#### `def test_default_channel_settings(self)`

Checks DEFAULT_DC_CV_CHANNEL_SETTINGS has expected default values.

#### `def test_default_timing_parameters(self)`

Checks DEFAULT_DC_CV_TIMING_PARAMETERS has expected default values.

#### `def test_default_trigger_parameters(self)`

Checks DEFAULT_DC_CV_TRIGGER_PARAMETERS has expected default values.

#### `def test_default_source_and_measure_parameters(self)`

Checks DEFAULT_DC_CV_SOURCE_AND_MEASURE_PARAMETERS has expected default sub-objects.

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/power_supply_source_and_measurements/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/power_supply_source_and_measurements/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for 
   nipcbatt.pcbatt_library.power_supply_source_and_measurements package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/power_supply_source_and_measurements/test_power_supply_source_and_measure.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/power_supply_source_and_measurements/test_power_supply_source_and_measure.py

### MODULE DOCSTRING

This module provides PowerSupplySourceAndMeasure check.

### `class TestPowerSupplySourceAndMeasure(unittest.TestCase)`

Defines a test fixture that checks
    `PowerSupplySourceAndMeasure` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_power_supply_source_and_measure(self)`

Checks if class PowerSupplySourceAndMeasure is ready to use

#### `def test_analyze_measurement_data_results_when_providing_valid_data(self)`

unit test of PowerSupplySourceAndMeasureData.

#### `def test_analyze_measurement_data_results_when_providing_undefined_data(self)`

unit test of PowerSupplySourceAndMeasureData.

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/power_supply_source_and_measurements/test_power_supply_source_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/power_supply_source_and_measurements/test_power_supply_source_data_types.py

### MODULE DOCSTRING

This module provides Power supply source data types check.

### `class TestPowerSupplySourceAndMeasureTerminalParameters(unittest.TestCase)`

Defines a test fixture that checks
    `PowerSupplySourceAndMeasureTerminalParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_power_supply_source_and_measure_terminal_parameters(self)`

unit test of PowerSupplySourceAndMeasureTerminalParameters.

### `class TestPowerSupplySourceAndMeasureConfiguration(unittest.TestCase)`

Defines a test fixture that checks
    `PowerSupplySourceAndMeasureConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_power_supply_source_and_measure_configuration(self)`

unit test of PowerSupplySourceAndMeasureConfiguration.

### `class TestPowerSupplySourceAndMeasureData(unittest.TestCase)`

Defines a test fixture that checks
    `PowerSupplySourceAndMeasureData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_power_supply_source_and_measure_data(self)`

unit test of PowerSupplySourceAndMeasureData.

#### `def test_power_supply_source_and_measure_data_with_invalid_data(self)`

Tests if expected error is thrown when creating an instance of
        `PowerSupplySourceAndMeasureData` with invalid data

### `class TestPowerSupplySourceAndMeasureResultData(unittest.TestCase)`

Defines a test fixture that checks
    `PowerSupplySourceAndMeasureResultData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_power_supply_source_and_measure_result_data(self)`

unit test of PowerSupplySourceAndMeasureResultData.

#### `def test_power_supply_source_and_measure_result_data_with_invalid_waveforms(self)`

Test if the expected error is thrown if the current or voltage waveform is None

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/resistance_measurements/test_dmm_resistance_measurements.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/resistance_measurements/test_dmm_resistance_measurements.py

### MODULE DOCSTRING

 Performs unit tests ensuring the integrity of the datatypes used in 
    DMM-based resistance measurements 

### `class TestDmmResistance(unittest.TestCase)`

Defines a test fixture that ensures the data types of the 
        dmm.Resistance class are created correctly
        
        Args:
            unittest.TestCase: Base class from which this class inherits
        

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_enum_members_shape_and_types(self)`

Tests the creation of different type and shapes of enums

#### `def test_function_params_basic_construction_and_properties(self)`

Create a ResistanceMeasurementFunctionParameters and verify properties.

#### `def test_properties_are_effectively_read_only(self)`

Attempting to assign to properties should raise AttributeError.

#### `def test_basic_construction_and_properties(self)`

Create params and verify properties return the same objects.

#### `def test_construct_for_every_current_range_enum_value(self)`

Iterate all CurrentRangeAndFunctions, instantiate params, and verify.

#### `def test_dcrms_meas_config_properties_are_read_only(self)`

Ensure all function properties are read only

#### `def test_identity_of_references(self)`

Make sure the same object is returned, not a copy

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/serial_communications/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/serial_communications/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for 
   nipcbatt.pcbatt_library.serial_communications package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/serial_communications/test_serial_communication.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/serial_communications/test_serial_communication.py

### MODULE DOCSTRING

This module provides SerialCommunication check.

### `class TestSerialCommunication(unittest.TestCase)`

Defines a test fixture that checks `SerialCommunication` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_serial_communication(self)`

Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_communication.SerialCommunication
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/serial_communications/test_serial_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/serial_communications/test_serial_data_types.py

### MODULE DOCSTRING

This module provides Serial communication data types check.

### `class TestSerialCommunicationParameters(unittest.TestCase)`

Defines a test fixture that checks
    `SerialCommunicationParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_serial_communication_parameters_init_fails_when_data_rate_bauds_is_equal_to_zero(self)`

Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationParameters.
        

#### `def test_serial_communication_parameters_init_fails_when_data_rate_bauds_is_lower_than_zero(self)`

Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationParameters.
        

#### `def test_serial_communication_parameters_init_fails_when_number_of_bits_in_data_frame_is_lower_than_four(self)`

Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationParameters.
        

#### `def test_serial_communication_parameters_init_fails_when_number_of_bits_in_data_frame_is_greater_than_eight(self)`

Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationParameters.
        

#### `def test_serial_communication_parameters_init_fails_when_delay_before_receive_response_milliseconds_is_equal_to_zero(self)`

Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationParameters.
        

#### `def test_serial_communication_parameters_init_fails_when_delay_before_receive_response_milliseconds_is_lower_than_zero(self)`

Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationParameters.
        

#### `def test_serial_communication_parameters(self)`

Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationParameters.
        

### `class TestSerialCommunicationConfiguration(unittest.TestCase)`

Defines a test fixture that checks
    `SerialCommunicationConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_serial_communication_configuration_init_fails_when_communication_parameters_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationConfiguration.
        

#### `def test_serial_communication_configuration_init_fails_when_command_to_send_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationConfiguration.
        

#### `def test_serial_communication_configuration_init_fails_when_command_to_send_is_empty(self)`

Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationConfiguration.
        

#### `def test_serial_communication_configuration_init_fails_when_command_to_send_is_whitespace(self)`

Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationConfiguration.
        

#### `def test_serial_communication_configuration(self)`

Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationConfiguration.
        

### `class TestSerialCommunicationData(unittest.TestCase)`

Defines a test fixture that checks
    `SerialCommunicationData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_serial_communication_data_init_fails_when_received_response_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationData.
        

#### `def test_serial_communication_data_init_fails_when_received_response_is_empty(self)`

Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationData.
        

#### `def test_serial_communication_data_init_fails_when_received_response_is_whitespace(self)`

Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationData.
        

#### `def test_serial_communication_data(self)`

Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationData.
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/signal_voltage_generations/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/signal_voltage_generations/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for 
   nipcbatt.pcbatt_library.signal_voltage_generations package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/signal_voltage_generations/test_signal_voltage_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/signal_voltage_generations/test_signal_voltage_data_types.py

### MODULE DOCSTRING

This module provides Signal Voltage data types check.

### `class TestToneParameters(unittest.TestCase)`

Defines a test fixture that checks
    'ToneParameters' class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_tone_parameters(self)`

Tests if the instance of `ToneParameters` is created as expected

#### `def test_tone_parameters_with_invalid_parameters(self)`

Tests if  expected ValueError is thrown when an instance of
        `ToneParameters` is created with invalid parameters

### `class TestSignalVoltageGenerationTimingParameters(unittest.TestCase)`

Defines a test fixture that checks
    `SignalVoltageGenerationTimingParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_signal_voltage_generation_timing_parameters_init_fails_when_sample_clock_source_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SignalVoltageGenerationTimingParameters.
        

#### `def test_signal_voltage_generation_timing_parameters_init_fails_when_sample_clock_source_is_empty(self)`

Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SignalVoltageGenerationTimingParameters.
        

#### `def test_signal_voltage_generation_timing_parameters_init_fails_when_sample_clock_source_is_whitespace(self)`

Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SignalVoltageGenerationTimingParameters.
        

#### `def test_signal_voltage_generation_timing_parameters_init_fails_when_sampling_rate_hertz_is_less_than_zero(self)`

Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SignalVoltageGenerationTimingParameters.
        

#### `def test_signal_voltage_generation_timing_parameters_init_fails_when_generated_signal_duration_is_less_than_zero(self)`

Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SignalVoltageGenerationTimingParameters.
        

#### `def test_signal_voltage_generation_timing_parameters(self)`

Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SignalVoltageGenerationTimingParameters.
        

### `class TestSignalVoltageGenerationSineWaveParameters(unittest.TestCase)`

Defines a test fixture that checks
    'ToneParameters' class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_signal_voltage_generation_sine_wave_parameters(self)`

Tests if the instance of `SignalVoltageGenerationSineWaveParameters`
        is created as expected

#### `def test_signal_voltage_generation_sine_wave_parameters_init_fails_when_tone_parameters_is_none(self)`

Tests if  expected ValueError is thrown when an instance of
        `SignalVoltageGenerationSineWaveParameters` is created with signal_tone_parameters is none.
        

### `class TestSignalVoltageGenerationSquareWaveParameters(unittest.TestCase)`

Defines a test fixture that checks
    'SignalVoltageGenerationSquareWaveParameters' class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_signal_voltage_generation_square_wave_parameters(self)`

Tests if the instance of `SignalVoltageGenerationSquareWaveParameters`
        is created as expected

#### `def test_signal_voltage_generation_square_wave_parameters_init_fails_when_signal_frequency_is_less_than_zero(self)`

Tests if  expected ValueError is thrown when an instance of
        `SignalVoltageGenerationSquareWaveParameters` is created with signal frequency is set to 0.
        

#### `def test_signal_voltage_generation_square_wave_parameters_init_fails_when_signal_amplitude_is_less_than_zero(self)`

Tests if  expected ValueError is thrown when an instance of
        `SignalVoltageGenerationSquareWaveParameters` is created with signal amplitude is set to 0.
        

#### `def test_signal_voltage_generation_square_wave_parameters_init_fails_when_duty_cycle_is_not_within_limits(self)`

Tests if  expected ValueError is thrown when an instance of
        `SignalVoltageGenerationSquareWaveParameters` is created
        with duty_cycle value not within 0 and 100.
        

### `class TestSignalVoltageGenerationMultipleTonesWaveParameters(unittest.TestCase)`

Defines a test fixture that checks
    'SignalVoltageGenerationMultipleTonesWaveParameters' class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_signal_voltage_generation_multiple_tones_wave_parameters(self)`

Tests if the instance of `SignalVoltageGenerationMultipleTonesWaveParameters`
        is created as expected

#### `def test_signal_voltage_generation_multiple_tones_wave_parameters_with_signal_amplitude_zero(self)`

Tests if  expected ValueError is thrown when an instance of
        `SignalVoltageGenerationMultipleTonesWaveParameters` is created
        with signal_amplitude is set to 0.
        

#### `def test_signal_voltage_generation_multiple_tones_wave_parameters_with_tones_parameter_is_none(self)`

Tests if  expected ValueError is thrown when an instance of
        `SignalVoltageGenerationMultipleTonesWaveParameters` is created with
        multiple_tones_parameters is set to None.
        

#### `def test_signal_voltage_generation_multiple_tones_wave_parameters_with_tones_parameter_is_empty(self)`

Tests if  expected ValueError is thrown when an instance of
        `SignalVoltageGenerationMultipleTonesWaveParameters` is created with
        multiple_tones_parameters is set to empty list.
        

### `class TestSignalVoltageGenerationSineWaveConfiguration(unittest.TestCase)`

Defines a test fixture that checks
    'ToneParametersSignalVoltageGenerationSineWaveConfiguration' class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_signal_voltage_generation_sine_wave_configuration(self)`

Tests if the instance of `SignalVoltageGenerationSineWaveConfiguration`
        is created as expected

#### `def test_signal_voltage_generation_sine_wave_configuration_with_invalid_parameters(self)`

Tests if the instance creation with invalid parameters throws exception as expected

### `class TestSignalVoltageGenerationSquareWaveConfiguration(unittest.TestCase)`

Defines a test fixture that checks
    'SignalVoltageGenerationSquareWaveConfiguration' class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_signal_voltage_generation_square_wave_configuration(self)`

Tests if the instance of `SignalVoltageGenerationSquareWaveConfiguration`
        is created as expected

#### `def test_signal_voltage_generation_square_wave_configuration_with_invalid_parameters(self)`

Tests if  expected ValueError is thrown when an instance of
        `SignalVoltageGenerationSquareWaveConfiguration` is created with invalid parameters
        

### `class TestSignalVoltageGenerationMultipleTonesConfiguration(unittest.TestCase)`

Defines a test fixture that checks
    `SignalVoltageGenerationMultipleTonesConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_signal_voltage_generation_multiple_tones_configuration(self)`

Tests if the instance of `SignalVoltageGenerationMultipleTonesConfiguration`
        is created as expected

#### `def test_signal_voltage_generation_multiple_tones_configuration_with_invalid_parameters(self)`

Tests if the instance creation with invalid parameters throws exception as expected

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/signal_voltage_generations/test_signal_voltage_generation.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/signal_voltage_generations/test_signal_voltage_generation.py

### MODULE DOCSTRING

This module provides SignalVoltageGeneration check.

### `class TestSignalVoltageGeneration(unittest.TestCase)`

Defines a test fixture that checks
    `SignalVoltageGeneration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_signal_voltage_generation_sine_wave(self)`

Checks if class `SignalVoltageGeneration` is ready for use

#### `def test_signal_voltage_generation_square_wave(self)`

Checks if class `daq.PowerSupplySourceAndMeasureData` is ready for use for square wave generation

#### `def test_signal_voltage_generation_multiple_tones_wave(self)`

Checks if class `SignalVoltageGeneration` is ready for use
        for Multiple-tones generation

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for 
   nipcbatt.pcbatt_library.spi_communications package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/test_spi_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/test_spi_data_types.py

### MODULE DOCSTRING

This module provides SPI data types check.

### `class TestSpiDeviceParameters(unittest.TestCase)`

Defines a test fixture that checks
    `SpiDeviceParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_spi_device_parameters(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_data_types.SpiDeviceParameters.
        

### `class TestSpiCommunicationParameters(unittest.TestCase)`

Defines a test fixture that checks
    `SpiCommunicationParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_spi_communication_parameters_init_fails_when_clock_rate_kilohertz_is_equal_to_zero(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_data_types.SpiCommunicationParameters.
        

#### `def test_spi_communication_parameters_init_fails_when_clock_rate_kilohertz_is_less_than_zero(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_data_types.SpiCommunicationParameters.
        

#### `def test_spi_communication_parameters(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_data_types.SpiCommunicationParameters.
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/test_spi_read_communication.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/test_spi_read_communication.py

### MODULE DOCSTRING

This module provides SpiReadCommunication check.

### `class TestSpiReadCommunication(unittest.TestCase)`

Defines a test fixture that checks the `SpiReadCommunication` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_spi_read_communication(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_communication.SpiReadCommunication
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/test_spi_read_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/test_spi_read_data_types.py

### MODULE DOCSTRING

This module provides SPI read communication data types check.

### `class TestSpiReadParameters(unittest.TestCase)`

Defines a test fixture that checks
    `SpiReadParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_spi_read_parameters_init_fails_when_memory_address_parameters_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadParameters.
        

#### `def test_spi_read_parameters_init_fails_when_number_of_bytes_to_read_is_equal_to_zero(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadParameters.
        

#### `def test_spi_read_parameters_init_fails_when_number_of_bytes_to_read_is_less_than_zero(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadParameters.
        

#### `def test_spi_read_parameters(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadParameters.
        

### `class TestSpiReadCommunicationConfiguration(unittest.TestCase)`

Defines a test fixture that checks
    `SpiReadCommunicationConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_spi_read_communication_configuration_init_fails_when_device_parameters_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadCommunicationConfiguration.
        

#### `def test_spi_read_communication_configuration_init_fails_when_communication_parameters_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadCommunicationConfiguration.
        

#### `def test_spi_read_communication_configuration_init_fails_when_read_parameters_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadCommunicationConfiguration.
        

#### `def test_spi_read_communication_configuration(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadCommunicationConfiguration.
        

### `class TestSpiReadCommunicationData(unittest.TestCase)`

Defines a test fixture that checks
    `TestSpiReadCommunicationData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_spi_read_communication_data_init_fails_when_data_bytes_read_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadCommunicationData.
        

#### `def test_spi_read_communication_data_init_fails_when_data_bytes_read_is_empty(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadCommunicationData.
        

#### `def test_spi_read_communication_data(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadCommunicationData.
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/test_spi_write_communication.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/test_spi_write_communication.py

### MODULE DOCSTRING

This module provides SpiWriteCommunication check.

### `class TestSpiWriteCommunication(unittest.TestCase)`

Defines a test fixture that checks the `SpiWriteCommunication` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_spi_write_communication(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_communication.SpiWriteCommunication
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/test_spi_write_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/spi_communications/test_spi_write_data_types.py

### MODULE DOCSTRING

This module provides SPI write communication data types check.

### `class TestSpiWriteParameters(unittest.TestCase)`

Defines a test fixture that checks
    `SpiWriteParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_spi_write_parameters_init_fails_when_memory_address_parameters_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_data_types.SpiWriteParameters.
        

#### `def test_spi_write_parameters_init_fails_when_data_to_be_written_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_data_types.SpiWriteParameters.
        

#### `def test_spi_write_parameters_init_fails_when_data_to_be_written_is_empty(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_data_types.SpiWriteParameters.
        

#### `def test_spi_write_parameters_init_fails_when_number_of_bytes_per_page_is_less_than_zero(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_data_types.SpiWriteParameters.
        

#### `def test_spi_write_parameters_init_fails_when_number_of_bytes_per_page_is_equal_to_zero(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_data_types.SpiWriteParameters.
        

#### `def test_spi_write_parameters_init_fails_when_delay_between_page_write_operations_milliseconds_is_less_than_zero(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_data_types.SpiWriteParameters.
        

#### `def test_spi_write_parameters(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_data_types.SpiWriteParameters.
        

### `class TestSpiWriteCommunicationConfiguration(unittest.TestCase)`

Defines a test fixture that checks
    `SpiWriteCommunicationConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_spi_write_communication_configuration_init_fails_when_device_parameters_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_data_types.SpiWriteCommunicationConfiguration.
        

#### `def test_spi_write_communication_configuration_init_fails_when_communication_parameters_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_data_types.SpiWriteCommunicationConfiguration.
        

#### `def test_spi_write_communication_configuration_init_fails_when_write_parameters_is_none(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_data_types.SpiWriteCommunicationConfiguration.
        

#### `def test_spi_write_communication_configuration(self)`

Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_data_types.SpiWriteCommunicationConfiguration.
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/static_digital_path_tests/test_static_digital_path_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/static_digital_path_tests/test_static_digital_path_data_types.py

### MODULE DOCSTRING

This module provides static digital path data types check.

### `class TestStaticDigitalPathGenerationData(unittest.TestCase)`

Defines a test fixture that ensures the class 
       'StaticDigitalStateGenerationData' is correct and
       ready to use

    Args:
        unittest.TestCase: Base class from which this class inherits
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_static_digital_path_generation_channel_parameters(self)`

Test the creation of a StaticDigitalStateGenerationData object

#### `def test_static_digital_generation_channel_parameters_with_invalid_data(self)`

Tests the creation of StaticDigitalStateGenerationData object with
            invalid data. The value errors should be caught.

#### `def test_static_digital_path_generation_status_with_valid_data(self)`

Tests the generation static digital path status with valid data

#### `def test_static_digital_path_generation_status_false_is_valid(self)`

False should also be accepted as a valid status (non-float, non-None).

#### `def test_static_digital_path_generation_status_with_invalid_data(self)`

Tests the generation static digital path status with invalid data
            throws a ValueError as expected

#### `def test_static_digital_path_generation_timing_parameters_with_valid_data(self)`

Tests if a StaticDigitalTimingParameters object correctly 
        instantiates when given valid data

#### `def test_static_digital_generation_channel_parameters_with_whitespace(self)`

Whitespace-only channel names should be rejected.

#### `def test_static_digital_path_generation_state_parameters_valid_true_false(self)`

Both True and False should be accepted.

#### `def test_static_digital_path_generation_state_parameters_invalid(self)`

Invalid types should be rejected.

#### `def test_static_digital_path_generation_timing_parameters_zero_and_positive(self)`

Zero and positive max_debounce_wait are valid.

#### `def test_static_digital_path_generation_timing_parameters_invalid_negative(self)`

Negative values should be rejected.

#### `def test_static_digital_path_generation_terminal_and_state_settings_valid(self)`

Valid aggregation of channel + state parameters.

#### `def test_static_digital_path_generation_terminal_and_state_settings_invalid(self)`

None for either parameter should be rejected.

#### `def test_static_digital_path_generation_module_characteristics_valid(self)`

Non-negative floats should be accepted; properties should return exact values.

#### `def test_static_digital_path_generation_module_characteristics_invalid_none(self)`

Each field None should be rejected individually.

#### `def test_static_digital_path_generation_module_characteristics_invalid_negative(self)`

Negative values should be rejected for each field.

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_generations/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_generations/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for 
   nipcbatt.pcbatt_library.static_digital_state_generations package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_generations/test_static_digital_state_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_generations/test_static_digital_state_data_types.py

### MODULE DOCSTRING

This module provides state digital state data types check.

### `class TestStaticDigitalStateGenerationData(unittest.TestCase)`

Defines a test fixture that ensures the class
       'StaticDigitalStateGenerationData' is correct and
       ready to use

    Args:
        unittest.TestCase: Base class from which this class inherits
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_static_digital_state_generation_data(self)`

Tests the creation of a StaticDigitalStateGenerationData object

#### `def test_static_digital_state_generation_data_with_invalid_data(self)`

Tests the creation of an instance of StaticDigitalStateGeneration
        when using invalid data. It should produce and catch the associated error.
        

#### `def test_static_digital_state_generation_configuration(self)`

Tests the creation of an instance of StaticDigitalStateGeneration

#### `def test_static_digital_state_generation_configuration_with_invalid_data(self)`

Create an instance of DigitalStateGenerationConfiguration which is
        invalid and ensure this throws an error
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_generations/test_static_digital_state_generation.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_generations/test_static_digital_state_generation.py

### MODULE DOCSTRING

This module provides StaticDigitalStateGeneration check.

### `class TestStaticDigitalStateGeneration(unittest.TestCase)`

Defines a test fixture that ensures the class
       'StaticDigitalStateGeneration' is correct and
       ready to use

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_static_digital_state_generation(self)`

Checks if class 'StaticDigitalStateGeneration' is ready to use

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_measurements/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_measurements/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for 
   nipcbatt.pcbatt_library.static_digital_state_measurements package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_measurements/test_static_digital_state_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_measurements/test_static_digital_state_data_types.py

### MODULE DOCSTRING

This module provides Static digital state data types check.

### `class TestStaticDigitalStateMeasurementResultData(unittest.TestCase)`

Defines a test fixture that ensures the class
       'StaticDigitalStateMeasurementResultData' is correct
       and ready to use

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_static_digital_state_measurement_result_data(self)`

Tests the creation of a StaticDigitalStateMeasurementResultData object

#### `def test_static_digital_state_measurement_result_data_with_invalid_data(self)`

Tests if expected error is thrown when creating an instance of
        'StaticDigitalStateMeasurementResultData with invalid data

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_measurements/test_static_digital_state_measurement.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/static_digital_state_measurements/test_static_digital_state_measurement.py

### MODULE DOCSTRING

This module provides StaticDigitalStateMeasurement check.

### `class TestStaticDigitalStateMeasurement(unittest.TestCase)`

Defines a test fixture that ensures the class
       'StaticDigitalStateMeasurement' is correct
       and ready to use

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_static_digital_state_measurement(self)`

Checks if class 'StaticDigitalStateMeasurement' is ready for use

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/synchronizations/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/synchronizations/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for 
   nipcbatt.pcbatt_library.synchronizations package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/synchronizations/test_synchronization_signal_routing.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/synchronizations/test_synchronization_signal_routing.py

### MODULE DOCSTRING

This module provides SynchronizationSignalsRouting check.

### `class TestSynchronizationSignalRouting(unittest.TestCase)`

Defines a test fixture that checks
    `SynchronizationSignalRouting` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_route_sample_clock_signal_to_terminal_fails_when_terminal_name_is_none(self)`

unit test of SynchronizationSignalRouting.route_sample_clock_signal_to_terminal.

#### `def test_route_sample_clock_signal_to_terminal_fails_when_terminal_name_is_empty(self)`

unit test of SynchronizationSignalRouting.route_sample_clock_signal_to_terminal.

#### `def test_route_sample_clock_signal_to_terminal_fails_when_terminal_name_is_whitespace(self)`

unit test of SynchronizationSignalRouting.route_sample_clock_signal_to_terminal.

#### `def test_route_sample_clock_signal_to_terminal(self)`

unit test of SynchronizationSignalRouting.route_sample_clock_signal_to_terminal.

#### `def test_route_start_trigger_signal_to_terminal_fails_when_terminal_name_is_none(self)`

unit test of SynchronizationSignalRouting.route_start_trigger_signal_to_terminal.

#### `def test_route_start_trigger_signal_to_terminal_fails_when_terminal_name_is_empty(self)`

unit test of SynchronizationSignalRouting.route_start_trigger_signal_to_terminal.

#### `def test_route_start_trigger_signal_to_terminal_fails_when_terminal_name_is_whitespace(self)`

unit test of SynchronizationSignalRouting.route_start_trigger_signal_to_terminal.

#### `def test_route_start_trigger_signal_to_terminal(self)`

unit test of SynchronizationSignalRouting.route_start_trigger_signal_to_terminal.

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/temperature_measurements/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/temperature_measurements/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for 
   nipcbatt.pcbatt_library.temperature_measurements package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/temperature_measurements/test_temperature_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/temperature_measurements/test_temperature_data_types.py

### MODULE DOCSTRING

This module provides temperature data types check.

### `class TestTemperatureRtdMeasurementConfiguration(unittest.TestCase)`

Defines a test fixture that checks
    `TemperatureRtdMeasurementConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_temperature_rtd_measurement_configuration_init_fails_when_global_channel_parameters_is_none(self)`

unit test of TemperatureRtdMeasurementConfiguration.

#### `def test_temperature_rtd_measurement_configuration_init_fails_when_specific_channels_parameters_is_none(self)`

unit test of TemperatureRtdMeasurementConfiguration.

#### `def test_temperature_rtd_measurement_configuration_init_fails_when_sample_clock_timing_parameters_is_none(self)`

unit test of TemperatureRtdMeasurementConfiguration.

#### `def test_temperature_rtd_measurement_configuration_init_fails_when_digital_start_trigger_parameters_is_none(self)`

unit test of TemperatureRtdMeasurementConfiguration.

#### `def test_temperature_rtd_measurement_configuration(self)`

unit test of TemperatureRtdMeasurementConfiguration.

### `class TestTemperatureRtdMeasurementTerminalParameters(unittest.TestCase)`

Defines a test fixture that checks
    `TemperatureRtdMeasurementTerminalParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_temperature_rtd_measurement_terminal_parameters_init_fails_if_maximum_is_less_that_minimum(self)`

unit test of TemperatureRtdMeasurementTerminalParameters.

#### `def test_temperature_rtd_measurement_terminal_parameters(self)`

unit test of TemperatureRtdMeasurementTerminalParameters.

### `class TestTemperatureRtdMeasurementChannelParameters(unittest.TestCase)`

Defines a test fixture that checks
    `TemperatureRtdMeasurementTerminalParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_temperature_rtd_measurement_channel_parameters_init_fails_if_channel_name_is_none(self)`

unit test of TemperatureRtdMeasurementChannelParameters.

#### `def test_temperature_rtd_measurement_channel_parameters_init_fails_if_channel_name_is_empty(self)`

unit test of TemperatureRtdMeasurementChannelParameters.

#### `def test_temperature_rtd_measurement_channel_parameters_init_fails_if_channel_name_is_whitespace(self)`

unit test of TemperatureRtdMeasurementChannelParameters.

#### `def test_temperature_rtd_measurement_channel_parameters(self)`

unit test of TemperatureRtdMeasurementChannelParameters.

### `class TestTemperatureMeasurementResultData(unittest.TestCase)`

Defines a test fixture that checks
    `TemperatureMeasurementResultData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def __init__(self, methodName: str='runTest') -> None`

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_temperature_measurement_result_data_init_fails_when_waveforms_is_none(self)`

unit test of TemperatureMeasurementResultData.

#### `def test_temperature_measurement_result_data_init_fails_when_waveforms_is_empty(self)`

unit test of TemperatureMeasurementResultData.

#### `def test_temperature_measurement_result_data_init_fails_when_waveforms_contains_object_that_are_not_of_analog_waveform(self)`

unit test of TemperatureMeasurementResultData.

#### `def test_temperature_measurement_result_data_init_fails_when_average_temperatures_celsius_degrees_is_none(self)`

unit test of TemperatureMeasurementResultData.

#### `def test_temperature_measurement_result_data_init_fails_when_average_temperatures_celsius_degrees_is_empty(self)`

unit test of TemperatureMeasurementResultData.

#### `def test_temperature_measurement_result_data_init_fails_when_average_temperatures_celsius_degrees_contains_object_that_are_not_of_float(self)`

unit test of TemperatureMeasurementResultData.

#### `def test_temperature_measurement_result_data_init_fails_when_average_temperatures_kelvins_is_none(self)`

unit test of TemperatureMeasurementResultData.

#### `def test_temperature_measurement_result_data_init_fails_when_average_temperatures_kelvins_is_empty(self)`

unit test of TemperatureMeasurementResultData.

#### `def test_temperature_measurement_result_data_init_fails_when_average_temperatures_kelvins_contains_object_that_are_not_of_float(self)`

unit test of TemperatureMeasurementResultData.

#### `def _initialize_waveforms(self)`

### `class TestTemperatureThermistorMeasurementConfiguration(unittest.TestCase)`

Defines a test fixture that checks
    `TemperatureThermistorMeasurementConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_temperature_thermistor_measurement_configuration_init_fails_when_global_channel_parameters_is_none(self)`

unit test of TemperatureThermistorMeasurementConfiguration.

#### `def test_temperature_thermistor_measurement_configuration_init_fails_when_specific_channels_parameters_is_none(self)`

unit test of TemperatureThermistorMeasurementConfiguration.

#### `def test_temperature_thermistor_measurement_configuration_init_fails_when_sample_clock_timing_parameters_is_none(self)`

unit test of TemperatureThermistorMeasurementConfiguration.

#### `def test_temperature_thermistor_measurement_configuration_init_fails_when_digital_start_trigger_parameters_is_none(self)`

unit test of TemperatureThermistorMeasurementConfiguration.

#### `def test_temperature_thermistor_measurement_configuration(self)`

unit test of TemperatureThermistorMeasurementConfiguration.

### `class TestCoefficientsSteinhartHartParameters(unittest.TestCase)`

Defines a test fixture that checks
    `CoefficientsSteinhartHartParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_coefficients_steinhart_hart_parameters(self)`

unit test of CoefficientsSteinhartHartParameters.

### `class TestBetaCoefficientAndSensorResistanceParameters(unittest.TestCase)`

Defines a test fixture that checks
    `BetaCoefficientAndSensorResistanceParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_beta_coefficient_and_sensor_resistance_parameters(self)`

unit test of BetaCoefficientAndSensorResistanceParameters.

### `class TestTemperatureThermistorRangeAndTerminalParameters(unittest.TestCase)`

Defines a test fixture that checks
    `TemperatureThermistorRangeAndTerminalParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_temperature_thermistor_range_and_terminal_parameters_init_fails_if_maximum_is_less_that_minimum(self)`

unit test of TemperatureThermistorRangeAndTerminalParameters.

#### `def test_temperature_thermistor_range_and_terminal_parameters(self)`

unit test of TemperatureThermistorRangeAndTerminalParameters.

### `class TestTemperatureThermocoupleMeasurementConfiguration(unittest.TestCase)`

Defines a test fixture that checks
    `TemperatureThermocoupleMeasurementConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_temperature_thermocouple_measurement_configuration_init_fails_when_global_channel_parameters_is_none(self)`

unit test of TemperatureThermocoupleMeasurementConfiguration.

#### `def test_temperature_thermocouple_measurement_configuration_init_fails_when_specific_channels_parameters_is_none(self)`

unit test of TemperatureThermocoupleMeasurementConfiguration.

#### `def test_temperature_thermocouple_measurement_configuration_init_fails_when_sample_clock_timing_parameters_is_none(self)`

unit test of TemperatureThermocoupleMeasurementConfiguration.

#### `def test_temperature_thermocouple_measurement_configuration_init_fails_when_digital_start_trigger_parameters_is_none(self)`

unit test of TemperatureThermocoupleMeasurementConfiguration.

#### `def test_temperature_thermocouple_measurement_configuration(self)`

unit test of TemperatureThermocoupleMeasurementConfiguration.

### `class TestTemperatureThermocoupleMeasurementTerminalParameters(unittest.TestCase)`

Defines a test fixture that checks
    `TemperatureThermocoupleMeasurementTerminalParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_temperature_thermocouple_measurement_terminal_parameters_init_fails_if_maximum_is_less_that_minimum(self)`

unit test of TemperatureThermocoupleMeasurementTerminalParameters.

#### `def test_temperature_thermocouple_measurement_terminal_parameters_fails_if_perform_auto_zero_mode_is_none(self)`

unit test of TemperatureThermocoupleMeasurementTerminalParameters.

#### `def test_temperature_thermocouple_measurement_terminal_parameters_fails_if_auto_zero_mode_is_none(self)`

unit test of TemperatureThermocoupleMeasurementTerminalParameters.

#### `def test_temperature_thermocouple_measurement_terminal_parameters(self)`

unit test of TemperatureThermocoupleMeasurementTerminalParameters.

### `class TestTemperatureThermocoupleRangeAndTerminalParameters(unittest.TestCase)`

Defines a test fixture that checks
    `TemperatureThermocoupleRangeAndTerminalParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_temperature_thermocouple_range_and_terminal_parameters_init_fails_if_maximum_is_less_that_minimum(self)`

unit test of TemperatureThermocoupleRangeAndTerminalParameters.

#### `def test_temperature_thermocouple_range_and_terminal_parameters_fails_if_perform_auto_zero_mode_is_none(self)`

unit test of TemperatureThermocoupleRangeAndTerminalParameters.

#### `def test_temperature_thermocouple_range_and_terminal_parameters_fails_if_auto_zero_mode_is_none(self)`

unit test of TemperatureThermocoupleRangeAndTerminalParameters.

#### `def test_temperature_thermocouple_range_and_terminal_parameters(self)`

unit test of TemperatureThermocoupleRangeAndTerminalParameters.

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/temperature_measurements/test_temperature_measurement_using_rtd.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/temperature_measurements/test_temperature_measurement_using_rtd.py

### MODULE DOCSTRING

This module provides TemperatureMeasurementUsingRtd check.

### `class TestTemperatureMeasurementUsingRtd(unittest.TestCase)`

Defines a test fixture that checks
    `TemperatureMeasurementUsingRtd` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_temperature_measurement_using_rtd(self)`

Checks if class TemperatureMeasurementUsingRtd is ready to use

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/temperature_measurements/test_temperature_measurement_using_thermistor.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/temperature_measurements/test_temperature_measurement_using_thermistor.py

### MODULE DOCSTRING

This module provides TemperatureMeasurementUsingThermistor check.

### `class TestTemperatureMeasurementUsingThermistor(unittest.TestCase)`

Defines a test fixture that checks
    `TemperatureMeasurementUsingThermistor` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_temperature_measurement_using_thermistor(self)`

Checks if class TemperatureMeasurementUsingThermistor is ready to use

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/temperature_measurements/test_temperature_measurement_using_thermocouple.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/temperature_measurements/test_temperature_measurement_using_thermocouple.py

### MODULE DOCSTRING

This module provides TemperatureMeasurementUsingThermocouple check.

### `class TestTemperatureMeasurementUsingThermocouple(unittest.TestCase)`

Defines a test fixture that checks
    `TemperatureMeasurementUsingThermocouple` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_temperature_measurement_using_thermocouple(self)`

Checks if class TemperatureMeasurementUsingThermocouple is ready to use

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/time_domain_measurements/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/time_domain_measurements/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for 
   nipcbatt.pcbatt_library.time_domain_measurements package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/time_domain_measurements/test_time_domain_data_types.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/time_domain_measurements/test_time_domain_data_types.py

### MODULE DOCSTRING

This module provides time domain data types check.

### `class TestTimeDomainMeasurementConfiguration(unittest.TestCase)`

Defines a test fixture that checks
    `TimeDomainMeasurementConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_time_domain_measurement_configuration_init_fails_when_global_channel_parameters_is_none(self)`

unit test of TimeDomainMeasurementConfiguration.

#### `def test_time_domain_measurement_configuration_init_fails_when_specific_channels_parameters_is_none(self)`

unit test of TimeDomainMeasurementConfiguration.

#### `def test_time_domain_measurement_configuration_init_fails_when_measurement_options_is_none(self)`

unit test of TimeDomainMeasurementConfiguration.

#### `def test_time_domain_measurement_configuration_init_fails_when_sample_clock_timing_parameters_is_none(self)`

unit test of TimeDomainMeasurementConfiguration.

#### `def test_time_domain_measurement_configuration_init_fails_when_digital_start_trigger_parameters_is_none(self)`

unit test of TimeDomainMeasurementConfiguration.

#### `def test_time_domain_measurement_configuration(self)`

unit test of TimeDomainMeasurementConfiguration.

### `class TestTimeDomainMeasurementResultData(unittest.TestCase)`

Defines a test fixture that checks
    `TimeDomainMeasurementResultData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def __init__(self, methodName: str='runTest') -> None`

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_time_domain_measurement_result_data_init_fails_when_waveforms_is_none(self)`

unit test of TestTimeDomainMeasurementResultData.

#### `def test_time_domain_measurement_result_data_init_fails_when_waveforms_is_empty(self)`

unit test of TestTimeDomainMeasurementResultData.

#### `def test_time_domain_measurement_result_data_init_fails_when_waveforms_contains_object_that_are_not_of_analog_waveform(self)`

unit test of TestTimeDomainMeasurementResultData.

#### `def test_time_domain_measurement_result_data_init_fails_when_mean_dc_voltage_values_volts_is_none(self)`

unit test of TestTimeDomainMeasurementResultData.

#### `def test_time_domain_measurement_result_data_init_fails_when_mean_dc_voltage_values_volts_is_empty(self)`

unit test of TestTimeDomainMeasurementResultData.

#### `def test_time_domain_measurement_result_data_init_fails_when_mean_dc_voltage_values_volts_contains_object_that_are_not_of_float(self)`

unit test of TestTimeDomainMeasurementResultData.

#### `def test_time_domain_measurement_result_data_init_fails_when_vpp_amplitudes_volts_is_none(self)`

unit test of TestTimeDomainMeasurementResultData.

#### `def test_time_domain_measurement_result_data_init_fails_when_vpp_amplitudes_volts_is_empty(self)`

unit test of TestTimeDomainMeasurementResultData.

#### `def test_time_domain_measurement_result_data_init_fails_when_vpp_amplitudes_volts_contains_object_that_are_not_of_float(self)`

unit test of TestTimeDomainMeasurementResultData.

#### `def test_time_domain_measurement_result_data_init_fails_when_voltage_waveforms_frequencies_hertz_is_none(self)`

unit test of TestTimeDomainMeasurementResultData.

#### `def test_time_domain_measurement_result_data_init_does_not_fail_when_voltage_waveforms_frequencies_hertz_is_empty(self)`

unit test of TestTimeDomainMeasurementResultData.

#### `def test_time_domain_measurement_result_data_init_fails_when_voltage_waveforms_frequencies_hertz_contains_object_that_are_not_of_float(self)`

unit test of TestTimeDomainMeasurementResultData.

#### `def test_time_domain_measurement_result_data_init_fails_when_voltage_waveforms_periods_seconds_is_none(self)`

unit test of TestTimeDomainMeasurementResultData.

#### `def test_time_domain_measurement_result_data_init_does_not_fail_when_voltage_waveforms_periods_seconds_is_empty(self)`

unit test of TestTimeDomainMeasurementResultData.

#### `def test_time_domain_measurement_result_data_init_fails_when_voltage_waveforms_periods_seconds_contains_object_that_are_not_of_float(self)`

unit test of TestTimeDomainMeasurementResultData.

#### `def test_time_domain_measurement_result_data_init_fails_when_voltage_waveforms_duty_cycles_percent_is_none(self)`

unit test of TestTimeDomainMeasurementResultData.

#### `def test_time_domain_measurement_result_data_init_does_not_fail_when_voltage_waveforms_duty_cycles_percent_is_empty(self)`

unit test of TestTimeDomainMeasurementResultData.

#### `def test_time_domain_measurement_result_data_init_fails_when_voltage_waveforms_duty_cycles_percent_contains_object_that_are_not_of_float(self)`

unit test of TestTimeDomainMeasurementResultData.

#### `def test_time_domain_measurement_result_data(self)`

unit test of TestTimeDomainMeasurementResultData.

#### `def _initialize_waveforms(self)`

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/time_domain_measurements/test_time_domain_measurement.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_library_tests/time_domain_measurements/test_time_domain_measurement.py

### MODULE DOCSTRING

This module provides TimeDomainMeasurement check.

### `class TestTimeDomainMeasurement(unittest.TestCase)`

Defines a test fixture that checks
    `TimeDomainMeasurement` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_time_domain_measurement(self)`

Checks if class TimeDomainMeasurement is ready to use

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_utilities_tests/__init__.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_utilities_tests/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for nipcbatt.pcbatt_utilities package

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_utilities_tests/test_csv_utilities.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_utilities_tests/test_csv_utilities.py

### MODULE DOCSTRING

Provides unit tests related to functional_utilities.py module

### `class TestCsvUtilities(unittest.TestCase)`

Defines a test fixture that checks function of module
    `pcbatt_utilities.csv_utilities`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_export_signal_to_csv_file(self)`

Unit test of csv_utilities.export_signal_to_csv_file

#### `def test_export_columns_to_csv_file(self)`

Unit test of csv_utilities.export_to_csv_file_columns

#### `def test_import_from_csv_file_2d_array(self)`

Unit test of csv_utilities.import_from_csv_file_2d_array

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_utilities_tests/test_file_utilities.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_utilities_tests/test_file_utilities.py

### MODULE DOCSTRING

Provides unit tests related to file_utilities.py module

### `class TestFileUtilities(unittest.TestCase)`

Defines a test fixture that checks function of module
    `pcbatt_utilities.file_utilities`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_write_lines(self)`

Unit test of file_utilities.write_lines

#### `def test_read_lines(self)`

Unit test of file_utilities.read_lines

#### `def test_file_exists_should_not_fail(self, file_path: str)`

Unit test of nipcbatt.pcbatt_utilities.file_utilities.file_exists

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_utilities_tests/test_functional_utilities.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_utilities_tests/test_functional_utilities.py

### MODULE DOCSTRING

Provides unit tests related to functional_utilities.py module

### `class TestFunctionalUtilities(unittest.TestCase)`

Defines a test fixture that checks function of module
    `pcbatt_utilities.functional_utilities`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_repeat(self)`

Unit test of functional_utilities.repeat

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_utilities_tests/test_guard_utilities.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_utilities_tests/test_guard_utilities.py

### MODULE DOCSTRING

Provides unit tests related to guard_utilities.py module

### `class TestGuard(unittest.TestCase)`

Defines a test fixture that checks function of module
    `nipcbatt.pcbatt_utilities.guard_utilities.Guard`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_is_not_empty_fails_if_iterable_empty(self)`

Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_not_empty

#### `def test_is_not_empty_should_not_fail_if_iterable_not_empty(self)`

Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_not_empty

#### `def test_size_of_iterable_breaks_iterator(self)`

Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.size_is_greater_or_equal_than

#### `def test_size_is_greater_or_equal_than_fails_if_iterable_has_not_enough_elements(self)`

Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.size_is_greater_or_equal_than

#### `def test_size_is_greater_or_equal_than_should_not_fail(self)`

Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.size_is_greater_or_equal_than

#### `def test_size_is_less_than_or_equal_fails_if_iterable_is_too_large(self)`

Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.Guard.size_is_less_than_or_equal

#### `def test_size_is_less_than_or_equal_should_not_fail(self)`

Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.Guard.size_is_less_than_or_equal

#### `def test_all_elements_are_of_same_type_fails_if_list_contains_invalid_objects(self)`

Unit test
        of nipcbatt.pcbatt_utilities.guard_utilities.Guard.all_elements_are_of_same_type
        

#### `def test_all_elements_are_of_same_type_should_not_fail(self)`

Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.all_elements_are_of_same_type

#### `def test_have_same_size_fails_if_lists_have_not_same_size(self)`

Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.have_same_size

#### `def test_have_same_size_should_not_fail(self)`

Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.have_same_size

#### `def test_is_not_none_fails_if_object_is_none(self)`

Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_not_none

#### `def test_is_not_none_should_not_fail(self)`

Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_not_none

#### `def test_is_greater_than_zero_fails_if_object_is_string(self)`

Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_zero

#### `def test_is_greater_than_zero_fails_if_object_is_less_than_or_equal_to_zero(self)`

Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_zero

#### `def test_is_greater_than_zero_should_not_fail(self)`

Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_zero

#### `def test_is_greater_than_or_equal_to_zero_fails_if_object_is_string(self)`

Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_or_equal_to_zero
        

#### `def test_is_greater_than_or_equal_to_zero_fails_if_object_is_negative(self)`

Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_or_equal_to_zero
        

#### `def test_is_greater_than_or_equal_to_zero_should_not_fail(self)`

Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_or_equal_to_zero
        

#### `def test_is_less_than_zero_fails_if_object_is_string(self)`

Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_zero

#### `def test_is_less_than_zero_fails_if_object_is_positive_or_equal_to_zero(self)`

Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_zero

#### `def test_is_less_than_zero_should_not_fail(self)`

Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_zero

#### `def test_is_less_than_or_equal_to_zero_fails_if_object_is_string(self)`

Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_or_equal_to_zero

#### `def test_is_less_than_or_equal_to_zero_fails_if_object_is_greater_than_zero(self)`

Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_or_equal_to_zero

#### `def test_is_less_than_or_equal_to_zero_should_not_fail(self)`

Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_or_equal_to_zero

#### `def test_is_less_than_fails_if_value_is_string(self)`

Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than

#### `def test_is_less_than_fails_if_expected_greater_value_is_string(self)`

Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than

#### `def test_is_less_than_fails_if_value_is_greater_or_equal(self)`

Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than

#### `def test_is_less_than_should_not_fail(self)`

Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than

#### `def test_is_less_than_or_equal_to_fails_if_value_is_string(self)`

Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_or_equal_to

#### `def test_is_less_than_or_equal_to_fails_if_expected_greater_value_is_string(self)`

Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_or_equal_to

#### `def test_is_less_than_or_equal_to_fails_if_value_is_greater(self)`

Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_or_equal_to

#### `def test_is_less_than_or_equal_to_should_not_fail(self)`

Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_or_equal_to

#### `def test_is_greater_than_fails_if_value_is_string(self)`

Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than

#### `def test_is_greater_than_fails_if_expected_smaller_value_is_string(self)`

Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than

#### `def test_is_greater_than_fails_if_value_is_less_than_or_equal_to(self)`

Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than

#### `def test_is_greater_than_should_not_fail(self)`

Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than

#### `def test_is_greater_or_equal_to_fails_if_value_is_string(self)`

Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_or_equal_to

#### `def test_is_greater_than_or_equal_to_fails_if_expected_smaller_value_is_string(self)`

Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_or_equal_to

#### `def test_is_greater_than_or_equal_to_fails_if_value_is_less_than(self)`

Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_or_equal_to

#### `def test_is_greater_than_or_equal_to_should_not_fail(self)`

Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_or_equal_to

#### `def test_is_not_none_nor_empty_nor_whitespace_fails_if_string_value_is_none(self)`

Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_not_none_nor_empty_nor_whitespace
        

#### `def test_is_not_none_nor_empty_nor_whitespace_fails_if_string_value_is_empty(self)`

Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_not_none_nor_empty_nor_whitespace
        

#### `def test_is_not_none_nor_empty_nor_whitespace_fails_if_string_value_is_whitespace(self)`

Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_not_none_nor_empty_nor_whitespace
        

#### `def test_is_not_none_nor_empty_nor_whitespace_should_not_fail(self)`

Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_not_none_nor_empty_nor_whitespace
        

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_utilities_tests/test_iterable_utilities.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_utilities_tests/test_iterable_utilities.py

### MODULE DOCSTRING

Provides unit tests related to iterable_utilities.py module

### `class TestIterableUtilities(unittest.TestCase)`

Defines a test fixture that checks function of module
    `pcbatt_utilities.iterable_utilities`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_count_invalid_input(self)`

Unit test of iterable_utilities.count

#### `def test_count(self)`

Unit test of iterable_utilities.count

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_utilities_tests/test_native_interop_utilities.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_utilities_tests/test_native_interop_utilities.py

### MODULE DOCSTRING

This module provides check of functions in 
nipcbatt.pcbatt_library_code.ni_845x_i2c_spi_communications.ni_845x_helper_functions package

### `class TestCreateNativeStdCallWinFunction(unittest.TestCase)`

Defines a test fixture that checks
    `_create_native_stdcall_win_function` function is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_create_native_stdcall_win_function_fails_if_dll_path(self, test_name: str, dll_path: str)`

unit test of _create_native_stdcall_win_function.

#### `def test_create_native_stdcall_win_function_fails_if_function_name_is_invalid(self, test_name: str, function_name: str)`

unit test of _create_native_stdcall_win_function.

#### `def test_create_native_stdcall_win_function_fails_if_library_not_exist(self)`

unit test of _create_native_stdcall_win_function.

#### `def test_create_native_stdcall_win_function_fails_if_function_not_found(self)`

unit test of _create_native_stdcall_win_function.

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_utilities_tests/test_numeric_utilities.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_utilities_tests/test_numeric_utilities.py

### MODULE DOCSTRING

Provides unit tests related to numeric_utilities.py module

### `class TestNumericUtilities(unittest.TestCase)`

Defines a test fixture that checks function of module
    `pcbatt_utilities.numeric_utilities`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_invert_value(self)`

Unit test of numeric_utilities.invert_value

#### `def test_absolute_value(self)`

Unit test of numeric_utilities.absolute_value

#### `def test_percent_of(self)`

Unit test of numeric_utilities.percent_of

#### `def test_from_percent_to_decimal_ratio(self)`

Unit test of numeric_utilities.percent_of

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_utilities_tests/test_os_utilities.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_utilities_tests/test_os_utilities.py

### MODULE DOCSTRING

Provides unit tests related to os_utilities.py module

### `class TestOsUtilities(unittest.TestCase)`

Defines a test fixture that checks function of module
    `pcbatt_utilities.os_utilities`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_is_path_absolute_should_not_fail(self, file_path: str, expected_value: bool)`

Unit test of nipcbatt.pcbatt_utilities.os_utilities.is_path_absolute

#### `def test_combine_path_components_should_not_fail(self, path: str, expected_combined_path: str, *paths: str)`

Unit test of nipcbatt.pcbatt_utilities.os_utilities.combine_path_components

<!--NI_PYTHON_API repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_utilities_tests/test_platform_utilities.py -->
## PYTHON MODULE: tests/nipcbatt_tests/pcbatt_utilities_tests/test_platform_utilities.py

### MODULE DOCSTRING

Provides unit tests related to platform_utilities.py module

### `class TestPlatformUtilities(unittest.TestCase)`

Defines a test fixture that checks function of module
    `pcbatt_utilities.platform_utilities`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_is_python_windows_32bits(self)`

Unit test of pcbatt_utilities.platform_utilities.is_python_windows_32bits

#### `def test_is_python_windows_64bits(self)`

Unit test of pcbatt_utilities.platform_utilities.is_python_windows_64bits

<!--NI_PYTHON_API repo=nipcbatt path=tests/requirements_tests/__init__.py -->
## PYTHON MODULE: tests/requirements_tests/__init__.py

### MODULE DOCSTRING

Provides a set of unit tests for nipcbatt dependent packages

<!--NI_PYTHON_API repo=nipcbatt path=tests/requirements_tests/test_numpy.py -->
## PYTHON MODULE: tests/requirements_tests/test_numpy.py

### MODULE DOCSTRING

This module provides numpy framework check.

### `class TestNDArray(unittest.TestCase)`

Defines a test fixture that provides sample usage of ndarray datastructure.

    Args:
        unittest (TestCase): test case using unittest framework
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_ndarray_zeros_array(self)`

Checks method numpy.zeros is ready to use

#### `def test_ndarray_create_single_dimension_array(self)`

Checks method numpy.array is ready to use

#### `def test_ndarray_create_two_dimensions_array(self)`

Checks method numpy.ndarray is ready to use

#### `def test_ndarray_sum_single_dimension_array(self)`

Checks method numpy.sum is ready to use

#### `def test_ndarray_mean_single_dimension_array(self)`

Checks method numpy.mean is ready to use

### `class TestMatlib(unittest.TestCase)`

Defines a test fixture that checks numpy package is ready to use.

    Args:
        unittest (_type_): test case type
    

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def test_mathlib_average(self)`

Checks method numpy.matlib.average is ready to use

#### `def test_mathlib_amax(self)`

Checks method numpy.matlib.amax is ready to use

#### `def test_mathlib_amin(self)`

Checks method numpy.matlib.amin is ready to use

#### `def test_mathlib_all(self)`

Checks method numpy.matlib.all is ready to use

<!--NI_PYTHON_API repo=nipcbatt path=tests/requirements_tests/test_scipy.py -->
## PYTHON MODULE: tests/requirements_tests/test_scipy.py

### MODULE DOCSTRING

This module provides scipy framework check.

### `class TestSignal(unittest.TestCase)`

Defines a test fixture that checks scipy package is ready to use.

    Args:
        unittest (TestCase): test case type
    

#### `def setUpClass(cls)`

#### `def tearDownClass(cls)`

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def test_signal_windows_hann(self)`

Checks method scipy.signal.windows.hann is ready to use

#### `def test_signal_windows_hamming(self)`

Checks method scipy.signal.windows.hamming is ready to use

#### `def test_signal_find_peaks(self)`

Checks method scipy.signal.find_peaks is ready to use

#### `def test_signal_square(self)`

Checks method scipy.signal.square is ready to use

#### `def test_signal_sawtooth(self)`

Checks method scipy.signal.sawtooth is ready to use

<!--NI_PYTHON_API repo=nipcbatt path=tests/requirements_tests/test_unittest.py -->
## PYTHON MODULE: tests/requirements_tests/test_unittest.py

### MODULE DOCSTRING

This module provides unit tests framework check.

### `class TestUnittest(unittest.TestCase)`

Defines a test fixture that checks unit test framework is ready to use.

    Args:
        unittest (unittest.TestCase): test case type
    

#### `def setUp(self)`

#### `def tearDown(self)`

#### `def test_assert_equal(self)`

Checks method unittest.TestCase.assertEqual is ready to use

#### `def test_assert_almost_equal(self)`

Checks method unittest.TestCase.assertAlmostEqual is ready to use

#### `def test_assert_assert_count_equal(self)`

Checks method unittest.TestCase.assertCountEqual is ready to use

#### `def test_assert_sequence_equal(self)`

Checks method unittest.TestCase.assertSequenceEqual is ready to use

#### `def test_assert_dict_equal(self)`

Checks method unittest.TestCase.assertDictEqual is ready to use

#### `def test_assert_in(self)`

Checks method unittest.TestCase.assertIn is ready to use

#### `def test_assert_not_in(self)`

Checks method unittest.TestCase.assertNotIn is ready to use

#### `def test_assert_is_not_none(self)`

Checks method unittest.TestCase.assertIsNotNone is ready to use

#### `def test_assert_is_none(self)`

Checks method unittest.TestCase.assertIsNotNone is ready to use
