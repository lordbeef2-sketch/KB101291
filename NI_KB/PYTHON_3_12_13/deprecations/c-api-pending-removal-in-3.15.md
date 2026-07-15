# PYTHON_3_12_13::deprecations/c-api-pending-removal-in-3.15.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=deprecations/c-api-pending-removal-in-3.15.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

Pending Removal in Python 3.15
******************************

* The bundled copy of "libmpdecimal".

* The "PyImport_ImportModuleNoBlock()": Use "PyImport_ImportModule()"
  instead.

* "PyWeakref_GetObject()" and "PyWeakref_GET_OBJECT()": Use
  "PyWeakref_GetRef()" instead.

* "Py_UNICODE" type and the "Py_UNICODE_WIDE" macro: Use "wchar_t"
  instead.

* Python initialization functions:

  * "PySys_ResetWarnOptions()": Clear "sys.warnoptions" and
    "warnings.filters" instead.

  * "Py_GetExecPrefix()": Get "sys.exec_prefix" instead.

  * "Py_GetPath()": Get "sys.path" instead.

  * "Py_GetPrefix()": Get "sys.prefix" instead.

  * "Py_GetProgramFullPath()": Get "sys.executable" instead.

  * "Py_GetProgramName()": Get "sys.executable" instead.

  * "Py_GetPythonHome()": Get "PyConfig.home" or the "PYTHONHOME"
    environment variable instead.
