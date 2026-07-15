# PYTHON_3_12_13::howto/argparse-optparse.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=howto/argparse-optparse.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

Upgrading optparse code
***********************

Originally, the "argparse" module had attempted to maintain
compatibility with "optparse".  However, "optparse" was difficult to
extend transparently, particularly with the changes required to
support "nargs=" specifiers and better usage messages.  When most
everything in "optparse" had either been copy-pasted over or monkey-
patched, it no longer seemed practical to try to maintain the
backwards compatibility.

The "argparse" module improves on the "optparse" module in a number of
ways including:

* Handling positional arguments.

* Supporting subcommands.

* Allowing alternative option prefixes like "+" and "/".

* Handling zero-or-more and one-or-more style arguments.

* Producing more informative usage messages.

* Providing a much simpler interface for custom "type" and "action".

A partial upgrade path from "optparse" to "argparse":

* Replace all "optparse.OptionParser.add_option()" calls with
  "ArgumentParser.add_argument()" calls.

* Replace "(options, args) = parser.parse_args()" with "args =
  parser.parse_args()" and add additional
  "ArgumentParser.add_argument()" calls for the positional arguments.
  Keep in mind that what was previously called "options", now in the
  "argparse" context is called "args".

* Replace "optparse.OptionParser.disable_interspersed_args()" by using
  "parse_intermixed_args()" instead of "parse_args()".

* Replace callback actions and the "callback_*" keyword arguments with
  "type" or "action" arguments.

* Replace string names for "type" keyword arguments with the
  corresponding type objects (e.g. int, float, complex, etc).

* Replace "optparse.Values" with "Namespace" and
  "optparse.OptionError" and "optparse.OptionValueError" with
  "ArgumentError".

* Replace strings with implicit arguments such as "%default" or
  "%prog" with the standard Python syntax to use dictionaries to
  format strings, that is, "%(default)s" and "%(prog)s".

* Replace the OptionParser constructor "version" argument with a call
  to "parser.add_argument('--version', action='version', version='<the
  version>')".
