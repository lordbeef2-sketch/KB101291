# PYTHON_3_12_13::deprecations/c-api-pending-removal-in-3.14.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=deprecations/c-api-pending-removal-in-3.14.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

Pending Removal in Python 3.14
******************************

* The "ma_version_tag" field in "PyDictObject" for extension modules
  (**PEP 699**; gh-101193).

* Creating "immutable types" with mutable bases (gh-95388).

* Functions to configure Python's initialization, deprecated in Python
  3.11:

  * "PySys_SetArgvEx()": Set "PyConfig.argv" instead.

  * "PySys_SetArgv()": Set "PyConfig.argv" instead.

  * "Py_SetProgramName()": Set "PyConfig.program_name" instead.

  * "Py_SetPythonHome()": Set "PyConfig.home" instead.

  The "Py_InitializeFromConfig()" API should be used with "PyConfig"
  instead.

* Global configuration variables:

  * "Py_DebugFlag": Use "PyConfig.parser_debug" instead.

  * "Py_VerboseFlag": Use "PyConfig.verbose" instead.

  * "Py_QuietFlag": Use "PyConfig.quiet" instead.

  * "Py_InteractiveFlag": Use "PyConfig.interactive" instead.

  * "Py_InspectFlag": Use "PyConfig.inspect" instead.

  * "Py_OptimizeFlag": Use "PyConfig.optimization_level" instead.

  * "Py_NoSiteFlag": Use "PyConfig.site_import" instead.

  * "Py_BytesWarningFlag": Use "PyConfig.bytes_warning" instead.

  * "Py_FrozenFlag": Use "PyConfig.pathconfig_warnings" instead.

  * "Py_IgnoreEnvironmentFlag": Use "PyConfig.use_environment"
    instead.

  * "Py_DontWriteBytecodeFlag": Use "PyConfig.write_bytecode" instead.

  * "Py_NoUserSiteDirectory": Use "PyConfig.user_site_directory"
    instead.

  * "Py_UnbufferedStdioFlag": Use "PyConfig.buffered_stdio" instead.

  * "Py_HashRandomizationFlag": Use "PyConfig.use_hash_seed" and
    "PyConfig.hash_seed" instead.

  * "Py_IsolatedFlag": Use "PyConfig.isolated" instead.

  * "Py_LegacyWindowsFSEncodingFlag": Use
    "PyPreConfig.legacy_windows_fs_encoding" instead.

  * "Py_LegacyWindowsStdioFlag": Use "PyConfig.legacy_windows_stdio"
    instead.

  * "Py_FileSystemDefaultEncoding": Use "PyConfig.filesystem_encoding"
    instead.

  * "Py_HasFileSystemDefaultEncoding": Use
    "PyConfig.filesystem_encoding" instead.

  * "Py_FileSystemDefaultEncodeErrors": Use
    "PyConfig.filesystem_errors" instead.

  * "Py_UTF8Mode": Use "PyPreConfig.utf8_mode" instead. (see
    "Py_PreInitialize()")

  The "Py_InitializeFromConfig()" API should be used with "PyConfig"
  instead.
