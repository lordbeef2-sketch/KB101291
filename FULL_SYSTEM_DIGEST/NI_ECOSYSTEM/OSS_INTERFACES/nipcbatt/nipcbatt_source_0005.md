# NI OSS SOURCE SNAPSHOT: nipcbatt

<!--NI_OSS_SNAPSHOT repo=ni/nipcbatt commit=a26fcd38af55e0286aacff6cdc44bf53b2041111 -->

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/temperature_measurements/test_temperature_data_types.py sha256=fff531283d156911fa998bb97942229e87b92792da8f44d3b8a49865a6f5cd91 bytes=87202 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/temperature_measurements/test_temperature_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/temperature_measurements/test_temperature_data_types.py`
- sha256: `fff531283d156911fa998bb97942229e87b92792da8f44d3b8a49865a6f5cd91`
- bytes: 87202

````python
# pylint: disable=C0301
"""This module provides temperature data types check."""
import importlib.metadata
import logging
import random
import sys
import unittest

import nidaqmx.constants
import numpy
from varname import nameof

import nipcbatt
from nipcbatt import daq


class TestTemperatureRtdMeasurementConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    `TemperatureRtdMeasurementConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_temperature_rtd_measurement_configuration_init_fails_when_global_channel_parameters_is_none(
        self,
    ):
        """unit test of TemperatureRtdMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (164 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TemperatureRtdMeasurementConfiguration(
                    global_channel_parameters=None,
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object global_channel_parameters is None.", str(ctx.exception))

    def test_temperature_rtd_measurement_configuration_init_fails_when_specific_channels_parameters_is_none(
        self,
    ):
        """unit test of TemperatureRtdMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (164 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TemperatureRtdMeasurementConfiguration(
                    global_channel_parameters=(
                        daq.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=None,
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object specific_channels_parameters is None.", str(ctx.exception))

    def test_temperature_rtd_measurement_configuration_init_fails_when_sample_clock_timing_parameters_is_none(
        self,
    ):
        """unit test of TemperatureRtdMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (164 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TemperatureRtdMeasurementConfiguration(
                    global_channel_parameters=(
                        daq.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=None,
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object sample_clock_timing_parameters is None.", str(ctx.exception))

    def test_temperature_rtd_measurement_configuration_init_fails_when_digital_start_trigger_parameters_is_none(
        self,
    ):
        """unit test of TemperatureRtdMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (164 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TemperatureRtdMeasurementConfiguration(
                    global_channel_parameters=(
                        daq.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=None,
                )
            )

        # Assert
        self.assertEqual("The object digital_start_trigger_parameters is None.", str(ctx.exception))

    def test_temperature_rtd_measurement_configuration(self):
        """unit test of TemperatureRtdMeasurementConfiguration."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (241 > 100 characters) (auto-generated noqa)

        # Arrange

        expected_global_channel_parameters = daq.TemperatureRtdMeasurementTerminalParameters(
            temperature_minimum_value_celsius_degrees=1.0,
            temperature_maximum_value_celsius_degrees=99.0,
            current_excitation_value_amperes=1.0,
            sensor_resistance_ohms=10.0,
            rtd_type=nidaqmx.constants.RTDType.PT_3916,
            excitation_source=nidaqmx.constants.ExcitationSource.EXTERNAL,
            resistance_configuration=nidaqmx.constants.ResistanceConfiguration.TWO_WIRE,
            adc_timing_mode=nidaqmx.constants.ADCTimingMode.BEST_60_HZ_REJECTION,
        )

        expected_specific_channels_parameters = []
        expected_specific_channels_parameters.append(
            daq.TemperatureRtdMeasurementChannelParameters(
                channel_name="Dev/ai0",
                sensor_resistance_ohms=8.0,
                current_excitation_value_amperes=2.0,
                rtd_type=nidaqmx.constants.RTDType.PT_3851,
                resistance_configuration=nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE,
                excitation_source=nidaqmx.constants.ExcitationSource.NONE,
            ),
        )

        expected_specific_channels_parameters.append(
            daq.TemperatureRtdMeasurementChannelParameters(
                channel_name="Dev/ai1",
                sensor_resistance_ohms=11.0,
                current_excitation_value_amperes=3.0,
                rtd_type=nidaqmx.constants.RTDType.PT_3928,
                resistance_configuration=nidaqmx.constants.ResistanceConfiguration.THREE_WIRE,
                excitation_source=nidaqmx.constants.ExcitationSource.INTERNAL,
            ),
        )
        expected_specific_channels_parameters.append(
            daq.TemperatureRtdMeasurementChannelParameters(
                channel_name="Dev/ai2",
                sensor_resistance_ohms=7.0,
                current_excitation_value_amperes=6.0,
                rtd_type=nidaqmx.constants.RTDType.PT_3911,
                resistance_configuration=nidaqmx.constants.ResistanceConfiguration.TWO_WIRE,
                excitation_source=nidaqmx.constants.ExcitationSource.EXTERNAL,
            ),
        )

        expected_sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source="OnboardClock",
            sampling_rate_hertz=100,
            number_of_samples_per_channel=10,
            sample_timing_engine=nipcbatt.SampleTimingEngine.TE0,
        )

        expected_measurement_execution_type = nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY

        expected_digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
            digital_start_trigger_source="trigger_source",
            digital_start_trigger_edge=nidaqmx.constants.Edge.FALLING,
        )

        logging.debug(
            "%s = %s",
            nameof(expected_specific_channels_parameters),
            expected_specific_channels_parameters,
        )

        # Act
        temperature_rtd_configuration_instance = daq.TemperatureRtdMeasurementConfiguration(
            global_channel_parameters=expected_global_channel_parameters,
            specific_channels_parameters=expected_specific_channels_parameters,
            measurement_execution_type=expected_measurement_execution_type,
            sample_clock_timing_parameters=expected_sample_clock_timing_parameters,
            digital_start_trigger_parameters=expected_digital_start_trigger_parameters,
        )

        logging.debug(
            "%s = %s",
            nameof(temperature_rtd_configuration_instance),
            temperature_rtd_configuration_instance,
        )

        # Assert
        self.assertListEqual(
            expected_specific_channels_parameters,
            temperature_rtd_configuration_instance.specific_channels_parameters,
        )
        self.assertEqual(
            expected_global_channel_parameters,
            temperature_rtd_configuration_instance.global_channel_parameters,
        )
        self.assertEqual(
            expected_measurement_execution_type,
            temperature_rtd_configuration_instance.measurement_execution_type,
        )
        self.assertEqual(
            expected_sample_clock_timing_parameters,
            temperature_rtd_configuration_instance.sample_clock_timing_parameters,
        )
        self.assertEqual(
            expected_digital_start_trigger_parameters,
            temperature_rtd_configuration_instance.digital_start_trigger_parameters,
        )


class TestTemperatureRtdMeasurementTerminalParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `TemperatureRtdMeasurementTerminalParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_temperature_rtd_measurement_terminal_parameters_init_fails_if_maximum_is_less_that_minimum(
        self,
    ):
        """unit test of TemperatureRtdMeasurementTerminalParameters."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (169 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TemperatureRtdMeasurementTerminalParameters(
                    temperature_minimum_value_celsius_degrees=99.0,
                    temperature_maximum_value_celsius_degrees=1.0,
                    current_excitation_value_amperes=1.5,
                    sensor_resistance_ohms=25.0,
                    rtd_type=nidaqmx.constants.RTDType.PT_3750,
                    excitation_source=nidaqmx.constants.ExcitationSource.EXTERNAL,
                    resistance_configuration=nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE,
                    adc_timing_mode=nidaqmx.constants.ADCTimingMode.AUTOMATIC,
                )
            )

        # Assert
        self.assertEqual(
            "The value temperature_minimum_value_celsius_degrees must be less than 1.0.",
            str(ctx.exception),
        )

    def test_temperature_rtd_measurement_terminal_parameters(self):
        """unit test of TemperatureRtdMeasurementTerminalParameters."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (169 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        expected_temperature_rtd_measurement_terminal_parameters = (
            daq.TemperatureRtdMeasurementTerminalParameters(
                temperature_minimum_value_celsius_degrees=1.0,
                temperature_maximum_value_celsius_degrees=99.0,
                current_excitation_value_amperes=1.5,
                sensor_resistance_ohms=25.0,
                rtd_type=nidaqmx.constants.RTDType.PT_3750,
                excitation_source=nidaqmx.constants.ExcitationSource.EXTERNAL,
                resistance_configuration=nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE,
                adc_timing_mode=nidaqmx.constants.ADCTimingMode.AUTOMATIC,
            )
        )

        # Assert
        self.assertEqual(
            1.0,
            expected_temperature_rtd_measurement_terminal_parameters.temperature_minimum_value_celsius_degrees,
        )
        self.assertEqual(
            99.0,
            expected_temperature_rtd_measurement_terminal_parameters.temperature_maximum_value_celsius_degrees,
        )
        self.assertEqual(
            1.5,
            expected_temperature_rtd_measurement_terminal_parameters.current_excitation_value_amperes,
        )
        self.assertEqual(
            25.0,
            expected_temperature_rtd_measurement_terminal_parameters.sensor_resistance_ohms,
        )
        self.assertEqual(
            nidaqmx.constants.RTDType.PT_3750,
            expected_temperature_rtd_measurement_terminal_parameters.rtd_type,
        )
        self.assertEqual(
            nidaqmx.constants.ExcitationSource.EXTERNAL,
            expected_temperature_rtd_measurement_terminal_parameters.excitation_source,
        )
        self.assertEqual(
            nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE,
            expected_temperature_rtd_measurement_terminal_parameters.resistance_configuration,
        )
        self.assertEqual(
            nidaqmx.constants.ADCTimingMode.AUTOMATIC,
            expected_temperature_rtd_measurement_terminal_parameters.adc_timing_mode,
        )


class TestTemperatureRtdMeasurementChannelParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `TemperatureRtdMeasurementTerminalParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_temperature_rtd_measurement_channel_parameters_init_fails_if_channel_name_is_none(
        self,
    ):
        """unit test of TemperatureRtdMeasurementChannelParameters."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (168 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TemperatureRtdMeasurementChannelParameters(
                    channel_name=None,
                    sensor_resistance_ohms=25.0,
                    current_excitation_value_amperes=1.5,
                    rtd_type=nidaqmx.constants.RTDType.PT_3750,
                    resistance_configuration=nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE,
                    excitation_source=nidaqmx.constants.ExcitationSource.EXTERNAL,
                )
            )

        # Assert
        self.assertEqual(
            "The string value channel_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_temperature_rtd_measurement_channel_parameters_init_fails_if_channel_name_is_empty(
        self,
    ):
        """unit test of TemperatureRtdMeasurementChannelParameters."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (168 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TemperatureRtdMeasurementChannelParameters(
                    channel_name="",
                    sensor_resistance_ohms=25.0,
                    current_excitation_value_amperes=1.5,
                    rtd_type=nidaqmx.constants.RTDType.PT_3750,
                    resistance_configuration=nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE,
                    excitation_source=nidaqmx.constants.ExcitationSource.EXTERNAL,
                )
            )

        # Assert
        self.assertEqual(
            "The string value channel_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_temperature_rtd_measurement_channel_parameters_init_fails_if_channel_name_is_whitespace(
        self,
    ):
        """unit test of TemperatureRtdMeasurementChannelParameters."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (168 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TemperatureRtdMeasurementChannelParameters(
                    channel_name=" ",
                    sensor_resistance_ohms=25.0,
                    current_excitation_value_amperes=1.5,
                    rtd_type=nidaqmx.constants.RTDType.PT_3750,
                    resistance_configuration=nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE,
                    excitation_source=nidaqmx.constants.ExcitationSource.EXTERNAL,
                )
            )

        # Assert
        self.assertEqual(
            "The string value channel_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_temperature_rtd_measurement_channel_parameters(self):
        """unit test of TemperatureRtdMeasurementChannelParameters."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (168 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        expected_temperature_rtd_measurement_channel_parameters = (
            daq.TemperatureRtdMeasurementChannelParameters(
                channel_name="Dev/ai0",
                sensor_resistance_ohms=25.0,
                current_excitation_value_amperes=1.5,
                rtd_type=nidaqmx.constants.RTDType.PT_3750,
                resistance_configuration=nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE,
                excitation_source=nidaqmx.constants.ExcitationSource.EXTERNAL,
            )
        )

        # Assert
        self.assertEqual(
            "Dev/ai0",
            expected_temperature_rtd_measurement_channel_parameters.channel_name,
        )
        self.assertEqual(
            25.0,
            expected_temperature_rtd_measurement_channel_parameters.sensor_resistance_ohms,
        )
        self.assertEqual(
            1.5,
            expected_temperature_rtd_measurement_channel_parameters.current_excitation_value_amperes,
        )
        self.assertEqual(
            nidaqmx.constants.RTDType.PT_3750,
            expected_temperature_rtd_measurement_channel_parameters.rtd_type,
        )
        self.assertEqual(
            nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE,
            expected_temperature_rtd_measurement_channel_parameters.resistance_configuration,
        )
        self.assertEqual(
            nidaqmx.constants.ExcitationSource.EXTERNAL,
            expected_temperature_rtd_measurement_channel_parameters.excitation_source,
        )


class TestTemperatureMeasurementResultData(unittest.TestCase):
    """Defines a test fixture that checks
    `TemperatureMeasurementResultData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self,
        methodName: str = "runTest",  # noqa: N803 - argument name 'methodName' should be lowercase (auto-generated noqa)
    ) -> None:
        super().__init__(methodName)
        self._expected_waveforms = None

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_temperature_measurement_result_data_init_fails_when_waveforms_is_none(
        self,
    ):
        """unit test of TemperatureMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (158 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_acquisition_duration_seconds = 0.3
        expected_average_temperatures_celsius_degrees = [25.0, 23.0, 10.0]
        expected_average_temperatures_kelvin = [1.0, 1.0, 1.0]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TemperatureMeasurementResultData(
                    waveforms=None,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    average_temperatures_celsius_degrees=expected_average_temperatures_celsius_degrees,
                    average_temperatures_kelvin=expected_average_temperatures_kelvin,
                )
            )

        # Assert
        self.assertEqual("The object waveforms is None.", str(ctx.exception))

    def test_temperature_measurement_result_data_init_fails_when_waveforms_is_empty(
        self,
    ):
        """unit test of TemperatureMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (158 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_acquisition_duration_seconds = 0.3
        expected_average_temperatures_celsius_degrees = [25.0, 23.0, 10.0]
        expected_average_temperatures_kelvin = [1.0, 1.0, 1.0]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TemperatureMeasurementResultData(
                    waveforms=[],
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    average_temperatures_celsius_degrees=expected_average_temperatures_celsius_degrees,
                    average_temperatures_kelvin=expected_average_temperatures_kelvin,
                )
            )

        # Assert
        self.assertEqual("The iterable waveforms of type list is empty.", str(ctx.exception))

    def test_temperature_measurement_result_data_init_fails_when_waveforms_contains_object_that_are_not_of_analog_waveform(
        self,
    ):
        """unit test of TemperatureMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (158 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_acquisition_duration_seconds = 0.3
        expected_average_temperatures_celsius_degrees = [25.0, 23.0, 10.0]
        expected_average_temperatures_kelvin = [1.0, 1.0, 1.0]

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                daq.TemperatureMeasurementResultData(
                    waveforms=[2.0, "3.5"],
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    average_temperatures_celsius_degrees=expected_average_temperatures_celsius_degrees,
                    average_temperatures_kelvin=expected_average_temperatures_kelvin,
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (AnalogWaveform).",
            str(ctx.exception),
        )

    def test_temperature_measurement_result_data_init_fails_when_average_temperatures_celsius_degrees_is_none(
        self,
    ):
        """unit test of TemperatureMeasurementResultData."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (235 > 100 characters) (auto-generated noqa)

        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_average_temperatures_kelvin = [1.0, 1.0, 1.0]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TemperatureMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    average_temperatures_celsius_degrees=None,
                    average_temperatures_kelvin=expected_average_temperatures_kelvin,
                )
            )

        # Assert
        self.assertEqual(
            "The object average_temperatures_celsius_degrees is None.",
            str(ctx.exception),
        )

    def test_temperature_measurement_result_data_init_fails_when_average_temperatures_celsius_degrees_is_empty(
        self,
    ):
        """unit test of TemperatureMeasurementResultData."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (235 > 100 characters) (auto-generated noqa)

        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_average_temperatures_kelvin = [1.0, 1.0, 1.0]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TemperatureMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    average_temperatures_celsius_degrees=[],
                    average_temperatures_kelvin=expected_average_temperatures_kelvin,
                )
            )

        # Assert
        self.assertEqual(
            "The iterable average_temperatures_celsius_degrees of type list is empty.",
            str(ctx.exception),
        )

    def test_temperature_measurement_result_data_init_fails_when_average_temperatures_celsius_degrees_contains_object_that_are_not_of_float(
        self,
    ):
        """unit test of TemperatureMeasurementResultData."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (235 > 100 characters) (auto-generated noqa)

        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_average_temperatures_kelvin = [1.0, 1.0, 1.0]

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                daq.TemperatureMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    average_temperatures_celsius_degrees=["2.3", 23.0, 27.0],
                    average_temperatures_kelvin=expected_average_temperatures_kelvin,
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (float).",
            str(ctx.exception),
        )

    def test_temperature_measurement_result_data_init_fails_when_average_temperatures_kelvins_is_none(
        self,
    ):
        """unit test of TemperatureMeasurementResultData."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (235 > 100 characters) (auto-generated noqa)

        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_average_temperatures_celsius_degrees = [1.0, 1.0, 1.0]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TemperatureMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    average_temperatures_celsius_degrees=expected_average_temperatures_celsius_degrees,
                    average_temperatures_kelvin=None,
                )
            )

        # Assert
        self.assertEqual(
            "The object average_temperatures_kelvin is None.",
            str(ctx.exception),
        )

    def test_temperature_measurement_result_data_init_fails_when_average_temperatures_kelvins_is_empty(
        self,
    ):
        """unit test of TemperatureMeasurementResultData."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (235 > 100 characters) (auto-generated noqa)

        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_average_temperatures_celsius_degrees = [1.0, 1.0, 1.0]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TemperatureMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    average_temperatures_celsius_degrees=expected_average_temperatures_celsius_degrees,
                    average_temperatures_kelvin=[],
                )
            )

        # Assert
        self.assertEqual(
            "The iterable average_temperatures_kelvin of type list is empty.",
            str(ctx.exception),
        )

    def test_temperature_measurement_result_data_init_fails_when_average_temperatures_kelvins_contains_object_that_are_not_of_float(
        self,
    ):
        """unit test of TemperatureMeasurementResultData."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (235 > 100 characters) (auto-generated noqa)

        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_average_temperatures_celsius_degrees = [1.0, 1.0, 1.0]

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                daq.TemperatureMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    average_temperatures_celsius_degrees=expected_average_temperatures_celsius_degrees,
                    average_temperatures_kelvin=["2.3", 23.0, 27.0],
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (float).",
            str(ctx.exception),
        )

    def _initialize_waveforms(self):
        self._expected_waveforms = []
        self._expected_waveforms.append(
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai0",
                delta_time_seconds=1.0 / 100,
                samples=numpy.ones(shape=(10), dtype=numpy.float64),
            )
        )
        self._expected_waveforms.append(
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai1",
                delta_time_seconds=1.0 / 100,
                samples=numpy.array(
                    [random.random() * 0.1 for item in range(0, 10)],
                    dtype=numpy.float64,
                ),
            )
        )
        self._expected_waveforms.append(
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai2",
                delta_time_seconds=1.0 / 100,
                samples=numpy.array(
                    [random.random() * 0.1 for item in range(0, 10)],
                    dtype=numpy.float64,
                ),
            )
        )


class TestTemperatureThermistorMeasurementConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    `TemperatureThermistorMeasurementConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_temperature_thermistor_measurement_configuration_init_fails_when_global_channel_parameters_is_none(
        self,
    ):
        """unit test of TemperatureThermistorMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TemperatureThermistorMeasurementConfiguration(
                    global_channel_parameters=None,
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object global_channel_parameters is None.", str(ctx.exception))

    def test_temperature_thermistor_measurement_configuration_init_fails_when_specific_channels_parameters_is_none(
        self,
    ):
        """unit test of TemperatureThermistorMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TemperatureThermistorMeasurementConfiguration(
                    global_channel_parameters=(
                        daq.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=None,
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object specific_channels_parameters is None.", str(ctx.exception))

    def test_temperature_thermistor_measurement_configuration_init_fails_when_sample_clock_timing_parameters_is_none(
        self,
    ):
        """unit test of TemperatureThermistorMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TemperatureThermistorMeasurementConfiguration(
                    global_channel_parameters=(
                        daq.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=None,
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object sample_clock_timing_parameters is None.", str(ctx.exception))

    def test_temperature_thermistor_measurement_configuration_init_fails_when_digital_start_trigger_parameters_is_none(
        self,
    ):
        """unit test of TemperatureThermistorMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TemperatureThermistorMeasurementConfiguration(
                    global_channel_parameters=(
                        daq.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=None,
                )
            )

        # Assert
        self.assertEqual("The object digital_start_trigger_parameters is None.", str(ctx.exception))

    def test_temperature_thermistor_measurement_configuration(self):
        """unit test of TemperatureThermistorMeasurementConfiguration."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (248 > 100 characters) (auto-generated noqa)

        # Arrange

        expected_global_channel_parameters = (
            daq.DEFAULT_TEMPERATURE_THERMISTOR_RANGE_AND_TERMINAL_PARAMETERS
        )

        expected_specific_channels_parameters = []
        expected_specific_channels_parameters.append(
            daq.TemperatureThermistorChannelRangeAndTerminalParameters(
                channel_name="Dev/ai0",
                channel_parameters=daq.TemperatureThermistorRangeAndTerminalParameters(
                    terminal_configuration=nidaqmx.constants.TerminalConfiguration.DEFAULT,
                    temperature_minimum_value_celsius_degrees=10.0,
                    temperature_maximum_value_celsius_degrees=89.0,
                    voltage_excitation_value_volts=15.0,
                    thermistor_resistor_ohms=5.0,
                    steinhart_hart_equation_option=daq.SteinhartHartEquationOption.USE_STEINHART_HART_COEFFICIENTS,
                    coefficients_steinhart_hart_parameters=daq.CoefficientsSteinhartHartParameters(
                        coefficient_steinhart_hart_a=10.0,
                        coefficient_steinhart_hart_b=20.0,
                        coefficient_steinhart_hart_c=10.0,
                    ),
                    beta_coefficient_and_sensor_resistance_parameters=daq.BetaCoefficientAndSensorResistanceParameters(
                        coefficient_steinhart_hart_beta_kelvins=289.15,
                        sensor_resistance_ohms=5.0,
                    ),
                ),
            ),
        )

        expected_specific_channels_parameters.append(
            daq.TemperatureThermistorChannelRangeAndTerminalParameters(
                channel_name="Dev/ai1",
                channel_parameters=daq.TemperatureThermistorRangeAndTerminalParameters(
                    terminal_configuration=nidaqmx.constants.TerminalConfiguration.NRSE,
                    temperature_minimum_value_celsius_degrees=1.0,
                    temperature_maximum_value_celsius_degrees=79.0,
                    voltage_excitation_value_volts=10.0,
                    thermistor_resistor_ohms=10.0,
                    steinhart_hart_equation_option=daq.SteinhartHartEquationOption.USE_STEINHART_HART_COEFFICIENTS,
                    coefficients_steinhart_hart_parameters=daq.CoefficientsSteinhartHartParameters(
                        coefficient_steinhart_hart_a=1.5,
                        coefficient_steinhart_hart_b=2.5,
                        coefficient_steinhart_hart_c=10.0,
                    ),
                    beta_coefficient_and_sensor_resistance_parameters=daq.BetaCoefficientAndSensorResistanceParameters(
                        coefficient_steinhart_hart_beta_kelvins=303.15,
                        sensor_resistance_ohms=15.0,
                    ),
                ),
            ),
        )
        expected_specific_channels_parameters.append(
            daq.TemperatureThermistorChannelRangeAndTerminalParameters(
                channel_name="Dev/ai2",
                channel_parameters=daq.TemperatureThermistorRangeAndTerminalParameters(
                    terminal_configuration=nidaqmx.constants.TerminalConfiguration.DIFF,
                    temperature_minimum_value_celsius_degrees=0.0,
                    temperature_maximum_value_celsius_degrees=100.0,
                    voltage_excitation_value_volts=10.0,
                    thermistor_resistor_ohms=15.0,
                    steinhart_hart_equation_option=daq.SteinhartHartEquationOption.USE_STEINHART_HART_COEFFICIENTS,
                    coefficients_steinhart_hart_parameters=daq.CoefficientsSteinhartHartParameters(
                        coefficient_steinhart_hart_a=15.0,
                        coefficient_steinhart_hart_b=25.0,
                        coefficient_steinhart_hart_c=16.0,
                    ),
                    beta_coefficient_and_sensor_resistance_parameters=daq.BetaCoefficientAndSensorResistanceParameters(
                        coefficient_steinhart_hart_beta_kelvins=289.15,
                        sensor_resistance_ohms=5.0,
                    ),
                ),
            ),
        )

        expected_sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source="OnboardClock",
            sampling_rate_hertz=100,
            number_of_samples_per_channel=10,
            sample_timing_engine=nipcbatt.SampleTimingEngine.TE0,
        )

        expected_measurement_execution_type = nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY

        expected_digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
            digital_start_trigger_source="trigger_source",
            digital_start_trigger_edge=nidaqmx.constants.Edge.FALLING,
        )

        logging.debug(
            "%s = %s",
            nameof(expected_specific_channels_parameters),
            expected_specific_channels_parameters,
        )

        # Act
        temperature_thermistor_configuration_instance = (
            daq.TemperatureThermistorMeasurementConfiguration(
                global_channel_parameters=expected_global_channel_parameters,
                specific_channels_parameters=expected_specific_channels_parameters,
                measurement_execution_type=expected_measurement_execution_type,
                sample_clock_timing_parameters=expected_sample_clock_timing_parameters,
                digital_start_trigger_parameters=expected_digital_start_trigger_parameters,
            )
        )

        logging.debug(
            "%s = %s",
            nameof(temperature_thermistor_configuration_instance),
            temperature_thermistor_configuration_instance,
        )

        # Assert
        self.assertListEqual(
            expected_specific_channels_parameters,
            temperature_thermistor_configuration_instance.specific_channels_parameters,
        )
        self.assertEqual(
            expected_global_channel_parameters,
            temperature_thermistor_configuration_instance.global_channel_parameters,
        )
        self.assertEqual(
            expected_measurement_execution_type,
            temperature_thermistor_configuration_instance.measurement_execution_type,
        )
        self.assertEqual(
            expected_sample_clock_timing_parameters,
            temperature_thermistor_configuration_instance.sample_clock_timing_parameters,
        )
        self.assertEqual(
            expected_digital_start_trigger_parameters,
            temperature_thermistor_configuration_instance.digital_start_trigger_parameters,
        )


class TestCoefficientsSteinhartHartParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `CoefficientsSteinhartHartParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_coefficients_steinhart_hart_parameters(self):
        """unit test of CoefficientsSteinhartHartParameters."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        expected_coefficients_steinhart_hart_parameters = (
            daq.CoefficientsSteinhartHartParameters(
                coefficient_steinhart_hart_a=10.0,
                coefficient_steinhart_hart_b=25.0,
                coefficient_steinhart_hart_c=5.0,
            )
        )

        # Assert
        self.assertEqual(
            10.0,
            expected_coefficients_steinhart_hart_parameters.coefficient_steinhart_hart_a,
        )
        self.assertEqual(
            25.0,
            expected_coefficients_steinhart_hart_parameters.coefficient_steinhart_hart_b,
        )
        self.assertEqual(
            5.0,
            expected_coefficients_steinhart_hart_parameters.coefficient_steinhart_hart_c,
        )


class TestBetaCoefficientAndSensorResistanceParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `BetaCoefficientAndSensorResistanceParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_beta_coefficient_and_sensor_resistance_parameters(self):
        """unit test of BetaCoefficientAndSensorResistanceParameters."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (170 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        expected_beta_coefficient_and_sensor_resistance_parameters = (
            daq.BetaCoefficientAndSensorResistanceParameters(
                coefficient_steinhart_hart_beta_kelvins=289.15,
                sensor_resistance_ohms=10.0,
            )
        )

        # Assert
        self.assertEqual(
            289.15,
            expected_beta_coefficient_and_sensor_resistance_parameters.coefficient_steinhart_hart_beta_kelvins,
        )
        self.assertEqual(
            10.0,
            expected_beta_coefficient_and_sensor_resistance_parameters.sensor_resistance_ohms,
        )


class TestTemperatureThermistorRangeAndTerminalParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `TemperatureThermistorRangeAndTerminalParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_temperature_thermistor_range_and_terminal_parameters_init_fails_if_maximum_is_less_that_minimum(
        self,
    ):
        """unit test of TemperatureThermistorRangeAndTerminalParameters."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_coefficients_steinhart_hart_parameters = (
            daq.CoefficientsSteinhartHartParameters(
                coefficient_steinhart_hart_a=10.0,
                coefficient_steinhart_hart_b=25.0,
                coefficient_steinhart_hart_c=5.0,
            )
        )
        expected_beta_coefficient_and_sensor_resistance_parameters = (
            daq.BetaCoefficientAndSensorResistanceParameters(
                coefficient_steinhart_hart_beta_kelvins=289.15,
                sensor_resistance_ohms=10.0,
            )
        )
        # Act

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TemperatureThermistorRangeAndTerminalParameters(
                    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
                    temperature_minimum_value_celsius_degrees=99.0,
                    temperature_maximum_value_celsius_degrees=1.0,
                    voltage_excitation_value_volts=5.0,
                    thermistor_resistor_ohms=10.0,
                    steinhart_hart_equation_option=daq.SteinhartHartEquationOption.USE_STEINHART_HART_COEFFICIENTS,
                    coefficients_steinhart_hart_parameters=expected_coefficients_steinhart_hart_parameters,
                    beta_coefficient_and_sensor_resistance_parameters=expected_beta_coefficient_and_sensor_resistance_parameters,
                )
            )

        # Assert
        self.assertEqual(
            "The value temperature_minimum_value_celsius_degrees must be less than 1.0.",
            str(ctx.exception),
        )

    def test_temperature_thermistor_range_and_terminal_parameters(self):
        """unit test of TemperatureThermistorRangeAndTerminalParameters."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_coefficients_steinhart_hart_parameters = (
            daq.CoefficientsSteinhartHartParameters(
                coefficient_steinhart_hart_a=10.0,
                coefficient_steinhart_hart_b=25.0,
                coefficient_steinhart_hart_c=5.0,
            )
        )
        expected_beta_coefficient_and_sensor_resistance_parameters = (
            daq.BetaCoefficientAndSensorResistanceParameters(
                coefficient_steinhart_hart_beta_kelvins=289.15,
                sensor_resistance_ohms=10.0,
            )
        )

        # Act
        expected_temperature_thermistor_range_and_terminal_parameters = daq.TemperatureThermistorRangeAndTerminalParameters(
            terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
            temperature_minimum_value_celsius_degrees=0.0,
            temperature_maximum_value_celsius_degrees=100.0,
            voltage_excitation_value_volts=5.0,
            thermistor_resistor_ohms=10.0,
            steinhart_hart_equation_option=daq.SteinhartHartEquationOption.USE_STEINHART_HART_COEFFICIENTS,
            coefficients_steinhart_hart_parameters=expected_coefficients_steinhart_hart_parameters,
            beta_coefficient_and_sensor_resistance_parameters=expected_beta_coefficient_and_sensor_resistance_parameters,
        )

        # Assert
        self.assertEqual(
            nidaqmx.constants.TerminalConfiguration.RSE,
            expected_temperature_thermistor_range_and_terminal_parameters.terminal_configuration,
        )
        self.assertEqual(
            0.0,
            expected_temperature_thermistor_range_and_terminal_parameters.temperature_minimum_value_celsius_degrees,
        )
        self.assertEqual(
            100.0,
            expected_temperature_thermistor_range_and_terminal_parameters.temperature_maximum_value_celsius_degrees,
        )
        self.assertEqual(
            5.0,
            expected_temperature_thermistor_range_and_terminal_parameters.voltage_excitation_value_volts,
        )
        self.assertEqual(
            10.0,
            expected_temperature_thermistor_range_and_terminal_parameters.thermistor_resistor_ohms,
        )
        self.assertEqual(
            daq.SteinhartHartEquationOption.USE_STEINHART_HART_COEFFICIENTS,
            expected_temperature_thermistor_range_and_terminal_parameters.steinhart_hart_equation_option,
        )
        self.assertEqual(
            expected_coefficients_steinhart_hart_parameters,
            expected_temperature_thermistor_range_and_terminal_parameters.coefficients_steinhart_hart_parameters,
        )
        self.assertEqual(
            expected_beta_coefficient_and_sensor_resistance_parameters,
            expected_temperature_thermistor_range_and_terminal_parameters.beta_coefficient_and_sensor_resistance_parameters,
        )


class TestTemperatureThermocoupleMeasurementConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    `TemperatureThermocoupleMeasurementConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_temperature_thermocouple_measurement_configuration_init_fails_when_global_channel_parameters_is_none(
        self,
    ):
        """unit test of TemperatureThermocoupleMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TemperatureThermocoupleMeasurementConfiguration(
                    global_channel_parameters=None,
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object global_channel_parameters is None.", str(ctx.exception))

    def test_temperature_thermocouple_measurement_configuration_init_fails_when_specific_channels_parameters_is_none(
        self,
    ):
        """unit test of TemperatureThermocoupleMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TemperatureThermocoupleMeasurementConfiguration(
                    global_channel_parameters=(
                        daq.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=None,
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object specific_channels_parameters is None.", str(ctx.exception))

    def test_temperature_thermocouple_measurement_configuration_init_fails_when_sample_clock_timing_parameters_is_none(
        self,
    ):
        """unit test of TemperatureThermocoupleMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TemperatureThermocoupleMeasurementConfiguration(
                    global_channel_parameters=(
                        daq.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=None,
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object sample_clock_timing_parameters is None.", str(ctx.exception))

    def test_temperature_thermocouple_measurement_configuration_init_fails_when_digital_start_trigger_parameters_is_none(
        self,
    ):
        """unit test of TemperatureThermocoupleMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TemperatureThermocoupleMeasurementConfiguration(
                    global_channel_parameters=(
                        daq.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=None,
                )
            )

        # Assert
        self.assertEqual("The object digital_start_trigger_parameters is None.", str(ctx.exception))

    def test_temperature_thermocouple_measurement_configuration(self):
        """unit test of TemperatureThermocoupleMeasurementConfiguration."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (250 > 100 characters) (auto-generated noqa)

        # Arrange
        expected_global_channel_parameters = (
            daq.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS
        )

        expected_specific_channels_parameters = []
        expected_specific_channels_parameters.append(
            daq.TemperatureThermocoupleChannelRangeAndTerminalParameters(
                channel_name="Dev/ai0",
                channel_parameters=daq.TemperatureThermocoupleRangeAndTerminalParameters(
                    temperature_minimum_value_celsius_degrees=10.0,
                    temperature_maximum_value_celsius_degrees=89.0,
                    thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
                    cold_junction_compensation_source=nidaqmx.constants.CJCSource.BUILT_IN,
                    cold_junction_compensation_temperature=25.0,
                    cold_junction_compensation_channel_name="",
                    perform_auto_zero_mode=False,
                    auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
                ),
            ),
        )

        expected_specific_channels_parameters.append(
            daq.TemperatureThermocoupleChannelRangeAndTerminalParameters(
                channel_name="Dev/ai1",
                channel_parameters=daq.TemperatureThermocoupleRangeAndTerminalParameters(
                    temperature_minimum_value_celsius_degrees=1.0,
                    temperature_maximum_value_celsius_degrees=79.0,
                    thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
                    cold_junction_compensation_source=nidaqmx.constants.CJCSource.BUILT_IN,
                    cold_junction_compensation_temperature=25.0,
                    cold_junction_compensation_channel_name="",
                    perform_auto_zero_mode=False,
                    auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
                ),
            ),
        )
        expected_specific_channels_parameters.append(
            daq.TemperatureThermocoupleChannelRangeAndTerminalParameters(
                channel_name="Dev/ai2",
                channel_parameters=daq.TemperatureThermocoupleRangeAndTerminalParameters(
                    temperature_minimum_value_celsius_degrees=0.0,
                    temperature_maximum_value_celsius_degrees=100.0,
                    thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
                    cold_junction_compensation_source=nidaqmx.constants.CJCSource.BUILT_IN,
                    cold_junction_compensation_temperature=25.0,
                    cold_junction_compensation_channel_name="",
                    perform_auto_zero_mode=False,
                    auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
                ),
            ),
        )

        expected_sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source="OnboardClock",
            sampling_rate_hertz=100,
            number_of_samples_per_channel=10,
            sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
        )

        expected_measurement_execution_type = nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY

        expected_digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
            digital_start_trigger_source="",
            digital_start_trigger_edge=nidaqmx.constants.Edge.FALLING,
        )

        logging.debug(
            "%s = %s",
            nameof(expected_specific_channels_parameters),
            expected_specific_channels_parameters,
        )

        # Act
        temperature_thermocouple_configuration_instance = (
            daq.TemperatureThermocoupleMeasurementConfiguration(
                global_channel_parameters=expected_global_channel_parameters,
                specific_channels_parameters=expected_specific_channels_parameters,
                measurement_execution_type=expected_measurement_execution_type,
                sample_clock_timing_parameters=expected_sample_clock_timing_parameters,
                digital_start_trigger_parameters=expected_digital_start_trigger_parameters,
            )
        )

        logging.debug(
            "%s = %s",
            nameof(temperature_thermocouple_configuration_instance),
            temperature_thermocouple_configuration_instance,
        )

        # Assert
        self.assertListEqual(
            expected_specific_channels_parameters,
            temperature_thermocouple_configuration_instance.specific_channels_parameters,
        )
        self.assertEqual(
            expected_global_channel_parameters,
            temperature_thermocouple_configuration_instance.global_channel_parameters,
        )
        self.assertEqual(
            expected_measurement_execution_type,
            temperature_thermocouple_configuration_instance.measurement_execution_type,
        )
        self.assertEqual(
            expected_sample_clock_timing_parameters,
            temperature_thermocouple_configuration_instance.sample_clock_timing_parameters,
        )
        self.assertEqual(
            expected_digital_start_trigger_parameters,
            temperature_thermocouple_configuration_instance.digital_start_trigger_parameters,
        )


class TestTemperatureThermocoupleMeasurementTerminalParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `TemperatureThermocoupleMeasurementTerminalParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_temperature_thermocouple_measurement_terminal_parameters_init_fails_if_maximum_is_less_that_minimum(
        self,
    ):
        """unit test of TemperatureThermocoupleMeasurementTerminalParameters."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (255 > 100 characters) (auto-generated noqa)

        # Act

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TemperatureThermocoupleMeasurementTerminalParameters(
                    temperature_minimum_value_celsius_degrees=99.0,
                    temperature_maximum_value_celsius_degrees=1.0,
                    thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
                    cold_junction_compensation_temperature=25.0,
                    perform_auto_zero_mode=False,
                    auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
                )
            )

        # Assert
        self.assertEqual(
            "The value temperature_minimum_value_celsius_degrees must be less than 1.0.",
            str(ctx.exception),
        )

    def test_temperature_thermocouple_measurement_terminal_parameters_fails_if_perform_auto_zero_mode_is_none(
        self,
    ):
        """unit test of TemperatureThermocoupleMeasurementTerminalParameters."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (255 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError):
            print(
                daq.TemperatureThermocoupleMeasurementTerminalParameters(
                    temperature_minimum_value_celsius_degrees=99.0,
                    temperature_maximum_value_celsius_degrees=1.0,
                    thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
                    cold_junction_compensation_temperature=25.0,
                    perform_auto_zero_mode=None,
                    auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
                )
            )

    def test_temperature_thermocouple_measurement_terminal_parameters_fails_if_auto_zero_mode_is_none(
        self,
    ):
        """unit test of TemperatureThermocoupleMeasurementTerminalParameters."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (255 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError):
            print(
                daq.TemperatureThermocoupleMeasurementTerminalParameters(
                    temperature_minimum_value_celsius_degrees=99.0,
                    temperature_maximum_value_celsius_degrees=1.0,
                    thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
                    cold_junction_compensation_temperature=25.0,
                    perform_auto_zero_mode=True,
                    auto_zero_mode=None,
                )
            )

    def test_temperature_thermocouple_measurement_terminal_parameters(self):
        """unit test of TemperatureThermocoupleMeasurementTerminalParameters."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (255 > 100 characters) (auto-generated noqa)

        # Act
        expected_temperature_thermocouple_measurement_terminal_parameters = (
            daq.TemperatureThermocoupleMeasurementTerminalParameters(
                temperature_minimum_value_celsius_degrees=0.0,
                temperature_maximum_value_celsius_degrees=100.0,
                thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
                cold_junction_compensation_temperature=25.0,
                perform_auto_zero_mode=False,
                auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
            )
        )

        # Assert
        self.assertEqual(
            0.0,
            expected_temperature_thermocouple_measurement_terminal_parameters.temperature_minimum_value_celsius_degrees,
        )
        self.assertEqual(
            100.0,
            expected_temperature_thermocouple_measurement_terminal_parameters.temperature_maximum_value_celsius_degrees,
        )
        self.assertEqual(
            nidaqmx.constants.ThermocoupleType.J,
            expected_temperature_thermocouple_measurement_terminal_parameters.thermocouple_type,
        )
        self.assertEqual(
            25.0,
            expected_temperature_thermocouple_measurement_terminal_parameters.cold_junction_compensation_temperature,
        )
        self.assertEqual(
            False,
            expected_temperature_thermocouple_measurement_terminal_parameters.perform_auto_zero_mode,
        )
        self.assertEqual(
            nidaqmx.constants.AutoZeroType.NONE,
            expected_temperature_thermocouple_measurement_terminal_parameters.auto_zero_mode,
        )


class TestTemperatureThermocoupleRangeAndTerminalParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `TemperatureThermocoupleRangeAndTerminalParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_temperature_thermocouple_range_and_terminal_parameters_init_fails_if_maximum_is_less_that_minimum(
        self,
    ):
        """unit test of TemperatureThermocoupleRangeAndTerminalParameters."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (252 > 100 characters) (auto-generated noqa)

        # Act

        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TemperatureThermocoupleRangeAndTerminalParameters(
                    temperature_minimum_value_celsius_degrees=99.0,
                    temperature_maximum_value_celsius_degrees=1.0,
                    thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
                    cold_junction_compensation_source=nidaqmx.constants.CJCSource.BUILT_IN,
                    cold_junction_compensation_temperature=25.0,
                    cold_junction_compensation_channel_name="",
                    perform_auto_zero_mode=False,
                    auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
                )
            )

        # Assert
        self.assertEqual(
            "The value temperature_minimum_value_celsius_degrees must be less than 1.0.",
            str(ctx.exception),
        )

    def test_temperature_thermocouple_range_and_terminal_parameters_fails_if_perform_auto_zero_mode_is_none(
        self,
    ):
        """unit test of TemperatureThermocoupleRangeAndTerminalParameters."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (252 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError):
            print(
                daq.TemperatureThermocoupleRangeAndTerminalParameters(
                    temperature_minimum_value_celsius_degrees=99.0,
                    temperature_maximum_value_celsius_degrees=1.0,
                    thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
                    cold_junction_compensation_source=nidaqmx.constants.CJCSource.BUILT_IN,
                    cold_junction_compensation_temperature=25.0,
                    cold_junction_compensation_channel_name="",
                    perform_auto_zero_mode=None,
                    auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
                )
            )

    def test_temperature_thermocouple_range_and_terminal_parameters_fails_if_auto_zero_mode_is_none(
        self,
    ):
        """unit test of TemperatureThermocoupleRangeAndTerminalParameters."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (252 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError):
            print(
                daq.TemperatureThermocoupleRangeAndTerminalParameters(
                    temperature_minimum_value_celsius_degrees=99.0,
                    temperature_maximum_value_celsius_degrees=1.0,
                    thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
                    cold_junction_compensation_source=nidaqmx.constants.CJCSource.BUILT_IN,
                    cold_junction_compensation_temperature=25.0,
                    cold_junction_compensation_channel_name="",
                    perform_auto_zero_mode=True,
                    auto_zero_mode=None,
                )
            )

    def test_temperature_thermocouple_range_and_terminal_parameters(self):
        """unit test of TemperatureThermocoupleRangeAndTerminalParameters."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (252 > 100 characters) (auto-generated noqa)

        # Act
        expected_temperature_thermocouple_range_and_terminal_parameters = (
            daq.TemperatureThermocoupleRangeAndTerminalParameters(
                temperature_minimum_value_celsius_degrees=0.0,
                temperature_maximum_value_celsius_degrees=100.0,
                thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
                cold_junction_compensation_source=nidaqmx.constants.CJCSource.BUILT_IN,
                cold_junction_compensation_temperature=25.0,
                cold_junction_compensation_channel_name="",
                perform_auto_zero_mode=False,
                auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
            )
        )

        # Assert
        self.assertEqual(
            0.0,
            expected_temperature_thermocouple_range_and_terminal_parameters.temperature_minimum_value_celsius_degrees,
        )
        self.assertEqual(
            100.0,
            expected_temperature_thermocouple_range_and_terminal_parameters.temperature_maximum_value_celsius_degrees,
        )
        self.assertEqual(
            nidaqmx.constants.ThermocoupleType.J,
            expected_temperature_thermocouple_range_and_terminal_parameters.thermocouple_type,
        )
        self.assertEqual(
            nidaqmx.constants.CJCSource.BUILT_IN,
            expected_temperature_thermocouple_range_and_terminal_parameters.cold_junction_compensation_source,
        )
        self.assertEqual(
            25.0,
            expected_temperature_thermocouple_range_and_terminal_parameters.cold_junction_compensation_temperature,
        )
        self.assertEqual(
            "",
            expected_temperature_thermocouple_range_and_terminal_parameters.cold_junction_compensation_channel_name,
        )
        self.assertEqual(
            False,
            expected_temperature_thermocouple_range_and_terminal_parameters.perform_auto_zero_mode,
        )
        self.assertEqual(
            nidaqmx.constants.AutoZeroType.NONE,
            expected_temperature_thermocouple_range_and_terminal_parameters.auto_zero_mode,
        )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/temperature_measurements/test_temperature_measurement_using_rtd.py sha256=0f04aecd1e1a5a64d21788df5bd3742ac1943b6e1789b48ce0ab3ff6d14d4874 bytes=3404 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/temperature_measurements/test_temperature_measurement_using_rtd.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/temperature_measurements/test_temperature_measurement_using_rtd.py`
- sha256: `0f04aecd1e1a5a64d21788df5bd3742ac1943b6e1789b48ce0ab3ff6d14d4874`
- bytes: 3404

````python
"""This module provides TemperatureMeasurementUsingRtd check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_interpreters import (
    _InterpreterDcRmsVoltageMeasurement,
)
from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx,
)


class TestTemperatureMeasurementUsingRtd(unittest.TestCase):
    """Defines a test fixture that checks
    `TemperatureMeasurementUsingRtd` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)
        _replace_daqmx(_InterpreterDcRmsVoltageMeasurement)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_temperature_measurement_using_rtd(self):
        """Checks if class TemperatureMeasurementUsingRtd is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (187 > 100 characters) (auto-generated noqa)
        measurement = nipcbatt.daq.TemperatureMeasurementUsingRtd()
        measurement.initialize(channel_expression="Dev/ai0")

        # Create a custom configuration with CONFIGURE_ONLY to avoid mock limitations
        from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
        from nipcbatt.pcbatt_library.daq.temperature_measurements.temperature_data_types import (
            TemperatureRtdMeasurementConfiguration,
        )
        from nipcbatt.pcbatt_library.daq.temperature_measurements.temperature_constants import (
            DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS,
            DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS,
            DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS,
        )

        configure_only_configuration = TemperatureRtdMeasurementConfiguration(
            global_channel_parameters=DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS,
            specific_channels_parameters=[],
            measurement_execution_type=MeasurementExecutionType.CONFIGURE_ONLY,
            sample_clock_timing_parameters=DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS,
            digital_start_trigger_parameters=DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS,
        )

        measurement.configure_and_measure(configuration=configure_only_configuration)

        measurement.close()


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/temperature_measurements/test_temperature_measurement_using_thermistor.py sha256=3dfd3d0907663fd04fda386552eb4788ed0ed90a86d79486bee5b3eb845845ae bytes=2375 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/temperature_measurements/test_temperature_measurement_using_thermistor.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/temperature_measurements/test_temperature_measurement_using_thermistor.py`
- sha256: `3dfd3d0907663fd04fda386552eb4788ed0ed90a86d79486bee5b3eb845845ae`
- bytes: 2375

````python
"""This module provides TemperatureMeasurementUsingThermistor check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_interpreters import (
    _InterpreterDcRmsVoltageMeasurement,
)
from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx,
)


class TestTemperatureMeasurementUsingThermistor(unittest.TestCase):
    """Defines a test fixture that checks
    `TemperatureMeasurementUsingThermistor` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)
        _replace_daqmx(_InterpreterDcRmsVoltageMeasurement)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_temperature_measurement_using_thermistor(self):
        """Checks if class TemperatureMeasurementUsingThermistor is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (194 > 100 characters) (auto-generated noqa)
        measurement = nipcbatt.daq.TemperatureMeasurementUsingThermistor()
        measurement.initialize(channel_expression="Dev/ai0")

        results = measurement.configure_and_measure(
            configuration=nipcbatt.daq.DEFAULT_TEMPERATURE_THERMISTOR_MEASUREMENT_CONFIGURATION
        )
        print(results)

        measurement.close()


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/temperature_measurements/test_temperature_measurement_using_thermocouple.py sha256=28b48043ea95b6759ae555538e37df29e6b3d694ade08b33e05d4917b35200dc bytes=2307 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/temperature_measurements/test_temperature_measurement_using_thermocouple.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/temperature_measurements/test_temperature_measurement_using_thermocouple.py`
- sha256: `28b48043ea95b6759ae555538e37df29e6b3d694ade08b33e05d4917b35200dc`
- bytes: 2307

````python
"""This module provides TemperatureMeasurementUsingThermocouple check."""

import importlib.metadata
import logging
import sys
import unittest

import nidaqmx.constants
from varname import nameof

import nipcbatt
from nipcbatt import daq


class TestTemperatureMeasurementUsingThermocouple(unittest.TestCase):
    """Defines a test fixture that checks
    `TemperatureMeasurementUsingThermocouple` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_temperature_measurement_using_thermocouple(self):
        """Checks if class TemperatureMeasurementUsingThermocouple is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (196 > 100 characters) (auto-generated noqa)
        measurement = daq.TemperatureMeasurementUsingThermocouple()
        measurement.initialize(
            channel_expression="Sim_PXIeDAQ/ai0",
            cold_junction_compensation_source=nidaqmx.constants.CJCSource.CONSTANT_USER_VALUE,
            cold_junction_compensation_channel="",
        )

        results = measurement.configure_and_measure(
            configuration=daq.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_CONFIGURATION
        )
        print(results)

        measurement.close()


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/time_domain_measurements/__init__.py sha256=af761066ea221dbab099166d3b31532dfdcf87b400be54af38b43fda1b99504c bytes=465 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/time_domain_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/time_domain_measurements/__init__.py`
- sha256: `af761066ea221dbab099166d3b31532dfdcf87b400be54af38b43fda1b99504c`
- bytes: 465

````python
"""Provides a set of unit tests for 
   nipcbatt.pcbatt_library.time_domain_measurements package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (355 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/time_domain_measurements/test_time_domain_data_types.py sha256=3aded99617f81457f0187400d6063e6a5d994abb82d1ad72bde402ba9f57c3bc bytes=50062 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/time_domain_measurements/test_time_domain_data_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/time_domain_measurements/test_time_domain_data_types.py`
- sha256: `3aded99617f81457f0187400d6063e6a5d994abb82d1ad72bde402ba9f57c3bc`
- bytes: 50062

````python
# pylint: disable=C0301
"""This module provides time domain data types check."""

import importlib.metadata
import logging
import random
import sys
import unittest

import nidaqmx.constants
import numpy
from varname import nameof

import nipcbatt
from nipcbatt import daq


class TestTimeDomainMeasurementConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    `TimeDomainMeasurementConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_time_domain_measurement_configuration_init_fails_when_global_channel_parameters_is_none(
        self,
    ):
        """unit test of TimeDomainMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (160 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TimeDomainMeasurementConfiguration(
                    global_channel_parameters=None,
                    specific_channels_parameters=[],
                    measurement_options=daq.DEFAULT_TIME_DOMAIN_MEASUREMENT_OPTIONS,
                    sample_clock_timing_parameters=daq.DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS,
                    digital_start_trigger_parameters=daq.DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS,
                )
            )

        # Assert
        self.assertEqual("The object global_channel_parameters is None.", str(ctx.exception))

    def test_time_domain_measurement_configuration_init_fails_when_specific_channels_parameters_is_none(
        self,
    ):
        """unit test of TimeDomainMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (160 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TimeDomainMeasurementConfiguration(
                    global_channel_parameters=daq.DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS,
                    specific_channels_parameters=None,
                    measurement_options=daq.DEFAULT_TIME_DOMAIN_MEASUREMENT_OPTIONS,
                    sample_clock_timing_parameters=daq.DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS,
                    digital_start_trigger_parameters=daq.DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS,
                )
            )

        # Assert
        self.assertEqual("The object specific_channels_parameters is None.", str(ctx.exception))

    def test_time_domain_measurement_configuration_init_fails_when_measurement_options_is_none(
        self,
    ):
        """unit test of TimeDomainMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (160 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TimeDomainMeasurementConfiguration(
                    global_channel_parameters=daq.DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS,
                    specific_channels_parameters=[],
                    measurement_options=None,
                    sample_clock_timing_parameters=daq.DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS,
                    digital_start_trigger_parameters=daq.DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS,
                )
            )

        # Assert
        self.assertEqual("The object measurement_options is None.", str(ctx.exception))

    def test_time_domain_measurement_configuration_init_fails_when_sample_clock_timing_parameters_is_none(
        self,
    ):
        """unit test of TimeDomainMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (160 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TimeDomainMeasurementConfiguration(
                    global_channel_parameters=daq.DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS,
                    specific_channels_parameters=[],
                    measurement_options=daq.DEFAULT_TIME_DOMAIN_MEASUREMENT_OPTIONS,
                    sample_clock_timing_parameters=None,
                    digital_start_trigger_parameters=daq.DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS,
                )
            )

        # Assert
        self.assertEqual("The object sample_clock_timing_parameters is None.", str(ctx.exception))

    def test_time_domain_measurement_configuration_init_fails_when_digital_start_trigger_parameters_is_none(
        self,
    ):
        """unit test of TimeDomainMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (160 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TimeDomainMeasurementConfiguration(
                    global_channel_parameters=daq.DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS,
                    specific_channels_parameters=[],
                    measurement_options=daq.DEFAULT_TIME_DOMAIN_MEASUREMENT_OPTIONS,
                    sample_clock_timing_parameters=daq.DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS,
                    digital_start_trigger_parameters=None,
                )
            )

        # Assert
        self.assertEqual("The object digital_start_trigger_parameters is None.", str(ctx.exception))

    def test_time_domain_measurement_configuration(self):
        """unit test of TimeDomainMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (160 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_terminal_configuration = nidaqmx.constants.TerminalConfiguration.NRSE
        expected_range_min_volts = -9.0
        expected_range_max_volts = 6.3
        expected_specific_terminal_configuration = nidaqmx.constants.TerminalConfiguration.DIFF
        expected_specific_range_min_volts = -5.0
        expected_specific_range_max_volts = 7.5

        global_channel_parameters = daq.VoltageRangeAndTerminalParameters(
            terminal_configuration=expected_terminal_configuration,
            range_min_volts=expected_range_min_volts,
            range_max_volts=expected_range_max_volts,
        )

        expected_execution_option = nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE
        expected_measurement_analysis_requirement = (
            nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
        )

        measurement_options = nipcbatt.MeasurementOptions(
            execution_option=expected_execution_option,
            measurement_analysis_requirement=expected_measurement_analysis_requirement,
        )

        specific_channels_parameters = []
        specific_channels_parameters.append(
            daq.VoltageMeasurementChannelAndTerminalRangeParameters(
                channel_name="Dev/ai0",
                channel_parameters=daq.VoltageRangeAndTerminalParameters(
                    terminal_configuration=expected_specific_terminal_configuration,
                    range_min_volts=expected_specific_range_min_volts,
                    range_max_volts=expected_specific_range_max_volts,
                ),
            )
        )
        specific_channels_parameters.append(
            daq.VoltageMeasurementChannelAndTerminalRangeParameters(
                channel_name="Dev/ai1",
                channel_parameters=daq.VoltageRangeAndTerminalParameters(
                    terminal_configuration=expected_specific_terminal_configuration,
                    range_min_volts=expected_specific_range_min_volts,
                    range_max_volts=expected_specific_range_max_volts,
                ),
            )
        )
        specific_channels_parameters.append(
            daq.VoltageMeasurementChannelAndTerminalRangeParameters(
                channel_name="Dev/ai2",
                channel_parameters=daq.VoltageRangeAndTerminalParameters(
                    terminal_configuration=expected_specific_terminal_configuration,
                    range_min_volts=expected_specific_range_min_volts,
                    range_max_volts=expected_specific_range_max_volts,
                ),
            )
        )

        expected_sample_clock_source = "OnboardClock"
        expected_sampling_rate_hertz = 10000
        expected_number_of_samples_per_channel = 1500
        expected_sample_timing_engine = nipcbatt.SampleTimingEngine.TE1

        sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source=expected_sample_clock_source,
            sampling_rate_hertz=expected_sampling_rate_hertz,
            number_of_samples_per_channel=expected_number_of_samples_per_channel,
            sample_timing_engine=expected_sample_timing_engine,
        )

        expected_trigger_select = nipcbatt.StartTriggerType.DIGITAL_TRIGGER
        expected_digital_start_trigger_source = "trigger_source"
        expected_digital_start_trigger_edge = nidaqmx.constants.Edge.FALLING

        digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=expected_trigger_select,
            digital_start_trigger_source=expected_digital_start_trigger_source,
            digital_start_trigger_edge=expected_digital_start_trigger_edge,
        )

        logging.debug(
            "%s = %s",
            nameof(specific_channels_parameters),
            specific_channels_parameters,
        )

        # Act
        dc_rms_configuration_instance = daq.TimeDomainMeasurementConfiguration(
            global_channel_parameters=global_channel_parameters,
            specific_channels_parameters=specific_channels_parameters,
            measurement_options=measurement_options,
            sample_clock_timing_parameters=sample_clock_timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        logging.debug(
            "%s = %s",
            nameof(dc_rms_configuration_instance),
            dc_rms_configuration_instance,
        )

        # Assert
        self.assertListEqual(
            specific_channels_parameters,
            dc_rms_configuration_instance.specific_channels_parameters,
        )

        actual_terminal_configuration = (
            dc_rms_configuration_instance.global_channel_parameters.terminal_configuration
        )
        actual_range_min_volts = (
            dc_rms_configuration_instance.global_channel_parameters.range_min_volts
        )
        actual_range_max_volts = (
            dc_rms_configuration_instance.global_channel_parameters.range_max_volts
        )

        actual_execution_option = dc_rms_configuration_instance.measurement_options.execution_option
        actual_measurement_analysis_requirement = (
            dc_rms_configuration_instance.measurement_options.measurement_analysis_requirement
        )
        actual_sample_clock_source = (
            dc_rms_configuration_instance.sample_clock_timing_parameters.sample_clock_source
        )
        actual_sampling_rate_hertz = (
            dc_rms_configuration_instance.sample_clock_timing_parameters.sampling_rate_hertz
        )
        actual_number_of_samples_per_channel = (
            dc_rms_configuration_instance.sample_clock_timing_parameters.number_of_samples_per_channel
        )
        actual_sample_timing_engine = (
            dc_rms_configuration_instance.sample_clock_timing_parameters.sample_timing_engine
        )

        self.assertEqual(expected_terminal_configuration, actual_terminal_configuration)
        self.assertEqual(expected_range_min_volts, actual_range_min_volts)
        self.assertEqual(expected_range_max_volts, actual_range_max_volts)

        self.assertEqual(expected_execution_option, actual_execution_option)
        self.assertEqual(
            expected_measurement_analysis_requirement,
            actual_measurement_analysis_requirement,
        )
        self.assertEqual(expected_sample_clock_source, actual_sample_clock_source)
        self.assertEqual(expected_sampling_rate_hertz, actual_sampling_rate_hertz)
        self.assertEqual(
            expected_number_of_samples_per_channel, actual_number_of_samples_per_channel
        )
        self.assertEqual(
            expected_sample_timing_engine,
            actual_sample_timing_engine,
        )


class TestTimeDomainMeasurementResultData(unittest.TestCase):
    """Defines a test fixture that checks
    `TimeDomainMeasurementResultData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self,
        methodName: str = "runTest",  # noqa: N803 - argument name 'methodName' should be lowercase (auto-generated noqa)
    ) -> None:
        super().__init__(methodName)
        self._expected_waveforms = None

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_time_domain_measurement_result_data_init_fails_when_waveforms_is_none(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TimeDomainMeasurementResultData(
                    waveforms=None,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
                    vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual("The object waveforms is None.", str(ctx.exception))

    def test_time_domain_measurement_result_data_init_fails_when_waveforms_is_empty(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TimeDomainMeasurementResultData(
                    waveforms=[],
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
                    vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual("The iterable waveforms of type list is empty.", str(ctx.exception))

    def test_time_domain_measurement_result_data_init_fails_when_waveforms_contains_object_that_are_not_of_analog_waveform(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                daq.TimeDomainMeasurementResultData(
                    waveforms=[2.0],
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
                    vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (AnalogWaveform).",
            str(ctx.exception),
        )

    def test_time_domain_measurement_result_data_init_fails_when_mean_dc_voltage_values_volts_is_none(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (238 > 100 characters) (auto-generated noqa)

        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                daq.TimeDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=None,
                    vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual("object of type 'NoneType' has no len()", str(ctx.exception))

    def test_time_domain_measurement_result_data_init_fails_when_mean_dc_voltage_values_volts_is_empty(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TimeDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=[],
                    vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual(
            "The iterable mean_dc_voltage_values_volts of type list is empty.",
            str(ctx.exception),
        )

    def test_time_domain_measurement_result_data_init_fails_when_mean_dc_voltage_values_volts_contains_object_that_are_not_of_float(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                daq.TimeDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=["1.0", 1.0, 1.0],
                    vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (float).",
            str(ctx.exception),
        )

    def test_time_domain_measurement_result_data_init_fails_when_vpp_amplitudes_volts_is_none(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TimeDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
                    vpp_amplitudes_volts=None,
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual("The object vpp_amplitudes_volts is None.", str(ctx.exception))

    def test_time_domain_measurement_result_data_init_fails_when_vpp_amplitudes_volts_is_empty(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TimeDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
                    vpp_amplitudes_volts=[],
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual(
            "The iterable vpp_amplitudes_volts of type list is empty.",
            str(ctx.exception),
        )

    def test_time_domain_measurement_result_data_init_fails_when_vpp_amplitudes_volts_contains_object_that_are_not_of_float(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                daq.TimeDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
                    vpp_amplitudes_volts=["1.0", 1.0, 1.0],
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (float).",
            str(ctx.exception),
        )

    def test_time_domain_measurement_result_data_init_fails_when_voltage_waveforms_frequencies_hertz_is_none(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TimeDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
                    vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
                    voltage_waveforms_frequencies_hertz=None,
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual(
            "The object voltage_waveforms_frequencies_hertz is None.",
            str(ctx.exception),
        )

    def test_time_domain_measurement_result_data_init_does_not_fail_when_voltage_waveforms_frequencies_hertz_is_empty(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        time_domain_result = daq.TimeDomainMeasurementResultData(
            waveforms=self._expected_waveforms,
            acquisition_duration_seconds=expected_acquisition_duration_seconds,
            mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
            vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
            voltage_waveforms_frequencies_hertz=[],
            voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
            voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
        )

        # Assert
        self.assertIsNotNone(time_domain_result.voltage_waveforms_periods_seconds)
        self.assertIsNotNone(time_domain_result.voltage_waveforms_frequencies_hertz)
        self.assertFalse(time_domain_result.voltage_waveforms_frequencies_hertz)
        self.assertIsNotNone(time_domain_result.voltage_waveforms_duty_cycles_percent)

    def test_time_domain_measurement_result_data_init_fails_when_voltage_waveforms_frequencies_hertz_contains_object_that_are_not_of_float(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                daq.TimeDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
                    vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
                    voltage_waveforms_frequencies_hertz=[1.0, "1.0", 1.0],
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (float).",
            str(ctx.exception),
        )

    def test_time_domain_measurement_result_data_init_fails_when_voltage_waveforms_periods_seconds_is_none(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TimeDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
                    vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=None,
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual(
            "The object voltage_waveforms_periods_seconds is None.",
            str(ctx.exception),
        )

    def test_time_domain_measurement_result_data_init_does_not_fail_when_voltage_waveforms_periods_seconds_is_empty(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        time_domain_result = daq.TimeDomainMeasurementResultData(
            waveforms=self._expected_waveforms,
            acquisition_duration_seconds=expected_acquisition_duration_seconds,
            mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
            vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
            voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
            voltage_waveforms_periods_seconds=[],
            voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
        )

        # Assert
        self.assertIsNotNone(time_domain_result.voltage_waveforms_periods_seconds)
        self.assertFalse(time_domain_result.voltage_waveforms_periods_seconds)
        self.assertIsNotNone(time_domain_result.voltage_waveforms_frequencies_hertz)
        self.assertIsNotNone(time_domain_result.voltage_waveforms_duty_cycles_percent)

    def test_time_domain_measurement_result_data_init_fails_when_voltage_waveforms_periods_seconds_contains_object_that_are_not_of_float(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                daq.TimeDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
                    vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=[0.01, 0.01, "0.01"],
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (float).",
            str(ctx.exception),
        )

    def test_time_domain_measurement_result_data_init_fails_when_voltage_waveforms_duty_cycles_percent_is_none(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                daq.TimeDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
                    vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=None,
                )
            )

        # Assert
        self.assertEqual(
            "The object voltage_waveforms_duty_cycles_percent is None.",
            str(ctx.exception),
        )

    def test_time_domain_measurement_result_data_init_does_not_fail_when_voltage_waveforms_duty_cycles_percent_is_empty(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]

        # Act
        time_domain_result = daq.TimeDomainMeasurementResultData(
            waveforms=self._expected_waveforms,
            acquisition_duration_seconds=expected_acquisition_duration_seconds,
            mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
            vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
            voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
            voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
            voltage_waveforms_duty_cycles_percent=[],
        )

        # Assert
        self.assertIsNotNone(time_domain_result.voltage_waveforms_periods_seconds)
        self.assertIsNotNone(time_domain_result.voltage_waveforms_frequencies_hertz)
        self.assertIsNotNone(time_domain_result.voltage_waveforms_duty_cycles_percent)
        self.assertFalse(time_domain_result.voltage_waveforms_duty_cycles_percent)

    def test_time_domain_measurement_result_data_init_fails_when_voltage_waveforms_duty_cycles_percent_contains_object_that_are_not_of_float(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                daq.TimeDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
                    vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=[0.5, "0.5", 0.5],
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (float).",
            str(ctx.exception),
        )

    def test_time_domain_measurement_result_data(self):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3

        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]
        instance = daq.TimeDomainMeasurementResultData(
            waveforms=self._expected_waveforms,
            acquisition_duration_seconds=expected_acquisition_duration_seconds,
            mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
            vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
            voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
            voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
            voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
        )

        logging.debug("%s = %s", nameof(instance), instance)

        actual_waveforms = instance.waveforms
        actual_acquisition_duration_seconds = instance.acquisition_duration_seconds
        actual_mean_dc_voltage_values_volts = instance.mean_dc_voltage_values_volts
        actual_vpp_amplitudes_volts = instance.vpp_amplitudes_volts
        actual_voltage_waveforms_frequencies_hertz = instance.voltage_waveforms_frequencies_hertz
        actual_voltage_waveforms_periods_seconds = instance.voltage_waveforms_periods_seconds
        actual_voltage_waveforms_duty_cycles_percent = (
            instance.voltage_waveforms_duty_cycles_percent
        )

        self.assertListEqual(self._expected_waveforms, actual_waveforms)
        self.assertEqual(expected_acquisition_duration_seconds, actual_acquisition_duration_seconds)
        self.assertListEqual(
            expected_mean_dc_voltage_values_volts, actual_mean_dc_voltage_values_volts
        )
        self.assertListEqual(expected_vpp_amplitudes_volts, actual_vpp_amplitudes_volts)
        self.assertListEqual(
            expected_voltage_waveforms_frequencies_hertz,
            actual_voltage_waveforms_frequencies_hertz,
        )
        self.assertListEqual(
            expected_voltage_waveforms_periods_seconds,
            actual_voltage_waveforms_periods_seconds,
        )
        self.assertListEqual(
            expected_voltage_waveforms_duty_cycles_percent,
            actual_voltage_waveforms_duty_cycles_percent,
        )

    def _initialize_waveforms(self):
        self._expected_waveforms = []
        self._expected_waveforms.append(
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai0",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.ones(shape=(1000), dtype=numpy.float64),
            )
        )
        self._expected_waveforms.append(
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai1",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.array(
                    [random.random() * 0.1 for item in range(0, 1000)],
                    dtype=numpy.float64,
                ),
            )
        )
        self._expected_waveforms.append(
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai2",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.array(
                    [random.random() * 0.1 for item in range(0, 1000)],
                    dtype=numpy.float64,
                ),
            )
        )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_tests/time_domain_measurements/test_time_domain_measurement.py sha256=abb14d779a48e656041a6983952b2c1e8b199c066256174c89f5a73d99b8d1ee bytes=2359 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_tests/time_domain_measurements/test_time_domain_measurement.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_tests/time_domain_measurements/test_time_domain_measurement.py`
- sha256: `abb14d779a48e656041a6983952b2c1e8b199c066256174c89f5a73d99b8d1ee`
- bytes: 2359

````python
"""This module provides TimeDomainMeasurement check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_interpreters import (
    _InterpreterDcRmsVoltageMeasurement,
)
from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx,
)


class TestTimeDomainMeasurement(unittest.TestCase):
    """Defines a test fixture that checks
    `TimeDomainMeasurement` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)
        _replace_daqmx(_InterpreterDcRmsVoltageMeasurement)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_time_domain_measurement(self):
        """Checks if class TimeDomainMeasurement is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (178 > 100 characters) (auto-generated noqa)
        with nipcbatt.daq.TimeDomainMeasurement() as measurement:
            measurement.initialize(
                analog_input_channel_expression=(
                    "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0"
                )
            )

            measurement.configure_and_measure(
                configuration=nipcbatt.daq.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION
            )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_utilities_tests/__init__.py sha256=fb71edab48af304bd48836e98e40c271757e97acbfc0309ba73643af992abdd9 bytes=255 -->
## FILE: tests/nipcbatt_tests/pcbatt_utilities_tests/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_utilities_tests/__init__.py`
- sha256: `fb71edab48af304bd48836e98e40c271757e97acbfc0309ba73643af992abdd9`
- bytes: 255

````python
"""Provides a set of unit tests for nipcbatt.pcbatt_utilities package"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (183 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_utilities_tests/test_csv_utilities.py sha256=e51b636bb0162cf789da7f5bfa147a8395c52ce405242428db0b6295b3579a82 bytes=5813 -->
## FILE: tests/nipcbatt_tests/pcbatt_utilities_tests/test_csv_utilities.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_utilities_tests/test_csv_utilities.py`
- sha256: `e51b636bb0162cf789da7f5bfa147a8395c52ce405242428db0b6295b3579a82`
- bytes: 5813

````python
"""Provides unit tests related to functional_utilities.py module"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (178 > 100 characters) (auto-generated noqa)

import logging
import os
import platform
import sys
import unittest
from pathlib import Path

from varname import nameof

from nipcbatt.pcbatt_utilities import (
    csv_utilities,
    file_utilities,
    functional_utilities,
)


class TestCsvUtilities(unittest.TestCase):
    """Defines a test fixture that checks function of module
    `pcbatt_utilities.csv_utilities`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        self.counter = 0

    def tearDown(self):
        self.counter = 0

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

        repository_dir_path = Path(__file__).parent.parent.parent.parent
        cls.tests_output_folder_path = os.path.join(
            repository_dir_path,
            "tests_outputs",
            Path(__file__).stem,
            nameof(TestCsvUtilities),
        )

        if not os.path.exists(cls.tests_output_folder_path):
            os.makedirs(cls.tests_output_folder_path, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_export_signal_to_csv_file(self):
        """Unit test of csv_utilities.export_signal_to_csv_file"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (177 > 100 characters) (auto-generated noqa)
        # Arrange
        signal_samples = [1, 4, 9, 16]
        csv_file_ouput_path = os.path.join(
            TestCsvUtilities.tests_output_folder_path,
            "test_export_signal_to_csv_file.csv",
        )

        # Act
        csv_utilities.export_signal_to_csv_file(
            signal_csv_file_path=csv_file_ouput_path,
            signal_samples=signal_samples,
            signal_sampling_rate=1,
            x_axis_name="Time (s)",
            y_axis_name="Amplitude (V)",
        )

        # Assert
        self.assertTrue(os.path.exists(path=csv_file_ouput_path))
        csv_lines_list = list(file_utilities.read_lines(csv_file_ouput_path, "utf8"))

        logging.debug("%s = %s", nameof(csv_lines_list), csv_lines_list)
        self.assertEqual(first=1 + len(signal_samples), second=len(csv_lines_list))

    @functional_utilities.repeat(2)
    def test_export_columns_to_csv_file(self):
        """Unit test of csv_utilities.export_to_csv_file_columns"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (178 > 100 characters) (auto-generated noqa)
        # Arrange
        x_samples = [1, 2, 3, 4]
        y_samples = [1, 4, 9, 16]
        csv_file_ouput_path = os.path.join(
            TestCsvUtilities.tests_output_folder_path,
            "test_export_columns_to_csv_file.csv",
        )

        # Act
        csv_utilities.export_columns_to_csv_file(
            csv_file_path=csv_file_ouput_path,
            column1_data=x_samples,
            column2_data=y_samples,
            column1_name="X",
            column2_name="X^2",
        )

        # Assert
        self.assertTrue(os.path.exists(path=csv_file_ouput_path))

    @functional_utilities.repeat(2)
    def test_import_from_csv_file_2d_array(self):
        """Unit test of csv_utilities.import_from_csv_file_2d_array"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (258 > 100 characters) (auto-generated noqa)

        # Arrange
        expected_csv_lines_count = 14001
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent

        logging.debug("%s = %s", nameof(repository_dir_path), repository_dir_path)

        emv_csv_file_path = os.path.join(
            repository_dir_path, "pcbatt.testdata", "EMV_Waveform_TA121.csv"
        )
        logging.debug("%s = %s", nameof(emv_csv_file_path), emv_csv_file_path)

        # Act
        (column_1_array, column_2_array) = csv_utilities.import_from_csv_file_2d_array(
            csv_file_path=emv_csv_file_path, header_is_present=False
        )
        logging.debug(
            "%s[%s] = %s",
            nameof(column_1_array),
            "Time (s)",
            column_1_array,
        )

        logging.debug(
            "%s[%s] = %s",
            nameof(column_2_array),
            "Ampltiude (V)",
            column_2_array,
        )

        # Assert
        self.assertIsNotNone(column_1_array)
        self.assertIsNotNone(column_2_array)

        self.assertEqual(first=expected_csv_lines_count, second=column_1_array.size)
        self.assertEqual(first=expected_csv_lines_count, second=column_2_array.size)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_utilities_tests/test_file_utilities.py sha256=71738f73e59c8f4820812a755c212d0d0e46b21fb047e08600dd570aaec71c66 bytes=4679 -->
## FILE: tests/nipcbatt_tests/pcbatt_utilities_tests/test_file_utilities.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_utilities_tests/test_file_utilities.py`
- sha256: `71738f73e59c8f4820812a755c212d0d0e46b21fb047e08600dd570aaec71c66`
- bytes: 4679

````python
"""Provides unit tests related to file_utilities.py module"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (172 > 100 characters) (auto-generated noqa)

import logging
import os
import platform
import sys
import unittest
from pathlib import Path

from parameterized import parameterized
from varname import nameof

from nipcbatt.pcbatt_utilities import (
    file_utilities,
    functional_utilities,
    iterable_utilities,
)


class TestFileUtilities(unittest.TestCase):
    """Defines a test fixture that checks function of module
    `pcbatt_utilities.file_utilities`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

        repository_dir_path = Path(__file__).parent.parent.parent.parent
        cls.tests_output_folder_path = os.path.join(
            repository_dir_path,
            "tests_outputs",
            Path(__file__).stem,
            nameof(TestFileUtilities),
        )

        if not os.path.exists(cls.tests_output_folder_path):
            os.makedirs(cls.tests_output_folder_path, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    @functional_utilities.repeat(2)
    def test_write_lines(self):
        """Unit test of file_utilities.write_lines"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (164 > 100 characters) (auto-generated noqa)
        # Arrange
        file_output_path = os.path.join(
            TestFileUtilities.tests_output_folder_path,
            "test_write_lines.txt",
        )
        file_lines = ["a", "b", "c"]

        # Act
        file_utilities.write_lines(
            text_file_path=file_output_path,
            text_file_encoding="utf8",
            text_lines=file_lines,
        )

        # Assert
        self.assertTrue(os.path.exists(path=file_output_path))

    @functional_utilities.repeat(2)
    def test_read_lines(self):
        """Unit test of file_utilities.read_lines"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (163 > 100 characters) (auto-generated noqa)
        # Arrange
        file_input_path = os.path.join(
            TestFileUtilities.tests_output_folder_path,
            "test_read_lines.txt",
        )

        file_lines = ["a", "b", "c"]

        file_utilities.write_lines(
            text_file_path=file_input_path,
            text_file_encoding="utf8",
            text_lines=file_lines,
        )

        # Act
        read_lines = file_utilities.read_lines(
            text_file_path=file_input_path, text_file_encoding="utf8"
        )

        count, iterable_reset = iterable_utilities.count(read_lines)
        # Assert
        self.assertIsNotNone(read_lines)
        self.assertEqual(first=3, second=count)

        read_lines_list = list(iterable_reset)
        self.assertEqual(first=3, second=len(read_lines_list))
        self.assertEqual(first="a", second=read_lines_list[0])
        self.assertEqual(first="b", second=read_lines_list[1])
        self.assertEqual(first="c", second=read_lines_list[2])

    @parameterized.expand([("C:/windows/explorer.exe"), ("C:/windows/system32/kernel32.dll")])
    def test_file_exists_should_not_fail(self, file_path: str):
        """Unit test of nipcbatt.pcbatt_utilities.file_utilities.file_exists"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (267 > 100 characters) (auto-generated noqa)

        self.assertTrue(file_utilities.file_exists(file_path))


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_utilities_tests/test_functional_utilities.py sha256=9140aaa6e16c0bce40b908032a89862bd5730743f78e983771e9899a31f4782f bytes=2010 -->
## FILE: tests/nipcbatt_tests/pcbatt_utilities_tests/test_functional_utilities.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_utilities_tests/test_functional_utilities.py`
- sha256: `9140aaa6e16c0bce40b908032a89862bd5730743f78e983771e9899a31f4782f`
- bytes: 2010

````python
"""Provides unit tests related to functional_utilities.py module"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (178 > 100 characters) (auto-generated noqa)

import logging
import platform
import sys
import unittest

from nipcbatt.pcbatt_utilities import functional_utilities


class TestFunctionalUtilities(unittest.TestCase):
    """Defines a test fixture that checks function of module
    `pcbatt_utilities.functional_utilities`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        self.counter = 0

    def tearDown(self):
        self.counter = 0

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_repeat(self):
        """Unit test of functional_utilities.repeat"""  # noqa: D415, W505, D202 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)

        @functional_utilities.repeat(10)
        def increment():
            self.counter = 1 + self.counter

        increment()
        self.assertEqual(10, self.counter)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_utilities_tests/test_guard_utilities.py sha256=d357d8da96de21f7ad07768d107f765e2ecc0d797373e9a46229e4dc2e087a0c bytes=32357 -->
## FILE: tests/nipcbatt_tests/pcbatt_utilities_tests/test_guard_utilities.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_utilities_tests/test_guard_utilities.py`
- sha256: `d357d8da96de21f7ad07768d107f765e2ecc0d797373e9a46229e4dc2e087a0c`
- bytes: 32357

````python
"""Provides unit tests related to guard_utilities.py module"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

import logging
import platform
import sys
import unittest

from varname import nameof

from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class TestGuard(unittest.TestCase):
    """Defines a test fixture that checks function of module
    `nipcbatt.pcbatt_utilities.guard_utilities.Guard`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_is_not_empty_fails_if_iterable_empty(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_not_empty"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (198 > 100 characters) (auto-generated noqa)
        empty_tuple = ()

        with self.assertRaises(ValueError) as ctx:
            Guard.is_not_empty(empty_tuple, nameof(empty_tuple))

        self.assertEqual("The iterable empty_tuple of type tuple is empty.", str(ctx.exception))

    def test_is_not_empty_should_not_fail_if_iterable_not_empty(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_not_empty"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (198 > 100 characters) (auto-generated noqa)
        tuple_instance = (1, 3)

        Guard.is_not_empty(tuple_instance, nameof(tuple_instance))

    @unittest.skip("known to fail!")
    def test_size_of_iterable_breaks_iterator(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.size_is_greater_or_equal_than"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (381 > 100 characters) (auto-generated noqa)
        iterable_instance = map(lambda x: x, range(0, 10))

        Guard.size_is_greater_or_equal_than(iterable_instance, 3, nameof(iterable_instance))

        iterable_instance_to_list = list(iterable_instance)
        self.assertEqual(first=10, second=len(iterable_instance_to_list))

    def test_size_is_greater_or_equal_than_fails_if_iterable_has_not_enough_elements(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.size_is_greater_or_equal_than"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (381 > 100 characters) (auto-generated noqa)
        tuple_instance = (2, 4)

        with self.assertRaises(ValueError) as ctx:
            Guard.size_is_greater_or_equal_than(tuple_instance, 3, nameof(tuple_instance))

        self.assertEqual(
            "The iterable tuple_instance must have at least 3 elements.",
            str(ctx.exception),
        )

    def test_size_is_greater_or_equal_than_should_not_fail(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.size_is_greater_or_equal_than"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (381 > 100 characters) (auto-generated noqa)
        tuple_instance = (1.0, 2, 3, 4)

        Guard.size_is_greater_or_equal_than(tuple_instance, 3, nameof(tuple_instance))

    def test_size_is_less_than_or_equal_fails_if_iterable_is_too_large(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.Guard.size_is_less_than_or_equal"""  # noqa: W505, D415 - doc line too long (107 > 100 characters) (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)
        tuple_instance = (2, 4, 5, 6)

        with self.assertRaises(ValueError) as ctx:
            Guard.size_is_less_than_or_equal(tuple_instance, 3, nameof(tuple_instance))

        self.assertEqual(
            "The size of tuple_instance must less than or equal to 3.",
            str(ctx.exception),
        )

    def test_size_is_less_than_or_equal_should_not_fail(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.Guard.size_is_less_than_or_equal"""  # noqa: W505, D415 - doc line too long (107 > 100 characters) (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)
        tuple_instance = (1.0, 2)

        Guard.size_is_less_than_or_equal(tuple_instance, 3, nameof(tuple_instance))

    def test_all_elements_are_of_same_type_fails_if_list_contains_invalid_objects(self):
        """Unit test
        of nipcbatt.pcbatt_utilities.guard_utilities.Guard.all_elements_are_of_same_type
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        input_list = [1.0, 3.0, "string_not_allowed"]

        with self.assertRaises(TypeError) as ctx:
            Guard.all_elements_are_of_same_type(input_list=input_list, expected_type=float)

        self.assertEqual(
            "Not all elements of the list are of the type (float).", str(ctx.exception)
        )

    def test_all_elements_are_of_same_type_should_not_fail(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.all_elements_are_of_same_type"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (381 > 100 characters) (auto-generated noqa)
        input_list = [1.0, 3.0, 10.0]

        Guard.all_elements_are_of_same_type(input_list=input_list, expected_type=float)

    def test_have_same_size_fails_if_lists_have_not_same_size(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.have_same_size"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (200 > 100 characters) (auto-generated noqa)
        first_input_list = [1.0, 3.0, 4.0]
        second_input_list = ["item_1", "item_2", "item_3", "item_4"]

        with self.assertRaises(ValueError) as ctx:
            Guard.have_same_size(
                first_iterable_instance=first_input_list,
                first_iterable_name=nameof(first_input_list),
                second_iterable_instance=second_input_list,
                second_iterable_name=nameof(second_input_list),
            )

        self.assertEqual(
            "The iterables (first_input_list and second_input_list) do not have same size.",
            str(ctx.exception),
        )

    def test_have_same_size_should_not_fail(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.have_same_size"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (200 > 100 characters) (auto-generated noqa)
        first_input_list = [1.0, 3.0, 4.0]
        second_input_list = ["item_1", "item_2", "item_3"]

        Guard.have_same_size(
            first_iterable_instance=first_input_list,
            first_iterable_name=nameof(first_input_list),
            second_iterable_instance=second_input_list,
            second_iterable_name=nameof(second_input_list),
        )

    def test_is_not_none_fails_if_object_is_none(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_not_none"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (363 > 100 characters) (auto-generated noqa)
        instance = None
        with self.assertRaises(ValueError) as ctx:
            Guard.is_not_none(instance, nameof(instance))

        self.assertEqual("The object instance is None.", str(ctx.exception))

    def test_is_not_none_should_not_fail(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_not_none"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (363 > 100 characters) (auto-generated noqa)
        instance = 3.0
        Guard.is_not_none(instance, nameof(instance))

    def test_is_greater_than_zero_fails_if_object_is_string(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_zero"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (372 > 100 characters) (auto-generated noqa)
        instance = "-6"

        with self.assertRaises(TypeError) as ctx:
            Guard.is_greater_than_zero(instance, nameof(instance))

        self.assertEqual("The object instance is not a numeric value.", str(ctx.exception))

    def test_is_greater_than_zero_fails_if_object_is_less_than_or_equal_to_zero(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_zero"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (372 > 100 characters) (auto-generated noqa)
        instance = -6
        with self.assertRaises(ValueError) as ctx:
            Guard.is_greater_than_zero(instance, nameof(instance))

        self.assertEqual("The value instance must be greater than 0.", str(ctx.exception))

    def test_is_greater_than_zero_should_not_fail(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_zero"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (372 > 100 characters) (auto-generated noqa)
        instance = 3.0
        Guard.is_greater_than_zero(instance, nameof(instance))

    def test_is_greater_than_or_equal_to_zero_fails_if_object_is_string(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_or_equal_to_zero
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        instance = "-6"

        with self.assertRaises(TypeError) as ctx:
            Guard.is_greater_than_or_equal_to_zero(instance, nameof(instance))

        self.assertEqual("The object instance is not a numeric value.", str(ctx.exception))

    def test_is_greater_than_or_equal_to_zero_fails_if_object_is_negative(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_or_equal_to_zero
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        instance = -6
        with self.assertRaises(ValueError) as ctx:
            Guard.is_greater_than_or_equal_to_zero(instance, nameof(instance))

        self.assertEqual(
            "The value instance must be greater than or equal to 0.", str(ctx.exception)
        )

    def test_is_greater_than_or_equal_to_zero_should_not_fail(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_or_equal_to_zero
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        instance = 3.0
        Guard.is_greater_than_or_equal_to_zero(instance, nameof(instance))
        instance = 0.0
        Guard.is_greater_than_or_equal_to_zero(instance, nameof(instance))

    def test_is_less_than_zero_fails_if_object_is_string(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_zero"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (203 > 100 characters) (auto-generated noqa)
        instance = "-6"

        with self.assertRaises(TypeError) as ctx:
            Guard.is_less_than_zero(instance, nameof(instance))

        self.assertEqual("The object instance is not a numeric value.", str(ctx.exception))

    def test_is_less_than_zero_fails_if_object_is_positive_or_equal_to_zero(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_zero"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (203 > 100 characters) (auto-generated noqa)
        instance = 6
        with self.assertRaises(ValueError) as ctx:
            Guard.is_less_than_zero(instance, nameof(instance))

        self.assertEqual("The value instance must be less than 0.", str(ctx.exception))

    def test_is_less_than_zero_should_not_fail(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_zero"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (203 > 100 characters) (auto-generated noqa)
        instance = -3.0
        Guard.is_less_than_zero(instance, nameof(instance))

    def test_is_less_than_or_equal_to_zero_fails_if_object_is_string(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_or_equal_to_zero"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (381 > 100 characters) (auto-generated noqa)
        instance = "-6"

        with self.assertRaises(TypeError) as ctx:
            Guard.is_less_than_or_equal_to_zero(instance, nameof(instance))

        self.assertEqual("The object instance is not a numeric value.", str(ctx.exception))

    def test_is_less_than_or_equal_to_zero_fails_if_object_is_greater_than_zero(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_or_equal_to_zero"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (381 > 100 characters) (auto-generated noqa)
        instance = 6
        with self.assertRaises(ValueError) as ctx:
            Guard.is_less_than_or_equal_to_zero(instance, nameof(instance))

        self.assertEqual("The value instance must be less than or equal to 0.", str(ctx.exception))

    def test_is_less_than_or_equal_to_zero_should_not_fail(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_or_equal_to_zero"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (381 > 100 characters) (auto-generated noqa)
        instance = -3.0
        Guard.is_less_than_or_equal_to_zero(instance, nameof(instance))
        instance = 0.0
        Guard.is_less_than_or_equal_to_zero(instance, nameof(instance))

    def test_is_less_than_fails_if_value_is_string(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (198 > 100 characters) (auto-generated noqa)
        instance = "-6"

        with self.assertRaises(TypeError) as ctx:
            Guard.is_less_than(instance, -3, nameof(instance))

        self.assertEqual("The object instance is not a numeric value.", str(ctx.exception))

    def test_is_less_than_fails_if_expected_greater_value_is_string(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (198 > 100 characters) (auto-generated noqa)
        instance = -6

        with self.assertRaises(TypeError) as ctx:
            Guard.is_less_than(instance, "-3", nameof(instance))

        self.assertEqual(
            "The object expected_greater_value is not a numeric value.",
            str(ctx.exception),
        )

    def test_is_less_than_fails_if_value_is_greater_or_equal(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (198 > 100 characters) (auto-generated noqa)
        instance = -6
        with self.assertRaises(ValueError) as ctx:
            Guard.is_less_than(instance, -8, nameof(instance))

        self.assertEqual("The value instance must be less than -8.", str(ctx.exception))

    def test_is_less_than_should_not_fail(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (198 > 100 characters) (auto-generated noqa)
        instance = 3.0
        Guard.is_less_than(instance, 4.0, nameof(instance))

    def test_is_less_than_or_equal_to_fails_if_value_is_string(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_or_equal_to"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        instance = "-6"

        with self.assertRaises(TypeError) as ctx:
            Guard.is_less_than_or_equal_to(instance, -3, nameof(instance))

        self.assertEqual("The object instance is not a numeric value.", str(ctx.exception))

    def test_is_less_than_or_equal_to_fails_if_expected_greater_value_is_string(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_or_equal_to"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        instance = -6

        with self.assertRaises(TypeError) as ctx:
            Guard.is_less_than_or_equal_to(instance, "-3", nameof(instance))

        self.assertEqual(
            "The object expected_greater_value is not a numeric value.",
            str(ctx.exception),
        )

    def test_is_less_than_or_equal_to_fails_if_value_is_greater(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_or_equal_to"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        instance = -6
        with self.assertRaises(ValueError) as ctx:
            Guard.is_less_than_or_equal_to(instance, -8, nameof(instance))

        self.assertEqual("The value instance must be less than or equal to -8.", str(ctx.exception))

    def test_is_less_than_or_equal_to_should_not_fail(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_or_equal_to"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        instance = 3.0
        Guard.is_less_than_or_equal_to(instance, 4.0, nameof(instance))
        instance = 4.0
        Guard.is_less_than_or_equal_to(instance, 4.0, nameof(instance))

    def test_is_greater_than_fails_if_value_is_string(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (201 > 100 characters) (auto-generated noqa)
        instance = "6"

        with self.assertRaises(TypeError) as ctx:
            Guard.is_greater_than(instance, 3, nameof(instance))

        self.assertEqual("The object instance is not a numeric value.", str(ctx.exception))

    def test_is_greater_than_fails_if_expected_smaller_value_is_string(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (201 > 100 characters) (auto-generated noqa)
        instance = 6

        with self.assertRaises(TypeError) as ctx:
            Guard.is_greater_than(
                value=instance, expected_smaller_value="3", value_name=nameof(instance)
            )

        self.assertEqual(
            "The object expected_smaller_value is not a numeric value.",
            str(ctx.exception),
        )

    def test_is_greater_than_fails_if_value_is_less_than_or_equal_to(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (201 > 100 characters) (auto-generated noqa)
        instance = 6
        with self.assertRaises(ValueError) as ctx:
            Guard.is_greater_than(instance, 8, nameof(instance))

        self.assertEqual("The value instance must be greater than 8.", str(ctx.exception))

    def test_is_greater_than_should_not_fail(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (201 > 100 characters) (auto-generated noqa)
        instance = 6.0
        Guard.is_greater_than(instance, 4.0, nameof(instance))

    def test_is_greater_or_equal_to_fails_if_value_is_string(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_or_equal_to"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (379 > 100 characters) (auto-generated noqa)
        instance = "6"

        with self.assertRaises(TypeError) as ctx:
            Guard.is_greater_than_or_equal_to(instance, 3, nameof(instance))

        self.assertEqual("The object instance is not a numeric value.", str(ctx.exception))

    def test_is_greater_than_or_equal_to_fails_if_expected_smaller_value_is_string(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_or_equal_to"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (379 > 100 characters) (auto-generated noqa)
        instance = 6

        with self.assertRaises(TypeError) as ctx:
            Guard.is_greater_than_or_equal_to(
                value=instance, expected_smaller_value="3", value_name=nameof(instance)
            )

        self.assertEqual(
            "The object expected_smaller_value is not a numeric value.",
            str(ctx.exception),
        )

    def test_is_greater_than_or_equal_to_fails_if_value_is_less_than(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_or_equal_to"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (379 > 100 characters) (auto-generated noqa)
        instance = 6
        with self.assertRaises(ValueError) as ctx:
            Guard.is_greater_than_or_equal_to(instance, 8, nameof(instance))

        self.assertEqual(
            "The value instance must be greater than or equal to 8.", str(ctx.exception)
        )

    def test_is_greater_than_or_equal_to_should_not_fail(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_or_equal_to"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (379 > 100 characters) (auto-generated noqa)
        instance = 6.0
        Guard.is_greater_than_or_equal_to(instance, 4.0, nameof(instance))
        instance = 4.0
        Guard.is_greater_than_or_equal_to(instance, 4.0, nameof(instance))

    def test_is_not_none_nor_empty_nor_whitespace_fails_if_string_value_is_none(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_not_none_nor_empty_nor_whitespace
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        instance = None
        with self.assertRaises(ValueError) as ctx:
            Guard.is_not_none_nor_empty_nor_whitespace(value=instance, value_name=nameof(instance))

        self.assertEqual(
            "The string value instance is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_is_not_none_nor_empty_nor_whitespace_fails_if_string_value_is_empty(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_not_none_nor_empty_nor_whitespace
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        instance = ""
        with self.assertRaises(ValueError) as ctx:
            Guard.is_not_none_nor_empty_nor_whitespace(value=instance, value_name=nameof(instance))

        self.assertEqual(
            "The string value instance is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_is_not_none_nor_empty_nor_whitespace_fails_if_string_value_is_whitespace(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_not_none_nor_empty_nor_whitespace
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        instance = " "
        with self.assertRaises(ValueError) as ctx:
            Guard.is_not_none_nor_empty_nor_whitespace(value=instance, value_name=nameof(instance))

        self.assertEqual(
            "The string value instance is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_is_not_none_nor_empty_nor_whitespace_should_not_fail(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_not_none_nor_empty_nor_whitespace
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        instance = "3.0"
        Guard.is_not_none_nor_empty_nor_whitespace(value=instance, value_name=nameof(instance))


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_utilities_tests/test_iterable_utilities.py sha256=7d34f7b35c866d3ed5143b2a853ec8ed23e20273303b7d5513d4a2be8f64055b bytes=2463 -->
## FILE: tests/nipcbatt_tests/pcbatt_utilities_tests/test_iterable_utilities.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_utilities_tests/test_iterable_utilities.py`
- sha256: `7d34f7b35c866d3ed5143b2a853ec8ed23e20273303b7d5513d4a2be8f64055b`
- bytes: 2463

````python
"""Provides unit tests related to iterable_utilities.py module"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (176 > 100 characters) (auto-generated noqa)

import logging
import platform
import sys
import unittest

from nipcbatt.pcbatt_utilities import iterable_utilities


class TestIterableUtilities(unittest.TestCase):
    """Defines a test fixture that checks function of module
    `pcbatt_utilities.iterable_utilities`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_count_invalid_input(self):
        """Unit test of iterable_utilities.count"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)
        self.assertRaises(ValueError, lambda: iterable_utilities.count(None))

    def test_count(self):
        """Unit test of iterable_utilities.count"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)
        self.assertEqual(first=0, second=iterable_utilities.count([])[0])
        self.assertEqual(first=1, second=iterable_utilities.count([1])[0])
        self.assertEqual(first=2, second=iterable_utilities.count([1, "aa"])[0])

        self.assertEqual(first=10, second=iterable_utilities.count(range(0, 10))[0])


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_utilities_tests/test_native_interop_utilities.py sha256=1253ec70017a7e7f96a1525a7f2b78a4aadaaaf3134ab1342ae3a54f75c0cada bytes=5502 -->
## FILE: tests/nipcbatt_tests/pcbatt_utilities_tests/test_native_interop_utilities.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_utilities_tests/test_native_interop_utilities.py`
- sha256: `1253ec70017a7e7f96a1525a7f2b78a4aadaaaf3134ab1342ae3a54f75c0cada`
- bytes: 5502

````python
"""This module provides check of functions in 
nipcbatt.pcbatt_library_code.ni_845x_i2c_spi_communications.ni_845x_helper_functions package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (388 > 100 characters) (auto-generated noqa)

import importlib.metadata
import logging
import sys
import unittest

from parameterized import parameterized
from varname import nameof

from nipcbatt.pcbatt_utilities.native_interop_utilities import (
    create_native_stdcall_win_function,
)


class TestCreateNativeStdCallWinFunction(unittest.TestCase):
    """Defines a test fixture that checks
    `_create_native_stdcall_win_function` function is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    @parameterized.expand([("is_none", None), ("is_empty", ""), ("is_whitespace", " ")])
    def test_create_native_stdcall_win_function_fails_if_dll_path(
        self, test_name: str, dll_path: str
    ):
        """unit test of _create_native_stdcall_win_function."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        logging.debug("Running with %s", test_name)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            create_native_stdcall_win_function(
                dll_path=dll_path,
                function_name=None,
                return_value_type=str,
                arguments_types=[],
            )

        # Assert
        self.assertEqual(
            "The string value dll_path is None, empty or whitespace.",
            str(ctx.exception),
        )

    @parameterized.expand([("none", None), ("empty", ""), ("whitespace", " ")])
    def test_create_native_stdcall_win_function_fails_if_function_name_is_invalid(
        self, test_name: str, function_name: str
    ):
        """unit test of _create_native_stdcall_win_function."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        logging.debug("Running with %s", test_name)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            create_native_stdcall_win_function(
                dll_path="kernel32.dll",
                function_name=function_name,
                return_value_type=str,
                arguments_types=[],
            )

        # Assert
        self.assertEqual(
            "The string value function_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_create_native_stdcall_win_function_fails_if_library_not_exist(self):
        """unit test of _create_native_stdcall_win_function."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(FileNotFoundError) as ctx:
            create_native_stdcall_win_function(
                dll_path="library_not_exist.dll",
                function_name="function",
                return_value_type=str,
                arguments_types=[],
            )

        # Assert
        self.assertEqual(
            "file 'library_not_exist.dll' not found",
            str(ctx.exception),
        )

    def test_create_native_stdcall_win_function_fails_if_function_not_found(self):
        """unit test of _create_native_stdcall_win_function."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(AttributeError) as ctx:
            create_native_stdcall_win_function(
                dll_path="kernel32.dll",
                function_name="function_not_exist",
                return_value_type=str,
                arguments_types=[],
            )

        # Assert
        self.assertEqual(
            "function 'function_not_exist' not found",
            str(ctx.exception),
        )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_utilities_tests/test_numeric_utilities.py sha256=a97790888284889efdfb72cf6d6b3034c3bbddb9ab1fb132b0909ea1c81bcabc bytes=3742 -->
## FILE: tests/nipcbatt_tests/pcbatt_utilities_tests/test_numeric_utilities.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_utilities_tests/test_numeric_utilities.py`
- sha256: `a97790888284889efdfb72cf6d6b3034c3bbddb9ab1fb132b0909ea1c81bcabc`
- bytes: 3742

````python
"""Provides unit tests related to numeric_utilities.py module"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (175 > 100 characters) (auto-generated noqa)

import logging
import platform
import sys
import unittest

from nipcbatt.pcbatt_utilities import numeric_utilities


class TestNumericUtilities(unittest.TestCase):
    """Defines a test fixture that checks function of module
    `pcbatt_utilities.numeric_utilities`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_invert_value(self):
        """Unit test of numeric_utilities.invert_value"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (168 > 100 characters) (auto-generated noqa)
        self.assertEqual(1, numeric_utilities.invert_value(1))
        self.assertEqual(2, numeric_utilities.invert_value(0.5))
        self.assertRaises(ValueError, numeric_utilities.invert_value, 0)

    def test_absolute_value(self):
        """Unit test of numeric_utilities.absolute_value"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (170 > 100 characters) (auto-generated noqa)
        self.assertEqual(1, numeric_utilities.absolute_value(-1))
        self.assertEqual(1, numeric_utilities.absolute_value(1))

    def test_percent_of(self):
        """Unit test of numeric_utilities.percent_of"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (166 > 100 characters) (auto-generated noqa)
        self.assertEqual(0, numeric_utilities.percent_of(0, 100))
        self.assertEqual(0.5, numeric_utilities.percent_of(0.5, 100))
        self.assertEqual(1, numeric_utilities.percent_of(1, 100))
        self.assertEqual(10, numeric_utilities.percent_of(10, 100))
        self.assertEqual(50, numeric_utilities.percent_of(50, 100))
        self.assertEqual(100, numeric_utilities.percent_of(100, 100))

        self.assertRaises(ValueError, numeric_utilities.percent_of, -10, 100)

    def test_from_percent_to_decimal_ratio(self):
        """Unit test of numeric_utilities.percent_of"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (166 > 100 characters) (auto-generated noqa)
        self.assertEqual(1, numeric_utilities.from_percent_to_decimal_ratio(percent=100))
        self.assertEqual(0, numeric_utilities.from_percent_to_decimal_ratio(percent=0))
        self.assertEqual(0.5, numeric_utilities.from_percent_to_decimal_ratio(percent=50))


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_utilities_tests/test_os_utilities.py sha256=aaa0dea179eeb21124124072f8dd2a4d3860ed8187780f276243ff3294033af9 bytes=3032 -->
## FILE: tests/nipcbatt_tests/pcbatt_utilities_tests/test_os_utilities.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_utilities_tests/test_os_utilities.py`
- sha256: `aaa0dea179eeb21124124072f8dd2a4d3860ed8187780f276243ff3294033af9`
- bytes: 3032

````python
"""Provides unit tests related to os_utilities.py module"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (170 > 100 characters) (auto-generated noqa)

import logging
import platform
import sys
import unittest

from parameterized import parameterized

from nipcbatt.pcbatt_utilities import os_utilities


class TestOsUtilities(unittest.TestCase):
    """Defines a test fixture that checks function of module
    `pcbatt_utilities.os_utilities`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    @parameterized.expand(
        [
            ("C:/windows/explorer.exe", True),
            ("../winload.exe", False),
            ("./kernel32.dll", False),
        ]
    )
    def test_is_path_absolute_should_not_fail(self, file_path: str, expected_value: bool):
        """Unit test of nipcbatt.pcbatt_utilities.os_utilities.is_path_absolute"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (193 > 100 characters) (auto-generated noqa)
        self.assertEqual(expected_value, os_utilities.is_path_absolute(file_path))

    @parameterized.expand(
        [
            ("C:\\windows", "C:\\windows\\explorer.exe", "explorer.exe"),
            ("..", "..\\winload.exe", "winload.exe"),
            (
                "C:\\Program Files",
                "C:\\Program Files\\Python310\\Scripts\\pip.exe",
                "Python310",
                "Scripts",
                "pip.exe",
            ),
        ]
    )
    def test_combine_path_components_should_not_fail(
        self, path: str, expected_combined_path: str, *paths: str
    ):
        """Unit test of nipcbatt.pcbatt_utilities.os_utilities.combine_path_components"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (277 > 100 characters) (auto-generated noqa)

        self.assertEqual(expected_combined_path, os_utilities.combine_path_components(path, *paths))
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_utilities_tests/test_platform_utilities.py sha256=124ed032887790be48f3363b00ff941a945cdd23b4d518c790fbd9b8f8a7e6bb bytes=2613 -->
## FILE: tests/nipcbatt_tests/pcbatt_utilities_tests/test_platform_utilities.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_utilities_tests/test_platform_utilities.py`
- sha256: `124ed032887790be48f3363b00ff941a945cdd23b4d518c790fbd9b8f8a7e6bb`
- bytes: 2613

````python
"""Provides unit tests related to platform_utilities.py module"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (176 > 100 characters) (auto-generated noqa)

import logging
import platform
import sys
import unittest

from varname import nameof

from nipcbatt.pcbatt_utilities import platform_utilities


class TestPlatformUtilities(unittest.TestCase):
    """Defines a test fixture that checks function of module
    `pcbatt_utilities.platform_utilities`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_is_python_windows_32bits(self):
        """Unit test of pcbatt_utilities.platform_utilities.is_python_windows_32bits"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (198 > 100 characters) (auto-generated noqa)
        is_python_32_bits = platform_utilities.is_python_windows_32bits()
        logging.debug("%s = %s", nameof(is_python_32_bits), is_python_32_bits)
        self.assertIn(is_python_32_bits, [False, True])

    def test_is_python_windows_64bits(self):
        """Unit test of pcbatt_utilities.platform_utilities.is_python_windows_64bits"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (198 > 100 characters) (auto-generated noqa)
        is_python_64_bits = platform_utilities.is_python_windows_64bits()
        logging.debug("%s = %s", nameof(is_python_64_bits), is_python_64_bits)
        self.assertIn(is_python_64_bits, [False, True])


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/requirements_tests/__init__.py sha256=bfe755502d909429b1e7cd67c9ca93ee1a3ea29ad1a810b0feb738d5ce721034 bytes=249 -->
## FILE: tests/requirements_tests/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/requirements_tests/__init__.py`
- sha256: `bfe755502d909429b1e7cd67c9ca93ee1a3ea29ad1a810b0feb738d5ce721034`
- bytes: 249

````python
"""Provides a set of unit tests for nipcbatt dependent packages"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (177 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/requirements_tests/test_numpy.py sha256=0f28944e21602339c3c906a67809b68005ab41f7486e775baad78399def185c7 bytes=7951 -->
## FILE: tests/requirements_tests/test_numpy.py

- repository: `ni/nipcbatt`
- source_path: `tests/requirements_tests/test_numpy.py`
- sha256: `0f28944e21602339c3c906a67809b68005ab41f7486e775baad78399def185c7`
- bytes: 7951

````python
"""This module provides numpy framework check."""

import importlib.metadata
import inspect
import logging
import sys
import unittest

import numpy
import numpy.matlib
from varname import nameof


class TestNDArray(unittest.TestCase):
    """Defines a test fixture that provides sample usage of ndarray datastructure.

    Args:
        unittest (TestCase): test case using unittest framework
    """

    def setUp(self):
        print("Setup test method")

    def tearDown(self):
        print("Teardown test method")

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_numpy_version = importlib.metadata.version("numpy")
        logging.debug("%s = %s", nameof(used_numpy_version), used_numpy_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_ndarray_zeros_array(self):
        """Checks method numpy.zeros is ready to use"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (243 > 100 characters) (auto-generated noqa)

        logging.debug("=> %s", inspect.currentframe().f_code.co_name)
        ndarray_instance = numpy.zeros(shape=(4, 1), dtype=numpy.int16)
        self.assertIsNotNone(ndarray_instance)
        self.assertEqual(first=4, second=ndarray_instance.size)

        array_shape = ndarray_instance.shape
        array_shape_item1 = array_shape[0]

        logging.debug("%s = %s", nameof(array_shape), array_shape)

        self.assertEqual(first=4, second=array_shape_item1)
        self.assertEqual(first=0, second=ndarray_instance[0])
        self.assertEqual(first=0, second=ndarray_instance[1])
        self.assertEqual(first=0, second=ndarray_instance[2])
        self.assertEqual(first=0, second=ndarray_instance[3])

    def test_ndarray_create_single_dimension_array(self):
        """Checks method numpy.array is ready to use"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (243 > 100 characters) (auto-generated noqa)

        logging.debug("=> %s", inspect.currentframe().f_code.co_name)
        ndarray_instance = numpy.array([1, 2, 3, 4], dtype=numpy.int16)
        self.assertIsNotNone(ndarray_instance)
        self.assertEqual(first=4, second=ndarray_instance.size)

        array_shape = ndarray_instance.shape
        array_shape_item1 = array_shape[0]

        logging.debug("%s = %s", nameof(array_shape), array_shape)

        self.assertEqual(first=4, second=array_shape_item1)

    def test_ndarray_create_two_dimensions_array(self):
        """Checks method numpy.ndarray is ready to use"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (245 > 100 characters) (auto-generated noqa)

        logging.debug("=> %s", inspect.currentframe().f_code.co_name)
        ndarray_instance = numpy.ndarray(shape=(2, 2), dtype=numpy.int16)
        logging.debug("%s = %s", nameof(ndarray_instance), ndarray_instance)

        self.assertIsNotNone(ndarray_instance)
        self.assertEqual(first=4, second=ndarray_instance.size)

        array_shape = ndarray_instance.shape
        array_shape_item1 = array_shape[0]
        array_shape_item2 = array_shape[1]

        logging.debug("%s = %s", nameof(array_shape), array_shape)

        self.assertEqual(first=2, second=array_shape_item1)
        self.assertEqual(first=2, second=array_shape_item2)

        ndarray_instance[0][0] = 2
        ndarray_instance[0][1] = 2
        ndarray_instance[1][0] = 2
        ndarray_instance[1][1] = 2

        self.assertEqual(first=ndarray_instance[0][0], second=2)
        self.assertEqual(first=ndarray_instance[0][1], second=2)
        self.assertEqual(first=ndarray_instance[1][0], second=2)
        self.assertEqual(first=ndarray_instance[1][0], second=2)

    def test_ndarray_sum_single_dimension_array(self):
        """Checks method numpy.sum is ready to use"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (241 > 100 characters) (auto-generated noqa)

        logging.debug("=> %s", inspect.currentframe().f_code.co_name)
        ndarray_instance = numpy.array([1, 2, 3, 4], dtype=numpy.int16)

        ndarray_instance_sum = ndarray_instance.sum()
        self.assertEqual(first=10, second=ndarray_instance_sum)

    def test_ndarray_mean_single_dimension_array(self):
        """Checks method numpy.mean is ready to use"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (242 > 100 characters) (auto-generated noqa)

        logging.debug("=> %s", inspect.currentframe().f_code.co_name)
        ndarray_instance = numpy.array([1, 2, 3, 4], dtype=numpy.int16)

        ndarray_instance_sum = ndarray_instance.mean()
        self.assertEqual(first=10 / 4, second=ndarray_instance_sum)


class TestMatlib(unittest.TestCase):
    """Defines a test fixture that checks numpy package is ready to use.

    Args:
        unittest (_type_): test case type
    """

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_mathlib_average(self):
        """Checks method numpy.matlib.average is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (175 > 100 characters) (auto-generated noqa)
        average_result = numpy.matlib.average(a=[1, -1, -2, 2])
        self.assertIsNotNone(average_result)
        self.assertEqual(first=0, second=average_result)

    def test_mathlib_amax(self):
        """Checks method numpy.matlib.amax is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (172 > 100 characters) (auto-generated noqa)
        amax_result = numpy.matlib.amax(a=[1, -1, -2, 2])
        self.assertIsNotNone(amax_result)
        self.assertEqual(first=2, second=amax_result)

    def test_mathlib_amin(self):
        """Checks method numpy.matlib.amin is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (172 > 100 characters) (auto-generated noqa)
        amin_result = numpy.matlib.amin(a=[1, -1, -2, 2])
        self.assertIsNotNone(amin_result)
        self.assertEqual(first=-2, second=amin_result)

    def test_mathlib_all(self):
        """Checks method numpy.matlib.all is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
        all_result = numpy.matlib.all(a=[-1, -1, -2, -2], axis=0, where=lambda x: x < 0)
        self.assertIsNotNone(all_result)
        self.assertEqual(first=True, second=all_result)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/requirements_tests/test_scipy.py sha256=086f093aff9c05a67bed1308411a7bf587d7a5038fd48982eb24f117bdd37eba bytes=5317 -->
## FILE: tests/requirements_tests/test_scipy.py

- repository: `ni/nipcbatt`
- source_path: `tests/requirements_tests/test_scipy.py`
- sha256: `086f093aff9c05a67bed1308411a7bf587d7a5038fd48982eb24f117bdd37eba`
- bytes: 5317

````python
"""This module provides scipy framework check."""

import importlib.metadata
import logging
import sys
import unittest

import scipy
import scipy.signal
from varname import nameof


class TestSignal(unittest.TestCase):
    """Defines a test fixture that checks scipy package is ready to use.

    Args:
        unittest (TestCase): test case type
    """

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_numpy_version = importlib.metadata.version("numpy")
        used_scypi_version = importlib.metadata.version("scipy")

        logging.debug("%s = %s", nameof(used_numpy_version), used_numpy_version)
        logging.debug("%s = %s", nameof(used_scypi_version), used_scypi_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def setUp(self):
        print("Setup method")

    def tearDown(self):
        print("Teardown method")

    def test_signal_windows_hann(self):
        """Checks method scipy.signal.windows.hann is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (180 > 100 characters) (auto-generated noqa)
        window_length = 51
        hann_window = scipy.signal.windows.hann(M=window_length)
        self.assertIsNotNone(hann_window)
        self.assertEqual(first=window_length, second=len(hann_window.data))

        hann_window_first_element = hann_window[0]
        hann_window_last_element = hann_window[-1]

        self.assertEqual(first=hann_window_first_element, second=hann_window_last_element)

        self.assertAlmostEqual(first=hann_window[1], second=hann_window[-2], delta=0.0001)
        self.assertAlmostEqual(first=hann_window[2], second=hann_window[-3], delta=0.0001)
        self.assertAlmostEqual(first=hann_window[3], second=hann_window[-4], delta=0.0001)
        self.assertAlmostEqual(first=hann_window[4], second=hann_window[-5], delta=0.0001)
        self.assertAlmostEqual(first=hann_window[5], second=hann_window[-6], delta=0.0001)

    def test_signal_windows_hamming(self):
        """Checks method scipy.signal.windows.hamming is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (183 > 100 characters) (auto-generated noqa)
        window_length = 51
        hann_window = scipy.signal.windows.hamming(M=window_length)
        self.assertIsNotNone(hann_window)
        self.assertEqual(first=window_length, second=len(hann_window.data))

        hann_window_first_element = hann_window[0]
        hann_window_last_element = hann_window[-1]

        self.assertEqual(first=hann_window_first_element, second=hann_window_last_element)

        self.assertAlmostEqual(first=hann_window[1], second=hann_window[-2], delta=0.0001)
        self.assertAlmostEqual(first=hann_window[2], second=hann_window[-3], delta=0.0001)
        self.assertAlmostEqual(first=hann_window[3], second=hann_window[-4], delta=0.0001)
        self.assertAlmostEqual(first=hann_window[4], second=hann_window[-5], delta=0.0001)
        self.assertAlmostEqual(first=hann_window[5], second=hann_window[-6], delta=0.0001)

    def test_signal_find_peaks(self):
        """Checks method scipy.signal.find_peaks is ready to use"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (255 > 100 characters) (auto-generated noqa)

        sawtooth_width_eq1 = scipy.signal.sawtooth(t=range(0, 16), width=1)
        found_peaks = scipy.signal.find_peaks(x=sawtooth_width_eq1, threshold=0.01)

        logging.debug("%s = %s", nameof(sawtooth_width_eq1), sawtooth_width_eq1)
        logging.debug("%s = %s", nameof(found_peaks), found_peaks)

        self.assertIsNotNone(found_peaks)
        self.assertEqual(first=2, second=len(found_peaks[1]))

    def test_signal_square(self):
        """Checks method scipy.signal.square is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (174 > 100 characters) (auto-generated noqa)
        square_05_duty_cycle = scipy.signal.square(t=[1, 2, 3, 4], duty=0.5)
        self.assertIsNotNone(square_05_duty_cycle)
        self.assertEqual(first=4, second=len(square_05_duty_cycle.data))

    def test_signal_sawtooth(self):
        """Checks method scipy.signal.sawtooth is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (176 > 100 characters) (auto-generated noqa)
        sawtooth_width_eq1 = scipy.signal.sawtooth(t=[1, 2, 3, 4], width=1)
        self.assertIsNotNone(sawtooth_width_eq1)
        self.assertEqual(first=4, second=len(sawtooth_width_eq1.data))


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/requirements_tests/test_unittest.py sha256=b925ca9eb54d648546c6187188db7d6b41082a4bded6d1ece20a85a3fef911d5 bytes=3950 -->
## FILE: tests/requirements_tests/test_unittest.py

- repository: `ni/nipcbatt`
- source_path: `tests/requirements_tests/test_unittest.py`
- sha256: `b925ca9eb54d648546c6187188db7d6b41082a4bded6d1ece20a85a3fef911d5`
- bytes: 3950

````python
"""This module provides unit tests framework check."""

import unittest


class TestUnittest(unittest.TestCase):
    """Defines a test fixture that checks unit test framework is ready to use.

    Args:
        unittest (unittest.TestCase): test case type
    """

    def setUp(self):
        print("Setup test fixture")

    def tearDown(self):
        print("Teardown fixture")

    def test_assert_equal(self):
        """Checks method unittest.TestCase.assertEqual is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (184 > 100 characters) (auto-generated noqa)
        expected = "str"
        actual = str("str")

        self.assertEqual(first=expected, second=actual)

    def test_assert_almost_equal(self):
        """Checks method unittest.TestCase.assertAlmostEqual is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (190 > 100 characters) (auto-generated noqa)
        expected = 5
        actual = 5.1

        self.assertAlmostEqual(first=expected, second=actual, delta=0.1)

    def test_assert_assert_count_equal(self):
        """Checks method unittest.TestCase.assertCountEqual is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (189 > 100 characters) (auto-generated noqa)
        expected = [1, 2, 3, 4]
        actual = reversed(expected)

        self.assertCountEqual(first=expected, second=actual)

    def test_assert_sequence_equal(self):
        """Checks method unittest.TestCase.assertSequenceEqual is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (192 > 100 characters) (auto-generated noqa)
        expected = [1, 2, 3, 4]
        actual = (1, 2, 3, 4)

        self.assertSequenceEqual(seq1=expected, seq2=actual)

    def test_assert_dict_equal(self):
        """Checks method unittest.TestCase.assertDictEqual is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (188 > 100 characters) (auto-generated noqa)
        dictionary_src = {"k1": "v1", "k2": "v2"}

        self.assertDictEqual(d1=dictionary_src, d2=dictionary_src)

    def test_assert_in(self):
        """Checks method unittest.TestCase.assertIn is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (181 > 100 characters) (auto-generated noqa)
        self.assertIn(member=2, container=(1, 2, 3))

    def test_assert_not_in(self):
        """Checks method unittest.TestCase.assertNotIn is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (184 > 100 characters) (auto-generated noqa)
        self.assertNotIn(member=4, container=(1, 2, 3))

    def test_assert_is_not_none(self):
        """Checks method unittest.TestCase.assertIsNotNone is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (188 > 100 characters) (auto-generated noqa)
        self.assertIsNotNone(obj={})

    def test_assert_is_none(self):
        """Checks method unittest.TestCase.assertIsNotNone is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (188 > 100 characters) (auto-generated noqa)
        self.assertIsNone(obj=None)


if __name__ == "__main__":
    unittest.main()
````
