# PYTHON_3_12_13::c-api/descriptor.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=c-api/descriptor.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

Descriptor Objects
******************

"Descriptors" are objects that describe some attribute of an object.
They are found in the dictionary of type objects.

PyTypeObject PyProperty_Type
    * Part of the Stable ABI.*

   The type object for the built-in descriptor types.

PyObject *PyDescr_NewGetSet(PyTypeObject *type, struct PyGetSetDef *getset)
    *Return value: New reference.** Part of the Stable ABI.*

PyObject *PyDescr_NewMember(PyTypeObject *type, struct PyMemberDef *meth)
    *Return value: New reference.** Part of the Stable ABI.*

PyObject *PyDescr_NewMethod(PyTypeObject *type, struct PyMethodDef *meth)
    *Return value: New reference.** Part of the Stable ABI.*

PyObject *PyDescr_NewWrapper(PyTypeObject *type, struct wrapperbase *wrapper, void *wrapped)
    *Return value: New reference.*

PyObject *PyDescr_NewClassMethod(PyTypeObject *type, PyMethodDef *method)
    *Return value: New reference.** Part of the Stable ABI.*

int PyDescr_IsData(PyObject *descr)

   Return non-zero if the descriptor objects *descr* describes a data
   attribute, or "0" if it describes a method.  *descr* must be a
   descriptor object; there is no error checking.

PyObject *PyWrapper_New(PyObject*, PyObject*)
    *Return value: New reference.** Part of the Stable ABI.*
