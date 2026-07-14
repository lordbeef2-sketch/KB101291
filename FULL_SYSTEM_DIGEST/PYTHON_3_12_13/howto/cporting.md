# PYTHON_3_12_13::howto/cporting.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=howto/cporting.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

Porting Extension Modules to Python 3
*************************************

We recommend the following resources for porting extension modules to
Python 3:

* The Migrating C extensions chapter from *Supporting Python 3: An in-
  depth guide*, a book on moving from Python 2 to Python 3 in general,
  guides the reader through porting an extension module.

* The Porting guide from the *py3c* project provides opinionated
  suggestions with supporting code.

* The Cython and CFFI libraries offer abstractions over Python's C
  API. Extensions generally need to be re-written to use one of them,
  but the library then handles differences between various Python
  versions and implementations.
