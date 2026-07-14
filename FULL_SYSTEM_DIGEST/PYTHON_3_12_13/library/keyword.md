# PYTHON_3_12_13::library/keyword.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=library/keyword.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

"keyword" --- Testing for Python keywords
*****************************************

**Source code:** Lib/keyword.py

======================================================================

This module allows a Python program to determine if a string is a
keyword or soft keyword.

keyword.iskeyword(s)

   Return "True" if *s* is a Python keyword.

keyword.kwlist

   Sequence containing all the keywords defined for the interpreter.
   If any keywords are defined to only be active when particular
   "__future__" statements are in effect, these will be included as
   well.

keyword.issoftkeyword(s)

   Return "True" if *s* is a Python soft keyword.

   Added in version 3.9.

keyword.softkwlist

   Sequence containing all the soft keywords defined for the
   interpreter.  If any soft keywords are defined to only be active
   when particular "__future__" statements are in effect, these will
   be included as well.

   Added in version 3.9.
