# PYTHON_3_12_13::library/archiving.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=library/archiving.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

Data Compression and Archiving
******************************

The modules described in this chapter support data compression with
the zlib, gzip, bzip2 and lzma algorithms, and the creation of ZIP-
and tar-format archives.  See also Archiving operations provided by
the "shutil" module.

* "zlib" --- Compression compatible with **gzip**

* "gzip" --- Support for **gzip** files

  * Examples of usage

  * Command Line Interface

    * Command line options

* "bz2" --- Support for **bzip2** compression

  * (De)compression of files

  * Incremental (de)compression

  * One-shot (de)compression

  * Examples of usage

* "lzma" --- Compression using the LZMA algorithm

  * Reading and writing compressed files

  * Compressing and decompressing data in memory

  * Miscellaneous

  * Specifying custom filter chains

  * Examples

* "zipfile" --- Work with ZIP archives

  * ZipFile Objects

  * Path Objects

  * PyZipFile Objects

  * ZipInfo Objects

  * Command-Line Interface

    * Command-line options

  * Decompression pitfalls

    * From file itself

    * File System limitations

    * Resources limitations

    * Interruption

    * Default behaviors of extraction

* "tarfile" --- Read and write tar archive files

  * TarFile Objects

  * TarInfo Objects

  * Extraction filters

    * Default named filters

    * Filter errors

    * Hints for further verification

    * Supporting older Python versions

    * Stateful extraction filter example

  * Command-Line Interface

    * Command-line options

  * Examples

  * Supported tar formats

  * Unicode issues
