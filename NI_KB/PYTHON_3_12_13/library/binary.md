# PYTHON_3_12_13::library/binary.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=library/binary.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

Binary Data Services
********************

The modules described in this chapter provide some basic services
operations for manipulation of binary data. Other operations on binary
data, specifically in relation to file formats and network protocols,
are described in the relevant sections.

Some libraries described under Text Processing Services also work with
either ASCII-compatible binary formats (for example, "re") or all
binary data (for example, "difflib").

In addition, see the documentation for Python's built-in binary data
types in Binary Sequence Types --- bytes, bytearray, memoryview.

* "struct" --- Interpret bytes as packed binary data

  * Functions and Exceptions

  * Format Strings

    * Byte Order, Size, and Alignment

    * Format Characters

    * Examples

  * Applications

    * Native Formats

    * Standard Formats

  * Classes

* "codecs" --- Codec registry and base classes

  * Codec Base Classes

    * Error Handlers

    * Stateless Encoding and Decoding

    * Incremental Encoding and Decoding

      * IncrementalEncoder Objects

      * IncrementalDecoder Objects

    * Stream Encoding and Decoding

      * StreamWriter Objects

      * StreamReader Objects

      * StreamReaderWriter Objects

      * StreamRecoder Objects

  * Encodings and Unicode

  * Standard Encodings

  * Python Specific Encodings

    * Text Encodings

    * Binary Transforms

    * Text Transforms

  * "encodings.idna" --- Internationalized Domain Names in
    Applications

  * "encodings.mbcs" --- Windows ANSI codepage

  * "encodings.utf_8_sig" --- UTF-8 codec with BOM signature
