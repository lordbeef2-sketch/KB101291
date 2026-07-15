# PYTHON_3_12_13::deprecations/pending-removal-in-3.13.md

<!--SYSTEM_CORPUS id=PYTHON_3_12_13 source_path=deprecations/pending-removal-in-3.13.txt -->
- source: https://docs.python.org/3.12/
- archive_sha256: 48e950ab70335f2f49bd0418eaa26ab225942cd9c100e15428dc4f70f21b6ba0
- license: Python Software Foundation License Version 2; documentation examples additionally Zero Clause BSD
- fidelity: full-official-plain-text-document

Pending Removal in Python 3.13
******************************

Modules (see **PEP 594**):

* "aifc"

* "audioop"

* "cgi"

* "cgitb"

* "chunk"

* "crypt"

* "imghdr"

* "mailcap"

* "msilib"

* "nis"

* "nntplib"

* "ossaudiodev"

* "pipes"

* "sndhdr"

* "spwd"

* "sunau"

* "telnetlib"

* "uu"

* "xdrlib"

Other modules:

* "lib2to3", and the **2to3** program (gh-84540)

APIs:

* "configparser.LegacyInterpolation" (gh-90765)

* "locale.resetlocale()" (gh-90817)

* "turtle.RawTurtle.settiltangle()" (gh-50096)

* "unittest.findTestCases()" (gh-50096)

* "unittest.getTestCaseNames()" (gh-50096)

* "unittest.makeSuite()" (gh-50096)

* "unittest.TestProgram.usageExit()" (gh-67048)

* "webbrowser.MacOSX" (gh-86421)

* "classmethod" descriptor chaining (gh-89519)

* "importlib.resources" deprecated methods:

  * "contents()"

  * "is_resource()"

  * "open_binary()"

  * "open_text()"

  * "path()"

  * "read_binary()"

  * "read_text()"

  Use "importlib.resources.files()" instead.  Refer to importlib-
  resources: Migrating from Legacy (gh-106531)
