# PYTHON_3_12_13::library/custominterp.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=library/custominterp.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

Custom Python Interpreters
**************************

The modules described in this chapter allow writing interfaces similar
to Python's interactive interpreter.  If you want a Python interpreter
that supports some special feature in addition to the Python language,
you should look at the "code" module.  (The "codeop" module is lower-
level, used to support compiling a possibly incomplete chunk of Python
code.)

The full list of modules described in this chapter is:

* "code" --- Interpreter base classes

  * Interactive Interpreter Objects

  * Interactive Console Objects

* "codeop" --- Compile Python code
