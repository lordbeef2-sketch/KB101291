# PYTHON_3_12_13::library/language.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=library/language.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

Python Language Services
************************

Python provides a number of modules to assist in working with the
Python language.  These modules support tokenizing, parsing, syntax
analysis, bytecode disassembly, and various other facilities.

These modules include:

* "ast" --- Abstract Syntax Trees

  * Abstract Grammar

  * Node classes

    * Root nodes

    * Literals

    * Variables

    * Expressions

      * Subscripting

      * Comprehensions

    * Statements

      * Imports

    * Control flow

    * Pattern matching

    * Type parameters

    * Function and class definitions

    * Async and await

  * "ast" Helpers

  * Compiler Flags

  * Command-Line Usage

* "symtable" --- Access to the compiler's symbol tables

  * Generating Symbol Tables

  * Examining Symbol Tables

* "token" --- Constants used with Python parse trees

* "keyword" --- Testing for Python keywords

* "tokenize" --- Tokenizer for Python source

  * Tokenizing Input

  * Command-Line Usage

  * Examples

* "tabnanny" --- Detection of ambiguous indentation

* "pyclbr" --- Python module browser support

  * Function Objects

  * Class Objects

* "py_compile" --- Compile Python source files

  * Command-Line Interface

* "compileall" --- Byte-compile Python libraries

  * Command-line use

  * Public functions

* "dis" --- Disassembler for Python bytecode

  * Command-line interface

  * Bytecode analysis

  * Analysis functions

  * Python Bytecode Instructions

  * Opcode collections

* "pickletools" --- Tools for pickle developers

  * Command line usage

    * Command line options

  * Programmatic Interface
