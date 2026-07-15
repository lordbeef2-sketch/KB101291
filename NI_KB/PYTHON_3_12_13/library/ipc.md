# PYTHON_3_12_13::library/ipc.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=library/ipc.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

Networking and Interprocess Communication
*****************************************

The modules described in this chapter provide mechanisms for
networking and inter-processes communication.

Some modules only work for two processes that are on the same machine,
e.g. "signal" and "mmap".  Other modules support networking protocols
that two or more processes can use to communicate across machines.

The list of modules described in this chapter is:

* "asyncio" --- Asynchronous I/O

* "socket" --- Low-level networking interface

* "ssl" --- TLS/SSL wrapper for socket objects

* "select" --- Waiting for I/O completion

* "selectors" --- High-level I/O multiplexing

* "signal" --- Set handlers for asynchronous events

* "mmap" --- Memory-mapped file support
