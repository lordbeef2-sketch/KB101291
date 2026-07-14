# NI_LABVIEW_PYTHON_COMPATIBILITY_AND_INTEGRATION

<!--SYSTEM_CORPUS id=NI_LABVIEW_PYTHON_INTEROP generated=2026-07-14T12:02:18+00:00 -->
- source: https://www.ni.com/en/support/documentation/supplemental/18/installing-python-for-calling-python-code.html
- source_sha256: 6a69ca09bfa43f33149b2afd5eaaac76f352755d2aa539d47c3ec8e09bc93ed9

## NORMALIZED_COMPATIBILITY_MATRIX

| LabVIEW | Supported Python versions |
|---|---|
| 2026 Q1 | 3.12, 3.11, 3.10, 3.9 |
| 2025 Q3 | 3.12, 3.11, 3.10, 3.9 |
| 2025 Q1 | 3.12, 3.11, 3.10, 3.9 |
| 2024 Q3 | 3.10, 3.9, 3.8, 3.7, 3.6 |
| 2024 Q1 | 3.10, 3.9, 3.8, 3.7, 3.6 |

## FULL_SOURCE_TEXT

## Integrating Python Code in LabVIEW

## Overview

You can integrate code developed in Python® from LabVIEW by using the LabVIEW Python functions. The LabVIEW Python Node provides native capability to intuitively call a Python script from a LabVIEW Block Diagram. It uses LabVIEW primitives, providing a way to interoperate between the languages with low latency.

## Contents

- LabVIEW and Python Compatibility

- Installing Python for Calling Python Code

- LabVIEW Python Functions Examples

- Support for Python Virtual Environments

- Additional Resources

Use the following table to determine which version of Python is compatible with your LabVIEW version. Although unsupported versions might work with the LabVIEW Python functions, NI recommends using supported versions of Python only.

Note – this functionality was introduced in LabVIEW 2018 and is not available in previous versions.

Compatible

### Installing Python Shared Libraries

You must install Python to use the LabVIEW Python functions; and to run the Python code, LabVIEW requires the Python shared libraries in the system path. Follow steps for your operating system to add the Python shared libraries to the system path.

Before you begin:

- Use the LabVIEW and Python Compatibility table to determine which supported version of Python to install.

- Ensure that the bitness of Python corresponds to the bitness of LabVIEW installed on the machine.

### Windows

Download and install the Python Interpreter in a compatible version. You can either either use the pure Python Interpreter installation, or a IDE which also installs the Python Interpreter.

LabVIEW will then use registry entries to find the installed python3.x interpreters. Alternatively, use the Python path input of the Open Python Session.vi.

### Linux

Use the package manager of your Linux Distribution to get the Python Interpreter in a compatible version. You can either either use the pure Python Interpreter installation, or a IDE which also installs the Python Interpreter.

LabVIEW search in /bin/python3.x, /usr/local/bin/python3.x and /usr/bin/python3.x for installed python3.x interpreters. Alternatively, use the Python path input of the Open Python Session.vi.

There are multiple examples from LabVIEW that demonstrate how to set up your block diagram and call your Python code.

Examples for using the Python Node are available in the LabVIEW Example Finder (found in Help >> Find Examples...) under Communicating with External Applications >> Using External Code >> Integrating Python Code.

LabVIEW 2023 Q1 and later supports Python Virtual Environments using Open Anaconda 2 and 3 (32 and 64 bit) and Virtual Env. (venv) with the Open Virtual Environment Session function.

- Python Resources for NI Hardware and Software.

- Python Functions – LabVIEW Help

- Calling Python Class Methods Using LabVIEW Python Node

- Introduction to Scripting in Perl, Python and Tcl

Windows® is registered trademarks of Microsoft Corporation in the United States and/or other countries. Python® is a registered trademark of the PSF.

### Was this information helpful?

Yes

No
