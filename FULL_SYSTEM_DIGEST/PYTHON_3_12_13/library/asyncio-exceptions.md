# PYTHON_3_12_13::library/asyncio-exceptions.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=library/asyncio-exceptions.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

Exceptions
**********

**Source code:** Lib/asyncio/exceptions.py

======================================================================

exception asyncio.TimeoutError

   A deprecated alias of "TimeoutError", raised when the operation has
   exceeded the given deadline.

   Changed in version 3.11: This class was made an alias of
   "TimeoutError".

exception asyncio.CancelledError

   The operation has been cancelled.

   This exception can be caught to perform custom operations when
   asyncio Tasks are cancelled.  In almost all situations the
   exception must be re-raised.

   Changed in version 3.8: "CancelledError" is now a subclass of
   "BaseException" rather than "Exception".

exception asyncio.InvalidStateError

   Invalid internal state of "Task" or "Future".

   Can be raised in situations like setting a result value for a
   *Future* object that already has a result value set.

exception asyncio.SendfileNotAvailableError

   The "sendfile" syscall is not available for the given socket or
   file type.

   A subclass of "RuntimeError".

exception asyncio.IncompleteReadError

   The requested read operation did not complete fully.

   Raised by the asyncio stream APIs.

   This exception is a subclass of "EOFError".

   expected

      The total number ("int") of expected bytes.

   partial

      A string of "bytes" read before the end of stream was reached.

exception asyncio.LimitOverrunError

   Reached the buffer size limit while looking for a separator.

   Raised by the asyncio stream APIs.

   consumed

      The total number of to be consumed bytes.
