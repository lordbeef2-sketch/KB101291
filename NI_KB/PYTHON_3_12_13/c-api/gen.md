# PYTHON_3_12_13::c-api/gen.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=c-api/gen.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

Generator Objects
*****************

Generator objects are what Python uses to implement generator
iterators. They are normally created by iterating over a function that
yields values, rather than explicitly calling "PyGen_New()" or
"PyGen_NewWithQualName()".

type PyGenObject

   The C structure used for generator objects.

PyTypeObject PyGen_Type

   The type object corresponding to generator objects.

int PyGen_Check(PyObject *ob)

   Return true if *ob* is a generator object; *ob* must not be "NULL".
   This function always succeeds.

int PyGen_CheckExact(PyObject *ob)

   Return true if *ob*'s type is "PyGen_Type"; *ob* must not be
   "NULL".  This function always succeeds.

PyObject *PyGen_New(PyFrameObject *frame)
    *Return value: New reference.*

   Create and return a new generator object based on the *frame*
   object. A reference to *frame* is stolen by this function. The
   argument must not be "NULL".

PyObject *PyGen_NewWithQualName(PyFrameObject *frame, PyObject *name, PyObject *qualname)
    *Return value: New reference.*

   Create and return a new generator object based on the *frame*
   object, with "__name__" and "__qualname__" set to *name* and
   *qualname*. A reference to *frame* is stolen by this function.  The
   *frame* argument must not be "NULL".
