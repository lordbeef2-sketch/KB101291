# PYTHON_3_12_13::deprecations/c-api-pending-removal-in-future.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=deprecations/c-api-pending-removal-in-future.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

Pending Removal in Future Versions
**********************************

The following APIs are deprecated and will be removed, although there
is currently no date scheduled for their removal.

* "Py_TPFLAGS_HAVE_FINALIZE": Unneeded since Python 3.8.

* "PyErr_Fetch()": Use "PyErr_GetRaisedException()" instead.

* "PyErr_NormalizeException()": Use "PyErr_GetRaisedException()"
  instead.

* "PyErr_Restore()": Use "PyErr_SetRaisedException()" instead.

* "PyModule_GetFilename()": Use "PyModule_GetFilenameObject()"
  instead.

* "PyOS_AfterFork()": Use "PyOS_AfterFork_Child()" instead.

* "PySlice_GetIndicesEx()": Use "PySlice_Unpack()" and
  "PySlice_AdjustIndices()" instead.

* "PyUnicode_AsDecodedObject()": Use "PyCodec_Decode()" instead.

* "PyUnicode_AsDecodedUnicode()": Use "PyCodec_Decode()" instead.

* "PyUnicode_AsEncodedObject()": Use "PyCodec_Encode()" instead.

* "PyUnicode_AsEncodedUnicode()": Use "PyCodec_Encode()" instead.

* "PyUnicode_READY()": Unneeded since Python 3.12

* "PyErr_Display()": Use "PyErr_DisplayException()" instead.

* "_PyErr_ChainExceptions()": Use "_PyErr_ChainExceptions1()" instead.

* "PyBytesObject.ob_shash" member: call "PyObject_Hash()" instead.

* "PyDictObject.ma_version_tag" member.

* Thread Local Storage (TLS) API:

  * "PyThread_create_key()": Use "PyThread_tss_alloc()" instead.

  * "PyThread_delete_key()": Use "PyThread_tss_free()" instead.

  * "PyThread_set_key_value()": Use "PyThread_tss_set()" instead.

  * "PyThread_get_key_value()": Use "PyThread_tss_get()" instead.

  * "PyThread_delete_key_value()": Use "PyThread_tss_delete()"
    instead.

  * "PyThread_ReInitTLS()": Unneeded since Python 3.7.
