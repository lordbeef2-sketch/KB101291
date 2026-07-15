# NI OSS SOURCE SNAPSHOT: nidaqmx-python

<!--NI_OSS_SNAPSHOT repo=ni/nidaqmx-python commit=03282e1b5c741b9f37e4a4e1b5de3a52ae72442e -->

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/task/test_timing_properties.py sha256=dacda1ab296f448b045ced5c6793def7d89c98d9d21cf74d7a16f37ea8ec9eec bytes=19550 -->
## FILE: tests/component/task/test_timing_properties.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/task/test_timing_properties.py`
- sha256: `dacda1ab296f448b045ced5c6793def7d89c98d9d21cf74d7a16f37ea8ec9eec`
- bytes: 19550

````python
from datetime import datetime as std_datetime

import pytest

from nidaqmx import DaqError
from nidaqmx.constants import AcquisitionType, Edge, SampleTimingType
from nidaqmx.error_codes import DAQmxErrors


def test___timing___get_boolean_property___returns_value(task, sim_6363_device):
    task.ao_channels.add_ao_voltage_chan(sim_6363_device.ao_physical_chans[0].name)
    task.timing.samp_timing_type = SampleTimingType.ON_DEMAND

    assert not task.timing.simultaneous_ao_enable


def test___timing___get_boolean_property_with_device_context___throw_daqerror(
    task, sim_6363_device
):
    task.ao_channels.add_ao_voltage_chan(sim_6363_device.ao_physical_chans[0].name)

    with pytest.raises(DaqError) as e:
        task.timing[sim_6363_device].simultaneous_ao_enable

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___set_boolean_property___returns_assigned_value(task, sim_6363_device):
    task.ao_channels.add_ao_voltage_chan(sim_6363_device.ao_physical_chans[0].name)
    task.timing.samp_timing_type = SampleTimingType.ON_DEMAND

    task.timing.simultaneous_ao_enable = True

    assert task.timing.simultaneous_ao_enable


def test___timing___set_boolean_property_with_device_context___throw_daqerror(
    task, sim_6363_device
):
    task.ao_channels.add_ao_voltage_chan(sim_6363_device.ao_physical_chans[0].name)
    task.timing.samp_timing_type = SampleTimingType.ON_DEMAND

    with pytest.raises(DaqError) as e:
        task.timing[sim_6363_device].simultaneous_ao_enable = True

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___reset_boolean_property___returns_default_value(task, sim_6363_device):
    task.ao_channels.add_ao_voltage_chan(sim_6363_device.ao_physical_chans[0].name)
    task.timing.samp_timing_type = SampleTimingType.ON_DEMAND
    task.timing.simultaneous_ao_enable = True

    del task.timing.simultaneous_ao_enable

    assert not task.timing.simultaneous_ao_enable


def test___timing___reset_boolean_property_with_device_context___throw_daqerror(
    task, sim_6363_device
):
    task.ao_channels.add_ao_voltage_chan(sim_6363_device.ao_physical_chans[0].name)
    task.timing.samp_timing_type = SampleTimingType.ON_DEMAND
    task.timing.simultaneous_ao_enable = True

    with pytest.raises(DaqError) as e:
        del task.timing[sim_6363_device].simultaneous_ao_enable

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___get_string_property___returns_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)

    assert task.timing.samp_clk_src == f"/{sim_6363_device.name}/ai/SampleClockTimebase"


def test___timing___get_string_property_with_device_context___throw_daqerror(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)

    with pytest.raises(DaqError) as e:
        _ = task.timing[sim_6363_device].samp_clk_src

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___set_string_property___returns_assigned_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)

    task.timing.samp_clk_src = "PFI0"

    assert task.timing.samp_clk_src == f"/{sim_6363_device.name}/PFI0"


def test___timing___set_string_property_with_device_context___throw_daqerror(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)

    with pytest.raises(DaqError) as e:
        task.timing[sim_6363_device].samp_clk_src = "PFI0"

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___reset_string_property___returns_default_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000, source="PFI0")

    del task.timing.samp_clk_src

    assert task.timing.samp_clk_src == f"/{sim_6363_device.name}/ai/SampleClockTimebase"


def test___timing___reset_string_property_with_device_context___throw_daqerror(
    task, sim_6363_device
):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000, source="PFI0")

    with pytest.raises(DaqError) as e:
        del task.timing[sim_6363_device].samp_clk_src

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___set_invalid_source_terminal_name___throws_daqerror(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)

    task.timing.cfg_samp_clk_timing(1000, source="Test_Invalid_Device_Source")

    with pytest.raises(DaqError) as e:
        _ = task.timing.samp_clk_src
    assert e.value.error_type == DAQmxErrors.INVALID_ROUTING_SOURCE_TERMINAL_NAME_ROUTING


def test___timing___get_enum_property___returns_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.CONTINUOUS)

    assert task.timing.samp_quant_samp_mode == AcquisitionType.CONTINUOUS


def test___timing___get_enum_property_with_device_context___returns_value(task, sim_9205_device):
    task.ai_channels.add_ai_voltage_chan(sim_9205_device.ai_physical_chans[0].name)

    assert task.timing[sim_9205_device].ai_conv_active_edge == Edge.RISING


def test___timing___get_enum_property_with_device_context___throws_daqerror(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.CONTINUOUS)

    with pytest.raises(DaqError) as e:
        _ = task.timing[sim_6363_device].samp_quant_samp_mode

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___set_enum_property___returns_assigned_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.CONTINUOUS)

    task.timing.samp_quant_samp_mode = AcquisitionType.FINITE

    assert task.timing.samp_quant_samp_mode == AcquisitionType.FINITE


def test___timing___set_enum_property_with_device_context___returns_assigned_value(
    task, sim_9205_device
):
    task.ai_channels.add_ai_voltage_chan(sim_9205_device.ai_physical_chans[0].name)

    task.timing[sim_9205_device].ai_conv_active_edge = Edge.FALLING

    assert task.timing[sim_9205_device].ai_conv_active_edge == Edge.FALLING


def test___timing___set_enum_property_with_device_context___throw_daqerror(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.CONTINUOUS)

    with pytest.raises(DaqError) as e:
        task.timing[sim_6363_device].samp_quant_samp_mode = AcquisitionType.FINITE

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___reset_enum_property___returns_default_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.FINITE)

    del task.timing.samp_quant_samp_mode

    assert task.timing.samp_quant_samp_mode == AcquisitionType.CONTINUOUS


def test___timing___reset_enum_property_with_device_context___returns_default_value(
    task, sim_9205_device
):
    task.ai_channels.add_ai_voltage_chan(sim_9205_device.ai_physical_chans[0].name)
    default_value = task.timing[sim_9205_device].ai_conv_active_edge
    task.timing[sim_9205_device].ai_conv_active_edge = Edge.FALLING

    del task.timing[sim_9205_device].ai_conv_active_edge

    assert task.timing[sim_9205_device].ai_conv_active_edge == default_value


def test___timing___reset_enum_property_with_device_context___throws_daqerror(
    task, sim_6363_device
):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.FINITE)

    with pytest.raises(DaqError) as e:
        del task.timing[sim_6363_device].samp_quant_samp_mode

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___get_float64_property___returns_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)

    assert task.timing.samp_clk_rate == 1000


def test___timing___get_float64_property_with_device_context___returns_value(task, sim_9205_device):
    task.ai_channels.add_ai_voltage_chan(sim_9205_device.ai_physical_chans[0].name)

    assert task.timing[sim_9205_device].ai_conv_max_rate == 250000.0


def test___timing___get_float64_property_with_device_context___throws_daqerror(
    task, sim_6363_device
):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)

    with pytest.raises(DaqError) as e:
        _ = task.timing[sim_6363_device].samp_clk_rate

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___set_float64_property___returns_assigned_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)

    task.timing.samp_clk_rate = 2000

    assert task.timing.samp_clk_rate == 2000


def test___timing___set_float64_property_with_device_context___returns_assigned_value(
    task, sim_9205_device
):
    task.ai_channels.add_ai_voltage_chan(sim_9205_device.ai_physical_chans[0].name)
    task.timing[sim_9205_device].ai_conv_rate = 1000.0

    assert task.timing[sim_9205_device].ai_conv_rate == 1000.0


def test___timing___set_float64_property_with_device_context___throws_daqerror(
    task, sim_6363_device
):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)

    with pytest.raises(DaqError) as e:
        task.timing[sim_6363_device].samp_clk_rate = 2000

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___reset_float64_property___returns_default_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    default_value = task.timing.samp_clk_rate
    task.timing.cfg_samp_clk_timing(10000)

    del task.timing.samp_clk_rate

    assert task.timing.samp_clk_rate == default_value


def test___timing___reset_float64_property_with_device_context___returns_default_value(
    task, sim_9205_device
):
    task.ai_channels.add_ai_voltage_chan(sim_9205_device.ai_physical_chans[0].name)
    default_value = task.timing[sim_9205_device].ai_conv_rate
    task.timing[sim_9205_device].ai_conv_rate = 123456.0

    del task.timing[sim_9205_device].ai_conv_rate

    assert task.timing[sim_9205_device].ai_conv_rate == default_value


def test___timing___reset_float64_property_with_device_context___throws_daqerror(
    task, sim_6363_device
):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(10000)

    with pytest.raises(DaqError) as e:
        del task.timing[sim_6363_device].samp_clk_rate

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___get_uint32_property___returns_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)

    assert task.timing.samp_clk_timebase_div == 100000


def test___timing___get_uint32_property_with_device_context___returns_value(task, sim_9205_device):
    task.ai_channels.add_ai_voltage_chan(sim_9205_device.ai_physical_chans[0].name)

    assert task.timing[sim_9205_device].ai_conv_timebase_div == 1121


def test___timing___get_uint32_property_with_device_context___throws_daqerror(
    task, sim_6363_device
):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)

    with pytest.raises(DaqError) as e:
        _ = task.timing[sim_6363_device].samp_clk_timebase_div

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___set_uint32_property___returns_assigned_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)

    task.timing.samp_clk_timebase_div = 500

    assert task.timing.samp_clk_timebase_div == 500


def test___timing___set_uint32_property_with_device_context___returns_assigned_value(
    task, sim_9205_device
):
    task.ai_channels.add_ai_voltage_chan(sim_9205_device.ai_physical_chans[0].name)

    task.timing[sim_9205_device].ai_conv_timebase_div = 1150

    assert task.timing[sim_9205_device].ai_conv_timebase_div == 1150


def test___timing___set_uint32_property_with_device_context___throws_daqerror(
    task, sim_6363_device
):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)

    with pytest.raises(DaqError) as e:
        task.timing[sim_6363_device].samp_clk_timebase_div = 500

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___reset_uint32_property___returns_default_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)
    default_value = task.timing.samp_clk_timebase_div
    task.timing.samp_clk_timebase_div = 200000
    assert task.timing.samp_clk_rate == 500

    del task.timing.samp_clk_timebase_div

    assert task.timing.samp_clk_timebase_div == default_value


def test___timing___reset_uint32_property_with_device_context___returns_default_value(
    task, sim_9205_device
):
    task.ai_channels.add_ai_voltage_chan(sim_9205_device.ai_physical_chans[0].name)
    default_value = task.timing[sim_9205_device].ai_conv_timebase_div
    task.timing[sim_9205_device].ai_conv_timebase_div = 1150

    del task.timing[sim_9205_device].ai_conv_timebase_div

    assert task.timing[sim_9205_device].ai_conv_timebase_div == default_value


def test___timing___reset_uint32_property_with_device_context___throws_daqerror(
    task, sim_6363_device
):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(10000)

    with pytest.raises(DaqError) as e:
        del task.timing[sim_6363_device].samp_clk_timebase_div

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___get_uint64_property___returns_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000, samps_per_chan=100)

    assert task.timing.samp_quant_samp_per_chan == 100


def test___timing___get_uint64_property_with_device_context___throws_daqerror(
    task, sim_6363_device
):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000, samps_per_chan=100)

    with pytest.raises(DaqError) as e:
        _ = task.timing[sim_6363_device].samp_quant_samp_per_chan

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___set_uint64_property___returns_assigned_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)

    task.timing.samp_quant_samp_per_chan = 10000

    assert task.timing.samp_quant_samp_per_chan == 10000


def test___timing___set_uint64_property_with_device_context___throws_daqerror(
    task, sim_6363_device
):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)

    with pytest.raises(DaqError) as e:
        task.timing[sim_6363_device].samp_quant_samp_per_chan = 10000

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___reset_uint64_property___returns_default_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    default_value = task.timing.samp_quant_samp_per_chan
    task.timing.cfg_samp_clk_timing(1000, samps_per_chan=10000)

    del task.timing.samp_quant_samp_per_chan

    assert task.timing.samp_quant_samp_per_chan == default_value


def test___timing___reset_uint64_property_with_device_context___throws_daqerror(
    task, sim_6363_device
):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000, samps_per_chan=10000)

    with pytest.raises(DaqError) as e:
        del task.timing[sim_6363_device].samp_quant_samp_per_chan

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___set_uint64_property_out_of_range_value___throws_daqerror(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)

    task.timing.cfg_samp_clk_timing(1000, samps_per_chan=1)

    with pytest.raises(DaqError) as e:
        _ = task.timing.samp_quant_samp_per_chan
    assert e.value.error_type == DAQmxErrors.INVALID_ATTRIBUTE_VALUE


def test___timing___get_timestamp_property___returns_value(task, sim_9205_device):
    task.ai_channels.add_ai_voltage_chan(sim_9205_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000, samps_per_chan=100)

    task.start()
    timestamp = task.timing.first_samp_timestamp_val

    assert isinstance(timestamp, std_datetime)

    task.stop()


def test___timing___get_timestamp_property_with_device_context___throws_daqerror(
    task, sim_9205_device
):
    task.ai_channels.add_ai_voltage_chan(sim_9205_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000, samps_per_chan=100)
    task.start()

    with pytest.raises(DaqError) as e:
        _ = task.timing[sim_9205_device].first_samp_timestamp_val

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT

    task.stop()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/task/test_triggers.py sha256=b091c51c331cb1a65d0f9f7cfedc52f3cbdab0f88cd86ecbf9e64016d5b37866 bytes=18566 -->
## FILE: tests/component/task/test_triggers.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/task/test_triggers.py`
- sha256: `b091c51c331cb1a65d0f9f7cfedc52f3cbdab0f88cd86ecbf9e64016d5b37866`
- bytes: 18566

````python
from __future__ import annotations

from datetime import timezone

import pytest
from hightime import datetime as ht_datetime, timedelta as ht_timedelta

import nidaqmx
from nidaqmx.constants import (
    DigitalPatternCondition,
    Edge,
    LineGrouping,
    Slope,
    Timescale,
    TimestampEvent,
    TriggerType,
    WindowTriggerCondition1,
)
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.task import Task
from nidaqmx.utils import flatten_channel_string


@pytest.fixture()
def ai_voltage_task(task, sim_time_aware_9215_device) -> Task:
    """Gets AI voltage task."""
    task.ai_channels.add_ai_voltage_chan(sim_time_aware_9215_device.ai_physical_chans[0].name)
    return task


@pytest.fixture()
def ci_count_edges_task(task, sim_9189_device) -> Task:
    chan = task.ci_channels.add_ci_count_edges_chan(f"{sim_9189_device.name}/_ctr0")
    chan.ci_count_edges_term = f"/{sim_9189_device.name}/te0/SampleClock"
    chan.ci_count_edges_active_edge = Edge.RISING
    return task


@pytest.fixture()
def sim_6363_ai_voltage_task(task, sim_6363_device) -> Task:
    """Gets AI voltage task."""
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    return task


@pytest.fixture()
def sim_6535_di_single_line_task(task, sim_6535_device) -> Task:
    """Gets DI task."""
    task.di_channels.add_di_chan(
        sim_6535_device.di_lines[0].name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )
    return task


@pytest.fixture()
def sim_9775_ai_voltage_multi_edge_task(task, sim_9775_device) -> Task:
    """Gets AI voltage multi edge task."""
    task.ai_channels.add_ai_voltage_chan(sim_9775_device.ai_physical_chans[0].name)
    task.ai_channels.add_ai_voltage_chan(sim_9775_device.ai_physical_chans[1].name)
    return task


def test___default_arguments___cfg_time_start_trig___no_errors(
    ai_voltage_task: Task,
):
    ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    utc_dt = ht_datetime.now(timezone.utc)  # UTC time
    dt_now = utc_dt.astimezone()  # local time
    trigger_time = dt_now + ht_timedelta(seconds=10)

    ai_voltage_task.triggers.start_trigger.cfg_time_start_trig(trigger_time)

    when_value = ai_voltage_task.triggers.start_trigger.time_when
    timescale_value = ai_voltage_task.triggers.start_trigger.timestamp_timescale
    assert timescale_value == Timescale.USE_HOST
    assert when_value.year == trigger_time.year
    assert when_value.month == trigger_time.month
    assert when_value.day == trigger_time.day
    assert when_value.hour == trigger_time.hour
    assert when_value.minute == trigger_time.minute
    assert when_value.second == trigger_time.second


@pytest.mark.parametrize("timescale", [Timescale.USE_HOST, Timescale.USE_IO_DEVICE])
def test___arguments_provided___cfg_time_start_trig___no_errors(
    ai_voltage_task: Task,
    timescale: Timescale,
):
    ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    utc_dt = ht_datetime.now(timezone.utc)  # UTC time
    dt_now = utc_dt.astimezone()  # local time
    trigger_time = dt_now + ht_timedelta(seconds=10)

    ai_voltage_task.triggers.start_trigger.cfg_time_start_trig(trigger_time, timescale)

    when_value = ai_voltage_task.triggers.start_trigger.time_when
    assert when_value.year == trigger_time.year
    assert when_value.month == trigger_time.month
    assert when_value.day == trigger_time.day
    assert when_value.hour == trigger_time.hour
    assert when_value.minute == trigger_time.minute
    assert when_value.second == trigger_time.second
    assert ai_voltage_task.triggers.start_trigger.time_timescale == timescale


def test___start_trigger___wait_for_valid_timestamp___no_errors(
    ai_voltage_task: Task,
):
    ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    ai_voltage_task.triggers.start_trigger.timestamp_enable = True
    ai_voltage_task.start()

    timestamp = ai_voltage_task.wait_for_valid_timestamp(TimestampEvent.START_TRIGGER)

    assert isinstance(timestamp, ht_datetime)


def test___reference_trigger___wait_for_valid_timestamp___no_errors(
    ai_voltage_task: Task,
):
    ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    ai_voltage_task.triggers.reference_trigger.timestamp_enable = True
    ai_voltage_task.start()

    timestamp = ai_voltage_task.wait_for_valid_timestamp(TimestampEvent.REFERENCE_TRIGGER)

    assert isinstance(timestamp, ht_datetime)


def test___arm_start_trigger___wait_for_valid_timestamp___no_errors(
    ci_count_edges_task: Task,
):
    ci_count_edges_task.timing.cfg_samp_clk_timing(1000, source="PFI0")
    ci_count_edges_task.triggers.arm_start_trigger.trig_type = TriggerType.TIME
    ci_count_edges_task.triggers.arm_start_trigger.timestamp_enable = True
    ci_count_edges_task.start()

    timestamp = ci_count_edges_task.wait_for_valid_timestamp(TimestampEvent.ARM_START_TRIGGER)

    assert isinstance(timestamp, ht_datetime)


def test___first_sample_trigger___wait_for_valid_timestamp___no_errors(
    ai_voltage_task: Task,
):
    ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    ai_voltage_task.start()

    timestamp = ai_voltage_task.wait_for_valid_timestamp(TimestampEvent.FIRST_SAMPLE)

    assert isinstance(timestamp, ht_datetime)
    assert ai_voltage_task.timing.first_samp_timestamp_enable
    assert ai_voltage_task.timing.first_samp_timestamp_timescale == Timescale.USE_HOST


def test___timestamp_not_enabled___wait_for_valid_timestamp___throw_error(
    ai_voltage_task: Task,
):
    ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    ai_voltage_task.triggers.start_trigger.timestamp_enable = False
    ai_voltage_task.start()

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        ai_voltage_task.wait_for_valid_timestamp(TimestampEvent.START_TRIGGER)

    assert exc_info.value.error_code == DAQmxErrors.TIMESTAMP_NOT_ENABLED


@pytest.mark.parametrize(
    "trig_src, trig_slope, trig_level",
    [
        ("APFI0", Slope.RISING, 2.0),
        ("APFI0", Slope.FALLING, 3.0),
        ("APFI1", Slope.FALLING, -2.0),
        ("APFI1", Slope.RISING, -3.0),
    ],
)
def test___start_trigger___cfg_anlg_edge_start_trig___no_errors(
    sim_6363_ai_voltage_task: Task,
    trig_src: str,
    trig_slope: Slope,
    trig_level: float,
):
    device_name = sim_6363_ai_voltage_task.devices[0].name

    sim_6363_ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    sim_6363_ai_voltage_task.triggers.start_trigger.cfg_anlg_edge_start_trig(
        trigger_source=trig_src, trigger_slope=trig_slope, trigger_level=trig_level
    )

    assert (
        sim_6363_ai_voltage_task.triggers.start_trigger.anlg_edge_src
        == f"/{device_name}/{trig_src}"
    )
    assert sim_6363_ai_voltage_task.triggers.start_trigger.anlg_edge_slope == trig_slope
    assert sim_6363_ai_voltage_task.triggers.start_trigger.anlg_edge_lvl == pytest.approx(
        trig_level, abs=0.001
    )


@pytest.mark.parametrize(
    "window_top, window_bottom, trig_src, trig_when",
    [
        (8.456, 3.9, "APFI0", WindowTriggerCondition1.ENTERING_WINDOW),
        (8.456, 3.9, "APFI1", WindowTriggerCondition1.LEAVING_WINDOW),
    ],
)
def test___start_trigger___cfg_anlg_window_start_trig___no_errors(
    sim_6363_ai_voltage_task: Task,
    window_top: float,
    window_bottom: float,
    trig_src: str,
    trig_when: int,
):
    device_name = sim_6363_ai_voltage_task.devices[0].name

    sim_6363_ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    sim_6363_ai_voltage_task.triggers.start_trigger.cfg_anlg_window_start_trig(
        window_top=window_top,
        window_bottom=window_bottom,
        trigger_source=trig_src,
        trigger_when=trig_when,
    )

    assert (
        sim_6363_ai_voltage_task.triggers.start_trigger.anlg_win_src == f"/{device_name}/{trig_src}"
    )
    assert sim_6363_ai_voltage_task.triggers.start_trigger.anlg_win_top == pytest.approx(
        window_top, abs=0.001
    )
    assert sim_6363_ai_voltage_task.triggers.start_trigger.anlg_win_btm == pytest.approx(
        window_bottom, abs=0.001
    )
    assert sim_6363_ai_voltage_task.triggers.start_trigger.anlg_win_trig_when == trig_when


def test___start_trigger___disable___no_errors(
    sim_6363_ai_voltage_task: Task,
):
    sim_6363_ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    sim_6363_ai_voltage_task.triggers.start_trigger.disable_start_trig()

    assert sim_6363_ai_voltage_task.triggers.start_trigger.trig_type == TriggerType.NONE


def test___reference_trigger___disable___no_errors(
    sim_6363_ai_voltage_task: Task,
):
    sim_6363_ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    sim_6363_ai_voltage_task.triggers.reference_trigger.disable_ref_trig()

    assert sim_6363_ai_voltage_task.triggers.reference_trigger.trig_type == TriggerType.NONE


@pytest.mark.parametrize(
    "window_top, window_bottom, pretrigger_samples, trig_src, trig_when",
    [
        (8.456, 3.9, 6, "APFI0", WindowTriggerCondition1.ENTERING_WINDOW),
        (8.456, 3.9, 6, "APFI1", WindowTriggerCondition1.LEAVING_WINDOW),
    ],
)
def test___reference_trigger___cfg_anlg_window_ref_trig___no_errors(
    sim_6363_ai_voltage_task: Task,
    window_top: float,
    window_bottom: float,
    pretrigger_samples: int,
    trig_src: str,
    trig_when: int,
):
    device_name = sim_6363_ai_voltage_task.devices[0].name

    sim_6363_ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    sim_6363_ai_voltage_task.triggers.reference_trigger.cfg_anlg_window_ref_trig(
        window_top=window_top,
        window_bottom=window_bottom,
        pretrigger_samples=pretrigger_samples,
        trigger_source=trig_src,
        trigger_when=trig_when,
    )

    assert (
        sim_6363_ai_voltage_task.triggers.reference_trigger.anlg_win_src
        == f"/{device_name}/{trig_src}"
    )
    assert sim_6363_ai_voltage_task.triggers.reference_trigger.anlg_win_top == pytest.approx(
        window_top, abs=0.001
    )
    assert sim_6363_ai_voltage_task.triggers.reference_trigger.anlg_win_btm == pytest.approx(
        window_bottom, abs=0.001
    )
    assert sim_6363_ai_voltage_task.triggers.reference_trigger.pretrig_samples == pretrigger_samples
    assert sim_6363_ai_voltage_task.triggers.reference_trigger.anlg_win_trig_when == trig_when


@pytest.mark.parametrize(
    "trig_slopes, trig_levels",
    [
        ([Slope.RISING, Slope.RISING], [2.0, 2.0]),
        ([Slope.FALLING, Slope.FALLING], [3.0, 3.0]),
        ([Slope.FALLING, Slope.FALLING], [-2.0, -2.0]),
        ([Slope.RISING, Slope.RISING], [-3.0, -3.0]),
    ],
)
def test___start_trigger___cfg_anlg_multi_edge_start_trig___no_errors(
    sim_9775_ai_voltage_multi_edge_task: Task,
    trig_slopes: list[Slope],
    trig_levels: list[float],
):
    trigger_sources = ["cdaqTesterMod3/ai0", "cdaqTesterMod3/ai1"]
    flatten_trigger_sources = flatten_channel_string([s for s in trigger_sources])

    sim_9775_ai_voltage_multi_edge_task.timing.cfg_samp_clk_timing(1000)
    sim_9775_ai_voltage_multi_edge_task.triggers.start_trigger.cfg_anlg_multi_edge_start_trig(
        trigger_sources=flatten_trigger_sources,
        trigger_slope_array=trig_slopes,
        trigger_level_array=trig_levels,
    )

    # AB#2698564 - For now we are accepting either format of the trigger sources
    assert sim_9775_ai_voltage_multi_edge_task.triggers.start_trigger.anlg_multi_edge_srcs in [
        ", ".join(trigger_sources),
        flatten_trigger_sources,
    ]
    assert (
        sim_9775_ai_voltage_multi_edge_task.triggers.start_trigger.anlg_multi_edge_slopes
        == trig_slopes
    )
    assert (
        sim_9775_ai_voltage_multi_edge_task.triggers.start_trigger.anlg_multi_edge_lvls
        == pytest.approx(trig_levels, abs=0.001)
    )


@pytest.mark.parametrize(
    "trig_src, trig_pattern, trig_when",
    [
        ("port1/line2, port1/line4", "1R", DigitalPatternCondition.PATTERN_MATCHES),
        (
            "port1/line2, port1/line3, port1/line4",
            "0EF",
            DigitalPatternCondition.PATTERN_DOES_NOT_MATCH,
        ),
    ],
)
def test___start_trigger__cfg_dig_pattern_start_trig___no_errors(
    sim_6535_di_single_line_task: Task,
    trig_src: str,
    trig_pattern: str,
    trig_when: int,
):
    sim_6535_di_single_line_task.timing.cfg_samp_clk_timing(1000)
    sim_6535_di_single_line_task.triggers.start_trigger.cfg_dig_pattern_start_trig(
        trigger_source=trig_src,
        trigger_pattern=trig_pattern,
        trigger_when=trig_when,
    )

    assert sim_6535_di_single_line_task.triggers.start_trigger.dig_pattern_src.name == f"{trig_src}"
    assert sim_6535_di_single_line_task.triggers.start_trigger.dig_pattern_pattern == trig_pattern
    assert sim_6535_di_single_line_task.triggers.start_trigger.dig_pattern_trig_when == trig_when


@pytest.mark.parametrize(
    "trig_src, pretrig_samples, trig_slope, trig_level",
    [
        ("APFI0", 10, Slope.RISING, 2.0),
        ("APFI0", 20, Slope.FALLING, 3.0),
        ("APFI1", 30, Slope.FALLING, -2.0),
        ("APFI1", 40, Slope.RISING, -3.0),
    ],
)
def test___reference_trigger___cfg_anlg_edge_ref_trig___no_errors(
    sim_6363_ai_voltage_task: Task,
    trig_src: str,
    pretrig_samples: int,
    trig_slope: Slope,
    trig_level: float,
):
    device_name = sim_6363_ai_voltage_task.devices[0].name

    sim_6363_ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    sim_6363_ai_voltage_task.triggers.reference_trigger.cfg_anlg_edge_ref_trig(
        trigger_source=trig_src,
        pretrigger_samples=pretrig_samples,
        trigger_slope=trig_slope,
        trigger_level=trig_level,
    )

    assert (
        sim_6363_ai_voltage_task.triggers.reference_trigger.anlg_edge_src
        == f"/{device_name}/{trig_src}"
    )
    assert sim_6363_ai_voltage_task.triggers.reference_trigger.pretrig_samples == pretrig_samples
    assert sim_6363_ai_voltage_task.triggers.reference_trigger.anlg_edge_slope == trig_slope
    assert sim_6363_ai_voltage_task.triggers.reference_trigger.anlg_edge_lvl == pytest.approx(
        trig_level, abs=0.001
    )


@pytest.mark.parametrize(
    "pretrig_samples, trig_slopes, trig_levels",
    [
        (10, [Slope.RISING, Slope.RISING], [2.0, 2.0]),
        (20, [Slope.FALLING, Slope.FALLING], [3.0, 3.0]),
        (30, [Slope.FALLING, Slope.FALLING], [-2.0, -2.0]),
        (40, [Slope.RISING, Slope.RISING], [-3.0, -3.0]),
    ],
)
def test___reference_trigger___cfg_anlg_multi_edge_ref_trig___no_errors(
    sim_9775_ai_voltage_multi_edge_task: Task,
    pretrig_samples: int,
    trig_slopes: list[Slope],
    trig_levels: list[float],
):
    trigger_sources = ["cdaqTesterMod3/ai0", "cdaqTesterMod3/ai1"]
    flatten_trigger_sources = flatten_channel_string([s for s in trigger_sources])

    sim_9775_ai_voltage_multi_edge_task.timing.cfg_samp_clk_timing(1000)
    sim_9775_ai_voltage_multi_edge_task.triggers.reference_trigger.cfg_anlg_multi_edge_ref_trig(
        trigger_sources=flatten_trigger_sources,
        pretrigger_samples=pretrig_samples,
        trigger_slope_array=trig_slopes,
        trigger_level_array=trig_levels,
    )

    # AB#2698564 - For now we are accepting either format of the trigger sources
    assert sim_9775_ai_voltage_multi_edge_task.triggers.reference_trigger.anlg_multi_edge_srcs in [
        ", ".join(trigger_sources),
        flatten_trigger_sources,
    ]
    assert (
        sim_9775_ai_voltage_multi_edge_task.triggers.reference_trigger.pretrig_samples
        == pretrig_samples
    )
    assert (
        sim_9775_ai_voltage_multi_edge_task.triggers.reference_trigger.anlg_multi_edge_slopes
        == trig_slopes
    )
    assert (
        sim_9775_ai_voltage_multi_edge_task.triggers.reference_trigger.anlg_multi_edge_lvls
        == pytest.approx(trig_levels, abs=0.001)
    )


@pytest.mark.parametrize(
    "trig_src, pretrig_samples, trig_edge",
    [
        ("APFI0", 10, Edge.RISING),
        ("APFI1", 20, Edge.FALLING),
    ],
)
def test___reference_trigger___cfg_dig_edge_ref_trig___no_errors(
    sim_6363_ai_voltage_task: Task,
    trig_src: str,
    pretrig_samples: int,
    trig_edge: Edge,
):
    device_name = sim_6363_ai_voltage_task.devices[0].name

    sim_6363_ai_voltage_task.timing.cfg_samp_clk_timing(1000)
    sim_6363_ai_voltage_task.triggers.reference_trigger.cfg_dig_edge_ref_trig(
        trigger_source=trig_src,
        pretrigger_samples=pretrig_samples,
        trigger_edge=trig_edge,
    )

    assert (
        sim_6363_ai_voltage_task.triggers.reference_trigger.dig_edge_src
        == f"/{device_name}/{trig_src}"
    )
    assert sim_6363_ai_voltage_task.triggers.reference_trigger.pretrig_samples == pretrig_samples
    assert sim_6363_ai_voltage_task.triggers.reference_trigger.dig_edge_edge == trig_edge


@pytest.mark.parametrize(
    "trig_src, trig_pattern, pretrig_samples, trig_when",
    [
        ("port1/line2, port1/line4", "1E", 10, DigitalPatternCondition.PATTERN_MATCHES),
        (
            "port1/line2, port1/line3, port1/line4",
            "0RF",
            20,
            DigitalPatternCondition.PATTERN_DOES_NOT_MATCH,
        ),
    ],
)
def test___reference_trigger__cfg_dig_pattern_ref_trig___no_errors(
    sim_6535_di_single_line_task: Task,
    trig_src: str,
    trig_pattern: str,
    pretrig_samples: int,
    trig_when: int,
):
    sim_6535_di_single_line_task.timing.cfg_samp_clk_timing(1000)
    sim_6535_di_single_line_task.triggers.reference_trigger.cfg_dig_pattern_ref_trig(
        trigger_source=trig_src,
        trigger_pattern=trig_pattern,
        pretrigger_samples=pretrig_samples,
        trigger_when=trig_when,
    )

    assert (
        sim_6535_di_single_line_task.triggers.reference_trigger.dig_pattern_src.name
        == f"{trig_src}"
    )
    assert (
        sim_6535_di_single_line_task.triggers.reference_trigger.dig_pattern_pattern == trig_pattern
    )
    assert (
        sim_6535_di_single_line_task.triggers.reference_trigger.pretrig_samples == pretrig_samples
    )
    assert (
        sim_6535_di_single_line_task.triggers.reference_trigger.dig_pattern_trig_when == trig_when
    )
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/task/test_triggers_properties.py sha256=7a8603dfed118b59004b22a147a11c4a59c61f71eae25494d8943f0752ead60a bytes=8362 -->
## FILE: tests/component/task/test_triggers_properties.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/task/test_triggers_properties.py`
- sha256: `7a8603dfed118b59004b22a147a11c4a59c61f71eae25494d8943f0752ead60a`
- bytes: 8362

````python
import pytest

from nidaqmx._time import _convert_to_desired_timezone
from nidaqmx.constants import TaskMode, TriggerType
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError
from nidaqmx.task import Task
from tests.unit._time_utils import JAN_01_1904_HIGHTIME, JAN_01_2002_HIGHTIME


@pytest.fixture()
def ai_voltage_task(task, sim_6363_device):
    """Gets AI voltage task."""
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    yield task


@pytest.fixture()
def ai_voltage_time_aware_task(task, sim_time_aware_9215_device):
    """Gets AI voltage task."""
    task.ai_channels.add_ai_voltage_chan(sim_time_aware_9215_device.ai_physical_chans[0].name)
    yield task


def test___ai_task___get_float_property___returns_default_value(ai_voltage_task: Task):
    assert ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate == 0.0


def test___ai_task___set_float_property___returns_assigned_value(ai_voltage_task: Task):
    value_to_test = 2.505
    ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate = value_to_test

    assert ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate == value_to_test


def test___ai_task___reset_float_property___returns_default_value(ai_voltage_task: Task):
    ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate = 1.2

    del ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate

    assert ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_rate == 0.0


def test___ai_task___get_string_property___returns_default_value(ai_voltage_task: Task):
    assert ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src == ""


def test___ai_task___set_string_property___returns_assigned_value(ai_voltage_task: Task):
    value_to_test = "Test Value for Digital Edge Digital Filter Timebase Source"
    ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src = value_to_test

    assert ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src == value_to_test


def test___ai_task___reset_string_property___returns_default_value(ai_voltage_task: Task):
    ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src = "PFI3"

    del ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src

    assert ai_voltage_task.triggers.start_trigger.dig_edge_dig_fltr_timebase_src == ""


def test___ai_task___get_enum_property___returns_default_value(ai_voltage_task: Task):
    assert ai_voltage_task.triggers.start_trigger.trig_type == TriggerType.NONE


def test___ai_task_without_cfg_samp_clk___set_trig_type___throws_daqerror(ai_voltage_task: Task):
    value_to_test = TriggerType.ANALOG_EDGE

    ai_voltage_task.triggers.start_trigger.trig_type = value_to_test
    with pytest.raises(DaqError) as exc_info:
        ai_voltage_task.control(TaskMode.TASK_VERIFY)

    assert exc_info.value.error_type == DAQmxErrors.TRIG_WHEN_ON_DEMAND_SAMP_TIMING


def test___ai_task___set_enum_property___returns_assigned_value(ai_voltage_task: Task):
    ai_voltage_task.timing.cfg_samp_clk_timing(1000)

    value_to_test = TriggerType.ANALOG_EDGE
    ai_voltage_task.triggers.start_trigger.trig_type = value_to_test

    assert ai_voltage_task.triggers.start_trigger.trig_type == value_to_test


def test___ai_task___reset_enum_property___returns_default_value(ai_voltage_task: Task):
    ai_voltage_task.triggers.start_trigger.trig_type = TriggerType.ANALOG_EDGE

    del ai_voltage_task.triggers.start_trigger.trig_type

    assert ai_voltage_task.triggers.start_trigger.trig_type == TriggerType.NONE


def test___ai_task___get_uint32_property___returns_default_value(ai_voltage_task: Task):
    assert ai_voltage_task.triggers.reference_trigger.pretrig_samples == 2


def test___ai_task___set_uint32_property___returns_assigned_value(ai_voltage_task: Task):
    value_to_test = 54544544
    ai_voltage_task.triggers.reference_trigger.pretrig_samples = value_to_test

    assert ai_voltage_task.triggers.reference_trigger.pretrig_samples == value_to_test


def test___ai_task___reset_uint32_property___returns_default_value(ai_voltage_task: Task):
    ai_voltage_task.triggers.reference_trigger.pretrig_samples = 10

    del ai_voltage_task.triggers.reference_trigger.pretrig_samples

    assert ai_voltage_task.triggers.reference_trigger.pretrig_samples == 2


def test___ai_voltage_time_aware_task___get_timestamp_property___returns_default_value(
    ai_voltage_time_aware_task: Task,
):
    ai_voltage_time_aware_task.timing.cfg_samp_clk_timing(1000)

    when_value = ai_voltage_time_aware_task.triggers.start_trigger.time_when

    localized_default_value = _convert_to_desired_timezone(JAN_01_1904_HIGHTIME)
    assert when_value.year == localized_default_value.year
    assert when_value.month == localized_default_value.month
    assert when_value.day == localized_default_value.day
    assert when_value.hour == localized_default_value.hour
    assert when_value.minute == localized_default_value.minute
    assert when_value.second == localized_default_value.second


def test___ai_voltage_time_aware_task___set_timestamp_property___returns_assigned_value(
    ai_voltage_time_aware_task: Task,
):
    value_to_test = JAN_01_2002_HIGHTIME
    ai_voltage_time_aware_task.timing.cfg_samp_clk_timing(1000)

    ai_voltage_time_aware_task.triggers.start_trigger.time_when = value_to_test

    when_value = ai_voltage_time_aware_task.triggers.start_trigger.time_when
    localized_value_to_test = _convert_to_desired_timezone(value_to_test)
    assert when_value.year == localized_value_to_test.year
    assert when_value.month == localized_value_to_test.month
    assert when_value.day == localized_value_to_test.day
    assert when_value.hour == localized_value_to_test.hour
    assert when_value.minute == localized_value_to_test.minute
    assert when_value.second == localized_value_to_test.second


def test___ai_voltage_time_aware_task___reset_timestamp_property___returns_default_value(
    ai_voltage_time_aware_task: Task,
):
    ai_voltage_time_aware_task.timing.cfg_samp_clk_timing(1000)
    ai_voltage_time_aware_task.triggers.start_trigger.time_when = JAN_01_2002_HIGHTIME

    del ai_voltage_time_aware_task.triggers.start_trigger.time_when

    when_value = ai_voltage_time_aware_task.triggers.start_trigger.time_when
    localized_default_value = _convert_to_desired_timezone(JAN_01_1904_HIGHTIME)
    assert when_value.year == localized_default_value.year
    assert when_value.month == localized_default_value.month
    assert when_value.day == localized_default_value.day
    assert when_value.hour == localized_default_value.hour
    assert when_value.minute == localized_default_value.minute
    assert when_value.second == localized_default_value.second


def test___trigger___set_nonexistent_property___raises_exception(task: Task):
    with pytest.raises(AttributeError):
        task.triggers.nonexistent_property = "foo"  # type: ignore[attr-defined]


def test___arm_start_trigger___set_nonexistent_property___raises_exception(task: Task):
    with pytest.raises(AttributeError):
        task.triggers.arm_start_trigger.nonexistent_property = "foo"  # type: ignore[attr-defined]


def test___handshake_trigger___set_nonexistent_property___raises_exception(task: Task):
    with pytest.raises(AttributeError):
        task.triggers.handshake_trigger.nonexistent_property = "foo"  # type: ignore[attr-defined]


def test___pause_trigger___set_nonexistent_property___raises_exception(task: Task):
    with pytest.raises(AttributeError):
        task.triggers.pause_trigger.nonexistent_property = "foo"  # type: ignore[attr-defined]


def test___reference_trigger___set_nonexistent_property___raises_exception(task: Task):
    with pytest.raises(AttributeError):
        task.triggers.reference_trigger.nonexistent_property = "foo"  # type: ignore[attr-defined]


def test___start_trigger___set_nonexistent_property___raises_exception(task: Task):
    with pytest.raises(AttributeError):
        task.triggers.start_trigger.nonexistent_property = "foo"  # type: ignore[attr-defined]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/test_export_signals.py sha256=2ca35a24ad04a991f9d88f43b4f2738b7dc224dc532ec614d0439ce4dd2c4fa4 bytes=260 -->
## FILE: tests/component/test_export_signals.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/test_export_signals.py`
- sha256: `2ca35a24ad04a991f9d88f43b4f2738b7dc224dc532ec614d0439ce4dd2c4fa4`
- bytes: 260

````python
import pytest

import nidaqmx


def test___export_signals___set_nonexistent_property___raises_exception(task: nidaqmx.Task):
    with pytest.raises(AttributeError):
        task.export_signals.nonexistent_property = "foo"  # type: ignore[attr-defined]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/test_interpreter.py sha256=6cccf68c36fc02486954c7fea0b9c51ef9b75a58383955713a86a7d6ec02794e bytes=1737 -->
## FILE: tests/component/test_interpreter.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/test_interpreter.py`
- sha256: `6cccf68c36fc02486954c7fea0b9c51ef9b75a58383955713a86a7d6ec02794e`
- bytes: 1737

````python
import pytest

from nidaqmx._base_interpreter import BaseInterpreter
from nidaqmx.error_codes import DAQmxErrors

try:
    from nidaqmx._grpc_interpreter import _ERROR_MESSAGES
except ImportError:
    _ERROR_MESSAGES = {}


def test___known_error_code___get_error_string___returns_known_error_message(
    interpreter: BaseInterpreter,
) -> None:
    error_message = interpreter.get_error_string(DAQmxErrors.INVALID_ATTRIBUTE_VALUE)

    assert error_message.startswith("Requested value is not a supported value for this property.")


def test___unknown_error_code___get_error_string___returns_unable_to_locate_error_resources(
    interpreter: BaseInterpreter,
) -> None:
    error_message = interpreter.get_error_string(-12345)

    assert error_message.startswith("Error code could not be found.")


@pytest.mark.grpc_only(reason="Tests gRPC-specific error case")
@pytest.mark.temporary_grpc_channel(options=[("grpc.max_send_message_length", 1)])
def test___grpc_channel_with_errors___get_error_string___returns_failed_to_retrieve_error_description(
    interpreter: BaseInterpreter,
) -> None:
    error_message = interpreter.get_error_string(DAQmxErrors.INVALID_ATTRIBUTE_VALUE)

    assert error_message.startswith("Failed to retrieve error description.")


@pytest.mark.grpc_only(reason="Tests gRPC-specific error message lookup")
@pytest.mark.parametrize("error_code", list(_ERROR_MESSAGES))
def test___error_code_with_hardcoded_error_message___get_error_string___returns_hardcoded_error_message(
    interpreter: BaseInterpreter, error_code: DAQmxErrors
) -> None:
    error_message = interpreter.get_error_string(error_code)

    assert error_message == _ERROR_MESSAGES[error_code]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/test_scale.py sha256=d2908b26e650655f17860e68b9f7ed8c6cf4fd00e821dcc8a527b7dbe5e10c5a bytes=685 -->
## FILE: tests/component/test_scale.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/test_scale.py`
- sha256: `d2908b26e650655f17860e68b9f7ed8c6cf4fd00e821dcc8a527b7dbe5e10c5a`
- bytes: 685

````python
import pytest

import nidaqmx


def test___polynomial___calculate_reverse_poly_coeff___returns_reverse_coeff(init_kwargs):
    # The given values represents the polynomial y = 2x + 1
    forward_coeff = [1.0, 2.0]
    min_val_x = -10.0
    max_val_x = 10.0
    num_of_points_to_compute = 1000
    reverse_polynomial_order = 1

    reverse_coeff = nidaqmx.Scale.calculate_reverse_poly_coeff(
        forward_coeff,
        min_val_x,
        max_val_x,
        num_of_points_to_compute,
        reverse_polynomial_order,
        **init_kwargs
    )

    # The expected inverted polynomial is 0.5y - 0.5 = x
    assert reverse_coeff == pytest.approx([-0.5, 0.5])
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/test_scale_properties.py sha256=171569ec786cebd955af97408eaf10829f514e4e47d47924690ca69b8c8a6f9b bytes=2919 -->
## FILE: tests/component/test_scale_properties.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/test_scale_properties.py`
- sha256: `171569ec786cebd955af97408eaf10829f514e4e47d47924690ca69b8c8a6f9b`
- bytes: 2919

````python
import pytest

from nidaqmx.constants import UnitsPreScaled
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError
from nidaqmx.scale import Scale

# Do not modify persisted scale properties in this test. Persisted scales are
# cached for the lifetime of the process, so modifying persisted scale
# properties will affect other tests that use the same scale.


def test___scale___get_float64_property___returns_assigned_value(init_kwargs):
    scale = Scale.create_lin_scale("custom_linear_scale", 2, **init_kwargs)

    assert scale.lin_slope == 2.0


def test___scale___set_float64_property___returns_assigned_value(init_kwargs):
    scale = Scale.create_lin_scale("custom_linear_scale", 2, **init_kwargs)

    scale.lin_slope = 5

    assert scale.lin_slope == 5.0


def test___scale___get_float64_list_property___returns_assigned_value(init_kwargs):
    scale = Scale.create_polynomial_scale("custom_polynomial_scale", [0, 1], [0, 1], **init_kwargs)

    assert scale.poly_forward_coeff == [0.0, 1.0]


def test___scale___set_float64_list_property___returns_assigned_value(init_kwargs):
    scale = Scale.create_polynomial_scale("custom_polynomial_scale", [0, 1], [0, 1], **init_kwargs)

    coeff_list = [1.0, 2.0]
    scale.poly_forward_coeff = coeff_list

    assert scale.poly_forward_coeff == coeff_list


def test___linear_scale___get_poly_scale_property___throws_daqerror(init_kwargs):
    linear_scale = Scale.create_lin_scale("custom_linear_scale", 1, **init_kwargs)

    with pytest.raises(DaqError) as exc_info:
        _ = linear_scale.poly_forward_coeff

    assert exc_info.value.error_type == DAQmxErrors.PROPERTY_NOT_SUPPORTED_FOR_SCALE_TYPE


def test___scale___get_enum_property___returns_assigned_value(init_kwargs):
    scale = Scale.create_lin_scale(
        "custom_linear_scale",
        1,
        y_intercept=1,
        pre_scaled_units=UnitsPreScaled.VOLTS,
        **init_kwargs
    )

    assert scale.pre_scaled_units == UnitsPreScaled.VOLTS


def test___scale___set_enum_property___returns_assigned_value(init_kwargs):
    scale = Scale.create_lin_scale(
        "custom_linear_scale",
        1,
        y_intercept=1,
        pre_scaled_units=UnitsPreScaled.VOLTS,
        **init_kwargs
    )

    scale.pre_scaled_units = UnitsPreScaled.AMPS

    assert scale.pre_scaled_units == UnitsPreScaled.AMPS


def test___scale___get_string_property___returns_assigned_value(init_kwargs):
    scale = Scale.create_lin_scale("custom_linear_scale", 1, scaled_units="AMPS", **init_kwargs)

    assert scale.scaled_units == "AMPS"


def test___scale___set_string_property___returns_assigned_value(init_kwargs):
    scale = Scale.create_lin_scale("custom_linear_scale", 1, scaled_units="AMPS", **init_kwargs)

    scale.scaled_units = "OHMS"

    assert scale.scaled_units == "OHMS"
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/test_stream_readers_ci.py sha256=581a0db5586e163dea8323bafe45bf520ab44c353268ebb5b6c035d14a4d1d95 bytes=13426 -->
## FILE: tests/component/test_stream_readers_ci.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/test_stream_readers_ci.py`
- sha256: `581a0db5586e163dea8323bafe45bf520ab44c353268ebb5b6c035d14a4d1d95`
- bytes: 13426

````python
from __future__ import annotations

import ctypes
import math

import numpy
import numpy.typing
import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.stream_readers import CounterReader

SIGNAL_TO_MEASURE = "100kHzTimebase"
EXPECTED_FREQUENCY = 100000.0
EXPECTED_FREQUENCY_TOLERANCE = 1e-6
EXPECTED_DUTY_CYCLE = 0.5
EXPECTED_DUTY_CYCLE_TOLERANCE = 1e-6
EXPECTED_HIGH_TIME = 1.0 / EXPECTED_FREQUENCY * EXPECTED_DUTY_CYCLE
EXPECTED_LOW_TIME = 1.0 / EXPECTED_FREQUENCY * (1.0 - EXPECTED_DUTY_CYCLE)
EXPECTED_TIME_TOLERANCE = 1e-6
EXPECTED_HIGH_TICKS = int(100e6 / EXPECTED_FREQUENCY * EXPECTED_DUTY_CYCLE)
EXPECTED_LOW_TICKS = int(100e6 / EXPECTED_FREQUENCY * (1.0 - EXPECTED_DUTY_CYCLE))
EXPECTED_TICKS_TOLERANCE = 1


def _validate_count_edges_data(data: numpy.typing.NDArray[numpy.uint32]) -> None:
    # When counting a fast timebase, we can expect the data to be ever-increasing as long as the
    # test time is less than the rollover time, ~42s for the 100MHz timebase.
    last = 0
    for datum in data:
        assert datum >= last


def _validate_frequency_data(data: numpy.typing.NDArray[numpy.float64]) -> None:
    assert data == pytest.approx(EXPECTED_FREQUENCY, abs=EXPECTED_FREQUENCY_TOLERANCE)


def _validate_pulse_frequency_data(
    frequency_data: numpy.typing.NDArray[numpy.float64],
    duty_cycle_data: numpy.typing.NDArray[numpy.float64],
) -> None:
    assert frequency_data == pytest.approx(EXPECTED_FREQUENCY, abs=EXPECTED_FREQUENCY_TOLERANCE)
    assert duty_cycle_data == pytest.approx(EXPECTED_DUTY_CYCLE, abs=EXPECTED_DUTY_CYCLE_TOLERANCE)


def _validate_pulse_time_data(
    high_time_data: numpy.typing.NDArray[numpy.float64],
    low_time_data: numpy.typing.NDArray[numpy.float64],
) -> None:
    assert high_time_data == pytest.approx(EXPECTED_HIGH_TIME, abs=EXPECTED_TIME_TOLERANCE)
    assert low_time_data == pytest.approx(EXPECTED_LOW_TIME, abs=EXPECTED_TIME_TOLERANCE)


def _validate_pulse_tick_data(
    high_tick_data: numpy.typing.NDArray[numpy.uint32],
    low_tick_data: numpy.typing.NDArray[numpy.uint32],
) -> None:
    assert high_tick_data == pytest.approx(EXPECTED_HIGH_TICKS, abs=EXPECTED_TICKS_TOLERANCE)
    assert low_tick_data == pytest.approx(EXPECTED_LOW_TICKS, abs=EXPECTED_TICKS_TOLERANCE)


@pytest.fixture
def ci_count_edges_task(
    task: nidaqmx.Task, real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    chan = task.ci_channels.add_ci_count_edges_chan(
        real_x_series_device.ci_physical_chans[0].name,
    )
    chan.ci_count_edges_term = SIGNAL_TO_MEASURE
    # Start the task to ensure the first sample is non-zero
    task.start()
    return task


@pytest.fixture
def ci_frequency_task(
    task: nidaqmx.Task, real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    chan = task.ci_channels.add_ci_freq_chan(
        real_x_series_device.ci_physical_chans[0].name,
    )
    chan.ci_freq_term = SIGNAL_TO_MEASURE
    return task


@pytest.fixture
def ci_pulse_frequency_task(
    task: nidaqmx.Task, real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    chan = task.ci_channels.add_ci_pulse_chan_freq(
        real_x_series_device.ci_physical_chans[0].name,
    )
    chan.ci_pulse_freq_term = SIGNAL_TO_MEASURE
    return task


@pytest.fixture
def ci_pulse_time_task(
    task: nidaqmx.Task, real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    chan = task.ci_channels.add_ci_pulse_chan_time(
        real_x_series_device.ci_physical_chans[0].name,
    )
    chan.ci_pulse_time_term = SIGNAL_TO_MEASURE
    return task


@pytest.fixture
def ci_pulse_ticks_task(
    task: nidaqmx.Task, real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    chan = task.ci_channels.add_ci_pulse_chan_ticks(
        real_x_series_device.ci_physical_chans[0].name,
    )
    chan.ci_pulse_ticks_term = SIGNAL_TO_MEASURE
    return task


def test___counter_reader___read_one_sample_uint32___returns_valid_samples(
    ci_count_edges_task: nidaqmx.Task,
) -> None:
    reader = CounterReader(ci_count_edges_task.in_stream)
    samples_to_read = 10

    data = numpy.array([reader.read_one_sample_uint32() for _ in range(samples_to_read)])

    _validate_count_edges_data(data)


def test___counter_reader___read_many_sample_uint32___returns_valid_samples(
    ci_count_edges_task: nidaqmx.Task,
) -> None:
    reader = CounterReader(ci_count_edges_task.in_stream)
    samples_to_read = 10
    data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)

    samples_read = reader.read_many_sample_uint32(
        data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    _validate_count_edges_data(data)


def test___counter_reader___read_many_sample_uint32_with_wrong_dtype___raises_error_with_correct_dtype(
    ci_count_edges_task: nidaqmx.Task,
) -> None:
    reader = CounterReader(ci_count_edges_task.in_stream)
    samples_to_read = 10
    data = numpy.full(samples_to_read, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_uint32(data, samples_to_read)

    assert "uint32" in exc_info.value.args[0]


def test___counter_reader___read_one_sample_double___returns_valid_samples(
    ci_frequency_task: nidaqmx.Task,
) -> None:
    reader = CounterReader(ci_frequency_task.in_stream)
    samples_to_read = 10

    data = numpy.array([reader.read_one_sample_double() for _ in range(samples_to_read)])

    _validate_frequency_data(data)


def test___counter_reader___read_many_sample_double___returns_valid_samples(
    ci_frequency_task: nidaqmx.Task,
) -> None:
    reader = CounterReader(ci_frequency_task.in_stream)
    samples_to_read = 10
    data = numpy.full(samples_to_read, numpy.inf, dtype=numpy.float64)

    samples_read = reader.read_many_sample_double(
        data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    _validate_frequency_data(data)


def test___counter_reader___read_many_sample_double_with_wrong_dtype___raises_error_with_correct_dtype(
    ci_frequency_task: nidaqmx.Task,
) -> None:
    reader = CounterReader(ci_frequency_task.in_stream)
    samples_to_read = 10
    data = numpy.full(samples_to_read, math.inf, dtype=numpy.float32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_double(data, samples_to_read)

    assert "float64" in exc_info.value.args[0]


def test___counter_reader___read_one_sample_pulse_frequency___returns_valid_samples(
    ci_pulse_frequency_task: nidaqmx.Task,
) -> None:
    reader = CounterReader(ci_pulse_frequency_task.in_stream)
    samples_to_read = 10

    data = [reader.read_one_sample_pulse_frequency() for _ in range(samples_to_read)]
    frequency_data = numpy.array([datum.freq for datum in data])
    duty_cycle_data = numpy.array([datum.duty_cycle for datum in data])

    _validate_pulse_frequency_data(frequency_data, duty_cycle_data)


def test___counter_reader___read_many_sample_pulse_frequency___returns_valid_samples(
    ci_pulse_frequency_task: nidaqmx.Task,
) -> None:
    reader = CounterReader(ci_pulse_frequency_task.in_stream)
    samples_to_read = 10
    frequency_data = numpy.full(samples_to_read, numpy.inf, dtype=numpy.float64)
    duty_cycle_data = numpy.full(samples_to_read, numpy.inf, dtype=numpy.float64)

    samples_read = reader.read_many_sample_pulse_frequency(
        frequency_data, duty_cycle_data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    _validate_pulse_frequency_data(frequency_data, duty_cycle_data)


@pytest.mark.parametrize(
    "frequency_dtype, duty_cycle_dtype",
    [
        (numpy.float32, numpy.float64),
        (numpy.float64, numpy.float32),
        (numpy.float32, numpy.float32),
    ],
)
def test___counter_reader___read_many_sample_pulse_frequency_with_wrong_dtype___raises_error_with_correct_dtype(
    ci_pulse_frequency_task: nidaqmx.Task, frequency_dtype, duty_cycle_dtype
) -> None:
    reader = CounterReader(ci_pulse_frequency_task.in_stream)
    samples_to_read = 10
    frequency_data = numpy.full(samples_to_read, math.inf, dtype=frequency_dtype)
    duty_cycle_data = numpy.full(samples_to_read, math.inf, dtype=duty_cycle_dtype)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_pulse_frequency(
            frequency_data, duty_cycle_data, number_of_samples_per_channel=samples_to_read
        )

    assert "float64" in exc_info.value.args[0]


def test___counter_reader___read_one_sample_pulse_time___returns_valid_samples(
    ci_pulse_time_task: nidaqmx.Task,
) -> None:
    reader = CounterReader(ci_pulse_time_task.in_stream)
    samples_to_read = 10

    data = [reader.read_one_sample_pulse_time() for _ in range(samples_to_read)]
    high_time_data = numpy.array([datum.high_time for datum in data])
    low_time_data = numpy.array([datum.low_time for datum in data])

    _validate_pulse_time_data(high_time_data, low_time_data)


def test___counter_reader___read_many_sample_pulse_time___returns_valid_samples(
    ci_pulse_time_task: nidaqmx.Task,
) -> None:
    reader = CounterReader(ci_pulse_time_task.in_stream)
    samples_to_read = 10
    high_time_data = numpy.full(samples_to_read, numpy.inf, dtype=numpy.float64)
    low_time_data = numpy.full(samples_to_read, numpy.inf, dtype=numpy.float64)

    samples_read = reader.read_many_sample_pulse_time(
        high_time_data, low_time_data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    _validate_pulse_time_data(high_time_data, low_time_data)


@pytest.mark.parametrize(
    "high_time_dtype, low_time_dtype",
    [
        (numpy.float32, numpy.float64),
        (numpy.float64, numpy.float32),
        (numpy.float32, numpy.float32),
    ],
)
def test___counter_reader___read_many_sample_pulse_time_with_wrong_dtype___raises_error_with_correct_dtype(
    ci_pulse_time_task: nidaqmx.Task,
    high_time_dtype: numpy.typing.DTypeLike,
    low_time_dtype: numpy.typing.DTypeLike,
) -> None:
    reader = CounterReader(ci_pulse_time_task.in_stream)
    samples_to_read = 10
    high_time_data = numpy.full(samples_to_read, math.inf, dtype=high_time_dtype)
    low_time_data = numpy.full(samples_to_read, math.inf, dtype=low_time_dtype)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_pulse_time(
            high_time_data, low_time_data, number_of_samples_per_channel=samples_to_read
        )

    assert "float64" in exc_info.value.args[0]


def test___counter_reader___read_one_sample_pulse_ticks___returns_valid_samples(
    ci_pulse_ticks_task: nidaqmx.Task,
) -> None:
    reader = CounterReader(ci_pulse_ticks_task.in_stream)
    samples_to_read = 10

    data = [reader.read_one_sample_pulse_ticks() for _ in range(samples_to_read)]
    high_tick_data = numpy.array([datum.high_tick for datum in data])
    low_tick_data = numpy.array([datum.low_tick for datum in data])

    _validate_pulse_tick_data(high_tick_data, low_tick_data)


def test___counter_reader___read_many_sample_pulse_ticks___returns_valid_samples(
    ci_pulse_ticks_task: nidaqmx.Task,
) -> None:
    reader = CounterReader(ci_pulse_ticks_task.in_stream)
    samples_to_read = 10
    high_tick_data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)
    low_tick_data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)

    samples_read = reader.read_many_sample_pulse_ticks(
        high_tick_data, low_tick_data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    _validate_pulse_tick_data(high_tick_data, low_tick_data)


@pytest.mark.parametrize(
    "high_ticks_dtype, high_ticks_default, low_ticks_dtype, low_ticks_default",
    [
        (numpy.float64, math.inf, numpy.uint32, numpy.iinfo(numpy.uint32).min),
        (numpy.uint32, numpy.iinfo(numpy.uint32).min, numpy.float64, math.inf),
        (numpy.float64, math.inf, numpy.float64, math.inf),
    ],
)
def test___counter_reader___read_many_sample_pulse_ticks_with_wrong_dtype___raises_error_with_correct_dtype(
    ci_pulse_ticks_task: nidaqmx.Task,
    high_ticks_dtype: numpy.typing.DTypeLike,
    high_ticks_default: float | int,
    low_ticks_dtype: numpy.typing.DTypeLike,
    low_ticks_default: float | int,
) -> None:
    reader = CounterReader(ci_pulse_ticks_task.in_stream)
    samples_to_read = 10
    high_tick_data = numpy.full(samples_to_read, high_ticks_default, dtype=high_ticks_dtype)
    low_tick_data = numpy.full(samples_to_read, low_ticks_default, dtype=low_ticks_dtype)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_pulse_ticks(
            high_tick_data, low_tick_data, number_of_samples_per_channel=samples_to_read
        )

    assert "uint32" in exc_info.value.args[0]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/test_stream_writers_co.py sha256=6b2adc2eeb529db904f13d8f4ce9118ef9ef0ce2ec9f0e8e852cbdcf46eb2552 bytes=10529 -->
## FILE: tests/component/test_stream_writers_co.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/test_stream_writers_co.py`
- sha256: `6b2adc2eeb529db904f13d8f4ce9118ef9ef0ce2ec9f0e8e852cbdcf46eb2552`
- bytes: 10529

````python
from __future__ import annotations

import ctypes
import math
from collections.abc import Callable

import numpy
import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import AcquisitionType
from nidaqmx.stream_writers import CounterWriter
from nidaqmx.types import CtrFreq, CtrTick, CtrTime

START_DUTY_CYCLE = 0.1
END_DUTY_CYCLE = 0.9
START_FREQUENCY = 10000.0
END_FREQUENCY = 100000.0
TIMEBASE_NAME = "100MHzTimebase"
TIMEBASE_FREQUENCY = 100000000.0
EXPECTED_FREQUENCY_TOLERANCE = 1e-6
EXPECTED_DUTY_CYCLE_TOLERANCE = 1e-6


def _configure_and_start_co_task(task: nidaqmx.Task) -> None:
    task.co_channels.all.co_ctr_timebase_src = TIMEBASE_NAME
    task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)
    # We'll be doing on-demand, so start the task
    task.start()


@pytest.fixture
def co_freq_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task = generate_task()
    task.co_channels.add_co_pulse_chan_freq(
        real_x_series_device.co_physical_chans[0].name,
        # start the frequency "fast", so the write doesn't wait long
        freq=START_FREQUENCY,
    )
    _configure_and_start_co_task(task)
    return task


@pytest.fixture
def co_time_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task = generate_task()
    task.co_channels.add_co_pulse_chan_time(real_x_series_device.co_physical_chans[0].name)
    _configure_and_start_co_task(task)
    return task


@pytest.fixture
def co_ticks_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task = generate_task()
    task.co_channels.add_co_pulse_chan_ticks(
        real_x_series_device.co_physical_chans[0].name, source_terminal=TIMEBASE_NAME
    )
    _configure_and_start_co_task(task)
    return task


@pytest.fixture
def ci_freq_loopback_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task = generate_task()
    chan = task.ci_channels.add_ci_pulse_chan_freq(real_x_series_device.ci_physical_chans[1].name)
    chan.ci_pulse_freq_term = "Ctr0InternalOutput"
    chan.ci_ctr_timebase_src = TIMEBASE_NAME
    # We'll be doing on-demand, so start the task
    task.start()
    return task


def _get_counter_freq_data(num_samples: int) -> list[CtrFreq]:
    frequencies = numpy.linspace(START_FREQUENCY, END_FREQUENCY, num_samples)
    duty_cycles = numpy.linspace(START_DUTY_CYCLE, END_DUTY_CYCLE, num_samples)

    return [
        CtrFreq(freq=freq, duty_cycle=duty_cycle)
        for freq, duty_cycle in zip(frequencies, duty_cycles)
    ]


def _to_time(freq: CtrFreq) -> CtrTime:
    period = 1.0 / freq.freq
    high_time = period * freq.duty_cycle
    low_time = period - high_time
    return CtrTime(high_time, low_time)


def _to_ticks(freq: CtrFreq) -> CtrTick:
    period_ticks = TIMEBASE_FREQUENCY / freq.freq
    high_tick = int(period_ticks * freq.duty_cycle)
    low_tick = int(period_ticks - high_tick)
    return CtrTick(high_tick, low_tick)


def test___counter_writer___write_one_sample_pulse_frequency___updates_output(
    co_freq_task: nidaqmx.Task,
    ci_freq_loopback_task: nidaqmx.Task,
) -> None:
    writer = CounterWriter(co_freq_task.out_stream)
    samples_to_write = 10

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_counter_freq_data(samples_to_write):
        writer.write_one_sample_pulse_frequency(datum.freq, datum.duty_cycle)

    result = ci_freq_loopback_task.read()
    assert result.freq == pytest.approx(datum.freq, abs=EXPECTED_FREQUENCY_TOLERANCE)
    assert result.duty_cycle == pytest.approx(datum.duty_cycle, abs=EXPECTED_DUTY_CYCLE_TOLERANCE)


def test___counter_writer___write_many_sample_pulse_frequency___updates_output(
    co_freq_task: nidaqmx.Task,
    ci_freq_loopback_task: nidaqmx.Task,
) -> None:
    writer = CounterWriter(co_freq_task.out_stream)
    samples_to_write = 10
    data = _get_counter_freq_data(samples_to_write)
    frequencies = numpy.array([datum.freq for datum in data], dtype=numpy.float64)
    duty_cycles = numpy.array([datum.duty_cycle for datum in data], dtype=numpy.float64)

    writer.write_many_sample_pulse_frequency(frequencies, duty_cycles)

    result = ci_freq_loopback_task.read()
    assert result.freq == pytest.approx(data[-1].freq, abs=EXPECTED_FREQUENCY_TOLERANCE)
    assert result.duty_cycle == pytest.approx(
        data[-1].duty_cycle, abs=EXPECTED_DUTY_CYCLE_TOLERANCE
    )


@pytest.mark.parametrize(
    "freq_dtype, duty_cycle_dtype",
    [
        (numpy.float32, numpy.float64),
        (numpy.float64, numpy.float32),
        (numpy.float32, numpy.float32),
    ],
)
def test___counter_writer___write_many_sample_pulse_frequency_with_wrong_dtype___raises_error_with_correct_dtype(
    co_freq_task: nidaqmx.Task,
    freq_dtype: numpy.typing.DTypeLike,
    duty_cycle_dtype: numpy.typing.DTypeLike,
) -> None:
    writer = CounterWriter(co_freq_task.out_stream)
    samples_to_write = 10
    frequencies = numpy.full(samples_to_write, math.inf, dtype=freq_dtype)
    duty_cycles = numpy.full(samples_to_write, math.inf, dtype=duty_cycle_dtype)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_many_sample_pulse_frequency(frequencies, duty_cycles)

    assert "float64" in exc_info.value.args[0]


def test___counter_writer___write_one_sample_pulse_time___updates_output(
    co_time_task: nidaqmx.Task,
    ci_freq_loopback_task: nidaqmx.Task,
) -> None:
    writer = CounterWriter(co_time_task.out_stream)
    samples_to_write = 10

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_counter_freq_data(samples_to_write):
        datum_time = _to_time(datum)
        writer.write_one_sample_pulse_time(datum_time.high_time, datum_time.low_time)

    result = ci_freq_loopback_task.read()
    assert result.freq == pytest.approx(datum.freq, abs=EXPECTED_FREQUENCY_TOLERANCE)
    assert result.duty_cycle == pytest.approx(datum.duty_cycle, abs=EXPECTED_DUTY_CYCLE_TOLERANCE)


def test___counter_writer___write_many_sample_pulse_time___updates_output(
    co_time_task: nidaqmx.Task,
    ci_freq_loopback_task: nidaqmx.Task,
) -> None:
    writer = CounterWriter(co_time_task.out_stream)
    samples_to_write = 10
    data = _get_counter_freq_data(samples_to_write)
    high_times = numpy.array([_to_time(datum).high_time for datum in data], dtype=numpy.float64)
    low_times = numpy.array([_to_time(datum).low_time for datum in data], dtype=numpy.float64)

    writer.write_many_sample_pulse_time(high_times, low_times)

    result = ci_freq_loopback_task.read()
    assert result.freq == pytest.approx(data[-1].freq, abs=EXPECTED_FREQUENCY_TOLERANCE)
    assert result.duty_cycle == pytest.approx(
        data[-1].duty_cycle, abs=EXPECTED_DUTY_CYCLE_TOLERANCE
    )


@pytest.mark.parametrize(
    "high_time_dtype, low_time_dtype",
    [
        (numpy.float32, numpy.float64),
        (numpy.float64, numpy.float32),
        (numpy.float32, numpy.float32),
    ],
)
def test___counter_writer___write_many_sample_pulse_time_with_wrong_dtype___raises_error_with_correct_dtype(
    co_time_task: nidaqmx.Task,
    high_time_dtype: numpy.typing.DTypeLike,
    low_time_dtype: numpy.typing.DTypeLike,
) -> None:
    writer = CounterWriter(co_time_task.out_stream)
    samples_to_write = 10
    high_times = numpy.full(samples_to_write, math.inf, dtype=high_time_dtype)
    low_times = numpy.full(samples_to_write, math.inf, dtype=low_time_dtype)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_many_sample_pulse_time(high_times, low_times)

    assert "float64" in exc_info.value.args[0]


def test___counter_writer___write_one_sample_pulse_ticks___updates_output(
    co_ticks_task: nidaqmx.Task,
    ci_freq_loopback_task: nidaqmx.Task,
) -> None:
    writer = CounterWriter(co_ticks_task.out_stream)
    samples_to_write = 10

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_counter_freq_data(samples_to_write):
        datum_ticks = _to_ticks(datum)
        writer.write_one_sample_pulse_ticks(datum_ticks.high_tick, datum_ticks.low_tick)

    result = ci_freq_loopback_task.read()
    assert result.freq == pytest.approx(datum.freq, abs=EXPECTED_FREQUENCY_TOLERANCE)
    assert result.duty_cycle == pytest.approx(datum.duty_cycle, abs=EXPECTED_DUTY_CYCLE_TOLERANCE)


def test___counter_writer___write_many_sample_pulse_ticks___updates_output(
    co_ticks_task: nidaqmx.Task,
    ci_freq_loopback_task: nidaqmx.Task,
) -> None:
    writer = CounterWriter(co_ticks_task.out_stream)
    samples_to_write = 10
    data = _get_counter_freq_data(samples_to_write)
    high_ticks = numpy.array([_to_ticks(datum).high_tick for datum in data], dtype=numpy.uint32)
    low_ticks = numpy.array([_to_ticks(datum).low_tick for datum in data], dtype=numpy.uint32)

    writer.write_many_sample_pulse_ticks(high_ticks, low_ticks)

    result = ci_freq_loopback_task.read()
    assert result.freq == pytest.approx(data[-1].freq, abs=EXPECTED_FREQUENCY_TOLERANCE)
    assert result.duty_cycle == pytest.approx(
        data[-1].duty_cycle, abs=EXPECTED_DUTY_CYCLE_TOLERANCE
    )


@pytest.mark.parametrize(
    "high_ticks_dtype, low_ticks_dtype",
    [
        (numpy.uint16, numpy.uint32),
        (numpy.uint32, numpy.uint16),
        (numpy.uint16, numpy.uint16),
    ],
)
def test___counter_writer___write_many_sample_pulse_ticks_with_wrong_dtype___raises_error_with_correct_dtype(
    co_ticks_task: nidaqmx.Task,
    high_ticks_dtype: numpy.typing.DTypeLike,
    low_ticks_dtype: numpy.typing.DTypeLike,
) -> None:
    writer = CounterWriter(co_ticks_task.out_stream)
    samples_to_write = 10
    high_ticks = numpy.full(samples_to_write, 0, dtype=high_ticks_dtype)
    low_ticks = numpy.full(samples_to_write, 0, dtype=low_ticks_dtype)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_many_sample_pulse_ticks(high_ticks, low_ticks)

    assert "uint32" in exc_info.value.args[0]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/test_task.py sha256=6f656475d5d6865afdfd560938c7f9a6c16f670a92abc02f3a8d4021982d6111 bytes=7411 -->
## FILE: tests/component/test_task.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/test_task.py`
- sha256: `6f656475d5d6865afdfd560938c7f9a6c16f670a92abc02f3a8d4021982d6111`
- bytes: 7411

````python
import weakref

import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import ShuntCalSelect, ShuntCalSource, ShuntElementLocation
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system.storage import PersistedChannel


@pytest.fixture
def ai_bridge_task(task: nidaqmx.Task, device) -> nidaqmx.Task:
    task.ai_channels.add_ai_bridge_chan(device.ai_physical_chans[0].name)
    return task


@pytest.fixture
def ai_strain_gage_task(task: nidaqmx.Task, device) -> nidaqmx.Task:
    task.ai_channels.add_ai_strain_gage_chan(
        device.ai_physical_chans[0].name, initial_bridge_voltage=0.002
    )
    return task


@pytest.fixture
def ai_thermocouple_task(task: nidaqmx.Task, device) -> nidaqmx.Task:
    task.ai_channels.add_ai_thrmcpl_chan(device.ai_physical_chans[0].name)
    return task


@pytest.fixture
def ai_on_demand_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task:
    """Gets an AI task."""
    task.ai_channels.add_ai_voltage_chan(
        f"{sim_6363_device.name}/ai0:3", name_to_assign_to_channel="MyChannel"
    )
    return task


@pytest.mark.library_only(reason="Default gRPC initialization behavior is auto (create or attach)")
def test___task___create_task_with_same_name___raises_duplicate_task(init_kwargs):
    task1 = nidaqmx.Task("MyTask1", **init_kwargs)

    with task1, pytest.raises(nidaqmx.DaqError) as exc_info:
        _ = nidaqmx.Task("MyTask1", **init_kwargs)

    assert exc_info.value.error_code == DAQmxErrors.DUPLICATE_TASK


def test___tasks_with_different_names___compare___not_equal(generate_task):
    task1 = generate_task("MyTask1")
    task2 = generate_task("MyTask2")

    assert task1 != task2


def test___tasks_with_different_names___hash___not_equal(generate_task):
    task1 = generate_task("MyTask1")
    task2 = generate_task("MyTask2")

    assert hash(task1) != hash(task2)


@pytest.mark.device_name("bridgeTester")
@pytest.mark.parametrize("skip_unsupported_channels", [True, False])
def test___arguments_specified___perform_bridge_offset_nulling_cal___no_errors(
    ai_bridge_task: nidaqmx.Task, skip_unsupported_channels
) -> None:
    ai_bridge_task.perform_bridge_offset_nulling_cal(
        ai_bridge_task.channels.name, skip_unsupported_channels
    )


@pytest.mark.device_name("bridgeTester")
def test___default_arguments___perform_bridge_offset_nulling_cal___no_errors(
    ai_bridge_task: nidaqmx.Task,
) -> None:
    ai_bridge_task.perform_bridge_offset_nulling_cal()


@pytest.mark.device_name("bridgeTester")
@pytest.mark.parametrize(
    "shunt_resistor_value, shunt_resistor_location, shunt_resistor_select, shunt_resistor_source, bridge_resistance, skip_unsupported_channels",
    [
        (100000, ShuntElementLocation.R1, ShuntCalSelect.A, ShuntCalSource.DEFAULT, 0.2, True),
        (100000, ShuntElementLocation.R1, ShuntCalSelect.A, ShuntCalSource.DEFAULT, 0.2, False),
        (100000, ShuntElementLocation.R3, ShuntCalSelect.A, ShuntCalSource.DEFAULT, 0.2, True),
        (100000, ShuntElementLocation.R3, ShuntCalSelect.A, ShuntCalSource.DEFAULT, 0.2, False),
    ],
)
def test___perform_bridge_shunt_cal___no_errors(
    ai_bridge_task: nidaqmx.Task,
    shunt_resistor_value,
    shunt_resistor_location,
    shunt_resistor_select,
    shunt_resistor_source,
    bridge_resistance,
    skip_unsupported_channels,
) -> None:
    try:
        ai_bridge_task.perform_bridge_shunt_cal(
            ai_bridge_task.channels.name,
            shunt_resistor_value,
            shunt_resistor_location,
            shunt_resistor_select,
            shunt_resistor_source,
            bridge_resistance,
            skip_unsupported_channels,
        )
    except nidaqmx.DaqError as e:
        if e.error_code != DAQmxErrors.SHUNT_CAL_FAILED_OUT_OF_RANGE:
            raise


@pytest.mark.device_name("bridgeTester")
def test___perform_bridge_shunt_cal_default___no_errors(
    ai_bridge_task: nidaqmx.Task,
) -> None:
    try:
        ai_bridge_task.perform_bridge_shunt_cal(ai_bridge_task.channels.name)
    except nidaqmx.DaqError as e:
        if e.error_code != DAQmxErrors.SHUNT_CAL_FAILED_OUT_OF_RANGE:
            raise


@pytest.mark.device_name("bridgeTester")
@pytest.mark.parametrize(
    "shunt_resistor_value, shunt_resistor_location, shunt_resistor_select, shunt_resistor_source, skip_unsupported_channels",
    [
        (100000, ShuntElementLocation.R1, ShuntCalSelect.A, ShuntCalSource.DEFAULT, False),
        (100000, ShuntElementLocation.R1, ShuntCalSelect.A, ShuntCalSource.DEFAULT, False),
        (100000, ShuntElementLocation.R3, ShuntCalSelect.A, ShuntCalSource.DEFAULT, True),
        (100000, ShuntElementLocation.R3, ShuntCalSelect.A, ShuntCalSource.DEFAULT, False),
    ],
)
def test___perform_strain_shunt_cal___no_errors(
    ai_strain_gage_task: nidaqmx.Task,
    shunt_resistor_value,
    shunt_resistor_location,
    shunt_resistor_select,
    shunt_resistor_source,
    skip_unsupported_channels,
) -> None:
    try:
        ai_strain_gage_task.perform_strain_shunt_cal(
            ai_strain_gage_task.channels.name,
            shunt_resistor_value,
            shunt_resistor_location,
            shunt_resistor_select,
            shunt_resistor_source,
            skip_unsupported_channels,
        )
    except nidaqmx.DaqError as e:
        if e.error_code != DAQmxErrors.SHUNT_CAL_FAILED_OUT_OF_RANGE:
            raise


@pytest.mark.device_name("bridgeTester")
def test___perform_strain_shunt_cal_default___no_errors(
    ai_strain_gage_task: nidaqmx.Task,
) -> None:
    try:
        ai_strain_gage_task.perform_strain_shunt_cal(ai_strain_gage_task.channels.name)
    except nidaqmx.DaqError as e:
        if e.error_code != DAQmxErrors.SHUNT_CAL_FAILED_OUT_OF_RANGE:
            raise


@pytest.mark.device_name("cDAQ1Mod2")
@pytest.mark.parametrize("skip_unsupported_channels", [True, False])
def test___arguments_specified___perform_thrmcpl_lead_offset_nulling_cal___no_errors(
    ai_thermocouple_task: nidaqmx.Task, skip_unsupported_channels
) -> None:
    ai_thermocouple_task.perform_thrmcpl_lead_offset_nulling_cal(
        ai_thermocouple_task.channels.name, skip_unsupported_channels
    )


@pytest.mark.device_name("cDAQ1Mod2")
def test___default_arguments___perform_thrmcpl_lead_offset_nulling_cal___no_errors(
    ai_thermocouple_task: nidaqmx.Task,
) -> None:
    ai_thermocouple_task.perform_thrmcpl_lead_offset_nulling_cal()


def test___on_demand_task_is_done___is_task_done___returns_true(ai_on_demand_task: nidaqmx.Task):
    assert ai_on_demand_task.is_task_done()
    ai_on_demand_task.start()
    ai_on_demand_task.wait_until_done()

    assert ai_on_demand_task.is_task_done()


def test___task___add_global_channels___adds_to_channel_names(task: nidaqmx.Task):
    persisted_channel = PersistedChannel("VoltageTesterChannel")
    persisted_channel2 = PersistedChannel("VoltageTesterChannel2")

    task.add_global_channels([persisted_channel, persisted_channel2])

    assert task.channel_names == [persisted_channel.name, persisted_channel2.name]


def test___task___create_weakref___succeeds(task: nidaqmx.Task):
    ref = weakref.ref(task)
    task2 = ref()
    assert task is task2
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/test_task_events.py sha256=7f48972151eaf58745459b0e756f4aa08b5e73bcd695b3bcbf077984309eb550 bytes=24304 -->
## FILE: tests/component/test_task_events.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/test_task_events.py`
- sha256: `7f48972151eaf58745459b0e756f4aa08b5e73bcd695b3bcbf077984309eb550`
- bytes: 24304

````python
from __future__ import annotations

import threading
import time
import traceback
from logging import LogRecord

import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import AcquisitionType, EveryNSamplesEventType, Signal
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqResourceWarning
from nidaqmx.task import _TaskEventType
from tests._event_utils import (
    DoneEventObserver,
    EveryNSamplesEventObserver,
    SignalEventObserver,
)


@pytest.fixture
def ai_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task:
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    return task


@pytest.fixture
def ai_task_with_real_device(
    task: nidaqmx.Task, real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    task.ai_channels.add_ai_voltage_chan(real_x_series_device.ai_physical_chans[0].name)
    return task


@pytest.fixture
def ao_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task:
    task.ao_channels.add_ao_voltage_chan(sim_6363_device.ao_physical_chans[0].name)
    return task


def test___done_event_registered___run_finite_acquisition___callback_invoked_once_with_success_status(
    ai_task: nidaqmx.Task,
) -> None:
    event_observer = DoneEventObserver()
    ai_task.register_done_event(event_observer.handle_done_event)
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    ai_task.start()

    event_observer.wait_for_events()
    with pytest.raises(TimeoutError):
        event_observer.wait_for_events(timeout=100e-3)
    assert len(event_observer.events) == 1
    assert all(e.status == 0 for e in event_observer.events)


@pytest.mark.grpc_xfail(
    reason="#559: Can't close tasks in an event callback when using gRPC", raises=AssertionError
)
def test___done_event_registered___call_stop_close_in_callback___task_closed_with_success_status(
    sim_6363_device: nidaqmx.system.Device,
    init_kwargs: dict,
) -> None:

    # We have to define and set this here because mypy will error if it is
    # defined below with everything else: https://github.com/python/mypy/issues/7057
    side_effect_semaphore = threading.Semaphore(value=0)

    # side_effect for callback
    def _clear_task():
        task.stop()
        task.close()
        side_effect_semaphore.release()

    try:
        # We need to create our own task here because we need to call stop() and close() on it.
        task: nidaqmx.Task = nidaqmx.Task(**init_kwargs)
        task.ai_channels.add_ai_voltage_chan(
            sim_6363_device.ai_physical_chans[0].name, max_val=10, min_val=-10
        )
    except nidaqmx.DaqError:
        if task is not None:
            task.close()
        raise
    event_observer = DoneEventObserver(side_effect=_clear_task)
    task.register_done_event(event_observer.handle_done_event)
    task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    task.start()
    event_observer.wait_for_events(1)
    acquired = side_effect_semaphore.acquire(timeout=10.0)

    # Ensure we get the expected exception and warning
    with pytest.raises(nidaqmx.DaqError) as exc_info:
        task.stop()
    with pytest.warns(
        DaqResourceWarning,
        match="Attempted to close NI-DAQmx task",
    ) as warnings_record:
        task.close()
    assert acquired
    assert len(event_observer.events) == 1
    assert event_observer.events[0].status == 0
    assert exc_info.value.error_code == DAQmxErrors.INVALID_TASK
    assert len(warnings_record) == 1


@pytest.mark.grpc_xfail(
    reason="#559: Can't close tasks in an event callback when using gRPC", raises=AssertionError
)
def test___every_n_samples_event_registered___call_stop_close_in_callback___task_closed_with_success_status(
    sim_6363_device: nidaqmx.system.Device,
    init_kwargs: dict,
) -> None:

    # We have to define and set this here because mypy will error if it is
    # defined below with everything else: https://github.com/python/mypy/issues/7057
    callback_call_number = 0
    side_effect_semaphore = threading.Semaphore(value=0)

    # side_effect for callback
    def _clear_task():
        nonlocal callback_call_number
        callback_call_number += 1
        if callback_call_number == 4:
            task.stop()
            task.close()
            side_effect_semaphore.release()

    try:
        # We need to create our own task here because we need to call stop() and close() on it.
        task: nidaqmx.Task = nidaqmx.Task(**init_kwargs)
        task.ai_channels.add_ai_voltage_chan(
            sim_6363_device.ai_physical_chans[0].name, max_val=10, min_val=-10
        )
    except nidaqmx.DaqError:
        if task is not None:
            task.close()
        raise
    event_observer = EveryNSamplesEventObserver(side_effect=_clear_task)
    task.register_every_n_samples_acquired_into_buffer_event(
        100, event_observer.handle_every_n_samples_event
    )
    task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    task.start()
    event_observer.wait_for_events(4)
    acquired = side_effect_semaphore.acquire(timeout=10.0)

    # Ensure we get the expected exception and warning
    with pytest.raises(nidaqmx.DaqError) as exc_info:
        task.stop()
    with pytest.warns(
        DaqResourceWarning,
        match="Attempted to close NI-DAQmx task",
    ) as warnings_record:
        task.close()
    assert acquired
    assert len(event_observer.events) == 4
    assert [e.number_of_samples for e in event_observer.events] == [100, 100, 100, 100]
    assert exc_info.value.error_code == DAQmxErrors.INVALID_TASK
    assert len(warnings_record) == 1


def test___every_n_samples_event_registered___run_finite_acquisition___callback_invoked_n_times_with_type_and_num_samples(
    ai_task: nidaqmx.Task,
) -> None:
    event_observer = EveryNSamplesEventObserver()
    ai_task.register_every_n_samples_acquired_into_buffer_event(
        100, event_observer.handle_every_n_samples_event
    )
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    ai_task.start()

    event_observer.wait_for_events(10)
    with pytest.raises(TimeoutError):
        event_observer.wait_for_events(timeout=100e-3)
    assert len(event_observer.events) == 10
    assert all(
        e.event_type == EveryNSamplesEventType.ACQUIRED_INTO_BUFFER.value
        for e in event_observer.events
    )
    assert all(e.number_of_samples == 100 for e in event_observer.events)


def test___signal_event_registered___run_finite_acquisition___callback_invoked_n_times_with_type(
    ai_task_with_real_device: nidaqmx.Task,
) -> None:
    ai_task = ai_task_with_real_device
    event_observer = SignalEventObserver()
    ai_task.register_signal_event(Signal.SAMPLE_COMPLETE, event_observer.handle_signal_event)
    ai_task.timing.cfg_samp_clk_timing(
        rate=10.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=10
    )

    ai_task.start()

    event_observer.wait_for_events(10)
    with pytest.raises(TimeoutError):
        event_observer.wait_for_events(timeout=100e-3)
    assert len(event_observer.events) == 10
    assert all(e.signal_type == Signal.SAMPLE_COMPLETE.value for e in event_observer.events)


def test___done_event_unregistered___run_finite_acquisition___callback_not_invoked(
    ai_task: nidaqmx.Task,
) -> None:
    event_observer = DoneEventObserver()
    ai_task.register_done_event(event_observer.handle_done_event)
    ai_task.register_done_event(None)
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    ai_task.start()
    ai_task.wait_until_done()

    with pytest.raises(TimeoutError):
        event_observer.wait_for_events(timeout=100e-3)
    assert len(event_observer.events) == 0


def test___every_n_samples_event_unregistered___run_finite_acquisition___callback_not_invoked(
    ai_task: nidaqmx.Task,
) -> None:
    event_observer = EveryNSamplesEventObserver()
    ai_task.register_every_n_samples_acquired_into_buffer_event(
        100, event_observer.handle_every_n_samples_event
    )
    ai_task.register_every_n_samples_acquired_into_buffer_event(100, None)
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    ai_task.start()
    ai_task.wait_until_done()

    with pytest.raises(TimeoutError):
        event_observer.wait_for_events(timeout=100e-3)
    assert len(event_observer.events) == 0


def test___signal_event_unregistered___run_finite_acquisition___callback_not_invoked(
    ai_task_with_real_device: nidaqmx.Task,
) -> None:
    ai_task = ai_task_with_real_device
    event_observer = SignalEventObserver()
    ai_task.register_signal_event(Signal.SAMPLE_COMPLETE, event_observer.handle_signal_event)
    ai_task.register_signal_event(Signal.SAMPLE_COMPLETE, None)
    ai_task.timing.cfg_samp_clk_timing(
        rate=10.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=10
    )

    ai_task.start()
    ai_task.wait_until_done()

    with pytest.raises(TimeoutError):
        event_observer.wait_for_events(timeout=100e-3)
    assert len(event_observer.events) == 0


def test___done_and_every_n_samples_events_registered___run_finite_acquisition___callbacks_invoked(
    ai_task: nidaqmx.Task,
) -> None:
    done_event_observer = DoneEventObserver()
    every_n_samples_event_observer = EveryNSamplesEventObserver()
    ai_task.register_done_event(done_event_observer.handle_done_event)
    ai_task.register_every_n_samples_acquired_into_buffer_event(
        100, every_n_samples_event_observer.handle_every_n_samples_event
    )
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    ai_task.start()

    done_event_observer.wait_for_events()
    every_n_samples_event_observer.wait_for_events(10)
    assert len(done_event_observer.events) == 1
    assert len(every_n_samples_event_observer.events) == 10


def test___done_and_every_n_samples_events_registered___run_multiple_finite_acquisitions___callbacks_invoked(
    ai_task: nidaqmx.Task,
) -> None:
    num_acquisitions = 3
    done_event_observer = DoneEventObserver()
    every_n_samples_event_count = 10
    every_n_samples_event_observer = EveryNSamplesEventObserver()
    ai_task.register_done_event(done_event_observer.handle_done_event)
    ai_task.register_every_n_samples_acquired_into_buffer_event(
        100, every_n_samples_event_observer.handle_every_n_samples_event
    )
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    for _ in range(num_acquisitions):
        ai_task.start()
        done_event_observer.wait_for_events()
        every_n_samples_event_observer.wait_for_events(every_n_samples_event_count)
        ai_task.stop()

    assert len(done_event_observer.events) == num_acquisitions
    assert (
        len(every_n_samples_event_observer.events) == num_acquisitions * every_n_samples_event_count
    )


def test___ai_task____run_multiple_finite_acquisitions_with_varying_every_n_samples_event_interval___callbacks_invoked(
    ai_task: nidaqmx.Task,
) -> None:
    num_acquisitions = 3
    done_event_observer = DoneEventObserver()
    every_n_samples_event_counts = [10, 5, 4]
    every_n_samples_event_intervals = [100, 200, 250]
    every_n_samples_event_observers = [
        EveryNSamplesEventObserver() for _ in range(num_acquisitions)
    ]
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )
    ai_task.register_done_event(done_event_observer.handle_done_event)

    for i in range(3):
        ai_task.register_every_n_samples_acquired_into_buffer_event(
            every_n_samples_event_intervals[i],
            every_n_samples_event_observers[i].handle_every_n_samples_event,
        )
        ai_task.start()
        done_event_observer.wait_for_events()
        every_n_samples_event_observers[i].wait_for_events(every_n_samples_event_counts[i])
        ai_task.stop()
        ai_task.register_every_n_samples_acquired_into_buffer_event(100, None)

    assert len(done_event_observer.events) == num_acquisitions
    assert [
        len(observer.events) for observer in every_n_samples_event_observers
    ] == every_n_samples_event_counts


def test___done_event_registered___register_done_event___already_registered_error_raised(
    ai_task: nidaqmx.Task,
) -> None:
    event_observer = DoneEventObserver()
    ai_task.register_done_event(event_observer.handle_done_event)
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        ai_task.register_done_event(event_observer.handle_done_event)

    assert exc_info.value.error_code == DAQmxErrors.DONE_EVENT_ALREADY_REGISTERED


def test___every_n_samples_acquired_into_buffer_event_registered___register_every_n_samples_acquired_into_buffer_event___already_registered_error_raised(
    ai_task: nidaqmx.Task,
) -> None:
    event_observer = EveryNSamplesEventObserver()
    ai_task.register_every_n_samples_acquired_into_buffer_event(
        100, event_observer.handle_every_n_samples_event
    )
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        ai_task.register_every_n_samples_acquired_into_buffer_event(
            100, event_observer.handle_every_n_samples_event
        )

    assert (
        exc_info.value.error_code
        == DAQmxErrors.EVERY_N_SAMPS_ACQ_INTO_BUFFER_EVENT_ALREADY_REGISTERED
    )


def test___every_n_samples_transferred_from_buffer_event_registered___register_every_n_samples_transferred_from_buffer_event___already_registered_error_raised(
    ao_task: nidaqmx.Task,
) -> None:
    event_observer = EveryNSamplesEventObserver()
    ao_task.register_every_n_samples_transferred_from_buffer_event(
        100, event_observer.handle_every_n_samples_event
    )
    ao_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        ao_task.register_every_n_samples_transferred_from_buffer_event(
            100, event_observer.handle_every_n_samples_event
        )

    assert (
        exc_info.value.error_code
        == DAQmxErrors.EVERY_N_SAMPS_TRANSFERRED_FROM_BUFFER_EVENT_ALREADY_REGISTERED
    )


def test___signal_event_registered___register_signal_event___already_registered_error_raised(
    ai_task: nidaqmx.Task,
) -> None:
    event_observer = SignalEventObserver()
    ai_task.register_signal_event(Signal.SAMPLE_COMPLETE, event_observer.handle_signal_event)
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        ai_task.register_signal_event(Signal.SAMPLE_COMPLETE, event_observer.handle_signal_event)

    assert exc_info.value.error_code == DAQmxErrors.SIGNAL_EVENT_ALREADY_REGISTERED


def test___ai_task___register_wrong_every_n_samples_event___not_supported_by_device_error_raised(
    ai_task: nidaqmx.Task,
) -> None:
    event_observer = EveryNSamplesEventObserver()
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        ai_task.register_every_n_samples_transferred_from_buffer_event(
            100, event_observer.handle_every_n_samples_event
        )

    assert (
        exc_info.value.error_code
        == DAQmxErrors.EVERY_N_SAMPS_TRANSFERRED_FROM_BUFFER_EVENT_NOT_SUPPORTED_BY_DEVICE
    )


def test___ao_task___register_wrong_every_n_samples_event___not_supported_by_device_error_raised(
    ao_task: nidaqmx.Task,
) -> None:
    event_observer = EveryNSamplesEventObserver()
    ao_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        ao_task.register_every_n_samples_acquired_into_buffer_event(
            100, event_observer.handle_every_n_samples_event
        )

    assert (
        exc_info.value.error_code
        == DAQmxErrors.EVERY_N_SAMPLES_ACQ_INTO_BUFFER_EVENT_NOT_SUPPORTED_BY_DEVICE
    )


def test___task___register_unregister_done_event___callback_not_invoked(
    ai_task: nidaqmx.Task,
) -> None:
    event_observer = DoneEventObserver()

    for _ in range(10):
        ai_task.register_done_event(event_observer.handle_done_event)
        ai_task.register_done_event(None)

    assert len(event_observer.events) == 0


def test___task___register_unregister_every_n_samples_acquired_into_buffer_event___callback_not_invoked(
    ai_task: nidaqmx.Task,
) -> None:
    event_observer = EveryNSamplesEventObserver()

    for _ in range(10):
        ai_task.register_every_n_samples_acquired_into_buffer_event(
            100, event_observer.handle_every_n_samples_event
        )
        ai_task.register_every_n_samples_acquired_into_buffer_event(100, None)

    assert len(event_observer.events) == 0


def test___task___register_unregister_every_n_samples_transferred_from_buffer_event___callback_not_invoked(
    ao_task: nidaqmx.Task,
) -> None:
    event_observer = EveryNSamplesEventObserver()

    for _ in range(10):
        ao_task.register_every_n_samples_transferred_from_buffer_event(
            100, event_observer.handle_every_n_samples_event
        )
        ao_task.register_every_n_samples_transferred_from_buffer_event(100, None)

    assert len(event_observer.events) == 0


def test___task___register_unregister_signal_event___callback_not_invoked(
    ai_task: nidaqmx.Task,
) -> None:
    event_observer = SignalEventObserver()

    for _ in range(10):
        ai_task.register_signal_event(Signal.SAMPLE_COMPLETE, event_observer.handle_signal_event)
        ai_task.register_signal_event(Signal.SAMPLE_COMPLETE, None)

    assert len(event_observer.events) == 0


@pytest.mark.grpc_only(reason="Tests gRPC-specific error case")
@pytest.mark.temporary_grpc_channel
def test___events_registered_and_grpc_channel_closed___close_task___events_cleaned_up_and_clear_task_error_raised(
    ai_task: nidaqmx.Task, grpc_channel
):
    done_event_observer = DoneEventObserver()
    every_n_samples_event_observer = EveryNSamplesEventObserver()
    ai_task.register_done_event(done_event_observer.handle_done_event)
    ai_task.register_every_n_samples_acquired_into_buffer_event(
        100, every_n_samples_event_observer.handle_every_n_samples_event
    )
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )
    done_event_handler = ai_task._event_handlers[_TaskEventType.DONE]
    every_n_samples_event_handler = ai_task._event_handlers[
        _TaskEventType.EVERY_N_SAMPLES_ACQUIRED_INTO_BUFFER
    ]
    ai_task._close_on_exit = False  # avoid double-close warning
    grpc_channel.close()

    with pytest.raises(ValueError, match="closed channel") as exc_info:
        ai_task.close()

    assert "in clear_task\n" in "".join(traceback.format_tb(exc_info.value.__traceback__))
    assert ai_task._handle is None
    assert len(ai_task._event_handlers) == 0
    assert not done_event_handler._thread.is_alive()
    assert not every_n_samples_event_handler._thread.is_alive()


# ctypes reports exceptions in callback functions by invoking sys.unraisablehook.
@pytest.mark.filterwarnings("ignore::pytest.PytestUnraisableExceptionWarning")
def test___event_callback_that_raises_exceptions___run_finite_acquisition___exceptions_ignored(
    ai_task: nidaqmx.Task,
) -> None:
    done_event_exception = RuntimeError("done event error")
    done_event_observer = DoneEventObserver(side_effect=done_event_exception)
    every_n_samples_event_count = 10
    every_n_samples_event_exception = RuntimeError("every n samples event error")
    every_n_samples_event_observer = EveryNSamplesEventObserver(
        side_effect=every_n_samples_event_exception
    )
    ai_task.register_done_event(done_event_observer.handle_done_event)
    ai_task.register_every_n_samples_acquired_into_buffer_event(
        100, every_n_samples_event_observer.handle_every_n_samples_event
    )
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    ai_task.start()
    done_event_observer.wait_for_events()
    every_n_samples_event_observer.wait_for_events(every_n_samples_event_count)
    ai_task.stop()

    assert len(done_event_observer.events) == 1
    assert len(every_n_samples_event_observer.events) == every_n_samples_event_count


@pytest.mark.grpc_only(reason="This tests gRPC-specific behavior")
def test___event_callback_that_raises_exceptions___run_finite_acquisition___exceptions_logged(
    ai_task: nidaqmx.Task,
    caplog: pytest.LogCaptureFixture,
) -> None:
    done_event_exception = RuntimeError("done event error")
    done_event_observer = DoneEventObserver(side_effect=done_event_exception)
    every_n_samples_event_count = 10
    every_n_samples_event_exception = RuntimeError("every n samples event error")
    every_n_samples_event_observer = EveryNSamplesEventObserver(
        side_effect=every_n_samples_event_exception
    )
    ai_task.register_done_event(done_event_observer.handle_done_event)
    ai_task.register_every_n_samples_acquired_into_buffer_event(
        100, every_n_samples_event_observer.handle_every_n_samples_event
    )
    ai_task.timing.cfg_samp_clk_timing(
        rate=10000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000
    )

    ai_task.start()
    done_event_observer.wait_for_events()
    every_n_samples_event_observer.wait_for_events(every_n_samples_event_count)
    ai_task.stop()

    done_event_records = _wait_for_log_records(caplog, "handle_done_event", 1)
    every_n_samples_event_records = _wait_for_log_records(
        caplog, "handle_every_n_samples_event", every_n_samples_event_count
    )
    assert all(
        _exception_matches(_get_exception(record), done_event_exception)
        for record in done_event_records
    )
    assert all(
        _exception_matches(_get_exception(record), every_n_samples_event_exception)
        for record in every_n_samples_event_records
    )


def _exception_matches(e1: BaseException, e2: BaseException) -> bool:
    return type(e1) is type(e2) and e1.args == e2.args


def _get_exception(record: LogRecord) -> BaseException:
    assert record.exc_info and record.exc_info[1]
    return record.exc_info[1]


def _wait_for_log_records(
    caplog: pytest.LogCaptureFixture, message_substring: str, expected_count: int, timeout=10.0
) -> list[LogRecord]:
    start_time = time.time()
    while time.time() - start_time < timeout:
        matching_records = [
            record for record in caplog.records if message_substring in record.message
        ]
        if len(matching_records) >= expected_count:
            return matching_records
        time.sleep(10e-3)
    raise TimeoutError(f"Expected {expected_count} records, got {len(matching_records)}.")
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/test_task_properties.py sha256=2e87b3ac775313b9dcdc9aa9322b9b0305bdbdae6de9b3d8f6f478bb640caddf bytes=1188 -->
## FILE: tests/component/test_task_properties.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/test_task_properties.py`
- sha256: `2e87b3ac775313b9dcdc9aa9322b9b0305bdbdae6de9b3d8f6f478bb640caddf`
- bytes: 1188

````python
import pytest

from nidaqmx import Task
from nidaqmx.system import Device


@pytest.fixture
def ai_task(task: Task, sim_6363_device: Device) -> Task:
    """Gets an AI task."""
    task.ai_channels.add_ai_voltage_chan(
        f"{sim_6363_device.name}/ai0:3", name_to_assign_to_channel="MyChannel"
    )
    return task


def test___get_channels___returns_channels(ai_task: Task):
    channel = ai_task.channels

    assert channel.name == "MyChannel0:3"


def test___get_channels___shared_interpreter(ai_task: Task):
    channel = ai_task.channels

    assert channel._interpreter is ai_task._interpreter


def test___get_devices___returns_devices(ai_task: Task, sim_6363_device: Device):
    devices = ai_task.devices

    assert [dev.name for dev in devices] == [sim_6363_device.name]


def test___get_devices___shared_interpreter(ai_task: Task):
    devices = ai_task.devices

    assert all(dev._interpreter is ai_task._interpreter for dev in devices)


def test___task___set_nonexistent_property___raises_exception(task: Task):
    with pytest.raises(AttributeError):
        task.nonexistent_property = "foo"  # type: ignore[attr-defined]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/test_task_resource_warnings.py sha256=99a4b9e768c83cbdddef3cd00eb8c9239033a1377208459b0757e4b32cd4a4dc bytes=1014 -->
## FILE: tests/component/test_task_resource_warnings.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/test_task_resource_warnings.py`
- sha256: `99a4b9e768c83cbdddef3cd00eb8c9239033a1377208459b0757e4b32cd4a4dc`
- bytes: 1014

````python
import warnings

import pytest

import nidaqmx
from nidaqmx.errors import DaqResourceWarning


@pytest.mark.library_only(reason="gRPC task allows detaching from task on server")
def test___unclosed_task___leak_task___resource_warning_raised(task):
    # Since __del__ is not guaranteed to be called, for the purposes of
    # consistent test results call __del__ manually.
    with pytest.warns(DaqResourceWarning):
        task.__del__()


@pytest.mark.grpc_only(reason="gRPC task allows detaching from task on server")
def test___grpc_task___leak_task___resource_warning_not_raised(task):
    with warnings.catch_warnings(record=True) as warnings_raised:
        task.__del__()

    assert len(warnings_raised) == 0


def test___closed_task___del_task___resource_warning_not_raised(init_kwargs):
    task = nidaqmx.Task(**init_kwargs)
    task.close()

    with warnings.catch_warnings(record=True) as warnings_raised:
        task.__del__()

    assert len(warnings_raised) == 0
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/test_watchdog.py sha256=018792809efdd29b6e59c80d5869d80baa10c4a4c4419d8ba0ad103a65647ebc bytes=4881 -->
## FILE: tests/component/test_watchdog.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/test_watchdog.py`
- sha256: `018792809efdd29b6e59c80d5869d80baa10c4a4c4419d8ba0ad103a65647ebc`
- bytes: 4881

````python
from __future__ import annotations

import weakref
from collections.abc import Callable

import pytest

from nidaqmx.constants import WatchdogAOExpirState, WatchdogCOExpirState
from nidaqmx.system import Device
from nidaqmx.system.watchdog import (
    AOExpirationState,
    COExpirationState,
    ExpirationState,
    WatchdogTask,
)


def test___watchdog_task___cfg_watchdog_ao_expir_states___no_error(
    generate_watchdog_task: Callable[..., WatchdogTask],
    sim_9189_device: Device,
    sim_9263_device: Device,
):
    watchdog_task = generate_watchdog_task(f"{sim_9189_device.name}", timeout=0.8)
    expir_states = [
        AOExpirationState(
            physical_channel=sim_9263_device.ao_physical_chans[0].name,
            expiration_state=0.0,
            output_type=WatchdogAOExpirState.VOLTAGE,
        ),
        AOExpirationState(
            physical_channel=sim_9263_device.ao_physical_chans[1].name,
            expiration_state=0.0,
            output_type=WatchdogAOExpirState.VOLTAGE,
        ),
    ]

    watchdog_task.cfg_watchdog_ao_expir_states(expir_states)
    watchdog_task.start()

    assert not watchdog_task.expired
    assert watchdog_task.timeout == 0.8
    assert (
        watchdog_task.expiration_states[sim_9263_device.ao_physical_chans[1].name].ao_state == 0.0
    )
    assert (
        watchdog_task.expiration_states[sim_9263_device.ao_physical_chans[1].name].ao_output_type
        == WatchdogAOExpirState.VOLTAGE
    )


def test___watchdog_task___cfg_watchdog_co_expir_states___no_error(
    generate_watchdog_task: Callable[..., WatchdogTask],
    sim_9189_device: Device,
    sim_9401_device: Device,
):
    watchdog_task = generate_watchdog_task(f"{sim_9189_device.name}", timeout=0.8)
    expir_states = [
        COExpirationState(
            physical_channel=sim_9401_device.co_physical_chans[0].name,
            expiration_state=WatchdogCOExpirState.LOW,
        ),
        COExpirationState(
            physical_channel=sim_9401_device.co_physical_chans[1].name,
            expiration_state=WatchdogCOExpirState.LOW,
        ),
    ]

    watchdog_task.cfg_watchdog_co_expir_states(expir_states)
    watchdog_task.start()

    assert not watchdog_task.expired
    assert watchdog_task.timeout == 0.8
    assert (
        watchdog_task.expiration_states[sim_9401_device.co_physical_chans[1].name].co_state
        == WatchdogCOExpirState.LOW
    )


def test___watchdog_task___clear_expiration___no_error(
    generate_watchdog_task: Callable[..., WatchdogTask],
    sim_9189_device: Device,
    sim_9263_device: Device,
):
    watchdog_task = generate_watchdog_task(f"{sim_9189_device.name}", timeout=0.8)
    expir_states = [
        AOExpirationState(
            physical_channel=sim_9263_device.ao_physical_chans[0].name,
            expiration_state=0.0,
            output_type=WatchdogAOExpirState.VOLTAGE,
        ),
        AOExpirationState(
            physical_channel=sim_9263_device.ao_physical_chans[1].name,
            expiration_state=0.0,
            output_type=WatchdogAOExpirState.VOLTAGE,
        ),
    ]
    watchdog_task.cfg_watchdog_ao_expir_states(expir_states)
    watchdog_task.start()

    watchdog_task.clear_expiration()


def test___watchdog_task___create_weakref___succeeds(
    generate_watchdog_task: Callable[..., WatchdogTask],
    sim_9189_device: Device,
):
    watchdog_task = generate_watchdog_task(f"{sim_9189_device.name}", timeout=0.8)
    ref = weakref.ref(watchdog_task)
    watchdog_task2 = ref()
    assert watchdog_task is watchdog_task2


def test___watchdog_task___set_nonexistent_property___raises_exception(
    generate_watchdog_task: Callable[..., WatchdogTask],
    sim_9189_device: Device,
):
    watchdog_task = generate_watchdog_task(f"{sim_9189_device.name}", timeout=0.8)

    with pytest.raises(AttributeError):
        watchdog_task.nonexistent_property = "foo"  # type: ignore[attr-defined]


def test___watchdog_expiration_states___set_nonexistent_property___raises_exception(
    generate_watchdog_task: Callable[..., WatchdogTask],
    sim_9189_device: Device,
    sim_9263_device: Device,
):
    watchdog_task = generate_watchdog_task(f"{sim_9189_device.name}", timeout=0.8)
    expir_states = [
        AOExpirationState(
            physical_channel=sim_9263_device.ao_physical_chans[0].name,
            expiration_state=0.0,
            output_type=WatchdogAOExpirState.VOLTAGE,
        )
    ]
    watchdog_task.cfg_watchdog_ao_expir_states(expir_states)
    expir_state: ExpirationState = watchdog_task.expiration_states[
        sim_9263_device.ao_physical_chans[0].name
    ]

    with pytest.raises(AttributeError):
        expir_state.nonexistent_property = "foo"  # type: ignore[attr-defined]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/conftest.py sha256=deb03d996246538902e037ac22c4d4b5222fd79f62ab97a3251e6b3edda5369d bytes=29350 -->
## FILE: tests/conftest.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/conftest.py`
- sha256: `deb03d996246538902e037ac22c4d4b5222fd79f62ab97a3251e6b3edda5369d`
- bytes: 29350

````python
"""Fixtures used in the DAQmx tests."""

from __future__ import annotations

import contextlib
import pathlib
from collections.abc import Callable, Generator
from concurrent.futures import ThreadPoolExecutor
from enum import Enum
from typing import TYPE_CHECKING

import pytest

import nidaqmx.system
from nidaqmx import _feature_toggles
from nidaqmx._base_interpreter import BaseInterpreter
from nidaqmx._feature_toggles import (
    CodeReadiness,
    FeatureToggle,
)
from nidaqmx.constants import ProductCategory, UsageTypeAI

try:
    import grpc

    from tests._grpc_utils import GrpcServerProcess
except ImportError:
    grpc = None  # type: ignore

if TYPE_CHECKING:
    # Not public yet: https://github.com/pytest-dev/pytest/issues/7469
    import _pytest.mark.structures  # noqa: I300


class Error(Exception):
    """Base error class."""

    pass


class NoFixtureDetectedError(Error):
    """Custom error class when no fixtures are available."""

    pass


class DeviceType(Enum):
    """Device Type."""

    ANY = (-1,)
    REAL = (0,)
    SIMULATED = 1


class SamplingType(Enum):
    """Sampling Type."""

    ANY = -1
    MULTIPLEXED = 0
    SIMULTANEOUS = 1


def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:
    """Parametrizes the "init_kwargs" fixture by examining the the markers set for a test.

    This is used to decide if tests for gRPC or Library interpreters should be run.
    This is done based on the custom markers @pytest.mark.grpc_only and @pytest.mark.library_only.
    """
    if "init_kwargs" in metafunc.fixturenames:
        # fixtures can't be parametrized more than once. this approach prevents exclusive
        # markers from being set on the same test

        grpc_only = metafunc.definition.get_closest_marker("grpc_only")
        library_only = metafunc.definition.get_closest_marker("library_only")
        params: list[_pytest.mark.structures.ParameterSet] = []

        if not grpc_only:
            library_marks: list[pytest.MarkDecorator] = []
            library_skip = metafunc.definition.get_closest_marker("library_skip")
            if library_skip:
                library_marks.append(pytest.mark.skip(*library_skip.args, **library_skip.kwargs))
            library_xfail = metafunc.definition.get_closest_marker("library_xfail")
            if library_xfail:
                library_marks.append(pytest.mark.xfail(*library_xfail.args, **library_xfail.kwargs))
            params.append(pytest.param("library_init_kwargs", marks=library_marks))

        if not library_only:
            grpc_marks: list[pytest.MarkDecorator] = []
            grpc_skip = metafunc.definition.get_closest_marker("grpc_skip")
            if grpc_skip:
                grpc_marks.append(pytest.mark.skip(*grpc_skip.args, **grpc_skip.kwargs))
            grpc_xfail = metafunc.definition.get_closest_marker("grpc_xfail")
            if grpc_xfail:
                grpc_marks.append(pytest.mark.xfail(*grpc_xfail.args, **grpc_xfail.kwargs))
            params.append(pytest.param("grpc_init_kwargs", marks=grpc_marks))

        metafunc.parametrize("init_kwargs", params, indirect=True)


@pytest.fixture(scope="function")
def system(init_kwargs) -> nidaqmx.system.System:
    """Gets system instance based on the grpc options."""
    if "grpc_options" in init_kwargs:
        return nidaqmx.system.System.remote(**init_kwargs)
    else:
        return nidaqmx.system.System.local(**init_kwargs)


def _x_series_device(
    device_type: DeviceType,
    system: nidaqmx.system.System,
    sampling_type: SamplingType = SamplingType.ANY,
    min_num_lines: int = 8,
) -> nidaqmx.system.Device:
    for device in system.devices:
        device_type_match = (
            device_type == DeviceType.ANY
            or (device_type == DeviceType.REAL and not device.is_simulated)
            or (device_type == DeviceType.SIMULATED and device.is_simulated)
        )
        device_type_match = device_type_match and (
            sampling_type == SamplingType.ANY
            or (
                sampling_type == SamplingType.MULTIPLEXED
                and not device.ai_simultaneous_sampling_supported
            )
            or (
                sampling_type == SamplingType.SIMULTANEOUS
                and device.ai_simultaneous_sampling_supported
            )
        )
        if (
            device_type_match
            and device.product_category == ProductCategory.X_SERIES_DAQ
            and len(device.ao_physical_chans) >= 2
            and len(device.ai_physical_chans) >= 4
            and len(device.do_lines) >= min_num_lines
            and len(device.di_lines) == len(device.do_lines)
            and len(device.ci_physical_chans) >= 4
        ):
            return device

    pytest.skip(
        "Could not detect a device that meets the requirements to be an X Series fixture of type "
        f"{device_type} with {sampling_type} sampling. Cannot proceed to run tests. Import the NI "
        "MAX configuration file located at nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to "
        "create these devices."
    )


def _device_by_product_type(
    product_type: str, device_type: DeviceType, system: nidaqmx.system.System
) -> nidaqmx.system.Device:
    for device in system.devices:
        device_type_match = (
            device_type == DeviceType.ANY
            or (device_type == DeviceType.REAL and not device.is_simulated)
            or (device_type == DeviceType.SIMULATED and device.is_simulated)
        )
        if device_type_match and device.product_type == product_type:
            return device

    pytest.skip(
        f"Could not detect a {product_type} device that meets the requirements to be of type "
        f"{device_type}. Cannot proceed to run tests. Import the NI MAX configuration file located "
        "at nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create these devices."
    )


def _cdaq_module_by_product_type(
    product_type: str, cdaq_chassis: nidaqmx.system.Device
) -> nidaqmx.system.Device:
    for module in cdaq_chassis.chassis_module_devices:
        if module.product_type == product_type:
            return module

    pytest.skip(
        f"Could not detect a {product_type} device within {cdaq_chassis.name}. "
        "Cannot proceed to run tests. Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create these devices."
    )


@pytest.fixture(scope="function")
def real_x_series_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets real X Series device information."""
    return _x_series_device(DeviceType.REAL, system)


@pytest.fixture(scope="function")
def real_x_series_device_32dio(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets real 32 DIO X Series device information."""
    return _x_series_device(
        DeviceType.REAL, system, sampling_type=SamplingType.ANY, min_num_lines=32
    )


@pytest.fixture(scope="function")
def real_x_series_multiplexed_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets device information for a real X Series device with multiplexed sampling."""
    return _x_series_device(DeviceType.REAL, system, sampling_type=SamplingType.MULTIPLEXED)


@pytest.fixture(scope="function")
def sim_4311_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets 4311 device information."""
    return _device_by_product_type("PXIe-4311", DeviceType.ANY, system)


@pytest.fixture(scope="function")
def sim_6363_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets simulated 6363 device information."""
    return _device_by_product_type("PCIe-6363", DeviceType.SIMULATED, system)


@pytest.fixture(scope="function")
def sim_6423_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets simulated 6423 device information."""
    return _device_by_product_type("USB-6423", DeviceType.SIMULATED, system)


@pytest.fixture(scope="function")
def sim_6535_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets simulated 6535 device information."""
    return _device_by_product_type("PCIe-6535", DeviceType.SIMULATED, system)


@pytest.fixture(scope="function")
def sim_9189_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets simulated 9185 device information."""
    return _device_by_product_type("cDAQ-9189", DeviceType.SIMULATED, system)


@pytest.fixture(scope="function")
def sim_9205_device(sim_9189_device: nidaqmx.system.Device) -> nidaqmx.system.Device:
    """Gets device information for a simulated 9205 device within a 9185."""
    return _cdaq_module_by_product_type("NI 9205", sim_9189_device)


@pytest.fixture(scope="function")
def sim_time_aware_9215_device(sim_9189_device: nidaqmx.system.Device) -> nidaqmx.system.Device:
    """Gets device information for a simulated 9215 device within a 9185."""
    return _cdaq_module_by_product_type("NI 9215", sim_9189_device)


@pytest.fixture(scope="function")
def sim_9263_device(sim_9189_device: nidaqmx.system.Device) -> nidaqmx.system.Device:
    """Gets device information for a simulated 9263 device within a 9185."""
    return _cdaq_module_by_product_type("NI 9263", sim_9189_device)


@pytest.fixture(scope="function")
def sim_9401_device(sim_9189_device: nidaqmx.system.Device) -> nidaqmx.system.Device:
    """Gets device information for a simulated 9401 device within a 9185."""
    return _cdaq_module_by_product_type("NI 9401", sim_9189_device)


@pytest.fixture(scope="function")
def sim_9775_device(sim_9189_device: nidaqmx.system.Device) -> nidaqmx.system.Device:
    """Gets device information for a simulated 9775 device within a 9185."""
    return _cdaq_module_by_product_type("NI 9775", sim_9189_device)


@pytest.fixture(scope="function")
def sim_ts_chassis(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets simulated TestScale chassis information."""
    # Prefer tsChassisTester if available so that multi-module tests will use
    # modules from the same chassis.
    if "tsChassisTester" in system.devices:
        return system.devices["tsChassisTester"]

    for device in system.devices:
        if device.is_simulated and device.product_category == ProductCategory.TEST_SCALE_CHASSIS:
            return device

    pytest.skip(
        "Could not detect a device that meets the requirements to be a TestScale simulated chassis. "
        "Cannot proceed to run tests. Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create these devices."
    )


@pytest.fixture(scope="function")
def sim_ts_power_device(sim_ts_chassis: nidaqmx.system.Device) -> nidaqmx.system.Device:
    """Gets simulated power device information."""
    for device in sim_ts_chassis.chassis_module_devices:
        if (
            device.is_simulated
            and device.product_category == ProductCategory.TEST_SCALE_MODULE
            and UsageTypeAI.POWER in device.ai_meas_types
        ):
            return device

    pytest.skip(
        "Could not detect a device that meets the requirements to be a TestScale simulated power device. "
        "Cannot proceed to run tests. Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create these devices."
    )


@pytest.fixture(scope="function")
def sim_ts_voltage_device(sim_ts_chassis: nidaqmx.system.Device) -> nidaqmx.system.Device:
    """Gets simulated voltage device information."""
    for device in sim_ts_chassis.chassis_module_devices:
        if (
            device.is_simulated
            and device.product_category == ProductCategory.TEST_SCALE_MODULE
            and UsageTypeAI.VOLTAGE in device.ai_meas_types
        ):
            return device

    pytest.skip(
        "Could not detect a device that meets the requirements to be a TestScale simulated voltage device. "
        "Cannot proceed to run tests. Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create these devices."
    )


@pytest.fixture(scope="function")
def sim_ts_power_devices(sim_ts_chassis: nidaqmx.system.Device) -> list[nidaqmx.system.Device]:
    """Gets simulated power devices information."""
    devices = []
    for device in sim_ts_chassis.chassis_module_devices:
        if (
            device.is_simulated
            and device.product_category == ProductCategory.TEST_SCALE_MODULE
            and UsageTypeAI.POWER in device.ai_meas_types
        ):
            devices.append(device)
            if len(devices) == 2:
                return devices

    pytest.skip(
        "Could not detect two or more devices that meets the requirements to be a TestScale simulated power "
        "device. Cannot proceed to run tests. Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create these devices."
    )


@pytest.fixture(scope="function")
def sim_charge_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets a simulated 4480."""
    return _device_by_product_type("PXIe-4480", DeviceType.SIMULATED, system)


@pytest.fixture(scope="function")
def sim_dsa_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets a simulated 4466."""
    return _device_by_product_type("PXIe-4466", DeviceType.SIMULATED, system)


@pytest.fixture(scope="function")
def sim_dmm_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets a simulated myDAQ."""
    return _device_by_product_type("NI myDAQ", DeviceType.SIMULATED, system)


@pytest.fixture(scope="function")
def sim_bridge_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets a simulated 4431."""
    return _device_by_product_type("PXIe-4331", DeviceType.SIMULATED, system)


@pytest.fixture(scope="function")
def sim_position_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets a simulated 4340."""
    return _device_by_product_type("PXIe-4340", DeviceType.SIMULATED, system)


@pytest.fixture(scope="function")
def sim_temperature_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets a simulated 4353."""
    return _device_by_product_type("PXIe-4353", DeviceType.SIMULATED, system)


@pytest.fixture(scope="function")
def sim_velocity_device(system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets a simulated 9361."""
    return _device_by_product_type("NI 9361", DeviceType.SIMULATED, system)


@pytest.fixture(scope="function")
def multi_threading_test_devices(system: nidaqmx.system.System) -> list[nidaqmx.system.Device]:
    """Gets multi threading test devices information."""
    devices = []
    for device in system.devices:
        if (
            device.is_simulated
            and device.product_category == ProductCategory.X_SERIES_DAQ
            and len(device.ai_physical_chans) >= 1
        ):
            devices.append(device)
            if len(devices) == 4:
                return devices

    pytest.skip(
        "Could not detect 4 simulated X Series devices for multithreading tests.  Cannot proceed "
        "to run tests. Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create these devices."
    )


@pytest.fixture(scope="function")
def device(request, system: nidaqmx.system.System) -> nidaqmx.system.Device:
    """Gets the device information based on the device name."""
    device_name = _get_marker_value(request, "device_name")
    for device in system.devices:
        if device.name == device_name:
            return device

    pytest.skip(
        "Could not detect a device that has the given name. Cannot proceed to run tests. "
        "Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create these devices."
    )


@pytest.fixture(scope="session")
def test_assets_directory() -> pathlib.Path:
    """Gets path to test_assets directory."""
    return pathlib.Path(__file__).parent / "test_assets"


@pytest.fixture(scope="session")
def grpc_server_process() -> Generator[GrpcServerProcess]:
    """Gets the grpc server process."""
    if grpc is None:
        pytest.skip("The grpc module is not available.")
    with GrpcServerProcess() as proc:
        yield proc


@pytest.fixture(scope="function")
def grpc_channel(request: pytest.FixtureRequest) -> grpc.Channel:
    """Gets a gRPC channel."""
    if request.node.get_closest_marker("temporary_grpc_channel") is not None:
        return request.getfixturevalue("temporary_grpc_channel")
    else:
        return request.getfixturevalue("shared_grpc_channel")


@pytest.fixture(scope="session")
def shared_grpc_channel(
    grpc_server_process: GrpcServerProcess,
) -> Generator[grpc.Channel]:
    """Gets the shared gRPC channel."""
    with grpc.insecure_channel(f"localhost:{grpc_server_process.server_port}") as channel:
        yield channel


@pytest.fixture(scope="function")
def temporary_grpc_channel(
    request: pytest.FixtureRequest, grpc_server_process: GrpcServerProcess
) -> Generator[grpc.Channel]:
    """Gets a temporary gRPC channel (not shared with other tests)."""
    marker = request.node.get_closest_marker("temporary_grpc_channel")
    options = marker.kwargs.get("options", None)
    with grpc.insecure_channel(f"localhost:{grpc_server_process.server_port}", options) as channel:
        yield channel


@pytest.fixture(scope="function")
def grpc_init_kwargs(request: pytest.FixtureRequest, grpc_channel: grpc.Channel) -> dict:
    """Gets the keyword arguments required for creating the gRPC interpreter."""
    session_name = _get_marker_value(request, "grpc_session_name", "")
    initialization_behavior = _get_marker_value(
        request, "grpc_session_initialization_behavior", nidaqmx.SessionInitializationBehavior.AUTO
    )
    grpc_options = nidaqmx.GrpcSessionOptions(
        grpc_channel=grpc_channel,
        session_name=session_name,
        initialization_behavior=initialization_behavior,
    )
    return {"grpc_options": grpc_options}


@pytest.fixture(scope="function")
def library_init_kwargs():
    """Gets the keyword arguments required for creating the library interpreter."""
    return {}


@pytest.fixture(scope="function")
def init_kwargs(request):
    """Gets the keyword arguments to create a nidaqmx session."""
    return request.getfixturevalue(request.param)


@pytest.fixture(scope="function")
def task(request, generate_task) -> nidaqmx.Task:
    """Gets a task instance.

    The closure of task objects will be done by this fixture once the test is complete.
    This fixture owns the task. Do not use it for test cases that destroy the task, or else you
    may get double-close warnings.
    """
    new_task_name = _get_marker_value(request, "new_task_name", "")
    return generate_task(task_name=new_task_name)


@pytest.fixture(scope="function")
def generate_task(init_kwargs) -> Generator[Callable[..., nidaqmx.Task]]:
    """Gets a factory function which can be used to generate new tasks.

    The closure of task objects will be done by this fixture once the test is complete.
    This fixture owns the task. Do not use it for test cases that destroy the task, or else you
    may get double-close warnings.
    """
    with contextlib.ExitStack() as stack:

        def _create_task(task_name: str = ""):
            return stack.enter_context(nidaqmx.Task(new_task_name=task_name, **init_kwargs))

        yield _create_task


@pytest.fixture(scope="function")
def persisted_task(request, system: nidaqmx.system.System) -> nidaqmx.system.storage.PersistedTask:
    """Gets the persisted task based on the task name."""
    task_name = _get_marker_value(request, "task_name")

    if task_name in system.tasks.task_names:
        return system.tasks[task_name]

    pytest.skip(
        "Could not detect a persisted task that has the given name."
        "Cannot proceed to run tests. Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create the required tasks."
    )


@pytest.fixture(scope="function")
def persisted_scale(
    request, system: nidaqmx.system.System
) -> nidaqmx.system.storage.PersistedScale:
    """Gets the persisted scale based on the scale name."""
    scale_name = _get_marker_value(request, "scale_name")
    if scale_name in system.scales:
        return system.scales[scale_name]
    pytest.skip(
        "Could not detect a persisted scale with the requested scale name.  Cannot proceed "
        "to run tests. Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create the required scales."
    )


@pytest.fixture(scope="function")
def persisted_channel(
    request, system: nidaqmx.system.System
) -> nidaqmx.system.storage.PersistedChannel:
    """Gets the persisted channel based on the channel name."""
    channel_name = _get_marker_value(request, "channel_name")

    if channel_name in system.global_channels.global_channel_names:
        return system.global_channels[channel_name]

    pytest.skip(
        "Could not detect a global channel that has the given name."
        "Cannot proceed to run tests. Import the NI MAX configuration file located at "
        "nidaqmx\\tests\\max_config\\nidaqmxMaxConfig.ini to create the required channels."
    )


@pytest.fixture(scope="function")
def watchdog_task(request, sim_6363_device, generate_watchdog_task) -> nidaqmx.system.WatchdogTask:
    """Gets a watchdog task instance."""
    # set default values used for the initialization of the task.
    device_name = _get_marker_value(request, "device_name", sim_6363_device.name)
    timeout = _get_marker_value(request, "timeout", 0.5)

    return generate_watchdog_task(device_name=device_name, timeout=timeout)


@pytest.fixture(scope="function")
def generate_watchdog_task(
    init_kwargs,
) -> Generator[Callable[..., nidaqmx.system.WatchdogTask]]:
    """Gets a factory function which can be used to generate new watchdog tasks.

    The closure of task objects will be done by this fixture once the test is complete.
    This fixture owns the task. Do not use it for test cases that destroy the task, or else you
    may get double-close warnings.
    """
    with contextlib.ExitStack() as stack:

        def _create_task(device_name: str, task_name: str = "", timeout: float = 0.5):
            return stack.enter_context(
                nidaqmx.system.WatchdogTask(device_name, task_name, timeout, **init_kwargs)
            )

        yield _create_task


def _get_marker_value(request, marker_name, default=None):
    """Gets the value of a pytest marker based on the marker name."""
    marker_value = default
    for marker in request.node.iter_markers():
        if marker.name == marker_name:  # only look at markers with valid argument name
            marker_value = marker.args[0]  # assume single parameter in marker

    return marker_value


@pytest.fixture(scope="function")
def thread_pool_executor() -> Generator[ThreadPoolExecutor]:
    """Creates a thread pool executor.

    When the test completes, this fixture shuts down the thread pool executor. If any futures are
    still running at this time, shutting down the thread pool executor will wait for them to
    complete.
    """
    with ThreadPoolExecutor() as executor:
        yield executor


@pytest.fixture
def interpreter(system: nidaqmx.system.System) -> BaseInterpreter:
    """Gets an interpreter."""
    return system._interpreter


@pytest.fixture
def teds_assets_directory(test_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns the path to TEDS assets."""
    return test_assets_directory / "teds"


@pytest.fixture
def voltage_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "Voltage.ted"


@pytest.fixture
def accelerometer_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "Accelerometer.ted"


@pytest.fixture
def bridge_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    # Our normal bridge sensor TEDS file is incompatible with most devices. It
    # has a 1ohm bridge resistance.
    return teds_assets_directory / "ForceBridge.ted"


@pytest.fixture
def force_bridge_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "ForceBridge.ted"


@pytest.fixture
def current_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "Current.ted"


@pytest.fixture
def force_iepe_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "ForceSensor.ted"


@pytest.fixture
def microphone_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "Microphone.ted"


@pytest.fixture
def lvdt_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "LVDT.ted"


@pytest.fixture
def rvdt_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "RVDT.ted"


@pytest.fixture
def pressure_bridge_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "PressureBridge.ted"


@pytest.fixture
def torque_bridge_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "TorqueBridge.ted"


@pytest.fixture
def resistance_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "Resistance.ted"


@pytest.fixture
def rtd_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "TempRTD.ted"


@pytest.fixture
def strain_gage_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "StrainGage.ted"


@pytest.fixture
def thermocouple_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "TempTC.ted"


@pytest.fixture
def thermistor_iex_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "ThermistorIex.ted"


@pytest.fixture
def thermistor_vex_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path:
    """Returns a TEDS file path."""
    return teds_assets_directory / "ThermistorVex.ted"


@pytest.fixture
def feature_toggles(monkeypatch: pytest.MonkeyPatch, request: pytest.FixtureRequest) -> None:
    """Test fixture that disables or enables feature toggles."""
    for mark in request.node.iter_markers():
        if mark.name in ["disable_feature_toggle", "enable_feature_toggle"]:
            feature_toggle = mark.args[0]
            assert isinstance(feature_toggle, FeatureToggle)
            monkeypatch.setattr(
                feature_toggle, "_is_enabled_override", mark.name == "enable_feature_toggle"
            )
        elif mark.name == "use_code_readiness":
            code_readiness = mark.args[0]
            assert isinstance(code_readiness, CodeReadiness)
            monkeypatch.setattr(_feature_toggles, "_CODE_READINESS_LEVEL", code_readiness)


def pytest_collection_modifyitems(items: list[pytest.Item]) -> None:
    """Hook to inject fixtures based on marks."""
    # By default, all features are enabled when running tests.
    _feature_toggles._CODE_READINESS_LEVEL = CodeReadiness.PROTOTYPE

    for item in items:
        if (
            item.get_closest_marker("disable_feature_toggle")
            or item.get_closest_marker("enable_feature_toggle")
            or item.get_closest_marker("use_code_readiness")
        ):
            assert hasattr(item, "fixturenames")
            item.fixturenames.append("feature_toggles")
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/helpers.py sha256=5a328c1e1c9c48a0c5cd45d68c2f9a74e7300cec8207e7b491b9821f91065e3f bytes=1030 -->
## FILE: tests/helpers.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/helpers.py`
- sha256: `5a328c1e1c9c48a0c5cd45d68c2f9a74e7300cec8207e7b491b9821f91065e3f`
- bytes: 1030

````python
"""This contains the helpers methods used in the DAQmx tests."""

from __future__ import annotations

import contextlib
import pathlib
from collections.abc import Generator

from nidaqmx.system.physical_channel import PhysicalChannel

# Power uses fixed-point scaling, so we have a pretty wide epsilon.
POWER_ABS_EPSILON = 1e-3


def generate_random_seed():
    """Creates a random integer."""
    # Randomizing the random seed makes the GitHub test reporting action
    # (EnricoMi/publish-unit-test-result-action) report many added/removed
    # tests, so use the same random seed every time.
    return 42


@contextlib.contextmanager
def configure_teds(
    phys_chan: PhysicalChannel, teds_file_path: str | pathlib.PurePath | None = None
) -> Generator[PhysicalChannel]:
    """Yields a physical channel with TEDS configured and then clears it after the test is done."""
    phys_chan.configure_teds(teds_file_path)
    try:
        yield phys_chan
    finally:
        phys_chan.clear_teds()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/legacy/__init__.py sha256=b82ab2cc54acf7b0145b4abb9c7ebc415f4a6fd2b9e0f1511ef7fb397cf301ac bytes=72 -->
## FILE: tests/legacy/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/legacy/__init__.py`
- sha256: `b82ab2cc54acf7b0145b4abb9c7ebc415f4a6fd2b9e0f1511ef7fb397cf301ac`
- bytes: 72

````python
"""Legacy tests that do not follow NI's Python testing conventions."""
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/legacy/test_channel_creation.py sha256=d75d7756e624bd76dc9f260f8e64a2be9f3179b01ebd15670ea869319798b1cb bytes=15127 -->
## FILE: tests/legacy/test_channel_creation.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/legacy/test_channel_creation.py`
- sha256: `d75d7756e624bd76dc9f260f8e64a2be9f3179b01ebd15670ea869319798b1cb`
- bytes: 15127

````python
"""Tests for creating channels."""

import random

import numpy
import pytest

from nidaqmx import constants
from nidaqmx.constants import (
    BridgeConfiguration,
    CurrentShuntResistorLocation,
    CurrentUnits,
    ExcitationSource,
    ResistanceConfiguration,
    ResistanceUnits,
    RTDType,
    StrainGageBridgeType,
    StrainUnits,
    TemperatureUnits,
    TerminalConfiguration,
    VoltageUnits,
)
from tests.helpers import generate_random_seed


class TestAnalogCreateChannels:
    """Contains a collection of pytest tests.

    These validate the analog Create Channel functions in the NI-DAQmx Python API.
    These tests simply call create channel functions with some valid values
    for function parameters, and then read properties to verify that the
    parameter values were set properly.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_create_ai_voltage_chan(self, task, sim_6363_device, seed):
        """Test for creating AI voltage channel."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chan = random.choice(sim_6363_device.ai_physical_chans).name

        ai_channel = task.ai_channels.add_ai_voltage_chan(
            ai_phys_chan,
            name_to_assign_to_channel="VoltageChannel",
            terminal_config=TerminalConfiguration.NRSE,
            min_val=-20.0,
            max_val=20.0,
            units=VoltageUnits.FROM_CUSTOM_SCALE,
            custom_scale_name="double_gain_scale",
        )

        assert ai_channel.physical_channel.name == ai_phys_chan
        assert ai_channel.name == "VoltageChannel"
        assert ai_channel.ai_term_cfg == TerminalConfiguration.NRSE
        assert ai_channel.ai_min == -20.0
        assert ai_channel.ai_max == 20.0
        assert ai_channel.ai_voltage_units == VoltageUnits.FROM_CUSTOM_SCALE
        assert ai_channel.ai_custom_scale.name == "double_gain_scale"

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_create_ai_current_chan(self, task, sim_6363_device, seed):
        """Test for creating AI current channel."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chan = random.choice(sim_6363_device.ai_physical_chans).name

        ai_channel = task.ai_channels.add_ai_current_chan(
            ai_phys_chan,
            name_to_assign_to_channel="CurrentChannel",
            terminal_config=TerminalConfiguration.RSE,
            min_val=-0.01,
            max_val=0.01,
            units=CurrentUnits.AMPS,
            shunt_resistor_loc=CurrentShuntResistorLocation.EXTERNAL,
            ext_shunt_resistor_val=100.0,
        )

        assert ai_channel.physical_channel.name == ai_phys_chan
        assert ai_channel.name == "CurrentChannel"
        assert ai_channel.ai_term_cfg == TerminalConfiguration.RSE
        assert ai_channel.ai_min == -0.01
        assert ai_channel.ai_max == 0.01
        assert ai_channel.ai_current_units == CurrentUnits.AMPS
        assert ai_channel.ai_current_shunt_loc == CurrentShuntResistorLocation.EXTERNAL
        assert ai_channel.ai_current_shunt_resistance == 100.0

    # @pytest.mark.parametrize('seed', [generate_random_seed()])
    # def test_create_ai_voltage_rms_chan(self, task, sim_6363_device, seed):
    #     # Reset the pseudorandom number generator with seed.
    #     random.seed(seed)
    #
    #     ai_phys_chan = random.choice(sim_6363_device.ai_physical_chans).name
    #
    #     ai_channel = task.ai_channels.add_ai_voltage_rms_chan(
    #         ai_phys_chan, name_to_assign_to_channel="VoltageRMSChannel",
    #         terminal_config=TerminalConfiguration.bal_diff, min_val=-1.0,
    #         max_val=1.0, units=VoltageUnits.volts, custom_scale_name="")
    #
    #     assert ai_channel.name == "VoltageRMSChannel"
    #     assert ai_channel.ai_term_cfg == TerminalConfiguration.bal_diff
    #     assert ai_channel.ai_min == -1.0
    #     assert ai_channel.ai_max == 1.0
    #     assert ai_channel.ai_voltage_units == VoltageUnits.volts
    #     assert ai_channel.ai_custom_scale.name == ""

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_create_ai_rtd_chan(self, task, sim_6363_device, seed):
        """Test for creating AI RTD channel."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chan = random.choice(sim_6363_device.ai_physical_chans).name

        ai_channel = task.ai_channels.add_ai_rtd_chan(
            ai_phys_chan,
            name_to_assign_to_channel="RTDChannel",
            min_val=28.0,
            max_val=120.0,
            units=TemperatureUnits.K,
            rtd_type=RTDType.PT_3750,
            resistance_config=ResistanceConfiguration.TWO_WIRE,
            current_excit_source=ExcitationSource.EXTERNAL,
            current_excit_val=0.0025,
            r_0=100.0,
        )

        assert ai_channel.physical_channel.name == ai_phys_chan
        assert ai_channel.name == "RTDChannel"
        assert numpy.isclose(ai_channel.ai_min, 28.0, atol=1)
        assert numpy.isclose(ai_channel.ai_max, 221.0, atol=1)
        assert ai_channel.ai_temp_units == TemperatureUnits.K
        assert ai_channel.ai_rtd_type == RTDType.PT_3750
        assert ai_channel.ai_resistance_cfg == ResistanceConfiguration.TWO_WIRE
        assert ai_channel.ai_excit_src == ExcitationSource.EXTERNAL
        assert ai_channel.ai_excit_val == 0.0025
        assert ai_channel.ai_rtd_r0 == 100.0

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_create_ai_thrmstr_chan_iex(self, task, sim_6363_device, seed):
        """Test for creating AI thermistor channel with current excitation."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chan = random.choice(sim_6363_device.ai_physical_chans).name

        ai_channel = task.ai_channels.add_ai_thrmstr_chan_iex(
            ai_phys_chan,
            name_to_assign_to_channel="ThermistorIexChannel",
            min_val=-30.0,
            max_val=300.0,
            units=TemperatureUnits.DEG_C,
            resistance_config=ResistanceConfiguration.FOUR_WIRE,
            current_excit_source=ExcitationSource.EXTERNAL,
            current_excit_val=0.0001,
            a=0.0013,
            b=0.00023,
            c=0.000000102,
        )

        assert ai_channel.physical_channel.name == ai_phys_chan
        assert ai_channel.name == "ThermistorIexChannel"
        assert numpy.isclose(ai_channel.ai_min, -30.0, atol=1)
        assert numpy.isclose(ai_channel.ai_max, 300.0, atol=1)
        assert ai_channel.ai_temp_units == TemperatureUnits.DEG_C
        assert ai_channel.ai_resistance_cfg == ResistanceConfiguration.FOUR_WIRE
        assert ai_channel.ai_excit_src == ExcitationSource.EXTERNAL
        assert ai_channel.ai_excit_val == 0.0001

        assert ai_channel.ai_thrmstr_a == 0.0013
        assert ai_channel.ai_thrmstr_b == 0.00023
        assert ai_channel.ai_thrmstr_c == 0.000000102

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_create_ai_thrmstr_chan_vex(self, task, sim_6363_device, seed):
        """Test for creating AI thermistor channel with voltage excitation."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chan = random.choice(sim_6363_device.ai_physical_chans).name

        ai_channel = task.ai_channels.add_ai_thrmstr_chan_vex(
            ai_phys_chan,
            name_to_assign_to_channel="ThermistorVexChannel",
            min_val=-50.0,
            max_val=300.0,
            units=TemperatureUnits.DEG_C,
            resistance_config=ResistanceConfiguration.FOUR_WIRE,
            voltage_excit_source=ExcitationSource.EXTERNAL,
            voltage_excit_val=2.5,
            a=0.001295361,
            b=0.0002343159,
            c=0.0000001018703,
            r_1=5000.0,
        )

        assert ai_channel.physical_channel.name == ai_phys_chan
        assert ai_channel.name == "ThermistorVexChannel"
        assert numpy.isclose(ai_channel.ai_min, -50.0, atol=1)
        assert numpy.isclose(ai_channel.ai_max, 300.0, atol=1)
        assert ai_channel.ai_temp_units == TemperatureUnits.DEG_C
        assert ai_channel.ai_resistance_cfg == ResistanceConfiguration.FOUR_WIRE
        assert ai_channel.ai_excit_src == ExcitationSource.EXTERNAL
        assert ai_channel.ai_excit_val == 2.5

        assert ai_channel.ai_thrmstr_a == 0.001295361
        assert ai_channel.ai_thrmstr_b == 0.0002343159
        assert ai_channel.ai_thrmstr_c == 0.0000001018703
        assert ai_channel.ai_thrmstr_r1 == 5000.0

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_create_ai_resistance_chan(self, task, sim_6363_device, seed):
        """Test for creating AI resistance channel."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chan = random.choice(sim_6363_device.ai_physical_chans).name

        # Note: 1000 ohms @ 5 mA = 5V range, which exists on most X Series devices.
        ai_channel = task.ai_channels.add_ai_resistance_chan(
            ai_phys_chan,
            name_to_assign_to_channel="ResistanceChannel",
            min_val=-1000.0,
            max_val=1000.0,
            units=ResistanceUnits.OHMS,
            resistance_config=ResistanceConfiguration.TWO_WIRE,
            current_excit_source=ExcitationSource.EXTERNAL,
            current_excit_val=0.005,
            custom_scale_name="",
        )

        assert ai_channel.physical_channel.name == ai_phys_chan
        assert ai_channel.name == "ResistanceChannel"
        assert numpy.isclose(ai_channel.ai_min, -1000.0, atol=1)
        assert numpy.isclose(ai_channel.ai_max, 1000.0, atol=1)
        assert ai_channel.ai_resistance_units == ResistanceUnits.OHMS
        assert ai_channel.ai_resistance_cfg == ResistanceConfiguration.TWO_WIRE
        assert ai_channel.ai_excit_src == ExcitationSource.EXTERNAL
        assert ai_channel.ai_excit_val == 0.005

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_ai_strain_gage_chan(self, task, sim_6363_device, seed):
        """Test for creating AI strain gage channel."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chan = random.choice(sim_6363_device.ai_physical_chans).name

        ai_channel = task.ai_channels.add_ai_strain_gage_chan(
            ai_phys_chan,
            name_to_assign_to_channel="StrainGageChannel",
            min_val=-0.05,
            max_val=0.05,
            units=StrainUnits.STRAIN,
            strain_config=StrainGageBridgeType.FULL_BRIDGE_I,
            voltage_excit_source=ExcitationSource.EXTERNAL,
            voltage_excit_val=1.0,
            gage_factor=4.0,
            initial_bridge_voltage=0.0,
            nominal_gage_resistance=350.0,
            poisson_ratio=0.30,
            lead_wire_resistance=0.1,
            custom_scale_name="",
        )

        assert ai_channel.physical_channel.name == ai_phys_chan
        assert ai_channel.name == "StrainGageChannel"
        assert numpy.isclose(ai_channel.ai_min, -0.05)
        assert numpy.isclose(ai_channel.ai_max, 0.05)
        assert ai_channel.ai_strain_units == StrainUnits.STRAIN
        assert ai_channel.ai_strain_gage_cfg == StrainGageBridgeType.FULL_BRIDGE_I
        assert ai_channel.ai_excit_src == ExcitationSource.EXTERNAL
        assert ai_channel.ai_excit_val == 1.0
        assert ai_channel.ai_strain_gage_gage_factor == 4.0
        assert ai_channel.ai_bridge_initial_voltage == 0.0
        assert ai_channel.ai_strain_gage_poisson_ratio == 0.30
        assert ai_channel.ai_lead_wire_resistance == 0.1

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_create_ai_voltage_chan_with_excit(self, task, sim_6363_device, seed):
        """Test for creating AI voltage channel."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chan = random.choice(sim_6363_device.ai_physical_chans).name

        ai_channel = task.ai_channels.add_ai_voltage_chan_with_excit(
            ai_phys_chan,
            name_to_assign_to_channel="VoltageExcitChannel",
            terminal_config=TerminalConfiguration.NRSE,
            min_val=-10.0,
            max_val=10.0,
            units=VoltageUnits.VOLTS,
            bridge_config=BridgeConfiguration.NO_BRIDGE,
            voltage_excit_source=ExcitationSource.EXTERNAL,
            voltage_excit_val=0.1,
            use_excit_for_scaling=False,
            custom_scale_name="",
        )

        assert ai_channel.physical_channel.name == ai_phys_chan
        assert ai_channel.name == "VoltageExcitChannel"
        assert ai_channel.ai_term_cfg == TerminalConfiguration.NRSE
        assert numpy.isclose(ai_channel.ai_min, -10.0)
        assert numpy.isclose(ai_channel.ai_max, 10.0)
        assert ai_channel.ai_voltage_units == VoltageUnits.VOLTS
        assert ai_channel.ai_bridge_cfg == BridgeConfiguration.NO_BRIDGE
        assert ai_channel.ai_excit_src == ExcitationSource.EXTERNAL
        assert ai_channel.ai_excit_val == 0.1
        assert not ai_channel.ai_excit_use_for_scaling

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_create_ai_power_chan(self, task, sim_ts_power_device, seed):
        """Test for creating AI power channel."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        pwr_phys_chan = f"{sim_ts_power_device.name}/power"
        voltage_setpoint = random.random() * 6.0
        current_setpoint = random.uniform(0.03, 3.0)
        output_enable = random.choice([True, False])
        # CPLD is fixed-point, so values are coerced to something close.
        setpoint_tolerance = 1e-03

        pwr_channel = task.ai_channels.add_ai_power_chan(
            pwr_phys_chan,
            voltage_setpoint,
            current_setpoint,
            output_enable,
            name_to_assign_to_channel="PowerChannel",
        )

        assert pwr_channel.physical_channel.name == pwr_phys_chan
        assert pwr_channel.name == "PowerChannel"
        assert numpy.isclose(
            pwr_channel.pwr_voltage_setpoint, voltage_setpoint, atol=setpoint_tolerance
        )
        assert numpy.isclose(
            pwr_channel.pwr_current_setpoint, current_setpoint, atol=setpoint_tolerance
        )
        assert pwr_channel.pwr_output_enable == output_enable
        assert (
            pwr_channel.pwr_idle_output_behavior
            == constants.PowerIdleOutputBehavior.MAINTAIN_EXISTING_VALUE
        )
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/legacy/test_channels.py sha256=94d5ae4778d0037d527e5ce5e36a50023e5cc5b07a3d9d98c6c31c00c5afe096 bytes=2099 -->
## FILE: tests/legacy/test_channels.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/legacy/test_channels.py`
- sha256: `94d5ae4778d0037d527e5ce5e36a50023e5cc5b07a3d9d98c6c31c00c5afe096`
- bytes: 2099

````python
"""Tests for validating the channel objects."""

import numpy

from nidaqmx.constants import TaskMode


class TestChannels:
    """Contains a collection of pytest tests.

    This validate the channel objects in the NI-DAQmx Python API.
    """

    def test_ai_channel(self, task, sim_6363_device):
        """Tests for creating ai channel."""
        ai_channel = task.ai_channels.add_ai_voltage_chan(
            sim_6363_device.ai_physical_chans[0].name, max_val=10
        )

        # Test property default value.
        assert ai_channel.ai_max == 10

    def test_ao_channel(self, task, sim_6363_device):
        """Tests for creating ao channel."""
        ao_channel = task.ao_channels.add_ao_voltage_chan(
            sim_6363_device.ao_physical_chans[0].name, max_val=5
        )

        # Test property default value.
        assert ao_channel.ao_max == 5

    def test_ci_channel(self, task, real_x_series_device):
        """Tests for creating ci channel."""
        ci_channel = task.ci_channels.add_ci_count_edges_chan(
            real_x_series_device.ci_physical_chans[0].name, initial_count=10
        )

        task.control(TaskMode.TASK_COMMIT)

        assert ci_channel.ci_count == 10

    def test_co_channel(self, task, sim_6363_device):
        """Tests for creating co channel."""
        co_channel = task.co_channels.add_co_pulse_chan_freq(
            sim_6363_device.co_physical_chans[0].name, freq=5000
        )

        task.control(TaskMode.TASK_COMMIT)

        numpy.testing.assert_allclose([co_channel.co_pulse_freq], [5000], rtol=0.05)

    def test_di_channel(self, task, sim_6363_device):
        """Tests for creating di channel."""
        di_channel = task.di_channels.add_di_chan(sim_6363_device.di_lines[0].name)

        assert di_channel.di_num_lines == 1

    def test_do_channel(self, task, sim_6363_device):
        """Tests for creating do channel."""
        do_channel = task.do_channels.add_do_chan(sim_6363_device.do_lines[0].name)

        assert do_channel.do_num_lines == 1
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/legacy/test_container_operations.py sha256=8ae78cdbc28c208ec157156208606a47982103635970672adbe513a04c8c296c bytes=4245 -->
## FILE: tests/legacy/test_container_operations.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/legacy/test_container_operations.py`
- sha256: `8ae78cdbc28c208ec157156208606a47982103635970672adbe513a04c8c296c`
- bytes: 4245

````python
"""Tests for validating the container operations."""

import random

import pytest

from nidaqmx.utils import flatten_channel_string
from tests.helpers import generate_random_seed


class TestContainerOperations:
    """Contains a collection of pytest tests.

    This validate the container operations in the Python NI-DAQmx API.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_concatenate_operations(self, task, sim_6363_device, seed):
        """Test for concatenate operation."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chans = random.sample(sim_6363_device.ai_physical_chans, 2)

        ai_channel_1 = task.ai_channels.add_ai_voltage_chan(
            ai_phys_chans[0].name, max_val=5, min_val=-5
        )

        ai_channel_2 = task.ai_channels.add_ai_voltage_chan(
            ai_phys_chans[1].name, max_val=5, min_val=-5
        )

        # Concatenate two channels.
        ai_channel = ai_channel_1 + ai_channel_2

        # Test that concatenated channel name has flattened value of the
        # individual channel names.
        assert ai_channel.name == flatten_channel_string(
            [ai_phys_chans[0].name, ai_phys_chans[1].name]
        )

        # Test that setting property on concatenated channel changes the
        # property values of the individual channels.
        ai_channel.ai_max = 10
        assert ai_channel_1.ai_max == 10
        assert ai_channel_2.ai_max == 10

        # Concatenate two channels.
        ai_channel_1 += ai_channel_2

        # Test that concatenated channel name has flattened value of the
        # individual channel names.
        assert ai_channel_1.name == flatten_channel_string(
            [ai_phys_chans[0].name, ai_phys_chans[1].name]
        )

        # Test that setting property on concatenated channel changes the
        # property values of the individual channels.
        # Note: 0.2V range exists on most X Series devices.
        ai_channel_1.ai_max = 0.2
        ai_channel_1.ai_min = -0.2
        assert ai_channel_2.ai_max == 0.2
        assert ai_channel_2.ai_min == -0.2

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_equality_operations(self, task, sim_6363_device, seed):
        """Test for equality operation."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chans = random.sample(sim_6363_device.ai_physical_chans, 2)

        ai_channel_1 = task.ai_channels.add_ai_voltage_chan(
            ai_phys_chans[0].name, max_val=5, min_val=-5
        )
        ai_channel_2 = task.ai_channels.add_ai_voltage_chan(
            ai_phys_chans[1].name, max_val=5, min_val=-5
        )

        assert ai_channel_1 == task.ai_channels[0]
        assert ai_channel_1 == task.ai_channels[ai_phys_chans[0].name]
        assert ai_channel_1 != ai_channel_2

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_hash_operations(self, generate_task, sim_6363_device, seed):
        """Test for hash operation."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_phys_chans = random.sample(sim_6363_device.ai_physical_chans, 3)
        task_1 = generate_task()
        task_2 = generate_task()
        ai_channel_1 = task_1.ai_channels.add_ai_voltage_chan(
            ai_phys_chans[0].name,
            name_to_assign_to_channel="VoltageChannel",
            max_val=5,
            min_val=-5,
        )
        ai_channel_2 = task_1.ai_channels.add_ai_voltage_chan(
            ai_phys_chans[1].name, max_val=5, min_val=-5
        )

        ai_channel_3 = task_2.ai_channels.add_ai_voltage_chan(
            ai_phys_chans[2].name,
            name_to_assign_to_channel="VoltageChannel",
            max_val=5,
            min_val=-5,
        )

        assert hash(ai_channel_1) == hash(task_1.ai_channels[0])
        assert hash(ai_channel_1) != hash(ai_channel_2)
        assert hash(task_1.ai_channels) != hash(task_2.ai_channels)
        assert hash(ai_channel_1) != hash(ai_channel_3)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/legacy/test_enum_bitfields.py sha256=d9e514c4094bcb6722423fa44dc8ac9d0174067c48e79e4458c28dce9316ab0d bytes=2667 -->
## FILE: tests/legacy/test_enum_bitfields.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/legacy/test_enum_bitfields.py`
- sha256: `d9e514c4094bcb6722423fa44dc8ac9d0174067c48e79e4458c28dce9316ab0d`
- bytes: 2667

````python
"""Tests for validating the bitfield enums."""

from functools import partial

from nidaqmx._bitfield_utils import enum_bitfield_to_list, enum_list_to_bitfield
from nidaqmx.constants import (
    Coupling,
    TerminalConfiguration,
    TriggerUsage,
    _CouplingTypes,
    _TermCfg,
    _TriggerUsageTypes,
)


def test_coupling_bitfield():
    """Test for coupling bitfield."""
    _convert_from = partial(
        enum_bitfield_to_list, bitfield_enum_type=_CouplingTypes, actual_enum_type=Coupling
    )
    _convert_to = partial(enum_list_to_bitfield, bitfield_enum_type=_CouplingTypes)

    bitfield_value = _CouplingTypes.AC.value + _CouplingTypes.DC.value + _CouplingTypes.GND.value
    expected_bitfield_list = [Coupling.AC, Coupling.DC, Coupling.GND]
    assert _convert_from(bitfield_value) == expected_bitfield_list
    assert _convert_to(expected_bitfield_list) == bitfield_value


def test_terminal_configuration_bitfield():
    """Test for terminal configuration bitfield."""
    _convert_from = partial(
        enum_bitfield_to_list, bitfield_enum_type=_TermCfg, actual_enum_type=TerminalConfiguration
    )
    _convert_to = partial(enum_list_to_bitfield, bitfield_enum_type=_TermCfg)

    bitfield_value = (
        _TermCfg.RSE.value + _TermCfg.NRSE.value + _TermCfg.DIFF.value + _TermCfg.PSEUDO_DIFF.value
    )
    expected_bitfield_list = [
        TerminalConfiguration.RSE,
        TerminalConfiguration.NRSE,
        TerminalConfiguration.DIFF,
        TerminalConfiguration.PSEUDO_DIFF,
    ]
    assert _convert_from(bitfield_value) == expected_bitfield_list
    assert _convert_to(expected_bitfield_list) == bitfield_value


def test_trigger_usage_bitfield():
    """Test for trigger usage bitfield."""
    _convert_from = partial(
        enum_bitfield_to_list, bitfield_enum_type=_TriggerUsageTypes, actual_enum_type=TriggerUsage
    )
    _convert_to = partial(enum_list_to_bitfield, bitfield_enum_type=_TriggerUsageTypes)

    bitfield_value = (
        _TriggerUsageTypes.ADVANCE.value
        + _TriggerUsageTypes.PAUSE.value
        + _TriggerUsageTypes.REFERENCE.value
        + _TriggerUsageTypes.START.value
        + _TriggerUsageTypes.HANDSHAKE.value
        + _TriggerUsageTypes.ARM_START.value
    )
    expected_bitfield_list = [
        TriggerUsage.ADVANCE,
        TriggerUsage.PAUSE,
        TriggerUsage.REFERENCE,
        TriggerUsage.START,
        TriggerUsage.HANDSHAKE,
        TriggerUsage.ARM_START,
    ]
    assert _convert_from(bitfield_value) == expected_bitfield_list
    assert _convert_to(expected_bitfield_list) == bitfield_value
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/legacy/test_events.py sha256=a3cd427d31a9588dacef12e0acc6ae27c208ea66efaff7018967a1b61bb262b5 bytes=2445 -->
## FILE: tests/legacy/test_events.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/legacy/test_events.py`
- sha256: `a3cd427d31a9588dacef12e0acc6ae27c208ea66efaff7018967a1b61bb262b5`
- bytes: 2445

````python
"""Tests for validating the NI-DAQmx events."""

import random
import time

import pytest

from nidaqmx.constants import AcquisitionType
from tests.helpers import generate_random_seed


class TestEvents:
    """Contains a collection of pytest tests.

    This validate the NI-DAQmx events functionality in the Python NI-DAQmx API.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_every_n_samples_event(self, task, sim_6363_device, seed):
        """Test for validating every n samples event."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        samples_chunk = 100
        sample_rate = 5000

        task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)

        samples_multiple = random.randint(2, 5)
        num_samples = samples_chunk * samples_multiple

        task.timing.cfg_samp_clk_timing(
            sample_rate, sample_mode=AcquisitionType.FINITE, samps_per_chan=num_samples
        )

        # Python 2.X does not have nonlocal keyword.
        non_local_var = {"samples_read": 0}

        def callback(task_handle, every_n_samples_event_type, number_of_samples, callback_data):
            samples = task.read(number_of_samples_per_channel=samples_chunk, timeout=2.0)
            non_local_var["samples_read"] += len(samples)
            return 0

        task.register_every_n_samples_acquired_into_buffer_event(samples_chunk, callback)

        task.start()
        task.wait_until_done(timeout=2)

        # Wait until done doesn't wait for all callbacks to be processed.
        time.sleep(1)
        task.stop()

        assert non_local_var["samples_read"] == num_samples

        samples_multiple = random.randint(2, 5)
        num_samples = samples_chunk * samples_multiple

        task.timing.cfg_samp_clk_timing(
            sample_rate, sample_mode=AcquisitionType.FINITE, samps_per_chan=num_samples
        )

        non_local_var = {"samples_read": 0}

        # Unregister event callback function by passing None.
        task.register_every_n_samples_acquired_into_buffer_event(samples_chunk, None)

        task.start()
        task.wait_until_done(timeout=2)

        # Wait until done doesn't wait for all callbacks to be processed.
        time.sleep(1)
        task.stop()

        assert non_local_var["samples_read"] == 0
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/legacy/test_export_signals.py sha256=bb3468e7c7dbfcc0c63f73797af836fd0cd67715ad31983111e50aac4fcf35d3 bytes=1213 -->
## FILE: tests/legacy/test_export_signals.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/legacy/test_export_signals.py`
- sha256: `bb3468e7c7dbfcc0c63f73797af836fd0cd67715ad31983111e50aac4fcf35d3`
- bytes: 1213

````python
"""Tests for validating export signals functionality."""

import random

import pytest

from nidaqmx.constants import Signal
from tests.helpers import generate_random_seed
from tests.legacy.test_read_write import TestDAQmxIOBase


class TestExportSignals(TestDAQmxIOBase):
    """Contains a collection of pytest tests.

    These validate the export signals functionality in the NI-DAQmx Python API.
    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_export_signals(self, task, sim_6363_device, seed):
        """Test for validating export signals."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_chan = random.choice(sim_6363_device.ai_physical_chans)
        pfi_line = random.choice(self._get_device_pfi_lines(sim_6363_device))

        task.ai_channels.add_ai_voltage_chan(ai_chan.name)
        task.timing.cfg_samp_clk_timing(1000)

        task.export_signals.export_signal(Signal.SAMPLE_CLOCK, pfi_line)

        assert task.export_signals.samp_clk_output_term == pfi_line
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/legacy/test_invalid_reads.py sha256=c0c44602fb6705780bdd111f1d58ed7286e269dee6206e7835f06fc3da397585 bytes=2915 -->
## FILE: tests/legacy/test_invalid_reads.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/legacy/test_invalid_reads.py`
- sha256: `c0c44602fb6705780bdd111f1d58ed7286e269dee6206e7835f06fc3da397585`
- bytes: 2915

````python
"""Tests for validating invalid read functionality."""

# import numpy
# import pytest
# import random

# import nidaqmx
# from nidaqmx.errors import DaqError
# from nidaqmx.utils import flatten_channel_string
# from .fixtures import sim_6363_device
# from tests.helpers import generate_random_seed
# from tests.legacy.test_read_write import TestDAQmxIOBase


# class TestInvalidReads(TestReadWriteBase):

# @pytest.mark.parametrize('seed', [generate_random_seed()])
# def test_one_chan_read_for_n_chan_task(self, task, sim_6363_device, seed):
#     # Reset the pseudorandom number generator with seed.
#     random.seed(seed)
#
#     number_of_channels = random.randint(
#         2, len(sim_6363_device.ai_physical_chans))
#
#     ai_channels = random.sample(
#         sim_6363_device.ai_physical_chans, number_of_channels)
#
#     task.ai_channels.add_ai_voltage_chan(
#         flatten_channel_string([c.name for c in ai_channels]),
#         max_val=10, min_val=-10)
#
#     with pytest.raises(DaqError) as e:
#         task.read_one_chan()
#     assert e.value.error_code == -200523

# @pytest.mark.parametrize('seed', [generate_random_seed()])
# def test_numpy_read_for_counter_pulse_task(self, task, sim_6363_device, seed):
#     # Reset the pseudorandom number generator with seed.
#     random.seed(seed)
#
#     counter = random.choice(self._get_device_counters(sim_6363_device))
#
#     task.ci_channels.add_ci_pulse_chan_freq(counter)
#
#     with pytest.raises(DaqError) as e:
#         task.read_numpy()
#     assert e.value.error_code == -1
#
# @pytest.mark.parametrize('seed', [generate_random_seed()])
# def test_numpy_read_incorrectly_shaped_data(self, task, sim_6363_device, seed):
#     # Reset the pseudorandom number generator with seed.
#     random.seed(seed)
#
#     # Randomly select physical channels to test.
#     number_of_channels = random.randint(
#         2, len(sim_6363_device.ai_physical_chans))
#     channels_to_test = random.sample(
#         sim_6363_device.ai_physical_chans, number_of_channels)
#     number_of_samples = random.randint(50, 100)
#
#     task.ai_channels.add_ai_voltage_chan(
#         flatten_channel_string([c.name for c in channels_to_test]),
#         max_val=10, min_val=-10)
#     task.timing.cfg_samp_clk_timing(
#         1000, samps_per_chan=number_of_samples)
#
#     # Allocate numpy array but swap the rows and columns so the numpy
#     # array is shaped incorrectly, but the amount of samples is still
#     # the same.
#     numpy_array = numpy.zeros(
#         (number_of_samples, number_of_channels), dtype=numpy.float64)
#
#     with pytest.raises(DaqError) as e:
#         task.read_numpy(
#             numpy_array=numpy_array,
#             number_of_samples_per_channel=number_of_samples,
#             timeout=2)
#
#     assert e.value.error_code == -1
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/legacy/test_invalid_writes.py sha256=1928b1e3977a2638221c33dcebcf2c4ef5c5708a06471bc3918521553e6dadf1 bytes=6379 -->
## FILE: tests/legacy/test_invalid_writes.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/legacy/test_invalid_writes.py`
- sha256: `1928b1e3977a2638221c33dcebcf2c4ef5c5708a06471bc3918521553e6dadf1`
- bytes: 6379

````python
"""Tests for validating invalid write functionality."""

import random

import numpy
import pytest

from nidaqmx.errors import DaqError
from nidaqmx.utils import flatten_channel_string
from tests.helpers import generate_random_seed


class TestInvalidWrites:
    """Contains a collection of pytest tests.

    These validate the write functionality with improper data.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_insufficient_write_data(self, task, sim_6363_device, seed):
        """Test for validating write functionality with insufficient data."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        # Randomly select physical channels to test.
        number_of_channels = random.randint(2, len(sim_6363_device.ao_physical_chans))
        channels_to_test = random.sample(sim_6363_device.ao_physical_chans, number_of_channels)

        task.ao_channels.add_ao_voltage_chan(
            flatten_channel_string([c.name for c in channels_to_test]), max_val=10, min_val=-10
        )

        with pytest.raises(DaqError) as e:
            task.write(random.uniform(-10, 10))
        assert e.value.error_code == -200524

        number_of_samples = random.randint(1, number_of_channels - 1)
        values_to_test = [random.uniform(-10, 10) for _ in range(number_of_samples)]

        with pytest.raises(DaqError) as e:
            task.write(values_to_test, auto_start=True)
        assert e.value.error_code == -200524

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_insufficient_numpy_write_data(self, task, sim_6363_device, seed):
        """Test for validating write functionality with insufficient data."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        # Randomly select physical channels to test.
        number_of_channels = random.randint(2, len(sim_6363_device.ao_physical_chans))
        channels_to_test = random.sample(sim_6363_device.ao_physical_chans, number_of_channels)

        task.ao_channels.add_ao_voltage_chan(
            flatten_channel_string([c.name for c in channels_to_test]), max_val=10, min_val=-10
        )

        number_of_samples = random.randint(1, number_of_channels - 1)
        values_to_test = numpy.array(
            [random.uniform(-10, 10) for _ in range(number_of_samples)], dtype=numpy.float64
        )

        with pytest.raises(DaqError) as e:
            task.write(values_to_test, auto_start=True)
        assert e.value.error_code == -200524

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_extraneous_write_data(self, task, sim_6363_device, seed):
        """Test for validating write functionality with extraneous data."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        # Randomly select physical channels to test.
        number_of_channels = random.randint(1, len(sim_6363_device.ao_physical_chans))
        channels_to_test = random.sample(sim_6363_device.ao_physical_chans, number_of_channels)

        task.ao_channels.add_ao_voltage_chan(
            flatten_channel_string([c.name for c in channels_to_test]), max_val=10, min_val=-10
        )

        # Generate random values to test.
        number_of_data_rows = random.randint(number_of_channels + 1, number_of_channels + 10)
        values_to_test = [
            [random.uniform(-10, 10) for _ in range(10)] for _ in range(number_of_data_rows)
        ]

        with pytest.raises(DaqError) as e:
            task.write(values_to_test, auto_start=True)

        assert e.value.error_code == -200524

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_extraneous_numpy_write_data(self, task, sim_6363_device, seed):
        """Test for validating write functionality with extraneous data."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        # Randomly select physical channels to test.
        number_of_channels = random.randint(1, len(sim_6363_device.ao_physical_chans))
        channels_to_test = random.sample(sim_6363_device.ao_physical_chans, number_of_channels)

        task.ao_channels.add_ao_voltage_chan(
            flatten_channel_string([c.name for c in channels_to_test]), max_val=10, min_val=-10
        )

        # Generate random values to test.
        number_of_data_rows = random.randint(number_of_channels + 1, number_of_channels + 10)
        values_to_test = [
            [random.uniform(-10, 10) for _ in range(10)] for _ in range(number_of_data_rows)
        ]

        numpy_data = numpy.array(values_to_test, dtype=numpy.float64)

        with pytest.raises(DaqError) as e:
            task.write(numpy_data, auto_start=True)

        assert e.value.error_code == -200524

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_numpy_write_incorrectly_shaped_data(self, task, sim_6363_device, seed):
        """Test for validating write functionality with incorrectly shaped data."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        # Randomly select physical channels to test.
        number_of_channels = random.randint(2, len(sim_6363_device.ao_physical_chans))
        channels_to_test = random.sample(sim_6363_device.ao_physical_chans, number_of_channels)
        number_of_samples = random.randint(50, 100)

        task.ao_channels.add_ao_voltage_chan(
            flatten_channel_string([c.name for c in channels_to_test]), max_val=10, min_val=-10
        )
        task.timing.cfg_samp_clk_timing(1000, samps_per_chan=number_of_samples)

        # Generate write data but swap the rows and columns so the numpy
        # array is shaped incorrectly, but the amount of samples is still
        # the same.
        values_to_test = numpy.array(
            [
                [random.uniform(-10, 10) for _ in range(number_of_channels)]
                for _ in range(number_of_samples)
            ],
            dtype=numpy.float64,
        )

        with pytest.raises(DaqError) as e:
            task.write(values_to_test, auto_start=True)

        assert e.value.error_code == -200524
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/legacy/test_multi_threading.py sha256=46d4aa5077c14723a30c086e01bb7a326ac41b74cdebb435b65192c7f0fcf30e bytes=3569 -->
## FILE: tests/legacy/test_multi_threading.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/legacy/test_multi_threading.py`
- sha256: `46d4aa5077c14723a30c086e01bb7a326ac41b74cdebb435b65192c7f0fcf30e`
- bytes: 3569

````python
"""Tests for validating multi-thread reading functionality."""

import random

import pykka
import pytest

import nidaqmx
from tests.helpers import generate_random_seed


class Error(Exception):
    """Base error class."""

    pass


class NoFixtureDetectedError(Error):
    """Custom error class when no fixtures are available."""

    pass


class DAQmxReaderActor(pykka.ThreadingActor):
    """A proxy for reading samples."""

    def __init__(self, task):
        """A proxy for reading samples."""
        super().__init__()
        self.task = task

    def read(self, samples_per_read, number_of_reads, timeout=10):
        """Reads the samples from the thread."""
        for i in range(number_of_reads):
            self.task.read(number_of_samples_per_channel=samples_per_read, timeout=timeout)


class TestMultiThreadedReads:
    """Contains a collection of pytest tests.

    This validates multi-threaded reads using the NI-DAQmx Python API.
    These tests create multiple tasks, each of which uses one of 4 simulated
    X Series devices.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_multi_threaded_analog_read(self, multi_threading_test_devices, seed, init_kwargs):
        """Test for validating multi-thread read operation."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        sample_rate = 10000
        samples_per_read = int(sample_rate / 10)

        number_of_reads = random.randint(200, 500)
        number_of_samples = samples_per_read * number_of_reads

        channels_to_test = []
        for device in multi_threading_test_devices:
            channels_to_test.append(random.choice(device.ai_physical_chans))

        tasks = []
        try:
            for channel_to_test in channels_to_test:
                task = None
                try:
                    task = nidaqmx.Task(**init_kwargs)
                    task.ai_channels.add_ai_voltage_chan(
                        channel_to_test.name, max_val=10, min_val=-10
                    )
                    task.timing.cfg_samp_clk_timing(sample_rate, samps_per_chan=number_of_samples)
                except nidaqmx.DaqError:
                    if task is not None:
                        task.close()
                    raise
                else:
                    tasks.append(task)
        except nidaqmx.DaqError:
            for task in tasks:
                task.close()
            raise

        actor_refs = []
        actor_proxies = []
        for task in tasks:
            actor_ref = DAQmxReaderActor.start(task)
            actor_refs.append(actor_ref)
            actor_proxies.append(actor_ref.proxy())

        try:
            for task in tasks:
                task.start()

            read_futures = []
            for actor_proxy in actor_proxies:
                read_futures.append(actor_proxy.read(samples_per_read, number_of_reads, timeout=2))

            pykka.get_all(read_futures, timeout=(number_of_samples / sample_rate) + 10)

        finally:
            for task in tasks:
                task.close()

            for actor_ref in actor_refs:
                try:
                    actor_ref.stop(timeout=(number_of_samples / sample_rate) + 10)
                except pykka.Timeout:
                    print(
                        "Could not stop actor {} within the specified " "timeout.".format(actor_ref)
                    )
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/legacy/test_power_up_states.py sha256=9b704ac69a0e527111a6b7f9d0c19b1ccad82a6df77698fdc3a500bf455a5145 bytes=1864 -->
## FILE: tests/legacy/test_power_up_states.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/legacy/test_power_up_states.py`
- sha256: `9b704ac69a0e527111a6b7f9d0c19b1ccad82a6df77698fdc3a500bf455a5145`
- bytes: 1864

````python
"""Tests for validating power up states functions."""

from nidaqmx.constants import PowerUpStates
from nidaqmx.system.system import DOPowerUpState


class TestPowerUpStates:
    """Contains a collection of pytest tests.

    This validate the power up states functions in the Python NI-DAQmx API.
    """

    def test_digital_power_up_states(self, real_x_series_device, system):
        """Test for validating digital power up states."""
        # The power up state for digital lines for an X Series device has to
        # be set for the whole port.
        do_port = real_x_series_device.do_ports[0].name

        # Set power up state for whole port.
        state_to_set = DOPowerUpState(physical_channel=do_port, power_up_state=PowerUpStates.LOW)
        system.set_digital_power_up_states(real_x_series_device.name, [state_to_set])

        # Getting power up states returns state for all channels on device.
        all_states = system.get_digital_power_up_states(real_x_series_device.name)

        # Find power states for all the digital lines that belong to the port.
        port_states = [p for p in all_states if do_port in p.physical_channel]

        # Validate power up states were set.
        for state in port_states:
            assert state.power_up_state == PowerUpStates.LOW

        # Reset power up states to tristate.
        state_to_set = DOPowerUpState(
            physical_channel=do_port, power_up_state=PowerUpStates.TRISTATE
        )
        system.set_digital_power_up_states(real_x_series_device.name, [state_to_set])

        all_states = system.get_digital_power_up_states(real_x_series_device.name)
        port_states = [p for p in all_states if do_port in p.physical_channel]

        for state in port_states:
            assert state.power_up_state == PowerUpStates.TRISTATE
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/legacy/test_properties.py sha256=7ac2384772b2df87c2584edfe18d5bb48c02d1f68794ae42ab1f4cb260f31923 bytes=7106 -->
## FILE: tests/legacy/test_properties.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/legacy/test_properties.py`
- sha256: `7ac2384772b2df87c2584edfe18d5bb48c02d1f68794ae42ab1f4cb260f31923`
- bytes: 7106

````python
"""Tests for validating properties for different basic data types."""

import random

import pytest

from nidaqmx import DaqError
from nidaqmx.constants import AcquisitionType, UsageTypeAI
from tests.helpers import generate_random_seed


class TestPropertyBasicDataTypes:
    """Contains a collection of pytest tests.

    This validates the property getter,setter and deleter methods for different basic data types.
    """

    def test_boolean_property(self, task, sim_6363_device):
        """Test for validating boolean property."""
        task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)

        task.timing.cfg_samp_clk_timing(1000)
        task.triggers.start_trigger.cfg_dig_edge_start_trig(
            f"/{sim_6363_device.name}/Ctr0InternalOutput"
        )

        # Test property initial value.
        assert not task.triggers.start_trigger.retriggerable

        # Test property setter and getter.
        task.triggers.start_trigger.retriggerable = True
        assert task.triggers.start_trigger.retriggerable

        # Test property deleter.
        del task.triggers.start_trigger.retriggerable
        assert not task.triggers.start_trigger.retriggerable

    def test_enum_property(self, task, sim_6363_device):
        """Test for validating enum property."""
        task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)

        task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.CONTINUOUS)

        # Test property initial value.
        assert task.timing.samp_quant_samp_mode == AcquisitionType.CONTINUOUS

        # Test property setter and getter.
        task.timing.samp_quant_samp_mode = AcquisitionType.FINITE
        assert task.timing.samp_quant_samp_mode == AcquisitionType.FINITE

        # Test property deleter.
        del task.timing.samp_quant_samp_mode
        assert task.timing.samp_quant_samp_mode == AcquisitionType.CONTINUOUS

    def test_float_property(self, task, sim_6363_device):
        """Test for validating float property."""
        ai_channel = task.ai_channels.add_ai_voltage_chan(
            sim_6363_device.ai_physical_chans[0].name, max_val=5
        )

        # Test property default value.
        assert ai_channel.ai_max == 5

        # Test property setter and getter.
        max_value = 10
        ai_channel.ai_max = max_value
        assert ai_channel.ai_max == max_value

        # Test property deleter. Reading this property will throw an
        # error after being reset.
        del ai_channel.ai_max
        with pytest.raises(DaqError) as e:
            read_value = ai_channel.ai_max  # noqa: F841
        assert e.value.error_code == -200695

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_int_property(self, task, sim_6363_device, seed):
        """Test for validating integer property."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        task.ci_channels.add_ci_count_edges_chan(sim_6363_device.ci_physical_chans[0].name)

        # Test property default value.
        assert task.in_stream.offset == 0

        # Test property setter and getter.
        value_to_test = random.randint(0, 100)
        task.in_stream.offset = value_to_test
        assert task.in_stream.offset == value_to_test

        value_to_test = random.randint(-100, 0)
        task.in_stream.offset = value_to_test
        assert task.in_stream.offset == value_to_test

        # Test property deleter.
        del task.in_stream.offset
        assert task.in_stream.offset == 0

    def test_string_property(self, task, sim_6363_device):
        """Test for validating string property."""
        ai_channel = task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)

        # Test property default value.
        assert ai_channel.description == ""

        # Test property setter and getter.
        description = "Channel description."
        ai_channel.description = description
        assert ai_channel.description == description

        # Test property deleter.
        del ai_channel.description
        assert ai_channel.description == ""

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_uint_property(self, task, sim_6363_device, seed):
        """Test for validating uint property."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)

        task.timing.cfg_samp_clk_timing(1000)

        # Test property initial value.
        assert task.timing.samp_clk_timebase_div == 100000

        # Test property setter and getter.
        value_to_test = random.randint(500, 10000)
        task.timing.samp_clk_timebase_div = value_to_test
        assert task.timing.samp_clk_timebase_div == value_to_test

        # Test property deleter.
        del task.timing.samp_clk_timebase_div
        assert task.timing.samp_clk_timebase_div == 100000


class TestPropertyListDataTypes:
    """Contains a collection of pytest tests.

    This validates the property getter, setter, and deleter methods for list data types.
    There are almost no setter and deleter methods for properties that have
    list data types.
    """

    def test_list_of_strings_property(self, sim_6363_device):
        """Test for validating list of strings property."""
        terminals = sim_6363_device.terminals

        assert isinstance(terminals, list)
        assert isinstance(terminals[0], str)

    def test_list_of_enums_property(self, sim_6363_device):
        """Test for validating list of enums property."""
        terminals = sim_6363_device.ai_meas_types

        assert isinstance(terminals, list)
        assert isinstance(terminals[0], UsageTypeAI)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    @pytest.mark.device_name("bridgeTester")
    def test_list_of_floats_property(self, task, device, seed):
        """Test for validating list of float property."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        ai_channel = task.ai_channels.add_ai_bridge_chan(device.ai_physical_chans[0].name)

        # Test default property value.
        assert isinstance(ai_channel.ai_bridge_poly_forward_coeff, list)
        assert len(ai_channel.ai_bridge_poly_forward_coeff) == 0

        # Test property setter and getter.
        value_to_test = [random.randint(-10, 10) for _ in range(random.randint(2, 5))]
        ai_channel.ai_bridge_poly_forward_coeff = value_to_test
        assert ai_channel.ai_bridge_poly_forward_coeff == value_to_test

        # Test property deleter.
        del ai_channel.ai_bridge_poly_forward_coeff
        assert isinstance(ai_channel.ai_bridge_poly_forward_coeff, list)
        assert len(ai_channel.ai_bridge_poly_forward_coeff) == 0
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/legacy/test_read_exceptions.py sha256=899bd55020e799185268de591bc83c301c6d38ce5844117e0f01d0b3998e0f4d bytes=9692 -->
## FILE: tests/legacy/test_read_exceptions.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/legacy/test_read_exceptions.py`
- sha256: `899bd55020e799185268de591bc83c301c6d38ce5844117e0f01d0b3998e0f4d`
- bytes: 9692

````python
"""Tests for validating read error behavior."""

import numpy
import pytest

import nidaqmx
import nidaqmx.stream_readers
from nidaqmx.constants import AcquisitionType, BusType, Level, TaskMode
from nidaqmx.error_codes import DAQmxErrors


class TestReadExceptions:
    """Contains a collection of pytest tests.

    This validates the Read error behavior in the NI-DAQmx Python API.
    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    """

    def test_timeout(self, generate_task, real_x_series_device):
        """Test for validating read timeout."""
        # USB streaming is very tricky.
        if not (
            real_x_series_device.bus_type == BusType.PCIE
            or real_x_series_device.bus_type == BusType.PXIE
        ):
            pytest.skip("Requires a plugin device.")

        samples_to_read = 75
        clocks_to_give = 100
        sample_rate = 1000

        read_task = generate_task()
        sample_clk_task = generate_task()

        # Use a counter output pulse train task as the sample clock source
        # for both the AI and AO tasks.
        sample_clk_task.co_channels.add_co_pulse_chan_freq(
            f"{real_x_series_device.name}/ctr0", freq=sample_rate, idle_state=Level.LOW
        )
        sample_clk_task.timing.cfg_implicit_timing(
            samps_per_chan=clocks_to_give, sample_mode=AcquisitionType.FINITE
        )
        sample_clk_task.control(TaskMode.TASK_COMMIT)

        samp_clk_terminal = f"/{real_x_series_device.name}/Ctr0InternalOutput"

        read_task.ai_channels.add_ai_voltage_chan(
            real_x_series_device.ai_physical_chans[0].name, max_val=10, min_val=-10
        )
        read_task.timing.cfg_samp_clk_timing(
            sample_rate, source=samp_clk_terminal, sample_mode=AcquisitionType.CONTINUOUS
        )

        # Start the read task before the clock.
        read_task.start()

        # Generate all the clocks.
        sample_clk_task.start()
        sample_clk_task.wait_until_done()
        sample_clk_task.stop()

        # Do a partial read which succeeds.
        values_read = read_task.read(number_of_samples_per_channel=samples_to_read, timeout=2.0)
        assert len(values_read) == samples_to_read

        # Now read more data than is available.
        with pytest.raises(nidaqmx.DaqReadError) as timeout_exception:
            values_read = read_task.read(number_of_samples_per_channel=samples_to_read, timeout=2.0)

        assert timeout_exception.value.error_code == DAQmxErrors.SAMPLES_NOT_YET_AVAILABLE
        # We should have read a partial dataset.
        number_of_samples_expected = clocks_to_give - samples_to_read
        assert timeout_exception.value.samps_per_chan_read == number_of_samples_expected

    def test_timeout_raw(self, generate_task, real_x_series_device):
        """Test for validating read timeout."""
        # USB streaming is very tricky.
        if not (
            real_x_series_device.bus_type == BusType.PCIE
            or real_x_series_device.bus_type == BusType.PXIE
        ):
            pytest.skip("Requires a plugin device.")

        samples_to_read = 75
        clocks_to_give = 100
        sample_rate = 1000

        read_task = generate_task()
        sample_clk_task = generate_task()

        # Use a counter output pulse train task as the sample clock source
        # for both the AI and AO tasks.
        sample_clk_task.co_channels.add_co_pulse_chan_freq(
            f"{real_x_series_device.name}/ctr0", freq=sample_rate, idle_state=Level.LOW
        )
        sample_clk_task.timing.cfg_implicit_timing(
            samps_per_chan=clocks_to_give, sample_mode=AcquisitionType.FINITE
        )
        sample_clk_task.control(TaskMode.TASK_COMMIT)

        samp_clk_terminal = f"/{real_x_series_device.name}/Ctr0InternalOutput"

        read_task.ai_channels.add_ai_voltage_chan(
            real_x_series_device.ai_physical_chans[0].name, max_val=10, min_val=-10
        )
        read_task.timing.cfg_samp_clk_timing(
            sample_rate, source=samp_clk_terminal, sample_mode=AcquisitionType.CONTINUOUS
        )

        # Start the read task before the clock.
        read_task.start()

        # Generate all the clocks.
        sample_clk_task.start()
        sample_clk_task.wait_until_done()
        sample_clk_task.stop()

        # Set read timeout.
        read_task.in_stream.timeout = 2.0

        # Do a partial read which should succeed.
        values_read = read_task.in_stream.read(number_of_samples_per_channel=samples_to_read)
        assert len(values_read) == samples_to_read

        # Now read more data than is available.
        with pytest.raises(nidaqmx.DaqReadError) as timeout_exception:
            values_read = read_task.in_stream.read(number_of_samples_per_channel=samples_to_read)

        assert timeout_exception.value.error_code == DAQmxErrors.SAMPLES_NOT_YET_AVAILABLE
        # We should have read a partial dataset.
        number_of_samples_expected = clocks_to_give - samples_to_read
        assert timeout_exception.value.samps_per_chan_read == number_of_samples_expected

    def test_timeout_stream(self, generate_task, real_x_series_device):
        """Test for validating read timeout."""
        # USB streaming is very tricky.
        if not (
            real_x_series_device.bus_type == BusType.PCIE
            or real_x_series_device.bus_type == BusType.PXIE
        ):
            pytest.skip("Requires a plugin device.")

        if real_x_series_device.ai_simultaneous_sampling_supported:
            pytest.skip(
                "Requires device that do not have simultaneous sampling, since AO loopback have to be programmed differently."
            )

        number_of_channels = len(real_x_series_device.ao_physical_chans)

        if not number_of_channels:
            pytest.skip("Requires AO channels in the device")

        samples_to_read = 75
        clocks_to_give = 100
        sample_rate = 1000
        data_to_write = [float(i + 1) for i in range(number_of_channels)]

        write_task = generate_task()
        read_task = generate_task()
        sample_clk_task = generate_task()

        write_task.ao_channels.add_ao_voltage_chan(
            f"{real_x_series_device.name}/ao0:{number_of_channels - 1}"
        )
        write_task.write(data_to_write, auto_start=True)

        # Use a counter output pulse train task as the sample clock source
        # for both the AI and AO tasks.
        sample_clk_task.co_channels.add_co_pulse_chan_freq(
            f"{real_x_series_device.name}/ctr0", freq=sample_rate, idle_state=Level.LOW
        )
        sample_clk_task.timing.cfg_implicit_timing(
            samps_per_chan=clocks_to_give, sample_mode=AcquisitionType.FINITE
        )
        sample_clk_task.control(TaskMode.TASK_COMMIT)

        samp_clk_terminal = f"/{real_x_series_device.name}/Ctr0InternalOutput"

        read_task.ai_channels.add_ai_voltage_chan(
            ",".join(
                f"{real_x_series_device.name}/_ao{i}_vs_aognd" for i in range(number_of_channels)
            ),
            max_val=10,
            min_val=-10,
        )
        read_task.timing.cfg_samp_clk_timing(
            sample_rate, source=samp_clk_terminal, sample_mode=AcquisitionType.FINITE
        )

        reader = nidaqmx.stream_readers.AnalogMultiChannelReader(read_task.in_stream)

        # Start the read task before the clock.
        read_task.start()

        # Generate all the clocks.
        sample_clk_task.start()
        sample_clk_task.wait_until_done()
        sample_clk_task.stop()

        # Set read timeout.
        read_task.in_stream.timeout = 2

        # Do a partial read which should succeed.
        data = numpy.zeros((number_of_channels, samples_to_read), dtype=numpy.float64)
        num_values_read = reader.read_many_sample(
            data, number_of_samples_per_channel=samples_to_read, timeout=2.0
        )

        assert num_values_read == samples_to_read
        # All the data should have been overwritten.
        assert not any(element == 0 for element in data.reshape(data.size))

        for i in range(number_of_channels):
            assert all(element == pytest.approx(data_to_write[i], abs=1e-2) for element in data[i])

        # Now read more data than is available.
        data = numpy.zeros((number_of_channels, samples_to_read), dtype=numpy.float64)
        with pytest.raises(nidaqmx.DaqReadError) as timeout_exception:
            num_values_read = reader.read_many_sample(
                data, number_of_samples_per_channel=samples_to_read, timeout=2.0
            )

        assert timeout_exception.value.error_code == DAQmxErrors.SAMPLES_NOT_YET_AVAILABLE
        # We should have read a partial dataset.
        number_of_samples_expected = clocks_to_give - samples_to_read
        number_of_samples_read = timeout_exception.value.samps_per_chan_read
        assert number_of_samples_read == number_of_samples_expected

        # DAQmx overwrites first channel array slices with other channel data as in AB#2420742
        # Hence resize of the data is needed to extract each data correctly
        resized_data = numpy.resize(data, (number_of_channels, number_of_samples_read))
        for i in range(number_of_channels):
            assert all(
                element == pytest.approx(data_to_write[i], abs=1e-2) for element in resized_data[i]
            )
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/legacy/test_read_write.py sha256=11639bc9e9c9a2f84d58a4c63a79262972931d09bcb22eff00c96a37f08ffb88 bytes=31801 -->
## FILE: tests/legacy/test_read_write.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/legacy/test_read_write.py`
- sha256: `11639bc9e9c9a2f84d58a4c63a79262972931d09bcb22eff00c96a37f08ffb88`
- bytes: 31801

````python
"""Tests for validating read and write operation."""

import collections
import math
import random
import re
import time

import numpy
import pytest

import nidaqmx
from nidaqmx.constants import (
    AcquisitionType,
    Edge,
    Level,
    LineGrouping,
    TaskMode,
    TriggerType,
)
from nidaqmx.utils import flatten_channel_string
from tests.helpers import POWER_ABS_EPSILON, generate_random_seed


class Error(Exception):
    """Base error class."""

    pass


class NoFixtureDetectedError(Error):
    """Custom error class when no fixtures are available."""

    pass


class TestDAQmxIOBase:
    """Contains a collection of methods that are used in read and write tests.

    Classes which validate the Task Read and Write functions in the NI-DAQmx Python API
    uses these methods.These tests use only a single X Series device by utilizing the
    internal loopback routes on the device.
    """

    ChannelPair = collections.namedtuple("ChannelPair", ["output_channel", "input_channel"])

    def _get_device_counters(self, device):
        r = re.compile("/ctr[0-9]+$", flags=re.IGNORECASE)
        co_phys_chan_names = [c.name for c in device.co_physical_chans]
        return list(filter(r.search, co_phys_chan_names))

    def _get_device_pfi_lines(self, device):
        r = re.compile("/PFI[0-9]+$", flags=re.IGNORECASE)
        return list(filter(r.search, device.terminals))

    def _get_analog_loopback_channels(self, device):
        loopback_channel_pairs = []

        for ao_physical_chan in device.ao_physical_chans:
            device_name, ao_channel_name = ao_physical_chan.name.split("/")

            loopback_channel_pairs.append(
                TestDAQmxIOBase.ChannelPair(
                    ao_physical_chan.name, f"{device_name}/_{ao_channel_name}_vs_aognd"
                )
            )

        return loopback_channel_pairs


class TestAnalogReadWrite(TestDAQmxIOBase):
    """Contains a collection of pytest tests.

    These validate the analog Read and Write functions in the NI-DAQmx Python API.
    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_1_chan_1_samp(self, generate_task, real_x_series_device, seed):
        """Test to validate reading and writing a sample data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)
        # Select a random loopback channel pair on the device.
        loopback_channel_pairs = self._get_analog_loopback_channels(real_x_series_device)
        loopback_channel_pair = random.choice(loopback_channel_pairs)

        write_task = generate_task()
        read_task = generate_task()
        write_task.ao_channels.add_ao_voltage_chan(
            loopback_channel_pair.output_channel, max_val=10, min_val=-10
        )

        read_task.ai_channels.add_ai_voltage_chan(
            loopback_channel_pair.input_channel, max_val=10, min_val=-10
        )

        # Generate random values to test.
        values_to_test = [random.uniform(-10, 10) for _ in range(10)]

        values_read = []
        for value_to_test in values_to_test:
            write_task.write(value_to_test)
            time.sleep(0.001)
            values_read.append(read_task.read())

        numpy.testing.assert_allclose(values_read, values_to_test, rtol=0.05, atol=0.005)

        # Verify setting number_of_samples_per_channel (even to 1)
        # returns a list.
        value_read = read_task.read(number_of_samples_per_channel=1)
        assert isinstance(value_read, list)
        assert len(value_read) == 1

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_n_chan_1_samp(self, generate_task, real_x_series_device, seed):
        """Test to validate reading and writing sample data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        # Select a random loopback channel pair on the device.
        loopback_channel_pairs = self._get_analog_loopback_channels(real_x_series_device)

        number_of_channels = random.randint(2, len(loopback_channel_pairs))
        channels_to_test = random.sample(loopback_channel_pairs, number_of_channels)

        write_task = generate_task()
        read_task = generate_task()
        write_task.ao_channels.add_ao_voltage_chan(
            flatten_channel_string([c.output_channel for c in channels_to_test]),
            max_val=10,
            min_val=-10,
        )

        read_task.ai_channels.add_ai_voltage_chan(
            flatten_channel_string([c.input_channel for c in channels_to_test]),
            max_val=10,
            min_val=-10,
        )

        # Generate random values to test.
        values_to_test = [random.uniform(-10, 10) for _ in range(number_of_channels)]

        write_task.write(values_to_test)
        time.sleep(0.001)
        values_read = read_task.read()

        numpy.testing.assert_allclose(values_read, values_to_test, rtol=0.05, atol=0.005)

        # Verify setting number_of_samples_per_channel (even to 1)
        # returns a list of lists.
        value_read = read_task.read(number_of_samples_per_channel=1)
        assert isinstance(value_read, list)
        assert isinstance(value_read[0], list)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_1_chan_n_samp(self, generate_task, real_x_series_device, seed):
        """Test to validate reading and writing sample data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(20, 100)
        sample_rate = random.uniform(1000, 5000)

        # Select a random loopback channel pair on the device.
        loopback_channel_pairs = self._get_analog_loopback_channels(real_x_series_device)
        loopback_channel_pair = random.choice(loopback_channel_pairs)

        write_task = generate_task()
        read_task = generate_task()
        sample_clk_task = generate_task()

        # Use a counter output pulse train task as the sample clock source
        # for both the AI and AO tasks.
        sample_clk_task.co_channels.add_co_pulse_chan_freq(
            f"{real_x_series_device.name}/ctr0", freq=sample_rate, idle_state=Level.LOW
        )
        sample_clk_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples)
        sample_clk_task.control(TaskMode.TASK_COMMIT)

        samp_clk_terminal = f"/{real_x_series_device.name}/Ctr0InternalOutput"

        write_task.ao_channels.add_ao_voltage_chan(
            loopback_channel_pair.output_channel, max_val=10, min_val=-10
        )
        write_task.timing.cfg_samp_clk_timing(
            sample_rate,
            source=samp_clk_terminal,
            active_edge=Edge.RISING,
            samps_per_chan=number_of_samples,
        )

        read_task.ai_channels.add_ai_voltage_chan(
            loopback_channel_pair.input_channel, max_val=10, min_val=-10
        )
        read_task.timing.cfg_samp_clk_timing(
            sample_rate,
            source=samp_clk_terminal,
            active_edge=Edge.FALLING,
            samps_per_chan=number_of_samples,
        )

        # Generate random values to test.
        values_to_test = [random.uniform(-10, 10) for _ in range(number_of_samples)]
        write_task.write(values_to_test)

        # Start the read and write tasks before starting the sample clock
        # source task.
        read_task.start()
        write_task.start()
        sample_clk_task.start()

        values_read = read_task.read(number_of_samples_per_channel=number_of_samples, timeout=2)

        numpy.testing.assert_allclose(values_read, values_to_test, rtol=0.05, atol=0.005)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_n_chan_n_samp(self, generate_task, real_x_series_device, seed):
        """Test to validate reading and writing sample data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(20, 100)
        sample_rate = random.uniform(1000, 5000)

        # Select a random loopback channel pair on the device.
        loopback_channel_pairs = self._get_analog_loopback_channels(real_x_series_device)

        number_of_channels = random.randint(2, len(loopback_channel_pairs))
        channels_to_test = random.sample(loopback_channel_pairs, number_of_channels)

        write_task = generate_task()
        read_task = generate_task()
        sample_clk_task = generate_task()

        # Use a counter output pulse train task as the sample clock source
        # for both the AI and AO tasks.
        sample_clk_task.co_channels.add_co_pulse_chan_freq(
            f"{real_x_series_device.name}/ctr0", freq=sample_rate
        )
        sample_clk_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples)
        sample_clk_task.control(TaskMode.TASK_COMMIT)

        samp_clk_terminal = f"/{real_x_series_device.name}/Ctr0InternalOutput"

        write_task.ao_channels.add_ao_voltage_chan(
            flatten_channel_string([c.output_channel for c in channels_to_test]),
            max_val=10,
            min_val=-10,
        )
        write_task.timing.cfg_samp_clk_timing(
            sample_rate,
            source=samp_clk_terminal,
            active_edge=Edge.RISING,
            samps_per_chan=number_of_samples,
        )

        read_task.ai_channels.add_ai_voltage_chan(
            flatten_channel_string([c.input_channel for c in channels_to_test]),
            max_val=10,
            min_val=-10,
        )
        read_task.timing.cfg_samp_clk_timing(
            sample_rate,
            source=samp_clk_terminal,
            active_edge=Edge.FALLING,
            samps_per_chan=number_of_samples,
        )

        # Generate random values to test.
        values_to_test = [
            [random.uniform(-10, 10) for _ in range(number_of_samples)]
            for _ in range(number_of_channels)
        ]
        write_task.write(values_to_test)

        # Start the read and write tasks before starting the sample clock
        # source task.
        read_task.start()
        write_task.start()
        sample_clk_task.start()

        values_read = read_task.read(number_of_samples_per_channel=number_of_samples, timeout=2)

        numpy.testing.assert_allclose(values_read, values_to_test, rtol=0.05, atol=0.005)


class TestDigitalReadWrite(TestDAQmxIOBase):
    """Contains a collection of pytest tests.

    These validate the digital Read and Write functions in the NI-DAQmx Python API.
    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_bool_1_chan_1_samp(self, task, real_x_series_device, seed):
        """Test to validate reading and writing boolean data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        do_line = random.choice(real_x_series_device.do_lines).name

        task.do_channels.add_do_chan(do_line, line_grouping=LineGrouping.CHAN_PER_LINE)

        # Generate random values to test.
        values_to_test = [bool(random.getrandbits(1)) for _ in range(10)]

        values_read = []
        for value_to_test in values_to_test:
            task.write(value_to_test)
            time.sleep(0.001)
            values_read.append(task.read())

        assert values_read == values_to_test

        # Verify setting number_of_samples_per_channel (even to 1)
        # returns a list.
        value_read = task.read(number_of_samples_per_channel=1)
        assert isinstance(value_read, list)
        assert len(value_read) == 1

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_bool_n_chan_1_samp(self, task, real_x_series_device, seed):
        """Test to validate reading and writing boolean data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_channels = random.randint(2, len(real_x_series_device.do_lines))
        do_lines = random.sample(real_x_series_device.do_lines, number_of_channels)

        task.do_channels.add_do_chan(
            flatten_channel_string([d.name for d in do_lines]),
            line_grouping=LineGrouping.CHAN_PER_LINE,
        )

        # Generate random values to test.
        values_to_test = [bool(random.getrandbits(1)) for _ in range(number_of_channels)]

        task.write(values_to_test)
        time.sleep(0.001)
        values_read = task.read()

        assert values_read == values_to_test

        # Verify setting number_of_samples_per_channel (even to 1)
        # returns a list of lists.
        value_read = task.read(number_of_samples_per_channel=1)
        assert isinstance(value_read, list)
        assert isinstance(value_read[0], list)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_uint_1_chan_1_samp(self, task, real_x_series_device, seed):
        """Test to validate reading and writing uint data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        do_port = random.choice(real_x_series_device.do_ports)

        task.do_channels.add_do_chan(do_port.name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

        # Generate random values to test.
        values_to_test = [int(random.getrandbits(do_port.do_port_width)) for _ in range(10)]

        values_read = []
        for value_to_test in values_to_test:
            task.write(value_to_test)
            time.sleep(0.001)
            values_read.append(task.read())

        assert values_read == values_to_test

        # Verify setting number_of_samples_per_channel (even to 1)
        # returns a list.
        value_read = task.read(number_of_samples_per_channel=1)
        assert isinstance(value_read, list)
        assert len(value_read) == 1

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_uint_multi_port(self, task, real_x_series_device, seed):
        """Test to validate reading and writing uint data ."""
        if len([d.do_port_width <= 16 for d in real_x_series_device.do_ports]) < 2:
            pytest.skip("task.read() accepts max of 32 bits for digital uint reads.")

        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        do_ports = random.sample(
            [d for d in real_x_series_device.do_ports if d.do_port_width <= 16], 2
        )

        total_port_width = sum([d.do_port_width for d in do_ports])

        task.do_channels.add_do_chan(
            flatten_channel_string([d.name for d in do_ports]),
            line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
        )

        # Generate random values to test.
        values_to_test = [int(random.getrandbits(total_port_width)) for _ in range(10)]

        values_read = []
        for value_to_test in values_to_test:
            task.write(value_to_test)
            time.sleep(0.001)
            values_read.append(task.read())

        assert values_read == values_to_test


class TestCounterReadWrite(TestDAQmxIOBase):
    """Contains a collection of pytest tests.

    These validate the counter Read and Write functions in the NI-DAQmx Python API.
    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_count_edges_1_samp(self, generate_task, real_x_series_device, seed):
        """Test to validate the set and read operations of edge count."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_pulses = random.randint(2, 100)
        frequency = random.uniform(5000, 50000)

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 2)

        write_task = generate_task()
        read_task = generate_task()
        write_task.co_channels.add_co_pulse_chan_freq(counters[0], freq=frequency)
        write_task.timing.cfg_implicit_timing(samps_per_chan=number_of_pulses)

        ci_channel = read_task.ci_channels.add_ci_count_edges_chan(counters[1])
        ci_channel.ci_count_edges_term = f"/{counters[0]}InternalOutput"

        read_task.start()
        write_task.start()
        write_task.wait_until_done(timeout=2)

        value_read = read_task.read()
        assert value_read == number_of_pulses

        # Verify setting number_of_samples_per_channel (even to 1)
        # returns a list.
        value_read = read_task.read(number_of_samples_per_channel=1)
        assert isinstance(value_read, list)
        assert len(value_read) == 1
        assert value_read[0] == number_of_pulses

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_count_edges_n_samp(self, generate_task, real_x_series_device, seed):
        """Test to validate the set and read operations of edge count."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(2, 100)
        frequency = random.uniform(5000, 50000)

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 3)

        write_task = generate_task()
        read_task = generate_task()
        sample_clk_task = generate_task()

        # Create a finite pulse train task that acts as the sample clock
        # for the read task and the arm start trigger for the write task.
        sample_clk_task.co_channels.add_co_pulse_chan_freq(counters[0], freq=frequency)
        actual_frequency = sample_clk_task.co_channels.all.co_pulse_freq
        sample_clk_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples)
        sample_clk_task.control(TaskMode.TASK_COMMIT)
        samp_clk_terminal = f"/{counters[0]}InternalOutput"

        write_task.co_channels.add_co_pulse_chan_freq(counters[1], freq=actual_frequency)
        write_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples)
        write_task.triggers.arm_start_trigger.trig_type = TriggerType.DIGITAL_EDGE
        write_task.triggers.arm_start_trigger.dig_edge_edge = Edge.RISING
        write_task.triggers.arm_start_trigger.dig_edge_src = samp_clk_terminal

        read_task.ci_channels.add_ci_count_edges_chan(counters[2], edge=Edge.RISING)
        read_task.ci_channels.all.ci_count_edges_term = f"/{counters[1]}InternalOutput"
        read_task.timing.cfg_samp_clk_timing(
            actual_frequency,
            source=samp_clk_terminal,
            active_edge=Edge.FALLING,
            samps_per_chan=number_of_samples,
        )

        read_task.start()
        write_task.start()
        sample_clk_task.start()
        sample_clk_task.wait_until_done(timeout=2)

        value_read = read_task.read(number_of_samples_per_channel=number_of_samples, timeout=2)

        expected_values = [i + 1 for i in range(number_of_samples)]

        assert value_read == expected_values

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_pulse_freq_1_samp(self, generate_task, real_x_series_device, seed):
        """Test to validate the set and read operations of pulse frequency."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        frequency = random.uniform(100, 1000)
        duty_cycle = random.uniform(0.2, 0.8)
        starting_edge = random.choice([Edge.RISING, Edge.FALLING])

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 2)

        write_task = generate_task()
        read_task = generate_task()
        write_task.co_channels.add_co_pulse_chan_freq(
            counters[0], freq=frequency, duty_cycle=duty_cycle
        )
        write_task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)

        read_task.ci_channels.add_ci_pulse_chan_freq(counters[1], min_val=100, max_val=1000)
        read_task.ci_channels.all.ci_pulse_freq_term = f"/{counters[0]}InternalOutput"
        read_task.ci_channels.all.ci_pulse_freq_starting_edge = starting_edge

        read_task.start()
        write_task.start()

        value_read = read_task.read(timeout=2)
        write_task.stop()

        assert numpy.isclose(value_read.freq, frequency, rtol=0.01)
        assert numpy.isclose(value_read.duty_cycle, duty_cycle, rtol=0.01)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_pulse_time_1_samp(self, generate_task, real_x_series_device, seed):
        """Test to validate the set and read operations of pulse time."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        high_time = random.uniform(0.001, 0.01)
        low_time = random.uniform(0.001, 0.01)
        starting_edge = random.choice([Edge.RISING, Edge.FALLING])

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 2)

        write_task = generate_task()
        read_task = generate_task()
        write_task.co_channels.add_co_pulse_chan_time(
            counters[0], high_time=high_time, low_time=low_time
        )
        write_task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)

        read_task.ci_channels.add_ci_pulse_chan_time(counters[1], min_val=0.001, max_val=0.01)
        read_task.ci_channels.all.ci_pulse_time_term = f"/{counters[0]}InternalOutput"
        read_task.ci_channels.all.ci_pulse_time_starting_edge = starting_edge

        read_task.start()
        write_task.start()

        value_read = read_task.read(timeout=2)
        write_task.stop()

        assert numpy.isclose(value_read.high_time, high_time, rtol=0.01)
        assert numpy.isclose(value_read.low_time, low_time, rtol=0.01)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_pulse_ticks_1_samp(self, generate_task, real_x_series_device, seed):
        """Test to validate the set and read operations of pulse ticks."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        high_ticks = random.randint(100, 1000)
        low_ticks = random.randint(100, 1000)
        starting_edge = random.choice([Edge.RISING, Edge.FALLING])

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 2)

        write_task = generate_task()
        read_task = generate_task()
        write_task.co_channels.add_co_pulse_chan_ticks(
            counters[0],
            f"/{real_x_series_device.name}/100kHzTimebase",
            high_ticks=high_ticks,
            low_ticks=low_ticks,
        )
        write_task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)

        read_task.ci_channels.add_ci_pulse_chan_ticks(
            counters[1],
            source_terminal=f"/{real_x_series_device.name}/100kHzTimebase",
            min_val=100,
            max_val=1000,
        )
        read_task.ci_channels.all.ci_pulse_ticks_term = f"/{counters[0]}InternalOutput"
        read_task.ci_channels.all.ci_pulse_ticks_starting_edge = starting_edge

        read_task.start()
        write_task.start()

        value_read = read_task.read(timeout=2)
        write_task.stop()

        assert value_read.high_tick == high_ticks
        assert value_read.low_tick == low_ticks


class TestPowerRead(TestDAQmxIOBase):
    """Contains a collection of pytest tests.

    These validate the power Read and Write functions in the NI-DAQmx Python API.
    These tests use simulated TestScale PPS device(s), TS-15200.
    """

    @pytest.mark.parametrize(
        "seed,output_enable", [(generate_random_seed(), True), (generate_random_seed(), False)]
    )
    def test_power_1_chan_1_samp(self, task, sim_ts_power_device, seed, output_enable):
        """Test to validate the set and read operations of power."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        voltage_setpoint = 0.0
        current_setpoint = 0.03

        task.ai_channels.add_ai_power_chan(
            f"{sim_ts_power_device.name}/power",
            voltage_setpoint,
            current_setpoint,
            output_enable,
        )

        task.start()
        value_read = task.read()

        if output_enable:
            assert value_read.voltage == pytest.approx(voltage_setpoint, abs=POWER_ABS_EPSILON)
            assert value_read.current == pytest.approx(current_setpoint, abs=POWER_ABS_EPSILON)
        else:
            assert math.isnan(value_read.voltage)
            assert math.isnan(value_read.current)

    @pytest.mark.parametrize(
        "seed,output_enables",
        [
            (generate_random_seed(), [True, True]),
            (generate_random_seed(), [True, False]),
            (generate_random_seed(), [False, True]),
            (generate_random_seed(), [False, False]),
        ],
    )
    def test_power_n_chan_1_samp(self, task, sim_ts_power_devices, seed, output_enables):
        """Test to validate the set and read operations of power."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        voltage_setpoint = 0.0
        current_setpoint = 0.03

        for device, output_enable in zip(sim_ts_power_devices, output_enables):
            task.ai_channels.add_ai_power_chan(
                f"{device.name}/power", voltage_setpoint, current_setpoint, output_enable
            )

        task.start()
        value_read = task.read()

        for data_idx, output_enable in enumerate(output_enables):
            if output_enable:
                assert value_read[data_idx].voltage == pytest.approx(
                    voltage_setpoint, abs=POWER_ABS_EPSILON
                )
                assert value_read[data_idx].current == pytest.approx(
                    current_setpoint, abs=POWER_ABS_EPSILON
                )
            else:
                assert math.isnan(value_read[data_idx].voltage)
                assert math.isnan(value_read[data_idx].current)

    @pytest.mark.parametrize(
        "seed,output_enable", [(generate_random_seed(), True), (generate_random_seed(), False)]
    )
    def test_power_1_chan_n_samp(self, task, sim_ts_power_device, seed, output_enable):
        """Test to validate the set and read operations of power."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        voltage_setpoint = 0.0
        current_setpoint = 0.03

        task.ai_channels.add_ai_power_chan(
            f"{sim_ts_power_device.name}/power",
            voltage_setpoint,
            current_setpoint,
            output_enable,
        )

        task.start()
        values_read = task.read(number_of_samples_per_channel=10)

        if output_enable:
            assert all(
                sample.voltage == pytest.approx(voltage_setpoint, abs=POWER_ABS_EPSILON)
                for sample in values_read
            )
            assert all(
                sample.current == pytest.approx(current_setpoint, abs=POWER_ABS_EPSILON)
                for sample in values_read
            )
        else:
            assert all(math.isnan(sample.voltage) for sample in values_read)
            assert all(math.isnan(sample.current) for sample in values_read)

    @pytest.mark.parametrize(
        "seed,output_enables",
        [
            (generate_random_seed(), [True, True]),
            (generate_random_seed(), [True, False]),
            (generate_random_seed(), [False, True]),
            (generate_random_seed(), [False, False]),
        ],
    )
    def test_power_n_chan_n_samp(self, task, sim_ts_power_devices, seed, output_enables):
        """Test to validate the set and read operations of power."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        voltage_setpoint = 0.0
        current_setpoint = 0.03

        for device, output_enable in zip(sim_ts_power_devices, output_enables):
            task.ai_channels.add_ai_power_chan(
                f"{device.name}/power", voltage_setpoint, current_setpoint, output_enable
            )

        task.start()
        values_read = task.read(number_of_samples_per_channel=10)

        for data_idx, output_enable in enumerate(output_enables):
            # Get the data for just this channel
            channel_values = values_read[data_idx]
            if output_enable:
                assert all(
                    sample.voltage == pytest.approx(voltage_setpoint, abs=POWER_ABS_EPSILON)
                    for sample in channel_values
                )
                assert all(
                    sample.current == pytest.approx(current_setpoint, abs=POWER_ABS_EPSILON)
                    for sample in channel_values
                )
            else:
                assert all(math.isnan(sample.voltage) for sample in channel_values)
                assert all(math.isnan(sample.current) for sample in channel_values)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_mixed_chans(self, task, sim_6363_device, seed):
        """Test to validate mixed channels."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        task.ai_channels.add_ai_voltage_chan(f"{sim_6363_device.name}/ai0", max_val=10, min_val=-10)
        task.ai_channels.add_ai_current_chan(
            f"{sim_6363_device.name}/ai1", max_val=0.01, min_val=-0.01
        )

        task.start()
        # We aren't validating data, just assuring that it doesn't fail.
        values_read = task.read(number_of_samples_per_channel=10)  # noqa: F841

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_mixed_chans_with_power(self, task, sim_ts_power_device, sim_ts_voltage_device, seed):
        """Test to validate mixed channels with power."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        voltage_setpoint = 0.0
        current_setpoint = 0.03
        output_enable = False

        task.ai_channels.add_ai_power_chan(
            f"{sim_ts_power_device.name}/power",
            voltage_setpoint,
            current_setpoint,
            output_enable,
        )
        task.ai_channels.add_ai_voltage_chan(
            f"{sim_ts_voltage_device.name}/ai0", max_val=10, min_val=-10
        )

        task.start()
        # We aren't validating data, just assuring that it fails. The error
        # code is currently not very good, so we'll ignore that for now.
        with pytest.raises(nidaqmx.errors.DaqReadError):
            values_read = task.read(number_of_samples_per_channel=10)  # noqa: F841
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/legacy/test_resource_warnings.py sha256=1a64a2c9d4abe1678a3b65062b5ab9ddf863edd7444c351dbbc423119e1b20f5 bytes=542 -->
## FILE: tests/legacy/test_resource_warnings.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/legacy/test_resource_warnings.py`
- sha256: `1a64a2c9d4abe1678a3b65062b5ab9ddf863edd7444c351dbbc423119e1b20f5`
- bytes: 542

````python
"""Tests for validating resource warning behavior."""

import pytest

import nidaqmx
from nidaqmx import DaqResourceWarning


class TestResourceWarnings:
    """Contains a collection of pytest tests.

    These validate the ResourceWarning behavior of the Python NI-DAQmx API.
    """

    def test_task_double_close(self, init_kwargs):
        """Test to validate double closure of tasks."""
        with pytest.warns(DaqResourceWarning):
            with nidaqmx.Task(**init_kwargs) as task:
                task.close()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/legacy/test_stream_analog_readers_writers.py sha256=e09c3e47834f627ffe12718332c973a83f1ae32814ef513aec1c96a5d29b8354 bytes=10299 -->
## FILE: tests/legacy/test_stream_analog_readers_writers.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/legacy/test_stream_analog_readers_writers.py`
- sha256: `e09c3e47834f627ffe12718332c973a83f1ae32814ef513aec1c96a5d29b8354`
- bytes: 10299

````python
"""Tests for validating analog read and write operation."""

import random
import time

import numpy
import pytest

from nidaqmx.constants import Edge
from nidaqmx.stream_readers import AnalogMultiChannelReader, AnalogSingleChannelReader
from nidaqmx.stream_writers import AnalogMultiChannelWriter, AnalogSingleChannelWriter
from nidaqmx.utils import flatten_channel_string
from tests.helpers import generate_random_seed
from tests.legacy.test_read_write import TestDAQmxIOBase


class Error(Exception):
    """Base error class."""

    pass


class NoFixtureDetectedError(Error):
    """Custom error class when no fixtures are available."""

    pass


class TestAnalogSingleChannelReaderWriter(TestDAQmxIOBase):
    """Contains a collection of pytest tests.

    These validate the analog single channel stream reader and writer in the NI-DAQmx Python API.
    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_one_sample(self, generate_task, real_x_series_device, seed):
        """Test to validate read and write analog data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        # Select a random loopback channel pair on the device.
        loopback_channel_pairs = self._get_analog_loopback_channels(real_x_series_device)
        loopback_channel_pair = random.choice(loopback_channel_pairs)

        write_task = generate_task()
        read_task = generate_task()
        write_task.ao_channels.add_ao_voltage_chan(
            loopback_channel_pair.output_channel, max_val=10, min_val=-10
        )

        read_task.ai_channels.add_ai_voltage_chan(
            loopback_channel_pair.input_channel, max_val=10, min_val=-10
        )

        writer = AnalogSingleChannelWriter(write_task.out_stream)
        reader = AnalogSingleChannelReader(read_task.in_stream)

        # Generate random values to test.
        values_to_test = [random.uniform(-10, 10) for _ in range(10)]

        values_read = []
        for value_to_test in values_to_test:
            writer.write_one_sample(value_to_test)
            time.sleep(0.001)

            value_read = reader.read_one_sample()
            assert isinstance(value_read, float)
            values_read.append(value_read)

        numpy.testing.assert_allclose(values_read, values_to_test, rtol=0.05, atol=0.005)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_many_sample(self, generate_task, real_x_series_device, seed):
        """Test to validate read and write analog data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(20, 100)
        sample_rate = random.uniform(1000, 5000)

        # Select a random loopback channel pair on the device.
        loopback_channel_pairs = self._get_analog_loopback_channels(real_x_series_device)
        loopback_channel_pair = random.choice(loopback_channel_pairs)

        write_task = generate_task()
        read_task = generate_task()
        sample_clk_task = generate_task()

        # Use a counter output pulse train task as the sample clock source
        # for both the AI and AO tasks.
        sample_clk_task.co_channels.add_co_pulse_chan_freq(
            f"{real_x_series_device.name}/ctr0", freq=sample_rate
        )
        sample_clk_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples)

        samp_clk_terminal = f"/{real_x_series_device.name}/Ctr0InternalOutput"

        write_task.ao_channels.add_ao_voltage_chan(
            loopback_channel_pair.output_channel, max_val=10, min_val=-10
        )
        write_task.timing.cfg_samp_clk_timing(
            sample_rate,
            source=samp_clk_terminal,
            active_edge=Edge.RISING,
            samps_per_chan=number_of_samples,
        )

        read_task.ai_channels.add_ai_voltage_chan(
            loopback_channel_pair.input_channel, max_val=10, min_val=-10
        )
        read_task.timing.cfg_samp_clk_timing(
            sample_rate,
            source=samp_clk_terminal,
            active_edge=Edge.FALLING,
            samps_per_chan=number_of_samples,
        )

        writer = AnalogSingleChannelWriter(write_task.out_stream)
        reader = AnalogSingleChannelReader(read_task.in_stream)

        # Generate random values to test.
        values_to_test = numpy.array(
            [random.uniform(-10, 10) for _ in range(number_of_samples)], dtype=numpy.float64
        )
        writer.write_many_sample(values_to_test)

        # Start the read and write tasks before starting the sample clock
        # source task.
        read_task.start()
        write_task.start()
        sample_clk_task.start()

        values_read = numpy.zeros(number_of_samples, dtype=numpy.float64)
        reader.read_many_sample(
            values_read, number_of_samples_per_channel=number_of_samples, timeout=2
        )

        numpy.testing.assert_allclose(values_read, values_to_test, rtol=0.05, atol=0.005)


class TestAnalogMultiChannelReaderWriter(TestDAQmxIOBase):
    """Contains a collection of pytest tests.

    These validate the analog multi channel stream reader and writer in the NI-DAQmx Python API.
    These tests use only a single X Series device by utilizing the internal loopback routes
    on the device.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_one_sample(self, generate_task, real_x_series_device, seed):
        """Test to validate read and write multichannel analog data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        # Select a random loopback channel pair on the device.
        loopback_channel_pairs = self._get_analog_loopback_channels(real_x_series_device)

        number_of_channels = random.randint(2, len(loopback_channel_pairs))
        channels_to_test = random.sample(loopback_channel_pairs, number_of_channels)

        write_task = generate_task()
        read_task = generate_task()
        write_task.ao_channels.add_ao_voltage_chan(
            flatten_channel_string([c.output_channel for c in channels_to_test]),
            max_val=10,
            min_val=-10,
        )

        read_task.ai_channels.add_ai_voltage_chan(
            flatten_channel_string([c.input_channel for c in channels_to_test]),
            max_val=10,
            min_val=-10,
        )

        writer = AnalogMultiChannelWriter(write_task.out_stream)
        reader = AnalogMultiChannelReader(read_task.in_stream)

        values_to_test = numpy.array(
            [random.uniform(-10, 10) for _ in range(number_of_channels)], dtype=numpy.float64
        )
        writer.write_one_sample(values_to_test)
        time.sleep(0.001)

        values_read = numpy.zeros(number_of_channels, dtype=numpy.float64)
        reader.read_one_sample(values_read)

        numpy.testing.assert_allclose(values_read, values_to_test, rtol=0.05, atol=0.005)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_many_sample(self, generate_task, real_x_series_device, seed):
        """Test to validate read and write multichannel analog data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(20, 100)
        sample_rate = random.uniform(1000, 5000)

        # Select a random loopback channel pair on the device.
        loopback_channel_pairs = self._get_analog_loopback_channels(real_x_series_device)

        number_of_channels = random.randint(2, len(loopback_channel_pairs))
        channels_to_test = random.sample(loopback_channel_pairs, number_of_channels)

        write_task = generate_task()
        read_task = generate_task()
        sample_clk_task = generate_task()
        # Use a counter output pulse train task as the sample clock source
        # for both the AI and AO tasks.
        sample_clk_task.co_channels.add_co_pulse_chan_freq(
            f"{real_x_series_device.name}/ctr0", freq=sample_rate
        )
        sample_clk_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples)

        samp_clk_terminal = f"/{real_x_series_device.name}/Ctr0InternalOutput"

        write_task.ao_channels.add_ao_voltage_chan(
            flatten_channel_string([c.output_channel for c in channels_to_test]),
            max_val=10,
            min_val=-10,
        )
        write_task.timing.cfg_samp_clk_timing(
            sample_rate,
            source=samp_clk_terminal,
            active_edge=Edge.RISING,
            samps_per_chan=number_of_samples,
        )

        read_task.ai_channels.add_ai_voltage_chan(
            flatten_channel_string([c.input_channel for c in channels_to_test]),
            max_val=10,
            min_val=-10,
        )
        read_task.timing.cfg_samp_clk_timing(
            sample_rate,
            source=samp_clk_terminal,
            active_edge=Edge.FALLING,
            samps_per_chan=number_of_samples,
        )

        writer = AnalogMultiChannelWriter(write_task.out_stream)
        reader = AnalogMultiChannelReader(read_task.in_stream)

        values_to_test = numpy.array(
            [
                [random.uniform(-10, 10) for _ in range(number_of_samples)]
                for _ in range(number_of_channels)
            ],
            dtype=numpy.float64,
        )
        writer.write_many_sample(values_to_test)

        # Start the read and write tasks before starting the sample clock
        # source task.
        read_task.start()
        write_task.start()
        sample_clk_task.start()

        values_read = numpy.zeros((number_of_channels, number_of_samples), dtype=numpy.float64)
        reader.read_many_sample(
            values_read, number_of_samples_per_channel=number_of_samples, timeout=2
        )

        numpy.testing.assert_allclose(values_read, values_to_test, rtol=0.05, atol=0.005)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/legacy/test_stream_counter_readers_writers.py sha256=c559850d6a9ace67878310ec9ef5025cd14fc86745f851ffe157935df5cf2b43 bytes=18827 -->
## FILE: tests/legacy/test_stream_counter_readers_writers.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/legacy/test_stream_counter_readers_writers.py`
- sha256: `c559850d6a9ace67878310ec9ef5025cd14fc86745f851ffe157935df5cf2b43`
- bytes: 18827

````python
"""Tests for validating counter read and write operation."""

import random

import numpy
import pytest

from nidaqmx.constants import AcquisitionType, Edge, Level, TaskMode, TriggerType
from nidaqmx.stream_readers import CounterReader
from nidaqmx.stream_writers import CounterWriter
from tests.helpers import generate_random_seed
from tests.legacy.test_read_write import TestDAQmxIOBase


class TestCounterReaderWriter(TestDAQmxIOBase):
    """Contains a collection of pytest tests.

    These validate the counter Read and Write functions in the NI-DAQmx Python API.
    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_one_sample_uint32(self, generate_task, real_x_series_device, seed):
        """Test to validate counter read and write operation with sample data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_pulses = random.randint(2, 50)
        frequency = random.uniform(1000, 10000)

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 2)

        write_task = generate_task()
        read_task = generate_task()
        write_task.co_channels.add_co_pulse_chan_freq(counters[0], freq=frequency)
        write_task.timing.cfg_implicit_timing(samps_per_chan=number_of_pulses)

        read_task.ci_channels.add_ci_count_edges_chan(counters[1])
        read_task.ci_channels.all.ci_count_edges_term = f"/{counters[0]}InternalOutput"

        reader = CounterReader(read_task.in_stream)

        read_task.start()
        write_task.start()

        write_task.wait_until_done(timeout=2)

        value_read = reader.read_one_sample_uint32()
        assert value_read == number_of_pulses

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_multi_sample_uint32(self, generate_task, real_x_series_device, seed):
        """Test to validate counter read and write operation with sample data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(2, 50)
        frequency = random.uniform(1000, 10000)

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 3)

        write_task = generate_task()
        read_task = generate_task()
        sample_clk_task = generate_task()

        # Create a finite pulse train task that acts as the sample clock
        # for the read task and the arm start trigger for the write task.
        sample_clk_task.co_channels.add_co_pulse_chan_freq(counters[0], freq=frequency)
        actual_frequency = sample_clk_task.co_channels.all.co_pulse_freq
        sample_clk_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples)
        samp_clk_terminal = f"/{counters[0]}InternalOutput"

        write_task.co_channels.add_co_pulse_chan_freq(counters[1], freq=actual_frequency)
        write_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples)
        write_task.triggers.arm_start_trigger.trig_type = TriggerType.DIGITAL_EDGE
        write_task.triggers.arm_start_trigger.dig_edge_edge = Edge.RISING
        write_task.triggers.arm_start_trigger.dig_edge_src = samp_clk_terminal

        read_task.ci_channels.add_ci_count_edges_chan(counters[2], edge=Edge.RISING)
        read_task.ci_channels.all.ci_count_edges_term = f"/{counters[1]}InternalOutput"
        read_task.timing.cfg_samp_clk_timing(
            actual_frequency,
            source=samp_clk_terminal,
            active_edge=Edge.FALLING,
            samps_per_chan=number_of_samples,
        )

        read_task.start()
        write_task.start()
        sample_clk_task.start()
        sample_clk_task.wait_until_done(timeout=2)

        reader = CounterReader(read_task.in_stream)

        values_read = numpy.zeros(number_of_samples, dtype=numpy.uint32)
        reader.read_many_sample_uint32(
            values_read, number_of_samples_per_channel=number_of_samples, timeout=2
        )

        expected_values = [i + 1 for i in range(number_of_samples)]

        assert values_read.tolist() == expected_values

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_one_sample_double(self, generate_task, real_x_series_device, seed):
        """Test to validate counter read and write operation with sample data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        frequency = random.uniform(1000, 10000)

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 2)

        write_task = generate_task()
        read_task = generate_task()
        write_task.co_channels.add_co_pulse_chan_freq(counters[0], freq=frequency)
        write_task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)
        actual_frequency = write_task.co_channels.all.co_pulse_freq

        read_task.ci_channels.add_ci_freq_chan(counters[1], min_val=1000, max_val=10000)
        read_task.ci_channels.all.ci_freq_term = f"/{counters[0]}InternalOutput"

        reader = CounterReader(read_task.in_stream)

        read_task.start()
        write_task.start()

        value_read = reader.read_one_sample_double()

        numpy.testing.assert_allclose([value_read], [actual_frequency], rtol=0.05)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_multi_sample_double(self, generate_task, real_x_series_device, seed):
        """Test to validate counter read and write operation with sample data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(2, 50)
        frequency = random.uniform(1000, 10000)

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 3)

        write_task = generate_task()
        read_task = generate_task()
        write_task.co_channels.add_co_pulse_chan_freq(counters[1], freq=frequency)
        write_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples + 1)

        read_task.ci_channels.add_ci_freq_chan(
            counters[2], min_val=1000, max_val=10000, edge=Edge.RISING
        )
        read_task.ci_channels.all.ci_freq_term = f"/{counters[1]}InternalOutput"
        read_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples)

        read_task.start()
        write_task.start()
        write_task.wait_until_done(timeout=2)

        reader = CounterReader(read_task.in_stream)

        values_read = numpy.zeros(number_of_samples, dtype=numpy.float64)
        reader.read_many_sample_double(
            values_read, number_of_samples_per_channel=number_of_samples, timeout=2
        )

        expected_values = [frequency for _ in range(number_of_samples)]

        numpy.testing.assert_allclose(values_read, expected_values, rtol=0.05)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_one_sample_pulse_freq(self, generate_task, real_x_series_device, seed):
        """Test to validate counter read and write operation with sample data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        frequency = random.uniform(1000, 10000)
        duty_cycle = random.uniform(0.2, 0.8)

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 2)

        write_task = generate_task()
        read_task = generate_task()
        write_task.co_channels.add_co_pulse_chan_freq(
            counters[0], freq=frequency, duty_cycle=duty_cycle
        )
        write_task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)

        read_task.ci_channels.add_ci_pulse_chan_freq(counters[1], min_val=1000, max_val=10000)
        read_task.ci_channels.all.ci_pulse_freq_term = f"/{counters[0]}InternalOutput"

        read_task.start()
        write_task.start()

        reader = CounterReader(read_task.in_stream)

        value_read = reader.read_one_sample_pulse_frequency()
        write_task.stop()

        assert numpy.isclose(value_read.freq, frequency, rtol=0.05)
        assert numpy.isclose(value_read.duty_cycle, duty_cycle, rtol=0.05)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_many_sample_pulse_freq(self, generate_task, real_x_series_device, seed):
        """Test to validate counter read and write operation with sample data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(2, 50)

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 2)

        write_task = generate_task()
        read_task = generate_task()
        write_task.co_channels.add_co_pulse_chan_freq(counters[0], idle_state=Level.HIGH)
        write_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples + 1)
        write_task.control(TaskMode.TASK_COMMIT)

        read_task.ci_channels.add_ci_pulse_chan_freq(counters[1], min_val=1000, max_val=10000)
        read_task.ci_channels.all.ci_pulse_freq_term = f"/{counters[0]}InternalOutput"
        read_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples)

        frequencies_to_test = numpy.array(
            [random.uniform(1000, 10000) for _ in range(number_of_samples + 1)],
            dtype=numpy.float64,
        )

        duty_cycles_to_test = numpy.array(
            [random.uniform(0.2, 0.8) for _ in range(number_of_samples + 1)],
            dtype=numpy.float64,
        )

        writer = CounterWriter(write_task.out_stream)
        reader = CounterReader(read_task.in_stream)

        writer.write_many_sample_pulse_frequency(frequencies_to_test, duty_cycles_to_test)

        read_task.start()
        write_task.start()

        frequencies_read = numpy.zeros(number_of_samples, dtype=numpy.float64)
        duty_cycles_read = numpy.zeros(number_of_samples, dtype=numpy.float64)

        reader.read_many_sample_pulse_frequency(
            frequencies_read,
            duty_cycles_read,
            number_of_samples_per_channel=number_of_samples,
            timeout=2,
        )

        numpy.testing.assert_allclose(frequencies_read, frequencies_to_test[1:], rtol=0.05)
        numpy.testing.assert_allclose(duty_cycles_read, duty_cycles_to_test[1:], rtol=0.05)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_one_sample_pulse_time(self, generate_task, real_x_series_device, seed):
        """Test to validate counter read and write operation with sample data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        high_time = random.uniform(0.0001, 0.001)
        low_time = random.uniform(0.0001, 0.001)

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 2)

        write_task = generate_task()
        read_task = generate_task()
        write_task.co_channels.add_co_pulse_chan_time(
            counters[0], high_time=high_time, low_time=low_time
        )
        write_task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)

        read_task.ci_channels.add_ci_pulse_chan_time(counters[1], min_val=0.0001, max_val=0.001)
        read_task.ci_channels.all.ci_pulse_time_term = f"/{counters[0]}InternalOutput"

        read_task.start()
        write_task.start()

        reader = CounterReader(read_task.in_stream)
        value_read = reader.read_one_sample_pulse_time()
        write_task.stop()

        assert numpy.isclose(value_read.high_time, high_time, rtol=0.05)
        assert numpy.isclose(value_read.low_time, low_time, rtol=0.05)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_many_sample_pulse_time(self, generate_task, real_x_series_device, seed):
        """Test to validate counter read and write operation with sample data ."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(2, 50)

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 2)

        write_task = generate_task()
        read_task = generate_task()
        write_task.co_channels.add_co_pulse_chan_time(counters[0], idle_state=Level.HIGH)
        write_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples + 1)
        write_task.control(TaskMode.TASK_COMMIT)

        read_task.ci_channels.add_ci_pulse_chan_time(counters[1], min_val=0.0001, max_val=0.001)
        read_task.ci_channels.all.ci_pulse_time_term = f"/{counters[0]}InternalOutput"
        read_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples)

        high_times_to_test = numpy.array(
            [random.uniform(0.0001, 0.001) for _ in range(number_of_samples + 1)],
            dtype=numpy.float64,
        )

        low_times_to_test = numpy.array(
            [random.uniform(0.0001, 0.001) for _ in range(number_of_samples + 1)],
            dtype=numpy.float64,
        )

        writer = CounterWriter(write_task.out_stream)
        reader = CounterReader(read_task.in_stream)

        writer.write_many_sample_pulse_time(high_times_to_test, low_times_to_test)

        read_task.start()
        write_task.start()

        high_times_read = numpy.zeros(number_of_samples, dtype=numpy.float64)
        low_times_read = numpy.zeros(number_of_samples, dtype=numpy.float64)

        reader.read_many_sample_pulse_time(
            high_times_read,
            low_times_read,
            number_of_samples_per_channel=number_of_samples,
            timeout=2,
        )

        numpy.testing.assert_allclose(high_times_read, high_times_to_test[1:], rtol=0.05)
        numpy.testing.assert_allclose(low_times_read, low_times_to_test[1:], rtol=0.05)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_pulse_ticks_1_samp(self, generate_task, real_x_series_device, seed):
        """Test to validate counter read and write operation with pulse ticks."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        high_ticks = random.randint(100, 1000)
        low_ticks = random.randint(100, 1000)
        starting_edge = random.choice([Edge.RISING, Edge.FALLING])

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 2)

        write_task = generate_task()
        read_task = generate_task()
        write_task.co_channels.add_co_pulse_chan_ticks(
            counters[0],
            f"/{real_x_series_device.name}/100kHzTimebase",
            high_ticks=high_ticks,
            low_ticks=low_ticks,
        )
        write_task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)

        read_task.ci_channels.add_ci_pulse_chan_ticks(
            counters[1],
            source_terminal=f"/{real_x_series_device.name}/100kHzTimebase",
            min_val=100,
            max_val=1000,
        )
        read_task.ci_channels.all.ci_pulse_ticks_term = f"/{counters[0]}InternalOutput"
        read_task.ci_channels.all.ci_pulse_ticks_starting_edge = starting_edge

        read_task.start()
        write_task.start()

        reader = CounterReader(read_task.in_stream)
        value_read = reader.read_one_sample_pulse_ticks()
        write_task.stop()

        assert numpy.isclose(value_read.high_tick, high_ticks, rtol=0.05, atol=1)
        assert numpy.isclose(value_read.low_tick, low_ticks, rtol=0.05, atol=1)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_many_sample_pulse_ticks(self, generate_task, real_x_series_device, seed):
        """Test to validate counter read and write operation with pulse ticks."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(2, 50)

        # Select random counters from the device.
        counters = random.sample(self._get_device_counters(real_x_series_device), 2)

        write_task = generate_task()
        read_task = generate_task()
        write_task.co_channels.add_co_pulse_chan_ticks(
            counters[0],
            f"/{real_x_series_device.name}/100kHzTimebase",
            idle_state=Level.HIGH,
        )
        write_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples + 1)
        write_task.control(TaskMode.TASK_COMMIT)

        read_task.ci_channels.add_ci_pulse_chan_ticks(
            counters[1],
            source_terminal=f"/{real_x_series_device.name}/100kHzTimebase",
            min_val=100,
            max_val=1000,
        )
        read_task.ci_channels.all.ci_pulse_ticks_term = f"/{counters[0]}InternalOutput"
        read_task.timing.cfg_implicit_timing(samps_per_chan=number_of_samples)

        high_ticks_to_test = numpy.array(
            [random.randint(100, 1000) for _ in range(number_of_samples + 1)],
            dtype=numpy.uint32,
        )

        low_ticks_to_test = numpy.array(
            [random.randint(100, 1000) for _ in range(number_of_samples + 1)],
            dtype=numpy.uint32,
        )

        writer = CounterWriter(write_task.out_stream)
        reader = CounterReader(read_task.in_stream)

        writer.write_many_sample_pulse_ticks(high_ticks_to_test, low_ticks_to_test)

        read_task.start()
        write_task.start()

        high_ticks_read = numpy.zeros(number_of_samples, dtype=numpy.uint32)
        low_ticks_read = numpy.zeros(number_of_samples, dtype=numpy.uint32)

        reader.read_many_sample_pulse_ticks(
            high_ticks_read,
            low_ticks_read,
            number_of_samples_per_channel=number_of_samples,
            timeout=2,
        )

        numpy.testing.assert_allclose(high_ticks_read, high_ticks_to_test[1:], rtol=0.05, atol=1)
        numpy.testing.assert_allclose(low_ticks_read, low_ticks_to_test[1:], rtol=0.05, atol=1)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/legacy/test_stream_digital_readers_writers.py sha256=7c13603080cc133ae6ba23f15f5a99e4a69b80242152df70b18a4c6120c71f3a bytes=26542 -->
## FILE: tests/legacy/test_stream_digital_readers_writers.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/legacy/test_stream_digital_readers_writers.py`
- sha256: `7c13603080cc133ae6ba23f15f5a99e4a69b80242152df70b18a4c6120c71f3a`
- bytes: 26542

````python
"""Tests for validating digital read and write operation."""

import random
import time

import numpy
import pytest

from nidaqmx.constants import LineGrouping
from nidaqmx.stream_readers import DigitalMultiChannelReader, DigitalSingleChannelReader
from nidaqmx.stream_writers import DigitalMultiChannelWriter, DigitalSingleChannelWriter
from nidaqmx.utils import flatten_channel_string
from tests.helpers import generate_random_seed
from tests.legacy.test_read_write import TestDAQmxIOBase


class TestDigitalSingleChannelReaderWriter(TestDAQmxIOBase):
    """Contains a collection of pytest tests.

    These validate the digital single channel readers and writers in the NI-DAQmx Python API.
    These tests use only a single X Series device by both writing to and reading from ONLY
    the digital output lines.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_one_sample_one_line(self, task, real_x_series_device, seed):
        """Test to validate digital read and write operation with sample data."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        do_line = random.choice(real_x_series_device.do_lines).name

        task.do_channels.add_do_chan(do_line, line_grouping=LineGrouping.CHAN_PER_LINE)

        writer = DigitalSingleChannelWriter(task.out_stream)
        reader = DigitalSingleChannelReader(task.in_stream)

        # Generate random values to test.
        values_to_test = [bool(random.getrandbits(1)) for _ in range(10)]

        values_read = []
        for value_to_test in values_to_test:
            writer.write_one_sample_one_line(value_to_test)
            time.sleep(0.001)
            values_read.append(reader.read_one_sample_one_line())

        numpy.testing.assert_array_equal(values_read, values_to_test)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_one_sample_multi_line(self, task, real_x_series_device, seed):
        """Test to validate digital read and write operation with sample data."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_lines = random.randint(2, len(real_x_series_device.do_lines))
        do_lines = random.sample(real_x_series_device.do_lines, number_of_lines)

        task.do_channels.add_do_chan(
            flatten_channel_string([d.name for d in do_lines]),
            line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
        )

        writer = DigitalSingleChannelWriter(task.out_stream)
        reader = DigitalSingleChannelReader(task.in_stream)

        # Generate random values to test.
        values_to_test = numpy.array([bool(random.getrandbits(1)) for _ in range(number_of_lines)])

        writer.write_one_sample_multi_line(values_to_test)
        time.sleep(0.001)

        values_read = numpy.zeros(number_of_lines, dtype=bool)
        reader.read_one_sample_multi_line(values_read)

        numpy.testing.assert_array_equal(values_read, values_to_test)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_one_sample_port_byte(self, task, real_x_series_device, seed):
        """Test to validate digital read and write operation with sample port byte."""
        if not any([d.do_port_width <= 8 for d in real_x_series_device.do_ports]):
            pytest.skip("Requires digital port with at most 8 lines.")

        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        do_port = random.choice([d for d in real_x_series_device.do_ports if d.do_port_width <= 8])

        task.do_channels.add_do_chan(do_port.name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

        # Generate random values to test.
        values_to_test = [int(random.getrandbits(do_port.do_port_width)) for _ in range(10)]

        writer = DigitalSingleChannelWriter(task.out_stream)
        reader = DigitalSingleChannelReader(task.in_stream)

        values_read = []
        for value_to_test in values_to_test:
            writer.write_one_sample_port_byte(value_to_test)
            time.sleep(0.001)
            values_read.append(reader.read_one_sample_port_byte())

        numpy.testing.assert_array_equal(values_read, values_to_test)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_one_sample_port_uint16(self, task, real_x_series_device, seed):
        """Test to validate digital read and write operation with sample uint16."""
        if not any([d.do_port_width <= 16 for d in real_x_series_device.do_ports]):
            pytest.skip("Requires digital port with at most 16 lines.")

        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        do_port = random.choice(
            [do for do in real_x_series_device.do_ports if do.do_port_width <= 16]
        )

        task.do_channels.add_do_chan(do_port.name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

        # Generate random values to test.
        values_to_test = [int(random.getrandbits(do_port.do_port_width)) for _ in range(10)]

        writer = DigitalSingleChannelWriter(task.out_stream)
        reader = DigitalSingleChannelReader(task.in_stream)

        values_read = []
        for value_to_test in values_to_test:
            writer.write_one_sample_port_uint16(value_to_test)
            time.sleep(0.001)
            values_read.append(reader.read_one_sample_port_uint16())

        numpy.testing.assert_array_equal(values_read, values_to_test)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_one_sample_port_uint32(self, task, real_x_series_device, seed):
        """Test to validate digital read and write operation with sample uint32."""
        if not any([d.do_port_width <= 32 for d in real_x_series_device.do_ports]):
            pytest.skip("Requires digital port with at most 32 lines.")

        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        do_port = random.choice(
            [do for do in real_x_series_device.do_ports if do.do_port_width <= 32]
        )

        task.do_channels.add_do_chan(do_port.name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

        # Generate random values to test.
        values_to_test = [int(random.getrandbits(do_port.do_port_width)) for _ in range(10)]

        writer = DigitalSingleChannelWriter(task.out_stream)
        reader = DigitalSingleChannelReader(task.in_stream)

        values_read = []
        for value_to_test in values_to_test:
            writer.write_one_sample_port_uint32(value_to_test)
            time.sleep(0.001)
            values_read.append(reader.read_one_sample_port_uint32())

        numpy.testing.assert_array_equal(values_read, values_to_test)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_many_sample_port_byte(self, task, real_x_series_device, seed):
        """Test to validate digital read and write operation with sample byte."""
        if not any([d.do_port_width <= 8 for d in real_x_series_device.do_ports]):
            pytest.skip("Requires digital port with at most 8 lines.")

        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(2, 20)
        do_port = random.choice([d for d in real_x_series_device.do_ports if d.do_port_width <= 8])

        task.do_channels.add_do_chan(do_port.name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

        # Generate random values to test.
        values_to_test = numpy.array(
            [int(random.getrandbits(do_port.do_port_width)) for _ in range(number_of_samples)],
            dtype=numpy.uint8,
        )

        writer = DigitalSingleChannelWriter(task.out_stream)
        reader = DigitalSingleChannelReader(task.in_stream)

        task.start()

        writer.write_many_sample_port_byte(values_to_test)
        time.sleep(0.001)

        # Since we're writing to and reading from ONLY the digital
        # output lines, we can't use sample clocks to correlate the
        # read and write sampling times. Thus, we essentially read
        # the last value written multiple times.
        values_read = numpy.zeros(number_of_samples, dtype=numpy.uint8)
        reader.read_many_sample_port_byte(
            values_read, number_of_samples_per_channel=number_of_samples
        )

        expected_values = [values_to_test[-1] for _ in range(number_of_samples)]
        numpy.testing.assert_array_equal(values_read, expected_values)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_many_sample_port_uint16(self, task, real_x_series_device, seed):
        """Test to validate digital read and write operation with sample uint16."""
        if not any([d.do_port_width <= 16 for d in real_x_series_device.do_ports]):
            pytest.skip("Requires digital port with at most 16 lines.")

        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(2, 20)
        do_port = random.choice([d for d in real_x_series_device.do_ports if d.do_port_width <= 16])

        task.do_channels.add_do_chan(do_port.name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

        # Generate random values to test.
        values_to_test = numpy.array(
            [int(random.getrandbits(do_port.do_port_width)) for _ in range(number_of_samples)],
            dtype=numpy.uint16,
        )

        writer = DigitalSingleChannelWriter(task.out_stream)
        reader = DigitalSingleChannelReader(task.in_stream)

        task.start()

        writer.write_many_sample_port_uint16(values_to_test)
        time.sleep(0.001)

        # Since we're writing to and reading from ONLY the digital
        # output lines, we can't use sample clocks to correlate the
        # read and write sampling times. Thus, we essentially read
        # the last value written multiple times.
        values_read = numpy.zeros(number_of_samples, dtype=numpy.uint16)
        reader.read_many_sample_port_uint16(
            values_read, number_of_samples_per_channel=number_of_samples
        )

        expected_values = [values_to_test[-1] for _ in range(number_of_samples)]
        numpy.testing.assert_array_equal(values_read, expected_values)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_many_sample_port_uint32(self, task, real_x_series_device, seed):
        """Test to validate digital read and write operation with sample uint32."""
        if not any([d.do_port_width <= 32 for d in real_x_series_device.do_ports]):
            pytest.skip("Requires digital port with at most 32 lines.")

        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(2, 20)
        do_port = random.choice([d for d in real_x_series_device.do_ports if d.do_port_width <= 32])

        task.do_channels.add_do_chan(do_port.name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

        # Generate random values to test.
        values_to_test = numpy.array(
            [int(random.getrandbits(do_port.do_port_width)) for _ in range(number_of_samples)],
            dtype=numpy.uint32,
        )

        writer = DigitalSingleChannelWriter(task.out_stream)
        reader = DigitalSingleChannelReader(task.in_stream)

        task.start()

        writer.write_many_sample_port_uint32(values_to_test)
        time.sleep(0.001)

        # Since we're writing to and reading from ONLY the digital
        # output lines, we can't use sample clocks to correlate the
        # read and write sampling times. Thus, we essentially read
        # the last value written multiple times.
        values_read = numpy.zeros(number_of_samples, dtype=numpy.uint32)
        reader.read_many_sample_port_uint32(
            values_read, number_of_samples_per_channel=number_of_samples
        )

        expected_values = [values_to_test[-1] for _ in range(number_of_samples)]
        numpy.testing.assert_array_equal(values_read, expected_values)


class TestDigitalMultiChannelReaderWriter(TestDAQmxIOBase):
    """Contains a collection of pytest tests.

    These validate the digital multi channel readers and writers in the NI-DAQmx Python API.
    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_one_sample_one_line(self, task, real_x_series_device, seed):
        """Test to validate digital multichannel read and write operation with sample data."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_channels = random.randint(2, len(real_x_series_device.do_lines))
        do_lines = random.sample(real_x_series_device.do_lines, number_of_channels)

        task.do_channels.add_do_chan(
            flatten_channel_string([d.name for d in do_lines]),
            line_grouping=LineGrouping.CHAN_PER_LINE,
        )

        writer = DigitalMultiChannelWriter(task.out_stream)
        reader = DigitalMultiChannelReader(task.in_stream)

        # Generate random values to test.
        values_to_test = numpy.array(
            [bool(random.getrandbits(1)) for _ in range(number_of_channels)]
        )

        writer.write_one_sample_one_line(values_to_test)
        time.sleep(0.001)

        values_read = numpy.zeros(number_of_channels, dtype=bool)
        reader.read_one_sample_one_line(values_read)

        numpy.testing.assert_array_equal(values_read, values_to_test)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_one_sample_multi_line(self, task, real_x_series_device, seed):
        """Test to validate digital multichannel read and write operation with sample data."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        num_lines = random.randint(2, 4)
        number_of_channels = random.randint(
            2, int(numpy.floor(len(real_x_series_device.do_lines) / float(num_lines)))
        )

        all_lines = random.sample(real_x_series_device.do_lines, num_lines * number_of_channels)

        for i in range(number_of_channels):
            do_lines = all_lines[i * num_lines : (i + 1) * num_lines]

            task.do_channels.add_do_chan(
                flatten_channel_string([d.name for d in do_lines]),
                line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
            )

        writer = DigitalMultiChannelWriter(task.out_stream)
        reader = DigitalMultiChannelReader(task.in_stream)

        # Generate random values to test.
        values_to_test = numpy.array(
            [
                [bool(random.getrandbits(1)) for _ in range(num_lines)]
                for _ in range(number_of_channels)
            ]
        )

        writer.write_one_sample_multi_line(values_to_test)
        time.sleep(0.001)

        values_read = numpy.zeros((number_of_channels, num_lines), dtype=bool)
        reader.read_one_sample_multi_line(values_read)

        numpy.testing.assert_array_equal(values_read, values_to_test)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_one_sample_port_byte(self, task, real_x_series_device, seed):
        """Test to validate digital multichannel read and write operation with sample bytes."""
        if len([d.do_port_width <= 8 for d in real_x_series_device.do_ports]) < 2:
            pytest.skip("Requires 2 digital ports with at most 8 lines.")

        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        all_ports = [d for d in real_x_series_device.do_ports if d.do_port_width <= 8]
        number_of_channels = random.randint(2, len(all_ports))
        do_ports = random.sample(all_ports, number_of_channels)

        for do_port in do_ports:
            task.do_channels.add_do_chan(
                do_port.name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
            )

        # Generate random values to test.
        values_to_test = numpy.array(
            [int(random.getrandbits(d.do_port_width)) for d in do_ports], dtype=numpy.uint8
        )

        writer = DigitalMultiChannelWriter(task.out_stream)
        reader = DigitalMultiChannelReader(task.in_stream)

        writer.write_one_sample_port_byte(values_to_test)
        time.sleep(0.001)

        values_read = numpy.zeros(number_of_channels, dtype=numpy.uint8)
        reader.read_one_sample_port_byte(values_read)

        numpy.testing.assert_array_equal(values_read, values_to_test)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_one_sample_port_uint16(self, task, real_x_series_device, seed):
        """Test to validate digital multichannel read and write operation with uint16."""
        if len([d.do_port_width <= 16 for d in real_x_series_device.do_ports]) < 2:
            pytest.skip("Requires 2 digital ports with at most 16 lines.")

        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        all_ports = [d for d in real_x_series_device.do_ports if d.do_port_width <= 16]
        number_of_channels = random.randint(2, len(all_ports))
        do_ports = random.sample(all_ports, number_of_channels)

        for do_port in do_ports:
            task.do_channels.add_do_chan(
                do_port.name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
            )

        # Generate random values to test.
        values_to_test = numpy.array(
            [int(random.getrandbits(d.do_port_width)) for d in do_ports], dtype=numpy.uint16
        )

        writer = DigitalMultiChannelWriter(task.out_stream)
        reader = DigitalMultiChannelReader(task.in_stream)

        writer.write_one_sample_port_uint16(values_to_test)
        time.sleep(0.001)

        values_read = numpy.zeros(number_of_channels, dtype=numpy.uint16)
        reader.read_one_sample_port_uint16(values_read)

        numpy.testing.assert_array_equal(values_read, values_to_test)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_one_sample_port_uint32(self, task, real_x_series_device, seed):
        """Test to validate digital multichannel read and write operation with uint32."""
        if len([d.do_port_width <= 32 for d in real_x_series_device.do_ports]) < 2:
            pytest.skip("Requires 2 digital ports with at most 32 lines.")

        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        all_ports = [d for d in real_x_series_device.do_ports if d.do_port_width <= 32]
        number_of_channels = random.randint(2, len(all_ports))
        do_ports = random.sample(all_ports, number_of_channels)

        for do_port in do_ports:
            task.do_channels.add_do_chan(
                do_port.name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
            )

        # Generate random values to test.
        values_to_test = numpy.array(
            [int(random.getrandbits(d.do_port_width)) for d in do_ports], dtype=numpy.uint32
        )

        writer = DigitalMultiChannelWriter(task.out_stream)
        reader = DigitalMultiChannelReader(task.in_stream)

        writer.write_one_sample_port_uint32(values_to_test)
        time.sleep(0.001)

        values_read = numpy.zeros(number_of_channels, dtype=numpy.uint32)
        reader.read_one_sample_port_uint32(values_read)

        numpy.testing.assert_array_equal(values_read, values_to_test)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_many_sample_port_byte(self, task, real_x_series_device, seed):
        """Test to validate digital multichannel read and write operation with sample bytes."""
        if len([d.do_port_width <= 8 for d in real_x_series_device.do_ports]) < 2:
            pytest.skip("Requires 2 digital ports with at most 8 lines.")

        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(2, 20)

        all_ports = [d for d in real_x_series_device.do_ports if d.do_port_width <= 8]
        number_of_channels = random.randint(2, len(all_ports))
        do_ports = random.sample(all_ports, number_of_channels)

        for do_port in do_ports:
            task.do_channels.add_do_chan(
                do_port.name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
            )

        # Generate random values to test.
        values_to_test = numpy.array(
            [
                [int(random.getrandbits(do_port.do_port_width)) for _ in range(number_of_samples)]
                for do_port in do_ports
            ],
            dtype=numpy.uint8,
        )

        writer = DigitalMultiChannelWriter(task.out_stream)
        reader = DigitalMultiChannelReader(task.in_stream)

        task.start()

        writer.write_many_sample_port_byte(values_to_test)
        time.sleep(0.001)

        # Since we're writing to and reading from ONLY the digital
        # output lines, we can't use sample clocks to correlate the
        # read and write sampling times. Thus, we essentially read
        # the last value written multiple times.
        values_read = numpy.zeros((number_of_channels, number_of_samples), dtype=numpy.uint8)
        reader.read_many_sample_port_byte(
            values_read, number_of_samples_per_channel=number_of_samples
        )

        expected_values = [
            [values_to_test[i, -1] for _ in range(number_of_samples)]
            for i in range(number_of_channels)
        ]
        numpy.testing.assert_array_equal(values_read, expected_values)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_many_sample_port_uint16(self, task, real_x_series_device, seed):
        """Test to validate digital multichannel read and write operation with uint16."""
        if len([d.do_port_width <= 16 for d in real_x_series_device.do_ports]) < 2:
            pytest.skip("Requires 2 digital ports with at most 16 lines.")

        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(2, 20)

        all_ports = [d for d in real_x_series_device.do_ports if d.do_port_width <= 16]
        number_of_channels = random.randint(2, len(all_ports))
        do_ports = random.sample(all_ports, number_of_channels)

        for do_port in do_ports:
            task.do_channels.add_do_chan(
                do_port.name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
            )

        # Generate random values to test.
        values_to_test = numpy.array(
            [
                [int(random.getrandbits(do_port.do_port_width)) for _ in range(number_of_samples)]
                for do_port in do_ports
            ],
            dtype=numpy.uint16,
        )

        writer = DigitalMultiChannelWriter(task.out_stream)
        reader = DigitalMultiChannelReader(task.in_stream)

        task.start()

        writer.write_many_sample_port_uint16(values_to_test)
        time.sleep(0.001)

        # Since we're writing to and reading from ONLY the digital
        # output lines, we can't use sample clocks to correlate the
        # read and write sampling times. Thus, we essentially read
        # the last value written multiple times.
        values_read = numpy.zeros((number_of_channels, number_of_samples), dtype=numpy.uint16)
        reader.read_many_sample_port_uint16(
            values_read, number_of_samples_per_channel=number_of_samples
        )

        expected_values = [
            [values_to_test[i, -1] for _ in range(number_of_samples)]
            for i in range(number_of_channels)
        ]
        numpy.testing.assert_array_equal(values_read, expected_values)

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_many_sample_port_uint32(self, task, real_x_series_device, seed):
        """Test to validate digital multichannel read and write operation with uint32."""
        if len([d.do_port_width <= 32 for d in real_x_series_device.do_ports]) < 2:
            pytest.skip("Requires 2 digital ports with at most 32 lines.")

        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        number_of_samples = random.randint(2, 20)

        all_ports = [d for d in real_x_series_device.do_ports if d.do_port_width <= 32]
        number_of_channels = random.randint(2, len(all_ports))
        do_ports = random.sample(all_ports, number_of_channels)

        for do_port in do_ports:
            task.do_channels.add_do_chan(
                do_port.name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
            )

        # Generate random values to test.
        values_to_test = numpy.array(
            [
                [int(random.getrandbits(do_port.do_port_width)) for _ in range(number_of_samples)]
                for do_port in do_ports
            ],
            dtype=numpy.uint32,
        )

        writer = DigitalMultiChannelWriter(task.out_stream)
        reader = DigitalMultiChannelReader(task.in_stream)

        task.start()

        writer.write_many_sample_port_uint32(values_to_test)
        time.sleep(0.001)

        # Since we're writing to and reading from ONLY the digital
        # output lines, we can't use sample clocks to correlate the
        # read and write sampling times. Thus, we essentially read
        # the last value written multiple times.
        values_read = numpy.zeros((number_of_channels, number_of_samples), dtype=numpy.uint32)
        reader.read_many_sample_port_uint32(
            values_read, number_of_samples_per_channel=number_of_samples
        )

        expected_values = [
            [values_to_test[i, -1] for _ in range(number_of_samples)]
            for i in range(number_of_channels)
        ]
        numpy.testing.assert_array_equal(values_read, expected_values)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/legacy/test_stream_power_readers.py sha256=de2531f2258d3d5d209ba120d3ba3a09ca16e081e432e0620765656502dd9639 bytes=12654 -->
## FILE: tests/legacy/test_stream_power_readers.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/legacy/test_stream_power_readers.py`
- sha256: `de2531f2258d3d5d209ba120d3ba3a09ca16e081e432e0620765656502dd9639`
- bytes: 12654

````python
"""Tests for validating power read operation."""

import math
import random

import numpy
import pytest

from nidaqmx.stream_readers import (
    PowerBinaryReader,
    PowerMultiChannelReader,
    PowerSingleChannelReader,
)
from tests.helpers import POWER_ABS_EPSILON, generate_random_seed
from tests.legacy.test_read_write import TestDAQmxIOBase


class TestPowerSingleChannelReader(TestDAQmxIOBase):
    """Contains a collection of pytest tests.

    These validate power single channel stream reader in the NI-DAQmx Python API.
    These tests use simulated TestScale PPS device(s), TS-15200.
    """

    # @pytest.mark.skip(reason="DAQmxReadPowerScalarF64 not implemented, yet")
    @pytest.mark.parametrize(
        "seed,output_enable", [(generate_random_seed(), True), (generate_random_seed(), False)]
    )
    def test_power_1_chan_1_samp(self, task, sim_ts_power_device, seed, output_enable):
        """Test to validate power read operation with sample data."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        voltage_setpoint = 0.0
        current_setpoint = 0.03

        task.ai_channels.add_ai_power_chan(
            f"{sim_ts_power_device.name}/power",
            voltage_setpoint,
            current_setpoint,
            output_enable,
        )

        reader = PowerSingleChannelReader(task.in_stream)

        task.start()
        value_read = reader.read_one_sample()

        if output_enable:
            assert value_read.voltage == pytest.approx(voltage_setpoint, abs=POWER_ABS_EPSILON)
            assert value_read.current == pytest.approx(current_setpoint, abs=POWER_ABS_EPSILON)
        else:
            assert math.isnan(value_read.voltage)
            assert math.isnan(value_read.current)

    @pytest.mark.parametrize(
        "seed,output_enable", [(generate_random_seed(), True), (generate_random_seed(), False)]
    )
    def test_power_1_chan_n_samp(self, task, sim_ts_power_device, seed, output_enable):
        """Test to validate power read operation with sample data."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        voltage_setpoint = 0.0
        current_setpoint = 0.03
        number_of_samples_per_channel = 10

        # Fill with bad data to ensure its overwritten by read.
        voltage_data = numpy.full(number_of_samples_per_channel, -1.0, dtype=numpy.float64)
        current_data = numpy.full(number_of_samples_per_channel, -1.0, dtype=numpy.float64)

        task.ai_channels.add_ai_power_chan(
            f"{sim_ts_power_device.name}/power",
            voltage_setpoint,
            current_setpoint,
            output_enable,
        )

        reader = PowerSingleChannelReader(task.in_stream)

        task.start()
        reader.read_many_sample(
            voltage_data,
            current_data,
            number_of_samples_per_channel=number_of_samples_per_channel,
        )

        if output_enable:
            assert all(
                [
                    sample == pytest.approx(voltage_setpoint, abs=POWER_ABS_EPSILON)
                    for sample in voltage_data
                ]
            )
            assert all(
                [
                    sample == pytest.approx(current_setpoint, abs=POWER_ABS_EPSILON)
                    for sample in current_data
                ]
            )
        else:
            assert all([math.isnan(sample) for sample in voltage_data])
            assert all([math.isnan(sample) for sample in current_data])


class TestPowerMultiChannelReader(TestDAQmxIOBase):
    """Contains a collection of pytest tests.

    These validate power multi channel stream reader in the NI-DAQmx Python API.
    These tests use simulated TestScale PPS device(s), TS-15200.
    """

    @pytest.mark.parametrize(
        "seed,output_enables",
        [
            (generate_random_seed(), [True, True]),
            (generate_random_seed(), [True, False]),
            (generate_random_seed(), [False, True]),
            (generate_random_seed(), [False, False]),
        ],
    )
    def test_power_n_chan_1_samp(self, task, sim_ts_power_devices, seed, output_enables):
        """Test to validate multi channel power read operation with sample data."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        voltage_setpoint = 0.0
        current_setpoint = 0.03

        # Fill with bad data to ensure its overwritten by read.
        voltage_data = numpy.full(len(sim_ts_power_devices), -1.0, dtype=numpy.float64)
        current_data = numpy.full(len(sim_ts_power_devices), -1.0, dtype=numpy.float64)

        for device, output_enable in zip(sim_ts_power_devices, output_enables):
            task.ai_channels.add_ai_power_chan(
                f"{device.name}/power", voltage_setpoint, current_setpoint, output_enable
            )

        reader = PowerMultiChannelReader(task.in_stream)

        task.start()
        reader.read_one_sample(voltage_data, current_data)

        for chan_index, output_enable in enumerate(output_enables):
            if output_enable:
                assert voltage_data[chan_index] == pytest.approx(
                    voltage_setpoint, abs=POWER_ABS_EPSILON
                )
                assert current_data[chan_index] == pytest.approx(
                    current_setpoint, abs=POWER_ABS_EPSILON
                )
            else:
                assert math.isnan(voltage_data[chan_index])
                assert math.isnan(current_data[chan_index])

    @pytest.mark.parametrize(
        "seed,output_enables",
        [
            (generate_random_seed(), [True, True]),
            (generate_random_seed(), [True, False]),
            (generate_random_seed(), [False, True]),
            (generate_random_seed(), [False, False]),
        ],
    )
    def test_power_n_chan_n_samp(self, task, sim_ts_power_devices, seed, output_enables):
        """Test to validate multi channel power read operation with sample data."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        voltage_setpoint = 0.0
        current_setpoint = 0.03
        number_of_samples_per_channel = 10

        # Fill with bad data to ensure its overwritten by read.
        voltage_data = numpy.full(
            (len(sim_ts_power_devices), number_of_samples_per_channel), -1.0, dtype=numpy.float64
        )
        current_data = numpy.full(
            (len(sim_ts_power_devices), number_of_samples_per_channel), -1.0, dtype=numpy.float64
        )

        for device, output_enable in zip(sim_ts_power_devices, output_enables):
            task.ai_channels.add_ai_power_chan(
                f"{device.name}/power", voltage_setpoint, current_setpoint, output_enable
            )

        reader = PowerMultiChannelReader(task.in_stream)

        task.start()
        reader.read_many_sample(
            voltage_data,
            current_data,
            number_of_samples_per_channel=number_of_samples_per_channel,
        )

        for chan_index, output_enable in enumerate(output_enables):
            # Get the data for just this channel
            voltage_channel_data = voltage_data[chan_index]
            current_channel_data = current_data[chan_index]
            if output_enable:
                assert all(
                    [
                        sample == pytest.approx(voltage_setpoint, abs=POWER_ABS_EPSILON)
                        for sample in voltage_channel_data
                    ]
                )
                assert all(
                    [
                        sample == pytest.approx(current_setpoint, abs=POWER_ABS_EPSILON)
                        for sample in current_channel_data
                    ]
                )
            else:
                assert all([math.isnan(sample) for sample in voltage_channel_data])
                assert all([math.isnan(sample) for sample in current_channel_data])


class TestPowerBinaryReader(TestDAQmxIOBase):
    """Contains a collection of pytest tests.

    These validate power binary stream reader in the NI-DAQmx Python API.
    These tests use simulated TestScale PPS device(s), TS-15200.
    """

    @pytest.mark.parametrize(
        "seed,output_enable", [(generate_random_seed(), True), (generate_random_seed(), False)]
    )
    def test_power_1_chan_n_samp_binary(self, task, sim_ts_power_device, seed, output_enable):
        """Test to validate power binary read operation with sample binary data."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        voltage_setpoint = 0.0
        current_setpoint = 0.03
        number_of_samples_per_channel = 10

        # Fill with bad data to ensure its overwritten by read.
        voltage_data = numpy.full((1, number_of_samples_per_channel), -32768, dtype=numpy.int16)
        current_data = numpy.full((1, number_of_samples_per_channel), -32768, dtype=numpy.int16)

        task.ai_channels.add_ai_power_chan(
            f"{sim_ts_power_device.name}/power",
            voltage_setpoint,
            current_setpoint,
            output_enable,
        )

        reader = PowerBinaryReader(task.in_stream)

        task.start()
        reader.read_many_sample(
            voltage_data,
            current_data,
            number_of_samples_per_channel=number_of_samples_per_channel,
        )

        channel_voltage_data = voltage_data[0]
        channel_current_data = current_data[0]
        if output_enable:
            # Scaling is complicated, just ensure everything was overwritten.
            assert not any([sample == -32768 for sample in channel_voltage_data])
            assert not any([sample == -32768 for sample in channel_current_data])
        else:
            # Simulated data is 0 when output is disabled for binary reads.
            assert all([sample == 0 for sample in channel_voltage_data])
            assert all([sample == 0 for sample in channel_current_data])

    @pytest.mark.parametrize(
        "seed,output_enables",
        [
            (generate_random_seed(), [True, True]),
            (generate_random_seed(), [True, False]),
            (generate_random_seed(), [False, True]),
            (generate_random_seed(), [False, False]),
        ],
    )
    def test_power_n_chan_many_sample_binary(
        self, task, sim_ts_power_devices, seed, output_enables
    ):
        """Test to validate power binary read operation with sample binary data."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        voltage_setpoint = 0.0
        current_setpoint = 0.03
        number_of_samples_per_channel = 10

        # Fill with bad data to ensure its overwritten by read.
        voltage_data = numpy.full(
            (len(sim_ts_power_devices), number_of_samples_per_channel), -32768, dtype=numpy.int16
        )
        current_data = numpy.full(
            (len(sim_ts_power_devices), number_of_samples_per_channel), -32768, dtype=numpy.int16
        )

        for device, output_enable in zip(sim_ts_power_devices, output_enables):
            task.ai_channels.add_ai_power_chan(
                f"{device.name}/power", voltage_setpoint, current_setpoint, output_enable
            )

        reader = PowerBinaryReader(task.in_stream)

        task.start()
        reader.read_many_sample(
            voltage_data,
            current_data,
            number_of_samples_per_channel=number_of_samples_per_channel,
        )

        for chan_index, output_enable in enumerate(output_enables):
            # Get the data for just this channel
            voltage_channel_data = voltage_data[chan_index]
            current_channel_data = current_data[chan_index]
            if output_enable:
                # Scaling is complicated, just ensure everything was overwritten.
                assert not any([sample == -32768 for sample in voltage_channel_data])
                assert not any([sample == -32768 for sample in current_channel_data])
            else:
                # Simulated data is 0 when output is disabled for binary reads.
                assert all([sample == 0 for sample in voltage_channel_data])
                assert all([sample == 0 for sample in current_channel_data])
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/legacy/test_system_collections.py sha256=aa0dfb9ab50d3b2c053f5cfa2ed8be9833720aba00b8bd68c54040a824a6078f bytes=3271 -->
## FILE: tests/legacy/test_system_collections.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/legacy/test_system_collections.py`
- sha256: `aa0dfb9ab50d3b2c053f5cfa2ed8be9833720aba00b8bd68c54040a824a6078f`
- bytes: 3271

````python
"""Tests for validating systems collections."""

import collections.abc

import nidaqmx
import nidaqmx.system
from nidaqmx.system._collections.device_collection import DeviceCollection
from nidaqmx.system._collections.persisted_channel_collection import (
    PersistedChannelCollection,
)
from nidaqmx.system._collections.persisted_scale_collection import (
    PersistedScaleCollection,
)
from nidaqmx.system._collections.persisted_task_collection import (
    PersistedTaskCollection,
)
from nidaqmx.system._collections.physical_channel_collection import (
    PhysicalChannelCollection,
)


class TestSystemCollections:
    """Contains a collection of pytest tests.

    These validate the system collections functionality in the NI-DAQmx Python API.
    """

    def test_devices_collection_property(self, system):
        """Test to validate device collection property."""
        devices = system.devices
        assert isinstance(devices, DeviceCollection)
        assert isinstance(devices, collections.abc.Sequence)

        assert isinstance(devices[0], nidaqmx.system.Device)
        assert isinstance(devices[0].is_simulated, bool)

    def test_persisted_scale_collection_property(self, system):
        """Test to validate persisted scale property."""
        scales = system.scales
        assert isinstance(scales, PersistedScaleCollection)
        assert isinstance(scales, collections.abc.Sequence)

        if len(scales) > 0:
            assert isinstance(scales[0], nidaqmx.system.storage.PersistedScale)

            # Test specific property on object.
            assert isinstance(scales[0].author, str)

    def test_persisted_task_collection_property(self, system):
        """Test to validate persisted task collection property."""
        tasks = system.tasks
        assert isinstance(tasks, PersistedTaskCollection)
        assert isinstance(tasks, collections.abc.Sequence)

        if len(tasks) > 0:
            assert isinstance(tasks[0], nidaqmx.system.storage.PersistedTask)

            # Test specific property on object.
            assert isinstance(tasks[0].author, str)

    def test_persisted_channel_collection_property(self, system):
        """Test to validate persisted channel collection property."""
        global_channels = system.global_channels
        assert isinstance(global_channels, PersistedChannelCollection)
        assert isinstance(global_channels, collections.abc.Sequence)

        if len(global_channels) > 0:
            assert isinstance(global_channels[0], nidaqmx.system.storage.PersistedChannel)

            # Test specific property on object.
            assert isinstance(global_channels[0].author, str)

    def test_physical_channel_collection_property(self, sim_6363_device):
        """Test to validate physical channel collection property."""
        phys_chans = sim_6363_device.ai_physical_chans

        assert isinstance(phys_chans, PhysicalChannelCollection)
        assert isinstance(phys_chans, collections.abc.Sequence)

        assert isinstance(phys_chans[0], nidaqmx.system.PhysicalChannel)

        # Test specific property on object.
        assert isinstance(phys_chans[0].ai_meas_types, list)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/legacy/test_teds.py sha256=f6dab22f3634853be89b195c369e5a1957cd87c0b8a962faeff34771f1a373e0 bytes=1656 -->
## FILE: tests/legacy/test_teds.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/legacy/test_teds.py`
- sha256: `f6dab22f3634853be89b195c369e5a1957cd87c0b8a962faeff34771f1a373e0`
- bytes: 1656

````python
"""Tests for validating TEDS functionality."""

import random

import pytest

from nidaqmx.constants import TEDSUnits, TerminalConfiguration
from tests.helpers import configure_teds, generate_random_seed


class TestTEDS:
    """Contains a collection of pytest tests.

    These validate the TEDS functionality in the NI-DAQmx Python API.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_create_teds_ai_voltage_chan(self, task, sim_6363_device, seed, voltage_teds_file_path):
        """Test to validate TEDS functionality."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        with configure_teds(
            random.choice(sim_6363_device.ai_physical_chans), voltage_teds_file_path
        ) as ai_phys_chan:
            assert ai_phys_chan.teds_mfg_id == 17
            assert ai_phys_chan.teds_model_num == 1
            assert ai_phys_chan.teds_version_letter == "A"
            assert ai_phys_chan.teds_version_num == 1
            assert ai_phys_chan.teds_template_ids == [30]

            ai_channel = task.ai_channels.add_teds_ai_voltage_chan(
                ai_phys_chan.name,
                name_to_assign_to_channel="TEDSVoltageChannel",
                terminal_config=TerminalConfiguration.DEFAULT,
                min_val=-300.0,
                max_val=100.0,
                units=TEDSUnits.FROM_TEDS,
            )

            assert ai_channel.ai_teds_is_teds
            assert ai_channel.ai_teds_units == "Kelvin"
            assert ai_channel.ai_min == -300.0
            assert ai_channel.ai_max == 100.0
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/legacy/test_triggers.py sha256=0e8548ba7c6f06892a8e35fc630e9158942463586c22ebfd8e893e21a199e0a7 bytes=3908 -->
## FILE: tests/legacy/test_triggers.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/legacy/test_triggers.py`
- sha256: `0e8548ba7c6f06892a8e35fc630e9158942463586c22ebfd8e893e21a199e0a7`
- bytes: 3908

````python
"""Tests for validating trigger functionality."""

import random

import pytest

from nidaqmx import DaqError
from nidaqmx.constants import AcquisitionType, Edge, TriggerType
from tests.helpers import generate_random_seed
from tests.legacy.test_read_write import TestDAQmxIOBase


class TestTriggers(TestDAQmxIOBase):
    """Contains a collection of pytest tests.

    These validate the triggers functionality in the NI-DAQmx Python API.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_arm_start_trigger(self, task, sim_6363_device, seed):
        """Test to validate start trigger functionality."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        counter = random.choice(self._get_device_counters(sim_6363_device))

        task.co_channels.add_co_pulse_chan_freq(counter)
        task.triggers.arm_start_trigger.trig_type = TriggerType.DIGITAL_EDGE
        assert task.triggers.arm_start_trigger.trig_type == TriggerType.DIGITAL_EDGE

        task.triggers.arm_start_trigger.trig_type = TriggerType.NONE
        assert task.triggers.arm_start_trigger.trig_type == TriggerType.NONE

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_handshake_trigger(self, task, sim_6363_device, seed):
        """Test to validate trigger handshake."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        counter = random.choice(self._get_device_counters(sim_6363_device))

        task.co_channels.add_co_pulse_chan_freq(counter)

        with pytest.raises(DaqError) as e:
            task.triggers.handshake_trigger.trig_type = TriggerType.INTERLOCKED
        assert e.value.error_code == -200452

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_pause_trigger(self, task, sim_6363_device, seed):
        """Test to validate pause trigger."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        counter = random.choice(self._get_device_counters(sim_6363_device))

        task.co_channels.add_co_pulse_chan_freq(counter)
        task.timing.cfg_implicit_timing(sample_mode=AcquisitionType.CONTINUOUS)

        task.triggers.pause_trigger.trig_type = TriggerType.DIGITAL_LEVEL
        assert task.triggers.pause_trigger.trig_type == TriggerType.DIGITAL_LEVEL

        task.triggers.pause_trigger.trig_type = TriggerType.NONE
        assert task.triggers.pause_trigger.trig_type == TriggerType.NONE

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_reference_trigger(self, task, sim_6363_device, seed):
        """Test to validate reference trigger."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        counter = random.choice(self._get_device_counters(sim_6363_device))

        task.co_channels.add_co_pulse_chan_freq(counter)

        with pytest.raises(DaqError) as e:
            task.triggers.reference_trigger.trig_type = TriggerType.NONE
        assert e.value.error_code == -200452

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_start_trigger(self, task, sim_6363_device, seed):
        """Test to validate start trigger functionality."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        counter = random.choice(self._get_device_counters(sim_6363_device))
        pfi_line = random.choice(self._get_device_pfi_lines(sim_6363_device))

        task.co_channels.add_co_pulse_chan_freq(counter)
        task.triggers.start_trigger.cfg_dig_edge_start_trig(pfi_line, trigger_edge=Edge.FALLING)

        assert task.triggers.start_trigger.trig_type == TriggerType.DIGITAL_EDGE
        assert task.triggers.start_trigger.dig_edge_edge == Edge.FALLING
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/legacy/test_utils.py sha256=04dd82244e4685703c948c5ff61024c03c1d1b190daa6c5dfe3a169a30d070de bytes=2028 -->
## FILE: tests/legacy/test_utils.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/legacy/test_utils.py`
- sha256: `04dd82244e4685703c948c5ff61024c03c1d1b190daa6c5dfe3a169a30d070de`
- bytes: 2028

````python
"""Tests for validating utilities functionality."""

from __future__ import annotations

from nidaqmx.utils import flatten_channel_string, unflatten_channel_string


class TestUtils:
    """Contains a collection of pytest tests.

    These validate the utilities functionality in the NI-DAQmx Python API.
    """

    def test_basic_flatten_flatten_and_unflatten(self):
        """Test to validate flatten and unflatten channel string function."""
        unflattened_channels = ["Dev1/ai0", "Dev1/ai1", "Dev1/ai2", "Dev1/ai4", "Dev2/ai0"]
        flattened_channels = "Dev1/ai0:2,Dev1/ai4,Dev2/ai0"
        assert flatten_channel_string(unflattened_channels) == flattened_channels
        assert unflatten_channel_string(flattened_channels) == unflattened_channels

    def test_backwards_flatten_flatten_and_unflatten(self):
        """Test to validate unflatten and flatten channel string function."""
        unflattened_channels = ["Dev1/ai2", "Dev1/ai1", "Dev1/ai0", "Dev1/ai4", "Dev2/ai0"]
        flattened_channels = "Dev1/ai2:0,Dev1/ai4,Dev2/ai0"
        assert flatten_channel_string(unflattened_channels) == flattened_channels
        assert unflatten_channel_string(flattened_channels) == unflattened_channels

    def test_empty_flatten_flatten_and_unflatten(self):
        """Test to validate flatten and unflatten empty channel."""
        unflattened_channels: list[str] = []
        flattened_channels = ""
        assert flatten_channel_string(unflattened_channels) == flattened_channels
        assert unflatten_channel_string(flattened_channels) == unflattened_channels

    def test_leading_zeros_flatten_and_unflatten(self):
        """Test to validate leading zeros in flatten and unflatten string function."""
        unflattened_channels = ["EV01", "EV02"]
        flattened_channels = "EV01:02"
        assert flatten_channel_string(unflattened_channels) == flattened_channels
        assert unflatten_channel_string(flattened_channels) == unflattened_channels
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/legacy/test_watchdog.py sha256=6bb8b972955516fe6f56db69c1ccd57da249a3a9813532966f66dc00706e9576 bytes=2480 -->
## FILE: tests/legacy/test_watchdog.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/legacy/test_watchdog.py`
- sha256: `6bb8b972955516fe6f56db69c1ccd57da249a3a9813532966f66dc00706e9576`
- bytes: 2480

````python
"""Tests for validating watchdog functionality."""

import random
import time

import pytest

from nidaqmx.constants import Level
from nidaqmx.system.watchdog import DOExpirationState
from tests.helpers import generate_random_seed


class TestWatchdog:
    """Contains a collection of pytest tests.

    These validate the watchdog functionality in the NI-DAQmx Python API.
    """

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_watchdog_task(self, real_x_series_device, seed, generate_watchdog_task):
        """Test to validate watchdog task."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        do_line = random.choice(real_x_series_device.do_lines)

        task = generate_watchdog_task(device_name=real_x_series_device.name)

        expir_states = [
            DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
        ]

        task.cfg_watchdog_do_expir_states(expir_states)
        task.start()

        # First, assert that watchdog expires after timeout.
        assert not task.expired
        time.sleep(1)
        assert task.expired

        task.clear_expiration()
        assert not task.expired
        task.stop()

        # Continually reset the watchdog timer using an interval less
        # than the timeout and assert that it never expires.
        task.start()
        for _ in range(5):
            task.reset_timer()
            time.sleep(0.2)
            assert not task.expired

        task.stop()

    @pytest.mark.parametrize("seed", [generate_random_seed()])
    def test_watchdog_expir_state(self, real_x_series_device, seed, generate_watchdog_task):
        """Test to validate watchdog expiration state."""
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        do_line = random.choice(real_x_series_device.do_lines)

        task = generate_watchdog_task(device_name=real_x_series_device.name, timeout=0.1)

        expir_states = [
            DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
        ]

        task.cfg_watchdog_do_expir_states(expir_states)

        expir_state_obj = task.expiration_states[do_line.name]
        assert expir_state_obj.do_state == Level.TRISTATE

        expir_state_obj.do_state = Level.LOW
        assert expir_state_obj.do_state == Level.LOW
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/legacy/test_write_exceptions.py sha256=3529eb8a3c253cbbccba8d57bd3b37ec2eb568ea71a5f0e94bf2420e10feaf3a bytes=4797 -->
## FILE: tests/legacy/test_write_exceptions.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/legacy/test_write_exceptions.py`
- sha256: `3529eb8a3c253cbbccba8d57bd3b37ec2eb568ea71a5f0e94bf2420e10feaf3a`
- bytes: 4797

````python
"""Tests for validating write error behavior."""

import numpy
import pytest

import nidaqmx
import nidaqmx.stream_writers
from nidaqmx.constants import AcquisitionType, BusType, RegenerationMode
from nidaqmx.error_codes import DAQmxErrors


class TestWriteExceptions:
    """Contains a collection of pytest tests.

    These validate the Write error behavior in the NI-DAQmx Python API.
    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    """

    def test_overwrite(self, task, real_x_series_device):
        """Test to validate overwrite functionality."""
        # USB streaming is very tricky.
        if not (
            real_x_series_device.bus_type == BusType.PCIE
            or real_x_series_device.bus_type == BusType.PXIE
        ):
            pytest.skip("Requires a plugin device.")

        number_of_samples = 100
        sample_rate = 1000
        fifo_size = 8191
        host_buffer_size = 1000

        samp_clk_terminal = f"/{real_x_series_device.name}/Ctr0InternalOutput"

        task.ao_channels.add_ao_voltage_chan(
            real_x_series_device.ao_physical_chans[0].name, max_val=10, min_val=-10
        )
        task.timing.cfg_samp_clk_timing(
            sample_rate,
            source=samp_clk_terminal,
            sample_mode=AcquisitionType.CONTINUOUS,
            samps_per_chan=number_of_samples,
        )

        # Don't allow regeneration - this enables explicit hardware flow control.
        task.out_stream.regen_mode = RegenerationMode.DONT_ALLOW_REGENERATION

        # This is the only entrypoint that correctly sets number_of_samples_written in error
        # conditions prior to DAQmx 21.8.
        writer = nidaqmx.stream_writers.AnalogUnscaledWriter(task.out_stream, auto_start=False)

        # Fill up the host buffer first.
        initial_write_data = numpy.zeros((1, host_buffer_size), dtype=numpy.int16)
        writer.write_int16(initial_write_data)

        # Start the write task. All data from the host buffer should be in the FIFO.
        task.start()

        # Now write more data than can fit in the FIFO + host buffer.
        large_write_data = numpy.zeros((1, fifo_size * 2), dtype=numpy.int16)
        with pytest.raises(nidaqmx.DaqWriteError) as timeout_exception:
            writer.write_int16(large_write_data, timeout=2.0)

        assert timeout_exception.value.error_code == DAQmxErrors.SAMPLES_CAN_NOT_YET_BE_WRITTEN
        # Some of the data should have been written successfully. This test doesn't
        # need to get into the nitty gritty device details on how much.
        assert timeout_exception.value.samps_per_chan_written > 0

    def test_overwrite_during_prime(self, task, real_x_series_device):
        """Test to validate overwrite functionality during prime."""
        # USB streaming is very tricky.
        if not (
            real_x_series_device.bus_type == BusType.PCIE
            or real_x_series_device.bus_type == BusType.PXIE
        ):
            pytest.skip("Requires a plugin device.")

        number_of_samples = 100
        sample_rate = 1000
        fifo_size = 8191
        host_buffer_size = 1000
        total_buffer_size = fifo_size + host_buffer_size

        samp_clk_terminal = f"/{real_x_series_device.name}/Ctr0InternalOutput"

        task.ao_channels.add_ao_voltage_chan(
            real_x_series_device.ao_physical_chans[0].name, max_val=10, min_val=-10
        )
        task.timing.cfg_samp_clk_timing(
            sample_rate,
            source=samp_clk_terminal,
            sample_mode=AcquisitionType.CONTINUOUS,
            samps_per_chan=number_of_samples,
        )

        # Don't allow regeneration - this enables explicit hardware flow control.
        task.out_stream.regen_mode = RegenerationMode.DONT_ALLOW_REGENERATION
        # Make the host buffer small.
        task.out_stream.output_buf_size = number_of_samples

        # This is the only entrypoint that correctly sets number_of_samples_written in error
        # conditions prior to DAQmx 21.8.
        writer = nidaqmx.stream_writers.AnalogUnscaledWriter(task.out_stream, auto_start=False)

        # This is more data than can be primed, so this should fail.
        initial_write_data = numpy.zeros((1, total_buffer_size * 2), dtype=numpy.int16)
        with pytest.raises(nidaqmx.DaqWriteError) as timeout_exception:
            writer.write_int16(initial_write_data)

        assert timeout_exception.value.error_code == DAQmxErrors.NO_MORE_SPACE
        # The driver detects that the write will fail immediately, so no data was written.
        assert timeout_exception.value.samps_per_chan_written == 0
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/max_config/examplesMaxConfig.ini sha256=d904445ed4bdb9229c7d402aa1a8a1ac501a2e68d8a211cb058f1bfe1ee04911 bytes=1194 -->
## FILE: tests/max_config/examplesMaxConfig.ini

- repository: `ni/nidaqmx-python`
- source_path: `tests/max_config/examplesMaxConfig.ini`
- sha256: `d904445ed4bdb9229c7d402aa1a8a1ac501a2e68d8a211cb058f1bfe1ee04911`
- bytes: 1194

````ini
[DAQmx]
MajorVersion = 23
MinorVersion = 0

[DAQmxCDAQChassis cDAQ1]
ProductType = cDAQ-9178
DevSerialNum = 0x0
DevIsSimulated = 1

[DAQmxCDAQModule cDAQ1Mod1]
ProductType = NI 9215
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = cDAQ1
CompactDAQ.SlotNum = 1

[DAQmxCDAQModule cDAQ1Mod2]
ProductType = NI 9214
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = cDAQ1
CompactDAQ.SlotNum = 2

[DAQmxDevice Dev1]
ProductType = PCIe-6363
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x7435C4C4
BusType = PCIe
PCI.BusNum = 0x0
PCI.DevNum = 0x0

[DAQmxDevice PXI1Slot3]
ProductType = PXIe-6368
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x7439C4C4
BusType = PXIe
PXI.ChassisNum = 1
PXI.SlotNum = 3

[DAQmxDevice PXI1Slot7]
ProductType = PXIe-6368
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x7439C4C4
BusType = PXIe
PXI.ChassisNum = 1
PXI.SlotNum = 7

[DAQmxCDAQChassis TS1]
ProductType = TS-15000
DevSerialNum = 0x0
DevIsSimulated = 1

[DAQmxCDAQModule TS1Mod1]
ProductType = TS-15200
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = TS1
CompactDAQ.SlotNum = 1
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/max_config/linux/nidaqmxMaxConfig.ini sha256=dfb644aeea854b2aa899b19d3b0e57b2f5313d1facdce87fcb44ec4e997b7003 bytes=6093 -->
## FILE: tests/max_config/linux/nidaqmxMaxConfig.ini

- repository: `ni/nidaqmx-python`
- source_path: `tests/max_config/linux/nidaqmxMaxConfig.ini`
- sha256: `dfb644aeea854b2aa899b19d3b0e57b2f5313d1facdce87fcb44ec4e997b7003`
- bytes: 6093

````ini
[DAQmx]
MajorVersion = 21
MinorVersion = 8

[DAQmxChannel AOTesterTask/VoltageOut_0]
AO.OutputType = Voltage
AO.Voltage.Units = Volts
AO.Max = 16
AO.Min = -16
ChanType = Analog Output
AO.TermCfg = Differential
PhysicalChanName = aoTester/ao0

[DAQmxChannel AOTesterTask/VoltageOut_1]
AO.OutputType = Voltage
AO.Voltage.Units = Volts
AO.Max = 16
AO.Min = -16
ChanType = Analog Output
AO.TermCfg = Differential
PhysicalChanName = aoTester/ao1

[DAQmxChannel AOTesterTask/VoltageOut_2]
AO.OutputType = Voltage
AO.Voltage.Units = Volts
AO.Max = 16
AO.Min = -16
ChanType = Analog Output
AO.TermCfg = Differential
PhysicalChanName = aoTester/ao2

[DAQmxTask AOTesterTask]
Channels = AOTesterTask/VoltageOut_0, AOTesterTask/VoltageOut_1, AOTesterTask/VoltageOut_2
SampQuant.SampMode = Finite Samples
SampClk.ActiveEdge = Rising
SampQuant.SampPerChan = 100
SampClk.Rate = 1000
SampTimingType = Sample Clock
RegenMode = Allow Regeneration
SampClk.Src =

[DAQmxChannel VoltageTesterChannel]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = Differential
AI.Max = 10
AI.Min = -10
ChanType = Analog Input
PhysicalChanName = tsVoltageTester1/ai0
Descr = 
Author = "Test Author"
AllowInteractiveEditing = True

[DAQmxChannel VoltageTesterChannel2]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = Differential
AI.Max = 5
AI.Min = -5
ChanType = Analog Input
PhysicalChanName = tsVoltageTester1/ai1
Descr = "Another channel"
Author = "Another Test Author"
AllowInteractiveEditing = True

[DAQmxChannel VoltageTesterTask/Voltage_0]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = Differential
AI.Max = 10
AI.Min = -10
ChanType = Analog Input
PhysicalChanName = tsVoltageTester1/ai0

[DAQmxTask VoltageTesterTask]
Channels = VoltageTesterTask/Voltage_0
SampQuant.SampMode = Finite Samples
SampClk.ActiveEdge = Rising
SampQuant.SampPerChan = 100
SampClk.Rate = 1000
SampTimingType = Sample Clock
SampClk.Src = 
Author = Test Author
AllowInteractiveEditing = True

[DAQmxScale double_gain_scale]
Lin.Slope = 2
Lin.YIntercept = 0
PreScaledUnits = Volts
ScaledUnits = 
ScaleType = Linear
Author = Test Author
AllowInteractiveEditing = True
Descr = Twice the gain

[DAQmxScale no_scaling_scale]
Lin.Slope = 1
Lin.YIntercept = 0
PreScaledUnits = Volts
ScaledUnits = 
ScaleType = Linear

[DAQmxScale polynomial_scale]
Poly.ForwardCoeff = 0, 1
Poly.ReverseCoeff = 0, 1
PreScaledUnits = Volts
ScaledUnits = 
ScaleType = Polynomial

[DAQmxScale degrees_scale]
Lin.Slope = 2
Lin.YIntercept = 0
PreScaledUnits = Degrees
ScaledUnits = potatoes
ScaleType = Linear

[DAQmxDevice aoTester]
ProductType = PXIe-4322
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x76ABC4C4
BusType = PXIe
PXI.ChassisNum = 1
PXI.SlotNum = 3

[DAQmxDevice bridgeTester]
ProductType = PXIe-4331
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x74A9C4C4
BusType = PXIe
PXI.ChassisNum = 1
PXI.SlotNum = 2

[DAQmxAccessory RM-24999_A/bridgeTester/0]

[DAQmxDevice chargeTester]
ProductType = PXIe-4480
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x7844C4C4
BusType = PXIe
PXI.ChassisNum = 1
PXI.SlotNum = 5

[DAQmxDevice dsaTester]
ProductType = PXIe-4466
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x7A8DC4C4
BusType = PXIe
PXI.ChassisNum = 1
PXI.SlotNum = 6

[DAQmxDevice nidaqmxMultithreadingTester1]
ProductType = PCIe-6363
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x7435C4C4
BusType = PCIe
PCI.BusNum = 0x0
PCI.DevNum = 0x0

[DAQmxDevice nidaqmxMultithreadingTester2]
ProductType = PCIe-6363
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x7435C4C4
BusType = PCIe
PCI.BusNum = 0x0
PCI.DevNum = 0x0

[DAQmxDevice nidaqmxMultithreadingTester3]
ProductType = PCIe-6363
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x7435C4C4
BusType = PCIe
PCI.BusNum = 0x0
PCI.DevNum = 0x0

[DAQmxDevice nidaqmxMultithreadingTester4]
ProductType = PCIe-6363
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x7435C4C4
BusType = PCIe
PCI.BusNum = 0x0
PCI.DevNum = 0x0

[DAQmxDevice positionTester]
ProductType = PXIe-4340
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x7829C4C4
BusType = PXIe
PXI.ChassisNum = 4294967295
PXI.SlotNum = 4294967295

[DAQmxDevice tempTester]
ProductType = PXIe-4353
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x74B2C4C4
BusType = PXIe
PXI.ChassisNum = 1
PXI.SlotNum = 7

[DAQmxCDAQChassis tsChassisTester]
ProductType = TS-15000
DevSerialNum = 0x0
DevIsSimulated = 1

[DAQmxCDAQModule tsPowerTester1]
ProductType = TS-15200
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = tsChassisTester
CompactDAQ.SlotNum = 1

[DAQmxCDAQModule tsPowerTester2]
ProductType = TS-15200
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = tsChassisTester
CompactDAQ.SlotNum = 2

[DAQmxCDAQModule tsVoltageTester1]
ProductType = TS-15100
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = tsChassisTester
CompactDAQ.SlotNum = 3

[DAQmxCDAQChassis cdaqChassisTester]
ProductType = cDAQ-9189
DevSerialNum = 0x0
DevIsSimulated = 1
BusType = TCP/IP
TCPIP.Hostname = 
TCPIP.EthernetIP = 0.0.0.0
TCPIP.EthernetMAC = 00:00:00:00:00:00
TCPIP.EthernetMDNSServiceInstance = 
TCPIP.DevIsReserved = 0

[DAQmxCDAQModule cdaqTesterMod1]
ProductType = NI 9361
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = cdaqChassisTester
CompactDAQ.SlotNum = 1

[DAQmxCDAQModule cdaqTesterMod2]
ProductType = NI 9215
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = cdaqChassisTester
CompactDAQ.SlotNum = 2

[DAQmxCDAQModule cdaqTesterMod4]
ProductType = NI 9401
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = cdaqChassisTester
CompactDAQ.SlotNum = 4

[DAQmxCDAQModule cdaqTesterMod5]
ProductType = NI 9263
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = cdaqChassisTester
CompactDAQ.SlotNum = 5
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/max_config/nidaqmxMaxConfig.ini sha256=108faecc6b94c430857bbff2473b37b4bc427b0116ce7b8728f4e5954ff688f6 bytes=6844 -->
## FILE: tests/max_config/nidaqmxMaxConfig.ini

- repository: `ni/nidaqmx-python`
- source_path: `tests/max_config/nidaqmxMaxConfig.ini`
- sha256: `108faecc6b94c430857bbff2473b37b4bc427b0116ce7b8728f4e5954ff688f6`
- bytes: 6844

````ini
[DAQmx]
MajorVersion = 21
MinorVersion = 8

[DAQmxChannel AOTesterTask/VoltageOut_0]
AO.OutputType = Voltage
AO.Voltage.Units = Volts
AO.Max = 16
AO.Min = -16
ChanType = Analog Output
AO.TermCfg = Differential
PhysicalChanName = aoTester/ao0

[DAQmxChannel AOTesterTask/VoltageOut_1]
AO.OutputType = Voltage
AO.Voltage.Units = Volts
AO.Max = 16
AO.Min = -16
ChanType = Analog Output
AO.TermCfg = Differential
PhysicalChanName = aoTester/ao1

[DAQmxChannel AOTesterTask/VoltageOut_2]
AO.OutputType = Voltage
AO.Voltage.Units = Volts
AO.Max = 16
AO.Min = -16
ChanType = Analog Output
AO.TermCfg = Differential
PhysicalChanName = aoTester/ao2

[DAQmxTask AOTesterTask]
Channels = AOTesterTask/VoltageOut_0, AOTesterTask/VoltageOut_1, AOTesterTask/VoltageOut_2
SampQuant.SampMode = Finite Samples
SampClk.ActiveEdge = Rising
SampQuant.SampPerChan = 100
SampClk.Rate = 1000
SampTimingType = Sample Clock
RegenMode = Allow Regeneration
SampClk.Src =

[DAQmxChannel VoltageTesterChannel]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = Differential
AI.Max = 10
AI.Min = -10
ChanType = Analog Input
PhysicalChanName = tsVoltageTester1/ai0
Descr =
Author = "Test Author"
AllowInteractiveEditing = True

[DAQmxChannel VoltageTesterChannel2]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = Differential
AI.Max = 5
AI.Min = -5
ChanType = Analog Input
PhysicalChanName = tsVoltageTester1/ai1
Descr = "Another channel"
Author = "Another Test Author"
AllowInteractiveEditing = True

[DAQmxChannel VoltageTesterTask/Voltage_0]
AI.MeasType = Voltage
AI.Voltage.Units = Volts
AI.TermCfg = Differential
AI.Max = 10
AI.Min = -10
ChanType = Analog Input
PhysicalChanName = tsVoltageTester1/ai0

[DAQmxTask VoltageTesterTask]
Channels = VoltageTesterTask/Voltage_0
SampQuant.SampMode = Finite Samples
SampClk.ActiveEdge = Rising
SampQuant.SampPerChan = 100
SampClk.Rate = 1000
SampTimingType = Sample Clock
SampClk.Src =
Author = Test Author
AllowInteractiveEditing = True

[DAQmxScale double_gain_scale]
Lin.Slope = 2
Lin.YIntercept = 0
PreScaledUnits = Volts
ScaledUnits =
ScaleType = Linear
Author = Test Author
AllowInteractiveEditing = True
Descr = Twice the gain

[DAQmxScale no_scaling_scale]
Lin.Slope = 1
Lin.YIntercept = 0
PreScaledUnits = Volts
ScaledUnits =
ScaleType = Linear

[DAQmxScale polynomial_scale]
Poly.ForwardCoeff = 0, 1
Poly.ReverseCoeff = 0, 1
PreScaledUnits = Volts
ScaledUnits =
ScaleType = Polynomial

[DAQmxScale degrees_scale]
Lin.Slope = 2
Lin.YIntercept = 0
PreScaledUnits = Degrees
ScaledUnits = potatoes
ScaleType = Linear

[DAQmxDevice aoTester]
ProductType = PXIe-4322
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x76ABC4C4
BusType = PXIe
PXI.ChassisNum = 1
PXI.SlotNum = 3

[DAQmxDevice bridgeTester]
ProductType = PXIe-4331
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x74A9C4C4
BusType = PXIe
PXI.ChassisNum = 1
PXI.SlotNum = 2

[DAQmxAccessory RM-24999_A/bridgeTester/0]

[DAQmxDevice chargeTester]
ProductType = PXIe-4480
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x7844C4C4
BusType = PXIe
PXI.ChassisNum = 1
PXI.SlotNum = 5

[DAQmxDevice dmmTester]
ProductType = NI myDAQ
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x755B
BusType = USB

[DAQmxDevice dsaTester]
ProductType = PXIe-4466
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x7A8DC4C4
BusType = PXIe
PXI.ChassisNum = 1
PXI.SlotNum = 6

[DAQmxDevice nidaqmxMultithreadingTester1]
ProductType = PCIe-6363
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x7435C4C4
BusType = PCIe
PCI.BusNum = 0x0
PCI.DevNum = 0x0

[DAQmxDevice nidaqmxMultithreadingTester2]
ProductType = PCIe-6363
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x7435C4C4
BusType = PCIe
PCI.BusNum = 0x0
PCI.DevNum = 0x0

[DAQmxDevice nidaqmxMultithreadingTester3]
ProductType = PCIe-6363
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x7435C4C4
BusType = PCIe
PCI.BusNum = 0x0
PCI.DevNum = 0x0

[DAQmxDevice nidaqmxMultithreadingTester4]
ProductType = PCIe-6363
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x7435C4C4
BusType = PCIe
PCI.BusNum = 0x0
PCI.DevNum = 0x0

[DAQmxDevice hsdioTester]
ProductType = PCIe-6535
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x719F
BusType = PCIe
PCI.BusNum = 0x0
PCI.DevNum = 0x0

[DAQmxDevice positionTester]
ProductType = PXIe-4340
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x7829C4C4
BusType = PXIe
PXI.ChassisNum = 4294967295
PXI.SlotNum = 4294967295

[DAQmxDevice tempTester]
ProductType = PXIe-4353
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x74B2C4C4
BusType = PXIe
PXI.ChassisNum = 1
PXI.SlotNum = 7

[DAQmxCDAQChassis tsChassisTester]
ProductType = TS-15000
DevSerialNum = 0x0
DevIsSimulated = 1

[DAQmxCDAQModule tsPowerTester1]
ProductType = TS-15200
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = tsChassisTester
CompactDAQ.SlotNum = 1

[DAQmxCDAQModule tsPowerTester2]
ProductType = TS-15200
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = tsChassisTester
CompactDAQ.SlotNum = 2

[DAQmxCDAQModule tsVoltageTester1]
ProductType = TS-15100
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = tsChassisTester
CompactDAQ.SlotNum = 3

[DAQmxCDAQChassis cdaqChassisTester]
ProductType = cDAQ-9189
DevSerialNum = 0x0
DevIsSimulated = 1
BusType = TCP/IP
TCPIP.Hostname =
TCPIP.EthernetIP = 0.0.0.0
TCPIP.EthernetMAC = 00:00:00:00:00:00
TCPIP.EthernetMDNSServiceInstance =
TCPIP.DevIsReserved = 0

[DAQmxCDAQModule cdaqTesterMod1]
ProductType = NI 9361
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = cdaqChassisTester
CompactDAQ.SlotNum = 1

[DAQmxCDAQModule cdaqTesterMod2]
ProductType = NI 9215
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = cdaqChassisTester
CompactDAQ.SlotNum = 2

[DAQmxCDAQModule cdaqTesterMod3]
ProductType = NI 9775
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = cdaqChassisTester
CompactDAQ.SlotNum = 3

[DAQmxCDAQModule cdaqTesterMod4]
ProductType = NI 9401
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = cdaqChassisTester
CompactDAQ.SlotNum = 4

[DAQmxCDAQModule cdaqTesterMod5]
ProductType = NI 9263
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = cdaqChassisTester
CompactDAQ.SlotNum = 5

[DAQmxCDAQModule cdaqTesterMod6]
ProductType = NI 9205
DevSerialNum = 0x0
DevIsSimulated = 1
CompactDAQ.ChassisDevName = cdaqChassisTester
CompactDAQ.SlotNum = 6

[DAQmxDevice mioDAQ]
ProductType = USB-6423
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x7B40
BusType = USB
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/max_config/nidaqmxMaxConfig26Q1.ini sha256=60e78930efbe22d7f5043287ad5d18f340b8179feb6332aa23a9102306812f1a bytes=338 -->
## FILE: tests/max_config/nidaqmxMaxConfig26Q1.ini

- repository: `ni/nidaqmx-python`
- source_path: `tests/max_config/nidaqmxMaxConfig26Q1.ini`
- sha256: `60e78930efbe22d7f5043287ad5d18f340b8179feb6332aa23a9102306812f1a`
- bytes: 338

````ini
[DAQmx]
MajorVersion = 26
MinorVersion = 0

[DAQmxScale power_scale]
Lin.Slope = 1
Lin.YIntercept = 0
PreScaledUnits = Watts
ScaledUnits =
ScaleType = Linear

[DAQmxDevice pxie4311]
ProductType = PXIe-4311
DevSerialNum = 0x0
DevIsSimulated = 1
ProductNum = 0x7B1AC4C4
BusType = PXIe
PXI.ChassisNum = 1
PXI.SlotNum = 4
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/unit/__init__.py sha256=4c20d9d00d1de3b0286ce93d6f2a264991aa036d57adec5aa981b0543f5ccb07 bytes=43 -->
## FILE: tests/unit/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/unit/__init__.py`
- sha256: `4c20d9d00d1de3b0286ce93d6f2a264991aa036d57adec5aa981b0543f5ccb07`
- bytes: 43

````python
"""Unit tests for the nidaqmx package."""
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/unit/_grpc_utils.py sha256=1a111784374465bac935c1b8fb234cf4ce0af1190a1844ae2b0c4b28f350a04a bytes=567 -->
## FILE: tests/unit/_grpc_utils.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/unit/_grpc_utils.py`
- sha256: `1a111784374465bac935c1b8fb234cf4ce0af1190a1844ae2b0c4b28f350a04a`
- bytes: 567

````python
"""gRPC helper functions."""

import pytest
from pytest_mock import MockerFixture

import nidaqmx

try:
    import grpc
except ImportError:
    grpc = None  # type: ignore


def create_grpc_options(mocker: MockerFixture, session_name="") -> nidaqmx.GrpcSessionOptions:
    """Create a GrpcSessionOptions object."""
    if grpc is None:
        pytest.skip("The grpc module is not available.")
    grpc_channel = mocker.create_autospec(grpc.Channel)
    grpc_options = nidaqmx.GrpcSessionOptions(grpc_channel, session_name)
    return grpc_options
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/unit/_task_utils.py sha256=01a7aab3dc733ac6ad3867864fced62744408a061e465bd1f044f1ead584badc bytes=1716 -->
## FILE: tests/unit/_task_utils.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/unit/_task_utils.py`
- sha256: `01a7aab3dc733ac6ad3867864fced62744408a061e465bd1f044f1ead584badc`
- bytes: 1716

````python
"""Task helper functions."""

from __future__ import annotations

from collections.abc import Iterable
from unittest.mock import Mock

from pytest_mock import MockerFixture

from nidaqmx import Task
from nidaqmx._base_interpreter import BaseEventHandler
from nidaqmx.task import _TaskEventType


def expect_create_task(
    interpreter: Mock,
    task_handle="SomeTaskHandle",
    new_session_initialized=True,
):
    """Expect a call to interpreter.create_task."""
    interpreter.create_task.return_value = (task_handle, new_session_initialized)


def expect_load_task(
    interpreter: Mock,
    task_handle="SomeTaskHandle",
    new_session_initialized=True,
):
    """Expect a call to interpreter.load_task."""
    interpreter.load_task.return_value = (task_handle, new_session_initialized)


def expect_get_task_name(interpreter: Mock, name: str):
    """Expect a call to get the task name."""
    # Assume there are no other calls to get_task_attribute_string.
    interpreter.get_task_attribute_string.return_value = name


def register_event_handler(mocker: MockerFixture, task: Task, event_type: _TaskEventType) -> Mock:
    """Register a mock event handler."""
    event_handler = mocker.create_autospec(BaseEventHandler)
    task._event_handlers[event_type] = event_handler
    return event_handler


def register_event_handlers(
    mocker: MockerFixture, task: Task, event_types: Iterable[_TaskEventType]
) -> dict[_TaskEventType, Mock]:
    """Register mock event handlers and return a dictionary mapping event name -> handler."""
    return {
        event_type: register_event_handler(mocker, task, event_type) for event_type in event_types
    }
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/unit/_time_utils.py sha256=2bfa109c69e727c003aa5f62f5386fc0908906f3eca415c9c858c51e57fa9bf7 bytes=922 -->
## FILE: tests/unit/_time_utils.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/unit/_time_utils.py`
- sha256: `2bfa109c69e727c003aa5f62f5386fc0908906f3eca415c9c858c51e57fa9bf7`
- bytes: 922

````python
from datetime import datetime as std_datetime
from datetime import timezone

from hightime import datetime as ht_datetime

# Jan 1, 2002 = 32 years + 8 leapdays = 11688 days = 1009843200 seconds
JAN_01_2002_TIMESTAMP_1970_EPOCH = 0x3C30FC00
JAN_01_1850_TIMESTAMP_1970_EPOCH = -0xE1B65F80
# Jan 1, 2002 = 98 years + 25 leapdays = 35795 days = 3092688000 seconds
JAN_01_2002_TIMESTAMP_1904_EPOCH = 0xB856AC80
JAN_01_1904_TIMESTAMP_1904_EPOCH = 0
JAN_01_1850_TIMESTAMP_1904_EPOCH = -0x6590AF00

JAN_01_2002_DATETIME = std_datetime(2002, 1, 1, tzinfo=timezone.utc)
JAN_01_2002_HIGHTIME = ht_datetime(2002, 1, 1, tzinfo=timezone.utc)
JAN_01_1904_DATETIME = std_datetime(1904, 1, 1, tzinfo=timezone.utc)
JAN_01_1904_HIGHTIME = ht_datetime(1904, 1, 1, tzinfo=timezone.utc)
JAN_01_1850_DATETIME = std_datetime(1850, 1, 1, tzinfo=timezone.utc)
JAN_01_1850_HIGHTIME = ht_datetime(1850, 1, 1, tzinfo=timezone.utc)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/unit/conftest.py sha256=ac5e01f5ebe9bc7cd09ac723846f09c6cb3f8d59dd45364bbab5b323ea275e90 bytes=1116 -->
## FILE: tests/unit/conftest.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/unit/conftest.py`
- sha256: `ac5e01f5ebe9bc7cd09ac723846f09c6cb3f8d59dd45364bbab5b323ea275e90`
- bytes: 1116

````python
"""Fixtures used in the DAQmx unit tests."""

from __future__ import annotations

from collections.abc import Generator
from unittest.mock import Mock

import pytest
from pytest_mock import MockerFixture

from nidaqmx import Task
from nidaqmx._base_interpreter import BaseInterpreter
from tests.unit._task_utils import expect_create_task, expect_get_task_name


@pytest.fixture
def interpreter(mocker: MockerFixture) -> Mock:
    """Create a mock interpreter."""
    mock_interpreter = mocker.create_autospec(BaseInterpreter)
    mock_select_interpreter = mocker.patch("nidaqmx.utils._select_interpreter", autospec=True)
    mock_select_interpreter.return_value = mock_interpreter
    return mock_interpreter


@pytest.fixture
def task(interpreter: Mock) -> Generator[Task]:
    """Create a DAQmx task.

    This fixture owns the task. Do not use it for test cases that destroy the task, or else you
    may get double-close warnings.
    """
    expect_create_task(interpreter)
    expect_get_task_name(interpreter, "MyTask")

    with Task("MyTask") as task:
        yield task
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/unit/system/__init__.py sha256=f21a136d9c8eccf5bdfafcbdc73ea5e706659049d85510d882c4ba9551a32801 bytes=40 -->
## FILE: tests/unit/system/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/unit/system/__init__.py`
- sha256: `f21a136d9c8eccf5bdfafcbdc73ea5e706659049d85510d882c4ba9551a32801`
- bytes: 40

````python
"""Unit tests for nidaqmx.system.*."""
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/unit/system/storage/__init__.py sha256=eaa195b0940fb2223cf37a4578b5eb324daf0835547d00fdcf866650f7e7a104 bytes=48 -->
## FILE: tests/unit/system/storage/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/unit/system/storage/__init__.py`
- sha256: `eaa195b0940fb2223cf37a4578b5eb324daf0835547d00fdcf866650f7e7a104`
- bytes: 48

````python
"""Unit tests for nidaqmx.system.storage.*."""
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/unit/system/storage/test_persisted_task.py sha256=e6e4dcec90d500b9559f0973a0c5455069c438468cdf4c63d052c5fe0f3777fd bytes=1107 -->
## FILE: tests/unit/system/storage/test_persisted_task.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/unit/system/storage/test_persisted_task.py`
- sha256: `e6e4dcec90d500b9559f0973a0c5455069c438468cdf4c63d052c5fe0f3777fd`
- bytes: 1107

````python
from unittest.mock import Mock

import pytest

from nidaqmx.system.storage import PersistedTask
from tests.unit._task_utils import expect_get_task_name, expect_load_task


def test___persisted_task___load___specified_name_saved(interpreter: Mock):
    expect_load_task(interpreter)
    expect_get_task_name(interpreter, "SpecifiedName")
    persisted_task = PersistedTask("SpecifiedName")

    task = persisted_task.load()

    with task:
        assert task._saved_name == "SpecifiedName"


@pytest.mark.parametrize("new_session_initialized", [False, True])
def test___persisted_task___load___load_task_called(
    interpreter: Mock, new_session_initialized: bool
):
    expect_load_task(interpreter, "MyTaskHandle", new_session_initialized)
    expect_get_task_name(interpreter, "SpecifiedName")
    persisted_task = PersistedTask("SpecifiedName")

    task = persisted_task.load()

    with task:
        interpreter.load_task.assert_called_with("SpecifiedName")
        assert task._handle == "MyTaskHandle"
        assert task._close_on_exit == new_session_initialized
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/unit/test_dotenv_path.py sha256=51f84cfb4592d87774e0b7383e451fb71e365318cb09cad2c4fa9807713e87e6 bytes=1156 -->
## FILE: tests/unit/test_dotenv_path.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/unit/test_dotenv_path.py`
- sha256: `51f84cfb4592d87774e0b7383e451fb71e365318cb09cad2c4fa9807713e87e6`
- bytes: 1156

````python
from pathlib import Path

import pytest

from nidaqmx import _dotenv_path


@pytest.mark.parametrize("dotenv_exists", [False, True])
def test___dotenv_exists_varies___has_dotenv_file___matches_dotenv_exists(
    dotenv_exists: bool, tmp_path: Path
) -> None:
    if dotenv_exists:
        (tmp_path / ".env").write_text("")
    subdirs = [tmp_path / "a", tmp_path / "a" / "b", tmp_path / "a" / "b" / "c"]
    for dir in subdirs:
        dir.mkdir()

    assert _dotenv_path._has_dotenv_file(tmp_path) == dotenv_exists
    assert all([_dotenv_path._has_dotenv_file(p) == dotenv_exists for p in subdirs])


def test___get_caller_path___returns_this_modules_path() -> None:
    assert _dotenv_path._get_caller_path() == Path(__file__)


def test___get_package_path___returns_package_dir() -> None:
    assert _dotenv_path._get_package_path() == Path(_dotenv_path.__file__).parent


def test___get_script_or_exe_path___returns_pytest_path() -> None:
    path = _dotenv_path._get_script_or_exe_path()

    assert path is not None
    assert "pytest" in path.parts or "pytest.exe" in path.parts or "vscode_pytest" in path.parts
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/unit/test_feature_toggles.py sha256=bb416f54e1e1295cd318234e730bc1ebcabdc57e99b28b48c29870b17a86b098 bytes=4002 -->
## FILE: tests/unit/test_feature_toggles.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/unit/test_feature_toggles.py`
- sha256: `bb416f54e1e1295cd318234e730bc1ebcabdc57e99b28b48c29870b17a86b098`
- bytes: 4002

````python
from __future__ import annotations

import pytest
from pytest_mock import MockerFixture

from nidaqmx._feature_toggles import (
    CodeReadiness,
    FeatureNotSupportedError,
    FeatureToggle,
    get_code_readiness_level,
    requires_feature,
)

RELEASE_FEATURE = FeatureToggle("RELEASE_FEATURE", CodeReadiness.RELEASE)
NEXT_RELEASE_FEATURE = FeatureToggle("NEXT_RELEASE_FEATURE", CodeReadiness.NEXT_RELEASE)
INCOMPLETE_FEATURE = FeatureToggle("INCOMPLETE_FEATURE", CodeReadiness.INCOMPLETE)
PROTOTYPE_FEATURE = FeatureToggle("PROTOTYPE_FEATURE", CodeReadiness.PROTOTYPE)


@requires_feature(PROTOTYPE_FEATURE)
def _prototype_function(x: int, y: str, z: list[int]) -> str:
    return _prototype_function_impl(x, y, z)


def _prototype_function_impl(x: int, y: str, z: list[int]) -> str:
    return ""


def test___default_code_readiness_level___get_code_readiness_level___equals_prototype() -> None:
    assert get_code_readiness_level() == CodeReadiness.PROTOTYPE


@pytest.mark.use_code_readiness(CodeReadiness.RELEASE)
def test___use_release_readiness___get_code_readiness_level___equals_release() -> None:
    assert get_code_readiness_level() == CodeReadiness.RELEASE


@pytest.mark.use_code_readiness(CodeReadiness.NEXT_RELEASE)
def test___use_next_release_readiness___get_code_readiness_level___equals_next_release() -> None:
    assert get_code_readiness_level() == CodeReadiness.NEXT_RELEASE


def test___default_code_readiness_level___is_enabled___returns_true() -> None:
    assert RELEASE_FEATURE.is_enabled
    assert NEXT_RELEASE_FEATURE.is_enabled
    assert INCOMPLETE_FEATURE.is_enabled
    assert PROTOTYPE_FEATURE.is_enabled


@pytest.mark.use_code_readiness(CodeReadiness.INCOMPLETE)
def test___use_incomplete_readiness___is_enabled___reflects_code_readiness_level() -> None:
    assert RELEASE_FEATURE.is_enabled
    assert NEXT_RELEASE_FEATURE.is_enabled
    assert INCOMPLETE_FEATURE.is_enabled
    assert not PROTOTYPE_FEATURE.is_enabled


@pytest.mark.use_code_readiness(CodeReadiness.NEXT_RELEASE)
def test___use_next_release_readiness___is_enabled___reflects_code_readiness_level() -> None:
    assert RELEASE_FEATURE.is_enabled
    assert NEXT_RELEASE_FEATURE.is_enabled
    assert not INCOMPLETE_FEATURE.is_enabled
    assert not PROTOTYPE_FEATURE.is_enabled


@pytest.mark.use_code_readiness(CodeReadiness.RELEASE)
def test___release_readiness_level___is_enabled___reflects_code_readiness_level() -> None:
    assert RELEASE_FEATURE.is_enabled
    assert not NEXT_RELEASE_FEATURE.is_enabled
    assert not INCOMPLETE_FEATURE.is_enabled
    assert not PROTOTYPE_FEATURE.is_enabled


@pytest.mark.enable_feature_toggle(PROTOTYPE_FEATURE)
def test___feature_toggle_enabled___is_enabled___returns_true() -> None:
    assert PROTOTYPE_FEATURE.is_enabled


@pytest.mark.disable_feature_toggle(PROTOTYPE_FEATURE)
def test___feature_toggle_disabled___is_enabled___returns_false() -> None:
    assert not PROTOTYPE_FEATURE.is_enabled


@pytest.mark.enable_feature_toggle(PROTOTYPE_FEATURE)
def test___feature_toggle_enabled___call_decorated_function___impl_called(
    mocker: MockerFixture,
) -> None:
    impl = mocker.patch("tests.unit.test_feature_toggles._prototype_function_impl")
    impl.return_value = "def"

    result = _prototype_function(123, "abc", [4, 5, 6])

    impl.assert_called_once_with(123, "abc", [4, 5, 6])
    assert result == "def"


@pytest.mark.disable_feature_toggle(PROTOTYPE_FEATURE)
def test___feature_toggle_disabled___call_decorated_function___error_raised(
    mocker: MockerFixture,
) -> None:
    impl = mocker.patch("tests.unit.test_feature_toggles._prototype_function_impl")
    impl.return_value = "def"

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        _ = _prototype_function(123, "abc", [4, 5, 6])

    impl.assert_not_called()
    assert "set NIDAQMX_ENABLE_PROTOTYPE_FEATURE" in exc_info.value.args[0]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/unit/test_grpc_time.py sha256=133f3afd302c232e074749c0487f8ce32ae68bb563af716d6587e31a097d90e8 bytes=12803 -->
## FILE: tests/unit/test_grpc_time.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/unit/test_grpc_time.py`
- sha256: `133f3afd302c232e074749c0487f8ce32ae68bb563af716d6587e31a097d90e8`
- bytes: 12803

````python
from datetime import datetime as std_datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import pytest
from hightime import datetime as ht_datetime

from tests.unit._time_utils import (
    JAN_01_1850_DATETIME,
    JAN_01_1850_HIGHTIME,
    JAN_01_1850_TIMESTAMP_1970_EPOCH,
    JAN_01_2002_DATETIME,
    JAN_01_2002_HIGHTIME,
    JAN_01_2002_TIMESTAMP_1970_EPOCH,
)

try:
    import nidaqmx._grpc_time as grpc_time
    from nidaqmx._stubs import nidaqmx_pb2
except ImportError:
    pass


@pytest.mark.parametrize("from_dt", [(JAN_01_2002_DATETIME), (JAN_01_2002_HIGHTIME)])
def test___utc_datetime_after_1970___convert_to_timestamp___is_reversible(from_dt):
    to_ts = grpc_time.convert_time_to_timestamp(from_dt)
    roundtrip_dt = grpc_time.convert_timestamp_to_time(to_ts, tzinfo=timezone.utc)

    total_nanoseconds = to_ts.ToNanoseconds()
    seconds, nanos = divmod(total_nanoseconds, grpc_time._NS_PER_S)
    assert seconds == JAN_01_2002_TIMESTAMP_1970_EPOCH
    assert nanos == 0
    assert roundtrip_dt == JAN_01_2002_HIGHTIME


@pytest.mark.parametrize("from_dt", [(JAN_01_1850_DATETIME), (JAN_01_1850_HIGHTIME)])
def test___utc_datetime_before_1970___convert_to_timestamp___is_reversible(from_dt):
    to_ts = grpc_time.convert_time_to_timestamp(from_dt)
    roundtrip_dt = grpc_time.convert_timestamp_to_time(to_ts, tzinfo=timezone.utc)

    total_nanoseconds = to_ts.ToNanoseconds()
    seconds, nanos = divmod(total_nanoseconds, grpc_time._NS_PER_S)
    assert seconds == JAN_01_1850_TIMESTAMP_1970_EPOCH
    assert nanos == 0
    assert roundtrip_dt == JAN_01_1850_HIGHTIME


@pytest.mark.parametrize("request_dt", [(JAN_01_2002_DATETIME), (JAN_01_2002_HIGHTIME)])
def test___utc_datetime_after_1970___convert_to_grpc_request___succeeds(request_dt):
    request = nidaqmx_pb2.CfgTimeStartTrigRequest()

    grpc_time.convert_time_to_timestamp(request_dt, request.when)

    total_nanoseconds = request.when.ToNanoseconds()
    seconds, nanos = divmod(total_nanoseconds, grpc_time._NS_PER_S)
    assert seconds == JAN_01_2002_TIMESTAMP_1970_EPOCH
    assert nanos == 0


@pytest.mark.parametrize("request_dt", [(JAN_01_1850_DATETIME), (JAN_01_1850_HIGHTIME)])
def test___utc_datetime_before_1970___convert_to_grpc_request___succeeds(request_dt):
    request = nidaqmx_pb2.CfgTimeStartTrigRequest()

    grpc_time.convert_time_to_timestamp(request_dt, request.when)

    total_nanoseconds = request.when.ToNanoseconds()
    seconds, nanos = divmod(total_nanoseconds, grpc_time._NS_PER_S)
    assert seconds == JAN_01_1850_TIMESTAMP_1970_EPOCH
    assert nanos == 0


@pytest.mark.parametrize("response_dt", [(JAN_01_2002_DATETIME), (JAN_01_2002_HIGHTIME)])
def test___grpc_response_after_1970___convert_to_timestamp___succeeds(response_dt):
    response = nidaqmx_pb2.GetStartTrigTrigWhenResponse()
    grpc_time.convert_time_to_timestamp(response_dt, response.data)

    to_dt = grpc_time.convert_timestamp_to_time(response.data, tzinfo=timezone.utc)

    assert to_dt == JAN_01_2002_HIGHTIME


@pytest.mark.parametrize("response_dt", [(JAN_01_1850_DATETIME), (JAN_01_1850_HIGHTIME)])
def test___grpc_response_before_1970___convert_to_timestamp___succeeds(response_dt):
    response = nidaqmx_pb2.GetStartTrigTrigWhenResponse()
    grpc_time.convert_time_to_timestamp(response_dt, response.data)

    to_dt = grpc_time.convert_timestamp_to_time(response.data, tzinfo=timezone.utc)

    assert to_dt == JAN_01_1850_HIGHTIME


@pytest.mark.parametrize(
    "date",
    [
        (std_datetime(1904, 1, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 1, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 2, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 3, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 4, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 5, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 6, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 7, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 8, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 9, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 10, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 11, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 12, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 1, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 2, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 3, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 4, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 5, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 6, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 7, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 8, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 9, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 10, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 11, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 12, 1, tzinfo=timezone.utc)),
    ],
)
def test___utc_datetime___convert_to_timestamp_with_dst___is_reversible(date):
    # we use a location that has daylight savings date change on the dates above
    target_timezone = ZoneInfo("America/Los_Angeles")
    astimezone_date = date.astimezone(target_timezone)

    to_ts = grpc_time.convert_time_to_timestamp(date)
    roundtrip_dt = grpc_time.convert_timestamp_to_time(to_ts, tzinfo=target_timezone)

    assert astimezone_date == roundtrip_dt


@pytest.mark.parametrize(
    "datetime_cls, tzinfo, expected_offset",
    [
        (std_datetime, timezone(timedelta(minutes=30)), -1800),
        (std_datetime, timezone(timedelta(minutes=-30)), 1800),
        (std_datetime, timezone(timedelta(hours=1)), -3600),
        (std_datetime, timezone(timedelta(hours=-1)), 3600),
        (ht_datetime, timezone(timedelta(minutes=30)), -1800),
        (ht_datetime, timezone(timedelta(minutes=-30)), 1800),
        (ht_datetime, timezone(timedelta(hours=1)), -3600),
        (ht_datetime, timezone(timedelta(hours=-1)), 3600),
    ],
)
def test___tz_datetime_after_1970___convert_to_timestamp___is_reversible(
    datetime_cls, tzinfo, expected_offset
):
    from_dt = datetime_cls(2002, 1, 1, tzinfo=tzinfo)

    to_ts = grpc_time.convert_time_to_timestamp(from_dt)
    roundtrip_dt = grpc_time.convert_timestamp_to_time(to_ts, tzinfo=tzinfo)

    assert to_ts.seconds == JAN_01_2002_TIMESTAMP_1970_EPOCH + expected_offset
    assert to_ts.nanos == 0
    assert from_dt == roundtrip_dt


@pytest.mark.parametrize(
    "datetime_cls, tzinfo, expected_offset",
    [
        (std_datetime, timezone(timedelta(minutes=30)), -1800),
        (std_datetime, timezone(timedelta(minutes=-30)), 1800),
        (std_datetime, timezone(timedelta(hours=1)), -3600),
        (std_datetime, timezone(timedelta(hours=-1)), 3600),
        (ht_datetime, timezone(timedelta(minutes=30)), -1800),
        (ht_datetime, timezone(timedelta(minutes=-30)), 1800),
        (ht_datetime, timezone(timedelta(hours=1)), -3600),
        (ht_datetime, timezone(timedelta(hours=-1)), 3600),
    ],
)
def test___tz_datetime_before_1970___convert_to_timestamp___is_reversible(
    datetime_cls, tzinfo, expected_offset
):
    from_dt = datetime_cls(1850, 1, 1, tzinfo=tzinfo)

    to_ts = grpc_time.convert_time_to_timestamp(from_dt)
    roundtrip_dt = grpc_time.convert_timestamp_to_time(to_ts, tzinfo=tzinfo)

    assert to_ts.seconds == JAN_01_1850_TIMESTAMP_1970_EPOCH + expected_offset
    assert to_ts.nanos == 0
    assert from_dt == roundtrip_dt


@pytest.mark.parametrize(
    "base_dt, microsecond, nanoseconds",
    [
        (JAN_01_2002_DATETIME, 0, 0),
        (JAN_01_2002_DATETIME, 1, 1000),
        (JAN_01_2002_DATETIME, 250000, 250000000),
        (JAN_01_2002_DATETIME, 500000, 500000000),
        (JAN_01_2002_DATETIME, 750000, 750000000),
        (JAN_01_2002_DATETIME, 999999, 999999000),
        (JAN_01_2002_HIGHTIME, 0, 0),
        (JAN_01_2002_HIGHTIME, 1, 1000),
        (JAN_01_2002_HIGHTIME, 250000, 250000000),
        (JAN_01_2002_HIGHTIME, 500000, 500000000),
        (JAN_01_2002_HIGHTIME, 750000, 750000000),
        (JAN_01_2002_HIGHTIME, 999999, 999999000),
    ],
)
def test___datetime_after_1970_with_microseconds___convert_to_timestamp___is_reversible(
    base_dt, microsecond, nanoseconds
):
    from_dt = base_dt.replace(microsecond=microsecond)

    to_ts = grpc_time.convert_time_to_timestamp(from_dt)
    roundtrip_dt = grpc_time.convert_timestamp_to_time(to_ts, tzinfo=timezone.utc)

    assert to_ts.seconds == JAN_01_2002_TIMESTAMP_1970_EPOCH
    assert to_ts.nanos == nanoseconds
    assert roundtrip_dt.microsecond == microsecond


@pytest.mark.parametrize(
    "base_dt, microsecond, nanoseconds",
    [
        (JAN_01_1850_DATETIME, 0, 0),
        (JAN_01_1850_DATETIME, 1, 1000),
        (JAN_01_1850_DATETIME, 250000, 250000000),
        (JAN_01_1850_DATETIME, 500000, 500000000),
        (JAN_01_1850_DATETIME, 750000, 750000000),
        (JAN_01_1850_DATETIME, 999999, 999999000),
        (JAN_01_1850_HIGHTIME, 0, 0),
        (JAN_01_1850_HIGHTIME, 1, 1000),
        (JAN_01_1850_HIGHTIME, 250000, 250000000),
        (JAN_01_1850_HIGHTIME, 500000, 500000000),
        (JAN_01_1850_HIGHTIME, 750000, 750000000),
        (JAN_01_1850_HIGHTIME, 999999, 999999000),
    ],
)
def test___datetime_before_1970_with_microseconds___convert_to_timestamp___is_reversible(
    base_dt, microsecond, nanoseconds
):
    from_dt = base_dt.replace(microsecond=microsecond)

    to_ts = grpc_time.convert_time_to_timestamp(from_dt)
    roundtrip_dt = grpc_time.convert_timestamp_to_time(to_ts, tzinfo=timezone.utc)

    if microsecond:
        # with a change of non-zero subsecond value, the seconds value is off by 1
        # because of negative seconds value
        assert to_ts.seconds == JAN_01_1850_TIMESTAMP_1970_EPOCH + 1
    else:
        assert to_ts.seconds == JAN_01_1850_TIMESTAMP_1970_EPOCH
    assert to_ts.nanos == nanoseconds
    assert roundtrip_dt.microsecond == microsecond


@pytest.mark.parametrize(
    "base_dt, femtosecond, nanoseconds",
    [
        (JAN_01_2002_HIGHTIME, 0, 0),
        (JAN_01_2002_HIGHTIME, 1, 0),
        # If femtoseconds get high enough, then it should round up
        (JAN_01_2002_HIGHTIME, 500000, 1),
        (JAN_01_2002_HIGHTIME, 999999, 1),
        # And of course, whole nanos
        (JAN_01_2002_HIGHTIME, 1000000, 1),
        (JAN_01_2002_HIGHTIME, 1000001, 1),
        (JAN_01_2002_HIGHTIME, 1500000, 2),
        (JAN_01_2002_HIGHTIME, 1999999, 2),
        (JAN_01_2002_HIGHTIME, 2000000, 2),
        (JAN_01_2002_HIGHTIME, 2000001, 2),
    ],
)
def test___datetime_after_1970_with_femtoseconds___convert_to_timestamp___is_reversible(
    base_dt, femtosecond, nanoseconds
):
    from_dt = base_dt.replace(femtosecond=femtosecond)

    to_ts = grpc_time.convert_time_to_timestamp(from_dt)
    roundtrip_dt = grpc_time.convert_timestamp_to_time(to_ts, tzinfo=timezone.utc)

    assert to_ts.seconds == JAN_01_2002_TIMESTAMP_1970_EPOCH
    assert to_ts.nanos == nanoseconds
    # we lost femtosecond precision coercing to nanoseconds.
    assert roundtrip_dt.femtosecond == nanoseconds * (10**6)


@pytest.mark.parametrize(
    "base_dt, femtosecond, nanoseconds",
    [
        (JAN_01_1850_HIGHTIME, 0, 0),
        (JAN_01_1850_HIGHTIME, 1, 0),
        # If femtoseconds get high enough, then it should round up
        (JAN_01_1850_HIGHTIME, 500000, 1),
        (JAN_01_1850_HIGHTIME, 999999, 1),
        # And of course, whole nanos
        (JAN_01_1850_HIGHTIME, 1000000, 1),
        (JAN_01_1850_HIGHTIME, 1000001, 1),
        (JAN_01_1850_HIGHTIME, 1500000, 2),
        (JAN_01_1850_HIGHTIME, 1999999, 2),
        (JAN_01_1850_HIGHTIME, 2000000, 2),
        (JAN_01_1850_HIGHTIME, 2000001, 2),
    ],
)
def test___datetime_before_1970_with_femtoseconds___convert_to_timestamp___is_reversible(
    base_dt, femtosecond, nanoseconds
):
    from_dt = base_dt.replace(femtosecond=femtosecond)

    to_ts = grpc_time.convert_time_to_timestamp(from_dt)
    roundtrip_dt = grpc_time.convert_timestamp_to_time(to_ts, tzinfo=timezone.utc)

    if femtosecond:
        # with a change of non-zero subsecond value, the seconds value is off by 1
        # because of negative seconds value
        assert to_ts.seconds == JAN_01_1850_TIMESTAMP_1970_EPOCH + 1
    else:
        assert to_ts.seconds == JAN_01_1850_TIMESTAMP_1970_EPOCH
    assert to_ts.nanos == nanoseconds
    # we lost femtosecond precision coercing to nanoseconds.
    assert roundtrip_dt.femtosecond == nanoseconds * (10**6)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/unit/test_lib_time.py sha256=475c697fc2f810b130d76e945df8606d52c1ceef1b428139756d99d5b1ed22b0 bytes=15696 -->
## FILE: tests/unit/test_lib_time.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/unit/test_lib_time.py`
- sha256: `475c697fc2f810b130d76e945df8606d52c1ceef1b428139756d99d5b1ed22b0`
- bytes: 15696

````python
import random
from copy import copy
from datetime import datetime as std_datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import pytest
from hightime import datetime as ht_datetime

from nidaqmx._lib_time import AbsoluteTime as LibTimestamp
from nidaqmx._time import _convert_to_desired_timezone
from tests.unit._time_utils import (
    JAN_01_1850_DATETIME,
    JAN_01_1850_HIGHTIME,
    JAN_01_1850_TIMESTAMP_1904_EPOCH,
    JAN_01_1904_DATETIME,
    JAN_01_1904_HIGHTIME,
    JAN_01_1904_TIMESTAMP_1904_EPOCH,
    JAN_01_2002_DATETIME,
    JAN_01_2002_HIGHTIME,
    JAN_01_2002_TIMESTAMP_1904_EPOCH,
)

JAN_01_2002_LIB = LibTimestamp(lsb=0, msb=JAN_01_2002_TIMESTAMP_1904_EPOCH)
JAN_01_1904_LIB = LibTimestamp(lsb=0, msb=JAN_01_1904_TIMESTAMP_1904_EPOCH)
JAN_01_1850_LIB = LibTimestamp(lsb=0, msb=JAN_01_1850_TIMESTAMP_1904_EPOCH)


def test___timestamps___sort___is_ordered():
    ordered = [
        LibTimestamp(msb=1, lsb=0),
        LibTimestamp(msb=2, lsb=0),
        LibTimestamp(msb=2, lsb=1),
        LibTimestamp(msb=2, lsb=2),
        LibTimestamp(msb=3, lsb=0),
    ]

    shuffled = copy(ordered)
    random.shuffle(shuffled)
    assert sorted(shuffled) == ordered


@pytest.mark.parametrize("from_dt", [(JAN_01_2002_DATETIME), (JAN_01_2002_HIGHTIME)])
def test___utc_datetime_after_1904___convert_to_timestamp___is_reversible(from_dt):
    to_ts = LibTimestamp.from_datetime(from_dt)
    roundtrip_dt = to_ts.to_datetime(tzinfo=timezone.utc)

    assert to_ts == JAN_01_2002_LIB
    assert roundtrip_dt == JAN_01_2002_HIGHTIME


@pytest.mark.parametrize("from_dt", [(JAN_01_1904_DATETIME), (JAN_01_1904_HIGHTIME)])
def test___utc_datetime_on_1904___convert_to_timestamp___is_reversible(from_dt):
    to_ts = LibTimestamp.from_datetime(from_dt)
    roundtrip_dt = to_ts.to_datetime(tzinfo=timezone.utc)

    assert to_ts == JAN_01_1904_LIB
    assert roundtrip_dt == JAN_01_1904_HIGHTIME


@pytest.mark.parametrize("from_dt", [(JAN_01_1850_DATETIME), (JAN_01_1850_HIGHTIME)])
def test___utc_datetime_before_1904___convert_to_timestamp___is_reversible(from_dt):
    to_ts = LibTimestamp.from_datetime(from_dt)
    roundtrip_dt = to_ts.to_datetime(tzinfo=timezone.utc)

    assert to_ts == JAN_01_1850_LIB
    assert roundtrip_dt == JAN_01_1850_HIGHTIME


@pytest.mark.parametrize(
    "date",
    [
        (std_datetime(1904, 1, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 1, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 2, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 3, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 4, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 5, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 6, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 7, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 8, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 9, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 10, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 11, 1, tzinfo=timezone.utc)),
        (std_datetime(2023, 12, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 1, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 2, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 3, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 4, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 5, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 6, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 7, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 8, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 9, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 10, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 11, 1, tzinfo=timezone.utc)),
        (ht_datetime(2023, 12, 1, tzinfo=timezone.utc)),
    ],
)
def test___utc_datetime___convert_to_timestamp_with_dst___is_reversible(date):
    # we use a location that has daylight savings date change on the dates above
    target_timezone = ZoneInfo("America/Los_Angeles")
    astimezone_date = date.astimezone(target_timezone)

    to_ts = LibTimestamp.from_datetime(date)
    roundtrip_dt = to_ts.to_datetime(tzinfo=target_timezone)

    assert astimezone_date == roundtrip_dt


@pytest.mark.parametrize(
    "base_dt, femtosecond, subseconds",
    [
        (ht_datetime(2023, 3, 12, tzinfo=timezone.utc), 0, 0),
        (ht_datetime(2023, 3, 12, tzinfo=timezone.utc), 1, 0x480F),
        (ht_datetime(2023, 6, 1, tzinfo=timezone.utc), 0, 0),
        (ht_datetime(2023, 6, 1, tzinfo=timezone.utc), 1, 0x480F),
        (ht_datetime(2023, 11, 5, tzinfo=timezone.utc), 0, 0),
        (ht_datetime(2023, 11, 5, tzinfo=timezone.utc), 1, 0x480F),
    ],
)
def test___utc_datetime_with_femtoseconds___convert_to_timestamp_with_dst___is_reversible(
    base_dt, femtosecond, subseconds
):
    target_timezone = ZoneInfo("America/Los_Angeles")
    from_dt = base_dt.replace(femtosecond=femtosecond)
    expected_la_time = _convert_to_desired_timezone(from_dt, target_timezone)

    ts = LibTimestamp.from_datetime(from_dt)
    roundtrip_dt = ts.to_datetime(tzinfo=target_timezone)

    assert ts.msb == LibTimestamp.from_datetime(expected_la_time).msb
    assert ts.lsb == subseconds
    assert roundtrip_dt.microsecond == expected_la_time.microsecond
    assert roundtrip_dt.femtosecond == expected_la_time.femtosecond
    # The yoctosecond field may contain up to 1 NI-BTF tick of rounding error.
    assert roundtrip_dt.yoctosecond <= 54210


@pytest.mark.parametrize(
    "base_dt, yoctosecond, subseconds",
    [
        (ht_datetime(2023, 3, 12, tzinfo=timezone.utc), 0, 0),
        (ht_datetime(2023, 3, 12, tzinfo=timezone.utc), 54210, 1),
        (ht_datetime(2023, 6, 1, tzinfo=timezone.utc), 0, 0),
        (ht_datetime(2023, 6, 1, tzinfo=timezone.utc), 54210, 1),
        (ht_datetime(2023, 11, 5, tzinfo=timezone.utc), 0, 0),
        (ht_datetime(2023, 11, 5, tzinfo=timezone.utc), 54210, 1),
    ],
)
def test___utc_datetime_with_yoctoseconds___convert_to_timestamp_with_dst___is_reversible(
    base_dt, yoctosecond, subseconds
):
    target_timezone = ZoneInfo("America/Los_Angeles")
    from_dt = base_dt.replace(yoctosecond=yoctosecond)
    expected_la_time = _convert_to_desired_timezone(from_dt, target_timezone)

    ts = LibTimestamp.from_datetime(from_dt)
    roundtrip_dt = ts.to_datetime(tzinfo=target_timezone)

    assert ts.msb == LibTimestamp.from_datetime(expected_la_time).msb
    assert ts.lsb == subseconds
    assert roundtrip_dt.microsecond == expected_la_time.microsecond
    assert roundtrip_dt.femtosecond == expected_la_time.femtosecond
    assert roundtrip_dt.yoctosecond == expected_la_time.yoctosecond


@pytest.mark.parametrize(
    "datetime_cls, tzinfo, expected_offset",
    [
        (std_datetime, timezone(timedelta(minutes=30)), -1800),
        (std_datetime, timezone(timedelta(minutes=-30)), 1800),
        (std_datetime, timezone(timedelta(hours=1)), -3600),
        (std_datetime, timezone(timedelta(hours=-1)), 3600),
        (ht_datetime, timezone(timedelta(minutes=30)), -1800),
        (ht_datetime, timezone(timedelta(minutes=-30)), 1800),
        (ht_datetime, timezone(timedelta(hours=1)), -3600),
        (ht_datetime, timezone(timedelta(hours=-1)), 3600),
    ],
)
def test___tz_datetime_after_1904___convert_to_timestamp___is_reversible(
    datetime_cls, tzinfo, expected_offset
):
    from_dt = datetime_cls(2002, 1, 1, tzinfo=tzinfo)

    to_ts = LibTimestamp.from_datetime(from_dt)
    roundtrip_dt = to_ts.to_datetime(tzinfo=tzinfo)

    assert to_ts.msb == JAN_01_2002_LIB.msb + expected_offset
    assert to_ts.lsb == JAN_01_2002_LIB.lsb
    assert roundtrip_dt == from_dt


@pytest.mark.parametrize(
    "datetime_cls, tzinfo, expected_offset",
    [
        (std_datetime, timezone(timedelta(minutes=30)), -1800),
        (std_datetime, timezone(timedelta(minutes=-30)), 1800),
        (std_datetime, timezone(timedelta(hours=1)), -3600),
        (std_datetime, timezone(timedelta(hours=-1)), 3600),
        (ht_datetime, timezone(timedelta(minutes=30)), -1800),
        (ht_datetime, timezone(timedelta(minutes=-30)), 1800),
        (ht_datetime, timezone(timedelta(hours=1)), -3600),
        (ht_datetime, timezone(timedelta(hours=-1)), 3600),
    ],
)
def test___tz_datetime_before_1904___convert_to_timestamp___is_reversible(
    datetime_cls, tzinfo, expected_offset
):
    from_dt = datetime_cls(1850, 1, 1, tzinfo=tzinfo)

    to_ts = LibTimestamp.from_datetime(from_dt)
    roundtrip_dt = to_ts.to_datetime(tzinfo=tzinfo)

    assert to_ts.msb == JAN_01_1850_LIB.msb + expected_offset
    assert to_ts.lsb == JAN_01_1850_LIB.lsb
    assert roundtrip_dt == from_dt


@pytest.mark.parametrize(
    "base_dt, microsecond, subseconds",
    [
        (JAN_01_2002_DATETIME, 0, 0),
        (JAN_01_2002_DATETIME, 1, 0x10C6F7A0B5EE),
        (JAN_01_2002_DATETIME, 250000, 0x4000000000000000),
        (JAN_01_2002_DATETIME, 500000, 0x8000000000000000),
        (JAN_01_2002_DATETIME, 750000, 0xC000000000000000),
        (JAN_01_2002_DATETIME, 999999, 0xFFFFEF39085F4800),
        (JAN_01_2002_HIGHTIME, 0, 0),
        (JAN_01_2002_HIGHTIME, 1, 0x10C6F7A0B5EE),
        (JAN_01_2002_HIGHTIME, 250000, 0x4000000000000000),
        (JAN_01_2002_HIGHTIME, 500000, 0x8000000000000000),
        (JAN_01_2002_HIGHTIME, 750000, 0xC000000000000000),
        (JAN_01_2002_HIGHTIME, 999999, 0xFFFFEF39085F4800),
    ],
)
def test___datetime_after_1904_with_microseconds___convert_to_timestamp___is_reversible(
    base_dt, microsecond, subseconds
):
    from_dt = base_dt.replace(microsecond=microsecond)

    to_ts = LibTimestamp.from_datetime(from_dt)
    roundtrip_dt = to_ts.to_datetime(tzinfo=timezone.utc)

    assert to_ts.msb == JAN_01_2002_LIB.msb
    assert to_ts.lsb == subseconds
    # comparison is tricky since imprecision in the conversion to NI-BTF are
    # caught by the higher precision values in hightime, so we round here.
    roundtrip_dt_microsecond = roundtrip_dt.microsecond
    if roundtrip_dt.femtosecond > LibTimestamp.MAX_FS / 2:
        roundtrip_dt_microsecond += 1

    assert roundtrip_dt_microsecond == microsecond


@pytest.mark.parametrize(
    "base_dt, microsecond, subseconds",
    [
        (JAN_01_1850_DATETIME, 0, 0),
        (JAN_01_1850_DATETIME, 1, 0x10C6F7A0B5EE),
        (JAN_01_1850_DATETIME, 250000, 0x4000000000000000),
        (JAN_01_1850_DATETIME, 500000, 0x8000000000000000),
        (JAN_01_1850_DATETIME, 750000, 0xC000000000000000),
        (JAN_01_1850_DATETIME, 999999, 0xFFFFEF39085F4800),
        (JAN_01_1850_HIGHTIME, 0, 0),
        (JAN_01_1850_HIGHTIME, 1, 0x10C6F7A0B5EE),
        (JAN_01_1850_HIGHTIME, 250000, 0x4000000000000000),
        (JAN_01_1850_HIGHTIME, 500000, 0x8000000000000000),
        (JAN_01_1850_HIGHTIME, 750000, 0xC000000000000000),
        (JAN_01_1850_HIGHTIME, 999999, 0xFFFFEF39085F4800),
    ],
)
def test___datetime_before_1904_with_microseconds___convert_to_timestamp___is_reversible(
    base_dt, microsecond, subseconds
):
    from_dt = base_dt.replace(microsecond=microsecond)

    to_ts = LibTimestamp.from_datetime(from_dt)
    roundtrip_dt = to_ts.to_datetime(tzinfo=timezone.utc)

    if microsecond:
        # with a change of non-zero subsecond value, the seconds value is off by 1
        # because of negative seconds value
        assert to_ts.msb == JAN_01_1850_LIB.msb + 1
    else:
        assert to_ts.msb == JAN_01_1850_LIB.msb
    assert to_ts.lsb == subseconds
    # comparison is tricky since imprecision in the conversion to NI-BTF are
    # caught by the higher precision values in hightime, so we round here.
    assert pytest.approx(roundtrip_dt.microsecond, abs=1) == microsecond


@pytest.mark.parametrize(
    "base_dt, femtosecond, subseconds",
    [
        (JAN_01_2002_HIGHTIME, 0, 0),
        (JAN_01_2002_HIGHTIME, 1, 0x480F),
    ],
)
def test___datetime_with_femtoseconds___convert_to_timestamp___is_reversible(
    base_dt, femtosecond, subseconds
):
    from_dt = base_dt.replace(femtosecond=femtosecond)

    ts = LibTimestamp.from_datetime(from_dt)
    roundtrip_dt = ts.to_datetime(tzinfo=timezone.utc)

    assert ts.msb == JAN_01_2002_LIB.msb
    assert ts.lsb == subseconds
    # comparison is tricky since imprecision in the conversion to NI-BTF are
    # caught by the higher precision values in hightime, so we round here.
    roundtrip_dt_femtosecond = roundtrip_dt.femtosecond
    if roundtrip_dt.yoctosecond > LibTimestamp.MAX_YS / 2:
        roundtrip_dt_femtosecond += 1
    assert roundtrip_dt_femtosecond == femtosecond


@pytest.mark.parametrize(
    "base_dt, femtosecond, subseconds",
    [
        (JAN_01_1850_HIGHTIME, 0, 0),
        (JAN_01_1850_HIGHTIME, 1, 0x480F),
    ],
)
def test___datetime_before_1904_with_femtoseconds___convert_to_timestamp___is_reversible(
    base_dt, femtosecond, subseconds
):
    from_dt = base_dt.replace(femtosecond=femtosecond)

    ts = LibTimestamp.from_datetime(from_dt)
    roundtrip_dt = ts.to_datetime(tzinfo=timezone.utc)

    if femtosecond:
        # with a change of non-zero subsecond value, the seconds value is off by 1
        # because of negative seconds value
        assert ts.msb == JAN_01_1850_LIB.msb + 1
    else:
        assert ts.msb == JAN_01_1850_LIB.msb
    assert ts.lsb == subseconds
    # comparison is tricky since imprecision in the conversion to NI-BTF are
    # caught by the higher precision values in hightime, so we round here.
    roundtrip_dt_femtosecond = roundtrip_dt.femtosecond
    if roundtrip_dt.yoctosecond > LibTimestamp.MAX_YS / 2:
        roundtrip_dt_femtosecond += 1
    assert roundtrip_dt_femtosecond == femtosecond


@pytest.mark.parametrize(
    "base_dt, yoctosecond, subseconds, yoctosecond_round_trip",
    [
        (JAN_01_2002_HIGHTIME, 0, 0, 0),
        # Yoctoseconds is quite a bit more precise than NI-BTF
        (JAN_01_2002_HIGHTIME, 54210, 1, 54210),
        (JAN_01_2002_HIGHTIME, 54211, 1, 54210),
    ],
)
def test___datetime_after_1904_with_yoctoseconds___convert_to_timestamp___is_reversible(
    base_dt, yoctosecond, subseconds, yoctosecond_round_trip
):
    from_dt = base_dt.replace(yoctosecond=yoctosecond)

    ts = LibTimestamp.from_datetime(from_dt)
    to_dt = ts.to_datetime(tzinfo=timezone.utc)

    assert ts.msb == JAN_01_2002_LIB.msb
    assert ts.lsb == subseconds
    assert to_dt.yoctosecond == yoctosecond_round_trip


@pytest.mark.parametrize(
    "base_dt, yoctosecond, subseconds, yoctosecond_round_trip",
    [
        (JAN_01_1850_HIGHTIME, 0, 0, 0),
        # Yoctoseconds is quite a bit more precise than NI-BTF
        (JAN_01_1850_HIGHTIME, 54210, 1, 54210),
        (JAN_01_1850_HIGHTIME, 54211, 1, 54210),
    ],
)
def test___datetime_before_1904_with_yoctoseconds___convert_to_timestamp___is_reversible(
    base_dt, yoctosecond, subseconds, yoctosecond_round_trip
):
    from_dt = base_dt.replace(yoctosecond=yoctosecond)

    ts = LibTimestamp.from_datetime(from_dt)
    to_dt = ts.to_datetime(tzinfo=timezone.utc)

    if yoctosecond:
        # with a change of non-zero subsecond value, the seconds value is off by 1
        # because of negative seconds value
        assert ts.msb == JAN_01_1850_LIB.msb + 1
    else:
        assert ts.msb == JAN_01_1850_LIB.msb
    assert ts.lsb == subseconds
    assert to_dt.yoctosecond == yoctosecond_round_trip
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/unit/test_task.py sha256=540c42ae1414a389e32fc47e67ed1ecde3050e239543f375a0eb1c480faf1972 bytes=6698 -->
## FILE: tests/unit/test_task.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/unit/test_task.py`
- sha256: `540c42ae1414a389e32fc47e67ed1ecde3050e239543f375a0eb1c480faf1972`
- bytes: 6698

````python
import warnings
from unittest.mock import Mock

import pytest
from pytest_mock import MockerFixture

import nidaqmx.utils
from nidaqmx import Task
from nidaqmx.task import _TaskAlternateConstructor
from tests.unit._grpc_utils import create_grpc_options
from tests.unit._task_utils import expect_create_task, expect_get_task_name


def test___init___generated_name_saved(interpreter: Mock):
    expect_create_task(interpreter)
    expect_get_task_name(interpreter, "_unnamedTask<123>")

    task = Task()

    with task:
        interpreter.create_task.assert_called_with("")
        assert task._saved_name == "_unnamedTask<123>"


def test___init_with_name___specified_name_saved(interpreter: Mock):
    expect_create_task(interpreter)
    expect_get_task_name(interpreter, "SpecifiedName")

    task = Task("SpecifiedName")

    with task:
        interpreter.create_task.assert_called_with("SpecifiedName")
        assert task._saved_name == "SpecifiedName"


def test___init_with_grpc_options___select_interpreter_called_with_grpc_options(
    interpreter: Mock, mocker: MockerFixture
):
    expect_create_task(interpreter)
    expect_get_task_name(interpreter, "_unnamedTask<123>")
    grpc_options = create_grpc_options(mocker)

    task = Task(grpc_options=grpc_options)

    with task:
        nidaqmx.utils._select_interpreter.mock.assert_called_with(grpc_options)  # type: ignore[attr-defined]


def test___init_with_name_and_grpc_options___specified_name_saved(
    interpreter: Mock, mocker: MockerFixture
):
    expect_create_task(interpreter)
    expect_get_task_name(interpreter, "SpecifiedName")
    grpc_options = create_grpc_options(mocker)

    task = Task("SpecifiedName", grpc_options=grpc_options)

    with task:
        assert task._saved_name == "SpecifiedName"


def test___init_with_name_and_grpc_options_with_specified_name___specified_name_saved(
    interpreter: Mock, mocker: MockerFixture
):
    expect_create_task(interpreter)
    expect_get_task_name(interpreter, "SpecifiedName")
    grpc_options = create_grpc_options(mocker, "SpecifiedName")

    task = Task("SpecifiedName", grpc_options=grpc_options)

    with task:
        assert task._saved_name == "SpecifiedName"


def test___init_with_name_and_grpc_options_with_mismatched_name___daqerror_raised(
    interpreter: Mock, mocker: MockerFixture
):
    expect_create_task(interpreter)
    expect_get_task_name(interpreter, "SpecifiedName")
    grpc_options = create_grpc_options(mocker, "MismatchedName")

    with pytest.raises(nidaqmx.DaqError):
        _ = Task("SpecifiedName", grpc_options=grpc_options)


@pytest.mark.parametrize("new_session_initialized", [False, True])
def test___init_with_name___create_task_called(interpreter: Mock, new_session_initialized: bool):
    expect_create_task(interpreter, "MyTaskHandle", new_session_initialized)
    expect_get_task_name(interpreter, "SpecifiedName")

    task = Task("SpecifiedName")

    with task:
        interpreter.create_task.assert_called_with("SpecifiedName")
        assert task._handle == "MyTaskHandle"
        assert task._close_on_exit == new_session_initialized


@pytest.mark.parametrize("new_session_initialized", [False, True])
def test___call_alternate_constructor___create_task_not_called(
    interpreter: Mock, new_session_initialized: bool
):
    expect_get_task_name(interpreter, "SpecifiedName")

    task = _TaskAlternateConstructor("InjectedTaskHandle", interpreter, new_session_initialized)

    with task:
        interpreter.create_task.assert_not_called()
        assert task._handle == "InjectedTaskHandle"
        assert task._close_on_exit == new_session_initialized


@pytest.mark.parametrize("close_on_exit", [False, True])
def test___varying_close_on_exit___close___clear_task_called(
    interpreter: Mock, close_on_exit: bool
):
    expect_create_task(interpreter, "MyTaskHandle", close_on_exit)
    expect_get_task_name(interpreter, "MyTask")
    task = Task("MyTask")
    task_handle = task._handle

    task.close()

    interpreter.clear_task.assert_called_with(task_handle)


def test___close_on_exit___context_manager___clear_task_called(interpreter: Mock):
    expect_create_task(interpreter, "MyTaskHandle", new_session_initialized=True)
    expect_get_task_name(interpreter, "MyTask")
    task = Task("MyTask")
    task_handle = task._handle

    with task:
        interpreter.clear_task.assert_not_called()

    interpreter.clear_task.assert_called_with(task_handle)


def test___no_close_on_exit___context_manager___clear_task_not_called(interpreter: Mock):
    expect_create_task(interpreter, "MyTaskHandle", new_session_initialized=False)
    expect_get_task_name(interpreter, "MyTask")
    task = Task("MyTask")

    with task:
        interpreter.clear_task.assert_not_called()

    interpreter.clear_task.assert_not_called()


def test___close_on_exit___leak_task___raises_resource_warning(interpreter: Mock):
    expect_create_task(interpreter, "MyTaskHandle", new_session_initialized=True)
    expect_get_task_name(interpreter, "MyTask")
    task = Task("MyTask")

    with pytest.warns(ResourceWarning, match="Resources on the task device may still be reserved."):
        task.__del__()

    task.close()


def test___close_on_exit_with_grpc_options___leak_task___resource_warning_not_raised(
    interpreter: Mock, mocker: MockerFixture
):
    expect_create_task(interpreter, "GrpcTaskHandle")
    expect_get_task_name(interpreter, "GrpcTask")
    grpc_options = create_grpc_options(mocker)
    task = Task("GrpcTask", grpc_options=grpc_options)

    with warnings.catch_warnings(record=True) as warnings_raised:
        task.__del__()

    assert len(warnings_raised) == 0
    task.close()


def test___close_on_exit_with_alternate_constructor___leak_task___raises_resource_warning(
    interpreter: Mock,
):
    task = _TaskAlternateConstructor("MyTaskHandle", interpreter, close_on_exit=True)

    with pytest.warns(ResourceWarning, match="Resources on the task device may still be reserved."):
        task.__del__()

    task.close()


def test___close_on_exit_with_alternate_constructor_and_grpc_options___leak_task___resource_warning_not_raised(
    interpreter: Mock, mocker: MockerFixture
):
    interpreter._grpc_options = create_grpc_options(mocker)
    task = _TaskAlternateConstructor("MyTaskHandle", interpreter, close_on_exit=True)

    with warnings.catch_warnings(record=True) as warnings_raised:
        task.__del__()

    assert len(warnings_raised) == 0
    task.close()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/unit/test_task_events.py sha256=0f7861263ec9c419170112ed48cd429a8aa87e6ec48482b91cc04d92f2065f0b bytes=3495 -->
## FILE: tests/unit/test_task_events.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/unit/test_task_events.py`
- sha256: `0f7861263ec9c419170112ed48cd429a8aa87e6ec48482b91cc04d92f2065f0b`
- bytes: 3495

````python
from __future__ import annotations

from unittest.mock import Mock

import pytest
from pytest_mock import MockerFixture

from nidaqmx import Task
from nidaqmx.task import _TaskEventType
from tests.unit._grpc_utils import create_grpc_options
from tests.unit._task_utils import (
    expect_create_task,
    expect_get_task_name,
    register_event_handler,
    register_event_handlers,
)


@pytest.mark.parametrize("event_type", _TaskEventType)
def test___grpc_event_registered___leak_task___raises_resource_warning(
    event_type: _TaskEventType, interpreter: Mock, mocker: MockerFixture
):
    expect_create_task(interpreter, "GrpcTaskHandle")
    expect_get_task_name(interpreter, "GrpcTask")
    grpc_options = create_grpc_options(mocker)
    task = Task("GrpcTask", grpc_options=grpc_options)
    register_event_handler(mocker, task, event_type)

    with pytest.warns(ResourceWarning, match="Event handlers may still be active."):
        task.__del__()

    task.close()


def test___events_registered_and_clear_task_error_raised___close___task_resources_cleaned_up_and_clear_task_error_raised(
    interpreter: Mock, mocker: MockerFixture
):
    expect_create_task(interpreter, "MyTaskHandle")
    expect_get_task_name(interpreter, "MyTask")
    task = Task("MyTask")
    event_handlers = register_event_handlers(mocker, task, _TaskEventType)
    interpreter.clear_task.side_effect = RuntimeError("clear_task")

    with pytest.raises(RuntimeError, match="clear_task"):
        task.close()

    _assert_task_resources_cleaned_up(task, interpreter, event_handlers)


@pytest.mark.parametrize("event_type", _TaskEventType)
def test___events_registered_and_close_event_handler_error_raised___close___task_resources_cleaned_up_and_close_event_handler_error_raised(
    event_type: _TaskEventType, interpreter: Mock, mocker: MockerFixture
):
    expect_create_task(interpreter, "MyTaskHandle")
    expect_get_task_name(interpreter, "MyTask")
    task = Task("MyTask")
    event_handlers = register_event_handlers(mocker, task, _TaskEventType)
    event_handlers[event_type].close.side_effect = RuntimeError(str(event_type))

    with pytest.raises(RuntimeError, match=str(event_type)):
        task.close()

    _assert_task_resources_cleaned_up(task, interpreter, event_handlers)


def test___events_registered_and_multiple_errors_raised___close___task_resources_cleaned_up_and_first_error_raised(
    interpreter: Mock, mocker: MockerFixture
):
    expect_create_task(interpreter, "MyTaskHandle")
    expect_get_task_name(interpreter, "MyTask")
    task = Task("MyTask")
    event_handlers = register_event_handlers(mocker, task, _TaskEventType)
    interpreter.clear_task.side_effect = RuntimeError("clear_task")
    for event_type, event_handler in event_handlers.items():
        event_handler.close.side_effect = RuntimeError(str(event_type))

    with pytest.raises(RuntimeError, match="clear_task"):
        task.close()

    _assert_task_resources_cleaned_up(task, interpreter, event_handlers)


def _assert_task_resources_cleaned_up(
    task: Task, interpreter: Mock, event_handlers: dict[_TaskEventType, Mock]
) -> None:
    interpreter.clear_task.assert_called_once_with("MyTaskHandle")
    assert task._handle is None
    for event_type, event_handler in event_handlers.items():
        event_handler.close.assert_called_once_with()
        assert event_type not in task._event_handlers
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tox.ini sha256=c35e4d6850d1ec1e43e8496decea64930eec3db1b18b2e3551da4c637ff26e01 bytes=2050 -->
## FILE: tox.ini

- repository: `ni/nidaqmx-python`
- source_path: `tox.ini`
- sha256: `c35e4d6850d1ec1e43e8496decea64930eec3db1b18b2e3551da4c637ff26e01`
- bytes: 2050

````ini
# Tox (http://tox.testrun.org/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox" from this directory.

[tox]
isolated_build = true
# grpcio does not have binary wheels for pypy or free-threading, as of version 1.75.1.
# nidaqmxbot does not have pypy yet.
# TODO: Get system tests running on Python 3.14t (free-threaded) - https://github.com/ni/nidaqmx-python/issues/853 
envlist = clean, py{39,310,311,312,313,314,314}-base, py{39,310,311,312,313,314}-grpc, py310-base-nicaiu, py310-base-nicai_utf8, py310-base-benchmark, report, docs

[testenv]
skip_install = true
allowlist_externals = poetry
setenv =
   base: INSTALL_OPTS=--only main,test
   grpc: INSTALL_OPTS=--only main,test --extras grpc
   base: PYTEST_OPTS=-k "library"
   grpc: PYTEST_OPTS=
   nicaiu: NIDAQMX_C_LIBRARY=nicaiu
   nicai_utf8: NIDAQMX_C_LIBRARY=nicai_utf8
platform = 
   nicaiu: win32
   nicai_utf8: win32
commands =
   poetry run python -VV
   poetry install -v {env:INSTALL_OPTS}
   poetry run python -c "from nidaqmx._lib import lib_importer; print(f'Library: {lib_importer.windll._library._name}\nLibrary encoding: {lib_importer.encoding}')"
   !benchmark: poetry run pytest --quiet --cov=generated/nidaqmx --cov-append --cov-report= --junitxml=test_results/system-{envname}.xml {env:PYTEST_OPTS} {posargs}
   benchmark: poetry run pytest tests/benchmark/ --quiet --junitxml=test_results/benchmark-{envname}.xml {env:PYTEST_OPTS} {posargs}

[testenv:clean]
commands = poetry run coverage erase

[testenv:report]
commands =
   poetry run coverage html
   poetry run coverage report

[testenv:docs]
# base_python should match the version specified in .readthedocs.yml and the PR workflow.
base_python = python3.11
commands =
   poetry run python -VV
   poetry install -v --only main,docs
   # Use -W to treat warnings as errors.
   poetry run sphinx-build -b html -W docs docs/_build
````
