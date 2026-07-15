# NI OSS SOURCE SNAPSHOT: nimi-python

<!--NI_OSS_SNAPSHOT repo=ni/nimi-python commit=6511f8025f072f7f7021953888b916bbdc31aa2a -->

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/system_tests/test_system_niscope.py sha256=da2aaccc20e0ed47c9876112cd6223ef4d774ffd851359516158447494c127e6 bytes=34463 -->
## FILE: src/niscope/system_tests/test_system_niscope.py

- repository: `ni/nimi-python`
- source_path: `src/niscope/system_tests/test_system_niscope.py`
- sha256: `da2aaccc20e0ed47c9876112cd6223ef4d774ffd851359516158447494c127e6`
- bytes: 34463

````python
import collections
import copy
import os
import pathlib
import sys
import tempfile

import fasteners
import grpc
import hightime
import numpy
import pytest

import niscope

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent / 'shared'))
import system_test_utilities  # noqa: E402


instruments = ['FakeDevice1', 'FakeDevice2']
test_channels_1 = 'FakeDevice2/0,FakeDevice1/1'
test_channels_1_expanded = test_channels_1
test_channels_2 = 'FakeDevice2/0:1'
test_channels_2_expanded = 'FakeDevice2/0,FakeDevice2/1'


# There are system tests below that need either a PXI-5124 or a PXI-5142 instead of the PXIe-5164 we use everywhere else
# because of specific capabilities on those models. Due to internal NI bug 969274, opening a simulated session to those models
# sometimes fails. As a workaround, the nimi-bot VMs are configured with one persistently simulated instrument of each kind respectively
# named "5124" and "5142". If you want to run these tests on your own system, you will need to create these two simulated
# instruments using MAX.
# In addition, we need a global lock in order to keep us from opening more than one session to the same simulated instrument
# at the same time. This is because NI-SCOPE (like other MI driver runtimes) disallow two simultaneous sessions to the same
# instrument, even when the instrument is simulated. This will impact the performance at which system tests run because we
# parallelize at the tox level :(.
daqmx_sim_5124_lock_file = os.path.join(tempfile.gettempdir(), 'daqmx_5124.lock')
daqmx_sim_5124_lock = fasteners.InterProcessLock(daqmx_sim_5124_lock_file)
daqmx_sim_5142_lock_file = os.path.join(tempfile.gettempdir(), 'daqmx_5142.lock')
daqmx_sim_5142_lock = fasteners.InterProcessLock(daqmx_sim_5142_lock_file)


def check_fetched_data(
    data,  # either waveforms or measurement_stats
    test_channels_expanded,
    test_record_length,
    test_num_records_to_fetch,
    test_starting_record_number=0
):
    test_num_channels = len(test_channels_expanded.split(','))

    # Ordering: rec 0: ch 0, rec 0: ch 1, rec 1: ch 0, rec 1: ch 1, etc.
    expected_channels = test_channels_expanded.split(',') * test_num_records_to_fetch
    expected_records = []
    for i in range(test_starting_record_number, test_starting_record_number + test_num_records_to_fetch):
        expected_records += [i] * test_num_channels

    assert len(data) == test_num_channels * test_num_records_to_fetch
    for i in range(len(data)):
        if isinstance(data[i], niscope.WaveformInfo):
            assert len(data[i].samples) == test_record_length
        elif isinstance(data[i], niscope.MeasurementStats):
            assert data[i].result == 0.0
        else:
            raise TypeError(f"data is unsupported type {type(data[i])}")
        assert data[i].channel == expected_channels[i]
        assert data[i].record == expected_records[i]


class SystemTests:
    @pytest.fixture(scope='function')
    def single_instrument_session(self, session_creation_kwargs):
        with niscope.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe', **session_creation_kwargs) as simulated_session:
            yield simulated_session

    @pytest.fixture(scope='function')
    def single_instrument_session_5171(self, session_creation_kwargs):  # High channel-count session for get_channel_names testing
        with niscope.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:5171R (8CH); BoardType:PXIe', **session_creation_kwargs) as simulated_session:
            yield simulated_session

    @pytest.fixture(scope='function')
    def multi_instrument_session(self, session_creation_kwargs):
        with niscope.Session(','.join(instruments), False, True, 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe', **session_creation_kwargs) as simulated_session:
            yield simulated_session

    @pytest.fixture(scope='function')
    def multi_instrument_session_5171(self, session_creation_kwargs):  # High channel-count session for get_channel_names testing
        with niscope.Session(','.join(instruments), False, True, 'Simulate=1, DriverSetup=Model:5171R (8CH); BoardType:PXIe', **session_creation_kwargs) as simulated_session:
            yield simulated_session

    @pytest.fixture(scope='function')
    def session_5124(self, session_creation_kwargs):
        with daqmx_sim_5124_lock:
            with niscope.Session('5124', False, False, '', **session_creation_kwargs) as simulated_session:  # 5124 is needed for video triggering
                yield simulated_session

    @pytest.fixture(scope='function')
    def session_5142(self, session_creation_kwargs):
        with daqmx_sim_5142_lock:
            with niscope.Session('5142', False, False, '', **session_creation_kwargs) as simulated_session:  # 5142 is needed for OSP
                yield simulated_session

    # Attribute tests
    def test_vi_boolean_attribute(self, multi_instrument_session):
        multi_instrument_session.allow_more_records_than_memory = False
        default_option = multi_instrument_session.allow_more_records_than_memory
        assert default_option is False

    def test_vi_string_attribute(self, multi_instrument_session):
        trigger_source = f'/{instruments[1]}/NISCOPE_VAL_IMMEDIATE'
        multi_instrument_session.acq_arm_source = trigger_source
        assert trigger_source == multi_instrument_session.acq_arm_source

    # Basic usability tests
    def test_get_channel_names_with_single_instrument_session(self, single_instrument_session_5171):
        expected_string = [f'{x}' for x in range(8)]
        # Sanity test few different types of input. No need for test to be exhaustive
        # since all the various types are covered by converter unit tests.
        channel_indices = ['0-1, 2, 3:4', 5, range(6, 7), slice(7, 8)]
        assert single_instrument_session_5171.get_channel_names(indices=channel_indices) == expected_string

    def test_get_channel_names_with_multi_instrument_session(self, multi_instrument_session_5171):
        expected_string = [f'{instruments[0]}/{x}' for x in range(8)] + [f'{instruments[1]}/{x}' for x in range(4)]
        # Sanity test few different types of input. No need for test to be exhaustive
        # since all the various types are covered by converter unit tests.
        channel_indices = ['0-1, 2, 3:4', 5, (6, 7), range(8, 10), slice(10, 12)]
        assert multi_instrument_session_5171.get_channel_names(indices=channel_indices) == expected_string

    @pytest.mark.parametrize(
        "test_channels,test_channels_expanded",
        [
            (test_channels_1, test_channels_1_expanded),
            (test_channels_2, test_channels_2_expanded),
        ],
    )
    def test_read(self, multi_instrument_session, test_channels, test_channels_expanded):
        test_voltage = 1.0
        test_record_length = 2000
        test_num_records = 3
        multi_instrument_session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
        multi_instrument_session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records, True)
        waveforms = multi_instrument_session.channels[test_channels].read(num_samples=test_record_length, num_records=test_num_records)
        check_fetched_data(waveforms, test_channels_expanded, test_record_length, test_num_records)

    @pytest.mark.parametrize(
        "test_channels,test_channels_expanded",
        [
            (test_channels_1, test_channels_1_expanded),
            (test_channels_2, test_channels_2_expanded),
        ],
    )
    def test_fetch(self, multi_instrument_session, test_channels, test_channels_expanded):
        test_voltage = 1.0
        test_record_length = 2000
        test_starting_record_number = 2
        test_num_records_to_acquire = 5
        test_num_records_to_fetch = test_num_records_to_acquire - test_starting_record_number
        multi_instrument_session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
        multi_instrument_session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records_to_acquire, True)
        with multi_instrument_session.initiate():
            waveforms = multi_instrument_session.channels[test_channels].fetch(
                num_samples=test_record_length,
                record_number=test_starting_record_number,
                num_records=test_num_records_to_fetch)
        check_fetched_data(
            waveforms,
            test_channels_expanded,
            test_record_length,
            test_num_records_to_fetch,
            test_starting_record_number,
        )

    def test_fetch_defaults(self, multi_instrument_session):
        test_voltage = 1.0
        test_record_length = 2000
        test_num_channels = 2
        multi_instrument_session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
        multi_instrument_session.configure_horizontal_timing(50000000, test_record_length, 50.0, 1, True)
        with multi_instrument_session.initiate():
            waveforms = multi_instrument_session.channels[test_channels_1].fetch()
        assert len(waveforms) == test_num_channels
        for i in range(len(waveforms)):
            assert len(waveforms[i].samples) == test_record_length

    @pytest.fixture(params=[(1000, 1000), (2000, 2000), (3000, 2000)], ids=["less_than_actual", "equal_to_actual", "greater_than_actual"])
    def measurement_wfm_length(self, request):
        MeasWfmLength = collections.namedtuple('MeasurementWaveformLength', ['passed_in', 'expected'])
        return MeasWfmLength(passed_in=request.param[0], expected=request.param[1])

    @pytest.mark.parametrize(
        "test_channels,test_channels_expanded",
        [
            (test_channels_1, test_channels_1_expanded),
            (test_channels_2, test_channels_2_expanded),
        ],
    )
    def test_fetch_array_measurement(
        self,
        multi_instrument_session,
        measurement_wfm_length,
        test_channels,
        test_channels_expanded,
    ):
        test_voltage = 1.0
        test_record_length = 1000
        test_meas_wfm_length = measurement_wfm_length.passed_in
        test_array_meas_function = niscope.ArrayMeasurement.ARRAY_GAIN
        test_starting_record_number = 2
        test_num_records_to_acquire = 5
        test_num_records_to_fetch = test_num_records_to_acquire - test_starting_record_number
        multi_instrument_session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
        multi_instrument_session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records_to_acquire, True)

        with multi_instrument_session.initiate():
            waveforms = multi_instrument_session.channels[test_channels].fetch_array_measurement(
                array_meas_function=test_array_meas_function,
                meas_wfm_size=test_meas_wfm_length,
                relative_to=niscope.FetchRelativeTo.PRETRIGGER,
                offset=5,
                record_number=test_starting_record_number,
                num_records=test_num_records_to_fetch,
                meas_num_samples=2000,
                timeout=hightime.timedelta(seconds=4))

        check_fetched_data(
            waveforms,
            test_channels_expanded,
            measurement_wfm_length.expected,
            test_num_records_to_fetch,
            test_starting_record_number,
        )

    def test_fetch_array_measurement_defaults(self, multi_instrument_session):
        test_voltage = 1.0
        test_record_length = 1000
        test_num_channels = 2
        test_num_records = 3
        test_array_meas_function = niscope.ArrayMeasurement.ARRAY_GAIN

        multi_instrument_session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
        multi_instrument_session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records, True)

        with multi_instrument_session.initiate():
            waveforms = multi_instrument_session.channels[test_channels_1].fetch_array_measurement(
                array_meas_function=test_array_meas_function)

        assert len(waveforms) == test_num_channels * test_num_records
        for i in range(len(waveforms)):
            assert len(waveforms[i].samples) == test_record_length

    @pytest.mark.parametrize(
        "test_channels,test_channels_expanded",
        [
            (test_channels_1, test_channels_1_expanded),
            (test_channels_2, test_channels_2_expanded),
        ],
    )
    def test_fetch_measurement_stats(
        self,
        multi_instrument_session,
        test_channels,
        test_channels_expanded,
    ):
        test_voltage = 1.0
        test_record_length = 1000
        test_starting_record_number = 2
        test_num_records_to_acquire = 5
        test_num_records_to_fetch = test_num_records_to_acquire - test_starting_record_number
        multi_instrument_session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
        multi_instrument_session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records_to_acquire, True)
        with multi_instrument_session.initiate():
            measurement_stats = multi_instrument_session.channels[test_channels].fetch_measurement_stats(
                scalar_meas_function=niscope.enums.ScalarMeasurement.NO_MEASUREMENT,
                relative_to=niscope.FetchRelativeTo.PRETRIGGER,
                offset=5,
                record_number=test_starting_record_number,
                num_records=test_num_records_to_fetch,
                timeout=hightime.timedelta(seconds=4))

        check_fetched_data(
            measurement_stats,
            test_channels_expanded,
            None,  # pass None for test_record_length, because we shouldn't need it
            test_num_records_to_fetch,
            test_starting_record_number
        )

    def test_fetch_measurement_stats_defaults(self, multi_instrument_session):
        test_voltage = 1.0
        test_record_length = 1000
        test_num_channels = 2
        test_num_records = 3
        multi_instrument_session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
        multi_instrument_session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records, True)
        with multi_instrument_session.initiate():
            measurement_stats = multi_instrument_session.channels[test_channels_1].fetch_measurement_stats(niscope.enums.ScalarMeasurement.NO_MEASUREMENT)

        assert len(measurement_stats) == test_num_channels * test_num_records
        for stat in measurement_stats:
            assert stat.result == 0.0

    def test_clear_waveform_measurement_stats(self, multi_instrument_session):
        test_voltage = 1.0
        test_record_length = 1000
        test_num_records = 1
        multi_instrument_session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
        multi_instrument_session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records, True)
        with multi_instrument_session.initiate():
            uncleared_stats = multi_instrument_session.channels[test_channels_1].fetch_measurement_stats(niscope.enums.ScalarMeasurement.FREQUENCY)
            uncleared_stats_2 = multi_instrument_session.channels[test_channels_1].fetch_measurement_stats(niscope.enums.ScalarMeasurement.FREQUENCY)
            multi_instrument_session.channels[test_channels_1].clear_waveform_measurement_stats(niscope.enums.ClearableMeasurement.FREQUENCY)
            cleared_stats = multi_instrument_session.channels[test_channels_1].fetch_measurement_stats(niscope.enums.ScalarMeasurement.FREQUENCY)

        # The principle here is using consistent behavior (i.e. if stats are fetched twice on a single record/channel measurement in a row, it will always be the same)
        # to demonstrate that clearing the stats does in fact cause a measurable change.
        assert uncleared_stats[0].result == uncleared_stats_2[0].result
        assert uncleared_stats[0].stdev == uncleared_stats_2[0].stdev
        assert uncleared_stats[0].mean == uncleared_stats_2[0].mean
        assert uncleared_stats[0].min_val == uncleared_stats_2[0].min_val
        assert uncleared_stats[0].max_val == uncleared_stats_2[0].max_val
        assert uncleared_stats[0].num_in_stats == uncleared_stats_2[0].num_in_stats
        assert uncleared_stats[0].num_in_stats != cleared_stats[0].num_in_stats

    def test_waveform_processing(self, multi_instrument_session):
        test_voltage = 1.0
        test_record_length = 1000
        test_num_channels = 2
        test_num_records = 3
        multi_instrument_session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
        multi_instrument_session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records, True)
        with multi_instrument_session.initiate():
            multi_instrument_session.add_waveform_processing(niscope.enums.ArrayMeasurement.DERIVATIVE)
            processed_waveforms = multi_instrument_session.channels[test_channels_1].fetch_measurement_stats(niscope.enums.ScalarMeasurement.MID_REF_VOLTS)
            multi_instrument_session.clear_waveform_processing()
            unprocessed_waveforms = multi_instrument_session.channels[test_channels_1].fetch_measurement_stats(niscope.enums.ScalarMeasurement.MID_REF_VOLTS)

        assert len(processed_waveforms) == test_num_channels * test_num_records
        assert len(unprocessed_waveforms) == test_num_channels * test_num_records
        # Here the idea is to leave a large margin to not test too specifically for any returned values but to demonstrate that the waveform processing does
        # undeniably cause a consistent shift in the values returned. The "0" exception for processed is due to the nature of derivatives -- if two samples
        # next to each other are identical, the derivative will be 0.
        for processed, unprocessed in zip(processed_waveforms, unprocessed_waveforms):
            assert abs(unprocessed.result) < 1
            assert abs(processed.result) > 1 or processed.result == 0

    def test_measurement_stats_str(self, multi_instrument_session):
        test_voltage = 1.0
        test_record_length = 1000
        test_num_records = 1
        multi_instrument_session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
        multi_instrument_session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records, True)
        with multi_instrument_session.initiate():
            measurement_stat = multi_instrument_session.channels[test_channels_1].fetch_measurement_stats(niscope.enums.ScalarMeasurement.NO_MEASUREMENT)

        assert isinstance(measurement_stat[0].__str__(), str)
        assert isinstance(measurement_stat[0].__repr__(), str)

    def test_self_test(self, multi_instrument_session):
        # We should not get an assert if self_test passes
        multi_instrument_session.self_test()

    def test_reset(self, multi_instrument_session):
        default_fetch_relative_to = multi_instrument_session._fetch_relative_to
        assert default_fetch_relative_to == niscope.FetchRelativeTo.PRETRIGGER
        multi_instrument_session._fetch_relative_to = niscope.FetchRelativeTo.READ_POINTER
        non_default_acqusition_type = multi_instrument_session._fetch_relative_to
        assert non_default_acqusition_type == niscope.FetchRelativeTo.READ_POINTER
        multi_instrument_session.reset()
        assert multi_instrument_session._fetch_relative_to == niscope.FetchRelativeTo.PRETRIGGER

    def test_reset_device(self, multi_instrument_session):
        default_meas_time_histogram_high_time = multi_instrument_session.meas_time_histogram_high_time
        assert default_meas_time_histogram_high_time == hightime.timedelta(microseconds=500)
        multi_instrument_session.meas_time_histogram_high_time = hightime.timedelta(microseconds=1000)
        non_default_meas_time_histogram_high_time = multi_instrument_session.meas_time_histogram_high_time
        assert non_default_meas_time_histogram_high_time == hightime.timedelta(microseconds=1000)
        multi_instrument_session.reset_device()
        assert multi_instrument_session.meas_time_histogram_high_time == hightime.timedelta(microseconds=500)

    def test_error_message(self, session_creation_kwargs):
        try:
            # We pass in an invalid model name to force going to error_message
            with niscope.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:invalid_model; BoardType:PXIe', **session_creation_kwargs):
                assert False
        except niscope.Error as e:
            assert e.code == -1074118609
            assert e.description.find('Simulation does not support the selected model and board type.') != -1

    def test_get_error(self, multi_instrument_session):
        try:
            multi_instrument_session.instrument_model = ''
            assert False
        except niscope.Error as e:
            assert e.code == -1074135027  # Error : Attribute is read-only.
            assert e.description.find('Attribute is read-only.') != -1

    def test_acquisition_status(self, multi_instrument_session):
        assert multi_instrument_session.acquisition_status() == niscope.AcquisitionStatus.COMPLETE

    def test_self_cal(self, multi_instrument_session):
        multi_instrument_session.self_cal(niscope.Option.SELF_CALIBRATE_ALL_CHANNELS)

    def test_get_self_cal_last_date_time(self, single_instrument_session):
        last_cal = single_instrument_session.get_self_cal_last_date_and_time()
        assert last_cal.month == 12
        assert last_cal.day == 21
        assert last_cal.year == 1999
        assert last_cal.hour == 0
        assert last_cal.minute == 0

    def test_get_ext_cal_last_date_time(self, single_instrument_session):
        last_cal = single_instrument_session.get_ext_cal_last_date_and_time()
        assert last_cal.month == 12
        assert last_cal.day == 21
        assert last_cal.year == 1999
        assert last_cal.hour == 0
        assert last_cal.minute == 0

    def test_get_self_cal_last_temperature(self, single_instrument_session):
        last_cal_temp = single_instrument_session.get_self_cal_last_temp()
        assert last_cal_temp == 25

    def test_get_ext_cal_last_temperature(self, single_instrument_session):
        last_cal_temp = single_instrument_session.get_ext_cal_last_temp()
        assert last_cal_temp == 25

    def test_probe_compensation_signal(self, multi_instrument_session):
        multi_instrument_session.probe_compensation_signal_start()
        multi_instrument_session.probe_compensation_signal_stop()

    def test_configure_horizontal_timing(self, multi_instrument_session):
        multi_instrument_session.configure_vertical(5.0, niscope.VerticalCoupling.DC)
        multi_instrument_session.auto_setup()
        multi_instrument_session.configure_horizontal_timing(10000000, 1000, 50.0, 1, True)
        multi_instrument_session.trigger_modifier = niscope.TriggerModifier.AUTO
        multi_instrument_session.configure_trigger_immediate()
        multi_instrument_session.horz_record_length == 1000
        multi_instrument_session.horz_sample_rate == 10000000

    def test_configure_chan_characteristics(self, multi_instrument_session):
        multi_instrument_session.vertical_range = 4.0
        multi_instrument_session.configure_chan_characteristics(50, 0)
        assert 50.0 == multi_instrument_session.input_impedance

    def test_filter_coefficients(self, session_5142):
        assert [1.0] + [0.0] * 34 == session_5142.get_equalization_filter_coefficients()  # coefficients list should have 35 items
        try:
            filter_coefficients = [1.0, 0.0, 0.0]
            session_5142.configure_equalization_filter_coefficients(filter_coefficients)
        except niscope.Error as e:
            assert "Incorrect number of filter coefficients." in e.description
            assert e.code == -1074135024
        filter_coefficients = [0.01] * 35
        session_5142.configure_equalization_filter_coefficients(filter_coefficients)
        assert filter_coefficients == session_5142.get_equalization_filter_coefficients()

    def test_send_software_trigger_edge(self, multi_instrument_session):
        multi_instrument_session.send_software_trigger_edge(niscope.WhichTrigger.ARM_REFERENCE)

    def test_disable(self, multi_instrument_session):
        assert multi_instrument_session.allow_more_records_than_memory is False
        multi_instrument_session.allow_more_records_than_memory = True
        multi_instrument_session.disable()
        assert multi_instrument_session.allow_more_records_than_memory is False

    # Basic configuration tests
    def test_configure_trigger_digital(self, multi_instrument_session):
        trigger_source = f'/{instruments[1]}/VAL_RTSI_0'
        multi_instrument_session.configure_trigger_digital(trigger_source)
        multi_instrument_session.vertical_range = 5
        assert trigger_source == multi_instrument_session.trigger_source

    def test_configure_trigger_edge(self, multi_instrument_session):
        assert niscope.TriggerSlope.POSITIVE == multi_instrument_session.trigger_slope
        trigger_source = f'{instruments[1]}/0'
        multi_instrument_session.configure_trigger_edge(trigger_source, 0.0, niscope.TriggerCoupling.DC)
        multi_instrument_session.commit()
        assert trigger_source == multi_instrument_session.trigger_source
        assert niscope.TriggerCoupling.DC == multi_instrument_session.trigger_coupling

    def test_configure_trigger_hysteresis(self, multi_instrument_session):
        trigger_source = f'{instruments[1]}/1'
        multi_instrument_session.configure_trigger_hysteresis(trigger_source, 0.0, 0.05, niscope.TriggerCoupling.DC)
        assert trigger_source == multi_instrument_session.trigger_source
        assert niscope.TriggerCoupling.DC == multi_instrument_session.trigger_coupling

    def test_import_export_buffer(self, multi_instrument_session):
        test_value_1 = 1
        test_value_2 = 5
        multi_instrument_session.vertical_range = test_value_1
        assert multi_instrument_session.vertical_range == test_value_1
        buffer = multi_instrument_session.export_attribute_configuration_buffer()
        multi_instrument_session.vertical_range = test_value_2
        assert multi_instrument_session.vertical_range == test_value_2
        multi_instrument_session.import_attribute_configuration_buffer(buffer)
        assert multi_instrument_session.vertical_range == test_value_1

    def test_import_export_file(self, multi_instrument_session):
        test_value_1 = 1
        test_value_2 = 5
        temp_file = tempfile.NamedTemporaryFile(suffix='.txt', delete=False)
        # NamedTemporaryFile() returns the file already opened, so we need to close it before we can use it
        temp_file.close()
        path = temp_file.name
        multi_instrument_session.vertical_range = test_value_1
        assert multi_instrument_session.vertical_range == test_value_1
        multi_instrument_session.export_attribute_configuration_file(path)
        multi_instrument_session.vertical_range = test_value_2
        assert multi_instrument_session.vertical_range == test_value_2
        multi_instrument_session.import_attribute_configuration_file(path)
        assert multi_instrument_session.vertical_range == test_value_1
        os.remove(path)

    def test_configure_trigger_software(self, multi_instrument_session):
        multi_instrument_session.configure_trigger_software()

    def test_configure_trigger_video(self, session_5124):
        session_5124.configure_trigger_video('0', niscope.VideoSignalFormat.PAL, niscope.VideoTriggerEvent.FIELD1, niscope.VideoPolarity.POSITIVE, niscope.TriggerCoupling.DC)
        assert niscope.VideoSignalFormat.PAL == session_5124.tv_trigger_signal_format
        assert niscope.VideoTriggerEvent.FIELD1 == session_5124.tv_trigger_event
        assert niscope.VideoPolarity.POSITIVE == session_5124.tv_trigger_polarity
        assert niscope.TriggerCoupling.DC == session_5124.trigger_coupling

    def test_configure_trigger_window(self, multi_instrument_session):
        trigger_source = f'{instruments[1]}/1'
        multi_instrument_session.configure_trigger_window(trigger_source, 0, 5, niscope.TriggerWindowMode.ENTERING, niscope.TriggerCoupling.DC)
        assert trigger_source == multi_instrument_session.trigger_source
        assert niscope.TriggerWindowMode.ENTERING == multi_instrument_session.trigger_window_mode

    # Multi-Threading tests
    def test_multi_threading_lock_unlock(self, multi_instrument_session):
        system_test_utilities.impl_test_multi_threading_lock_unlock(multi_instrument_session)

    def test_multi_threading_ivi_synchronized_wrapper_releases_lock(self, multi_instrument_session):
        system_test_utilities.impl_test_multi_threading_ivi_synchronized_wrapper_releases_lock(
            multi_instrument_session.abort)


class TestLibrary(SystemTests):
    @pytest.fixture(scope='class')
    def session_creation_kwargs(self):
        return {}

    # not supported by grpc due to numpy usage
    @pytest.mark.parametrize(
        "fetch_waveform_type,type_min_value,test_channels,test_channels_expanded",
        [
            (numpy.int8, numpy.iinfo(numpy.int8).min, test_channels_1, test_channels_1_expanded),
            (numpy.int16, numpy.iinfo(numpy.int16).min, test_channels_1, test_channels_1_expanded),
            (numpy.int32, numpy.iinfo(numpy.int32).min, test_channels_1, test_channels_1_expanded),
            (numpy.float64, numpy.finfo(numpy.float64).min, test_channels_1, test_channels_1_expanded),
            (numpy.int8, numpy.iinfo(numpy.int8).min, test_channels_2, test_channels_2_expanded),
            (numpy.int16, numpy.iinfo(numpy.int16).min, test_channels_2, test_channels_2_expanded),
            (numpy.int32, numpy.iinfo(numpy.int32).min, test_channels_2, test_channels_2_expanded),
            (numpy.float64, numpy.finfo(numpy.float64).min, test_channels_2, test_channels_2_expanded),
        ],
    )
    def test_fetch_into(
        self,
        multi_instrument_session,
        fetch_waveform_type,
        type_min_value,
        test_channels,
        test_channels_expanded,
    ):
        test_voltage = 1.0
        test_record_length = 2000
        test_num_channels = len(test_channels_expanded.split(','))
        test_starting_record_number = 2
        test_num_records_to_acquire = 5
        test_num_records_to_fetch = test_num_records_to_acquire - test_starting_record_number
        init_waveform = numpy.ndarray(test_num_channels * test_num_records_to_fetch * test_record_length, dtype=fetch_waveform_type)
        # Initialize with min supported value so we can later verify all samples were overwritten by the driver.
        init_waveform.fill(type_min_value)
        waveform = copy.deepcopy(init_waveform)
        multi_instrument_session.configure_vertical(test_voltage, niscope.VerticalCoupling.AC)
        multi_instrument_session.configure_horizontal_timing(50000000, test_record_length, 50.0, test_num_records_to_acquire, True)
        with multi_instrument_session.initiate():
            waveforms = multi_instrument_session.channels[test_channels].fetch_into(
                waveform=waveform,
                record_number=test_starting_record_number,
                num_records=test_num_records_to_fetch)

        for index, sample in enumerate(waveform):
            assert sample != init_waveform[index]

        check_fetched_data(
            waveforms,
            test_channels_expanded,
            test_record_length,
            test_num_records_to_fetch,
            test_starting_record_number,
        )
        for i in range(len(waveforms)):
            record_wfm = waveforms[i].samples
            for j in range(len(record_wfm)):
                assert record_wfm[j] == waveform[i * test_record_length + j]

    def test_configure_ref_levels(self, single_instrument_session):
        single_instrument_session._configure_ref_levels()
        assert 90.0 == single_instrument_session.meas_chan_high_ref_level

    def test_reset_with_defaults(self, single_instrument_session):
        default_meas_time_histogram_high_time = single_instrument_session.meas_time_histogram_high_time
        assert default_meas_time_histogram_high_time == hightime.timedelta(microseconds=500)
        single_instrument_session.meas_time_histogram_high_time = hightime.timedelta(microseconds=1000)
        non_default_meas_time_histogram_high_time = single_instrument_session.meas_time_histogram_high_time
        assert non_default_meas_time_histogram_high_time == hightime.timedelta(microseconds=1000)
        single_instrument_session.reset_with_defaults()
        assert single_instrument_session.meas_time_histogram_high_time == hightime.timedelta(microseconds=500)


class TestGrpc(SystemTests):
    @pytest.fixture(scope='class')
    def grpc_channel(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(current_directory, 'grpc_server_config.json')
        with system_test_utilities.GrpcServerProcess(config_file_path) as proc:
            channel = grpc.insecure_channel(f"localhost:{proc.server_port}")
            yield channel

    @pytest.fixture(scope='class')
    def session_creation_kwargs(self, grpc_channel):
        grpc_options = niscope.GrpcSessionOptions(grpc_channel, "")
        return {'grpc_options': grpc_options}

    def test_configure_ref_levels(self, single_instrument_session):
        with pytest.raises(NotImplementedError) as exc_info:
            single_instrument_session._configure_ref_levels()
        assert exc_info.value.args[0] == 'configure_ref_levels is not supported over gRPC'
        assert str(exc_info.value) == 'configure_ref_levels is not supported over gRPC'

    def test_reset_with_defaults(self, single_instrument_session):
        with pytest.raises(NotImplementedError) as exc_info:
            single_instrument_session.reset_with_defaults()
        assert exc_info.value.args[0] == 'reset_with_defaults is not supported over gRPC'
        assert str(exc_info.value) == 'reset_with_defaults is not supported over gRPC'
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/templates/session.py/fancy_fetch.py.mako sha256=2c5bd171cf5f55a51b4444b9081d5e6cdb43015c1bd7e27697efcfeffaa819dc bytes=1182 -->
## FILE: src/niscope/templates/session.py/fancy_fetch.py.mako

- repository: `ni/nimi-python`
- source_path: `src/niscope/templates/session.py/fancy_fetch.py.mako`
- sha256: `2c5bd171cf5f55a51b4444b9081d5e6cdb43015c1bd7e27697efcfeffaa819dc`
- bytes: 1182

````mako
<%page args="f, config, method_template"/>\
<%
    '''Forwards to _fetch()/_read() with a nicer interface'''
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        # Set the fetch attributes
        with _NoChannel(session=self):
            self._fetch_relative_to = relative_to
            self._fetch_offset = offset
            self._fetch_record_number = record_number
            self._fetch_num_records = -1 if num_records is None else num_records
            if num_samples is None:
                num_samples = self.horz_record_length

        wfm, wfm_info = self._${f['python_name']}(num_samples, timeout)

        if isinstance(wfm, array.ArrayType):
            mv = memoryview(wfm)
        else:
            mv = wfm

        waveform_info._populate_samples_info(wfm_info, mv, num_samples)

<%include file="./fetch_waveform_info_population.py.mako"/>

        return wfm_info
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/templates/session.py/fancy_fetch_array_measurement.py.mako sha256=186e9c270339635116a5451c9d408a35e88d62eb9b6020dad2d1fddb3f84d6f4 bytes=1487 -->
## FILE: src/niscope/templates/session.py/fancy_fetch_array_measurement.py.mako

- repository: `ni/nimi-python`
- source_path: `src/niscope/templates/session.py/fancy_fetch_array_measurement.py.mako`
- sha256: `186e9c270339635116a5451c9d408a35e88d62eb9b6020dad2d1fddb3f84d6f4`
- bytes: 1487

````mako
<%page args="f, config, method_template"/>\
<%
    '''Forwards to _fetch_array_measurement with cleaner return values.'''
    import build.helper as helper
    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        r'''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        # Set the fetch attributes
        with _NoChannel(session=self):
            self._fetch_relative_to = relative_to
            self._fetch_offset = offset
            self._fetch_record_number = record_number
            self._fetch_num_records = -1 if num_records is None else num_records
            self._fetch_meas_num_samples = -1 if meas_num_samples is None else meas_num_samples

        # For GrpcStubInterpreter, the server will automatically get _actual_meas_wfm_size, if needed.
        if isinstance(self._interpreter, _library_interpreter.LibraryInterpreter):
            if meas_wfm_size is None:
                meas_wfm_size = self._actual_meas_wfm_size(array_meas_function)

        meas_wfm, wfm_info = self._${f['python_name']}(array_meas_function, meas_wfm_size, timeout)

        record_length = int(len(meas_wfm) / len(wfm_info))
        waveform_info._populate_samples_info(wfm_info, meas_wfm, record_length)

<%include file="./fetch_waveform_info_population.py.mako"/>

        return wfm_info
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/templates/session.py/fancy_fetch_measurement_stats.py.mako sha256=847252f419f8ea019c4d741a8013b9e4b550f448dcabf08d2bdeaebec99744d5 bytes=1358 -->
## FILE: src/niscope/templates/session.py/fancy_fetch_measurement_stats.py.mako

- repository: `ni/nimi-python`
- source_path: `src/niscope/templates/session.py/fancy_fetch_measurement_stats.py.mako`
- sha256: `847252f419f8ea019c4d741a8013b9e4b550f448dcabf08d2bdeaebec99744d5`
- bytes: 1358

````mako
<%page args="f, config, method_template"/>\
<%
    '''Forwards to _fetch_measurement_stats with cleaner return values.'''
    import build.helper as helper
    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        r'''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        # Set the fetch attributes
        with _NoChannel(session=self):
            self._fetch_relative_to = relative_to
            self._fetch_offset = offset
            self._fetch_record_number = record_number
            self._fetch_num_records = -1 if num_records is None else num_records

        results, means, stdevs, min_vals, max_vals, nums_in_stats = self._${f['python_name']}(scalar_meas_function, timeout)

        output = []
        for result, mean, stdev, min_val, max_val, num_in_stats in zip(results, means, stdevs, min_vals, max_vals, nums_in_stats):
            measurement_stat = measurement_stats.MeasurementStats(result, mean, stdev, min_val, max_val, num_in_stats)
            output.append(measurement_stat)

<%include file="./fetch_waveform_info_population.py.mako" args="results_name='results', results_description='results', output_name='output'"/>

        return output
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/templates/session.py/fancy_get_cal_last_date.py.mako sha256=fb213eed0d9242b7e71507d22977df77c8f9a65bf98ac2d9ae9a121e97e84f82 bytes=735 -->
## FILE: src/niscope/templates/session.py/fancy_get_cal_last_date.py.mako

- repository: `ni/nimi-python`
- source_path: `src/niscope/templates/session.py/fancy_get_cal_last_date.py.mako`
- sha256: `fb213eed0d9242b7e71507d22977df77c8f9a65bf98ac2d9ae9a121e97e84f82`
- bytes: 735

````mako
<%page args="f, config, method_template"/>\
<%
    '''Forwards to _cal_fetch_date, with calibration type pre-selected.'''
    import build.helper as helper
    if f['python_name'] == "get_self_cal_last_date_and_time":
        calibration_type = "SELF"
    else: #f['python_name'] == "get_ext_cal_last_date_and_time"
        calibration_type = "EXTERNAL"
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''

        year, month, day = self._cal_fetch_date(enums._CalibrationTypes.${calibration_type})
        return hightime.datetime(year, month, day)
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/templates/session.py/fancy_get_cal_last_temp.py.mako sha256=33a6e5ee181987551e9a56b840101c2dc5baaffd85a15e4a5abc76ed8ecb0c44 bytes=668 -->
## FILE: src/niscope/templates/session.py/fancy_get_cal_last_temp.py.mako

- repository: `ni/nimi-python`
- source_path: `src/niscope/templates/session.py/fancy_get_cal_last_temp.py.mako`
- sha256: `33a6e5ee181987551e9a56b840101c2dc5baaffd85a15e4a5abc76ed8ecb0c44`
- bytes: 668

````mako
<%page args="f, config, method_template"/>\
<%
    '''Forwards to _cal_fetch_temp, with calibration type pre-selected.'''
    import build.helper as helper
    if f['python_name'] == "get_self_cal_last_temp":
        calibration_type = "SELF"
    else: # f['python_name'] == "get_ext_cal_last_temp"
        calibration_type = "EXTERNAL"
%>\
    def ${f['python_name']}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''

        return self._cal_fetch_temperature(enums._CalibrationTypes.${calibration_type}.value)
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/templates/session.py/fetch_waveform.py.mako sha256=353984e829542ae6b62115330e6dcf4da34dda634324266ac0ab3be11d73ff31 bytes=1880 -->
## FILE: src/niscope/templates/session.py/fetch_waveform.py.mako

- repository: `ni/nimi-python`
- source_path: `src/niscope/templates/session.py/fetch_waveform.py.mako`
- sha256: `353984e829542ae6b62115330e6dcf4da34dda634324266ac0ab3be11d73ff31`
- bytes: 1880

````mako
<%page args="f, config, method_template"/>\
<%
    '''Dispatches to the appropriate "fetch waveform into" method based on the waveform type.'''
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_NUMPY_INTO_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        import numpy

        # Set the fetch attributes
        with _NoChannel(session=self):
            self._fetch_relative_to = relative_to
            self._fetch_offset = offset
            self._fetch_record_number = record_number
            self._fetch_num_records = -1 if num_records is None else num_records

        num_samples = int(len(waveform) / self._actual_num_wfms())

        if waveform.dtype == numpy.float64:
            wfm_info = self._fetch_into_numpy(num_samples=num_samples, waveform=waveform, timeout=timeout)
        elif waveform.dtype == numpy.int8:
            wfm_info = self._fetch_binary8_into_numpy(num_samples=num_samples, waveform=waveform, timeout=timeout)
        elif waveform.dtype == numpy.int16:
            wfm_info = self._fetch_binary16_into_numpy(num_samples=num_samples, waveform=waveform, timeout=timeout)
        elif waveform.dtype == numpy.int32:
            wfm_info = self._fetch_binary32_into_numpy(num_samples=num_samples, waveform=waveform, timeout=timeout)
        else:
            raise TypeError("Unsupported dtype. Is {}, expected {}, {}, {}, or {}".format(waveform.dtype, numpy.float64, numpy.int8, numpy.int16, numpy.int32))

        mv = memoryview(waveform)

        waveform_info._populate_samples_info(wfm_info, mv, num_samples)

<%include file="./fetch_waveform_info_population.py.mako"/>

        return wfm_info
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/templates/session.py/fetch_waveform_info_population.py.mako sha256=cc78d436d7f79151b14765eac9be7aaa384f8b1e6c86f0599c27f7420dfabef0 bytes=986 -->
## FILE: src/niscope/templates/session.py/fetch_waveform_info_population.py.mako

- repository: `ni/nimi-python`
- source_path: `src/niscope/templates/session.py/fetch_waveform_info_population.py.mako`
- sha256: `cc78d436d7f79151b14765eac9be7aaa384f8b1e6c86f0599c27f7420dfabef0`
- bytes: 986

````mako
<%page args="results_name='wfm_info', results_description='waveforms', output_name='wfm_info'"/>\
<%
    '''Sub-template to populate channel and record info for a waveform in a fetch method.'''
%>\
        channel_names = _converters.expand_channel_string(
            self._repeated_capability,
            self._all_channels_in_session
        )

        ${results_name}_count = len(${results_name})
        channel_count = len(channel_names)
        # Should this raise instead? If this asserts, is it the users fault?
        assert ${results_name}_count % channel_count == 0, 'Number of ${results_description} should be evenly divisible by the number of channels: len(${results_name}) == {0}, len(channel_names) == {1}'.format(${results_name}_count, channel_count)
        actual_num_records = int(${results_name}_count / channel_count)
        waveform_info._populate_channel_and_record_info(${output_name}, channel_names, range(record_number, record_number + actual_num_records))
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/templates/session.py/get_equalization_filter_coefficients.py.mako sha256=fb380c06ea39a4c02c6d521a3413f92cc5b1ede155cce4749cb7b4814be836c6 bytes=564 -->
## FILE: src/niscope/templates/session.py/get_equalization_filter_coefficients.py.mako

- repository: `ni/nimi-python`
- source_path: `src/niscope/templates/session.py/get_equalization_filter_coefficients.py.mako`
- sha256: `fb380c06ea39a4c02c6d521a3413f92cc5b1ede155cce4749cb7b4814be836c6`
- bytes: 564

````mako
<%page args="f, config, method_template"/>\
<%
    '''Forwards to _get_equalization_filter_coefficients() with a nicer interface'''
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        return self._get_equalization_filter_coefficients(self.equalization_num_coefficients)
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niscope/unit_tests/test_niscope.py sha256=1876ff95986991afeff97e4dc81ed0bd05dc211e45586785d519cdc9e22a1d28 bytes=1259 -->
## FILE: src/niscope/unit_tests/test_niscope.py

- repository: `ni/nimi-python`
- source_path: `src/niscope/unit_tests/test_niscope.py`
- sha256: `1876ff95986991afeff97e4dc81ed0bd05dc211e45586785d519cdc9e22a1d28`
- bytes: 1259

````python
import array
import niscope.waveform_info


def test_populate_samples_info():
    waveform_infos = []
    for i in range(1, 4):
        waveform_infos.append(niscope.waveform_info.WaveformInfo())
        waveform_infos[-1]._actual_samples = i

    sample_data = array.array('d', [0, 1, 2, 3, 4, 5, 6, 7, 8])
    niscope.waveform_info._populate_samples_info(waveform_infos, sample_data, 3)

    expected = [
        array.array('d', [0]),
        array.array('d', [3, 4]),
        array.array('d', [6, 7, 8])
    ]
    for i in range(len(waveform_infos)):
        assert waveform_infos[i]._actual_samples is None
        assert waveform_infos[i].samples == expected[i]


def test_populate_channel_and_record_info():
    waveform_infos = []
    for i in range(6):
        waveform_infos.append(niscope.waveform_info.WaveformInfo())

    channels = ["Dev1/4", "Dev2/2"]
    records = [0, 1, 2]
    niscope.waveform_info._populate_channel_and_record_info(waveform_infos, channels, records)

    expected_channels = ["Dev1/4", "Dev2/2"] * len(records)
    expected_records = [0, 0, 1, 1, 2, 2]

    for i in range(len(waveform_infos)):
        assert waveform_infos[i].channel == expected_channels[i]
        assert waveform_infos[i].record == expected_records[i]
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nise/examples/nise_basic_example.py sha256=22432a616abea122ff3705119f9fc761be7c76908d0f705fc172abd78c1dc4be bytes=966 -->
## FILE: src/nise/examples/nise_basic_example.py

- repository: `ni/nimi-python`
- source_path: `src/nise/examples/nise_basic_example.py`
- sha256: `22432a616abea122ff3705119f9fc761be7c76908d0f705fc172abd78c1dc4be`
- bytes: 966

````python
#!/usr/bin/python
import argparse
import nise
import sys


def example(virtual_device_name, connection):
    with nise.Session(virtual_device_name=virtual_device_name) as session:
        session.connect(connection)
        print(connection, ' is now connected.')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Connects the specified connection specification', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--virtual-device', default='SwitchExecutiveExample', help='NI Switch Executive Virtual Device name')
    parser.add_argument('-c', '--connection', default='DIOToUUT', help='Connection Specification')
    args = parser.parse_args(argsv)
    example(args.virtual_device, args.connection)


def main():
    _main(sys.argv[1:])


def test_example():
    example('SwitchExecutiveExample', 'DIOToUUT')


def test_main():
    cmd_line = []
    _main(cmd_line)


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nise/LATEST_RELEASE sha256=dd1b44562fc7c779fd9bef2e55d2e7b58783c4ca61885f5b549cd89de7e9a3fd bytes=7 -->
## FILE: src/nise/LATEST_RELEASE

- repository: `ni/nimi-python`
- source_path: `src/nise/LATEST_RELEASE`
- sha256: `dd1b44562fc7c779fd9bef2e55d2e7b58783c4ca61885f5b549cd89de7e9a3fd`
- bytes: 7

````text
1.4.9
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nise/metadata/__init__.py sha256=4b7b39cf71ea45690188c6523109d0f0f8d8fcd1aa92823d69a7a1554cb97ddc bytes=513 -->
## FILE: src/nise/metadata/__init__.py

- repository: `ni/nimi-python`
- source_path: `src/nise/metadata/__init__.py`
- sha256: `4b7b39cf71ea45690188c6523109d0f0f8d8fcd1aa92823d69a7a1554cb97ddc`
- bytes: 513

````python
from metadata.config import config
from metadata.functions import functions
from metadata.attributes import attributes
from metadata.enums import enums
import metadata.functions_addon
import metadata.attributes_addon
import metadata.enums_addon
import metadata.config_addon

import build.helper as helper
import sys

# Update generated functions data with hand maintained data
config['modules'] = sys.modules
helper.add_all_metadata(functions, attributes, enums, config)

__version__ = config['module_version']
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nise/metadata/attributes.py sha256=ddafc8890d6c490623cc955d0e55b00c4de1f1b88a626c9a439ec0dd59c8c92a bytes=122 -->
## FILE: src/nise/metadata/attributes.py

- repository: `ni/nimi-python`
- source_path: `src/nise/metadata/attributes.py`
- sha256: `ddafc8890d6c490623cc955d0e55b00c4de1f1b88a626c9a439ec0dd59c8c92a`
- bytes: 122

````python
# -*- coding: utf-8 -*-
# This file is generated from NI Switch Executive API metadata version 24.3.0d13
attributes = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nise/metadata/attributes_addon.py sha256=17a2127d02579d026109ae3070d68b679f75dfef78e81e17ee575a6a80fec153 bytes=201 -->
## FILE: src/nise/metadata/attributes_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nise/metadata/attributes_addon.py`
- sha256: `17a2127d02579d026109ae3070d68b679f75dfef78e81e17ee575a6a80fec153`
- bytes: 201

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nise/metadata/config.py sha256=f2bdecc8cb725b4fe9eee4960c7e9b83787323d7ea2261671f6ae3240a0a2ab0 bytes=1126 -->
## FILE: src/nise/metadata/config.py

- repository: `ni/nimi-python`
- source_path: `src/nise/metadata/config.py`
- sha256: `f2bdecc8cb725b4fe9eee4960c7e9b83787323d7ea2261671f6ae3240a0a2ab0`
- bytes: 1126

````python
# -*- coding: utf-8 -*-
# This file is generated from NI Switch Executive API metadata version 24.3.0d13
config = {
    'api_version': '24.3.0d13',
    'c_function_prefix': 'niSE_',
    'close_function': 'CloseSession',
    'context_manager_name': {
    },
    'custom_types': [
    ],
    'driver_name': 'NI Switch Executive',
    'driver_registry': 'Switch Executive',
    'extra_errors_used': [
        'InvalidRepeatedCapabilityError'
    ],
    'grpc_service_class_prefix': 'NiSE',
    'init_function': 'OpenSession',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nise',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'nise.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'nise.dll',
                'type': 'cdll'
            }
        }
    },
    'module_name': 'nise',
    'repeated_capabilities': [
    ],
    'session_class_description': 'An NI Switch Executive session',
    'session_handle_parameter_name': 'vi',
    'use_locking': False
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nise/metadata/config_addon.py sha256=5ad7c08e1888e8ec087b1bf066763c7340ca09cb8c36be356261ac640cd4cbdf bytes=259 -->
## FILE: src/nise/metadata/config_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nise/metadata/config_addon.py`
- sha256: `5ad7c08e1888e8ec087b1bf066763c7340ca09cb8c36be356261ac640cd4cbdf`
- bytes: 259

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.4.10.dev0',
    'latest_runtime_version_tested_against': '2023 Q1',
    'initial_release_year': '2018',
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nise/metadata/enums.py sha256=49f0cd0fb0d9728e9a7aba67c35c26324372b3f83ce25331a53eee02213cdc15 bytes=3829 -->
## FILE: src/nise/metadata/enums.py

- repository: `ni/nimi-python`
- source_path: `src/nise/metadata/enums.py`
- sha256: `49f0cd0fb0d9728e9a7aba67c35c26324372b3f83ce25331a53eee02213cdc15`
- bytes: 3829

````python
# -*- coding: utf-8 -*-
# This file is generated from NI Switch Executive API metadata version 24.3.0d13
enums = {
    'ExpandAction': {
        'values': [
            {
                'documentation': {
                    'description': 'Expand to routes'
                },
                'name': 'NISE_VAL_EXPAND_TO_ROUTES',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Expand to paths'
                },
                'name': 'NISE_VAL_EXPAND_TO_PATHS',
                'value': 1
            }
        ]
    },
    'MulticonnectMode': {
        'values': [
            {
                'documentation': {
                    'description': 'Default'
                },
                'name': 'NISE_VAL_DEFAULT',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'No multiconnect'
                },
                'name': 'NISE_VAL_NO_MULTICONNECT',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Multiconnect'
                },
                'name': 'NISE_VAL_MULTICONNECT',
                'value': 1
            }
        ]
    },
    'OperationOrder': {
        'values': [
            {
                'documentation': {
                    'description': 'Break before make'
                },
                'name': 'NISE_VAL_BREAK_BEFORE_MAKE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Break after make'
                },
                'name': 'NISE_VAL_BREAK_AFTER_MAKE',
                'value': 2
            }
        ]
    },
    'PathCapability': {
        'values': [
            {
                'documentation': {
                    'description': 'Path needs hardwire'
                },
                'name': 'NISE_VAL_PATH_NEEDS_HARDWIRE',
                'value': -2
            },
            {
                'documentation': {
                    'description': 'Path needs config channel'
                },
                'name': 'NISE_VAL_PATH_NEEDS_CONFIG_CHANNEL',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'Path available'
                },
                'name': 'NISE_VAL_PATH_AVAILABLE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Path exists'
                },
                'name': 'NISE_VAL_PATH_EXISTS',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Path Unsupported'
                },
                'name': 'NISE_VAL_PATH_UNSUPPORTED',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Resource in use'
                },
                'name': 'NISE_VAL_RESOURCE_IN_USE',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Exclusion conflict'
                },
                'name': 'NISE_VAL_EXCLUSION_CONFLICT',
                'value': 5
            },
            {
                'documentation': {
                    'description': 'Channel not available'
                },
                'name': 'NISE_VAL_CHANNEL_NOT_AVAILABLE',
                'value': 6
            },
            {
                'documentation': {
                    'description': 'Channels hardwired'
                },
                'name': 'NISE_VAL_CHANNELS_HARDWIRED',
                'value': 7
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nise/metadata/enums_addon.py sha256=6679b48316d199674e91c7dc700f9768376a2671afeea80f4c06ac360cd41596 bytes=186 -->
## FILE: src/nise/metadata/enums_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nise/metadata/enums_addon.py`
- sha256: `6679b48316d199674e91c7dc700f9768376a2671afeea80f4c06ac360cd41596`
- bytes: 186

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nise/metadata/functions.py sha256=dd57a136c83dbf95e74e6e4a96ea89f8a9a37b109e32a8f28267592a15dc4240 bytes=40722 -->
## FILE: src/nise/metadata/functions.py

- repository: `ni/nimi-python`
- source_path: `src/nise/metadata/functions.py`
- sha256: `dd57a136c83dbf95e74e6e4a96ea89f8a9a37b109e32a8f28267592a15dc4240`
- bytes: 40722

````python
# -*- coding: utf-8 -*-
# This file is generated from NI Switch Executive API metadata version 24.3.0d13
functions = {
    'CloseSession': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReduces the reference count of open sessions by one. If the reference\ncount goes to 0, the function deallocates any memory resources the\ndriver uses and closes any open IVI switch sessions. After calling the\nniSE_CloseSession function, you should not use the NI Switch Executive\nvirtual device again until you call niSE_OpenSession.\n'
        },
        'included_in_proto': False,
        'method_name_for_documentation': 'close',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe Session handle that you obtain from niSE_OpenSession. The handle\nidentifies a particular session to the virtual switch device.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Connect': {
        'documentation': {
            'description': '\nConnects the routes specified by the connection specification. When\nconnecting, it may allow for multiconnection based on the\nmulticonnection mode. In the event of an error, the call to\nniSE_Connect will attempt to undo any connections made so that the\nsystem will be left in the same state that it was in before the call was\nmade. Some errors can be caught before manipulating hardware, although\nit is feasible that a hardware call could fail causing some connections\nto be momentarily closed and then reopened. If the wait for debounce\nparameter is set, the function will not return until the switch system\nhas debounced.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe Session handle that you obtain from niSE_OpenSession. The handle\nidentifies a particular session to the virtual switch device.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nString describing the connections to be made. The route specification\nstrings are best summarized as a series of routes delimited by\nampersands. The specified routes may be route names, route group names,\nor fully specified route paths delimited by square brackets. Some\nexamples of route specification strings are: MyRoute MyRouteGroup\nMyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &\n[A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch\nExecutive Help for more information.\n'
                },
                'name': 'connectSpec',
                'type': 'ViConstString'
            },
            {
                'default_value': 'MulticonnectMode.DEFAULT',
                'direction': 'in',
                'documentation': {
                    'description': '\nThis value sets the connection mode for the function. The mode might be\none of the following: NISE_VAL_USE_DEFAULT_MODE (-1) - uses the mode\nselected as the default for the route in the NI Switch Executive virtual\ndevice configuration. If a mode has not been selected for the route in\nthe NI Switch Executive virtual device, this parameter defaults to\nNISE_VAL_MULTICONNECT_ROUTES. NISE_VAL_NO_MULTICONNECT (0) -\nroutes specified in the connection specification must be disconnected\nbefore they can be reconnected. Calling Connect on a route that was\nconnected using No Multiconnect mode results in an error condition.\nNISE_VAL_MULTICONNECT_ROUTES (1)- routes specified in the connection\nspecification can be connected multiple times. The first call to Connect\nperforms the physical hardware connection. Successive calls to Connect\nincrease a connection reference count. Similarly, calls to Disconnect\ndecrease the reference count. Once it reaches 0, the hardware is\nphysically disconnected. Multiconnecting routes applies to entire routes\nand not to route segments.\n'
                },
                'enum': 'MulticonnectMode',
                'name': 'multiconnectMode',
                'type': 'ViInt32'
            },
            {
                'default_value': True,
                'direction': 'in',
                'documentation': {
                    'description': '\nWaits (if true) for switches to debounce between its connect and\ndisconnect operations. If false, it immediately begins the second\noperation after completing the first. The order of connect and\ndisconnect operation is set by the Operation Order input.\n'
                },
                'name': 'waitForDebounce',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConnectAndDisconnect': {
        'documentation': {
            'description': '\nConnects routes and disconnects routes in a similar fashion to\nniSE_Connect and niSE_Disconnect except that the operations happen in\nthe context of a single function call. This function is useful for\nswitching from one state to another state. niSE_ConnectAndDisconnect\nmanipulates the hardware connections and disconnections only when the\nroutes are different between the connection and disconnection\nspecifications. If any routes are common between the connection and\ndisconnection specifications, NI Switch Executive determines whether or\nnot the relays need to be switched. This functionality has the distinct\nadvantage of increased throughput for shared connections, because\nhardware does not have to be involved and potentially increases relay\nlifetime by decreasing the number of times that the relay has to be\nswitched. In the event of an error, the call to\nniSE_ConnectAndDisconnect attempts to undo any connections made, but\ndoes not attempt to reconnect disconnections. Some errors can be caught\nbefore manipulating hardware, although it is feasible that a hardware\ncall could fail causing some connections to be momentarily closed and\nthen reopened.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe Session handle that you obtain from niSE_OpenSession. The handle\nidentifies a particular session to the virtual switch device.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nString describing the connections to be made. The route specification\nstrings are best summarized as a series of routes delimited by\nampersands. The specified routes may be route names, route group names,\nor fully specified route paths delimited by square brackets. Some\nexamples of route specification strings are: MyRoute MyRouteGroup\nMyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &\n[A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch\nExecutive Help for more information.\n'
                },
                'name': 'connectSpec',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nString describing the disconnections to be made. The route specification\nstrings are best summarized as a series of routes delimited by\nampersands. The specified routes may be route names, route group names,\nor fully specified route paths delimited by square brackets. Some\nexamples of route specification strings are: MyRoute MyRouteGroup\nMyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &\n[A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch\nExecutive Help for more information.\n'
                },
                'name': 'disconnectSpec',
                'type': 'ViConstString'
            },
            {
                'default_value': 'MulticonnectMode.DEFAULT',
                'direction': 'in',
                'documentation': {
                    'description': '\nThis value sets the connection mode for the function. The mode might be\none of the following: NISE_VAL_USE_DEFAULT_MODE (-1) - uses the mode\nselected as the default for the route in the NI Switch Executive virtual\ndevice configuration. If a mode has not been selected for the route in\nthe NI Switch Executive virtual device, this parameter defaults to\nNISE_VAL_MULTICONNECT_ROUTES. NISE_VAL_NO_MULTICONNECT (0) -\nroutes specified in the connection specification must be disconnected\nbefore they can be reconnected. Calling Connect on a route that was\nconnected using No Multiconnect mode results in an error condition.\nNISE_VAL_MULTICONNECT_ROUTES (1) - routes specified in the connection\nspecification can be connected multiple times. The first call to Connect\nperforms the physical hardware connection. Successive calls to Connect\nincrease a connection reference count. Similarly, calls to Disconnect\ndecrease the reference count. Once it reaches 0, the hardware is\nphysically disconnected. This behavior is slightly different with SPDT\nrelays. For more information, refer to the Exclusions and SPDT Relays\ntopic in the NI Switch Executive Help. Multiconnecting routes applies to\nentire routes and not to route segments.\n'
                },
                'enum': 'MulticonnectMode',
                'name': 'multiconnectMode',
                'type': 'ViInt32'
            },
            {
                'default_value': 'OperationOrder.AFTER',
                'direction': 'in',
                'documentation': {
                    'description': '\nSets the order of the operation for the function. Defined values are\nBreak Before Make and Break After Make. NISE_VAL_BREAK_BEFORE_MAKE\n(1) - The function disconnects the routes specified in the disconnect\nspecification before connecting the routes specified in the connect\nspecification. This is the typical mode of operation.\nNISE_VAL_BREAK_AFTER_MAKE (2) - The function connects the routes\nspecified in the connection specification before connecting the routes\nspecified in the disconnection specification. This mode of operation is\nnormally used when you are switching current and want to ensure that a\nload is always connected to your source. The order of operation is to\nconnect first or disconnect first.\n'
                },
                'enum': 'OperationOrder',
                'name': 'operationOrder',
                'type': 'ViInt32'
            },
            {
                'default_value': True,
                'direction': 'in',
                'documentation': {
                    'description': '\nWaits (if true) for switches to debounce between its connect and\ndisconnect operations. If false, it immediately begins the second\noperation after completing the first. The order of connect and\ndisconnect operation is set by the Operation Order input.\n'
                },
                'name': 'waitForDebounce',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'Disconnect': {
        'documentation': {
            'description': '\nDisconnects the routes specified in the Disconnection Specification. If\nany of the specified routes were originally connected in a\nmulticonnected mode, the call to niSE_Disconnect reduces the reference\ncount on the route by 1. If the reference count reaches 0, it is\ndisconnected. If a specified route does not exist, it is an error\ncondition. In the event of an error, the call to niSE_Disconnect\ncontinues to try to disconnect everything specified by the route\nspecification string but reports the error on completion.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe Session handle that you obtain from niSE_OpenSession. The handle\nidentifies a particular session to the virtual switch device.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nString describing the disconnections to be made. The route specification\nstrings are best summarized as a series of routes delimited by\nampersands. The specified routes may be route names, route group names,\nor fully specified route paths delimited by square brackets. Some\nexamples of route specification strings are: MyRoute MyRouteGroup\nMyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &\n[A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch\nExecutive Help for more information.\n'
                },
                'name': 'disconnectSpec',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisconnectAll': {
        'documentation': {
            'description': '\nDisconnects all connections on every IVI switch device managed by the\nNISE session reference passed to this function. niSE_DisconnectAll\nignores all multiconnect modes. Calling niSE_DisconnectAll resets all\nof the switch states for the system.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe Session handle that you obtain from niSE_OpenSession. The handle\nidentifies a particular session to the virtual switch device.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExpandRouteSpec': {
        'documentation': {
            'description': '\nExpands a route spec string to yield more information about the routes\nand route groups within the spec. The route specification string\nreturned from niSE_ExpandRouteSpec can be passed to other Switch\nExecutive API functions (such as niSE_Connect, niSE_Disconnect, and\nniSE_ConnectAndDisconnect) that use route specification strings.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe Session handle that you obtain from niSE_OpenSession. The handle\nidentifies a particular session to the virtual switch device.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nString describing the routes and route groups to expand. The route\nspecification strings are best summarized as a series of routes\ndelimited by ampersands. The specified routes may be route names, route\ngroup names, or fully specified route paths delimited by square\nbrackets. Some examples of route specification strings are: MyRoute\nMyRouteGroup MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute &\nMyRouteGroup & [A->Switch1/r0->B] Refer to Route Specification Strings\nin the NI Switch Executive Help for more information.\n'
                },
                'name': 'routeSpec',
                'type': 'ViConstString'
            },
            {
                'default_value': 'ExpandAction.ROUTES',
                'direction': 'in',
                'documentation': {
                    'description': '\nThis value sets the expand action for the function. The action might be\none of the following: NISE_VAL_EXPAND_TO_ROUTES (0) - expands the\nroute spec to routes. Converts route groups to their constituent routes.\nNISE_VAL_EXPAND_TO_PATHS (1) - expands the route spec to paths.\nConverts routes and route groups to their constituent square bracket\nroute spec strings. Example: [Dev1/c0->Dev1/r0->Dev1/c1]\n'
                },
                'enum': 'ExpandAction',
                'name': 'expandAction',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe expanded route spec. Route specification strings can be directly\npassed to niSE_Connect, niSE_Disconnect, or niSE_ConnectAndDisconnect\nRefer to Route Specification Strings in the NI Switch Executive Help for\nmore information. You may pass NULL for this parameter if you are not\ninterested in the return value. To obtain the route specification\nstring, you should pass a buffer to this parameter. The size of the\nbuffer required may be obtained by calling the function with NULL for\nthis parameter and a valid ViInt32 to routeSpecSize. The routeSpecSize\nwill contain the size needed to hold the entire route specification\n(including the NULL termination character). Common operation is to call\nthe function twice. The first time you call the function you can\ndetermine the size needed to hold the route specification string.\nAllocate a buffer of the appropriate size and then re-call the function\nto obtain the entire buffer.\n'
                },
                'name': 'expandedRouteSpec',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'expanded_route_spec_size[0]'
                },
                'type': 'ViChar[]'
            },
            {
                'default_value': [
                    1024
                ],
                'direction': 'in',
                'documentation': {
                    'description': '\nThe routeSpecSize is an ViInt32 that is passed by reference into the\nfunction. As an input, it is the size of the route spec string buffer\nbeing passed. If the route spec string is larger than the string buffer\nbeing passed, only the portion of the route spec string that can fit in\nthe string buffer is copied into it. On return from the function,\nrouteSpecSize holds the size required to hold the entire route spec\nstring. Note that this size may be larger than the buffer size as the\nfunction always returns the size needed to hold the entire buffer. You\nmay pass NULL for this parameter if you are not interested in the return\nvalue for routeSpecSize and routeSpec.\n'
                },
                'name': 'expandedRouteSpecSize',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'ViInt32[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FindRoute': {
        'documentation': {
            'description': '\nFinds an existing or potential route between channel 1 and channel 2.\nThe returned route specification contains the route specification and\nthe route capability determines whether or not the route existed, is\npossible, or is not possible for various reasons. The route\nspecification string returned from niSE_FindRoute can be passed to\nother Switch Executive API functions (such as niSE_Connect,\nniSE_Disconnect, and niSE_ConnectAndDisconnect) that use route\nspecification strings.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe Session handle that you obtain from niSE_OpenSession. The handle\nidentifies a particular session to the virtual switch device.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nChannel name of one of the endpoints of the route to find. The channel\nname must either be a channel alias name or a name in the\ndevice/ivichannel syntax. Examples: MyChannel Switch1/R0\n'
                },
                'name': 'channel1',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nChannel name of one of the endpoints of the route to find. The channel\nname must either be a channel alias name or a name in the\ndevice/ivichannel syntax. Examples: MyChannel Switch1/R0\n'
                },
                'name': 'channel2',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe fully specified route path complete with delimiting square\nbrackets if the route exists or is possible. An example of a fully\nspecified route string is: [A->Switch1/r0->B] Route specification\nstrings can be directly passed to niSE_Connect, niSE_Disconnect, or\nniSE_ConnectAndDisconnect Refer to Route Specification Strings in the\nNI Switch Executive Help for more information. You may pass NULL for\nthis parameter if you are not interested in the return value. To obtain\nthe route specification string, you should pass a buffer to this\nparameter. The size of the buffer required may be obtained by calling\nthe function with NULL for this parameter and a valid ViInt32 to\nrouteSpecSize. The routeSpecSize will contain the size needed to hold\nthe entire route specification (including the NULL termination\ncharacter). Common operation is to call the function twice. The first\ntime you call the function you can determine the size needed to hold the\nroute specification string. Allocate a buffer of the appropriate size\nand then re-call the function to obtain the entire buffer.\n'
                },
                'name': 'routeSpec',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'route_spec_size[0]'
                },
                'type': 'ViChar[]'
            },
            {
                'default_value': [
                    1024
                ],
                'direction': 'in',
                'documentation': {
                    'description': '\nThe routeSpecSize is an ViInt32 that is passed by reference into the\nfunction. As an input, it is the size of the route string buffer being\npassed. If the route string is larger than the string buffer being\npassed, only the portion of the route string that can fit in the string\nbuffer is copied into it. On return from the function, routeSpecSize\nholds the size required to hold the entire route string. Note that this\nsize may be larger than the buffer size as the function always returns\nthe size needed to hold the entire buffer. You may pass NULL for this\nparameter if you are not interested in the return value for\nrouteSpecSize and routeSpec.\n'
                },
                'name': 'routeSpecSize',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe return value which expresses the capability of finding a valid route\nbetween Channel 1 and Channel 2. Refer to the table below for value\ndescriptions. You may pass NULL for this parameter if you are not\ninterested in the return value. Route capability might be one of the\nfollowing: Path Available (1) A path between channel 1 and channel 2 is\navailable. The route specification parameter returns a string describing\nthe available path. Path Exists (2) A path between channel 1 and channel\n2 already exists. The route specification parameter returns a string\ndescribing the existing path. Path Unsupported (3) There is no potential\npath between channel 1 and channel 2 given the current configuration.\nResource In Use (4) There is a potential path between channel 1 and\nchannel 2, although a resource needed to complete the path is already in\nuse. Source Conflict (5) Channel 1 and channel 2 cannot be connected\nbecause their connection would result in an exclusion violation. Channel\nNot Available (6) One of the channels is not useable as an endpoint\nchannel. Make sure that it is not marked as a reserved for routing.\nChannels Hardwired (7) The two channels reside on the same hardwire. An\nimplicit path already exists.\n'
                },
                'enum': 'PathCapability',
                'name': 'pathCapability',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAllConnections': {
        'documentation': {
            'description': '\nReturns the top-level connected routes and route groups. The route\nspecification string returned from niSE_GetAllConnections can be passed\nto other Switch Executive API functions (such as niSE_Connect,\nniSE_Disconnect, niSE_ConnectAndDisconnect, and niSE_ExpandRouteSpec)\nthat use route specification strings.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe Session handle that you obtain from niSE_OpenSession. The handle\nidentifies a particular session to the virtual switch device.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe route spec of all currently connected routes and route groups. Route\nspecification strings can be directly passed to niSE_Connect,\nniSE_Disconnect, niSE_ConnectAndDisconnect, or niSE_ExpandRouteSpec\nRefer to Route Specification Strings in the NI Switch Executive Help for\nmore information. You may pass NULL for this parameter if you are not\ninterested in the return value. To obtain the route specification\nstring, you should pass a buffer to this parameter. The size of the\nbuffer required may be obtained by calling the function with NULL for\nthis parameter and a valid ViInt32 to routeSpecSize. The routeSpecSize\nwill contain the size needed to hold the entire route specification\n(including the NULL termination character). Common operation is to call\nthe function twice. The first time you call the function you can\ndetermine the size needed to hold the route specification string.\nAllocate a buffer of the appropriate size and then re-call the function\nto obtain the entire buffer.\n'
                },
                'name': 'routeSpec',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'route_spec_size[0]'
                },
                'type': 'ViChar[]'
            },
            {
                'default_value': [
                    1024
                ],
                'direction': 'in',
                'documentation': {
                    'description': '\nThe routeSpecSize is an ViInt32 that is passed by reference into the\nfunction. As an input, it is the size of the route spec string buffer\nbeing passed. If the route spec string is larger than the string buffer\nbeing passed, only the portion of the route spec string that can fit in\nthe string buffer is copied into it. On return from the function,\nrouteSpecSize holds the size required to hold the entire route spec\nstring. Note that this size may be larger than the buffer size as the\nfunction always returns the size needed to hold the entire buffer. You\nmay pass NULL for this parameter if you are not interested in the return\nvalue for routeSpecSize and routeSpec.\n'
                },
                'name': 'routeSpecSize',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'ViInt32[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'private',
        'documentation': {
            'description': "\nGet error information of the first error that occurred. If a valid\npointer is passed to errorDescription or errorNumber, GetError will\nclear the error on completion. errorDescriptionSize is an in/out\nparameter that describes the size of the errorDescription buffer. On the\nway in, it tells the function the size of string. On the way out, it\ndescribes the number of bytes (including the trailing null string)\nneeded to hold the entire error description buffer. If NULL is passed\nfor errorDescription and the errorNumber, the function will not clear\nthe error. Users wanting to dynamically size the errorDescription string\ncan thus call the function twice. On the first call they can pass NULL\nfor the errorDescription and use the returned errorDescriptionSize to\nallocate enough space for the entire errorDescription buffer. Note that\nif a buffer is passed that is not large enough to hold the entire\ndescription string, the portion of of the string that will fit in the\npassed buffer will be returned and the error will still be cleared. All\nof the parameters are NULL tolerant. Note that passing NULL for both\nerrorNumber and errorDescription can change the function's behavior.\n"
        },
        'included_in_proto': False,
        'is_error_handling': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'none'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe Session handle that you obtain from niSE_OpenSession. The handle\nidentifies a particular session to the virtual switch device.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nBy reference parameter which returns the error number of the first error\nwhich occurred on the session since the error was last cleared. You may\npass NULL for this parameter if you are not interested in the return\nvalue.\n'
                },
                'name': 'errorNumber',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nBy reference buffer which is to be filled with the error description\nstring. You may pass NULL for this parameter if you are not interested\nin the return value. To obtain the error description string, you should\npass a buffer to this parameter. The size of the buffer required may be\nobtained by calling the function with NULL for this parameter and a\nvalid ViInt32 to the error description size parameter. The error\ndescription size will contain the size needed to hold the entire route\nspecification (including the NULL termination character). Common\noperation is to call the function twice. The first time you call the\nfunction you can determine the size needed to hold the route\nspecification string. Allocate a buffer of the appropriate size and then\nre-call the function to obtain the entire buffer.\n'
                },
                'name': 'errorDescription',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'error_description_size[0]'
                },
                'type': 'ViChar[]'
            },
            {
                'default_value': [
                    1024
                ],
                'direction': 'in',
                'documentation': {
                    'description': '\nAs input, it is the size of the error description string buffer. As\noutput, it is the Size of the entire error description string (may be\nlarger than the buffer size as the function always returns the size\nneeded to hold the entire buffer). This parameter is a ViInt32 that is\npassed by reference into the function. As an input, it is the size of\nthe error description buffer being passed. If the error description\nstring is larger than the string buffer being passed, only the portion\nof the route string that can fit in the string buffer will be copied\ninto it. On return from the function, it holds the size required to hold\nthe entire error description string, including the NULL termination\ncharacter. Note that this size may be larger than the buffer size as the\nfunction always returns the size needed to hold the entire buffer. You\nmay pass NULL for this parameter if you are not interested in the return\nvalue for it.\n'
                },
                'name': 'errorDescriptionSize',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'ViInt32[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'IsConnected': {
        'documentation': {
            'description': '\nChecks whether the specified routes and routes groups are connected. It\nreturns true if connected.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe Session handle that you obtain from niSE_OpenSession. The handle\nidentifies a particular session to the virtual switch device.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nString describing the connections to check. The route specification\nstrings are best summarized as a series of routes delimited by\nampersands. The specified routes may be route names, route group names,\nor fully specified route paths delimited by square brackets. Some\nexamples of route specification strings are: MyRoute MyRouteGroup\nMyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &\n[A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch\nExecutive Help for more information.\n'
                },
                'name': 'routeSpec',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns TRUE if the routes and routes groups are connected or FALSE if\nthey are not.\n'
                },
                'name': 'isConnected',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'IsDebounced': {
        'documentation': {
            'description': '\nChecks to see if the switching system is debounced or not. This function\ndoes not wait for debouncing to occur. It returns true if the system is\nfully debounced. This function is similar to the IviSwtch specific\nfunction.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe Session handle that you obtain from niSE_OpenSession. The handle\nidentifies a particular session to the virtual switch device.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns TRUE if the system is fully debounced or FALSE if it is still\nsettling.\n'
                },
                'name': 'isDebounced',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'OpenSession': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nOpens a session to a specified NI Switch Executive virtual device. Opens\ncommunications with all of the IVI switches associated with the\nspecified NI Switch Executive virtual device. Returns a session handle\nthat you use to identify the virtual device in all subsequent NI Switch\nExecutive function calls. NI Switch Executive uses a reference counting\nscheme to manage open session handles to an NI Switch Executive virtual\ndevice. Each call to niSE_OpenSession must be matched with a subsequent\ncall to niSE_CloseSession. Successive calls to niSE_OpenSession with\nthe same virtual device name always returns the same session handle. NI\nSwitch Executive disconnects its communication with the IVI switches\nafter all session handles are closed to a given virtual device. The\nsession handles may be used safely in multiple threads of an\napplication. Sessions may only be opened to a given NI Switch Executive\nvirtual device from a single process at a time.\n'
        },
        'included_in_proto': False,
        'method_name_for_documentation': '__init__',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The name of the NI Switch Executive virtual device.'
                },
                'name': 'virtualDeviceName',
                'type': 'ViConstString'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe option string can be used to pass information to each of the IVI\ndevices on startup. It can be used to set things such as simulation,\nrange checking, etc. Consult your driver documentation for more\ninformation about valid entries for the option string.\n'
                },
                'name': 'optionString',
                'python_api_converter_name': 'convert_init_with_options_dictionary',
                'type': 'ViConstString',
                'type_in_documentation': 'dict'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The session referencing this NI Switch Executive virtual device session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'WaitForDebounce': {
        'documentation': {
            'description': '\nWaits for all of the switches in the NI Switch Executive virtual device\nto debounce. This function does not return until either the switching\nsystem is completely debounced and settled or the maximum time has\nelapsed and the system is not yet debounced. In the event that the\nmaximum time elapses, the function returns an error indicating that a\ntimeout has occurred. To ensure that all of the switches have settled,\nNI recommends calling niSE_WaitForDebounce after a series of connection\nor disconnection operations and before taking any measurements of the\nsignals connected to the switching system.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe Session handle that you obtain from niSE_OpenSession. The handle\nidentifies a particular session to the virtual switch device.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'hightime.timedelta(milliseconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe amount of time to wait (in milliseconds) for the debounce to\ncomplete. A value of 0 checks for debouncing once and returns an error\nif the system is not debounced at that time. A value of -1 means to\nblock for an infinite period of time until the system is debounced.\n'
                },
                'name': 'maximumTimeMs',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds_int32',
                'type': 'ViInt32',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or int in milliseconds'
            }
        ],
        'returns': 'ViStatus'
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nise/metadata/functions_addon.py sha256=46c53953df0069cf0ddc98438dda6c2fe2350e047331e0e9835f7c9362ba2597 bytes=236 -->
## FILE: src/nise/metadata/functions_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nise/metadata/functions_addon.py`
- sha256: `46c53953df0069cf0ddc98438dda6c2fe2350e047331e0e9835f7c9362ba2597`
- bytes: 236

````python
# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nise/nise.mak sha256=3a17688a980c3dd3858a798b6ec13fc73302494c9df2b04a76f879dda3aea4b8 bytes=485 -->
## FILE: src/nise/nise.mak

- repository: `ni/nimi-python`
- source_path: `src/nise/nise.mak`
- sha256: `3a17688a980c3dd3858a798b6ec13fc73302494c9df2b04a76f879dda3aea4b8`
- bytes: 485

````makefile
include $(BUILD_HELPER_DIR)/defines.mak
include $(BUILD_HELPER_DIR)/tools.mak

# We want everything but _attributes.py
MODULE_FILES_TO_GENERATE := $(filter-out _attributes.py,$(DEFAULT_PY_FILES_TO_GENERATE))

MODULE_FILES_TO_COPY := $(DEFAULT_PY_FILES_TO_COPY)

RST_FILES_TO_GENERATE := $(filter-out rep_caps.rst,$(DEFAULT_RST_FILES_TO_GENERATE))

SPHINX_CONF_PY := $(DEFAULT_SPHINX_CONF_PY)
READTHEDOCS_CONFIG := $(DEFAULT_READTHEDOCS_CONFIG)

include $(BUILD_HELPER_DIR)/rules.mak
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nise/system_tests/test_system_nise.py sha256=82272bfa13ef5d65daf5676fef09e573909950672dd863dd27b0b282e7496212 bytes=3059 -->
## FILE: src/nise/system_tests/test_system_nise.py

- repository: `ni/nimi-python`
- source_path: `src/nise/system_tests/test_system_nise.py`
- sha256: `82272bfa13ef5d65daf5676fef09e573909950672dd863dd27b0b282e7496212`
- bytes: 3059

````python
import nise
import pytest


@pytest.fixture(scope='function')
def session():
    with nise.Session('SwitchExecutiveExample') as simulated_session:
        yield simulated_session


def test_connect_single_disconnect_single_is_connected(session):
    test_connection = 'DIOToUUT'
    session.connect(test_connection)
    assert session.is_connected(test_connection) is True
    session.disconnect(test_connection)
    assert session.is_connected(test_connection) is False


def test_connect_and_disconnect(session):
    test_connection = 'DIOToUUT'
    test_connection_2 = 'PowerUUT'
    session.connect(test_connection)
    assert session.is_connected(test_connection) is True
    session.connect_and_disconnect(test_connection_2, test_connection)
    assert session.is_connected(test_connection) is False
    assert session.is_connected(test_connection_2) is True
    session.disconnect(test_connection_2)
    assert session.is_connected(test_connection_2) is False


def test_connect_single_disconnect_all(session):
    test_connection = 'DIOToUUT'
    session.connect(test_connection)
    assert session.is_connected(test_connection) is True
    session.disconnect_all()
    assert session.is_connected(test_connection) is False


def test_get_all_connections(session):
    test_connection = 'DIOToUUT'
    session.connect(test_connection)
    assert session.is_connected(test_connection) is True
    connections = session.get_all_connections()
    assert connections == test_connection
    session.disconnect(test_connection)
    assert session.is_connected(test_connection) is False


def test_find_route(session):
    test_channel_1 = 'DCPower'
    test_channel_2 = 'Scope'
    route, capability = session.find_route(test_channel_1, test_channel_2)
    assert route == '[SampleMatrix1/c0->SampleMatrix1/r0->SampleMatrix1/c1]'
    assert capability == nise.PathCapability.PATH_AVAILABLE


def test_find_route_different_length(session):
    test_channel_1 = 'DCPower'
    test_channel_2 = 'Scope'
    length = [5]
    route, capability = session.find_route(test_channel_1, test_channel_2, length)
    assert route == '[Sam'
    assert capability == nise.PathCapability.PATH_AVAILABLE


def test_expand_route_spec(session):
    test_connection = 'DIOToUUT'
    route_spec = session.expand_route_spec(test_connection)
    assert route_spec.find('DIO_0ToUUT_IO_0_Leg1') != -1


def test_is_debounced_wait_for_debounce(session):
    test_connection = 'DIOToUUT'
    session.connect(test_connection, wait_for_debounce=False)
    session.wait_for_debounce()
    assert session.is_debounced() is True
    assert session.is_connected(test_connection) is True
    session.disconnect(test_connection)
    assert session.is_connected(test_connection) is False


def test_error(session):
    test_connection = 'FakeConnection'
    try:
        session.connect(test_connection)
    except nise.Error as e:
        assert e.code == -29007
        assert e.description.find('The route specification string contains invalid characters or could not be understood.') != -1
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niswitch/examples/niswitch_connect_channels.py sha256=120c2e50cd2877edfc2c679489aa13f36a32a00053ba3c7a21e78d1616c4524a bytes=1678 -->
## FILE: src/niswitch/examples/niswitch_connect_channels.py

- repository: `ni/nimi-python`
- source_path: `src/niswitch/examples/niswitch_connect_channels.py`
- sha256: `120c2e50cd2877edfc2c679489aa13f36a32a00053ba3c7a21e78d1616c4524a`
- bytes: 1678

````python
#!/usr/bin/python

import argparse
import niswitch
import sys


def example(resource_name, channel1, channel2, topology, simulate):
    # if we are simulating resource name must be blank
    resource_name = '' if simulate else resource_name

    with niswitch.Session(resource_name=resource_name, topology=topology, simulate=simulate) as session:
        session.connect(channel1=channel1, channel2=channel2)
        print('Channel ', channel1, ' and ', channel2, ' are now connected.')
        session.disconnect(channel1=channel1, channel2=channel2)
        print('Channel ', channel1, ' and ', channel2, ' are now disconnected.')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Performs a connection with NI-SWITCH Channels.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI switch.')
    parser.add_argument('-ch1', '--channel1', default='c0', help='Channel One.')
    parser.add_argument('-ch2', '--channel2', default='r0', help='Channel Two.')
    parser.add_argument('-t', '--topology', default='Configured Topology', help='Topology.')
    parser.add_argument('-s', '--simulate', default=False, action='store_true', help='Simulate device.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.channel1, args.channel2, args.topology, args.simulate)


def test_example():
    example('', 'c0', 'r0', '2737/2-Wire 4x64 Matrix', True)


def test_main():
    cmd_line = ['--topology', '2737/2-Wire 4x64 Matrix', '--simulate']
    _main(cmd_line)


def main():
    _main(sys.argv[1:])


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niswitch/examples/niswitch_get_device_info.py sha256=bb4e7819b9aca3ebbc4ddba86c387737247a76cffa13ab1d3ca2f44360219fdc bytes=3344 -->
## FILE: src/niswitch/examples/niswitch_get_device_info.py

- repository: `ni/nimi-python`
- source_path: `src/niswitch/examples/niswitch_get_device_info.py`
- sha256: `bb4e7819b9aca3ebbc4ddba86c387737247a76cffa13ab1d3ca2f44360219fdc`
- bytes: 3344

````python
#!/usr/bin/python

import argparse
import niswitch
import sys


def example(resource_name, topology, simulate, device, channel, relay):
    # if we are simulating resource name must be blank
    resource_name = '' if simulate else resource_name

    with niswitch.Session(resource_name=resource_name, topology=topology, simulate=simulate) as session:
        if device:
            print('Device Info:')
            row_format = '{:<18}' * (2)
            print(row_format.format('Device Name: ', session.io_resource_descriptor))
            print(row_format.format('Device Model: ', session.instrument_model))
            print(row_format.format('Driver Revision: ', session.specific_driver_revision))
            print(row_format.format('Channel count: ', session.channel_count))
            print(row_format.format('Relay count: ', session.number_of_relays))
        if channel:
            print('Channel Info:')
            row_format = '{:6}' + ' ' * 12 + '{:<15}{:<22}{:6}'
            print(row_format.format('Number', 'Name', 'Is Configuration', 'Is Source'))
            for i in range(1, session.channel_count + 1):
                channel_name = session.get_channel_name(index=i)
                channel = session.channels[channel_name]
                print(row_format.format(i, channel_name, str(channel.is_configuration_channel), str(channel.is_source_channel)))
        if relay:
            print('Relay Info:')
            row_format = '{:6}' + ' ' * 12 + '{:<15}{:<22}{:6}'
            print(row_format.format('Number', 'Name', 'Position', 'Count'))
            for i in range(1, session.number_of_relays + 1):
                relay_name = session.get_relay_name(index=i)
                print(row_format.format(i, relay_name, session.get_relay_position(relay_name=relay_name), session.get_relay_count(relay_name=relay_name)))


def _main(argsv):
    parser = argparse.ArgumentParser(description='Prints information for the specified NI-SWITCH.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI switch.')
    parser.add_argument('-d', '--device', default=False, action='store_true', help='Prints information for the device')
    parser.add_argument('-c', '--channel', default=False, action='store_true', help='Prints information for all channels on the device')
    parser.add_argument('-r', '--relay', default=False, action='store_true', help='Prints information for all relays on the device')
    parser.add_argument('-t', '--topology', default='Configured Topology', help='Topology.')
    parser.add_argument('-s', '--simulate', default=False, action='store_true', help='Simulate device.')
    args = parser.parse_args(argsv)

    if not (args.device or args.channel or args.relay):
        print('You must specify at least one of -d, -c, or -r!')
        parser.print_help()
        sys.exit(1)

    example(args.resource_name, args.topology, args.simulate, args.device, args.channel, args.relay)


def test_example():
    example('', '2737/2-Wire 4x64 Matrix', True, True, True, True)


def test_main():
    cmd_line = ['--topology', '2737/2-Wire 4x64 Matrix', '--simulate', '--device', '--channel', '--relay', ]
    _main(cmd_line)


def main():
    _main(sys.argv[1:])


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niswitch/examples/niswitch_relay_control.py sha256=8934c642e5b06f8d767aeb83d1192176622281d762857177d11bdfba991a8fc3 bytes=1633 -->
## FILE: src/niswitch/examples/niswitch_relay_control.py

- repository: `ni/nimi-python`
- source_path: `src/niswitch/examples/niswitch_relay_control.py`
- sha256: `8934c642e5b06f8d767aeb83d1192176622281d762857177d11bdfba991a8fc3`
- bytes: 1633

````python
#!/usr/bin/python

import argparse
import niswitch
import sys


def example(resource_name, topology, simulate, relay, action):
    # if we are simulating resource name must be blank
    resource_name = '' if simulate else resource_name

    with niswitch.Session(resource_name=resource_name, topology=topology, simulate=simulate) as session:
        session.relay_control(relay_name=relay, relay_action=niswitch.RelayAction[action])
        print('Relay ', relay, ' has had the action ', action, ' performed.')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Performs relay control with NI-SWITCH relays.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--resource-name', default='PXI1Slot2', help='Resource name of an NI switch.')
    parser.add_argument('-r', '--relay', default='k0', help='Relay Name.')
    parser.add_argument('-a', '--action', default='OPEN', choices=niswitch.RelayAction.__members__.keys(), type=str.upper, help='Relay Action.')
    parser.add_argument('-t', '--topology', default='Configured Topology', help='Topology.')
    parser.add_argument('-s', '--simulate', default=False, action='store_true', help='Simulate device.')
    args = parser.parse_args(argsv)
    example(args.resource_name, args.topology, args.simulate, args.relay, args.action)


def test_example():
    example('', '2737/2-Wire 4x64 Matrix', True, 'kr0c0', 'OPEN')


def test_main():
    cmd_line = ['--topology', '2737/2-Wire 4x64 Matrix', '--simulate', '--relay', 'kr0c0']
    _main(cmd_line)


def main():
    _main(sys.argv[1:])


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niswitch/LATEST_RELEASE sha256=dd1b44562fc7c779fd9bef2e55d2e7b58783c4ca61885f5b549cd89de7e9a3fd bytes=7 -->
## FILE: src/niswitch/LATEST_RELEASE

- repository: `ni/nimi-python`
- source_path: `src/niswitch/LATEST_RELEASE`
- sha256: `dd1b44562fc7c779fd9bef2e55d2e7b58783c4ca61885f5b549cd89de7e9a3fd`
- bytes: 7

````text
1.4.9
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niswitch/metadata/__init__.py sha256=4b7b39cf71ea45690188c6523109d0f0f8d8fcd1aa92823d69a7a1554cb97ddc bytes=513 -->
## FILE: src/niswitch/metadata/__init__.py

- repository: `ni/nimi-python`
- source_path: `src/niswitch/metadata/__init__.py`
- sha256: `4b7b39cf71ea45690188c6523109d0f0f8d8fcd1aa92823d69a7a1554cb97ddc`
- bytes: 513

````python
from metadata.config import config
from metadata.functions import functions
from metadata.attributes import attributes
from metadata.enums import enums
import metadata.functions_addon
import metadata.attributes_addon
import metadata.enums_addon
import metadata.config_addon

import build.helper as helper
import sys

# Update generated functions data with hand maintained data
config['modules'] = sys.modules
helper.add_all_metadata(functions, attributes, enums, config)

__version__ = config['module_version']
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niswitch/metadata/attributes.py sha256=3c431e3c4891f8de1fe8b51097b3bf837c368132b92138e29dd902c60c0c01c7 bytes=26765 -->
## FILE: src/niswitch/metadata/attributes.py

- repository: `ni/nimi-python`
- source_path: `src/niswitch/metadata/attributes.py`
- sha256: `3c431e3c4891f8de1fe8b51097b3bf837c368132b92138e29dd902c60c0c01c7`
- bytes: 26765

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-SWITCH API metadata version 25.0.0f94
attributes = {
    1050005: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether or not to simulate instrument driver I/O operations.  If  simulation is enabled, instrument driver functions perform range checking  and call Ivi_GetAttribute and Ivi_SetAttribute functions, but they do not  perform instrument I/O.  For output parameters that represent instrument  data, the instrument driver functions return calculated values.\nThe default value is VI_FALSE.   Use the niSwitch_InitWithOptions  function to override this value.\n'
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Simulate',
        'name': 'SIMULATE',
        'type': 'ViBoolean'
    },
    1050007: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis attribute indicates the Driver Setup string that the user  specified when initializing the driver.\nSome cases exist where the end-user must specify instrument driver  options at initialization time.  An example of this is specifying  a particular instrument model from among a family of instruments  that the driver supports.  This is useful when using simulation.   The end-user can specify driver-specific options through  the DriverSetup keyword in the optionsString parameter to the  niSwitch_InitWithOptions function, or through the IVI Configuration Utility.\nIf the user does not specify a Driver Setup string, this attribute returns an empty string.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:Driver Setup',
        'name': 'DRIVER_SETUP',
        'type': 'ViString'
    },
    1050203: {
        'access': 'read only',
        'documentation': {
            'description': '\nIndicates the number of channels that the specific instrument  driver supports.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Capabilities:Channel Count',
        'name': 'CHANNEL_COUNT',
        'type': 'ViInt32'
    },
    1050304: {
        'access': 'read only',
        'documentation': {
            'description': '\nIndicates the resource descriptor the driver  uses to identify the physical device.\nIf you initialize the driver with a logical name, this  attribute contains the resource descriptor that corresponds  to the entry in the IVI Configuration utility.\nIf you initialize the instrument driver with the resource  descriptor, this attribute contains that value.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:IO Resource Descriptor',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'type': 'ViString'
    },
    1050305: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string containing the logical name you specified when opening the  current IVI session.\nYou may pass a logical name to the niSwitch_init or  niSwitch_InitWithOptions functions.   The IVI Configuration utility must contain an entry for the logical name.   The logical name entry refers to a virtual instrument section in the  IVI Configuration file.  The virtual instrument section specifies a physical  device and initial user options.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:Logical Name',
        'name': 'LOGICAL_NAME',
        'type': 'ViString'
    },
    1050327: {
        'access': 'read only',
        'documentation': {
            'description': '\nContains a comma-separated list of supported instrument models.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models',
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'type': 'ViString'
    },
    1050510: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains the firmware revision information  for the instrument you are currently using.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Firmware Revision',
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'type': 'ViString'
    },
    1050511: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains the name of the instrument manufacturer you are currently  using.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Manufacturer',
        'name': 'INSTRUMENT_MANUFACTURER',
        'type': 'ViString'
    },
    1050512: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains the model number or name of the instrument that you  are currently using.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Model',
        'name': 'INSTRUMENT_MODEL',
        'type': 'ViString'
    },
    1050513: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains the name of the vendor that supplies this driver.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Driver Vendor',
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'type': 'ViString'
    },
    1050514: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains a brief description of the specific  driver.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Description',
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'type': 'ViString'
    },
    1050551: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains additional version information about this  instrument driver.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Revision',
        'name': 'SPECIFIC_DRIVER_REVISION',
        'type': 'ViString'
    },
    1150004: {
        'access': 'read only',
        'documentation': {
            'description': 'In a scan list, a semi-colon (;) is used to indicate that at that point in  the scan list, the scan engine should pause until a trigger is received  from the trigger input.  If that trigger is user generated through either  a hardware pulse or the Send SW Trigger operation, it is necessary for the  user to know  when the scan engine has reached such a state.'
        },
        'lv_property': 'Scanning Configuration:Is Waiting for Trigger?',
        'name': 'IS_WAITING_FOR_TRIG',
        'type': 'ViBoolean'
    },
    1150010: {
        'access': 'read-write',
        'documentation': {
            'description': 'Determines the behavior of the trigger Input.'
        },
        'enum': 'TriggerInputPolarity',
        'lv_property': 'Scanning Configuration:Trigger Input Polarity',
        'name': 'TRIGGER_INPUT_POLARITY',
        'type': 'ViInt32'
    },
    1150011: {
        'access': 'read-write',
        'enum': 'ScanAdvancedPolarity',
        'lv_property': 'Scanning Configuration:Scan Advanced Polarity',
        'name': 'SCAN_ADVANCED_POLARITY',
        'type': 'ViInt32'
    },
    1150013: {
        'access': 'read-write',
        'enum': 'HandshakingInitiation',
        'lv_property': 'Scanning Configuration:Handshaking Initiation',
        'name': 'HANDSHAKING_INITIATION',
        'type': 'ViInt32'
    },
    1150014: {
        'access': 'read only',
        'documentation': {
            'description': 'This attribute returns the number of relays.'
        },
        'lv_property': 'Module Characteristics:Number of Relays',
        'name': 'NUMBER_OF_RELAYS',
        'type': 'ViInt32'
    },
    1150015: {
        'access': 'read only',
        'documentation': {
            'description': 'This read-only attribute returns the serial number for the switch device  controlled by this instrument driver.  If the device does not return a  serial number, the driver returns the IVI_ERROR_ATTRIBUTE_NOT_SUPPORTED error.'
        },
        'lv_property': 'Module Characteristics:Serial Number',
        'name': 'SERIAL_NUMBER',
        'type': 'ViString'
    },
    1150016: {
        'access': 'read-write',
        'documentation': {
            'description': '\nThis property specifies whether to apply the pulse width filter to the  Trigger Input. Enabling the Digital Filter (VI_TRUE) prevents the switch  module from being triggered by pulses that are less than 150 ns on PXI  trigger lines 0–7.\nWhen Digital Filter is disabled (VI_FALSE), it is possible for the switch  module to be triggered by noise on the PXI trigger lines. If the device  triggering the switch is capable of sending pulses greater than 150 ns, you should not disable the Digital Filter.\n'
        },
        'lv_property': 'Scanning Configuration:Digital Filter Enable',
        'name': 'DIGITAL_FILTER_ENABLE',
        'type': 'ViBoolean'
    },
    1150017: {
        'access': 'read-write',
        'documentation': {
            'description': '\nThis property specifies whether to power down latching relays after  calling Wait For Debounce.\nWhen Power Down Latching Relays After Debounce is enabled (VI_TRUE),  a call to Wait For Debounce ensures that the relays are settled  and the latching relays are powered down.\n'
        },
        'lv_property': 'Module Characteristics:Power Down Latching Relays After Debounce',
        'name': 'POWER_DOWN_LATCHING_RELAYS_AFTER_DEBOUNCE',
        'type': 'ViBoolean'
    },
    1150018: {
        'access': 'read-write',
        'documentation': {
            'description': '\nEnables or disables sharing of an analog bus line so that multiple  NI SwitchBlock devices may connect to it simultaneously. To enable  multiple NI SwitchBlock devices to share an analog bus line, set this  attribute to VI_TRUE for each device on the channel that corresponds  with the shared analog bus line. The default value for all devices is  VI_FALSE, which disables sharing of the analog bus.\nRefer to the Using the Analog Bus on an NI SwitchBlock Carrier topic  in the NI Switches Help for more information about sharing the analog bus.\n'
        },
        'lv_property': 'Channel Configuration:Analog Bus Sharing Enable',
        'name': 'ANALOG_BUS_SHARING_ENABLE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    },
    1150019: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis attribute returns the temperature as read by the Switch module.     The units are degrees Celsius.\n'
        },
        'lv_property': 'Module Characteristics:Temperature',
        'name': 'TEMPERATURE',
        'type': 'ViReal64'
    },
    1250001: {
        'access': 'read-write',
        'documentation': {
            'description': 'This channel-based attribute specifies whether you want to identify the  channel as a source channel.  Typically, you set this attribute to VI_TRUE  when you attach the channel to a power supply, a function generator, or an  active measurement point on the unit under test, and you do not want to  connect the channel to another source.  The driver prevents source  channels from connecting to each other.  The niSwitch_Connect function  returns the NISWITCH_ERROR_ATTEMPT_TO_CONNECT_SOURCES when you attempt to  connect two channels that you identify as source channels.'
        },
        'lv_property': 'Channel Configuration:Is Source Channel',
        'name': 'IS_SOURCE_CHANNEL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    },
    1250002: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis attribute indicates whether the entire switch device has settled  since the last switching command.  A value of VI_TRUE indicates that all  signals going through the switch device are valid.\n'
        },
        'lv_property': 'Module Characteristics:Is Debounced',
        'name': 'IS_DEBOUNCED',
        'type': 'ViBoolean'
    },
    1250003: {
        'access': 'read-write',
        'documentation': {
            'description': '\nThis channel-based attribute specifies whether to reserve the channel for  internal path creation.  A channel that is available for internal path  creation is called a configuration channel.  The driver may use  configuration channels to create paths between two channels you specify in  the niSwitch_Connect function.  Configuration channels are not available  for external connections.\nSet this attribute to VI_TRUE to mark the channel as a configuration  channel.  Set this attribute to VI_FALSE to mark the channel as available  for external connections.\nAfter you identify a channel as a configuration channel, you cannot  use that channel for external connections.  The niSwitch_Connect function  returns the NISWITCH_ERROR_IS_CONFIGURATION_CHANNEL error when you attempt  to establish a connection between a configuration channel and any other  channel.\n'
        },
        'lv_property': 'Channel Configuration:Is Configuration Channel',
        'name': 'IS_CONFIGURATION_CHANNEL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    },
    1250004: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nThis channel-based attribute returns the maximum length of time from after  you make a connection until the signal flowing through the channel  settles. The units are seconds.\nthe greater value of the settling time and the value you specify as the  scan delay.\n',
            'note': 'NI PXI-2501/2503/2565/2590/2591 Users--the actual delay will always be'
        },
        'lv_property': 'Module Characteristics:Settling Time',
        'name': 'SETTLING_TIME',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1250005: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis channel-based attribute returns the bandwidth for the channel.\nThe units are hertz.\n'
        },
        'lv_property': 'Module Characteristics:Bandwidth',
        'name': 'BANDWIDTH',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250006: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis channel-based attribute returns the maximum DC voltage the channel  can switch.\nThe units are volts.\n'
        },
        'lv_property': 'Module Characteristics:Maximum DC Voltage',
        'name': 'MAX_DC_VOLTAGE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250007: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis channel-based attribute returns the maximum AC voltage the channel  can switch.\nThe units are volts RMS.\n'
        },
        'lv_property': 'Module Characteristics:Maximum AC Voltage',
        'name': 'MAX_AC_VOLTAGE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250008: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis channel-based attribute returns the maximum DC current the channel  can switch.\nThe units are amperes.\n'
        },
        'lv_property': 'Module Characteristics:Maximum Switching DC Current',
        'name': 'MAX_SWITCHING_DC_CURRENT',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250009: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis channel-based attribute returns the maximum AC current the channel  can switch.\nThe units are amperes RMS.\n'
        },
        'lv_property': 'Module Characteristics:Maximum Switching AC Current',
        'name': 'MAX_SWITCHING_AC_CURRENT',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250010: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis channel-based attribute returns the maximum DC current the channel  can carry.\nThe units are amperes.\n'
        },
        'lv_property': 'Module Characteristics:Maximum Carry DC Current',
        'name': 'MAX_CARRY_DC_CURRENT',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250011: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis channel-based attribute returns the maximum AC current the channel  can carry.\nThe units are amperes RMS.\n'
        },
        'lv_property': 'Module Characteristics:Maximum Carry AC Current',
        'name': 'MAX_CARRY_AC_CURRENT',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250012: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis channel-based attribute returns the maximum DC power the channel can  switch.\nThe units are watts.\n'
        },
        'lv_property': 'Module Characteristics:Maximum Switching DC Power',
        'name': 'MAX_SWITCHING_DC_POWER',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250013: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis channel-based attribute returns the maximum AC power the channel can  switch.\nThe units are volt-amperes.\n'
        },
        'lv_property': 'Module Characteristics:Maximum Switching AC Power',
        'name': 'MAX_SWITCHING_AC_POWER',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250014: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis channel-based attribute returns the maximum DC power the channel can  carry.\nThe units are watts.\n'
        },
        'lv_property': 'Module Characteristics:Maximum Carry DC Power',
        'name': 'MAX_CARRY_DC_POWER',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250015: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis channel-based attribute returns the maximum AC power the channel can  carry.\nThe units are volt-amperes.\n'
        },
        'lv_property': 'Module Characteristics:Maximum Carry AC Power',
        'name': 'MAX_CARRY_AC_POWER',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250016: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis channel-based attribute returns the characteristic impedance for the  channel.\nThe units are ohms.\n'
        },
        'lv_property': 'Module Characteristics:Characteristic Impedance',
        'name': 'CHARACTERISTIC_IMPEDANCE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250017: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis attribute returns the wire mode of the switch device.\nThis attribute affects the values of the NISWITCH_ATTR_NUM_OF_ROWS and  NISWITCH_ATTR_NUM_OF_COLUMNS attributes.   The actual number of input and  output lines on the switch device is fixed, but the number of channels  depends on how many lines constitute each channel.\n'
        },
        'grpc_enum': 'WireMode',
        'lv_property': 'Module Characteristics:Wire mode',
        'name': 'WIRE_MODE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1250018: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis attribute returns the number of channels on the row of a matrix or  scanner.  If the switch device is a scanner, this value is the number of  output channels.\nThe NISWITCH_ATTR_WIRE_MODE attribute affects the number of available  rows.  For example, if your device has 8 input lines and you use the  two-wire mode, then the number of columns you have available is 4.\n'
        },
        'lv_property': 'Matrix Configuration:Number of Rows',
        'name': 'NUM_OF_ROWS',
        'type': 'ViInt32'
    },
    1250019: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis attribute returns the number of channels on the column of a matrix or  scanner.  If the switch device is a scanner, this value is the number of  input channels.\nThe NISWITCH_ATTR_WIRE_MODE attribute affects the number of available  columns.  For example, if your device has 8 input lines and you use the  four-wire mode, then the number of columns you have available is 2.\n'
        },
        'lv_property': 'Matrix Configuration:Number of Columns',
        'name': 'NUM_OF_COLUMNS',
        'type': 'ViInt32'
    },
    1250020: {
        'access': 'read-write',
        'documentation': {
            'description': "\nThis attribute contains a scan list, which is a string that specifies  channel connections and trigger conditions.  The niSwitch_InitiateScan  function makes or breaks connections and waits for triggers according to  the instructions in the scan list.\nThe scan list is comprised of channel names that you separate with  special characters.  These special characters determine the operations the  scanner performs on the channels when it executes this scan list.\nTo create a path between two channels, use the following character between  the two channel names:\n-> (a dash followed by a '>' sign)\nExample:  'CH1->CH2' tells the switch to make a path from channel CH1 to channel  CH2.\nTo break or clear a path, use the following character as a prefix before  the path:\n~ (tilde)\nExample:  '~CH1->CH2' tells the switch to break the path from channel CH1 to  channel CH2.\nTo tell the switch device to wait for a trigger event, use the following  character as a separator between paths:\n; (semi-colon)\nExample:  'CH1->CH2;CH3->CH4' tells the switch to make the path from channel CH1  to channel CH2, wait for a trigger, and then make the path from CH3 to  CH4.\n"
        },
        'lv_property': 'Scanning Configuration:Scan List',
        'name': 'SCAN_LIST',
        'type': 'ViString'
    },
    1250021: {
        'access': 'read-write',
        'documentation': {
            'description': "\nThis attribute specifies what happens to existing connections that  conflict with the connections you make in a scan list.  For example, if  CH1 is already connected to CH2 and the scan list instructs the switch  device to connect CH1 to CH3, this attribute specifies what happens to the  connection between CH1 and CH2.\nIf the value of this attribute is NISWITCH_VAL_NONE, the switch device  takes no action on existing paths.  If the value is  NISWITCH_VAL_BREAK_BEFORE_MAKE, the switch device breaks conflicting paths  before making new ones.  If the value is NISWITCH_VAL_BREAK_AFTER_MAKE,  the switch device breaks conflicting paths after making new ones.\nMost switch devices support only one of the possible values.  In such  cases, this attribute serves as an indicator of the device's behavior.\n"
        },
        'enum': 'ScanMode',
        'lv_property': 'Scanning Configuration:Scan Mode',
        'name': 'SCAN_MODE',
        'type': 'ViInt32'
    },
    1250022: {
        'access': 'read-write',
        'documentation': {
            'description': '\nThis attribute specifies the source of the trigger for which the switch  device can wait when processing a scan list.  The switch device waits for  a trigger when it encounters a semi-colon in a scan list.  When the trigger  occurs, the switch device advances to the next entry in the scan list.\n'
        },
        'enum': 'TriggerInput',
        'lv_property': 'Scanning Configuration:Trigger Input',
        'name': 'TRIGGER_INPUT',
        'type': 'ViInt32'
    },
    1250023: {
        'access': 'read-write',
        'documentation': {
            'description': '\nThis attribute specifies the method you want to use to notify another  instrument that all signals going through the switch device have settled  following the processing of one entry in the scan list.\n'
        },
        'enum': 'ScanAdvancedOutput',
        'lv_property': 'Scanning Configuration:Scan Advanced Output',
        'name': 'SCAN_ADVANCED_OUTPUT',
        'type': 'ViInt32'
    },
    1250024: {
        'access': 'read only',
        'documentation': {
            'description': 'If VI_TRUE, the switch module is currently scanning through the scan list  (i.e. it is not in the Idle state). If VI_FALSE, the switch module is not  currently scanning through the scan list (i.e. it is in the Idle state).'
        },
        'lv_property': 'Scanning Configuration:Is Scanning',
        'name': 'IS_SCANNING',
        'type': 'ViBoolean'
    },
    1250025: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nThis attribute specifies the minimum amount of time the switch device  waits before it asserts the scan advanced output trigger after opening or  closing the switch.  The switch device always waits for debounce before  asserting the trigger. The units are seconds.\nthe greater value of the settling time and the value you specify as the  scan delay.\n',
            'note': 'NI PXI-2501/2503/2565/2590/2591 Users--the actual delay will always be'
        },
        'lv_property': 'Scanning Configuration:Scan Delay',
        'name': 'SCAN_DELAY',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1250026: {
        'access': 'read-write',
        'documentation': {
            'description': '\nWhen a switch device is scanning, the swich can either stop scanning when  the end of the scan (VI_FALSE) or continue scanning from the top of the  scan list again (VI_TRUE).\nNotice that if you set the scan to continuous (VI_TRUE), the Wait For Scan  Complete operation will always time out and you must call Abort to stop  the scan.\n'
        },
        'lv_property': 'Scanning Configuration:Continuous Scan',
        'name': 'CONTINUOUS_SCAN',
        'type': 'ViBoolean'
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niswitch/metadata/attributes_addon.py sha256=17a2127d02579d026109ae3070d68b679f75dfef78e81e17ee575a6a80fec153 bytes=201 -->
## FILE: src/niswitch/metadata/attributes_addon.py

- repository: `ni/nimi-python`
- source_path: `src/niswitch/metadata/attributes_addon.py`
- sha256: `17a2127d02579d026109ae3070d68b679f75dfef78e81e17ee575a6a80fec153`
- bytes: 201

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niswitch/metadata/config.py sha256=54d5ea22067c63b2907590197044ca1f2e6d7da77bbdf082267c9d962803b8b1 bytes=1295 -->
## FILE: src/niswitch/metadata/config.py

- repository: `ni/nimi-python`
- source_path: `src/niswitch/metadata/config.py`
- sha256: `54d5ea22067c63b2907590197044ca1f2e6d7da77bbdf082267c9d962803b8b1`
- bytes: 1295

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-SWITCH API metadata version 25.0.0f94
config = {
    'api_version': '25.0.0f94',
    'c_function_prefix': 'niSwitch_',
    'close_function': 'close',
    'context_manager_name': {
        'abort_function': 'AbortScan',
        'initiate_function': 'InitiateScan',
        'task': 'scan'
    },
    'custom_types': [
    ],
    'driver_name': 'NI-SWITCH',
    'extra_errors_used': [
        'InvalidRepeatedCapabilityError',
        'SelfTestError'
    ],
    'grpc_service_class_prefix': 'NiSwitch',
    'init_function': 'InitWithTopology',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'niswitch',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niswitch_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niswitch_64.dll',
                'type': 'cdll'
            }
        }
    },
    'module_name': 'niswitch',
    'repeated_capabilities': [
        {
            'prefix': '',
            'python_name': 'channels'
        }
    ],
    'session_class_description': 'An NI-SWITCH session to an NI switch module.',
    'session_handle_parameter_name': 'vi'
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niswitch/metadata/config_addon.py sha256=7a8b3bfc5168c40cb294c8415cda6f1a9999194ebf9e4500091321041b2b12d2 bytes=259 -->
## FILE: src/niswitch/metadata/config_addon.py

- repository: `ni/nimi-python`
- source_path: `src/niswitch/metadata/config_addon.py`
- sha256: `7a8b3bfc5168c40cb294c8415cda6f1a9999194ebf9e4500091321041b2b12d2`
- bytes: 259

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.4.10.dev0',
    'latest_runtime_version_tested_against': '2025 Q4',
    'initial_release_year': '2017',
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niswitch/metadata/enums.py sha256=79d37f17e525fea633973829afd5d83848f641f27c37a97d70ebafc3d57399a8 bytes=41151 -->
## FILE: src/niswitch/metadata/enums.py

- repository: `ni/nimi-python`
- source_path: `src/niswitch/metadata/enums.py`
- sha256: `79d37f17e525fea633973829afd5d83848f641f27c37a97d70ebafc3d57399a8`
- bytes: 41151

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-SWITCH API metadata version 25.0.0f94
enums = {
    'CabledModuleScanAdvancedBus': {
        'values': [
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig0\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG0',
                'value': 111
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig1\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG1',
                'value': 112
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig2\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG2',
                'value': 113
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig3\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG3',
                'value': 114
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig4\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG4',
                'value': 115
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig5\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG5',
                'value': 116
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig6\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG6',
                'value': 117
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig7\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG7',
                'value': 118
            }
        ]
    },
    'CabledModuleTriggerBus': {
        'values': [
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_PXI_TRIG0',
                'value': 111
            },
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_PXI_TRIG1',
                'value': 112
            },
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_PXI_TRIG2',
                'value': 113
            },
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_PXI_TRIG3',
                'value': 114
            },
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_PXI_TRIG4',
                'value': 115
            },
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_PXI_TRIG5',
                'value': 116
            },
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_PXI_TRIG6',
                'value': 117
            },
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_PXI_TRIG7',
                'value': 118
            }
        ]
    },
    'HandshakingInitiation': {
        'values': [
            {
                'documentation': {
                    'description': '\nThe `niSwitch Initiate\nScan <switchviref.chm::/niSwitch_Initiate_Scan.html>`__ VI does not\nreturn until the switch hardware is waiting for a trigger input. This\nensures that if you initiate the measurement device after calling the\n`niSwitch Initiate\nScan <switchviref.chm::/niSwitch_Initiate_Scan.html>`__ VI , the switch\nis sure to receive the first measurement complete (MC) signal sent by\nthe measurement device. The measurement device should be configured to\nfirst take a measurement, send MC, then wait for scanner advanced output\nsignal. Thus, the first MC of the measurement device initiates\nhandshaking.\n'
                },
                'name': 'NISWITCH_VAL_MEASUREMENT_DEVICE_INITIATED',
                'value': 0
            },
            {
                'documentation': {
                    'description': '\nThe `niSwitch Initiate\nScan <switchviref.chm::/niSwitch_Initiate_Scan.html>`__ VI returns\nimmediately after beginning scan list execution. It is assumed that the\nmeasurement device has already been configured and is waiting for the\nscanner advanced signal. The measurement should be configured to first\nwait for a trigger, then take a measurement. Thus, the first scanner\nadvanced output signal of the switch module initiates handshaking.\n'
                },
                'name': 'NISWITCH_VAL_SWITCH_INITIATED',
                'value': 1
            }
        ]
    },
    'MasterSlaveScanAdvancedBus': {
        'values': [
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig0\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG0',
                'value': 111
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig1\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG1',
                'value': 112
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig2\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG2',
                'value': 113
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig3\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG3',
                'value': 114
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig4\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG4',
                'value': 115
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig5\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG5',
                'value': 116
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig6\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG6',
                'value': 117
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig7\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG7',
                'value': 118
            }
        ]
    },
    'MasterSlaveTriggerBus': {
        'values': [
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig0\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG0',
                'value': 111
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig1\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG1',
                'value': 112
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig2\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG2',
                'value': 113
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig3\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG3',
                'value': 114
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig4\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG4',
                'value': 115
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig5\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG5',
                'value': 116
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig6\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG6',
                'value': 117
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the PXI\\_Trig7\nline before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_TRIG7',
                'value': 118
            }
        ]
    },
    'PathCapability': {
        'values': [
            {
                'documentation': {
                    'description': 'Path Available'
                },
                'name': 'NISWITCH_VAL_PATH_AVAILABLE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Path Exists'
                },
                'name': 'NISWITCH_VAL_PATH_EXISTS',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Path Unsupported'
                },
                'name': 'NISWITCH_VAL_PATH_UNSUPPORTED',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Resource in use'
                },
                'name': 'NISWITCH_VAL_RSRC_IN_USE',
                'python_name': 'RESOURCE_IN_USE',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Source conflict'
                },
                'name': 'NISWITCH_VAL_SOURCE_CONFLICT',
                'value': 5
            },
            {
                'documentation': {
                    'description': 'Channel not available'
                },
                'name': 'NISWITCH_VAL_CHANNEL_NOT_AVAILABLE',
                'value': 6
            }
        ]
    },
    'RelayAction': {
        'values': [
            {
                'documentation': {
                    'description': 'Open Relay'
                },
                'name': 'NISWITCH_VAL_OPEN_RELAY',
                'value': 20
            },
            {
                'documentation': {
                    'description': 'Close Relay'
                },
                'name': 'NISWITCH_VAL_CLOSE_RELAY',
                'value': 21
            }
        ]
    },
    'RelayContact': {
        'values': [
            {
                'name': 'NISWITCH_VAL_RELAYTEST_RELAY_CONTACT_0',
                'value': 0
            },
            {
                'name': 'NISWITCH_VAL_RELAYTEST_RELAY_CONTACT_1',
                'value': 1
            },
            {
                'name': 'NISWITCH_VAL_RELAYTEST_RELAY_CONTACT_2',
                'value': 2
            },
            {
                'name': 'NISWITCH_VAL_RELAYTEST_RELAY_CONTACT_3',
                'value': 3
            }
        ]
    },
    'RelayPosition': {
        'values': [
            {
                'documentation': {
                    'description': 'Open'
                },
                'name': 'NISWITCH_VAL_OPEN',
                'value': 10
            },
            {
                'documentation': {
                    'description': 'Closed'
                },
                'name': 'NISWITCH_VAL_CLOSED',
                'value': 11
            }
        ]
    },
    'ScanAdvancedOutput': {
        'values': [
            {
                'documentation': {
                    'description': 'The switch device does not produce a Scan Advanced Output trigger.'
                },
                'name': 'NISWITCH_VAL_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'External Trigger. The switch device produces the Scan Advanced Output  trigger on the external trigger output.'
                },
                'name': 'NISWITCH_VAL_EXTERNAL',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'The switch device produces the Scan Advanced Output on the PXI TRIG0 line.'
                },
                'name': 'NISWITCH_VAL_TTL0',
                'value': 111
            },
            {
                'documentation': {
                    'description': 'The switch device produces the Scan Advanced Output on the PXI TRIG1 line.'
                },
                'name': 'NISWITCH_VAL_TTL1',
                'value': 112
            },
            {
                'documentation': {
                    'description': 'The switch device produces the Scan Advanced Output on the PXI TRIG2 line.'
                },
                'name': 'NISWITCH_VAL_TTL2',
                'value': 113
            },
            {
                'documentation': {
                    'description': 'The switch device produces the Scan Advanced Output on the PXI TRIG3 line.'
                },
                'name': 'NISWITCH_VAL_TTL3',
                'value': 114
            },
            {
                'documentation': {
                    'description': 'The switch device produces the Scan Advanced Output on the PXI TRIG4 line.'
                },
                'name': 'NISWITCH_VAL_TTL4',
                'value': 115
            },
            {
                'documentation': {
                    'description': 'The switch device produces the Scan Advanced Output on the PXI TRIG5 line.'
                },
                'name': 'NISWITCH_VAL_TTL5',
                'value': 116
            },
            {
                'documentation': {
                    'description': 'The switch device produces the Scan Advanced Output on the PXI TRIG6 line.'
                },
                'name': 'NISWITCH_VAL_TTL6',
                'value': 117
            },
            {
                'documentation': {
                    'description': 'The switch device produces the Scan Advanced Output on the PXI TRIG7 line.'
                },
                'name': 'NISWITCH_VAL_TTL7',
                'value': 118
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the PXI\nStar trigger bus before processing the next entry in the scan list.\n'
                },
                'name': 'NISWITCH_VAL_PXI_STAR',
                'value': 125
            },
            {
                'documentation': {
                    'description': 'The switch device produces the Scan Advanced Output  trigger on the rear connector.'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR',
                'value': 1000
            },
            {
                'documentation': {
                    'description': 'The switch device produces the Scan Advanced Output  trigger on the front connector.'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR',
                'value': 1001
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the rear\nconnector module 1.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE1',
                'value': 1021
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the rear\nconnector module 2.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE2',
                'value': 1022
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the rear\nconnector module 3.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE3',
                'value': 1023
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the rear\nconnector module 4.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE4',
                'value': 1024
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the rear\nconnector module 5.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE5',
                'value': 1025
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the rear\nconnector module 6.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE6',
                'value': 1026
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the rear\nconnector module 7.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE7',
                'value': 1027
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the rear\nconnector module 8.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE8',
                'value': 1028
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Ouptut Trigger on the rear\nconnector module 9.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE9',
                'value': 1029
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the rear\nconnector module 10.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE10',
                'value': 1030
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the rear\nconnector module 11.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE11',
                'value': 1031
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the rear\nconnector module 12.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE12',
                'value': 1032
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the front\nconnector module 1.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE1',
                'value': 1041
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the front\nconnector module 2.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE2',
                'value': 1042
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the front\nconnector module 3.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE3',
                'value': 1043
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the front\nconnector module 4.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE4',
                'value': 1044
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the front\nconnector module 5.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE5',
                'value': 1045
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the front\nconnector module 6.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE6',
                'value': 1046
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the front\nconnector module 7.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE7',
                'value': 1047
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the front\nconnector module 8.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE8',
                'value': 1048
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the front\nconnector module 9.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE9',
                'value': 1049
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the front\nconnector module 10.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE10',
                'value': 1050
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the front\nconnector module 11.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE11',
                'value': 1051
            },
            {
                'documentation': {
                    'description': '\nThe switch module produces the Scan Advanced Output Trigger on the front\nconnector module 12.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE12',
                'value': 1052
            }
        ]
    },
    'ScanAdvancedPolarity': {
        'values': [
            {
                'documentation': {
                    'description': 'The trigger occurs on the rising edge of the signal.'
                },
                'name': 'NISWITCH_VAL_RISING_EDGE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The trigger occurs on the falling edge of the signal.'
                },
                'name': 'NISWITCH_VAL_FALLING_EDGE',
                'value': 1
            }
        ]
    },
    'ScanMode': {
        'values': [
            {
                'documentation': {
                    'description': 'No implicit action on connections when scanning.'
                },
                'name': 'NISWITCH_VAL_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'When scanning, the switch device breaks existing connections before  making new connections.'
                },
                'name': 'NISWITCH_VAL_BREAK_BEFORE_MAKE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'When scanning, the switch device breaks existing connections after making  new connections.'
                },
                'name': 'NISWITCH_VAL_BREAK_AFTER_MAKE',
                'value': 2
            }
        ]
    },
    'TriggerInput': {
        'values': [
            {
                'documentation': {
                    'description': 'Immediate Trigger. The switch device does not wait for a trigger before  processing the next entry in the scan list.'
                },
                'name': 'NISWITCH_VAL_IMMEDIATE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'External Trigger. The switch device waits until it receives a trigger  from an external source through the external trigger input before  processing the next entry in the scan list.'
                },
                'name': 'NISWITCH_VAL_EXTERNAL',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'The switch device waits until you call the niSwitch_SendSoftwareTrigger  function before processing the next entry in the scan list.'
                },
                'name': 'NISWITCH_VAL_SOFTWARE_TRIG',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'The switch device waits until it receives a trigger on the PXI TRIG0 line before processing the next entry in the scan list.'
                },
                'name': 'NISWITCH_VAL_TTL0',
                'value': 111
            },
            {
                'documentation': {
                    'description': 'The switch device waits until it receives a trigger on the PXI TRIG1 line before processing the next entry in the scan list.'
                },
                'name': 'NISWITCH_VAL_TTL1',
                'value': 112
            },
            {
                'documentation': {
                    'description': 'The switch device waits until it receives a trigger on the PXI TRIG2 line before processing the next entry in the scan list.'
                },
                'name': 'NISWITCH_VAL_TTL2',
                'value': 113
            },
            {
                'documentation': {
                    'description': 'The switch device waits until it receives a trigger on the PXI TRIG3 line before processing the next entry in the scan list.'
                },
                'name': 'NISWITCH_VAL_TTL3',
                'value': 114
            },
            {
                'documentation': {
                    'description': 'The switch device waits until it receives a trigger on the PXI TRIG4 line before processing the next entry in the scan list.'
                },
                'name': 'NISWITCH_VAL_TTL4',
                'value': 115
            },
            {
                'documentation': {
                    'description': 'The switch device waits until it receives a trigger on the PXI TRIG5 line before processing the next entry in the scan list.'
                },
                'name': 'NISWITCH_VAL_TTL5',
                'value': 116
            },
            {
                'documentation': {
                    'description': 'The switch device waits until it receives a trigger on the PXI TRIG6 line before processing the next entry in the scan list.'
                },
                'name': 'NISWITCH_VAL_TTL6',
                'value': 117
            },
            {
                'documentation': {
                    'description': 'The switch device waits until it receives a trigger on the PXI TRIG7 line before processing the next entry in the scan list.'
                },
                'name': 'NISWITCH_VAL_TTL7',
                'value': 118
            },
            {
                'documentation': {
                    'description': 'The switch device waits until it receives a trigger on the PXI STAR  trigger bus before processing the next entry in the scan list.'
                },
                'name': 'NISWITCH_VAL_PXI_STAR',
                'value': 125
            },
            {
                'documentation': {
                    'description': 'The switch device waits until it receives a trigger on the  rear connector.'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR',
                'value': 1000
            },
            {
                'documentation': {
                    'description': 'The switch device waits until it receives a trigger on the  front connector.'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR',
                'value': 1001
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the rear\nconnector module 1.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE1',
                'value': 1021
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the rear\nconnector module 2.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE2',
                'value': 1022
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the rear\nconnector module 3.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE3',
                'value': 1023
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the rear\nconnector module 4.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE4',
                'value': 1024
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the rear\nconnector module 5.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE5',
                'value': 1025
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the rear\nconnector module 6.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE6',
                'value': 1026
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the rear\nconnector module 7.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE7',
                'value': 1027
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the rear\nconnector module 8.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE8',
                'value': 1028
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the rear\nconnector module 9.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE9',
                'value': 1029
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the rear\nconnector module 10.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE10',
                'value': 1030
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the rear\nconnector module 11.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE11',
                'value': 1031
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the rear\nconnector module 12.\n'
                },
                'name': 'NISWITCH_VAL_REARCONNECTOR_MODULE12',
                'value': 1032
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the front\nconnector module 1.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE1',
                'value': 1041
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the front\nconnector module 2.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE2',
                'value': 1042
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the front\nconnector module 3.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE3',
                'value': 1043
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the front\nconnector module 4.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE4',
                'value': 1044
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the front\nconnector module 5.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE5',
                'value': 1045
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the front\nconnector module 6.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE6',
                'value': 1046
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the front\nconnector module 7.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE7',
                'value': 1047
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the front\nconnector module 8.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE8',
                'value': 1048
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the front\nconnector module 9.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE9',
                'value': 1049
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the front\nconnector module 10.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE10',
                'value': 1050
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the front\nconnector module 11.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE11',
                'value': 1051
            },
            {
                'documentation': {
                    'description': '\nThe switch module waits until it receives a trigger on the front\nconnector module 12.\n'
                },
                'name': 'NISWITCH_VAL_FRONTCONNECTOR_MODULE12',
                'value': 1052
            }
        ]
    },
    'TriggerInputPolarity': {
        'values': [
            {
                'documentation': {
                    'description': 'The trigger occurs on the rising edge of the signal.'
                },
                'name': 'NISWITCH_VAL_RISING_EDGE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The trigger occurs on the falling edge of the signal.'
                },
                'name': 'NISWITCH_VAL_FALLING_EDGE',
                'value': 1
            }
        ]
    },
    'TriggerMode': {
        'values': [
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_SINGLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_MASTER',
                'value': 1
            },
            {
                'documentation': {
                    'description': ''
                },
                'name': 'NISWITCH_VAL_SLAVE',
                'value': 2
            }
        ]
    },
    'WireMode': {
        'values': [
            {
                'name': 'NISWITCH_VAL_1_WIRE',
                'value': 1
            },
            {
                'name': 'NISWITCH_VAL_2_WIRE',
                'value': 2
            },
            {
                'name': 'NISWITCH_VAL_4_WIRE',
                'value': 4
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niswitch/metadata/enums_addon.py sha256=6679b48316d199674e91c7dc700f9768376a2671afeea80f4c06ac360cd41596 bytes=186 -->
## FILE: src/niswitch/metadata/enums_addon.py

- repository: `ni/nimi-python`
- source_path: `src/niswitch/metadata/enums_addon.py`
- sha256: `6679b48316d199674e91c7dc700f9768376a2671afeea80f4c06ac360cd41596`
- bytes: 186

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niswitch/metadata/functions.py sha256=d1a7c46b73e0e2362ebd114ca37b747c24ad52eb78c86077329cba1f222e04fa bytes=104110 -->
## FILE: src/niswitch/metadata/functions.py

- repository: `ni/nimi-python`
- source_path: `src/niswitch/metadata/functions.py`
- sha256: `d1a7c46b73e0e2362ebd114ca37b747c24ad52eb78c86077329cba1f222e04fa`
- bytes: 104110

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-SWITCH API metadata version 25.0.0f94
functions = {
    'AbortScan': {
        'documentation': {
            'description': '\nAborts the scan in progress. Initiate a scan with\nniSwitch_InitiateScan. If the switch module is not scanning,\nNISWITCH_ERROR_NO_SCAN_IN_PROGRESS error is returned.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': 'abort',
        'returns': 'ViStatus'
    },
    'CanConnect': {
        'documentation': {
            'description': '\nVerifies that a path between channel 1 and channel 2 can be created. If\na path is possible in the switch module, the availability of that path\nis returned given the existing connections. If the path is possible but\nin use, a NISWITCH_WARN_IMPLICIT_CONNECTION_EXISTS warning is\nreturned.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nInput one of the channel names of the desired path. Pass the other\nchannel name as the channel 2 parameter. Refer to Devices Overview for\nvalid channel names for the switch module. Examples of valid channel\nnames: ch0, com0, ab0, r1, c2, cjtemp Default value: ""\n'
                },
                'name': 'channel1',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nInput one of the channel names of the desired path. Pass the other\nchannel name as the channel 1 parameter. Refer to Devices Overview for\nvalid channel names for the switch module. Examples of valid channel\nnames: ch0, com0, ab0, r1, c2, cjtemp Default value: ""\n'
                },
                'name': 'channel2',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nIndicates whether a path is valid. Possible values include:\n\n- NISWITCH_VAL_PATH_AVAILABLE 1\n- NISWITCH_VAL_PATH_EXISTS 2\n- NISWITCH_VAL_PATH_UNSUPPORTED 3\n- NISWITCH_VAL_RSRC_IN_USE 4\n- NISWITCH_VAL_SOURCE_CONFLICT 5\n- NISWITCH_VAL_CHANNEL_NOT_AVAILABLE 6\n\nNotes: (1)\nNISWITCH_VAL_PATH_AVAILABLE indicates that the driver can create the\npath at this time. (2) NISWITCH_VAL_PATH_EXISTS indicates that the\npath already exists. (3) NISWITCH_VAL_PATH_UNSUPPORTED indicates that\nthe instrument is not capable of creating a path between the channels\nyou specify. (4) NISWITCH_VAL_RSRC_IN_USE indicates that although\nthe path is valid, the driver cannot create the path at this moment\nbecause the switch device is currently using one or more of the required\nchannels to create another path. You must destroy the other path before\ncreating this one. (5) NISWITCH_VAL_SOURCE_CONFLICT indicates that\nthe instrument cannot create a path because both channels are connected\nto a different source channel. (6)\nNISWITCH_VAL_CHANNEL_NOT_AVAILABLE indicates that the driver cannot\ncreate a path between the two channels because one of the channels is a\nconfiguration channel and thus unavailable for external connections.\n'
                },
                'enum': 'PathCapability',
                'name': 'pathCapability',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'Commit': {
        'documentation': {
            'description': '\nDownloads the configured scan list and trigger settings to hardware.\nCalling niSwitch_Commit optional as it is implicitly called during\nniSwitch_InitiateScan. Use niSwitch_Commit to arm triggers in a given\norder or to control when expensive hardware operations are performed.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Connect': {
        'documentation': {
            'description': '\nCreates a path between channel 1 and channel 2. The driver calculates\nand uses the shortest path between the two channels. Refer to Immediate\nOperations for information about Channel Usage types. If a path is not\navailable, the function returns one of the following errors: -\nNISWITCH_ERROR_EXPLICIT_CONNECTION_EXISTS, if the two channels are\nalready explicitly connected by calling either the niSwitch_Connect or\nniSwitch_SetPath function. -\nNISWITCH_ERROR_IS_CONFIGURATION_CHANNEL, if a channel is a\nconfiguration channel. Error elaboration contains information about\nwhich of the two channels is a configuration channel. -\nNISWITCH_ERROR_ATTEMPT_TO_CONNECT_SOURCES, if both channels are\nconnected to a different source. Error elaboration contains information\nabout sources channel 1 and 2 connect to. -\nNISWITCH_ERROR_CANNOT_CONNECT_TO_ITSELF, if channels 1 and 2 are\none and the same channel. - NISWITCH_ERROR_PATH_NOT_FOUND, if the\ndriver cannot find a path between the two channels. Note: Paths are\nbidirectional. For example, if a path exists between channels CH1 and\nCH2, then the path also exists between channels CH2 and CH1.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nInput one of the channel names of the desired path. Pass the other\nchannel name as the channel 2 parameter. Refer to Devices Overview for\nvalid channel names for the switch module. Examples of valid channel\nnames: ch0, com0, ab0, r1, c2, cjtemp Default value: None\n'
                },
                'name': 'channel1',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nInput one of the channel names of the desired path. Pass the other\nchannel name as the channel 1 parameter. Refer to Devices Overview for\nvalid channel names for the switch module. Examples of valid channel\nnames: ch0, com0, ab0, r1, c2, cjtemp Default value: None\n'
                },
                'name': 'channel2',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConnectMultiple': {
        'documentation': {
            'description': '\nCreates the connections between channels specified in Connection List.\nSpecify connections with two endpoints only or the explicit path between\ntwo endpoints. NI-SWITCH calculates and uses the shortest path between\nthe channels. Refer to Setting Source and Configuration Channels for\ninformation about channel usage types. In the event of an error,\nconnecting stops at the point in the list where the error occurred. If a\npath is not available, the function returns one of the following errors:\n- NISWITCH_ERROR_EXPLICIT_CONNECTION_EXISTS, if the two channels are\nalready explicitly connected. -\nNISWITCH_ERROR_IS_CONFIGURATION_CHANNEL, if a channel is a\nconfiguration channel. Error elaboration contains information about\nwhich of the two channels is a configuration channel. -\nNISWITCH_ERROR_ATTEMPT_TO_CONNECT_SOURCES, if both channels are\nconnected to a different source. Error elaboration contains information\nabout sources channel 1 and 2 to connect. -\nNISWITCH_ERROR_CANNOT_CONNECT_TO_ITSELF, if channels 1 and 2 are\none and the same channel. - NISWITCH_ERROR_PATH_NOT_FOUND, if the\ndriver cannot find a path between the two channels. Note: Paths are\nbidirectional. For example, if a path exists between channels ch1 and\nch2, then the path also exists between channels ch1 and ch2.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nConnection List specifies a list of connections between channels to\nmake. NI-SWITCH validates the connection list, and aborts execution of\nthe list if errors are returned. Refer to Connection and Disconnection\nList Syntax for valid connection list syntax and examples. Refer to\nDevices Overview for valid channel names for the switch module. Example\nof a valid connection list: c0 -> r1, [c2 -> r2 -> c3] In this example,\nr2 is a configuration channel. Default value: None\n'
                },
                'name': 'connectionList',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'Disable': {
        'documentation': {
            'description': '\nPlaces the switch module in a quiescent state where it has minimal or no\nimpact on the system to which it is connected. All channels are\ndisconnected and any scan in progress is aborted.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Disconnect': {
        'documentation': {
            'description': '\nThis function destroys the path between two channels that you create\nwith the niSwitch_Connect or niSwitch_SetPath function. If a path is\nnot connected or not available, the function returns the\nIVISWTCH_ERROR_NO_SUCH_PATH error.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nInput one of the channel names of the path to break. Pass the other\nchannel name as the channel 2 parameter. Refer to Devices Overview for\nvalid channel names for the switch module. Examples of valid channel\nnames: ch0, com0, ab0, r1, c2, cjtemp Default value: None\n'
                },
                'name': 'channel1',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nInput one of the channel names of the path to break. Pass the other\nchannel name as the channel 1 parameter. Refer to Devices Overview for\nvalid channel names for the switch module. Examples of valid channel\nnames: ch0, com0, ab0, r1, c2, cjtemp Default value: None\n'
                },
                'name': 'channel2',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisconnectAll': {
        'documentation': {
            'description': '\nBreaks all existing paths. If the switch module cannot break all paths,\nNISWITCH_WARN_PATH_REMAINS warning is returned.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisconnectMultiple': {
        'documentation': {
            'description': '\nBreaks the connections between channels specified in Disconnection List.\nIf no connections exist between channels, NI-SWITCH returns an error. In\nthe event of an error, the VI stops at the point in the list where the\nerror occurred.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nDisconnection List specifies a list of connections between channels to\nbreak. NI-SWITCH validates the disconnection list, and aborts execution\nof the list if errors are returned. Refer to Connection and\nDisconnection List Syntax for valid disconnection list syntax and\nexamples. Refer to Devices Overview for valid channel names for the\nswitch module. Example of a valid disconnection list: c0 -> r1, [c2 ->\nr2 -> c3] In this example, r2 is a configuration channel. Default value:\nNone\n'
                },
                'name': 'disconnectionList',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function queries the value of a ViBoolean attribute. You can use\nthis function to get the values of instrument specific attributes and\ninherent IVI attributes. If the attribute represents an instrument\nstate, this function performs instrument I/O in the following cases: -\nState caching is disabled for the entire session or for the particular\nattribute. - State caching is enabled and the currently cached value is\ninvalid.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSome attributes are unique per channel. For these, pass the name of the\nchannel. Other attributes are unique per switch device. Pass VI_NULL or\nan empty string for this parameter. Default Value: ""\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the ID of an attribute. From the function panel window, you can use\nthis control as follows. - Click on the control or press , , or , to\ndisplay a dialog box containing a hierarchical list of the available\nattributes. Attributes whose value cannot be set are dim. Help text is\nshown for each attribute. Select an attribute by double-clicking on it\nor by selecting it and then pressing . A ring control at the top of the\ndialog box allows you to see all IVI attributes or only the attributes\nof the ViInt32 type. If you choose to see all IVI attributes, the data\ntypes appear to the right of the attribute names in the list box. The\ndata types that are not consistent with this function are dim. If you\nselect an attribute data type that is dim, LabWindows/CVI transfers you\nto the function panel for the corresponding function that is consistent\nwith the data type. - If you want to enter a variable name, press to\nchange this ring control to a manual input box. - If the attribute in\nthis ring control has constants as valid values, you can view the\nconstants by moving to the Attribute Value control and pressing .\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Pass the address of a\nViBoolean variable. From the function panel window, you can use this\ncontrol as follows. - If the attribute currently showing in the\nAttribute ID ring control has constants as valid values, you can view a\nlist of the constants by pressing on this control. Select a value by\ndouble-clicking on it or by selecting it and then pressing .\n'
                },
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function queries the value of a ViInt32 attribute. You can use this\nfunction to get the values of instrument specific attributes and\ninherent IVI attributes. If the attribute represents an instrument\nstate, this function performs instrument I/O in the following cases: -\nState caching is disabled for the entire session or for the particular\nattribute. - State caching is enabled and the currently cached value is\ninvalid.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSome attributes are unique per channel. For these, pass the name of the\nchannel. Other attributes are unique per switch device. Pass VI_NULL or\nan empty string for this parameter. Default Value: ""\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the ID of an attribute. From the function panel window, you can use\nthis control as follows. - Click on the control or press , , or , to\ndisplay a dialog box containing a hierarchical list of the available\nattributes. Attributes whose value cannot be set are dim. Help text is\nshown for each attribute. Select an attribute by double-clicking on it\nor by selecting it and then pressing . A ring control at the top of the\ndialog box allows you to see all IVI attributes or only the attributes\nof the ViInt32 type. If you choose to see all IVI attributes, the data\ntypes appear to the right of the attribute names in the list box. The\ndata types that are not consistent with this function are dim. If you\nselect an attribute data type that is dim, LabWindows/CVI transfers you\nto the function panel for the corresponding function that is consistent\nwith the data type. - If you want to enter a variable name, press to\nchange this ring control to a manual input box. - If the attribute in\nthis ring control has constants as valid values, you can view the\nconstants by moving to the Attribute Value control and pressing .\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Pass the address of a\nViInt32 variable. From the function panel window, you can use this\ncontrol as follows. - If the attribute currently showing in the\nAttribute ID ring control has constants as valid values, you can view a\nlist of the constants by pressing on this control. Select a value by\ndouble-clicking on it or by selecting it and then pressing .\n'
                },
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function queries the value of a ViReal64 attribute. You can use\nthis function to get the values of instrument specific attributes and\ninherent IVI attributes. If the attribute represents an instrument\nstate, this function performs instrument I/O in the following cases: -\nState caching is disabled for the entire session or for the particular\nattribute. - State caching is enabled and the currently cached value is\ninvalid.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSome attributes are unique per channel. For these, pass the name of the\nchannel. Other attributes are unique per switch device. Pass VI_NULL or\nan empty string for this parameter. Default Value: ""\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the ID of an attribute. From the function panel window, you can use\nthis control as follows. - Click on the control or press , , or , to\ndisplay a dialog box containing a hierarchical list of the available\nattributes. Attributes whose value cannot be set are dim. Help text is\nshown for each attribute. Select an attribute by double-clicking on it\nor by selecting it and then pressing . A ring control at the top of the\ndialog box allows you to see all IVI attributes or only the attributes\nof the ViInt32 type. If you choose to see all IVI attributes, the data\ntypes appear to the right of the attribute names in the list box. The\ndata types that are not consistent with this function are dim. If you\nselect an attribute data type that is dim, LabWindows/CVI transfers you\nto the function panel for the corresponding function that is consistent\nwith the data type. - If you want to enter a variable name, press to\nchange this ring control to a manual input box. - If the attribute in\nthis ring control has constants as valid values, you can view the\nconstants by moving to the Attribute Value control and pressing .\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Pass the address of a\nViReal64 variable. From the function panel window, you can use this\ncontrol as follows. - If the attribute currently showing in the\nAttribute ID ring control has constants as valid values, you can view a\nlist of the constants by pressing on this control. Select a value by\ndouble-clicking on it or by selecting it and then pressing .\n'
                },
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function queries the value of a ViString attribute. You can use\nthis function to get the values of instrument specific attributes and\ninherent IVI attributes. If the attribute represents an instrument\nstate, this function performs instrument I/O in the following cases: -\nState caching is disabled for the entire session or for the particular\nattribute. - State caching is enabled and the currently cached value is\ninvalid. You must provide a ViChar array to serve as a buffer for the\nvalue. You pass the number of bytes in the buffer as the Array Size\nparameter. If the current value of the attribute, including the\nterminating NULL byte, is larger than the size you indicate in the Array\nSize parameter, the function copies Array Size-1 bytes into the buffer,\nplaces an ASCII NULL byte at the end of the buffer, and returns the\narray size you must pass to get the entire value. For example, if the\nvalue is "123456" and the Array Size is 4, the function places "123"\ninto the buffer and returns 7. If you want to call this function just to\nget the required array size, you can pass 0 for the Array Size and\nVI_NULL for the Attribute Value buffer. If you want the function to\nfill in the buffer regardless of the number of bytes in the value, pass\na negative number for the Array Size parameter.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSome attributes are unique per channel. For these, pass the name of the\nchannel. Other attributes are unique per switch device. Pass VI_NULL or\nan empty string for this parameter. Default Value: ""\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the ID of an attribute. From the function panel window, you can use\nthis control as follows. - Click on the control or press , , or , to\ndisplay a dialog box containing a hierarchical list of the available\nattributes. Attributes whose value cannot be set are dim. Help text is\nshown for each attribute. Select an attribute by double-clicking on it\nor by selecting it and then pressing . A ring control at the top of the\ndialog box allows you to see all IVI attributes or only the attributes\nof the ViInt32 type. If you choose to see all IVI attributes, the data\ntypes appear to the right of the attribute names in the list box. The\ndata types that are not consistent with this function are dim. If you\nselect an attribute data type that is dim, LabWindows/CVI transfers you\nto the function panel for the corresponding function that is consistent\nwith the data type. - If you want to enter a variable name, press to\nchange this ring control to a manual input box. - If the attribute in\nthis ring control has constants as valid values, you can view the\nconstants by moving to the Attribute Value control and pressing .\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the number of bytes in the ViChar array you specify for the\nAttribute Value parameter. If the current value of the attribute,\nincluding the terminating NUL byte, contains more bytes that you\nindicate in this parameter, the function copies Array Size-1 bytes into\nthe buffer, places an ASCII NUL byte at the end of the buffer, and\nreturns the array size you must pass to get the entire value. For\nexample, if the value is "123456" and the Array Size is 4, the function\nplaces "123" into the buffer and returns 7. If you pass a negative\nnumber, the function copies the value to the buffer regardless of the\nnumber of bytes in the value. If you pass 0, you can pass VI_NULL for\nthe Attribute Value buffer parameter. Default Value:512\n'
                },
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe buffer in which the function returns the current value of the\nattribute. The buffer must be of type ViChar and have at least as many\nbytes as indicated in the Array Size parameter. If the current value of\nthe attribute, including the terminating NUL byte, contains more bytes\nthat you indicate in this parameter, the function copies Array Size-1\nbytes into the buffer, places an ASCII NUL byte at the end of the\nbuffer, and returns the array size you must pass to get the entire\nvalue. For example, if the value is "123456" and the Array Size is 4,\nthe function places "123" into the buffer and returns 7. If you specify\n0 for the Array Size parameter, you can pass VI_NULL for this\nparameter. From the function panel window, you can use this control as\nfollows. - If the attribute currently showing in the Attribute ID ring\ncontrol has constants as valid values, you can view a list of the\nconstants by pressing on this control. Select a value by double-clicking\non it or by selecting it and then pressing .\n'
                },
                'name': 'attributeValue',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetChannelName': {
        'documentation': {
            'description': '\nReturns the channel string that is in the channel table at the specified\nindex. Use niSwitch_GetChannelName in a For Loop to get a complete list\nof valid channel names for the switch module. Use the Channel Count\nattribute to determine the number of channels.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA 1-based index into the channel table. Default value: 1 Maximum value:\nValue of Channel Count attribute.\n'
                },
                'name': 'index',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the number of bytes in the ViChar array you specify for the Channel\nName Buffer parameter. If the channel name string, including the\nterminating NUL byte, contains more bytes than you indicate in this\nparameter, the function copies Buffer Size - 1 bytes into the buffer,\nplaces an ASCII NUL byte at the end of the buffer, and returns the\nbuffer size you must pass to get the entire value. For example, if the\nvalue is "123456" and the Buffer Size is 4, the function places "123"\ninto the buffer and returns 7. If you pass a negative number, the\nfunction copies the value to the buffer regardless of the number of\nbytes in the value. If you pass 0, you can pass VI_NULL for the\nCoercion Record buffer parameter. Default Value: None\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the channel name that is in the channel table at the index you\nspecify.\n'
                },
                'name': 'channelNameBuffer',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function retrieves and then clears the IVI error information for\nthe session or the current execution thread. One exception exists: If\nthe buffer_size parameter is 0, the function does not clear the error\ninformation. By passing 0 for the buffer size, the caller can ascertain\nthe buffer size required to get the entire error description string and\nthen call the function again with a sufficiently large buffer. If the\nuser specifies a valid IVI session for the InstrumentHandle parameter,\nGet Error retrieves and then clears the error information for the\nsession. If the user passes VI_NULL for the InstrumentHandle parameter,\nthis function retrieves and then clears the error information for the\ncurrent execution thread. If the InstrumentHandle parameter is an\ninvalid session, the function does nothing and returns an error.\nNormally, the error information describes the first error that occurred\nsince the user last called niSwitch_GetError or niSwitch_ClearError.\n'
        },
        'included_in_proto': True,
        'is_error_handling': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'none'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the error code for the session or execution thread. If you pass\n0 for the Buffer Size, you can pass VI_NULL for this parameter.\n'
                },
                'grpc_name': 'code',
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the number of bytes in the ViChar array you specify for the\nDescription parameter. If the error description, including the\nterminating NUL byte, contains more bytes than you indicate in this\nparameter, the function copies buffer_size - 1 bytes into the buffer,\nplaces an ASCII NUL byte at the end of the buffer, and returns the\nbuffer size you must pass to get the entire value. For example, if the\nvalue is "123456" and the Buffer Size is 4, the function places "123"\ninto the buffer and returns 7. If you pass a negative number, the\nfunction copies the value to the buffer regardless of the number of\nbytes in the value. If you pass 0, you can pass VI_NULL for the\nDescription buffer parameter. Default Value: None\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the error description for the IVI session or execution thread.\nIf there is no description, the function returns an empty string. The\nbuffer must contain at least as many elements as the value you specify\nwith the Buffer Size parameter. If the error description, including the\nterminating NUL byte, contains more bytes than you indicate with the\nBuffer Size parameter, the function copies Buffer Size - 1 bytes into\nthe buffer, places an ASCII NUL byte at the end of the buffer, and\nreturns the buffer size you must pass to get the entire value. For\nexample, if the value is "123456" and the Buffer Size is 4, the function\nplaces "123" into the buffer and returns 7. If you pass 0 for the Buffer\nSize, you can pass VI_NULL for this parameter.\n'
                },
                'name': 'description',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'GetPath': {
        'documentation': {
            'description': '\nReturns a string that identifies the explicit path created with\nniSwitch_Connect. Pass this string to niSwitch_SetPath to establish\nthe exact same path in future connections. In some cases, multiple paths\nare available between two channels. When you call niSwitch_Connect, the\ndriver selects an available path. With niSwitch_Connect, there is no\nguarantee that the driver selected path will always be the same path\nthrough the switch module. niSwitch_GetPath only returns those paths\nexplicitly created by niSwitch Connect Channels or niSwitch_SetPath.\nFor example, if you connect channels CH1 and CH3,and then channels CH2\nand CH3, an explicit path between channels CH1 and CH2 does not exist an\nerror is returned\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nInput one of the channel names of the desired path. Pass the other\nchannel name as the channel 2 parameter. Refer to Devices Overview for\nvalid channel names for the switch module. Examples of valid channel\nnames: ch0, com0, ab0, r1, c2, cjtemp Default value: ""\n'
                },
                'name': 'channel1',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nInput one of the channel names of the desired path. Pass the other\nchannel name as the channel 1 parameter. Refer to Devices Overview for\nvalid channel names for the switch module. Examples of valid channel\nnames: ch0, com0, ab0, r1, c2, cjtemp Default value: ""\n'
                },
                'name': 'channel2',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the number of bytes in the ViChar array you specify for the Path\nList parameter. If the current value of the attribute, including the\nterminating NULL byte, contains more bytes that you indicate in this\nparameter, the function copies Buffer Size - 1 bytes into the buffer,\nplaces an ASCII NULL byte at the end of the buffer, and returns the\nbuffer size you must pass to get the entire value. For example, if the\nvalue is "R1->C1" and the Buffer Size is 4, the function places "R1-"\ninto the buffer and returns 7. If you pass 0, you can pass VI_NULL for\nthe Path parameter. This enables you to find out the path size and to\nallocate the buffer of the appropriate size before calling this function\nagain.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nA string composed of comma-separated paths between channel 1 and channel\n2. The first and last names in the path are the endpoints of the path.\nAll other channels in the path are configuration channels. Examples of\nreturned paths: ch0->com0, com0->ab0\n'
                },
                'name': 'path',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetRelayCount': {
        'documentation': {
            'description': '\nReturns the number of times the relay has changed from Closed to Open.\nRelay count is useful for tracking relay lifetime and usage. Call\nniSwitch_WaitForDebounce before niSwitch_GetRelayCount to ensure an\naccurate count. Refer to the Relay Count topic in the NI Switches Help\nto determine if the switch module supports relay counting.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nName of the relay. Default value: None Examples of valid relay names:\nch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid\nrelay names for the switch module.\n'
                },
                'name': 'relayName',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The number of relay cycles.'
                },
                'name': 'relayCount',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetRelayName': {
        'documentation': {
            'description': '\nReturns the relay name string that is in the relay list at the specified\nindex. Use niSwitch_GetRelayName in a For Loop to get a complete list\nof valid relay names for the switch module. Use the Number of Relays\nattribute to determine the number of relays.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA 1-based index into the channel table. Default value: 1 Maximum value:\nValue of Channel Count attribute.\n'
                },
                'name': 'index',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the number of bytes in the ViChar array you specify for the Relay\nName Buffer parameter. If the relay name string, including the\nterminating NUL byte, contains more bytes than you indicate in this\nparameter, the function copies Buffer Size - 1 bytes into the buffer,\nplaces an ASCII NUL byte at the end of the buffer, and returns the\nbuffer size you must pass to get the entire value. For example, if the\nvalue is "123456" and the Buffer Size is 4, the function places "123"\ninto the buffer and returns 7. If you pass a negative number, the\nfunction copies the value to the buffer regardless of the number of\nbytes in the value. If you pass 0, you can pass VI_NULL for the\nCoercion Record buffer parameter. Default Value: None\n'
                },
                'name': 'relayNameBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the relay name for the index you specify.'
                },
                'name': 'relayNameBuffer',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'relayNameBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetRelayPosition': {
        'documentation': {
            'description': '\nReturns the relay position for the relay specified in the Relay Name\nparameter.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nName of the relay. Default value: None Examples of valid relay names:\nch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid\nrelay names for the switch module.\n'
                },
                'name': 'relayName',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nIndicates whether the relay is open or closed. NISWITCH_VAL_OPEN 10\nNISWITCH_VAL_CLOSED 11\n'
                },
                'enum': 'RelayPosition',
                'name': 'relayPosition',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitWithTopology': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns a session handle used to identify the switch in all subsequent\ninstrument driver calls and sets the topology of the switch.\nniSwitch_InitWithTopology creates a new IVI instrument driver session\nfor the switch specified in the resourceName parameter. The driver uses\nthe topology specified in the topology parameter and overrides the\ntopology specified in MAX. Note: When initializing an NI SwitchBlock\ndevice with topology, you must specify the topology created when you\nconfigured the device in MAX, using either\n"Configured Topology" or the topology string of the\ndevice. Refer to the Initializing with Topology for NI SwitchBlock\nDevices topic in the NI Switches Help for information about determining\nthe topology string of an NI SwitchBlock device. By default, the switch\nis reset to a known state. Enable simulation by specifying the topology\nand setting the simulate parameter to VI_TRUE.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': '__init__',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'initialization_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nResource name of the switch module to initialize. Default value: None\nSyntax: Optional fields are shown in square brackets ([]). Configured in\nMAX Under Valid Syntax Devices and Interfaces DeviceName Traditional\nNI-DAQ Devices SCXI[chassis ID]::slot number PXI System PXI[bus\nnumber]::device number TIP: IVI logical names are also valid for the\nresource name. Default values for optional fields: chassis ID = 1 bus\nnumber = 0 Example resource names: Resource Name Description SC1Mod3\nNI-DAQmx module in chassis "SC1" slot 3 MySwitch NI-DAQmx module renamed\nto "MySwitch" SCXI1::3 Traditional NI-DAQ module in chassis 1, slot 3\nSCXI::3 Traditional NI-DAQ module in chassis 1, slot 3 PXI0::16 PXI bus\n0, device number 16 PXI::16 PXI bus 0, device number 16\n'
                },
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'default_value': '"Configured Topology"',
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the topology name you want to use for the switch you specify with\nResource Name parameter. You can also pass\n"Configured Topology" to use the last topology that\nwas configured for the device in MAX.\nDefault Value:\n"Configured Topology"\nValid Values:\n"Configured Topology"\n"2501/1-Wire 48x1 Mux"\n"2501/1-Wire 48x1 Amplified Mux"\n"2501/2-Wire 24x1 Mux"\n"2501/2-Wire 24x1 Amplified Mux"\n"2501/2-Wire Dual 12x1 Mux"\n"2501/2-Wire Quad 6x1 Mux"\n"2501/2-Wire 4x6 Matrix"\n"2501/4-Wire 12x1 Mux"\n"2503/1-Wire 48x1 Mux"\n"2503/2-Wire 24x1 Mux"\n"2503/2-Wire Dual 12x1 Mux"\n"2503/2-Wire Quad 6x1 Mux"\n"2503/2-Wire 4x6 Matrix"\n"2503/4-Wire 12x1 Mux"\n"2510/Independent"\n"2512/Independent"\n"2514/Independent"\n"2515/Independent"\n"2520/80-SPST"\n"2521/40-DPST"\n"2522/53-SPDT"\n"2523/26-DPDT"\n"2524/1-Wire 128x1 Mux"\n"2524/1-Wire Dual 64x1 Mux"\n"2524/1-Wire Quad 32x1 Mux"\n"2524/1-Wire Octal 16x1 Mux"\n"2524/1-Wire Sixteen 8x1 Mux"\n"2525/2-Wire 64x1 Mux"\n"2525/2-Wire Dual 32x1 Mux"\n"2525/2-Wire Quad 16x1 Mux"\n"2525/2-Wire Octal 8x1 Mux"\n"2525/2-Wire Sixteen 4x1 Mux"\n"2526/1-Wire 158x1 Mux"\n"2526/2-Wire 79x1 Mux"\n"2527/1-Wire 64x1 Mux"\n"2527/1-Wire Dual 32x1 Mux"\n"2527/2-Wire 32x1 Mux"\n"2527/2-Wire Dual 16x1 Mux"\n"2527/4-Wire 16x1 Mux"\n"2527/Independent"\n"2529/2-Wire Dual 4x16 Matrix"\n"2529/2-Wire 8x16 Matrix"\n"2529/2-Wire 4x32 Matrix"\n"2530/1-Wire 128x1 Mux"\n"2530/1-Wire Dual 64x1 Mux"\n"2530/1-Wire 4x32 Matrix"\n"2530/1-Wire 8x16 Matrix"\n"2530/1-Wire Octal 16x1 Mux"\n"2530/1-Wire Quad 32x1 Mux"\n"2530/2-Wire 4x16 Matrix"\n"2530/2-Wire 64x1 Mux"\n"2530/2-Wire Dual 32x1 Mux"\n"2530/2-Wire Quad 16x1 Mux"\n"2530/4-Wire 32x1 Mux"\n"2530/4-Wire Dual 16x1 Mux"\n"2530/Independent"\n"2531/1-Wire 4x128 Matrix"\n"2531/1-Wire 8x64 Matrix"\n"2531/1-Wire Dual 4x64 Matrix"\n"2531/1-Wire Dual 8x32 Matrix"\n"2531/2-Wire 4x64 Matrix"\n"2531/2-Wire 8x32 Matrix"\n"2532/1-Wire 16x32 Matrix"\n"2532/1-Wire 4x128 Matrix"\n"2532/1-Wire 8x64 Matrix"\n"2532/1-Wire Dual 16x16 Matrix"\n"2532/1-Wire Dual 4x64 Matrix"\n"2532/1-Wire Dual 8x32 Matrix"\n"2532/1-Wire Quad 4x32 Matrix"\n"2532/1-Wire Sixteen 2x16 Matrix"\n"2532/2-Wire 16x16 Matrix"\n"2532/2-Wire 4x64 Matrix"\n"2532/2-Wire 8x32 Matrix"\n"2532/2-Wire Dual 4x32 Matrix"\n"2533/1-Wire 4x64 Matrix"\n"2534/1-Wire 8x32 Matrix"\n"2535/1-Wire 4x136 Matrix"\n"2536/1-Wire 8x68 Matrix"\n"2540/1-Wire 8x9 Matrix"\n"2541/1-Wire 8x12 Matrix"\n"2542/Quad 2x1 Terminated Mux"\n"2543/Dual 4x1 Terminated Mux"\n"2544/8x1 Terminated Mux"\n"2545/4x1 Terminated Mux"\n"2546/Dual 4x1 Mux"\n"2547/8x1 Mux"\n"2548/4-SPDT"\n"2549/Terminated 2-SPDT"\n"2554/4x1 Mux"\n"2555/4x1 Terminated Mux"\n"2556/Dual 4x1 Mux"\n"2557/8x1 Mux"\n"2558/4-SPDT"\n"2559/Terminated 2-SPDT"\n"2564/16-SPST"\n"2564/8-DPST"\n"2565/16-SPST"\n"2566/16-SPDT"\n"2566/8-DPDT"\n"2567/Independent"\n"2568/15-DPST"\n"2568/31-SPST"\n"2569/100-SPST"\n"2569/50-DPST"\n"2570/20-DPDT"\n"2570/40-SPDT"\n"2571/66-SPDT"\n"2575/1-Wire 196x1 Mux"\n"2575/2-Wire 98x1 Mux"\n"2575/2-Wire 95x1 Mux"\n"2576/2-Wire 64x1 Mux"\n"2576/2-Wire Dual 32x1 Mux"\n"2576/2-Wire Octal 8x1 Mux"\n"2576/2-Wire Quad 16x1 Mux"\n"2576/2-Wire Sixteen 4x1 Mux"\n"2576/Independent"\n"2584/1-Wire 12x1 Mux"\n"2584/1-Wire Dual 6x1 Mux"\n"2584/2-Wire 6x1 Mux"\n"2584/Independent"\n"2585/1-Wire 10x1 Mux"\n"2586/10-SPST"\n"2586/5-DPST"\n"2590/4x1 Mux"\n"2591/4x1 Mux"\n"2593/16x1 Mux"\n"2593/8x1 Terminated Mux"\n"2593/Dual 8x1 Mux"\n"2593/Dual 4x1 Terminated Mux"\n"2593/Independent"\n"2594/4x1 Mux"\n"2595/4x1 Mux"\n"2596/Dual 6x1 Mux"\n"2597/6x1 Terminated Mux"\n"2598/Dual Transfer"\n"2599/2-SPDT"\n"2720/Independent"\n"2722/Independent"\n"2725/Independent"\n"2727/Independent"\n"2737/2-Wire 4x64 Matrix"\n"2738/2-Wire 8x32 Matrix"\n"2739/2-Wire 16x16 Matrix"\n"2746/Quad 4x1 Mux"\n"2747/Dual 8x1 Mux"\n"2748/16x1 Mux"\n"2790/Independent"\n"2796/Dual 6x1 Mux"\n"2797/6x1 Terminated Mux"\n"2798/Dual Transfer"\n"2799/2-SPDT"\n'
                },
                'name': 'topology',
                'type': 'ViConstString'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': "\nEnables simulation of the switch module specified in the resource name\nparameter. Valid Values: VI_TRUE - simulate VI_FALSE - Don't simulate\n(Default Value)\n"
                },
                'name': 'simulate',
                'type': 'ViBoolean'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether to reset the switch module during the initialization\nprocess. Valid Values: VI_TRUE - Reset Device (Default Value) VI_FALSE\n- Currently unsupported. The device will not reset.\n'
                },
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'default_value': '""',
                'direction': 'out',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'InitiateScan': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nCommits the configured scan list and trigger settings to hardware and\ninitiates the scan. If niSwitch Commit was called earlier, niSwitch\nInitiate Scan only initiates the scan and returns immediately. Once the\nscanning operation begins, you cannot perform any other operation other\nthan GetAttribute, AbortScan, or SendSoftwareTrigger. All other\nfunctions return NISWITCH_ERROR_SCAN_IN_PROGRESS. To stop the\nscanning operation, To stop the scanning operation, call\nniSwitch_AbortScan.\n'
        },
        'included_in_proto': True,
        'method_name_for_documentation': 'initiate',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'LockSession': {
        'documentation': {
            'description': "\nThis function obtains a multithread lock on the instrument session.\nBefore it does so, it waits until all other execution threads have\nreleased their locks on the instrument session. Other threads might have\nobtained a lock on this session in the following ways: - The user's\napplication called niSwitch_LockSession. - A call to the instrument\ndriver locked the session. - A call to the IVI engine locked the\nsession. After your call to niSwitch_LockSession returns successfully,\nno other threads can access the instrument session until you call\nniSwitch_UnlockSession. Use niSwitch_LockSession and\nniSwitch_UnlockSession around a sequence of calls to instrument driver\nfunctions if you require that the instrument retain its settings through\nthe end of the sequence. You can safely make nested calls to\nniSwitch_LockSession within the same thread. To completely unlock the\nsession, you must balance each call to niSwitch_LockSession with a call\nto niSwitch_UnlockSession. If, however, you use the Caller Has Lock\nparameter in all calls to niSwitch_LockSession and\nniSwitch_UnlockSession within a function, the IVI Library locks the\nsession only once within the function regardless of the number of calls\nyou make to niSwitch_LockSession. This allows you to call\nniSwitch_UnlockSession just once at the end of the function.\n"
        },
        'included_in_proto': False,
        'method_templates': [
            {
                'documentation_filename': 'lock',
                'library_interpreter_filename': 'lock',
                'method_python_name_suffix': '',
                'session_filename': 'lock'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter serves as a convenience. If you do not want to use this\nparameter, pass VI_NULL. Use this parameter in complex functions to\nkeep track of whether you obtain a lock and therefore need to unlock the\nsession. Pass the address of a local ViBoolean variable. In the\ndeclaration of the local variable, initialize it to VI_FALSE. Pass the\naddress of the same local variable to any other calls you make to\nniSwitch_LockSession or niSwitch_UnlockSession in the same function.\nThe parameter is an input/output parameter. niSwitch_LockSession and\nniSwitch_UnlockSession each inspect the current value and take the\nfollowing actions: - If the value is VI_TRUE, niSwitch_LockSession\ndoes not lock the session again. If the value is VI_FALSE,\nniSwitch_LockSession obtains the lock and sets the value of the\nparameter to VI_TRUE. - If the value is VI_FALSE,\nniSwitch_UnlockSession does not attempt to unlock the session. If the\nvalue is VI_TRUE, niSwitch_UnlockSession releases the lock and sets\nthe value of the parameter to VI_FALSE. Thus, you can, call\nniSwitch_UnlockSession at the end of your function without worrying\nabout whether you actually have the lock. Example: ViStatus TestFunc\n(ViSession vi, ViInt32 flags) { ViStatus error = VI_SUCCESS; ViBoolean\nhaveLock = VI_FALSE; if (flags & BIT_1) { viCheckErr(\nniSwitch_LockSession(vi, &haveLock;)); viCheckErr( TakeAction1(vi)); if\n(flags & BIT_2) { viCheckErr( niSwitch_UnlockSession(vi, &haveLock;));\nviCheckErr( TakeAction2(vi)); viCheckErr( niSwitch_LockSession(vi,\n&haveLock;); } if (flags & BIT_3) viCheckErr( TakeAction3(vi)); }\nError: /\\* At this point, you cannot really be sure that you have the\nlock. Fortunately, the haveLock variable takes care of that for you. \\*/\nniSwitch_UnlockSession(vi, &haveLock;); return error; }\n'
                },
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'python_name': 'lock',
        'render_in_session_base': True,
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'RelayControl': {
        'documentation': {
            'description': '\nControls individual relays of the switch. When controlling individual\nrelays, the protection offered by setting the usage of source channels\nand configuration channels, and by enabling or disabling analog bus\nsharing on the NI SwitchBlock, does not apply. Refer to the device book\nfor your switch in the NI Switches Help to determine if the switch\nsupports individual relay control.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nName of the relay. Default value: None Examples of valid relay names:\nch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid\nrelay names for the switch module.\n'
                },
                'name': 'relayName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether to open or close a given relay. Default value: Relay\nClose Defined values: NISWITCH_VAL_OPEN_RELAY\nNISWITCH_VAL_CLOSE_RELAY (Default Value)\n'
                },
                'enum': 'RelayAction',
                'name': 'relayAction',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetWithDefaults': {
        'documentation': {
            'description': '\nResets the switch module and applies initial user specified settings\nfrom the logical name used to initialize the session. If the session was\ncreated without a logical name, this function is equivalent to\nniSwitch_reset.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'RouteScanAdvancedOutput': {
        'documentation': {
            'description': '\nRoutes the scan advanced output trigger from a trigger bus line (TTLx)\nto the front or rear connector.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe scan advanced trigger destination. Valid locations are the\nNISWITCH_VAL_FRONTCONNECTOR and NISWITCH_VAL_REARCONNECTOR. Default\nvalue: NISWITCH_VAL_FRONTCONNECTOR\n'
                },
                'enum': 'ScanAdvancedOutput',
                'name': 'scanAdvancedOutputConnector',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe trigger line to route the scan advanced output trigger from the\nfront or rear connector. Select NISWITCH_VAL_NONE to break an existing\nroute. Default value: None Valid Values: NISWITCH_VAL_NONE\nNISWITCH_VAL_TTL0 NISWITCH_VAL_TTL1 NISWITCH_VAL_TTL2\nNISWITCH_VAL_TTL3 NISWITCH_VAL_TTL4 NISWITCH_VAL_TTL5\nNISWITCH_VAL_TTL6 NISWITCH_VAL_TTL7\n'
                },
                'enum': 'ScanAdvancedOutput',
                'name': 'scanAdvancedOutputBusLine',
                'type': 'ViInt32'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': '\nIf VI_TRUE, inverts the input trigger signal from falling to rising or\nvice versa. Default value: VI_FALSE\n'
                },
                'name': 'invert',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'RouteTriggerInput': {
        'documentation': {
            'description': '\nRoutes the input trigger from the front or rear connector to a trigger\nbus line (TTLx). To disconnect the route, call this function again and\nspecify None for trigger bus line parameter.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe location of the input trigger source on the switch module. Valid\nlocations are the NISWITCH_VAL_FRONTCONNECTOR and\nNISWITCH_VAL_REARCONNECTOR. Default value:\nNISWITCH_VAL_FRONTCONNECTOR\n'
                },
                'enum': 'TriggerInput',
                'name': 'triggerInputConnector',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe trigger line to route the input trigger. Select NISWITCH_VAL_NONE\nto break an existing route. Default value: None Valid Values:\nNISWITCH_VAL_NONE NISWITCH_VAL_TTL0 NISWITCH_VAL_TTL1\nNISWITCH_VAL_TTL2 NISWITCH_VAL_TTL3 NISWITCH_VAL_TTL4\nNISWITCH_VAL_TTL5 NISWITCH_VAL_TTL6 NISWITCH_VAL_TTL7\n'
                },
                'enum': 'TriggerInput',
                'name': 'triggerInputBusLine',
                'type': 'ViInt32'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': '\nIf VI_TRUE, inverts the input trigger signal from falling to rising or\nvice versa. Default value: VI_FALSE\n'
                },
                'name': 'invert',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SendSoftwareTrigger': {
        'documentation': {
            'description': '\nSends a software trigger to the switch module specified in the NI-SWITCH\nsession. When the trigger input is set to NISWITCH_VAL_SOFTWARE_TRIG\nthrough either the niSwitch_ConfigureScanTrigger or the\nNISWITCH_ATTR_TRIGGER_INPUT attribute, the scan does not proceed from\na semi-colon (wait for trigger) until niSwitch_SendSoftwareTrigger is\ncalled.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function sets the value of a ViBoolean attribute. This is a\nlow-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes. If the\nattribute represents an instrument state, this function performs\ninstrument I/O in the following cases: - State caching is disabled for\nthe entire session or for the particular attribute. - State caching is\nenabled and the currently cached value is invalid or is different than\nthe value you specify. This instrument driver contains high-level\nfunctions that set most of the instrument attributes. It is best to use\nthe high-level driver functions as much as possible. They handle order\ndependencies and multithread locking for you. In addition, they perform\nstatus checking only after setting all of the attributes. In contrast,\nwhen you set multiple attributes using the SetAttribute functions, the\nfunctions check the instrument status after each call. Also, when state\ncaching is enabled, the high-level functions that configure multiple\nattributes perform instrument I/O only for the attributes whose value\nyou change. Thus, you can safely call the high-level functions without\nthe penalty of redundant instrument I/O.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSome attributes are unique per channel. For these, pass the name of the\nchannel. Other attributes are unique per switch device. Pass VI_NULL or\nan empty string for this parameter. Default Value: ""\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the ID of an attribute. From the function panel window, you can use\nthis control as follows. - Click on the control or press , , or , to\ndisplay a dialog box containing a hierarchical list of the available\nattributes. Attributes whose value cannot be set are dim. Help text is\nshown for each attribute. Select an attribute by double-clicking on it\nor by selecting it and then pressing . Read-only attributes appear dim\nin the list box. If you select a read-only attribute, an error message\nappears. A ring control at the top of the dialog box allows you to see\nall IVI attributes or only the attributes of the ViInt32 type. If you\nchoose to see all IVI attributes, the data types appear to the right of\nthe attribute names in the list box. The data types that are not\nconsistent with this function are dim. If you select an attribute data\ntype that is dim, LabWindows/CVI transfers you to the function panel for\nthe corresponding function that is consistent with the data type. - If\nyou want to enter a variable name, press to change this ring control to\na manual input box. - If the attribute in this ring control has\nconstants as valid values, you can view the constants by moving to the\nAttribute Value control and pressing .\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the value to which you want to set the attribute. From the function\npanel window, you can use this control as follows. - If the attribute\ncurrently showing in the Attribute ID ring control has constants as\nvalid values, you can view a list of the constants by pressing on this\ncontrol. Select a value by double-clicking on it or by selecting it and\nthen pressing . Note: Some of the values might not be valid depending on\nthe current settings of the instrument session. Default Value: none\n'
                },
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function sets the value of a ViInt32 attribute. This is a low-level\nfunction that you can use to set the values of instrument-specific\nattributes and inherent IVI attributes. If the attribute represents an\ninstrument state, this function performs instrument I/O in the following\ncases: - State caching is disabled for the entire session or for the\nparticular attribute. - State caching is enabled and the currently\ncached value is invalid or is different than the value you specify. This\ninstrument driver contains high-level functions that set most of the\ninstrument attributes. It is best to use the high-level driver functions\nas much as possible. They handle order dependencies and multithread\nlocking for you. In addition, they perform status checking only after\nsetting all of the attributes. In contrast, when you set multiple\nattributes using the SetAttribute functions, the functions check the\ninstrument status after each call. Also, when state caching is enabled,\nthe high-level functions that configure multiple attributes perform\ninstrument I/O only for the attributes whose value you change. Thus, you\ncan safely call the high-level functions without the penalty of\nredundant instrument I/O.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSome attributes are unique per channel. For these, pass the name of the\nchannel. Other attributes are unique per switch device. Pass VI_NULL or\nan empty string for this parameter. Default Value: ""\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the ID of an attribute. From the function panel window, you can use\nthis control as follows. - Click on the control or press , , or , to\ndisplay a dialog box containing a hierarchical list of the available\nattributes. Attributes whose value cannot be set are dim. Help text is\nshown for each attribute. Select an attribute by double-clicking on it\nor by selecting it and then pressing . Read-only attributes appear dim\nin the list box. If you select a read-only attribute, an error message\nappears. A ring control at the top of the dialog box allows you to see\nall IVI attributes or only the attributes of the ViInt32 type. If you\nchoose to see all IVI attributes, the data types appear to the right of\nthe attribute names in the list box. The data types that are not\nconsistent with this function are dim. If you select an attribute data\ntype that is dim, LabWindows/CVI transfers you to the function panel for\nthe corresponding function that is consistent with the data type. - If\nyou want to enter a variable name, press to change this ring control to\na manual input box. - If the attribute in this ring control has\nconstants as valid values, you can view the constants by moving to the\nAttribute Value control and pressing .\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the value to which you want to set the attribute. From the function\npanel window, you can use this control as follows. - If the attribute\ncurrently showing in the Attribute ID ring control has constants as\nvalid values, you can view a list of the constants by pressing on this\ncontrol. Select a value by double-clicking on it or by selecting it and\nthen pressing . Note: Some of the values might not be valid depending on\nthe current settings of the instrument session. Default Value: none\n'
                },
                'grpc_enum': 'NiSwitchInt32AttributeValues',
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function sets the value of a ViReal64 attribute. This is a\nlow-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes. If the\nattribute represents an instrument state, this function performs\ninstrument I/O in the following cases: - State caching is disabled for\nthe entire session or for the particular attribute. - State caching is\nenabled and the currently cached value is invalid or is different than\nthe value you specify. This instrument driver contains high-level\nfunctions that set most of the instrument attributes. It is best to use\nthe high-level driver functions as much as possible. They handle order\ndependencies and multithread locking for you. In addition, they perform\nstatus checking only after setting all of the attributes. In contrast,\nwhen you set multiple attributes using the SetAttribute functions, the\nfunctions check the instrument status after each call. Also, when state\ncaching is enabled, the high-level functions that configure multiple\nattributes perform instrument I/O only for the attributes whose value\nyou change. Thus, you can safely call the high-level functions without\nthe penalty of redundant instrument I/O.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSome attributes are unique per channel. For these, pass the name of the\nchannel. Other attributes are unique per switch device. Pass VI_NULL or\nan empty string for this parameter. Default Value: ""\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the ID of an attribute. From the function panel window, you can use\nthis control as follows. - Click on the control or press , , or , to\ndisplay a dialog box containing a hierarchical list of the available\nattributes. Attributes whose value cannot be set are dim. Help text is\nshown for each attribute. Select an attribute by double-clicking on it\nor by selecting it and then pressing . Read-only attributes appear dim\nin the list box. If you select a read-only attribute, an error message\nappears. A ring control at the top of the dialog box allows you to see\nall IVI attributes or only the attributes of the ViInt32 type. If you\nchoose to see all IVI attributes, the data types appear to the right of\nthe attribute names in the list box. The data types that are not\nconsistent with this function are dim. If you select an attribute data\ntype that is dim, LabWindows/CVI transfers you to the function panel for\nthe corresponding function that is consistent with the data type. - If\nyou want to enter a variable name, press to change this ring control to\na manual input box. - If the attribute in this ring control has\nconstants as valid values, you can view the constants by moving to the\nAttribute Value control and pressing .\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the value to which you want to set the attribute. From the function\npanel window, you can use this control as follows. - If the attribute\ncurrently showing in the Attribute ID ring control has constants as\nvalid values, you can view a list of the constants by pressing on this\ncontrol. Select a value by double-clicking on it or by selecting it and\nthen pressing . Note: Some of the values might not be valid depending on\nthe current settings of the instrument session. Default Value: none\n'
                },
                'grpc_name': 'attribute_value_raw',
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function sets the value of a ViString attribute. This is a\nlow-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes. If the\nattribute represents an instrument state, this function performs\ninstrument I/O in the following cases: - State caching is disabled for\nthe entire session or for the particular attribute. - State caching is\nenabled and the currently cached value is invalid or is different than\nthe value you specify. This instrument driver contains high-level\nfunctions that set most of the instrument attributes. It is best to use\nthe high-level driver functions as much as possible. They handle order\ndependencies and multithread locking for you. In addition, they perform\nstatus checking only after setting all of the attributes. In contrast,\nwhen you set multiple attributes using the SetAttribute functions, the\nfunctions check the instrument status after each call. Also, when state\ncaching is enabled, the high-level functions that configure multiple\nattributes perform instrument I/O only for the attributes whose value\nyou change. Thus, you can safely call the high-level functions without\nthe penalty of redundant instrument I/O.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSome attributes are unique per channel. For these, pass the name of the\nchannel. Other attributes are unique per switch device. Pass VI_NULL or\nan empty string for this parameter. Default Value: ""\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the ID of an attribute. From the function panel window, you can use\nthis control as follows. - Click on the control or press , , or , to\ndisplay a dialog box containing a hierarchical list of the available\nattributes. Attributes whose value cannot be set are dim. Help text is\nshown for each attribute. Select an attribute by double-clicking on it\nor by selecting it and then pressing . Read-only attributes appear dim\nin the list box. If you select a read-only attribute, an error message\nappears. A ring control at the top of the dialog box allows you to see\nall IVI attributes or only the attributes of the ViInt32 type. If you\nchoose to see all IVI attributes, the data types appear to the right of\nthe attribute names in the list box. The data types that are not\nconsistent with this function are dim. If you select an attribute data\ntype that is dim, LabWindows/CVI transfers you to the function panel for\nthe corresponding function that is consistent with the data type. - If\nyou want to enter a variable name, press to change this ring control to\na manual input box. - If the attribute in this ring control has\nconstants as valid values, you can view the constants by moving to the\nAttribute Value control and pressing .\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the value to which you want to set the attribute. From the function\npanel window, you can use this control as follows. - If the attribute\ncurrently showing in the Attribute ID ring control has constants as\nvalid values, you can view a list of the constants by pressing on this\ncontrol. Select a value by double-clicking on it or by selecting it and\nthen pressing . Note: Some of the values might not be valid depending on\nthe current settings of the instrument session. Default Value: none\n'
                },
                'grpc_name': 'attribute_value_raw',
                'name': 'attributeValue',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetPath': {
        'documentation': {
            'description': '\nConnects two channels by specifying an explicit path in the path list\nparameter. niSwitch_SetPath is particularly useful where path\nrepeatability is important, such as in calibrated signal paths. If this\nis not necessary, use niSwitch_Connect.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA string composed of comma-separated paths between channel 1 and channel\n2. The first and last names in the path are the endpoints of the path.\nEvery other channel in the path are configuration channels. Example of a\nvalid path list string: ch0->com0, com0->ab0. In this example, com0 is a\nconfiguration channel. Default value: None Obtain the path list for a\npreviously created path with niSwitch_GetPath.\n'
                },
                'name': 'pathList',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetRuntimeEnvironment': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'TBD'
        },
        'included_in_proto': False,
        'method_templates': [
            {
                'documentation_filename': 'none',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'none'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'environment',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'environmentVersion',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'reserved1',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'reserved2',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnlockSession': {
        'documentation': {
            'description': '\nThis function releases a lock that you acquired on an instrument session\nusing niSwitch_LockSession. Refer to niSwitch_LockSession for\nadditional information on session locks.\n'
        },
        'included_in_proto': False,
        'method_templates': [
            {
                'documentation_filename': 'unlock',
                'library_interpreter_filename': 'unlock',
                'method_python_name_suffix': '',
                'session_filename': 'unlock'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter serves as a convenience. If you do not want to use this\nparameter, pass VI_NULL. Use this parameter in complex functions to\nkeep track of whether you obtain a lock and therefore need to unlock the\nsession. Pass the address of a local ViBoolean variable. In the\ndeclaration of the local variable, initialize it to VI_FALSE. Pass the\naddress of the same local variable to any other calls you make to\nniSwitch_LockSession or niSwitch_UnlockSession in the same function.\nThe parameter is an input/output parameter. niSwitch_LockSession and\nniSwitch_UnlockSession each inspect the current value and take the\nfollowing actions: - If the value is VI_TRUE, niSwitch_LockSession\ndoes not lock the session again. If the value is VI_FALSE,\nniSwitch_LockSession obtains the lock and sets the value of the\nparameter to VI_TRUE. - If the value is VI_FALSE,\nniSwitch_UnlockSession does not attempt to unlock the session. If the\nvalue is VI_TRUE, niSwitch_UnlockSession releases the lock and sets\nthe value of the parameter to VI_FALSE. Thus, you can, call\nniSwitch_UnlockSession at the end of your function without worrying\nabout whether you actually have the lock. Example: ViStatus TestFunc\n(ViSession vi, ViInt32 flags) { ViStatus error = VI_SUCCESS; ViBoolean\nhaveLock = VI_FALSE; if (flags & BIT_1) { viCheckErr(\nniSwitch_LockSession(vi, &haveLock;)); viCheckErr( TakeAction1(vi)); if\n(flags & BIT_2) { viCheckErr( niSwitch_UnlockSession(vi, &haveLock;));\nviCheckErr( TakeAction2(vi)); viCheckErr( niSwitch_LockSession(vi,\n&haveLock;); } if (flags & BIT_3) viCheckErr( TakeAction3(vi)); }\nError: /\\* At this point, you cannot really be sure that you have the\nlock. Fortunately, the haveLock variable takes care of that for you. \\*/\nniSwitch_UnlockSession(vi, &haveLock;); return error; }\n'
                },
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'python_name': 'unlock',
        'render_in_session_base': True,
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'WaitForDebounce': {
        'documentation': {
            'description': '\nPauses until all created paths have settled. If the time you specify\nwith the Maximum Time (ms) parameter elapsed before the switch paths\nhave settled, this function returns the\nNISWITCH_ERROR_MAX_TIME_EXCEEDED error.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'hightime.timedelta(milliseconds=5000)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the maximum length of time to wait for all relays in the\nswitch module to activate or deactivate. If the specified time elapses\nbefore all relays active or deactivate, a timeout error is returned.\nDefault Value:5000 ms\n'
                },
                'name': 'maximumTimeMs',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds_int32',
                'type': 'ViInt32',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or int in milliseconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'WaitForScanComplete': {
        'documentation': {
            'description': '\nPauses until the switch module stops scanning or the maximum time has\nelapsed and returns a timeout error. If the time you specify with the\nMaximum Time (ms) parameter elapsed before the scanning operation has\nfinished, this function returns the NISWITCH_ERROR_MAX_TIME_EXCEEDED\nerror.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'hightime.timedelta(milliseconds=5000)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the maximum length of time to wait for the switch module to\nstop scanning. If the specified time elapses before the scan ends,\nNISWITCH_ERROR_MAX_TIME_EXCEEDED error is returned. Default\nValue:5000 ms\n'
                },
                'name': 'maximumTimeMs',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds_int32',
                'type': 'ViInt32',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or int in milliseconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'close': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nTerminates the NI-SWITCH session and all of its attributes and\ndeallocates any memory resources the driver uses. Notes: (1) You must\nunlock the session before calling niSwitch_close. (2) After calling\nniSwitch_close, you cannot use the instrument driver again until you\ncall niSwitch_init or niSwitch_InitWithOptions.\n'
        },
        'grpc_name': 'Close',
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': '_close',
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'error_message': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nConverts an error code returned by NI-SWITCH into a user-readable\nstring. Generally this information is supplied in error out of any\nNI-SWITCH VI. Use niSwitch_error_message for a static lookup of an\nerror code description.\n'
        },
        'grpc_name': 'ErrorMessage',
        'included_in_proto': True,
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nStatus code returned by any NI-SWITCH function. Default Value: 0\n(VI_SUCCESS)\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe error information formatted into a string. You must pass a ViChar\narray with at least 256 bytes.\n'
                },
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'fancy_self_test': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nVerifies that the driver can communicate with the switch module.\n\nRaises `SelfTestError` on self test failure. Attributes on exception object:\n\n- code - failure code from driver\n- message - status message from driver\n',
            'table_body': [
                [
                    '0',
                    'Passed self-test'
                ],
                [
                    '1',
                    'Self-test failed'
                ]
            ],
            'table_header': [
                'Self-Test Code',
                'Description'
            ]
        },
        'grpc_name': 'FancySelfTest',
        'included_in_proto': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_self_test'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls.'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': 'self_test',
        'returns': 'ViStatus'
    },
    'reset': {
        'documentation': {
            'description': '\nDisconnects all created paths and returns the switch module to the state\nat initialization. Configuration channel and source channel settings\nremain unchanged.\n'
        },
        'grpc_name': 'Reset',
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'self_test': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Verifies that the driver can communicate with the switch module.'
        },
        'grpc_name': 'SelfTest',
        'included_in_proto': True,
        'method_name_for_documentation': 'self_test',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nA particular NI-SWITCH session established with\nniSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init\nand used for all subsequent NI-SWITCH calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Value returned from the switch device self-test. Passed 0 Failed 1'
                },
                'name': 'selfTestResult',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nSelf-test response string from the switch device. You must pass a ViChar\narray with at least 256 bytes.\n'
                },
                'name': 'selfTestMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niswitch/metadata/functions_addon.py sha256=46c53953df0069cf0ddc98438dda6c2fe2350e047331e0e9835f7c9362ba2597 bytes=236 -->
## FILE: src/niswitch/metadata/functions_addon.py

- repository: `ni/nimi-python`
- source_path: `src/niswitch/metadata/functions_addon.py`
- sha256: `46c53953df0069cf0ddc98438dda6c2fe2350e047331e0e9835f7c9362ba2597`
- bytes: 236

````python
# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niswitch/metadata/niswitch.proto sha256=0bd8ba3dddb6aa43c2aae22ee9ec7e5a66d408bd86a810b98cdae844440b2275 bytes=32524 -->
## FILE: src/niswitch/metadata/niswitch.proto

- repository: `ni/nimi-python`
- source_path: `src/niswitch/metadata/niswitch.proto`
- sha256: `0bd8ba3dddb6aa43c2aae22ee9ec7e5a66d408bd86a810b98cdae844440b2275`
- bytes: 32524

````protobuf

//---------------------------------------------------------------------
// This file is generated from NI-SWITCH API metadata version 25.0.0f94
//---------------------------------------------------------------------
// Proto file for the NI-SWITCH Metadata
//---------------------------------------------------------------------
syntax = "proto3";

option java_multiple_files = true;
option java_package = "com.ni.grpc.niswitch";
option java_outer_classname = "NiSwitch";
option csharp_namespace = "NationalInstruments.Grpc.Switch";

package niswitch_grpc;

import "session.proto";

service NiSwitch {
  rpc Init(InitRequest) returns (InitResponse);
  rpc InitWithOptions(InitWithOptionsRequest) returns (InitWithOptionsResponse);
  rpc InitWithTopology(InitWithTopologyRequest) returns (InitWithTopologyResponse);
  rpc Close(CloseRequest) returns (CloseResponse);
  rpc Connect(ConnectRequest) returns (ConnectResponse);
  rpc ConnectMultiple(ConnectMultipleRequest) returns (ConnectMultipleResponse);
  rpc Disconnect(DisconnectRequest) returns (DisconnectResponse);
  rpc DisconnectMultiple(DisconnectMultipleRequest) returns (DisconnectMultipleResponse);
  rpc DisconnectAll(DisconnectAllRequest) returns (DisconnectAllResponse);
  rpc GetPath(GetPathRequest) returns (GetPathResponse);
  rpc SetPath(SetPathRequest) returns (SetPathResponse);
  rpc CanConnect(CanConnectRequest) returns (CanConnectResponse);
  rpc IsDebounced(IsDebouncedRequest) returns (IsDebouncedResponse);
  rpc WaitForDebounce(WaitForDebounceRequest) returns (WaitForDebounceResponse);
  rpc Scan(ScanRequest) returns (ScanResponse);
  rpc InitiateScan(InitiateScanRequest) returns (InitiateScanResponse);
  rpc AbortScan(AbortScanRequest) returns (AbortScanResponse);
  rpc IsScanning(IsScanningRequest) returns (IsScanningResponse);
  rpc WaitForScanComplete(WaitForScanCompleteRequest) returns (WaitForScanCompleteResponse);
  rpc SendSoftwareTrigger(SendSoftwareTriggerRequest) returns (SendSoftwareTriggerResponse);
  rpc ConfigureScanList(ConfigureScanListRequest) returns (ConfigureScanListResponse);
  rpc ConfigureScanTrigger(ConfigureScanTriggerRequest) returns (ConfigureScanTriggerResponse);
  rpc SetContinuousScan(SetContinuousScanRequest) returns (SetContinuousScanResponse);
  rpc RouteTriggerInput(RouteTriggerInputRequest) returns (RouteTriggerInputResponse);
  rpc RouteScanAdvancedOutput(RouteScanAdvancedOutputRequest) returns (RouteScanAdvancedOutputResponse);
  rpc ErrorQuery(ErrorQueryRequest) returns (ErrorQueryResponse);
  rpc GetError(GetErrorRequest) returns (GetErrorResponse);
  rpc ClearError(ClearErrorRequest) returns (ClearErrorResponse);
  rpc ErrorMessage(ErrorMessageRequest) returns (ErrorMessageResponse);
  rpc GetChannelName(GetChannelNameRequest) returns (GetChannelNameResponse);
  rpc GetRelayName(GetRelayNameRequest) returns (GetRelayNameResponse);
  rpc GetRelayCount(GetRelayCountRequest) returns (GetRelayCountResponse);
  rpc GetRelayPosition(GetRelayPositionRequest) returns (GetRelayPositionResponse);
  rpc RelayControl(RelayControlRequest) returns (RelayControlResponse);
  rpc ResetInterchangeCheck(ResetInterchangeCheckRequest) returns (ResetInterchangeCheckResponse);
  rpc ClearInterchangeWarnings(ClearInterchangeWarningsRequest) returns (ClearInterchangeWarningsResponse);
  rpc Commit(CommitRequest) returns (CommitResponse);
  rpc ResetWithDefaults(ResetWithDefaultsRequest) returns (ResetWithDefaultsResponse);
  rpc Disable(DisableRequest) returns (DisableResponse);
  rpc Reset(ResetRequest) returns (ResetResponse);
  rpc SelfTest(SelfTestRequest) returns (SelfTestResponse);
  rpc RevisionQuery(RevisionQueryRequest) returns (RevisionQueryResponse);
  rpc GetAttributeViInt32(GetAttributeViInt32Request) returns (GetAttributeViInt32Response);
  rpc GetAttributeViReal64(GetAttributeViReal64Request) returns (GetAttributeViReal64Response);
  rpc GetAttributeViString(GetAttributeViStringRequest) returns (GetAttributeViStringResponse);
  rpc GetAttributeViSession(GetAttributeViSessionRequest) returns (GetAttributeViSessionResponse);
  rpc GetAttributeViBoolean(GetAttributeViBooleanRequest) returns (GetAttributeViBooleanResponse);
  rpc SetAttributeViInt32(SetAttributeViInt32Request) returns (SetAttributeViInt32Response);
  rpc SetAttributeViReal64(SetAttributeViReal64Request) returns (SetAttributeViReal64Response);
  rpc SetAttributeViString(SetAttributeViStringRequest) returns (SetAttributeViStringResponse);
  rpc SetAttributeViSession(SetAttributeViSessionRequest) returns (SetAttributeViSessionResponse);
  rpc SetAttributeViBoolean(SetAttributeViBooleanRequest) returns (SetAttributeViBooleanResponse);
  rpc CheckAttributeViInt32(CheckAttributeViInt32Request) returns (CheckAttributeViInt32Response);
  rpc CheckAttributeViReal64(CheckAttributeViReal64Request) returns (CheckAttributeViReal64Response);
  rpc CheckAttributeViString(CheckAttributeViStringRequest) returns (CheckAttributeViStringResponse);
  rpc CheckAttributeViSession(CheckAttributeViSessionRequest) returns (CheckAttributeViSessionResponse);
  rpc CheckAttributeViBoolean(CheckAttributeViBooleanRequest) returns (CheckAttributeViBooleanResponse);
  rpc InvalidateAllAttributes(InvalidateAllAttributesRequest) returns (InvalidateAllAttributesResponse);
}

enum NiSwitchAttribute {
  NISWITCH_ATTRIBUTE_UNSPECIFIED = 0;
  NISWITCH_ATTRIBUTE_RANGE_CHECK = 1050002;
  NISWITCH_ATTRIBUTE_QUERY_INSTRUMENT_STATUS = 1050003;
  NISWITCH_ATTRIBUTE_CACHE = 1050004;
  NISWITCH_ATTRIBUTE_SIMULATE = 1050005;
  NISWITCH_ATTRIBUTE_RECORD_COERCIONS = 1050006;
  NISWITCH_ATTRIBUTE_INTERCHANGE_CHECK = 1050021;
  NISWITCH_ATTRIBUTE_CHANNEL_COUNT = 1050203;
  NISWITCH_ATTRIBUTE_GROUP_CAPABILITIES = 1050401;
  NISWITCH_ATTRIBUTE_SPECIFIC_DRIVER_PREFIX = 1050302;
  NISWITCH_ATTRIBUTE_SUPPORTED_INSTRUMENT_MODELS = 1050327;
  NISWITCH_ATTRIBUTE_INSTRUMENT_MANUFACTURER = 1050511;
  NISWITCH_ATTRIBUTE_INSTRUMENT_MODEL = 1050512;
  NISWITCH_ATTRIBUTE_INSTRUMENT_FIRMWARE_REVISION = 1050510;
  NISWITCH_ATTRIBUTE_SPECIFIC_DRIVER_REVISION = 1050551;
  NISWITCH_ATTRIBUTE_SPECIFIC_DRIVER_VENDOR = 1050513;
  NISWITCH_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION = 1050515;
  NISWITCH_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION = 1050516;
  NISWITCH_ATTRIBUTE_SPECIFIC_DRIVER_DESCRIPTION = 1050514;
  NISWITCH_ATTRIBUTE_DRIVER_SETUP = 1050007;
  NISWITCH_ATTRIBUTE_LOGICAL_NAME = 1050305;
  NISWITCH_ATTRIBUTE_IO_RESOURCE_DESCRIPTOR = 1050304;
  NISWITCH_ATTRIBUTE_IS_SOURCE_CHANNEL = 1250001;
  NISWITCH_ATTRIBUTE_IS_CONFIGURATION_CHANNEL = 1250003;
  NISWITCH_ATTRIBUTE_IS_DEBOUNCED = 1250002;
  NISWITCH_ATTRIBUTE_SETTLING_TIME = 1250004;
  NISWITCH_ATTRIBUTE_BANDWIDTH = 1250005;
  NISWITCH_ATTRIBUTE_MAX_DC_VOLTAGE = 1250006;
  NISWITCH_ATTRIBUTE_MAX_AC_VOLTAGE = 1250007;
  NISWITCH_ATTRIBUTE_MAX_SWITCHING_AC_CURRENT = 1250009;
  NISWITCH_ATTRIBUTE_MAX_SWITCHING_DC_CURRENT = 1250008;
  NISWITCH_ATTRIBUTE_MAX_CARRY_AC_CURRENT = 1250011;
  NISWITCH_ATTRIBUTE_MAX_CARRY_DC_CURRENT = 1250010;
  NISWITCH_ATTRIBUTE_MAX_SWITCHING_AC_POWER = 1250013;
  NISWITCH_ATTRIBUTE_MAX_SWITCHING_DC_POWER = 1250012;
  NISWITCH_ATTRIBUTE_MAX_CARRY_AC_POWER = 1250015;
  NISWITCH_ATTRIBUTE_MAX_CARRY_DC_POWER = 1250014;
  NISWITCH_ATTRIBUTE_CHARACTERISTIC_IMPEDANCE = 1250016;
  NISWITCH_ATTRIBUTE_WIRE_MODE = 1250017;
  NISWITCH_ATTRIBUTE_NUM_OF_ROWS = 1250018;
  NISWITCH_ATTRIBUTE_NUM_OF_COLUMNS = 1250019;
  NISWITCH_ATTRIBUTE_SCAN_LIST = 1250020;
  NISWITCH_ATTRIBUTE_SCAN_MODE = 1250021;
  NISWITCH_ATTRIBUTE_TRIGGER_INPUT = 1250022;
  NISWITCH_ATTRIBUTE_SCAN_ADVANCED_OUTPUT = 1250023;
  NISWITCH_ATTRIBUTE_SCAN_DELAY = 1250025;
  NISWITCH_ATTRIBUTE_CONTINUOUS_SCAN = 1250026;
  NISWITCH_ATTRIBUTE_IS_SCANNING = 1250024;
  NISWITCH_ATTRIBUTE_IS_WAITING_FOR_TRIG = 1150004;
  NISWITCH_ATTRIBUTE_TRIGGER_MODE = 1150005;
  NISWITCH_ATTRIBUTE_MASTER_SLAVE_TRIGGER_BUS = 1150006;
  NISWITCH_ATTRIBUTE_MASTER_SLAVE_SCAN_ADVANCED_BUS = 1150007;
  NISWITCH_ATTRIBUTE_CABLED_MODULE_TRIGGER_BUS = 1150008;
  NISWITCH_ATTRIBUTE_CABLED_MODULE_SCAN_ADVANCED_BUS = 1150009;
  NISWITCH_ATTRIBUTE_TRIGGER_INPUT_POLARITY = 1150010;
  NISWITCH_ATTRIBUTE_SCAN_ADVANCED_POLARITY = 1150011;
  NISWITCH_ATTRIBUTE_PARSED_SCAN_LIST = 1150012;
  NISWITCH_ATTRIBUTE_HANDSHAKING_INITIATION = 1150013;
  NISWITCH_ATTRIBUTE_NUMBER_OF_RELAYS = 1150014;
  NISWITCH_ATTRIBUTE_SERIAL_NUMBER = 1150015;
  NISWITCH_ATTRIBUTE_DIGITAL_FILTER_ENABLE = 1150016;
  NISWITCH_ATTRIBUTE_POWER_DOWN_LATCHING_RELAYS_AFTER_DEBOUNCE = 1150017;
  NISWITCH_ATTRIBUTE_ANALOG_BUS_SHARING_ENABLE = 1150018;
  NISWITCH_ATTRIBUTE_TEMPERATURE = 1150019;
  NISWITCH_ATTRIBUTE_SERIAL_NUMBER_I32 = 1150001;
}

enum ScanMode {
  SCAN_MODE_NISWITCH_VAL_NONE = 0;
  SCAN_MODE_NISWITCH_VAL_BREAK_BEFORE_MAKE = 1;
  SCAN_MODE_NISWITCH_VAL_BREAK_AFTER_MAKE = 2;
}

enum TriggerInput {
  TRIGGER_INPUT_UNSPECIFIED = 0;
  TRIGGER_INPUT_NISWITCH_VAL_IMMEDIATE = 1;
  TRIGGER_INPUT_NISWITCH_VAL_EXTERNAL = 2;
  TRIGGER_INPUT_NISWITCH_VAL_SOFTWARE_TRIG = 3;
  TRIGGER_INPUT_NISWITCH_VAL_TTL0 = 111;
  TRIGGER_INPUT_NISWITCH_VAL_TTL1 = 112;
  TRIGGER_INPUT_NISWITCH_VAL_TTL2 = 113;
  TRIGGER_INPUT_NISWITCH_VAL_TTL3 = 114;
  TRIGGER_INPUT_NISWITCH_VAL_TTL4 = 115;
  TRIGGER_INPUT_NISWITCH_VAL_TTL5 = 116;
  TRIGGER_INPUT_NISWITCH_VAL_TTL6 = 117;
  TRIGGER_INPUT_NISWITCH_VAL_TTL7 = 118;
  TRIGGER_INPUT_NISWITCH_VAL_PXI_STAR = 125;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR = 1000;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR = 1001;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE1 = 1021;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE2 = 1022;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE3 = 1023;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE4 = 1024;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE5 = 1025;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE6 = 1026;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE7 = 1027;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE8 = 1028;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE9 = 1029;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE10 = 1030;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE11 = 1031;
  TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE12 = 1032;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE1 = 1041;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE2 = 1042;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE3 = 1043;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE4 = 1044;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE5 = 1045;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE6 = 1046;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE7 = 1047;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE8 = 1048;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE9 = 1049;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE10 = 1050;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE11 = 1051;
  TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE12 = 1052;
}

enum PathCapability {
  PATH_CAPABILITY_UNSPECIFIED = 0;
  PATH_CAPABILITY_NISWITCH_VAL_PATH_AVAILABLE = 1;
  PATH_CAPABILITY_NISWITCH_VAL_PATH_EXISTS = 2;
  PATH_CAPABILITY_NISWITCH_VAL_PATH_UNSUPPORTED = 3;
  PATH_CAPABILITY_NISWITCH_VAL_RSRC_IN_USE = 4;
  PATH_CAPABILITY_NISWITCH_VAL_SOURCE_CONFLICT = 5;
  PATH_CAPABILITY_NISWITCH_VAL_CHANNEL_NOT_AVAILABLE = 6;
}

enum HandshakingInitiation {
  HANDSHAKING_INITIATION_NISWITCH_VAL_MEASUREMENT_DEVICE_INITIATED = 0;
  HANDSHAKING_INITIATION_NISWITCH_VAL_SWITCH_INITIATED = 1;
}

enum RelayPosition {
  RELAY_POSITION_UNSPECIFIED = 0;
  RELAY_POSITION_NISWITCH_VAL_OPEN = 10;
  RELAY_POSITION_NISWITCH_VAL_CLOSED = 11;
}

enum RelayAction {
  RELAY_ACTION_UNSPECIFIED = 0;
  RELAY_ACTION_NISWITCH_VAL_OPEN_RELAY = 20;
  RELAY_ACTION_NISWITCH_VAL_CLOSE_RELAY = 21;
}

enum ScanAdvancedOutput {
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_NONE = 0;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_EXTERNAL = 2;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_TTL0 = 111;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_TTL1 = 112;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_TTL2 = 113;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_TTL3 = 114;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_TTL4 = 115;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_TTL5 = 116;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_TTL6 = 117;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_TTL7 = 118;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_PXI_STAR = 125;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR = 1000;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR = 1001;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE1 = 1021;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE2 = 1022;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE3 = 1023;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE4 = 1024;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE5 = 1025;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE6 = 1026;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE7 = 1027;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE8 = 1028;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE9 = 1029;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE10 = 1030;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE11 = 1031;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE12 = 1032;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE1 = 1041;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE2 = 1042;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE3 = 1043;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE4 = 1044;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE5 = 1045;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE6 = 1046;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE7 = 1047;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE8 = 1048;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE9 = 1049;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE10 = 1050;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE11 = 1051;
  SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE12 = 1052;
}

enum NiSwitchInt32AttributeValues {
  option allow_alias = true;
  NISWITCH_INT32_UNSPECIFIED = 0;
  NISWITCH_INT32_HANDSHAKING_INITIATION_VAL_MEASUREMENT_DEVICE_INITIATED = 0;
  NISWITCH_INT32_HANDSHAKING_INITIATION_VAL_SWITCH_INITIATED = 1;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_NONE = 0;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_EXTERNAL = 2;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_TTL0 = 111;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_TTL1 = 112;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_TTL2 = 113;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_TTL3 = 114;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_TTL4 = 115;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_TTL5 = 116;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_TTL6 = 117;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_TTL7 = 118;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_PXI_STAR = 125;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR = 1000;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR = 1001;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE1 = 1021;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE2 = 1022;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE3 = 1023;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE4 = 1024;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE5 = 1025;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE6 = 1026;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE7 = 1027;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE8 = 1028;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE9 = 1029;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE10 = 1030;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE11 = 1031;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE12 = 1032;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE1 = 1041;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE2 = 1042;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE3 = 1043;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE4 = 1044;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE5 = 1045;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE6 = 1046;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE7 = 1047;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE8 = 1048;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE9 = 1049;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE10 = 1050;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE11 = 1051;
  NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE12 = 1052;
  NISWITCH_INT32_SCAN_ADVANCED_POLARITY_VAL_RISING_EDGE = 0;
  NISWITCH_INT32_SCAN_ADVANCED_POLARITY_VAL_FALLING_EDGE = 1;
  NISWITCH_INT32_SCAN_MODE_VAL_NONE = 0;
  NISWITCH_INT32_SCAN_MODE_VAL_BREAK_BEFORE_MAKE = 1;
  NISWITCH_INT32_SCAN_MODE_VAL_BREAK_AFTER_MAKE = 2;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_IMMEDIATE = 1;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_EXTERNAL = 2;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_SOFTWARE_TRIG = 3;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_TTL0 = 111;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_TTL1 = 112;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_TTL2 = 113;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_TTL3 = 114;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_TTL4 = 115;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_TTL5 = 116;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_TTL6 = 117;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_TTL7 = 118;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_PXI_STAR = 125;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR = 1000;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR = 1001;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE1 = 1021;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE2 = 1022;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE3 = 1023;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE4 = 1024;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE5 = 1025;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE6 = 1026;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE7 = 1027;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE8 = 1028;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE9 = 1029;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE10 = 1030;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE11 = 1031;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE12 = 1032;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE1 = 1041;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE2 = 1042;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE3 = 1043;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE4 = 1044;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE5 = 1045;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE6 = 1046;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE7 = 1047;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE8 = 1048;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE9 = 1049;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE10 = 1050;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE11 = 1051;
  NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE12 = 1052;
  NISWITCH_INT32_TRIGGER_INPUT_POLARITY_VAL_RISING_EDGE = 0;
  NISWITCH_INT32_TRIGGER_INPUT_POLARITY_VAL_FALLING_EDGE = 1;
  NISWITCH_INT32_WIRE_MODE_VAL_1_WIRE = 1;
  NISWITCH_INT32_WIRE_MODE_VAL_2_WIRE = 2;
  NISWITCH_INT32_WIRE_MODE_VAL_4_WIRE = 4;
}

message InitRequest {
  string session_name = 1;
  string resource_name = 2;
  bool id_query = 3;
  bool reset_device = 4;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 5;
}

message InitResponse {
  int32 status = 1;
  nidevice_grpc.Session vi = 2;
  string error_message = 3 [deprecated = true];
  bool new_session_initialized = 4;
}

message InitWithOptionsRequest {
  string session_name = 1;
  string resource_name = 2;
  bool id_query = 3;
  bool reset_device = 4;
  string option_string = 5;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 6;
}

message InitWithOptionsResponse {
  int32 status = 1;
  nidevice_grpc.Session vi = 2;
  string error_message = 3 [deprecated = true];
  bool new_session_initialized = 4;
}

message InitWithTopologyRequest {
  string session_name = 1;
  string resource_name = 2;
  string topology = 3;
  bool simulate = 4;
  bool reset_device = 5;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 6;
}

message InitWithTopologyResponse {
  int32 status = 1;
  nidevice_grpc.Session vi = 2;
  string error_message = 3 [deprecated = true];
  bool new_session_initialized = 4;
}

message CloseRequest {
  nidevice_grpc.Session vi = 1;
}

message CloseResponse {
  int32 status = 1;
}

message ConnectRequest {
  nidevice_grpc.Session vi = 1;
  string channel1 = 2;
  string channel2 = 3;
}

message ConnectResponse {
  int32 status = 1;
}

message ConnectMultipleRequest {
  nidevice_grpc.Session vi = 1;
  string connection_list = 2;
}

message ConnectMultipleResponse {
  int32 status = 1;
}

message DisconnectRequest {
  nidevice_grpc.Session vi = 1;
  string channel1 = 2;
  string channel2 = 3;
}

message DisconnectResponse {
  int32 status = 1;
}

message DisconnectMultipleRequest {
  nidevice_grpc.Session vi = 1;
  string disconnection_list = 2;
}

message DisconnectMultipleResponse {
  int32 status = 1;
}

message DisconnectAllRequest {
  nidevice_grpc.Session vi = 1;
}

message DisconnectAllResponse {
  int32 status = 1;
}

message GetPathRequest {
  nidevice_grpc.Session vi = 1;
  string channel1 = 2;
  string channel2 = 3;
}

message GetPathResponse {
  int32 status = 1;
  string path = 2;
}

message SetPathRequest {
  nidevice_grpc.Session vi = 1;
  string path_list = 2;
}

message SetPathResponse {
  int32 status = 1;
}

message CanConnectRequest {
  nidevice_grpc.Session vi = 1;
  string channel1 = 2;
  string channel2 = 3;
}

message CanConnectResponse {
  int32 status = 1;
  PathCapability path_capability = 2;
  sint32 path_capability_raw = 3;
}

message IsDebouncedRequest {
  nidevice_grpc.Session vi = 1;
}

message IsDebouncedResponse {
  int32 status = 1;
  bool is_debounced = 2;
}

message WaitForDebounceRequest {
  nidevice_grpc.Session vi = 1;
  sint32 maximum_time_ms = 2;
}

message WaitForDebounceResponse {
  int32 status = 1;
}

message ScanRequest {
  nidevice_grpc.Session vi = 1;
  string scan_list = 2;
  oneof initiation_enum {
    HandshakingInitiation initiation = 3;
    sint32 initiation_raw = 4;
  }
}

message ScanResponse {
  int32 status = 1;
}

message InitiateScanRequest {
  nidevice_grpc.Session vi = 1;
}

message InitiateScanResponse {
  int32 status = 1;
}

message AbortScanRequest {
  nidevice_grpc.Session vi = 1;
}

message AbortScanResponse {
  int32 status = 1;
}

message IsScanningRequest {
  nidevice_grpc.Session vi = 1;
}

message IsScanningResponse {
  int32 status = 1;
  bool is_scanning = 2;
}

message WaitForScanCompleteRequest {
  nidevice_grpc.Session vi = 1;
  sint32 maximum_time_ms = 2;
}

message WaitForScanCompleteResponse {
  int32 status = 1;
}

message SendSoftwareTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message SendSoftwareTriggerResponse {
  int32 status = 1;
}

message ConfigureScanListRequest {
  nidevice_grpc.Session vi = 1;
  string scan_list = 2;
  oneof scan_mode_enum {
    ScanMode scan_mode = 3;
    sint32 scan_mode_raw = 4;
  }
}

message ConfigureScanListResponse {
  int32 status = 1;
}

message ConfigureScanTriggerRequest {
  nidevice_grpc.Session vi = 1;
  double scan_delay = 2;
  oneof trigger_input_enum {
    TriggerInput trigger_input = 3;
    sint32 trigger_input_raw = 4;
  }
  oneof scan_advanced_output_enum {
    ScanAdvancedOutput scan_advanced_output = 5;
    sint32 scan_advanced_output_raw = 6;
  }
}

message ConfigureScanTriggerResponse {
  int32 status = 1;
}

message SetContinuousScanRequest {
  nidevice_grpc.Session vi = 1;
  bool continuous_scan = 2;
}

message SetContinuousScanResponse {
  int32 status = 1;
}

message RouteTriggerInputRequest {
  nidevice_grpc.Session vi = 1;
  oneof trigger_input_connector_enum {
    TriggerInput trigger_input_connector = 2;
    sint32 trigger_input_connector_raw = 3;
  }
  oneof trigger_input_bus_line_enum {
    TriggerInput trigger_input_bus_line = 4;
    sint32 trigger_input_bus_line_raw = 5;
  }
  bool invert = 6;
}

message RouteTriggerInputResponse {
  int32 status = 1;
}

message RouteScanAdvancedOutputRequest {
  nidevice_grpc.Session vi = 1;
  oneof scan_advanced_output_connector_enum {
    ScanAdvancedOutput scan_advanced_output_connector = 2;
    sint32 scan_advanced_output_connector_raw = 3;
  }
  oneof scan_advanced_output_bus_line_enum {
    ScanAdvancedOutput scan_advanced_output_bus_line = 4;
    sint32 scan_advanced_output_bus_line_raw = 5;
  }
  bool invert = 6;
}

message RouteScanAdvancedOutputResponse {
  int32 status = 1;
}

message ErrorQueryRequest {
  nidevice_grpc.Session vi = 1;
}

message ErrorQueryResponse {
  int32 status = 1;
  sint32 error_code = 2;
  string error_message = 3;
}

message GetErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message GetErrorResponse {
  int32 status = 1;
  sint32 code = 2;
  string description = 3;
}

message ClearErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message ClearErrorResponse {
  int32 status = 1;
}

message ErrorMessageRequest {
  nidevice_grpc.Session vi = 1;
  sint32 error_code = 2;
}

message ErrorMessageResponse {
  int32 status = 1;
  string error_message = 2;
}

message GetChannelNameRequest {
  nidevice_grpc.Session vi = 1;
  sint32 index = 2;
}

message GetChannelNameResponse {
  int32 status = 1;
  string channel_name_buffer = 2;
}

message GetRelayNameRequest {
  nidevice_grpc.Session vi = 1;
  sint32 index = 2;
}

message GetRelayNameResponse {
  int32 status = 1;
  string relay_name_buffer = 2;
}

message GetRelayCountRequest {
  nidevice_grpc.Session vi = 1;
  string relay_name = 2;
}

message GetRelayCountResponse {
  int32 status = 1;
  sint32 relay_count = 2;
}

message GetRelayPositionRequest {
  nidevice_grpc.Session vi = 1;
  string relay_name = 2;
}

message GetRelayPositionResponse {
  int32 status = 1;
  RelayPosition relay_position = 2;
  sint32 relay_position_raw = 3;
}

message RelayControlRequest {
  nidevice_grpc.Session vi = 1;
  string relay_name = 2;
  oneof relay_action_enum {
    RelayAction relay_action = 3;
    sint32 relay_action_raw = 4;
  }
}

message RelayControlResponse {
  int32 status = 1;
}

message ResetInterchangeCheckRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetInterchangeCheckResponse {
  int32 status = 1;
}

message ClearInterchangeWarningsRequest {
  nidevice_grpc.Session vi = 1;
}

message ClearInterchangeWarningsResponse {
  int32 status = 1;
}

message CommitRequest {
  nidevice_grpc.Session vi = 1;
}

message CommitResponse {
  int32 status = 1;
}

message ResetWithDefaultsRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetWithDefaultsResponse {
  int32 status = 1;
}

message DisableRequest {
  nidevice_grpc.Session vi = 1;
}

message DisableResponse {
  int32 status = 1;
}

message ResetRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetResponse {
  int32 status = 1;
}

message SelfTestRequest {
  nidevice_grpc.Session vi = 1;
}

message SelfTestResponse {
  int32 status = 1;
  sint32 self_test_result = 2;
  string self_test_message = 3;
}

message RevisionQueryRequest {
  nidevice_grpc.Session vi = 1;
}

message RevisionQueryResponse {
  int32 status = 1;
  string instrument_driver_revision = 2;
  string firmware_revision = 3;
}

message GetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
}

message GetAttributeViInt32Response {
  int32 status = 1;
  sint32 attribute_value = 2;
}

message GetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
}

message GetAttributeViReal64Response {
  int32 status = 1;
  double attribute_value = 2;
}

message GetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
}

message GetAttributeViStringResponse {
  int32 status = 1;
  string attribute_value = 2;
}

message GetAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
}

message GetAttributeViSessionResponse {
  int32 status = 1;
  nidevice_grpc.Session attribute_value = 2;
}

message GetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
}

message GetAttributeViBooleanResponse {
  int32 status = 1;
  bool attribute_value = 2;
}

message SetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
  oneof attribute_value_enum {
    sint32 attribute_value_raw = 4;
    NiSwitchInt32AttributeValues attribute_value = 5;
  }
}

message SetAttributeViInt32Response {
  int32 status = 1;
}

message SetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
  double attribute_value_raw = 4;
}

message SetAttributeViReal64Response {
  int32 status = 1;
}

message SetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
  string attribute_value_raw = 4;
}

message SetAttributeViStringResponse {
  int32 status = 1;
}

message SetAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
  nidevice_grpc.Session attribute_value = 4;
}

message SetAttributeViSessionResponse {
  int32 status = 1;
}

message SetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
  bool attribute_value = 4;
}

message SetAttributeViBooleanResponse {
  int32 status = 1;
}

message CheckAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
  oneof attribute_value_enum {
    sint32 attribute_value_raw = 4;
    NiSwitchInt32AttributeValues attribute_value = 5;
  }
}

message CheckAttributeViInt32Response {
  int32 status = 1;
}

message CheckAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
  double attribute_value_raw = 4;
}

message CheckAttributeViReal64Response {
  int32 status = 1;
}

message CheckAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
  string attribute_value_raw = 4;
}

message CheckAttributeViStringResponse {
  int32 status = 1;
}

message CheckAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
  nidevice_grpc.Session attribute_value = 4;
}

message CheckAttributeViSessionResponse {
  int32 status = 1;
}

message CheckAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiSwitchAttribute attribute_id = 3;
  bool attribute_value = 4;
}

message CheckAttributeViBooleanResponse {
  int32 status = 1;
}

message InvalidateAllAttributesRequest {
  nidevice_grpc.Session vi = 1;
}

message InvalidateAllAttributesResponse {
  int32 status = 1;
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niswitch/niswitch.mak sha256=5ea7de782af9ede80d0a095945ab98d2067502770ce68c69d91211a0e216fc75 bytes=352 -->
## FILE: src/niswitch/niswitch.mak

- repository: `ni/nimi-python`
- source_path: `src/niswitch/niswitch.mak`
- sha256: `5ea7de782af9ede80d0a095945ab98d2067502770ce68c69d91211a0e216fc75`
- bytes: 352

````makefile


include $(BUILD_HELPER_DIR)/defines.mak

MODULE_FILES_TO_GENERATE := $(DEFAULT_PY_FILES_TO_GENERATE)

MODULE_FILES_TO_COPY := $(DEFAULT_PY_FILES_TO_COPY)

RST_FILES_TO_GENERATE := $(DEFAULT_RST_FILES_TO_GENERATE)

SPHINX_CONF_PY := $(DEFAULT_SPHINX_CONF_PY)
READTHEDOCS_CONFIG := $(DEFAULT_READTHEDOCS_CONFIG)

include $(BUILD_HELPER_DIR)/rules.mak
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niswitch/system_tests/grpc_server_config.json sha256=1376c6f0085243579095f1c333a09f6a4a4e3fbd4e5159457f7b44f6ed1dd031 bytes=156 -->
## FILE: src/niswitch/system_tests/grpc_server_config.json

- repository: `ni/nimi-python`
- source_path: `src/niswitch/system_tests/grpc_server_config.json`
- sha256: `1376c6f0085243579095f1c333a09f6a4a4e3fbd4e5159457f7b44f6ed1dd031`
- bytes: 156

````json
{
    "address": "[::1]",
    "port": 31765,
    "security" : {
       "server_cert": "",
       "server_key": "",
       "root_cert": ""
    }
 }
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/niswitch/system_tests/test_system_niswitch.py sha256=e96d748431bb0425c0cdab113b21d56f4c7a85741cc55d14b60c6ce18f8edecc bytes=8776 -->
## FILE: src/niswitch/system_tests/test_system_niswitch.py

- repository: `ni/nimi-python`
- source_path: `src/niswitch/system_tests/test_system_niswitch.py`
- sha256: `e96d748431bb0425c0cdab113b21d56f4c7a85741cc55d14b60c6ce18f8edecc`
- bytes: 8776

````python
import os
import pathlib
import sys
import tempfile

import fasteners
import grpc
import hightime
import pytest

import niswitch

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent / 'shared'))
import system_test_utilities  # noqa: E402

# We need a lock file so multiple tests aren't hitting the db at the same time
# Trying to create simulated DAQmx devices at the same time (which can happen when running
# tox with --parallel N, or when two different drivers are being tested at the same time on
# the same machine, can result in an internal error:
# -2147220733: MAX:  (Hex 0x80040303) Internal error: The requested object was not found in
# the configuration database. Please note the steps you performed that led to this error and
# contact technical support at http://ni.com/support.
# This is filed as internal bug 255545
daqmx_sim_db_lock_file = os.path.join(tempfile.gettempdir(), 'daqmx_db.lock')
daqmx_sim_db_lock = fasteners.InterProcessLock(daqmx_sim_db_lock_file)


class SystemTests:
    @pytest.fixture(scope='function')
    def session(self, session_creation_kwargs):
        with niswitch.Session('', '2737/2-Wire 4x64 Matrix', True, True, **session_creation_kwargs) as simulated_session:
            yield simulated_session

    @pytest.fixture(scope='function')
    def session_2532(self, session_creation_kwargs):
        with daqmx_sim_db_lock:
            simulated_session = niswitch.Session('', '2532/1-Wire 4x128 Matrix', True, False, **session_creation_kwargs)
        yield simulated_session
        with daqmx_sim_db_lock:
            simulated_session.close()

    # Basic Use Case Tests
    def test_relayclose(self, session):
        relay_name = 'kr0c0'
        assert session.get_relay_position(relay_name) == niswitch.RelayPosition.OPEN
        session.relay_control(relay_name, niswitch.RelayAction.CLOSE)
        assert session.get_relay_position(relay_name) == niswitch.RelayPosition.CLOSED
        relay_count = session.get_relay_count(relay_name)
        assert relay_count == 0

    def test_channel_connection(self, session):
        channel1 = 'c0'
        channel2 = 'r0'
        assert session.can_connect(channel1, channel2) == niswitch.PathCapability.PATH_AVAILABLE
        session.connect(channel1, channel2)
        session.wait_for_debounce()
        assert session.is_debounced is True
        assert session.can_connect(channel1, channel2) == niswitch.PathCapability.PATH_EXISTS
        session.disconnect(channel1, channel2)
        assert session.can_connect(channel1, channel2) == niswitch.PathCapability.PATH_AVAILABLE
        session.connect(channel1, channel2)
        assert session.can_connect(channel1, channel2) == niswitch.PathCapability.PATH_EXISTS
        session.disconnect_all()
        assert session.can_connect(channel1, channel2) == niswitch.PathCapability.PATH_AVAILABLE

    @pytest.mark.skip(reason="TODO(sbethur): Intermittent failures, GitHub issue #1622.")
    def test_continuous_software_scanning(self, session_2532):
        scan_list = 'r0->c0; r1->c1'
        session_2532.scan_list = scan_list
        assert session_2532.scan_list == scan_list
        session_2532.route_scan_advanced_output(niswitch.ScanAdvancedOutput.FRONTCONNECTOR, niswitch.ScanAdvancedOutput.NONE)
        session_2532.route_trigger_input(niswitch.TriggerInput.FRONTCONNECTOR, niswitch.TriggerInput.TTL0)
        session_2532.trigger_input = niswitch.TriggerInput.SOFTWARE_TRIG
        session_2532.scan_advanced_output = niswitch.ScanAdvancedOutput.NONE
        session_2532.scan_list = scan_list
        session_2532.scan_mode = niswitch.ScanMode.BREAK_BEFORE_MAKE
        session_2532.continuous_scan = True
        session_2532.commit()
        with session_2532.initiate():
            assert session_2532.is_scanning is True
            session_2532.send_software_trigger()
            try:
                session_2532.wait_for_scan_complete()
                assert False
            except niswitch.Error as e:
                assert e.code == -1074126826  # Error : Max time exceeded.

    # Attribute Tests
    # No R/W non-IVI boolean attributes on all devices
    '''
    def test_vi_boolean_attribute(session):
        session.power_down_latching_relays_after_debounce = False
        assert session.power_down_latching_relays_after_debounce is False
        session.power_down_latching_relays_after_debounce = True
        assert session.power_down_latching_relays_after_debounce is True
    '''

    def test_vi_string_attribute(self, session):
        assert 'NI PXIe-2737' == session.instrument_model

    def test_vi_int32_attribute(self, session):
        assert session.channel_count == 68

    def test_vi_real64_attribute(self, session):
        session.settling_time = hightime.timedelta(seconds=0.1)
        assert session.settling_time.total_seconds() == 0.1

    @pytest.mark.skip(reason="TODO(sbethur): Intermittent failures, GitHub issue #1622.")
    def test_enum_attribute(self, session_2532):
        assert session_2532.scan_mode == niswitch.ScanMode.BREAK_BEFORE_MAKE

    def test_write_only_attribute(self, session):
        try:
            session.channel_count = 5
            assert False
        except niswitch.Error as e:
            assert e.code == -1074135027  # Error : Attribute is read-only.

    # Function Tests
    def test_method_reset(self, session):
        session.reset()

    def test_method_set_path(self, session):
        session.set_path('r0->c0')

    def test_method_can_connect(self, session):
        path_capability = session.can_connect('r0', 'r1')
        assert path_capability == niswitch.PathCapability.PATH_UNSUPPORTED

    def test_method_reset_with_defaults(self, session):
        assert session.reset_with_defaults() is None

    def test_functions_get_relay_name(self, session):
        relay_name = session.get_relay_name(1)
        assert relay_name == 'kr0c0'

    def test_functions_get_channel_name(self, session):
        channel_name = session.get_channel_name(1)
        assert channel_name == 'r0'

    def test_functions_self_test(self, session):
        # We should not get an assert if self_test passes
        session.self_test()

    def test_locks_are_reentrant(self, session):
        with session.lock():
            with session.lock():
                # We should not get an assert if self_test passes
                session.self_test()

    def test_functions_get_path(self, session):
        channel1 = 'r0'
        channel2 = 'c0'
        session.connect(channel1, channel2)
        path = session.get_path(channel1, channel2)
        assert path == 'r0->c0'
        session.disconnect(channel1, channel2)
        session.set_path(path)

    def test_functions_connect_disconnect_multiple(self, session):
        session.connect_multiple('c0->r0, c0->r1')   # expect no errors
        session.disconnect_multiple('c0->r0, c0->r1')   # expect no errors

    def test_functions_disable(self, session):
        channel1 = 'c0'
        channel2 = 'r0'
        session.connect(channel1, channel2)
        session.disable()   # expect no errors
        assert session.can_connect(channel1, channel2) == niswitch.PathCapability.PATH_AVAILABLE

    def test_error_message(self, session_creation_kwargs):
        try:
            # We pass in an invalid model name to force going to error_message
            with niswitch.Session('', 'Invalid Topology', True, True, **session_creation_kwargs):
                assert False
        except niswitch.Error as e:
            assert e.code == -1074118654
            assert e.description.find('Invalid resource name.') != -1

    # Multi-Threading tests
    def test_multi_threading_lock_unlock(self, session):
        system_test_utilities.impl_test_multi_threading_lock_unlock(session)

    def test_multi_threading_ivi_synchronized_wrapper_releases_lock(self, session):
        system_test_utilities.impl_test_multi_threading_ivi_synchronized_wrapper_releases_lock(
            session.self_test)


class TestLibrary(SystemTests):
    @pytest.fixture(scope='class')
    def session_creation_kwargs(self):
        return {}


class TestGrpc(SystemTests):
    @pytest.fixture(scope='class')
    def grpc_channel(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(current_directory, 'grpc_server_config.json')
        with system_test_utilities.GrpcServerProcess(config_file_path) as proc:
            channel = grpc.insecure_channel(f"localhost:{proc.server_port}")
            yield channel

    @pytest.fixture(scope='class')
    def session_creation_kwargs(self, grpc_channel):
        grpc_options = niswitch.GrpcSessionOptions(grpc_channel, "")
        return {'grpc_options': grpc_options}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nitclk/examples/nitclk_niscope_synchronize_with_trigger.py sha256=7dcc62fb90c07c545c61ac6acb52304b1972a1866024fda900b9258c6c84a730 bytes=2088 -->
## FILE: src/nitclk/examples/nitclk_niscope_synchronize_with_trigger.py

- repository: `ni/nimi-python`
- source_path: `src/nitclk/examples/nitclk_niscope_synchronize_with_trigger.py`
- sha256: `7dcc62fb90c07c545c61ac6acb52304b1972a1866024fda900b9258c6c84a730`
- bytes: 2088

````python
import argparse
import niscope
import nitclk
import sys
import time


def example(resource_name1, resource_name2, options):
    with niscope.Session(resource_name=resource_name1, options=options) as session1, niscope.Session(resource_name=resource_name2, options=options) as session2:
        session_list = [session1, session2]
        for session in session_list:
            session.configure_vertical(range=1.0, coupling=niscope.VerticalCoupling.DC)
            session.configure_horizontal_timing(min_sample_rate=50000000, min_num_pts=1000, ref_position=50.0, num_records=1, enforce_realtime=True)
        session1.trigger_type = niscope.TriggerType.SOFTWARE
        nitclk.configure_for_homogeneous_triggers(session_list)
        nitclk.synchronize(session_list, 200e-9)
        nitclk.initiate(session_list)
        time.sleep(100)
        session1.send_software_trigger_edge(niscope.WhichTrigger.START)
        waveforms = session2.channels[0].fetch(num_samples=1000)
        for i in range(len(waveforms)):
            print(f'Waveform {i} information:')
            print(str(waveforms[i]) + '\n\n')


def _main(argsv):
    parser = argparse.ArgumentParser(description='Synchronizes multiple instruments to one trigger.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n1', '--resource-name1', default='PXI1Slot2', help='Resource name of a NI Digitizer')
    parser.add_argument('-n2', '--resource-name2', default='PXI1Slot3', help='Resource name of a NI Digitizer')
    parser.add_argument('-op', '--option-string', default='', type=str, help='Option string')
    args = parser.parse_args(argsv)
    example(args.resource_name1, args.resource_name2, args.option_string)


def main():
    _main(sys.argv[1:])


def test_example():
    options = {'simulate': True, 'driver_setup': {'Model': '5164', 'BoardType': 'PXIe', }, }
    example('PXI1Slot2', 'PXI1Slot13', options)


def test_main():
    cmd_line = ['--option-string', 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe', ]
    _main(cmd_line)


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nitclk/LATEST_RELEASE sha256=dd1b44562fc7c779fd9bef2e55d2e7b58783c4ca61885f5b549cd89de7e9a3fd bytes=7 -->
## FILE: src/nitclk/LATEST_RELEASE

- repository: `ni/nimi-python`
- source_path: `src/nitclk/LATEST_RELEASE`
- sha256: `dd1b44562fc7c779fd9bef2e55d2e7b58783c4ca61885f5b549cd89de7e9a3fd`
- bytes: 7

````text
1.4.9
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nitclk/metadata/__init__.py sha256=4b7b39cf71ea45690188c6523109d0f0f8d8fcd1aa92823d69a7a1554cb97ddc bytes=513 -->
## FILE: src/nitclk/metadata/__init__.py

- repository: `ni/nimi-python`
- source_path: `src/nitclk/metadata/__init__.py`
- sha256: `4b7b39cf71ea45690188c6523109d0f0f8d8fcd1aa92823d69a7a1554cb97ddc`
- bytes: 513

````python
from metadata.config import config
from metadata.functions import functions
from metadata.attributes import attributes
from metadata.enums import enums
import metadata.functions_addon
import metadata.attributes_addon
import metadata.enums_addon
import metadata.config_addon

import build.helper as helper
import sys

# Update generated functions data with hand maintained data
config['modules'] = sys.modules
helper.add_all_metadata(functions, attributes, enums, config)

__version__ = config['module_version']
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nitclk/metadata/attributes.py sha256=9153d899d4ba4d6306b1798c2cc30aac47dec1d92f24b53ead27d6e67e87dd2f bytes=8369 -->
## FILE: src/nitclk/metadata/attributes.py

- repository: `ni/nimi-python`
- source_path: `src/nitclk/metadata/attributes.py`
- sha256: `9153d899d4ba4d6306b1798c2cc30aac47dec1d92f24b53ead27d6e67e87dd2f`
- bytes: 8369

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-TClk API metadata version 25.0.0f93
attributes = {
    1: {
        'access': 'read-write',
        'documentation': {
            'description': "\nSpecifies the Sync Pulse source. This attribute is most often used when  synchronizing a multichassis system.\nValues\nEmpty string\nPXI Devices -  'PXI_Trig0' through  'PXI_Trig7' and device-specific settings\nPCI Devices -  'RTSI_0' through  'RTSI_7' and device-specific settings\nExamples of Device-Specific Settings\n- NI PXI-5122 supports  'PFI0' and  'PFI1'\n- NI PXI-5421 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'\n- NI PXI-6551/6552 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'\nDefault Value - Empty string. This default value directs  niTClk_Synchronize to set this attribute when all the synchronized devices  are in one PXI chassis. To synchronize a multichassis system, you must set  this attribute before calling niTClk_Synchronize.\n"
        },
        'lv_property': 'Sync Pulse Source',
        'name': 'SYNC_PULSE_SOURCE',
        'type': 'ViString'
    },
    2: {
        'access': 'read-write',
        'documentation': {
            'description': "\nSpecifies the destination of the Sync Pulse. This attribute is most often  used when synchronizing a multichassis system.\nValues\nEmpty string. Empty string is a valid value, indicating that the signal is  not exported.\nPXI Devices -  'PXI_Trig0' through  'PXI_Trig7' and device-specific settings\nPCI Devices -  'RTSI_0' through  'RTSI_7' and device-specific settings\nExamples of Device-Specific Settings\n- NI PXI-5122 supports  'PFI0' and  'PFI1'\n- NI PXI-5421 supports  'PFI0',  'PFI1',  'PFI4', and  'PFI5'\n- NI PXI-6551/6552 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'\nDefault Value is empty string\n"
        },
        'lv_property': 'Export Sync Pulse Output Terminal',
        'name': 'EXPORTED_SYNC_PULSE_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    3: {
        'access': 'read-write',
        'attribute_class': 'AttributeSessionReference',
        'documentation': {
            'description': '\nSpecifies the start trigger master session.\nFor external triggers, the session that originally receives the trigger.  For None (no trigger configured) or software triggers, the session that  originally generates the trigger.\n'
        },
        'lv_property': 'Start Trigger Master Session',
        'name': 'START_TRIGGER_MASTER_SESSION',
        'type': 'ViSession',
        'type_in_documentation': 'instrument-specific session or an instance of nitclk.SessionReference'
    },
    4: {
        'access': 'read-write',
        'attribute_class': 'AttributeSessionReference',
        'documentation': {
            'description': '\nSpecifies the reference trigger master session.\nFor external triggers, the session that originally receives the trigger.  For None (no trigger configured) or software triggers, the session that  originally generates the trigger.\n'
        },
        'lv_property': 'Reference Trigger Master Session',
        'name': 'REF_TRIGGER_MASTER_SESSION',
        'type': 'ViSession',
        'type_in_documentation': 'instrument-specific session or an instance of nitclk.SessionReference'
    },
    6: {
        'access': 'read-write',
        'attribute_class': 'AttributeSessionReference',
        'documentation': {
            'description': '\nSpecifies the pause trigger master session.\nFor external triggers, the session that originally receives the trigger.  For None (no trigger configured) or software triggers, the session that  originally generates the trigger.\n'
        },
        'lv_property': 'Pause Trigger Master Session',
        'name': 'PAUSE_TRIGGER_MASTER_SESSION',
        'type': 'ViSession',
        'type_in_documentation': 'instrument-specific session or an instance of nitclk.SessionReference'
    },
    8: {
        'access': 'read only',
        'documentation': {
            'description': '\nIndicates the computed TClk period that will be used during the acquisition.\n'
        },
        'lv_property': 'Period',
        'name': 'TCLK_ACTUAL_PERIOD',
        'type': 'ViReal64'
    },
    9: {
        'access': 'read-write',
        'documentation': {
            'description': "\nSpecifies the destination of the device's TClk signal.\nValues\nEmpty string. Empty string is a valid value, indicating that the signal is  not exported.\nPXI Devices -  'PXI_Trig0' through  'PXI_Trig7' and device-specific settings\nPCI Devices -  'RTSI_0' through  'RTSI_7' and device-specific settings\nExamples of Device-Specific Settings\n- NI PXI-5122 supports  'PFI0' and  'PFI1'\n- NI PXI-5421 supports  'PFI0',  'PFI1',  'PFI4', and  'PFI5'\n- NI PXI-6551/6552 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'\nDefault Value is empty string\n"
        },
        'lv_property': 'Output Terminal',
        'name': 'EXPORTED_TCLK_OUTPUT_TERMINAL',
        'type': 'ViString'
    },
    10: {
        'access': 'read-write',
        'documentation': {
            'description': "\nSpecifies the Sync Pulse Clock source. This attribute is typically used to  synchronize PCI devices when you want to control RTSI 7 yourself. Make  sure that a 10 MHz clock is driven onto RTSI 7.\nValues\nPCI Devices -  'RTSI_7' and  'None'\nPXI Devices -  'PXI_CLK10' and  'None'\nDefault Value -  'None' directs niTClk_Synchronize to create the necessary routes. For  PCI, one of the synchronized devices drives a 10 MHz clock on RTSI 7  unless that line is already being driven.\n"
        },
        'lv_property': 'Sync Pulse Clock Source',
        'name': 'SYNC_PULSE_CLOCK_SOURCE',
        'type': 'ViString'
    },
    11: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nSpecifies the sample clock delay.\nSpecifies the delay, in seconds, to apply to the session sample clock  relative to the other synchronized sessions. During synchronization,  NI-TClk aligns the sample clocks on the synchronized devices. If you want  to delay the sample clocks, set this attribute before calling  niTClk_Synchronize.\nnot supported for acquisition sessions.\nValues - Between minus one and plus one period of the sample clock.\nOne sample clock period is equal to (1/sample clock rate). For example,  for a session with sample rate of 100 MS/s, you can specify sample clock  delays between -10.0 ns and +10.0 ns.\nDefault Value is 0\n',
            'note': 'Sample clock delay is supported for generation sessions only; it is'
        },
        'lv_property': 'Sample Clock Delay',
        'name': 'SAMPLE_CLOCK_DELAY',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    13: {
        'access': 'read-write',
        'documentation': {
            'description': "\nSpecifies the external sync pulse source for the Sync Pulse Sender.  You can use this source to synchronize  the Sync Pulse Sender with an external non-TClk source.\nValues\nEmpty string. Empty string is a valid value, indicating that the signal is  not exported.\nPXI Devices -  'PXI_Trig0' through  'PXI_Trig7' and device-specific settings\nPCI Devices -  'RTSI_0' through  'RTSI_7' and device-specific settings\nExamples of Device-Specific Settings\n- NI PXI-5122 supports  'PFI0' and  'PFI1'\n- NI PXI-5421 supports  'PFI0',  'PFI1',  'PFI4', and  'PFI5'\n- NI PXI-6551/6552 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'\nDefault Value is empty string\n"
        },
        'lv_property': 'External Pulse Source',
        'name': 'SYNC_PULSE_SENDER_SYNC_PULSE_SOURCE',
        'type': 'ViString'
    },
    16: {
        'access': 'read-write',
        'attribute_class': 'AttributeSessionReference',
        'documentation': {
            'description': '\nSpecifies the sequencer flag master session.\nFor external triggers, the session that originally receives the trigger.\nFor None (no trigger configured) or software triggers, the session that\noriginally generates the trigger.\n'
        },
        'lv_property': 'Sequencer Flag Master Session',
        'name': 'SEQUENCER_FLAG_MASTER_SESSION',
        'type': 'ViSession',
        'type_in_documentation': 'instrument-specific session or an instance of nitclk.SessionReference'
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nitclk/metadata/attributes_addon.py sha256=47ce6cf355aa81eb0eb3ea168e57031b15e72e974b8ec3d991170a7cc6e2223a bytes=471 -->
## FILE: src/nitclk/metadata/attributes_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nitclk/metadata/attributes_addon.py`
- sha256: `47ce6cf355aa81eb0eb3ea168e57031b15e72e974b8ec3d991170a7cc6e2223a`
- bytes: 471

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# We are not code genning attributes that have been marked as obsolete prior to the initial
# Python API bindings release

attributes_codegen_method = {
}

attributes_converters = {
}

attributes_enums = {
}

# If the associated enum represents boolean values only, disconnect
attributes_remove_enum = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nitclk/metadata/config.py sha256=fb6dde7cc35864cd66d5324845dd58df6cc5bad7cab5fa3141bc92329d3b0022 bytes=989 -->
## FILE: src/nitclk/metadata/config.py

- repository: `ni/nimi-python`
- source_path: `src/nitclk/metadata/config.py`
- sha256: `fb6dde7cc35864cd66d5324845dd58df6cc5bad7cab5fa3141bc92329d3b0022`
- bytes: 989

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-TClk API metadata version 25.0.0f93
config = {
    'api_version': '25.0.0f93',
    'c_function_prefix': 'niTClk_',
    'close_function': None,
    'context_manager_name': {
    },
    'custom_types': [
    ],
    'driver_name': 'NI-TClk',
    'extra_errors_used': [
    ],
    'grpc_service_class_prefix': 'NiTClk',
    'init_function': None,
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nitclk',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niTClk.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niTClk_64.dll',
                'type': 'cdll'
            }
        }
    },
    'module_name': 'nitclk',
    'repeated_capabilities': [
    ],
    'session_class_description': 'An NI-TClk session.',
    'session_handle_parameter_name': 'session_number'
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nitclk/metadata/config_addon.py sha256=531b9a0fbd58b0e49a96de19dad677c606846d87a9439236706c722498514644 bytes=259 -->
## FILE: src/nitclk/metadata/config_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nitclk/metadata/config_addon.py`
- sha256: `531b9a0fbd58b0e49a96de19dad677c606846d87a9439236706c722498514644`
- bytes: 259

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.4.10.dev0',
    'latest_runtime_version_tested_against': '2025 Q4',
    'initial_release_year': '2019',
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nitclk/metadata/enums.py sha256=557c5bfe577d2e8211c911586d6a2fe501f0e6168b3091e6a082e0705574b6be bytes=105 -->
## FILE: src/nitclk/metadata/enums.py

- repository: `ni/nimi-python`
- source_path: `src/nitclk/metadata/enums.py`
- sha256: `557c5bfe577d2e8211c911586d6a2fe501f0e6168b3091e6a082e0705574b6be`
- bytes: 105

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-TClk API metadata version 25.0.0f93
enums = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nitclk/metadata/enums_addon.py sha256=3d8508ed4539dfd142bac23996f2f69f4bce127c9101b100dd4cb8b982c0043a bytes=452 -->
## FILE: src/nitclk/metadata/enums_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nitclk/metadata/enums_addon.py`
- sha256: `3d8508ed4539dfd142bac23996f2f69f4bce127c9101b100dd4cb8b982c0043a`
- bytes: 452

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

# We are not code genning enums that have been marked as obsolete prior to the initial
# Python API bindings release
# We also do not codegen enums associated with P2P or External Calibration since neither 
# are supported in Python
enums_codegen_method = {
}

enums_additional_enums = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nitclk/metadata/functions.py sha256=0d7d9568b88661e2f685a3aacc4b866b1c5e2cef2af51925285fe17e38b39ae2 bytes=35055 -->
## FILE: src/nitclk/metadata/functions.py

- repository: `ni/nimi-python`
- source_path: `src/nitclk/metadata/functions.py`
- sha256: `0d7d9568b88661e2f685a3aacc4b866b1c5e2cef2af51925285fe17e38b39ae2`
- bytes: 35055

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-TClk API metadata version 25.0.0f93
functions = {
    'ConfigureForHomogeneousTriggers': {
        'documentation': {
            'description': '\nConfigures the attributes commonly required for the TClk synchronization\nof device sessions with homogeneous triggers in a single PXI chassis or\na single PC. Use niTClk_ConfigureForHomogeneousTriggers to configure\nthe attributes for the reference clocks, start triggers, reference\ntriggers, script triggers, and pause triggers. If\nniTClk_ConfigureForHomogeneousTriggers cannot perform all the steps\nappropriate for the given sessions, it returns an error. If an error is\nreturned, use the instrument driver functions and attributes for signal\nrouting, along with the following NI-TClk attributes:\nNITCLK_ATTR_START_TRIGGER_MASTER_SESSION\nNITCLK_ATTR_REF_TRIGGER_MASTER_SESSION\nNITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION\nniTClk_ConfigureForHomogeneousTriggers affects the following clocks and\ntriggers: - Reference clocks - Start triggers - Reference triggers -\nScript triggers - Pause triggers Reference Clocks\nniTClk_ConfigureForHomogeneousTriggers configures the reference clocks\nif they are needed. Specifically, if the internal sample clocks or\ninternal sample clock timebases are used, and the reference clock source\nis not configured--or is set to None (no trigger\nconfigured)--niTClk_ConfigureForHomogeneousTriggers configures the\nfollowing: PXI--The reference clock source on all devices is set to be\nthe 10 MHz PXI backplane clock (PXI_CLK10). PCI--One of the devices\nexports its 10 MHz onboard reference clock to RTSI 7. The reference\nclock source on all devices is set to be RTSI 7. Note: If the reference\nclock source is set to a value other than None,\nniTClk_ConfigureForHomogeneousTriggers cannot configure the reference\nclock source. Start Triggers If the start trigger is set to None (no\ntrigger configured) for all sessions, the sessions are configured to\nshare the start trigger. The start trigger is shared by: - Implicitly\nexporting the start trigger from one session - Configuring the other\nsessions for digital edge start triggers with sources corresponding to\nthe exported start trigger - Setting\nNITCLK_ATTR_START_TRIGGER_MASTER_SESSION to the session that is\nexporting the trigger for all sessions If the start triggers are None\nfor all except one session, niTClk_ConfigureForHomogeneousTriggers\nconfigures the sessions to share the start trigger from the one excepted\nsession. The start trigger is shared by: - Implicitly exporting start\ntrigger from the session with the start trigger that is not None -\nConfiguring the other sessions for digital-edge start triggers with\nsources corresponding to the exported start trigger - Setting\nNITCLK_ATTR_START_TRIGGER_MASTER_SESSION to the session that is\nexporting the trigger for all sessions If start triggers are configured\nfor all sessions, niTClk_ConfigureForHomogeneousTriggers does not\naffect the start triggers. Start triggers are considered to be\nconfigured for all sessions if either of the following conditions is\ntrue: - No session has a start trigger that is None - One session has a\nstart trigger that is None, and all other sessions have start triggers\nother than None. The one session with the None trigger must have\nNITCLK_ATTR_START_TRIGGER_MASTER_SESSION set to itself, indicating\nthat the session itself is the start trigger master Reference Triggers\nniTClk_ConfigureForHomogeneousTriggers configures sessions that support\nreference triggers to share the reference triggers if the reference\ntriggers are None (no trigger configured) for all except one session.\nThe reference triggers are shared by: - Implicitly exporting the\nreference trigger from the session whose reference trigger is not None -\nConfiguring the other sessions that support the reference trigger for\ndigital-edge reference triggers with sources corresponding to the\nexported reference trigger - Setting\nNITCLK_ATTR_REF_TRIGGER_MASTER_SESSION to the session that is\nexporting the trigger for all sessions that support reference trigger If\nthe reference triggers are configured for all sessions that support\nreference triggers, niTClk_ConfigureForHomogeneousTriggers does not\naffect the reference triggers. Reference triggers are considered to be\nconfigured for all sessions if either one or the other of the following\nconditions is true: - No session has a reference trigger that is None -\nOne session has a reference trigger that is None, and all other sessions\nhave reference triggers other than None. The one session with the None\ntrigger must have NITCLK_ATTR_REF_TRIGGER_MASTER_SESSION set to\nitself, indicating that the session itself is the reference trigger\nmaster Reference Trigger Holdoffs Acquisition sessions may be configured\nwith the reference trigger. For acquisition sessions, when the reference\ntrigger is shared, niTClk_ConfigureForHomogeneousTriggers configures\nthe holdoff attributes (which are instrument driver specific) on the\nreference trigger master session so that the session does not recognize\nthe reference trigger before the other sessions are ready. This\ncondition is only relevant when the sample clock rates, sample clock\ntimebase rates, sample counts, holdoffs, and/or any delays for the\nacquisitions are different. When the sample clock rates, sample clock\ntimebase rates, and/or the sample counts are different in acquisition\nsessions sharing the reference trigger, you should also set the holdoff\nattributes for the reference trigger master using the instrument driver.\nPause Triggers\nniTClk_ConfigureForHomogeneousTriggers configures generation sessions\nthat support pause triggers to share them, if the pause triggers are\nNone (no trigger configured) for all except one session. The pause\ntriggers are shared by: - Implicitly exporting the pause trigger from\nthe session whose script trigger is not None - Configuring the other\nsessions that support the pause trigger for digital-edge pause triggers\nwith sources corresponding to the exported pause trigger - Setting\nNITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION to the session that is\nexporting the trigger for all sessions that support script triggers If\nthe pause triggers are configured for all generation sessions that\nsupport pause triggers, niTClk_ConfigureForHomogeneousTriggers does not\naffect pause triggers. Pause triggers are considered to be configured\nfor all sessions if either one or the other of the following conditions\nis true: - No session has a pause trigger that is None - One session has\na pause trigger that is None and all other sessions have pause triggers\nother than None. The one session with the None trigger must have\nNITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION set to itself, indicating\nthat the session itself is the pause trigger master Note: TClk\nsynchronization is not supported for pause triggers on acquisition\nsessions.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the sessions array'
                },
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'sessions is an array of sessions that are being synchronized.'
                },
                'is_session_handle': False,
                'name': 'sessions',
                'python_api_converter_name': 'convert_to_nitclk_session_number_list',
                'size': {
                    'mechanism': 'len',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]',
                'type_in_documentation': 'list of instrument-specific sessions or nitclk.SessionReference instances'
            }
        ],
        'returns': 'ViStatus'
    },
    'FinishSyncPulseSenderSynchronize': {
        'documentation': {
            'description': 'Finishes synchronizing the Sync Pulse Sender.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the sessions array'
                },
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'sessions is an array of sessions that are being synchronized.'
                },
                'is_session_handle': False,
                'name': 'sessions',
                'python_api_converter_name': 'convert_to_nitclk_session_number_list',
                'size': {
                    'mechanism': 'len',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]',
                'type_in_documentation': 'list of instrument-specific sessions or nitclk.SessionReference instances'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nMinimal period of TClk, expressed in seconds. Supported values are\nbetween 0.0 s and 0.050 s (50 ms). Minimal period for a single\nchassis/PC is 200 ns. If the specified value is less than 200 ns,\nNI-TClk automatically coerces minTime to 200 ns. For multichassis\nsynchronization, adjust this value to account for propagation delays\nthrough the various devices and cables.\n'
                },
                'name': 'minTime',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Gets the value of an NI-TClk ViReal64 attribute.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'session references the sessions being synchronized.'
                },
                'name': 'session',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass VI_NULL or an empty string'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe ID of the attribute that you want to get Supported Attribute\nNITCLK_ATTR_SAMPLE_CLOCK_DELAY\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The value that you are getting'
                },
                'name': 'value',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViSession': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Gets the value of an NI-TClk ViSession attribute.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'session references the sessions being synchronized.'
                },
                'name': 'session',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass VI_NULL or an empty string'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe ID of the attribute that you want to set Supported Attributes\nNITCLK_ATTR_START_TRIGGER_MASTER_SESSION\nNITCLK_ATTR_REF_TRIGGER_MASTER_SESSION\nNITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The value that you are getting'
                },
                'is_session_handle': False,
                'name': 'value',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function queries the value of an NI-TClk ViString attribute. You\nmust provide a ViChar array to serve as a buffer for the value. You pass\nthe number of bytes in the buffer as bufSize. If the current value of\nthe attribute, including the terminating NULL byte, is larger than the\nsize you indicate in bufSize, the function copies bufSize minus 1 bytes\ninto the buffer, places an ASCII NULL byte at the end of the buffer, and\nreturns the array size that you must pass to get the entire value. For\nexample, if the value is "123456" and bufSize is 4, the function places\n"123" into the buffer and returns 7. If you want to call\nniTClk_GetAttributeViString just to get the required array size, pass 0\nfor bufSize and VI_NULL for the value.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'session references the sessions being synchronized.'
                },
                'name': 'session',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass VI_NULL or an empty string'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe ID of the attribute that you want to get Supported Attributes\nNITCLK_ATTR_SYNC_PULSE_SOURCE\nNITCLK_ATTR_SYNC_PULSE_CLOCK_SOURCE\nNITCLK_ATTR_EXPORTED_SYNC_PULSE_OUTPUT_TERMINAL\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe number of bytes in the ViChar array that you specify for the value\nparameter\n'
                },
                'name': 'bufSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The value that you are getting'
                },
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtendedErrorInfo': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReports extended error information for the most recent NI-TClk function\nthat returned an error. To establish the function that returned an\nerror, use the return values of the individual functions because once\nniTClk_GetExtendedErrorInfo reports an errorString, it does not report\nan empty string again.\n'
        },
        'included_in_proto': True,
        'is_error_handling': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'none'
            }
        ],
        'parameters': [
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nExtended error description. If errorString is NULL, then it is not large\nenough to hold the entire error description. In this case, the return\nvalue of niTClk_GetExtendedErrorInfo is the size that you should use\nfor niTClk_GetExtendedErrorInfo to return the full error string.\n'
                },
                'name': 'errorString',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'errorStringSize'
                },
                'type': 'ViChar[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSize of the errorString. If errorStringSize is 0, then it is not large\nenough to hold the entire error description. In this case, the return\nvalue of niTClk_GetExtendedErrorInfo is the size that you should use\nfor niTClk_GetExtendedErrorInfo to return the full error string.\n'
                },
                'name': 'errorStringSize',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'Initiate': {
        'documentation': {
            'description': '\nInitiates the acquisition or generation sessions specified, taking into\nconsideration any special requirements needed for synchronization. For\nexample, the session exporting the TClk-synchronized start trigger is\nnot initiated until after niTClk_Initiate initiates all the sessions\nthat import the TClk-synchronized start trigger.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the sessions array'
                },
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'sessions is an array of sessions that are being synchronized.'
                },
                'is_session_handle': False,
                'name': 'sessions',
                'python_api_converter_name': 'convert_to_nitclk_session_number_list',
                'size': {
                    'mechanism': 'len',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]',
                'type_in_documentation': 'list of instrument-specific sessions or nitclk.SessionReference instances'
            }
        ],
        'returns': 'ViStatus'
    },
    'IsDone': {
        'documentation': {
            'description': '\nMonitors the progress of the acquisitions and/or generations\ncorresponding to sessions.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the sessions array'
                },
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'sessions is an array of sessions that are being synchronized.'
                },
                'is_session_handle': False,
                'name': 'sessions',
                'python_api_converter_name': 'convert_to_nitclk_session_number_list',
                'size': {
                    'mechanism': 'len',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]',
                'type_in_documentation': 'list of instrument-specific sessions or nitclk.SessionReference instances'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nIndicates that the operation is done. The operation is done when each\nsession has completed without any errors or when any one of the sessions\nreports an error.\n'
                },
                'name': 'done',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of an NI-TClk VIReal64 attribute.\nniTClk_SetAttributeViReal64 is a low-level function that you can use to\nset the values NI-TClk attributes. NI-TClk contains high-level functions\nthat set most of the attributes. It is best to use the high-level\nfunctions as much as possible.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'session references the sessions being synchronized.'
                },
                'name': 'session',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass VI_NULL or an empty string'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe ID of the attribute that you want to set Supported Attribute\nNITCLK_ATTR_SAMPLE_CLOCK_DELAY\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The value for the attribute'
                },
                'grpc_name': 'value_raw',
                'name': 'value',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViSession': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of an NI-TClk ViSession attribute.\nniTClk_SetAttributeViSession is a low-level function that you can use\nto set the values NI-TClk attributes. NI-TClk contains high-level\nfunctions that set most of the attributes. It is best to use the\nhigh-level functions as much as possible.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'session references the sessions being synchronized.'
                },
                'name': 'session',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass VI_NULL or an empty string'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe ID of the attribute that you want to set Supported Attributes\nNITCLK_ATTR_START_TRIGGER_MASTER_SESSION\nNITCLK_ATTR_REF_TRIGGER_MASTER_SESSION\nNITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The value for the attribute'
                },
                'is_session_handle': False,
                'name': 'value',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of an NI-TClk VIString attribute.\nniTClk_SetAttributeViString is a low-level function that you can use to\nset the values of NI-TClk attributes. NI-TClk contain high-level\nfunctions that set most of the attributes. It is best to use the\nhigh-level functions as much as possible.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'session references the sessions being synchronized.'
                },
                'name': 'session',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass VI_NULL or an empty string'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the ID of the attribute that you want to set Supported Attributes\nNITCLK_ATTR_SYNC_PULSE_SOURCE\nNITCLK_ATTR_SYNC_PULSE_CLOCK_SOURCE\nNITCLK_ATTR_EXPORTED_SYNC_PULSE_OUTPUT_TERMINAL\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value for the attribute'
                },
                'grpc_name': 'value_raw',
                'name': 'value',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetupForSyncPulseSenderSynchronize': {
        'documentation': {
            'description': 'Configures the TClks on all the devices and prepares the Sync Pulse Sender for synchronization'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the sessions array'
                },
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'sessions is an array of sessions that are being synchronized.'
                },
                'is_session_handle': False,
                'name': 'sessions',
                'python_api_converter_name': 'convert_to_nitclk_session_number_list',
                'size': {
                    'mechanism': 'len',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]',
                'type_in_documentation': 'list of instrument-specific sessions or nitclk.SessionReference instances'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nMinimal period of TClk, expressed in seconds. Supported values are\nbetween 0.0 s and 0.050 s (50 ms). Minimal period for a single\nchassis/PC is 200 ns. If the specified value is less than 200 ns,\nNI-TClk automatically coerces minTime to 200 ns. For multichassis\nsynchronization, adjust this value to account for propagation delays\nthrough the various devices and cables.\n'
                },
                'name': 'minTime',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'Synchronize': {
        'documentation': {
            'description': '\nSynchronizes the TClk signals on the given sessions. After\nniTClk_Synchronize executes, TClk signals from all sessions are\nsynchronized. Note: Before using this NI-TClk function, verify that your\nsystem is configured as specified in the PXI Trigger Lines and RTSI\nLines topic of the NI-TClk Synchronization Help. You can locate this\nhelp file at Start>>Programs>>National Instruments>>NI-TClk.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the sessions array'
                },
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'sessions is an array of sessions that are being synchronized.'
                },
                'is_session_handle': False,
                'name': 'sessions',
                'python_api_converter_name': 'convert_to_nitclk_session_number_list',
                'size': {
                    'mechanism': 'len',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]',
                'type_in_documentation': 'list of instrument-specific sessions or nitclk.SessionReference instances'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nMinimal period of TClk, expressed in seconds. Supported values are\nbetween 0.0 s and 0.050 s (50 ms). Minimal period for a single\nchassis/PC is 200 ns. If the specified value is less than 200 ns,\nNI-TClk automatically coerces minTime to 200 ns. For multichassis\nsynchronization, adjust this value to account for propagation delays\nthrough the various devices and cables.\n'
                },
                'name': 'minTclkPeriod',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'SynchronizeToSyncPulseSender': {
        'documentation': {
            'description': 'Synchronizes the other devices to the Sync Pulse Sender.'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the sessions array'
                },
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'sessions is an array of sessions that are being synchronized.'
                },
                'is_session_handle': False,
                'name': 'sessions',
                'python_api_converter_name': 'convert_to_nitclk_session_number_list',
                'size': {
                    'mechanism': 'len',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]',
                'type_in_documentation': 'list of instrument-specific sessions or nitclk.SessionReference instances'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nMinimal period of TClk, expressed in seconds. Supported values are\nbetween 0.0 s and 0.050 s (50 ms). Minimal period for a single\nchassis/PC is 200 ns. If the specified value is less than 200 ns,\nNI-TClk automatically coerces minTime to 200 ns. For multichassis\nsynchronization, adjust this value to account for propagation delays\nthrough the various devices and cables.\n'
                },
                'name': 'minTime',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'WaitUntilDone': {
        'documentation': {
            'description': '\nCall this function to pause execution of your program until the\nacquisitions and/or generations corresponding to sessions are done or\nuntil the function returns a timeout error. niTClk_WaitUntilDone is a\nblocking function that periodically checks the operation status. It\nreturns control to the calling program if the operation completes\nsuccessfully or an error occurs (including a timeout error). This\nfunction is most useful for finite data operations that you expect to\ncomplete within a certain time.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of elements in the sessions array'
                },
                'name': 'sessionCount',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'sessions is an array of sessions that are being synchronized.'
                },
                'is_session_handle': False,
                'name': 'sessions',
                'python_api_converter_name': 'convert_to_nitclk_session_number_list',
                'size': {
                    'mechanism': 'len',
                    'value': 'sessionCount'
                },
                'type': 'ViSession[]',
                'type_in_documentation': 'list of instrument-specific sessions or nitclk.SessionReference instances'
            },
            {
                'default_value': 'hightime.timedelta(seconds=0.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe amount of time in seconds that niTClk_WaitUntilDone waits for the\nsessions to complete. If timeout is exceeded, niTClk_WaitUntilDone\nreturns an error.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    }
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nitclk/metadata/functions_addon.py sha256=716565fdf9a08d0b08eb7f50e3970e05b616648c56db3868559273033dc90b57 bytes=1583 -->
## FILE: src/nitclk/metadata/functions_addon.py

- repository: `ni/nimi-python`
- source_path: `src/nitclk/metadata/functions_addon.py`
- sha256: `716565fdf9a08d0b08eb7f50e3970e05b616648c56db3868559273033dc90b57`
- bytes: 1583

````python
# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

# By default all functions in functions.py are "public".
# This will override that with private (prefixes name with '_'), or don't generate at all
functions_codegen_method = {
}

functions_locking = {
}

# Attach the given parameter to the given enum from enums.py
functions_enums = {
}

# This is the additional metadata needed by the code generator in order create code that can properly handle buffer allocation.
functions_buffer_info = {
}

# These are functions we mark as "error_handling":True. The generator uses this information to
# change how error handling is done within those functions themselves - basically, if an error occurs,
# dont try to handle it, since the functions are only used within the context of error handling.
functions_is_error_handling = {
}

# There are some parameters that are needed in the C function call we use under the hood, but that we do not want in the Python API
functions_remove_from_python_api = {
}

# Default values for method parameters
functions_default_value = {
}

# Parameter that need to be array.array
functions_array = {
}

# We want to use a common name for self_cal across all drivers
functions_name = {
}

# Functions not in original metadata.
functions_additional_functions = {
}

# Converted parameters
functions_converters = {
}

# The extracted metadata is incorrect. Patch it here.
functions_bad_source_metadata = {
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nitclk/nitclk.mak sha256=185aa2c872ec9a8cb6e5fdf5254eb0c867c8340986e481f1778a5bbc26e92bb0 bytes=978 -->
## FILE: src/nitclk/nitclk.mak

- repository: `ni/nimi-python`
- source_path: `src/nitclk/nitclk.mak`
- sha256: `185aa2c872ec9a8cb6e5fdf5254eb0c867c8340986e481f1778a5bbc26e92bb0`
- bytes: 978

````makefile


include $(BUILD_HELPER_DIR)/defines.mak

MODULE_FILES_TO_GENERATE := $(filter-out enums.py,$(DEFAULT_PY_FILES_TO_GENERATE))

MODULE_FILES_TO_COPY := $(DEFAULT_PY_FILES_TO_COPY)

RST_FILES_TO_GENERATE := $(filter-out rep_caps.rst enums.rst,$(DEFAULT_RST_FILES_TO_GENERATE))

SPHINX_CONF_PY := $(DEFAULT_SPHINX_CONF_PY)
READTHEDOCS_CONFIG := $(DEFAULT_READTHEDOCS_CONFIG)

include $(BUILD_HELPER_DIR)/rules.mak

# We need to override the default rule for generating session since we have
# a specialized copy for TClk
$(MODULE_DIR)/session.py: $(DRIVER_DIR)/templates/session.py.mako $(BUILD_HELPER_SCRIPTS) $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call GENERATE_SCRIPT, $<, $(MODULE_DIR), $(METADATA_DIR))

$(DRIVER_DOCS_DIR)/class.rst: $(DRIVER_DIR)/templates/class.rst.mako $(BUILD_HELPER_SCRIPTS) $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call GENERATE_SCRIPT, $<, $(DRIVER_DOCS_DIR), $(METADATA_DIR))
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nitclk/system_tests/test_system_nitclk.py sha256=644a516d155c8a156ebc5f91233daa01aadba26577d80bee2aa87b61f4d79540 bytes=4002 -->
## FILE: src/nitclk/system_tests/test_system_nitclk.py

- repository: `ni/nimi-python`
- source_path: `src/nitclk/system_tests/test_system_nitclk.py`
- sha256: `644a516d155c8a156ebc5f91233daa01aadba26577d80bee2aa87b61f4d79540`
- bytes: 4002

````python
#!/usr/bin/python

import niscope
import nitclk
import pytest


@pytest.fixture(scope='function')
def single_niscope_session():
    with niscope.Session('', False, False, 'Simulate=1, DriverSetup=Model:5164;BoardType:PXIe') as simulated_session:
        yield simulated_session


@pytest.fixture(scope='function')
def multiple_niscope_sessions():
    with niscope.Session('', False, False, 'Simulate=1, DriverSetup=Model:5164;BoardType:PXIe') as simulated_session_1, niscope.Session('', False, False, 'Simulate=1, DriverSetup=Model:5164;BoardType:PXIe') as simulated_session_2:
        yield [simulated_session_1, simulated_session_2]


def test_nitclk_integration(single_niscope_session):
    assert isinstance(single_niscope_session.tclk, nitclk.SessionReference)


def test_nitclk_vi_string(single_niscope_session):
    # default is empty string
    assert single_niscope_session.tclk.exported_tclk_output_terminal == ''
    single_niscope_session.tclk.exported_tclk_output_terminal = 'PXI_Trig0'
    assert single_niscope_session.tclk.exported_tclk_output_terminal == 'PXI_Trig0'


def test_nitclk_session_reference(single_niscope_session):
    test_session = niscope.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe')
    single_niscope_session.tclk.ref_trigger_master_session = test_session
    # We need to look at the actual session number inside the class
    # we know the type returned from session.tclk.pause_trigger_master_session will be nitclk.SessionReference
    # This test assumes knowledge of the class internals
    assert single_niscope_session.tclk.ref_trigger_master_session._interpreter._session_number == test_session.tclk._get_tclk_session_reference()
    assert single_niscope_session.tclk.ref_trigger_master_session._interpreter._session_number == test_session._interpreter._vi


def test_nitclk_vi_real64(single_niscope_session):
    # default is 0
    assert single_niscope_session.tclk.sample_clock_delay.total_seconds() == 0
    test_number = 4.2
    single_niscope_session.tclk.sample_clock_delay = test_number
    assert single_niscope_session.tclk.sample_clock_delay.total_seconds() == test_number


def test_nitclk_error_handling():
    test_session_reference = nitclk.SessionReference(42)  # Invalid session
    try:
        test_session_reference.exported_tclk_output_terminal = 'test'
        assert False
    except nitclk.errors.DriverError as e:
        assert e.code == -250032


def test_nitclk_configure_for_homogeneous_triggers(multiple_niscope_sessions):
    nitclk.configure_for_homogeneous_triggers(multiple_niscope_sessions)


def test_nitclk_sync_pulse_sender_synchronize(multiple_niscope_sessions):
    nitclk.configure_for_homogeneous_triggers(multiple_niscope_sessions)
    nitclk.setup_for_sync_pulse_sender_synchronize(multiple_niscope_sessions, .001)
    nitclk.synchronize_to_sync_pulse_sender(multiple_niscope_sessions, .001)
    nitclk.finish_sync_pulse_sender_synchronize(multiple_niscope_sessions, .001)


def test_nitclk_synchronize(multiple_niscope_sessions):
    nitclk.configure_for_homogeneous_triggers(multiple_niscope_sessions)
    nitclk.synchronize(multiple_niscope_sessions, .001)


def test_nitclk_initiate(multiple_niscope_sessions):
    nitclk.configure_for_homogeneous_triggers(multiple_niscope_sessions)
    nitclk.synchronize(multiple_niscope_sessions, .001)
    nitclk.initiate(multiple_niscope_sessions)


def test_nitclk_is_done(multiple_niscope_sessions):
    nitclk.configure_for_homogeneous_triggers(multiple_niscope_sessions)
    nitclk.synchronize(multiple_niscope_sessions, .001)
    nitclk.initiate(multiple_niscope_sessions)
    nitclk.is_done(multiple_niscope_sessions)


def test_nitclk_wait_until_done(multiple_niscope_sessions):
    nitclk.configure_for_homogeneous_triggers(multiple_niscope_sessions)
    nitclk.synchronize(multiple_niscope_sessions, .001)
    nitclk.initiate(multiple_niscope_sessions)
    nitclk.wait_until_done(multiple_niscope_sessions, .001)
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nitclk/templates/_library_interpreter.py/_get_error_description.py.mako sha256=94a9b2373f0e43d1af0afd758f57d5973696b246efe274028546138801fdc514 bytes=325 -->
## FILE: src/nitclk/templates/_library_interpreter.py/_get_error_description.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nitclk/templates/_library_interpreter.py/_get_error_description.py.mako`
- sha256: `94a9b2373f0e43d1af0afd758f57d5973696b246efe274028546138801fdc514`
- bytes: 325

````mako
    def get_error_description(self, error_code):
        '''get_error_description

        Returns the error description.
        '''
        try:
            error_string = self.get_extended_error_info()
            return error_string
        except errors.Error:
            return "Failed to retrieve error description."
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nitclk/templates/class.rst.mako sha256=74803805289d04490d7ca498f1d30cc71ee2f1ebee53ec2c86c9cbdff884c4cb bytes=4310 -->
## FILE: src/nitclk/templates/class.rst.mako

- repository: `ni/nimi-python`
- source_path: `src/nitclk/templates/class.rst.mako`
- sha256: `74803805289d04490d7ca498f1d30cc71ee2f1ebee53ec2c86c9cbdff884c4cb`
- bytes: 4310

````mako
<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    driver_name = config['driver_name']
    c_function_prefix = config['c_function_prefix']

    functions_all = template_parameters['metadata'].functions
    functions = helper.filter_public_functions(functions_all)

    if 'context_manager_name' in config:
        # Add a InitiateDoc entry - only used to add initiate() to the Session documentation
        initiate_doc = helper.initiate_function_def_for_doc(functions_all, config)
        if initiate_doc is not None:
            functions['InitiateDoc'] = initiate_doc

    doc_list = {}
    for fname in sorted(functions):
        for method_template in functions[fname]['method_templates']:
            name =  functions[fname]['python_name'] + method_template['method_python_name_suffix']
            doc_list[name] = { 'filename': method_template['documentation_filename'], 'method_template': method_template, 'function': functions[fname], }

    attributes = helper.filter_codegen_attributes_public_only(config['attributes'])
%>\

.. py:module:: ${module_name}

${helper.get_rst_header_snippet('Public API', '=')}

The `nitclk` module provides synchronization facilites to allow multiple instruments to simultaneously
respond to triggers, to align Sample Clocks on multiple instruments, and/or to simultaneously start multiple
instruments.

It consists of a set of functions that act on a list of :py:class:`SessionReference` objects or instrument `Session`
objects for drivers that support NI-TClk. :py:class:`SessionReference` also has a set of properties for configuration.

.. code:: python

    with niscope.Session('dev1') as scope1, niscope.Session('dev2') as scope2:
        nitclk.configure_for_homogeneous_triggers([scope1, scope2])
        nitclk.initiate([scope1, scope2])
        wfm1 = scope1.fetch()
        wfm2 = scope2.fetch()

% for item in sorted(doc_list):
<%
function_item = doc_list[item]
%>\
${helper.get_rst_header_snippet(item, '-')}

    .. py:currentmodule:: ${module_name}

    ${helper.get_function_rst(function_item['function'], method_template=function_item['method_template'], numpy=False, config=config, indent=4, method_or_function='function')}

% endfor

${helper.get_rst_header_snippet('SessionReference', '=')}
.. py:currentmodule:: ${module_name}

.. py:class:: SessionReference(session_number)

    Helper class that contains all NI-TClk properties. This class is what is returned by
    any nimi-python Session class tclk attribute when the driver supports NI-TClk

    .. code:: python

        with niscope.Session('dev1') as session:
            session.tclk.sample_clock_delay = .42

    ..note:: Constructing this class is an advanced use case and should not be needed in most circumstances.

    :param session_number:
        nitclk session
    :type session_number: int, nimi-python Session class, SessionReference


% for attr in helper.sorted_attrs(attributes):
${helper.get_rst_header_snippet(attributes[attr]["python_name"], '-')}

    .. py:currentmodule:: ${module_name}.SessionReference

    .. py:attribute:: ${attributes[attr]["python_name"]}

<%
a = attributes[attr]
table_contents = [
         ('Characteristic', 'Value'),
         ('Datatype', a['type_in_documentation']),
         ('Permissions', a['access']),
         ]
if helper.module_supports_repeated_caps(config):
    table_contents.append(('Repeated Capabilities', helper.get_attribute_repeated_caps(a)))

table = helper.as_rest_table(table_contents)

helper.add_attribute_rep_cap_tip(a, config)

desc = helper.get_documentation_for_node_rst(a, config, indent=0)
%>\
        ${helper.get_indented_docstring_snippet(desc, indent=8)}

        The following table lists the characteristics of this property.

            ${helper.get_indented_docstring_snippet(table, indent=12)}

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

%   if 'lv_property' in attributes[attr] and len(attributes[attr]['lv_property']) > 0:
                - LabVIEW Property: **${attributes[attr]['lv_property'].strip()}**
%   endif
                - C Attribute: **${c_function_prefix.upper()}ATTR_${attributes[attr]["name"].upper()}**

% endfor

.. contents:: nitclk
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nitclk/templates/session.py.mako sha256=5dcf34aa42c92985c26b1ed90f4d7162329be22e8799d20b96bc9f89377ac2ee bytes=5250 -->
## FILE: src/nitclk/templates/session.py.mako

- repository: `ni/nimi-python`
- source_path: `src/nitclk/templates/session.py.mako`
- sha256: `5dcf34aa42c92985c26b1ed90f4d7162329be22e8799d20b96bc9f89377ac2ee`
- bytes: 5250

````mako
# This file was generated
<%
    import build.helper as helper

    config            = template_parameters['metadata'].config
    attributes        = helper.filter_codegen_attributes(config['attributes'])
    functions         = config['functions']

    module_name       = config['module_name']
    c_function_prefix = config['c_function_prefix']

    functions = helper.filter_codegen_functions(functions)
%>\

import hightime

import ${module_name}._attributes as _attributes
import ${module_name}._converters as _converters
import ${module_name}._library_interpreter as _library_interpreter

# Used for __repr__ and __str__
import pprint
pp = pprint.PrettyPrinter(indent=4)


class SessionReference(object):
    '''Properties container for NI-TClk attributes.

    Note: Constructing this class is an advanced use case and should not be needed in most circumstances.
    '''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

% for attribute in helper.sorted_attrs(attributes):
<%
helper.add_attribute_rep_cap_tip(attributes[attribute], config)
%>\
    %if attributes[attribute]['enum']:
    ${attributes[attribute]['python_name']} = _attributes.AttributeEnum(_attributes.Attribute${attributes[attribute]['type']}, enums.${enums[attributes[attribute]['enum']]['python_name']}, ${attribute})
    %else:
    ${attributes[attribute]['python_name']} = _attributes.${attributes[attribute]['attribute_class']}(${attribute})
    %endif
%   if 'documentation' in attributes[attribute] and len(helper.get_documentation_for_node_docstring(attributes[attribute], config, indent=4).strip()) > 0:
    '''Type: ${attributes[attribute]['type_in_documentation']}

    ${helper.get_documentation_for_node_docstring(attributes[attribute], config, indent=4)}
    '''
%   endif
% endfor

    def __init__(self, ${config['session_handle_parameter_name']}, encoding='windows-1251'):
        self._interpreter = _library_interpreter.LibraryInterpreter(encoding)
        self._interpreter.set_session_handle(${config['session_handle_parameter_name']})
        # We need a self._repeated_capability string for passing down to function calls on the LibraryInterpreter class. We just need to set it to empty string.
        self._repeated_capability = ''

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("${config['session_handle_parameter_name']}=" + pp.pformat(${config['session_handle_parameter_name']}))
        param_list.append("encoding=" + pp.pformat(encoding))
        self._param_list = ', '.join(param_list)

        self._is_frozen = True

    def __repr__(self):
        return '{0}.{1}({2})'.format('${module_name}', self.__class__.__name__, self._param_list)

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("'{0}' object has no attribute '{1}'".format(type(self).__name__, key))
        object.__setattr__(self, key, value)

    def _get_tclk_session_reference(self):
        return self._interpreter.get_session_handle()
% for func_name in sorted({k: v for k, v in functions.items() if v['render_in_session_base']}):
% for method_template in functions[func_name]['method_templates']:
% if method_template['session_filename'] != '/none':

<%include file="${'/session.py' + method_template['session_filename'] + '.py.mako'}" args="f=functions[func_name], config=config, method_template=method_template" />\
% endif
% endfor
% endfor


## The main reason for having this class is to allow reusing the default method template.
class _Session(object):
    '''Private class

    This class allows reusing function templates that are used in all other drivers. If
    we don't do this, we would need new template(s) that the only difference is in the
    indentation.
    '''

    def __init__(self):
        self._interpreter = _library_interpreter.LibraryInterpreter('windows-1251')

        # Instantiate any repeated capability objects
% for rep_cap in config['repeated_capabilities']:
        self.${rep_cap['python_name']} = _RepeatedCapabilities(self, '${rep_cap["prefix"]}')
% endfor

        # Store the parameter list for later printing in __repr__
        param_list = []
        self._param_list = ', '.join(param_list)

        self._is_frozen = True

    ''' These are code-generated '''
% for func_name in sorted({k: v for k, v in functions.items() if not v['render_in_session_base']}):
% for method_template in functions[func_name]['method_templates']:
% if method_template['session_filename'] != '/none':

<%include file="${'/session.py' + method_template['session_filename'] + '.py.mako'}" args="f=functions[func_name], config=config, method_template=method_template" />\
% endif
% endfor
% endfor
% for func_name in sorted({k: v for k, v in functions.items() if not v['render_in_session_base']}):


<%
f = functions[func_name]
name = f['python_name']
parameter_list = helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_PASSTHROUGH_CALL)
%>\
def ${name}(${parameter_list}):
    '''${name}

    ${helper.get_function_docstring(f, False, config, indent=4)}
    '''
    return _Session().${name}(${parameter_list})
% endfor
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/nitclk/unit_tests/test_nitclk.py sha256=8f77df484f446c0e34266cfe011c334ad543d3f0b76eea16a3ae0d90d2a85134 bytes=17529 -->
## FILE: src/nitclk/unit_tests/test_nitclk.py

- repository: `ni/nimi-python`
- source_path: `src/nitclk/unit_tests/test_nitclk.py`
- sha256: `8f77df484f446c0e34266cfe011c334ad543d3f0b76eea16a3ae0d90d2a85134`
- bytes: 17529

````python
import _matchers
import _mock_helper

import hightime
import nitclk

from unittest.mock import MagicMock
from unittest.mock import patch

SESSION_NUM_FOR_TEST = 42
single_session = [SESSION_NUM_FOR_TEST]
multiple_sessions = [SESSION_NUM_FOR_TEST, SESSION_NUM_FOR_TEST * 10, SESSION_NUM_FOR_TEST * 100, SESSION_NUM_FOR_TEST + 1]


class NitclkSupportingDriverSession:
    '''Session objects for drivers that support NI-TClk are expected to have a property of type nitclk.SessionReference called tclk

    This is why we're creating this fake driver class and adding the tclk property.
    '''
    def __init__(self, session_number):
        self.tclk = nitclk.SessionReference(session_number)


class TestNitclkApi:
    class PatchedLibrary(nitclk._library.Library):
        def __init__(self, ctypes_library):
            super().__init__(ctypes_library)

            for f in dir(self):
                if f.startswith("niTClk_") and not f.endswith("_cfunc"):
                    setattr(self, f, MagicMock())

    def setup_method(self, method):
        self.patched_library = self.PatchedLibrary(None)
        self.patched_library_singleton_get = patch('nitclk._library_interpreter._library_singleton.get', return_value=self.patched_library)
        self.patched_library_singleton_get.start()

        self.side_effects_helper = _mock_helper.SideEffectsHelper()
        self.side_effects_helper.set_side_effects_and_return_values(self.patched_library)

        self._single_session_reference = [nitclk.SessionReference(x) for x in single_session]
        self._multiple_session_references = [nitclk.SessionReference(x) for x in multiple_sessions]

    def teardown_method(self, method):
        self.patched_library_singleton_get.stop()

    # API Tests

    def test_initialize_one_session(self):
        self.patched_library.niTClk_Initiate.side_effect = self.side_effects_helper.niTClk_Initiate
        nitclk.initiate(self._single_session_reference)
        self.patched_library.niTClk_Initiate.assert_called_once_with(_matchers.ViUInt32Matcher(len(single_session)), _matchers.ViSessionBufferMatcher(single_session))
        return

    def test_initialize_multiple_sessions(self):
        self.patched_library.niTClk_Initiate.side_effect = self.side_effects_helper.niTClk_Initiate
        nitclk.initiate(self._multiple_session_references)
        self.patched_library.niTClk_Initiate.assert_called_once_with(_matchers.ViUInt32Matcher(len(multiple_sessions)), _matchers.ViSessionBufferMatcher(multiple_sessions))
        return

    def test_configure_for_homogeneous_triggers(self):
        self.patched_library.niTClk_ConfigureForHomogeneousTriggers.side_effect = self.side_effects_helper.niTClk_ConfigureForHomogeneousTriggers
        nitclk.configure_for_homogeneous_triggers(self._multiple_session_references)
        self.patched_library.niTClk_ConfigureForHomogeneousTriggers.assert_called_once_with(_matchers.ViUInt32Matcher(len(multiple_sessions)), _matchers.ViSessionBufferMatcher(multiple_sessions))
        return

    def test_finish_sync_pulse_sender_synchronize(self):
        min_time = 0.042
        self.patched_library.niTClk_FinishSyncPulseSenderSynchronize.side_effect = self.side_effects_helper.niTClk_FinishSyncPulseSenderSynchronize
        nitclk.finish_sync_pulse_sender_synchronize(self._multiple_session_references, min_time)
        self.patched_library.niTClk_FinishSyncPulseSenderSynchronize.assert_called_once_with(_matchers.ViUInt32Matcher(len(multiple_sessions)), _matchers.ViSessionBufferMatcher(multiple_sessions), _matchers.ViReal64Matcher(min_time))
        return

    def test_is_done(self):
        expected_result = True
        self.side_effects_helper['IsDone']['done'] = expected_result

        self.patched_library.niTClk_IsDone.side_effect = self.side_effects_helper.niTClk_IsDone
        actual_result = nitclk.is_done(self._multiple_session_references)
        assert actual_result == expected_result
        self.patched_library.niTClk_IsDone.assert_called_once_with(_matchers.ViUInt32Matcher(len(multiple_sessions)), _matchers.ViSessionBufferMatcher(multiple_sessions), _matchers.ViBooleanPointerMatcher())
        return

    def test_setup_for_sync_pulse_sender_synchronize(self):
        min_time = 0.042
        self.patched_library.niTClk_SetupForSyncPulseSenderSynchronize.side_effect = self.side_effects_helper.niTClk_SetupForSyncPulseSenderSynchronize
        nitclk.setup_for_sync_pulse_sender_synchronize(self._multiple_session_references, min_time)
        self.patched_library.niTClk_SetupForSyncPulseSenderSynchronize.assert_called_once_with(_matchers.ViUInt32Matcher(len(multiple_sessions)), _matchers.ViSessionBufferMatcher(multiple_sessions), _matchers.ViReal64Matcher(min_time))
        return

    def test_synchronize(self):
        min_time = 0.042
        self.patched_library.niTClk_Synchronize.side_effect = self.side_effects_helper.niTClk_Synchronize
        nitclk.synchronize(self._multiple_session_references, min_time)
        self.patched_library.niTClk_Synchronize.assert_called_once_with(_matchers.ViUInt32Matcher(len(multiple_sessions)), _matchers.ViSessionBufferMatcher(multiple_sessions), _matchers.ViReal64Matcher(min_time))
        return

    def test_synchronize_timedelta(self):
        min_time = hightime.timedelta(seconds=0.042)
        self.patched_library.niTClk_Synchronize.side_effect = self.side_effects_helper.niTClk_Synchronize
        nitclk.synchronize(self._multiple_session_references, min_time)
        self.patched_library.niTClk_Synchronize.assert_called_once_with(_matchers.ViUInt32Matcher(len(multiple_sessions)), _matchers.ViSessionBufferMatcher(multiple_sessions), _matchers.ViReal64Matcher(min_time.total_seconds()))
        return

    def test_synchronize_to_sync_pulse_sender(self):
        min_time = 0.042
        self.patched_library.niTClk_SynchronizeToSyncPulseSender.side_effect = self.side_effects_helper.niTClk_SynchronizeToSyncPulseSender
        nitclk.synchronize_to_sync_pulse_sender(self._multiple_session_references, min_time)
        self.patched_library.niTClk_SynchronizeToSyncPulseSender.assert_called_once_with(_matchers.ViUInt32Matcher(len(multiple_sessions)), _matchers.ViSessionBufferMatcher(multiple_sessions), _matchers.ViReal64Matcher(min_time))
        return

    def test_wait_until_done(self):
        min_time = 4.2
        self.patched_library.niTClk_WaitUntilDone.side_effect = self.side_effects_helper.niTClk_WaitUntilDone
        nitclk.wait_until_done(self._multiple_session_references, min_time)
        self.patched_library.niTClk_WaitUntilDone.assert_called_once_with(_matchers.ViUInt32Matcher(len(multiple_sessions)), _matchers.ViSessionBufferMatcher(multiple_sessions), _matchers.ViReal64Matcher(min_time))
        return

    # API error handling

    def test_api_error(self):
        error_string = 'Error'
        self.patched_library.niTClk_Synchronize.side_effect = self.side_effects_helper.niTClk_Synchronize
        self.side_effects_helper['Synchronize']['return'] = -1
        self.patched_library.niTClk_GetExtendedErrorInfo.side_effect = self.side_effects_helper.niTClk_GetExtendedErrorInfo
        self.side_effects_helper['GetExtendedErrorInfo']['errorString'] = error_string
        try:
            nitclk.synchronize(self._multiple_session_references, 0.42)
        except nitclk.Error as e:
            assert e.code == -1
            assert e.description == error_string

    def test_api_get_error_description_fails(self):
        self.patched_library.niTClk_Synchronize.side_effect = self.side_effects_helper.niTClk_Synchronize
        self.side_effects_helper['Synchronize']['return'] = -1
        self.patched_library.niTClk_GetExtendedErrorInfo.side_effect = self.side_effects_helper.niTClk_GetExtendedErrorInfo
        self.side_effects_helper['GetExtendedErrorInfo']['return'] = -2
        try:
            nitclk.synchronize(self._multiple_session_references, 0.42)
        except nitclk.Error as e:
            assert e.code == -1  # we want the original error code from getting the attribute.
            assert e.description == "Failed to retrieve error description."

    # SessionReference error handling

    def test_session_reference_error(self):
        session = nitclk.SessionReference(SESSION_NUM_FOR_TEST)
        error_string = 'Error'
        self.patched_library.niTClk_GetAttributeViReal64.side_effect = self.side_effects_helper.niTClk_GetAttributeViReal64
        self.side_effects_helper['GetAttributeViReal64']['return'] = -1
        self.patched_library.niTClk_GetExtendedErrorInfo.side_effect = self.side_effects_helper.niTClk_GetExtendedErrorInfo
        self.side_effects_helper['GetExtendedErrorInfo']['errorString'] = error_string
        try:
            test = session.sample_clock_delay
            print(test)  # Get rid of flake8 F841
            assert False
        except nitclk.Error as e:
            assert e.code == -1
            assert e.description == error_string

    def test_session_reference_get_error_description_fails(self):
        session = nitclk.SessionReference(SESSION_NUM_FOR_TEST)
        self.patched_library.niTClk_GetAttributeViReal64.side_effect = self.side_effects_helper.niTClk_GetAttributeViReal64
        self.side_effects_helper['GetAttributeViReal64']['return'] = -1
        self.patched_library.niTClk_GetExtendedErrorInfo.side_effect = self.side_effects_helper.niTClk_GetExtendedErrorInfo
        self.side_effects_helper['GetExtendedErrorInfo']['return'] = -2
        try:
            test = session.sample_clock_delay
            print(test)  # Get rid of flake8 F841
            assert False
        except nitclk.Error as e:
            assert e.code == -1  # we want the original error code from getting the attribute.
            assert e.description == "Failed to retrieve error description."

    # Session Reference

    def test_set_vi_real64(self):
        session = nitclk.SessionReference(SESSION_NUM_FOR_TEST)
        self.patched_library.niTClk_SetAttributeViReal64.side_effect = self.side_effects_helper.niTClk_SetAttributeViReal64
        attribute_id = 8
        test_number = 4.2
        session.tclk_actual_period = test_number
        self.patched_library.niTClk_SetAttributeViReal64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViReal64Matcher(test_number))

    def test_get_vi_real64(self):
        session = nitclk.SessionReference(SESSION_NUM_FOR_TEST)
        self.patched_library.niTClk_GetAttributeViReal64.side_effect = self.side_effects_helper.niTClk_GetAttributeViReal64
        attribute_id = 8
        test_number = 4.2
        self.side_effects_helper['GetAttributeViReal64']['value'] = test_number
        attr_val = session.tclk_actual_period
        assert attr_val == test_number
        self.patched_library.niTClk_GetAttributeViReal64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViReal64PointerMatcher())

    def test_set_timedelta_as_vi_real64(self):
        session = nitclk.SessionReference(SESSION_NUM_FOR_TEST)
        self.patched_library.niTClk_SetAttributeViReal64.side_effect = self.side_effects_helper.niTClk_SetAttributeViReal64
        attribute_id = 11
        test_number = 4.2
        session.sample_clock_delay = test_number
        self.patched_library.niTClk_SetAttributeViReal64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViReal64Matcher(test_number))

    def test_set_timedelta_as_timedelta(self):
        session = nitclk.SessionReference(SESSION_NUM_FOR_TEST)
        self.patched_library.niTClk_SetAttributeViReal64.side_effect = self.side_effects_helper.niTClk_SetAttributeViReal64
        attribute_id = 11
        test_number = 4.2
        session.sample_clock_delay = hightime.timedelta(seconds=test_number)
        self.patched_library.niTClk_SetAttributeViReal64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViReal64Matcher(test_number))

    def test_get_timedelta(self):
        session = nitclk.SessionReference(SESSION_NUM_FOR_TEST)
        self.patched_library.niTClk_GetAttributeViReal64.side_effect = self.side_effects_helper.niTClk_GetAttributeViReal64
        attribute_id = 11
        test_number = 4.2
        self.side_effects_helper['GetAttributeViReal64']['value'] = test_number
        attr_timedelta = session.sample_clock_delay
        assert attr_timedelta.total_seconds() == test_number
        self.patched_library.niTClk_GetAttributeViReal64.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViReal64PointerMatcher())

    def test_set_vi_string(self):
        session = nitclk.SessionReference(SESSION_NUM_FOR_TEST)
        self.patched_library.niTClk_SetAttributeViString.side_effect = self.side_effects_helper.niTClk_SetAttributeViString
        attribute_id = 13
        test_string = "The answer to the ultimate question is 42"
        session.sync_pulse_sender_sync_pulse_source = test_string
        self.patched_library.niTClk_SetAttributeViString.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViStringMatcher(test_string))

    def test_get_vi_string(self):
        session = nitclk.SessionReference(SESSION_NUM_FOR_TEST)
        self.patched_library.niTClk_GetAttributeViString.side_effect = self.side_effects_helper.niTClk_GetAttributeViString
        attribute_id = 13
        test_string = "The answer to the ultimate question is 42"
        self.side_effects_helper['GetAttributeViString']['value'] = test_string
        attr_string = session.sync_pulse_sender_sync_pulse_source
        assert attr_string == test_string

        from unittest.mock import call
        calls = [call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt32Matcher(0), None), call(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViInt32Matcher(len(test_string)), _matchers.ViCharBufferMatcher(len(test_string)))]
        self.patched_library.niTClk_GetAttributeViString.assert_has_calls(calls)
        assert self.patched_library.niTClk_GetAttributeViString.call_count == 2

    # All ViInt32 attributes are really sessions references
    def test_set_vi_session_with_int(self):
        session = nitclk.SessionReference(SESSION_NUM_FOR_TEST)
        self.patched_library.niTClk_SetAttributeViSession.side_effect = self.side_effects_helper.niTClk_SetAttributeViSession
        other_session_number = 43
        # We do not support using just the number
        try:
            session.start_trigger_master_session = other_session_number
            assert False
        except TypeError:
            pass

    def test_set_vi_session_with_session_reference(self):
        session = nitclk.SessionReference(SESSION_NUM_FOR_TEST)
        self.patched_library.niTClk_SetAttributeViSession.side_effect = self.side_effects_helper.niTClk_SetAttributeViSession
        attribute_id = 3
        other_session_number = 43
        other_session_reference = nitclk.SessionReference(other_session_number)
        session.start_trigger_master_session = other_session_reference
        self.patched_library.niTClk_SetAttributeViSession.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViSessionMatcher(other_session_number))

    def test_set_vi_session_with_session(self):
        session = nitclk.SessionReference(SESSION_NUM_FOR_TEST)
        self.patched_library.niTClk_SetAttributeViSession.side_effect = self.side_effects_helper.niTClk_SetAttributeViSession
        attribute_id = 3
        other_session_number = 43
        other_session = NitclkSupportingDriverSession(other_session_number)
        session.start_trigger_master_session = other_session
        self.patched_library.niTClk_SetAttributeViSession.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViSessionMatcher(other_session_number))

    def test_get_tclk_session_reference(self):
        session = nitclk.SessionReference(SESSION_NUM_FOR_TEST)
        self.patched_library.niTClk_GetAttributeViSession.side_effect = self.side_effects_helper.niTClk_GetAttributeViSession
        attribute_id = 3
        other_session_number = 43
        self.side_effects_helper['GetAttributeViSession']['value'] = other_session_number
        attr_session_reference = session.start_trigger_master_session
        assert type(attr_session_reference) is nitclk.SessionReference
        assert attr_session_reference._get_tclk_session_reference() == other_session_number
        self.patched_library.niTClk_GetAttributeViSession.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST), _matchers.ViStringMatcher(''), _matchers.ViAttrMatcher(attribute_id), _matchers.ViSessionPointerMatcher())
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/shared/system_test_utilities.py sha256=5d420065a6f1e03da93e44c1974b120ce79505c7fc63716a50416e13053e8444 bytes=3419 -->
## FILE: src/shared/system_test_utilities.py

- repository: `ni/nimi-python`
- source_path: `src/shared/system_test_utilities.py`
- sha256: `5d420065a6f1e03da93e44c1974b120ce79505c7fc63716a50416e13053e8444`
- bytes: 3419

````python
import os
import pathlib
import pytest
import re
import subprocess
import threading
import time


class GrpcServerProcess:
    def __init__(self, config_file_path):
        server_exe = self._get_grpc_server_exe()
        self._proc = subprocess.Popen([str(server_exe), config_file_path], stdout=subprocess.PIPE)

        # Read/parse output until we find the port number or the process exits; discard the rest.
        try:
            self.server_port = None
            while self.server_port is None and self._proc.poll() is None:
                line = self._proc.stdout.readline()
                match = re.search(rb"Server listening on port (\d+)", line)
                if match:
                    self.server_port = int(match.group(1))

            if self._proc.poll() is not None:
                raise RuntimeError(f"Server exited with return code {self._proc.returncode}")

            self._stdout_thread = threading.Thread(target=self._discard_output, args=(self._proc.stdout,), daemon=True)
            self._stdout_thread.start()
        except Exception:
            self._proc.kill()
            raise

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._proc.kill()

    def _get_grpc_server_exe(self):
        if os.name != "nt":
            pytest.skip("Only supported on Windows")
        import winreg
        try:
            reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
            read64key = winreg.KEY_READ | winreg.KEY_WOW64_64KEY
            with winreg.OpenKey(reg, r"SOFTWARE\National Instruments\Common\Installer", access=read64key) as key:
                shared_dir, _ = winreg.QueryValueEx(key, "NISHAREDDIR64")
        except OSError:
            pytest.skip("NI gRPC Device Server not installed")
        server_exe = pathlib.Path(shared_dir) / "NI gRPC Device Server" / "ni_grpc_device_server.exe"
        if not server_exe.exists():
            pytest.skip("NI gRPC Device Server not installed")
        return server_exe

    def _discard_output(self, stdout):
        while True:
            data = stdout.read(8196)
            if not data:
                return


def impl_test_multi_threading_lock_unlock(session):
    t1_lock_engaged = threading.Event()
    release_t1_lock = threading.Event()

    def lock_wait_unlock():
        session.lock()
        t1_lock_engaged.set()
        assert session.instrument_manufacturer != ''
        release_t1_lock.wait()
        session.unlock()

    def lock_unlock():
        session.lock()
        assert session.instrument_model != ''
        session.unlock()

    # test that lock, unlock functions work properly
    t1 = threading.Thread(target=lock_wait_unlock)
    t2 = threading.Thread(target=lock_unlock)

    t1.start()
    t2.start()

    t1_lock_engaged.wait()
    time.sleep(2.0)
    # t1 is blocked by the release event, t2 should be blocked by t1's lock
    assert t2.is_alive()
    release_t1_lock.set()
    t2.join()

    assert not t1.is_alive()
    assert not t2.is_alive()

def impl_test_multi_threading_ivi_synchronized_wrapper_releases_lock(ivi_method_to_call):
    # test that the 2nd thread doesn't hang
    t1 = threading.Thread(target=ivi_method_to_call)
    t2 = threading.Thread(target=ivi_method_to_call)

    t1.start()
    t1.join()
    assert not t1.is_alive()

    t2.start()
    t2.join()
    assert not t2.is_alive()
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/shared_protos/nidevice.proto sha256=9d146d9ae8a7d1b3f5af7dc305b511f0a6e9a1c89c4644a78657f356f2d5b6da bytes=622 -->
## FILE: src/shared_protos/nidevice.proto

- repository: `ni/nimi-python`
- source_path: `src/shared_protos/nidevice.proto`
- sha256: `9d146d9ae8a7d1b3f5af7dc305b511f0a6e9a1c89c4644a78657f356f2d5b6da`
- bytes: 622

````protobuf
syntax = "proto3";

option java_multiple_files = true;
option java_package = "com.ni.grpc.device";
option java_outer_classname = "NiDevice";
option csharp_namespace = "NationalInstruments.Grpc.Device";

package nidevice_grpc;

message NIComplexNumber {
  double real = 1;
  double imaginary = 2;
}

message NIComplexNumberF32 {
  float real = 1;
  float imaginary = 2;
}

message NIComplexI16 {
  sint32 real = 1;
  sint32 imaginary = 2;
}

message SmtSpectrumInfo {
  uint32 spectrum_type = 1;
  uint32 linear_db = 2;
  uint32 window = 3;
  sint32 window_size = 4;
  sint32 fft_size = 5;
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=src/shared_protos/README.md sha256=2c1f787629f580a2b88ec2d3a1fa07d163267efa095c2ab482206a7b77ba038d bytes=125 -->
## FILE: src/shared_protos/README.md

- repository: `ni/nimi-python`
- source_path: `src/shared_protos/README.md`
- sha256: `2c1f787629f580a2b88ec2d3a1fa07d163267efa095c2ab482206a7b77ba038d`
- bytes: 125

````markdown
# Updating

To update this folder, copy the .proto files from <https://github.com/ni/grpc-device/tree/main/source/protobuf>.
````

<!--NI_OSS_SOURCE repo=nimi-python path=tools/build_release.py sha256=7df33f9934eccd97d0387bc7db55855d44567945755b64ceed32f239d2052bdb bytes=5871 -->
## FILE: tools/build_release.py

- repository: `ni/nimi-python`
- source_path: `tools/build_release.py`
- sha256: `7df33f9934eccd97d0387bc7db55855d44567945755b64ceed32f239d2052bdb`
- bytes: 5871

````python
# !python

import argparse
from configure_logging import configure_logging
import logging
import pprint
from subprocess import check_call

pp = pprint.PrettyPrinter(indent=4, width=100)

default_python_cmd = ['python']


class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter):
    '''We want the description to use the raw formatting but have the parameters be formatted as before

    from stackoverflow:
    https://stackoverflow.com/questions/18462610/argumentparser-epilog-and-description-formatting-in-conjunction-with-argumentdef
    '''
    pass


def main():
    drivers_to_update = ['nidcpower', 'nidigital', 'nidmm', 'nifake', 'niswitch', 'nimodinst', 'nifgen', 'nirfsg', 'niscope', 'nise', 'nitclk']

    # Setup the required arguments for this script
    usage = """Release script
Prereqs
    * Be able to build locally
    * `pip install --upgrade twine tox` into whichever Python you use to build
Steps: see "Release Process" section of CONTRIBUTING.md
"""
    parser = argparse.ArgumentParser(description=usage, formatter_class=CustomFormatter)

    build_group = parser.add_argument_group("Build configuration")
    build_group.add_argument("--upload", action="store_true", default=False, help="Upload build distributions to PyPI")
    build_group.add_argument("--build", action="store_true", default=False, help="Clean and build")
    build_group.add_argument("--python-cmd", action="store", default=None, help=f"Command to use for invoking python. Default: {default_python_cmd}")
    build_group.add_argument("--drivers", action="store", default=None, help="Comma-separated list of drivers to update. Default: All Drivers")
    build_group.add_argument("--increment-major-version", action="store_true", default=False, help="Increment the major version")
    build_group.add_argument("--increment-minor-version", action="store_true", default=False, help="Increment the minor version")
    build_group.add_argument("--increment-patch-version", action="store_true", default=False, help="Increment the patch version")
    build_group.add_argument("--update-for-release", action="store_true", default=False, help="This is a release build, so only remove '.devN'. build, then update with .dev0")

    verbosity_group = parser.add_argument_group("Verbosity, Logging & Debugging")
    verbosity_group.add_argument("-v", "--verbose", action="count", default=0, help="Verbose output")
    verbosity_group.add_argument("--preview", action="store_true", default=False, help="Show what would happen when running with given parameters")
    verbosity_group.add_argument("--log-file", action="store", default=None, help="Send logging to listed file instead of stdout")
    args = parser.parse_args()

    # Validate that only one of the version-related flags is provided
    version_flags = [
        args.increment_major_version,
        args.increment_minor_version,
        args.increment_patch_version,
        args.update_for_release,
    ]
    if sum(version_flags) > 1:
        raise ValueError("Only one of --increment-major-version, --increment-minor-version, --increment-patch-version or --update-for-release can be provided.")

    if args.verbose > 1:
        configure_logging(logging.DEBUG, args.log_file)
    elif args.verbose == 1:
        configure_logging(logging.INFO, args.log_file)
    else:
        configure_logging(logging.WARNING, args.log_file)

    logging.info(pp.pformat(args))

    python_cmd = [args.python_cmd] if args.python_cmd is not None else default_python_cmd

    tox_cmd = python_cmd + ['-m', 'tox']
    twine_cmd = python_cmd + ['-m', 'twine']

    passthrough_params = ['-v' for i in range(args.verbose)]
    if args.preview:
        passthrough_params.append('--preview')
    if args.log_file:
        passthrough_params.append('--log-file').append(args.log_file)
    if args.update_for_release:
        passthrough_params.append('--release')
    if args.increment_patch_version:
        passthrough_params.append('--update-type=patch')
    if args.increment_minor_version:
        passthrough_params.append('--update-type=minor')
    if args.increment_major_version:
        passthrough_params.append('--update-type=major')

    if args.drivers:
        provided_drivers = args.drivers.split(",")
        invalid_drivers = [driver for driver in provided_drivers if driver not in drivers_to_update]

        if invalid_drivers:
            raise ValueError(f"The following drivers are invalid: {', '.join(invalid_drivers)}. Valid drivers are: {','.join(drivers_to_update)}")
        drivers_to_update = provided_drivers

    if any([args.increment_major_version, args.increment_minor_version, args.increment_patch_version, args.update_for_release]):
        logging.info('Updating versions')

        for d in drivers_to_update:
            logging.info(pp.pformat(python_cmd + ['tools/updateReleaseInfo.py', '--src-folder', f'src/{d}',] + passthrough_params))
            check_call(python_cmd + ['tools/updateReleaseInfo.py', '--src-folder', f'src/{d}', ] + passthrough_params)

    if args.build:
        logging.info('Clean and build')
        logging.info(pp.pformat(tox_cmd + ['-e', 'clean']))
        logging.info(pp.pformat(tox_cmd))
        logging.info(pp.pformat(tox_cmd + ['-e', 'pkg']))
        if not args.preview:
            check_call(tox_cmd + ['-e', 'clean'])
            check_call(tox_cmd)

    if args.upload:
        logging.info('Uploading to PyPI')
        complete_twine_cmd = twine_cmd + ['upload']
        drivers_to_upload = [driver for driver in drivers_to_update if driver != 'nifake']
        for d in drivers_to_upload:
            complete_twine_cmd += [f'generated/{d}/dist/*']

        logging.info(pp.pformat(complete_twine_cmd))
        if not args.preview:
            check_call(complete_twine_cmd)


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=tools/configure_logging.py sha256=c0e3169a6e0bb01eee2aa8dd4d2ae03b8300054fd874cee260536e9d89fe3657 bytes=532 -->
## FILE: tools/configure_logging.py

- repository: `ni/nimi-python`
- source_path: `tools/configure_logging.py`
- sha256: `c0e3169a6e0bb01eee2aa8dd4d2ae03b8300054fd874cee260536e9d89fe3657`
- bytes: 532

````python
import logging
import sys


def configure_logging(lvl=logging.WARNING, logfile=None):
    root = logging.getLogger()
    root.setLevel(lvl)

    formatter = logging.Formatter("[%(asctime)s] [%(levelname)8s] --- %(message)s (%(filename)s:%(funcName)s:%(lineno)s)", "%Y-%m-%d %H:%M:%S")
    if logfile is None:
        handler = logging.StreamHandler(sys.stdout)
    else:
        print("Logging to file %s" % logfile)
        handler = logging.FileHandler(logfile)
    handler.setFormatter(formatter)
    root.addHandler(handler)
````

<!--NI_OSS_SOURCE repo=nimi-python path=tools/coverage_system_tests.rc sha256=faec122adba5d85542803fdef15a3c092dd25cad0198b1f657ed0c7861f00eac bytes=963 -->
## FILE: tools/coverage_system_tests.rc

- repository: `ni/nimi-python`
- source_path: `tools/coverage_system_tests.rc`
- sha256: `faec122adba5d85542803fdef15a3c092dd25cad0198b1f657ed0c7861f00eac`
- bytes: 963

````text
; This file controls what modules are examined for code coverage in our system tests.

[run]
omit =
    ; Common code, so covered by nifake unit tests.
    ; Some modules don't even exercise all of _attributes.py and _converters.py, making parts unreachable in system tests.
    */__init__.py
    */_attributes.py
    */_converters.py
    */errors.py
    */_library_singleton.py
    */_visatype.py

    ; Although the enum names and values vary between modules, all enums are mostly the same. nifake unit tests cover the various kinds that we use.
    */enums.py

    ; Most of the lines in *_pb2.py are only used for the pure-Python implementation of protobuf, and the default implementation nowadays is the upb C implementation.
    */*pb2.py

    ; *_pb2_grpc.py defines a stub, a servicer, and an "experimental API", and we only use the stub.
    ; If our system test coverage of the stub_interpreter is okay, we should be in good shape.
    */*_pb2_grpc.py
````

<!--NI_OSS_SOURCE repo=nimi-python path=tools/coverage_unit_tests.rc sha256=1493862b52da9e1c2676bfc748f435987d0081512f8e32e04b0f0a96e59881d7 bytes=2285 -->
## FILE: tools/coverage_unit_tests.rc

- repository: `ni/nimi-python`
- source_path: `tools/coverage_unit_tests.rc`
- sha256: `1493862b52da9e1c2676bfc748f435987d0081512f8e32e04b0f0a96e59881d7`
- bytes: 2285

````text
; This file controls what modules are examined for code coverage in our unit tests.
; See https://coverage.readthedocs.io/en/latest/source.html#source

[run]
; Fileset is restricted to include matches, first
; Unfortunately, all of these patterns will be ignored, because we pass --source, when running the unit tests.
include =
    ; nifake is tested entirely by unit tests. Its sole purpose is to test code that is common to all APIs
    */nifake/*
    ; System testing is preferred, but some published modules have code that's easier to test with a unit test
    */nidcpower/lcr_load_compensation_spot.py
    */nidcpower/lcr_measurement.py
    */nidigital/session.py
    */nimodinst/session.py
    */niscope/waveform_info.py
    */nitclk/session.py
    build/*
; Any include matches that match omit patterns are removed
omit =
    ; Covered by system tests
    */_library*

    ; Everthing below here needs to be explicitly excluded because "include" is ignored.

    ; All private modules are covered by nifake unit tests, except for interpreter modules, which are covered by system tests.
    */nidcpower/_*
    */nidigital/_*
    */nimodinst/_*
    */niscope/_*
    */nitclk/_*

    ; Common code, so covered by nifake unit tests
    */nidcpower/enums.py
    */nidcpower/errors.py
    */nidigital/enums.py
    */nidigital/errors.py
    */nimodinst/errors.py
    */niscope/enums.py
    */niscope/errors.py
    */nitclk/errors.py

    ; See the include section; these modules don't have unit tests covering session.py
    */nidcpower/session.py
    */niscope/session.py

    ; Covered by System tests
    */nidigital/history_ram_cycle_information.py
    */niscope/measurement_stats.py

    ; Most of the lines in *_pb2.py are only used for the pure-Python implementation of protobuf, and the default implementation nowadays is the upb C implementation.
    */*pb2.py

    ; *_pb2_grpc.py defines a stub, a servicer, and an "experimental API", and we only use the stub.
    ; If our system test coverage of the stub_interpreter is okay, we should be in good shape.
    */*_pb2_grpc.py

    ; grpc_session_options.py is tested by system tests and nifake unit tests
    */nidcpower/grpc_session_options.py
    */nidigital/grpc_session_options.py
    */niscope/grpc_session_options.py
````

<!--NI_OSS_SOURCE repo=nimi-python path=tools/ensure_codegen_up_to_date.py sha256=a3e79e873544d4d24b2a493de3583207de96f5757a7578dd305a982c17a9c667 bytes=1694 -->
## FILE: tools/ensure_codegen_up_to_date.py

- repository: `ni/nimi-python`
- source_path: `tools/ensure_codegen_up_to_date.py`
- sha256: `a3e79e873544d4d24b2a493de3583207de96f5757a7578dd305a982c17a9c667`
- bytes: 1694

````python
"""
ensure_codegen_up_to_date
-------------------------
Ensure changes to code generation are committed to repository
"""

import os
import subprocess
import sys


def _configure_git_credentials():

    """Configures git user name and email with dummy name and email"""

    if os.system('git config user.email "dummy@ni.com"') != 0:
        sys.exit("Error: Unable to configure \"user email\" using git")

    if os.system('git config user.name "dummy"') != 0:
        sys.exit("Error: Unable to configure \"user name\" using git")


def _clean_codegen_files():

    """Before code generation clean the existing codegen files"""

    if os.system("tox -e clean") != 0:
        sys.exit("Error: Unable to clean the repo using \"tox -e clean\"")


def _create_codegen_files():

    """create codegen files"""

    if os.system("tox -e codegen") != 0:
        sys.exit("Error: Unable to generate code using \"tox -e codegen\"")


def _check_no_dirty_files():

    '''Checks if there are any modified files, outputting a warning if only line endings are different'''

    if int(subprocess.check_output("git status -s -uno | wc -l", shell=True).decode().strip("b'\\n'")) != 0:
        list_of_changed_files = subprocess.check_output("git status -s -uno", shell=True).decode()
        sys.exit(f"The following code generated files do not match what is commited to Git. Run codegen and include the generated files in the PR.\n{list_of_changed_files} \n")
    print("All changes to code generation are committed to repository")


if __name__ == "__main__":
    """
    Main
    """
    _configure_git_credentials()

    _clean_codegen_files()
    _create_codegen_files()

    _check_no_dirty_files()
````

<!--NI_OSS_SOURCE repo=nimi-python path=tools/install_local_wheel.py sha256=0bd481d58b217525248ed6380e8ccfd9f7391ea89bf697de784a724c17bcb558 bytes=2152 -->
## FILE: tools/install_local_wheel.py

- repository: `ni/nimi-python`
- source_path: `tools/install_local_wheel.py`
- sha256: `0bd481d58b217525248ed6380e8ccfd9f7391ea89bf697de784a724c17bcb558`
- bytes: 2152

````python
# !python

import argparse
from configure_logging import configure_logging
import logging
import os
import pprint
from subprocess import call
import sys

pp = pprint.PrettyPrinter(indent=4, width=100)


def main():
    # Setup the required arguments for this script
    usage = """
Install the wheel found in generated/<driver>/dist
"""
    parser = argparse.ArgumentParser(description=usage)
    file_group = parser.add_argument_group("Input and Output files")
    file_group.add_argument("--driver", action="store", default=None, required=True, help="Source file")
    file_group.add_argument("--start-path", action="store", default=None, help="Prepend to path to search")

    verbosity_group = parser.add_argument_group("Verbosity, Logging & Debugging")
    verbosity_group.add_argument("-v", "--verbose", action="count", dest="verbose", default=0, help="Verbose output")
    verbosity_group.add_argument("--test", action="store_true", dest="test", default=False, help="Run doctests and quit")
    verbosity_group.add_argument("--log-file", action="store", dest="logfile", default=None, help="Send logging to listed file instead of stdout")
    args = parser.parse_args()

    if args.verbose > 1:
        configure_logging(logging.DEBUG, args.logfile)
    elif args.verbose == 1:
        configure_logging(logging.INFO, args.logfile)
    else:
        configure_logging(logging.WARNING, args.logfile)

    logging.info(pp.pformat(args))

    rel_path = os.path.join('generated', args.driver, 'dist')
    if args.start_path is not None:
        rel_path = os.path.join(args.start_path, rel_path)
    wheel = None
    for file in os.listdir(rel_path):
        if file.endswith(".whl"):
            if wheel is not None:
                logging.error(f'More than one wheel has been found: {wheel} and {os.path.join(rel_path, file)}')
                sys.exit(1)
            wheel = os.path.join(rel_path, file)

    if wheel is None:
        logging.error('No wheel found. Has the build run successfully?')
        sys.exit(2)

    # Install/upgrade the wheel
    call(['pip', 'install', '--upgrade', wheel])


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=tools/simple_mako.py sha256=c99a70f2355acf79b79efab6dc3527924f9cf0c2a1960af2093b6f5a657cb782 bytes=3460 -->
## FILE: tools/simple_mako.py

- repository: `ni/nimi-python`
- source_path: `tools/simple_mako.py`
- sha256: `c99a70f2355acf79b79efab6dc3527924f9cf0c2a1960af2093b6f5a657cb782`
- bytes: 3460

````python
# !python

import argparse
from configure_logging import configure_logging
import logging
from mako.exceptions import RichTraceback
from mako.lookup import TemplateLookup
from mako.template import Template
import pprint
import sys


pp = pprint.PrettyPrinter(indent=4, width=100)


def generate_template(template_name, template_params, dest_file):
    try:
        template_params['encoding_tag'] = '# -*- coding: utf-8 -*-'
        lookup = TemplateLookup(directories=['build/templates'])
        template = Template(filename=template_name, lookup=lookup)
        rendered_template = template.render(template_parameters=template_params)

    except Exception:
        # Because mako expands into python, we catch all errors, not just MakoException.
        # Ideally, we'd use text_error_template, but it sucks.  html_error_template,
        # however, is useful.  Unfortunately emitting html isn't acceptable.  So we
        # re-implement using mako.exceptions.RichTraceback here.
        tback = RichTraceback(traceback=None)
        line = tback.lineno
        lines = tback.source.split('\n')

        # The underlying error.
        logging.error("\n{}: {}\n".format(str(tback.error.__class__.__name__), str(tback.error)))
        logging.error("Offending Template: %s\n" % template_name)

        # Show a source listing of the template, with offending line marked.
        for index in range(max(0, line - 4), min(len(lines), line + 5)):
            if index + 1 == line:
                logging.error(">> %#08d: %s" % (index + 1, lines[index]))
            else:
                logging.error("   %08d: %s" % (index + 1, lines[index]))

        logging.error("\nTraceback (most recent call last):")
        for (filename, lineno, function, line) in tback.reverse_traceback:
            logging.error("   File %s, line %d, in %s\n     %s" % (filename, lineno, function, line))

        logging.error("\n")
        sys.exit(1)

    logging.debug(rendered_template)
    with open(dest_file, 'wb') as file_handle_public:
        file_handle_public.write(bytes(rendered_template, "UTF-8"))


def main():
    # Setup the required arguments for this script
    usage = """
Run generate_template on the requested mako template
"""
    parser = argparse.ArgumentParser(description=usage)
    file_group = parser.add_argument_group("Input and Output files")
    file_group.add_argument("--output-file", action="store", required=True, help="Output file")
    file_group.add_argument("--template", action="store", required=True, help="Template file")

    verbosity_group = parser.add_argument_group("Verbosity, Logging & Debugging")
    verbosity_group.add_argument("-v", "--verbose", action="count", dest="verbose", default=0, help="Verbose output")
    verbosity_group.add_argument("--test", action="store_true", dest="test", default=False, help="Run doctests and quit")
    verbosity_group.add_argument("--log-file", action="store", dest="logfile", default=None, help="Send logging to listed file instead of stdout")
    args = parser.parse_args()

    if args.verbose > 1:
        configure_logging(logging.DEBUG, args.logfile)
    elif args.verbose == 1:
        configure_logging(logging.INFO, args.logfile)
    else:
        configure_logging(logging.WARNING, args.logfile)

    logging.info(pp.pformat(args))

    template_params = {}
    generate_template(args.template, template_params, args.output_file)


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=tools/update_version_file.py sha256=66bc138ea7041efc991f0895fea3009f93ef168760377031aa16c5a7f2b81a18 bytes=1826 -->
## FILE: tools/update_version_file.py

- repository: `ni/nimi-python`
- source_path: `tools/update_version_file.py`
- sha256: `66bc138ea7041efc991f0895fea3009f93ef168760377031aa16c5a7f2b81a18`
- bytes: 1826

````python
# !python

import argparse
from configure_logging import configure_logging
import logging
import pprint

from packaging.version import Version

pp = pprint.PrettyPrinter(indent=4, width=100)


def main():
    # Setup the required arguments for this script
    usage = """
Find the max version in any referenced VERSION file and then write that max version to the output VERSION file
"""
    parser = argparse.ArgumentParser(description=usage)
    file_group = parser.add_argument_group("Input and Output files")
    file_group.add_argument("--output-file", action="store", required=True, help="Output file")
    file_group.add_argument("--input-file", action="append", required=True, help="Input file, multiple allowed")

    verbosity_group = parser.add_argument_group("Verbosity, Logging & Debugging")
    verbosity_group.add_argument("-v", "--verbose", action="count", dest="verbose", default=0, help="Verbose output")
    verbosity_group.add_argument("--test", action="store_true", dest="test", default=False, help="Run doctests and quit")
    verbosity_group.add_argument("--log-file", action="store", dest="logfile", default=None, help="Send logging to listed file instead of stdout")
    args = parser.parse_args()

    if args.verbose > 1:
        configure_logging(logging.DEBUG, args.logfile)
    elif args.verbose == 1:
        configure_logging(logging.INFO, args.logfile)
    else:
        configure_logging(logging.WARNING, args.logfile)

    logging.info(pp.pformat(args))

    max_version = Version('0.0.0.dev0')
    for version_file in args.input_file:
        with open(version_file) as f:
            v = Version(f.read().strip())

        if v > max_version:
            max_version = v

    with open(args.output_file, 'w') as f:
        f.write(str(max_version))


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=tools/updateReleaseInfo.py sha256=5e070e418c9e225a9eda998b64771b3318ab17d27c4b576a888e7c37aa0bab7c bytes=3741 -->
## FILE: tools/updateReleaseInfo.py

- repository: `ni/nimi-python`
- source_path: `tools/updateReleaseInfo.py`
- sha256: `5e070e418c9e225a9eda998b64771b3318ab17d27c4b576a888e7c37aa0bab7c`
- bytes: 3741

````python
import argparse
from configure_logging import configure_logging
import logging
import os
import pprint
import re

pp = pprint.PrettyPrinter(indent=4, width=100)


# Increment version based on bump type ('major', 'minor', 'patch').
def bump_version(version, bump_type):
    major, minor, patch = map(int, version.split('.'))

    if bump_type == 'patch':
        patch += 1
    elif bump_type == 'minor':
        minor += 1
        patch = 0
    elif bump_type == 'major':
        major += 1
        minor = 0
        patch = 0

    return f"{major}.{minor}.{patch}"


def main():
    usage = """
Update version in files. Example: X.Y.Z.devN to X.Y.Z
"""
    parser = argparse.ArgumentParser(description=usage)
    file_group = parser.add_argument_group("Input and Output files")
    file_group.add_argument("--src-folder", action="store", required=True, help="Source folder")
    file_group.add_argument("--release", action="store_true", default=False, help="This is a release build, so only remove '.devN'. Error if not there")
    file_group.add_argument("--update-type", action="store", default=None, choices=["major", "minor", "patch"], help="Specify the type of update: major, minor or patch. ")

    verbosity_group = parser.add_argument_group("Verbosity, Logging & Debugging")
    verbosity_group.add_argument("-v", "--verbose", action="count", default=0, help="Verbose output")
    verbosity_group.add_argument("--preview", action="store_true", default=False, help="Show what would happen when running with given parameters")
    verbosity_group.add_argument("--log-file", action="store", default=None, help="Send logging to listed file instead of stdout")
    args = parser.parse_args()

    if args.verbose > 1:
        configure_logging(logging.DEBUG, args.log_file)
    elif args.verbose == 1:
        configure_logging(logging.INFO, args.log_file)
    else:
        configure_logging(logging.WARNING, args.log_file)

    logging.info(pp.pformat(args))
    metadata_file = os.path.join(args.src_folder, "metadata", "config_addon.py")
    with open(metadata_file) as content_file:
        contents = content_file.read()

    module_version_re = re.compile(r"'module_version': '(\d+\.\d+\.\d+)(?:\.dev(\d+))?'")
    m = module_version_re.search(contents)
    logging.debug(f"Version regex match: {m}")

    if m:
        base_version = m.group(1)
        dev_number = int(m.group(2)) if m.group(2) else None

        if dev_number is not None:
            logging.info("Dev version found")
            current_version = f"{base_version}.dev{dev_number}"
        else:
            logging.info("Release version found")
            current_version = base_version

        if args.release:
            if dev_number is not None:
                new_version = base_version
            else:
                logging.error("Error: Attempting to release an already released version.")
                return
        else:
            bumped_version = bump_version(base_version, args.update_type)
            new_version = f"{bumped_version}.dev0"

        logging.info(f"Updating {current_version} to {new_version}")
        contents = module_version_re.sub(f"'module_version': '{new_version}'", contents)

    if not args.preview:
        with open(metadata_file, 'w') as content_file:
            content_file.write(contents)

    if args.release and "nifake" not in args.src_folder:
        latest_release_file = os.path.join(args.src_folder, "LATEST_RELEASE")
        logging.info(f'Updating version in {latest_release_file} to {new_version}.')
        if not args.preview:
            with open(latest_release_file, 'w') as content_file:
                content_file.write(f'{new_version}\n')


if __name__ == '__main__':
    main()
````

<!--NI_OSS_SOURCE repo=nimi-python path=tox-travis.ini sha256=8da668bd5cfa4581db62262471e0d2158ab682b87736add74e638ec163cb39c1 bytes=10266 -->
## FILE: tox-travis.ini

- repository: `ni/nimi-python`
- source_path: `tox-travis.ini`
- sha256: `8da668bd5cfa4581db62262471e0d2158ab682b87736add74e638ec163cb39c1`
- bytes: 10266

````ini
# Tox (http://tox.testrun.org/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox" from this directory.
[tox]
# tox.ini and tox-travis.ini are copies of the same content with different envlist commented out
# tox-travis.ini will have pyXX-clean and all pyXX-installers in the default envlist, while the developer tox.ini
# does not have clean and only has one pyXX-installers
# Historically we've used the latest Python for environments that we only list one Python for. For now, we're using Python 3.12
# to avoid updating our pb2 files, which could possibly cause incompatibilities with other NI Python packages.
# When other NI Python packages bump the version that they use for generating pb2 files, we can bump this Python version to match.
# We may also bump it sooner, if we agree with team members who own other NI Python packages that it's okay to do so.
# At the latest, we'll bump it when we drop support for Python 3.12.
# Uncomment this line for tox.ini
# envlist = py312-build_test,py312-codegen,py312-installers,py{310,311,312,313,314}-test,py312-flake8,py312-docs,py312-pkg
# Uncomment this line for tox-travis.ini
envlist = py312-clean,py312-build_test,py312-codegen,py{310,311,312,313,314}-installers,py{310,311,312,313,314}-test,py312-flake8,py312-docs,py312-pkg
skip_missing_interpreters=True
ignore_basepython_conflict=True
skipsdist = true
toxworkdir = .tox/{env:BITNESS:64}

[testenv]
description =
    test: Run tests
    build_test: Test the build scripts
    clean: Clean code generated files
    codegen: Run code generation step
    installers: Build the installers (wheels and sdists)
    flake8: Run static analysis
    docs: Generate documentation
    pkg: Verify the package

changedir =
    build_test: .
    test: .
    codegen: .
    installers: .
    clean: .
    docs: docs
    flake8: .
    pkg: .

commands =
    build_test: python --version
    build_test: python -c "import platform; print(platform.architecture())"
    build_test: python -m pip install --disable-pip-version-check --upgrade pip
    build_test: python -m pip list
    # doctest validation of code docstrings
    build_test: coverage run --rcfile=tools/coverage_unit_tests.rc --source build.helper -m pytest --pyargs build.helper
    # actual unit tests
    build_test: coverage run --append --rcfile=tools/coverage_unit_tests.rc --source build.helper -m pytest build/unit_tests {posargs} -s
    # Display the report on console
    build_test: coverage report
    # Create the report to upload
    build_test: coverage xml -o codegen.xml
    # Save the report
    build_test: coverage html --directory=generated/htmlcov/unit_tests/codegen
    build_test: flake8 --config=./tox.ini --per-file-ignores=build/unit_tests/*.py:F403,F405 build/
    test: python --version
    test: python -c "import platform; print(platform.architecture())"
    test: python -m pip install --disable-pip-version-check --upgrade pip
    test: python tools/install_local_wheel.py --driver nitclk
    test: coverage run --rcfile=tools/coverage_unit_tests.rc --source nifake -m pytest generated/nifake/nifake {posargs} -s
    test: coverage report
    test: coverage xml -o nifakeunittest.xml
    test: coverage html --directory=generated/htmlcov/unit_tests/nifake
    test: coverage run --rcfile=tools/coverage_unit_tests.rc --source nidcpower -m pytest generated/nidcpower/nidcpower {posargs} -s
    test: coverage report
    test: coverage xml -o nidcpowerunittest.xml
    test: coverage html --directory=generated/htmlcov/unit_tests/nidcpower
    test: coverage run --rcfile=tools/coverage_unit_tests.rc --source nidigital -m pytest generated/nidigital/nidigital {posargs} -s
    test: coverage report
    test: coverage xml -o nidigitalunittest.xml
    test: coverage html --directory=generated/htmlcov/unit_tests/nidigital
    test: coverage run --rcfile=tools/coverage_unit_tests.rc --source nimodinst -m pytest generated/nimodinst/nimodinst {posargs} -s
    test: coverage report
    test: coverage xml -o nimodinstunittest.xml
    test: coverage html --directory=generated/htmlcov/unit_tests/nimodinst
    test: coverage run --rcfile=tools/coverage_unit_tests.rc --source niscope -m pytest generated/niscope/niscope {posargs} -s
    test: coverage report
    test: coverage xml -o niscopeunittest.xml
    test: coverage html --directory=generated/htmlcov/unit_tests/niscope
    test: coverage run --rcfile=tools/coverage_unit_tests.rc --source nitclk -m pytest generated/nitclk/nitclk {posargs} -s
    test: coverage report
    test: coverage xml -o nitclkunittest.xml
    test: coverage html --directory=generated/htmlcov/unit_tests/nitclk
    clean: python --version
    clean: python -c "import platform; print(platform.architecture())"
    clean: make clean {posargs}
    codegen: python --version
    codegen: python -c "import platform; print(platform.architecture())"
    codegen: python -m pip install --disable-pip-version-check --upgrade pip
    codegen: make {posargs}
    installers: python --version
    installers: python -c "import platform; print(platform.architecture())"
    installers: python -m pip install --disable-pip-version-check --upgrade pip
    installers: make installers {posargs}
    flake8: python --version
    flake8: python -c "import platform; print(platform.architecture())"
    flake8: python -m pip install --disable-pip-version-check --upgrade pip
    flake8: flake8 --config=./tox.ini generated/
    flake8: flake8 --config=./tox.ini tools/
    flake8: flake8 --config=./tox.ini src/nidcpower/system_tests/ src/nidcpower/examples/
    flake8: flake8 --config=./tox.ini src/nidigital/system_tests/ src/nidigital/examples/
    flake8: flake8 --config=./tox.ini src/nidmm/system_tests/ src/nidmm/examples/
    flake8: flake8 --config=./tox.ini src/nifgen/system_tests/ src/nifgen/examples/
    flake8: flake8 --config=./tox.ini src/nimodinst/system_tests/ src/nimodinst/examples/
    flake8: flake8 --config=./tox.ini src/nirfsg/system_tests/ src/nirfsg/examples/
    flake8: flake8 --config=./tox.ini src/niscope/system_tests/ src/niscope/examples/
    flake8: flake8 --config=./tox.ini src/nise/system_tests/ src/nise/examples/
    flake8: flake8 --config=./tox.ini src/niswitch/system_tests/ src/niswitch/examples/
    flake8: flake8 --config=./tox.ini src/nitclk/system_tests/ src/nitclk/examples/
    docs: python --version
    docs: python -c "import platform; print(platform.architecture())"
    docs: sphinx-build -b html -d {envtmpdir}/doctrees ./nidcpower ../generated/docs/nidcpower/html {posargs}
    docs: sphinx-build -b html -d {envtmpdir}/doctrees ./nidigital ../generated/docs/nidigital/html {posargs}
    docs: sphinx-build -b html -d {envtmpdir}/doctrees ./nidmm ../generated/docs/nidmm/html {posargs}
    docs: sphinx-build -b html -d {envtmpdir}/doctrees ./nifgen ../generated/docs/nifgen/html {posargs}
    docs: sphinx-build -b html -d {envtmpdir}/doctrees ./nimodinst ../generated/docs/nimodinst/html {posargs}
    docs: sphinx-build -b html -d {envtmpdir}/doctrees ./nirfsg ../generated/docs/nirfsg/html {posargs}
    docs: sphinx-build -b html -d {envtmpdir}/doctrees ./niscope ../generated/docs/niscope/html {posargs}
    docs: sphinx-build -b html -d {envtmpdir}/doctrees ./nise ../generated/docs/nise/html {posargs}
    docs: sphinx-build -b html -d {envtmpdir}/doctrees ./niswitch ../generated/docs/niswitch/html {posargs}
    docs: sphinx-build -b html -d {envtmpdir}/doctrees ./nitclk ../generated/docs/nitclk/html {posargs}
    pkg: python --version
    pkg: python -c "import platform; print(platform.architecture())"
    pkg: python -m twine --version
    pkg: python -m twine check generated/nifake/dist/*
    pkg: python -m twine check generated/nidcpower/dist/*
    pkg: python -m twine check generated/nidigital/dist/*
    pkg: python -m twine check generated/nidmm/dist/*
    pkg: python -m twine check generated/nifgen/dist/*
    pkg: python -m twine check generated/nirfsg/dist/*
    pkg: python -m twine check generated/niscope/dist/*
    pkg: python -m twine check generated/nise/dist/*
    pkg: python -m twine check generated/niswitch/dist/*
    # pkg: check-manifest --ignore tox.ini,tests*,.github,.github/*,CONTRIBUTING.rst,docs,docs/*

deps =
    test: pytest
    test: pytest-timeout
    test: coverage
    test: mako
    test: numpy
    test: hightime
    test: grpcio == 1.75.1  # Compatible with Python 3.14; should be backwards compatible with grpcio-tools 1.59.0
    test: protobuf == 5.27.2  # Compatible with Python 3.14; should be backwards compatible with grpcio-tools 1.59.0
    test: ni.grpcdevice.v1.proto >= 1.0.0  # Provides session_pb2 package at runtime since we no longer generate it per-driver
    build_test: pytest
    build_test: coverage
    build_test: mako
    build_test: hacking
    build_test: pep8-naming
    codegen: mako
    codegen: packaging
    codegen: setuptools < 82 # grpcio-tools 1.59.0 needs pkg_resources which was removed in setuptools v82
    codegen: grpcio-tools == 1.59.0 # First version to support Python 3.12
    installers: build
    flake8: hacking
    flake8: pep8-naming
    docs: sphinx
    docs: sphinx-rtd-theme
    pkg: check-manifest
    pkg: docutils
    pkg: pygments
    pkg: twine

depends =
    codegen: py312-clean
    installers: py312-codegen
    flake8: py312-codegen
    docs: py312-codegen
    test: py312-installers
    pkg: py312-installers

allowlist_externals =
    build_test: mv
    test: mv
    codegen: make
    installers: make
    clean: make

[flake8]
show_source = true
# We recommend setting your editor's visual guide to 79 but allow overflow to
# 160 for readability in certain cases due to generated code
# max_line_length = 160
exclude = build,docs,.tox,__pycache__,processed_metadata,.eggs,*_pb2*.py,third_party
# H903: Windows style line endings not allowed in code
# E501: Line length
# W391: Blank line at end of file
ignore = H903,E501,W391

[pytest]
addopts = --verbose --doctest-modules --ignore=setup.py
norecursedirs = system_tests examples .* build dist CVS _darcs {arch} *.egg venv
junit_suite_name = nimi-python
python_files = *.py
junit_family = xunit1
````

<!--NI_OSS_SOURCE repo=nimi-python path=tox.ini sha256=d1b938a79918cab787c2bd3457bf2c74caa59eadbacbc852129559a7503093a8 bytes=10266 -->
## FILE: tox.ini

- repository: `ni/nimi-python`
- source_path: `tox.ini`
- sha256: `d1b938a79918cab787c2bd3457bf2c74caa59eadbacbc852129559a7503093a8`
- bytes: 10266

````ini
# Tox (http://tox.testrun.org/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox" from this directory.
[tox]
# tox.ini and tox-travis.ini are copies of the same content with different envlist commented out
# tox-travis.ini will have pyXX-clean and all pyXX-installers in the default envlist, while the developer tox.ini
# does not have clean and only has one pyXX-installers
# Historically we've used the latest Python for environments that we only list one Python for. For now, we're using Python 3.12
# to avoid updating our pb2 files, which could possibly cause incompatibilities with other NI Python packages.
# When other NI Python packages bump the version that they use for generating pb2 files, we can bump this Python version to match.
# We may also bump it sooner, if we agree with team members who own other NI Python packages that it's okay to do so.
# At the latest, we'll bump it when we drop support for Python 3.12.
# Uncomment this line for tox.ini
envlist = py312-build_test,py312-codegen,py312-installers,py{310,311,312,313,314}-test,py312-flake8,py312-docs,py312-pkg
# Uncomment this line for tox-travis.ini
# envlist = py312-clean,py312-build_test,py312-codegen,py{310,311,312,313,314}-installers,py{310,311,312,313,314}-test,py312-flake8,py312-docs,py312-pkg
skip_missing_interpreters=True
ignore_basepython_conflict=True
skipsdist = true
toxworkdir = .tox/{env:BITNESS:64}

[testenv]
description =
    test: Run tests
    build_test: Test the build scripts
    clean: Clean code generated files
    codegen: Run code generation step
    installers: Build the installers (wheels and sdists)
    flake8: Run static analysis
    docs: Generate documentation
    pkg: Verify the package

changedir =
    build_test: .
    test: .
    codegen: .
    installers: .
    clean: .
    docs: docs
    flake8: .
    pkg: .

commands =
    build_test: python --version
    build_test: python -c "import platform; print(platform.architecture())"
    build_test: python -m pip install --disable-pip-version-check --upgrade pip
    build_test: python -m pip list
    # doctest validation of code docstrings
    build_test: coverage run --rcfile=tools/coverage_unit_tests.rc --source build.helper -m pytest --pyargs build.helper
    # actual unit tests
    build_test: coverage run --append --rcfile=tools/coverage_unit_tests.rc --source build.helper -m pytest build/unit_tests {posargs} -s
    # Display the report on console
    build_test: coverage report
    # Create the report to upload
    build_test: coverage xml -o codegen.xml
    # Save the report
    build_test: coverage html --directory=generated/htmlcov/unit_tests/codegen
    build_test: flake8 --config=./tox.ini --per-file-ignores=build/unit_tests/*.py:F403,F405 build/
    test: python --version
    test: python -c "import platform; print(platform.architecture())"
    test: python -m pip install --disable-pip-version-check --upgrade pip
    test: python tools/install_local_wheel.py --driver nitclk
    test: coverage run --rcfile=tools/coverage_unit_tests.rc --source nifake -m pytest generated/nifake/nifake {posargs} -s
    test: coverage report
    test: coverage xml -o nifakeunittest.xml
    test: coverage html --directory=generated/htmlcov/unit_tests/nifake
    test: coverage run --rcfile=tools/coverage_unit_tests.rc --source nidcpower -m pytest generated/nidcpower/nidcpower {posargs} -s
    test: coverage report
    test: coverage xml -o nidcpowerunittest.xml
    test: coverage html --directory=generated/htmlcov/unit_tests/nidcpower
    test: coverage run --rcfile=tools/coverage_unit_tests.rc --source nidigital -m pytest generated/nidigital/nidigital {posargs} -s
    test: coverage report
    test: coverage xml -o nidigitalunittest.xml
    test: coverage html --directory=generated/htmlcov/unit_tests/nidigital
    test: coverage run --rcfile=tools/coverage_unit_tests.rc --source nimodinst -m pytest generated/nimodinst/nimodinst {posargs} -s
    test: coverage report
    test: coverage xml -o nimodinstunittest.xml
    test: coverage html --directory=generated/htmlcov/unit_tests/nimodinst
    test: coverage run --rcfile=tools/coverage_unit_tests.rc --source niscope -m pytest generated/niscope/niscope {posargs} -s
    test: coverage report
    test: coverage xml -o niscopeunittest.xml
    test: coverage html --directory=generated/htmlcov/unit_tests/niscope
    test: coverage run --rcfile=tools/coverage_unit_tests.rc --source nitclk -m pytest generated/nitclk/nitclk {posargs} -s
    test: coverage report
    test: coverage xml -o nitclkunittest.xml
    test: coverage html --directory=generated/htmlcov/unit_tests/nitclk
    clean: python --version
    clean: python -c "import platform; print(platform.architecture())"
    clean: make clean {posargs}
    codegen: python --version
    codegen: python -c "import platform; print(platform.architecture())"
    codegen: python -m pip install --disable-pip-version-check --upgrade pip
    codegen: make {posargs}
    installers: python --version
    installers: python -c "import platform; print(platform.architecture())"
    installers: python -m pip install --disable-pip-version-check --upgrade pip
    installers: make installers {posargs}
    flake8: python --version
    flake8: python -c "import platform; print(platform.architecture())"
    flake8: python -m pip install --disable-pip-version-check --upgrade pip
    flake8: flake8 --config=./tox.ini generated/
    flake8: flake8 --config=./tox.ini tools/
    flake8: flake8 --config=./tox.ini src/nidcpower/system_tests/ src/nidcpower/examples/
    flake8: flake8 --config=./tox.ini src/nidigital/system_tests/ src/nidigital/examples/
    flake8: flake8 --config=./tox.ini src/nidmm/system_tests/ src/nidmm/examples/
    flake8: flake8 --config=./tox.ini src/nifgen/system_tests/ src/nifgen/examples/
    flake8: flake8 --config=./tox.ini src/nimodinst/system_tests/ src/nimodinst/examples/
    flake8: flake8 --config=./tox.ini src/nirfsg/system_tests/ src/nirfsg/examples/
    flake8: flake8 --config=./tox.ini src/niscope/system_tests/ src/niscope/examples/
    flake8: flake8 --config=./tox.ini src/nise/system_tests/ src/nise/examples/
    flake8: flake8 --config=./tox.ini src/niswitch/system_tests/ src/niswitch/examples/
    flake8: flake8 --config=./tox.ini src/nitclk/system_tests/ src/nitclk/examples/
    docs: python --version
    docs: python -c "import platform; print(platform.architecture())"
    docs: sphinx-build -b html -d {envtmpdir}/doctrees ./nidcpower ../generated/docs/nidcpower/html {posargs}
    docs: sphinx-build -b html -d {envtmpdir}/doctrees ./nidigital ../generated/docs/nidigital/html {posargs}
    docs: sphinx-build -b html -d {envtmpdir}/doctrees ./nidmm ../generated/docs/nidmm/html {posargs}
    docs: sphinx-build -b html -d {envtmpdir}/doctrees ./nifgen ../generated/docs/nifgen/html {posargs}
    docs: sphinx-build -b html -d {envtmpdir}/doctrees ./nimodinst ../generated/docs/nimodinst/html {posargs}
    docs: sphinx-build -b html -d {envtmpdir}/doctrees ./nirfsg ../generated/docs/nirfsg/html {posargs}
    docs: sphinx-build -b html -d {envtmpdir}/doctrees ./niscope ../generated/docs/niscope/html {posargs}
    docs: sphinx-build -b html -d {envtmpdir}/doctrees ./nise ../generated/docs/nise/html {posargs}
    docs: sphinx-build -b html -d {envtmpdir}/doctrees ./niswitch ../generated/docs/niswitch/html {posargs}
    docs: sphinx-build -b html -d {envtmpdir}/doctrees ./nitclk ../generated/docs/nitclk/html {posargs}
    pkg: python --version
    pkg: python -c "import platform; print(platform.architecture())"
    pkg: python -m twine --version
    pkg: python -m twine check generated/nifake/dist/*
    pkg: python -m twine check generated/nidcpower/dist/*
    pkg: python -m twine check generated/nidigital/dist/*
    pkg: python -m twine check generated/nidmm/dist/*
    pkg: python -m twine check generated/nifgen/dist/*
    pkg: python -m twine check generated/nirfsg/dist/*
    pkg: python -m twine check generated/niscope/dist/*
    pkg: python -m twine check generated/nise/dist/*
    pkg: python -m twine check generated/niswitch/dist/*
    # pkg: check-manifest --ignore tox.ini,tests*,.github,.github/*,CONTRIBUTING.rst,docs,docs/*

deps =
    test: pytest
    test: pytest-timeout
    test: coverage
    test: mako
    test: numpy
    test: hightime
    test: grpcio == 1.75.1  # Compatible with Python 3.14; should be backwards compatible with grpcio-tools 1.59.0
    test: protobuf == 5.27.2  # Compatible with Python 3.14; should be backwards compatible with grpcio-tools 1.59.0
    test: ni.grpcdevice.v1.proto >= 1.0.0  # Provides session_pb2 package at runtime since we no longer generate it per-driver
    build_test: pytest
    build_test: coverage
    build_test: mako
    build_test: hacking
    build_test: pep8-naming
    codegen: mako
    codegen: packaging
    codegen: setuptools < 82 # grpcio-tools 1.59.0 needs pkg_resources which was removed in setuptools v82
    codegen: grpcio-tools == 1.59.0 # First version to support Python 3.12
    installers: build
    flake8: hacking
    flake8: pep8-naming
    docs: sphinx
    docs: sphinx-rtd-theme
    pkg: check-manifest
    pkg: docutils
    pkg: pygments
    pkg: twine

depends =
    codegen: py312-clean
    installers: py312-codegen
    flake8: py312-codegen
    docs: py312-codegen
    test: py312-installers
    pkg: py312-installers

allowlist_externals =
    build_test: mv
    test: mv
    codegen: make
    installers: make
    clean: make

[flake8]
show_source = true
# We recommend setting your editor's visual guide to 79 but allow overflow to
# 160 for readability in certain cases due to generated code
# max_line_length = 160
exclude = build,docs,.tox,__pycache__,processed_metadata,.eggs,*_pb2*.py,third_party
# H903: Windows style line endings not allowed in code
# E501: Line length
# W391: Blank line at end of file
ignore = H903,E501,W391

[pytest]
addopts = --verbose --doctest-modules --ignore=setup.py
norecursedirs = system_tests examples .* build dist CVS _darcs {arch} *.egg venv
junit_suite_name = nimi-python
python_files = *.py
junit_family = xunit1
````
