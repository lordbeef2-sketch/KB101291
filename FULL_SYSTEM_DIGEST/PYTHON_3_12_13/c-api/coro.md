# PYTHON_3_12_13::c-api/coro.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=c-api/coro.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

Coroutine Objects
*****************

Added in version 3.5.

Coroutine objects are what functions declared with an "async" keyword
return.

type PyCoroObject

   The C structure used for coroutine objects.

PyTypeObject PyCoro_Type

   The type object corresponding to coroutine objects.

int PyCoro_CheckExact(PyObject *ob)

   Return true if *ob*'s type is "PyCoro_Type"; *ob* must not be
   "NULL". This function always succeeds.

PyObject *PyCoro_New(PyFrameObject *frame, PyObject *name, PyObject *qualname)
    *Return value: New reference.*

   Create and return a new coroutine object based on the *frame*
   object, with "__name__" and "__qualname__" set to *name* and
   *qualname*. A reference to *frame* is stolen by this function.  The
   *frame* argument must not be "NULL".
