# PYTHON_3_12_13::library/builtins.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=library/builtins.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

"builtins" --- Built-in objects
*******************************

======================================================================

This module provides direct access to all 'built-in' identifiers of
Python; for example, "builtins.open" is the full name for the built-in
function "open()".

This module is not normally accessed explicitly by most applications,
but can be useful in modules that provide objects with the same name
as a built-in value, but in which the built-in of that name is also
needed.  For example, in a module that wants to implement an "open()"
function that wraps the built-in "open()", this module can be used
directly:

   import builtins

   def open(path):
       f = builtins.open(path, 'r')
       return UpperCaser(f)

   class UpperCaser:
       '''Wrapper around a file that converts output to uppercase.'''

       def __init__(self, f):
           self._f = f

       def read(self, count=-1):
           return self._f.read(count).upper()

       # ...

As an implementation detail, most modules have the name "__builtins__"
made available as part of their globals.  The value of "__builtins__"
is normally either this module or the value of this module's
"__dict__" attribute. Since this is an implementation detail, it may
not be used by alternate implementations of Python.

See also:

  * Built-in Constants

  * Built-in Exceptions

  * Built-in Functions

  * Built-in Types
