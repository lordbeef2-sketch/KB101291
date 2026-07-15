# NI PYTHON API DIGEST: nitypes-python

<!--NI_PYTHON_API_SNAPSHOT repo=ni/nitypes-python commit=2744270de1437c671fecc48b9f8ebc17a8343cda -->

<!--NI_PYTHON_API repo=nitypes-python path=docs/conf.py -->
## PYTHON MODULE: docs/conf.py

### MODULE DOCSTRING

Sphinx Configuration File.

### `def skip_aliases(app, what, name, obj, skip, options)`

Skip documentation for classes that are exported from multiple modules.

### `def setup(sphinx)`

Sphinx setup callback.

<!--NI_PYTHON_API repo=nitypes-python path=examples/placeholder.py -->
## PYTHON MODULE: examples/placeholder.py

### MODULE DOCSTRING

Temporary placeholder example.

<!--NI_PYTHON_API repo=nitypes-python path=scripts/pin_oldest_deps.py -->
## PYTHON MODULE: scripts/pin_oldest_deps.py

### MODULE DOCSTRING

Pin dependencies to the oldest compatible version for testing.

### `def main(args: list[str]) -> int | str | None`

Pin dependencies to the oldest compatible version for testing.

### `def _pin_oldest_for_deps_list(deps_list: AbstractTable) -> None`

### `def _remove_duplicate_dev_deps(poetry_deps: AbstractTable, dev_deps: AbstractTable) -> None`

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/__init__.py -->
## PYTHON MODULE: src/nitypes/__init__.py

### MODULE DOCSTRING

Data types for NI Python APIs.

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/_arguments.py -->
## PYTHON MODULE: src/nitypes/_arguments.py

### `def arg_to_float(arg_description: str, value: SupportsFloat | None, default_value: float | None=None) -> float`

Convert an argument to a float.

    >>> arg_to_float("xyz", 1.234)
    1.234
    >>> arg_to_float("xyz", 1234)
    1234.0
    >>> arg_to_float("xyz", np.float64(1.234))
    np.float64(1.234)
    >>> arg_to_float("xyz", np.float32(1.234))  # doctest: +ELLIPSIS
    1.233999...
    >>> arg_to_float("xyz", 1.234, 5.0)
    1.234
    >>> arg_to_float("xyz", None, 5.0)
    5.0
    >>> arg_to_float("xyz", None)
    Traceback (most recent call last):
    ...
    TypeError: The xyz must be a floating point number.
    <BLANKLINE>
    Provided value: None
    >>> arg_to_float("xyz", "1.234")
    Traceback (most recent call last):
    ...
    TypeError: The xyz must be a floating point number.
    <BLANKLINE>
    Provided value: '1.234'
    

### `def arg_to_int(arg_description: str, value: SupportsIndex | None, default_value: int | None=None) -> int`

Convert an argument to a signed integer.

    >>> arg_to_int("xyz", 1234)
    1234
    >>> arg_to_int("xyz", 1234, -1)
    1234
    >>> arg_to_int("xyz", None, -1)
    -1
    >>> arg_to_int("xyz", None)
    Traceback (most recent call last):
    ...
    TypeError: The xyz must be an integer.
    <BLANKLINE>
    Provided value: None
    >>> arg_to_int("xyz", 1.234)
    Traceback (most recent call last):
    ...
    TypeError: The xyz must be an integer.
    <BLANKLINE>
    Provided value: 1.234
    >>> arg_to_int("xyz", "1234")
    Traceback (most recent call last):
    ...
    TypeError: The xyz must be an integer.
    <BLANKLINE>
    Provided value: '1234'
    

### `def arg_to_uint(arg_description: str, value: SupportsIndex | None, default_value: int | None=None) -> int`

Convert an argument to an unsigned integer.

    >>> arg_to_uint("xyz", 1234)
    1234
    >>> arg_to_uint("xyz", 1234, 5000)
    1234
    >>> arg_to_uint("xyz", None, 5000)
    5000
    >>> arg_to_uint("xyz", -1234)
    Traceback (most recent call last):
    ...
    ValueError: The xyz must be a non-negative integer.
    <BLANKLINE>
    Provided value: -1234
    >>> arg_to_uint("xyz", "1234")
    Traceback (most recent call last):
    ...
    TypeError: The xyz must be an integer.
    <BLANKLINE>
    Provided value: '1234'
    

### `def is_dtype(dtype: npt.DTypeLike, supported_dtypes: tuple[npt.DTypeLike, ...]) -> bool`

Check a dtype-like object against a tuple of supported dtype-like objects.

    Unlike :any:`numpy.isdtype`, this function supports structured data types.

    >>> is_dtype(np.float64, (np.float64, np.intc, np.long,))
    True
    >>> is_dtype("float64", (np.float64, np.intc, np.long,))
    True
    >>> is_dtype(np.float64, (np.byte, np.short, np.intc, np.int_, np.long, np.longlong))
    False
    >>> a_type = np.dtype([('a', np.int32)])
    >>> b_type = np.dtype([('b', np.int32)])
    >>> is_dtype(a_type, (np.float64, np.int32, a_type,))
    True
    >>> is_dtype(b_type, (np.float64, np.int32, a_type,))
    False
    >>> is_dtype("i2, i2", (np.float64, np.int32, a_type,))
    False
    >>> is_dtype("i4", (np.float64, np.int32, a_type,))
    True
    

### `def validate_dtype(dtype: npt.DTypeLike, supported_dtypes: tuple[npt.DTypeLike, ...]) -> None`

Validate a dtype-like object against a tuple of supported dtype-like objects.

    >>> validate_dtype(np.float64, (np.float64, np.intc, np.long,))
    >>> validate_dtype("float64", (np.float64, np.intc, np.long,))
    >>> validate_dtype(np.float64, (np.byte, np.short, np.intc, np.int_, np.long, np.longlong))
    Traceback (most recent call last):
    ...
    TypeError: The requested data type is not supported.
    <BLANKLINE>
    Data type: float64
    Supported data types: int8, int16, int32, int64
    >>> a_type = np.dtype([('a', np.int32)])
    >>> b_type = np.dtype([('b', np.int32)])
    >>> validate_dtype(a_type, (np.float64, np.int32, a_type,))
    >>> validate_dtype(b_type, (np.float64, np.int32, a_type,))
    Traceback (most recent call last):
    ...
    TypeError: The requested data type is not supported.
    <BLANKLINE>
    Data type: [('b', '<i4')]
    Supported data types: float64, int32, void32
    

### `def validate_unsupported_arg(arg_description: str, value: object) -> None`

Validate that an unsupported argument is None.

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/_exceptions.py -->
## PYTHON MODULE: src/nitypes/_exceptions.py

### `def add_note(exception: Exception, note: str) -> None`

Add a note to an exception.

    >>> try:
    ...     raise ValueError("Oh no")
    ... except Exception as e:
    ...     add_note(e, "p.s. This is bad")
    ...     raise
    Traceback (most recent call last):
    ...
    ValueError: Oh no
    p.s. This is bad
    

### `def invalid_arg_value(arg_description: str, valid_value_description: str, value: object) -> ValueError`

Create a ValueError for an invalid argument value.

### `def invalid_arg_type(arg_description: str, type_description: str, value: object) -> TypeError`

Create a TypeError for an invalid argument type.

### `def invalid_array_ndim(arg_description: str, valid_value_description: str, ndim: int) -> ValueError`

Create a ValueError for an array with an invalid number of dimensions.

### `def invalid_requested_type(type_description: str, requested_type: type) -> TypeError`

Create a TypeError for an invalid requested type.

### `def unsupported_arg(arg_description: str, value: object) -> ValueError`

Create a ValueError for an unsupported argument.

### `def unsupported_dtype(arg_description: str, dtype: npt.DTypeLike, supported_dtypes: tuple[npt.DTypeLike, ...]) -> TypeError`

Create a TypeError for an unsupported dtype.

### `def int_out_of_range(value: int, min: int, max: int) -> OverflowError`

Create an OverflowError when an int is out of the specified range.

### `def _a(noun: str) -> str`

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/_numpy.py -->
## PYTHON MODULE: src/nitypes/_numpy.py

### MODULE DOCSTRING

NumPy 1.x compatibility shims.

- `__all__ = ['asarray', 'bool', 'isdtype', 'long', 'numpy_version_info', 'ulong']`

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/_numpy1x.py -->
## PYTHON MODULE: src/nitypes/_numpy1x.py

### MODULE DOCSTRING

NumPy 1.x compatibility shim implementations.

- `__all__ = ['asarray', 'bool', 'isdtype', 'long', 'ulong']`

### `def asarray(a: npt.ArrayLike, dtype: npt.DTypeLike | None=None, *, copy: builtins.bool | None=None) -> npt.NDArray[Any]`

### `def isdtype(dtype: type[Any] | np.dtype[Any], kind: npt.DTypeLike | tuple[npt.DTypeLike, ...]) -> builtins.bool`

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/_version.py -->
## PYTHON MODULE: src/nitypes/_version.py

### `def parse_version(version: str) -> tuple[int, int, int]`

Parse a version number into a major/minor/update tuple, ignoring suffixes.

    This is a minimal version parser to avoid requiring the ``packaging`` package.

    >>> parse_version("1.2.3")
    (1, 2, 3)
    >>> parse_version("123.456.789")
    (123, 456, 789)
    >>> parse_version("1.0")
    (1, 0, 0)
    >>> parse_version("1")
    (1, 0, 0)
    >>> parse_version("1.2.3-dev0")
    (1, 2, 3)
    

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/bintime/__init__.py -->
## PYTHON MODULE: src/nitypes/bintime/__init__.py

### MODULE DOCSTRING

Binary time data types for NI Python APIs.

NI Binary Time Format
=====================

This module implements the NI Binary Time Format (`NI-BTF`_), a high-resolution time format used by
NI software.

An NI-BTF time value is a 128-bit fixed point number consisting of a 64-bit whole seconds part and a
64-bit fractional seconds part. There are two types of NI-BTF time values:

* An NI-BTF absolute time represents a point in time as the number of seconds after midnight,
  January 1, 1904, UTC.
* An NI-BTF time interval represents a difference between two points in time.

NI-BTF time types are also supported in LabVIEW, LabWindows/CVI, and .NET. You can use NI-BTF time
to efficiently share high-resolution date-time information with other NI application development
environments.

.. _ni-btf: https://www.ni.com/docs/en-US/bundle/labwindows-cvi/page/cvi/libref/ni-btf.htm

NI-BTF Python Data Types
========================

* :class:`DateTime`: represents an NI-BTF absolute time as a Python object.
* :class:`DateTimeArray`: an array of :class:`DateTime` values.
* :class:`TimeDelta`: represents a NI-BTF time interval as a Python object.
* :class:`TimeDeltaArray`: an array of :class:`TimeDelta` values.

NI-BTF NumPy Structured Data Types
==================================

:any:`CVIAbsoluteTimeDType` and :any:`CVITimeIntervalDType` are NumPy structured data type objects
representing the ``CVIAbsoluteTime`` and ``CVITimeInterval`` C structs. These structured data types
can be used to efficiently represent NI-BTF time values in NumPy arrays or pass them to/from C DLLs.

.. warning::
    :any:`CVIAbsoluteTimeDType` and :any:`CVITimeIntervalDType` have the same layout and field
    names, so NumPy and type checkers such as Mypy currently treat them as the same type.

NI-BTF versus ``hightime``
==========================

NI also provides the ``hightime`` Python package, which extends the standard Python :mod:`datetime`
module to support up to yoctosecond precision.

``nitypes.bintime`` is not a replacement for ``hightime``. The two time formats have different
strengths and weaknesses.

* ``hightime`` supports local time zones and time-zone-naive times. ``bintime`` only supports UTC.
* ``hightime`` classes supports the same operations as the standard ``datetime`` classes.
  ``bintime`` classes support a subset of the standard ``datetime`` operations.
* ``hightime`` has a larger memory footprint than NI-BTF. ``hightime`` objects are separately
  allocated from the heap. ``bintime`` offers the choice of separately allocated Python objects or
  a more compact NumPy representation that can store multiple timestamps in a single block of
  memory.
* ``hightime`` requires conversion to/from NI-BTF when calling the NI driver C APIs from Python.
  ``nitypes.bintime`` includes reusable conversion routines for NI driver Python APIs to use.

NI-BTF versus :any:`numpy.datetime64`
=====================================

NumPy provides the :any:`numpy.datetime64` data type, which is even more compact than NI-BTF.
However, it has lower resolution than NI-BTF and is not interoperable with NI driver C APIs that use
NI-BTF.


- `__all__ = ['DateTime', 'DateTimeArray', 'CVIAbsoluteTimeBase', 'CVIAbsoluteTimeDType', 'CVITimeIntervalBase', 'CVITimeIntervalDType', 'TimeDelta', 'TimeDeltaArray', 'TimeValueTuple']`

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/bintime/_datetime.py -->
## PYTHON MODULE: src/nitypes/bintime/_datetime.py

- `_DT_EPOCH_1904 = dt.datetime(1904, 1, 1, tzinfo=dt.timezone.utc)`

- `_HT_EPOCH_1904 = ht.datetime(1904, 1, 1, tzinfo=dt.timezone.utc)`

- `_OTHER_DATETIME_TUPLE = (dt.datetime, ht.datetime)`

### `class DateTime()`

An absolute time in NI Binary Time Format (NI-BTF).

    DateTime represents time as a 128-bit fixed point number with 64-bit whole seconds and
    64-bit fractional seconds.

    .. warning::
        The fractional seconds are represented as a binary fraction, which is a sum of inverse
        powers of 2. Values that are not exactly representable as binary fractions will display
        rounding error or "bruising" similar to a floating point number.

    DateTime instances are duck typing compatible with a subset of the method and properties
    supported by :any:`datetime.datetime` and :any:`hightime.datetime`.

    This class only supports the UTC time zone and does not support timezone-naive times.

    This class does not support the ``fold`` property for disambiguating repeated times for daylight
    saving time and time zone changes.

    Constructing
    ^^^^^^^^^^^^

    As with :any:`datetime.datetime`, you can construct a :class:`DateTime` by specifying the year,
    month, day, etc.:

    >>> import datetime
    >>> DateTime(2025, 5, 25, 16, 45, tzinfo=datetime.timezone.utc)
    nitypes.bintime.DateTime(2025, 5, 25, 16, 45, tzinfo=datetime.timezone.utc)

    .. note::
        :class:`DateTime` only supports :any:`datetime.timezone.utc`. It does not support time-zone-naive
        objects or time zones other than UTC.

    You can also construct a :class:`DateTime` from a :any:`datetime.datetime` or
    :any:`hightime.datetime`:

    >>> DateTime(datetime.datetime(2025, 5, 25, 16, 45, tzinfo=datetime.timezone.utc))
    nitypes.bintime.DateTime(2025, 5, 25, 16, 45, tzinfo=datetime.timezone.utc)
    >>> import hightime
    >>> DateTime(hightime.datetime(2025, 5, 25, 16, 45, tzinfo=datetime.timezone.utc))
    nitypes.bintime.DateTime(2025, 5, 25, 16, 45, tzinfo=datetime.timezone.utc)

    You can get the current time of day by calling :any:`DateTime.now`:

    >>> DateTime.now(datetime.timezone.utc) # doctest: +ELLIPSIS
    nitypes.bintime.DateTime(...)

    Properties
    ^^^^^^^^^^

    Like other ``datetime`` objects, :class:`DateTime` has properties for the year, month, day, hour,
    minute, second, and microsecond.

    >>> import datetime
    >>> x = DateTime(datetime.datetime(2025, 5, 25, 16, 45, tzinfo=datetime.timezone.utc))
    >>> (x.year, x.month, x.day)
    (2025, 5, 25)
    >>> (x.hour, x.minute, x.second, x.microsecond)
    (16, 45, 0, 0)

    Like :any:`hightime.datetime`, it also supports the femtosecond and yoctosecond properties.

    >>> (x.femtosecond, x.yoctosecond)
    (0, 0)

    Resolution
    ^^^^^^^^^^

    NI-BTF is a high-resolution time format, so it has significantly higher resolution than
    :any:`datetime.datetime`. However, :any:`hightime.datetime` has even higher resolution:

    ========================   ================================
    Class                      Smallest Time Increment
    ========================   ================================
    :any:`datetime.datetime`   1 microsecond (1e-6 sec)
    :class:`DateTime`            54210 yoctoseconds (5.4e-20 sec)
    :any:`hightime.datetime`   1 yoctosecond (1e-24 sec)
    ========================   ================================

    As a result, :any:`hightime.datetime` can represent the time down to the exact yoctosecond, but
    :class:`DateTime` rounds the yoctosecond field.

    >>> import hightime
    >>> x = hightime.datetime(2025, 1, 1, yoctosecond=123456789, tzinfo=datetime.timezone.utc)
    >>> x
    hightime.datetime(2025, 1, 1, 0, 0, 0, 0, 0, 123456789, tzinfo=datetime.timezone.utc)
    >>> DateTime(x) # doctest: +NORMALIZE_WHITESPACE
    nitypes.bintime.DateTime(2025, 1, 1, 0, 0, 0, 0, 0, 123436417, tzinfo=datetime.timezone.utc)

    Rounding
    ^^^^^^^^

    NI-BTF represents fractional seconds as a binary fraction, which is a sum of inverse
    powers of 2. Values that are not exactly representable as binary fractions will display
    rounding error or "bruising" similar to a floating point number.

    For example, it may round 100 microseconds down to 99.9999... microseconds.

    >>> x = hightime.datetime(2025, 1, 1, microsecond=100, tzinfo=datetime.timezone.utc)
    >>> x
    hightime.datetime(2025, 1, 1, 0, 0, 0, 100, tzinfo=datetime.timezone.utc)
    >>> DateTime(x) # doctest: +NORMALIZE_WHITESPACE
    nitypes.bintime.DateTime(2025, 1, 1, 0, 0, 0, 99, 999999999, 999991239,
        tzinfo=datetime.timezone.utc)

    Class members
    ^^^^^^^^^^^^^
    

#### `def __init__(self) -> None`

#### `def __init__(self, value: _OtherDateTime, /) -> None`

#### `def __init__(self, year: SupportsIndex, month: SupportsIndex, day: SupportsIndex, hour: SupportsIndex=..., minute: SupportsIndex=..., second: SupportsIndex=..., microsecond: SupportsIndex=..., femtosecond: SupportsIndex=..., yoctosecond: SupportsIndex=..., tzinfo: dt.tzinfo | None=None) -> None`

#### `def __init__(self, year: SupportsIndex | _OtherDateTime | None=None, month: SupportsIndex | None=None, day: SupportsIndex | None=None, hour: SupportsIndex=0, minute: SupportsIndex=0, second: SupportsIndex=0, microsecond: SupportsIndex=0, femtosecond: SupportsIndex=0, yoctosecond: SupportsIndex=0, tzinfo: dt.tzinfo | None=None) -> None`

Initialize a DateTime.

#### `def _to_offset(cls, value: object) -> TimeDelta`

#### `def _(cls, value: ht.datetime) -> TimeDelta`

#### `def _(cls, value: dt.datetime) -> TimeDelta`

#### `def _(cls, value: None) -> TimeDelta`

#### `def from_ticks(cls, ticks: SupportsIndex) -> Self`

Create an DateTime from a 128-bit fixed point number expressed as an integer.

#### `def from_tuple(cls, value: TimeValueTuple) -> Self`

Create a DateTime from whole and fractional seconds as 64-bit ints.

#### `def from_offset(cls, offset: TimeDelta) -> Self`

Create an DateTime from a TimeValue offset from the epoch, Jan 1, 1904.

#### `def _to_datetime_datetime(self) -> dt.datetime`

Return self as a :any:`datetime.datetime`.

#### `def _to_hightime_datetime(self) -> ht.datetime`

Return self as a :any:`hightime.datetime`.

#### `def year(self) -> int`

The year.

#### `def month(self) -> int`

The month, between 1 and 12 inclusive.

#### `def day(self) -> int`

The day of the month, between 1 and 31 inclusive.

#### `def hour(self) -> int`

The hour, between 0 and 23 inclusive.

#### `def minute(self) -> int`

The minute, between 0 and 59 inclusive.

#### `def second(self) -> int`

The second, between 0 and 59 inclusive.

#### `def microsecond(self) -> int`

The microsecond, between 0 and 999_999 inclusive.

#### `def femtosecond(self) -> int`

The femtosecond, between 0 and 999_999_999 inclusive.

#### `def yoctosecond(self) -> int`

The yoctosecond, between 0 and 999_999_999 inclusive.

        .. warning::
            Because this class uses a 64-bit binary fraction, the smallest time increment it can
            represent is ``1.0 / (1 << 64)`` seconds, which is about 54210 yoctoseconds.
        

#### `def ticks(self) -> int`

The number of ticks since the epoch, Jan 1, 1904.

#### `def tzinfo(self) -> dt.tzinfo | None`

The time zone.

#### `def to_tuple(self) -> TimeValueTuple`

Convert to the number of whole and fractional seconds since the epoch, Jan 1, 1904.

#### `def now(cls, tz: dt.tzinfo | None=None) -> Self`

Return the current absolute time.

#### `def __add__(self, value: TimeDelta | _OtherTimeDelta, /) -> DateTime`

Return self+value.

#### `def __sub__(self, value: DateTime | _OtherDateTime, /) -> TimeDelta`

#### `def __sub__(self, value: TimeDelta | _OtherTimeDelta, /) -> DateTime`

#### `def __sub__(self, value: DateTime | _OtherDateTime | TimeDelta | _OtherTimeDelta, /) -> TimeDelta | DateTime`

Return self-value.

#### `def __rsub__(self, value: DateTime | _OtherDateTime, /) -> TimeDelta`

#### `def __rsub__(self, value: TimeDelta | _OtherTimeDelta, /) -> DateTime`

#### `def __rsub__(self, value: DateTime | _OtherDateTime | TimeDelta | _OtherTimeDelta, /) -> TimeDelta | DateTime`

Return value-self.

#### `def __lt__(self, value: DateTime | _OtherDateTime, /) -> bool`

Return self<value.

#### `def __le__(self, value: DateTime | _OtherDateTime, /) -> bool`

Return self<=value.

#### `def __eq__(self, value: object, /) -> bool`

Return self==value.

#### `def __gt__(self, value: DateTime | _OtherDateTime, /) -> bool`

Return self<value.

#### `def __ge__(self, value: DateTime | _OtherDateTime, /) -> bool`

Return self>=value.

#### `def __hash__(self) -> int`

Return hash(self).

#### `def __reduce__(self) -> tuple[Any, ...]`

Return object state for pickling.

#### `def __str__(self) -> str`

Return repr(self).

#### `def __repr__(self) -> str`

Return repr(self).

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/bintime/_datetime_array.py -->
## PYTHON MODULE: src/nitypes/bintime/_datetime_array.py

### `class DateTimeArray(MutableSequence[DateTime])`

A mutable array of :class:`DateTime` values in NI Binary Time Format (NI-BTF).

    Raises:
        TypeError: If any item in value is not a DateTime instance.
    

#### `def __init__(self, value: Iterable[DateTime] | None=None) -> None`

Initialize a new DateTimeArray.

#### `def __getitem__(self, index: int) -> DateTime`

#### `def __getitem__(self, index: slice) -> DateTimeArray`

#### `def __getitem__(self, index: int | slice) -> DateTime | DateTimeArray`

Return self[index].

        Raises:
            TypeError: If index is an invalid type.
            IndexError: If index is out of range.
        

#### `def __len__(self) -> int`

Return len(self).

#### `def __setitem__(self, index: int, value: DateTime) -> None`

#### `def __setitem__(self, index: slice, value: Iterable[DateTime]) -> None`

#### `def __setitem__(self, index: int | slice, value: DateTime | Iterable[DateTime]) -> None`

Set a new value for DateTime at the specified location or slice.

        Raises:
            TypeError: If index is an invalid type, or slice value is not iterable.
            ValueError: If slice assignment length doesn't match the selected range.
            IndexError: If index is out of range.
        

#### `def __delitem__(self, index: int) -> None`

#### `def __delitem__(self, index: slice) -> None`

#### `def __delitem__(self, index: int | slice) -> None`

Delete the value at the specified location or slice.

        Raises:
            TypeError: If index is an invalid type.
            IndexError: If index is out of range.
        

#### `def insert(self, index: int, value: DateTime) -> None`

Insert the DateTime value before the specified index.

        Raises:
            TypeError: If index is not int or value is not DateTime.
        

#### `def extend(self, values: Iterable[DateTime]) -> None`

Extend the array by appending the elements from values.

#### `def __eq__(self, other: object) -> bool`

Return self == other.

#### `def __reduce__(self) -> tuple[Any, ...]`

Return object state for pickling.

#### `def __repr__(self) -> str`

Return repr(self).

#### `def __str__(self) -> str`

Return str(self).

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/bintime/_time_value_tuple.py -->
## PYTHON MODULE: src/nitypes/bintime/_time_value_tuple.py

### `class TimeValueTuple(NamedTuple)`

A named tuple containing the whole seconds and fractional seconds parts of a time value.

#### `def from_cvi(lsb: int, msb: int) -> TimeValueTuple`

Create a :class:`TimeValueTuple` from a ``CVIAbsoluteTime`` representation.

#### `def to_cvi(self) -> tuple[int, int]`

Return a representation as ``CVIAbsoluteTime``.

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/bintime/_timedelta.py -->
## PYTHON MODULE: src/nitypes/bintime/_timedelta.py

- `_INT64_MAX = (1 << 63) - 1`

- `_INT64_MIN = -(1 << 63)`

- `_UINT64_MAX = (1 << 64) - 1`

- `_UINT64_MIN = 0`

- `_INT128_MAX = (1 << 127) - 1`

- `_INT128_MIN = -(1 << 127)`

- `_BITS_PER_SECOND = 64`

- `_TICKS_PER_SECOND = 1 << _BITS_PER_SECOND`

- `_FRACTIONAL_SECONDS_MASK = _TICKS_PER_SECOND - 1`

- `_SECONDS_PER_DAY = 86400`

- `_MICROSECONDS_PER_SECOND = 10 ** 6`

- `_FEMTOSECONDS_PER_SECOND = 10 ** 15`

- `_YOCTOSECONDS_PER_SECOND = 10 ** 24`

- `_FEMTOSECONDS_PER_MICROSECOND = _FEMTOSECONDS_PER_SECOND // _MICROSECONDS_PER_SECOND`

- `_YOCTOSECONDS_PER_FEMTOSECOND = _YOCTOSECONDS_PER_SECOND // _FEMTOSECONDS_PER_SECOND`

- `_DECIMAL_DIGITS = 64`

- `_REPR_TICKS = False`

- `_OTHER_TIMEDELTA_TUPLE = (dt.timedelta, ht.timedelta)`

### `class TimeDelta()`

A duration, represented in NI Binary Time Format (NI-BTF).

    TimeDelta represents time as a 128-bit fixed point number with 64-bit whole seconds and 64-bit
    fractional seconds.

    .. warning::
        The fractional seconds are represented as a binary fraction, which is a sum of inverse
        powers of 2. Values that are not exactly representable as binary fractions will display
        rounding error or "bruising" similar to a floating point number.

    TimeDelta instances are duck typing compatible with :any:`datetime.timedelta` and
    :any:`hightime.timedelta`.

    Constructing
    ^^^^^^^^^^^^

    You can construct a :class:`TimeDelta` from a number of seconds, expressed as an :any:`int`,
    :any:`float`, or :any:`decimal.Decimal`.

    >>> TimeDelta(100)
    nitypes.bintime.TimeDelta(Decimal('100'))
    >>> TimeDelta(100.125)
    nitypes.bintime.TimeDelta(Decimal('100.125'))
    >>> from decimal import Decimal
    >>> TimeDelta(Decimal("100.125"))
    nitypes.bintime.TimeDelta(Decimal('100.125'))

    :class:`TimeDelta` has the same resolution and rounding behavior as :class:`DateTime`.

    >>> TimeDelta(Decimal("100.01234567890123456789"))
    nitypes.bintime.TimeDelta(Decimal('100.012345678901234567889'))

    Unlike other ``timedelta`` objects, you cannot construct a :class:`TimeDelta` from separate weeks,
    days, hours, etc. If you want to do that, construct a :any:`datetime.timedelta` or
    :any:`hightime.timedelta` and then use it to construct a :class:`TimeDelta`.

    >>> import datetime, hightime
    >>> TimeDelta(datetime.timedelta(days=1, microseconds=1))
    nitypes.bintime.TimeDelta(Decimal('86400.0000010000000000000'))
    >>> TimeDelta(hightime.timedelta(days=1, femtoseconds=1))
    nitypes.bintime.TimeDelta(Decimal('86400.0000000000000010000'))

    Math Operations
    ^^^^^^^^^^^^^^^

    :class:`DateTime` and :class:`TimeDelta` support the same math operations as :any:`datetime.datetime`
    and :any:`datetime.timedelta`.

    For example, you can add or subtract :class:`TimeDelta` objects together:

    >>> TimeDelta(100.5) + TimeDelta(0.5)
    nitypes.bintime.TimeDelta(Decimal('101'))
    >>> TimeDelta(100.5) - TimeDelta(0.5)
    nitypes.bintime.TimeDelta(Decimal('100'))

    Or add/subtract a :class:`DateTime` with a :class:`TimeDelta`, :any:`datetime.timedelta`, or
    :any:`hightime.timedelta`:

    >>> DateTime(2025, 1, 1, tzinfo=datetime.timezone.utc) + TimeDelta(86400)
    nitypes.bintime.DateTime(2025, 1, 2, 0, 0, tzinfo=datetime.timezone.utc)
    >>> DateTime(2025, 1, 1, tzinfo=datetime.timezone.utc) + datetime.timedelta(days=1)
    nitypes.bintime.DateTime(2025, 1, 2, 0, 0, tzinfo=datetime.timezone.utc)
    >>> DateTime(2025, 1, 1, tzinfo=datetime.timezone.utc) + hightime.timedelta(femtoseconds=1)
    nitypes.bintime.DateTime(2025, 1, 1, 0, 0, 0, 0, 1, 13873, tzinfo=datetime.timezone.utc)

    Class members
    ^^^^^^^^^^^^^
    

#### `def __init__(self) -> None`

#### `def __init__(self, value: _OtherTimeDelta, /) -> None`

#### `def __init__(self, seconds: SupportsIndex | Decimal | float) -> None`

#### `def __init__(self, seconds: SupportsIndex | Decimal | float | _OtherTimeDelta | None=None) -> None`

Initialize a TimeDelta.

#### `def _to_ticks(cls, seconds: object) -> int`

#### `def _(cls, seconds: SupportsIndex) -> int`

#### `def _(cls, seconds: Decimal) -> int`

#### `def _(cls, seconds: float) -> int`

#### `def _(cls, seconds: ht.timedelta) -> int`

#### `def _(cls, seconds: dt.timedelta) -> int`

#### `def _(cls, seconds: None) -> int`

#### `def from_ticks(cls, ticks: SupportsIndex) -> Self`

Create a TimeDelta from a 128-bit fixed point number expressed as an integer.

#### `def from_tuple(cls, value: TimeValueTuple) -> Self`

Create a TimeDelta from 64-bit whole seconds and fractional seconds ints.

#### `def _to_datetime_timedelta(self) -> dt.timedelta`

Return self as a :any:`datetime.timedelta`.

#### `def _to_hightime_timedelta(self) -> ht.timedelta`

Return self as a :any:`hightime.timedelta`.

#### `def days(self) -> int`

The number of days in the time delta.

#### `def seconds(self) -> int`

The number of seconds in the time delta, up to the nearest day.

#### `def microseconds(self) -> int`

The number of microseconds in the time delta, up to the nearest second.

#### `def femtoseconds(self) -> int`

The number of femtoseconds in the time delta, up to the nearest microsecond.

#### `def yoctoseconds(self) -> int`

The number of yoctoseconds in the time delta, up to the nearest femtosecond.

        .. warning::
            Because this class uses a 64-bit binary fraction, the smallest value it can represent
            is ``1.0 / (1 << 64)`` seconds, which is about 54210 yoctoseconds.
        

#### `def ticks(self) -> int`

The total ticks in the time delta as a 128-bit integer.

#### `def to_tuple(self) -> TimeValueTuple`

The whole seconds and fractional seconds parts of the time delta as 64-bit ints.

#### `def total_seconds(self) -> float`

The total seconds in the time delta.

        .. warning::
            Converting a time value to a floating point number loses precision. Consider using
            :any:`precision_total_seconds` instead.
        

#### `def precision_total_seconds(self) -> Decimal`

The precise total seconds in the time delta.

        Note: up to 64 significant digits are used in computation.
        

#### `def __neg__(self) -> TimeDelta`

Return -self.

#### `def __pos__(self) -> TimeDelta`

Return +self.

#### `def __abs__(self) -> TimeDelta`

Return abs(self).

#### `def __add__(self, value: TimeDelta | _OtherTimeDelta, /) -> TimeDelta`

#### `def __add__(self, value: ht.datetime, /) -> ht.datetime`

#### `def __add__(self, value: dt.datetime, /) -> dt.datetime`

#### `def __add__(self, value: TimeDelta | _OtherTimeDelta | _OtherDateTime, /) -> TimeDelta | _OtherDateTime`

Return self+value.

#### `def __sub__(self, value: TimeDelta | _OtherTimeDelta, /) -> TimeDelta`

Return self-value.

#### `def __rsub__(self, value: TimeDelta | _OtherTimeDelta, /) -> TimeDelta`

#### `def __rsub__(self, value: ht.datetime, /) -> ht.datetime`

#### `def __rsub__(self, value: dt.datetime, /) -> dt.datetime`

#### `def __rsub__(self, value: TimeDelta | _OtherTimeDelta | _OtherDateTime, /) -> TimeDelta | _OtherDateTime`

Return value-self.

#### `def __mul__(self, value: int | float | Decimal, /) -> TimeDelta`

Return self*value.

#### `def __floordiv__(self, value: TimeDelta, /) -> int`

#### `def __floordiv__(self, value: int, /) -> TimeDelta`

#### `def __floordiv__(self, value: TimeDelta | int, /) -> int | TimeDelta`

Return self//value.

#### `def __truediv__(self, value: TimeDelta, /) -> float`

#### `def __truediv__(self, value: float, /) -> TimeDelta`

#### `def __truediv__(self, value: TimeDelta | float, /) -> float | TimeDelta`

Return self/value.

#### `def __mod__(self, value: TimeDelta | _OtherTimeDelta, /) -> TimeDelta`

Return self%value.

#### `def __divmod__(self, value: TimeDelta | _OtherTimeDelta, /) -> tuple[int, TimeDelta]`

Return (self//value, self%value).

#### `def __lt__(self, value: TimeDelta | _OtherTimeDelta, /) -> bool`

Return self<value.

#### `def __le__(self, value: TimeDelta | _OtherTimeDelta, /) -> bool`

Return self<=value.

#### `def __eq__(self, value: object, /) -> bool`

Return self==value.

#### `def __gt__(self, value: TimeDelta | _OtherTimeDelta, /) -> bool`

Return self<value.

#### `def __ge__(self, value: TimeDelta | _OtherTimeDelta, /) -> bool`

Return self>=value.

#### `def __bool__(self) -> bool`

Return bool(self).

#### `def __hash__(self) -> int`

Return hash(self).

#### `def __reduce__(self) -> tuple[Any, ...]`

Return object state for pickling.

#### `def __str__(self) -> str`

Return repr(self).

#### `def __repr__(self) -> str`

Return repr(self).

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/bintime/_timedelta_array.py -->
## PYTHON MODULE: src/nitypes/bintime/_timedelta_array.py

### `class TimeDeltaArray(MutableSequence[TimeDelta])`

A mutable array of :class:`TimeDelta` values in NI Binary Time Format (NI-BTF).

    Raises:
        TypeError: If any item in value is not a TimeDelta instance.
    

#### `def __init__(self, value: Iterable[TimeDelta] | None=None) -> None`

Initialize a new TimeDeltaArray.

#### `def __getitem__(self, index: int) -> TimeDelta`

#### `def __getitem__(self, index: slice) -> TimeDeltaArray`

#### `def __getitem__(self, index: int | slice) -> TimeDelta | TimeDeltaArray`

Return self[index].

        Raises:
            TypeError: If index is an invalid type.
            IndexError: If index is out of range.
        

#### `def __len__(self) -> int`

Return len(self).

#### `def __setitem__(self, index: int, value: TimeDelta) -> None`

#### `def __setitem__(self, index: slice, value: Iterable[TimeDelta]) -> None`

#### `def __setitem__(self, index: int | slice, value: TimeDelta | Iterable[TimeDelta]) -> None`

Set a new value for TimeDelta at the specified location or slice.

        Raises:
            TypeError: If index is an invalid type, or slice value is not iterable.
            ValueError: If slice assignment length doesn't match the selected range.
            IndexError: If index is out of range.
        

#### `def __delitem__(self, index: int) -> None`

#### `def __delitem__(self, index: slice) -> None`

#### `def __delitem__(self, index: int | slice) -> None`

Delete the value at the specified location or slice.

        Raises:
            TypeError: If index is an invalid type.
            IndexError: If index is out of range.
        

#### `def insert(self, index: int, value: TimeDelta) -> None`

Insert the TimeDelta value before the specified index.

        Raises:
            TypeError: If index is not int or value is not TimeDelta.
        

#### `def extend(self, values: Iterable[TimeDelta]) -> None`

Extend the array by appending the elements from values.

#### `def __eq__(self, other: object) -> bool`

Return self == other.

#### `def __reduce__(self) -> tuple[Any, ...]`

Return object state for pickling.

#### `def __repr__(self) -> str`

Return repr(self).

#### `def __str__(self) -> str`

Return str(self).

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/complex/__init__.py -->
## PYTHON MODULE: src/nitypes/complex/__init__.py

### MODULE DOCSTRING

Complex number data types for NI Python APIs.

================
Complex Integers
================

Some NI driver APIs (such as NI-FGEN, NI-SCOPE, NI-RFSA, and NI-RFSG) use complex numbers to
represent I/Q data. Python and NumPy have native support for complex floating-point numbers, but
not complex integers, so the :mod:`nitypes.complex` submodule provides a NumPy representation of
complex integers.

:any:`ComplexInt32DType` is a NumPy structured data type object representing a complex integer with
16-bit ``real`` and ``imag`` fields. This structured data type has the same memory layout as the
``NIComplexI16`` C struct used by NI driver APIs.

For more information about NumPy structured data types, see the
:ref:`NumPy documentation on structured arrays <numpy:structured_arrays>`.

.. note::
   In ``NIComplexI16``, the number 16 refers to the number of bits in each field. In
   :any:`ComplexInt32DType`, the number 32 refers to the total number of bits, following the
   precedent set by NumPy's other complex types. For example, :any:`numpy.complex128` contains
   64-bit ``real`` and ``imag`` fields.

Constructing arrays of complex integers
---------------------------------------

You can construct an array of complex integers from a sequence of tuples using :func:`numpy.array`:

>>> import numpy as np
>>> np.array([(1, 2), (3, 4)], dtype=ComplexInt32DType)
array([(1, 2), (3, 4)], dtype=[('real', '<i2'), ('imag', '<i2')])

Likewise, you can construct an array of complex integer zeros using :func:`numpy.zeros`:

>>> np.zeros(3, dtype=ComplexInt32DType)
array([(0, 0), (0, 0), (0, 0)], dtype=[('real', '<i2'), ('imag', '<i2')])

Indexing and slicing
--------------------

Indexing the array gives you a complex integer structured scalar:

>>> x = np.array([(1, 2), (3, 4), (5, 6)], dtype=ComplexInt32DType)
>>> x[0]
np.void((1, 2), dtype=[('real', '<i2'), ('imag', '<i2')])
>>> x[1]
np.void((3, 4), dtype=[('real', '<i2'), ('imag', '<i2')])

.. note:
    NumPy displays :any:`numpy.void` because the :any:`ComplexInt32DType` structured data type has
    a base type of :any:`numpy.void`. Using a different base type such as :any:`numpy.int32`
    would have benefits, such as making it easier to convert array elements to/from
    :any:`numpy.int32`, but it would also have drawbacks, such as making it harder to initialize
    the array using a sequence of tuples.

You can index a complex integer structured scalar to get the real and imaginary parts:

>>> x[0][0]
np.int16(1)
>>> x[0][1]
np.int16(2)

You can also index by the field names ``real`` and ``imag``:

>>> x[0]['real']
np.int16(1)
>>> x[0]['imag']
np.int16(2)

Or you can index the entire array by the field names ``real`` and ``imag``:

>>> x['real']
array([1, 3, 5], dtype=int16)
>>> x['imag']
array([2, 4, 6], dtype=int16)

Arrays of complex integers support slicing and negative indices like any other array:

>>> x[0:2]
array([(1, 2), (3, 4)], dtype=[('real', '<i2'), ('imag', '<i2')])
>>> x[1:]
array([(3, 4), (5, 6)], dtype=[('real', '<i2'), ('imag', '<i2')])
>>> x[-1]
np.void((5, 6), dtype=[('real', '<i2'), ('imag', '<i2')])

Conversion
----------

To convert a complex integer structured scalar to a tuple, use the :any:`numpy.ndarray.item`
method:

>>> x[0].item()
(1, 2)
>>> [y.item() for y in x]
[(1, 2), (3, 4), (5, 6)]

To convert NumPy arrays between between different complex number data types, use the
:func:`convert_complex` function:

>>> convert_complex(np.complex128, x)
array([1.+2.j, 3.+4.j, 5.+6.j])
>>> convert_complex(ComplexInt32DType, np.array([1.23+4.56j]))
array([(1, 4)], dtype=[('real', '<i2'), ('imag', '<i2')])

You can also use :func:`convert_complex` with NumPy scalars:

>>> convert_complex(np.complex128, x[0])
np.complex128(1+2j)
>>> convert_complex(ComplexInt32DType, np.complex128(3+4j))
np.void((3, 4), dtype=[('real', '<i2'), ('imag', '<i2')])

.. note::
    As of NumPy 2.2, shape typing is still under development, so its type hints do not reflect that
    many operations coerce zero-dimensional arrays to :any:`numpy.generic`. The type hints for the
    scalar overloads of :func:`convert_complex` follow this precedent and return an
    :any:`numpy.ndarray`. This behavior may change in a future release.

Mathematical operations
-----------------------

Structured arrays of complex integers do not support mathematical operations. Convert
them to arrays of complex floating-point numbers before doing any sort of math or analysis.


- `__all__ = ['convert_complex', 'ComplexInt32DType', 'ComplexInt32Base']`

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/complex/_conversion.py -->
## PYTHON MODULE: src/nitypes/complex/_conversion.py

- `_COMPLEX_DTYPES = (np.complex64, np.complex128, ComplexInt32DType)`

- `_FIELD_DTYPE = {np.dtype(np.complex64): np.float32, np.dtype(np.complex128): np.float64, ComplexInt32DType: np.int16}`

### `def convert_complex(requested_dtype: type[_ScalarType] | np.dtype[_ScalarType], value: np.ndarray[_Shape, Any]) -> np.ndarray[_Shape, np.dtype[_ScalarType]]`

### `def convert_complex(requested_dtype: npt.DTypeLike, value: np.ndarray[_Shape, Any]) -> np.ndarray[_Shape, Any]`

### `def convert_complex(requested_dtype: type[_ScalarType] | np.dtype[_ScalarType], value: np.generic[Any]) -> np.ndarray[tuple[()], np.dtype[_ScalarType]]`

### `def convert_complex(requested_dtype: npt.DTypeLike, value: np.generic[Any]) -> np.ndarray[tuple[()], Any]`

### `def convert_complex(requested_dtype: npt.DTypeLike, value: np.ndarray[_Shape, Any] | np.generic[Any]) -> np.ndarray[_Shape, Any]`

Convert a NumPy array or scalar of complex numbers to the specified dtype.

    Args:
        requested_dtype: The NumPy data type to convert to. Supported data types:
            :any:`numpy.complex64`, :any:`numpy.complex128`, :any:`ComplexInt32DType`.
        value: The NumPy array or scalar to convert.

    Returns:
        The value converted to the specified dtype.
    

### `def _convert_complexint32_array(requested_dtype: npt.DTypeLike | type[_ScalarType] | np.dtype[_ScalarType], value: np.ndarray[_Shape, Any]) -> np.ndarray[_Shape, np.dtype[_ScalarType]]`

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/scalar.py -->
## PYTHON MODULE: src/nitypes/scalar.py

### MODULE DOCSTRING

Scalar data types for NI Python APIs.

Scalar Data Type
=================

:class:`Scalar`: A scalar data object represents a single scalar value with units information.
Valid types for the scalar value are :any:`bool`, :any:`int`, :any:`float`, and :any:`str`.


- `_NUMERIC = (bool, int, float)`

### `class Scalar(Generic[TScalar_co])`

A scalar data class, which encapsulates scalar data and units information.

    Constructing
    ^^^^^^^^^^^^

    To construct a scalar data object, use the :class:`Scalar` class:

    >>> Scalar(False)
    nitypes.scalar.Scalar(value=False)
    >>> Scalar(0)
    nitypes.scalar.Scalar(value=0)
    >>> Scalar(5.0, 'volts')
    nitypes.scalar.Scalar(value=5.0, units='volts')
    >>> Scalar("value", "volts")
    nitypes.scalar.Scalar(value='value', units='volts')

    Comparing Scalar Objects
    ^^^^^^^^^^^^^^^^^^^^^^^^

    You can compare scalar objects using standard comparison
    operators: ``<``, ``<=``, ``>``, ``>=``, ``==``, and ``!=``.
    Detailed descriptions of operator behaviors are provided below.

    Equality Comparison Operators
    -----------------------------

    Equality comparison operators (``==`` and ``!=``) are always supported and behave as follows:

    - Comparison of scalar objects with compatible types and identical units results
      in ``True`` or ``False`` based on the comparison of scalar object values.
    - Comparison of scalar objects with incompatible types (such as numeric and string)
      results in inequality.
    - Comparison of scalar objects with different units results in inequality.

    Here are a few examples:

    >>> Scalar(5.0, 'V') == Scalar(5.0, 'V') # Numeric scalars with identical values and units
    True
    >>> Scalar(5.0, 'V') == Scalar(12.3, 'V') # Numeric scalars with identical units
    False
    >>> Scalar(5.0, 'V') != Scalar(12.3, 'V') # Numeric scalars with identical units
    True
    >>> Scalar("apple") == Scalar("banana") # String scalars
    False
    >>> Scalar("apple") == Scalar("Apple") # String scalars - note case sensitivity
    False
    >>> Scalar(0.5, 'V') == Scalar(500, 'mV') # Numeric scalars with different units
    False
    >>> Scalar(5.0, 'V') == Scalar("5.0", 'V') # Comparison of a numeric and a string scalar
    False

    Order Comparison Operators
    --------------------------

    Order comparison operators (``<``, ``<=``, ``>``, and ``>=``) behave as follows:

    - Comparison of scalar objects with compatible types and identical units results
      in ``True`` or ``False`` based on the comparison of scalar object values.
    - Comparison of scalar objects with incompatible types (such as numeric and string)
      is not permitted and will raise a ``TypeError`` exception.
    - Comparison of scalar objects with compatible types and different units
      is not permitted and will raise a ``ValueError`` exception.

    Here are a few examples:

    >>> Scalar(5.0, 'V') < Scalar(10.0, 'V') # Numeric scalars with identical units
    True
    >>> Scalar(5.0, 'V') >= Scalar(10.0, 'V') # Numeric scalars with identical units
    False
    >>> Scalar("apple") < Scalar("banana") # String scalars
    True
    >>> Scalar("apple") < Scalar("Banana") # String scalars - note case sensitivity
    False
    >>> Scalar(5.0, 'V') < Scalar("5.0", 'V') # Comparison of a numeric and a string scalar
    Traceback (most recent call last):
        ...
    TypeError: Comparing Scalar objects of numeric and string types is not permitted.
    >>> Scalar(0.5, 'V') < Scalar(500, 'mV') # Numeric scalars with different units
    Traceback (most recent call last):
        ...
    ValueError: Comparing Scalar objects with different units is not permitted.

    Class Members
    ^^^^^^^^^^^^^
    

#### `def __init__(self, value: TScalar_co, units: str='', *, extended_properties: Mapping[str, ExtendedPropertyValue] | None=None, copy_extended_properties: bool=True) -> None`

Initialize a new scalar.

        Args:
            value: The scalar data to store in this object.
            units: The units string associated with this data.
            extended_properties: The extended properties of the Scalar.
            copy_extended_properties: Specifies whether to copy the extended properties or take
                ownership.

        Returns:
            A scalar data object.
        

#### `def value(self) -> TScalar_co`

The scalar value.

#### `def units(self) -> str`

The unit of measurement, such as volts, of the scalar.

#### `def units(self, value: str) -> None`

#### `def extended_properties(self) -> ExtendedPropertyDictionary`

The extended properties for the scalar.

        .. note::
            Data stored in the extended properties dictionary may not be encrypted when you send it
            over the network or write it to a TDMS file.
        

#### `def __eq__(self, other: object, /) -> bool`

Return self == other.

#### `def __gt__(self, other: Scalar[TScalar_co], /) -> bool`

Return self > other.

#### `def __ge__(self, other: Scalar[TScalar_co], /) -> bool`

Return self >= other.

#### `def __lt__(self, other: Scalar[TScalar_co], /) -> bool`

Return self < other.

#### `def __le__(self, other: Scalar[TScalar_co], /) -> bool`

Return self <= other.

#### `def __reduce__(self) -> tuple[Any, ...]`

Return object state for pickling.

#### `def _unpickle(cls, args: tuple[Any, ...], kwargs: dict[str, Any]) -> Self`

#### `def __repr__(self) -> str`

Return repr(self).

#### `def __str__(self) -> str`

Return str(self).

#### `def _check_units_equal_for_comparison(self, other_units: str) -> None`

### `def _comparing_numeric_and_string_not_permitted() -> TypeError`

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/time/__init__.py -->
## PYTHON MODULE: src/nitypes/time/__init__.py

### MODULE DOCSTRING

Time data types for NI Python APIs.

- `__all__ = ['convert_datetime', 'convert_timedelta']`

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/time/_conversion.py -->
## PYTHON MODULE: src/nitypes/time/_conversion.py

### `def convert_datetime(requested_type: type[TDateTime], value: AnyDateTime, /) -> TDateTime`

Convert a datetime object to the specified type.

### `def _convert_to_bt_absolute_time(value: object, /) -> bt.DateTime`

### `def _(value: bt.DateTime, /) -> bt.DateTime`

### `def _(value: dt.datetime, /) -> bt.DateTime`

### `def _(value: ht.datetime, /) -> bt.DateTime`

### `def _convert_to_dt_datetime(value: object, /) -> dt.datetime`

### `def _(value: bt.DateTime, /) -> dt.datetime`

### `def _(value: dt.datetime, /) -> dt.datetime`

### `def _(value: ht.datetime, /) -> dt.datetime`

### `def _convert_to_ht_datetime(value: object, /) -> ht.datetime`

### `def _(value: bt.DateTime, /) -> ht.datetime`

### `def _(value: dt.datetime, /) -> ht.datetime`

### `def _(value: ht.datetime, /) -> ht.datetime`

- `_CONVERT_DATETIME_FOR_TYPE = {bt.DateTime: _convert_to_bt_absolute_time, dt.datetime: _convert_to_dt_datetime, ht.datetime: _convert_to_ht_datetime}`

### `def convert_timedelta(requested_type: type[TTimeDelta], value: AnyTimeDelta, /) -> TTimeDelta`

Convert a timedelta object to the specified type.

### `def _convert_to_bt_timedelta(value: object, /) -> bt.TimeDelta`

### `def _(value: bt.TimeDelta, /) -> bt.TimeDelta`

### `def _(value: dt.timedelta, /) -> bt.TimeDelta`

### `def _(value: ht.timedelta, /) -> bt.TimeDelta`

### `def _convert_to_dt_timedelta(value: object, /) -> dt.timedelta`

### `def _(value: bt.TimeDelta, /) -> dt.timedelta`

### `def _(value: dt.timedelta, /) -> dt.timedelta`

### `def _(value: ht.timedelta, /) -> dt.timedelta`

### `def _convert_to_ht_timedelta(value: object, /) -> ht.timedelta`

### `def _(value: bt.TimeDelta, /) -> ht.timedelta`

### `def _(value: dt.timedelta, /) -> ht.timedelta`

### `def _(value: ht.timedelta, /) -> ht.timedelta`

- `_CONVERT_TIMEDELTA_FOR_TYPE = {bt.TimeDelta: _convert_to_bt_timedelta, dt.timedelta: _convert_to_dt_timedelta, ht.timedelta: _convert_to_ht_timedelta}`

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/time/_types.py -->
## PYTHON MODULE: src/nitypes/time/_types.py

- `ANY_DATETIME_TUPLE = (bt.DateTime, dt.datetime, ht.datetime)`

- `ANY_TIMEDELTA_TUPLE = (bt.TimeDelta, dt.timedelta, ht.timedelta)`

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/time/typing.py -->
## PYTHON MODULE: src/nitypes/time/typing.py

### MODULE DOCSTRING

Type aliases and type variables for time types.

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/vector.py -->
## PYTHON MODULE: src/nitypes/vector.py

### MODULE DOCSTRING

Vector data type for NI Python APIs.

Vector Data Type
=================
:class:`Vector`: A vector data object represents an array of scalar values with units information.
Valid types for the scalar value are :any:`bool`, :any:`int`, :any:`float`, and :any:`str`.


### `class Vector(MutableSequence[TScalar])`

A sequence of scalar values with units information.

    Constructing
    ^^^^^^^^^^^^

    To construct a vector data object, use the :class:`Vector` class:

    >>> Vector([False, True])
    nitypes.vector.Vector(values=[False, True])
    >>> Vector([0, 1, 2])
    nitypes.vector.Vector(values=[0, 1, 2])
    >>> Vector([5.0, 6.0], 'volts')
    nitypes.vector.Vector(values=[5.0, 6.0], units='volts')
    >>> Vector(["one", "two"], "volts")
    nitypes.vector.Vector(values=['one', 'two'], units='volts')
    

#### `def __init__(self, values: Iterable[TScalar], units: str='', *, value_type: type[TScalar] | None=None, extended_properties: Mapping[str, ExtendedPropertyValue] | None=None, copy_extended_properties: bool=True) -> None`

Initialize a new vector.

        Args:
            values: The scalar values to store in this object.
            units: The units string associated with this data.
            value_type: The type of values that will be added to this Vector.
                This parameter should only be used when creating a Vector with
                an empty Iterable.
            extended_properties: The extended properties of the Vector.
            copy_extended_properties: Specifies whether to copy the extended properties or take
                ownership.

        Returns:
            A vector data object.
        

#### `def units(self) -> str`

The unit of measurement, such as volts, of the vector.

#### `def units(self, value: str) -> None`

#### `def extended_properties(self) -> ExtendedPropertyDictionary`

The extended properties for the vector.

        .. note::
            Data stored in the extended properties dictionary may not be encrypted when you send it
            over the network or write it to a TDMS file.
        

#### `def __getitem__(self, index: int) -> TScalar`

#### `def __getitem__(self, index: slice) -> MutableSequence[TScalar]`

#### `def __getitem__(self, index: int | slice) -> TScalar | MutableSequence[TScalar]`

Return the TimeDelta at the specified location.

#### `def __setitem__(self, index: int, value: TScalar) -> None`

#### `def __setitem__(self, index: slice, value: Iterable[TScalar]) -> None`

#### `def __setitem__(self, index: int | slice, value: TScalar | Iterable[TScalar]) -> None`

Set value(s) at the specified location.

#### `def __delitem__(self, index: int | slice) -> None`

Delete item(s) from the specified location.

#### `def __len__(self) -> int`

Return the length of the Vector.

#### `def insert(self, index: int, value: TScalar) -> None`

Insert a value at the specified location.

#### `def __eq__(self, value: object, /) -> bool`

Return self==value.

#### `def __reduce__(self) -> tuple[Any, ...]`

Return object state for pickling.

#### `def _unpickle(cls, args: tuple[Any, ...], kwargs: dict[str, Any]) -> Self`

#### `def __repr__(self) -> str`

Return repr(self).

#### `def __str__(self) -> str`

Return str(self).

#### `def _create_value_mismatch_exception(self, value: object) -> TypeError`

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/__init__.py -->
## PYTHON MODULE: src/nitypes/waveform/__init__.py

### MODULE DOCSTRING

Waveform data types for NI Python APIs.

Waveform Data Types
===================

* :class:`AnalogWaveform`: An analog waveform represents a single analog signal with timing
  information and extended properties such as units.
* :class:`ComplexWaveform`: A complex waveform represents a single complex-number signal, such as
  I/Q data, with timing information and extended properties such as units.
* :class:`DigitalWaveform`: A digital waveform represents one or more digital signals with timing
  information and extended properties such as channel name and signal names.
* :class:`Spectrum`: A frequency spectrum represents an analog signal with frequency information
  and extended properties such as units.


- `__all__ = ['AnalogWaveform', 'ComplexWaveform', 'DigitalState', 'DigitalWaveform', 'DigitalWaveformFailure', 'DigitalWaveformSignal', 'DigitalWaveformSignalCollection', 'DigitalWaveformTestResult', 'ExtendedPropertyDictionary', 'LinearScaleMode', 'NO_SCALING', 'NoneScaleMode', 'NumericWaveform', 'SampleIntervalMode', 'ScaleMode', 'Spectrum', 'Timing']`

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_analog.py -->
## PYTHON MODULE: src/nitypes/waveform/_analog.py

- `_RAW_DTYPES = (np.single, np.double, np.byte, np.short, np.intc, np.int_, _np_long, np.longlong, np.ubyte, np.ushort, np.uintc, np.uint, _np_ulong, np.ulonglong)`

- `_SCALED_DTYPES = (np.single, np.double)`

### `class AnalogWaveform(NumericWaveform[_TRaw, np.float64])`

An analog waveform, which encapsulates analog data and timing information.

    Constructing
    ^^^^^^^^^^^^

    To construct an analog waveform, use the :class:`AnalogWaveform` class:

    >>> AnalogWaveform()
    nitypes.waveform.AnalogWaveform(0)
    >>> AnalogWaveform(5)
    nitypes.waveform.AnalogWaveform(5, raw_data=array([0., 0., 0., 0., 0.]))

    To construct an analog waveform from a NumPy array, use the :any:`AnalogWaveform.from_array_1d`
    method.

    >>> import numpy as np
    >>> AnalogWaveform.from_array_1d(np.array([1.0, 2.0, 3.0]))
    nitypes.waveform.AnalogWaveform(3, raw_data=array([1., 2., 3.]))

    You can also use :any:`AnalogWaveform.from_array_1d` to construct an analog waveform from a
    sequence, such as a list. In this case, you must specify the NumPy data type.

    >>> AnalogWaveform.from_array_1d([1.0, 2.0, 3.0], np.float64)
    nitypes.waveform.AnalogWaveform(3, raw_data=array([1., 2., 3.]))

    The 2D version, :any:`AnalogWaveform.from_array_2d`, returns multiple waveforms, one for each row of
    data in the array or nested sequence.

    >>> nested_list = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    >>> AnalogWaveform.from_array_2d(nested_list, np.float64)  # doctest: +NORMALIZE_WHITESPACE
    [nitypes.waveform.AnalogWaveform(3, raw_data=array([1., 2., 3.])),
    nitypes.waveform.AnalogWaveform(3, raw_data=array([4., 5., 6.]))]

    Timing information
    ^^^^^^^^^^^^^^^^^^

    Analog waveforms include timing information, such as the start time and sample interval, to support
    analyzing and visualizing the data.

    You can specify timing information by constructing a :class:`Timing` object and passing it to the
    waveform constructor or factory method:

    >>> import datetime as dt
    >>> wfm = AnalogWaveform(timing=Timing.create_with_regular_interval(
    ...     dt.timedelta(seconds=1e-3), dt.datetime(2024, 12, 31, 23, 59, 59, tzinfo=dt.timezone.utc)
    ... ))
    >>> wfm.timing  # doctest: +NORMALIZE_WHITESPACE
    nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR,
        timestamp=datetime.datetime(2024, 12, 31, 23, 59, 59, tzinfo=datetime.timezone.utc),
        sample_interval=datetime.timedelta(microseconds=1000))

    You can query the waveform's timing information using the :class:`Timing` object's properties:

    >>> wfm.timing.start_time
    datetime.datetime(2024, 12, 31, 23, 59, 59, tzinfo=datetime.timezone.utc)
    >>> wfm.timing.sample_interval
    datetime.timedelta(microseconds=1000)

    Timing objects are immutable, so you cannot directly set their properties:

    >>> wfm.timing.sample_interval = dt.timedelta(seconds=10e-3)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    AttributeError: ...

    Instead, if you want to modify the timing information for an existing waveform, you can create a new
    timing object and set the :any:`NumericWaveform.timing` property:

    >>> wfm.timing = Timing.create_with_regular_interval(
    ...     dt.timedelta(seconds=1e-3), dt.datetime(2025, 1, 1, tzinfo=dt.timezone.utc)
    ... )
    >>> wfm.timing  # doctest: +NORMALIZE_WHITESPACE
    nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR,
        timestamp=datetime.datetime(2025, 1, 1, 0, 0, tzinfo=datetime.timezone.utc),
        sample_interval=datetime.timedelta(microseconds=1000))

    Timing objects support time types from the :class:`DateTime`, :any:`hightime`, and
    :any:`nitypes.bintime` modules. If you need the timing information in a specific representation, use
    the conversion methods:

    >>> wfm.timing.to_datetime()  # doctest: +NORMALIZE_WHITESPACE
    nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR,
        timestamp=datetime.datetime(2025, 1, 1, 0, 0, tzinfo=datetime.timezone.utc),
        sample_interval=datetime.timedelta(microseconds=1000))
    >>> wfm.timing.to_hightime()  # doctest: +NORMALIZE_WHITESPACE
    nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR,
        timestamp=hightime.datetime(2025, 1, 1, 0, 0, tzinfo=datetime.timezone.utc),
        sample_interval=hightime.timedelta(microseconds=1000))
    >>> wfm.timing.to_bintime()  # doctest: +NORMALIZE_WHITESPACE
    nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR,
        timestamp=nitypes.bintime.DateTime(2025, 1, 1, 0, 0, tzinfo=datetime.timezone.utc),
        sample_interval=nitypes.bintime.TimeDelta(Decimal('0.000999999999999999966606573')))

    If :any:`NumericWaveform.timing` is not specified for a given waveform, it defaults to the
    :any:`Timing.empty` singleton object.

    >>> AnalogWaveform().timing
    nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.NONE)
    >>> AnalogWaveform().timing is Timing.empty
    True

    Accessing unspecified properties of the timing object raises an exception:

    >>> Timing.empty.sample_interval
    Traceback (most recent call last):
    ...
    RuntimeError: The waveform timing does not have a sample interval.

    You can use :any:`Timing.sample_interval_mode` and ``has_*`` properties such as
    :any:`Timing.has_timestamp` to query which properties of the timing object were specified:

    >>> wfm.timing.sample_interval_mode
    <SampleIntervalMode.REGULAR: 1>
    >>> (wfm.timing.has_timestamp, wfm.timing.has_sample_interval)
    (True, True)
    >>> Timing.empty.sample_interval_mode
    <SampleIntervalMode.NONE: 0>
    >>> (Timing.empty.has_timestamp, Timing.empty.has_sample_interval)
    (False, False)

    Scaling analog data
    ^^^^^^^^^^^^^^^^^^^

    By default, analog waveforms contain floating point data in :any:`numpy.float64` format, but they
    can also be used to scale raw integer data to floating-point:

    >>> import numpy as np
    >>> scale_mode = LinearScaleMode(gain=2.0, offset=0.5)
    >>> wfm = AnalogWaveform.from_array_1d([1, 2, 3], np.int32, scale_mode=scale_mode)
    >>> wfm  # doctest: +NORMALIZE_WHITESPACE
    nitypes.waveform.AnalogWaveform(3, int32, raw_data=array([1, 2, 3], dtype=int32),
        scale_mode=nitypes.waveform.LinearScaleMode(2.0, 0.5))
    >>> wfm.raw_data
    array([1, 2, 3], dtype=int32)
    >>> wfm.scaled_data
    array([2.5, 4.5, 6.5])

    Class members
    ^^^^^^^^^^^^^
    

#### `def _get_default_raw_dtype() -> type[np.generic] | np.dtype[np.generic]`

#### `def _get_default_scaled_dtype() -> type[np.generic] | np.dtype[np.generic]`

#### `def _get_supported_raw_dtypes() -> tuple[npt.DTypeLike, ...]`

#### `def _get_supported_scaled_dtypes() -> tuple[npt.DTypeLike, ...]`

#### `def from_array_1d(cls, array: npt.NDArray[_TOtherRaw], dtype: None=..., *, copy: bool=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=..., scale_mode: ScaleMode | None=...) -> AnalogWaveform[_TOtherRaw]`

#### `def from_array_1d(cls, array: npt.NDArray[Any] | Sequence[Any], dtype: type[_TOtherRaw] | np.dtype[_TOtherRaw], *, copy: bool=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=..., scale_mode: ScaleMode | None=...) -> AnalogWaveform[_TOtherRaw]`

#### `def from_array_1d(cls, array: npt.NDArray[Any] | Sequence[Any], dtype: npt.DTypeLike | None=..., *, copy: bool=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=..., scale_mode: ScaleMode | None=...) -> AnalogWaveform[Any]`

#### `def from_array_1d(cls, array: npt.NDArray[Any] | Sequence[Any], dtype: npt.DTypeLike | None=None, *, copy: bool=True, start_index: SupportsIndex | None=0, sample_count: SupportsIndex | None=None, extended_properties: Mapping[str, ExtendedPropertyValue] | None=None, timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=None, scale_mode: ScaleMode | None=None) -> AnalogWaveform[Any]`

Construct an analog waveform from a one-dimensional array or sequence.

        Args:
            array: The waveform data as a one-dimensional array or a sequence.
            dtype: The NumPy data type for the waveform data. This argument is required
                when array is a sequence.
            copy: Specifies whether to copy the array or save a reference to it.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
            extended_properties: The extended properties of the waveform.
            timing: The timing information of the waveform.
            scale_mode: The scale mode of the waveform.

        Returns:
            An analog waveform containing the specified data.
        

#### `def from_array_2d(cls, array: npt.NDArray[_TOtherRaw], dtype: None=..., *, copy: bool=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=..., scale_mode: ScaleMode | None=...) -> Sequence[AnalogWaveform[_TOtherRaw]]`

#### `def from_array_2d(cls, array: npt.NDArray[Any] | Sequence[Sequence[Any]], dtype: type[_TOtherRaw] | np.dtype[_TOtherRaw], *, copy: bool=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=..., scale_mode: ScaleMode | None=...) -> Sequence[AnalogWaveform[_TOtherRaw]]`

#### `def from_array_2d(cls, array: npt.NDArray[Any] | Sequence[Sequence[Any]], dtype: npt.DTypeLike | None=..., *, copy: bool=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=..., scale_mode: ScaleMode | None=...) -> Sequence[AnalogWaveform[Any]]`

#### `def from_array_2d(cls, array: npt.NDArray[Any] | Sequence[Sequence[Any]], dtype: npt.DTypeLike | None=None, *, copy: bool=True, start_index: SupportsIndex | None=0, sample_count: SupportsIndex | None=None, extended_properties: Mapping[str, ExtendedPropertyValue] | None=None, timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=None, scale_mode: ScaleMode | None=None) -> Sequence[AnalogWaveform[Any]]`

Construct multiple analog waveforms from a two-dimensional array or nested sequence.

        Args:
            array: The waveform data as a two-dimensional array or a nested sequence.
            dtype: The NumPy data type for the waveform data. This argument is required
                when array is a sequence.
            copy: Specifies whether to copy the array or save a reference to it.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
            extended_properties: The extended properties of the waveform.
            timing: The timing information of the waveform.
            scale_mode: The scale mode of the waveform.

        Returns:
            A sequence containing an analog waveform for each row of the specified data.

        When constructing multiple waveforms, the same extended properties, timing
        information, and scale mode are applied to all waveforms. Consider assigning
        these properties after construction.
        

#### `def __init__(self: AnalogWaveform[np.float64], sample_count: SupportsIndex | None=..., dtype: None=..., *, raw_data: None=..., start_index: SupportsIndex | None=..., capacity: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., copy_extended_properties: bool=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=..., scale_mode: ScaleMode | None=...) -> None`

#### `def __init__(self: AnalogWaveform[_TOtherRaw], sample_count: SupportsIndex | None=..., dtype: type[_TOtherRaw] | np.dtype[_TOtherRaw]=..., *, raw_data: None=..., start_index: SupportsIndex | None=..., capacity: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., copy_extended_properties: bool=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=..., scale_mode: ScaleMode | None=...) -> None`

#### `def __init__(self: AnalogWaveform[_TOtherRaw], sample_count: SupportsIndex | None=..., dtype: None=..., *, raw_data: npt.NDArray[_TOtherRaw]=..., start_index: SupportsIndex | None=..., capacity: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., copy_extended_properties: bool=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=..., scale_mode: ScaleMode | None=...) -> None`

#### `def __init__(self: AnalogWaveform[Any], sample_count: SupportsIndex | None=..., dtype: npt.DTypeLike | None=..., *, raw_data: npt.NDArray[Any] | None=..., start_index: SupportsIndex | None=..., capacity: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., copy_extended_properties: bool=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=..., scale_mode: ScaleMode | None=...) -> None`

#### `def __init__(self, sample_count: SupportsIndex | None=None, dtype: npt.DTypeLike | None=None, *, raw_data: npt.NDArray[Any] | None=None, start_index: SupportsIndex | None=None, capacity: SupportsIndex | None=None, extended_properties: Mapping[str, ExtendedPropertyValue] | None=None, copy_extended_properties: bool=True, timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=None, scale_mode: ScaleMode | None=None) -> None`

Initialize a new analog waveform.

        Args:
            sample_count: The number of samples in the analog waveform.
            dtype: The NumPy data type for the analog waveform data. If not specified, the data
                type defaults to np.float64.
            raw_data: A NumPy ndarray to use for sample storage. The analog waveform takes ownership
                of this array. If not specified, an ndarray is created based on the specified dtype,
                start index, sample count, and capacity.
            start_index: The sample index at which the analog waveform data begins.
            capacity: The number of samples to allocate. Pre-allocating a larger buffer optimizes
                appending samples to the waveform.
            extended_properties: The extended properties of the analog waveform.
            copy_extended_properties: Specifies whether to copy the extended properties or take
                ownership.
            timing: The timing information of the analog waveform.
            scale_mode: The scale mode of the analog waveform.

        Returns:
            An analog waveform.
        

#### `def _convert_data(self, dtype: npt.DTypeLike | type[_TOtherScaled] | np.dtype[_TOtherScaled], raw_data: npt.NDArray[_TRaw]) -> npt.NDArray[_TOtherScaled]`

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_complex.py -->
## PYTHON MODULE: src/nitypes/waveform/_complex.py

- `_RAW_DTYPES = (np.csingle, np.cdouble, ComplexInt32DType)`

- `_SCALED_DTYPES = (np.csingle, np.cdouble)`

### `class ComplexWaveform(NumericWaveform[_TRaw, np.complex128])`

A complex waveform, which encapsulates complex data and timing information.

    Constructing
    ^^^^^^^^^^^^

    To construct a complex waveform, use the :class:`ComplexWaveform` class:

    >>> ComplexWaveform()
    nitypes.waveform.ComplexWaveform(0)
    >>> ComplexWaveform(5)
    nitypes.waveform.ComplexWaveform(5, raw_data=array([0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]))

    To construct a complex waveform from a NumPy array, use the :any:`ComplexWaveform.from_array_1d`
    method.

    >>> import numpy as np
    >>> ComplexWaveform.from_array_1d(np.array([1+2j, 3+4j, 5+6j]))
    nitypes.waveform.ComplexWaveform(3, raw_data=array([1.+2.j, 3.+4.j, 5.+6.j]))

    You can also use :any:`ComplexWaveform.from_array_1d` to construct a complex waveform from a
    sequence, such as a list. In this case, you must specify the NumPy data type.

    >>> ComplexWaveform.from_array_1d([1+2j, 3+4j, 5+6j], np.complex128)
    nitypes.waveform.ComplexWaveform(3, raw_data=array([1.+2.j, 3.+4.j, 5.+6.j]))

    The 2D version, :any:`ComplexWaveform.from_array_2d`, returns multiple waveforms, one for each row of
    data in the array or nested sequence.

    >>> nested_list = [[1+2j, 3+4j, 5+6j], [7+8j, 9+10j, 11+12j]]
    >>> ComplexWaveform.from_array_2d(nested_list, np.complex128)  # doctest: +NORMALIZE_WHITESPACE
    [nitypes.waveform.ComplexWaveform(3, raw_data=array([1.+2.j, 3.+4.j, 5.+6.j])),
    nitypes.waveform.ComplexWaveform(3, raw_data=array([ 7. +8.j,  9.+10.j, 11.+12.j]))]

    Scaling complex-number data
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Complex waveforms support scaling raw integer data to floating-point. Python and NumPy do not have
    native support for complex integers, so this uses the :any:`ComplexInt32DType` structured data type.

    >>> from nitypes.complex import ComplexInt32DType
    >>> scale_mode = LinearScaleMode(gain=2.0, offset=0.5)
    >>> wfm = ComplexWaveform.from_array_1d([(1, 2), (3, 4)], ComplexInt32DType, scale_mode=scale_mode)
    >>> wfm  # doctest: +NORMALIZE_WHITESPACE
    nitypes.waveform.ComplexWaveform(2, void32, raw_data=array([(1, 2), (3, 4)],
        dtype=[('real', '<i2'), ('imag', '<i2')]),
        scale_mode=nitypes.waveform.LinearScaleMode(2.0, 0.5))
    >>> wfm.raw_data
    array([(1, 2), (3, 4)], dtype=[('real', '<i2'), ('imag', '<i2')])
    >>> wfm.scaled_data
    array([2.5+4.j, 6.5+8.j])

    Timing information
    ^^^^^^^^^^^^^^^^^^

    Complex waveforms have the same timing information as analog waveforms. For more details, see
    :class:`AnalogWaveform`.

    Class members
    ^^^^^^^^^^^^^
    

#### `def _get_default_raw_dtype() -> type[np.generic] | np.dtype[np.generic]`

#### `def _get_default_scaled_dtype() -> type[np.generic] | np.dtype[np.generic]`

#### `def _get_supported_raw_dtypes() -> tuple[npt.DTypeLike, ...]`

#### `def _get_supported_scaled_dtypes() -> tuple[npt.DTypeLike, ...]`

#### `def from_array_1d(cls, array: npt.NDArray[_TOtherRaw], dtype: None=..., *, copy: bool=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=..., scale_mode: ScaleMode | None=...) -> ComplexWaveform[_TOtherRaw]`

#### `def from_array_1d(cls, array: npt.NDArray[Any] | Sequence[Any], dtype: type[_TOtherRaw] | np.dtype[_TOtherRaw], *, copy: bool=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=..., scale_mode: ScaleMode | None=...) -> ComplexWaveform[_TOtherRaw]`

#### `def from_array_1d(cls, array: npt.NDArray[Any] | Sequence[Any], dtype: npt.DTypeLike | None=..., *, copy: bool=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=..., scale_mode: ScaleMode | None=...) -> ComplexWaveform[Any]`

#### `def from_array_1d(cls, array: npt.NDArray[Any] | Sequence[Any], dtype: npt.DTypeLike | None=None, *, copy: bool=True, start_index: SupportsIndex | None=0, sample_count: SupportsIndex | None=None, extended_properties: Mapping[str, ExtendedPropertyValue] | None=None, timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=None, scale_mode: ScaleMode | None=None) -> ComplexWaveform[Any]`

Construct a complex waveform from a one-dimensional array or sequence.

        Args:
            array: The waveform data as a one-dimensional array or a sequence.
            dtype: The NumPy data type for the waveform data. This argument is required
                when array is a sequence.
            copy: Specifies whether to copy the array or save a reference to it.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
            extended_properties: The extended properties of the waveform.
            timing: The timing information of the waveform.
            scale_mode: The scale mode of the waveform.

        Returns:
            A complex waveform containing the specified data.
        

#### `def from_array_2d(cls, array: npt.NDArray[_TOtherRaw], dtype: None=..., *, copy: bool=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=..., scale_mode: ScaleMode | None=...) -> Sequence[ComplexWaveform[_TOtherRaw]]`

#### `def from_array_2d(cls, array: npt.NDArray[Any] | Sequence[Sequence[Any]], dtype: type[_TOtherRaw] | np.dtype[_TOtherRaw], *, copy: bool=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=..., scale_mode: ScaleMode | None=...) -> Sequence[ComplexWaveform[_TOtherRaw]]`

#### `def from_array_2d(cls, array: npt.NDArray[Any] | Sequence[Sequence[Any]], dtype: npt.DTypeLike | None=..., *, copy: bool=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=..., scale_mode: ScaleMode | None=...) -> Sequence[ComplexWaveform[Any]]`

#### `def from_array_2d(cls, array: npt.NDArray[Any] | Sequence[Sequence[Any]], dtype: npt.DTypeLike | None=None, *, copy: bool=True, start_index: SupportsIndex | None=0, sample_count: SupportsIndex | None=None, extended_properties: Mapping[str, ExtendedPropertyValue] | None=None, timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=None, scale_mode: ScaleMode | None=None) -> Sequence[ComplexWaveform[Any]]`

Construct multiple complex waveforms from a two-dimensional array or nested sequence.

        Args:
            array: The waveform data as a two-dimensional array or a nested sequence.
            dtype: The NumPy data type for the waveform data. This argument is required
                when array is a sequence.
            copy: Specifies whether to copy the array or save a reference to it.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
            extended_properties: The extended properties of the waveform.
            timing: The timing information of the waveform.
            scale_mode: The scale mode of the waveform.

        Returns:
            A sequence containing a complex waveform for each row of the specified data.

        When constructing multiple waveforms, the same extended properties, timing
        information, and scale mode are applied to all waveforms. Consider assigning
        these properties after construction.
        

#### `def __init__(self: ComplexWaveform[np.complex128], sample_count: SupportsIndex | None=..., dtype: None=..., *, raw_data: None=..., start_index: SupportsIndex | None=..., capacity: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., copy_extended_properties: bool=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=..., scale_mode: ScaleMode | None=...) -> None`

#### `def __init__(self: ComplexWaveform[_TOtherRaw], sample_count: SupportsIndex | None=..., dtype: type[_TOtherRaw] | np.dtype[_TOtherRaw]=..., *, raw_data: None=..., start_index: SupportsIndex | None=..., capacity: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., copy_extended_properties: bool=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=..., scale_mode: ScaleMode | None=...) -> None`

#### `def __init__(self: ComplexWaveform[_TOtherRaw], sample_count: SupportsIndex | None=..., dtype: None=..., *, raw_data: npt.NDArray[_TOtherRaw]=..., start_index: SupportsIndex | None=..., capacity: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., copy_extended_properties: bool=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=..., scale_mode: ScaleMode | None=...) -> None`

#### `def __init__(self: ComplexWaveform[Any], sample_count: SupportsIndex | None=..., dtype: npt.DTypeLike | None=..., *, raw_data: npt.NDArray[Any] | None=..., start_index: SupportsIndex | None=..., capacity: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., copy_extended_properties: bool=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=..., scale_mode: ScaleMode | None=...) -> None`

#### `def __init__(self, sample_count: SupportsIndex | None=None, dtype: npt.DTypeLike | None=None, *, raw_data: npt.NDArray[Any] | None=None, start_index: SupportsIndex | None=None, capacity: SupportsIndex | None=None, extended_properties: Mapping[str, ExtendedPropertyValue] | None=None, copy_extended_properties: bool=True, timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=None, scale_mode: ScaleMode | None=None) -> None`

Initialize a new complex waveform.

        Args:
            sample_count: The number of samples in the waveform.
            dtype: The NumPy data type for the waveform data. If not specified, the data
                type defaults to np.complex128.
            raw_data: A NumPy ndarray to use for sample storage. The waveform takes ownership
                of this array. If not specified, an ndarray is created based on the specified dtype,
                start index, sample count, and capacity.
            start_index: The sample index at which the waveform data begins.
            capacity: The number of samples to allocate. Pre-allocating a larger buffer optimizes
                appending samples to the waveform.
            extended_properties: The extended properties of the waveform.
            copy_extended_properties: Specifies whether to copy the extended properties or take
                ownership.
            timing: The timing information of the waveform.
            scale_mode: The scale mode of the waveform.

        Returns:
            A complex waveform.
        

#### `def _convert_data(self, dtype: npt.DTypeLike | type[_TOtherScaled] | np.dtype[_TOtherScaled], raw_data: npt.NDArray[_TRaw]) -> npt.NDArray[_TOtherScaled]`

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_digital/__init__.py -->
## PYTHON MODULE: src/nitypes/waveform/_digital/__init__.py

### MODULE DOCSTRING

Digital waveform data types.

- `__all__ = ['DigitalState', 'DigitalWaveform', 'DigitalWaveformFailure', 'DigitalWaveformSignal', 'DigitalWaveformSignalCollection', 'DigitalWaveformTestResult']`

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_digital/_port.py -->
## PYTHON MODULE: src/nitypes/waveform/_digital/_port.py

### `def bit_mask(n: int, /) -> int`

Return the bit mask with the lower n bits set.

    >>> bit_mask(0)
    0
    >>> bit_mask(4)
    15
    >>> bit_mask(9)
    511
    >>> bit_mask(32)
    4294967295
    >>> bit_mask(-1)
    Traceback (most recent call last):
    ...
    ValueError: The number of bits must be a non-negative integer.
    <BLANKLINE>
    Number of bits: -1
    

### `def get_port_dtype(mask: int | Sequence[int]) -> np.dtype[AnyDigitalPort]`

Return the NumPy port dtype for the given mask.

    >>> get_port_dtype(0xF)
    dtype('uint8')
    >>> get_port_dtype(0x100)
    dtype('uint16')
    >>> get_port_dtype(0xDEADBEEF)
    dtype('uint32')
    >>> get_port_dtype(0x1_0000_0000)
    Traceback (most recent call last):
    ...
    ValueError: The mask must be an unsigned 8-, 16-, or 32-bit integer.
    <BLANKLINE>
    Mask: 4294967296
    >>> get_port_dtype([0x0F, 0xF0])
    dtype('uint8')
    >>> get_port_dtype([0x100, 0x01])
    dtype('uint16')
    >>> get_port_dtype([0x01, 0x100])
    dtype('uint16')
    >>> get_port_dtype([0xDEADBEEF])
    dtype('uint32')
    

### `def _get_port_dtype(mask: int) -> np.dtype[AnyDigitalPort]`

### `def port_to_line_data(port_data: npt.NDArray[AnyDigitalPort], mask: int, bitorder: Literal['big', 'little']='big') -> npt.NDArray[np.uint8]`

Convert a 1D array of port data to a 2D array of line data, using the specified mask.

    >>> port_to_line_data(np.array([0,1,2,3], np.uint8), 0xFF)
    array([[0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0, 0, 1, 1]], dtype=uint8)

    >>> port_to_line_data(np.array([0,1,2,3], np.uint8), 0xFF, bitorder="little")
    array([[0, 0, 0, 0, 0, 0, 0, 0],
           [1, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 0, 0, 0],
           [1, 1, 0, 0, 0, 0, 0, 0]], dtype=uint8)
    >>> port_to_line_data(np.array([0,1,2,3], np.uint8), 0x3)
    array([[0, 0],
           [0, 1],
           [1, 0],
           [1, 1]], dtype=uint8)
    >>> port_to_line_data(np.array([0,1,2,3], np.uint8), 0x3, bitorder="little")
    array([[0, 0],
           [1, 0],
           [0, 1],
           [1, 1]], dtype=uint8)
    >>> port_to_line_data(np.array([0,1,2,3], np.uint8), 0x2)
    array([[0],
           [0],
           [1],
           [1]], dtype=uint8)
    >>> port_to_line_data(np.array([0,1,2,3], np.uint8), 0)
    array([], shape=(4, 0), dtype=uint8)
    >>> port_to_line_data(np.array([0x12000000,0xFE000000], np.uint32), 0xFF000000)
    array([[0, 0, 0, 1, 0, 0, 1, 0],
           [1, 1, 1, 1, 1, 1, 1, 0]], dtype=uint8)
    

### `def _mask_to_column_indices(mask: int, port_size: int, bitorder: Literal['big', 'little'], /) -> list[int]`

Return the column indices for the given mask.

    >>> _mask_to_column_indices(0xF, 8, "big")
    [4, 5, 6, 7]
    >>> _mask_to_column_indices(0x100, 16, "big")
    [7]
    >>> _mask_to_column_indices(0xDEADBEEF, 32, "big")
    [0, 1, 3, 4, 5, 6, 8, 10, 12, 13, 15, 16, 18, 19, 20, 21, 22, 24, 25, 26, 28, 29, 30, 31]
    >>> _mask_to_column_indices(0xF, 8, "little")
    [0, 1, 2, 3]
    >>> _mask_to_column_indices(0x100, 16, "little")
    [8]
    >>> _mask_to_column_indices(0xDEADBEEF, 32, "little")
    [0, 1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 13, 15, 16, 18, 19, 21, 23, 25, 26, 27, 28, 30, 31]
    >>> _mask_to_column_indices(-1, 8, "little")
    Traceback (most recent call last):
    ...
    ValueError: The mask must be a non-negative integer.
    <BLANKLINE>
    Mask: -1
    

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_digital/_signal.py -->
## PYTHON MODULE: src/nitypes/waveform/_digital/_signal.py

### `class DigitalWaveformSignal(Generic[TDigitalState])`

A signal of a digital waveform.

    To construct this object, use the :any:`DigitalWaveform.signals` property and index the returned
    collection, e.g. ``waveform.signals[0]`` or ``waveform.signals["Dev1/port0/line0"]``.
    

#### `def __init__(self, owner: DigitalWaveform[TDigitalState], signal_index: SupportsIndex, column_index: SupportsIndex | None=None) -> None`

Initialize a new digital waveform signal.

#### `def owner(self) -> DigitalWaveform[TDigitalState]`

The waveform that owns this signal.

#### `def signal_index(self) -> int`

The signal's position in the DigitalWaveform.signals collection (0-based).

#### `def column_index(self) -> int`

The signal's position in the DigitalWaveform.data array's second dimension (0-based).

        This index is used to access the signal's data within the waveform's data array:
        `waveform.data[:, column_index]`.

        Note: The column_index is reversed compared to the signal_index. column_index 0 (the
        leftmost column) corresponds to the highest signal_index and highest line number. The
        highest column_index (the rightmost column) corresponds to signal_index 0 and line 0. This
        matches industry conventions where line 0 is the LSB and appears as the rightmost bit.
        

#### `def data(self) -> npt.NDArray[TDigitalState]`

The signal data, indexed by sample.

#### `def name(self) -> str`

The signal name.

#### `def name(self, value: str) -> None`

#### `def __eq__(self, value: object, /) -> bool`

Return self==value.

#### `def __reduce__(self) -> tuple[Any, ...]`

Return object state for pickling.

#### `def __repr__(self) -> str`

Return repr(self).

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_digital/_signal_collection.py -->
## PYTHON MODULE: src/nitypes/waveform/_digital/_signal_collection.py

### `class DigitalWaveformSignalCollection(Generic[TDigitalState], Sequence[DigitalWaveformSignal[TDigitalState]])`

A collection of digital waveform signals.

    To construct this object, use the :any:`DigitalWaveform.signals` property.
    

#### `def __init__(self, owner: DigitalWaveform[TDigitalState]) -> None`

Initialize a new DigitalWaveformSignalCollection.

#### `def __len__(self) -> int`

Return len(self).

#### `def __getitem__(self, index: int | str) -> DigitalWaveformSignal[TDigitalState]`

#### `def __getitem__(self, index: slice) -> Sequence[DigitalWaveformSignal[TDigitalState]]`

#### `def __getitem__(self, index: int | str | slice) -> DigitalWaveformSignal[TDigitalState] | Sequence[DigitalWaveformSignal[TDigitalState]]`

Get self[index].

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_digital/_state.py -->
## PYTHON MODULE: src/nitypes/waveform/_digital/_state.py

- `_CHAR_TABLE = '01ZLHXTV'`

- `_STATE_TEST_TABLE = [[1, 0, 0, 1, 0, 1, 0, 1], [0, 1, 0, 0, 1, 1, 0, 1], [0, 0, 1, 0, 0, 1, 1, 0], [1, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 0, 0, 1, 1, 0], [1, 1, 0, 0, 0, 1, 0, 1]]`

### `class DigitalState(IntEnum)`

An IntEnum of the different digital states that a digital signal can represent.

    You can use :class:`DigitalState` in place of an :any:`int`:

    >>> DigitalState.FORCE_OFF
    <DigitalState.FORCE_OFF: 2>
    >>> DigitalState.FORCE_OFF == 2
    True

    Use :meth:`from_char` and :meth:`to_char` to convert between states and characters:

    >>> DigitalState.from_char("Z")
    <DigitalState.FORCE_OFF: 2>
    >>> DigitalState.to_char(2)
    'Z'

    Use :meth:`test` to compare actual vs. expected states, returning True on failure.

    >>> DigitalState.test(DigitalState.FORCE_DOWN, DigitalState.COMPARE_LOW)
    False
    >>> DigitalState.test(DigitalState.FORCE_UP, DigitalState.COMPARE_LOW)
    True
    

#### `def char(self) -> str`

The character representing the digital state.

#### `def from_char(cls, char: str) -> DigitalState`

Look up the digital state for the corresponding character.

#### `def to_char(cls, state: DigitalState, errors: str='strict') -> str`

Get a character representing the digital state.

        Args:
            state: The digital state.
            errors: Specifies how to handle errors.

                * "strict": raise ``KeyError``
                * "replace": return "?"

        Returns:
            A character representing the digital state.
        

#### `def test(state1: DigitalState, state2: DigitalState) -> bool`

Test two digital states and return True if the test failed.

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_digital/_waveform.py -->
## PYTHON MODULE: src/nitypes/waveform/_digital/_waveform.py

### `class DigitalWaveformFailure()`

A test failure, indicating where the actual waveform did not match the expected waveform.

### `class DigitalWaveformTestResult()`

A test result from comparing a digital waveform against an expected digital waveform.

#### `def success(self) -> bool`

True if the test is successful, False if the test failed.

### `class DigitalWaveform(Generic[TDigitalState])`

A digital waveform, which encapsulates digital data and timing information.

    Constructing
    ^^^^^^^^^^^^

    To construct a digital waveform, use the :class:`DigitalWaveform` class:

    >>> DigitalWaveform()
    nitypes.waveform.DigitalWaveform(0, 1)
    >>> DigitalWaveform(sample_count=5, signal_count=3)  # doctest: +NORMALIZE_WHITESPACE
    nitypes.waveform.DigitalWaveform(5, 3, data=array([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
    [0, 0, 0]], dtype=uint8))

    When displaying a digital waveform as a string, the first number is the sample count and the second
    number is the signal count.

    To construct a digital waveform from a NumPy array of line data, use the
    :any:`DigitalWaveform.from_lines` method. Each array element represents a digital state, such as 1
    for "on" or 0 for "off". The line data should be in a 1D array indexed by sample or a 2D array
    indexed by (sample, signal). *(Note, signal indices are reversed! See "Signal index vs. column index"
    below for details.)* The digital waveform displays the line data as a 2D array.

    >>> import numpy as np
    >>> DigitalWaveform.from_lines(np.array([0, 1, 0], np.uint8))
    nitypes.waveform.DigitalWaveform(3, 1, data=array([[0], [1], [0]], dtype=uint8))
    >>> DigitalWaveform.from_lines(np.array([[0, 0], [1, 0], [0, 1], [1, 1]], np.uint8))
    nitypes.waveform.DigitalWaveform(4, 2, data=array([[0, 0], [1, 0], [0, 1], [1, 1]], dtype=uint8))

    You can also use :any:`DigitalWaveform.from_lines` to construct a digital waveform from a sequence,
    such as a list.

    >>> DigitalWaveform.from_lines([[0, 0], [1, 0], [0, 1], [1, 1]])
    nitypes.waveform.DigitalWaveform(4, 2, data=array([[0, 0], [1, 0], [0, 1], [1, 1]], dtype=uint8))

    To construct a digital waveform from a NumPy array of port data, use the
    :any:`DigitalWaveform.from_port` method. Each element of the port data array represents a digital
    sample taken over a port of signals. Each bit in the sample is a signal value, either 1 for "on" or
    0 for "off". *(Note, signal indices are reversed! See "Signal index vs. column index" below for
    details.)*

    >>> DigitalWaveform.from_port(np.array([0, 1, 2, 3], np.uint8))  # doctest: +NORMALIZE_WHITESPACE
    nitypes.waveform.DigitalWaveform(4, 8, data=array([[0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 1]], dtype=uint8))

    You can use a mask to specify which lines in the port to include in the waveform.

    >>> DigitalWaveform.from_port(np.array([0, 1, 2, 3], np.uint8), 0x3)
    nitypes.waveform.DigitalWaveform(4, 2, data=array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=uint8))

    You can also use a non-NumPy sequence such as a list, but you must specify a mask so the waveform
    knows how many bits are in each list element.

    >>> DigitalWaveform.from_port([0, 1, 2, 3], 0x3)
    nitypes.waveform.DigitalWaveform(4, 2, data=array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=uint8))

    The 2D version, :any:`DigitalWaveform.from_ports`, returns multiple waveforms, one for each row of
    data in the array or nested sequence.

    >>> nested_list = [[0, 1, 2, 3], [3, 0, 3, 0]]
    >>> DigitalWaveform.from_ports(nested_list, [0x3, 0x3])  # doctest: +NORMALIZE_WHITESPACE
    [nitypes.waveform.DigitalWaveform(4, 2, data=array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=uint8)),
    nitypes.waveform.DigitalWaveform(4, 2, data=array([[1, 1], [0, 0], [1, 1], [0, 0]], dtype=uint8))]

    Digital signals
    ^^^^^^^^^^^^^^^

    You can access individual signals using the :any:`DigitalWaveform.signals` property.

    >>> wfm = DigitalWaveform.from_port([0, 1, 2, 3], 0x3)
    >>> wfm.signals[0]
    nitypes.waveform.DigitalWaveformSignal(data=array([0, 1, 0, 1], dtype=uint8))
    >>> wfm.signals[1]
    nitypes.waveform.DigitalWaveformSignal(data=array([0, 0, 1, 1], dtype=uint8))

    The :any:`DigitalWaveformSignal.data` property returns a view of the data for that signal.

    >>> wfm.signals[0].data
    array([0, 1, 0, 1], dtype=uint8)

    Signal index vs. column index
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Each :class:`DigitalWaveformSignal` has two index properties:

    * :attr:`DigitalWaveformSignal.signal_index` - The position in the :attr:`DigitalWaveform.signals`
      collection (0-based from the first signal). signal_index 0 is the rightmost column in the data.
    * :attr:`DigitalWaveformSignal.column_index` - The column in the :attr:`DigitalWaveform.data`
      array, e.g. `waveform.data[:, column_index]`. column_index 0 is the leftmost column in the data.

    These indices are reversed with respect to each other. signal_index 0 (line 0) corresponds to
    the highest column_index, and the highest signal_index (the highest line) corresponds to
    column_index 0. This ordering follows industry conventions where line 0 is the least
    significant bit and appears last (in the rightmost column) of the data array.

    >>> wfm = DigitalWaveform.from_port([0, 1, 2, 3], 0x7)  # 3 signals
    >>> wfm.data
    array([[0, 0, 0],
           [0, 0, 1],
           [0, 1, 0],
           [0, 1, 1]], dtype=uint8)
    >>> wfm.signals[0].signal_index
    0
    >>> wfm.signals[0].column_index
    2
    >>> wfm.signals[0].data
    array([0, 1, 0, 1], dtype=uint8)
    >>> wfm.signals[2].signal_index
    2
    >>> wfm.signals[2].column_index
    0
    >>> wfm.signals[2].data
    array([0, 0, 0, 0], dtype=uint8)

    Digital signal names
    ^^^^^^^^^^^^^^^^^^^^

    The :any:`DigitalWaveformSignal.name` property allows you to get and set the signal names.

    >>> wfm.signals[0].name = "port0/line0"
    >>> wfm.signals[1].name = "port0/line1"
    >>> wfm.signals[2].name = "port0/line2"
    >>> wfm.signals[0].name
    'port0/line0'
    >>> wfm.signals[0]
    nitypes.waveform.DigitalWaveformSignal(name='port0/line0', data=array([0, 1, 0, 1], dtype=uint8))

    The signal names are stored in the ``NI_LineNames`` extended property on the digital waveform.
    Note that the order of the names in the string follows column_index order (highest line number
    first), which is reversed compared to signal_index order (lowest line first). This means line 0
    (signal_index 0) appears last in the NI_LineNames string. This matches industry conventions
    where line 0 appears in the rightmost column of the data array.

    >>> wfm.extended_properties["NI_LineNames"]
    'port0/line2, port0/line1, port0/line0'

    When creating a digital waveform, you can directly set the ``NI_LineNames`` extended property.

    >>> wfm = DigitalWaveform.from_port([2, 4], 0x7,
    ... extended_properties={"NI_LineNames": "Dev1/port1/line6, Dev1/port1/line5, Dev1/port1/line4"})
    >>> wfm.signals[0]
    nitypes.waveform.DigitalWaveformSignal(name='Dev1/port1/line4', data=array([0, 0], dtype=uint8))
    >>> wfm.signals[1]
    nitypes.waveform.DigitalWaveformSignal(name='Dev1/port1/line5', data=array([1, 0], dtype=uint8))
    >>> wfm.signals[2]
    nitypes.waveform.DigitalWaveformSignal(name='Dev1/port1/line6', data=array([0, 1], dtype=uint8))

    Digital state types
    ^^^^^^^^^^^^^^^^^^^

    By default, digital waveforms use a NumPy ``dtype`` of :any:`numpy.uint8`, which uses a byte of
    memory for each digital state.

    Using ``np.uint8`` allows the waveform to contain digital states other than "on" or off", such as
    such as :any:`DigitalState.FORCE_OFF` (``X``) or :any:`DigitalState.COMPARE_HIGH` (``H``). This
    capability is used for digital pattern applications.

    You can also construct a digital waveform using a NumPy ``dtype`` of :any:`numpy.bool`. This also
    uses a byte of memory for each digital state, but it restricts the states to "on" and "off".

    Testing digital waveforms
    ^^^^^^^^^^^^^^^^^^^^^^^^^

    You can use :meth:`DigitalWaveform.test` to compare an acquired waveform against an expected
    waveform. This returns a :class:`DigitalWaveformTestResult` object, which has a Boolean ``success``
    property and a ``failures`` property containing a collection of :class:`DigitalWaveformFailure`
    objects, which indicate the location of each test failure.

    Here is an example. The expected waveform counts in binary using ``COMPARE_LOW`` (``L``) and
    ``COMPARE_HIGH`` (``H``), but signal 0 of the actual waveform is stuck high.

    >>> actual = DigitalWaveform.from_lines([[0, 1], [1, 1], [0, 1], [1, 1]])
    >>> expected = DigitalWaveform.from_lines([[DigitalState.COMPARE_LOW, DigitalState.COMPARE_LOW],
    ... [DigitalState.COMPARE_HIGH, DigitalState.COMPARE_LOW],
    ... [DigitalState.COMPARE_LOW, DigitalState.COMPARE_HIGH],
    ... [DigitalState.COMPARE_HIGH, DigitalState.COMPARE_HIGH]])
    >>> result = actual.test(expected)
    >>> result.success
    False
    >>> len(result.failures)
    2

    The failures indicate the sample indices into the actual and expected waveforms, the signal index,
    and the digital state from the actual and expected waveforms:

    >>> result.failures[0]  # doctest: +NORMALIZE_WHITESPACE
    DigitalWaveformFailure(sample_index=0, expected_sample_index=0, signal_index=0,
    actual_state=<DigitalState.FORCE_UP: 1>, expected_state=<DigitalState.COMPARE_LOW: 3>)
    >>> result.failures[1]  # doctest: +NORMALIZE_WHITESPACE
    DigitalWaveformFailure(sample_index=1, expected_sample_index=1, signal_index=0,
    actual_state=<DigitalState.FORCE_UP: 1>, expected_state=<DigitalState.COMPARE_LOW: 3>)

    Timing information
    ^^^^^^^^^^^^^^^^^^

    Digital waveforms have the same timing information as analog waveforms.

    Class members
    ^^^^^^^^^^^^^
    

#### `def from_lines(cls, array: npt.NDArray[TOtherDigitalState], dtype: None=..., *, copy: bool=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., signal_count: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=...) -> DigitalWaveform[TOtherDigitalState]`

#### `def from_lines(cls, array: npt.NDArray[Any] | Sequence[Any], dtype: type[TOtherDigitalState] | np.dtype[TOtherDigitalState], *, copy: bool=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., signal_count: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=...) -> DigitalWaveform[TOtherDigitalState]`

#### `def from_lines(cls, array: npt.NDArray[Any] | Sequence[Any], dtype: npt.DTypeLike | None=..., *, copy: bool=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., signal_count: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=...) -> DigitalWaveform[Any]`

#### `def from_lines(cls, array: npt.NDArray[Any] | Sequence[Any], dtype: npt.DTypeLike | None=None, *, copy: bool=True, start_index: SupportsIndex | None=0, sample_count: SupportsIndex | None=None, signal_count: SupportsIndex | None=None, extended_properties: Mapping[str, ExtendedPropertyValue] | None=None, timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=None) -> DigitalWaveform[Any]`

Construct a waveform from a one or two-dimensional array or sequence of line data.

        Each element of the line data array represents a digital state, such as 1 for "on" or 0
        for "off". The line data should be in a 1D array indexed by sample or a 2D array indexed
        by (sample, signal). The line data may also use digital state values from the
        :class:`DigitalState` enum.

        Note that signal indices are reversed with respect to this array's column indices.
        The first column in each sample corresponds to the highest line number and highest signal
        index. The last column in each sample corresponds to line 0 and signal index 0.

        Args:
            array: The line data as a one or two-dimensional array or a sequence.
            dtype: The NumPy data type for the waveform data.
            copy: Specifies whether to copy the array or save a reference to it.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
            signal_count: The number of signals in the waveform.
            extended_properties: The extended properties of the waveform.
            timing: The timing information of the waveform.

        Returns:
            A waveform containing the specified data.
        

#### `def from_port(cls, array: npt.NDArray[Any] | Sequence[Any], mask: SupportsIndex | None=..., dtype: None=..., *, bitorder: Literal['big', 'little']=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=...) -> DigitalWaveform[np.uint8]`

#### `def from_port(cls, array: npt.NDArray[Any] | Sequence[Any], mask: SupportsIndex | None=..., dtype: type[TOtherDigitalState] | np.dtype[TOtherDigitalState]=..., *, bitorder: Literal['big', 'little']=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=...) -> DigitalWaveform[TOtherDigitalState]`

#### `def from_port(cls, array: npt.NDArray[Any] | Sequence[Any], mask: SupportsIndex | None=..., dtype: npt.DTypeLike | None=..., *, bitorder: Literal['big', 'little']=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=...) -> DigitalWaveform[Any]`

#### `def from_port(cls, array: npt.NDArray[Any] | Sequence[Any], mask: SupportsIndex | None=None, dtype: npt.DTypeLike | None=None, *, bitorder: Literal['big', 'little']='big', start_index: SupportsIndex | None=0, sample_count: SupportsIndex | None=None, extended_properties: Mapping[str, ExtendedPropertyValue] | None=None, timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=None) -> DigitalWaveform[Any]`

Construct a waveform from a one-dimensional array or sequence of port data.

        This method allocates a new array in order to convert the port data (integers) to line data
        (bits).

        Each element of the port data array represents a digital sample taken over a port of
        signals. Each bit in the sample represents a digital state, either 1 for "on" or 0 for
        "off".

        When bitorder='big' (default), the integers in the samples are big-endian. The most
        significant bit of each integer will be placed in the first column of the data array
        (corresponding to the highest line number and highest signal index). The least significant
        bit will be placed in the last column of the data array (corresponding to line 0 and signal
        index 0).

        When bitorder='little', the integers in the samples are little-endian. The least
        significant bit of each integer will be placed in the first column of the data array
        (corresponding to the highest line number and highest signal index). The most significant
        bit will be placed in the last column of the data array (corresponding to line 0 and signal
        index 0).

        If the input array is not a NumPy array, you must specify the mask.

        Args:
            array: The port data as a one-dimensional array or a sequence.
            mask: A bitmask specifying which lines to include in the waveform.
            dtype: The NumPy data type for the waveform (line) data.
            bitorder: The bit ordering to use when unpacking port data ('big' or 'little').
                Defaults to 'big'.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
            extended_properties: The extended properties of the waveform.
            timing: The timing information of the waveform.

        Returns:
            A waveform containing the specified data.
        

#### `def from_ports(cls, array: npt.NDArray[Any] | Sequence[Any], masks: Sequence[SupportsIndex] | None=..., dtype: None=..., *, bitorder: Literal['big', 'little']=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=...) -> Sequence[DigitalWaveform[np.uint8]]`

#### `def from_ports(cls, array: npt.NDArray[Any] | Sequence[Any], masks: Sequence[SupportsIndex] | None=..., dtype: type[TOtherDigitalState] | np.dtype[TOtherDigitalState]=..., *, bitorder: Literal['big', 'little']=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=...) -> Sequence[DigitalWaveform[TOtherDigitalState]]`

#### `def from_ports(cls, array: npt.NDArray[Any] | Sequence[Any], masks: Sequence[SupportsIndex] | None=..., dtype: npt.DTypeLike | None=..., *, bitorder: Literal['big', 'little']=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=...) -> Sequence[DigitalWaveform[Any]]`

#### `def from_ports(cls, array: npt.NDArray[Any] | Sequence[Any], masks: Sequence[SupportsIndex] | None=None, dtype: npt.DTypeLike | None=None, *, bitorder: Literal['big', 'little']='big', start_index: SupportsIndex | None=0, sample_count: SupportsIndex | None=None, extended_properties: Mapping[str, ExtendedPropertyValue] | None=None, timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=None) -> Sequence[DigitalWaveform[Any]]`

Construct a waveform from a two-dimensional array or sequence of port data.

        This method allocates a new array in order to convert the port data to line data.

        Each row of the port data array corresponds to a resulting DigitalWaveform. Each element of
        the port data array represents a digital sample taken over a port of signals. Each bit in
        the sample represents a digital state, either 1 for "on" or 0 for "off".

        When bitorder='big' (default), the integers in the samples are big-endian. The most
        significant bit of each integer will be placed in the first column of the data array
        (corresponding to the highest line number and highest signal index). The least significant
        bit will be placed in the last column of the data array (corresponding to line 0 and signal
        index 0).

        When bitorder='little', the integers in the samples are little-endian. The least
        significant bit of each integer will be placed in the first column of the data array
        (corresponding to the highest line number and highest signal index). The most significant
        bit will be placed in the last column of the data array (corresponding to line 0 and signal
        index 0).

        If the input array is not a NumPy array, you must specify the masks.

        Args:
            array: The port data as a two-dimensional array or a sequence.
            masks: A sequence of bitmasks specifying which lines from each port to include in the
                corresponding waveform.
            dtype: The NumPy data type for the waveform (line) data.
            bitorder: The bit ordering to use when unpacking port data ('big' or 'little').
                Defaults to 'big'.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
            extended_properties: The extended properties of the waveform.
            timing: The timing information of the waveform.

        Returns:
            A waveform containing the specified data.
        

#### `def __init__(self: DigitalWaveform[np.uint8], sample_count: SupportsIndex | None=..., signal_count: SupportsIndex | None=..., dtype: None=..., default_value: bool | int | DigitalState | None=..., *, data: None=..., start_index: SupportsIndex | None=..., capacity: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., copy_extended_properties: bool=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=...) -> None`

#### `def __init__(self: DigitalWaveform[TOtherDigitalState], sample_count: SupportsIndex | None=..., signal_count: SupportsIndex | None=..., dtype: type[TOtherDigitalState] | np.dtype[TOtherDigitalState]=..., default_value: bool | int | DigitalState | None=..., *, data: None=..., start_index: SupportsIndex | None=..., capacity: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., copy_extended_properties: bool=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=...) -> None`

#### `def __init__(self: DigitalWaveform[TOtherDigitalState], sample_count: SupportsIndex | None=..., signal_count: SupportsIndex | None=..., dtype: None=..., default_value: bool | int | DigitalState | None=..., *, data: npt.NDArray[TOtherDigitalState]=..., start_index: SupportsIndex | None=..., capacity: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., copy_extended_properties: bool=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=...) -> None`

#### `def __init__(self: DigitalWaveform[Any], sample_count: SupportsIndex | None=..., signal_count: SupportsIndex | None=..., dtype: npt.DTypeLike | None=..., default_value: bool | int | DigitalState | None=..., *, data: npt.NDArray[Any] | None=..., start_index: SupportsIndex | None=..., capacity: SupportsIndex | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., copy_extended_properties: bool=..., timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=...) -> None`

#### `def __init__(self, sample_count: SupportsIndex | None=None, signal_count: SupportsIndex | None=None, dtype: npt.DTypeLike | None=None, default_value: bool | int | DigitalState | None=None, *, data: npt.NDArray[Any] | None=None, start_index: SupportsIndex | None=None, capacity: SupportsIndex | None=None, extended_properties: Mapping[str, ExtendedPropertyValue] | None=None, copy_extended_properties: bool=True, timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=None) -> None`

Initialize a new digital waveform.

        Args:
            sample_count: The number of samples in the waveform.
            signal_count: The number of signals in the waveform.
            dtype: The NumPy data type for the waveform data.
            default_value: The :class:`DigitalState` to initialize the waveform with.
            data: A NumPy ndarray to use for sample storage. The waveform takes ownership
                of this array. If not specified, an ndarray is created based on the specified dtype,
                start index, sample count, and capacity.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
            capacity: The number of samples to allocate. Pre-allocating a larger buffer optimizes
                appending samples to the waveform.
            extended_properties: The extended properties of the waveform.
            copy_extended_properties: Specifies whether to copy the extended properties or take
                ownership.
            timing: The timing information of the waveform.

        Returns:
            A digital waveform.
        

#### `def _on_extended_property_changed(self, key: str) -> None`

#### `def _init_with_new_array(self, sample_count: SupportsIndex | None=None, signal_count: SupportsIndex | None=None, dtype: npt.DTypeLike | None=None, default_value: bool | int | DigitalState | None=None, *, start_index: SupportsIndex | None=None, capacity: SupportsIndex | None=None) -> None`

#### `def _init_with_provided_array(self, data: npt.NDArray[TDigitalState], dtype: npt.DTypeLike | None=None, *, start_index: SupportsIndex | None=None, sample_count: SupportsIndex | None=None, signal_count: SupportsIndex | None=None, capacity: SupportsIndex | None=None) -> None`

#### `def signals(self) -> DigitalWaveformSignalCollection[TDigitalState]`

A collection of objects representing waveform signals.

#### `def data(self) -> npt.NDArray[TDigitalState]`

The waveform data, indexed by (sample, signal).

#### `def get_data(self, start_index: SupportsIndex | None=0, sample_count: SupportsIndex | None=None) -> npt.NDArray[TDigitalState]`

Get a subset of the waveform data.

        Args:
            start_index: The sample index at which the data begins.
            sample_count: The number of samples to return.

        Returns:
            A subset of the raw waveform data.
        

#### `def sample_count(self) -> int`

The number of samples in the waveform.

#### `def sample_count(self, value: int) -> None`

Set the number of samples in the waveform.

#### `def signal_count(self) -> int`

The number of signals in the waveform.

#### `def start_index(self) -> int`

The sample index of the underlying array at which the waveform data begins.

#### `def capacity(self) -> int`

The total capacity available for waveform data.

        Setting the capacity resizes the underlying NumPy array in-place.

        * Other Python objects with references to the array will see the array size change.
        * If the array has a reference to an external buffer (such as an array.array), attempting
          to resize it raises ValueError.
        

#### `def capacity(self, value: int) -> None`

#### `def dtype(self) -> np.dtype[TDigitalState]`

The NumPy dtype for the waveform data.

#### `def extended_properties(self) -> ExtendedPropertyDictionary`

The extended properties for the waveform.

#### `def channel_name(self) -> str`

The name of the device channel from which the waveform was acquired.

#### `def channel_name(self, value: str) -> None`

#### `def _get_line_names(self) -> list[str]`

#### `def _get_line_name(self, column_index: int) -> str`

#### `def _set_line_name(self, column_index: int, value: str) -> None`

#### `def _set_timing(self, value: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta]) -> None`

#### `def _validate_timing(self, value: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta]) -> None`

#### `def timing(self) -> Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta]`

The timing information of the waveform.

        The default value is Timing.empty.
        

#### `def timing(self, value: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta]) -> None`

#### `def append(self, other: npt.NDArray[TDigitalState] | DigitalWaveform[TDigitalState] | Sequence[DigitalWaveform[TDigitalState]], /, timestamps: Sequence[dt.datetime] | Sequence[ht.datetime] | None=None) -> None`

Append data to the waveform.

        Args:
            other: The array or waveform(s) to append.
            timestamps: A sequence of timestamps. When the current waveform has
                SampleIntervalMode.IRREGULAR, you must provide a sequence of timestamps with the
                same length as the array.

        Raises:
            TimingMismatchError: The current and other waveforms have incompatible timing.
            TimingMismatchWarning: The sample intervals of the waveform(s) do not match.
            ValueError: The other array has the wrong number of dimensions or the length of the
                timestamps argument does not match the length of the other array.
            TypeError: The data types of the current waveform and other array or waveform(s) do not
                match, or an argument has the wrong data type.

        When appending waveforms:

        * Timing information is merged based on the sample interval mode of the current
          waveform:

          * SampleIntervalMode.NONE or SampleIntervalMode.REGULAR: The other waveform(s) must also
            have SampleIntervalMode.NONE or SampleIntervalMode.REGULAR. If the sample interval does
            not match, a TimingMismatchWarning is generated. Otherwise, the timing information of
            the other waveform(s) is discarded.

          * SampleIntervalMode.IRREGULAR: The other waveforms(s) must also have
            SampleIntervalMode.IRREGULAR. The timestamps of the other waveforms(s) are appended to
            the current waveform's timing information.

        * Extended properties of the other waveform(s) are merged into the current waveform if they
          are not already set in the current waveform.
        

#### `def _append_array(self, array: npt.NDArray[TDigitalState], timestamps: Sequence[dt.datetime] | Sequence[ht.datetime] | None=None) -> None`

#### `def _append_waveform(self, waveform: DigitalWaveform[TDigitalState]) -> None`

#### `def _append_waveforms(self, waveforms: Sequence[DigitalWaveform[TDigitalState]]) -> None`

#### `def _increase_capacity(self, amount: int) -> None`

#### `def load_data(self, array: npt.NDArray[TDigitalState], *, copy: bool=True, start_index: SupportsIndex | None=0, sample_count: SupportsIndex | None=None) -> None`

Load new data into an existing waveform.

        Args:
            array: A NumPy array containing the data to load.
            copy: Specifies whether to copy the array or save a reference to it.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
        

#### `def _load_array(self, array: npt.NDArray[TDigitalState], *, copy: bool=True, start_index: SupportsIndex | None=0, sample_count: SupportsIndex | None=None, signal_count: SupportsIndex | None=None) -> None`

#### `def test(self, expected_waveform: DigitalWaveform[TDigitalState], *, start_sample: SupportsIndex | None=0, expected_start_sample: SupportsIndex | None=0, sample_count: SupportsIndex | None=None) -> DigitalWaveformTestResult`

Test the digital waveform against an expected digital waveform.

        Args:
            expected_waveform: The expected digital waveform to compare against.
            start_sample: The beginning sample of ``self`` to compare.
            expected_start_sample: The beginning sample of ``expected_waveform`` to compare.
            sample_count: The number of samples to compare.

        Returns:
            The test result.
        

#### `def _reverse_index(self, index: int) -> int`

Convert a signal_index to a column_index, or vice versa.

#### `def __eq__(self, value: object, /) -> bool`

Return self==value.

#### `def __reduce__(self) -> tuple[Any, ...]`

Return object state for pickling.

#### `def _unpickle(cls, args: tuple[Any, ...], kwargs: dict[str, Any]) -> Self`

#### `def __repr__(self) -> str`

Return repr(self).

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_exceptions.py -->
## PYTHON MODULE: src/nitypes/waveform/_exceptions.py

### `def create_capacity_mismatch_error(capacity: int, array_length: int) -> CapacityMismatchError`

Create an error for a capacity-length mismatch.

### `def create_capacity_too_small_error(capacity: int, min_capacity: int, object_description: str) -> CapacityTooSmallError`

Create an error for when capacity is too small.

### `def create_datatype_mismatch_error(arg_description: Literal['input array', 'input spectrum', 'input waveform'], arg_dtype: object, other_description: Literal['requested', 'spectrum', 'waveform'], other_dtype: object) -> DatatypeMismatchError`

Create an error for a data type mismatch.

### `def create_irregular_timestamp_count_mismatch_error(irregular_timestamp_count: int, other_description: Literal['input array length', 'number of samples in the waveform'], other: int, *, reversed: bool=False) -> IrregularTimestampCountMismatchError`

Create an error for an irregular timestamp count mismatch.

### `def create_start_index_too_large_error(start_index: int, capacity_description: Literal['capacity', 'input array length', 'number of samples in the spectrum', 'number of samples in the waveform'], capacity: int) -> StartIndexTooLargeError`

Create an error for an invalid start index argument.

### `def create_start_index_or_sample_count_too_large_error(start_index: int, sample_count: int, capacity_description: Literal['capacity', 'input array length', 'number of samples in the expected waveform', 'number of samples in the spectrum', 'number of samples in the waveform'], capacity: int) -> StartIndexOrSampleCountTooLargeError`

Create an error for an invalid start index or sample count argument.

### `def create_no_timestamp_information_error() -> NoTimestampInformationError`

Create an error for waveform timing with no timestamp information.

### `def create_sample_interval_mode_mismatch_error() -> SampleIntervalModeMismatchError`

Create an error for mixing none/regular with irregular timing.

### `def create_signal_count_mismatch_error(arg_description: Literal['expected waveform', 'input array', 'input waveform', 'provided'], arg_signal_count: int, other_description: Literal['array', 'port', 'waveform'], other_signal_count: int) -> SignalCountMismatchError`

Create an error for a mismatched signal count.

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_extended_properties.py -->
## PYTHON MODULE: src/nitypes/waveform/_extended_properties.py

- `CHANNEL_NAME = 'NI_ChannelName'`

- `LINE_NAMES = 'NI_LineNames'`

- `UNIT_DESCRIPTION = 'NI_UnitDescription'`

### `class ExtendedPropertyDictionary(MutableMapping[str, ExtendedPropertyValue])`

A dictionary of extended properties.

    .. note::
        Data stored in the extended properties dictionary may not be encrypted when you send it
        over the network or write it to a TDMS file.
    

#### `def __init__(self, properties: Mapping[str, ExtendedPropertyValue] | None=None, /) -> None`

Initialize a new ExtendedPropertyDictionary.

#### `def __len__(self) -> int`

Return len(self).

#### `def __iter__(self) -> Iterator[str]`

Implement iter(self).

#### `def __contains__(self, value: object, /) -> bool`

Implement value in self.

#### `def __getitem__(self, key: str, /) -> ExtendedPropertyValue`

Get self[key].

#### `def __setitem__(self, key: str, value: ExtendedPropertyValue, /) -> None`

Set self[key] to value.

#### `def __delitem__(self, key: str, /) -> None`

Delete self[key].

#### `def _notify_on_key_changed(self, key: str) -> None`

#### `def _merge(self, other: ExtendedPropertyDictionary) -> None`

#### `def __reduce__(self) -> tuple[type[ExtendedPropertyDictionary], tuple[dict[str, ExtendedPropertyValue]]]`

Return object state for pickling, excluding the callback.

#### `def __repr__(self) -> str`

Return repr(self).

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_numeric.py -->
## PYTHON MODULE: src/nitypes/waveform/_numeric.py

### `class NumericWaveform(ABC, Generic[_TRaw, _TScaled])`

A numeric waveform, which encapsulates numeric data and timing information.

    This is an abstract base class. To create a numeric waveform, use :class:`AnalogWaveform` or
    :class:`ComplexWaveform`.
    

#### `def _get_default_raw_dtype() -> type[np.generic] | np.dtype[np.generic]`

#### `def _get_default_scaled_dtype() -> type[np.generic] | np.dtype[np.generic]`

#### `def _get_supported_raw_dtypes() -> tuple[npt.DTypeLike, ...]`

#### `def _get_supported_scaled_dtypes() -> tuple[npt.DTypeLike, ...]`

#### `def from_array_1d(cls, array: npt.NDArray[Any] | Sequence[Any], dtype: npt.DTypeLike | None=None, *, copy: bool=True, start_index: SupportsIndex | None=0, sample_count: SupportsIndex | None=None, extended_properties: Mapping[str, ExtendedPropertyValue] | None=None, timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=None, scale_mode: ScaleMode | None=None) -> Self`

Construct a waveform from a one-dimensional array or sequence.

        Args:
            array: The waveform data as a one-dimensional array or a sequence.
            dtype: The NumPy data type for the waveform data. This argument is required
                when array is a sequence.
            copy: Specifies whether to copy the array or save a reference to it.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
            extended_properties: The extended properties of the waveform.
            timing: The timing information of the waveform.
            scale_mode: The scale mode of the waveform.

        Returns:
            A waveform containing the specified data.
        

#### `def from_array_2d(cls, array: npt.NDArray[Any] | Sequence[Sequence[Any]], dtype: npt.DTypeLike | None=None, *, copy: bool=True, start_index: SupportsIndex | None=0, sample_count: SupportsIndex | None=None, extended_properties: Mapping[str, ExtendedPropertyValue] | None=None, timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=None, scale_mode: ScaleMode | None=None) -> Sequence[Self]`

Construct multiple waveforms from a two-dimensional array or nested sequence.

        Args:
            array: The waveform data as a two-dimensional array or a nested sequence.
            dtype: The NumPy data type for the waveform data. This argument is required
                when array is a sequence.
            copy: Specifies whether to copy the array or save a reference to it.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
            extended_properties: The extended properties of the waveform.
            timing: The timing information of the waveform.
            scale_mode: The scale mode of the waveform.

        Returns:
            A sequence containing a waveform for each row of the specified data.

        When constructing multiple waveforms, the same extended properties, timing
        information, and scale mode are applied to all waveforms. Consider assigning
        these properties after construction.
        

#### `def __init__(self, sample_count: SupportsIndex | None=None, dtype: npt.DTypeLike | None=None, *, raw_data: npt.NDArray[_TRaw] | None=None, start_index: SupportsIndex | None=None, capacity: SupportsIndex | None=None, extended_properties: Mapping[str, ExtendedPropertyValue] | None=None, copy_extended_properties: bool=True, timing: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta] | None=None, scale_mode: ScaleMode | None=None) -> None`

Initialize a new numeric waveform.

        Args:
            sample_count: The number of samples in the waveform.
            dtype: The NumPy data type for the waveform data.
            raw_data: A NumPy ndarray to use for sample storage. The waveform takes ownership
                of this array. If not specified, an ndarray is created based on the specified dtype,
                start index, sample count, and capacity.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
            capacity: The number of samples to allocate. Pre-allocating a larger buffer optimizes
                appending samples to the waveform.
            extended_properties: The extended properties of the waveform.
            copy_extended_properties: Specifies whether to copy the extended properties or take
                ownership.
            timing: The timing information of the waveform.
            scale_mode: The scale mode of the waveform.

        Returns:
            A numeric waveform.
        

#### `def _init_with_new_array(self, sample_count: SupportsIndex | None=None, dtype: npt.DTypeLike | None=None, *, start_index: SupportsIndex | None=None, capacity: SupportsIndex | None=None) -> None`

#### `def _init_with_provided_array(self, data: npt.NDArray[_TRaw], dtype: npt.DTypeLike | None=None, *, start_index: SupportsIndex | None=None, sample_count: SupportsIndex | None=None, capacity: SupportsIndex | None=None) -> None`

#### `def raw_data(self) -> npt.NDArray[_TRaw]`

The raw waveform data.

#### `def get_raw_data(self, start_index: SupportsIndex | None=0, sample_count: SupportsIndex | None=None) -> npt.NDArray[_TRaw]`

Get a subset of the raw waveform data.

        Args:
            start_index: The sample index at which the data begins.
            sample_count: The number of samples to return.

        Returns:
            A subset of the raw waveform data.
        

#### `def scaled_data(self) -> npt.NDArray[_TScaled]`

The scaled waveform data.

        This property converts all of the waveform samples from the raw data type to the scaled
        data type and scales them using :attr:`scale_mode`. To scale a subset of the waveform or
        scale to single-precision floating point, use the :meth:`get_scaled_data` method
        instead.
        

#### `def get_scaled_data(self, dtype: None=..., *, start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=...) -> npt.NDArray[_TScaled]`

#### `def get_scaled_data(self, dtype: type[_TOtherScaled] | np.dtype[_TOtherScaled], *, start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=...) -> npt.NDArray[_TOtherScaled]`

#### `def get_scaled_data(self, dtype: npt.DTypeLike=..., *, start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=...) -> npt.NDArray[Any]`

#### `def get_scaled_data(self, dtype: npt.DTypeLike | None=None, *, start_index: SupportsIndex | None=0, sample_count: SupportsIndex | None=None) -> npt.NDArray[Any]`

Get a subset of the scaled waveform data with the specified dtype.

        Args:
            dtype: The NumPy data type to use for scaled data.
            start_index: The sample index at which to start scaling.
            sample_count: The number of samples to scale.

        Returns:
            A subset of the scaled waveform data.
        

#### `def _convert_data(self, dtype: npt.DTypeLike | type[_TOtherScaled] | np.dtype[_TOtherScaled], raw_data: npt.NDArray[_TRaw]) -> npt.NDArray[_TOtherScaled]`

#### `def sample_count(self) -> int`

The number of samples in the waveform.

#### `def sample_count(self, value: int) -> None`

Set the number of samples in the waveform.

#### `def start_index(self) -> int`

The sample index of the underlying array at which the waveform data begins.

#### `def capacity(self) -> int`

The total capacity available for waveform data.

        Setting the capacity resizes the underlying NumPy array in-place.

        * Other Python objects with references to the array will see the array size change.
        * If the array has a reference to an external buffer (such as an array.array), attempting
          to resize it raises ValueError.
        

#### `def capacity(self, value: int) -> None`

#### `def dtype(self) -> np.dtype[_TRaw]`

The NumPy dtype for the waveform data.

#### `def extended_properties(self) -> ExtendedPropertyDictionary`

The extended properties for the waveform.

        .. note::
            Data stored in the extended properties dictionary may not be encrypted when you send it
            over the network or write it to a TDMS file.
        

#### `def channel_name(self) -> str`

The name of the device channel from which the waveform was acquired.

#### `def channel_name(self, value: str) -> None`

#### `def units(self) -> str`

The unit of measurement, such as volts, of the waveform.

#### `def units(self, value: str) -> None`

#### `def _set_timing(self, value: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta]) -> None`

#### `def _validate_timing(self, value: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta]) -> None`

#### `def timing(self) -> Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta]`

The timing information of the waveform.

        The default value is Timing.empty.
        

#### `def timing(self, value: Timing[AnyDateTime, AnyTimeDelta, AnyTimeDelta]) -> None`

#### `def scale_mode(self) -> ScaleMode`

The scale mode of the waveform.

#### `def scale_mode(self, value: ScaleMode) -> None`

#### `def append(self, other: npt.NDArray[_TRaw] | NumericWaveform[_TRaw, _TScaled] | Sequence[NumericWaveform[_TRaw, _TScaled]], /, timestamps: Sequence[dt.datetime] | Sequence[ht.datetime] | None=None) -> None`

Append data to the waveform.

        Args:
            other: The array or waveform(s) to append.
            timestamps: A sequence of timestamps. When the current waveform has
                SampleIntervalMode.IRREGULAR, you must provide a sequence of timestamps with the
                same length as the array.

        Raises:
            TimingMismatchError: The current and other waveforms have incompatible timing.
            TimingMismatchWarning: The sample intervals of the waveform(s) do not match.
            ScalingMismatchWarning: The scale modes of the waveform(s) do not match.
            ValueError: The other array has the wrong number of dimensions or the length of the
                timestamps argument does not match the length of the other array.
            TypeError: The data types of the current waveform and other array or waveform(s) do not
                match, or an argument has the wrong data type.

        When appending waveforms:

        * Timing information is merged based on the sample interval mode of the current
          waveform:

          * SampleIntervalMode.NONE or SampleIntervalMode.REGULAR: The other waveform(s) must also
            have SampleIntervalMode.NONE or SampleIntervalMode.REGULAR. If the sample interval does
            not match, a TimingMismatchWarning is generated. Otherwise, the timing information of
            the other waveform(s) is discarded.

          * SampleIntervalMode.IRREGULAR: The other waveforms(s) must also have
            SampleIntervalMode.IRREGULAR. The timestamps of the other waveforms(s) are appended to
            the current waveform's timing information.

        * Extended properties of the other waveform(s) are merged into the current waveform if they
          are not already set in the current waveform.

        * If the scale mode of other waveform(s) does not match the scale mode of the current
          waveform, a ScalingMismatchWarning is generated. Otherwise, the scaling information of the
          other waveform(s) is discarded.
        

#### `def _append_array(self, array: npt.NDArray[_TRaw], timestamps: Sequence[dt.datetime] | Sequence[ht.datetime] | None=None) -> None`

#### `def _append_waveform(self, waveform: NumericWaveform[_TRaw, _TScaled]) -> None`

#### `def _append_waveforms(self, waveforms: Sequence[NumericWaveform[_TRaw, _TScaled]]) -> None`

#### `def _increase_capacity(self, amount: int) -> None`

#### `def load_data(self, array: npt.NDArray[_TRaw], *, copy: bool=True, start_index: SupportsIndex | None=0, sample_count: SupportsIndex | None=None) -> None`

Load new data into an existing waveform.

        Args:
            array: A NumPy array containing the data to load.
            copy: Specifies whether to copy the array or save a reference to it.
            start_index: The sample index at which the waveform data begins.
            sample_count: The number of samples in the waveform.
        

#### `def _load_array(self, array: npt.NDArray[_TRaw], *, copy: bool=True, start_index: SupportsIndex | None=0, sample_count: SupportsIndex | None=None) -> None`

#### `def __eq__(self, value: object, /) -> bool`

Return self==value.

#### `def __reduce__(self) -> tuple[Any, ...]`

Return object state for pickling.

#### `def _unpickle(cls, args: tuple[Any, ...], kwargs: dict[str, Any]) -> Self`

#### `def __repr__(self) -> str`

Return repr(self).

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_scaling/__init__.py -->
## PYTHON MODULE: src/nitypes/waveform/_scaling/__init__.py

### MODULE DOCSTRING

Waveform scaling data types for NI Python APIs.

- `__all__ = ['LinearScaleMode', 'NO_SCALING', 'NoneScaleMode', 'ScaleMode']`

- `NO_SCALING = NoneScaleMode()`

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_scaling/_base.py -->
## PYTHON MODULE: src/nitypes/waveform/_scaling/_base.py

### `class ScaleMode(ABC)`

An object that specifies how the waveform is scaled.

#### `def _transform_data(self, data: npt.NDArray[_ScalarType]) -> npt.NDArray[_ScalarType]`

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_scaling/_linear.py -->
## PYTHON MODULE: src/nitypes/waveform/_scaling/_linear.py

### `class LinearScaleMode(ScaleMode)`

A scale mode that scales data linearly.

#### `def __init__(self, gain: SupportsFloat, offset: SupportsFloat) -> None`

Initialize a new scale mode object that scales data linearly.

        Args:
            gain: The gain of the linear scale.
            offset: The offset of the linear scale.

        Returns:
            A scale mode that scales data linearly.
        

#### `def gain(self) -> float`

The gain of the linear scale.

#### `def offset(self) -> float`

The offset of the linear scale.

#### `def _transform_data(self, data: npt.NDArray[_ScalarType]) -> npt.NDArray[_ScalarType]`

#### `def __eq__(self, value: object, /) -> bool`

Return self==value.

#### `def __repr__(self) -> str`

Return repr(self).

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_scaling/_none.py -->
## PYTHON MODULE: src/nitypes/waveform/_scaling/_none.py

### `class NoneScaleMode(ScaleMode)`

A scale mode that does not scale data.

#### `def _transform_data(self, data: npt.NDArray[_ScalarType]) -> npt.NDArray[_ScalarType]`

#### `def __eq__(self, value: object, /) -> bool`

Return self==value.

#### `def __repr__(self) -> str`

Return repr(self).

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_spectrum.py -->
## PYTHON MODULE: src/nitypes/waveform/_spectrum.py

- `_DATA_DTYPES = (np.single, np.double, np.byte, np.short, np.intc, np.int_, _np_long, np.longlong, np.ubyte, np.ushort, np.uintc, np.uint, _np_ulong, np.ulonglong)`

### `class Spectrum(Generic[_TData])`

A frequency spectrum, which encapsulates analog data and frequency information.

    Constructing
    ^^^^^^^^^^^^

    To construct a frequency spectrum, use the :class:`Spectrum` class:

    >>> Spectrum()
    nitypes.waveform.Spectrum(0)
    >>> Spectrum(5)
    nitypes.waveform.Spectrum(5, data=array([0., 0., 0., 0., 0.]))

    To construct a frequency spectrum from a NumPy array, use the :any:`Spectrum.from_array_1d`
    method.

    >>> import numpy as np
    >>> Spectrum.from_array_1d(np.array([1.0, 2.0, 3.0]))
    nitypes.waveform.Spectrum(3, data=array([1., 2., 3.]))

    You can also use :any:`Spectrum.from_array_1d` to construct a frequency spectrum from a
    sequence, such as a list. In this case, you must specify the NumPy data type.

    >>> Spectrum.from_array_1d([1.0, 2.0, 3.0], np.float64)
    nitypes.waveform.Spectrum(3, data=array([1., 2., 3.]))

    The 2D version, :any:`Spectrum.from_array_2d`, returns multiple waveforms, one for each row of
    data in the array or nested sequence.

    >>> nested_list = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    >>> Spectrum.from_array_2d(nested_list, np.float64)  # doctest: +NORMALIZE_WHITESPACE
    [nitypes.waveform.Spectrum(3, data=array([1., 2., 3.])),
    nitypes.waveform.Spectrum(3, data=array([4., 5., 6.]))]

    Class members
    ^^^^^^^^^^^^^
    

#### `def from_array_1d(cls, array: npt.NDArray[_TOtherData], dtype: None=..., *, copy: bool=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., start_frequency: SupportsFloat | None=..., frequency_increment: SupportsFloat | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=...) -> Spectrum[_TOtherData]`

#### `def from_array_1d(cls, array: npt.NDArray[Any] | Sequence[Any], dtype: type[_TOtherData] | np.dtype[_TOtherData], *, copy: bool=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., start_frequency: SupportsFloat | None=..., frequency_increment: SupportsFloat | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=...) -> Spectrum[_TOtherData]`

#### `def from_array_1d(cls, array: npt.NDArray[Any] | Sequence[Any], dtype: npt.DTypeLike | None=..., *, copy: bool=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., start_frequency: SupportsFloat | None=..., frequency_increment: SupportsFloat | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=...) -> Spectrum[Any]`

#### `def from_array_1d(cls, array: npt.NDArray[Any] | Sequence[Any], dtype: npt.DTypeLike | None=None, *, copy: bool=True, start_index: SupportsIndex | None=0, sample_count: SupportsIndex | None=None, start_frequency: SupportsFloat | None=None, frequency_increment: SupportsFloat | None=None, extended_properties: Mapping[str, ExtendedPropertyValue] | None=None) -> Spectrum[Any]`

Construct a spectrum from a one-dimensional array or sequence.

        Args:
            array: The spectrum data as a one-dimensional array or a sequence.
            dtype: The NumPy data type for the spectrum data. This argument is required
                when array is a sequence.
            copy: Specifies whether to copy the array or save a reference to it.
            start_index: The sample index at which the spectrum data begins.
            sample_count: The number of samples in the spectrum.
            start_frequency: The start frequency of the spectrum.
            frequency_increment: The frequency increment of the spectrum.
            extended_properties: The extended properties of the spectrum.

        Returns:
            A spectrum containing the specified data.
        

#### `def from_array_2d(cls, array: npt.NDArray[_TOtherData], dtype: None=..., *, copy: bool=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., start_frequency: SupportsFloat | None=..., frequency_increment: SupportsFloat | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=...) -> Sequence[Spectrum[_TOtherData]]`

#### `def from_array_2d(cls, array: npt.NDArray[Any] | Sequence[Sequence[Any]], dtype: type[_TOtherData] | np.dtype[_TOtherData], *, copy: bool=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., start_frequency: SupportsFloat | None=..., frequency_increment: SupportsFloat | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=...) -> Sequence[Spectrum[_TOtherData]]`

#### `def from_array_2d(cls, array: npt.NDArray[Any] | Sequence[Sequence[Any]], dtype: npt.DTypeLike | None=..., *, copy: bool=..., start_index: SupportsIndex | None=..., sample_count: SupportsIndex | None=..., start_frequency: SupportsFloat | None=..., frequency_increment: SupportsFloat | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=...) -> Sequence[Spectrum[Any]]`

#### `def from_array_2d(cls, array: npt.NDArray[Any] | Sequence[Sequence[Any]], dtype: npt.DTypeLike | None=None, *, copy: bool=True, start_index: SupportsIndex | None=0, sample_count: SupportsIndex | None=None, start_frequency: SupportsFloat | None=None, frequency_increment: SupportsFloat | None=None, extended_properties: Mapping[str, ExtendedPropertyValue] | None=None) -> Sequence[Spectrum[Any]]`

Construct a list of spectrums from a two-dimensional array or nested sequence.

        Args:
            array: The spectrum data as a two-dimensional array or a nested sequence.
            dtype: The NumPy data type for the spectrum data. This argument is required
                when array is a sequence.
            copy: Specifies whether to copy the array or save a reference to it.
            start_index: The sample index at which the spectrum data begins.
            sample_count: The number of samples in the spectrum.
            start_frequency: The start frequency of the spectrum.
            frequency_increment: The frequency increment of the spectrum.
            extended_properties: The extended properties of the spectrum.

        Returns:
            A list containing a spectrum for each row of the specified data.

        When constructing multiple spectrums, the same extended properties, timing
        information, and scale mode are applied to all spectrums. Consider assigning
        these properties after construction.
        

#### `def __init__(self: Spectrum[np.float64], sample_count: SupportsIndex | None=..., dtype: None=..., *, data: None=..., start_index: SupportsIndex | None=..., capacity: SupportsIndex | None=..., start_frequency: SupportsFloat | None=..., frequency_increment: SupportsFloat | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., copy_extended_properties: bool=...) -> None`

#### `def __init__(self: Spectrum[_TOtherData], sample_count: SupportsIndex | None=..., dtype: type[_TOtherData] | np.dtype[_TOtherData]=..., *, data: None=..., start_index: SupportsIndex | None=..., capacity: SupportsIndex | None=..., start_frequency: SupportsFloat | None=..., frequency_increment: SupportsFloat | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., copy_extended_properties: bool=...) -> None`

#### `def __init__(self: Spectrum[_TOtherData], sample_count: SupportsIndex | None=..., dtype: None=..., *, data: npt.NDArray[_TOtherData]=..., start_index: SupportsIndex | None=..., capacity: SupportsIndex | None=..., start_frequency: SupportsFloat | None=..., frequency_increment: SupportsFloat | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., copy_extended_properties: bool=...) -> None`

#### `def __init__(self: Spectrum[Any], sample_count: SupportsIndex | None=..., dtype: npt.DTypeLike | None=..., *, data: npt.NDArray[Any] | None=..., start_index: SupportsIndex | None=..., capacity: SupportsIndex | None=..., start_frequency: SupportsFloat | None=..., frequency_increment: SupportsFloat | None=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=..., copy_extended_properties: bool=...) -> None`

#### `def __init__(self, sample_count: SupportsIndex | None=None, dtype: npt.DTypeLike | None=None, *, data: npt.NDArray[Any] | None=None, start_index: SupportsIndex | None=None, capacity: SupportsIndex | None=None, start_frequency: SupportsFloat | None=None, frequency_increment: SupportsFloat | None=None, extended_properties: Mapping[str, ExtendedPropertyValue] | None=None, copy_extended_properties: bool=True) -> None`

Initialize a new frequency spectrum.

        Args:
            sample_count: The number of samples in the spectrum.
            dtype: The NumPy data type for the spectrum data.
            data: A NumPy ndarray to use for sample storage. The spectrum takes ownership
                of this array. If not specified, an ndarray is created based on the specified dtype,
                start index, sample count, and capacity.
            start_index: The sample index at which the spectrum data begins.
            sample_count: The number of samples in the spectrum.
            capacity: The number of samples to allocate. Pre-allocating a larger buffer optimizes
                appending samples to the spectrum.
            start_frequency: The start frequency of the spectrum.
            frequency_increment: The frequency increment of the spectrum.
            extended_properties: The extended properties of the spectrum.
            copy_extended_properties: Specifies whether to copy the extended properties or take
                ownership.

        Returns:
            A frequency spectrum.
        

#### `def _init_with_new_array(self, sample_count: SupportsIndex | None=None, dtype: npt.DTypeLike | None=None, *, start_index: SupportsIndex | None=None, capacity: SupportsIndex | None=None) -> None`

#### `def _init_with_provided_array(self, data: npt.NDArray[_TData], dtype: npt.DTypeLike | None=None, *, start_index: SupportsIndex | None=None, sample_count: SupportsIndex | None=None, capacity: SupportsIndex | None=None) -> None`

#### `def data(self) -> npt.NDArray[_TData]`

The spectrum data.

#### `def get_data(self, start_index: SupportsIndex | None=0, sample_count: SupportsIndex | None=None) -> npt.NDArray[_TData]`

Get a subset of the spectrum data.

        Args:
            start_index: The sample index at which the data begins.
            sample_count: The number of samples to return.

        Returns:
            A subset of the spectrum data.
        

#### `def sample_count(self) -> int`

The number of samples in the spectrum.

#### `def start_index(self) -> int`

The sample index of the underlying array at which the spectrum data begins.

#### `def capacity(self) -> int`

The total capacity available for spectrum data.

        Setting the capacity resizes the underlying NumPy array in-place.

        * Other Python objects with references to the array will see the array size change.
        * If the array has a reference to an external buffer (such as an array.array), attempting
          to resize it raises ValueError.
        

#### `def capacity(self, value: int) -> None`

#### `def dtype(self) -> np.dtype[_TData]`

The NumPy dtype for the spectrum data.

#### `def start_frequency(self) -> float`

The start frequency of the spectrum.

#### `def start_frequency(self, value: float) -> None`

#### `def frequency_increment(self) -> float`

The frequency increment of the spectrum.

#### `def frequency_increment(self, value: float) -> None`

#### `def extended_properties(self) -> ExtendedPropertyDictionary`

The extended properties for the spectrum.

#### `def channel_name(self) -> str`

The name of the device channel from which the spectrum was acquired.

#### `def channel_name(self, value: str) -> None`

#### `def units(self) -> str`

The unit of measurement, such as volts, of the spectrum.

#### `def units(self, value: str) -> None`

#### `def append(self, other: npt.NDArray[_TData] | Spectrum[_TData] | Sequence[Spectrum[_TData]], /) -> None`

Append data to the spectrum.

        Args:
            other: The array or spectrum(s) to append.

        Raises:
            ValueError: The other array has the wrong number of dimensions.
            TypeError: The data types of the current spectrum and other array or spectrum(s) do not
                match, or an argument has the wrong data type.

        When appending spectrums:

        * Extended properties of the other spectrum(s) are merged into the current spectrum if they
          are not already set in the current spectrum.
        

#### `def _append_array(self, array: npt.NDArray[_TData]) -> None`

#### `def _append_spectrum(self, spectrum: Spectrum[_TData]) -> None`

#### `def _append_spectrums(self, spectrums: Sequence[Spectrum[_TData]]) -> None`

#### `def _increase_capacity(self, amount: int) -> None`

#### `def load_data(self, array: npt.NDArray[_TData], *, copy: bool=True, start_index: SupportsIndex | None=0, sample_count: SupportsIndex | None=None) -> None`

Load new data into an existing spectrum.

        Args:
            array: A NumPy array containing the data to load.
            copy: Specifies whether to copy the array or save a reference to it.
            start_index: The sample index at which the spectrum data begins.
            sample_count: The number of samples in the spectrum.
        

#### `def _load_array(self, array: npt.NDArray[_TData], *, copy: bool=True, start_index: SupportsIndex | None=0, sample_count: SupportsIndex | None=None) -> None`

#### `def __eq__(self, value: object, /) -> bool`

Return self==value.

#### `def __reduce__(self) -> tuple[Any, ...]`

Return object state for pickling.

#### `def _unpickle(cls, args: tuple[Any, ...], kwargs: dict[str, Any]) -> Self`

#### `def __repr__(self) -> str`

Return repr(self).

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_timing/__init__.py -->
## PYTHON MODULE: src/nitypes/waveform/_timing/__init__.py

### MODULE DOCSTRING

Waveform timing data types for NI Python APIs.

- `__all__ = ['SampleIntervalMode', 'Timing']`

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_timing/_sample_interval/__init__.py -->
## PYTHON MODULE: src/nitypes/waveform/_timing/_sample_interval/__init__.py

### MODULE DOCSTRING

Sample interval strategies for waveform timing.

- `__all__ = ['create_sample_interval_strategy', 'IrregularSampleIntervalStrategy', 'NoneSampleIntervalStrategy', 'RegularSampleIntervalStrategy', 'SampleIntervalMode', 'SampleIntervalStrategy']`

### `def create_sample_interval_strategy(sample_interval_mode: SampleIntervalMode) -> SampleIntervalStrategy[Any, Any, Any]`

Create a sample interval strategy for the specified mode.

- `_SAMPLE_INTERVAL_STRATEGY_TYPE_FOR_MODE = {SampleIntervalMode.NONE: NoneSampleIntervalStrategy, SampleIntervalMode.REGULAR: RegularSampleIntervalStrategy, SampleIntervalMode.IRREGULAR: IrregularSampleIntervalStrategy}`

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_timing/_sample_interval/_base.py -->
## PYTHON MODULE: src/nitypes/waveform/_timing/_sample_interval/_base.py

### `class SampleIntervalStrategy(ABC, Generic[TTimestamp_co, TTimeOffset_co, TSampleInterval_co])`

Implements SampleIntervalMode specific behavior.

#### `def validate_init_args(self, timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co], sample_interval_mode: SampleIntervalMode, timestamp: TTimestamp_co | None, time_offset: TTimeOffset_co | None, sample_interval: TSampleInterval_co | None, timestamps: Sequence[TTimestamp_co] | None) -> None`

Validate the BaseTiming.__init__ arguments for this mode.

#### `def get_timestamps(self, timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co], start_index: int, count: int) -> Iterable[TTimestamp_co]`

Get or generate timestamps for the specified samples.

#### `def append_timestamps(self, timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co], timestamps: Sequence[TTimestamp_co] | None) -> Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co]`

Append timestamps and return a new waveform timing if needed.

#### `def append_timing(self, timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co], other: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co]) -> Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co]`

Append timing and return a new waveform timing if needed.

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_timing/_sample_interval/_irregular.py -->
## PYTHON MODULE: src/nitypes/waveform/_timing/_sample_interval/_irregular.py

### `class _Direction(Enum)`

### `def _are_timestamps_monotonic(timestamps: Sequence[TTimestamp_co]) -> bool`

### `def _get_direction(left: TTimestamp, right: TTimestamp) -> _Direction`

### `class IrregularSampleIntervalStrategy(SampleIntervalStrategy[TTimestamp_co, TTimeOffset_co, TSampleInterval_co])`

Implements SampleIntervalMode.IRREGULAR specific behavior.

#### `def validate_init_args(self, timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co], sample_interval_mode: SampleIntervalMode, timestamp: TTimestamp_co | None, time_offset: TTimeOffset_co | None, sample_interval: TSampleInterval_co | None, timestamps: Sequence[TTimestamp_co] | None) -> None`

#### `def get_timestamps(self, timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co], start_index: int, count: int) -> Iterable[TTimestamp_co]`

#### `def append_timestamps(self, timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co], timestamps: Sequence[TTimestamp_co] | None) -> Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co]`

#### `def append_timing(self, timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co], other: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co]) -> Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co]`

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_timing/_sample_interval/_mode.py -->
## PYTHON MODULE: src/nitypes/waveform/_timing/_sample_interval/_mode.py

### `class SampleIntervalMode(Enum)`

The sample interval mode that specifies how the waveform is sampled.

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_timing/_sample_interval/_none.py -->
## PYTHON MODULE: src/nitypes/waveform/_timing/_sample_interval/_none.py

### `class NoneSampleIntervalStrategy(SampleIntervalStrategy[TTimestamp_co, TTimeOffset_co, TSampleInterval_co])`

Implements SampleIntervalMode.NONE specific behavior.

#### `def validate_init_args(self, timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co], sample_interval_mode: SampleIntervalMode, timestamp: TTimestamp_co | None, time_offset: TTimeOffset_co | None, sample_interval: TSampleInterval_co | None, timestamps: Sequence[TTimestamp_co] | None) -> None`

#### `def get_timestamps(self, timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co], start_index: int, count: int) -> Iterable[TTimestamp_co]`

#### `def append_timestamps(self, timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co], timestamps: Sequence[TTimestamp_co] | None) -> Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co]`

#### `def append_timing(self, timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co], other: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co]) -> Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co]`

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_timing/_sample_interval/_regular.py -->
## PYTHON MODULE: src/nitypes/waveform/_timing/_sample_interval/_regular.py

### `class RegularSampleIntervalStrategy(SampleIntervalStrategy[TTimestamp_co, TTimeOffset_co, TSampleInterval_co])`

Implements SampleIntervalMode.REGULAR specific behavior.

#### `def validate_init_args(self, timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co], sample_interval_mode: SampleIntervalMode, timestamp: TTimestamp_co | None, time_offset: TTimeOffset_co | None, sample_interval: TSampleInterval_co | None, timestamps: Sequence[TTimestamp_co] | None) -> None`

#### `def get_timestamps(self, timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co], start_index: int, count: int) -> Iterable[TTimestamp_co]`

#### `def _generate_regular_timestamps(self, timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co], start_index: int, count: int) -> Generator[TTimestamp_co]`

#### `def append_timestamps(self, timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co], timestamps: Sequence[TTimestamp_co] | None) -> Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co]`

#### `def append_timing(self, timing: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co], other: Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co]) -> Timing[TTimestamp_co, TTimeOffset_co, TSampleInterval_co]`

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_timing/_timing.py -->
## PYTHON MODULE: src/nitypes/waveform/_timing/_timing.py

### `class Timing(Generic[TTimestamp_co, TTimeOffset_co, TSampleInterval_co])`

Waveform timing information.

    Waveform timing objects are immutable.
    

#### `def create_with_no_interval(cls, timestamp: TTimestamp | None=None, time_offset: TTimeOffset | None=None) -> Timing[TTimestamp, TTimeOffset, TSampleInterval_co]`

Create a waveform timing object with no sample interval.

        Args:
            timestamp: A timestamp representing the start of an acquisition or a related
                occurrence.
            time_offset: The time difference between the timestamp and the time that the first
                sample was acquired.

        Returns:
            A waveform timing object.
        

#### `def create_with_regular_interval(cls, sample_interval: TSampleInterval, timestamp: TTimestamp | None=None, time_offset: TTimeOffset | None=None) -> Timing[TTimestamp, TTimeOffset, TSampleInterval]`

Create a waveform timing object with a regular sample interval.

        Args:
            sample_interval: The time difference between samples.
            timestamp: A timestamp representing the start of an acquisition or a related
                occurrence.
            time_offset: The time difference between the timestamp and the time that the first
                sample was acquired.

        Returns:
            A waveform timing object.
        

#### `def create_with_irregular_interval(cls, timestamps: Sequence[TTimestamp]) -> Timing[TTimestamp, TTimeOffset_co, TSampleInterval_co]`

Create a waveform timing object with an irregular sample interval.

        Args:
            timestamps: A sequence containing a timestamp for each sample in the waveform,
                specifying the time that the sample was acquired.

        Returns:
            A waveform timing object.
        

#### `def __init__(self, sample_interval_mode: SampleIntervalMode, timestamp: TTimestamp_co | None=None, time_offset: TTimeOffset_co | None=None, sample_interval: TSampleInterval_co | None=None, timestamps: Sequence[TTimestamp_co] | None=None, *, copy_timestamps: bool=True) -> None`

Initialize a new waveform timing object.

        Args:
            sample_interval_mode: The sample interval mode of the waveform timing.
            timestamp: The timestamp of the waveform timing. This argument is optional for
                SampleIntervalMode.NONE and SampleIntervalMode.REGULAR and unsupported for
                SampleIntervalMode.IRREGULAR.
            time_offset: The time difference between the timestamp and the first sample. This
                argument is optional for SampleIntervalMode.NONE and SampleIntervalMode.REGULAR and
                unsupported for SampleIntervalMode.IRREGULAR.
            sample_interval: The time interval between samples. This argument is required for
                SampleIntervalMode.REGULAR and unsupported otherwise.
            timestamps: A sequence containing a timestamp for each sample in the waveform,
                specifying the time that the sample was acquired. This argument is required for
                SampleIntervalMode.IRREGULAR and unsupported otherwise.
            copy_timestamps: Specifies whether to copy the timestamps or take ownership.

        Most applications should use the named constructors instead:
        * :any:`create_with_no_interval`
        * :any:`create_with_regular_interval`
        * :any:`create_with_irregular_interval`
        

#### `def has_timestamp(self) -> bool`

Indicates whether the waveform timing has a timestamp.

#### `def timestamp(self) -> TTimestamp_co`

A timestamp representing the start of an acquisition or a related occurrence.

#### `def has_start_time(self) -> bool`

Indicates whether the waveform timing has a start_time.

#### `def start_time(self) -> TTimestamp_co`

The time that the first sample in the waveform was acquired.

        This is equivalent to ``t0`` in a LabVIEW waveform.
        This value is derived from :attr:`timestamp` + :attr:`time_offset`.
        

#### `def has_time_offset(self) -> bool`

Indicates whether the waveform timing has a time offset.

#### `def time_offset(self) -> TTimeOffset_co`

The time difference between the timestamp and the first sample.

#### `def has_sample_interval(self) -> bool`

Indicates whether the waveform timing has a sample interval.

#### `def sample_interval(self) -> TSampleInterval_co`

The time interval between samples.

        This is equivalent to ``dt`` in a LabVIEW waveform.
        

#### `def sample_interval_mode(self) -> SampleIntervalMode`

The sample interval mode that specifies how the waveform is sampled.

#### `def get_timestamps(self, start_index: SupportsIndex, count: SupportsIndex) -> Iterable[TTimestamp_co]`

Retrieve the timestamps of the waveform samples.

        Args:
            start_index: The sample index of the first timestamp to retrieve.
            count: The number of timestamps to retrieve.

        Returns:
            An iterable containing the requested timestamps.
        

#### `def to_bintime(self) -> Timing[bt.DateTime, bt.TimeDelta, bt.TimeDelta]`

Convert the timing information to use :any:`nitypes.bintime`.

#### `def to_datetime(self) -> Timing[dt.datetime, dt.timedelta, dt.timedelta]`

Convert the timing information to use :class:`DateTime`.

#### `def to_hightime(self) -> Timing[ht.datetime, ht.timedelta, ht.timedelta]`

Convert the timing information to use :any:`hightime`.

#### `def _convert(self, timestamp_type: type[TOtherTimestamp], time_offset_type: type[TOtherTimeOffset], sample_interval_type: type[TOtherSampleInterval]) -> Timing[TOtherTimestamp, TOtherTimeOffset, TOtherSampleInterval]`

#### `def __eq__(self, value: object, /) -> bool`

Return self==value.

#### `def __reduce__(self) -> tuple[Any, ...]`

Return object state for pickling.

#### `def _unpickle(cls, args: tuple[Any, ...], kwargs: dict[str, Any]) -> Self`

#### `def __repr__(self) -> str`

Return repr(self).

#### `def _append_timestamps(self, timestamps: Sequence[TTimestamp_co] | None) -> Self`

#### `def _append_timing(self, other: Self) -> Self`

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_types.py -->
## PYTHON MODULE: src/nitypes/waveform/_types.py

- `DIGITAL_PORT_DTYPES = (np.uint8, np.uint16, np.uint32)`

- `DIGITAL_STATE_DTYPES = (_np_bool, np.int8, np.uint8)`

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/_warnings.py -->
## PYTHON MODULE: src/nitypes/waveform/_warnings.py

### `def sample_interval_mismatch() -> TimingMismatchWarning`

Create a TimingMismatchWarning about appending waveforms with mismatched sample intervals.

### `def scale_mode_mismatch() -> ScalingMismatchWarning`

Create a ScalingMismatchwarning about appending waveforms with mismatched scale modes.

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/errors.py -->
## PYTHON MODULE: src/nitypes/waveform/errors.py

### MODULE DOCSTRING

Custom error classes for waveforms.

### `class TimingMismatchError(RuntimeError)`

Exception used when appending waveforms with mismatched timing.

### `class CapacityMismatchError(ValueError)`

An error for an invalid capacity.

### `class CapacityTooSmallError(ValueError)`

An error for an invalid capacity argument.

### `class DatatypeMismatchError(TypeError)`

An error for a data type mismatch.

### `class IrregularTimestampCountMismatchError(ValueError)`

An error for an irregular timestamp count mismatch.

### `class StartIndexTooLargeError(ValueError)`

An error for an invalid start index argument.

### `class StartIndexOrSampleCountTooLargeError(ValueError)`

An error for an invalid start index or sample count argument.

### `class NoTimestampInformationError(RuntimeError)`

An error for waveform timing with no timestamp information.

### `class SampleIntervalModeMismatchError(TimingMismatchError)`

An error for mixing none/regular with irregular timing.

### `class SignalCountMismatchError(ValueError)`

An error for a mismatched signal count.

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/typing.py -->
## PYTHON MODULE: src/nitypes/waveform/typing.py

### MODULE DOCSTRING

Type aliases and type variables for waveforms.

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/waveform/warnings.py -->
## PYTHON MODULE: src/nitypes/waveform/warnings.py

### MODULE DOCSTRING

Custom warning classes for waveforms.

### `class ScalingMismatchWarning(RuntimeWarning)`

Warning used when appending waveforms with mismatched scaling information.

### `class TimingMismatchWarning(RuntimeWarning)`

Warning used when appending waveforms with mismatched timing information.

<!--NI_PYTHON_API repo=nitypes-python path=src/nitypes/xy_data.py -->
## PYTHON MODULE: src/nitypes/xy_data.py

### MODULE DOCSTRING

XYData type for NI Python APIs.

XYData Data Type
=================
:class:`XYData`: An XYData object represents two axes (sequences) of numeric values with units
information. Valid types for the numeric values are :any:`int` and :any:`float`.


- `_UNIT_DESCRIPTION_X = 'NI_UnitDescription_X'`

- `_UNIT_DESCRIPTION_Y = 'NI_UnitDescription_Y'`

- `_DATA_DTYPES = (np.single, np.double, np.byte, np.short, np.intc, np.int_, _np_long, np.longlong, np.ubyte, np.ushort, np.uintc, np.uint, _np_ulong, np.ulonglong)`

### `class XYData(Generic[TData])`

Two axes (sequences) of numeric values with units information.

    Constructing
    ^^^^^^^^^^^^

    To construct an XYData object, use the :class:`XYData` class:

    >>> XYData(np.array([1.1], np.float64), np.array([4.1], np.float64))
    nitypes.xy_data.XYData(x_data=array([1.1]), y_data=array([4.1]))
    >>> XYData(np.array([1, 2]), np.array([4, 5]), x_units="A", y_units="V")
    nitypes.xy_data.XYData(x_data=array([1, 2]), y_data=array([4, 5]), x_units='A', y_units='V')

    To construct an XYData object using built-in lists, use from_arrays_1d():

    >>> XYData.from_arrays_1d([1, 2], [5, 6], np.int32)
    nitypes.xy_data.XYData(x_data=array([1, 2], dtype=int32), y_data=array([5, 6], dtype=int32))
    >>> XYData.from_arrays_1d([1.0, 1.1], [1.2, 1.3], np.float64)
    nitypes.xy_data.XYData(x_data=array([1. , 1.1]), y_data=array([1.2, 1.3]))
    

#### `def from_arrays_1d(cls, x_array: npt.NDArray[TOtherData], y_array: npt.NDArray[TOtherData], dtype: None=..., *, x_units: str=..., y_units: str=..., copy: bool=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=...) -> XYData[TOtherData]`

#### `def from_arrays_1d(cls, x_array: npt.NDArray[Any] | Sequence[Any], y_array: npt.NDArray[Any] | Sequence[Any], dtype: type[TOtherData] | np.dtype[TOtherData], *, x_units: str=..., y_units: str=..., copy: bool=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=...) -> XYData[TOtherData]`

#### `def from_arrays_1d(cls, x_array: npt.NDArray[Any] | Sequence[Any], y_array: npt.NDArray[Any] | Sequence[Any], dtype: npt.DTypeLike | None=..., *, x_units: str=..., y_units: str=..., copy: bool=..., extended_properties: Mapping[str, ExtendedPropertyValue] | None=...) -> XYData[Any]`

#### `def from_arrays_1d(cls, x_array: npt.NDArray[Any] | Sequence[Any], y_array: npt.NDArray[Any] | Sequence[Any], dtype: npt.DTypeLike | None=None, *, x_units: str='', y_units: str='', copy: bool=True, extended_properties: Mapping[str, ExtendedPropertyValue] | None=None) -> XYData[Any]`

Construct an XYData from two one-dimensional arrays or sequences.

        Args:
            x_array: The x-axis data as a one-dimensional array or a sequence.
            y_array: The y-axis data as a one-dimensional array or a sequence.
            dtype: The NumPy data type for the XYdata axes. This argument is required
                when x_array and y_array are sequences.
            x_units: The units string associated with x_array.
            y_units: The units string associated with y_array
            copy: Specifies whether to copy the arrays or save references to them.
            extended_properties: The extended properties of the XYData.

        Returns:
            An XYData object containing the specified data.
        

#### `def __init__(self: XYData[TOtherData], x_data: npt.NDArray[TOtherData], y_data: npt.NDArray[TOtherData], *, x_units: str='', y_units: str='', extended_properties: Mapping[str, ExtendedPropertyValue] | None=None, copy_extended_properties: bool=True) -> None`

Initialize a new XYData.

        Args:
            x_data: A NumPy ndarray to use for x-axis data storage. The XYData takes ownership
                of this array. If not specified, an ndarray is created based on the specified
                dtype and capacity.
            y_data: A NumPy ndarray to use for y-axis data storage. The XYData takes ownership
                of this array. If not specified, an ndarray is created based on the specified
                dtype and capacity.
            x_units: The units string associated with x_data.
            y_units: The units string associated with y_data.
            extended_properties: The extended properties of the XYData.
            copy_extended_properties: Specifies whether to copy the extended properties or take
                ownership.

        Returns:
            An XYData object.
        

#### `def _init_with_provided_arrays(self, x_data: npt.NDArray[TData], y_data: npt.NDArray[TData], dtype: npt.DTypeLike | None=None) -> None`

#### `def x_data(self) -> npt.NDArray[TData]`

The x-axis data of this XYData.

#### `def y_data(self) -> npt.NDArray[TData]`

The y-axis data of this XYData.

#### `def x_units(self) -> str`

The unit of measurement, such as volts, of x_data.

#### `def x_units(self, value: str) -> None`

#### `def y_units(self) -> str`

The unit of measurement, such as volts, of y_data.

#### `def y_units(self, value: str) -> None`

#### `def dtype(self) -> np.dtype[TData]`

The NumPy dtype for the XYData.

#### `def extended_properties(self) -> ExtendedPropertyDictionary`

The extended properties for the XYData.

        .. note::
            Data stored in the extended properties dictionary may not be encrypted when you send it
            over the network or write it to a TDMS file.
        

#### `def __eq__(self, value: object, /) -> bool`

Return self==value.

#### `def __reduce__(self) -> tuple[Any, ...]`

Return object state for pickling.

#### `def _unpickle(cls, args: tuple[Any, ...], kwargs: dict[str, Any]) -> Self`

#### `def __repr__(self) -> str`

Return repr(self).

#### `def __str__(self) -> str`

Return str(self).

#### `def _format_values_with_units(values: npt.NDArray[TData], units: str) -> str`

<!--NI_PYTHON_API repo=nitypes-python path=tests/__init__.py -->
## PYTHON MODULE: tests/__init__.py

### MODULE DOCSTRING

Tests for the nitypes package.

<!--NI_PYTHON_API repo=nitypes-python path=tests/acceptance/__init__.py -->
## PYTHON MODULE: tests/acceptance/__init__.py

### MODULE DOCSTRING

Acceptance tests for the nitypes package.

<!--NI_PYTHON_API repo=nitypes-python path=tests/acceptance/waveform/__init__.py -->
## PYTHON MODULE: tests/acceptance/waveform/__init__.py

### MODULE DOCSTRING

Acceptance tests for the nitypes.waveform package.

<!--NI_PYTHON_API repo=nitypes-python path=tests/acceptance/waveform/test_memmap.py -->
## PYTHON MODULE: tests/acceptance/waveform/test_memmap.py

### `def test___memmap_array_1d___create_waveform_from_array___waveform_contains_memmap_data(tmp_path: Path, copy: bool) -> None`

### `def test___memmap_array_2d___create_waveforms_from_array___waveforms_contains_memmap_data(tmp_path: Path, copy: bool) -> None`

### `def test___memmap_waveform___append___waveform_writes_to_memmap(tmp_path: Path) -> None`

### `def test___memmap_waveforms___append___waveforms_write_to_memmap(tmp_path: Path) -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/benchmark/__init__.py -->
## PYTHON MODULE: tests/benchmark/__init__.py

### MODULE DOCSTRING

Benchmarks for the nitypes package.

<!--NI_PYTHON_API repo=nitypes-python path=tests/benchmark/bintime/__init__.py -->
## PYTHON MODULE: tests/benchmark/bintime/__init__.py

### MODULE DOCSTRING

Benchmarks for the nitypes.bintime package.

<!--NI_PYTHON_API repo=nitypes-python path=tests/benchmark/bintime/test_datetime.py -->
## PYTHON MODULE: tests/benchmark/bintime/test_datetime.py

### `def test___bt_datetime___construct(benchmark: BenchmarkFixture) -> None`

### `def test___dt_datetime___construct(benchmark: BenchmarkFixture) -> None`

### `def test___ht_datetime___construct(benchmark: BenchmarkFixture) -> None`

### `def test___bt_datetime___from_ticks(benchmark: BenchmarkFixture) -> None`

### `def test___bt_datetime___from_tuple(benchmark: BenchmarkFixture) -> None`

### `def test___bt_datetime___now(benchmark: BenchmarkFixture) -> None`

### `def test___dt_datetime___now(benchmark: BenchmarkFixture) -> None`

### `def test___ht_datetime___now(benchmark: BenchmarkFixture) -> None`

### `def test___bt_datetime___lt(benchmark: BenchmarkFixture) -> None`

### `def test___dt_datetime___lt(benchmark: BenchmarkFixture) -> None`

### `def test___ht_datetime___lt(benchmark: BenchmarkFixture) -> None`

### `def test___bt_datetime___add(benchmark: BenchmarkFixture) -> None`

### `def test___dt_datetime___add(benchmark: BenchmarkFixture) -> None`

### `def test___ht_datetime___add(benchmark: BenchmarkFixture) -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/benchmark/bintime/test_datetime_array.py -->
## PYTHON MODULE: tests/benchmark/bintime/test_datetime_array.py

- `LIST_1 = [bt.DateTime.from_offset(bt.TimeDelta(0.3))]`

- `LIST_10 = [bt.DateTime.from_offset(bt.TimeDelta(float(offset))) for offset in np.arange(0, 10, 0.3)]`

- `LIST_100 = [bt.DateTime.from_offset(bt.TimeDelta(float(offset))) for offset in np.arange(0, 100, 0.3)]`

- `LIST_1000 = [bt.DateTime.from_offset(bt.TimeDelta(float(offset))) for offset in np.arange(0, 1000, 0.3)]`

- `LIST_10000 = [bt.DateTime.from_offset(bt.TimeDelta(float(offset))) for offset in np.arange(0, 10000, 0.3)]`

- `FAST_CASES = (LIST_1,)`

- `BIG_O_CASES = (LIST_1, LIST_10, LIST_100, LIST_1000, LIST_10000)`

### `def test___bt_datetime_array___construct(benchmark: BenchmarkFixture, constructor_list: list[bt.DateTime]) -> None`

### `def test___bt_datetime_array___extend(benchmark: BenchmarkFixture, extend_list: list[bt.DateTime]) -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/benchmark/bintime/test_timedelta.py -->
## PYTHON MODULE: tests/benchmark/bintime/test_timedelta.py

### `def test___bt_timedelta___construct(benchmark: BenchmarkFixture) -> None`

### `def test___dt_timedelta___construct(benchmark: BenchmarkFixture) -> None`

### `def test___ht_timedelta___construct(benchmark: BenchmarkFixture) -> None`

### `def test___bt_timedelta___from_ticks(benchmark: BenchmarkFixture) -> None`

### `def test___bt_timedelta___from_tuple(benchmark: BenchmarkFixture) -> None`

### `def test___bt_timedelta___eq(benchmark: BenchmarkFixture) -> None`

### `def test___dt_timedelta___eq(benchmark: BenchmarkFixture) -> None`

### `def test___ht_timedelta___eq(benchmark: BenchmarkFixture) -> None`

### `def test___bt_timedelta___lt(benchmark: BenchmarkFixture) -> None`

### `def test___dt_timedelta___lt(benchmark: BenchmarkFixture) -> None`

### `def test___ht_timedelta___lt(benchmark: BenchmarkFixture) -> None`

### `def test___bt_timedelta___add(benchmark: BenchmarkFixture) -> None`

### `def test___dt_timedelta___add(benchmark: BenchmarkFixture) -> None`

### `def test___ht_timedelta___add(benchmark: BenchmarkFixture) -> None`

### `def test___bt_timedelta___mul(benchmark: BenchmarkFixture) -> None`

### `def test___dt_timedelta___mul(benchmark: BenchmarkFixture) -> None`

### `def test___ht_timedelta___mul(benchmark: BenchmarkFixture) -> None`

### `def test___bt_timedelta___total_seconds(benchmark: BenchmarkFixture) -> None`

### `def test___dt_timedelta___total_seconds(benchmark: BenchmarkFixture) -> None`

### `def test___ht_timedelta___total_seconds(benchmark: BenchmarkFixture) -> None`

### `def test___bt_timedelta___precision_total_seconds(benchmark: BenchmarkFixture) -> None`

### `def test___ht_timedelta___precision_total_seconds(benchmark: BenchmarkFixture) -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/benchmark/bintime/test_timedelta_array.py -->
## PYTHON MODULE: tests/benchmark/bintime/test_timedelta_array.py

- `LIST_1 = [bt.TimeDelta(0.3)]`

- `LIST_10 = [bt.TimeDelta(float(value)) for value in np.arange(-10, 10, 0.3)]`

- `LIST_100 = [bt.TimeDelta(float(value)) for value in np.arange(-100, 100, 0.3)]`

- `LIST_1000 = [bt.TimeDelta(float(value)) for value in np.arange(-1000, 1000, 0.3)]`

- `LIST_10000 = [bt.TimeDelta(float(value)) for value in np.arange(-10000, 10000, 0.3)]`

- `FAST_CASES = (LIST_1,)`

- `BIG_O_CASES = (LIST_1, LIST_10, LIST_100, LIST_1000, LIST_10000)`

### `def test___bt_timedelta_array___construct(benchmark: BenchmarkFixture, constructor_list: list[bt.TimeDelta]) -> None`

### `def test___bt_timedelta_array___extend(benchmark: BenchmarkFixture, extend_list: list[bt.TimeDelta]) -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/__init__.py -->
## PYTHON MODULE: tests/unit/__init__.py

### MODULE DOCSTRING

Unit tests for the nitypes package.

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/bintime/__init__.py -->
## PYTHON MODULE: tests/unit/bintime/__init__.py

### MODULE DOCSTRING

Unit tests for the nitypes.bintime package.

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/bintime/test_datetime.py -->
## PYTHON MODULE: tests/unit/bintime/test_datetime.py

### `def test___no_args___construct___returns_epoch() -> None`

### `def test___dt_datetime___construct___returns_datetime() -> None`

### `def test___ht_datetime___construct___returns_nearest_datetime() -> None`

### `def test___unit_args___construct___returns_nearest_datetime() -> None`

### `def test___naive_dt_datetime___construct___raises_value_error() -> None`

### `def test___naive_ht_datetime___construct___raises_value_error() -> None`

### `def test___naive_unit_args___construct___raises_value_error() -> None`

### `def test___local_dt_datetime___construct___raises_value_error() -> None`

### `def test___local_ht_datetime___construct___raises_value_error() -> None`

### `def test___local_unit_args___construct___raises_value_error() -> None`

### `def test___int_ticks___from_ticks___returns_time_value() -> None`

### `def test___time_value___from_offset___returns_time_value() -> None`

### `def test___various_values___unit_properties___return_unit_values(other: ht.datetime, expected: tuple[int, ...]) -> None`

### `def test___time_value___add___returns_datetime(left: DateTime, right: TimeDelta, expected: DateTime) -> None`

### `def test___dt_timedelta___add___returns_datetime(left: DateTime, right: dt.timedelta, expected: DateTime) -> None`

### `def test___ht_timedelta___add___returns_datetime(left: DateTime, right: ht.timedelta, expected: DateTime) -> None`

### `def test___time_value___sub___returns_datetime(left: DateTime, right: TimeDelta, expected: DateTime) -> None`

### `def test___datetime___sub___returns_time_value(left: DateTime, right: DateTime, expected: TimeDelta) -> None`

### `def test___same_value___comparison___equal(left: DateTime | dt.datetime | ht.datetime, right: DateTime | dt.datetime | ht.datetime) -> None`

### `def test___lesser_value___comparison___lesser(left: TimeDelta | dt.timedelta | ht.timedelta, right: TimeDelta | dt.timedelta | ht.timedelta) -> None`

- `_VARIOUS_VALUES = [DateTime(dt.MINYEAR, 1, 1, 0, 0, 0, 0, 0, 0, dt.timezone.utc), DateTime(1850, 12, 25, 8, 15, 30, 123456, 234567789, 345567890, dt.timezone.utc), DateTime(1903, 12, 31, 23, 59, 59, 123456, 234567789, 345567890, dt.timezone.utc), DateTime(1904, 1, 1, 0, 30, 0, 0, 0, 1000000, dt.timezone.utc), DateTime(2000, 1, 1, 0, 0, 0, 0, 0, 0, dt.timezone.utc), DateTime(dt.MAXYEAR, 12, 31, 23, 59, 59, 999999, 999999999, 999000000, dt.timezone.utc)]`

### `def test___various_values___hash___returns_probably_unique_int() -> None`

### `def test___various_values___copy___makes_copy(value: DateTime) -> None`

### `def test___various_values___pickle_unpickle___makes_copy(value: DateTime) -> None`

### `def test___time_value___pickle___references_public_modules() -> None`

### `def test___pickled_value___unpickle___is_compatible(pickled_value: bytes, expected: DateTime) -> None`

### `def test___various_values___str___looks_ok(value: TimeDelta, expected: str) -> None`

### `def test___various_values___repr___looks_ok(value: TimeDelta, expected: str) -> None`

### `def test___various_values___get_ticks___returns_correct_value(seconds: float) -> None`

### `def test___various_values___to_tuple___returns_correct_values(seconds: float) -> None`

### `def test___various_values___from_tuple___datetime_correct(seconds: float) -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/bintime/test_datetime_array.py -->
## PYTHON MODULE: tests/unit/bintime/test_datetime_array.py

### `def test___no_args___construct___returns_empty_array() -> None`

### `def test___sequence_arg___construct___returns_matching_array(constructor_arg: Sequence[DateTime]) -> None`

### `def test___mixed_arg___construct___raises(constructor_arg: list[Any]) -> None`

### `def test___datetime_array___get_len___returns_length(datetime_list: list[DateTime] | None, expected_length: int) -> None`

### `def test___datetime_array___index___returns_datetime(datetime_list: list[DateTime], indexer: int, raised_exception: BaseException | None) -> None`

### `def test___datetime_array___slice___returns_slice() -> None`

### `def test___datetime_array___invalid_index___raises(indexer: Any) -> None`

### `def test___datetime_array___set_by_index___updates_array(datetime_list: list[DateTime] | None, indexer: int, raised_exception: BaseException | None) -> None`

### `def test___datetime_array___set_by_slice___updates_array(indexer: slice, new_entries: Sequence[DateTime], expected_result: DateTimeArray) -> None`

### `def test___datetime_array___set_slice_wrong_value___raises(indexer: slice, new_entries: Sequence[DateTime] | DateTime, raised_exception: BaseException) -> None`

### `def test___datetime_array___set_invalid_index___raises(indexer: Any) -> None`

### `def test___datetime_array___set_invalid_value___raises(new_entry: Any) -> None`

### `def test___datetime_array___set_mixed_slice___raises(new_entries: list[Any]) -> None`

### `def test___datetime_array___delete_by_index___removes_item(datetime_list: list[DateTime] | None, indexer: int, raised_exception: BaseException | None) -> None`

### `def test___datetime_array___delete_by_slice___removes_items(indexer: slice, expected_result: DateTimeArray) -> None`

### `def test___datetime_array___delete_invalid_index___raises(indexer: Any) -> None`

### `def test___datetime_array___insert_value___inserts(initial_value: list[DateTime] | None, index: int) -> None`

### `def test___datetime_array___insert_invalid_index___raises(index: int) -> None`

### `def test___datetime_array___insert_invalid_value___raises(value: Any) -> None`

### `def test___datetime_array___count___returns_matching_count(array: DateTimeArray, item: DateTime, expected_count: int) -> None`

### `def test___datetime_array___index___returns_matching_index(array: DateTimeArray, item: DateTime, expected_index: int) -> None`

### `def test___datetime_array_no_item___index___raises() -> None`

### `def test___datetime_array___append___adds_to_end() -> None`

### `def test___datetime_array___append_invalid_value___raises(new_entry: Any) -> None`

### `def test___datetime_array___extend___adds_to_end(new_entries: Sequence[DateTime]) -> None`

### `def test___datetime_array___plus_equals___adds_to_end(new_entries: Sequence[DateTime]) -> None`

### `def test___datetime_array___extend_invalid_values___raises(new_entries: Any) -> None`

### `def test___datetime_array___plus_equals_invalid_values___raises(new_entries: Any) -> None`

### `def test___datetime_array___remove___removes_first_match() -> None`

### `def test___datetime_array_no_item___remove___raises(item_to_remove: Any) -> None`

### `def test___datetime_array___pop___removes_from_location() -> None`

### `def test___empty_datetime_array___pop___raises() -> None`

### `def test___datetime_array___pop_out_of_bounds___raises() -> None`

### `def test___datetime_array___reverse___reverses() -> None`

### `def test___datetime_array___clear___empties_array() -> None`

### `def test___datetime_array___iterate___visits_entries() -> None`

### `def test___datetime_array___contains___returns_presence() -> None`

### `def test___same_value___equality___equal(left: DateTimeArray, right: DateTimeArray) -> None`

### `def test___different_value___equality___not_equal(left: DateTimeArray, right: DateTimeArray) -> None`

### `def test___datetime_array___min___returns_minimum() -> None`

### `def test___datetime_array___max___returns_maximum() -> None`

### `def test___datetime_array___copy___returns_copy() -> None`

### `def test___datetime_array___deepcopy___returns_deepcopy() -> None`

### `def test___datetime_array___str___looks_ok(value: DateTimeArray, expected_str: str) -> None`

### `def test___datetime_array___repr___looks_ok(value: DateTimeArray, expected_repr: str) -> None`

### `def test___datetime_array___pickle___references_public_modules() -> None`

### `def test___pickled_value___unpickle___is_compatible(pickled_value: bytes, expected: DateTimeArray) -> None`

### `def test___datetime_array___pickle_unpickle___makes_copy(value: DateTimeArray) -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/bintime/test_timedelta.py -->
## PYTHON MODULE: tests/unit/bintime/test_timedelta.py

- `_BT_EPSILON = ht.timedelta(yoctoseconds=54210)`

- `_DT_EPSILON = ht.timedelta(microseconds=1)`

### `def test___no_args___construct___returns_zero_timedelta() -> None`

### `def test___int_seconds___construct___returns_timedelta() -> None`

### `def test___float_seconds___construct___returns_timedelta() -> None`

### `def test___decimal_seconds___construct___returns_timedelta() -> None`

### `def test___dt_timedelta___construct___returns_nearest_timedelta() -> None`

### `def test___ht_timedelta___construct___returns_nearest_timedelta() -> None`

### `def test___out_of_range___construct___raises_overflow_error(seconds: int | float | Decimal) -> None`

### `def test___invalid_seconds_type___construct___raises_type_error() -> None`

### `def test___int_ticks___from_ticks___returns_timedelta() -> None`

### `def test___out_of_range___from_ticks___raises_overflow_error(ticks: int) -> None`

### `def test___unsupported_type___from_ticks___raises_type_error() -> None`

### `def test___various_values___unit_properties___return_unit_values(value: TimeDelta, expected: tuple[int, ...]) -> None`

### `def test___float_seconds___total_seconds___approximate_match(seconds: float) -> None`

### `def test___whole_decimal_seconds___precision_total_seconds___exact_match(seconds: Decimal) -> None`

### `def test___fractional_decimal_seconds___precision_total_seconds___approximate_match(seconds: Decimal) -> None`

### `def test___round_trip___precision_total_seconds___exact_match(ticks: int) -> None`

### `def test___random_round_trip___precision_total_seconds___exact_match(_random_state: tuple[Any, ...]) -> None`

### `def _random_state() -> Generator[tuple[Any, ...]]`

### `def test___timedeltas___neg___returns_negation(value: TimeDelta, expected: TimeDelta) -> None`

### `def test___timedeltas___pos___returns_identity(value: TimeDelta, expected: TimeDelta) -> None`

### `def test___timedeltas___abs___returns_absolute_value(value: TimeDelta, expected: TimeDelta) -> None`

### `def test___timedeltas___add___returns_sum(left: TimeDelta, right: TimeDelta, expected: TimeDelta) -> None`

### `def test___dt_timedelta___add___returns_sum(left: TimeDelta, right: dt.timedelta, expected: TimeDelta) -> None`

### `def test___dt_timedelta_inexact_result___add___returns_approximate_sum(left: TimeDelta, right: dt.timedelta, expected: TimeDelta) -> None`

### `def test___ht_timedelta___add___returns_sum(left: TimeDelta, right: ht.timedelta, expected: TimeDelta) -> None`

### `def test___ht_timedelta_inexact_result___add___returns_approximate_sum(left: TimeDelta, right: ht.timedelta, expected: TimeDelta) -> None`

### `def test___dt_datetime___add___returns_sum(left: dt.datetime, right: TimeDelta, expected: dt.datetime) -> None`

### `def test___dt_datetime_inexact_result___add___returns_approximate_sum(left: dt.datetime, right: TimeDelta, expected: dt.datetime) -> None`

### `def test___ht_datetime___add___returns_sum(left: ht.datetime, right: TimeDelta, expected: ht.datetime) -> None`

### `def test___ht_datetime_inexact_result___add___returns_approximate_sum(left: ht.datetime, right: TimeDelta, expected: ht.datetime) -> None`

### `def test___timedeltas___sub___returns_difference(left: TimeDelta, right: TimeDelta, expected: TimeDelta) -> None`

### `def test___dt_timedelta___sub___returns_difference(left: TimeDelta, right: dt.timedelta, expected: TimeDelta) -> None`

### `def test___dt_timedelta_inexact_result___sub___returns_approximate_difference(left: TimeDelta, right: dt.timedelta, expected: TimeDelta) -> None`

### `def test___ht_timedelta___sub___returns_difference(left: TimeDelta, right: ht.timedelta, expected: TimeDelta) -> None`

### `def test___ht_timedelta_inexact_result___sub___returns_approximate_difference(left: TimeDelta, right: ht.timedelta, expected: TimeDelta) -> None`

### `def test___dt_datetime___sub___returns_sum(left: dt.datetime, right: TimeDelta, expected: dt.datetime) -> None`

### `def test___dt_datetime_inexact_result___sub___returns_approximate_sum(left: dt.datetime, right: TimeDelta, expected: dt.datetime) -> None`

### `def test___ht_datetime___sub___returns_sum(left: ht.datetime, right: TimeDelta, expected: ht.datetime) -> None`

### `def test___ht_datetime_inexact_result___sub___returns_approximate_sum(left: ht.datetime, right: TimeDelta, expected: ht.datetime) -> None`

### `def test___int___mul___returns_exact_product(left: TimeDelta, right: int, expected: TimeDelta) -> None`

### `def test___exact_float___mul___returns_exact_product(left: TimeDelta, right: float, expected: TimeDelta) -> None`

### `def test___inexact_float___mul___returns_approximate_product(left: TimeDelta, right: float, expected: TimeDelta) -> None`

### `def test___decimal___mul___returns_exact_product(left: TimeDelta, right: float, expected: TimeDelta) -> None`

### `def test___timedelta___floordiv___returns_int(left: TimeDelta, right: TimeDelta, expected: int) -> None`

### `def test___int___floordiv___returns_timedelta(left: TimeDelta, right: int, expected: TimeDelta) -> None`

### `def test___timedelta___truediv___returns_float(left: TimeDelta, right: TimeDelta, expected: int) -> None`

### `def test___float___truediv___returns_approximate_timedelta(left: TimeDelta, right: float, expected: TimeDelta) -> None`

### `def test___timedelta___mod___returns_timedelta(left: TimeDelta, right: TimeDelta, expected: TimeDelta) -> None`

### `def test___dt_timedelta___mod___returns_timedelta(left: TimeDelta, right: dt.timedelta, expected: TimeDelta) -> None`

### `def test___ht_timedelta___mod___returns_timedelta(left: TimeDelta, right: ht.timedelta, expected: TimeDelta) -> None`

### `def test___timedelta___divmod___returns_int_and_timedelta(left: TimeDelta, right: TimeDelta, expected: tuple[int, TimeDelta]) -> None`

### `def test___dt_timedelta___divmod___returns_int_and_timedelta(left: TimeDelta, right: dt.timedelta, expected: tuple[int, TimeDelta]) -> None`

### `def test___ht_timedelta___divmod___returns_int_and_timedelta(left: TimeDelta, right: ht.timedelta, expected: tuple[int, TimeDelta]) -> None`

### `def test___same_value___comparison___equal(left: TimeDelta | dt.timedelta | ht.timedelta, right: TimeDelta | dt.timedelta | ht.timedelta) -> None`

### `def test___lesser_value___comparison___lesser(left: TimeDelta | dt.timedelta | ht.timedelta, right: TimeDelta | dt.timedelta | ht.timedelta) -> None`

### `def test___timedelta___bool___returns_not_zero(value: TimeDelta, expected: bool) -> None`

- `_VARIOUS_VALUES = [TimeDelta(0), TimeDelta(2), TimeDelta(-2), TimeDelta.from_ticks((1 << 124) + (2 << 64) + 3), TimeDelta.from_ticks((-1 << 124) + (-2 << 64) + -3), TimeDelta.min, TimeDelta.max]`

### `def test___various_values___hash___returns_probably_unique_int() -> None`

### `def test___various_values___copy___makes_copy(value: TimeDelta) -> None`

### `def test___various_values___pickle_unpickle___makes_copy(value: TimeDelta) -> None`

### `def test___timedelta___pickle___references_public_modules() -> None`

### `def test___pickled_value___unpickle___is_compatible(pickled_value: bytes, expected: TimeDelta) -> None`

### `def test___various_values___str___looks_ok(value: TimeDelta, expected: str) -> None`

### `def test___various_values___repr___looks_ok(value: TimeDelta, expected: str) -> None`

### `def test___various_values___get_ticks___returns_correct_value(seconds: float) -> None`

### `def test___various_values___to_tuple___returns_correct_values(seconds: float) -> None`

### `def test___various_values___from_tuple___timedelta_correct(seconds: float) -> None`

### `def test___whole_seconds_too_large___from_tuple___throws_error() -> None`

### `def test___fractional_seconds_too_large___from_tuple___throws_error() -> None`

### `def test___fractional_seconds_negative___from_tuple___throws_error() -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/bintime/test_timedelta_array.py -->
## PYTHON MODULE: tests/unit/bintime/test_timedelta_array.py

### `def test___no_args___construct___returns_empty_array() -> None`

### `def test___sequence_arg___construct___returns_matching_array(constructor_arg: Sequence[TimeDelta]) -> None`

### `def test___mixed_arg___construct___raises(constructor_arg: list[Any]) -> None`

### `def test___timedelta_array___get_len___returns_length(timedelta_list: list[TimeDelta], expected_length: int) -> None`

### `def test___timedelta_array___index___returns_timedelta(timedelta_list: list[TimeDelta], indexer: int, raised_exception: BaseException | None) -> None`

### `def test___timedelta_array___slice___returns_slice() -> None`

### `def test___timedelta_array___invalid_index___raises(indexer: Any) -> None`

### `def test___timedelta_array___set_by_index___updates_array(timedelta_list: list[TimeDelta] | None, indexer: int, raised_exception: BaseException | None) -> None`

### `def test___timedelta_array___set_by_slice___updates_array(indexer: slice, new_entries: Sequence[TimeDelta], expected_result: TimeDeltaArray) -> None`

### `def test___timedelta_array___set_slice_wrong_value___raises(indexer: slice, new_entries: Sequence[TimeDelta] | TimeDelta, raised_exception: BaseException) -> None`

### `def test___timedelta_array___set_invalid_index___raises(indexer: Any) -> None`

### `def test___timedelta_array___set_invalid_value___raises(new_entry: Any) -> None`

### `def test___timedelta_array___set_mixed_slice___raises(new_entries: list[Any]) -> None`

### `def test___timedelta_array___delete_by_index___removes_item(timedelta_list: list[TimeDelta] | None, indexer: int, raised_exception: BaseException | None) -> None`

### `def test___timedelta_array___delete_by_slice___removes_items(indexer: slice, expected_result: TimeDeltaArray) -> None`

### `def test___timedelta_array___delete_invalid_index___raises(indexer: Any) -> None`

### `def test___timedelta_array___insert_value___inserts(initial_value: list[TimeDelta], index: int) -> None`

### `def test___timedelta_array___insert_invalid_index___raises(index: int) -> None`

### `def test___timedelta_array___insert_invalid_value___raises(value: Any) -> None`

### `def test___timedelta_array___count___returns_matching_count(array: TimeDeltaArray, item: TimeDelta, expected_count: int) -> None`

### `def test___timedelta_array___index___returns_matching_index(array: TimeDeltaArray, item: TimeDelta, expected_index: int) -> None`

### `def test___timedelta_array_no_item___index___raises() -> None`

### `def test___timedelta_array___append___adds_to_end() -> None`

### `def test___timedelta_array___append_invalid_value___raises(new_entry: Any) -> None`

### `def test___timedelta_array___extend___adds_to_end(new_entries: Sequence[TimeDelta]) -> None`

### `def test___timedelta_array___plus_equals___adds_to_end(new_entries: Sequence[TimeDelta]) -> None`

### `def test___timedelta_array___extend_invalid_values___raises(new_entries: Any) -> None`

### `def test___timedelta_array___plus_equals_invalid_values___raises(new_entries: Any) -> None`

### `def test___timedelta_array___remove___removes_first_match() -> None`

### `def test___timedelta_array_no_item___remove___raises(item_to_remove: Any) -> None`

### `def test___timedelta_array___pop___removes_from_location() -> None`

### `def test___empty_timedelta_array___pop___raises() -> None`

### `def test___timedelta_array___pop_out_of_bounds___raises() -> None`

### `def test___timedelta_array___reverse___reverses() -> None`

### `def test___timedelta_array___clear___empties_array() -> None`

### `def test___timedelta_array___iterate___visits_entries() -> None`

### `def test___timedelta_array___contains___returns_presence() -> None`

### `def test___same_value___equality___equal(left: TimeDeltaArray, right: TimeDeltaArray) -> None`

### `def test___different_value___equality___not_equal(left: TimeDeltaArray, right: TimeDeltaArray) -> None`

### `def test___timedelta_array___min___returns_minimum() -> None`

### `def test___timedelta_array___max___returns_maximum() -> None`

### `def test___timedelta_array___copy___returns_copy() -> None`

### `def test___timedelta_array___deepcopy___returns_deepcopy() -> None`

### `def test___timedelta_array___str___looks_ok(value: TimeDeltaArray, expected_str: str) -> None`

### `def test___timedelta_array___repr___looks_ok(value: TimeDeltaArray, expected_repr: str) -> None`

### `def test___timedelta_array___pickle___references_public_modules() -> None`

### `def test___pickled_value___unpickle___is_compatible(pickled_value: bytes, expected: TimeDeltaArray) -> None`

### `def test___timedelta_array___pickle_unpickle___makes_copy(value: TimeDeltaArray) -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/complex/__init__.py -->
## PYTHON MODULE: tests/unit/complex/__init__.py

### MODULE DOCSTRING

Unit tests for the nitypes.complex package.

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/complex/test_conversion.py -->
## PYTHON MODULE: tests/unit/complex/test_conversion.py

### `def test___complexint32_array_to_complex64_array___convert_complex___converts_array() -> None`

### `def test___complexint32_array_to_complex128_array___convert_complex___converts_array() -> None`

### `def test___complexint32_array_to_complexint32_array___convert_complex___returns_original_array() -> None`

### `def test___complex64_array_to_complexint32_array___convert_complex___converts_array() -> None`

### `def test___complex64_array_to_complex64_array___convert_complex___returns_original_array() -> None`

### `def test___complex64_array_to_complex128_array___convert_complex___converts_array() -> None`

### `def test___complex128_array_to_complexint32_array___convert_complex___converts_array() -> None`

### `def test___complex128_array_to_complex64_array___convert_complex___converts_array() -> None`

### `def test___complex128_array_to_complex128_array___convert_complex___returns_original_array() -> None`

### `def test___2d_complexint32_array_to_complex128_array___convert_complex___preserves_shape() -> None`

### `def test___2d_complex64_array_to_complex128_array___convert_complex___preserves_shape() -> None`

### `def test___arrays_with_static_shape___convert_complex___preserves_static_and_runtime_shape() -> None`

### `def test___complexint32_scalar_to_complex128_scalar___convert_complex___converts_scalar() -> None`

### `def test___complex128_scalar_to_complexint32_scalar___convert_complex___converts_scalar() -> None`

### `def test___complexint32_scalar_to_complexint32_scalar___convert_complex___returns_original_scalar() -> None`

### `def test___complex64_scalar_to_complex128_scalar___convert_complex___converts_scalar() -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/complex/test_dtypes.py -->
## PYTHON MODULE: tests/unit/complex/test_dtypes.py

### `def test___complexint32_dtype___np_array___constructs_array_with_dtype() -> None`

### `def test___complexint32_dtype___np_zeros___constructs_array_with_dtype() -> None`

### `def test___complexint32_array___index___returns_complexint32_scalar() -> None`

### `def test___complexint32_arrays___add___raises_type_error() -> None`

### `def test___complexint32_array_and_int16_array___add___raises_type_error() -> None`

### `def test___unknown_structured_dtype___equality___not_equal() -> None`

### `def test___duplicate_structured_dtype___equality___equal() -> None`

### `def test___structured_dtype_str___equality___not_equal() -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/scalar/__init__.py -->
## PYTHON MODULE: tests/unit/scalar/__init__.py

### MODULE DOCSTRING

Unit tests for the nitypes.scalar package.

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/scalar/test_scalar.py -->
## PYTHON MODULE: tests/unit/scalar/test_scalar.py

### `def test___bool_data_value___create___creates_scalar_data_with_data_and_default_units() -> None`

### `def test___int_data_value___create___creates_scalar_data_with_data_and_default_units() -> None`

### `def test___float_data_value___create___creates_scalar_data_with_data_and_default_units() -> None`

### `def test___str_data_value___create___creates_scalar_data_with_data_and_default_units() -> None`

### `def test___data_value_and_units___create___creates_scalar_data_with_data_and_units(data_value: Any, units: str) -> None`

### `def test___invalid_data_value___create___raises_type_error(data_value: Any) -> None`

### `def test___both_units_specified_unequal__create___raises_value_error() -> None`

### `def test___units_only_specified_in_extended_properties__create___creates_with_units() -> None`

### `def test___same_value___comparison___equal(left: Scalar[TScalar_co], right: Scalar[TScalar_co]) -> None`

### `def test___lesser_value___comparison___lesser(left: Scalar[TScalar_co], right: Scalar[TScalar_co]) -> None`

### `def test___mixed_numeric_types___comparison___lesser(left: Scalar[TScalar_co], right: Scalar[TScalar_co]) -> None`

### `def test___numeric_and_string___comparison___throws_exception(left: Scalar[TScalar_co], right: Scalar[TScalar_co]) -> None`

### `def test___different_units___comparison___throws_exception() -> None`

### `def test___various_values___repr___looks_ok(value: Scalar[Any], expected_repr: str) -> None`

### `def test___various_values___str___looks_ok(value: Scalar[Any], expected_str: str) -> None`

### `def test___scalar_with_units___get_extended_properties___returns_correct_dictionary() -> None`

### `def test___scalar_with_units___set_units___units_updated_correctly() -> None`

### `def test___various_values___copy___makes_copy(value: Scalar[TScalar_co]) -> None`

### `def test___various_values___pickle_unpickle___makes_copy(value: Scalar[TScalar_co]) -> None`

### `def test___scalar___pickle___references_public_modules() -> None`

### `def test___pickled_value___unpickle___is_compatible(pickled_value: bytes, expected: Scalar[Any]) -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/test_placeholder.py -->
## PYTHON MODULE: tests/unit/test_placeholder.py

### `def test___placeholder() -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/time/__init__.py -->
## PYTHON MODULE: tests/unit/time/__init__.py

### MODULE DOCSTRING

Unit tests for the nitypes.time package.

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/time/test_conversion.py -->
## PYTHON MODULE: tests/unit/time/test_conversion.py

- `_BT_EPSILON = ht.timedelta(yoctoseconds=54210)`

- `_DT_EPSILON = ht.timedelta(microseconds=1)`

### `def test___bt_to_bt___convert_datetime___returns_original_object() -> None`

### `def test___dt_to_dt___convert_datetime___returns_original_object() -> None`

### `def test___ht_to_ht___convert_datetime___returns_original_object() -> None`

### `def test___bt_to_dt___convert_datetime___returns_equivalent_dt_datetime() -> None`

### `def test___bt_to_ht___convert_datetime___returns_equivalent_ht_datetime() -> None`

### `def test___dt_to_bt___convert_datetime___returns_equivalent_bt_datetime() -> None`

### `def test___dt_to_ht___convert_datetime___returns_equivalent_ht_datetime() -> None`

### `def test___ht_to_bt___convert_datetime___returns_equivalent_bt_datetime() -> None`

### `def test___ht_to_dt___convert_datetime___returns_equivalent_dt_datetime() -> None`

### `def test___precise_ht_to_bt___convert_datetime___loses_precision() -> None`

### `def test___precise_ht_to_dt___convert_datetime___loses_precision() -> None`

### `def test___variable_requested_type___convert_datetime___static_return_type_unknown(requested_type: type[Any]) -> None`

### `def test___invalid_requested_type___convert_datetime___raises_type_error(value_in: bt.DateTime | dt.datetime | ht.datetime) -> None`

### `def test___invalid_value___convert_datetime___raises_type_error(requested_type: type[Any]) -> None`

### `def test___bt_to_bt___convert_timedelta___returns_original_object() -> None`

### `def test___dt_to_dt___convert_timedelta___returns_original_object() -> None`

### `def test___ht_to_ht___convert_timedelta___returns_original_object() -> None`

### `def test___bt_to_dt___convert_timedelta___returns_equivalent_dt_timedelta() -> None`

### `def test___bt_to_ht___convert_timedelta___returns_equivalent_ht_timedelta() -> None`

### `def test___dt_to_bt___convert_timedelta___returns_equivalent_bt_timedelta() -> None`

### `def test___dt_to_ht___convert_timedelta___returns_equivalent_ht_timedelta() -> None`

### `def test___ht_to_bt___convert_timedelta___returns_equivalent_bt_timedelta() -> None`

### `def test___ht_to_dt___convert_timedelta___returns_equivalent_dt_timedelta() -> None`

### `def test___precise_ht_to_bt___convert_timedelta___loses_precision() -> None`

### `def test___precise_ht_to_dt___convert_timedelta___loses_precision() -> None`

### `def test___variable_requested_type___convert_timedelta___static_return_type_unknown(requested_type: type[Any]) -> None`

### `def test___invalid_requested_type___convert_timedelta___raises_type_error(value_in: dt.timedelta | ht.timedelta) -> None`

### `def test___invalid_value___convert_timedelta___raises_type_error(requested_type: type[Any]) -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/vector/__init__.py -->
## PYTHON MODULE: tests/unit/vector/__init__.py

### MODULE DOCSTRING

Unit tests for the nitypes.vector package.

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/vector/test_vector.py -->
## PYTHON MODULE: tests/unit/vector/test_vector.py

### `def test___no_data_values_no_type___create___raises_type_error() -> None`

### `def test___no_data_values_bool_type___create___creates_with_bool_type() -> None`

### `def test___bool_data_values___create___creates_with_bool_data_and_default_units() -> None`

### `def test___int_data_values___create___creates_with_int_data_and_default_units() -> None`

### `def test___float_data_values___create___creates_with_float_data_and_default_units() -> None`

### `def test___str_data_values___create___creates_with_str_data_and_default_units() -> None`

### `def test___generator_data_values___create___creates_with_data_and_default_units() -> None`

### `def test___data_value_and_units___create___creates_scalar_data_with_data_and_units(data_value: Any, units: str) -> None`

### `def test___both_units_specified_unequal__create___raises_value_error() -> None`

### `def test___units_only_specified_in_extended_properties__create___creates_with_units() -> None`

### `def test___invalid_data_value___create___raises_type_error(data_value: Any) -> None`

### `def test___invalid_generator_data_values___create___raises_type_error() -> None`

### `def test___empty_generator_data_values___create___raises_type_error() -> None`

### `def test___mixed_data_values___create___raises_type_error() -> None`

### `def test___vector_with_data___get_item_at_index___returns_correct_value() -> None`

### `def test___vector_with_data___get_item_at_slice___returns_correct_values() -> None`

### `def test___vector_with_data___set_item_at_index___value_set_correctly() -> None`

### `def test___vector_with_data___set_item_at_slice___values_set_correctly() -> None`

### `def test___vector_with_data___set_item_at_slice_with_generator___values_set_correctly() -> None`

### `def test___vector_with_data___set_item_at_slice_to_empty_list___values_set_correctly() -> None`

### `def test___vector_with_data___append_same_type___values_appended() -> None`

### `def test___vector_with_data___append_different_type___raises_type_error() -> None`

### `def test___no_data_values_bool_type___append___appends_bool_data() -> None`

### `def test___vector_with_data___extend_same_type___values_extended() -> None`

### `def test___vector_with_data___extend_different_type___raises_type_error() -> None`

### `def test___vector_with_data___extend_mixed_type___raises_type_error() -> None`

### `def test___no_data_values_bool_type___extend___extends_bool_data() -> None`

### `def test___vector_with_data___extend_with_empty_list___values_unchanged() -> None`

### `def test___vector_with_data___delete_at_index___value_deleted() -> None`

### `def test___vector_with_data___delete_at_slice___values_deleted() -> None`

### `def test___vector_with_data___remove_value___value_removed() -> None`

### `def test___vector_with_data___check_length___length_correct() -> None`

### `def test___same_value___comparison___equal(left: Vector[TScalar], right: Vector[TScalar]) -> None`

### `def test___different_values___comparison___not_equal(left: Vector[TScalar], right: Vector[TScalar]) -> None`

### `def test___different_units___comparison___not_equal() -> None`

### `def test___various_values___repr___looks_ok(value: Vector[Any], expected_repr: str) -> None`

### `def test___various_values___str___looks_ok(value: Vector[Any], expected_str: str) -> None`

### `def test___vector_with_units___get_extended_properties___returns_correct_dictionary() -> None`

### `def test___vector_with_units___set_units___units_updated_correctly() -> None`

### `def test___various_values___copy___makes_copy(value: Vector[TScalar]) -> None`

### `def test___various_values___pickle_unpickle___makes_copy(value: Vector[TScalar]) -> None`

### `def test___vector___pickle___references_public_modules() -> None`

### `def test___pickled_value___unpickle___is_compatible(pickled_value: bytes, expected: Vector[Any]) -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/waveform/__init__.py -->
## PYTHON MODULE: tests/unit/waveform/__init__.py

### MODULE DOCSTRING

Unit tests for the nitypes.waveform package.

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/waveform/_scaling/__init__.py -->
## PYTHON MODULE: tests/unit/waveform/_scaling/__init__.py

### MODULE DOCSTRING

Unit tests for the nitypes.waveform._scaling package.

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/waveform/_scaling/test_linear.py -->
## PYTHON MODULE: tests/unit/waveform/_scaling/test_linear.py

### `def test___gain_and_offset___construct___constructs_with_gain_and_offset(gain: SupportsFloat, offset: SupportsFloat) -> None`

### `def test__invalid_gain_or_offset___construct___raises_type_error(gain: object, offset: object, expected_message: str) -> None`

### `def test___empty_ndarray___transform_data___returns_empty_scaled_data() -> None`

### `def test___float32_ndarray___transform_data___returns_float32_scaled_data() -> None`

### `def test___float64_ndarray___transform_data___returns_float64_scaled_data() -> None`

### `def test___complex64_ndarray___transform_data___returns_complex64_scaled_data() -> None`

### `def test___complex128_ndarray___transform_data___returns_complex128_scaled_data() -> None`

### `def test___same_value___equality___equal(left: LinearScaleMode, right: LinearScaleMode) -> None`

### `def test___different_value___equality___not_equal(left: ScaleMode, right: ScaleMode) -> None`

### `def test___scale_mode___repr___looks_ok() -> None`

### `def test___scale_mode___copy___makes_shallow_copy() -> None`

### `def test___scale_mode___deepcopy___makes_deep_copy() -> None`

### `def test___scale_mode___pickle_unpickle___makes_deep_copy() -> None`

### `def test___scale_mode___pickle___references_public_modules() -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/waveform/_scaling/test_none.py -->
## PYTHON MODULE: tests/unit/waveform/_scaling/test_none.py

### `def test___no_scaling___type_is_none_scale_mode() -> None`

### `def test___empty_ndarray___transform_data___returns_empty_scaled_data() -> None`

### `def test___float32_ndarray___transform_data___returns_float32_scaled_data() -> None`

### `def test___float64_ndarray___transform_data___returns_float64_scaled_data() -> None`

### `def test___complex64_ndarray___transform_data___returns_complex64_scaled_data() -> None`

### `def test___complex128_ndarray___transform_data___returns_complex128_scaled_data() -> None`

### `def test___scale_mode___repr___looks_ok() -> None`

### `def test___scale_mode___copy___makes_shallow_copy() -> None`

### `def test___scale_mode___deepcopy___makes_deep_copy() -> None`

### `def test___scale_mode___pickle_unpickle___makes_deep_copy() -> None`

### `def test___scale_mode___pickle___references_public_modules() -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/waveform/_timing/__init__.py -->
## PYTHON MODULE: tests/unit/waveform/_timing/__init__.py

### MODULE DOCSTRING

Unit tests for the nitypes.waveform._timing package.

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/waveform/_timing/_utils.py -->
## PYTHON MODULE: tests/unit/waveform/_timing/_utils.py

### `def assert_deep_copy(value: Timing[Any, Any, Any], other: Timing[Any, Any, Any]) -> None`

Assert that value is a deep copy of other.

### `def assert_shallow_copy(value: Timing[Any, Any, Any], other: Timing[Any, Any, Any]) -> None`

Assert that value is a shallow copy of other.

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/waveform/_timing/test_bintime.py -->
## PYTHON MODULE: tests/unit/waveform/_timing/test_bintime.py

### `def test___empty___is_timing() -> None`

### `def test___empty___no_timestamp() -> None`

### `def test___empty___no_start_time() -> None`

### `def test___empty___no_time_offset() -> None`

### `def test___empty___no_sample_interval() -> None`

### `def test___empty___sample_interval_mode_none() -> None`

### `def test___no_optional_args___construct___creates_empty_timing() -> None`

### `def test___timestamp___construct___creates_timing_with_timestamp() -> None`

### `def test___timestamp___construct___has_start_time() -> None`

### `def test___time_offset___construct___creates_timing_with_time_offset() -> None`

### `def test___sample_interval___construct___creates_timing_with_sample_interval() -> None`

### `def test___sample_interval_timestamp_and_time_offset___construct___creates_timing_with_sample_interval_timestamp_and_time_offset() -> None`

### `def test___no_args___create_with_no_interval___creates_empty_timing() -> None`

### `def test___timestamp___create_with_no_interval___creates_timing_with_timestamp() -> None`

### `def test___timestamp_and_time_offset___create_with_no_interval___creates_timing_with_timestamp_and_time_offset() -> None`

### `def test___time_offset___create_with_no_interval___creates_timing_with_time_offset() -> None`

### `def test___sample_interval___create_with_regular_interval___creates_timing_with_sample_interval() -> None`

### `def test___sample_interval_and_timestamp___create_with_regular_interval___creates_timing_with_sample_interval_and_timestamp() -> None`

### `def test___sample_interval_timestamp_and_time_offset___create_with_regular_interval___creates_timing_with_sample_interval_timestamp_and_time_offset() -> None`

### `def test___sample_interval_and_time_offset___create_with_regular_interval___creates_timing_with_sample_interval_and_time_offset() -> None`

### `def test___monotonic_timestamps___create_with_irregular_interval___creates_timing_with_timestamps(time_offsets: list[bt.TimeDelta]) -> None`

### `def test___non_monotonic_timestamps___create_with_irregular_interval___raises_value_error(time_offsets: list[bt.TimeDelta]) -> None`

### `def test___timestamps_tuple___create_with_irregular_interval___creates_timing_with_timestamps() -> None`

### `def test___no_interval___get_timestamps___raises_correct_error() -> None`

### `def test___regular_interval___get_timestamps___gets_timestamps() -> None`

### `def test___irregular_interval___get_timestamps___gets_timestamps() -> None`

### `def test___irregular_interval_subset___get_timestamps___gets_timestamps() -> None`

### `def test___same_value___equality___equal(left: Timing[Any, Any, Any], right: Timing[Any, Any, Any]) -> None`

### `def test___different_value___equality___not_equal(left: Timing[Any, Any, Any], right: Timing[Any, Any, Any]) -> None`

### `def test___various_values___repr___looks_ok(value: Timing[Any, Any, Any], expected_repr: str) -> None`

- `_VARIOUS_VALUES = [Timing.create_with_no_interval(), Timing.create_with_no_interval(bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc)), Timing.create_with_no_interval(None, bt.TimeDelta(1)), Timing.create_with_no_interval(bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), bt.TimeDelta(1)), Timing.create_with_regular_interval(bt.TimeDelta(0.001)), Timing.create_with_regular_interval(bt.TimeDelta(0.001), bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc)), Timing.create_with_regular_interval(bt.TimeDelta(0.001), bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), bt.TimeDelta(1)), Timing.create_with_irregular_interval([bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), bt.DateTime(2025, 1, 2, tzinfo=dt.timezone.utc)])]`

### `def test___various_values___copy___makes_shallow_copy(value: Timing[Any, Any, Any]) -> None`

### `def test___various_values___deepcopy___makes_deep_copy(value: Timing[Any, Any, Any]) -> None`

### `def test___various_values___pickle_unpickle___makes_deep_copy(value: Timing[Any, Any, Any]) -> None`

### `def test___timing___pickle___references_public_modules() -> None`

### `def test___monotonic_timestamps___append_timing___appends_timestamps(left_offsets: list[bt.TimeDelta], right_offsets: list[bt.TimeDelta]) -> None`

### `def test___non_monotonic_timestamps___append_timing___raises_value_error(left_offsets: list[bt.TimeDelta], right_offsets: list[bt.TimeDelta]) -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/waveform/_timing/test_conversion.py -->
## PYTHON MODULE: tests/unit/waveform/_timing/test_conversion.py

### `def test___bt_to_bt___convert_timing___returns_original_object() -> None`

### `def test___dt_to_dt___convert_timing___returns_original_object() -> None`

### `def test___ht_to_ht___convert_timing___returns_original_object() -> None`

### `def test___empty_to_bt___convert_timing___returns_equivalent_timing() -> None`

### `def test___empty_to_dt___convert_timing___returns_original_object() -> None`

### `def test___empty_to_ht___convert_timing___returns_equivalent_timing() -> None`

### `def test___dt_to_bt_regular_interval___convert_timing___returns_equivalent_timing() -> None`

### `def test___dt_to_ht_regular_interval___convert_timing___returns_equivalent_timing() -> None`

### `def test___ht_to_dt_regular_interval___convert_timing___returns_equivalent_timing() -> None`

### `def test___dt_to_ht_irregular_interval___convert_timing___returns_equivalent_timing() -> None`

### `def test___ht_to_dt_irregular_interval___convert_timing___returns_equivalent_timing() -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/waveform/_timing/test_datetime.py -->
## PYTHON MODULE: tests/unit/waveform/_timing/test_datetime.py

### `def test___empty___is_timing() -> None`

### `def test___empty___no_timestamp() -> None`

### `def test___empty___no_start_time() -> None`

### `def test___empty___no_time_offset() -> None`

### `def test___empty___no_sample_interval() -> None`

### `def test___empty___sample_interval_mode_none() -> None`

### `def test___no_optional_args___construct___creates_empty_timing() -> None`

### `def test___timestamp___construct___creates_timing_with_timestamp() -> None`

### `def test___timestamp___construct___has_start_time() -> None`

### `def test___time_offset___construct___creates_timing_with_time_offset() -> None`

### `def test___sample_interval___construct___creates_timing_with_sample_interval() -> None`

### `def test___sample_interval_timestamp_and_time_offset___construct___creates_timing_with_sample_interval_timestamp_and_time_offset() -> None`

### `def test___no_args___create_with_no_interval___creates_empty_timing() -> None`

### `def test___timestamp___create_with_no_interval___creates_timing_with_timestamp() -> None`

### `def test___timestamp_and_time_offset___create_with_no_interval___creates_timing_with_timestamp_and_time_offset() -> None`

### `def test___time_offset___create_with_no_interval___creates_timing_with_time_offset() -> None`

### `def test___sample_interval___create_with_regular_interval___creates_timing_with_sample_interval() -> None`

### `def test___sample_interval_and_timestamp___create_with_regular_interval___creates_timing_with_sample_interval_and_timestamp() -> None`

### `def test___sample_interval_timestamp_and_time_offset___create_with_regular_interval___creates_timing_with_sample_interval_timestamp_and_time_offset() -> None`

### `def test___sample_interval_and_time_offset___create_with_regular_interval___creates_timing_with_sample_interval_and_time_offset() -> None`

### `def test___monotonic_timestamps___create_with_irregular_interval___creates_timing_with_timestamps(time_offsets: list[dt.timedelta]) -> None`

### `def test___non_monotonic_timestamps___create_with_irregular_interval___raises_value_error(time_offsets: list[dt.timedelta]) -> None`

### `def test___timestamps_tuple___create_with_irregular_interval___creates_timing_with_timestamps() -> None`

### `def test___no_interval___get_timestamps___raises_correct_error() -> None`

### `def test___regular_interval___get_timestamps___gets_timestamps() -> None`

### `def test___irregular_interval___get_timestamps___gets_timestamps() -> None`

### `def test___irregular_interval_subset___get_timestamps___gets_timestamps() -> None`

### `def test___same_value___equality___equal(left: Timing[Any, Any, Any], right: Timing[Any, Any, Any]) -> None`

### `def test___different_value___equality___not_equal(left: Timing[Any, Any, Any], right: Timing[Any, Any, Any]) -> None`

### `def test___various_values___repr___looks_ok(value: Timing[Any, Any, Any], expected_repr: str) -> None`

- `_VARIOUS_VALUES = [Timing.create_with_no_interval(), Timing.create_with_no_interval(dt.datetime(2025, 1, 1)), Timing.create_with_no_interval(None, dt.timedelta(seconds=1)), Timing.create_with_no_interval(dt.datetime(2025, 1, 1), dt.timedelta(seconds=1)), Timing.create_with_regular_interval(dt.timedelta(milliseconds=1)), Timing.create_with_regular_interval(dt.timedelta(milliseconds=1), dt.datetime(2025, 1, 1)), Timing.create_with_regular_interval(dt.timedelta(milliseconds=1), dt.datetime(2025, 1, 1), dt.timedelta(seconds=1)), Timing.create_with_irregular_interval([dt.datetime(2025, 1, 1), dt.datetime(2025, 1, 2)])]`

### `def test___various_values___copy___makes_shallow_copy(value: Timing[Any, Any, Any]) -> None`

### `def test___various_values___deepcopy___makes_deep_copy(value: Timing[Any, Any, Any]) -> None`

### `def test___various_values___pickle_unpickle___makes_deep_copy(value: Timing[Any, Any, Any]) -> None`

### `def test___timing___pickle___references_public_modules() -> None`

### `def test___monotonic_timestamps___append_timing___appends_timestamps(left_offsets: list[dt.timedelta], right_offsets: list[dt.timedelta]) -> None`

### `def test___non_monotonic_timestamps___append_timing___raises_value_error(left_offsets: list[dt.timedelta], right_offsets: list[dt.timedelta]) -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/waveform/_timing/test_hightime.py -->
## PYTHON MODULE: tests/unit/waveform/_timing/test_hightime.py

### `def test___empty___is_timing() -> None`

### `def test___empty___no_timestamp() -> None`

### `def test___empty___no_start_time() -> None`

### `def test___empty___no_time_offset() -> None`

### `def test___empty___no_sample_interval() -> None`

### `def test___empty___sample_interval_mode_none() -> None`

### `def test___no_optional_args___construct___creates_empty_timing() -> None`

### `def test___timestamp___construct___creates_timing_with_timestamp() -> None`

### `def test___timestamp___construct___has_start_time() -> None`

### `def test___time_offset___construct___creates_timing_with_time_offset() -> None`

### `def test___sample_interval___construct___creates_timing_with_sample_interval() -> None`

### `def test___sample_interval_timestamp_and_time_offset___construct___creates_timing_with_sample_interval_timestamp_and_time_offset() -> None`

### `def test___no_args___create_with_no_interval___creates_empty_timing() -> None`

### `def test___timestamp___create_with_no_interval___creates_timing_with_timestamp() -> None`

### `def test___timestamp_and_time_offset___create_with_no_interval___creates_timing_with_timestamp_and_time_offset() -> None`

### `def test___time_offset___create_with_no_interval___creates_timing_with_time_offset() -> None`

### `def test___sample_interval___create_with_regular_interval___creates_timing_with_sample_interval() -> None`

### `def test___sample_interval_and_timestamp___create_with_regular_interval___creates_timing_with_sample_interval_and_timestamp() -> None`

### `def test___sample_interval_timestamp_and_time_offset___create_with_regular_interval___creates_timing_with_sample_interval_timestamp_and_time_offset() -> None`

### `def test___sample_interval_and_time_offset___create_with_regular_interval___creates_timing_with_sample_interval_and_time_offset() -> None`

### `def test___monotonic_timestamps___create_with_irregular_interval___creates_timing_with_timestamps(time_offsets: list[ht.timedelta]) -> None`

### `def test___non_monotonic_timestamps___create_with_irregular_interval___raises_value_error(time_offsets: list[ht.timedelta]) -> None`

### `def test___timestamps_tuple___create_with_irregular_interval___creates_timing_with_timestamps() -> None`

### `def test___no_interval___get_timestamps___raises_correct_error() -> None`

### `def test___regular_interval___get_timestamps___gets_timestamps() -> None`

### `def test___irregular_interval___get_timestamps___gets_timestamps() -> None`

### `def test___irregular_interval_subset___get_timestamps___gets_timestamps() -> None`

### `def test___same_value___equality___equal(left: Timing[Any, Any, Any], right: Timing[Any, Any, Any]) -> None`

### `def test___different_value___equality___not_equal(left: Timing[Any, Any, Any], right: Timing[Any, Any, Any]) -> None`

### `def test___various_values___repr___looks_ok(value: Timing[Any, Any, Any], expected_repr: str) -> None`

- `_VARIOUS_VALUES = [Timing.create_with_no_interval(), Timing.create_with_no_interval(ht.datetime(2025, 1, 1)), Timing.create_with_no_interval(None, ht.timedelta(seconds=1)), Timing.create_with_no_interval(ht.datetime(2025, 1, 1), ht.timedelta(seconds=1)), Timing.create_with_regular_interval(ht.timedelta(milliseconds=1)), Timing.create_with_regular_interval(ht.timedelta(milliseconds=1), ht.datetime(2025, 1, 1)), Timing.create_with_regular_interval(ht.timedelta(milliseconds=1), ht.datetime(2025, 1, 1), ht.timedelta(seconds=1)), Timing.create_with_irregular_interval([ht.datetime(2025, 1, 1), ht.datetime(2025, 1, 2)])]`

### `def test___various_values___copy___makes_shallow_copy(value: Timing[Any, Any, Any]) -> None`

### `def test___various_values___deepcopy___makes_deep_copy(value: Timing[Any, Any, Any]) -> None`

### `def test___various_values___pickle_unpickle___makes_deep_copy(value: Timing[Any, Any, Any]) -> None`

### `def test___timing___pickle___references_public_modules() -> None`

### `def test___monotonic_timestamps___append_timing___appends_timestamps(left_offsets: list[ht.timedelta], right_offsets: list[ht.timedelta]) -> None`

### `def test___non_monotonic_timestamps___append_timing___raises_value_error(left_offsets: list[ht.timedelta], right_offsets: list[ht.timedelta]) -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/waveform/test_analog_waveform.py -->
## PYTHON MODULE: tests/unit/waveform/test_analog_waveform.py

### `def test___no_args___create___creates_empty_waveform_with_default_dtype() -> None`

### `def test___sample_count___create___creates_waveform_with_sample_count_and_default_dtype() -> None`

### `def test___sample_count_and_dtype___create___creates_waveform_with_sample_count_and_dtype() -> None`

### `def test___sample_count_and_dtype_str___create___creates_waveform_with_sample_count_and_dtype() -> None`

### `def test___sample_count_and_dtype_any___create___creates_waveform_with_sample_count_and_dtype() -> None`

### `def test___sample_count_dtype_and_capacity___create___creates_waveform_with_sample_count_dtype_and_capacity() -> None`

### `def test___sample_count_and_unsupported_dtype___create___raises_type_error(dtype: npt.DTypeLike) -> None`

### `def test___dtype_str_with_unsupported_traw_hint___create___mypy_type_var_warning() -> None`

### `def test___dtype_str_with_traw_hint___create___narrows_traw() -> None`

### `def test___float64_ndarray___from_array_1d___creates_waveform_with_float64_dtype() -> None`

### `def test___int32_ndarray___from_array_1d___creates_waveform_with_int32_dtype() -> None`

### `def test___int32_array_with_dtype___from_array_1d___creates_waveform_with_specified_dtype() -> None`

### `def test___int16_ndarray_with_mismatched_dtype___from_array_1d___creates_waveform_with_specified_dtype() -> None`

### `def test___int_list_with_dtype___from_array_1d___creates_waveform_with_specified_dtype() -> None`

### `def test___int_list_with_dtype_str___from_array_1d___creates_waveform_with_specified_dtype() -> None`

### `def test___int32_ndarray_2d___from_array_1d___raises_value_error() -> None`

### `def test___int_list_without_dtype___from_array_1d___raises_value_error() -> None`

### `def test___bytes___from_array_1d___raises_value_error() -> None`

### `def test___iterable___from_array_1d___raises_type_error() -> None`

### `def test___ndarray_with_unsupported_dtype___from_array_1d___raises_type_error() -> None`

### `def test___copy___from_array_1d___creates_waveform_linked_to_different_buffer() -> None`

### `def test___int32_ndarray_no_copy___from_array_1d___creates_waveform_linked_to_same_buffer() -> None`

### `def test___int32_array_no_copy___from_array_1d___creates_waveform_linked_to_same_buffer() -> None`

### `def test___int_list_no_copy___from_array_1d___raises_value_error() -> None`

### `def test___array_subset___from_array_1d___creates_waveform_with_array_subset(start_index: SupportsIndex, sample_count: SupportsIndex | None, expected_data: list[int]) -> None`

### `def test___invalid_array_subset___from_array_1d___raises_correct_error(start_index: SupportsIndex, sample_count: SupportsIndex | None, expected_message: str, exception_type: type[Exception]) -> None`

### `def test___float64_ndarray___from_array_2d___creates_waveform_with_float64_dtype() -> None`

### `def test___int32_ndarray___from_array_2d___creates_waveform_with_int32_dtype() -> None`

### `def test___int16_ndarray_with_mismatched_dtype___from_array_2d___creates_waveform_with_specified_dtype() -> None`

### `def test___int32_array_list_with_dtype___from_array_2d___creates_waveform_with_specified_dtype() -> None`

### `def test___int_list_list_with_dtype___from_array_2d___creates_waveform_with_specified_dtype() -> None`

### `def test___int_list_list_with_dtype_str___from_array_2d___creates_waveform_with_specified_dtype() -> None`

### `def test___int32_ndarray_1d___from_array_2d___raises_value_error() -> None`

### `def test___int_list_list_without_dtype___from_array_2d___raises_value_error() -> None`

### `def test___bytes_list___from_array_2d___raises_value_error() -> None`

### `def test___list_iterable___from_array_2d___raises_type_error() -> None`

### `def test___iterable_list___from_array_2d___raises_type_error() -> None`

### `def test___ndarray_with_unsupported_dtype___from_array_2d___raises_type_error() -> None`

### `def test___copy___from_array_2d___creates_waveform_linked_to_different_buffer() -> None`

### `def test___int32_ndarray_no_copy___from_array_2d___creates_waveform_linked_to_same_buffer() -> None`

### `def test___int32_array_list_no_copy___from_array_2d___creates_waveform_linked_to_same_buffer() -> None`

### `def test___int_list_list_no_copy___from_array_2d___raises_value_error() -> None`

### `def test___array_subset___from_array_2d___creates_waveform_with_array_subset(start_index: SupportsIndex, sample_count: SupportsIndex | None, expected_data: list[list[int]]) -> None`

### `def test___invalid_array_subset___from_array_2d___raises_correct_error(start_index: SupportsIndex, sample_count: SupportsIndex | None, expected_message: str, exception_type: type[Exception]) -> None`

### `def test___int32_waveform___raw_data___returns_int32_data() -> None`

### `def test___int32_waveform_with_linear_scale___raw_data___returns_int32_data() -> None`

### `def test___int32_waveform___get_raw_data___returns_raw_data() -> None`

### `def test___int32_waveform_with_linear_scale___get_raw_data___returns_raw_data() -> None`

### `def test___array_subset___get_raw_data___returns_array_subset(start_index: int, sample_count: int, expected_raw_data: list[int]) -> None`

### `def test___invalid_array_subset___get_raw_data___returns_array_subset(start_index: int, sample_count: int, expected_message: str, exception_type: type[Exception]) -> None`

### `def test___int32_waveform___scaled_data___converts_to_float64() -> None`

### `def test___int32_waveform_with_linear_scale___scaled_data___applies_linear_scale() -> None`

### `def test___int32_waveform___get_scaled_data___converts_to_float64() -> None`

### `def test___int32_waveform_with_linear_scale___get_scaled_data___applies_linear_scale() -> None`

### `def test___float32_dtype___get_scaled_data___converts_to_float32() -> None`

### `def test___varying_dtype___get_scaled_data___converts_to_requested_dtype(waveform_dtype: npt.DTypeLike, scaled_dtype: npt.DTypeLike) -> None`

### `def test___unsupported_dtype___get_scaled_data___raises_type_error() -> None`

### `def test___array_subset___get_scaled_data___returns_array_subset() -> None`

### `def test___waveform___set_sample_count___updates_sample_count() -> None`

### `def test___waveform___set_sample_count_exceeds_capacity___raises_value_error() -> None`

### `def test___waveform___set_capacity___resizes_array_and_pads_with_zeros(capacity: int, expected_data: list[int]) -> None`

### `def test___invalid_capacity___set_capacity___raises_correct_error(capacity: int, expected_message: str, exception_type: type[Exception]) -> None`

### `def test___referenced_array___set_capacity___reference_sees_size_change() -> None`

### `def test___array_with_external_buffer___set_capacity___raises_value_error() -> None`

### `def test___waveform___set_channel_name___sets_extended_property() -> None`

### `def test___invalid_type___set_channel_name___raises_type_error() -> None`

### `def test___waveform___set_units___sets_extended_property() -> None`

### `def test___invalid_type___set_units___raises_type_error() -> None`

### `def test___waveform___set_undefined_property___raises_attribute_error() -> None`

### `def test___waveform___take_weak_ref___references_waveform() -> None`

### `def test___waveform___has_empty_timing() -> None`

### `def test___bintime___waveform_with_timing___static_type_erased() -> None`

### `def test___datetime___waveform_with_timing___static_type_erased() -> None`

### `def test___hightime___waveform_with_timing___static_type_erased() -> None`

### `def test___polymorphic_timing___get_timing_properties___behaves_polymorphically(timing: Timing[Any, Any, Any]) -> None`

### `def test___waveform___scale_mode___defaults_to_no_scaling() -> None`

### `def test___empty_ndarray___append___no_effect() -> None`

### `def test___int32_ndarray___append___appends_array() -> None`

### `def test___float64_ndarray___append___appends_array() -> None`

### `def test___ndarray_with_mismatched_dtype___append___raises_correct_error() -> None`

### `def test___ndarray_2d___append___raises_value_error() -> None`

### `def test___irregular_waveform_and_int32_ndarray_with_timestamps___append___appends_array() -> None`

### `def test___irregular_waveform_and_int32_ndarray_without_timestamps___append___raises_timing_mismatch_error_and_does_not_append() -> None`

### `def test___irregular_waveform_and_int32_ndarray_with_wrong_timestamp_count___append___raises_correct_error_and_does_not_append() -> None`

### `def test___regular_waveform_and_int32_ndarray_with_timestamps___append___raises_value_error_and_does_not_append() -> None`

### `def test___empty_waveform___append___no_effect() -> None`

### `def test___int32_waveform___append___appends_waveform() -> None`

### `def test___float64_waveform___append___appends_waveform() -> None`

### `def test___waveform_with_mismatched_dtype___append___raises_correct_error() -> None`

### `def test___irregular_waveform_and_irregular_waveform___append___appends_waveform() -> None`

### `def test___irregular_waveform_and_regular_waveform___append___raises_correct_error() -> None`

### `def test___regular_waveform_and_irregular_waveform___append___raises_correct_error() -> None`

### `def test___regular_waveform_and_regular_waveform_with_different_sample_interval___append___appends_waveform_with_timing_mismatch_warning() -> None`

### `def test___regular_waveform_and_regular_waveform_with_different_extended_properties___append___merges_extended_properties() -> None`

### `def test___regular_waveform_and_regular_waveform_with_different_scale_mode___append___appends_waveform_with_scaling_mismatch_warning() -> None`

### `def test___empty_waveform_list___append___no_effect() -> None`

### `def test___int32_waveform_list___append___appends_waveform() -> None`

### `def test___float64_waveform_tuple___append___appends_waveform() -> None`

### `def test___waveform_list_with_mismatched_dtype___append___raises_correct_error_and_does_not_append() -> None`

### `def test___irregular_waveform_and_irregular_waveform_list___append___appends_waveform() -> None`

### `def test___irregular_waveform_and_regular_waveform_list___append___raises_correct_error_and_does_not_append() -> None`

### `def test___regular_waveform_and_irregular_waveform_list___append___raises_correct_error_and_does_not_append() -> None`

### `def test___empty_ndarray___load_data___clears_data() -> None`

### `def test___int32_ndarray___load_data___overwrites_data() -> None`

### `def test___float64_ndarray___load_data___overwrites_data() -> None`

### `def test___ndarray_with_mismatched_dtype___load_data___raises_correct_error() -> None`

### `def test___ndarray_2d___load_data___raises_value_error() -> None`

### `def test___smaller_ndarray___load_data___preserves_capacity() -> None`

### `def test___larger_ndarray___load_data___grows_capacity() -> None`

### `def test___waveform_with_start_index___load_data___clears_start_index() -> None`

### `def test___ndarray_subset___load_data___overwrites_data() -> None`

### `def test___smaller_ndarray_no_copy___load_data___takes_ownership_of_array() -> None`

### `def test___larger_ndarray_no_copy___load_data___takes_ownership_of_array() -> None`

### `def test___ndarray_subset_no_copy___load_data___takes_ownership_of_array_subset() -> None`

### `def test___irregular_waveform_and_int32_ndarray_with_timestamps___load_data___overwrites_data_but_not_timestamps() -> None`

### `def test___irregular_waveform_and_int32_ndarray_with_wrong_sample_count___load_data___raises_correct_error_and_does_not_overwrite_data() -> None`

### `def test___same_value___equality___equal(left: AnalogWaveform[Any], right: AnalogWaveform[Any]) -> None`

### `def test___different_value___equality___not_equal(left: AnalogWaveform[Any], right: AnalogWaveform[Any]) -> None`

### `def test___various_values___repr___looks_ok(value: AnalogWaveform[Any], expected_repr: str) -> None`

- `_VARIOUS_VALUES = [AnalogWaveform(), AnalogWaveform(10), AnalogWaveform(10, np.float64), AnalogWaveform(10, np.int32), AnalogWaveform(10, np.int32, start_index=5, capacity=20), AnalogWaveform.from_array_1d([1, 2, 3], np.float64), AnalogWaveform.from_array_1d([1, 2, 3], np.int32), AnalogWaveform(timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))), AnalogWaveform(timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=1))), AnalogWaveform(extended_properties={'NI_ChannelName': 'Dev1/ai0', 'NI_UnitDescription': 'Volts'}), AnalogWaveform(scale_mode=LinearScaleMode(2.0, 1.0)), AnalogWaveform(10, np.int32, start_index=5, capacity=20), AnalogWaveform.from_array_1d([0, 0, 1, 2, 3, 4, 5, 0], np.int32, start_index=2, sample_count=5)]`

### `def test___various_values___copy___makes_shallow_copy(value: AnalogWaveform[Any]) -> None`

### `def _assert_shallow_copy(value: AnalogWaveform[Any], other: AnalogWaveform[Any]) -> None`

### `def test___various_values___deepcopy___makes_shallow_copy(value: AnalogWaveform[Any]) -> None`

### `def _assert_deep_copy(value: AnalogWaveform[Any], other: AnalogWaveform[Any]) -> None`

### `def test___various_values___pickle_unpickle___makes_deep_copy(value: AnalogWaveform[Any]) -> None`

### `def test___waveform___pickle___references_public_modules() -> None`

### `def test___pickled_value___unpickle___is_compatible(pickled_value: bytes, expected: AnalogWaveform[Any]) -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/waveform/test_complex_waveform.py -->
## PYTHON MODULE: tests/unit/waveform/test_complex_waveform.py

### `def test___sample_count_and_complexint32_dtype___create___creates_waveform_with_sample_count_and_dtype() -> None`

### `def test___sample_count_and_complex64_dtype___create___creates_waveform_with_sample_count_and_dtype() -> None`

### `def test___sample_count_and_complex128_dtype___create___creates_waveform_with_sample_count_and_dtype() -> None`

### `def test___sample_count_and_unknown_structured_dtype___create___raises_type_error() -> None`

### `def test___sample_count_and_structured_dtype_str___create___raises_type_error() -> None`

### `def test___sample_count_and_unsupported_dtype___create___raises_type_error(dtype: npt.DTypeLike) -> None`

### `def test___dtype_str_with_unsupported_traw_hint___create___mypy_type_var_warning() -> None`

### `def test___dtype_str_with_traw_hint___create___narrows_traw() -> None`

### `def test___complexint32_ndarray___from_array_1d___creates_waveform_with_complexint32_dtype() -> None`

### `def test___complex64_ndarray___from_array_1d___creates_waveform_with_complex64_dtype() -> None`

### `def test___complex128_ndarray___from_array_1d___creates_waveform_with_complex128_dtype() -> None`

### `def test___complex_list_with_dtype___from_array_1d___creates_waveform_with_specified_dtype() -> None`

### `def test___complex_list_with_dtype_str___from_array_1d___creates_waveform_with_specified_dtype() -> None`

### `def test___complexint32_ndarray___from_array_2d___creates_waveform_with_complexint32_dtype() -> None`

### `def test___complex64_ndarray___from_array_2d___creates_waveform_with_complex64_dtype() -> None`

### `def test___complex128_ndarray___from_array_2d___creates_waveform_with_complex128_dtype() -> None`

### `def test___complex_list_list_with_dtype___from_array_2d___creates_waveform_with_specified_dtype() -> None`

### `def test___int_list_list_with_dtype_str___from_array_2d___creates_waveform_with_specified_dtype() -> None`

### `def test___complexint32_waveform___raw_data___returns_complexint32_data() -> None`

### `def test___complex64_waveform___raw_data___returns_complex64_data() -> None`

### `def test___complexint32_waveform___scaled_data___converts_to_complex128() -> None`

### `def test___complex64_waveform___scaled_data___converts_to_complex128() -> None`

### `def test___complexint32_waveform_with_linear_scale___scaled_data___converts_to_complex128() -> None`

### `def test___complex64_waveform_with_linear_scale___scaled_data___converts_to_complex128() -> None`

### `def test___complexint32_waveform_with_complex64_dtype___get_scaled_data___converts_to_complex64() -> None`

### `def test___complex64_waveform_with_complex64_dtype___get_scaled_data___does_not_convert() -> None`

### `def test___complexint32_waveform_with_unknown_structured_dtype___get_scaled_data___raises_type_error() -> None`

### `def test___same_value___equality___equal(left: ComplexWaveform[Any], right: ComplexWaveform[Any]) -> None`

### `def test___different_value___equality___not_equal(left: ComplexWaveform[Any], right: ComplexWaveform[Any]) -> None`

### `def test___various_values___repr___looks_ok(value: ComplexWaveform[Any], expected_repr: str) -> None`

- `_VARIOUS_VALUES = [ComplexWaveform(), ComplexWaveform(10), ComplexWaveform(10, np.complex128), ComplexWaveform(10, ComplexInt32DType), ComplexWaveform(10, ComplexInt32DType, start_index=5, capacity=20), ComplexWaveform.from_array_1d([123 + 3.45j, 6.78 - 9.01j], np.complex128), ComplexWaveform.from_array_1d([(1, 2), (3, 4), (5, 6)], ComplexInt32DType), ComplexWaveform(timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))), ComplexWaveform(timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=1))), ComplexWaveform(extended_properties={'NI_ChannelName': 'Dev1/ai0', 'NI_UnitDescription': 'Volts'}), ComplexWaveform(scale_mode=LinearScaleMode(2.0, 1.0)), ComplexWaveform(10, ComplexInt32DType, start_index=5, capacity=20), ComplexWaveform.from_array_1d([(0, 0), (0, 0), (1, 1), (2, -2), (3, 33), (4, -44), (5, 50), (0, 0)], ComplexInt32DType, start_index=2, sample_count=5)]`

### `def test___various_values___copy___makes_shallow_copy(value: ComplexWaveform[Any]) -> None`

### `def _assert_shallow_copy(value: ComplexWaveform[Any], other: ComplexWaveform[Any]) -> None`

### `def test___various_values___deepcopy___makes_shallow_copy(value: ComplexWaveform[Any]) -> None`

### `def _assert_deep_copy(value: ComplexWaveform[Any], other: ComplexWaveform[Any]) -> None`

### `def test___various_values___pickle_unpickle___makes_deep_copy(value: ComplexWaveform[Any]) -> None`

### `def test___waveform___pickle___references_public_modules() -> None`

### `def test___pickled_value___unpickle___is_compatible(pickled_value: bytes, expected: ComplexWaveform[Any]) -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/waveform/test_digital_state.py -->
## PYTHON MODULE: tests/unit/waveform/test_digital_state.py

### `def test___state___to_char___returns_char(state: DigitalState, expected_char: str) -> None`

### `def test___invalid_state___to_char___raises_key_error(state: DigitalState) -> None`

### `def test___invalid_state_errors_replace___to_char___returns_question_mark(state: DigitalState) -> None`

### `def test___char___from_char___returns_state(char: str, expected_state: DigitalState) -> None`

### `def test___invalid_char___from_char___raises_key_error(char: str) -> None`

### `def test___states___test___returns_pass_fail(char1: str, char2: str, expected_result: bool) -> None`

### `def test___invalid_state___test___raises_value_error(state1: DigitalState, state2: DigitalState) -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/waveform/test_digital_waveform.py -->
## PYTHON MODULE: tests/unit/waveform/test_digital_waveform.py

### `def test___no_args___create___creates_empty_waveform_with_default_signal_count_and_default_dtype() -> None`

### `def test___sample_count___create___creates_waveform_with_sample_count_default_signal_count_and_default_dtype() -> None`

### `def test___sample_count_signal_count_and_dtype___create___creates_waveform_with_sample_count_and_dtype() -> None`

### `def test___sample_count_and_dtype_str___create___creates_waveform_with_sample_count_and_dtype() -> None`

### `def test___sample_count_and_dtype_any___create___creates_waveform_with_sample_count_and_dtype() -> None`

### `def test___sample_count_dtype_and_capacity___create___creates_waveform_with_sample_count_dtype_and_capacity() -> None`

### `def test___sample_count_and_unsupported_dtype___create___raises_type_error(dtype: npt.DTypeLike) -> None`

### `def test___dtype_str_with_unsupported_tdata_hint___create___mypy_type_var_warning() -> None`

### `def test___dtype_str_with_tdata_hint___create___narrows_tdata() -> None`

### `def test___default_value___create___creates_waveform_with_default_value(default_value: bool | int | DigitalState) -> None`

### `def test___uint8_ndarray___from_lines___creates_waveform_with_uint8_dtype() -> None`

### `def test___bool_ndarray___from_lines___creates_waveform_with_bool_dtype() -> None`

### `def test___int_list_with_int8_dtype___from_lines___creates_waveform_with_int8_dtype() -> None`

### `def test___int_list_1d___from_lines___creates_waveform_with_one_signal() -> None`

### `def test___int_list_2d___from_lines___creates_waveform_with_multi_signal() -> None`

### `def test___ndarray_1d___from_lines___creates_waveform_with_one_signal() -> None`

### `def test___ndarray_2d___from_lines___creates_waveform_with_multi_signal() -> None`

### `def test___uint8_ndarray___from_port_bitorder_little___creates_waveform_with_8_lines() -> None`

### `def test___uint16_ndarray___from_port_bitorder_little___creates_waveform_with_16_lines() -> None`

### `def test___int_list_and_mask___from_port_bitorder_little___creates_waveform_with_masked_lines() -> None`

### `def test___mask___from_port_bitorder_little___creates_waveform_with_masked_lines() -> None`

### `def test___bool_dtype___from_port_bitorder_little___creates_waveform_with_bool_dtype() -> None`

### `def test___array_subset___from_port_bitorder_little___creates_waveform_with_array_subset() -> None`

### `def test___uint8_ndarray___from_port___creates_waveform_with_8_lines() -> None`

### `def test___uint16_ndarray___from_port___creates_waveform_with_16_lines() -> None`

### `def test___int_list_and_mask___from_port___creates_waveform_with_masked_lines() -> None`

### `def test___mask___from_port___creates_waveform_with_masked_lines() -> None`

### `def test___bool_dtype___from_port___creates_waveform_with_bool_dtype() -> None`

### `def test___array_subset___from_port___creates_waveform_with_array_subset() -> None`

### `def test___uint8_ndarray___from_ports_bitorder_little___creates_waveform_with_8_lines() -> None`

### `def test___uint16_ndarray___from_ports_bitorder_little___creates_waveform_with_16_lines() -> None`

### `def test___int_list_and_mask___from_ports_bitorder_little___creates_waveform_with_masked_lines() -> None`

### `def test___masks___from_ports_bitorder_little___creates_waveform_with_masked_lines() -> None`

### `def test___bool_dtype___from_ports_bitorder_little___creates_waveform_with_bool_dtype() -> None`

### `def test___array_subset___from_ports_bitorder_little___creates_waveform_with_array_subset() -> None`

### `def test___uint8_ndarray___from_ports___creates_waveform_with_8_lines() -> None`

### `def test___uint16_ndarray___from_ports___creates_waveform_with_16_lines() -> None`

### `def test___int_list_and_mask___from_ports___creates_waveform_with_masked_lines() -> None`

### `def test___masks___from_ports___creates_waveform_with_masked_lines() -> None`

### `def test___bool_dtype___from_ports___creates_waveform_with_bool_dtype() -> None`

### `def test___array_subset___from_ports___creates_waveform_with_array_subset() -> None`

### `def test___uint8_waveform___data___returns_uint8_data() -> None`

### `def test___uint8_waveform___get_data___returns_data() -> None`

### `def test___array_subset___get_data___returns_array_subset(start_index: int, sample_count: int, expected_data: list[int]) -> None`

### `def test___invalid_array_subset___get_data___returns_array_subset(start_index: int, sample_count: int, expected_message: str, exception_type: type[Exception]) -> None`

### `def test___waveform___set_sample_count___updates_sample_count() -> None`

### `def test___waveform___set_sample_count_to_zero___creates_empty_waveform() -> None`

### `def test___waveform___set_sample_count_exceeds_capacity___raises_value_error() -> None`

### `def test___waveform___set_capacity___resizes_array_and_pads_with_zeros(capacity: int, expected_data: list[int]) -> None`

### `def test___invalid_capacity___set_capacity___raises_correct_error(capacity: int, expected_message: str, exception_type: type[Exception]) -> None`

### `def test___referenced_array___set_capacity___reference_sees_size_change() -> None`

### `def test___array_with_external_buffer___set_capacity___raises_value_error() -> None`

### `def test___waveform___set_channel_name___sets_extended_property() -> None`

### `def test___invalid_type___set_channel_name___raises_type_error() -> None`

### `def test___waveform___set_undefined_property___raises_attribute_error() -> None`

### `def test___waveform___take_weak_ref___references_waveform() -> None`

### `def test___waveform___has_empty_timing() -> None`

### `def test___bintime___waveform_with_timing___static_type_erased() -> None`

### `def test___datetime___waveform_with_timing___static_type_erased() -> None`

### `def test___hightime___waveform_with_timing___static_type_erased() -> None`

### `def test___polymorphic_timing___get_timing_properties___behaves_polymorphically(timing: Timing[Any, Any, Any]) -> None`

### `def test___empty_ndarray___append___no_effect() -> None`

### `def test___uint8_ndarray___append___appends_array() -> None`

### `def test___bool_ndarray___append___appends_array() -> None`

### `def test___ndarray_with_mismatched_dtype___append___raises_correct_error() -> None`

### `def test___ndarray_2d___append___appends_array() -> None`

### `def test___irregular_waveform_and_uint8_ndarray_with_timestamps___append___appends_array() -> None`

### `def test___irregular_waveform_and_uint8_ndarray_without_timestamps___append___raises_timing_mismatch_error_and_does_not_append() -> None`

### `def test___irregular_waveform_and_uint8_ndarray_with_wrong_timestamp_count___append___raises_correct_error_and_does_not_append() -> None`

### `def test___regular_waveform_and_uint8_ndarray_with_timestamps___append___raises_value_error_and_does_not_append() -> None`

### `def test___empty_waveform___append___no_effect() -> None`

### `def test___uint8_waveform___append___appends_waveform() -> None`

### `def test___bool_waveform___append___appends_waveform() -> None`

### `def test___waveform_with_mismatched_dtype___append___raises_correct_error() -> None`

### `def test___irregular_waveform_and_irregular_waveform___append___appends_waveform() -> None`

### `def test___irregular_waveform_and_regular_waveform___append___raises_correct_error() -> None`

### `def test___regular_waveform_and_irregular_waveform___append___raises_correct_error() -> None`

### `def test___regular_waveform_and_regular_waveform_with_different_sample_interval___append___appends_waveform_with_timing_mismatch_warning() -> None`

### `def test___regular_waveform_and_regular_waveform_with_different_extended_properties___append___merges_extended_properties() -> None`

### `def test___empty_waveform_list___append___no_effect() -> None`

### `def test___uint8_waveform_list___append___appends_waveform() -> None`

### `def test___bool_waveform_tuple___append___appends_waveform() -> None`

### `def test___waveform_list_with_mismatched_dtype___append___raises_correct_error_and_does_not_append() -> None`

### `def test___irregular_waveform_and_irregular_waveform_list___append___appends_waveform() -> None`

### `def test___irregular_waveform_and_regular_waveform_list___append___raises_correct_error_and_does_not_append() -> None`

### `def test___regular_waveform_and_irregular_waveform_list___append___raises_correct_error_and_does_not_append() -> None`

### `def test___empty_ndarray___load_data___clears_data() -> None`

### `def test___uint8_ndarray___load_data___overwrites_data() -> None`

### `def test___bool_ndarray___load_data___overwrites_data() -> None`

### `def test___ndarray_with_mismatched_dtype___load_data___raises_correct_error() -> None`

### `def test___ndarray_2d___load_data___overwrites_data() -> None`

### `def test___smaller_ndarray___load_data___preserves_capacity() -> None`

### `def test___larger_ndarray___load_data___grows_capacity() -> None`

### `def test___waveform_with_start_index___load_data___clears_start_index() -> None`

### `def test___ndarray_subset___load_data___overwrites_data() -> None`

### `def test___smaller_ndarray_no_copy___load_data___takes_ownership_of_array() -> None`

### `def test___larger_ndarray_no_copy___load_data___takes_ownership_of_array() -> None`

### `def test___ndarray_subset_no_copy___load_data___takes_ownership_of_array_subset() -> None`

### `def test___irregular_waveform_and_uint8_ndarray_with_timestamps___load_data___overwrites_data_but_not_timestamps() -> None`

### `def test___irregular_waveform_and_uint8_ndarray_with_wrong_sample_count___load_data___raises_correct_error_and_does_not_overwrite_data() -> None`

### `def test___same_value___equality___equal(left: DigitalWaveform[Any], right: DigitalWaveform[Any]) -> None`

### `def test___different_value___equality___not_equal(left: DigitalWaveform[Any], right: DigitalWaveform[Any]) -> None`

### `def test___various_values___repr___looks_ok(value: DigitalWaveform[Any] | Sequence[DigitalWaveform[Any]], expected_repr: str) -> None`

- `_VARIOUS_VALUES = [DigitalWaveform(), DigitalWaveform(10, 2), DigitalWaveform(10, 2, _np_bool), DigitalWaveform(10, 2, np.uint8), DigitalWaveform(10, 2, np.uint8, start_index=5, capacity=20), DigitalWaveform.from_lines([0, 1, 2, 3], _np_bool), DigitalWaveform.from_lines([0, 1, 2, 3], np.uint8), DigitalWaveform(timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))), DigitalWaveform(timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=1))), DigitalWaveform(extended_properties={'NI_ChannelName': 'Dev1/ai0', 'NI_UnitDescription': 'Volts'}), DigitalWaveform(10, 2, np.uint8, start_index=5, capacity=20), DigitalWaveform.from_lines([0, 0, 1, 2, 3, 4, 5, 0], np.uint8, start_index=2, sample_count=5)]`

### `def test___various_values___copy___makes_shallow_copy(value: DigitalWaveform[Any]) -> None`

### `def _assert_on_key_changed_valid(value: DigitalWaveform[Any]) -> None`

### `def _assert_shallow_copy(value: DigitalWaveform[Any], other: DigitalWaveform[Any]) -> None`

### `def test___various_values___deepcopy___makes_deep_copy(value: DigitalWaveform[Any]) -> None`

### `def _assert_deep_copy(value: DigitalWaveform[Any], other: DigitalWaveform[Any]) -> None`

### `def test___various_values___pickle_unpickle___makes_deep_copy(value: DigitalWaveform[Any]) -> None`

### `def test___waveform___pickle___references_public_modules() -> None`

### `def test___pickled_value___unpickle___is_compatible(pickled_value: bytes, expected: DigitalWaveform[Any]) -> None`

### `def test___waveform_with_extended_properties___pickle_unpickle___valid_on_key_changed() -> None`

### `def test___waveform_with_extended_properties___shallow_copy___valid_on_key_changed() -> None`

### `def test___waveform_with_extended_properties___deep_copy___valid_on_key_changed() -> None`

### `def test___same_data___test___returns_success() -> None`

### `def test___different_data___test___reports_failures() -> None`

### `def test___shifted_different_data___test___reports_shifted_failures() -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/waveform/test_digital_waveform_signal.py -->
## PYTHON MODULE: tests/unit/waveform/test_digital_waveform_signal.py

### `def test___waveform___signals___is_signal_collection() -> None`

### `def test___waveform___signals_len___returns_signal_count() -> None`

### `def test___int_index___signals_getitem___returns_signal() -> None`

### `def test___negative_int_index___signals_getitem___returns_signal() -> None`

### `def test___str_index___signals_getitem___returns_signal() -> None`

### `def test___invalid_str_index___signals_getitem___raises_index_error() -> None`

### `def test___slice_index___signals_getitem___returns_signal() -> None`

### `def test___negative_slice_index___signals_getitem___returns_signal() -> None`

### `def test___signal___set_signal_name___sets_name() -> None`

### `def test___signal_with_line_names___get_signal_name___returns_line_name() -> None`

### `def test___signal_with_line_names___set_signal_name___returns_line_name() -> None`

### `def test___signal_with_line_names___change_line_names_property___signal_returns_new_line_name() -> None`

### `def test___pickled_waveform___change_line_names_property___signal_returns_new_line_name() -> None`

### `def test___shallow_copied_waveform___change_line_names_property___signal_returns_new_line_name() -> None`

### `def test___deep_copied_waveform___change_line_names_property___signal_returns_new_line_name() -> None`

### `def test___waveform___get_signal_data___returns_line_data() -> None`

### `def test___waveform___get_data_with_column_index___returns_line_data() -> None`

### `def test___same_value___equality___equal(left: DigitalWaveformSignal[Any], right: DigitalWaveformSignal[Any]) -> None`

### `def test___different_value___equality___not_equal(left: DigitalWaveformSignal[Any], right: DigitalWaveformSignal[Any]) -> None`

### `def test___various_values___repr___looks_ok(value: DigitalWaveformSignal[Any], expected_repr: str) -> None`

- `_VARIOUS_VALUES = [DigitalWaveform(3, 2).signals[0], DigitalWaveform(3, 2, _np_bool).signals[0], DigitalWaveform(3, 2, extended_properties={'NI_LineNames': 'port0/line1, port0/line0'}).signals[1]]`

### `def test___various_values___copy___makes_shallow_copy(value: DigitalWaveformSignal[Any]) -> None`

### `def _assert_shallow_copy(value: DigitalWaveformSignal[Any], other: DigitalWaveformSignal[Any]) -> None`

### `def test___various_values___deepcopy___makes_deep_copy(value: DigitalWaveformSignal[Any]) -> None`

### `def _assert_deep_copy(value: DigitalWaveformSignal[Any], other: DigitalWaveformSignal[Any]) -> None`

### `def test___various_values___pickle_unpickle___makes_deep_copy(value: DigitalWaveformSignal[Any]) -> None`

### `def test___waveform___pickle___references_public_modules() -> None`

### `def test___pickled_value___unpickle___is_compatible(pickled_value: bytes, expected: DigitalWaveformSignal[Any]) -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/waveform/test_extended_property_dictionary.py -->
## PYTHON MODULE: tests/unit/waveform/test_extended_property_dictionary.py

### `def test___pickled_value___unpickle___is_compatible(pickled_value: bytes, expected: ExtendedPropertyDictionary) -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/waveform/test_spectrum.py -->
## PYTHON MODULE: tests/unit/waveform/test_spectrum.py

### `def test___no_args___create___creates_empty_spectrum_with_default_dtype() -> None`

### `def test___sample_count___create___creates_spectrum_with_sample_count_and_default_dtype() -> None`

### `def test___sample_count_and_dtype___create___creates_spectrum_with_sample_count_and_dtype() -> None`

### `def test___sample_count_and_dtype_str___create___creates_spectrum_with_sample_count_and_dtype() -> None`

### `def test___sample_count_and_dtype_any___create___creates_spectrum_with_sample_count_and_dtype() -> None`

### `def test___sample_count_dtype_and_capacity___create___creates_spectrum_with_sample_count_dtype_and_capacity() -> None`

### `def test___sample_count_and_unsupported_dtype___create___raises_type_error(dtype: npt.DTypeLike) -> None`

### `def test___dtype_str_with_unsupported_traw_hint___create___mypy_type_var_warning() -> None`

### `def test___dtype_str_with_traw_hint___create___narrows_traw() -> None`

### `def test___float64_ndarray___from_array_1d___creates_spectrum_with_float64_dtype() -> None`

### `def test___int32_ndarray___from_array_1d___creates_spectrum_with_int32_dtype() -> None`

### `def test___int32_array_with_dtype___from_array_1d___creates_spectrum_with_specified_dtype() -> None`

### `def test___int16_ndarray_with_mismatched_dtype___from_array_1d___creates_spectrum_with_specified_dtype() -> None`

### `def test___int_list_with_dtype___from_array_1d___creates_spectrum_with_specified_dtype() -> None`

### `def test___int_list_with_dtype_str___from_array_1d___creates_spectrum_with_specified_dtype() -> None`

### `def test___int32_ndarray_2d___from_array_1d___raises_value_error() -> None`

### `def test___int_list_without_dtype___from_array_1d___raises_value_error() -> None`

### `def test___bytes___from_array_1d___raises_value_error() -> None`

### `def test___iterable___from_array_1d___raises_type_error() -> None`

### `def test___ndarray_with_unsupported_dtype___from_array_1d___raises_type_error() -> None`

### `def test___copy___from_array_1d___creates_spectrum_linked_to_different_buffer() -> None`

### `def test___int32_ndarray_no_copy___from_array_1d___creates_spectrum_linked_to_same_buffer() -> None`

### `def test___int32_array_no_copy___from_array_1d___creates_spectrum_linked_to_same_buffer() -> None`

### `def test___int_list_no_copy___from_array_1d___raises_value_error() -> None`

### `def test___array_subset___from_array_1d___creates_spectrum_with_array_subset(start_index: SupportsIndex, sample_count: SupportsIndex | None, expected_data: list[int]) -> None`

### `def test___invalid_array_subset___from_array_1d___raises_correct_error(start_index: SupportsIndex, sample_count: SupportsIndex | None, expected_message: str, exception_type: type[Exception]) -> None`

### `def test___float64_ndarray___from_array_2d___creates_spectrum_with_float64_dtype() -> None`

### `def test___int32_ndarray___from_array_2d___creates_spectrum_with_int32_dtype() -> None`

### `def test___int16_ndarray_with_mismatched_dtype___from_array_2d___creates_spectrum_with_specified_dtype() -> None`

### `def test___int32_array_list_with_dtype___from_array_2d___creates_spectrum_with_specified_dtype() -> None`

### `def test___int_list_list_with_dtype___from_array_2d___creates_spectrum_with_specified_dtype() -> None`

### `def test___int_list_list_with_dtype_str___from_array_2d___creates_spectrum_with_specified_dtype() -> None`

### `def test___int32_ndarray_1d___from_array_2d___raises_value_error() -> None`

### `def test___int_list_list_without_dtype___from_array_2d___raises_value_error() -> None`

### `def test___bytes_list___from_array_2d___raises_value_error() -> None`

### `def test___list_iterable___from_array_2d___raises_type_error() -> None`

### `def test___iterable_list___from_array_2d___raises_type_error() -> None`

### `def test___ndarray_with_unsupported_dtype___from_array_2d___raises_type_error() -> None`

### `def test___copy___from_array_2d___creates_spectrum_linked_to_different_buffer() -> None`

### `def test___int32_ndarray_no_copy___from_array_2d___creates_spectrum_linked_to_same_buffer() -> None`

### `def test___int32_array_list_no_copy___from_array_2d___creates_spectrum_linked_to_same_buffer() -> None`

### `def test___int_list_list_no_copy___from_array_2d___raises_value_error() -> None`

### `def test___array_subset___from_array_2d___creates_spectrum_with_array_subset(start_index: SupportsIndex, sample_count: SupportsIndex | None, expected_data: list[list[int]]) -> None`

### `def test___invalid_array_subset___from_array_2d___raises_correct_error(start_index: SupportsIndex, sample_count: SupportsIndex | None, expected_message: str, exception_type: type[Exception]) -> None`

### `def test___int32_spectrum___data___returns_int32_data() -> None`

### `def test___int32_spectrum___get_data___returns_data() -> None`

### `def test___array_subset___get_data___returns_array_subset(start_index: int, sample_count: int, expected_data: list[int]) -> None`

### `def test___invalid_array_subset___get_data___returns_array_subset(start_index: int, sample_count: int, expected_message: str) -> None`

### `def test___spectrum___set_capacity___resizes_array_and_pads_with_zeros(capacity: int, expected_data: list[int]) -> None`

### `def test___invalid_capacity___set_capacity___raises_correct_error(capacity: int, expected_message: str, exception_type: type[Exception]) -> None`

### `def test___referenced_array___set_capacity___reference_sees_size_change() -> None`

### `def test___array_with_external_buffer___set_capacity___raises_value_error() -> None`

### `def test___spectrum___set_channel_name___sets_extended_property() -> None`

### `def test___invalid_type___set_channel_name___raises_type_error() -> None`

### `def test___spectrum___set_units___sets_extended_property() -> None`

### `def test___invalid_type___set_units___raises_type_error() -> None`

### `def test___spectrum___set_undefined_property___raises_attribute_error() -> None`

### `def test___spectrum___take_weak_ref___references_spectrum() -> None`

### `def test___spectrum___has_default_frequency_range() -> None`

### `def test___spectrum_with_frequencies___has_specified_frequency_range() -> None`

### `def test___spectrum_with_frequencies___set_frequencies___has_set_frequency_range() -> None`

### `def test___empty_ndarray___append___no_effect() -> None`

### `def test___int32_ndarray___append___appends_array() -> None`

### `def test___float64_ndarray___append___appends_array() -> None`

### `def test___ndarray_with_mismatched_dtype___append___raises_correct_error() -> None`

### `def test___ndarray_2d___append___raises_value_error() -> None`

### `def test___empty_spectrum___append___no_effect() -> None`

### `def test___int32_spectrum___append___appends_spectrum() -> None`

### `def test___float64_spectrum___append___appends_spectrum() -> None`

### `def test___spectrum_with_mismatched_dtype___append___raises_correct_error() -> None`

### `def test___empty_spectrum_list___append___no_effect() -> None`

### `def test___int32_spectrum_list___append___appends_spectrum() -> None`

### `def test___float64_spectrum_tuple___append___appends_spectrum() -> None`

### `def test___spectrum_list_with_mismatched_dtype___append___raises_correct_error_and_does_not_append() -> None`

### `def test___empty_ndarray___load_data___clears_data() -> None`

### `def test___int32_ndarray___load_data___overwrites_data() -> None`

### `def test___float64_ndarray___load_data___overwrites_data() -> None`

### `def test___ndarray_with_mismatched_dtype___load_data___raises_correct_error() -> None`

### `def test___ndarray_2d___load_data___raises_value_error() -> None`

### `def test___smaller_ndarray___load_data___preserves_capacity() -> None`

### `def test___larger_ndarray___load_data___grows_capacity() -> None`

### `def test___spectrum_with_start_index___load_data___clears_start_index() -> None`

### `def test___ndarray_subset___load_data___overwrites_data() -> None`

### `def test___smaller_ndarray_no_copy___load_data___takes_ownership_of_array() -> None`

### `def test___larger_ndarray_no_copy___load_data___takes_ownership_of_array() -> None`

### `def test___ndarray_subset_no_copy___load_data___takes_ownership_of_array_subset() -> None`

### `def test___same_value___equality___equal(left: Spectrum[Any], right: Spectrum[Any]) -> None`

### `def test___different_value___equality___not_equal(left: Spectrum[Any], right: Spectrum[Any]) -> None`

### `def test___various_values___repr___looks_ok(value: Spectrum[Any], expected_repr: str) -> None`

- `_VARIOUS_VALUES = [Spectrum(), Spectrum(10), Spectrum(10, np.float64), Spectrum(10, np.int32), Spectrum(10, np.int32, start_index=5, capacity=20), Spectrum.from_array_1d([1, 2, 3], np.float64), Spectrum.from_array_1d([1, 2, 3], np.int32), Spectrum(start_frequency=123.456, frequency_increment=0.1), Spectrum(extended_properties={'NI_ChannelName': 'Dev1/ai0', 'NI_UnitDescription': 'Volts'}), Spectrum(10, np.int32, start_index=5, capacity=20), Spectrum.from_array_1d([0, 0, 1, 2, 3, 4, 5, 0], np.int32, start_index=2, sample_count=5)]`

### `def test___various_values___copy___makes_shallow_copy(value: Spectrum[Any]) -> None`

### `def _assert_shallow_copy(value: Spectrum[Any], other: Spectrum[Any]) -> None`

### `def test___various_values___deepcopy___makes_shallow_copy(value: Spectrum[Any]) -> None`

### `def _assert_deep_copy(value: Spectrum[Any], other: Spectrum[Any]) -> None`

### `def test___various_values___pickle_unpickle___makes_deep_copy(value: Spectrum[Any]) -> None`

### `def test___spectrum___pickle___references_public_modules() -> None`

### `def test___pickled_value___unpickle___is_compatible(pickled_value: bytes, expected: Spectrum[Any]) -> None`

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/xy_data/__init__.py -->
## PYTHON MODULE: tests/unit/xy_data/__init__.py

### MODULE DOCSTRING

Unit tests for the nitypes.xy_data package.

<!--NI_PYTHON_API repo=nitypes-python path=tests/unit/xy_data/test_xy_data.py -->
## PYTHON MODULE: tests/unit/xy_data/test_xy_data.py

### `def test___data_and_dtype___create___creates_xydata_with_data_dtype_and_default_units() -> None`

### `def test___data_dtype_and_units___create___creates_xydata_with_data_dtype_and_units() -> None`

### `def test___both_x_units_specified_unequal__create___raises_value_error() -> None`

### `def test___both_y_units_specified_unequal__create___raises_value_error() -> None`

### `def test___x_units_only_specified_in_extended_properties__create___creates_with_units() -> None`

### `def test___y_units_only_specified_in_extended_properties__create___creates_with_units() -> None`

### `def test___mismatched_dtypes___create___raises_type_error() -> None`

### `def test___unsupported_dtype___create___raises_type_error(data: np.ndarray) -> None`

### `def test___float64_ndarray___from_arrays_1d___creates_xydata_with_float64_dtype() -> None`

### `def test___float64_ndarray_with_units___from_arrays_1d___creates_xydata_with_float64_dtype_and_units() -> None`

### `def test___int32_ndarray___from_arrays_1d___creates_xydata_with_int32_dtype() -> None`

### `def test___int32_array_with_dtype___from_arrays_1d___creates_xydata_with_specified_dtype() -> None`

### `def test___int16_ndarray_with_mismatched_dtype___from_arrays_1d___creates_xydata_with_specified_dtype() -> None`

### `def test___int_list_with_dtype___from_arrays_1d___creates_xydata_with_specified_dtype() -> None`

### `def test___int_list_with_dtype_str___from_arrays_1d___creates_xydata_with_specified_dtype() -> None`

### `def test___int32_ndarray_2d___from_arrays_1d___raises_value_error() -> None`

### `def test___int_list_without_dtype___from_arrays_1d___raises_value_error() -> None`

### `def test___bytes___from_arrays_1d___raises_value_error() -> None`

### `def test___iterable___from_arrays_1d___raises_type_error() -> None`

### `def test___ndarray_with_unsupported_dtype___from_arrays_1d___raises_type_error() -> None`

### `def test___copy___from_arrays_1d___creates_xydata_linked_to_different_buffer() -> None`

### `def test___int32_ndarray_no_copy___from_arrays_1d___creates_xydata_linked_to_same_buffer() -> None`

### `def test___int_list_no_copy___from_arrays_1d___raises_value_error() -> None`

### `def test___same_value___comparison___equal(left: XYData[TData], right: XYData[TData]) -> None`

### `def test___different_values___comparison___not_equal(left: XYData[TData], right: XYData[TData]) -> None`

### `def test___different_units___comparison___not_equal() -> None`

### `def test___various_values___repr___looks_ok(value: XYData[Any], expected_repr: str) -> None`

### `def test___various_values___str___looks_ok(value: XYData[Any], expected_str: str) -> None`

### `def test___xy_data_with_units___get_extended_properties___returns_correct_dictionary() -> None`

### `def test___xy_data_with_units___set_units___units_updated_correctly() -> None`

### `def test___various_values___copy___makes_copy(value: XYData[TData]) -> None`

### `def test___various_values___pickle_unpickle___makes_copy(value: XYData[TData]) -> None`

### `def test___xy_data___pickle___references_public_modules() -> None`

### `def test___pickled_value___unpickle___is_compatible(pickled_value: bytes, expected: XYData[Any]) -> None`

### `def test___various_units_values___change_units___updates_units_correctly() -> None`
