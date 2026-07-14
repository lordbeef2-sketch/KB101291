# PYTHON_3_12_13::library/getpass.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=library/getpass.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

"getpass" --- Portable password input
*************************************

**Source code:** Lib/getpass.py

======================================================================

Availability: not Emscripten, not WASI.

This module does not work or is not available on WebAssembly platforms
"wasm32-emscripten" and "wasm32-wasi". See WebAssembly platforms for
more information.

The "getpass" module provides two functions:

getpass.getpass(prompt='Password: ', stream=None)

   Prompt the user for a password without echoing.  The user is
   prompted using the string *prompt*, which defaults to "'Password:
   '".  On Unix, the prompt is written to the file-like object
   *stream* using the replace error handler if needed.  *stream*
   defaults to the controlling terminal ("/dev/tty") or if that is
   unavailable to "sys.stderr" (this argument is ignored on Windows).

   If echo free input is unavailable getpass() falls back to printing
   a warning message to *stream* and reading from "sys.stdin" and
   issuing a "GetPassWarning".

   Note:

     If you call getpass from within IDLE, the input may be done in
     the terminal you launched IDLE from rather than the idle window
     itself.

exception getpass.GetPassWarning

   A "UserWarning" subclass issued when password input may be echoed.

getpass.getuser()

   Return the "login name" of the user.

   This function checks the environment variables "LOGNAME", "USER",
   "LNAME" and "USERNAME", in order, and returns the value of the
   first one which is set to a non-empty string.  If none are set, the
   login name from the password database is returned on systems which
   support the "pwd" module, otherwise, an exception is raised.

   In general, this function should be preferred over "os.getlogin()".
