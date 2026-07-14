# NI PYTHON API DIGEST: hightime

<!--NI_PYTHON_API_SNAPSHOT repo=ni/hightime commit=f84fccc31ab546a66c605990c739036bf89d42a3 -->

<!--NI_PYTHON_API repo=hightime path=docs/conf.py -->
## PYTHON MODULE: docs/conf.py

### MODULE DOCSTRING

Sphinx Configuration File.

### `def skip_aliases(app, what, name, obj, skip, options)`

Skip documentation for classes that are exported from multiple modules.

### `def setup(sphinx)`

Sphinx setup callback.

<!--NI_PYTHON_API repo=hightime path=hightime/__init__.py -->
## PYTHON MODULE: hightime/__init__.py

### MODULE DOCSTRING

This package extends the built-in datetime types to support sub-microsecond values.

The classes defined in this package are:

* :any:`hightime.datetime`: A subclass of :any:`datetime.datetime` with sub-microsecond
  capabilities.

* :any:`hightime.timedelta`: A subclass of :any:`datetime.timedelta` with sub-microsecond
  capabilities.

.. note::
   Due to floating point arithmetic inaccuracies, the ability to specify
   sub-microsecond values in terms of much larger units (weeks, days, seconds) has been
   limited. For the exact limitations, please consult the source code.


- `__all__ = ['datetime', 'timedelta']`

<!--NI_PYTHON_API repo=hightime path=hightime/_datetime.py -->
## PYTHON MODULE: hightime/_datetime.py

### `def _check_arg(name, value)`

### `class datetime(std_datetime.datetime)`

A datetime represents a point in time.

    This class extends :any:`datetime.datetime` to support up to yoctosecond precision.

    The constructor takes the same arguments as :any:`datetime.datetime`, with the addition of
    ``femtosecond`` and ``yoctosecond``.

    >>> new_years = datetime(year=1999, month=12, day=31, hour=23, minute=59, second=59,
    ... microsecond=999999, femtosecond=999999999, yoctosecond=999999999)
    >>> new_years
    hightime.datetime(1999, 12, 31, 23, 59, 59, 999999, 999999999, 999999999)
    >>> new_years + timedelta(yoctoseconds=1)
    hightime.datetime(2000, 1, 1, 0, 0)
    

#### `def _new_impl(cls, year, month=None, day=None, hour=0, minute=0, second=0, microsecond=0, femtosecond=0, yoctosecond=0, tzinfo=None, *, fold=0)`

#### `def __new__(cls, *args, **kwargs)`

Construct a datetime.

#### `def femtosecond(self)`

femtosecond (0-999999999)

#### `def yoctosecond(self)`

yoctosecond (0-999999999)

#### `def fromtimestamp(cls, t, tz=None)`

Return a datetime corresponding to a POSIX timestamp with the provided time zone.

        .. warning::
            This method does not support sub-microsecond values.
        

#### `def utcfromtimestamp(cls, t)`

Return a datetime corresponding to a POSIX timestamp in UTC.

        .. warning::
            This method does not support sub-microsecond values.
        

#### `def astimezone(self, tz=None)`

Return a copy of self converted to the specified time zone.

#### `def isoformat(self, sep='T', timespec='auto')`

Return a string representing the time in ISO 8601 format.

#### `def replace(self, year=None, month=None, day=None, hour=None, minute=None, second=None, microsecond=None, femtosecond=None, yoctosecond=None, tzinfo=True, *, fold=None)`

Return a copy of self with the specified fields replaced with the provided values.

#### `def __repr__(self)`

Return repr(self).

#### `def __eq__(self, other)`

Return self==other.

#### `def __ne__(self, other)`

Return self!=other.

#### `def __lt__(self, other)`

Return self<other.

#### `def __le__(self, other)`

Return self<=other.

#### `def __gt__(self, other)`

Return self>other.

#### `def __ge__(self, other)`

Return self>=other.

#### `def __add__(self, other)`

Return self+other.

#### `def __sub__(self, other)`

Return self-other.

#### `def __hash__(self)`

Return hash(self).

#### `def _hightime_getstate(self, protocol=3)`

#### `def __reduce_ex__(self, protocol)`

Return object state for pickling.

#### `def __reduce__(self)`

Return object state for pickling.

#### `def _cmp(self, other)`

#### `def _from_base(cls, base_datetime)`

<!--NI_PYTHON_API repo=hightime path=hightime/_timedelta.py -->
## PYTHON MODULE: hightime/_timedelta.py

- `_YS_PER_S = 10 ** 24`

- `_YS_PER_US = 10 ** 18`

- `_YS_PER_FS = 10 ** 9`

- `_YS_PER_DAY = 60 * 60 * 24 * _YS_PER_S`

- `_US_PER_DAY = 24 * 60 * 60 * 1000 * 1000`

- `_US_PER_WEEK = 7 * _US_PER_DAY`

- `_NS_PER_HOUR = 60 * 60 * 10 ** 9`

- `_PS_PER_MINUTE = 60 * 10 ** 12`

- `_FIELD_NAMES = ['days', 'seconds', 'microseconds', 'femtoseconds', 'yoctoseconds']`

### `def _divide_and_round(a, b)`

### `def _cmp(x, y)`

### `class timedelta(std_datetime.timedelta)`

A timedelta represents a duration.

    This class extends :any:`datetime.timedelta` to support up to yoctosecond precision.

    The constructor takes the same arguments as :any:`datetime.timedelta`, with the addition of
    ``nanoseconds``, ``picoseconds``, ``femtoseconds``, ``attoseconds``, ``zeptoseconds``, and
    ``yoctoseconds``.

    >>> timedelta(days=1, seconds=2, microseconds=3,  # doctest: +NORMALIZE_WHITESPACE
    ... milliseconds=4, minutes=5, hours=6, weeks=7, nanoseconds=8, picoseconds=9, femtoseconds=10,
    ... attoseconds=11, zeptoseconds=12, yoctoseconds=13)
    hightime.timedelta(days=50, seconds=21902, microseconds=4003, femtoseconds=8009010,
    yoctoseconds=11012013)
    >>> timedelta(picoseconds=1e12)
    hightime.timedelta(seconds=1)

    .. note::
       Performing math operations with floating point may reduce the precision of the result.

    For example, multiplying or dividing by the number of yoctoseconds in a second has the correct
    result when it is expressed as an integer, and the wrong result when it is expressed as a float:

    >>> timedelta(yoctoseconds=1) * 10**24
    hightime.timedelta(seconds=1)
    >>> timedelta(yoctoseconds=1) * 1e24
    hightime.timedelta(microseconds=999999, femtoseconds=999999999, yoctoseconds=983222784)
    >>> timedelta(seconds=1) // 10**24
    hightime.timedelta(yoctoseconds=1)
    >>> timedelta(seconds=1) / 1e24
    hightime.timedelta()

    Likewise, you can specify larger units as a float with a sub-microsecond value, but this may
    reduce the precision of the result:

    >>> timedelta(seconds=1e-15)
    hightime.timedelta(femtoseconds=1)
    >>> timedelta(seconds=1e-24)   # expected hightime.timedelta(yoctoseconds=1)
    hightime.timedelta()
    

#### `def __new__(cls, days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0, nanoseconds=0, picoseconds=0, femtoseconds=0, attoseconds=0, zeptoseconds=0, yoctoseconds=0)`

Construct a timedelta object.

#### `def femtoseconds(self)`

femtoseconds

#### `def yoctoseconds(self)`

yoctoseconds

#### `def total_seconds(self)`

Total seconds in the duration.

#### `def precision_total_seconds(self)`

Precise total seconds in the duration.

        .. note::
            Up to 64 significant digits are used in computation.
        

#### `def __repr__(self)`

Return repr(self).

#### `def __str__(self)`

Return str(self).

#### `def __eq__(self, other)`

Return self==other.

#### `def __ne__(self, other)`

Return self!=other.

#### `def __lt__(self, other)`

Return self<other.

#### `def __le__(self, other)`

Return self<=other.

#### `def __gt__(self, other)`

Return self>other.

#### `def __ge__(self, other)`

Return self>=other.

#### `def __bool__(self)`

Return bool(self).

#### `def __pos__(self)`

Return +self.

#### `def __abs__(self)`

Return abs(self).

#### `def __add__(self, other)`

Return self+other.

#### `def __sub__(self, other)`

Return self-other.

#### `def __neg__(self)`

Return -self.

#### `def __mul__(self, other)`

Return self*other.

#### `def __floordiv__(self, other)`

Return self//other.

#### `def __truediv__(self, other)`

Return self/other.

#### `def __mod__(self, other)`

Return self%other.

#### `def __divmod__(self, other)`

Return divmod(self, other).

#### `def __hash__(self)`

Return hash(self).

#### `def _getstate(self)`

#### `def __reduce__(self)`

Return object state for pickling.

#### `def _as_ys(cls, td)`

#### `def _as_tuple(cls, td)`

#### `def _cmp(self, other)`

<!--NI_PYTHON_API repo=hightime path=tests/__init__.py -->
## PYTHON MODULE: tests/__init__.py

### MODULE DOCSTRING

Tests for the hightime package.

<!--NI_PYTHON_API repo=hightime path=tests/othertime.py -->
## PYTHON MODULE: tests/othertime.py

### MODULE DOCSTRING

Another set of time types for testing operators.

### `class OtherDateTime()`

Another datetime class that supports comparisons with hightime.datetime.

#### `def __init__(self, timestamp: float) -> None`

Initialize the OtherDateTime.

#### `def __eq__(self, value: object, /) -> bool`

Return self==value.

#### `def __lt__(self, value: OtherDateTime | datetime.datetime | hightime.datetime, /) -> bool`

Return self<value.

#### `def __repr__(self) -> str`

Return repr(self).

### `class OtherTimeDelta()`

Another timedelta class that supports comparisons with hightime.timedelta.

#### `def __init__(self, seconds: float) -> None`

Initialize the OtherTimeDelta.

#### `def __eq__(self, value: object, /) -> bool`

Return self==value.

#### `def __lt__(self, value: OtherTimeDelta | datetime.timedelta | hightime.timedelta, /) -> bool`

Return self<value.

#### `def __repr__(self) -> str`

Return repr(self).

<!--NI_PYTHON_API repo=hightime path=tests/shorthands.py -->
## PYTHON MODULE: tests/shorthands.py

### MODULE DOCSTRING

Constructor wrappers that support shorthands for keyword arguments.

- `_UNIT_SHORTHANDS = {'y': 'year', 'mo': 'month', 'w': 'week', 'd': 'day', 'h': 'hour', 'm': 'minute', 's': 'second', 'ms': 'millisecond', 'us': 'microsecond', 'ns': 'nanosecond', 'ps': 'picosecond', 'fs': 'femtosecond', 'as_': 'attosecond', 'zs': 'zeptosecond', 'ys': 'yoctosecond'}`

### `def _replace(kwargs: dict[str, Any], *, plural: bool) -> dict[str, Any]`

### `def datetime(*args: Any, **kwargs: Any) -> hightime.datetime`

Instantiate a hightime.datetime with some shorthands.

    Allows unit shorthand kwargs as well as passing year/month/day if none are provided.
    

### `def timedelta(*args: Any, **kwargs: Any) -> hightime.timedelta`

Instantiate a hightime.timedelta, allowing unit shorthand kwargs.

<!--NI_PYTHON_API repo=hightime path=tests/test_datetime.py -->
## PYTHON MODULE: tests/test_datetime.py

- `_SUBMICROSECOND_FIELDS = ['femtosecond', 'yoctosecond']`

- `_ALL_FIELDS = ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond'] + _SUBMICROSECOND_FIELDS`

### `class IntLike(object)`

An object that supports conversion to int.

#### `def __init__(self, value: int=1)`

Initialize the IntLike object.

#### `def __index__(self) -> int`

Return self converted to an integer.

### `def tzinfo(*, hours: int) -> std_datetime.timezone`

### `def test_datetime_isinstance() -> None`

### `def test_datetime_arg_wrong_type(argname: str, argvalue: float | int | SupportsIndex) -> None`

### `def test_datetime_arg_wrong_value(argname: str, smallest: int, biggest: int, argtype: Type) -> None`

### `def test_datetime_tzinfo_as_femtoseconds() -> None`

### `def test_datetime_properties() -> None`

### `def test_datetime_repr(dt: hightime.datetime, middle_part: str) -> None`

### `def test_datetime_isoformat(dt: hightime.datetime, expected: str, expected_tz: str) -> None`

### `def test_datetime_str(dt: hightime.datetime, expected: str) -> None`

### `def test_datetime_comparison(left: hightime.datetime, right: hightime.datetime, eq: bool, lt: bool) -> None`

### `def test_datetime_comparison_tzinfo_mismatch() -> None`

### `def test_datetime_comparison_unrelated_type(dt: hightime.datetime, other: Any) -> None`

### `def test_datetime_comparison_compatible_type(left: hightime.datetime | OtherDateTime, right: hightime.datetime | OtherDateTime, eq: bool, lt: bool) -> None`

### `def test_datetime_add(left: hightime.datetime, right: hightime.timedelta, expected: hightime.datetime) -> None`

### `def test_datetime_sub(left: hightime.datetime, right: hightime.datetime, expected: hightime.timedelta) -> None`

### `def test_datetime_hash() -> None`

### `def test_datetime_strptime_type() -> None`

### `def test_datetime_tzname() -> None`

### `def test_datetime_dst() -> None`

### `def test_datetime_utcoffset() -> None`

### `def test_datetime_ctime() -> None`

### `def test_datetime_combine_type() -> None`

### `def test_datetime_utcnow_type() -> None`

### `def test_datetime_now_type() -> None`

### `def test_datetime_fromtimestamp_type() -> None`

### `def test_datetime_utcfromtimestamp_type() -> None`

### `def test_datetime_astimezone_type() -> None`

### `def test_datetime_replace() -> None`

### `def test_datetime_timestamp(dt: hightime.datetime, expected: object) -> None`

### `def test_datetime_sub_total_seconds_precision(left: hightime.datetime, right: hightime.datetime, expected: Decimal) -> None`

### `def test_datetime_copy(dt: hightime.datetime) -> None`

### `def test_datetime_pickle(dt: hightime.datetime) -> None`

### `def test_datetime_pickle_uses_public_package_name() -> None`

<!--NI_PYTHON_API repo=hightime path=tests/test_timedelta.py -->
## PYTHON MODULE: tests/test_timedelta.py

### `def test_timedelta_constuctor(left: hightime.timedelta, right: hightime.timedelta) -> None`

### `def test_timedelta_properties() -> None`

### `def test_timedelta_total_seconds(td: hightime.timedelta, expected: float) -> None`

### `def test_timedelta_precision_total_seconds(td: hightime.timedelta, expected: float) -> None`

### `def test_timedelta_repr(td: hightime.timedelta, middle_part: str) -> None`

### `def test_timedelta_str(td: hightime.timedelta, expected: str) -> None`

### `def test_timedelta_comparison(left: hightime.timedelta, right: hightime.timedelta, eq: bool, lt: bool) -> None`

### `def test_timedelta_comparison_unrelated_type(td: hightime.timedelta, other: Any) -> None`

### `def test_timedelta_comparison_compatible_type(left: hightime.timedelta | OtherTimeDelta, right: hightime.timedelta | OtherTimeDelta, eq: bool, lt: bool) -> None`

### `def test_timedelta_bool() -> None`

### `def test_timedelta_add(left: hightime.timedelta, right: hightime.timedelta, expected: hightime.timedelta) -> None`

### `def test_timedelta_add_integrals() -> None`

### `def test_timedelta_sub(left: hightime.timedelta, right: hightime.timedelta, expected: hightime.timedelta) -> None`

### `def test_timedelta_sub_integrals() -> None`

### `def test_timedelta_mul(left: hightime.timedelta, right: float, expected: hightime.timedelta) -> None`

### `def test_timedelta_mul_nan() -> None`

### `def test_timedelta_floordiv(left: hightime.timedelta, right: int | hightime.timedelta, expected: hightime.timedelta | int) -> None`

### `def test_timedelta_floordiv_unrelated_type() -> None`

### `def test_timedelta_floordiv_dividebyzero() -> None`

### `def test_timedelta_truediv(left: hightime.timedelta, right: float | datetime.timedelta, expected: float | hightime.timedelta) -> None`

### `def test_timedelta_truediv_unrelated_type() -> None`

### `def test_timedelta_truediv_dividebyzero() -> None`

### `def test_timedelta_mod(left: hightime.timedelta, right: hightime.timedelta, expected: hightime.timedelta) -> None`

### `def test_timedelta_mod_dividebyzero() -> None`

### `def test_timedelta_divmod(left: hightime.timedelta, right: hightime.timedelta, expected_q: int, expected_r: hightime.timedelta) -> None`

### `def test_timedelta_divmod_unrelated_type() -> None`

### `def test_timedelta_divmod_dividebyzero() -> None`

### `def test_stddatetime_leftside_arithmetic() -> None`

### `def test_timedelta_unary_arithmetic() -> None`

### `def test_timedelta_abs() -> None`

### `def test_timedelta_resolution() -> None`

### `def test_timedelta_hash() -> None`

### `def test_timedelta_copy(td: hightime.timedelta) -> None`

### `def test_timedelta_pickle(td: hightime.timedelta) -> None`

### `def test_timedelta_pickle_uses_public_package_name() -> None`
