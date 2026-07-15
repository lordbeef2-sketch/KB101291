# NI OSS SOURCE SNAPSHOT: nitypes-python

<!--NI_OSS_SNAPSHOT repo=ni/nitypes-python commit=2744270de1437c671fecc48b9f8ebc17a8343cda -->

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/waveform/_scaling/test_linear.py sha256=7af71912930364de99c21ddbae9c238eb5c1c4e46f0aa8d11180a10259dfaa03 bytes=5915 -->
## FILE: tests/unit/waveform/_scaling/test_linear.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/waveform/_scaling/test_linear.py`
- sha256: `7af71912930364de99c21ddbae9c238eb5c1c4e46f0aa8d11180a10259dfaa03`
- bytes: 5915

````python
from __future__ import annotations

import copy
import pickle
from typing import SupportsFloat

import numpy as np
import numpy.typing as npt
import pytest
from typing_extensions import assert_type

from nitypes.waveform import NO_SCALING, LinearScaleMode, ScaleMode


@pytest.mark.parametrize(
    "gain, offset",
    [
        (1.0, 0.0),
        (1.2345, 0.006789),
        (3, 4),
        (np.float64(1.2345), np.float64(0.006789)),
        # np.float32 is not a subclass of float, but it supports __float__.
        (np.float32(1.2345), np.float32(0.006789)),
    ],
)
def test___gain_and_offset___construct___constructs_with_gain_and_offset(
    gain: SupportsFloat, offset: SupportsFloat
) -> None:
    scale_mode = LinearScaleMode(gain, offset)

    assert scale_mode.gain == gain
    assert scale_mode.offset == offset


@pytest.mark.parametrize(
    "gain, offset, expected_message",
    [
        (None, 0.0, "The gain must be a floating point number."),
        ("1.0", 0.0, "The gain must be a floating point number."),
        (1.0, "0.0", "The offset must be a floating point number."),
    ],
)
def test__invalid_gain_or_offset___construct___raises_type_error(
    gain: object, offset: object, expected_message: str
) -> None:
    with pytest.raises(TypeError) as exc:
        _ = LinearScaleMode(gain, offset)  # type: ignore[arg-type]

    assert exc.value.args[0].startswith(expected_message)


def test___empty_ndarray___transform_data___returns_empty_scaled_data() -> None:
    waveform = np.zeros(0, np.float64)
    scale_mode = LinearScaleMode(3.0, 4.0)

    scaled_data = scale_mode._transform_data(waveform)

    assert_type(scaled_data, npt.NDArray[np.float64])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.float64
    assert list(scaled_data) == []


def test___float32_ndarray___transform_data___returns_float32_scaled_data() -> None:
    raw_data = np.array([0, 1, 2, 3], np.float32)
    scale_mode = LinearScaleMode(3.0, 4.0)

    scaled_data = scale_mode._transform_data(raw_data)

    assert_type(scaled_data, npt.NDArray[np.float32])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.float32
    assert list(scaled_data) == [4.0, 7.0, 10.0, 13.0]


def test___float64_ndarray___transform_data___returns_float64_scaled_data() -> None:
    raw_data = np.array([0, 1, 2, 3], np.float64)
    scale_mode = LinearScaleMode(3.0, 4.0)

    scaled_data = scale_mode._transform_data(raw_data)

    assert_type(scaled_data, npt.NDArray[np.float64])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.float64
    assert list(scaled_data) == [4.0, 7.0, 10.0, 13.0]


def test___complex64_ndarray___transform_data___returns_complex64_scaled_data() -> None:
    raw_data = np.array([1 + 2j, 3 - 4j], np.complex64)
    scale_mode = LinearScaleMode(3.0, 4.0)

    scaled_data = scale_mode._transform_data(raw_data)

    assert_type(scaled_data, npt.NDArray[np.complex64])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.complex64
    assert list(scaled_data) == [7 + 6j, 13 - 12j]


def test___complex128_ndarray___transform_data___returns_complex128_scaled_data() -> None:
    raw_data = np.array([1 + 2j, 3 - 4j], np.complex128)
    scale_mode = LinearScaleMode(3.0, 4.0)

    scaled_data = scale_mode._transform_data(raw_data)

    assert_type(scaled_data, npt.NDArray[np.complex128])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.complex128
    assert list(scaled_data) == [7 + 6j, 13 - 12j]


@pytest.mark.parametrize(
    "left, right",
    [
        (LinearScaleMode(1.0, 0.0), LinearScaleMode(1.0, 0.0)),
        (LinearScaleMode(1.2345, 0.006789), LinearScaleMode(1.2345, 0.006789)),
    ],
)
def test___same_value___equality___equal(left: LinearScaleMode, right: LinearScaleMode) -> None:
    assert left == right
    assert not (left != right)


@pytest.mark.parametrize(
    "left, right",
    [
        (LinearScaleMode(1.0, 0.0), LinearScaleMode(1.0, 0.1)),
        (LinearScaleMode(1.0, 0.0), LinearScaleMode(1.1, 0.0)),
        (LinearScaleMode(1.2345, 0.006789), LinearScaleMode(1.23456, 0.006789)),
        (LinearScaleMode(1.2345, 0.006789), LinearScaleMode(1.2345, 0.00678)),
        (LinearScaleMode(1.0, 0.0), NO_SCALING),
        (NO_SCALING, LinearScaleMode(1.0, 0.0)),
    ],
)
def test___different_value___equality___not_equal(left: ScaleMode, right: ScaleMode) -> None:
    assert not (left == right)
    assert left != right


def test___scale_mode___repr___looks_ok() -> None:
    scale_mode = LinearScaleMode(1.2345, 0.006789)

    assert repr(scale_mode) == "nitypes.waveform.LinearScaleMode(1.2345, 0.006789)"


def test___scale_mode___copy___makes_shallow_copy() -> None:
    scale_mode = LinearScaleMode(1.2345, 0.006789)

    new_scale_mode = copy.copy(scale_mode)

    assert new_scale_mode == scale_mode
    assert new_scale_mode is not scale_mode


def test___scale_mode___deepcopy___makes_deep_copy() -> None:
    scale_mode = LinearScaleMode(1.2345, 0.006789)

    new_scale_mode = copy.deepcopy(scale_mode)

    assert new_scale_mode == scale_mode
    assert new_scale_mode is not scale_mode


def test___scale_mode___pickle_unpickle___makes_deep_copy() -> None:
    scale_mode = LinearScaleMode(1.2345, 0.006789)

    new_scale_mode = pickle.loads(pickle.dumps(scale_mode))

    assert new_scale_mode == scale_mode
    assert new_scale_mode is not scale_mode


def test___scale_mode___pickle___references_public_modules() -> None:
    scale_mode = LinearScaleMode(1.2345, 0.006789)

    scale_mode_bytes = pickle.dumps(scale_mode)

    assert b"nitypes.waveform" in scale_mode_bytes
    assert b"nitypes.waveform._scaling" not in scale_mode_bytes
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/waveform/_scaling/test_none.py sha256=5d3095b554702a0760606b08251d0908258deab85e56ff3aa55cdc22e6c85882 bytes=3327 -->
## FILE: tests/unit/waveform/_scaling/test_none.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/waveform/_scaling/test_none.py`
- sha256: `5d3095b554702a0760606b08251d0908258deab85e56ff3aa55cdc22e6c85882`
- bytes: 3327

````python
from __future__ import annotations

import copy
import pickle

import numpy as np
import numpy.typing as npt
from typing_extensions import assert_type

from nitypes.waveform import NO_SCALING, NoneScaleMode


def test___no_scaling___type_is_none_scale_mode() -> None:
    assert_type(NO_SCALING, NoneScaleMode)
    assert isinstance(NO_SCALING, NoneScaleMode)


def test___empty_ndarray___transform_data___returns_empty_scaled_data() -> None:
    waveform = np.zeros(0, np.float64)

    scaled_data = NO_SCALING._transform_data(waveform)

    assert_type(scaled_data, npt.NDArray[np.float64])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.float64
    assert list(scaled_data) == []


def test___float32_ndarray___transform_data___returns_float32_scaled_data() -> None:
    raw_data = np.array([0, 1, 2, 3], np.float32)

    scaled_data = NO_SCALING._transform_data(raw_data)

    assert_type(scaled_data, npt.NDArray[np.float32])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.float32
    assert list(scaled_data) == [0.0, 1.0, 2.0, 3.0]


def test___float64_ndarray___transform_data___returns_float64_scaled_data() -> None:
    raw_data = np.array([0, 1, 2, 3], np.float64)

    scaled_data = NO_SCALING._transform_data(raw_data)

    assert_type(scaled_data, npt.NDArray[np.float64])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.float64
    assert list(scaled_data) == [0.0, 1.0, 2.0, 3.0]


def test___complex64_ndarray___transform_data___returns_complex64_scaled_data() -> None:
    raw_data = np.array([1 + 2j, 3 - 4j], np.complex64)

    scaled_data = NO_SCALING._transform_data(raw_data)

    assert_type(scaled_data, npt.NDArray[np.complex64])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.complex64
    assert list(scaled_data) == [1 + 2j, 3 - 4j]


def test___complex128_ndarray___transform_data___returns_complex128_scaled_data() -> None:
    raw_data = np.array([1 + 2j, 3 - 4j], np.complex128)

    scaled_data = NO_SCALING._transform_data(raw_data)

    assert_type(scaled_data, npt.NDArray[np.complex128])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.complex128
    assert list(scaled_data) == [1 + 2j, 3 - 4j]


def test___scale_mode___repr___looks_ok() -> None:
    assert repr(NO_SCALING) == "nitypes.waveform.NoneScaleMode()"


def test___scale_mode___copy___makes_shallow_copy() -> None:
    new_scale_mode = copy.copy(NO_SCALING)

    assert new_scale_mode == NO_SCALING
    assert new_scale_mode is not NO_SCALING


def test___scale_mode___deepcopy___makes_deep_copy() -> None:
    new_scale_mode = copy.deepcopy(NO_SCALING)

    assert new_scale_mode == NO_SCALING
    assert new_scale_mode is not NO_SCALING


def test___scale_mode___pickle_unpickle___makes_deep_copy() -> None:
    new_scale_mode = pickle.loads(pickle.dumps(NO_SCALING))

    assert new_scale_mode == NO_SCALING
    assert new_scale_mode is not NO_SCALING


def test___scale_mode___pickle___references_public_modules() -> None:
    scale_mode_bytes = pickle.dumps(NO_SCALING)

    assert b"nitypes.waveform" in scale_mode_bytes
    assert b"nitypes.waveform._scaling" not in scale_mode_bytes
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/waveform/_timing/__init__.py sha256=572310c1d73ff8d5cc65fe835ffbd731c6ad0523ee304e5a248768d810c9826a bytes=60 -->
## FILE: tests/unit/waveform/_timing/__init__.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/waveform/_timing/__init__.py`
- sha256: `572310c1d73ff8d5cc65fe835ffbd731c6ad0523ee304e5a248768d810c9826a`
- bytes: 60

````python
"""Unit tests for the nitypes.waveform._timing package."""
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/waveform/_timing/_utils.py sha256=4aefcf56b72e2cbabbec665fb77b0f4431fe56f61f832099f99993ecc84d4110 bytes=1142 -->
## FILE: tests/unit/waveform/_timing/_utils.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/waveform/_timing/_utils.py`
- sha256: `4aefcf56b72e2cbabbec665fb77b0f4431fe56f61f832099f99993ecc84d4110`
- bytes: 1142

````python
from __future__ import annotations

from typing import Any

from nitypes.waveform import Timing


def assert_deep_copy(value: Timing[Any, Any, Any], other: Timing[Any, Any, Any]) -> None:
    """Assert that value is a deep copy of other."""
    assert value == other
    assert value is not other
    if other._timestamp is not None:
        assert value._timestamp is not other._timestamp
    if other._time_offset is not None:
        assert value._time_offset is not other._time_offset
    if other._sample_interval is not None:
        assert value._sample_interval is not other._sample_interval
    if other._timestamps is not None:
        assert value._timestamps is not other._timestamps


def assert_shallow_copy(value: Timing[Any, Any, Any], other: Timing[Any, Any, Any]) -> None:
    """Assert that value is a shallow copy of other."""
    assert value == other
    assert value is not other
    assert value._timestamp is other._timestamp
    assert value._time_offset is other._time_offset
    assert value._sample_interval is other._sample_interval
    assert value._timestamps is other._timestamps
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/waveform/_timing/test_bintime.py sha256=08a48964b5ef0c5e850b049d1ed2b09b3805b8e4fd6b0ad2649f2d655f25b141 bytes=27477 -->
## FILE: tests/unit/waveform/_timing/test_bintime.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/waveform/_timing/test_bintime.py`
- sha256: `08a48964b5ef0c5e850b049d1ed2b09b3805b8e4fd6b0ad2649f2d655f25b141`
- bytes: 27477

````python
from __future__ import annotations

import copy
import datetime as dt
import pickle
from typing import Any

import pytest
from typing_extensions import assert_type

import nitypes.bintime as bt
import nitypes.waveform.errors as wfmex
from nitypes.waveform import SampleIntervalMode, Timing
from tests.unit.waveform._timing._utils import assert_deep_copy, assert_shallow_copy


###############################################################################
# empty
###############################################################################
def test___empty___is_timing() -> None:
    assert_type(Timing.empty, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    assert isinstance(Timing.empty, Timing)


def test___empty___no_timestamp() -> None:
    assert not Timing.empty.has_timestamp
    with pytest.raises(RuntimeError) as exc:
        _ = Timing.empty.timestamp

    assert exc.value.args[0] == "The waveform timing does not have a timestamp."


def test___empty___no_start_time() -> None:
    assert not Timing.empty.has_start_time
    with pytest.raises(RuntimeError) as exc:
        _ = Timing.empty.start_time

    assert exc.value.args[0] == "The waveform timing does not have a timestamp."


def test___empty___no_time_offset() -> None:
    assert not Timing.empty.has_time_offset
    with pytest.raises(RuntimeError) as exc:
        _ = Timing.empty.time_offset

    assert exc.value.args[0] == "The waveform timing does not have a time offset."


def test___empty___no_sample_interval() -> None:
    assert not Timing.empty.has_sample_interval
    with pytest.raises(RuntimeError) as exc:
        _ = Timing.empty.sample_interval

    assert exc.value.args[0] == "The waveform timing does not have a sample interval."


def test___empty___sample_interval_mode_none() -> None:
    assert Timing.empty.sample_interval_mode == SampleIntervalMode.NONE


###############################################################################
# construct
###############################################################################
def test___no_optional_args___construct___creates_empty_timing() -> None:
    timing = Timing(SampleIntervalMode.NONE)

    assert_type(timing, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    assert not timing.has_timestamp
    assert not timing.has_time_offset
    assert not timing.has_sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.NONE


def test___timestamp___construct___creates_timing_with_timestamp() -> None:
    timestamp = bt.DateTime.now(dt.timezone.utc)
    timing = Timing(SampleIntervalMode.NONE, timestamp)

    assert_type(timing, Timing[bt.DateTime, dt.timedelta, dt.timedelta])
    assert timing.timestamp == timestamp
    assert not timing.has_time_offset
    assert not timing.has_sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.NONE


def test___timestamp___construct___has_start_time() -> None:
    timestamp = bt.DateTime.now(dt.timezone.utc)
    timing = Timing(SampleIntervalMode.NONE, timestamp)

    assert timing.has_start_time


def test___time_offset___construct___creates_timing_with_time_offset() -> None:
    time_offset = bt.TimeDelta(1.23)
    timing = Timing(SampleIntervalMode.NONE, time_offset=time_offset)

    assert_type(timing, Timing[dt.datetime, bt.TimeDelta, dt.timedelta])
    assert not timing.has_timestamp
    assert timing.time_offset == time_offset
    assert not timing.has_sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.NONE


def test___sample_interval___construct___creates_timing_with_sample_interval() -> None:
    sample_interval = bt.TimeDelta(1e-3)

    timing = Timing(SampleIntervalMode.REGULAR, sample_interval=sample_interval)

    assert_type(timing, Timing[dt.datetime, dt.timedelta, bt.TimeDelta])
    assert not timing.has_timestamp
    assert not timing.has_time_offset
    assert timing.sample_interval == sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.REGULAR


def test___sample_interval_timestamp_and_time_offset___construct___creates_timing_with_sample_interval_timestamp_and_time_offset() -> (
    None
):
    sample_interval = bt.TimeDelta(1e-3)
    timestamp = bt.DateTime.now(dt.timezone.utc)
    time_offset = bt.TimeDelta(1.23)

    timing = Timing(SampleIntervalMode.REGULAR, timestamp, time_offset, sample_interval)

    assert_type(timing, Timing[bt.DateTime, bt.TimeDelta, bt.TimeDelta])
    assert timing.timestamp == timestamp
    assert timing.time_offset == time_offset
    assert timing.sample_interval == sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.REGULAR


###############################################################################
# create_with_no_interval
###############################################################################
def test___no_args___create_with_no_interval___creates_empty_timing() -> None:
    timing = Timing.create_with_no_interval()

    assert_type(timing, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    assert not timing.has_timestamp
    assert not timing.has_time_offset
    assert not timing.has_sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.NONE


def test___timestamp___create_with_no_interval___creates_timing_with_timestamp() -> None:
    timestamp = bt.DateTime.now(dt.timezone.utc)
    timing = Timing.create_with_no_interval(timestamp)

    assert_type(timing, Timing[bt.DateTime, dt.timedelta, dt.timedelta])
    assert timing.timestamp == timestamp
    assert not timing.has_time_offset
    assert not timing.has_sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.NONE


def test___timestamp_and_time_offset___create_with_no_interval___creates_timing_with_timestamp_and_time_offset() -> (
    None
):
    timestamp = bt.DateTime.now(dt.timezone.utc)
    time_offset = bt.TimeDelta(1.23)
    timing = Timing.create_with_no_interval(timestamp, time_offset)

    assert_type(timing, Timing[bt.DateTime, bt.TimeDelta, dt.timedelta])
    assert timing.timestamp == timestamp
    assert timing.time_offset == time_offset
    assert not timing.has_sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.NONE


def test___time_offset___create_with_no_interval___creates_timing_with_time_offset() -> None:
    time_offset = bt.TimeDelta(1.23)
    timing = Timing.create_with_no_interval(time_offset=time_offset)

    assert_type(timing, Timing[dt.datetime, bt.TimeDelta, dt.timedelta])
    assert not timing.has_timestamp
    assert timing.time_offset == time_offset
    assert not timing.has_sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.NONE


###############################################################################
# create_with_regular_interval
###############################################################################
def test___sample_interval___create_with_regular_interval___creates_timing_with_sample_interval() -> (
    None
):
    sample_interval = bt.TimeDelta(1e-3)

    timing = Timing.create_with_regular_interval(sample_interval)

    assert_type(timing, Timing[dt.datetime, dt.timedelta, bt.TimeDelta])
    assert not timing.has_timestamp
    assert not timing.has_time_offset
    assert timing.sample_interval == sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.REGULAR


def test___sample_interval_and_timestamp___create_with_regular_interval___creates_timing_with_sample_interval_and_timestamp() -> (
    None
):
    sample_interval = bt.TimeDelta(1e-3)
    timestamp = bt.DateTime.now(dt.timezone.utc)

    timing = Timing.create_with_regular_interval(sample_interval, timestamp)

    assert_type(timing, Timing[bt.DateTime, dt.timedelta, bt.TimeDelta])
    assert timing.timestamp == timestamp
    assert not timing.has_time_offset
    assert timing.sample_interval == sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.REGULAR


def test___sample_interval_timestamp_and_time_offset___create_with_regular_interval___creates_timing_with_sample_interval_timestamp_and_time_offset() -> (
    None
):
    sample_interval = bt.TimeDelta(1e-3)
    timestamp = bt.DateTime.now(dt.timezone.utc)
    time_offset = bt.TimeDelta(1.23)

    timing = Timing.create_with_regular_interval(sample_interval, timestamp, time_offset)

    assert_type(timing, Timing[bt.DateTime, bt.TimeDelta, bt.TimeDelta])
    assert timing.timestamp == timestamp
    assert timing.time_offset == time_offset
    assert timing.sample_interval == sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.REGULAR


def test___sample_interval_and_time_offset___create_with_regular_interval___creates_timing_with_sample_interval_and_time_offset() -> (
    None
):
    sample_interval = bt.TimeDelta(1e-3)
    time_offset = bt.TimeDelta(1.23)

    timing = Timing.create_with_regular_interval(sample_interval, time_offset=time_offset)

    assert_type(timing, Timing[dt.datetime, bt.TimeDelta, bt.TimeDelta])
    assert not timing.has_timestamp
    assert timing.time_offset == time_offset
    assert timing.sample_interval == sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.REGULAR


###############################################################################
# create_with_irregular_interval
###############################################################################
@pytest.mark.parametrize(
    "time_offsets",
    [
        [],
        [bt.TimeDelta(0)],
        [bt.TimeDelta(0), bt.TimeDelta(0)],
        [bt.TimeDelta(0), bt.TimeDelta(1)],
        [bt.TimeDelta(0), bt.TimeDelta(1), bt.TimeDelta(2)],
        [
            bt.TimeDelta(0),
            bt.TimeDelta(1),
            bt.TimeDelta(2),
            bt.TimeDelta(3),
        ],
        [
            bt.TimeDelta(3),
            bt.TimeDelta(2),
            bt.TimeDelta(1),
            bt.TimeDelta(0),
        ],
        [
            bt.TimeDelta.from_ticks(0 << 60 | 0 << 32 | 1),
            bt.TimeDelta.from_ticks(0 << 60 | 1 << 32 | 0),
            bt.TimeDelta.from_ticks(1 << 60 | 0 << 32 | 0),
        ],
        [
            bt.TimeDelta.from_ticks(1 << 60 | 0 << 32 | 0),
            bt.TimeDelta.from_ticks(0 << 60 | 1 << 32 | 0),
            bt.TimeDelta.from_ticks(0 << 60 | 0 << 32 | 1),
        ],
        [
            bt.TimeDelta(0),
            bt.TimeDelta(1),
            bt.TimeDelta(1),
            bt.TimeDelta(2),
        ],
    ],
)
def test___monotonic_timestamps___create_with_irregular_interval___creates_timing_with_timestamps(
    time_offsets: list[bt.TimeDelta],
) -> None:
    start_time = bt.DateTime.now(dt.timezone.utc)
    timestamps = [start_time + offset for offset in time_offsets]

    timing = Timing.create_with_irregular_interval(timestamps)

    assert_type(timing, Timing[bt.DateTime, dt.timedelta, dt.timedelta])
    assert timing.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert timing._timestamps == timestamps


@pytest.mark.parametrize(
    "time_offsets",
    [
        [bt.TimeDelta(0), bt.TimeDelta(1), bt.TimeDelta(0)],
        [bt.TimeDelta(1), bt.TimeDelta(0), bt.TimeDelta(1)],
    ],
)
def test___non_monotonic_timestamps___create_with_irregular_interval___raises_value_error(
    time_offsets: list[bt.TimeDelta],
) -> None:
    start_time = bt.DateTime.now(dt.timezone.utc)
    timestamps = [start_time + offset for offset in time_offsets]

    with pytest.raises(ValueError) as exc:
        _ = Timing.create_with_irregular_interval(timestamps)

    assert exc.value.args[0].startswith("The timestamps must be in ascending or descending order.")


def test___timestamps_tuple___create_with_irregular_interval___creates_timing_with_timestamps() -> (
    None
):
    start_time = bt.DateTime.now(dt.timezone.utc)
    timestamps = (start_time,)

    timing = Timing.create_with_irregular_interval(timestamps)

    assert_type(timing, Timing[bt.DateTime, dt.timedelta, dt.timedelta])
    assert timing.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert timing._timestamps == list(timestamps)


###############################################################################
# get_timestamps
###############################################################################
def test___no_interval___get_timestamps___raises_correct_error() -> None:
    start_time = bt.DateTime.now(dt.timezone.utc)
    timing = Timing.create_with_no_interval(start_time)

    with pytest.raises(wfmex.NoTimestampInformationError) as exc:
        _ = timing.get_timestamps(0, 5)

    assert exc.value.args[0].startswith(
        "The waveform timing does not have valid timestamp information."
    )


def test___regular_interval___get_timestamps___gets_timestamps() -> None:
    start_time = bt.DateTime.now(dt.timezone.utc)
    sample_interval = bt.TimeDelta(1e-3)
    timing = Timing.create_with_regular_interval(sample_interval, start_time)

    assert list(timing.get_timestamps(3, 4)) == [
        start_time + 3 * sample_interval,
        start_time + 4 * sample_interval,
        start_time + 5 * sample_interval,
        start_time + 6 * sample_interval,
    ]


def test___irregular_interval___get_timestamps___gets_timestamps() -> None:
    start_time = bt.DateTime.now(dt.timezone.utc)
    sample_interval = bt.TimeDelta(1e-3)
    timestamps = [start_time + i * sample_interval for i in range(10)]
    timing = Timing.create_with_irregular_interval(timestamps)

    assert list(timing.get_timestamps(0, 10)) == timestamps


def test___irregular_interval_subset___get_timestamps___gets_timestamps() -> None:
    start_time = bt.DateTime.now(dt.timezone.utc)
    sample_interval = bt.TimeDelta(1e-3)
    timestamps = [start_time + i * sample_interval for i in range(10)]
    timing = Timing.create_with_irregular_interval(timestamps)

    assert list(timing.get_timestamps(3, 4)) == timestamps[3:7]


###############################################################################
# magic methods
###############################################################################
@pytest.mark.parametrize(
    "left, right",
    [
        (Timing.create_with_no_interval(), Timing.create_with_no_interval()),
        (
            Timing.create_with_no_interval(bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc)),
            Timing.create_with_no_interval(bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc)),
        ),
        (
            Timing.create_with_no_interval(None, bt.TimeDelta(1)),
            Timing.create_with_no_interval(None, bt.TimeDelta(1)),
        ),
        (
            Timing.create_with_no_interval(
                bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), bt.TimeDelta(1)
            ),
            Timing.create_with_no_interval(
                bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), bt.TimeDelta(1)
            ),
        ),
        (
            Timing.create_with_regular_interval(bt.TimeDelta(1e-3)),
            Timing.create_with_regular_interval(bt.TimeDelta(1e-3)),
        ),
        (
            Timing.create_with_regular_interval(
                bt.TimeDelta(1e-3), bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc)
            ),
            Timing.create_with_regular_interval(
                bt.TimeDelta(1e-3), bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc)
            ),
        ),
        (
            Timing.create_with_regular_interval(
                bt.TimeDelta(1e-3), bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), bt.TimeDelta(1)
            ),
            Timing.create_with_regular_interval(
                bt.TimeDelta(1e-3), bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), bt.TimeDelta(1)
            ),
        ),
        (
            Timing.create_with_irregular_interval(
                [
                    bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                    bt.DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
                ]
            ),
            Timing.create_with_irregular_interval(
                [
                    bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                    bt.DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
                ]
            ),
        ),
    ],
)
def test___same_value___equality___equal(
    left: Timing[Any, Any, Any], right: Timing[Any, Any, Any]
) -> None:
    assert left == right
    assert not (left != right)


@pytest.mark.parametrize(
    "left, right",
    [
        (
            Timing.create_with_no_interval(
                bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), bt.TimeDelta(1)
            ),
            Timing.create_with_no_interval(
                bt.DateTime(2025, 1, 2, tzinfo=dt.timezone.utc), bt.TimeDelta(1)
            ),
        ),
        (
            Timing.create_with_no_interval(
                bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), bt.TimeDelta(1)
            ),
            Timing.create_with_no_interval(
                bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), bt.TimeDelta(2)
            ),
        ),
        (
            Timing.create_with_regular_interval(
                bt.TimeDelta(1e-3), bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), bt.TimeDelta(1)
            ),
            Timing.create_with_regular_interval(
                bt.TimeDelta(2e-3), bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), bt.TimeDelta(1)
            ),
        ),
        (
            Timing.create_with_regular_interval(
                bt.TimeDelta(1e-3), bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), bt.TimeDelta(1)
            ),
            Timing.create_with_regular_interval(
                bt.TimeDelta(1e-3), bt.DateTime(2025, 1, 2, tzinfo=dt.timezone.utc), bt.TimeDelta(1)
            ),
        ),
        (
            Timing.create_with_regular_interval(
                bt.TimeDelta(1e-3), bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), bt.TimeDelta(1)
            ),
            Timing.create_with_regular_interval(
                bt.TimeDelta(1e-3), bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), bt.TimeDelta(2)
            ),
        ),
        (
            Timing.create_with_irregular_interval(
                [
                    bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                    bt.DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
                ]
            ),
            Timing.create_with_irregular_interval(
                [
                    bt.DateTime(2025, 1, 3, tzinfo=dt.timezone.utc),
                    bt.DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
                ]
            ),
        ),
    ],
)
def test___different_value___equality___not_equal(
    left: Timing[Any, Any, Any],
    right: Timing[Any, Any, Any],
) -> None:
    assert not (left == right)
    assert left != right


@pytest.mark.parametrize(
    "value, expected_repr",
    [
        (
            Timing.create_with_no_interval(),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.NONE)",
        ),
        (
            Timing.create_with_no_interval(bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc)),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.NONE, timestamp=nitypes.bintime.DateTime(2025, 1, 1, 0, 0, tzinfo=datetime.timezone.utc))",
        ),
        (
            Timing.create_with_no_interval(None, bt.TimeDelta(1)),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.NONE, time_offset=nitypes.bintime.TimeDelta(Decimal('1')))",
        ),
        (
            Timing.create_with_no_interval(
                bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), bt.TimeDelta(1)
            ),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.NONE, timestamp=nitypes.bintime.DateTime(2025, 1, 1, 0, 0, tzinfo=datetime.timezone.utc), time_offset=nitypes.bintime.TimeDelta(Decimal('1')))",
        ),
        (
            Timing.create_with_no_interval(
                bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), bt.TimeDelta()
            ),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.NONE, timestamp=nitypes.bintime.DateTime(2025, 1, 1, 0, 0, tzinfo=datetime.timezone.utc), time_offset=nitypes.bintime.TimeDelta(Decimal('0')))",
        ),
        (
            Timing.create_with_regular_interval(bt.TimeDelta(1e-3)),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR, sample_interval=nitypes.bintime.TimeDelta(Decimal('0.00100000000000000002081668')))",
        ),
        (
            Timing.create_with_regular_interval(
                bt.TimeDelta(1e-3), bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc)
            ),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR, timestamp=nitypes.bintime.DateTime(2025, 1, 1, 0, 0, tzinfo=datetime.timezone.utc), sample_interval=nitypes.bintime.TimeDelta(Decimal('0.00100000000000000002081668')))",
        ),
        (
            Timing.create_with_regular_interval(
                bt.TimeDelta(1e-3), bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), bt.TimeDelta(1)
            ),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR, timestamp=nitypes.bintime.DateTime(2025, 1, 1, 0, 0, tzinfo=datetime.timezone.utc), time_offset=nitypes.bintime.TimeDelta(Decimal('1')), sample_interval=nitypes.bintime.TimeDelta(Decimal('0.00100000000000000002081668')))",
        ),
        (
            Timing.create_with_irregular_interval(
                [
                    bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
                    bt.DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
                ]
            ),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.IRREGULAR, timestamps=[nitypes.bintime.DateTime(2025, 1, 1, 0, 0, tzinfo=datetime.timezone.utc), nitypes.bintime.DateTime(2025, 1, 2, 0, 0, tzinfo=datetime.timezone.utc)])",
        ),
    ],
)
def test___various_values___repr___looks_ok(
    value: Timing[Any, Any, Any], expected_repr: str
) -> None:
    assert repr(value) == expected_repr


_VARIOUS_VALUES = [
    Timing.create_with_no_interval(),
    Timing.create_with_no_interval(bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc)),
    Timing.create_with_no_interval(None, bt.TimeDelta(1)),
    Timing.create_with_no_interval(
        bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), bt.TimeDelta(1)
    ),
    Timing.create_with_regular_interval(bt.TimeDelta(1e-3)),
    Timing.create_with_regular_interval(
        bt.TimeDelta(1e-3), bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc)
    ),
    Timing.create_with_regular_interval(
        bt.TimeDelta(1e-3), bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), bt.TimeDelta(1)
    ),
    Timing.create_with_irregular_interval(
        [
            bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc),
            bt.DateTime(2025, 1, 2, tzinfo=dt.timezone.utc),
        ]
    ),
]


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___copy___makes_shallow_copy(value: Timing[Any, Any, Any]) -> None:
    new_value = copy.copy(value)

    assert_shallow_copy(new_value, value)


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___deepcopy___makes_deep_copy(value: Timing[Any, Any, Any]) -> None:
    new_value = copy.deepcopy(value)

    assert_deep_copy(new_value, value)


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___pickle_unpickle___makes_deep_copy(
    value: Timing[Any, Any, Any],
) -> None:
    new_value = pickle.loads(pickle.dumps(value))

    assert_deep_copy(new_value, value)


def test___timing___pickle___references_public_modules() -> None:
    value = Timing.create_with_regular_interval(bt.TimeDelta(1e-3))

    value_bytes = pickle.dumps(value)

    assert b"nitypes.waveform" in value_bytes
    assert b"nitypes.waveform._timing" not in value_bytes


###############################################################################
# _append_timing
###############################################################################
@pytest.mark.parametrize(
    "left_offsets, right_offsets",
    [
        ([], []),
        ([bt.TimeDelta(0)], []),
        ([bt.TimeDelta(0), bt.TimeDelta(1)], []),
        ([bt.TimeDelta(0), bt.TimeDelta(1), bt.TimeDelta(2)], []),
        ([bt.TimeDelta(0)], [bt.TimeDelta(1)]),
        ([bt.TimeDelta(0)], [bt.TimeDelta(1), bt.TimeDelta(2)]),
        (
            [bt.TimeDelta(0), bt.TimeDelta(1)],
            [bt.TimeDelta(2), bt.TimeDelta(3)],
        ),
        (
            [bt.TimeDelta(3), bt.TimeDelta(2)],
            [bt.TimeDelta(1), bt.TimeDelta(0)],
        ),
        (
            [bt.TimeDelta(0), bt.TimeDelta(1)],
            [bt.TimeDelta(1), bt.TimeDelta(2)],
        ),
        (
            [bt.TimeDelta(2), bt.TimeDelta(1)],
            [bt.TimeDelta(1), bt.TimeDelta(0)],
        ),
    ],
)
def test___monotonic_timestamps___append_timing___appends_timestamps(
    left_offsets: list[bt.TimeDelta],
    right_offsets: list[bt.TimeDelta],
) -> None:
    start_time = bt.DateTime.now(dt.timezone.utc)
    left_timestamps = [start_time + offset for offset in left_offsets]
    right_timestamps = [start_time + offset for offset in right_offsets]
    left_timing = Timing.create_with_irregular_interval(left_timestamps)
    right_timing = Timing.create_with_irregular_interval(right_timestamps)

    new_timing = left_timing._append_timing(right_timing)

    assert_type(new_timing, Timing[bt.DateTime, dt.timedelta, dt.timedelta])
    assert isinstance(new_timing, Timing)
    assert new_timing._timestamps == left_timestamps + right_timestamps


@pytest.mark.parametrize(
    "left_offsets, right_offsets",
    [
        ([bt.TimeDelta(0)], [bt.TimeDelta(1), bt.TimeDelta(0)]),
        ([bt.TimeDelta(1)], [bt.TimeDelta(0), bt.TimeDelta(2)]),
        ([bt.TimeDelta(0), bt.TimeDelta(1)], [bt.TimeDelta(0)]),
        ([bt.TimeDelta(1), bt.TimeDelta(0)], [bt.TimeDelta(1)]),
        ([bt.TimeDelta(0), bt.TimeDelta(1)], [bt.TimeDelta(2), bt.TimeDelta(0)]),
    ],
)
def test___non_monotonic_timestamps___append_timing___raises_value_error(
    left_offsets: list[bt.TimeDelta],
    right_offsets: list[bt.TimeDelta],
) -> None:
    start_time = bt.DateTime.now(dt.timezone.utc)
    left_timestamps = [start_time + offset for offset in left_offsets]
    right_timestamps = [start_time + offset for offset in right_offsets]
    left_timing = Timing.create_with_irregular_interval(left_timestamps)
    right_timing = Timing.create_with_irregular_interval(right_timestamps)

    with pytest.raises(ValueError) as exc:
        _ = left_timing._append_timing(right_timing)

    assert exc.value.args[0].startswith("The timestamps must be in ascending or descending order.")
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/waveform/_timing/test_conversion.py sha256=2940e9a2e39d4fef39930248d29fe064ec41521105dd1710c1616a06e8615eb7 bytes=6166 -->
## FILE: tests/unit/waveform/_timing/test_conversion.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/waveform/_timing/test_conversion.py`
- sha256: `2940e9a2e39d4fef39930248d29fe064ec41521105dd1710c1616a06e8615eb7`
- bytes: 6166

````python
from __future__ import annotations

import datetime as dt

import hightime as ht
import pytest
from typing_extensions import assert_type

import nitypes.bintime as bt
from nitypes.waveform import SampleIntervalMode, Timing


def test___bt_to_bt___convert_timing___returns_original_object() -> None:
    value_in = Timing.create_with_regular_interval(
        bt.TimeDelta(1e-3), bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), bt.TimeDelta(1)
    )

    value_out = value_in.to_bintime()

    assert_type(value_out, Timing[bt.DateTime, bt.TimeDelta, bt.TimeDelta])
    assert value_out is value_in


def test___dt_to_dt___convert_timing___returns_original_object() -> None:
    value_in = Timing.create_with_regular_interval(
        dt.timedelta(milliseconds=1), dt.datetime(2025, 1, 1), dt.timedelta(seconds=1)
    )

    value_out = value_in.to_datetime()

    assert_type(value_out, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    assert value_out is value_in


def test___ht_to_ht___convert_timing___returns_original_object() -> None:
    value_in = Timing.create_with_regular_interval(
        ht.timedelta(milliseconds=1), ht.datetime(2025, 1, 1), ht.timedelta(seconds=1)
    )

    value_out = value_in.to_hightime()

    assert_type(value_out, Timing[ht.datetime, ht.timedelta, ht.timedelta])

    assert value_out is value_in


def test___empty_to_bt___convert_timing___returns_equivalent_timing() -> None:
    value_in = Timing.empty

    value_out = value_in.to_bintime()

    assert_type(value_out, Timing[bt.DateTime, bt.TimeDelta, bt.TimeDelta])
    # Can't check runtime field type because they are all None.
    assert value_out == value_in


def test___empty_to_dt___convert_timing___returns_original_object() -> None:
    value_in = Timing.empty

    value_out = value_in.to_datetime()

    assert_type(value_out, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    # Can't check runtime field type because they are all None.
    assert value_out is value_in


def test___empty_to_ht___convert_timing___returns_equivalent_timing() -> None:
    value_in = Timing.empty

    value_out = value_in.to_hightime()

    assert_type(value_out, Timing[ht.datetime, ht.timedelta, ht.timedelta])
    # Can't check runtime field type because they are all None.
    assert value_out == value_in


def test___dt_to_bt_regular_interval___convert_timing___returns_equivalent_timing() -> None:
    value_in = Timing.create_with_regular_interval(
        dt.timedelta(milliseconds=1),
        dt.datetime(2025, 1, 1, tzinfo=dt.timezone.utc),
        dt.timedelta(seconds=1),
    )

    value_out = value_in.to_bintime()

    assert_type(value_out, Timing[bt.DateTime, bt.TimeDelta, bt.TimeDelta])
    assert isinstance(value_out.timestamp, bt.DateTime)
    assert isinstance(value_out.time_offset, bt.TimeDelta)
    assert isinstance(value_out.sample_interval, bt.TimeDelta)
    assert value_out.sample_interval_mode == SampleIntervalMode.REGULAR
    assert value_out.sample_interval.total_seconds() == pytest.approx(1e-3)  # rounding
    assert value_out.timestamp == bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc)
    assert value_out.time_offset == bt.TimeDelta(1)


def test___dt_to_ht_regular_interval___convert_timing___returns_equivalent_timing() -> None:
    value_in = Timing.create_with_regular_interval(
        dt.timedelta(milliseconds=1), dt.datetime(2025, 1, 1), dt.timedelta(seconds=1)
    )

    value_out = value_in.to_hightime()

    assert_type(value_out, Timing[ht.datetime, ht.timedelta, ht.timedelta])
    assert isinstance(value_out.timestamp, ht.datetime)
    assert isinstance(value_out.time_offset, ht.timedelta)
    assert isinstance(value_out.sample_interval, ht.timedelta)
    assert value_out.sample_interval_mode == SampleIntervalMode.REGULAR
    assert value_out.sample_interval == ht.timedelta(milliseconds=1)
    assert value_out.timestamp == ht.datetime(2025, 1, 1)
    assert value_out.time_offset == ht.timedelta(seconds=1)


def test___ht_to_dt_regular_interval___convert_timing___returns_equivalent_timing() -> None:
    value_in = Timing.create_with_regular_interval(
        ht.timedelta(milliseconds=1), ht.datetime(2025, 1, 1), ht.timedelta(seconds=1)
    )

    value_out = value_in.to_datetime()

    assert_type(value_out, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    assert isinstance(value_out.timestamp, dt.datetime)
    assert isinstance(value_out.time_offset, dt.timedelta)
    assert isinstance(value_out.sample_interval, dt.timedelta)
    assert value_out.sample_interval_mode == SampleIntervalMode.REGULAR
    assert value_out.sample_interval == dt.timedelta(milliseconds=1)
    assert value_out.timestamp == dt.datetime(2025, 1, 1)
    assert value_out.time_offset == dt.timedelta(seconds=1)


def test___dt_to_ht_irregular_interval___convert_timing___returns_equivalent_timing() -> None:
    value_in = Timing.create_with_irregular_interval(
        [dt.datetime(2025, 1, 1), dt.datetime(2025, 1, 2)]
    )

    value_out = value_in.to_hightime()

    assert_type(value_out, Timing[ht.datetime, ht.timedelta, ht.timedelta])
    assert value_out._timestamps is not None and all(
        isinstance(ts, ht.datetime) for ts in value_out._timestamps
    )
    assert value_out.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert value_out._timestamps == [ht.datetime(2025, 1, 1), ht.datetime(2025, 1, 2)]


def test___ht_to_dt_irregular_interval___convert_timing___returns_equivalent_timing() -> None:
    value_in = Timing.create_with_irregular_interval(
        [ht.datetime(2025, 1, 1), ht.datetime(2025, 1, 2)]
    )

    value_out = value_in.to_datetime()

    assert_type(value_out, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    assert value_out._timestamps is not None and all(
        isinstance(ts, dt.datetime) for ts in value_out._timestamps
    )
    assert value_out.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert value_out._timestamps == [dt.datetime(2025, 1, 1), dt.datetime(2025, 1, 2)]
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/waveform/_timing/test_datetime.py sha256=18e7294efcac237595fba0157e66cfe8a0b6d3c59048464d639fc60b1817481a bytes=25666 -->
## FILE: tests/unit/waveform/_timing/test_datetime.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/waveform/_timing/test_datetime.py`
- sha256: `18e7294efcac237595fba0157e66cfe8a0b6d3c59048464d639fc60b1817481a`
- bytes: 25666

````python
from __future__ import annotations

import copy
import datetime as dt
import pickle
from typing import Any

import pytest
from typing_extensions import assert_type

import nitypes.waveform.errors as wfmex
from nitypes.waveform import SampleIntervalMode, Timing
from tests.unit.waveform._timing._utils import assert_deep_copy, assert_shallow_copy


###############################################################################
# empty
###############################################################################
def test___empty___is_timing() -> None:
    assert_type(Timing.empty, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    assert isinstance(Timing.empty, Timing)


def test___empty___no_timestamp() -> None:
    assert not Timing.empty.has_timestamp
    with pytest.raises(RuntimeError) as exc:
        _ = Timing.empty.timestamp

    assert exc.value.args[0] == "The waveform timing does not have a timestamp."


def test___empty___no_start_time() -> None:
    assert not Timing.empty.has_start_time
    with pytest.raises(RuntimeError) as exc:
        _ = Timing.empty.start_time

    assert exc.value.args[0] == "The waveform timing does not have a timestamp."


def test___empty___no_time_offset() -> None:
    assert not Timing.empty.has_time_offset
    with pytest.raises(RuntimeError) as exc:
        _ = Timing.empty.time_offset

    assert exc.value.args[0] == "The waveform timing does not have a time offset."


def test___empty___no_sample_interval() -> None:
    assert not Timing.empty.has_sample_interval
    with pytest.raises(RuntimeError) as exc:
        _ = Timing.empty.sample_interval

    assert exc.value.args[0] == "The waveform timing does not have a sample interval."


def test___empty___sample_interval_mode_none() -> None:
    assert Timing.empty.sample_interval_mode == SampleIntervalMode.NONE


###############################################################################
# construct
###############################################################################
def test___no_optional_args___construct___creates_empty_timing() -> None:
    timing = Timing(SampleIntervalMode.NONE)

    assert_type(timing, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    assert not timing.has_timestamp
    assert not timing.has_time_offset
    assert not timing.has_sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.NONE


def test___timestamp___construct___creates_timing_with_timestamp() -> None:
    timestamp = dt.datetime.now(dt.timezone.utc)
    timing = Timing(SampleIntervalMode.NONE, timestamp)

    assert_type(timing, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    assert timing.timestamp == timestamp
    assert not timing.has_time_offset
    assert not timing.has_sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.NONE


def test___timestamp___construct___has_start_time() -> None:
    timestamp = dt.datetime.now(dt.timezone.utc)
    timing = Timing(SampleIntervalMode.NONE, timestamp)

    assert timing.has_start_time


def test___time_offset___construct___creates_timing_with_time_offset() -> None:
    time_offset = dt.timedelta(seconds=1.23)
    timing = Timing(SampleIntervalMode.NONE, time_offset=time_offset)

    assert_type(timing, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    assert not timing.has_timestamp
    assert timing.time_offset == time_offset
    assert not timing.has_sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.NONE


def test___sample_interval___construct___creates_timing_with_sample_interval() -> None:
    sample_interval = dt.timedelta(seconds=1e-3)

    timing = Timing(SampleIntervalMode.REGULAR, sample_interval=sample_interval)

    assert_type(timing, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    assert not timing.has_timestamp
    assert not timing.has_time_offset
    assert timing.sample_interval == sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.REGULAR


def test___sample_interval_timestamp_and_time_offset___construct___creates_timing_with_sample_interval_timestamp_and_time_offset() -> (
    None
):
    sample_interval = dt.timedelta(seconds=1e-3)
    timestamp = dt.datetime.now(dt.timezone.utc)
    time_offset = dt.timedelta(seconds=1.23)

    timing = Timing(SampleIntervalMode.REGULAR, timestamp, time_offset, sample_interval)

    assert_type(timing, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    assert timing.timestamp == timestamp
    assert timing.time_offset == time_offset
    assert timing.sample_interval == sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.REGULAR


###############################################################################
# create_with_no_interval
###############################################################################
def test___no_args___create_with_no_interval___creates_empty_timing() -> None:
    timing = Timing.create_with_no_interval()

    assert_type(timing, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    assert not timing.has_timestamp
    assert not timing.has_time_offset
    assert not timing.has_sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.NONE


def test___timestamp___create_with_no_interval___creates_timing_with_timestamp() -> None:
    timestamp = dt.datetime.now(dt.timezone.utc)
    timing = Timing.create_with_no_interval(timestamp)

    assert_type(timing, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    assert timing.timestamp == timestamp
    assert not timing.has_time_offset
    assert not timing.has_sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.NONE


def test___timestamp_and_time_offset___create_with_no_interval___creates_timing_with_timestamp_and_time_offset() -> (
    None
):
    timestamp = dt.datetime.now(dt.timezone.utc)
    time_offset = dt.timedelta(seconds=1.23)
    timing = Timing.create_with_no_interval(timestamp, time_offset)

    assert_type(timing, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    assert timing.timestamp == timestamp
    assert timing.time_offset == time_offset
    assert not timing.has_sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.NONE


def test___time_offset___create_with_no_interval___creates_timing_with_time_offset() -> None:
    time_offset = dt.timedelta(seconds=1.23)
    timing = Timing.create_with_no_interval(time_offset=time_offset)

    assert_type(timing, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    assert not timing.has_timestamp
    assert timing.time_offset == time_offset
    assert not timing.has_sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.NONE


###############################################################################
# create_with_regular_interval
###############################################################################
def test___sample_interval___create_with_regular_interval___creates_timing_with_sample_interval() -> (
    None
):
    sample_interval = dt.timedelta(milliseconds=1)

    timing = Timing.create_with_regular_interval(sample_interval)

    assert_type(timing, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    assert not timing.has_timestamp
    assert not timing.has_time_offset
    assert timing.sample_interval == sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.REGULAR


def test___sample_interval_and_timestamp___create_with_regular_interval___creates_timing_with_sample_interval_and_timestamp() -> (
    None
):
    sample_interval = dt.timedelta(milliseconds=1)
    timestamp = dt.datetime.now(dt.timezone.utc)

    timing = Timing.create_with_regular_interval(sample_interval, timestamp)

    assert_type(timing, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    assert timing.timestamp == timestamp
    assert not timing.has_time_offset
    assert timing.sample_interval == sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.REGULAR


def test___sample_interval_timestamp_and_time_offset___create_with_regular_interval___creates_timing_with_sample_interval_timestamp_and_time_offset() -> (
    None
):
    sample_interval = dt.timedelta(milliseconds=1)
    timestamp = dt.datetime.now(dt.timezone.utc)
    time_offset = dt.timedelta(seconds=1.23)

    timing = Timing.create_with_regular_interval(sample_interval, timestamp, time_offset)

    assert_type(timing, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    assert timing.timestamp == timestamp
    assert timing.time_offset == time_offset
    assert timing.sample_interval == sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.REGULAR


def test___sample_interval_and_time_offset___create_with_regular_interval___creates_timing_with_sample_interval_and_time_offset() -> (
    None
):
    sample_interval = dt.timedelta(milliseconds=1)
    time_offset = dt.timedelta(seconds=1.23)

    timing = Timing.create_with_regular_interval(sample_interval, time_offset=time_offset)

    assert_type(timing, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    assert not timing.has_timestamp
    assert timing.time_offset == time_offset
    assert timing.sample_interval == sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.REGULAR


###############################################################################
# create_with_irregular_interval
###############################################################################
@pytest.mark.parametrize(
    "time_offsets",
    [
        [],
        [dt.timedelta(0)],
        [dt.timedelta(0), dt.timedelta(0)],
        [dt.timedelta(0), dt.timedelta(1)],
        [dt.timedelta(0), dt.timedelta(1), dt.timedelta(2)],
        [
            dt.timedelta(0),
            dt.timedelta(1),
            dt.timedelta(2),
            dt.timedelta(3),
        ],
        [
            dt.timedelta(3),
            dt.timedelta(2),
            dt.timedelta(1),
            dt.timedelta(0),
        ],
        [dt.timedelta(0, 0, 1), dt.timedelta(0, 1, 0), dt.timedelta(1, 0, 0)],
        [dt.timedelta(1, 0, 0), dt.timedelta(0, 1, 0), dt.timedelta(0, 0, 1)],
        [
            dt.timedelta(0),
            dt.timedelta(1),
            dt.timedelta(1),
            dt.timedelta(2),
        ],
    ],
)
def test___monotonic_timestamps___create_with_irregular_interval___creates_timing_with_timestamps(
    time_offsets: list[dt.timedelta],
) -> None:
    start_time = dt.datetime.now(dt.timezone.utc)
    timestamps = [start_time + offset for offset in time_offsets]

    timing = Timing.create_with_irregular_interval(timestamps)

    assert_type(timing, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    assert timing.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert timing._timestamps == timestamps


@pytest.mark.parametrize(
    "time_offsets",
    [
        [dt.timedelta(0), dt.timedelta(1), dt.timedelta(0)],
        [dt.timedelta(1), dt.timedelta(0), dt.timedelta(1)],
    ],
)
def test___non_monotonic_timestamps___create_with_irregular_interval___raises_value_error(
    time_offsets: list[dt.timedelta],
) -> None:
    start_time = dt.datetime.now(dt.timezone.utc)
    timestamps = [start_time + offset for offset in time_offsets]

    with pytest.raises(ValueError) as exc:
        _ = Timing.create_with_irregular_interval(timestamps)

    assert exc.value.args[0].startswith("The timestamps must be in ascending or descending order.")


def test___timestamps_tuple___create_with_irregular_interval___creates_timing_with_timestamps() -> (
    None
):
    start_time = dt.datetime.now(dt.timezone.utc)
    timestamps = (start_time,)

    timing = Timing.create_with_irregular_interval(timestamps)

    assert_type(timing, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    assert timing.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert timing._timestamps == list(timestamps)


###############################################################################
# get_timestamps
###############################################################################
def test___no_interval___get_timestamps___raises_correct_error() -> None:
    start_time = dt.datetime.now(dt.timezone.utc)
    timing = Timing.create_with_no_interval(start_time)

    with pytest.raises(wfmex.NoTimestampInformationError) as exc:
        _ = timing.get_timestamps(0, 5)

    assert exc.value.args[0].startswith(
        "The waveform timing does not have valid timestamp information."
    )


def test___regular_interval___get_timestamps___gets_timestamps() -> None:
    start_time = dt.datetime.now(dt.timezone.utc)
    sample_interval = dt.timedelta(milliseconds=1)
    timing = Timing.create_with_regular_interval(sample_interval, start_time)

    assert list(timing.get_timestamps(3, 4)) == [
        start_time + 3 * sample_interval,
        start_time + 4 * sample_interval,
        start_time + 5 * sample_interval,
        start_time + 6 * sample_interval,
    ]


def test___irregular_interval___get_timestamps___gets_timestamps() -> None:
    start_time = dt.datetime.now(dt.timezone.utc)
    sample_interval = dt.timedelta(milliseconds=1)
    timestamps = [start_time + i * sample_interval for i in range(10)]
    timing = Timing.create_with_irregular_interval(timestamps)

    assert list(timing.get_timestamps(0, 10)) == timestamps


def test___irregular_interval_subset___get_timestamps___gets_timestamps() -> None:
    start_time = dt.datetime.now(dt.timezone.utc)
    sample_interval = dt.timedelta(milliseconds=1)
    timestamps = [start_time + i * sample_interval for i in range(10)]
    timing = Timing.create_with_irregular_interval(timestamps)

    assert list(timing.get_timestamps(3, 4)) == timestamps[3:7]


###############################################################################
# magic methods
###############################################################################
@pytest.mark.parametrize(
    "left, right",
    [
        (Timing.create_with_no_interval(), Timing.create_with_no_interval()),
        (
            Timing.create_with_no_interval(dt.datetime(2025, 1, 1)),
            Timing.create_with_no_interval(dt.datetime(2025, 1, 1)),
        ),
        (
            Timing.create_with_no_interval(None, dt.timedelta(seconds=1)),
            Timing.create_with_no_interval(None, dt.timedelta(seconds=1)),
        ),
        (
            Timing.create_with_no_interval(dt.datetime(2025, 1, 1), dt.timedelta(seconds=1)),
            Timing.create_with_no_interval(dt.datetime(2025, 1, 1), dt.timedelta(seconds=1)),
        ),
        (
            Timing.create_with_regular_interval(dt.timedelta(milliseconds=1)),
            Timing.create_with_regular_interval(dt.timedelta(milliseconds=1)),
        ),
        (
            Timing.create_with_regular_interval(
                dt.timedelta(milliseconds=1), dt.datetime(2025, 1, 1)
            ),
            Timing.create_with_regular_interval(
                dt.timedelta(milliseconds=1), dt.datetime(2025, 1, 1)
            ),
        ),
        (
            Timing.create_with_regular_interval(
                dt.timedelta(milliseconds=1), dt.datetime(2025, 1, 1), dt.timedelta(seconds=1)
            ),
            Timing.create_with_regular_interval(
                dt.timedelta(milliseconds=1), dt.datetime(2025, 1, 1), dt.timedelta(seconds=1)
            ),
        ),
        (
            Timing.create_with_irregular_interval(
                [dt.datetime(2025, 1, 1), dt.datetime(2025, 1, 2)]
            ),
            Timing.create_with_irregular_interval(
                [dt.datetime(2025, 1, 1), dt.datetime(2025, 1, 2)]
            ),
        ),
    ],
)
def test___same_value___equality___equal(
    left: Timing[Any, Any, Any], right: Timing[Any, Any, Any]
) -> None:
    assert left == right
    assert not (left != right)


@pytest.mark.parametrize(
    "left, right",
    [
        (
            Timing.create_with_no_interval(dt.datetime(2025, 1, 1), dt.timedelta(seconds=1)),
            Timing.create_with_no_interval(dt.datetime(2025, 1, 2), dt.timedelta(seconds=1)),
        ),
        (
            Timing.create_with_no_interval(dt.datetime(2025, 1, 1), dt.timedelta(seconds=1)),
            Timing.create_with_no_interval(dt.datetime(2025, 1, 1), dt.timedelta(seconds=2)),
        ),
        (
            Timing.create_with_regular_interval(
                dt.timedelta(milliseconds=1), dt.datetime(2025, 1, 1), dt.timedelta(seconds=1)
            ),
            Timing.create_with_regular_interval(
                dt.timedelta(milliseconds=2), dt.datetime(2025, 1, 1), dt.timedelta(seconds=1)
            ),
        ),
        (
            Timing.create_with_regular_interval(
                dt.timedelta(milliseconds=1), dt.datetime(2025, 1, 1), dt.timedelta(seconds=1)
            ),
            Timing.create_with_regular_interval(
                dt.timedelta(milliseconds=1), dt.datetime(2025, 1, 2), dt.timedelta(seconds=1)
            ),
        ),
        (
            Timing.create_with_regular_interval(
                dt.timedelta(milliseconds=1), dt.datetime(2025, 1, 1), dt.timedelta(seconds=1)
            ),
            Timing.create_with_regular_interval(
                dt.timedelta(milliseconds=1), dt.datetime(2025, 1, 1), dt.timedelta(seconds=2)
            ),
        ),
        (
            Timing.create_with_irregular_interval(
                [dt.datetime(2025, 1, 1), dt.datetime(2025, 1, 2)]
            ),
            Timing.create_with_irregular_interval(
                [dt.datetime(2025, 1, 3), dt.datetime(2025, 1, 2)]
            ),
        ),
    ],
)
def test___different_value___equality___not_equal(
    left: Timing[Any, Any, Any], right: Timing[Any, Any, Any]
) -> None:
    assert not (left == right)
    assert left != right


@pytest.mark.parametrize(
    "value, expected_repr",
    [
        (
            Timing.create_with_no_interval(),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.NONE)",
        ),
        (
            Timing.create_with_no_interval(dt.datetime(2025, 1, 1)),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.NONE, timestamp=datetime.datetime(2025, 1, 1, 0, 0))",
        ),
        (
            Timing.create_with_no_interval(None, dt.timedelta(seconds=1)),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.NONE, time_offset=datetime.timedelta(seconds=1))",
        ),
        (
            Timing.create_with_no_interval(dt.datetime(2025, 1, 1), dt.timedelta(seconds=1)),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.NONE, timestamp=datetime.datetime(2025, 1, 1, 0, 0), time_offset=datetime.timedelta(seconds=1))",
        ),
        (
            Timing.create_with_no_interval(dt.datetime(2025, 1, 1), dt.timedelta()),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.NONE, timestamp=datetime.datetime(2025, 1, 1, 0, 0), time_offset=datetime.timedelta(0))",
        ),
        (
            Timing.create_with_regular_interval(dt.timedelta(milliseconds=1)),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR, sample_interval=datetime.timedelta(microseconds=1000))",
        ),
        (
            Timing.create_with_regular_interval(
                dt.timedelta(milliseconds=1), dt.datetime(2025, 1, 1)
            ),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR, timestamp=datetime.datetime(2025, 1, 1, 0, 0), sample_interval=datetime.timedelta(microseconds=1000))",
        ),
        (
            Timing.create_with_regular_interval(
                dt.timedelta(milliseconds=1), dt.datetime(2025, 1, 1), dt.timedelta(seconds=1)
            ),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR, timestamp=datetime.datetime(2025, 1, 1, 0, 0), time_offset=datetime.timedelta(seconds=1), sample_interval=datetime.timedelta(microseconds=1000))",
        ),
        (
            Timing.create_with_irregular_interval(
                [dt.datetime(2025, 1, 1), dt.datetime(2025, 1, 2)]
            ),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.IRREGULAR, timestamps=[datetime.datetime(2025, 1, 1, 0, 0), datetime.datetime(2025, 1, 2, 0, 0)])",
        ),
    ],
)
def test___various_values___repr___looks_ok(
    value: Timing[Any, Any, Any], expected_repr: str
) -> None:
    assert repr(value) == expected_repr


_VARIOUS_VALUES = [
    Timing.create_with_no_interval(),
    Timing.create_with_no_interval(dt.datetime(2025, 1, 1)),
    Timing.create_with_no_interval(None, dt.timedelta(seconds=1)),
    Timing.create_with_no_interval(dt.datetime(2025, 1, 1), dt.timedelta(seconds=1)),
    Timing.create_with_regular_interval(dt.timedelta(milliseconds=1)),
    Timing.create_with_regular_interval(dt.timedelta(milliseconds=1), dt.datetime(2025, 1, 1)),
    Timing.create_with_regular_interval(
        dt.timedelta(milliseconds=1), dt.datetime(2025, 1, 1), dt.timedelta(seconds=1)
    ),
    Timing.create_with_irregular_interval([dt.datetime(2025, 1, 1), dt.datetime(2025, 1, 2)]),
]


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___copy___makes_shallow_copy(value: Timing[Any, Any, Any]) -> None:
    new_value = copy.copy(value)

    assert_shallow_copy(new_value, value)


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___deepcopy___makes_deep_copy(value: Timing[Any, Any, Any]) -> None:
    new_value = copy.deepcopy(value)

    assert_deep_copy(new_value, value)


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___pickle_unpickle___makes_deep_copy(
    value: Timing[Any, Any, Any],
) -> None:
    new_value = pickle.loads(pickle.dumps(value))

    assert_deep_copy(new_value, value)


def test___timing___pickle___references_public_modules() -> None:
    value = Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))

    value_bytes = pickle.dumps(value)

    assert b"nitypes.waveform" in value_bytes
    assert b"nitypes.waveform._timing" not in value_bytes


###############################################################################
# _append_timing
###############################################################################
@pytest.mark.parametrize(
    "left_offsets, right_offsets",
    [
        ([], []),
        ([dt.timedelta(0)], []),
        ([dt.timedelta(0), dt.timedelta(1)], []),
        ([dt.timedelta(0), dt.timedelta(1), dt.timedelta(2)], []),
        ([dt.timedelta(0)], [dt.timedelta(1)]),
        ([dt.timedelta(0)], [dt.timedelta(1), dt.timedelta(2)]),
        (
            [dt.timedelta(0), dt.timedelta(1)],
            [dt.timedelta(2), dt.timedelta(3)],
        ),
        (
            [dt.timedelta(3), dt.timedelta(2)],
            [dt.timedelta(1), dt.timedelta(0)],
        ),
        (
            [dt.timedelta(0), dt.timedelta(1)],
            [dt.timedelta(1), dt.timedelta(2)],
        ),
        (
            [dt.timedelta(2), dt.timedelta(1)],
            [dt.timedelta(1), dt.timedelta(0)],
        ),
    ],
)
def test___monotonic_timestamps___append_timing___appends_timestamps(
    left_offsets: list[dt.timedelta],
    right_offsets: list[dt.timedelta],
) -> None:
    start_time = dt.datetime.now(dt.timezone.utc)
    left_timestamps = [start_time + offset for offset in left_offsets]
    right_timestamps = [start_time + offset for offset in right_offsets]
    left_timing = Timing.create_with_irregular_interval(left_timestamps)
    right_timing = Timing.create_with_irregular_interval(right_timestamps)

    new_timing = left_timing._append_timing(right_timing)

    assert_type(new_timing, Timing)
    assert isinstance(new_timing, Timing)
    assert new_timing._timestamps == left_timestamps + right_timestamps


@pytest.mark.parametrize(
    "left_offsets, right_offsets",
    [
        ([dt.timedelta(0)], [dt.timedelta(1), dt.timedelta(0)]),
        ([dt.timedelta(1)], [dt.timedelta(0), dt.timedelta(2)]),
        ([dt.timedelta(0), dt.timedelta(1)], [dt.timedelta(0)]),
        ([dt.timedelta(1), dt.timedelta(0)], [dt.timedelta(1)]),
        ([dt.timedelta(0), dt.timedelta(1)], [dt.timedelta(2), dt.timedelta(0)]),
    ],
)
def test___non_monotonic_timestamps___append_timing___raises_value_error(
    left_offsets: list[dt.timedelta],
    right_offsets: list[dt.timedelta],
) -> None:
    start_time = dt.datetime.now(dt.timezone.utc)
    left_timestamps = [start_time + offset for offset in left_offsets]
    right_timestamps = [start_time + offset for offset in right_offsets]
    left_timing = Timing.create_with_irregular_interval(left_timestamps)
    right_timing = Timing.create_with_irregular_interval(right_timestamps)

    with pytest.raises(ValueError) as exc:
        _ = left_timing._append_timing(right_timing)

    assert exc.value.args[0].startswith("The timestamps must be in ascending or descending order.")
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/waveform/_timing/test_hightime.py sha256=ff13c1fb9c8cbc89fa396c887a8516d9192a070998cd9cd6d3467d497827cea1 bytes=25735 -->
## FILE: tests/unit/waveform/_timing/test_hightime.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/waveform/_timing/test_hightime.py`
- sha256: `ff13c1fb9c8cbc89fa396c887a8516d9192a070998cd9cd6d3467d497827cea1`
- bytes: 25735

````python
from __future__ import annotations

import copy
import datetime as dt
import pickle
from typing import Any

import hightime as ht
import pytest
from typing_extensions import assert_type

import nitypes.waveform.errors as wfmex
from nitypes.waveform import SampleIntervalMode, Timing
from tests.unit.waveform._timing._utils import assert_deep_copy, assert_shallow_copy


###############################################################################
# empty
###############################################################################
def test___empty___is_timing() -> None:
    assert_type(Timing.empty, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    assert isinstance(Timing.empty, Timing)


def test___empty___no_timestamp() -> None:
    assert not Timing.empty.has_timestamp
    with pytest.raises(RuntimeError) as exc:
        _ = Timing.empty.timestamp

    assert exc.value.args[0] == "The waveform timing does not have a timestamp."


def test___empty___no_start_time() -> None:
    assert not Timing.empty.has_start_time
    with pytest.raises(RuntimeError) as exc:
        _ = Timing.empty.start_time

    assert exc.value.args[0] == "The waveform timing does not have a timestamp."


def test___empty___no_time_offset() -> None:
    assert not Timing.empty.has_time_offset
    with pytest.raises(RuntimeError) as exc:
        _ = Timing.empty.time_offset

    assert exc.value.args[0] == "The waveform timing does not have a time offset."


def test___empty___no_sample_interval() -> None:
    assert not Timing.empty.has_sample_interval
    with pytest.raises(RuntimeError) as exc:
        _ = Timing.empty.sample_interval

    assert exc.value.args[0] == "The waveform timing does not have a sample interval."


def test___empty___sample_interval_mode_none() -> None:
    assert Timing.empty.sample_interval_mode == SampleIntervalMode.NONE


###############################################################################
# construct
###############################################################################
def test___no_optional_args___construct___creates_empty_timing() -> None:
    timing = Timing(SampleIntervalMode.NONE)

    assert_type(timing, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    assert not timing.has_timestamp
    assert not timing.has_time_offset
    assert not timing.has_sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.NONE


def test___timestamp___construct___creates_timing_with_timestamp() -> None:
    timestamp = ht.datetime.now(dt.timezone.utc)
    timing = Timing(SampleIntervalMode.NONE, timestamp)

    assert_type(timing, Timing[ht.datetime, dt.timedelta, dt.timedelta])
    assert timing.timestamp == timestamp
    assert not timing.has_time_offset
    assert not timing.has_sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.NONE


def test___timestamp___construct___has_start_time() -> None:
    timestamp = ht.datetime.now(dt.timezone.utc)
    timing = Timing(SampleIntervalMode.NONE, timestamp)

    assert timing.has_start_time


def test___time_offset___construct___creates_timing_with_time_offset() -> None:
    time_offset = ht.timedelta(seconds=1.23)
    timing = Timing(SampleIntervalMode.NONE, time_offset=time_offset)

    assert_type(timing, Timing[dt.datetime, ht.timedelta, dt.timedelta])
    assert not timing.has_timestamp
    assert timing.time_offset == time_offset
    assert not timing.has_sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.NONE


def test___sample_interval___construct___creates_timing_with_sample_interval() -> None:
    sample_interval = ht.timedelta(seconds=1e-3)

    timing = Timing(SampleIntervalMode.REGULAR, sample_interval=sample_interval)

    assert_type(timing, Timing[dt.datetime, dt.timedelta, ht.timedelta])
    assert not timing.has_timestamp
    assert not timing.has_time_offset
    assert timing.sample_interval == sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.REGULAR


def test___sample_interval_timestamp_and_time_offset___construct___creates_timing_with_sample_interval_timestamp_and_time_offset() -> (
    None
):
    sample_interval = ht.timedelta(seconds=1e-3)
    timestamp = ht.datetime.now(dt.timezone.utc)
    time_offset = ht.timedelta(seconds=1.23)

    timing = Timing(SampleIntervalMode.REGULAR, timestamp, time_offset, sample_interval)

    assert_type(timing, Timing[ht.datetime, ht.timedelta, ht.timedelta])
    assert timing.timestamp == timestamp
    assert timing.time_offset == time_offset
    assert timing.sample_interval == sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.REGULAR


###############################################################################
# create_with_no_interval
###############################################################################
def test___no_args___create_with_no_interval___creates_empty_timing() -> None:
    timing = Timing.create_with_no_interval()

    assert_type(timing, Timing[dt.datetime, dt.timedelta, dt.timedelta])
    assert not timing.has_timestamp
    assert not timing.has_time_offset
    assert not timing.has_sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.NONE


def test___timestamp___create_with_no_interval___creates_timing_with_timestamp() -> None:
    timestamp = ht.datetime.now(dt.timezone.utc)
    timing = Timing.create_with_no_interval(timestamp)

    assert_type(timing, Timing[ht.datetime, dt.timedelta, dt.timedelta])
    assert timing.timestamp == timestamp
    assert not timing.has_time_offset
    assert not timing.has_sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.NONE


def test___timestamp_and_time_offset___create_with_no_interval___creates_timing_with_timestamp_and_time_offset() -> (
    None
):
    timestamp = ht.datetime.now(dt.timezone.utc)
    time_offset = ht.timedelta(seconds=1.23)
    timing = Timing.create_with_no_interval(timestamp, time_offset)

    assert_type(timing, Timing[ht.datetime, ht.timedelta, dt.timedelta])
    assert timing.timestamp == timestamp
    assert timing.time_offset == time_offset
    assert not timing.has_sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.NONE


def test___time_offset___create_with_no_interval___creates_timing_with_time_offset() -> None:
    time_offset = ht.timedelta(seconds=1.23)
    timing = Timing.create_with_no_interval(time_offset=time_offset)

    assert_type(timing, Timing[dt.datetime, ht.timedelta, dt.timedelta])
    assert not timing.has_timestamp
    assert timing.time_offset == time_offset
    assert not timing.has_sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.NONE


###############################################################################
# create_with_regular_interval
###############################################################################
def test___sample_interval___create_with_regular_interval___creates_timing_with_sample_interval() -> (
    None
):
    sample_interval = ht.timedelta(milliseconds=1)

    timing = Timing.create_with_regular_interval(sample_interval)

    assert_type(timing, Timing[dt.datetime, dt.timedelta, ht.timedelta])
    assert not timing.has_timestamp
    assert not timing.has_time_offset
    assert timing.sample_interval == sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.REGULAR


def test___sample_interval_and_timestamp___create_with_regular_interval___creates_timing_with_sample_interval_and_timestamp() -> (
    None
):
    sample_interval = ht.timedelta(milliseconds=1)
    timestamp = ht.datetime.now(dt.timezone.utc)

    timing = Timing.create_with_regular_interval(sample_interval, timestamp)

    assert_type(timing, Timing[ht.datetime, dt.timedelta, ht.timedelta])
    assert timing.timestamp == timestamp
    assert not timing.has_time_offset
    assert timing.sample_interval == sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.REGULAR


def test___sample_interval_timestamp_and_time_offset___create_with_regular_interval___creates_timing_with_sample_interval_timestamp_and_time_offset() -> (
    None
):
    sample_interval = ht.timedelta(milliseconds=1)
    timestamp = ht.datetime.now(dt.timezone.utc)
    time_offset = ht.timedelta(seconds=1.23)

    timing = Timing.create_with_regular_interval(sample_interval, timestamp, time_offset)

    assert_type(timing, Timing[ht.datetime, ht.timedelta, ht.timedelta])
    assert timing.timestamp == timestamp
    assert timing.time_offset == time_offset
    assert timing.sample_interval == sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.REGULAR


def test___sample_interval_and_time_offset___create_with_regular_interval___creates_timing_with_sample_interval_and_time_offset() -> (
    None
):
    sample_interval = ht.timedelta(milliseconds=1)
    time_offset = ht.timedelta(seconds=1.23)

    timing = Timing.create_with_regular_interval(sample_interval, time_offset=time_offset)

    assert_type(timing, Timing[dt.datetime, ht.timedelta, ht.timedelta])
    assert not timing.has_timestamp
    assert timing.time_offset == time_offset
    assert timing.sample_interval == sample_interval
    assert timing.sample_interval_mode == SampleIntervalMode.REGULAR


###############################################################################
# create_with_irregular_interval
###############################################################################
@pytest.mark.parametrize(
    "time_offsets",
    [
        [],
        [ht.timedelta(0)],
        [ht.timedelta(0), ht.timedelta(0)],
        [ht.timedelta(0), ht.timedelta(1)],
        [ht.timedelta(0), ht.timedelta(1), ht.timedelta(2)],
        [
            ht.timedelta(0),
            ht.timedelta(1),
            ht.timedelta(2),
            ht.timedelta(3),
        ],
        [
            ht.timedelta(3),
            ht.timedelta(2),
            ht.timedelta(1),
            ht.timedelta(0),
        ],
        [ht.timedelta(0, 0, 1), ht.timedelta(0, 1, 0), ht.timedelta(1, 0, 0)],
        [ht.timedelta(1, 0, 0), ht.timedelta(0, 1, 0), ht.timedelta(0, 0, 1)],
        [
            ht.timedelta(0),
            ht.timedelta(1),
            ht.timedelta(1),
            ht.timedelta(2),
        ],
    ],
)
def test___monotonic_timestamps___create_with_irregular_interval___creates_timing_with_timestamps(
    time_offsets: list[ht.timedelta],
) -> None:
    start_time = ht.datetime.now(dt.timezone.utc)
    timestamps = [start_time + offset for offset in time_offsets]

    timing = Timing.create_with_irregular_interval(timestamps)

    assert_type(timing, Timing[ht.datetime, dt.timedelta, dt.timedelta])
    assert timing.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert timing._timestamps == timestamps


@pytest.mark.parametrize(
    "time_offsets",
    [
        [ht.timedelta(0), ht.timedelta(1), ht.timedelta(0)],
        [ht.timedelta(1), ht.timedelta(0), ht.timedelta(1)],
    ],
)
def test___non_monotonic_timestamps___create_with_irregular_interval___raises_value_error(
    time_offsets: list[ht.timedelta],
) -> None:
    start_time = ht.datetime.now(dt.timezone.utc)
    timestamps = [start_time + offset for offset in time_offsets]

    with pytest.raises(ValueError) as exc:
        _ = Timing.create_with_irregular_interval(timestamps)

    assert exc.value.args[0].startswith("The timestamps must be in ascending or descending order.")


def test___timestamps_tuple___create_with_irregular_interval___creates_timing_with_timestamps() -> (
    None
):
    start_time = ht.datetime.now(dt.timezone.utc)
    timestamps = (start_time,)

    timing = Timing.create_with_irregular_interval(timestamps)

    assert_type(timing, Timing[ht.datetime, dt.timedelta, dt.timedelta])
    assert timing.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert timing._timestamps == list(timestamps)


###############################################################################
# get_timestamps
###############################################################################
def test___no_interval___get_timestamps___raises_correct_error() -> None:
    start_time = ht.datetime.now(dt.timezone.utc)
    timing = Timing.create_with_no_interval(start_time)

    with pytest.raises(wfmex.NoTimestampInformationError) as exc:
        _ = timing.get_timestamps(0, 5)

    assert exc.value.args[0].startswith(
        "The waveform timing does not have valid timestamp information."
    )


def test___regular_interval___get_timestamps___gets_timestamps() -> None:
    start_time = ht.datetime.now(dt.timezone.utc)
    sample_interval = ht.timedelta(milliseconds=1)
    timing = Timing.create_with_regular_interval(sample_interval, start_time)

    assert list(timing.get_timestamps(3, 4)) == [
        start_time + 3 * sample_interval,
        start_time + 4 * sample_interval,
        start_time + 5 * sample_interval,
        start_time + 6 * sample_interval,
    ]


def test___irregular_interval___get_timestamps___gets_timestamps() -> None:
    start_time = ht.datetime.now(dt.timezone.utc)
    sample_interval = ht.timedelta(milliseconds=1)
    timestamps = [start_time + i * sample_interval for i in range(10)]
    timing = Timing.create_with_irregular_interval(timestamps)

    assert list(timing.get_timestamps(0, 10)) == timestamps


def test___irregular_interval_subset___get_timestamps___gets_timestamps() -> None:
    start_time = ht.datetime.now(dt.timezone.utc)
    sample_interval = ht.timedelta(milliseconds=1)
    timestamps = [start_time + i * sample_interval for i in range(10)]
    timing = Timing.create_with_irregular_interval(timestamps)

    assert list(timing.get_timestamps(3, 4)) == timestamps[3:7]


###############################################################################
# magic methods
###############################################################################
@pytest.mark.parametrize(
    "left, right",
    [
        (Timing.create_with_no_interval(), Timing.create_with_no_interval()),
        (
            Timing.create_with_no_interval(ht.datetime(2025, 1, 1)),
            Timing.create_with_no_interval(ht.datetime(2025, 1, 1)),
        ),
        (
            Timing.create_with_no_interval(None, ht.timedelta(seconds=1)),
            Timing.create_with_no_interval(None, ht.timedelta(seconds=1)),
        ),
        (
            Timing.create_with_no_interval(ht.datetime(2025, 1, 1), ht.timedelta(seconds=1)),
            Timing.create_with_no_interval(ht.datetime(2025, 1, 1), ht.timedelta(seconds=1)),
        ),
        (
            Timing.create_with_regular_interval(ht.timedelta(milliseconds=1)),
            Timing.create_with_regular_interval(ht.timedelta(milliseconds=1)),
        ),
        (
            Timing.create_with_regular_interval(
                ht.timedelta(milliseconds=1), ht.datetime(2025, 1, 1)
            ),
            Timing.create_with_regular_interval(
                ht.timedelta(milliseconds=1), ht.datetime(2025, 1, 1)
            ),
        ),
        (
            Timing.create_with_regular_interval(
                ht.timedelta(milliseconds=1), ht.datetime(2025, 1, 1), ht.timedelta(seconds=1)
            ),
            Timing.create_with_regular_interval(
                ht.timedelta(milliseconds=1), ht.datetime(2025, 1, 1), ht.timedelta(seconds=1)
            ),
        ),
        (
            Timing.create_with_irregular_interval(
                [ht.datetime(2025, 1, 1), ht.datetime(2025, 1, 2)]
            ),
            Timing.create_with_irregular_interval(
                [ht.datetime(2025, 1, 1), ht.datetime(2025, 1, 2)]
            ),
        ),
    ],
)
def test___same_value___equality___equal(
    left: Timing[Any, Any, Any], right: Timing[Any, Any, Any]
) -> None:
    assert left == right
    assert not (left != right)


@pytest.mark.parametrize(
    "left, right",
    [
        (
            Timing.create_with_no_interval(ht.datetime(2025, 1, 1), ht.timedelta(seconds=1)),
            Timing.create_with_no_interval(ht.datetime(2025, 1, 2), ht.timedelta(seconds=1)),
        ),
        (
            Timing.create_with_no_interval(ht.datetime(2025, 1, 1), ht.timedelta(seconds=1)),
            Timing.create_with_no_interval(ht.datetime(2025, 1, 1), ht.timedelta(seconds=2)),
        ),
        (
            Timing.create_with_regular_interval(
                ht.timedelta(milliseconds=1), ht.datetime(2025, 1, 1), ht.timedelta(seconds=1)
            ),
            Timing.create_with_regular_interval(
                ht.timedelta(milliseconds=2), ht.datetime(2025, 1, 1), ht.timedelta(seconds=1)
            ),
        ),
        (
            Timing.create_with_regular_interval(
                ht.timedelta(milliseconds=1), ht.datetime(2025, 1, 1), ht.timedelta(seconds=1)
            ),
            Timing.create_with_regular_interval(
                ht.timedelta(milliseconds=1), ht.datetime(2025, 1, 2), ht.timedelta(seconds=1)
            ),
        ),
        (
            Timing.create_with_regular_interval(
                ht.timedelta(milliseconds=1), ht.datetime(2025, 1, 1), ht.timedelta(seconds=1)
            ),
            Timing.create_with_regular_interval(
                ht.timedelta(milliseconds=1), ht.datetime(2025, 1, 1), ht.timedelta(seconds=2)
            ),
        ),
        (
            Timing.create_with_irregular_interval(
                [ht.datetime(2025, 1, 1), ht.datetime(2025, 1, 2)]
            ),
            Timing.create_with_irregular_interval(
                [ht.datetime(2025, 1, 3), ht.datetime(2025, 1, 2)]
            ),
        ),
    ],
)
def test___different_value___equality___not_equal(
    left: Timing[Any, Any, Any],
    right: Timing[Any, Any, Any],
) -> None:
    assert not (left == right)
    assert left != right


@pytest.mark.parametrize(
    "value, expected_repr",
    [
        (
            Timing.create_with_no_interval(),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.NONE)",
        ),
        (
            Timing.create_with_no_interval(ht.datetime(2025, 1, 1)),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.NONE, timestamp=hightime.datetime(2025, 1, 1, 0, 0))",
        ),
        (
            Timing.create_with_no_interval(None, ht.timedelta(seconds=1)),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.NONE, time_offset=hightime.timedelta(seconds=1))",
        ),
        (
            Timing.create_with_no_interval(ht.datetime(2025, 1, 1), ht.timedelta(seconds=1)),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.NONE, timestamp=hightime.datetime(2025, 1, 1, 0, 0), time_offset=hightime.timedelta(seconds=1))",
        ),
        (
            Timing.create_with_no_interval(ht.datetime(2025, 1, 1), ht.timedelta()),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.NONE, timestamp=hightime.datetime(2025, 1, 1, 0, 0), time_offset=hightime.timedelta())",
        ),
        (
            Timing.create_with_regular_interval(ht.timedelta(milliseconds=1)),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR, sample_interval=hightime.timedelta(microseconds=1000))",
        ),
        (
            Timing.create_with_regular_interval(
                ht.timedelta(milliseconds=1), ht.datetime(2025, 1, 1)
            ),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR, timestamp=hightime.datetime(2025, 1, 1, 0, 0), sample_interval=hightime.timedelta(microseconds=1000))",
        ),
        (
            Timing.create_with_regular_interval(
                ht.timedelta(milliseconds=1), ht.datetime(2025, 1, 1), ht.timedelta(seconds=1)
            ),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR, timestamp=hightime.datetime(2025, 1, 1, 0, 0), time_offset=hightime.timedelta(seconds=1), sample_interval=hightime.timedelta(microseconds=1000))",
        ),
        (
            Timing.create_with_irregular_interval(
                [ht.datetime(2025, 1, 1), ht.datetime(2025, 1, 2)]
            ),
            "nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.IRREGULAR, timestamps=[hightime.datetime(2025, 1, 1, 0, 0), hightime.datetime(2025, 1, 2, 0, 0)])",
        ),
    ],
)
def test___various_values___repr___looks_ok(
    value: Timing[Any, Any, Any], expected_repr: str
) -> None:
    assert repr(value) == expected_repr


_VARIOUS_VALUES = [
    Timing.create_with_no_interval(),
    Timing.create_with_no_interval(ht.datetime(2025, 1, 1)),
    Timing.create_with_no_interval(None, ht.timedelta(seconds=1)),
    Timing.create_with_no_interval(ht.datetime(2025, 1, 1), ht.timedelta(seconds=1)),
    Timing.create_with_regular_interval(ht.timedelta(milliseconds=1)),
    Timing.create_with_regular_interval(ht.timedelta(milliseconds=1), ht.datetime(2025, 1, 1)),
    Timing.create_with_regular_interval(
        ht.timedelta(milliseconds=1), ht.datetime(2025, 1, 1), ht.timedelta(seconds=1)
    ),
    Timing.create_with_irregular_interval([ht.datetime(2025, 1, 1), ht.datetime(2025, 1, 2)]),
]


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___copy___makes_shallow_copy(value: Timing[Any, Any, Any]) -> None:
    new_value = copy.copy(value)

    assert_shallow_copy(new_value, value)


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___deepcopy___makes_deep_copy(value: Timing[Any, Any, Any]) -> None:
    new_value = copy.deepcopy(value)

    assert_deep_copy(new_value, value)


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___pickle_unpickle___makes_deep_copy(
    value: Timing[Any, Any, Any],
) -> None:
    new_value = pickle.loads(pickle.dumps(value))

    assert_deep_copy(new_value, value)


def test___timing___pickle___references_public_modules() -> None:
    value = Timing.create_with_regular_interval(ht.timedelta(milliseconds=1))

    value_bytes = pickle.dumps(value)

    assert b"nitypes.waveform" in value_bytes
    assert b"nitypes.waveform._timing" not in value_bytes


###############################################################################
# _append_timing
###############################################################################
@pytest.mark.parametrize(
    "left_offsets, right_offsets",
    [
        ([], []),
        ([ht.timedelta(0)], []),
        ([ht.timedelta(0), ht.timedelta(1)], []),
        ([ht.timedelta(0), ht.timedelta(1), ht.timedelta(2)], []),
        ([ht.timedelta(0)], [ht.timedelta(1)]),
        ([ht.timedelta(0)], [ht.timedelta(1), ht.timedelta(2)]),
        (
            [ht.timedelta(0), ht.timedelta(1)],
            [ht.timedelta(2), ht.timedelta(3)],
        ),
        (
            [ht.timedelta(3), ht.timedelta(2)],
            [ht.timedelta(1), ht.timedelta(0)],
        ),
        (
            [ht.timedelta(0), ht.timedelta(1)],
            [ht.timedelta(1), ht.timedelta(2)],
        ),
        (
            [ht.timedelta(2), ht.timedelta(1)],
            [ht.timedelta(1), ht.timedelta(0)],
        ),
    ],
)
def test___monotonic_timestamps___append_timing___appends_timestamps(
    left_offsets: list[ht.timedelta],
    right_offsets: list[ht.timedelta],
) -> None:
    start_time = ht.datetime.now(dt.timezone.utc)
    left_timestamps = [start_time + offset for offset in left_offsets]
    right_timestamps = [start_time + offset for offset in right_offsets]
    left_timing = Timing.create_with_irregular_interval(left_timestamps)
    right_timing = Timing.create_with_irregular_interval(right_timestamps)

    new_timing = left_timing._append_timing(right_timing)

    assert_type(new_timing, Timing[ht.datetime, dt.timedelta, dt.timedelta])
    assert isinstance(new_timing, Timing)
    assert new_timing._timestamps == left_timestamps + right_timestamps


@pytest.mark.parametrize(
    "left_offsets, right_offsets",
    [
        ([ht.timedelta(0)], [ht.timedelta(1), ht.timedelta(0)]),
        ([ht.timedelta(1)], [ht.timedelta(0), ht.timedelta(2)]),
        ([ht.timedelta(0), ht.timedelta(1)], [ht.timedelta(0)]),
        ([ht.timedelta(1), ht.timedelta(0)], [ht.timedelta(1)]),
        ([ht.timedelta(0), ht.timedelta(1)], [ht.timedelta(2), ht.timedelta(0)]),
    ],
)
def test___non_monotonic_timestamps___append_timing___raises_value_error(
    left_offsets: list[ht.timedelta],
    right_offsets: list[ht.timedelta],
) -> None:
    start_time = ht.datetime.now(dt.timezone.utc)
    left_timestamps = [start_time + offset for offset in left_offsets]
    right_timestamps = [start_time + offset for offset in right_offsets]
    left_timing = Timing.create_with_irregular_interval(left_timestamps)
    right_timing = Timing.create_with_irregular_interval(right_timestamps)

    with pytest.raises(ValueError) as exc:
        _ = left_timing._append_timing(right_timing)

    assert exc.value.args[0].startswith("The timestamps must be in ascending or descending order.")
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/waveform/test_analog_waveform.py sha256=43ad304232c66e3c1dab707e66ef012dfc116fa694e5e7f1746876513f7ae639 bytes=80255 -->
## FILE: tests/unit/waveform/test_analog_waveform.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/waveform/test_analog_waveform.py`
- sha256: `43ad304232c66e3c1dab707e66ef012dfc116fa694e5e7f1746876513f7ae639`
- bytes: 80255

````python
from __future__ import annotations

import array
import copy
import datetime as dt
import itertools
import pickle
import sys
import weakref
from collections.abc import Sequence
from typing import Any, SupportsIndex, Union

import hightime as ht
import numpy as np
import numpy.typing as npt
import pytest
from packaging.version import Version
from typing_extensions import assert_type

import nitypes.bintime as bt
import nitypes.waveform.errors as wfmex
import nitypes.waveform.warnings as wfmwarn
from nitypes.waveform import (
    NO_SCALING,
    AnalogWaveform,
    LinearScaleMode,
    NoneScaleMode,
    SampleIntervalMode,
    ScaleMode,
    Timing,
)


###############################################################################
# create
###############################################################################
def test___no_args___create___creates_empty_waveform_with_default_dtype() -> None:
    waveform = AnalogWaveform()

    assert waveform.sample_count == waveform.capacity == len(waveform.raw_data) == 0
    assert waveform.dtype == np.float64
    assert_type(waveform, AnalogWaveform[np.float64])


def test___sample_count___create___creates_waveform_with_sample_count_and_default_dtype() -> None:
    waveform = AnalogWaveform(10)

    assert waveform.sample_count == waveform.capacity == len(waveform.raw_data) == 10
    assert waveform.dtype == np.float64
    assert_type(waveform, AnalogWaveform[np.float64])


def test___sample_count_and_dtype___create___creates_waveform_with_sample_count_and_dtype() -> None:
    waveform = AnalogWaveform(10, np.int32)

    assert waveform.sample_count == waveform.capacity == len(waveform.raw_data) == 10
    assert waveform.dtype == np.int32
    assert_type(waveform, AnalogWaveform[np.int32])


def test___sample_count_and_dtype_str___create___creates_waveform_with_sample_count_and_dtype() -> (
    None
):
    waveform = AnalogWaveform(10, "i4")

    assert waveform.sample_count == waveform.capacity == len(waveform.raw_data) == 10
    assert waveform.dtype == np.int32
    assert_type(waveform, AnalogWaveform[Any])  # dtype not inferred from string


def test___sample_count_and_dtype_any___create___creates_waveform_with_sample_count_and_dtype() -> (
    None
):
    dtype: np.dtype[Any] = np.dtype(np.int32)
    waveform = AnalogWaveform(10, dtype)

    assert waveform.sample_count == waveform.capacity == len(waveform.raw_data) == 10
    assert waveform.dtype == np.int32
    assert_type(waveform, AnalogWaveform[Any])  # dtype not inferred from np.dtype[Any]


def test___sample_count_dtype_and_capacity___create___creates_waveform_with_sample_count_dtype_and_capacity() -> (
    None
):
    waveform = AnalogWaveform(10, np.int32, capacity=20)

    assert waveform.sample_count == len(waveform.raw_data) == 10
    assert waveform.capacity == 20
    assert waveform.dtype == np.int32
    assert_type(waveform, AnalogWaveform[np.int32])


@pytest.mark.parametrize("dtype", [np.complex128, np.str_, np.void, "i2, i2"])
def test___sample_count_and_unsupported_dtype___create___raises_type_error(
    dtype: npt.DTypeLike,
) -> None:
    with pytest.raises(TypeError) as exc:
        _ = AnalogWaveform(10, dtype)

    assert exc.value.args[0].startswith("The requested data type is not supported.")


def test___dtype_str_with_unsupported_traw_hint___create___mypy_type_var_warning() -> None:
    waveform1: AnalogWaveform[np.complex128] = AnalogWaveform(dtype="int32")  # type: ignore[type-var]
    waveform2: AnalogWaveform[np.str_] = AnalogWaveform(dtype="int32")  # type: ignore[type-var]
    waveform3: AnalogWaveform[np.void] = AnalogWaveform(dtype="int32")  # type: ignore[type-var]
    _ = waveform1, waveform2, waveform3


def test___dtype_str_with_traw_hint___create___narrows_traw() -> None:
    waveform: AnalogWaveform[np.int32] = AnalogWaveform(dtype="int32")

    assert_type(waveform, AnalogWaveform[np.int32])


###############################################################################
# from_array_1d
###############################################################################
def test___float64_ndarray___from_array_1d___creates_waveform_with_float64_dtype() -> None:
    data = np.array([1.1, 2.2, 3.3, 4.4, 5.5], np.float64)

    waveform = AnalogWaveform.from_array_1d(data)

    assert waveform.raw_data.tolist() == data.tolist()
    assert waveform.dtype == np.float64
    assert_type(waveform, AnalogWaveform[np.float64])


def test___int32_ndarray___from_array_1d___creates_waveform_with_int32_dtype() -> None:
    data = np.array([1, 2, 3, 4, 5], np.int32)

    waveform = AnalogWaveform.from_array_1d(data)

    assert waveform.raw_data.tolist() == data.tolist()
    assert waveform.dtype == np.int32
    assert_type(waveform, AnalogWaveform[np.int32])


def test___int32_array_with_dtype___from_array_1d___creates_waveform_with_specified_dtype() -> None:
    data = array.array("i", [1, 2, 3, 4, 5])

    waveform = AnalogWaveform.from_array_1d(data, np.int32)

    assert waveform.raw_data.tolist() == data.tolist()
    assert waveform.dtype == np.int32
    assert_type(waveform, AnalogWaveform[np.int32])


def test___int16_ndarray_with_mismatched_dtype___from_array_1d___creates_waveform_with_specified_dtype() -> (
    None
):
    data = np.array([1, 2, 3, 4, 5], np.int16)

    waveform = AnalogWaveform.from_array_1d(data, np.int32)

    assert waveform.raw_data.tolist() == data.tolist()
    assert waveform.dtype == np.int32
    assert_type(waveform, AnalogWaveform[np.int32])


def test___int_list_with_dtype___from_array_1d___creates_waveform_with_specified_dtype() -> None:
    data = [1, 2, 3, 4, 5]

    waveform = AnalogWaveform.from_array_1d(data, np.int32)

    assert waveform.raw_data.tolist() == data
    assert waveform.dtype == np.int32
    assert_type(waveform, AnalogWaveform[np.int32])


def test___int_list_with_dtype_str___from_array_1d___creates_waveform_with_specified_dtype() -> (
    None
):
    data = [1, 2, 3, 4, 5]

    waveform = AnalogWaveform.from_array_1d(data, "int32")

    assert waveform.raw_data.tolist() == data
    assert waveform.dtype == np.int32
    assert_type(waveform, AnalogWaveform[Any])  # dtype not inferred from string


def test___int32_ndarray_2d___from_array_1d___raises_value_error() -> None:
    data = np.array([[1, 2, 3], [4, 5, 6]], np.int32)

    with pytest.raises(ValueError) as exc:
        _ = AnalogWaveform.from_array_1d(data)

    assert exc.value.args[0].startswith(
        "The input array must be a one-dimensional array or sequence."
    )


def test___int_list_without_dtype___from_array_1d___raises_value_error() -> None:
    data = [1, 2, 3, 4, 5]

    with pytest.raises(ValueError) as exc:
        _ = AnalogWaveform.from_array_1d(data)

    assert exc.value.args[0].startswith(
        "You must specify a dtype when the input array is a sequence."
    )


def test___bytes___from_array_1d___raises_value_error() -> None:
    data = b"\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00"

    with pytest.raises(ValueError) as exc:
        _ = AnalogWaveform.from_array_1d(data, np.int32)

    assert exc.value.args[0].startswith("invalid literal for int() with base 10:")


def test___iterable___from_array_1d___raises_type_error() -> None:
    data = itertools.repeat(3)

    with pytest.raises(TypeError) as exc:
        _ = AnalogWaveform.from_array_1d(data, np.int32)  # type: ignore[call-overload]

    assert exc.value.args[0].startswith(
        "The input array must be a one-dimensional array or sequence."
    )


def test___ndarray_with_unsupported_dtype___from_array_1d___raises_type_error() -> None:
    data = np.zeros(3, np.str_)

    with pytest.raises(TypeError) as exc:
        _ = AnalogWaveform.from_array_1d(data)

    assert exc.value.args[0].startswith("The requested data type is not supported.")


def test___copy___from_array_1d___creates_waveform_linked_to_different_buffer() -> None:
    data = np.array([1, 2, 3, 4, 5], np.int32)

    waveform = AnalogWaveform.from_array_1d(data, copy=True)

    assert waveform._data is not data
    assert waveform.raw_data.tolist() == data.tolist()
    data[:] = [5, 4, 3, 2, 1]
    assert waveform.raw_data.tolist() != data.tolist()


def test___int32_ndarray_no_copy___from_array_1d___creates_waveform_linked_to_same_buffer() -> None:
    data = np.array([1, 2, 3, 4, 5], np.int32)

    waveform = AnalogWaveform.from_array_1d(data, copy=False)

    assert waveform._data is data
    assert waveform.raw_data.tolist() == data.tolist()
    data[:] = [5, 4, 3, 2, 1]
    assert waveform.raw_data.tolist() == data.tolist()


def test___int32_array_no_copy___from_array_1d___creates_waveform_linked_to_same_buffer() -> None:
    data = array.array("i", [1, 2, 3, 4, 5])

    waveform = AnalogWaveform.from_array_1d(data, dtype=np.int32, copy=False)

    assert waveform.raw_data.tolist() == data.tolist()
    data[:] = array.array("i", [5, 4, 3, 2, 1])
    assert waveform.raw_data.tolist() == data.tolist()


def test___int_list_no_copy___from_array_1d___raises_value_error() -> None:
    data = [1, 2, 3, 4, 5]

    with pytest.raises(ValueError) as exc:
        _ = AnalogWaveform.from_array_1d(data, np.int32, copy=False)

    assert exc.value.args[0].startswith(
        "Unable to avoid copy while creating an array as requested."
    )


@pytest.mark.parametrize(
    "start_index, sample_count, expected_data",
    [
        (0, None, [1, 2, 3, 4, 5]),
        (1, None, [2, 3, 4, 5]),
        (4, None, [5]),
        (5, None, []),
        (0, 1, [1]),
        (0, 4, [1, 2, 3, 4]),
        (1, 1, [2]),
        (1, 3, [2, 3, 4]),
        (1, 4, [2, 3, 4, 5]),
    ],
)
def test___array_subset___from_array_1d___creates_waveform_with_array_subset(
    start_index: SupportsIndex, sample_count: SupportsIndex | None, expected_data: list[int]
) -> None:
    data = np.array([1, 2, 3, 4, 5], np.int32)

    waveform = AnalogWaveform.from_array_1d(
        data, start_index=start_index, sample_count=sample_count
    )

    assert waveform.raw_data.tolist() == expected_data


@pytest.mark.parametrize(
    "start_index, sample_count, expected_message, exception_type",
    [
        (-2, None, "The start index must be a non-negative integer.", ValueError),
        (-1, None, "The start index must be a non-negative integer.", ValueError),
        (
            6,
            None,
            "The start index must be less than or equal to the input array length.",
            wfmex.StartIndexTooLargeError,
        ),
        (0, -2, "The sample count must be a non-negative integer.", ValueError),
        (0, -1, "The sample count must be a non-negative integer.", ValueError),
        (
            0,
            6,
            "The sum of the start index and sample count must be less than or equal to the input array length.",
            wfmex.StartIndexOrSampleCountTooLargeError,
        ),
        (
            1,
            5,
            "The sum of the start index and sample count must be less than or equal to the input array length.",
            wfmex.StartIndexOrSampleCountTooLargeError,
        ),
        (
            5,
            1,
            "The sum of the start index and sample count must be less than or equal to the input array length.",
            wfmex.StartIndexOrSampleCountTooLargeError,
        ),
    ],
)
def test___invalid_array_subset___from_array_1d___raises_correct_error(
    start_index: SupportsIndex,
    sample_count: SupportsIndex | None,
    expected_message: str,
    exception_type: type[Exception],
) -> None:
    data = np.array([1, 2, 3, 4, 5], np.int32)

    with pytest.raises(exception_type) as exc:
        _ = AnalogWaveform.from_array_1d(data, start_index=start_index, sample_count=sample_count)

    assert exc.value.args[0].startswith(expected_message)


###############################################################################
# from_array_2d
###############################################################################
def test___float64_ndarray___from_array_2d___creates_waveform_with_float64_dtype() -> None:
    data = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]], np.float64)

    waveforms = AnalogWaveform.from_array_2d(data)

    assert_type(waveforms, Sequence[AnalogWaveform[np.float64]])
    assert len(waveforms) == 2
    for i in range(len(waveforms)):
        assert waveforms[i].raw_data.tolist() == data[i].tolist()
        assert waveforms[i].dtype == np.float64
        assert_type(waveforms[i], AnalogWaveform[np.float64])


def test___int32_ndarray___from_array_2d___creates_waveform_with_int32_dtype() -> None:
    data = np.array([[1, 2, 3], [4, 5, 6]], np.int32)

    waveforms = AnalogWaveform.from_array_2d(data)

    assert_type(waveforms, Sequence[AnalogWaveform[np.int32]])
    assert len(waveforms) == 2
    for i in range(len(waveforms)):
        assert waveforms[i].raw_data.tolist() == data[i].tolist()
        assert waveforms[i].dtype == np.int32
        assert_type(waveforms[i], AnalogWaveform[np.int32])


def test___int16_ndarray_with_mismatched_dtype___from_array_2d___creates_waveform_with_specified_dtype() -> (
    None
):
    data = np.array([[1, 2, 3], [4, 5, 6]], np.int16)

    waveforms = AnalogWaveform.from_array_2d(data, np.int32)

    assert_type(waveforms, Sequence[AnalogWaveform[np.int32]])
    assert len(waveforms) == 2
    for i in range(len(waveforms)):
        assert waveforms[i].raw_data.tolist() == data[i].tolist()
        assert waveforms[i].dtype == np.int32
        assert_type(waveforms[i], AnalogWaveform[np.int32])


def test___int32_array_list_with_dtype___from_array_2d___creates_waveform_with_specified_dtype() -> (
    None
):
    data = [array.array("i", [1, 2, 3]), array.array("i", [4, 5, 6])]

    waveforms = AnalogWaveform.from_array_2d(data, np.int32)

    assert_type(waveforms, Sequence[AnalogWaveform[np.int32]])
    assert len(waveforms) == 2
    for i in range(len(waveforms)):
        assert waveforms[i].raw_data.tolist() == data[i].tolist()
        assert waveforms[i].dtype == np.int32
        assert_type(waveforms[i], AnalogWaveform[np.int32])


def test___int_list_list_with_dtype___from_array_2d___creates_waveform_with_specified_dtype() -> (
    None
):
    data = [[1, 2, 3], [4, 5, 6]]

    waveforms = AnalogWaveform.from_array_2d(data, np.int32)

    assert_type(waveforms, Sequence[AnalogWaveform[np.int32]])
    assert len(waveforms) == 2
    for i in range(len(waveforms)):
        assert waveforms[i].raw_data.tolist() == data[i]
        assert waveforms[i].dtype == np.int32
        assert_type(waveforms[i], AnalogWaveform[np.int32])


def test___int_list_list_with_dtype_str___from_array_2d___creates_waveform_with_specified_dtype() -> (
    None
):
    data = [[1, 2, 3], [4, 5, 6]]

    waveforms = AnalogWaveform.from_array_2d(data, "int32")

    assert_type(waveforms, Sequence[AnalogWaveform[Any]])  # dtype not inferred from string
    assert len(waveforms) == 2
    for i in range(len(waveforms)):
        assert waveforms[i].raw_data.tolist() == data[i]
        assert waveforms[i].dtype == np.int32
        assert_type(waveforms[i], AnalogWaveform[Any])  # dtype not inferred from string


def test___int32_ndarray_1d___from_array_2d___raises_value_error() -> None:
    data = np.array([1, 2, 3, 4, 5], np.int32)

    with pytest.raises(ValueError) as exc:
        _ = AnalogWaveform.from_array_2d(data)

    assert exc.value.args[0].startswith(
        "The input array must be a two-dimensional array or nested sequence."
    )


def test___int_list_list_without_dtype___from_array_2d___raises_value_error() -> None:
    data = [[1, 2, 3], [4, 5, 6]]

    with pytest.raises(ValueError) as exc:
        _ = AnalogWaveform.from_array_2d(data)

    assert exc.value.args[0].startswith(
        "You must specify a dtype when the input array is a sequence."
    )


def test___bytes_list___from_array_2d___raises_value_error() -> None:
    data = [
        b"\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00",
        b"\x04\x00\x00\x00\x05\x00\x00\x00\x06\x00\x00\x00",
    ]

    with pytest.raises(ValueError) as exc:
        _ = AnalogWaveform.from_array_2d(data, np.int32)

    assert exc.value.args[0].startswith("invalid literal for int() with base 10:")


def test___list_iterable___from_array_2d___raises_type_error() -> None:
    data = itertools.repeat([3])

    with pytest.raises(TypeError) as exc:
        _ = AnalogWaveform.from_array_2d(data, np.int32)  # type: ignore[call-overload]

    assert exc.value.args[0].startswith(
        "The input array must be a two-dimensional array or nested sequence."
    )


def test___iterable_list___from_array_2d___raises_type_error() -> None:
    data = [itertools.repeat(3), itertools.repeat(4)]

    with pytest.raises(TypeError) as exc:
        _ = AnalogWaveform.from_array_2d(data, np.int32)  # type: ignore[arg-type]

    assert exc.value.args[0].startswith("int() argument must be")


def test___ndarray_with_unsupported_dtype___from_array_2d___raises_type_error() -> None:
    data = np.zeros((2, 3), np.str_)

    with pytest.raises(TypeError) as exc:
        _ = AnalogWaveform.from_array_2d(data)

    assert exc.value.args[0].startswith("The requested data type is not supported.")


def test___copy___from_array_2d___creates_waveform_linked_to_different_buffer() -> None:
    data = np.array([[1, 2, 3], [4, 5, 6]], np.int32)

    waveforms = AnalogWaveform.from_array_2d(data, copy=True)

    assert len(waveforms) == 2
    for i in range(len(waveforms)):
        assert waveforms[i].raw_data.tolist() == data[i].tolist()
    data[0][:] = [3, 2, 1]
    data[1][:] = [6, 5, 4]
    for i in range(len(waveforms)):
        assert waveforms[i].raw_data.tolist() != data[i].tolist()


def test___int32_ndarray_no_copy___from_array_2d___creates_waveform_linked_to_same_buffer() -> None:
    data = np.array([[1, 2, 3], [4, 5, 6]], np.int32)

    waveforms = AnalogWaveform.from_array_2d(data, copy=False)

    assert len(waveforms) == 2
    for i in range(len(waveforms)):
        assert waveforms[i].raw_data.tolist() == data[i].tolist()
    data[0][:] = [3, 2, 1]
    data[1][:] = [6, 5, 4]
    for i in range(len(waveforms)):
        assert waveforms[i].raw_data.tolist() == data[i].tolist()


def test___int32_array_list_no_copy___from_array_2d___creates_waveform_linked_to_same_buffer() -> (
    None
):
    data = [array.array("i", [1, 2, 3]), array.array("i", [4, 5, 6])]

    waveforms = AnalogWaveform.from_array_2d(data, dtype=np.int32, copy=False)

    assert len(waveforms) == 2
    for i in range(len(waveforms)):
        assert waveforms[i].raw_data.tolist() == data[i].tolist()
    data[0][:] = array.array("i", [3, 2, 1])
    data[1][:] = array.array("i", [6, 5, 4])
    for i in range(len(waveforms)):
        assert waveforms[i].raw_data.tolist() == data[i].tolist()


def test___int_list_list_no_copy___from_array_2d___raises_value_error() -> None:
    data = [[1, 2, 3], [4, 5, 6]]

    with pytest.raises(ValueError) as exc:
        _ = AnalogWaveform.from_array_2d(data, np.int32, copy=False)

    assert exc.value.args[0].startswith(
        "Unable to avoid copy while creating an array as requested."
    )


@pytest.mark.parametrize(
    "start_index, sample_count, expected_data",
    [
        (0, None, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]),
        (1, None, [[2, 3, 4, 5], [7, 8, 9, 10]]),
        (4, None, [[5], [10]]),
        (5, None, [[], []]),
        (0, 1, [[1], [6]]),
        (0, 4, [[1, 2, 3, 4], [6, 7, 8, 9]]),
        (1, 1, [[2], [7]]),
        (1, 3, [[2, 3, 4], [7, 8, 9]]),
        (1, 4, [[2, 3, 4, 5], [7, 8, 9, 10]]),
    ],
)
def test___array_subset___from_array_2d___creates_waveform_with_array_subset(
    start_index: SupportsIndex, sample_count: SupportsIndex | None, expected_data: list[list[int]]
) -> None:
    data = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], np.int32)

    waveforms = AnalogWaveform.from_array_2d(
        data, start_index=start_index, sample_count=sample_count
    )

    assert len(waveforms) == 2
    for i in range(len(waveforms)):
        assert waveforms[i].raw_data.tolist() == expected_data[i]
        assert waveforms[i].start_index == (start_index if start_index is not None else 0)


@pytest.mark.parametrize(
    "start_index, sample_count, expected_message, exception_type",
    [
        (-2, None, "The start index must be a non-negative integer.", ValueError),
        (-1, None, "The start index must be a non-negative integer.", ValueError),
        (
            6,
            None,
            "The start index must be less than or equal to the input array length.",
            wfmex.StartIndexTooLargeError,
        ),
        (0, -2, "The sample count must be a non-negative integer.", ValueError),
        (0, -1, "The sample count must be a non-negative integer.", ValueError),
        (
            0,
            6,
            "The sum of the start index and sample count must be less than or equal to the input array length.",
            wfmex.StartIndexOrSampleCountTooLargeError,
        ),
        (
            1,
            5,
            "The sum of the start index and sample count must be less than or equal to the input array length.",
            wfmex.StartIndexOrSampleCountTooLargeError,
        ),
        (
            5,
            1,
            "The sum of the start index and sample count must be less than or equal to the input array length.",
            wfmex.StartIndexOrSampleCountTooLargeError,
        ),
    ],
)
def test___invalid_array_subset___from_array_2d___raises_correct_error(
    start_index: SupportsIndex,
    sample_count: SupportsIndex | None,
    expected_message: str,
    exception_type: type[Exception],
) -> None:
    data = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], np.int32)

    with pytest.raises(exception_type) as exc:
        _ = AnalogWaveform.from_array_2d(data, start_index=start_index, sample_count=sample_count)

    assert exc.value.args[0].startswith(expected_message)


###############################################################################
# raw_data
###############################################################################
def test___int32_waveform___raw_data___returns_int32_data() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2, 3], np.int32)

    raw_data = waveform.raw_data

    assert_type(raw_data, npt.NDArray[np.int32])
    assert isinstance(raw_data, np.ndarray) and raw_data.dtype == np.int32
    assert list(raw_data) == [0, 1, 2, 3]


def test___int32_waveform_with_linear_scale___raw_data___returns_int32_data() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2, 3], np.int32)
    waveform.scale_mode = LinearScaleMode(2.0, 0.5)

    raw_data = waveform.raw_data

    assert_type(raw_data, npt.NDArray[np.int32])
    assert isinstance(raw_data, np.ndarray) and raw_data.dtype == np.int32
    assert list(raw_data) == [0, 1, 2, 3]


###############################################################################
# get_raw_data
###############################################################################
def test___int32_waveform___get_raw_data___returns_raw_data() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2, 3], np.int32)

    scaled_data = waveform.get_raw_data()

    assert_type(scaled_data, npt.NDArray[np.int32])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.int32
    assert list(scaled_data) == [0, 1, 2, 3]


def test___int32_waveform_with_linear_scale___get_raw_data___returns_raw_data() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2, 3], np.int32)
    waveform.scale_mode = LinearScaleMode(2.0, 0.5)

    scaled_data = waveform.get_raw_data()

    assert_type(scaled_data, npt.NDArray[np.int32])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.int32
    assert list(scaled_data) == [0, 1, 2, 3]


@pytest.mark.parametrize(
    "start_index, sample_count, expected_raw_data",
    [
        (None, None, [0, 1, 2, 3]),
        (0, None, [0, 1, 2, 3]),
        (1, None, [1, 2, 3]),
        (3, None, [3]),
        (4, None, []),
        (None, None, [0, 1, 2, 3]),
        (None, 1, [0]),
        (None, 3, [0, 1, 2]),
        (None, 4, [0, 1, 2, 3]),
        (1, 2, [1, 2]),
        (4, 0, []),
    ],
)
def test___array_subset___get_raw_data___returns_array_subset(
    start_index: int, sample_count: int, expected_raw_data: list[int]
) -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2, 3], np.int32)
    waveform.scale_mode = LinearScaleMode(2.0, 0.5)

    scaled_data = waveform.get_raw_data(start_index=start_index, sample_count=sample_count)

    assert_type(scaled_data, npt.NDArray[np.int32])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.int32
    assert list(scaled_data) == expected_raw_data


@pytest.mark.parametrize(
    "start_index, sample_count, expected_message, exception_type",
    [
        (
            5,
            None,
            "The start index must be less than or equal to the number of samples in the waveform.",
            wfmex.StartIndexTooLargeError,
        ),
        (
            0,
            5,
            "The sum of the start index and sample count must be less than or equal to the number of samples in the waveform.",
            wfmex.StartIndexOrSampleCountTooLargeError,
        ),
        (
            4,
            1,
            "The sum of the start index and sample count must be less than or equal to the number of samples in the waveform.",
            wfmex.StartIndexOrSampleCountTooLargeError,
        ),
    ],
)
def test___invalid_array_subset___get_raw_data___returns_array_subset(
    start_index: int, sample_count: int, expected_message: str, exception_type: type[Exception]
) -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2, 3], np.int32)
    waveform.scale_mode = LinearScaleMode(2.0, 0.5)

    with pytest.raises(exception_type) as exc:
        _ = waveform.get_raw_data(start_index=start_index, sample_count=sample_count)

    assert exc.value.args[0].startswith(expected_message)


###############################################################################
# scaled_data
###############################################################################
def test___int32_waveform___scaled_data___converts_to_float64() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2, 3], np.int32)

    scaled_data = waveform.scaled_data

    assert_type(scaled_data, npt.NDArray[np.float64])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.float64
    assert list(scaled_data) == [0, 1, 2, 3]


def test___int32_waveform_with_linear_scale___scaled_data___applies_linear_scale() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2, 3], np.int32)
    waveform.scale_mode = LinearScaleMode(2.0, 0.5)

    scaled_data = waveform.scaled_data

    assert_type(scaled_data, npt.NDArray[np.float64])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.float64
    assert list(scaled_data) == [0.5, 2.5, 4.5, 6.5]


###############################################################################
# get_scaled_data
###############################################################################
def test___int32_waveform___get_scaled_data___converts_to_float64() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2, 3], np.int32)

    scaled_data = waveform.get_scaled_data()

    assert_type(scaled_data, npt.NDArray[np.float64])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.float64
    assert list(scaled_data) == [0, 1, 2, 3]


def test___int32_waveform_with_linear_scale___get_scaled_data___applies_linear_scale() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2, 3], np.int32)
    waveform.scale_mode = LinearScaleMode(2.0, 0.5)

    scaled_data = waveform.get_scaled_data()

    assert_type(scaled_data, npt.NDArray[np.float64])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.float64
    assert list(scaled_data) == [0.5, 2.5, 4.5, 6.5]


def test___float32_dtype___get_scaled_data___converts_to_float32() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2, 3], np.int32)
    waveform.scale_mode = LinearScaleMode(2.0, 0.5)

    scaled_data = waveform.get_scaled_data(np.float32)

    assert_type(scaled_data, npt.NDArray[np.float32])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.float32
    assert list(scaled_data) == [0.5, 2.5, 4.5, 6.5]


@pytest.mark.parametrize(
    "waveform_dtype",
    [
        np.float32,
        np.float64,
        np.int8,
        np.int16,
        np.int32,
        np.int64,
        np.uint8,
        np.uint16,
        np.uint32,
        np.uint64,
    ],
)
@pytest.mark.parametrize("scaled_dtype", [np.float32, np.float64])
def test___varying_dtype___get_scaled_data___converts_to_requested_dtype(
    waveform_dtype: npt.DTypeLike, scaled_dtype: npt.DTypeLike
) -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2, 3], waveform_dtype)
    waveform.scale_mode = LinearScaleMode(3.0, 4.0)

    scaled_data = waveform.get_scaled_data(scaled_dtype)

    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == scaled_dtype
    assert list(scaled_data) == [4.0, 7.0, 10.0, 13.0]


def test___unsupported_dtype___get_scaled_data___raises_type_error() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2, 3], np.int32)
    waveform.scale_mode = LinearScaleMode(3.0, 4.0)

    with pytest.raises(TypeError) as exc:
        _ = waveform.get_scaled_data(np.int32)

    assert exc.value.args[0].startswith("The requested data type is not supported.")
    assert "Data type: int32" in exc.value.args[0]
    assert "Supported data types: float32, float64" in exc.value.args[0]


def test___array_subset___get_scaled_data___returns_array_subset() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2, 3], np.int32)
    waveform.scale_mode = LinearScaleMode(2.0, 0.5)

    scaled_data = waveform.get_scaled_data(start_index=1, sample_count=2)

    assert_type(scaled_data, npt.NDArray[np.float64])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.float64
    assert list(scaled_data) == [2.5, 4.5]


###############################################################################
# sample count
###############################################################################
def test___waveform___set_sample_count___updates_sample_count() -> None:
    waveform = AnalogWaveform(10, np.float64)

    waveform.sample_count = 5

    assert waveform.sample_count == 5
    assert waveform.capacity == 10  # Capacity should remain unchanged
    assert len(waveform.raw_data) == 5  # Raw data length should reflect new sample count


def test___waveform___set_sample_count_exceeds_capacity___raises_value_error() -> None:
    waveform = AnalogWaveform(5, np.float64, capacity=10)

    with pytest.raises(ValueError) as exc:
        waveform.sample_count = 15

    assert exc.value.args[0].startswith(
        "The sum of the start index and sample count must be less than or equal to the capacity."
    )

    assert waveform.sample_count == 5  # Original sample count preserved


###############################################################################
# capacity
###############################################################################
@pytest.mark.parametrize(
    "capacity, expected_data",
    [(3, [1, 2, 3]), (4, [1, 2, 3, 0]), (10, [1, 2, 3, 0, 0, 0, 0, 0, 0, 0])],
)
def test___waveform___set_capacity___resizes_array_and_pads_with_zeros(
    capacity: int, expected_data: list[int]
) -> None:
    data = [1, 2, 3]
    waveform = AnalogWaveform.from_array_1d(data, np.int32)

    waveform.capacity = capacity

    assert waveform.capacity == capacity
    assert waveform.raw_data.tolist() == data
    assert waveform._data.tolist() == expected_data


@pytest.mark.parametrize(
    "capacity, expected_message, exception_type",
    [
        (-2, "The capacity must be a non-negative integer.", ValueError),
        (-1, "The capacity must be a non-negative integer.", ValueError),
        (
            0,
            "The capacity must be equal to or greater than the number of samples in the waveform.",
            wfmex.CapacityTooSmallError,
        ),
        (
            2,
            "The capacity must be equal to or greater than the number of samples in the waveform.",
            wfmex.CapacityTooSmallError,
        ),
    ],
)
def test___invalid_capacity___set_capacity___raises_correct_error(
    capacity: int, expected_message: str, exception_type: type[Exception]
) -> None:
    data = [1, 2, 3]
    waveform = AnalogWaveform.from_array_1d(data, np.int32)

    with pytest.raises(exception_type) as exc:
        waveform.capacity = capacity

    assert exc.value.args[0].startswith(expected_message)


def test___referenced_array___set_capacity___reference_sees_size_change() -> None:
    data = np.array([1, 2, 3], np.int32)
    waveform = AnalogWaveform.from_array_1d(data, np.int32, copy=False)

    waveform.capacity = 10

    assert len(data) == 10
    assert waveform.capacity == 10
    assert data.tolist() == [1, 2, 3, 0, 0, 0, 0, 0, 0, 0]
    assert waveform.raw_data.tolist() == [1, 2, 3]
    assert waveform._data.tolist() == [1, 2, 3, 0, 0, 0, 0, 0, 0, 0]


def test___array_with_external_buffer___set_capacity___raises_value_error() -> None:
    data = array.array("i", [1, 2, 3])
    waveform = AnalogWaveform.from_array_1d(data, np.int32, copy=False)

    with pytest.raises(ValueError) as exc:
        waveform.capacity = 10

    assert exc.value.args[0].startswith("cannot resize this array: it does not own its data")


###############################################################################
# extended properties
###############################################################################
def test___waveform___set_channel_name___sets_extended_property() -> None:
    waveform = AnalogWaveform()

    waveform.channel_name = "Dev1/ai0"

    assert waveform.channel_name == "Dev1/ai0"
    assert waveform.extended_properties["NI_ChannelName"] == "Dev1/ai0"


def test___invalid_type___set_channel_name___raises_type_error() -> None:
    waveform = AnalogWaveform()

    with pytest.raises(TypeError) as exc:
        waveform.channel_name = 1  # type: ignore[assignment]

    assert exc.value.args[0].startswith("The channel name must be a str.")


def test___waveform___set_units___sets_extended_property() -> None:
    waveform = AnalogWaveform()

    waveform.units = "Volts"

    assert waveform.units == "Volts"
    assert waveform.extended_properties["NI_UnitDescription"] == "Volts"


def test___invalid_type___set_units___raises_type_error() -> None:
    waveform = AnalogWaveform()

    with pytest.raises(TypeError) as exc:
        waveform.units = None  # type: ignore[assignment]

    assert exc.value.args[0].startswith("The units must be a str.")


def test___waveform___set_undefined_property___raises_attribute_error() -> None:
    waveform = AnalogWaveform()

    with pytest.raises(AttributeError):
        waveform.undefined_property = "Whatever"  # type: ignore[attr-defined]


def test___waveform___take_weak_ref___references_waveform() -> None:
    waveform = AnalogWaveform()

    waveform_ref = weakref.ref(waveform)

    assert waveform_ref() is waveform


###############################################################################
# timing
###############################################################################
def test___waveform___has_empty_timing() -> None:
    waveform = AnalogWaveform()

    assert waveform.timing is Timing.empty


def test___bintime___waveform_with_timing___static_type_erased() -> None:
    sample_interval = bt.TimeDelta(1e-3)
    timestamp = bt.DateTime.now(dt.timezone.utc)
    time_offset = bt.TimeDelta(1e-6)
    waveform = AnalogWaveform(
        timing=Timing.create_with_regular_interval(sample_interval, timestamp, time_offset)
    )

    assert_type(waveform.timing.sample_interval, Union[bt.TimeDelta, dt.timedelta, ht.timedelta])
    assert_type(waveform.timing.timestamp, Union[bt.DateTime, dt.datetime, ht.datetime])
    assert_type(waveform.timing.start_time, Union[bt.DateTime, dt.datetime, ht.datetime])
    assert_type(waveform.timing.time_offset, Union[bt.TimeDelta, dt.timedelta, ht.timedelta])
    assert waveform.timing.sample_interval == sample_interval
    assert waveform.timing.timestamp == timestamp
    assert waveform.timing.start_time == timestamp + time_offset
    assert waveform.timing.time_offset == time_offset


def test___datetime___waveform_with_timing___static_type_erased() -> None:
    sample_interval = dt.timedelta(milliseconds=1)
    timestamp = dt.datetime.now(dt.timezone.utc)
    time_offset = dt.timedelta(microseconds=1)
    waveform = AnalogWaveform(
        timing=Timing.create_with_regular_interval(sample_interval, timestamp, time_offset)
    )

    assert_type(waveform.timing.sample_interval, Union[bt.TimeDelta, dt.timedelta, ht.timedelta])
    assert_type(waveform.timing.timestamp, Union[bt.DateTime, dt.datetime, ht.datetime])
    assert_type(waveform.timing.start_time, Union[bt.DateTime, dt.datetime, ht.datetime])
    assert_type(waveform.timing.time_offset, Union[bt.TimeDelta, dt.timedelta, ht.timedelta])
    assert waveform.timing.sample_interval == sample_interval
    assert waveform.timing.timestamp == timestamp
    assert waveform.timing.start_time == timestamp + time_offset
    assert waveform.timing.time_offset == time_offset


def test___hightime___waveform_with_timing___static_type_erased() -> None:
    sample_interval = ht.timedelta(milliseconds=1)
    timestamp = ht.datetime.now(dt.timezone.utc)
    time_offset = ht.timedelta(microseconds=1)
    waveform = AnalogWaveform(
        timing=Timing.create_with_regular_interval(sample_interval, timestamp, time_offset)
    )

    assert_type(waveform.timing.sample_interval, Union[bt.TimeDelta, dt.timedelta, ht.timedelta])
    assert_type(waveform.timing.timestamp, Union[bt.DateTime, dt.datetime, ht.datetime])
    assert_type(waveform.timing.start_time, Union[bt.DateTime, dt.datetime, ht.datetime])
    assert_type(waveform.timing.time_offset, Union[bt.TimeDelta, dt.timedelta, ht.timedelta])
    assert waveform.timing.sample_interval == sample_interval
    assert waveform.timing.timestamp == timestamp
    assert waveform.timing.start_time == timestamp + time_offset
    assert waveform.timing.time_offset == time_offset


@pytest.mark.parametrize(
    "timing",
    [
        Timing.create_with_regular_interval(
            bt.TimeDelta(1e-3), bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), bt.TimeDelta(1e-6)
        ),
        Timing.create_with_regular_interval(
            dt.timedelta(milliseconds=1),
            dt.datetime(2025, 1, 1, tzinfo=dt.timezone.utc),
            dt.timedelta(microseconds=1),
        ),
        Timing.create_with_regular_interval(
            ht.timedelta(milliseconds=1),
            ht.datetime(2025, 1, 1, tzinfo=dt.timezone.utc),
            dt.timedelta(microseconds=1),
        ),
    ],
)
def test___polymorphic_timing___get_timing_properties___behaves_polymorphically(
    timing: Timing[Any, Any, Any],
) -> None:
    waveform = AnalogWaveform(timing=timing)

    assert waveform.timing.sample_interval.total_seconds() == pytest.approx(1e-3)
    assert (
        waveform.timing.timestamp.year,
        waveform.timing.timestamp.month,
        waveform.timing.timestamp.day,
    ) == (2025, 1, 1)
    assert waveform.timing.time_offset.total_seconds() == pytest.approx(1e-6)


###############################################################################
# scale_mode
###############################################################################
def test___waveform___scale_mode___defaults_to_no_scaling() -> None:
    waveform = AnalogWaveform()

    assert_type(waveform.scale_mode, ScaleMode)
    assert isinstance(waveform.scale_mode, NoneScaleMode)
    assert waveform.scale_mode is NO_SCALING


###############################################################################
# append array
###############################################################################
def test___empty_ndarray___append___no_effect() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    array = np.array([], np.int32)

    waveform.append(array)

    assert list(waveform.raw_data) == [0, 1, 2]


def test___int32_ndarray___append___appends_array() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    array = np.array([3, 4, 5], np.int32)

    waveform.append(array)

    assert list(waveform.raw_data) == [0, 1, 2, 3, 4, 5]


def test___float64_ndarray___append___appends_array() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.float64)
    array = np.array([3, 4, 5], np.float64)

    waveform.append(array)

    assert list(waveform.raw_data) == [0, 1, 2, 3, 4, 5]


def test___ndarray_with_mismatched_dtype___append___raises_correct_error() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.float64)
    array = np.array([3, 4, 5], np.int32)

    with pytest.raises(wfmex.DatatypeMismatchError) as exc:
        waveform.append(array)  # type: ignore[arg-type]

    assert exc.value.args[0].startswith(
        "The data type of the input array must match the waveform data type."
    )


def test___ndarray_2d___append___raises_value_error() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.float64)
    array = np.array([[3, 4, 5], [6, 7, 8]], np.float64)

    with pytest.raises(ValueError) as exc:
        waveform.append(array)

    assert exc.value.args[0].startswith("The input array must be a one-dimensional array.")


def test___irregular_waveform_and_int32_ndarray_with_timestamps___append___appends_array() -> None:
    start_time = dt.datetime.now(dt.timezone.utc)
    waveform_offsets = [dt.timedelta(0), dt.timedelta(1), dt.timedelta(2)]
    waveform_timestamps = [start_time + offset for offset in waveform_offsets]
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    waveform.timing = Timing.create_with_irregular_interval(waveform_timestamps)
    array_offsets = [dt.timedelta(3), dt.timedelta(4), dt.timedelta(5)]
    array_timestamps = [start_time + offset for offset in array_offsets]
    array = np.array([3, 4, 5], np.int32)

    waveform.append(array, array_timestamps)

    assert list(waveform.raw_data) == [0, 1, 2, 3, 4, 5]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert waveform.timing._timestamps == waveform_timestamps + array_timestamps


def test___irregular_waveform_and_int32_ndarray_without_timestamps___append___raises_timing_mismatch_error_and_does_not_append() -> (
    None
):
    start_time = dt.datetime.now(dt.timezone.utc)
    waveform_offsets = [dt.timedelta(0), dt.timedelta(1), dt.timedelta(2)]
    waveform_timestamps = [start_time + offset for offset in waveform_offsets]
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    waveform.timing = Timing.create_with_irregular_interval(waveform_timestamps)
    array = np.array([3, 4, 5], np.int32)

    with pytest.raises(wfmex.TimingMismatchError) as exc:
        waveform.append(array)

    assert exc.value.args[0].startswith(
        "The timestamps argument is required when appending to a waveform with irregular timing."
    )
    assert list(waveform.raw_data) == [0, 1, 2]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert waveform.timing._timestamps == waveform_timestamps


def test___irregular_waveform_and_int32_ndarray_with_wrong_timestamp_count___append___raises_correct_error_and_does_not_append() -> (
    None
):
    start_time = dt.datetime.now(dt.timezone.utc)
    waveform_offsets = [dt.timedelta(0), dt.timedelta(1), dt.timedelta(2)]
    waveform_timestamps = [start_time + offset for offset in waveform_offsets]
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    waveform.timing = Timing.create_with_irregular_interval(waveform_timestamps)
    array_offsets = [dt.timedelta(3), dt.timedelta(4)]
    array_timestamps = [start_time + offset for offset in array_offsets]
    array = np.array([3, 4, 5], np.int32)

    with pytest.raises(wfmex.IrregularTimestampCountMismatchError) as exc:
        waveform.append(array, array_timestamps)

    assert exc.value.args[0].startswith(
        "The number of irregular timestamps must be equal to the input array length."
    )
    assert list(waveform.raw_data) == [0, 1, 2]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert waveform.timing._timestamps == waveform_timestamps


def test___regular_waveform_and_int32_ndarray_with_timestamps___append___raises_value_error_and_does_not_append() -> (
    None
):
    start_time = dt.datetime.now(dt.timezone.utc)
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    waveform.timing = Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
    array_offsets = [dt.timedelta(3), dt.timedelta(4), dt.timedelta(5)]
    array_timestamps = [start_time + offset for offset in array_offsets]
    array = np.array([3, 4, 5], np.int32)

    with pytest.raises(ValueError) as exc:
        waveform.append(array, array_timestamps)

    assert exc.value.args[0].startswith("The timestamps argument is not supported.")
    assert list(waveform.raw_data) == [0, 1, 2]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.timing.sample_interval == dt.timedelta(milliseconds=1)


###############################################################################
# append waveform
###############################################################################
def test___empty_waveform___append___no_effect() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    other = AnalogWaveform(dtype=np.int32)

    waveform.append(other)

    assert list(waveform.raw_data) == [0, 1, 2]


def test___int32_waveform___append___appends_waveform() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    other = AnalogWaveform.from_array_1d([3, 4, 5], np.int32)

    waveform.append(other)

    assert list(waveform.raw_data) == [0, 1, 2, 3, 4, 5]


def test___float64_waveform___append___appends_waveform() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.float64)
    other = AnalogWaveform.from_array_1d([3, 4, 5], np.float64)

    waveform.append(other)

    assert list(waveform.raw_data) == [0, 1, 2, 3, 4, 5]


def test___waveform_with_mismatched_dtype___append___raises_correct_error() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.float64)
    other = AnalogWaveform.from_array_1d([3, 4, 5], np.int32)

    with pytest.raises(wfmex.DatatypeMismatchError) as exc:
        waveform.append(other)  # type: ignore[arg-type]

    assert exc.value.args[0].startswith(
        "The data type of the input waveform must match the waveform data type."
    )


def test___irregular_waveform_and_irregular_waveform___append___appends_waveform() -> None:
    start_time = dt.datetime.now(dt.timezone.utc)
    waveform_offsets = [dt.timedelta(0), dt.timedelta(1), dt.timedelta(2)]
    waveform_timestamps = [start_time + offset for offset in waveform_offsets]
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    waveform.timing = Timing.create_with_irregular_interval(waveform_timestamps)
    other_offsets = [dt.timedelta(3), dt.timedelta(4), dt.timedelta(5)]
    other_timestamps = [start_time + offset for offset in other_offsets]
    other = AnalogWaveform.from_array_1d([3, 4, 5], np.int32)
    other.timing = Timing.create_with_irregular_interval(other_timestamps)

    waveform.append(other)

    assert list(waveform.raw_data) == [0, 1, 2, 3, 4, 5]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert waveform.timing._timestamps == waveform_timestamps + other_timestamps


def test___irregular_waveform_and_regular_waveform___append___raises_correct_error() -> None:
    start_time = dt.datetime.now(dt.timezone.utc)
    waveform_offsets = [dt.timedelta(0), dt.timedelta(1), dt.timedelta(2)]
    waveform_timestamps = [start_time + offset for offset in waveform_offsets]
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    waveform.timing = Timing.create_with_irregular_interval(waveform_timestamps)
    other = AnalogWaveform.from_array_1d([3, 4, 5], np.int32)

    with pytest.raises(wfmex.SampleIntervalModeMismatchError) as exc:
        waveform.append(other)

    assert exc.value.args[0].startswith(
        "The timing of one or more waveforms does not match the timing of the current waveform."
    )
    assert list(waveform.raw_data) == [0, 1, 2]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert waveform.timing._timestamps == waveform_timestamps


def test___regular_waveform_and_irregular_waveform___append___raises_correct_error() -> None:
    start_time = dt.datetime.now(dt.timezone.utc)
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    waveform.timing = Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
    other_offsets = [dt.timedelta(3), dt.timedelta(4), dt.timedelta(5)]
    other_timestamps = [start_time + offset for offset in other_offsets]
    other = AnalogWaveform.from_array_1d([3, 4, 5], np.int32)
    other.timing = Timing.create_with_irregular_interval(other_timestamps)

    with pytest.raises(wfmex.SampleIntervalModeMismatchError) as exc:
        waveform.append(other)

    assert exc.value.args[0].startswith(
        "The timing of one or more waveforms does not match the timing of the current waveform."
    )
    assert list(waveform.raw_data) == [0, 1, 2]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.timing.sample_interval == dt.timedelta(milliseconds=1)


def test___regular_waveform_and_regular_waveform_with_different_sample_interval___append___appends_waveform_with_timing_mismatch_warning() -> (
    None
):
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    waveform.timing = Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
    other = AnalogWaveform.from_array_1d([3, 4, 5], np.int32)
    other.timing = Timing.create_with_regular_interval(dt.timedelta(milliseconds=2))

    with pytest.warns(wfmwarn.TimingMismatchWarning):
        waveform.append(other)

    assert list(waveform.raw_data) == [0, 1, 2, 3, 4, 5]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.timing.sample_interval == dt.timedelta(milliseconds=1)


def test___regular_waveform_and_regular_waveform_with_different_extended_properties___append___merges_extended_properties() -> (
    None
):
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    waveform.extended_properties["A"] = 1
    waveform.extended_properties["B"] = 2
    other = AnalogWaveform.from_array_1d([3, 4, 5], np.int32)
    other.extended_properties["B"] = 3
    other.extended_properties["C"] = 4

    waveform.append(other)

    assert list(waveform.raw_data) == [0, 1, 2, 3, 4, 5]
    assert waveform.extended_properties == {"A": 1, "B": 2, "C": 4}


def test___regular_waveform_and_regular_waveform_with_different_scale_mode___append___appends_waveform_with_scaling_mismatch_warning() -> (
    None
):
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    waveform.scale_mode = LinearScaleMode(1.0, 0.0)
    other = AnalogWaveform.from_array_1d([3, 4, 5], np.int32)
    other.scale_mode = LinearScaleMode(2.0, 0.0)

    with pytest.warns(wfmwarn.ScalingMismatchWarning):
        waveform.append(other)

    assert list(waveform.raw_data) == [0, 1, 2, 3, 4, 5]
    assert waveform.scale_mode == LinearScaleMode(1.0, 0.0)


###############################################################################
# append waveforms
###############################################################################
def test___empty_waveform_list___append___no_effect() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    other: list[AnalogWaveform[np.int32]] = []

    waveform.append(other)

    assert list(waveform.raw_data) == [0, 1, 2]


def test___int32_waveform_list___append___appends_waveform() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    other = [
        AnalogWaveform.from_array_1d([3, 4, 5], np.int32),
        AnalogWaveform.from_array_1d([6], np.int32),
        AnalogWaveform.from_array_1d([7, 8], np.int32),
    ]

    waveform.append(other)

    assert list(waveform.raw_data) == [0, 1, 2, 3, 4, 5, 6, 7, 8]


def test___float64_waveform_tuple___append___appends_waveform() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.float64)
    other = (
        AnalogWaveform.from_array_1d([3, 4, 5], np.float64),
        AnalogWaveform.from_array_1d([6, 7, 8], np.float64),
    )

    waveform.append(other)

    assert list(waveform.raw_data) == [0, 1, 2, 3, 4, 5, 6, 7, 8]


def test___waveform_list_with_mismatched_dtype___append___raises_correct_error_and_does_not_append() -> (
    None
):
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.float64)
    other = [
        AnalogWaveform.from_array_1d([3, 4, 5], np.float64),
        AnalogWaveform.from_array_1d([6, 7, 8], np.int32),
    ]

    with pytest.raises(wfmex.DatatypeMismatchError) as exc:
        waveform.append(other)  # type: ignore[arg-type]

    assert exc.value.args[0].startswith(
        "The data type of the input waveform must match the waveform data type."
    )
    assert list(waveform.raw_data) == [0, 1, 2]


def test___irregular_waveform_and_irregular_waveform_list___append___appends_waveform() -> None:
    start_time = dt.datetime.now(dt.timezone.utc)
    waveform_offsets = [dt.timedelta(0), dt.timedelta(1), dt.timedelta(2)]
    waveform_timestamps = [start_time + offset for offset in waveform_offsets]
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    waveform.timing = Timing.create_with_irregular_interval(waveform_timestamps)
    other1_offsets = [dt.timedelta(3), dt.timedelta(4), dt.timedelta(5)]
    other1_timestamps = [start_time + offset for offset in other1_offsets]
    other1 = AnalogWaveform.from_array_1d([3, 4, 5], np.int32)
    other1.timing = Timing.create_with_irregular_interval(other1_timestamps)
    other2_offsets = [dt.timedelta(6), dt.timedelta(7), dt.timedelta(8)]
    other2_timestamps = [start_time + offset for offset in other2_offsets]
    other2 = AnalogWaveform.from_array_1d([6, 7, 8], np.int32)
    other2.timing = Timing.create_with_irregular_interval(other2_timestamps)
    other = [other1, other2]

    waveform.append(other)

    assert list(waveform.raw_data) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert (
        waveform.timing._timestamps == waveform_timestamps + other1_timestamps + other2_timestamps
    )


def test___irregular_waveform_and_regular_waveform_list___append___raises_correct_error_and_does_not_append() -> (
    None
):
    start_time = dt.datetime.now(dt.timezone.utc)
    waveform_offsets = [dt.timedelta(0), dt.timedelta(1), dt.timedelta(2)]
    waveform_timestamps = [start_time + offset for offset in waveform_offsets]
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    waveform.timing = Timing.create_with_irregular_interval(waveform_timestamps)
    other1_offsets = [dt.timedelta(3), dt.timedelta(4), dt.timedelta(5)]
    other1_timestamps = [start_time + offset for offset in other1_offsets]
    other1 = AnalogWaveform.from_array_1d([3, 4, 5], np.int32)
    other1.timing = Timing.create_with_irregular_interval(other1_timestamps)
    other2 = AnalogWaveform.from_array_1d([6, 7, 8], np.int32)
    other2.timing = Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
    other = [other1, other2]

    with pytest.raises(wfmex.SampleIntervalModeMismatchError) as exc:
        waveform.append(other)

    assert exc.value.args[0].startswith(
        "The timing of one or more waveforms does not match the timing of the current waveform."
    )
    assert list(waveform.raw_data) == [0, 1, 2]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert waveform.timing._timestamps == waveform_timestamps


def test___regular_waveform_and_irregular_waveform_list___append___raises_correct_error_and_does_not_append() -> (
    None
):
    start_time = dt.datetime.now(dt.timezone.utc)
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    waveform.timing = Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
    other1 = AnalogWaveform.from_array_1d([3, 4, 5], np.int32)
    other1.timing = Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
    other2_offsets = [dt.timedelta(3), dt.timedelta(4), dt.timedelta(5)]
    other2_timestamps = [start_time + offset for offset in other2_offsets]
    other2 = AnalogWaveform.from_array_1d([3, 4, 5], np.int32)
    other2.timing = Timing.create_with_irregular_interval(other2_timestamps)
    other = [other1, other2]

    with pytest.raises(wfmex.SampleIntervalModeMismatchError) as exc:
        waveform.append(other)

    assert exc.value.args[0].startswith(
        "The timing of one or more waveforms does not match the timing of the current waveform."
    )
    assert list(waveform.raw_data) == [0, 1, 2]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.timing.sample_interval == dt.timedelta(milliseconds=1)


###############################################################################
# load data
###############################################################################
def test___empty_ndarray___load_data___clears_data() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    array = np.array([], np.int32)

    waveform.load_data(array)

    assert list(waveform.raw_data) == []


def test___int32_ndarray___load_data___overwrites_data() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    array = np.array([3, 4, 5], np.int32)

    waveform.load_data(array)

    assert list(waveform.raw_data) == [3, 4, 5]


def test___float64_ndarray___load_data___overwrites_data() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.float64)
    array = np.array([3, 4, 5], np.float64)

    waveform.load_data(array)

    assert list(waveform.raw_data) == [3, 4, 5]


def test___ndarray_with_mismatched_dtype___load_data___raises_correct_error() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.float64)
    array = np.array([3, 4, 5], np.int32)

    with pytest.raises(wfmex.DatatypeMismatchError) as exc:
        waveform.load_data(array)  # type: ignore[arg-type]

    assert exc.value.args[0].startswith(
        "The data type of the input array must match the waveform data type."
    )


def test___ndarray_2d___load_data___raises_value_error() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.float64)
    array = np.array([[3, 4, 5], [6, 7, 8]], np.float64)

    with pytest.raises(ValueError) as exc:
        waveform.load_data(array)

    assert exc.value.args[0].startswith("The input array must be a one-dimensional array.")


def test___smaller_ndarray___load_data___preserves_capacity() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    array = np.array([3], np.int32)

    waveform.load_data(array)

    assert list(waveform.raw_data) == [3]
    assert waveform.capacity == 3


def test___larger_ndarray___load_data___grows_capacity() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    array = np.array([3, 4, 5, 6], np.int32)

    waveform.load_data(array)

    assert list(waveform.raw_data) == [3, 4, 5, 6]
    assert waveform.capacity == 4


def test___waveform_with_start_index___load_data___clears_start_index() -> None:
    waveform = AnalogWaveform.from_array_1d(
        np.array([0, 1, 2], np.int32), np.int32, copy=False, start_index=1, sample_count=1
    )
    assert waveform.start_index == 1
    array = np.array([3], np.int32)

    waveform.load_data(array)

    assert list(waveform.raw_data) == [3]
    assert waveform.start_index == 0


def test___ndarray_subset___load_data___overwrites_data() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    array = np.array([3, 4, 5], np.int32)

    waveform.load_data(array, start_index=1, sample_count=1)

    assert list(waveform.raw_data) == [4]
    assert waveform.start_index == 0
    assert waveform.capacity == 3


def test___smaller_ndarray_no_copy___load_data___takes_ownership_of_array() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    array = np.array([3], np.int32)

    waveform.load_data(array, copy=False)

    assert list(waveform.raw_data) == [3]
    assert waveform._data is array


def test___larger_ndarray_no_copy___load_data___takes_ownership_of_array() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    array = np.array([3, 4, 5, 6], np.int32)

    waveform.load_data(array, copy=False)

    assert list(waveform.raw_data) == [3, 4, 5, 6]
    assert waveform._data is array


def test___ndarray_subset_no_copy___load_data___takes_ownership_of_array_subset() -> None:
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    array = np.array([3, 4, 5, 6], np.int32)

    waveform.load_data(array, copy=False, start_index=1, sample_count=2)

    assert list(waveform.raw_data) == [4, 5]
    assert waveform._data is array


def test___irregular_waveform_and_int32_ndarray_with_timestamps___load_data___overwrites_data_but_not_timestamps() -> (
    None
):
    start_time = dt.datetime.now(dt.timezone.utc)
    waveform_offsets = [dt.timedelta(0), dt.timedelta(1), dt.timedelta(2)]
    waveform_timestamps = [start_time + offset for offset in waveform_offsets]
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    waveform.timing = Timing.create_with_irregular_interval(waveform_timestamps)
    array = np.array([3, 4, 5], np.int32)

    waveform.load_data(array)

    assert list(waveform.raw_data) == [3, 4, 5]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert waveform.timing._timestamps == waveform_timestamps


def test___irregular_waveform_and_int32_ndarray_with_wrong_sample_count___load_data___raises_correct_error_and_does_not_overwrite_data() -> (
    None
):
    start_time = dt.datetime.now(dt.timezone.utc)
    waveform_offsets = [dt.timedelta(0), dt.timedelta(1), dt.timedelta(2)]
    waveform_timestamps = [start_time + offset for offset in waveform_offsets]
    waveform = AnalogWaveform.from_array_1d([0, 1, 2], np.int32)
    waveform.timing = Timing.create_with_irregular_interval(waveform_timestamps)
    array = np.array([3, 4], np.int32)

    with pytest.raises(wfmex.IrregularTimestampCountMismatchError) as exc:
        waveform.load_data(array)

    assert exc.value.args[0].startswith(
        "The input array length must be equal to the number of irregular timestamps."
    )
    assert list(waveform.raw_data) == [0, 1, 2]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert waveform.timing._timestamps == waveform_timestamps


###############################################################################
# magic methods
###############################################################################
@pytest.mark.parametrize(
    "left, right",
    [
        (AnalogWaveform(), AnalogWaveform()),
        (AnalogWaveform(10), AnalogWaveform(10)),
        (AnalogWaveform(10, np.float64), AnalogWaveform(10, np.float64)),
        (AnalogWaveform(10, np.int32), AnalogWaveform(10, np.int32)),
        (
            AnalogWaveform(10, np.int32, start_index=5, capacity=20),
            AnalogWaveform(10, np.int32, start_index=5, capacity=20),
        ),
        (
            AnalogWaveform.from_array_1d([1, 2, 3], np.float64),
            AnalogWaveform.from_array_1d([1, 2, 3], np.float64),
        ),
        (
            AnalogWaveform.from_array_1d([1, 2, 3], np.int32),
            AnalogWaveform.from_array_1d([1, 2, 3], np.int32),
        ),
        (
            AnalogWaveform(
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
            ),
            AnalogWaveform(
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
            ),
        ),
        (
            AnalogWaveform(
                timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=1))
            ),
            AnalogWaveform(
                timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=1))
            ),
        ),
        (
            AnalogWaveform(
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"}
            ),
            AnalogWaveform(
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"}
            ),
        ),
        (
            AnalogWaveform(scale_mode=LinearScaleMode(2.0, 1.0)),
            AnalogWaveform(scale_mode=LinearScaleMode(2.0, 1.0)),
        ),
        # start_index and capacity may differ as long as raw_data and sample_count are the same.
        (
            AnalogWaveform(10, np.int32, start_index=5, capacity=20),
            AnalogWaveform(10, np.int32, start_index=10, capacity=25),
        ),
        (
            AnalogWaveform.from_array_1d(
                [0, 0, 1, 2, 3, 4, 5, 0], np.int32, start_index=2, sample_count=5
            ),
            AnalogWaveform.from_array_1d(
                [0, 1, 2, 3, 4, 5, 0, 0, 0], np.int32, start_index=1, sample_count=5
            ),
        ),
        # Same value, different time type
        (
            AnalogWaveform(
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
            ),
            AnalogWaveform(
                timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=1))
            ),
        ),
        (
            AnalogWaveform(
                timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=1))
            ),
            AnalogWaveform(
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
            ),
        ),
    ],
)
def test___same_value___equality___equal(
    left: AnalogWaveform[Any], right: AnalogWaveform[Any]
) -> None:
    assert left == right
    assert not (left != right)


@pytest.mark.parametrize(
    "left, right",
    [
        (AnalogWaveform(), AnalogWaveform(10)),
        (AnalogWaveform(10), AnalogWaveform(11)),
        (AnalogWaveform(10, np.float64), AnalogWaveform(10, np.int32)),
        (
            AnalogWaveform(15, np.int32, start_index=5, capacity=20),
            AnalogWaveform(10, np.int32, start_index=5, capacity=20),
        ),
        (
            AnalogWaveform.from_array_1d([1, 4, 3], np.float64),
            AnalogWaveform.from_array_1d([1, 2, 3], np.float64),
        ),
        (
            AnalogWaveform.from_array_1d([1, 2, 3], np.int32),
            AnalogWaveform.from_array_1d([1, 2, 3], np.float64),
        ),
        (
            AnalogWaveform(
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
            ),
            AnalogWaveform(
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=2))
            ),
        ),
        (
            AnalogWaveform(
                timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=1))
            ),
            AnalogWaveform(
                timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=2))
            ),
        ),
        (
            AnalogWaveform(
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"}
            ),
            AnalogWaveform(
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Amps"}
            ),
        ),
        (
            AnalogWaveform(scale_mode=LinearScaleMode(2.0, 1.0)),
            AnalogWaveform(scale_mode=LinearScaleMode(2.0, 1.1)),
        ),
        (
            AnalogWaveform(scale_mode=NO_SCALING),
            AnalogWaveform(scale_mode=LinearScaleMode(2.0, 1.0)),
        ),
    ],
)
def test___different_value___equality___not_equal(
    left: AnalogWaveform[Any], right: AnalogWaveform[Any]
) -> None:
    assert not (left == right)
    assert left != right


if Version(np.__version__) >= Version("2.0.0") or sys.platform != "win32":
    _NDARRAY_DTYPE_INT32 = ", dtype=int32"
else:
    _NDARRAY_DTYPE_INT32 = ""


@pytest.mark.parametrize(
    "value, expected_repr",
    [
        (AnalogWaveform(), "nitypes.waveform.AnalogWaveform(0)"),
        (
            AnalogWaveform(5),
            "nitypes.waveform.AnalogWaveform(5, raw_data=array([0., 0., 0., 0., 0.]))",
        ),
        (
            AnalogWaveform(5, np.float64),
            "nitypes.waveform.AnalogWaveform(5, raw_data=array([0., 0., 0., 0., 0.]))",
        ),
        (AnalogWaveform(0, np.int32), "nitypes.waveform.AnalogWaveform(0, int32)"),
        (
            AnalogWaveform(5, np.int32),
            f"nitypes.waveform.AnalogWaveform(5, int32, raw_data=array([0, 0, 0, 0, 0]{_NDARRAY_DTYPE_INT32}))",
        ),
        (
            AnalogWaveform(5, np.int32, start_index=5, capacity=20),
            f"nitypes.waveform.AnalogWaveform(5, int32, raw_data=array([0, 0, 0, 0, 0]{_NDARRAY_DTYPE_INT32}))",
        ),
        (
            AnalogWaveform.from_array_1d([1, 2, 3], np.float64),
            "nitypes.waveform.AnalogWaveform(3, raw_data=array([1., 2., 3.]))",
        ),
        (
            AnalogWaveform.from_array_1d([1, 2, 3], np.int32),
            f"nitypes.waveform.AnalogWaveform(3, int32, raw_data=array([1, 2, 3]{_NDARRAY_DTYPE_INT32}))",
        ),
        (
            AnalogWaveform(
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
            ),
            "nitypes.waveform.AnalogWaveform(0, "
            "timing=nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR, "
            "sample_interval=datetime.timedelta(microseconds=1000)))",
        ),
        (
            AnalogWaveform(
                timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=1))
            ),
            "nitypes.waveform.AnalogWaveform(0, "
            "timing=nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR, "
            "sample_interval=hightime.timedelta(microseconds=1000)))",
        ),
        (
            AnalogWaveform(
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"}
            ),
            "nitypes.waveform.AnalogWaveform(0, extended_properties={'NI_ChannelName': 'Dev1/ai0', "
            "'NI_UnitDescription': 'Volts'})",
        ),
        (
            AnalogWaveform(scale_mode=LinearScaleMode(2.0, 1.0)),
            "nitypes.waveform.AnalogWaveform(0, scale_mode=nitypes.waveform.LinearScaleMode(2.0, 1.0))",
        ),
        (
            AnalogWaveform.from_array_1d(
                [1, 2, 3],
                np.int32,
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1)),
            ),
            f"nitypes.waveform.AnalogWaveform(3, int32, raw_data=array([1, 2, 3]{_NDARRAY_DTYPE_INT32}), "
            "timing=nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR, "
            "sample_interval=datetime.timedelta(microseconds=1000)))",
        ),
        (
            AnalogWaveform.from_array_1d(
                [1, 2, 3],
                np.int32,
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"},
            ),
            f"nitypes.waveform.AnalogWaveform(3, int32, raw_data=array([1, 2, 3]{_NDARRAY_DTYPE_INT32}), "
            "extended_properties={'NI_ChannelName': 'Dev1/ai0', 'NI_UnitDescription': 'Volts'})",
        ),
        (
            AnalogWaveform.from_array_1d([1, 2, 3], np.int32, scale_mode=LinearScaleMode(2.0, 1.0)),
            f"nitypes.waveform.AnalogWaveform(3, int32, raw_data=array([1, 2, 3]{_NDARRAY_DTYPE_INT32}), "
            "scale_mode=nitypes.waveform.LinearScaleMode(2.0, 1.0))",
        ),
    ],
)
def test___various_values___repr___looks_ok(value: AnalogWaveform[Any], expected_repr: str) -> None:
    assert repr(value) == expected_repr


_VARIOUS_VALUES = [
    AnalogWaveform(),
    AnalogWaveform(10),
    AnalogWaveform(10, np.float64),
    AnalogWaveform(10, np.int32),
    AnalogWaveform(10, np.int32, start_index=5, capacity=20),
    AnalogWaveform.from_array_1d([1, 2, 3], np.float64),
    AnalogWaveform.from_array_1d([1, 2, 3], np.int32),
    AnalogWaveform(timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))),
    AnalogWaveform(timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=1))),
    AnalogWaveform(
        extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"}
    ),
    AnalogWaveform(scale_mode=LinearScaleMode(2.0, 1.0)),
    AnalogWaveform(10, np.int32, start_index=5, capacity=20),
    AnalogWaveform.from_array_1d([0, 0, 1, 2, 3, 4, 5, 0], np.int32, start_index=2, sample_count=5),
]


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___copy___makes_shallow_copy(value: AnalogWaveform[Any]) -> None:
    new_value = copy.copy(value)

    _assert_shallow_copy(new_value, value)


def _assert_shallow_copy(value: AnalogWaveform[Any], other: AnalogWaveform[Any]) -> None:
    assert value == other
    assert value is not other
    # _data may be a view of the original array.
    assert value._data is other._data or value._data.base is other._data
    assert value._extended_properties is other._extended_properties
    assert value._timing is other._timing
    assert value._scale_mode is other._scale_mode


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___deepcopy___makes_shallow_copy(value: AnalogWaveform[Any]) -> None:
    new_value = copy.deepcopy(value)

    _assert_deep_copy(new_value, value)


def _assert_deep_copy(value: AnalogWaveform[Any], other: AnalogWaveform[Any]) -> None:
    assert value == other
    assert value is not other
    assert value._data is not other._data and value._data.base is not other._data
    assert value._extended_properties is not other._extended_properties
    if other._timing is not Timing.empty:
        assert value._timing is not other._timing
    if other._scale_mode is not NO_SCALING:
        assert value._scale_mode is not other._scale_mode


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___pickle_unpickle___makes_deep_copy(
    value: AnalogWaveform[Any],
) -> None:
    new_value = pickle.loads(pickle.dumps(value))

    _assert_deep_copy(new_value, value)


def test___waveform___pickle___references_public_modules() -> None:
    value = AnalogWaveform(
        raw_data=np.array([1, 2, 3], np.float64),
        extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"},
        timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1)),
        scale_mode=LinearScaleMode(2.0, 1.0),
    )

    value_bytes = pickle.dumps(value)

    assert b"nitypes.waveform" in value_bytes
    assert b"nitypes.waveform._analog" not in value_bytes
    assert b"nitypes.waveform._extended_properties" not in value_bytes
    assert b"nitypes.waveform._numeric" not in value_bytes
    assert b"nitypes.waveform._timing" not in value_bytes
    assert b"nitypes.waveform._scaling" not in value_bytes


@pytest.mark.parametrize(
    "pickled_value, expected",
    [
        # nitypes 1.0.0
        (
            b"\x80\x04\x95n\x02\x00\x00\x00\x00\x00\x00\x8c\x08builtins\x94\x8c\x07getattr\x94\x93\x94\x8c\x10nitypes.waveform\x94\x8c\x0eAnalogWaveform\x94\x93\x94\x8c\t_unpickle\x94\x86\x94R\x94K\x03\x8c\x05numpy\x94\x8c\x05dtype\x94\x93\x94\x8c\x02f8\x94\x89\x88\x87\x94R\x94(K\x03\x8c\x01<\x94NNNJ\xff\xff\xff\xffJ\xff\xff\xff\xffK\x00t\x94b\x86\x94}\x94(\x8c\x08raw_data\x94\x8c\x16numpy._core.multiarray\x94\x8c\x0c_reconstruct\x94\x93\x94h\t\x8c\x07ndarray\x94\x93\x94K\x00\x85\x94C\x01b\x94\x87\x94R\x94(K\x01K\x03\x85\x94h\x0e\x89C\x18\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x08@\x94t\x94b\x8c\x13extended_properties\x94h\x03\x8c\x1aExtendedPropertyDictionary\x94\x93\x94)\x81\x94N}\x94\x8c\x0b_properties\x94}\x94(\x8c\x0eNI_ChannelName\x94\x8c\x08Dev1/ai0\x94\x8c\x12NI_UnitDescription\x94\x8c\x05Volts\x94us\x86\x94b\x8c\x18copy_extended_properties\x94\x89\x8c\x06timing\x94h\x02h\x03\x8c\x06Timing\x94\x93\x94h\x06\x86\x94R\x94(h\x03\x8c\x12SampleIntervalMode\x94\x93\x94K\x01\x85\x94R\x94NN\x8c\x08datetime\x94\x8c\ttimedelta\x94\x93\x94K\x00K\x00M\xe8\x03\x87\x94R\x94Nt\x94}\x94\x86\x94R\x94\x8c\nscale_mode\x94h\x03\x8c\x0fLinearScaleMode\x94\x93\x94)\x81\x94N}\x94(\x8c\x05_gain\x94G@\x00\x00\x00\x00\x00\x00\x00\x8c\x07_offset\x94G?\xf0\x00\x00\x00\x00\x00\x00u\x86\x94bu\x86\x94R\x94.",
            AnalogWaveform(
                raw_data=np.array([1, 2, 3], np.float64),
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"},
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1)),
                scale_mode=LinearScaleMode(2.0, 1.0),
            ),
        ),
    ],
)
def test___pickled_value___unpickle___is_compatible(
    pickled_value: bytes, expected: AnalogWaveform[Any]
) -> None:
    new_value = pickle.loads(pickled_value)
    assert new_value == expected
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/waveform/test_complex_waveform.py sha256=830f5664f0d5d1125f97b48be083dee953b41c8ebad0540edd57a3f8c33bd0d1 bytes=29387 -->
## FILE: tests/unit/waveform/test_complex_waveform.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/waveform/test_complex_waveform.py`
- sha256: `830f5664f0d5d1125f97b48be083dee953b41c8ebad0540edd57a3f8c33bd0d1`
- bytes: 29387

````python
from __future__ import annotations

import copy
import datetime as dt
import pickle
from collections.abc import Sequence
from typing import Any

import hightime as ht
import numpy as np
import numpy.typing as npt
import pytest
from typing_extensions import assert_type

from nitypes.complex import ComplexInt32Base, ComplexInt32DType
from nitypes.waveform import NO_SCALING, ComplexWaveform, LinearScaleMode, Timing


###############################################################################
# create
###############################################################################
def test___sample_count_and_complexint32_dtype___create___creates_waveform_with_sample_count_and_dtype() -> (
    None
):
    waveform = ComplexWaveform(10, ComplexInt32DType)

    assert waveform.sample_count == waveform.capacity == len(waveform.raw_data) == 10
    assert waveform.dtype == ComplexInt32DType
    assert_type(waveform, ComplexWaveform[ComplexInt32Base])


def test___sample_count_and_complex64_dtype___create___creates_waveform_with_sample_count_and_dtype() -> (
    None
):
    waveform = ComplexWaveform(10, np.complex64)

    assert waveform.sample_count == waveform.capacity == len(waveform.raw_data) == 10
    assert waveform.dtype == np.complex64
    assert_type(waveform, ComplexWaveform[np.complex64])


def test___sample_count_and_complex128_dtype___create___creates_waveform_with_sample_count_and_dtype() -> (
    None
):
    waveform = ComplexWaveform(10, np.complex128)

    assert waveform.sample_count == waveform.capacity == len(waveform.raw_data) == 10
    assert waveform.dtype == np.complex128
    assert_type(waveform, ComplexWaveform[np.complex128])


def test___sample_count_and_unknown_structured_dtype___create___raises_type_error() -> None:
    dtype = np.dtype([("a", np.int16), ("b", np.int32)])

    with pytest.raises(TypeError) as exc:
        waveform = ComplexWaveform(10, dtype)

        # ComplexWaveform currently cannot distinguish between ComplexInt32DType and other
        # structured data types at type-checking time.
        assert_type(waveform, ComplexWaveform[ComplexInt32Base])

    assert exc.value.args[0].startswith("The requested data type is not supported.")
    assert "Data type: [('a', '<i2'), ('b', '<i4')]" in exc.value.args[0]


def test___sample_count_and_structured_dtype_str___create___raises_type_error() -> None:
    with pytest.raises(TypeError) as exc:
        _ = ComplexWaveform(10, "i2, i2")

    assert exc.value.args[0].startswith("The requested data type is not supported.")
    assert "Data type: [('f0', '<i2'), ('f1', '<i2')]" in exc.value.args[0]


@pytest.mark.parametrize("dtype", [np.int32, np.float64, np.str_])
def test___sample_count_and_unsupported_dtype___create___raises_type_error(
    dtype: npt.DTypeLike,
) -> None:
    with pytest.raises(TypeError) as exc:
        _ = ComplexWaveform(10, dtype)

    assert exc.value.args[0].startswith("The requested data type is not supported.")


def test___dtype_str_with_unsupported_traw_hint___create___mypy_type_var_warning() -> None:
    waveform1: ComplexWaveform[np.int32] = ComplexWaveform(dtype="complex64")  # type: ignore[type-var]
    waveform2: ComplexWaveform[np.float64] = ComplexWaveform(dtype="complex64")  # type: ignore[type-var]
    waveform3: ComplexWaveform[np.str_] = ComplexWaveform(dtype="complex64")  # type: ignore[type-var]
    _ = waveform1, waveform2, waveform3


def test___dtype_str_with_traw_hint___create___narrows_traw() -> None:
    waveform: ComplexWaveform[np.complex64] = ComplexWaveform(dtype="complex64")

    assert_type(waveform, ComplexWaveform[np.complex64])


###############################################################################
# from_array_1d
###############################################################################
def test___complexint32_ndarray___from_array_1d___creates_waveform_with_complexint32_dtype() -> (
    None
):
    data = np.array([(1, 2), (3, -4)], ComplexInt32DType)

    waveform = ComplexWaveform.from_array_1d(data)

    assert waveform.raw_data.tolist() == data.tolist()
    assert waveform.dtype == ComplexInt32DType
    assert_type(waveform, ComplexWaveform[ComplexInt32Base])


def test___complex64_ndarray___from_array_1d___creates_waveform_with_complex64_dtype() -> None:
    data = np.array([1.1 + 2.2j, 3.3 - 4.4j], np.complex64)

    waveform = ComplexWaveform.from_array_1d(data)

    assert waveform.raw_data.tolist() == data.tolist()
    assert waveform.dtype == np.complex64
    assert_type(waveform, ComplexWaveform[np.complex64])


def test___complex128_ndarray___from_array_1d___creates_waveform_with_complex128_dtype() -> None:
    data = np.array([1.1 + 2.2j, 3.3 - 4.4j], np.complex128)

    waveform = ComplexWaveform.from_array_1d(data)

    assert waveform.raw_data.tolist() == data.tolist()
    assert waveform.dtype == np.complex128
    assert_type(waveform, ComplexWaveform[np.complex128])


def test___complex_list_with_dtype___from_array_1d___creates_waveform_with_specified_dtype() -> (
    None
):
    data = [1.1 + 2.2j, 3.3 - 4.4j]

    waveform = ComplexWaveform.from_array_1d(data, np.complex64)

    assert waveform.raw_data.tolist() == pytest.approx(data)
    assert waveform.dtype == np.complex64
    assert_type(waveform, ComplexWaveform[np.complex64])


def test___complex_list_with_dtype_str___from_array_1d___creates_waveform_with_specified_dtype() -> (
    None
):
    data = [1.1 + 2.2j, 3.3 - 4.4j]

    waveform = ComplexWaveform.from_array_1d(data, "complex64")

    assert waveform.raw_data.tolist() == pytest.approx(data)
    assert waveform.dtype == np.complex64
    assert_type(waveform, ComplexWaveform[Any])  # dtype not inferred from string


###############################################################################
# from_array_2d
###############################################################################
def test___complexint32_ndarray___from_array_2d___creates_waveform_with_complexint32_dtype() -> (
    None
):
    data = np.array([[(1, 2), (3, -4), (-5, 6)], [(-7 - 8), (9, 10), (11, 12)]], ComplexInt32DType)

    waveforms = ComplexWaveform.from_array_2d(data)

    assert_type(waveforms, Sequence[ComplexWaveform[ComplexInt32Base]])
    assert len(waveforms) == 2
    for i in range(len(waveforms)):
        assert waveforms[i].raw_data.tolist() == data[i].tolist()
        assert waveforms[i].dtype == ComplexInt32DType
        assert_type(waveforms[i], ComplexWaveform[ComplexInt32Base])


def test___complex64_ndarray___from_array_2d___creates_waveform_with_complex64_dtype() -> None:
    data = np.array([[1 + 2j, 3 - 4j, -5 + 6j], [-7 - 8j, 9 + 10j, 11 + 12j]], np.complex64)

    waveforms = ComplexWaveform.from_array_2d(data)

    assert_type(waveforms, Sequence[ComplexWaveform[np.complex64]])
    assert len(waveforms) == 2
    for i in range(len(waveforms)):
        assert waveforms[i].raw_data.tolist() == data[i].tolist()
        assert waveforms[i].dtype == np.complex64
        assert_type(waveforms[i], ComplexWaveform[np.complex64])


def test___complex128_ndarray___from_array_2d___creates_waveform_with_complex128_dtype() -> None:
    data = np.array([[1 + 2j, 3 - 4j, -5 + 6j], [-7 - 8j, 9 + 10j, 11 + 12j]], np.complex128)

    waveforms = ComplexWaveform.from_array_2d(data)

    assert_type(waveforms, Sequence[ComplexWaveform[np.complex128]])
    assert len(waveforms) == 2
    for i in range(len(waveforms)):
        assert waveforms[i].raw_data.tolist() == data[i].tolist()
        assert waveforms[i].dtype == np.complex128
        assert_type(waveforms[i], ComplexWaveform[np.complex128])


def test___complex_list_list_with_dtype___from_array_2d___creates_waveform_with_specified_dtype() -> (
    None
):
    data = [[1 + 2j, 3 - 4j, -5 + 6j], [-7 - 8j, 9 + 10j, 11 + 12j]]

    waveforms = ComplexWaveform.from_array_2d(data, np.complex64)

    assert_type(waveforms, Sequence[ComplexWaveform[np.complex64]])
    assert len(waveforms) == 2
    for i in range(len(waveforms)):
        assert waveforms[i].raw_data.tolist() == data[i]
        assert waveforms[i].dtype == np.complex64
        assert_type(waveforms[i], ComplexWaveform[np.complex64])


def test___int_list_list_with_dtype_str___from_array_2d___creates_waveform_with_specified_dtype() -> (
    None
):
    data = [[1 + 2j, 3 - 4j, -5 + 6j], [-7 - 8j, 9 + 10j, 11 + 12j]]

    waveforms = ComplexWaveform.from_array_2d(data, "complex64")

    assert_type(waveforms, Sequence[ComplexWaveform[Any]])  # dtype not inferred from string
    assert len(waveforms) == 2
    for i in range(len(waveforms)):
        assert waveforms[i].raw_data.tolist() == data[i]
        assert waveforms[i].dtype == np.complex64
        assert_type(waveforms[i], ComplexWaveform[Any])  # dtype not inferred from string


###############################################################################
# raw_data
###############################################################################
def test___complexint32_waveform___raw_data___returns_complexint32_data() -> None:
    waveform = ComplexWaveform.from_array_1d([(1, 2), (3, -4)], ComplexInt32DType)

    raw_data = waveform.raw_data

    assert_type(raw_data, npt.NDArray[ComplexInt32Base])
    assert isinstance(raw_data, np.ndarray) and raw_data.dtype == ComplexInt32DType
    assert [x.item() for x in raw_data] == [(1, 2), (3, -4)]


def test___complex64_waveform___raw_data___returns_complex64_data() -> None:
    waveform = ComplexWaveform.from_array_1d([1 + 2j, 3 - 4j], np.complex64)

    raw_data = waveform.raw_data

    assert_type(raw_data, npt.NDArray[np.complex64])
    assert isinstance(raw_data, np.ndarray) and raw_data.dtype == np.complex64
    assert list(raw_data) == [1 + 2j, 3 - 4j]


###############################################################################
# scaled_data
###############################################################################
def test___complexint32_waveform___scaled_data___converts_to_complex128() -> None:
    waveform = ComplexWaveform.from_array_1d([(1, 2), (3, -4)], ComplexInt32DType)

    scaled_data = waveform.scaled_data

    assert_type(scaled_data, npt.NDArray[np.complex128])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.complex128
    assert list(scaled_data) == [1 + 2j, 3 - 4j]


def test___complex64_waveform___scaled_data___converts_to_complex128() -> None:
    waveform = ComplexWaveform.from_array_1d([1 + 2j, 3 - 4j], np.complex64)

    scaled_data = waveform.scaled_data

    assert_type(scaled_data, npt.NDArray[np.complex128])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.complex128
    assert list(scaled_data) == [1 + 2j, 3 - 4j]


def test___complexint32_waveform_with_linear_scale___scaled_data___converts_to_complex128() -> None:
    waveform = ComplexWaveform.from_array_1d([(1, 2), (3, -4)], ComplexInt32DType)
    waveform.scale_mode = LinearScaleMode(2.0, 0.5)

    scaled_data = waveform.scaled_data

    assert_type(scaled_data, npt.NDArray[np.complex128])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.complex128
    assert list(scaled_data) == [2.5 + 4j, 6.5 - 8j]


def test___complex64_waveform_with_linear_scale___scaled_data___converts_to_complex128() -> None:
    waveform = ComplexWaveform.from_array_1d([1 + 2j, 3 - 4j], np.complex64)
    waveform.scale_mode = LinearScaleMode(2.0, 0.5)

    scaled_data = waveform.scaled_data

    assert_type(scaled_data, npt.NDArray[np.complex128])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.complex128
    assert list(scaled_data) == [2.5 + 4j, 6.5 - 8j]


###############################################################################
# get_scaled_data
###############################################################################
def test___complexint32_waveform_with_complex64_dtype___get_scaled_data___converts_to_complex64() -> (
    None
):
    waveform = ComplexWaveform.from_array_1d([(1, 2), (3, -4)], ComplexInt32DType)

    scaled_data = waveform.get_scaled_data(np.complex64)

    assert_type(scaled_data, npt.NDArray[np.complex64])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.complex64
    assert list(scaled_data) == [1 + 2j, 3 - 4j]


def test___complex64_waveform_with_complex64_dtype___get_scaled_data___does_not_convert() -> None:
    waveform = ComplexWaveform.from_array_1d([1 + 2j, 3 - 4j], np.complex64)

    scaled_data = waveform.get_scaled_data(np.complex64)

    assert_type(scaled_data, npt.NDArray[np.complex64])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.complex64
    assert list(scaled_data) == [1 + 2j, 3 - 4j]


def test___complexint32_waveform_with_unknown_structured_dtype___get_scaled_data___raises_type_error() -> (
    None
):
    waveform = ComplexWaveform.from_array_1d([(1, 2), (3, -4)], ComplexInt32DType)
    dtype = np.dtype([("a", np.int16), ("b", np.int16)])

    with pytest.raises(TypeError) as exc:
        _ = waveform.get_scaled_data(dtype)

    assert exc.value.args[0].startswith("The requested data type is not supported.")
    assert "Data type: [('a', '<i2'), ('b', '<i2')]" in exc.value.args[0]
    assert "Supported data types: complex64, complex128" in exc.value.args[0]


###############################################################################
# magic methods
###############################################################################
@pytest.mark.parametrize(
    "left, right",
    [
        (ComplexWaveform(), ComplexWaveform()),
        (ComplexWaveform(10), ComplexWaveform(10)),
        (ComplexWaveform(10, np.complex128), ComplexWaveform(10, np.complex128)),
        (ComplexWaveform(10, ComplexInt32DType), ComplexWaveform(10, ComplexInt32DType)),
        (
            ComplexWaveform(10, ComplexInt32DType, start_index=5, capacity=20),
            ComplexWaveform(10, ComplexInt32DType, start_index=5, capacity=20),
        ),
        (
            ComplexWaveform.from_array_1d([1 + 2j, 3 + 4j, 5 + 6j], np.complex128),
            ComplexWaveform.from_array_1d([1 + 2j, 3 + 4j, 5 + 6j], np.complex128),
        ),
        (
            ComplexWaveform.from_array_1d([(1, 2), (3, 4), (5, 6)], ComplexInt32DType),
            ComplexWaveform.from_array_1d([(1, 2), (3, 4), (5, 6)], ComplexInt32DType),
        ),
        (
            ComplexWaveform(
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
            ),
            ComplexWaveform(
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
            ),
        ),
        (
            ComplexWaveform(
                timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=1))
            ),
            ComplexWaveform(
                timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=1))
            ),
        ),
        (
            ComplexWaveform(
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"}
            ),
            ComplexWaveform(
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"}
            ),
        ),
        (
            ComplexWaveform(scale_mode=LinearScaleMode(2.0, 1.0)),
            ComplexWaveform(scale_mode=LinearScaleMode(2.0, 1.0)),
        ),
        # start_index and capacity may differ as long as raw_data and sample_count are the same.
        (
            ComplexWaveform(10, ComplexInt32DType, start_index=5, capacity=20),
            ComplexWaveform(10, ComplexInt32DType, start_index=10, capacity=25),
        ),
        (
            ComplexWaveform.from_array_1d(
                [0, 0, 1, 2, 3, 4, 5, 0], ComplexInt32DType, start_index=2, sample_count=5
            ),
            ComplexWaveform.from_array_1d(
                [0, 1, 2, 3, 4, 5, 0, 0, 0], ComplexInt32DType, start_index=1, sample_count=5
            ),
        ),
        # Same value, different time type
        (
            ComplexWaveform(
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
            ),
            ComplexWaveform(
                timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=1))
            ),
        ),
        (
            ComplexWaveform(
                timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=1))
            ),
            ComplexWaveform(
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
            ),
        ),
    ],
)
def test___same_value___equality___equal(
    left: ComplexWaveform[Any], right: ComplexWaveform[Any]
) -> None:
    assert left == right
    assert not (left != right)


@pytest.mark.parametrize(
    "left, right",
    [
        (ComplexWaveform(), ComplexWaveform(10)),
        (ComplexWaveform(10), ComplexWaveform(11)),
        (ComplexWaveform(10, np.complex128), ComplexWaveform(10, ComplexInt32DType)),
        (
            ComplexWaveform(15, ComplexInt32DType, start_index=5, capacity=20),
            ComplexWaveform(10, ComplexInt32DType, start_index=5, capacity=20),
        ),
        (
            ComplexWaveform.from_array_1d([1 + 2j, 3 + 5j, 5 + 6j], np.complex128),
            ComplexWaveform.from_array_1d([1 + 2j, 3 + 4j, 5 + 6j], np.complex128),
        ),
        (
            ComplexWaveform.from_array_1d([(1, 2), (3, 4), (5, 6)], ComplexInt32DType),
            ComplexWaveform.from_array_1d([1 + 2j, 3 + 4j, 5 + 6j], np.complex128),
        ),
        (
            ComplexWaveform(
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
            ),
            ComplexWaveform(
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=2))
            ),
        ),
        (
            ComplexWaveform(
                timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=1))
            ),
            ComplexWaveform(
                timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=2))
            ),
        ),
        (
            ComplexWaveform(
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"}
            ),
            ComplexWaveform(
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Amps"}
            ),
        ),
        (
            ComplexWaveform(scale_mode=LinearScaleMode(2.0, 1.0)),
            ComplexWaveform(scale_mode=LinearScaleMode(2.0, 1.1)),
        ),
        (
            ComplexWaveform(scale_mode=NO_SCALING),
            ComplexWaveform(scale_mode=LinearScaleMode(2.0, 1.0)),
        ),
    ],
)
def test___different_value___equality___not_equal(
    left: ComplexWaveform[Any], right: ComplexWaveform[Any]
) -> None:
    assert not (left == right)
    assert left != right


@pytest.mark.parametrize(
    "value, expected_repr",
    [
        (ComplexWaveform(), "nitypes.waveform.ComplexWaveform(0)"),
        (
            ComplexWaveform(5),
            "nitypes.waveform.ComplexWaveform(5, raw_data=array([0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]))",
        ),
        (
            ComplexWaveform(5, np.complex128),
            "nitypes.waveform.ComplexWaveform(5, raw_data=array([0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]))",
        ),
        (ComplexWaveform(0, ComplexInt32DType), "nitypes.waveform.ComplexWaveform(0, void32)"),
        (
            ComplexWaveform(5, ComplexInt32DType),
            "nitypes.waveform.ComplexWaveform(5, void32, raw_data=array([(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],\n"
            "      dtype=[('real', '<i2'), ('imag', '<i2')]))",
        ),
        (
            ComplexWaveform(5, ComplexInt32DType, start_index=5, capacity=20),
            "nitypes.waveform.ComplexWaveform(5, void32, raw_data=array([(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],\n"
            "      dtype=[('real', '<i2'), ('imag', '<i2')]))",
        ),
        (
            ComplexWaveform.from_array_1d([1.23 + 3.45j, 6.78 - 9.01j], np.complex128),
            "nitypes.waveform.ComplexWaveform(2, raw_data=array([1.23+3.45j, 6.78-9.01j]))",
        ),
        (
            ComplexWaveform.from_array_1d([(1, 2), (3, 4), (5, 6)], ComplexInt32DType),
            "nitypes.waveform.ComplexWaveform(3, void32, raw_data=array([(1, 2), (3, 4), (5, 6)], dtype=[('real', '<i2'), ('imag', '<i2')]))",
        ),
        (
            ComplexWaveform(
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
            ),
            "nitypes.waveform.ComplexWaveform(0, timing=nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR, sample_interval=datetime.timedelta(microseconds=1000)))",
        ),
        (
            ComplexWaveform(
                timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=1))
            ),
            "nitypes.waveform.ComplexWaveform(0, timing=nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR, sample_interval=hightime.timedelta(microseconds=1000)))",
        ),
        (
            ComplexWaveform(
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"}
            ),
            "nitypes.waveform.ComplexWaveform(0, extended_properties={'NI_ChannelName': 'Dev1/ai0', 'NI_UnitDescription': 'Volts'})",
        ),
        (
            ComplexWaveform(scale_mode=LinearScaleMode(2.0, 1.0)),
            "nitypes.waveform.ComplexWaveform(0, scale_mode=nitypes.waveform.LinearScaleMode(2.0, 1.0))",
        ),
        (
            ComplexWaveform.from_array_1d(
                [(1, 2), (3, 4), (5, 6)],
                ComplexInt32DType,
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1)),
            ),
            "nitypes.waveform.ComplexWaveform(3, void32, raw_data=array([(1, 2), (3, 4), (5, 6)], dtype=[('real', '<i2'), ('imag', '<i2')]), timing=nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR, sample_interval=datetime.timedelta(microseconds=1000)))",
        ),
        (
            ComplexWaveform.from_array_1d(
                [(1, 2), (3, 4), (5, 6)],
                ComplexInt32DType,
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"},
            ),
            "nitypes.waveform.ComplexWaveform(3, void32, raw_data=array([(1, 2), (3, 4), (5, 6)], dtype=[('real', '<i2'), ('imag', '<i2')]), extended_properties={'NI_ChannelName': 'Dev1/ai0', 'NI_UnitDescription': 'Volts'})",
        ),
        (
            ComplexWaveform.from_array_1d(
                [(1, 2), (3, 4), (5, 6)], ComplexInt32DType, scale_mode=LinearScaleMode(2.0, 1.0)
            ),
            "nitypes.waveform.ComplexWaveform(3, void32, raw_data=array([(1, 2), (3, 4), (5, 6)], dtype=[('real', '<i2'), ('imag', '<i2')]), scale_mode=nitypes.waveform.LinearScaleMode(2.0, 1.0))",
        ),
    ],
)
def test___various_values___repr___looks_ok(
    value: ComplexWaveform[Any], expected_repr: str
) -> None:
    assert repr(value) == expected_repr


_VARIOUS_VALUES = [
    ComplexWaveform(),
    ComplexWaveform(10),
    ComplexWaveform(10, np.complex128),
    ComplexWaveform(10, ComplexInt32DType),
    ComplexWaveform(10, ComplexInt32DType, start_index=5, capacity=20),
    ComplexWaveform.from_array_1d([123 + 3.45j, 6.78 - 9.01j], np.complex128),
    ComplexWaveform.from_array_1d([(1, 2), (3, 4), (5, 6)], ComplexInt32DType),
    ComplexWaveform(timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))),
    ComplexWaveform(timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=1))),
    ComplexWaveform(
        extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"}
    ),
    ComplexWaveform(scale_mode=LinearScaleMode(2.0, 1.0)),
    ComplexWaveform(10, ComplexInt32DType, start_index=5, capacity=20),
    ComplexWaveform.from_array_1d(
        [(0, 0), (0, 0), (1, 1), (2, -2), (3, 33), (4, -44), (5, 50), (0, 0)],
        ComplexInt32DType,
        start_index=2,
        sample_count=5,
    ),
]


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___copy___makes_shallow_copy(value: ComplexWaveform[Any]) -> None:
    new_value = copy.copy(value)

    _assert_shallow_copy(new_value, value)


def _assert_shallow_copy(value: ComplexWaveform[Any], other: ComplexWaveform[Any]) -> None:
    assert value == other
    assert value is not other
    # _data may be a view of the original array.
    assert value._data is other._data or value._data.base is other._data
    assert value._extended_properties is other._extended_properties
    assert value._timing is other._timing
    assert value._scale_mode is other._scale_mode


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___deepcopy___makes_shallow_copy(value: ComplexWaveform[Any]) -> None:
    new_value = copy.deepcopy(value)

    _assert_deep_copy(new_value, value)


def _assert_deep_copy(value: ComplexWaveform[Any], other: ComplexWaveform[Any]) -> None:
    assert value == other
    assert value is not other
    assert value._data is not other._data and value._data.base is not other._data
    assert value._extended_properties is not other._extended_properties
    if other._timing is not Timing.empty:
        assert value._timing is not other._timing
    if other._scale_mode is not NO_SCALING:
        assert value._scale_mode is not other._scale_mode


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___pickle_unpickle___makes_deep_copy(
    value: ComplexWaveform[Any],
) -> None:
    new_value = pickle.loads(pickle.dumps(value))

    _assert_deep_copy(new_value, value)


def test___waveform___pickle___references_public_modules() -> None:
    value = ComplexWaveform(
        raw_data=np.array([1, 2, 3], np.complex128),
        extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"},
        timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1)),
        scale_mode=LinearScaleMode(2.0, 1.0),
    )

    value_bytes = pickle.dumps(value)

    assert b"nitypes.waveform" in value_bytes
    assert b"nitypes.waveform._complex" not in value_bytes
    assert b"nitypes.waveform._extended_properties" not in value_bytes
    assert b"nitypes.waveform._numeric" not in value_bytes
    assert b"nitypes.waveform._timing" not in value_bytes
    assert b"nitypes.waveform._scaling" not in value_bytes


@pytest.mark.parametrize(
    "pickled_value, expected",
    [
        # nitypes 1.0.0
        (
            b"\x80\x04\x95\x88\x02\x00\x00\x00\x00\x00\x00\x8c\x08builtins\x94\x8c\x07getattr\x94\x93\x94\x8c\x10nitypes.waveform\x94\x8c\x0fComplexWaveform\x94\x93\x94\x8c\t_unpickle\x94\x86\x94R\x94K\x03\x8c\x05numpy\x94\x8c\x05dtype\x94\x93\x94\x8c\x03c16\x94\x89\x88\x87\x94R\x94(K\x03\x8c\x01<\x94NNNJ\xff\xff\xff\xffJ\xff\xff\xff\xffK\x00t\x94b\x86\x94}\x94(\x8c\x08raw_data\x94\x8c\x16numpy._core.multiarray\x94\x8c\x0c_reconstruct\x94\x93\x94h\t\x8c\x07ndarray\x94\x93\x94K\x00\x85\x94C\x01b\x94\x87\x94R\x94(K\x01K\x03\x85\x94h\x0e\x89C0\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x00\x00\x94t\x94b\x8c\x13extended_properties\x94h\x03\x8c\x1aExtendedPropertyDictionary\x94\x93\x94)\x81\x94N}\x94\x8c\x0b_properties\x94}\x94(\x8c\x0eNI_ChannelName\x94\x8c\x08Dev1/ai0\x94\x8c\x12NI_UnitDescription\x94\x8c\x05Volts\x94us\x86\x94b\x8c\x18copy_extended_properties\x94\x89\x8c\x06timing\x94h\x02h\x03\x8c\x06Timing\x94\x93\x94h\x06\x86\x94R\x94(h\x03\x8c\x12SampleIntervalMode\x94\x93\x94K\x01\x85\x94R\x94NN\x8c\x08datetime\x94\x8c\ttimedelta\x94\x93\x94K\x00K\x00M\xe8\x03\x87\x94R\x94Nt\x94}\x94\x86\x94R\x94\x8c\nscale_mode\x94h\x03\x8c\x0fLinearScaleMode\x94\x93\x94)\x81\x94N}\x94(\x8c\x05_gain\x94G@\x00\x00\x00\x00\x00\x00\x00\x8c\x07_offset\x94G?\xf0\x00\x00\x00\x00\x00\x00u\x86\x94bu\x86\x94R\x94.",
            ComplexWaveform(
                raw_data=np.array([1, 2, 3], np.complex128),
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"},
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1)),
                scale_mode=LinearScaleMode(2.0, 1.0),
            ),
        ),
    ],
)
def test___pickled_value___unpickle___is_compatible(
    pickled_value: bytes, expected: ComplexWaveform[Any]
) -> None:
    new_value = pickle.loads(pickled_value)
    assert new_value == expected
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/waveform/test_digital_state.py sha256=1c029cfe576f58644162aaf3649cf44e2c8df8371b5b1af20d5b630882264422 bytes=2679 -->
## FILE: tests/unit/waveform/test_digital_state.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/waveform/test_digital_state.py`
- sha256: `1c029cfe576f58644162aaf3649cf44e2c8df8371b5b1af20d5b630882264422`
- bytes: 2679

````python
from __future__ import annotations

import pytest

from nitypes.waveform import DigitalState


@pytest.mark.parametrize(
    "state, expected_char",
    [
        (DigitalState.FORCE_DOWN, "0"),
        (DigitalState.COMPARE_HIGH, "H"),
        (DigitalState.COMPARE_UNKNOWN, "X"),
    ],
)
def test___state___to_char___returns_char(state: DigitalState, expected_char: str) -> None:
    assert DigitalState.to_char(state) == expected_char


@pytest.mark.parametrize("state", [-1, 8, 255])
def test___invalid_state___to_char___raises_key_error(state: DigitalState) -> None:
    with pytest.raises(KeyError) as exc:
        _ = DigitalState.to_char(state)

    assert exc.value.args[0] == state


@pytest.mark.parametrize("state", [-1, 8, 255])
def test___invalid_state_errors_replace___to_char___returns_question_mark(
    state: DigitalState,
) -> None:
    assert DigitalState.to_char(state, errors="replace") == "?"


@pytest.mark.parametrize(
    "char, expected_state",
    [
        ("0", DigitalState.FORCE_DOWN),
        ("H", DigitalState.COMPARE_HIGH),
        ("X", DigitalState.COMPARE_UNKNOWN),
    ],
)
def test___char___from_char___returns_state(char: str, expected_state: DigitalState) -> None:
    assert DigitalState.from_char(char) == expected_state


@pytest.mark.parametrize("char", ["}", "?", "A"])
def test___invalid_char___from_char___raises_key_error(char: str) -> None:
    with pytest.raises(KeyError) as exc:
        _ = DigitalState.from_char(char)

    assert exc.value.args[0] == char


@pytest.mark.parametrize(
    "char1, char2, expected_result",
    [
        ("0", "0", False),
        ("0", "L", False),
        ("0", "H", True),
        ("1", "1", False),
        ("1", "H", False),
        ("1", "L", True),
        ("1", "0", True),
        ("1", "X", False),
        ("0", "X", False),
        ("H", "L", True),
    ],
)
def test___states___test___returns_pass_fail(char1: str, char2: str, expected_result: bool) -> None:
    state1 = DigitalState.from_char(char1)
    state2 = DigitalState.from_char(char2)

    assert DigitalState.test(state1, state2) == expected_result
    assert DigitalState.test(state2, state1) == expected_result


@pytest.mark.parametrize(
    "state1, state2",
    [
        (DigitalState.FORCE_DOWN, -1),
        (8, DigitalState.COMPARE_UNKNOWN),
    ],
)
def test___invalid_state___test___raises_value_error(
    state1: DigitalState, state2: DigitalState
) -> None:
    with pytest.raises(ValueError) as exc:
        _ = DigitalState.test(state1, state2)

    assert "is not a valid DigitalState" in exc.value.args[0]
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/waveform/test_digital_waveform.py sha256=1821ae182492b72d2c7fa939cb61ff8564440b06c3d5485890f7ab78a16785d1 bytes=85988 -->
## FILE: tests/unit/waveform/test_digital_waveform.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/waveform/test_digital_waveform.py`
- sha256: `1821ae182492b72d2c7fa939cb61ff8564440b06c3d5485890f7ab78a16785d1`
- bytes: 85988

````python
from __future__ import annotations

import array
import copy
import datetime as dt
import pickle
import weakref
from collections.abc import Sequence
from typing import Any, Union

import hightime as ht
import numpy as np
import numpy.typing as npt
import pytest
from typing_extensions import assert_type

import nitypes.bintime as bt
import nitypes.waveform.errors as wfmex
import nitypes.waveform.warnings as wfmwarn
from nitypes._numpy import bool as _np_bool
from nitypes.waveform import (
    DigitalState,
    DigitalWaveform,
    DigitalWaveformFailure,
    SampleIntervalMode,
    Timing,
)


###############################################################################
# create
###############################################################################
def test___no_args___create___creates_empty_waveform_with_default_signal_count_and_default_dtype() -> (
    None
):
    waveform = DigitalWaveform()

    assert waveform.sample_count == waveform.capacity == len(waveform.data) == 0
    assert waveform.signal_count == 1
    assert waveform.dtype == np.uint8
    assert_type(waveform, DigitalWaveform[np.uint8])


def test___sample_count___create___creates_waveform_with_sample_count_default_signal_count_and_default_dtype() -> (
    None
):
    waveform = DigitalWaveform(10)

    assert waveform.sample_count == waveform.capacity == len(waveform.data) == 10
    assert waveform.signal_count == 1
    assert waveform.dtype == np.uint8
    assert_type(waveform, DigitalWaveform[np.uint8])


def test___sample_count_signal_count_and_dtype___create___creates_waveform_with_sample_count_and_dtype() -> (
    None
):
    waveform = DigitalWaveform(10, 3, _np_bool)

    assert waveform.sample_count == waveform.capacity == len(waveform.data) == 10
    assert waveform.signal_count == 3
    assert waveform.dtype == _np_bool
    # https://github.com/microsoft/pyright/issues/10631 - Passing a generic type via a parameter of
    # type type[T] can leak an unsolved type variable
    assert_type(waveform, DigitalWaveform[_np_bool])  # pyright: ignore[reportAssertTypeFailure]


def test___sample_count_and_dtype_str___create___creates_waveform_with_sample_count_and_dtype() -> (
    None
):
    waveform = DigitalWaveform(10, dtype="i1")

    assert waveform.sample_count == waveform.capacity == len(waveform.data) == 10
    assert waveform.signal_count == 1
    assert waveform.dtype == np.int8
    assert_type(waveform, DigitalWaveform[Any])  # dtype not inferred from string


def test___sample_count_and_dtype_any___create___creates_waveform_with_sample_count_and_dtype() -> (
    None
):
    dtype: np.dtype[Any] = np.dtype(np.int8)
    waveform = DigitalWaveform(10, dtype=dtype)

    assert waveform.sample_count == waveform.capacity == len(waveform.data) == 10
    assert waveform.signal_count == 1
    assert waveform.dtype == np.int8
    assert_type(waveform, DigitalWaveform[Any])  # dtype not inferred from np.dtype[Any]


def test___sample_count_dtype_and_capacity___create___creates_waveform_with_sample_count_dtype_and_capacity() -> (
    None
):
    waveform = DigitalWaveform(10, dtype=np.int8, capacity=20)

    assert waveform.sample_count == len(waveform.data) == 10
    assert waveform.signal_count == 1
    assert waveform.capacity == 20
    assert waveform.dtype == np.int8
    assert_type(waveform, DigitalWaveform[np.int8])


@pytest.mark.parametrize("dtype", [np.complex128, np.str_, np.void, "u1, u1"])
def test___sample_count_and_unsupported_dtype___create___raises_type_error(
    dtype: npt.DTypeLike,
) -> None:
    with pytest.raises(TypeError) as exc:
        _ = DigitalWaveform(10, dtype=dtype)

    assert exc.value.args[0].startswith("The requested data type is not supported.")


def test___dtype_str_with_unsupported_tdata_hint___create___mypy_type_var_warning() -> None:
    waveform1: DigitalWaveform[np.complex128] = DigitalWaveform(dtype="u1")  # type: ignore[type-var]
    waveform2: DigitalWaveform[np.str_] = DigitalWaveform(dtype="u1")  # type: ignore[type-var]
    waveform3: DigitalWaveform[np.void] = DigitalWaveform(dtype="u1")  # type: ignore[type-var]
    _ = waveform1, waveform2, waveform3


def test___dtype_str_with_tdata_hint___create___narrows_tdata() -> None:
    waveform: DigitalWaveform[np.uint8] = DigitalWaveform(dtype="u1")

    assert_type(waveform, DigitalWaveform[np.uint8])


@pytest.mark.parametrize(
    "default_value",
    [
        False,
        True,
        0,
        1,
        3,
        DigitalState.FORCE_DOWN,
        DigitalState.FORCE_UP,
        DigitalState.COMPARE_VALID,
    ],
)
def test___default_value___create___creates_waveform_with_default_value(
    default_value: bool | int | DigitalState,
) -> None:
    waveform = DigitalWaveform(2, 3, default_value=default_value)

    assert waveform.sample_count == len(waveform.data) == 2
    assert waveform.signal_count == 3
    # default_value does not affect the dtype.
    assert waveform.dtype == np.uint8
    assert_type(waveform, DigitalWaveform[np.uint8])
    assert waveform.data.tolist() == [
        [default_value, default_value, default_value],
        [default_value, default_value, default_value],
    ]


###############################################################################
# from_lines
###############################################################################
def test___uint8_ndarray___from_lines___creates_waveform_with_uint8_dtype() -> None:
    array = np.array([0, 1, 2, 3], np.uint8)

    waveform = DigitalWaveform.from_lines(array)

    assert_type(waveform, DigitalWaveform[np.uint8])
    assert isinstance(waveform, DigitalWaveform) and waveform.dtype == np.uint8
    assert waveform.data.tolist() == [[0], [1], [2], [3]]


def test___bool_ndarray___from_lines___creates_waveform_with_bool_dtype() -> None:
    array = np.array([False, True, False], _np_bool)

    waveform = DigitalWaveform.from_lines(array)

    assert_type(waveform, DigitalWaveform[_np_bool])
    assert isinstance(waveform, DigitalWaveform) and waveform.dtype == _np_bool
    assert waveform.data.tolist() == [[False], [True], [False]]


def test___int_list_with_int8_dtype___from_lines___creates_waveform_with_int8_dtype() -> None:
    waveform = DigitalWaveform.from_lines([0, 1, 2, 3], np.int8)

    assert_type(waveform, DigitalWaveform[np.int8])
    assert isinstance(waveform, DigitalWaveform) and waveform.dtype == np.int8
    assert waveform.data.tolist() == [[0], [1], [2], [3]]


def test___int_list_1d___from_lines___creates_waveform_with_one_signal() -> None:
    waveform = DigitalWaveform.from_lines([0, 1, 2, 3])

    assert waveform.sample_count == 4
    assert waveform.signal_count == 1
    assert waveform.data.tolist() == [[0], [1], [2], [3]]


def test___int_list_2d___from_lines___creates_waveform_with_multi_signal() -> None:
    waveform = DigitalWaveform.from_lines([[0, 1, 2], [3, 4, 5]])

    assert waveform.sample_count == 2
    assert waveform.signal_count == 3
    assert waveform.data.tolist() == [[0, 1, 2], [3, 4, 5]]


def test___ndarray_1d___from_lines___creates_waveform_with_one_signal() -> None:
    array = np.array([0, 1, 2, 3], np.uint8)

    waveform = DigitalWaveform.from_lines(array)

    assert waveform.sample_count == 4
    assert waveform.signal_count == 1
    assert waveform.data.tolist() == [[0], [1], [2], [3]]


def test___ndarray_2d___from_lines___creates_waveform_with_multi_signal() -> None:
    array = np.array([[0, 1, 2], [3, 4, 5]], np.uint8)

    waveform = DigitalWaveform.from_lines(array)

    assert waveform.sample_count == 2
    assert waveform.signal_count == 3
    assert waveform.data.tolist() == [[0, 1, 2], [3, 4, 5]]


###############################################################################
# from_port
###############################################################################
def test___uint8_ndarray___from_port_bitorder_little___creates_waveform_with_8_lines() -> None:
    array = np.array([0, 1, 2, 3, 0xFF, 0x12, 0x34], np.uint8)

    waveform = DigitalWaveform.from_port(array, bitorder="little")

    assert waveform.sample_count == 7
    assert waveform.signal_count == 8
    assert waveform.data.tolist() == [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 0],
    ]


def test___uint16_ndarray___from_port_bitorder_little___creates_waveform_with_16_lines() -> None:
    array = np.array([0, 1, 2, 3, 0xFFFF, 0x1234, 0x5678], np.uint16)

    waveform = DigitalWaveform.from_port(array, bitorder="little")

    assert waveform.sample_count == 7
    assert waveform.signal_count == 16
    assert waveform.data.tolist() == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
    ]


def test___int_list_and_mask___from_port_bitorder_little___creates_waveform_with_masked_lines() -> (
    None
):
    array = [0, 1, 2, 3, 0xFFFF, 0x1234, 0x5678]

    waveform = DigitalWaveform.from_port(array, mask=0xFFFF, bitorder="little")

    assert waveform.sample_count == 7
    assert waveform.signal_count == 16
    assert waveform.data.tolist() == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
    ]


def test___mask___from_port_bitorder_little___creates_waveform_with_masked_lines() -> None:
    array = np.array([0xFF, 0x12, 0x34], np.uint8)

    waveform_lo = DigitalWaveform.from_port(array, 0x0F, bitorder="little")
    waveform_hi = DigitalWaveform.from_port(array, 0xF0, bitorder="little")

    assert waveform_lo.sample_count == 3
    assert waveform_lo.signal_count == 4
    assert waveform_lo.data.tolist() == [
        [1, 1, 1, 1],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
    ]
    assert waveform_hi.sample_count == 3
    assert waveform_hi.signal_count == 4
    assert waveform_hi.data.tolist() == [
        [1, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 1, 0, 0],
    ]


def test___bool_dtype___from_port_bitorder_little___creates_waveform_with_bool_dtype() -> None:
    array = np.array([0, 1, 2, 3, 0xFF, 0x12, 0x34], np.uint8)

    waveform = DigitalWaveform.from_port(array, dtype=_np_bool, bitorder="little")

    assert waveform.sample_count == 7
    assert waveform.signal_count == 8
    assert waveform.data.tolist() == [
        [False, False, False, False, False, False, False, False],
        [True, False, False, False, False, False, False, False],
        [False, True, False, False, False, False, False, False],
        [True, True, False, False, False, False, False, False],
        [True, True, True, True, True, True, True, True],
        [False, True, False, False, True, False, False, False],
        [False, False, True, False, True, True, False, False],
    ]


def test___array_subset___from_port_bitorder_little___creates_waveform_with_array_subset() -> None:
    array = np.array([0, 1, 2, 3, 0xFF, 0x12, 0x34], np.uint8)

    waveform = DigitalWaveform.from_port(array, start_index=2, sample_count=4, bitorder="little")

    assert waveform.start_index == 2
    assert waveform.sample_count == 4
    assert waveform.signal_count == 8
    assert waveform.data.tolist() == [
        [0, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 0, 0, 1, 0, 0, 0],
    ]


def test___uint8_ndarray___from_port___creates_waveform_with_8_lines() -> None:
    array = np.array([0, 1, 2, 3, 0xFF, 0x12, 0x34], np.uint8)

    waveform = DigitalWaveform.from_port(array)

    assert waveform.sample_count == 7
    assert waveform.signal_count == 8
    assert waveform.data.tolist() == [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 1, 1, 0, 1, 0, 0],
    ]


def test___uint16_ndarray___from_port___creates_waveform_with_16_lines() -> None:
    array = np.array([0, 1, 2, 3, 0xFFFF, 0x1234, 0x5678], np.uint16)

    waveform = DigitalWaveform.from_port(array)

    assert waveform.sample_count == 7
    assert waveform.signal_count == 16
    assert waveform.data.tolist() == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    ]


def test___int_list_and_mask___from_port___creates_waveform_with_masked_lines() -> None:
    array = [0, 1, 2, 3, 0xFFFF, 0x1234, 0x5678]

    waveform = DigitalWaveform.from_port(array, mask=0xFFFF)

    assert waveform.sample_count == 7
    assert waveform.signal_count == 16
    assert waveform.data.tolist() == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    ]


def test___mask___from_port___creates_waveform_with_masked_lines() -> None:
    array = np.array([0xFF, 0x12, 0x34], np.uint8)

    waveform_lo = DigitalWaveform.from_port(array, 0x0F)
    waveform_hi = DigitalWaveform.from_port(array, 0xF0)

    assert waveform_lo.sample_count == 3
    assert waveform_lo.signal_count == 4
    assert waveform_lo.data.tolist() == [
        [1, 1, 1, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
    ]
    assert waveform_hi.sample_count == 3
    assert waveform_hi.signal_count == 4
    assert waveform_hi.data.tolist() == [
        [1, 1, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 1, 1],
    ]


def test___bool_dtype___from_port___creates_waveform_with_bool_dtype() -> None:
    array = np.array([0, 1, 2, 3, 0xFF, 0x12, 0x34], np.uint8)

    waveform = DigitalWaveform.from_port(array, dtype=_np_bool)

    assert waveform.sample_count == 7
    assert waveform.signal_count == 8
    assert waveform.data.tolist() == [
        [False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, True],
        [False, False, False, False, False, False, True, False],
        [False, False, False, False, False, False, True, True],
        [True, True, True, True, True, True, True, True],
        [False, False, False, True, False, False, True, False],
        [False, False, True, True, False, True, False, False],
    ]


def test___array_subset___from_port___creates_waveform_with_array_subset() -> None:
    array = np.array([0, 1, 2, 3, 0xFF, 0x12, 0x34], np.uint8)

    waveform = DigitalWaveform.from_port(array, start_index=2, sample_count=4)

    assert waveform.start_index == 2
    assert waveform.sample_count == 4
    assert waveform.signal_count == 8
    assert waveform.data.tolist() == [
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 1, 0],
    ]


###############################################################################
# from_ports
###############################################################################
def test___uint8_ndarray___from_ports_bitorder_little___creates_waveform_with_8_lines() -> None:
    array = np.array([[0, 1, 2], [0xFF, 0x12, 0x34]], np.uint8)

    waveforms = DigitalWaveform.from_ports(array, bitorder="little")

    assert len(waveforms) == 2
    assert waveforms[0].sample_count == 3
    assert waveforms[0].signal_count == 8
    assert waveforms[0].data.tolist() == [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
    ]
    assert waveforms[1].sample_count == 3
    assert waveforms[1].signal_count == 8
    assert waveforms[1].data.tolist() == [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 0],
    ]


def test___uint16_ndarray___from_ports_bitorder_little___creates_waveform_with_16_lines() -> None:
    array = np.array([[0, 1, 2], [0xFFFF, 0x1234, 0x5678]], np.uint16)

    waveforms = DigitalWaveform.from_ports(array, bitorder="little")

    assert len(waveforms) == 2
    assert waveforms[0].sample_count == 3
    assert waveforms[0].signal_count == 16
    assert waveforms[0].data.tolist() == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    assert waveforms[1].sample_count == 3
    assert waveforms[1].signal_count == 16
    assert waveforms[1].data.tolist() == [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
    ]


def test___int_list_and_mask___from_ports_bitorder_little___creates_waveform_with_masked_lines() -> (
    None
):
    array = [[0, 1, 2], [0xFFFF, 0x1234, 0x5678]]

    waveforms = DigitalWaveform.from_ports(array, masks=[0xFFFF, 0xFFFF], bitorder="little")

    assert len(waveforms) == 2
    assert waveforms[0].sample_count == 3
    assert waveforms[0].signal_count == 16
    assert waveforms[0].data.tolist() == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    assert waveforms[1].sample_count == 3
    assert waveforms[1].signal_count == 16
    assert waveforms[1].data.tolist() == [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
    ]


def test___masks___from_ports_bitorder_little___creates_waveform_with_masked_lines() -> None:
    array = np.array([[0x00, 0xFF], [0x12, 0x34]], np.uint8)

    waveforms = DigitalWaveform.from_ports(array, [0x0F, 0xF0], bitorder="little")

    assert len(waveforms) == 2
    assert waveforms[0].sample_count == 2
    assert waveforms[0].signal_count == 4
    assert waveforms[0].data.tolist() == [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
    ]
    assert waveforms[1].sample_count == 2
    assert waveforms[1].signal_count == 4
    assert waveforms[1].data.tolist() == [
        [1, 0, 0, 0],
        [1, 1, 0, 0],
    ]


def test___bool_dtype___from_ports_bitorder_little___creates_waveform_with_bool_dtype() -> None:
    array = np.array([[0, 1, 2], [0xFF, 0x12, 0x34]], np.uint8)

    waveforms = DigitalWaveform.from_ports(array, dtype=_np_bool, bitorder="little")

    assert len(waveforms) == 2
    assert waveforms[0].sample_count == 3
    assert waveforms[0].signal_count == 8
    assert waveforms[0].data.tolist() == [
        [False, False, False, False, False, False, False, False],
        [True, False, False, False, False, False, False, False],
        [False, True, False, False, False, False, False, False],
    ]
    assert waveforms[1].sample_count == 3
    assert waveforms[1].signal_count == 8
    assert waveforms[1].data.tolist() == [
        [True, True, True, True, True, True, True, True],
        [False, True, False, False, True, False, False, False],
        [False, False, True, False, True, True, False, False],
    ]


def test___array_subset___from_ports_bitorder_little___creates_waveform_with_array_subset() -> None:
    array = np.array([[0, 1, 2], [0xFF, 0x12, 0x34]], np.uint8)

    waveforms = DigitalWaveform.from_ports(array, start_index=1, sample_count=1, bitorder="little")

    assert len(waveforms) == 2
    assert waveforms[0].start_index == 1
    assert waveforms[0].sample_count == 1
    assert waveforms[0].signal_count == 8
    assert waveforms[0].data.tolist() == [
        [1, 0, 0, 0, 0, 0, 0, 0],
    ]
    assert waveforms[1].start_index == 1
    assert waveforms[1].sample_count == 1
    assert waveforms[1].signal_count == 8
    assert waveforms[1].data.tolist() == [
        [0, 1, 0, 0, 1, 0, 0, 0],
    ]


def test___uint8_ndarray___from_ports___creates_waveform_with_8_lines() -> None:
    array = np.array([[0, 1, 2], [0xFF, 0x12, 0x34]], np.uint8)

    waveforms = DigitalWaveform.from_ports(array)

    assert len(waveforms) == 2
    assert waveforms[0].sample_count == 3
    assert waveforms[0].signal_count == 8
    assert waveforms[0].data.tolist() == [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0],
    ]
    assert waveforms[1].sample_count == 3
    assert waveforms[1].signal_count == 8
    assert waveforms[1].data.tolist() == [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 1, 1, 0, 1, 0, 0],
    ]


def test___uint16_ndarray___from_ports___creates_waveform_with_16_lines() -> None:
    array = np.array([[0, 1, 2], [0xFFFF, 0x1234, 0x5678]], np.uint16)

    waveforms = DigitalWaveform.from_ports(array)

    assert len(waveforms) == 2
    assert waveforms[0].sample_count == 3
    assert waveforms[0].signal_count == 16
    assert waveforms[0].data.tolist() == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    ]
    assert waveforms[1].sample_count == 3
    assert waveforms[1].signal_count == 16
    assert waveforms[1].data.tolist() == [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    ]


def test___int_list_and_mask___from_ports___creates_waveform_with_masked_lines() -> None:
    array = [[0, 1, 2], [0xFFFF, 0x1234, 0x5678]]

    waveforms = DigitalWaveform.from_ports(array, masks=[0xFFFF, 0xFFFF])

    assert len(waveforms) == 2
    assert waveforms[0].sample_count == 3
    assert waveforms[0].signal_count == 16
    assert waveforms[0].data.tolist() == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    ]
    assert waveforms[1].sample_count == 3
    assert waveforms[1].signal_count == 16
    assert waveforms[1].data.tolist() == [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    ]


def test___masks___from_ports___creates_waveform_with_masked_lines() -> None:
    array = np.array([[0x00, 0xFF], [0x12, 0x34]], np.uint8)

    waveforms = DigitalWaveform.from_ports(array, [0x0F, 0xF0])

    assert len(waveforms) == 2
    assert waveforms[0].sample_count == 2
    assert waveforms[0].signal_count == 4
    assert waveforms[0].data.tolist() == [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
    ]
    assert waveforms[1].sample_count == 2
    assert waveforms[1].signal_count == 4
    assert waveforms[1].data.tolist() == [
        [0, 0, 0, 1],
        [0, 0, 1, 1],
    ]


def test___bool_dtype___from_ports___creates_waveform_with_bool_dtype() -> None:
    array = np.array([[0, 1, 2], [0xFF, 0x12, 0x34]], np.uint8)

    waveforms = DigitalWaveform.from_ports(array, dtype=_np_bool)

    assert len(waveforms) == 2
    assert waveforms[0].sample_count == 3
    assert waveforms[0].signal_count == 8
    assert waveforms[0].data.tolist() == [
        [False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, True],
        [False, False, False, False, False, False, True, False],
    ]
    assert waveforms[1].sample_count == 3
    assert waveforms[1].signal_count == 8
    assert waveforms[1].data.tolist() == [
        [True, True, True, True, True, True, True, True],
        [False, False, False, True, False, False, True, False],
        [False, False, True, True, False, True, False, False],
    ]


def test___array_subset___from_ports___creates_waveform_with_array_subset() -> None:
    array = np.array([[0, 1, 2], [0xFF, 0x12, 0x34]], np.uint8)

    waveforms = DigitalWaveform.from_ports(array, start_index=1, sample_count=1)

    assert len(waveforms) == 2
    assert waveforms[0].start_index == 1
    assert waveforms[0].sample_count == 1
    assert waveforms[0].signal_count == 8
    assert waveforms[0].data.tolist() == [
        [0, 0, 0, 0, 0, 0, 0, 1],
    ]
    assert waveforms[1].start_index == 1
    assert waveforms[1].sample_count == 1
    assert waveforms[1].signal_count == 8
    assert waveforms[1].data.tolist() == [
        [0, 0, 0, 1, 0, 0, 1, 0],
    ]


###############################################################################
# data
###############################################################################
def test___uint8_waveform___data___returns_uint8_data() -> None:
    waveform = DigitalWaveform.from_lines([0, 1, 2, 3], np.uint8)

    data = waveform.data

    assert_type(data, npt.NDArray[np.uint8])
    assert isinstance(data, np.ndarray) and data.dtype == np.uint8
    assert list(data) == [0, 1, 2, 3]


###############################################################################
# get_data
###############################################################################
def test___uint8_waveform___get_data___returns_data() -> None:
    waveform = DigitalWaveform.from_lines([0, 1, 2, 3], np.uint8)

    data = waveform.get_data()

    assert_type(data, npt.NDArray[np.uint8])
    assert isinstance(data, np.ndarray) and data.dtype == np.uint8
    assert list(data) == [0, 1, 2, 3]


@pytest.mark.parametrize(
    "start_index, sample_count, expected_data",
    [
        (None, None, [0, 1, 2, 3]),
        (0, None, [0, 1, 2, 3]),
        (1, None, [1, 2, 3]),
        (3, None, [3]),
        (4, None, []),
        (None, None, [0, 1, 2, 3]),
        (None, 1, [0]),
        (None, 3, [0, 1, 2]),
        (None, 4, [0, 1, 2, 3]),
        (1, 2, [1, 2]),
        (4, 0, []),
    ],
)
def test___array_subset___get_data___returns_array_subset(
    start_index: int, sample_count: int, expected_data: list[int]
) -> None:
    waveform = DigitalWaveform.from_lines([0, 1, 2, 3], np.uint8)

    data = waveform.get_data(start_index=start_index, sample_count=sample_count)

    assert_type(data, npt.NDArray[np.uint8])
    assert isinstance(data, np.ndarray) and data.dtype == np.uint8
    assert list(data) == expected_data


@pytest.mark.parametrize(
    "start_index, sample_count, expected_message, exception_type",
    [
        (
            5,
            None,
            "The start index must be less than or equal to the number of samples in the waveform.",
            wfmex.StartIndexTooLargeError,
        ),
        (
            0,
            5,
            "The sum of the start index and sample count must be less than or equal to the number of samples in the waveform.",
            wfmex.StartIndexOrSampleCountTooLargeError,
        ),
        (
            4,
            1,
            "The sum of the start index and sample count must be less than or equal to the number of samples in the waveform.",
            wfmex.StartIndexOrSampleCountTooLargeError,
        ),
    ],
)
def test___invalid_array_subset___get_data___returns_array_subset(
    start_index: int, sample_count: int, expected_message: str, exception_type: type[Exception]
) -> None:
    waveform = DigitalWaveform.from_lines([0, 1, 2, 3], np.uint8)

    with pytest.raises(exception_type) as exc:
        _ = waveform.get_data(start_index=start_index, sample_count=sample_count)

    assert exc.value.args[0].startswith(expected_message)


###############################################################################
# sample_count
###############################################################################
def test___waveform___set_sample_count___updates_sample_count() -> None:
    waveform = DigitalWaveform(10, 2, np.uint8)

    waveform.sample_count = 5

    assert waveform.sample_count == 5
    assert waveform.capacity == 10  # Capacity should remain unchanged
    assert waveform.signal_count == 2  # Signal count should remain unchanged
    assert waveform.data.shape == (5, 2)  # Data shape should reflect new sample count


def test___waveform___set_sample_count_to_zero___creates_empty_waveform() -> None:
    waveform = DigitalWaveform.from_lines([[1, 2], [3, 4]], np.uint8)

    waveform.sample_count = 0

    assert waveform.sample_count == 0
    assert waveform.data.tolist() == []
    assert waveform.capacity == 2  # Capacity preserved


def test___waveform___set_sample_count_exceeds_capacity___raises_value_error() -> None:
    waveform = DigitalWaveform(5, 2, np.uint8, capacity=10)

    with pytest.raises(ValueError) as exc:
        waveform.sample_count = 15

    assert exc.value.args[0].startswith(
        "The sum of the start index and sample count must be less than or equal to the capacity."
    )
    assert waveform.sample_count == 5  # Original sample count preserved


###############################################################################
# capacity
###############################################################################
@pytest.mark.parametrize(
    "capacity, expected_data",
    [
        (3, [[1], [2], [3]]),
        (4, [[1], [2], [3], [0]]),
        (10, [[1], [2], [3], [0], [0], [0], [0], [0], [0], [0]]),
    ],
)
def test___waveform___set_capacity___resizes_array_and_pads_with_zeros(
    capacity: int, expected_data: list[int]
) -> None:
    data = [[1], [2], [3]]
    waveform = DigitalWaveform.from_lines(data, np.uint8)

    waveform.capacity = capacity

    assert waveform.capacity == capacity
    assert waveform.data.tolist() == data
    assert waveform._data.tolist() == expected_data


@pytest.mark.parametrize(
    "capacity, expected_message, exception_type",
    [
        (-2, "The capacity must be a non-negative integer.", ValueError),
        (-1, "The capacity must be a non-negative integer.", ValueError),
        (
            0,
            "The capacity must be equal to or greater than the number of samples in the waveform.",
            wfmex.CapacityTooSmallError,
        ),
        (
            2,
            "The capacity must be equal to or greater than the number of samples in the waveform.",
            wfmex.CapacityTooSmallError,
        ),
    ],
)
def test___invalid_capacity___set_capacity___raises_correct_error(
    capacity: int, expected_message: str, exception_type: type[Exception]
) -> None:
    data = [1, 2, 3]
    waveform = DigitalWaveform.from_lines(data, np.uint8)

    with pytest.raises(exception_type) as exc:
        waveform.capacity = capacity

    assert exc.value.args[0].startswith(expected_message)


def test___referenced_array___set_capacity___reference_sees_size_change() -> None:
    data = np.array([[1, 2], [3, 4], [5, 6]], np.uint8)
    waveform = DigitalWaveform.from_lines(data, np.uint8, copy=False)

    waveform.capacity = 5

    assert len(data) == 5
    assert waveform.capacity == 5
    assert data.tolist() == [[1, 2], [3, 4], [5, 6], [0, 0], [0, 0]]
    assert waveform.data.tolist() == [[1, 2], [3, 4], [5, 6]]
    assert waveform._data.tolist() == [[1, 2], [3, 4], [5, 6], [0, 0], [0, 0]]


def test___array_with_external_buffer___set_capacity___raises_value_error() -> None:
    data = array.array("B", [1, 2, 3])
    waveform = DigitalWaveform.from_lines(data, np.uint8, copy=False)

    with pytest.raises(ValueError) as exc:
        waveform.capacity = 10

    assert exc.value.args[0].startswith("cannot resize this array: it does not own its data")


###############################################################################
# extended properties
###############################################################################
def test___waveform___set_channel_name___sets_extended_property() -> None:
    waveform = DigitalWaveform()

    waveform.channel_name = "Dev1/ai0"

    assert waveform.channel_name == "Dev1/ai0"
    assert waveform.extended_properties["NI_ChannelName"] == "Dev1/ai0"


def test___invalid_type___set_channel_name___raises_type_error() -> None:
    waveform = DigitalWaveform()

    with pytest.raises(TypeError) as exc:
        waveform.channel_name = 1  # type: ignore[assignment]

    assert exc.value.args[0].startswith("The channel name must be a str.")


def test___waveform___set_undefined_property___raises_attribute_error() -> None:
    waveform = DigitalWaveform()

    with pytest.raises(AttributeError):
        waveform.undefined_property = "Whatever"  # type: ignore[attr-defined]


def test___waveform___take_weak_ref___references_waveform() -> None:
    waveform = DigitalWaveform()

    waveform_ref = weakref.ref(waveform)

    assert waveform_ref() is waveform


###############################################################################
# timing
###############################################################################
def test___waveform___has_empty_timing() -> None:
    waveform = DigitalWaveform()

    assert waveform.timing is Timing.empty


def test___bintime___waveform_with_timing___static_type_erased() -> None:
    sample_interval = bt.TimeDelta(1e-3)
    timestamp = bt.DateTime.now(dt.timezone.utc)
    time_offset = bt.TimeDelta(1e-6)
    waveform = DigitalWaveform(
        timing=Timing.create_with_regular_interval(sample_interval, timestamp, time_offset)
    )

    assert_type(waveform.timing.sample_interval, Union[bt.TimeDelta, dt.timedelta, ht.timedelta])
    assert_type(waveform.timing.timestamp, Union[bt.DateTime, dt.datetime, ht.datetime])
    assert_type(waveform.timing.start_time, Union[bt.DateTime, dt.datetime, ht.datetime])
    assert_type(waveform.timing.time_offset, Union[bt.TimeDelta, dt.timedelta, ht.timedelta])
    assert waveform.timing.sample_interval == sample_interval
    assert waveform.timing.timestamp == timestamp
    assert waveform.timing.start_time == timestamp + time_offset
    assert waveform.timing.time_offset == time_offset


def test___datetime___waveform_with_timing___static_type_erased() -> None:
    sample_interval = dt.timedelta(milliseconds=1)
    timestamp = dt.datetime.now(dt.timezone.utc)
    time_offset = dt.timedelta(microseconds=1)
    waveform = DigitalWaveform(
        timing=Timing.create_with_regular_interval(sample_interval, timestamp, time_offset)
    )

    assert_type(waveform.timing.sample_interval, Union[bt.TimeDelta, dt.timedelta, ht.timedelta])
    assert_type(waveform.timing.timestamp, Union[bt.DateTime, dt.datetime, ht.datetime])
    assert_type(waveform.timing.start_time, Union[bt.DateTime, dt.datetime, ht.datetime])
    assert_type(waveform.timing.time_offset, Union[bt.TimeDelta, dt.timedelta, ht.timedelta])
    assert waveform.timing.sample_interval == sample_interval
    assert waveform.timing.timestamp == timestamp
    assert waveform.timing.start_time == timestamp + time_offset
    assert waveform.timing.time_offset == time_offset


def test___hightime___waveform_with_timing___static_type_erased() -> None:
    sample_interval = ht.timedelta(milliseconds=1)
    timestamp = ht.datetime.now(dt.timezone.utc)
    time_offset = ht.timedelta(microseconds=1)
    waveform = DigitalWaveform(
        timing=Timing.create_with_regular_interval(sample_interval, timestamp, time_offset)
    )

    assert_type(waveform.timing.sample_interval, Union[bt.TimeDelta, dt.timedelta, ht.timedelta])
    assert_type(waveform.timing.timestamp, Union[bt.DateTime, dt.datetime, ht.datetime])
    assert_type(waveform.timing.start_time, Union[bt.DateTime, dt.datetime, ht.datetime])
    assert_type(waveform.timing.time_offset, Union[bt.TimeDelta, dt.timedelta, ht.timedelta])
    assert waveform.timing.sample_interval == sample_interval
    assert waveform.timing.timestamp == timestamp
    assert waveform.timing.start_time == timestamp + time_offset
    assert waveform.timing.time_offset == time_offset


@pytest.mark.parametrize(
    "timing",
    [
        Timing.create_with_regular_interval(
            bt.TimeDelta(1e-3), bt.DateTime(2025, 1, 1, tzinfo=dt.timezone.utc), bt.TimeDelta(1e-6)
        ),
        Timing.create_with_regular_interval(
            dt.timedelta(milliseconds=1),
            dt.datetime(2025, 1, 1, tzinfo=dt.timezone.utc),
            dt.timedelta(microseconds=1),
        ),
        Timing.create_with_regular_interval(
            ht.timedelta(milliseconds=1),
            ht.datetime(2025, 1, 1, tzinfo=dt.timezone.utc),
            dt.timedelta(microseconds=1),
        ),
    ],
)
def test___polymorphic_timing___get_timing_properties___behaves_polymorphically(
    timing: Timing[Any, Any, Any],
) -> None:
    waveform = DigitalWaveform(timing=timing)

    assert waveform.timing.sample_interval.total_seconds() == pytest.approx(1e-3)
    assert (
        waveform.timing.timestamp.year,
        waveform.timing.timestamp.month,
        waveform.timing.timestamp.day,
    ) == (2025, 1, 1)
    assert waveform.timing.time_offset.total_seconds() == pytest.approx(1e-6)


###############################################################################
# append array
###############################################################################
def test___empty_ndarray___append___no_effect() -> None:
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    array = np.array([], np.uint8)

    waveform.append(array)

    assert waveform.data.tolist() == [[0], [1], [2]]


def test___uint8_ndarray___append___appends_array() -> None:
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    array = np.array([3, 4, 5], np.uint8)

    waveform.append(array)

    assert waveform.data.tolist() == [[0], [1], [2], [3], [4], [5]]


def test___bool_ndarray___append___appends_array() -> None:
    waveform = DigitalWaveform.from_lines([False, True, False], _np_bool)
    array = np.array([True, False, True], _np_bool)

    waveform.append(array)

    assert waveform.data.tolist() == [[False], [True], [False], [True], [False], [True]]


def test___ndarray_with_mismatched_dtype___append___raises_correct_error() -> None:
    waveform = DigitalWaveform.from_lines([0, 1, 2], _np_bool)
    array = np.array([3, 4, 5], np.uint8)

    with pytest.raises(wfmex.DatatypeMismatchError) as exc:
        waveform.append(array)  # type: ignore[arg-type]

    assert exc.value.args[0].startswith(
        "The data type of the input array must match the waveform data type."
    )


def test___ndarray_2d___append___appends_array() -> None:
    waveform = DigitalWaveform.from_lines([[0, 1, 2], [3, 4, 5]], np.uint8)
    array = np.array([[6, 7, 8], [9, 10, 11]], np.uint8)

    waveform.append(array)

    assert waveform.data.tolist() == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]


def test___irregular_waveform_and_uint8_ndarray_with_timestamps___append___appends_array() -> None:
    start_time = dt.datetime.now(dt.timezone.utc)
    waveform_offsets = [dt.timedelta(0), dt.timedelta(1), dt.timedelta(2)]
    waveform_timestamps = [start_time + offset for offset in waveform_offsets]
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    waveform.timing = Timing.create_with_irregular_interval(waveform_timestamps)
    array_offsets = [dt.timedelta(3), dt.timedelta(4), dt.timedelta(5)]
    array_timestamps = [start_time + offset for offset in array_offsets]
    array = np.array([3, 4, 5], np.uint8)

    waveform.append(array, array_timestamps)

    assert waveform.data.tolist() == [[0], [1], [2], [3], [4], [5]]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert waveform.timing._timestamps == waveform_timestamps + array_timestamps


def test___irregular_waveform_and_uint8_ndarray_without_timestamps___append___raises_timing_mismatch_error_and_does_not_append() -> (
    None
):
    start_time = dt.datetime.now(dt.timezone.utc)
    waveform_offsets = [dt.timedelta(0), dt.timedelta(1), dt.timedelta(2)]
    waveform_timestamps = [start_time + offset for offset in waveform_offsets]
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    waveform.timing = Timing.create_with_irregular_interval(waveform_timestamps)
    array = np.array([3, 4, 5], np.uint8)

    with pytest.raises(wfmex.TimingMismatchError) as exc:
        waveform.append(array)

    assert exc.value.args[0].startswith(
        "The timestamps argument is required when appending to a waveform with irregular timing."
    )
    assert waveform.data.tolist() == [[0], [1], [2]]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert waveform.timing._timestamps == waveform_timestamps


def test___irregular_waveform_and_uint8_ndarray_with_wrong_timestamp_count___append___raises_correct_error_and_does_not_append() -> (
    None
):
    start_time = dt.datetime.now(dt.timezone.utc)
    waveform_offsets = [dt.timedelta(0), dt.timedelta(1), dt.timedelta(2)]
    waveform_timestamps = [start_time + offset for offset in waveform_offsets]
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    waveform.timing = Timing.create_with_irregular_interval(waveform_timestamps)
    array_offsets = [dt.timedelta(3), dt.timedelta(4)]
    array_timestamps = [start_time + offset for offset in array_offsets]
    array = np.array([3, 4, 5], np.uint8)

    with pytest.raises(wfmex.IrregularTimestampCountMismatchError) as exc:
        waveform.append(array, array_timestamps)

    assert exc.value.args[0].startswith(
        "The number of irregular timestamps must be equal to the input array length."
    )
    assert waveform.data.tolist() == [[0], [1], [2]]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert waveform.timing._timestamps == waveform_timestamps


def test___regular_waveform_and_uint8_ndarray_with_timestamps___append___raises_value_error_and_does_not_append() -> (
    None
):
    start_time = dt.datetime.now(dt.timezone.utc)
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    waveform.timing = Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
    array_offsets = [dt.timedelta(3), dt.timedelta(4), dt.timedelta(5)]
    array_timestamps = [start_time + offset for offset in array_offsets]
    array = np.array([3, 4, 5], np.uint8)

    with pytest.raises(ValueError) as exc:
        waveform.append(array, array_timestamps)

    assert exc.value.args[0].startswith("The timestamps argument is not supported.")
    assert waveform.data.tolist() == [[0], [1], [2]]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.timing.sample_interval == dt.timedelta(milliseconds=1)


###############################################################################
# append waveform
###############################################################################
def test___empty_waveform___append___no_effect() -> None:
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    other = DigitalWaveform(dtype=np.uint8)

    waveform.append(other)

    assert waveform.data.tolist() == [[0], [1], [2]]


def test___uint8_waveform___append___appends_waveform() -> None:
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    other = DigitalWaveform.from_lines([[3], [4], [5]], np.uint8)

    waveform.append(other)

    assert waveform.data.tolist() == [[0], [1], [2], [3], [4], [5]]


def test___bool_waveform___append___appends_waveform() -> None:
    waveform = DigitalWaveform.from_lines([[False], [True], [False]], _np_bool)
    other = DigitalWaveform.from_lines([[True], [False], [True]], _np_bool)

    waveform.append(other)

    assert waveform.data.tolist() == [[False], [True], [False], [True], [False], [True]]


def test___waveform_with_mismatched_dtype___append___raises_correct_error() -> None:
    waveform = DigitalWaveform.from_lines([[False], [True], [False]], _np_bool)
    other = DigitalWaveform.from_lines([[3], [4], [5]], np.uint8)

    with pytest.raises(wfmex.DatatypeMismatchError) as exc:
        waveform.append(other)  # type: ignore[arg-type]

    assert exc.value.args[0].startswith(
        "The data type of the input waveform must match the waveform data type."
    )


def test___irregular_waveform_and_irregular_waveform___append___appends_waveform() -> None:
    start_time = dt.datetime.now(dt.timezone.utc)
    waveform_offsets = [dt.timedelta(0), dt.timedelta(1), dt.timedelta(2)]
    waveform_timestamps = [start_time + offset for offset in waveform_offsets]
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    waveform.timing = Timing.create_with_irregular_interval(waveform_timestamps)
    other_offsets = [dt.timedelta(3), dt.timedelta(4), dt.timedelta(5)]
    other_timestamps = [start_time + offset for offset in other_offsets]
    other = DigitalWaveform.from_lines([[3], [4], [5]], np.uint8)
    other.timing = Timing.create_with_irregular_interval(other_timestamps)

    waveform.append(other)

    assert waveform.data.tolist() == [[0], [1], [2], [3], [4], [5]]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert waveform.timing._timestamps == waveform_timestamps + other_timestamps


def test___irregular_waveform_and_regular_waveform___append___raises_correct_error() -> None:
    start_time = dt.datetime.now(dt.timezone.utc)
    waveform_offsets = [dt.timedelta(0), dt.timedelta(1), dt.timedelta(2)]
    waveform_timestamps = [start_time + offset for offset in waveform_offsets]
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    waveform.timing = Timing.create_with_irregular_interval(waveform_timestamps)
    other = DigitalWaveform.from_lines([[3], [4], [5]], np.uint8)

    with pytest.raises(wfmex.SampleIntervalModeMismatchError) as exc:
        waveform.append(other)

    assert exc.value.args[0].startswith(
        "The timing of one or more waveforms does not match the timing of the current waveform."
    )
    assert waveform.data.tolist() == [[0], [1], [2]]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert waveform.timing._timestamps == waveform_timestamps


def test___regular_waveform_and_irregular_waveform___append___raises_correct_error() -> None:
    start_time = dt.datetime.now(dt.timezone.utc)
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    waveform.timing = Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
    other_offsets = [dt.timedelta(3), dt.timedelta(4), dt.timedelta(5)]
    other_timestamps = [start_time + offset for offset in other_offsets]
    other = DigitalWaveform.from_lines([[3], [4], [5]], np.uint8)
    other.timing = Timing.create_with_irregular_interval(other_timestamps)

    with pytest.raises(wfmex.SampleIntervalModeMismatchError) as exc:
        waveform.append(other)

    assert exc.value.args[0].startswith(
        "The timing of one or more waveforms does not match the timing of the current waveform."
    )
    assert waveform.data.tolist() == [[0], [1], [2]]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.timing.sample_interval == dt.timedelta(milliseconds=1)


def test___regular_waveform_and_regular_waveform_with_different_sample_interval___append___appends_waveform_with_timing_mismatch_warning() -> (
    None
):
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    waveform.timing = Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
    other = DigitalWaveform.from_lines([[3], [4], [5]], np.uint8)
    other.timing = Timing.create_with_regular_interval(dt.timedelta(milliseconds=2))

    with pytest.warns(wfmwarn.TimingMismatchWarning):
        waveform.append(other)

    assert waveform.data.tolist() == [[0], [1], [2], [3], [4], [5]]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.timing.sample_interval == dt.timedelta(milliseconds=1)


def test___regular_waveform_and_regular_waveform_with_different_extended_properties___append___merges_extended_properties() -> (
    None
):
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    waveform.extended_properties["A"] = 1
    waveform.extended_properties["B"] = 2
    other = DigitalWaveform.from_lines([[3], [4], [5]], np.uint8)
    other.extended_properties["B"] = 3
    other.extended_properties["C"] = 4

    waveform.append(other)

    assert waveform.data.tolist() == [[0], [1], [2], [3], [4], [5]]
    assert waveform.extended_properties == {"A": 1, "B": 2, "C": 4}


###############################################################################
# append waveforms
###############################################################################
def test___empty_waveform_list___append___no_effect() -> None:
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    other: list[DigitalWaveform[np.uint8]] = []

    waveform.append(other)

    assert waveform.data.tolist() == [[0], [1], [2]]


def test___uint8_waveform_list___append___appends_waveform() -> None:
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    other = [
        DigitalWaveform.from_lines([[3], [4], [5]], np.uint8),
        DigitalWaveform.from_lines([[6]], np.uint8),
        DigitalWaveform.from_lines([[7], [8]], np.uint8),
    ]

    waveform.append(other)

    assert waveform.data.tolist() == [[0], [1], [2], [3], [4], [5], [6], [7], [8]]


def test___bool_waveform_tuple___append___appends_waveform() -> None:
    waveform = DigitalWaveform.from_lines([[False], [True], [False]], _np_bool)
    other = (
        DigitalWaveform.from_lines([[True], [False], [True]], _np_bool),
        DigitalWaveform.from_lines([[True], [True], [False]], _np_bool),
    )

    waveform.append(other)

    assert waveform.data.tolist() == [
        [False],
        [True],
        [False],
        [True],
        [False],
        [True],
        [True],
        [True],
        [False],
    ]


def test___waveform_list_with_mismatched_dtype___append___raises_correct_error_and_does_not_append() -> (
    None
):
    waveform = DigitalWaveform.from_lines([[False], [True], [False]], _np_bool)
    other = [
        DigitalWaveform.from_lines([[True], [False], [True]], _np_bool),
        DigitalWaveform.from_lines([[6], [7], [8]], np.uint8),
    ]

    with pytest.raises(wfmex.DatatypeMismatchError) as exc:
        waveform.append(other)  # type: ignore[arg-type]

    assert exc.value.args[0].startswith(
        "The data type of the input waveform must match the waveform data type."
    )
    assert waveform.data.tolist() == [[False], [True], [False]]


def test___irregular_waveform_and_irregular_waveform_list___append___appends_waveform() -> None:
    start_time = dt.datetime.now(dt.timezone.utc)
    waveform_offsets = [dt.timedelta(0), dt.timedelta(1), dt.timedelta(2)]
    waveform_timestamps = [start_time + offset for offset in waveform_offsets]
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    waveform.timing = Timing.create_with_irregular_interval(waveform_timestamps)
    other1_offsets = [dt.timedelta(3), dt.timedelta(4), dt.timedelta(5)]
    other1_timestamps = [start_time + offset for offset in other1_offsets]
    other1 = DigitalWaveform.from_lines([[3], [4], [5]], np.uint8)
    other1.timing = Timing.create_with_irregular_interval(other1_timestamps)
    other2_offsets = [dt.timedelta(6), dt.timedelta(7), dt.timedelta(8)]
    other2_timestamps = [start_time + offset for offset in other2_offsets]
    other2 = DigitalWaveform.from_lines([[6], [7], [8]], np.uint8)
    other2.timing = Timing.create_with_irregular_interval(other2_timestamps)
    other = [other1, other2]

    waveform.append(other)

    assert waveform.data.tolist() == [[0], [1], [2], [3], [4], [5], [6], [7], [8]]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert (
        waveform.timing._timestamps == waveform_timestamps + other1_timestamps + other2_timestamps
    )


def test___irregular_waveform_and_regular_waveform_list___append___raises_correct_error_and_does_not_append() -> (
    None
):
    start_time = dt.datetime.now(dt.timezone.utc)
    waveform_offsets = [dt.timedelta(0), dt.timedelta(1), dt.timedelta(2)]
    waveform_timestamps = [start_time + offset for offset in waveform_offsets]
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    waveform.timing = Timing.create_with_irregular_interval(waveform_timestamps)
    other1_offsets = [dt.timedelta(3), dt.timedelta(4), dt.timedelta(5)]
    other1_timestamps = [start_time + offset for offset in other1_offsets]
    other1 = DigitalWaveform.from_lines([[3], [4], [5]], np.uint8)
    other1.timing = Timing.create_with_irregular_interval(other1_timestamps)
    other2 = DigitalWaveform.from_lines([[6], [7], [8]], np.uint8)
    other2.timing = Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
    other = [other1, other2]

    with pytest.raises(wfmex.SampleIntervalModeMismatchError) as exc:
        waveform.append(other)

    assert exc.value.args[0].startswith(
        "The timing of one or more waveforms does not match the timing of the current waveform."
    )
    assert waveform.data.tolist() == [[0], [1], [2]]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert waveform.timing._timestamps == waveform_timestamps


def test___regular_waveform_and_irregular_waveform_list___append___raises_correct_error_and_does_not_append() -> (
    None
):
    start_time = dt.datetime.now(dt.timezone.utc)
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    waveform.timing = Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
    other1 = DigitalWaveform.from_lines([[3], [4], [5]], np.uint8)
    other1.timing = Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
    other2_offsets = [dt.timedelta(3), dt.timedelta(4), dt.timedelta(5)]
    other2_timestamps = [start_time + offset for offset in other2_offsets]
    other2 = DigitalWaveform.from_lines([[3], [4], [5]], np.uint8)
    other2.timing = Timing.create_with_irregular_interval(other2_timestamps)
    other = [other1, other2]

    with pytest.raises(wfmex.SampleIntervalModeMismatchError) as exc:
        waveform.append(other)

    assert exc.value.args[0].startswith(
        "The timing of one or more waveforms does not match the timing of the current waveform."
    )
    assert waveform.data.tolist() == [[0], [1], [2]]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.timing.sample_interval == dt.timedelta(milliseconds=1)


###############################################################################
# load data
###############################################################################
def test___empty_ndarray___load_data___clears_data() -> None:
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    array = np.array([], np.uint8)

    waveform.load_data(array)

    assert waveform.data.tolist() == []


def test___uint8_ndarray___load_data___overwrites_data() -> None:
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    array = np.array([[3], [4], [5]], np.uint8)

    waveform.load_data(array)

    assert waveform.data.tolist() == [[3], [4], [5]]


def test___bool_ndarray___load_data___overwrites_data() -> None:
    waveform = DigitalWaveform.from_lines([[False], [True], [False]], _np_bool)
    array = np.array([[True], [False], [True]], _np_bool)

    waveform.load_data(array)

    assert waveform.data.tolist() == [[True], [False], [True]]


def test___ndarray_with_mismatched_dtype___load_data___raises_correct_error() -> None:
    waveform = DigitalWaveform.from_lines([[False], [True], [False]], _np_bool)
    array = np.array([[3], [4], [5]], np.uint8)

    with pytest.raises(wfmex.DatatypeMismatchError) as exc:
        waveform.load_data(array)  # type: ignore[arg-type]

    assert exc.value.args[0].startswith(
        "The data type of the input array must match the waveform data type."
    )


def test___ndarray_2d___load_data___overwrites_data() -> None:
    waveform = DigitalWaveform.from_lines([[False, True], [False, False]], _np_bool)
    array = np.array([[True, True], [False, False], [True, False]], _np_bool)

    waveform.load_data(array)

    assert waveform.data.tolist() == [[True, True], [False, False], [True, False]]


def test___smaller_ndarray___load_data___preserves_capacity() -> None:
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    array = np.array([[3]], np.uint8)

    waveform.load_data(array)

    assert waveform.data.tolist() == [[3]]
    assert waveform.capacity == 3


def test___larger_ndarray___load_data___grows_capacity() -> None:
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    array = np.array([[3], [4], [5], [6]], np.uint8)

    waveform.load_data(array)

    assert waveform.data.tolist() == [[3], [4], [5], [6]]
    assert waveform.capacity == 4


def test___waveform_with_start_index___load_data___clears_start_index() -> None:
    waveform = DigitalWaveform.from_lines(
        np.array([[0], [1], [2]], np.uint8), np.uint8, copy=False, start_index=1, sample_count=1
    )
    assert waveform.start_index == 1
    array = np.array([[3]], np.uint8)

    waveform.load_data(array)

    assert waveform.data.tolist() == [[3]]
    assert waveform.start_index == 0


def test___ndarray_subset___load_data___overwrites_data() -> None:
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    array = np.array([[3], [4], [5]], np.uint8)

    waveform.load_data(array, start_index=1, sample_count=1)

    assert waveform.data.tolist() == [[4]]
    assert waveform.start_index == 0
    assert waveform.capacity == 3


def test___smaller_ndarray_no_copy___load_data___takes_ownership_of_array() -> None:
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    array = np.array([[3]], np.uint8)

    waveform.load_data(array, copy=False)

    assert waveform.data.tolist() == [[3]]
    assert waveform._data is array


def test___larger_ndarray_no_copy___load_data___takes_ownership_of_array() -> None:
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    array = np.array([[3], [4], [5], [6]], np.uint8)

    waveform.load_data(array, copy=False)

    assert waveform.data.tolist() == [[3], [4], [5], [6]]
    assert waveform._data is array


def test___ndarray_subset_no_copy___load_data___takes_ownership_of_array_subset() -> None:
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    array = np.array([[3], [4], [5], [6]], np.uint8)

    waveform.load_data(array, copy=False, start_index=1, sample_count=2)

    assert waveform.data.tolist() == [[4], [5]]
    assert waveform._data is array


def test___irregular_waveform_and_uint8_ndarray_with_timestamps___load_data___overwrites_data_but_not_timestamps() -> (
    None
):
    start_time = dt.datetime.now(dt.timezone.utc)
    waveform_offsets = [dt.timedelta(0), dt.timedelta(1), dt.timedelta(2)]
    waveform_timestamps = [start_time + offset for offset in waveform_offsets]
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    waveform.timing = Timing.create_with_irregular_interval(waveform_timestamps)
    array = np.array([3, 4, 5], np.uint8)

    waveform.load_data(array)

    assert waveform.data.tolist() == [[3], [4], [5]]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert waveform.timing._timestamps == waveform_timestamps


def test___irregular_waveform_and_uint8_ndarray_with_wrong_sample_count___load_data___raises_correct_error_and_does_not_overwrite_data() -> (
    None
):
    start_time = dt.datetime.now(dt.timezone.utc)
    waveform_offsets = [dt.timedelta(0), dt.timedelta(1), dt.timedelta(2)]
    waveform_timestamps = [start_time + offset for offset in waveform_offsets]
    waveform = DigitalWaveform.from_lines([[0], [1], [2]], np.uint8)
    waveform.timing = Timing.create_with_irregular_interval(waveform_timestamps)
    array = np.array([3, 4], np.uint8)

    with pytest.raises(wfmex.IrregularTimestampCountMismatchError) as exc:
        waveform.load_data(array)

    assert exc.value.args[0].startswith(
        "The input array length must be equal to the number of irregular timestamps."
    )
    assert waveform.data.tolist() == [[0], [1], [2]]
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.IRREGULAR
    assert waveform.timing._timestamps == waveform_timestamps


###############################################################################
# magic methods
###############################################################################
@pytest.mark.parametrize(
    "left, right",
    [
        (DigitalWaveform(), DigitalWaveform()),
        (DigitalWaveform(10), DigitalWaveform(10)),
        (DigitalWaveform(10, 1), DigitalWaveform(10, 1)),
        (DigitalWaveform(10, 1, _np_bool), DigitalWaveform(10, 1, _np_bool)),
        (DigitalWaveform(10, 1, np.uint8), DigitalWaveform(10, 1, np.uint8)),
        (
            DigitalWaveform(10, 1, np.uint8, start_index=5, capacity=20),
            DigitalWaveform(10, 1, np.uint8, start_index=5, capacity=20),
        ),
        (
            DigitalWaveform.from_lines([0, 1, 2, 3], _np_bool),
            DigitalWaveform.from_lines([0, 1, 2, 3], _np_bool),
        ),
        # _np_bool coerces non-zero values to True, so in this case, 4 == 2.
        (
            DigitalWaveform.from_lines([0, 1, 4, 3], _np_bool),
            DigitalWaveform.from_lines([0, 1, 2, 3], _np_bool),
        ),
        (
            DigitalWaveform.from_lines([0, 1, 2, 3], np.uint8),
            DigitalWaveform.from_lines([0, 1, 2, 3], np.uint8),
        ),
        (
            DigitalWaveform(
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
            ),
            DigitalWaveform(
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
            ),
        ),
        (
            DigitalWaveform(
                timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=1))
            ),
            DigitalWaveform(
                timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=1))
            ),
        ),
        (
            DigitalWaveform(
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"}
            ),
            DigitalWaveform(
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"}
            ),
        ),
        # start_index and capacity may differ as long as data and sample_count are the same.
        (
            DigitalWaveform(10, 1, np.uint8, start_index=5, capacity=20),
            DigitalWaveform(10, 1, np.uint8, start_index=10, capacity=25),
        ),
        (
            DigitalWaveform.from_lines(
                [0, 0, 1, 2, 3, 4, 5, 0], np.uint8, start_index=2, sample_count=5
            ),
            DigitalWaveform.from_lines(
                [0, 1, 2, 3, 4, 5, 0, 0, 0], np.uint8, start_index=1, sample_count=5
            ),
        ),
        # Same value, different time type
        (
            DigitalWaveform(
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
            ),
            DigitalWaveform(
                timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=1))
            ),
        ),
        (
            DigitalWaveform(
                timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=1))
            ),
            DigitalWaveform(
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
            ),
        ),
    ],
)
def test___same_value___equality___equal(
    left: DigitalWaveform[Any], right: DigitalWaveform[Any]
) -> None:
    assert left == right
    assert not (left != right)


@pytest.mark.parametrize(
    "left, right",
    [
        (DigitalWaveform(), DigitalWaveform(10)),
        (DigitalWaveform(10), DigitalWaveform(11)),
        (DigitalWaveform(10, 1), DigitalWaveform(10, 2)),
        (DigitalWaveform(10, 1, _np_bool), DigitalWaveform(10, 1, np.uint8)),
        (
            DigitalWaveform(15, 1, np.uint8, start_index=5, capacity=20),
            DigitalWaveform(10, 1, np.uint8, start_index=5, capacity=20),
        ),
        (
            DigitalWaveform.from_lines([0, 1, 0, 3], _np_bool),
            DigitalWaveform.from_lines([0, 1, 2, 3], _np_bool),
        ),
        (
            DigitalWaveform.from_lines([0, 1, 4, 3], np.uint8),
            DigitalWaveform.from_lines([0, 1, 2, 3], np.uint8),
        ),
        (
            DigitalWaveform.from_lines([0, 1, 2, 3], np.uint8),
            DigitalWaveform.from_lines([0, 1, 2, 3], _np_bool),
        ),
        (
            DigitalWaveform(
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
            ),
            DigitalWaveform(
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=2))
            ),
        ),
        (
            DigitalWaveform(
                timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=1))
            ),
            DigitalWaveform(
                timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=2))
            ),
        ),
        (
            DigitalWaveform(
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"}
            ),
            DigitalWaveform(
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Amps"}
            ),
        ),
    ],
)
def test___different_value___equality___not_equal(
    left: DigitalWaveform[Any], right: DigitalWaveform[Any]
) -> None:
    assert not (left == right)
    assert left != right


@pytest.mark.parametrize(
    "value, expected_repr",
    [
        (DigitalWaveform(), "nitypes.waveform.DigitalWaveform(0, 1)"),
        (
            DigitalWaveform(3, 2),
            "nitypes.waveform.DigitalWaveform(3, 2, data=array([[0, 0], [0, 0], [0, 0]], dtype=uint8))",
        ),
        (
            DigitalWaveform(3, 2, _np_bool),
            "nitypes.waveform.DigitalWaveform(3, 2, bool, data=array([[False, False], [False, False], [False, False]]))",
        ),
        (DigitalWaveform(0, 1, np.uint8), "nitypes.waveform.DigitalWaveform(0, 1)"),
        (
            DigitalWaveform(5, 1, np.uint8),
            f"nitypes.waveform.DigitalWaveform(5, 1, data=array([[0], [0], [0], [0], [0]], dtype=uint8))",
        ),
        (
            DigitalWaveform(5, 1, np.uint8, start_index=5, capacity=20),
            f"nitypes.waveform.DigitalWaveform(5, 1, data=array([[0], [0], [0], [0], [0]], dtype=uint8))",
        ),
        (
            DigitalWaveform.from_lines([0, 1, 2, 3], _np_bool),
            "nitypes.waveform.DigitalWaveform(4, 1, bool, data=array([[False], [ True], [ True], [ True]]))",
        ),
        (
            DigitalWaveform.from_lines([0, 1, 2, 3], np.uint8),
            f"nitypes.waveform.DigitalWaveform(4, 1, data=array([[0], [1], [2], [3]], dtype=uint8))",
        ),
        (
            DigitalWaveform(
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))
            ),
            "nitypes.waveform.DigitalWaveform(0, 1, "
            "timing=nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR, "
            "sample_interval=datetime.timedelta(microseconds=1000)))",
        ),
        (
            DigitalWaveform(
                timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=1))
            ),
            "nitypes.waveform.DigitalWaveform(0, 1, "
            "timing=nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR, "
            "sample_interval=hightime.timedelta(microseconds=1000)))",
        ),
        (
            DigitalWaveform(
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"}
            ),
            "nitypes.waveform.DigitalWaveform(0, 1, extended_properties={'NI_ChannelName': 'Dev1/ai0', "
            "'NI_UnitDescription': 'Volts'})",
        ),
        (
            DigitalWaveform.from_lines(
                [1, 2, 3],
                np.uint8,
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1)),
            ),
            f"nitypes.waveform.DigitalWaveform(3, 1, data=array([[1], [2], [3]], dtype=uint8), "
            "timing=nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR, "
            "sample_interval=datetime.timedelta(microseconds=1000)))",
        ),
        (
            DigitalWaveform.from_lines(
                [1, 2, 3],
                np.uint8,
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"},
            ),
            f"nitypes.waveform.DigitalWaveform(3, 1, data=array([[1], [2], [3]], dtype=uint8), "
            "extended_properties={'NI_ChannelName': 'Dev1/ai0', 'NI_UnitDescription': 'Volts'})",
        ),
        (
            DigitalWaveform.from_port(
                [1, 2, 3],
                0xFF,
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1)),
            ),
            f"nitypes.waveform.DigitalWaveform(3, 8, data=array([[0, 0, 0, 0, 0, 0, 0, 1], "
            "[0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 1]], dtype=uint8), "
            "timing=nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR, "
            "sample_interval=datetime.timedelta(microseconds=1000)))",
        ),
        (
            DigitalWaveform.from_port(
                [1, 2, 3],
                0xFF,
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"},
            ),
            f"nitypes.waveform.DigitalWaveform(3, 8, data=array([[0, 0, 0, 0, 0, 0, 0, 1], "
            "[0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 1]], dtype=uint8), "
            "extended_properties={'NI_ChannelName': 'Dev1/ai0', 'NI_UnitDescription': 'Volts'})",
        ),
        (
            DigitalWaveform.from_ports(
                [[1, 2, 3], [4, 5, 6]],
                [0xFF, 0xFF],
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1)),
            ),
            f"[nitypes.waveform.DigitalWaveform(3, 8, data=array([[0, 0, 0, 0, 0, 0, 0, 1], "
            "[0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 1]], dtype=uint8), "
            "timing=nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR, "
            "sample_interval=datetime.timedelta(microseconds=1000))), "
            "nitypes.waveform.DigitalWaveform(3, 8, data=array([[0, 0, 0, 0, 0, 1, 0, 0], "
            "[0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 1, 1, 0]], dtype=uint8), "
            "timing=nitypes.waveform.Timing(nitypes.waveform.SampleIntervalMode.REGULAR, "
            "sample_interval=datetime.timedelta(microseconds=1000)))]",
        ),
        (
            DigitalWaveform.from_ports(
                [[1, 2, 3], [4, 5, 6]],
                [0xFF, 0xFF],
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"},
            ),
            f"[nitypes.waveform.DigitalWaveform(3, 8, data=array([[0, 0, 0, 0, 0, 0, 0, 1], "
            "[0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 1]], dtype=uint8), "
            "extended_properties={'NI_ChannelName': 'Dev1/ai0', 'NI_UnitDescription': 'Volts'}), "
            "nitypes.waveform.DigitalWaveform(3, 8, data=array([[0, 0, 0, 0, 0, 1, 0, 0], "
            "[0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 1, 1, 0]], dtype=uint8), "
            "extended_properties={'NI_ChannelName': 'Dev1/ai0', 'NI_UnitDescription': 'Volts'})]",
        ),
    ],
)
def test___various_values___repr___looks_ok(
    value: DigitalWaveform[Any] | Sequence[DigitalWaveform[Any]], expected_repr: str
) -> None:
    assert repr(value) == expected_repr


_VARIOUS_VALUES = [
    DigitalWaveform(),
    DigitalWaveform(10, 2),
    DigitalWaveform(10, 2, _np_bool),
    DigitalWaveform(10, 2, np.uint8),
    DigitalWaveform(10, 2, np.uint8, start_index=5, capacity=20),
    DigitalWaveform.from_lines([0, 1, 2, 3], _np_bool),
    DigitalWaveform.from_lines([0, 1, 2, 3], np.uint8),
    DigitalWaveform(timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1))),
    DigitalWaveform(timing=Timing.create_with_regular_interval(ht.timedelta(milliseconds=1))),
    DigitalWaveform(
        extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"}
    ),
    DigitalWaveform(10, 2, np.uint8, start_index=5, capacity=20),
    DigitalWaveform.from_lines([0, 0, 1, 2, 3, 4, 5, 0], np.uint8, start_index=2, sample_count=5),
]


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___copy___makes_shallow_copy(value: DigitalWaveform[Any]) -> None:
    new_value = copy.copy(value)

    _assert_shallow_copy(new_value, value)


def _assert_on_key_changed_valid(value: DigitalWaveform[Any]) -> None:
    assert any(
        ref() == value._on_extended_property_changed
        for ref in value.extended_properties._on_key_changed
    )


def _assert_shallow_copy(value: DigitalWaveform[Any], other: DigitalWaveform[Any]) -> None:
    assert value == other
    assert value is not other
    # _data may be a view of the original array. If the original array is 1D, then look at _data_1d.
    assert (
        value._data is other._data
        or value._data.base is other._data
        or value._data.base is other._data_1d
    )
    assert value._extended_properties is other._extended_properties
    _assert_on_key_changed_valid(value)
    _assert_on_key_changed_valid(other)
    assert value._timing is other._timing


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___deepcopy___makes_deep_copy(value: DigitalWaveform[Any]) -> None:
    new_value = copy.deepcopy(value)

    _assert_deep_copy(new_value, value)


def _assert_deep_copy(value: DigitalWaveform[Any], other: DigitalWaveform[Any]) -> None:
    assert value == other
    assert value is not other
    assert value._data is not other._data and value._data.base is not other._data
    assert value._extended_properties is not other._extended_properties
    _assert_on_key_changed_valid(value)
    _assert_on_key_changed_valid(other)
    if other._timing is not Timing.empty:
        assert value._timing is not other._timing


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___pickle_unpickle___makes_deep_copy(value: DigitalWaveform[Any]) -> None:
    new_value = pickle.loads(pickle.dumps(value))

    _assert_deep_copy(new_value, value)


def test___waveform___pickle___references_public_modules() -> None:
    value = DigitalWaveform(
        data=np.array([1, 2, 3], _np_bool),
        extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"},
        timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1)),
    )

    value_bytes = pickle.dumps(value)

    assert b"nitypes.waveform" in value_bytes
    assert b"nitypes.waveform._digital" not in value_bytes
    assert b"nitypes.waveform._extended_properties" not in value_bytes
    assert b"nitypes.waveform._timing" not in value_bytes


@pytest.mark.parametrize(
    "pickled_value, expected",
    [
        # nitypes 1.0.0
        pytest.param(
            b"\x80\x04\x95\x08\x02\x00\x00\x00\x00\x00\x00\x8c\x08builtins\x94\x8c\x07getattr\x94\x93\x94\x8c\x10nitypes.waveform\x94\x8c\x0fDigitalWaveform\x94\x93\x94\x8c\t_unpickle\x94\x86\x94R\x94K\x03K\x01\x8c\x05numpy\x94\x8c\x05dtype\x94\x93\x94\x8c\x02b1\x94\x89\x88\x87\x94R\x94(K\x03\x8c\x01|\x94NNNJ\xff\xff\xff\xffJ\xff\xff\xff\xffK\x00t\x94b\x87\x94}\x94(\x8c\x04data\x94\x8c\x16numpy._core.multiarray\x94\x8c\x0c_reconstruct\x94\x93\x94h\t\x8c\x07ndarray\x94\x93\x94K\x00\x85\x94C\x01b\x94\x87\x94R\x94(K\x01K\x03K\x01\x86\x94h\x0e\x89C\x03\x01\x01\x01\x94t\x94b\x8c\x13extended_properties\x94h\x03\x8c\x1aExtendedPropertyDictionary\x94\x93\x94)\x81\x94N}\x94\x8c\x0b_properties\x94}\x94(\x8c\x0eNI_ChannelName\x94\x8c\x08Dev1/ai0\x94\x8c\x12NI_UnitDescription\x94\x8c\x05Volts\x94us\x86\x94b\x8c\x18copy_extended_properties\x94\x89\x8c\x06timing\x94h\x02h\x03\x8c\x06Timing\x94\x93\x94h\x06\x86\x94R\x94(h\x03\x8c\x12SampleIntervalMode\x94\x93\x94K\x01\x85\x94R\x94NN\x8c\x08datetime\x94\x8c\ttimedelta\x94\x93\x94K\x00K\x00M\xe8\x03\x87\x94R\x94Nt\x94}\x94\x86\x94R\x94u\x86\x94R\x94.",
            DigitalWaveform(
                data=np.array([1, 2, 3], _np_bool),
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"},
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1)),
            ),
        ),
        # nitypes 1.0.1
        (
            b"\x80\x04\x95\xf4\x01\x00\x00\x00\x00\x00\x00\x8c\x08builtins\x94\x8c\x07getattr\x94\x93\x94\x8c\x10nitypes.waveform\x94\x8c\x0fDigitalWaveform\x94\x93\x94\x8c\t_unpickle\x94\x86\x94R\x94K\x03K\x01\x8c\x05numpy\x94\x8c\x05dtype\x94\x93\x94\x8c\x02b1\x94\x89\x88\x87\x94R\x94(K\x03\x8c\x01|\x94NNNJ\xff\xff\xff\xffJ\xff\xff\xff\xffK\x00t\x94b\x87\x94}\x94(\x8c\x04data\x94\x8c\x16numpy._core.multiarray\x94\x8c\x0c_reconstruct\x94\x93\x94h\t\x8c\x07ndarray\x94\x93\x94K\x00\x85\x94C\x01b\x94\x87\x94R\x94(K\x01K\x03K\x01\x86\x94h\x0e\x89C\x03\x01\x01\x01\x94t\x94b\x8c\x13extended_properties\x94h\x03\x8c\x1aExtendedPropertyDictionary\x94\x93\x94}\x94(\x8c\x0eNI_ChannelName\x94\x8c\x08Dev1/ai0\x94\x8c\x12NI_UnitDescription\x94\x8c\x05Volts\x94u\x85\x94R\x94\x8c\x18copy_extended_properties\x94\x89\x8c\x06timing\x94h\x02h\x03\x8c\x06Timing\x94\x93\x94h\x06\x86\x94R\x94(h\x03\x8c\x12SampleIntervalMode\x94\x93\x94K\x01\x85\x94R\x94NN\x8c\x08datetime\x94\x8c\ttimedelta\x94\x93\x94K\x00K\x00M\xe8\x03\x87\x94R\x94Nt\x94}\x94\x86\x94R\x94u\x86\x94R\x94.",
            DigitalWaveform(
                data=np.array([1, 2, 3], _np_bool),
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"},
                timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1)),
            ),
        ),
    ],
)
def test___pickled_value___unpickle___is_compatible(
    pickled_value: bytes, expected: DigitalWaveform[Any]
) -> None:
    new_value = pickle.loads(pickled_value)
    assert new_value == expected


def test___waveform_with_extended_properties___pickle_unpickle___valid_on_key_changed() -> None:
    value = DigitalWaveform(
        data=np.array([1, 2, 3], _np_bool),
        extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"},
        timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1)),
    )

    new_value = pickle.loads(pickle.dumps(value))

    _assert_on_key_changed_valid(value)
    _assert_on_key_changed_valid(new_value)


def test___waveform_with_extended_properties___shallow_copy___valid_on_key_changed() -> None:
    value = DigitalWaveform(
        data=np.array([1, 2, 3], _np_bool),
        extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"},
        timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1)),
    )

    new_value = copy.copy(value)

    _assert_on_key_changed_valid(value)
    _assert_on_key_changed_valid(new_value)


def test___waveform_with_extended_properties___deep_copy___valid_on_key_changed() -> None:
    value = DigitalWaveform(
        data=np.array([1, 2, 3], _np_bool),
        extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"},
        timing=Timing.create_with_regular_interval(dt.timedelta(milliseconds=1)),
    )

    new_value = copy.deepcopy(value)

    _assert_on_key_changed_valid(value)
    _assert_on_key_changed_valid(new_value)


###############################################################################
# test
###############################################################################
def test___same_data___test___returns_success() -> None:
    waveform = DigitalWaveform.from_port([1, 2, 3, 0xFF, 0x12, 0x34], 0xFF)
    expected_waveform = DigitalWaveform.from_port([1, 2, 3, 0xFF, 0x12, 0x34], 0xFF)

    result = waveform.test(expected_waveform)

    assert result.success
    assert len(result.failures) == 0


def test___different_data___test___reports_failures() -> None:
    waveform = DigitalWaveform.from_port([1, 3, 3, 0xFF, 0x82, 0x34], 0xFF)
    expected_waveform = DigitalWaveform.from_port([1, 2, 3, 0xFF, 0x12, 0x34], 0xFF)

    result = waveform.test(expected_waveform)

    assert not result.success
    assert result.failures == [
        DigitalWaveformFailure(
            sample_index=1,
            expected_sample_index=1,
            signal_index=0,
            actual_state=DigitalState.FORCE_UP,
            expected_state=DigitalState.FORCE_DOWN,
        ),
        DigitalWaveformFailure(
            sample_index=4,
            expected_sample_index=4,
            signal_index=7,
            actual_state=DigitalState.FORCE_UP,
            expected_state=DigitalState.FORCE_DOWN,
        ),
        DigitalWaveformFailure(
            sample_index=4,
            expected_sample_index=4,
            signal_index=4,
            actual_state=DigitalState.FORCE_DOWN,
            expected_state=DigitalState.FORCE_UP,
        ),
    ]


def test___shifted_different_data___test___reports_shifted_failures() -> None:
    waveform = DigitalWaveform.from_port([0, 0, 1, 3, 3, 0xFF, 0x82, 0x34], 0xFF)
    expected_waveform = DigitalWaveform.from_port([0, 1, 2, 3, 0xFF, 0x12, 0x34, 0, 0, 0], 0xFF)

    result = waveform.test(
        expected_waveform, start_sample=2, expected_start_sample=1, sample_count=6
    )

    assert not result.success
    assert result.failures == [
        DigitalWaveformFailure(
            sample_index=3,
            expected_sample_index=2,
            signal_index=0,
            actual_state=DigitalState.FORCE_UP,
            expected_state=DigitalState.FORCE_DOWN,
        ),
        DigitalWaveformFailure(
            sample_index=6,
            expected_sample_index=5,
            signal_index=7,
            actual_state=DigitalState.FORCE_UP,
            expected_state=DigitalState.FORCE_DOWN,
        ),
        DigitalWaveformFailure(
            sample_index=6,
            expected_sample_index=5,
            signal_index=4,
            actual_state=DigitalState.FORCE_DOWN,
            expected_state=DigitalState.FORCE_UP,
        ),
    ]
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/waveform/test_digital_waveform_signal.py sha256=4044341018a07c363a07c388b582888b0146384f9e8a39c0c5c6fea34f652f0d bytes=17069 -->
## FILE: tests/unit/waveform/test_digital_waveform_signal.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/waveform/test_digital_waveform_signal.py`
- sha256: `4044341018a07c363a07c388b582888b0146384f9e8a39c0c5c6fea34f652f0d`
- bytes: 17069

````python
from __future__ import annotations

import copy
import pickle
from collections.abc import Sequence
from typing import Any

import numpy as np
import numpy.typing as npt
import pytest
from typing_extensions import assert_type

from nitypes._numpy import bool as _np_bool
from nitypes.waveform import (
    DigitalWaveform,
    DigitalWaveformSignal,
    DigitalWaveformSignalCollection,
)


###############################################################################
# signal collection
###############################################################################
def test___waveform___signals___is_signal_collection() -> None:
    waveform = DigitalWaveform(10, 3)

    assert_type(waveform.signals, DigitalWaveformSignalCollection[np.uint8])
    assert isinstance(waveform.signals, DigitalWaveformSignalCollection)


def test___waveform___signals_len___returns_signal_count() -> None:
    waveform = DigitalWaveform(10, 3)

    assert len(waveform.signals) == 3


def test___int_index___signals_getitem___returns_signal() -> None:
    waveform = DigitalWaveform(10, 3)

    assert_type(waveform.signals[0], DigitalWaveformSignal[np.uint8])
    assert waveform.signals[0].signal_index == 0
    assert waveform.signals[1].signal_index == 1
    assert waveform.signals[2].signal_index == 2
    assert waveform.signals[0].column_index == 2
    assert waveform.signals[1].column_index == 1
    assert waveform.signals[2].column_index == 0


def test___negative_int_index___signals_getitem___returns_signal() -> None:
    waveform = DigitalWaveform(10, 3)

    assert waveform.signals[-1].signal_index == 2
    assert waveform.signals[-2].signal_index == 1
    assert waveform.signals[-3].signal_index == 0
    assert waveform.signals[-1].column_index == 0
    assert waveform.signals[-2].column_index == 1
    assert waveform.signals[-3].column_index == 2


def test___str_index___signals_getitem___returns_signal() -> None:
    waveform = DigitalWaveform(
        10, 3, extended_properties={"NI_LineNames": "port0/line2, port0/line1, port0/line0"}
    )

    assert_type(waveform.signals["port0/line0"], DigitalWaveformSignal[np.uint8])
    assert waveform.signals["port0/line0"].signal_index == 0
    assert waveform.signals["port0/line1"].signal_index == 1
    assert waveform.signals["port0/line2"].signal_index == 2
    assert waveform.signals["port0/line0"].column_index == 2
    assert waveform.signals["port0/line1"].column_index == 1
    assert waveform.signals["port0/line2"].column_index == 0


def test___invalid_str_index___signals_getitem___raises_index_error() -> None:
    waveform = DigitalWaveform(
        10, 3, extended_properties={"NI_LineNames": "port0/line2, port0/line1, port0/line0"}
    )

    with pytest.raises(IndexError) as exc:
        _ = waveform.signals["port0/line3"]

    assert exc.value.args[0] == "port0/line3"


def test___slice_index___signals_getitem___returns_signal() -> None:
    waveform = DigitalWaveform(10, 5)

    assert_type(waveform.signals[1:3], Sequence[DigitalWaveformSignal[np.uint8]])
    assert [signal.signal_index for signal in waveform.signals[1:3]] == [1, 2]
    assert [signal.signal_index for signal in waveform.signals[2:]] == [2, 3, 4]
    assert [signal.signal_index for signal in waveform.signals[:3]] == [0, 1, 2]
    assert [signal.column_index for signal in waveform.signals[1:3]] == [3, 2]
    assert [signal.column_index for signal in waveform.signals[2:]] == [2, 1, 0]
    assert [signal.column_index for signal in waveform.signals[:3]] == [4, 3, 2]


def test___negative_slice_index___signals_getitem___returns_signal() -> None:
    waveform = DigitalWaveform(10, 5)

    assert [signal.signal_index for signal in waveform.signals[-2:]] == [3, 4]
    assert [signal.signal_index for signal in waveform.signals[:-2]] == [0, 1, 2]
    assert [signal.signal_index for signal in waveform.signals[-3:-1]] == [2, 3]
    assert [signal.column_index for signal in waveform.signals[-2:]] == [1, 0]
    assert [signal.column_index for signal in waveform.signals[:-2]] == [4, 3, 2]
    assert [signal.column_index for signal in waveform.signals[-3:-1]] == [2, 1]


###############################################################################
# signal name
###############################################################################
def test___signal___set_signal_name___sets_name() -> None:
    waveform = DigitalWaveform(10, 3)

    waveform.signals[0].name = "port0/line0"
    waveform.signals[1].name = "port0/line1"
    waveform.signals[2].name = "port0/line2"

    assert waveform.extended_properties["NI_LineNames"] == "port0/line2, port0/line1, port0/line0"


def test___signal_with_line_names___get_signal_name___returns_line_name() -> None:
    waveform = DigitalWaveform(
        10, 3, extended_properties={"NI_LineNames": "port0/line2, port0/line1, port0/line0"}
    )

    assert waveform.signals[0].name == "port0/line0"
    assert waveform.signals[1].name == "port0/line1"
    assert waveform.signals[2].name == "port0/line2"


def test___signal_with_line_names___set_signal_name___returns_line_name() -> None:
    waveform = DigitalWaveform(
        10, 3, extended_properties={"NI_LineNames": "port0/line2, port0/line1, port0/line0"}
    )

    waveform.signals[1].name = "MySignal"

    assert waveform.extended_properties["NI_LineNames"] == "port0/line2, MySignal, port0/line0"


def test___signal_with_line_names___change_line_names_property___signal_returns_new_line_name() -> (
    None
):
    waveform = DigitalWaveform(
        10, 2, extended_properties={"NI_LineNames": "port0/line1, port0/line0"}
    )
    assert waveform.signals[0].name == "port0/line0"
    assert waveform.signals[1].name == "port0/line1"

    waveform.extended_properties["NI_LineNames"] = "port0/line11, port0/line10"

    assert waveform.signals[0].name == "port0/line10"
    assert waveform.signals[1].name == "port0/line11"


def test___pickled_waveform___change_line_names_property___signal_returns_new_line_name() -> None:
    waveform = DigitalWaveform(
        10, 2, extended_properties={"NI_LineNames": "port0/line1, port0/line0"}
    )
    pickled_waveform = pickle.loads(pickle.dumps(waveform))
    assert waveform.signals[0].name == "port0/line0"
    assert waveform.signals[1].name == "port0/line1"
    assert pickled_waveform.signals[0].name == "port0/line0"
    assert pickled_waveform.signals[1].name == "port0/line1"

    waveform.extended_properties["NI_LineNames"] = "port0/line11, port0/line10"
    pickled_waveform.extended_properties["NI_LineNames"] = "port0/line21, port0/line20"

    assert waveform.signals[0].name == "port0/line10"
    assert waveform.signals[1].name == "port0/line11"
    assert pickled_waveform.signals[0].name == "port0/line20"
    assert pickled_waveform.signals[1].name == "port0/line21"


def test___shallow_copied_waveform___change_line_names_property___signal_returns_new_line_name() -> (
    None
):
    waveform = DigitalWaveform(
        10, 2, extended_properties={"NI_LineNames": "port0/line1, port0/line0"}
    )
    copied_waveform = copy.copy(waveform)
    assert waveform.signals[0].name == "port0/line0"
    assert waveform.signals[1].name == "port0/line1"
    assert copied_waveform.signals[0].name == "port0/line0"
    assert copied_waveform.signals[1].name == "port0/line1"

    copied_waveform.extended_properties["NI_LineNames"] = "port0/line11, port0/line10"

    assert waveform.signals[0].name == "port0/line10"
    assert waveform.signals[1].name == "port0/line11"
    assert copied_waveform.signals[0].name == "port0/line10"
    assert copied_waveform.signals[1].name == "port0/line11"


def test___deep_copied_waveform___change_line_names_property___signal_returns_new_line_name() -> (
    None
):
    waveform = DigitalWaveform(
        10, 2, extended_properties={"NI_LineNames": "port0/line1, port0/line0"}
    )
    copied_waveform = copy.deepcopy(waveform)
    assert waveform.signals[0].name == "port0/line0"
    assert waveform.signals[1].name == "port0/line1"
    assert copied_waveform.signals[0].name == "port0/line0"
    assert copied_waveform.signals[1].name == "port0/line1"

    waveform.extended_properties["NI_LineNames"] = "port0/line11, port0/line10"
    copied_waveform.extended_properties["NI_LineNames"] = "port0/line21, port0/line20"

    assert waveform.signals[0].name == "port0/line10"
    assert waveform.signals[1].name == "port0/line11"
    assert copied_waveform.signals[0].name == "port0/line20"
    assert copied_waveform.signals[1].name == "port0/line21"


###############################################################################
# signal data
###############################################################################
def test___waveform___get_signal_data___returns_line_data() -> None:
    waveform = DigitalWaveform.from_lines([[0, 1, 2], [3, 4, 5]], np.uint8)

    assert_type(waveform.signals[0].data, npt.NDArray[np.uint8])
    assert len(waveform.signals) == 3
    assert waveform.signals[0].data.tolist() == [2, 5]
    assert waveform.signals[1].data.tolist() == [1, 4]
    assert waveform.signals[2].data.tolist() == [0, 3]


def test___waveform___get_data_with_column_index___returns_line_data() -> None:
    waveform = DigitalWaveform.from_lines([[0, 1, 2], [3, 4, 5]], np.uint8)

    assert_type(waveform.signals[0].data, npt.NDArray[np.uint8])
    assert len(waveform.signals) == 3
    assert waveform.data[0][waveform.signals[0].column_index] == 2
    assert waveform.data[0][waveform.signals[1].column_index] == 1
    assert waveform.data[0][waveform.signals[2].column_index] == 0
    assert waveform.data[1][waveform.signals[0].column_index] == 5
    assert waveform.data[1][waveform.signals[1].column_index] == 4
    assert waveform.data[1][waveform.signals[2].column_index] == 3


###############################################################################
# magic methods
###############################################################################
@pytest.mark.parametrize(
    "left, right",
    [
        (
            DigitalWaveform.from_lines([0, 1, 2, 3], np.uint8).signals[0],
            DigitalWaveform.from_lines([0, 1, 2, 3], np.uint8).signals[0],
        ),
        (
            DigitalWaveform.from_lines([False, True, False], _np_bool).signals[0],
            DigitalWaveform.from_lines([False, True, False], _np_bool).signals[0],
        ),
        # Equality does not take the signal index or signal name into account.
        (
            DigitalWaveform(3, 2, extended_properties={"NI_LineNames": "0, 1"}).signals[0],
            DigitalWaveform(3, 2, extended_properties={"NI_LineNames": "0, 1"}).signals[1],
        ),
    ],
)
def test___same_value___equality___equal(
    left: DigitalWaveformSignal[Any], right: DigitalWaveformSignal[Any]
) -> None:
    assert left == right
    assert not (left != right)


@pytest.mark.parametrize(
    "left, right",
    [
        (
            DigitalWaveform.from_lines([0, 1, 2, 3], np.uint8).signals[0],
            DigitalWaveform.from_lines([0, 1, 4, 3], np.uint8).signals[0],
        ),
        (
            DigitalWaveform.from_lines([False, True, False], _np_bool).signals[0],
            DigitalWaveform.from_lines([False, False, False], _np_bool).signals[0],
        ),
    ],
)
def test___different_value___equality___not_equal(
    left: DigitalWaveformSignal[Any], right: DigitalWaveformSignal[Any]
) -> None:
    assert not (left == right)
    assert left != right


@pytest.mark.parametrize(
    "value, expected_repr",
    [
        (
            DigitalWaveform(3, 2).signals[0],
            "nitypes.waveform.DigitalWaveformSignal(data=array([0, 0, 0], dtype=uint8))",
        ),
        (
            DigitalWaveform(3, 2, _np_bool).signals[0],
            "nitypes.waveform.DigitalWaveformSignal(data=array([False, False, False]))",
        ),
        (
            DigitalWaveform(
                3, 2, extended_properties={"NI_LineNames": "port0/line1, port0/line0"}
            ).signals[1],
            "nitypes.waveform.DigitalWaveformSignal(name='port0/line1', data=array([0, 0, 0], dtype=uint8))",
        ),
    ],
)
def test___various_values___repr___looks_ok(
    value: DigitalWaveformSignal[Any], expected_repr: str
) -> None:
    assert repr(value) == expected_repr


_VARIOUS_VALUES = [
    DigitalWaveform(3, 2).signals[0],
    DigitalWaveform(3, 2, _np_bool).signals[0],
    DigitalWaveform(3, 2, extended_properties={"NI_LineNames": "port0/line1, port0/line0"}).signals[
        1
    ],
]


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___copy___makes_shallow_copy(value: DigitalWaveformSignal[Any]) -> None:
    new_value = copy.copy(value)

    _assert_shallow_copy(new_value, value)


def _assert_shallow_copy(
    value: DigitalWaveformSignal[Any], other: DigitalWaveformSignal[Any]
) -> None:
    assert value == other
    assert value is not other
    assert value._owner is other._owner


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___deepcopy___makes_deep_copy(
    value: DigitalWaveformSignal[Any],
) -> None:
    new_value = copy.deepcopy(value)

    _assert_deep_copy(new_value, value)


def _assert_deep_copy(value: DigitalWaveformSignal[Any], other: DigitalWaveformSignal[Any]) -> None:
    assert value == other
    assert value is not other
    assert value._owner is not other._owner


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___pickle_unpickle___makes_deep_copy(
    value: DigitalWaveformSignal[Any],
) -> None:
    new_value = pickle.loads(pickle.dumps(value))

    _assert_deep_copy(new_value, value)


def test___waveform___pickle___references_public_modules() -> None:
    value = DigitalWaveform(3, 2).signals[0]

    value_bytes = pickle.dumps(value)

    assert b"nitypes.waveform" in value_bytes
    assert b"nitypes.waveform._digital" not in value_bytes


@pytest.mark.parametrize(
    "pickled_value, expected",
    [
        # nitypes 1.0.0
        pytest.param(
            b"\x80\x04\x95\xfa\x01\x00\x00\x00\x00\x00\x00\x8c\x10nitypes.waveform\x94\x8c\x15DigitalWaveformSignal\x94\x93\x94\x8c\x08builtins\x94\x8c\x07getattr\x94\x93\x94h\x00\x8c\x0fDigitalWaveform\x94\x93\x94\x8c\t_unpickle\x94\x86\x94R\x94K\x03K\x02\x8c\x05numpy\x94\x8c\x05dtype\x94\x93\x94\x8c\x02u1\x94\x89\x88\x87\x94R\x94(K\x03\x8c\x01|\x94NNNJ\xff\xff\xff\xffJ\xff\xff\xff\xffK\x00t\x94b\x87\x94}\x94(\x8c\x04data\x94\x8c\x16numpy._core.multiarray\x94\x8c\x0c_reconstruct\x94\x93\x94h\x0b\x8c\x07ndarray\x94\x93\x94K\x00\x85\x94C\x01b\x94\x87\x94R\x94(K\x01K\x03K\x02\x86\x94h\x10\x89C\x06\x00\x00\x00\x00\x00\x00\x94t\x94b\x8c\x13extended_properties\x94h\x00\x8c\x1aExtendedPropertyDictionary\x94\x93\x94)\x81\x94N}\x94\x8c\x0b_properties\x94}\x94\x8c\x0cNI_LineNames\x94\x8c\x18port0/line1, port0/line0\x94ss\x86\x94b\x8c\x18copy_extended_properties\x94\x89\x8c\x06timing\x94h\x05h\x00\x8c\x06Timing\x94\x93\x94h\x08\x86\x94R\x94(h\x00\x8c\x12SampleIntervalMode\x94\x93\x94K\x00\x85\x94R\x94NNNNt\x94}\x94\x86\x94R\x94u\x86\x94R\x94K\x01\x86\x94R\x94.",
            DigitalWaveform(
                3, 2, extended_properties={"NI_LineNames": "port0/line1, port0/line0"}
            ).signals[1],
        ),
        # nitypes 1.0.1
        (
            b"\x80\x04\x95\xe8\x01\x00\x00\x00\x00\x00\x00\x8c\x10nitypes.waveform\x94\x8c\x15DigitalWaveformSignal\x94\x93\x94\x8c\x08builtins\x94\x8c\x07getattr\x94\x93\x94h\x00\x8c\x0fDigitalWaveform\x94\x93\x94\x8c\t_unpickle\x94\x86\x94R\x94K\x03K\x02\x8c\x05numpy\x94\x8c\x05dtype\x94\x93\x94\x8c\x02u1\x94\x89\x88\x87\x94R\x94(K\x03\x8c\x01|\x94NNNJ\xff\xff\xff\xffJ\xff\xff\xff\xffK\x00t\x94b\x87\x94}\x94(\x8c\x04data\x94\x8c\x16numpy._core.multiarray\x94\x8c\x0c_reconstruct\x94\x93\x94h\x0b\x8c\x07ndarray\x94\x93\x94K\x00\x85\x94C\x01b\x94\x87\x94R\x94(K\x01K\x03K\x02\x86\x94h\x10\x89C\x06\x00\x00\x00\x00\x00\x00\x94t\x94b\x8c\x13extended_properties\x94h\x00\x8c\x1aExtendedPropertyDictionary\x94\x93\x94}\x94\x8c\x0cNI_LineNames\x94\x8c\x18port0/line1, port0/line0\x94s\x85\x94R\x94\x8c\x18copy_extended_properties\x94\x89\x8c\x06timing\x94h\x05h\x00\x8c\x06Timing\x94\x93\x94h\x08\x86\x94R\x94(h\x00\x8c\x12SampleIntervalMode\x94\x93\x94K\x00\x85\x94R\x94NNNNt\x94}\x94\x86\x94R\x94u\x86\x94R\x94K\x01K\x00\x87\x94R\x94.",
            DigitalWaveform(
                3, 2, extended_properties={"NI_LineNames": "port0/line1, port0/line0"}
            ).signals[1],
        ),
    ],
)
def test___pickled_value___unpickle___is_compatible(
    pickled_value: bytes, expected: DigitalWaveformSignal[Any]
) -> None:
    new_value = pickle.loads(pickled_value)
    assert new_value == expected
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/waveform/test_extended_property_dictionary.py sha256=59b4de3d1f3ce32f61314ef0394865017fcf7b594d17c8805283af0ec87dfe51 bytes=1319 -->
## FILE: tests/unit/waveform/test_extended_property_dictionary.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/waveform/test_extended_property_dictionary.py`
- sha256: `59b4de3d1f3ce32f61314ef0394865017fcf7b594d17c8805283af0ec87dfe51`
- bytes: 1319

````python
from __future__ import annotations

import pickle

import pytest

from nitypes.waveform import ExtendedPropertyDictionary


@pytest.mark.parametrize(
    "pickled_value, expected",
    [
        # nitypes 1.0.0
        (
            b"\x80\x04\x95\x88\x00\x00\x00\x00\x00\x00\x00\x8c\x10nitypes.waveform\x94\x8c\x1aExtendedPropertyDictionary\x94\x93\x94)\x81\x94N}\x94\x8c\x0b_properties\x94}\x94(\x8c\x0eNI_ChannelName\x94\x8c\x08Dev1/ai0\x94\x8c\x12NI_UnitDescription\x94\x8c\x05Volts\x94us\x86\x94b.",
            ExtendedPropertyDictionary(
                {"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"}
            ),
        ),
        # nitypes 1.0.1
        (
            b"\x80\x04\x95t\x00\x00\x00\x00\x00\x00\x00\x8c\x10nitypes.waveform\x94\x8c\x1aExtendedPropertyDictionary\x94\x93\x94}\x94(\x8c\x0eNI_ChannelName\x94\x8c\x08Dev1/ai0\x94\x8c\x12NI_UnitDescription\x94\x8c\x05Volts\x94u\x85\x94R\x94.",
            ExtendedPropertyDictionary(
                {"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"}
            ),
        ),
    ],
)
def test___pickled_value___unpickle___is_compatible(
    pickled_value: bytes, expected: ExtendedPropertyDictionary
) -> None:
    new_value = pickle.loads(pickled_value)
    assert new_value == expected
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/waveform/test_spectrum.py sha256=dfc9f5944a640282be7f581184f9ee3c4a3a0864d5e7aaed7815428c065e0648 bytes=48446 -->
## FILE: tests/unit/waveform/test_spectrum.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/waveform/test_spectrum.py`
- sha256: `dfc9f5944a640282be7f581184f9ee3c4a3a0864d5e7aaed7815428c065e0648`
- bytes: 48446

````python
from __future__ import annotations

import array
import copy
import itertools
import pickle
import sys
import weakref
from typing import Any, SupportsIndex

import numpy as np
import numpy.typing as npt
import pytest
from packaging.version import Version
from typing_extensions import assert_type

import nitypes.waveform.errors as wfmex
from nitypes.waveform import Spectrum


###############################################################################
# create
###############################################################################
def test___no_args___create___creates_empty_spectrum_with_default_dtype() -> None:
    spectrum = Spectrum()

    assert spectrum.sample_count == spectrum.capacity == len(spectrum.data) == 0
    assert spectrum.dtype == np.float64
    assert_type(spectrum, Spectrum[np.float64])


def test___sample_count___create___creates_spectrum_with_sample_count_and_default_dtype() -> None:
    spectrum = Spectrum(10)

    assert spectrum.sample_count == spectrum.capacity == len(spectrum.data) == 10
    assert spectrum.dtype == np.float64
    assert_type(spectrum, Spectrum[np.float64])


def test___sample_count_and_dtype___create___creates_spectrum_with_sample_count_and_dtype() -> None:
    spectrum = Spectrum(10, np.int32)

    assert spectrum.sample_count == spectrum.capacity == len(spectrum.data) == 10
    assert spectrum.dtype == np.int32
    assert_type(spectrum, Spectrum[np.int32])


def test___sample_count_and_dtype_str___create___creates_spectrum_with_sample_count_and_dtype() -> (
    None
):
    spectrum = Spectrum(10, "i4")

    assert spectrum.sample_count == spectrum.capacity == len(spectrum.data) == 10
    assert spectrum.dtype == np.int32
    assert_type(spectrum, Spectrum[Any])  # dtype not inferred from string


def test___sample_count_and_dtype_any___create___creates_spectrum_with_sample_count_and_dtype() -> (
    None
):
    dtype: np.dtype[Any] = np.dtype(np.int32)
    spectrum = Spectrum(10, dtype)

    assert spectrum.sample_count == spectrum.capacity == len(spectrum.data) == 10
    assert spectrum.dtype == np.int32
    assert_type(spectrum, Spectrum[Any])  # dtype not inferred from np.dtype[Any]


def test___sample_count_dtype_and_capacity___create___creates_spectrum_with_sample_count_dtype_and_capacity() -> (
    None
):
    spectrum = Spectrum(10, np.int32, capacity=20)

    assert spectrum.sample_count == len(spectrum.data) == 10
    assert spectrum.capacity == 20
    assert spectrum.dtype == np.int32
    assert_type(spectrum, Spectrum[np.int32])


@pytest.mark.parametrize("dtype", [np.complex128, np.str_, np.void, "i2, i2"])
def test___sample_count_and_unsupported_dtype___create___raises_type_error(
    dtype: npt.DTypeLike,
) -> None:
    with pytest.raises(TypeError) as exc:
        _ = Spectrum(10, dtype)

    assert exc.value.args[0].startswith("The requested data type is not supported.")


def test___dtype_str_with_unsupported_traw_hint___create___mypy_type_var_warning() -> None:
    spectrum1: Spectrum[np.complex128] = Spectrum(dtype="int32")  # type: ignore[type-var]
    spectrum2: Spectrum[np.str_] = Spectrum(dtype="int32")  # type: ignore[type-var]
    spectrum3: Spectrum[np.void] = Spectrum(dtype="int32")  # type: ignore[type-var]
    _ = spectrum1, spectrum2, spectrum3


def test___dtype_str_with_traw_hint___create___narrows_traw() -> None:
    spectrum: Spectrum[np.int32] = Spectrum(dtype="int32")

    assert_type(spectrum, Spectrum[np.int32])


###############################################################################
# from_array_1d
###############################################################################
def test___float64_ndarray___from_array_1d___creates_spectrum_with_float64_dtype() -> None:
    data = np.array([1.1, 2.2, 3.3, 4.4, 5.5], np.float64)

    spectrum = Spectrum.from_array_1d(data)

    assert spectrum.data.tolist() == data.tolist()
    assert spectrum.dtype == np.float64
    assert_type(spectrum, Spectrum[np.float64])


def test___int32_ndarray___from_array_1d___creates_spectrum_with_int32_dtype() -> None:
    data = np.array([1, 2, 3, 4, 5], np.int32)

    spectrum = Spectrum.from_array_1d(data)

    assert spectrum.data.tolist() == data.tolist()
    assert spectrum.dtype == np.int32
    assert_type(spectrum, Spectrum[np.int32])


def test___int32_array_with_dtype___from_array_1d___creates_spectrum_with_specified_dtype() -> None:
    data = array.array("i", [1, 2, 3, 4, 5])

    spectrum = Spectrum.from_array_1d(data, np.int32)

    assert spectrum.data.tolist() == data.tolist()
    assert spectrum.dtype == np.int32
    assert_type(spectrum, Spectrum[np.int32])


def test___int16_ndarray_with_mismatched_dtype___from_array_1d___creates_spectrum_with_specified_dtype() -> (
    None
):
    data = np.array([1, 2, 3, 4, 5], np.int16)

    spectrum = Spectrum.from_array_1d(data, np.int32)

    assert spectrum.data.tolist() == data.tolist()
    assert spectrum.dtype == np.int32
    assert_type(spectrum, Spectrum[np.int32])


def test___int_list_with_dtype___from_array_1d___creates_spectrum_with_specified_dtype() -> None:
    data = [1, 2, 3, 4, 5]

    spectrum = Spectrum.from_array_1d(data, np.int32)

    assert spectrum.data.tolist() == data
    assert spectrum.dtype == np.int32
    assert_type(spectrum, Spectrum[np.int32])


def test___int_list_with_dtype_str___from_array_1d___creates_spectrum_with_specified_dtype() -> (
    None
):
    data = [1, 2, 3, 4, 5]

    spectrum = Spectrum.from_array_1d(data, "int32")

    assert spectrum.data.tolist() == data
    assert spectrum.dtype == np.int32
    assert_type(spectrum, Spectrum[Any])  # dtype not inferred from string


def test___int32_ndarray_2d___from_array_1d___raises_value_error() -> None:
    data = np.array([[1, 2, 3], [4, 5, 6]], np.int32)

    with pytest.raises(ValueError) as exc:
        _ = Spectrum.from_array_1d(data)

    assert exc.value.args[0].startswith(
        "The input array must be a one-dimensional array or sequence."
    )


def test___int_list_without_dtype___from_array_1d___raises_value_error() -> None:
    data = [1, 2, 3, 4, 5]

    with pytest.raises(ValueError) as exc:
        _ = Spectrum.from_array_1d(data)

    assert exc.value.args[0].startswith(
        "You must specify a dtype when the input array is a sequence."
    )


def test___bytes___from_array_1d___raises_value_error() -> None:
    data = b"\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00"

    with pytest.raises(ValueError) as exc:
        _ = Spectrum.from_array_1d(data, np.int32)

    assert exc.value.args[0].startswith("invalid literal for int() with base 10:")


def test___iterable___from_array_1d___raises_type_error() -> None:
    data = itertools.repeat(3)

    with pytest.raises(TypeError) as exc:
        _ = Spectrum.from_array_1d(data, np.int32)  # type: ignore[call-overload]

    assert exc.value.args[0].startswith(
        "The input array must be a one-dimensional array or sequence."
    )


def test___ndarray_with_unsupported_dtype___from_array_1d___raises_type_error() -> None:
    data = np.zeros(3, np.str_)

    with pytest.raises(TypeError) as exc:
        _ = Spectrum.from_array_1d(data)

    assert exc.value.args[0].startswith("The requested data type is not supported.")


def test___copy___from_array_1d___creates_spectrum_linked_to_different_buffer() -> None:
    data = np.array([1, 2, 3, 4, 5], np.int32)

    spectrum = Spectrum.from_array_1d(data, copy=True)

    assert spectrum._data is not data
    assert spectrum.data.tolist() == data.tolist()
    data[:] = [5, 4, 3, 2, 1]
    assert spectrum.data.tolist() != data.tolist()


def test___int32_ndarray_no_copy___from_array_1d___creates_spectrum_linked_to_same_buffer() -> None:
    data = np.array([1, 2, 3, 4, 5], np.int32)

    spectrum = Spectrum.from_array_1d(data, copy=False)

    assert spectrum._data is data
    assert spectrum.data.tolist() == data.tolist()
    data[:] = [5, 4, 3, 2, 1]
    assert spectrum.data.tolist() == data.tolist()


def test___int32_array_no_copy___from_array_1d___creates_spectrum_linked_to_same_buffer() -> None:
    data = array.array("i", [1, 2, 3, 4, 5])

    spectrum = Spectrum.from_array_1d(data, dtype=np.int32, copy=False)

    assert spectrum.data.tolist() == data.tolist()
    data[:] = array.array("i", [5, 4, 3, 2, 1])
    assert spectrum.data.tolist() == data.tolist()


def test___int_list_no_copy___from_array_1d___raises_value_error() -> None:
    data = [1, 2, 3, 4, 5]

    with pytest.raises(ValueError) as exc:
        _ = Spectrum.from_array_1d(data, np.int32, copy=False)

    assert exc.value.args[0].startswith(
        "Unable to avoid copy while creating an array as requested."
    )


@pytest.mark.parametrize(
    "start_index, sample_count, expected_data",
    [
        (0, None, [1, 2, 3, 4, 5]),
        (1, None, [2, 3, 4, 5]),
        (4, None, [5]),
        (5, None, []),
        (0, 1, [1]),
        (0, 4, [1, 2, 3, 4]),
        (1, 1, [2]),
        (1, 3, [2, 3, 4]),
        (1, 4, [2, 3, 4, 5]),
    ],
)
def test___array_subset___from_array_1d___creates_spectrum_with_array_subset(
    start_index: SupportsIndex, sample_count: SupportsIndex | None, expected_data: list[int]
) -> None:
    data = np.array([1, 2, 3, 4, 5], np.int32)

    spectrum = Spectrum.from_array_1d(data, start_index=start_index, sample_count=sample_count)

    assert spectrum.data.tolist() == expected_data


@pytest.mark.parametrize(
    "start_index, sample_count, expected_message, exception_type",
    [
        (-2, None, "The start index must be a non-negative integer.", ValueError),
        (-1, None, "The start index must be a non-negative integer.", ValueError),
        (
            6,
            None,
            "The start index must be less than or equal to the input array length.",
            wfmex.StartIndexTooLargeError,
        ),
        (0, -2, "The sample count must be a non-negative integer.", ValueError),
        (0, -1, "The sample count must be a non-negative integer.", ValueError),
        (
            0,
            6,
            "The sum of the start index and sample count must be less than or equal to the input array length.",
            wfmex.StartIndexOrSampleCountTooLargeError,
        ),
        (
            1,
            5,
            "The sum of the start index and sample count must be less than or equal to the input array length.",
            wfmex.StartIndexOrSampleCountTooLargeError,
        ),
        (
            5,
            1,
            "The sum of the start index and sample count must be less than or equal to the input array length.",
            wfmex.StartIndexOrSampleCountTooLargeError,
        ),
    ],
)
def test___invalid_array_subset___from_array_1d___raises_correct_error(
    start_index: SupportsIndex,
    sample_count: SupportsIndex | None,
    expected_message: str,
    exception_type: type[Exception],
) -> None:
    data = np.array([1, 2, 3, 4, 5], np.int32)

    with pytest.raises(exception_type) as exc:
        _ = Spectrum.from_array_1d(data, start_index=start_index, sample_count=sample_count)

    assert exc.value.args[0].startswith(expected_message)


###############################################################################
# from_array_2d
###############################################################################
def test___float64_ndarray___from_array_2d___creates_spectrum_with_float64_dtype() -> None:
    data = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]], np.float64)

    spectrums = Spectrum.from_array_2d(data)

    assert len(spectrums) == 2
    for i in range(len(spectrums)):
        assert spectrums[i].data.tolist() == data[i].tolist()
        assert spectrums[i].dtype == np.float64
        assert_type(spectrums[i], Spectrum[np.float64])


def test___int32_ndarray___from_array_2d___creates_spectrum_with_int32_dtype() -> None:
    data = np.array([[1, 2, 3], [4, 5, 6]], np.int32)

    spectrums = Spectrum.from_array_2d(data)

    assert len(spectrums) == 2
    for i in range(len(spectrums)):
        assert spectrums[i].data.tolist() == data[i].tolist()
        assert spectrums[i].dtype == np.int32
        assert_type(spectrums[i], Spectrum[np.int32])


def test___int16_ndarray_with_mismatched_dtype___from_array_2d___creates_spectrum_with_specified_dtype() -> (
    None
):
    data = np.array([[1, 2, 3], [4, 5, 6]], np.int16)

    spectrums = Spectrum.from_array_2d(data, np.int32)

    assert len(spectrums) == 2
    for i in range(len(spectrums)):
        assert spectrums[i].data.tolist() == data[i].tolist()
        assert spectrums[i].dtype == np.int32
        assert_type(spectrums[i], Spectrum[np.int32])


def test___int32_array_list_with_dtype___from_array_2d___creates_spectrum_with_specified_dtype() -> (
    None
):
    data = [array.array("i", [1, 2, 3]), array.array("i", [4, 5, 6])]

    spectrums = Spectrum.from_array_2d(data, np.int32)

    assert len(spectrums) == 2
    for i in range(len(spectrums)):
        assert spectrums[i].data.tolist() == data[i].tolist()
        assert spectrums[i].dtype == np.int32
        assert_type(spectrums[i], Spectrum[np.int32])


def test___int_list_list_with_dtype___from_array_2d___creates_spectrum_with_specified_dtype() -> (
    None
):
    data = [[1, 2, 3], [4, 5, 6]]

    spectrums = Spectrum.from_array_2d(data, np.int32)

    assert len(spectrums) == 2
    for i in range(len(spectrums)):
        assert spectrums[i].data.tolist() == data[i]
        assert spectrums[i].dtype == np.int32
        assert_type(spectrums[i], Spectrum[np.int32])


def test___int_list_list_with_dtype_str___from_array_2d___creates_spectrum_with_specified_dtype() -> (
    None
):
    data = [[1, 2, 3], [4, 5, 6]]

    spectrums = Spectrum.from_array_2d(data, "int32")

    assert len(spectrums) == 2
    for i in range(len(spectrums)):
        assert spectrums[i].data.tolist() == data[i]
        assert spectrums[i].dtype == np.int32
        assert_type(spectrums[i], Spectrum[Any])  # dtype not inferred from string


def test___int32_ndarray_1d___from_array_2d___raises_value_error() -> None:
    data = np.array([1, 2, 3, 4, 5], np.int32)

    with pytest.raises(ValueError) as exc:
        _ = Spectrum.from_array_2d(data)

    assert exc.value.args[0].startswith(
        "The input array must be a two-dimensional array or nested sequence."
    )


def test___int_list_list_without_dtype___from_array_2d___raises_value_error() -> None:
    data = [[1, 2, 3], [4, 5, 6]]

    with pytest.raises(ValueError) as exc:
        _ = Spectrum.from_array_2d(data)

    assert exc.value.args[0].startswith(
        "You must specify a dtype when the input array is a sequence."
    )


def test___bytes_list___from_array_2d___raises_value_error() -> None:
    data = [
        b"\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00",
        b"\x04\x00\x00\x00\x05\x00\x00\x00\x06\x00\x00\x00",
    ]

    with pytest.raises(ValueError) as exc:
        _ = Spectrum.from_array_2d(data, np.int32)

    assert exc.value.args[0].startswith("invalid literal for int() with base 10:")


def test___list_iterable___from_array_2d___raises_type_error() -> None:
    data = itertools.repeat([3])

    with pytest.raises(TypeError) as exc:
        _ = Spectrum.from_array_2d(data, np.int32)  # type: ignore[call-overload]

    assert exc.value.args[0].startswith(
        "The input array must be a two-dimensional array or nested sequence."
    )


def test___iterable_list___from_array_2d___raises_type_error() -> None:
    data = [itertools.repeat(3), itertools.repeat(4)]

    with pytest.raises(TypeError) as exc:
        _ = Spectrum.from_array_2d(data, np.int32)  # type: ignore[arg-type]

    assert exc.value.args[0].startswith("int() argument must be")


def test___ndarray_with_unsupported_dtype___from_array_2d___raises_type_error() -> None:
    data = np.zeros((2, 3), np.str_)

    with pytest.raises(TypeError) as exc:
        _ = Spectrum.from_array_2d(data)

    assert exc.value.args[0].startswith("The requested data type is not supported.")


def test___copy___from_array_2d___creates_spectrum_linked_to_different_buffer() -> None:
    data = np.array([[1, 2, 3], [4, 5, 6]], np.int32)

    spectrums = Spectrum.from_array_2d(data, copy=True)

    assert len(spectrums) == 2
    for i in range(len(spectrums)):
        assert spectrums[i].data.tolist() == data[i].tolist()
    data[0][:] = [3, 2, 1]
    data[1][:] = [6, 5, 4]
    for i in range(len(spectrums)):
        assert spectrums[i].data.tolist() != data[i].tolist()


def test___int32_ndarray_no_copy___from_array_2d___creates_spectrum_linked_to_same_buffer() -> None:
    data = np.array([[1, 2, 3], [4, 5, 6]], np.int32)

    spectrums = Spectrum.from_array_2d(data, copy=False)

    assert len(spectrums) == 2
    for i in range(len(spectrums)):
        assert spectrums[i].data.tolist() == data[i].tolist()
    data[0][:] = [3, 2, 1]
    data[1][:] = [6, 5, 4]
    for i in range(len(spectrums)):
        assert spectrums[i].data.tolist() == data[i].tolist()


def test___int32_array_list_no_copy___from_array_2d___creates_spectrum_linked_to_same_buffer() -> (
    None
):
    data = [array.array("i", [1, 2, 3]), array.array("i", [4, 5, 6])]

    spectrums = Spectrum.from_array_2d(data, dtype=np.int32, copy=False)

    assert len(spectrums) == 2
    for i in range(len(spectrums)):
        assert spectrums[i].data.tolist() == data[i].tolist()
    data[0][:] = array.array("i", [3, 2, 1])
    data[1][:] = array.array("i", [6, 5, 4])
    for i in range(len(spectrums)):
        assert spectrums[i].data.tolist() == data[i].tolist()


def test___int_list_list_no_copy___from_array_2d___raises_value_error() -> None:
    data = [[1, 2, 3], [4, 5, 6]]

    with pytest.raises(ValueError) as exc:
        _ = Spectrum.from_array_2d(data, np.int32, copy=False)

    assert exc.value.args[0].startswith(
        "Unable to avoid copy while creating an array as requested."
    )


@pytest.mark.parametrize(
    "start_index, sample_count, expected_data",
    [
        (0, None, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]),
        (1, None, [[2, 3, 4, 5], [7, 8, 9, 10]]),
        (4, None, [[5], [10]]),
        (5, None, [[], []]),
        (0, 1, [[1], [6]]),
        (0, 4, [[1, 2, 3, 4], [6, 7, 8, 9]]),
        (1, 1, [[2], [7]]),
        (1, 3, [[2, 3, 4], [7, 8, 9]]),
        (1, 4, [[2, 3, 4, 5], [7, 8, 9, 10]]),
    ],
)
def test___array_subset___from_array_2d___creates_spectrum_with_array_subset(
    start_index: SupportsIndex, sample_count: SupportsIndex | None, expected_data: list[list[int]]
) -> None:
    data = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], np.int32)

    spectrums = Spectrum.from_array_2d(data, start_index=start_index, sample_count=sample_count)

    assert len(spectrums) == 2
    for i in range(len(spectrums)):
        assert spectrums[i].data.tolist() == expected_data[i]


@pytest.mark.parametrize(
    "start_index, sample_count, expected_message, exception_type",
    [
        (-2, None, "The start index must be a non-negative integer.", ValueError),
        (-1, None, "The start index must be a non-negative integer.", ValueError),
        (
            6,
            None,
            "The start index must be less than or equal to the input array length.",
            wfmex.StartIndexTooLargeError,
        ),
        (0, -2, "The sample count must be a non-negative integer.", ValueError),
        (0, -1, "The sample count must be a non-negative integer.", ValueError),
        (
            0,
            6,
            "The sum of the start index and sample count must be less than or equal to the input array length.",
            wfmex.StartIndexOrSampleCountTooLargeError,
        ),
        (
            1,
            5,
            "The sum of the start index and sample count must be less than or equal to the input array length.",
            wfmex.StartIndexOrSampleCountTooLargeError,
        ),
        (
            5,
            1,
            "The sum of the start index and sample count must be less than or equal to the input array length.",
            wfmex.StartIndexOrSampleCountTooLargeError,
        ),
    ],
)
def test___invalid_array_subset___from_array_2d___raises_correct_error(
    start_index: SupportsIndex,
    sample_count: SupportsIndex | None,
    expected_message: str,
    exception_type: type[Exception],
) -> None:
    data = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], np.int32)

    with pytest.raises(exception_type) as exc:
        _ = Spectrum.from_array_2d(data, start_index=start_index, sample_count=sample_count)

    assert exc.value.args[0].startswith(expected_message)


###############################################################################
# data
###############################################################################
def test___int32_spectrum___data___returns_int32_data() -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2, 3], np.int32)

    data = spectrum.data

    assert_type(data, npt.NDArray[np.int32])
    assert isinstance(data, np.ndarray) and data.dtype == np.int32
    assert list(data) == [0, 1, 2, 3]


###############################################################################
# get_data
###############################################################################
def test___int32_spectrum___get_data___returns_data() -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2, 3], np.int32)

    scaled_data = spectrum.get_data()

    assert_type(scaled_data, npt.NDArray[np.int32])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.int32
    assert list(scaled_data) == [0, 1, 2, 3]


@pytest.mark.parametrize(
    "start_index, sample_count, expected_data",
    [
        (None, None, [0, 1, 2, 3]),
        (0, None, [0, 1, 2, 3]),
        (1, None, [1, 2, 3]),
        (3, None, [3]),
        (4, None, []),
        (None, None, [0, 1, 2, 3]),
        (None, 1, [0]),
        (None, 3, [0, 1, 2]),
        (None, 4, [0, 1, 2, 3]),
        (1, 2, [1, 2]),
        (4, 0, []),
    ],
)
def test___array_subset___get_data___returns_array_subset(
    start_index: int, sample_count: int, expected_data: list[int]
) -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2, 3], np.int32)

    scaled_data = spectrum.get_data(start_index=start_index, sample_count=sample_count)

    assert_type(scaled_data, npt.NDArray[np.int32])
    assert isinstance(scaled_data, np.ndarray) and scaled_data.dtype == np.int32
    assert list(scaled_data) == expected_data


@pytest.mark.parametrize(
    "start_index, sample_count, expected_message",
    [
        (
            5,
            None,
            "The start index must be less than or equal to the number of samples in the spectrum.",
        ),
        (
            0,
            5,
            "The sum of the start index and sample count must be less than or equal to the number of samples in the spectrum.",
        ),
        (
            4,
            1,
            "The sum of the start index and sample count must be less than or equal to the number of samples in the spectrum.",
        ),
    ],
)
def test___invalid_array_subset___get_data___returns_array_subset(
    start_index: int, sample_count: int, expected_message: str
) -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2, 3], np.int32)

    with pytest.raises(
        (wfmex.StartIndexTooLargeError, wfmex.StartIndexOrSampleCountTooLargeError)
    ) as exc:
        _ = spectrum.get_data(start_index=start_index, sample_count=sample_count)

    assert exc.value.args[0].startswith(expected_message)


###############################################################################
# capacity
###############################################################################
@pytest.mark.parametrize(
    "capacity, expected_data",
    [(3, [1, 2, 3]), (4, [1, 2, 3, 0]), (10, [1, 2, 3, 0, 0, 0, 0, 0, 0, 0])],
)
def test___spectrum___set_capacity___resizes_array_and_pads_with_zeros(
    capacity: int, expected_data: list[int]
) -> None:
    data = [1, 2, 3]
    spectrum = Spectrum.from_array_1d(data, np.int32)

    spectrum.capacity = capacity

    assert spectrum.capacity == capacity
    assert spectrum.data.tolist() == data
    assert spectrum._data.tolist() == expected_data


@pytest.mark.parametrize(
    "capacity, expected_message, exception_type",
    [
        (-2, "The capacity must be a non-negative integer.", ValueError),
        (-1, "The capacity must be a non-negative integer.", ValueError),
        (
            0,
            "The capacity must be equal to or greater than the number of samples in the spectrum.",
            wfmex.CapacityTooSmallError,
        ),
        (
            2,
            "The capacity must be equal to or greater than the number of samples in the spectrum.",
            wfmex.CapacityTooSmallError,
        ),
    ],
)
def test___invalid_capacity___set_capacity___raises_correct_error(
    capacity: int, expected_message: str, exception_type: type[Exception]
) -> None:
    data = [1, 2, 3]
    spectrum = Spectrum.from_array_1d(data, np.int32)

    with pytest.raises(exception_type) as exc:
        spectrum.capacity = capacity

    assert exc.value.args[0].startswith(expected_message)


def test___referenced_array___set_capacity___reference_sees_size_change() -> None:
    data = np.array([1, 2, 3], np.int32)
    spectrum = Spectrum.from_array_1d(data, np.int32, copy=False)

    spectrum.capacity = 10

    assert len(data) == 10
    assert spectrum.capacity == 10
    assert data.tolist() == [1, 2, 3, 0, 0, 0, 0, 0, 0, 0]
    assert spectrum.data.tolist() == [1, 2, 3]
    assert spectrum._data.tolist() == [1, 2, 3, 0, 0, 0, 0, 0, 0, 0]


def test___array_with_external_buffer___set_capacity___raises_value_error() -> None:
    data = array.array("i", [1, 2, 3])
    spectrum = Spectrum.from_array_1d(data, np.int32, copy=False)

    with pytest.raises(ValueError) as exc:
        spectrum.capacity = 10

    assert exc.value.args[0].startswith("cannot resize this array: it does not own its data")


###############################################################################
# extended properties
###############################################################################
def test___spectrum___set_channel_name___sets_extended_property() -> None:
    spectrum = Spectrum()

    spectrum.channel_name = "Dev1/ai0"

    assert spectrum.channel_name == "Dev1/ai0"
    assert spectrum.extended_properties["NI_ChannelName"] == "Dev1/ai0"


def test___invalid_type___set_channel_name___raises_type_error() -> None:
    spectrum = Spectrum()

    with pytest.raises(TypeError) as exc:
        spectrum.channel_name = 1  # type: ignore[assignment]

    assert exc.value.args[0].startswith("The channel name must be a str.")


def test___spectrum___set_units___sets_extended_property() -> None:
    spectrum = Spectrum()

    spectrum.units = "Volts"

    assert spectrum.units == "Volts"
    assert spectrum.extended_properties["NI_UnitDescription"] == "Volts"


def test___invalid_type___set_units___raises_type_error() -> None:
    spectrum = Spectrum()

    with pytest.raises(TypeError) as exc:
        spectrum.units = None  # type: ignore[assignment]

    assert exc.value.args[0].startswith("The units must be a str.")


def test___spectrum___set_undefined_property___raises_attribute_error() -> None:
    spectrum = Spectrum()

    with pytest.raises(AttributeError):
        spectrum.undefined_property = "Whatever"  # type: ignore[attr-defined]


def test___spectrum___take_weak_ref___references_spectrum() -> None:
    spectrum = Spectrum()

    spectrum_ref = weakref.ref(spectrum)

    assert spectrum_ref() is spectrum


###############################################################################
# frequency range
###############################################################################
def test___spectrum___has_default_frequency_range() -> None:
    spectrum = Spectrum()

    assert spectrum.start_frequency == 0.0
    assert spectrum.frequency_increment == 0.0


def test___spectrum_with_frequencies___has_specified_frequency_range() -> None:
    spectrum = Spectrum(start_frequency=123.456, frequency_increment=0.1)

    assert spectrum.start_frequency == 123.456
    assert spectrum.frequency_increment == 0.1


def test___spectrum_with_frequencies___set_frequencies___has_set_frequency_range() -> None:
    spectrum = Spectrum(start_frequency=123.456, frequency_increment=0.1)

    spectrum.start_frequency = 234.567
    spectrum.frequency_increment = 0.2

    assert spectrum.start_frequency == 234.567
    assert spectrum.frequency_increment == 0.2


###############################################################################
# append array
###############################################################################
def test___empty_ndarray___append___no_effect() -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2], np.int32)
    array = np.array([], np.int32)

    spectrum.append(array)

    assert list(spectrum.data) == [0, 1, 2]


def test___int32_ndarray___append___appends_array() -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2], np.int32)
    array = np.array([3, 4, 5], np.int32)

    spectrum.append(array)

    assert list(spectrum.data) == [0, 1, 2, 3, 4, 5]


def test___float64_ndarray___append___appends_array() -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2], np.float64)
    array = np.array([3, 4, 5], np.float64)

    spectrum.append(array)

    assert list(spectrum.data) == [0, 1, 2, 3, 4, 5]


def test___ndarray_with_mismatched_dtype___append___raises_correct_error() -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2], np.float64)
    array = np.array([3, 4, 5], np.int32)

    with pytest.raises(wfmex.DatatypeMismatchError) as exc:
        spectrum.append(array)  # type: ignore[arg-type]

    assert exc.value.args[0].startswith(
        "The data type of the input array must match the spectrum data type."
    )


def test___ndarray_2d___append___raises_value_error() -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2], np.float64)
    array = np.array([[3, 4, 5], [6, 7, 8]], np.float64)

    with pytest.raises(ValueError) as exc:
        spectrum.append(array)

    assert exc.value.args[0].startswith("The input array must be a one-dimensional array.")


###############################################################################
# append spectrum
###############################################################################
def test___empty_spectrum___append___no_effect() -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2], np.int32)
    other = Spectrum(dtype=np.int32)

    spectrum.append(other)

    assert list(spectrum.data) == [0, 1, 2]


def test___int32_spectrum___append___appends_spectrum() -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2], np.int32)
    other = Spectrum.from_array_1d([3, 4, 5], np.int32)

    spectrum.append(other)

    assert list(spectrum.data) == [0, 1, 2, 3, 4, 5]


def test___float64_spectrum___append___appends_spectrum() -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2], np.float64)
    other = Spectrum.from_array_1d([3, 4, 5], np.float64)

    spectrum.append(other)

    assert list(spectrum.data) == [0, 1, 2, 3, 4, 5]


def test___spectrum_with_mismatched_dtype___append___raises_correct_error() -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2], np.float64)
    other = Spectrum.from_array_1d([3, 4, 5], np.int32)

    with pytest.raises(wfmex.DatatypeMismatchError) as exc:
        spectrum.append(other)  # type: ignore[arg-type]

    assert exc.value.args[0].startswith(
        "The data type of the input spectrum must match the spectrum data type."
    )


###############################################################################
# append spectrums
###############################################################################
def test___empty_spectrum_list___append___no_effect() -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2], np.int32)
    other: list[Spectrum[np.int32]] = []

    spectrum.append(other)

    assert list(spectrum.data) == [0, 1, 2]


def test___int32_spectrum_list___append___appends_spectrum() -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2], np.int32)
    other = [
        Spectrum.from_array_1d([3, 4, 5], np.int32),
        Spectrum.from_array_1d([6], np.int32),
        Spectrum.from_array_1d([7, 8], np.int32),
    ]

    spectrum.append(other)

    assert list(spectrum.data) == [0, 1, 2, 3, 4, 5, 6, 7, 8]


def test___float64_spectrum_tuple___append___appends_spectrum() -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2], np.float64)
    other = (
        Spectrum.from_array_1d([3, 4, 5], np.float64),
        Spectrum.from_array_1d([6, 7, 8], np.float64),
    )

    spectrum.append(other)

    assert list(spectrum.data) == [0, 1, 2, 3, 4, 5, 6, 7, 8]


def test___spectrum_list_with_mismatched_dtype___append___raises_correct_error_and_does_not_append() -> (
    None
):
    spectrum = Spectrum.from_array_1d([0, 1, 2], np.float64)
    other = [
        Spectrum.from_array_1d([3, 4, 5], np.float64),
        Spectrum.from_array_1d([6, 7, 8], np.int32),
    ]

    with pytest.raises(wfmex.DatatypeMismatchError) as exc:
        spectrum.append(other)  # type: ignore[arg-type]

    assert exc.value.args[0].startswith(
        "The data type of the input spectrum must match the spectrum data type."
    )
    assert list(spectrum.data) == [0, 1, 2]


###############################################################################
# load data
###############################################################################
def test___empty_ndarray___load_data___clears_data() -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2], np.int32)
    array = np.array([], np.int32)

    spectrum.load_data(array)

    assert list(spectrum.data) == []


def test___int32_ndarray___load_data___overwrites_data() -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2], np.int32)
    array = np.array([3, 4, 5], np.int32)

    spectrum.load_data(array)

    assert list(spectrum.data) == [3, 4, 5]


def test___float64_ndarray___load_data___overwrites_data() -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2], np.float64)
    array = np.array([3, 4, 5], np.float64)

    spectrum.load_data(array)

    assert list(spectrum.data) == [3, 4, 5]


def test___ndarray_with_mismatched_dtype___load_data___raises_correct_error() -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2], np.float64)
    array = np.array([3, 4, 5], np.int32)

    with pytest.raises(wfmex.DatatypeMismatchError) as exc:
        spectrum.load_data(array)  # type: ignore[arg-type]

    assert exc.value.args[0].startswith(
        "The data type of the input array must match the spectrum data type."
    )


def test___ndarray_2d___load_data___raises_value_error() -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2], np.float64)
    array = np.array([[3, 4, 5], [6, 7, 8]], np.float64)

    with pytest.raises(ValueError) as exc:
        spectrum.load_data(array)

    assert exc.value.args[0].startswith("The input array must be a one-dimensional array.")


def test___smaller_ndarray___load_data___preserves_capacity() -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2], np.int32)
    array = np.array([3], np.int32)

    spectrum.load_data(array)

    assert list(spectrum.data) == [3]
    assert spectrum.capacity == 3


def test___larger_ndarray___load_data___grows_capacity() -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2], np.int32)
    array = np.array([3, 4, 5, 6], np.int32)

    spectrum.load_data(array)

    assert list(spectrum.data) == [3, 4, 5, 6]
    assert spectrum.capacity == 4


def test___spectrum_with_start_index___load_data___clears_start_index() -> None:
    spectrum = Spectrum.from_array_1d(
        np.array([0, 1, 2], np.int32), np.int32, copy=False, start_index=1, sample_count=1
    )
    assert spectrum.start_index == 1
    array = np.array([3], np.int32)

    spectrum.load_data(array)

    assert list(spectrum.data) == [3]
    assert spectrum.start_index == 0


def test___ndarray_subset___load_data___overwrites_data() -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2], np.int32)
    array = np.array([3, 4, 5], np.int32)

    spectrum.load_data(array, start_index=1, sample_count=1)

    assert list(spectrum.data) == [4]
    assert spectrum.start_index == 0
    assert spectrum.capacity == 3


def test___smaller_ndarray_no_copy___load_data___takes_ownership_of_array() -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2], np.int32)
    array = np.array([3], np.int32)

    spectrum.load_data(array, copy=False)

    assert list(spectrum.data) == [3]
    assert spectrum._data is array


def test___larger_ndarray_no_copy___load_data___takes_ownership_of_array() -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2], np.int32)
    array = np.array([3, 4, 5, 6], np.int32)

    spectrum.load_data(array, copy=False)

    assert list(spectrum.data) == [3, 4, 5, 6]
    assert spectrum._data is array


def test___ndarray_subset_no_copy___load_data___takes_ownership_of_array_subset() -> None:
    spectrum = Spectrum.from_array_1d([0, 1, 2], np.int32)
    array = np.array([3, 4, 5, 6], np.int32)

    spectrum.load_data(array, copy=False, start_index=1, sample_count=2)

    assert list(spectrum.data) == [4, 5]
    assert spectrum._data is array


###############################################################################
# magic methods
###############################################################################
@pytest.mark.parametrize(
    "left, right",
    [
        (Spectrum(), Spectrum()),
        (Spectrum(10), Spectrum(10)),
        (Spectrum(10, np.float64), Spectrum(10, np.float64)),
        (Spectrum(10, np.int32), Spectrum(10, np.int32)),
        (
            Spectrum(10, np.int32, start_index=5, capacity=20),
            Spectrum(10, np.int32, start_index=5, capacity=20),
        ),
        (
            Spectrum.from_array_1d([1, 2, 3], np.float64),
            Spectrum.from_array_1d([1, 2, 3], np.float64),
        ),
        (
            Spectrum.from_array_1d([1, 2, 3], np.int32),
            Spectrum.from_array_1d([1, 2, 3], np.int32),
        ),
        (
            Spectrum(
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"}
            ),
            Spectrum(
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"}
            ),
        ),
        # start_index and capacity may differ as long as data and sample_count are the same.
        (
            Spectrum(10, np.int32, start_index=5, capacity=20),
            Spectrum(10, np.int32, start_index=10, capacity=25),
        ),
        (
            Spectrum.from_array_1d(
                [0, 0, 1, 2, 3, 4, 5, 0], np.int32, start_index=2, sample_count=5
            ),
            Spectrum.from_array_1d(
                [0, 1, 2, 3, 4, 5, 0, 0, 0], np.int32, start_index=1, sample_count=5
            ),
        ),
    ],
)
def test___same_value___equality___equal(left: Spectrum[Any], right: Spectrum[Any]) -> None:
    assert left == right
    assert not (left != right)


@pytest.mark.parametrize(
    "left, right",
    [
        (Spectrum(), Spectrum(10)),
        (Spectrum(10), Spectrum(11)),
        (Spectrum(10, np.float64), Spectrum(10, np.int32)),
        (
            Spectrum(15, np.int32, start_index=5, capacity=20),
            Spectrum(10, np.int32, start_index=5, capacity=20),
        ),
        (
            Spectrum.from_array_1d([1, 4, 3], np.float64),
            Spectrum.from_array_1d([1, 2, 3], np.float64),
        ),
        (
            Spectrum.from_array_1d([1, 2, 3], np.int32),
            Spectrum.from_array_1d([1, 2, 3], np.float64),
        ),
        (
            Spectrum(
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"}
            ),
            Spectrum(
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Amps"}
            ),
        ),
    ],
)
def test___different_value___equality___not_equal(
    left: Spectrum[Any], right: Spectrum[Any]
) -> None:
    assert not (left == right)
    assert left != right


if Version(np.__version__) >= Version("2.0.0") or sys.platform != "win32":
    _NDARRAY_DTYPE_INT32 = ", dtype=int32"
else:
    _NDARRAY_DTYPE_INT32 = ""


@pytest.mark.parametrize(
    "value, expected_repr",
    [
        (Spectrum(), "nitypes.waveform.Spectrum(0)"),
        (
            Spectrum(5),
            "nitypes.waveform.Spectrum(5, data=array([0., 0., 0., 0., 0.]))",
        ),
        (
            Spectrum(5, np.float64),
            "nitypes.waveform.Spectrum(5, data=array([0., 0., 0., 0., 0.]))",
        ),
        (Spectrum(0, np.int32), "nitypes.waveform.Spectrum(0, int32)"),
        (
            Spectrum(5, np.int32),
            f"nitypes.waveform.Spectrum(5, int32, data=array([0, 0, 0, 0, 0]{_NDARRAY_DTYPE_INT32}))",
        ),
        (
            Spectrum(5, np.int32, start_index=5, capacity=20),
            f"nitypes.waveform.Spectrum(5, int32, data=array([0, 0, 0, 0, 0]{_NDARRAY_DTYPE_INT32}))",
        ),
        (
            Spectrum.from_array_1d([1, 2, 3], np.float64),
            "nitypes.waveform.Spectrum(3, data=array([1., 2., 3.]))",
        ),
        (
            Spectrum.from_array_1d([1, 2, 3], np.int32),
            f"nitypes.waveform.Spectrum(3, int32, data=array([1, 2, 3]{_NDARRAY_DTYPE_INT32}))",
        ),
        (
            Spectrum(
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"}
            ),
            "nitypes.waveform.Spectrum(0, extended_properties={'NI_ChannelName': 'Dev1/ai0', "
            "'NI_UnitDescription': 'Volts'})",
        ),
        (
            Spectrum.from_array_1d(
                [1, 2, 3],
                np.int32,
                start_frequency=123.456,
                frequency_increment=0.1,
            ),
            f"nitypes.waveform.Spectrum(3, int32, data=array([1, 2, 3]{_NDARRAY_DTYPE_INT32}), "
            "start_frequency=123.456, frequency_increment=0.1)",
        ),
        (
            Spectrum.from_array_1d(
                [1, 2, 3],
                np.int32,
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"},
            ),
            f"nitypes.waveform.Spectrum(3, int32, data=array([1, 2, 3]{_NDARRAY_DTYPE_INT32}), "
            "extended_properties={'NI_ChannelName': 'Dev1/ai0', 'NI_UnitDescription': 'Volts'})",
        ),
    ],
)
def test___various_values___repr___looks_ok(value: Spectrum[Any], expected_repr: str) -> None:
    assert repr(value) == expected_repr


_VARIOUS_VALUES = [
    Spectrum(),
    Spectrum(10),
    Spectrum(10, np.float64),
    Spectrum(10, np.int32),
    Spectrum(10, np.int32, start_index=5, capacity=20),
    Spectrum.from_array_1d([1, 2, 3], np.float64),
    Spectrum.from_array_1d([1, 2, 3], np.int32),
    Spectrum(start_frequency=123.456, frequency_increment=0.1),
    Spectrum(extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"}),
    Spectrum(10, np.int32, start_index=5, capacity=20),
    Spectrum.from_array_1d([0, 0, 1, 2, 3, 4, 5, 0], np.int32, start_index=2, sample_count=5),
]


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___copy___makes_shallow_copy(value: Spectrum[Any]) -> None:
    new_value = copy.copy(value)

    _assert_shallow_copy(new_value, value)


def _assert_shallow_copy(value: Spectrum[Any], other: Spectrum[Any]) -> None:
    assert value == other
    assert value is not other
    # _data may be a view of the original array.
    assert value._data is other._data or value._data.base is other._data
    assert value._start_frequency == other._start_frequency
    assert value._frequency_increment == other._frequency_increment
    assert value._extended_properties is other._extended_properties


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___deepcopy___makes_shallow_copy(value: Spectrum[Any]) -> None:
    new_value = copy.deepcopy(value)

    _assert_deep_copy(new_value, value)


def _assert_deep_copy(value: Spectrum[Any], other: Spectrum[Any]) -> None:
    assert value == other
    assert value is not other
    assert value._data is not other._data and value._data.base is not other._data
    assert value._start_frequency == other._start_frequency
    assert value._frequency_increment == other._frequency_increment
    assert value._extended_properties is not other._extended_properties


@pytest.mark.parametrize("value", _VARIOUS_VALUES)
def test___various_values___pickle_unpickle___makes_deep_copy(
    value: Spectrum[Any],
) -> None:
    new_value = pickle.loads(pickle.dumps(value))

    _assert_deep_copy(new_value, value)


def test___spectrum___pickle___references_public_modules() -> None:
    value = Spectrum(
        data=np.array([1, 2, 3], np.float64),
        start_frequency=123.456,
        frequency_increment=0.1,
        extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"},
    )

    value_bytes = pickle.dumps(value)

    assert b"nitypes.waveform" in value_bytes
    assert b"nitypes.waveform._extended_properties" not in value_bytes
    assert b"nitypes.waveform._spectrum" not in value_bytes


@pytest.mark.parametrize(
    "pickled_value, expected",
    [
        # nitypes 1.0.0
        (
            b"\x80\x04\x95\xdf\x01\x00\x00\x00\x00\x00\x00\x8c\x08builtins\x94\x8c\x07getattr\x94\x93\x94\x8c\x10nitypes.waveform\x94\x8c\x08Spectrum\x94\x93\x94\x8c\t_unpickle\x94\x86\x94R\x94K\x03\x8c\x05numpy\x94\x8c\x05dtype\x94\x93\x94\x8c\x02f8\x94\x89\x88\x87\x94R\x94(K\x03\x8c\x01<\x94NNNJ\xff\xff\xff\xffJ\xff\xff\xff\xffK\x00t\x94b\x86\x94}\x94(\x8c\x04data\x94\x8c\x16numpy._core.multiarray\x94\x8c\x0c_reconstruct\x94\x93\x94h\t\x8c\x07ndarray\x94\x93\x94K\x00\x85\x94C\x01b\x94\x87\x94R\x94(K\x01K\x03\x85\x94h\x0e\x89C\x18\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x08@\x94t\x94b\x8c\x0fstart_frequency\x94G@^\xdd/\x1a\x9f\xbew\x8c\x13frequency_increment\x94G?\xb9\x99\x99\x99\x99\x99\x9a\x8c\x13extended_properties\x94h\x03\x8c\x1aExtendedPropertyDictionary\x94\x93\x94)\x81\x94N}\x94\x8c\x0b_properties\x94}\x94(\x8c\x0eNI_ChannelName\x94\x8c\x08Dev1/ai0\x94\x8c\x12NI_UnitDescription\x94\x8c\x05Volts\x94us\x86\x94b\x8c\x18copy_extended_properties\x94\x89u\x86\x94R\x94.",
            Spectrum(
                data=np.array([1, 2, 3], np.float64),
                start_frequency=123.456,
                frequency_increment=0.1,
                extended_properties={"NI_ChannelName": "Dev1/ai0", "NI_UnitDescription": "Volts"},
            ),
        ),
    ],
)
def test___pickled_value___unpickle___is_compatible(
    pickled_value: bytes, expected: Spectrum[Any]
) -> None:
    new_value = pickle.loads(pickled_value)
    assert new_value == expected
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/xy_data/__init__.py sha256=5230a64612398f9621b69e20447a5e5bf7a76628ae3745f8f35146d59c3feb31 bytes=51 -->
## FILE: tests/unit/xy_data/__init__.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/xy_data/__init__.py`
- sha256: `5230a64612398f9621b69e20447a5e5bf7a76628ae3745f8f35146d59c3feb31`
- bytes: 51

````python
"""Unit tests for the nitypes.xy_data package."""
````

<!--NI_OSS_SOURCE repo=nitypes-python path=tests/unit/xy_data/test_xy_data.py sha256=30ec886a9b44d6ec714d4ee96a589cf660af8665b3ecce922d7af7dc138c917c bytes=18963 -->
## FILE: tests/unit/xy_data/test_xy_data.py

- repository: `ni/nitypes-python`
- source_path: `tests/unit/xy_data/test_xy_data.py`
- sha256: `30ec886a9b44d6ec714d4ee96a589cf660af8665b3ecce922d7af7dc138c917c`
- bytes: 18963

````python
from __future__ import annotations

import array
import copy
import itertools
import pickle
import sys
from typing import Any

import numpy as np
import pytest
from packaging.version import Version
from typing_extensions import assert_type

from nitypes.waveform._extended_properties import ExtendedPropertyDictionary
from nitypes.xy_data import _UNIT_DESCRIPTION_X, _UNIT_DESCRIPTION_Y, TData, XYData


###############################################################################
# create
###############################################################################
def test___data_and_dtype___create___creates_xydata_with_data_dtype_and_default_units() -> None:
    data = np.array([1, 2, 3, 4, 5], np.int32)
    xydata = XYData(data, data)

    assert xydata.dtype == np.int32
    assert_type(xydata, XYData[np.int32])
    assert xydata.x_units == ""
    assert xydata.y_units == ""


def test___data_dtype_and_units___create___creates_xydata_with_data_dtype_and_units() -> None:
    data = np.array([1, 2, 3, 4, 5], np.int32)
    xydata = XYData(data, data, x_units="volts", y_units="seconds")

    assert xydata.dtype == np.int32
    assert_type(xydata, XYData[np.int32])
    assert xydata.x_units == "volts"
    assert xydata.y_units == "seconds"


def test___both_x_units_specified_unequal__create___raises_value_error() -> None:
    data = np.array([1, 2, 3, 4, 5], np.int32)
    with pytest.raises(ValueError) as exc:
        _ = XYData(data, data, x_units="Volts", extended_properties={_UNIT_DESCRIPTION_X: "Amps"})

    assert exc.value.args[0].startswith(
        "The specified x_units input does not match the units specified in extended_properties."
    )


def test___both_y_units_specified_unequal__create___raises_value_error() -> None:
    data = np.array([1, 2, 3, 4, 5], np.int32)
    with pytest.raises(ValueError) as exc:
        _ = XYData(data, data, y_units="Volts", extended_properties={_UNIT_DESCRIPTION_Y: "Amps"})

    assert exc.value.args[0].startswith(
        "The specified y_units input does not match the units specified in extended_properties."
    )


def test___x_units_only_specified_in_extended_properties__create___creates_with_units() -> None:
    data = np.array([1, 2, 3, 4, 5], np.int32)
    xydata = XYData(data, data, extended_properties={_UNIT_DESCRIPTION_X: "Volts"})
    assert xydata.x_units == "Volts"


def test___y_units_only_specified_in_extended_properties__create___creates_with_units() -> None:
    data = np.array([1, 2, 3, 4, 5], np.int32)
    xydata = XYData(data, data, extended_properties={_UNIT_DESCRIPTION_Y: "Volts"})
    assert xydata.y_units == "Volts"


def test___mismatched_dtypes___create___raises_type_error() -> None:
    data = np.array([1, 2, 3, 4, 5], np.int32)
    data2 = np.array([1, 2, 3, 4, 5], np.float64)

    with pytest.raises(TypeError) as exc:
        _ = XYData(data, data2)

    assert exc.value.args[0].startswith("x_data and y_data must have the same type.")


@pytest.mark.parametrize(
    "data",
    [
        np.array([1 + 2j, 3 - 4j, -5 + 6j, -7 - 8j], dtype=np.complex128),
        np.array(["a", "b", "c"], dtype=np.str_),
        np.array([b"\x01\x02", b"\x03\x04"], dtype=np.void),
        np.array([(1, 2), (3, 4)], dtype="i2,i2"),
    ],
)
def test___unsupported_dtype___create___raises_type_error(
    data: np.ndarray,
) -> None:
    with pytest.raises(TypeError) as exc:
        _ = XYData(data, data)

    assert exc.value.args[0].startswith("The requested data type is not supported.")


###############################################################################
# from_arrays_1d
###############################################################################
def test___float64_ndarray___from_arrays_1d___creates_xydata_with_float64_dtype() -> None:
    data = np.array([1.1, 2.2, 3.3, 4.4, 5.5], np.float64)

    xydata = XYData.from_arrays_1d(data, data)

    assert xydata.x_data.tolist() == data.tolist()
    assert xydata.y_data.tolist() == data.tolist()
    assert xydata.dtype == np.float64
    assert_type(xydata, XYData[np.float64])
    assert xydata.x_units == ""
    assert xydata.y_units == ""


def test___float64_ndarray_with_units___from_arrays_1d___creates_xydata_with_float64_dtype_and_units() -> (
    None
):
    data = np.array([1.1, 2.2, 3.3, 4.4, 5.5], np.float64)

    xydata = XYData.from_arrays_1d(data, data, x_units="amps", y_units="hours")

    assert xydata.x_data.tolist() == data.tolist()
    assert xydata.y_data.tolist() == data.tolist()
    assert xydata.dtype == np.float64
    assert_type(xydata, XYData[np.float64])
    assert xydata.x_units == "amps"
    assert xydata.y_units == "hours"


def test___int32_ndarray___from_arrays_1d___creates_xydata_with_int32_dtype() -> None:
    data = np.array([1, 2, 3, 4, 5], np.int32)

    xydata = XYData.from_arrays_1d(data, data)

    assert xydata.x_data.tolist() == data.tolist()
    assert xydata.y_data.tolist() == data.tolist()
    assert xydata.dtype == np.int32
    assert_type(xydata, XYData[np.int32])


def test___int32_array_with_dtype___from_arrays_1d___creates_xydata_with_specified_dtype() -> None:
    data = array.array("i", [1, 2, 3, 4, 5])

    xydata = XYData.from_arrays_1d(data, data, np.int32)

    assert xydata.x_data.tolist() == data.tolist()
    assert xydata.y_data.tolist() == data.tolist()
    assert xydata.dtype == np.int32
    assert_type(xydata, XYData[np.int32])


def test___int16_ndarray_with_mismatched_dtype___from_arrays_1d___creates_xydata_with_specified_dtype() -> (
    None
):
    data = np.array([1, 2, 3, 4, 5], np.int16)

    xydata = XYData.from_arrays_1d(data, data, np.int32)

    assert xydata.x_data.tolist() == data.tolist()
    assert xydata.y_data.tolist() == data.tolist()
    assert xydata.dtype == np.int32
    assert_type(xydata, XYData[np.int32])


def test___int_list_with_dtype___from_arrays_1d___creates_xydata_with_specified_dtype() -> None:
    data = [1, 2, 3, 4, 5]

    xydata = XYData.from_arrays_1d(data, data, np.int32)

    assert xydata.x_data.tolist() == data
    assert xydata.y_data.tolist() == data
    assert xydata.dtype == np.int32
    assert_type(xydata, XYData[np.int32])


def test___int_list_with_dtype_str___from_arrays_1d___creates_xydata_with_specified_dtype() -> None:
    data = [1, 2, 3, 4, 5]

    xydata = XYData.from_arrays_1d(data, data, "int32")

    assert xydata.x_data.tolist() == data
    assert xydata.y_data.tolist() == data
    assert xydata.dtype == np.int32
    assert_type(xydata, XYData[Any])  # dtype not inferred from string


def test___int32_ndarray_2d___from_arrays_1d___raises_value_error() -> None:
    data = np.array([[1, 2, 3], [4, 5, 6]], np.int32)

    with pytest.raises(ValueError) as exc:
        _ = XYData.from_arrays_1d(data, data)

    assert exc.value.args[0].startswith(
        "The input array must be a one-dimensional array or sequence."
    )


def test___int_list_without_dtype___from_arrays_1d___raises_value_error() -> None:
    data = [1, 2, 3, 4, 5]

    with pytest.raises(ValueError) as exc:
        _ = XYData.from_arrays_1d(data, data)

    assert exc.value.args[0].startswith(
        "You must specify a dtype when the input array is a sequence."
    )


def test___bytes___from_arrays_1d___raises_value_error() -> None:
    data = b"\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00"

    with pytest.raises(ValueError) as exc:
        _ = XYData.from_arrays_1d(data, data, np.int32)

    assert exc.value.args[0].startswith("invalid literal for int() with base 10:")


def test___iterable___from_arrays_1d___raises_type_error() -> None:
    data = itertools.repeat(3)

    with pytest.raises(TypeError) as exc:
        _ = XYData.from_arrays_1d(data, data, np.int32)  # type: ignore[call-overload]

    assert exc.value.args[0].startswith(
        "The input array must be a one-dimensional array or sequence."
    )


def test___ndarray_with_unsupported_dtype___from_arrays_1d___raises_type_error() -> None:
    data = np.zeros(3, np.str_)

    with pytest.raises(TypeError) as exc:
        _ = XYData.from_arrays_1d(data, data)

    assert exc.value.args[0].startswith("The requested data type is not supported.")


def test___copy___from_arrays_1d___creates_xydata_linked_to_different_buffer() -> None:
    x_data = np.array([1, 2, 3, 4, 5], np.int32)
    y_data = np.array([6, 7, 8, 9, 10], np.int32)

    xydata = XYData.from_arrays_1d(x_data, y_data, copy=True)

    assert xydata.x_data is not x_data
    assert xydata.x_data.tolist() == x_data.tolist()
    x_data[:] = [5, 4, 3, 2, 1]
    assert xydata.x_data.tolist() != x_data.tolist()

    assert xydata.y_data is not y_data
    assert xydata.y_data.tolist() == y_data.tolist()
    y_data[:] = [5, 4, 3, 2, 1]
    assert xydata.y_data.tolist() != y_data.tolist()


def test___int32_ndarray_no_copy___from_arrays_1d___creates_xydata_linked_to_same_buffer() -> None:
    x_data = np.array([1, 2, 3, 4, 5], np.int32)
    y_data = np.array([6, 7, 8, 9, 10], np.int32)

    xydata = XYData.from_arrays_1d(x_data, y_data, copy=False)

    assert xydata._x_data is x_data
    assert xydata.x_data.tolist() == x_data.tolist()
    x_data[:] = [5, 4, 3, 2, 1]
    assert xydata.x_data.tolist() == x_data.tolist()

    assert xydata._y_data is y_data
    assert xydata.y_data.tolist() == y_data.tolist()
    y_data[:] = [5, 4, 3, 2, 1]
    assert xydata.y_data.tolist() == y_data.tolist()


def test___int_list_no_copy___from_arrays_1d___raises_value_error() -> None:
    x_data = [1, 2, 3, 4, 5]
    y_data = [6, 7, 8, 9, 10]

    with pytest.raises(ValueError) as exc:
        _ = XYData.from_arrays_1d(x_data, y_data, np.int32, copy=False)

    assert exc.value.args[0].startswith(
        "Unable to avoid copy while creating an array as requested."
    )


###############################################################################
# compare
###############################################################################
@pytest.mark.parametrize(
    "left, right",
    [
        (
            XYData.from_arrays_1d([1, 2], [3, 4], np.int32),
            XYData.from_arrays_1d([1, 2], [3, 4], np.int32),
        ),
        (
            XYData.from_arrays_1d([1.0, 2.0], [3.0, 4.0], np.int32),
            XYData.from_arrays_1d([1.0, 2.0], [3.0, 4.0], np.int32),
        ),
    ],
)
def test___same_value___comparison___equal(left: XYData[TData], right: XYData[TData]) -> None:
    assert left == right


@pytest.mark.parametrize(
    "left, right",
    [
        (
            XYData.from_arrays_1d([1, 2], [5, 6], np.int32),
            XYData.from_arrays_1d([1, 2], [3, 4], np.int32),
        ),
        (
            XYData.from_arrays_1d([1.0, 2.0], [5.0, 6.0], np.int32),
            XYData.from_arrays_1d([1.0, 2.0], [3.0, 4.0], np.int32),
        ),
    ],
)
def test___different_values___comparison___not_equal(
    left: XYData[TData], right: XYData[TData]
) -> None:
    assert left != right


def test___different_units___comparison___not_equal() -> None:
    left = XYData.from_arrays_1d([0], [0], np.int32, x_units="volts", y_units="seconds")
    right = XYData.from_arrays_1d([0], [0], np.int32, x_units="amps", y_units="seconds")

    assert left != right


###############################################################################
# other operators
###############################################################################
if Version(np.__version__) >= Version("2.0.0") or sys.platform != "win32":
    _NDARRAY_DTYPE_INT32 = ", dtype=int32"
else:
    _NDARRAY_DTYPE_INT32 = ""


@pytest.mark.parametrize(
    "value, expected_repr",
    [
        (
            XYData.from_arrays_1d([10], [20], np.int32),
            f"nitypes.xy_data.XYData(x_data=array([10]{_NDARRAY_DTYPE_INT32}), "
            f"y_data=array([20]{_NDARRAY_DTYPE_INT32}))",
        ),
        (
            XYData.from_arrays_1d([1.0, 1.1], [1.2, 1.3], np.float64),
            "nitypes.xy_data.XYData(x_data=array([1. , 1.1]), y_data=array([1.2, 1.3]))",
        ),
        (
            XYData.from_arrays_1d([10], [20], np.int32, x_units="volts", y_units="s"),
            f"nitypes.xy_data.XYData(x_data=array([10]{_NDARRAY_DTYPE_INT32}), "
            f"y_data=array([20]{_NDARRAY_DTYPE_INT32}), x_units='volts', y_units='s')",
        ),
        (
            XYData.from_arrays_1d(
                [1.0, 1.1],
                [1.2, 1.3],
                np.float64,
                extended_properties={"NI_ChannelName": "Dev1/ai0"},
            ),
            "nitypes.xy_data.XYData(x_data=array([1. , 1.1]), y_data=array([1.2, 1.3]), "
            "extended_properties=nitypes.waveform.ExtendedPropertyDictionary({'NI_ChannelName': "
            "'Dev1/ai0', 'NI_UnitDescription_X': '', 'NI_UnitDescription_Y': ''}))",
        ),
    ],
)
def test___various_values___repr___looks_ok(value: XYData[Any], expected_repr: str) -> None:
    assert repr(value) == expected_repr


@pytest.mark.parametrize(
    "value, expected_str",
    [
        (
            XYData.from_arrays_1d([], [], np.int32),
            "[[], []]",
        ),
        (
            XYData.from_arrays_1d([], [], np.int32, x_units="volts", y_units="s"),
            "[[], []]",
        ),
        (
            XYData.from_arrays_1d([10, 20], [30, 40], np.int32),
            "[[10, 20], [30, 40]]",
        ),
        (
            XYData.from_arrays_1d([10.0, 20.0], [30.0, 40.0], np.float64),
            "[[10.0, 20.0], [30.0, 40.0]]",
        ),
        (
            XYData.from_arrays_1d([10], [20], np.int32, x_units="volts", y_units="s"),
            "[[10 volts], [20 s]]",
        ),
        (
            XYData.from_arrays_1d([1, 2], [3, 4], np.int32, x_units="miles", y_units="hr"),
            "[[1 miles, 2 miles], [3 hr, 4 hr]]",
        ),
    ],
)
def test___various_values___str___looks_ok(value: XYData[Any], expected_str: str) -> None:
    assert str(value) == expected_str


###############################################################################
# other properties
###############################################################################
def test___xy_data_with_units___get_extended_properties___returns_correct_dictionary() -> None:
    value = XYData.from_arrays_1d([20.0], [40.0], np.float64, x_units="watts", y_units="hr")

    prop_dict = value.extended_properties

    assert isinstance(prop_dict, ExtendedPropertyDictionary)
    assert prop_dict.get(_UNIT_DESCRIPTION_X) == "watts"
    assert prop_dict.get(_UNIT_DESCRIPTION_Y) == "hr"


def test___xy_data_with_units___set_units___units_updated_correctly() -> None:
    value = XYData.from_arrays_1d([20.0], [40.0], np.float64, x_units="watts", y_units="hr")

    value.x_units = "volts"
    value.y_units = "s"

    assert value.x_units == "volts"
    assert value.y_units == "s"


@pytest.mark.parametrize(
    "value",
    [
        XYData.from_arrays_1d([10, 20], [30, 40], np.int32),
        XYData.from_arrays_1d([20.0, 20.1], [20.3, 20.4], np.float64),
        XYData.from_arrays_1d([10, 20], [30, 40], np.int32, x_units="A", y_units="B"),
        XYData.from_arrays_1d([20.0, 20.1], [20.3, 20.4], np.float64, x_units="C", y_units="D"),
        XYData.from_arrays_1d(
            [20.0, 20.1],
            [20.3, 20.4],
            np.float64,
            x_units="C",
            y_units="D",
            extended_properties={"one": 1},
        ),
    ],
)
def test___various_values___copy___makes_copy(value: XYData[TData]) -> None:
    new_value = copy.copy(value)
    assert new_value is not value
    assert new_value == value
    assert new_value.extended_properties == value.extended_properties


@pytest.mark.parametrize(
    "value",
    [
        XYData.from_arrays_1d([10, 20], [30, 40], np.int32),
        XYData.from_arrays_1d([20.0, 20.1], [20.3, 20.4], np.float64),
        XYData.from_arrays_1d([10, 20], [30, 40], np.int32, x_units="A", y_units="B"),
        XYData.from_arrays_1d([20.0, 20.1], [20.3, 20.4], np.float64, x_units="C", y_units="D"),
    ],
)
def test___various_values___pickle_unpickle___makes_copy(value: XYData[TData]) -> None:
    new_value = pickle.loads(pickle.dumps(value))
    assert new_value is not value
    assert new_value == value


def test___xy_data___pickle___references_public_modules() -> None:
    value = XYData.from_arrays_1d([10, 20], [30, 40], np.int32)
    value_bytes = pickle.dumps(value)

    assert b"nitypes.xy_data" in value_bytes
    assert b"nitypes.xy_data._xy_data" not in value_bytes


@pytest.mark.parametrize(
    "pickled_value, expected",
    [
        # nitypes 1.1.0
        (
            b"\x80\x04\x95\xb7\x01\x00\x00\x00\x00\x00\x00\x8c\x08builtins\x94\x8c\x07getattr\x94\x93\x94\x8c\x0fnitypes.xy_data\x94\x8c\x06XYData\x94\x93\x94\x8c\t_unpickle\x94\x86\x94R\x94\x8c\x16numpy._core.multiarray\x94\x8c\x0c_reconstruct\x94\x93\x94\x8c\x05numpy\x94\x8c\x07ndarray\x94\x93\x94K\x00\x85\x94C\x01b\x94\x87\x94R\x94(K\x01K\x02\x85\x94h\x0c\x8c\x05dtype\x94\x93\x94\x8c\x02f8\x94\x89\x88\x87\x94R\x94(K\x03\x8c\x01<\x94NNNJ\xff\xff\xff\xffJ\xff\xff\xff\xffK\x00t\x94b\x89C\x10\x00\x00\x00\x00\x00\x004@\x9a\x99\x99\x99\x99\x194@\x94t\x94bh\x0bh\x0eK\x00\x85\x94h\x10\x87\x94R\x94(K\x01K\x02\x85\x94h\x18\x89C\x10\xcd\xcc\xcc\xcc\xccL4@ffffff4@\x94t\x94b\x86\x94}\x94(\x8c\x13extended_properties\x94\x8c\x10nitypes.waveform\x94\x8c\x1aExtendedPropertyDictionary\x94\x93\x94}\x94(\x8c\x14NI_UnitDescription_X\x94\x8c\x01C\x94\x8c\x14NI_UnitDescription_Y\x94\x8c\x01D\x94u\x85\x94R\x94\x8c\x18copy_extended_properties\x94\x89u\x86\x94R\x94.",
            XYData.from_arrays_1d([20.0, 20.1], [20.3, 20.4], np.float64, x_units="C", y_units="D"),
        ),
    ],
)
def test___pickled_value___unpickle___is_compatible(
    pickled_value: bytes, expected: XYData[Any]
) -> None:
    new_value = pickle.loads(pickled_value)
    assert new_value == expected


def test___various_units_values___change_units___updates_units_correctly() -> None:
    data = XYData.from_arrays_1d([1], [2], np.int32)
    data.x_units = "volts"

    assert data.x_units == "volts"
    assert data.y_units == ""

    data.y_units = "seconds"

    assert data.x_units == "volts"
    assert data.y_units == "seconds"

    data.x_units = ""
    data.y_units = "hours"

    assert data.x_units == ""
    assert data.y_units == "hours"

    data.y_units = ""

    assert data.x_units == data.y_units == ""

    data.y_units = "A"
    data.x_units = "B"

    assert data.x_units == "B"
    assert data.y_units == "A"
````
