# NI OSS SOURCE SNAPSHOT: nimi-python

<!--NI_OSS_SNAPSHOT repo=ni/nimi-python commit=6511f8025f072f7f7021953888b916bbdc31aa2a -->

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nimodinst/README.rst sha256=0b721c94f18ae124b7dda216d76d2cbe86d981c392fdd408c9ca50d8b7c86a39 bytes=7002 -->
## FILE: generated/nimodinst/README.rst

- repository: `ni/nimi-python`
- source_path: `generated/nimodinst/README.rst`
- sha256: `0b721c94f18ae124b7dda216d76d2cbe86d981c392fdd408c9ca50d8b7c86a39`
- bytes: 7002

````rst
Overall Status
--------------

+----------------------+------------------------------------------------------------------------------------------------------------------------------------+
| master branch status | |BuildStatus| |MITLicense| |CoverageStatus|                                                                                        |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------+
| GitHub status        | |OpenIssues| |OpenPullRequests|                                                                                                    |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------+

===========  ============================================================================================================================
Info         NI Modular Instrument driver APIs for Python.
Author       NI
===========  ============================================================================================================================

.. |BuildStatus| image:: https://api.travis-ci.com/ni/nimi-python.svg
    :alt: Build Status - master branch
    :target: https://travis-ci.org/ni/nimi-python

.. |MITLicense| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :alt: MIT License
    :target: https://opensource.org/licenses/MIT

.. |CoverageStatus| image:: https://codecov.io/github/ni/nimi-python/graph/badge.svg
    :alt: Test Coverage - master branch
    :target: https://codecov.io/github/ni/nimi-python

.. |OpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python.svg
    :alt: Open Issues + Pull Requests
    :target: https://github.com/ni/nimi-python/issues

.. |OpenPullRequests| image:: https://img.shields.io/github/issues-pr/ni/nimi-python.svg
    :alt: Open Pull Requests
    :target: https://github.com/ni/nimi-python/pulls


.. _about-section:

About
=====

The **nimodinst** module provides a Python API for NI-ModInst. The code is maintained in the Open Source repository for `nimi-python <https://github.com/ni/nimi-python>`_.

Support Policy
--------------
**nimodinst** supports all the Operating Systems supported by NI-ModInst.

It follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions of CPython.

NI created and supports **nimodinst**.


NI-ModInst Python API Status
----------------------------

+-------------------------------+--------------------------+
| NI-ModInst (nimodinst)        |                          |
+===============================+==========================+
| Driver Version Tested Against | 2025 Q4                  |
+-------------------------------+--------------------------+
| PyPI Version                  | |nimodinstLatestVersion| |
+-------------------------------+--------------------------+
| Supported Python Version      | |nimodinstPythonVersion| |
+-------------------------------+--------------------------+
| Documentation                 | |nimodinstDocs|          |
+-------------------------------+--------------------------+
| Open Issues                   | |nimodinstOpenIssues|    |
+-------------------------------+--------------------------+
| Open Pull Requests            | |nimodinstOpenPRs|       |
+-------------------------------+--------------------------+


.. |nimodinstLatestVersion| image:: http://img.shields.io/pypi/v/nimodinst.svg
    :alt: Latest NI-ModInst Version
    :target: http://pypi.python.org/pypi/nimodinst


.. |nimodinstPythonVersion| image:: http://img.shields.io/pypi/pyversions/nimodinst.svg
    :alt: NI-ModInst supported Python versions
    :target: http://pypi.python.org/pypi/nimodinst


.. |nimodinstDocs| image:: https://readthedocs.org/projects/nimodinst/badge/?version=latest
    :alt: NI-ModInst Python API Documentation Status
    :target: https://nimodinst.readthedocs.io/en/latest


.. |nimodinstOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/nimodinst.svg
    :alt: Open Issues + Pull Requests for NI-ModInst
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Animodinst


.. |nimodinstOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/nimodinst.svg
    :alt: Pull Requests for NI-ModInst
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Animodinst



.. _nimodinst_installation-section:

Installation
------------

As a prerequisite to using the **nimodinst** module, you must install the NI-ModInst runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **NI-ModInst**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install nimodinst


Contributing
============

We welcome contributions! You can clone the project repository, build it, and install it by `following these instructions <https://github.com/ni/nimi-python/blob/master/CONTRIBUTING.md>`_.

Usage
------

The following is a basic example of using the **nimodinst** module to retrieve information on all High Speed Digitizers currently in the system.

.. code-block:: python

    import nimodinst
    with nimodinst.Session("niscope") as session:
        for device in session:
            print("{: >20} {: >15} {: >10}".format(device.device_name, device.device_model, device.serial_number))

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nimodinst/examples>`_

.. _support-section:

Support / Feedback
==================

For support specific to the Python API, follow the processs in `Bugs / Feature Requests`_.
For support with hardware, the driver runtime or any other questions not specific to the Python API, please visit `NI Community Forums <https://forums.ni.com/>`_.

.. _bugs-section:

Bugs / Feature Requests
=======================

To report a bug or submit a feature request specific to Python API, please use the
`GitHub issues page <https://github.com/ni/nimi-python/issues>`_.

Fill in the issue template as completely as possible and we will respond as soon
as we can.


.. _documentation-section:

Documentation
=============

Documentation is available `here <http://nimodinst.readthedocs.io>`_.


.. _license-section:

License
=======

**nimi-python** is licensed under an MIT-style license (`see
LICENSE <https://github.com/ni/nimi-python/blob/master/LICENSE>`_).
Other incorporated projects may be licensed under different licenses. All
licenses allow for non-commercial and commercial use.


**gRPC Features**

For driver APIs that support it, passing a GrpcSessionOptions instance as a parameter to Session.__init__() is
subject to the NI General Purpose EULA (`see NILICENSE <https://github.com/ni/nimi-python/blob/master/NILICENSE>`_).
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nimodinst/setup.py sha256=81fe8f3b6788b3a2aa4f5a1ce9bccc919caf2107cfc41f4fee1fe2516c8568a7 bytes=1650 -->
## FILE: generated/nimodinst/setup.py

- repository: `ni/nimi-python`
- source_path: `generated/nimodinst/setup.py`
- sha256: `81fe8f3b6788b3a2aa4f5a1ce9bccc919caf2107cfc41f4fee1fe2516c8568a7`
- bytes: 1650

````python
#!/usr/bin/python
# This file was generated


from setuptools import setup


pypi_name = 'nimodinst'


def read_contents(file_to_read):
    with open(file_to_read, 'r') as f:
        return f.read()


setup(
    name=pypi_name,
    zip_safe=True,
    version='1.4.10.dev0',
    description='NI-ModInst Python API',
    long_description=read_contents('README.rst'),
    long_description_content_type='text/x-rst',
    author='NI',
    author_email="opensource@ni.com",
    url="https://github.com/ni/nimi-python",
    maintainer="NI",
    maintainer_email="opensource@ni.com",
    keywords=['nimodinst'],
    license='MIT',
    include_package_data=True,
    packages=['nimodinst'],
    python_requires='>=3.10',
    install_requires=[
        'hightime>=0.2.0',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering :: Instrument Drivers",
        "Topic :: System :: Hardware :: Hardware Drivers"
    ],
    package_data={pypi_name: ['VERSION']},
)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nimodinst/tox-system_tests.ini sha256=56bb63f035bc25f3d1f4150e41f096b9e6044ba04791d4a8b7773398c0109620 bytes=2727 -->
## FILE: generated/nimodinst/tox-system_tests.ini

- repository: `ni/nimi-python`
- source_path: `generated/nimodinst/tox-system_tests.ini`
- sha256: `56bb63f035bc25f3d1f4150e41f096b9e6044ba04791d4a8b7773398c0109620`
- bytes: 2727

````ini
# Tox (http://tox.testrun.org/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox -c tox-system_tests.ini" from the driver directory. (generated/nimodinst)
[tox]
envlist = py{310,311,312,313,314}-nimodinst-system_tests, py314-nimodinst-coverage
skip_missing_interpreters=True
ignore_basepython_conflict=True
# We put the .tox directory outside of the Jenkins workspace so that it isn't wiped with the rest of the repo
toxworkdir = ../../../.tox

[testenv]
description =
    nimodinst-system_tests: Run nimodinst system tests (requires NI-ModInst runtime to be installed)
    nimodinst-coverage: Prepare coverage report for upload to codecov.io  # upload handled by GitHub Actions

changedir =
    nimodinst-system_tests: .
    nimodinst-coverage: .

commands =
    # --disable-pip-version-check prevents pip from telling us we need to upgrade pip, since we are doing that now
    nimodinst-system_tests: python -m pip install --disable-pip-version-check --upgrade pip
    nimodinst-system_tests: python -c "import nimodinst; nimodinst.print_diagnostic_information()"
    nimodinst-system_tests: coverage run --rcfile=../../tools/coverage_system_tests.rc --source nimodinst --parallel-mode -m pytest ../../src/nimodinst/examples --junitxml=../junit/junit-nimodinst-{envname}-examples-{env:BITNESS:64}.xml {posargs}
    nimodinst-system_tests: coverage run --rcfile=../../tools/coverage_system_tests.rc --source nimodinst --parallel-mode -m pytest ../../src/nimodinst/system_tests -c tox-system_tests.ini --junitxml=../junit/junit-nimodinst-{envname}-{env:BITNESS:64}.xml --durations=5 {posargs}

    nimodinst-coverage: coverage combine --rcfile=../../tools/coverage_system_tests.rc ./
    # Create the report to upload
    nimodinst-coverage: coverage xml -i --rcfile=../../tools/coverage_system_tests.rc
    # Display the coverage results
    nimodinst-coverage: coverage report --rcfile=../../tools/coverage_system_tests.rc

deps =
    nimodinst-system_tests: pytest
    nimodinst-system_tests: coverage
    nimodinst-system_tests: numpy
    nimodinst-system_tests: hightime
    nimodinst-system_tests: fasteners
    nimodinst-system_tests: pytest-json

    nimodinst-coverage: coverage

depends =
    nimodinst-coverage: py{310,311,312,313,314}-nimodinst-system_tests

passenv =
    GIT_BRANCH
    GIT_COMMIT
    BUILD_URL
    BRANCH_NAME
    JENKINS_URL
    BUILD_NUMBER

[pytest]
addopts = --verbose
filterwarnings =
   error::pytest.PytestUnhandledThreadExceptionWarning
norecursedirs = .* build dist CVS _darcs {arch} *.egg venv
junit_suite_name = nimi-python
junit_family = xunit1
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nirfsg/nirfsg/__init__.py sha256=97fea53327b56e6a2d9a29577580aea3290fb047c69ea6836ee96ceffac8a625 bytes=3288 -->
## FILE: generated/nirfsg/nirfsg/__init__.py

- repository: `ni/nimi-python`
- source_path: `generated/nirfsg/nirfsg/__init__.py`
- sha256: `97fea53327b56e6a2d9a29577580aea3290fb047c69ea6836ee96ceffac8a625`
- bytes: 3288

````python
# -*- coding: utf-8 -*-
# This file was generated


__version__ = '1.1.1.dev0'

from nirfsg.enums import *  # noqa: F403,F401,H303
from nirfsg.errors import DriverWarning  # noqa: F401
from nirfsg.errors import Error  # noqa: F401
from nirfsg.grpc_session_options import *  # noqa: F403,F401,H303
from nirfsg.session import Session  # noqa: F401


def get_diagnostic_information():
    '''Get diagnostic information about the system state that is suitable for printing or logging

    returns: dict

    note: Python bitness may be incorrect when running in a virtual environment
    '''
    import importlib.metadata
    import os
    import platform
    import struct
    import sys

    def is_python_64bit():
        return (struct.calcsize("P") == 8)

    def is_os_64bit():
        return platform.machine().endswith('64')

    def is_venv():
        return 'VIRTUAL_ENV' in os.environ

    info = {}
    info['os'] = {}
    info['python'] = {}
    info['driver'] = {}
    info['module'] = {}
    if platform.system() == 'Windows':
        try:
            import winreg as winreg
        except ImportError:
            import _winreg as winreg

        os_name = 'Windows'
        try:
            driver_version_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\National Instruments\NI-RFSG\CurrentVersion")
            driver_version = winreg.QueryValueEx(driver_version_key, "Version")[0]
        except WindowsError:
            driver_version = 'Unknown'
    elif platform.system() == 'Linux':
        os_name = 'Linux'
        driver_version = 'Unknown'
    else:
        raise SystemError('Unsupported platform: {}'.format(platform.system()))

    installed_packages_names = [
        name
        for name_list in importlib.metadata.packages_distributions().values()
        for name in name_list
    ]
    installed_packages_names = set(installed_packages_names)
    installed_packages_list = [
        {'name': name, 'version': importlib.metadata.distribution(name).version}
        for name in sorted(installed_packages_names)
    ]

    info['os']['name'] = os_name
    info['os']['version'] = platform.version()
    info['os']['bits'] = '64' if is_os_64bit() else '32'
    info['driver']['name'] = "NI-RFSG"
    info['driver']['version'] = driver_version
    info['module']['name'] = 'nirfsg'
    info['module']['version'] = "1.1.1.dev0"
    info['python']['version'] = sys.version
    info['python']['bits'] = '64' if is_python_64bit() else '32'
    info['python']['is_venv'] = is_venv()
    info['python']['packages'] = installed_packages_list

    return info


def print_diagnostic_information():
    '''Print diagnostic information in a format suitable for issue report

    note: Python bitness may be incorrect when running in a virtual environment
    '''
    info = get_diagnostic_information()

    row_format = '    {:<10} {}'
    for type in ['OS', 'Driver', 'Module', 'Python']:
        typename = type.lower()
        print(type + ':')
        for item in info[typename]:
            if item != 'packages':
                print(row_format.format(item.title() + ':', info[typename][item]))
    print('    Installed Packages:')
    for p in info['python']['packages']:
        print((' ' * 8) + p['name'] + '==' + p['version'])

    return info
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nirfsg/nirfsg/_attributes.py sha256=d8561d1cdcb7d85f810e7101675712541720cd48f851822b681620b8955bfea4 bytes=6175 -->
## FILE: generated/nirfsg/nirfsg/_attributes.py

- repository: `ni/nimi-python`
- source_path: `generated/nirfsg/nirfsg/_attributes.py`
- sha256: `d8561d1cdcb7d85f810e7101675712541720cd48f851822b681620b8955bfea4`
- bytes: 6175

````python
# -*- coding: utf-8 -*-
# This file was generated
import nirfsg._converters as _converters
import nirfsg.errors as errors

import hightime


class Attribute(object):
    '''Base class for all typed attributes.'''

    def __init__(self, attribute_id):
        self._attribute_id = attribute_id


class AttributeViInt32(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_int32(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_int32(self._attribute_id, value)


class AttributeViInt32TimeDeltaMilliseconds(Attribute):

    def __get__(self, session, session_type):
        return hightime.timedelta(milliseconds=session._get_attribute_vi_int32(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_int32(self._attribute_id, _converters.convert_timedelta_to_milliseconds_int32(value))


class AttributeViInt32TimeDeltaMonths(Attribute):

    def __get__(self, session, session_type):
        return _converters.convert_month_to_timedelta(session._get_attribute_vi_int32(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_int32(self._attribute_id, _converters.convert_timedelta_to_months_int32(value))


class AttributeViInt64(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_int64(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_int64(self._attribute_id, value)


class AttributeViReal64(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_real64(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_real64(self._attribute_id, value)


class AttributeViReal64TimeDeltaSeconds(Attribute):

    def __get__(self, session, session_type):
        return hightime.timedelta(seconds=session._get_attribute_vi_real64(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_real64(self._attribute_id, _converters.convert_timedelta_to_seconds_real64(value))


class AttributeViString(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_string(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_string(self._attribute_id, value)


class AttributeViStringRepeatedCapability(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_string(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_string(self._attribute_id, _converters.convert_repeated_capabilities_without_prefix(value))


class AttributeViStringCommaSeparated(Attribute):

    def __get__(self, session, session_type):
        return _converters.convert_comma_separated_string_to_list(session._get_attribute_vi_string(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_string(self._attribute_id, _converters.convert_list_to_comma_separated_string(value))


class AttributeViBoolean(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_boolean(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_boolean(self._attribute_id, value)


class AttributeEnum(Attribute):

    def __init__(self, underlying_attribute_meta_class, enum_meta_class, attribute_id):
        super(AttributeEnum, self).__init__(attribute_id)
        self._underlying_attribute = underlying_attribute_meta_class(attribute_id)
        self._attribute_type = enum_meta_class

    def __get__(self, session, session_type):
        return self._attribute_type(self._underlying_attribute.__get__(session, session_type))

    def __set__(self, session, value):
        if type(value) is not self._attribute_type:
            raise TypeError('must be ' + str(self._attribute_type.__name__) + ' not ' + str(type(value).__name__))
        return self._underlying_attribute.__set__(session, value.value)


class AttributeEnumWithConverter(Attribute):
    '''Class for attributes that use enums internally but are exposed in the nirfsg Python module as something else, thus need conversion.'''

    def __init__(self, underlying_attribute_enum, getter_converter, setter_converter):
        '''Creates and returns an instance of AttributeEnumWithConverter attribute meta class.

        Args:
            underlying_attribute_enum (AttributeEnum): The AttributeEnum instance for the underlying
                enum

            getter_converter (function): The function that converts the enum value to its converted
                value

            setter_converter (function): The function that converts the converted value back to the
                enum value
        '''
        super(AttributeEnumWithConverter, self).__init__(underlying_attribute_enum._attribute_id)
        self._underlying_attribute_enum = underlying_attribute_enum
        self._getter_converter = getter_converter
        self._setter_converter = setter_converter

    def __get__(self, session, session_type):
        try:
            return self._getter_converter(
                self._underlying_attribute_enum.__get__(session, session_type)
            )
        except (KeyError, ValueError):
            raise errors.DriverTooNewError()

    def __set__(self, session, value):
        try:
            return self._underlying_attribute_enum.__set__(session, self._setter_converter(value))
        except KeyError:
            raise ValueError(f'Invalid value: {value}')


# nitclk specific attribute type
class AttributeSessionReference(Attribute):

    def __get__(self, session, session_type):
        # Import here to avoid a circular dependency when initial import happens
        from nirfsg.session import SessionReference
        return SessionReference(session._get_attribute_vi_session(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_session(self._attribute_id, _converters.convert_to_nitclk_session_number(value))
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nirfsg/nirfsg/_complextype.py sha256=71b9d4407e8b368436cae076a1707c553026e4b88dd3179b54f1282c20fd63fa bytes=456 -->
## FILE: generated/nirfsg/nirfsg/_complextype.py

- repository: `ni/nimi-python`
- source_path: `generated/nirfsg/nirfsg/_complextype.py`
- sha256: `71b9d4407e8b368436cae076a1707c553026e4b88dd3179b54f1282c20fd63fa`
- bytes: 456

````python
# -*- coding: utf-8 -*-
# This file was generated
import ctypes
import nirfsg._visatype as _visatype


class NIComplexNumber(ctypes.Structure):
    _fields_ = [("real", _visatype.ViReal64), ("imag", _visatype.ViReal64)]


class NIComplexNumberF32(ctypes.Structure):
    _fields_ = [("real", _visatype.ViReal32), ("imag", _visatype.ViReal32)]


class NIComplexI16(ctypes.Structure):
    _fields_ = [("real", _visatype.ViInt16), ("imag", _visatype.ViInt16)]
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nirfsg/nirfsg/_converters.py sha256=f0fcd7db6b50e111754366e6192806ff3155ff344f5c7f9581b1a0e894aa43b1 bytes=14621 -->
## FILE: generated/nirfsg/nirfsg/_converters.py

- repository: `ni/nimi-python`
- source_path: `generated/nirfsg/nirfsg/_converters.py`
- sha256: `f0fcd7db6b50e111754366e6192806ff3155ff344f5c7f9581b1a0e894aa43b1`
- bytes: 14621

````python
# -*- coding: utf-8 -*-
# This file was generated
import nirfsg._visatype as _visatype
import nirfsg.errors as errors

import array
import collections
import hightime
import numbers

from functools import singledispatch


@singledispatch
def _convert_repeated_capabilities(arg, prefix):  # noqa: F811
    '''Base version that should not be called

    Overall purpose is to convert the repeated capabilities to a list of strings with prefix from what ever form

    Supported types:
    - str - List (comma delimited)
    - str - Range (using '-' or ':')
    - str - single item
    - int
    - tuple
    - range
    - slice

    Each instance should return a list of strings, without prefix
    - '0' --> ['0']
    - 0 --> ['0']
    - '0, 1' --> ['0', '1']
    - 'ScriptTrigger0, ScriptTrigger1' --> ['0', '1']
    - '0-1' --> ['0', '1']
    - '0:1' --> ['0', '1']
    - '0-1,4' --> ['0', '1', '4']
    - range(0, 2) --> ['0', '1']
    - slice(0, 2) --> ['0', '1']
    - (0, 1, 4) --> ['0', '1', '4']
    - ('0-1', 4) --> ['0', '1', '4']
    - (slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17') -->
        ['0', '2', '4', '5', '6', '7', '8', '9', '11', '12', '13', '14', '16', '17']
    '''
    raise errors.InvalidRepeatedCapabilityError('Invalid type', type(arg))


@_convert_repeated_capabilities.register(numbers.Integral)  # noqa: F811
def _(repeated_capability, prefix):
    '''Integer version'''
    return [str(repeated_capability)]


# This parsing function duplicate the parsing in the driver, so if changes to the allowed format are made there, they will need to be replicated here.
@_convert_repeated_capabilities.register(str)  # noqa: F811
def _(repeated_capability, prefix):
    '''String version (this is the most complex)

    We need to deal with a range ('0-3' or '0:3'), a list ('0,1,2,3') and a single item
    '''
    # First we deal with a list
    rep_cap_list = repeated_capability.split(',')
    if len(rep_cap_list) > 1:
        # We have a list so call ourselves again to let the iterable instance handle it
        return _convert_repeated_capabilities(rep_cap_list, prefix)

    # Now we deal with ranges
    # We remove any prefix and change ':' to '-'
    r = repeated_capability.strip().replace(prefix, '').replace(':', '-')
    rc = r.split('-')
    if len(rc) > 1:
        if len(rc) > 2:
            raise errors.InvalidRepeatedCapabilityError("Multiple '-' or ':'", repeated_capability)
        try:
            start = int(rc[0])
            end = int(rc[1])
        except ValueError:
            # This exception is raised when repeated_capability is of the form "dev/0-1". rc[0] == "dev/0" in this case.
            # Just return the repeated_capability string as-is in that case.
            pass
        else:
            if end < start:
                rng = range(start, end - 1, -1)
            else:
                rng = range(start, end + 1)
            return _convert_repeated_capabilities(rng, prefix)

    # If we made it here, it must be a simple item so we remove any prefix and return
    return [repeated_capability.replace(prefix, '').strip()]


# We cannot use collections.abc.Iterable here because strings are also iterable and then this
# instance is what gets called instead of the string one.
@_convert_repeated_capabilities.register(list)  # noqa: F811
@_convert_repeated_capabilities.register(range)  # noqa: F811
@_convert_repeated_capabilities.register(tuple)  # noqa: F811
def _(repeated_capability, prefix):
    '''Iterable version - can handle lists, ranges, and tuples'''
    rep_cap_list = []
    for r in repeated_capability:
        rep_cap_list += _convert_repeated_capabilities(r, prefix)
    return rep_cap_list


@_convert_repeated_capabilities.register(slice)  # noqa: F811
def _(repeated_capability, prefix):
    '''slice version'''
    def ifnone(a, b):
        return b if a is None else a
    # Turn the slice into a list and call ourselves again to let the iterable instance handle it
    rng = range(ifnone(repeated_capability.start, 0), repeated_capability.stop, ifnone(repeated_capability.step, 1))
    return _convert_repeated_capabilities(rng, prefix)


def convert_repeated_capabilities(repeated_capability, prefix=''):
    '''Convert a repeated capabilities object to a comma delimited list

    Args:
        repeated_capability (str, list, tuple, slice, None) -
        prefix (str) - common prefix for all strings

    Returns:
        rep_cap_list (list of str) - list of each repeated capability item with ranges expanded and prefix added
    '''
    # We need to explicitly handle None here. Everything else we can pass on to the singledispatch functions
    if repeated_capability is None:
        return []
    return [prefix + r for r in _convert_repeated_capabilities(repeated_capability, prefix)]


def convert_repeated_capabilities_without_prefix(repeated_capability):
    '''Convert a repeated capabilities object, without any prefix, to a comma delimited list

    Args:
        repeated_capability - Supported types:
            - str - list (comma-delimited)
            - str - range (using '-' or ':')
            - str - single item
            - int
            - list of str
            - tuple of str
            - range of str
            - slice of str
            - None

    Returns:
        rep_cap (str) - comma delimited string of each repeated capability item with ranges expanded
    '''
    return ','.join(convert_repeated_capabilities(repeated_capability, ''))


def expand_channel_string(channel_string, all_channels_in_session):
    '''Expands a channel_string to a list of individual channel names.

    The individual channel names may or may not be fully qualified channel names as applicable for
    the session. In other words, the individual channel names will be a subset of
    all_channels_in_session.

    Examples:
        - expand_channel_string('1', ['0', '1', '2', '3']) --> ['1']
        - expand_channel_string('4,1:2', ['1', '2', '4']) --> ['4', '1', '2']
        - expand_channel_string('2:3,0', ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/3'])
            --> ['Dev1/2', 'Dev1/3', 'Dev1/0']
        - expand_channel_string('Dev1/1', ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/3'])
            --> ['Dev1/1']
        - expand_channel_string('4,Dev1/1:2', ['Dev1/1', 'Dev1/2', 'Dev1/4'])
            --> ['Dev1/4', 'Dev1/1', 'Dev1/2']
        - expand_channel_string('Dev1/4,Dev1/2,Dev1/3', ['Dev1/2', 'Dev1/3', 'Dev1/4'])
            --> ['Dev1/4', 'Dev1/2', 'Dev1/3']
        - expand_channel_string('Dev1/1,Dev2/2', ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/3', 'Dev2/0', 'Dev2/1', 'Dev2/2', 'Dev2/3'])
            --> ['Dev1/1', 'Dev2/2']
        - expand_channel_string(' Dev1 / 1 : 2 , 4 ', ['Dev1/1', 'Dev1/2', 'Dev1/4'])
            --> ['Dev1/1', 'Dev1/2', 'Dev1/4']
        - expand_channel_string('DEV1/0-1    , Dev1/3', ['dev1/0', 'dev1/1', 'dev1/2', 'dev1/3'])
            --> ['dev1/0', 'dev1/1', 'dev1/3']

    Args:
        channel_string (str) - refer to _convert_repeated_capabilities() for the
            supported formats (this string is expected to be used as the index of session.channels)

        all_channels_in_session (list of str) - names of all the channels in the session as returned
            by get_channel_names()

    Returns:
        channel_names (list of str) - A list in which each element is the name of a single channel,
            with the exact capitalization used by the driver runtime.
    '''
    if channel_string.strip() == '':
        return all_channels_in_session

    # Rule 1: If all_channels_in_session is fully-qualified then returned channel names should be
    #         fully-qualified, otherwise returned channel names should not be fully-qualified.
    # Rule 2: If any channel in the input is not fully-qualified, but we need to return
    #         fully-qualified channels because of Rule 1, then use the channel qualifier obtained
    #         from all_channels_in_session. This can only happen on a single-instrument session,
    #         so all the channel qualifiers are the same and we pick the first one.

    instrument, separator, channel = all_channels_in_session[0].rpartition('/')
    default_channel_qualifier = instrument + separator

    expanded_channel_list = []
    for token in channel_string.split(','):
        instrument, separator, channel = token.rpartition('/')
        instrument = instrument.strip()
        channel_qualifier = instrument + separator if instrument else default_channel_qualifier
        expanded_channel_list.extend(
            convert_repeated_capabilities(channel.strip(), channel_qualifier)
        )

    # Convert the expanded channel names to their canonical form based on all_channels_in_session
    lowercase_channel_name_to_session_channel_name_dict = {
        channel_name.lower(): channel_name for channel_name in all_channels_in_session
    }
    return [
        lowercase_channel_name_to_session_channel_name_dict[channel_name.lower()]
        for channel_name in expanded_channel_list
    ]


def _convert_timedelta(value, library_type, scaling):
    try:
        # We first assume it is a timedelta object
        scaled_value = value.total_seconds() * scaling
    except AttributeError:
        # If that doesn't work, assume it is a value in seconds
        # cast to float so scaled_value is always a float. This allows `timeout=10` to work as expected
        scaled_value = float(value) * scaling

    # ctype integer types don't convert to int from float so we need to
    if library_type in [_visatype.ViInt64, _visatype.ViInt32, _visatype.ViUInt32, _visatype.ViInt16, _visatype.ViUInt16, _visatype.ViInt8]:
        scaled_value = int(scaled_value)

    return scaled_value


def convert_timedelta_to_seconds_real64(value):
    return _convert_timedelta(value, _visatype.ViReal64, 1)


def convert_timedelta_to_milliseconds_int32(value):
    return _convert_timedelta(value, _visatype.ViInt32, 1000)


def convert_timedeltas_to_seconds_real64(values):
    return [convert_timedelta_to_seconds_real64(i) for i in values]


def convert_seconds_real64_to_timedelta(value):
    return hightime.timedelta(seconds=value)


def convert_seconds_real64_to_timedeltas(values):
    return [convert_seconds_real64_to_timedelta(i) for i in values]


def convert_month_to_timedelta(months):
    return hightime.timedelta(days=(30.4167 * months))


# Scaling factor to apply on seconds to get months
# would be 1/(60 seconds * 60 minutes * 24 hours * 30.4167 days)
def convert_timedelta_to_months_int32(value):
    return _convert_timedelta(value, _visatype.ViInt32, 1.0 / (60 * 60 * 24 * 30.4167))


# This converter is not called from the normal codegen path for function. Instead it is
# call from init and is a special case.
def convert_init_with_options_dictionary(values):
    if type(values) is str:
        init_with_options_string = values
    else:
        good_keys = {
            'rangecheck': 'RangeCheck',
            'queryinstrstatus': 'QueryInstrStatus',
            'cache': 'Cache',
            'simulate': 'Simulate',
            'recordcoercions': 'RecordCoercions',
            'interchangecheck': 'InterchangeCheck',
            'driversetup': 'DriverSetup',
            'range_check': 'RangeCheck',
            'query_instr_status': 'QueryInstrStatus',
            'record_coercions': 'RecordCoercions',
            'interchange_check': 'InterchangeCheck',
            'driver_setup': 'DriverSetup',
        }
        init_with_options = []
        for k in sorted(values.keys()):
            value = None
            if k.lower() in good_keys and not good_keys[k.lower()] == 'DriverSetup':
                value = good_keys[k.lower()] + ('=1' if values[k] is True else '=0')
            elif k.lower() in good_keys and good_keys[k.lower()] == 'DriverSetup':
                if not isinstance(values[k], dict):
                    raise TypeError('DriverSetup must be a dictionary')
                value = 'DriverSetup=' + (';'.join([key + ':' + values[k][key] for key in sorted(values[k])]))
            else:
                value = k + ('=1' if values[k] is True else '=0')

            init_with_options.append(value)

        init_with_options_string = ','.join(init_with_options)

    return init_with_options_string


# convert value to bytes
@singledispatch
def _convert_to_bytes(value):  # noqa: F811
    pass


@_convert_to_bytes.register(list)  # noqa: F811
@_convert_to_bytes.register(bytes)  # noqa: F811
@_convert_to_bytes.register(bytearray)  # noqa: F811
@_convert_to_bytes.register(array.array)  # noqa: F811
def _(value):
    return value


@_convert_to_bytes.register(str)  # noqa: F811
def _(value):
    return value.encode()


def convert_to_bytes(value):  # noqa: F811
    return bytes(_convert_to_bytes(value))


def convert_comma_separated_string_to_list(comma_separated_string):
    return [x.strip() for x in comma_separated_string.split(',')]


def convert_list_to_comma_separated_string(list_of_strings):
    '''Convert a list or tuple of strings into a comma-separated string.

    Args:
        list_of_strings (list or tuple of str): List or tuple of strings.

    Returns:
        str: Comma-separated string.
    '''
    if not isinstance(list_of_strings, (list, tuple)) or not all(isinstance(item, str) for item in list_of_strings):
        raise TypeError('Input must be a list or tuple of str')
    return ','.join(list_of_strings)


def convert_chained_repeated_capability_to_parts(chained_repeated_capability):
    '''Convert a chained repeated capabilities string to a list of comma-delimited repeated capabilities string.

    Converter assumes that the input contains the full cartesian product of its parts.
    e.g. If chained_repeated_capability is 'site0/PinA,site0/PinB,site1/PinA,site1/PinB',
    ['site0,site1', 'PinA,PinB'] is returned.

    Args:
        chained_repeated_capability (str) - comma-delimited repeated capabilities string where each
        item is a chain of slash-delimited repeated capabilities

    Returns:
        rep_cap_list (list of str) - list of comma-delimited repeated capabilities string
    '''
    chained_repeated_capability_items = convert_comma_separated_string_to_list(chained_repeated_capability)
    repeated_capability_lists = [[] for _ in range(chained_repeated_capability_items[0].count('/') + 1)]
    for item in chained_repeated_capability_items:
        repeated_capability_lists = [x + [y] for x, y in zip(repeated_capability_lists, item.split('/'))]
    return [','.join(collections.OrderedDict.fromkeys(x)) for x in repeated_capability_lists]
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nirfsg/nirfsg/_grpc_stub_interpreter.py sha256=be6b082f09c8972864c91ed850261910106ea42a42bad11544073397979c3448 bytes=27423 -->
## FILE: generated/nirfsg/nirfsg/_grpc_stub_interpreter.py

- repository: `ni/nimi-python`
- source_path: `generated/nirfsg/nirfsg/_grpc_stub_interpreter.py`
- sha256: `be6b082f09c8972864c91ed850261910106ea42a42bad11544073397979c3448`
- bytes: 27423

````python
# -*- coding: utf-8 -*-
# This file was generated

import grpc
import hightime  # noqa: F401
import session_pb2 as session_grpc_types
import threading
import warnings

from . import enums as enums  # noqa: F401
from . import errors as errors
from . import nidevice_pb2 as grpc_complex_types  # noqa: F401
from . import nirfsg_pb2 as grpc_types
from . import nirfsg_pb2_grpc as nirfsg_grpc


class GrpcStubInterpreter(object):
    '''Interpreter for interacting with a gRPC Stub class'''

    def __init__(self, grpc_options):
        self._grpc_options = grpc_options
        self._lock = threading.RLock()
        self._client = nirfsg_grpc.NiRFSGStub(grpc_options.grpc_channel)
        self.set_session_handle()

    def set_session_handle(self, value=session_grpc_types.Session()):
        self._vi = value

    def get_session_handle(self):
        return self._vi

    def _invoke(self, func, request, metadata=None):
        try:
            response = func(request, metadata=metadata)
            error_code = response.status
            error_message = ''
        except grpc.RpcError as rpc_error:
            error_code = None
            error_message = rpc_error.details()
            for entry in rpc_error.trailing_metadata() or []:
                if entry.key == 'ni-error':
                    value = entry.value if isinstance(entry.value, str) else entry.value.decode('utf-8')
                    try:
                        error_code = int(value)
                    except ValueError:
                        error_message += f'\nError status: {value}'

            grpc_error = rpc_error.code()
            if grpc_error == grpc.StatusCode.NOT_FOUND:
                raise errors.DriverTooOldError() from None
            elif grpc_error == grpc.StatusCode.INVALID_ARGUMENT:
                raise ValueError(error_message) from None
            elif grpc_error == grpc.StatusCode.UNAVAILABLE:
                error_message = 'Failed to connect to server'
            elif grpc_error == grpc.StatusCode.UNIMPLEMENTED:
                error_message = (
                    'This operation is not supported by the NI gRPC Device Server being used. Upgrade NI gRPC Device Server.'
                )

            if error_code is None:
                raise errors.RpcError(grpc_error, error_message) from None

        if error_code < 0:
            raise errors.DriverError(error_code, error_message)
        elif error_code > 0:
            if not error_message:
                try:
                    error_message = self.error_message(error_code)
                except errors.Error:
                    error_message = 'Failed to retrieve error description.'
            warnings.warn(errors.DriverWarning(error_code, error_message))
        return response

    def abort(self):  # noqa: N802
        self._invoke(
            self._client.Abort,
            grpc_types.AbortRequest(vi=self._vi),
        )

    def allocate_arb_waveform(self, waveform_name, size_in_samples):  # noqa: N802
        self._invoke(
            self._client.AllocateArbWaveform,
            grpc_types.AllocateArbWaveformRequest(vi=self._vi, waveform_name=waveform_name, size_in_samples=size_in_samples),
        )

    def change_external_calibration_password(self, old_password, new_password):  # noqa: N802
        self._invoke(
            self._client.ChangeExternalCalibrationPassword,
            grpc_types.ChangeExternalCalibrationPasswordRequest(vi=self._vi, old_password=old_password, new_password=new_password),
        )

    def check_generation_status(self):  # noqa: N802
        response = self._invoke(
            self._client.CheckGenerationStatus,
            grpc_types.CheckGenerationStatusRequest(vi=self._vi),
        )
        return response.is_done

    def check_if_script_exists(self, script_name):  # noqa: N802
        response = self._invoke(
            self._client.CheckIfScriptExists,
            grpc_types.CheckIfScriptExistsRequest(vi=self._vi, script_name=script_name),
        )
        return response.script_exists

    def check_if_waveform_exists(self, waveform_name):  # noqa: N802
        response = self._invoke(
            self._client.CheckIfWaveformExists,
            grpc_types.CheckIfWaveformExistsRequest(vi=self._vi, waveform_name=waveform_name),
        )
        return response.waveform_exists

    def clear_all_arb_waveforms(self):  # noqa: N802
        self._invoke(
            self._client.ClearAllArbWaveforms,
            grpc_types.ClearAllArbWaveformsRequest(vi=self._vi),
        )

    def clear_arb_waveform(self, waveform_name):  # noqa: N802
        self._invoke(
            self._client.ClearArbWaveform,
            grpc_types.ClearArbWaveformRequest(vi=self._vi, name=waveform_name),
        )

    def clear_self_calibrate_range(self):  # noqa: N802
        self._invoke(
            self._client.ClearSelfCalibrateRange,
            grpc_types.ClearSelfCalibrateRangeRequest(vi=self._vi),
        )

    def commit(self):  # noqa: N802
        self._invoke(
            self._client.Commit,
            grpc_types.CommitRequest(vi=self._vi),
        )

    def configure_deembedding_table_interpolation_linear(self, port, table_name, format):  # noqa: N802
        self._invoke(
            self._client.ConfigureDeembeddingTableInterpolationLinear,
            grpc_types.ConfigureDeembeddingTableInterpolationLinearRequest(vi=self._vi, port=port, table_name=table_name, format_raw=format.value),
        )

    def configure_deembedding_table_interpolation_nearest(self, port, table_name):  # noqa: N802
        self._invoke(
            self._client.ConfigureDeembeddingTableInterpolationNearest,
            grpc_types.ConfigureDeembeddingTableInterpolationNearestRequest(vi=self._vi, port=port, table_name=table_name),
        )

    def configure_deembedding_table_interpolation_spline(self, port, table_name):  # noqa: N802
        self._invoke(
            self._client.ConfigureDeembeddingTableInterpolationSpline,
            grpc_types.ConfigureDeembeddingTableInterpolationSplineRequest(vi=self._vi, port=port, table_name=table_name),
        )

    def configure_digital_edge_script_trigger(self, trigger_id, source, edge):  # noqa: N802
        self._invoke(
            self._client.ConfigureDigitalEdgeScriptTrigger,
            grpc_types.ConfigureDigitalEdgeScriptTriggerRequest(vi=self._vi, trigger_id_raw=trigger_id, source_raw=source, edge_raw=edge.value),
        )

    def configure_digital_edge_start_trigger(self, source, edge):  # noqa: N802
        self._invoke(
            self._client.ConfigureDigitalEdgeStartTrigger,
            grpc_types.ConfigureDigitalEdgeStartTriggerRequest(vi=self._vi, source_raw=source, edge_raw=edge.value),
        )

    def configure_digital_level_script_trigger(self, trigger_id, source, level):  # noqa: N802
        self._invoke(
            self._client.ConfigureDigitalLevelScriptTrigger,
            grpc_types.ConfigureDigitalLevelScriptTriggerRequest(vi=self._vi, trigger_id_raw=trigger_id, source=source, level=level),
        )

    def configure_rf(self, frequency, power_level):  # noqa: N802
        self._invoke(
            self._client.ConfigureRF,
            grpc_types.ConfigureRFRequest(vi=self._vi, frequency=frequency, power_level=power_level),
        )

    def configure_ref_clock(self, ref_clock_source, ref_clock_rate):  # noqa: N802
        self._invoke(
            self._client.ConfigureRefClock,
            grpc_types.ConfigureRefClockRequest(vi=self._vi, ref_clock_source=ref_clock_source, ref_clock_rate=ref_clock_rate),
        )

    def configure_software_script_trigger(self, trigger_id):  # noqa: N802
        self._invoke(
            self._client.ConfigureSoftwareScriptTrigger,
            grpc_types.ConfigureSoftwareScriptTriggerRequest(vi=self._vi, trigger_id_raw=trigger_id),
        )

    def configure_software_start_trigger(self):  # noqa: N802
        self._invoke(
            self._client.ConfigureSoftwareStartTrigger,
            grpc_types.ConfigureSoftwareStartTriggerRequest(vi=self._vi),
        )

    def create_deembedding_sparameter_table_array(self, port, table_name, frequencies, sparameter_table, number_of_ports, sparameter_orientation):  # noqa: N802
        # Use ravel() so that gRPC always receives a flat numpy array, regardless of input dimensions.
        sparameter_table_list = [
            grpc_complex_types.NIComplexNumber(real=val.real, imaginary=val.imag)
            for val in sparameter_table.ravel()
        ]
        self._invoke(
            self._client.CreateDeembeddingSparameterTableArray,
            grpc_types.CreateDeembeddingSparameterTableArrayRequest(vi=self._vi, port=port, table_name=table_name, frequencies=frequencies, sparameter_table=sparameter_table_list, number_of_ports=number_of_ports, sparameter_orientation_raw=sparameter_orientation.value),
        )

    def create_deembedding_sparameter_table_s2p_file(self, port, table_name, s2p_file_path, sparameter_orientation):  # noqa: N802
        self._invoke(
            self._client.CreateDeembeddingSparameterTableS2PFile,
            grpc_types.CreateDeembeddingSparameterTableS2PFileRequest(vi=self._vi, port=port, table_name=table_name, s2p_file_path=s2p_file_path, sparameter_orientation_raw=sparameter_orientation.value),
        )

    def delete_all_deembedding_tables(self):  # noqa: N802
        self._invoke(
            self._client.DeleteAllDeembeddingTables,
            grpc_types.DeleteAllDeembeddingTablesRequest(vi=self._vi),
        )

    def delete_deembedding_table(self, port, table_name):  # noqa: N802
        self._invoke(
            self._client.DeleteDeembeddingTable,
            grpc_types.DeleteDeembeddingTableRequest(vi=self._vi, port=port, table_name=table_name),
        )

    def delete_script(self, script_name):  # noqa: N802
        self._invoke(
            self._client.DeleteScript,
            grpc_types.DeleteScriptRequest(vi=self._vi, script_name=script_name),
        )

    def disable_script_trigger(self, trigger_id):  # noqa: N802
        self._invoke(
            self._client.DisableScriptTrigger,
            grpc_types.DisableScriptTriggerRequest(vi=self._vi, trigger_id_raw=trigger_id),
        )

    def disable_start_trigger(self):  # noqa: N802
        self._invoke(
            self._client.DisableStartTrigger,
            grpc_types.DisableStartTriggerRequest(vi=self._vi),
        )

    def error_message(self, error_code):  # noqa: N802
        response = self._invoke(
            self._client.ErrorMessage,
            grpc_types.ErrorMessageRequest(vi=self._vi, error_code=error_code),
        )
        return response.error_message

    def get_all_named_waveform_names(self):  # noqa: N802
        response = self._invoke(
            self._client.GetAllNamedWaveformNames,
            grpc_types.GetAllNamedWaveformNamesRequest(vi=self._vi),
        )
        return response.waveform_names

    def get_all_script_names(self):  # noqa: N802
        response = self._invoke(
            self._client.GetAllScriptNames,
            grpc_types.GetAllScriptNamesRequest(vi=self._vi),
        )
        return response.script_names

    def get_attribute_vi_boolean(self, channel_name, attribute):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViBoolean,
            grpc_types.GetAttributeViBooleanRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute),
        )
        return response.value

    def get_attribute_vi_int32(self, channel_name, attribute):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViInt32,
            grpc_types.GetAttributeViInt32Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute),
        )
        return response.value

    def get_attribute_vi_int64(self, channel_name, attribute):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViInt64,
            grpc_types.GetAttributeViInt64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute),
        )
        return response.value

    def get_attribute_vi_real64(self, channel_name, attribute):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViReal64,
            grpc_types.GetAttributeViReal64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute),
        )
        return response.value

    def get_attribute_vi_session(self, channel_name, attribute):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViSession,
            grpc_types.GetAttributeViSessionRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute),
        )
        return response.value

    def get_attribute_vi_string(self, channel_name, attribute):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViString,
            grpc_types.GetAttributeViStringRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute),
        )
        return response.value

    def get_deembedding_sparameters(self):
        import numpy as np
        response = self._invoke(
            self._client.GetDeembeddingSparameters,
            grpc_types.GetDeembeddingSparametersRequest(vi=self._vi),
        )
        number_of_ports = response.number_of_ports
        sparameters = np.array([c.real + 1j * c.imaginary for c in response.sparameters], dtype=np.complex128)
        sparameters = sparameters.reshape((number_of_ports, number_of_ports))
        return sparameters

    def get_deembedding_table_number_of_ports(self):  # noqa: N802
        response = self._invoke(
            self._client.GetDeembeddingTableNumberOfPorts,
            grpc_types.GetDeembeddingTableNumberOfPortsRequest(vi=self._vi),
        )
        return response.number_of_ports

    def get_error(self):  # noqa: N802
        response = self._invoke(
            self._client.GetError,
            grpc_types.GetErrorRequest(vi=self._vi),
        )
        return response.error_code, response.error_description

    def get_external_calibration_last_date_and_time(self):  # noqa: N802
        response = self._invoke(
            self._client.GetExternalCalibrationLastDateAndTime,
            grpc_types.GetExternalCalibrationLastDateAndTimeRequest(vi=self._vi),
        )
        return response.year, response.month, response.day, response.hour, response.minute, response.second

    def get_max_settable_power(self):  # noqa: N802
        response = self._invoke(
            self._client.GetMaxSettablePower,
            grpc_types.GetMaxSettablePowerRequest(vi=self._vi),
        )
        return response.value

    def get_script(self, script_name):  # noqa: N802
        response = self._invoke(
            self._client.GetScript,
            grpc_types.GetScriptRequest(vi=self._vi, script_name=script_name),
        )
        return response.script

    def get_self_calibration_date_and_time(self, module):  # noqa: N802
        response = self._invoke(
            self._client.GetSelfCalibrationDateAndTime,
            grpc_types.GetSelfCalibrationDateAndTimeRequest(vi=self._vi, module=module.value),
        )
        return response.year, response.month, response.day, response.hour, response.minute, response.second

    def get_self_calibration_temperature(self, module):  # noqa: N802
        response = self._invoke(
            self._client.GetSelfCalibrationTemperature,
            grpc_types.GetSelfCalibrationTemperatureRequest(vi=self._vi, module_raw=module.value),
        )
        return response.temperature

    def get_terminal_name(self, signal, signal_identifier):  # noqa: N802
        response = self._invoke(
            self._client.GetTerminalName,
            grpc_types.GetTerminalNameRequest(vi=self._vi, signal_raw=signal.value, signal_identifier_raw=signal_identifier),
        )
        return response.terminal_name

    def get_waveform_burst_start_locations(self, channel_name):  # noqa: N802
        response = self._invoke(
            self._client.GetWaveformBurstStartLocations,
            grpc_types.GetWaveformBurstStartLocationsRequest(vi=self._vi, channel_name=channel_name),
        )
        return response.locations

    def get_waveform_burst_stop_locations(self, channel_name):  # noqa: N802
        response = self._invoke(
            self._client.GetWaveformBurstStopLocations,
            grpc_types.GetWaveformBurstStopLocationsRequest(vi=self._vi, channel_name=channel_name),
        )
        return response.locations

    def get_waveform_marker_event_locations(self, channel_name):  # noqa: N802
        response = self._invoke(
            self._client.GetWaveformMarkerEventLocations,
            grpc_types.GetWaveformMarkerEventLocationsRequest(vi=self._vi, channel_name=channel_name),
        )
        return response.locations

    def init_with_options(self, resource_name, id_query, reset_device, option_string):  # noqa: N802
        metadata = (
            ('ni-api-key', self._grpc_options.api_key),
        )
        response = self._invoke(
            self._client.InitWithOptions,
            grpc_types.InitWithOptionsRequest(resource_name=resource_name, id_query=id_query, reset_device=reset_device, option_string=option_string, session_name=self._grpc_options.session_name, initialization_behavior=self._grpc_options.initialization_behavior),
            metadata=metadata,
        )
        self._close_on_exit = response.new_session_initialized
        return response.vi

    def initiate(self):  # noqa: N802
        self._invoke(
            self._client.Initiate,
            grpc_types.InitiateRequest(vi=self._vi),
        )

    def load_configurations_from_file(self, channel_name, file_path):  # noqa: N802
        self._invoke(
            self._client.LoadConfigurationsFromFile,
            grpc_types.LoadConfigurationsFromFileRequest(vi=self._vi, channel_name=channel_name, file_path=file_path),
        )

    def lock(self):  # noqa: N802
        self._lock.acquire()

    def perform_power_search(self):  # noqa: N802
        self._invoke(
            self._client.PerformPowerSearch,
            grpc_types.PerformPowerSearchRequest(vi=self._vi),
        )

    def perform_thermal_correction(self):  # noqa: N802
        self._invoke(
            self._client.PerformThermalCorrection,
            grpc_types.PerformThermalCorrectionRequest(vi=self._vi),
        )

    def query_arb_waveform_capabilities(self):  # noqa: N802
        response = self._invoke(
            self._client.QueryArbWaveformCapabilities,
            grpc_types.QueryArbWaveformCapabilitiesRequest(vi=self._vi),
        )
        return response.max_number_waveforms, response.waveform_quantum, response.min_waveform_size, response.max_waveform_size

    def read_and_download_waveform_from_file_tdms(self, waveform_name, file_path, waveform_index):  # noqa: N802
        self._invoke(
            self._client.ReadAndDownloadWaveformFromFileTDMS,
            grpc_types.ReadAndDownloadWaveformFromFileTDMSRequest(vi=self._vi, waveform_name=waveform_name, file_path=file_path, waveform_index=waveform_index),
        )

    def reset_device(self):  # noqa: N802
        self._invoke(
            self._client.ResetDevice,
            grpc_types.ResetDeviceRequest(vi=self._vi),
        )

    def reset_with_defaults(self):  # noqa: N802
        self._invoke(
            self._client.ResetWithDefaults,
            grpc_types.ResetWithDefaultsRequest(vi=self._vi),
        )

    def reset_with_options(self, steps_to_omit):  # noqa: N802
        self._invoke(
            self._client.ResetWithOptions,
            grpc_types.ResetWithOptionsRequest(vi=self._vi, steps_to_omit_raw=steps_to_omit.value),
        )

    def save_configurations_to_file(self, channel_name, file_path):  # noqa: N802
        self._invoke(
            self._client.SaveConfigurationsToFile,
            grpc_types.SaveConfigurationsToFileRequest(vi=self._vi, channel_name=channel_name, file_path=file_path),
        )

    def select_arb_waveform(self, waveform_name):  # noqa: N802
        self._invoke(
            self._client.SelectArbWaveform,
            grpc_types.SelectArbWaveformRequest(vi=self._vi, name=waveform_name),
        )

    def self_cal(self):  # noqa: N802
        self._invoke(
            self._client.SelfCal,
            grpc_types.SelfCalRequest(vi=self._vi),
        )

    def self_calibrate_range(self, steps_to_omit, min_frequency, max_frequency, min_power_level, max_power_level):  # noqa: N802
        self._invoke(
            self._client.SelfCalibrateRange,
            grpc_types.SelfCalibrateRangeRequest(vi=self._vi, steps_to_omit_raw=steps_to_omit.value, min_frequency=min_frequency, max_frequency=max_frequency, min_power_level=min_power_level, max_power_level=max_power_level),
        )

    def send_software_edge_trigger(self, trigger, trigger_identifier):  # noqa: N802
        self._invoke(
            self._client.SendSoftwareEdgeTrigger,
            grpc_types.SendSoftwareEdgeTriggerRequest(vi=self._vi, trigger_raw=trigger.value, trigger_identifier_raw=trigger_identifier.value),
        )

    def set_arb_waveform_next_write_position(self, waveform_name, relative_to, offset):  # noqa: N802
        self._invoke(
            self._client.SetArbWaveformNextWritePosition,
            grpc_types.SetArbWaveformNextWritePositionRequest(vi=self._vi, waveform_name=waveform_name, relative_to_raw=relative_to.value, offset=offset),
        )

    def set_attribute_vi_boolean(self, channel_name, attribute, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViBoolean,
            grpc_types.SetAttributeViBooleanRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute, value=value),
        )

    def set_attribute_vi_int32(self, channel_name, attribute, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViInt32,
            grpc_types.SetAttributeViInt32Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute, value_raw=value),
        )

    def set_attribute_vi_int64(self, channel_name, attribute, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViInt64,
            grpc_types.SetAttributeViInt64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute, value_raw=value),
        )

    def set_attribute_vi_real64(self, channel_name, attribute, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViReal64,
            grpc_types.SetAttributeViReal64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute, value_raw=value),
        )

    def set_attribute_vi_session(self, channel_name, attribute):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViSession,
            grpc_types.SetAttributeViSessionRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute, value=self._vi),
        )

    def set_attribute_vi_string(self, channel_name, attribute, value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViString,
            grpc_types.SetAttributeViStringRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute, value_raw=value),
        )

    def set_waveform_burst_start_locations(self, channel_name, locations):  # noqa: N802
        self._invoke(
            self._client.SetWaveformBurstStartLocations,
            grpc_types.SetWaveformBurstStartLocationsRequest(vi=self._vi, channel_name=channel_name, locations=locations),
        )

    def set_waveform_burst_stop_locations(self, channel_name, locations):  # noqa: N802
        self._invoke(
            self._client.SetWaveformBurstStopLocations,
            grpc_types.SetWaveformBurstStopLocationsRequest(vi=self._vi, channel_name=channel_name, locations=locations),
        )

    def set_waveform_marker_event_locations(self, channel_name, locations):  # noqa: N802
        self._invoke(
            self._client.SetWaveformMarkerEventLocations,
            grpc_types.SetWaveformMarkerEventLocationsRequest(vi=self._vi, channel_name=channel_name, locations=locations),
        )

    def unlock(self):  # noqa: N802
        self._lock.release()

    def wait_until_settled(self, max_time_milliseconds):  # noqa: N802
        self._invoke(
            self._client.WaitUntilSettled,
            grpc_types.WaitUntilSettledRequest(vi=self._vi, max_time_milliseconds=max_time_milliseconds),
        )

    def write_arb_waveform_complex_f32(self, waveform_name, waveform_data_array, more_data_pending):  # noqa: N802
        # Use ravel() so that gRPC always receives a flat numpy array, regardless of input dimensions.
        waveform_data_array_list = [
            grpc_complex_types.NIComplexNumberF32(real=val.real, imaginary=val.imag)
            for val in waveform_data_array.ravel()
        ]
        self._invoke(
            self._client.WriteArbWaveformComplexF32,
            grpc_types.WriteArbWaveformComplexF32Request(vi=self._vi, waveform_name=waveform_name, wfm_data=waveform_data_array_list, more_data_pending=more_data_pending),
        )

    def write_arb_waveform_complex_f64(self, waveform_name, waveform_data_array, more_data_pending):  # noqa: N802
        # Use ravel() so that gRPC always receives a flat numpy array, regardless of input dimensions.
        waveform_data_array_list = [
            grpc_complex_types.NIComplexNumber(real=val.real, imaginary=val.imag)
            for val in waveform_data_array.ravel()
        ]
        self._invoke(
            self._client.WriteArbWaveformComplexF64,
            grpc_types.WriteArbWaveformComplexF64Request(vi=self._vi, waveform_name=waveform_name, wfm_data=waveform_data_array_list, more_data_pending=more_data_pending),
        )

    def write_arb_waveform_complex_i16(self, waveform_name, waveform_data_array):  # noqa: N802
        # Use ravel() so that gRPC always receives a flat numpy array, regardless of input dimensions.
        arr = waveform_data_array.ravel()
        if arr.size % 2 != 0:
            raise ValueError("Interleaved int16 array must have even length (real/imag pairs)")
        arr_pairs = arr.reshape(-1, 2)
        waveform_data_array_list = [
            grpc_complex_types.NIComplexI16(real=int(pair[0]), imaginary=int(pair[1]))
            for pair in arr_pairs
        ]
        self._invoke(
            self._client.WriteArbWaveformComplexI16,
            grpc_types.WriteArbWaveformComplexI16Request(vi=self._vi, waveform_name=waveform_name, wfm_data=waveform_data_array_list),
        )

    def write_script(self, script):  # noqa: N802
        self._invoke(
            self._client.WriteScript,
            grpc_types.WriteScriptRequest(vi=self._vi, script=script),
        )

    def close(self):  # noqa: N802
        self._invoke(
            self._client.Close,
            grpc_types.CloseRequest(vi=self._vi),
        )

    def reset(self):  # noqa: N802
        self._invoke(
            self._client.Reset,
            grpc_types.ResetRequest(vi=self._vi),
        )

    def self_test(self):  # noqa: N802
        response = self._invoke(
            self._client.SelfTest,
            grpc_types.SelfTestRequest(vi=self._vi),
        )
        return response.self_test_result, response.self_test_message
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nirfsg/nirfsg/_library.py sha256=e3370544dfc0905bb72ae966128938009183c82d7131760fa006f826a7dee153 bytes=57388 -->
## FILE: generated/nirfsg/nirfsg/_library.py

- repository: `ni/nimi-python`
- source_path: `generated/nirfsg/nirfsg/_library.py`
- sha256: `e3370544dfc0905bb72ae966128938009183c82d7131760fa006f826a7dee153`
- bytes: 57388

````python
# -*- coding: utf-8 -*-
# This file was generated

import ctypes
import nirfsg.errors as errors
import threading

from nirfsg._complextype import *  # noqa: F403
from nirfsg._visatype import *  # noqa: F403,H303


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
        self.niRFSG_Abort_cfunc = None
        self.niRFSG_AllocateArbWaveform_cfunc = None
        self.niRFSG_ChangeExternalCalibrationPassword_cfunc = None
        self.niRFSG_CheckGenerationStatus_cfunc = None
        self.niRFSG_CheckIfScriptExists_cfunc = None
        self.niRFSG_CheckIfWaveformExists_cfunc = None
        self.niRFSG_ClearAllArbWaveforms_cfunc = None
        self.niRFSG_ClearArbWaveform_cfunc = None
        self.niRFSG_ClearSelfCalibrateRange_cfunc = None
        self.niRFSG_Commit_cfunc = None
        self.niRFSG_ConfigureDeembeddingTableInterpolationLinear_cfunc = None
        self.niRFSG_ConfigureDeembeddingTableInterpolationNearest_cfunc = None
        self.niRFSG_ConfigureDeembeddingTableInterpolationSpline_cfunc = None
        self.niRFSG_ConfigureDigitalEdgeScriptTrigger_cfunc = None
        self.niRFSG_ConfigureDigitalEdgeStartTrigger_cfunc = None
        self.niRFSG_ConfigureDigitalLevelScriptTrigger_cfunc = None
        self.niRFSG_ConfigureRF_cfunc = None
        self.niRFSG_ConfigureRefClock_cfunc = None
        self.niRFSG_ConfigureSoftwareScriptTrigger_cfunc = None
        self.niRFSG_ConfigureSoftwareStartTrigger_cfunc = None
        self.niRFSG_CreateDeembeddingSparameterTableArray_cfunc = None
        self.niRFSG_CreateDeembeddingSparameterTableS2PFile_cfunc = None
        self.niRFSG_DeleteAllDeembeddingTables_cfunc = None
        self.niRFSG_DeleteDeembeddingTable_cfunc = None
        self.niRFSG_DeleteScript_cfunc = None
        self.niRFSG_DisableScriptTrigger_cfunc = None
        self.niRFSG_DisableStartTrigger_cfunc = None
        self.niRFSG_ErrorMessage_cfunc = None
        self.niRFSG_GetAllNamedWaveformNames_cfunc = None
        self.niRFSG_GetAllScriptNames_cfunc = None
        self.niRFSG_GetAttributeViBoolean_cfunc = None
        self.niRFSG_GetAttributeViInt32_cfunc = None
        self.niRFSG_GetAttributeViInt64_cfunc = None
        self.niRFSG_GetAttributeViReal64_cfunc = None
        self.niRFSG_GetAttributeViSession_cfunc = None
        self.niRFSG_GetAttributeViString_cfunc = None
        self.niRFSG_GetDeembeddingSparameters_cfunc = None
        self.niRFSG_GetDeembeddingTableNumberOfPorts_cfunc = None
        self.niRFSG_GetError_cfunc = None
        self.niRFSG_GetExternalCalibrationLastDateAndTime_cfunc = None
        self.niRFSG_GetMaxSettablePower_cfunc = None
        self.niRFSG_GetScript_cfunc = None
        self.niRFSG_GetSelfCalibrationDateAndTime_cfunc = None
        self.niRFSG_GetSelfCalibrationTemperature_cfunc = None
        self.niRFSG_GetTerminalName_cfunc = None
        self.niRFSG_GetWaveformBurstStartLocations_cfunc = None
        self.niRFSG_GetWaveformBurstStopLocations_cfunc = None
        self.niRFSG_GetWaveformMarkerEventLocations_cfunc = None
        self.niRFSG_InitWithOptions_cfunc = None
        self.niRFSG_Initiate_cfunc = None
        self.niRFSG_LoadConfigurationsFromFile_cfunc = None
        self.niRFSG_LockSession_cfunc = None
        self.niRFSG_PerformPowerSearch_cfunc = None
        self.niRFSG_PerformThermalCorrection_cfunc = None
        self.niRFSG_QueryArbWaveformCapabilities_cfunc = None
        self.niRFSG_ReadAndDownloadWaveformFromFileTDMS_cfunc = None
        self.niRFSG_ResetDevice_cfunc = None
        self.niRFSG_ResetWithDefaults_cfunc = None
        self.niRFSG_ResetWithOptions_cfunc = None
        self.niRFSG_SaveConfigurationsToFile_cfunc = None
        self.niRFSG_SelectArbWaveform_cfunc = None
        self.niRFSG_SelfCal_cfunc = None
        self.niRFSG_SelfCalibrateRange_cfunc = None
        self.niRFSG_SendSoftwareEdgeTrigger_cfunc = None
        self.niRFSG_SetArbWaveformNextWritePosition_cfunc = None
        self.niRFSG_SetAttributeViBoolean_cfunc = None
        self.niRFSG_SetAttributeViInt32_cfunc = None
        self.niRFSG_SetAttributeViInt64_cfunc = None
        self.niRFSG_SetAttributeViReal64_cfunc = None
        self.niRFSG_SetAttributeViSession_cfunc = None
        self.niRFSG_SetAttributeViString_cfunc = None
        self.niRFSG_SetWaveformBurstStartLocations_cfunc = None
        self.niRFSG_SetWaveformBurstStopLocations_cfunc = None
        self.niRFSG_SetWaveformMarkerEventLocations_cfunc = None
        self.niRFSG_UnlockSession_cfunc = None
        self.niRFSG_WaitUntilSettled_cfunc = None
        self.niRFSG_WriteArbWaveformComplexF32_cfunc = None
        self.niRFSG_WriteArbWaveformComplexF64_cfunc = None
        self.niRFSG_WriteArbWaveformComplexI16_cfunc = None
        self.niRFSG_WriteScript_cfunc = None
        self.niRFSG_close_cfunc = None
        self.niRFSG_reset_cfunc = None
        self.niRFSG_self_test_cfunc = None

    def _get_library_function(self, name):
        try:
            function = getattr(self._library, name)
        except AttributeError as e:
            raise errors.DriverTooOldError() from e
        return function

    def niRFSG_Abort(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_Abort_cfunc is None:
                self.niRFSG_Abort_cfunc = self._get_library_function('niRFSG_Abort')
                self.niRFSG_Abort_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_Abort_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_Abort_cfunc(vi)

    def niRFSG_AllocateArbWaveform(self, vi, waveform_name, size_in_samples):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_AllocateArbWaveform_cfunc is None:
                self.niRFSG_AllocateArbWaveform_cfunc = self._get_library_function('niRFSG_AllocateArbWaveform')
                self.niRFSG_AllocateArbWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niRFSG_AllocateArbWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_AllocateArbWaveform_cfunc(vi, waveform_name, size_in_samples)

    def niRFSG_ChangeExternalCalibrationPassword(self, vi, old_password, new_password):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ChangeExternalCalibrationPassword_cfunc is None:
                self.niRFSG_ChangeExternalCalibrationPassword_cfunc = self._get_library_function('niRFSG_ChangeExternalCalibrationPassword')
                self.niRFSG_ChangeExternalCalibrationPassword_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_ChangeExternalCalibrationPassword_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ChangeExternalCalibrationPassword_cfunc(vi, old_password, new_password)

    def niRFSG_CheckGenerationStatus(self, vi, is_done):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_CheckGenerationStatus_cfunc is None:
                self.niRFSG_CheckGenerationStatus_cfunc = self._get_library_function('niRFSG_CheckGenerationStatus')
                self.niRFSG_CheckGenerationStatus_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niRFSG_CheckGenerationStatus_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_CheckGenerationStatus_cfunc(vi, is_done)

    def niRFSG_CheckIfScriptExists(self, vi, script_name, script_exists):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_CheckIfScriptExists_cfunc is None:
                self.niRFSG_CheckIfScriptExists_cfunc = self._get_library_function('niRFSG_CheckIfScriptExists')
                self.niRFSG_CheckIfScriptExists_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niRFSG_CheckIfScriptExists_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_CheckIfScriptExists_cfunc(vi, script_name, script_exists)

    def niRFSG_CheckIfWaveformExists(self, vi, waveform_name, waveform_exists):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_CheckIfWaveformExists_cfunc is None:
                self.niRFSG_CheckIfWaveformExists_cfunc = self._get_library_function('niRFSG_CheckIfWaveformExists')
                self.niRFSG_CheckIfWaveformExists_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niRFSG_CheckIfWaveformExists_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_CheckIfWaveformExists_cfunc(vi, waveform_name, waveform_exists)

    def niRFSG_ClearAllArbWaveforms(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ClearAllArbWaveforms_cfunc is None:
                self.niRFSG_ClearAllArbWaveforms_cfunc = self._get_library_function('niRFSG_ClearAllArbWaveforms')
                self.niRFSG_ClearAllArbWaveforms_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_ClearAllArbWaveforms_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ClearAllArbWaveforms_cfunc(vi)

    def niRFSG_ClearArbWaveform(self, vi, waveform_name):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ClearArbWaveform_cfunc is None:
                self.niRFSG_ClearArbWaveform_cfunc = self._get_library_function('niRFSG_ClearArbWaveform')
                self.niRFSG_ClearArbWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_ClearArbWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ClearArbWaveform_cfunc(vi, waveform_name)

    def niRFSG_ClearSelfCalibrateRange(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ClearSelfCalibrateRange_cfunc is None:
                self.niRFSG_ClearSelfCalibrateRange_cfunc = self._get_library_function('niRFSG_ClearSelfCalibrateRange')
                self.niRFSG_ClearSelfCalibrateRange_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_ClearSelfCalibrateRange_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ClearSelfCalibrateRange_cfunc(vi)

    def niRFSG_Commit(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_Commit_cfunc is None:
                self.niRFSG_Commit_cfunc = self._get_library_function('niRFSG_Commit')
                self.niRFSG_Commit_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_Commit_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_Commit_cfunc(vi)

    def niRFSG_ConfigureDeembeddingTableInterpolationLinear(self, vi, port, table_name, format):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ConfigureDeembeddingTableInterpolationLinear_cfunc is None:
                self.niRFSG_ConfigureDeembeddingTableInterpolationLinear_cfunc = self._get_library_function('niRFSG_ConfigureDeembeddingTableInterpolationLinear')
                self.niRFSG_ConfigureDeembeddingTableInterpolationLinear_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niRFSG_ConfigureDeembeddingTableInterpolationLinear_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ConfigureDeembeddingTableInterpolationLinear_cfunc(vi, port, table_name, format)

    def niRFSG_ConfigureDeembeddingTableInterpolationNearest(self, vi, port, table_name):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ConfigureDeembeddingTableInterpolationNearest_cfunc is None:
                self.niRFSG_ConfigureDeembeddingTableInterpolationNearest_cfunc = self._get_library_function('niRFSG_ConfigureDeembeddingTableInterpolationNearest')
                self.niRFSG_ConfigureDeembeddingTableInterpolationNearest_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_ConfigureDeembeddingTableInterpolationNearest_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ConfigureDeembeddingTableInterpolationNearest_cfunc(vi, port, table_name)

    def niRFSG_ConfigureDeembeddingTableInterpolationSpline(self, vi, port, table_name):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ConfigureDeembeddingTableInterpolationSpline_cfunc is None:
                self.niRFSG_ConfigureDeembeddingTableInterpolationSpline_cfunc = self._get_library_function('niRFSG_ConfigureDeembeddingTableInterpolationSpline')
                self.niRFSG_ConfigureDeembeddingTableInterpolationSpline_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_ConfigureDeembeddingTableInterpolationSpline_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ConfigureDeembeddingTableInterpolationSpline_cfunc(vi, port, table_name)

    def niRFSG_ConfigureDigitalEdgeScriptTrigger(self, vi, trigger_id, source, edge):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ConfigureDigitalEdgeScriptTrigger_cfunc is None:
                self.niRFSG_ConfigureDigitalEdgeScriptTrigger_cfunc = self._get_library_function('niRFSG_ConfigureDigitalEdgeScriptTrigger')
                self.niRFSG_ConfigureDigitalEdgeScriptTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niRFSG_ConfigureDigitalEdgeScriptTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ConfigureDigitalEdgeScriptTrigger_cfunc(vi, trigger_id, source, edge)

    def niRFSG_ConfigureDigitalEdgeStartTrigger(self, vi, source, edge):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ConfigureDigitalEdgeStartTrigger_cfunc is None:
                self.niRFSG_ConfigureDigitalEdgeStartTrigger_cfunc = self._get_library_function('niRFSG_ConfigureDigitalEdgeStartTrigger')
                self.niRFSG_ConfigureDigitalEdgeStartTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niRFSG_ConfigureDigitalEdgeStartTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ConfigureDigitalEdgeStartTrigger_cfunc(vi, source, edge)

    def niRFSG_ConfigureDigitalLevelScriptTrigger(self, vi, trigger_id, source, level):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ConfigureDigitalLevelScriptTrigger_cfunc is None:
                self.niRFSG_ConfigureDigitalLevelScriptTrigger_cfunc = self._get_library_function('niRFSG_ConfigureDigitalLevelScriptTrigger')
                self.niRFSG_ConfigureDigitalLevelScriptTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niRFSG_ConfigureDigitalLevelScriptTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ConfigureDigitalLevelScriptTrigger_cfunc(vi, trigger_id, source, level)

    def niRFSG_ConfigureRF(self, vi, frequency, power_level):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ConfigureRF_cfunc is None:
                self.niRFSG_ConfigureRF_cfunc = self._get_library_function('niRFSG_ConfigureRF')
                self.niRFSG_ConfigureRF_cfunc.argtypes = [ViSession, ViReal64, ViReal64]  # noqa: F405
                self.niRFSG_ConfigureRF_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ConfigureRF_cfunc(vi, frequency, power_level)

    def niRFSG_ConfigureRefClock(self, vi, ref_clock_source, ref_clock_rate):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ConfigureRefClock_cfunc is None:
                self.niRFSG_ConfigureRefClock_cfunc = self._get_library_function('niRFSG_ConfigureRefClock')
                self.niRFSG_ConfigureRefClock_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64]  # noqa: F405
                self.niRFSG_ConfigureRefClock_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ConfigureRefClock_cfunc(vi, ref_clock_source, ref_clock_rate)

    def niRFSG_ConfigureSoftwareScriptTrigger(self, vi, trigger_id):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ConfigureSoftwareScriptTrigger_cfunc is None:
                self.niRFSG_ConfigureSoftwareScriptTrigger_cfunc = self._get_library_function('niRFSG_ConfigureSoftwareScriptTrigger')
                self.niRFSG_ConfigureSoftwareScriptTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_ConfigureSoftwareScriptTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ConfigureSoftwareScriptTrigger_cfunc(vi, trigger_id)

    def niRFSG_ConfigureSoftwareStartTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ConfigureSoftwareStartTrigger_cfunc is None:
                self.niRFSG_ConfigureSoftwareStartTrigger_cfunc = self._get_library_function('niRFSG_ConfigureSoftwareStartTrigger')
                self.niRFSG_ConfigureSoftwareStartTrigger_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_ConfigureSoftwareStartTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ConfigureSoftwareStartTrigger_cfunc(vi)

    def niRFSG_CreateDeembeddingSparameterTableArray(self, vi, port, table_name, frequencies, frequencies_size, sparameter_table, sparameter_table_size, number_of_ports, sparameter_orientation):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_CreateDeembeddingSparameterTableArray_cfunc is None:
                self.niRFSG_CreateDeembeddingSparameterTableArray_cfunc = self._get_library_function('niRFSG_CreateDeembeddingSparameterTableArray')
                self.niRFSG_CreateDeembeddingSparameterTableArray_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViReal64), ViInt32, ctypes.POINTER(NIComplexNumber), ViInt32, ViInt32, ViInt32]  # noqa: F405
                self.niRFSG_CreateDeembeddingSparameterTableArray_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_CreateDeembeddingSparameterTableArray_cfunc(vi, port, table_name, frequencies, frequencies_size, sparameter_table, sparameter_table_size, number_of_ports, sparameter_orientation)

    def niRFSG_CreateDeembeddingSparameterTableS2PFile(self, vi, port, table_name, s2p_file_path, sparameter_orientation):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_CreateDeembeddingSparameterTableS2PFile_cfunc is None:
                self.niRFSG_CreateDeembeddingSparameterTableS2PFile_cfunc = self._get_library_function('niRFSG_CreateDeembeddingSparameterTableS2PFile')
                self.niRFSG_CreateDeembeddingSparameterTableS2PFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niRFSG_CreateDeembeddingSparameterTableS2PFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_CreateDeembeddingSparameterTableS2PFile_cfunc(vi, port, table_name, s2p_file_path, sparameter_orientation)

    def niRFSG_DeleteAllDeembeddingTables(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_DeleteAllDeembeddingTables_cfunc is None:
                self.niRFSG_DeleteAllDeembeddingTables_cfunc = self._get_library_function('niRFSG_DeleteAllDeembeddingTables')
                self.niRFSG_DeleteAllDeembeddingTables_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_DeleteAllDeembeddingTables_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_DeleteAllDeembeddingTables_cfunc(vi)

    def niRFSG_DeleteDeembeddingTable(self, vi, port, table_name):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_DeleteDeembeddingTable_cfunc is None:
                self.niRFSG_DeleteDeembeddingTable_cfunc = self._get_library_function('niRFSG_DeleteDeembeddingTable')
                self.niRFSG_DeleteDeembeddingTable_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_DeleteDeembeddingTable_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_DeleteDeembeddingTable_cfunc(vi, port, table_name)

    def niRFSG_DeleteScript(self, vi, script_name):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_DeleteScript_cfunc is None:
                self.niRFSG_DeleteScript_cfunc = self._get_library_function('niRFSG_DeleteScript')
                self.niRFSG_DeleteScript_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_DeleteScript_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_DeleteScript_cfunc(vi, script_name)

    def niRFSG_DisableScriptTrigger(self, vi, trigger_id):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_DisableScriptTrigger_cfunc is None:
                self.niRFSG_DisableScriptTrigger_cfunc = self._get_library_function('niRFSG_DisableScriptTrigger')
                self.niRFSG_DisableScriptTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_DisableScriptTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_DisableScriptTrigger_cfunc(vi, trigger_id)

    def niRFSG_DisableStartTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_DisableStartTrigger_cfunc is None:
                self.niRFSG_DisableStartTrigger_cfunc = self._get_library_function('niRFSG_DisableStartTrigger')
                self.niRFSG_DisableStartTrigger_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_DisableStartTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_DisableStartTrigger_cfunc(vi)

    def niRFSG_ErrorMessage(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ErrorMessage_cfunc is None:
                self.niRFSG_ErrorMessage_cfunc = self._get_library_function('niRFSG_ErrorMessage')
                self.niRFSG_ErrorMessage_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_ErrorMessage_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ErrorMessage_cfunc(vi, error_code, error_message)

    def niRFSG_GetAllNamedWaveformNames(self, vi, waveform_names, buffer_size, actual_buffer_size):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetAllNamedWaveformNames_cfunc is None:
                self.niRFSG_GetAllNamedWaveformNames_cfunc = self._get_library_function('niRFSG_GetAllNamedWaveformNames')
                self.niRFSG_GetAllNamedWaveformNames_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSG_GetAllNamedWaveformNames_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetAllNamedWaveformNames_cfunc(vi, waveform_names, buffer_size, actual_buffer_size)

    def niRFSG_GetAllScriptNames(self, vi, script_names, buffer_size, actual_buffer_size):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetAllScriptNames_cfunc is None:
                self.niRFSG_GetAllScriptNames_cfunc = self._get_library_function('niRFSG_GetAllScriptNames')
                self.niRFSG_GetAllScriptNames_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSG_GetAllScriptNames_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetAllScriptNames_cfunc(vi, script_names, buffer_size, actual_buffer_size)

    def niRFSG_GetAttributeViBoolean(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetAttributeViBoolean_cfunc is None:
                self.niRFSG_GetAttributeViBoolean_cfunc = self._get_library_function('niRFSG_GetAttributeViBoolean')
                self.niRFSG_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niRFSG_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetAttributeViBoolean_cfunc(vi, channel_name, attribute, value)

    def niRFSG_GetAttributeViInt32(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetAttributeViInt32_cfunc is None:
                self.niRFSG_GetAttributeViInt32_cfunc = self._get_library_function('niRFSG_GetAttributeViInt32')
                self.niRFSG_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSG_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetAttributeViInt32_cfunc(vi, channel_name, attribute, value)

    def niRFSG_GetAttributeViInt64(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetAttributeViInt64_cfunc is None:
                self.niRFSG_GetAttributeViInt64_cfunc = self._get_library_function('niRFSG_GetAttributeViInt64')
                self.niRFSG_GetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niRFSG_GetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetAttributeViInt64_cfunc(vi, channel_name, attribute, value)

    def niRFSG_GetAttributeViReal64(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetAttributeViReal64_cfunc is None:
                self.niRFSG_GetAttributeViReal64_cfunc = self._get_library_function('niRFSG_GetAttributeViReal64')
                self.niRFSG_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niRFSG_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetAttributeViReal64_cfunc(vi, channel_name, attribute, value)

    def niRFSG_GetAttributeViSession(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetAttributeViSession_cfunc is None:
                self.niRFSG_GetAttributeViSession_cfunc = self._get_library_function('niRFSG_GetAttributeViSession')
                self.niRFSG_GetAttributeViSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViSession)]  # noqa: F405
                self.niRFSG_GetAttributeViSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetAttributeViSession_cfunc(vi, channel_name, attribute, value)

    def niRFSG_GetAttributeViString(self, vi, channel_name, attribute, buf_size, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetAttributeViString_cfunc is None:
                self.niRFSG_GetAttributeViString_cfunc = self._get_library_function('niRFSG_GetAttributeViString')
                self.niRFSG_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetAttributeViString_cfunc(vi, channel_name, attribute, buf_size, value)

    def niRFSG_GetDeembeddingSparameters(self, vi, sparameters, sparameters_array_size, number_of_sparameters, number_of_ports):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetDeembeddingSparameters_cfunc is None:
                self.niRFSG_GetDeembeddingSparameters_cfunc = self._get_library_function('niRFSG_GetDeembeddingSparameters')
                self.niRFSG_GetDeembeddingSparameters_cfunc.argtypes = [ViSession, ctypes.POINTER(NIComplexNumber), ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSG_GetDeembeddingSparameters_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetDeembeddingSparameters_cfunc(vi, sparameters, sparameters_array_size, number_of_sparameters, number_of_ports)

    def niRFSG_GetDeembeddingTableNumberOfPorts(self, vi, number_of_ports):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetDeembeddingTableNumberOfPorts_cfunc is None:
                self.niRFSG_GetDeembeddingTableNumberOfPorts_cfunc = self._get_library_function('niRFSG_GetDeembeddingTableNumberOfPorts')
                self.niRFSG_GetDeembeddingTableNumberOfPorts_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSG_GetDeembeddingTableNumberOfPorts_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetDeembeddingTableNumberOfPorts_cfunc(vi, number_of_ports)

    def niRFSG_GetError(self, vi, error_code, error_description_buffer_size, error_description):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetError_cfunc is None:
                self.niRFSG_GetError_cfunc = self._get_library_function('niRFSG_GetError')
                self.niRFSG_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_GetError_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetError_cfunc(vi, error_code, error_description_buffer_size, error_description)

    def niRFSG_GetExternalCalibrationLastDateAndTime(self, vi, year, month, day, hour, minute, second):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetExternalCalibrationLastDateAndTime_cfunc is None:
                self.niRFSG_GetExternalCalibrationLastDateAndTime_cfunc = self._get_library_function('niRFSG_GetExternalCalibrationLastDateAndTime')
                self.niRFSG_GetExternalCalibrationLastDateAndTime_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSG_GetExternalCalibrationLastDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetExternalCalibrationLastDateAndTime_cfunc(vi, year, month, day, hour, minute, second)

    def niRFSG_GetMaxSettablePower(self, vi, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetMaxSettablePower_cfunc is None:
                self.niRFSG_GetMaxSettablePower_cfunc = self._get_library_function('niRFSG_GetMaxSettablePower')
                self.niRFSG_GetMaxSettablePower_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niRFSG_GetMaxSettablePower_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetMaxSettablePower_cfunc(vi, value)

    def niRFSG_GetScript(self, vi, script_name, script, buffer_size, actual_buffer_size):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetScript_cfunc is None:
                self.niRFSG_GetScript_cfunc = self._get_library_function('niRFSG_GetScript')
                self.niRFSG_GetScript_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSG_GetScript_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetScript_cfunc(vi, script_name, script, buffer_size, actual_buffer_size)

    def niRFSG_GetSelfCalibrationDateAndTime(self, vi, module, year, month, day, hour, minute, second):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetSelfCalibrationDateAndTime_cfunc is None:
                self.niRFSG_GetSelfCalibrationDateAndTime_cfunc = self._get_library_function('niRFSG_GetSelfCalibrationDateAndTime')
                self.niRFSG_GetSelfCalibrationDateAndTime_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSG_GetSelfCalibrationDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetSelfCalibrationDateAndTime_cfunc(vi, module, year, month, day, hour, minute, second)

    def niRFSG_GetSelfCalibrationTemperature(self, vi, module, temperature):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetSelfCalibrationTemperature_cfunc is None:
                self.niRFSG_GetSelfCalibrationTemperature_cfunc = self._get_library_function('niRFSG_GetSelfCalibrationTemperature')
                self.niRFSG_GetSelfCalibrationTemperature_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niRFSG_GetSelfCalibrationTemperature_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetSelfCalibrationTemperature_cfunc(vi, module, temperature)

    def niRFSG_GetTerminalName(self, vi, signal, signal_identifier, buffer_size, terminal_name):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetTerminalName_cfunc is None:
                self.niRFSG_GetTerminalName_cfunc = self._get_library_function('niRFSG_GetTerminalName')
                self.niRFSG_GetTerminalName_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_GetTerminalName_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetTerminalName_cfunc(vi, signal, signal_identifier, buffer_size, terminal_name)

    def niRFSG_GetWaveformBurstStartLocations(self, vi, channel_name, number_of_locations, locations, required_size):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetWaveformBurstStartLocations_cfunc is None:
                self.niRFSG_GetWaveformBurstStartLocations_cfunc = self._get_library_function('niRFSG_GetWaveformBurstStartLocations')
                self.niRFSG_GetWaveformBurstStartLocations_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSG_GetWaveformBurstStartLocations_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetWaveformBurstStartLocations_cfunc(vi, channel_name, number_of_locations, locations, required_size)

    def niRFSG_GetWaveformBurstStopLocations(self, vi, channel_name, number_of_locations, locations, required_size):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetWaveformBurstStopLocations_cfunc is None:
                self.niRFSG_GetWaveformBurstStopLocations_cfunc = self._get_library_function('niRFSG_GetWaveformBurstStopLocations')
                self.niRFSG_GetWaveformBurstStopLocations_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSG_GetWaveformBurstStopLocations_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetWaveformBurstStopLocations_cfunc(vi, channel_name, number_of_locations, locations, required_size)

    def niRFSG_GetWaveformMarkerEventLocations(self, vi, channel_name, number_of_locations, locations, required_size):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_GetWaveformMarkerEventLocations_cfunc is None:
                self.niRFSG_GetWaveformMarkerEventLocations_cfunc = self._get_library_function('niRFSG_GetWaveformMarkerEventLocations')
                self.niRFSG_GetWaveformMarkerEventLocations_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSG_GetWaveformMarkerEventLocations_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_GetWaveformMarkerEventLocations_cfunc(vi, channel_name, number_of_locations, locations, required_size)

    def niRFSG_InitWithOptions(self, resource_name, id_query, reset_device, option_string, new_vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_InitWithOptions_cfunc is None:
                self.niRFSG_InitWithOptions_cfunc = self._get_library_function('niRFSG_InitWithOptions')
                self.niRFSG_InitWithOptions_cfunc.argtypes = [ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niRFSG_InitWithOptions_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_InitWithOptions_cfunc(resource_name, id_query, reset_device, option_string, new_vi)

    def niRFSG_Initiate(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_Initiate_cfunc is None:
                self.niRFSG_Initiate_cfunc = self._get_library_function('niRFSG_Initiate')
                self.niRFSG_Initiate_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_Initiate_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_Initiate_cfunc(vi)

    def niRFSG_LoadConfigurationsFromFile(self, vi, channel_name, file_path):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_LoadConfigurationsFromFile_cfunc is None:
                self.niRFSG_LoadConfigurationsFromFile_cfunc = self._get_library_function('niRFSG_LoadConfigurationsFromFile')
                self.niRFSG_LoadConfigurationsFromFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_LoadConfigurationsFromFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_LoadConfigurationsFromFile_cfunc(vi, channel_name, file_path)

    def niRFSG_LockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_LockSession_cfunc is None:
                self.niRFSG_LockSession_cfunc = self._get_library_function('niRFSG_LockSession')
                self.niRFSG_LockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niRFSG_LockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_LockSession_cfunc(vi, caller_has_lock)

    def niRFSG_PerformPowerSearch(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_PerformPowerSearch_cfunc is None:
                self.niRFSG_PerformPowerSearch_cfunc = self._get_library_function('niRFSG_PerformPowerSearch')
                self.niRFSG_PerformPowerSearch_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_PerformPowerSearch_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_PerformPowerSearch_cfunc(vi)

    def niRFSG_PerformThermalCorrection(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_PerformThermalCorrection_cfunc is None:
                self.niRFSG_PerformThermalCorrection_cfunc = self._get_library_function('niRFSG_PerformThermalCorrection')
                self.niRFSG_PerformThermalCorrection_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_PerformThermalCorrection_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_PerformThermalCorrection_cfunc(vi)

    def niRFSG_QueryArbWaveformCapabilities(self, vi, max_number_waveforms, waveform_quantum, min_waveform_size, max_waveform_size):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_QueryArbWaveformCapabilities_cfunc is None:
                self.niRFSG_QueryArbWaveformCapabilities_cfunc = self._get_library_function('niRFSG_QueryArbWaveformCapabilities')
                self.niRFSG_QueryArbWaveformCapabilities_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niRFSG_QueryArbWaveformCapabilities_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_QueryArbWaveformCapabilities_cfunc(vi, max_number_waveforms, waveform_quantum, min_waveform_size, max_waveform_size)

    def niRFSG_ReadAndDownloadWaveformFromFileTDMS(self, vi, waveform_name, file_path, waveform_index):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ReadAndDownloadWaveformFromFileTDMS_cfunc is None:
                self.niRFSG_ReadAndDownloadWaveformFromFileTDMS_cfunc = self._get_library_function('niRFSG_ReadAndDownloadWaveformFromFileTDMS')
                self.niRFSG_ReadAndDownloadWaveformFromFileTDMS_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViUInt32]  # noqa: F405
                self.niRFSG_ReadAndDownloadWaveformFromFileTDMS_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ReadAndDownloadWaveformFromFileTDMS_cfunc(vi, waveform_name, file_path, waveform_index)

    def niRFSG_ResetDevice(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ResetDevice_cfunc is None:
                self.niRFSG_ResetDevice_cfunc = self._get_library_function('niRFSG_ResetDevice')
                self.niRFSG_ResetDevice_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_ResetDevice_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ResetDevice_cfunc(vi)

    def niRFSG_ResetWithDefaults(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ResetWithDefaults_cfunc is None:
                self.niRFSG_ResetWithDefaults_cfunc = self._get_library_function('niRFSG_ResetWithDefaults')
                self.niRFSG_ResetWithDefaults_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_ResetWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ResetWithDefaults_cfunc(vi)

    def niRFSG_ResetWithOptions(self, vi, steps_to_omit):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_ResetWithOptions_cfunc is None:
                self.niRFSG_ResetWithOptions_cfunc = self._get_library_function('niRFSG_ResetWithOptions')
                self.niRFSG_ResetWithOptions_cfunc.argtypes = [ViSession, ViUInt64]  # noqa: F405
                self.niRFSG_ResetWithOptions_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_ResetWithOptions_cfunc(vi, steps_to_omit)

    def niRFSG_SaveConfigurationsToFile(self, vi, channel_name, file_path):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SaveConfigurationsToFile_cfunc is None:
                self.niRFSG_SaveConfigurationsToFile_cfunc = self._get_library_function('niRFSG_SaveConfigurationsToFile')
                self.niRFSG_SaveConfigurationsToFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_SaveConfigurationsToFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SaveConfigurationsToFile_cfunc(vi, channel_name, file_path)

    def niRFSG_SelectArbWaveform(self, vi, waveform_name):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SelectArbWaveform_cfunc is None:
                self.niRFSG_SelectArbWaveform_cfunc = self._get_library_function('niRFSG_SelectArbWaveform')
                self.niRFSG_SelectArbWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_SelectArbWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SelectArbWaveform_cfunc(vi, waveform_name)

    def niRFSG_SelfCal(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SelfCal_cfunc is None:
                self.niRFSG_SelfCal_cfunc = self._get_library_function('niRFSG_SelfCal')
                self.niRFSG_SelfCal_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_SelfCal_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SelfCal_cfunc(vi)

    def niRFSG_SelfCalibrateRange(self, vi, steps_to_omit, min_frequency, max_frequency, min_power_level, max_power_level):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SelfCalibrateRange_cfunc is None:
                self.niRFSG_SelfCalibrateRange_cfunc = self._get_library_function('niRFSG_SelfCalibrateRange')
                self.niRFSG_SelfCalibrateRange_cfunc.argtypes = [ViSession, ViInt64, ViReal64, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niRFSG_SelfCalibrateRange_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SelfCalibrateRange_cfunc(vi, steps_to_omit, min_frequency, max_frequency, min_power_level, max_power_level)

    def niRFSG_SendSoftwareEdgeTrigger(self, vi, trigger, trigger_identifier):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SendSoftwareEdgeTrigger_cfunc is None:
                self.niRFSG_SendSoftwareEdgeTrigger_cfunc = self._get_library_function('niRFSG_SendSoftwareEdgeTrigger')
                self.niRFSG_SendSoftwareEdgeTrigger_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_SendSoftwareEdgeTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SendSoftwareEdgeTrigger_cfunc(vi, trigger, trigger_identifier)

    def niRFSG_SetArbWaveformNextWritePosition(self, vi, waveform_name, relative_to, offset):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SetArbWaveformNextWritePosition_cfunc is None:
                self.niRFSG_SetArbWaveformNextWritePosition_cfunc = self._get_library_function('niRFSG_SetArbWaveformNextWritePosition')
                self.niRFSG_SetArbWaveformNextWritePosition_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32]  # noqa: F405
                self.niRFSG_SetArbWaveformNextWritePosition_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SetArbWaveformNextWritePosition_cfunc(vi, waveform_name, relative_to, offset)

    def niRFSG_SetAttributeViBoolean(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SetAttributeViBoolean_cfunc is None:
                self.niRFSG_SetAttributeViBoolean_cfunc = self._get_library_function('niRFSG_SetAttributeViBoolean')
                self.niRFSG_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niRFSG_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SetAttributeViBoolean_cfunc(vi, channel_name, attribute, value)

    def niRFSG_SetAttributeViInt32(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SetAttributeViInt32_cfunc is None:
                self.niRFSG_SetAttributeViInt32_cfunc = self._get_library_function('niRFSG_SetAttributeViInt32')
                self.niRFSG_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niRFSG_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SetAttributeViInt32_cfunc(vi, channel_name, attribute, value)

    def niRFSG_SetAttributeViInt64(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SetAttributeViInt64_cfunc is None:
                self.niRFSG_SetAttributeViInt64_cfunc = self._get_library_function('niRFSG_SetAttributeViInt64')
                self.niRFSG_SetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt64]  # noqa: F405
                self.niRFSG_SetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SetAttributeViInt64_cfunc(vi, channel_name, attribute, value)

    def niRFSG_SetAttributeViReal64(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SetAttributeViReal64_cfunc is None:
                self.niRFSG_SetAttributeViReal64_cfunc = self._get_library_function('niRFSG_SetAttributeViReal64')
                self.niRFSG_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niRFSG_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SetAttributeViReal64_cfunc(vi, channel_name, attribute, value)

    def niRFSG_SetAttributeViSession(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SetAttributeViSession_cfunc is None:
                self.niRFSG_SetAttributeViSession_cfunc = self._get_library_function('niRFSG_SetAttributeViSession')
                self.niRFSG_SetAttributeViSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViSession]  # noqa: F405
                self.niRFSG_SetAttributeViSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SetAttributeViSession_cfunc(vi, channel_name, attribute, value)

    def niRFSG_SetAttributeViString(self, vi, channel_name, attribute, value):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SetAttributeViString_cfunc is None:
                self.niRFSG_SetAttributeViString_cfunc = self._get_library_function('niRFSG_SetAttributeViString')
                self.niRFSG_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SetAttributeViString_cfunc(vi, channel_name, attribute, value)

    def niRFSG_SetWaveformBurstStartLocations(self, vi, channel_name, number_of_locations, locations):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SetWaveformBurstStartLocations_cfunc is None:
                self.niRFSG_SetWaveformBurstStartLocations_cfunc = self._get_library_function('niRFSG_SetWaveformBurstStartLocations')
                self.niRFSG_SetWaveformBurstStartLocations_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niRFSG_SetWaveformBurstStartLocations_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SetWaveformBurstStartLocations_cfunc(vi, channel_name, number_of_locations, locations)

    def niRFSG_SetWaveformBurstStopLocations(self, vi, channel_name, number_of_locations, locations):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SetWaveformBurstStopLocations_cfunc is None:
                self.niRFSG_SetWaveformBurstStopLocations_cfunc = self._get_library_function('niRFSG_SetWaveformBurstStopLocations')
                self.niRFSG_SetWaveformBurstStopLocations_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niRFSG_SetWaveformBurstStopLocations_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SetWaveformBurstStopLocations_cfunc(vi, channel_name, number_of_locations, locations)

    def niRFSG_SetWaveformMarkerEventLocations(self, vi, channel_name, number_of_locations, locations):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_SetWaveformMarkerEventLocations_cfunc is None:
                self.niRFSG_SetWaveformMarkerEventLocations_cfunc = self._get_library_function('niRFSG_SetWaveformMarkerEventLocations')
                self.niRFSG_SetWaveformMarkerEventLocations_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niRFSG_SetWaveformMarkerEventLocations_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_SetWaveformMarkerEventLocations_cfunc(vi, channel_name, number_of_locations, locations)

    def niRFSG_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_UnlockSession_cfunc is None:
                self.niRFSG_UnlockSession_cfunc = self._get_library_function('niRFSG_UnlockSession')
                self.niRFSG_UnlockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niRFSG_UnlockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_UnlockSession_cfunc(vi, caller_has_lock)

    def niRFSG_WaitUntilSettled(self, vi, max_time_milliseconds):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_WaitUntilSettled_cfunc is None:
                self.niRFSG_WaitUntilSettled_cfunc = self._get_library_function('niRFSG_WaitUntilSettled')
                self.niRFSG_WaitUntilSettled_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niRFSG_WaitUntilSettled_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_WaitUntilSettled_cfunc(vi, max_time_milliseconds)

    def niRFSG_WriteArbWaveformComplexF32(self, vi, waveform_name, number_of_samples, waveform_data_array, more_data_pending):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_WriteArbWaveformComplexF32_cfunc is None:
                self.niRFSG_WriteArbWaveformComplexF32_cfunc = self._get_library_function('niRFSG_WriteArbWaveformComplexF32')
                self.niRFSG_WriteArbWaveformComplexF32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(NIComplexNumberF32), ViBoolean]  # noqa: F405
                self.niRFSG_WriteArbWaveformComplexF32_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_WriteArbWaveformComplexF32_cfunc(vi, waveform_name, number_of_samples, waveform_data_array, more_data_pending)

    def niRFSG_WriteArbWaveformComplexF64(self, vi, waveform_name, number_of_samples, waveform_data_array, more_data_pending):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_WriteArbWaveformComplexF64_cfunc is None:
                self.niRFSG_WriteArbWaveformComplexF64_cfunc = self._get_library_function('niRFSG_WriteArbWaveformComplexF64')
                self.niRFSG_WriteArbWaveformComplexF64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(NIComplexNumber), ViBoolean]  # noqa: F405
                self.niRFSG_WriteArbWaveformComplexF64_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_WriteArbWaveformComplexF64_cfunc(vi, waveform_name, number_of_samples, waveform_data_array, more_data_pending)

    def niRFSG_WriteArbWaveformComplexI16(self, vi, waveform_name, number_of_samples, waveform_data_array):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_WriteArbWaveformComplexI16_cfunc is None:
                self.niRFSG_WriteArbWaveformComplexI16_cfunc = self._get_library_function('niRFSG_WriteArbWaveformComplexI16')
                self.niRFSG_WriteArbWaveformComplexI16_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(NIComplexI16)]  # noqa: F405
                self.niRFSG_WriteArbWaveformComplexI16_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_WriteArbWaveformComplexI16_cfunc(vi, waveform_name, number_of_samples, waveform_data_array)

    def niRFSG_WriteScript(self, vi, script):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_WriteScript_cfunc is None:
                self.niRFSG_WriteScript_cfunc = self._get_library_function('niRFSG_WriteScript')
                self.niRFSG_WriteScript_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_WriteScript_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_WriteScript_cfunc(vi, script)

    def niRFSG_close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_close_cfunc is None:
                self.niRFSG_close_cfunc = self._get_library_function('niRFSG_close')
                self.niRFSG_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_close_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_close_cfunc(vi)

    def niRFSG_reset(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_reset_cfunc is None:
                self.niRFSG_reset_cfunc = self._get_library_function('niRFSG_reset')
                self.niRFSG_reset_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niRFSG_reset_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_reset_cfunc(vi)

    def niRFSG_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        with self._func_lock:
            if self.niRFSG_self_test_cfunc is None:
                self.niRFSG_self_test_cfunc = self._get_library_function('niRFSG_self_test')
                self.niRFSG_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niRFSG_self_test_cfunc.restype = ViStatus  # noqa: F405
        return self.niRFSG_self_test_cfunc(vi, self_test_result, self_test_message)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nirfsg/nirfsg/_library_interpreter.py sha256=ac4c19257100503b44a8818ede2a7b98844071f66bfd1f49686adcbe1131e4aa bytes=57564 -->
## FILE: generated/nirfsg/nirfsg/_library_interpreter.py

- repository: `ni/nimi-python`
- source_path: `generated/nirfsg/nirfsg/_library_interpreter.py`
- sha256: `ac4c19257100503b44a8818ede2a7b98844071f66bfd1f49686adcbe1131e4aa`
- bytes: 57564

````python
# -*- coding: utf-8 -*-
# This file was generated

import array
import ctypes
import hightime  # noqa: F401
import nirfsg._complextype as _complextype
import nirfsg._library_singleton as _library_singleton
import nirfsg._visatype as _visatype
import nirfsg.enums as enums  # noqa: F401
import nirfsg.errors as errors


# Helper functions for creating ctypes needed for calling into the driver DLL
def _get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None):
    if isinstance(value, array.array):
        assert library_type is not None, 'library_type is required for array.array'
        addr, _ = value.buffer_info()
        return ctypes.cast(addr, ctypes.POINTER(library_type))
    elif str(type(value)).find("'numpy.ndarray'") != -1:
        import numpy
        if library_type in (_complextype.NIComplexI16, _complextype.NIComplexNumberF32, _complextype.NIComplexNumber):
            complex_dtype = numpy.dtype(library_type)
            if value.ndim > 1:
                # we create a flattened view of the multi-dimensional numpy array
                restructured_array_view = value.ravel().view(complex_dtype)
            else:
                restructured_array_view = value.view(complex_dtype)
            return restructured_array_view.ctypes.data_as(ctypes.POINTER(library_type))
        else:
            return numpy.ctypeslib.as_ctypes(value)
    elif isinstance(value, bytes):
        return ctypes.cast(value, ctypes.POINTER(library_type))
    elif isinstance(value, list):
        assert library_type is not None, 'library_type is required for list'
        return (library_type * len(value))(*value)
    else:
        if library_type is not None and size is not None:
            return (library_type * size)()
        else:
            return None


def _convert_to_array(value, array_type):
    if value is not None:
        if isinstance(value, array.array):
            value_array = value
        else:
            value_array = array.array(array_type, value)
    else:
        value_array = None

    return value_array


class LibraryInterpreter(object):
    '''Library C<->Python interpreter.

    This class is responsible for interpreting the Library's C API. It is responsible for:
    * Converting ctypes to native Python types.
    * Dealing with string encoding.
    * Allocating memory.
    * Converting errors returned by Library into Python exceptions.
    '''

    def __init__(self, encoding):
        self._encoding = encoding
        self._library = _library_singleton.get()
        # Initialize _vi to 0 for now.
        # Session will directly update it once the driver runtime init function has been called and
        # we have a valid session handle.
        self.set_session_handle()

    def set_session_handle(self, value=0):
        self._vi = value

    def get_session_handle(self):
        return self._vi

    def get_error_description(self, error_code):
        '''get_error_description

        Returns the error description.
        '''
        try:
            returned_error_code, error_string = self.get_error()
            if returned_error_code == error_code:
                return error_string
        except errors.Error:
            pass
        return "Failed to retrieve error description."

    def abort(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_Abort(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def allocate_arb_waveform(self, waveform_name, size_in_samples):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        size_in_samples_ctype = _visatype.ViInt32(size_in_samples)  # case S150
        error_code = self._library.niRFSG_AllocateArbWaveform(vi_ctype, waveform_name_ctype, size_in_samples_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def change_external_calibration_password(self, old_password, new_password):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        old_password_ctype = ctypes.create_string_buffer(old_password.encode(self._encoding))  # case C020
        new_password_ctype = ctypes.create_string_buffer(new_password.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_ChangeExternalCalibrationPassword(vi_ctype, old_password_ctype, new_password_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def check_generation_status(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        is_done_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niRFSG_CheckGenerationStatus(vi_ctype, None if is_done_ctype is None else (ctypes.pointer(is_done_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(is_done_ctype.value)

    def check_if_script_exists(self, script_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        script_name_ctype = ctypes.create_string_buffer(script_name.encode(self._encoding))  # case C020
        script_exists_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niRFSG_CheckIfScriptExists(vi_ctype, script_name_ctype, None if script_exists_ctype is None else (ctypes.pointer(script_exists_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(script_exists_ctype.value)

    def check_if_waveform_exists(self, waveform_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        waveform_exists_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niRFSG_CheckIfWaveformExists(vi_ctype, waveform_name_ctype, None if waveform_exists_ctype is None else (ctypes.pointer(waveform_exists_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(waveform_exists_ctype.value)

    def clear_all_arb_waveforms(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_ClearAllArbWaveforms(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_arb_waveform(self, waveform_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_ClearArbWaveform(vi_ctype, waveform_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_self_calibrate_range(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_ClearSelfCalibrateRange(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def commit(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_Commit(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_deembedding_table_interpolation_linear(self, port, table_name, format):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        port_ctype = ctypes.create_string_buffer(port.encode(self._encoding))  # case C020
        table_name_ctype = ctypes.create_string_buffer(table_name.encode(self._encoding))  # case C020
        format_ctype = _visatype.ViInt32(format.value)  # case S130
        error_code = self._library.niRFSG_ConfigureDeembeddingTableInterpolationLinear(vi_ctype, port_ctype, table_name_ctype, format_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_deembedding_table_interpolation_nearest(self, port, table_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        port_ctype = ctypes.create_string_buffer(port.encode(self._encoding))  # case C020
        table_name_ctype = ctypes.create_string_buffer(table_name.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_ConfigureDeembeddingTableInterpolationNearest(vi_ctype, port_ctype, table_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_deembedding_table_interpolation_spline(self, port, table_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        port_ctype = ctypes.create_string_buffer(port.encode(self._encoding))  # case C020
        table_name_ctype = ctypes.create_string_buffer(table_name.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_ConfigureDeembeddingTableInterpolationSpline(vi_ctype, port_ctype, table_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_edge_script_trigger(self, trigger_id, source, edge):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_id_ctype = ctypes.create_string_buffer(trigger_id.encode(self._encoding))  # case C010
        source_ctype = ctypes.create_string_buffer(source.encode(self._encoding))  # case C020
        edge_ctype = _visatype.ViInt32(edge.value)  # case S130
        error_code = self._library.niRFSG_ConfigureDigitalEdgeScriptTrigger(vi_ctype, trigger_id_ctype, source_ctype, edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_edge_start_trigger(self, source, edge):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        source_ctype = ctypes.create_string_buffer(source.encode(self._encoding))  # case C020
        edge_ctype = _visatype.ViInt32(edge.value)  # case S130
        error_code = self._library.niRFSG_ConfigureDigitalEdgeStartTrigger(vi_ctype, source_ctype, edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_level_script_trigger(self, trigger_id, source, level):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_id_ctype = ctypes.create_string_buffer(trigger_id.encode(self._encoding))  # case C010
        source_ctype = ctypes.create_string_buffer(source.encode(self._encoding))  # case C020
        level_ctype = _visatype.ViInt32(level)  # case S150
        error_code = self._library.niRFSG_ConfigureDigitalLevelScriptTrigger(vi_ctype, trigger_id_ctype, source_ctype, level_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_rf(self, frequency, power_level):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        frequency_ctype = _visatype.ViReal64(frequency)  # case S150
        power_level_ctype = _visatype.ViReal64(power_level)  # case S150
        error_code = self._library.niRFSG_ConfigureRF(vi_ctype, frequency_ctype, power_level_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_ref_clock(self, ref_clock_source, ref_clock_rate):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        ref_clock_source_ctype = ctypes.create_string_buffer(ref_clock_source.encode(self._encoding))  # case C020
        ref_clock_rate_ctype = _visatype.ViReal64(ref_clock_rate)  # case S150
        error_code = self._library.niRFSG_ConfigureRefClock(vi_ctype, ref_clock_source_ctype, ref_clock_rate_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_software_script_trigger(self, trigger_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_id_ctype = ctypes.create_string_buffer(trigger_id.encode(self._encoding))  # case C010
        error_code = self._library.niRFSG_ConfigureSoftwareScriptTrigger(vi_ctype, trigger_id_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_software_start_trigger(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_ConfigureSoftwareStartTrigger(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_deembedding_sparameter_table_array(self, port, table_name, frequencies, sparameter_table, number_of_ports, sparameter_orientation):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        port_ctype = ctypes.create_string_buffer(port.encode(self._encoding))  # case C020
        table_name_ctype = ctypes.create_string_buffer(table_name.encode(self._encoding))  # case C020
        frequencies_ctype = _get_ctypes_pointer_for_buffer(value=frequencies)  # case B510
        frequencies_size_ctype = _visatype.ViInt32(0 if frequencies is None else len(frequencies))  # case S160
        sparameter_table_ctype = _get_ctypes_pointer_for_buffer(value=sparameter_table, library_type=_complextype.NIComplexNumber)  # case B510
        sparameter_table_size_ctype = _visatype.ViInt32(0 if sparameter_table is None else sparameter_table.size)  # case S161
        number_of_ports_ctype = _visatype.ViInt32(number_of_ports)  # case S150
        sparameter_orientation_ctype = _visatype.ViInt32(sparameter_orientation.value)  # case S130
        error_code = self._library.niRFSG_CreateDeembeddingSparameterTableArray(vi_ctype, port_ctype, table_name_ctype, frequencies_ctype, frequencies_size_ctype, sparameter_table_ctype, sparameter_table_size_ctype, number_of_ports_ctype, sparameter_orientation_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_deembedding_sparameter_table_s2p_file(self, port, table_name, s2p_file_path, sparameter_orientation):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        port_ctype = ctypes.create_string_buffer(port.encode(self._encoding))  # case C020
        table_name_ctype = ctypes.create_string_buffer(table_name.encode(self._encoding))  # case C020
        s2p_file_path_ctype = ctypes.create_string_buffer(s2p_file_path.encode(self._encoding))  # case C020
        sparameter_orientation_ctype = _visatype.ViInt32(sparameter_orientation.value)  # case S130
        error_code = self._library.niRFSG_CreateDeembeddingSparameterTableS2PFile(vi_ctype, port_ctype, table_name_ctype, s2p_file_path_ctype, sparameter_orientation_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def delete_all_deembedding_tables(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_DeleteAllDeembeddingTables(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def delete_deembedding_table(self, port, table_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        port_ctype = ctypes.create_string_buffer(port.encode(self._encoding))  # case C020
        table_name_ctype = ctypes.create_string_buffer(table_name.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_DeleteDeembeddingTable(vi_ctype, port_ctype, table_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def delete_script(self, script_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        script_name_ctype = ctypes.create_string_buffer(script_name.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_DeleteScript(vi_ctype, script_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable_script_trigger(self, trigger_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_id_ctype = ctypes.create_string_buffer(trigger_id.encode(self._encoding))  # case C010
        error_code = self._library.niRFSG_DisableScriptTrigger(vi_ctype, trigger_id_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable_start_trigger(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_DisableStartTrigger(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def error_message(self, error_code):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niRFSG_ErrorMessage(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)

    def get_all_named_waveform_names(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_names_ctype = None  # case C090
        buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        actual_buffer_size_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSG_GetAllNamedWaveformNames(vi_ctype, waveform_names_ctype, buffer_size_ctype, None if actual_buffer_size_ctype is None else (ctypes.pointer(actual_buffer_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(actual_buffer_size_ctype.value)  # case S200
        waveform_names_ctype = (_visatype.ViChar * actual_buffer_size_ctype.value)()  # case C100
        error_code = self._library.niRFSG_GetAllNamedWaveformNames(vi_ctype, waveform_names_ctype, buffer_size_ctype, None if actual_buffer_size_ctype is None else (ctypes.pointer(actual_buffer_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return waveform_names_ctype.value.decode(self._encoding)

    def get_all_script_names(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        script_names_ctype = None  # case C090
        buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        actual_buffer_size_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSG_GetAllScriptNames(vi_ctype, script_names_ctype, buffer_size_ctype, None if actual_buffer_size_ctype is None else (ctypes.pointer(actual_buffer_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(actual_buffer_size_ctype.value)  # case S200
        script_names_ctype = (_visatype.ViChar * actual_buffer_size_ctype.value)()  # case C100
        error_code = self._library.niRFSG_GetAllScriptNames(vi_ctype, script_names_ctype, buffer_size_ctype, None if actual_buffer_size_ctype is None else (ctypes.pointer(actual_buffer_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return script_names_ctype.value.decode(self._encoding)

    def get_attribute_vi_boolean(self, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niRFSG_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(value_ctype.value)

    def get_attribute_vi_int32(self, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSG_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def get_attribute_vi_int64(self, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niRFSG_GetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def get_attribute_vi_real64(self, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niRFSG_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(value_ctype.value)

    def get_attribute_vi_session(self, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niRFSG_GetAttributeViSession(vi_ctype, channel_name_ctype, attribute_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def get_attribute_vi_string(self, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        buf_size_ctype = _visatype.ViInt32()  # case S170
        value_ctype = None  # case C050
        error_code = self._library.niRFSG_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_ctype, buf_size_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buf_size_ctype = _visatype.ViInt32(error_code)  # case S180
        value_ctype = (_visatype.ViChar * buf_size_ctype.value)()  # case C060
        error_code = self._library.niRFSG_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_ctype, buf_size_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return value_ctype.value.decode(self._encoding)

    def get_deembedding_sparameters(self):
        import numpy as np
        number_of_ports = self.get_deembedding_table_number_of_ports()
        sparameters_array_size = number_of_ports ** 2
        sparameters = np.full((number_of_ports, number_of_ports), 0 + 0j, dtype=np.complex128)
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        sparameters_ctype = _get_ctypes_pointer_for_buffer(value=sparameters, library_type=_complextype.NIComplexNumber)  # case B510
        sparameters_array_size_ctype = _visatype.ViInt32(sparameters_array_size)  # case S150
        number_of_sparameters_ctype = _visatype.ViInt32()  # case S220
        number_of_ports_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSG_GetDeembeddingSparameters(vi_ctype, sparameters_ctype, sparameters_array_size_ctype, None if number_of_sparameters_ctype is None else (ctypes.pointer(number_of_sparameters_ctype)), None if number_of_ports_ctype is None else (ctypes.pointer(number_of_ports_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        sparameters = sparameters.reshape((int(number_of_ports_ctype.value), int(number_of_ports_ctype.value)))
        return sparameters

    def get_deembedding_table_number_of_ports(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        number_of_ports_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSG_GetDeembeddingTableNumberOfPorts(vi_ctype, None if number_of_ports_ctype is None else (ctypes.pointer(number_of_ports_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(number_of_ports_ctype.value)

    def get_error(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus()  # case S220
        error_description_buffer_size_ctype = _visatype.ViInt32()  # case S170
        error_description_ctype = None  # case C050
        error_code = self._library.niRFSG_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        error_description_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        error_description_ctype = (_visatype.ViChar * error_description_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niRFSG_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), error_description_ctype.value.decode(self._encoding)

    def get_external_calibration_last_date_and_time(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        second_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSG_GetExternalCalibrationLastDateAndTime(vi_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)), None if second_ctype is None else (ctypes.pointer(second_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value), int(second_ctype.value)

    def get_max_settable_power(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niRFSG_GetMaxSettablePower(vi_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(value_ctype.value)

    def get_script(self, script_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        script_name_ctype = ctypes.create_string_buffer(script_name.encode(self._encoding))  # case C020
        script_ctype = None  # case C090
        buffer_size_ctype = _visatype.ViInt32(0)  # case S190
        actual_buffer_size_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSG_GetScript(vi_ctype, script_name_ctype, script_ctype, buffer_size_ctype, None if actual_buffer_size_ctype is None else (ctypes.pointer(actual_buffer_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(actual_buffer_size_ctype.value)  # case S200
        script_ctype = (_visatype.ViChar * actual_buffer_size_ctype.value)()  # case C100
        error_code = self._library.niRFSG_GetScript(vi_ctype, script_name_ctype, script_ctype, buffer_size_ctype, None if actual_buffer_size_ctype is None else (ctypes.pointer(actual_buffer_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return script_ctype.value.decode(self._encoding)

    def get_self_calibration_date_and_time(self, module):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        module_ctype = _visatype.ViInt32(module.value)  # case S130
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        second_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSG_GetSelfCalibrationDateAndTime(vi_ctype, module_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)), None if second_ctype is None else (ctypes.pointer(second_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value), int(second_ctype.value)

    def get_self_calibration_temperature(self, module):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        module_ctype = _visatype.ViInt32(module.value)  # case S130
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niRFSG_GetSelfCalibrationTemperature(vi_ctype, module_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def get_terminal_name(self, signal, signal_identifier):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        signal_ctype = _visatype.ViInt32(signal.value)  # case S130
        signal_identifier_ctype = ctypes.create_string_buffer(signal_identifier.encode(self._encoding))  # case C020
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        terminal_name_ctype = None  # case C050
        error_code = self._library.niRFSG_GetTerminalName(vi_ctype, signal_ctype, signal_identifier_ctype, buffer_size_ctype, terminal_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        terminal_name_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niRFSG_GetTerminalName(vi_ctype, signal_ctype, signal_identifier_ctype, buffer_size_ctype, terminal_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return terminal_name_ctype.value.decode(self._encoding)

    def get_waveform_burst_start_locations(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        number_of_locations_ctype = _visatype.ViInt32(0)  # case S190
        locations_ctype = None  # case B610
        required_size_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSG_GetWaveformBurstStartLocations(vi_ctype, channel_name_ctype, number_of_locations_ctype, locations_ctype, None if required_size_ctype is None else (ctypes.pointer(required_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        number_of_locations_ctype = _visatype.ViInt32(required_size_ctype.value)  # case S200
        locations_size = required_size_ctype.value  # case B620
        locations_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=locations_size)  # case B620
        error_code = self._library.niRFSG_GetWaveformBurstStartLocations(vi_ctype, channel_name_ctype, number_of_locations_ctype, locations_ctype, None if required_size_ctype is None else (ctypes.pointer(required_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(locations_ctype[i]) for i in range(number_of_locations_ctype.value)]

    def get_waveform_burst_stop_locations(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        number_of_locations_ctype = _visatype.ViInt32(0)  # case S190
        locations_ctype = None  # case B610
        required_size_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSG_GetWaveformBurstStopLocations(vi_ctype, channel_name_ctype, number_of_locations_ctype, locations_ctype, None if required_size_ctype is None else (ctypes.pointer(required_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        number_of_locations_ctype = _visatype.ViInt32(required_size_ctype.value)  # case S200
        locations_size = required_size_ctype.value  # case B620
        locations_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=locations_size)  # case B620
        error_code = self._library.niRFSG_GetWaveformBurstStopLocations(vi_ctype, channel_name_ctype, number_of_locations_ctype, locations_ctype, None if required_size_ctype is None else (ctypes.pointer(required_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(locations_ctype[i]) for i in range(number_of_locations_ctype.value)]

    def get_waveform_marker_event_locations(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        number_of_locations_ctype = _visatype.ViInt32(0)  # case S190
        locations_ctype = None  # case B610
        required_size_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSG_GetWaveformMarkerEventLocations(vi_ctype, channel_name_ctype, number_of_locations_ctype, locations_ctype, None if required_size_ctype is None else (ctypes.pointer(required_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        number_of_locations_ctype = _visatype.ViInt32(required_size_ctype.value)  # case S200
        locations_size = required_size_ctype.value  # case B620
        locations_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=locations_size)  # case B620
        error_code = self._library.niRFSG_GetWaveformMarkerEventLocations(vi_ctype, channel_name_ctype, number_of_locations_ctype, locations_ctype, None if required_size_ctype is None else (ctypes.pointer(required_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(locations_ctype[i]) for i in range(number_of_locations_ctype.value)]

    def init_with_options(self, resource_name, id_query, reset_device, option_string):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        id_query_ctype = _visatype.ViBoolean(id_query)  # case S150
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case C020
        new_vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niRFSG_InitWithOptions(resource_name_ctype, id_query_ctype, reset_device_ctype, option_string_ctype, None if new_vi_ctype is None else (ctypes.pointer(new_vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        self._close_on_exit = True
        return int(new_vi_ctype.value)

    def initiate(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_Initiate(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def load_configurations_from_file(self, channel_name, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_LoadConfigurationsFromFile(vi_ctype, channel_name_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def lock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_LockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def perform_power_search(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_PerformPowerSearch(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def perform_thermal_correction(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_PerformThermalCorrection(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def query_arb_waveform_capabilities(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        max_number_waveforms_ctype = _visatype.ViInt32()  # case S220
        waveform_quantum_ctype = _visatype.ViInt32()  # case S220
        min_waveform_size_ctype = _visatype.ViInt32()  # case S220
        max_waveform_size_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niRFSG_QueryArbWaveformCapabilities(vi_ctype, None if max_number_waveforms_ctype is None else (ctypes.pointer(max_number_waveforms_ctype)), None if waveform_quantum_ctype is None else (ctypes.pointer(waveform_quantum_ctype)), None if min_waveform_size_ctype is None else (ctypes.pointer(min_waveform_size_ctype)), None if max_waveform_size_ctype is None else (ctypes.pointer(max_waveform_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(max_number_waveforms_ctype.value), int(waveform_quantum_ctype.value), int(min_waveform_size_ctype.value), int(max_waveform_size_ctype.value)

    def read_and_download_waveform_from_file_tdms(self, waveform_name, file_path, waveform_index):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        waveform_index_ctype = _visatype.ViUInt32(waveform_index)  # case S150
        error_code = self._library.niRFSG_ReadAndDownloadWaveformFromFileTDMS(vi_ctype, waveform_name_ctype, file_path_ctype, waveform_index_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_device(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_ResetDevice(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_with_defaults(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_ResetWithDefaults(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_with_options(self, steps_to_omit):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        steps_to_omit_ctype = _visatype.ViUInt64(steps_to_omit.value)  # case S130
        error_code = self._library.niRFSG_ResetWithOptions(vi_ctype, steps_to_omit_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def save_configurations_to_file(self, channel_name, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_SaveConfigurationsToFile(vi_ctype, channel_name_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def select_arb_waveform(self, waveform_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_SelectArbWaveform(vi_ctype, waveform_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_cal(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_SelfCal(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_calibrate_range(self, steps_to_omit, min_frequency, max_frequency, min_power_level, max_power_level):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        steps_to_omit_ctype = _visatype.ViInt64(steps_to_omit.value)  # case S130
        min_frequency_ctype = _visatype.ViReal64(min_frequency)  # case S150
        max_frequency_ctype = _visatype.ViReal64(max_frequency)  # case S150
        min_power_level_ctype = _visatype.ViReal64(min_power_level)  # case S150
        max_power_level_ctype = _visatype.ViReal64(max_power_level)  # case S150
        error_code = self._library.niRFSG_SelfCalibrateRange(vi_ctype, steps_to_omit_ctype, min_frequency_ctype, max_frequency_ctype, min_power_level_ctype, max_power_level_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_edge_trigger(self, trigger, trigger_identifier):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_ctype = _visatype.ViInt32(trigger.value)  # case S130
        trigger_identifier_ctype = ctypes.create_string_buffer(trigger_identifier.value.encode(self._encoding))  # case C030
        error_code = self._library.niRFSG_SendSoftwareEdgeTrigger(vi_ctype, trigger_ctype, trigger_identifier_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_arb_waveform_next_write_position(self, waveform_name, relative_to, offset):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        relative_to_ctype = _visatype.ViInt32(relative_to.value)  # case S130
        offset_ctype = _visatype.ViInt32(offset)  # case S150
        error_code = self._library.niRFSG_SetArbWaveformNextWritePosition(vi_ctype, waveform_name_ctype, relative_to_ctype, offset_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_boolean(self, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViBoolean(value)  # case S150
        error_code = self._library.niRFSG_SetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int32(self, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt32(value)  # case S150
        error_code = self._library.niRFSG_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int64(self, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViInt64(value)  # case S150
        error_code = self._library.niRFSG_SetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_real64(self, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViReal64(value)  # case S150
        error_code = self._library.niRFSG_SetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_session(self, channel_name, attribute):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_SetAttributeViSession(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_string(self, channel_name, attribute, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_ctype = _visatype.ViAttr(attribute)  # case S150
        value_ctype = ctypes.create_string_buffer(value.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_SetAttributeViString(vi_ctype, channel_name_ctype, attribute_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_waveform_burst_start_locations(self, channel_name, locations):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        number_of_locations_ctype = _visatype.ViInt32(0 if locations is None else len(locations))  # case S160
        locations_ctype = _get_ctypes_pointer_for_buffer(value=locations, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niRFSG_SetWaveformBurstStartLocations(vi_ctype, channel_name_ctype, number_of_locations_ctype, locations_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_waveform_burst_stop_locations(self, channel_name, locations):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        number_of_locations_ctype = _visatype.ViInt32(0 if locations is None else len(locations))  # case S160
        locations_ctype = _get_ctypes_pointer_for_buffer(value=locations, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niRFSG_SetWaveformBurstStopLocations(vi_ctype, channel_name_ctype, number_of_locations_ctype, locations_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_waveform_marker_event_locations(self, channel_name, locations):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        number_of_locations_ctype = _visatype.ViInt32(0 if locations is None else len(locations))  # case S160
        locations_ctype = _get_ctypes_pointer_for_buffer(value=locations, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niRFSG_SetWaveformMarkerEventLocations(vi_ctype, channel_name_ctype, number_of_locations_ctype, locations_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_UnlockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def wait_until_settled(self, max_time_milliseconds):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        max_time_milliseconds_ctype = _visatype.ViInt32(max_time_milliseconds)  # case S150
        error_code = self._library.niRFSG_WaitUntilSettled(vi_ctype, max_time_milliseconds_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_arb_waveform_complex_f32(self, waveform_name, waveform_data_array, more_data_pending):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        number_of_samples_ctype = _visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_ctype = _get_ctypes_pointer_for_buffer(value=waveform_data_array, library_type=_complextype.NIComplexNumberF32)  # case B510
        more_data_pending_ctype = _visatype.ViBoolean(more_data_pending)  # case S150
        error_code = self._library.niRFSG_WriteArbWaveformComplexF32(vi_ctype, waveform_name_ctype, number_of_samples_ctype, waveform_data_array_ctype, more_data_pending_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_arb_waveform_complex_f64(self, waveform_name, waveform_data_array, more_data_pending):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        number_of_samples_ctype = _visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_ctype = _get_ctypes_pointer_for_buffer(value=waveform_data_array, library_type=_complextype.NIComplexNumber)  # case B510
        more_data_pending_ctype = _visatype.ViBoolean(more_data_pending)  # case S150
        error_code = self._library.niRFSG_WriteArbWaveformComplexF64(vi_ctype, waveform_name_ctype, number_of_samples_ctype, waveform_data_array_ctype, more_data_pending_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_arb_waveform_complex_i16(self, waveform_name, waveform_data_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        number_of_samples_ctype = _visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array) // 2)  # case S160
        waveform_data_array_ctype = _get_ctypes_pointer_for_buffer(value=waveform_data_array, library_type=_complextype.NIComplexI16)  # case B510
        error_code = self._library.niRFSG_WriteArbWaveformComplexI16(vi_ctype, waveform_name_ctype, number_of_samples_ctype, waveform_data_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_script(self, script):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        script_ctype = ctypes.create_string_buffer(script.encode(self._encoding))  # case C020
        error_code = self._library.niRFSG_WriteScript(vi_ctype, script_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def close(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niRFSG_reset(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_test(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niRFSG_self_test(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nirfsg/nirfsg/_library_singleton.py sha256=5f9122be3a5a130ae344eda5b98bb6dc5b0b116ce305396873db0de7a5b83bc0 bytes=1690 -->
## FILE: generated/nirfsg/nirfsg/_library_singleton.py

- repository: `ni/nimi-python`
- source_path: `generated/nirfsg/nirfsg/_library_singleton.py`
- sha256: `5f9122be3a5a130ae344eda5b98bb6dc5b0b116ce305396873db0de7a5b83bc0`
- bytes: 1690

````python
# -*- coding: utf-8 -*-
# This file was generated

import platform

import ctypes
import ctypes.util
import nirfsg._library as _library
import nirfsg.errors as errors
import threading


_instance = None
_instance_lock = threading.Lock()
_library_info = {'Linux': {'64bit': {'name': 'nirfsg', 'type': 'cdll'}},
                 'Windows': {'32bit': {'name': 'niRFSG.dll', 'type': 'windll'},
                             '64bit': {'name': 'niRFSG_64.dll', 'type': 'cdll'}}}


def _get_library_name():
    try:
        lib_name = ctypes.util.find_library(_library_info[platform.system()][platform.architecture()[0]]['name'])  # We find and return full path to the DLL
        if lib_name is None:
            raise errors.DriverNotInstalledError()
        return lib_name
    except KeyError:
        raise errors.UnsupportedConfigurationError


def _get_library_type():
    try:
        return _library_info[platform.system()][platform.architecture()[0]]['type']
    except KeyError:
        raise errors.UnsupportedConfigurationError


def get():
    '''get

    Returns the library.Library singleton for nirfsg.
    '''
    global _instance

    with _instance_lock:
        if _instance is None:
            try:
                library_type = _get_library_type()
                if library_type == 'windll':
                    ctypes_library = ctypes.WinDLL(_get_library_name())
                else:
                    assert library_type == 'cdll'
                    ctypes_library = ctypes.CDLL(_get_library_name())
            except OSError:
                raise errors.DriverNotInstalledError()
            _instance = _library.Library(ctypes_library)
        return _instance
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nirfsg/nirfsg/_visatype.py sha256=ac436ae1613f5e807cd16d2df951c7a502f37996234e4d324c5412b3633e1c92 bytes=662 -->
## FILE: generated/nirfsg/nirfsg/_visatype.py

- repository: `ni/nimi-python`
- source_path: `generated/nirfsg/nirfsg/_visatype.py`
- sha256: `ac436ae1613f5e807cd16d2df951c7a502f37996234e4d324c5412b3633e1c92`
- bytes: 662

````python
import ctypes


'''Definitions of the VISA types used by the C API of the driver runtime.
These are aliased directly to ctypes types so can be used directly to call into the library.
'''


ViChar = ctypes.c_char
ViInt8 = ctypes.c_int8
ViUInt8 = ctypes.c_uint8
ViInt16 = ctypes.c_int16
ViUInt16 = ctypes.c_uint16
ViInt32 = ctypes.c_int32
ViUInt32 = ctypes.c_uint32
ViInt64 = ctypes.c_int64
ViUInt64 = ctypes.c_uint64
ViString = ctypes.c_char_p
ViReal32 = ctypes.c_float
ViReal64 = ctypes.c_double

# Types that are based on other visatypes
ViBoolean = ViUInt16
ViStatus = ViInt32
ViSession = ViUInt32
ViAttr = ViUInt32
ViConstString = ViString
ViRsrc = ViString
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nirfsg/nirfsg/enums.py sha256=37ca393027df56a70b66a673f6b6052338e23ddfc31d1b8e4259ebbf7557ce21 bytes=23034 -->
## FILE: generated/nirfsg/nirfsg/enums.py

- repository: `ni/nimi-python`
- source_path: `generated/nirfsg/nirfsg/enums.py`
- sha256: `37ca393027df56a70b66a673f6b6052338e23ddfc31d1b8e4259ebbf7557ce21`
- bytes: 23034

````python
# -*- coding: utf-8 -*-
# This file was generated

from enum import Enum
from enum import IntFlag


class AllowOutOfSpecificationUserSettings(Enum):
    DISABLE = 0
    r'''
    Disables out-of-specification user settings.
    '''
    ENABLE = 1
    r'''
    Enables out-of-specification user settings.
    '''


class AmpPath(Enum):
    HIGH_POWER = 16000
    r'''
    Sets the amplification path to use the high power path.
    '''
    LOW_HARMONIC = 16001
    r'''
    Sets the amplification path to use the low harmonic path.
    '''


class AnalogModulationFmBand(Enum):
    NARROWBAND = 17000
    r'''
    Specifies narrowband frequency modulation.
    '''
    WIDEBAND = 17001
    r'''
    Specifies wideband frequency modulation.
    '''


class AnalogModulationFmNarrowbandIntegrator(Enum):
    RANGE_100_HERTZ_TO_1_KILOHERTZ = 18000
    r'''
    Specifies a range from 100Hz to 1kHz.
    '''
    RANGE_1_KILOHERTZ_TO_10_KILOHERTZ = 18001
    r'''
    Specifies a range from 1kHz to 10kHz.
    '''
    RANGE_10_KILOHERTZ_TO_100_KILOHERTZ = 18002
    r'''
    Specifies a range from 10kHz to 100kHz.
    '''


class AnalogModulationPmMode(Enum):
    HIGH_DEVIATION = 19000
    r'''
    Specifies high deviation. High deviation comes at the expense of a higher phase noise.
    '''
    LOW_PHASE_NOISE = 19001
    r'''
    Specifies low phase noise. Low phase noise comes at the expense of a lower maximum deviation.
    '''


class AnalogModulationType(Enum):
    NONE = 0
    r'''
    Disables analog modulation.
    '''
    FM = 2000
    r'''
    Specifies that the analog modulation type is FM.
    '''
    PM = 2001
    r'''
    Specifies that the analog modulation type is PM.
    '''
    AM = 2002
    r'''
    Specifies that the analog modulation type is AM.
    '''


class ArbOnboardSampleClockMode(Enum):
    HIGH_RESOLUTION = 6000
    r'''
    Sample rates are generated by a high-resolution clock.
    '''
    DIVIDE_DOWN = 6001
    r'''
    Sample rates are generated by dividing the source frequency.
    '''


class ArbSampleClockSource(Enum):
    ONBOARD_CLOCK = 'OnboardClock'
    r'''
    Uses the AWG module onboard clock as the Sample Clock source.
    '''
    CLK_IN = 'ClkIn'
    r'''
    Uses the external clock as the Sample Clock source.
    '''


class AutomaticLevelControl(Enum):
    DISABLE = 0
    r'''
    Disables ALC.
    '''
    ENABLE = 1
    r'''
    Enables the ALC.
    '''


class AutomaticPowerSearch(Enum):
    DISABLE = 0
    r'''
    Disables automatic power search.
    '''
    ENABLE = 1
    r'''
    Enables automatic power search.
    '''


class AutomaticThermalCorrection(Enum):
    DISABLE = 0
    r'''
    Automatic thermal correction is disabled.
    '''
    ENABLE = 1
    r'''
    Automatic thermal correction is enabled.
    '''


class DeembeddingType(Enum):
    NONE = 25000
    r'''
    De-embedding is not applied to the measurement.
    '''
    SCALAR = 25001
    r'''
    De-embeds the measurement using only the gain term.
    '''
    VECTOR = 25002
    r'''
    De-embeds the measurement using the gain term and the reflection term.
    '''


class DigitalEqualizationEnabled(Enum):
    DISABLE = 0
    r'''
    Filter is not applied
    '''
    ENABLE = 1
    r'''
    Filter is applied.
    '''


class DirectDownload(Enum):
    DISABLE = 0
    r'''
    The RF In local oscillator signal is not present at the front panel LO OUT connector.
    '''
    ENABLE = 1
    r'''
    The RF In local oscillator signal is present at the front panel LO OUT connector.
    '''
    UNSPECIFIED = -2
    r'''
    The RF IN local oscillator signal may or may not be present at the front panel LO OUT connector, because NI-RFSA may be controlling it.
    '''


class Format(Enum):
    MAGNITUDE_AND_PHASE = 26001
    r'''
    Results in a linear interpolation of the magnitude and a separate linear interpolation of the phase.
    '''
    MAGNITUDE_DB_AND_PHASE = 26002
    r'''
    Results in a linear interpolation of the magnitude, in decibels, and a separate linear interpolation of the phase.
    '''
    REAL_AND_IMAGINARY = 26000
    r'''
    Results in a linear interpolation of the real portion of the complex number and a separate linear interpolation of the complex portion.
    '''


class FrequencySettlingUnits(Enum):
    TIME_AFTER_LOCK = 12000
    r'''
    Specifies the time to wait after the frequency PLL locks.
    '''
    TIME_AFTER_IO = 12001
    r'''
    Specifies the time to wait after all writes occur to change the frequency
    '''
    PPM = 12002
    r'''
    Specifies the minimum frequency accuracy when settling completes. Units are in parts per million (PPM or 1E-6).
    '''


class GenerationMode(Enum):
    CW = 1000
    r'''
    Configures the RF signal generator to generate a CW signal.
    '''
    ARB_WAVEFORM = 1001
    r'''
    Configures the RF signal generator to generate the arbitrary waveform specified by the arb_selected_waveform property.
    '''
    SCRIPT = 1002
    r'''
    Configures the RF signal generator to generate arbitrary waveforms as directed by the selected_script property.
    '''


class IQOutPortTerminalConfiguration(Enum):
    DIFFERENTIAL = 15000
    r'''
    Sets the terminal configuration to differential.
    '''
    SINGLE_ENDED = 15001
    r'''
    Sets the terminal configuration to single-ended.
    '''


class LoOutExportConfigureFromRfsaEnable(Enum):
    DISABLE = 0
    r'''
    Do not allow NI-RFSA to control the NI-RFSG local oscillator export.
    '''
    ENABLE = 1
    r'''
    Allow NI-RFSA to control the NI-RFSG local oscillator export.
    '''


class LoPllFractionalModeEnabled(Enum):
    DISABLE = 0
    r'''
    Disables fractional mode for the LO PLL.
    '''
    ENABLE = 1
    r'''
    Enables fractional mode for the LO PLL.
    '''


class LoSource(Enum):
    ONBOARD = 'Onboard'
    r'''
    Uses an internal LO as the LO source. If you specify an internal LO source, the LO is generated inside the device itself.
    '''
    LO_IN = 'LO_In'
    r'''
    Uses an external LO as the LO source. Connect a signal to the LO IN connector on the device and use the UPCONVERTER_CENTER_FREQUENCY property to specify the LO frequency.
    '''
    SECONDARY = 'Secondary'
    r'''
    Uses the PXIe-5831/5840 internal LO as the LO source. This value is valid only on the PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653.
    '''
    SG_SA_SHARED = 'SG_SA_Shared'
    r'''
    Uses the same internal LO during NI-RFSA and NI-RFSG sessions. NI-RFSG selects an internal synthesizer and the synthesizer signal is switched to both the RF In and RF Out mixers. This value is valid only on the PXIe-5830/5831/5832/5841 with PXIe-5655/5842.
    '''
    AUTOMATIC_SG_SA_SHARED = 'Automatic_SG_SA_Shared'
    r'''
    NI-RFSG internally makes the configuration to share the LO between NI-RFSA and NI-RFSG. This value is valid only on the PXIe-5820/5830/5831/5832/5840/5841/5842.
    '''


class LoadConfigurationResetOptions(Enum):
    WAVEFORMS = 1
    r'''
    NI-RFSG skips resetting the waveform configurations.
    '''
    DEEMBEDDING_TABLES = 8
    r'''
    NI-RFSG skips resetting the de-embedding tables.
    '''
    SCRIPTS = 2
    r'''
    NI-RFSG skips resetting the scripts.
    '''
    NONE = 0
    r'''
    NI-RFSG resets all configurations.
    '''


class LoadOptions(Enum):
    NONE = 0
    r'''
    NI-RFSG loads all the configurations to the session.
    '''
    WAVEFORMS = 1
    r'''
    NI-RFSG skips loading the waveform configurations to the session.
    '''
    SCRIPTS = 2
    r'''
    NI-RFSG skips loading the scripts to the session.
    '''


class LoopBandwidth(Enum):
    NARROW = 0
    r'''
    Uses the narrowest loop bandwidth setting for the PLL.
    '''
    MEDIUM = 1
    r'''
    Uses the medium loop bandwidth setting for the PLL.
    '''
    WIDE = 2
    r'''
    Uses the widest loop bandwidth setting for the PLL.
    '''


class MarkerEventOutputBehavior(Enum):
    PULSE = 23000
    r'''
    Specifies the Marker Event output behavior as pulse.
    '''
    TOGGLE = 23001
    r'''
    Specifies the Marker Event output behavior as toggle.
    '''


class MarkerEventPulseWidthUnits(Enum):
    SECONDS = 22000
    r'''
    Specifies the Marker Event pulse width units as seconds.
    '''
    SAMPLE_CLOCK_PERIODS = 22001
    r'''
    Specifies the Marker Event pulse width units as Sample Clock periods.
    '''


class MarkerEventToggleInitialState(Enum):
    LOW = 21000
    r'''
    Specifies the initial state of the Marker Event toggle behavior as digital low.
    '''
    HIGH = 21001
    r'''
    Specifies the initial state of the Marker Event toggle behavior as digital high.
    '''


class Module(Enum):
    AWG = 13001
    r'''
    The AWG associated with the primary module.
    '''
    LO = 13002
    r'''
    The LO associated with the primary module.
    '''
    PRIMARY_MODULE = 13000
    r'''
    The stand-alone device or the main module in a multi-module device.
    '''


class OffsetUnits(Enum):
    PERCENT = 11000
    r'''
    Specifies the unit in percentage.
    '''
    VOLTS = 11001
    r'''
    Specifies the unit in volts.
    '''


class OutputPort(Enum):
    RF_OUT = 14000
    r'''
    Enables the RF OUT port. This value is not valid for the PXIe-5820.
    '''
    IQ_OUT = 14001
    r'''
    Enables the I/Q OUT port. This value is valid on only the PXIe-5645 and PXIe-5820.
    '''
    CAL_OUT = 14002
    r'''
    Enables the CAL OUT port.
    '''
    I_ONLY = 14003
    r'''
    Enables the I connectors of the I/Q OUT port. This value is valid on only the PXIe-5645.
    '''


class OverflowErrorReporting(Enum):
    WARNING = 1301
    r'''
    NI-RFSG returns a warning when an OSP overflow occurs.
    '''
    DISABLED = 1302
    r'''
    NI-RFSG does not return an error or a warning when an OSP overflow occurs.
    '''


class PhaseContinuityEnabled(Enum):
    AUTO = -1
    r'''
    The arbitrary waveform may be repeated to ensure phase continuity after upconversion. This setting could cause waveform size to increase.
    '''
    DISABLE = 0
    r'''
    The arbitrary waveform plays back without regard to any possible phase discontinuities introduced by upconversion. The time duration of the original waveform is maintained.
    '''
    ENABLE = 1
    r'''
    The arbitrary waveform may be repeated to ensure phase continuity after upconversion. Enabling this property could cause waveform size to increase.
    '''


class PowerLevelType(Enum):
    AVERAGE = 7000
    r'''
    Indicates the desired power averaged in time. The driver maximizes the dynamic range by scaling the I/Q waveform so that its peak magnitude is equal to one. If your write more than one waveform, NI-RFSG scales each waveform without preserving the power level ratio between the waveforms. This value is not valid for the PXIe-5820.
    '''
    PEAK = 7001
    r'''
    Indicates the maximum power level of the RF signal averaged over one period of the RF carrier frequency (the peak envelope power). This setting requires that the magnitude of the I/Q waveform must always be less than or equal to one. When using peak power, the power level of the RF signal matches the specified power level at moments when the magnitude of the I/Q waveform equals one. If you write more than one waveform, the relative scaling between waveforms is preserved. In peak power mode, waveforms are scaled according to the arb_waveform_software_scaling_factor property. You can use the peak_power_adjustment property in conjunction with the power_level property when the power_level_type property is set to PowerLevelType.PEAK.
    '''


class PulseModulationMode(Enum):
    OPTIMAL_MATCH = 20000
    r'''
    Provides for a more optimal power output match for the device during the off cycle of the pulse mode operation. Not supported on PXIe-5842
    '''
    HIGH_ISOLATION = 20001
    r'''
    Allows for the best on/off power ratio of the pulsed signal.
    '''
    ANALOG = 20002
    r'''
    Analog switch blanking. Balance between switching speed and on/off power ratio of the pulsed signal.
    '''
    DIGITAL = 20003
    r'''
    Digital only modulation. Provides the best on/off switching speed of the pulsed signal at the cost of signal isolation.
    '''


class PulseModulationOutputTerminal(Enum):
    DO_NOT_EXPORT = ''
    r'''
    Pulse modulation video signal is not exported.
    '''
    PULSE_OUT = 'PulseOut'
    r'''
    Export the pulse modulation video signal on the pulse out terminal.
    '''


class PulseModulationSource(Enum):
    PULSE_IN = 'PulseIn'
    r'''
    The trigger is received on the PULSE IN terminal. This value is valid on only the PXIe-5842.
    '''
    MARKER0 = 'Marker0'
    r'''
    The trigger is received from the Marker 0.
    '''
    MARKER1 = 'Marker1'
    r'''
    The trigger is received from the Marker 1.
    '''
    MARKER2 = 'Marker2'
    r'''
    The trigger is received from the Marker 2.
    '''
    MARKER3 = 'Marker3'
    r'''
    The trigger is received from the Marker 3.
    '''
    DO_NOT_DRIVE_SIGNAL = ''
    r'''
    Do not drive pulse modulation.
    '''


class RFBlanking(Enum):
    DISABLE = 0
    r'''
    RF blanking is disabled.
    '''
    ENABLE = 1
    r'''
    RF blanking is enabled.
    '''


class RFInLoExportEnabled(Enum):
    UNSPECIFIED = -2
    r'''
    The RF IN local oscillator signal may or may not be present at the front panel LO OUT connector, because NI-RFSA may
    '''
    DISABLE = 0
    r'''
    The RF In local oscillator signal is not present at the front panel LO OUT connector.
    '''
    ENABLE = 1
    r'''
    The RF In local oscillator signal is present at the front panel LO OUT connector.
    '''


class ReferenceClockExportOutputTerminal(Enum):
    DO_NOT_EXPORT = ''
    r'''
    The Reference Clock signal is not exported.
    '''
    REF_OUT = 'RefOut'
    r'''
    Exports the Reference Clock signal to the REF OUT connector of the device.
    '''
    REF_OUT2 = 'RefOut2'
    r'''
    Exports the Reference Clock signal to the REF OUT2 connector of the device, if applicable.
    '''
    CLK_OUT = 'ClkOut'
    r'''
    Exports the Reference Clock signal to the CLK OUT connector of the device.
    '''


class ReferenceClockSource(Enum):
    ONBOARD_CLOCK = 'OnboardClock'
    r'''
    Uses the onboard Reference Clock as the clock source.
    '''
    REF_IN = 'RefIn'
    r'''
    Uses the clock signal present at the front panel REF IN connector as the Reference Clock source.
    '''
    PXI_CLK = 'PXI_CLK'
    r'''
    Uses the PXI_CLK signal, which is present on the PXI backplane, as the Reference Clock source.
    '''
    CLK_IN = 'ClkIn'
    r'''
    Uses the clock signal present at the front panel CLK IN connector as the Reference Clock source. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5841 with PXIe-5655.
    '''
    REF_IN_2 = 'RefIn2'
    r'''
    This value is not valid on any supported devices.
    '''
    PXI_CLK_MASTER = 'PXI_ClkMaster'
    r'''
    This value is valid on only the PXIe-5831/5832 with PXIe-5653. **PXIe-5831/5832 with PXIe-5653 -** NI-RFSG configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3622 to use ReferenceClockSource.PXI_CLK as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector.
    '''


class ReferencePllBandwidth(Enum):
    NARROW = 0
    r'''
    Uses the narrowest loop bandwidth setting for the PLL. Setting this property to NIRFSG_VAL_NARROW allows the PXIe-5653 to lock to a reference with worse phase noise than the PXIe-5653 and utilize the better phase noise of the PXIe-5653.
    '''
    MEDIUM = 1
    r'''
    Uses the medium loop bandwidth setting for the PLL.
    '''
    WIDE = 2
    r'''
    Uses the widest loop bandwidth setting for the PLL. Setting this property to NIRFSG_VAL_WIDE on the PXIe-5653 allows the reference PLL to lock to a better reference with better phase noise than the PXIe-5653 and utilize the better phase noise of the reference.
    '''


class RelativeTo(Enum):
    CURRENT_POSITION = 8001
    r'''
    The reference position is relative to the current position.
    '''
    START_OF_WAVEFORM = 8000
    r'''
    The reference position is relative to the start of the waveform.
    '''


class ResetWithOptionsStepsToOmit(IntFlag):
    DEEMBEDDING_TABLES = 8
    r'''
    Omits deleting de-embedding tables. This step is valid only for the PXIe-5830/5831/5832/5840.
    '''
    NONE = 0
    r'''
    No step is omitted during reset.
    '''
    ROUTES = 4
    r'''
    Omits the routing reset step. Routing is preserved after a reset. However, routing related properties are reset to default, and routing is released if the default properties are committed after a reset.
    '''
    SCRIPTS = 2
    r'''
    Omits clearing scripts.
    '''
    WAVEFORMS = 1
    r'''
    Omits clearing waveforms.
    '''


class ScriptTriggerDigitalEdgeEdge(Enum):
    RISING = 0
    r'''
    Asserts the trigger when the signal transitions from low level to high level.
    '''
    FALLING = 1
    r'''
    Asserts the trigger when the signal transitions from high level to low level.
    '''


class ScriptTriggerDigitalLevelActiveLevel(Enum):
    HIGH = 9000
    r'''
    Trigger when the digital trigger signal is high.
    '''
    LOW = 9001
    r'''
    Trigger when the digital trigger signal is low.
    '''


class ScriptTriggerType(Enum):
    NONE = 0
    r'''
    No trigger is configured. Signal generation starts immediately.
    '''
    DIGITAL_EDGE = 1
    r'''
    The data operation does not start until a digital edge is detected. The source of the digital edge is specified with the digital_edge_start_trigger_source property, and the active edge is specified with the digital_edge_start_trigger_edge property.
    '''
    DIGITAL_LEVEL = 8000
    r'''
    The data operation does not start until the digital level is detected. The source of the digital level is specified in the digital_level_script_trigger_source property, and the active level is specified in the digital_level_script_trigger_active_level property.
    '''
    SOFTWARE = 2
    r'''
    The data operation does not start until a software trigger occurs. You can create a software event by calling the send_software_edge_trigger method.
    '''


class SelfCalibrateRangeStepsToOmit(IntFlag):
    IMAGE_SUPPRESSION = 8
    r'''
    Omits the Image Suppression step. If you omit this step, the Residual Sideband Image performance is not adjusted.
    '''
    LO_SELF_CAL = 1
    r'''
    Omits the LO Self Cal step. If you omit this step, the power level of the LO is not adjusted.
    '''
    OMIT_NONE = 0
    r'''
    No calibration steps are omitted.
    '''
    POWER_LEVEL_ACCURACY = 2
    r'''
    Omits the Power Level Accuracy step. If you omit this step, the power level accuracy of the device is not adjusted.
    '''
    RESIDUAL_LO_POWER = 4
    r'''
    Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted.
    '''
    SYNTHESIZER_ALIGNMENT = 16
    r'''
    Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.
    '''


class Signal(Enum):
    START_TRIGGER = 0
    r'''
    Exports a Start Trigger.
    '''
    SCRIPT_TRIGGER = 1
    r'''
    Exports a Script Trigger.
    '''
    MARKER_EVENT = 2
    r'''
    Exports a Marker Event.
    '''
    REF_CLOCK = 3
    r'''
    Exports the Reference Clock.
    '''
    STARTED_EVENT = 4
    r'''
    Exports a Started Event.
    '''
    DONE_EVENT = 5
    r'''
    Exports a Done Event.
    '''


class SoftwareTriggerType(Enum):
    SCRIPT = 1
    r'''
    Specifies the Script Trigger.
    '''
    START = 0
    r'''
    Specifies the Start Trigger.
    '''


class SparameterOrientation(Enum):
    PORT1_TOWARDS_DUT = 24000
    r'''
    Port 1 of the S2P is oriented towards the DUT port.
    '''
    PORT2_TOWARDS_DUT = 24001
    r'''
    Port 2 of the S2P is oriented towards the DUT port.
    '''


class StartTriggerDigitalEdgeEdge(Enum):
    RISING = 0
    r'''
    Occurs when the signal transitions from low level to high level.
    '''
    FALLING = 1
    r'''
    Occurs when the signal transitions from high level to low level.
    '''


class StartTriggerType(Enum):
    NONE = 0
    r'''
    No trigger is configured.
    '''
    DIGITAL_EDGE = 1
    r'''
    The data operation does not start until a digital edge is detected. The source of the digital edge is specified with the digital_edge_start_trigger_source property, and the active edge is specified in the digital_edge_start_trigger_edge property.
    '''
    SOFTWARE = 2
    r'''
    The data operation does not start until a software event occurs. You may create a software trigger by calling the send_software_edge_trigger method.
    '''


class TriggerIdentifier(Enum):
    SCRIPT_TRIGGER0 = 'scriptTrigger0'
    r'''
    Specifies Script Trigger 0.
    '''
    SCRIPT_TRIGGER1 = 'scriptTrigger1'
    r'''
    Specifies Script Trigger 1.
    '''
    SCRIPT_TRIGGER2 = 'scriptTrigger2'
    r'''
    Specifies Script Trigger 2.
    '''
    SCRIPT_TRIGGER3 = 'scriptTrigger3'
    r'''
    Specifies Script Trigger 3.
    '''
    NONE = ''
    r'''
    None (no signal to export)
    '''


class UpconverterFrequencyOffsetMode(Enum):
    AUTO = -1
    r'''
    NI-RFSG places the upconverter center frequency outside of the signal bandwidth if the signal_bandwidth property has been set and can be avoided.
    '''
    ENABLE = 1
    r'''
    NI-RFSG places the upconverter center frequency outside of the signal bandwidth if the signal_bandwidth property has been set and can be avoided. NI-RFSG returns an error if the signal_bandwidth property has not been set, or if the signal bandwidth is too large.
    '''
    USER_DEFINED = 5001
    r'''
    NI-RFSG uses the offset that you specified with the upconverter_frequency_offset or upconverter_center_frequency properties.
    '''


class WriteWaveformBurstDetection(Enum):
    DISABLE = 0
    r'''
    Burst detection is disabled.
    '''
    ENABLE = 1
    r'''
    Burst detection is enabled.
    '''


class WriteWaveformBurstDetectionMode(Enum):
    AUTO = -1
    r'''
    NI-RFSG automatically detects the burst start and burst stop locations by analyzing the waveform.
    '''
    MANUAL = 0
    r'''
    User sets the burst detection parameters.
    '''


class WriteWaveformNormalization(Enum):
    DISABLE = 0
    r'''
    Disables normalization on the waveform.
    '''
    ENABLE = 1
    r'''
    Enables normalization on a waveform to transform the waveform data so that its maximum is 1.00 and its minimum is -1.00
    '''


class YigMainCoilDrive(Enum):
    MANUAL = 0
    r'''
    Adjusts the YIG main coil for an underdamped response.
    '''
    FAST = 1
    r'''
    Adjusts the YIG main coil for an overdamped response.
    '''
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nirfsg/nirfsg/errors.py sha256=2e13073ce026354c098725c52b10123e59386576393fa312474c57cba3d23903 bytes=4349 -->
## FILE: generated/nirfsg/nirfsg/errors.py

- repository: `ni/nimi-python`
- source_path: `generated/nirfsg/nirfsg/errors.py`
- sha256: `2e13073ce026354c098725c52b10123e59386576393fa312474c57cba3d23903`
- bytes: 4349

````python
# -*- coding: utf-8 -*-
# This file was generated


import platform
import warnings


def _is_success(code):
    return (code == 0)


def _is_error(code):
    return (code < 0)


def _is_warning(code):
    return (code > 0)


class Error(Exception):
    '''Base error class for NI-RFSG'''

    def __init__(self, message):
        super(Error, self).__init__(message)


class DriverError(Error):
    '''An error originating from the NI-RFSG driver'''

    def __init__(self, code, description):
        assert _is_error(code), "Should not raise Error if code is not fatal."
        self.code = code
        self.description = description
        super(DriverError, self).__init__(str(self.code) + ": " + self.description)


class DriverWarning(Warning):
    '''A warning originating from the NI-RFSG driver'''

    def __init__(self, code, description):
        assert _is_warning(code), "Should not create Warning if code is not positive."
        super(DriverWarning, self).__init__('Warning {} occurred.\n\n{}'.format(code, description))


class RpcError(Error):
    '''An error specific to sessions to the NI gRPC Device Server'''

    def __init__(self, rpc_code, description):
        self.rpc_code = rpc_code
        self.description = description
        try:
            import grpc
            rpc_error = str(grpc.StatusCode(self.rpc_code))
        except Exception:
            rpc_error = str(self.rpc_code)
        super(RpcError, self).__init__(rpc_error + ": " + self.description)


class UnsupportedConfigurationError(Error):
    '''An error due to using this module in an usupported platform.'''

    def __init__(self):
        super(UnsupportedConfigurationError, self).__init__('System configuration is unsupported: ' + platform.architecture()[0] + ' ' + platform.system())


class DriverNotInstalledError(Error):
    '''An error due to using this module without the driver runtime installed.'''

    def __init__(self):
        super(DriverNotInstalledError, self).__init__('The NI-RFSG runtime could not be loaded. Make sure it is installed and its bitness matches that of your Python interpreter. Please visit http://www.ni.com/downloads/drivers/ to download and install it.')


class DriverTooOldError(Error):
    '''An error due to using this module with an older version of the NI-RFSG driver runtime.'''

    def __init__(self):
        super(DriverTooOldError, self).__init__('A function was not found in the NI-RFSG runtime. Please visit http://www.ni.com/downloads/drivers/ to download a newer version and install it.')


class DriverTooNewError(Error):
    '''An error due to the NI-RFSG driver runtime being too new for this module.'''

    def __init__(self):
        super(DriverTooNewError, self).__init__('The NI-RFSG runtime returned an unexpected value. This can occur if it is too new for the nirfsg Python module. Upgrade the nirfsg Python module.')


class InvalidRepeatedCapabilityError(Error):
    '''An error due to an invalid character in a repeated capability'''

    def __init__(self, invalid_character, invalid_string):
        super(InvalidRepeatedCapabilityError, self).__init__('An invalid character ({}) was found in repeated capability string ({})'.format(invalid_character, invalid_string))


class SelfTestError(Error):
    '''An error due to a failed self-test'''

    def __init__(self, code, msg):
        self.code = code
        self.message = msg
        super(SelfTestError, self).__init__('Self-test failed with code {}: {}'.format(code, msg))


def handle_error(library_interpreter, code, ignore_warnings, is_error_handling):
    '''handle_error

    Helper function for handling errors returned by nirfsg.Library.
    It calls back into the LibraryInterpreter to get the corresponding error
    description and raises if necessary.
    '''

    if _is_success(code) or (_is_warning(code) and ignore_warnings):
        return

    if is_error_handling:
        # The caller is in the midst of error handling and an error occurred.
        # Don't try to get the description or we'll start recursing until the stack overflows.
        description = ''
    else:
        description = library_interpreter.get_error_description(code)

    if _is_error(code):
        raise DriverError(code, description)

    assert _is_warning(code)
    warnings.warn(DriverWarning(code, description))
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nirfsg/nirfsg/grpc_session_options.py sha256=60c6975d4f0a41eb633d0c8107fcc8469ab0f678413453476d75b4aa4f5996a0 bytes=3452 -->
## FILE: generated/nirfsg/nirfsg/grpc_session_options.py

- repository: `ni/nimi-python`
- source_path: `generated/nirfsg/nirfsg/grpc_session_options.py`
- sha256: `60c6975d4f0a41eb633d0c8107fcc8469ab0f678413453476d75b4aa4f5996a0`
- bytes: 3452

````python
# -*- coding: utf-8 -*-
# This file was generated

from enum import IntEnum


# This constant specifies the gRPC package and service used by this API.
# Customers can pass this value to the MeasurementLink discovery service to resolve the server instance that provides this interface.
GRPC_SERVICE_INTERFACE_NAME = 'nirfsg_grpc.NiRFSG'

# This constant specifies the API license key required by the NI gRPC Device Server that comes with
# MeasurementLink 2023 Q1.
MEASUREMENTLINK_23Q1_NIMI_PYTHON_API_KEY = 'DE10751B-3EE0-44EC-A93B-800E6A3C89E4'


class SessionInitializationBehavior(IntEnum):
    AUTO = 0
    r'''
    The NI gRPC Device Server will attach to an existing session with the specified name if it exists, otherwise the server
    will initialize a new session.

    Note:
    When using the Session as a context manager and the context exits, the behavior depends on what happened when the constructor
    was called. If it resulted in a new session being initialized on the NI gRPC Device Server, then it will automatically close the
    server session. If it instead attached to an existing session, then it will detach from the server session and leave it open.
    '''
    INITIALIZE_SERVER_SESSION = 1
    r'''
    Require the NI gRPC Device Server to initialize a new session with the specified name.

    Note:
    When using the Session as a context manager and the context exits, it will automatically close the
    server session.
    '''
    ATTACH_TO_SERVER_SESSION = 2
    r'''
    Require the NI gRPC Device Server to attach to an existing session with the specified name.

    Note:
    When using the Session as a context manager and the context exits, it will detach from the server session
    and leave it open.
    '''


class GrpcSessionOptions(object):
    '''Collection of options that specifies session behaviors related to gRPC.'''

    def __init__(
        self,
        grpc_channel,
        session_name,
        *,
        api_key=MEASUREMENTLINK_23Q1_NIMI_PYTHON_API_KEY,
        initialization_behavior=SessionInitializationBehavior.AUTO
    ):
        r'''Collection of options that specifies session behaviors related to gRPC.

        Creates and returns an object you can pass to a Session constructor.

        Args:
            grpc_channel (grpc.Channel): Specifies the channel to the NI gRPC Device Server.

            session_name (str): User-specified name that identifies the driver session on the NI gRPC Device
                Server. This is different from the resource name parameter many APIs take as a separate
                parameter. Specifying a name makes it easy to share sessions across multiple gRPC clients.
                You can use an empty string if you want to always initialize a new session on the server.
                To attach to an existing session, you must specify the session name it was initialized with.

            api_key (str): Specifies the API license key required by the NI gRPC Device Server.

            initialization_behavior (enum): Specifies whether it is acceptable to initialize a new
                session or attach to an existing one, or if only one of the behaviors is desired.
                The driver session exists on the NI gRPC Device Server.
        '''
        self.grpc_channel = grpc_channel
        self.session_name = session_name
        self.api_key = api_key
        self.initialization_behavior = initialization_behavior
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nirfsg/nirfsg/nidevice_pb2.py sha256=9a935a95cbe830099345438b27f1460989b073de2e873f43cb394ac0df4ced54 bytes=2009 -->
## FILE: generated/nirfsg/nirfsg/nidevice_pb2.py

- repository: `ni/nimi-python`
- source_path: `generated/nirfsg/nirfsg/nidevice_pb2.py`
- sha256: `9a935a95cbe830099345438b27f1460989b073de2e873f43cb394ac0df4ced54`
- bytes: 2009

````python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nidevice.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0enidevice.proto\x12\rnidevice_grpc\"2\n\x0fNIComplexNumber\x12\x0c\n\x04real\x18\x01 \x01(\x01\x12\x11\n\timaginary\x18\x02 \x01(\x01\"5\n\x12NIComplexNumberF32\x12\x0c\n\x04real\x18\x01 \x01(\x02\x12\x11\n\timaginary\x18\x02 \x01(\x02\"/\n\x0cNIComplexI16\x12\x0c\n\x04real\x18\x01 \x01(\x11\x12\x11\n\timaginary\x18\x02 \x01(\x11\"r\n\x0fSmtSpectrumInfo\x12\x15\n\rspectrum_type\x18\x01 \x01(\r\x12\x11\n\tlinear_db\x18\x02 \x01(\r\x12\x0e\n\x06window\x18\x03 \x01(\r\x12\x13\n\x0bwindow_size\x18\x04 \x01(\x11\x12\x10\n\x08\x66\x66t_size\x18\x05 \x01(\x11\x42\x42\n\x12\x63om.ni.grpc.deviceB\x08NiDeviceP\x01\xaa\x02\x1fNationalInstruments.Grpc.Deviceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nidevice_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022com.ni.grpc.deviceB\010NiDeviceP\001\252\002\037NationalInstruments.Grpc.Device'
  _globals['_NICOMPLEXNUMBER']._serialized_start=33
  _globals['_NICOMPLEXNUMBER']._serialized_end=83
  _globals['_NICOMPLEXNUMBERF32']._serialized_start=85
  _globals['_NICOMPLEXNUMBERF32']._serialized_end=138
  _globals['_NICOMPLEXI16']._serialized_start=140
  _globals['_NICOMPLEXI16']._serialized_end=187
  _globals['_SMTSPECTRUMINFO']._serialized_start=189
  _globals['_SMTSPECTRUMINFO']._serialized_end=303
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nirfsg/nirfsg/nidevice_pb2_grpc.py sha256=d686e804f171693117b7d030ec4023f205c70c234c8590f6557aa8702f65fe09 bytes=159 -->
## FILE: generated/nirfsg/nirfsg/nidevice_pb2_grpc.py

- repository: `ni/nimi-python`
- source_path: `generated/nirfsg/nirfsg/nidevice_pb2_grpc.py`
- sha256: `d686e804f171693117b7d030ec4023f205c70c234c8590f6557aa8702f65fe09`
- bytes: 159

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nirfsg/nirfsg/nirfsg_pb2.py sha256=48be8c80d912d6aa009d969cb6de32c2d6437671e3242f44acde57361191a754 bytes=125149 -->
## FILE: generated/nirfsg/nirfsg/nirfsg_pb2.py

- repository: `ni/nimi-python`
- source_path: `generated/nirfsg/nirfsg/nirfsg_pb2.py`
- sha256: `48be8c80d912d6aa009d969cb6de32c2d6437671e3242f44acde57361191a754`
- bytes: 125149

````python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nirfsg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import nidevice_pb2 as nidevice__pb2
import session_pb2 as session__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cnirfsg.proto\x12\x0bnirfsg_grpc\x1a\x0enidevice.proto\x1a\rsession.proto\"2\n\x0c\x41\x62ortRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\x1f\n\rAbortResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"p\n\x1a\x41llocateArbWaveformRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t\x12\x17\n\x0fsize_in_samples\x18\x03 \x01(\x11\"-\n\x1b\x41llocateArbWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x9d\x01\n\x1e\x43heckAttributeViBooleanRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nirfsg_grpc.NiRFSGAttribute\x12\r\n\x05value\x18\x04 \x01(\x08\"1\n\x1f\x43heckAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xe9\x01\n\x1c\x43heckAttributeViInt32Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nirfsg_grpc.NiRFSGAttribute\x12\x38\n\x05value\x18\x04 \x01(\x0e\x32\'.nirfsg_grpc.NiRFSGInt32AttributeValuesH\x00\x12\x13\n\tvalue_raw\x18\x05 \x01(\x11H\x00\x42\x0c\n\nvalue_enum\"/\n\x1d\x43heckAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x9f\x01\n\x1c\x43heckAttributeViInt64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nirfsg_grpc.NiRFSGAttribute\x12\x11\n\tvalue_raw\x18\x04 \x01(\x03\"/\n\x1d\x43heckAttributeViInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xeb\x01\n\x1d\x43heckAttributeViReal64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nirfsg_grpc.NiRFSGAttribute\x12\x39\n\x05value\x18\x04 \x01(\x0e\x32(.nirfsg_grpc.NiRFSGReal64AttributeValuesH\x00\x12\x13\n\tvalue_raw\x18\x05 \x01(\x01H\x00\x42\x0c\n\nvalue_enum\"0\n\x1e\x43heckAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xb5\x01\n\x1e\x43heckAttributeViSessionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nirfsg_grpc.NiRFSGAttribute\x12%\n\x05value\x18\x04 \x01(\x0b\x32\x16.nidevice_grpc.Session\"1\n\x1f\x43heckAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xf8\x01\n\x1d\x43heckAttributeViStringRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nirfsg_grpc.NiRFSGAttribute\x12\x46\n\x0cvalue_mapped\x18\x04 \x01(\x0e\x32..nirfsg_grpc.NiRFSGStringAttributeValuesMappedH\x00\x12\x13\n\tvalue_raw\x18\x05 \x01(\tH\x00\x42\x0c\n\nvalue_enum\"0\n\x1e\x43heckAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"B\n\x1c\x43heckGenerationStatusRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"@\n\x1d\x43heckGenerationStatusResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07is_done\x18\x02 \x01(\x08\"^\n%CheckIfConfigurationListExistsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tlist_name\x18\x02 \x01(\t\"M\n&CheckIfConfigurationListExistsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0blist_exists\x18\x02 \x01(\x08\"U\n\x1a\x43heckIfScriptExistsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x13\n\x0bscript_name\x18\x02 \x01(\t\"D\n\x1b\x43heckIfScriptExistsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rscript_exists\x18\x02 \x01(\x08\"Y\n\x1c\x43heckIfWaveformExistsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t\"H\n\x1d\x43heckIfWaveformExistsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fwaveform_exists\x18\x02 \x01(\x08\"A\n\x1b\x43learAllArbWaveformsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\".\n\x1c\x43learAllArbWaveformsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"K\n\x17\x43learArbWaveformRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0c\n\x04name\x18\x02 \x01(\t\"*\n\x18\x43learArbWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"7\n\x11\x43learErrorRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"$\n\x12\x43learErrorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"D\n\x1e\x43learSelfCalibrateRangeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"1\n\x1f\x43learSelfCalibrateRangeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"2\n\x0c\x43loseRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\x1f\n\rCloseResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"3\n\rCommitRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\" \n\x0e\x43ommitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xda\x01\n3ConfigureDeembeddingTableInterpolationLinearRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0c\n\x04port\x18\x02 \x01(\t\x12\x12\n\ntable_name\x18\x03 \x01(\t\x12\x38\n\x06\x66ormat\x18\x04 \x01(\x0e\x32&.nirfsg_grpc.LinearInterpolationFormatH\x00\x12\x14\n\nformat_raw\x18\x05 \x01(\x11H\x00\x42\r\n\x0b\x66ormat_enum\"F\n4ConfigureDeembeddingTableInterpolationLinearResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"|\n4ConfigureDeembeddingTableInterpolationNearestRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0c\n\x04port\x18\x02 \x01(\t\x12\x12\n\ntable_name\x18\x03 \x01(\t\"G\n5ConfigureDeembeddingTableInterpolationNearestResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"{\n3ConfigureDeembeddingTableInterpolationSplineRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0c\n\x04port\x18\x02 \x01(\t\x12\x12\n\ntable_name\x18\x03 \x01(\t\"F\n4ConfigureDeembeddingTableInterpolationSplineResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xa6\x02\n7ConfigureDigitalEdgeConfigurationListStepTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12S\n\rsource_mapped\x18\x02 \x01(\x0e\x32:.nirfsg_grpc.DigitalEdgeConfigurationListStepTriggerSourceH\x00\x12\x14\n\nsource_raw\x18\x03 \x01(\tH\x00\x12,\n\x04\x65\x64ge\x18\x04 \x01(\x0e\x32\x1c.nirfsg_grpc.DigitalEdgeEdgeH\x01\x12\x12\n\x08\x65\x64ge_raw\x18\x05 \x01(\x11H\x01\x42\r\n\x0bsource_enumB\x0b\n\tedge_enum\"J\n8ConfigureDigitalEdgeConfigurationListStepTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xf2\x02\n(ConfigureDigitalEdgeScriptTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12L\n\x11trigger_id_mapped\x18\x02 \x01(\x0e\x32/.nirfsg_grpc.DigitalEdgeScriptTriggerIdentifierH\x00\x12\x18\n\x0etrigger_id_raw\x18\x03 \x01(\tH\x00\x12\x33\n\rsource_mapped\x18\x04 \x01(\x0e\x32\x1a.nirfsg_grpc.TriggerSourceH\x01\x12\x14\n\nsource_raw\x18\x05 \x01(\tH\x01\x12,\n\x04\x65\x64ge\x18\x06 \x01(\x0e\x32\x1c.nirfsg_grpc.DigitalEdgeEdgeH\x02\x12\x12\n\x08\x65\x64ge_raw\x18\x07 \x01(\x11H\x02\x42\x11\n\x0ftrigger_id_enumB\r\n\x0bsource_enumB\x0b\n\tedge_enum\";\n)ConfigureDigitalEdgeScriptTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xf6\x01\n\'ConfigureDigitalEdgeStartTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x33\n\rsource_mapped\x18\x02 \x01(\x0e\x32\x1a.nirfsg_grpc.TriggerSourceH\x00\x12\x14\n\nsource_raw\x18\x03 \x01(\tH\x00\x12,\n\x04\x65\x64ge\x18\x04 \x01(\x0e\x32\x1c.nirfsg_grpc.DigitalEdgeEdgeH\x01\x12\x12\n\x08\x65\x64ge_raw\x18\x05 \x01(\x11H\x01\x42\r\n\x0bsource_enumB\x0b\n\tedge_enum\":\n(ConfigureDigitalEdgeStartTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xfe\x02\n)ConfigureDigitalLevelScriptTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12L\n\x11trigger_id_mapped\x18\x02 \x01(\x0e\x32/.nirfsg_grpc.DigitalEdgeScriptTriggerIdentifierH\x00\x12\x18\n\x0etrigger_id_raw\x18\x03 \x01(\tH\x00\x12\x33\n\rsource_mapped\x18\x04 \x01(\x0e\x32\x1a.nirfsg_grpc.TriggerSourceH\x01\x12\x14\n\nsource_raw\x18\x05 \x01(\tH\x01\x12\x35\n\x05level\x18\x06 \x01(\x0e\x32$.nirfsg_grpc.DigitalLevelActiveLevelH\x02\x12\x13\n\tlevel_raw\x18\x07 \x01(\x11H\x02\x42\x11\n\x0ftrigger_id_enumB\r\n\x0bsource_enumB\x0c\n\nlevel_enum\"<\n*ConfigureDigitalLevelScriptTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"y\n4ConfigureDigitalModulationUserDefinedWaveformRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x1d\n\x15user_defined_waveform\x18\x02 \x01(\x0c\"G\n5ConfigureDigitalModulationUserDefinedWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xb3\x01\n\x1e\x43onfigureGenerationModeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x36\n\x0fgeneration_mode\x18\x02 \x01(\x0e\x32\x1b.nirfsg_grpc.GenerationModeH\x00\x12\x1d\n\x13generation_mode_raw\x18\x03 \x01(\x11H\x00\x42\x16\n\x14generation_mode_enum\"1\n\x1f\x43onfigureGenerationModeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"[\n\x1d\x43onfigureOutputEnabledRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x16\n\x0eoutput_enabled\x18\x02 \x01(\x08\"0\n\x1e\x43onfigureOutputEnabledResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"z\n/ConfigureP2PEndpointFullnessStartTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12#\n\x1bp2p_endpoint_fullness_level\x18\x02 \x01(\x03\"B\n0ConfigureP2PEndpointFullnessStartTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xbf\x01\n\x1f\x43onfigurePXIChassisClk10Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12?\n\x17pxi_clk10_source_mapped\x18\x02 \x01(\x0e\x32\x1c.nirfsg_grpc.PXIChassisClk10H\x00\x12\x1e\n\x14pxi_clk10_source_raw\x18\x03 \x01(\tH\x00\x42\x17\n\x15pxi_clk10_source_enum\"2\n ConfigurePXIChassisClk10Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xb6\x01\n\x1e\x43onfigurePowerLevelTypeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x37\n\x10power_level_type\x18\x02 \x01(\x0e\x32\x1b.nirfsg_grpc.PowerLevelTypeH\x00\x12\x1e\n\x14power_level_type_raw\x18\x03 \x01(\x11H\x00\x42\x17\n\x15power_level_type_enum\"1\n\x1f\x43onfigurePowerLevelTypeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"`\n\x12\x43onfigureRFRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tfrequency\x18\x02 \x01(\x01\x12\x13\n\x0bpower_level\x18\x03 \x01(\x01\"%\n\x13\x43onfigureRFResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xcf\x01\n\x18\x43onfigureRefClockRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12>\n\x17ref_clock_source_mapped\x18\x02 \x01(\x0e\x32\x1b.nirfsg_grpc.RefClockSourceH\x00\x12\x1e\n\x14ref_clock_source_raw\x18\x03 \x01(\tH\x00\x12\x16\n\x0eref_clock_rate\x18\x04 \x01(\x01\x42\x17\n\x15ref_clock_source_enum\"+\n\x19\x43onfigureRefClockResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"_\n\x1f\x43onfigureSignalBandwidthRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x18\n\x10signal_bandwidth\x18\x02 \x01(\x01\"2\n ConfigureSignalBandwidthResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xc6\x01\n%ConfigureSoftwareScriptTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12L\n\x11trigger_id_mapped\x18\x02 \x01(\x0e\x32/.nirfsg_grpc.DigitalEdgeScriptTriggerIdentifierH\x00\x12\x18\n\x0etrigger_id_raw\x18\x03 \x01(\tH\x00\x42\x11\n\x0ftrigger_id_enum\"8\n&ConfigureSoftwareScriptTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"J\n$ConfigureSoftwareStartTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"7\n%ConfigureSoftwareStartTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x86\x01\n*ConfigureUpconverterPLLSettlingTimeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x19\n\x11pll_settling_time\x18\x02 \x01(\x01\x12\x19\n\x11\x65nsure_pll_locked\x18\x03 \x01(\x08\"=\n+ConfigureUpconverterPLLSettlingTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xb8\x01\n\x1e\x43reateConfigurationListRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tlist_name\x18\x02 \x01(\t\x12\x43\n\x1d\x63onfiguration_list_attributes\x18\x03 \x03(\x0e\x32\x1c.nirfsg_grpc.NiRFSGAttribute\x12\x1a\n\x12set_as_active_list\x18\x04 \x01(\x08\"1\n\x1f\x43reateConfigurationListResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"d\n\"CreateConfigurationListStepRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x1a\n\x12set_as_active_step\x18\x02 \x01(\x08\"5\n#CreateConfigurationListStepResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xe7\x02\n,CreateDeembeddingSparameterTableArrayRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0c\n\x04port\x18\x02 \x01(\t\x12\x12\n\ntable_name\x18\x03 \x01(\t\x12\x13\n\x0b\x66requencies\x18\x04 \x03(\x01\x12\x38\n\x10sparameter_table\x18\x05 \x03(\x0b\x32\x1e.nidevice_grpc.NIComplexNumber\x12\x17\n\x0fnumber_of_ports\x18\x06 \x01(\x11\x12\x44\n\x16sparameter_orientation\x18\x07 \x01(\x0e\x32\".nirfsg_grpc.SParameterOrientationH\x00\x12$\n\x1asparameter_orientation_raw\x18\x08 \x01(\x11H\x00\x42\x1d\n\x1bsparameter_orientation_enum\"?\n-CreateDeembeddingSparameterTableArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x98\x02\n.CreateDeembeddingSparameterTableS2PFileRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0c\n\x04port\x18\x02 \x01(\t\x12\x12\n\ntable_name\x18\x03 \x01(\t\x12\x15\n\rs2p_file_path\x18\x04 \x01(\t\x12\x44\n\x16sparameter_orientation\x18\x05 \x01(\x0e\x32\".nirfsg_grpc.SParameterOrientationH\x00\x12$\n\x1asparameter_orientation_raw\x18\x06 \x01(\x11H\x00\x42\x1d\n\x1bsparameter_orientation_enum\"A\n/CreateDeembeddingSparameterTableS2PFileResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"G\n!DeleteAllDeembeddingTablesRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"4\n\"DeleteAllDeembeddingTablesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"W\n\x1e\x44\x65leteConfigurationListRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tlist_name\x18\x02 \x01(\t\"1\n\x1f\x44\x65leteConfigurationListResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"e\n\x1d\x44\x65leteDeembeddingTableRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0c\n\x04port\x18\x02 \x01(\t\x12\x12\n\ntable_name\x18\x03 \x01(\t\"0\n\x1e\x44\x65leteDeembeddingTableResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"N\n\x13\x44\x65leteScriptRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x13\n\x0bscript_name\x18\x02 \x01(\t\"&\n\x14\x44\x65leteScriptResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"4\n\x0e\x44isableRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"!\n\x0f\x44isableResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"A\n\x1b\x44isableAllModulationRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\".\n\x1c\x44isableAllModulationResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"P\n*DisableConfigurationListStepTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"=\n+DisableConfigurationListStepTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xbc\x01\n\x1b\x44isableScriptTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12L\n\x11trigger_id_mapped\x18\x02 \x01(\x0e\x32/.nirfsg_grpc.DigitalEdgeScriptTriggerIdentifierH\x00\x12\x18\n\x0etrigger_id_raw\x18\x03 \x01(\tH\x00\x42\x11\n\x0ftrigger_id_enum\".\n\x1c\x44isableScriptTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"@\n\x1a\x44isableStartTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"-\n\x1b\x44isableStartTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"M\n\x13\x45rrorMessageRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x12\n\nerror_code\x18\x02 \x01(\x11\"=\n\x14\x45rrorMessageResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t\"7\n\x11\x45rrorQueryRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"O\n\x12\x45rrorQueryResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nerror_code\x18\x02 \x01(\x11\x12\x15\n\rerror_message\x18\x03 \x01(\t\"\xfd\x02\n\x13\x45xportSignalRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12+\n\x06signal\x18\x02 \x01(\x0e\x32\x19.nirfsg_grpc.RoutedSignalH\x00\x12\x14\n\nsignal_raw\x18\x03 \x01(\x11H\x00\x12\x41\n\x18signal_identifier_mapped\x18\x04 \x01(\x0e\x32\x1d.nirfsg_grpc.SignalIdentifierH\x01\x12\x1f\n\x15signal_identifier_raw\x18\x05 \x01(\tH\x01\x12;\n\x16output_terminal_mapped\x18\x06 \x01(\x0e\x32\x19.nirfsg_grpc.OutputSignalH\x02\x12\x1d\n\x13output_terminal_raw\x18\x07 \x01(\tH\x02\x42\r\n\x0bsignal_enumB\x18\n\x16signal_identifier_enumB\x16\n\x14output_terminal_enum\"&\n\x14\x45xportSignalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"E\n\x1fGetAllNamedWaveformNamesRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"f\n GetAllNamedWaveformNamesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x16\n\x0ewaveform_names\x18\x02 \x01(\t\x12\x1a\n\x12\x61\x63tual_buffer_size\x18\x03 \x01(\x11\">\n\x18GetAllScriptNamesRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"]\n\x19GetAllScriptNamesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x14\n\x0cscript_names\x18\x02 \x01(\t\x12\x1a\n\x12\x61\x63tual_buffer_size\x18\x03 \x01(\x11\"K\n\x10GetScriptRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x13\n\x0bscript_name\x18\x02 \x01(\t\"O\n\x11GetScriptResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06script\x18\x02 \x01(\t\x12\x1a\n\x12\x61\x63tual_buffer_size\x18\x03 \x01(\x11\"\x8c\x01\n\x1cGetAttributeViBooleanRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nirfsg_grpc.NiRFSGAttribute\">\n\x1dGetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08\"\x8a\x01\n\x1aGetAttributeViInt32Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nirfsg_grpc.NiRFSGAttribute\"<\n\x1bGetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x11\"\x8a\x01\n\x1aGetAttributeViInt64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nirfsg_grpc.NiRFSGAttribute\"<\n\x1bGetAttributeViInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x03\"\x8b\x01\n\x1bGetAttributeViReal64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nirfsg_grpc.NiRFSGAttribute\"=\n\x1cGetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01\"\x8c\x01\n\x1cGetAttributeViSessionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nirfsg_grpc.NiRFSGAttribute\"V\n\x1dGetAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\x8b\x01\n\x1bGetAttributeViStringRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nirfsg_grpc.NiRFSGAttribute\"=\n\x1cGetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t\"J\n\x15GetChannelNameRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\r\n\x05index\x18\x02 \x01(\x11\"6\n\x16GetChannelNameResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"F\n GetDeembeddingSparametersRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\xa0\x01\n!GetDeembeddingSparametersResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x33\n\x0bsparameters\x18\x02 \x03(\x0b\x32\x1e.nidevice_grpc.NIComplexNumber\x12\x1d\n\x15number_of_sparameters\x18\x03 \x01(\x11\x12\x17\n\x0fnumber_of_ports\x18\x04 \x01(\x11\"5\n\x0fGetErrorRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"Q\n\x10GetErrorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nerror_code\x18\x02 \x01(\x11\x12\x19\n\x11\x65rror_description\x18\x03 \x01(\t\"R\n,GetExternalCalibrationLastDateAndTimeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\x97\x01\n-GetExternalCalibrationLastDateAndTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04year\x18\x02 \x01(\x11\x12\r\n\x05month\x18\x03 \x01(\x11\x12\x0b\n\x03\x64\x61y\x18\x04 \x01(\x11\x12\x0c\n\x04hour\x18\x05 \x01(\x11\x12\x0e\n\x06minute\x18\x06 \x01(\x11\x12\x0e\n\x06second\x18\x07 \x01(\x11\"@\n\x1aGetMaxSettablePowerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"<\n\x1bGetMaxSettablePowerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01\"\x96\x01\n$GetSelfCalibrationDateAndTimeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12%\n\x06module\x18\x02 \x01(\x0e\x32\x13.nirfsg_grpc.ModuleH\x00\x12\x14\n\nmodule_raw\x18\x03 \x01(\x11H\x00\x42\r\n\x0bmodule_enum\"\x8f\x01\n%GetSelfCalibrationDateAndTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04year\x18\x02 \x01(\x11\x12\r\n\x05month\x18\x03 \x01(\x11\x12\x0b\n\x03\x64\x61y\x18\x04 \x01(\x11\x12\x0c\n\x04hour\x18\x05 \x01(\x11\x12\x0e\n\x06minute\x18\x06 \x01(\x11\x12\x0e\n\x06second\x18\x07 \x01(\x11\"\x96\x01\n$GetSelfCalibrationTemperatureRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12%\n\x06module\x18\x02 \x01(\x0e\x32\x13.nirfsg_grpc.ModuleH\x00\x12\x14\n\nmodule_raw\x18\x03 \x01(\x11H\x00\x42\r\n\x0bmodule_enum\"L\n%GetSelfCalibrationTemperatureResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0btemperature\x18\x02 \x01(\x01\"\x8c\x02\n\x16GetTerminalNameRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12+\n\x06signal\x18\x02 \x01(\x0e\x32\x19.nirfsg_grpc.RoutedSignalH\x00\x12\x14\n\nsignal_raw\x18\x03 \x01(\x11H\x00\x12\x41\n\x18signal_identifier_mapped\x18\x04 \x01(\x0e\x32\x1d.nirfsg_grpc.SignalIdentifierH\x01\x12\x1f\n\x15signal_identifier_raw\x18\x05 \x01(\tH\x01\x42\r\n\x0bsignal_enumB\x18\n\x16signal_identifier_enum\"@\n\x17GetTerminalNameResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rterminal_name\x18\x02 \x01(\t\"L\n\x12GetUserDataRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x12\n\nidentifier\x18\x02 \x01(\t\"M\n\x13GetUserDataResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\x18\n\x10\x61\x63tual_data_size\x18\x03 \x01(\x11\"a\n%GetWaveformBurstStartLocationsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\"b\n&GetWaveformBurstStartLocationsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\tlocations\x18\x02 \x03(\x01\x12\x15\n\rrequired_size\x18\x03 \x01(\x11\"`\n$GetWaveformBurstStopLocationsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\"a\n%GetWaveformBurstStopLocationsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\tlocations\x18\x02 \x03(\x01\x12\x15\n\rrequired_size\x18\x03 \x01(\x11\"b\n&GetWaveformMarkerEventLocationsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\"c\n\'GetWaveformMarkerEventLocationsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\tlocations\x18\x02 \x03(\x01\x12\x15\n\rrequired_size\x18\x03 \x01(\x11\"\xb1\x01\n\x0bInitRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x10\n\x08id_query\x18\x03 \x01(\x08\x12\x14\n\x0creset_device\x18\x04 \x01(\x08\x12M\n\x17initialization_behavior\x18\x05 \x01(\x0e\x32,.nidevice_grpc.SessionInitializationBehavior\"\x82\x01\n\x0cInitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12&\n\x06new_vi\x18\x02 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x19\n\rerror_message\x18\x03 \x01(\tB\x02\x18\x01\x12\x1f\n\x17new_session_initialized\x18\x04 \x01(\x08\"\xd3\x01\n\x16InitWithOptionsRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x10\n\x08id_query\x18\x03 \x01(\x08\x12\x14\n\x0creset_device\x18\x04 \x01(\x08\x12\x15\n\roption_string\x18\x05 \x01(\t\x12M\n\x17initialization_behavior\x18\x06 \x01(\x0e\x32,.nidevice_grpc.SessionInitializationBehavior\"\x89\x01\n\x17InitWithOptionsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\"\n\x02vi\x18\x02 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x19\n\rerror_message\x18\x03 \x01(\tB\x02\x18\x01\x12\x1f\n\x17new_session_initialized\x18\x04 \x01(\x08\"5\n\x0fInitiateRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\"\n\x10InitiateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"D\n\x1eInvalidateAllAttributesRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"1\n\x1fInvalidateAllAttributesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"p\n!LoadConfigurationsFromFileRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x11\n\tfile_path\x18\x03 \x01(\t\"4\n\"LoadConfigurationsFromFileResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"?\n\x19PerformPowerSearchRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\",\n\x1aPerformPowerSearchResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"E\n\x1fPerformThermalCorrectionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"2\n PerformThermalCorrectionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"I\n#QueryArbWaveformCapabilitiesRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\xa4\x01\n$QueryArbWaveformCapabilitiesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1c\n\x14max_number_waveforms\x18\x02 \x01(\x11\x12\x18\n\x10waveform_quantum\x18\x03 \x01(\x11\x12\x19\n\x11min_waveform_size\x18\x04 \x01(\x11\x12\x19\n\x11max_waveform_size\x18\x05 \x01(\x11\"\x92\x01\n*ReadAndDownloadWaveformFromFileTDMSRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t\x12\x11\n\tfile_path\x18\x03 \x01(\t\x12\x16\n\x0ewaveform_index\x18\x04 \x01(\r\"=\n+ReadAndDownloadWaveformFromFileTDMSResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"2\n\x0cResetRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\x1f\n\rResetResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x85\x01\n\x15ResetAttributeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nirfsg_grpc.NiRFSGAttribute\"(\n\x16ResetAttributeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"8\n\x12ResetDeviceRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"%\n\x13ResetDeviceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\">\n\x18ResetWithDefaultsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"+\n\x19ResetWithDefaultsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xb3\x01\n\x17ResetWithOptionsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x41\n\rsteps_to_omit\x18\x02 \x01(\x0e\x32(.nirfsg_grpc.ResetWithOptionsStepsToOmitH\x00\x12\x1b\n\x11steps_to_omit_raw\x18\x03 \x01(\x04H\x00\x42\x14\n\x12steps_to_omit_enum\"*\n\x18ResetWithOptionsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\":\n\x14RevisionQueryRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"f\n\x15RevisionQueryResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\"\n\x1ainstrument_driver_revision\x18\x02 \x01(\t\x12\x19\n\x11\x66irmware_revision\x18\x03 \x01(\t\"n\n\x1fSaveConfigurationsToFileRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x11\n\tfile_path\x18\x03 \x01(\t\"2\n SaveConfigurationsToFileResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"L\n\x18SelectArbWaveformRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0c\n\x04name\x18\x02 \x01(\t\"+\n\x19SelectArbWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"4\n\x0eSelfCalRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"!\n\x0fSelfCalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x97\x02\n\x19SelfCalibrateRangeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x43\n\rsteps_to_omit\x18\x02 \x01(\x0e\x32*.nirfsg_grpc.SelfCalibrateRangeStepsToOmitH\x00\x12\x1b\n\x11steps_to_omit_raw\x18\x03 \x01(\x03H\x00\x12\x15\n\rmin_frequency\x18\x04 \x01(\x01\x12\x15\n\rmax_frequency\x18\x05 \x01(\x01\x12\x17\n\x0fmin_power_level\x18\x06 \x01(\x01\x12\x17\n\x0fmax_power_level\x18\x07 \x01(\x01\x42\x14\n\x12steps_to_omit_enum\",\n\x1aSelfCalibrateRangeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"5\n\x0fSelfTestRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"W\n\x10SelfTestResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x18\n\x10self_test_result\x18\x02 \x01(\x11\x12\x19\n\x11self_test_message\x18\x03 \x01(\t\"\x9a\x02\n\x1eSendSoftwareEdgeTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12,\n\x07trigger\x18\x02 \x01(\x0e\x32\x19.nirfsg_grpc.RoutedSignalH\x00\x12\x15\n\x0btrigger_raw\x18\x03 \x01(\x11H\x00\x12\x42\n\x19trigger_identifier_mapped\x18\x04 \x01(\x0e\x32\x1d.nirfsg_grpc.SignalIdentifierH\x01\x12 \n\x16trigger_identifier_raw\x18\x05 \x01(\tH\x01\x42\x0e\n\x0ctrigger_enumB\x19\n\x17trigger_identifier_enum\"1\n\x1fSendSoftwareEdgeTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xd2\x01\n&SetArbWaveformNextWritePositionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t\x12.\n\x0brelative_to\x18\x03 \x01(\x0e\x32\x17.nirfsg_grpc.RelativeToH\x00\x12\x19\n\x0frelative_to_raw\x18\x04 \x01(\x11H\x00\x12\x0e\n\x06offset\x18\x05 \x01(\x11\x42\x12\n\x10relative_to_enum\"9\n\'SetArbWaveformNextWritePositionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x9b\x01\n\x1cSetAttributeViBooleanRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nirfsg_grpc.NiRFSGAttribute\x12\r\n\x05value\x18\x04 \x01(\x08\"/\n\x1dSetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xe7\x01\n\x1aSetAttributeViInt32Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nirfsg_grpc.NiRFSGAttribute\x12\x38\n\x05value\x18\x04 \x01(\x0e\x32\'.nirfsg_grpc.NiRFSGInt32AttributeValuesH\x00\x12\x13\n\tvalue_raw\x18\x05 \x01(\x11H\x00\x42\x0c\n\nvalue_enum\"-\n\x1bSetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x9d\x01\n\x1aSetAttributeViInt64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nirfsg_grpc.NiRFSGAttribute\x12\x11\n\tvalue_raw\x18\x04 \x01(\x03\"-\n\x1bSetAttributeViInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xe9\x01\n\x1bSetAttributeViReal64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nirfsg_grpc.NiRFSGAttribute\x12\x39\n\x05value\x18\x04 \x01(\x0e\x32(.nirfsg_grpc.NiRFSGReal64AttributeValuesH\x00\x12\x13\n\tvalue_raw\x18\x05 \x01(\x01H\x00\x42\x0c\n\nvalue_enum\".\n\x1cSetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xb3\x01\n\x1cSetAttributeViSessionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nirfsg_grpc.NiRFSGAttribute\x12%\n\x05value\x18\x04 \x01(\x0b\x32\x16.nidevice_grpc.Session\"/\n\x1dSetAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xf6\x01\n\x1bSetAttributeViStringRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nirfsg_grpc.NiRFSGAttribute\x12\x46\n\x0cvalue_mapped\x18\x04 \x01(\x0e\x32..nirfsg_grpc.NiRFSGStringAttributeValuesMappedH\x00\x12\x13\n\tvalue_raw\x18\x05 \x01(\tH\x00\x42\x0c\n\nvalue_enum\".\n\x1cSetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"Z\n\x12SetUserDataRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x12\n\nidentifier\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"%\n\x13SetUserDataResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"t\n%SetWaveformBurstStartLocationsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x11\n\tlocations\x18\x03 \x03(\x01\"8\n&SetWaveformBurstStartLocationsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"s\n$SetWaveformBurstStopLocationsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x11\n\tlocations\x18\x03 \x03(\x01\"7\n%SetWaveformBurstStopLocationsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"u\n&SetWaveformMarkerEventLocationsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x11\n\tlocations\x18\x03 \x03(\x01\"9\n\'SetWaveformMarkerEventLocationsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\\\n\x17WaitUntilSettledRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x1d\n\x15max_time_milliseconds\x18\x02 \x01(\x11\"*\n\x18WaitUntilSettledResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x8f\x01\n\x17WriteArbWaveformRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t\x12\x0e\n\x06i_data\x18\x03 \x03(\x01\x12\x0e\n\x06q_data\x18\x04 \x03(\x01\x12\x19\n\x11more_data_pending\x18\x05 \x01(\x08\"*\n\x18WriteArbWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xae\x01\n!WriteArbWaveformComplexF32Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t\x12\x33\n\x08wfm_data\x18\x03 \x03(\x0b\x32!.nidevice_grpc.NIComplexNumberF32\x12\x19\n\x11more_data_pending\x18\x04 \x01(\x08\"4\n\"WriteArbWaveformComplexF32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xab\x01\n!WriteArbWaveformComplexF64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t\x12\x30\n\x08wfm_data\x18\x03 \x03(\x0b\x32\x1e.nidevice_grpc.NIComplexNumber\x12\x19\n\x11more_data_pending\x18\x04 \x01(\x08\"4\n\"WriteArbWaveformComplexF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x8d\x01\n!WriteArbWaveformComplexI16Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t\x12-\n\x08wfm_data\x18\x03 \x03(\x0b\x32\x1b.nidevice_grpc.NIComplexI16\"4\n\"WriteArbWaveformComplexI16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x92\x01\n\x1aWriteArbWaveformF32Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t\x12\x0e\n\x06i_data\x18\x03 \x03(\x02\x12\x0e\n\x06q_data\x18\x04 \x03(\x02\x12\x19\n\x11more_data_pending\x18\x05 \x01(\x08\"-\n\x1bWriteArbWaveformF32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"H\n\x12WriteScriptRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0e\n\x06script\x18\x02 \x01(\t\"%\n\x13WriteScriptResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05*\xdd\x61\n\x0fNiRFSGAttribute\x12 \n\x1cNIRFSG_ATTRIBUTE_UNSPECIFIED\x10\x00\x12\"\n\x1cNIRFSG_ATTRIBUTE_RANGE_CHECK\x10\x92\x8b@\x12.\n(NIRFSG_ATTRIBUTE_QUERY_INSTRUMENT_STATUS\x10\x93\x8b@\x12\x1c\n\x16NIRFSG_ATTRIBUTE_CACHE\x10\x94\x8b@\x12\x1f\n\x19NIRFSG_ATTRIBUTE_SIMULATE\x10\x95\x8b@\x12\'\n!NIRFSG_ATTRIBUTE_RECORD_COERCIONS\x10\x96\x8b@\x12#\n\x1dNIRFSG_ATTRIBUTE_DRIVER_SETUP\x10\x97\x8b@\x12(\n\"NIRFSG_ATTRIBUTE_INTERCHANGE_CHECK\x10\xa5\x8b@\x12\x1a\n\x14NIRFSG_ATTRIBUTE_SPY\x10\xa6\x8b@\x12.\n(NIRFSG_ATTRIBUTE_USE_SPECIFIC_SIMULATION\x10\xa7\x8b@\x12$\n\x1eNIRFSG_ATTRIBUTE_CHANNEL_COUNT\x10\xdb\x8c@\x12-\n\'NIRFSG_ATTRIBUTE_SPECIFIC_DRIVER_PREFIX\x10\xbe\x8d@\x12-\n\'NIRFSG_ATTRIBUTE_IO_RESOURCE_DESCRIPTOR\x10\xc0\x8d@\x12#\n\x1dNIRFSG_ATTRIBUTE_LOGICAL_NAME\x10\xc1\x8d@\x12\x32\n,NIRFSG_ATTRIBUTE_SUPPORTED_INSTRUMENT_MODELS\x10\xd7\x8d@\x12)\n#NIRFSG_ATTRIBUTE_GROUP_CAPABILITIES\x10\xa1\x8e@\x12,\n&NIRFSG_ATTRIBUTE_FUNCTION_CAPABILITIES\x10\xa2\x8e@\x12\x33\n-NIRFSG_ATTRIBUTE_INSTRUMENT_FIRMWARE_REVISION\x10\x8e\x8f@\x12.\n(NIRFSG_ATTRIBUTE_INSTRUMENT_MANUFACTURER\x10\x8f\x8f@\x12\'\n!NIRFSG_ATTRIBUTE_INSTRUMENT_MODEL\x10\x90\x8f@\x12-\n\'NIRFSG_ATTRIBUTE_SPECIFIC_DRIVER_VENDOR\x10\x91\x8f@\x12\x32\n,NIRFSG_ATTRIBUTE_SPECIFIC_DRIVER_DESCRIPTION\x10\x92\x8f@\x12?\n9NIRFSG_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION\x10\x93\x8f@\x12?\n9NIRFSG_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION\x10\x94\x8f@\x12/\n)NIRFSG_ATTRIBUTE_SPECIFIC_DRIVER_REVISION\x10\xb7\x8f@\x12\'\n!NIRFSG_ATTRIBUTE_REF_CLOCK_SOURCE\x10\xb1\x98\x46\x12\x38\n2NIRFSG_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_SOURCE\x10\xb2\x98\x46\x12=\n7NIRFSG_ATTRIBUTE_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL\x10\xb3\x98\x46\x12/\n)NIRFSG_ATTRIBUTE_PXI_CHASSIS_CLK10_SOURCE\x10\xb4\x98\x46\x12/\n)NIRFSG_ATTRIBUTE_PHASE_CONTINUITY_ENABLED\x10\xb5\x98\x46\x12*\n$NIRFSG_ATTRIBUTE_FREQUENCY_TOLERANCE\x10\xb6\x98\x46\x12\'\n!NIRFSG_ATTRIBUTE_SIGNAL_BANDWIDTH\x10\xb7\x98\x46\x12\x33\n-NIRFSG_ATTRIBUTE_AUTOMATIC_THERMAL_CORRECTION\x10\xb8\x98\x46\x12.\n(NIRFSG_ATTRIBUTE_ATTENUATOR_HOLD_ENABLED\x10\xb9\x98\x46\x12\x30\n*NIRFSG_ATTRIBUTE_ATTENUATOR_HOLD_MAX_POWER\x10\xba\x98\x46\x12*\n$NIRFSG_ATTRIBUTE_PEAK_ENVELOPE_POWER\x10\xbb\x98\x46\x12\x33\n-NIRFSG_ATTRIBUTE_DIGITAL_EQUALIZATION_ENABLED\x10\xbc\x98\x46\x12%\n\x1fNIRFSG_ATTRIBUTE_LO_OUT_ENABLED\x10\xbd\x98\x46\x12?\n9NIRFSG_ATTRIBUTE_ALLOW_OUT_OF_SPECIFICATION_USER_SETTINGS\x10\xbe\x98\x46\x12,\n&NIRFSG_ATTRIBUTE_ARB_CARRIER_FREQUENCY\x10\xbf\x98\x46\x12 \n\x1aNIRFSG_ATTRIBUTE_ARB_POWER\x10\xc0\x98\x46\x12)\n#NIRFSG_ATTRIBUTE_DEVICE_TEMPERATURE\x10\xc1\x98\x46\x12&\n NIRFSG_ATTRIBUTE_GENERATION_MODE\x10\xc2\x98\x46\x12*\n$NIRFSG_ATTRIBUTE_SCRIPT_TRIGGER_TYPE\x10\xc3\x98\x46\x12\x39\n3NIRFSG_ATTRIBUTE_DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE\x10\xc4\x98\x46\x12\x37\n1NIRFSG_ATTRIBUTE_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE\x10\xc5\x98\x46\x12>\n8NIRFSG_ATTRIBUTE_EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL\x10\xc6\x98\x46\x12&\n NIRFSG_ATTRIBUTE_SELECTED_SCRIPT\x10\xc7\x98\x46\x12#\n\x1dNIRFSG_ATTRIBUTE_PHASE_OFFSET\x10\xc8\x98\x46\x12*\n$NIRFSG_ATTRIBUTE_ARB_PRE_FILTER_GAIN\x10\xc9\x98\x46\x12$\n\x1eNIRFSG_ATTRIBUTE_SERIAL_NUMBER\x10\xca\x98\x46\x12%\n\x1fNIRFSG_ATTRIBUTE_LOOP_BANDWIDTH\x10\xcb\x98\x46\x12\x34\n.NIRFSG_ATTRIBUTE_ARB_ONBOARD_SAMPLE_CLOCK_MODE\x10\xcd\x98\x46\x12.\n(NIRFSG_ATTRIBUTE_ARB_SAMPLE_CLOCK_SOURCE\x10\xce\x98\x46\x12,\n&NIRFSG_ATTRIBUTE_ARB_SAMPLE_CLOCK_RATE\x10\xcf\x98\x46\x12-\n\'NIRFSG_ATTRIBUTE_ANALOG_MODULATION_TYPE\x10\xd0\x98\x46\x12\x36\n0NIRFSG_ATTRIBUTE_ANALOG_MODULATION_WAVEFORM_TYPE\x10\xd1\x98\x46\x12;\n5NIRFSG_ATTRIBUTE_ANALOG_MODULATION_WAVEFORM_FREQUENCY\x10\xd2\x98\x46\x12\x35\n/NIRFSG_ATTRIBUTE_ANALOG_MODULATION_FM_DEVIATION\x10\xd3\x98\x46\x12.\n(NIRFSG_ATTRIBUTE_DIGITAL_MODULATION_TYPE\x10\xd4\x98\x46\x12\x35\n/NIRFSG_ATTRIBUTE_DIGITAL_MODULATION_SYMBOL_RATE\x10\xd5\x98\x46\x12\x37\n1NIRFSG_ATTRIBUTE_DIGITAL_MODULATION_WAVEFORM_TYPE\x10\xd6\x98\x46\x12\x34\n.NIRFSG_ATTRIBUTE_DIGITAL_MODULATION_PRBS_ORDER\x10\xd7\x98\x46\x12\x33\n-NIRFSG_ATTRIBUTE_DIGITAL_MODULATION_PRBS_SEED\x10\xd8\x98\x46\x12\x37\n1NIRFSG_ATTRIBUTE_DIGITAL_MODULATION_FSK_DEVIATION\x10\xd9\x98\x46\x12&\n NIRFSG_ATTRIBUTE_DIRECT_DOWNLOAD\x10\xda\x98\x46\x12\'\n!NIRFSG_ATTRIBUTE_POWER_LEVEL_TYPE\x10\xdb\x98\x46\x12&\n NIRFSG_ATTRIBUTE_DIGITAL_PATTERN\x10\xdc\x98\x46\x12(\n\"NIRFSG_ATTRIBUTE_STREAMING_ENABLED\x10\xdd\x98\x46\x12.\n(NIRFSG_ATTRIBUTE_STREAMING_WAVEFORM_NAME\x10\xde\x98\x46\x12<\n6NIRFSG_ATTRIBUTE_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM\x10\xdf\x98\x46\x12/\n)NIRFSG_ATTRIBUTE_DATA_TRANSFER_BLOCK_SIZE\x10\xe0\x98\x46\x12;\n5NIRFSG_ATTRIBUTE_ARB_WAVEFORM_SOFTWARE_SCALING_FACTOR\x10\xe4\x98\x46\x12\x39\n3NIRFSG_ATTRIBUTE_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL\x10\xe5\x98\x46\x12:\n4NIRFSG_ATTRIBUTE_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE\x10\xe6\x98\x46\x12@\n:NIRFSG_ATTRIBUTE_DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL\x10\xe7\x98\x46\x12&\n NIRFSG_ATTRIBUTE_ARB_FILTER_TYPE\x10\xe8\x98\x46\x12:\n4NIRFSG_ATTRIBUTE_ARB_FILTER_ROOT_RAISED_COSINE_ALPHA\x10\xe9\x98\x46\x12=\n7NIRFSG_ATTRIBUTE_UPCONVERTER_CENTER_FREQUENCY_INCREMENT\x10\xea\x98\x46\x12\x44\n>NIRFSG_ATTRIBUTE_UPCONVERTER_CENTER_FREQUENCY_INCREMENT_ANCHOR\x10\xeb\x98\x46\x12\x35\n/NIRFSG_ATTRIBUTE_ARB_FILTER_RAISED_COSINE_ALPHA\x10\xec\x98\x46\x12\"\n\x1cNIRFSG_ATTRIBUTE_MEMORY_SIZE\x10\xed\x98\x46\x12\x35\n/NIRFSG_ATTRIBUTE_ANALOG_MODULATION_PM_DEVIATION\x10\xee\x98\x46\x12:\n4NIRFSG_ATTRIBUTE_EXPORTED_DONE_EVENT_OUTPUT_TERMINAL\x10\xef\x98\x46\x12<\n6NIRFSG_ATTRIBUTE_EXPORTED_MARKER_EVENT_OUTPUT_TERMINAL\x10\xf0\x98\x46\x12=\n7NIRFSG_ATTRIBUTE_EXPORTED_STARTED_EVENT_OUTPUT_TERMINAL\x10\xf1\x98\x46\x12#\n\x1dNIRFSG_ATTRIBUTE_LO_OUT_POWER\x10\xf2\x98\x46\x12\"\n\x1cNIRFSG_ATTRIBUTE_LO_IN_POWER\x10\xf3\x98\x46\x12&\n NIRFSG_ATTRIBUTE_ARB_TEMPERATURE\x10\xf4\x98\x46\x12,\n&NIRFSG_ATTRIBUTE_IQ_IMPAIRMENT_ENABLED\x10\xf5\x98\x46\x12\"\n\x1cNIRFSG_ATTRIBUTE_IQ_I_OFFSET\x10\xf6\x98\x46\x12\"\n\x1cNIRFSG_ATTRIBUTE_IQ_Q_OFFSET\x10\xf7\x98\x46\x12(\n\"NIRFSG_ATTRIBUTE_IQ_GAIN_IMBALANCE\x10\xf8\x98\x46\x12\x1e\n\x18NIRFSG_ATTRIBUTE_IQ_SKEW\x10\xf9\x98\x46\x12%\n\x1fNIRFSG_ATTRIBUTE_LO_TEMPERATURE\x10\xfb\x98\x46\x12@\n:NIRFSG_ATTRIBUTE_EXTERNAL_CALIBRATION_RECOMMENDED_INTERVAL\x10\xfc\x98\x46\x12\x37\n1NIRFSG_ATTRIBUTE_EXTERNAL_CALIBRATION_TEMPERATURE\x10\xfd\x98\x46\x12=\n7NIRFSG_ATTRIBUTE_EXTERNAL_CALIBRATION_USER_DEFINED_INFO\x10\xfe\x98\x46\x12\x46\n@NIRFSG_ATTRIBUTE_EXTERNAL_CALIBRATION_USER_DEFINED_INFO_MAX_SIZE\x10\xff\x98\x46\x12&\n NIRFSG_ATTRIBUTE_IQ_OFFSET_UNITS\x10\x81\x99\x46\x12/\n)NIRFSG_ATTRIBUTE_FREQUENCY_SETTLING_UNITS\x10\x82\x99\x46\x12)\n#NIRFSG_ATTRIBUTE_FREQUENCY_SETTLING\x10\x83\x99\x46\x12&\n NIRFSG_ATTRIBUTE_MODULE_REVISION\x10\x84\x99\x46\x12$\n\x1eNIRFSG_ATTRIBUTE_EXTERNAL_GAIN\x10\x85\x99\x46\x12\x36\n0NIRFSG_ATTRIBUTE_DATA_TRANSFER_MAXIMUM_BANDWIDTH\x10\x86\x99\x46\x12:\n4NIRFSG_ATTRIBUTE_DATA_TRANSFER_PREFERRED_PACKET_SIZE\x10\x87\x99\x46\x12<\n6NIRFSG_ATTRIBUTE_DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS\x10\x88\x99\x46\x12\x35\n/NIRFSG_ATTRIBUTE_ARB_OSCILLATOR_PHASE_DAC_VALUE\x10\x89\x99\x46\x12\x30\n*NIRFSG_ATTRIBUTE_ACTIVE_CONFIGURATION_LIST\x10\x90\x99\x46\x12\x35\n/NIRFSG_ATTRIBUTE_ACTIVE_CONFIGURATION_LIST_STEP\x10\x91\x99\x46\x12;\n5NIRFSG_ATTRIBUTE_CONFIGURATION_LIST_STEP_TRIGGER_TYPE\x10\x92\x99\x46\x12J\nDNIRFSG_ATTRIBUTE_DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE\x10\x93\x99\x46\x12+\n%NIRFSG_ATTRIBUTE_TIMER_EVENT_INTERVAL\x10\x94\x99\x46\x12\x30\n*NIRFSG_ATTRIBUTE_CONFIGURATION_LIST_REPEAT\x10\x96\x99\x46\x12H\nBNIRFSG_ATTRIBUTE_DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_EDGE\x10\x97\x99\x46\x12-\n\'NIRFSG_ATTRIBUTE_CORRECTION_TEMPERATURE\x10\x98\x99\x46\x12O\nINIRFSG_ATTRIBUTE_EXPORTED_CONFIGURATION_LIST_STEP_TRIGGER_OUTPUT_TERMINAL\x10\x99\x99\x46\x12\x32\n,NIRFSG_ATTRIBUTE_STARTED_EVENT_TERMINAL_NAME\x10\xa0\x99\x46\x12/\n)NIRFSG_ATTRIBUTE_DONE_EVENT_TERMINAL_NAME\x10\xa1\x99\x46\x12\x32\n,NIRFSG_ATTRIBUTE_START_TRIGGER_TERMINAL_NAME\x10\xa2\x99\x46\x12\x31\n+NIRFSG_ATTRIBUTE_MARKER_EVENT_TERMINAL_NAME\x10\xa3\x99\x46\x12\x33\n-NIRFSG_ATTRIBUTE_SCRIPT_TRIGGER_TERMINAL_NAME\x10\xa4\x99\x46\x12\x44\n>NIRFSG_ATTRIBUTE_CONFIGURATION_LIST_STEP_TRIGGER_TERMINAL_NAME\x10\xa5\x99\x46\x12*\n$NIRFSG_ATTRIBUTE_YIG_MAIN_COIL_DRIVE\x10\xa6\x99\x46\x12:\n4NIRFSG_ATTRIBUTE_CONFIGURATION_LIST_STEP_IN_PROGRESS\x10\xaa\x99\x46\x12\"\n\x1cNIRFSG_ATTRIBUTE_P2P_ENABLED\x10\xab\x99\x46\x12(\n\"NIRFSG_ATTRIBUTE_P2P_ENDPOINT_SIZE\x10\xac\x99\x46\x12\x36\n0NIRFSG_ATTRIBUTE_P2P_SPACE_AVAILABLE_IN_ENDPOINT\x10\xad\x99\x46\x12;\n5NIRFSG_ATTRIBUTE_P2P_MOST_SPACE_AVAILABLE_IN_ENDPOINT\x10\xae\x99\x46\x12)\n#NIRFSG_ATTRIBUTE_P2P_ENDPOINT_COUNT\x10\xaf\x99\x46\x12@\n:NIRFSG_ATTRIBUTE_P2P_ENDPOINT_FULLNESS_START_TRIGGER_LEVEL\x10\xb0\x99\x46\x12K\nENIRFSG_ATTRIBUTE_EXPORTED_CONFIGURATION_SETTLED_EVENT_OUTPUT_TERMINAL\x10\xb1\x99\x46\x12,\n&NIRFSG_ATTRIBUTE_PEAK_POWER_ADJUSTMENT\x10\xb4\x99\x46\x12(\n\"NIRFSG_ATTRIBUTE_REF_PLL_BANDWIDTH\x10\xb5\x99\x46\x12<\n6NIRFSG_ATTRIBUTE_P2P_DATA_TRANSFER_PERMISSION_INTERVAL\x10\xb6\x99\x46\x12\x43\n=NIRFSG_ATTRIBUTE_P2P_DATA_TRANSFER_PERMISSION_INITIAL_CREDITS\x10\xb7\x99\x46\x12\x33\n-NIRFSG_ATTRIBUTE_SELF_CALIBRATION_TEMPERATURE\x10\xb8\x99\x46\x12)\n#NIRFSG_ATTRIBUTE_AMPLITUDE_SETTLING\x10\xb9\x99\x46\x12.\n(NIRFSG_ATTRIBUTE_STREAMING_WRITE_TIMEOUT\x10\xbc\x99\x46\x12\x38\n2NIRFSG_ATTRIBUTE_PEAK_POWER_ADJUSTMENT_INHERITANCE\x10\xbd\x99\x46\x12\x31\n+NIRFSG_ATTRIBUTE_SYNC_SCRIPT_TRIGGER_MASTER\x10\xbe\x99\x46\x12\x34\n.NIRFSG_ATTRIBUTE_SYNC_SCRIPT_TRIGGER_DIST_LINE\x10\xbf\x99\x46\x12\"\n\x1cNIRFSG_ATTRIBUTE_OUTPUT_PORT\x10\xc0\x99\x46\x12\x34\n.NIRFSG_ATTRIBUTE_IQ_OUT_PORT_CARRIER_FREQUENCY\x10\xc1\x99\x46\x12\x39\n3NIRFSG_ATTRIBUTE_IQ_OUT_PORT_TERMINAL_CONFIGURATION\x10\xc2\x99\x46\x12(\n\"NIRFSG_ATTRIBUTE_IQ_OUT_PORT_LEVEL\x10\xc3\x99\x46\x12\x35\n/NIRFSG_ATTRIBUTE_IQ_OUT_PORT_COMMON_MODE_OFFSET\x10\xc4\x99\x46\x12)\n#NIRFSG_ATTRIBUTE_IQ_OUT_PORT_OFFSET\x10\xc5\x99\x46\x12 \n\x1aNIRFSG_ATTRIBUTE_LO_SOURCE\x10\xc6\x99\x46\x12-\n\'NIRFSG_ATTRIBUTE_LO_FREQUENCY_STEP_SIZE\x10\xc7\x99\x46\x12\x35\n/NIRFSG_ATTRIBUTE_LO_PLL_FRACTIONAL_MODE_ENABLED\x10\xc8\x99\x46\x12*\n$NIRFSG_ATTRIBUTE_INTERPOLATION_DELAY\x10\xc9\x99\x46\x12#\n\x1dNIRFSG_ATTRIBUTE_EVENTS_DELAY\x10\xca\x99\x46\x12\x30\n*NIRFSG_ATTRIBUTE_SYNC_START_TRIGGER_MASTER\x10\xcb\x99\x46\x12\x33\n-NIRFSG_ATTRIBUTE_SYNC_START_TRIGGER_DIST_LINE\x10\xcc\x99\x46\x12:\n4NIRFSG_ATTRIBUTE_ARB_WAVEFORM_REPEAT_COUNT_IS_FINITE\x10\xcd\x99\x46\x12\x30\n*NIRFSG_ATTRIBUTE_ARB_WAVEFORM_REPEAT_COUNT\x10\xce\x99\x46\x12\x33\n-NIRFSG_ATTRIBUTE_UPCONVERTER_FREQUENCY_OFFSET\x10\xd0\x99\x46\x12.\n(NIRFSG_ATTRIBUTE_IQ_OUT_PORT_TEMPERATURE\x10\xd1\x99\x46\x12)\n#NIRFSG_ATTRIBUTE_RF_BLANKING_SOURCE\x10\xd2\x99\x46\x12\x31\n+NIRFSG_ATTRIBUTE_IQ_OUT_PORT_LOAD_IMPEDANCE\x10\xd3\x99\x46\x12\x41\n;NIRFSG_ATTRIBUTE_ANALOG_MODULATION_FM_NARROWBAND_INTEGRATOR\x10\xd5\x99\x46\x12\x37\n1NIRFSG_ATTRIBUTE_ANALOG_MODULATION_FM_SENSITIVITY\x10\xd6\x99\x46\x12\x37\n1NIRFSG_ATTRIBUTE_ANALOG_MODULATION_AM_SENSITIVITY\x10\xd7\x99\x46\x12\x37\n1NIRFSG_ATTRIBUTE_ANALOG_MODULATION_PM_SENSITIVITY\x10\xd8\x99\x46\x12)\n#NIRFSG_ATTRIBUTE_ATTENUATOR_SETTING\x10\xdd\x99\x46\x12\x31\n+NIRFSG_ATTRIBUTE_CONFIGURATION_LIST_IS_DONE\x10\xdf\x99\x46\x12/\n)NIRFSG_ATTRIBUTE_SYNC_SAMPLE_CLOCK_MASTER\x10\xe4\x99\x46\x12\x32\n,NIRFSG_ATTRIBUTE_SYNC_SAMPLE_CLOCK_DIST_LINE\x10\xe5\x99\x46\x12%\n\x1fNIRFSG_ATTRIBUTE_AE_TEMPERATURE\x10\xe6\x99\x46\x12\x1f\n\x19NIRFSG_ATTRIBUTE_AMP_PATH\x10\xe9\x99\x46\x12(\n\"NIRFSG_ATTRIBUTE_FPGA_BITFILE_PATH\x10\xea\x99\x46\x12)\n#NIRFSG_ATTRIBUTE_FAST_TUNING_OPTION\x10\xec\x99\x46\x12,\n&NIRFSG_ATTRIBUTE_PULSE_MODULATION_MODE\x10\xee\x99\x46\x12\x30\n*NIRFSG_ATTRIBUTE_ANALOG_MODULATION_FM_BAND\x10\xef\x99\x46\x12\x30\n*NIRFSG_ATTRIBUTE_ANALOG_MODULATION_PM_MODE\x10\xf0\x99\x46\x12@\n:NIRFSG_ATTRIBUTE_CONFIGURATION_SETTLED_EVENT_TERMINAL_NAME\x10\xf2\x99\x46\x12\"\n\x1cNIRFSG_ATTRIBUTE_ALC_CONTROL\x10\xf3\x99\x46\x12(\n\"NIRFSG_ATTRIBUTE_AUTO_POWER_SEARCH\x10\xf4\x99\x46\x12#\n\x1dNIRFSG_ATTRIBUTE_LO_FREQUENCY\x10\xf7\x99\x46\x12\'\n!NIRFSG_ATTRIBUTE_ARB_DIGITAL_GAIN\x10\xfc\x99\x46\x12\x33\n-NIRFSG_ATTRIBUTE_MARKER_EVENT_OUTPUT_BEHAVIOR\x10\xfe\x99\x46\x12/\n)NIRFSG_ATTRIBUTE_MARKER_EVENT_PULSE_WIDTH\x10\xff\x99\x46\x12\x35\n/NIRFSG_ATTRIBUTE_MARKER_EVENT_PULSE_WIDTH_UNITS\x10\x80\x9a\x46\x12\x38\n2NIRFSG_ATTRIBUTE_MARKER_EVENT_TOGGLE_INITIAL_STATE\x10\x81\x9a\x46\x12/\n)NIRFSG_ATTRIBUTE_MODULE_POWER_CONSUMPTION\x10\x82\x9a\x46\x12\'\n!NIRFSG_ATTRIBUTE_FPGA_TEMPERATURE\x10\x83\x9a\x46\x12\x30\n*NIRFSG_ATTRIBUTE_TEMPERATURE_READ_INTERVAL\x10\x84\x9a\x46\x12/\n)NIRFSG_ATTRIBUTE_P2P_IS_FINITE_GENERATION\x10\x89\x9a\x46\x12\x38\n2NIRFSG_ATTRIBUTE_P2P_NUMBER_OF_SAMPLES_TO_GENERATE\x10\x8a\x9a\x46\x12\x39\n3NIRFSG_ATTRIBUTE_P2P_GENERATION_FIFO_SAMPLE_QUANTUM\x10\x8b\x9a\x46\x12%\n\x1fNIRFSG_ATTRIBUTE_RELATIVE_DELAY\x10\x8c\x9a\x46\x12%\n\x1fNIRFSG_ATTRIBUTE_ABSOLUTE_DELAY\x10\x91\x9a\x46\x12\x35\n/NIRFSG_ATTRIBUTE_DEVICE_INSTANTANEOUS_BANDWIDTH\x10\x92\x9a\x46\x12/\n)NIRFSG_ATTRIBUTE_OVERFLOW_ERROR_REPORTING\x10\x94\x9a\x46\x12+\n%NIRFSG_ATTRIBUTE_HOST_DMA_BUFFER_SIZE\x10\x9f\x9a\x46\x12%\n\x1fNIRFSG_ATTRIBUTE_SELECTED_PORTS\x10\xa1\x9a\x46\x12\x38\n2NIRFSG_ATTRIBUTE_LO_OUT_EXPORT_CONFIGURE_FROM_RFSA\x10\xa2\x9a\x46\x12.\n(NIRFSG_ATTRIBUTE_RF_IN_LO_EXPORT_ENABLED\x10\xa3\x9a\x46\x12@\n:NIRFSG_ATTRIBUTE_THERMAL_CORRECTION_TEMPERATURE_RESOLUTION\x10\xa4\x9a\x46\x12\x38\n2NIRFSG_ATTRIBUTE_UPCONVERTER_FREQUENCY_OFFSET_MODE\x10\xa8\x9a\x46\x12&\n NIRFSG_ATTRIBUTE_AVAILABLE_PORTS\x10\xa9\x9a\x46\x12\'\n!NIRFSG_ATTRIBUTE_FPGA_TARGET_NAME\x10\xab\x9a\x46\x12\'\n!NIRFSG_ATTRIBUTE_DEEMBEDDING_TYPE\x10\xac\x9a\x46\x12\x31\n+NIRFSG_ATTRIBUTE_DEEMBEDDING_SELECTED_TABLE\x10\xad\x9a\x46\x12\x31\n+NIRFSG_ATTRIBUTE_LO_VCO_FREQUENCY_STEP_SIZE\x10\xb1\x9a\x46\x12\x38\n2NIRFSG_ATTRIBUTE_THERMAL_CORRECTION_HEADROOM_RANGE\x10\xb2\x9a\x46\x12\'\n!NIRFSG_ATTRIBUTE_WAVEFORM_IQ_RATE\x10\xb7\x9a\x46\x12\x30\n*NIRFSG_ATTRIBUTE_WAVEFORM_SIGNAL_BANDWIDTH\x10\xb8\x9a\x46\x12/\n)NIRFSG_ATTRIBUTE_WAVEFORM_RUNTIME_SCALING\x10\xb9\x9a\x46\x12$\n\x1eNIRFSG_ATTRIBUTE_WAVEFORM_PAPR\x10\xba\x9a\x46\x12\x35\n/NIRFSG_ATTRIBUTE_FIXED_GROUP_DELAY_ACROSS_PORTS\x10\xbf\x9a\x46\x12(\n\"NIRFSG_ATTRIBUTE_WAVEFORM_FILEPATH\x10\xc0\x9a\x46\x12\x35\n/NIRFSG_ATTRIBUTE_WRITE_WAVEFORM_BURST_DETECTION\x10\xc1\x9a\x46\x12:\n4NIRFSG_ATTRIBUTE_WRITE_WAVEFORM_BURST_DETECTION_MODE\x10\xc2\x9a\x46\x12H\nBNIRFSG_ATTRIBUTE_WRITE_WAVEFORM_BURST_DETECTION_MINIMUM_QUIET_TIME\x10\xc3\x9a\x46\x12\x45\n?NIRFSG_ATTRIBUTE_WRITE_WAVEFORM_BURST_DETECTION_POWER_THRESHOLD\x10\xc4\x9a\x46\x12H\nBNIRFSG_ATTRIBUTE_WRITE_WAVEFORM_BURST_DETECTION_MINIMUM_BURST_TIME\x10\xc5\x9a\x46\x12+\n%NIRFSG_ATTRIBUTE_WAVEFORM_RF_BLANKING\x10\xc6\x9a\x46\x12\x34\n.NIRFSG_ATTRIBUTE_DEEMBEDDING_COMPENSATION_GAIN\x10\xd1\x9a\x46\x12\x41\n;NIRFSG_ATTRIBUTE_LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS\x10\xd2\x9a\x46\x12\x42\n<NIRFSG_ATTRIBUTE_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS\x10\xd3\x9a\x46\x12.\n(NIRFSG_ATTRIBUTE_EXPORTED_REF_CLOCK_RATE\x10\xd4\x9a\x46\x12\x33\n-NIRFSG_ATTRIBUTE_WRITE_WAVEFORM_NORMALIZATION\x10\xd5\x9a\x46\x12-\n\'NIRFSG_ATTRIBUTE_WAVEFORM_WAVEFORM_SIZE\x10\xd9\x9a\x46\x12\x34\n.NIRFSG_ATTRIBUTE_PULSE_MODULATION_ACTIVE_LEVEL\x10\xe3\x9a\x46\x12.\n(NIRFSG_ATTRIBUTE_PULSE_MODULATION_SOURCE\x10\xe4\x9a\x46\x12\x46\n@NIRFSG_ATTRIBUTE_EXPORTED_PULSE_MODULATION_EVENT_OUTPUT_TERMINAL\x10\xe5\x9a\x46\x12\x43\n=NIRFSG_ATTRIBUTE_EXPORTED_PULSE_MODULATION_EVENT_ACTIVE_LEVEL\x10\xe6\x9a\x46\x12$\n\x1eNIRFSG_ATTRIBUTE_SELECTED_PATH\x10\xe7\x9a\x46\x12&\n NIRFSG_ATTRIBUTE_AVAILABLE_PATHS\x10\xe8\x9a\x46\x12\x38\n2NIRFSG_ATTRIBUTE_COMPENSATE_FOR_FILTER_GROUP_DELAY\x10\xc0\xae\x46\x12\'\n!NIRFSG_ATTRIBUTE_UPCONVERTER_GAIN\x10\xb1\xb8\x46\x12\x33\n-NIRFSG_ATTRIBUTE_UPCONVERTER_CENTER_FREQUENCY\x10\xb2\xb8\x46\x12 \n\x1aNIRFSG_ATTRIBUTE_FREQUENCY\x10\xd1\xa5L\x12\"\n\x1cNIRFSG_ATTRIBUTE_POWER_LEVEL\x10\xd2\xa5L\x12%\n\x1fNIRFSG_ATTRIBUTE_OUTPUT_ENABLED\x10\xd4\xa5L\x12/\n)NIRFSG_ATTRIBUTE_PULSE_MODULATION_ENABLED\x10\x83\xa6L\x12%\n\x1fNIRFSG_ATTRIBUTE_REF_CLOCK_RATE\x10\x92\xa8L\x12!\n\x1bNIRFSG_ATTRIBUTE_IQ_ENABLED\x10\xe1\xa8L\x12)\n#NIRFSG_ATTRIBUTE_IQ_NOMINAL_VOLTAGE\x10\xe2\xa8L\x12&\n NIRFSG_ATTRIBUTE_IQ_SWAP_ENABLED\x10\xe4\xa8L\x12,\n&NIRFSG_ATTRIBUTE_ARB_SELECTED_WAVEFORM\x10\x93\xa9L\x12\x1e\n\x18NIRFSG_ATTRIBUTE_IQ_RATE\x10\x94\xa9L\x12+\n%NIRFSG_ATTRIBUTE_ARB_FILTER_FREQUENCY\x10\x95\xa9L\x12/\n)NIRFSG_ATTRIBUTE_ARB_MAX_NUMBER_WAVEFORMS\x10\x96\xa9L\x12+\n%NIRFSG_ATTRIBUTE_ARB_WAVEFORM_QUANTUM\x10\x97\xa9L\x12,\n&NIRFSG_ATTRIBUTE_ARB_WAVEFORM_SIZE_MIN\x10\x98\xa9L\x12,\n&NIRFSG_ATTRIBUTE_ARB_WAVEFORM_SIZE_MAX\x10\x99\xa9L\x12)\n#NIRFSG_ATTRIBUTE_START_TRIGGER_TYPE\x10\x9a\xa9L\x12\x36\n0NIRFSG_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_EDGE\x10\x9b\xa9L*\xe8\n\n-DigitalEdgeConfigurationListStepTriggerSource\x12\x43\n?DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_UNSPECIFIED\x10\x00\x12<\n8DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PFI0\x10\x01\x12<\n8DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PFI1\x10\x02\x12<\n8DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PFI2\x10\x03\x12<\n8DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PFI3\x10\x04\x12\x41\n=DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_TRIG0\x10\x05\x12\x41\n=DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_TRIG1\x10\x06\x12\x41\n=DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_TRIG2\x10\x07\x12\x41\n=DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_TRIG3\x10\x08\x12\x41\n=DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_TRIG4\x10\t\x12\x41\n=DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_TRIG5\x10\n\x12\x41\n=DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_TRIG6\x10\x0b\x12\x41\n=DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_TRIG7\x10\x0c\x12@\n<DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_STAR\x10\r\x12\x45\nADIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_MARKER0_EVENT\x10\x0e\x12\x45\nADIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_MARKER1_EVENT\x10\x0f\x12\x45\nADIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_MARKER2_EVENT\x10\x10\x12\x45\nADIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_MARKER3_EVENT\x10\x11\x12\x43\n?DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_TIMER_EVENT\x10\x12\x12?\n;DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_TRIG_IN\x10\x13*X\n\x0f\x44igitalEdgeEdge\x12!\n\x1d\x44IGITAL_EDGE_EDGE_RISING_EDGE\x10\x00\x12\"\n\x1e\x44IGITAL_EDGE_EDGE_FALLING_EDGE\x10\x01*\xcc\x02\n\"DigitalEdgeScriptTriggerIdentifier\x12\x36\n2DIGITAL_EDGE_SCRIPT_TRIGGER_IDENTIFIER_UNSPECIFIED\x10\x00\x12:\n6DIGITAL_EDGE_SCRIPT_TRIGGER_IDENTIFIER_SCRIPT_TRIGGER0\x10\x01\x12:\n6DIGITAL_EDGE_SCRIPT_TRIGGER_IDENTIFIER_SCRIPT_TRIGGER1\x10\x02\x12:\n6DIGITAL_EDGE_SCRIPT_TRIGGER_IDENTIFIER_SCRIPT_TRIGGER2\x10\x03\x12:\n6DIGITAL_EDGE_SCRIPT_TRIGGER_IDENTIFIER_SCRIPT_TRIGGER3\x10\x04*\x9e\x01\n\x17\x44igitalLevelActiveLevel\x12*\n&DIGITAL_LEVEL_ACTIVE_LEVEL_UNSPECIFIED\x10\x00\x12+\n&DIGITAL_LEVEL_ACTIVE_LEVEL_ACTIVE_HIGH\x10\xa8\x46\x12*\n%DIGITAL_LEVEL_ACTIVE_LEVEL_ACTIVE_LOW\x10\xa9\x46*\x8a\x01\n\x0eGenerationMode\x12\x1f\n\x1bGENERATION_MODE_UNSPECIFIED\x10\x00\x12\x17\n\x12GENERATION_MODE_CW\x10\xe8\x07\x12!\n\x1cGENERATION_MODE_ARB_WAVEFORM\x10\xe9\x07\x12\x1b\n\x16GENERATION_MODE_SCRIPT\x10\xea\x07*\xef\x01\n\x19LinearInterpolationFormat\x12+\n\'LINEAR_INTERPOLATION_FORMAT_UNSPECIFIED\x10\x00\x12\x34\n.LINEAR_INTERPOLATION_FORMAT_REAL_AND_IMAGINARY\x10\x90\xcb\x01\x12\x35\n/LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_AND_PHASE\x10\x91\xcb\x01\x12\x38\n2LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_DB_AND_PHASE\x10\x92\xcb\x01*]\n\x06Module\x12\x16\n\x12MODULE_UNSPECIFIED\x10\x00\x12\x1a\n\x15MODULE_PRIMARY_MODULE\x10\xc8\x65\x12\x0f\n\nMODULE_AWG\x10\xc9\x65\x12\x0e\n\tMODULE_LO\x10\xca\x65*\xe8\x03\n\x0cOutputSignal\x12\x1d\n\x19OUTPUT_SIGNAL_UNSPECIFIED\x10\x00\x12\x1f\n\x1bOUTPUT_SIGNAL_DO_NOT_EXPORT\x10\x01\x12\x16\n\x12OUTPUT_SIGNAL_PFI0\x10\x02\x12\x16\n\x12OUTPUT_SIGNAL_PFI1\x10\x03\x12\x16\n\x12OUTPUT_SIGNAL_PFI4\x10\x04\x12\x16\n\x12OUTPUT_SIGNAL_PFI5\x10\x05\x12\x1a\n\x16OUTPUT_SIGNAL_PXI_STAR\x10\x06\x12\x1b\n\x17OUTPUT_SIGNAL_PXI_TRIG0\x10\x07\x12\x1b\n\x17OUTPUT_SIGNAL_PXI_TRIG1\x10\x08\x12\x1b\n\x17OUTPUT_SIGNAL_PXI_TRIG2\x10\t\x12\x1b\n\x17OUTPUT_SIGNAL_PXI_TRIG3\x10\n\x12\x1b\n\x17OUTPUT_SIGNAL_PXI_TRIG4\x10\x0b\x12\x1b\n\x17OUTPUT_SIGNAL_PXI_TRIG5\x10\x0c\x12\x1b\n\x17OUTPUT_SIGNAL_PXI_TRIG6\x10\r\x12\x1a\n\x16OUTPUT_SIGNAL_REF_OUT2\x10\x0e\x12\x19\n\x15OUTPUT_SIGNAL_REF_OUT\x10\x0f\x12\x1a\n\x16OUTPUT_SIGNAL_TRIG_OUT\x10\x10*\x93\x01\n\x0fPXIChassisClk10\x12!\n\x1dPXI_CHASSIS_CLK10_UNSPECIFIED\x10\x00\x12\x1a\n\x16PXI_CHASSIS_CLK10_NONE\x10\x01\x12#\n\x1fPXI_CHASSIS_CLK10_ONBOARD_CLOCK\x10\x02\x12\x1c\n\x18PXI_CHASSIS_CLK10_REF_IN\x10\x03*y\n\x0ePowerLevelType\x12 \n\x1cPOWER_LEVEL_TYPE_UNSPECIFIED\x10\x00\x12#\n\x1ePOWER_LEVEL_TYPE_AVERAGE_POWER\x10\xd8\x36\x12 \n\x1bPOWER_LEVEL_TYPE_PEAK_POWER\x10\xd9\x36*\xf2\x01\n\x0eRefClockSource\x12 \n\x1cREF_CLOCK_SOURCE_UNSPECIFIED\x10\x00\x12\"\n\x1eREF_CLOCK_SOURCE_ONBOARD_CLOCK\x10\x01\x12\x1b\n\x17REF_CLOCK_SOURCE_REF_IN\x10\x02\x12\x1c\n\x18REF_CLOCK_SOURCE_PXI_CLK\x10\x03\x12\x1b\n\x17REF_CLOCK_SOURCE_CLK_IN\x10\x04\x12\x1d\n\x19REF_CLOCK_SOURCE_REF_IN_2\x10\x05\x12#\n\x1fREF_CLOCK_SOURCE_PXI_CLK_MASTER\x10\x06*p\n\nRelativeTo\x12\x1b\n\x17RELATIVE_TO_UNSPECIFIED\x10\x00\x12\"\n\x1dRELATIVE_TO_START_OF_WAVEFORM\x10\xc0>\x12!\n\x1cRELATIVE_TO_CURRENT_POSITION\x10\xc1>*\x8c\x02\n\x1bResetWithOptionsStepsToOmit\x12)\n%RESET_WITH_OPTIONS_STEPS_TO_OMIT_NONE\x10\x00\x12.\n*RESET_WITH_OPTIONS_STEPS_TO_OMIT_WAVEFORMS\x10\x01\x12,\n(RESET_WITH_OPTIONS_STEPS_TO_OMIT_SCRIPTS\x10\x02\x12+\n\'RESET_WITH_OPTIONS_STEPS_TO_OMIT_ROUTES\x10\x04\x12\x37\n3RESET_WITH_OPTIONS_STEPS_TO_OMIT_DEEMBEDDING_TABLES\x10\x08*\xaf\x02\n\x0cRoutedSignal\x12\x1f\n\x1bROUTED_SIGNAL_START_TRIGGER\x10\x00\x12\x31\n-ROUTED_SIGNAL_CONFIGURATION_LIST_STEP_TRIGGER\x10\x06\x12-\n)ROUTED_SIGNAL_CONFIGURATION_SETTLED_EVENT\x10\x07\x12\x1c\n\x18ROUTED_SIGNAL_DONE_EVENT\x10\x05\x12\x1e\n\x1aROUTED_SIGNAL_MARKER_EVENT\x10\x02\x12\x1b\n\x17ROUTED_SIGNAL_REF_CLOCK\x10\x03\x12 \n\x1cROUTED_SIGNAL_SCRIPT_TRIGGER\x10\x01\x12\x1f\n\x1bROUTED_SIGNAL_STARTED_EVENT\x10\x04*\xa2\x01\n\x15SParameterOrientation\x12\'\n#S_PARAMETER_ORIENTATION_UNSPECIFIED\x10\x00\x12/\n)S_PARAMETER_ORIENTATION_PORT1_TOWARDS_DUT\x10\xc0\xbb\x01\x12/\n)S_PARAMETER_ORIENTATION_PORT2_TOWARDS_DUT\x10\xc1\xbb\x01*\xf4\x02\n\x1dSelfCalibrateRangeStepsToOmit\x12\x30\n,SELF_CALIBRATE_RANGE_STEPS_TO_OMIT_OMIT_NONE\x10\x00\x12\x32\n.SELF_CALIBRATE_RANGE_STEPS_TO_OMIT_LO_SELF_CAL\x10\x01\x12;\n7SELF_CALIBRATE_RANGE_STEPS_TO_OMIT_POWER_LEVEL_ACCURACY\x10\x02\x12\x38\n4SELF_CALIBRATE_RANGE_STEPS_TO_OMIT_RESIDUAL_LO_POWER\x10\x04\x12\x38\n4SELF_CALIBRATE_RANGE_STEPS_TO_OMIT_IMAGE_SUPPRESSION\x10\x08\x12<\n8SELF_CALIBRATE_RANGE_STEPS_TO_OMIT_SYNTHESIZER_ALIGNMENT\x10\x10*\xe9\x02\n\x10SignalIdentifier\x12!\n\x1dSIGNAL_IDENTIFIER_UNSPECIFIED\x10\x00\x12\x1a\n\x16SIGNAL_IDENTIFIER_NONE\x10\x01\x12%\n!SIGNAL_IDENTIFIER_SCRIPT_TRIGGER0\x10\x02\x12%\n!SIGNAL_IDENTIFIER_SCRIPT_TRIGGER1\x10\x03\x12%\n!SIGNAL_IDENTIFIER_SCRIPT_TRIGGER2\x10\x04\x12%\n!SIGNAL_IDENTIFIER_SCRIPT_TRIGGER3\x10\x05\x12\x1d\n\x19SIGNAL_IDENTIFIER_MARKER0\x10\x06\x12\x1d\n\x19SIGNAL_IDENTIFIER_MARKER1\x10\x07\x12\x1d\n\x19SIGNAL_IDENTIFIER_MARKER2\x10\x08\x12\x1d\n\x19SIGNAL_IDENTIFIER_MARKER3\x10\t*\x90\x06\n\rTriggerSource\x12\x1e\n\x1aTRIGGER_SOURCE_UNSPECIFIED\x10\x00\x12\x17\n\x13TRIGGER_SOURCE_PFI0\x10\x01\x12\x17\n\x13TRIGGER_SOURCE_PFI1\x10\x02\x12\x17\n\x13TRIGGER_SOURCE_PFI2\x10\x03\x12\x17\n\x13TRIGGER_SOURCE_PFI3\x10\x04\x12\x1c\n\x18TRIGGER_SOURCE_PXI_TRIG0\x10\x05\x12\x1c\n\x18TRIGGER_SOURCE_PXI_TRIG1\x10\x06\x12\x1c\n\x18TRIGGER_SOURCE_PXI_TRIG2\x10\x07\x12\x1c\n\x18TRIGGER_SOURCE_PXI_TRIG3\x10\x08\x12\x1c\n\x18TRIGGER_SOURCE_PXI_TRIG4\x10\t\x12\x1c\n\x18TRIGGER_SOURCE_PXI_TRIG5\x10\n\x12\x1c\n\x18TRIGGER_SOURCE_PXI_TRIG6\x10\x0b\x12\x1c\n\x18TRIGGER_SOURCE_PXI_TRIG7\x10\x0c\x12\x1b\n\x17TRIGGER_SOURCE_PXI_STAR\x10\r\x12\x1e\n\x1aTRIGGER_SOURCE_PXIE_DSTARB\x10\x0e\x12%\n!TRIGGER_SOURCE_SYNC_START_TRIGGER\x10\x0f\x12&\n\"TRIGGER_SOURCE_SYNC_SCRIPT_TRIGGER\x10\x10\x12\x1a\n\x16TRIGGER_SOURCE_TRIG_IN\x10\x11\x12\x1b\n\x17TRIGGER_SOURCE_PULSE_IN\x10\x12\x12\x17\n\x13TRIGGER_SOURCE_DIO0\x10\x13\x12\x17\n\x13TRIGGER_SOURCE_DIO1\x10\x14\x12\x17\n\x13TRIGGER_SOURCE_DIO2\x10\x15\x12\x17\n\x13TRIGGER_SOURCE_DIO3\x10\x16\x12\x17\n\x13TRIGGER_SOURCE_DIO4\x10\x17\x12\x17\n\x13TRIGGER_SOURCE_DIO5\x10\x18\x12\x17\n\x13TRIGGER_SOURCE_DIO6\x10\x19\x12\x17\n\x13TRIGGER_SOURCE_DIO7\x10\x1a*\x85)\n\x1aNiRFSGInt32AttributeValues\x12\x1c\n\x18NIRFSG_INT32_UNSPECIFIED\x10\x00\x12%\n NIRFSG_INT32_AMP_PATH_HIGH_POWER\x10\x80}\x12\'\n\"NIRFSG_INT32_AMP_PATH_LOW_HARMONIC\x10\x81}\x12\x37\n1NIRFSG_INT32_ANALOG_MODULATION_FM_BAND_NARROWBAND\x10\xe8\x84\x01\x12\x35\n/NIRFSG_INT32_ANALOG_MODULATION_FM_BAND_WIDEBAND\x10\xe9\x84\x01\x12M\nGNIRFSG_INT32_ANALOG_MODULATION_FM_NARROWBAND_INTEGRATOR_100_HZ_TO_1_KHZ\x10\xd0\x8c\x01\x12M\nGNIRFSG_INT32_ANALOG_MODULATION_FM_NARROWBAND_INTEGRATOR_1_KHZ_TO_10_KHZ\x10\xd1\x8c\x01\x12O\nINIRFSG_INT32_ANALOG_MODULATION_FM_NARROWBAND_INTEGRATOR_10_KHZ_TO_100_KHZ\x10\xd2\x8c\x01\x12;\n5NIRFSG_INT32_ANALOG_MODULATION_PM_MODE_HIGH_DEVIATION\x10\xb8\x94\x01\x12<\n6NIRFSG_INT32_ANALOG_MODULATION_PM_MODE_LOW_PHASE_NOISE\x10\xb9\x94\x01\x12,\n(NIRFSG_INT32_ANALOG_MODULATION_TYPE_NONE\x10\x00\x12+\n&NIRFSG_INT32_ANALOG_MODULATION_TYPE_FM\x10\xd0\x0f\x12+\n&NIRFSG_INT32_ANALOG_MODULATION_TYPE_PM\x10\xd1\x0f\x12+\n&NIRFSG_INT32_ANALOG_MODULATION_TYPE_AM\x10\xd2\x0f\x12\x36\n1NIRFSG_INT32_ANALOG_MODULATION_WAVEFORM_TYPE_SINE\x10\xb8\x17\x12\x38\n3NIRFSG_INT32_ANALOG_MODULATION_WAVEFORM_TYPE_SQUARE\x10\xb9\x17\x12:\n5NIRFSG_INT32_ANALOG_MODULATION_WAVEFORM_TYPE_TRIANGLE\x10\xba\x17\x12&\n!NIRFSG_INT32_ARB_FILTER_TYPE_NONE\x10\x90N\x12\x34\n/NIRFSG_INT32_ARB_FILTER_TYPE_ROOT_RAISED_COSINE\x10\x91N\x12/\n*NIRFSG_INT32_ARB_FILTER_TYPE_RAISED_COSINE\x10\x92N\x12?\n:NIRFSG_INT32_ARB_ONBOARD_SAMPLE_CLOCK_MODE_HIGH_RESOLUTION\x10\xf0.\x12;\n6NIRFSG_INT32_ARB_ONBOARD_SAMPLE_CLOCK_MODE_DIVIDE_DOWN\x10\xf1.\x12>\n:NIRFSG_INT32_CONFIG_LIST_TRIGGER_DIG_EDGE_EDGE_RISING_EDGE\x10\x00\x12O\nKNIRFSG_INT32_CONFIGURATION_LIST_REPEAT_CONFIGURATION_LIST_REPEAT_CONTINUOUS\x10\x00\x12K\nGNIRFSG_INT32_CONFIGURATION_LIST_REPEAT_CONFIGURATION_LIST_REPEAT_SINGLE\x10\x01\x12(\n\"NIRFSG_INT32_DEEMBEDDING_TYPE_NONE\x10\xa8\xc3\x01\x12*\n$NIRFSG_INT32_DEEMBEDDING_TYPE_SCALAR\x10\xa9\xc3\x01\x12*\n$NIRFSG_INT32_DEEMBEDDING_TYPE_VECTOR\x10\xaa\xc3\x01\x12.\n*NIRFSG_INT32_DIGITAL_EDGE_EDGE_RISING_EDGE\x10\x00\x12/\n+NIRFSG_INT32_DIGITAL_EDGE_EDGE_FALLING_EDGE\x10\x01\x12\x38\n3NIRFSG_INT32_DIGITAL_LEVEL_ACTIVE_LEVEL_ACTIVE_HIGH\x10\xa8\x46\x12\x37\n2NIRFSG_INT32_DIGITAL_LEVEL_ACTIVE_LEVEL_ACTIVE_LOW\x10\xa9\x46\x12-\n)NIRFSG_INT32_DIGITAL_MODULATION_TYPE_NONE\x10\x00\x12-\n(NIRFSG_INT32_DIGITAL_MODULATION_TYPE_FSK\x10\xa0\x1f\x12-\n(NIRFSG_INT32_DIGITAL_MODULATION_TYPE_OOK\x10\xa1\x1f\x12-\n(NIRFSG_INT32_DIGITAL_MODULATION_TYPE_PSK\x10\xa2\x1f\x12\x37\n2NIRFSG_INT32_DIGITAL_MODULATION_WAVEFORM_TYPE_PRBS\x10\x88\'\x12?\n:NIRFSG_INT32_DIGITAL_MODULATION_WAVEFORM_TYPE_USER_DEFINED\x10\x89\'\x12&\n\"NIRFSG_INT32_ENABLE_VALUES_DISABLE\x10\x00\x12%\n!NIRFSG_INT32_ENABLE_VALUES_ENABLE\x10\x01\x12:\n5NIRFSG_INT32_FREQUENCY_SETTLING_UNITS_TIME_AFTER_LOCK\x10\xe0]\x12\x38\n3NIRFSG_INT32_FREQUENCY_SETTLING_UNITS_TIME_AFTER_IO\x10\xe1]\x12.\n)NIRFSG_INT32_FREQUENCY_SETTLING_UNITS_PPM\x10\xe2]\x12$\n\x1fNIRFSG_INT32_GENERATION_MODE_CW\x10\xe8\x07\x12.\n)NIRFSG_INT32_GENERATION_MODE_ARB_WAVEFORM\x10\xe9\x07\x12(\n#NIRFSG_INT32_GENERATION_MODE_SCRIPT\x10\xea\x07\x12)\n$NIRFSG_INT32_IQ_OFFSET_UNITS_PERCENT\x10\xf8U\x12\'\n\"NIRFSG_INT32_IQ_OFFSET_UNITS_VOLTS\x10\xf9U\x12\x36\n1NIRFSG_INT32_IQ_OUT_PORT_TERM_CONFIG_DIFFERENTIAL\x10\x98u\x12\x36\n1NIRFSG_INT32_IQ_OUT_PORT_TERM_CONFIG_SINGLE_ENDED\x10\x99u\x12,\n(NIRFSG_INT32_LIST_STEP_TRIGGER_TYPE_NONE\x10\x00\x12\x34\n0NIRFSG_INT32_LIST_STEP_TRIGGER_TYPE_DIGITAL_EDGE\x10\x01\x12\'\n#NIRFSG_INT32_LOAD_OPTIONS_SKIP_NONE\x10\x00\x12,\n(NIRFSG_INT32_LOAD_OPTIONS_SKIP_WAVEFORMS\x10\x01\x12&\n\"NIRFSG_INT32_LOOP_BANDWIDTH_NARROW\x10\x00\x12&\n\"NIRFSG_INT32_LOOP_BANDWIDTH_MEDIUM\x10\x01\x12$\n NIRFSG_INT32_LOOP_BANDWIDTH_WIDE\x10\x02\x12\x35\n/NIRFSG_INT32_MARKER_EVENT_OUTPUT_BEHAVIOR_PULSE\x10\xd8\xb3\x01\x12\x36\n0NIRFSG_INT32_MARKER_EVENT_OUTPUT_BEHAVIOR_TOGGLE\x10\xd9\xb3\x01\x12\x39\n3NIRFSG_INT32_MARKER_EVENT_PULSE_WIDTH_UNITS_SECONDS\x10\xf0\xab\x01\x12\x46\n@NIRFSG_INT32_MARKER_EVENT_PULSE_WIDTH_UNITS_SAMPLE_CLOCK_PERIODS\x10\xf1\xab\x01\x12@\n:NIRFSG_INT32_MARKER_EVENT_TOGGLE_INITIAL_STATE_DIGITAL_LOW\x10\x88\xa4\x01\x12\x41\n;NIRFSG_INT32_MARKER_EVENT_TOGGLE_INITIAL_STATE_DIGITAL_HIGH\x10\x89\xa4\x01\x12$\n\x1fNIRFSG_INT32_OUTPUT_PORT_RF_OUT\x10\xb0m\x12$\n\x1fNIRFSG_INT32_OUTPUT_PORT_IQ_OUT\x10\xb1m\x12%\n NIRFSG_INT32_OUTPUT_PORT_CAL_OUT\x10\xb2m\x12$\n\x1fNIRFSG_INT32_OUTPUT_PORT_I_ONLY\x10\xb3m\x12\x32\n-NIRFSG_INT32_OVERFLOW_ERROR_REPORTING_WARNING\x10\x95\n\x12\x33\n.NIRFSG_INT32_OVERFLOW_ERROR_REPORTING_DISABLED\x10\x96\n\x12\x33\n/NIRFSG_INT32_PPA_SCRIPT_INHERITANCE_EXACT_MATCH\x10\x00\x12/\n+NIRFSG_INT32_PPA_SCRIPT_INHERITANCE_MINIMUM\x10\x01\x12/\n+NIRFSG_INT32_PPA_SCRIPT_INHERITANCE_MAXIMUM\x10\x02\x12)\n%NIRFSG_INT32_PHASE_CONTINUITY_DISABLE\x10\x00\x12/\n\"NIRFSG_INT32_PHASE_CONTINUITY_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12(\n$NIRFSG_INT32_PHASE_CONTINUITY_ENABLE\x10\x01\x12\x30\n+NIRFSG_INT32_POWER_LEVEL_TYPE_AVERAGE_POWER\x10\xd8\x36\x12-\n(NIRFSG_INT32_POWER_LEVEL_TYPE_PEAK_POWER\x10\xd9\x36\x12\x36\n0NIRFSG_INT32_PULSE_MODULATION_MODE_OPTIMAL_MATCH\x10\xa0\x9c\x01\x12\x37\n1NIRFSG_INT32_PULSE_MODULATION_MODE_HIGH_ISOLATION\x10\xa1\x9c\x01\x12(\n$NIRFSG_INT32_RESET_OPTIONS_SKIP_NONE\x10\x00\x12-\n)NIRFSG_INT32_RESET_OPTIONS_SKIP_WAVEFORMS\x10\x01\x12+\n\'NIRFSG_INT32_RESET_OPTIONS_SKIP_SCRIPTS\x10\x02\x12\x35\n1NIRFSG_INT32_RESET_OPTIONS_SKIP_DEEMBEDING_TABLES\x10\x08\x12\x30\n,NIRFSG_INT32_RF_IN_LO_EXPORT_ENABLED_DISABLE\x10\x00\x12=\n0NIRFSG_INT32_RF_IN_LO_EXPORT_ENABLED_UNSPECIFIED\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12/\n+NIRFSG_INT32_RF_IN_LO_EXPORT_ENABLED_ENABLE\x10\x01\x12)\n%NIRFSG_INT32_SCRIPT_TRIGGER_TYPE_NONE\x10\x00\x12\x31\n-NIRFSG_INT32_SCRIPT_TRIGGER_TYPE_DIGITAL_EDGE\x10\x01\x12\x33\n.NIRFSG_INT32_SCRIPT_TRIGGER_TYPE_DIGITAL_LEVEL\x10\xc0>\x12-\n)NIRFSG_INT32_SCRIPT_TRIGGER_TYPE_SOFTWARE\x10\x02\x12(\n$NIRFSG_INT32_START_TRIGGER_TYPE_NONE\x10\x00\x12\x30\n,NIRFSG_INT32_START_TRIGGER_TYPE_DIGITAL_EDGE\x10\x01\x12,\n(NIRFSG_INT32_START_TRIGGER_TYPE_SOFTWARE\x10\x02\x12:\n6NIRFSG_INT32_START_TRIGGER_TYPE_P2_P_ENDPOINT_FULLNESS\x10\x03\x12@\n3NIRFSG_INT32_UPCONVERTER_FREQUENCY_OFFSET_MODE_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x39\n5NIRFSG_INT32_UPCONVERTER_FREQUENCY_OFFSET_MODE_ENABLE\x10\x01\x12@\n;NIRFSG_INT32_UPCONVERTER_FREQUENCY_OFFSET_MODE_USER_DEFINED\x10\x89\'\x12;\n7NIRFSG_INT32_WRITE_WAVEFORM_BURST_DETECTION_MODE_MANUAL\x10\x00\x12\x42\n5NIRFSG_INT32_WRITE_WAVEFORM_BURST_DETECTION_MODE_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12#\n\x1fNIRFSG_INT32_YIG_MAIN_COIL_SLOW\x10\x00\x12#\n\x1fNIRFSG_INT32_YIG_MAIN_COIL_FAST\x10\x01\x1a\x02\x10\x01*\x98\x01\n\x1bNiRFSGReal64AttributeValues\x12\x1d\n\x19NIRFSG_REAL64_UNSPECIFIED\x10\x00\x12*\n#NIRFSG_REAL64_REF_CLOCK_RATE_10_MHZ\x10\x80\xad\xe2\x04\x12.\n!NIRFSG_REAL64_REF_CLOCK_RATE_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01*\xd0\x30\n!NiRFSGStringAttributeValuesMapped\x12$\n NIRFSG_STRING_MAPPED_UNSPECIFIED\x10\x00\x12\x36\n2NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DO_NOT_EXPORT\x10\x01\x12-\n)NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PFI0\x10\x02\x12-\n)NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PFI1\x10\x03\x12-\n)NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PFI4\x10\x04\x12-\n)NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PFI5\x10\x05\x12\x32\n.NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PXI_TRIG0\x10\x06\x12\x32\n.NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PXI_TRIG1\x10\x07\x12\x32\n.NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PXI_TRIG2\x10\x08\x12\x32\n.NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PXI_TRIG3\x10\t\x12\x32\n.NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PXI_TRIG4\x10\n\x12\x32\n.NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PXI_TRIG5\x10\x0b\x12\x32\n.NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PXI_TRIG6\x10\x0c\x12\x34\n0NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PXIE_DSTARC\x10\r\x12\x31\n-NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_TRIG_OUT\x10\x0e\x12\x37\n3NIRFSG_STRING_ARB_SAMPLE_CLOCK_SOURCE_ONBOARD_CLOCK\x10\x0f\x12\x30\n,NIRFSG_STRING_ARB_SAMPLE_CLOCK_SOURCE_CLK_IN\x10\x10\x12<\n8NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DO_NOT_EXPORT\x10\x11\x12\x33\n/NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PFI0\x10\x12\x12\x33\n/NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PFI1\x10\x13\x12\x38\n4NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PXI_TRIG0\x10\x14\x12\x38\n4NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PXI_TRIG1\x10\x15\x12\x38\n4NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PXI_TRIG2\x10\x16\x12\x38\n4NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PXI_TRIG3\x10\x17\x12\x38\n4NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PXI_TRIG4\x10\x18\x12\x38\n4NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PXI_TRIG5\x10\x19\x12\x38\n4NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PXI_TRIG6\x10\x1a\x12:\n6NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PXIE_DSTARC\x10\x1b\x12\x37\n3NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_TRIG_OUT\x10\x1c\x12.\n*NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PFI0\x10\x1d\x12.\n*NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PFI1\x10\x1e\x12\x33\n/NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXI_TRIG0\x10\x1f\x12\x33\n/NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXI_TRIG1\x10 \x12\x33\n/NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXI_TRIG2\x10!\x12\x33\n/NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXI_TRIG3\x10\"\x12\x33\n/NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXI_TRIG4\x10#\x12\x33\n/NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXI_TRIG5\x10$\x12\x33\n/NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXI_TRIG6\x10%\x12\x33\n/NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXI_TRIG7\x10&\x12\x35\n1NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXIE_DSTARB\x10\'\x12\x37\n3NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_MARKER0_EVENT\x10(\x12\x37\n3NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_MARKER1_EVENT\x10)\x12\x37\n3NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_MARKER2_EVENT\x10*\x12\x37\n3NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_MARKER3_EVENT\x10+\x12\x35\n1NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_TIMER_EVENT\x10,\x12\x31\n-NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_TRIG_IN\x10-\x12@\n<NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_DO_NOT_EXPORT\x10.\x12<\n8NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_PXI_TRIG0\x10/\x12<\n8NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_PXI_TRIG1\x10\x30\x12<\n8NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_PXI_TRIG2\x10\x31\x12<\n8NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_PXI_TRIG3\x10\x32\x12<\n8NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_PXI_TRIG4\x10\x33\x12<\n8NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_PXI_TRIG5\x10\x34\x12<\n8NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_PXI_TRIG6\x10\x35\x12>\n:NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_PXIE_DSTARC\x10\x36\x12;\n7NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_TRIG_OUT\x10\x37\x12#\n\x1fNIRFSG_STRING_LO_SOURCE_ONBOARD\x10\x38\x12!\n\x1dNIRFSG_STRING_LO_SOURCE_LO_IN\x10\x39\x12%\n!NIRFSG_STRING_LO_SOURCE_SECONDARY\x10:\x12(\n$NIRFSG_STRING_LO_SOURCE_SG_SA_SHARED\x10;\x12\x32\n.NIRFSG_STRING_LO_SOURCE_AUTOMATIC_SG_SA_SHARED\x10<\x12(\n$NIRFSG_STRING_PXI_CHASSIS_CLK10_NONE\x10=\x12\x31\n-NIRFSG_STRING_PXI_CHASSIS_CLK10_ONBOARD_CLOCK\x10>\x12*\n&NIRFSG_STRING_PXI_CHASSIS_CLK10_REF_IN\x10?\x12\x35\n1NIRFSG_STRING_REF_CLOCK_OUTPUT_TERM_DO_NOT_EXPORT\x10@\x12/\n+NIRFSG_STRING_REF_CLOCK_OUTPUT_TERM_REF_OUT\x10\x41\x12\x30\n,NIRFSG_STRING_REF_CLOCK_OUTPUT_TERM_REF_OUT2\x10\x42\x12/\n+NIRFSG_STRING_REF_CLOCK_OUTPUT_TERM_CLK_OUT\x10\x43\x12\x30\n,NIRFSG_STRING_REF_CLOCK_SOURCE_ONBOARD_CLOCK\x10\x44\x12)\n%NIRFSG_STRING_REF_CLOCK_SOURCE_REF_IN\x10\x45\x12*\n&NIRFSG_STRING_REF_CLOCK_SOURCE_PXI_CLK\x10\x46\x12)\n%NIRFSG_STRING_REF_CLOCK_SOURCE_CLK_IN\x10G\x12+\n\'NIRFSG_STRING_REF_CLOCK_SOURCE_REF_IN_2\x10H\x12\x31\n-NIRFSG_STRING_REF_CLOCK_SOURCE_PXI_CLK_MASTER\x10I\x12%\n!NIRFSG_STRING_TRIGGER_SOURCE_PFI0\x10J\x12%\n!NIRFSG_STRING_TRIGGER_SOURCE_PFI1\x10K\x12%\n!NIRFSG_STRING_TRIGGER_SOURCE_PFI2\x10L\x12%\n!NIRFSG_STRING_TRIGGER_SOURCE_PFI3\x10M\x12*\n&NIRFSG_STRING_TRIGGER_SOURCE_PXI_TRIG0\x10N\x12*\n&NIRFSG_STRING_TRIGGER_SOURCE_PXI_TRIG1\x10O\x12*\n&NIRFSG_STRING_TRIGGER_SOURCE_PXI_TRIG2\x10P\x12*\n&NIRFSG_STRING_TRIGGER_SOURCE_PXI_TRIG3\x10Q\x12*\n&NIRFSG_STRING_TRIGGER_SOURCE_PXI_TRIG4\x10R\x12*\n&NIRFSG_STRING_TRIGGER_SOURCE_PXI_TRIG5\x10S\x12*\n&NIRFSG_STRING_TRIGGER_SOURCE_PXI_TRIG6\x10T\x12*\n&NIRFSG_STRING_TRIGGER_SOURCE_PXI_TRIG7\x10U\x12)\n%NIRFSG_STRING_TRIGGER_SOURCE_PXI_STAR\x10V\x12,\n(NIRFSG_STRING_TRIGGER_SOURCE_PXIE_DSTARB\x10W\x12\x33\n/NIRFSG_STRING_TRIGGER_SOURCE_SYNC_START_TRIGGER\x10X\x12\x34\n0NIRFSG_STRING_TRIGGER_SOURCE_SYNC_SCRIPT_TRIGGER\x10Y\x12(\n$NIRFSG_STRING_TRIGGER_SOURCE_TRIG_IN\x10Z\x12-\n)NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DIO0\x10[\x12-\n)NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DIO1\x10\\\x12-\n)NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DIO2\x10]\x12-\n)NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DIO3\x10^\x12-\n)NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DIO4\x10_\x12-\n)NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DIO5\x10`\x12-\n)NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DIO6\x10\x61\x12-\n)NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DIO7\x10\x62\x12\x33\n/NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DIO0\x10\x63\x12\x33\n/NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DIO1\x10\x64\x12\x33\n/NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DIO2\x10\x65\x12\x33\n/NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DIO3\x10\x66\x12\x33\n/NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DIO4\x10g\x12\x33\n/NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DIO5\x10h\x12\x33\n/NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DIO6\x10i\x12\x33\n/NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DIO7\x10j\x12.\n*NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_DIO0\x10k\x12.\n*NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_DIO1\x10l\x12.\n*NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_DIO2\x10m\x12.\n*NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_DIO3\x10n\x12.\n*NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_DIO4\x10o\x12.\n*NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_DIO5\x10p\x12.\n*NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_DIO6\x10q\x12.\n*NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_DIO7\x10r\x12)\n%NIRFSG_STRING_TRIGGER_SOURCE_PULSE_IN\x10s\x12%\n!NIRFSG_STRING_TRIGGER_SOURCE_DIO0\x10t\x12%\n!NIRFSG_STRING_TRIGGER_SOURCE_DIO1\x10u\x12%\n!NIRFSG_STRING_TRIGGER_SOURCE_DIO2\x10v\x12%\n!NIRFSG_STRING_TRIGGER_SOURCE_DIO3\x10w\x12%\n!NIRFSG_STRING_TRIGGER_SOURCE_DIO4\x10x\x12%\n!NIRFSG_STRING_TRIGGER_SOURCE_DIO5\x10y\x12%\n!NIRFSG_STRING_TRIGGER_SOURCE_DIO6\x10z\x12%\n!NIRFSG_STRING_TRIGGER_SOURCE_DIO7\x10{2\xaf\x65\n\x06NiRFSG\x12>\n\x05\x41\x62ort\x12\x19.nirfsg_grpc.AbortRequest\x1a\x1a.nirfsg_grpc.AbortResponse\x12h\n\x13\x41llocateArbWaveform\x12\'.nirfsg_grpc.AllocateArbWaveformRequest\x1a(.nirfsg_grpc.AllocateArbWaveformResponse\x12t\n\x17\x43heckAttributeViBoolean\x12+.nirfsg_grpc.CheckAttributeViBooleanRequest\x1a,.nirfsg_grpc.CheckAttributeViBooleanResponse\x12n\n\x15\x43heckAttributeViInt32\x12).nirfsg_grpc.CheckAttributeViInt32Request\x1a*.nirfsg_grpc.CheckAttributeViInt32Response\x12n\n\x15\x43heckAttributeViInt64\x12).nirfsg_grpc.CheckAttributeViInt64Request\x1a*.nirfsg_grpc.CheckAttributeViInt64Response\x12q\n\x16\x43heckAttributeViReal64\x12*.nirfsg_grpc.CheckAttributeViReal64Request\x1a+.nirfsg_grpc.CheckAttributeViReal64Response\x12t\n\x17\x43heckAttributeViSession\x12+.nirfsg_grpc.CheckAttributeViSessionRequest\x1a,.nirfsg_grpc.CheckAttributeViSessionResponse\x12q\n\x16\x43heckAttributeViString\x12*.nirfsg_grpc.CheckAttributeViStringRequest\x1a+.nirfsg_grpc.CheckAttributeViStringResponse\x12n\n\x15\x43heckGenerationStatus\x12).nirfsg_grpc.CheckGenerationStatusRequest\x1a*.nirfsg_grpc.CheckGenerationStatusResponse\x12\x89\x01\n\x1e\x43heckIfConfigurationListExists\x12\x32.nirfsg_grpc.CheckIfConfigurationListExistsRequest\x1a\x33.nirfsg_grpc.CheckIfConfigurationListExistsResponse\x12h\n\x13\x43heckIfScriptExists\x12\'.nirfsg_grpc.CheckIfScriptExistsRequest\x1a(.nirfsg_grpc.CheckIfScriptExistsResponse\x12n\n\x15\x43heckIfWaveformExists\x12).nirfsg_grpc.CheckIfWaveformExistsRequest\x1a*.nirfsg_grpc.CheckIfWaveformExistsResponse\x12k\n\x14\x43learAllArbWaveforms\x12(.nirfsg_grpc.ClearAllArbWaveformsRequest\x1a).nirfsg_grpc.ClearAllArbWaveformsResponse\x12_\n\x10\x43learArbWaveform\x12$.nirfsg_grpc.ClearArbWaveformRequest\x1a%.nirfsg_grpc.ClearArbWaveformResponse\x12M\n\nClearError\x12\x1e.nirfsg_grpc.ClearErrorRequest\x1a\x1f.nirfsg_grpc.ClearErrorResponse\x12t\n\x17\x43learSelfCalibrateRange\x12+.nirfsg_grpc.ClearSelfCalibrateRangeRequest\x1a,.nirfsg_grpc.ClearSelfCalibrateRangeResponse\x12>\n\x05\x43lose\x12\x19.nirfsg_grpc.CloseRequest\x1a\x1a.nirfsg_grpc.CloseResponse\x12\x41\n\x06\x43ommit\x12\x1a.nirfsg_grpc.CommitRequest\x1a\x1b.nirfsg_grpc.CommitResponse\x12\xb3\x01\n,ConfigureDeembeddingTableInterpolationLinear\x12@.nirfsg_grpc.ConfigureDeembeddingTableInterpolationLinearRequest\x1a\x41.nirfsg_grpc.ConfigureDeembeddingTableInterpolationLinearResponse\x12\xb6\x01\n-ConfigureDeembeddingTableInterpolationNearest\x12\x41.nirfsg_grpc.ConfigureDeembeddingTableInterpolationNearestRequest\x1a\x42.nirfsg_grpc.ConfigureDeembeddingTableInterpolationNearestResponse\x12\xb3\x01\n,ConfigureDeembeddingTableInterpolationSpline\x12@.nirfsg_grpc.ConfigureDeembeddingTableInterpolationSplineRequest\x1a\x41.nirfsg_grpc.ConfigureDeembeddingTableInterpolationSplineResponse\x12\xbf\x01\n0ConfigureDigitalEdgeConfigurationListStepTrigger\x12\x44.nirfsg_grpc.ConfigureDigitalEdgeConfigurationListStepTriggerRequest\x1a\x45.nirfsg_grpc.ConfigureDigitalEdgeConfigurationListStepTriggerResponse\x12\x92\x01\n!ConfigureDigitalEdgeScriptTrigger\x12\x35.nirfsg_grpc.ConfigureDigitalEdgeScriptTriggerRequest\x1a\x36.nirfsg_grpc.ConfigureDigitalEdgeScriptTriggerResponse\x12\x8f\x01\n ConfigureDigitalEdgeStartTrigger\x12\x34.nirfsg_grpc.ConfigureDigitalEdgeStartTriggerRequest\x1a\x35.nirfsg_grpc.ConfigureDigitalEdgeStartTriggerResponse\x12\x95\x01\n\"ConfigureDigitalLevelScriptTrigger\x12\x36.nirfsg_grpc.ConfigureDigitalLevelScriptTriggerRequest\x1a\x37.nirfsg_grpc.ConfigureDigitalLevelScriptTriggerResponse\x12\xb6\x01\n-ConfigureDigitalModulationUserDefinedWaveform\x12\x41.nirfsg_grpc.ConfigureDigitalModulationUserDefinedWaveformRequest\x1a\x42.nirfsg_grpc.ConfigureDigitalModulationUserDefinedWaveformResponse\x12t\n\x17\x43onfigureGenerationMode\x12+.nirfsg_grpc.ConfigureGenerationModeRequest\x1a,.nirfsg_grpc.ConfigureGenerationModeResponse\x12q\n\x16\x43onfigureOutputEnabled\x12*.nirfsg_grpc.ConfigureOutputEnabledRequest\x1a+.nirfsg_grpc.ConfigureOutputEnabledResponse\x12\xa7\x01\n(ConfigureP2PEndpointFullnessStartTrigger\x12<.nirfsg_grpc.ConfigureP2PEndpointFullnessStartTriggerRequest\x1a=.nirfsg_grpc.ConfigureP2PEndpointFullnessStartTriggerResponse\x12w\n\x18\x43onfigurePXIChassisClk10\x12,.nirfsg_grpc.ConfigurePXIChassisClk10Request\x1a-.nirfsg_grpc.ConfigurePXIChassisClk10Response\x12t\n\x17\x43onfigurePowerLevelType\x12+.nirfsg_grpc.ConfigurePowerLevelTypeRequest\x1a,.nirfsg_grpc.ConfigurePowerLevelTypeResponse\x12P\n\x0b\x43onfigureRF\x12\x1f.nirfsg_grpc.ConfigureRFRequest\x1a .nirfsg_grpc.ConfigureRFResponse\x12\x62\n\x11\x43onfigureRefClock\x12%.nirfsg_grpc.ConfigureRefClockRequest\x1a&.nirfsg_grpc.ConfigureRefClockResponse\x12w\n\x18\x43onfigureSignalBandwidth\x12,.nirfsg_grpc.ConfigureSignalBandwidthRequest\x1a-.nirfsg_grpc.ConfigureSignalBandwidthResponse\x12\x89\x01\n\x1e\x43onfigureSoftwareScriptTrigger\x12\x32.nirfsg_grpc.ConfigureSoftwareScriptTriggerRequest\x1a\x33.nirfsg_grpc.ConfigureSoftwareScriptTriggerResponse\x12\x86\x01\n\x1d\x43onfigureSoftwareStartTrigger\x12\x31.nirfsg_grpc.ConfigureSoftwareStartTriggerRequest\x1a\x32.nirfsg_grpc.ConfigureSoftwareStartTriggerResponse\x12\x98\x01\n#ConfigureUpconverterPLLSettlingTime\x12\x37.nirfsg_grpc.ConfigureUpconverterPLLSettlingTimeRequest\x1a\x38.nirfsg_grpc.ConfigureUpconverterPLLSettlingTimeResponse\x12t\n\x17\x43reateConfigurationList\x12+.nirfsg_grpc.CreateConfigurationListRequest\x1a,.nirfsg_grpc.CreateConfigurationListResponse\x12\x80\x01\n\x1b\x43reateConfigurationListStep\x12/.nirfsg_grpc.CreateConfigurationListStepRequest\x1a\x30.nirfsg_grpc.CreateConfigurationListStepResponse\x12\x9e\x01\n%CreateDeembeddingSparameterTableArray\x12\x39.nirfsg_grpc.CreateDeembeddingSparameterTableArrayRequest\x1a:.nirfsg_grpc.CreateDeembeddingSparameterTableArrayResponse\x12\xa4\x01\n\'CreateDeembeddingSparameterTableS2PFile\x12;.nirfsg_grpc.CreateDeembeddingSparameterTableS2PFileRequest\x1a<.nirfsg_grpc.CreateDeembeddingSparameterTableS2PFileResponse\x12}\n\x1a\x44\x65leteAllDeembeddingTables\x12..nirfsg_grpc.DeleteAllDeembeddingTablesRequest\x1a/.nirfsg_grpc.DeleteAllDeembeddingTablesResponse\x12t\n\x17\x44\x65leteConfigurationList\x12+.nirfsg_grpc.DeleteConfigurationListRequest\x1a,.nirfsg_grpc.DeleteConfigurationListResponse\x12q\n\x16\x44\x65leteDeembeddingTable\x12*.nirfsg_grpc.DeleteDeembeddingTableRequest\x1a+.nirfsg_grpc.DeleteDeembeddingTableResponse\x12S\n\x0c\x44\x65leteScript\x12 .nirfsg_grpc.DeleteScriptRequest\x1a!.nirfsg_grpc.DeleteScriptResponse\x12\x44\n\x07\x44isable\x12\x1b.nirfsg_grpc.DisableRequest\x1a\x1c.nirfsg_grpc.DisableResponse\x12k\n\x14\x44isableAllModulation\x12(.nirfsg_grpc.DisableAllModulationRequest\x1a).nirfsg_grpc.DisableAllModulationResponse\x12\x98\x01\n#DisableConfigurationListStepTrigger\x12\x37.nirfsg_grpc.DisableConfigurationListStepTriggerRequest\x1a\x38.nirfsg_grpc.DisableConfigurationListStepTriggerResponse\x12k\n\x14\x44isableScriptTrigger\x12(.nirfsg_grpc.DisableScriptTriggerRequest\x1a).nirfsg_grpc.DisableScriptTriggerResponse\x12h\n\x13\x44isableStartTrigger\x12\'.nirfsg_grpc.DisableStartTriggerRequest\x1a(.nirfsg_grpc.DisableStartTriggerResponse\x12S\n\x0c\x45rrorMessage\x12 .nirfsg_grpc.ErrorMessageRequest\x1a!.nirfsg_grpc.ErrorMessageResponse\x12M\n\nErrorQuery\x12\x1e.nirfsg_grpc.ErrorQueryRequest\x1a\x1f.nirfsg_grpc.ErrorQueryResponse\x12S\n\x0c\x45xportSignal\x12 .nirfsg_grpc.ExportSignalRequest\x1a!.nirfsg_grpc.ExportSignalResponse\x12w\n\x18GetAllNamedWaveformNames\x12,.nirfsg_grpc.GetAllNamedWaveformNamesRequest\x1a-.nirfsg_grpc.GetAllNamedWaveformNamesResponse\x12\x62\n\x11GetAllScriptNames\x12%.nirfsg_grpc.GetAllScriptNamesRequest\x1a&.nirfsg_grpc.GetAllScriptNamesResponse\x12J\n\tGetScript\x12\x1d.nirfsg_grpc.GetScriptRequest\x1a\x1e.nirfsg_grpc.GetScriptResponse\x12n\n\x15GetAttributeViBoolean\x12).nirfsg_grpc.GetAttributeViBooleanRequest\x1a*.nirfsg_grpc.GetAttributeViBooleanResponse\x12h\n\x13GetAttributeViInt32\x12\'.nirfsg_grpc.GetAttributeViInt32Request\x1a(.nirfsg_grpc.GetAttributeViInt32Response\x12h\n\x13GetAttributeViInt64\x12\'.nirfsg_grpc.GetAttributeViInt64Request\x1a(.nirfsg_grpc.GetAttributeViInt64Response\x12k\n\x14GetAttributeViReal64\x12(.nirfsg_grpc.GetAttributeViReal64Request\x1a).nirfsg_grpc.GetAttributeViReal64Response\x12n\n\x15GetAttributeViSession\x12).nirfsg_grpc.GetAttributeViSessionRequest\x1a*.nirfsg_grpc.GetAttributeViSessionResponse\x12k\n\x14GetAttributeViString\x12(.nirfsg_grpc.GetAttributeViStringRequest\x1a).nirfsg_grpc.GetAttributeViStringResponse\x12Y\n\x0eGetChannelName\x12\".nirfsg_grpc.GetChannelNameRequest\x1a#.nirfsg_grpc.GetChannelNameResponse\x12z\n\x19GetDeembeddingSparameters\x12-.nirfsg_grpc.GetDeembeddingSparametersRequest\x1a..nirfsg_grpc.GetDeembeddingSparametersResponse\x12G\n\x08GetError\x12\x1c.nirfsg_grpc.GetErrorRequest\x1a\x1d.nirfsg_grpc.GetErrorResponse\x12\x9e\x01\n%GetExternalCalibrationLastDateAndTime\x12\x39.nirfsg_grpc.GetExternalCalibrationLastDateAndTimeRequest\x1a:.nirfsg_grpc.GetExternalCalibrationLastDateAndTimeResponse\x12h\n\x13GetMaxSettablePower\x12\'.nirfsg_grpc.GetMaxSettablePowerRequest\x1a(.nirfsg_grpc.GetMaxSettablePowerResponse\x12\x86\x01\n\x1dGetSelfCalibrationDateAndTime\x12\x31.nirfsg_grpc.GetSelfCalibrationDateAndTimeRequest\x1a\x32.nirfsg_grpc.GetSelfCalibrationDateAndTimeResponse\x12\x86\x01\n\x1dGetSelfCalibrationTemperature\x12\x31.nirfsg_grpc.GetSelfCalibrationTemperatureRequest\x1a\x32.nirfsg_grpc.GetSelfCalibrationTemperatureResponse\x12\\\n\x0fGetTerminalName\x12#.nirfsg_grpc.GetTerminalNameRequest\x1a$.nirfsg_grpc.GetTerminalNameResponse\x12P\n\x0bGetUserData\x12\x1f.nirfsg_grpc.GetUserDataRequest\x1a .nirfsg_grpc.GetUserDataResponse\x12\x89\x01\n\x1eGetWaveformBurstStartLocations\x12\x32.nirfsg_grpc.GetWaveformBurstStartLocationsRequest\x1a\x33.nirfsg_grpc.GetWaveformBurstStartLocationsResponse\x12\x86\x01\n\x1dGetWaveformBurstStopLocations\x12\x31.nirfsg_grpc.GetWaveformBurstStopLocationsRequest\x1a\x32.nirfsg_grpc.GetWaveformBurstStopLocationsResponse\x12\x8c\x01\n\x1fGetWaveformMarkerEventLocations\x12\x33.nirfsg_grpc.GetWaveformMarkerEventLocationsRequest\x1a\x34.nirfsg_grpc.GetWaveformMarkerEventLocationsResponse\x12;\n\x04Init\x12\x18.nirfsg_grpc.InitRequest\x1a\x19.nirfsg_grpc.InitResponse\x12\\\n\x0fInitWithOptions\x12#.nirfsg_grpc.InitWithOptionsRequest\x1a$.nirfsg_grpc.InitWithOptionsResponse\x12G\n\x08Initiate\x12\x1c.nirfsg_grpc.InitiateRequest\x1a\x1d.nirfsg_grpc.InitiateResponse\x12t\n\x17InvalidateAllAttributes\x12+.nirfsg_grpc.InvalidateAllAttributesRequest\x1a,.nirfsg_grpc.InvalidateAllAttributesResponse\x12}\n\x1aLoadConfigurationsFromFile\x12..nirfsg_grpc.LoadConfigurationsFromFileRequest\x1a/.nirfsg_grpc.LoadConfigurationsFromFileResponse\x12\x65\n\x12PerformPowerSearch\x12&.nirfsg_grpc.PerformPowerSearchRequest\x1a\'.nirfsg_grpc.PerformPowerSearchResponse\x12w\n\x18PerformThermalCorrection\x12,.nirfsg_grpc.PerformThermalCorrectionRequest\x1a-.nirfsg_grpc.PerformThermalCorrectionResponse\x12\x83\x01\n\x1cQueryArbWaveformCapabilities\x12\x30.nirfsg_grpc.QueryArbWaveformCapabilitiesRequest\x1a\x31.nirfsg_grpc.QueryArbWaveformCapabilitiesResponse\x12\x98\x01\n#ReadAndDownloadWaveformFromFileTDMS\x12\x37.nirfsg_grpc.ReadAndDownloadWaveformFromFileTDMSRequest\x1a\x38.nirfsg_grpc.ReadAndDownloadWaveformFromFileTDMSResponse\x12>\n\x05Reset\x12\x19.nirfsg_grpc.ResetRequest\x1a\x1a.nirfsg_grpc.ResetResponse\x12Y\n\x0eResetAttribute\x12\".nirfsg_grpc.ResetAttributeRequest\x1a#.nirfsg_grpc.ResetAttributeResponse\x12P\n\x0bResetDevice\x12\x1f.nirfsg_grpc.ResetDeviceRequest\x1a .nirfsg_grpc.ResetDeviceResponse\x12\x62\n\x11ResetWithDefaults\x12%.nirfsg_grpc.ResetWithDefaultsRequest\x1a&.nirfsg_grpc.ResetWithDefaultsResponse\x12_\n\x10ResetWithOptions\x12$.nirfsg_grpc.ResetWithOptionsRequest\x1a%.nirfsg_grpc.ResetWithOptionsResponse\x12V\n\rRevisionQuery\x12!.nirfsg_grpc.RevisionQueryRequest\x1a\".nirfsg_grpc.RevisionQueryResponse\x12w\n\x18SaveConfigurationsToFile\x12,.nirfsg_grpc.SaveConfigurationsToFileRequest\x1a-.nirfsg_grpc.SaveConfigurationsToFileResponse\x12\x62\n\x11SelectArbWaveform\x12%.nirfsg_grpc.SelectArbWaveformRequest\x1a&.nirfsg_grpc.SelectArbWaveformResponse\x12\x44\n\x07SelfCal\x12\x1b.nirfsg_grpc.SelfCalRequest\x1a\x1c.nirfsg_grpc.SelfCalResponse\x12\x65\n\x12SelfCalibrateRange\x12&.nirfsg_grpc.SelfCalibrateRangeRequest\x1a\'.nirfsg_grpc.SelfCalibrateRangeResponse\x12G\n\x08SelfTest\x12\x1c.nirfsg_grpc.SelfTestRequest\x1a\x1d.nirfsg_grpc.SelfTestResponse\x12t\n\x17SendSoftwareEdgeTrigger\x12+.nirfsg_grpc.SendSoftwareEdgeTriggerRequest\x1a,.nirfsg_grpc.SendSoftwareEdgeTriggerResponse\x12\x8c\x01\n\x1fSetArbWaveformNextWritePosition\x12\x33.nirfsg_grpc.SetArbWaveformNextWritePositionRequest\x1a\x34.nirfsg_grpc.SetArbWaveformNextWritePositionResponse\x12n\n\x15SetAttributeViBoolean\x12).nirfsg_grpc.SetAttributeViBooleanRequest\x1a*.nirfsg_grpc.SetAttributeViBooleanResponse\x12h\n\x13SetAttributeViInt32\x12\'.nirfsg_grpc.SetAttributeViInt32Request\x1a(.nirfsg_grpc.SetAttributeViInt32Response\x12h\n\x13SetAttributeViInt64\x12\'.nirfsg_grpc.SetAttributeViInt64Request\x1a(.nirfsg_grpc.SetAttributeViInt64Response\x12k\n\x14SetAttributeViReal64\x12(.nirfsg_grpc.SetAttributeViReal64Request\x1a).nirfsg_grpc.SetAttributeViReal64Response\x12n\n\x15SetAttributeViSession\x12).nirfsg_grpc.SetAttributeViSessionRequest\x1a*.nirfsg_grpc.SetAttributeViSessionResponse\x12k\n\x14SetAttributeViString\x12(.nirfsg_grpc.SetAttributeViStringRequest\x1a).nirfsg_grpc.SetAttributeViStringResponse\x12P\n\x0bSetUserData\x12\x1f.nirfsg_grpc.SetUserDataRequest\x1a .nirfsg_grpc.SetUserDataResponse\x12\x89\x01\n\x1eSetWaveformBurstStartLocations\x12\x32.nirfsg_grpc.SetWaveformBurstStartLocationsRequest\x1a\x33.nirfsg_grpc.SetWaveformBurstStartLocationsResponse\x12\x86\x01\n\x1dSetWaveformBurstStopLocations\x12\x31.nirfsg_grpc.SetWaveformBurstStopLocationsRequest\x1a\x32.nirfsg_grpc.SetWaveformBurstStopLocationsResponse\x12\x8c\x01\n\x1fSetWaveformMarkerEventLocations\x12\x33.nirfsg_grpc.SetWaveformMarkerEventLocationsRequest\x1a\x34.nirfsg_grpc.SetWaveformMarkerEventLocationsResponse\x12_\n\x10WaitUntilSettled\x12$.nirfsg_grpc.WaitUntilSettledRequest\x1a%.nirfsg_grpc.WaitUntilSettledResponse\x12_\n\x10WriteArbWaveform\x12$.nirfsg_grpc.WriteArbWaveformRequest\x1a%.nirfsg_grpc.WriteArbWaveformResponse\x12}\n\x1aWriteArbWaveformComplexF32\x12..nirfsg_grpc.WriteArbWaveformComplexF32Request\x1a/.nirfsg_grpc.WriteArbWaveformComplexF32Response\x12}\n\x1aWriteArbWaveformComplexF64\x12..nirfsg_grpc.WriteArbWaveformComplexF64Request\x1a/.nirfsg_grpc.WriteArbWaveformComplexF64Response\x12}\n\x1aWriteArbWaveformComplexI16\x12..nirfsg_grpc.WriteArbWaveformComplexI16Request\x1a/.nirfsg_grpc.WriteArbWaveformComplexI16Response\x12h\n\x13WriteArbWaveformF32\x12\'.nirfsg_grpc.WriteArbWaveformF32Request\x1a(.nirfsg_grpc.WriteArbWaveformF32Response\x12P\n\x0bWriteScript\x12\x1f.nirfsg_grpc.WriteScriptRequest\x1a .nirfsg_grpc.WriteScriptResponseB@\n\x12\x63om.ni.grpc.nirfsgB\x06NiRFSGP\x01\xaa\x02\x1fNationalInstruments.Grpc.NiRFSGb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nirfsg_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022com.ni.grpc.nirfsgB\006NiRFSGP\001\252\002\037NationalInstruments.Grpc.NiRFSG'
  _NIRFSGINT32ATTRIBUTEVALUES._options = None
  _NIRFSGINT32ATTRIBUTEVALUES._serialized_options = b'\020\001'
  _INITRESPONSE.fields_by_name['error_message']._options = None
  _INITRESPONSE.fields_by_name['error_message']._serialized_options = b'\030\001'
  _INITWITHOPTIONSRESPONSE.fields_by_name['error_message']._options = None
  _INITWITHOPTIONSRESPONSE.fields_by_name['error_message']._serialized_options = b'\030\001'
  _globals['_NIRFSGATTRIBUTE']._serialized_start=22589
  _globals['_NIRFSGATTRIBUTE']._serialized_end=35098
  _globals['_DIGITALEDGECONFIGURATIONLISTSTEPTRIGGERSOURCE']._serialized_start=35101
  _globals['_DIGITALEDGECONFIGURATIONLISTSTEPTRIGGERSOURCE']._serialized_end=36485
  _globals['_DIGITALEDGEEDGE']._serialized_start=36487
  _globals['_DIGITALEDGEEDGE']._serialized_end=36575
  _globals['_DIGITALEDGESCRIPTTRIGGERIDENTIFIER']._serialized_start=36578
  _globals['_DIGITALEDGESCRIPTTRIGGERIDENTIFIER']._serialized_end=36910
  _globals['_DIGITALLEVELACTIVELEVEL']._serialized_start=36913
  _globals['_DIGITALLEVELACTIVELEVEL']._serialized_end=37071
  _globals['_GENERATIONMODE']._serialized_start=37074
  _globals['_GENERATIONMODE']._serialized_end=37212
  _globals['_LINEARINTERPOLATIONFORMAT']._serialized_start=37215
  _globals['_LINEARINTERPOLATIONFORMAT']._serialized_end=37454
  _globals['_MODULE']._serialized_start=37456
  _globals['_MODULE']._serialized_end=37549
  _globals['_OUTPUTSIGNAL']._serialized_start=37552
  _globals['_OUTPUTSIGNAL']._serialized_end=38040
  _globals['_PXICHASSISCLK10']._serialized_start=38043
  _globals['_PXICHASSISCLK10']._serialized_end=38190
  _globals['_POWERLEVELTYPE']._serialized_start=38192
  _globals['_POWERLEVELTYPE']._serialized_end=38313
  _globals['_REFCLOCKSOURCE']._serialized_start=38316
  _globals['_REFCLOCKSOURCE']._serialized_end=38558
  _globals['_RELATIVETO']._serialized_start=38560
  _globals['_RELATIVETO']._serialized_end=38672
  _globals['_RESETWITHOPTIONSSTEPSTOOMIT']._serialized_start=38675
  _globals['_RESETWITHOPTIONSSTEPSTOOMIT']._serialized_end=38943
  _globals['_ROUTEDSIGNAL']._serialized_start=38946
  _globals['_ROUTEDSIGNAL']._serialized_end=39249
  _globals['_SPARAMETERORIENTATION']._serialized_start=39252
  _globals['_SPARAMETERORIENTATION']._serialized_end=39414
  _globals['_SELFCALIBRATERANGESTEPSTOOMIT']._serialized_start=39417
  _globals['_SELFCALIBRATERANGESTEPSTOOMIT']._serialized_end=39789
  _globals['_SIGNALIDENTIFIER']._serialized_start=39792
  _globals['_SIGNALIDENTIFIER']._serialized_end=40153
  _globals['_TRIGGERSOURCE']._serialized_start=40156
  _globals['_TRIGGERSOURCE']._serialized_end=40940
  _globals['_NIRFSGINT32ATTRIBUTEVALUES']._serialized_start=40943
  _globals['_NIRFSGINT32ATTRIBUTEVALUES']._serialized_end=46196
  _globals['_NIRFSGREAL64ATTRIBUTEVALUES']._serialized_start=46199
  _globals['_NIRFSGREAL64ATTRIBUTEVALUES']._serialized_end=46351
  _globals['_NIRFSGSTRINGATTRIBUTEVALUESMAPPED']._serialized_start=46354
  _globals['_NIRFSGSTRINGATTRIBUTEVALUESMAPPED']._serialized_end=52578
  _globals['_ABORTREQUEST']._serialized_start=60
  _globals['_ABORTREQUEST']._serialized_end=110
  _globals['_ABORTRESPONSE']._serialized_start=112
  _globals['_ABORTRESPONSE']._serialized_end=143
  _globals['_ALLOCATEARBWAVEFORMREQUEST']._serialized_start=145
  _globals['_ALLOCATEARBWAVEFORMREQUEST']._serialized_end=257
  _globals['_ALLOCATEARBWAVEFORMRESPONSE']._serialized_start=259
  _globals['_ALLOCATEARBWAVEFORMRESPONSE']._serialized_end=304
  _globals['_CHECKATTRIBUTEVIBOOLEANREQUEST']._serialized_start=307
  _globals['_CHECKATTRIBUTEVIBOOLEANREQUEST']._serialized_end=464
  _globals['_CHECKATTRIBUTEVIBOOLEANRESPONSE']._serialized_start=466
  _globals['_CHECKATTRIBUTEVIBOOLEANRESPONSE']._serialized_end=515
  _globals['_CHECKATTRIBUTEVIINT32REQUEST']._serialized_start=518
  _globals['_CHECKATTRIBUTEVIINT32REQUEST']._serialized_end=751
  _globals['_CHECKATTRIBUTEVIINT32RESPONSE']._serialized_start=753
  _globals['_CHECKATTRIBUTEVIINT32RESPONSE']._serialized_end=800
  _globals['_CHECKATTRIBUTEVIINT64REQUEST']._serialized_start=803
  _globals['_CHECKATTRIBUTEVIINT64REQUEST']._serialized_end=962
  _globals['_CHECKATTRIBUTEVIINT64RESPONSE']._serialized_start=964
  _globals['_CHECKATTRIBUTEVIINT64RESPONSE']._serialized_end=1011
  _globals['_CHECKATTRIBUTEVIREAL64REQUEST']._serialized_start=1014
  _globals['_CHECKATTRIBUTEVIREAL64REQUEST']._serialized_end=1249
  _globals['_CHECKATTRIBUTEVIREAL64RESPONSE']._serialized_start=1251
  _globals['_CHECKATTRIBUTEVIREAL64RESPONSE']._serialized_end=1299
  _globals['_CHECKATTRIBUTEVISESSIONREQUEST']._serialized_start=1302
  _globals['_CHECKATTRIBUTEVISESSIONREQUEST']._serialized_end=1483
  _globals['_CHECKATTRIBUTEVISESSIONRESPONSE']._serialized_start=1485
  _globals['_CHECKATTRIBUTEVISESSIONRESPONSE']._serialized_end=1534
  _globals['_CHECKATTRIBUTEVISTRINGREQUEST']._serialized_start=1537
  _globals['_CHECKATTRIBUTEVISTRINGREQUEST']._serialized_end=1785
  _globals['_CHECKATTRIBUTEVISTRINGRESPONSE']._serialized_start=1787
  _globals['_CHECKATTRIBUTEVISTRINGRESPONSE']._serialized_end=1835
  _globals['_CHECKGENERATIONSTATUSREQUEST']._serialized_start=1837
  _globals['_CHECKGENERATIONSTATUSREQUEST']._serialized_end=1903
  _globals['_CHECKGENERATIONSTATUSRESPONSE']._serialized_start=1905
  _globals['_CHECKGENERATIONSTATUSRESPONSE']._serialized_end=1969
  _globals['_CHECKIFCONFIGURATIONLISTEXISTSREQUEST']._serialized_start=1971
  _globals['_CHECKIFCONFIGURATIONLISTEXISTSREQUEST']._serialized_end=2065
  _globals['_CHECKIFCONFIGURATIONLISTEXISTSRESPONSE']._serialized_start=2067
  _globals['_CHECKIFCONFIGURATIONLISTEXISTSRESPONSE']._serialized_end=2144
  _globals['_CHECKIFSCRIPTEXISTSREQUEST']._serialized_start=2146
  _globals['_CHECKIFSCRIPTEXISTSREQUEST']._serialized_end=2231
  _globals['_CHECKIFSCRIPTEXISTSRESPONSE']._serialized_start=2233
  _globals['_CHECKIFSCRIPTEXISTSRESPONSE']._serialized_end=2301
  _globals['_CHECKIFWAVEFORMEXISTSREQUEST']._serialized_start=2303
  _globals['_CHECKIFWAVEFORMEXISTSREQUEST']._serialized_end=2392
  _globals['_CHECKIFWAVEFORMEXISTSRESPONSE']._serialized_start=2394
  _globals['_CHECKIFWAVEFORMEXISTSRESPONSE']._serialized_end=2466
  _globals['_CLEARALLARBWAVEFORMSREQUEST']._serialized_start=2468
  _globals['_CLEARALLARBWAVEFORMSREQUEST']._serialized_end=2533
  _globals['_CLEARALLARBWAVEFORMSRESPONSE']._serialized_start=2535
  _globals['_CLEARALLARBWAVEFORMSRESPONSE']._serialized_end=2581
  _globals['_CLEARARBWAVEFORMREQUEST']._serialized_start=2583
  _globals['_CLEARARBWAVEFORMREQUEST']._serialized_end=2658
  _globals['_CLEARARBWAVEFORMRESPONSE']._serialized_start=2660
  _globals['_CLEARARBWAVEFORMRESPONSE']._serialized_end=2702
  _globals['_CLEARERRORREQUEST']._serialized_start=2704
  _globals['_CLEARERRORREQUEST']._serialized_end=2759
  _globals['_CLEARERRORRESPONSE']._serialized_start=2761
  _globals['_CLEARERRORRESPONSE']._serialized_end=2797
  _globals['_CLEARSELFCALIBRATERANGEREQUEST']._serialized_start=2799
  _globals['_CLEARSELFCALIBRATERANGEREQUEST']._serialized_end=2867
  _globals['_CLEARSELFCALIBRATERANGERESPONSE']._serialized_start=2869
  _globals['_CLEARSELFCALIBRATERANGERESPONSE']._serialized_end=2918
  _globals['_CLOSEREQUEST']._serialized_start=2920
  _globals['_CLOSEREQUEST']._serialized_end=2970
  _globals['_CLOSERESPONSE']._serialized_start=2972
  _globals['_CLOSERESPONSE']._serialized_end=3003
  _globals['_COMMITREQUEST']._serialized_start=3005
  _globals['_COMMITREQUEST']._serialized_end=3056
  _globals['_COMMITRESPONSE']._serialized_start=3058
  _globals['_COMMITRESPONSE']._serialized_end=3090
  _globals['_CONFIGUREDEEMBEDDINGTABLEINTERPOLATIONLINEARREQUEST']._serialized_start=3093
  _globals['_CONFIGUREDEEMBEDDINGTABLEINTERPOLATIONLINEARREQUEST']._serialized_end=3311
  _globals['_CONFIGUREDEEMBEDDINGTABLEINTERPOLATIONLINEARRESPONSE']._serialized_start=3313
  _globals['_CONFIGUREDEEMBEDDINGTABLEINTERPOLATIONLINEARRESPONSE']._serialized_end=3383
  _globals['_CONFIGUREDEEMBEDDINGTABLEINTERPOLATIONNEARESTREQUEST']._serialized_start=3385
  _globals['_CONFIGUREDEEMBEDDINGTABLEINTERPOLATIONNEARESTREQUEST']._serialized_end=3509
  _globals['_CONFIGUREDEEMBEDDINGTABLEINTERPOLATIONNEARESTRESPONSE']._serialized_start=3511
  _globals['_CONFIGUREDEEMBEDDINGTABLEINTERPOLATIONNEARESTRESPONSE']._serialized_end=3582
  _globals['_CONFIGUREDEEMBEDDINGTABLEINTERPOLATIONSPLINEREQUEST']._serialized_start=3584
  _globals['_CONFIGUREDEEMBEDDINGTABLEINTERPOLATIONSPLINEREQUEST']._serialized_end=3707
  _globals['_CONFIGUREDEEMBEDDINGTABLEINTERPOLATIONSPLINERESPONSE']._serialized_start=3709
  _globals['_CONFIGUREDEEMBEDDINGTABLEINTERPOLATIONSPLINERESPONSE']._serialized_end=3779
  _globals['_CONFIGUREDIGITALEDGECONFIGURATIONLISTSTEPTRIGGERREQUEST']._serialized_start=3782
  _globals['_CONFIGUREDIGITALEDGECONFIGURATIONLISTSTEPTRIGGERREQUEST']._serialized_end=4076
  _globals['_CONFIGUREDIGITALEDGECONFIGURATIONLISTSTEPTRIGGERRESPONSE']._serialized_start=4078
  _globals['_CONFIGUREDIGITALEDGECONFIGURATIONLISTSTEPTRIGGERRESPONSE']._serialized_end=4152
  _globals['_CONFIGUREDIGITALEDGESCRIPTTRIGGERREQUEST']._serialized_start=4155
  _globals['_CONFIGUREDIGITALEDGESCRIPTTRIGGERREQUEST']._serialized_end=4525
  _globals['_CONFIGUREDIGITALEDGESCRIPTTRIGGERRESPONSE']._serialized_start=4527
  _globals['_CONFIGUREDIGITALEDGESCRIPTTRIGGERRESPONSE']._serialized_end=4586
  _globals['_CONFIGUREDIGITALEDGESTARTTRIGGERREQUEST']._serialized_start=4589
  _globals['_CONFIGUREDIGITALEDGESTARTTRIGGERREQUEST']._serialized_end=4835
  _globals['_CONFIGUREDIGITALEDGESTARTTRIGGERRESPONSE']._serialized_start=4837
  _globals['_CONFIGUREDIGITALEDGESTARTTRIGGERRESPONSE']._serialized_end=4895
  _globals['_CONFIGUREDIGITALLEVELSCRIPTTRIGGERREQUEST']._serialized_start=4898
  _globals['_CONFIGUREDIGITALLEVELSCRIPTTRIGGERREQUEST']._serialized_end=5280
  _globals['_CONFIGUREDIGITALLEVELSCRIPTTRIGGERRESPONSE']._serialized_start=5282
  _globals['_CONFIGUREDIGITALLEVELSCRIPTTRIGGERRESPONSE']._serialized_end=5342
  _globals['_CONFIGUREDIGITALMODULATIONUSERDEFINEDWAVEFORMREQUEST']._serialized_start=5344
  _globals['_CONFIGUREDIGITALMODULATIONUSERDEFINEDWAVEFORMREQUEST']._serialized_end=5465
  _globals['_CONFIGUREDIGITALMODULATIONUSERDEFINEDWAVEFORMRESPONSE']._serialized_start=5467
  _globals['_CONFIGUREDIGITALMODULATIONUSERDEFINEDWAVEFORMRESPONSE']._serialized_end=5538
  _globals['_CONFIGUREGENERATIONMODEREQUEST']._serialized_start=5541
  _globals['_CONFIGUREGENERATIONMODEREQUEST']._serialized_end=5720
  _globals['_CONFIGUREGENERATIONMODERESPONSE']._serialized_start=5722
  _globals['_CONFIGUREGENERATIONMODERESPONSE']._serialized_end=5771
  _globals['_CONFIGUREOUTPUTENABLEDREQUEST']._serialized_start=5773
  _globals['_CONFIGUREOUTPUTENABLEDREQUEST']._serialized_end=5864
  _globals['_CONFIGUREOUTPUTENABLEDRESPONSE']._serialized_start=5866
  _globals['_CONFIGUREOUTPUTENABLEDRESPONSE']._serialized_end=5914
  _globals['_CONFIGUREP2PENDPOINTFULLNESSSTARTTRIGGERREQUEST']._serialized_start=5916
  _globals['_CONFIGUREP2PENDPOINTFULLNESSSTARTTRIGGERREQUEST']._serialized_end=6038
  _globals['_CONFIGUREP2PENDPOINTFULLNESSSTARTTRIGGERRESPONSE']._serialized_start=6040
  _globals['_CONFIGUREP2PENDPOINTFULLNESSSTARTTRIGGERRESPONSE']._serialized_end=6106
  _globals['_CONFIGUREPXICHASSISCLK10REQUEST']._serialized_start=6109
  _globals['_CONFIGUREPXICHASSISCLK10REQUEST']._serialized_end=6300
  _globals['_CONFIGUREPXICHASSISCLK10RESPONSE']._serialized_start=6302
  _globals['_CONFIGUREPXICHASSISCLK10RESPONSE']._serialized_end=6352
  _globals['_CONFIGUREPOWERLEVELTYPEREQUEST']._serialized_start=6355
  _globals['_CONFIGUREPOWERLEVELTYPEREQUEST']._serialized_end=6537
  _globals['_CONFIGUREPOWERLEVELTYPERESPONSE']._serialized_start=6539
  _globals['_CONFIGUREPOWERLEVELTYPERESPONSE']._serialized_end=6588
  _globals['_CONFIGURERFREQUEST']._serialized_start=6590
  _globals['_CONFIGURERFREQUEST']._serialized_end=6686
  _globals['_CONFIGURERFRESPONSE']._serialized_start=6688
  _globals['_CONFIGURERFRESPONSE']._serialized_end=6725
  _globals['_CONFIGUREREFCLOCKREQUEST']._serialized_start=6728
  _globals['_CONFIGUREREFCLOCKREQUEST']._serialized_end=6935
  _globals['_CONFIGUREREFCLOCKRESPONSE']._serialized_start=6937
  _globals['_CONFIGUREREFCLOCKRESPONSE']._serialized_end=6980
  _globals['_CONFIGURESIGNALBANDWIDTHREQUEST']._serialized_start=6982
  _globals['_CONFIGURESIGNALBANDWIDTHREQUEST']._serialized_end=7077
  _globals['_CONFIGURESIGNALBANDWIDTHRESPONSE']._serialized_start=7079
  _globals['_CONFIGURESIGNALBANDWIDTHRESPONSE']._serialized_end=7129
  _globals['_CONFIGURESOFTWARESCRIPTTRIGGERREQUEST']._serialized_start=7132
  _globals['_CONFIGURESOFTWARESCRIPTTRIGGERREQUEST']._serialized_end=7330
  _globals['_CONFIGURESOFTWARESCRIPTTRIGGERRESPONSE']._serialized_start=7332
  _globals['_CONFIGURESOFTWARESCRIPTTRIGGERRESPONSE']._serialized_end=7388
  _globals['_CONFIGURESOFTWARESTARTTRIGGERREQUEST']._serialized_start=7390
  _globals['_CONFIGURESOFTWARESTARTTRIGGERREQUEST']._serialized_end=7464
  _globals['_CONFIGURESOFTWARESTARTTRIGGERRESPONSE']._serialized_start=7466
  _globals['_CONFIGURESOFTWARESTARTTRIGGERRESPONSE']._serialized_end=7521
  _globals['_CONFIGUREUPCONVERTERPLLSETTLINGTIMEREQUEST']._serialized_start=7524
  _globals['_CONFIGUREUPCONVERTERPLLSETTLINGTIMEREQUEST']._serialized_end=7658
  _globals['_CONFIGUREUPCONVERTERPLLSETTLINGTIMERESPONSE']._serialized_start=7660
  _globals['_CONFIGUREUPCONVERTERPLLSETTLINGTIMERESPONSE']._serialized_end=7721
  _globals['_CREATECONFIGURATIONLISTREQUEST']._serialized_start=7724
  _globals['_CREATECONFIGURATIONLISTREQUEST']._serialized_end=7908
  _globals['_CREATECONFIGURATIONLISTRESPONSE']._serialized_start=7910
  _globals['_CREATECONFIGURATIONLISTRESPONSE']._serialized_end=7959
  _globals['_CREATECONFIGURATIONLISTSTEPREQUEST']._serialized_start=7961
  _globals['_CREATECONFIGURATIONLISTSTEPREQUEST']._serialized_end=8061
  _globals['_CREATECONFIGURATIONLISTSTEPRESPONSE']._serialized_start=8063
  _globals['_CREATECONFIGURATIONLISTSTEPRESPONSE']._serialized_end=8116
  _globals['_CREATEDEEMBEDDINGSPARAMETERTABLEARRAYREQUEST']._serialized_start=8119
  _globals['_CREATEDEEMBEDDINGSPARAMETERTABLEARRAYREQUEST']._serialized_end=8478
  _globals['_CREATEDEEMBEDDINGSPARAMETERTABLEARRAYRESPONSE']._serialized_start=8480
  _globals['_CREATEDEEMBEDDINGSPARAMETERTABLEARRAYRESPONSE']._serialized_end=8543
  _globals['_CREATEDEEMBEDDINGSPARAMETERTABLES2PFILEREQUEST']._serialized_start=8546
  _globals['_CREATEDEEMBEDDINGSPARAMETERTABLES2PFILEREQUEST']._serialized_end=8826
  _globals['_CREATEDEEMBEDDINGSPARAMETERTABLES2PFILERESPONSE']._serialized_start=8828
  _globals['_CREATEDEEMBEDDINGSPARAMETERTABLES2PFILERESPONSE']._serialized_end=8893
  _globals['_DELETEALLDEEMBEDDINGTABLESREQUEST']._serialized_start=8895
  _globals['_DELETEALLDEEMBEDDINGTABLESREQUEST']._serialized_end=8966
  _globals['_DELETEALLDEEMBEDDINGTABLESRESPONSE']._serialized_start=8968
  _globals['_DELETEALLDEEMBEDDINGTABLESRESPONSE']._serialized_end=9020
  _globals['_DELETECONFIGURATIONLISTREQUEST']._serialized_start=9022
  _globals['_DELETECONFIGURATIONLISTREQUEST']._serialized_end=9109
  _globals['_DELETECONFIGURATIONLISTRESPONSE']._serialized_start=9111
  _globals['_DELETECONFIGURATIONLISTRESPONSE']._serialized_end=9160
  _globals['_DELETEDEEMBEDDINGTABLEREQUEST']._serialized_start=9162
  _globals['_DELETEDEEMBEDDINGTABLEREQUEST']._serialized_end=9263
  _globals['_DELETEDEEMBEDDINGTABLERESPONSE']._serialized_start=9265
  _globals['_DELETEDEEMBEDDINGTABLERESPONSE']._serialized_end=9313
  _globals['_DELETESCRIPTREQUEST']._serialized_start=9315
  _globals['_DELETESCRIPTREQUEST']._serialized_end=9393
  _globals['_DELETESCRIPTRESPONSE']._serialized_start=9395
  _globals['_DELETESCRIPTRESPONSE']._serialized_end=9433
  _globals['_DISABLEREQUEST']._serialized_start=9435
  _globals['_DISABLEREQUEST']._serialized_end=9487
  _globals['_DISABLERESPONSE']._serialized_start=9489
  _globals['_DISABLERESPONSE']._serialized_end=9522
  _globals['_DISABLEALLMODULATIONREQUEST']._serialized_start=9524
  _globals['_DISABLEALLMODULATIONREQUEST']._serialized_end=9589
  _globals['_DISABLEALLMODULATIONRESPONSE']._serialized_start=9591
  _globals['_DISABLEALLMODULATIONRESPONSE']._serialized_end=9637
  _globals['_DISABLECONFIGURATIONLISTSTEPTRIGGERREQUEST']._serialized_start=9639
  _globals['_DISABLECONFIGURATIONLISTSTEPTRIGGERREQUEST']._serialized_end=9719
  _globals['_DISABLECONFIGURATIONLISTSTEPTRIGGERRESPONSE']._serialized_start=9721
  _globals['_DISABLECONFIGURATIONLISTSTEPTRIGGERRESPONSE']._serialized_end=9782
  _globals['_DISABLESCRIPTTRIGGERREQUEST']._serialized_start=9785
  _globals['_DISABLESCRIPTTRIGGERREQUEST']._serialized_end=9973
  _globals['_DISABLESCRIPTTRIGGERRESPONSE']._serialized_start=9975
  _globals['_DISABLESCRIPTTRIGGERRESPONSE']._serialized_end=10021
  _globals['_DISABLESTARTTRIGGERREQUEST']._serialized_start=10023
  _globals['_DISABLESTARTTRIGGERREQUEST']._serialized_end=10087
  _globals['_DISABLESTARTTRIGGERRESPONSE']._serialized_start=10089
  _globals['_DISABLESTARTTRIGGERRESPONSE']._serialized_end=10134
  _globals['_ERRORMESSAGEREQUEST']._serialized_start=10136
  _globals['_ERRORMESSAGEREQUEST']._serialized_end=10213
  _globals['_ERRORMESSAGERESPONSE']._serialized_start=10215
  _globals['_ERRORMESSAGERESPONSE']._serialized_end=10276
  _globals['_ERRORQUERYREQUEST']._serialized_start=10278
  _globals['_ERRORQUERYREQUEST']._serialized_end=10333
  _globals['_ERRORQUERYRESPONSE']._serialized_start=10335
  _globals['_ERRORQUERYRESPONSE']._serialized_end=10414
  _globals['_EXPORTSIGNALREQUEST']._serialized_start=10417
  _globals['_EXPORTSIGNALREQUEST']._serialized_end=10798
  _globals['_EXPORTSIGNALRESPONSE']._serialized_start=10800
  _globals['_EXPORTSIGNALRESPONSE']._serialized_end=10838
  _globals['_GETALLNAMEDWAVEFORMNAMESREQUEST']._serialized_start=10840
  _globals['_GETALLNAMEDWAVEFORMNAMESREQUEST']._serialized_end=10909
  _globals['_GETALLNAMEDWAVEFORMNAMESRESPONSE']._serialized_start=10911
  _globals['_GETALLNAMEDWAVEFORMNAMESRESPONSE']._serialized_end=11013
  _globals['_GETALLSCRIPTNAMESREQUEST']._serialized_start=11015
  _globals['_GETALLSCRIPTNAMESREQUEST']._serialized_end=11077
  _globals['_GETALLSCRIPTNAMESRESPONSE']._serialized_start=11079
  _globals['_GETALLSCRIPTNAMESRESPONSE']._serialized_end=11172
  _globals['_GETSCRIPTREQUEST']._serialized_start=11174
  _globals['_GETSCRIPTREQUEST']._serialized_end=11249
  _globals['_GETSCRIPTRESPONSE']._serialized_start=11251
  _globals['_GETSCRIPTRESPONSE']._serialized_end=11330
  _globals['_GETATTRIBUTEVIBOOLEANREQUEST']._serialized_start=11333
  _globals['_GETATTRIBUTEVIBOOLEANREQUEST']._serialized_end=11473
  _globals['_GETATTRIBUTEVIBOOLEANRESPONSE']._serialized_start=11475
  _globals['_GETATTRIBUTEVIBOOLEANRESPONSE']._serialized_end=11537
  _globals['_GETATTRIBUTEVIINT32REQUEST']._serialized_start=11540
  _globals['_GETATTRIBUTEVIINT32REQUEST']._serialized_end=11678
  _globals['_GETATTRIBUTEVIINT32RESPONSE']._serialized_start=11680
  _globals['_GETATTRIBUTEVIINT32RESPONSE']._serialized_end=11740
  _globals['_GETATTRIBUTEVIINT64REQUEST']._serialized_start=11743
  _globals['_GETATTRIBUTEVIINT64REQUEST']._serialized_end=11881
  _globals['_GETATTRIBUTEVIINT64RESPONSE']._serialized_start=11883
  _globals['_GETATTRIBUTEVIINT64RESPONSE']._serialized_end=11943
  _globals['_GETATTRIBUTEVIREAL64REQUEST']._serialized_start=11946
  _globals['_GETATTRIBUTEVIREAL64REQUEST']._serialized_end=12085
  _globals['_GETATTRIBUTEVIREAL64RESPONSE']._serialized_start=12087
  _globals['_GETATTRIBUTEVIREAL64RESPONSE']._serialized_end=12148
  _globals['_GETATTRIBUTEVISESSIONREQUEST']._serialized_start=12151
  _globals['_GETATTRIBUTEVISESSIONREQUEST']._serialized_end=12291
  _globals['_GETATTRIBUTEVISESSIONRESPONSE']._serialized_start=12293
  _globals['_GETATTRIBUTEVISESSIONRESPONSE']._serialized_end=12379
  _globals['_GETATTRIBUTEVISTRINGREQUEST']._serialized_start=12382
  _globals['_GETATTRIBUTEVISTRINGREQUEST']._serialized_end=12521
  _globals['_GETATTRIBUTEVISTRINGRESPONSE']._serialized_start=12523
  _globals['_GETATTRIBUTEVISTRINGRESPONSE']._serialized_end=12584
  _globals['_GETCHANNELNAMEREQUEST']._serialized_start=12586
  _globals['_GETCHANNELNAMEREQUEST']._serialized_end=12660
  _globals['_GETCHANNELNAMERESPONSE']._serialized_start=12662
  _globals['_GETCHANNELNAMERESPONSE']._serialized_end=12716
  _globals['_GETDEEMBEDDINGSPARAMETERSREQUEST']._serialized_start=12718
  _globals['_GETDEEMBEDDINGSPARAMETERSREQUEST']._serialized_end=12788
  _globals['_GETDEEMBEDDINGSPARAMETERSRESPONSE']._serialized_start=12791
  _globals['_GETDEEMBEDDINGSPARAMETERSRESPONSE']._serialized_end=12951
  _globals['_GETERRORREQUEST']._serialized_start=12953
  _globals['_GETERRORREQUEST']._serialized_end=13006
  _globals['_GETERRORRESPONSE']._serialized_start=13008
  _globals['_GETERRORRESPONSE']._serialized_end=13089
  _globals['_GETEXTERNALCALIBRATIONLASTDATEANDTIMEREQUEST']._serialized_start=13091
  _globals['_GETEXTERNALCALIBRATIONLASTDATEANDTIMEREQUEST']._serialized_end=13173
  _globals['_GETEXTERNALCALIBRATIONLASTDATEANDTIMERESPONSE']._serialized_start=13176
  _globals['_GETEXTERNALCALIBRATIONLASTDATEANDTIMERESPONSE']._serialized_end=13327
  _globals['_GETMAXSETTABLEPOWERREQUEST']._serialized_start=13329
  _globals['_GETMAXSETTABLEPOWERREQUEST']._serialized_end=13393
  _globals['_GETMAXSETTABLEPOWERRESPONSE']._serialized_start=13395
  _globals['_GETMAXSETTABLEPOWERRESPONSE']._serialized_end=13455
  _globals['_GETSELFCALIBRATIONDATEANDTIMEREQUEST']._serialized_start=13458
  _globals['_GETSELFCALIBRATIONDATEANDTIMEREQUEST']._serialized_end=13608
  _globals['_GETSELFCALIBRATIONDATEANDTIMERESPONSE']._serialized_start=13611
  _globals['_GETSELFCALIBRATIONDATEANDTIMERESPONSE']._serialized_end=13754
  _globals['_GETSELFCALIBRATIONTEMPERATUREREQUEST']._serialized_start=13757
  _globals['_GETSELFCALIBRATIONTEMPERATUREREQUEST']._serialized_end=13907
  _globals['_GETSELFCALIBRATIONTEMPERATURERESPONSE']._serialized_start=13909
  _globals['_GETSELFCALIBRATIONTEMPERATURERESPONSE']._serialized_end=13985
  _globals['_GETTERMINALNAMEREQUEST']._serialized_start=13988
  _globals['_GETTERMINALNAMEREQUEST']._serialized_end=14256
  _globals['_GETTERMINALNAMERESPONSE']._serialized_start=14258
  _globals['_GETTERMINALNAMERESPONSE']._serialized_end=14322
  _globals['_GETUSERDATAREQUEST']._serialized_start=14324
  _globals['_GETUSERDATAREQUEST']._serialized_end=14400
  _globals['_GETUSERDATARESPONSE']._serialized_start=14402
  _globals['_GETUSERDATARESPONSE']._serialized_end=14479
  _globals['_GETWAVEFORMBURSTSTARTLOCATIONSREQUEST']._serialized_start=14481
  _globals['_GETWAVEFORMBURSTSTARTLOCATIONSREQUEST']._serialized_end=14578
  _globals['_GETWAVEFORMBURSTSTARTLOCATIONSRESPONSE']._serialized_start=14580
  _globals['_GETWAVEFORMBURSTSTARTLOCATIONSRESPONSE']._serialized_end=14678
  _globals['_GETWAVEFORMBURSTSTOPLOCATIONSREQUEST']._serialized_start=14680
  _globals['_GETWAVEFORMBURSTSTOPLOCATIONSREQUEST']._serialized_end=14776
  _globals['_GETWAVEFORMBURSTSTOPLOCATIONSRESPONSE']._serialized_start=14778
  _globals['_GETWAVEFORMBURSTSTOPLOCATIONSRESPONSE']._serialized_end=14875
  _globals['_GETWAVEFORMMARKEREVENTLOCATIONSREQUEST']._serialized_start=14877
  _globals['_GETWAVEFORMMARKEREVENTLOCATIONSREQUEST']._serialized_end=14975
  _globals['_GETWAVEFORMMARKEREVENTLOCATIONSRESPONSE']._serialized_start=14977
  _globals['_GETWAVEFORMMARKEREVENTLOCATIONSRESPONSE']._serialized_end=15076
  _globals['_INITREQUEST']._serialized_start=15079
  _globals['_INITREQUEST']._serialized_end=15256
  _globals['_INITRESPONSE']._serialized_start=15259
  _globals['_INITRESPONSE']._serialized_end=15389
  _globals['_INITWITHOPTIONSREQUEST']._serialized_start=15392
  _globals['_INITWITHOPTIONSREQUEST']._serialized_end=15603
  _globals['_INITWITHOPTIONSRESPONSE']._serialized_start=15606
  _globals['_INITWITHOPTIONSRESPONSE']._serialized_end=15743
  _globals['_INITIATEREQUEST']._serialized_start=15745
  _globals['_INITIATEREQUEST']._serialized_end=15798
  _globals['_INITIATERESPONSE']._serialized_start=15800
  _globals['_INITIATERESPONSE']._serialized_end=15834
  _globals['_INVALIDATEALLATTRIBUTESREQUEST']._serialized_start=15836
  _globals['_INVALIDATEALLATTRIBUTESREQUEST']._serialized_end=15904
  _globals['_INVALIDATEALLATTRIBUTESRESPONSE']._serialized_start=15906
  _globals['_INVALIDATEALLATTRIBUTESRESPONSE']._serialized_end=15955
  _globals['_LOADCONFIGURATIONSFROMFILEREQUEST']._serialized_start=15957
  _globals['_LOADCONFIGURATIONSFROMFILEREQUEST']._serialized_end=16069
  _globals['_LOADCONFIGURATIONSFROMFILERESPONSE']._serialized_start=16071
  _globals['_LOADCONFIGURATIONSFROMFILERESPONSE']._serialized_end=16123
  _globals['_PERFORMPOWERSEARCHREQUEST']._serialized_start=16125
  _globals['_PERFORMPOWERSEARCHREQUEST']._serialized_end=16188
  _globals['_PERFORMPOWERSEARCHRESPONSE']._serialized_start=16190
  _globals['_PERFORMPOWERSEARCHRESPONSE']._serialized_end=16234
  _globals['_PERFORMTHERMALCORRECTIONREQUEST']._serialized_start=16236
  _globals['_PERFORMTHERMALCORRECTIONREQUEST']._serialized_end=16305
  _globals['_PERFORMTHERMALCORRECTIONRESPONSE']._serialized_start=16307
  _globals['_PERFORMTHERMALCORRECTIONRESPONSE']._serialized_end=16357
  _globals['_QUERYARBWAVEFORMCAPABILITIESREQUEST']._serialized_start=16359
  _globals['_QUERYARBWAVEFORMCAPABILITIESREQUEST']._serialized_end=16432
  _globals['_QUERYARBWAVEFORMCAPABILITIESRESPONSE']._serialized_start=16435
  _globals['_QUERYARBWAVEFORMCAPABILITIESRESPONSE']._serialized_end=16599
  _globals['_READANDDOWNLOADWAVEFORMFROMFILETDMSREQUEST']._serialized_start=16602
  _globals['_READANDDOWNLOADWAVEFORMFROMFILETDMSREQUEST']._serialized_end=16748
  _globals['_READANDDOWNLOADWAVEFORMFROMFILETDMSRESPONSE']._serialized_start=16750
  _globals['_READANDDOWNLOADWAVEFORMFROMFILETDMSRESPONSE']._serialized_end=16811
  _globals['_RESETREQUEST']._serialized_start=16813
  _globals['_RESETREQUEST']._serialized_end=16863
  _globals['_RESETRESPONSE']._serialized_start=16865
  _globals['_RESETRESPONSE']._serialized_end=16896
  _globals['_RESETATTRIBUTEREQUEST']._serialized_start=16899
  _globals['_RESETATTRIBUTEREQUEST']._serialized_end=17032
  _globals['_RESETATTRIBUTERESPONSE']._serialized_start=17034
  _globals['_RESETATTRIBUTERESPONSE']._serialized_end=17074
  _globals['_RESETDEVICEREQUEST']._serialized_start=17076
  _globals['_RESETDEVICEREQUEST']._serialized_end=17132
  _globals['_RESETDEVICERESPONSE']._serialized_start=17134
  _globals['_RESETDEVICERESPONSE']._serialized_end=17171
  _globals['_RESETWITHDEFAULTSREQUEST']._serialized_start=17173
  _globals['_RESETWITHDEFAULTSREQUEST']._serialized_end=17235
  _globals['_RESETWITHDEFAULTSRESPONSE']._serialized_start=17237
  _globals['_RESETWITHDEFAULTSRESPONSE']._serialized_end=17280
  _globals['_RESETWITHOPTIONSREQUEST']._serialized_start=17283
  _globals['_RESETWITHOPTIONSREQUEST']._serialized_end=17462
  _globals['_RESETWITHOPTIONSRESPONSE']._serialized_start=17464
  _globals['_RESETWITHOPTIONSRESPONSE']._serialized_end=17506
  _globals['_REVISIONQUERYREQUEST']._serialized_start=17508
  _globals['_REVISIONQUERYREQUEST']._serialized_end=17566
  _globals['_REVISIONQUERYRESPONSE']._serialized_start=17568
  _globals['_REVISIONQUERYRESPONSE']._serialized_end=17670
  _globals['_SAVECONFIGURATIONSTOFILEREQUEST']._serialized_start=17672
  _globals['_SAVECONFIGURATIONSTOFILEREQUEST']._serialized_end=17782
  _globals['_SAVECONFIGURATIONSTOFILERESPONSE']._serialized_start=17784
  _globals['_SAVECONFIGURATIONSTOFILERESPONSE']._serialized_end=17834
  _globals['_SELECTARBWAVEFORMREQUEST']._serialized_start=17836
  _globals['_SELECTARBWAVEFORMREQUEST']._serialized_end=17912
  _globals['_SELECTARBWAVEFORMRESPONSE']._serialized_start=17914
  _globals['_SELECTARBWAVEFORMRESPONSE']._serialized_end=17957
  _globals['_SELFCALREQUEST']._serialized_start=17959
  _globals['_SELFCALREQUEST']._serialized_end=18011
  _globals['_SELFCALRESPONSE']._serialized_start=18013
  _globals['_SELFCALRESPONSE']._serialized_end=18046
  _globals['_SELFCALIBRATERANGEREQUEST']._serialized_start=18049
  _globals['_SELFCALIBRATERANGEREQUEST']._serialized_end=18328
  _globals['_SELFCALIBRATERANGERESPONSE']._serialized_start=18330
  _globals['_SELFCALIBRATERANGERESPONSE']._serialized_end=18374
  _globals['_SELFTESTREQUEST']._serialized_start=18376
  _globals['_SELFTESTREQUEST']._serialized_end=18429
  _globals['_SELFTESTRESPONSE']._serialized_start=18431
  _globals['_SELFTESTRESPONSE']._serialized_end=18518
  _globals['_SENDSOFTWAREEDGETRIGGERREQUEST']._serialized_start=18521
  _globals['_SENDSOFTWAREEDGETRIGGERREQUEST']._serialized_end=18803
  _globals['_SENDSOFTWAREEDGETRIGGERRESPONSE']._serialized_start=18805
  _globals['_SENDSOFTWAREEDGETRIGGERRESPONSE']._serialized_end=18854
  _globals['_SETARBWAVEFORMNEXTWRITEPOSITIONREQUEST']._serialized_start=18857
  _globals['_SETARBWAVEFORMNEXTWRITEPOSITIONREQUEST']._serialized_end=19067
  _globals['_SETARBWAVEFORMNEXTWRITEPOSITIONRESPONSE']._serialized_start=19069
  _globals['_SETARBWAVEFORMNEXTWRITEPOSITIONRESPONSE']._serialized_end=19126
  _globals['_SETATTRIBUTEVIBOOLEANREQUEST']._serialized_start=19129
  _globals['_SETATTRIBUTEVIBOOLEANREQUEST']._serialized_end=19284
  _globals['_SETATTRIBUTEVIBOOLEANRESPONSE']._serialized_start=19286
  _globals['_SETATTRIBUTEVIBOOLEANRESPONSE']._serialized_end=19333
  _globals['_SETATTRIBUTEVIINT32REQUEST']._serialized_start=19336
  _globals['_SETATTRIBUTEVIINT32REQUEST']._serialized_end=19567
  _globals['_SETATTRIBUTEVIINT32RESPONSE']._serialized_start=19569
  _globals['_SETATTRIBUTEVIINT32RESPONSE']._serialized_end=19614
  _globals['_SETATTRIBUTEVIINT64REQUEST']._serialized_start=19617
  _globals['_SETATTRIBUTEVIINT64REQUEST']._serialized_end=19774
  _globals['_SETATTRIBUTEVIINT64RESPONSE']._serialized_start=19776
  _globals['_SETATTRIBUTEVIINT64RESPONSE']._serialized_end=19821
  _globals['_SETATTRIBUTEVIREAL64REQUEST']._serialized_start=19824
  _globals['_SETATTRIBUTEVIREAL64REQUEST']._serialized_end=20057
  _globals['_SETATTRIBUTEVIREAL64RESPONSE']._serialized_start=20059
  _globals['_SETATTRIBUTEVIREAL64RESPONSE']._serialized_end=20105
  _globals['_SETATTRIBUTEVISESSIONREQUEST']._serialized_start=20108
  _globals['_SETATTRIBUTEVISESSIONREQUEST']._serialized_end=20287
  _globals['_SETATTRIBUTEVISESSIONRESPONSE']._serialized_start=20289
  _globals['_SETATTRIBUTEVISESSIONRESPONSE']._serialized_end=20336
  _globals['_SETATTRIBUTEVISTRINGREQUEST']._serialized_start=20339
  _globals['_SETATTRIBUTEVISTRINGREQUEST']._serialized_end=20585
  _globals['_SETATTRIBUTEVISTRINGRESPONSE']._serialized_start=20587
  _globals['_SETATTRIBUTEVISTRINGRESPONSE']._serialized_end=20633
  _globals['_SETUSERDATAREQUEST']._serialized_start=20635
  _globals['_SETUSERDATAREQUEST']._serialized_end=20725
  _globals['_SETUSERDATARESPONSE']._serialized_start=20727
  _globals['_SETUSERDATARESPONSE']._serialized_end=20764
  _globals['_SETWAVEFORMBURSTSTARTLOCATIONSREQUEST']._serialized_start=20766
  _globals['_SETWAVEFORMBURSTSTARTLOCATIONSREQUEST']._serialized_end=20882
  _globals['_SETWAVEFORMBURSTSTARTLOCATIONSRESPONSE']._serialized_start=20884
  _globals['_SETWAVEFORMBURSTSTARTLOCATIONSRESPONSE']._serialized_end=20940
  _globals['_SETWAVEFORMBURSTSTOPLOCATIONSREQUEST']._serialized_start=20942
  _globals['_SETWAVEFORMBURSTSTOPLOCATIONSREQUEST']._serialized_end=21057
  _globals['_SETWAVEFORMBURSTSTOPLOCATIONSRESPONSE']._serialized_start=21059
  _globals['_SETWAVEFORMBURSTSTOPLOCATIONSRESPONSE']._serialized_end=21114
  _globals['_SETWAVEFORMMARKEREVENTLOCATIONSREQUEST']._serialized_start=21116
  _globals['_SETWAVEFORMMARKEREVENTLOCATIONSREQUEST']._serialized_end=21233
  _globals['_SETWAVEFORMMARKEREVENTLOCATIONSRESPONSE']._serialized_start=21235
  _globals['_SETWAVEFORMMARKEREVENTLOCATIONSRESPONSE']._serialized_end=21292
  _globals['_WAITUNTILSETTLEDREQUEST']._serialized_start=21294
  _globals['_WAITUNTILSETTLEDREQUEST']._serialized_end=21386
  _globals['_WAITUNTILSETTLEDRESPONSE']._serialized_start=21388
  _globals['_WAITUNTILSETTLEDRESPONSE']._serialized_end=21430
  _globals['_WRITEARBWAVEFORMREQUEST']._serialized_start=21433
  _globals['_WRITEARBWAVEFORMREQUEST']._serialized_end=21576
  _globals['_WRITEARBWAVEFORMRESPONSE']._serialized_start=21578
  _globals['_WRITEARBWAVEFORMRESPONSE']._serialized_end=21620
  _globals['_WRITEARBWAVEFORMCOMPLEXF32REQUEST']._serialized_start=21623
  _globals['_WRITEARBWAVEFORMCOMPLEXF32REQUEST']._serialized_end=21797
  _globals['_WRITEARBWAVEFORMCOMPLEXF32RESPONSE']._serialized_start=21799
  _globals['_WRITEARBWAVEFORMCOMPLEXF32RESPONSE']._serialized_end=21851
  _globals['_WRITEARBWAVEFORMCOMPLEXF64REQUEST']._serialized_start=21854
  _globals['_WRITEARBWAVEFORMCOMPLEXF64REQUEST']._serialized_end=22025
  _globals['_WRITEARBWAVEFORMCOMPLEXF64RESPONSE']._serialized_start=22027
  _globals['_WRITEARBWAVEFORMCOMPLEXF64RESPONSE']._serialized_end=22079
  _globals['_WRITEARBWAVEFORMCOMPLEXI16REQUEST']._serialized_start=22082
  _globals['_WRITEARBWAVEFORMCOMPLEXI16REQUEST']._serialized_end=22223
  _globals['_WRITEARBWAVEFORMCOMPLEXI16RESPONSE']._serialized_start=22225
  _globals['_WRITEARBWAVEFORMCOMPLEXI16RESPONSE']._serialized_end=22277
  _globals['_WRITEARBWAVEFORMF32REQUEST']._serialized_start=22280
  _globals['_WRITEARBWAVEFORMF32REQUEST']._serialized_end=22426
  _globals['_WRITEARBWAVEFORMF32RESPONSE']._serialized_start=22428
  _globals['_WRITEARBWAVEFORMF32RESPONSE']._serialized_end=22473
  _globals['_WRITESCRIPTREQUEST']._serialized_start=22475
  _globals['_WRITESCRIPTREQUEST']._serialized_end=22547
  _globals['_WRITESCRIPTRESPONSE']._serialized_start=22549
  _globals['_WRITESCRIPTRESPONSE']._serialized_end=22586
  _globals['_NIRFSG']._serialized_start=52581
  _globals['_NIRFSG']._serialized_end=65556
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nirfsg/nirfsg/nirfsg_pb2_grpc.py sha256=c5c2697d89b1847af970d4ad36b041f85e521ae91126c85354cbf73cce4c93ec bytes=189035 -->
## FILE: generated/nirfsg/nirfsg/nirfsg_pb2_grpc.py

- repository: `ni/nimi-python`
- source_path: `generated/nirfsg/nirfsg/nirfsg_pb2_grpc.py`
- sha256: `c5c2697d89b1847af970d4ad36b041f85e521ae91126c85354cbf73cce4c93ec`
- bytes: 189035

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import nirfsg_pb2 as nirfsg__pb2


class NiRFSGStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Abort = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/Abort',
                request_serializer=nirfsg__pb2.AbortRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.AbortResponse.FromString,
                )
        self.AllocateArbWaveform = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/AllocateArbWaveform',
                request_serializer=nirfsg__pb2.AllocateArbWaveformRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.AllocateArbWaveformResponse.FromString,
                )
        self.CheckAttributeViBoolean = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/CheckAttributeViBoolean',
                request_serializer=nirfsg__pb2.CheckAttributeViBooleanRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.CheckAttributeViBooleanResponse.FromString,
                )
        self.CheckAttributeViInt32 = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/CheckAttributeViInt32',
                request_serializer=nirfsg__pb2.CheckAttributeViInt32Request.SerializeToString,
                response_deserializer=nirfsg__pb2.CheckAttributeViInt32Response.FromString,
                )
        self.CheckAttributeViInt64 = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/CheckAttributeViInt64',
                request_serializer=nirfsg__pb2.CheckAttributeViInt64Request.SerializeToString,
                response_deserializer=nirfsg__pb2.CheckAttributeViInt64Response.FromString,
                )
        self.CheckAttributeViReal64 = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/CheckAttributeViReal64',
                request_serializer=nirfsg__pb2.CheckAttributeViReal64Request.SerializeToString,
                response_deserializer=nirfsg__pb2.CheckAttributeViReal64Response.FromString,
                )
        self.CheckAttributeViSession = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/CheckAttributeViSession',
                request_serializer=nirfsg__pb2.CheckAttributeViSessionRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.CheckAttributeViSessionResponse.FromString,
                )
        self.CheckAttributeViString = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/CheckAttributeViString',
                request_serializer=nirfsg__pb2.CheckAttributeViStringRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.CheckAttributeViStringResponse.FromString,
                )
        self.CheckGenerationStatus = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/CheckGenerationStatus',
                request_serializer=nirfsg__pb2.CheckGenerationStatusRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.CheckGenerationStatusResponse.FromString,
                )
        self.CheckIfConfigurationListExists = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/CheckIfConfigurationListExists',
                request_serializer=nirfsg__pb2.CheckIfConfigurationListExistsRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.CheckIfConfigurationListExistsResponse.FromString,
                )
        self.CheckIfScriptExists = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/CheckIfScriptExists',
                request_serializer=nirfsg__pb2.CheckIfScriptExistsRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.CheckIfScriptExistsResponse.FromString,
                )
        self.CheckIfWaveformExists = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/CheckIfWaveformExists',
                request_serializer=nirfsg__pb2.CheckIfWaveformExistsRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.CheckIfWaveformExistsResponse.FromString,
                )
        self.ClearAllArbWaveforms = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ClearAllArbWaveforms',
                request_serializer=nirfsg__pb2.ClearAllArbWaveformsRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ClearAllArbWaveformsResponse.FromString,
                )
        self.ClearArbWaveform = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ClearArbWaveform',
                request_serializer=nirfsg__pb2.ClearArbWaveformRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ClearArbWaveformResponse.FromString,
                )
        self.ClearError = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ClearError',
                request_serializer=nirfsg__pb2.ClearErrorRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ClearErrorResponse.FromString,
                )
        self.ClearSelfCalibrateRange = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ClearSelfCalibrateRange',
                request_serializer=nirfsg__pb2.ClearSelfCalibrateRangeRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ClearSelfCalibrateRangeResponse.FromString,
                )
        self.Close = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/Close',
                request_serializer=nirfsg__pb2.CloseRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.CloseResponse.FromString,
                )
        self.Commit = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/Commit',
                request_serializer=nirfsg__pb2.CommitRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.CommitResponse.FromString,
                )
        self.ConfigureDeembeddingTableInterpolationLinear = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ConfigureDeembeddingTableInterpolationLinear',
                request_serializer=nirfsg__pb2.ConfigureDeembeddingTableInterpolationLinearRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ConfigureDeembeddingTableInterpolationLinearResponse.FromString,
                )
        self.ConfigureDeembeddingTableInterpolationNearest = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ConfigureDeembeddingTableInterpolationNearest',
                request_serializer=nirfsg__pb2.ConfigureDeembeddingTableInterpolationNearestRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ConfigureDeembeddingTableInterpolationNearestResponse.FromString,
                )
        self.ConfigureDeembeddingTableInterpolationSpline = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ConfigureDeembeddingTableInterpolationSpline',
                request_serializer=nirfsg__pb2.ConfigureDeembeddingTableInterpolationSplineRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ConfigureDeembeddingTableInterpolationSplineResponse.FromString,
                )
        self.ConfigureDigitalEdgeConfigurationListStepTrigger = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ConfigureDigitalEdgeConfigurationListStepTrigger',
                request_serializer=nirfsg__pb2.ConfigureDigitalEdgeConfigurationListStepTriggerRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ConfigureDigitalEdgeConfigurationListStepTriggerResponse.FromString,
                )
        self.ConfigureDigitalEdgeScriptTrigger = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ConfigureDigitalEdgeScriptTrigger',
                request_serializer=nirfsg__pb2.ConfigureDigitalEdgeScriptTriggerRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ConfigureDigitalEdgeScriptTriggerResponse.FromString,
                )
        self.ConfigureDigitalEdgeStartTrigger = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ConfigureDigitalEdgeStartTrigger',
                request_serializer=nirfsg__pb2.ConfigureDigitalEdgeStartTriggerRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ConfigureDigitalEdgeStartTriggerResponse.FromString,
                )
        self.ConfigureDigitalLevelScriptTrigger = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ConfigureDigitalLevelScriptTrigger',
                request_serializer=nirfsg__pb2.ConfigureDigitalLevelScriptTriggerRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ConfigureDigitalLevelScriptTriggerResponse.FromString,
                )
        self.ConfigureDigitalModulationUserDefinedWaveform = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ConfigureDigitalModulationUserDefinedWaveform',
                request_serializer=nirfsg__pb2.ConfigureDigitalModulationUserDefinedWaveformRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ConfigureDigitalModulationUserDefinedWaveformResponse.FromString,
                )
        self.ConfigureGenerationMode = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ConfigureGenerationMode',
                request_serializer=nirfsg__pb2.ConfigureGenerationModeRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ConfigureGenerationModeResponse.FromString,
                )
        self.ConfigureOutputEnabled = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ConfigureOutputEnabled',
                request_serializer=nirfsg__pb2.ConfigureOutputEnabledRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ConfigureOutputEnabledResponse.FromString,
                )
        self.ConfigureP2PEndpointFullnessStartTrigger = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ConfigureP2PEndpointFullnessStartTrigger',
                request_serializer=nirfsg__pb2.ConfigureP2PEndpointFullnessStartTriggerRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ConfigureP2PEndpointFullnessStartTriggerResponse.FromString,
                )
        self.ConfigurePXIChassisClk10 = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ConfigurePXIChassisClk10',
                request_serializer=nirfsg__pb2.ConfigurePXIChassisClk10Request.SerializeToString,
                response_deserializer=nirfsg__pb2.ConfigurePXIChassisClk10Response.FromString,
                )
        self.ConfigurePowerLevelType = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ConfigurePowerLevelType',
                request_serializer=nirfsg__pb2.ConfigurePowerLevelTypeRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ConfigurePowerLevelTypeResponse.FromString,
                )
        self.ConfigureRF = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ConfigureRF',
                request_serializer=nirfsg__pb2.ConfigureRFRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ConfigureRFResponse.FromString,
                )
        self.ConfigureRefClock = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ConfigureRefClock',
                request_serializer=nirfsg__pb2.ConfigureRefClockRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ConfigureRefClockResponse.FromString,
                )
        self.ConfigureSignalBandwidth = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ConfigureSignalBandwidth',
                request_serializer=nirfsg__pb2.ConfigureSignalBandwidthRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ConfigureSignalBandwidthResponse.FromString,
                )
        self.ConfigureSoftwareScriptTrigger = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ConfigureSoftwareScriptTrigger',
                request_serializer=nirfsg__pb2.ConfigureSoftwareScriptTriggerRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ConfigureSoftwareScriptTriggerResponse.FromString,
                )
        self.ConfigureSoftwareStartTrigger = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ConfigureSoftwareStartTrigger',
                request_serializer=nirfsg__pb2.ConfigureSoftwareStartTriggerRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ConfigureSoftwareStartTriggerResponse.FromString,
                )
        self.ConfigureUpconverterPLLSettlingTime = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ConfigureUpconverterPLLSettlingTime',
                request_serializer=nirfsg__pb2.ConfigureUpconverterPLLSettlingTimeRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ConfigureUpconverterPLLSettlingTimeResponse.FromString,
                )
        self.CreateConfigurationList = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/CreateConfigurationList',
                request_serializer=nirfsg__pb2.CreateConfigurationListRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.CreateConfigurationListResponse.FromString,
                )
        self.CreateConfigurationListStep = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/CreateConfigurationListStep',
                request_serializer=nirfsg__pb2.CreateConfigurationListStepRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.CreateConfigurationListStepResponse.FromString,
                )
        self.CreateDeembeddingSparameterTableArray = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/CreateDeembeddingSparameterTableArray',
                request_serializer=nirfsg__pb2.CreateDeembeddingSparameterTableArrayRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.CreateDeembeddingSparameterTableArrayResponse.FromString,
                )
        self.CreateDeembeddingSparameterTableS2PFile = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/CreateDeembeddingSparameterTableS2PFile',
                request_serializer=nirfsg__pb2.CreateDeembeddingSparameterTableS2PFileRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.CreateDeembeddingSparameterTableS2PFileResponse.FromString,
                )
        self.DeleteAllDeembeddingTables = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/DeleteAllDeembeddingTables',
                request_serializer=nirfsg__pb2.DeleteAllDeembeddingTablesRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.DeleteAllDeembeddingTablesResponse.FromString,
                )
        self.DeleteConfigurationList = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/DeleteConfigurationList',
                request_serializer=nirfsg__pb2.DeleteConfigurationListRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.DeleteConfigurationListResponse.FromString,
                )
        self.DeleteDeembeddingTable = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/DeleteDeembeddingTable',
                request_serializer=nirfsg__pb2.DeleteDeembeddingTableRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.DeleteDeembeddingTableResponse.FromString,
                )
        self.DeleteScript = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/DeleteScript',
                request_serializer=nirfsg__pb2.DeleteScriptRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.DeleteScriptResponse.FromString,
                )
        self.Disable = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/Disable',
                request_serializer=nirfsg__pb2.DisableRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.DisableResponse.FromString,
                )
        self.DisableAllModulation = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/DisableAllModulation',
                request_serializer=nirfsg__pb2.DisableAllModulationRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.DisableAllModulationResponse.FromString,
                )
        self.DisableConfigurationListStepTrigger = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/DisableConfigurationListStepTrigger',
                request_serializer=nirfsg__pb2.DisableConfigurationListStepTriggerRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.DisableConfigurationListStepTriggerResponse.FromString,
                )
        self.DisableScriptTrigger = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/DisableScriptTrigger',
                request_serializer=nirfsg__pb2.DisableScriptTriggerRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.DisableScriptTriggerResponse.FromString,
                )
        self.DisableStartTrigger = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/DisableStartTrigger',
                request_serializer=nirfsg__pb2.DisableStartTriggerRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.DisableStartTriggerResponse.FromString,
                )
        self.ErrorMessage = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ErrorMessage',
                request_serializer=nirfsg__pb2.ErrorMessageRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ErrorMessageResponse.FromString,
                )
        self.ErrorQuery = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ErrorQuery',
                request_serializer=nirfsg__pb2.ErrorQueryRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ErrorQueryResponse.FromString,
                )
        self.ExportSignal = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ExportSignal',
                request_serializer=nirfsg__pb2.ExportSignalRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ExportSignalResponse.FromString,
                )
        self.GetAllNamedWaveformNames = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/GetAllNamedWaveformNames',
                request_serializer=nirfsg__pb2.GetAllNamedWaveformNamesRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.GetAllNamedWaveformNamesResponse.FromString,
                )
        self.GetAllScriptNames = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/GetAllScriptNames',
                request_serializer=nirfsg__pb2.GetAllScriptNamesRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.GetAllScriptNamesResponse.FromString,
                )
        self.GetScript = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/GetScript',
                request_serializer=nirfsg__pb2.GetScriptRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.GetScriptResponse.FromString,
                )
        self.GetAttributeViBoolean = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/GetAttributeViBoolean',
                request_serializer=nirfsg__pb2.GetAttributeViBooleanRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.GetAttributeViBooleanResponse.FromString,
                )
        self.GetAttributeViInt32 = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/GetAttributeViInt32',
                request_serializer=nirfsg__pb2.GetAttributeViInt32Request.SerializeToString,
                response_deserializer=nirfsg__pb2.GetAttributeViInt32Response.FromString,
                )
        self.GetAttributeViInt64 = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/GetAttributeViInt64',
                request_serializer=nirfsg__pb2.GetAttributeViInt64Request.SerializeToString,
                response_deserializer=nirfsg__pb2.GetAttributeViInt64Response.FromString,
                )
        self.GetAttributeViReal64 = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/GetAttributeViReal64',
                request_serializer=nirfsg__pb2.GetAttributeViReal64Request.SerializeToString,
                response_deserializer=nirfsg__pb2.GetAttributeViReal64Response.FromString,
                )
        self.GetAttributeViSession = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/GetAttributeViSession',
                request_serializer=nirfsg__pb2.GetAttributeViSessionRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.GetAttributeViSessionResponse.FromString,
                )
        self.GetAttributeViString = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/GetAttributeViString',
                request_serializer=nirfsg__pb2.GetAttributeViStringRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.GetAttributeViStringResponse.FromString,
                )
        self.GetChannelName = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/GetChannelName',
                request_serializer=nirfsg__pb2.GetChannelNameRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.GetChannelNameResponse.FromString,
                )
        self.GetDeembeddingSparameters = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/GetDeembeddingSparameters',
                request_serializer=nirfsg__pb2.GetDeembeddingSparametersRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.GetDeembeddingSparametersResponse.FromString,
                )
        self.GetError = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/GetError',
                request_serializer=nirfsg__pb2.GetErrorRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.GetErrorResponse.FromString,
                )
        self.GetExternalCalibrationLastDateAndTime = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/GetExternalCalibrationLastDateAndTime',
                request_serializer=nirfsg__pb2.GetExternalCalibrationLastDateAndTimeRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.GetExternalCalibrationLastDateAndTimeResponse.FromString,
                )
        self.GetMaxSettablePower = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/GetMaxSettablePower',
                request_serializer=nirfsg__pb2.GetMaxSettablePowerRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.GetMaxSettablePowerResponse.FromString,
                )
        self.GetSelfCalibrationDateAndTime = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/GetSelfCalibrationDateAndTime',
                request_serializer=nirfsg__pb2.GetSelfCalibrationDateAndTimeRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.GetSelfCalibrationDateAndTimeResponse.FromString,
                )
        self.GetSelfCalibrationTemperature = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/GetSelfCalibrationTemperature',
                request_serializer=nirfsg__pb2.GetSelfCalibrationTemperatureRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.GetSelfCalibrationTemperatureResponse.FromString,
                )
        self.GetTerminalName = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/GetTerminalName',
                request_serializer=nirfsg__pb2.GetTerminalNameRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.GetTerminalNameResponse.FromString,
                )
        self.GetUserData = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/GetUserData',
                request_serializer=nirfsg__pb2.GetUserDataRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.GetUserDataResponse.FromString,
                )
        self.GetWaveformBurstStartLocations = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/GetWaveformBurstStartLocations',
                request_serializer=nirfsg__pb2.GetWaveformBurstStartLocationsRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.GetWaveformBurstStartLocationsResponse.FromString,
                )
        self.GetWaveformBurstStopLocations = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/GetWaveformBurstStopLocations',
                request_serializer=nirfsg__pb2.GetWaveformBurstStopLocationsRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.GetWaveformBurstStopLocationsResponse.FromString,
                )
        self.GetWaveformMarkerEventLocations = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/GetWaveformMarkerEventLocations',
                request_serializer=nirfsg__pb2.GetWaveformMarkerEventLocationsRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.GetWaveformMarkerEventLocationsResponse.FromString,
                )
        self.Init = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/Init',
                request_serializer=nirfsg__pb2.InitRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.InitResponse.FromString,
                )
        self.InitWithOptions = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/InitWithOptions',
                request_serializer=nirfsg__pb2.InitWithOptionsRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.InitWithOptionsResponse.FromString,
                )
        self.Initiate = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/Initiate',
                request_serializer=nirfsg__pb2.InitiateRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.InitiateResponse.FromString,
                )
        self.InvalidateAllAttributes = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/InvalidateAllAttributes',
                request_serializer=nirfsg__pb2.InvalidateAllAttributesRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.InvalidateAllAttributesResponse.FromString,
                )
        self.LoadConfigurationsFromFile = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/LoadConfigurationsFromFile',
                request_serializer=nirfsg__pb2.LoadConfigurationsFromFileRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.LoadConfigurationsFromFileResponse.FromString,
                )
        self.PerformPowerSearch = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/PerformPowerSearch',
                request_serializer=nirfsg__pb2.PerformPowerSearchRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.PerformPowerSearchResponse.FromString,
                )
        self.PerformThermalCorrection = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/PerformThermalCorrection',
                request_serializer=nirfsg__pb2.PerformThermalCorrectionRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.PerformThermalCorrectionResponse.FromString,
                )
        self.QueryArbWaveformCapabilities = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/QueryArbWaveformCapabilities',
                request_serializer=nirfsg__pb2.QueryArbWaveformCapabilitiesRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.QueryArbWaveformCapabilitiesResponse.FromString,
                )
        self.ReadAndDownloadWaveformFromFileTDMS = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ReadAndDownloadWaveformFromFileTDMS',
                request_serializer=nirfsg__pb2.ReadAndDownloadWaveformFromFileTDMSRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ReadAndDownloadWaveformFromFileTDMSResponse.FromString,
                )
        self.Reset = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/Reset',
                request_serializer=nirfsg__pb2.ResetRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ResetResponse.FromString,
                )
        self.ResetAttribute = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ResetAttribute',
                request_serializer=nirfsg__pb2.ResetAttributeRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ResetAttributeResponse.FromString,
                )
        self.ResetDevice = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ResetDevice',
                request_serializer=nirfsg__pb2.ResetDeviceRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ResetDeviceResponse.FromString,
                )
        self.ResetWithDefaults = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ResetWithDefaults',
                request_serializer=nirfsg__pb2.ResetWithDefaultsRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ResetWithDefaultsResponse.FromString,
                )
        self.ResetWithOptions = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/ResetWithOptions',
                request_serializer=nirfsg__pb2.ResetWithOptionsRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.ResetWithOptionsResponse.FromString,
                )
        self.RevisionQuery = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/RevisionQuery',
                request_serializer=nirfsg__pb2.RevisionQueryRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.RevisionQueryResponse.FromString,
                )
        self.SaveConfigurationsToFile = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/SaveConfigurationsToFile',
                request_serializer=nirfsg__pb2.SaveConfigurationsToFileRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.SaveConfigurationsToFileResponse.FromString,
                )
        self.SelectArbWaveform = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/SelectArbWaveform',
                request_serializer=nirfsg__pb2.SelectArbWaveformRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.SelectArbWaveformResponse.FromString,
                )
        self.SelfCal = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/SelfCal',
                request_serializer=nirfsg__pb2.SelfCalRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.SelfCalResponse.FromString,
                )
        self.SelfCalibrateRange = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/SelfCalibrateRange',
                request_serializer=nirfsg__pb2.SelfCalibrateRangeRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.SelfCalibrateRangeResponse.FromString,
                )
        self.SelfTest = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/SelfTest',
                request_serializer=nirfsg__pb2.SelfTestRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.SelfTestResponse.FromString,
                )
        self.SendSoftwareEdgeTrigger = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/SendSoftwareEdgeTrigger',
                request_serializer=nirfsg__pb2.SendSoftwareEdgeTriggerRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.SendSoftwareEdgeTriggerResponse.FromString,
                )
        self.SetArbWaveformNextWritePosition = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/SetArbWaveformNextWritePosition',
                request_serializer=nirfsg__pb2.SetArbWaveformNextWritePositionRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.SetArbWaveformNextWritePositionResponse.FromString,
                )
        self.SetAttributeViBoolean = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/SetAttributeViBoolean',
                request_serializer=nirfsg__pb2.SetAttributeViBooleanRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.SetAttributeViBooleanResponse.FromString,
                )
        self.SetAttributeViInt32 = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/SetAttributeViInt32',
                request_serializer=nirfsg__pb2.SetAttributeViInt32Request.SerializeToString,
                response_deserializer=nirfsg__pb2.SetAttributeViInt32Response.FromString,
                )
        self.SetAttributeViInt64 = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/SetAttributeViInt64',
                request_serializer=nirfsg__pb2.SetAttributeViInt64Request.SerializeToString,
                response_deserializer=nirfsg__pb2.SetAttributeViInt64Response.FromString,
                )
        self.SetAttributeViReal64 = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/SetAttributeViReal64',
                request_serializer=nirfsg__pb2.SetAttributeViReal64Request.SerializeToString,
                response_deserializer=nirfsg__pb2.SetAttributeViReal64Response.FromString,
                )
        self.SetAttributeViSession = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/SetAttributeViSession',
                request_serializer=nirfsg__pb2.SetAttributeViSessionRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.SetAttributeViSessionResponse.FromString,
                )
        self.SetAttributeViString = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/SetAttributeViString',
                request_serializer=nirfsg__pb2.SetAttributeViStringRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.SetAttributeViStringResponse.FromString,
                )
        self.SetUserData = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/SetUserData',
                request_serializer=nirfsg__pb2.SetUserDataRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.SetUserDataResponse.FromString,
                )
        self.SetWaveformBurstStartLocations = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/SetWaveformBurstStartLocations',
                request_serializer=nirfsg__pb2.SetWaveformBurstStartLocationsRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.SetWaveformBurstStartLocationsResponse.FromString,
                )
        self.SetWaveformBurstStopLocations = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/SetWaveformBurstStopLocations',
                request_serializer=nirfsg__pb2.SetWaveformBurstStopLocationsRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.SetWaveformBurstStopLocationsResponse.FromString,
                )
        self.SetWaveformMarkerEventLocations = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/SetWaveformMarkerEventLocations',
                request_serializer=nirfsg__pb2.SetWaveformMarkerEventLocationsRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.SetWaveformMarkerEventLocationsResponse.FromString,
                )
        self.WaitUntilSettled = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/WaitUntilSettled',
                request_serializer=nirfsg__pb2.WaitUntilSettledRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.WaitUntilSettledResponse.FromString,
                )
        self.WriteArbWaveform = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/WriteArbWaveform',
                request_serializer=nirfsg__pb2.WriteArbWaveformRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.WriteArbWaveformResponse.FromString,
                )
        self.WriteArbWaveformComplexF32 = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/WriteArbWaveformComplexF32',
                request_serializer=nirfsg__pb2.WriteArbWaveformComplexF32Request.SerializeToString,
                response_deserializer=nirfsg__pb2.WriteArbWaveformComplexF32Response.FromString,
                )
        self.WriteArbWaveformComplexF64 = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/WriteArbWaveformComplexF64',
                request_serializer=nirfsg__pb2.WriteArbWaveformComplexF64Request.SerializeToString,
                response_deserializer=nirfsg__pb2.WriteArbWaveformComplexF64Response.FromString,
                )
        self.WriteArbWaveformComplexI16 = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/WriteArbWaveformComplexI16',
                request_serializer=nirfsg__pb2.WriteArbWaveformComplexI16Request.SerializeToString,
                response_deserializer=nirfsg__pb2.WriteArbWaveformComplexI16Response.FromString,
                )
        self.WriteArbWaveformF32 = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/WriteArbWaveformF32',
                request_serializer=nirfsg__pb2.WriteArbWaveformF32Request.SerializeToString,
                response_deserializer=nirfsg__pb2.WriteArbWaveformF32Response.FromString,
                )
        self.WriteScript = channel.unary_unary(
                '/nirfsg_grpc.NiRFSG/WriteScript',
                request_serializer=nirfsg__pb2.WriteScriptRequest.SerializeToString,
                response_deserializer=nirfsg__pb2.WriteScriptResponse.FromString,
                )


class NiRFSGServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Abort(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AllocateArbWaveform(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckAttributeViBoolean(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckAttributeViInt32(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckAttributeViInt64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckAttributeViReal64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckAttributeViSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckAttributeViString(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckGenerationStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckIfConfigurationListExists(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckIfScriptExists(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckIfWaveformExists(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearAllArbWaveforms(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearArbWaveform(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearError(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearSelfCalibrateRange(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Close(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Commit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureDeembeddingTableInterpolationLinear(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureDeembeddingTableInterpolationNearest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureDeembeddingTableInterpolationSpline(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureDigitalEdgeConfigurationListStepTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureDigitalEdgeScriptTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureDigitalEdgeStartTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureDigitalLevelScriptTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureDigitalModulationUserDefinedWaveform(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureGenerationMode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureOutputEnabled(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureP2PEndpointFullnessStartTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigurePXIChassisClk10(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigurePowerLevelType(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureRF(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureRefClock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureSignalBandwidth(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureSoftwareScriptTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureSoftwareStartTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureUpconverterPLLSettlingTime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateConfigurationList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateConfigurationListStep(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateDeembeddingSparameterTableArray(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateDeembeddingSparameterTableS2PFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAllDeembeddingTables(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteConfigurationList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteDeembeddingTable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteScript(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Disable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableAllModulation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableConfigurationListStepTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableScriptTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableStartTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ErrorMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ErrorQuery(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExportSignal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllNamedWaveformNames(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllScriptNames(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetScript(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttributeViBoolean(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttributeViInt32(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttributeViInt64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttributeViReal64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttributeViSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttributeViString(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetChannelName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDeembeddingSparameters(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetError(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetExternalCalibrationLastDateAndTime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMaxSettablePower(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSelfCalibrationDateAndTime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSelfCalibrationTemperature(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTerminalName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetWaveformBurstStartLocations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetWaveformBurstStopLocations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetWaveformMarkerEventLocations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Init(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitWithOptions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Initiate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InvalidateAllAttributes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadConfigurationsFromFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PerformPowerSearch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PerformThermalCorrection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryArbWaveformCapabilities(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadAndDownloadWaveformFromFileTDMS(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Reset(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetAttribute(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetDevice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetWithDefaults(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetWithOptions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RevisionQuery(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SaveConfigurationsToFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SelectArbWaveform(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SelfCal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SelfCalibrateRange(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SelfTest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendSoftwareEdgeTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetArbWaveformNextWritePosition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttributeViBoolean(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttributeViInt32(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttributeViInt64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttributeViReal64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttributeViSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttributeViString(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetUserData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetWaveformBurstStartLocations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetWaveformBurstStopLocations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetWaveformMarkerEventLocations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WaitUntilSettled(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteArbWaveform(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteArbWaveformComplexF32(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteArbWaveformComplexF64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteArbWaveformComplexI16(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteArbWaveformF32(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteScript(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NiRFSGServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Abort': grpc.unary_unary_rpc_method_handler(
                    servicer.Abort,
                    request_deserializer=nirfsg__pb2.AbortRequest.FromString,
                    response_serializer=nirfsg__pb2.AbortResponse.SerializeToString,
            ),
            'AllocateArbWaveform': grpc.unary_unary_rpc_method_handler(
                    servicer.AllocateArbWaveform,
                    request_deserializer=nirfsg__pb2.AllocateArbWaveformRequest.FromString,
                    response_serializer=nirfsg__pb2.AllocateArbWaveformResponse.SerializeToString,
            ),
            'CheckAttributeViBoolean': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckAttributeViBoolean,
                    request_deserializer=nirfsg__pb2.CheckAttributeViBooleanRequest.FromString,
                    response_serializer=nirfsg__pb2.CheckAttributeViBooleanResponse.SerializeToString,
            ),
            'CheckAttributeViInt32': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckAttributeViInt32,
                    request_deserializer=nirfsg__pb2.CheckAttributeViInt32Request.FromString,
                    response_serializer=nirfsg__pb2.CheckAttributeViInt32Response.SerializeToString,
            ),
            'CheckAttributeViInt64': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckAttributeViInt64,
                    request_deserializer=nirfsg__pb2.CheckAttributeViInt64Request.FromString,
                    response_serializer=nirfsg__pb2.CheckAttributeViInt64Response.SerializeToString,
            ),
            'CheckAttributeViReal64': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckAttributeViReal64,
                    request_deserializer=nirfsg__pb2.CheckAttributeViReal64Request.FromString,
                    response_serializer=nirfsg__pb2.CheckAttributeViReal64Response.SerializeToString,
            ),
            'CheckAttributeViSession': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckAttributeViSession,
                    request_deserializer=nirfsg__pb2.CheckAttributeViSessionRequest.FromString,
                    response_serializer=nirfsg__pb2.CheckAttributeViSessionResponse.SerializeToString,
            ),
            'CheckAttributeViString': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckAttributeViString,
                    request_deserializer=nirfsg__pb2.CheckAttributeViStringRequest.FromString,
                    response_serializer=nirfsg__pb2.CheckAttributeViStringResponse.SerializeToString,
            ),
            'CheckGenerationStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckGenerationStatus,
                    request_deserializer=nirfsg__pb2.CheckGenerationStatusRequest.FromString,
                    response_serializer=nirfsg__pb2.CheckGenerationStatusResponse.SerializeToString,
            ),
            'CheckIfConfigurationListExists': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckIfConfigurationListExists,
                    request_deserializer=nirfsg__pb2.CheckIfConfigurationListExistsRequest.FromString,
                    response_serializer=nirfsg__pb2.CheckIfConfigurationListExistsResponse.SerializeToString,
            ),
            'CheckIfScriptExists': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckIfScriptExists,
                    request_deserializer=nirfsg__pb2.CheckIfScriptExistsRequest.FromString,
                    response_serializer=nirfsg__pb2.CheckIfScriptExistsResponse.SerializeToString,
            ),
            'CheckIfWaveformExists': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckIfWaveformExists,
                    request_deserializer=nirfsg__pb2.CheckIfWaveformExistsRequest.FromString,
                    response_serializer=nirfsg__pb2.CheckIfWaveformExistsResponse.SerializeToString,
            ),
            'ClearAllArbWaveforms': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearAllArbWaveforms,
                    request_deserializer=nirfsg__pb2.ClearAllArbWaveformsRequest.FromString,
                    response_serializer=nirfsg__pb2.ClearAllArbWaveformsResponse.SerializeToString,
            ),
            'ClearArbWaveform': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearArbWaveform,
                    request_deserializer=nirfsg__pb2.ClearArbWaveformRequest.FromString,
                    response_serializer=nirfsg__pb2.ClearArbWaveformResponse.SerializeToString,
            ),
            'ClearError': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearError,
                    request_deserializer=nirfsg__pb2.ClearErrorRequest.FromString,
                    response_serializer=nirfsg__pb2.ClearErrorResponse.SerializeToString,
            ),
            'ClearSelfCalibrateRange': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearSelfCalibrateRange,
                    request_deserializer=nirfsg__pb2.ClearSelfCalibrateRangeRequest.FromString,
                    response_serializer=nirfsg__pb2.ClearSelfCalibrateRangeResponse.SerializeToString,
            ),
            'Close': grpc.unary_unary_rpc_method_handler(
                    servicer.Close,
                    request_deserializer=nirfsg__pb2.CloseRequest.FromString,
                    response_serializer=nirfsg__pb2.CloseResponse.SerializeToString,
            ),
            'Commit': grpc.unary_unary_rpc_method_handler(
                    servicer.Commit,
                    request_deserializer=nirfsg__pb2.CommitRequest.FromString,
                    response_serializer=nirfsg__pb2.CommitResponse.SerializeToString,
            ),
            'ConfigureDeembeddingTableInterpolationLinear': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureDeembeddingTableInterpolationLinear,
                    request_deserializer=nirfsg__pb2.ConfigureDeembeddingTableInterpolationLinearRequest.FromString,
                    response_serializer=nirfsg__pb2.ConfigureDeembeddingTableInterpolationLinearResponse.SerializeToString,
            ),
            'ConfigureDeembeddingTableInterpolationNearest': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureDeembeddingTableInterpolationNearest,
                    request_deserializer=nirfsg__pb2.ConfigureDeembeddingTableInterpolationNearestRequest.FromString,
                    response_serializer=nirfsg__pb2.ConfigureDeembeddingTableInterpolationNearestResponse.SerializeToString,
            ),
            'ConfigureDeembeddingTableInterpolationSpline': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureDeembeddingTableInterpolationSpline,
                    request_deserializer=nirfsg__pb2.ConfigureDeembeddingTableInterpolationSplineRequest.FromString,
                    response_serializer=nirfsg__pb2.ConfigureDeembeddingTableInterpolationSplineResponse.SerializeToString,
            ),
            'ConfigureDigitalEdgeConfigurationListStepTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureDigitalEdgeConfigurationListStepTrigger,
                    request_deserializer=nirfsg__pb2.ConfigureDigitalEdgeConfigurationListStepTriggerRequest.FromString,
                    response_serializer=nirfsg__pb2.ConfigureDigitalEdgeConfigurationListStepTriggerResponse.SerializeToString,
            ),
            'ConfigureDigitalEdgeScriptTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureDigitalEdgeScriptTrigger,
                    request_deserializer=nirfsg__pb2.ConfigureDigitalEdgeScriptTriggerRequest.FromString,
                    response_serializer=nirfsg__pb2.ConfigureDigitalEdgeScriptTriggerResponse.SerializeToString,
            ),
            'ConfigureDigitalEdgeStartTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureDigitalEdgeStartTrigger,
                    request_deserializer=nirfsg__pb2.ConfigureDigitalEdgeStartTriggerRequest.FromString,
                    response_serializer=nirfsg__pb2.ConfigureDigitalEdgeStartTriggerResponse.SerializeToString,
            ),
            'ConfigureDigitalLevelScriptTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureDigitalLevelScriptTrigger,
                    request_deserializer=nirfsg__pb2.ConfigureDigitalLevelScriptTriggerRequest.FromString,
                    response_serializer=nirfsg__pb2.ConfigureDigitalLevelScriptTriggerResponse.SerializeToString,
            ),
            'ConfigureDigitalModulationUserDefinedWaveform': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureDigitalModulationUserDefinedWaveform,
                    request_deserializer=nirfsg__pb2.ConfigureDigitalModulationUserDefinedWaveformRequest.FromString,
                    response_serializer=nirfsg__pb2.ConfigureDigitalModulationUserDefinedWaveformResponse.SerializeToString,
            ),
            'ConfigureGenerationMode': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureGenerationMode,
                    request_deserializer=nirfsg__pb2.ConfigureGenerationModeRequest.FromString,
                    response_serializer=nirfsg__pb2.ConfigureGenerationModeResponse.SerializeToString,
            ),
            'ConfigureOutputEnabled': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureOutputEnabled,
                    request_deserializer=nirfsg__pb2.ConfigureOutputEnabledRequest.FromString,
                    response_serializer=nirfsg__pb2.ConfigureOutputEnabledResponse.SerializeToString,
            ),
            'ConfigureP2PEndpointFullnessStartTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureP2PEndpointFullnessStartTrigger,
                    request_deserializer=nirfsg__pb2.ConfigureP2PEndpointFullnessStartTriggerRequest.FromString,
                    response_serializer=nirfsg__pb2.ConfigureP2PEndpointFullnessStartTriggerResponse.SerializeToString,
            ),
            'ConfigurePXIChassisClk10': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigurePXIChassisClk10,
                    request_deserializer=nirfsg__pb2.ConfigurePXIChassisClk10Request.FromString,
                    response_serializer=nirfsg__pb2.ConfigurePXIChassisClk10Response.SerializeToString,
            ),
            'ConfigurePowerLevelType': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigurePowerLevelType,
                    request_deserializer=nirfsg__pb2.ConfigurePowerLevelTypeRequest.FromString,
                    response_serializer=nirfsg__pb2.ConfigurePowerLevelTypeResponse.SerializeToString,
            ),
            'ConfigureRF': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureRF,
                    request_deserializer=nirfsg__pb2.ConfigureRFRequest.FromString,
                    response_serializer=nirfsg__pb2.ConfigureRFResponse.SerializeToString,
            ),
            'ConfigureRefClock': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureRefClock,
                    request_deserializer=nirfsg__pb2.ConfigureRefClockRequest.FromString,
                    response_serializer=nirfsg__pb2.ConfigureRefClockResponse.SerializeToString,
            ),
            'ConfigureSignalBandwidth': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureSignalBandwidth,
                    request_deserializer=nirfsg__pb2.ConfigureSignalBandwidthRequest.FromString,
                    response_serializer=nirfsg__pb2.ConfigureSignalBandwidthResponse.SerializeToString,
            ),
            'ConfigureSoftwareScriptTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureSoftwareScriptTrigger,
                    request_deserializer=nirfsg__pb2.ConfigureSoftwareScriptTriggerRequest.FromString,
                    response_serializer=nirfsg__pb2.ConfigureSoftwareScriptTriggerResponse.SerializeToString,
            ),
            'ConfigureSoftwareStartTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureSoftwareStartTrigger,
                    request_deserializer=nirfsg__pb2.ConfigureSoftwareStartTriggerRequest.FromString,
                    response_serializer=nirfsg__pb2.ConfigureSoftwareStartTriggerResponse.SerializeToString,
            ),
            'ConfigureUpconverterPLLSettlingTime': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureUpconverterPLLSettlingTime,
                    request_deserializer=nirfsg__pb2.ConfigureUpconverterPLLSettlingTimeRequest.FromString,
                    response_serializer=nirfsg__pb2.ConfigureUpconverterPLLSettlingTimeResponse.SerializeToString,
            ),
            'CreateConfigurationList': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateConfigurationList,
                    request_deserializer=nirfsg__pb2.CreateConfigurationListRequest.FromString,
                    response_serializer=nirfsg__pb2.CreateConfigurationListResponse.SerializeToString,
            ),
            'CreateConfigurationListStep': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateConfigurationListStep,
                    request_deserializer=nirfsg__pb2.CreateConfigurationListStepRequest.FromString,
                    response_serializer=nirfsg__pb2.CreateConfigurationListStepResponse.SerializeToString,
            ),
            'CreateDeembeddingSparameterTableArray': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateDeembeddingSparameterTableArray,
                    request_deserializer=nirfsg__pb2.CreateDeembeddingSparameterTableArrayRequest.FromString,
                    response_serializer=nirfsg__pb2.CreateDeembeddingSparameterTableArrayResponse.SerializeToString,
            ),
            'CreateDeembeddingSparameterTableS2PFile': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateDeembeddingSparameterTableS2PFile,
                    request_deserializer=nirfsg__pb2.CreateDeembeddingSparameterTableS2PFileRequest.FromString,
                    response_serializer=nirfsg__pb2.CreateDeembeddingSparameterTableS2PFileResponse.SerializeToString,
            ),
            'DeleteAllDeembeddingTables': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAllDeembeddingTables,
                    request_deserializer=nirfsg__pb2.DeleteAllDeembeddingTablesRequest.FromString,
                    response_serializer=nirfsg__pb2.DeleteAllDeembeddingTablesResponse.SerializeToString,
            ),
            'DeleteConfigurationList': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteConfigurationList,
                    request_deserializer=nirfsg__pb2.DeleteConfigurationListRequest.FromString,
                    response_serializer=nirfsg__pb2.DeleteConfigurationListResponse.SerializeToString,
            ),
            'DeleteDeembeddingTable': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteDeembeddingTable,
                    request_deserializer=nirfsg__pb2.DeleteDeembeddingTableRequest.FromString,
                    response_serializer=nirfsg__pb2.DeleteDeembeddingTableResponse.SerializeToString,
            ),
            'DeleteScript': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteScript,
                    request_deserializer=nirfsg__pb2.DeleteScriptRequest.FromString,
                    response_serializer=nirfsg__pb2.DeleteScriptResponse.SerializeToString,
            ),
            'Disable': grpc.unary_unary_rpc_method_handler(
                    servicer.Disable,
                    request_deserializer=nirfsg__pb2.DisableRequest.FromString,
                    response_serializer=nirfsg__pb2.DisableResponse.SerializeToString,
            ),
            'DisableAllModulation': grpc.unary_unary_rpc_method_handler(
                    servicer.DisableAllModulation,
                    request_deserializer=nirfsg__pb2.DisableAllModulationRequest.FromString,
                    response_serializer=nirfsg__pb2.DisableAllModulationResponse.SerializeToString,
            ),
            'DisableConfigurationListStepTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.DisableConfigurationListStepTrigger,
                    request_deserializer=nirfsg__pb2.DisableConfigurationListStepTriggerRequest.FromString,
                    response_serializer=nirfsg__pb2.DisableConfigurationListStepTriggerResponse.SerializeToString,
            ),
            'DisableScriptTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.DisableScriptTrigger,
                    request_deserializer=nirfsg__pb2.DisableScriptTriggerRequest.FromString,
                    response_serializer=nirfsg__pb2.DisableScriptTriggerResponse.SerializeToString,
            ),
            'DisableStartTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.DisableStartTrigger,
                    request_deserializer=nirfsg__pb2.DisableStartTriggerRequest.FromString,
                    response_serializer=nirfsg__pb2.DisableStartTriggerResponse.SerializeToString,
            ),
            'ErrorMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.ErrorMessage,
                    request_deserializer=nirfsg__pb2.ErrorMessageRequest.FromString,
                    response_serializer=nirfsg__pb2.ErrorMessageResponse.SerializeToString,
            ),
            'ErrorQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.ErrorQuery,
                    request_deserializer=nirfsg__pb2.ErrorQueryRequest.FromString,
                    response_serializer=nirfsg__pb2.ErrorQueryResponse.SerializeToString,
            ),
            'ExportSignal': grpc.unary_unary_rpc_method_handler(
                    servicer.ExportSignal,
                    request_deserializer=nirfsg__pb2.ExportSignalRequest.FromString,
                    response_serializer=nirfsg__pb2.ExportSignalResponse.SerializeToString,
            ),
            'GetAllNamedWaveformNames': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllNamedWaveformNames,
                    request_deserializer=nirfsg__pb2.GetAllNamedWaveformNamesRequest.FromString,
                    response_serializer=nirfsg__pb2.GetAllNamedWaveformNamesResponse.SerializeToString,
            ),
            'GetAllScriptNames': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllScriptNames,
                    request_deserializer=nirfsg__pb2.GetAllScriptNamesRequest.FromString,
                    response_serializer=nirfsg__pb2.GetAllScriptNamesResponse.SerializeToString,
            ),
            'GetScript': grpc.unary_unary_rpc_method_handler(
                    servicer.GetScript,
                    request_deserializer=nirfsg__pb2.GetScriptRequest.FromString,
                    response_serializer=nirfsg__pb2.GetScriptResponse.SerializeToString,
            ),
            'GetAttributeViBoolean': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViBoolean,
                    request_deserializer=nirfsg__pb2.GetAttributeViBooleanRequest.FromString,
                    response_serializer=nirfsg__pb2.GetAttributeViBooleanResponse.SerializeToString,
            ),
            'GetAttributeViInt32': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViInt32,
                    request_deserializer=nirfsg__pb2.GetAttributeViInt32Request.FromString,
                    response_serializer=nirfsg__pb2.GetAttributeViInt32Response.SerializeToString,
            ),
            'GetAttributeViInt64': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViInt64,
                    request_deserializer=nirfsg__pb2.GetAttributeViInt64Request.FromString,
                    response_serializer=nirfsg__pb2.GetAttributeViInt64Response.SerializeToString,
            ),
            'GetAttributeViReal64': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViReal64,
                    request_deserializer=nirfsg__pb2.GetAttributeViReal64Request.FromString,
                    response_serializer=nirfsg__pb2.GetAttributeViReal64Response.SerializeToString,
            ),
            'GetAttributeViSession': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViSession,
                    request_deserializer=nirfsg__pb2.GetAttributeViSessionRequest.FromString,
                    response_serializer=nirfsg__pb2.GetAttributeViSessionResponse.SerializeToString,
            ),
            'GetAttributeViString': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViString,
                    request_deserializer=nirfsg__pb2.GetAttributeViStringRequest.FromString,
                    response_serializer=nirfsg__pb2.GetAttributeViStringResponse.SerializeToString,
            ),
            'GetChannelName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetChannelName,
                    request_deserializer=nirfsg__pb2.GetChannelNameRequest.FromString,
                    response_serializer=nirfsg__pb2.GetChannelNameResponse.SerializeToString,
            ),
            'GetDeembeddingSparameters': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDeembeddingSparameters,
                    request_deserializer=nirfsg__pb2.GetDeembeddingSparametersRequest.FromString,
                    response_serializer=nirfsg__pb2.GetDeembeddingSparametersResponse.SerializeToString,
            ),
            'GetError': grpc.unary_unary_rpc_method_handler(
                    servicer.GetError,
                    request_deserializer=nirfsg__pb2.GetErrorRequest.FromString,
                    response_serializer=nirfsg__pb2.GetErrorResponse.SerializeToString,
            ),
            'GetExternalCalibrationLastDateAndTime': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExternalCalibrationLastDateAndTime,
                    request_deserializer=nirfsg__pb2.GetExternalCalibrationLastDateAndTimeRequest.FromString,
                    response_serializer=nirfsg__pb2.GetExternalCalibrationLastDateAndTimeResponse.SerializeToString,
            ),
            'GetMaxSettablePower': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMaxSettablePower,
                    request_deserializer=nirfsg__pb2.GetMaxSettablePowerRequest.FromString,
                    response_serializer=nirfsg__pb2.GetMaxSettablePowerResponse.SerializeToString,
            ),
            'GetSelfCalibrationDateAndTime': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSelfCalibrationDateAndTime,
                    request_deserializer=nirfsg__pb2.GetSelfCalibrationDateAndTimeRequest.FromString,
                    response_serializer=nirfsg__pb2.GetSelfCalibrationDateAndTimeResponse.SerializeToString,
            ),
            'GetSelfCalibrationTemperature': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSelfCalibrationTemperature,
                    request_deserializer=nirfsg__pb2.GetSelfCalibrationTemperatureRequest.FromString,
                    response_serializer=nirfsg__pb2.GetSelfCalibrationTemperatureResponse.SerializeToString,
            ),
            'GetTerminalName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTerminalName,
                    request_deserializer=nirfsg__pb2.GetTerminalNameRequest.FromString,
                    response_serializer=nirfsg__pb2.GetTerminalNameResponse.SerializeToString,
            ),
            'GetUserData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserData,
                    request_deserializer=nirfsg__pb2.GetUserDataRequest.FromString,
                    response_serializer=nirfsg__pb2.GetUserDataResponse.SerializeToString,
            ),
            'GetWaveformBurstStartLocations': grpc.unary_unary_rpc_method_handler(
                    servicer.GetWaveformBurstStartLocations,
                    request_deserializer=nirfsg__pb2.GetWaveformBurstStartLocationsRequest.FromString,
                    response_serializer=nirfsg__pb2.GetWaveformBurstStartLocationsResponse.SerializeToString,
            ),
            'GetWaveformBurstStopLocations': grpc.unary_unary_rpc_method_handler(
                    servicer.GetWaveformBurstStopLocations,
                    request_deserializer=nirfsg__pb2.GetWaveformBurstStopLocationsRequest.FromString,
                    response_serializer=nirfsg__pb2.GetWaveformBurstStopLocationsResponse.SerializeToString,
            ),
            'GetWaveformMarkerEventLocations': grpc.unary_unary_rpc_method_handler(
                    servicer.GetWaveformMarkerEventLocations,
                    request_deserializer=nirfsg__pb2.GetWaveformMarkerEventLocationsRequest.FromString,
                    response_serializer=nirfsg__pb2.GetWaveformMarkerEventLocationsResponse.SerializeToString,
            ),
            'Init': grpc.unary_unary_rpc_method_handler(
                    servicer.Init,
                    request_deserializer=nirfsg__pb2.InitRequest.FromString,
                    response_serializer=nirfsg__pb2.InitResponse.SerializeToString,
            ),
            'InitWithOptions': grpc.unary_unary_rpc_method_handler(
                    servicer.InitWithOptions,
                    request_deserializer=nirfsg__pb2.InitWithOptionsRequest.FromString,
                    response_serializer=nirfsg__pb2.InitWithOptionsResponse.SerializeToString,
            ),
            'Initiate': grpc.unary_unary_rpc_method_handler(
                    servicer.Initiate,
                    request_deserializer=nirfsg__pb2.InitiateRequest.FromString,
                    response_serializer=nirfsg__pb2.InitiateResponse.SerializeToString,
            ),
            'InvalidateAllAttributes': grpc.unary_unary_rpc_method_handler(
                    servicer.InvalidateAllAttributes,
                    request_deserializer=nirfsg__pb2.InvalidateAllAttributesRequest.FromString,
                    response_serializer=nirfsg__pb2.InvalidateAllAttributesResponse.SerializeToString,
            ),
            'LoadConfigurationsFromFile': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadConfigurationsFromFile,
                    request_deserializer=nirfsg__pb2.LoadConfigurationsFromFileRequest.FromString,
                    response_serializer=nirfsg__pb2.LoadConfigurationsFromFileResponse.SerializeToString,
            ),
            'PerformPowerSearch': grpc.unary_unary_rpc_method_handler(
                    servicer.PerformPowerSearch,
                    request_deserializer=nirfsg__pb2.PerformPowerSearchRequest.FromString,
                    response_serializer=nirfsg__pb2.PerformPowerSearchResponse.SerializeToString,
            ),
            'PerformThermalCorrection': grpc.unary_unary_rpc_method_handler(
                    servicer.PerformThermalCorrection,
                    request_deserializer=nirfsg__pb2.PerformThermalCorrectionRequest.FromString,
                    response_serializer=nirfsg__pb2.PerformThermalCorrectionResponse.SerializeToString,
            ),
            'QueryArbWaveformCapabilities': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryArbWaveformCapabilities,
                    request_deserializer=nirfsg__pb2.QueryArbWaveformCapabilitiesRequest.FromString,
                    response_serializer=nirfsg__pb2.QueryArbWaveformCapabilitiesResponse.SerializeToString,
            ),
            'ReadAndDownloadWaveformFromFileTDMS': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadAndDownloadWaveformFromFileTDMS,
                    request_deserializer=nirfsg__pb2.ReadAndDownloadWaveformFromFileTDMSRequest.FromString,
                    response_serializer=nirfsg__pb2.ReadAndDownloadWaveformFromFileTDMSResponse.SerializeToString,
            ),
            'Reset': grpc.unary_unary_rpc_method_handler(
                    servicer.Reset,
                    request_deserializer=nirfsg__pb2.ResetRequest.FromString,
                    response_serializer=nirfsg__pb2.ResetResponse.SerializeToString,
            ),
            'ResetAttribute': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetAttribute,
                    request_deserializer=nirfsg__pb2.ResetAttributeRequest.FromString,
                    response_serializer=nirfsg__pb2.ResetAttributeResponse.SerializeToString,
            ),
            'ResetDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetDevice,
                    request_deserializer=nirfsg__pb2.ResetDeviceRequest.FromString,
                    response_serializer=nirfsg__pb2.ResetDeviceResponse.SerializeToString,
            ),
            'ResetWithDefaults': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetWithDefaults,
                    request_deserializer=nirfsg__pb2.ResetWithDefaultsRequest.FromString,
                    response_serializer=nirfsg__pb2.ResetWithDefaultsResponse.SerializeToString,
            ),
            'ResetWithOptions': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetWithOptions,
                    request_deserializer=nirfsg__pb2.ResetWithOptionsRequest.FromString,
                    response_serializer=nirfsg__pb2.ResetWithOptionsResponse.SerializeToString,
            ),
            'RevisionQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.RevisionQuery,
                    request_deserializer=nirfsg__pb2.RevisionQueryRequest.FromString,
                    response_serializer=nirfsg__pb2.RevisionQueryResponse.SerializeToString,
            ),
            'SaveConfigurationsToFile': grpc.unary_unary_rpc_method_handler(
                    servicer.SaveConfigurationsToFile,
                    request_deserializer=nirfsg__pb2.SaveConfigurationsToFileRequest.FromString,
                    response_serializer=nirfsg__pb2.SaveConfigurationsToFileResponse.SerializeToString,
            ),
            'SelectArbWaveform': grpc.unary_unary_rpc_method_handler(
                    servicer.SelectArbWaveform,
                    request_deserializer=nirfsg__pb2.SelectArbWaveformRequest.FromString,
                    response_serializer=nirfsg__pb2.SelectArbWaveformResponse.SerializeToString,
            ),
            'SelfCal': grpc.unary_unary_rpc_method_handler(
                    servicer.SelfCal,
                    request_deserializer=nirfsg__pb2.SelfCalRequest.FromString,
                    response_serializer=nirfsg__pb2.SelfCalResponse.SerializeToString,
            ),
            'SelfCalibrateRange': grpc.unary_unary_rpc_method_handler(
                    servicer.SelfCalibrateRange,
                    request_deserializer=nirfsg__pb2.SelfCalibrateRangeRequest.FromString,
                    response_serializer=nirfsg__pb2.SelfCalibrateRangeResponse.SerializeToString,
            ),
            'SelfTest': grpc.unary_unary_rpc_method_handler(
                    servicer.SelfTest,
                    request_deserializer=nirfsg__pb2.SelfTestRequest.FromString,
                    response_serializer=nirfsg__pb2.SelfTestResponse.SerializeToString,
            ),
            'SendSoftwareEdgeTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.SendSoftwareEdgeTrigger,
                    request_deserializer=nirfsg__pb2.SendSoftwareEdgeTriggerRequest.FromString,
                    response_serializer=nirfsg__pb2.SendSoftwareEdgeTriggerResponse.SerializeToString,
            ),
            'SetArbWaveformNextWritePosition': grpc.unary_unary_rpc_method_handler(
                    servicer.SetArbWaveformNextWritePosition,
                    request_deserializer=nirfsg__pb2.SetArbWaveformNextWritePositionRequest.FromString,
                    response_serializer=nirfsg__pb2.SetArbWaveformNextWritePositionResponse.SerializeToString,
            ),
            'SetAttributeViBoolean': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViBoolean,
                    request_deserializer=nirfsg__pb2.SetAttributeViBooleanRequest.FromString,
                    response_serializer=nirfsg__pb2.SetAttributeViBooleanResponse.SerializeToString,
            ),
            'SetAttributeViInt32': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViInt32,
                    request_deserializer=nirfsg__pb2.SetAttributeViInt32Request.FromString,
                    response_serializer=nirfsg__pb2.SetAttributeViInt32Response.SerializeToString,
            ),
            'SetAttributeViInt64': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViInt64,
                    request_deserializer=nirfsg__pb2.SetAttributeViInt64Request.FromString,
                    response_serializer=nirfsg__pb2.SetAttributeViInt64Response.SerializeToString,
            ),
            'SetAttributeViReal64': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViReal64,
                    request_deserializer=nirfsg__pb2.SetAttributeViReal64Request.FromString,
                    response_serializer=nirfsg__pb2.SetAttributeViReal64Response.SerializeToString,
            ),
            'SetAttributeViSession': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViSession,
                    request_deserializer=nirfsg__pb2.SetAttributeViSessionRequest.FromString,
                    response_serializer=nirfsg__pb2.SetAttributeViSessionResponse.SerializeToString,
            ),
            'SetAttributeViString': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViString,
                    request_deserializer=nirfsg__pb2.SetAttributeViStringRequest.FromString,
                    response_serializer=nirfsg__pb2.SetAttributeViStringResponse.SerializeToString,
            ),
            'SetUserData': grpc.unary_unary_rpc_method_handler(
                    servicer.SetUserData,
                    request_deserializer=nirfsg__pb2.SetUserDataRequest.FromString,
                    response_serializer=nirfsg__pb2.SetUserDataResponse.SerializeToString,
            ),
            'SetWaveformBurstStartLocations': grpc.unary_unary_rpc_method_handler(
                    servicer.SetWaveformBurstStartLocations,
                    request_deserializer=nirfsg__pb2.SetWaveformBurstStartLocationsRequest.FromString,
                    response_serializer=nirfsg__pb2.SetWaveformBurstStartLocationsResponse.SerializeToString,
            ),
            'SetWaveformBurstStopLocations': grpc.unary_unary_rpc_method_handler(
                    servicer.SetWaveformBurstStopLocations,
                    request_deserializer=nirfsg__pb2.SetWaveformBurstStopLocationsRequest.FromString,
                    response_serializer=nirfsg__pb2.SetWaveformBurstStopLocationsResponse.SerializeToString,
            ),
            'SetWaveformMarkerEventLocations': grpc.unary_unary_rpc_method_handler(
                    servicer.SetWaveformMarkerEventLocations,
                    request_deserializer=nirfsg__pb2.SetWaveformMarkerEventLocationsRequest.FromString,
                    response_serializer=nirfsg__pb2.SetWaveformMarkerEventLocationsResponse.SerializeToString,
            ),
            'WaitUntilSettled': grpc.unary_unary_rpc_method_handler(
                    servicer.WaitUntilSettled,
                    request_deserializer=nirfsg__pb2.WaitUntilSettledRequest.FromString,
                    response_serializer=nirfsg__pb2.WaitUntilSettledResponse.SerializeToString,
            ),
            'WriteArbWaveform': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteArbWaveform,
                    request_deserializer=nirfsg__pb2.WriteArbWaveformRequest.FromString,
                    response_serializer=nirfsg__pb2.WriteArbWaveformResponse.SerializeToString,
            ),
            'WriteArbWaveformComplexF32': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteArbWaveformComplexF32,
                    request_deserializer=nirfsg__pb2.WriteArbWaveformComplexF32Request.FromString,
                    response_serializer=nirfsg__pb2.WriteArbWaveformComplexF32Response.SerializeToString,
            ),
            'WriteArbWaveformComplexF64': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteArbWaveformComplexF64,
                    request_deserializer=nirfsg__pb2.WriteArbWaveformComplexF64Request.FromString,
                    response_serializer=nirfsg__pb2.WriteArbWaveformComplexF64Response.SerializeToString,
            ),
            'WriteArbWaveformComplexI16': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteArbWaveformComplexI16,
                    request_deserializer=nirfsg__pb2.WriteArbWaveformComplexI16Request.FromString,
                    response_serializer=nirfsg__pb2.WriteArbWaveformComplexI16Response.SerializeToString,
            ),
            'WriteArbWaveformF32': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteArbWaveformF32,
                    request_deserializer=nirfsg__pb2.WriteArbWaveformF32Request.FromString,
                    response_serializer=nirfsg__pb2.WriteArbWaveformF32Response.SerializeToString,
            ),
            'WriteScript': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteScript,
                    request_deserializer=nirfsg__pb2.WriteScriptRequest.FromString,
                    response_serializer=nirfsg__pb2.WriteScriptResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nirfsg_grpc.NiRFSG', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NiRFSG(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Abort(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/Abort',
            nirfsg__pb2.AbortRequest.SerializeToString,
            nirfsg__pb2.AbortResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AllocateArbWaveform(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/AllocateArbWaveform',
            nirfsg__pb2.AllocateArbWaveformRequest.SerializeToString,
            nirfsg__pb2.AllocateArbWaveformResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckAttributeViBoolean(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/CheckAttributeViBoolean',
            nirfsg__pb2.CheckAttributeViBooleanRequest.SerializeToString,
            nirfsg__pb2.CheckAttributeViBooleanResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckAttributeViInt32(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/CheckAttributeViInt32',
            nirfsg__pb2.CheckAttributeViInt32Request.SerializeToString,
            nirfsg__pb2.CheckAttributeViInt32Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckAttributeViInt64(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/CheckAttributeViInt64',
            nirfsg__pb2.CheckAttributeViInt64Request.SerializeToString,
            nirfsg__pb2.CheckAttributeViInt64Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckAttributeViReal64(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/CheckAttributeViReal64',
            nirfsg__pb2.CheckAttributeViReal64Request.SerializeToString,
            nirfsg__pb2.CheckAttributeViReal64Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckAttributeViSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/CheckAttributeViSession',
            nirfsg__pb2.CheckAttributeViSessionRequest.SerializeToString,
            nirfsg__pb2.CheckAttributeViSessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckAttributeViString(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/CheckAttributeViString',
            nirfsg__pb2.CheckAttributeViStringRequest.SerializeToString,
            nirfsg__pb2.CheckAttributeViStringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckGenerationStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/CheckGenerationStatus',
            nirfsg__pb2.CheckGenerationStatusRequest.SerializeToString,
            nirfsg__pb2.CheckGenerationStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckIfConfigurationListExists(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/CheckIfConfigurationListExists',
            nirfsg__pb2.CheckIfConfigurationListExistsRequest.SerializeToString,
            nirfsg__pb2.CheckIfConfigurationListExistsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckIfScriptExists(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/CheckIfScriptExists',
            nirfsg__pb2.CheckIfScriptExistsRequest.SerializeToString,
            nirfsg__pb2.CheckIfScriptExistsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckIfWaveformExists(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/CheckIfWaveformExists',
            nirfsg__pb2.CheckIfWaveformExistsRequest.SerializeToString,
            nirfsg__pb2.CheckIfWaveformExistsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClearAllArbWaveforms(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ClearAllArbWaveforms',
            nirfsg__pb2.ClearAllArbWaveformsRequest.SerializeToString,
            nirfsg__pb2.ClearAllArbWaveformsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClearArbWaveform(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ClearArbWaveform',
            nirfsg__pb2.ClearArbWaveformRequest.SerializeToString,
            nirfsg__pb2.ClearArbWaveformResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClearError(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ClearError',
            nirfsg__pb2.ClearErrorRequest.SerializeToString,
            nirfsg__pb2.ClearErrorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClearSelfCalibrateRange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ClearSelfCalibrateRange',
            nirfsg__pb2.ClearSelfCalibrateRangeRequest.SerializeToString,
            nirfsg__pb2.ClearSelfCalibrateRangeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Close(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/Close',
            nirfsg__pb2.CloseRequest.SerializeToString,
            nirfsg__pb2.CloseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Commit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/Commit',
            nirfsg__pb2.CommitRequest.SerializeToString,
            nirfsg__pb2.CommitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureDeembeddingTableInterpolationLinear(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ConfigureDeembeddingTableInterpolationLinear',
            nirfsg__pb2.ConfigureDeembeddingTableInterpolationLinearRequest.SerializeToString,
            nirfsg__pb2.ConfigureDeembeddingTableInterpolationLinearResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureDeembeddingTableInterpolationNearest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ConfigureDeembeddingTableInterpolationNearest',
            nirfsg__pb2.ConfigureDeembeddingTableInterpolationNearestRequest.SerializeToString,
            nirfsg__pb2.ConfigureDeembeddingTableInterpolationNearestResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureDeembeddingTableInterpolationSpline(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ConfigureDeembeddingTableInterpolationSpline',
            nirfsg__pb2.ConfigureDeembeddingTableInterpolationSplineRequest.SerializeToString,
            nirfsg__pb2.ConfigureDeembeddingTableInterpolationSplineResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureDigitalEdgeConfigurationListStepTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ConfigureDigitalEdgeConfigurationListStepTrigger',
            nirfsg__pb2.ConfigureDigitalEdgeConfigurationListStepTriggerRequest.SerializeToString,
            nirfsg__pb2.ConfigureDigitalEdgeConfigurationListStepTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureDigitalEdgeScriptTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ConfigureDigitalEdgeScriptTrigger',
            nirfsg__pb2.ConfigureDigitalEdgeScriptTriggerRequest.SerializeToString,
            nirfsg__pb2.ConfigureDigitalEdgeScriptTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureDigitalEdgeStartTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ConfigureDigitalEdgeStartTrigger',
            nirfsg__pb2.ConfigureDigitalEdgeStartTriggerRequest.SerializeToString,
            nirfsg__pb2.ConfigureDigitalEdgeStartTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureDigitalLevelScriptTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ConfigureDigitalLevelScriptTrigger',
            nirfsg__pb2.ConfigureDigitalLevelScriptTriggerRequest.SerializeToString,
            nirfsg__pb2.ConfigureDigitalLevelScriptTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureDigitalModulationUserDefinedWaveform(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ConfigureDigitalModulationUserDefinedWaveform',
            nirfsg__pb2.ConfigureDigitalModulationUserDefinedWaveformRequest.SerializeToString,
            nirfsg__pb2.ConfigureDigitalModulationUserDefinedWaveformResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureGenerationMode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ConfigureGenerationMode',
            nirfsg__pb2.ConfigureGenerationModeRequest.SerializeToString,
            nirfsg__pb2.ConfigureGenerationModeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureOutputEnabled(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ConfigureOutputEnabled',
            nirfsg__pb2.ConfigureOutputEnabledRequest.SerializeToString,
            nirfsg__pb2.ConfigureOutputEnabledResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureP2PEndpointFullnessStartTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ConfigureP2PEndpointFullnessStartTrigger',
            nirfsg__pb2.ConfigureP2PEndpointFullnessStartTriggerRequest.SerializeToString,
            nirfsg__pb2.ConfigureP2PEndpointFullnessStartTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigurePXIChassisClk10(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ConfigurePXIChassisClk10',
            nirfsg__pb2.ConfigurePXIChassisClk10Request.SerializeToString,
            nirfsg__pb2.ConfigurePXIChassisClk10Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigurePowerLevelType(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ConfigurePowerLevelType',
            nirfsg__pb2.ConfigurePowerLevelTypeRequest.SerializeToString,
            nirfsg__pb2.ConfigurePowerLevelTypeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureRF(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ConfigureRF',
            nirfsg__pb2.ConfigureRFRequest.SerializeToString,
            nirfsg__pb2.ConfigureRFResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureRefClock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ConfigureRefClock',
            nirfsg__pb2.ConfigureRefClockRequest.SerializeToString,
            nirfsg__pb2.ConfigureRefClockResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureSignalBandwidth(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ConfigureSignalBandwidth',
            nirfsg__pb2.ConfigureSignalBandwidthRequest.SerializeToString,
            nirfsg__pb2.ConfigureSignalBandwidthResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureSoftwareScriptTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ConfigureSoftwareScriptTrigger',
            nirfsg__pb2.ConfigureSoftwareScriptTriggerRequest.SerializeToString,
            nirfsg__pb2.ConfigureSoftwareScriptTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureSoftwareStartTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ConfigureSoftwareStartTrigger',
            nirfsg__pb2.ConfigureSoftwareStartTriggerRequest.SerializeToString,
            nirfsg__pb2.ConfigureSoftwareStartTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureUpconverterPLLSettlingTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ConfigureUpconverterPLLSettlingTime',
            nirfsg__pb2.ConfigureUpconverterPLLSettlingTimeRequest.SerializeToString,
            nirfsg__pb2.ConfigureUpconverterPLLSettlingTimeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateConfigurationList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/CreateConfigurationList',
            nirfsg__pb2.CreateConfigurationListRequest.SerializeToString,
            nirfsg__pb2.CreateConfigurationListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateConfigurationListStep(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/CreateConfigurationListStep',
            nirfsg__pb2.CreateConfigurationListStepRequest.SerializeToString,
            nirfsg__pb2.CreateConfigurationListStepResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateDeembeddingSparameterTableArray(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/CreateDeembeddingSparameterTableArray',
            nirfsg__pb2.CreateDeembeddingSparameterTableArrayRequest.SerializeToString,
            nirfsg__pb2.CreateDeembeddingSparameterTableArrayResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateDeembeddingSparameterTableS2PFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/CreateDeembeddingSparameterTableS2PFile',
            nirfsg__pb2.CreateDeembeddingSparameterTableS2PFileRequest.SerializeToString,
            nirfsg__pb2.CreateDeembeddingSparameterTableS2PFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAllDeembeddingTables(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/DeleteAllDeembeddingTables',
            nirfsg__pb2.DeleteAllDeembeddingTablesRequest.SerializeToString,
            nirfsg__pb2.DeleteAllDeembeddingTablesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteConfigurationList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/DeleteConfigurationList',
            nirfsg__pb2.DeleteConfigurationListRequest.SerializeToString,
            nirfsg__pb2.DeleteConfigurationListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteDeembeddingTable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/DeleteDeembeddingTable',
            nirfsg__pb2.DeleteDeembeddingTableRequest.SerializeToString,
            nirfsg__pb2.DeleteDeembeddingTableResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteScript(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/DeleteScript',
            nirfsg__pb2.DeleteScriptRequest.SerializeToString,
            nirfsg__pb2.DeleteScriptResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Disable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/Disable',
            nirfsg__pb2.DisableRequest.SerializeToString,
            nirfsg__pb2.DisableResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableAllModulation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/DisableAllModulation',
            nirfsg__pb2.DisableAllModulationRequest.SerializeToString,
            nirfsg__pb2.DisableAllModulationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableConfigurationListStepTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/DisableConfigurationListStepTrigger',
            nirfsg__pb2.DisableConfigurationListStepTriggerRequest.SerializeToString,
            nirfsg__pb2.DisableConfigurationListStepTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableScriptTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/DisableScriptTrigger',
            nirfsg__pb2.DisableScriptTriggerRequest.SerializeToString,
            nirfsg__pb2.DisableScriptTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableStartTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/DisableStartTrigger',
            nirfsg__pb2.DisableStartTriggerRequest.SerializeToString,
            nirfsg__pb2.DisableStartTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ErrorMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ErrorMessage',
            nirfsg__pb2.ErrorMessageRequest.SerializeToString,
            nirfsg__pb2.ErrorMessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ErrorQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ErrorQuery',
            nirfsg__pb2.ErrorQueryRequest.SerializeToString,
            nirfsg__pb2.ErrorQueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExportSignal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ExportSignal',
            nirfsg__pb2.ExportSignalRequest.SerializeToString,
            nirfsg__pb2.ExportSignalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllNamedWaveformNames(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/GetAllNamedWaveformNames',
            nirfsg__pb2.GetAllNamedWaveformNamesRequest.SerializeToString,
            nirfsg__pb2.GetAllNamedWaveformNamesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllScriptNames(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/GetAllScriptNames',
            nirfsg__pb2.GetAllScriptNamesRequest.SerializeToString,
            nirfsg__pb2.GetAllScriptNamesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetScript(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/GetScript',
            nirfsg__pb2.GetScriptRequest.SerializeToString,
            nirfsg__pb2.GetScriptResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAttributeViBoolean(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/GetAttributeViBoolean',
            nirfsg__pb2.GetAttributeViBooleanRequest.SerializeToString,
            nirfsg__pb2.GetAttributeViBooleanResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAttributeViInt32(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/GetAttributeViInt32',
            nirfsg__pb2.GetAttributeViInt32Request.SerializeToString,
            nirfsg__pb2.GetAttributeViInt32Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAttributeViInt64(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/GetAttributeViInt64',
            nirfsg__pb2.GetAttributeViInt64Request.SerializeToString,
            nirfsg__pb2.GetAttributeViInt64Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAttributeViReal64(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/GetAttributeViReal64',
            nirfsg__pb2.GetAttributeViReal64Request.SerializeToString,
            nirfsg__pb2.GetAttributeViReal64Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAttributeViSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/GetAttributeViSession',
            nirfsg__pb2.GetAttributeViSessionRequest.SerializeToString,
            nirfsg__pb2.GetAttributeViSessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAttributeViString(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/GetAttributeViString',
            nirfsg__pb2.GetAttributeViStringRequest.SerializeToString,
            nirfsg__pb2.GetAttributeViStringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetChannelName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/GetChannelName',
            nirfsg__pb2.GetChannelNameRequest.SerializeToString,
            nirfsg__pb2.GetChannelNameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDeembeddingSparameters(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/GetDeembeddingSparameters',
            nirfsg__pb2.GetDeembeddingSparametersRequest.SerializeToString,
            nirfsg__pb2.GetDeembeddingSparametersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetError(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/GetError',
            nirfsg__pb2.GetErrorRequest.SerializeToString,
            nirfsg__pb2.GetErrorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetExternalCalibrationLastDateAndTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/GetExternalCalibrationLastDateAndTime',
            nirfsg__pb2.GetExternalCalibrationLastDateAndTimeRequest.SerializeToString,
            nirfsg__pb2.GetExternalCalibrationLastDateAndTimeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMaxSettablePower(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/GetMaxSettablePower',
            nirfsg__pb2.GetMaxSettablePowerRequest.SerializeToString,
            nirfsg__pb2.GetMaxSettablePowerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSelfCalibrationDateAndTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/GetSelfCalibrationDateAndTime',
            nirfsg__pb2.GetSelfCalibrationDateAndTimeRequest.SerializeToString,
            nirfsg__pb2.GetSelfCalibrationDateAndTimeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSelfCalibrationTemperature(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/GetSelfCalibrationTemperature',
            nirfsg__pb2.GetSelfCalibrationTemperatureRequest.SerializeToString,
            nirfsg__pb2.GetSelfCalibrationTemperatureResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTerminalName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/GetTerminalName',
            nirfsg__pb2.GetTerminalNameRequest.SerializeToString,
            nirfsg__pb2.GetTerminalNameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/GetUserData',
            nirfsg__pb2.GetUserDataRequest.SerializeToString,
            nirfsg__pb2.GetUserDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetWaveformBurstStartLocations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/GetWaveformBurstStartLocations',
            nirfsg__pb2.GetWaveformBurstStartLocationsRequest.SerializeToString,
            nirfsg__pb2.GetWaveformBurstStartLocationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetWaveformBurstStopLocations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/GetWaveformBurstStopLocations',
            nirfsg__pb2.GetWaveformBurstStopLocationsRequest.SerializeToString,
            nirfsg__pb2.GetWaveformBurstStopLocationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetWaveformMarkerEventLocations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/GetWaveformMarkerEventLocations',
            nirfsg__pb2.GetWaveformMarkerEventLocationsRequest.SerializeToString,
            nirfsg__pb2.GetWaveformMarkerEventLocationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Init(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/Init',
            nirfsg__pb2.InitRequest.SerializeToString,
            nirfsg__pb2.InitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InitWithOptions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/InitWithOptions',
            nirfsg__pb2.InitWithOptionsRequest.SerializeToString,
            nirfsg__pb2.InitWithOptionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Initiate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/Initiate',
            nirfsg__pb2.InitiateRequest.SerializeToString,
            nirfsg__pb2.InitiateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InvalidateAllAttributes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/InvalidateAllAttributes',
            nirfsg__pb2.InvalidateAllAttributesRequest.SerializeToString,
            nirfsg__pb2.InvalidateAllAttributesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LoadConfigurationsFromFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/LoadConfigurationsFromFile',
            nirfsg__pb2.LoadConfigurationsFromFileRequest.SerializeToString,
            nirfsg__pb2.LoadConfigurationsFromFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PerformPowerSearch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/PerformPowerSearch',
            nirfsg__pb2.PerformPowerSearchRequest.SerializeToString,
            nirfsg__pb2.PerformPowerSearchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PerformThermalCorrection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/PerformThermalCorrection',
            nirfsg__pb2.PerformThermalCorrectionRequest.SerializeToString,
            nirfsg__pb2.PerformThermalCorrectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryArbWaveformCapabilities(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/QueryArbWaveformCapabilities',
            nirfsg__pb2.QueryArbWaveformCapabilitiesRequest.SerializeToString,
            nirfsg__pb2.QueryArbWaveformCapabilitiesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadAndDownloadWaveformFromFileTDMS(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ReadAndDownloadWaveformFromFileTDMS',
            nirfsg__pb2.ReadAndDownloadWaveformFromFileTDMSRequest.SerializeToString,
            nirfsg__pb2.ReadAndDownloadWaveformFromFileTDMSResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Reset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/Reset',
            nirfsg__pb2.ResetRequest.SerializeToString,
            nirfsg__pb2.ResetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResetAttribute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ResetAttribute',
            nirfsg__pb2.ResetAttributeRequest.SerializeToString,
            nirfsg__pb2.ResetAttributeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResetDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ResetDevice',
            nirfsg__pb2.ResetDeviceRequest.SerializeToString,
            nirfsg__pb2.ResetDeviceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResetWithDefaults(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ResetWithDefaults',
            nirfsg__pb2.ResetWithDefaultsRequest.SerializeToString,
            nirfsg__pb2.ResetWithDefaultsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResetWithOptions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/ResetWithOptions',
            nirfsg__pb2.ResetWithOptionsRequest.SerializeToString,
            nirfsg__pb2.ResetWithOptionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RevisionQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/RevisionQuery',
            nirfsg__pb2.RevisionQueryRequest.SerializeToString,
            nirfsg__pb2.RevisionQueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SaveConfigurationsToFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/SaveConfigurationsToFile',
            nirfsg__pb2.SaveConfigurationsToFileRequest.SerializeToString,
            nirfsg__pb2.SaveConfigurationsToFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SelectArbWaveform(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/SelectArbWaveform',
            nirfsg__pb2.SelectArbWaveformRequest.SerializeToString,
            nirfsg__pb2.SelectArbWaveformResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SelfCal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/SelfCal',
            nirfsg__pb2.SelfCalRequest.SerializeToString,
            nirfsg__pb2.SelfCalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SelfCalibrateRange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/SelfCalibrateRange',
            nirfsg__pb2.SelfCalibrateRangeRequest.SerializeToString,
            nirfsg__pb2.SelfCalibrateRangeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SelfTest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/SelfTest',
            nirfsg__pb2.SelfTestRequest.SerializeToString,
            nirfsg__pb2.SelfTestResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendSoftwareEdgeTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/SendSoftwareEdgeTrigger',
            nirfsg__pb2.SendSoftwareEdgeTriggerRequest.SerializeToString,
            nirfsg__pb2.SendSoftwareEdgeTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetArbWaveformNextWritePosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/SetArbWaveformNextWritePosition',
            nirfsg__pb2.SetArbWaveformNextWritePositionRequest.SerializeToString,
            nirfsg__pb2.SetArbWaveformNextWritePositionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAttributeViBoolean(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/SetAttributeViBoolean',
            nirfsg__pb2.SetAttributeViBooleanRequest.SerializeToString,
            nirfsg__pb2.SetAttributeViBooleanResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAttributeViInt32(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/SetAttributeViInt32',
            nirfsg__pb2.SetAttributeViInt32Request.SerializeToString,
            nirfsg__pb2.SetAttributeViInt32Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAttributeViInt64(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/SetAttributeViInt64',
            nirfsg__pb2.SetAttributeViInt64Request.SerializeToString,
            nirfsg__pb2.SetAttributeViInt64Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAttributeViReal64(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/SetAttributeViReal64',
            nirfsg__pb2.SetAttributeViReal64Request.SerializeToString,
            nirfsg__pb2.SetAttributeViReal64Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAttributeViSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/SetAttributeViSession',
            nirfsg__pb2.SetAttributeViSessionRequest.SerializeToString,
            nirfsg__pb2.SetAttributeViSessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAttributeViString(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/SetAttributeViString',
            nirfsg__pb2.SetAttributeViStringRequest.SerializeToString,
            nirfsg__pb2.SetAttributeViStringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetUserData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/SetUserData',
            nirfsg__pb2.SetUserDataRequest.SerializeToString,
            nirfsg__pb2.SetUserDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetWaveformBurstStartLocations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/SetWaveformBurstStartLocations',
            nirfsg__pb2.SetWaveformBurstStartLocationsRequest.SerializeToString,
            nirfsg__pb2.SetWaveformBurstStartLocationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetWaveformBurstStopLocations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/SetWaveformBurstStopLocations',
            nirfsg__pb2.SetWaveformBurstStopLocationsRequest.SerializeToString,
            nirfsg__pb2.SetWaveformBurstStopLocationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetWaveformMarkerEventLocations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/SetWaveformMarkerEventLocations',
            nirfsg__pb2.SetWaveformMarkerEventLocationsRequest.SerializeToString,
            nirfsg__pb2.SetWaveformMarkerEventLocationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WaitUntilSettled(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/WaitUntilSettled',
            nirfsg__pb2.WaitUntilSettledRequest.SerializeToString,
            nirfsg__pb2.WaitUntilSettledResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteArbWaveform(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/WriteArbWaveform',
            nirfsg__pb2.WriteArbWaveformRequest.SerializeToString,
            nirfsg__pb2.WriteArbWaveformResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteArbWaveformComplexF32(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/WriteArbWaveformComplexF32',
            nirfsg__pb2.WriteArbWaveformComplexF32Request.SerializeToString,
            nirfsg__pb2.WriteArbWaveformComplexF32Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteArbWaveformComplexF64(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/WriteArbWaveformComplexF64',
            nirfsg__pb2.WriteArbWaveformComplexF64Request.SerializeToString,
            nirfsg__pb2.WriteArbWaveformComplexF64Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteArbWaveformComplexI16(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/WriteArbWaveformComplexI16',
            nirfsg__pb2.WriteArbWaveformComplexI16Request.SerializeToString,
            nirfsg__pb2.WriteArbWaveformComplexI16Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteArbWaveformF32(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/WriteArbWaveformF32',
            nirfsg__pb2.WriteArbWaveformF32Request.SerializeToString,
            nirfsg__pb2.WriteArbWaveformF32Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteScript(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nirfsg_grpc.NiRFSG/WriteScript',
            nirfsg__pb2.WriteScriptRequest.SerializeToString,
            nirfsg__pb2.WriteScriptResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
````
