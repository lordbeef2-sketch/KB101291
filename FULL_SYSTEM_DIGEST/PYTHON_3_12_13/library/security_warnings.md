# PYTHON_3_12_13::library/security_warnings.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=library/security_warnings.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

Security Considerations
***********************

The following modules have specific security considerations:

* "base64": base64 security considerations in **RFC 4648**

* "cgi": CGI security considerations

* "hashlib": all constructors take a "usedforsecurity" keyword-only
  argument disabling known insecure and blocked algorithms

* "http.server" is not suitable for production use, only implementing
  basic security checks. See the security considerations.

* "logging": Logging configuration uses eval()

* "multiprocessing": Connection.recv() uses pickle

* "pickle": Restricting globals in pickle

* "random" shouldn't be used for security purposes, use "secrets"
  instead

* "shelve": shelve is based on pickle and thus unsuitable for dealing
  with untrusted sources

* "ssl": SSL/TLS security considerations

* "subprocess": Subprocess security considerations

* "tempfile": mktemp is deprecated due to vulnerability to race
  conditions

* "xml": XML vulnerabilities

* "zipfile": maliciously prepared .zip files can cause disk volume
  exhaustion

The "-I" command line option can be used to run Python in isolated
mode. When it cannot be used, the "-P" option or the "PYTHONSAFEPATH"
environment variable can be used to not prepend a potentially unsafe
path to "sys.path" such as the current directory, the script's
directory or an empty string.
