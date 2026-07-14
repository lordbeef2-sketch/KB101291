# PYTHON_3_12_13::c-api/hash.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=c-api/hash.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

PyHash API
**********

See also the "PyTypeObject.tp_hash" member.

type Py_hash_t

   Hash value type: signed integer.

   Added in version 3.2.

type Py_uhash_t

   Hash value type: unsigned integer.

   Added in version 3.2.

type PyHash_FuncDef

   Hash function definition used by "PyHash_GetFuncDef()".

   const char *name

      Hash function name (UTF-8 encoded string).

   const int hash_bits

      Internal size of the hash value in bits.

   const int seed_bits

      Size of seed input in bits.

   Added in version 3.4.

PyHash_FuncDef *PyHash_GetFuncDef(void)

   Get the hash function definition.

   See also: **PEP 456** "Secure and interchangeable hash algorithm".

   Added in version 3.4.
