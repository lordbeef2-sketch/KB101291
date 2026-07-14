# PYTHON_3_12_13::c-api/none.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=c-api/none.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

The "None" Object
*****************

Note that the "PyTypeObject" for "None" is not directly exposed in the
Python/C API.  Since "None" is a singleton, testing for object
identity (using "==" in C) is sufficient. There is no "PyNone_Check()"
function for the same reason.

PyObject *Py_None

   The Python "None" object, denoting lack of value.  This object has
   no methods and is immortal.

Changed in version 3.12: "Py_None" is immortal.

Py_RETURN_NONE

   Return "Py_None" from a function.
