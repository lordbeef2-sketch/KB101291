# PYTHON_3_12_13::c-api/iter.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=c-api/iter.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

Iterator Protocol
*****************

There are two functions specifically for working with iterators.

int PyIter_Check(PyObject *o)
    * Part of the Stable ABI since version 3.8.*

   Return non-zero if the object *o* can be safely passed to
   "PyIter_Next()", and "0" otherwise.  This function always succeeds.

int PyAIter_Check(PyObject *o)
    * Part of the Stable ABI since version 3.10.*

   Return non-zero if the object *o* provides the "AsyncIterator"
   protocol, and "0" otherwise.  This function always succeeds.

   Added in version 3.10.

PyObject *PyIter_Next(PyObject *o)
    *Return value: New reference.** Part of the Stable ABI.*

   Return the next value from the iterator *o*.  The object must be an
   iterator according to "PyIter_Check()" (it is up to the caller to
   check this). If there are no remaining values, returns "NULL" with
   no exception set. If an error occurs while retrieving the item,
   returns "NULL" and passes along the exception.

To write a loop which iterates over an iterator, the C code should
look something like this:

   PyObject *iterator = PyObject_GetIter(obj);
   PyObject *item;

   if (iterator == NULL) {
       /* propagate error */
   }

   while ((item = PyIter_Next(iterator))) {
       /* do something with item */
       ...
       /* release reference when done */
       Py_DECREF(item);
   }

   Py_DECREF(iterator);

   if (PyErr_Occurred()) {
       /* propagate error */
   }
   else {
       /* continue doing useful work */
   }

type PySendResult

   The enum value used to represent different results of
   "PyIter_Send()".

   Added in version 3.10.

PySendResult PyIter_Send(PyObject *iter, PyObject *arg, PyObject **presult)
    * Part of the Stable ABI since version 3.10.*

   Sends the *arg* value into the iterator *iter*. Returns:

   * "PYGEN_RETURN" if iterator returns. Return value is returned via
     *presult*.

   * "PYGEN_NEXT" if iterator yields. Yielded value is returned via
     *presult*.

   * "PYGEN_ERROR" if iterator has raised and exception. *presult* is
     set to "NULL".

   Added in version 3.10.
