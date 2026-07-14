# PYTHON_3_12_13::deprecations/pending-removal-in-3.16.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=deprecations/pending-removal-in-3.16.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

Pending Removal in Python 3.16
******************************

* The import system:

  * Setting "__loader__" on a module while failing to set
    "__spec__.loader" is deprecated. In Python 3.16, "__loader__" will
    cease to be set or taken into consideration by the import system
    or the standard library.

* "array": "array.array" "'u'" type ("wchar_t"): use the "'w'" type
  instead ("Py_UCS4").

* "builtins": "~bool", bitwise inversion on bool.

* "symtable": Deprecate "symtable.Class.get_methods()" due to the lack
  of interest. (Contributed by Bénédikt Tran in gh-119698.)
