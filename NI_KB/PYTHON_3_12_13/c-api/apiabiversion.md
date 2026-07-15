# PYTHON_3_12_13::c-api/apiabiversion.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=c-api/apiabiversion.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

API and ABI Versioning
**********************

CPython exposes its version number in the following macros. Note that
these correspond to the version code is **built** with, not
necessarily the version used at **run time**.

See C API Stability for a discussion of API and ABI stability across
versions.

PY_MAJOR_VERSION

   The "3" in "3.4.1a2".

PY_MINOR_VERSION

   The "4" in "3.4.1a2".

PY_MICRO_VERSION

   The "1" in "3.4.1a2".

PY_RELEASE_LEVEL

   The "a" in "3.4.1a2". This can be "0xA" for alpha, "0xB" for beta,
   "0xC" for release candidate or "0xF" for final.

PY_RELEASE_SERIAL

   The "2" in "3.4.1a2". Zero for final releases.

PY_VERSION_HEX

   The Python version number encoded in a single integer.

   The underlying version information can be found by treating it as a
   32 bit number in the following manner:

   +---------+---------------------------+---------------------------+----------------------------+
   | Bytes   | Bits (big endian order)   | Meaning                   | Value for "3.4.1a2"        |
   |=========|===========================|===========================|============================|
   | 1       | 1-8                       | "PY_MAJOR_VERSION"        | "0x03"                     |
   +---------+---------------------------+---------------------------+----------------------------+
   | 2       | 9-16                      | "PY_MINOR_VERSION"        | "0x04"                     |
   +---------+---------------------------+---------------------------+----------------------------+
   | 3       | 17-24                     | "PY_MICRO_VERSION"        | "0x01"                     |
   +---------+---------------------------+---------------------------+----------------------------+
   | 4       | 25-28                     | "PY_RELEASE_LEVEL"        | "0xA"                      |
   |         +---------------------------+---------------------------+----------------------------+
   |         | 29-32                     | "PY_RELEASE_SERIAL"       | "0x2"                      |
   +---------+---------------------------+---------------------------+----------------------------+

   Thus "3.4.1a2" is hexversion "0x030401a2" and "3.10.0" is
   hexversion "0x030a00f0".

   Use this for numeric comparisons, e.g. "#if PY_VERSION_HEX >= ...".

   This version is also available via the symbol "Py_Version".

const unsigned long Py_Version
    * Part of the Stable ABI since version 3.11.*

   The Python runtime version number encoded in a single constant
   integer, with the same format as the "PY_VERSION_HEX" macro. This
   contains the Python version used at run time.

   Added in version 3.11.

All the given macros are defined in Include/patchlevel.h.
