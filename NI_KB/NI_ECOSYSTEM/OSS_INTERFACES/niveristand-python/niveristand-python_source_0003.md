# NI OSS SOURCE SNAPSHOT: niveristand-python

<!--NI_OSS_SNAPSHOT repo=ni/niveristand-python commit=9ced536d3414f04a8b6b9315ce4c71b879d02a96 -->

<!--NI_OSS_SOURCE repo=niveristand-python path=LICENSE sha256=431e6e9e2f5c5700455b16c214e06f7a1b821b53bb82a7595108eb1bc4709d99 bytes=1091 -->
## FILE: LICENSE

- repository: `ni/niveristand-python`
- source_path: `LICENSE`
- sha256: `431e6e9e2f5c5700455b16c214e06f7a1b821b53bb82a7595108eb1bc4709d99`
- bytes: 1091

````text
Copyright (c) 2018, National Instruments Corp.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
````

<!--NI_OSS_SOURCE repo=niveristand-python path=MANIFEST.in sha256=b066c2db9cb3b01981299b9f121bc001772872bcbc6ac64b9f9d5a664ef57afd bytes=37 -->
## FILE: MANIFEST.in

- repository: `ni/niveristand-python`
- source_path: `MANIFEST.in`
- sha256: `b066c2db9cb3b01981299b9f121bc001772872bcbc6ac64b9f9d5a664ef57afd`
- bytes: 37

````text
include README.rst
include LICENSE
````

<!--NI_OSS_SOURCE repo=niveristand-python path=README.rst sha256=37e4f4e08fb37debc2758eb09b9c1f3ac856aa09fcfe4d08194552caf6c5c035 bytes=2830 -->
## FILE: README.rst

- repository: `ni/niveristand-python`
- source_path: `README.rst`
- sha256: `37e4f4e08fb37debc2758eb09b9c1f3ac856aa09fcfe4d08194552caf6c5c035`
- bytes: 2830

````rst
===========  ====================================================
Info         VeriStand Python Support
Author       National Instruments
===========  ====================================================

About
=====
The **niveristand** package contains an API (Application Programming Interface) that interacts with VeriStand systems.
The package is implemented in Python. NI created and supports this package.

Requirements
============
**niveristand** requires the following to be installed:

* VeriStand 2021 or later
* CPython 3.8 or later (the standard Python, available on python.org and elsewhere)

.. _installation_section:

Recommended
-----------
NI recommends you use an editor with code completion, such as `Visual Studio Code <https://code.visualstudio.com/docs/languages/python/>`_, to make it easier to browse and use this code.

Installation
============

To install **niveristand**, use one of the following methods:

1. `pip <http://pypi.python.org/pypi/pip>`_::

   $ python -m pip install niveristand

2. **easy_install** from `setuptools <http://pypi.python.org/pypi/setuptools>`_::

   $ python -m easy_install niveristand

3. Download the project source and run the following script::

   $ python setup.py install

.. _usage_section:

Usage
=====
Refer to the `System Definition Examples section <https://niveristand-python.readthedocs.io/en/latest/sysdef_examples.html>`_ for detailed examples of how to script a system definition file.

Refer to the `Basic Real-time Sequence Examples section <https://niveristand-python.readthedocs.io/en/latest/basic_rt_sequence_examples.html>`_
for detailed information on how to write a Python real-time sequence.

.. _support_section:

Support / Feedback
==================

The **niveristand** package is supported by NI. For support for **niveristand**, open
a request through the NI support portal at `ni.com <http://www.ni.com>`_.

Bugs / Feature Requests
=======================

To report a bug or submit a feature request, please use the
`GitHub issues page <https://github.com/ni/niveristand-python/issues>`_.

Documentation
=============

To view the documentation, visit the `VeriStand Python Documentation Page <http://niveristand-python.readthedocs.io>`_.

Additional Documentation
========================

Refer to the `VeriStand Help <http://digital.ni.com/express.nsf/bycode/ex9v46>`_
for detailed information on setting up a system and running real-time test scenarios.

VeriStand Help installs only with the full version of VeriStand.

License
=======

**niveristand** is licensed under an MIT-style license (see `LICENSE
<LICENSE>`_).  Other incorporated projects may be licensed under different
licenses. All licenses allow for non-commercial and commercial use.
````

<!--NI_OSS_SOURCE repo=niveristand-python path=requirements.txt sha256=a86bd2e673a2c9a1f3012332a9bde57c47c83e18dd5a30f4f00ba226de09d242 bytes=39 -->
## FILE: requirements.txt

- repository: `ni/niveristand-python`
- source_path: `requirements.txt`
- sha256: `a86bd2e673a2c9a1f3012332a9bde57c47c83e18dd5a30f4f00ba226de09d242`
- bytes: 39

````text
pytest
pythonnet~=3.0.1
tox
pyyaml
````

<!--NI_OSS_SOURCE repo=niveristand-python path=setup.py sha256=6600575d67d6f4f2e97fba180f1f6e559f9b61bc8c4e59a00192057cde6ccefe bytes=1989 -->
## FILE: setup.py

- repository: `ni/niveristand-python`
- source_path: `setup.py`
- sha256: `6600575d67d6f4f2e97fba180f1f6e559f9b61bc8c4e59a00192057cde6ccefe`
- bytes: 1989

````python
"""Setup module for NI VeriStand."""
from os.path import dirname
from os.path import join
from setuptools import find_packages
from setuptools import setup


pypi_name = "niveristand"


def get_version(name):
    """Calculate a version number."""
    import os

    version = None
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_dir = os.path.join(script_dir, name)
    if not os.path.exists(os.path.join(script_dir, 'VERSION')):
        version = '3.2.3'
    else:
        with open(os.path.join(script_dir, "VERSION"), "r") as version_file:
            version = version_file.read().rstrip()
    return version


def read_contents(file_to_read):
    """Read a file in this folder."""
    with open(join(dirname(__file__), file_to_read), "r") as f:
        return f.read()


setup(
    name=pypi_name,
    version=get_version(pypi_name),
    description="NI VeriStand Python API",
    long_description=read_contents("README.rst"),
    author="National Instruments",
    maintainer="Marcelo Izaguirre",
    maintainer_email="marcelo.izaguirre@ni.com",
    url="https://github.com/ni/niveristand-python",
    keywords=["niveristand", "veristand"],
    license="MIT",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=["pythonnet~=3.0.1", "PyYAML"],
    tests_require=["pytest", "numpy"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Testing",
    ],
    package_data={pypi_name: ["VERSION"]},
)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/__init__.py sha256=02af48e8f68eef525e4bd3be1fa210eff68391d2f0b7dbf187d0720e33e54b7c bytes=510 -->
## FILE: src/niveristand/__init__.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/__init__.py`
- sha256: `02af48e8f68eef525e4bd3be1fa210eff68391d2f0b7dbf187d0720e33e54b7c`
- bytes: 510

````python
from niveristand import _internal  # noqa: F401: loads the .NET dlls for subsequent imports
from niveristand._auto_generated_classes import ErrorCode, VeriStandSdfError, XMLVersionInfo
from niveristand._decorators import nivs_rt_sequence, NivsParam
from niveristand.realtimesequencetools import run_py_as_rtseq, save_py_as_rtseq

__all__ = [
    "ErrorCode",
    "NivsParam",
    "nivs_rt_sequence",
    "run_py_as_rtseq",
    "save_py_as_rtseq",
    "VeriStandSdfError",
    "XMLVersionInfo",
]
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_auto_generated_classes.py sha256=b73a1ee0ed818a674e57fa8a636872b142d65b259f4f507f8ee04aadb8f58b63 bytes=33593 -->
## FILE: src/niveristand/_auto_generated_classes.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_auto_generated_classes.py`
- sha256: `b73a1ee0ed818a674e57fa8a636872b142d65b259f4f507f8ee04aadb8f58b63`
- bytes: 33593

````python
"""Module for NationalInstruments.VeriStand."""
### AUTO-GENERATED CODE - DO NOT MODIFY DIRECTLY ###

from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, Optional, overload, Sequence, Tuple, Union

import clr

clr.AddReference("NationalInstruments.VeriStand")
import NationalInstruments.VeriStand  # type: ignore
import System  # type: ignore


class _staticproperty(staticmethod):
    def __get__(self, *_):
        return self.__func__()


class _DotNetBase:
    def __eq__(self, other) -> bool:
        return self._dotnet_instance == other._dotnet_instance if isinstance(other, _DotNetBase) else False

    def __repr__(self) -> str:
        qualname = type(self).__qualname__
        return f"<niveristand.{qualname}{self._custom_repr()} object at {hex(id(self))}>"

    def _custom_repr(self) -> str:
        return ""


class _DotNetEnum(_DotNetBase):
    def __repr__(self) -> str:
        return f"<niveristand.{type(self).__qualname__}.{self._py_field_name}: {int(self)}>"

    def __str__(self) -> str:
        return f"{type(self).__qualname__}.{self._py_field_name}"

    def __int__(self) -> int:
        return int(self._dotnet_instance)


def _is_iterable(arg: Any) -> bool:
    return not isinstance(arg, str) and isinstance(arg, Iterable)


def _unwrap(out_params: Dict[Optional[Tuple[str, ...]], Tuple[int, Any]], *args: Tuple[Any]) -> Iterable[Any]:
    insertion_index = -1
    if out_params:
        use_out_param = False
        for signature, out_param in out_params.items():
            if not signature:
                use_out_param = True
            elif len(args) == len(signature):
                use_out_param = True
                for arg, sig_type in zip(args, signature):
                    if not isinstance(arg, sig_type):
                        use_out_param = False
                        break
            if use_out_param:
                insertion_index, insertion_value = out_param
                break

    for index, arg in enumerate(args):
        # insert the extra value then continue
        if index == insertion_index:
            yield insertion_value

        if hasattr(arg, "_dotnet_instance"):
            yield arg._dotnet_instance
        elif arg and _is_iterable(arg) and hasattr(next(iter(arg)), "_dotnet_instance"):
            yield [item._dotnet_instance for item in arg]
        else:
            yield arg
    # insert the extra value if at the end
    if len(args) == insertion_index:
        yield insertion_value


_wrap_sentinel_value = object()

def _wrap(one_or_many_args: Union[Any, Tuple[Any]]) -> Union[Any, Tuple[Any]]:
    def _is_ni_type(item: Any):
        return type(item).__module__.startswith("NationalInstruments.")

    def _wrap_dotnet_instance(dotnetitem: Any):
        if type(dotnetitem) != NationalInstruments.VeriStand.Error:
            pytype = eval(type(dotnetitem).__name__)
            return pytype(dotnetitem)
        elif dotnetitem.IsError:
            raise VeriStandSdfError(dotnetitem)
        else:
            return _wrap_sentinel_value

    def _wrap_core(arg: Any) -> Any:
        if _is_iterable(arg):
            first = next(iter(arg), _wrap_sentinel_value)
            if first is _wrap_sentinel_value:
                return []  # empty Python list preferable to an empty .NET list or enumerable
            elif _is_ni_type(first):
                return [_wrap_dotnet_instance(item) for item in arg]
            else:
                return [item for item in arg]
        elif _is_ni_type(arg):
            return _wrap_dotnet_instance(arg)
        elif str(type(arg)) == "<class 'System.Version'>":
            # System.Version uses `Build` as the third element, not the fourth
            return (arg.Major, arg.Minor, arg.Build, arg.Revision)
        return arg

    if isinstance(one_or_many_args, Tuple):
        wrapped = [_wrap_core(x) for x in one_or_many_args]
        result = [x for x in wrapped if x is not _wrap_sentinel_value]
        # if we have two parameters, and one is Error, only return the non-error one
        return result[0] if len(result) == 1 and len(wrapped) == 2 else tuple(result)
    else:
        result = _wrap_core(one_or_many_args)
        return result if result is not _wrap_sentinel_value else None


class VeriStandSdfError(Exception):
    """Represents NI VeriStand error information, including an integer error code and a string error message. Error objects are immutable once created."""

    def __str__(self) -> str:
        # Only use resolved_error_message if necessary; it often returns
        # "Additional error information is not available" before the error
        message = self.message if self.message else self.resolved_error_message
        return f"{int(self.error_code)} ({str(self._dotnet_instance)}): {message}"

    @overload
    def __init__(self, code: int, message: str):
        ...

    @overload
    def __init__(self, code: ErrorCode, message: str):
        ...

    @overload
    def __init__(self, code: int, message: str, resolved_error: str):
        ...

    @overload
    def __init__(self, code: ErrorCode, message: str, resolved_error: str):
        ...

    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, code: int):
        ...

    @overload
    def __init__(self, code: ErrorCode):
        ...

    @overload
    def __init__(self, e: System.Exception):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.Error:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.Error(*unwrapped)

    @property
    def code(self) -> int:
        """Gets the error code for the current instance of <see cref="T:NationalInstruments.VeriStand.Error" /> and returns it as an integer."""
        dotnet_result = self._dotnet_instance.Code
        return _wrap(dotnet_result)

    @property
    def message(self) -> str:
        """Gets the error message and returns it as a string."""
        dotnet_result = self._dotnet_instance.Message
        return _wrap(dotnet_result)

    @property
    def is_error(self) -> bool:
        """Gets a Boolean value indicating whether the <see cref="T:NationalInstruments.VeriStand.Error" /> object contains an error state."""
        dotnet_result = self._dotnet_instance.IsError
        return _wrap(dotnet_result)

    @property
    def resolved_error_message(self) -> str:
        """Gets the resolved error message. The resolved error message provides error information for non-LabVIEW applications."""
        dotnet_result = self._dotnet_instance.ResolvedErrorMessage
        return _wrap(dotnet_result)

    @property
    def is_defined_error_code(self) -> bool:
        """Gets a Boolean value indicating whether or not the integer error code is defined in the <see cref="T:NationalInstruments.VeriStand.ErrorCode" /> enumeration."""
        dotnet_result = self._dotnet_instance.IsDefinedErrorCode
        return _wrap(dotnet_result)

    @property
    def error_code(self) -> ErrorCode:
        """Gets the <see cref="T:NationalInstruments.VeriStand.ErrorCode" /> enumeration for the current <see cref="T:NationalInstruments.VeriStand.Error" />. If the integer error code is not defined in <see cref="T:NationalInstruments.VeriStand.ErrorCode" />, returns the UnexpectedError enumeration."""
        dotnet_result = self._dotnet_instance.ErrorCode
        return _wrap(dotnet_result)

    @overload
    def to_string(self) -> str:
        ...

    def to_string(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ToString(*unwrapped)
        return _wrap(dotnet_result)


class ErrorCode(_DotNetEnum):
    """Defines the types of error codes that NI VeriStand can return."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.ErrorCode:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for ErrorCode")

    @_staticproperty
    def SUCCESS() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "Success")
        return ErrorCode(dotnet_result, "SUCCESS")

    @_staticproperty
    def LAB_VIEW_MATHEMATICS_VI_BRACKET_PROBLEM() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "LabVIEWMathematicsVIBracketProblem")
        return ErrorCode(dotnet_result, "LAB_VIEW_MATHEMATICS_VI_BRACKET_PROBLEM")

    @_staticproperty
    def LAB_VIEW_MATHEMATICS_VI_BEGINNING_BRACKET_PROBLEM() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "LabVIEWMathematicsVIBeginningBracketProblem")
        return ErrorCode(dotnet_result, "LAB_VIEW_MATHEMATICS_VI_BEGINNING_BRACKET_PROBLEM")

    @_staticproperty
    def LAB_VIEW_MATHEMATICS_VI_END_BRACKET_PROBLEM() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "LabVIEWMathematicsVIEndBracketProblem")
        return ErrorCode(dotnet_result, "LAB_VIEW_MATHEMATICS_VI_END_BRACKET_PROBLEM")

    @_staticproperty
    def FILE_VERSION_UNSUPPORTED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "FileVersionUnsupported")
        return ErrorCode(dotnet_result, "FILE_VERSION_UNSUPPORTED")

    @_staticproperty
    def SERVICE_CONFIGURATION_FILE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ServiceConfigurationFile")
        return ErrorCode(dotnet_result, "SERVICE_CONFIGURATION_FILE")

    @_staticproperty
    def UNEXPECTED_ERROR() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "UnexpectedError")
        return ErrorCode(dotnet_result, "UNEXPECTED_ERROR")

    @_staticproperty
    def FUNCTION_NOT_SUPPORTED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "FunctionNotSupported")
        return ErrorCode(dotnet_result, "FUNCTION_NOT_SUPPORTED")

    @_staticproperty
    def FAILED_SERVER_CONNECTION() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "FailedServerConnection")
        return ErrorCode(dotnet_result, "FAILED_SERVER_CONNECTION")

    @_staticproperty
    def INVALID_FILE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "InvalidFile")
        return ErrorCode(dotnet_result, "INVALID_FILE")

    @_staticproperty
    def NOT_DEPLOYED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NotDeployed")
        return ErrorCode(dotnet_result, "NOT_DEPLOYED")

    @_staticproperty
    def COMPONENT_NOT_AVAILABLE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ComponentNotAvailable")
        return ErrorCode(dotnet_result, "COMPONENT_NOT_AVAILABLE")

    @_staticproperty
    def NO_SYSTEM_DEFINITION_LOADED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NoSystemDefinitionLoaded")
        return ErrorCode(dotnet_result, "NO_SYSTEM_DEFINITION_LOADED")

    @_staticproperty
    def INVALID_CONFIGURATION_PASSWORD() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "InvalidConfigurationPassword")
        return ErrorCode(dotnet_result, "INVALID_CONFIGURATION_PASSWORD")

    @_staticproperty
    def HOST_RUNNING_DIFFERENT_SYSTEM_DEFINITION() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "HostRunningDifferentSystemDefinition")
        return ErrorCode(dotnet_result, "HOST_RUNNING_DIFFERENT_SYSTEM_DEFINITION")

    @_staticproperty
    def SYSTEM_DEFINITION_ALREADY_ACTIVE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "SystemDefinitionAlreadyActive")
        return ErrorCode(dotnet_result, "SYSTEM_DEFINITION_ALREADY_ACTIVE")

    @_staticproperty
    def EMPTY_PASSWORD() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "EmptyPassword")
        return ErrorCode(dotnet_result, "EMPTY_PASSWORD")

    @_staticproperty
    def SYSTEM_DEFINITION_DEPLOYMENT_TIMEOUT() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "SystemDefinitionDeploymentTimeout")
        return ErrorCode(dotnet_result, "SYSTEM_DEFINITION_DEPLOYMENT_TIMEOUT")

    @_staticproperty
    def SYSTEM_DEFINITION_DEPLOYMENT_FAILURE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "SystemDefinitionDeploymentFailure")
        return ErrorCode(dotnet_result, "SYSTEM_DEFINITION_DEPLOYMENT_FAILURE")

    @_staticproperty
    def NODE_NOT_FOUND() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NodeNotFound")
        return ErrorCode(dotnet_result, "NODE_NOT_FOUND")

    @_staticproperty
    def TIMEOUT() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "Timeout")
        return ErrorCode(dotnet_result, "TIMEOUT")

    @_staticproperty
    def CHANNEL_NOT_READABLE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ChannelNotReadable")
        return ErrorCode(dotnet_result, "CHANNEL_NOT_READABLE")

    @_staticproperty
    def CHANNEL_NOT_WRITABLE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ChannelNotWritable")
        return ErrorCode(dotnet_result, "CHANNEL_NOT_WRITABLE")

    @_staticproperty
    def CHANNEL_CANNOT_BE_FAULTED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ChannelCannotBeFaulted")
        return ErrorCode(dotnet_result, "CHANNEL_CANNOT_BE_FAULTED")

    @_staticproperty
    def TARGET_INVALID() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "TargetInvalid")
        return ErrorCode(dotnet_result, "TARGET_INVALID")

    @_staticproperty
    def TARGET_DISABLED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "TargetDisabled")
        return ErrorCode(dotnet_result, "TARGET_DISABLED")

    @_staticproperty
    def MODEL_DIMENSION_MISMATCH() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ModelDimensionMismatch")
        return ErrorCode(dotnet_result, "MODEL_DIMENSION_MISMATCH")

    @_staticproperty
    def CHANNEL_MAPPINGS_SIZE_MISMATCH() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ChannelMappingsSizeMismatch")
        return ErrorCode(dotnet_result, "CHANNEL_MAPPINGS_SIZE_MISMATCH")

    @_staticproperty
    def NOT_A_CHANNEL() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NotAChannel")
        return ErrorCode(dotnet_result, "NOT_A_CHANNEL")

    @_staticproperty
    def NOT_A_WAVEFORM() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NotAWaveform")
        return ErrorCode(dotnet_result, "NOT_A_WAVEFORM")

    @_staticproperty
    def WAVEFORM_DATA_TYPE_MISMATCH() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "WaveformDataTypeMismatch")
        return ErrorCode(dotnet_result, "WAVEFORM_DATA_TYPE_MISMATCH")

    @_staticproperty
    def INVALID_STREAM_CONDITION_FOR_DATA_TYPE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "InvalidStreamConditionForDataType")
        return ErrorCode(dotnet_result, "INVALID_STREAM_CONDITION_FOR_DATA_TYPE")

    @_staticproperty
    def CHANNEL_NODE_REMOVED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ChannelNodeRemoved")
        return ErrorCode(dotnet_result, "CHANNEL_NODE_REMOVED")

    @_staticproperty
    def NODE_NOT_FOUND_DURING_COMPILE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NodeNotFoundDuringCompile")
        return ErrorCode(dotnet_result, "NODE_NOT_FOUND_DURING_COMPILE")

    @_staticproperty
    def CHANNEL_LENGTH_MISMATCH() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ChannelLengthMismatch")
        return ErrorCode(dotnet_result, "CHANNEL_LENGTH_MISMATCH")

    @_staticproperty
    def CHANNEL_NOT_SCALABLE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ChannelNotScalable")
        return ErrorCode(dotnet_result, "CHANNEL_NOT_SCALABLE")

    @_staticproperty
    def NO_PROJECT_OPEN() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NoProjectOpen")
        return ErrorCode(dotnet_result, "NO_PROJECT_OPEN")

    @_staticproperty
    def STIMULUS_PROFILE_SESSION_LOCKED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "StimulusProfileSessionLocked")
        return ErrorCode(dotnet_result, "STIMULUS_PROFILE_SESSION_LOCKED")

    @_staticproperty
    def SEQUENCE_NOT_FOUND_IN_SESSION() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "SequenceNotFoundInSession")
        return ErrorCode(dotnet_result, "SEQUENCE_NOT_FOUND_IN_SESSION")

    @_staticproperty
    def SESSION_NOT_DEPLOYED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "SessionNotDeployed")
        return ErrorCode(dotnet_result, "SESSION_NOT_DEPLOYED")

    @_staticproperty
    def SESSION_ALREADY_DEPLOYED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "SessionAlreadyDeployed")
        return ErrorCode(dotnet_result, "SESSION_ALREADY_DEPLOYED")

    @_staticproperty
    def RTSEQ_PARAMETER_ASSIGNMENT_PARAMETER_DOES_NOT_EXIST() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "RtseqParameterAssignmentParameterDoesNotExist")
        return ErrorCode(dotnet_result, "RTSEQ_PARAMETER_ASSIGNMENT_PARAMETER_DOES_NOT_EXIST")

    @_staticproperty
    def BY_REFERENCE_PARAMETER_VALUE_NOT_ASSIGNED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ByReferenceParameterValueNotAssigned")
        return ErrorCode(dotnet_result, "BY_REFERENCE_PARAMETER_VALUE_NOT_ASSIGNED")

    @_staticproperty
    def SEQUENCE_COMPILE_ERROR() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "SequenceCompileError")
        return ErrorCode(dotnet_result, "SEQUENCE_COMPILE_ERROR")

    @_staticproperty
    def RTSEQ_PARAMETER_ASSIGNMENT_INVALID_DATA_TYPE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "RtseqParameterAssignmentInvalidDataType")
        return ErrorCode(dotnet_result, "RTSEQ_PARAMETER_ASSIGNMENT_INVALID_DATA_TYPE")

    @_staticproperty
    def MODEL_PARAMETER_FILE_PARSE_ERROR() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ModelParameterFileParseError")
        return ErrorCode(dotnet_result, "MODEL_PARAMETER_FILE_PARSE_ERROR")

    @_staticproperty
    def NUMBER_OF_COEFFICIENTS_OUT_OF_RANGE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NumberOfCoefficientsOutOfRange")
        return ErrorCode(dotnet_result, "NUMBER_OF_COEFFICIENTS_OUT_OF_RANGE")

    @_staticproperty
    def DUPLICATE_LOG_SESSION_NAME() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "DuplicateLogSessionName")
        return ErrorCode(dotnet_result, "DUPLICATE_LOG_SESSION_NAME")

    @_staticproperty
    def LOG_SESSION_NOT_FOUND() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "LogSessionNotFound")
        return ErrorCode(dotnet_result, "LOG_SESSION_NOT_FOUND")

    @_staticproperty
    def NOT_ENOUGH_DYNAMIC_DATA_SHARING_SPACE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NotEnoughDynamicDataSharingSpace")
        return ErrorCode(dotnet_result, "NOT_ENOUGH_DYNAMIC_DATA_SHARING_SPACE")

    @_staticproperty
    def TARGET_MISSING_DATA_SHARING_DEVICE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "TargetMissingDataSharingDevice")
        return ErrorCode(dotnet_result, "TARGET_MISSING_DATA_SHARING_DEVICE")

    @_staticproperty
    def LOG_TRIGGER_CONDITION_SYNTAX_ERROR() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "LogTriggerConditionSyntaxError")
        return ErrorCode(dotnet_result, "LOG_TRIGGER_CONDITION_SYNTAX_ERROR")

    @_staticproperty
    def SERVER_PORT_ALREADY_IN_USE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ServerPortAlreadyInUse")
        return ErrorCode(dotnet_result, "SERVER_PORT_ALREADY_IN_USE")

    @_staticproperty
    def NOT_AN_INLINE_CUSTOM_DEVICE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NotAnInlineCustomDevice")
        return ErrorCode(dotnet_result, "NOT_AN_INLINE_CUSTOM_DEVICE")

    @_staticproperty
    def PARAMETER_NOT_FOUND() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ParameterNotFound")
        return ErrorCode(dotnet_result, "PARAMETER_NOT_FOUND")

    @_staticproperty
    def INVALID_DAQ_PLUGIN_FILE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "InvalidDaqPluginFile")
        return ErrorCode(dotnet_result, "INVALID_DAQ_PLUGIN_FILE")

    @_staticproperty
    def DUPLICATE_CHANNEL_ALIAS_MAPPINGS() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "DuplicateChannelAliasMappings")
        return ErrorCode(dotnet_result, "DUPLICATE_CHANNEL_ALIAS_MAPPINGS")

    @_staticproperty
    def MISMATCHED_LENGTHS() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "MismatchedLengths")
        return ErrorCode(dotnet_result, "MISMATCHED_LENGTHS")

    @_staticproperty
    def INCOMPATIBLE_MODEL() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "IncompatibleModel")
        return ErrorCode(dotnet_result, "INCOMPATIBLE_MODEL")

    @_staticproperty
    def UNSUPPORTED_MODEL_ARCHITECTURE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "UnsupportedModelArchitecture")
        return ErrorCode(dotnet_result, "UNSUPPORTED_MODEL_ARCHITECTURE")

    @_staticproperty
    def UNSUPPORTED_FMU_KIND() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "UnsupportedFMUKind")
        return ErrorCode(dotnet_result, "UNSUPPORTED_FMU_KIND")

    @_staticproperty
    def NON_POSITIVE_STEP_SIZE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NonPositiveStepSize")
        return ErrorCode(dotnet_result, "NON_POSITIVE_STEP_SIZE")

    @_staticproperty
    def UNSUPPORTED_FMI_VERSION() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "UnsupportedFMIVersion")
        return ErrorCode(dotnet_result, "UNSUPPORTED_FMI_VERSION")

    @_staticproperty
    def UNSUPPORTED_VS_MODEL_VERSION() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "UnsupportedVsModelVersion")
        return ErrorCode(dotnet_result, "UNSUPPORTED_VS_MODEL_VERSION")

    @_staticproperty
    def UNMAPPED_ALIAS() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "UnmappedAlias")
        return ErrorCode(dotnet_result, "UNMAPPED_ALIAS")

    @_staticproperty
    def CANNOT_ADD_VS_MODEL_IN_SYSTEM_EXPLORER() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "CannotAddVsModelInSystemExplorer")
        return ErrorCode(dotnet_result, "CANNOT_ADD_VS_MODEL_IN_SYSTEM_EXPLORER")

    @_staticproperty
    def CANNOT_ADD_NI_VS_ECU_NW_IN_SYSTEM_EXPLORER() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "CannotAddNiVsEcuNwInSystemExplorer")
        return ErrorCode(dotnet_result, "CANNOT_ADD_NI_VS_ECU_NW_IN_SYSTEM_EXPLORER")

    @_staticproperty
    def EMPTY_NODE_NAME() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "EmptyNodeName")
        return ErrorCode(dotnet_result, "EMPTY_NODE_NAME")

    @_staticproperty
    def NODE_ALREADY_EXISTS_BY_NAME() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NodeAlreadyExistsByName")
        return ErrorCode(dotnet_result, "NODE_ALREADY_EXISTS_BY_NAME")

    @_staticproperty
    def INPUT_PARAMETER_INVALID() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "InputParameterInvalid")
        return ErrorCode(dotnet_result, "INPUT_PARAMETER_INVALID")

    @_staticproperty
    def NO_ACTION_REQUIRED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NoActionRequired")
        return ErrorCode(dotnet_result, "NO_ACTION_REQUIRED")

    @_staticproperty
    def INCORRECT_LOG_FILE_NAME() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "IncorrectLogFileName")
        return ErrorCode(dotnet_result, "INCORRECT_LOG_FILE_NAME")

    @_staticproperty
    def DOWNLOAD_FILE_ERROR() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "DownloadFileError")
        return ErrorCode(dotnet_result, "DOWNLOAD_FILE_ERROR")

    @_staticproperty
    def TARGET_DISCONNECTED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "TargetDisconnected")
        return ErrorCode(dotnet_result, "TARGET_DISCONNECTED")

    @_staticproperty
    def GATEWAY_NOT_ON_LOCALHOST() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "GatewayNotOnLocalhost")
        return ErrorCode(dotnet_result, "GATEWAY_NOT_ON_LOCALHOST")

    @_staticproperty
    def CHANNEL_GROUP_NOT_FOUND_IN_LOG_FILE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ChannelGroupNotFoundInLogFile")
        return ErrorCode(dotnet_result, "CHANNEL_GROUP_NOT_FOUND_IN_LOG_FILE")

    @_staticproperty
    def CHANNEL_NOT_FOUND_IN_LOG_FILE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ChannelNotFoundInLogFile")
        return ErrorCode(dotnet_result, "CHANNEL_NOT_FOUND_IN_LOG_FILE")

    @_staticproperty
    def DEPENDENCIES_CYCLE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "DependenciesCycle")
        return ErrorCode(dotnet_result, "DEPENDENCIES_CYCLE")

    @_staticproperty
    def STI_FILE_ERROR() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "STIFileError")
        return ErrorCode(dotnet_result, "STI_FILE_ERROR")

    @_staticproperty
    def SLSC_CHASSIS_LOAD_FAILED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "SLSCChassisLoadFailed")
        return ErrorCode(dotnet_result, "SLSC_CHASSIS_LOAD_FAILED")

    @_staticproperty
    def ELECTRICAL_ERROR_NOT_HANDLED() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ElectricalErrorNotHandled")
        return ErrorCode(dotnet_result, "ELECTRICAL_ERROR_NOT_HANDLED")

    @_staticproperty
    def MODEL_NOT_FOUND() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "ModelNotFound")
        return ErrorCode(dotnet_result, "MODEL_NOT_FOUND")

    @_staticproperty
    def INVALID_SIGNAL_INDEX() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "InvalidSignalIndex")
        return ErrorCode(dotnet_result, "INVALID_SIGNAL_INDEX")

    @_staticproperty
    def NOT_SCALAR_SIGNAL() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NotScalarSignal")
        return ErrorCode(dotnet_result, "NOT_SCALAR_SIGNAL")

    @_staticproperty
    def TARGET_RUNNING_CONNECTED_TO_A_DIFFERENT_GATEWAY() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "TargetRunningConnectedToADifferentGateway")
        return ErrorCode(dotnet_result, "TARGET_RUNNING_CONNECTED_TO_A_DIFFERENT_GATEWAY")

    @_staticproperty
    def NO_SPACE_TO_DEPLOY_SEQUENCE() -> ErrorCode:
        dotnet_result = getattr(NationalInstruments.VeriStand.ErrorCode, "NoSpaceToDeploySequence")
        return ErrorCode(dotnet_result, "NO_SPACE_TO_DEPLOY_SEQUENCE")


class XMLVersionInfo(_DotNetBase):
    """Provides and configures version data for an XML file, including the major, minor, fix, and build version of the XML file."""

    @overload
    def __init__(self, major: int, minor: int, fix: int, build: int):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.XMLVersionInfo:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.XMLVersionInfo(*unwrapped)

    @property
    def major(self) -> int:
        """Gets or sets the major version number for the current XML file."""
        dotnet_result = self._dotnet_instance.Major
        return _wrap(dotnet_result)

    @major.setter
    def major(self, value: int):
        """Gets or sets the major version number for the current XML file."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Major = next(unwrapped)

    @property
    def minor(self) -> int:
        """Gets or sets the minor version number for the current XML file."""
        dotnet_result = self._dotnet_instance.Minor
        return _wrap(dotnet_result)

    @minor.setter
    def minor(self, value: int):
        """Gets or sets the minor version number for the current XML file."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Minor = next(unwrapped)

    @property
    def fix(self) -> int:
        """Gets or sets the fix number for the current XML file."""
        dotnet_result = self._dotnet_instance.Fix
        return _wrap(dotnet_result)

    @fix.setter
    def fix(self, value: int):
        """Gets or sets the fix number for the current XML file."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Fix = next(unwrapped)

    @property
    def build(self) -> int:
        """Gets or sets the build number for the current XML file."""
        dotnet_result = self._dotnet_instance.Build
        return _wrap(dotnet_result)

    @build.setter
    def build(self, value: int):
        """Gets or sets the build number for the current XML file."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Build = next(unwrapped)

    @overload
    def to_string(self) -> str:
        ...

    def to_string(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ToString(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def equals(self, obj: Any) -> bool:
        ...

    @overload
    def equals(self, other: XMLVersionInfo) -> bool:
        ...

    def equals(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Equals(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_hash_code(self) -> int:
        ...

    def get_hash_code(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetHashCode(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def clone(self) -> Any:
        ...

    def clone(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Clone(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def compare_to(self, other: Any) -> int:
        ...

    @overload
    def compare_to(self, other: XMLVersionInfo) -> int:
        ...

    def compare_to(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CompareTo(*unwrapped)
        return _wrap(dotnet_result)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_decorators.py sha256=f4a6f9c95097ea5a92987d41d1232c8c10a3a203b4faf29f42334e85ad7b3d59 bytes=5442 -->
## FILE: src/niveristand/_decorators.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_decorators.py`
- sha256: `f4a6f9c95097ea5a92987d41d1232c8c10a3a203b4faf29f42334e85ad7b3d59`
- bytes: 5442

````python
from functools import wraps
import inspect
from niveristand import _errormessages, errors
from niveristand.clientapi._datatypes import DataType
from niveristand.clientapi._datatypes import rtprimitives

rt_seq_mode_id = "__rtseq_mode__"


def nivs_rt_sequence(func):
    from niveristand.library._tasks import get_scheduler, nivs_yield

    @wraps(func)
    def ret_func(*args, **kwargs):
        is_top_level = False
        this_task = get_scheduler().try_get_task_for_curr_thread()
        if this_task is None:
            is_top_level = True
            this_task = get_scheduler().create_and_register_task_for_top_level()
            get_scheduler().sched()
            this_task.wait_for_turn()
        try:
            if is_top_level:
                from niveristand.clientapi import RealTimeSequence

                RealTimeSequence(func)
            retval = func(*args, **kwargs)
        except errors.SequenceError:
            # generate error already saved this error in the task, so we can just pass.
            pass
        finally:
            if is_top_level:
                this_task.mark_stopped()
                this_task.iteration_counter.finished = True
                nivs_yield()
                if this_task.error and this_task.error.should_raise:
                    raise errors.RunError.RunErrorFactory(this_task.error)
        return retval

    _set_rtseq_attrs(func, ret_func)
    return ret_func


class NivsParam:
    """
    Describes a parameter passed down to a function.

    Args:
        param_name(str): Name of the parameter as it is found in the function definition.
        default_elem: Default value and type. Refer to :ref:`api_datatypes_page` for valid values.
        by_value(bool): Specifies whether to pass a parameter by value or by reference. Set to True to pass by value.
                        Set to False to pass by reference.
                        Refer to :any:`NivsParam.BY_REF` or :any:`NivsParam.BY_VALUE` for details.

    """

    BY_REF = (
        False  #: Passes a parameter by reference. Allows the called function to modify the value.
    )
    BY_VALUE = True  #: Passes a parameter by value. Creates a copy of the caller's value for use inside the function.

    def __init__(self, param_name, default_elem, by_value):
        self.param_name = param_name
        self.default_elem = default_elem
        self.by_value = by_value

    def __call__(self, func):
        @wraps(func)
        def ret_func(*args, **kwargs):
            args = _reconstruct_args(func, args, self)
            return func(*args, **kwargs)

        _set_rtseq_attrs(func, ret_func)
        return ret_func


def _set_rtseq_attrs(func, ret_func):
    wrapped = getattr(func, rt_seq_mode_id, None)
    if wrapped is None:
        wrapped = func
        setattr(func, rt_seq_mode_id, wrapped)
    setattr(ret_func, rt_seq_mode_id, wrapped)


def _reconstruct_args(f, args, new_param):
    real_func = getattr(f, rt_seq_mode_id, f)
    new_args = list(args)
    arg_spec = inspect.signature(real_func).parameters

    if new_param is not None:
        if new_param.param_name in arg_spec.keys():
            idx = list(arg_spec.keys()).index(new_param.param_name)
            datatype_name = new_param.default_elem.__class__.__name__
            datatype = rtprimitives.get_class_by_name(datatype_name)
            if new_param.by_value:
                if isinstance(args[idx], DataType):
                    value = args[idx].value
                else:
                    value = args[idx]
                new_args[idx] = datatype(value)
            else:
                if not isinstance(args[idx], DataType):
                    value = args[idx]
                    new_args[idx] = datatype(value)
        else:
            raise errors.VeristandError(_errormessages.param_description_no_param)

    return tuple(new_args)


def task(mt):
    """
    Marks a nested function-definition as a task inside a :func:`niveristand.library.multitask`.

    Args:
        mt: the parent :func:`niveristand.library.multitask`

    Use this function as a decorator.
    Refer to :func:`niveristand.library.multitask` for more details on using tasks.

    """

    def _add_task_to_list(func):
        from niveristand.library._tasks import nivs_yield

        @wraps(func)
        def _internal_task(task_info):
            # all tasks start waiting for their turn from the scheduler.
            task_info.wait_for_turn()
            try:
                return func()
            except (errors._StopTaskException, errors.SequenceError):
                pass
            finally:
                # if the task was stopped or it finished execution mark it stopped, then yield.
                # It won't get scheduled again, and the thread will be marked finished.
                task_info.mark_stopped()
                nivs_yield()

        mt.add_func(_internal_task)
        # return the original function, since we already added the wrapped one to the mt.
        # this allows the user to call it normally if they choose outside an mt context.
        return func

    return _add_task_to_list


_VALID_DECORATORS = {
    nivs_rt_sequence.__name__: nivs_rt_sequence,
    NivsParam.__name__: NivsParam,
    task.__name__: task,
}
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_errormessages.py sha256=7f44d1baa28f7a6b8bc0a2e3ec14dbe881afc7766e5e538e512af0fa34f3a9bd bytes=4621 -->
## FILE: src/niveristand/_errormessages.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_errormessages.py`
- sha256: `7f44d1baa28f7a6b8bc0a2e3ec14dbe881afc7766e5e538e512af0fa34f3a9bd`
- bytes: 4621

````python
init_var_invalid_type = "Variables must be initialized with a valid VeriStand datatype."
invalid_nested_funcdef = "Nested function definitions are only allowed inside a multitask."
invalid_top_level_func = "Invalid top level function."
save_without_valid_sequence = "No valid real-time sequence to save."
invalid_type_for_operator = "This operator doesn't support the given type."
name_constant_not_supported = "This named constant is not supported."
constant_not_supported = "This constant is not supported."
invalid_return_type = "Invalid return type."
invalid_return_value = "Return statement uses undeclared value."
invalid_type_to_convert = "Invalid conversion between types."
dependency_not_found = "Dependency not found."
invalid_type_for_channel_ref = "Channel references do not support the given type."
unsupported_orelse_while = "While loops do not support else blocks."
return_unsupported_unless_last = (
    "A function can only have a single return statement "
    "and it has to be the last line of the function."
)
break_unsupported = "Loops do not support break statements."
variable_reassignment = "Redefining a variable is not allowed."
cannot_change_array_elements = (
    "To assign values to an existing array element, "
    "you must use the value property of the object."
)
param_description_no_param = "The parameter specified in this definition does not exist."
invalid_function_definition = "Unsupported element in function definition."
invalid_param_decorator = "Parameter description decorator doesn't follow parameter rules."
unexpected_argument_redefine = "Unexpected argument added to list."
invalid_nivs_yield = "nivs_yield can only be used as a stand-alone statement."
invalid_with_block = "with statement can only be used inside multitask block."
for_else_not_supported = "for loops do not support else statements."
invalid_iterable_collection = "The iterable collection can only be a variable or a range(end)."
invalid_for_loop_iterator = "The iterator variable is not valid."
invalid_range_call = "range() can only be called with one parameter, the end value."
scalar_iterable_collection = "A for loop can only iterate on ArrayType."
invalid_stmt_after_try = "Invalid statement after try block. Only return statements are allowed."
try_must_be_first_stmt = "try must be the first statement in the function definition."
invalid_try_except_orelse = "try blocks do not support orelse or except blocks."
return_not_supported_in_try_finally = "return statement not supported inside a try/finally block."
try_only_in_top_level_func = (
    "The use of try is not allowed in this context. "
    "Use try/finally only as the first block in the top-level function."
)
invalid_taskname_for_stop_task = "The task name is invalid."
unregistered_thread = "Unregistered thread found."
reregister_thread = "Thread tried to register twice."
ref_param_not_ref = "A parameter marked as pass by reference was not of valid object type."
invalid_error_code_for_generate_error = (
    "Invalid error code provided. Provide an integer number as an error code."
)
invalid_message_for_generate_error = "Invalid error message provided. Provide a string message."
invalid_action_for_generate_error = (
    "Invalid error action provided. Provide an error action from ErrorAction enum."
)
unknown_identifier = "Undefined identifier '%s' found."
run_without_valid_sequence = "Invalid rtseq."
invalid_path_for_sequence = "Invalid real-time sequence path."
run_aborted = "The real-time sequence was stopped or aborted during run."
run_failed = "The real-time sequence failed."
csharp_call_failed = "The call into the C# API failed with error code %d. Message: %s."
channel_not_found = "A channel with name %s could not be found."
multiple_return_statements = "A function can only have a single return statement."
none_not_supported = "NoneType not supported."
invalid_decorator = "Custom decorators are not allowed."
cascaded_comparison_operators_not_allowed = (
    "You cannot use cascading comparison operators. " "Only use one comparison operator at a time."
)
invalid_operand_for_boolean_operator = "Logical operators only accept boolean values."
invalid_type_for_if_test = "If statements only allow for boolean checks."
invalid_operand_for_unary_invert_operator = (
    "The unary inversion operator (~) only accepts integer values."
)
negative_operand_for_binary_operator = (
    "You cannot use a negative number to the right of an arithmetic shift operation."
)
unexpected_dot_net_data_type = "Expecting a .net instance of type %s"
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_internal.py sha256=4226fe6f056992238a670196e6b3cf0e836ecd4de393b77a3f7f8f7c16a20606 bytes=2788 -->
## FILE: src/niveristand/_internal.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_internal.py`
- sha256: `4226fe6f056992238a670196e6b3cf0e836ecd4de393b77a3f7f8f7c16a20606`
- bytes: 2788

````python
import os
import tempfile
import clr


def base_assembly_path():
    try:
        return _getdevconfig()["BaseBinariesPath"]
    except (IOError, KeyError):
        pass
    try:
        return _get_install_path()
    except IOError:
        return ""


def _get_install_path():
    import winreg

    with winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Wow6432Node\\National Instruments\\VeriStand\\"
    ) as vskey:
        r = winreg.QueryInfoKey(vskey)
        ver = "0"
        for k in range(r[0]):
            with winreg.OpenKey(vskey, winreg.EnumKey(vskey, k)) as this_key:
                this_ver = winreg.QueryValueEx(this_key, "Version")[0]
                if this_ver > ver:
                    latest_dir = winreg.QueryValueEx(this_key, "InstallDir")[0]
                    ver = this_ver
    return latest_dir if latest_dir is not None else ""


def _getdevconfig():
    import json

    cfgfile = os.environ["vsdev.json"]
    cfgfile = cfgfile.strip('"')
    with open(os.path.normpath(cfgfile), "r") as f:
        cfg = json.load(f)
    return cfg


clr.AddReference("System")
clr.AddReference("System.IO")
from System.IO import (  # noqa: E402, I202 .net imports can't be at top of file.
    FileNotFoundException,
)

try:
    # Try loading from the GAC first, dev/install folders second.
    clr.AddReference("NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi")
    clr.AddReference("NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities")
    clr.AddReference("NationalInstruments.VeriStand.DataTypes")
    clr.AddReference("NationalInstruments.VeriStand.ClientAPI")
except FileNotFoundException:
    try:
        from sys import path

        path.append(base_assembly_path())
        clr.AddReference("NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi")
        clr.AddReference("NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities")
        clr.AddReference("NationalInstruments.VeriStand.DataTypes")
        clr.AddReference("NationalInstruments.VeriStand.ClientAPI")
    except FileNotFoundException as e:
        raise IOError(e.Message)


def dummy():
    """
    Do nothing because you're just a dummy.

    This dummy can be used by any module that imports internal to get rid of PEP8 errors about
    an import not being used. This internal module takes care of loading C# references, so most
    times it will only be imported but not actually used.
    """
    pass


# set the temporary folder to C:\Users\$USER\AppData\Local\Temp\python_rt_sequences
tempfile.tempdir = os.path.join(tempfile.gettempdir(), "python_rt_sequences")
if not os.path.exists(tempfile.tempdir):
    os.makedirs(tempfile.tempdir)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/__init__.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: src/niveristand/_translation/__init__.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/__init__.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/custom_action_symbols.py sha256=c5d85215a718a444043eb1e2a3df4b4e45a93e61fdc57367ae12e9cc0c42cfb1 bytes=780 -->
## FILE: src/niveristand/_translation/custom_action_symbols.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/custom_action_symbols.py`
- sha256: `c5d85215a718a444043eb1e2a3df4b4e45a93e61fdc57367ae12e9cc0c42cfb1`
- bytes: 780

````python
from niveristand._translation.py2rtseq import custom_generate_error
from niveristand._translation.py2rtseq import custom_localhost_wait
from niveristand._translation.py2rtseq import custom_math_log
from niveristand._translation.py2rtseq import custom_nivs_yield
from niveristand._translation.py2rtseq import custom_stop_task

"""Custom Action Symbols dictionary

Left-side: python symbol
Right-side: the function to call to process this symbol
"""
_custom_action_symbols = {
    "nivs_yield": custom_nivs_yield.custom_nivs_yield,
    "log": custom_math_log.custom_math_log,
    "localhost_wait": custom_localhost_wait.custom_localhost_wait,
    "stop_task": custom_stop_task.custom_stop_task,
    "generate_error": custom_generate_error.custom_generate_error,
}
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/__init__.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: src/niveristand/_translation/py2rtseq/__init__.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/__init__.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/assign_transformer.py sha256=e4e2d0fcd6970816cd8e68904c02d3f1eed5f06f3be1ce2aa458b5106c8481da bytes=3249 -->
## FILE: src/niveristand/_translation/py2rtseq/assign_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/assign_transformer.py`
- sha256: `e4e2d0fcd6970816cd8e68904c02d3f1eed5f06f3be1ce2aa458b5106c8481da`
- bytes: 3249

````python
import ast
from niveristand import _errormessages
from niveristand._translation import utils
from niveristand.clientapi import _datatypes, realtimesequencedefinition as rtseqapi
from niveristand.errors import TranslateError


def assign_transformer(node, resources):
    node_value = None
    initial_channel_ref_declaration = False
    lhs = node.targets[0]
    rtseq_var_name = utils.generic_ast_node_transform(lhs, resources)
    # the left hand side can only be a variable name or a name with an attribute (var.value)
    if isinstance(lhs, ast.Name):
        variable_name = utils.get_variable_name_from_node(lhs)
        # if the variable already exists this kind of assignment is invalid, use var.value instead
        if resources.has_variable(variable_name):
            raise TranslateError(_errormessages.variable_reassignment)
    elif isinstance(lhs, ast.Attribute):
        # in case of var[0].value get rid of the [0] part and search in the dictionary for var
        stripped_rtseq_var_name = (
            rtseq_var_name[: rtseq_var_name.find("[")]
            if rtseq_var_name.find("[") != -1
            else rtseq_var_name
        )
        variable_name = resources.get_variable_py_name(stripped_rtseq_var_name)
    else:
        raise TranslateError(_errormessages.variable_reassignment)
    rtseq = resources.get_rtseq()
    block = resources.get_current_block()
    if not resources.has_variable(variable_name):
        # new local variable
        node_value = utils.get_value_from_node(node.value, resources)
        if isinstance(node_value, (_datatypes.ChannelReference, _datatypes.VectorChannelReference)):
            initial_channel_ref_declaration = True
            channel_name = utils.get_channel_name(node.value.args[0])
            rtseq_var_name = rtseqapi.to_channel_ref_name(variable_name)
            resources.add_channel_ref(
                variable_name,
                channel_name,
                rtseq_var_name,
                isinstance(node_value, _datatypes.ArrayType),
            )
        elif isinstance(node_value, _datatypes.DataType):
            rtseq_var_name = rtseqapi.add_local_variable(rtseq, variable_name, node_value)
            # add the local variable's accessor to the resources
            resources.add_variable(variable_name, node_value, rtseq_var_name)
            resources.add_variable(variable_name + ".value", node_value, rtseq_var_name)
        else:
            raise TranslateError(_errormessages.init_var_invalid_type)
    transformed_node_value = utils.generic_ast_node_transform(node.value, resources)
    rtseq_var_name = (
        resources.get_variable_rtseq_name(variable_name) if not rtseq_var_name else rtseq_var_name
    )
    if not initial_channel_ref_declaration:
        if isinstance(node_value, _datatypes.ArrayType):
            if transformed_node_value.count(",") > 0:
                value_list = transformed_node_value.split(",")
                for index, val in enumerate(value_list):
                    rtseqapi.add_assignment(block, rtseq_var_name + "[" + str(index) + "]", val)
        else:
            rtseqapi.add_assignment(block, rtseq_var_name, transformed_node_value)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/attribute_transformer.py sha256=d8733b4b6295985bfb3c9151b9208ce52e1a430730c7207f8c95dc513c44626e bytes=1074 -->
## FILE: src/niveristand/_translation/py2rtseq/attribute_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/attribute_transformer.py`
- sha256: `d8733b4b6295985bfb3c9151b9208ce52e1a430730c7207f8c95dc513c44626e`
- bytes: 1074

````python
import ast
from niveristand import _errormessages, errors
from niveristand._translation import symbols, utils


def attribute_transformer(node, resources):
    var_name = utils.get_variable_name_from_node(node)
    if resources.has_variable(var_name):
        if isinstance(node.value, ast.Subscript):
            return utils.generic_ast_node_transform(node.value, resources)
        else:
            return resources.get_variable_rtseq_name(var_name)
    try:
        # Try to get the value of the node in case it's a DataType(x).value style.
        node_value = utils.get_value_from_node(node.value, resources)
        return str(node_value)
    except errors.TranslateError:
        # If we get a TranslateError it's because it wasn't a DataType(x).value, so move on.
        pass
    built_exp = utils.generic_ast_node_transform(node.value, resources) + "." + node.attr
    if built_exp in symbols._symbols:
        return symbols._symbols[built_exp]
    else:
        raise errors.TranslateError(_errormessages.unknown_identifier % var_name)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/augassign_transformer.py sha256=c0ad12930a6a701847b6d39fbaf96942149d8377189ba6ef0b5681bcf1ed0c8a bytes=285 -->
## FILE: src/niveristand/_translation/py2rtseq/augassign_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/augassign_transformer.py`
- sha256: `c0ad12930a6a701847b6d39fbaf96942149d8377189ba6ef0b5681bcf1ed0c8a`
- bytes: 285

````python
import ast
from niveristand._translation import utils


def augassign_transformer(node, resources):
    bin_op = ast.BinOp(node.target, node.op, node.value)
    assign_node = ast.Assign([node.target], bin_op)
    return utils.generic_ast_node_transform(assign_node, resources)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/binaryoperator_transformer.py sha256=bd4f8aaa77785d7ad04f400eba809a54420f1db7f6839cdacad477fc0026adec bytes=1101 -->
## FILE: src/niveristand/_translation/py2rtseq/binaryoperator_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/binaryoperator_transformer.py`
- sha256: `bd4f8aaa77785d7ad04f400eba809a54420f1db7f6839cdacad477fc0026adec`
- bytes: 1101

````python
from niveristand._translation import utils
from niveristand._translation.py2rtseq import validations
from niveristand.errors import VeristandNotImplementedError


def binaryoperator_transformer(node, resources):
    operator = _operator(node.op.__class__.__name__)
    if operator == "unknown":
        raise VeristandNotImplementedError()
    if operator in ("<<", ">>"):
        # Validate only the right hand side, on the left it makes sense to have negative numbers.
        validations.raise_if_negative_binary_operator_operand(node.right, resources)
    left = utils.generic_ast_node_transform(node.left, resources)
    right = utils.generic_ast_node_transform(node.right, resources)
    return "((" + left + ") " + operator + " (" + right + "))"


def _operator(ast_operator):
    return {
        "Add": "+",
        "Sub": "-",
        "Mult": "*",
        "Div": "/",
        "Pow": "**",
        "Mod": "%",
        "BitAnd": "&",
        "BitOr": "|",
        "BitXor": "^",
        "LShift": "<<",
        "RShift": ">>",
    }.get(ast_operator, "unknown")
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/booloperator_transformer.py sha256=656f9348ca1598d8dbe872ae8e87a0fc069196645b4f75219dae19209dcd47b7 bytes=823 -->
## FILE: src/niveristand/_translation/py2rtseq/booloperator_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/booloperator_transformer.py`
- sha256: `656f9348ca1598d8dbe872ae8e87a0fc069196645b4f75219dae19209dcd47b7`
- bytes: 823

````python
from niveristand._translation import utils
from niveristand._translation.py2rtseq import validations
from niveristand.errors import VeristandNotImplementedError


def booloperator_transformer(node, resources):
    operator = _operator(node.op.__class__.__name__)
    if operator == "unknown":
        raise VeristandNotImplementedError()
    for value in node.values:
        validations.raise_if_invalid_bool_operand(value, resources)
    result = "( " + utils.generic_ast_node_transform(node.values[0], resources) + " "
    for o in node.values[1:]:
        op = utils.generic_ast_node_transform(o, resources)
        result += operator + " " + op + " "
    return result + ")"


def _operator(ast_operator):
    return {
        "And": "&&",
        "Or": "||",
    }.get(ast_operator, "unknown")
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/break_transformer.py sha256=9c67efa69ab2ac38629a085d5024b32195ee3964aac90f3f532ad6a53d6ab0e6 bytes=160 -->
## FILE: src/niveristand/_translation/py2rtseq/break_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/break_transformer.py`
- sha256: `9c67efa69ab2ac38629a085d5024b32195ee3964aac90f3f532ad6a53d6ab0e6`
- bytes: 160

````python
from niveristand import _errormessages, errors


def break_transformer(node, resources):
    raise errors.TranslateError(_errormessages.break_unsupported)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/call_transformer.py sha256=7d96fad4f3fb55167dd3e712cede68776d5a059bf0ac783fe29dda6c3992d698 bytes=2809 -->
## FILE: src/niveristand/_translation/py2rtseq/call_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/call_transformer.py`
- sha256: `7d96fad4f3fb55167dd3e712cede68776d5a059bf0ac783fe29dda6c3992d698`
- bytes: 2809

````python
import ast
from niveristand import _errormessages
from niveristand import errors
from niveristand._translation import custom_action_symbols, symbols, utils
from niveristand.clientapi._datatypes import rtprimitives


def call_transformer(node, resources):
    if rtprimitives.is_channel_ref_type(node.func.id):
        if utils.is_node_ast_str(node.args[0]):
            node_value = utils.get_value_from_str_node(node.args[0])
            identifier = resources.get_channel_ref_rtseq_name_from_channel_name(node_value)
        else:
            raise errors.TranslateError(_errormessages.invalid_type_for_channel_ref)
        return identifier
    if rtprimitives.is_supported_data_type(node.func.id):
        if rtprimitives.is_scalar_type(node.func.id):
            return _transform_data_type_scalar(node)
        elif isinstance(node.args[0], ast.List):
            return _transform_datatype_non_scalar(node, resources)
        else:
            raise errors.TranslateError(_errormessages.init_var_invalid_type)
    if node.func.id in custom_action_symbols._custom_action_symbols:
        # Custom action symbols are basically transformers for functions that don't have
        # their own ast node. Invoke them here
        return custom_action_symbols._custom_action_symbols[node.func.id](node, resources)
    if node.func.id in symbols._symbols:
        # In case of a builtin expression get it out from symbols and add any arguments it may have
        func_name = symbols._symbols[node.func.id]
    else:
        # It only can be a RT sequence call, so treat it accordingly
        func_name = str(utils.generic_ast_node_transform(node.func, resources))
        resources.add_referenced_sequence(func_name)
    node_str = func_name + "("
    for arg in node.args:
        node_str += str(utils.generic_ast_node_transform(arg, resources))
        node_str += " ,"
    if not node.args:
        return node_str + ")"
    else:
        # remove space and comma
        return node_str[:-2] + ")"


def _transform_datatype_non_scalar(node, resources):
    data_value_str = utils.generic_ast_node_transform(node.args[0], resources)
    return data_value_str


def _transform_data_type_scalar(node):
    # In case of data type creation or declaration, create the appropriate value (for example Double(3)
    # needs to return "3.0", not "3".)
    data_type = rtprimitives.get_class_by_name(node.func.id)
    data_value_str = str(data_type(utils.get_element_value(node.args[0])).value)
    # we need to check the symbols dictionary because of named constants. Using Boolean(True)
    # needs to return "true" not "True"
    if data_value_str in symbols._symbols:
        data_value_str = symbols._symbols[data_value_str]
    return data_value_str
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/compareoperator_transformer.py sha256=90546e4a29477f40cf6fee06b1275be5854e9421733833ef4892449404b24b1d bytes=985 -->
## FILE: src/niveristand/_translation/py2rtseq/compareoperator_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/compareoperator_transformer.py`
- sha256: `90546e4a29477f40cf6fee06b1275be5854e9421733833ef4892449404b24b1d`
- bytes: 985

````python
from niveristand import _errormessages
from niveristand._translation import utils
from niveristand.errors import TranslateError, VeristandNotImplementedError


def compareoperator_transformer(node, resources):
    left = utils.generic_ast_node_transform(node.left, resources)
    result = "((" + left + ") "
    if len(node.ops) > 1:
        raise TranslateError(_errormessages.cascaded_comparison_operators_not_allowed)
    operator = _operator(node.ops[0].__class__.__name__)
    if operator == "unknown":
        raise VeristandNotImplementedError()
    right = utils.generic_ast_node_transform(node.comparators[0], resources)
    result += operator + " (" + right + ")"
    result += ")"
    return result


def _operator(ast_operator):
    return {
        "Eq": "==",
        "NotEq": "!=",
        "Gt": ">",
        "GtE": ">=",
        "Lt": "<",
        "LtE": "<=",
        "Is": "==",
        "IsNot": "!=",
    }.get(ast_operator, "unknown")
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/constant_transformer.py sha256=8f7010c7b263d29fe0102962917d455dec7f90eb0de9b09aa652f50c11df65b9 bytes=541 -->
## FILE: src/niveristand/_translation/py2rtseq/constant_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/constant_transformer.py`
- sha256: `8f7010c7b263d29fe0102962917d455dec7f90eb0de9b09aa652f50c11df65b9`
- bytes: 541

````python
from niveristand import _errormessages
from niveristand import errors


def constant_transformer(node, resources):
    if node.value is True or node.value is False:
        return str(node.value).lower()
    elif isinstance(node.value, (int, float, complex)) and str(node.value) not in (
        "True",
        "False",
        "None",
    ):
        return str(node.value)
    elif isinstance(node.value, str):
        return node.value
    else:
        raise errors.TranslateError(_errormessages.constant_not_supported)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/custom_generate_error.py sha256=0fa8d99bbde02c619b5a4ed3fa15e2e1985da4b73110ccdc8f14b3ca5b0c3f5b bytes=1244 -->
## FILE: src/niveristand/_translation/py2rtseq/custom_generate_error.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/custom_generate_error.py`
- sha256: `0fa8d99bbde02c619b5a4ed3fa15e2e1985da4b73110ccdc8f14b3ca5b0c3f5b`
- bytes: 1244

````python
import ast

from niveristand import _errormessages
from niveristand._translation import utils
from niveristand.clientapi import ErrorAction
from niveristand.clientapi import realtimesequencedefinition
from niveristand.errors import TranslateError


def custom_generate_error(node, resources):
    _validate_restrictions(node)
    try:
        error_code = eval(utils.generic_ast_node_transform(node.args[0], resources))
    except NameError:
        raise TranslateError(_errormessages.invalid_error_code_for_generate_error)
    message = node.args[1].s
    action = ErrorAction[node.args[2].attr]
    realtimesequencedefinition.add_generate_error(
        resources.get_current_block(), error_code, message, action.value
    )
    return ""


def _validate_restrictions(node):
    if not isinstance(node.args[0], ast.UnaryOp) and not utils.is_node_ast_num(node.args[0]):
        raise TranslateError(_errormessages.invalid_error_code_for_generate_error)
    if not utils.is_node_ast_str(node.args[1]):
        raise TranslateError(_errormessages.invalid_message_for_generate_error)
    if not isinstance(node.args[2], ast.Attribute):
        raise TranslateError(_errormessages.invalid_action_for_generate_error)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/custom_localhost_wait.py sha256=ebe16b33fe4de40e4b358e827d121487250d15282add04b46d15102c96d66f1a bytes=60 -->
## FILE: src/niveristand/_translation/py2rtseq/custom_localhost_wait.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/custom_localhost_wait.py`
- sha256: `ebe16b33fe4de40e4b358e827d121487250d15282add04b46d15102c96d66f1a`
- bytes: 60

````python
def custom_localhost_wait(node, resources):
    return ""
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/custom_math_log.py sha256=c2ac84b081ac64e33e421419824a55c157d3425f80bbbd9e8dd38b5986f91966 bytes=462 -->
## FILE: src/niveristand/_translation/py2rtseq/custom_math_log.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/custom_math_log.py`
- sha256: `c2ac84b081ac64e33e421419824a55c157d3425f80bbbd9e8dd38b5986f91966`
- bytes: 462

````python
from niveristand._translation import utils


def custom_math_log(node, resources):
    if len(node.args) == 1:
        func = "ln"
    else:
        func = "log"

    node_str = func + "("
    for arg in node.args:
        node_str += str(utils.generic_ast_node_transform(arg, resources))
        node_str += " ,"
    if not node.args:
        return node_str + ")"
    else:
        # remove space and comma
        return node_str[:-2] + ")"
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/custom_nivs_yield.py sha256=7759bbb447943145d9739e9b40ed424bcb5e2b6d06354c20e93417c03c8ff81e bytes=795 -->
## FILE: src/niveristand/_translation/py2rtseq/custom_nivs_yield.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/custom_nivs_yield.py`
- sha256: `7759bbb447943145d9739e9b40ed424bcb5e2b6d06354c20e93417c03c8ff81e`
- bytes: 795

````python
import inspect
from niveristand import _errormessages, errors
from niveristand.clientapi import realtimesequencedefinition


def custom_nivs_yield(node, resources):
    _validate_node()
    realtimesequencedefinition.add_yield(resources.get_current_block())
    return ""


def _validate_node():
    from niveristand._translation.py2rtseq import exp_transformer

    # There's only one valid way to call nivs_yield which is this call stack:
    # 0: _validate_node
    # 1: custom_nivs_yield
    # 2: call_transformer
    # 3: generic_ast_transform
    # 4: exp_transformer
    exp_frame = inspect.stack()[4]
    func = exp_frame.function
    if func is not exp_transformer.exp_transformer.__name__:
        raise errors.TranslateError(_errormessages.invalid_nivs_yield)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/custom_stop_task.py sha256=02d84549b5845bbafe6c019e4fba6d7d84d38876f0de8fa75b116fbc2b437c1e bytes=497 -->
## FILE: src/niveristand/_translation/py2rtseq/custom_stop_task.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/custom_stop_task.py`
- sha256: `02d84549b5845bbafe6c019e4fba6d7d84d38876f0de8fa75b116fbc2b437c1e`
- bytes: 497

````python
import ast
from niveristand import _errormessages
from niveristand.clientapi import realtimesequencedefinition
from niveristand.errors import TranslateError


def custom_stop_task(node, resources):
    _validate_restrictions(node)
    realtimesequencedefinition.add_stop_task(resources.get_current_block(), node.args[0].id)


def _validate_restrictions(node):
    if not isinstance(node.args[0], ast.Name):
        raise TranslateError(_errormessages.invalid_taskname_for_stop_task)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/default_transformer.py sha256=c008ff0a2353f3da05d5be276f1e1457f120f383a01164480165bbd0a2f78b36 bytes=187 -->
## FILE: src/niveristand/_translation/py2rtseq/default_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/default_transformer.py`
- sha256: `c008ff0a2353f3da05d5be276f1e1457f120f383a01164480165bbd0a2f78b36`
- bytes: 187

````python
from niveristand.errors import TranslateError


def default_transformer(node, resources):
    raise TranslateError("Unexpected transform for node type %s" % node.__class__.__name__)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/exp_transformer.py sha256=1372218cc8aff0d5004433cfb3b15e2f23cdd02820a56feeefce089818a61ed9 bytes=617 -->
## FILE: src/niveristand/_translation/py2rtseq/exp_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/exp_transformer.py`
- sha256: `1372218cc8aff0d5004433cfb3b15e2f23cdd02820a56feeefce089818a61ed9`
- bytes: 617

````python
from niveristand._translation import utils
from niveristand._translation.py2rtseq import validations
from niveristand.clientapi import realtimesequencedefinition as rtseqapi


def exp_transformer(node, resources):
    if validations.check_if_looks_like_doc_block(node):
        exp = ""
    else:
        exp = utils.generic_ast_node_transform(node.value, resources)
    if bool(exp):
        # Custom actions generate their own expressions and return None
        # so only add an expression if something was returned
        rtseqapi.add_expression(resources.get_current_block(), exp)
    return exp
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/for_transformer.py sha256=df80a12ebbdcf8f84ddb7887b220454e0c4072112c32cbeaa75c5b1195b1928a bytes=2622 -->
## FILE: src/niveristand/_translation/py2rtseq/for_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/for_transformer.py`
- sha256: `df80a12ebbdcf8f84ddb7887b220454e0c4072112c32cbeaa75c5b1195b1928a`
- bytes: 2622

````python
import ast

from niveristand import _errormessages
from niveristand._translation import utils
from niveristand._translation.py2rtseq import validations
from niveristand.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.clientapi._datatypes import ArrayType
from niveristand.errors import TranslateError


def for_transformer(node, resources):
    _validate_restrictions(node)
    parent_block = resources.get_current_block()
    var_name = utils.get_variable_name_from_node(node.iter)
    if resources.has_variable(var_name):
        collection_value = resources.get_variable_py_value(var_name)
        if not isinstance(collection_value, ArrayType):
            raise TranslateError(_errormessages.scalar_iterable_collection)
        collection = resources.get_variable_rtseq_name(var_name)
        iterator = node.target.id
        for_statement = rtseqapi.add_foreach_loop(parent_block, iterator, collection)
        # add the iterator as local variable, so that attribute_transformer returns the actual rtseq name of
        # the iterator
        resources.add_variable(iterator, 0, iterator)
        resources.add_variable(iterator + ".value", 0, iterator)
    elif utils.generic_ast_node_transform(node.iter, resources).startswith("range("):
        if len(node.iter.args) > 1:
            raise TranslateError(_errormessages.invalid_range_call)
        max_range = utils.generic_ast_node_transform(node.iter.args[0], resources)
        variable = node.target.id
        for_statement = rtseqapi.add_for_loop(parent_block, variable, max_range)
    else:
        raise TranslateError(_errormessages.invalid_iterable_collection)
    for statement in node.body:
        resources.set_current_block(for_statement.Body)
        utils.generic_ast_node_transform(statement, resources)
    resources.set_current_block(parent_block)


def _validate_restrictions(node):
    if node.orelse:
        raise TranslateError(_errormessages.for_else_not_supported)
    if not isinstance(node.iter, (ast.Name, ast.Attribute, ast.Call)):
        raise TranslateError(_errormessages.invalid_iterable_collection)
    if not isinstance(node.target, ast.Name):
        raise TranslateError(_errormessages.invalid_for_loop_iterator)
    if validations.check_if_any_in_block(ast.Return, node.body):
        raise TranslateError(_errormessages.return_unsupported_unless_last)
    if validations.check_if_any_in_block(ast.FunctionDef, node.body):
        raise TranslateError(_errormessages.invalid_nested_funcdef)
    validations.raise_if_try_in_node_body(node.body)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/functiondef_transformer.py sha256=bc126f2371b15a8c14f1dc9febfc08acffad7028c965d9d66df4560046dbef65 bytes=5065 -->
## FILE: src/niveristand/_translation/py2rtseq/functiondef_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/functiondef_transformer.py`
- sha256: `bc126f2371b15a8c14f1dc9febfc08acffad7028c965d9d66df4560046dbef65`
- bytes: 5065

````python
import ast
from collections import namedtuple
from niveristand import _decorators, _errormessages, errors
from niveristand._translation import utils
from niveristand._translation.py2rtseq import validations
from niveristand.clientapi._datatypes import BooleanValue, DoubleValue


def functiondef_transformer(node, resources):
    if validations.check_if_looks_like_doc_block(node.body[0]):
        node.body = node.body[1:]
    _validate_restrictions(node)
    for param in node.args.args:
        p = _init_args(param, resources)
        resources.add_parameter(p.name, p.def_value, p.by_value)
    for decorator in [dec for dec in node.decorator_list if type(dec) is ast.Call]:
        # the NivsParam decorator is a class, so it gets used like this:
        # @NivsParam(param_name, DataType(default), BY_REF)
        # which in ast terms is treated as an ast.Call. So, we look for those and convert to args.
        p = _decorator_to_arg(decorator, resources)
        resources.update_parameter(p.name, p.def_value, p.by_value)
    # reparenting should happen in each transformer that contains nested blocks
    resources.set_current_block(resources.get_rtseq().Code.Main.Body)
    for instruction in node.body:
        utils.generic_ast_node_transform(instruction, resources)
    return ""


_param = namedtuple("_param", "name def_value by_value")


def _init_args(node, resources):
    # default values for now
    by_value = False
    def_value = DoubleValue(0)
    if type(node) is ast.Name:
        arg_name = utils.generic_ast_node_transform(node, resources)
    elif "arg" in dir(ast) and type(node) is ast.arg:
        arg_name = node.arg
    return _param(arg_name, def_value, by_value)


def _decorator_to_arg(node, resources):
    arg_name = def_value = by_value = None
    if not len(node.args) == 3:
        raise errors.TranslateError(_errormessages.invalid_param_decorator)
    # this is a decorator param definition. First parameter is the string for the name.
    if utils.is_node_ast_str(node.args[0]):
        arg_name = utils.get_value_from_str_node(node.args[0])
    # second is the default value
    try:
        def_value = utils.get_value_from_node(node.args[1], resources)
    except errors.TranslateError:
        # def_value won't get assigned anything if an error occurs, which will trigger the exception later.
        pass
    # third is whether to pass by ref or by value
    valid_types = [ast.Name, ast.Attribute]
    if isinstance(node.args[2], tuple(valid_types)):
        by_value_str = utils.get_variable_name_from_node(node.args[2])
        by_value_str = getattr(_decorators.NivsParam, by_value_str.split(".")[-1], by_value_str)
        by_value = BooleanValue(by_value_str).value
    elif "NameConstant" in dir(ast) and utils.is_node_ast_nameconstant(node.args[2]):
        by_value = utils.get_value_from_nameconstant_node(node.args[2])

    if arg_name is None or def_value is None or by_value is None:
        raise errors.TranslateError(_errormessages.invalid_param_decorator)
    return _param(arg_name, def_value, by_value)


def _validate_restrictions(node):
    if validations.check_if_any_in_block(ast.FunctionDef, node.body):
        raise errors.TranslateError(_errormessages.invalid_function_definition)
    if (
        node.returns is not None
        or len(node.args.kwonlyargs) != 0
        or len(node.args.kw_defaults) != 0
        or node.args.vararg is not None
        or node.args.kwarg is not None
        or len(node.args.defaults) != 0
    ):
        raise errors.TranslateError(_errormessages.invalid_function_definition)
    if validations.check_if_any_in_block(validations.ast_try(), node.body):
        if not isinstance(node.body[0], validations.ast_try()):
            raise errors.TranslateError(_errormessages.try_must_be_first_stmt)
        if len(node.body) > 2:
            raise errors.TranslateError(_errormessages.invalid_stmt_after_try)
        elif len(node.body) == 2:
            if not isinstance(node.body[1], ast.Return):
                raise errors.TranslateError(_errormessages.invalid_stmt_after_try)
    return_statements = [statement for statement in node.body if isinstance(statement, ast.Return)]
    if len(return_statements) > 1:
        raise errors.TranslateError(_errormessages.multiple_return_statements)
    if validations.check_if_any_in_block(ast.Return, node.body[:-1]):
        raise errors.TranslateError(_errormessages.return_unsupported_unless_last)
    for decorator in node.decorator_list:
        decorator_name_node = decorator.func if isinstance(decorator, ast.Call) else decorator
        decorator_name = utils.get_variable_name_from_node(decorator_name_node)
        decorator_name = decorator_name.split(".")[-1]
        _raise_if_invalid_decorator(decorator_name)


def _raise_if_invalid_decorator(attribute):
    if not (attribute in _decorators._VALID_DECORATORS):
        raise errors.TranslateError(_errormessages.invalid_decorator)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/if_transformer.py sha256=e960cd768ecb8045d096a39263f683b30b1184a532b43c5bf9fbccdd5be3f57d bytes=1493 -->
## FILE: src/niveristand/_translation/py2rtseq/if_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/if_transformer.py`
- sha256: `e960cd768ecb8045d096a39263f683b30b1184a532b43c5bf9fbccdd5be3f57d`
- bytes: 1493

````python
import ast
from niveristand import _errormessages, errors
from niveristand._translation import utils
from niveristand._translation.py2rtseq import validations
from niveristand.clientapi import realtimesequencedefinition as rtseqapi


def if_transformer(node, resources):
    _validate_restrictions(node)
    test_condition = utils.generic_ast_node_transform(node.test, resources)
    parent_block = resources.get_current_block()
    if_else_statement = rtseqapi.add_if_else(parent_block, test_condition)
    for statement in node.body:
        resources.set_current_block(if_else_statement.IfTrue)
        utils.generic_ast_node_transform(statement, resources)
    for statement in node.orelse:
        resources.set_current_block(if_else_statement.IfFalse)
        utils.generic_ast_node_transform(statement, resources)
    resources.set_current_block(parent_block)


def _validate_restrictions(node):
    validations.raise_if_try_in_node_body(node.body)
    validations.raise_if_try_in_node_body(node.orelse)
    if validations.check_if_any_in_block(
        ast.Return, node.body
    ) or validations.check_if_any_in_block(ast.Return, node.orelse):
        raise errors.TranslateError(_errormessages.return_unsupported_unless_last)
    if validations.check_if_any_in_block(
        ast.FunctionDef, node.body
    ) or validations.check_if_any_in_block(ast.FunctionDef, node.orelse):
        raise errors.TranslateError(_errormessages.invalid_nested_funcdef)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/ifexp_transformer.py sha256=6e915276c20443e18c0df3e2f5570dba174aed2011d1f92bd7042de8913fa8c9 bytes=471 -->
## FILE: src/niveristand/_translation/py2rtseq/ifexp_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/ifexp_transformer.py`
- sha256: `6e915276c20443e18c0df3e2f5570dba174aed2011d1f92bd7042de8913fa8c9`
- bytes: 471

````python
from niveristand._translation import utils
from niveristand._translation.py2rtseq import validations


def ifexp_transformer(node, resources):
    validations.raise_if_invalid_if_test(node.test)
    test = utils.generic_ast_node_transform(node.test, resources)
    body = utils.generic_ast_node_transform(node.body, resources)
    orelse = utils.generic_ast_node_transform(node.orelse, resources)
    return "(" + test + ") ? (" + body + ") : (" + orelse + ")"
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/index_transformer.py sha256=501ef30be2c4afd9c3bedd631e3fa942def0990437ac386631767fd895fcde00 bytes=176 -->
## FILE: src/niveristand/_translation/py2rtseq/index_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/index_transformer.py`
- sha256: `501ef30be2c4afd9c3bedd631e3fa942def0990437ac386631767fd895fcde00`
- bytes: 176

````python
from niveristand._translation import utils


def index_transformer(node, resources):
    index = utils.generic_ast_node_transform(node.value, resources)
    return index
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/list_transformer.py sha256=3c26ee522d3f2764926ce3cd8faabef81d94a83131aabeee442a2ac9d3532351 bytes=327 -->
## FILE: src/niveristand/_translation/py2rtseq/list_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/list_transformer.py`
- sha256: `3c26ee522d3f2764926ce3cd8faabef81d94a83131aabeee442a2ac9d3532351`
- bytes: 327

````python
from niveristand._translation import utils


def list_transformer(node, resources):
    list_string = ""
    if not node.elts:
        return list_string
    else:
        for element in node.elts:
            list_string += utils.generic_ast_node_transform(element, resources) + ","
        return list_string[:-1]
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/module_transformer.py sha256=1d900acf374c10a2174a58e235c331c1db5747784a0cf62ed9df118984dce359 bytes=830 -->
## FILE: src/niveristand/_translation/py2rtseq/module_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/module_transformer.py`
- sha256: `1d900acf374c10a2174a58e235c331c1db5747784a0cf62ed9df118984dce359`
- bytes: 830

````python
import ast

from niveristand import _decorators
from niveristand._translation import utils


def module_transformer(node, resources):
    rtseqfuncs = [
        rtf
        for rtf in ast.iter_child_nodes(node)
        if type(rtf) is ast.FunctionDef and _has_rtseq_decorator(rtf)
    ]
    for rtseqfunc in rtseqfuncs:
        utils.generic_ast_node_transform(rtseqfunc, resources)
    return ""


def _has_rtseq_decorator(func_node):
    for decorator in func_node.decorator_list:
        if (
            isinstance(decorator, ast.Name)
            and (decorator.id == _decorators.nivs_rt_sequence.__name__)
        ) or (
            isinstance(decorator, ast.Attribute)
            and (decorator.attr == _decorators.nivs_rt_sequence.__name__)
        ):
            return True
    return False
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/name_transformer.py sha256=1977387722d1b448179838b2b658eacb749e864fb6f82a7479b05e54b9592e61 bytes=485 -->
## FILE: src/niveristand/_translation/py2rtseq/name_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/name_transformer.py`
- sha256: `1977387722d1b448179838b2b658eacb749e864fb6f82a7479b05e54b9592e61`
- bytes: 485

````python
from niveristand import _errormessages
from niveristand._translation import symbols
from niveristand.errors import TranslateError


def name_transformer(node, resources):
    if node.id == "None":
        raise TranslateError(_errormessages.none_not_supported)
    if node.id in symbols._symbols:
        return symbols._symbols[node.id]
    elif resources.has_variable(node.id):
        return resources.get_variable_rtseq_name(node.id)
    else:
        return node.id
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/nameconstant_transformer.py sha256=4cf88288fb181f970b5a66f2a5c5106995adea350a3d0adc7775cb3be99bd4e3 bytes=307 -->
## FILE: src/niveristand/_translation/py2rtseq/nameconstant_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/nameconstant_transformer.py`
- sha256: `4cf88288fb181f970b5a66f2a5c5106995adea350a3d0adc7775cb3be99bd4e3`
- bytes: 307

````python
from niveristand import _errormessages
from niveristand import errors


def nameconstant_transformer(node, resources):
    if node.value is True or node.value is False:
        return str(node.value).lower()
    else:
        raise errors.TranslateError(_errormessages.name_constant_not_supported)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/num_transformer.py sha256=310b27e3172689ce61ecd874e844d43d3fc3bd0c78eb43817dd527018b2ffee4 bytes=63 -->
## FILE: src/niveristand/_translation/py2rtseq/num_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/num_transformer.py`
- sha256: `310b27e3172689ce61ecd874e844d43d3fc3bd0c78eb43817dd527018b2ffee4`
- bytes: 63

````python
def num_transformer(node, resources):
    return str(node.n)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/pass_transformer.py sha256=6cb6f78abf67be9dfe9aabaf18524da0ad070a3b3cd1c7f9c279fbc89d35ee93 bytes=55 -->
## FILE: src/niveristand/_translation/py2rtseq/pass_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/pass_transformer.py`
- sha256: `6cb6f78abf67be9dfe9aabaf18524da0ad070a3b3cd1c7f9c279fbc89d35ee93`
- bytes: 55

````python
def pass_transformer(node, resources):
    return ""
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/return_transformer.py sha256=b969a69f5aee53b2284fa299610826d24de0a25f8c975d7be2603c65ba64a303 bytes=2520 -->
## FILE: src/niveristand/_translation/py2rtseq/return_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/return_transformer.py`
- sha256: `b969a69f5aee53b2284fa299610826d24de0a25f8c975d7be2603c65ba64a303`
- bytes: 2520

````python
import ast
from niveristand import _errormessages
from niveristand._translation import utils
from niveristand.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.clientapi._datatypes import ArrayType
from niveristand.errors import TranslateError


def return_transformer(node, resources):
    _validate_restrictions(node)
    rtseq = resources.get_rtseq()
    expression = utils.generic_ast_node_transform(node.value, resources)
    stripped_expression = (
        expression[: expression.find("[")] if expression.find("[") != -1 else expression
    )
    if isinstance(node.value, (ast.Name, ast.Attribute, ast.Subscript)):
        src_var_name = utils.get_variable_name_from_node(node.value)
        if resources.has_variable(str(src_var_name)) and not resources.has_channel_ref(
            stripped_expression
        ):
            rt_expression = expression
            return_default_value = resources.get_variable_py_value(src_var_name)
            # In case of "return var[0]" the default value is saved as a list, so make sure to not return list type
            # because those cannot be return variables.
            # The len check is there to not get index error in case of empty lists -> for that I don't know yet
            # what the solution is, so I will leave it like this (Arnold)
            if isinstance(return_default_value, ArrayType):
                if len(return_default_value.value):
                    return_default_value = return_default_value[0]
        else:
            raise TranslateError(_errormessages.invalid_return_value)
    elif isinstance(node.value, ast.Call) or utils.is_node_ast_num(node.value):
        return_default_value = utils.get_value_from_node(node.value, resources)
        if isinstance(return_default_value, ArrayType):
            raise TranslateError(_errormessages.invalid_return_type)
        rt_expression = expression
    else:
        raise TranslateError(_errormessages.invalid_return_value)
    var_name = rtseqapi.add_return_variable(rtseq, "__ret_var__", return_default_value)
    rtseqapi.add_assignment(resources.get_current_block(), var_name, rt_expression)
    return "return " + str(expression)


def _validate_restrictions(node):
    if (
        not isinstance(node.value, ast.Attribute)
        and not utils.is_node_ast_nameconstant(node.value)
        and not utils.is_node_ast_num(node.value)
    ):
        raise TranslateError(_errormessages.invalid_return_type)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/subscript_transformer.py sha256=9ecfd5b07eed8756f511c32a57f097ed1e6e5bf427d8a274d4ae81aac7fd1753 bytes=341 -->
## FILE: src/niveristand/_translation/py2rtseq/subscript_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/subscript_transformer.py`
- sha256: `9ecfd5b07eed8756f511c32a57f097ed1e6e5bf427d8a274d4ae81aac7fd1753`
- bytes: 341

````python
from niveristand._translation import utils


def subscript_transformer(node, resources):
    variable_name = utils.get_variable_name_from_node(node)
    rtseq_var_name = resources.get_variable_rtseq_name(variable_name)
    index = utils.generic_ast_node_transform(node.slice, resources)
    return rtseq_var_name + "[" + index + "]"
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/transformers.py sha256=884fca469e6a4728462869c1c02d8fb080d588d5470d91369d5c71be6db8b9c9 bytes=3852 -->
## FILE: src/niveristand/_translation/py2rtseq/transformers.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/transformers.py`
- sha256: `884fca469e6a4728462869c1c02d8fb080d588d5470d91369d5c71be6db8b9c9`
- bytes: 3852

````python
import ast
import sys
from niveristand._translation.py2rtseq import assign_transformer
from niveristand._translation.py2rtseq import attribute_transformer
from niveristand._translation.py2rtseq import augassign_transformer
from niveristand._translation.py2rtseq import binaryoperator_transformer
from niveristand._translation.py2rtseq import booloperator_transformer
from niveristand._translation.py2rtseq import break_transformer
from niveristand._translation.py2rtseq import call_transformer
from niveristand._translation.py2rtseq import compareoperator_transformer
from niveristand._translation.py2rtseq import constant_transformer
from niveristand._translation.py2rtseq import default_transformer
from niveristand._translation.py2rtseq import exp_transformer
from niveristand._translation.py2rtseq import for_transformer
from niveristand._translation.py2rtseq import functiondef_transformer
from niveristand._translation.py2rtseq import if_transformer
from niveristand._translation.py2rtseq import ifexp_transformer
from niveristand._translation.py2rtseq import index_transformer
from niveristand._translation.py2rtseq import list_transformer
from niveristand._translation.py2rtseq import module_transformer
from niveristand._translation.py2rtseq import name_transformer
from niveristand._translation.py2rtseq import nameconstant_transformer
from niveristand._translation.py2rtseq import num_transformer
from niveristand._translation.py2rtseq import pass_transformer
from niveristand._translation.py2rtseq import return_transformer
from niveristand._translation.py2rtseq import subscript_transformer
from niveristand._translation.py2rtseq import try_transformer
from niveristand._translation.py2rtseq import unaryoperator_transformer
from niveristand._translation.py2rtseq import while_transformer
from niveristand._translation.py2rtseq import with_transformer


TRANSFORMERS = {
    "Default": default_transformer.default_transformer,
    ast.Assign.__name__: assign_transformer.assign_transformer,
    ast.Attribute.__name__: attribute_transformer.attribute_transformer,
    ast.AugAssign.__name__: augassign_transformer.augassign_transformer,
    ast.BinOp.__name__: binaryoperator_transformer.binaryoperator_transformer,
    ast.BoolOp.__name__: booloperator_transformer.booloperator_transformer,
    ast.Break.__name__: break_transformer.break_transformer,
    ast.Call.__name__: call_transformer.call_transformer,
    ast.Compare.__name__: compareoperator_transformer.compareoperator_transformer,
    ast.Expr.__name__: exp_transformer.exp_transformer,
    ast.For.__name__: for_transformer.for_transformer,
    ast.FunctionDef.__name__: functiondef_transformer.functiondef_transformer,
    ast.If.__name__: if_transformer.if_transformer,
    ast.IfExp.__name__: ifexp_transformer.ifexp_transformer,
    ast.Index.__name__: index_transformer.index_transformer,
    ast.List.__name__: list_transformer.list_transformer,
    ast.Module.__name__: module_transformer.module_transformer,
    ast.Name.__name__: name_transformer.name_transformer,
    ast.Pass.__name__: pass_transformer.pass_transformer,
    ast.Return.__name__: return_transformer.return_transformer,
    ast.Subscript.__name__: subscript_transformer.subscript_transformer,
    ast.Try.__name__: try_transformer.try_transformer,
    ast.UnaryOp.__name__: unaryoperator_transformer.unaryoperator_transformer,
    ast.While.__name__: while_transformer.while_transformer,
    ast.With.__name__: with_transformer.with_transformer,
}

if sys.version_info < (3, 8):
    TRANSFORMERS[ast.NameConstant.__name__] = nameconstant_transformer.nameconstant_transformer
    TRANSFORMERS[ast.Num.__name__] = num_transformer.num_transformer
else:
    TRANSFORMERS[ast.Constant.__name__] = constant_transformer.constant_transformer
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/try_transformer.py sha256=dcf7cb1d6839511650778f9b5a81aedf11c4b5247212d9b0167af7c89347de15 bytes=1073 -->
## FILE: src/niveristand/_translation/py2rtseq/try_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/try_transformer.py`
- sha256: `dcf7cb1d6839511650778f9b5a81aedf11c4b5247212d9b0167af7c89347de15`
- bytes: 1073

````python
import ast
from niveristand import _errormessages
from niveristand._translation import utils
from niveristand._translation.py2rtseq import validations
from niveristand.errors import TranslateError


def try_transformer(node, resources):
    _validate_restrictions(node)
    for stmt in node.body:
        utils.generic_ast_node_transform(stmt, resources)
    resources.set_current_block(resources.get_rtseq().Code.CleanUp)
    for stmt in node.finalbody:
        utils.generic_ast_node_transform(stmt, resources)


def except_transformer(node, resources):
    raise TranslateError(_errormessages.invalid_try_except_orelse)


def _validate_restrictions(node):
    if node.handlers or node.orelse:
        raise TranslateError(_errormessages.invalid_try_except_orelse)
    if validations.check_if_any_in_block(
        ast.Return, node.body
    ) or validations.check_if_any_in_block(ast.Return, node.finalbody):
        raise TranslateError(_errormessages.return_not_supported_in_try_finally)
    validations.raise_if_try_in_node_body(node.body)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/unaryoperator_transformer.py sha256=19fdec3fe72b58491c4dfc39f6c2e49ba823a1c044aedc41c51a9b6e9cc4022b bytes=1001 -->
## FILE: src/niveristand/_translation/py2rtseq/unaryoperator_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/unaryoperator_transformer.py`
- sha256: `19fdec3fe72b58491c4dfc39f6c2e49ba823a1c044aedc41c51a9b6e9cc4022b`
- bytes: 1001

````python
import ast
from niveristand._translation import utils
from niveristand._translation.py2rtseq import validations
from niveristand.errors import VeristandNotImplementedError


def unaryoperator_transformer(node, resources):
    operator = _operator(node.op.__class__.__name__)
    if operator == "unknown":
        raise VeristandNotImplementedError()
    if operator == "!":
        if isinstance(node.operand, ast.UnaryOp):
            validations.raise_if_invalid_bool_operand(node.operand.operand, resources)
        else:
            validations.raise_if_invalid_bool_operand(node.operand, resources)
    if operator == "~":
        validations.raise_if_invalid_invert_operand(node.operand, resources)
    operand = utils.generic_ast_node_transform(node.operand, resources)
    return "(" + operator + "(" + operand + ")" + ")"


def _operator(ast_operator):
    return {
        "USub": "-",
        "Not": "!",
        "Invert": "~",
    }.get(ast_operator, "unknown")
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/unittests/test_attribute_transformer.py sha256=e9056202d368629e88fe7d20ea05f8688f42165c539ac526d9ff4965f92974f2 bytes=494 -->
## FILE: src/niveristand/_translation/py2rtseq/unittests/test_attribute_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/unittests/test_attribute_transformer.py`
- sha256: `e9056202d368629e88fe7d20ea05f8688f42165c539ac526d9ff4965f92974f2`
- bytes: 494

````python
import ast
from niveristand._translation.py2rtseq.attribute_transformer import attribute_transformer
from niveristand._translation.py2rtseq.utils import Resources
from niveristand.clientapi import DoubleValue


def test_datatype_value_works():
    tree = ast.parse("DoubleValue(0).value")
    # tree.body[0] is an Expr, and the attribute is the .value of that node.
    res = attribute_transformer(tree.body[0].value, Resources(None, "<test>"))
    assert res == str(DoubleValue(0))
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/unittests/test_functiondef_transformer.py sha256=4c154ce7615423d21a715d7ec2cc03e56d852d1e8b17446892e55db7a61b1ee2 bytes=1763 -->
## FILE: src/niveristand/_translation/py2rtseq/unittests/test_functiondef_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/unittests/test_functiondef_transformer.py`
- sha256: `4c154ce7615423d21a715d7ec2cc03e56d852d1e8b17446892e55db7a61b1ee2`
- bytes: 1763

````python
import ast
import inspect
from niveristand import errors
from niveristand._translation.py2rtseq import functiondef_transformer
from niveristand._translation.py2rtseq import utils
import pytest


def functiondef_with_default(i=1):
    return i


def functiondef_with_args(*args):
    return args


def functiondef_with_kwargs(**kwargs):
    return kwargs


def functiondef_nested():
    def functiondef_inside():
        pass

    pass


# def functiondef_with_kwarg_default(*args, kwarg=1):
#    return kwarg


def invalid_decorator(func):
    return func


class InvalidDecoratorClass:
    def __call__(self, f):
        return f

    @staticmethod
    def invalid_decorator_as_attribute(func):
        return func


@invalid_decorator
def functiondef_invalid_decorator():
    pass


@InvalidDecoratorClass()
def functiondef_invalid_decorator2():
    pass


@InvalidDecoratorClass.invalid_decorator_as_attribute
def functiondef_invalid_decorator3():
    pass


invalid_func_tests = [
    functiondef_with_default,
    functiondef_with_args,
    functiondef_with_kwargs,
    functiondef_nested,
    #  functiondef_with_kwarg_default,
    functiondef_invalid_decorator,
    functiondef_invalid_decorator2,
    functiondef_invalid_decorator3,
]


def idfunc(val):
    return val.__name__


@pytest.mark.parametrize("func", invalid_func_tests, ids=idfunc)
def test_functiondef_transformer_fails(func):
    _fail_function_helper(func)


def _fail_function_helper(func):
    node = ast.parse(inspect.getsource(func))
    node = node.body[0]
    with pytest.raises(errors.TranslateError):
        functiondef_transformer.functiondef_transformer(node, utils.Resources(None, "<test>"))
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/unittests/test_nameconstant_transformer.py sha256=d8753e836dbb4f1a536345c20302682f85f1d353ef8f269e3978764c31949525 bytes=703 -->
## FILE: src/niveristand/_translation/py2rtseq/unittests/test_nameconstant_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/unittests/test_nameconstant_transformer.py`
- sha256: `d8753e836dbb4f1a536345c20302682f85f1d353ef8f269e3978764c31949525`
- bytes: 703

````python
import ast
from niveristand import errors
from niveristand._translation.py2rtseq import nameconstant_transformer
import pytest


def test_true_node_returns_true_string():
    node = ast.NameConstant(value=True)
    res = nameconstant_transformer.nameconstant_transformer(node, None)
    assert res == "true"


def test_false_node_returns_false_string():
    node = ast.NameConstant(value=False)
    res = nameconstant_transformer.nameconstant_transformer(node, None)
    assert res == "false"


def test_none_node_throws():
    node = ast.NameConstant(value=None)
    with pytest.raises(errors.TranslateError):
        nameconstant_transformer.nameconstant_transformer(node, None)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/utils.py sha256=00e9205750856783f838249f266bee216d8cd5c6e061a5f4ca1dbf0b9af55276 bytes=4414 -->
## FILE: src/niveristand/_translation/py2rtseq/utils.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/utils.py`
- sha256: `00e9205750856783f838249f266bee216d8cd5c6e061a5f4ca1dbf0b9af55276`
- bytes: 4414

````python
from collections import OrderedDict
from niveristand import _errormessages
from niveristand import errors
from niveristand.clientapi._datatypes.rtprimitives import DoubleValue


class Resources:
    def __init__(self, rtseq, alias):
        from niveristand.clientapi.realtimesequencepkg import RealTimeSequencePkg

        self._rtseq = rtseq
        self._seq_alias = alias
        self._block = None
        self._local_variables = {}
        self._parameters = OrderedDict()
        self._deps = RealTimeSequencePkg()
        self._channel_references = list()

    def get_rtseq(self):
        return self._rtseq

    def set_current_block(self, block):
        self._block = block

    def get_current_block(self):
        return self._block

    def add_variable(self, py_name, py_value, rtseq_name):
        variable = _Variable(py_value, rtseq_name)
        self._local_variables[py_name] = variable

    def has_variable(self, variable_name):
        return variable_name in self._local_variables

    def get_variable_rtseq_name(self, variable_name):
        return self._local_variables[variable_name].rtseq_name

    def get_variable_py_name(self, rtseq_var_name):
        result = ""
        for key in self._local_variables.keys():
            if self._local_variables[key].rtseq_name == rtseq_var_name:
                result = key
        return result

    def get_variable_py_value(self, variable_name):
        return self._local_variables[variable_name].py_value

    def add_referenced_sequence(self, referenced):
        self._deps.add_referenced_sequence(self._seq_alias, referenced)

    def get_dependency_pkg(self):
        return self._deps

    def set_dependency_pkg(self, pkg):
        self._deps = pkg

    def add_channel_ref(self, variable_name, channel_name, rtseq_var_name, channel_is_vector):
        self._channel_references.append(
            _ChannelReference(channel_name, rtseq_var_name, channel_is_vector)
        )
        self.add_variable(variable_name, DoubleValue(0), rtseq_var_name)
        self.add_variable(variable_name + ".value", DoubleValue(0), rtseq_var_name)

    def has_channel_ref(self, rtseq_name):
        for channel_ref_obj in self._channel_references:
            if channel_ref_obj.rtseq_name == rtseq_name:
                return True
        return False

    def get_channel_ref_rtseq_name_from_channel_name(self, channel_name):
        for channel_ref_obj in self._channel_references:
            if channel_ref_obj.channel_name == channel_name:
                return channel_ref_obj.rtseq_name

    def get_all_channel_refs(self):
        return self._channel_references

    def add_parameter(self, param_name, default_value, by_value):
        if param_name in self._parameters:
            raise errors.UnexpectedError(_errormessages.unexpected_argument_redefine)
        rt_seq_param_name = _py_param_name_to_rtseq_param_name(param_name)
        self._parameters[param_name] = _Parameter(rt_seq_param_name, default_value, by_value)
        self.add_variable(param_name, default_value, rt_seq_param_name)
        self.add_variable(param_name + ".value", default_value, rt_seq_param_name)

    def get_parameters(self):
        return self._parameters.values()

    def update_parameter(self, param_name, default_value, by_value):
        if param_name not in self._parameters:
            raise errors.TranslateError(_errormessages.param_description_no_param)
        rt_seq_param_name = _py_param_name_to_rtseq_param_name(param_name)
        self._parameters[param_name] = _Parameter(rt_seq_param_name, default_value, by_value)
        self._local_variables[param_name].py_value = default_value


def _py_param_name_to_rtseq_param_name(name):
    return "p_" + name


class _Variable:
    def __init__(self, py_value, rtseq_name):
        self.py_value = py_value
        self.rtseq_name = rtseq_name


class _Parameter:
    def __init__(self, rtseq_name, default_value, by_value):
        self.rtseq_name = rtseq_name
        self.default_value = default_value
        self.by_value = by_value


class _ChannelReference:
    def __init__(self, channel_name, rtseq_name, channel_is_vector):
        self.channel_name = channel_name
        self.rtseq_name = rtseq_name
        self.channel_is_vector = channel_is_vector
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/validations.py sha256=ded68f7d226455df0c0983723d2d6ab426475cb36cd8e70cfa309b4346bf95f9 bytes=2262 -->
## FILE: src/niveristand/_translation/py2rtseq/validations.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/validations.py`
- sha256: `ded68f7d226455df0c0983723d2d6ab426475cb36cd8e70cfa309b4346bf95f9`
- bytes: 2262

````python
import ast
from niveristand import _errormessages, errors
from niveristand._translation import utils
from niveristand.clientapi._datatypes import VALID_TYPES


def raise_if_try_in_node_body(statements):
    if check_if_any_in_block(ast_try(), statements):
        raise errors.TranslateError(_errormessages.try_only_in_top_level_func)


def ast_try():
    return ast.Try


def check_if_any_in_block(ast_node, block):
    if any([isinstance(body_stmt, ast_node) for body_stmt in block]):
        return True
    return False


def check_if_looks_like_doc_block(node):
    return isinstance(node, ast.Expr) and utils.is_node_ast_str(node.value)


def raise_if_invalid_bool_operand(node, resources):
    invalid_operand = False
    try:
        if not isinstance(utils.get_value_from_node(node, resources).value, bool):
            invalid_operand = True
    except errors.TranslateError:
        pass
    if invalid_operand:
        raise errors.TranslateError(_errormessages.invalid_operand_for_boolean_operator)


def raise_if_invalid_if_test(node):
    if isinstance(node, ast.UnaryOp):
        node = node.operand
    if isinstance(node, ast.Call) and utils.get_variable_name_from_node(node.func) in VALID_TYPES:
        raise errors.TranslateError(_errormessages.invalid_type_for_if_test)


def raise_if_invalid_invert_operand(node, resources):
    invalid_operand = False
    try:
        if isinstance(utils.get_value_from_node(node, resources).value, (bool, float)):
            invalid_operand = True
    except errors.TranslateError:
        pass
    if invalid_operand:
        raise errors.TranslateError(_errormessages.invalid_operand_for_unary_invert_operator)


def raise_if_negative_binary_operator_operand(node, resources):
    invalid_operand = False
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        invalid_operand = True
    else:
        try:
            value = utils.get_value_from_node(node, resources).value
            if value < 0:
                invalid_operand = True
        except errors.TranslateError:
            pass
    if invalid_operand:
        raise errors.TranslateError(_errormessages.negative_operand_for_binary_operator)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/while_transformer.py sha256=a5166a679bb50aa4092a620d4a73f5ba8fe55db694738d53fa1745b669b44795 bytes=1229 -->
## FILE: src/niveristand/_translation/py2rtseq/while_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/while_transformer.py`
- sha256: `a5166a679bb50aa4092a620d4a73f5ba8fe55db694738d53fa1745b669b44795`
- bytes: 1229

````python
import ast
from niveristand import _errormessages, errors
from niveristand._translation import utils
from niveristand._translation.py2rtseq import validations
from niveristand.clientapi import realtimesequencedefinition as rtseqapi


def while_transformer(node, resources):
    _validate_restrictions(node, resources)
    test_condition = utils.generic_ast_node_transform(node.test, resources)
    parent_block = resources.get_current_block()
    while_statement = rtseqapi.add_while(parent_block, test_condition)
    for statement in node.body:
        resources.set_current_block(while_statement.Body)
        utils.generic_ast_node_transform(statement, resources)
    resources.set_current_block(parent_block)


def _validate_restrictions(node, resources):
    if node.orelse:
        raise errors.TranslateError(_errormessages.unsupported_orelse_while)
    if validations.check_if_any_in_block(ast.Return, node.body):
        raise errors.TranslateError(_errormessages.return_unsupported_unless_last)
    if validations.check_if_any_in_block(ast.FunctionDef, node.body):
        raise errors.TranslateError(_errormessages.invalid_nested_funcdef)
    validations.raise_if_try_in_node_body(node.body)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/py2rtseq/with_transformer.py sha256=ecb1fe9e83eefa0616d4477f210e27bc9d2fd5528ace2ae726f19fe775636b3e bytes=3174 -->
## FILE: src/niveristand/_translation/py2rtseq/with_transformer.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/py2rtseq/with_transformer.py`
- sha256: `ecb1fe9e83eefa0616d4477f210e27bc9d2fd5528ace2ae726f19fe775636b3e`
- bytes: 3174

````python
import ast
from niveristand import _decorators, _errormessages, errors
from niveristand._translation import utils
from niveristand._translation.py2rtseq import validations
from niveristand.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.library import _tasks


def with_transformer(node, resources):
    mt_name = _validate_multitask(node)
    parent_block = resources.get_current_block()
    multi_task = rtseqapi.add_multi_task(parent_block)
    for task_def in [func_def for func_def in node.body if isinstance(func_def, ast.FunctionDef)]:
        _validate_task(task_def, mt_name)
        task_block = rtseqapi.add_task(multi_task, task_def.name)
        resources.set_current_block(task_block)
        for stmt in task_def.body:
            utils.generic_ast_node_transform(stmt, resources)
    resources.set_current_block(parent_block)


def _validate_multitask(node):
    validations.raise_if_try_in_node_body(node.body)
    if validations.check_if_any_in_block(ast.Return, node.body):
        raise errors.TranslateError(_errormessages.return_unsupported_unless_last)
    # this validation is the opposite of the usual funcdef check.
    # we must make sure ALL statements are ast.FunctionDef
    if any(not isinstance(stmt, ast.FunctionDef) for stmt in node.body):
        raise errors.TranslateError(_errormessages.return_unsupported_unless_last)
    if "items" in dir(node):
        if len(node.items) > 1 or len(node.items) <= 0:
            raise errors.TranslateError(_errormessages.invalid_with_block)
        expr = node.items[0].context_expr
        opt_var = node.items[0].optional_vars
    else:
        expr = node.context_expr
        opt_var = node.optional_vars
    if not isinstance(expr, ast.Call):
        raise errors.TranslateError(_errormessages.invalid_with_block)
    # make sure the expression is "multitask()"
    func_name = _get_name_without_namespace_from_node(expr.func)
    if func_name is not _tasks.multitask.__name__ or len(expr.args) > 0 or opt_var is None:
        raise errors.TranslateError(_errormessages.invalid_with_block)
    return opt_var


def _validate_task(node, mt_name):
    body = node.body
    validations.raise_if_try_in_node_body(body)
    if validations.check_if_any_in_block(ast.FunctionDef, body):
        raise errors.TranslateError(_errormessages.invalid_function_definition)
    if validations.check_if_any_in_block(ast.Return, body):
        raise errors.TranslateError(_errormessages.return_unsupported_unless_last)
    if len(node.args.args) > 0:
        raise errors.TranslateError(_errormessages.invalid_with_block)
    decs = node.decorator_list
    if (
        len(decs) != 1
        or not isinstance(decs[0], ast.Call)
        or _get_name_without_namespace_from_node(decs[0].func) != _decorators.task.__name__
        or len(decs[0].args) != 1
        or decs[0].args[0].id is not mt_name.id
    ):
        raise errors.TranslateError(_errormessages.invalid_with_block)
    return node


def _get_name_without_namespace_from_node(node):
    return utils.get_variable_name_from_node(node).split(".")[-1]
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/rtseq2py/__init__.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: src/niveristand/_translation/rtseq2py/__init__.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/rtseq2py/__init__.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/symbols.py sha256=96425f1cf2346b0383f63149b2aacbbbe30b4fb543f298e283657464ff2e73d6 bytes=1417 -->
## FILE: src/niveristand/_translation/symbols.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/symbols.py`
- sha256: `96425f1cf2346b0383f63149b2aacbbbe30b4fb543f298e283657464ff2e73d6`
- bytes: 1417

````python
_symbols = {
    """Symbols dictionary

    Left-side: python symbol
    Right-side: rtsequence symbol
    """
    # built-in math
    "pi": "pi",
    "math.pi": "pi",
    "True": "true",
    "False": "false",
    "abs": "abs",
    "acos": "acos",
    "acosh": "acosh",
    "asin": "asin",
    "asinh": "asinh",
    "atan": "atan",
    "atan2": "atan2",
    "atanh": "atanh",
    "ceil": "ceil",
    "cos": "cos",
    "cosh": "cosh",
    "exp": "exp",
    "expm1": "expm1",
    "floor": "floor",
    "hypot": "hypot",
    "isnan": "isnan",
    "log1p": "ln1p",
    "log10": "log10",
    "log2": "log2",
    "max": "max",
    "min": "min",
    "fmod": "mod",
    "pow": "pow",
    "rand": "rand",
    "round": "round",
    "sin": "sin",
    "sinh": "sinh",
    "sqrt": "sqrt",
    "tan": "tan",
    "tanh": "tanh",
    # vs-specific functions
    "abstime": "abstime",
    "arraysize": "arraysize",
    "clearfault": "clearfault",
    "clearlasterror": "clearlasterror",
    "deltat": "deltat",
    "deltatus": "deltatus",
    "fault": "fault",
    "fix": "fix",
    "getlasterror": "getlasterror",
    "iteration": "iteration",
    "quotient": "quotient",
    "recip": "recip",
    "rem": "rem",
    "seqtime": "seqtime",
    "seqtimeus": "seqtimeus",
    "tickcountms": "tickcountms",
    "tickcountus": "tickcountus",
    # misc
    "range": "range",
}
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/unittests/test_is_node_ast_nameconstant.py sha256=1f00c1b4fe59797a0b468d567e87c2f51cb1a3c80269b8feebd9371fef1d4a48 bytes=3183 -->
## FILE: src/niveristand/_translation/unittests/test_is_node_ast_nameconstant.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/unittests/test_is_node_ast_nameconstant.py`
- sha256: `1f00c1b4fe59797a0b468d567e87c2f51cb1a3c80269b8feebd9371fef1d4a48`
- bytes: 3183

````python
import ast
import sys
from niveristand._translation import utils


def test_str_0_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value="0")
        res = utils.is_node_ast_nameconstant(node)
        assert res is False


def test_str_1_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value="1.0")
        res = utils.is_node_ast_nameconstant(node)
        assert res is False


def test_str_true_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value="True")
        res = utils.is_node_ast_nameconstant(node)
        assert res is False


def test_str_false_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value="False")
        res = utils.is_node_ast_nameconstant(node)
        assert res is False


def test_str_none_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value="None")
        res = utils.is_node_ast_nameconstant(node)
        assert res is False


def test_str_empty_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value="")
        res = utils.is_node_ast_nameconstant(node)
        assert res is False


def test_int_0_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=0)
        res = utils.is_node_ast_nameconstant(node)
        assert res is False


def test_int_1_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=1)
        res = utils.is_node_ast_nameconstant(node)
        assert res is False


def test_float_0_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=0.0)
        res = utils.is_node_ast_nameconstant(node)
        assert res is False


def test_float_1_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=1.0)
        res = utils.is_node_ast_nameconstant(node)
        assert res is False


def test_complex_1_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=1j)
        res = utils.is_node_ast_nameconstant(node)
        assert res is False


def test_complex_2_3_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=complex(2, 3))
        res = utils.is_node_ast_nameconstant(node)
        assert res is False


def test_true_check_returns_true_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=True)
        res = utils.is_node_ast_nameconstant(node)
        assert res is True


def test_false_check_returns_true_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=False)
        res = utils.is_node_ast_nameconstant(node)
        assert res is True


def test_none_check_returns_true_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=None)
        res = utils.is_node_ast_nameconstant(node)
        assert res is True
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/unittests/test_is_node_ast_num.py sha256=17f1c54a22fb4f5e0949921a04f9e350eab07d6a45a888185b80ad5828b38e6c bytes=3110 -->
## FILE: src/niveristand/_translation/unittests/test_is_node_ast_num.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/unittests/test_is_node_ast_num.py`
- sha256: `17f1c54a22fb4f5e0949921a04f9e350eab07d6a45a888185b80ad5828b38e6c`
- bytes: 3110

````python
import ast
import sys
from niveristand._translation import utils


def test_true_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=True)
        res = utils.is_node_ast_num(node)
        assert res is False
    assert True


def test_false_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=False)
        res = utils.is_node_ast_num(node)
        assert res is False
    assert True


def test_none_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=None)
        res = utils.is_node_ast_num(node)
        assert res is False
    assert True


def test_str_0_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value="0")
        res = utils.is_node_ast_num(node)
        assert res is False
    assert True


def test_str_1_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value="1.0")
        res = utils.is_node_ast_num(node)
        assert res is False


def test_str_true_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value="True")
        res = utils.is_node_ast_num(node)
        assert res is False


def test_str_false_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value="False")
        res = utils.is_node_ast_num(node)
        assert res is False


def test_str_none_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value="None")
        res = utils.is_node_ast_num(node)
        assert res is False


def test_str_empty_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value="")
        res = utils.is_node_ast_num(node)
        assert res is False


def test_int_0_check_returns_true_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=0)
        res = utils.is_node_ast_num(node)
        assert res is True


def test_int_1_check_returns_true_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=1)
        res = utils.is_node_ast_num(node)
        assert res is True


def test_float_0_check_returns_true_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=0.0)
        res = utils.is_node_ast_num(node)
        assert res is True


def test_float_1_check_returns_true_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=1.0)
        res = utils.is_node_ast_num(node)
        assert res is True


def test_complex_1_check_returns_true_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=1j)
        res = utils.is_node_ast_num(node)
        assert res is True


def test_complex_2_3_check_returns_true_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=complex(2, 3))
        res = utils.is_node_ast_num(node)
        assert res is True
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/unittests/test_is_node_ast_str.py sha256=0681434e577f0c6d5d0075fbc6c0e99a641b7d8f2f62002355afc18fefc0d931 bytes=2233 -->
## FILE: src/niveristand/_translation/unittests/test_is_node_ast_str.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/unittests/test_is_node_ast_str.py`
- sha256: `0681434e577f0c6d5d0075fbc6c0e99a641b7d8f2f62002355afc18fefc0d931`
- bytes: 2233

````python
import ast
import sys
from niveristand._translation import utils


def test_true_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=True)
        res = utils.is_node_ast_str(node)
        assert res is False


def test_false_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=False)
        res = utils.is_node_ast_str(node)
        assert res is False


def test_none_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=None)
        res = utils.is_node_ast_str(node)
        assert res is False


def test_int_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=0)
        res = utils.is_node_ast_str(node)
        assert res is False


def test_float_check_returns_false_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value=1.0)
        res = utils.is_node_ast_str(node)
        assert res is False


def test_str_true_check_returns_true_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value="True")
        res = utils.is_node_ast_str(node)
        assert res is True


def test_str_false_check_returns_true_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value="False")
        res = utils.is_node_ast_str(node)
        assert res is True


def test_str_none_check_returns_true_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value="None")
        res = utils.is_node_ast_str(node)
        assert res is True


def test_str_0_check_returns_true_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value="0")
        res = utils.is_node_ast_str(node)
        assert res is True


def test_str_1_check_returns_true_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value="1")
        res = utils.is_node_ast_str(node)
        assert res is True


def test_str_empty_check_returns_true_bool():
    if sys.version_info >= (3, 8):
        node = ast.Constant(value="")
        res = utils.is_node_ast_str(node)
        assert res is True
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/_translation/utils.py sha256=c8adfde088aea27199594e8c7f3b722a0c4c0ddb152968d7b6cc37b5d48a567d bytes=5855 -->
## FILE: src/niveristand/_translation/utils.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/_translation/utils.py`
- sha256: `c8adfde088aea27199594e8c7f3b722a0c4c0ddb152968d7b6cc37b5d48a567d`
- bytes: 5855

````python
import ast
import sys

from niveristand import _errormessages
from niveristand import errors
from niveristand._translation import symbols
from niveristand.clientapi import _datatypes
from niveristand.clientapi._datatypes import rtprimitives
from niveristand.errors import TranslateError


def generic_ast_node_transform(node, resources):
    from niveristand._translation.py2rtseq.transformers import TRANSFORMERS

    transformer_name = node.__class__.__name__
    transformer = TRANSFORMERS.get(transformer_name, TRANSFORMERS["Default"])
    return transformer(node, resources)


def get_value_from_node(node, resources):
    if isinstance(node, ast.Call):
        call = generic_ast_node_transform(node.func, resources)
        node_id = call.split(".")[-1]
        if rtprimitives.is_supported_data_type(node_id):
            datatype = rtprimitives.get_class_by_name(node.func.id)
            if rtprimitives.is_channel_ref_type(datatype.__name__):
                if rtprimitives.is_array_type(datatype.__name__):
                    datavalue = [0.0]
                else:
                    datavalue = 0.0
            elif type(node.args[0]) is ast.UnaryOp or is_node_ast_num(node.args[0]):
                datavalue = get_element_value(node.args[0])
            elif type(node.args[0]) is ast.Name:
                if node.args[0].id in symbols._symbols:
                    datavalue = symbols._symbols[node.args[0].id]
                else:
                    raise TranslateError(_errormessages.init_var_invalid_type)
            elif is_node_ast_nameconstant(node.args[0]):
                node_value = get_value_from_nameconstant_node(node.args[0])
                if node_value is True or node_value is False:
                    datavalue = node_value
                else:
                    raise TranslateError(_errormessages.init_var_invalid_type)
            elif type(node.args[0]) is ast.List:
                datavalue = [get_element_value(element) for element in node.args[0].elts]
            else:
                raise TranslateError(_errormessages.init_var_invalid_type)
            return datatype(datavalue)
    elif isinstance(node, ast.Name):
        if node.id in ["True", "False"]:
            return _datatypes.BooleanValue(node.id)
    elif is_node_ast_num(node):
        node_value = get_value_from_num_node(node)
        if isinstance(node_value, int):
            try:
                return_obj = _datatypes.I32Value(node_value)
            except OverflowError:
                return_obj = _datatypes.I64Value(node_value)
            return return_obj
        elif isinstance(node_value, float):
            return _datatypes.DoubleValue(node_value)
    elif is_node_ast_nameconstant(node):
        node_value = get_value_from_nameconstant_node(node)
        if node_value is None:
            raise TranslateError(_errormessages.init_var_invalid_type)
        return _datatypes.BooleanValue(node_value)
    raise TranslateError(_errormessages.init_var_invalid_type)


def get_element_value(node):
    if is_node_ast_num(node):
        return get_value_from_num_node(node)
    elif type(node) is ast.UnaryOp:
        return eval(generic_ast_node_transform(node, ()))
    elif type(node) is ast.Name:
        if node.id in symbols._symbols:
            return symbols._symbols[node.id]
        else:
            raise TranslateError(_errormessages.init_var_invalid_type)
    elif is_node_ast_nameconstant(node):
        return get_value_from_nameconstant_node(node)
    else:
        raise TranslateError(_errormessages.init_var_invalid_type)


def get_variable_name_from_node(node):
    full_name = ""
    cur_node = node
    while isinstance(cur_node, ast.Attribute):
        full_name = "." + cur_node.attr + full_name
        cur_node = cur_node.value
    if isinstance(cur_node, ast.Name):
        full_name = cur_node.id + full_name
    if isinstance(cur_node, ast.Subscript):
        full_name = get_variable_name_from_node(cur_node.value) + full_name
    return full_name


def get_channel_name(node):
    if is_node_ast_str(node):
        channel_name = get_value_from_str_node(node)
    else:
        raise errors.TranslateError(_errormessages.invalid_type_for_channel_ref)
    return channel_name


def is_node_ast_str(node):
    # Python 3.7
    if sys.version_info < (3, 8) and isinstance(node, ast.Str):
        return True
    # In Python 3.8, Str is Constant
    elif (
        sys.version_info >= (3, 8)
        and isinstance(node, ast.Constant)
        and isinstance(node.value, str)
    ):
        return True
    return False


def is_node_ast_num(node):
    # Python 3.7
    if sys.version_info < (3, 8) and isinstance(node, ast.Num):
        return True
    # In Python 3.8, Num is Constant
    elif (
        isinstance(node, ast.Constant)
        and isinstance(node.value, (int, float, complex))
        and str(node.value) not in ["True", "False", "None"]
    ):
        return True
    return False


def is_node_ast_nameconstant(node):
    # Python 3.7
    if sys.version_info < (3, 8) and isinstance(node, ast.NameConstant):
        return True
    # In Python 3.8, NameConstant is Constant
    elif (
        isinstance(node, ast.Constant)
        and node.value in [True, False, None]
        and str(node.value) in ["True", "False", "None"]
    ):
        return True
    return False


def get_value_from_str_node(node):
    if sys.version_info < (3, 8):
        return node.s
    else:
        return node.value


def get_value_from_num_node(node):
    if sys.version_info < (3, 8):
        return node.n
    else:
        return node.value


def get_value_from_nameconstant_node(node):
    return node.value
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/clientapi/__init__.py sha256=2fcbd69c12baa2bf333df952222fa7a14474a784744dec136f4eea3462a8e58b bytes=1468 -->
## FILE: src/niveristand/clientapi/__init__.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/clientapi/__init__.py`
- sha256: `2fcbd69c12baa2bf333df952222fa7a14474a784744dec136f4eea3462a8e58b`
- bytes: 1468

````python
from niveristand.clientapi._datatypes import BooleanValue
from niveristand.clientapi._datatypes import BooleanValueArray
from niveristand.clientapi._datatypes import ChannelReference
from niveristand.clientapi._datatypes import DoubleValue
from niveristand.clientapi._datatypes import DoubleValueArray
from niveristand.clientapi._datatypes import I32Value
from niveristand.clientapi._datatypes import I32ValueArray
from niveristand.clientapi._datatypes import I64Value
from niveristand.clientapi._datatypes import I64ValueArray
from niveristand.clientapi._datatypes import U32Value
from niveristand.clientapi._datatypes import U32ValueArray
from niveristand.clientapi._datatypes import U64Value
from niveristand.clientapi._datatypes import U64ValueArray
from niveristand.clientapi._datatypes import VectorChannelReference
from niveristand.clientapi._realtimesequencedefinitionapi.erroraction import ErrorAction
from niveristand.clientapi.realtimesequence import RealTimeSequence
from niveristand.clientapi.stimulusprofileapi import StimulusProfileState


__all__ = [
    "BooleanValue",
    "BooleanValueArray",
    "ChannelReference",
    "DoubleValue",
    "DoubleValueArray",
    "I32Value",
    "I32ValueArray",
    "I64Value",
    "I64ValueArray",
    "U32Value",
    "U32ValueArray",
    "U64Value",
    "U64ValueArray",
    "VectorChannelReference",
    "ErrorAction",
    "RealTimeSequence",
    "StimulusProfileState",
]
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/clientapi/_datatypes/__init__.py sha256=08b04c68ed50c5730e5ee2e6fcfe94cd567060a0fc6d0654561bf890f992ec35 bytes=1605 -->
## FILE: src/niveristand/clientapi/_datatypes/__init__.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/clientapi/_datatypes/__init__.py`
- sha256: `08b04c68ed50c5730e5ee2e6fcfe94cd567060a0fc6d0654561bf890f992ec35`
- bytes: 1605

````python
from niveristand.clientapi._datatypes.rtprimitives import ArrayType
from niveristand.clientapi._datatypes.rtprimitives import BooleanValue
from niveristand.clientapi._datatypes.rtprimitives import BooleanValueArray
from niveristand.clientapi._datatypes.rtprimitives import ChannelReference
from niveristand.clientapi._datatypes.rtprimitives import DataType
from niveristand.clientapi._datatypes.rtprimitives import DoubleValue
from niveristand.clientapi._datatypes.rtprimitives import DoubleValueArray
from niveristand.clientapi._datatypes.rtprimitives import I32Value
from niveristand.clientapi._datatypes.rtprimitives import I32ValueArray
from niveristand.clientapi._datatypes.rtprimitives import I64Value
from niveristand.clientapi._datatypes.rtprimitives import I64ValueArray
from niveristand.clientapi._datatypes.rtprimitives import U32Value
from niveristand.clientapi._datatypes.rtprimitives import U32ValueArray
from niveristand.clientapi._datatypes.rtprimitives import U64Value
from niveristand.clientapi._datatypes.rtprimitives import U64ValueArray
from niveristand.clientapi._datatypes.rtprimitives import VALID_TYPES
from niveristand.clientapi._datatypes.rtprimitives import VectorChannelReference


__all__ = [
    "ArrayType",
    "BooleanValue",
    "BooleanValueArray",
    "ChannelReference",
    "VectorChannelReference",
    "DataType",
    "DoubleValue",
    "DoubleValueArray",
    "I32Value",
    "I32ValueArray",
    "I64Value",
    "I64ValueArray",
    "U32Value",
    "U32ValueArray",
    "U64Value",
    "U64ValueArray",
    "VALID_TYPES",
]
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/clientapi/_datatypes/rtprimitives.py sha256=b2ad178df25a5111e9ba8965763214d6f1ae0daf7bf7b0aea46b01d13bf1d5b9 bytes=21816 -->
## FILE: src/niveristand/clientapi/_datatypes/rtprimitives.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/clientapi/_datatypes/rtprimitives.py`
- sha256: `b2ad178df25a5111e9ba8965763214d6f1ae0daf7bf7b0aea46b01d13bf1d5b9`
- bytes: 21816

````python
from niveristand import _internal
from NationalInstruments.VeriStand.Data import (  # noqa: I100 .NET imports need to be out of order
    BooleanValue as ClientApiBooleanValue,
)
from NationalInstruments.VeriStand.Data import BooleanValueArray as ClientApiBooleanValueArray
from NationalInstruments.VeriStand.Data import DataValue
from NationalInstruments.VeriStand.Data import DoubleValue as ClientApiDoubleValue
from NationalInstruments.VeriStand.Data import DoubleValueArray as ClientApiDoubleValueArray
from NationalInstruments.VeriStand.Data import I32Value as ClientApiI32Value
from NationalInstruments.VeriStand.Data import I32ValueArray as ClientApiI32ValueArray
from NationalInstruments.VeriStand.Data import I64Value as ClientApiI64Value
from NationalInstruments.VeriStand.Data import I64ValueArray as ClientApiI64ValueArray
from NationalInstruments.VeriStand.Data import U32Value as ClientApiU32Value
from NationalInstruments.VeriStand.Data import U32ValueArray as ClientApiU32ValueArray
from NationalInstruments.VeriStand.Data import U64Value as ClientApiU64Value
from NationalInstruments.VeriStand.Data import U64ValueArray as ClientApiU64ValueArray
from niveristand import _errormessages
from niveristand import errors as nivsexceptions
from niveristand.clientapi._factory import _DefaultGatewayFactory
from System import Int32 as SystemInt32
from System import Int64 as SystemInt64
from System import UInt32 as SystemUInt32
from System import UInt64 as SystemUInt64

_internal.dummy()


def get_class_by_name(name):
    return VALID_TYPES[name]


def is_supported_data_type(name):
    return name in VALID_TYPES


def is_supported_return_type(name):
    return name in VALID_RETURN_TYPES


def is_scalar_type(name):
    return name in VALID_RETURN_TYPES


def is_array_type(name):
    return name in VALID_ARRAY_TYPES


def is_channel_ref_type(name):
    return name in CHANNEL_REF_TYPES


class DataType(object):
    """
    Use as base class for all VeriStand datatypes.

    Args:
        value: initial value. Note: Actual value and type depends on subclass.
        description(str): a description of the value. For documentation purposes only.
        units(str): units represented by this value. For documentation purposes only.

    Raises:
        :class:`TypeError`: if an invalid value is used to initialize an instance.

    This class is not meant to be instantiated.

    """

    def __init__(self, value, description="", units=""):
        if isinstance(value, DataValue):
            self._data_value = value
        elif isinstance(value, DataType):
            self._data_value = self._to_data_value(value.value)
        else:
            self._data_value = self._to_data_value(value)

    def __str__(self):
        return str(self._data_value)

    def _to_data_value(self, value):
        raise nivsexceptions.TranslateError(_errormessages.invalid_type_to_convert)

    @staticmethod
    def _is_compatible_with_datatype(other):
        return isinstance(other, (int, float))  # noqa F821

    @staticmethod
    def _is_integer_type(other):
        return isinstance(other, int)  # noqa F821

    @staticmethod
    def _is_valid_assign_type(other):
        return isinstance(other, (int, float, bool))  # noqa F821

    def __add__(self, other):
        if isinstance(other, DataType):
            return self.value + other.value
        elif isinstance(other, (int, float)):
            return self.value + other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, DataType):
            return self.value - other.value
        elif isinstance(other, (int, float)):
            return self.value - other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rsub__(self, other):
        if isinstance(other, DataType):
            return other.value - self.value
        elif isinstance(other, (int, float)):
            return other - self.value
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __mul__(self, other):
        if isinstance(other, DataType):
            return self.value * other.value
        elif isinstance(other, (int, float)):
            return self.value * other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __divmod__(self, other):
        if isinstance(other, DataType):
            return self.value / other.value
        elif isinstance(other, (int, float)):
            return self.value / other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rdivmod__(self, other):
        if isinstance(other, DataType):
            return other.value / self.value
        elif isinstance(other, (int, float)):
            return other / self.value
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __floordiv__(self, other):
        if isinstance(other, DataType):
            return self.value // other.value
        elif isinstance(other, (int, float)):
            return self.value // other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rfloordiv__(self, other):
        if isinstance(other, DataType):
            return other.value // self.value
        elif isinstance(other, (int, float)):
            return other // self.value
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __truediv__(self, other):
        if isinstance(other, DataType):
            return self.value / other.value
        elif isinstance(other, (int, float)):
            return self.value / other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rtruediv__(self, other):
        if isinstance(other, DataType):
            return other.value / self.value
        elif isinstance(other, (int, float)):
            return other / self.value
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __div__(self, other):
        if isinstance(other, DataType):
            return self.value / other.value
        elif isinstance(other, (int, float)):
            return self.value / other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rdiv__(self, other):
        if isinstance(other, DataType):
            return other.value / self.value
        elif isinstance(other, (int, float)):
            return other / self.value

    def __pow__(self, power, modulo=None):
        if isinstance(power, DataType):
            return self.value**power.value
        elif isinstance(power, (int, float)):
            return self.value**power
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rpow__(self, other):
        if isinstance(other, DataType):
            return other.value**self.value
        elif isinstance(other, (int, float)):
            return other**self.value
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __mod__(self, other):
        if isinstance(other, DataType):
            return self.value % other.value
        elif self._is_compatible_with_datatype(other):
            return self.value % other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rmod__(self, other):
        if isinstance(other, DataType):
            return other.value % self.value
        elif self._is_compatible_with_datatype(other):
            return other % self.value
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __and__(self, other):
        if isinstance(other, (I32Value, I64Value)):
            return self.value & other.value
        elif self._is_integer_type(other):
            return self.value & other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rand__(self, other):
        return self.__and__(other)

    def __or__(self, other):
        if isinstance(other, (I32Value, I64Value)):
            return self.value | other.value
        elif self._is_integer_type(other):
            return self.value | other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __ror__(self, other):
        return self.__or__(other)

    def __xor__(self, other):
        if isinstance(other, (I32Value, I64Value)):
            return self.value ^ other.value
        elif self._is_integer_type(other):
            return self.value ^ other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rxor__(self, other):
        return self.__xor__(other)

    def __lshift__(self, other):
        if isinstance(other, (I32Value, I64Value)):
            return self.value << other.value
        elif self._is_integer_type(other):
            return self.value << other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rlshift__(self, other):
        if isinstance(other, (I32Value, I64Value)):
            return other.value << self.value
        elif self._is_integer_type(other):
            return other << self.value

        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rshift__(self, other):
        if isinstance(other, (I32Value, I64Value)):
            return self.value >> other.value
        elif self._is_integer_type(other):
            return self.value >> other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __rrshift__(self, other):
        if isinstance(other, (I32Value, I64Value)):
            return other.value >> self.value
        elif self._is_integer_type(other):
            return other >> self.value

    def __eq__(self, other):
        if isinstance(other, DataType):
            return self.value == other.value
        elif isinstance(other, (int, float, bool)):
            return self.value == other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __ne__(self, other):
        if isinstance(other, DataType):
            return self.value != other.value
        elif self._is_compatible_with_datatype(other):
            return self.value != other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __gt__(self, other):
        if isinstance(other, DataType):
            return self.value > other.value
        elif self._is_compatible_with_datatype(other):
            return self.value > other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __ge__(self, other):
        if isinstance(other, DataType):
            return self.value >= other.value
        elif self._is_compatible_with_datatype(other):
            return self.value >= other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __lt__(self, other):
        if isinstance(other, DataType):
            return self.value < other.value
        elif self._is_compatible_with_datatype(other):
            return self.value < other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __inv__(self):
        self.__invert__()

    def __invert__(self):
        if isinstance(self, (I32Value, I64Value, U32Value, U64Value)):
            return ~self.value
        elif isinstance(self, (BooleanValue, DoubleValue)):
            return 0
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    def __le__(self, other):
        if isinstance(other, DataType):
            return self.value <= other.value
        elif self._is_compatible_with_datatype(other):
            return self.value <= other
        else:
            raise nivsexceptions.VeristandError(_errormessages.invalid_type_for_operator)

    @property
    def value(self):
        return self._data_value.Value

    @value.setter
    def value(self, newvalue):
        self._data_value.Value = self._to_data_value(newvalue).Value


class ArrayType(DataType):
    def _to_data_value(self, value):
        raise nivsexceptions.TranslateError(_errormessages.invalid_type_to_convert)

    def __getitem__(self, key):
        return self.value[key]

    def __setitem__(self, key, value):
        return nivsexceptions.VeristandError(_errormessages.cannot_change_array_elements)


class ChannelReference(DataType):
    """
    Creates a new scalar channel reference.

    Creates a new reference to a scalar channel and specifies which channel assignment to map the new channel reference
    to. You can specify a channel by its alias or by the path to the channel in the system definition. For example:
    Targets/Controller/System Channels/Model Count.
    """

    def __init__(self, value, description="", units=""):
        super(ChannelReference, self).__init__(value, description, units)
        self._channel_name = value

    @property
    def value(self):
        return _DefaultGatewayFactory.get_workspace2().get_single_channel_value(self._channel_name)

    @value.setter
    def value(self, newvalue):
        _DefaultGatewayFactory.get_workspace2().set_single_channel_value(
            self._channel_name, newvalue
        )

    def _to_data_value(self, value):
        # in pythonnet 3.0.0+, strings are no longer coerced to 0 by ClientApiDoubleValue
        if isinstance(value, str):
            return ClientApiDoubleValue(0.0)
        else:
            return ClientApiDoubleValue(value)


class VectorChannelReference(ArrayType):
    """
    Creates a new vector channel reference.

    Creates a new reference to a vector channel and specifies which channel assignment to map the new channel reference
    to. You can specify a channel by its alias or by the path to the channel in the system definition. For example:
    Targets/Controller/System Channels/Model Count.
    """

    @property
    def value(self):
        return [DoubleValue(item) for item in self._data_value.Value]

    def _to_data_value(self, value):
        return ClientApiDoubleValueArray(value)

    def __getitem__(self, key):
        raise nivsexceptions.VeristandNotImplementedError()


class BooleanValue(DataType):
    """Creates a new boolean value reference."""

    def _to_data_value(self, value):
        if self._is_valid_assign_type(value):
            value = bool(value)
        elif type(value) is str and str(value).lower() == "true":
            value = True
        elif type(value) is str and str(value).lower() == "false":
            value = False
        else:
            raise TypeError(
                '%s can not be created from value "%s"' % (self.__class__.__name__, str(value))
            )
        return ClientApiBooleanValue(value)


class BooleanValueArray(ArrayType):
    """Creates a new reference to an array of :class:`BooleanValue`."""

    @property
    def value(self):
        return [BooleanValue(item) for item in self._data_value.Value]

    def _to_data_value(self, value):
        values = [BooleanValue(item).value for item in value]
        return ClientApiBooleanValueArray(values)


class DoubleValue(DataType):
    """Creates a new floating-point value reference."""

    def _to_data_value(self, value):
        if self._is_valid_assign_type(value):
            value = float(value)
        else:
            raise TypeError(
                '%s can not be created from value "%s"' % (self.__class__.__name__, str(value))
            )
        return ClientApiDoubleValue(value)


class DoubleValueArray(ArrayType):
    """Creates a new reference to an array of :class:`DoubleValue`."""

    @property
    def value(self):
        return [DoubleValue(item) for item in self._data_value.Value]

    def _to_data_value(self, value):
        values = [DoubleValue(item).value for item in value]
        return ClientApiDoubleValueArray(values)


class I32Value(DataType):
    """Creates a new, signed 32-bit integer value reference."""

    def _to_data_value(self, value):
        if self._is_valid_assign_type(value):
            value = SystemInt32(int(value))
        else:
            raise TypeError(
                '%s can not be created from value "%s"' % (self.__class__.__name__, str(value))
            )
        return ClientApiI32Value(value)


class I32ValueArray(ArrayType):
    """Creates a new reference to an array of :class:`I32Value`."""

    @property
    def value(self):
        return [I32Value(item) for item in self._data_value.Value]

    def _to_data_value(self, value):
        values = [I32Value(item).value for item in value]
        return ClientApiI32ValueArray(values)


class I64Value(DataType):
    """Creates a new, signed 64-bit integer value reference."""

    def _to_data_value(self, value):
        if self._is_valid_assign_type(value):
            value = SystemInt64(int(value))
        else:
            raise TypeError(
                '%s can not be created from value "%s"' % (self.__class__.__name__, str(value))
            )
        return ClientApiI64Value(value)


class I64ValueArray(ArrayType):
    """Creates a new reference to an array of :class:`I64Value`."""

    @property
    def value(self):
        return [I64Value(item) for item in self._data_value.Value]

    def _to_data_value(self, value):
        values = [I64Value(item).value for item in value]
        return ClientApiI64ValueArray(values)


class U32Value(DataType):
    """Creates a new, unsigned 32-bit integer value reference."""

    def _to_data_value(self, value):
        if self._is_valid_assign_type(value):
            value = SystemUInt32(int(value))
        else:
            raise TypeError(
                '%s can not be created from value "%s"' % (self.__class__.__name__, str(value))
            )
        return ClientApiU32Value(value)


class U32ValueArray(ArrayType):
    """Creates a new reference to an array of :class:`U32Value`."""

    @property
    def value(self):
        return [U32Value(item) for item in self._data_value.Value]

    def _to_data_value(self, value):
        values = [U32Value(item).value for item in value]
        return ClientApiU32ValueArray(values)


class U64Value(DataType):
    """Creates a new, unsigned 64-bit integer value reference."""

    def _to_data_value(self, value):
        if self._is_valid_assign_type(value):
            value = SystemUInt64(int(value))
        else:
            raise TypeError(
                '%s can not be created from value "%s"' % (self.__class__.__name__, str(value))
            )
        return ClientApiU64Value(value)


class U64ValueArray(ArrayType):
    """Creates a new reference to an array of :class:`U64Value`."""

    @property
    def value(self):
        return [U64Value(item) for item in self._data_value.Value]

    def _to_data_value(self, value):
        values = [U64Value(item).value for item in value]
        return ClientApiU64ValueArray(values)


VALID_TYPES = {
    ArrayType.__name__: ArrayType,
    BooleanValue.__name__: BooleanValue,
    BooleanValueArray.__name__: BooleanValueArray,
    ChannelReference.__name__: ChannelReference,
    DoubleValue.__name__: DoubleValue,
    DoubleValueArray.__name__: DoubleValueArray,
    I32Value.__name__: I32Value,
    I32ValueArray.__name__: I32ValueArray,
    I64Value.__name__: I64Value,
    I64ValueArray.__name__: I64ValueArray,
    U32Value.__name__: U32Value,
    U32ValueArray.__name__: U32ValueArray,
    U64Value.__name__: U64Value,
    U64ValueArray.__name__: U64ValueArray,
    VectorChannelReference.__name__: VectorChannelReference,
}

VALID_RETURN_TYPES = {
    BooleanValue.__name__: BooleanValue,
    DoubleValue.__name__: DoubleValue,
    I32Value.__name__: I32Value,
    I64Value.__name__: I64Value,
    U32Value.__name__: U32Value,
    U64Value.__name__: U64Value,
}

VALID_ARRAY_TYPES = {
    BooleanValueArray.__name__: BooleanValueArray,
    DoubleValueArray.__name__: DoubleValueArray,
    I32ValueArray.__name__: I32ValueArray,
    I64Value.__name__: I64ValueArray,
    U32ValueArray.__name__: U32ValueArray,
    U64ValueArray.__name__: U64ValueArray,
    VectorChannelReference.__name__: VectorChannelReference,
}

CHANNEL_REF_TYPES = {
    ChannelReference.__name__: ChannelReference,
    VectorChannelReference.__name__: VectorChannelReference,
}
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/clientapi/_dotnetclasswrapperbase.py sha256=38924ba0d39ebcc3eec4cc38ce21d259e3261fc014eea87d320e2bceb114e3c1 bytes=579 -->
## FILE: src/niveristand/clientapi/_dotnetclasswrapperbase.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/clientapi/_dotnetclasswrapperbase.py`
- sha256: `38924ba0d39ebcc3eec4cc38ce21d259e3261fc014eea87d320e2bceb114e3c1`
- bytes: 579

````python
class _DotNetClassWrapperBase(object):
    """

    The base class for all the classes that wrap around a VeriStand public api C# class.

    Args:
        dot_net_instance (): a C# instance of the wrapped C# class.

    """

    def __init__(self, dot_net_instance):
        self._dot_net_instance = dot_net_instance

    @property
    def dot_net_instance(self):
        """
        Gets the C# instance of the wrapped C# class.

        Returns:
            (): The C# instance of the wrapped C# class

        """
        return self._dot_net_instance
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/clientapi/_error.py sha256=8cc1e1f3e2ed93dd0eaabeb60904a86511525ca0d90f6264407bd1a816c07274 bytes=1778 -->
## FILE: src/niveristand/clientapi/_error.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/clientapi/_error.py`
- sha256: `8cc1e1f3e2ed93dd0eaabeb60904a86511525ca0d90f6264407bd1a816c07274`
- bytes: 1778

````python
from niveristand import _errormessages, errors
from niveristand.clientapi._dotnetclasswrapperbase import _DotNetClassWrapperBase
from NationalInstruments.VeriStand import (  # noqa: I100 .NET imports need to be out of order
    Error as ErrorDotNet,
)


class _Error(_DotNetClassWrapperBase):
    """

    Represents NI VeriStand error information, including an integer error code and a string error message.

    Args:
        dot_net_instance (NationalInstruments.VeriStand.Error):  the C# instance to wrap around.

    """

    def __init__(self, dot_net_instance):
        if isinstance(dot_net_instance, ErrorDotNet):
            super(_Error, self).__init__(dot_net_instance)
        else:
            raise errors.VeristandError(
                _errormessages.unexpected_dot_net_data_type % "NationalInstruments.VeriStand.Error"
            )

    @property
    def error_code(self):
        """
        Gets the VeriStand specific ErrorCode.

        Returns:
            (int): the VeriStand specific error code

        """
        return self.dot_net_instance.ErrorCode

    @property
    def is_error(self):
        """
        Gets a Boolean value indicating whether the Error object contains an error state.

        Returns:
            (bool): True if the Error contains an error state.

        """
        return self.dot_net_instance.IsError

    @property
    def resolved_error_message(self):
        """
        Gets the resolved error message.

        The resolved error message provides error information for non-LabVIEW applications.

        Returns:
            (str): The resolved error message for the current Error.

        """
        return self.dot_net_instance.ResolvedErrorMessage
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/clientapi/_factory.py sha256=eb18db115b84b60a0033668e3ca11dee3ca66b15a39be7472636c4111b28b3b9 bytes=7069 -->
## FILE: src/niveristand/clientapi/_factory.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/clientapi/_factory.py`
- sha256: `eb18db115b84b60a0033668e3ca11dee3ca66b15a39be7472636c4111b28b3b9`
- bytes: 7069

````python
from niveristand.clientapi._dotnetclasswrapperbase import _DotNetClassWrapperBase
from niveristand.clientapi._stimulusprofilesession import _StimulusProfileSession
from niveristand.clientapi._workspace2 import _Workspace2
from NationalInstruments.VeriStand.ClientAPI import (  # noqa: I100 .NET imports need to be out of order
    Factory as FactoryDotNet,
)


class _Factory(_DotNetClassWrapperBase):
    """
    Provides access to the NI VeriStand system and the various interfaces available in the Execution API.

    Any code you write using this API must include a Factory constructor to access NI VeriStand.

    """

    def __init__(self):
        super(_Factory, self).__init__(FactoryDotNet())

    def get_existing_stimulus_profile_session(self, gateway_ip_address, session_id):
        """
        Gets an instance that implements StimulusProfileSession interface.

        The instance can be used to automate the execution of an already deployed Stimulus Profile Session.

        Args:
            gateway_ip_address(str): Specifies the IP address of the VeriStand Gateway.
            session_id(str): Specifies the Session ID of the deployed Stimulus Profile Session.

        Returns:
            niveristand.clientapi._stimulusprofilesession._StimulusProfileSession : A StimulusProfileSession instance

        """
        pass

    def get_new_stimulus_profile_session(self, gateway_ip_address, name, sequences, description):
        """
        Gets an instance that implements StimulusProfileSession interface.

        The instance can be used to automate the execution of an already deployed Stimulus Profile Session.

        Args:
            gateway_ip_address(str): Specifies the IP address of the VeriStand Gateway.
            name(str): Specifies the name of the Stimulus Profile Session.
            sequences([niveristand.clientapi._sequencecallinfo._SequenceCallInfo]): Specifies the sequences to execute
             in the Stimulus Profile Session.
            description(str): Specifies a description for the Stimulus Profile Session.

        Returns:
            niveristand.clientapi._stimulusprofilesession._StimulusProfileSession : A StimulusProfileSession instance.

        """
        return _StimulusProfileSession(
            self._dot_net_instance.GetIStimulusProfileSession(
                gateway_ip_address,
                name,
                [seq_call_info.dot_net_instance for seq_call_info in sequences],
                description,
            )
        )

    def get_workspace2(self, gateway_ip_address):
        """
        Gets an instance that implements the Workspace2 interface.

        The instance can be used use to manage connections between the VeriStand Gateway and one or more targets,
         to start and stop data logging operations, and to configure events for error and status notifications.
          This method allows you to specify the IP address of the VeriStand Gateway.

        Args:
            gateway_ip_address (str): Specifies the IP address of the VeriStand Gateway.

        Returns:
            niveristand.clientapi._workspace2._Workspace2: A Workspace2 instance.

        """
        workspace2 = self._dot_net_instance.GetIWorkspace2(gateway_ip_address)
        return _Workspace2(workspace2)

    def get_localhost_workspace2(self):
        """
        Gets an instance that implements the Workspace2 interface.

        The instance can be used to manage connections between the VeriStand Gateway and one or more targets, to start
         and stop data logging operations, and to configure events for error and status notifications. This method
         assumes that the VeriStand Gateway is running on the localhost.

        Returns:
            niveristand.clientapi._workspace2._Workspace2: A Workspace2 instance.

        """
        workspace2 = self._dot_net_instance.GetIWorkspace2()
        return _Workspace2(workspace2)


class _DefaultGatewayFactory(object):
    """
    Provides access to the NI VeriStand system and the various interfaces available in the Execution API.

    All the instances that are created by this class are using the gateway at a default ip address. Any code you write
     using this API must include a Factory constructor to access NI VeriStand.

    """

    _default_gateway_ip_address = ""
    _default_workspace = None

    @classmethod
    def set_default_gateway_ip_address(cls, gateway_ip_address):
        """
        Sets the default ip address of the gateway.

        This ip address is to be used by work sessions that do not explicitly specify it for every operation.

        Args:
            gateway_ip_address (str): The default ip address of the VeriStand gateway.

        """
        cls._default_gateway_ip_address = gateway_ip_address
        cls._default_gateway = _Factory().get_workspace2(gateway_ip_address)

    @classmethod
    def get_default_gateway_ip_address(cls):
        """
        Gets the default ip address of the gateway.

        This ip address is to be used by default by work sessions that do not explicitly specify it for every operation.

        Returns:
            str: The default ip adderess of the VeriStand gateway.

        """
        return cls._default_gateway_ip_address

    @classmethod
    def get_new_stimulus_profile_session(cls, name, sequences, description):
        """
        Gets an instance that implements StimulusProfileSession interface.

        The instance can be used to automate the execution of an already deployed Stimulus Profile Session.

        Args:
            name(str): Specifies the name of the Stimulus Profile Session.
            sequences([niveristand.clientapi._sequencecallinfo._SequenceCallInfo]): Specifies the sequences to execute
             in the Stimulus Profile Session.
            description(str): Specifies a description for the Stimulus Profile Session.

        Returns:
            niveristand.clientapi._stimulusprofilesession._StimulusProfileSession : A StimulusProfileSession instance.

        """
        return _Factory().get_new_stimulus_profile_session(
            cls._default_gateway_ip_address, name, sequences, description
        )

    @classmethod
    def get_workspace2(cls):
        """
        Gets an instance that implements the Workspace2 interface.

        The instance can be used use to manage connections between the VeriStand Gateway and one or more targets,
         to start and stop data logging operations, and to configure events for error and status notifications.
          This method allows you to specify the IP address of the VeriStand Gateway.

        Returns:
            niveristand.clientapi._workspace2._Workspace2: A Workspace2 instance.

        """
        if cls._default_workspace is None:
            cls._default_workspace = _Factory().get_workspace2("")
        return cls._default_workspace
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/clientapi/_nodeinfo.py sha256=dc71d2c20761b42f4d34114e852e8c3b38bd8de4e980e2ac2df398879e6dcb53 bytes=1493 -->
## FILE: src/niveristand/clientapi/_nodeinfo.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/clientapi/_nodeinfo.py`
- sha256: `dc71d2c20761b42f4d34114e852e8c3b38bd8de4e980e2ac2df398879e6dcb53`
- bytes: 1493

````python
from niveristand import _errormessages, errors
from niveristand.clientapi._dotnetclasswrapperbase import _DotNetClassWrapperBase
from NationalInstruments.VeriStand.ClientAPI import (  # noqa: I100 .NET imports need to be out of order
    NodeInfo as NodeInfoDotNet,
)


class _NodeInfo(_DotNetClassWrapperBase):
    """
    Provides information about and configures a node in the system definition file.

    Args:
        dot_net_instance (NationalInstruments.VeriStand.ClientAPI.NodeInfo): the C# instance to wrap around.

    """

    def __init__(self, dot_net_instance):
        if isinstance(dot_net_instance, NodeInfoDotNet):
            super(_NodeInfo, self).__init__(dot_net_instance)
        else:
            raise errors.VeristandError(
                _errormessages.unexpected_dot_net_data_type
                % "NationalInstruments.VeriStand.ClientAPI.NodeInfo"
            )

    @property
    def channel_row_dimension(self):
        """
        Gets the number of rows in a channel node value.

        Returns:
            int: The number of rows in a channel node value.

        """
        return self._dot_net_instance.ChannelRowDimension

    @property
    def channel_column_dimension(self):
        """
        Gets the number of columns in a channel node value.

        Returns:
            int: The number of columns in a channel node value.

        """
        return self._dot_net_instance.ChannelColumnDimension
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/clientapi/_realtimesequencedefinitionapi/__init__.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: src/niveristand/clientapi/_realtimesequencedefinitionapi/__init__.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/clientapi/_realtimesequencedefinitionapi/__init__.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/clientapi/_realtimesequencedefinitionapi/erroraction.py sha256=31612bb6b28c6a1f61f4b3825a3d261627168e10306154bba209175f8f0355b3 bytes=390 -->
## FILE: src/niveristand/clientapi/_realtimesequencedefinitionapi/erroraction.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/clientapi/_realtimesequencedefinitionapi/erroraction.py`
- sha256: `31612bb6b28c6a1f61f4b3825a3d261627168e10306154bba209175f8f0355b3`
- bytes: 390

````python
from enum import Enum


class ErrorAction(Enum):
    """Actions you can take when calling :func:`niveristand.library.generate_error`."""

    ContinueSequenceExecution = 0  #: Continues execution but still fails the test run.
    StopSequence = 1  #: Stops execution and calls all try/finally blocks.
    AbortSequence = 2  #: Stops execution and avoid calling try/finally blocks.
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/clientapi/_sequencecallinfo.py sha256=77ea783e9285911ef40a031d0cf26bd5f2c6cf449e64d05c3a53206485e8095e bytes=2814 -->
## FILE: src/niveristand/clientapi/_sequencecallinfo.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/clientapi/_sequencecallinfo.py`
- sha256: `77ea783e9285911ef40a031d0cf26bd5f2c6cf449e64d05c3a53206485e8095e`
- bytes: 2814

````python
from niveristand import _errormessages, errors
from niveristand.clientapi._dotnetclasswrapperbase import _DotNetClassWrapperBase
from NationalInstruments.VeriStand.ClientAPI import (  # noqa: I100 .NET imports need to be out of order
    SequenceCallInfo as SequenceCallInfoDotNet,
)
from NationalInstruments.VeriStand.ClientAPI import SequenceParameterAssignmentInfo
import System


class _SequenceCallInfoFactory(object):
    """Factory class to create niveristand.clientapi._sequencecallinfo._SequenceCallInfo instances."""

    def __init__(self):
        pass

    @staticmethod
    def create(sequence_path, target, parameters, debug, timeout):
        """
        Creates an instance of niveristand.clientapi._sequencecallinfo._SequenceCallInfo class.

        Args:
            sequence_path (str): The file path of the sequence file to execute.
            target (str): The name of the target on which to execute the sequence.
            parameters (list[niveristand.clientapi._sequenceparameterassignmentinfo._SequenceParameterAssignmentInfo]):
             The parameter assignments for the sequence.
            debug (bool): Whether the sequence executes in debug mode.
            timeout (float): The timeout in milliseconds within which the sequence must complete each time step.

        Returns:
            niveristand.clientapi._sequencecallinfo._SequenceCallInfo: Newly created instance.

        """
        if target is None:
            target = ""
        target = System.String(target)
        sequence_path = System.String(sequence_path)
        debug = System.Boolean(debug)
        timeout = System.Double(timeout)
        parameters_dot_net = [parameter.dot_net_instance for parameter in parameters]
        parameters_dot_net_array = System.Array[SequenceParameterAssignmentInfo](parameters_dot_net)
        sequence_call_info_dot_net = SequenceCallInfoDotNet(
            sequence_path, target, parameters_dot_net_array, debug, timeout
        )
        sequence_call_info = _SequenceCallInfo(sequence_call_info_dot_net)
        return sequence_call_info


class _SequenceCallInfo(_DotNetClassWrapperBase):
    """
    Provides information about a stimulus profile sequence.

    Args:
        dot_net_instance (NationalInstruments.VeriStand.ClientAPI.SequenceCallInfo): the C# instance to wrap around.

    """

    def __init__(self, dot_net_instance):
        if isinstance(dot_net_instance, SequenceCallInfoDotNet):
            super(_SequenceCallInfo, self).__init__(dot_net_instance)
        else:
            raise errors.VeristandError(
                _errormessages.unexpected_dot_net_data_type
                % "NationalInstruments.VeriStand.ClientAPI."
                "SequenceCallInfo"
            )
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/clientapi/_sequenceparameterassignmentinfo.py sha256=676fd5bc45f8a530d6938fee4503421c73388fa707d88ffd1fb56ec5ca0b9b6b bytes=2795 -->
## FILE: src/niveristand/clientapi/_sequenceparameterassignmentinfo.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/clientapi/_sequenceparameterassignmentinfo.py`
- sha256: `676fd5bc45f8a530d6938fee4503421c73388fa707d88ffd1fb56ec5ca0b9b6b`
- bytes: 2795

````python
from niveristand import _errormessages, errors
from niveristand.clientapi._datatypes.rtprimitives import ChannelReference, DataType
from niveristand.clientapi._dotnetclasswrapperbase import _DotNetClassWrapperBase
from niveristand.clientapi._systemdefinitionchannelresource import (
    _SystemDefinitionChannelResourceFactory,
)
from NationalInstruments.VeriStand.ClientAPI import (  # noqa: I100 .NET imports need to be out of order
    SequenceParameterAssignmentInfo as SequenceParameterAssignmentInfoDotNet,
)


class _SequenceParameterAssignmentInfoFactory(object):
    """
    Factory class.

    Creates niveristand.clientapi._sequenceparameterassignmentinfo._SequenceParameterAssignmentInfo instances.

    """

    def __init__(self):
        pass

    @staticmethod
    def create(parameter_name, value):
        """
        Creates an instance.

        The instance is of type niveristand.clientapi._sequenceparameterassignmentinfo._SequenceParameterAssignmentInfo.

        Args:
            parameter_name (): The name of the parameter.
            value (niveristand.clientapi.DataType): The value of the parameter.

        Returns:
            niveristand.clientapi._sequenceparameterassignmentinfo._SequenceParameterAssignmentInfo: Newly created
             instance.

        """
        if isinstance(value, ChannelReference):
            sysdef_ch_res = _SystemDefinitionChannelResourceFactory.create(value._channel_name)
            data_resource_dot_net = sysdef_ch_res.dot_net_instance
        elif isinstance(value, DataType):
            data_resource_dot_net = value._data_value
        else:
            raise ValueError

        seq_param_assignment_info_dot_net = SequenceParameterAssignmentInfoDotNet(
            parameter_name, data_resource_dot_net
        )
        seq_param_assignment_info = _SequenceParameterAssignmentInfo(
            seq_param_assignment_info_dot_net
        )
        return seq_param_assignment_info


class _SequenceParameterAssignmentInfo(_DotNetClassWrapperBase):
    """
    Provides information about an input parameter of a real-time sequence.

    Args:
        dot_net_instance (NationalInstruments.VeriStand.ClientAPI.SequenceParameterAssignmentInfo): the C# instance to
         wrap around.

    """

    def __init__(self, dot_net_instance):
        if isinstance(dot_net_instance, SequenceParameterAssignmentInfoDotNet):
            super(_SequenceParameterAssignmentInfo, self).__init__(dot_net_instance)
        else:
            raise errors.VeristandError(
                _errormessages.unexpected_dot_net_data_type
                % "NationalInstruments.VeriStand.ClientAPI."
                "SequenceParameterAssignmentInfo"
            )
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/clientapi/_stimulusprofilesession.py sha256=e4b2d94eff37df0bc686b20d9c9362503b56db8d5ac280a94aa4c83ac82145c9 bytes=3854 -->
## FILE: src/niveristand/clientapi/_stimulusprofilesession.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/clientapi/_stimulusprofilesession.py`
- sha256: `e4b2d94eff37df0bc686b20d9c9362503b56db8d5ac280a94aa4c83ac82145c9`
- bytes: 3854

````python
from niveristand import _errormessages, errors
from niveristand import _internal
from niveristand.clientapi._dotnetclasswrapperbase import _DotNetClassWrapperBase
from niveristand.clientapi._error import _Error
from NationalInstruments.VeriStand.ClientAPI import (  # noqa: I100 .NET imports need to be out of order
    ISequenceControl as ISequenceControlDotNet,
)
from NationalInstruments.VeriStand.ClientAPI import (
    IStimulusProfileSession as IStimulusProfileSessionDotNet,
)

_internal.dummy()


class _StimulusProfileSession(_DotNetClassWrapperBase):
    """
    Interface to control and monitor Stimulus Profile Session execution.

    Args:
        dot_net_instance (NationalInstruments.VeriStand.ClientAPI.StimulusProfileSessionImpl): the C# instance to wrap.
         around.

    """

    def __init__(self, dot_net_instance):
        if isinstance(dot_net_instance, IStimulusProfileSessionDotNet):
            super(_StimulusProfileSession, self).__init__(dot_net_instance)
        else:
            raise errors.VeristandError(
                _errormessages.unexpected_dot_net_data_type
                % "NationalInstruments.VeriStand.ClientAPI."
                "IStimulusProfileSession"
            )

    def __getitem__(self, item):
        """
        Gets a reference to the sequence specified by the qualified sequence name in the Stimulus Profile Session.

        Args:
            item (str): The sequence for which to get the reference.

        Returns:
            niveristand.clientapi._stimulusprofilesession._SequenceControl: Sequence control reference.

        """
        sequence_control = self._dot_net_instance[item]
        return _SequenceControl(sequence_control)

    def deploy(self, auto_start):
        """
        Deploys the Stimulus Profile Session.

        Args:
            auto_start (bool): If True, starts sequences immediately upon deploy. If False, waits for an external Run
             command.

        Returns:
            str: The ID of the Stimulus profile session.

        """
        session_id, err = self._dot_net_instance.Deploy(auto_start, None, None)
        err = _Error(err)
        if err.is_error:
            raise errors.VeristandError(
                _errormessages.csharp_call_failed % (err.error_code, err.resolved_error_message)
            )
        return session_id

    def undeploy(self):
        """
        Undeploys the Stimulus Profile Session.

        Returns:
            None:

        """
        err = self._dot_net_instance.Undeploy(None)
        err = _Error(err)
        if err.is_error:
            raise errors.VeristandError(
                _errormessages.csharp_call_failed % (err.error_code, err.resolved_error_message)
            )


class _SequenceControl(_DotNetClassWrapperBase):
    """
    Automates and monitors the execution of a sequence in a stimulus profile session.

    Args:
        dot_net_instance (NationalInstruments.VeriStand.ClientAPI.SequenceControl): the C# instance to wrap.

    """

    def __init__(self, dot_net_instance):
        if isinstance(dot_net_instance, ISequenceControlDotNet):
            super(_SequenceControl, self).__init__(dot_net_instance)
        else:
            raise errors.VeristandError(
                _errormessages.unexpected_dot_net_data_type
                % "NationalInstruments.VeriStand.ClientAPI."
                "ISequenceControl"
            )

    def register_sequence_complete_event_handler(self, handler):
        """
        Register callback for when a sequence completes execution.

        Args:
            handler (method): The callback function.

        Returns:
            None:

        """
        self._dot_net_instance.SequenceComplete += handler
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/clientapi/_systemdefinitionchannelresource.py sha256=5594c16389ff6c5b334fba721d09654c9fb67679afe0828b3386f5051f9fce44 bytes=1928 -->
## FILE: src/niveristand/clientapi/_systemdefinitionchannelresource.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/clientapi/_systemdefinitionchannelresource.py`
- sha256: `5594c16389ff6c5b334fba721d09654c9fb67679afe0828b3386f5051f9fce44`
- bytes: 1928

````python
from niveristand import _errormessages, errors
from niveristand.clientapi._dotnetclasswrapperbase import _DotNetClassWrapperBase
from NationalInstruments.VeriStand.Data import (  # noqa: I100 .NET imports need to be out of order
    SystemDefinitionChannelResource as SystemDefinitionChannelResourceDotNet,
)


class _SystemDefinitionChannelResourceFactory(object):
    """
    Factory class.

    Creates niveristand.clientapi._systemdefinitionchannelresource._SystemDefinitionChannelResource instances.

    """

    def __init__(self):
        pass

    @staticmethod
    def create(channel):
        """
        Creates an instance.

        The instance is of type niveristand.clientapi._systemdefinitionchannelresource._SystemDefinitionChannelResource.

        Args:
            channel (str): The channel to map the data resource to in the system definition file.

        Returns:
            niveristand.clientapi._systemdefinitionchannelresource._SystemDefinitionChannelResource: The newly created
             instance.

        """
        return _SystemDefinitionChannelResource(SystemDefinitionChannelResourceDotNet(channel))


class _SystemDefinitionChannelResource(_DotNetClassWrapperBase):
    """
    Represents a data resource mapped to a system definition channel.

    Args:
        dot_net_instance (NationalInstruments.VeriStand.ClientAPI.SystemDefinitionChannelResource): the C# instance to
         wrap around.

    """

    def __init__(self, dot_net_instance):
        if isinstance(dot_net_instance, SystemDefinitionChannelResourceDotNet):
            super(_SystemDefinitionChannelResource, self).__init__(dot_net_instance)
        else:
            raise errors.VeristandError(
                _errormessages.unexpected_dot_net_data_type % "NationalInstruments.VeriStand.Data."
                "SystemDefinitionChannelResource"
            )
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/clientapi/_workspace2.py sha256=5a2875f5096e363486c6aa50fbb2bc7991965d8eea709e5363f5b619256f94c8 bytes=4909 -->
## FILE: src/niveristand/clientapi/_workspace2.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/clientapi/_workspace2.py`
- sha256: `5a2875f5096e363486c6aa50fbb2bc7991965d8eea709e5363f5b619256f94c8`
- bytes: 4909

````python
from niveristand import _errormessages, errors
from niveristand.clientapi._dotnetclasswrapperbase import _DotNetClassWrapperBase
from niveristand.clientapi._error import _Error
from niveristand.clientapi._nodeinfo import _NodeInfo
from NationalInstruments.VeriStand.ClientAPI import (  # noqa: I100 .NET imports need to be out of order
    IWorkspace2 as IWorkspace2DotNet,
)


class _Workspace2(_DotNetClassWrapperBase):
    """
    Class to perform basic workspace operations, such as getting, setting, and logging channel data.

    Args:
        dot_net_instance (NationalInstruments.VeriStand.ClientAPI.WorkspaceImpl): the C# instance to wrap around.

    """

    def __init__(self, dot_net_instance):
        if isinstance(dot_net_instance, IWorkspace2DotNet):
            super(_Workspace2, self).__init__(dot_net_instance)
        else:
            raise errors.VeristandError(
                _errormessages.unexpected_dot_net_data_type
                % "NationalInstruments.VeriStand.ClientAPI.IWorkspace2"
            )

    def get_channel_vector_values(self, channel):
        """
        Gets the vector values of a channel on the target.

        Args:
            channel (): The name of the channel. You must enter the full path to the channel as specified in the system
             definition file.

        Returns:
            int: The number of rows in the vector array.
            int: The number of columns in the vector array.
            [float]: The vector values.

        """
        err, row_dim, col_dim, value = self._dot_net_instance.GetChannelVectorValues(channel)
        err = _Error(err)
        if err.is_error:
            raise errors.VeristandError(
                _errormessages.csharp_call_failed % (err.error_code, err.resolved_error_message)
            )
        return row_dim, col_dim, value

    def get_multiple_system_nodes_data(self, names):
        """
        Gets information about multiple nodes in the system definition file.

        Args:
            names ([str]): The names of the nodes. You must enter the full path to each node as specified in the system
             definition file.

        Returns:
            niveristand.clientapi._nodeinfo._NodeInfo: Information about the nodes.

        """
        err, node_infos = self._dot_net_instance.GetMultipleSystemNodesData(names, None)
        err = _Error(err)
        if err.is_error:
            raise errors.VeristandError(
                _errormessages.csharp_call_failed % (err.error_code, err.resolved_error_message)
            )
        return [_NodeInfo(node_info) for node_info in node_infos]

    def get_single_channel_value(self, name):
        """
        Gets the value of a single channel on the target.

        Args:
            name (str): The name of the channel. You must enter the full path to the channel as specified in the system
             definition file.

        Returns:
            float: The value of the specified channel.

        """
        err, value = self._dot_net_instance.GetSingleChannelValue(name, 0)
        err = _Error(err)
        if err.is_error:
            raise errors.VeristandError(
                _errormessages.csharp_call_failed % (err.error_code, err.resolved_error_message)
            )
        return value

    def set_channel_vector_values(self, channel, new_values):
        """
        Sets the vector values of a channel on the target.

        Args:
            channel (str): The name of the channel. You must enter the full path to the channel as specified in the
             system definition file.
            new_values (List[float]): The vector values. This parameter expects a 1D array. If the channel expects
             two-dimensional data, convert the 2D channel data into a 1D array before passing it to this method.

        """
        err = self._dot_net_instance.SetChannelVectorValues(channel, new_values)
        err = _Error(err)
        if err.is_error:
            raise errors.VeristandError(
                _errormessages.csharp_call_failed % (err.error_code, err.resolved_error_message)
            )

    def set_single_channel_value(self, name, new_val):
        """
        Sets the value of a single channel on the target.

        Args:
            name (str): The name of the channel. You must enter the full path to the channel as specified in the system
             definition file.
            new_val (float): The value to set.

        Returns:
            None:

        """
        err = self._dot_net_instance.SetSingleChannelValue(name, new_val)
        err = _Error(err)
        if err.is_error:
            raise errors.VeristandError(
                _errormessages.csharp_call_failed % (err.error_code, err.resolved_error_message)
            )
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/clientapi/realtimesequence.py sha256=3900c905c4e2ecf9e760dd3af9448719a0c786b5b5200d03d562eeb489d23ed6 bytes=7441 -->
## FILE: src/niveristand/clientapi/realtimesequence.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/clientapi/realtimesequence.py`
- sha256: `3900c905c4e2ecf9e760dd3af9448719a0c786b5b5200d03d562eeb489d23ed6`
- bytes: 7441

````python
import ast
import inspect
import os
import tempfile

from niveristand import _errormessages
from niveristand._translation import utils
from niveristand._translation.py2rtseq.utils import Resources
from niveristand.clientapi import realtimesequencedefinition as rtseqapi
from niveristand.clientapi import rtsequencedefinitionutils as rtsequtils
from niveristand.errors import TranslateError, VeristandError
from NationalInstruments.VeriStand.Data import (  # noqa: I100 .NET imports need to be out of order
    SystemDefinitionChannelResource,
)
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import (
    ChannelReferenceDeclaration,
    ChannelSizeType,
)
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import EvaluationMethod
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import ParameterDeclaration
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import Reference
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import References


class RealTimeSequence:
    """
    A real-time sequence that can run on the VeriStand Engine.

    Args:
        top_level_func: the function to transform.
        rtseq_pkg(:class:`RealTimeSequencePackage`): the containing package in case you want to add this sequence to a
                                                    library.
        target: The name of the target on which to deploy or run the real-time sequence.
         If None, the default target is used.

    Raises:
        :class:`niveristand.errors.TranslateError`: if translation fails.
        :class:`niveristand.errors.VeristandError`: if compilation fails.

    """

    def __init__(self, top_level_func, rtseq_pkg=None, target=None):
        self._top_level_func = top_level_func
        self._path = ""
        self._rtseq = None
        self._rtseqpkg = rtseq_pkg
        self._ref = list()
        self.target = target
        # finally, initialize the transform
        self._transform()

    def run(self, rtseq_params={}):
        """
        Runs the sequence on the globally configured VeriStand Engine.

        Args:
            rtseq_params (Dict[str, niveristand.clientapi._datatypes.rtprimitives.DoubleValue]):  the parameters to be
             passed to the RT sequence.

        Returns:
            niveristand.clientapi.stimulusprofileapi.StimulusProfileState: Stimulus profile session state.

        Deploys and runs the sequence without waiting for the sequence to finish. Use the returned
        :class:`StimulusProfileState` to wait for the sequence to complete and obtain the return value.

        For a simpler use case, refer to :func:`niveristand.realtimesequencetools.run_py_as_rtseq`

        """
        if self._rtseq is None:
            raise VeristandError(_errormessages.run_without_valid_sequence)
        if self._path is None:
            raise VeristandError(_errormessages.invalid_path_for_sequence)

        name = self._build_file_name()
        return rtseqapi.run_rt_sequence(name, rtseq_params, target=self.target)

    def save(self, path=None):
        """
        Saves this sequence to disk.

        Args:
            path(Optional[str]): path to the location you want to save the sequence file.

        Returns:
            path you specify in **path**.

        All dependencies required for deployment of this sequence save to the same path.
        If you do not specify a path in **path**, this sequence saves to the location where you last saved the object.
        If you did not previously save the object, it saves to a temporary folder.

        For a simpler use case, refer to :func:`niveristand.realtimesequencetools.save_py_as_rtseq`

        """
        if self._rtseq is None:
            raise VeristandError(_errormessages.save_without_valid_sequence)
        if path is not None:
            self._path = os.path.abspath(path)
        elif not os.path.isdir(self._path):
            self._path = tempfile.mkdtemp()

        name = self._build_file_name()
        self._rtseqpkg.save_referenced(self._path, self)
        self._update_references()
        rtseqapi.save_real_time_sequence(self._rtseq, name)
        return name

    def _transform(self):
        from niveristand._decorators import rt_seq_mode_id

        real_obj = getattr(self._top_level_func, rt_seq_mode_id, None)
        if real_obj is None:
            raise TranslateError(_errormessages.invalid_top_level_func)
        src = inspect.getsource(real_obj)
        top_node = ast.parse(src)
        try:
            func_node = top_node.body[0]
        except TypeError:
            func_node = None
        if func_node is None or not isinstance(func_node, ast.FunctionDef):
            raise TranslateError(_errormessages.invalid_top_level_func)

        self._rtseq = rtseqapi.create_real_time_sequence()
        transform_resources = Resources(self._rtseq, str(self))
        if self._rtseqpkg is not None:
            transform_resources.set_dependency_pkg(self._rtseqpkg)
        utils.generic_ast_node_transform(func_node, transform_resources)
        self._rtseqpkg = transform_resources.get_dependency_pkg()
        self._rtseqpkg.append(inspect.getmodule(real_obj))
        self._update_parameters(transform_resources.get_parameters())
        self._update_channel_refs(transform_resources.get_all_channel_refs())
        self.save()
        rtsequtils.compile_rtseq(self._rtseq)

    def _update_references(self):
        self._ref.append(Reference(str(self), self._build_file_name()))
        self._rtseq.References = References()
        for referenced in self._rtseqpkg.get_referenced(self):
            self._rtseq.References.AddReference(referenced.get_reference().pop())

    def _update_parameters(self, param_list):
        self._rtseq.Variables.Parameters.ClearParameters()
        for param in param_list:
            real_default = param.default_value._data_value
            real_eval_method = (
                EvaluationMethod.ByValue if param.by_value else EvaluationMethod.ByReference
            )
            real_param = ParameterDeclaration(param.rtseq_name, real_default, real_eval_method)
            self._rtseq.Variables.Parameters.AddParameter(real_param)

    def _update_channel_refs(self, channel_ref_list):
        self._rtseq.Variables.ChannelReferences.ClearChannelReferences()
        for channel_ref_obj in channel_ref_list:
            if channel_ref_obj.channel_is_vector:
                size_argument = ChannelSizeType.Vector
            else:
                size_argument = ChannelSizeType.Scalar
            system_definition_channel_resource = SystemDefinitionChannelResource(
                channel_ref_obj.channel_name
            )
            channel_reference_declaration = ChannelReferenceDeclaration(
                channel_ref_obj.rtseq_name, system_definition_channel_resource, size_argument
            )
            self._rtseq.Variables.ChannelReferences.AddChannelReference(
                channel_reference_declaration
            )

    def _build_file_name(self):
        return os.path.join(self._path, str(self) + ".nivsseq")

    def get_reference(self):
        return self._ref

    def __str__(self):
        return self._top_level_func.__name__
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/clientapi/realtimesequencedefinition.py sha256=e1ed56bfa00678c125f2b18156bdad033dea512ec2b3296673df3f12185a7dce bytes=5471 -->
## FILE: src/niveristand/clientapi/realtimesequencedefinition.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/clientapi/realtimesequencedefinition.py`
- sha256: `e1ed56bfa00678c125f2b18156bdad033dea512ec2b3296673df3f12185a7dce`
- bytes: 5471

````python
import os
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import ErrorAction
from niveristand import _errormessages, errors
from niveristand import _internal
from niveristand._translation.py2rtseq.utils import _py_param_name_to_rtseq_param_name
from niveristand.clientapi import stimulusprofileapi
from niveristand.clientapi._factory import _DefaultGatewayFactory
from niveristand.clientapi._sequencecallinfo import _SequenceCallInfoFactory
from niveristand.clientapi._sequenceparameterassignmentinfo import (
    _SequenceParameterAssignmentInfoFactory,
)
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import (  # noqa: I100 .NET imports out of order
    Expression,
)
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import ForEachLoop
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import ForLoop
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import GenerateError
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import IfElse
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import LocalDeclaration
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import Multitask
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import RealTimeSequence
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import ReturnDeclaration
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import StopTask
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import Task
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import WhileLoop
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import Yield
from System.IO import IOException


_internal.dummy()

factory = None
workspace = None


def add_local_variable(rt_seq, name, value):
    name = _create_unique_lv_name(name)
    local_declaration = LocalDeclaration(name, value._data_value)
    rt_seq.Variables.LocalVariables.AddLocalVariable(local_declaration)
    return name


def add_assignment(block, dest_name, source_name):
    add_expression(block, "%s = %s" % (dest_name, source_name))


def add_expression(block, expression):
    block.AddStatement(Expression("%s" % expression))


def add_yield(block):
    block.AddStatement(Yield())


def add_if_else(block, test_condition):
    if_else = IfElse(Expression(test_condition))
    block.AddStatement(if_else)
    return if_else


def add_for_loop(block, loop_variable, iterations):
    for_loop = ForLoop(loop_variable, Expression(str(iterations)), False)
    block.AddStatement(for_loop)
    return for_loop


def add_foreach_loop(block, loop_variable, iterations):
    foreach_loop = ForEachLoop(loop_variable, Expression(str(iterations)), False)
    block.AddStatement(foreach_loop)
    return foreach_loop


def add_while(block, test_condition):
    while_block = WhileLoop(Expression(test_condition), False)
    block.AddStatement(while_block)
    return while_block


def add_multi_task(block):
    multi_task = Multitask()
    block.AddStatement(multi_task)
    return multi_task


def add_task(multi_task, name):
    task = Task(name)
    multi_task.AddTask(task)
    return task.Body


def create_real_time_sequence():
    return RealTimeSequence()


def add_return_variable(rtseq, name, default_value):
    name = _create_unique_lv_name(name)
    return_declaration = ReturnDeclaration(name, default_value._data_value)
    rtseq.Variables.ReturnType = return_declaration
    return name


def add_generate_error(block, code, message, action):
    block.AddStatement(GenerateError(code, message, ErrorAction(action)))


def add_stop_task(block, taskname):
    block.AddStatement(StopTask(taskname))


def save_real_time_sequence(rtseq, filepath):
    try:
        rtseq.SaveSequence(os.path.join(filepath))
    except IOException as e:
        raise IOError(e.Message)


def _create_unique_lv_name(name):
    try:
        _create_unique_lv_name.lv_cnt += 1
    except AttributeError:
        _create_unique_lv_name.lv_cnt = 0
    if name is None:
        name = ""
    name = "lv_" + name + "_" + str(_create_unique_lv_name.lv_cnt)
    _create_unique_lv_name.lv_cnt += 1
    return name


def to_channel_ref_name(name):
    return "ch_" + name


def _get_channel_node_info(name, node_info_list):
    for channel in node_info_list:
        if channel.FullPath == name:
            return channel
    raise errors.VeristandError(_errormessages.channel_not_found % name)


def run_rt_sequence(rt_sequence_path, rtseq_params, target=None):
    rtseq_params = [
        _SequenceParameterAssignmentInfoFactory.create(
            _py_param_name_to_rtseq_param_name(key), rtseq_params[key]
        )
        for key in rtseq_params
    ]
    seq_call_info = _SequenceCallInfoFactory.create(
        rt_sequence_path, target, rtseq_params, False, 100000
    )
    session = _DefaultGatewayFactory.get_new_stimulus_profile_session(
        rt_sequence_path, [seq_call_info], ""
    )
    sequence_control = session[os.path.splitext(os.path.basename(rt_sequence_path))[0] + ":1"]
    state = stimulusprofileapi.StimulusProfileState(session)
    sequence_control.register_sequence_complete_event_handler(
        state._sequence_complete_event_handler
    )
    session.deploy(True)
    return state
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/clientapi/realtimesequencepkg.py sha256=8534819f77d8c970a9b3a96c147bb03db3313d3140239653d96cd704a286749b bytes=4168 -->
## FILE: src/niveristand/clientapi/realtimesequencepkg.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/clientapi/realtimesequencepkg.py`
- sha256: `8534819f77d8c970a9b3a96c147bb03db3313d3140239653d96cd704a286749b`
- bytes: 4168

````python
import collections.abc
import inspect
from niveristand import _errormessages
from niveristand._decorators import rt_seq_mode_id
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError


class RealTimeSequencePkg(collections.abc.MutableMapping):
    def __init__(self):
        self._rtseqs = dict()
        self._dep_graph = dict()

    def save_all(self, path):
        for seq in self:
            self[seq].save(path)

    def save_referenced(self, path, referencer):
        for seq in self.get_referenced(referencer):
            if seq is None:
                raise TranslateError(_errormessages.dependency_not_found)
            seq.save(path)

    def add_referenced_sequence(self, referencer, referenced_sequence):
        referencer_name = self._obj_to_key(referencer)
        referenced_sequence = self._obj_to_key(referenced_sequence)
        if referencer_name not in self._dep_graph:
            self._dep_graph[referencer_name] = list()
        if referenced_sequence not in self._dep_graph[referencer_name]:
            self._dep_graph[referencer_name].append(referenced_sequence)

    def get_referenced(self, referencer):
        referencer = self._obj_to_key(referencer)
        return [self._try_resolve(dep_name) for dep_name in self._dep_graph[referencer]]

    def __len__(self):
        return len(self._rtseqs)

    def __getitem__(self, item):
        item = self._obj_to_key(item)
        seq = self._try_resolve(item)
        if seq is None:
            raise TranslateError(_errormessages.dependency_not_found)
        return self._rtseqs.get(item)

    def _obj_to_key(self, item):
        return str(item) if not inspect.isfunction(item) else item.__name__

    def _try_resolve(self, item):
        seq = self._rtseqs.get(item)
        if inspect.isfunction(seq):
            for dep in self._dep_graph[item]:
                if not isinstance(self._rtseqs[dep], RealTimeSequence):
                    self._try_resolve(item)
            seq = RealTimeSequence(seq, self)
            self._rtseqs[item] = seq
        return seq

    def __contains__(self, item):
        if self._obj_to_key(item) in self._rtseqs:
            return True
        return False

    def append(self, new):
        funcs_to_add = list()
        if inspect.isfunction(new) or isinstance(new, RealTimeSequence):
            funcs_to_add.append(new)
        elif inspect.ismodule(new):
            for func_name, func in inspect.getmembers(new, inspect.isfunction):
                if getattr(func, rt_seq_mode_id, None) is not None:
                    funcs_to_add.append(func)
        else:
            raise VeristandError()
        for func in [f for f in funcs_to_add if self._obj_to_key(f) not in self._rtseqs]:
            name = func.__name__
            self._rtseqs[name] = func
            if name not in self._dep_graph:
                self._dep_graph[name] = list()

    def count(self):
        len(self._rtseqs)

    def __iter__(self):
        return self._rtseqs.__iter__()

    def __setitem__(self, key, value):
        raise VeristandError()

    def __delitem__(self, key):
        raise VeristandError()

    def __reversed__(self):
        raise NotImplementedError

    def __index__(self):
        raise NotImplementedError()

    def extend(self):
        raise NotImplementedError()

    def insert(self):
        raise NotImplementedError()

    def pop(self, key, default=object()):
        raise NotImplementedError()

    def remove(self):
        raise NotImplementedError()

    def sort(self):
        raise NotImplementedError()

    def __add__(self, other):
        raise NotImplementedError()

    def __radd__(self, other):
        raise NotImplementedError()

    def __iadd__(self, other):
        raise NotImplementedError()

    def __mul__(self, other):
        raise NotImplementedError()

    def __imul__(self, other):
        raise NotImplementedError()

    def __rmul__(self, other):
        raise NotImplementedError()
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/clientapi/rtsequencedefinitionutils.py sha256=4a62e0b386e569ee60ae2628e92f6de7834426e62014dec6b01bde10c2a477f7 bytes=629 -->
## FILE: src/niveristand/clientapi/rtsequencedefinitionutils.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/clientapi/rtsequencedefinitionutils.py`
- sha256: `4a62e0b386e569ee60ae2628e92f6de7834426e62014dec6b01bde10c2a477f7`
- bytes: 629

````python
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import CompilationEventType
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApiUtilities import CompilerUtilities
from niveristand import _internal
from niveristand.errors import VeristandError

_internal.dummy()


def compile_rtseq(rtseq):
    success, _, compilation_events = CompilerUtilities.TryGetCompiledInstance(rtseq, False, [], [])
    if not success:
        errormsg = " ".join(
            [x.Message for x in compilation_events if x.EventType == CompilationEventType.Error]
        )
        raise VeristandError(errormsg)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/clientapi/stimulusprofileapi.py sha256=f8113b1bd0ff145f6ae2bcc5b83f4cd93a2e0a6314912ba9b97d2ad6b37956ef bytes=3616 -->
## FILE: src/niveristand/clientapi/stimulusprofileapi.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/clientapi/stimulusprofileapi.py`
- sha256: `f8113b1bd0ff145f6ae2bcc5b83f4cd93a2e0a6314912ba9b97d2ad6b37956ef`
- bytes: 3616

````python
from enum import Enum
import time
from niveristand import _errormessages
from niveristand import _internal
from niveristand.errors import SequenceError, VeristandError
from NationalInstruments.VeriStand.Data import (  # noqa: I100 .NET imports need to be out of order
    DataType,
)

_internal.dummy()


class StimulusProfileState(object):
    """Contains the execution state of a real-time sequence."""

    class CompletionState(Enum):
        """Enum used for possible completion states."""

        Success = 0  #: operation ran to completion successfully. No errors occurred.
        Aborted = 1  #: operation stopped forcefully.
        Failed = 2  #: operation ran to completion, but an error occurred.

    def __init__(self, session):
        self._ret_val = None
        self._rt_sequence_completed = False
        self._completion_state = None
        self._session = session
        self._last_error = None

    @property
    def last_error(self):
        """
        Returns the last error generated by the sequence.

        Returns:
            :class:`niveristand.errors.SequenceError`: final error the sequence generated.

        """
        return self._last_error

    @property
    def ret_val(self):
        """
        Returns the return value of the sequence.

        Returns:
            (bool, int, float): the return value of the sequence.

        """
        return self._ret_val

    @property
    def completion_state(self):
        """
        Returns the state after running.

        Returns:
            :class:`CompletionState`: state after the operation runs to completion. `None` if unfinished.

        """
        return self._completion_state

    @property
    def session(self):
        """
        Returns the session you created to execute this sequence.

        Returns:
            a session connected to the VeriStand Engine.

        """
        return self._session

    def _sequence_complete_event_handler(self, source, args):
        from niveristand.clientapi import ErrorAction

        data_value = args.ReturnValue
        if data_value.Type == DataType.Void:
            self._ret_val = None
        elif data_value.Type in [
            DataType.Boolean,
            DataType.Double,
            DataType.Int32,
            DataType.Int64,
            DataType.UInt32,
            DataType.UInt64,
        ]:
            self._ret_val = data_value.Value
        else:
            raise VeristandError(_errormessages.invalid_return_type)
        aborted = args.Aborted
        error = args.Error
        if aborted:
            self._completion_state = StimulusProfileState.CompletionState.Aborted
            self._last_error = SequenceError(error.Code, error.Message, ErrorAction.AbortSequence)
        else:
            if error.Code != 0:
                self._completion_state = StimulusProfileState.CompletionState.Failed
                self._last_error = SequenceError(
                    error.Code, error.Message, ErrorAction.ContinueSequenceExecution
                )
            else:
                self._completion_state = StimulusProfileState.CompletionState.Success
        self._rt_sequence_completed = True

    def wait_for_result(self):
        """
        Waits for the sequence to finish running.

        Returns:
            the value returned by the VeriStand Engine after this sequence runs.

        """
        while not self._rt_sequence_completed:
            time.sleep(0.01)
        return self._ret_val
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/customdevice/__init__.py sha256=095c0c8403e6a1eb5c9938c63c70e6c338dca829fbece9322d98af9f820fd41f bytes=158 -->
## FILE: src/niveristand/customdevice/__init__.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/customdevice/__init__.py`
- sha256: `095c0c8403e6a1eb5c9938c63c70e6c338dca829fbece9322d98af9f820fd41f`
- bytes: 158

````python
"""Module for NationalInstruments.VeriStand.CustomDevice."""
### AUTO-GENERATED CODE - DO NOT MODIFY DIRECTLY ###

from ._auto_generated_classes import *
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/customdevice/_auto_generated_classes.py sha256=80e7ed4e660259522bf36cce2b4c6db3d38751f72876d41930ae73021e2db94d bytes=5873 -->
## FILE: src/niveristand/customdevice/_auto_generated_classes.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/customdevice/_auto_generated_classes.py`
- sha256: `80e7ed4e660259522bf36cce2b4c6db3d38751f72876d41930ae73021e2db94d`
- bytes: 5873

````python
"""Module for NationalInstruments.VeriStand.CustomDevice."""
### AUTO-GENERATED CODE - DO NOT MODIFY DIRECTLY ###

from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, Optional, overload, Sequence, Tuple, Union

import clr

clr.AddReference("NationalInstruments.VeriStand.XMLReader")
import NationalInstruments.VeriStand  # type: ignore
import NationalInstruments.VeriStand.CustomDevice  # type: ignore
import System  # type: ignore

from .. import *


class _staticproperty(staticmethod):
    def __get__(self, *_):
        return self.__func__()


class _DotNetBase:
    def __eq__(self, other) -> bool:
        return self._dotnet_instance == other._dotnet_instance if isinstance(other, _DotNetBase) else False

    def __repr__(self) -> str:
        qualname = type(self).__qualname__
        return f"<niveristand.customdevice.{qualname}{self._custom_repr()} object at {hex(id(self))}>"

    def _custom_repr(self) -> str:
        return ""


class _DotNetEnum(_DotNetBase):
    def __repr__(self) -> str:
        return f"<niveristand.customdevice.{type(self).__qualname__}.{self._py_field_name}: {int(self)}>"

    def __str__(self) -> str:
        return f"{type(self).__qualname__}.{self._py_field_name}"

    def __int__(self) -> int:
        return int(self._dotnet_instance)


def _is_iterable(arg: Any) -> bool:
    return not isinstance(arg, str) and isinstance(arg, Iterable)


def _unwrap(out_params: Dict[Optional[Tuple[str, ...]], Tuple[int, Any]], *args: Tuple[Any]) -> Iterable[Any]:
    insertion_index = -1
    if out_params:
        use_out_param = False
        for signature, out_param in out_params.items():
            if not signature:
                use_out_param = True
            elif len(args) == len(signature):
                use_out_param = True
                for arg, sig_type in zip(args, signature):
                    if not isinstance(arg, sig_type):
                        use_out_param = False
                        break
            if use_out_param:
                insertion_index, insertion_value = out_param
                break

    for index, arg in enumerate(args):
        # insert the extra value then continue
        if index == insertion_index:
            yield insertion_value

        if hasattr(arg, "_dotnet_instance"):
            yield arg._dotnet_instance
        elif arg and _is_iterable(arg) and hasattr(next(iter(arg)), "_dotnet_instance"):
            yield [item._dotnet_instance for item in arg]
        else:
            yield arg
    # insert the extra value if at the end
    if len(args) == insertion_index:
        yield insertion_value


_wrap_sentinel_value = object()

def _wrap(one_or_many_args: Union[Any, Tuple[Any]]) -> Union[Any, Tuple[Any]]:
    def _is_ni_type(item: Any):
        return type(item).__module__.startswith("NationalInstruments.")

    def _wrap_dotnet_instance(dotnetitem: Any):
        if type(dotnetitem) != NationalInstruments.VeriStand.Error:
            pytype = eval(type(dotnetitem).__name__)
            return pytype(dotnetitem)
        elif dotnetitem.IsError:
            raise VeriStandSdfError(dotnetitem)
        else:
            return _wrap_sentinel_value

    def _wrap_core(arg: Any) -> Any:
        if _is_iterable(arg):
            first = next(iter(arg), _wrap_sentinel_value)
            if first is _wrap_sentinel_value:
                return []  # empty Python list preferable to an empty .NET list or enumerable
            elif _is_ni_type(first):
                return [_wrap_dotnet_instance(item) for item in arg]
            else:
                return [item for item in arg]
        elif _is_ni_type(arg):
            return _wrap_dotnet_instance(arg)
        elif str(type(arg)) == "<class 'System.Version'>":
            # System.Version uses `Build` as the third element, not the fourth
            return (arg.Major, arg.Minor, arg.Build, arg.Revision)
        return arg

    if isinstance(one_or_many_args, Tuple):
        wrapped = [_wrap_core(x) for x in one_or_many_args]
        result = [x for x in wrapped if x is not _wrap_sentinel_value]
        # if we have two parameters, and one is Error, only return the non-error one
        return result[0] if len(result) == 1 and len(wrapped) == 2 else tuple(result)
    else:
        result = _wrap_core(one_or_many_args)
        return result if result is not _wrap_sentinel_value else None


class PathType(_DotNetEnum):
    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.CustomDevice.PathType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for PathType")

    @_staticproperty
    def ABSOLUTE() -> PathType:
        dotnet_result = getattr(NationalInstruments.VeriStand.CustomDevice.PathType, "Absolute")
        return PathType(dotnet_result, "ABSOLUTE")

    @_staticproperty
    def TO_BASE() -> PathType:
        dotnet_result = getattr(NationalInstruments.VeriStand.CustomDevice.PathType, "ToBase")
        return PathType(dotnet_result, "TO_BASE")

    @_staticproperty
    def TO_COMMON_DOC_DIR() -> PathType:
        dotnet_result = getattr(NationalInstruments.VeriStand.CustomDevice.PathType, "ToCommonDocDir")
        return PathType(dotnet_result, "TO_COMMON_DOC_DIR")

    @_staticproperty
    def TO_APPLICATION_DATA_DIR() -> PathType:
        dotnet_result = getattr(NationalInstruments.VeriStand.CustomDevice.PathType, "ToApplicationDataDir")
        return PathType(dotnet_result, "TO_APPLICATION_DATA_DIR")
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/daqplugin/__init__.py sha256=0c78062559a4107af1965d92048e2a221965a37cf246e0b51e2af6b6504e690d bytes=155 -->
## FILE: src/niveristand/daqplugin/__init__.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/daqplugin/__init__.py`
- sha256: `0c78062559a4107af1965d92048e2a221965a37cf246e0b51e2af6b6504e690d`
- bytes: 155

````python
"""Module for NationalInstruments.VeriStand.DAQPlugin."""
### AUTO-GENERATED CODE - DO NOT MODIFY DIRECTLY ###

from ._auto_generated_classes import *
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/daqplugin/_auto_generated_classes.py sha256=26371b8aa29d02015c872af068dcc3c06af348fad7e57aa62af40c3d2ee8789d bytes=7056 -->
## FILE: src/niveristand/daqplugin/_auto_generated_classes.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/daqplugin/_auto_generated_classes.py`
- sha256: `26371b8aa29d02015c872af068dcc3c06af348fad7e57aa62af40c3d2ee8789d`
- bytes: 7056

````python
"""Module for NationalInstruments.VeriStand.DAQPlugin."""
### AUTO-GENERATED CODE - DO NOT MODIFY DIRECTLY ###

from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, Optional, overload, Sequence, Tuple, Union

import clr

clr.AddReference("NationalInstruments.VeriStand.XMLReader")
import NationalInstruments.VeriStand  # type: ignore
import NationalInstruments.VeriStand.DAQPlugin  # type: ignore
import System  # type: ignore

from .. import *


class _staticproperty(staticmethod):
    def __get__(self, *_):
        return self.__func__()


class _DotNetBase:
    def __eq__(self, other) -> bool:
        return self._dotnet_instance == other._dotnet_instance if isinstance(other, _DotNetBase) else False

    def __repr__(self) -> str:
        qualname = type(self).__qualname__
        return f"<niveristand.daqplugin.{qualname}{self._custom_repr()} object at {hex(id(self))}>"

    def _custom_repr(self) -> str:
        return ""


class _DotNetEnum(_DotNetBase):
    def __repr__(self) -> str:
        return f"<niveristand.daqplugin.{type(self).__qualname__}.{self._py_field_name}: {int(self)}>"

    def __str__(self) -> str:
        return f"{type(self).__qualname__}.{self._py_field_name}"

    def __int__(self) -> int:
        return int(self._dotnet_instance)


def _is_iterable(arg: Any) -> bool:
    return not isinstance(arg, str) and isinstance(arg, Iterable)


def _unwrap(out_params: Dict[Optional[Tuple[str, ...]], Tuple[int, Any]], *args: Tuple[Any]) -> Iterable[Any]:
    insertion_index = -1
    if out_params:
        use_out_param = False
        for signature, out_param in out_params.items():
            if not signature:
                use_out_param = True
            elif len(args) == len(signature):
                use_out_param = True
                for arg, sig_type in zip(args, signature):
                    if not isinstance(arg, sig_type):
                        use_out_param = False
                        break
            if use_out_param:
                insertion_index, insertion_value = out_param
                break

    for index, arg in enumerate(args):
        # insert the extra value then continue
        if index == insertion_index:
            yield insertion_value

        if hasattr(arg, "_dotnet_instance"):
            yield arg._dotnet_instance
        elif arg and _is_iterable(arg) and hasattr(next(iter(arg)), "_dotnet_instance"):
            yield [item._dotnet_instance for item in arg]
        else:
            yield arg
    # insert the extra value if at the end
    if len(args) == insertion_index:
        yield insertion_value


_wrap_sentinel_value = object()

def _wrap(one_or_many_args: Union[Any, Tuple[Any]]) -> Union[Any, Tuple[Any]]:
    def _is_ni_type(item: Any):
        return type(item).__module__.startswith("NationalInstruments.")

    def _wrap_dotnet_instance(dotnetitem: Any):
        if type(dotnetitem) != NationalInstruments.VeriStand.Error:
            pytype = eval(type(dotnetitem).__name__)
            return pytype(dotnetitem)
        elif dotnetitem.IsError:
            raise VeriStandSdfError(dotnetitem)
        else:
            return _wrap_sentinel_value

    def _wrap_core(arg: Any) -> Any:
        if _is_iterable(arg):
            first = next(iter(arg), _wrap_sentinel_value)
            if first is _wrap_sentinel_value:
                return []  # empty Python list preferable to an empty .NET list or enumerable
            elif _is_ni_type(first):
                return [_wrap_dotnet_instance(item) for item in arg]
            else:
                return [item for item in arg]
        elif _is_ni_type(arg):
            return _wrap_dotnet_instance(arg)
        elif str(type(arg)) == "<class 'System.Version'>":
            # System.Version uses `Build` as the third element, not the fourth
            return (arg.Major, arg.Minor, arg.Build, arg.Revision)
        return arg

    if isinstance(one_or_many_args, Tuple):
        wrapped = [_wrap_core(x) for x in one_or_many_args]
        result = [x for x in wrapped if x is not _wrap_sentinel_value]
        # if we have two parameters, and one is Error, only return the non-error one
        return result[0] if len(result) == 1 and len(wrapped) == 2 else tuple(result)
    else:
        result = _wrap_core(one_or_many_args)
        return result if result is not _wrap_sentinel_value else None


class ValueDataType(_DotNetEnum):
    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.DAQPlugin.ValueDataType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for ValueDataType")

    @_staticproperty
    def STRING() -> ValueDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.DAQPlugin.ValueDataType, "String")
        return ValueDataType(dotnet_result, "STRING")

    @_staticproperty
    def ENUM() -> ValueDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.DAQPlugin.ValueDataType, "Enum")
        return ValueDataType(dotnet_result, "ENUM")

    @_staticproperty
    def DOUBLE() -> ValueDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.DAQPlugin.ValueDataType, "Double")
        return ValueDataType(dotnet_result, "DOUBLE")

    @_staticproperty
    def U64() -> ValueDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.DAQPlugin.ValueDataType, "U64")
        return ValueDataType(dotnet_result, "U64")

    @_staticproperty
    def U32() -> ValueDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.DAQPlugin.ValueDataType, "U32")
        return ValueDataType(dotnet_result, "U32")

    @_staticproperty
    def U16() -> ValueDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.DAQPlugin.ValueDataType, "U16")
        return ValueDataType(dotnet_result, "U16")

    @_staticproperty
    def I64() -> ValueDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.DAQPlugin.ValueDataType, "I64")
        return ValueDataType(dotnet_result, "I64")

    @_staticproperty
    def I32() -> ValueDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.DAQPlugin.ValueDataType, "I32")
        return ValueDataType(dotnet_result, "I32")

    @_staticproperty
    def I16() -> ValueDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.DAQPlugin.ValueDataType, "I16")
        return ValueDataType(dotnet_result, "I16")

    @_staticproperty
    def BOOLEAN() -> ValueDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.DAQPlugin.ValueDataType, "Boolean")
        return ValueDataType(dotnet_result, "BOOLEAN")
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/errors.py sha256=17e8ddc5a9285b55b4fc864d6fb5b3751312c291aabde7e9a730763178b71603 bytes=4983 -->
## FILE: src/niveristand/errors.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/errors.py`
- sha256: `17e8ddc5a9285b55b4fc864d6fb5b3751312c291aabde7e9a730763178b71603`
- bytes: 4983

````python
class VeristandError(Exception):
    """
    The base class for all VeriStandErrors.

    Note: This class generates a :class:`VeristandError` if a more specific error cannot be determined.
    """

    pass


class TranslateError(VeristandError):
    """Raised if a Python function fails to translate to a VeriStand real-time sequence."""

    pass


class UnexpectedError(VeristandError):
    """Raised if the state of the operation can not be determined."""

    pass


class VeristandNotImplementedError(VeristandError):
    """Raised to indicate this functionality is not yet available."""

    def __init__(self):
        """Throw Generic exception for things that are not implemented yet."""
        self.message = "Not Implemented"
        super(VeristandNotImplementedError, self).__init__(self.message)


class _StopTaskException(Exception):
    pass


class RunError(VeristandError):
    """Raised at the end of execution if an RT sequence called :any:`generate_error`."""

    def __init__(self, error):
        assert isinstance(error, SequenceError)
        self.error = error

    def get_all_errors(self):
        """
        Generates a list of all errors reported during execution.

        Returns:
            List(:class:`SequenceError`): all errors generated during execution.

        """
        error = self.error
        while error:
            yield error
            error = error.inner_error

    @classmethod
    def RunErrorFactory(cls, error):
        from niveristand.clientapi._realtimesequencedefinitionapi.erroraction import ErrorAction

        assert isinstance(error, SequenceError)
        if error.error_action is ErrorAction.ContinueSequenceExecution:
            return RunFailedError(error)
        else:
            return RunAbortedError(error)


class RunFailedError(RunError):
    """
    Raised by :any:`run_py_as_rtseq` to report that the sequence failed.

    This error is raised when a real-time sequence executes successfully,
    but :any:`generate_error` was called with :any:`ErrorAction.ContinueSequenceExecution`.
    """

    def __init__(self, error):
        super(RunFailedError, self).__init__(error)


class RunAbortedError(RunError):
    """
    Raised by :any:`run_py_as_rtseq` to report that the sequence failed.

    This error is raised when a real-time sequence executes successfully,
    but :any:`generate_error` was called with :any:`ErrorAction.StopSequence` or :any:`ErrorAction.AbortSequence`.
    """

    def __init__(self, error):
        super(RunAbortedError, self).__init__(error)


class SequenceError(VeristandError):
    """Raised by :any:`generate_error` to report a sequence failure."""

    def __init__(self, error_code, message, error_action):
        super(SequenceError, self).__init__(message)
        self.error_code = error_code
        self.error_action = error_action
        self.message = message
        self._inner_error = None

    @property
    def inner_error(self):
        """
        Returns the error generated before the most recent error, if any, or `None`.

        Returns:
            :any:`SequenceError`: the previous error generated by this sequence.

        Real-time sequences report only the last error the sequence generates. If you want to see a list of all the
        inner errors, use :any:`RunError.get_all_errors`.

        """
        return self._inner_error

    @inner_error.setter
    def inner_error(self, value):
        assert isinstance(value, SequenceError) or value is None
        assert self._inner_error is None
        self._inner_error = value

    @property
    def is_fatal(self):
        """
        Returns whether or not any error causes the sequence to stop.

        Returns:
            bool: True if the error is :any:`ErrorAction.AbortSequence` or :any:`ErrorAction.StopSequence`, false if
            the error is :any:`ErrorAction.ContinueSequenceExecution`.

        """
        from niveristand.clientapi._realtimesequencedefinitionapi.erroraction import ErrorAction

        isfatal = (self.error_action in (ErrorAction.AbortSequence, ErrorAction.StopSequence)) or (
            self._inner_error and self.inner_error.is_fatal
        )
        return isfatal

    @property
    def should_raise(self):
        """
        Determines whether or not this error raises an exception.

        Returns:
            bool: False if the error is :any:`ErrorAction.ContinueSequenceExecution` with an error code of 0. Otherwise,
            this function returns True.

        """
        from niveristand.clientapi._realtimesequencedefinitionapi.erroraction import ErrorAction

        # If the error code was 0 in a Continue error then don't raise.
        return not (
            self.error_action is ErrorAction.ContinueSequenceExecution and self.error_code == 0
        )
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/legacy/__init__.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: src/niveristand/legacy/__init__.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/legacy/__init__.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/legacy/NIVeriStand.py sha256=93a1b370837ae0f4953b0431b6ef09e552bdd8a8dceebf6f9944a614c4a9265d bytes=44015 -->
## FILE: src/niveristand/legacy/NIVeriStand.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/legacy/NIVeriStand.py`
- sha256: `93a1b370837ae0f4953b0431b6ef09e552bdd8a8dceebf6f9944a614c4a9265d`
- bytes: 44015

````python
"""
NI VeriStand Python API.

C-Python code wrapper of NI VeriStand client API.
"""

import os
import warnings
from niveristand import _internal
import System  # noqa
from NationalInstruments.VeriStand import DataArray  # noqa
from NationalInstruments.VeriStand.ClientAPI import DeployOptions  # noqa
from NationalInstruments.VeriStand.ClientAPI import Factory  # noqa
from NationalInstruments.VeriStand.ClientAPI import SystemState  # noqa
from NationalInstruments.VeriStand.ClientAPI import AlarmInfo  # noqa
from NationalInstruments.VeriStand.ClientAPI import AlarmPriority  # noqa
from NationalInstruments.VeriStand.ClientAPI import AlarmState  # noqa
from NationalInstruments.VeriStand.ClientAPI import AlarmMode  # noqa
from NationalInstruments.VeriStand.ClientAPI import ModelState  # noqa
from NationalInstruments.VeriStand.ClientAPI import ModelCommand  # noqa
from NationalInstruments.VeriStand.ClientAPI import StimulusState  # noqa
from NationalInstruments.VeriStand.ClientAPI import StimulusResult  # noqa
from NationalInstruments.VeriStand.ClientAPI import LogChannel  # noqa
from NationalInstruments.VeriStand.ClientAPI import LogInfo  # noqa
from NationalInstruments.VeriStand.ClientAPI import PlayModeEnum  # noqa
from NationalInstruments.VeriStand.ClientAPI import PlayStateEnum  # noqa

_internal.dummy()
warnings.warn(
    "NIVeriStand.py module is deprecated. "
    "Use only if required functionality is not yet present in niveristand.clientapi",
    DeprecationWarning,
    stacklevel=2,
)


def LaunchNIVeriStand():
    """Launch NI VeriStand.exe from the installed location."""
    import subprocess

    path = _internal.base_assembly_path()
    # Try launching VeriStand with new .exe name.
    try:
        veristand = os.path.join(path, "VeriStand Project Explorer.exe")
        subprocess.Popen([veristand, ""]).pid
        print(veristand)
    except OSError:
        raise NIVeriStandException(-307652, "Could not launch VeriStand.")


def WaitForNIVeriStandReady(address="localhost", secondsTimeout=120):
    import time

    start = time.time()
    while True:
        try:
            Factory().GetIWorkspace2(address)
            break
        except Exception:
            time.sleep(0.5)
            now = time.time()
            if (now - start) > secondsTimeout:
                raise NIVeriStandException(-307663, "Could not connect to gateway.")


def _ConvertMATRIXTO1DARRVAL_(values):
    dataArray = []
    rowDim = len(values)
    colDim = len(values[0])
    for col in range(0, colDim):
        for row in range(0, rowDim):
            dataArray.append(values[row][col])
    return tuple(dataArray)


# Exception
class NIVeriStandException(Exception):
    """NI VeriStand exception."""

    def __init__(self, errcode, errstring):
        self.errcode = errcode
        self.errstring = errstring

    def errorcode(self):
        """Return the error code."""
        return self.errcode

    def message(self):
        """Return a formatted message of the error."""
        return "Consult NI VeriStand help for error code 0x%x error message %s" % (
            self.errcode,
            self.errstring,
        )

    def __str__(self):
        return self.message()

    def __repr__(self):
        return self.message()


def _RaiseException_(errorObject):
    if errorObject.IsError:
        raise NIVeriStandException(errorObject.Code, errorObject.Message)


# Helper function to convert 1D flat array of values into a 2 dimensional data. Data is packed by its column first.
def _Convert1DARRVALTOMATRIX_(rowDim, colDim, data):
    values = []
    for row in range(0, rowDim):
        values.append([])
    for row in range(0, rowDim):
        dataIdx = row
        for col in range(0, colDim):
            values[row].append(data[dataIdx])
            dataIdx = dataIdx + rowDim
    return values


def _ConvertMATRIXARRToDataArray_(matArr):
    dataArrayArray = []
    numElements = len(matArr)
    for elIdx in range(0, numElements):
        rowDim = len(matArr[elIdx])
        colDim = len(matArr[elIdx][0])
        dimValue = []
        dimValue.append(rowDim)
        dimValue.append(colDim)
        doubleVectorValue = []
        for col in range(0, colDim):
            for row in range(0, rowDim):
                doubleVectorValue.append(matArr[elIdx][row][col])
        dataArrayElem = DataArray()
        dataArrayElem.Value = tuple(doubleVectorValue)
        dataArrayElem.Dim = tuple(dimValue)
        dataArrayArray.append(dataArrayElem)
    return tuple(dataArrayArray)


def _ConvertListParamToTuple_(param):
    if isinstance(param, list):
        return tuple(param)
    else:
        return param


# Workspace enum:
class PySystemState:
    """
    The State of the NI VeriStand.exe.

    Idle indicate there is no workspace configuration file deployed
    Active indicate there is a workspace configuration file deployed
    """

    Idle = 0
    Active = 1


# Helper function to create Log Info and Log Channel classes.
def CreateLogChannel(channel_path):
    return LogChannel(channel_path)


def CreateLogInfo():
    return LogInfo()


# define Log Info Trigger Type
class PyLogInfoTriggerType:
    """Priority of an alarm."""

    none = 0
    in_limits = 1
    out_of_limits = 2


def SetLogInfoTrigger(logInfo, triggerType):
    if triggerType == 0:
        logInfo.trigger_type = LogInfo.trigger.none
    elif triggerType == 1:
        logInfo.trigger_type = LogInfo.trigger.in_limits
    elif triggerType == 2:
        logInfo.trigger_type = LogInfo.trigger.out_of_limits


def SetLogInfoChannels(logInfo, logChannelList):
    tupleChannels = _ConvertListParamToTuple_(logChannelList)
    logInfo.channels = tupleChannels


# Workspace definition
class Workspace:
    """Interface that controls the running state of the system and accesses the channels in the system."""

    def __init__(self):
        self.iwks = Factory().GetIWorkspace()

    def GetEngineState(self):
        """Returns the current state of the system."""
        data = self.iwks.GetEngineState(SystemState(0), "", "", "")
        _RaiseException_(data[0])
        return {
            "state": self._NetSystemStateToPy_(data[1]),
            "workspace_file": data[2],
            "systemdefinition_file": data[3],
            "ip_address": data[4],
        }

    def RunWorkspaceFile(
        self, file, launchworkspacewindow, deploysystemdefinition, timeout, username, password
    ):
        """Runs the workspace configuration file you specify.

        Raises an error if you call this function while a configuration is already running.
        You must stop all running configurations before you call this function.
        If this function times out, check to see if the deployment process took longer than expected
        and caused the operation to timeout. Use the GetEngineState function to check the status of the system.
        """
        _RaiseException_(
            self.iwks.RunWorkspaceFile(
                file,
                bool(launchworkspacewindow),
                bool(deploysystemdefinition),
                timeout,
                username,
                password,
            )
        )

    def StopWorkspaceFile(self, password):
        """Stops the execution of the currently running configuration."""
        _RaiseException_(self.iwks.StopWorkspaceFile(password))

    def LockWorkspaceFile(self, old_password, new_password):
        """
        Locks the configuration that is currently running.

        This function will only succeed if a configuration is currently running.
        If this configuration was locked previously, you must enter the previous password in `old_password`.
        """
        _RaiseException_(self.iwks.LockWorkspaceFile(old_password, new_password))

    def UnlockWorkspaceFile(self, password):
        """Unlocks the currently running configuration."""
        _RaiseException_(self.iwks.UnlockWorkspaceFile(password))

    def GetSingleChannelValue(self, name):
        """Acquires the value of the channel you specify."""
        data = 0.0
        data = self.iwks.GetSingleChannelValue(name, data)
        _RaiseException_(data[0])
        return data[1]

    def GetMultipleChannelValues(self, names):
        """Acquires values from the channels you specify."""
        tuppleNames = _ConvertListParamToTuple_(names)
        data = self.iwks.GetMultipleChannelValues(tuppleNames, None)
        _RaiseException_(data[0])
        values = []
        for i in data[1]:
            values.append(i)
        return values

    def GetChannelVectorValues(self, name):
        """Acquires the vector value of the channel you specify."""
        zero = System.UInt32(0)
        data = self.iwks.GetChannelVectorValues(name, zero, zero, None)
        _RaiseException_(data[0])
        return _Convert1DARRVALTOMATRIX_(data[1], data[2], data[3])

    def SetSingleChannelValue(self, name, value):
        """Sets the value for the channel you specify."""
        _RaiseException_(self.iwks.SetSingleChannelValue(name, float(value)))

    def SetMultipleChannelValues(self, names, values):
        """Sets the value(s) for the channels you specify."""
        tuppleNames = _ConvertListParamToTuple_(names)
        tuppleValues = _ConvertListParamToTuple_(values)
        _RaiseException_(self.iwks.SetMultipleChannelValues(tuppleNames, tuppleValues))

    def SetChannelVectorValues(self, name, values):
        """
        Sets the starting parameter vector value for the channel you specify.

        The value you specify in `values` must be a matrix data type.
        """
        ws2 = Workspace2("")
        ws2.SetChannelValues([name], [values])

    def GetMultipleSystemNodesData(self, names):
        """Acquires data from the nodes you specify."""
        tuppleNames = _ConvertListParamToTuple_(names)
        data = self.iwks.GetMultipleSystemNodesData(tuppleNames, None)
        _RaiseException_(data[0])
        nodes = []
        for i in data[1]:
            nodes.append(self._ConvertNodeInfoToDictionary_(i))
        return nodes

    def GetSystemNodeChildren(self, name):
        """Acquires a list of all the child nodes nested under the node you specify."""
        data = self.iwks.GetSystemNodeChildren(name, None)
        _RaiseException_(data[0])
        nodes = []
        for i in data[1]:
            nodes.append(self._ConvertNodeInfoToDictionary_(i))
        return nodes

    def GetSystemNodeChannelList(self, name):
        """
        Acquires all channels of the node you specify.

        If you want to acquire all the channels in the system, enter "" as the node name.
        """
        data = self.iwks.GetSystemNodeChannelList(name, None)
        _RaiseException_(data[0])
        nodes = []
        for i in data[1]:
            nodes.append(self._ConvertNodeInfoToDictionary_(i))
        return nodes

    def GetAliasList(self):
        """Acquires all the aliases of a system."""
        data = self.iwks.GetAliasList(None, None)
        _RaiseException_(data[0])
        dict = {}
        for i in range(0, len(data[1])):
            dict[data[1][i]] = data[2][i]
        return dict

    def _NetSystemStateToPy_(self, net):
        if net == SystemState.Idle:
            return PySystemState.Idle
        elif net == SystemState.Active:
            return PySystemState.Active
        else:
            raise ValueError

    def _ConvertNodeInfoToDictionary_(self, nodeInfo):
        return {
            "name": nodeInfo.Name,
            "path": nodeInfo.FullPath,
            "isChannel": nodeInfo.IsChannel,
            "isReadable": nodeInfo.IsReadable,
            "isWritable": nodeInfo.IsWritable,
            "isScalable": nodeInfo.IsScalable,
            "unit": nodeInfo.ChannelUnit,
        }


class Workspace2(Workspace):
    """Interface that controls the running state of the system and accesses the channels in the system."""

    def __init__(self, gatewayIPAddress=None):
        if gatewayIPAddress is None:
            self.iwks = Factory().GetIWorkspace2("")
        else:
            self.iwks = Factory().GetIWorkspace2(gatewayIPAddress)

    def GetSystemState(self):
        """Returns the current state of the system."""
        data = self.iwks.GetSystemState(SystemState(0), "", None)
        _RaiseException_(data[0])
        targets = []
        for target in data[3]:
            targets.append(target)
        return {
            "state": self._NetSystemStateToPy_(data[1]),
            "systemdefinition_file": data[2],
            "targets": tuple(targets),
        }

    def ConnectToSystem(self, systemdefinition_file, deploy, timeout, calibration_file="", filtered_targets=None):
        """Connects the VeriStand Gateway to one or more targets running on the System Definition file you specify."""
        if filtered_targets is None:
            filtered_targets = []
        options = DeployOptions()
        options.DeploySystemDefinition = System.Boolean(deploy)
        options.Timeout = timeout
        options.CalibrationFilePath = calibration_file
        options.FilteredTargets = filtered_targets

        _RaiseException_(self.iwks.ConnectToSystem(systemdefinition_file, options))

    def ReconnectToSystem(self, target, deploy, calibration_file, timeout):
        """Reconnects the VeriStand Gateway to a target within the system definition file used by the Gateway.\
            You can also redeploy the system definition file."""
        options = DeployOptions()
        options.DeploySystemDefinition = System.Boolean(deploy)
        options.Timeout = timeout
        options.CalibrationFilePath = calibration_file

        _RaiseException_(self.iwks.ReconnectToSystem(System.String(target), options))

    def DisconnectFromSystem(self, password, undeploy_system_definition):
        """Disconnects the VeriStand Gateway from the targets."""
        _RaiseException_(self.iwks.DisconnectFromSystem(password, bool(undeploy_system_definition)))

    def LockConnection(self, old_password, new_password):
        """
        Locks the current VeriStand Gateway connection.

        If the connection was locked previously, you must enter the previous password in `old_password`.
        """
        _RaiseException_(self.iwks.LockConnection(old_password, new_password))

    def UnlockConnection(self, password):
        """Unlocks the current VeriStand Gateway connection."""
        _RaiseException_(self.iwks.UnlockConnection(password))

    def StartDataLogging(self, configuration_name, logInfo):
        """Starts logging data to the configuration you specify."""
        _RaiseException_(self.iwks.StartDataLogging(configuration_name, logInfo))

    def StopDataLogging(self, configuration_name):
        """Terminates data logging for the configuration you specify."""
        _RaiseException_(self.iwks.StopDataLogging(configuration_name))

    def SetChannelValues(self, channels, newValues):
        """Sets the value for the channels you specify.

        The `newValues` parameter accepts scalar, vector, and matrix data types.
        """
        tupleChannelNames = _ConvertListParamToTuple_(channels)
        tupleArray = _ConvertMATRIXARRToDataArray_(newValues)
        _RaiseException_(self.iwks.SetChannelValues(tupleChannelNames, tupleArray))


# define Alarm enums
class PyAlarmPriority:
    """Priority of an alarm."""

    Low = 0
    Medium = 1
    High = 2


class PyAlarmState:
    """State of an alarm in the engine."""

    Disabled = 0
    Enabled = 1
    Tripped = 2
    DelayedTripped = 3
    Indicate = 4


class PyAlarmMode:
    """
    Specifies the mode of an alarm when triggered.

    Normal mode - triggers the alarm and runs the associated script.
    Indicate mode - only triggers the alarm.
    """

    Normal = 0
    IndicateOnly = 1


# define alarm class
class Alarm:
    """Interface that queries information on a configured alarm."""

    def __init__(self, name, target=None, gatewayIPAddress=None):
        if (target is None) and (gatewayIPAddress is None):
            self.ialarm = Factory().GetIAlarm(name)
        elif target is None:
            self.ialarm = Factory().GetIAlarm("", name, gatewayIPAddress)
        elif gatewayIPAddress is None:
            self.ialarm = Factory().GetIAlarm(target, name, "")
        else:
            self.ialarm = Factory().GetIAlarm(target, name, gatewayIPAddress)

    def GetAlarmData(self, timeout):
        """Acquires the alarm data."""
        data = self.ialarm.GetAlarmData(None, System.UInt32(timeout))
        _RaiseException_(data[0])
        return self._ConvertAlarmToDictionary_(data[1])

    def SetAlarmData(self, alarmDict):
        """
        Sets the alarm data.

        DEPRECATED function. This function does not support the Priority Number field.
        Use SetAlarmData2() instead.
        """
        netAlarmInfo = self._ConvertDictionaryToAlarm_(alarmDict)
        _RaiseException_(self.ialarm.SetAlarmData(netAlarmInfo))

    def SetAlarmData2(self, alarmDict):
        """Modifies an alarm in the system."""
        netAlarmInfo = self._ConvertDictionaryToAlarm2_(alarmDict)
        _RaiseException_(self.ialarm.SetAlarmData(netAlarmInfo))

    def SetEnabledState(self, enabled):
        """Enables or disables the current alarm."""
        _RaiseException_(self.ialarm.SetEnabledState(bool(enabled)))

    def SetAlarmMode(self, mode):
        """Changes the mode of this alarm. See PyAlarmMode for possible values."""
        _RaiseException_(self.ialarm.SetAlarmMode(self._PyAlarmModeToNet_(mode)))

    def _NetAlarmPriorityToPy_(self, net):
        if net == AlarmPriority.Low:
            return PyAlarmPriority.Low
        elif net == AlarmPriority.Medium:
            return PyAlarmPriority.Medium
        elif net == AlarmPriority.High:
            return PyAlarmPriority.High
        else:
            raise ValueError

    def _PyAlarmPriorityToNet_(self, py):
        if py == PyAlarmPriority.Low:
            return AlarmPriority.Low
        elif py == PyAlarmPriority.Medium:
            return AlarmPriority.Medium
        elif py == PyAlarmPriority.High:
            return AlarmPriority.High
        else:
            raise ValueError

    def _NetAlarmStateToPy_(self, net):
        if net == AlarmState.Disabled:
            return PyAlarmState.Disabled
        elif net == AlarmState.Enabled:
            return PyAlarmState.Enabled
        elif net == AlarmState.Tripped:
            return PyAlarmState.Tripped
        elif net == AlarmState.DelayedTripped:
            return PyAlarmState.DelayedTripped
        elif net == AlarmState.Indicate:
            return PyAlarmState.Indicate
        else:
            raise ValueError

    def _PyAlarmStateToNet_(self, py):
        if py == PyAlarmState.Disabled:
            return AlarmState.Disabled
        elif py == PyAlarmState.Enabled:
            return AlarmState.Enabled
        elif py == PyAlarmState.Tripped:
            return AlarmState.Tripped
        elif py == PyAlarmState.DelayedTripped:
            return AlarmState.DelayedTripped
        elif py == PyAlarmState.Indicaet:
            return AlarmState.Indicate
        else:
            raise ValueError

    def _NetAlarmModeToPy_(self, net):
        if net == AlarmMode.Normal:
            return PyAlarmMode.Normal
        elif net == AlarmMode.IndicateOnly:
            return PyAlarmMode.IndicateOnly
        else:
            raise ValueError

    def _PyAlarmModeToNet_(self, py):
        if py == PyAlarmMode.Normal:
            return AlarmMode.Normal
        elif py == PyAlarmMode.IndicateOnly:
            return AlarmMode.IndicateOnly
        else:
            raise ValueError

    def _ConvertAlarmToDictionary_(self, alarm):
        return {
            "WatchChannel": alarm.WatchChannel,
            "HighLimitIsConstant": alarm.HighLimitIsConstant,
            "HighLimit": alarm.HighLimit,
            "HighLimitChannel": alarm.HighLimitChannelName,
            "LowLimitIsConstant": alarm.LowLimitIsConstant,
            "LowLimit": alarm.LowLimit,
            "LowLimitChannel": alarm.LowLimitChannelName,
            "DelayDuration": alarm.DelayDuration,
            "TripValue": alarm.TripValue,
            "ProcedureName": alarm.ProcedureName,
            "Priority": self._NetAlarmPriorityToPy_(alarm.Priority),
            "PriorityNumber": alarm.PriorityNumber,
            "State": self._NetAlarmStateToPy_(alarm.State),
            "Mode": self._NetAlarmModeToPy_(alarm.Mode),
            "GroupNumber": alarm.GroupNumber,
            "Name": alarm.Name,
            "FullName": alarm.FullName,
        }

    def _ConvertDictionaryToAlarm_(self, alarm):
        net = AlarmInfo()
        net.WatchChannel = alarm["WatchChannel"]
        net.HighLimitIsConstant = alarm["HighLimitIsConstant"]
        net.HighLimit = alarm["HighLimit"]
        net.HighLimitChannelName = alarm["HighLimitChannel"]
        net.LowLimitIsConstant = alarm["LowLimitIsConstant"]
        net.LowLimit = alarm["LowLimit"]
        net.LowLimitChannelName = alarm["LowLimitChannel"]
        net.DelayDuration = alarm["DelayDuration"]
        net.TripValue = alarm["TripValue"]
        net.ProcedureName = alarm["ProcedureName"]
        net.Priority = self._PyAlarmPriorityToNet_(alarm["Priority"])
        net.State = self._PyAlarmStateToNet_(alarm["State"])
        net.Mode = self._PyAlarmModeToNet_(alarm["Mode"])
        return net

    def _ConvertDictionaryToAlarm2_(self, alarm):
        net = AlarmInfo()
        net.WatchChannel = alarm["WatchChannel"]
        net.HighLimitIsConstant = alarm["HighLimitIsConstant"]
        net.HighLimit = alarm["HighLimit"]
        net.HighLimitChannelName = alarm["HighLimitChannel"]
        net.LowLimitIsConstant = alarm["LowLimitIsConstant"]
        net.LowLimit = alarm["LowLimit"]
        net.LowLimitChannelName = alarm["LowLimitChannel"]
        net.DelayDuration = alarm["DelayDuration"]
        net.TripValue = alarm["TripValue"]
        net.ProcedureName = alarm["ProcedureName"]
        net.PriorityNumber = alarm["PriorityNumber"]
        net.State = self._PyAlarmStateToNet_(alarm["State"])
        net.Mode = self._PyAlarmModeToNet_(alarm["Mode"])
        return net


# define AlarmManager class
class AlarmManager:
    """Interface that acquires information on the state of the server alarm."""

    def __init__(self):
        self.iamgr = Factory().GetIAlarmManager()

    def GetAlarmList(self):
        """Acquires a list of names of all the alarms configured in the system."""
        data = []
        data = self.iamgr.GetAlarmList(data)
        _RaiseException_(data[0])
        values = []
        for i in data[1]:
            values.append(i)
        return values

    def GetAlarmsStatus(self):
        """Acquires a list of alarms organized by status (high, medium, and low)."""
        a0 = a1 = a2 = System.Boolean(False)
        aname0 = aname1 = aname2 = System.String("")
        data = self.iamgr.GetAlarmsStatus(a0, a1, a2, aname0, aname1, aname2)
        _RaiseException_(data[0])
        return {
            "HighAlarm": data[1],
            "MediumAlarm": data[2],
            "LowAlarm": data[3],
            "HighAlarmName": data[4],
            "MedAlarmName": data[5],
            "LowAlarmName": data[6],
        }

    def GetMultipleAlarmsData(self, alarms, timeout):
        """Acquires information about a list of alarms."""
        data = self.iamgr.GetMultipleAlarmsData(list(alarms), System.UInt32(timeout), [])
        _RaiseException_(data[0])
        temp = Alarm("")
        values = []
        for netAlarmInfo in data[1]:
            values.append(temp._ConvertAlarmToDictionary_(netAlarmInfo))
        return values


class AlarmManager2:
    """Interface that acquires information on the state of the server alarm."""

    def __init__(self, gateway_ip_address=None):
        if gateway_ip_address is None:
            self.iamgr = Factory().GetIAlarmManager2("")
        else:
            self.iamgr = Factory().GetIAlarmManager2(gateway_ip_address)

    def GetAlarmList(self, target):
        """Acquires a list of names of all the alarms configured in the system."""
        data = self.iamgr.GetAlarmList(target, None)
        _RaiseException_(data[0])
        values = []
        for i in data[1]:
            values.append(i)
        return values

    def GetAlarmsStatus(self, target):
        """Acquires a list of alarms organized by status (high, medium, and low)."""
        data = self.iamgr.GetAlarmsStatus(target)
        _RaiseException_(data[0])
        return {
            "HighAlarm": data[1],
            "MediumAlarm": data[2],
            "LowAlarm": data[3],
            "HighAlarmName": data[4],
            "MedAlarmName": data[5],
            "LowAlarmName": data[6],
        }

    def GetMultipleAlarmsData(self, target, alarms, timeout):
        """Acquires information about a list of alarms."""
        tupleAlarmNames = _ConvertListParamToTuple_(alarms)
        data = self.iamgr.GetMultipleAlarmsData(
            target, tupleAlarmNames, System.UInt32(timeout), None
        )
        _RaiseException_(data[0])
        temp = Alarm("")
        values = []
        for netAlarmInfo in data[1]:
            values.append(temp._ConvertAlarmToDictionary_(netAlarmInfo))
        return values


# define Model enum
class PyModelState:
    """Represents the state of a model."""

    Running = 0
    Paused = 1
    Resetting = 2
    Idle = 3
    Stopped = 4
    Restoring = 5
    Stopping = 6


class PyModelCommand:
    """Changes the state of the model."""

    Start = 0
    Pause = 1
    Reset = 2


# define Model class
class Model:
    """Interface that acquires information on a specific model running on the system."""

    def __init__(self, name, target=None, gatewayIPAddress=None):
        if (target is None) and (gatewayIPAddress is None):
            self.imodel = Factory().GetIModel(name)
        elif target is None:
            self.imodel = Factory().GetIModel(gatewayIPAddress, "", name)
        elif gatewayIPAddress is None:
            self.imodel = Factory().GetIModel("", target, name)
        else:
            self.imodel = Factory().GetIModel(gatewayIPAddress, target, name)

    def GetModelExecutionState(self):
        """Acquires the execution time and state of the model."""
        data = self.imodel.GetModelExecutionState(0.0, ModelState.Idle)
        _RaiseException_(data[0])
        values = {"time": data[1], "state": self._NetModelStateToPy_(data[2])}
        return values

    def SetModelExecutionState(self, command):
        """
        Changes the current state of the model on the server.

        This is a request operation on the server.
        Even if this function executes successfully, the model state may remain unchanged in some cases.
        See PyModelState for command values.
        """
        _RaiseException_(self.imodel.SetModelExecutionState(self._PyModelStateToNet_(command)))

    def SaveModelState(self, filepath):
        """Saves the current model state to the path on the target you specify in `filepath`."""
        _RaiseException_(self.imodel.SaveModelState(filepath))

    def RestoreModelState(self, filepath):
        """Restores the state of a model running on the target. Specify the path to the model file in `filepath`."""
        _RaiseException_(self.imodel.RestoreModelState(filepath))

    def _NetModelStateToPy_(self, net):
        if net == ModelState.Running:
            return PyModelState.Running
        elif net == ModelState.Paused:
            return PyModelState.Paused
        elif net == ModelState.Resetting:
            return PyModelState.Resetting
        elif net == ModelState.Idle:
            return PyModelState.Idle
        elif net == ModelState.Stopped:
            return PyModelState.Stopped
        elif net == ModelState.Restoring:
            return PyModelState.Restoring
        elif net == ModelState.Saving:
            return PyModelState.Saving
        else:
            raise ValueError

    def _PyModelStateToNet_(self, py):
        if py == PyModelCommand.Start:
            return ModelCommand.Start
        elif py == PyModelCommand.Pause:
            return ModelCommand.Pause
        elif py == PyModelCommand.Reset:
            return ModelCommand.Reset
        else:
            raise ValueError


# define ModelManager
class ModelManager:
    """Interface that queries information on the models configured in the system."""

    def __init__(self):
        self.modmgr = Factory().GetIModelManager()

    def GetModelList(self):
        """Returns a list of all models configured in the system."""
        data = self.modmgr.GetModelList(None)
        _RaiseException_(data[0])
        models = []
        for i in data[1]:
            models.append(i)
        return models

    def GetParametersList(self):
        """Returns a list of all parameters in the system."""
        data = self.modmgr.GetParametersList(None)
        _RaiseException_(data[0])
        params = []
        for i in data[1]:
            params.append(i)
        return params

    def GetSingleParameterValue(self, name):
        """Acquires the value of the parameter you specify."""
        data = self.modmgr.GetSingleParameterValue(name, System.Double(0))
        _RaiseException_(data[0])
        return data[1]

    def GetMultipleParameterValues(self, names):
        """Acquires the value(s) of the parameters you specify."""
        tupleParamNames = _ConvertListParamToTuple_(names)
        data = self.modmgr.GetMultipleParameterValues(tupleParamNames, None)
        _RaiseException_(data[0])
        values = []
        for i in data[1]:
            values.append(i)
        return values

    def GetParameterVectorValues(self, name):
        """Acquires the vector values of the parameter you specify."""
        data = self.modmgr.GetParameterVectorValues(name, System.UInt32(0), System.UInt32(0), None)
        _RaiseException_(data[0])
        return _Convert1DARRVALTOMATRIX_(data[1], data[2], data[3])

    def SetSingleParameterValue(self, name, value):
        """Sets the value of the parameter you specify."""
        _RaiseException_(self.modmgr.SetSingleParameterValue(name, System.Double(value)))

    def SetMultipleParameterValues(self, names, values):
        """Sets the value(s) of the parameters you specify."""
        tupleParamNames = _ConvertListParamToTuple_(names)
        tupleParamValues = _ConvertListParamToTuple_(values)
        _RaiseException_(self.modmgr.SetMultipleParameterValues(tupleParamNames, tupleParamValues))

    def SetParameterVectorValues(self, name, values):
        """
        Sets a vector value for a parameter.

        The value you specify in `value` must be a matrix data type.
        """
        tupleArray = _ConvertMATRIXTO1DARRVAL_(values)
        _RaiseException_(self.modmgr.SetParameterVectorValues(name, tupleArray))


class ModelManager2(ModelManager):
    """Interface that queries information on the models configured in the system."""

    def __init__(self, gateway_ip_address=None):
        super(self.__class__, self).__init__()
        if gateway_ip_address is None:
            self.modmgr = Factory().GetIModelManager2("")
        else:
            self.modmgr = Factory().GetIModelManager2(gateway_ip_address)

    def GetModelList(self, target):
        """Returns a list of models on the target you specify."""
        data = self.modmgr.GetModelList(target, None)
        _RaiseException_(data[0])
        models = []
        for i in data[1]:
            models.append(i)
        return models

    def GetParametersList(self, target):
        """Returns a list of all parameters in the target you specify."""
        data = self.modmgr.GetParametersList(target, None)
        _RaiseException_(data[0])
        params = []
        for i in data[1]:
            params.append(i)
        return params

    def GetSingleParameterValue(self, target, name):
        """Acquires the value of the parameter you specify."""
        data = self.modmgr.GetSingleParameterValue(target, name, System.Double(0))
        _RaiseException_(data[0])
        return data[1]

    def GetMultipleParameterValues(self, target, names):
        """Acquires the value(s) of the parameters you specify."""
        tupleNames = _ConvertListParamToTuple_(names)
        data = self.modmgr.GetMultipleParameterValues(target, tupleNames, None)
        _RaiseException_(data[0])
        values = []
        for i in data[1]:
            values.append(i)
        return values

    def GetParameterVectorValues(self, target, name):
        """Acquires the vector values of the parameter you specify."""
        data = self.modmgr.GetParameterVectorValues(
            target, name, System.UInt32(0), System.UInt32(0), None
        )
        _RaiseException_(data[0])
        return _Convert1DARRVALTOMATRIX_(data[1], data[2], data[3])

    def SetSingleParameterValue(self, target, name, value):
        """Sets the value of the parameter you specify."""
        _RaiseException_(self.modmgr.SetSingleParameterValue(target, name, System.Double(value)))

    def SetMultipleParameterValues(self, target, names, values):
        """Sets the value of the parameter(s) you specify."""
        tupleNames = _ConvertListParamToTuple_(names)
        tupleValues = _ConvertListParamToTuple_(values)
        _RaiseException_(self.modmgr.SetMultipleParameterValues(target, tupleNames, tupleValues))

    def SetParameterVectorValues(self, target, name, values):
        """Set a parameter vector values.

        Values are expected to be a matrix type.
        """
        tupleArray = _ConvertMATRIXTO1DARRVAL_(values)
        _RaiseException_(self.modmgr.SetParameterVectorValues(target, name, tupleArray))

    def SetParameterValues(self, target, names, matrixArr):
        """
        Sets the vector value of the parameter(s) you specify.

        The value you specify in `matrixArr` must be a matrix data type.
        Sample usage ModelManager2.SetParameterValues("target1",["1By3Param","2By3Param"],[[[1,2,3]],[[1,2,3],[4,5,6]]])
        """
        tupleNames = _ConvertListParamToTuple_(names)
        dataArrayArrays = _ConvertMATRIXARRToDataArray_(matrixArr)
        _RaiseException_(self.modmgr.SetParameterValues(target, tupleNames, dataArrayArrays))

    def UpdateParametersFromFile(self, target, parameterfiles):
        """Update a set of parameters specified in the parameter files."""
        tupleFiles = _ConvertListParamToTuple_(parameterfiles)
        _RaiseException_(self.modmgr.UpdateParametersFromFile(target, tupleFiles))


# define class ChannelFaultManager
class ChannelFaultManager:
    """Interface that institutes software value forcing on the system."""

    def __init__(self, gatewayIPAddress=None):
        if gatewayIPAddress is None:
            self.isfiu = Factory().GetIChannelFault("")
        else:
            self.isfiu = Factory().GetIChannelFault(gatewayIPAddress)

    def GetFaultList(self):
        """Acquires a list of all currently faulted channels."""
        data = self.isfiu.GetFaultList(None, None)
        _RaiseException_(data[0])
        return list(zip(data[1], data[2]))

    def GetFaultValue(self, name):
        """Acquires the fault value of a channel you specify."""
        data = self.isfiu.GetFaultValue(name, False, 0.0)
        _RaiseException_(data[0])
        return {"faulted": data[1], "fault value": data[2]}

    def SetFaultValue(self, name, value):
        """Sets the fault value of the channel you specify."""
        _RaiseException_(self.isfiu.SetFaultValue(name, value))

    def ClearFault(self, name):
        """Removes the channel you specify from the fault list."""
        _RaiseException_(self.isfiu.ClearFault(name))

    def ClearAllFaults(self):
        """Clears all faults."""
        _RaiseException_(self.isfiu.ClearAllFaults())


# define stimulus enum
class PyStimulusState:
    """Represents the state of the stimulus generation server."""

    Stopped = 0
    Starting = 1
    Running = 2
    Stopping = 3


class PyStimulusResult:
    """Represents the result of the stimulus generation."""

    NoResult = 0
    Passed = 1
    Failed = 2
    Error = 3


# define stimulus
class Stimulus:
    def __init__(self):
        self.istim = Factory().GetIStimulus()

    def __del__(self):
        self.UnreserveStimulusProfileManager()

    def ReserveStimulusProfileManager(self):
        """
        Creates a task that reserves the stimulus generation server.

        This task prevents other clients from interrupting the stimulus generation process.
        """
        _RaiseException_(self.istim.ReserveStimulusProfileManager())

    def UnreserveStimulusProfileManager(self):
        """Destroys the task that reserves the stimulus generation server. Frees the server for other clients to use."""
        _RaiseException_(self.istim.UnreserveStimulusProfileManager())

    def GetStimulusProfileManagerState(self):
        """Returns the state of the stimulus generation component."""
        data = self.istim.GetStimulusProfileManagerState(StimulusState.Stopped)
        _RaiseException_(data[0])
        return self._NetStimulusStateToPy_(data[1])

    def RunStimulusProfile(self, testfile, baselogpath, timeout, autostart, stopondisconnect):
        """Starts the stimulus generation you defined in the test file."""
        _RaiseException_(
            self.istim.RunStimulusProfile(
                str(testfile),
                str(baselogpath),
                System.UInt32(timeout),
                bool(autostart),
                bool(stopondisconnect),
            )
        )

    def StopStimulusProfile(self):
        """Stops the stimulus generation."""
        _RaiseException_(self.istim.StopStimulusProfile())

    def GetStimulusProfileFile(self):
        """Acquires the current stimulus definition file."""
        data = self.istim.GetStimulusProfileFile("")
        _RaiseException_(data[0])
        return data[1]

    def GetStimulusProfileResult(self):
        """
        Acquires the result of stimulus generation test.

        Only the table test produces a test file of the result.
        """
        data = self.istim.GetStimulusProfileResult(StimulusResult.Failed, "")
        _RaiseException_(data[0])
        values = {"Result": self._NetStimulusResultToPy_(data[1]), "File": data[2]}
        return values

    def _NetStimulusStateToPy_(self, net):
        if net == StimulusState.Stopped:
            return PyStimulusState.Stopped
        elif net == StimulusState.Starting:
            return PyStimulusState.Starting
        elif net == StimulusState.Running:
            return PyStimulusState.Running
        elif net == StimulusState.Stopping:
            return PyStimulusState.Stopping
        else:
            raise ValueError

    def _NetStimulusResultToPy_(self, net):
        if net == 0:
            return PyStimulusResult.NoResult
        elif net == StimulusResult.Passed:
            return PyStimulusResult.Passed
        elif net == StimulusResult.Failed:
            return PyStimulusResult.Failed
        elif net == PyStimulusResult.Error:
            return PyStimulusResult.Error
        else:
            raise ValueError


class Stimulus2(Stimulus):
    """Automates the execution of stimulus profiles."""

    def __init__(self, gatewayIPAddress=None):
        if gatewayIPAddress is None:
            self.istim = Factory().GetIStimulus2("")
        else:
            self.istim = Factory().GetIStimulus2(gatewayIPAddress)

    def __del__(self):
        self.UnreserveStimulusProfileManager()

    def RunStimulusProfile(
        self, testfile, baselogpath, timeout, autostart, stopondisconnect, parameterfiles=()
    ):
        """Starts the stimulus generation you defined in the test file."""
        tupleFiles = _ConvertListParamToTuple_(parameterfiles)
        _RaiseException_(
            self.istim.RunStimulusProfile(
                testfile, baselogpath, timeout, autostart, stopondisconnect, tupleFiles
            )
        )


# define MacroRecorder
class MacroRecorder:
    def __init__(self):
        self.record = Factory().GetIMacroRecorder()

    def StartRecording(self):
        _RaiseException_(self.record.StartRecording())

    def StopRecording(self):
        _RaiseException_(self.record.StopRecording())

    def ResumeRecording(self):
        _RaiseException_(self.record.ResumeRecording())

    def SaveMacro(self, file):
        _RaiseException_(self.record.SaveMacro(file))

    def GetCommandLines(self):
        data = self.record.GetCommandLines()
        _RaiseException_(data[0])
        commandLines = []
        for i in data[1]:
            data = {"seconds": i.seconds, "cmdLine": i.cmdLine}
            commandLines.append(data)
        return commandLines


# define MacroPlayer
class PyMacroPlayerState:
    """Represents the state of the macro player."""

    NotPlaying = 0
    Playing = 1
    Paused = 2


class PyMacroPlayerMode:
    """Represents the replay mode of the macro player."""

    IgnoreTiming = 0
    UseTiming = 1


class MacroPlayer:
    def __init__(self, gatewayIPAddress=None):
        if gatewayIPAddress is None:
            self.player = Factory().GetIMacroPlayer("")
        else:
            self.player = Factory().GetIMacroPlayer(gatewayIPAddress)

    def LoadMacro(self, file):
        """Loads a workspace macro."""
        _RaiseException_(self.player.LoadMacro(file))

    def PlayState(self):
        """Acquires the current play state."""
        data = self.player.PlayState()
        if data == PlayStateEnum.NotPlaying:
            return PyMacroPlayerState.NotPlaying
        elif data == PlayStateEnum.Playing:
            return PyMacroPlayerState.Playing
        elif data == PlayStateEnum.Paused:
            return PyMacroPlayerState.Paused

    def PlayMacro(self, mode):
        """Replays the loaded macro."""
        if mode == 0:
            _RaiseException_(self.player.PlayMacro(PlayModeEnum.IgnoreTiming))
        else:
            _RaiseException_(self.player.PlayMacro(PlayModeEnum.UseTiming))

    def Wait(self):
        _RaiseException_(self.player.Wait())

    def PausePlaying(self):
        _RaiseException_(self.player.PausePlaying())

    def ResumePlaying(self):
        _RaiseException_(self.player.ResumePlaying())

    def StopPlaying(self):
        _RaiseException_(self.player.StopPlaying())

    def GetCommandLines(self):
        data = self.player.GetCommandLines()
        _RaiseException_(data[0])
        commandLines = []
        for i in data[1]:
            data = {"seconds": i.seconds, "cmdLine": i.cmdLine}
            commandLines.append(data)
        return commandLines
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/library/__init__.py sha256=78eb25427311766a4a7647a7508b2c7d0b3520b6dcb62add42a440e346286259 bytes=1461 -->
## FILE: src/niveristand/library/__init__.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/library/__init__.py`
- sha256: `78eb25427311766a4a7647a7508b2c7d0b3520b6dcb62add42a440e346286259`
- bytes: 1461

````python
from niveristand._decorators import task
from niveristand.library._tasks import multitask, nivs_yield, stop_task
from niveristand.library.primitives import (
    abstime,
    arraysize,
    clearfault,
    clearlasterror,
    deltat,
    deltatus,
    fault,
    fix,
    generate_error,
    getlasterror,
    iteration,
    localhost_wait,
    quotient,
    rand,
    recip,
    rem,
    seqtime,
    seqtimeus,
    tickcountms,
    tickcountus,
)
from niveristand.library.timing import (
    wait,
    wait_until_next_ms_multiple,
    wait_until_next_us_multiple,
    wait_until_settled,
)
from niveristand.library.waveforms import (
    ramp,
    sawtooth_wave,
    sine_wave,
    square_wave,
    triangle_wave,
    uniform_white_noise_wave,
)

__all__ = [
    "abstime",
    "arraysize",
    "clearfault",
    "clearlasterror",
    "deltat",
    "deltatus",
    "fault",
    "fix",
    "generate_error",
    "getlasterror",
    "iteration",
    "localhost_wait",
    "multitask",
    "nivs_yield",
    "quotient",
    "recip",
    "rand",
    "rem",
    "ramp",
    "sawtooth_wave",
    "sine_wave",
    "square_wave",
    "triangle_wave",
    "uniform_white_noise_wave",
    "seqtime",
    "seqtimeus",
    "stop_task",
    "task",
    "tickcountms",
    "tickcountus",
    "wait",
    "wait_until_next_ms_multiple",
    "wait_until_next_us_multiple",
    "wait_until_settled",
]
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/library/_tasks.py sha256=9155b3d958620ab61cf59c0229bafd5f820b3082d9e6bcfb5adc3bce96116728 bytes=10103 -->
## FILE: src/niveristand/library/_tasks.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/library/_tasks.py`
- sha256: `9155b3d958620ab61cf59c0229bafd5f820b3082d9e6bcfb5adc3bce96116728`
- bytes: 10103

````python
from collections import deque
from contextlib import contextmanager
from enum import Enum
import inspect
import logging
from threading import current_thread, Event, RLock, Thread
from niveristand import _errormessages, errors


def get_scheduler():
    return _Scheduler.get_scheduler()


@contextmanager
def multitask():
    """
    Creates a multitask context for branching execution.

    Refer to :func:`niveristand.library.multitask` for more details on branching execution.
    """
    multitask_info = _MultiTaskInfo()
    yield multitask_info
    # for a multitask the children need to be added to the queue ahead of the rest of the parent's tasks.
    # So here we reverse the list and add the tasks at the top because we don't know how far the bottom is.
    list.reverse(multitask_info.tasks)
    for task in multitask_info.tasks:
        get_scheduler().register_task_at_top(task)

    for task in multitask_info.tasks:
        task.start()

    this_task = get_scheduler().get_task_for_curr_thread()
    while not multitask_info.finished:
        if this_task.error and this_task.error.is_fatal:
            for task in multitask_info.tasks:
                task.stop_task()
        nivs_yield()
    if this_task.error and this_task.error.is_fatal:
        raise this_task.error


def nivs_yield():
    """
    Yields execution from this task or block to the next.

    Refer to :func:`niveristand.library.multitask` for more details on yielding to other tasks.
    """
    s = get_scheduler()
    task = s.thread_yielded()
    if not task.is_stopped():
        task.wait_for_turn()


class _MultiTaskInfo(object):
    task_id = 0

    def __init__(self):
        self.task = get_scheduler().get_task_for_curr_thread()
        self.tasks = []

    def add_func(self, func):
        task = _Task(func, parent=self, iteration_counter=self.task.iteration_counter)
        self.tasks.append(task)

    @property
    def finished(self):
        return all([t.is_stopped() for t in self.tasks])

    @classmethod
    def get_unique_task_name(cls):
        cls.task_id += 1
        return str(cls.task_id)


class _IterationCounter(object):
    def __init__(self):
        self._count = 0
        self._finished = False

    def inc(self):
        self._count += 1
        return self

    @property
    def count(self):
        return self._count

    @property
    def finished(self):
        return self._finished

    @finished.setter
    def finished(self, value):
        self._finished = value


class _Task(object):
    class _TaskState(Enum):
        Running = 0
        Stopping = 1
        Stopped = 2

    def __init__(self, func, parent=None, iteration_counter=None):
        if inspect.isfunction(func) or inspect.ismethod(func):
            self._task_name = func.__name__
            self._thread = Thread(
                target=func,
                args=(self,),
                name=self._task_name + "_" + _MultiTaskInfo.get_unique_task_name(),
            )
        else:
            self._thread = current_thread()
            self._task_name = str(func)
        self._state = _Task._TaskState.Running
        self._state_signal = Event()
        self._parent = parent
        self._generated_error = None
        self._iteration_counter = iteration_counter if iteration_counter else _IterationCounter()

    def start(self):
        self._thread.start()

    @property
    def parent(self):
        return self._parent

    @property
    def thread(self):
        return self._thread

    @property
    def iteration_counter(self):
        return self._iteration_counter

    def is_stopped(self):
        return self._state == _Task._TaskState.Stopped

    def is_stopping(self):
        return self._state == _Task._TaskState.Stopping

    def wait_for_turn(self):
        result = self._state_signal.wait()
        if self.is_stopping():
            self.mark_stopped()
            raise errors._StopTaskException
        return result

    def signal_to_run(self):
        self._state_signal.set()

    def move_to_ready(self):
        self._state_signal.clear()

    def mark_stopped(self):
        self._state = _Task._TaskState.Stopped

    def stop_task(self):
        # only mark a task as stopping if it's running, otherwise we could get into
        # an infinite loop of going between stopped and stopping.
        if self._state is _Task._TaskState.Running:
            self._state = _Task._TaskState.Stopping

    @property
    def error(self):
        return self._generated_error

    @error.setter
    def error(self, error):
        # cascade errors inside the previous reported error. Only the latest error is reported here, but all are
        # accessible traversing the chain.
        error.inner_error = self.error
        self._generated_error = error
        if self._parent:
            self._parent.task.error = error

    def __repr__(self):
        return "Task:name={} thread={}".format(self._task_name, str(self._thread))

    def __str__(self):
        return "Task:name={}".format(self._task_name)


class _Scheduler(object):
    _schedulers_lock = RLock()
    _scheduler = None

    @classmethod
    def get_scheduler(cls):
        with cls._schedulers_lock:
            if cls._scheduler is None:
                cls._scheduler = _Scheduler()
            return cls._scheduler

    def __init__(self):
        # a dictionary of {threadID:  _Task()}
        self._task_dict = dict()
        self._task_queue = deque()
        self._log = logging.getLogger("<sched>")
        self._last_sched = None

    @property
    def _can_sched(self):
        return not self._last_sched or self._last_sched is self.get_task_for_curr_thread()

    def sched(self):
        self._log.debug("Enter sched")
        # bail early if we were not waiting for this thread to yield
        if not self._can_sched:
            return False
        with self._schedulers_lock:
            try:
                # find the next task in the queue.
                next_task = self._task_queue.popleft()
                # if we have iteration counters, process them all.
                while isinstance(next_task, _IterationCounter):
                    next_task.inc()
                    # requeue the iteration counter only if it's not done counting
                    if not next_task.finished:
                        self._task_queue.append(next_task)
                    next_task = self._task_queue.popleft()

                # then tell it to run
                self._log.debug("Next task:%s", str(next_task))
                self._last_sched = next_task
                next_task.signal_to_run()
            except IndexError:
                # there was no work to do, so set the _last_sched to None
                self._last_sched = None
                return False
        return True

    def thread_yielded(self):
        task = self.get_task_for_curr_thread()
        self._log.debug("Task yielded:%s", str(task))
        # mark the yielding task ready to run
        task.move_to_ready()

        # if this thread is not finished, add it to the run queue
        if not task.is_stopped():
            self._log.debug("Reschedule Task :%s", str(task))
            self._task_queue.append(task)

        # then call sched() so the next thread is signaled to run if necessary
        self.sched()
        # finally, remove the task if it's not going to run anymore
        if task.is_stopped():
            self._log.debug("Finished Task :%s", str(task))
            # in case the task we're about to delete was the last one we were waiting for,
            # reset the last_sched marker.
            self.task_finished(task)
        return task

    def register_task_at_top(self, task):
        self._register_task_core(task, True)

    def register_task(self, task):
        self._register_task_core(task, False)

    def _register_task_core(self, task, at_top):
        self._task_dict[task.thread] = task
        self._log.debug("Register Task :%s", (str(task)))
        if at_top:
            self._task_queue.appendleft(task)
        else:
            self._task_queue.append(task)

    def task_finished(self, task):
        del self._task_dict[task.thread]

    def create_and_register_task_for_top_level(self):
        thread = current_thread()
        if thread in self._task_dict:
            raise errors.VeristandError(_errormessages.reregister_thread)
        task = _Task(thread.name)
        # queue the task
        self.register_task(task)
        # queue an iteration counter for this top-level task
        self._task_queue.append(task.iteration_counter)
        return task

    def get_task_for_curr_thread(self):
        thread = current_thread()

        if thread not in self._task_dict:
            raise errors.VeristandError(_errormessages.unregistered_thread)
        return self._task_dict[thread]

    def try_get_task_for_curr_thread(self):
        try:
            task = self.get_task_for_curr_thread()
        except errors.VeristandError:
            task = None
        return task

    def get_task_by_name(self, taskname):
        found_tasks = [task for task in self._task_dict.values() if task._task_name == taskname]
        assert len(found_tasks) <= 1
        if found_tasks:
            return found_tasks[0]
        return None


def stop_task(task_function):
    """
    Stops the task you specify.

    Args:
        task_function:  task function you want to stop. You must have previously declared the task function inside
                        a :func:`multitask` context.


    Refer to :func:`niveristand.library.multitask` for more details on stopping tasks.

    """
    task = get_scheduler().get_task_by_name(task_function.__name__)
    if task:
        task.stop_task()
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/library/primitives.py sha256=971f1b2fb5bb38bdd49e5c854ecf81fa1c6afc0dacfa7beabfe4404a678a15cc bytes=6256 -->
## FILE: src/niveristand/library/primitives.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/library/primitives.py`
- sha256: `971f1b2fb5bb38bdd49e5c854ecf81fa1c6afc0dacfa7beabfe4404a678a15cc`
- bytes: 6256

````python
import time
from niveristand.errors import VeristandNotImplementedError


def abstime():
    """
    Returns the current date and time, in seconds, relative to the operating system's epoc.

    **Note**: Only available for RT sequences.
    """
    raise VeristandNotImplementedError()


def arraysize(x):
    """
    Returns the number of elements in x, where x is an array.

    Args:
        x: the array for which you want to get the number of elements.

    Returns:
        int: the size of the array. If **x** is not an array, this function returns 0.


    """
    if "__len__" in dir(x):
        return len(x)
    return 0


def clearfault(x):
    """
    Clears all faults set on channel x.

    Args:
        x: the channel you want to clear faults on.

    Channel `x` must be a reference to a channel and should not be a reference to a local variable.
    If `channel` references a local variable, :func:`clearfault` performs no operation.

    **Note**: Only available for RT sequences.

    """
    raise VeristandNotImplementedError()


def clearlasterror():
    """
    Clears the last error set by :func:`generate_error`.

    **Note**: Only available for RT sequences.
    """
    raise VeristandNotImplementedError()


def deltat():
    """
    Returns the duration, in seconds, of the current system timestep.

    To perform equality or comparison operations, use `deltatus`.

    **Note**: In Python Mode, this function always returns `0.01` for a rate of 100Hz.
    """
    return 0.01


def deltatus():
    """
    Returns the duration, in microseconds, of the current system timestep.

    **Note**: In Python Mode, this function always returns `10,000` for a rate of 100Hz.
    """
    return 10000


def fault(channel, value):
    """
    Faults `channel` with `value`.

    Args:
        channel: channel to fault.
        value(float): value to fault the channel.

    `channel` must be a reference to a channel and should not be a reference to a local variable.
    If `channel` references a local variable, :func:`fault` performs no operation.

    **Note**: Only available for RT sequences.

    """
    raise VeristandNotImplementedError()


def fix(x):
    """
    Rounds x to the nearest integer between x and zero.

    Args:
        x(float): value you want to round.

    Returns:
        (float): floating-point representation of the rounded value.

    **Note**: Only available for RT sequences.

    """
    raise VeristandNotImplementedError()


def getlasterror():
    """
    Returns the numeric error code of the last error set by :func:`generate_error`.

    **Note**: Only available for RT sequences.
    """
    raise VeristandNotImplementedError()


def iteration():
    """
    Returns the number of iterations since the current top-level sequence started.

    Returns:
        int: iteration count.

    """
    from niveristand.library._tasks import get_scheduler

    return get_scheduler().get_task_for_curr_thread().iteration_counter.count


def quotient(x, y):
    """
    Returns floor(x/y), the number of times y evenly divides into x.

    Args:
        x: dividend.
        y: divisor.

    Returns:
        int: integer quotient of x/y


    """
    return x // y


def rand(x):
    """
    Returns a random floating-point number between 0 and the maximum value.

    Args:
        x(float): maximum value.

    Returns:
        float: random number between 0 and `x`

    """
    from random import random

    return random() * x


def recip(x):
    """
    Returns 1/x.

    Args:
        x: divisor.

    **Note**: Only available for RT sequences.

    """
    raise VeristandNotImplementedError()


def rem(x, y):
    """
    Returns the remainder of x/y, when the quotient is rounded to the nearest integer.

    Args:
        x(float): dividend.
        y(float): divisor.

    """
    return x % y


def seqtime():
    """
    Returns the number of elapsed seconds since the epoch.

    Returns:
        float: time, in seconds, since the epoch.

    To perform equality or comparison operations, use `seqtimeus` instead.

    """
    return time.time()


def seqtimeus():
    """
    Returns the elapsed time, in microseconds, since the epoch.

    Returns:
        int: elapsed time, in microseconds, as reported by the system clock.

    """
    return int(time.time() * 10**6)


def tickcountms():
    """
    Returns the current value of the milliseconds counter.

    Returns:
        int: time, in milliseconds, as reported by the high-precision counter (if available).

    """
    return int(time.perf_counter() * 10**3)


def tickcountus():
    """
    Returns the current value of the microseconds counter.

    Returns:
        int: time, in microseconds, as reported by the high-precision counter (if available).

    """
    return int(time.perf_counter() * 10**6)


def localhost_wait(amount=0.1):
    """
    Waits for channel values to update.

    Args:
        amount(float): time, in seconds, this function waits for channel values to update.

    When running in the VeriStand Engine, this function is ignored as channels are always up to date.

    """
    time.sleep(amount)


def generate_error(code, message, action):
    """
    Generates an error to report test failure.

    Args:
        code(int): error code to display.
        message(str): error string to display.
        action(:class:`niveristand.clientapi.ErrorAction`): action to perform.

    Returns:
        If action is Continue, returns the generated error.

    """
    from niveristand.clientapi._realtimesequencedefinitionapi.erroraction import ErrorAction
    from niveristand import errors
    from niveristand.library._tasks import get_scheduler

    assert isinstance(action, ErrorAction)
    error = errors.SequenceError(code, message, action)
    get_scheduler().get_task_for_curr_thread().error = error

    if action is ErrorAction.ContinueSequenceExecution:
        return error
    else:
        raise error
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/library/timing.py sha256=94d2794eb020535508164c6463f86e5ff2a157360dbebc7f7dda0e14cf0db5d5 bytes=5266 -->
## FILE: src/niveristand/library/timing.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/library/timing.py`
- sha256: `94d2794eb020535508164c6463f86e5ff2a157360dbebc7f7dda0e14cf0db5d5`
- bytes: 5266

````python
from niveristand import nivs_rt_sequence, NivsParam
from niveristand.clientapi import BooleanValue, DoubleValue, I64Value
from niveristand.library import nivs_yield
from niveristand.library.primitives import quotient, seqtime, tickcountms, tickcountus


@NivsParam("duration", DoubleValue(0), NivsParam.BY_REF)
@nivs_rt_sequence
def wait(duration):
    """
    Waits the duration, in seconds, you specify.

    Args:
        duration (:any:`DoubleValue`): time, in seconds, this function waits. You may specify fractions of seconds.

    Returns:
        float: actual seconds waited.

    This wait is non-blocking, so other tasks will run while this wait executes.

    """
    init_time = DoubleValue(0)
    init_time.value = seqtime()
    while seqtime() - init_time.value < duration.value:
        nivs_yield()

    init_time.value = seqtime()
    return init_time.value


@NivsParam("ms_multiple", I64Value(0), NivsParam.BY_REF)
@nivs_rt_sequence
def wait_until_next_ms_multiple(ms_multiple):
    """
    Waits until the next millisecond multiple of the number you specify in `ms_multiple`.

    Args:
        ms_multiple(:any:`I64Value`): the millisecond multiple to wait until.

    Returns:
        int: actual milliseconds waited.

    This wait is non-blocking, so other tasks will run while this wait executes.

    """
    ticks = I64Value(0)
    if ms_multiple.value > 0:
        last_q = I64Value(0)
        q = I64Value(0)
        ticks.value = tickcountms()
        q.value = quotient(ticks.value, ms_multiple.value)
        last_q.value = q.value
        while q.value == last_q.value:
            last_q.value = q.value
            ticks.value = tickcountms()
            q.value = quotient(ticks.value, ms_multiple.value)
            nivs_yield()
    else:
        nivs_yield()
        ticks.value = tickcountms()
    return ticks.value


@NivsParam("us_multiple", I64Value(0), NivsParam.BY_REF)
@nivs_rt_sequence
def wait_until_next_us_multiple(us_multiple):
    """
    Waits until the next microsecond multiple of the number you specify in `us_multiple`.

    Args:
        us_multiple(:any:`I64Value`): the microsecond multiple to wait until.

    Returns:
        int: actual microseconds waited.

    This wait is non-blocking, so other tasks will run while this wait executes.

    """
    ticks = I64Value(0)
    if us_multiple.value > 0:
        last_q = I64Value(0)
        q = I64Value(0)
        ticks.value = tickcountus()
        q.value = quotient(ticks.value, us_multiple.value)
        last_q.value = q.value
        while q.value == last_q.value:
            last_q.value = q.value
            ticks.value = tickcountus()
            q.value = quotient(ticks.value, us_multiple.value)
            nivs_yield()
    else:
        nivs_yield()
        ticks.value = tickcountus()
    return ticks.value


@NivsParam("signal", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("upper_limit", DoubleValue(150), NivsParam.BY_VALUE)
@NivsParam("lower_limit", DoubleValue(50), NivsParam.BY_VALUE)
@NivsParam("settle_time", DoubleValue(10), NivsParam.BY_VALUE)
@NivsParam("timeout", DoubleValue(60), NivsParam.BY_VALUE)
@nivs_rt_sequence
def wait_until_settled(signal, upper_limit, lower_limit, settle_time, timeout):
    """
    Waits until `signal` settles for the amount of time you specify in `settle_time`.

    Args:
        signal(:any:`DoubleValue`): value to monitor.
        upper_limit(:any:`DoubleValue`): maximum value of the settle range.
        lower_limit(:any:`DoubleValue`): minimum value of the settle range.
        settle_time(:any:`DoubleValue`): time, in seconds, `signal` must stay inside the settle range.
        timeout(:any:`DoubleValue`): seconds to wait before the function times out.

    Returns:
        bool:

        True: The signal failed to settle before the operation timed out.
        False: The signal settled before the operation timed out.


    This wait is non-blocking, so other tasks will run while this wait executes.

    """
    init_time = DoubleValue(0)
    curr_time = DoubleValue(0)
    in_limits_duration = DoubleValue(0)
    in_limits_start = DoubleValue(0)
    timed_out = BooleanValue(False)
    in_limits = BooleanValue(False)
    first = BooleanValue(True)

    init_time.value = seqtime()
    # first is just used to emulate a do-while loop
    while first.value or (
        (not in_limits.value or (in_limits_duration.value < settle_time.value))
        and not timed_out.value
    ):
        first.value = False
        curr_time.value = seqtime()
        if signal.value <= upper_limit.value and signal.value >= lower_limit.value:
            if not in_limits.value:
                in_limits.value = True
                in_limits_start.value = curr_time.value
                in_limits_duration.value = 0
            else:
                in_limits_duration.value = curr_time.value - in_limits_start.value
        else:
            in_limits.value = False

        if timeout.value >= 0:
            timed_out.value = (curr_time.value - init_time.value) > timeout.value
        nivs_yield()

    return timed_out.value
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/library/waveforms.py sha256=ef25689196b673136337d1c2e55571bdd14d86760b37b270d029dd1a91554764 bytes=9381 -->
## FILE: src/niveristand/library/waveforms.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/library/waveforms.py`
- sha256: `ef25689196b673136337d1c2e55571bdd14d86760b37b270d029dd1a91554764`
- bytes: 9381

````python
from math import ceil, floor, pi, sin
from niveristand import nivs_rt_sequence, NivsParam
from niveristand.clientapi import DoubleValue, I32Value, I64Value
from niveristand.library import deltat, localhost_wait, nivs_yield, rem, seqtime


@NivsParam("ramp_out", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("init_value", DoubleValue(1), NivsParam.BY_VALUE)
@NivsParam("final_value", DoubleValue(10), NivsParam.BY_VALUE)
@NivsParam("duration", DoubleValue(10), NivsParam.BY_VALUE)
@nivs_rt_sequence
def ramp(ramp_out, init_value, final_value, duration):
    """
    Ramps a variable from an initial value to an ending value over the duration you specify.

    Args:
        ramp_out(:any:`DoubleValue`): variable you want to ramp.
        init_value(:any:`DoubleValue`): starting value.
        final_value(:any:`DoubleValue`): ending value.
        duration(:any:`DoubleValue`): time, in seconds, you want the ramp to take.

    """
    step_count = I64Value(0)
    increment = DoubleValue(0)

    step_count.value = ceil(duration.value / deltat())
    if step_count.value <= 0:
        ramp_out.value = final_value.value
    else:
        increment.value = (final_value.value - init_value.value) / step_count.value
        for i in range(step_count.value + 1):
            ramp_out.value = (i * increment.value) + init_value.value
            localhost_wait(deltat())
            nivs_yield()


@NivsParam("wave_out", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("amplitude", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("freq", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("phase", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("bias", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("duration", DoubleValue(0), NivsParam.BY_REF)
@nivs_rt_sequence
def sawtooth_wave(wave_out, amplitude, freq, phase, bias, duration):
    """
    Plays a sawtooth wave with the parameters you specify.

    Args:
        wave_out(:any:`DoubleValue`): variable onto which the sawtooth wave plays.
        amplitude(:any:`DoubleValue`): amplitude of the sawtooth wave.
        freq(:any:`DoubleValue`): frequency, in Hz, of the sawtooth wave.
        phase(:any:`DoubleValue`): phase, in degrees, of the sawtooth wave.
        bias(:any:`DoubleValue`): offset to add to the sawtooth wave.
        duration(:any:`DoubleValue`): duration, in seconds, to play the sawtooth wave.

    """
    init_time = DoubleValue(0)
    curr_phase = DoubleValue(0)
    init_time.value = seqtime()
    while seqtime() - init_time.value < duration.value:
        curr_phase.value = rem(
            (freq.value * 360.0 * (seqtime() - init_time.value)) + phase.value, 360.0
        )
        if curr_phase.value < 180.0:
            wave_out.value = ((curr_phase.value / 180.0) * amplitude.value) + bias.value
        else:
            wave_out.value = (((curr_phase.value / 180.0) - 2.0) * amplitude.value) + bias.value
        localhost_wait(deltat())
        nivs_yield()


@NivsParam("wave_out", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("amplitude", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("freq", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("phase", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("bias", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("duration", DoubleValue(0), NivsParam.BY_REF)
@nivs_rt_sequence
def sine_wave(wave_out, amplitude, freq, phase, bias, duration):
    """
    Plays a sine wave with the parameters you specify.

    Args:
        wave_out(:any:`DoubleValue`): variable onto which the sine wave plays.
        amplitude(:any:`DoubleValue`): amplitude of the sine wave.
        freq(:any:`DoubleValue`): frequency, in Hz, of the sine wave.
        phase(:any:`DoubleValue`): phase, in degrees, of the sine wave.
        bias(:any:`DoubleValue`): offset to add to the sine wave.
        duration(:any:`DoubleValue`): duration, in seconds, to play the sine wave.

    """
    init_time = DoubleValue(0)
    phase_rad = DoubleValue(0)

    init_time.value = seqtime()
    phase_rad.value = (phase.value * pi) / 180.0
    while seqtime() - init_time.value < duration.value:
        wave_out.value = (
            amplitude.value
            * sin(((2 * pi * freq.value) * (seqtime() - init_time.value)) + phase_rad.value)
            + bias.value
        )
        localhost_wait(deltat())
        nivs_yield()


@NivsParam("wave_out", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("amplitude", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("freq", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("phase", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("bias", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("duty_cycle", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("duration", DoubleValue(0), NivsParam.BY_REF)
@nivs_rt_sequence
def square_wave(wave_out, amplitude, freq, phase, bias, duty_cycle, duration):
    """
    Plays a square wave with the parameters you specify.

    Args:
        wave_out(:any:`DoubleValue`): variable onto which the square wave plays.
        amplitude(:any:`DoubleValue`): amplitude of the square wave.
        freq(:any:`DoubleValue`): frequency, in Hz, of the square wave.
        phase(:any:`DoubleValue`): phase, in degrees, of the square wave.
        bias(:any:`DoubleValue`): offset to add to the square wave.
        duty_cycle(:any:`DoubleValue`): percentage of time the square wave remains high versus low over one period.
        duration(:any:`DoubleValue`): time, in seconds, to play the square wave.

    """
    init_time = DoubleValue(0)
    curr_phase = DoubleValue(0)

    init_time.value = seqtime()
    while seqtime() - init_time.value < duration.value:
        curr_phase.value = rem(
            ((freq.value * 360.0 * (seqtime() - init_time.value)) + phase.value), 360.0
        )
        if curr_phase.value < (duty_cycle.value * 3.6):
            wave_out.value = amplitude.value + bias.value
        else:
            wave_out.value = -amplitude.value + bias.value
        localhost_wait(deltat())
        nivs_yield()


@NivsParam("wave_out", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("amplitude", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("freq", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("phase", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("bias", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("duration", DoubleValue(0), NivsParam.BY_REF)
@nivs_rt_sequence
def triangle_wave(wave_out, amplitude, freq, phase, bias, duration):
    """
    Plays a triangle wave with the parameters you specify.

    Args:
        wave_out(:any:`DoubleValue`): variable onto which the triangle wave plays.
        amplitude(:any:`DoubleValue`): amplitude of the triangle wave.
        freq(:any:`DoubleValue`): frequency, in Hz, of the triangle wave.
        phase(:any:`DoubleValue`): phase, in degrees, of the triangle wave.
        bias(:any:`DoubleValue`): offset to add to the triangle wave.
        duration(:any:`DoubleValue`): duration, in seconds, to play the triangle wave.

    """
    init_time = DoubleValue(0)
    curr_phase = DoubleValue(0)

    init_time.value = seqtime()
    while seqtime() - init_time.value < duration.value:
        curr_phase.value = rem(
            (freq.value * 360.0 * (seqtime() - init_time.value)) + phase.value, 360.0
        )
        if curr_phase.value < 90.0:
            wave_out.value = ((curr_phase.value / 90.0) * amplitude.value) + bias.value
        elif curr_phase.value < 270.0:
            wave_out.value = ((2.0 - (curr_phase.value / 90.0)) * amplitude.value) + bias.value
        else:
            wave_out.value = (((curr_phase.value / 90.0) - 4.0) * amplitude.value) + bias.value
        localhost_wait(deltat())
        nivs_yield()


@NivsParam("wave_out", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("amplitude", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("duration", DoubleValue(0), NivsParam.BY_REF)
@NivsParam("seed", I32Value(0), NivsParam.BY_VALUE)
@nivs_rt_sequence
def uniform_white_noise_wave(wave_out, amplitude, seed, duration):
    """
    Plays a uniform white noise wave with the parameters you specify.

    Args:
        wave_out(:any:`DoubleValue`): variable onto which the white noise wave plays.
        amplitude(:any:`DoubleValue`): amplitude of the white noise wave.
        seed(:any:`I32Value`): seed for random number generator.
        duration(:any:`DoubleValue`): duration, in seconds, to play the white noise wave.

    """
    x_seed = I32Value(0)
    y_seed = I32Value(0)
    z_seed = I32Value(0)
    init_time = DoubleValue(0)
    seed_sum = DoubleValue(0)

    x_seed.value = seed.value
    y_seed.value = (seed.value * 8191) & 16383
    z_seed.value = (y_seed.value * 8191) & 16383
    init_time.value = seqtime()

    while seqtime() - init_time.value < duration.value:
        x_seed.value = rem(x_seed.value * 171.0, 30269.0)
        y_seed.value = rem(x_seed.value * 172.0, 30307.0)
        z_seed.value = rem(x_seed.value * 170.0, 30323.0)
        seed_sum.value = (
            (x_seed.value / 30269.0) + (y_seed.value / 30307.0) + (z_seed.value / 30323.0)
        )
        wave_out.value = amplitude.value * ((seed_sum - floor(seed_sum.value)) - 0.5) * 2.0
        localhost_wait(deltat())
        nivs_yield()
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/realtimesequencetools.py sha256=e2a7db5873d30875d2ed3d970663f76b3c5e45ef81d13675d35e06d1eb1be681 bytes=2336 -->
## FILE: src/niveristand/realtimesequencetools.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/realtimesequencetools.py`
- sha256: `e2a7db5873d30875d2ed3d970663f76b3c5e45ef81d13675d35e06d1eb1be681`
- bytes: 2336

````python
from niveristand.errors import RunError, VeristandNotImplementedError


def run_py_as_rtseq(toplevelfunc, rtseq_params={}, target=None):
    """
    Runs a Python function as an RT sequence in the VeriStand Engine.

    Args:
        toplevelfunc: the Python function to run.
        rtseq_params (Dict[str, niveristand.clientapi._datatypes.rtprimitives.DoubleValue]):  the parameters to be
         passed to the RT sequence.
        target: The name of the target on which to deploy or run the real-time sequence.
         If None, the default target is used.

    Returns:
        Union[float, None]:
        The numeric value returned by the real-time sequence execution.

    Raises:
        :any:`TranslateError`: if the function is not successfully translated.
        :any:`RunAbortedError`: if this function calls :any:`generate_error` with an action of Abort or Stop.
        :any:`RunFailedError`: if this function calls :any:`generate_error` with a Continue action.

    """
    from niveristand.clientapi import RealTimeSequence

    seq = RealTimeSequence(toplevelfunc, target=target)
    result_state = seq.run(rtseq_params)
    result_state.wait_for_result()
    result_state.session.undeploy()
    if result_state.last_error:
        raise RunError.RunErrorFactory(result_state.last_error)
    return result_state.ret_val


def save_rtseq_as_py(toplevelseq, srcfolder, destfolder):
    raise VeristandNotImplementedError()


def save_py_as_rtseq(toplevelfunc, dest_folder):
    """
    Saves a Python function as an RT sequence that is compatible with the Stimulus Profile Editor.

    Args:
        toplevelfunc: the Python function you want to save.
        dest_folder[str]: the folder you want to save the sequence and all its dependencies in.

    Returns:
        The full path to the main sequence file.

    Raises:
        :class:`niveristand.errors.TranslateError`: if the function is not successfully translated.

    """
    from niveristand.clientapi import RealTimeSequence

    seq = RealTimeSequence(toplevelfunc)
    filename = seq.save(dest_folder)
    return filename


def validate_py_as_rtseq(toplevelobj):
    raise VeristandNotImplementedError()


def run_rtseq(toplevelseq, destfolder):
    raise VeristandNotImplementedError()
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/systemdefinitionapi/__init__.py sha256=e391051b19b28218ebeb325228205d906aebfca3cd9b1057b5061254796b3374 bytes=165 -->
## FILE: src/niveristand/systemdefinitionapi/__init__.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/systemdefinitionapi/__init__.py`
- sha256: `e391051b19b28218ebeb325228205d906aebfca3cd9b1057b5061254796b3374`
- bytes: 165

````python
"""Module for NationalInstruments.VeriStand.SystemDefinitionAPI."""
### AUTO-GENERATED CODE - DO NOT MODIFY DIRECTLY ###

from ._auto_generated_classes import *
````
