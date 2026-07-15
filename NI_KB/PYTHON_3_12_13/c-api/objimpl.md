# PYTHON_3_12_13::c-api/objimpl.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=c-api/objimpl.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

Object Implementation Support
*****************************

This chapter describes the functions, types, and macros used when
defining new object types.

* Allocating Objects on the Heap

* Common Object Structures

  * Base object types and macros

  * Implementing functions and methods

  * Accessing attributes of extension types

    * Member flags

    * Member types

    * Defining Getters and Setters

* Type Object Structures

  * Quick Reference

    * "tp slots"

    * sub-slots

    * slot typedefs

  * PyTypeObject Definition

  * PyObject Slots

  * PyVarObject Slots

  * PyTypeObject Slots

  * Static Types

  * Heap Types

  * Number Object Structures

  * Mapping Object Structures

  * Sequence Object Structures

  * Buffer Object Structures

  * Async Object Structures

  * Slot Type typedefs

  * Examples

* Supporting Cyclic Garbage Collection

  * Controlling the Garbage Collector State

  * Querying Garbage Collector State
