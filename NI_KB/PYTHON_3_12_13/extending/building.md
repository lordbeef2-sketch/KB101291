# PYTHON_3_12_13::extending/building.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=extending/building.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

4. Building C and C++ Extensions
********************************

A C extension for CPython is a shared library (e.g. a ".so" file on
Linux, ".pyd" on Windows), which exports an *initialization function*.

To be importable, the shared library must be available on
"PYTHONPATH", and must be named after the module name, with an
appropriate extension. When using setuptools, the correct filename is
generated automatically.

The initialization function has the signature:

PyObject *PyInit_modulename(void)

It returns either a fully initialized module, or a "PyModuleDef"
instance. See Initializing C modules for details.

For modules with ASCII-only names, the function must be named
"PyInit_<modulename>", with "<modulename>" replaced by the name of the
module. When using Multi-phase initialization, non-ASCII module names
are allowed. In this case, the initialization function name is
"PyInitU_<modulename>", with "<modulename>" encoded using Python's
*punycode* encoding with hyphens replaced by underscores. In Python:

   def initfunc_name(name):
       try:
           suffix = b'_' + name.encode('ascii')
       except UnicodeEncodeError:
           suffix = b'U_' + name.encode('punycode').replace(b'-', b'_')
       return b'PyInit' + suffix

It is possible to export multiple modules from a single shared library
by defining multiple initialization functions. However, importing them
requires using symbolic links or a custom importer, because by default
only the function corresponding to the filename is found. See the
*"Multiple modules in one library"* section in **PEP 489** for
details.


4.1. Building C and C++ Extensions with setuptools
==================================================

Python 3.12 and newer no longer come with distutils. Please refer to
the "setuptools" documentation at
https://setuptools.readthedocs.io/en/latest/setuptools.html to learn
more about how build and distribute C/C++ extensions with setuptools.
