# PYTHON_3_12_13::library/crypto.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=library/crypto.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

Cryptographic Services
**********************

The modules described in this chapter implement various algorithms of
a cryptographic nature.  They are available at the discretion of the
installation. On Unix systems, the "crypt" module may also be
available. Here's an overview:

* "hashlib" --- Secure hashes and message digests

  * Hash algorithms

  * Usage

  * Constructors

  * Attributes

  * Hash Objects

  * SHAKE variable length digests

  * File hashing

  * Key derivation

  * BLAKE2

    * Creating hash objects

    * Constants

    * Examples

      * Simple hashing

      * Using different digest sizes

      * Keyed hashing

      * Randomized hashing

      * Personalization

      * Tree mode

    * Credits

* "hmac" --- Keyed-Hashing for Message Authentication

* "secrets" --- Generate secure random numbers for managing secrets

  * Random numbers

  * Generating tokens

    * How many bytes should tokens use?

  * Other functions

  * Recipes and best practices
