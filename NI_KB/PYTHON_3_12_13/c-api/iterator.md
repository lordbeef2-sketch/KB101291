# PYTHON_3_12_13::c-api/iterator.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=c-api/iterator.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

Iterator Objects
****************

Python provides two general-purpose iterator objects.  The first, a
sequence iterator, works with an arbitrary sequence supporting the
"__getitem__()" method.  The second works with a callable object and a
sentinel value, calling the callable for each item in the sequence,
and ending the iteration when the sentinel value is returned.

PyTypeObject PySeqIter_Type
    * Part of the Stable ABI.*

   Type object for iterator objects returned by "PySeqIter_New()" and
   the one-argument form of the "iter()" built-in function for built-
   in sequence types.

int PySeqIter_Check(PyObject *op)

   Return true if the type of *op* is "PySeqIter_Type".  This function
   always succeeds.

PyObject *PySeqIter_New(PyObject *seq)
    *Return value: New reference.** Part of the Stable ABI.*

   Return an iterator that works with a general sequence object,
   *seq*.  The iteration ends when the sequence raises "IndexError"
   for the subscripting operation.

PyTypeObject PyCallIter_Type
    * Part of the Stable ABI.*

   Type object for iterator objects returned by "PyCallIter_New()" and
   the two-argument form of the "iter()" built-in function.

int PyCallIter_Check(PyObject *op)

   Return true if the type of *op* is "PyCallIter_Type".  This
   function always succeeds.

PyObject *PyCallIter_New(PyObject *callable, PyObject *sentinel)
    *Return value: New reference.** Part of the Stable ABI.*

   Return a new iterator.  The first parameter, *callable*, can be any
   Python callable object that can be called with no parameters; each
   call to it should return the next item in the iteration.  When
   *callable* returns a value equal to *sentinel*, the iteration will
   be terminated.
