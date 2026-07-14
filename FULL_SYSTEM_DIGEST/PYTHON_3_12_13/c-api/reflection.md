# PYTHON_3_12_13::c-api/reflection.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=c-api/reflection.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

Reflection
**********

PyObject *PyEval_GetBuiltins(void)
    *Return value: Borrowed reference.** Part of the Stable ABI.*

   Return a dictionary of the builtins in the current execution frame,
   or the interpreter of the thread state if no frame is currently
   executing.

PyObject *PyEval_GetLocals(void)
    *Return value: Borrowed reference.** Part of the Stable ABI.*

   Return a dictionary of the local variables in the current execution
   frame, or "NULL" if no frame is currently executing.

PyObject *PyEval_GetGlobals(void)
    *Return value: Borrowed reference.** Part of the Stable ABI.*

   Return a dictionary of the global variables in the current
   execution frame, or "NULL" if no frame is currently executing.

PyFrameObject *PyEval_GetFrame(void)
    *Return value: Borrowed reference.** Part of the Stable ABI.*

   Return the current thread state's frame, which is "NULL" if no
   frame is currently executing.

   See also "PyThreadState_GetFrame()".

const char *PyEval_GetFuncName(PyObject *func)
    * Part of the Stable ABI.*

   Return the name of *func* if it is a function, class or instance
   object, else the name of *func*s type.

const char *PyEval_GetFuncDesc(PyObject *func)
    * Part of the Stable ABI.*

   Return a description string, depending on the type of *func*.
   Return values include "()" for functions and methods, "
   constructor", " instance", and " object".  Concatenated with the
   result of "PyEval_GetFuncName()", the result will be a description
   of *func*.
