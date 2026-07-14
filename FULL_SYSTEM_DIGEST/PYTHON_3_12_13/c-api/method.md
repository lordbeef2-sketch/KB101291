# PYTHON_3_12_13::c-api/method.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=c-api/method.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

Instance Method Objects
***********************

An instance method is a wrapper for a "PyCFunction" and the new way to
bind a "PyCFunction" to a class object. It replaces the former call
"PyMethod_New(func, NULL, class)".

PyTypeObject PyInstanceMethod_Type

   This instance of "PyTypeObject" represents the Python instance
   method type. It is not exposed to Python programs.

int PyInstanceMethod_Check(PyObject *o)

   Return true if *o* is an instance method object (has type
   "PyInstanceMethod_Type").  The parameter must not be "NULL". This
   function always succeeds.

PyObject *PyInstanceMethod_New(PyObject *func)
    *Return value: New reference.*

   Return a new instance method object, with *func* being any callable
   object. *func* is the function that will be called when the
   instance method is called.

PyObject *PyInstanceMethod_Function(PyObject *im)
    *Return value: Borrowed reference.*

   Return the function object associated with the instance method
   *im*.

PyObject *PyInstanceMethod_GET_FUNCTION(PyObject *im)
    *Return value: Borrowed reference.*

   Macro version of "PyInstanceMethod_Function()" which avoids error
   checking.


Method Objects
**************

Methods are bound function objects. Methods are always bound to an
instance of a user-defined class. Unbound methods (methods bound to a
class object) are no longer available.

PyTypeObject PyMethod_Type

   This instance of "PyTypeObject" represents the Python method type.
   This is exposed to Python programs as "types.MethodType".

int PyMethod_Check(PyObject *o)

   Return true if *o* is a method object (has type "PyMethod_Type").
   The parameter must not be "NULL".  This function always succeeds.

PyObject *PyMethod_New(PyObject *func, PyObject *self)
    *Return value: New reference.*

   Return a new method object, with *func* being any callable object
   and *self* the instance the method should be bound. *func* is the
   function that will be called when the method is called. *self* must
   not be "NULL".

PyObject *PyMethod_Function(PyObject *meth)
    *Return value: Borrowed reference.*

   Return the function object associated with the method *meth*.

PyObject *PyMethod_GET_FUNCTION(PyObject *meth)
    *Return value: Borrowed reference.*

   Macro version of "PyMethod_Function()" which avoids error checking.

PyObject *PyMethod_Self(PyObject *meth)
    *Return value: Borrowed reference.*

   Return the instance associated with the method *meth*.

PyObject *PyMethod_GET_SELF(PyObject *meth)
    *Return value: Borrowed reference.*

   Macro version of "PyMethod_Self()" which avoids error checking.
