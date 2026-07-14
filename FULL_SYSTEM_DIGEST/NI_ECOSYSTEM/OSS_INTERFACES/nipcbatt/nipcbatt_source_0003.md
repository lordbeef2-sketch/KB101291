# NI OSS SOURCE SNAPSHOT: nipcbatt

<!--NI_OSS_SNAPSHOT repo=ni/nipcbatt commit=a26fcd38af55e0286aacff6cdc44bf53b2041111 -->

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm_scan/dmm_scan_pmps_16V_15C.py sha256=d02b1d0790ac67df2b731e0b0abc5e65b94f781192c0913be7464fe3fed2a7a9 bytes=16240 -->
## FILE: src/nipcbatt/pcbatt_library/dmm_scan/dmm_scan_pmps_16V_15C.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dmm_scan/dmm_scan_pmps_16V_15C.py`
- sha256: `d02b1d0790ac67df2b731e0b0abc5e65b94f781192c0913be7464fe3fed2a7a9`
- bytes: 16240

````python
# pylint: disable=C0200, C0103, C0301

"""Defines class used for DMM Scan using PXI Mux and PXI Shunt"""

import time
from typing import NamedTuple

from nipcbatt import dmm, switch
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import (
    BuildingBlockUsingNIDMM,
    BuildingBlockUsingNISWITCH,
)


class ScanResources(NamedTuple):
    """This class exists to be the return type of the initialize method of DmmScanPMPS.
       It contains 2 initialized switch sessions and an initialized dmm session

    Args:
        NamedTuple: Built-in datatype to hold abstract tuples
    """

    mux_generation: switch.StaticDigitalPathGeneration
    shunt_generation: switch.StaticDigitalPathGeneration
    dmm_generation: dmm.MixedMeasurement


class MeasurementResult(NamedTuple):
    """This class is the return type of the configure_and_measure method of DmmScanPMPS.
       It contains:
        sessions: The references to the switch and dmm sessions used in the measurement
        scan_time: The total elapsed time of the scan.
        formatted_measurements: The list of all completed DMM measurements.
        execution_settings: The list of execution settings used in each measurement.
        raw_measurements: The list of raw measurements captured during the scan

    Args:
        NamedTuple: Built-in datatype to hold abstract tuples

    """

    sessions: ScanResources
    scan_time: float
    formatted_measurements: list
    execution_settings: list
    raw_measurements: list


class DmmScanPMPS(BuildingBlockUsingNIDMM, BuildingBlockUsingNISWITCH):
    """This class represents the set of properties and methods needed
       to complete a scan of different measurements using a DMM
       and various switch configurations

    Args:
        BuildingBlockUsingNISWITCH: The NI-SWITCH building block
        BuildingBlockUsingNIDMM: The NI-DMM building block
    """

    def initialize(
        self,
        mux_resource_name="Sim_MUX",
        mux_topology_name="2527/2-Wire Dual 16x1 Mux",
        shunt_resource_name="Sim_SHUNT",
        shunt_topology_name="2568/31-SPST",
        dmm_resource_name="Sim_DMM",
        powerline_freq=50,
        close_all_shunts=True,
    ) -> ScanResources:
        """Initializes the switch and dmm objects to be used in the dmm scan

        Args:
            mux_resource_name (str): The name of the mux resource. Defaults to "Sim_MUX".
            mux_topology_name (str): The name of the mux topology. Defaults to "2527/2-Wire Dual 16x1 Mux".
            shunt_resource_name (str): The name of the shunt resource. Defaults to "Sim_SHUNT".
            shunt_topology_name (str): The name of the shunt topology. Defaults to "2568/31-SPST".
            dmm_resource_name (str): The name of the dmm resource. Defaults to "Sim_DMM".
            powerline_freq (int): The power grid frequency. Defaults to 50.
            close_all_shunts (bool): If True, all shunt paths will be closed. Defaults to True.

        Returns:
            ScanResources: A tuple of two initialized switch sessions and one initialized dmm session
        """

        # Generate switch sessions for scan
        mux_generation = switch.StaticDigitalPathGeneration()
        shunt_generation = switch.StaticDigitalPathGeneration()

        # Generate dmm session for mixed measurements
        dmm_generation = dmm.MixedMeasurement()

        # Ensure sessions are cleared before use
        mux_generation.close()
        shunt_generation.close()
        dmm_generation.close()

        # Initialize sessions
        mux_generation.initialize(
            mux_resource_name, mux_topology_name, reset_device=True, simulate=False
        )
        shunt_generation.initialize(
            shunt_resource_name, shunt_topology_name, reset_device=True, simulate=False
        )
        dmm_generation.initialize(dmm_resource_name, powerline_freq)

        # Close all shunt relays from 16 to 30 (NI 2568) in a fixed
        # channel topology mapping - option to open shunts only for 2-wire resistance measuerments
        if close_all_shunts:

            # cycle across all 16 channel pairs
            for i in range(15):

                # adjust channel index
                idx = i + 16

                # declare channels
                ch1 = f"ch{idx}"
                ch2 = f"com{idx}"

                # create channel parameters and state objects
                channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch1, ch2)
                state = switch.StaticDigitalPathGenerationStateParameters(True)

                # configure terminal and timing settings
                ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(
                    channel_params, state
                )
                timing_settings = switch.StaticDigitalPathGenerationTimingParameters()
                config = switch.StaticDigitalPathGenerationConfiguration(
                    ts_settings, timing_settings
                )

                # configure and generate
                shunt_generation.configure_and_generate(config)

        # Store close_all_shunts for use in configure_and_measure
        self.close_all_shunts = close_all_shunts

        # return initialized objects
        return ScanResources(mux_generation, shunt_generation, dmm_generation)

    def configure_and_measure(
        self,
        resource_handles: ScanResources,
        scan_configuration: list,
        verbose=True,
    ) -> MeasurementResult:
        """This method executes a complete scan across every measurement which is
           provided in the scan_configuration input parameter.

        Args:
            resource_handles (ScanResources): The two switch sessions and dmm session to use.
            scan_configuration (list): Populate this list with every measurement you
              wish to make during the scan.
            verbose (bool): If True, this will print out all of the measurement results
              from the scan. Pass False if you do not wish to print results to console. Defaults to True.

        Returns:
            MeasurementResult: The results of all measurements, including sessions, scan time,
              formatted measurements, execution settings, and raw measurements.
        """
        # extract individual resource handles from resource_handles input
        mux_generation = resource_handles.mux_generation
        shunt_generation = resource_handles.shunt_generation
        dmm_generation = resource_handles.dmm_generation

        # Extract range & function, resolution in digits and channel from scan configuration.
        function_range_resolution = []
        channel_list = []
        for cfg in scan_configuration:
            channel_list.append(cfg[0])
            function_range_resolution.append((cfg[1], cfg[2]))

        # Pair channels with respective com -- ch 0-15 -> com0, ch 16-30 -> com1.
        channel_pairs = []
        for ch in channel_list:
            if ch < 16:
                pair = (ch, "com0")
            else:
                pair = (ch, "com1")
            channel_pairs.append(pair)

        # Data structures for output.
        raw_measurements = []
        formatted_measurements = []
        execution_settings = []

        # Previous function, range, resolution for comparison.
        prev = None
        params = None

        # Start wall time counter.
        start_time_all_tests = time.perf_counter()

        # Main Scan Loop
        for i in range(len(scan_configuration)):

            # Test start time.
            start_single_test_time = time.perf_counter()

            # Extract ch (int) and com (string).
            ch, com = channel_pairs[i][0], channel_pairs[i][1]
            channel_name = "ch" + str(ch)

            # MUX handling -- close MUX channel for respective ch#, com#.
            channel_params = switch.StaticDigitalPathGenerationChannelParameters(channel_name, com)
            state = switch.StaticDigitalPathGenerationStateParameters(
                True
            )  # Use TRUE value to CLOSE mux channel.
            ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(
                channel_params, state
            )
            timing_settings = switch.StaticDigitalPathGenerationTimingParameters()
            mux_config = switch.StaticDigitalPathGenerationConfiguration(
                ts_settings, timing_settings
            )

            # Execute configure and generate for mux channel pair.
            mux_generation.configure_and_generate(mux_config)

            # SHUNT handling -- if channel is a current channel, open SHUNT.
            if ch >= 16 and self.close_all_shunts:  # current channels are ch16 - ch30
                com = "com" + str(ch)
                channel_params = switch.StaticDigitalPathGenerationChannelParameters(
                    channel_name, com
                )
                state = switch.StaticDigitalPathGenerationStateParameters(
                    False
                )  # False state to OPEN shunt.
                ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(
                    channel_params, state
                )
                timing_settings = switch.StaticDigitalPathGenerationTimingParameters()
                shunt_config = switch.StaticDigitalPathGenerationConfiguration(
                    ts_settings, timing_settings
                )

                # Execute configure and generate for shunt channel pair.
                shunt_generation.configure_and_generate(shunt_config)

            # DMM handling -- configure and acquire measurement.
            function_and_range = function_range_resolution[i][0]
            resolution = function_range_resolution[i][1]

            # If previous function, range, and resolution are the same, skip dmm configuration.
            if prev != function_range_resolution[i]:

                # Instantiate parameters object.
                params = dmm.MixedMeasurementFunctionParameters(function_and_range, resolution)
                dmm_generation.configure_measurement_function(params)

            # Measure only.
            dmm_read = dmm_generation.acquire_measurement(resolution.value)

            # SHUNT handling -- close current shunt if opened.
            if ch >= 16 and self.close_all_shunts:  # current channels are ch16 - ch30
                com = "com" + str(ch)
                channel_params = switch.StaticDigitalPathGenerationChannelParameters(
                    channel_name, com
                )
                state = switch.StaticDigitalPathGenerationStateParameters(
                    True
                )  # True state to CLOSE shunt.
                ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(
                    channel_params, state
                )
                timing_settings = switch.StaticDigitalPathGenerationTimingParameters()
                shunt_config = switch.StaticDigitalPathGenerationConfiguration(
                    ts_settings, timing_settings
                )

                # Execute configure and generate for shunt channel pair.
                shunt_generation.configure_and_generate(shunt_config)

            # MUX handling -- open MUX channel to release it.
            ch, com = channel_pairs[i][0], channel_pairs[i][1]
            channel_name = "ch" + str(ch)
            channel_params = switch.StaticDigitalPathGenerationChannelParameters(channel_name, com)
            state = switch.StaticDigitalPathGenerationStateParameters(
                False
            )  # Use FALSE value to OPEN mux channel.
            ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(
                channel_params, state
            )
            timing_settings = switch.StaticDigitalPathGenerationTimingParameters()
            mux_config = switch.StaticDigitalPathGenerationConfiguration(
                ts_settings, timing_settings
            )

            # Execute configure and generate for mux channel pair.
            mux_generation.configure_and_generate(mux_config)

            # Measure elapsed time.
            switch_time = time.perf_counter() - start_single_test_time

            # Store raw output.
            meas_type = params.measurement_function.value[0].name
            value = dmm_read.measurement
            raw_data = (channel_name, value, meas_type)
            raw_measurements.append(raw_data)

            # Store formatted measurement output.
            data = dmm_read
            meas = data.measurement
            formatted_measurement = (channel_name, meas["Formatted_Measurement"], switch_time)
            formatted_measurements.append(formatted_measurement)

            # Store execution settings.
            exec_settings = data.dmm_execution_settings
            execution_settings.append(exec_settings)

            # Store current function/range/resolution settings for comparison in next loop.
            prev = function_range_resolution[i]

            # End main loop.

        # Capture total scan time.
        total_time_elapsed = time.perf_counter() - start_time_all_tests

        # If verbose is True, print results to console.
        if verbose:
            print()
            print("------------- SCAN TIME --------------")
            print("Total Scan Time (s):", f"{total_time_elapsed: .2f}")
            print("\n")

            print("------- FORMATTED MEASUREMENTS -------")
            print(f'{"Channel":<10} {"Measurement":<18} {"Time (s)":>8}')

            for i in range(len(formatted_measurements)):
                measurement = formatted_measurements[i]

                channel = measurement[0]
                value = f"{measurement[1]}"
                switch_time = measurement[2]

                print(f"{channel:<10} {value:<18} {switch_time:>8.3f}")
            print("\n")

            print("--------- EXECUTION SETTINGS ---------")
            for i, setting in enumerate(execution_settings):
                print(f"Channel: {formatted_measurements[i][0]}")
                for key, value in setting.items():
                    print(str(key) + ": " + str(value))
                print()
            print("\n")

            # Prepare raw measurements for output -- get largest width.
            values_as_str = [f"{m[1]['Measured_Value']:.16g}" for m in raw_measurements]
            value_width = max(len(v) for v in values_as_str)

            print("----------- RAW MEASUREMENTS -------------")
            print(f'{"Channel":<10} {"Value":^23} {"Units":^6}')

            for measurement, value_str in zip(raw_measurements, values_as_str):
                channel = measurement[0]
                unit = measurement[1]["Unit"]

                print(f"{channel:<10} {value_str:<{value_width}} {unit:^11}")
            print("\n")

        # Prepare output.
        output = MeasurementResult(
            ScanResources(mux_generation, shunt_generation, dmm_generation),
            total_time_elapsed,
            formatted_measurements,
            execution_settings,
            raw_measurements,
        )

        # Return measurement result.
        return output

    def close(self, resource_handles: ScanResources) -> None:
        """This method disconnects, closes, and releases the resources.

        Args:
            resource_handles (ScanResources): Contains the session handles used in the scan.
        """
        mux_generation = resource_handles.mux_generation
        shunt_generation = resource_handles.shunt_generation
        dmm_generation = resource_handles.dmm_generation

        # Close and release all resources.
        mux_generation.close()
        shunt_generation.close()
        dmm_generation.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/switch/__init__.py sha256=2cb186e31e7ed18725b4b432e8572d70139bd90cb5c9c90266180d8b4b1a460a bytes=661 -->
## FILE: src/nipcbatt/pcbatt_library/switch/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/switch/__init__.py`
- sha256: `2cb186e31e7ed18725b4b432e8572d70139bd90cb5c9c90266180d8b4b1a460a`
- bytes: 661

````python
"Contains switch modules for pcbatt library."

from nipcbatt.pcbatt_library.switch.static_digital_path_generations.static_digital_path_data_types import (
    StaticDigitalPathGenerationChannelParameters,
    StaticDigitalPathGenerationConfiguration,
    StaticDigitalPathGenerationModuleCharacteristics,
    StaticDigitalPathGenerationPathStatus,
    StaticDigitalPathGenerationStateParameters,
    StaticDigitalPathGenerationTerminalAndStateSettings,
    StaticDigitalPathGenerationTimingParameters,
)
from nipcbatt.pcbatt_library.switch.static_digital_path_generations.static_digital_path_generation import (
    StaticDigitalPathGeneration,
)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/switch/static_digital_path_generations/__init__.py sha256=f8468987591a38b01a12a0fcfd6d263910df51738b710f15694749faad0fbdb5 bytes=64 -->
## FILE: src/nipcbatt/pcbatt_library/switch/static_digital_path_generations/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/switch/static_digital_path_generations/__init__.py`
- sha256: `f8468987591a38b01a12a0fcfd6d263910df51738b710f15694749faad0fbdb5`
- bytes: 64

````python
"""Provides nipcbatt static digital path generation modules"""
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/switch/static_digital_path_generations/static_digital_path_data_types.py sha256=45129b83db9d302afd8a96abae9cd3d738f800606d55f89ac42aeae6d3af834a bytes=9490 -->
## FILE: src/nipcbatt/pcbatt_library/switch/static_digital_path_generations/static_digital_path_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/switch/static_digital_path_generations/static_digital_path_data_types.py`
- sha256: `45129b83db9d302afd8a96abae9cd3d738f800606d55f89ac42aeae6d3af834a`
- bytes: 9490

````python
"These data types are used when implementing digital path generation"

import niswitch
from varname import nameof

from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class StaticDigitalPathGenerationChannelParameters(PCBATestToolkitData):
    """Defines the channel value names assigned for the switch connection"""

    def __init__(self, channel_one: str, channel_two: str) -> None:
        """Creates an instance of StaticDigitalPathGenerationChannelParameters

        Args:
            channel_one (str): The name of the first channel
            channel_two (str): The name of the second channel
        """

        # input validation
        Guard.is_not_none_nor_empty_nor_whitespace(channel_one, nameof(channel_one))
        Guard.is_not_none_nor_empty_nor_whitespace(channel_two, nameof(channel_two))

        # assign values
        self._channel_one = channel_one
        self._channel_two = channel_two

    @property
    def channel_one(self) -> str:
        """
        :type:'str': Returns the name of channel one
        """
        return self._channel_one

    @property
    def channel_two(self) -> str:
        """
        :type:'str': Returns the name of channel two
        """
        return self._channel_two


class StaticDigitalPathGenerationStateParameters(PCBATestToolkitData):
    """Creates an instance of StaticDigitalPathGenerationStateParameters"""

    def __init__(self, connect: bool) -> None:
        """Defines whether to disconnect or connect a particular path

        Args:
            connect(bool): Indicates whether to make or break a given connection
        """

        # inout validation
        Guard.is_not_none(connect, nameof(connect))
        Guard.is_not_float(connect, nameof(connect))

        # assign values
        self._connect = connect

    @property
    def connect(self) -> bool:
        """
        :type:'boolean': Gets the boolean value to write
        """
        return self._connect


class StaticDigitalPathGenerationTimingParameters(PCBATestToolkitData):
    """Creates an instance of StaticDigitalPathGenerationTimingParameters"""

    def __init__(self, max_debounce_wait: int = 5000):
        """Defines the maximum wait for debounce time

        Args:
            max_debounce_wait (int): The maximum time to wait for debounce
        """

        # Input Validation
        Guard.is_not_none(max_debounce_wait, nameof(max_debounce_wait))
        Guard.is_greater_than_or_equal_to_zero(max_debounce_wait, nameof(max_debounce_wait))

        # assign values
        self._max_debounce_wait = max_debounce_wait

    @property
    def max_debounce_wait(self) -> int:
        """
        :type:int
        """
        return self._max_debounce_wait


class StaticDigitalPathGenerationTerminalAndStateSettings(PCBATestToolkitData):
    """Creates an instance of StaticDigitalPathGenerationTerminalAndStateSettings"""

    def __init__(
        self,
        channel_parameters: StaticDigitalPathGenerationChannelParameters,
        connection_state: StaticDigitalPathGenerationStateParameters,
    ):
        """Aggragates channel and timing parameters into a single class

        Args:
            channel_parameters (StaticDigitalPathGenerationChannelParameters): The channels
                involved in the connection
            timing_parameters (StaticDigitalPathGenerationStateParameters): The connection
                state to be implemented
        """
        # input validation
        Guard.is_not_none(channel_parameters, nameof(channel_parameters))
        Guard.is_not_none(connection_state, nameof(connection_state))

        # assign values
        self._channel_parameters = channel_parameters
        self._connection_state = connection_state

    @property
    def channel_parameters(self) -> StaticDigitalPathGenerationChannelParameters:
        """
        :type: StaticDigitalPathGenerationChannelParameters
        """
        return self._channel_parameters

    @property
    def connection_state(self) -> StaticDigitalPathGenerationStateParameters:
        """
        :type: StaticDigitalPathGenerationStateParameters
        """
        return self._connection_state


class StaticDigitalPathGenerationModuleCharacteristics(PCBATestToolkitData):
    """Defines the max voltage and current characteristics of the switch"""

    def __init__(
        self,
        max_dc_voltage: float,
        max_ac_voltage: float,
        max_switching_dc_current: float,
        max_switching_ac_current: float,
    ) -> None:
        """Creates an instance of StaticDigitalPathGenerationModuleCharacteristics

        Args:
            max_dc_voltage (float): The rated maximum DC voltage of the topology
            max_ac_voltage (float): The rated maximum AC voltage of the topology
            max_switching_dc_current (float): The rated maximum DC switching current of the topology
            max_switching_ac_current (float): The rated maximum AC switching current of the topology
        """

        # input validation
        Guard.is_not_none(max_dc_voltage, nameof(max_dc_voltage))
        Guard.is_greater_than_or_equal_to_zero(max_dc_voltage, nameof(max_dc_voltage))

        Guard.is_not_none(max_ac_voltage, nameof(max_ac_voltage))
        Guard.is_greater_than_or_equal_to_zero(max_ac_voltage, nameof(max_ac_voltage))

        Guard.is_not_none(max_switching_dc_current, nameof(max_switching_dc_current))
        Guard.is_greater_than_or_equal_to_zero(
            max_switching_dc_current, nameof(max_switching_dc_current)
        )

        Guard.is_not_none(max_switching_ac_current, nameof(max_switching_ac_current))
        Guard.is_greater_than_or_equal_to_zero(
            max_switching_ac_current, nameof(max_switching_ac_current)
        )

        # assign values
        self._max_dc_voltage = max_dc_voltage
        self._max_ac_voltage = max_ac_voltage
        self._max_switching_dc_current = max_switching_dc_current
        self._max_switching_ac_current = max_switching_ac_current

    @property
    def max_dc_voltage(self) -> float:
        """
        :type:'float': Returns the max DC voltage for the topology
        """
        return self._max_dc_voltage

    @property
    def max_ac_voltage(self) -> float:
        """
        :type:'float': Returns the max AC voltage for the topology
        """
        return self._max_ac_voltage

    @property
    def max_switching_dc_current(self) -> float:
        """
        :type:'float': Returns the max dc switching current
        """
        return self._max_switching_dc_current

    @property
    def max_switching_ac_current(self) -> float:
        """
        :type:'float': Returns the max ac switching current
        """
        return self._max_switching_ac_current


class StaticDigitalPathGenerationConfiguration(PCBATestToolkitData):
    """Contains the ultimate configuration used in path generation"""

    def __init__(
        self,
        terminal_and_state_settings: StaticDigitalPathGenerationTerminalAndStateSettings,
        timing_settings: StaticDigitalPathGenerationTimingParameters,
    ) -> None:
        """Creates an instance of StaticDigitalPathGenerationConfiguration

        Args:
            terminal_state_settings (StaticDigitalPathGenerationTerminalAndStateSettings):
                A populated instance of StaticDigitalPathGenerationTerminalAndStateSettings
            timing_settings (StaticDigitalPathGenerationTimingParameters):
                A populated instance of StaticDigitalPathTimingParameters
        """

        # input validation
        Guard.is_not_none(terminal_and_state_settings, nameof(terminal_and_state_settings))
        Guard.is_not_none(timing_settings, nameof(timing_settings))

        # assign values
        self._terminal_and_state_settings = terminal_and_state_settings
        self._timing_settings = timing_settings

    @property
    def terminal_and_state_settings(self) -> StaticDigitalPathGenerationTerminalAndStateSettings:
        """
        :type: StaticDigitalPathGenerationTerminalAndStateSettings
        """
        return self._terminal_and_state_settings

    @property
    def timing_settings(self) -> StaticDigitalPathGenerationTimingParameters:
        """
        :type: StaticDigitalPathGenerationTimingParameters
        """
        return self._timing_settings


class StaticDigitalPathGenerationPathStatus(PCBATestToolkitData):
    """Defines the status of the path"""

    def __init__(self, path_status: niswitch.PathCapability) -> None:
        """Creates an instance of StaticDigitalPathGenerationPathStatus

        Args:
            path_status (str): Displays whether or not the switch path is available
        """

        # input validation
        Guard.is_not_none(path_status, nameof(path_status))
        Guard.is_not_float(path_status, nameof(path_status))

        # assign values
        self._path_status = path_status

    @property
    def path_status(self) -> niswitch.PathCapability:
        """
        :type:'string': Returns the availability of the path for the given connections
        """
        return self._path_status
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/switch/static_digital_path_generations/static_digital_path_generation.py sha256=e497df411e0a2bc5da9f87948272cbc30878f0aba2e2ac02d23fb0e46bb3e084 bytes=7447 -->
## FILE: src/nipcbatt/pcbatt_library/switch/static_digital_path_generations/static_digital_path_generation.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/switch/static_digital_path_generations/static_digital_path_generation.py`
- sha256: `e497df411e0a2bc5da9f87948272cbc30878f0aba2e2ac02d23fb0e46bb3e084`
- bytes: 7447

````python
"""Use this class to connect switch paths in a test fixture"""

# pylint: disable=W0611

from typing import List

import nidaqmx.constants
import nidaqmx.errors
import nidaqmx.stream_writers
import nidaqmx.system
import niswitch
import numpy as np
from varname import nameof

from nipcbatt.pcbatt_library.switch.static_digital_path_generations.static_digital_path_data_types import (
    StaticDigitalPathGenerationChannelParameters,
    StaticDigitalPathGenerationConfiguration,
    StaticDigitalPathGenerationModuleCharacteristics,
    StaticDigitalPathGenerationPathStatus,
    StaticDigitalPathGenerationStateParameters,
    StaticDigitalPathGenerationTerminalAndStateSettings,
    StaticDigitalPathGenerationTimingParameters,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import (
    BuildingBlockUsingDAQmx,
    BuildingBlockUsingNISWITCH,
)
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryException,
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class StaticDigitalPathGeneration(BuildingBlockUsingNISWITCH):
    """This class represents the set of digital path connections the
       user wishes to create on the switch matrix

    Args:
        BuildingBlockUsingNISWITCH: The NI-SWITCH building block
    """

    def initialize(
        self,
        switch_resource_name: str,
        topology_name: str,
        reset_device: bool = True,
        simulate: bool = False,
    ) -> StaticDigitalPathGenerationModuleCharacteristics:
        """Initializes the session to prepare for path generation

        Args:
            switch_resource_name (str): The name of the switch
            resource to be used
        """
        if self.is_session_initialized:
            return

        # input validation
        Guard.is_not_none(switch_resource_name, nameof(switch_resource_name))
        Guard.is_not_empty(switch_resource_name, nameof(switch_resource_name))

        Guard.is_not_none(topology_name, nameof(topology_name))
        Guard.is_not_empty(topology_name, nameof(topology_name))

        Guard.is_not_none(reset_device, nameof(reset_device))
        if not isinstance(reset_device, bool):
            raise TypeError(f"{nameof(reset_device)} must be a bool.")

        # clean input
        switch_resource_name = switch_resource_name.strip()
        topology_name = topology_name.strip()

        # create session with parameters
        session = niswitch.Session(
            resource_name=switch_resource_name,
            topology=topology_name,
            simulate=simulate,
            reset_device=reset_device,
        )

        # assign session
        self._instrument = session

        # populate module characteristics
        module_characteristics = StaticDigitalPathGenerationModuleCharacteristics(
            self.session.max_dc_voltage,
            self.session.max_ac_voltage,
            self.session.max_switching_dc_current,
            self.session.max_switching_ac_current,
        )

        # return the utilized moduel characteristics
        return module_characteristics

    def close(self):
        """Disconnects all channels, closes the session and returns the resource"""
        if not self.is_session_initialized:
            return

        # disconnect all connections
        self.session.disconnect_all()

        # close the session
        self.session.close()

    def configure_and_generate(
        self, configuration=StaticDigitalPathGenerationConfiguration
    ) -> StaticDigitalPathGenerationPathStatus:
        """Creates the connections defined within the terminal and state settings
        and generates a path status indicating if the operation was succesful

        Args:
             StaticDigitalPathGenerationConfiguration: Contains both the channel and state to employ

         Returns: A StaticDigitalPathGenerationPathStatus object containing the path status
        """

        # extract channels and state to employ
        channel_one = configuration.terminal_and_state_settings.channel_parameters.channel_one
        channel_two = configuration.terminal_and_state_settings.channel_parameters.channel_two
        connect = configuration.terminal_and_state_settings.connection_state.connect

        # extract maximum wait for debounce time
        max_wait = configuration.timing_settings.max_debounce_wait

        # verify channels can be connected
        path_capability = self.session.can_connect(channel_one, channel_two)

        # connect depending on path capability
        if path_capability == niswitch.PathCapability.PATH_AVAILABLE:

            # if connecting make connection, else disconnect
            if connect:
                self.session.connect(channel_one, channel_two)
            else:
                self.session.disconnect(channel_one, channel_two)

            # wait for maximum debounce time
            self.session.wait_for_debounce(max_wait)

        # if the path is connected and connect is False
        elif connect is False and path_capability == niswitch.PathCapability.PATH_EXISTS:

            # disconnect
            self.session.disconnect(channel_one, channel_two)

        # populate path status object
        path_status = StaticDigitalPathGenerationPathStatus(path_capability)

        # return path capbility inside path status object
        return path_status

    def display_status(self, status: StaticDigitalPathGenerationPathStatus) -> None:
        """Takes in a StaticDigitalPathGenerationPathStatus object and
           prints the contents in human-readable format based on the status

        Args:
            path_status (StaticDigitalPathGenerationPathStatus): A populated
            StaticDigitalPathGenerationPathStatus object
        """

        # define a set of message strings to display for a given path status
        messages = {
            niswitch.PathCapability.PATH_AVAILABLE: "Path Available",
            niswitch.PathCapability.PATH_EXISTS: "Path Exists",
            niswitch.PathCapability.PATH_UNSUPPORTED: "Path Unsupported",
            niswitch.PathCapability.RESOURCE_IN_USE: "Resource in use",
            niswitch.PathCapability.SOURCE_CONFLICT: "Source conflict",
            niswitch.PathCapability.CHANNEL_NOT_AVAILABLE: "Channel not available",
        }

        print("Path Status:", messages[status.path_status])

    def display_module_characteristics(
        self, chararteristics: StaticDigitalPathGenerationModuleCharacteristics
    ) -> None:
        """Takes in a StaticDigitalPathGenerationModuleCharacteristics object
           and prints the contents in human-readble format

        Args:
            chararteristics (StaticDigitalPathGenerationModuleCharacteristics): A
            populated StaticDigitalPathGenerationModuleCharacteristics object
        """

        print("----- MODULE CHARACTERISTICS -------")
        print("Max. DC Voltage (V):", chararteristics.max_dc_voltage)
        print("Max. AC Voltage (V):", chararteristics.max_ac_voltage)
        print("Max. Switching DC Current (A):", chararteristics.max_switching_dc_current)
        print("Max. Switching AC Current (A):", chararteristics.max_switching_ac_current)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library_core/daq/__init__.py sha256=bec6b239a4e6626d31cc42fcaf5bcb37178d9e6acafe3693f2e7f8dd3ea97df3 bytes=227 -->
## FILE: src/nipcbatt/pcbatt_library_core/daq/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library_core/daq/__init__.py`
- sha256: `bec6b239a4e6626d31cc42fcaf5bcb37178d9e6acafe3693f2e7f8dd3ea97df3`
- bytes: 227

````python
"""Provides nipcbatt core library modules"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (155 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library_core/daq/_mock_daqmx/__init__.py sha256=2ef11bc037281cb6592bd96dc9be11dee29a890170e9a2d68696d883d8813aad bytes=234 -->
## FILE: src/nipcbatt/pcbatt_library_core/daq/_mock_daqmx/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library_core/daq/_mock_daqmx/__init__.py`
- sha256: `2ef11bc037281cb6592bd96dc9be11dee29a890170e9a2d68696d883d8813aad`
- bytes: 234

````python
"""Initialization of _mock_daqmx modules package"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library_core/daq/_mock_daqmx/_mock_daqmx_constants.py sha256=4a1490f258637544775df38a9ca99b184c6f445e9ce4b09f238000402f87c8b1 bytes=11915 -->
## FILE: src/nipcbatt/pcbatt_library_core/daq/_mock_daqmx/_mock_daqmx_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library_core/daq/_mock_daqmx/_mock_daqmx_constants.py`
- sha256: `4a1490f258637544775df38a9ca99b184c6f445e9ce4b09f238000402f87c8b1`
- bytes: 11915

````python
# pylint: disable=C0301
"""Constants for mock implementation of nidaqmx."""

from enum import Enum


class _ConstantsForMockDAQmx(Enum):
    """Constants used mock implementation of nidaqmx."""

    COUNT_EDGES_TERM = "count_edges_term"
    FREQ_TERM = "freq_term"
    SEMI_PERIOD_TERM = "semi_period_term"
    PULSE_TERM = "pulse_term"
    COUNT_EDGES_ACTIVE_EDGE = "count_edges_active_edge"
    INITIAL_COUNT = "initial_count"
    COUNT_DIRECTION = "count_direction"
    FREQ_STARTING_EDGE = "freq_starting_edge"
    SEMI_PERIOD_STARTING_EDGE = "semi_period_starting_edge"
    MEAS_METHOD = "meas_method"
    MEAS_TIME = "meas_time"
    DIVISOR = "divisor"
    IDLE_STATE = "idle_state"
    INITIAL_DELAY = "initial_delay"
    PULSE_FREQ = "pulse_freq"
    PULSE_DUTY_CYC = "pulse_duty_cyc"
    PULSE_LOW_TIME = "pulse_low_time"
    PULSE_HIGH_TIME = "pulse_high_time"
    CTR_TIME_BASE_RATE = "ctr_timebase_rate"
    UNITS = "units"
    MIN_VAL = "min_val"
    MAX_VAL = "max_val"
    TERMINAL_CONFIG = "terminal_config"
    POWER_SENSE = "power_sense"
    PWR_IDLE_OUTPUT_BEHAVIOR = "pwr_idle_output_behavior"
    ADC_TIMING_MODE = "adc_timing_mode"
    CURRENT_EXCIT_SOURCE = "current_excit_source"
    RESISTANCE_CONFIG = "resistance_config"
    EXCIT_VOLTAGE_OR_CURRENT = "excit_voltage_or_current"
    VOLTAGE_SETPOINT = "voltage_setpoint"
    CURRENT_SETPOINT = "current_setpoint"
    SHUNT_RESISTOR_LOC = "shunt_resistor_loc"
    EXCIT_SOURCE = "excit_source"
    EXT_SHUNT_RESISTOR_VAL = "ext_shunt_resistor_val"
    EXCIT_VAL = "excit_val"
    R_0 = "r_0"
    R_1 = "r_1"
    RTD_TYPE = "rtd_type"
    THRMSTR_A = "thrmstr_a"
    THRMSTR_B = "thrmstr_b"
    THRMSTR_C = "thrmstr_c"
    OUTPUT_ENABLE = "output_enable"
    SAMP_PER_CHAN = "samp_quant_samp_per_chan"
    SAMP_QUANT_SAMP_PER_CHAN = "samp_quant_samp_per_chan"
    RATE = "rate"
    SOURCE = "source"
    ACTIVE_EDGE = "active_edge"
    SAMPLE_MODE = "sample_mode"
    SAMP_TIMING_ENGINE = "samp_timing_engine"
    CUSTOM_SCALE_NAME = "custom_scale_name"
    AI_MEAS_TYPE = "ai_meas_type"
    AO_MEAS_TYPE = "ao_meas_type"
    DI_MEAS_TYPE = "di_meas_type"
    DO_MEAS_TYPE = "do_meas_type"
    CI_MEAS_TYPE = "ci_meas_type"
    CO_MEAS_TYPE = "co_meas_type"
    CHANNEL_TYPE = "channel_type"
    CHANNEL_NAME = "channel_name"

    ATTRIBUTE_NOT_DEFINED_ARGS2 = "attribute {} ({}) is not defined."
    CHANNEL_NOT_DEFINED_ARGS1 = "channel {} not defined."
    NO_CHANNEL_DEFINED = "no channel is defined in task."
    NO_LINE_DEFINED_IN_CHANNEL = "No digital line defined in channel."

    DEFAULT_CTR_TIME_BASE_RATE = 80000000.0
    DEFAULT_LOW_TIME_SECONDS = 0.5
    DEFAULT_HIGH_TIME_SECONDS = 0.5
    DEFAULT_COUNTER_FREQUENCY = 10.0
    DEFAULT_COUNTER_DUTY_CYCLE = 0.5
    DEFAULT_COUNTER_SAMPLE_F64 = 1.5
    DEFAULT_COUNTER_SAMPLE_U32 = 10


_DAQMX_ATTRIBUTES = {
    # used when invoke property nidaqmx._task_modules.channels.channel.Channel.chan_type
    0x187F: _ConstantsForMockDAQmx.CHANNEL_TYPE,
    # used when invoke property nidaqmx._task_modules.channels.ci_channel.CIChannel.ci_count_edges_term  # noqa: W505 - doc line too long (103 > 100 characters) (auto-generated noqa)
    0x18C7: _ConstantsForMockDAQmx.COUNT_EDGES_TERM,
    # used when invoke property nidaqmx._task_modules.channels.ci_channel.CIChannel.ci_freq_term
    0x18A2: _ConstantsForMockDAQmx.FREQ_TERM,
    # used when invoke property nidaqmx._task_modules.channels.ci_channel.CIChannel.ci_semi_period_term  # noqa: W505 - doc line too long (103 > 100 characters) (auto-generated noqa)
    0x18B0: _ConstantsForMockDAQmx.SEMI_PERIOD_TERM,
    # used when invoke property nidaqmx._task_modules.channels.co_channel.COChannel.co_pulse_term
    0x18E1: _ConstantsForMockDAQmx.PULSE_TERM,
    # used when invoke property nidaqmx._task_modules.channels.ci_channel.CIChannel.ci_count_edges_active_edge  # noqa: W505 - doc line too long (110 > 100 characters) (auto-generated noqa)
    0x697: _ConstantsForMockDAQmx.COUNT_EDGES_ACTIVE_EDGE,
    # used when invoke property nidaqmx._task_modules.channels.ci_channel.CIChannel.ci_freq_starting_edge  # noqa: W505 - doc line too long (105 > 100 characters) (auto-generated noqa)
    0x799: _ConstantsForMockDAQmx.FREQ_STARTING_EDGE,
    # used when invoke property nidaqmx._task_modules.channels.ci_channel.CIChannel.ci_semi_period_starting_edge  # noqa: W505 - doc line too long (112 > 100 characters) (auto-generated noqa)
    0x22FE: _ConstantsForMockDAQmx.SEMI_PERIOD_STARTING_EDGE,
    # used when invoke property nidaqmx._task_modules.channels.ci_channel.CIChannel.ci_freq_meas_meth  # noqa: W505 - doc line too long (101 > 100 characters) (auto-generated noqa)
    0x144: _ConstantsForMockDAQmx.MEAS_METHOD,
    # used when invoke property nidaqmx._task_modules.channels.ci_channel.CIChannel.ci_freq_meas_time  # noqa: W505 - doc line too long (101 > 100 characters) (auto-generated noqa)
    0x145: _ConstantsForMockDAQmx.MEAS_TIME,
    # used when invoke property nidaqmx._task_modules.channels.ci_channel.CIChannel.ci_freq_div
    0x147: _ConstantsForMockDAQmx.DIVISOR,
    # used when invoke property nidaqmx._task_modules.channels.ci_channel.CIChannel.ci_freq_units
    0x18A1: _ConstantsForMockDAQmx.UNITS,
    # used when invoke property nidaqmx._task_modules.channels.ci_channel.CIChannel.ci_min
    0x189D: _ConstantsForMockDAQmx.MIN_VAL,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.ci_max
    0x189C: _ConstantsForMockDAQmx.MAX_VAL,
    # used when invoke property nidaqmx._task_modules.channels.co_channel.COChannel.co_pulse_freq
    0x1178: _ConstantsForMockDAQmx.PULSE_FREQ,
    # used when invoke property nidaqmx._task_modules.channels.co_channel.COChannel.co_pulse_duty_cyc  # noqa: W505 - doc line too long (101 > 100 characters) (auto-generated noqa)
    0x1176: _ConstantsForMockDAQmx.PULSE_DUTY_CYC,
    # used when invoke property nidaqmx._task_modules.channels.co_channel.COChannel.co_ctr_timebase_rate  # noqa: W505 - doc line too long (104 > 100 characters) (auto-generated noqa)
    0x18C2: _ConstantsForMockDAQmx.CTR_TIME_BASE_RATE,
    # used when invoke property nidaqmx._task_modules.channels.co_channel.COChannel.co_pulse_idle_state  # noqa: W505 - doc line too long (103 > 100 characters) (auto-generated noqa)
    0x1170: _ConstantsForMockDAQmx.IDLE_STATE,
    # used when invoke property nidaqmx._task_modules.channels.co_channel.COChannel.co_pulse_low_time  # noqa: W505 - doc line too long (101 > 100 characters) (auto-generated noqa)
    0x18BB: _ConstantsForMockDAQmx.PULSE_LOW_TIME,
    # used when invoke property nidaqmx._task_modules.channels.co_channel.COChannel.co_pulse_low_time  # noqa: W505 - doc line too long (101 > 100 characters) (auto-generated noqa)
    0x18BA: _ConstantsForMockDAQmx.PULSE_HIGH_TIME,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.ai_term_cfg
    0x1097: _ConstantsForMockDAQmx.TERMINAL_CONFIG,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.pwr_remote_sense
    0x31DB: _ConstantsForMockDAQmx.POWER_SENSE,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.pwr_idle_output_behavior  # noqa: W505 - doc line too long (108 > 100 characters) (auto-generated noqa)
    0x31D8: _ConstantsForMockDAQmx.PWR_IDLE_OUTPUT_BEHAVIOR,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.ai_adc_timing_mode  # noqa: W505 - doc line too long (102 > 100 characters) (auto-generated noqa)
    0x29F9: _ConstantsForMockDAQmx.ADC_TIMING_MODE,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.ai_excit_src
    0x17F4: _ConstantsForMockDAQmx.CURRENT_EXCIT_SOURCE,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.ai_resistance_cfg  # noqa: W505 - doc line too long (101 > 100 characters) (auto-generated noqa)
    0x1881: _ConstantsForMockDAQmx.RESISTANCE_CONFIG,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.ai_excit_voltage_or_current  # noqa: W505 - doc line too long (111 > 100 characters) (auto-generated noqa)
    0x17F6: _ConstantsForMockDAQmx.EXCIT_VOLTAGE_OR_CURRENT,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.ai_min
    0x17DE: _ConstantsForMockDAQmx.MIN_VAL,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.ai_max
    0x17DD: _ConstantsForMockDAQmx.MAX_VAL,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.current_shunt_resistance  # noqa: W505 - doc line too long (108 > 100 characters) (auto-generated noqa)
    0x17F3: _ConstantsForMockDAQmx.EXT_SHUNT_RESISTOR_VAL,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.pwr_voltage_setpoint  # noqa: W505 - doc line too long (104 > 100 characters) (auto-generated noqa)
    0x31D4: _ConstantsForMockDAQmx.VOLTAGE_SETPOINT,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.pwr_current_setpoint  # noqa: W505 - doc line too long (104 > 100 characters) (auto-generated noqa)
    0x31D5: _ConstantsForMockDAQmx.CURRENT_SETPOINT,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.ai_excit_val
    0x17F5: _ConstantsForMockDAQmx.EXCIT_VAL,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.ai_rtd_r0
    0x1030: _ConstantsForMockDAQmx.R_0,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.ai_rtd_type
    0x1032: _ConstantsForMockDAQmx.RTD_TYPE,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.thrmstr_a
    0x18C9: _ConstantsForMockDAQmx.THRMSTR_A,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.thrmstr_b
    0x18CB: _ConstantsForMockDAQmx.THRMSTR_B,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.thrmstr_c
    0x18CA: _ConstantsForMockDAQmx.THRMSTR_C,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.ai_thrmstr_r1
    0x1061: _ConstantsForMockDAQmx.R_1,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.pwr_output_enable  # noqa: W505 - doc line too long (101 > 100 characters) (auto-generated noqa)
    0x31D6: _ConstantsForMockDAQmx.OUTPUT_ENABLE,
    # used when invoke property nidaqmx._task_modules.timing.Timing.samp_quant_samp_per_chan
    0x1300: _ConstantsForMockDAQmx.SAMP_QUANT_SAMP_PER_CHAN,
    # used when invoke property nidaqmx._task_modules.timing.Timing.samp_per_chan
    0x1310: _ConstantsForMockDAQmx.SAMP_PER_CHAN,
    # used when invoke property nidaqmx._task_modules.timing.Timing.samp_clk_rate
    0x1344: _ConstantsForMockDAQmx.RATE,
    # used when invoke property nidaqmx._task_modules.timing.Timing.samp_timing_engine
    0x2A26: _ConstantsForMockDAQmx.SAMP_TIMING_ENGINE,
    # used when invoke property nidaqmx._task_modules.channels.ao_channel.AOChannel.ao_min
    0x1187: _ConstantsForMockDAQmx.MIN_VAL,
    # used when invoke property nidaqmx._task_modules.channels.ao_channel.AOChannel.ao_max
    0x1186: _ConstantsForMockDAQmx.MAX_VAL,
    # used when invoke property nidaqmx._task_modules.channels.channel.Channel.physical_name
    0x18F5: _ConstantsForMockDAQmx.CHANNEL_NAME,
    # used when invoke property nidaqmx._task_modules.channels.ao_channel.AOChannel.ao_term_cfg
    0x188E: _ConstantsForMockDAQmx.TERMINAL_CONFIG,
}
"""The dictionnary makes a relation between attribute IDs and the attributes stored in dictionnaries of the interpreter"""  # noqa: W505 - doc line too long (122 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library_core/daq/_mock_daqmx/_mock_daqmx_interpreters.py sha256=6b58c3fa7f5c760e92f67e6b19edf9a5b507837372a5b30554c640f0305aeed7 bytes=62801 -->
## FILE: src/nipcbatt/pcbatt_library_core/daq/_mock_daqmx/_mock_daqmx_interpreters.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library_core/daq/_mock_daqmx/_mock_daqmx_interpreters.py`
- sha256: `6b58c3fa7f5c760e92f67e6b19edf9a5b507837372a5b30554c640f0305aeed7`
- bytes: 62801

````python
"""Provides mock version of nidaqmx interpreter and a set of interpreter classes related to Measurements."""  # noqa: W505 - doc line too long (108 > 100 characters) (auto-generated noqa)

import random
from enum import Enum
from typing import Any, Dict

import nidaqmx.constants
import nidaqmx.errors
import nidaqmx.utils
from nidaqmx._library_interpreter import LibraryInterpreter
from nidaqmx._task_modules.channels.channel import ChannelType

from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_constants import (
    _DAQMX_ATTRIBUTES,
    _ConstantsForMockDAQmx,
)


class _MockInterpreter(LibraryInterpreter):
    """The interpreter defines methods used for interactions with DAQmx.
    During call of methods related to DAQmx (from Task, AIChannelCollection, Timing,...),
    a call of the interpreter occurs.
    Example when calling the method `add_ai_voltage_chan` of AIChannelCollection, the method
    `create_ai_voltage_chan` of the interpreter is called.
    """  # noqa: D205, W505 - 1 blank line required between summary line and description (auto-generated noqa), doc line too long (104 > 100 characters) (auto-generated noqa)

    def __init__(self):
        super().__init__()
        self._analog_input_channels = {}
        self._digital_input_channels = {}
        self._counter_input_channels = {}
        self._analog_output_channels = {}
        self._digital_output_channels = {}
        self._counter_output_channels = {}
        self._timing = {}

    def create_task(self, session_name):
        """Called when the task is about to be created."""
        return id(self), True

    def get_task_attribute_string(self, task, attribute):
        """Called when invoke properties `nidaqmx.Task.name` or `nidaqmx.Task.channel_names`."""
        if attribute == 0x1276:
            # returns the task name.
            return ""
        if attribute == 0x1273:
            # returns the names of channels defined in task.
            channels = []
            channels.extend(list(self._analog_input_channels))
            channels.extend(list(self._analog_output_channels))
            channels.extend(list(self._digital_input_channels))
            channels.extend(list(self._digital_output_channels))
            channels.extend(list(self._counter_input_channels))
            channels.extend(list(self._counter_output_channels))

            return nidaqmx.utils.flatten_channel_string(channels)

        raise AttributeError(
            _ConstantsForMockDAQmx.ATTRIBUTE_NOT_DEFINED_ARGS2.value.format(
                attribute, hex(attribute)
            )
        )

    def get_task_attribute_uint32(self, task, attribute):
        """Called when invoke properties `nidaqmx.Task.number_of_channels`."""
        if attribute == 0x2181:
            # returns the number of channels defined in task.
            return (
                len(self._analog_input_channels)
                + len(self._analog_output_channels)
                + len(self._digital_input_channels)
                + len(self._digital_output_channels)
                + len(self._counter_input_channels)
                + len(self._counter_output_channels)
            )

        raise AttributeError(
            _ConstantsForMockDAQmx.ATTRIBUTE_NOT_DEFINED_ARGS2.value.format(
                attribute, hex(attribute)
            )
        )

    def get_read_attribute_string(self, task, attribute):
        """Called when invoke property `nidaqmx.Task.in_stream.channels_to_read`."""
        if attribute == 0x1823:
            # returns the names of channels defined in task.in_stream.
            channels = []
            channels.extend(list(self._analog_input_channels))
            channels.extend(list(self._digital_input_channels))
            channels.extend(list(self._counter_input_channels))

            return nidaqmx.utils.flatten_channel_string(channels)

        raise AttributeError(
            _ConstantsForMockDAQmx.ATTRIBUTE_NOT_DEFINED_ARGS2.value.format(
                attribute, hex(attribute)
            )
        )

    def get_read_attribute_uint32(self, task, attribute):
        """Called when invoke property `nidaqmx.Task.in_stream.di_num_booleans_per_chan`"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (279 > 100 characters) (auto-generated noqa)

        if attribute == 0x217C:
            number_of_booleans_per_channel = 0
            for channel_name in self._digital_input_channels:
                number_of_booleans_per_channel = max(
                    number_of_booleans_per_channel,
                    len(nidaqmx.utils.unflatten_channel_string(channel_name)),
                )
            return number_of_booleans_per_channel

    def get_write_attribute_uint32(self, task, attribute):
        """Called when invoke properties of `nidaqmx._task_modules.out_stream.OutStream`."""
        if attribute == 0x217E:
            # returns the number of channels defined in task.out_stream.
            channels = []
            channels.extend(list(self._analog_output_channels))
            channels.extend(list(self._digital_output_channels))
            channels.extend(list(self._counter_output_channels))

            return len(channels)

        if attribute == 0x217F:
            # returns the number of channels defined in task.out_stream.
            number_of_booleans_per_channel = 0
            for channel_name in self._digital_output_channels:
                number_of_booleans_per_channel = max(
                    number_of_booleans_per_channel,
                    len(nidaqmx.utils.unflatten_channel_string(channel_name)),
                )

            return number_of_booleans_per_channel

        raise AttributeError(
            _ConstantsForMockDAQmx.ATTRIBUTE_NOT_DEFINED_ARGS2.value.format(
                attribute, hex(attribute)
            )
        )

    def get_system_info_attribute_string(self, attribute):
        """Called when invoke property nidaqmx.system.System.local().global_channels"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (198 > 100 characters) (auto-generated noqa)
        if attribute == 0x1265:
            # returns an expression describing the global channels defined in mock system.
            return ""

        raise AttributeError(
            _ConstantsForMockDAQmx.ATTRIBUTE_NOT_DEFINED_ARGS2.value.format(
                attribute, hex(attribute)
            )
        )

    def get_chan_attribute_int32(self, task, channel: str, attribute):
        """Called when invoke properties of `nidaqmx._task_modules.channels.channel.Channel`
        and its inherited classes (AIChannel, AOChannel, DIChannel,
        DOChannel, CIChannel and COChannel).
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        return self._get_attribute_value_from_channel_settings(channel, attribute)

    def get_chan_attribute_double(self, task, channel, attribute):
        """Called when invoke properties of `nidaqmx._task_modules.channels.channel.Channel`
        and its inherited classes (AIChannel, AOChannel, DIChannel,
        DOChannel, CIChannel and COChannel).
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        return self._get_attribute_value_from_channel_settings(channel, attribute)

    def get_chan_attribute_string(self, task, channel, attribute):
        """Called when invoke properties of `nidaqmx._task_modules.channels.channel.Channel`
        and its inherited classes (AIChannel, AOChannel, DIChannel,
        DOChannel, CIChannel and COChannel).
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        return self._get_attribute_value_from_channel_settings(channel, attribute)

    def get_timing_attribute_uint64(self, task, attribute):
        """Called when invoke properties of `nidaqmx._task_modules.timing.Timing`."""
        return _MockInterpreter._retrieve_attribute_value(self._timing, attribute)

    def get_timing_attribute_uint32(self, task, attribute):
        """Called when invoke properties of `nidaqmx._task_modules.timing.Timing`."""
        return _MockInterpreter._retrieve_attribute_value(self._timing, attribute)

    def get_timing_attribute_int32(self, task, attribute):
        """Called when invoke properties of `nidaqmx._task_modules.timing.Timing`."""
        return _MockInterpreter._retrieve_attribute_value(self._timing, attribute)

    def get_timing_attribute_double(self, task, attribute):
        """Called when invoke properties of `nidaqmx._task_modules.timing.Timing`."""
        return _MockInterpreter._retrieve_attribute_value(self._timing, attribute)

    def set_timing_attribute_uint32(self, task, attribute, value):
        """Called when invoke properties of `nidaqmx._task_modules.timing.Timing`."""
        _MockInterpreter._assign_attribute_value(self._timing, attribute, value)

    def set_timing_attribute_int32(self, task, attribute, value):
        """Called when invoke properties of `nidaqmx._task_modules.timing.Timing`."""
        _MockInterpreter._assign_attribute_value(self._timing, attribute, value)

    def set_timing_attribute_uint64(self, task, attribute, value):
        """Called when invoke properties of `nidaqmx._task_modules.timing.Timing`."""
        _MockInterpreter._assign_attribute_value(self._timing, attribute, value)

    def set_chan_attribute_string(self, task, channel, attribute, value):
        """Called when invoke properties of `nidaqmx._task_modules.channels.channel.Channel`
        and its inherited classes (AIChannel, AOChannel, DIChannel,
        DOChannel, CIChannel and COChannel).
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._set_attribute_value_to_channel_settings(channel, attribute, value)

    def set_chan_attribute_int32(self, task, channel, attribute, value):
        """Called when invoke properties of `nidaqmx._task_modules.channels.channel.Channel`
        and its inherited classes (AIChannel, AOChannel, DIChannel,
        DOChannel, CIChannel and COChannel).
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._set_attribute_value_to_channel_settings(channel, attribute, value)

    def set_chan_attribute_uint32(self, task, channel, attribute, value):
        """Called when invoke properties of `nidaqmx._task_modules.channels.channel.Channel`
        and its inherited classes (AIChannel, AOChannel, DIChannel,
        DOChannel, CIChannel and COChannel).
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._set_attribute_value_to_channel_settings(channel, attribute, value)

    def set_chan_attribute_double(self, task, channel, attribute, value):
        """Called when invoke properties of `nidaqmx._task_modules.channels.channel.Channel`
        and its inherited classes (AIChannel, AOChannel, DIChannel,
        DOChannel, CIChannel and COChannel).
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._set_attribute_value_to_channel_settings(channel, attribute, value)

    def set_chan_attribute_bool(self, task, channel, attribute, value):
        """Called when invoke properties of `nidaqmx._task_modules.channels.channel.Channel`
        and its inherited classes (AIChannel, AOChannel, DIChannel,
        DOChannel, CIChannel and COChannel).
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._set_attribute_value_to_channel_settings(channel, attribute, value)

    def create_ai_voltage_chan(
        self,
        task,
        physical_channel,
        name_to_assign_to_channel,
        terminal_config,
        min_val,
        max_val,
        units,
        custom_scale_name,
    ):
        """Called when method
        `nidaqmx._task_modules.ai_channel_collection.AIChannelCollection.add_ai_voltage_chan`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)
        physical_channels_names = nidaqmx.utils.unflatten_channel_string(physical_channel)
        for physical_channel_name in physical_channels_names:
            channel = (
                self._analog_input_channels[physical_channel_name]
                if physical_channel_name in self._analog_input_channels
                else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = physical_channel_name
            channel[_ConstantsForMockDAQmx.TERMINAL_CONFIG] = terminal_config
            channel[_ConstantsForMockDAQmx.MIN_VAL] = min_val
            channel[_ConstantsForMockDAQmx.MAX_VAL] = max_val
            channel[_ConstantsForMockDAQmx.UNITS] = units
            channel[_ConstantsForMockDAQmx.CUSTOM_SCALE_NAME] = custom_scale_name
            channel[
                _ConstantsForMockDAQmx.AI_MEAS_TYPE
            ] = nidaqmx.constants.UsageTypeAI.VOLTAGE.value
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.ANALOG_INPUT.value

            self._analog_input_channels[physical_channel_name] = channel

    def create_ai_current_chan(
        self,
        task,
        physical_channel,
        name_to_assign_to_channel,
        terminal_config,
        min_val,
        max_val,
        units,
        shunt_resistor_loc,
        ext_shunt_resistor_val,
        custom_scale_name,
    ):
        """Called when method
        `nidaqmx._task_modules.ai_channel_collection.AIChannelCollection.add_ai_current_chan`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)
        physical_channels_names = nidaqmx.utils.unflatten_channel_string(physical_channel)
        for physical_channel_name in physical_channels_names:
            channel = (
                self._analog_input_channels[physical_channel_name]
                if physical_channel_name in self._analog_input_channels
                else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = physical_channel_name
            channel[_ConstantsForMockDAQmx.TERMINAL_CONFIG] = terminal_config
            channel[_ConstantsForMockDAQmx.MIN_VAL] = min_val
            channel[_ConstantsForMockDAQmx.MAX_VAL] = max_val
            channel[_ConstantsForMockDAQmx.UNITS] = units
            channel[_ConstantsForMockDAQmx.SHUNT_RESISTOR_LOC] = shunt_resistor_loc
            channel[_ConstantsForMockDAQmx.EXT_SHUNT_RESISTOR_VAL] = ext_shunt_resistor_val
            channel[_ConstantsForMockDAQmx.CUSTOM_SCALE_NAME] = custom_scale_name
            channel[
                _ConstantsForMockDAQmx.AI_MEAS_TYPE
            ] = nidaqmx.constants.UsageTypeAI.VOLTAGE.value
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.ANALOG_INPUT.value

            self._analog_input_channels[physical_channel_name] = channel

    def create_ai_power_chan(
        self,
        task,
        physical_channel,
        voltage_setpoint,
        current_setpoint,
        output_enable,
        name_to_assign_to_channel,
    ):
        """Called when method
        `nidaqmx._task_modules.ai_channel_collection.AIChannelCollection.add_ai_power_chan`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)
        physical_channels_names = nidaqmx.utils.unflatten_channel_string(physical_channel)
        for physical_channel_name in physical_channels_names:
            channel = (
                self._analog_input_channels[physical_channel_name]
                if physical_channel_name in self._analog_input_channels
                else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = physical_channel_name
            channel[_ConstantsForMockDAQmx.VOLTAGE_SETPOINT] = voltage_setpoint
            channel[_ConstantsForMockDAQmx.CURRENT_SETPOINT] = current_setpoint
            channel[_ConstantsForMockDAQmx.OUTPUT_ENABLE] = output_enable
            channel[_ConstantsForMockDAQmx.POWER_SENSE] = nidaqmx.constants.Sense.LOCAL.value
            channel[
                _ConstantsForMockDAQmx.PWR_IDLE_OUTPUT_BEHAVIOR
            ] = nidaqmx.constants.PowerIdleOutputBehavior.MAINTAIN_EXISTING_VALUE.value
            channel[_ConstantsForMockDAQmx.AI_MEAS_TYPE] = nidaqmx.constants.UsageTypeAI.POWER.value
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.ANALOG_INPUT.value

            self._analog_input_channels[physical_channel_name] = channel

    def create_airtd_chan(
        self,
        task,
        physical_channel,
        name_to_assign_to_channel,
        min_val,
        max_val,
        units,
        rtd_type,
        resistance_config,
        current_excit_source,
        current_excit_val,
        r_0,
    ):
        """Called when method
        `nidaqmx._task_modules.ai_channel_collection.AIChannelCollection.add_ai_rtd_chan`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)
        physical_channels_names = nidaqmx.utils.unflatten_channel_string(physical_channel)
        for physical_channel_name in physical_channels_names:
            channel = (
                self._analog_input_channels[physical_channel_name]
                if physical_channel_name in self._analog_input_channels
                else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = physical_channel_name
            channel[_ConstantsForMockDAQmx.MIN_VAL] = min_val
            channel[_ConstantsForMockDAQmx.MAX_VAL] = max_val
            channel[_ConstantsForMockDAQmx.UNITS] = units
            channel[_ConstantsForMockDAQmx.RTD_TYPE] = rtd_type
            channel[_ConstantsForMockDAQmx.RESISTANCE_CONFIG] = resistance_config
            channel[_ConstantsForMockDAQmx.EXCIT_SOURCE] = current_excit_source
            channel[_ConstantsForMockDAQmx.EXCIT_VAL] = current_excit_val
            channel[_ConstantsForMockDAQmx.R_0] = r_0
            channel[
                _ConstantsForMockDAQmx.AI_MEAS_TYPE
            ] = nidaqmx.constants.UsageTypeAI.TEMPERATURE_RTD.value
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.ANALOG_INPUT.value

            self._analog_input_channels[physical_channel_name] = channel

    def create_ai_thrmstr_chan_vex(
        self,
        task,
        physical_channel,
        name_to_assign_to_channel,
        min_val,
        max_val,
        units,
        resistance_config,
        voltage_excit_source,
        voltage_excit_val,
        a,
        b,
        c,
        r_1,
    ):
        """Called when method
        `nidaqmx._task_modules.ai_channel_collection.AIChannelCollection.add_ai_thrmstr_chan_vex`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)
        physical_channels_names = nidaqmx.utils.unflatten_channel_string(physical_channel)
        for physical_channel_name in physical_channels_names:
            channel = (
                self._analog_input_channels[physical_channel_name]
                if physical_channel_name in self._analog_input_channels
                else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = physical_channel_name
            channel[
                _ConstantsForMockDAQmx.TERMINAL_CONFIG
            ] = nidaqmx.constants.TerminalConfiguration.DEFAULT.value
            channel[_ConstantsForMockDAQmx.MIN_VAL] = min_val
            channel[_ConstantsForMockDAQmx.MAX_VAL] = max_val
            channel[_ConstantsForMockDAQmx.UNITS] = units
            channel[_ConstantsForMockDAQmx.RESISTANCE_CONFIG] = resistance_config
            channel[_ConstantsForMockDAQmx.EXCIT_SOURCE] = voltage_excit_source
            channel[_ConstantsForMockDAQmx.EXCIT_VAL] = voltage_excit_val
            channel[_ConstantsForMockDAQmx.THRMSTR_A] = a
            channel[_ConstantsForMockDAQmx.THRMSTR_B] = b
            channel[_ConstantsForMockDAQmx.THRMSTR_C] = c
            channel[_ConstantsForMockDAQmx.R_1] = r_1
            channel[
                _ConstantsForMockDAQmx.AI_MEAS_TYPE
            ] = nidaqmx.constants.UsageTypeAI.TEMPERATURE_THERMISTOR.value
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.ANALOG_INPUT.value

            self._analog_input_channels[physical_channel_name] = channel

    def create_ao_voltage_chan(
        self,
        task,
        physical_channel,
        name_to_assign_to_channel,
        min_val,
        max_val,
        units,
        custom_scale_name,
    ):
        """Called when method
        `nidaqmx._task_modules.ao_channel_collection.AOChannelCollection.add_ao_voltage_chan`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)
        physical_channels_names = nidaqmx.utils.unflatten_channel_string(physical_channel)
        for physical_channel_name in physical_channels_names:
            channel = (
                self._analog_output_channels[physical_channel_name]
                if physical_channel_name in self._analog_input_channels
                else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = physical_channel_name
            channel[_ConstantsForMockDAQmx.MIN_VAL] = min_val
            channel[_ConstantsForMockDAQmx.MAX_VAL] = max_val
            channel[_ConstantsForMockDAQmx.UNITS] = units
            channel[_ConstantsForMockDAQmx.CUSTOM_SCALE_NAME] = custom_scale_name
            channel[
                _ConstantsForMockDAQmx.AO_MEAS_TYPE
            ] = nidaqmx.constants.UsageTypeAO.VOLTAGE.value
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.ANALOG_OUTPUT.value

            self._analog_output_channels[physical_channel_name] = channel

    def create_di_chan(self, task, lines, name_to_assign_to_lines, line_grouping):
        """Called when method
        `nidaqmx._task_modules.di_channel_collection.DIChannelCollection.add_di_chan`
        is called."""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (391 > 100 characters) (auto-generated noqa)

        if "/line" not in lines:
            raise nidaqmx.errors.DaqError(
                _ConstantsForMockDAQmx.NO_LINE_DEFINED_IN_CHANNEL, -200376
            )

        line_grouping_value = nidaqmx.constants.LineGrouping(line_grouping)
        if line_grouping_value == nidaqmx.constants.LineGrouping.CHAN_FOR_ALL_LINES:
            channel = (
                self._digital_input_channels[lines] if lines in self._digital_input_channels else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = lines
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.DIGITAL_INPUT.value
            self._digital_input_channels[lines] = channel
        else:
            lines_names = nidaqmx.utils.unflatten_channel_string(lines)
            for line_name in lines_names:
                channel = (
                    self._digital_input_channels[line_name]
                    if line_name in self._digital_input_channels
                    else {}
                )
                channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = line_name
                channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.DIGITAL_INPUT.value
                self._digital_input_channels[line_name] = channel

    def create_do_chan(self, task, lines, name_to_assign_to_lines, line_grouping):
        """Called when method
        `nidaqmx._task_modules.do_channel_collection.DOChannelCollection.add_do_chan`
        is called."""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (391 > 100 characters) (auto-generated noqa)

        if "/line" not in lines:
            raise nidaqmx.errors.DaqError(
                _ConstantsForMockDAQmx.NO_LINE_DEFINED_IN_CHANNEL, -200376
            )

        line_grouping_value = nidaqmx.constants.LineGrouping(line_grouping)
        if line_grouping_value == nidaqmx.constants.LineGrouping.CHAN_FOR_ALL_LINES:
            channel = (
                self._digital_output_channels[lines]
                if lines in self._digital_output_channels
                else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.DIGITAL_OUTPUT.value
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = lines
            self._digital_output_channels[lines] = channel
        else:
            lines_names = nidaqmx.utils.unflatten_channel_string(lines)
            for line_name in lines_names:
                channel = (
                    self._digital_output_channels[line_name]
                    if line_name in self._digital_output_channels
                    else {}
                )
                channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = line_name
                channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.DIGITAL_OUTPUT.value
                self._digital_output_channels[line_name] = channel

    def create_ci_count_edges_chan(
        self,
        task,
        counter,
        name_to_assign_to_channel,
        edge,
        initial_count,
        count_direction,
    ):
        """Called when method
        `nidaqmx._task_modules.ci_channel_collection.CIChannelCollection.add_ci_count_edges_chan`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)
        counter_channels_names = nidaqmx.utils.unflatten_channel_string(counter)
        for counter_channel_name in counter_channels_names:
            channel = (
                self._counter_input_channels[counter_channel_name]
                if counter_channel_name in self._counter_input_channels
                else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = counter_channel_name
            channel[_ConstantsForMockDAQmx.COUNT_EDGES_ACTIVE_EDGE] = edge
            channel[_ConstantsForMockDAQmx.INITIAL_COUNT] = initial_count
            channel[_ConstantsForMockDAQmx.COUNT_DIRECTION] = count_direction
            channel[
                _ConstantsForMockDAQmx.CI_MEAS_TYPE
            ] = nidaqmx.constants.UsageTypeCI.COUNT_EDGES.value
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.COUNTER_INPUT.value

            self._counter_input_channels[counter_channel_name] = channel

    def create_ci_freq_chan(
        self,
        task,
        counter,
        name_to_assign_to_channel,
        min_val,
        max_val,
        units,
        edge,
        meas_method,
        meas_time,
        divisor,
        custom_scale_name,
    ):
        """Called when method
        `nidaqmx._task_modules.ci_channel_collection.CIChannelCollection.add_ci_freq_chan`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)
        counter_channels_names = nidaqmx.utils.unflatten_channel_string(counter)
        for counter_channel_name in counter_channels_names:
            channel = (
                self._counter_input_channels[counter_channel_name]
                if counter_channel_name in self._counter_input_channels
                else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = counter_channel_name
            channel[_ConstantsForMockDAQmx.FREQ_STARTING_EDGE] = edge
            channel[_ConstantsForMockDAQmx.MIN_VAL] = min_val
            channel[_ConstantsForMockDAQmx.MAX_VAL] = max_val
            channel[_ConstantsForMockDAQmx.UNITS] = units
            channel[_ConstantsForMockDAQmx.MEAS_METHOD] = meas_method
            channel[_ConstantsForMockDAQmx.MEAS_TIME] = meas_time
            channel[_ConstantsForMockDAQmx.DIVISOR] = divisor
            channel[_ConstantsForMockDAQmx.CUSTOM_SCALE_NAME] = custom_scale_name
            channel[
                _ConstantsForMockDAQmx.CI_MEAS_TYPE
            ] = nidaqmx.constants.UsageTypeCI.COUNT_EDGES.value
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.COUNTER_INPUT.value

            self._counter_input_channels[counter_channel_name] = channel

    def create_ci_semi_period_chan(
        self,
        task,
        counter,
        name_to_assign_to_channel,
        min_val,
        max_val,
        units,
        custom_scale_name,
    ):
        """Called when method
        `nidaqmx._task_modules.ci_channel_collection.CIChannelCollection.add_ci_semi_period_chan`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)
        counter_channels_names = nidaqmx.utils.unflatten_channel_string(counter)
        for counter_channel_name in counter_channels_names:
            channel = (
                self._counter_input_channels[counter_channel_name]
                if counter_channel_name in self._counter_input_channels
                else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = counter_channel_name
            channel[_ConstantsForMockDAQmx.MIN_VAL] = min_val
            channel[_ConstantsForMockDAQmx.MAX_VAL] = max_val
            channel[_ConstantsForMockDAQmx.UNITS] = units
            channel[_ConstantsForMockDAQmx.CUSTOM_SCALE_NAME] = custom_scale_name
            channel[
                _ConstantsForMockDAQmx.CI_MEAS_TYPE
            ] = nidaqmx.constants.UsageTypeCI.PULSE_WIDTH_DIGITAL_SEMI_PERIOD.value
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.COUNTER_INPUT.value

            self._counter_input_channels[counter_channel_name] = channel

    def create_co_pulse_chan_freq(
        self,
        task,
        counter,
        name_to_assign_to_channel,
        units,
        idle_state,
        initial_delay,
        freq,
        duty_cycle,
    ):
        """Called when method
        `nidaqmx._task_modules.co_channel_collection.COChannelCollection.add_co_pulse_chan_freq`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)
        counter_channels_names = nidaqmx.utils.unflatten_channel_string(counter)
        for counter_channel_name in counter_channels_names:
            channel = (
                self._counter_output_channels[counter_channel_name]
                if counter_channel_name in self._counter_output_channels
                else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = counter_channel_name
            channel[_ConstantsForMockDAQmx.UNITS] = units
            channel[_ConstantsForMockDAQmx.IDLE_STATE] = idle_state
            channel[_ConstantsForMockDAQmx.INITIAL_DELAY] = initial_delay
            channel[_ConstantsForMockDAQmx.PULSE_FREQ] = freq
            channel[_ConstantsForMockDAQmx.PULSE_DUTY_CYC] = duty_cycle
            channel[
                _ConstantsForMockDAQmx.CTR_TIME_BASE_RATE
            ] = _ConstantsForMockDAQmx.DEFAULT_CTR_TIME_BASE_RATE.value
            channel[
                _ConstantsForMockDAQmx.CO_MEAS_TYPE
            ] = nidaqmx.constants.UsageTypeCO.PULSE_FREQUENCY.value
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.COUNTER_OUTPUT.value

            self._counter_output_channels[counter_channel_name] = channel

    def create_co_pulse_chan_time(
        self,
        task,
        counter,
        name_to_assign_to_channel,
        units,
        idle_state,
        initial_delay,
        low_time,
        high_time,
    ):
        """Called when method
        `nidaqmx._task_modules.co_channel_collection.COChannelCollection.add_co_pulse_chan_time`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)
        counter_channels_names = nidaqmx.utils.unflatten_channel_string(counter)
        for counter_channel_name in counter_channels_names:
            channel = (
                self._counter_output_channels[counter_channel_name]
                if counter_channel_name in self._counter_output_channels
                else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = counter_channel_name
            channel[_ConstantsForMockDAQmx.IDLE_STATE] = idle_state
            channel[_ConstantsForMockDAQmx.INITIAL_DELAY] = initial_delay
            channel[_ConstantsForMockDAQmx.UNITS] = units
            channel[_ConstantsForMockDAQmx.PULSE_LOW_TIME] = low_time
            channel[_ConstantsForMockDAQmx.PULSE_HIGH_TIME] = high_time
            channel[
                _ConstantsForMockDAQmx.CTR_TIME_BASE_RATE
            ] = _ConstantsForMockDAQmx.DEFAULT_CTR_TIME_BASE_RATE.value
            channel[
                _ConstantsForMockDAQmx.CO_MEAS_TYPE
            ] = nidaqmx.constants.UsageTypeCO.PULSE_TIME.value
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.COUNTER_OUTPUT.value

            self._counter_output_channels[counter_channel_name] = channel

    def cfg_samp_clk_timing(self, task, rate, source, active_edge, sample_mode, samps_per_chan):
        """Called when method
        `nidaqmx._task_modules.timing.Timing.cfg_samp_clk_timing`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)
        self._timing[_ConstantsForMockDAQmx.RATE] = rate
        self._timing[_ConstantsForMockDAQmx.SOURCE] = source
        self._timing[_ConstantsForMockDAQmx.ACTIVE_EDGE] = active_edge
        self._timing[_ConstantsForMockDAQmx.SAMPLE_MODE] = sample_mode
        self._timing[_ConstantsForMockDAQmx.SAMP_PER_CHAN] = samps_per_chan

    def cfg_implicit_timing(self, task, sample_mode, samps_per_chan):
        """Called when method 'nidaqmx._task_modules.timing.Timing.cfg_implicit_timing'
        is called"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (313 > 100 characters) (auto-generated noqa)
        self._timing[_ConstantsForMockDAQmx.SAMPLE_MODE] = sample_mode
        self._timing[_ConstantsForMockDAQmx.SAMP_PER_CHAN] = samps_per_chan
        self._timing[_ConstantsForMockDAQmx.SAMP_QUANT_SAMP_PER_CHAN] = samps_per_chan

    def reset_timing_attribute(self, task, attribute):
        _MockInterpreter._assign_attribute_value(self._timing, attribute, None)

    def stop_task(self, task):
        """Called when method `nidaqmx.Task.stop` is called."""

    def start_task(self, task):
        """Called when method `nidaqmx.Task.start` is called."""

    def clear_task(self, task):
        """Called when method `nidaqmx.Task.close` is called."""

    def task_control(self, task, action):
        """Called when method `nidaqmx.Task.control` is called."""

    def cfg_dig_edge_start_trig(self, task, trigger_source, trigger_edge):
        """Called when method
        `nidaqmx._task_modules.triggering.start_trigger.StartTrigger.cfg_dig_edge_start_trig`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)

    def cfg_anlg_edge_start_trig(self, task, trigger_source, trigger_slope, trigger_level):
        """Called when method
        `nidaqmx._task_modules.triggering.start_trigger.StartTrigger.cfg_anlg_edge_start_trig`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)

    def disable_start_trig(self, task):
        """Called when method
        `nidaqmx._task_modules.triggering.start_trigger.StartTrigger.disable_start_trig`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)

    def read_analog_f64(self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        """Reads data samples (float64) from channel(s) defined in task."""
        return read_array, num_samps_per_chan

    def read_power_f64(
        self,
        task,
        num_samps_per_chan,
        timeout,
        fill_mode,
        read_voltage_array,
        read_current_array,
    ):
        """Reads voltage and current samples (float64) from channel(s) defined in task."""
        return read_voltage_array, read_current_array, num_samps_per_chan

    def read_counter_f64(self, task, num_samps_per_chan, timeout, read_array):
        """Reads counter samples (float64) from channel(s) defined in task."""
        return read_array, num_samps_per_chan

    def read_counter_f64_ex(self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        """Reads counter samples (float64) from channel(s) defined in task."""
        return read_array, num_samps_per_chan

    def read_counter_scalar_f64(self, task, timeout):
        """Reads counter sample (float64) from channel(s) defined in task."""
        return _ConstantsForMockDAQmx.DEFAULT_COUNTER_SAMPLE_F64.value

    def read_counter_u32(self, task, num_samps_per_chan, timeout, read_array):
        """Reads counter samples (uint32) from channel(s) defined in task."""
        return read_array, num_samps_per_chan

    def read_counter_u32_ex(self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        """Reads counter samples (uint32) from channel(s) defined in task."""
        return read_array, num_samps_per_chan

    def read_counter_scalar_u32(self, task, timeout):
        """Reads counter sample (uint32) from channel(s) defined in task."""
        return _ConstantsForMockDAQmx.DEFAULT_COUNTER_SAMPLE_U32.value

    def read_ctr_freq(
        self,
        task,
        num_samps_per_chan,
        timeout,
        interleaved,
        read_array_frequency,
        read_array_duty_cycle,
    ):
        """Reads frequency samples from channel(s) defined in task."""
        return read_array_frequency, read_array_duty_cycle, num_samps_per_chan

    def read_ctr_freq_scalar(self, task, timeout):
        """Reads frequency sample from channel(s) defined in task."""
        return (
            _ConstantsForMockDAQmx.DEFAULT_COUNTER_FREQUENCY.value,
            _ConstantsForMockDAQmx.DEFAULT_COUNTER_FREQUENCY.value,
        )

    def read_ctr_time(
        self,
        task,
        num_samps_per_chan,
        timeout,
        interleaved,
        read_array_high_time,
        read_array_low_time,
    ):
        """Reads low time and high time samples from channel(s) defined in task."""
        return read_array_high_time, read_array_low_time, num_samps_per_chan

    def read_ctr_time_scalar(self, task, timeout):
        """Reads low time and high time sample from channel(s) defined in task."""
        return (
            _ConstantsForMockDAQmx.DEFAULT_LOW_TIME_SECONDS.value,
            _ConstantsForMockDAQmx.DEFAULT_HIGH_TIME_SECONDS.value,
        )

    def read_digital_u8(self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        """Reads data samples (uint8) from channel(s) defined in task."""
        return read_array, num_samps_per_chan

    def read_digital_u16(self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        """Reads data samples (uint16) from channel(s) defined in task."""
        return read_array, num_samps_per_chan

    def read_digital_u32(self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        """Reads data samples (uint32) from channel(s) defined in task."""

    def read_digital_lines(self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        """Reads data samples from channel(s) defined in task."""
        return read_array, num_samps_per_chan, num_samps_per_chan

    def write_analog_f64(
        self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array
    ):
        """Writes data samples (float64) to channel(s) defined in task."""
        return num_samps_per_chan

    def write_digital_u8(
        self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array
    ):
        """Writes data samples (uint8) to channel(s) defined in task."""
        return num_samps_per_chan

    def write_digital_u16(
        self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array
    ):
        """Writes data samples (uint16) to channel(s) defined in task."""
        return num_samps_per_chan

    def write_digital_u32(
        self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array
    ):
        """Writes data samples (uint32) to channel(s) defined in task."""
        return num_samps_per_chan

    def write_digital_scalar_u32(self, task, auto_start, timeout, value):
        """Writes data samples to channel(s) defined in task."""

    def write_digital_lines(
        self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array
    ):
        """Writes data samples to lines in channel(s) defined in task."""
        return num_samps_per_chan

    def write_ctr_freq_scalar(self, task, auto_start, timeout, frequency, duty_cycle):
        """Writes sample to channel defined in task"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)

    def write_ctr_time_scalar(self, _handle, auto_start, timeout, high_time, low_time):
        """Writes sample to channel defined in task"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)

    def wait_until_task_done(self, task, time_to_wait):
        """Waits until the task has completed its action."""

    def export_signal(self, task, signal_id, output_terminal) -> None:
        """Exports the clock or trigger signal to the specified terminal"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (186 > 100 characters) (auto-generated noqa)

    def _get_attribute_value_from_channel_settings(self, channel_expression, attribute):
        """Retrieves value of specific attribute of channel(s) defined in channel expression"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
        channels_names = nidaqmx.utils.unflatten_channel_string(channel_expression)

        # if list of channels names is empty, gets the setting to first defined channel.
        if not channels_names:
            return self._retrieve_attribute_value_from_first_channel(attribute)

        # take the first channel in the list.
        channel_name = channels_names[0]

        attribute_value = None
        if channel_name in self._analog_input_channels:
            attribute_value = _MockInterpreter._retrieve_attribute_value_from_channel(
                self._analog_input_channels, channel_name, attribute
            )
        elif channel_name in self._analog_output_channels:
            attribute_value = _MockInterpreter._retrieve_attribute_value_from_channel(
                self._analog_output_channels, channel_name, attribute
            )
        elif channel_name in self._digital_input_channels:
            attribute_value = _MockInterpreter._retrieve_attribute_value_from_channel(
                self._digital_input_channels, channel_name, attribute
            )
        elif channel_name in self._digital_output_channels:
            attribute_value = _MockInterpreter._retrieve_attribute_value_from_channel(
                self._digital_output_channels, channel_name, attribute
            )
        elif channel_name in self._counter_input_channels:
            attribute_value = _MockInterpreter._retrieve_attribute_value_from_channel(
                self._counter_input_channels, channel_name, attribute
            )
        elif channel_name in self._counter_output_channels:
            attribute_value = _MockInterpreter._retrieve_attribute_value_from_channel(
                self._counter_output_channels, channel_name, attribute
            )
        else:
            raise ValueError(
                _ConstantsForMockDAQmx.CHANNEL_NOT_DEFINED_ARGS1.value.format(channel_name)
            )

        return attribute_value

    def _set_attribute_value_to_channel_settings(self, channel_expression, attribute, value):
        """Retrieves value to specific attribute of channel(s) defined in channel expression"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
        channels_names = nidaqmx.utils.unflatten_channel_string(channel_expression)

        # if list of channels names is empty, set the setting to all channels.
        if not channels_names:
            self._assign_attribute_value_to_channels(attribute, value)
            return

        # take the first channel in the list.
        channel_name = channels_names[0]

        if channel_name in self._analog_input_channels:
            _MockInterpreter._assign_attribute_value_to_channel(
                self._analog_input_channels,
                channel_name,
                attribute,
                value,
            )

        if channel_name in self._analog_output_channels:
            _MockInterpreter._assign_attribute_value_to_channel(
                self._analog_output_channels,
                channel_name,
                attribute,
                value,
            )

        if channel_name in self._digital_input_channels:
            _MockInterpreter._assign_attribute_value_to_channel(
                self._digital_input_channels,
                channel_name,
                attribute,
                value,
            )

        if channel_name in self._digital_output_channels:
            _MockInterpreter._assign_attribute_value_to_channel(
                self._digital_output_channels,
                channel_name,
                attribute,
                value,
            )

        if channel_name in self._counter_input_channels:
            _MockInterpreter._assign_attribute_value_to_channel(
                self._counter_input_channels,
                channel_name,
                attribute,
                value,
            )

        if channel_name in self._counter_output_channels:
            _MockInterpreter._assign_attribute_value_to_channel(
                self._counter_output_channels,
                channel_name,
                attribute,
                value,
            )

    def _retrieve_attribute_value_from_first_channel(self, attribute: int):
        channel_settings = {}

        # if analog input channels list is not empty.
        if self._analog_input_channels:
            # gets the settings of the first analog input channel.
            channel_settings = next(self._analog_input_channels.values())
        elif self._analog_output_channels:
            channel_settings = next(self._analog_output_channels.values())
        elif self._digital_input_channels:
            channel_settings = next(self._digital_input_channels.values())
        elif self._digital_output_channels:
            channel_settings = next(self._digital_output_channels.values())
        elif self._counter_input_channels:
            channel_settings = next(self._counter_input_channels.values())
        elif self._counter_output_channels:
            channel_settings = next(self._counter_output_channels.values())
        else:
            raise LookupError(_ConstantsForMockDAQmx.NO_CHANNEL_DEFINED.value)

        return _MockInterpreter._retrieve_attribute_value(channel_settings, attribute)

    def _assign_attribute_value_to_channels(self, attribute: int, value: Any):
        # sets the setting to all analog input channels.
        _MockInterpreter._assign_attribute_value_to_channels(
            self._analog_input_channels, attribute, value
        )

        _MockInterpreter._assign_attribute_value_to_channels(
            self._analog_output_channels, attribute, value
        )

        _MockInterpreter._assign_attribute_value_to_channels(
            self._digital_input_channels, attribute, value
        )

        _MockInterpreter._assign_attribute_value_to_channels(
            self._digital_output_channels, attribute, value
        )

        _MockInterpreter._assign_attribute_value_to_channels(
            self._counter_input_channels, attribute, value
        )

        _MockInterpreter._assign_attribute_value_to_channels(
            self._counter_output_channels, attribute, value
        )

    @staticmethod
    def _assign_attribute_value_to_channels(  # noqa: F811 - redefinition of unused '_assign_attribute_value_to_channels' from line 1007 (auto-generated noqa)
        channels: Dict[str, Dict], attribute: int, value: Any
    ):
        for channel_name in channels:
            _MockInterpreter._assign_attribute_value_to_channel(
                channels, channel_name, attribute, value
            )

    @staticmethod
    def _retrieve_attribute_value_from_channel(
        channels: Dict[str, Dict], channel_name: str, attribute: int
    ):
        channel_characteristics = channels[channel_name]
        return _MockInterpreter._retrieve_attribute_value(channel_characteristics, attribute)

    @staticmethod
    def _retrieve_attribute_value(attributes: Dict[str, Any], attribute: int):
        attribute_name = _DAQMX_ATTRIBUTES[attribute]
        if attribute_name in attributes:
            return attributes[attribute_name]

        raise AttributeError(
            _ConstantsForMockDAQmx.ATTRIBUTE_NOT_DEFINED_ARGS2.value.format(
                attribute, hex(attribute)
            )
        )

    @staticmethod
    def _assign_attribute_value_to_channel(
        channels: Dict[str, Dict], channel_name: str, attribute: int, value: Any
    ):
        channel_characteristics = channels[channel_name]
        _MockInterpreter._assign_attribute_value(channel_characteristics, attribute, value)

    @staticmethod
    def _assign_attribute_value(attributes: Dict[str, Any], attribute: int, value: Any):
        attribute_name = _DAQMX_ATTRIBUTES[attribute]
        attributes[attribute_name] = value


class _ConstantsForMockInterpreters(Enum):
    DC_RMS_VOLTAGE_MEASUREMENT_INCERTAINTY = 0.01
    DC_RMS_CURRENT_MEASUREMENT_INCERTAINTY = 0.001
    POWER_SUPPLY_SOURCE_AND_MEASURE_INCERTAINTY = 0.001


class _InterpreterDcRmsCurrentMeasurement(_MockInterpreter):
    """Defines interpreter used for DC-RMS Voltage Measurement."""

    def read_analog_f64(self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        channels_characteristics = [
            channel_characteristics
            for _, channel_characteristics in self._analog_input_channels.items()
        ]

        # retrieve the smallest maximum voltage from channel(s)
        max_current_range = min(
            [
                channel_characteristics[_ConstantsForMockDAQmx.MAX_VAL]
                for channel_characteristics in channels_characteristics
            ]
        )

        for index_row in range(0, len(channels_characteristics)):
            # Build a current value between 0 and max_voltage_range.
            current_value = random.random() * max_current_range

            # assign a voltage value = voltage_value +/- 0.001
            for index_col in range(0, self._timing[_ConstantsForMockDAQmx.SAMP_PER_CHAN]):
                read_array[index_row, index_col] = (
                    current_value
                    - _ConstantsForMockInterpreters.DC_RMS_CURRENT_MEASUREMENT_INCERTAINTY.value
                    / 2.0
                    + random.random()
                    * _ConstantsForMockInterpreters.DC_RMS_CURRENT_MEASUREMENT_INCERTAINTY.value
                )
        return read_array, num_samps_per_chan


class _InterpreterDcRmsVoltageMeasurement(_MockInterpreter):
    """Defines interpreter used for DC-RMS Voltage Measurement."""

    def read_analog_f64(self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        channels_characteristics = [
            channel_characteristics
            for _, channel_characteristics in self._analog_input_channels.items()
        ]

        # retrieve the smallest maximum voltage from channel(s)
        max_voltage_range = min(
            [
                channel_characteristics[_ConstantsForMockDAQmx.MAX_VAL]
                for channel_characteristics in channels_characteristics
            ]
        )

        for index_row in range(0, len(channels_characteristics)):
            # Build a voltage value between 0 and max_voltage_range.
            voltage_value = random.random() * max_voltage_range

            # assign a voltage value = voltage_value +/- 0.01
            for index_col in range(0, self._timing[_ConstantsForMockDAQmx.SAMP_PER_CHAN]):
                read_array[index_row, index_col] = (
                    voltage_value
                    - _ConstantsForMockInterpreters.DC_RMS_VOLTAGE_MEASUREMENT_INCERTAINTY.value
                    / 2.0
                    + random.random()
                    * _ConstantsForMockInterpreters.DC_RMS_VOLTAGE_MEASUREMENT_INCERTAINTY.value
                )
        return read_array, num_samps_per_chan


class _InterpreterPowerSupplySourceAndMeasure(_MockInterpreter):
    """Defines interpreter used for Power Supply Source And Measure."""

    def read_power_f64(
        self,
        task,
        num_samps_per_chan,
        timeout,
        fill_mode,
        read_voltage_array,
        read_current_array,
    ):
        channel_characteristics = next(
            channel_characteristics
            for _, channel_characteristics in self._analog_input_channels.items()
        )
        voltage_setpoint = channel_characteristics[_ConstantsForMockDAQmx.VOLTAGE_SETPOINT]
        current_setpoint = channel_characteristics[_ConstantsForMockDAQmx.CURRENT_SETPOINT]
        for index in range(0, self._timing[_ConstantsForMockDAQmx.SAMP_PER_CHAN]):
            read_voltage_array[index] = (
                voltage_setpoint
                - _ConstantsForMockInterpreters.POWER_SUPPLY_SOURCE_AND_MEASURE_INCERTAINTY.value
                / 2.0
                + random.random()
                * _ConstantsForMockInterpreters.POWER_SUPPLY_SOURCE_AND_MEASURE_INCERTAINTY.value
            )
            read_current_array[index] = (
                current_setpoint
                - _ConstantsForMockInterpreters.POWER_SUPPLY_SOURCE_AND_MEASURE_INCERTAINTY.value
                / 2.0
                + random.random()
                * _ConstantsForMockInterpreters.POWER_SUPPLY_SOURCE_AND_MEASURE_INCERTAINTY.value
            )
        return read_voltage_array, read_current_array, num_samps_per_chan
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library_core/daq/_mock_daqmx/_mock_daqmx_task.py sha256=bd6bd23be9737fbeaae3387218f4cea4f37d6b417e47198eee7a769593db512d bytes=1735 -->
## FILE: src/nipcbatt/pcbatt_library_core/daq/_mock_daqmx/_mock_daqmx_task.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library_core/daq/_mock_daqmx/_mock_daqmx_task.py`
- sha256: `bd6bd23be9737fbeaae3387218f4cea4f37d6b417e47198eee7a769593db512d`
- bytes: 1735

````python
# pylint: disable=W0231, W0221
"""Simulation of DAQmx implementation."""
import nidaqmx
import nidaqmx.constants
import nidaqmx.system.system
import nidaqmx.utils


class _MockSystem(nidaqmx.system.system.System):
    """Defines methods used to discover mock instruments."""

    def __init__(self, interpreter):
        self._interpreter = interpreter

    @staticmethod
    def local(interpreter):
        """
        nidaqmx.system.system.System: Represents the local DAQmx system.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        return _MockSystem(interpreter=interpreter)


class _MockTask(nidaqmx.Task):
    """Defines methods used to simulate instruments though DAQmx tasks."""

    def __init__(self, new_task_name="", *, interpreter=None):
        self._close_on_exit = False
        self._saved_name = new_task_name  # _initialize sets this to the name assigned by DAQmx.
        self._grpc_options = None
        self._event_handlers = {}

        # assign a custom interpreter.
        self._interpreter = interpreter
        self._handle, self._close_on_exit = self._interpreter.create_task(new_task_name)

        self._initialize(self._handle, self._interpreter)

    def close(self):
        """
        Clears the task.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        if self._handle is None:
            return

        self._interpreter.clear_task(self._handle)
        self._handle = None
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library_core/daq/_mock_daqmx/_mock_daqmx_utilities.py sha256=109b1b5ae7c2f1f835327633f33c4d80d9308032cdb95eadf6714ee8dd112b1d bytes=2890 -->
## FILE: src/nipcbatt/pcbatt_library_core/daq/_mock_daqmx/_mock_daqmx_utilities.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library_core/daq/_mock_daqmx/_mock_daqmx_utilities.py`
- sha256: `109b1b5ae7c2f1f835327633f33c4d80d9308032cdb95eadf6714ee8dd112b1d`
- bytes: 2890

````python
"""Provides a set of higher order function utilities related to daqmx."""

import logging
from typing import Type

import nidaqmx
import nidaqmx.errors
import nidaqmx.system.system

from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_task import (
    _MockSystem,
    _MockTask,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_utilities.reflection_utilities import substitute_method


def _replace_daqmx(interpreter_class: Type):
    """Substitutes mock version of nidaqmx in Building block class.

    Args:
        interpreter_class (Type): Class of interpreter to use in mock version.
    """

    def _instrument_factory() -> _MockTask:
        logging.debug("Using mock version of nidaqmx.Task")
        return _MockTask(interpreter=interpreter_class())

    def _daqmx_local_system() -> _MockSystem:
        return _MockSystem.local(interpreter=interpreter_class())

    substitute_method(
        cls=BuildingBlockUsingDAQmx,
        method=_instrument_factory,
        method_name="_instrument_factory",
    )

    substitute_method(
        cls=BuildingBlockUsingDAQmx,
        method=_daqmx_local_system,
        method_name="_daqmx_local_system",
    )


def _replace_daqmx_if_not_installed(interpreter_class: Type):
    """Substitutes mock version of nidaqmx in Building block class
    if nidaqmx in not installed on local system.
    Args:
        interpreter_class (Type): Class of interpreter to use in mock version.
    """  # noqa: D202, D205, D411, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Missing blank line before section (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (269 > 100 characters) (auto-generated noqa)

    def _instrument_factory() -> nidaqmx.Task:
        try:
            task = nidaqmx.Task()
            logging.debug("Using nidaqmx.Task")
            return task
        except nidaqmx.errors.DaqNotFoundError:
            logging.debug("Using mock version of nidaqmx.Task")
            return _MockTask(interpreter=interpreter_class())

    def _daqmx_local_system() -> nidaqmx.system.system.System:
        try:
            print(nidaqmx.system.system.System.local().driver_version)
            return nidaqmx.system.system.System.local()
        except nidaqmx.errors.DaqNotFoundError:
            return _MockSystem.local(interpreter=interpreter_class())

    substitute_method(
        cls=BuildingBlockUsingDAQmx,
        method=_instrument_factory,
        method_name="_instrument_factory",
    )

    substitute_method(
        cls=BuildingBlockUsingDAQmx,
        method=_daqmx_local_system,
        method_name="_daqmx_local_system",
    )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library_core/daq/pcbatt_building_blocks.py sha256=0860b8dad33ba2af6469ddf9e113f3e2fe03b3ee1fee1b1565738547e53eb2c7 bytes=16352 -->
## FILE: src/nipcbatt/pcbatt_library_core/daq/pcbatt_building_blocks.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library_core/daq/pcbatt_building_blocks.py`
- sha256: `0860b8dad33ba2af6469ddf9e113f3e2fe03b3ee1fee1b1565738547e53eb2c7`
- bytes: 16352

````python
# pylint: disable=W0707, W0719, W0702
"""Defines the base classes used by PCBA Test Toolkit building blocks"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (183 > 100 characters) (auto-generated noqa)

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Callable, Optional

import nidaqmx
import nidaqmx.constants
import nidaqmx.system
import nidaqmx.system.storage.persisted_channel
import nidaqmx.utils
import pyvisa
import niswitch
import nidmm
import nidcpower

from nipcbatt.pcbatt_communication_library.ni_845x_i2c_communication_devices import (
    Ni845xI2cDevicesHandler,
)
from nipcbatt.pcbatt_communication_library.ni_845x_spi_communication_devices import (
    Ni845xSpiDevicesHandler,
)
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryChannelNotCompatibleWithGenerationException,
    PCBATTLibraryChannelNotCompatibleWithMeasurementException,
    PCBATTLibraryException,
)
from nipcbatt.pcbatt_library_core.pcbatt_library_messages import (
    PCBATTLibraryExceptionMessages,
)


class BuildingBlockUsingInstrument(ABC):
    """Defines the base methods for initialization and release"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (176 > 100 characters) (auto-generated noqa)

    def __init__(self, *args, **kwargs):
        """Constructor that initializes instrument."""
        self._instrument = self.__class__._instrument_factory()
        self._initialize(*args, **kwargs)

    def __enter__(self):
        """Magic method called when 'with' is called."""
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        """Magic method called at end of 'with' is call block."""
        self._close()

    def __del__(self):
        """Destructor that calls _close() method."""
        self._close()

    @classmethod
    @abstractmethod
    def _instrument_factory(cls):
        """Initializes the instrument.

        Raises:
            NotImplementedError: raised when cleared directly.
        """
        raise NotImplementedError()

    def _initialize(self, *args, **kwargs):
        if len(args) == 0:
            return

        self._invoke("initialize", *args, **kwargs)

    def _close(self):
        try:
            self._invoke("close")
        finally:
            if hasattr(self, "_instrument"):
                del self._instrument

    def _invoke(self, method_name: str, *args, **kwargs):
        try:
            method = getattr(self, method_name)

            if isinstance(method, Callable):
                method(*args, **kwargs)
        except AttributeError as exception:
            raise PCBATTLibraryException(
                PCBATTLibraryExceptionMessages.CLASS_DOES_NOT_IMPLEMENT_METHOD_ARGS_2.format(
                    type(self).__name__, method_name
                )
            ) from exception


class BuildingBlockUsingNISWITCH(BuildingBlockUsingInstrument):
    """Defines building block that uses NI-SWITCH for switch matrix routing"""

    @classmethod
    def _instrument_factory(cls) -> Optional[niswitch.Session]:
        """Creates a placeholder for an NI-SWITCH session

        Returns:
            Optional[niswitch.Session]: None until user calls initialize() to open the session
        """
        return None
    
    @property
    def is_session_initialized(self) -> bool:
        """ Checks if an NI-SWITCH session has been opened.

        Returns:
            bool: True if the NI-SWITCH session is open
        """
        return self._instrument is not None
    
    @property
    def session(self) -> niswitch.Session:
        """Defines the instance of the NI_SWITCH session.
        
        Returns:
            niswitch.Session: the type of instrument
        """
        if self._instrument is None:
            raise RuntimeError(
                "NI-SWITCH session is not initialized. \n"
                "Call initialize() on derived building block"
            )
        return self._instrument
    
class BuildingBlockUsingNIDMM(BuildingBlockUsingInstrument):
    """Defines building block that uses NI-DMM for instrument measurements."""

    @classmethod
    def _instrument_factory(cls) -> Optional[nidmm.Session]:
        """Creates a placeholder for an NI-DMM session.

        Returns:
            Optional[nidmm.Session]: None until initialize() opens the session.
        """
        return None

    @property
    def is_session_initialized(self) -> bool:
        """Checks whether an NI-DMM session has been opened.

        Returns:
            bool: True if the NI-DMM session is open.
        """
        return self._instrument is not None

    @property
    def session(self) -> nidmm.Session:
        """Defines the instance of the NI-DMM session.

        Returns:
            nidmm.Session: the instrument session.

        Raises:
            PCBATTLibraryException: if the session has not been initialized.
        """
        if self._instrument is None:
            raise PCBATTLibraryException(
                "NI-DMM session is not initialized. \n"
                "Call initialize() on the derived building block."
            )
        return self._instrument

class BuildingBlockUsingNIDCPower(BuildingBlockUsingInstrument):
    """Defines building block that uses NI-DCPower for DC power sourcing and measurement."""

    @classmethod
    def _instrument_factory(cls) -> Optional[nidcpower.Session]:
        """Creates a placeholder for an NI-DCPower session.

        Returns:
            Optional[nidcpower.Session]: None until initialize() opens the session.
        """
        return None

    @property
    def is_session_initialized(self) -> bool:
        """Checks whether an NI-DCPower session has been opened.

        Returns:
            bool: True if the NI-DCPower session is open.
        """
        return self._instrument is not None

    @property
    def session(self) -> nidcpower.Session:
        """Defines the instance of the NI-DCPower session.

        Returns:
            nidcpower.Session: the instrument session.

        Raises:
            PCBATTLibraryException: if the session has not been initialized.
        """
        if self._instrument is None:
            raise PCBATTLibraryException(
                "NI-DCPower session is not initialized. \n"
                "Call initialize() on the derived building block."
            )
        return self._instrument


class BuildingBlockUsingDAQmx(BuildingBlockUsingInstrument):
    """Defines Building block that uses DAQmx task for instrument management."""

    @classmethod
    def _instrument_factory(cls) -> nidaqmx.Task:
        """Creates a DAQmx task instance.
        Returns:
            nidaqmx.Task: the type of instrument.
        """  # noqa: D205, D411, W505 - 1 blank line required between summary line and description (auto-generated noqa), Missing blank line before section (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
        return nidaqmx.Task()

    @property
    def is_task_initialized(self) -> bool:
        """Checks whether the task is initialized.

        Returns:
            bool: True, if the task is initialized with channel(s)
        """
        task_is_initialized: bool = False
        try:
            task_is_initialized = len(self.task.channel_names) != 0
        finally:
            return task_is_initialized

    @property
    def task(self) -> nidaqmx.Task:
        """Defines the instance of DAQmx task.

        Returns:
            nidaqmx.Task: the type of instrument.
        """
        return self._instrument

    def contains_only_global_virtual_channels(self, channel_expression: str) -> bool:
        """Check whether the channel expression contains
           only global virtual channels defined in NI MAX.
        Args:
            channel_expression (str): the channel expression

        Returns:
            bool: True if the channel expression
            only contains global virtual channels defined in NI MAX.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        channel_names_in_expression = nidaqmx.utils.unflatten_channel_string(
            channel_names=channel_expression
        )

        global_channel_names = (
            self.__class__._daqmx_local_system().global_channels.global_channel_names
        )

        return all(
            channel_name in global_channel_names for channel_name in channel_names_in_expression
        )

    @classmethod
    def _daqmx_local_system(cls) -> nidaqmx.system.System:
        """Gets the local DAQmx system.

        Returns:
            nidaqmx.system.System: The instance of the local DAQmx system.
        """
        return nidaqmx.system.System.local()

    def verify_measurement_type(self, measurement_type: nidaqmx.constants.UsageTypeAI):
        """Verifies the DAQ handler channels are compatible with the measurement type.

        Args:
            measurement_type (nidaqmx.constants.UsageTypeAI): type of the measurement.
        """
        if all(channel.ai_meas_type == measurement_type for channel in self.task.ai_channels):
            return

        raise PCBATTLibraryChannelNotCompatibleWithMeasurementException(measurement_type)

    def verify_generation_type(self, generation_type: nidaqmx.constants.UsageTypeAO):
        """Verifies the DAQ handler channels are compatible with the generation type.

        Args:
            generation_type (nidaqmx.constants.UsageTypeAI): type of the generation.
        """
        if all(channel.ao_output_type == generation_type for channel in self.task.ai_channels):
            return

        raise PCBATTLibraryChannelNotCompatibleWithGenerationException(generation_type)

    def add_global_channels(self, global_channel_expression: str):
        """Add global channels (defined in the channel expression)
        to the DAQmx task.

        Args:
            global_channel_expression (str):
                Expression representing the name of
                a global channel in DAQ System.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        global_channels_names = nidaqmx.utils.unflatten_channel_string(
            channel_names=global_channel_expression
        )
        self.task.add_global_channels(
            [
                nidaqmx.system.storage.persisted_channel.PersistedChannel(global_channel_name)
                for global_channel_name in global_channels_names
            ]
        )


class BuildingBlockUsingNi845xI2cDevice(BuildingBlockUsingInstrument):
    """Defines building block that uses NI-845x devices handler for I2C communication."""

    @classmethod
    def _instrument_factory(cls) -> Ni845xI2cDevicesHandler:
        """Creates a NI-845x I2C device handler.
        Returns:
            Ni845xI2cDevicesHandler: the type of instrument.
        """  # noqa: D205, D411, W505 - 1 blank line required between summary line and description (auto-generated noqa), Missing blank line before section (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
        return Ni845xI2cDevicesHandler()

    @property
    def is_devices_handler_initialized(self) -> bool:
        """Checks whether the device handler is initialized.

        Returns:
            bool: True, if the device handler is initalized.
        """
        return self.devices_handler.is_initialized()

    @property
    def devices_handler(self) -> Ni845xI2cDevicesHandler:
        """Defines the instance of devices handler.

        Returns:
            Ni845xI2cDevicesHandler: the type of instrument.
        """
        return self._instrument


class BuildingBlockUsingNi845xSpiDevice(BuildingBlockUsingInstrument):
    """Defines building block that uses NI-845x devices handler for SPI communication."""

    @classmethod
    def _instrument_factory(cls) -> Ni845xSpiDevicesHandler:
        """Creates a NI 845x device handler.
        Returns:
            Ni845xSpiDevicesHandler: the type of instrument.
        """  # noqa: D205, D411, W505 - 1 blank line required between summary line and description (auto-generated noqa), Missing blank line before section (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
        return Ni845xSpiDevicesHandler()

    @property
    def is_devices_handler_initialized(self) -> bool:
        """Checks whether the devices handler is initialized.

        Returns:
            bool: True, if the devices handler is initalized.
        """
        return self.devices_handler.is_initialized()

    @property
    def devices_handler(self) -> Ni845xSpiDevicesHandler:
        """Defines the instance of device handler.

        Returns:
            Ni845xSpiDevicesHandler: the type of instrument.
        """
        return self._instrument


class BuildingBlockUsingVisa(BuildingBlockUsingInstrument):
    """Defines Building block that uses
    serial device handler (NI-VISA) for instrument management."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (358 > 100 characters) (auto-generated noqa)

    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self._serial_device_handler = None

    @classmethod
    def _instrument_factory(cls) -> pyvisa.ResourceManager:
        """Creates a NI-VISA resource manager.
        Returns:
            pyvisa.ResourceManager: the type of resource manager.
        """  # noqa: D205, D411, W505 - 1 blank line required between summary line and description (auto-generated noqa), Missing blank line before section (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
        return pyvisa.ResourceManager()

    @property
    def is_serial_device_handler_initialized(self) -> bool:
        """Checks whether the serial device handler is initialized.

        Returns:
            bool: True, if the serial device handler is initialized.
        """
        return self._serial_device_handler is not None

    @property
    def serial_device_handler(self) -> pyvisa.resources.SerialInstrument:
        """Defines the instance of device handler.

        Returns:
            pyvisa.resources.SerialInstrument: the type of instrument.
        """
        if self._serial_device_handler is not None:
            return self._serial_device_handler

        raise PCBATTLibraryException(
            PCBATTLibraryExceptionMessages.VISA_SERIAL_DEVICE_NOT_INITIALIZED
        )

    def open_serial_device(self, serial_device_name: str):
        """Opens a serial device with the specific name.

        Args:
            serial_device_name (str): The name of the serial device.
        """
        self._serial_device_handler = self._instrument.open_resource(serial_device_name)

    def close_serial_device(self):
        """Closes the serial device."""
        self._serial_device_handler.close()
        self._serial_device_handler = None
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library_core/pcbatt_data_types.py sha256=5ef5cc3cb09310d55d8267a88c8ec2c5a0e8bfe1b64fc2eeadc52c204f2804d1 bytes=2525 -->
## FILE: src/nipcbatt/pcbatt_library_core/pcbatt_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library_core/pcbatt_data_types.py`
- sha256: `5ef5cc3cb09310d55d8267a88c8ec2c5a0e8bfe1b64fc2eeadc52c204f2804d1`
- bytes: 2525

````python
# pylint: disable=W0707, W0719, W0702, W0212
"""Defines the base classes used by PCBA Test Toolkit data types"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (178 > 100 characters) (auto-generated noqa)

import json

from nipcbatt.pcbatt_utilities.reflection_utilities import (
    convert_for_json_serialization,
    enumerate_properties,
)


class PCBATestToolkitData:
    """Base class that defines methods for all building block data."""

    def __repr__(self) -> str:
        """Called when repr() is invoked on the `PCBATestToolkitData`object

        Returns:
            str: The string representing the object.
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        return self._to_json_representation()

    def __str__(self) -> str:
        """Called when str() is invoked on the `PCBATestToolkitData`object

        Returns:
            str: The string representing the object.
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        return self._to_json_representation()

    def __eq__(self, value_to_compare: object) -> bool:
        """instances equality.

        Args:
            value_to_compare (object): the instance of `PCBATestToolkitData` to compare.

        Returns:
            bool: True if equals to `value_to_compare`
                (e.g. all properties defined in self object are equal to those of value_to_compare).
        """  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        if isinstance(value_to_compare, self.__class__):
            return all(
                property_value == property_value_of_value_to_compare
                for (_, property_value), (_, property_value_of_value_to_compare) in zip(
                    enumerate_properties(self), enumerate_properties(value_to_compare)
                )
            )

        return False

    def _to_json_representation(self) -> str:
        return json.dumps(
            convert_for_json_serialization(self),
            indent=4,
        ).replace("\\n", "\n")
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library_core/pcbatt_library_exceptions.py sha256=73807076e18aebf3f9fe565ba450391aac5834993ddb3eca9ad080e66814bc4f bytes=3034 -->
## FILE: src/nipcbatt/pcbatt_library_core/pcbatt_library_exceptions.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library_core/pcbatt_library_exceptions.py`
- sha256: `73807076e18aebf3f9fe565ba450391aac5834993ddb3eca9ad080e66814bc4f`
- bytes: 3034

````python
# pylint: disable=W0707, W0719, W0702, W0212
"""Defines the exceptions that can be raised during execution of PCBA Test Toolkit"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (196 > 100 characters) (auto-generated noqa)

import nidaqmx.constants

from nipcbatt.pcbatt_library_core.pcbatt_library_messages import (
    PCBATTLibraryExceptionMessages,
)


class PCBATTLibraryException(  # noqa: N818 - exception name 'PCBATTLibraryException' should be named with an Error suffix (auto-generated noqa)
    Exception
):
    """Defines base class for all exception raised by
    `nipcatt.pcbatt_library` and `nipcatt.pcbatt_library_core` modules."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (367 > 100 characters) (auto-generated noqa)

    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self, message: str
    ):
        super().__init__(message)


class PCBATTLibraryChannelNotCompatibleWithMeasurementException(  # noqa: N818 - exception name 'PCBATTLibraryChannelNotCompatibleWithMeasurementException' should be named with an Error suffix (auto-generated noqa)
    PCBATTLibraryException
):
    """Raised if the global virtual channels are not compatible with the type of measurement."""

    def __init__(
        self,
        measurement_type: nidaqmx.constants.UsageTypeAI,
    ) -> None:
        """Initializes an instance of `PCBATTLibraryChannelNotCompatibleWithMeasurementException`.

        Args:
            measurement_type (nidaqmx.constants.UsageTypeAI): The type of measurement.
        """
        super().__init__(
            PCBATTLibraryExceptionMessages.ANALOG_INPUT_CHANNEL_NOT_COMPATIBLE_WITH_MEASUREMENT_ARGS_1.format(
                measurement_type.name
            )
        )


class PCBATTLibraryChannelNotCompatibleWithGenerationException(  # noqa: N818 - exception name 'PCBATTLibraryChannelNotCompatibleWithGenerationException' should be named with an Error suffix (auto-generated noqa)
    PCBATTLibraryException
):
    """Raised if the global virtual channels are not compatible with the type of generation."""

    def __init__(
        self,
        measurement_type: nidaqmx.constants.UsageTypeAO,
    ) -> None:
        """Initializes an instance of `PCBATTLibraryChannelNotCompatibleWithGenerationException`.

        Args:
            measurement_type (nidaqmx.constants.UsageTypeAO): The type of generation.
        """
        super().__init__(
            PCBATTLibraryExceptionMessages.ANALOG_INPUT_CHANNEL_NOT_COMPATIBLE_WITH_MEASUREMENT_ARGS_1.format(
                measurement_type.name
            )
        )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library_core/pcbatt_library_messages.py sha256=31781fdb4a22bf6f1116f62ef847e098bcd8b173472ccc296f6a42d4578f0856 bytes=1832 -->
## FILE: src/nipcbatt/pcbatt_library_core/pcbatt_library_messages.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library_core/pcbatt_library_messages.py`
- sha256: `31781fdb4a22bf6f1116f62ef847e098bcd8b173472ccc296f6a42d4578f0856`
- bytes: 1832

````python
"""Module containing message strings."""


class PCBATTLibraryExceptionMessages:
    """Messages used in exception classes."""

    ANALOG_INPUT_CHANNEL_NOT_COMPATIBLE_WITH_MEASUREMENT_ARGS_1 = (
        "The analog input channel is not compatible with the specific measurement ({})."
    )

    ANALOG_OUTPUT_CHANNEL_NOT_COMPATIBLE_WITH_MEASUREMENT_ARGS_1 = (
        "The analog output channel is not compatible with the specific generation ({})."
    )

    CLASS_DOES_NOT_IMPLEMENT_METHOD_ARGS_2 = "The class {} does not implement the method {}."

    VISA_SERIAL_DEVICE_NOT_INITIALIZED = "VISA serial instrument not initialized"

    SECOND_ARGUMENT_OF_TYPE_INT_FLOAT_OR_STRING = (
        "Second argument must be a int or float value"
        + " for cold-junction compensation value,"
        + " or a string for cold-junction compensation channel name"
    )

    INVALID_NUMPY_ARRAY_TYPE_ARGS_1 = "The type of the numpy array is not of {}."

    GLOBAL_CHANNEL_PORT_NOT_SUPPORTED_ARGS_3 = (
        "Global Channel Port is not supported. {} represents a port with a width of {}. "
        + "Specify a range of digital lines, such as '{}/line0:31' as the global channel"
    )

    PHYSICAL_CHANNEL_PORT_NOT_SUPPORTED_ARGS_3 = (
        "Physical Channel Port is not supported. '{}' represents a port with a width of {}."
        + "Specify a range of digital lines, such as '{}/line0:31' as the physical channel"
    )

    MORE_THAN_ONE_CHANNEL_INVALID = "Multiple channels are not allowed for counter tasks."

    GLOBAL_CHANNEL_TOO_MANY_MODULES_ARGS_1 = (
        "Global channels input is invalid because multiple module global channels were"
        + "listed in the string. Global channels are supported only from a single module."
        + "\n Modules Listed: {}"
    )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/__init__.py sha256=1426145ca5f3cd6d9c0fd0891e7b2a053cf97ae5b25618bcb42aa9f65b54cd6d bytes=224 -->
## FILE: src/nipcbatt/pcbatt_utilities/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_utilities/__init__.py`
- sha256: `1426145ca5f3cd6d9c0fd0891e7b2a053cf97ae5b25618bcb42aa9f65b54cd6d`
- bytes: 224

````python
"""Provides a set of utilities modules"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (152 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/csv_utilities.py sha256=4b77e73a02083f34a4d8b269e0b83bda42fc96885a5474f4781cdac2e4f4b2b5 bytes=5885 -->
## FILE: src/nipcbatt/pcbatt_utilities/csv_utilities.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_utilities/csv_utilities.py`
- sha256: `4b77e73a02083f34a4d8b269e0b83bda42fc96885a5474f4781cdac2e4f4b2b5`
- bytes: 5885

````python
"""Provides a set of csv related routines."""

import os
from typing import Iterable

import numpy
import pandas
from varname import nameof

from nipcbatt.pcbatt_utilities.guard_utilities import Guard


def export_signal_to_csv_file(
    signal_csv_file_path: str,
    signal_samples: Iterable[float],
    signal_sampling_rate: float,
    x_axis_name: str,
    y_axis_name: str,
):
    """Exports a sequence of float elements into a csv file as a signal.

    Args:
        signal_csv_file_path (str): path where csv file will be placed.
        signal_samples (Iterable[float]): content of the second column.
        signal_sampling_rate (float): sampling rate of the signal,
            will be used to infere content of the second column.
        x_axis_name (str): name of the first column.
        y_axis_name (str): name of the second column.
    Raises:
        ValueError: is raised when one of the provided
            argument is not supported.
    """  # noqa: D411 - Missing blank line before section (auto-generated noqa)
    Guard.is_not_none(signal_csv_file_path, nameof(signal_csv_file_path))
    Guard.is_not_empty(signal_csv_file_path, nameof(signal_csv_file_path))
    Guard.is_not_none(signal_samples, nameof(signal_samples))
    Guard.is_greater_than_zero(signal_sampling_rate, nameof(signal_sampling_rate))

    Guard.is_not_none(x_axis_name, nameof(x_axis_name))
    Guard.is_not_empty(x_axis_name, nameof(x_axis_name))
    Guard.is_not_none(y_axis_name, nameof(y_axis_name))
    Guard.is_not_empty(y_axis_name, nameof(y_axis_name))

    signal_dates = [
        sample_index / signal_sampling_rate for sample_index in range(0, len(signal_samples))
    ]

    return export_columns_to_csv_file(
        csv_file_path=signal_csv_file_path,
        column1_data=signal_dates,
        column2_data=signal_samples,
        column1_name=x_axis_name,
        column2_name=y_axis_name,
    )


def export_columns_to_csv_file(
    csv_file_path: str,
    column1_data: Iterable[float],
    column2_data: Iterable[float],
    column1_name: str,
    column2_name: str,
):
    """Exports two columns of float elements into a csv file.

    Args:
        csv_file_path (str): path where csv file will be placed.
        column1_data (Iterable[float]): content of the first column.
        column2_data (Iterable[float]): content of the second column.
        column1_name (str): name of the first column.
        column2_name (str): name of the second column.
    Raises:
        ValueError: is raised when one of the provided
            argument is not supported.
    """  # noqa: D411 - Missing blank line before section (auto-generated noqa)
    Guard.is_not_none(csv_file_path, nameof(csv_file_path))
    Guard.is_not_empty(csv_file_path, nameof(csv_file_path))
    Guard.is_not_none(column1_data, nameof(column1_data))
    Guard.is_not_empty(column2_data, nameof(column2_data))
    Guard.is_not_none(column1_name, nameof(column1_name))
    Guard.is_not_empty(column2_name, nameof(column2_name))

    Guard.have_same_size(
        first_iterable_instance=column1_data,
        first_iterable_name=nameof(column1_data),
        second_iterable_instance=column2_data,
        second_iterable_name=nameof(column2_data),
    )

    write_data_frame: pandas.DataFrame = pandas.DataFrame(
        data={column1_name: column1_data, column2_name: column2_data}
    )
    write_data_frame.to_csv(path_or_buf=csv_file_path, index=False, sep=";")


def import_from_csv_file_2d_array(
    csv_file_path: str, header_is_present: bool, column_delimiter=";"
) -> tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64]]:
    """Imports from a csv file located at a given path a 2D array.

    Args:
        csv_file_path (str): path of the csv file.
        header_is_present (bool): indicates if csv file headers are present.

    Raises:
        ValueError: is raised when provided file path does not exist.
        IOError: is raised when csv file parsing fails for some reason.
        TypeError:
            is raised when csv file parsing succeeded but data conversion into 2D array fails.

    Returns:
        tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64]]:
            tuple first array represents first column of the csv file
            tuple second array represents second column of the csv file.
    """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

    Guard.is_not_none(csv_file_path, nameof(csv_file_path))
    Guard.is_not_empty(csv_file_path, nameof(csv_file_path))

    if not os.path.exists(csv_file_path):
        raise ValueError(f"{nameof(csv_file_path)} ('{csv_file_path}') does not exist!")

    read_data_frame: pandas.DataFrame = None

    try:
        if header_is_present:
            read_data_frame = pandas.read_csv(
                filepath_or_buffer=csv_file_path,
                delimiter=column_delimiter,
                header="infer",
            )
        else:
            read_data_frame = pandas.read_csv(
                filepath_or_buffer=csv_file_path,
                delimiter=column_delimiter,
                header=None,
            )
    except Exception as e:
        raise IOError("Import of csv file failed for some reason!") from e

    try:
        column_1: numpy.ndarray[numpy.float64] = (
            read_data_frame[read_data_frame.columns[0]].astype(numpy.float64).array.to_numpy()
        )
        column_2: numpy.ndarray[numpy.float64] = (
            read_data_frame[read_data_frame.columns[1]].astype(numpy.float64).array.to_numpy()
        )

        return (column_1, column_2)
    except Exception as e:
        raise TypeError("Import of csv file failed due to data conversion error!") from e
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/file_utilities.py sha256=91e4b32203c27f70c17d1ec7edc3d5d2689cd6accc170024617a5ece6e493cfd bytes=2931 -->
## FILE: src/nipcbatt/pcbatt_utilities/file_utilities.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_utilities/file_utilities.py`
- sha256: `91e4b32203c27f70c17d1ec7edc3d5d2689cd6accc170024617a5ece6e493cfd`
- bytes: 2931

````python
""" Provides a set of file utilities routines."""

import os
from collections.abc import Iterable

from varname import nameof

from nipcbatt.pcbatt_utilities.guard_utilities import Guard


def write_lines(text_file_path: str, text_file_encoding: str, text_lines: Iterable[str]):
    """Writes lines into a text file, input example ["line1", "line2", "line3"].

    Args:
        text_file_path (str): text file path.
        text_file_encoding (str): text file encoding.
        text_lines (Iterable[str]): text file lines.

    Raises:
        ValueError: occurs when one of the input arguments is None or empty string.
        IOError: occurs when reading text file fails for some reason.
    """
    Guard.is_not_none(instance=text_file_path, instance_name=nameof(text_file_path))
    Guard.is_not_empty(iterable_instance=text_file_path, instance_name=nameof(text_file_path))
    Guard.is_not_none(instance=text_lines, instance_name=nameof(text_lines))
    Guard.is_not_empty(iterable_instance=text_lines, instance_name=nameof(text_lines))

    try:
        with open(file=text_file_path, mode="w", encoding=text_file_encoding) as text_file:
            text_file.writelines(map(lambda line: f"{line}\n", text_lines))
    except Exception as e:
        raise IOError("Write text file failed for some reason!") from e


def read_lines(text_file_path: str, text_file_encoding: str) -> Iterable[str]:
    """Reads lines of a text file in a lazy way.

    Args:
        text_file_path (str): text file path.
        text_file_encoding (str): text file encoding.

    Raises:
        ValueError: occurs when one of the input arguments is None or empty string.
        IOError: occurs when reading text file fails for some reason.

    Returns:
        Iterable[str]: text file lines.

    Yields:
        Iterator[Iterable[str]]: text file lines exposed through iterator.
    """
    Guard.is_not_none(instance=text_file_path, instance_name=nameof(text_file_path))
    Guard.is_not_empty(iterable_instance=text_file_path, instance_name=nameof(text_file_path))

    if not os.path.exists(text_file_path):
        raise ValueError(f"{nameof(text_file_path)} does not exist!")

    try:
        with open(file=text_file_path, mode="r", encoding=text_file_encoding) as text_file:
            for text_file_line in text_file:
                yield text_file_line.strip()
    except Exception as e:
        raise IOError("Read text file failed for some reason!") from e


def file_exists(relative_or_absolute_file_path: str) -> bool:
    """Checks if a file exists.

    Raises:
        ValueError: occurs when one of the input arguments is None or empty string.
    """
    Guard.is_not_none_nor_empty_nor_whitespace(
        relative_or_absolute_file_path, nameof(relative_or_absolute_file_path)
    )

    return os.path.exists(relative_or_absolute_file_path)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/functional_utilities.py sha256=b979a460ba9875efe2a328e8e745db6680f90d95d699eb2c51b1891ab6ac9080 bytes=809 -->
## FILE: src/nipcbatt/pcbatt_utilities/functional_utilities.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_utilities/functional_utilities.py`
- sha256: `b979a460ba9875efe2a328e8e745db6680f90d95d699eb2c51b1891ab6ac9080`
- bytes: 809

````python
""" Provides a set of higher order function utilities routines."""


def repeat(times: int):
    """Returns a function which is repeated execution of inner function
       provided as argument.
    Args:
        times (int): number of times, function will be repeated.
    """  # noqa: D202, D205, D411, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Missing blank line before section (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (269 > 100 characters) (auto-generated noqa)

    def repeat_helper(f):
        def call_helper(*args):
            for _ in range(0, times):
                f(*args)

        return call_helper

    return repeat_helper
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/guard_utilities.py sha256=e9ed9c378b9b0aaf1974c8c628efa9e49e7f68c50ae72164eb8877da54d2b2d8 bytes=12320 -->
## FILE: src/nipcbatt/pcbatt_utilities/guard_utilities.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_utilities/guard_utilities.py`
- sha256: `e9ed9c378b9b0aaf1974c8c628efa9e49e7f68c50ae72164eb8877da54d2b2d8`
- bytes: 12320

````python
""" Provides a set of guard function utilities routines."""

from typing import Iterable, Type

from varname import nameof


class Guard:
    """Defines some methods used to validate arguments of functions."""

    NOT_ALL_ELEMENTS_OF_LIST_ARE_OF_TYPE_ARGS_1 = (
        "Not all elements of the list are of the type ({})."
    )

    ITERABLE_IS_EMPTY_ARGS_2 = "The iterable {} of type {} is empty."

    ITERABLES_HAVE_NOT_SAME_SIZE_ARGS_2 = "The iterables ({} and {}) do not have same size."

    ITERABLE_MUST_HAVE_ENOUGH_ELEMENTS_ARGS_2 = "The iterable {} must have at least {} elements."

    ITERABLE_MUST_CONTAIN_LESS_THAN_SPECIFIC_NUMBER_OF_ELEMENTS_ARGS_2 = (
        "The size of {} must less than or equal to {}."
    )

    VALUE_IS_NOT_INTEGER = "The value {} is not an integer."

    VALUE_IS_NOT_FLOAT = "The value {} is not a float."

    OBJECT_IS_NONE_ARGS_1 = "The object {} is None."

    VALUE_MUST_BE_LESS_THAN_ARGS_2 = "The value {} must be less than {}."

    VALUE_MUST_BE_LESS_THAN_OR_EQUAL_TO_ARGS_2 = "The value {} must be less than or equal to {}."

    VALUE_MUST_BE_GREATER_THAN_ARGS_2 = "The value {} must be greater than {}."

    VALUE_MUST_BE_GREATER_THAN_OR_EQUAL_TO_ARGS_2 = (
        "The value {} must be greater than or equal to {}."
    )

    VALUE_MUST_BE_WITHIN_LIMITS_INCLUDED = (
        "The value of {} must be greater than or equal to {} and less than or equal to {}."
    )

    VALUE_MUST_BE_WITHIN_LIMITS_EXCLUDED = (
        "The value of {} must be greater than {} and less than {}."
    )

    STRING_IS_NONE_OR_EMPTY_OR_WHITESPACE_ARGS_1 = (
        "The string value {} is None, empty or whitespace."
    )

    VALUE_IS_NOT_NUMERIC_ARGS_1 = "The object {} is not a numeric value."

    @staticmethod
    def all_elements_are_of_same_type(input_list: list, expected_type: Type):
        """Asserts that all elements of the the list are of same type.

        Args:
            input_list (List): The list to validate.
            expected_type (Type): The expected type.

        Raises:
            TypeError: Raised when some elements in the list are not of the expected type.
        """
        if all(isinstance(item, expected_type) for item in input_list):
            return

        raise TypeError(
            Guard.NOT_ALL_ELEMENTS_OF_LIST_ARE_OF_TYPE_ARGS_1.format(expected_type.__name__)
        )

    @staticmethod
    def is_not_none(instance: object, instance_name: str):
        """Asserts that the object is not None."""
        if (  # noqa: E714 - test for object identity should be 'is not' (auto-generated noqa)
            not instance is None
        ):
            return

        raise ValueError(Guard.OBJECT_IS_NONE_ARGS_1.format(instance_name))

    @staticmethod
    def is_not_int(value, value_name: str):
        """Ensures value is not an integer"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (156 > 100 characters) (auto-generated noqa)
        if isinstance(value, int):
            raise ValueError(Guard.VALUE_IS_NOT_INTEGER.format(value_name))

    @staticmethod
    def is_float(value, value_name: str):
        "Ensures value is a float"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (145 > 100 characters) (auto-generated noqa)
        if isinstance(value, float):
            return

        raise ValueError(Guard.VALUE_IS_NOT_FLOAT.format(value_name))

    @staticmethod
    def is_int(value, value_name: str):
        "Ensures value is an integer"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (148 > 100 characters) (auto-generated noqa)
        if isinstance(value, int):
            return

        raise ValueError(Guard.VALUE_IS_NOT_INTEGER.format(value_name))

    @staticmethod
    def is_not_float(value, value_name: str):
        """Ensures value is not a float"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (153 > 100 characters) (auto-generated noqa)
        if isinstance(value, float):
            raise ValueError(Guard.VALUE_IS_NOT_FLOAT.format(value_name))

    @staticmethod
    def is_greater_than_zero(value, value_name: str):
        """Asserts that the value is greater than zero."""
        Guard.is_greater_than(value=value, expected_smaller_value=0, value_name=value_name)

    @staticmethod
    def is_greater_than_or_equal_to_zero(value, value_name: str):
        """Asserts that the value is greater than or equal to zero."""
        Guard.is_greater_than_or_equal_to(
            value=value, expected_smaller_value=0, value_name=value_name
        )

    @staticmethod
    def is_less_than_zero(value, value_name: str):
        """Asserts that the value is less than to zero."""
        Guard.is_less_than(value=value, expected_greater_value=0, value_name=value_name)

    @staticmethod
    def is_less_than_or_equal_to_zero(value, value_name: str):
        """Asserts that the value is less than or equal to zero."""
        Guard.is_less_than_or_equal_to(value=value, expected_greater_value=0, value_name=value_name)

    @staticmethod
    def is_less_than(value, expected_greater_value, value_name: str):
        """Asserts that the value is less than expected greater value."""
        if not isinstance(value, (int, float)):
            raise TypeError(Guard.VALUE_IS_NOT_NUMERIC_ARGS_1.format(value_name))

        if not isinstance(expected_greater_value, (int, float)):
            raise TypeError(
                Guard.VALUE_IS_NOT_NUMERIC_ARGS_1.format(nameof(expected_greater_value))
            )

        if value < expected_greater_value:
            return

        raise ValueError(
            Guard.VALUE_MUST_BE_LESS_THAN_ARGS_2.format(value_name, expected_greater_value)
        )

    @staticmethod
    def is_less_than_or_equal_to(value, expected_greater_value, value_name: str):
        """Asserts that the value is less than expected greater value."""
        if not isinstance(value, (int, float)):
            raise TypeError(Guard.VALUE_IS_NOT_NUMERIC_ARGS_1.format(value_name))

        if not isinstance(expected_greater_value, (int, float)):
            raise TypeError(
                Guard.VALUE_IS_NOT_NUMERIC_ARGS_1.format(nameof(expected_greater_value))
            )

        if value <= expected_greater_value:
            return

        raise ValueError(
            Guard.VALUE_MUST_BE_LESS_THAN_OR_EQUAL_TO_ARGS_2.format(
                value_name, expected_greater_value
            )
        )

    @staticmethod
    def is_greater_than(value, expected_smaller_value, value_name: str):
        """Asserts that the value is greater than expected smaller value."""
        if not isinstance(value, (int, float)):
            raise TypeError(Guard.VALUE_IS_NOT_NUMERIC_ARGS_1.format(value_name))

        if not isinstance(expected_smaller_value, (int, float)):
            raise TypeError(
                Guard.VALUE_IS_NOT_NUMERIC_ARGS_1.format(nameof(expected_smaller_value))
            )

        if value > expected_smaller_value:
            return

        raise ValueError(
            Guard.VALUE_MUST_BE_GREATER_THAN_ARGS_2.format(value_name, expected_smaller_value)
        )

    @staticmethod
    def is_greater_than_or_equal_to(value, expected_smaller_value, value_name: str):
        """Asserts that the value is greater than or equal to expected smaller value."""
        if not isinstance(value, (int, float)):
            raise TypeError(Guard.VALUE_IS_NOT_NUMERIC_ARGS_1.format(value_name))

        if not isinstance(expected_smaller_value, (int, float)):
            raise TypeError(
                Guard.VALUE_IS_NOT_NUMERIC_ARGS_1.format(nameof(expected_smaller_value))
            )

        if value >= expected_smaller_value:
            return

        raise ValueError(
            Guard.VALUE_MUST_BE_GREATER_THAN_OR_EQUAL_TO_ARGS_2.format(
                value_name, expected_smaller_value
            )
        )

    @staticmethod
    def is_not_empty(iterable_instance: Iterable, instance_name: str):
        """Asserts that the iterable object is not empty."""
        if len(iterable_instance) > 0:
            return
        raise ValueError(
            Guard.ITERABLE_IS_EMPTY_ARGS_2.format(instance_name, type(iterable_instance).__name__)
        )

    @staticmethod
    def is_not_none_nor_empty_nor_whitespace(value: str, value_name: str):
        """Asserts that the str object is empty."""
        if (  # noqa: E714 - test for object identity should be 'is not' (auto-generated noqa)
            not value is None and value and value.strip()
        ):
            return

        raise ValueError(Guard.STRING_IS_NONE_OR_EMPTY_OR_WHITESPACE_ARGS_1.format(value_name))

    @staticmethod
    def size_is_greater_or_equal_than(iterable_instance: Iterable, size: int, iterable_name: str):
        """Asserts that the iterable object has enough elements."""
        if len(iterable_instance) >= size:
            return
        raise ValueError(
            Guard.ITERABLE_MUST_HAVE_ENOUGH_ELEMENTS_ARGS_2.format(iterable_name, size)
        )

    @staticmethod
    def size_is_less_than_or_equal(iterable_instance: Iterable, size: int, iterable_name: str):
        """Asserts that the iterable object does contains
        less than the specific size."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (332 > 100 characters) (auto-generated noqa)
        if len(iterable_instance) <= size:
            return
        raise ValueError(
            Guard.ITERABLE_MUST_CONTAIN_LESS_THAN_SPECIFIC_NUMBER_OF_ELEMENTS_ARGS_2.format(
                iterable_name, size
            )
        )

    @staticmethod
    def have_same_size(
        first_iterable_instance: Iterable,
        first_iterable_name: str,
        second_iterable_instance: Iterable,
        second_iterable_name: str,
    ):
        """Asserts that both iterable objects have same size."""
        if len(first_iterable_instance) == len(second_iterable_instance):
            return

        raise ValueError(
            Guard.ITERABLES_HAVE_NOT_SAME_SIZE_ARGS_2.format(
                first_iterable_name, second_iterable_name
            )
        )

    @staticmethod
    def is_within_limits_included(value, lower_limit, upper_limit, value_name: str):
        """Asserts that the value is not within the specified limits including the limit values"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (286 > 100 characters) (auto-generated noqa)

        if value >= lower_limit and value <= upper_limit:
            return

        raise ValueError(
            Guard.VALUE_MUST_BE_WITHIN_LIMITS_INCLUDED.format(value_name, lower_limit, upper_limit)
        )

    @staticmethod
    def is_within_limits_excluded(value, lower_limit, upper_limit, value_name: str):
        """Asserts that the value is not within the specified limits excluding the limit values"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (286 > 100 characters) (auto-generated noqa)

        if value > lower_limit and value < upper_limit:
            return

        raise ValueError(
            Guard.VALUE_MUST_BE_WITHIN_LIMITS_EXCLUDED.format(value_name, lower_limit, upper_limit)
        )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/iterable_utilities.py sha256=920fbf05af104d7f363c138f2fdf8cd8577b329d1aca5f880f3f960b1b827467 bytes=1160 -->
## FILE: src/nipcbatt/pcbatt_utilities/iterable_utilities.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_utilities/iterable_utilities.py`
- sha256: `920fbf05af104d7f363c138f2fdf8cd8577b329d1aca5f880f3f960b1b827467`
- bytes: 1160

````python
""" Provides a set of iterable related utilities routines."""

import itertools
from collections.abc import Iterable

from varname import nameof

from nipcbatt.pcbatt_utilities.guard_utilities import Guard


def count(iterable_element: Iterable) -> tuple[int, Iterable]:
    """Counts the number of elements is hold by an iterable,
        input iterable should be no more used after a call to this function.

    Args:
        iterable_element (Iterable): input iterable elements count.

    Returns:
        tuple[int, Iterable]: number of elements contained in the input
            iterable and new iterable replacing the input one.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
    Guard.is_not_none(iterable_element, nameof(iterable_element))
    forked_iterators = itertools.tee(iterable_element)
    count_result = sum(1 for f in forked_iterators[1])
    return count_result, forked_iterators[0]
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/native_interop_utilities.py sha256=9218db361473d57247bb654cf58c6fea944b93fa591c4510f1e2fb77d356d8e6 bytes=5974 -->
## FILE: src/nipcbatt/pcbatt_utilities/native_interop_utilities.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_utilities/native_interop_utilities.py`
- sha256: `9218db361473d57247bb654cf58c6fea944b93fa591c4510f1e2fb77d356d8e6`
- bytes: 5974

````python
"""Provides a set of utilities functions related to native functions."""

from ctypes import CDLL, WinDLL, c_int, cdll, windll
from typing import List, Type

from _ctypes import (
    FUNCFLAG_CDECL as _FUNCFLAG_CDECL,
    FUNCFLAG_STDCALL as _FUNCFLAG_STDCALL,
    FUNCFLAG_USE_ERRNO as _FUNCFLAG_USE_ERRNO,
    CFuncPtr as _CFunctPtr,
)
from varname import nameof

from nipcbatt.pcbatt_utilities import os_utilities
from nipcbatt.pcbatt_utilities.file_utilities import file_exists
from nipcbatt.pcbatt_utilities.guard_utilities import Guard

FUNCTION_CALL_FAILED_ARGS_2 = "Call of function '{}' failed ({})"
FILE_NOT_FOUND_ARGS_1 = "file '{}' not found"


class _StdCallFuncPtr(_CFunctPtr):
    """Defines a pointer to a callable that supports standard calling convention."""

    _flags_ = _FUNCFLAG_STDCALL | _FUNCFLAG_USE_ERRNO
    _restype_ = c_int


class _CdeclFuncPtr(_CFunctPtr):
    """Defines a pointer to a callable that supports C calling convention (Cdecl)."""

    _flags_ = _FUNCFLAG_CDECL | _FUNCFLAG_USE_ERRNO
    _restype_ = c_int


def load_stcall_win_dll(dll_path: str) -> WinDLL:
    """Loads a windows dll library with standard calling convention.

    Args:
        dll_path (str): the path of the dll.

    Raises:
        FileNotFoundError:
            Raised when an error occured while loading the dll.
        OSError:
            Raised when dll has invalid format.
    """
    Guard.is_not_none_nor_empty_nor_whitespace(dll_path, nameof(dll_path))

    return windll.LoadLibrary(dll_path)


def load_cdecl_dll(dll_path: str) -> CDLL:
    """Loads a dll with cdecl convention.

    Args:
        dll_path (str): The path of the dll.

    Raises:
        FileNotFoundError:
            Raised when an error occured while loading the dll.
        OSError:
            Raised when dll has invalid format.
    """
    Guard.is_not_none_nor_empty_nor_whitespace(dll_path, nameof(dll_path))

    return cdll.LoadLibrary(dll_path)


def create_native_stdcall_win_function(
    dll_path: str,
    function_name: str,
    return_value_type: Type,
    arguments_types: List[Type],
) -> _StdCallFuncPtr:
    """Creates a pointer on a native function from a win stdcall dll.

    Args:
        dll_path (str): The path of the dll.
        function_name (str): The name of the function.
        return_value_type (Type): The type of the object the function should return.
        arguments_types (List[Type]): A list of types for arguments.

    Raises:
        AttributeError:
            Raised the function is not defined in the library.
        FileNotFoundError:
            Raised when dll was not found.

    Returns:
        StdCallFuncPtr: the pointer to a callable object function retrieved from the library.
    """
    Guard.is_not_none_nor_empty_nor_whitespace(dll_path, nameof(dll_path))
    Guard.is_not_none_nor_empty_nor_whitespace(function_name, nameof(function_name))

    check_dll_availability(dll_path)

    library_entries = load_stcall_win_dll(dll_path)

    function_to_call = _StdCallFuncPtr()

    function_to_call = getattr(library_entries, function_name)

    function_to_call.restype = return_value_type
    function_to_call.argtypes = arguments_types

    return function_to_call


def create_native_cdecl_function(
    dll_path: str,
    function_name: str,
    return_value_type: Type,
    arguments_types: List[Type],
) -> _CdeclFuncPtr:
    """Creates a pointer on a native function from a dll with cdecl convention.

    Args:
        dll_path (str): The path of the dll.
        function_name (str): The name of the function.
        return_value_type (Type): The type of the object the function should return.
        arguments_types (List[Type]): A list of types for arguments.

    Raises:
        AttributeError:
            Raised the function is not defined in the library.
        FileNotFoundError:
            Raised when dll was not found.

    Returns:
        _CdeclFuncPtr: the pointer to a callable object function retrieved from the library.
    """
    Guard.is_not_none_nor_empty_nor_whitespace(dll_path, nameof(dll_path))
    Guard.is_not_none_nor_empty_nor_whitespace(function_name, nameof(function_name))

    check_dll_availability(dll_path)

    library_entries = load_cdecl_dll(dll_path)

    function_to_call = _CdeclFuncPtr()

    function_to_call = getattr(library_entries, function_name)

    function_to_call.restype = return_value_type
    function_to_call.argtypes = arguments_types

    return function_to_call


def check_dll_availability(relative_or_absolute_dll_path: str):
    """Checks a dll file exist when path is absolute,
    elsewhere, the function resolves an absolute path by looking up system path variables
    then it checks the existence of resolved path.

    Args:
        relative_or_absolute_dll_path (str): The path of the dll (absolute or relative).

    Raises:
        FileNotFoundError:
            Raised the dll is not found.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
    if os_utilities.is_path_absolute(relative_or_absolute_dll_path):
        if file_exists(relative_or_absolute_dll_path):
            return
    else:
        env_variable_paths = os_utilities.get_env_variable_paths()

        for env_variable_path in env_variable_paths:
            absolute_dll_path = os_utilities.combine_path_components(
                env_variable_path, relative_or_absolute_dll_path
            )
            if file_exists(absolute_dll_path):
                return

    raise FileNotFoundError(FILE_NOT_FOUND_ARGS_1.format(relative_or_absolute_dll_path))
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/numeric_utilities.py sha256=7e6839bb7e0a0322450db3ca96a6a4b8c345e2381497b433e23083f533968749 bytes=2151 -->
## FILE: src/nipcbatt/pcbatt_utilities/numeric_utilities.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_utilities/numeric_utilities.py`
- sha256: `7e6839bb7e0a0322450db3ca96a6a4b8c345e2381497b433e23083f533968749`
- bytes: 2151

````python
"""Provides a set of numeric related utilities functions."""

from varname import nameof

from nipcbatt.pcbatt_utilities.guard_utilities import Guard


def from_percent_to_decimal_ratio(percent: float) -> float:
    """Computes decimal ration of a given percentage value, for example 50%
    returns 0.5.

    Args:
        percent: percentage value to convert to ratio.

    Returns:
        float: for example 10  returns 0.1, 100 returns 1 and  0 returns 0

    Raises:
        ValueError: Occurs when input percent is less than zero.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
    Guard.is_greater_than_or_equal_to_zero(percent, nameof(percent))
    return percent / 100


def percent_of(percent: float, value: float) -> float:
    """Computes percent ratio of a given value.

    Args:
        percent (float): Percentage ratio to compute.
        value (float): Value for which percent ration is needed.

    Returns:
        float: for example (10 , 100) -> 10
    Raises:
        ValueError: Occurs when input percent is less than zero.
    """
    Guard.is_greater_than_or_equal_to_zero(percent, nameof(percent))
    return (value * percent) / 100


def absolute_value(value: float) -> float:
    """Computes absolute value of a given value.

    Args:
        value (float): Value for which absolute value is needed.

    Returns:
        float: for example -10 -> 10
    """
    return abs(value)


def invert_value(value: float):
    """Computes invert value of a given value.

    Args:
        value (float): Value for which invert value is needed.

    Returns:
        float: for example 0.5 -> 2
    Raises:
        ValueError: Occurs when input value equals zero.
    """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

    Guard.is_greater_than_zero(value, nameof(value))
    return 1 / value
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/os_utilities.py sha256=38036f66395240764ccab45be5e76a748312145de3e09b1605d02bac82d17c3d bytes=1014 -->
## FILE: src/nipcbatt/pcbatt_utilities/os_utilities.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_utilities/os_utilities.py`
- sha256: `38036f66395240764ccab45be5e76a748312145de3e09b1605d02bac82d17c3d`
- bytes: 1014

````python
""" Provides a set of operating system utilities routines."""

import os
from typing import List


def get_env_variable_paths() -> List[str]:
    """Enumerates paths described in the 'Path' environment variable."""
    path_env = set(os.getenv("Path").split(";"))
    return list(path_env)


def is_path_absolute(path: str) -> bool:
    """Checks is a path is absolute (containing root path).

    Args:
        path (str): the path of file or folder.

    Returns:
        bool: `True` if the path is absolute.
    """
    return os.path.isabs(path)


def combine_path_components(path: str, *path_components: str) -> str:
    """Appends path components to a specific path.

    Args:
        path (str): the path on which path are appended.
        *path_components (str): contains path components to add.
    Returns:
        str: the conbined path.
    """  # noqa: D411 - Missing blank line before section (auto-generated noqa)
    return os.path.join(path, *path_components)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/pcbatt_logger.py sha256=e1d6104a7b26bdceb61e0607067e98a41bca447b963a7a489061ad79bb1750c1 bytes=10522 -->
## FILE: src/nipcbatt/pcbatt_utilities/pcbatt_logger.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_utilities/pcbatt_logger.py`
- sha256: `e1d6104a7b26bdceb61e0607067e98a41bca447b963a7a489061ad79bb1750c1`
- bytes: 10522

````python
""" Implementation of PcbattLogger """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (149 > 100 characters) (auto-generated noqa)

import types
from datetime import datetime
from typing import List

# pylint: disable=C0301,W0212,W0105

# https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/line-too-long.html
# https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/protected-access.html


class PcbattLogger:
    """
    Class for logging inputs and outputs of methods.
    The goal is to log most informations without slowing down the caller.
    """  # noqa: D205, D212, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (193 > 100 characters) (auto-generated noqa)

    def __init__(self, file: str, methods: List[str] = None):
        """
        Initializes the PcbattLogger with a file path.
        methods default values is ['configure_and_measure', 'configure_and_generate']

        Args:
            file (str): The file path where the logs will be stored.
            methods (List[str], optional): List of methods to log. Defaults values : ['configure_and_measure', 'configure_and_generate'].
        """  # noqa: D205, D212, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (137 > 100 characters) (auto-generated noqa)
        # https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/dangerous-default-value.html
        if methods is None:
            methods = ["configure_and_measure", "configure_and_generate"]
        self.methods = methods
        self._modules = {}
        self.set_file(file)

    @staticmethod
    def _logger_txt(module, original_method, self, configuration):
        """
        A static method to log inputs and outputs of methods into txt format.

        Args:
            module: The module whose method is being logged.
            original_method: The original method to call.
            configuration: The input configuration passed to the method.
            self: The PcbattLogger instance.

        Returns:
            The result returned by the original method.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        if configuration:
            result = original_method(configuration)
        else:
            result = original_method()

        with open(self.__file, mode="a", encoding="utf-8") as f:
            f.write("Module : " + str(module.__class__).rsplit(".", maxsplit=1)[-1][:-2] + "\n")
            # Check if module has task attribute (DAQ modules)     
            if hasattr(module, 'task') and hasattr(module.task, 'channel_names'): 
                f.write("Channel names : " + str(module.task.channel_names) + "\n")
            # Check if module has DMM-specific attributes 
            if hasattr(module, '_dmm_resource_name'): 
                f.write("DMM Resource : " + str(module._dmm_resource_name) + "\n") 
            if hasattr(module, '_powerline_frequency'): 
                f.write("Powerline Frequency : " + str(module._powerline_frequency) + " Hz\n") 
            # Check if module has NI-DCPower-specific attributes
            if hasattr(module, '_resource_name'):
                f.write("DCPower Resource : " + str(module._resource_name) + "\n")
            if hasattr(module, '_channel_name'):
                f.write("DCPower Channel : " + str(module._channel_name) + "\n")
            if configuration:
                f.write("Inputs :\n")
                f.write(str(configuration) + "\n\n")
            if result:
                f.write("Outputs :\n")
                f.write(str(result) + "\n\n\n\n")
        return result

    @staticmethod
    def _logger_csv(module, original_method, self, configuration):
        """
        A static method to log inputs and outputs of methods into csv format.
        This method is just an example how to log in different format and needs modifications.

        Args:
            module: The module whose method is being logged.
            original_method: The original method being called.
            configuration: The input configuration passed to the method.
            self: The PcbattLogger instance.

        Returns:
            The result returned by the original method.
        """  # noqa: D205, D212, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (197 > 100 characters) (auto-generated noqa)
        result = original_method(configuration)

        with open(self.__file, mode="a", encoding="utf-8") as f:
            f.write("Module : " + str(module.__class__).rsplit(".", maxsplit=1)[-1][:-2] + "\n")
            # Check if module has task attribute (DAQ modules)     
            if hasattr(module, 'task') and hasattr(module.task, 'channel_names'): 
                f.write("Channel names : " + str(module.task.channel_names) + "\n")
            # Check if module has DMM-specific attributes 
            if hasattr(module, '_dmm_resource_name'): 
                f.write("DMM Resource : " + str(module._dmm_resource_name) + "\n") 
            if hasattr(module, '_powerline_frequency'): 
                f.write("Powerline Frequency : " + str(module._powerline_frequency) + " Hz\n") 
            # Check if module has NI-DCPower-specific attributes
            if hasattr(module, '_resource_name'):
                f.write("DCPower Resource : " + str(module._resource_name) + "\n")
            if hasattr(module, '_channel_name'):
                f.write("DCPower Channel : " + str(module._channel_name) + "\n")
            if configuration:
                f.write("Inputs\n")
                f.write(str(configuration) + "\n")
            if result:
                f.write("Outputs\n")
                f.write(str(result) + "\n")
        return result

    def _monkey_patch(self, module):
        """
        A method to monkey patch module methods for logging.

        Args:
            module: The module to be patched.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        # Retrieve all methods from module
        attributes = dir(module)
        # Monkey-patch the method
        for method in self.methods:
            if method in attributes:
                if self.__file.endswith(".csv"):
                    setattr(
                        module,
                        method,
                        types.MethodType(
                            lambda cls, configuration=None: PcbattLogger._logger_csv(
                                module, self._modules[module], self, configuration
                            ),
                            module,
                        ),
                    )
                else:
                    setattr(
                        module,
                        method,
                        types.MethodType(
                            lambda cls, configuration=None: PcbattLogger._logger_txt(
                                module, self._modules[module], self, configuration
                            ),
                            module,
                        ),
                    )

    def attach(self, module):
        """
        Attaches a module to log its method calls.

        Args:
            module: The module to be attached.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        # Retrieve all methods from module
        attributes = dir(module)
        # Save wanted method
        for method in self.methods:
            if method in attributes:
                self._modules[module] = getattr(module, method)
        self._monkey_patch(module)

    def remove(self, module):
        """
        Removes a module from logging.

        Args:
            module: The module to be removed.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        # Retrieve all methods from module
        attributes = dir(module)
        # Remove monkey patching
        for method in self.methods:
            if method in attributes:
                setattr(module, method, self._modules[module])
        # Remove from the list of monkey patched classes
        if module in self._modules:
            self._modules.pop(module)

    def set_file(self, file: str):
        """
        Sets the file path for logging.

        Args:
            file (str): The file path where the logs will be stored.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        self.__file = file
        now = datetime.now()
        current_time = now.strftime("%m-%d-%Y %H:%M:%S")
        # Always write the current date and time when changing the file
        with open(self.__file, mode="a", encoding="utf-8") as f:
            f.write("Current time : " + current_time + "\n")

    def get_modules(self) -> List[str]:
        """
        Retrieves the names of all attached modules.

        Returns:
            List[str]: The names of all attached modules.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        # Get all classes names
        # Split them with a . and get the last value
        # Remove the two last characters
        return [str(x.__class__).rsplit(".", maxsplit=1)[-1][:-2] for x in self._modules]
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/platform_utilities.py sha256=7ba8cf043b9f84e60b3a979da8b061230ce09e01aa86f771413e1e8bf0785f52 bytes=1385 -->
## FILE: src/nipcbatt/pcbatt_utilities/platform_utilities.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_utilities/platform_utilities.py`
- sha256: `7ba8cf043b9f84e60b3a979da8b061230ce09e01aa86f771413e1e8bf0785f52`
- bytes: 1385

````python
"""Defines a set of platform related utilities functions."""

import platform


def is_python_windows_32bits() -> bool:
    """Indicates if current python interpreter is running on windows os
    and if it is 32 bits architecture.

    Returns:
        Boolean: True if python is running 32 bits architecture on windows os
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
    if platform.system() == "Windows":
        return platform.architecture()[0].endswith("32bit")

    return False


def is_python_windows_64bits() -> bool:
    """Indicates if current python interpreter is running on windows os
    and if it is 64 bits architecture.

    Returns:
        Boolean: True if python is running 64 bits architecture on windows os
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
    if platform.system() == "Windows":
        return platform.architecture()[0].endswith("64bit")

    return False
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/plotter.py sha256=1c8684f53155c975580f821b6f1a21176bb7922180be4ba5cc533937e0dd3247 bytes=6333 -->
## FILE: src/nipcbatt/pcbatt_utilities/plotter.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_utilities/plotter.py`
- sha256: `1c8684f53155c975580f821b6f1a21176bb7922180be4ba5cc533937e0dd3247`
- bytes: 6333

````python
import os  # noqa: D100 - Missing docstring in public module (auto-generated noqa)
from datetime import datetime

import matplotlib.gridspec as gridspec
import matplotlib.pylab as pl
import matplotlib.pyplot as plt
import numpy as np  # noqa: F401 - 'numpy as np' imported but unused (auto-generated noqa)

## Using graph_plot function as a module in other files:

# import plotter as pl

# pl.graph_plot(y,x,title="Graph", save_fig=True)


def graph_plot(  # noqa: D103 - Missing docstring in public function (auto-generated noqa)
    y: list, x=[], title="", ylabel="", xlabel="", save_fig=False
):
    if x != []:
        plt.plot(x, y)
    else:
        plt.plot(y)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)

    if save_fig is True:
        if title == "":
            t = "Plot"
        else:
            t = title.replace(" ", "_")
        now = datetime.now()
        current_time = now.strftime("%m-%d-%Y_%H-%M-%S")
        path = os.getcwd() + "\\" + t + "_" + current_time + ".png"
        print(path)
        plt.savefig(path)
    plt.show()


# Examples

# y=[1,2,3,4,5,6,7,8,9]
# graph_plot(y, title="Sample Graph")


# y=[1,2,3,4,5,6,7,8,9]
# x=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
# graph_plot(y, x, title="Sample Graph1",  ylabel="Voltage", xlabel="Time", save_fig=True)

# _______________________________________________________________________________________________________________________________________________________


def plot_two(  # noqa: D103 - Missing docstring in public function (auto-generated noqa)
    y1: list,
    y2: list,
    x1=[],
    title1="",
    ylabel1="",
    xlabel1="",
    x2=[],
    title2="",
    ylabel2="",
    xlabel2="",
    stitle="",
    save_fig=False,
):
    fig, ax = plt.subplots(nrows=1, ncols=2)
    x1 = x1.tolist()
    x2 = x2.tolist()
    if x1 != [] and x2 != []:
        # create 2 subplots
        ax[0].plot(x1, y1)
        ax[1].plot(x2, y2)
    else:
        ax[0].plot(y1)
        ax[1].plot(y2)

    # plot 2 subplots
    ax[0].set_xlabel(xlabel1)
    ax[0].set_ylabel(ylabel1)
    ax[0].set_title(title1)
    ax[1].set_xlabel(xlabel2)
    ax[1].set_ylabel(ylabel2)
    ax[1].set_title(title2)

    plt.suptitle(stitle)

    # savefig
    if save_fig is True:
        if stitle == "":
            t = "Plot"
        else:
            t = stitle.replace(" ", "_")
        now = datetime.now()
        current_time = now.strftime("%m-%d-%Y_%H-%M-%S")
        path = os.getcwd() + "\\" + t + "_" + current_time + ".png"
        print(path)
        plt.savefig(path)
    plt.show()


# _______________________________________________________________________________________________________________________________________________________


def plot_three(  # noqa: D103 - Missing docstring in public function (auto-generated noqa)
    y1: list,
    y2: list,
    y3: list,
    x1=[],
    title1="",
    ylabel1="",
    xlabel1="",
    x2=[],
    title2="",
    ylabel2="",
    xlabel2="",
    x3=[],
    title3="",
    ylabel3="",
    xlabel3="",
    stitle="",
    save_fig=False,
):
    gs = gridspec.GridSpec(2, 2)

    pl.figure()
    ax = pl.subplot(gs[0, :])
    ax.set_xlabel(xlabel1)
    ax.set_ylabel(ylabel1)
    ax.set_title(title1)
    x1 = x1.tolist()
    x2 = x2.tolist()
    x3 = x3.tolist()
    if x1 != []:
        ax.plot(x1, y1)

    else:
        ax.plot(y1)

    ax = pl.subplot(gs[1, 0])
    ax.set_xlabel(xlabel2)
    ax.set_ylabel(ylabel2)
    ax.set_title(title2)
    if x2 != []:
        ax.plot(x2, y2)
    else:
        ax.plot(y2)

    ax = pl.subplot(gs[1, 1])
    ax.set_xlabel(xlabel3)
    ax.set_ylabel(ylabel3)
    ax.set_title(title3)
    if x3 != []:
        ax.plot(x3, y3)
    else:
        ax.plot(y3)

    pl.suptitle(stitle)

    # savefig
    if save_fig is True:
        if stitle == "":
            t = "Plot"
        else:
            t = stitle.replace(" ", "_")
        now = datetime.now()
        current_time = now.strftime("%m-%d-%Y_%H-%M-%S")
        path = os.getcwd() + "\\" + t + "_" + current_time + ".png"
        print(path)
        pl.savefig(path)
    pl.show()


# _______________________________________________________________________________________________________________________________________________________


def plot_four(  # noqa: D103 - Missing docstring in public function (auto-generated noqa)
    y1: list,
    y2: list,
    y3: list,
    y4: list,
    x1=[],
    title1="",
    ylabel1="",
    xlabel1="",
    x2=[],
    title2="",
    ylabel2="",
    xlabel2="",
    x3=[],
    title3="",
    ylabel3="",
    xlabel3="",
    x4=[],
    title4="",
    ylabel4="",
    xlabel4="",
    stitle="",
    save_fig=False,
):
    fig, ax = plt.subplots(nrows=2, ncols=2)
    x1 = x1.tolist()
    x2 = x2.tolist()
    x3 = x3.tolist()
    x4 = x4.tolist()

    ax[0, 0].set_xlabel(xlabel1)
    ax[0, 0].set_ylabel(ylabel1)
    ax[0, 0].set_title(title1)
    if x1 != []:
        ax[0, 0].plot(x1, y1)
    else:
        ax[0, 0].plot(y1)

    ax[0, 1].set_xlabel(xlabel2)
    ax[0, 1].set_ylabel(ylabel2)
    ax[0, 1].set_title(title2)
    if x2 != []:
        ax[0, 1].plot(x2, y2)
    else:
        ax[0, 1].plot(y2)

    ax[1, 0].set_xlabel(xlabel3)
    ax[1, 0].set_ylabel(ylabel3)
    ax[1, 0].set_title(title3)
    if x3 != []:
        ax[1, 0].plot(x3, y3)
    else:
        ax[1, 0].plot(y3)

    ax[1, 1].set_xlabel(xlabel4)
    ax[1, 1].set_ylabel(ylabel4)
    ax[1, 1].set_title(title4)
    if x4 != []:
        ax[1, 1].plot(x4, y4)
    else:
        ax[1, 1].plot(y4)

    plt.suptitle(stitle)

    # savefig
    if save_fig is True:
        if stitle == "":
            t = "Plot"
        else:
            t = stitle.replace(" ", "_")
        now = datetime.now()
        current_time = now.strftime("%m-%d-%Y_%H-%M-%S")
        path = os.getcwd() + "\\" + t + "_" + current_time + ".png"
        print(path)
        plt.savefig(path)
    plt.show()


# ______________________________________________________________________________________________________________________________________________
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/reflection_utilities.py sha256=9c8f8ffe39e6154d4a12e9a04a4c474b161c43a86f4afc039f57d7af974781f4 bytes=2942 -->
## FILE: src/nipcbatt/pcbatt_utilities/reflection_utilities.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_utilities/reflection_utilities.py`
- sha256: `9c8f8ffe39e6154d4a12e9a04a4c474b161c43a86f4afc039f57d7af974781f4`
- bytes: 2942

````python
""" Provides a set of reflection utilities functions."""

from enum import Enum
from typing import Callable, Iterable, Tuple, Type, Union

import numpy as np


def substitute_method(cls: Type, method: Callable, method_name: str):
    """Replaces the specific method of a class by a specific function (Callable).
       This function must have self as first argument.
    Args:
        cls (Type): The class on which the method is replaced.
        method (Callable): the function to substitute.
        method_name (str): the name of the method to replace.
    """  # noqa: D205, D411, W505 - 1 blank line required between summary line and description (auto-generated noqa), Missing blank line before section (auto-generated noqa), doc line too long (167 > 100 characters) (auto-generated noqa)
    setattr(
        cls,
        method_name,
        method,
    )


def enumerate_properties(instance: object) -> Iterable[Tuple]:
    """Enumerates properties defined in instance

    Args:
        instance (object): the object on which properties are enumerated.

    Returns:
        iterator with a sequence of tuples containing the name of property and its value.
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)
    members = [item for item in vars(type(instance)).items() if isinstance(item[1], property)]

    for property_name, property_object in members:
        yield property_name, property_object.fget(instance)


def convert_for_json_serialization(
    value: object,
) -> Union[int, float, bool, str, list, dict]:
    """Converts an instance for JSON serialization.

    Args:
        value (object): the value to convert.

    Returns:
        Union[int, float, bool, str, dict]:
            if value is an Enum, returns a string with its name and its value;
            if value is str, int, float or bool, returns the value itself;
            if value is a list, return a list of JSON representation of each item;
            if value is a class containing properties,
            returns a dictionary with property names and values.
    """
    if isinstance(value, Enum):
        return f"{value.name} ({value.value})"

    if isinstance(value, (int, float, bool, str)):
        return value

    if isinstance(value, dict):
        return {
            k: bool(v) if isinstance(v, np.bool_) else v
            for k, v in value.items()
        }

    if isinstance(value, list):
        return [convert_for_json_serialization(item) for item in value]

    if len(list(enumerate_properties(value))) != 0:
        return {
            property_name: convert_for_json_serialization(property_value)
            for property_name, property_value in enumerate_properties(value)
        }

    return repr(value)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_utilities/save_traces.py sha256=9a9b5fa63f2e6c77a434008f54b3000498fbe1cb49494835de51f30b99366f6d bytes=5653 -->
## FILE: src/nipcbatt/pcbatt_utilities/save_traces.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_utilities/save_traces.py`
- sha256: `9a9b5fa63f2e6c77a434008f54b3000498fbe1cb49494835de51f30b99366f6d`
- bytes: 5653

````python
"""
Save environment config, inputs and outputs from pcbatt
"""  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (203 > 100 characters) (auto-generated noqa)

import inspect
import os
import struct
import sys
from datetime import datetime
from pathlib import Path
from typing import Union

import pkg_resources

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.csv_utilities import export_signal_to_csv_file


# Using Union because PEP 604 was implemented in 3.10
# https://peps.python.org/pep-0604/
def save_traces(
    config: Union[
        daq.DcRmsCurrentMeasurementConfiguration,
        daq.DcRmsVoltageMeasurementConfiguration,
        daq.PowerSupplySourceAndMeasureConfiguration,
        daq.TimeDomainMeasurementConfiguration,
        daq.TemperatureRtdMeasurementConfiguration,
        daq.TemperatureThermistorMeasurementConfiguration,
    ],
    file_name: str,
    result_data: Union[
        daq.DcRmsCurrentMeasurementResultData,
        daq.DcRmsVoltageMeasurementResultData,
        daq.PowerSupplySourceAndMeasureResultData,
        daq.TimeDomainMeasurementResultData,
        daq.TemperatureMeasurementResultData,
    ] = None,
    sampling_rate: int = 10000,
    unit: str = "Amplitude",
):
    """
    This method is use to save any types of confiuration and result_data from nipcbatt
    the file are stored in a folder called results one folder above the caller
    it creates a folder with the date month-day-year_hour-minute-seconde
    it stores all waveforms in different csv files and the rest in a txt

    Args:
        config (Any Configuration): Configuration from nipcbatt
        file_name (str): name use to save the traces
        result_data (Any ResultData, optional): Result data from nipcbatt. Defaults to None.
        sampling_rate (int, optional): sampling rate. Defaults to 10000.
        unit (str, optional): unit use for the waveforms. Defaults to 'Amplitude'.
    """  # noqa: D202, D205, D212, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (372 > 100 characters) (auto-generated noqa)

    # Retrieve the caller path
    stack = inspect.stack()
    first_caller = stack[1]
    caller_path = first_caller[1]
    caller_name = Path(os.path.basename(caller_path)).stem

    now = datetime.now()
    current_time = now.strftime("%m-%d-%Y_%H-%M-%S")

    # Get the name of the used file to store the result
    folder_name = caller_name
    # Create folder if don't exist
    parent_folder = os.path.dirname(os.path.dirname(caller_path))
    result_folder = os.path.join(parent_folder, "results", folder_name, current_time)
    os.makedirs(result_folder, exist_ok=True)

    text_file = os.path.join(result_folder, file_name + ".txt")

    f = open(text_file, mode="a", encoding="utf-8")

    # Using version_info instead version because it was too much information and some are confusing
    f.write(
        "Python : "
        + str(sys.version_info.major)
        + "."
        + str(sys.version_info.minor)
        + "."
        + str(sys.version_info.micro)
        + " "
    )
    f.write(str(struct.calcsize("P") * 8) + "bits\n")
    f.write("nipcbatt : " + pkg_resources.get_distribution("nipcbatt").version + "\n\n\n")

    if config:
        f.write("inputs :\n")
        for attribute in config.__dict__:
            element = getattr(config, attribute)
            f.write(attribute + ": " + str(element) + "\n")
        f.write("\n\n")

    if result_data:
        f.write("outputs :\n")
        for attribute in result_data.__dict__:
            element = getattr(result_data, attribute)
            if isinstance(element, nipcbatt.AnalogWaveform):
                # f'{element=}'.split('=')[0] get the name of the variable
                # example voltage_waveform
                file_name = file_name + attribute + ".csv"
                export_signal_to_csv_file(
                    signal_csv_file_path=os.path.join(result_folder, file_name),
                    signal_samples=element.samples.tolist(),
                    signal_sampling_rate=sampling_rate,
                    x_axis_name="Time(s)",
                    y_axis_name=unit,
                )
            # Check if it's a list and that all elements are nipcbatt.AnalogWaveform
            elif isinstance(element, list) and all(
                isinstance(item, nipcbatt.AnalogWaveform) for item in element
            ):
                for waveform in element:
                    # Replace / from channel names to _
                    file_name = "tdm_" + waveform.channel_name.replace("/", "_") + ".csv"
                    export_signal_to_csv_file(
                        signal_csv_file_path=os.path.join(result_folder, file_name),
                        signal_samples=waveform.samples.tolist(),
                        signal_sampling_rate=sampling_rate,
                        x_axis_name="Time(s)",
                        y_axis_name=unit,
                    )
            else:
                f.write(attribute + ": " + str(element) + "\n")
    f.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/845x_examples/I2C.py sha256=78b964bbe29d445e0332eab94b588e5945fde9202f7f40795db5687538bfcfb1 bytes=3052 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/845x_examples/I2C.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/845x_examples/I2C.py`
- sha256: `78b964bbe29d445e0332eab94b588e5945fde9202f7f40795db5687538bfcfb1`
- bytes: 3052

````python
""" This example demonstrates use of LM75 I2C Temperature sensor for taking 
    temperature measurements using USB-8452 device """  

### Ensure correct hardware and corresponding trigger names before running this example

import threading
import time
from ctypes import c_uint8

import numpy

import nipcbatt
import nipcbatt.pcbatt_communication_library
import nipcbatt.pcbatt_communication_library._ni_845x_internal
import nipcbatt.pcbatt_communication_library._ni_845x_internal._ni_845x_functions
import nipcbatt.pcbatt_communication_library.ni_845x_data_types
import nipcbatt.pcbatt_communication_library.ni_845x_devices
import nipcbatt.pcbatt_communication_library.ni_845x_i2c_communication_devices
import nipcbatt.pcbatt_library

# Flag to control the loop
running = True


def check_input():  
    global running
    input("Press Enter to exit...\n")
    running = False


# Start a thread to listen for Enter key
input_thread = threading.Thread(target=check_input)
input_thread.start()

# Initialize
i2c = (
    nipcbatt.pcbatt_communication_library.ni_845x_i2c_communication_devices.Ni845xI2cDevicesHandler()
)
i2c.open(device_name="USB-8452")

# pylint: disable=protected-access
handle_type = (
    nipcbatt.pcbatt_communication_library._ni_845x_internal._ni_845x_functions._get_handle_type()
)

# begin I2C Configure
nipcbatt.pcbatt_communication_library._ni_845x_internal._ni_845x_functions.invoke_ni_845x_function(
    nipcbatt.pcbatt_communication_library._ni_845x_internal._ni_845x_functions._Ni845xFunctionsNames.NI_845X_SET_IO_VOLTAGE_LEVEL,
    handle_type(i2c._devices_handler),
    c_uint8(nipcbatt.pcbatt_communication_library.ni_845x_data_types.Ni845xVoltageLevel(33)),
)
# region manual call
i2c.enable_pullup_resistors(enable=False)
i2c.set_timeout(timeout_milliseconds=40000)

i2c.configuration.address = 73
seven_bits = nipcbatt.pcbatt_communication_library.ni_845x_data_types.Ni845xI2cAddressingType(0)
i2c.configuration.addressing_type = seven_bits
i2c.configuration.clock_rate_kilohertz = 400

data_bytes_to_be_written = numpy.ndarray(shape=[0], dtype=numpy.ubyte)
i2c_write_read = i2c.write_and_read_data(
    data_bytes_to_be_written=data_bytes_to_be_written, number_of_bytes_to_read=2
)
# end region I2C configure

# Region infinite Loop

# Click on the terminal and press Enter to exit this infinite loop
while running:
    i2c_read = i2c.read_data(number_of_bytes_to_read=2)

    # region temperature measure
    lsb = i2c_read[1]
    msb = i2c_read[0]
    joined = hex((msb << 8) + lsb)

    joined_ubyte = int(joined, 16)

    five_shifted = numpy.right_shift(joined_ubyte, 5)

    if numpy.right_shift(joined_ubyte, 15) != 0:
        five_shifted = numpy.add(five_shifted, numpy.int8(63488), dtype=numpy.int8)

    temp = five_shifted * 0.125
    print("Temperature : " + str(temp) + "°C\n")
    time.sleep(0.5)
    # endregion temperature measure

# Wait for the input thread to finish before exiting
input_thread.join()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/cDAQ_examples/cDAQ_TRTD.py sha256=b62d8d23635b7ac37ee53c20439e2cebec8d2a1f1ef243cbbc587bb88d0e7552 bytes=3195 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/cDAQ_examples/cDAQ_TRTD.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/cDAQ_examples/cDAQ_TRTD.py`
- sha256: `b62d8d23635b7ac37ee53c20439e2cebec8d2a1f1ef243cbbc587bb88d0e7552`
- bytes: 3195

````python
"""Standalone for TemperatureMeasurementUsingRtd.""" 

### Ensure correct hardware and corresponding trigger names before running this example

import nidaqmx.constants

import nipcbatt
from nipcbatt import daq
import nipcbatt.pcbatt_utilities.plotter as pl
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Global variables
plot_results = True
save_fig = False
use_specific_channel = False

# initialize 'TemperatureMeasurementUsingRtd' class instance
trtdm = daq.TemperatureMeasurementUsingRtd()
trtdm.initialize("TP_RTD")

# region TRTDM configure and measure

global_channel_parameters = daq.TemperatureRtdMeasurementTerminalParameters(
    temperature_minimum_value_celsius_degrees=0,
    temperature_maximum_value_celsius_degrees=100,
    current_excitation_value_amperes=0.001,
    sensor_resistance_ohms=100,
    rtd_type=nidaqmx.constants.RTDType.PT_3750,
    excitation_source=nidaqmx.constants.ExcitationSource.INTERNAL,
    resistance_configuration=nidaqmx.constants.ResistanceConfiguration.THREE_WIRE,
    adc_timing_mode=nidaqmx.constants.ADCTimingMode.AUTOMATIC,
)

# region specific_channels_parameters

channel0 = daq.TemperatureRtdMeasurementChannelParameters(
    channel_name="TP_RTD",
    sensor_resistance_ohms=100,
    current_excitation_value_amperes=0.001,
    rtd_type=nidaqmx.constants.RTDType.PT_3750,
    resistance_configuration=nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE,
    excitation_source=nidaqmx.constants.ExcitationSource.INTERNAL,
)

# endregion specific_channels_parameters

specific_channels_parameters = []
if use_specific_channel is True:
    specific_channels_parameters.append(channel0)

sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=100,
    number_of_samples_per_channel=10,
    sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
    digital_start_trigger_source="",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

trtdm_config = daq.TemperatureRtdMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion TRTDM configure and measure

trtdm_result_data = trtdm.configure_and_measure(configuration=trtdm_config)

trtdm.close()

print("TRTDM result :\n")
print(trtdm_result_data)

save_traces(config=trtdm_config, file_name="TRTDM", result_data=trtdm_result_data)

# region plot results

if plot_results is True:
    trtdm_w = trtdm_result_data.waveforms[0].samples.tolist()
    pl.graph_plot(
        y=trtdm_w,
        title="RTD Temperature",
        ylabel="Temp *C",
        xlabel="Samples",
        save_fig=save_fig,
    )

# endregion plot results
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/cDAQ_examples/cDAQ_TTCM.py sha256=888f810b8db512f7df88cf772d0d1291e420b343cd22da995b4be4a269796c5f bytes=3606 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/cDAQ_examples/cDAQ_TTCM.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/cDAQ_examples/cDAQ_TTCM.py`
- sha256: `888f810b8db512f7df88cf772d0d1291e420b343cd22da995b4be4a269796c5f`
- bytes: 3606

````python
"""Standalone for TemperatureMeasurementUsingThermocouple."""  

### Ensure correct hardware and corresponding trigger names before running this example

import nidaqmx.constants

import nipcbatt
from nipcbatt import daq
import nipcbatt.pcbatt_utilities.plotter as pl
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Global variables
plot_results = True
save_fig = False
use_specific_channel = False

# initialize 'TemperatureMeasurementUsingThermocouple' class instance
ttcm = daq.TemperatureMeasurementUsingThermocouple()
ttcm.initialize(
    channel_expression="Simulated_cDAQ_9211/ai0:1",
    cold_junction_compensation_source=nidaqmx.constants.CJCSource.BUILT_IN,
    cold_junction_compensation_channel="TP_RTD",
)

# region ttcm configure and measure

global_channel_parameters = daq.TemperatureThermocoupleMeasurementTerminalParameters(
    temperature_minimum_value_celsius_degrees=0.0,
    temperature_maximum_value_celsius_degrees=100.0,
    thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
    cold_junction_compensation_temperature=25.0,
    perform_auto_zero_mode=False,
    auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
)

# region specific_channels_parameters

channel_parameters = daq.TemperatureThermocoupleRangeAndTerminalParameters(
    temperature_minimum_value_celsius_degrees=0.0,
    temperature_maximum_value_celsius_degrees=100.0,
    thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
    cold_junction_compensation_source=nidaqmx.constants.CJCSource.CONSTANT_USER_VALUE,
    cold_junction_compensation_temperature=25.0,
    cold_junction_compensation_channel_name="TP_RTD",
    perform_auto_zero_mode=False,
    auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
)

channel1 = daq.TemperatureThermocoupleChannelRangeAndTerminalParameters(
    channel_name="Simulated_cDAQ_9211/ai0",
    channel_parameters=channel_parameters,
)

# endregion specific_channels_parameters

specific_channels_parameters = []
if use_specific_channel is True:
    specific_channels_parameters.append(channel1)

sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=10000,
    number_of_samples_per_channel=1000,
    sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
    digital_start_trigger_source="",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

ttcm_config = daq.TemperatureThermocoupleMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion ttcm configure and measure

ttcm_result_data = ttcm.configure_and_measure(configuration=ttcm_config)

ttcm.close()

print("ttcm result :\n")
print(ttcm_result_data)

save_traces(config=ttcm_config, file_name="ttcm", result_data=ttcm_result_data)

# region plot results

if plot_results is True:
    ttcm_w = ttcm_result_data.waveforms[0].samples.tolist()
    pl.graph_plot(
        y=ttcm_w,
        title="Thermocouple Temperature",
        ylabel="Temp *C",
        xlabel="Samples",
        save_fig=save_fig,
    )

# endregion plot results
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/cDAQ_examples/cDAQ_TTRM_DRVG_AO.py sha256=cccdaefcde3d6ec944f9c716a42d9d014a324212e7ac2422de29930dc7e8e191 bytes=5410 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/cDAQ_examples/cDAQ_TTRM_DRVG_AO.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/cDAQ_examples/cDAQ_TTRM_DRVG_AO.py`
- sha256: `cccdaefcde3d6ec944f9c716a42d9d014a324212e7ac2422de29930dc7e8e191`
- bytes: 5410

````python
# Temperature Thermistor Measurement connected with DC Voltage Generation 
# import plotter as pl
import os
import sys

import nidaqmx
# import numpy as np  

import nipcbatt
from nipcbatt import daq

# To use save_traces and plotter from utils folder

parent_folder = os.getcwd()
utils_folder = os.path.join(parent_folder, "Utils")
sys.path.append(utils_folder)
# from save_traces import save_traces


# Global variables
plot_results = True
save_fig = False
use_specific_channel = False

# Initialize
drvg = daq.DcVoltageGeneration()
drvg.initialize(analog_output_channel_expression="Simulated_cDAQ_9263/ao0")
ttrm = daq.TemperatureMeasurementUsingThermistor()
ttrm.initialize("Simulated_cDAQ_9215/ai0")  

# region drvg configure and generate

range_settings = daq.VoltageGenerationChannelParameters(
    range_min_volts=-10.0, range_max_volts=10.0
)

output_voltages = [10.0]

drvg_config = daq.DcVoltageGenerationConfiguration(
    voltage_generation_range_parameters=range_settings, output_voltages=output_voltages
)

# endregion drvg configure and generate

drvg.configure_and_generate(drvg_config)

# region TTR configure and measure

coefficients_steinhart_hart_parameters = daq.CoefficientsSteinhartHartParameters(
    coefficient_steinhart_hart_a=0,
    coefficient_steinhart_hart_b=0,
    coefficient_steinhart_hart_c=0,
)

beta_coefficient_and_sensor_resistance_parameters = (
    daq.BetaCoefficientAndSensorResistanceParameters(
        coefficient_steinhart_hart_beta_kelvins=3720, sensor_resistance_ohms=10000
    )
)

global_channel_parameters = daq.TemperatureThermistorRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.DIFF,
    temperature_minimum_value_celsius_degrees=0,
    temperature_maximum_value_celsius_degrees=100,
    voltage_excitation_value_volts=10,
    thermistor_resistor_ohms=9910,
    steinhart_hart_equation_option=daq.SteinhartHartEquationOption.USE_COEFFICIENT_BETA_AND_SENSOR_RESISTANCE,
    coefficients_steinhart_hart_parameters=coefficients_steinhart_hart_parameters,
    beta_coefficient_and_sensor_resistance_parameters=beta_coefficient_and_sensor_resistance_parameters,
)

# region specific_channels_parameters

coefficients_steinhart_hart_parameters1 = daq.CoefficientsSteinhartHartParameters(
    coefficient_steinhart_hart_a=0,
    coefficient_steinhart_hart_b=0,
    coefficient_steinhart_hart_c=0,
)

beta_coefficient_and_sensor_resistance_parameters1 = (
    daq.BetaCoefficientAndSensorResistanceParameters(
        coefficient_steinhart_hart_beta_kelvins=3720, sensor_resistance_ohms=10000
    )
)

channel_parameters1 = daq.TemperatureThermistorRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.DIFF,
    temperature_minimum_value_celsius_degrees=0,
    temperature_maximum_value_celsius_degrees=100,
    voltage_excitation_value_volts=10,
    thermistor_resistor_ohms=8000,
    steinhart_hart_equation_option=daq.SteinhartHartEquationOption.USE_COEFFICIENT_BETA_AND_SENSOR_RESISTANCE,
    coefficients_steinhart_hart_parameters=coefficients_steinhart_hart_parameters1,
    beta_coefficient_and_sensor_resistance_parameters=beta_coefficient_and_sensor_resistance_parameters1,
)

channel0 = daq.TemperatureThermistorChannelRangeAndTerminalParameters(
    channel_name="Simulated_cDAQ_9215/ai0",
    channel_parameters=channel_parameters1,
)
specific_channels_parameters = []
if use_specific_channel is True:
    specific_channels_parameters.append(channel0)

# endregion specific_channels_parameters

sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=10000,
    number_of_samples_per_channel=1000,
    sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
    digital_start_trigger_source="",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

ttr_config = daq.TemperatureThermistorMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion TTR configure and measure

ttr_result_data = ttrm.configure_and_measure(configuration=ttr_config)

# Set DC Voltage to 0
output_voltages = [0.0]

drvg_config1 = daq.DcVoltageGenerationConfiguration(
    voltage_generation_range_parameters=range_settings, output_voltages=output_voltages
)

drvg.configure_and_generate(drvg_config1)

drvg.close()
ttrm.close()


print("TTR result :\n")
print(ttr_result_data)

# region save traces

# save_traces(
#     config=drvg_config,
#     file_name='DRVG'
# )

# save_traces(
#     config=ttr_config,
#     file_name='TTR',
#     result_data=ttr_result_data
# )

# endregion save traces

# region plot results

# if plot_results is True:
#     ttr_w = ttr_result_data.waveforms[0].samples.tolist()

#     pl.graph_plot(ttr_w)

# endregion plot results
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cc_source_and_measure/custom_dc_cc_source_and_measure.py sha256=9f82142064aa8aabbc7c7d0adfc3e1db7edad5b420d83b433767a1b9e4bb439d bytes=2586 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cc_source_and_measure/custom_dc_cc_source_and_measure.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cc_source_and_measure/custom_dc_cc_source_and_measure.py`
- sha256: `9f82142064aa8aabbc7c7d0adfc3e1db7edad5b420d83b433767a1b9e4bb439d`
- bytes: 2586

````python
"""DC constant current source and measure example with custom input parameters."""

import nidcpower

from nipcbatt import dcpower
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes DC CC source and measure using custom parameters."""
    dc_current_source_and_measure = dcpower.DCCurrentSourceAndMeasure()

    # Configure custom current channel settings
    current_channel_settings = dcpower.CurrentChannelSettings(
        current_level=10e-6,
        current_level_range=0.1,
        voltage_limit=1.0,
        voltage_limit_range=2.0,
        sensing=nidcpower.Sense.REMOTE,
        enable_output=True,
    )

    # Configure custom timing parameters
    timing_parameters = dcpower.TimingParameters(
        source_delay=0.1,
        aperture_time=0.02,
        transient_response=nidcpower.TransientResponse.NORMAL,
    )

    # Configure custom trigger parameters
    trigger_parameters = dcpower.TriggerParameters(
        source_trigger_behavior=dcpower.SourceTriggerBehavior.Disable_Source_Trigger,
        start_source_name="",
        export_event=dcpower.ExportEvent.NONE,
        event_signal_to_export=dcpower.EventSignalToExport.Source_Complete_Event,
        output_event_signal_terminal="",
    )

    # Build the full measurement configuration
    configuration = dcpower.DCCurrentSourceAndMeasureParameters(
        current_channel_settings=current_channel_settings,
        execution_settings=dcpower.ExecutionSettings(
            execution_type=dcpower.MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
            skip_analysis=False,
        ),
        timing_parameters=timing_parameters,
        trigger_parameters=trigger_parameters,
    )
    # ======================= Initialize the SMU/PPS ============================
    dc_current_source_and_measure.initialize(resource_name="SMU1/0")

    # PcbattLogger logs NI-DCPower configurations and measurement results
    # to the mentioned file path.
    logger = PcbattLogger(file="c:\\Temp\\dc_cc_source_and_measure_logger.txt")
    logger.attach(dc_current_source_and_measure)

    # ================== Custom measurement configuration ===================
    results = dc_current_source_and_measure.configure_and_measure(configuration=configuration)

    # ===================== Close the SMU/PPS session ===========================
    dc_current_source_and_measure.close()

    # Print the measurement results
    print(results)


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cc_source_and_measure/dc_cc_source_and_measure_in_loop.py sha256=45fb4dfa56b6e7f7761e282d4a1a51bc8fa290e79bd00e5bea0314d4d8cd0add bytes=3885 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cc_source_and_measure/dc_cc_source_and_measure_in_loop.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cc_source_and_measure/dc_cc_source_and_measure_in_loop.py`
- sha256: `45fb4dfa56b6e7f7761e282d4a1a51bc8fa290e79bd00e5bea0314d4d8cd0add`
- bytes: 3885

````python
"""DC constant current source and measure example running in a loop."""

import time

import nidcpower

from nipcbatt import dcpower
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures DC CC source once, then measures repeatedly in a loop."""
    dc_current_source_and_measure = dcpower.DCCurrentSourceAndMeasure()

    # Configure current channel settings
    current_channel_settings = dcpower.CurrentChannelSettings(
        current_level=10e-6,
        current_level_range=0.1,
        voltage_limit=1.0,
        voltage_limit_range=2.0,
        sensing=nidcpower.Sense.REMOTE,
        enable_output=True,
    )

    # Configure timing parameters
    timing_parameters = dcpower.TimingParameters(
        source_delay=0.1,
        aperture_time=0.02,
        transient_response=nidcpower.TransientResponse.NORMAL,
    )

    # Configure trigger parameters
    trigger_parameters = dcpower.TriggerParameters(
        source_trigger_behavior=dcpower.SourceTriggerBehavior.Disable_Source_Trigger,
        start_source_name="",
        export_event=dcpower.ExportEvent.NONE,
        event_signal_to_export=dcpower.EventSignalToExport.Source_Complete_Event,
        output_event_signal_terminal="",
    )

    def configuration(
        execution_type: dcpower.MeasurementExecutionType,
    ) -> dcpower.DCCurrentSourceAndMeasureParameters:
        """Builds a DCCurrentSourceAndMeasureParameters with shared channel/timing/trigger settings."""
        return dcpower.DCCurrentSourceAndMeasureParameters(
            current_channel_settings=current_channel_settings,
            execution_settings=dcpower.ExecutionSettings(
                execution_type=execution_type,
                skip_analysis=False,
            ),
            timing_parameters=timing_parameters,
            trigger_parameters=trigger_parameters,
        )

    # ======================= Initialize the SMU/PPS ====================
    dc_current_source_and_measure.initialize(resource_name="SMU1/0")

    # PcbattLogger logs NI-DCPower configurations and measurement results
    # to the mentioned file path.
    logger = PcbattLogger(file="c:\\Temp\\dc_cc_source_and_measure_in_loop_logger.txt")
    logger.attach(dc_current_source_and_measure)

    # ======================= Configure only ============================
    dc_current_source_and_measure.configure_and_measure(
        configuration=configuration(dcpower.MeasurementExecutionType.CONFIGURE_ONLY)
    )

    # ======================= Start source only =========================
    dc_current_source_and_measure.configure_and_measure(
        configuration=configuration(dcpower.MeasurementExecutionType.START_SOURCE_ONLY)
    )
    # Note: when the execution type is set to "configure_only" or "start_source_only" mode,
    #  the return data will contain valid values for "execution_settings" only and
    # "measurement_results" will be NaN after the execution.

    # ======================= Measure only in loop ======================
    num_iterations = 5
    for iteration in range(num_iterations):
        results = dc_current_source_and_measure.configure_and_measure(
            configuration=configuration(dcpower.MeasurementExecutionType.MEASURE_ONLY)
        )
        print(f"Iteration {iteration + 1}/{num_iterations}: {results}")
        time.sleep(1)  # Optional delay between measurements
        # Note: when the execution type is set to  "measure_only" or "configure_and_measure" mode,
        # the return data will contain valid values for both "execution_settings" and
        # "measurement_results" after the execution.

    # ======================= Close the SMU/PPS session =================
    dc_current_source_and_measure.close()


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cc_source_and_measure/default_dc_cc_source_and_measure.py sha256=277ea9c83b11613912cd1f179d4b86496f96cb11dd8ca72778e4420b11cd3227 bytes=1218 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cc_source_and_measure/default_dc_cc_source_and_measure.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cc_source_and_measure/default_dc_cc_source_and_measure.py`
- sha256: `277ea9c83b11613912cd1f179d4b86496f96cb11dd8ca72778e4420b11cd3227`
- bytes: 1218

````python
"""DC constant current source and measure example with default input parameters."""

from nipcbatt import dcpower
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes DC CC source and measure using default constants."""
    dc_current_source_and_measure = dcpower.DCCurrentSourceAndMeasure()

    # PcbattLogger logs NI-DCPower configurations and measurement results
    # to the mentioned file path.
    logger = PcbattLogger(file="c:\\Temp\\dc_cc_source_and_measure_logger.txt")
    logger.attach(dc_current_source_and_measure)

    # ======================= Initialize the SMU/PPS ============================
    dc_current_source_and_measure.initialize(resource_name="SMU1/0")

    # ================= Default measurement configuration ===================
    results = dc_current_source_and_measure.configure_and_measure(
        configuration=dcpower.DEFAULT_DC_CC_SOURCE_AND_MEASURE_PARAMETERS
    )

    # ===================== Close the SMU/PPS session ===========================
    dc_current_source_and_measure.close()

    # Print the measurement results
    print(results)


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cv_source_and_measure/custom_dc_cv_source_and_measure.py sha256=79bf45d2f4a10c1ead59db1d9cc6be35bc2779661dd6ca2e8ee499bb90caa36f bytes=2585 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cv_source_and_measure/custom_dc_cv_source_and_measure.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cv_source_and_measure/custom_dc_cv_source_and_measure.py`
- sha256: `79bf45d2f4a10c1ead59db1d9cc6be35bc2779661dd6ca2e8ee499bb90caa36f`
- bytes: 2585

````python
"""DC constant voltage source and measure example with custom input parameters."""

import nidcpower

from nipcbatt import dcpower
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes DC CV source and measure using custom parameters."""
    dc_voltage_source_and_measure = dcpower.DCVoltageSourceAndMeasure()

    # Configure custom voltage channel settings
    voltage_channel_settings = dcpower.VoltageChannelSettings(
        voltage_level=1.0,
        voltage_level_range=1.0,
        current_limit=0.01,
        current_limit_range=0.1,
        sensing=nidcpower.Sense.REMOTE,
        enable_output=True,
    )

    # Configure custom timing parameters
    timing_parameters = dcpower.TimingParameters(
        source_delay=0.1,
        aperture_time=0.02,
        transient_response=nidcpower.TransientResponse.NORMAL,
    )

    # Configure custom trigger parameters
    trigger_parameters = dcpower.TriggerParameters(
        source_trigger_behavior=dcpower.SourceTriggerBehavior.Disable_Source_Trigger,
        start_source_name="",
        export_event=dcpower.ExportEvent.NONE,
        event_signal_to_export=dcpower.EventSignalToExport.Source_Complete_Event,
        output_event_signal_terminal="",
    )

    # Build the full measurement configuration
    configuration = dcpower.DCVoltageSourceAndMeasureParameters(
        voltage_channel_settings=voltage_channel_settings,
        execution_settings=dcpower.ExecutionSettings(
            execution_type=dcpower.MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
            skip_analysis=False,
        ),
        timing_parameters=timing_parameters,
        trigger_parameters=trigger_parameters,
    )
    # ======================= Initialize the SMU/PPS ============================
    dc_voltage_source_and_measure.initialize(resource_name="PPS1/0")

    # PcbattLogger logs NI-DCPower configurations and measurement results
    # to the mentioned file path.
    logger = PcbattLogger(file="c:\\Temp\\dc_cv_source_and_measure_logger.txt")
    logger.attach(dc_voltage_source_and_measure)

    # ================== Custom measurement configuration ===================
    results = dc_voltage_source_and_measure.configure_and_measure(configuration=configuration)

    # ===================== Close the SMU/PPS session ===========================
    dc_voltage_source_and_measure.close()

    # Print the measurement results
    print(results)


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cv_source_and_measure/dc_cv_source_and_measure_in_loop.py sha256=fe8fe316ddd45de5253f3887937d6c7642f006269d034a30fceeb0fb7c808d5b bytes=3884 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cv_source_and_measure/dc_cv_source_and_measure_in_loop.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cv_source_and_measure/dc_cv_source_and_measure_in_loop.py`
- sha256: `fe8fe316ddd45de5253f3887937d6c7642f006269d034a30fceeb0fb7c808d5b`
- bytes: 3884

````python
"""DC constant voltage source and measure example running in a loop."""

import time

import nidcpower

from nipcbatt import dcpower
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures DC CV source once, then measures repeatedly in a loop."""
    dc_voltage_source_and_measure = dcpower.DCVoltageSourceAndMeasure()

    # Configure voltage channel settings
    voltage_channel_settings = dcpower.VoltageChannelSettings(
        voltage_level=1.0,
        voltage_level_range=1.0,
        current_limit=0.01,
        current_limit_range=0.1,
        sensing=nidcpower.Sense.REMOTE,
        enable_output=True,
    )

    # Configure timing parameters
    timing_parameters = dcpower.TimingParameters(
        source_delay=0.1,
        aperture_time=0.02,
        transient_response=nidcpower.TransientResponse.NORMAL,
    )

    # Configure trigger parameters
    trigger_parameters = dcpower.TriggerParameters(
        source_trigger_behavior=dcpower.SourceTriggerBehavior.Disable_Source_Trigger,
        start_source_name="",
        export_event=dcpower.ExportEvent.NONE,
        event_signal_to_export=dcpower.EventSignalToExport.Source_Complete_Event,
        output_event_signal_terminal="",
    )

    def configuration(
        execution_type: dcpower.MeasurementExecutionType,
    ) -> dcpower.DCVoltageSourceAndMeasureParameters:
        """Builds a DCVoltageSourceAndMeasureParameters with shared channel/timing/trigger settings."""
        return dcpower.DCVoltageSourceAndMeasureParameters(
            voltage_channel_settings=voltage_channel_settings,
            execution_settings=dcpower.ExecutionSettings(
                execution_type=execution_type,
                skip_analysis=False,
            ),
            timing_parameters=timing_parameters,
            trigger_parameters=trigger_parameters,
        )

    # ======================= Initialize the SMU/PPS ====================
    dc_voltage_source_and_measure.initialize(resource_name="PPS1/0")

    # PcbattLogger logs NI-DCPower configurations and measurement results
    # to the mentioned file path.
    logger = PcbattLogger(file="c:\\Temp\\dc_cv_source_and_measure_in_loop_logger.txt")
    logger.attach(dc_voltage_source_and_measure)

    # ======================= Configure only ============================
    dc_voltage_source_and_measure.configure_and_measure(
        configuration=configuration(dcpower.MeasurementExecutionType.CONFIGURE_ONLY)
    )

    # ======================= Start source only =========================
    dc_voltage_source_and_measure.configure_and_measure(
        configuration=configuration(dcpower.MeasurementExecutionType.START_SOURCE_ONLY)
    )
    # Note: when the execution type is set to "configure_only" or "start_source_only" mode,
    #  the return data will contain valid values for "execution_settings" only and
    # "measurement_results" will be NaN after the execution.

    # ======================= Measure only in loop ======================
    num_iterations = 5
    for iteration in range(num_iterations):
        results = dc_voltage_source_and_measure.configure_and_measure(
            configuration=configuration(dcpower.MeasurementExecutionType.MEASURE_ONLY)
        )
        print(f"Iteration {iteration + 1}/{num_iterations}: {results}")
        time.sleep(1)  # Optional delay between measurements
        # Note: when the execution type is set to  "measure_only" or "configure_and_measure" mode,
        # the return data will contain valid values for both "execution_settings" and
        # "measurement_results" after the execution.

    # ======================= Close the SMU/PPS session =================
    dc_voltage_source_and_measure.close()


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cv_source_and_measure/default_dc_cv_source_and_measure.py sha256=bae1dd82734d640e84165d33bb7c9b272233be5d2e12746b749b5dd70c1e4f09 bytes=1218 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cv_source_and_measure/default_dc_cv_source_and_measure.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/dcpower_examples/dc_cv_source_and_measure/default_dc_cv_source_and_measure.py`
- sha256: `bae1dd82734d640e84165d33bb7c9b272233be5d2e12746b749b5dd70c1e4f09`
- bytes: 1218

````python
"""DC constant voltage source and measure example with default input parameters."""

from nipcbatt import dcpower
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes DC CV source and measure using default constants."""
    dc_voltage_source_and_measure = dcpower.DCVoltageSourceAndMeasure()

    # PcbattLogger logs NI-DCPower configurations and measurement results
    # to the mentioned file path.
    logger = PcbattLogger(file="c:\\Temp\\dc_cv_source_and_measure_logger.txt")
    logger.attach(dc_voltage_source_and_measure)

    # ======================= Initialize the SMU/PPS ============================
    dc_voltage_source_and_measure.initialize(resource_name="PPS1/0")

    # ================= Default measurement configuration ===================
    results = dc_voltage_source_and_measure.configure_and_measure(
        configuration=dcpower.DEFAULT_DC_CV_SOURCE_AND_MEASURE_PARAMETERS
    )

    # ===================== Close the SMU/PPS session ===========================
    dc_voltage_source_and_measure.close()

    # Print the measurement results
    print(results)


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_current_measurement/current_measurement_in_loop.py sha256=2fec28b09367b99886aab915f4bcfa5835a7c4c8304682ec987b610522ad8ca4 bytes=3260 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_current_measurement/current_measurement_in_loop.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_current_measurement/current_measurement_in_loop.py`
- sha256: `2fec28b09367b99886aab915f4bcfa5835a7c4c8304682ec987b610522ad8ca4`
- bytes: 3260

````python
"""DMM DC-RMS Current measurement in loop example with custom input parameters."""

import time

import nidmm

import nipcbatt
from nipcbatt import dmm
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes custom DMM DC-RMS current measurement with logging."""
    dmm_current_measurement = dmm.DcRmsCurrentMeasurement()

    # PcbattLogger logs DMM configurations and measurement results to the mentioned file path.
    logger = PcbattLogger(file="c:\\Temp\\current_measurement_logger.txt")
    logger.attach(dmm_current_measurement)

    # Configure the measurement configuration for the DMM DC-RMS current measurement
    config = dmm.DcRmsCurrentMeasurementConfiguration(
        nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        trigger_parameters=dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.IMMEDIATE,
            trigger_delay=5.0,
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=False,
        ),
        measurement_function_parameters=dmm.DcRmsCurrentMeasurementFunctionParameters(
            measurement_function=dmm.CurrentRangeAndFunctions.DC_1A,
            resolution_in_digits=dmm.ResolutionInDigits.DIGITS_5_5,
        ),
        timing_parameters=dmm.TimingParameters(
            aperture_time_seconds=-1.0,
            settle_time_seconds=-1.0,
        ),
        ac_min_frequency=40.0,
    )

    # Number of measurements to take in the loop
    number_of_measurements = 5

    # ======================= Initialize the DMM ============================
    dmm_current_measurement.initialize("Sim_DMM", 50)

    # ================= Configure once, then measure in a loop ===================
    config_only = dmm.DcRmsCurrentMeasurementConfiguration(
        nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
        trigger_parameters=config.trigger_parameters,
        measurement_function_parameters=config.measurement_function_parameters,
        timing_parameters=config.timing_parameters,
        ac_min_frequency=config.ac_min_frequency,
    )

    measure_only = dmm.DcRmsCurrentMeasurementConfiguration(
        nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
        trigger_parameters=config.trigger_parameters,
        measurement_function_parameters=config.measurement_function_parameters,
        timing_parameters=config.timing_parameters,
        ac_min_frequency=config.ac_min_frequency,
    )

    # Configure the DMM once before the loop
    dmm_current_measurement.configure_and_measure(configuration=config_only)

    # Measure in a loop
    for i in range(number_of_measurements):
        measurement = {}
        # Perform measurement using the measure_only configuration in the loop and store the result in the measurement dictionary
        measurement["value"] = dmm_current_measurement.configure_and_measure(
            configuration=measure_only
        )
        print(measurement["value"])
        time.sleep(2)  # Wait for 2 seconds between measurements

    # ===================== Close the DMM session ===========================
    dmm_current_measurement.close()


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_current_measurement/custom_dc_rms_current_measurement.py sha256=0c20a56cd456e937bf2508801502d78974b0d7a1e90596bf612b9c2b14099ea7 bytes=1970 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_current_measurement/custom_dc_rms_current_measurement.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_current_measurement/custom_dc_rms_current_measurement.py`
- sha256: `0c20a56cd456e937bf2508801502d78974b0d7a1e90596bf612b9c2b14099ea7`
- bytes: 1970

````python
"""DMM DC-RMS Current measurement example with custom input parameters."""

import nidmm

import nipcbatt
from nipcbatt import dmm
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes custom DMM DC-RMS current measurement with logging."""
    dmm_current_measurement = dmm.DcRmsCurrentMeasurement()

    # PcbattLogger logs DMM configurations and measurement results to the mentioned file path.
    logger = PcbattLogger(file="c:\\Temp\\current_measurement_logger.txt")
    logger.attach(dmm_current_measurement)

    # Configure the measurement configuration for the DMM DC-RMS current measurement
    config = dmm.DcRmsCurrentMeasurementConfiguration(
        nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        trigger_parameters=dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.IMMEDIATE,
            trigger_delay=5.0,
            slope=dmm.Slope.FALLING_EDGE,
            enable_trigger=False,
        ),
        measurement_function_parameters=dmm.DcRmsCurrentMeasurementFunctionParameters(
            measurement_function=dmm.CurrentRangeAndFunctions.DC_1A,
            resolution_in_digits=dmm.ResolutionInDigits.DIGITS_3_5,
        ),
        timing_parameters=dmm.TimingParameters(
            aperture_time_seconds=-1.0,
            settle_time_seconds=-1.0,
        ),
        ac_min_frequency=40.0,
    )
    # ======================= Initialize the DMM ============================
    dmm_current_measurement.initialize("Sim_DMM", 50)

    # ================= Custom measurement configuration ===================
    measurement = dmm_current_measurement.configure_and_measure(configuration=config)

    # ===================== Close the DMM session ===========================
    dmm_current_measurement.close()

    # Print the measurement result
    print(measurement)


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_current_measurement/default_dc_rms_current_measurement.py sha256=1bd4daa629d9129213d1b58cb80dbe5a3ce7331a327b4e1b89a8d1233cc019d3 bytes=1143 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_current_measurement/default_dc_rms_current_measurement.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_current_measurement/default_dc_rms_current_measurement.py`
- sha256: `1bd4daa629d9129213d1b58cb80dbe5a3ce7331a327b4e1b89a8d1233cc019d3`
- bytes: 1143

````python
"""DMM DC-RMS Current measurement example with default input parameters."""

from nipcbatt import dmm
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes default DMM DC-RMS current measurement with logging."""
    dmm_current_measurement = dmm.DcRmsCurrentMeasurement()

    # PcbattLogger logs DMM configurations and measurement results to the mentioned file path.
    logger = PcbattLogger(file="c:\\Temp\\current_measurement_logger.txt")
    logger.attach(dmm_current_measurement)

    # ======================= Initialize the DMM ============================
    dmm_current_measurement.initialize("Sim_DMM", 50)

    # ================= Default measurement configuration ===================
    measurement = dmm_current_measurement.configure_and_measure(
        configuration=dmm.DEFAULT_DC_RMS_CURRENT_MEASUREMENT_CONFIGURATION
    )

    # ===================== Close the DMM session ===========================
    dmm_current_measurement.close()

    # Print the measurement result
    print(measurement)


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_voltage_measurement/custom_dc_rms_voltage_measurement.py sha256=e9a5ff13abdb297d45b8149f53836b32227881fba717b9bcef04b10e7b32d9b9 bytes=1969 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_voltage_measurement/custom_dc_rms_voltage_measurement.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_voltage_measurement/custom_dc_rms_voltage_measurement.py`
- sha256: `e9a5ff13abdb297d45b8149f53836b32227881fba717b9bcef04b10e7b32d9b9`
- bytes: 1969

````python
"""DMM DC-RMS Voltage measurement example with custom input parameters."""

import nidmm

import nipcbatt
from nipcbatt import dmm
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes custom DMM DC-RMS voltage measurement with logging."""
    dmm_voltage_measurement = dmm.DcRmsVoltageMeasurement()

    # PcbattLogger logs DMM configurations and measurement results to the mentioned file path.
    logger = PcbattLogger(file="c:\\Temp\\voltage_measurement_logger.txt")
    logger.attach(dmm_voltage_measurement)

    # Configure the measurement configuration for the DMM DC-RMS voltage measurement
    config = dmm.DcRmsVoltageMeasurementConfiguration(
        nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        trigger_parameters=dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.IMMEDIATE,
            trigger_delay=5.0,
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=False,
        ),
        measurement_function_parameters=dmm.DcRmsVoltageMeasurementFunctionParameters(
            measurement_function=dmm.VoltageRangeAndFunctions.DC_1V,
            resolution_in_digits=dmm.ResolutionInDigits.DIGITS_5_5,
        ),
        timing_parameters=dmm.TimingParameters(
            aperture_time_seconds=-1.0,
            settle_time_seconds=-1.0,
        ),
        ac_min_frequency=40.0,
    )
    # ======================= Initialize the DMM ============================
    dmm_voltage_measurement.initialize("Sim_DMM", 50)

    # ================= Custom measurement configuration ===================
    measurement = dmm_voltage_measurement.configure_and_measure(configuration=config)

    # ===================== Close the DMM session ===========================
    dmm_voltage_measurement.close()

    # Print the measurement result
    print(measurement)


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_voltage_measurement/default_dc_rms_voltage_measurement.py sha256=66a7da3b9bdad76d11b694f860adfff33cf9d24b424c3dbe3d87d021267bfbec bytes=1143 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_voltage_measurement/default_dc_rms_voltage_measurement.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_voltage_measurement/default_dc_rms_voltage_measurement.py`
- sha256: `66a7da3b9bdad76d11b694f860adfff33cf9d24b424c3dbe3d87d021267bfbec`
- bytes: 1143

````python
"""DMM DC-RMS Voltage measurement example with default input parameters."""

from nipcbatt import dmm
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes default DMM DC-RMS voltage measurement with logging."""
    dmm_voltage_measurement = dmm.DcRmsVoltageMeasurement()

    # PcbattLogger logs DMM configurations and measurement results to the mentioned file path.
    logger = PcbattLogger(file="c:\\Temp\\voltage_measurement_logger.txt")
    logger.attach(dmm_voltage_measurement)

    # ======================= Initialize the DMM ============================
    dmm_voltage_measurement.initialize("Sim_DMM", 50)

    # ================= Default measurement configuration ===================
    measurement = dmm_voltage_measurement.configure_and_measure(
        configuration=dmm.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION
    )

    # ===================== Close the DMM session ===========================
    dmm_voltage_measurement.close()

    # Print the measurement result
    print(measurement)


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_voltage_measurement/PXI_HW_trigger_delay_voltage_measurement.py sha256=74ec8fb97c56cd7c8708796992d606eff9edcc3838266b914f052fd6a5dc668f bytes=3831 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_voltage_measurement/PXI_HW_trigger_delay_voltage_measurement.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_voltage_measurement/PXI_HW_trigger_delay_voltage_measurement.py`
- sha256: `74ec8fb97c56cd7c8708796992d606eff9edcc3838266b914f052fd6a5dc668f`
- bytes: 3831

````python
"""Signal Voltage Generation connected to DMM DC-RMS Voltage Measurement.""" 
### Ensure correct hardware and corresponding trigger names before running this example

import threading
import time

import nidaqmx.constants
import nidmm

import nipcbatt
from nipcbatt import dmm, daq
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

def main():
    # Initialize SVG and DMM
    svg = daq.SignalVoltageGeneration()
    svg.initialize(channel_expression="Sim_PXIeDAQ/ao0")

    dmm_voltage_measurement = dmm.DcRmsVoltageMeasurement()
    dmm_voltage_measurement.initialize("Sim_DMM", 50.0)

    # PcbattLogger logs DMM configurations and measurement results to the mentioned file path.
    logger = PcbattLogger(file="c:\\Temp\\svg_dmm_logger.txt")
    logger.attach(dmm_voltage_measurement)

    # SVG parameters configuration
    voltage_generation_range_parameters = daq.VoltageGenerationChannelParameters(
        range_min_volts=-10.0,
        range_max_volts=10.0,
    )

    svg_timing_parameters = daq.SignalVoltageGenerationTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=100000,
        generated_signal_duration_seconds=4.0,  
    )

    svg_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    svg_tone_parameters = daq.ToneParameters(
        tone_frequency_hertz=100,   
        tone_amplitude_volts=10.0,   
        tone_phase_radians=0,
    )

    svg_waveform_parameters = daq.SignalVoltageGenerationSineWaveParameters(
        generated_signal_offset_volts=0,
        generated_signal_tone_parameters=svg_tone_parameters,
    )

    svg.configure_all_channels(parameters=voltage_generation_range_parameters)
    svg.configure_timing(parameters=svg_timing_parameters)
    svg.configure_trigger(parameters=svg_trigger_parameters)

    # Route AO start-trigger → PXI_Trig0
    svg.route_start_trigger_signal_to_terminal("PXI_Trig0")

    # Configure DMM to wait for trigger on PXI_Trig0
    dmm_config = dmm.DcRmsVoltageMeasurementConfiguration(
        execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        measurement_function_parameters=dmm.DcRmsVoltageMeasurementFunctionParameters(
            measurement_function=dmm.VoltageRangeAndFunctions.AC_20V,
            resolution_in_digits=dmm.ResolutionInDigits.DIGITS_5_5,
        ),
        trigger_parameters=dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.PXI_TRIG0,  
            trigger_delay=1.0,                              
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=True,
        ),
        timing_parameters=dmm.TimingParameters(
            aperture_time_seconds=-1.0,  
            settle_time_seconds=-1.0,    
        ),
        ac_min_frequency=40.0,
    )

    # DMM voltage measurement in background thread 
    dmm_result = {}

    def _dmm_measure():
        dmm_result["value"] = dmm_voltage_measurement.configure_and_measure(
            configuration=dmm_config
        )

    dmm_thread = threading.Thread(target=_dmm_measure, daemon=True)
    dmm_thread.start()

    # 2 seconds wait
    time.sleep(2.0)

    svg.generate_voltage_sine_waveform(
        signal_parameters=svg_waveform_parameters,
        timing_parameters=svg_timing_parameters,
    )

    # Wait for DMM thread to complete 
    dmm_thread.join(timeout=15.0)

    # Close resources
    svg.close()
    dmm_voltage_measurement.close()

    # Print the DMM measurement result
    print(dmm_result["value"])


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_voltage_measurement/voltage_measurement_in_loop.py sha256=dc9d1fe7ea29b4a96755878bc56f43412d5b30249f301911dcac359ff7ac57f6 bytes=3256 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_voltage_measurement/voltage_measurement_in_loop.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/DMM_examples/dc_rms_voltage_measurement/voltage_measurement_in_loop.py`
- sha256: `dc9d1fe7ea29b4a96755878bc56f43412d5b30249f301911dcac359ff7ac57f6`
- bytes: 3256

````python
"""DMM DC-RMS Voltage measurement in loop example with custom input parameters."""

import time

import nidmm

import nipcbatt
from nipcbatt import dmm
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes custom DMM DC-RMS voltage measurement with logging."""
    dmm_voltage_measurement = dmm.DcRmsVoltageMeasurement()

    # PcbattLogger logs DMM configurations and measurement results to the mentioned file path.
    logger = PcbattLogger(file="c:\\Temp\\voltage_measurement_logger.txt")
    logger.attach(dmm_voltage_measurement)

    # Configure the measurement configuration for the DMM DC-RMS voltage measurement
    config = dmm.DcRmsVoltageMeasurementConfiguration(
        nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        trigger_parameters=dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.IMMEDIATE,
            trigger_delay=5.0,
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=False,
        ),
        measurement_function_parameters=dmm.DcRmsVoltageMeasurementFunctionParameters(
            measurement_function=dmm.VoltageRangeAndFunctions.DC_10V,
            resolution_in_digits=dmm.ResolutionInDigits.DIGITS_5_5,
        ),
        timing_parameters=dmm.TimingParameters(
            aperture_time_seconds=-1.0,
            settle_time_seconds=-1.0,
        ),
        ac_min_frequency=40.0,
    )
    # Number of measurements to take in the loop
    number_of_measurements = 5

    # ======================= Initialize the DMM ============================
    dmm_voltage_measurement.initialize("Sim_DMM", 50)

    # ================= Configure once, then measure in a loop ===================
    config_only = dmm.DcRmsVoltageMeasurementConfiguration(
        nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
        trigger_parameters=config.trigger_parameters,
        measurement_function_parameters=config.measurement_function_parameters,
        timing_parameters=config.timing_parameters,
        ac_min_frequency=config.ac_min_frequency,
    )

    measure_only = dmm.DcRmsVoltageMeasurementConfiguration(
        nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
        trigger_parameters=config.trigger_parameters,
        measurement_function_parameters=config.measurement_function_parameters,
        timing_parameters=config.timing_parameters,
        ac_min_frequency=config.ac_min_frequency,
    )

    # Configure the DMM once before the loop
    dmm_voltage_measurement.configure_and_measure(configuration=config_only)

    # Measure in a loop
    for i in range(number_of_measurements):
        measurement = {}
        # Perform measurement using the measure_only configuration in the loop and store the result in the measurement dictionary
        measurement["value"] = dmm_voltage_measurement.configure_and_measure(
            configuration=measure_only
        )
        print(measurement['value'])
        time.sleep(2) # Wait for 2 seconds between measurements

    # ===================== Close the DMM session ===========================
    dmm_voltage_measurement.close()


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_examples/mixed_measurement/custom_mixed_measurement.py sha256=59901154eca7bef30a229c505c2ae94fb034310d5c068776552d123e208325eb bytes=1938 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/DMM_examples/mixed_measurement/custom_mixed_measurement.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/DMM_examples/mixed_measurement/custom_mixed_measurement.py`
- sha256: `59901154eca7bef30a229c505c2ae94fb034310d5c068776552d123e208325eb`
- bytes: 1938

````python
"""DMM Mixed measurement example with custom input parameters."""

import nidmm

import nipcbatt
from nipcbatt.pcbatt_library import dmm
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes custom DMM mixed measurement with logging."""
    dmm_mixed_measurement = dmm.MixedMeasurement()

    # PcbattLogger logs DMM configurations and measurement results to the mentioned file path.
    logger = PcbattLogger(file="c:\\Temp\\mixed_measurement_logger.txt")
    logger.attach(dmm_mixed_measurement)

    # Configure the measurement configuration for the mixed measurement
    config = dmm.MixedMeasurementConfiguration(
        execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        trigger_parameters=dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.IMMEDIATE,
            trigger_delay=2.0,
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=False,
        ),
        measurement_function_parameters=dmm.MixedMeasurementFunctionParameters(
            measurement_function=dmm.MixedRangeAndFunctions.AC_100uA,
            resolution_in_digits=dmm.ResolutionInDigits.DIGITS_5_5,
        ),
        timing_parameters=dmm.TimingParameters(
            aperture_time_seconds=-1.0,
            settle_time_seconds=-1.0,
        ),
        ac_min_frequency=40.0,
    )
    # ======================= Initialize the DMM ============================
    dmm_mixed_measurement.initialize("Sim_DMM", 50)

    # ================= Custom measurement configuration ===================
    measurement = dmm_mixed_measurement.configure_and_measure(configuration=config)

    # ===================== Close the DMM session ===========================
    dmm_mixed_measurement.close()

    # Print the measurement result
    print(measurement)


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_examples/mixed_measurement/default_mixed_measurement.py sha256=97e9505a1b9c9d10d45d417cd6d89c5cf145135d8a599a4c29b079f0068befdc bytes=1091 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/DMM_examples/mixed_measurement/default_mixed_measurement.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/DMM_examples/mixed_measurement/default_mixed_measurement.py`
- sha256: `97e9505a1b9c9d10d45d417cd6d89c5cf145135d8a599a4c29b079f0068befdc`
- bytes: 1091

````python
"""Mixed measurement example with default input parameters."""

from nipcbatt import dmm
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes default Mixed measurement with logging."""
    dmm_mixed_measurement = dmm.MixedMeasurement()

    # PcbattLogger logs DMM configurations and measurement results to the mentioned file path.
    logger = PcbattLogger(file="c:\\Temp\\mixed_measurement_logger.txt")
    logger.attach(dmm_mixed_measurement)

    # ======================= Initialize the DMM ============================
    dmm_mixed_measurement.initialize("Sim_DMM", 50)

    # ================= Default measurement configuration ===================
    measurement = dmm_mixed_measurement.configure_and_measure(
        configuration=dmm.DEFAULT_MIXED_MEASUREMENT_CONFIGURATION
    )

    # ===================== Close the DMM session ===========================
    dmm_mixed_measurement.close()

    # Print the measurement result
    print(measurement)


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_examples/resistance_measurement/custom_resistance_measurement.py sha256=64a18c790aa31d0ce70c6f310b5d0cac53e8fbf6fb83652d249cbca1d09acabc bytes=1931 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/DMM_examples/resistance_measurement/custom_resistance_measurement.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/DMM_examples/resistance_measurement/custom_resistance_measurement.py`
- sha256: `64a18c790aa31d0ce70c6f310b5d0cac53e8fbf6fb83652d249cbca1d09acabc`
- bytes: 1931

````python
"""Resistance measurement example with custom input parameters."""

import nidmm

import nipcbatt
from nipcbatt import dmm
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes custom resistance measurement with logging."""
    resistance_measurement = dmm.DcRmsResistanceMeasurement()

    # PcbattLogger logs DMM configurations and measurement results to the mentioned file path.
    logger = PcbattLogger(file="c:\\Temp\\resistance_measurement_logger.txt")
    logger.attach(resistance_measurement)

    # Configure the measurement configuration for the resistance measurement
    config = dmm.ResistanceMeasurementConfiguration(
        execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        trigger_parameters=dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.IMMEDIATE,
            trigger_delay=-1.0,
            slope=dmm.Slope.FALLING_EDGE,
            enable_trigger=False,
        ),
        measurement_function_parameters=dmm.ResistanceMeasurementFunctionParameters(
            measurement_function=dmm.ResistanceRangeAndFunctions.TWO_W_RES_100k_Ohm,
            resolution_in_digits=dmm.ResolutionInDigits.DIGITS_6_5,
        ),
        timing_parameters=dmm.TimingParameters(
            aperture_time_seconds=-1.0, settle_time_seconds=-1.0
        ),
    )

    # ======================= Initialize the DMM ============================
    resistance_measurement.initialize("Sim_DMM", 50)

    # ================= Custom measurement configuration ===================
    measurement = resistance_measurement.configure_and_measure(configuration=config)

    # ===================== Close the DMM session ===========================
    resistance_measurement.close()

    # Print the measurement result
    print(measurement)


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_examples/resistance_measurement/default_resistance_measurement.py sha256=4d79f9b2787983820ab41b992db0d57a4532c4423005be49335ca78c95ef22f3 bytes=1124 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/DMM_examples/resistance_measurement/default_resistance_measurement.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/DMM_examples/resistance_measurement/default_resistance_measurement.py`
- sha256: `4d79f9b2787983820ab41b992db0d57a4532c4423005be49335ca78c95ef22f3`
- bytes: 1124

````python
"""Resistance measurement example with default input parameters."""

from nipcbatt import dmm
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes default resistance measurement with logging."""
    resistance_measurement = dmm.DcRmsResistanceMeasurement()

    # PcbattLogger logs DMM configurations and measurement results to the mentioned file path.
    logger = PcbattLogger(file="c:\\Temp\\resistance_measurement_logger.txt")
    logger.attach(resistance_measurement)

    # ======================= Initialize the DMM ============================
    resistance_measurement.initialize("Sim_DMM", 50)

    # ================= Default measurement configuration ===================
    measurement = resistance_measurement.configure_and_measure(
        configuration=dmm.DEFAULT_RESISTANCE_MEASUREMENT_CONFIGURATION
    )

    # ===================== Close the DMM session ===========================
    resistance_measurement.close()

    # Print the measurement result
    print(measurement)


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_SCAN_examples/dmm_loop_scan_pmps_example.py sha256=6af91476642b9c55a1a0d1efbfdd8c6756c40f0ed604e7481b9ccdcba0205128 bytes=2499 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/DMM_SCAN_examples/dmm_loop_scan_pmps_example.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/DMM_SCAN_examples/dmm_loop_scan_pmps_example.py`
- sha256: `6af91476642b9c55a1a0d1efbfdd8c6756c40f0ed604e7481b9ccdcba0205128`
- bytes: 2499

````python
# pylint: disable=C0200, C0103, C0301

"""This example executes a DMM Scan in a loop 5 times with a 2 second
   delay between iterations. Each iteration scans 3 voltage and 3 current
   measurements and prints the results."""

import time

from nipcbatt import dmm
from nipcbatt import dmm_scan

############### DECLARE INPUT VALUES ########################################################

# edit this list to define the configurations to use during the scan
# each entry should be a list in the format below:
# [channel (int), range & function (MixedRangeAndFunctions), resolution (ResolutionInDigits)]
scan_configuration = [
    [1,  dmm.MixedRangeAndFunctions.DC_10V,               dmm.ResolutionInDigits.DIGITS_5_5],
    [2,  dmm.MixedRangeAndFunctions.DC_1V,                dmm.ResolutionInDigits.DIGITS_5_5],
    [3,  dmm.MixedRangeAndFunctions.DC_10V,               dmm.ResolutionInDigits.DIGITS_5_5],
    [16, dmm.MixedRangeAndFunctions.DC_100mA,             dmm.ResolutionInDigits.DIGITS_5_5],
    [17, dmm.MixedRangeAndFunctions.DC_10mA,              dmm.ResolutionInDigits.DIGITS_5_5],
    [18, dmm.MixedRangeAndFunctions.DC_100mA,             dmm.ResolutionInDigits.DIGITS_5_5]
]

#Declare constants for initialization
mux_resource_name = "Sim_MUX"
shunt_resource_name = "Sim_SHUNT"
dmm_resource_name = "Sim_DMM"

mux_topology_name = "2527/2-Wire Dual 16x1 Mux"
shunt_topology_name = "2568/31-SPST"

powerline_freq = 50
close_all_shunts = True
verbose = True # Set to False to not print measurements to console
num_iterations = 5
delay_between_iterations = 2  # seconds

############ EXECUTE SCAN ####################################################################

# Create scan object
scan = dmm_scan.DmmScanPMPS()

# Initialize scan object
resources = scan.initialize(
    mux_resource_name,
    mux_topology_name,
    shunt_resource_name,
    shunt_topology_name,
    dmm_resource_name,
    powerline_freq,
    close_all_shunts
)

# Execute scan loop
for i in range(num_iterations):

    print(f"\n########################### ITERATION {i + 1} of {num_iterations} #######################################")

    # Execute full scan
    results = scan.configure_and_measure(resources, scan_configuration, verbose)

    # Wait before next iteration (skip delay after last iteration)
    if i < num_iterations - 1:
        time.sleep(delay_between_iterations)

# Disconnect and close resources
scan.close(resources)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_SCAN_examples/dmm_scan_pmps_example.py sha256=1a45ed3dff5e2de6237bf1ece1bd0359a0069af543979272b903c90eb222522c bytes=2037 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/DMM_SCAN_examples/dmm_scan_pmps_example.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/DMM_SCAN_examples/dmm_scan_pmps_example.py`
- sha256: `1a45ed3dff5e2de6237bf1ece1bd0359a0069af543979272b903c90eb222522c`
- bytes: 2037

````python
# pylint: disable=C0200, C0103, C0301

"""This example executes a DMM Scan to obtain 3 voltage, 3 current
   measurement. It returns both the formatted and the raw measurements."""

from nipcbatt import dmm
from nipcbatt import dmm_scan

############### DECLARE INPUT VALUES ########################################################

# edit this list to define the configurations to use during the scan
# each entry should be a list in the format below:
# [channel (int), range & function (MixedRangeAndFunctions), resolution (ResolutionInDigits)]
scan_configuration = [
    [1,  dmm.MixedRangeAndFunctions.DC_10V,               dmm.ResolutionInDigits.DIGITS_5_5],
    [2,  dmm.MixedRangeAndFunctions.DC_1V,                dmm.ResolutionInDigits.DIGITS_5_5],
    [3,  dmm.MixedRangeAndFunctions.DC_10V,               dmm.ResolutionInDigits.DIGITS_5_5],
    [16, dmm.MixedRangeAndFunctions.DC_100mA,             dmm.ResolutionInDigits.DIGITS_5_5],
    [17, dmm.MixedRangeAndFunctions.DC_10mA,              dmm.ResolutionInDigits.DIGITS_5_5],
    [18, dmm.MixedRangeAndFunctions.DC_100mA,             dmm.ResolutionInDigits.DIGITS_5_5]
]

#Declare constants for initialization
mux_resource_name = "Sim_MUX"
shunt_resource_name = "Sim_SHUNT"
dmm_resource_name = "Sim_DMM"

mux_topology_name = "2527/2-Wire Dual 16x1 Mux"
shunt_topology_name = "2568/31-SPST"

powerline_freq = 50
close_all_shunts = True
verbose = True # Set to False to not print measurements to console


############ EXECUTE SCAN ####################################################################

# Create scan object
scan = dmm_scan.DmmScanPMPS()

# Initialize scan object
resources = scan.initialize(
    mux_resource_name,
    mux_topology_name,
    shunt_resource_name,
    shunt_topology_name,
    dmm_resource_name,
    powerline_freq,
    close_all_shunts
)

# Execute scan
results = scan.configure_and_measure(resources, scan_configuration, verbose)

# Disconnect and close resources
scan.close(resources)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/DMM_SCAN_examples/dmm_two_scan_pmps_example.py sha256=cc9cf8442968fa3ec531e262f7ab0dd4ffb9df1033a8e593c5cee2300e97da5d bytes=2981 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/DMM_SCAN_examples/dmm_two_scan_pmps_example.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/DMM_SCAN_examples/dmm_two_scan_pmps_example.py`
- sha256: `cc9cf8442968fa3ec531e262f7ab0dd4ffb9df1033a8e593c5cee2300e97da5d`
- bytes: 2981

````python
# pylint: disable=C0200, C0103, C0301

"""This example executes a DMM Scan to obtain 3 voltage, 3 current
   measurement. It returns both the formatted and the raw measurements."""

from nipcbatt import dmm
from nipcbatt import dmm_scan

############### DECLARE INPUT VALUES ########################################################

# edit these lists to define the configurations to use during the scan
# each entry should be a list in the format below:
# [channel (int), range & function (MixedRangeAndFunctions), resolution (ResolutionInDigits)]
scan_configuration1 = [
    [1,  dmm.MixedRangeAndFunctions.DC_10V,               dmm.ResolutionInDigits.DIGITS_5_5],
    [2,  dmm.MixedRangeAndFunctions.DC_1V,                dmm.ResolutionInDigits.DIGITS_5_5],
    [3,  dmm.MixedRangeAndFunctions.DC_10V,               dmm.ResolutionInDigits.DIGITS_5_5],
    [16, dmm.MixedRangeAndFunctions.DC_100mA,             dmm.ResolutionInDigits.DIGITS_5_5],
    [17, dmm.MixedRangeAndFunctions.DC_10mA,              dmm.ResolutionInDigits.DIGITS_5_5],
    [18, dmm.MixedRangeAndFunctions.DC_100mA,             dmm.ResolutionInDigits.DIGITS_5_5]
]

scan_configuration2 = [
    [1,  dmm.MixedRangeAndFunctions.DC_10V,               dmm.ResolutionInDigits.DIGITS_5_5],
    [2,  dmm.MixedRangeAndFunctions.DC_1V,                dmm.ResolutionInDigits.DIGITS_5_5],
    [3,  dmm.MixedRangeAndFunctions.DC_10V,               dmm.ResolutionInDigits.DIGITS_5_5],
    [16, dmm.MixedRangeAndFunctions.DC_100mA,             dmm.ResolutionInDigits.DIGITS_5_5],
    [17, dmm.MixedRangeAndFunctions.DC_10mA,              dmm.ResolutionInDigits.DIGITS_5_5],
    [18, dmm.MixedRangeAndFunctions.DC_100mA,             dmm.ResolutionInDigits.DIGITS_5_5]
]


#Declare constants for initialization
mux_resource_name = "Sim_MUX"
shunt_resource_name = "Sim_SHUNT"
dmm_resource_name = "Sim_DMM"

mux_topology_name = "2527/2-Wire Dual 16x1 Mux"
shunt_topology_name = "2568/31-SPST"

powerline_freq = 50
close_all_shunts = True
verbose = True # Set to False to not print measurements to console

############ EXECUTE SCANS ####################################################################

# Create scan object
scan = dmm_scan.DmmScanPMPS()

# Initialize scan object
resources = scan.initialize(
    mux_resource_name,
    mux_topology_name,
    shunt_resource_name,
    shunt_topology_name,
    dmm_resource_name,
    powerline_freq,
    close_all_shunts
)

# Execute first scan
print('\n\n\n')
print('############################ SCAN 1 ##################################################')

results = scan.configure_and_measure(resources, scan_configuration1, verbose)

# Execute second scan
print('\n\n\n')
print('############################ SCAN 2 ##################################################')

results = scan.configure_and_measure(resources, scan_configuration2, verbose)

# Disconnect and close resources
scan.close(resources)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_AO_DRCM.py sha256=139d7fd8f2d9bfb5dc67c9775c27a0eee6f003ec05bf3d10a6ed6b47824d20ed bytes=4536 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_AO_DRCM.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_AO_DRCM.py`
- sha256: `139d7fd8f2d9bfb5dc67c9775c27a0eee6f003ec05bf3d10a6ed6b47824d20ed`
- bytes: 4536

````python
### Ensure correct hardware and corresponding trigger names before running this example  

import matplotlib.pyplot as plt
import nidaqmx.constants
import numpy as np  

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Global variables
plot_results = True
save_fig = False
use_specific_channel = False

# Initialize
drvg = daq.DcVoltageGeneration()
drvg.initialize("Dev1/ao2:3")
drcm = daq.DcRmsCurrentMeasurement()
drcm.initialize("Dev1/ai2:4", use_specific_channel)

# region DRVG configure and generate

voltage_generation_range_parameters = daq.VoltageGenerationChannelParameters(
    range_min_volts=-10, range_max_volts=10
)

output_voltages = [10.0, 10.0]

drvg_config = daq.DcVoltageGenerationConfiguration(
    voltage_generation_range_parameters=voltage_generation_range_parameters,
    output_voltages=output_voltages,
)

# endregion DRVG configure and generate

drvg.configure_and_generate(configuration=drvg_config)

# region drcm configure and measure

global_channel_parameters = daq.DcRmsCurrentMeasurementTerminalRangeParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
    range_min_amperes=-0.001,
    range_max_amperes=0.001,
    shunt_resistor_ohms=1000.0,
)

# region specific channels

channel_parameters1 = daq.DcRmsCurrentMeasurementTerminalRangeParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.DIFF,
    range_min_amperes=-0.002,
    range_max_amperes=0.002,
    shunt_resistor_ohms=5000.0,
)

channel1 = daq.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
    channel_name="Dev1/ai2", channel_parameters=channel_parameters1
)

channel_parameters2 = daq.DcRmsCurrentMeasurementTerminalRangeParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
    range_min_amperes=-0.002,
    range_max_amperes=0.002,
    shunt_resistor_ohms=5000.0,
)

channel2 = daq.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
    channel_name="Dev1/ai3", channel_parameters=channel_parameters2
)

channel_parameters3 = daq.DcRmsCurrentMeasurementTerminalRangeParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
    range_min_amperes=-0.001,
    range_max_amperes=0.001,
    shunt_resistor_ohms=10000.0,
)

channel3 = daq.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
    channel_name="Dev1/ai4", channel_parameters=channel_parameters3
)

specific_channels_parameters = []
if use_specific_channel is True:
    specific_channels_parameters.append(channel1)
    specific_channels_parameters.append(channel2)
    specific_channels_parameters.append(channel3)

# endregion specific channels

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=10000,
    number_of_samples_per_channel=1000,
    sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
    digital_start_trigger_source="",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

drcm_config = daq.DcRmsCurrentMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_options=measurement_options,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion drcm configure and measure

drcm_result_data = drcm.configure_and_measure(drcm_config)

drcm.close()
drvg.close()

print(drcm_result_data)

# plot results

if plot_results is True:
    c1 = drcm_result_data.waveforms[0].samples.tolist()
    c2 = drcm_result_data.waveforms[1].samples.tolist()
    c3 = drcm_result_data.waveforms[2].samples.tolist()
    plt.plot(c1)
    plt.plot(c2)
    plt.plot(c3)
    plt.show()

# region save traces

save_traces(config=drcm_config, file_name="DRCM", result_data=drcm_result_data)


save_traces(
    config=drvg_config,
    file_name="DRVG",
)

# endregion save traces
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DCG_DECM_HW.py sha256=95b93ce6395b2e0681b6184f54438f3055385bb9ff9f0a8ab8fc85b3b8cda448 bytes=3166 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DCG_DECM_HW.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DCG_DECM_HW.py`
- sha256: `95b93ce6395b2e0681b6184f54438f3055385bb9ff9f0a8ab8fc85b3b8cda448`
- bytes: 3166

````python
# Digital Clock Generation to Digital Edge Count Measurement.
### Ensure correct hardware and corresponding trigger names before running this example

import nidaqmx.constants

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Initialize
dcg = daq.DigitalClockGeneration()
decm = daq.DigitalEdgeCountMeasurementUsingHardwareTimer()

dcg.initialize(counter_channel_expression="Dev1/ctr0", output_terminal_name="/Dev1/PFI2")

decm.initialize(
    measurement_channel_expression="Dev1/ctr2",
    measurement_input_terminal_name="/Dev1/PFI3",
    timer_channel_expression="Dev1/ctr3",
)

# begin decm configure
counter_channel_parameters = daq.DigitalEdgeCountMeasurementCounterChannelParameters(
    edge_type=nidaqmx.constants.Edge.FALLING
)
timing_parameters = daq.DigitalEdgeCountMeasurementTimingParameters(
    edge_counting_duration=1.0,
)
trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
    digital_start_trigger_source="/Dev1/PFI3",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

decm_configuration = daq.DigitalEdgeCountHardwareTimerConfiguration(
    measurement_options=measurement_options,
    counter_channel_parameters=counter_channel_parameters,
    timing_parameters=timing_parameters,
    trigger_parameters=trigger_parameters,
)
decm.configure_and_measure(configuration=decm_configuration)
# end region decm configure

# begin dcg configure and generate
channel_parameters = daq.DigitalClockGenerationCounterChannelParameters(
    frequency_hertz=1000.0,
    duty_cycle_ratio=0.5,
)
clock_timing_parameters = daq.DigitalClockGenerationTimingParameters(
    clock_duration_seconds=1.0,
)
dcg_configuration = daq.DigitalClockGenerationConfiguration(
    counter_channel_parameters=channel_parameters,
    timing_parameters=clock_timing_parameters,
)
# end region dcg configure and generate
dcg_results = dcg.configure_and_generate(configuration=dcg_configuration)

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

decm_configuration = daq.DigitalEdgeCountHardwareTimerConfiguration(
    measurement_options=measurement_options,
    counter_channel_parameters=counter_channel_parameters,
    timing_parameters=timing_parameters,
    trigger_parameters=trigger_parameters,
)
decm_results = decm.configure_and_measure(configuration=decm_configuration)

# close generation and measurement session
dcg.close()
decm.close()

print(dcg_results)
print(decm_results)

save_traces(config=decm_configuration, file_name="DECM", result_data=decm_results)

save_traces(config=dcg_configuration, file_name="DCG", result_data=dcg_results)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DCG_DECM_HW_2DAQ_RSS.py sha256=6f5c42e17fffdf942afc24a87e4c2925a8da6a95437c610a85b8b7fdfef7664e bytes=3164 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DCG_DECM_HW_2DAQ_RSS.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DCG_DECM_HW_2DAQ_RSS.py`
- sha256: `6f5c42e17fffdf942afc24a87e4c2925a8da6a95437c610a85b8b7fdfef7664e`
- bytes: 3164

````python
# Digital Clock Generation to Digital Edge Count Measurement.
### Ensure correct hardware and corresponding trigger names before running this example

import nidaqmx.constants

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Initialize
dcg = daq.DigitalClockGeneration()
decm = daq.DigitalEdgeCountMeasurementUsingHardwareTimer()

dcg.initialize(counter_channel_expression="Dev1/ctr0", output_terminal_name="/Dev1/PFI0")

decm.initialize(
    measurement_channel_expression="Dev2/ctr0",
    measurement_input_terminal_name="/Dev2/PFI0",
    timer_channel_expression="Dev2/ctr1",
)

# begin decm configure
counter_channel_parameters = daq.DigitalEdgeCountMeasurementCounterChannelParameters(
    edge_type=nidaqmx.constants.Edge.FALLING
)
timing_parameters = daq.DigitalEdgeCountMeasurementTimingParameters(
    edge_counting_duration=1.0,
)
trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
    digital_start_trigger_source="/Dev2/PFI0",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

decm_configuration = daq.DigitalEdgeCountHardwareTimerConfiguration(
    measurement_options=measurement_options,
    counter_channel_parameters=counter_channel_parameters,
    timing_parameters=timing_parameters,
    trigger_parameters=trigger_parameters,
)
decm.configure_and_measure(configuration=decm_configuration)
# end region decm configure

# begin dcg configure and generate
channel_parameters = daq.DigitalClockGenerationCounterChannelParameters(
    frequency_hertz=1000.0,
    duty_cycle_ratio=0.5,
)
clock_timing_parameters = daq.DigitalClockGenerationTimingParameters(
    clock_duration_seconds=1.0,
)
dcg_configuration = daq.DigitalClockGenerationConfiguration(
    counter_channel_parameters=channel_parameters,
    timing_parameters=clock_timing_parameters,
)
# end region dcg configure and generate
dcg_results = dcg.configure_and_generate(configuration=dcg_configuration)

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)
decm_configuration = daq.DigitalEdgeCountHardwareTimerConfiguration(
    measurement_options=measurement_options,
    counter_channel_parameters=counter_channel_parameters,
    timing_parameters=timing_parameters,
    trigger_parameters=trigger_parameters,
)
decm_results = decm.configure_and_measure(configuration=decm_configuration)

# close generation and measurement session
dcg.close()
decm.close()

print(dcg_results)
print(decm_results)

save_traces(config=decm_configuration, file_name="DECM", result_data=decm_results)

save_traces(config=dcg_configuration, file_name="DCG", result_data=dcg_results)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DCG_DFM.py sha256=56ba0fb229005627530ae56f4f2c5cb2ad219a751bbb460b0539c26f04a13980 bytes=2091 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DCG_DFM.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DCG_DFM.py`
- sha256: `56ba0fb229005627530ae56f4f2c5cb2ad219a751bbb460b0539c26f04a13980`
- bytes: 2091

````python
# Digital Clock Generation to Digital Frequency Measurement 
### Ensure correct hardware and corresponding trigger names before running this example

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Initialize
dcg = daq.DigitalClockGeneration()
dfm = daq.DigitalFrequencyMeasurement()

dcg.initialize(
    counter_channel_expression="Dev1/ctr0",
    output_terminal_name="/Dev1/PFI2",
)

dfm.initialize(
    channel_expression="Dev1/ctr2",
    input_terminal_name="/Dev1/PFI3",
)
# begin dcg configure

channel_parameters = daq.DigitalClockGenerationCounterChannelParameters(
    frequency_hertz=10000.0,
    duty_cycle_ratio=0.5,
)
clock_timing_parameters = daq.DigitalClockGenerationTimingParameters(
    clock_duration_seconds=0.1,
)
dcg_configuration = daq.DigitalClockGenerationConfiguration(
    counter_channel_parameters=channel_parameters,
    timing_parameters=clock_timing_parameters,
)
# end region dcg configure

# begin dfm configure

range_parameters = daq.DigitalFrequencyRangeParameters(
    frequency_maximum_value_hertz=20000000.0,
    frequency_minimum_value_hertz=1.0,
)

counter_channel_parameter = daq.DigitalFrequencyMeasurementCounterChannelParameters(
    range_parameters=range_parameters,
    input_divisor_for_frequency_measurement=4,
    measurement_duration_seconds=0.10,
)

dfm_configuration = daq.DigitalFrequencyMeasurementConfiguration(
    counter_channel_configuration_parameters=counter_channel_parameter,
)
# end dfm configure

# begin generate and measure
dcg_results = dcg.configure_and_generate(configuration=dcg_configuration)
dfm_results = dfm.configure_and_measure(configuration=dfm_configuration)

# close generation and measurement session
dcg.close()
dfm.close()

print(dcg_results)
print()
print("detected_frequency(Hz):", dfm_results.frequency)
print()

save_traces(config=dfm_configuration, file_name="DFM", result_data=dfm_results)

save_traces(config=dcg_configuration, file_name="DCG", result_data=dcg_results)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DCG_DPWMM.py sha256=1708c2c54341bea85191f2a5eb864320f2f1a7c201522d51806c75a2b6bfd063 bytes=2528 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DCG_DPWMM.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DCG_DPWMM.py`
- sha256: `1708c2c54341bea85191f2a5eb864320f2f1a7c201522d51806c75a2b6bfd063`
- bytes: 2528

````python
# Digital Clock Generation to Digital Pulse Width Measurement 
### Ensure correct hardware and corresponding trigger names before running this example

import nidaqmx.constants

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Initialize

dcg = daq.DigitalClockGeneration()
dpwmm = daq.DigitalPwmMeasurement()

dcg.initialize(
    counter_channel_expression="Dev1/ctr0",
    output_terminal_name="/Dev1/PFI2",
)

dpwmm.initialize(
    channel_expression="Dev1/ctr2",
    input_terminal_name="/Dev1/PFI3",
)

# begin dpwmm configure

range_parameters = daq.DigitalPwmMeasurementRangeParameters(
    semi_period_maximum_value_seconds=42.949,
    semi_period_minimum_value_seconds=20e-9,
)

timing_parameters = daq.DigitalPwmMeasurementTimingParameters(
    semi_period_counter_wanted_cycles_count=2,
)

counter_channel_parameters = daq.DigitalPwmMeasurementCounterChannelParameters(
    timing_parameters=timing_parameters,
    range_parameters=range_parameters,
    semi_period_counter_starting_edge=nidaqmx.constants.Edge.RISING,
)


dpwmm_configuration = daq.DigitalPwmMeasurementConfiguration(
    parameters=counter_channel_parameters,
    measurement_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
)

dpwmm.configure_and_measure(configuration=dpwmm_configuration)
# end region dpwmm configure

# begin dcg configure and generate
channel_parameters = daq.DigitalClockGenerationCounterChannelParameters(
    frequency_hertz=10000.0,
    duty_cycle_ratio=0.5,
)
clock_timing_parameters = daq.DigitalClockGenerationTimingParameters(
    clock_duration_seconds=0.10,
)
dcg_configuration = daq.DigitalClockGenerationConfiguration(
    counter_channel_parameters=channel_parameters,
    timing_parameters=clock_timing_parameters,
)
# end region dcg configure and generate
dcg_results = dcg.configure_and_generate(configuration=dcg_configuration)

dpwmm_configuration = daq.DigitalPwmMeasurementConfiguration(
    parameters=counter_channel_parameters,
    measurement_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
)
dpwmm_results = dpwmm.configure_and_measure(configuration=dpwmm_configuration)

# close generation and measurement session
dcg.close()
dpwmm.close()

print(dcg_results)
print(dpwmm_results)

save_traces(config=dpwmm_configuration, file_name="DPWMM", result_data=dpwmm_results)

save_traces(config=dcg_configuration, file_name="DCG", result_data=dcg_results)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DCG_to_DPWMM_2DAQ_RSS.py sha256=62cc8805961c938c1cddf108c2c5f8a339f41a1337861bc4607b023df84b3c64 bytes=2530 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DCG_to_DPWMM_2DAQ_RSS.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DCG_to_DPWMM_2DAQ_RSS.py`
- sha256: `62cc8805961c938c1cddf108c2c5f8a339f41a1337861bc4607b023df84b3c64`
- bytes: 2530

````python
# Digital Clock Generation to Digital Pulse Width Measurement  
### Ensure correct hardware and corresponding trigger names before running this example

import nidaqmx.constants

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Initialize
dcg = daq.DigitalClockGeneration()
dpwmm = daq.DigitalPwmMeasurement()

dcg.initialize(
    counter_channel_expression="Dev1/ctr0",
    output_terminal_name="/Dev1/PFI2",
)

dpwmm.initialize(
    channel_expression="Dev1/ctr2",
    input_terminal_name="/Dev1/PFI3",
)

# begin dpwmm configure

range_parameters = daq.DigitalPwmMeasurementRangeParameters(
    semi_period_maximum_value_seconds=42.949672,
    semi_period_minimum_value_seconds=20e-9,
)

timing_parameters = daq.DigitalPwmMeasurementTimingParameters(
    semi_period_counter_wanted_cycles_count=2,
)

counter_channel_parameters = daq.DigitalPwmMeasurementCounterChannelParameters(
    timing_parameters=timing_parameters,
    range_parameters=range_parameters,
    semi_period_counter_starting_edge=nidaqmx.constants.Edge.RISING,
)


dpwmm_configuration = daq.DigitalPwmMeasurementConfiguration(
    parameters=counter_channel_parameters,
    measurement_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
)

dpwmm.configure_and_measure(configuration=dpwmm_configuration)
# end region dpwmm configure

# begin dcg configure and generate
channel_parameters = daq.DigitalClockGenerationCounterChannelParameters(
    frequency_hertz=10000.0,
    duty_cycle_ratio=0.5,
)
clock_timing_parameters = daq.DigitalClockGenerationTimingParameters(
    clock_duration_seconds=0.10,
)
dcg_configuration = daq.DigitalClockGenerationConfiguration(
    counter_channel_parameters=channel_parameters,
    timing_parameters=clock_timing_parameters,
)
# end region dcg configure and generate
dcg_results = dcg.configure_and_generate(configuration=dcg_configuration)

dpwmm_configuration = daq.DigitalPwmMeasurementConfiguration(
    parameters=counter_channel_parameters,
    measurement_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
)
dpwmm_results = dpwmm.configure_and_measure(configuration=dpwmm_configuration)

# close generation and measurement session
dcg.close()
dpwmm.close()

print(dcg_results)
print(dpwmm_results)

save_traces(config=dpwmm_configuration, file_name="DPWMM", result_data=dpwmm_results)

save_traces(config=dcg_configuration, file_name="DCG", result_data=dcg_results)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DDPG_DDPM_1DAQ_LOOP_RSS.py sha256=d48d091bf6a7c1ff13ed85d663307654abe8ccd825e85799b02bc332a91decc3 bytes=4038 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DDPG_DDPM_1DAQ_LOOP_RSS.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DDPG_DDPM_1DAQ_LOOP_RSS.py`
- sha256: `d48d091bf6a7c1ff13ed85d663307654abe8ccd825e85799b02bc332a91decc3`
- bytes: 4038

````python
### Ensure correct hardware and corresponding trigger names before running this example 

import nidaqmx.constants
import numpy as np

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# DDPG_Initialization
ddpg = daq.DynamicDigitalPatternGeneration()
ddpg.initialize(channel_expression="/Dev1/port0/line16:17")

# RouteSyncSignal
ddpg.route_start_trigger_signal_to_terminal(terminal_name="/Dev1/PFI0")
ddpg.route_sample_clock_signal_to_terminal(terminal_name="/Dev1/PFI1")

# DDPM_Initialization
ddpm = daq.DynamicDigitalPatternMeasurement()
ddpm.initialize(
    channel_expression="/Dev1/port0/line18:19",
)

# begin ddpm configure

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS,
)

timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
    sample_clock_source="/Dev1/PFI1",
    sampling_rate_hertz=10000.0,
    number_of_samples_per_channel=5,
    active_edge=nidaqmx.constants.Edge.FALLING,
)
trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
    digital_start_trigger_source="/Dev1/PFI0",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

ddpm_configuration = daq.DynamicDigitalPatternMeasurementConfiguration(
    measurement_options=measurement_options,
    timing_parameters=timing_parameters,
    trigger_parameters=trigger_parameters,
)

ddpm.configure_and_measure(configuration=ddpm_configuration)

# end region ddpm configure

# begin region ddpg configuration

timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=10000.0,
    number_of_samples_per_channel=5,
    active_edge=nidaqmx.constants.Edge.FALLING,
)

trigger_parameters = daq.DynamicDigitalStartTriggerParameters(
    digital_start_trigger_source="/Dev1/PFI6",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    trigger_type=nipcbatt.StartTriggerType.NO_TRIGGER,
)

# data to generate

digital_lis = [[262144, 615000, 713140, 616421, 679353, 0]]

pulse_signal = np.array(digital_lis, dtype=np.uint32)

ddpg_configuration = daq.DynamicDigitalPatternGenerationConfiguration(
    timing_parameters=timing_parameters,
    digital_start_trigger_parameters=trigger_parameters,
    pulse_signal=pulse_signal,
)
# end region ddpg configuration

ddpg_results = ddpg.configure_and_generate(configuration=ddpg_configuration)

# close generation session


# begin ddpm measurement

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
    sample_clock_source="/Dev1/PFI1",
    sampling_rate_hertz=10000.0,
    number_of_samples_per_channel=5,
    active_edge=nidaqmx.constants.Edge.FALLING,
)
trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
    digital_start_trigger_source="/Dev1/PFI0",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

ddpm_configuration = daq.DynamicDigitalPatternMeasurementConfiguration(
    measurement_options=measurement_options,
    timing_parameters=timing_parameters,
    trigger_parameters=trigger_parameters,
)
# end region ddpm measurement

ddpm_results = ddpm.configure_and_measure(configuration=ddpm_configuration)

ddpm.close()
ddpg.close()

print(ddpg_results.generation_time_seconds)

print(ddpm_results)

save_traces(config=ddpg_configuration, file_name="DDPG", result_data=ddpg_results)


save_traces(config=ddpm_configuration, file_name="DDPM", result_data=ddpm_results)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DDPG_DDPM_2DAQ_RSS.py sha256=e1016152a5835bdd9a22c5a17fcfbcc9c0bf2921dd9ea1c11ab4772d9b67e724 bytes=4070 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DDPG_DDPM_2DAQ_RSS.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DDPG_DDPM_2DAQ_RSS.py`
- sha256: `e1016152a5835bdd9a22c5a17fcfbcc9c0bf2921dd9ea1c11ab4772d9b67e724`
- bytes: 4070

````python
### Ensure correct hardware and corresponding trigger names before running this example 

import nidaqmx.constants
import numpy as np

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# DDPG_Initialization
ddpg = daq.DynamicDigitalPatternGeneration()
ddpg.initialize(channel_expression="Dev1/port0/line0:15")

# RouteSyncSignal
ddpg.route_start_trigger_signal_to_terminal(terminal_name="/Dev1/PFI0")
ddpg.route_sample_clock_signal_to_terminal(terminal_name="/Dev1/PFI1")

# DDPM_Initialization
ddpm = daq.DynamicDigitalPatternMeasurement()
ddpm.initialize(
    channel_expression="Dev2/port0/line0:15",
)

# begin ddpm configure

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS,
)

timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
    sample_clock_source="/Dev2/PFI1",
    sampling_rate_hertz=10000.0,
    number_of_samples_per_channel=65536,
    active_edge=nidaqmx.constants.Edge.FALLING,
)
trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
    digital_start_trigger_source="/Dev2/PFI0",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

ddpm_configuration = daq.DynamicDigitalPatternMeasurementConfiguration(
    measurement_options=measurement_options,
    timing_parameters=timing_parameters,
    trigger_parameters=trigger_parameters,
)

ddpm.configure_and_measure(configuration=ddpm_configuration)

# end region ddpm configure


# begin region ddpg configuration
timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=10000.0,
    number_of_samples_per_channel=65536,
    active_edge=nidaqmx.constants.Edge.FALLING,
)

trigger_parameters = daq.DynamicDigitalStartTriggerParameters(
    digital_start_trigger_source="/Dev1/PFI6",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    trigger_type=nipcbatt.StartTriggerType.NO_TRIGGER,
)

# data to generate

values_list = list(range(65536))
digital_lis = []
digital_lis.append(values_list)

pulse_signal = np.array(digital_lis, dtype=np.uint32)

ddpg_configuration = daq.DynamicDigitalPatternGenerationConfiguration(
    timing_parameters=timing_parameters,
    digital_start_trigger_parameters=trigger_parameters,
    pulse_signal=pulse_signal,
)
# end region ddpg configuration

ddpg_results = ddpg.configure_and_generate(configuration=ddpg_configuration)

# close generation session


# begin ddpm measurement

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
    sample_clock_source="/Dev2/PFI1",
    sampling_rate_hertz=10000.0,
    number_of_samples_per_channel=65536,
    active_edge=nidaqmx.constants.Edge.FALLING,
)
trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
    digital_start_trigger_source="/Dev2/PFI0",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

ddpm_configuration = daq.DynamicDigitalPatternMeasurementConfiguration(
    measurement_options=measurement_options,
    timing_parameters=timing_parameters,
    trigger_parameters=trigger_parameters,
)
# end region ddpm measurement

ddpm_results = ddpm.configure_and_measure(configuration=ddpm_configuration)

ddpm.close()
ddpg.close()

print(ddpg_results.generation_time_seconds)

print(ddpm_results)

save_traces(config=ddpg_configuration, file_name="DDPG", result_data=ddpg_results)


save_traces(config=ddpm_configuration, file_name="DDPM", result_data=ddpm_results)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DPG_DECM.py sha256=3052ccea17618936bb934d1de18ab8a19ed9b441902b908c3862049ef584278f bytes=3208 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DPG_DECM.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DPG_DECM.py`
- sha256: `3052ccea17618936bb934d1de18ab8a19ed9b441902b908c3862049ef584278f`
- bytes: 3208

````python
# Digital Pulse Generation to Digital Edge Count Measurement  
### Ensure correct hardware and corresponding trigger names before running this example

import nidaqmx.constants

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Initialize

dpg = daq.DigitalPulseGeneration()
decm = daq.DigitalEdgeCountMeasurementUsingHardwareTimer()

dpg.initialize(channel_expression="Dev1/ctr0", output_terminal_name="/Dev1/PFI2")

decm.initialize(
    measurement_channel_expression="Dev1/ctr1",
    measurement_input_terminal_name="/Dev1/PFI3",
    timer_channel_expression="Dev1/ctr2",
)

# begin decm configure
counter_channel_parameters = daq.DigitalEdgeCountMeasurementCounterChannelParameters(
    edge_type=nidaqmx.constants.Edge.FALLING
)
timing_parameters = daq.DigitalEdgeCountMeasurementTimingParameters(
    edge_counting_duration=5e-3,
)
trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
    digital_start_trigger_source="/Dev1/PFI3",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

decm_configuration = daq.DigitalEdgeCountHardwareTimerConfiguration(
    measurement_options=measurement_options,
    counter_channel_parameters=counter_channel_parameters,
    timing_parameters=timing_parameters,
    trigger_parameters=trigger_parameters,
)
decm.configure_and_measure(configuration=decm_configuration)
# end region decm configure

# begin dpg configure and generate
channel_parameters = daq.DigitalPulseGenerationCounterChannelParameters(
    pulse_idle_state=nidaqmx.constants.Level.LOW,
    low_time_seconds=500e-6,
    high_time_seconds=500e-6,
)
pulses_timing_parameters = daq.DigitalPulseGenerationTimingParameters(
    pulses_count=5,
)
dpg_configuration = daq.DigitalPulseGenerationConfiguration(
    counter_channel_parameters=channel_parameters,
    timing_parameters=pulses_timing_parameters,
)
# end region dpg configure and generate
dpg_results = dpg.configure_and_generate(configuration=dpg_configuration)

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

decm_configuration = daq.DigitalEdgeCountHardwareTimerConfiguration(
    measurement_options=measurement_options,
    counter_channel_parameters=counter_channel_parameters,
    timing_parameters=timing_parameters,
    trigger_parameters=trigger_parameters,
)
decm_results = decm.configure_and_measure(configuration=decm_configuration)

# close generation and measurement session
dpg.close()
decm.close()

print(dpg_results)
print(decm_results)

save_traces(config=decm_configuration, file_name="DECM", result_data=decm_results)

save_traces(config=dpg_configuration, file_name="DPG", result_data=dpg_results)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DPG_DPWMM.py sha256=e8739cdf2ff6781fe8de4039357b94ae85127ec0f01453ba379790d3ca09bca9 bytes=2583 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DPG_DPWMM.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DPG_DPWMM.py`
- sha256: `e8739cdf2ff6781fe8de4039357b94ae85127ec0f01453ba379790d3ca09bca9`
- bytes: 2583

````python
### Ensure correct hardware and corresponding trigger names before running this example 

import nidaqmx.constants

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.save_traces import save_traces

number_of_cycles = 101

# initialize
dpg = daq.DigitalPulseGeneration()
dpwmm = daq.DigitalPwmMeasurement()

# Terminals to be verified
dpg.initialize(channel_expression="Dev1/ctr0", output_terminal_name="/Dev1/PFI2")

dpwmm.initialize(
    channel_expression="Dev1/ctr2",
    input_terminal_name="/Dev1/PFI3",
)

# DPWMM configuration begins

range_parameters = daq.DigitalPwmMeasurementRangeParameters(
    semi_period_maximum_value_seconds=42.949672,
    semi_period_minimum_value_seconds=20e-9,
)

timing_parameters = daq.DigitalPwmMeasurementTimingParameters(
    semi_period_counter_wanted_cycles_count=number_of_cycles,
)

counter_channel_parameters = daq.DigitalPwmMeasurementCounterChannelParameters(
    timing_parameters=timing_parameters,
    range_parameters=range_parameters,
    semi_period_counter_starting_edge=nidaqmx.constants.Edge.RISING,
)

dpwmm_configuration = daq.DigitalPwmMeasurementConfiguration(
    parameters=counter_channel_parameters,
    measurement_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
)

dpwmm.configure_and_measure(configuration=dpwmm_configuration)
# end region dpwmm configure


# begin dpg configure and generate
channel_parameters = daq.DigitalPulseGenerationCounterChannelParameters(
    pulse_idle_state=nidaqmx.constants.Level.LOW,
    low_time_seconds=0.00005,
    high_time_seconds=0.00015,
)
pulse_timing_parameters = daq.DigitalPulseGenerationTimingParameters(
    pulses_count=number_of_cycles,
)
dpg_configuration = daq.DigitalPulseGenerationConfiguration(
    counter_channel_parameters=channel_parameters,
    timing_parameters=pulse_timing_parameters,
)
# end region dpg configure and generate
dpg_results = dpg.configure_and_generate(configuration=dpg_configuration)


dpwmm_configuration = daq.DigitalPwmMeasurementConfiguration(
    parameters=counter_channel_parameters,
    measurement_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
)

dpwmm_results = dpwmm.configure_and_measure(configuration=dpwmm_configuration)

# close generation and measurement session
dpg.close()
dpwmm.close()


print(dpg_results)
print(dpwmm_results)

save_traces(config=dpwmm_configuration, file_name="DPWMM", result_data=dpwmm_results)

save_traces(config=dpg_configuration, file_name="DPG", result_data=dpg_results)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DRVG_DRVM.py sha256=8b15d4b90578f7b389a493d5ff26a11ea066bb0abd9df1e74c89b28e191f6f9e bytes=3450 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DRVG_DRVM.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_DRVG_DRVM.py`
- sha256: `8b15d4b90578f7b389a493d5ff26a11ea066bb0abd9df1e74c89b28e191f6f9e`
- bytes: 3450

````python
# DC Voltage Generation connected to DC-RMS Voltage Measurement (single ch.)  
### Ensure correct hardware and corresponding trigger names before running this example

import nidaqmx.constants

import nipcbatt
from nipcbatt import daq
import nipcbatt.pcbatt_utilities.plotter as pl
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Global variable to plot
plot_results = True
save_fig = False

drvg = daq.DcVoltageGeneration()
drvg.initialize(analog_output_channel_expression="Dev1/ao0")

drvm = daq.DcRmsVoltageMeasurement()
drvm.initialize(analog_input_channel_expression="Dev1/ai0")

# region drvg configure and generate

range_settings = daq.VoltageGenerationChannelParameters(
    range_min_volts=-10.0, range_max_volts=10.0
)

output_voltages = [1.00]

drvg_config = daq.DcVoltageGenerationConfiguration(
    voltage_generation_range_parameters=range_settings, output_voltages=output_voltages
)

# endregion drvg configure and generate

drvg.configure_and_generate(drvg_config)

# region DC-RMS VM Configure and Measure

global_channel_parameters = daq.VoltageRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
    range_min_volts=-10,
    range_max_volts=10,
)

specific_channels_parameters = []

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=10000,
    number_of_samples_per_channel=1000,
    sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
    digital_start_trigger_source="",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

drvm_config = daq.DcRmsVoltageMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_options=measurement_options,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion DC-RMS VM Configure and Measure

drvm_result_data = drvm.configure_and_measure(configuration=drvm_config)

# Close drvm Measurement Task
drvm.close()

# Set DC Voltage to 0
output_voltages = [0.0]

drvg_config1 = daq.DcVoltageGenerationConfiguration(
    voltage_generation_range_parameters=range_settings, output_voltages=output_voltages
)

drvg.configure_and_generate(drvg_config1)

# Close drvg Measurement Task
drvg.close()

# DcRmsVoltageMeasurementResultData
print("drvm result :\n")
print(drvm_result_data)

# region save traces

save_traces(config=drvm_config, file_name="DRVM", result_data=drvm_result_data)

save_traces(config=drvg_config, file_name="DRVG")

# endregion save traces

# region plot results

if plot_results is True:
    drvm_w = drvm_result_data.waveforms[0].samples.tolist()
    pl.graph_plot(
        y=drvm_w,
        title="DRVM Voltage",
        ylabel="Voltage (V)",
        xlabel="Samples",
        save_fig=save_fig,
    )
# # endregion plot results
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_SDSG_SDSM.py sha256=cd6ae6209f6bab601543266dd678a77c4c4db5639f979932cce274d5dc947423 bytes=1357 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_SDSG_SDSM.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_SDSG_SDSM.py`
- sha256: `cd6ae6209f6bab601543266dd678a77c4c4db5639f979932cce274d5dc947423`
- bytes: 1357

````python
"""Static Digital State Generation and Measurement"""  

### Ensure correct hardware and corresponding trigger names before running this example

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Initialize
sdsg = daq.StaticDigitalStateGeneration()
sdsg.initialize(channel_expression="Dev1/port0/line0:3")

# region SDSG configure and generate

sdsg_config = daq.StaticDigitalStateGenerationConfiguration(
    data_to_write=[False, True, False, True]
)

# endregion SDSG configure and generate

sdsg_result_data = sdsg.configure_and_generate(configuration=sdsg_config)

# region SDSM configure and measure

sdsm = daq.StaticDigitalStateMeasurement()
sdsm.initialize(channel_expression="Dev2/port0/line0:3")

# end region SDSM configure and measure

sdsm_result_data = sdsm.configure_and_measure()

sdsm.close()
sdsg.close()


print(sdsg_result_data)
print(sdsm_result_data.states_per_channels)

print("data_to_write-", sdsg_config.data_to_write)
print()
print("sdsm_result-", sdsm_result_data.digital_states)
print()
print("sdsm_channel_identifiers-", sdsm_result_data.channel_identifiers)
print()

save_traces(config=sdsg_config, file_name="SDSG", result_data=sdsg_result_data)

save_traces(config=None, file_name="SDSM", result_data=sdsm_result_data)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_SVG_DRVM.py sha256=6dd662f19cb77ebdafbedb29aabc15fadac30580b90c623328759311f674623f bytes=6424 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_SVG_DRVM.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_SVG_DRVM.py`
- sha256: `6dd662f19cb77ebdafbedb29aabc15fadac30580b90c623328759311f674623f`
- bytes: 6424

````python
# Signal Voltage Generation connected to Time Domain Measurement 
### Ensure correct hardware and corresponding trigger names before running this example

from enum import Enum

import nidaqmx.constants

import nipcbatt
from nipcbatt import daq
import nipcbatt.pcbatt_utilities.plotter as pl
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Global variable to plot
plot_results = True
save_fig = False

# Enums to select generation and Waveform types


class Generation_type( 
    Enum
):
    Single_tone = 0
    Multi_tone = 1


class Waveform_type( 
    Enum
):
    Sine_wave = 0
    Square_wave = 1


# INPUTS

# Configure Generation and Waveform types
generation_type = Generation_type.Single_tone
waveform_type = Waveform_type.Square_wave

# Multiple tones settings
multiple_tones_parameters = []
multiple_tones_parameters.append(
    daq.ToneParameters(
        tone_frequency_hertz=100, tone_amplitude_volts=1.0, tone_phase_radians=0
    )
)
multiple_tones_parameters.append(
    daq.ToneParameters(
        tone_frequency_hertz=200, tone_amplitude_volts=1.0, tone_phase_radians=0
    )
)

# Initialize
svg = daq.SignalVoltageGeneration()
svg.initialize(channel_expression="Dev1/ao1")

drvm = daq.DcRmsVoltageMeasurement()
drvm.initialize("Dev1/ai1")

# region configure SVG
voltage_generation_range_parameters = daq.VoltageGenerationChannelParameters(
    range_min_volts=-10, range_max_volts=10
)

timing_parameters = daq.SignalVoltageGenerationTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=100000,
    generated_signal_duration_seconds=0.2,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
    digital_start_trigger_source="",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

if generation_type == Generation_type.Single_tone:
    if waveform_type == Waveform_type.Sine_wave:
        # region SVG SineWave configure and generate

        generated_signal_tone_parameters = daq.ToneParameters(
            tone_frequency_hertz=500, tone_amplitude_volts=1, tone_phase_radians=0
        )

        waveform_parameters = daq.SignalVoltageGenerationSineWaveParameters(
            generated_signal_offset_volts=0,
            generated_signal_tone_parameters=generated_signal_tone_parameters,
        )

        svg_config = daq.SignalVoltageGenerationSineWaveConfiguration(
            voltage_generation_range_parameters=voltage_generation_range_parameters,
            waveform_parameters=waveform_parameters,
            timing_parameters=timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        # endregion
        svg.configure_and_generate_sine_waveform(svg_config)

    else:
        # region SVG SquareWave configure and generate

        waveform_parameters = daq.SignalVoltageGenerationSquareWaveParameters(
            generated_signal_amplitude_volts=1.0,
            generated_signal_duty_cycle_percent=50.00,
            generated_signal_frequency_hertz=100,
            generated_signal_phase_radians=0,
            generated_signal_offset_volts=0,
        )

        svg_config = daq.SignalVoltageGenerationSquareWaveConfiguration(
            voltage_generation_range_parameters=voltage_generation_range_parameters,
            waveform_parameters=waveform_parameters,
            timing_parameters=timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )
        # endregion
        svg.configure_and_generate_square_waveform(svg_config)

else:
    # region SVG MultiTone configure and generate

    waveform_parameters = daq.SignalVoltageGenerationMultipleTonesWaveParameters(
        generated_signal_amplitude_volts=1.0,
        generated_signal_offset_volts=0,
        multiple_tones_parameters=multiple_tones_parameters,
    )

    svg_config = daq.SignalVoltageGenerationMultipleTonesConfiguration(
        voltage_generation_range_parameters=voltage_generation_range_parameters,
        waveform_parameters=waveform_parameters,
        timing_parameters=timing_parameters,
        digital_start_trigger_parameters=digital_start_trigger_parameters,
    )
    # endregion
    svg.configure_and_generate_multiple_tones_waveform(svg_config)

# region DRVM configure and measure

global_channel_parameters = daq.VoltageRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.DIFF,
    range_min_volts=-10,
    range_max_volts=10,
)

specific_channels_parameters = []

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=10000,
    number_of_samples_per_channel=1000,
    sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
    digital_start_trigger_source="",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

drvm_config = daq.DcRmsVoltageMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_options=measurement_options,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion

drvm_result_data = drvm.configure_and_measure(drvm_config)

drvm.close()
svg.close()

print("DRVM result :\n")
print(drvm_result_data)

# region save traces

save_traces(config=drvm_config, file_name="DRVM", result_data=drvm_result_data)

save_traces(config=svg_config, file_name="SVG")

if plot_results is True:
    drvm_w = drvm_result_data.waveforms[0].samples.tolist()
    pl.graph_plot(
        y=drvm_w,
        title="DRVM Voltage",
        ylabel="Voltage (V)",
        xlabel="Samples",
        save_fig=save_fig,
    )

# #endregion
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_SVG_FDVM.py sha256=d473dc31a7e2f0f0fe71895c7727221366740db8e8c35217a589fb5b639e3767 bytes=8612 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_SVG_FDVM.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_SVG_FDVM.py`
- sha256: `d473dc31a7e2f0f0fe71895c7727221366740db8e8c35217a589fb5b639e3767`
- bytes: 8612

````python
# Signal Voltage Generation connected to Frequency Domain Measurement  
### Ensure correct hardware and corresponding trigger names before running this example

from enum import Enum

import nidaqmx.constants
import numpy as np

import nipcbatt
from nipcbatt import daq
import nipcbatt.pcbatt_utilities.plotter as pl
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Global variable to plot
plot_results = True
save_fig = False

# Enums to select generation and Waveform types


class Generation_type(  
    Enum
):
    Single_tone = 0
    Multi_tone = 1


class Waveform_type( 
    Enum
):
    Sine_wave = 0
    Square_wave = 1


# INPUTS

# Configure Generation and Waveform types
generation_type = Generation_type.Single_tone
waveform_type = Waveform_type.Sine_wave

generation_time = 0.1  # change this according to the sampling rate

# Configure Multiple tones settings
multiple_tones_parameters = []
multiple_tones_parameters.append(
    daq.ToneParameters(
        tone_frequency_hertz=100, tone_amplitude_volts=1.0, tone_phase_radians=0
    )
)
multiple_tones_parameters.append(
    daq.ToneParameters(
        tone_frequency_hertz=200, tone_amplitude_volts=1.0, tone_phase_radians=0
    )
)

# Initialize
svg = daq.SignalVoltageGeneration()
svg.initialize(channel_expression="Dev1/ao1")

fdvm = daq.FrequencyDomainMeasurement()
fdvm.initialize(analog_input_channel_expression="Dev1/ai1")

# region fdvm configure only

global_channel_parameters = daq.VoltageRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
    range_min_volts=-10,
    range_max_volts=10,
)

sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=10000,
    number_of_samples_per_channel=1000,
    sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
)

specific_channels_parameters = []

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
    digital_start_trigger_source="/Dev1/ao/StartTrigger",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

fdvm_config = daq.FrequencyDomainMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_options=measurement_options,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion fdvm configure only
fdvm.configure_and_measure(configuration=fdvm_config)

# region configure SVG
voltage_generation_range_parameters = daq.VoltageGenerationChannelParameters(
    range_min_volts=-10, range_max_volts=10
)

timing_parameters = daq.SignalVoltageGenerationTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=100000,
    generated_signal_duration_seconds=generation_time,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
    digital_start_trigger_source="",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

if generation_type == Generation_type.Single_tone:
    if waveform_type == Waveform_type.Sine_wave:
        # region SVG SineWave configure and generate

        generated_signal_tone_parameters = daq.ToneParameters(
            tone_frequency_hertz=50, tone_amplitude_volts=0.5, tone_phase_radians=0
        )

        waveform_parameters = daq.SignalVoltageGenerationSineWaveParameters(
            generated_signal_offset_volts=0,
            generated_signal_tone_parameters=generated_signal_tone_parameters,
        )

        svg_config = daq.SignalVoltageGenerationSineWaveConfiguration(
            voltage_generation_range_parameters=voltage_generation_range_parameters,
            waveform_parameters=waveform_parameters,
            timing_parameters=timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        # endregion
        svg.configure_and_generate_sine_waveform(svg_config)

    else:
        # region SVG SquareWave configure and generate

        waveform_parameters = daq.SignalVoltageGenerationSquareWaveParameters(
            generated_signal_amplitude_volts=1.0,
            generated_signal_duty_cycle_percent=50.00,
            generated_signal_frequency_hertz=100,
            generated_signal_phase_radians=0,
            generated_signal_offset_volts=0,
        )

        svg_config = daq.SignalVoltageGenerationSquareWaveConfiguration(
            voltage_generation_range_parameters=voltage_generation_range_parameters,
            waveform_parameters=waveform_parameters,
            timing_parameters=timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )
        # endregion
        svg.configure_and_generate_square_waveform(svg_config)

else:
    # region SVG MultiTone configure and generate

    waveform_parameters = daq.SignalVoltageGenerationMultipleTonesWaveParameters(
        generated_signal_amplitude_volts=1.0,
        generated_signal_offset_volts=0.0,
        multiple_tones_parameters=multiple_tones_parameters,
    )

    svg_config = daq.SignalVoltageGenerationMultipleTonesConfiguration(
        voltage_generation_range_parameters=voltage_generation_range_parameters,
        waveform_parameters=waveform_parameters,
        timing_parameters=timing_parameters,
        digital_start_trigger_parameters=digital_start_trigger_parameters,
    )
    # endregion
    svg.configure_and_generate_multiple_tones_waveform(svg_config)


# region fdvm measure only

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
    digital_start_trigger_source="",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

fdvm_config = daq.FrequencyDomainMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_options=measurement_options,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion fdvm measure only
fdvm_result_data = fdvm.configure_and_measure(configuration=fdvm_config)

svg.close()
fdvm.close()

print("fdvm Result :\n")
print(fdvm_result_data)

print("Detected Tones")
print("Amplitudes (V)", fdvm_result_data.detected_tones[0].tones_amplitudes_volts)
print("Frequencies (Hz)", fdvm_result_data.detected_tones[0].tones_frequencies_hertz)


# region save traces

save_traces(config=fdvm_config, file_name="FDVM", result_data=fdvm_result_data)

save_traces(config=svg_config, file_name="SVG")

# endregion save traces

# region plot results

if plot_results is True:
    fdvm_w = fdvm_result_data.waveforms[0].samples.tolist()
    fdvm_mr = fdvm_result_data.magnitude_rms[0].amplitudes.tolist()
    fdvm_mp = fdvm_result_data.magnitude_peak[0].amplitudes.tolist()

    dt = fdvm_result_data.waveforms[0].delta_time_seconds
    t = np.arange(start=0, stop=generation_time, step=dt)
    df = fdvm_result_data.magnitude_rms[0].spectrum_frequency_resolution_hertz
    f = np.arange(start=0, stop=len(fdvm_mr) * df, step=df)

    pl.plot_three(
        y1=fdvm_w,
        y2=fdvm_mr,
        y3=fdvm_mp,
        x1=t,
        xlabel1="Time (s)",
        ylabel1="Voltage (V)",
        title1="Voltage waveforms",
        x2=f,
        xlabel2="Frequency (Hz)",
        ylabel2="Magnitude RMS (dBV)",
        title2="Magnitude RMS (dBV)",
        x3=f,
        xlabel3="Frequency (Hz)",
        ylabel3="Magnitude Peak (dBV)",
        title3="Magnitude Peak (dBV)",
        stitle="FDVM Waveforms",
        save_fig=save_fig,
    )

# endregion plot results
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_SVG_TDVM.py sha256=8f82df8cb9cf46201b48b1d6907d859ef66cb66ebb0fef505960790461367a19 bytes=7517 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_SVG_TDVM.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_SVG_TDVM.py`
- sha256: `8f82df8cb9cf46201b48b1d6907d859ef66cb66ebb0fef505960790461367a19`
- bytes: 7517

````python
# Signal Voltage Generation connected to Time Domain Measurement 
### Ensure correct hardware and corresponding trigger names before running this example

from enum import Enum

import nidaqmx.constants

import nipcbatt
from nipcbatt import daq
import nipcbatt.pcbatt_utilities.plotter as pl
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Global variable to plot
plot_results = True
save_fig = False

# Enums to select generation and Waveform types


class Generation_type(  
    Enum
):
    Single_tone = 0
    Multi_tone = 1


class Waveform_type(  
    Enum
):
    Sine_wave = 0
    Square_wave = 1


# INPUTS

# Configure Generation and Waveform types
generation_type = Generation_type.Single_tone
waveform_type = Waveform_type.Square_wave

# Multiple tones settings
multiple_tones_parameters = []
multiple_tones_parameters.append(
    daq.ToneParameters(
        tone_frequency_hertz=100, tone_amplitude_volts=1.0, tone_phase_radians=0
    )
)
multiple_tones_parameters.append(
    daq.ToneParameters(
        tone_frequency_hertz=200, tone_amplitude_volts=1.0, tone_phase_radians=1
    )
)

# Initialize
svg = daq.SignalVoltageGeneration()
svg.initialize(channel_expression="Dev1/ao0")

tdvm = daq.TimeDomainMeasurement()
tdvm.initialize(analog_input_channel_expression="Dev1/ai0")

# region tdvm configure only

global_channel_parameters = daq.VoltageRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
    range_min_volts=-10,
    range_max_volts=10,
)

sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=10000,
    number_of_samples_per_channel=1000,
    sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
)

specific_channels_parameters = []

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
    digital_start_trigger_source="/Dev1/ao/StartTrigger",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

tdvm_config = daq.TimeDomainMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_options=measurement_options,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion tdvm configure only
tdvm.configure_and_measure(configuration=tdvm_config)

# region configure SVG
voltage_generation_range_parameters = daq.VoltageGenerationChannelParameters(
    range_min_volts=-10, range_max_volts=10
)

timing_parameters = daq.SignalVoltageGenerationTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=100000,
    generated_signal_duration_seconds=0.1,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
    digital_start_trigger_source="",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

if generation_type == Generation_type.Single_tone:
    if waveform_type == Waveform_type.Sine_wave:
        # region SVG SineWave configure and generate

        generated_signal_tone_parameters = daq.ToneParameters(
            tone_frequency_hertz=100, tone_amplitude_volts=1, tone_phase_radians=0
        )

        waveform_parameters = daq.SignalVoltageGenerationSineWaveParameters(
            generated_signal_offset_volts=0,
            generated_signal_tone_parameters=generated_signal_tone_parameters,
        )

        svg_config = daq.SignalVoltageGenerationSineWaveConfiguration(
            voltage_generation_range_parameters=voltage_generation_range_parameters,
            waveform_parameters=waveform_parameters,
            timing_parameters=timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        # endregion
        svg.configure_and_generate_sine_waveform(svg_config)

    else:
        # region SVG SquareWave configure and generate

        waveform_parameters = daq.SignalVoltageGenerationSquareWaveParameters(
            generated_signal_amplitude_volts=1.0,
            generated_signal_duty_cycle_percent=50.00,
            generated_signal_frequency_hertz=100,
            generated_signal_phase_radians=0,
            generated_signal_offset_volts=0,
        )

        svg_config = daq.SignalVoltageGenerationSquareWaveConfiguration(
            voltage_generation_range_parameters=voltage_generation_range_parameters,
            waveform_parameters=waveform_parameters,
            timing_parameters=timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )
        # endregion
        svg.configure_and_generate_square_waveform(svg_config)

else:
    # region SVG MultiTone configure and generate

    waveform_parameters = daq.SignalVoltageGenerationMultipleTonesWaveParameters(
        generated_signal_amplitude_volts=1.0,
        generated_signal_offset_volts=0,
        multiple_tones_parameters=multiple_tones_parameters,
    )

    svg_config = daq.SignalVoltageGenerationMultipleTonesConfiguration(
        voltage_generation_range_parameters=voltage_generation_range_parameters,
        waveform_parameters=waveform_parameters,
        timing_parameters=timing_parameters,
        digital_start_trigger_parameters=digital_start_trigger_parameters,
    )
    # endregion
    svg.configure_and_generate_multiple_tones_waveform(svg_config)


# region tdvm measure only

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
    digital_start_trigger_source="",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

tdvm_config = daq.TimeDomainMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_options=measurement_options,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion tdvm measure only
tdvm_result_data = tdvm.configure_and_measure(configuration=tdvm_config)

svg.close()
tdvm.close()

print("TDVM result :\n")
print(tdvm_result_data)

# region save traces

save_traces(config=tdvm_config, file_name="TDVM", result_data=tdvm_result_data)

save_traces(config=svg_config, file_name="SVG")

# endregion save traces

# region plot results

if plot_results is True:
    tdvm_w = tdvm_result_data.waveforms[0].samples.tolist()
    pl.graph_plot(
        y=tdvm_w,
        title="TDVM Voltage",
        ylabel="Voltage (V)",
        xlabel="Samples",
        save_fig=save_fig,
    )

# # endregion plot results
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_SVG_TDVM_RSS.py sha256=e11a36a5aa50a9c1813b93d84e973ebdeb6611e708078b11521a3fae457319b4 bytes=8230 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_SVG_TDVM_RSS.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_SVG_TDVM_RSS.py`
- sha256: `e11a36a5aa50a9c1813b93d84e973ebdeb6611e708078b11521a3fae457319b4`
- bytes: 8230

````python
# Signal Voltage Generation from DAQ1 connected to Time Domain Measurement in DAQ2 using Route Synchronization 
### Ensure correct hardware and corresponding trigger names before running this example

from enum import Enum

import nidaqmx.constants

import nipcbatt
from nipcbatt import daq
import nipcbatt.pcbatt_utilities.plotter as pl
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Global variable to plot
plot_results = True
save_fig = False
use_specific_channel = False

# Enums to select generation and Waveform types


class Generation_type(  
    Enum
):
    Single_tone = 0
    Multi_tone = 1


class Waveform_type(  
    Enum
):
    Sine_wave = 0
    Square_wave = 1


# INPUTS

# Configure Generation and Waveform types
generation_type = Generation_type.Single_tone
waveform_type = Waveform_type.Square_wave

# Multiple tones settings
multiple_tones_parameters = []
multiple_tones_parameters.append(
    daq.ToneParameters(
        tone_frequency_hertz=100, tone_amplitude_volts=1.0, tone_phase_radians=0
    )
)
multiple_tones_parameters.append(
    daq.ToneParameters(
        tone_frequency_hertz=200, tone_amplitude_volts=1.0, tone_phase_radians=0
    )
)

# Initialize
svg = daq.SignalVoltageGeneration()
svg.initialize(channel_expression="Dev1/ao1")

tdvm = daq.TimeDomainMeasurement()
tdvm.initialize(analog_input_channel_expression="Dev2/ai0")


# Configure Routing paths
svg.route_start_trigger_signal_to_terminal(terminal_name="/Dev1/PFI0")
svg.route_sample_clock_signal_to_terminal(terminal_name="/Dev1/PFI1")


# region tdvm configure only

global_channel_parameters = daq.VoltageRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.DIFF,
    range_min_volts=-10,
    range_max_volts=10,
)

sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
    sample_clock_source="/Dev2/PFI1",
    sampling_rate_hertz=100000,
    number_of_samples_per_channel=10000,
    sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
)

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
    digital_start_trigger_source="/Dev2/PFI0",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

# Specific channel parameters

#    Channel 0
cp0 = daq.VoltageRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.DIFF,
    range_min_volts=-10,
    range_max_volts=10,
)

channel0 = daq.VoltageMeasurementChannelAndTerminalRangeParameters(
    channel_name="Dev2/ai0",
    channel_parameters=cp0,
)

specific_channels_parameters = []
if use_specific_channel is True:
    specific_channels_parameters.append(channel0)

tdvm_config = daq.TimeDomainMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_options=measurement_options,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion tdvm configure only
tdvm.configure_and_measure(configuration=tdvm_config)


# region configure SVG
voltage_generation_range_parameters = daq.VoltageGenerationChannelParameters(
    range_min_volts=-10, range_max_volts=10
)

timing_parameters = daq.SignalVoltageGenerationTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=100000,
    generated_signal_duration_seconds=0.1,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
    digital_start_trigger_source="",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

if generation_type == Generation_type.Single_tone:
    if waveform_type == Waveform_type.Sine_wave:
        # region SVG SineWave configure and generate

        generated_signal_tone_parameters = daq.ToneParameters(
            tone_frequency_hertz=100, tone_amplitude_volts=1, tone_phase_radians=0
        )

        waveform_parameters = daq.SignalVoltageGenerationSineWaveParameters(
            generated_signal_offset_volts=0,
            generated_signal_tone_parameters=generated_signal_tone_parameters,
        )

        svg_config = daq.SignalVoltageGenerationSineWaveConfiguration(
            voltage_generation_range_parameters=voltage_generation_range_parameters,
            waveform_parameters=waveform_parameters,
            timing_parameters=timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        # endregion
        svg.configure_and_generate_sine_waveform(svg_config)

    else:
        # region SVG SquareWave configure and generate

        waveform_parameters = daq.SignalVoltageGenerationSquareWaveParameters(
            generated_signal_amplitude_volts=1.0,
            generated_signal_duty_cycle_percent=50.00,
            generated_signal_frequency_hertz=100,
            generated_signal_phase_radians=4.71,
            generated_signal_offset_volts=0,
        )

        svg_config = daq.SignalVoltageGenerationSquareWaveConfiguration(
            voltage_generation_range_parameters=voltage_generation_range_parameters,
            waveform_parameters=waveform_parameters,
            timing_parameters=timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )
        # endregion
        svg.configure_and_generate_square_waveform(svg_config)

else:
    # region SVG MultiTone configure and generate

    waveform_parameters = daq.SignalVoltageGenerationMultipleTonesWaveParameters(
        generated_signal_amplitude_volts=1.0,
        generated_signal_offset_volts=0.0,
        multiple_tones_parameters=multiple_tones_parameters,
    )

    svg_config = daq.SignalVoltageGenerationMultipleTonesConfiguration(
        voltage_generation_range_parameters=voltage_generation_range_parameters,
        waveform_parameters=waveform_parameters,
        timing_parameters=timing_parameters,
        digital_start_trigger_parameters=digital_start_trigger_parameters,
    )
    # endregion
    svg.configure_and_generate_multiple_tones_waveform(svg_config)


# region tdvm measure only

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
    digital_start_trigger_source="/Dev1/ao/StartTrigger",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

tdvm_config = daq.TimeDomainMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_options=measurement_options,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion tdvm measure only
tdvm_result_data = tdvm.configure_and_measure(configuration=tdvm_config)

svg.close()
tdvm.close()

print("TDVM result :\n")
print(tdvm_result_data)

# region save traces

save_traces(config=tdvm_config, file_name="TDVM", result_data=tdvm_result_data)

save_traces(config=svg_config, file_name="SVG")

# endregion save traces

# region plot results

if plot_results is True:
    tdvm_w = tdvm_result_data.waveforms[0].samples.tolist()
    pl.graph_plot(
        y=tdvm_w,
        title="TDVM Voltage",
        ylabel="Voltage (V)",
        xlabel="Samples",
        save_fig=save_fig,
    )

# # endregion plot results
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_TTRM_DRVG.py sha256=caac2ad9a5c61e542c01ccafdc117869fd5dd9d47ff91b66687ce1550feab0ec bytes=6726 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_TTRM_DRVG.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/PC_Based_Examples/PC_TTRM_DRVG.py`
- sha256: `caac2ad9a5c61e542c01ccafdc117869fd5dd9d47ff91b66687ce1550feab0ec`
- bytes: 6726

````python
# Temperature Thermistor Measurement connected with DC Voltage Generation  
### Ensure correct hardware and corresponding trigger names before running this example

import matplotlib.pyplot as plt
import nidaqmx.constants
import numpy as np

import nipcbatt
from nipcbatt import daq
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Global variables
plot_results = True
save_fig = False
use_specific_channel = True

# Initialize
drvg = daq.DcVoltageGeneration()
drvg.initialize(analog_output_channel_expression="Dev1/ao2:3")

ttrm = daq.TemperatureMeasurementUsingThermistor()
ttrm.initialize("Dev1/ai2, Dev1/ai4")

# region drvg configure and generate

range_settings = daq.VoltageGenerationChannelParameters(
    range_min_volts=-10.0, range_max_volts=10.0
)

output_voltages = [10.0, 10.0]

drvg_config = daq.DcVoltageGenerationConfiguration(
    voltage_generation_range_parameters=range_settings, output_voltages=output_voltages
)

# endregion drvg configure and generate

drvg.configure_and_generate(drvg_config)

# region TTR configure and measure

coefficients_steinhart_hart_parameters = daq.CoefficientsSteinhartHartParameters(
    coefficient_steinhart_hart_a=0,
    coefficient_steinhart_hart_b=0,
    coefficient_steinhart_hart_c=0,
)

beta_coefficient_and_sensor_resistance_parameters = (
    daq.BetaCoefficientAndSensorResistanceParameters(
        coefficient_steinhart_hart_beta_kelvins=3720, sensor_resistance_ohms=5000
    )
)

global_channel_parameters = daq.TemperatureThermistorRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.DIFF,
    temperature_minimum_value_celsius_degrees=0,
    temperature_maximum_value_celsius_degrees=100,
    voltage_excitation_value_volts=10,
    thermistor_resistor_ohms=5000,
    steinhart_hart_equation_option=daq.SteinhartHartEquationOption.USE_COEFFICIENT_BETA_AND_SENSOR_RESISTANCE,
    coefficients_steinhart_hart_parameters=coefficients_steinhart_hart_parameters,
    beta_coefficient_and_sensor_resistance_parameters=beta_coefficient_and_sensor_resistance_parameters,
)

# region specific_channels_parameters

#   channel 0
coefficients_steinhart_hart_parameters_0 = daq.CoefficientsSteinhartHartParameters(
    coefficient_steinhart_hart_a=0,
    coefficient_steinhart_hart_b=0,
    coefficient_steinhart_hart_c=0,
)

beta_coefficient_and_sensor_resistance_parameters_0 = (
    daq.BetaCoefficientAndSensorResistanceParameters(
        coefficient_steinhart_hart_beta_kelvins=3720, sensor_resistance_ohms=5000
    )
)

channel_parameters_0 = daq.TemperatureThermistorRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.DIFF,
    temperature_minimum_value_celsius_degrees=0,
    temperature_maximum_value_celsius_degrees=100,
    voltage_excitation_value_volts=10,
    thermistor_resistor_ohms=4990,
    steinhart_hart_equation_option=daq.SteinhartHartEquationOption.USE_COEFFICIENT_BETA_AND_SENSOR_RESISTANCE,
    coefficients_steinhart_hart_parameters=coefficients_steinhart_hart_parameters_0,
    beta_coefficient_and_sensor_resistance_parameters=beta_coefficient_and_sensor_resistance_parameters_0,
)

channel0 = daq.TemperatureThermistorChannelRangeAndTerminalParameters(
    channel_name="Dev1/ai2", channel_parameters=channel_parameters_0
)

#   channel 1
coefficients_steinhart_hart_parameters_1 = daq.CoefficientsSteinhartHartParameters(
    coefficient_steinhart_hart_a=0,
    coefficient_steinhart_hart_b=0,
    coefficient_steinhart_hart_c=0,
)

beta_coefficient_and_sensor_resistance_parameters_1 = (
    daq.BetaCoefficientAndSensorResistanceParameters(
        coefficient_steinhart_hart_beta_kelvins=3720, sensor_resistance_ohms=10000
    )
)

channel_parameters_1 = daq.TemperatureThermistorRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.DIFF,
    temperature_minimum_value_celsius_degrees=0,
    temperature_maximum_value_celsius_degrees=100,
    voltage_excitation_value_volts=10,
    thermistor_resistor_ohms=10090,
    steinhart_hart_equation_option=daq.SteinhartHartEquationOption.USE_COEFFICIENT_BETA_AND_SENSOR_RESISTANCE,
    coefficients_steinhart_hart_parameters=coefficients_steinhart_hart_parameters_1,
    beta_coefficient_and_sensor_resistance_parameters=beta_coefficient_and_sensor_resistance_parameters_1,
)

channel1 = daq.TemperatureThermistorChannelRangeAndTerminalParameters(
    channel_name="Dev1/ai4", channel_parameters=channel_parameters_1
)

specific_channels_parameters = []
if use_specific_channel is True:
    specific_channels_parameters.append(channel0)
    specific_channels_parameters.append(channel1)

# endregion specific_channels_parameters

sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=10000,
    number_of_samples_per_channel=1000,
    sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
    digital_start_trigger_source="",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

ttrm_config = daq.TemperatureThermistorMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion TTR configure and measure

ttrm_result_data = ttrm.configure_and_measure(configuration=ttrm_config)

# Set DC Voltage to 0
output_voltages = [0.0, 0.0]

drvg_config1 = daq.DcVoltageGenerationConfiguration(
    voltage_generation_range_parameters=range_settings, output_voltages=output_voltages
)

drvg.configure_and_generate(drvg_config1)

drvg.close()
ttrm.close()


print("TTR result :\n")
print(ttrm_result_data)

# region save traces

save_traces(config=drvg_config, file_name="DRVG")

save_traces(config=ttrm_config, file_name="TTR", result_data=ttrm_result_data)

# endregion save traces

# region plot results

if plot_results is True:
    ttrm_w1 = ttrm_result_data.waveforms[0].samples.tolist()
    ttrm_w2 = ttrm_result_data.waveforms[1].samples.tolist()
    x1 = np.arange(0, len(ttrm_w1))
    x2 = np.arange(0, len(ttrm_w2))

    plt.plot(ttrm_w1)
    plt.plot(ttrm_w2)
    plt.show()

# endregion plot results
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/SWITCH_examples/default_ni_switch_generation.py sha256=add08fab4fa774c979c9ccfb0aabbac7bd42362bdbb0772c31ce32e2fd614561 bytes=1880 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/SWITCH_examples/default_ni_switch_generation.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/SWITCH_examples/default_ni_switch_generation.py`
- sha256: `add08fab4fa774c979c9ccfb0aabbac7bd42362bdbb0772c31ce32e2fd614561`
- bytes: 1880

````python
""" NI-SWITCH generation with default input parameters """

from nipcbatt import switch
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

def main():
    """Configures and executes default NI SWITCH generation with logging."""

    generation = switch.StaticDigitalPathGeneration()

    logger = PcbattLogger(file="c:\\Temp\\switch_logger.txt")
    logger.attach(generation)

    # declare all parameters necessary for path generaton
    resource_name = "Sim_MUX"
    topology = "2527/2-Wire Dual 16x1 Mux"
    p1, p2 = "ch0", "com0"
    max_wait_debounce = 100
    connect = True

    # instantiate parameters and settings objects
    channel_params = switch.StaticDigitalPathGenerationChannelParameters(p1, p2)
    state = switch.StaticDigitalPathGenerationStateParameters(connect)
    ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
    timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
    configuration = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)

    # print desired connection to user
    print('\nConnecting ' + p1 + ' to ' + p2)

    # ======================= Initialize the Switch ============================ #
    module_characteristics = generation.initialize(resource_name, topology)

    # =============== Configure and generate nominal configuration ============= #
    path_status = generation.configure_and_generate(configuration)

    # ======================== Close the Switch Session =========================== #
    generation.close()

    
    # print path status
    generation.display_status(path_status)

    #print module characteristics
    generation.display_module_characteristics(module_characteristics)
    print('\n') 

if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/SWITCH_examples/switch_validate_path_status.py sha256=d51caabdfcfeb2cd8e12847818763ee4483772df8c1373c44bd986a74cb1489f bytes=2999 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/SWITCH_examples/switch_validate_path_status.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/SWITCH_examples/switch_validate_path_status.py`
- sha256: `d51caabdfcfeb2cd8e12847818763ee4483772df8c1373c44bd986a74cb1489f`
- bytes: 2999

````python
""" Validates that the path capability between points is detected and reported correctly """

import niswitch
from nipcbatt import switch
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

generation = switch.StaticDigitalPathGeneration()

# Setup logger
logger = PcbattLogger(file="c:\\Temp\\switch_logger.txt")
logger.attach(generation)

resource_name = "Sim_MUX"
topology = "2527/2-Wire Dual 16x1 Mux"
max_wait_debounce = 100

#initialize session
module_characteristics = generation.initialize(resource_name, topology)

################## ch0 to ch1 connection ########################################################
channel_params1 = switch.StaticDigitalPathGenerationChannelParameters("ch0", "ch1")
state1 = switch.StaticDigitalPathGenerationStateParameters(True)
ts_settings1 = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params1, state1)
timing_settings1 = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
configuration1 = switch.StaticDigitalPathGenerationConfiguration(ts_settings1, timing_settings1)

path_status1 = generation.configure_and_generate(configuration1)
assert path_status1.path_status == niswitch.PathCapability.PATH_UNSUPPORTED

print()
print('ch0 to ch1')
generation.display_status(path_status1)

################# ch0 to com0 connection #########################################################
channel_params2 = switch.StaticDigitalPathGenerationChannelParameters("ch0", "com0")
state2 = switch.StaticDigitalPathGenerationStateParameters(True)
ts_settings2 = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params2, state2)
timing_settings2 = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
configuration2 = switch.StaticDigitalPathGenerationConfiguration(ts_settings2, timing_settings2)

path_status2 = generation.configure_and_generate(configuration2)
assert path_status2.path_status == niswitch.PathCapability.PATH_AVAILABLE

print()
print('ch0 to com0')
generation.display_status(path_status2)

################ ch1 to com0 connection ##########################################################
channel_params3 = switch.StaticDigitalPathGenerationChannelParameters("ch1", "com0")
state3 = switch.StaticDigitalPathGenerationStateParameters(True)
ts_settings3 = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params3, state3)
timing_settings3 = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
configuration3 = switch.StaticDigitalPathGenerationConfiguration(ts_settings3, timing_settings3)

path_status3 = generation.configure_and_generate(configuration3)
assert path_status3.path_status == niswitch.PathCapability.RESOURCE_IN_USE

print()
print('ch1 to com0')
generation.display_status(path_status3)

#close switch session
generation.close()

#print module characteristics
print()
generation.display_module_characteristics(module_characteristics)

print('\n')
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/TestScale_examples/TS_PSSM_to_DRCM.py sha256=314d58a70055209788a444c1c216a37f51bc296a6d09e31d2fb5d9a688e35579 bytes=5048 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/TestScale_examples/TS_PSSM_to_DRCM.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/TestScale_examples/TS_PSSM_to_DRCM.py`
- sha256: `314d58a70055209788a444c1c216a37f51bc296a6d09e31d2fb5d9a688e35579`
- bytes: 5048

````python
# DcRmsCurrentMeasurement connected with Power Supply Source and Measure without Trigger 
### Ensure correct hardware and corresponding trigger names before running this example

import nidaqmx.constants
import numpy as np

import nipcbatt
from nipcbatt import daq
import nipcbatt.pcbatt_utilities.plotter as pl
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Global variables
plot_results = True
save_fig = False
use_specific_channel = False

# Initialize
pssm = daq.PowerSupplySourceAndMeasure()
pssm.initialize("Simulated_TS1_Power/power")
drcm = daq.DcRmsCurrentMeasurement()
drcm.initialize("Simulated_TS1_AI/ai0")

# region PSSM configure and measure

terminal_parameters = daq.PowerSupplySourceAndMeasureTerminalParameters(
    voltage_setpoint_volts=6,
    current_setpoint_amperes=3,
    power_sense=nidaqmx.constants.Sense.LOCAL,
    idle_output_behaviour=nidaqmx.constants.PowerIdleOutputBehavior.MAINTAIN_EXISTING_VALUE,
    enable_output=True,
)

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=10000,
    number_of_samples_per_channel=1000,
    sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
    digital_start_trigger_source="",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

pssm_config = daq.PowerSupplySourceAndMeasureConfiguration(
    terminal_parameters=terminal_parameters,
    measurement_options=measurement_options,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion PSSM configure and measure

pssm_result_data = pssm.configure_and_measure(configuration=pssm_config)

# region DRCM configure and measure

global_channel_parameters = daq.DcRmsCurrentMeasurementTerminalRangeParameters(
    range_min_amperes=-3.0,
    range_max_amperes=3.0,
    shunt_resistor_ohms=0.13,
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
)

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=10000,
    number_of_samples_per_channel=1000,
    sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
    digital_start_trigger_source="",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

# Specific channel parameters

#    Channel 0
cp0 = daq.DcRmsCurrentMeasurementTerminalRangeParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
    range_min_amperes=-3,
    range_max_amperes=3,
    shunt_resistor_ohms=0.13,
)

channel0 = daq.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
    channel_name="Simulated_TS1_AI/ai4",
    channel_parameters=cp0,
)

specific_channels_parameters = []
if use_specific_channel is True:
    specific_channels_parameters.append(channel0)

drcm_config = daq.DcRmsCurrentMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_options=measurement_options,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion DRCM Configure and Measure

drcm_result_data = drcm.configure_and_measure(configuration=drcm_config)

drcm.close()
pssm.close()

print("PSSM result :\n")
print(pssm_result_data)
print("DRCM result :\n")
print(drcm_result_data)

# region save traces

save_traces(config=pssm_config, file_name="PSSM")

save_traces(config=drcm_config, file_name="DRCM", result_data=drcm_result_data)

# endregion save traces

# region plot results

if plot_results is True:
    pssm_v = pssm_result_data.voltage_waveform.samples
    drcm_w = drcm_result_data.waveforms[0].samples.tolist()
    x1 = np.arange(0, len(pssm_v))
    x2 = np.arange(0, len(drcm_w))
    pssm_c = pssm_result_data.current_waveform.samples
    pl.plot_two(
        y1=pssm_v,
        y2=drcm_w,
        x1=x1,
        ylabel1="Voltage (V)",
        ylabel2="Current (A)",
        x2=x2,
        stitle="PSSM Voltage and DRCM Current",
    )

# endregion plot results
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/TestScale_examples/TS_PSSM_to_TDVM.py sha256=841be97a08d754d670efdf6a030b0e07ffc3fa4df0b2380738f98bbb82b85153 bytes=6746 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/TestScale_examples/TS_PSSM_to_TDVM.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/TestScale_examples/TS_PSSM_to_TDVM.py`
- sha256: `841be97a08d754d670efdf6a030b0e07ffc3fa4df0b2380738f98bbb82b85153`
- bytes: 6746

````python
"""PSSM to TDVM""" 

### Ensure correct hardware and corresponding trigger names before running this example

import nidaqmx.constants
import numpy as np

import nipcbatt
from nipcbatt import daq
import nipcbatt.pcbatt_utilities.plotter as pl
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Global variables
plot_results = True
save_fig = False
use_specific_channel = False

# Initialize
pssm = daq.PowerSupplySourceAndMeasure()
pssm.initialize(power_channel_name="Simulated_TS1_Power/power")

tdvm = daq.TimeDomainMeasurement()
tdvm.initialize(analog_input_channel_expression="Simulated_TS1_AI/ai2")

# region TDVM configure only

global_channel_parameters = daq.VoltageRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
    range_min_volts=-10,
    range_max_volts=10,
)

# Specific channel parameters

channel_parameters = daq.VoltageRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.DIFF,
    range_max_volts=5,
    range_min_volts=-5,
)

channel0 = daq.VoltageMeasurementChannelAndTerminalRangeParameters(
    channel_name="Simulated_TS1_AI/ai2",
    channel_parameters=channel_parameters,
)

specific_channels_parameters = []
if use_specific_channel is True:
    specific_channels_parameters.append(channel0)

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=10000,
    number_of_samples_per_channel=1000,
    sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
    digital_start_trigger_source="/Sim_TS1/te0/StartTrigger",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

tdvm_config = daq.TimeDomainMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_options=measurement_options,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion TDVM configure only

tdvm.configure_and_measure(configuration=tdvm_config)

# region PSSM configure and measure

terminal_parameters = daq.PowerSupplySourceAndMeasureTerminalParameters(
    voltage_setpoint_volts=6,
    current_setpoint_amperes=3,
    power_sense=nidaqmx.constants.Sense.LOCAL,
    idle_output_behaviour=nidaqmx.constants.PowerIdleOutputBehavior.OUTPUT_DISABLED,
    enable_output=True,
)

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=10000,
    number_of_samples_per_channel=1000,
    sample_timing_engine=nipcbatt.SampleTimingEngine.TE0,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
    digital_start_trigger_source="",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

pssm_config = daq.PowerSupplySourceAndMeasureConfiguration(
    terminal_parameters=terminal_parameters,
    measurement_options=measurement_options,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion PSSM configure and measure

pssm_result_data = pssm.configure_and_measure(configuration=pssm_config)

# region TDVM measure only

global_channel_parameters = daq.VoltageRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
    range_min_volts=-10,
    range_max_volts=10,
)

specific_channels_parameters = []

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=10000,
    number_of_samples_per_channel=1000,
    sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
    digital_start_trigger_source="",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

tdvm_config = daq.TimeDomainMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_options=measurement_options,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion TDVM measure only

tdvm_result_data = tdvm.configure_and_measure(configuration=tdvm_config)

tdvm.close()
pssm.close()

print("PSSM result :\n")
print(pssm_result_data)

print("TDVM result :\n")
print(tdvm_result_data)


# region plot results

if plot_results is True:
    pssm_v = pssm_result_data.voltage_waveform.samples
    pssm_c = pssm_result_data.current_waveform.samples
    # np.linspace( )
    x1 = np.arange(0, len(pssm_v))
    x2 = np.arange(0, len(pssm_c))

    tdvm_w = tdvm_result_data.waveforms[0].samples.tolist()
    t = np.arange(0, len(tdvm_w))

    pl.plot_three(
        y1=pssm_v,
        y2=pssm_c,
        y3=tdvm_w,
        x1=x1,
        xlabel1="Samples",
        ylabel1="Voltage (V)",
        title1="PSSM Voltage",
        x2=x2,
        xlabel2="Samples",
        ylabel2="Current (A)",
        title2="PSSM Current",
        x3=t,
        xlabel3="Samples",
        ylabel3="Voltage (V))",
        title3="TDVM Voltage",
        stitle="PSSM to TDVM Waveforms",
        save_fig=save_fig,
    )

# endregion plot results

# region save traces

save_traces(config=pssm_config, file_name="PSSM", result_data=pssm_result_data)

save_traces(config=tdvm_config, file_name="TDVM", result_data=tdvm_result_data)

# endregion save traces
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_validation_examples/TestScale_examples/TS_TTRM_to_PSSM.py sha256=421e37666d0b22f8d5a2928de543eedac868360a33ac2fe192a42194ba4b3b82 bytes=6269 -->
## FILE: src/nipcbatt/pcbatt_validation_examples/TestScale_examples/TS_TTRM_to_PSSM.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_validation_examples/TestScale_examples/TS_TTRM_to_PSSM.py`
- sha256: `421e37666d0b22f8d5a2928de543eedac868360a33ac2fe192a42194ba4b3b82`
- bytes: 6269

````python
# Temperature Thermistor Measurement connected with Power Supply Source and Measure  
### Ensure correct hardware and corresponding trigger names before running this example

import nidaqmx.constants
import numpy as np

import nipcbatt
from nipcbatt import daq
import nipcbatt.pcbatt_utilities.plotter as pl
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Global variables
plot_results = True
save_fig = False
use_specific_channel = False

# Initialize
pssm = daq.PowerSupplySourceAndMeasure()
pssm.initialize("Simulated_TS1_Power/power")
ttr = daq.TemperatureMeasurementUsingThermistor()
ttr.initialize("TP_Rth0")

# region PSSM configure and measure

terminal_parameters = daq.PowerSupplySourceAndMeasureTerminalParameters(
    voltage_setpoint_volts=6,
    current_setpoint_amperes=3,
    power_sense=nidaqmx.constants.Sense.LOCAL,
    idle_output_behaviour=nidaqmx.constants.PowerIdleOutputBehavior.OUTPUT_DISABLED,  # Disable power output when idle
    enable_output=True,
)

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=10000,
    number_of_samples_per_channel=1000,
    sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
    digital_start_trigger_source="",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

pssm_config = daq.PowerSupplySourceAndMeasureConfiguration(
    terminal_parameters=terminal_parameters,
    measurement_options=measurement_options,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion PSSM configure and measure

pssm.configure_and_measure(configuration=pssm_config)

# region TTR configure and measure

coefficients_steinhart_hart_parameters = daq.CoefficientsSteinhartHartParameters(
    coefficient_steinhart_hart_a=0,
    coefficient_steinhart_hart_b=0,
    coefficient_steinhart_hart_c=0,
)

beta_coefficient_and_sensor_resistance_parameters = (
    daq.BetaCoefficientAndSensorResistanceParameters(
        coefficient_steinhart_hart_beta_kelvins=3720, sensor_resistance_ohms=10000
    )
)

global_channel_parameters = daq.TemperatureThermistorRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
    temperature_minimum_value_celsius_degrees=0,
    temperature_maximum_value_celsius_degrees=100,
    voltage_excitation_value_volts=6,
    thermistor_resistor_ohms=9980,
    steinhart_hart_equation_option=daq.SteinhartHartEquationOption.USE_COEFFICIENT_BETA_AND_SENSOR_RESISTANCE,
    coefficients_steinhart_hart_parameters=coefficients_steinhart_hart_parameters,
    beta_coefficient_and_sensor_resistance_parameters=beta_coefficient_and_sensor_resistance_parameters,
)

# region specific_channels_parameters

channel_coefficients_steinhart_hart_parameters = daq.CoefficientsSteinhartHartParameters(
    coefficient_steinhart_hart_a=0,
    coefficient_steinhart_hart_b=0,
    coefficient_steinhart_hart_c=0,
)

channel_beta_coefficient_and_sensor_resistance_parameters = (
    daq.BetaCoefficientAndSensorResistanceParameters(
        coefficient_steinhart_hart_beta_kelvins=0, sensor_resistance_ohms=0
    )
)

channel_parameters = daq.TemperatureThermistorRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
    temperature_minimum_value_celsius_degrees=0,
    temperature_maximum_value_celsius_degrees=100,
    voltage_excitation_value_volts=6,
    thermistor_resistor_ohms=9980,
    steinhart_hart_equation_option=daq.SteinhartHartEquationOption.USE_COEFFICIENT_BETA_AND_SENSOR_RESISTANCE,
    coefficients_steinhart_hart_parameters=channel_coefficients_steinhart_hart_parameters,
    beta_coefficient_and_sensor_resistance_parameters=channel_beta_coefficient_and_sensor_resistance_parameters,
)

channel0 = daq.TemperatureThermistorChannelRangeAndTerminalParameters(
    channel_name="TP_RTH0",
    channel_parameters=channel_parameters,
)

# endregion specific_channels_parameters

specific_channels_parameters = []
if use_specific_channel is True:
    specific_channels_parameters.append(channel0)

sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=10000,
    number_of_samples_per_channel=1000,
    sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
    digital_start_trigger_source="",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

ttr_config = daq.TemperatureThermistorMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion TTR configure and measure

ttr_result_data = ttr.configure_and_measure(configuration=ttr_config)

pssm.close()
ttr.close()

print("TTR result :\n")
print(ttr_result_data)

# region save traces

save_traces(config=pssm_config, file_name="PSSM")

save_traces(config=ttr_config, file_name="TTR", result_data=ttr_result_data)

# endregion save traces

# region plot results

if plot_results is True:
    ttr_w = ttr_result_data.waveforms[0].samples.tolist()
    dt = ttr_result_data.waveforms[0].delta_time_seconds
    tf = ttr_result_data.acquisition_duration_seconds
    t = np.arange(start=0, stop=tf, step=dt)

    pl.graph_plot(ttr_w)

# endregion plot results
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/__init__.py sha256=be00e9abedccb5e6725effc396d6aa3b60e6bb36530b4d9545cadab91271b163 bytes=275 -->
## FILE: tests/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/__init__.py`
- sha256: `be00e9abedccb5e6725effc396d6aa3b60e6bb36530b4d9545cadab91271b163`
- bytes: 275

````python
""" Provides a set of unit tests for nipcbatt and its dependencies, see requirements.txt """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (203 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/__init__.py sha256=20d46c339486c6f88a903d6a115edde214c9b9ae88d51a18bcad4bc772f4835d bytes=238 -->
## FILE: tests/nipcbatt_tests/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/__init__.py`
- sha256: `20d46c339486c6f88a903d6a115edde214c9b9ae88d51a18bcad4bc772f4835d`
- bytes: 238

````python
"""Provides a set of unit tests for nipcbatt package"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (166 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/__init__.py sha256=0678beca33a6da1fb93fda517f59e72a97790ff1b26c635758448abc4b72f0a8 bytes=254 -->
## FILE: tests/nipcbatt_tests/pcbatt_analysis_tests/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_analysis_tests/__init__.py`
- sha256: `0678beca33a6da1fb93fda517f59e72a97790ff1b26c635758448abc4b72f0a8`
- bytes: 254

````python
"""Provides a set of unit tests for nipcbatt.pcbatt_analysis package"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (182 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/common/__init__.py sha256=25bfc23df6f2f1a2133514334cd2df0537b62002aa5f3378e1978bfffdf4d515 bytes=261 -->
## FILE: tests/nipcbatt_tests/pcbatt_analysis_tests/common/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_analysis_tests/common/__init__.py`
- sha256: `25bfc23df6f2f1a2133514334cd2df0537b62002aa5f3378e1978bfffdf4d515`
- bytes: 261

````python
"""Provides a set of unit tests for nipcbatt.pcbatt_analysis.common package"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (189 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/common/test_common_types.py sha256=3f40ec7d5a58092313bd303bfdc78d9a79eb9050143ce319783a98bc00f81d1f bytes=9448 -->
## FILE: tests/nipcbatt_tests/pcbatt_analysis_tests/common/test_common_types.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_analysis_tests/common/test_common_types.py`
- sha256: `3f40ec7d5a58092313bd303bfdc78d9a79eb9050143ce319783a98bc00f81d1f`
- bytes: 9448

````python
"""Defines unit tests related to nipcbatt.pcbatt_analysis.common_types module."""

import logging
import math
import os
import platform
import sys
import unittest
from pathlib import Path

import numpy
from parameterized import parameterized
from varname import nameof

from nipcbatt.pcbatt_analysis.common.common_types import (
    AmplitudePhaseSpectrum,
    SpectrumAmplitudeType,
    SpectrumPhaseUnit,
    WaveformTone,
)


class TestSpectrumAmplitudeType(unittest.TestCase):
    """Provides unit tests of `SpectrumAmplitudeType` class.

    Args:
        unittest (TestCase): test cases fixture.
    """

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

    @parameterized.expand(
        [
            ("PEAK", SpectrumAmplitudeType.PEAK, 0),
            ("RMS", SpectrumAmplitudeType.RMS, 1),
        ]
    )
    def test_spectrum_amplitude_type_integer_values(
        self,
        case_name: str,
        actual_enum_value: SpectrumAmplitudeType,
        expected_int_value: int,
    ):
        """Test of enum `SpectrumAmplitudeType` integer values"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (176 > 100 characters) (auto-generated noqa)
        logging.debug("%s = %s", nameof(case_name), case_name)
        self.assertEqual(expected_int_value, actual_enum_value)


class TestSpectrumPhaseUnit(unittest.TestCase):
    """Provides unit tests of `SpectrumPhaseUnit` class.

    Args:
        unittest (TestCase): test cases fixture.
    """

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

    @parameterized.expand(
        [
            ("RADIAN", SpectrumPhaseUnit.RADIAN, 0),
            ("DEGREE", SpectrumPhaseUnit.DEGREE, 1),
        ]
    )
    def test_spectrum_phase_unit_integer_values(
        self,
        case_name: str,
        actual_enum_value: SpectrumPhaseUnit,
        expected_int_value: int,
    ):
        """Test of pcbatt_analysis.frequency_domain_analysis.FftSpectrumPhaseUnit integer values"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        logging.debug("%s = %s", nameof(case_name), case_name)
        self.assertEqual(expected_int_value, actual_enum_value)


class TestAmplitudePhaseSpectrum(unittest.TestCase):
    """Provides unit tests of `AmplitudePhaseSpectrum` class.

    Args:
        unittest (TestCase): test cases fixture.
    """

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

        # create tests output folder
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent
        cls.tests_output_folder_path = os.path.join(
            repository_dir_path,
            "tests_outputs",
            Path(__file__).stem,
            nameof(TestAmplitudePhaseSpectrum),
        )

        if not os.path.exists(cls.tests_output_folder_path):
            os.makedirs(cls.tests_output_folder_path, exist_ok=True)

    @parameterized.expand(
        [
            (
                "PEAK_NOT_DB_DEGREE",
                SpectrumAmplitudeType.PEAK,
                False,
                SpectrumPhaseUnit.DEGREE,
            ),
            (
                "RMS_DB_RADIAN",
                SpectrumAmplitudeType.RMS,
                True,
                SpectrumPhaseUnit.RADIAN,
            ),
        ]
    )
    def test_amplitude_phase_spectrum(
        self,
        case_name: str,
        expected_amplitude_type: SpectrumAmplitudeType,
        expected_amplitude_is_db: bool,
        expected_phase_unit: SpectrumPhaseUnit,
    ):
        """Test of `AmplitudePhaseSpectrum` class constructor."""
        logging.debug("%s = %s", nameof(case_name), case_name)

        # Act
        spectrum_instance = AmplitudePhaseSpectrum(
            f0=10,
            df=10,
            frequencies_amplitudes=numpy.array([0, 1, 2, 3]),
            spectrum_amplitude_type=expected_amplitude_type,
            spectrum_amplitude_unit_is_db=expected_amplitude_is_db,
            frequencies_phases=numpy.array([0, 0, 0, 0]),
            spectrum_phase_unit=expected_phase_unit,
        )

        spectrum_instance_repr = repr(spectrum_instance)
        logging.debug("%s = %s", nameof(spectrum_instance_repr), spectrum_instance_repr)

        # Assert
        self.assertIsNotNone(spectrum_instance)
        self.assertTrue(nameof(spectrum_instance.spectrum_amplitude_type) in spectrum_instance_repr)
        self.assertTrue(
            nameof(spectrum_instance.spectrum_amplitude_unit_is_db) in spectrum_instance_repr
        )

        self.assertTrue(nameof(spectrum_instance.spectrum_amplitudes) in spectrum_instance_repr)

        self.assertTrue(
            nameof(spectrum_instance.spectrum_frequency_resolution) in spectrum_instance_repr
        )
        self.assertTrue(nameof(spectrum_instance.spectrum_phase_unit) in spectrum_instance_repr)

        self.assertTrue(
            nameof(spectrum_instance.spectrum_start_frequency) in spectrum_instance_repr
        )

        self.assertEqual(4, spectrum_instance.spectrum_frequencies.size)
        self.assertEqual(4, spectrum_instance.spectrum_amplitudes.size)
        self.assertEqual(4, spectrum_instance.spectrum_phases.size)

        self.assertEqual(10, spectrum_instance.spectrum_frequencies[0])
        self.assertEqual(20, spectrum_instance.spectrum_frequencies[1])
        self.assertEqual(30, spectrum_instance.spectrum_frequencies[2])
        self.assertEqual(40, spectrum_instance.spectrum_frequencies[3])

        self.assertEqual(0, spectrum_instance.spectrum_amplitudes[0])
        self.assertEqual(1, spectrum_instance.spectrum_amplitudes[1])
        self.assertEqual(2, spectrum_instance.spectrum_amplitudes[2])
        self.assertEqual(3, spectrum_instance.spectrum_amplitudes[3])

        self.assertEqual(0, spectrum_instance.spectrum_phases[0])
        self.assertEqual(0, spectrum_instance.spectrum_phases[1])
        self.assertEqual(0, spectrum_instance.spectrum_phases[2])
        self.assertEqual(0, spectrum_instance.spectrum_phases[3])

        self.assertEqual(expected_amplitude_is_db, spectrum_instance.spectrum_amplitude_unit_is_db)

        self.assertEqual(expected_amplitude_type, spectrum_instance.spectrum_amplitude_type)

        self.assertEqual(expected_phase_unit, spectrum_instance.spectrum_phase_unit)


class TestWaveformTone(unittest.TestCase):
    """Defines a test fixture that checks
    `WaveformTone` class is ready to use.

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

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_waveform_tone(self):
        """Tests if an instance of `WaveformTone`
        is created with the specific values.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        waveform_tone = WaveformTone(frequency=440, amplitude=1, phase_radians=math.pi / 2)

        logging.debug("%s = %s", nameof(waveform_tone), repr(waveform_tone))
        self.assertEqual(440, waveform_tone.frequency)
        self.assertEqual(1, waveform_tone.amplitude)
        self.assertEqual(math.pi / 2, waveform_tone.phase_radians)
        self.assertEqual(90, waveform_tone.phase_degrees)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/test_analysis_library_info.py sha256=19bc711a1784f2a68e988a6b62633ea32e74d854acc3ab4a130044b6a78305d0 bytes=5296 -->
## FILE: tests/nipcbatt_tests/pcbatt_analysis_tests/test_analysis_library_info.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_analysis_tests/test_analysis_library_info.py`
- sha256: `19bc711a1784f2a68e988a6b62633ea32e74d854acc3ab4a130044b6a78305d0`
- bytes: 5296

````python
"""Defines unit tests related to nipcbatt.pcbatt_analysis.library_info module."""

import logging
import platform
import sys
import unittest

from varname import nameof

from nipcbatt.pcbatt_analysis import analysis_library_info
from nipcbatt.pcbatt_utilities import functional_utilities


class TestAnalysisLibraryInfo(unittest.TestCase):
    """Defines a test fixture that checks function of module
    `pcbatt_analysis.library_info`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        analysis_library_info.enable_traces(False)

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
        analysis_library_info.enable_traces(False)

    def test_get_labview_analysis_traces_folder_path(self):
        """Test of pcbatt_analysis.library_info.get_labview_analysis_traces_folder_path"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (201 > 100 characters) (auto-generated noqa)
        # Arrange
        analysis_library_info.enable_traces(True)

        # Act
        folder_path = analysis_library_info.get_labview_analysis_traces_folder_path()

        logging.debug("%s = %s", nameof(folder_path), folder_path)

        # Assert
        self.assertIsNotNone(folder_path)
        self.assertTrue(folder_path)

    @functional_utilities.repeat(10)
    def test_enable_traces(self):
        """Test of pcbatt_analysis.library_info.enable_traces"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (175 > 100 characters) (auto-generated noqa)
        analysis_library_info.enable_traces(True)
        traces_are_enabled = analysis_library_info.are_traces_enabled()

        self.assertTrue(traces_are_enabled)

        analysis_library_info.enable_traces(False)
        traces_are_enabled = analysis_library_info.are_traces_enabled()
        self.assertFalse(traces_are_enabled)

    @functional_utilities.repeat(10)
    def test_are_traces_enabled(self):
        """Test of pcbatt_analysis.library_info.are_traces_enabled"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (180 > 100 characters) (auto-generated noqa)
        traces_are_enabled = analysis_library_info.are_traces_enabled()
        self.assertFalse(traces_are_enabled)

    @functional_utilities.repeat(10)
    def test_is_labview_runtime_available(self):
        """Test of pcbatt_analysis.library_info.is_labview_runtime_available"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (190 > 100 characters) (auto-generated noqa)
        runtime_is_available = analysis_library_info.is_labview_runtime_available()
        self.assertIsNotNone(runtime_is_available)

    @functional_utilities.repeat(10)
    def test_get_labview_analysis_library_version_numbers(self):
        """Test of pcbatt_analysis.library_info.get_labview_analysis_library_version"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (198 > 100 characters) (auto-generated noqa)
        library_version_numbers = (
            analysis_library_info.get_labview_analysis_library_version_numbers()
        )

        logging.debug("%s = %s", nameof(library_version_numbers), library_version_numbers)

        self.assertIsNotNone(library_version_numbers)
        self.assertEqual(4, len(library_version_numbers))
        self.assertGreater(library_version_numbers[0], 0)
        self.assertGreater(library_version_numbers[3], 0)

    @functional_utilities.repeat(10)
    def test_get_labview_analysis_available_functions_names_list(self):
        """Test of pcbatt_analysis.library_info.get_supported_labview_functions_names_list"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (204 > 100 characters) (auto-generated noqa)
        labview_function_names = (
            analysis_library_info.get_labview_analysis_available_functions_names_list()
        )

        self.assertIsNotNone(labview_function_names)
        self.assertTrue(len(labview_function_names) >= 1)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_analysis/__init__.py sha256=a22c9a82aad6ebdbc691f7f63175dfe54a03b3843147ddff29436da8b83ef9ab bytes=272 -->
## FILE: tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_analysis/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_analysis/__init__.py`
- sha256: `a22c9a82aad6ebdbc691f7f63175dfe54a03b3843147ddff29436da8b83ef9ab`
- bytes: 272

````python
"""Provides a set of unit tests for nipcbatt.pcbatt_analysis.waveform_analysis package"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (200 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_analysis/test_amplitude_and_levels_analysis.py sha256=03ca987343fada71ef3d48c56cfb7100f5503a13749c981b4996401a3c33527f bytes=15114 -->
## FILE: tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_analysis/test_amplitude_and_levels_analysis.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_analysis/test_amplitude_and_levels_analysis.py`
- sha256: `03ca987343fada71ef3d48c56cfb7100f5503a13749c981b4996401a3c33527f`
- bytes: 15114

````python
"""Defines unit tests related to nipcbatt.pcbatt_analysis.amplitude_and_levels_analysis module."""

import argparse
import logging
import os
import platform
import sys
import unittest
from pathlib import Path

import numpy
from scipy import signal
from varname import nameof

from nipcbatt.pcbatt_analysis import analysis_library_info
from nipcbatt.pcbatt_analysis.waveform_analysis.amplitude_and_levels_analysis import (
    AmplitudeAndLevelsProcessingMethod,
    AmplitudeAndLevelsProcessingResult,
    LabViewAmplitudeAndLevels,
)
from nipcbatt.pcbatt_utilities import (
    csv_utilities,
    functional_utilities,
    numeric_utilities,
)


# Output result tests
class TestAmplitudeAndLevelsProcessingResult(unittest.TestCase):
    """Defines a test fixture that checks class AmplitudeAndLevelsProcessingResult of module
    `pcbatt_analysis.amplitude_and_levels_analysis`.

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

        # active debug traces of native dll
        analysis_library_info.enable_traces(True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")
        # active debug traces of native dll
        analysis_library_info.enable_traces(False)

    def test_amplitude_and_levels_processing_result(self):
        """Test of pcbatt_analysis.amplitude_and_levels_analysis.AmplitudeAndLevelsProcessingResult
        class constructor"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (398 > 100 characters) (auto-generated noqa)

        # Arrange + Act
        amplitude_and_levels_results_1 = AmplitudeAndLevelsProcessingResult(0, 0, 0)
        amplitude_and_levels_results_2 = AmplitudeAndLevelsProcessingResult(1, 1, -1)

        logging.debug(
            "%s = %s",
            nameof(amplitude_and_levels_results_1),
            str(amplitude_and_levels_results_1),
        )
        logging.debug(
            "%s = %s",
            nameof(amplitude_and_levels_results_2),
            str(amplitude_and_levels_results_2),
        )

        logging.debug(
            "repr(%s) = %s",
            nameof(amplitude_and_levels_results_1),
            repr(amplitude_and_levels_results_1),
        )
        logging.debug(
            "repr(%s) = %s",
            nameof(amplitude_and_levels_results_2),
            repr(amplitude_and_levels_results_2),
        )

        # Assert results 1
        self.assertIsNotNone(amplitude_and_levels_results_1)
        self.assertEqual(0, amplitude_and_levels_results_1.amplitude)
        self.assertEqual(0, amplitude_and_levels_results_1.high_state_level)
        self.assertEqual(0, amplitude_and_levels_results_1.low_state_level)

        # Assert results 2
        self.assertIsNotNone(amplitude_and_levels_results_2)
        self.assertEqual(1, amplitude_and_levels_results_2.amplitude)
        self.assertEqual(1, amplitude_and_levels_results_2.high_state_level)
        self.assertEqual(-1, amplitude_and_levels_results_2.low_state_level)


# LabVIEW VI tests
class TestLabViewAmplitudeAndLevels(unittest.TestCase):
    """Provides unit tests of LabViewAmplitudeAndLevels class.

    Args:
        unittest (TestCase): test cases fixture.
    """

    def setUp(self):
        # active debug traces of native dll
        analysis_library_info.enable_traces(True)

    def tearDown(self):
        # active debug traces of native dll
        analysis_library_info.enable_traces(False)

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

        # active debug traces of native dll
        analysis_library_info.enable_traces(True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")
        # active debug traces of native dll
        analysis_library_info.enable_traces(False)

    @functional_utilities.repeat(10)
    def test_get_last_error_message_returns_empty_string(self):
        """Test of pcbatt_analysis.amplitude_and_levels_analysis.LabViewAmplitudeAndLevels
        get_last_error_message method when there is no error"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (356 > 100 characters) (auto-generated noqa)
        last_error_message = LabViewAmplitudeAndLevels.get_last_error_message()
        self.assertEqual("", last_error_message)

    @functional_utilities.repeat(2)
    def test_process_single_waveform_amplitude_and_levels_auto_select_method_emv_trace(
        self,
    ):
        """Test of pcbatt_analysis.amplitude_and_levels.LabViewAmplitudeAndLevels
        process_single_waveform_amplitude_and_levels method using auto select analysis strategy
        using emv 106 Khz waveform.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_amplitude = 0.474
        expected_high_state = 0.476000212085181
        expected_low_state = 0.0018392165666242
        tolerance_percent = 0.1
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent.parent

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
        # Act
        amplitude_and_levels_result = LabViewAmplitudeAndLevels.process_single_waveform_amplitude_and_levels(
            waveform_samples=column_2_array,
            waveform_sampling_period_seconds=150_000_000,
            amplitude_and_levels_processing_method=AmplitudeAndLevelsProcessingMethod.AUTO_SELECT,
            histogram_size=512,
        )

        logging.debug(
            "%s = %s",
            nameof(amplitude_and_levels_result),
            repr(amplitude_and_levels_result),
        )

        # Assert
        self.assertAlmostEqual(
            first=expected_amplitude,
            second=amplitude_and_levels_result.amplitude,
            delta=numeric_utilities.percent_of(tolerance_percent, expected_amplitude),
        )
        self.assertAlmostEqual(
            first=expected_high_state,
            second=amplitude_and_levels_result.high_state_level,
            delta=numeric_utilities.percent_of(tolerance_percent, expected_high_state),
        )
        self.assertAlmostEqual(
            first=expected_low_state,
            second=amplitude_and_levels_result.low_state_level,
            delta=numeric_utilities.percent_of(tolerance_percent, expected_low_state),
        )

    @functional_utilities.repeat(10)
    def test_process_single_waveform_amplitude_and_levels_auto_select_method(self):
        """Test of pcbatt_analysis.amplitude_and_levels.LabViewAmplitudeAndLevels
        process_single_waveform_amplitude_and_levels method using auto select analysis strategy.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        t = numpy.linspace(0, 1, 500, endpoint=False)
        y = signal.square(2 * numpy.pi * 5 * t)

        logging.debug("%s = %s", nameof(t), t)
        logging.debug("%s = %s", nameof(y), y)

        # Act
        amplitude_and_levels_result = LabViewAmplitudeAndLevels.process_single_waveform_amplitude_and_levels(
            waveform_samples=y,
            waveform_sampling_period_seconds=1,
            amplitude_and_levels_processing_method=AmplitudeAndLevelsProcessingMethod.AUTO_SELECT,
            histogram_size=256,
        )

        logging.debug(
            "%s = %s",
            nameof(amplitude_and_levels_result),
            repr(amplitude_and_levels_result),
        )

        # Assert
        self.assertAlmostEqual(
            2,
            amplitude_and_levels_result.amplitude,
            delta=numeric_utilities.percent_of(0.8, 2),
        )
        self.assertAlmostEqual(
            1,
            amplitude_and_levels_result.high_state_level,
            delta=numeric_utilities.percent_of(0.8, 1),
        )
        self.assertAlmostEqual(
            -1,
            amplitude_and_levels_result.low_state_level,
            delta=numeric_utilities.percent_of(0.8, 1),
        )

    @functional_utilities.repeat(10)
    def test_process_single_waveform_amplitude_and_levels_histogram_method(self):
        """Test of pcbatt_analysis.amplitude_and_levels.LabViewAmplitudeAndLevels
        process_single_waveform_amplitude_and_levels method using histogram analysis strategy.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        t = numpy.linspace(0, 1, 500, endpoint=False)
        y = signal.square(2 * numpy.pi * 5 * t)

        logging.debug("%s = %s", nameof(t), t)
        logging.debug("%s = %s", nameof(y), y)

        # Act
        amplitude_and_levels_result = (
            LabViewAmplitudeAndLevels.process_single_waveform_amplitude_and_levels(
                waveform_samples=y,
                waveform_sampling_period_seconds=1,
                amplitude_and_levels_processing_method=AmplitudeAndLevelsProcessingMethod.HISTOGRAM,
                histogram_size=1024,
            )
        )

        logging.debug(
            "%s = %s",
            nameof(amplitude_and_levels_result),
            repr(amplitude_and_levels_result),
        )

        # Assert
        self.assertAlmostEqual(
            2,
            amplitude_and_levels_result.amplitude,
            delta=numeric_utilities.percent_of(0.1, 2),
        )

        self.assertAlmostEqual(
            1,
            amplitude_and_levels_result.high_state_level,
            delta=numeric_utilities.percent_of(0.1, 1),
        )

        self.assertAlmostEqual(
            -1,
            amplitude_and_levels_result.low_state_level,
            delta=numeric_utilities.percent_of(0.1, 1),
        )

    @functional_utilities.repeat(10)
    def test_process_single_waveform_amplitude_and_levels_peak_method(self):
        """Test of pcbatt_analysis.amplitude_and_levels.LabViewAmplitudeAndLevels
        process_single_waveform_amplitude_and_levels method using peak analysis strategy.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        t = numpy.linspace(0, 1, 500, endpoint=False)
        y = signal.sawtooth(2 * numpy.pi * 5 * t, 0.5)

        logging.debug("%s = %s", nameof(t), t)
        logging.debug("%s = %s", nameof(y), y)

        # Act
        amplitude_and_levels_result = (
            LabViewAmplitudeAndLevels.process_single_waveform_amplitude_and_levels(
                waveform_samples=y,
                waveform_sampling_period_seconds=1,
                amplitude_and_levels_processing_method=AmplitudeAndLevelsProcessingMethod.PEAK,
                histogram_size=1024,
            )
        )

        logging.debug(
            "%s = %s",
            nameof(amplitude_and_levels_result),
            repr(amplitude_and_levels_result),
        )

        # Assert
        self.assertEqual(
            2,
            amplitude_and_levels_result.amplitude,
        )

        self.assertEqual(
            1,
            amplitude_and_levels_result.high_state_level,
        )

        self.assertEqual(
            -1,
            amplitude_and_levels_result.low_state_level,
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--repeat", dest="repeat", help="repeat tests")
    (args, unitargs) = parser.parse_known_args()
    unitargs.insert(0, "placeholder")  # unittest ignores first arg

    # add more arguments to unitargs here
    repeat_count = int(vars(args)["repeat"] or 2)
    for iteration in range(repeat_count):
        was_successful = unittest.main(exit=False, argv=unitargs).result.wasSuccessful()
        if not was_successful:
            sys.exit(1)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_analysis/test_dc_rms_analysis.py sha256=fdd99eca8c054876951efe78955e54580801488181ad69f036486bc2b8454ca9 bytes=15089 -->
## FILE: tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_analysis/test_dc_rms_analysis.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_analysis/test_dc_rms_analysis.py`
- sha256: `fdd99eca8c054876951efe78955e54580801488181ad69f036486bc2b8454ca9`
- bytes: 15089

````python
"""Defines unit tests related to nipcbatt.pcbatt_analysis.dc_rms_analysis module."""

import argparse
import logging
import platform
import sys
import unittest

import numpy
from scipy import signal
from varname import nameof

from nipcbatt.pcbatt_analysis.waveform_analysis.dc_rms_analysis import (
    DcRmsProcessingResult,
    DcRmsProcessingWindow,
    LabViewBasicDcRms,
)
from nipcbatt.pcbatt_utilities import functional_utilities, numeric_utilities


# Output result tests
class TestDcRmsProcessingResult(unittest.TestCase):
    """Defines a test fixture that checks class DcRmsProcessingResult of module
    `pcbatt_analysis.dc_rms_analysis`.

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

    def test_dc_rms_processing_result(self):
        """Test of pcbatt_analysis.dc_rms_analysis.DcRmsProcessingResults class constructor"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (282 > 100 characters) (auto-generated noqa)

        # Arrange + Act
        dc_rms_results_1 = DcRmsProcessingResult(0, 0)
        dc_rms_results_2 = DcRmsProcessingResult(1, 0.707)

        logging.debug("%s = %s", nameof(dc_rms_results_1), repr(dc_rms_results_1))
        logging.debug("%s = %s", nameof(dc_rms_results_2), repr(dc_rms_results_2))

        # Assert results 1
        self.assertIsNotNone(dc_rms_results_1)
        self.assertEqual(0, dc_rms_results_1.dc_value)
        self.assertEqual(0, dc_rms_results_1.rms_value)

        # Assert results 2
        self.assertIsNotNone(dc_rms_results_2)
        self.assertEqual(1, dc_rms_results_2.dc_value)
        self.assertEqual(0.707, dc_rms_results_2.rms_value)


# LabVIEW VI tests
class TestLabViewBasicDcRms(unittest.TestCase):
    """Provides unit tests of LabViewBasicDcRms class.

    Args:
        unittest (TestCase): test cases fixture.
    """

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

    @functional_utilities.repeat(10)
    def test_get_last_error_message_returns_empty_string(self):
        """Test of pcbatt_analysis.dc_rms_analysis.LabViewDcRms
        get_last_error_message method when there is no error"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (356 > 100 characters) (auto-generated noqa)
        last_error_message = LabViewBasicDcRms.get_last_error_message()
        self.assertEqual("", last_error_message)

    @functional_utilities.repeat(10)
    def test_process_single_waveform_dc_rms_lsl_window(self):
        """Test of pcbatt_analysis.dc_rms_analysis.LabViewDcRms
        process_single_waveform_dc_rms method using low side lobe window"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (445 > 100 characters) (auto-generated noqa)

        # Arrange
        tolerance_percent = 0.1
        input_50 = signal.unit_impulse(5, 0)
        input_51 = signal.unit_impulse(5, 1)
        input_52 = signal.unit_impulse(5, 2)
        input_53 = signal.unit_impulse(5, 3)
        input_54 = signal.unit_impulse(5, 4)

        # Act
        dc_rms_50 = LabViewBasicDcRms.process_single_waveform_dc_rms(
            waveform_samples=input_50,
            waveform_sampling_period_seconds=1,
            dc_rms_processing_window=DcRmsProcessingWindow.LOW_SIDE_LOBE,
        )

        logging.debug("%s = %s", nameof(dc_rms_50), repr(dc_rms_50))

        dc_rms_51 = LabViewBasicDcRms.process_single_waveform_dc_rms(
            waveform_samples=input_51,
            waveform_sampling_period_seconds=1,
            dc_rms_processing_window=DcRmsProcessingWindow.LOW_SIDE_LOBE,
        )

        logging.debug("%s = %s", nameof(dc_rms_51), repr(dc_rms_51))

        dc_rms_52 = LabViewBasicDcRms.process_single_waveform_dc_rms(
            waveform_samples=input_52,
            waveform_sampling_period_seconds=1,
            dc_rms_processing_window=DcRmsProcessingWindow.LOW_SIDE_LOBE,
        )

        logging.debug("%s = %s", nameof(dc_rms_52), repr(dc_rms_52))

        dc_rms_53 = LabViewBasicDcRms.process_single_waveform_dc_rms(
            waveform_samples=input_53,
            waveform_sampling_period_seconds=1,
            dc_rms_processing_window=DcRmsProcessingWindow.LOW_SIDE_LOBE,
        )

        logging.debug("%s = %s", nameof(dc_rms_53), repr(dc_rms_53))

        dc_rms_54 = LabViewBasicDcRms.process_single_waveform_dc_rms(
            waveform_samples=input_54,
            waveform_sampling_period_seconds=1,
            dc_rms_processing_window=DcRmsProcessingWindow.LOW_SIDE_LOBE,
        )

        logging.debug("%s = %s", nameof(dc_rms_54), repr(dc_rms_54))

        # Assert
        # input 50
        self.assertAlmostEqual(13.45e-6, dc_rms_50.dc_value)
        self.assertAlmostEqual(20.20e-6, dc_rms_50.rms_value)

        # input 51
        self.assertAlmostEqual(
            0.03648,
            dc_rms_51.dc_value,
            delta=numeric_utilities.percent_of(percent=tolerance_percent, value=dc_rms_51.dc_value),
        )

        self.assertAlmostEqual(
            0.0548,
            dc_rms_51.rms_value,
            delta=numeric_utilities.percent_of(
                percent=tolerance_percent, value=dc_rms_51.rms_value
            ),
        )

        # input 52
        self.assertAlmostEqual(
            0.46352,
            dc_rms_52.dc_value,
            delta=numeric_utilities.percent_of(percent=tolerance_percent, value=dc_rms_52.dc_value),
        )

        self.assertAlmostEqual(
            0.69635,
            dc_rms_52.rms_value,
            delta=numeric_utilities.percent_of(
                percent=tolerance_percent, value=dc_rms_52.rms_value
            ),
        )

        # input 53
        self.assertAlmostEqual(
            0.46352,
            dc_rms_53.dc_value,
            delta=numeric_utilities.percent_of(percent=tolerance_percent, value=dc_rms_53.dc_value),
        )

        self.assertAlmostEqual(
            0.69635,
            dc_rms_53.rms_value,
            delta=numeric_utilities.percent_of(
                percent=tolerance_percent, value=dc_rms_53.rms_value
            ),
        )

        # input 54
        self.assertAlmostEqual(
            0.03648,
            dc_rms_54.dc_value,
            delta=numeric_utilities.percent_of(percent=tolerance_percent, value=dc_rms_54.dc_value),
        )

        self.assertAlmostEqual(
            0.05480,
            dc_rms_54.rms_value,
            delta=numeric_utilities.percent_of(
                percent=tolerance_percent, value=dc_rms_54.rms_value
            ),
        )

    @functional_utilities.repeat(10)
    def test_process_single_waveform_dc_rms_hann_window(self):
        """Test of pcbatt_analysis.dc_rms_analysis.LabViewDcRms
        process_single_waveform_dc_rms method using hann window"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (436 > 100 characters) (auto-generated noqa)

        # Arrange
        tolerance_percent = 0.1
        input_50 = signal.unit_impulse(5, 0)
        input_51 = signal.unit_impulse(5, 1)
        input_52 = signal.unit_impulse(5, 2)
        input_53 = signal.unit_impulse(5, 3)
        input_54 = signal.unit_impulse(5, 4)

        # Act
        dc_rms_50 = LabViewBasicDcRms.process_single_waveform_dc_rms(
            waveform_samples=input_50,
            waveform_sampling_period_seconds=1,
            dc_rms_processing_window=DcRmsProcessingWindow.HANN,
        )

        dc_rms_51 = LabViewBasicDcRms.process_single_waveform_dc_rms(
            waveform_samples=input_51,
            waveform_sampling_period_seconds=1,
            dc_rms_processing_window=DcRmsProcessingWindow.HANN,
        )

        dc_rms_52 = LabViewBasicDcRms.process_single_waveform_dc_rms(
            waveform_samples=input_52,
            waveform_sampling_period_seconds=1,
            dc_rms_processing_window=DcRmsProcessingWindow.HANN,
        )

        dc_rms_53 = LabViewBasicDcRms.process_single_waveform_dc_rms(
            waveform_samples=input_53,
            waveform_sampling_period_seconds=1,
            dc_rms_processing_window=DcRmsProcessingWindow.HANN,
        )

        dc_rms_54 = LabViewBasicDcRms.process_single_waveform_dc_rms(
            waveform_samples=input_54,
            waveform_sampling_period_seconds=1,
            dc_rms_processing_window=DcRmsProcessingWindow.HANN,
        )

        logging.debug("%s = %s", nameof(dc_rms_50), repr(dc_rms_50))
        logging.debug("%s = %s", nameof(dc_rms_51), repr(dc_rms_51))
        logging.debug("%s = %s", nameof(dc_rms_52), repr(dc_rms_52))
        logging.debug("%s = %s", nameof(dc_rms_53), repr(dc_rms_53))
        logging.debug("%s = %s", nameof(dc_rms_54), repr(dc_rms_54))

        # Assert
        # input 50
        self.assertAlmostEqual(0, dc_rms_50.dc_value)
        self.assertAlmostEqual(0, dc_rms_50.dc_value)

        # input 51
        self.assertAlmostEqual(
            0.13820,
            dc_rms_51.dc_value,
            delta=numeric_utilities.percent_of(percent=tolerance_percent, value=dc_rms_51.dc_value),
        )

        self.assertAlmostEqual(
            0.25231,
            dc_rms_51.rms_value,
            delta=numeric_utilities.percent_of(
                percent=tolerance_percent, value=dc_rms_51.rms_value
            ),
        )

        # input 52
        self.assertAlmostEqual(
            0.36180,
            dc_rms_52.dc_value,
            delta=numeric_utilities.percent_of(percent=tolerance_percent, value=dc_rms_52.dc_value),
        )

        self.assertAlmostEqual(
            0.66056,
            dc_rms_52.rms_value,
            delta=numeric_utilities.percent_of(
                percent=tolerance_percent, value=dc_rms_52.rms_value
            ),
        )

        # input 53
        self.assertAlmostEqual(
            0.36180,
            dc_rms_53.dc_value,
            delta=numeric_utilities.percent_of(percent=tolerance_percent, value=dc_rms_53.dc_value),
        )

        self.assertAlmostEqual(
            0.66056,
            dc_rms_53.rms_value,
            delta=numeric_utilities.percent_of(
                percent=tolerance_percent, value=dc_rms_53.rms_value
            ),
        )

        # input 54
        self.assertAlmostEqual(
            0.13820,
            dc_rms_54.dc_value,
            delta=numeric_utilities.percent_of(percent=tolerance_percent, value=dc_rms_54.dc_value),
        )

        self.assertAlmostEqual(
            0.25231,
            dc_rms_54.rms_value,
            delta=numeric_utilities.percent_of(
                percent=tolerance_percent, value=dc_rms_54.rms_value
            ),
        )

    @functional_utilities.repeat(10)
    def test_process_single_waveform_dc_rms_rectangular_window(self):
        """Test of pcbatt_analysis.dc_rms_analysis.LabViewDcRms
        process_single_waveform_dc_rms method using rectangular window"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (443 > 100 characters) (auto-generated noqa)

        samples = numpy.array(range(1, 11), dtype=numpy.float64)

        dc_rms_result = LabViewBasicDcRms.process_single_waveform_dc_rms(
            waveform_samples=samples,
            waveform_sampling_period_seconds=1.0,
            dc_rms_processing_window=DcRmsProcessingWindow.RECTANGULAR,
        )

        logging.debug("%s = %s", nameof(dc_rms_result), repr(dc_rms_result))

        self.assertGreaterEqual(dc_rms_result.dc_value, 5.5)
        self.assertGreaterEqual(dc_rms_result.rms_value, 6.2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--repeat", dest="repeat", help="repeat tests")
    (args, unitargs) = parser.parse_known_args()
    unitargs.insert(0, "placeholder")  # unittest ignores first arg

    # add more arguments to unitargs here
    repeat_count = int(vars(args)["repeat"] or 2)
    for iteration in range(repeat_count):
        was_successful = unittest.main(exit=False, argv=unitargs).result.wasSuccessful()
        if not was_successful:
            sys.exit(1)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_analysis/test_frequency_domain_analysis.py sha256=0fc223abcb01a660a3b4182d8ea3078abe0b1faa4fe76a3d6dc3da1b9e1ad46e bytes=38693 -->
## FILE: tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_analysis/test_frequency_domain_analysis.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_analysis/test_frequency_domain_analysis.py`
- sha256: `0fc223abcb01a660a3b4182d8ea3078abe0b1faa4fe76a3d6dc3da1b9e1ad46e`
- bytes: 38693

````python
"""Defines unit tests related to nipcbatt.pcbatt_analysis.frequency_domain_analysis module."""

import argparse
import logging
import math
import os
import platform
import sys
import unittest
from pathlib import Path

import numpy
import scipy.signal
from parameterized import parameterized
from varname import nameof

from nipcbatt.pcbatt_analysis import analysis_library_info
from nipcbatt.pcbatt_analysis.common.common_types import (
    AmplitudePhaseSpectrum,
    SpectrumAmplitudeType,
    SpectrumPhaseUnit,
    WaveformTone,
)
from nipcbatt.pcbatt_analysis.waveform_analysis.frequency_domain_analysis import (
    LabViewFftSpectrumAmplitudePhase,
    LabViewFftSpectrumWindow,
    LabViewFrequencyDomainProcessing,
    LabViewMultipleTonesMeasurement,
    LabViewTonesSortingMode,
    MultipleTonesAmplitudePhaseSpectrumProcessingResult,
    MultipleTonesProcessingResult,
)
from nipcbatt.pcbatt_analysis.waveform_creation import sine_waveform, square_waveform
from nipcbatt.pcbatt_utilities import (
    csv_utilities,
    functional_utilities,
    numeric_utilities,
)


# Input types
class TestLabViewFftSpectrumWindow(unittest.TestCase):
    """Provides unit tests of `FftSpectrumWindow` class.

    Args:
        unittest (TestCase): test cases fixture.
    """

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

    @parameterized.expand(
        [
            ("RECTANGLE", LabViewFftSpectrumWindow.RECTANGLE, 0),
            ("HANNING", LabViewFftSpectrumWindow.HANNING, 1),
            ("HAMMING", LabViewFftSpectrumWindow.HAMMING, 2),
            ("BLACKMAN_HARRIS", LabViewFftSpectrumWindow.BLACKMAN_HARRIS, 3),
            ("BLACKMAN_EXACT", LabViewFftSpectrumWindow.BLACKMAN_EXACT, 4),
            ("BLACKMAN", LabViewFftSpectrumWindow.BLACKMAN, 5),
            ("FLAT_TOP", LabViewFftSpectrumWindow.FLAT_TOP, 6),
            ("BHARRIS_4TERMS", LabViewFftSpectrumWindow.BHARRIS_4TERMS, 7),
            ("BHARRIS_7TERMS", LabViewFftSpectrumWindow.BHARRIS_7TERMS, 8),
            ("LOW_LATERAL_LOBE", LabViewFftSpectrumWindow.LOW_LATERAL_LOBE, 9),
            ("BLACKMAN_NUTTALL", LabViewFftSpectrumWindow.BLACKMAN_NUTTALL, 11),
            ("TRIANGLE", LabViewFftSpectrumWindow.TRIANGLE, 30),
            ("BARTLETT_HANNING", LabViewFftSpectrumWindow.BARTLETT_HANNING, 31),
            ("BOHMAN", LabViewFftSpectrumWindow.BOHMAN, 32),
            ("PARZEN", LabViewFftSpectrumWindow.PARZEN, 33),
            ("WELCH", LabViewFftSpectrumWindow.WELCH, 34),
            ("KAISER", LabViewFftSpectrumWindow.KAISER, 60),
            ("DOLPH_TCHEBYCHEV", LabViewFftSpectrumWindow.DOLPH_TCHEBYCHEV, 61),
            ("GAUSSIAN", LabViewFftSpectrumWindow.GAUSSIAN, 62),
        ]
    )
    def test_labview_fft_spectrum_window_integer_values(
        self,
        case_name: str,
        actual_enum_value: LabViewFftSpectrumWindow,
        expected_int_value: int,
    ):
        """Test of `LabViewFftSpectrumWindow` integer values"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (174 > 100 characters) (auto-generated noqa)
        logging.debug("%s = %s", nameof(case_name), case_name)
        self.assertEqual(expected_int_value, actual_enum_value)


# Results types
class TestMultipleTonesProcessingResult(unittest.TestCase):
    """Provides unit tests of `MultipleTonesProcessingResult` class.

    Args:
        unittest (TestCase): test cases fixture.
    """

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

        # create tests output folder
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent
        cls.tests_output_folder_path = os.path.join(
            repository_dir_path,
            "tests_outputs",
            Path(__file__).stem,
            nameof(TestMultipleTonesProcessingResult),
        )

        if not os.path.exists(cls.tests_output_folder_path):
            os.makedirs(cls.tests_output_folder_path, exist_ok=True)

    @parameterized.expand(
        [
            ("PEAK_AMPLITUDE_440Hz_90_Degrees", SpectrumAmplitudeType.PEAK, 1, 440, 90),
            (
                "RMS_AMPLITUDE_440Hz_90_Degrees",
                SpectrumAmplitudeType.RMS,
                0.707,
                440,
                90,
            ),
            (
                "RMS_AMPLITUDE_440Hz_180_Degrees",
                SpectrumAmplitudeType.RMS,
                0.707,
                440,
                180,
            ),
        ]
    )
    def test_multiple_tones_processing_result_single_tone_waveform(
        self,
        case_name: str,
        expected_amplitude_type: SpectrumAmplitudeType,
        expected_amplitude_value: float,
        expected_frequency_value: float,
        expected_phase_degrees: float,
    ):
        """Test of AmplitudePhaseSpectrum class constructor."""
        logging.debug("%s = %s", nameof(case_name), case_name)

        # Act
        multiple_tones_processing_result = MultipleTonesProcessingResult(
            detected_tones=[
                WaveformTone(
                    frequency=expected_frequency_value,
                    amplitude=expected_amplitude_value,
                    phase_radians=math.radians(expected_phase_degrees),
                )
            ],
            amplitude_type=expected_amplitude_type,
        )
        logging.debug(
            "%s = %s",
            nameof(multiple_tones_processing_result),
            repr(multiple_tones_processing_result),
        )

        # Assert
        self.assertEqual(expected_amplitude_type, multiple_tones_processing_result.amplitude_type)

        self.assertEqual(1, len(multiple_tones_processing_result.detected_tones))

        self.assertEqual(expected_amplitude_type, multiple_tones_processing_result.amplitude_type)
        self.assertEqual(
            expected_amplitude_value,
            multiple_tones_processing_result.detected_tones[0].amplitude,
        )

        self.assertEqual(
            expected_frequency_value,
            multiple_tones_processing_result.detected_tones[0].frequency,
        )
        self.assertEqual(
            expected_phase_degrees,
            multiple_tones_processing_result.detected_tones[0].phase_degrees,
        )


# Frequency domain processing tests
class TestMultipleTonesAmplitudePhaseSpectrumProcessingResult(unittest.TestCase):
    """Provides unit tests of `MultipleTonesAmplitudePhaseSpectrumProcessingResult` class.

    Args:
        unittest (TestCase): test cases fixture.
    """

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

        # activate debug traces of native dll
        analysis_library_info.enable_traces(True)

        # create tests output folder
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent
        cls.tests_output_folder_path = os.path.join(
            repository_dir_path,
            "tests_outputs",
            Path(__file__).stem,
            nameof(TestMultipleTonesAmplitudePhaseSpectrumProcessingResult),
        )

        if not os.path.exists(cls.tests_output_folder_path):
            os.makedirs(cls.tests_output_folder_path, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")
        # active debug traces of native dll
        analysis_library_info.enable_traces(False)

    def test_multiple_tones_amplitude_phase_spectrum_processing_result(self):
        """Test of `MultipleTonesAmplitudePhaseSpectrumProcessingResult` class constructor."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (180 > 100 characters) (auto-generated noqa)

        # Arrange
        expected_single_tone_amplitude = 4000
        expected_single_tone_frequency = 11
        expected_single_tone_phase_degrees = 90
        expected_phase_unit = SpectrumPhaseUnit.DEGREE
        expected_amplitude_type = SpectrumAmplitudeType.PEAK

        # Act
        multiple_tones_amplitude_phase_spectrum = (
            MultipleTonesAmplitudePhaseSpectrumProcessingResult(
                multiple_tones_result=MultipleTonesProcessingResult(
                    detected_tones=[
                        WaveformTone(
                            frequency=expected_single_tone_frequency,
                            amplitude=expected_single_tone_amplitude,
                            phase_radians=math.radians(expected_single_tone_phase_degrees),
                        )
                    ],
                    amplitude_type=expected_amplitude_type,
                ),
                amplitude_phase_spectrum=AmplitudePhaseSpectrum(
                    f0=10,
                    df=1,
                    frequencies_amplitudes=numpy.array(
                        [5, expected_single_tone_amplitude, 3, 2, 1]
                    ),
                    spectrum_amplitude_type=expected_amplitude_type,
                    spectrum_amplitude_unit_is_db=False,
                    frequencies_phases=numpy.array(
                        [180, expected_single_tone_phase_degrees, 45, 22.5, 0]
                    ),
                    spectrum_phase_unit=expected_phase_unit,
                ),
            )
        )

        logging.debug(
            "%s = %s",
            nameof(multiple_tones_amplitude_phase_spectrum),
            repr(multiple_tones_amplitude_phase_spectrum),
        )

        # Assert
        self.assertIsNotNone(multiple_tones_amplitude_phase_spectrum.multiple_tones_result)
        self.assertIsNotNone(multiple_tones_amplitude_phase_spectrum.amplitude_phase_spectrum)

        self.assertEqual(
            1,
            len(multiple_tones_amplitude_phase_spectrum.multiple_tones_result.detected_tones),
        )

        self.assertEqual(
            expected_single_tone_amplitude,
            multiple_tones_amplitude_phase_spectrum.multiple_tones_result.detected_tones[
                0
            ].amplitude,
        )

        self.assertEqual(
            expected_single_tone_frequency,
            multiple_tones_amplitude_phase_spectrum.multiple_tones_result.detected_tones[
                0
            ].frequency,
        )

        self.assertEqual(
            expected_single_tone_phase_degrees,
            multiple_tones_amplitude_phase_spectrum.multiple_tones_result.detected_tones[
                0
            ].phase_degrees,
        )


# LabVIEW VIs tests


class TestLabViewFrequencyDomainProcessing(unittest.TestCase):
    """Provides unit tests of `FrequencyDomainProcessing` class.

    Args:
        unittest (TestCase): test cases fixture.
    """

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

        # activate debug traces of native dll
        analysis_library_info.enable_traces(True)

        # create tests output folder
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent
        cls.tests_output_folder_path = os.path.join(
            repository_dir_path,
            "tests_outputs",
            Path(__file__).stem,
            nameof(TestLabViewFrequencyDomainProcessing),
        )

        if not os.path.exists(cls.tests_output_folder_path):
            os.makedirs(cls.tests_output_folder_path, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")
        # active debug traces of native dll
        analysis_library_info.enable_traces(False)

    @functional_utilities.repeat(10)
    def test_process_single_waveform_multiple_tones_and_amplitude_phase_spectrum_square_waveform(
        self,
    ):
        """Test of `LabViewFrequencyDomainProcessing`
        `process_single_waveform_multiple_tones_and_amplitude_phase_spectrum`
        method when there is no error"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (333 > 100 characters) (auto-generated noqa)
        # Arrange
        waveform_sampling_rate = 44100
        waveform_sampling_period = 1 / waveform_sampling_rate
        waveform_duration_seconds = 0.1
        waveform_samples_count = (int)(waveform_duration_seconds * waveform_sampling_rate)
        waveform_amplitude = 1
        waveform_frequency = 440

        spectrum_view_settings_amplitude_is_db = False
        spectrum_view_settings_phase_unit = SpectrumPhaseUnit.DEGREE
        spectrum_view_settings_amplitude_type = SpectrumAmplitudeType.RMS

        wanted_tones_selection_threshold = 0.15

        expected_spectrum_size = 2205
        expected_tones_count_above_threshold = 4

        square_waveform_samples = square_waveform.create_square_waveform(
            amplitude=waveform_amplitude,
            frequency=waveform_frequency,
            duty_cycle=0.5,
            phase=0,
            offset=0,
            samples_count=waveform_samples_count,
            sampling_rate=waveform_sampling_rate,
        )

        # Act
        fdvm_results = LabViewFrequencyDomainProcessing.process_single_waveform_multiple_tones_and_amplitude_phase_spectrum(
            waveform_samples=square_waveform_samples,
            waveform_sampling_period_seconds=waveform_sampling_period,
            spectrum_amplitude_must_be_db=spectrum_view_settings_amplitude_is_db,
            spectrum_phase_unit=spectrum_view_settings_phase_unit,
            fft_spectrum_window=LabViewFftSpectrumWindow.HANNING,
            tones_sorting_mode=LabViewTonesSortingMode.DECREASING_AMPLITUDES,
            tones_selection_threshold_peak_amplitude=wanted_tones_selection_threshold,
        )

        square_waveform_magnitude_phase_spectrum = fdvm_results.amplitude_phase_spectrum
        square_waveform_multiple_tones = fdvm_results.multiple_tones_result

        csv_file_ouput_path = os.path.join(
            TestLabViewFrequencyDomainProcessing.tests_output_folder_path,
            "test_process_single_waveform_multiple_tones_and_amplitude_phase_spectrum_square_waveform.csv",
        )

        csv_utilities.export_columns_to_csv_file(
            csv_file_path=csv_file_ouput_path,
            column1_data=square_waveform_magnitude_phase_spectrum.spectrum_frequencies,
            column2_data=square_waveform_magnitude_phase_spectrum.spectrum_amplitudes,
            column1_name="Frequency (Hz)",
            column2_name="RMS Amplitude",
        )

        logging.debug(
            "%s count = %s",
            nameof(square_waveform_magnitude_phase_spectrum.spectrum_amplitudes),
            len(square_waveform_magnitude_phase_spectrum.spectrum_amplitudes),
        )

        logging.debug(
            "%s count = %s",
            nameof(square_waveform_multiple_tones.detected_tones),
            len(square_waveform_multiple_tones.detected_tones),
        )

        logging.debug(
            "%s repr = %s",
            nameof(square_waveform_multiple_tones.detected_tones),
            repr(square_waveform_multiple_tones.detected_tones),
        )

        # Assert
        self.assertIsNotNone(square_waveform_magnitude_phase_spectrum)
        self.assertEqual(
            expected_spectrum_size,
            square_waveform_magnitude_phase_spectrum.spectrum_frequencies.size,
        )

        self.assertEqual(
            expected_spectrum_size,
            square_waveform_magnitude_phase_spectrum.spectrum_amplitudes.size,
        )

        self.assertEqual(
            expected_spectrum_size,
            square_waveform_magnitude_phase_spectrum.spectrum_phases.size,
        )

        self.assertEqual(
            spectrum_view_settings_amplitude_is_db,
            square_waveform_magnitude_phase_spectrum.spectrum_amplitude_unit_is_db,
        )

        self.assertEqual(
            spectrum_view_settings_phase_unit,
            square_waveform_magnitude_phase_spectrum.spectrum_phase_unit,
        )

        self.assertEqual(
            spectrum_view_settings_amplitude_type,
            square_waveform_magnitude_phase_spectrum.spectrum_amplitude_type,
        )

        self.assertEqual(
            expected_tones_count_above_threshold,
            len(square_waveform_multiple_tones.detected_tones),
        )

        for detected_tone in square_waveform_multiple_tones.detected_tones:
            self.assertGreaterEqual(detected_tone.amplitude, wanted_tones_selection_threshold)

    def test_process_single_waveform_multiple_tones_and_amplitude_phase_spectrum_modulated_waveform_amplitude_is_db(
        self,
    ):
        """Test of `LabViewFrequencyDomainProcessing`
        `process_single_waveform_multiple_tones_and_amplitude_phase_spectrum` method when there is no error
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (107 > 100 characters) (auto-generated noqa)
        # Arrange
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent.parent

        logging.debug("%s = %s", nameof(repository_dir_path), repository_dir_path)

        emv_csv_file_path = os.path.join(
            repository_dir_path, "pcbatt.testdata", "EMV_Waveform_TA123.csv"
        )
        logging.debug("%s = %s", nameof(emv_csv_file_path), emv_csv_file_path)

        (_, column_2_array) = csv_utilities.import_from_csv_file_2d_array(
            csv_file_path=emv_csv_file_path, header_is_present=False
        )

        wanted_tones_selection_threshold = 0.02

        # Act
        fdvm_results = LabViewFrequencyDomainProcessing.process_single_waveform_multiple_tones_and_amplitude_phase_spectrum(
            waveform_samples=column_2_array,
            waveform_sampling_period_seconds=1 / 150_000_000,
            spectrum_amplitude_must_be_db=True,
            spectrum_phase_unit=SpectrumPhaseUnit.DEGREE,
            fft_spectrum_window=LabViewFftSpectrumWindow.HANNING,
            tones_sorting_mode=LabViewTonesSortingMode.DECREASING_AMPLITUDES,
            tones_selection_threshold_peak_amplitude=wanted_tones_selection_threshold,
        )

        waveform_magnitude_phase_spectrum = fdvm_results.amplitude_phase_spectrum
        waveform_multiple_tones = fdvm_results.multiple_tones_result

        logging.debug(
            "%s count = %s",
            nameof(waveform_magnitude_phase_spectrum.spectrum_amplitudes),
            len(waveform_magnitude_phase_spectrum.spectrum_amplitudes),
        )

        logging.debug(
            "%s count = %s",
            nameof(waveform_multiple_tones.detected_tones),
            len(waveform_multiple_tones.detected_tones),
        )

        logging.debug(
            "%s repr = %s",
            nameof(waveform_multiple_tones.detected_tones),
            repr(waveform_multiple_tones.detected_tones),
        )

        csv_file_ouput_path = os.path.join(
            TestLabViewFrequencyDomainProcessing.tests_output_folder_path,
            "test_process_single_waveform_multiple_tones_and_amplitude_phase_spectrum_modulated_waveform_amplitude_is_db.csv",
        )

        csv_utilities.export_columns_to_csv_file(
            csv_file_path=csv_file_ouput_path,
            column1_data=waveform_magnitude_phase_spectrum.spectrum_frequencies,
            column2_data=waveform_magnitude_phase_spectrum.spectrum_amplitudes,
            column1_name="Frequency (Hz)",
            column2_name="RMS Amplitude",
        )

        for detected_tone in waveform_multiple_tones.detected_tones:
            self.assertGreaterEqual(detected_tone.amplitude, wanted_tones_selection_threshold)


class TestLabViewFftSpectrumAmplitudePhase(unittest.TestCase):
    """Provides unit tests of `LabViewFftSpectrumAmplitudePhase` class.

    Args:
        unittest (TestCase): test cases fixture.
    """

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

        # activate debug traces of native dll
        analysis_library_info.enable_traces(True)

        # create tests output folder
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent
        cls.tests_output_folder_path = os.path.join(
            repository_dir_path,
            "tests_outputs",
            Path(__file__).stem,
            nameof(TestLabViewFftSpectrumAmplitudePhase),
        )

        if not os.path.exists(cls.tests_output_folder_path):
            os.makedirs(cls.tests_output_folder_path, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")
        # active debug traces of native dll
        analysis_library_info.enable_traces(False)

    @functional_utilities.repeat(10)
    def test_get_last_error_message_returns_empty_string(self):
        """Test of `LabViewFftSpectrumAmplitudePhase`
        get_last_error_message method when there is no error"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (356 > 100 characters) (auto-generated noqa)
        error_message = LabViewFftSpectrumAmplitudePhase.get_last_error_message()
        self.assertEqual("", error_message)

    @parameterized.expand(
        [
            ("PEAK_AMPLITUDE", SpectrumAmplitudeType.PEAK),
            ("RMS_AMPLITUDE", SpectrumAmplitudeType.RMS),
        ]
    )
    def test_process_single_waveform_magnitude_phase_spectrum_single_tone_waveform(
        self, case_name: str, amplitude_type: SpectrumAmplitudeType
    ):
        """Test of `LabViewFftSpectrumAmplitudePhase`
        `process_single_waveform_amplitude_phase_spectrum` method when there is no error
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        logging.debug("%s = %s", nameof(case_name), case_name)

        # Arrange
        waveform_sampling_rate = 44100
        waveform_sampling_period = 1 / waveform_sampling_rate
        waveform_duration_seconds = 0.1
        waveform_samples_count = (int)(waveform_duration_seconds * waveform_sampling_rate)
        waveform_amplitude = 1
        waveform_frequency = 440

        spectrum_view_settings_amplitude_is_db = False
        spectrum_view_settings_phase_unit = SpectrumPhaseUnit.DEGREE
        spectrum_view_settings_amplitude_type = amplitude_type

        expected_spectrum_size = 2205

        square_waveform_samples = sine_waveform.create_sine_waveform(
            amplitude=waveform_amplitude,
            frequency=waveform_frequency,
            phase=math.radians(45),
            offset=0,
            samples_count=waveform_samples_count,
            sampling_rate=waveform_sampling_rate,
        )

        # Act
        square_waveform_magnitude_phase_spectrum = (
            LabViewFftSpectrumAmplitudePhase.process_single_waveform_amplitude_phase_spectrum(
                waveform_samples=square_waveform_samples,
                waveform_sampling_period_seconds=waveform_sampling_period,
                spectrum_amplitude_must_be_db=spectrum_view_settings_amplitude_is_db,
                spectrum_amplitude_type=spectrum_view_settings_amplitude_type,
                spectrum_phase_unit=spectrum_view_settings_phase_unit,
                fft_spectrum_window=LabViewFftSpectrumWindow.HANNING,
            )
        )

        csv_file_ouput_path = os.path.join(
            TestLabViewFftSpectrumAmplitudePhase.tests_output_folder_path,
            f"test_process_single_waveform_magnitude_phase_spectrum_single_tone_waveform_{str(amplitude_type)}.csv",
        )

        csv_utilities.export_columns_to_csv_file(
            csv_file_path=csv_file_ouput_path,
            column1_data=square_waveform_magnitude_phase_spectrum.spectrum_frequencies,
            column2_data=square_waveform_magnitude_phase_spectrum.spectrum_amplitudes,
            column1_name="Frequency (Hz)",
            column2_name=f"{str(amplitude_type)} Amplitude",
        )

        # Assert
        self.assertIsNotNone(square_waveform_magnitude_phase_spectrum)
        self.assertEqual(
            expected_spectrum_size,
            square_waveform_magnitude_phase_spectrum.spectrum_frequencies.size,
        )

        self.assertEqual(
            expected_spectrum_size,
            square_waveform_magnitude_phase_spectrum.spectrum_amplitudes.size,
        )

        self.assertEqual(
            expected_spectrum_size,
            square_waveform_magnitude_phase_spectrum.spectrum_phases.size,
        )

        self.assertEqual(
            spectrum_view_settings_amplitude_is_db,
            square_waveform_magnitude_phase_spectrum.spectrum_amplitude_unit_is_db,
        )

        self.assertEqual(
            spectrum_view_settings_phase_unit,
            square_waveform_magnitude_phase_spectrum.spectrum_phase_unit,
        )

        self.assertEqual(
            spectrum_view_settings_amplitude_type,
            square_waveform_magnitude_phase_spectrum.spectrum_amplitude_type,
        )

        # Assert amplitudes
        max_amplitude = square_waveform_magnitude_phase_spectrum.spectrum_amplitudes.max()

        if spectrum_view_settings_amplitude_type == SpectrumAmplitudeType.PEAK:
            self.assertAlmostEqual(1, max_amplitude, delta=0.001)

        if spectrum_view_settings_amplitude_type == SpectrumAmplitudeType.RMS:
            self.assertAlmostEqual(0.707, max_amplitude, delta=0.001)

    @parameterized.expand(
        [
            ("PEAK_AMPLITUDE", SpectrumAmplitudeType.PEAK),
            ("RMS_AMPLITUDE", SpectrumAmplitudeType.RMS),
        ]
    )
    def test_process_single_waveform_magnitude_phase_spectrum_square_waveform(
        self, case_name: str, amplitude_type: SpectrumAmplitudeType
    ):
        """Test of `LabViewFftSpectrumAmplitudePhase`
        `process_single_waveform_amplitude_phase_spectrum` method when there is no error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        logging.debug("%s = %s", nameof(case_name), case_name)

        # Arrange
        waveform_sampling_rate = 44100
        waveform_sampling_period = 1 / waveform_sampling_rate
        waveform_duration_seconds = 0.1
        waveform_samples_count = (int)(waveform_duration_seconds * waveform_sampling_rate)
        waveform_amplitude = 1
        waveform_frequency = 440

        spectrum_view_settings_amplitude_is_db = False
        spectrum_view_settings_phase_unit = SpectrumPhaseUnit.DEGREE
        spectrum_view_settings_amplitude_type = amplitude_type

        expected_spectrum_size = 2205

        square_waveform_samples = square_waveform.create_square_waveform(
            amplitude=waveform_amplitude,
            frequency=waveform_frequency,
            duty_cycle=0.5,
            phase=0,
            offset=0,
            samples_count=waveform_samples_count,
            sampling_rate=waveform_sampling_rate,
        )

        # Act
        square_waveform_magnitude_phase_spectrum = (
            LabViewFftSpectrumAmplitudePhase.process_single_waveform_amplitude_phase_spectrum(
                waveform_samples=square_waveform_samples,
                waveform_sampling_period_seconds=waveform_sampling_period,
                spectrum_amplitude_must_be_db=spectrum_view_settings_amplitude_is_db,
                spectrum_amplitude_type=spectrum_view_settings_amplitude_type,
                spectrum_phase_unit=spectrum_view_settings_phase_unit,
                fft_spectrum_window=LabViewFftSpectrumWindow.HANNING,
            )
        )

        csv_file_ouput_path = os.path.join(
            TestLabViewFftSpectrumAmplitudePhase.tests_output_folder_path,
            f"test_process_single_waveform_magnitude_phase_spectrum_square_waveform_{str(amplitude_type)}.csv",
        )

        csv_utilities.export_columns_to_csv_file(
            csv_file_path=csv_file_ouput_path,
            column1_data=square_waveform_magnitude_phase_spectrum.spectrum_frequencies,
            column2_data=square_waveform_magnitude_phase_spectrum.spectrum_amplitudes,
            column1_name="Frequency (Hz)",
            column2_name=f"{str(amplitude_type)} Amplitude",
        )

        spectrum_peaks = scipy.signal.find_peaks(
            x=square_waveform_magnitude_phase_spectrum.spectrum_amplitudes,
        )

        logging.debug(
            "%s count = %s",
            nameof(square_waveform_magnitude_phase_spectrum.spectrum_amplitudes),
            len(square_waveform_magnitude_phase_spectrum.spectrum_amplitudes),
        )
        logging.debug("%s count = %s", nameof(spectrum_peaks), len(spectrum_peaks[0]))
        logging.debug("%s indexes = %s", nameof(spectrum_peaks), spectrum_peaks[0])

        # Assert
        self.assertIsNotNone(square_waveform_magnitude_phase_spectrum)
        self.assertEqual(
            expected_spectrum_size,
            square_waveform_magnitude_phase_spectrum.spectrum_frequencies.size,
        )

        self.assertEqual(
            expected_spectrum_size,
            square_waveform_magnitude_phase_spectrum.spectrum_amplitudes.size,
        )

        self.assertEqual(
            expected_spectrum_size,
            square_waveform_magnitude_phase_spectrum.spectrum_phases.size,
        )

        self.assertEqual(
            spectrum_view_settings_amplitude_is_db,
            square_waveform_magnitude_phase_spectrum.spectrum_amplitude_unit_is_db,
        )

        self.assertEqual(
            spectrum_view_settings_phase_unit,
            square_waveform_magnitude_phase_spectrum.spectrum_phase_unit,
        )

        self.assertEqual(
            spectrum_view_settings_amplitude_type,
            square_waveform_magnitude_phase_spectrum.spectrum_amplitude_type,
        )


class TestLabViewMultipleTonesMeasurement(unittest.TestCase):
    """Provides unit tests of `LabViewMultipleTonesMeasurement` class.

    Args:
        unittest (TestCase): test cases fixture.
    """

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

        # activate debug traces of native dll
        analysis_library_info.enable_traces(True)

        # create tests output folder
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent
        cls.tests_output_folder_path = os.path.join(
            repository_dir_path,
            "tests_outputs",
            Path(__file__).stem,
            nameof(TestLabViewMultipleTonesMeasurement),
        )

        if not os.path.exists(cls.tests_output_folder_path):
            os.makedirs(cls.tests_output_folder_path, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")
        # active debug traces of native dll
        analysis_library_info.enable_traces(False)

    @functional_utilities.repeat(10)
    def test_get_last_error_message_returns_empty_string(self):
        """Test of `LabViewMultipleTonesMeasurement`
        get_last_error_message method when there is no error"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (356 > 100 characters) (auto-generated noqa)
        error_message = LabViewMultipleTonesMeasurement.get_last_error_message()
        self.assertEqual("", error_message)

    @functional_utilities.repeat(10)
    def test_process_single_waveform_multiple_tones_square_waveform(self):
        """Test of `LabViewMultipleTonesMeasurement`
        process_single_waveform_multiple_tones method when there is no error"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (372 > 100 characters) (auto-generated noqa)
        # Arrange
        waveform_sampling_rate = 44100
        waveform_sampling_period = 1 / waveform_sampling_rate
        waveform_duration_seconds = 0.1
        waveform_samples_count = (int)(waveform_duration_seconds * waveform_sampling_rate)
        waveform_amplitude = 1
        waveform_frequency = 440
        max_tones_count = 10
        tones_selection_threshold = 0.1
        expected_tones_count_above_threshold = 6
        comparison_tolerance_percent = 0.1

        square_waveform_samples = square_waveform.create_square_waveform(
            amplitude=waveform_amplitude,
            frequency=waveform_frequency,
            duty_cycle=0.5,
            phase=0,
            offset=0,
            samples_count=waveform_samples_count,
            sampling_rate=waveform_sampling_rate,
        )

        # Act
        square_waveform_tones = (
            LabViewMultipleTonesMeasurement.process_single_waveform_multiple_tones(
                waveform_samples=square_waveform_samples,
                waveform_sampling_period_seconds=waveform_sampling_period,
                tones_selection_threshold=tones_selection_threshold,
                tones_max_count=max_tones_count,
                tones_sorting_mode=LabViewTonesSortingMode.DECREASING_AMPLITUDES,
            )
        )

        logging.debug("%s = %s", nameof(square_waveform_tones), repr(square_waveform_tones))

        # Assert
        self.assertEqual(SpectrumAmplitudeType.PEAK, square_waveform_tones.amplitude_type)
        self.assertEqual(
            expected_tones_count_above_threshold,
            len(square_waveform_tones.detected_tones),
        )

        for waveform_tone, waveform_tone_index in zip(
            square_waveform_tones.detected_tones,
            range(0, len(square_waveform_tones.detected_tones)),
        ):
            self.assertGreaterEqual(a=waveform_tone.amplitude, b=tones_selection_threshold)

            k = waveform_tone_index
            expected_tone_frequency = (2 * k + 1) * waveform_frequency

            self.assertAlmostEqual(
                first=expected_tone_frequency,
                second=waveform_tone.frequency,
                delta=numeric_utilities.percent_of(
                    percent=comparison_tolerance_percent, value=expected_tone_frequency
                ),
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--repeat", dest="repeat", help="repeat tests")
    (args, unitargs) = parser.parse_known_args()
    unitargs.insert(0, "placeholder")  # unittest ignores first arg

    # add more arguments to unitargs here
    repeat_count = int(vars(args)["repeat"] or 2)
    for iteration in range(repeat_count):
        was_successful = unittest.main(exit=False, argv=unitargs).result.wasSuccessful()
        if not was_successful:
            sys.exit(1)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_analysis/test_pulse_analog_analysis.py sha256=7619b60c9c96e5c73a50a7a3379f9ae63397530f56f7b16413df0b9aa0bf36e2 bytes=49432 -->
## FILE: tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_analysis/test_pulse_analog_analysis.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_analysis/test_pulse_analog_analysis.py`
- sha256: `7619b60c9c96e5c73a50a7a3379f9ae63397530f56f7b16413df0b9aa0bf36e2`
- bytes: 49432

````python
"""Defines unit tests related to nipcbatt.pcbatt_analysis.pulse_analog_analysis module."""

import argparse
import importlib.metadata
import logging
import os
import platform
import sys
import unittest
from pathlib import Path

import numpy
import scipy
from varname import nameof

from nipcbatt.pcbatt_analysis import analysis_library_info
from nipcbatt.pcbatt_analysis.waveform_analysis.amplitude_and_levels_analysis import (
    AmplitudeAndLevelsProcessingMethod,
)
from nipcbatt.pcbatt_analysis.waveform_analysis.pulse_analog_analysis import (
    LabViewPulseAnalogMeasurements,
    PulseAnalogMeasurementPercentLevelsSettings,
    PulseAnalogProcessingExportMode,
    PulseAnalogProcessingPolarity,
    PulseAnalogProcessingReferenceLevels,
    PulseAnalogProcessingReferenceLevelsUnit,
    PulseAnalogProcessingResult,
    WaveformPeriodicityAnalogProcessingResult,
)
from nipcbatt.pcbatt_utilities import (
    csv_utilities,
    functional_utilities,
    numeric_utilities,
)

# Output result tests


class TestPulseAnalogProcessingReferenceLevels(unittest.TestCase):
    """Defines a test fixture that checks class `PulseAnalogProcessingReferenceLevels` of module
    `pcbatt_analysis.waveform_analysis.pulse_analog_analysis`.

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

    def test_pulse_analog_processing_reference_levels(self):
        """Test of `pcbatt_analysis.pulse_analog_analysis.PulseAnalogProcessingReferenceLevels`
        class constructor"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (398 > 100 characters) (auto-generated noqa)

        # Arrange
        expected_reference_level_high = 5
        expected_reference_level_middle = 4.5
        expected_reference_level_low = 1

        # Act
        pulse_analog_processing_reference_levels = PulseAnalogProcessingReferenceLevels(
            reference_level_high=expected_reference_level_high,
            reference_level_middle=expected_reference_level_middle,
            reference_level_low=expected_reference_level_low,
        )

        logging.debug(
            "%s = %s",
            nameof(pulse_analog_processing_reference_levels),
            repr(pulse_analog_processing_reference_levels),
        )

        # Assert result
        self.assertIsNotNone(pulse_analog_processing_reference_levels)
        self.assertEqual(
            first=expected_reference_level_high,
            second=pulse_analog_processing_reference_levels.reference_level_high,
        )
        self.assertEqual(
            first=expected_reference_level_middle,
            second=pulse_analog_processing_reference_levels.reference_level_middle,
        )
        self.assertEqual(
            first=expected_reference_level_low,
            second=pulse_analog_processing_reference_levels.reference_level_low,
        )


class TestWaveformPeriodicityAnalogProcessingResult(unittest.TestCase):
    """Defines a test fixture that checks class `PulsePeriodicityAnalogProcessingResult` of module
    `pcbatt_analysis.waveform_analysis.pulse_analog_analysis`.

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

    def test_waveform_periodicity_analog_processing_result(self):
        """Test of `pcbatt_analysis.pulse_analog_analysis.WaveformPeriodicityAnalogProcessingResult`
        class constructor"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (398 > 100 characters) (auto-generated noqa)

        # Arrange + Act
        pulse_periodicty_results = WaveformPeriodicityAnalogProcessingResult(
            period=1, duty_cycle=0.5
        )

        logging.debug(
            "%s = %s",
            nameof(pulse_periodicty_results),
            repr(pulse_periodicty_results),
        )

        # Assert result
        self.assertIsNotNone(pulse_periodicty_results)
        self.assertEqual(first=1, second=pulse_periodicty_results.period)
        self.assertEqual(first=1, second=pulse_periodicty_results.frequency)
        self.assertEqual(first=0.5, second=pulse_periodicty_results.duty_cycle)
        self.assertEqual(first=50, second=pulse_periodicty_results.duty_cycle_percent)

    def test_waveform_periodicity_analog_processing_result_invalid_inputs(self):
        """Test of `pcbatt_analysis.pulse_analog_analysis.WaveformPeriodicityAnalogProcessingResult`
        class constructor"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (398 > 100 characters) (auto-generated noqa)

        # Arrange + Act + Assert
        self.assertRaises(
            ValueError,
            lambda: WaveformPeriodicityAnalogProcessingResult(period=0, duty_cycle=0.5),
        )

        self.assertRaises(
            ValueError,
            lambda: WaveformPeriodicityAnalogProcessingResult(period=1, duty_cycle=-0.5),
        )

        self.assertRaises(
            ValueError,
            lambda: WaveformPeriodicityAnalogProcessingResult(period=-1, duty_cycle=0.5),
        )


class TestPulseAnalogMeasurementPercentLevelsSettings(unittest.TestCase):
    """Defines a test fixture that checks class
        `PulseAnalogMeasurementPercentLevelsSettings` of module
        `pcbatt_analysis.waveform_analysis.pulse_analog_analysis`.

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

        # active debug traces of native dll
        analysis_library_info.enable_traces(True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")
        # active debug traces of native dll
        analysis_library_info.enable_traces(False)

    def test_pulse_analog_measurement_percent_levels_settings_invalid_inputs(self):
        """Test of
        `pcbatt_analysis.pulse_analog_analysis.PulseAnalogMeasurementPercentLevelsSettings`
        class constructor
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self.assertRaises(
            ValueError,
            lambda: PulseAnalogMeasurementPercentLevelsSettings(
                AmplitudeAndLevelsProcessingMethod.AUTO_SELECT,
                histogram_size=0,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: PulseAnalogMeasurementPercentLevelsSettings(
                AmplitudeAndLevelsProcessingMethod.AUTO_SELECT,
                histogram_size=-0.5,
            ),
        )

    def test_pulse_analog_measurement_percent_levels_settings(self):
        """Test of
        `pcbatt_analysis.pulse_analog_analysis.PulseAnalogMeasurementPercentLevelsSettings`
        class constructor
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # Arrange
        expected_histogram_size = 256
        expected_amplitude_and_levels_processing_method_1 = (
            AmplitudeAndLevelsProcessingMethod.AUTO_SELECT
        )
        expected_amplitude_and_levels_processing_method_2 = (
            AmplitudeAndLevelsProcessingMethod.HISTOGRAM
        )
        expected_amplitude_and_levels_processing_method_3 = AmplitudeAndLevelsProcessingMethod.PEAK

        # Act
        pulse_analog_processing_settings_1 = PulseAnalogMeasurementPercentLevelsSettings(
            expected_amplitude_and_levels_processing_method_1,
            histogram_size=expected_histogram_size,
        )

        pulse_analog_processing_settings_2 = PulseAnalogMeasurementPercentLevelsSettings(
            expected_amplitude_and_levels_processing_method_2,
            histogram_size=expected_histogram_size,
        )

        pulse_analog_processing_settings_3 = PulseAnalogMeasurementPercentLevelsSettings(
            expected_amplitude_and_levels_processing_method_3,
            histogram_size=expected_histogram_size,
        )

        logging.debug(
            "%s = %s",
            nameof(pulse_analog_processing_settings_1),
            repr(pulse_analog_processing_settings_1),
        )

        logging.debug(
            "%s = %s",
            nameof(pulse_analog_processing_settings_2),
            repr(pulse_analog_processing_settings_2),
        )

        logging.debug(
            "%s = %s",
            nameof(pulse_analog_processing_settings_3),
            repr(pulse_analog_processing_settings_3),
        )

        # Assert results
        self.assertIsNotNone(pulse_analog_processing_settings_1)
        self.assertIsNotNone(pulse_analog_processing_settings_2)
        self.assertIsNotNone(pulse_analog_processing_settings_3)

        self.assertEqual(
            first=expected_histogram_size,
            second=pulse_analog_processing_settings_1.histogram_size,
        )
        self.assertEqual(
            first=expected_histogram_size,
            second=pulse_analog_processing_settings_2.histogram_size,
        )
        self.assertEqual(
            first=expected_histogram_size,
            second=pulse_analog_processing_settings_3.histogram_size,
        )

        self.assertEqual(
            first=expected_amplitude_and_levels_processing_method_1,
            second=pulse_analog_processing_settings_1.amplitude_and_levels_processing_method,
        )

        self.assertEqual(
            first=expected_amplitude_and_levels_processing_method_2,
            second=pulse_analog_processing_settings_2.amplitude_and_levels_processing_method,
        )

        self.assertEqual(
            first=expected_amplitude_and_levels_processing_method_3,
            second=pulse_analog_processing_settings_3.amplitude_and_levels_processing_method,
        )


class TestPulseAnalogProcessingResult(unittest.TestCase):
    """Defines a test fixture that checks class PulseAnalogProcessingResult of module
    `pcbatt_analysis.waveform_analysis.pulse_analog_analysis`.

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

        # active debug traces of native dll
        analysis_library_info.enable_traces(True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")
        # active debug traces of native dll
        analysis_library_info.enable_traces(False)

    def test_pulse_analog_processing_result(self):
        """Test of `pcbatt_analysis.pulse_analog_analysis.PulseAnalogProcessingResult`
        class constructor"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (398 > 100 characters) (auto-generated noqa)

        # Arrange
        expected_pulse_center = 125
        expected_pulse_duration = 10
        expected_pulse_reference_level_high = 90
        expected_pulse_reference_level_middle = 50
        expected_pulse_reference_level_low = 10
        expected_period = 2
        expected_frequency = 0.5
        expected_duty_cycle = 0.5
        expected_duty_cycle_percent = 50

        # Act
        pulse_analog_processing_results_1 = PulseAnalogProcessingResult(
            pulse_center=expected_pulse_center,
            pulse_duration=expected_pulse_duration,
            pulse_reference_level_high=expected_pulse_reference_level_high,
            pulse_reference_level_middle=expected_pulse_reference_level_middle,
            pulse_reference_level_low=expected_pulse_reference_level_low,
        )

        pulse_analog_processing_results_2 = PulseAnalogProcessingResult(
            pulse_center=expected_pulse_center,
            pulse_duration=expected_pulse_duration,
            pulse_reference_level_high=expected_pulse_reference_level_high,
            pulse_reference_level_middle=expected_pulse_reference_level_middle,
            pulse_reference_level_low=expected_pulse_reference_level_low,
            period=expected_period,
            duty_cycle=expected_duty_cycle,
        )

        logging.debug(
            "%s = %s",
            nameof(pulse_analog_processing_results_1),
            repr(pulse_analog_processing_results_1),
        )

        logging.debug(
            "%s = %s",
            nameof(pulse_analog_processing_results_2),
            repr(pulse_analog_processing_results_2),
        )

        # Assert results 1
        self.assertIsNotNone(pulse_analog_processing_results_1)
        self.assertEqual(
            first=expected_pulse_center,
            second=pulse_analog_processing_results_1.pulse_center,
        )

        self.assertEqual(
            first=expected_pulse_duration,
            second=pulse_analog_processing_results_1.pulse_duration,
        )

        self.assertEqual(
            first=expected_pulse_reference_level_high,
            second=pulse_analog_processing_results_1.pulse_reference_level_high,
        )

        self.assertEqual(
            first=expected_pulse_reference_level_middle,
            second=pulse_analog_processing_results_1.pulse_reference_level_middle,
        )

        self.assertEqual(
            first=expected_pulse_reference_level_low,
            second=pulse_analog_processing_results_1.pulse_reference_level_low,
        )

        self.assertIsNone(pulse_analog_processing_results_1.waveform_periodicity_processing_result)

        # Assert results 2
        self.assertIsNotNone(pulse_analog_processing_results_2)

        self.assertEqual(
            first=expected_pulse_center,
            second=pulse_analog_processing_results_2.pulse_center,
        )

        self.assertEqual(
            first=expected_pulse_duration,
            second=pulse_analog_processing_results_2.pulse_duration,
        )

        self.assertEqual(
            first=expected_pulse_reference_level_high,
            second=pulse_analog_processing_results_2.pulse_reference_level_high,
        )

        self.assertEqual(
            first=expected_pulse_reference_level_middle,
            second=pulse_analog_processing_results_2.pulse_reference_level_middle,
        )

        self.assertEqual(
            first=expected_pulse_reference_level_low,
            second=pulse_analog_processing_results_2.pulse_reference_level_low,
        )

        self.assertIsNotNone(
            pulse_analog_processing_results_2.waveform_periodicity_processing_result
        )

        self.assertEqual(
            first=expected_duty_cycle,
            second=pulse_analog_processing_results_2.waveform_periodicity_processing_result.duty_cycle,
        )

        self.assertEqual(
            first=expected_duty_cycle_percent,
            second=pulse_analog_processing_results_2.waveform_periodicity_processing_result.duty_cycle_percent,
        )

        self.assertEqual(
            first=expected_period,
            second=pulse_analog_processing_results_2.waveform_periodicity_processing_result.period,
        )

        self.assertEqual(
            first=expected_frequency,
            second=pulse_analog_processing_results_2.waveform_periodicity_processing_result.frequency,
        )

    def test_pulse_analog_processing_result_invalid_inputs(self):
        """Test of `pcbatt_analysis.pulse_analog_analysis.PulseAnalogProcessingResult`
        class constructor"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (398 > 100 characters) (auto-generated noqa)

        # Arrange + Act
        self.assertRaises(
            ValueError,
            lambda: PulseAnalogProcessingResult(
                pulse_center=-1,
                pulse_duration=0,
                pulse_reference_level_high=0,
                pulse_reference_level_middle=0,
                pulse_reference_level_low=0,
                period=0,
                duty_cycle=1,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: PulseAnalogProcessingResult(
                pulse_center=-1,
                pulse_duration=0,
                pulse_reference_level_high=0,
                pulse_reference_level_middle=0,
                pulse_reference_level_low=0,
                period=1,
                duty_cycle=-0.4,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: PulseAnalogProcessingResult(
                pulse_center=-1,
                pulse_duration=0,
                pulse_reference_level_high=0,
                pulse_reference_level_middle=0,
                pulse_reference_level_low=0,
                period=-1,
                duty_cycle=1,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: PulseAnalogProcessingResult(
                pulse_center=-1,
                pulse_duration=-1,
                pulse_reference_level_high=0,
                pulse_reference_level_middle=0,
                pulse_reference_level_low=0,
                period=1,
                duty_cycle=1,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: PulseAnalogProcessingResult(
                pulse_center=-1,
                pulse_duration=0,
                pulse_reference_level_high=0,
                pulse_reference_level_middle=0,
                pulse_reference_level_low=0,
                period=1,
                duty_cycle=-0.5,
            ),
        )


# LabVIEW VI tests
class TestLabViewPulseAnalogMeasurements(unittest.TestCase):
    """Provides unit tests of
    `pcbatt_analysis.pulse_analog_analysis.LabViewPulseAnalogMeasurements` class.

    Args:
        unittest (TestCase): test cases fixture.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        # active debug traces of native dll
        analysis_library_info.enable_traces(True)

    def tearDown(self):
        # active debug traces of native dll
        analysis_library_info.enable_traces(False)

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

        used_numpy_version = importlib.metadata.version(nameof(numpy))
        logging.debug("%s = %s", nameof(used_numpy_version), used_numpy_version)

        used_scipy_version = importlib.metadata.version(nameof(scipy))
        logging.debug("%s = %s", nameof(used_scipy_version), used_scipy_version)

        # active debug traces of native dll
        analysis_library_info.enable_traces(True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")
        # active debug traces of native dll
        analysis_library_info.enable_traces(False)

    @functional_utilities.repeat(10)
    def test_get_last_error_message_returns_empty_string(self):
        """Test of ``pcbatt_analysis.pulse_analog_analysis.LabViewPulseAnalogMeasurements
        get_last_error_message`` method when there is no error"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (358 > 100 characters) (auto-generated noqa)
        last_error_message = LabViewPulseAnalogMeasurements.get_last_error_message()
        self.assertEqual("", last_error_message)

    @functional_utilities.repeat(2)
    def test_process_single_waveform_multiple_pulse_measurements_export_all_relative_percent_reference_levels(
        self,
    ):
        """Test of
        `LabViewPulseAnalogMeasurements.process_single_waveform_multiple_pulse_measurements` method.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        tolerance_percent = 1
        expected_pulse_duration = 0.5
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent.parent

        logging.debug("%s = %s", nameof(repository_dir_path), repository_dir_path)

        csv_file_path = os.path.join(
            repository_dir_path, "pcbatt.testdata", "Ideal_Square_Waveforme.csv"
        )
        logging.debug("%s = %s", nameof(csv_file_path), csv_file_path)

        waveform_2d_array = csv_utilities.import_from_csv_file_2d_array(
            csv_file_path=csv_file_path, header_is_present=False
        )

        waveform_samples = waveform_2d_array[1]
        waveform_dates = waveform_2d_array[0]

        waveform_sampling_rate = 1000
        waveform_sampling_period = numeric_utilities.invert_value(waveform_sampling_rate)
        waveform_t0 = waveform_dates[0]

        logging.debug("%s = %s", nameof(waveform_sampling_rate), waveform_sampling_rate)

        logging.debug(
            "%s = %s",
            nameof(waveform_sampling_period),
            waveform_sampling_period,
        )

        logging.debug("%s = %s", nameof(waveform_t0), waveform_t0)
        logging.debug("%s = %s", nameof(waveform_samples), waveform_samples)

        processing_polarities = [
            PulseAnalogProcessingPolarity.HIGH,
            PulseAnalogProcessingPolarity.LOW,
        ]

        for processing_polarity in processing_polarities:
            multiple_pulse_measurements_result = LabViewPulseAnalogMeasurements.process_single_waveform_multiple_pulse_measurements(
                waveform_samples=waveform_samples,
                waveform_sampling_period_seconds=waveform_sampling_period,
                waveform_t0=waveform_t0,
                export_mode=PulseAnalogProcessingExportMode.ALL,
                processing_polarity=processing_polarity,
                reference_levels_unit=PulseAnalogProcessingReferenceLevelsUnit.RELATIVE_PERCENT,
                reference_levels=PulseAnalogProcessingReferenceLevels(
                    reference_level_high=95,
                    reference_level_middle=50,
                    reference_level_low=5,
                ),
                percent_levels_settings=PulseAnalogMeasurementPercentLevelsSettings(
                    amplitude_and_levels_processing_method=AmplitudeAndLevelsProcessingMethod.AUTO_SELECT,
                    histogram_size=512,
                ),
            )

            self.assertIsNotNone(multiple_pulse_measurements_result)

            for pulse_measurement_result in multiple_pulse_measurements_result:
                logging.debug(
                    "%s = %s",
                    nameof(pulse_measurement_result),
                    repr(pulse_measurement_result),
                )

                self.assertIsNotNone(
                    pulse_measurement_result.waveform_periodicity_processing_result
                )

                self.assertAlmostEqual(
                    first=expected_pulse_duration,
                    second=pulse_measurement_result.pulse_duration,
                    delta=numeric_utilities.percent_of(tolerance_percent, expected_pulse_duration),
                )

                self.assertLess(a=0, b=pulse_measurement_result.pulse_center)

                self.assertAlmostEqual(
                    first=1.0,
                    second=pulse_measurement_result.waveform_periodicity_processing_result.period,
                    delta=numeric_utilities.percent_of(tolerance_percent, 1.0),
                )

                self.assertAlmostEqual(
                    first=1.0,
                    second=pulse_measurement_result.waveform_periodicity_processing_result.frequency,
                    delta=numeric_utilities.percent_of(tolerance_percent, 1.0),
                )

                self.assertAlmostEqual(
                    first=0.5,
                    second=pulse_measurement_result.waveform_periodicity_processing_result.duty_cycle,
                    delta=numeric_utilities.percent_of(tolerance_percent, 0.5),
                )

    @functional_utilities.repeat(2)
    def test_process_single_waveform_pulse_measurements_export_all_relative_percent_reference_levels(
        self,
    ):
        """Test of
        `LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements` method.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        tolerance_percent = 1
        expected_pulse_centers_per_polarity = {
            PulseAnalogProcessingPolarity.HIGH: 1.25,
            PulseAnalogProcessingPolarity.LOW: 0.75,
        }
        expected_pulse_duration = 0.5
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent.parent

        logging.debug("%s = %s", nameof(repository_dir_path), repository_dir_path)

        csv_file_path = os.path.join(
            repository_dir_path, "pcbatt.testdata", "Ideal_Square_Waveforme.csv"
        )
        logging.debug("%s = %s", nameof(csv_file_path), csv_file_path)

        waveform_2d_array = csv_utilities.import_from_csv_file_2d_array(
            csv_file_path=csv_file_path, header_is_present=False
        )

        waveform_samples = waveform_2d_array[1]
        waveform_dates = waveform_2d_array[0]

        waveform_sampling_rate = 1000
        waveform_sampling_period = numeric_utilities.invert_value(waveform_sampling_rate)
        waveform_t0 = waveform_dates[0]

        logging.debug("%s = %s", nameof(waveform_sampling_rate), waveform_sampling_rate)

        logging.debug(
            "%s = %s",
            nameof(waveform_sampling_period),
            waveform_sampling_period,
        )

        logging.debug("%s = %s", nameof(waveform_t0), waveform_t0)
        logging.debug("%s = %s", nameof(waveform_samples), waveform_samples)

        processing_polarities = [
            PulseAnalogProcessingPolarity.HIGH,
            PulseAnalogProcessingPolarity.LOW,
        ]

        for processing_polarity in processing_polarities:
            pulse_measurements_result = LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements(
                waveform_samples=waveform_samples,
                waveform_sampling_period_seconds=waveform_sampling_period,
                waveform_t0=waveform_t0,
                export_mode=PulseAnalogProcessingExportMode.ALL,
                processing_polarity=processing_polarity,
                pulse_number=1,
                reference_levels_unit=PulseAnalogProcessingReferenceLevelsUnit.RELATIVE_PERCENT,
                reference_levels=PulseAnalogProcessingReferenceLevels(
                    reference_level_high=95,
                    reference_level_middle=50,
                    reference_level_low=5,
                ),
                percent_levels_settings=PulseAnalogMeasurementPercentLevelsSettings(
                    amplitude_and_levels_processing_method=AmplitudeAndLevelsProcessingMethod.AUTO_SELECT,
                    histogram_size=512,
                ),
            )
            logging.debug(
                "%s = %s",
                nameof(pulse_measurements_result),
                repr(pulse_measurements_result),
            )

            self.assertIsNotNone(pulse_measurements_result)
            self.assertIsNotNone(pulse_measurements_result.waveform_periodicity_processing_result)

            self.assertAlmostEqual(
                first=expected_pulse_duration,
                second=pulse_measurements_result.pulse_duration,
                delta=numeric_utilities.percent_of(tolerance_percent, expected_pulse_duration),
            )

            self.assertAlmostEqual(
                first=expected_pulse_centers_per_polarity[processing_polarity],
                second=pulse_measurements_result.pulse_center,
                delta=numeric_utilities.percent_of(
                    tolerance_percent,
                    expected_pulse_centers_per_polarity[processing_polarity],
                ),
            )

            self.assertAlmostEqual(
                first=1.0,
                second=pulse_measurements_result.waveform_periodicity_processing_result.period,
                delta=numeric_utilities.percent_of(tolerance_percent, 1.0),
            )

            self.assertAlmostEqual(
                first=1.0,
                second=pulse_measurements_result.waveform_periodicity_processing_result.frequency,
                delta=numeric_utilities.percent_of(tolerance_percent, 1.0),
            )

            self.assertAlmostEqual(
                first=0.5,
                second=pulse_measurements_result.waveform_periodicity_processing_result.duty_cycle,
                delta=numeric_utilities.percent_of(tolerance_percent, 0.5),
            )

    @functional_utilities.repeat(2)
    def test_process_single_waveform_pulse_measurements_ignore_periodicity_analysis_relative_percent_reference_levels(
        self,
    ):
        """Test of
        `LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements` method.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        tolerance_percent = 1
        expected_pulse_centers_per_polarity = {
            PulseAnalogProcessingPolarity.HIGH: 1.25,
            PulseAnalogProcessingPolarity.LOW: 0.75,
        }
        expected_pulse_duration = 0.5
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent.parent

        logging.debug("%s = %s", nameof(repository_dir_path), repository_dir_path)

        csv_file_path = os.path.join(
            repository_dir_path, "pcbatt.testdata", "Ideal_Square_Waveforme.csv"
        )
        logging.debug("%s = %s", nameof(csv_file_path), csv_file_path)

        waveform_2d_array = csv_utilities.import_from_csv_file_2d_array(
            csv_file_path=csv_file_path, header_is_present=False
        )

        waveform_samples = waveform_2d_array[1]
        waveform_dates = waveform_2d_array[0]

        waveform_sampling_rate = 1000
        waveform_sampling_period = numeric_utilities.invert_value(waveform_sampling_rate)
        waveform_t0 = waveform_dates[0]

        logging.debug("%s = %s", nameof(waveform_sampling_rate), waveform_sampling_rate)

        logging.debug(
            "%s = %s",
            nameof(waveform_sampling_period),
            waveform_sampling_period,
        )

        logging.debug("%s = %s", nameof(waveform_t0), waveform_t0)
        logging.debug("%s = %s", nameof(waveform_samples), waveform_samples)

        processing_polarities = [
            PulseAnalogProcessingPolarity.HIGH,
            PulseAnalogProcessingPolarity.LOW,
        ]

        for processing_polarity in processing_polarities:
            pulse_measurements_result = LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements(
                waveform_samples=waveform_samples,
                waveform_sampling_period_seconds=waveform_sampling_period,
                waveform_t0=waveform_t0,
                export_mode=PulseAnalogProcessingExportMode.IGNORE_WAVEFORM_PERIODICITY_ANALYSIS,
                processing_polarity=processing_polarity,
                pulse_number=1,
                reference_levels_unit=PulseAnalogProcessingReferenceLevelsUnit.RELATIVE_PERCENT,
                reference_levels=PulseAnalogProcessingReferenceLevels(
                    reference_level_high=95,
                    reference_level_middle=50,
                    reference_level_low=5,
                ),
                percent_levels_settings=PulseAnalogMeasurementPercentLevelsSettings(
                    amplitude_and_levels_processing_method=AmplitudeAndLevelsProcessingMethod.AUTO_SELECT,
                    histogram_size=512,
                ),
            )
            logging.debug(
                "%s = %s",
                nameof(pulse_measurements_result),
                repr(pulse_measurements_result),
            )

            self.assertIsNotNone(pulse_measurements_result)
            self.assertIsNone(pulse_measurements_result.waveform_periodicity_processing_result)

            self.assertAlmostEqual(
                first=expected_pulse_duration,
                second=pulse_measurements_result.pulse_duration,
                delta=numeric_utilities.percent_of(tolerance_percent, expected_pulse_duration),
            )

            self.assertAlmostEqual(
                first=expected_pulse_centers_per_polarity[processing_polarity],
                second=pulse_measurements_result.pulse_center,
                delta=numeric_utilities.percent_of(
                    tolerance_percent,
                    expected_pulse_centers_per_polarity[processing_polarity],
                ),
            )

    @functional_utilities.repeat(2)
    def test_process_single_waveform_pulse_measurements_ignore_periodicity_analysis_absolute_reference_levels(
        self,
    ):
        """Test of
        `LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements` method.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # Arrange
        tolerance_percent = 1
        expected_pulse_centers_per_polarity = {
            PulseAnalogProcessingPolarity.HIGH: 1.25,
            PulseAnalogProcessingPolarity.LOW: 0.75,
        }
        expected_pulse_duration = 0.5
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent.parent

        logging.debug("%s = %s", nameof(repository_dir_path), repository_dir_path)

        csv_file_path = os.path.join(
            repository_dir_path, "pcbatt.testdata", "Ideal_Square_Waveforme.csv"
        )
        logging.debug("%s = %s", nameof(csv_file_path), csv_file_path)

        waveform_2d_array = csv_utilities.import_from_csv_file_2d_array(
            csv_file_path=csv_file_path, header_is_present=False
        )

        waveform_samples = waveform_2d_array[1]
        waveform_dates = waveform_2d_array[0]

        waveform_sampling_rate = 1000
        waveform_sampling_period = numeric_utilities.invert_value(waveform_sampling_rate)
        waveform_t0 = waveform_dates[0]

        logging.debug("%s = %s", nameof(waveform_sampling_rate), waveform_sampling_rate)

        logging.debug(
            "%s = %s",
            nameof(waveform_sampling_period),
            waveform_sampling_period,
        )

        logging.debug("%s = %s", nameof(waveform_t0), waveform_t0)
        logging.debug("%s = %s", nameof(waveform_samples), waveform_samples)

        processing_polarities = [
            PulseAnalogProcessingPolarity.HIGH,
            PulseAnalogProcessingPolarity.LOW,
        ]

        for processing_polarity in processing_polarities:
            pulse_measurements_result = LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements(
                waveform_samples=waveform_samples,
                waveform_sampling_period_seconds=waveform_sampling_period,
                waveform_t0=waveform_t0,
                export_mode=PulseAnalogProcessingExportMode.IGNORE_WAVEFORM_PERIODICITY_ANALYSIS,
                processing_polarity=processing_polarity,
                pulse_number=1,
                reference_levels_unit=PulseAnalogProcessingReferenceLevelsUnit.ABSOLUTE,
                reference_levels=PulseAnalogProcessingReferenceLevels(
                    reference_level_high=0.45,
                    reference_level_middle=0.25,
                    reference_level_low=0.05,
                ),
                percent_levels_settings=None,
            )
            logging.debug(
                "%s = %s",
                nameof(pulse_measurements_result),
                repr(pulse_measurements_result),
            )

            self.assertIsNotNone(pulse_measurements_result)
            self.assertIsNone(pulse_measurements_result.waveform_periodicity_processing_result)

            self.assertAlmostEqual(
                first=expected_pulse_duration,
                second=pulse_measurements_result.pulse_duration,
                delta=numeric_utilities.percent_of(tolerance_percent, expected_pulse_duration),
            )

            self.assertAlmostEqual(
                first=expected_pulse_centers_per_polarity[processing_polarity],
                second=pulse_measurements_result.pulse_center,
                delta=numeric_utilities.percent_of(
                    tolerance_percent,
                    expected_pulse_centers_per_polarity[processing_polarity],
                ),
            )

    @functional_utilities.repeat(2)
    def test_process_single_waveform_pulse_measurements_export_all_absolute_reference_levels(
        self,
    ):
        """Test of
        `LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements` method.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # Arrange
        tolerance_percent = 1
        expected_pulse_centers_per_polarity = {
            PulseAnalogProcessingPolarity.HIGH: 1.25,
            PulseAnalogProcessingPolarity.LOW: 0.75,
        }
        expected_pulse_duration = 0.5
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent.parent

        logging.debug("%s = %s", nameof(repository_dir_path), repository_dir_path)

        csv_file_path = os.path.join(
            repository_dir_path, "pcbatt.testdata", "Ideal_Square_Waveforme.csv"
        )
        logging.debug("%s = %s", nameof(csv_file_path), csv_file_path)

        waveform_2d_array = csv_utilities.import_from_csv_file_2d_array(
            csv_file_path=csv_file_path, header_is_present=False
        )

        waveform_samples = waveform_2d_array[1]
        waveform_dates = waveform_2d_array[0]

        waveform_sampling_rate = 1000
        waveform_sampling_period = numeric_utilities.invert_value(waveform_sampling_rate)
        waveform_t0 = waveform_dates[0]

        logging.debug("%s = %s", nameof(waveform_sampling_rate), waveform_sampling_rate)

        logging.debug(
            "%s = %s",
            nameof(waveform_sampling_period),
            waveform_sampling_period,
        )

        logging.debug("%s = %s", nameof(waveform_t0), waveform_t0)
        logging.debug("%s = %s", nameof(waveform_samples), waveform_samples)

        processing_polarities = [
            PulseAnalogProcessingPolarity.HIGH,
            PulseAnalogProcessingPolarity.LOW,
        ]

        for processing_polarity in processing_polarities:
            pulse_measurements_result = (
                LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements(
                    waveform_samples=waveform_samples,
                    waveform_sampling_period_seconds=waveform_sampling_period,
                    waveform_t0=waveform_t0,
                    export_mode=PulseAnalogProcessingExportMode.ALL,
                    processing_polarity=processing_polarity,
                    pulse_number=1,
                    reference_levels_unit=PulseAnalogProcessingReferenceLevelsUnit.ABSOLUTE,
                    reference_levels=PulseAnalogProcessingReferenceLevels(
                        reference_level_high=0.45,
                        reference_level_middle=0.25,
                        reference_level_low=0.05,
                    ),
                    percent_levels_settings=None,
                )
            )
            logging.debug(
                "%s = %s",
                nameof(pulse_measurements_result),
                repr(pulse_measurements_result),
            )

            self.assertIsNotNone(pulse_measurements_result)
            self.assertIsNotNone(pulse_measurements_result.waveform_periodicity_processing_result)

            self.assertAlmostEqual(
                first=expected_pulse_duration,
                second=pulse_measurements_result.pulse_duration,
                delta=numeric_utilities.percent_of(tolerance_percent, expected_pulse_duration),
            )

            self.assertAlmostEqual(
                first=expected_pulse_centers_per_polarity[processing_polarity],
                second=pulse_measurements_result.pulse_center,
                delta=numeric_utilities.percent_of(
                    tolerance_percent,
                    expected_pulse_centers_per_polarity[processing_polarity],
                ),
            )

            self.assertAlmostEqual(
                first=1.0,
                second=pulse_measurements_result.waveform_periodicity_processing_result.period,
                delta=numeric_utilities.percent_of(tolerance_percent, 1.0),
            )

            self.assertAlmostEqual(
                first=1.0,
                second=pulse_measurements_result.waveform_periodicity_processing_result.frequency,
                delta=numeric_utilities.percent_of(tolerance_percent, 1.0),
            )

            self.assertAlmostEqual(
                first=0.5,
                second=pulse_measurements_result.waveform_periodicity_processing_result.duty_cycle,
                delta=numeric_utilities.percent_of(tolerance_percent, 0.5),
            )

        self.assertAlmostEqual(
            first=50,
            second=pulse_measurements_result.waveform_periodicity_processing_result.duty_cycle_percent,
            delta=numeric_utilities.percent_of(tolerance_percent, 50),
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--repeat", dest="repeat", help="repeat tests")
    (args, unitargs) = parser.parse_known_args()
    unitargs.insert(0, "placeholder")  # unittest ignores first arg

    # add more arguments to unitargs here
    repeat_count = int(vars(args)["repeat"] or 2)
    for iteration in range(repeat_count):
        was_successful = unittest.main(exit=False, argv=unitargs).result.wasSuccessful()
        if not was_successful:
            sys.exit(1)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_creation/__init__.py sha256=9fefd9a4b825d588c8c0fb84a411adff7b9e29301818d8e0739176b04f655771 bytes=456 -->
## FILE: tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_creation/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_creation/__init__.py`
- sha256: `9fefd9a4b825d588c8c0fb84a411adff7b9e29301818d8e0739176b04f655771`
- bytes: 456

````python
"""Provides a set of unit tests for 
nipcbatt.pcbatt_analysis.waveform_creation package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (346 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_creation/test_multitones_waveform.py sha256=3d84d489d48600e08d34e507201f4f56c4d57da336d6609db82ce770bd80bda5 bytes=7562 -->
## FILE: tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_creation/test_multitones_waveform.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_creation/test_multitones_waveform.py`
- sha256: `3d84d489d48600e08d34e507201f4f56c4d57da336d6609db82ce770bd80bda5`
- bytes: 7562

````python
"""Provides unit tests related to multitones_waveform.py module"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (177 > 100 characters) (auto-generated noqa)

import logging
import os
import platform
import sys
import unittest
from pathlib import Path

from varname import nameof

from nipcbatt.pcbatt_analysis.waveform_creation import multitones_waveform
from nipcbatt.pcbatt_utilities import csv_utilities, numeric_utilities


class TestMultitonesWaveform(unittest.TestCase):
    """Defines a test fixture that checks creation functions of module
    `multitones_waveform`.

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

        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent
        cls.tests_output_folder_path = os.path.join(
            repository_dir_path,
            "tests_outputs",
            Path(__file__).stem,
            nameof(TestMultitonesWaveform),
        )

        if not os.path.exists(cls.tests_output_folder_path):
            os.makedirs(cls.tests_output_folder_path, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_create_multitones_waveform_single_tone(
        self,
    ):
        """Test of `multitones_waveform.create_multitones_waveform` function"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (267 > 100 characters) (auto-generated noqa)

        # Arrange
        single_tone_frequency = 440
        single_tone_amplitude = 1
        single_tone_phase = 0
        single_tone_sampling_rate = 44100
        single_tone_duration_seconds = 0.2
        single_tone_samples_count = (int)(single_tone_duration_seconds * single_tone_sampling_rate)
        tolerance_percent = 0.5

        # Act
        single_tone_samples = multitones_waveform.create_multitones_waveform(
            multitones_amplitude=1,
            waveform_tones=[
                multitones_waveform.WaveformTone(
                    frequency=single_tone_frequency,
                    amplitude=single_tone_amplitude,
                    phase_radians=single_tone_phase,
                )
            ],
            samples_count=single_tone_samples_count,
            sampling_rate=single_tone_sampling_rate,
        )

        single_tone_samples_max = single_tone_samples.max()
        single_tone_samples_min = single_tone_samples.min()

        csv_file_ouput_path = os.path.join(
            TestMultitonesWaveform.tests_output_folder_path,
            "test_create_multitones_waveform_single_tone.csv",
        )

        csv_utilities.export_signal_to_csv_file(
            signal_csv_file_path=csv_file_ouput_path,
            signal_samples=single_tone_samples,
            signal_sampling_rate=single_tone_sampling_rate,
            x_axis_name="Time (s)",
            y_axis_name="Amplitude (V)",
        )

        # Assert
        self.assertEqual(first=single_tone_samples_count, second=single_tone_samples.size)
        self.assertAlmostEqual(
            first=single_tone_amplitude,
            second=single_tone_samples_max,
            delta=numeric_utilities.percent_of(tolerance_percent, single_tone_amplitude),
        )
        self.assertAlmostEqual(
            first=-single_tone_amplitude,
            second=single_tone_samples_min,
            delta=numeric_utilities.percent_of(tolerance_percent, single_tone_amplitude),
        )

    def test_create_multitones_waveform_multiple_harmonics(
        self,
    ):
        """Test of `multitones_waveform.create_multitones_waveform` function"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (267 > 100 characters) (auto-generated noqa)

        # Arrange
        fundamental_tone_frequency = 440
        fundamental_tone_amplitude = 1
        fundamental_tone_phase = 0
        multiple_tones_amplitude = 1
        tones_sampling_rate = 44100
        tones_duration_seconds = 0.2
        tones_samples_count = (int)(tones_duration_seconds * tones_sampling_rate)
        tolerance_percent = 0.5

        # Act
        multiple_tones_samples = multitones_waveform.create_multitones_waveform(
            multitones_amplitude=multiple_tones_amplitude,
            waveform_tones=[
                multitones_waveform.WaveformTone(
                    frequency=fundamental_tone_frequency,
                    amplitude=fundamental_tone_amplitude,
                    phase_radians=fundamental_tone_phase,
                ),
                multitones_waveform.WaveformTone(
                    frequency=2 * fundamental_tone_frequency,
                    amplitude=0.5 * fundamental_tone_amplitude,
                    phase_radians=fundamental_tone_phase,
                ),
                multitones_waveform.WaveformTone(
                    frequency=3 * fundamental_tone_frequency,
                    amplitude=0.25 * fundamental_tone_amplitude,
                    phase_radians=fundamental_tone_phase,
                ),
            ],
            samples_count=tones_samples_count,
            sampling_rate=tones_sampling_rate,
        )

        multiple_tones_samples_max = multiple_tones_samples.max()
        multiple_tones_samples_min = multiple_tones_samples.min()

        csv_file_ouput_path = os.path.join(
            TestMultitonesWaveform.tests_output_folder_path,
            "test_create_multitones_waveform_multiple_harmonics.csv",
        )

        csv_utilities.export_signal_to_csv_file(
            signal_csv_file_path=csv_file_ouput_path,
            signal_samples=multiple_tones_samples,
            signal_sampling_rate=tones_sampling_rate,
            x_axis_name="Time (s)",
            y_axis_name="Amplitude (V)",
        )

        # Assert
        self.assertEqual(first=tones_samples_count, second=multiple_tones_samples.size)

        self.assertAlmostEqual(
            first=multiple_tones_amplitude,
            second=multiple_tones_samples_max,
            delta=numeric_utilities.percent_of(tolerance_percent, multiple_tones_amplitude),
        )
        self.assertAlmostEqual(
            first=-multiple_tones_amplitude,
            second=multiple_tones_samples_min,
            delta=numeric_utilities.percent_of(tolerance_percent, multiple_tones_amplitude),
        )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_creation/test_sine_waveform.py sha256=70bb6e2b1a7f76f913566e0d4ef696556a0165e10fd80f79df6999b3deb79d39 bytes=6097 -->
## FILE: tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_creation/test_sine_waveform.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_creation/test_sine_waveform.py`
- sha256: `70bb6e2b1a7f76f913566e0d4ef696556a0165e10fd80f79df6999b3deb79d39`
- bytes: 6097

````python
"""Provides unit tests related to sine_waveform.py module"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)

import logging
import os
import platform
import sys
import unittest
from pathlib import Path

from parameterized import parameterized
from varname import nameof

from nipcbatt.pcbatt_analysis.waveform_creation import sine_waveform
from nipcbatt.pcbatt_utilities import csv_utilities


class TestSineWaveform(unittest.TestCase):
    """Defines a test fixture that checks creation functions of module
    `sine_waveform`.

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

        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent
        cls.tests_output_folder_path = os.path.join(
            repository_dir_path,
            "tests_outputs",
            Path(__file__).stem,
            nameof(TestSineWaveform),
        )

        if not os.path.exists(cls.tests_output_folder_path):
            os.makedirs(cls.tests_output_folder_path, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    @parameterized.expand(
        [
            ("60_Hz_Phase=0", 1, 60, 0, 0, 6000, 1),
            ("60_Hz_Phase=0.5_PI", 1, 60, 1.5707963, 0, 6000, 1),
            ("60_Hz_Phase=1.0_PI", 1, 60, 3.1415927, 0, 6000, 1),
            ("60_Hz_Phase=1.0_PI_Offset=1.0", 1, 60, 3.1415927, 1, 6000, 1),
        ]
    )
    def test_create_cosine_waveform(
        self,
        case_name: str,
        expected_amplitude: float,
        expected_frequency: float,
        expected_phase: float,
        expected_offset: float,
        expected_sampling_rate: float,
        expected_waveform_duration_seconds: float,
    ):
        """Test of `sin_waveform.create_cosine_waveform` function"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (256 > 100 characters) (auto-generated noqa)

        logging.debug("%s = %s", nameof(case_name), case_name)

        # Arrange
        expected_samples_count = expected_waveform_duration_seconds * expected_sampling_rate

        # Act
        waveform_samples = sine_waveform.create_cosine_waveform(
            amplitude=expected_amplitude,
            frequency=expected_frequency,
            phase=expected_phase,
            offset=expected_offset,
            samples_count=expected_samples_count,
            sampling_rate=expected_sampling_rate,
        )

        csv_file_ouput_path = os.path.join(
            TestSineWaveform.tests_output_folder_path,
            f"test_create_cosine_waveform_{case_name}.csv",
        )

        csv_utilities.export_signal_to_csv_file(
            signal_csv_file_path=csv_file_ouput_path,
            signal_samples=waveform_samples,
            signal_sampling_rate=expected_sampling_rate,
            x_axis_name="Time (s)",
            y_axis_name="Amplitude (V)",
        )

        # Assert
        self.assertEqual(first=expected_samples_count, second=waveform_samples.size)

    @parameterized.expand(
        [
            ("60_Hz_Phase=0", 1, 60, 0, 0, 6000, 1),
            ("60_Hz_Phase=0.5_PI", 1, 60, 1.5707963, 0, 6000, 1),
            ("60_Hz_Phase=1.0_PI", 1, 60, 3.1415927, 0, 6000, 1),
            ("60_Hz_Phase=1.0_PI_Offset=1.0", 1, 60, 3.1415927, 1, 6000, 1),
        ]
    )
    def test_create_sine_waveform(
        self,
        case_name: str,
        expected_amplitude: float,
        expected_frequency: float,
        expected_phase: float,
        expected_offset: float,
        expected_sampling_rate: float,
        expected_waveform_duration_seconds: float,
    ):
        """Test of `sin_waveform.create_sine_waveform` function"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (177 > 100 characters) (auto-generated noqa)
        logging.debug("%s = %s", nameof(case_name), case_name)

        # Arrange
        expected_samples_count = expected_waveform_duration_seconds * expected_sampling_rate

        # Act
        waveform_samples = sine_waveform.create_sine_waveform(
            amplitude=expected_amplitude,
            frequency=expected_frequency,
            phase=expected_phase,
            offset=expected_offset,
            samples_count=expected_samples_count,
            sampling_rate=expected_sampling_rate,
        )

        csv_file_ouput_path = os.path.join(
            TestSineWaveform.tests_output_folder_path,
            f"test_create_sine_waveform_{case_name}.csv",
        )

        csv_utilities.export_signal_to_csv_file(
            signal_csv_file_path=csv_file_ouput_path,
            signal_samples=waveform_samples,
            signal_sampling_rate=expected_sampling_rate,
            x_axis_name="Time (s)",
            y_axis_name="Amplitude (V)",
        )

        # Assert
        self.assertEqual(first=expected_samples_count, second=waveform_samples.size)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_creation/test_square_waveform.py sha256=207fdfec01b696506b8c9f18562d9a5e7453cc94b0a3a6f2344a95b289911d39 bytes=6697 -->
## FILE: tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_creation/test_square_waveform.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_creation/test_square_waveform.py`
- sha256: `207fdfec01b696506b8c9f18562d9a5e7453cc94b0a3a6f2344a95b289911d39`
- bytes: 6697

````python
"""Provides unit tests related to square_waveform.py module"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

import logging
import os
import platform
import sys
import unittest
from pathlib import Path

import numpy
from parameterized import parameterized
from varname import nameof

from nipcbatt.pcbatt_analysis.waveform_creation import square_waveform
from nipcbatt.pcbatt_utilities import csv_utilities


class TestSquareWaveform(unittest.TestCase):
    """Defines a test fixture that checks creation functions of module
    `square_waveform`.

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

        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent
        cls.tests_output_folder_path = os.path.join(
            repository_dir_path,
            "tests_outputs",
            Path(__file__).stem,
            nameof(TestSquareWaveform),
        )

        if not os.path.exists(cls.tests_output_folder_path):
            os.makedirs(cls.tests_output_folder_path, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    @parameterized.expand(
        [
            (
                "60_Hz_Duty=0.00_Offset=1.00_Phase=0.0_PI",  # case_name
                1,  # expected_amplitude
                60,  # expected_frequency
                0.0,  # expected_duty_cycle
                0,  # expected_phase
                1,  # expected_offset
                6000,  # expected_sampling_rate
                2,  # expected_waveform_duration_seconds
                0,  # expected_waveform_max
                0,  # expected_waveform_max
            ),
            ("60_Hz_Duty=0.25_Phase=0.0_PI", 1, 60, 0.25, 0, 0, 6000, 2, +1, -1),
            ("60_Hz_Duty=0.50_Phase=0.0_PI", 1, 60, 0.50, 0, 0, 6000, 2, +1, -1),
            ("60_Hz_Duty=0.75_Phase=0.0_PI", 1, 60, 0.75, 0, 0, 6000, 2, +1, -1),
            (
                "60_Hz_Duty=1.00_Phase=0.0_PI",  # case_name
                1,  # expected_amplitude
                60,  # expected_frequency
                1.00,  # expected_duty_cycle
                0,  # expected_phase
                1,  # expected_offset
                6000,  # expected_sampling_rate
                2,  # expected_waveform_duration_seconds
                2,  # expected_waveform_max
                2,  # expected_waveform_max
            ),
            (
                "60_Hz_Duty=0.50_Offset=1.00_Amplitude=0.5",
                0.5,
                60,
                0.50,
                0,
                1.00,
                6000,
                2,
                +1.5,
                +0.5,
            ),
            (
                "60_Hz_Duty=0.50_Phase=1.0_PI",
                1,
                60,
                0.50,
                3.1415927,
                0,
                6000,
                2,
                +1,
                -1,
            ),
            (
                "60_Hz_Duty=0.50_Phase=2.0_PI",
                1,
                60,
                0.50,
                2 * 3.1415927,
                0,
                6000,
                2,
                +1,
                -1,
            ),
            (
                "60_Hz_Duty=0.50_Phase=0.5_PI",
                1,
                60,
                0.50,
                0.5 * 3.1415927,
                0,
                6000,
                2,
                +1,
                -1,
            ),
        ]
    )
    def test_create_square_waveform(
        self,
        case_name: str,
        expected_amplitude: float,
        expected_frequency: float,
        expected_duty_cycle: float,
        expected_phase: float,
        expected_offset: float,
        expected_sampling_rate: float,
        expected_waveform_duration_seconds: float,
        expected_waveform_max: float,
        expected_waveform_min: float,
    ):
        """Test of `square_waveform.create_square_waveform` function"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (259 > 100 characters) (auto-generated noqa)

        logging.debug("%s = %s", nameof(case_name), case_name)

        # Arrange
        expected_samples_count = expected_waveform_duration_seconds * expected_sampling_rate

        # Act
        waveform_samples = square_waveform.create_square_waveform(
            amplitude=expected_amplitude,
            frequency=expected_frequency,
            duty_cycle=expected_duty_cycle,
            phase=expected_phase,
            offset=expected_offset,
            samples_count=expected_samples_count,
            sampling_rate=expected_sampling_rate,
        )

        actual_waveform_max = numpy.max(waveform_samples)
        actual_waveform_min = numpy.min(waveform_samples)

        csv_file_ouput_path = os.path.join(
            TestSquareWaveform.tests_output_folder_path,
            f"test_create_square_waveform{case_name}.csv",
        )

        csv_utilities.export_signal_to_csv_file(
            signal_csv_file_path=csv_file_ouput_path,
            signal_samples=waveform_samples,
            signal_sampling_rate=expected_sampling_rate,
            x_axis_name="Time (s)",
            y_axis_name="Amplitude (V)",
        )

        # Assert
        self.assertEqual(first=expected_samples_count, second=waveform_samples.size)
        self.assertEqual(first=expected_waveform_max, second=actual_waveform_max)
        self.assertEqual(first=expected_waveform_min, second=actual_waveform_min)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_transformation/__init__.py sha256=5c7a8615e313e45434dd9375b2b89965fc7a87c94cb67410da4f3485198a49cd bytes=462 -->
## FILE: tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_transformation/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_transformation/__init__.py`
- sha256: `5c7a8615e313e45434dd9375b2b89965fc7a87c94cb67410da4f3485198a49cd`
- bytes: 462

````python
"""Provides a set of unit tests for 
nipcbatt.pcbatt_analysis.waveform_transformation package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (352 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_transformation/test_scale_and_offset_waveform.py sha256=1b5a68259614f2bcbbaf604fd8c30a7474b6822d1a6f1eaa357e9e4b116a21d6 bytes=6722 -->
## FILE: tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_transformation/test_scale_and_offset_waveform.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_analysis_tests/waveform_transformation/test_scale_and_offset_waveform.py`
- sha256: `1b5a68259614f2bcbbaf604fd8c30a7474b6822d1a6f1eaa357e9e4b116a21d6`
- bytes: 6722

````python
"""Provides unit tests related to square_waveform.py module"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

import logging
import os
import platform
import sys
import unittest
from pathlib import Path

import numpy
from parameterized import parameterized
from varname import nameof

from nipcbatt.pcbatt_analysis.waveform_transformation import scale_and_offset_waveform


class TestScaleAndOffsetWaveform(unittest.TestCase):
    """Defines a test fixture that checks transformation functions of module
    `scale_and_offset_waveform`.

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

        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent
        cls.tests_output_folder_path = os.path.join(
            repository_dir_path,
            "tests_outputs",
            Path(__file__).stem,
            nameof(TestScaleAndOffsetWaveform),
        )

        if not os.path.exists(cls.tests_output_folder_path):
            os.makedirs(cls.tests_output_folder_path, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    @parameterized.expand(
        [
            (
                "ScaleFactor=1.00_Offset=0.00",  # case_name
                1,  # expected_scale_factor
                0,  # expected_offset
            ),
            (
                "ScaleFactor=2.00_Offset=0.00",  # case_name
                2,  # expected_scale_factor
                0,  # expected_offset
            ),
            (
                "ScaleFactor=0.05_Offset=0.00",  # case_name
                0.05,  # expected_scale_factor
                0,  # expected_offset
            ),
            (
                "ScaleFactor=2.00_Offset=1.00",  # case_name
                2,  # expected_scale_factor
                1,  # expected_offset
            ),
            (
                "ScaleFactor=2.00_Offset=-1.00",  # case_name
                2,  # expected_scale_factor
                -1,  # expected_offset
            ),
        ]
    )
    def test_scale_and_apply_offset_linear_function(
        self, case_name: str, expected_scale_factor: float, expected_offset: float
    ):
        """Test of `scale_and_offset_waveform.scale_and_apply_offset` function"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (269 > 100 characters) (auto-generated noqa)

        logging.debug("%s = %s", nameof(case_name), case_name)

        # Arrange
        input_waveform = numpy.array([1, 2, 3, 4], dtype=numpy.float64)

        # Act
        transformed_waveform = scale_and_offset_waveform.scale_and_apply_offset(
            waveform_samples=input_waveform,
            scale_factor=expected_scale_factor,
            offset=expected_offset,
        )
        # Assert
        self.assertEqual(first=input_waveform.size, second=transformed_waveform.size)
        self.assertNotEqual(first=id(input_waveform), second=id(transformed_waveform))

        for raw_sample, transformed_sample in zip(input_waveform, transformed_waveform):
            self.assertEqual(
                first=expected_scale_factor * raw_sample + expected_offset,
                second=transformed_sample,
            )

    @parameterized.expand(
        [
            (
                "ScaleFactor=1.00_Offset=0.00",  # case_name
                1,  # expected_scale_factor
                0,  # expected_offset
            ),
            (
                "ScaleFactor=2.00_Offset=0.00",  # case_name
                2,  # expected_scale_factor
                0,  # expected_offset
            ),
            (
                "ScaleFactor=0.05_Offset=0.00",  # case_name
                0.05,  # expected_scale_factor
                0,  # expected_offset
            ),
            (
                "ScaleFactor=2.00_Offset=1.00",  # case_name
                2,  # expected_scale_factor
                1,  # expected_offset
            ),
            (
                "ScaleFactor=2.00_Offset=-1.00",  # case_name
                2,  # expected_scale_factor
                -1,  # expected_offset
            ),
        ]
    )
    def test_scale_and_apply_offset_inplace_linear_function(
        self, case_name: str, expected_scale_factor: float, expected_offset: float
    ):
        """Test of `scale_and_offset_waveform.scale_and_apply_offset_inplace` function"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (277 > 100 characters) (auto-generated noqa)

        logging.debug("%s = %s", nameof(case_name), case_name)

        # Arrange
        input_waveform = numpy.array([1, 2, 3, 4], dtype=numpy.float64)
        input_waveform_copy = numpy.array([1, 2, 3, 4], dtype=numpy.float64)

        # Act
        transformed_waveform = scale_and_offset_waveform.scale_and_apply_offset_inplace(
            waveform_samples=input_waveform,
            scale_factor=expected_scale_factor,
            offset=expected_offset,
        )
        # Assert
        self.assertEqual(first=input_waveform_copy.size, second=transformed_waveform.size)
        self.assertEqual(first=id(input_waveform), second=id(transformed_waveform))

        for raw_sample, transformed_sample in zip(input_waveform_copy, transformed_waveform):
            self.assertEqual(
                first=expected_scale_factor * raw_sample + expected_offset,
                second=transformed_sample,
            )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_communication_library_tests/__init__.py sha256=9f3f5cc32401772389ce7f7bb6895f2b5e75292cd1f6a35c7e3f172028a9eaa2 bytes=87 -->
## FILE: tests/nipcbatt_tests/pcbatt_communication_library_tests/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_communication_library_tests/__init__.py`
- sha256: `9f3f5cc32401772389ce7f7bb6895f2b5e75292cd1f6a35c7e3f172028a9eaa2`
- bytes: 87

````python
"""Provides a set of unit tests for nipcbatt.pcbatt_communication_library package."""
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_communication_library_tests/_ni_845x_internal/__init__.py sha256=8b9f45d022282236a21942dab2a02963707b82620017097096d1e8366a4a6674 bytes=285 -->
## FILE: tests/nipcbatt_tests/pcbatt_communication_library_tests/_ni_845x_internal/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_communication_library_tests/_ni_845x_internal/__init__.py`
- sha256: `8b9f45d022282236a21942dab2a02963707b82620017097096d1e8366a4a6674`
- bytes: 285

````python
"""Provides a set of unit tests for nipcbatt.pcbatt_communication_library._ni_845x_internal package"""  # noqa: W505, D415 - doc line too long (102 > 100 characters) (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_communication_library_tests/_ni_845x_internal/test_ni_845x_functions.py sha256=c212f23cd80af988c3f9da6eb92c2a12cc06d9867c27d65f135eafef6dac0c5a bytes=22686 -->
## FILE: tests/nipcbatt_tests/pcbatt_communication_library_tests/_ni_845x_internal/test_ni_845x_functions.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_communication_library_tests/_ni_845x_internal/test_ni_845x_functions.py`
- sha256: `c212f23cd80af988c3f9da6eb92c2a12cc06d9867c27d65f135eafef6dac0c5a`
- bytes: 22686

````python
"""This module provides unit tests for functions defined in
nipcbatt.pcbatt_communication_library._ni_845x_internal._ni_845x_functions module."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (378 > 100 characters) (auto-generated noqa)

import importlib.metadata
import logging
import sys
import unittest
from random import random
from typing import List

from parameterized import parameterized
from varname import nameof

from nipcbatt.pcbatt_communication_library._ni_845x_internal import _ni_845x_functions
from nipcbatt.pcbatt_communication_library.ni_845x_data_types import (
    DataMemoryAddressEndianness,
    DataMemoryAddressType,
    Ni845xI2cAddressingType,
    SpiConfigurationClockPhase,
    SpiConfigurationClockPolarity,
)
from nipcbatt.pcbatt_communication_library.pcbatt_communication_exceptions import (
    PCBATTCommunicationException,
)
from nipcbatt.pcbatt_utilities.native_interop_utilities import check_dll_availability


def _is_ni_845x_installed():
    try:
        check_dll_availability("ni845x.dll")
        return True
    except FileNotFoundError:
        return False


class TestInvokeNi845xFunction(unittest.TestCase):
    """Defines a test fixture that checks
    `_invoke_ni_845x_function` function is ready to use.

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
    def test_invoke_ni_845x_function_fails_if_function_name(self, test_name, function_name):
        """unit test of _get_function_from_native_library."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)
        logging.debug("running test_invoke_ni_845x_function_fails_if_function_name_%s", test_name)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            _ni_845x_functions.invoke_ni_845x_function(
                function_name=function_name,
            )

        # Assert
        self.assertEqual(
            "The string value function_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_invoke_ni_845x_function_fails_if_function_name_does_not_exist(self):
        """unit test of _get_function_from_native_library."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(PCBATTCommunicationException) as ctx:
            _ni_845x_functions.invoke_ni_845x_function(
                function_name="ni845xFunctionNotExist",
            )

        # Assert
        self.assertEqual(
            "Failed to call function ni845xFunctionNotExist: 'ni845xFunctionNotExist'.",
            str(ctx.exception),
        )


class TestI2cConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    functions related to I2C configuration are ready to use.

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

    @unittest.skipIf(
        not _is_ni_845x_installed(),
        "The execution of test is skipped because Ni-845x driver is not installed.",
    )
    def test_ni_845x_i2c_configuration_open_should_not_fail(self):
        """unit test of ni_845x_i2c_configuration_open."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (156 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        configuration_handle = _ni_845x_functions.ni_845x_i2c_configuration_open_impl()
        _ni_845x_functions.ni_845x_i2c_configuration_close_impl(configuration_handle)

        # Assert
        self.assertNotEqual(
            first=0,
            second=configuration_handle,
        )

    @unittest.skipIf(
        not _is_ni_845x_installed(),
        "The execution of test is skipped because Ni-845x driver is not installed.",
    )
    def test_ni_845x_spi_configuration_open_should_not_fail(self):
        """unit test of ni_845x_spi_configuration_open."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (156 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        configuration_handle = _ni_845x_functions.ni_845x_spi_configuration_open_impl()
        _ni_845x_functions.ni_845x_spi_configuration_close_impl(configuration_handle)

        # Assert
        self.assertNotEqual(
            first=0,
            second=configuration_handle,
        )

    @unittest.skipIf(
        not _is_ni_845x_installed(),
        "The execution of test is skipped because Ni-845x driver is not installed.",
    )
    def test_ni_845x_i2c_configuration_set_address_should_not_fail(self):
        """unit test of ni_845x_i2c_configuration_set_address."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (163 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_address = int(random() * 65535)

        # Act
        configuration_handle = _ni_845x_functions.ni_845x_i2c_configuration_open_impl()
        _ni_845x_functions.ni_845x_i2c_configuration_set_address_impl(
            configuration_handle, expected_address
        )
        actual_address = _ni_845x_functions.ni_845x_i2c_configuration_get_address_impl(
            configuration_handle
        )
        _ni_845x_functions.ni_845x_i2c_configuration_close_impl(configuration_handle)

        # Assert
        self.assertEqual(
            first=expected_address,
            second=actual_address,
        )

    @unittest.skipIf(
        not _is_ni_845x_installed(),
        "The execution of test is skipped because Ni-845x driver is not installed.",
    )
    def test_ni_845x_i2c_configuration_set_clock_rate_should_not_fail(self):
        """unit test of ni_845x_i2c_configuration_set_clock_rate."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (166 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_clock_rate = int(random() * 500)

        # Act
        configuration_handle = _ni_845x_functions.ni_845x_i2c_configuration_open_impl()
        _ni_845x_functions.ni_845x_i2c_configuration_set_clock_rate_impl(
            configuration_handle, expected_clock_rate
        )
        actual_clock_rate = _ni_845x_functions.ni_845x_i2c_configuration_get_clock_rate_impl(
            configuration_handle
        )
        _ni_845x_functions.ni_845x_i2c_configuration_close_impl(configuration_handle)

        # Assert
        self.assertEqual(
            first=expected_clock_rate,
            second=actual_clock_rate,
        )

    @unittest.skipIf(
        not _is_ni_845x_installed(),
        "The execution of test is skipped because Ni-845x driver is not installed.",
    )
    def test_ni_845x_i2c_configuration_set_addressing_type_should_not_fail(self):
        """unit test of ni_845x_i2c_configuration_set_addressing_type."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_addressing_type = Ni845xI2cAddressingType.ADDRESSING_10_BIT

        # Act
        configuration_handle = _ni_845x_functions.ni_845x_i2c_configuration_open_impl()
        _ni_845x_functions.ni_845x_i2c_configuration_set_addressing_type_impl(
            configuration_handle, expected_addressing_type
        )
        actual_addressing_type = (
            _ni_845x_functions.ni_845x_i2c_configuration_get_addressing_type_impl(
                configuration_handle
            )
        )
        _ni_845x_functions.ni_845x_i2c_configuration_close_impl(configuration_handle)

        # Assert
        self.assertEqual(
            first=expected_addressing_type,
            second=actual_addressing_type,
        )

    @unittest.skipIf(
        not _is_ni_845x_installed(),
        "The execution of test is skipped because Ni-845x driver is not installed.",
    )
    def test_ni_845x_i2c_configuration_set_ack_poll_timeout_should_not_fail(self):
        """unit test of ni_845x_i2c_configuration_set_ack_poll_timeout."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (172 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_ack_poll_timeout = int(random() * 20000)

        # Act
        configuration_handle = _ni_845x_functions.ni_845x_i2c_configuration_open_impl()
        _ni_845x_functions.ni_845x_i2c_configuration_set_ack_poll_timeout_impl(
            configuration_handle, expected_ack_poll_timeout
        )
        actual_ack_poll_timeout = (
            _ni_845x_functions.ni_845x_i2c_configuration_get_ack_poll_timeout_impl(
                configuration_handle
            )
        )
        _ni_845x_functions.ni_845x_i2c_configuration_close_impl(configuration_handle)

        # Assert
        self.assertEqual(
            first=expected_ack_poll_timeout,
            second=actual_ack_poll_timeout,
        )


class TestSpiConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    functions related to SPI configuration are ready to use.

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

    @unittest.skipIf(
        not _is_ni_845x_installed(),
        "The execution of test is skipped because Ni-845x driver is not installed.",
    )
    def test_ni_845x_spi_configuration_set_chip_select_should_not_fail(self):
        """unit test of ni_845x_spi_configuration_set_chip_select."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (167 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_chip_select = int(random() * 100)

        # Act
        configuration_handle = _ni_845x_functions.ni_845x_spi_configuration_open_impl()
        _ni_845x_functions.ni_845x_spi_configuration_set_chip_select_impl(
            configuration_handle, expected_chip_select
        )
        actual_chip_select = _ni_845x_functions.ni_845x_spi_configuration_get_chip_select_impl(
            configuration_handle
        )
        _ni_845x_functions.ni_845x_spi_configuration_close_impl(configuration_handle)

        # Assert
        self.assertEqual(
            first=expected_chip_select,
            second=actual_chip_select,
        )

    @unittest.skipIf(
        not _is_ni_845x_installed(),
        "The execution of test is skipped because Ni-845x driver is not installed.",
    )
    def test_ni_845x_spi_configuration_set_clock_rate_should_not_fail(self):
        """unit test of ni_845x_spi_configuration_set_clock_rate."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (166 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_clock_rate = int(random() * 20000)

        # Act
        configuration_handle = _ni_845x_functions.ni_845x_spi_configuration_open_impl()
        _ni_845x_functions.ni_845x_spi_configuration_set_clock_rate_impl(
            configuration_handle, expected_clock_rate
        )
        actual_clock_rate = _ni_845x_functions.ni_845x_spi_configuration_get_clock_rate_impl(
            configuration_handle
        )
        _ni_845x_functions.ni_845x_spi_configuration_close_impl(configuration_handle)

        # Assert
        self.assertEqual(
            first=expected_clock_rate,
            second=actual_clock_rate,
        )

    @parameterized.expand(
        [
            (
                "CLOCK_PHASE_FIRST_EDGE",
                SpiConfigurationClockPhase.CLOCK_PHASE_FIRST_EDGE,
            ),
            (
                "CLOCK_PHASE_SECOND_EDGE",
                SpiConfigurationClockPhase.CLOCK_PHASE_SECOND_EDGE,
            ),
        ]
    )
    @unittest.skipIf(
        not _is_ni_845x_installed(),
        "The execution of test is skipped because Ni-845x driver is not installed.",
    )
    def test_ni_845x_spi_configuration_set_clock_phase_should_not_fail(
        self, test_name: str, clock_phase: SpiConfigurationClockPhase
    ):
        """unit test of ni_845x_spi_configuration_set_clock_phase."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (167 > 100 characters) (auto-generated noqa)
        logging.debug("Running with %s", test_name)
        # Arrange
        expected_clock_phase = clock_phase

        # Act
        configuration_handle = _ni_845x_functions.ni_845x_spi_configuration_open_impl()
        _ni_845x_functions.ni_845x_spi_configuration_set_clock_phase_impl(
            configuration_handle, expected_clock_phase
        )
        actual_clock_phase = _ni_845x_functions.ni_845x_spi_configuration_get_clock_phase_impl(
            configuration_handle
        )
        _ni_845x_functions.ni_845x_spi_configuration_close_impl(configuration_handle)

        # Assert
        self.assertEqual(
            first=expected_clock_phase,
            second=actual_clock_phase,
        )

    @parameterized.expand(
        [
            (
                "CLOCK_POLARITY_IDLE_HIGH",
                SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_HIGH,
            ),
            (
                "CLOCK_POLARITY_IDLE_LOW",
                SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW,
            ),
        ]
    )
    @unittest.skipIf(
        not _is_ni_845x_installed(),
        "The execution of test is skipped because Ni-845x driver is not installed.",
    )
    def test_ni_845x_spi_configuration_set_clock_polarity_should_not_fail(
        self, test_name: str, clock_polarity: SpiConfigurationClockPolarity
    ):
        """unit test of ni_845x_spi_configuration_set_clock_polarity."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (170 > 100 characters) (auto-generated noqa)
        logging.debug("Running with %s", test_name)
        # Arrange
        expected_clock_polarity = clock_polarity

        # Act
        configuration_handle = _ni_845x_functions.ni_845x_spi_configuration_open_impl()
        _ni_845x_functions.ni_845x_spi_configuration_set_clock_polarity_impl(
            configuration_handle, expected_clock_polarity
        )
        actual_clock_polarity = (
            _ni_845x_functions.ni_845x_spi_configuration_get_clock_polarity_impl(
                configuration_handle
            )
        )
        _ni_845x_functions.ni_845x_spi_configuration_close_impl(configuration_handle)

        # Assert
        self.assertEqual(
            first=expected_clock_polarity,
            second=actual_clock_polarity,
        )


class TestConvertMemoryAddressToDataBytesArray(unittest.TestCase):
    """Defines a test fixture that checks
    function `convert_memory_address_to_data_bytes_array` is ready to use.

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

    @parameterized.expand(
        [
            (
                "one byte little endian",
                12,
                DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE,
                DataMemoryAddressEndianness.LITTLE_ENDIAN,
                [12],
            ),
            (
                "one byte big endian",
                12,
                DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE,
                DataMemoryAddressEndianness.BIG_ENDIAN,
                [12],
            ),
            (
                "one byte little endian with 2-bytes sized value",
                3852,
                DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE,
                DataMemoryAddressEndianness.LITTLE_ENDIAN,
                [12],
            ),
            (
                "one byte big endian with 2-bytes sized value",
                3852,
                DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE,
                DataMemoryAddressEndianness.BIG_ENDIAN,
                [12],
            ),
            (
                "two bytes little endian",
                12,
                DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                DataMemoryAddressEndianness.LITTLE_ENDIAN,
                [0, 12],
            ),
            (
                "two bytes big endian",
                12,
                DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                DataMemoryAddressEndianness.BIG_ENDIAN,
                [12, 0],
            ),
            (
                "two bytes little endian with 2-bytes sized value",
                3852,
                DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                DataMemoryAddressEndianness.LITTLE_ENDIAN,
                [15, 12],
            ),
            (
                "two bytes big endian with 2-bytes sized value",
                3852,
                DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                DataMemoryAddressEndianness.BIG_ENDIAN,
                [12, 15],
            ),
        ]
    )
    def test_convert_memory_address_to_data_bytes_array(
        self,
        test_case_name: str,
        memory_address: int,
        address_type: DataMemoryAddressType,
        address_endianness: DataMemoryAddressEndianness,
        expected_bytes_array: List[int],
    ):
        """unit test of convert_memory_address_to_data_bytes_array."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (245 > 100 characters) (auto-generated noqa)

        logging.debug("running %s.", test_case_name)

        actual_bytes_array = _ni_845x_functions.convert_memory_address_to_data_bytes_array(
            memory_address=memory_address,
            address_type=address_type,
            address_endianness=address_endianness,
        )

        self.assertListEqual(expected_bytes_array, actual_bytes_array)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_core_tests/__init__.py sha256=bd409cf9650191a95d31f8d892f06865661856f960e02822e8b3ca7e0bc5c293 bytes=250 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_core_tests/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_core_tests/__init__.py`
- sha256: `bd409cf9650191a95d31f8d892f06865661856f960e02822e8b3ca7e0bc5c293`
- bytes: 250

````python
"""Provides a set of unit tests for nipcbatt.pcbatt_core package"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (178 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_core_tests/test_pcbatt_building_blocks.py sha256=9880ebec3b29b61dc8c543dc2ac1d0f6f0312b923e4b69e32e91b800d057cb25 bytes=27703 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_core_tests/test_pcbatt_building_blocks.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_core_tests/test_pcbatt_building_blocks.py`
- sha256: `9880ebec3b29b61dc8c543dc2ac1d0f6f0312b923e4b69e32e91b800d057cb25`
- bytes: 27703

````python
# pylint: disable=C0116, W0201, W0613, W0231
"""This module provides unit tests of module pcbatt_building_blocks
   present in package pcbatt_core located in src."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (345 > 100 characters) (auto-generated noqa)
import importlib.metadata
import logging
import sys
import unittest
from dataclasses import (  # noqa: F401 - 'dataclasses.dataclass' imported but unused (auto-generated noqa)
    dataclass,
)
from enum import Enum  # noqa: F401 - 'enum.Enum' imported but unused (auto-generated noqa)

import nidaqmx
from nidaqmx import utils  # noqa: F401 - 'nidaqmx.utils' imported but unused (auto-generated noqa)
from nidaqmx._task_modules.ai_channel_collection import AIChannelCollection
from nidaqmx._task_modules.ao_channel_collection import (  # noqa: F401 - 'nidaqmx._task_modules.ao_channel_collection.AOChannelCollection' imported but unused (auto-generated noqa)
    AOChannelCollection,
)
from nidaqmx._task_modules.channels.channel import (  # noqa: F401 - 'nidaqmx._task_modules.channels.channel.Channel' imported but unused (auto-generated noqa)
    Channel,
)
from nidaqmx._task_modules.ci_channel_collection import CIChannelCollection
from nidaqmx._task_modules.co_channel_collection import COChannelCollection
from nidaqmx._task_modules.di_channel_collection import DIChannelCollection
from nidaqmx._task_modules.do_channel_collection import DOChannelCollection
from nidaqmx._task_modules.export_signals import (  # noqa: F401 - 'nidaqmx._task_modules.export_signals.ExportSignals' imported but unused (auto-generated noqa)
    ExportSignals,
)
from nidaqmx._task_modules.in_stream import InStream
from nidaqmx._task_modules.out_stream import OutStream
from nidaqmx._task_modules.timing import Timing
from nidaqmx._task_modules.triggers import Triggers
from nidaqmx.constants import ChannelType, Edge, UsageTypeAI
from nidaqmx.errors import DaqError
from varname import nameof

import nipcbatt.pcbatt_utilities.reflection_utilities
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import (
    BuildingBlockUsingDAQmx,
    BuildingBlockUsingInstrument,
)


class TestInstrument:
    """Defines the instrument used in TestAbstractBuildingBlockUsingInstrument fixture"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (200 > 100 characters) (auto-generated noqa)

    def close(self):
        pass


class ChildClassForTests(BuildingBlockUsingInstrument):
    """chlid class of BuildingBlockUsingInstrument
     that defines minimum required implementations

    Args:
        BuildingBlockUsingInstrument: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    @property
    def is_instrument_initialized(self) -> bool:
        """Checks whether the instance of TestInstrument is initialized.

        Returns:
            bool: True, if the instance of TestInstrument is initialized.
        """
        return not isinstance(self._instrument, type(None))

    @property
    def instrument(self) -> TestInstrument:
        """Defines the instance of TestInstrument.

        Returns:
            TestInstrument: the type of instrument.
        """
        return self._instrument

    @property
    def name(self):
        return "blah"

    @classmethod
    def _instrument_factory(cls) -> TestInstrument:
        """Creates an instance of TestInstrument.
        Returns:
            TestInstrument: the type of instrument.
        """  # noqa: D205, D411, W505 - 1 blank line required between summary line and description (auto-generated noqa), Missing blank line before section (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
        return TestInstrument()

    def close(self):
        pass


class ChildClassInitWithIntFloat(ChildClassForTests):
    """Chlid class of ChildClassForTests(BuildingBlockUsingInstrument).
     It uses initialization with an int argument and a string argument.

    Args:
        ChildClassForTests: Base class from which this class inherits.
    """  # noqa: D205, W505 - 1 blank line required between summary line and description (auto-generated noqa), doc line too long (104 > 100 characters) (auto-generated noqa)

    def initialize(self, int_param: int, str_param: str):
        """Initializes the building block with specific values.

        Args:
            int_param (int): the int argument
            str_param (str): the string argument
        """
        self.int_param = int_param
        self.str_param = str_param


class ChildClassInitWithVarious(ChildClassForTests):
    """Chlid class of ChildClassForTests(BuildingBlockUsingInstrument).
       It uses initialization with variatic argument(s).

    Args:
        ChildClassForTests: Base class from which this class inherits.
    """  # noqa: D205, W505 - 1 blank line required between summary line and description (auto-generated noqa), doc line too long (104 > 100 characters) (auto-generated noqa)

    def initialize(self, *args, **kwnargs):
        """Initializes the building block with variatic arguments."""
        self.args = args
        self.kwnargs = kwnargs


class ChannelNames(ChildClassForTests):
    """x"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)

    def __init__(self, n):  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self.channel_names = ["x"] * n


class ChannelsToRead(ChildClassForTests):
    """x"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)

    def __init__(self, n):  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self.channels_to_read = ChannelNames(n)
        self._task = Task()
        self.di_num_booleans_per_chan = 1


class Task(ChildClassForTests):
    """x"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)

    def __init__(self):  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self._handle = 1
        self._interpreter = MockDAQmxTask.Interpreter()
        self.channels = DIChannel()

    def _calculate_num_samps_per_chan(self, one):
        return 1

    def _raise_invalid_write_num_chans_error(self, one, two):
        if two == 10:
            raise ValueError("num chans error!")


class Name(ChildClassForTests):
    """x"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)

    @property
    def name(self):
        return "One"


class DIChannel(ChildClassForTests):
    """x"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)

    def __iter__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        channel_list = [Name()] * self.num_channels
        self.a = iter(channel_list)
        return self.a

    def __next__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return self.a

    def __init__(self):  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self.num_channels = 3
        self.channel_names = ["One"]

    def add_di_chan(self, ch_exp, two, three):
        if "line" not in ch_exp:
            raise DaqError("Need channel", 1)
        x = int(ch_exp[-1]) + 1
        y = int(ch_exp[-3])
        self.num_channels = x - y


class OStream(  # noqa: D101 - Missing docstring in public class (auto-generated noqa)
    ChildClassForTests
):
    def __init__(self):  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self._task = Task()


class MockDAQmxTask(nidaqmx.Task):
    """defines methods used to simulate instruments though DAQmx.

    Args:
        nidaqmx.Task: the class from which this class inherits.
    """

    class Interpreter:
        "Empty class creates to deal with mock interpreter bugs"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (175 > 100 characters) (auto-generated noqa)

        def __init__(self):
            "Do nothing"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (135 > 100 characters) (auto-generated noqa)
            self.num_channels = 0

        def add_global_chans_to_task(self, one, two):
            if two == "":
                raise DaqError("This be error", 1)

        def stop_task(self, handle):
            "Stops the task (does nothing)"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (154 > 100 characters) (auto-generated noqa)

        def create_do_chan(self, handle, lines, name_to_assign_to_lines, line_grouping):
            "Do nothing"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (135 > 100 characters) (auto-generated noqa)

        def create_di_chan(self, handle, lines, name_to_assign_to_lines, line_grouping):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def create_ai_thrmcpl_chan(self, one, two, three, four, five, six, seven, eight, nine, ten):
            if ten == "" and eight == 10113:
                raise DaqError("channel is None", 1)

            if ten is None and nine is not None:
                raise DaqError("channel is None", 1)

        def add_ci_freq_chan(
            self, one, two, three, four, five, six, seven, eight, nine, ten, eleven
        ):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def create_ci_freq_chan(
            self, one, two, three, four, five, six, seven, eight, nine, ten, eleven
        ):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def create_co_pulse_chan_freq(self, one, two, three, four, five, six, seven, eight):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def create_co_pulse_chan_time(self, one, two, three, four, five, six, seven, eight):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def get_task_attribute_uint32(self, one, two):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def get_read_attribute_uint32(self, one, two):
            return 1

        def task_control(self, handle, action):
            "Do nothing"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (135 > 100 characters) (auto-generated noqa)

        def get_task_attribute_string(self, handle, x=int(1273)):
            return "stuff"

        def get_read_attribute_string(self, handle, two):
            return "One"

        def set_read_attribute_string(self, handle, d1823, val):
            self.num_channels = val

        def set_chan_attribute_int32(self, one, two, three, four):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def get_chan_attribute_int32(self, one, two, three):
            if three == 6271:
                return ChannelType.ANALOG_INPUT
            if three == 1685:
                return UsageTypeAI.TEMPERATURE_THERMOCOUPLE

        def write_many_sample_port_uint32(self, data):
            "yep"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (217 > 100 characters) (auto-generated noqa)

        def cfg_samp_clk_timing(
            self,
            rate,
            source,
            active_edge=Edge.RISING,
            sample_mode=1,
            samps_per_chan=1,
            stuff=1,
        ):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def cfg_dig_edge_start_trig(self, source, edge, stuff):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def write_digital_u32(self, one, two, three, four, five, six):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def get_timing_attribute_double(self, one, two):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def set_chan_attribute_double(self, handle, two, three, four):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def start_task(self, one):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def disable_start_trig(self, one):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def read_analog_f64(self, one, two, three, four, five):
            return [1.0], [1.0]

        def write_ctr_freq_scalar(self, one, two, three, four, five):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def write_ctr_time_scalar(self, one, two, three, four, five):
            return 100.0

        def read_counter_scalar_f64(self, handle, timeout):
            return 100.0

        def read_counter_f64_ex(self, handle, timeout, three, four, five):
            return [100.0, 100.0]

        def read_digital_lines(self, task, num_samps_per_chan, timeout, fill_mode, read_array):
            return [[1] * len(read_array), 1, 1]

    def __init__(self, new_task_name="", *, grpc_options=None):
        """Does not call Task.__init__ (it requires DAQmx to be installed)."""  # noqa: D402, W505 - First line should not be the function's "signature" (auto-generated noqa), doc line too long (168 > 100 characters) (auto-generated noqa)
        self._interpreter = self.Interpreter()
        self._handle = ""
        self._do_channels = DOChannelCollection("", self._interpreter)
        self._co_channels = COChannelCollection("", self._interpreter)
        self._ci_channels = CIChannelCollection("", self._interpreter)
        self._di_channels = DIChannelCollection("", self._interpreter)
        self._timing = Timing("", self._interpreter)
        self._triggers = Triggers("", self._interpreter)
        self._out_stream = OutStream(self, self._interpreter)
        self._in_stream = InStream(self, self._interpreter)
        self._di_channels = DIChannel()
        self._ai_channels = AIChannelCollection("", self._interpreter)
        # self.number_of_channels = 2

    @property
    def in_stream(self):
        self.num_channels = self.di_channels.num_channels
        self.channels_to_read = ChannelsToRead(self.num_channels)
        return self.channels_to_read

    @property
    def number_of_channels(self):
        return 1

    @property
    def out_stream(self):
        return OStream()

    def close(self):
        """Closes the task (does nothing)."""

    def __del__(self):
        """Called when the instance is deleted (does nothing)."""

    @property
    def channels(self):
        class Channels:
            "placeholder class"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (142 > 100 characters) (auto-generated noqa)

            def __init__(self):
                self.channel_names = DIChannel()
                self.co_pulse_freq = 1
                self.co_pulse_duty_cyc = 0.5
                self.co_ctr_timebase_rate = 1.0
                self.co_pulse_high_time = 0.5
                self.co_pulse_low_time = 0.5
                self.number_of_channels = 2

        return Channels()

    @property
    def channel_names(self):
        return None

    @property
    def do_channels(self):
        class DOChannel:
            def __init__(self):
                self.num_channels = 1

            def add_do_chan(self, exp):
                return [DOChannel()]

        return DOChannel()

    @property
    def ci_channels(self):
        class CI_Channels:  # noqa: N801 - class name 'CI_Channels' should use CapWords convention (auto-generated noqa)
            def __init__(self):
                self.channel_names = "Channel_One"

            def add_ci_freq_chan(self, one, two):
                self.channel_names = one

            def add_ci_semi_period_chan(
                self, counter, name_to_assign_to_channel, min_val, max_val, units
            ):
                self.channel_names = "Channel_One"

        return CI_Channels()

    def set_num_channels(self, n):
        self.num_channels = n

    @property
    def di_channels(self):
        return self._di_channels

    @property
    def timing(self):
        class Time:
            "placeholder class"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (142 > 100 characters) (auto-generated noqa)

            def __init__(self):
                self.samp_clk_rate = 1
                self.samp_quant_samp_per_chan = 1

            def cfg_samp_clk_timing(
                self,
                rate,
                source,
                active_edge=Edge.RISING,
                sample_mode=1,
                samps_per_chan=1,
            ):
                "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (228 > 100 characters) (auto-generated noqa)

            def cfg_implicit_timing(self, sample_mode="one", samps_per_chan="two"):
                "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (228 > 100 characters) (auto-generated noqa)

        return Time()


class TestBuildingBlockUsingInstrument(unittest.TestCase):
    """Defines a test fixture that checks child classes of
    BuildingBlockUsingInstrument are ready to use.

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

        used_numpy_version = importlib.metadata.version("numpy")
        logging.debug("%s = %s", nameof(used_numpy_version), used_numpy_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_child_initalization_without_arguments(self):
        block = ChildClassForTests()
        self.assertIsInstance(block, ChildClassForTests)

        block = ChildClassInitWithIntFloat()
        self.assertIsInstance(block, ChildClassInitWithIntFloat)

    def test_child_instrument(self):
        block = ChildClassForTests()
        self.assertIsNot(block.instrument, None)
        self.assertIsInstance(block.instrument, TestInstrument)

    def test_child_initalization_with_fixed_arguments(self):
        expected_int = 3.0
        expected_string = "Test_string"
        block = ChildClassInitWithIntFloat(expected_int, expected_string)
        self.assertIsInstance(block, ChildClassInitWithIntFloat)
        actual_int = block.int_param
        actual_string = block.str_param
        self.assertEqual(expected_int, actual_int)
        self.assertEqual(expected_string, actual_string)

    def test_child_initialazation_with_various_arguments(self):
        arg_1 = "test_argument_1"
        arg_2 = 2.8
        arg_3 = [45.9, "test_argument_3"]

        block = ChildClassInitWithVarious(arg_1, arg_2, arg_3)

        expected = 3
        actual = len(block.args)
        self.assertEqual(first=expected, second=actual)

        expected = arg_1
        actual = block.args[0]
        self.assertEqual(first=expected, second=actual)

        expected = arg_2
        actual = block.args[1]
        self.assertEqual(first=expected, second=actual)

        self.assertIsInstance(arg_3, list)

        expected = 2
        actual = len(block.args[2])
        self.assertEqual(first=expected, second=actual)

        expected = 45.9
        actual = block.args[2][0]
        self.assertEqual(first=expected, second=actual)

        expected = "test_argument_3"
        actual = block.args[2][1]
        self.assertEqual(first=expected, second=actual)


def instrument_factory() -> MockDAQmxTask:
    """Creates an instance of MockDAQmxTask."""
    return MockDAQmxTask()


class BuildingBlockUsingDAQmxForTests(BuildingBlockUsingDAQmx):
    """Chlid class of BuildingBlockUsingDAQmx(BuildingBlockUsingInstrument).

    Args:
        BuildingBlockUsingDAQmx: Base class from which this class inherits.
    """

    def initialize(self):
        """Initializes the building block with specific values."""

    def close(self):
        """Closes the building block and releases its internal resources."""


class TestBuildingBlockUsingDAQmx(unittest.TestCase):
    """Defines a test fixture that checks child classes of BuildingBlockUsingDAQmx are ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """

    def setUp(self):
        nipcbatt.pcbatt_utilities.reflection_utilities.substitute_method(
            cls=BuildingBlockUsingDAQmx,
            method=instrument_factory,
            method_name="_instrument_factory",
        )

    def tearDown(self):
        pass

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

    def test_child_initalization_without_arguments(self):
        block = BuildingBlockUsingDAQmxForTests()
        self.assertIsInstance(block, BuildingBlockUsingDAQmxForTests)
        self.assertIsInstance(block.task, MockDAQmxTask)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/__init__.py sha256=51471f53de7f6cdf320a602da5780b05764ff4f59ea3860abdd060b4ea14c335 bytes=260 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/__init__.py`
- sha256: `51471f53de7f6cdf320a602da5780b05764ff4f59ea3860abdd060b4ea14c335`
- bytes: 260

````python
"""Provides a set of integration tests for nipcbatt.pcbatt_library package"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (188 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_current_measurements/__init__.py sha256=aa8540cc7cad559dfbf9da2789f613b8457eb183f3eb2b6e43b9c91659962908 bytes=288 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_current_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_current_measurements/__init__.py`
- sha256: `aa8540cc7cad559dfbf9da2789f613b8457eb183f3eb2b6e43b9c91659962908`
- bytes: 288

````python
"""Provides a set of integration tests for nipcbatt.pcbatt_library.dc_rms_current_measurements package"""  # noqa: W505, D415 - doc line too long (105 > 100 characters) (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_current_measurements/test_integration_dc_rms_current_measurement.py sha256=988c72c55bd8b556c95e53d006fab49b725e8898b12f521db2544ba97104ba9f bytes=13200 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_current_measurements/test_integration_dc_rms_current_measurement.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_current_measurements/test_integration_dc_rms_current_measurement.py`
- sha256: `988c72c55bd8b556c95e53d006fab49b725e8898b12f521db2544ba97104ba9f`
- bytes: 13200

````python
"""This module provides test of integration of DcRmsCurrentMeasurement."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt import daq

'''from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
    _InterpreterDcRmsCurrentMeasurement,
)
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx_if_not_installed,
)'''


class TestIntegrationDcRmsCurrentMeasurement(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `DcRmsCurrentMeasurement` class.

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
        #_replace_daqmx_if_not_installed(_InterpreterDcRmsCurrentMeasurement)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_integration_dc_rms_current_measurement_configure_only(self):
        """Integration test of
        nipcbatt.pcbatt_library.dc_rms_current_measurements.dc_rms_current_measurement.DcRmsCurrentMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (425 > 100 characters) (auto-generated noqa)

        with daq.DcRmsCurrentMeasurement() as measurement:
            measurement.initialize(
                analog_input_channel_expression=(
                    "Sim_PXIeDAQ/ai0:3"
                )
            )

            configuration = daq.DcRmsCurrentMeasurementConfiguration(
                global_channel_parameters=(
                    daq.DEFAULT_DC_RMS_CURRENT_MEASUREMENT_TERMINAL_RANGE_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    daq.DEFAULT_DC_RMS_CURRENT_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    daq.DEFAULT_DC_RMS_CURRENT_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(f"results = {results}")
            self.assertIs(None, results)

            measurement.close()

    def test_integration_dc_rms_current_measurement_configure_only_and_measure_only(
        self,
    ):
        """Integration test of
        daq.pcbatt_library.dc_rms_current_measurements.dc_rms_current_measurement.DcRmsCurrentMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (422 > 100 characters) (auto-generated noqa)

        with daq.DcRmsCurrentMeasurement() as measurement:
            measurement.initialize(
                analog_input_channel_expression=(
                    "Sim_PXIeDAQ/ai0:3"
                )
            )

            configuration = daq.DcRmsCurrentMeasurementConfiguration(
                global_channel_parameters=(
                    daq.DEFAULT_DC_RMS_CURRENT_MEASUREMENT_TERMINAL_RANGE_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    daq.DEFAULT_DC_RMS_CURRENT_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    daq.DEFAULT_DC_RMS_CURRENT_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_ONLY, results = {results}"
            )
            self.assertIs(None, results)

            configuration = daq.DcRmsCurrentMeasurementConfiguration(
                global_channel_parameters=(
                    daq.DEFAULT_DC_RMS_CURRENT_MEASUREMENT_TERMINAL_RANGE_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    daq.DEFAULT_DC_RMS_CURRENT_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    daq.DEFAULT_DC_RMS_CURRENT_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )

            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
            )
            self.assertIsInstance(results, daq.DcRmsCurrentMeasurementResultData)

            measurement.close()

    def test_integration_dc_rms_current_measurement_configure_and_measure(
        self,
    ):
        """Integration test of
        daq.pcbatt_library.dc_rms_current_measurements.dc_rms_current_measurement.DcRmsCurrentMeasurement
        with MeasurementExecutionType.CONFIGURE_AND_MEASURE.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.DcRmsCurrentMeasurement() as measurement:
            measurement.initialize(
                analog_input_channel_expression=(
                    "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
                )
            )

            configuration = daq.DcRmsCurrentMeasurementConfiguration(
                global_channel_parameters=(
                    daq.DEFAULT_DC_RMS_CURRENT_MEASUREMENT_TERMINAL_RANGE_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    daq.DEFAULT_DC_RMS_CURRENT_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    daq.DEFAULT_DC_RMS_CURRENT_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_AND_MEASURE and MeasurementAnalysisRequirement.SKIP_ANALYSIS, results = {results}"
            )
            self.assertIs(None, results)

            configuration = daq.DcRmsCurrentMeasurementConfiguration(
                global_channel_parameters=(
                    daq.DEFAULT_DC_RMS_CURRENT_MEASUREMENT_TERMINAL_RANGE_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=(nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE),
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    daq.DEFAULT_DC_RMS_CURRENT_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    daq.DEFAULT_DC_RMS_CURRENT_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )

            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_AND_MEASURE and MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS, results = {results}"
            )
            self.assertIsInstance(results, daq.DcRmsCurrentMeasurementResultData)

            measurement.close()

    def test_integration_dc_rms_current_measurement_full_sequence_in_loop(
        self,
    ):
        """Integration test of
        daq.pcbatt_library.dc_rms_current_measurements.dc_rms_current_measurement.DcRmsCurrentMeasurement
        to be called in a loop.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        channel_list = [
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3",
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai5",
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai1,NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai6",
        ]

        for channel in channel_list:
            with daq.DcRmsCurrentMeasurement() as measurement:
                measurement.initialize(analog_input_channel_expression=channel)

                configuration = daq.DcRmsCurrentMeasurementConfiguration(
                    global_channel_parameters=(
                        daq.DEFAULT_DC_RMS_CURRENT_MEASUREMENT_TERMINAL_RANGE_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_options=daq.DEFAULT_DC_RMS_CURRENT_MEASUREMENT_OPTIONS,
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_DC_RMS_CURRENT_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_DC_RMS_CURRENT_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )

                results = measurement.configure_and_measure(configuration=configuration)

                print(
                    f"With Default configurations for channel string :{channel}, results = {results}"
                )
                self.assertIsInstance(results, daq.DcRmsCurrentMeasurementResultData)

                measurement.close()


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_current_measurements/test_integration_dmm_dcrms_current_measurements.py sha256=880a2a1a000b7f2f8a99d755a2952895fddda7772458d49ee2801028e2b4f5a6 bytes=9537 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_current_measurements/test_integration_dmm_dcrms_current_measurements.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_current_measurements/test_integration_dmm_dcrms_current_measurements.py`
- sha256: `880a2a1a000b7f2f8a99d755a2952895fddda7772458d49ee2801028e2b4f5a6`
- bytes: 9537

````python
"""This module provides test of integration of DMM DC RMS current generation"""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nidmm
import nipcbatt
from nipcbatt import dmm

class TestIntegrationDmmDcRmsCurrentMeasurement(unittest.TestCase):
    """Definte a test fixture that check the integration of 
    'DmmDCRmsCurrent'
    
    Args:
        unittest.TestCase: Base class from which this class inherits
    """

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

        used_niswitch_version = importlib.metadata.version("niswitch")
        logging.debug("%s = %s", nameof(used_niswitch_version), used_niswitch_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")


    def test_initialize_configure_measure_close_dc(self):
        """Happy path: DC current configure & measure."""

        resource_name = "Sim_DMM"
        powerline_freq = 60.0

        uut = dmm.DcRmsCurrentMeasurement()
        uut.initialize(resource_name, powerline_freq)

        meas_params = dmm.DcRmsCurrentMeasurementFunctionParameters(
             dmm.CurrentRangeAndFunctions.DC_1mA,
             dmm.ResolutionInDigits.DIGITS_5_5
        )

        trig_params = dmm.TriggerParameters(
             trigger_source = nidmm.TriggerSource.IMMEDIATE,
             trigger_delay= 0.0,
             slope=dmm.Slope.RISING_EDGE,
             enable_trigger=True
        )
       
        timing_params = dmm.TimingParameters(
             aperture_time_seconds = 0.001,
             settle_time_seconds = 0.01
        )

        cfg = dmm.DcRmsCurrentMeasurementConfiguration(
             execution_type = nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
             measurement_function_parameters = meas_params,
             trigger_parameters = trig_params,
             timing_parameters = timing_params,
             ac_min_frequency = 10.0
        )

        result = uut.configure_and_measure(cfg)

        uut.close()


    def test_initialize_and_close_is_idempotent(self):

        "Tests if class methods are idempotent"

        uut = dmm.DcRmsCurrentMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        # Power line frequency should be set
        assert uut.session.powerline_freq == 60.0  # attribute assignment on session

        # First close should call session.close and clear instrument
        uut.close()

        # Second close should be a no-op (no exception, no additional close())
        uut.close()


    def test_configure_only_returns_none(self):

        """Ensures configure only returns none"""

        uut = dmm.DcRmsCurrentMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        cfg = dmm.DcRmsCurrentMeasurementConfiguration(
            execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
            measurement_function_parameters=dmm.DcRmsCurrentMeasurementFunctionParameters(
                dmm.CurrentRangeAndFunctions.DC_10mA, dmm.ResolutionInDigits.DIGITS_5_5
            ),
            trigger_parameters=dmm.TriggerParameters(
                trigger_source=nidmm.TriggerSource.IMMEDIATE,
                trigger_delay=0.0,
                slope=None,
                enable_trigger=False,
            ),
            timing_parameters=dmm.TimingParameters(0.001, 0.01),
            ac_min_frequency=10.0,
        )

        result = uut.configure_and_measure(cfg)
        assert result is None  # configure-only path returns None 

        uut.close()

    
    def test_measure_only_reads_and_wraps(self):

        """Ensure measure only reads"""

        uut = dmm.DcRmsCurrentMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        cfg = dmm.DcRmsCurrentMeasurementConfiguration(
            execution_type=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
            measurement_function_parameters=dmm.DcRmsCurrentMeasurementFunctionParameters(
                dmm.CurrentRangeAndFunctions.DC_1mA, dmm.ResolutionInDigits.DIGITS_5_5
            ),
            trigger_parameters=dmm.TriggerParameters(
                trigger_source=nidmm.TriggerSource.IMMEDIATE, trigger_delay=0.0, slope=None, enable_trigger=True
            ),
            timing_parameters=dmm.TimingParameters(0.001, 0.01),
            ac_min_frequency=10.0,
        )

        result = uut.configure_and_measure(cfg)

        # `acquire_measurement` returns a result object with two dicts
        assert result is not None
        assert isinstance(result.dmm_execution_settings, dict)
        assert isinstance(result.measurement, dict)  # built in acquire_measurement 
        uut.close()


    def test_configure_measure_ac(self):
        """AC current measurement should apply ac_min_frequency."""

        uut = dmm.DcRmsCurrentMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        meas_params = dmm.DcRmsCurrentMeasurementFunctionParameters(
            dmm.CurrentRangeAndFunctions.AC_100mA,
            dmm.ResolutionInDigits.DIGITS_4_5
        )

        trig_params = dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.IMMEDIATE,
            trigger_delay=0.0,
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=True
        )

        timing_params = dmm.TimingParameters(
            aperture_time_seconds=0.001,
            settle_time_seconds=0.01
        )

        cfg = dmm.DcRmsCurrentMeasurementConfiguration(
            execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            measurement_function_parameters=meas_params,
            trigger_parameters=trig_params,
            timing_parameters=timing_params,
            ac_min_frequency=55.0  # AC path should apply this
        )

        result = uut.configure_and_measure(cfg)

        assert result is not None
        assert result.measurement is not None
        assert "Measured_Value" in result.measurement

        # AC min frequency should appear in result settings
        assert "Minimum_Frequency(Hz)" in result.dmm_execution_settings
        assert result.dmm_execution_settings["Minimum_Frequency(Hz)"] == 55.0

        uut.close()


    def test_trigger_disabled(self):
        """Trigger disabled should force IMMEDIATE trigger."""

        uut = dmm.DcRmsCurrentMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        meas_params = dmm.DcRmsCurrentMeasurementFunctionParameters(
            dmm.CurrentRangeAndFunctions.DC_100uA,
            dmm.ResolutionInDigits.DIGITS_5_5
        )

        trig_params = dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.EXTERNAL,  # ignored when disabled
            trigger_delay=999.0,
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=False
        )

        timing_params = dmm.TimingParameters(
            aperture_time_seconds=0.0005,
            settle_time_seconds=0.005
        )

        cfg = dmm.DcRmsCurrentMeasurementConfiguration(
            execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            measurement_function_parameters=meas_params,
            trigger_parameters=trig_params,
            timing_parameters=timing_params,
            ac_min_frequency=10.0
        )

        result = uut.configure_and_measure(cfg)

        assert result is not None
        assert "Function" in result.dmm_execution_settings

        # Trigger disabled should set delay to -1.0 (from your implementation)
        assert result.dmm_execution_settings["Auto_Range_Value"] is not None  # sanity check

    
    def test_multiple_ranges_and_resolutions(self):
        """Verify several measurement function parameters work."""

        uut = dmm.DcRmsCurrentMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        # Try several ranges
        test_ranges = [
            dmm.CurrentRangeAndFunctions.DC_1uA,
            dmm.CurrentRangeAndFunctions.DC_100uA,
            dmm.CurrentRangeAndFunctions.DC_10mA,
            dmm.CurrentRangeAndFunctions.DC_1A
        ]

        for rng in test_ranges:
            meas_params = dmm.DcRmsCurrentMeasurementFunctionParameters(
                rng,
                dmm.ResolutionInDigits.DIGITS_4_5
            )

            cfg = dmm.DcRmsCurrentMeasurementConfiguration(
                execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                measurement_function_parameters=meas_params,
                trigger_parameters=dmm.TriggerParameters(
                    trigger_source=nidmm.TriggerSource.IMMEDIATE,
                    trigger_delay=0.0,
                    slope=dmm.Slope.RISING_EDGE,
                    enable_trigger=True
                ),
                timing_parameters=dmm.TimingParameters(0.001, 0.01),
                ac_min_frequency=10.0
            )

            result = uut.configure_and_measure(cfg)
            assert result is not None
            assert "Measured_Value" in result.measurement

        uut.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_voltage_measurements/__init__.py sha256=ff2f177db5e1e92e50efc43218bf9a1559953838cb604bd1a67d2c5860182a97 bytes=288 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_voltage_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_voltage_measurements/__init__.py`
- sha256: `ff2f177db5e1e92e50efc43218bf9a1559953838cb604bd1a67d2c5860182a97`
- bytes: 288

````python
"""Provides a set of integration tests for nipcbatt.pcbatt_library.dc_rms_voltage_measurements package"""  # noqa: W505, D415 - doc line too long (105 > 100 characters) (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_voltage_measurements/test_integration_dc_rms_voltage_measurement.py sha256=1c398fac5141e58e0bc9cc694b49b4a148444714c21c056b6551c021c03f2f45 bytes=8754 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_voltage_measurements/test_integration_dc_rms_voltage_measurement.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_voltage_measurements/test_integration_dc_rms_voltage_measurement.py`
- sha256: `1c398fac5141e58e0bc9cc694b49b4a148444714c21c056b6551c021c03f2f45`
- bytes: 8754

````python
"""This module provides test of integration of DcRmsVoltageMeasurement."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt import daq

'''from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
    _InterpreterDcRmsVoltageMeasurement,
)
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx_if_not_installed,
)'''


class TestIntegrationDcRmsVoltageMeasurement(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `DcRmsVoltageMeasurement` class.

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
        #_replace_daqmx_if_not_installed(_InterpreterDcRmsVoltageMeasurement)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_integration_dc_rms_voltage_measurement_configure_only(self):
        """Integration test of
        daq.pcbatt_library.dc_rms_voltage_measurements.dc_rms_voltage_measurement.DcRmsVoltageMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (425 > 100 characters) (auto-generated noqa)

        with daq.DcRmsVoltageMeasurement() as measurement:
            measurement.initialize(
                analog_input_channel_expression=(
                    "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
                )
            )

            configuration = daq.DcRmsVoltageMeasurementConfiguration(
                global_channel_parameters=(
                    daq.DEFAULT_DC_RMS_VOLTAGE_RANGE_AND_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    daq.DEFAULT_DC_RMS_VOLTAGE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    daq.DEFAULT_DC_RMS_VOLTAGE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(f"results = {results}")
            self.assertIs(None, results)

    def test_integration_dc_rms_voltage_measurement_configure_and_measure(self):
        """Integration test of
        nipcbatt.pcbatt_library.dc_rms_voltage_measurements.dc_rms_voltage_measurement.DcRmsVoltageMeasurement
        with MeasurementExecutionType.CONFIGURE_AND_MEASURE"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (432 > 100 characters) (auto-generated noqa)

        with daq.DcRmsVoltageMeasurement() as measurement:
            measurement.initialize(
                analog_input_channel_expression=(
                    "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
                )
            )

            print(f"parameters = {daq.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION}")
            results = measurement.configure_and_measure(
                configuration=daq.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION
            )

            print(f"results = {results}")
            self.assertIsInstance(results, daq.DcRmsVoltageMeasurementResultData)

    def test_integration_dc_rms_voltage_measurement_configure_only_and_measure_only(
        self,
    ):
        """Integration test of
        daq.pcbatt_library.dc_rms_voltage_measurements.dc_rms_voltage_measurement.DcRmsVoltageMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (422 > 100 characters) (auto-generated noqa)

        with daq.DcRmsVoltageMeasurement() as measurement:
            measurement.initialize(
                analog_input_channel_expression=(
                    "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
                )
            )

            configuration = daq.DcRmsVoltageMeasurementConfiguration(
                global_channel_parameters=(
                    daq.DEFAULT_DC_RMS_VOLTAGE_RANGE_AND_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    daq.DEFAULT_DC_RMS_VOLTAGE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    daq.DEFAULT_DC_RMS_VOLTAGE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_ONLY, results = {results}"
            )
            self.assertIs(None, results)

            configuration = daq.DcRmsVoltageMeasurementConfiguration(
                global_channel_parameters=(
                    daq.DEFAULT_DC_RMS_VOLTAGE_RANGE_AND_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    daq.DEFAULT_DC_RMS_VOLTAGE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    daq.DEFAULT_DC_RMS_VOLTAGE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )

            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
            )
            self.assertIsInstance(results, daq.DcRmsVoltageMeasurementResultData)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_voltage_measurements/test_integration_dmm_dcrms_voltage_measurements.py sha256=93a7062fadb251f68e561ef4b6dcca818408d169bf1289df7b6eb7d30b59d942 bytes=8929 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_voltage_measurements/test_integration_dmm_dcrms_voltage_measurements.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_rms_voltage_measurements/test_integration_dmm_dcrms_voltage_measurements.py`
- sha256: `93a7062fadb251f68e561ef4b6dcca818408d169bf1289df7b6eb7d30b59d942`
- bytes: 8929

````python
"""This module provides test of integration of DMM DC RMS voltage generation"""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nidmm
import nipcbatt
from nipcbatt import dmm

class TestIntegrationDmmDcRmsVoltageMeasurement(unittest.TestCase):
    """Definte a test fixture that check the integration of 
    'DmmDCRmsVoltage'
    
    Args:
        unittest.TestCase: Base class from which this class inherits
    """

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

        used_niswitch_version = importlib.metadata.version("niswitch")
        logging.debug("%s = %s", nameof(used_niswitch_version), used_niswitch_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")


    def test_configure_only_dc_voltage(self):
        """CONFIGURE_ONLY should not perform a measurement."""

        resource_name = "Sim_DMM"
        powerline_freq = 60.0

        uut = dmm.DcRmsVoltageMeasurement()
        uut.initialize(resource_name, powerline_freq)

        meas_params = dmm.DcRmsVoltageMeasurementFunctionParameters(
            dmm.VoltageRangeAndFunctions.DC_10V,
            dmm.ResolutionInDigits.DIGITS_5_5
        )

        trig_params = dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.IMMEDIATE,
            trigger_delay=0.0,
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=False  # disabled ⇒ immediate/-1 path
        )

        timing_params = dmm.TimingParameters(
            aperture_time_seconds=0.001,
            settle_time_seconds=0.01
        )

        cfg = dmm.DcRmsVoltageMeasurementConfiguration(
            execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
            measurement_function_parameters=meas_params,
            trigger_parameters=trig_params,
            timing_parameters=timing_params,
            ac_min_frequency=10.0
        )

        result = uut.configure_and_measure(cfg)
        assert result is None


    def test_measure_only_dc_voltage(self):
        """MEASURE_ONLY should read and return a result."""

        uut = dmm.DcRmsVoltageMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        meas_params = dmm.DcRmsVoltageMeasurementFunctionParameters(
            dmm.VoltageRangeAndFunctions.DC_1V,
            dmm.ResolutionInDigits.DIGITS_5_5
        )

        trig_params = dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.IMMEDIATE,
            trigger_delay=0.0,
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=True
        )

        timing_params = dmm.TimingParameters(
            aperture_time_seconds=0.002,
            settle_time_seconds=0.02
        )

        cfg = dmm.DcRmsVoltageMeasurementConfiguration(
            execution_type=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
            measurement_function_parameters=meas_params,
            trigger_parameters=trig_params,
            timing_parameters=timing_params,
            ac_min_frequency=10.0
        )

        result = uut.configure_and_measure(cfg)
        assert result is not None
        assert result.measurement is not None
        assert "Measured_Value" in result.measurement

        uut.close()


    def test_configure_and_measure_dc_voltage_trigger_disabled(self):
        """Trigger disabled forces IMMEDIATE and -1.0 delay."""

        uut = dmm.DcRmsVoltageMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        meas_params = dmm.DcRmsVoltageMeasurementFunctionParameters(
            dmm.VoltageRangeAndFunctions.DC_100mV,
            dmm.ResolutionInDigits.DIGITS_5_5
        )

        trig_params = dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.EXTERNAL,   # ignored when disabled
            trigger_delay=0.123,                            # ignored when disabled
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=False
        )

        timing_params = dmm.TimingParameters(
            aperture_time_seconds=0.0005,
            settle_time_seconds=0.005
        )

        cfg = dmm.DcRmsVoltageMeasurementConfiguration(
            execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            measurement_function_parameters=meas_params,
            trigger_parameters=trig_params,
            timing_parameters=timing_params,
            ac_min_frequency=25.0  # DC path should not apply this
        )

        result = uut.configure_and_measure(cfg)

        assert result is not None
        # Sanity check on execution settings produced by acquire_measurement
        assert "Function" in result.dmm_execution_settings
        assert "Aperture_Time(s)" in result.dmm_execution_settings
        assert "Settle_Time(s)" in result.dmm_execution_settings

        uut.close()


    def test_configure_and_measure_ac_voltage(self):
        """AC voltage measurement should apply ac_min_frequency and slope."""

        uut = dmm.DcRmsVoltageMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        meas_params = dmm.DcRmsVoltageMeasurementFunctionParameters(
            dmm.VoltageRangeAndFunctions.AC_2V,
            dmm.ResolutionInDigits.DIGITS_4_5
        )

        trig_params = dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.EXTERNAL,
            trigger_delay=0.001,
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=True
        )

        timing_params = dmm.TimingParameters(
            aperture_time_seconds=0.001,
            settle_time_seconds=0.01
        )

        cfg = dmm.DcRmsVoltageMeasurementConfiguration(
            execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            measurement_function_parameters=meas_params,
            trigger_parameters=trig_params,
            timing_parameters=timing_params,
            ac_min_frequency=123.0
        )

        result = uut.configure_and_measure(cfg)

        assert result is not None
        assert result.measurement is not None

        # AC min frequency should be reported by acquire_measurement's execution settings
        assert "Minimum_Frequency(Hz)" in result.dmm_execution_settings
        assert result.dmm_execution_settings["Minimum_Frequency(Hz)"] == 123.0

        uut.close()


    def test_multiple_voltage_ranges_and_resolutions(self):
        """Exercise several voltage ranges and a common resolution."""

        uut = dmm.DcRmsVoltageMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        test_ranges = [
            dmm.VoltageRangeAndFunctions.DC_Voltage_Auto_Range,
            dmm.VoltageRangeAndFunctions.DC_100mV,
            dmm.VoltageRangeAndFunctions.DC_1V,
            dmm.VoltageRangeAndFunctions.DC_10V,
            dmm.VoltageRangeAndFunctions.DC_100V,
        ]

        for rng in test_ranges:
            meas_params = dmm.DcRmsVoltageMeasurementFunctionParameters(
                rng,
                dmm.ResolutionInDigits.DIGITS_4_5
            )

            trig_params = dmm.TriggerParameters(
                trigger_source=nidmm.TriggerSource.IMMEDIATE,
                trigger_delay=0.0,
                slope=dmm.Slope.RISING_EDGE,
                enable_trigger=True
            )

            timing_params = dmm.TimingParameters(
                aperture_time_seconds=0.001,
                settle_time_seconds=0.01
            )

            cfg = dmm.DcRmsVoltageMeasurementConfiguration(
                execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                measurement_function_parameters=meas_params,
                trigger_parameters=trig_params,
                timing_parameters=timing_params,
                ac_min_frequency=10.0
            )

            result = uut.configure_and_measure(cfg)
            assert result is not None
            assert "Measured_Value" in result.measurement

        uut.close()



    def test_voltage_initialize_and_close_is_idempotent(self):
        """Initialize then close twice to ensure no error and powerline is set."""

        uut = dmm.DcRmsVoltageMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        # Power line frequency should be set
        assert uut.session.powerline_freq == 60.0

        # First close
        uut.close()

        # Second close should be a no‑op (no exception)
        uut.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_voltage_generations/__init__.py sha256=1b0243fe92a789431218d91efd43061536653367606a4be4572da3cc79cf911d bytes=283 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_voltage_generations/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_voltage_generations/__init__.py`
- sha256: `1b0243fe92a789431218d91efd43061536653367606a4be4572da3cc79cf911d`
- bytes: 283

````python
"""Provides a set of integration tests for nipcbatt.pcbatt_library.dc_voltage_generations package"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_voltage_generations/test_integration_dc_voltage_generation.py sha256=01445d1804c06f5f6d75aca474cb01092a35724007fc025290ec878b9eba6e07 bytes=6302 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_voltage_generations/test_integration_dc_voltage_generation.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/dc_voltage_generations/test_integration_dc_voltage_generation.py`
- sha256: `01445d1804c06f5f6d75aca474cb01092a35724007fc025290ec878b9eba6e07`
- bytes: 6302

````python
"""This module provides test of integration of DcVoltageGeneration."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt import daq

'''from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
    _MockInterpreter,
)
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx,
)'''


class TestIntegrationDcVoltageGeneration(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `DcVoltageGeneration` class.

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
        #_replace_daqmx(_MockInterpreter)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_dc_voltage_generation_generate_only(self):
        """Checks if class `DcVoltageGeneration' can generate with just the initial configurations"""  # noqa: W505, D202, D415 - doc line too long (101 > 100 characters) (auto-generated noqa), No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)

        generation = daq.DcVoltageGeneration()
        generation.initialize(
            analog_output_channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod3/ao0"
        )
        generation.generate_voltage(output_voltages=[0.8])
        generation.close()

    def test_dc_voltage_generation_generate_voltage_with_configure_and_generate_in_loop(
        self,
    ):
        """Checks if class `DcVoltageGeneration' can configure and generate when they are called one after the other."""  # noqa: W505, D202 - doc line too long (120 > 100 characters) (auto-generated noqa), No blank lines allowed after function docstring (auto-generated noqa)

        generation_channel_parameters_1 = daq.VoltageGenerationChannelParameters(
            range_min_volts=-5.0,
            range_max_volts=5.0,
        )
        output_voltages_1 = [2.0, 3.7]

        generation_channel_parameters_2 = daq.VoltageGenerationChannelParameters(
            range_min_volts=-8.0,
            range_max_volts=8.0,
        )
        output_voltages_2 = [6.5, 7.5]

        output_voltages_3 = [1.2, 2.8]

        # Create a list of tuples of VoltageGenerationChannelParameters and output_voltages to test
        parameters_list = []
        parameters_list.append((generation_channel_parameters_1, output_voltages_1))
        parameters_list.append((generation_channel_parameters_2, output_voltages_2))

        generation = daq.DcVoltageGeneration()
        generation.initialize(
            analog_output_channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod3/ao0:1"
        )

        # With the instance of DCVoltageGeneration Initialized, test for configure and generate in loop with different Voltage ranges  # noqa: W505 - doc line too long (133 > 100 characters) (auto-generated noqa)
        for generation_parameters, output_voltages_list in parameters_list:
            generation.configure_all_channels(
                parameters=generation_parameters,
            )
            generation.generate_voltage(output_voltages_list)

        # With the same configuration, test for generate_voltage consecutively with a different set output_voltages  # noqa: W505 - doc line too long (115 > 100 characters) (auto-generated noqa)
        generation.generate_voltage(output_voltages_3)
        generation.close()

    def test_dc_voltage_generation_generate_voltage_with_incorrect_output_voltages(
        self,
    ):
        """Checks if class `DcVoltageGeneration' throws expected error when called with invalid output_voltages"""  # noqa: W505, D202, D415 - doc line too long (114 > 100 characters) (auto-generated noqa), No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)

        generation = daq.DcVoltageGeneration()
        generation.initialize(
            analog_output_channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod3/ao0:1"
        )
        generation.configure_all_channels(
            parameters=daq.DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS,
        )
        # The generate_voltage with valid output_voltages shoudl not throw any error
        generation.generate_voltage([0.5, 0.7])

        # Checks if the expected error is thrown when the size of output_voltages is more than the number of channels.  # noqa: W505 - doc line too long (118 > 100 characters) (auto-generated noqa)
        self.assertRaises(
            ValueError,
            lambda: generation.generate_voltage(output_voltages=[1.0, 2.0, 2.8]),
        )

        # Checks if the expected error is thrown when the size of output_voltages is less than the number of channels.  # noqa: W505 - doc line too long (118 > 100 characters) (auto-generated noqa)
        self.assertRaises(
            ValueError,
            lambda: generation.generate_voltage(output_voltages=[1.5]),
        )

        # Checks if the expected error is thrown when the output_voltages is an empty array.
        self.assertRaises(ValueError, lambda: generation.generate_voltage(output_voltages=[]))
        generation.close()


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_clock_generations/__init__.py sha256=e86764d14be0da556da296f275a42f03265c1acff224d2857394cdf83ad2a5fc bytes=286 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_clock_generations/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_clock_generations/__init__.py`
- sha256: `e86764d14be0da556da296f275a42f03265c1acff224d2857394cdf83ad2a5fc`
- bytes: 286

````python
"""Provides a set of integration tests for nipcbatt.pcbatt_library.digital_clock_generations package"""  # noqa: W505, D415 - doc line too long (103 > 100 characters) (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_clock_generations/test_integration_digital_clock_generation.py sha256=733c961093fd03dacb060dbe63ea07ef4d342d9ed665401d0d856219f1616580 bytes=12837 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_clock_generations/test_integration_digital_clock_generation.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_clock_generations/test_integration_digital_clock_generation.py`
- sha256: `733c961093fd03dacb060dbe63ea07ef4d342d9ed665401d0d856219f1616580`
- bytes: 12837

````python
"""This module provides test of integration of DigitalClockGeneration."""

# pylint: disable=W0611
import importlib
import logging
import sys
import unittest

from varname import nameof
import nipcbatt 
from nipcbatt import daq


# constants used across multiple tests
CHANNEL = "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/ctr0"
TERMINAL = "/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0"


class TestIntegrationDigitalClockGeneration(unittest.TestCase):
    """Defines a test fixture to verify the integration of the
       'DigitalClockGeneration' class

    Args:
        unittest.TestCase: Base class of the unittest framework
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

    def test_integration_digital_clock_generation_counter_channel_expression_is_empty(
        self,
    ):
        """Integration test ensuring that is channel expression
        is empty then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.DigitalClockGeneration() as gen:
            with self.assertRaises(ValueError):
                gen.initialize(counter_channel_expression="", output_terminal_name=TERMINAL)

            gen.close()

    def test_integration_digital_clock_generation_counter_channel_expression_is_none(
        self,
    ):
        """Integration test ensuring that is channel expression
        is null then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.DigitalClockGeneration() as gen:
            with self.assertRaises(ValueError):
                gen.initialize(counter_channel_expression=None, output_terminal_name=TERMINAL)

            gen.close()

    def test_integration_digital_clock_generation_output_terminal_is_empty(
        self,
    ):
        """Integration test ensuring that if terminal
        is empty then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.DigitalClockGeneration() as gen:
            with self.assertRaises(ValueError):
                gen.initialize(counter_channel_expression=CHANNEL, output_terminal_name="")

            gen.close()

    def test_integration_digital_clock_generation_output_terminal_is_none(
        self,
    ):
        """Integration test ensuring that if terminal
        is null then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        gen = daq.DigitalClockGeneration()

        with self.assertRaises(ValueError):
            gen.initialize(counter_channel_expression=CHANNEL, output_terminal_name=None)

        gen.close()

    def test_integration_digital_clock_generation_configure_counter_only(self):
        """Integration test of Digital Clock Generation that ensure an instance
        of DigitalClockGeneration is successfully initialized and configured
        when given correct inputs"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (406 > 100 characters) (auto-generated noqa)

        frequency = 1000.0
        duty_cyc = 0.5
        duration = 10.0

        with daq.DigitalClockGeneration() as gen:
            counter_params = daq.DigitalClockGenerationCounterChannelParameters(
                frequency_hertz=frequency, duty_cycle_ratio=duty_cyc
            )

            timing_params = daq.DigitalClockGenerationTimingParameters(clock_duration_seconds=duration)

            gen.initialize(CHANNEL, TERMINAL)
            gen.configure_counter_channel(parameters=counter_params)
            gen.configure_timing(parameters=timing_params)
            gen.close()

    def test_integration_digital_clock_generation_configure_and_measure(self):
        """Integration test of Digital Frequency Measurement that ensures
        a DigitalClockGeneration isntance is successfully returned
        when given the necessary inputs
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        frequency = 1000.0
        duty_cyc = 0.5
        duration = 10.0

        with daq.DigitalClockGeneration() as gen:
            counter_params = daq.DigitalClockGenerationCounterChannelParameters(
                frequency_hertz=frequency, duty_cycle_ratio=duty_cyc
            )

            timing_params = daq.DigitalClockGenerationTimingParameters(clock_duration_seconds=duration)

            config = daq.DigitalClockGenerationConfiguration(
                counter_channel_parameters=counter_params,
                timing_parameters=timing_params,
            )

            gen.initialize(CHANNEL, TERMINAL)
            actual_data = gen.configure_and_generate(configuration=config)
            gen.close()

            self.assertIsInstance(actual_data, daq.DigitalClockGenerationData)

    def test_integration_digital_clock_generation_negative_vales(self):
        """Integration test of Digital Frequency Measurement that ensures
        a DigitalClockGeneration instantiation fails if given a negative
        value for any parameter
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        frequency = -0.1
        duty_cyc = 0.5
        duration = 10.0

        with daq.DigitalClockGeneration() as gen:
            with self.assertRaises(ValueError):
                counter_params = daq.DigitalClockGenerationCounterChannelParameters(
                    frequency_hertz=frequency, duty_cycle_ratio=duty_cyc
                )

                timing_params = daq.DigitalClockGenerationTimingParameters(
                    clock_duration_seconds=duration
                )

                gen.initialize(CHANNEL, TERMINAL)

        frequency = 1000.0
        duty_cyc = -0.5
        duration = 10.0

        with daq.DigitalClockGeneration() as gen:
            with self.assertRaises(ValueError):
                counter_params = daq.DigitalClockGenerationCounterChannelParameters(
                    frequency_hertz=frequency, duty_cycle_ratio=duty_cyc
                )

                timing_params = daq.DigitalClockGenerationTimingParameters(
                    clock_duration_seconds=duration
                )

                gen.initialize(CHANNEL, TERMINAL)

        frequency = 1000.0
        duty_cyc = 0.5
        duration = -0.1

        with daq.DigitalClockGeneration() as gen:
            with self.assertRaises(ValueError):
                counter_params = daq.DigitalClockGenerationCounterChannelParameters(  # noqa: F841 - local variable 'counter_params' is assigned to but never used (auto-generated noqa)
                    frequency_hertz=frequency, duty_cycle_ratio=duty_cyc
                )

                timing_params = daq.DigitalClockGenerationTimingParameters(  # noqa: F841 - local variable 'timing_params' is assigned to but never used (auto-generated noqa)
                    clock_duration_seconds=duration
                )

                gen.initialize(CHANNEL, TERMINAL)

    def test_integration_digital_clock_generation_duty_cycle(self):
        """Integration test of Digital Frequency Measurement that ensures
        a DigitalClockGeneration instantiation fails if given a value
        greater than 1.0 or is provided for duty cycle
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        frequency = 1000
        duty_cyc = 1.1
        duration = 10.0

        with daq.DigitalClockGeneration() as gen:
            with self.assertRaises(ValueError):
                counter_params = daq.DigitalClockGenerationCounterChannelParameters(  # noqa: F841 - local variable 'counter_params' is assigned to but never used (auto-generated noqa)
                    frequency_hertz=frequency, duty_cycle_ratio=duty_cyc
                )

                timing_params = daq.DigitalClockGenerationTimingParameters(  # noqa: F841 - local variable 'timing_params' is assigned to but never used (auto-generated noqa)
                    clock_duration_seconds=duration
                )

                gen.initialize(CHANNEL, TERMINAL)

    def test_integration_digital_clock_generation_zero_duration(self):
        """Integration test of Digital Frequency Measurement that ensures
        a DigitalClockGeneration instantiation fails if given a value
        of 0 for duration
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        frequency = 1000
        duty_cyc = 0.5
        duration = 0.0

        with daq.DigitalClockGeneration() as gen:
            with self.assertRaises(ValueError):
                counter_params = daq.DigitalClockGenerationCounterChannelParameters(  # noqa: F841 - local variable 'counter_params' is assigned to but never used (auto-generated noqa)
                    frequency_hertz=frequency, duty_cycle_ratio=duty_cyc
                )

                timing_params = daq.DigitalClockGenerationTimingParameters(  # noqa: F841 - local variable 'timing_params' is assigned to but never used (auto-generated noqa)
                    clock_duration_seconds=duration
                )

                gen.initialize(CHANNEL, TERMINAL)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_edge_count_measurements/__init__.py sha256=075e4733dd5b2ee613265bee2512d35ef5b5d68d4908f261670ed29b8d2a9002 bytes=476 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_edge_count_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_edge_count_measurements/__init__.py`
- sha256: `075e4733dd5b2ee613265bee2512d35ef5b5d68d4908f261670ed29b8d2a9002`
- bytes: 476

````python
"""Provides a set of integration tests 
for nipcbatt.pcbatt_library.digital_edge_count_measurements package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (363 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_edge_count_measurements/test_integration_digital_edge_count_measurement.py sha256=4647074b53ec28b24d996fbc978830bb243da5fec718f82a0c5be1b8c8539405 bytes=27600 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_edge_count_measurements/test_integration_digital_edge_count_measurement.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_edge_count_measurements/test_integration_digital_edge_count_measurement.py`
- sha256: `4647074b53ec28b24d996fbc978830bb243da5fec718f82a0c5be1b8c8539405`
- bytes: 27600

````python
"""This module provides test of integration of DigitalEdgeCountMeasurementUsingSoftwareTimer
   and DigitalEdgeCountMeasurementUsingHardwareTimer."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (349 > 100 characters) (auto-generated noqa)

import importlib.metadata
import logging
import sys
import unittest

import nidaqmx
import nidaqmx.constants
from varname import nameof

import nipcbatt
from nipcbatt import daq


class TestIntegrationDigitalEdgeCountMeasurement(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `DigitalEdgeCountMeasurementUsingHardwareTimer` and
    'DigitalEdgeCountMeasurementUsingSoftwareTimer' classes.

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

    # Hardware timer
    def test_integration_test_digital_edge_count_measurement_using_hardware_timer_channel_expression_empty(
        self,
    ):
        """Integration test ensuring that if channel expression is empty then
        initialize() catches the error"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (411 > 100 characters) (auto-generated noqa)

        with daq.DigitalEdgeCountMeasurementUsingHardwareTimer() as measurement:
            with self.assertRaises(ValueError):
                measurement.initialize(
                    measurement_channel_expression="",
                    measurement_input_terminal_name="/TS1_Core/PFI6",
                    timer_channel_expression="TS1_Core/ctr2",
                )

            measurement.close()

    def test_integration_test_digital_edge_count_measurement_using_hardware_timer_channel_expression_is_none(
        self,
    ):
        """Integration test ensuring that if channel expression is None then
        initialize() catches the error"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (411 > 100 characters) (auto-generated noqa)

        with daq.DigitalEdgeCountMeasurementUsingHardwareTimer() as measurement:
            with self.assertRaises(ValueError):
                measurement.initialize(
                    measurement_channel_expression=None,
                    measurement_input_terminal_name="/TS1_Core/PFI6",
                    timer_channel_expression="TS1_Core/ctr2",
                )

            measurement.close()

    def test_integration_test_digital_edge_count_measurement_using_hardware_timer_input_terminal_empty(
        self,
    ):
        """Integration test ensuring that if measurement_input_terminal_name is empty then
        initialize() catches the error"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (411 > 100 characters) (auto-generated noqa)

        with daq.DigitalEdgeCountMeasurementUsingHardwareTimer() as measurement:
            with self.assertRaises(ValueError):
                measurement.initialize(
                    measurement_channel_expression="TS1_Core/ctr1",
                    measurement_input_terminal_name="",
                    timer_channel_expression="TS1_Core/ctr2",
                )

            measurement.close()

    def test_integration_test_digital_edge_count_measurement_using_hardware_timer_input_terminal_is_none(
        self,
    ):
        """Integration test ensuring that if measurement_input_terminal_name is None then
        initialize() catches the error"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (411 > 100 characters) (auto-generated noqa)

        with daq.DigitalEdgeCountMeasurementUsingHardwareTimer() as measurement:
            with self.assertRaises(ValueError):
                measurement.initialize(
                    measurement_channel_expression="TS1_Core/ctr1",
                    measurement_input_terminal_name=None,
                    timer_channel_expression="TS1_Core/ctr2",
                )

            measurement.close()

    def test_integration_test_digital_edge_count_measurement_using_hardware_timer_timer_channel_expression_empty(
        self,
    ):
        """Integration test ensuring that if timer channel expression is empty then
        initialize() catches the error"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (411 > 100 characters) (auto-generated noqa)

        with daq.DigitalEdgeCountMeasurementUsingHardwareTimer() as measurement:
            with self.assertRaises(ValueError):
                measurement.initialize(
                    measurement_channel_expression="TS1_Core/ctr1",
                    measurement_input_terminal_name="/TS1_Core/PFI6",
                    timer_channel_expression="",
                )

            measurement.close()

    def test_integration_test_digital_edge_count_measurement_using_hardware_timer_timer_channel_expression_is_none(
        self,
    ):
        """Integration test ensuring that if channel expression is None then
        initialize() catches the error"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (411 > 100 characters) (auto-generated noqa)

        with daq.DigitalEdgeCountMeasurementUsingHardwareTimer() as measurement:
            with self.assertRaises(ValueError):
                measurement.initialize(
                    measurement_channel_expression="TS1_Core/ctr1",
                    measurement_input_terminal_name="/TS1_Core/PFI6",
                    timer_channel_expression=None,
                )

            measurement.close()

    def test_integration_test_digital_edge_count_measurement_using_hardware_timer_configure_only(
        self,
    ):
        """Integration test of
        daq.pcbatt_library.digital_edge_count_measurements.test_digital_edge_count_measurement_using_hardware_timer.
        DigitalEdgeCountMeasurementUsingHardwareTimer with MeasurementExecutionType.CONFIGURE_ONLY
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.DigitalEdgeCountMeasurementUsingHardwareTimer() as measurement:
            measurement.initialize(
                measurement_channel_expression="TS1_Core/ctr0",
                measurement_input_terminal_name="/TS1_Core/PFI0",
                timer_channel_expression="TS1_Core/ctr2",
            )

            counter_channel_parameters = (
                daq.DigitalEdgeCountMeasurementCounterChannelParameters(
                    edge_type=nidaqmx.constants.Edge.FALLING,
                )
            )
            timing_parameters = daq.DigitalEdgeCountMeasurementTimingParameters(
                edge_counting_duration=0.005,
            )
            trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
                trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
                digital_start_trigger_source="/TS1_Core/PFI6",
                digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
            )
            configuration = daq.DigitalEdgeCountHardwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                counter_channel_parameters=counter_channel_parameters,
                timing_parameters=timing_parameters,
                trigger_parameters=trigger_parameters,
            )
            results = measurement.configure_and_measure(configuration=configuration)
            measurement.close()

            print(f"parameters = {configuration}")
            print(f"results = {results}")
            self.assertIs(None, results)

    def test_integration_test_digital_edge_count_measurement_using_hardware_timer_configure_and_measure(
        self,
    ):
        """Integration test of
        daq.pcbatt_library.digital_edge_count_measurements.test_digital_edge_count_measurement_using_hardware_timer.
        DigitalEdgeCountMeasurementUsingHardwareTimer with MeasurementExecutionType.CONFIGURE_AND_MEASURE
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (105 > 100 characters) (auto-generated noqa)

        with daq.DigitalEdgeCountMeasurementUsingHardwareTimer() as measurement:
            measurement.initialize(
                measurement_channel_expression="TS1_Core/ctr1",
                measurement_input_terminal_name="/TS1_Core/PFI6",
                timer_channel_expression="TS1_Core/ctr2",
            )

            counter_channel_parameters = (
                daq.DigitalEdgeCountMeasurementCounterChannelParameters(
                    edge_type=nidaqmx.constants.Edge.FALLING,
                )
            )
            timing_parameters = daq.DigitalEdgeCountMeasurementTimingParameters(
                edge_counting_duration=0.005,
            )
            trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
                trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
                digital_start_trigger_source="/TS1_Core/PFI0",
                digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
            )
            configuration = daq.DigitalEdgeCountHardwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                counter_channel_parameters=counter_channel_parameters,
                timing_parameters=timing_parameters,
                trigger_parameters=trigger_parameters,
            )
            results = measurement.configure_and_measure(configuration=configuration)
            measurement.close()

            print(f"parameters = {configuration}")
            print(f"results = {results}")
            self.assertIsInstance(results, daq.DigitalEdgeCountMeasurementResultData)

    def test_integration_test_digital_edge_count_measurement_using_hardware_timer_configure_only_and_measure_only(
        self,
    ):
        """Integration test of
        daq.pcbatt_library.digital_edge_count_measurements.test_digital_edge_count_measurement_using_hardware_timer.
        DigitalEdgeCountMeasurementUsingHardwareTimer with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (422 > 100 characters) (auto-generated noqa)

        with daq.DigitalEdgeCountMeasurementUsingHardwareTimer() as measurement:
            measurement.initialize(
                measurement_channel_expression="TS1_Core/ctr1",
                measurement_input_terminal_name="/TS1_Core/PFI6",
                timer_channel_expression="TS1_Core/ctr2",
            )

            counter_channel_parameters = (
                daq.DigitalEdgeCountMeasurementCounterChannelParameters(
                    edge_type=nidaqmx.constants.Edge.FALLING,
                )
            )
            timing_parameters = daq.DigitalEdgeCountMeasurementTimingParameters(
                edge_counting_duration=0.005,
            )
            trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
                trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
                digital_start_trigger_source="/TS1_Core/PFI0",
                digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
            )
            configuration = daq.DigitalEdgeCountHardwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                counter_channel_parameters=counter_channel_parameters,
                timing_parameters=timing_parameters,
                trigger_parameters=trigger_parameters,
            )
            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_ONLY, results = {results}"
            )
            self.assertIs(None, results)

            configuration = daq.DigitalEdgeCountHardwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                counter_channel_parameters=counter_channel_parameters,
                timing_parameters=timing_parameters,
                trigger_parameters=trigger_parameters,
            )
            results = measurement.configure_and_measure(configuration=configuration)
            measurement.close()

            print(
                f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
            )
            self.assertIsInstance(results, daq.DigitalEdgeCountMeasurementResultData)

    # Software timer
    def test_integration_test_digital_edge_count_measurement_using_software_timer_channel_expression_empty(
        self,
    ):
        """Integration test ensuring that if channel expression is empty then
        initialize() catches the error"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (411 > 100 characters) (auto-generated noqa)

        with daq.DigitalEdgeCountMeasurementUsingSoftwareTimer() as measurement:
            with self.assertRaises(ValueError):
                measurement.initialize(
                    measurement_channel_expression="",
                    measurement_input_terminal_name="/TS3_Core/PFI6",
                )

            measurement.close()

    def test_integration_test_digital_edge_count_measurement_using_software_timer_channel_expression_is_none(
        self,
    ):
        """Integration test ensuring that if channel expression is None then
        initialize() catches the error"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (411 > 100 characters) (auto-generated noqa)

        with daq.DigitalEdgeCountMeasurementUsingSoftwareTimer() as measurement:
            with self.assertRaises(ValueError):
                measurement.initialize(
                    measurement_channel_expression=None,
                    measurement_input_terminal_name="/TS3_Core/PFI6",
                )

            measurement.close()

    def test_integration_test_digital_edge_count_measurement_using_software_timer_input_terminal_empty(
        self,
    ):
        """Integration test ensuring that if channel expression is empty then
        initialize() catches the error"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (411 > 100 characters) (auto-generated noqa)

        with daq.DigitalEdgeCountMeasurementUsingSoftwareTimer() as measurement:
            with self.assertRaises(ValueError):
                measurement.initialize(
                    measurement_channel_expression="TS3_Core/ctr1",
                    measurement_input_terminal_name="",
                )

            measurement.close()

    def test_integration_test_digital_edge_count_measurement_using_software_timer_input_terminal_is_none(
        self,
    ):
        """Integration test ensuring that if channel expression is None then
        initialize() catches the error"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (411 > 100 characters) (auto-generated noqa)

        with daq.DigitalEdgeCountMeasurementUsingSoftwareTimer() as measurement:
            with self.assertRaises(ValueError):
                measurement.initialize(
                    measurement_channel_expression="TS3_Core/ctr1",
                    measurement_input_terminal_name=None,
                )

            measurement.close()

    def test_integration_test_digital_edge_count_measurement_using_software_timer_configure_only(
        self,
    ):
        """Integration test of
        daq.pcbatt_library.digital_edge_count_measurements.test_digital_edge_count_measurement_using_software_timer.
        DigitalEdgeCountMeasurementUsingSoftwareTimer with MeasurementExecutionType.CONFIGURE_ONLY
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.DigitalEdgeCountMeasurementUsingSoftwareTimer() as measurement:
            measurement.initialize(
                measurement_channel_expression="TS3_Core/ctr1",
                measurement_input_terminal_name="/TS3_Core/PFI6",
            )

            counter_channel_parameters = (
                daq.DigitalEdgeCountMeasurementCounterChannelParameters(
                    edge_type=nidaqmx.constants.Edge.FALLING,
                )
            )
            timing_parameters = daq.DigitalEdgeCountMeasurementTimingParameters(
                edge_counting_duration=0.005,
            )
            configuration = daq.DigitalEdgeCountSoftwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                counter_channel_parameters=counter_channel_parameters,
                timing_parameters=timing_parameters,
            )
            results = measurement.configure_and_measure(
                configuration=configuration,
            )
            measurement.close()

            print(f"parameters = {configuration}")
            print(f"results = {results}")
            self.assertIs(None, results)

    def test_integration_test_digital_edge_count_measurement_using_software_timer_configure_and_measure(
        self,
    ):
        """Integration test of
        daq.pcbatt_library.digital_edge_count_measurements.test_digital_edge_count_measurement_using_software_timer.
        DigitalEdgeCountMeasurementUsingSoftwareTimer with MeasurementExecutionType.CONFIGURE_AND_MEASURE
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (105 > 100 characters) (auto-generated noqa)

        with daq.DigitalEdgeCountMeasurementUsingSoftwareTimer() as measurement:
            measurement.initialize(
                measurement_channel_expression="TS3_Core/ctr1",
                measurement_input_terminal_name="/TS3_Core/PFI6",
            )

            counter_channel_parameters = (
                daq.DigitalEdgeCountMeasurementCounterChannelParameters(
                    edge_type=nidaqmx.constants.Edge.FALLING,
                )
            )
            timing_parameters = daq.DigitalEdgeCountMeasurementTimingParameters(
                edge_counting_duration=0.005,
            )
            configuration = daq.DigitalEdgeCountSoftwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                counter_channel_parameters=counter_channel_parameters,
                timing_parameters=timing_parameters,
            )
            results = measurement.configure_and_measure(configuration=configuration)
            measurement.close()

            print(f"parameters = {configuration}")
            print(f"results = {results}")
            self.assertIsInstance(results, daq.DigitalEdgeCountMeasurementResultData)

    def test_integration_test_digital_edge_count_measurement_using_software_timer_configure_only_and_measure_only(
        self,
    ):
        """Integration test of
        daq.pcbatt_library.digital_edge_count_measurements.test_digital_edge_count_measurement_using_software_timer.
        DigitalEdgeCountMeasurementUsingSoftwareTimer with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (422 > 100 characters) (auto-generated noqa)

        with daq.DigitalEdgeCountMeasurementUsingSoftwareTimer() as measurement:
            measurement.initialize(
                measurement_channel_expression="TS3_Core/ctr1",
                measurement_input_terminal_name="/TS3_Core/PFI6",
            )
            counter_channel_parameters = (
                daq.DigitalEdgeCountMeasurementCounterChannelParameters(
                    edge_type=nidaqmx.constants.Edge.FALLING,
                )
            )
            timing_parameters = daq.DigitalEdgeCountMeasurementTimingParameters(
                edge_counting_duration=0.005,
            )
            configuration = daq.DigitalEdgeCountSoftwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                counter_channel_parameters=counter_channel_parameters,
                timing_parameters=timing_parameters,
            )
            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_ONLY, results = {results}"
            )
            self.assertIs(None, results)

            configuration = daq.DigitalEdgeCountSoftwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                counter_channel_parameters=counter_channel_parameters,
                timing_parameters=timing_parameters,
            )
            results = measurement.configure_and_measure(configuration=configuration)
            measurement.close()

            print(
                f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
            )
            self.assertIsInstance(results, daq.DigitalEdgeCountMeasurementResultData)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_frequency_measurements/__init__.py sha256=4a7bcaa355c7022379ef4157cdd66ca964320a0da994050a0eb92a39990059f6 bytes=475 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_frequency_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_frequency_measurements/__init__.py`
- sha256: `4a7bcaa355c7022379ef4157cdd66ca964320a0da994050a0eb92a39990059f6`
- bytes: 475

````python
"""Provides a set of integration tests 
for nipcbatt.pcbatt_library.digital_frequency_measurements package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (362 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_frequency_measurements/test_integration_digital_frequency_measurement.py sha256=bc54497bea69b6f86e876982def3b57b53fc9eeab82e5f2df69c3b61990e7231 bytes=11889 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_frequency_measurements/test_integration_digital_frequency_measurement.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_frequency_measurements/test_integration_digital_frequency_measurement.py`
- sha256: `bc54497bea69b6f86e876982def3b57b53fc9eeab82e5f2df69c3b61990e7231`
- bytes: 11889

````python
"""This module provides test of integration of DigitalFrequencyMeasurement."""

import importlib
import logging
import sys
import unittest

from varname import nameof

import nipcbatt 
from nipcbatt import daq

# constants used across multiple tests
CHANNEL = "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/ctr0"
TERMINAL = "/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0"


class TestIntegrationDigitalFrequencyMeasurement(unittest.TestCase):
    """Defines a test fixture to verify the integration of the
       'DigitalFrequencyMeasurment' class

    Args:
        unittest.TestCase: Base class of the unittest framework
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

    def test_integration_digital_frequency_measurement_channel_expression_is_empty(
        self,
    ):
        """Integration test ensuring that is channel expression
        is empty then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.DigitalFrequencyMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(channel_expression="", input_terminal_name=TERMINAL)

            meas.close()

    def test_integration_digital_frequency_measurement_channel_expression_is_none(self):
        """Integration test ensuring that is channel expression
        is null then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.DigitalFrequencyMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(channel_expression=None, input_terminal_name=TERMINAL)

            meas.close()

    def test_integration_digital_frequency_measurement_input_terminal_is_empty(self):
        """Integration test ensuring that is input terminal
        is empty then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.DigitalFrequencyMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(
                    channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/ctr0",
                    input_terminal_name="",
                )

            meas.close()

    def test_integration_digital_frequency_measurement_input_terminal_is_none(self):
        """Integration test ensuring that is input terminal
        is null then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.DigitalFrequencyMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(
                    channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/ctr0",
                    input_terminal_name=None,
                )

            meas.close()

    def test_integration_digital_frequency_measurement_configure_counter_channel_only(
        self,
    ):
        """Integration test of Digital Frequency Measurement that ensures
        a DigitalFrequencyMeasurement is successfully configured
        when given the necessary inputs
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        min_frequency = 1.0
        max_frequency = 10000000.0
        input_divisor = 10
        measurement_duration = 1.0

        with daq.DigitalFrequencyMeasurement() as meas:
            range_parameters = daq.DigitalFrequencyRangeParameters(min_frequency, max_frequency)
            counter_channel_parameters = daq.DigitalFrequencyMeasurementCounterChannelParameters(
                range_parameters, input_divisor, measurement_duration
            )

            meas.initialize(CHANNEL, TERMINAL)
            meas.configure_counter_channel(counter_channel_parameters)
            meas.close()

    def test_integration_digital_frequency_measurement_configure_and_measure(self):
        """Integration test of Digital Frequency Measurement that ensures
        a DigitalFrequencyMeasurementResultData is successfully returned
        when given the necessary inputs
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        min_frequency = 1.0
        max_frequency = 10000000.0
        input_divisor = 10
        measurement_duration = 1.0

        with daq.DigitalFrequencyMeasurement() as meas:
            range_parameters = daq.DigitalFrequencyRangeParameters(min_frequency, max_frequency)
            counter_channel_parameters = daq.DigitalFrequencyMeasurementCounterChannelParameters(
                range_parameters, input_divisor, measurement_duration
            )

            meas.initialize(CHANNEL, TERMINAL)

            cfg = daq.DigitalFrequencyMeasurementConfiguration(counter_channel_parameters)
            results = meas.configure_and_measure(cfg)

            self.assertIsInstance(results, daq.DigitalFrequencyMeasurementResultData)

            meas.close()

    def test_integration_digital_frequency_measurement_negative_frequency(
        self,
    ):
        """Integration test of Digital Frequency Measurement that ensures
        an error is thrown when a negative minimum frequency is used
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        min_frequency = -0.1
        max_frequency = 10000000.0
        input_divisor = 10
        measurement_duration = 1.0

        with daq.DigitalFrequencyMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(
                    channel_expression=CHANNEL,
                    input_terminal_name=TERMINAL,
                )

                range_parameters = daq.DigitalFrequencyRangeParameters(min_frequency, max_frequency)
                counter_channel_parameters = daq.DigitalFrequencyMeasurementCounterChannelParameters(  # noqa: F841 - local variable 'counter_channel_parameters' is assigned to but never used (auto-generated noqa)
                    range_parameters, input_divisor, measurement_duration
                )

    def test_integration_digital_frequency_measurement_zero_divisor(
        self,
    ):
        """Integration test of Digital Frequency Measurement that ensures
        an error is thrown when 0 is used for the input divisor
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        min_frequency = -0.1
        max_frequency = 10000000.0
        input_divisor = 0
        measurement_duration = 1.0

        with daq.DigitalFrequencyMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(
                    channel_expression=CHANNEL,
                    input_terminal_name=TERMINAL,
                )

                range_parameters = daq.DigitalFrequencyRangeParameters(min_frequency, max_frequency)
                counter_channel_parameters = daq.DigitalFrequencyMeasurementCounterChannelParameters(  # noqa: F841 - local variable 'counter_channel_parameters' is assigned to but never used (auto-generated noqa)
                    range_parameters, input_divisor, measurement_duration
                )

    def test_integration_digital_frequency_measurement_zero_duration(
        self,
    ):
        """Integration test of Digital Frequency Measurement that ensures
        an error is thrown when 0 is used for the measurement duration
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        min_frequency = 1.0
        max_frequency = 10000000.0
        input_divisor = 10
        measurement_duration = 0.0

        with daq.DigitalFrequencyMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(
                    channel_expression=CHANNEL,
                    input_terminal_name=TERMINAL,
                )

                range_parameters = daq.DigitalFrequencyRangeParameters(min_frequency, max_frequency)
                counter_channel_parameters = daq.DigitalFrequencyMeasurementCounterChannelParameters(  # noqa: F841 - local variable 'counter_channel_parameters' is assigned to but never used (auto-generated noqa)
                    range_parameters, input_divisor, measurement_duration
                )


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_pulse_generations/__init__.py sha256=8424aafa9d9fc0b39e9c262941498588bab9286b8a545561c02b2827142fbed0 bytes=469 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_pulse_generations/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_pulse_generations/__init__.py`
- sha256: `8424aafa9d9fc0b39e9c262941498588bab9286b8a545561c02b2827142fbed0`
- bytes: 469

````python
"""Provides a set of integration tests
for nipcbatt.pcbatt_library.digital_pulse_generations package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (357 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_pulse_generations/test_integration_digital_pulse_generation.py sha256=d36b08767800b2fae2f5b51ee9e778cf273b5d4cb76bd809fcdd32cf6389f228 bytes=10662 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_pulse_generations/test_integration_digital_pulse_generation.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_pulse_generations/test_integration_digital_pulse_generation.py`
- sha256: `d36b08767800b2fae2f5b51ee9e778cf273b5d4cb76bd809fcdd32cf6389f228`
- bytes: 10662

````python
"""This module provides test of integration of DigitalPulseGeneration."""

import importlib
import logging
import sys
import unittest

import nidaqmx.constants
import nidaqmx.stream_writers  # noqa: F401 - 'nidaqmx.stream_writers' imported but unused (auto-generated noqa)
import numpy as np  # noqa: F401 - 'numpy as np' imported but unused (auto-generated noqa)
from varname import nameof

import nipcbatt 
from nipcbatt import daq

# constants used across multiple tests
CHANNEL = "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/ctr0"
TERMINAL = "/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0"


class TestIntegrationDigitalPulseGeneration(unittest.TestCase):
    """Defines a test fixture to verify the integration of the
       'DigitalPulseGeneration' class

    Args:
        unittest (_type_): _description_
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

    def test_integration_digital_pulse_generation_channel_expression_empty(self):
        """Integration test ensuring that if channel expression is empty then
        initialize() catches the error"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (411 > 100 characters) (auto-generated noqa)

        with daq.DigitalPulseGeneration() as gen:
            with self.assertRaises(ValueError):
                gen.initialize(channel_expression="", output_terminal_name=TERMINAL)

            gen.close()

    def test_integration_digital_pulse_generation_channel_expression_is_none(self):
        """Integration test ensuring that if channel expression is None then
        initialize() catches the error"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (411 > 100 characters) (auto-generated noqa)

        with daq.DigitalPulseGeneration() as gen:
            with self.assertRaises(ValueError):
                gen.initialize(channel_expression=None, output_terminal_name=TERMINAL)

            gen.close()

    def test_integration_digital_pulse_generation_terminal_empty(self):
        """Integration test ensuring that if input terminal
        is empty then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.DigitalPulseGeneration() as gen:
            with self.assertRaises(ValueError):
                gen.initialize(channel_expression=CHANNEL, output_terminal_name="")

            gen.close()

    def test_integration_digital_pulse_generation_terminal_is_none(self):
        """Integration test ensuring that if input terminal
        is null then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.DigitalPulseGeneration() as gen:
            with self.assertRaises(ValueError):
                gen.initialize(channel_expression=CHANNEL, output_terminal_name=None)

            gen.close()

    def test_integration_digital_pulse_generation_configure_and_generate(self):
        """Integration test of Digital Pulse Generation that ensures an instance
        of DigitalPulseGeneration is successfully executed when configure
        and measure is performed"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (405 > 100 characters) (auto-generated noqa)

        t_low = 0.1
        t_high = 0.1
        state_idle = daq.ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        p_count = 10

        channel_params = daq.DigitalPulseGenerationCounterChannelParameters(state_idle, t_low, t_high)
        timing_params = daq.DigitalPulseGenerationTimingParameters(p_count)
        config = daq.DigitalPulseGenerationConfiguration(channel_params, timing_params)

        with daq.DigitalPulseGeneration() as gen:
            gen.initialize(CHANNEL, TERMINAL)
            gen_data = gen.configure_and_generate(config)
            gen.close()

        self.assertIsInstance(gen_data, daq.DigitalPulseGenerationData)

    def test_integration_digital_pulse_generation_negative_values(self):
        """Integration test of Digital Pulse Generation that ensures
        a DigitalPulseGeneration instantiation fails if given a negative
        value for any parameter
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        t_low = -0.1
        t_high = 0.1
        state_idle = daq.ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        p_count = 10

        with daq.DigitalPulseGeneration() as gen:
            with self.assertRaises(ValueError):
                channel_params = daq.DigitalPulseGenerationCounterChannelParameters(
                    state_idle, t_low, t_high
                )

                timing_params = daq.DigitalPulseGenerationTimingParameters(p_count)
                config = daq.DigitalPulseGenerationConfiguration(channel_params, timing_params)

                gen.initialize(CHANNEL, TERMINAL)
                gen.configure_and_generate(config)
                gen.close()

        t_low = 0.1
        t_high = -0.1
        state_idle = daq.ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        p_count = 10

        with daq.DigitalPulseGeneration() as gen:
            with self.assertRaises(ValueError):
                channel_params = daq.DigitalPulseGenerationCounterChannelParameters(
                    state_idle, t_low, t_high
                )

                timing_params = daq.DigitalPulseGenerationTimingParameters(p_count)
                config = daq.DigitalPulseGenerationConfiguration(channel_params, timing_params)

                gen.initialize(CHANNEL, TERMINAL)
                gen.configure_and_generate(config)
                gen.close()

        t_low = 0.1
        t_high = 0.1
        state_idle = daq.ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        p_count = -10

        with daq.DigitalPulseGeneration() as gen:
            with self.assertRaises(ValueError):
                channel_params = daq.DigitalPulseGenerationCounterChannelParameters(
                    state_idle, t_low, t_high
                )

                timing_params = daq.DigitalPulseGenerationTimingParameters(p_count)
                config = daq.DigitalPulseGenerationConfiguration(channel_params, timing_params)

                gen.initialize(CHANNEL, TERMINAL)
                gen.configure_and_generate(config)
                gen.close()

    def test_integration_digital_pulse_generation_no_idle_state_defined(self):
        """Integration test of Digital Pulse Generation that ensures an instance
        of DigitalPulseGeneration is successfully executed when the user does not
        define an idle state with otherwise valid data"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (427 > 100 characters) (auto-generated noqa)

        t_low = 0.1
        t_high = 0.1
        p_count = 10

        with daq.DigitalPulseGeneration() as gen:
            channel_params = daq.DigitalPulseGenerationCounterChannelParameters(
                low_time_seconds=t_low, high_time_seconds=t_high
            )

            timing_params = daq.DigitalPulseGenerationTimingParameters(p_count)
            config = daq.DigitalPulseGenerationConfiguration(channel_params, timing_params)

            gen.initialize(CHANNEL, TERMINAL)
            gen_data = gen.configure_and_generate(config)
            gen.close()

            self.assertIsInstance(gen_data, daq.DigitalPulseGenerationData)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_pwm_measurements/__init__.py sha256=7e634ad0331ae1cd17778e4a6166c318148a0a1f0634b63d7030ab67b41c4e73 bytes=468 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_pwm_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_pwm_measurements/__init__.py`
- sha256: `7e634ad0331ae1cd17778e4a6166c318148a0a1f0634b63d7030ab67b41c4e73`
- bytes: 468

````python
"""Provides a set of integration tests
for nipcbatt.pcbatt_library.digital_pwm_measurements package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (356 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_pwm_measurements/test_integration_digital_pwm_measurement.py sha256=9645ab2cb4a7fc83c907fc7a2c03007464f0aedab53edf4ce586c36ad94da073 bytes=17581 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_pwm_measurements/test_integration_digital_pwm_measurement.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/digital_pwm_measurements/test_integration_digital_pwm_measurement.py`
- sha256: `9645ab2cb4a7fc83c907fc7a2c03007464f0aedab53edf4ce586c36ad94da073`
- bytes: 17581

````python
"""This module provides test of integration of DigitalPwmMeasurement."""

import importlib
import logging
import sys
import unittest

import numpy as np  # noqa: F401 - 'numpy as np' imported but unused (auto-generated noqa)
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType

import nipcbatt 
from nipcbatt import daq

# constants used across multiple tests
CHANNEL = "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/ctr0"
TERMINAL = "/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0"


class TestIntegrationDigitalPwmMeasurement(unittest.TestCase):
    """Defines a test fixture to verify the integration of the
       'DigitalPwmMeasurment' class

    Args:
        unittest.TestCase: Base class of the unittest framework
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

    def test_integration_digital_pwm_measurement_channel_expression_empty(self):
        """Integration test ensuring that if channel expression
        is empty then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.DigitalPwmMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(channel_expression="", input_terminal_name=TERMINAL)

            meas.close()

    def test_integration_digital_pwm_measurement_channel_expression_is_none(self):
        """Integration test ensuring that if channel expression
        is null then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.DigitalPwmMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(channel_expression=None, input_terminal_name=TERMINAL)

            meas.close()

    def test_integration_digital_pwm_measurement_input_terminal_empty(self):
        """Integration test ensuring that if input terminal
        is empty then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.DigitalPwmMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(channel_expression=CHANNEL, input_terminal_name="")

            meas.close()

    def test_integration_digital_pwm_measurement_input_terminal_is_none(self):
        """Integration test ensuring that if input terminal
        is null then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.DigitalPwmMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(channel_expression=CHANNEL, input_terminal_name=None)

            meas.close()

    def test_integration_digital_pwm_measurement_configure_only(self):
        """Integration test of Digital PWM Measurement that ensures an instance
        of DigitalPwmMeasurement is successfully initialized and configured
        given correct inputs"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (401 > 100 characters) (auto-generated noqa)

        min_semiperiod = 50.0e-9
        max_semiperiod = 50.0
        cycles = 100
        edge = daq.ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE
        execution_type = MeasurementExecutionType.CONFIGURE_ONLY

        range_params = daq.DigitalPwmMeasurementRangeParameters(min_semiperiod, max_semiperiod)

        timing_params = daq.DigitalPwmMeasurementTimingParameters(cycles)

        counter_channel_params = daq.DigitalPwmMeasurementCounterChannelParameters(
            range_params, timing_params, edge
        )

        config = daq.DigitalPwmMeasurementConfiguration(counter_channel_params, execution_type)

        with daq.DigitalPwmMeasurement() as meas:
            meas.initialize(CHANNEL, TERMINAL)
            result_data = meas.configure_and_measure(configuration=config)
            meas.close()

        self.assertIsNone(result_data)

    def test_integration_digital_pwm_measurement_measure_only(self):
        """Integration test of Digital PWM measurement that ensures an instance
        of DigitalPwmMeasurement is successfully executed when measure only
        is selected as the execution option"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (416 > 100 characters) (auto-generated noqa)

        min_semiperiod = 50.0e-9
        max_semiperiod = 50.0
        cycles = 100
        edge = daq.ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE
        execution_type = MeasurementExecutionType.MEASURE_ONLY

        range_params = daq.DigitalPwmMeasurementRangeParameters(min_semiperiod, max_semiperiod)
        timing_params = daq.DigitalPwmMeasurementTimingParameters(cycles)
        counter_channel_params = daq.DigitalPwmMeasurementCounterChannelParameters(
            range_params, timing_params, edge
        )
        config = daq.DigitalPwmMeasurementConfiguration(counter_channel_params, execution_type)

        with daq.DigitalPwmMeasurement() as meas:
            meas.initialize(CHANNEL, TERMINAL)
            result_data = meas.configure_and_measure(configuration=config)
            meas.close()

        self.assertIsInstance(result_data, daq.DigitalPwmMeasurementResultData)

    def test_integration_digital_pwm_measurement_both_configure_and_measure(self):
        """Integration test of Digital PWM measurement that ensures an instance
        of DigitalPwmMeasurement is successfully executed when both configure
        and measure is selected as the execution option"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (351 > 100 characters) (auto-generated noqa)
        min_semiperiod = 50.0e-9
        max_semiperiod = 50.0
        cycles = 100
        edge = daq.ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE
        execution_type = MeasurementExecutionType.CONFIGURE_AND_MEASURE

        range_params = daq.DigitalPwmMeasurementRangeParameters(min_semiperiod, max_semiperiod)
        timing_params = daq.DigitalPwmMeasurementTimingParameters(cycles)
        counter_channel_params = daq.DigitalPwmMeasurementCounterChannelParameters(
            range_params, timing_params, edge
        )
        config = daq.DigitalPwmMeasurementConfiguration(counter_channel_params, execution_type)

        with daq.DigitalPwmMeasurement() as meas:
            meas.initialize(CHANNEL, TERMINAL)
            result_data = meas.configure_and_measure(configuration=config)
            meas.close()

        self.assertIsInstance(result_data, daq.DigitalPwmMeasurementResultData)

    def test_integration_digital_pwm_negative_values(self):
        """Integration test of Digital Pwm measurement that ensures
        a DigitalPwmMeasurement instantiation fails if given a negative
        value for any parameter
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        min_semiperiod = -50.0e-9
        max_semiperiod = 50.0
        cycles = 10
        edge = daq.ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE
        execution_type = MeasurementExecutionType.CONFIGURE_AND_MEASURE

        with daq.DigitalPwmMeasurement() as meas:
            with self.assertRaises(ValueError):
                range_params = daq.DigitalPwmMeasurementRangeParameters(min_semiperiod, max_semiperiod)
                timing_params = daq.DigitalPwmMeasurementTimingParameters(cycles)
                counter_channel_params = daq.DigitalPwmMeasurementCounterChannelParameters(
                    range_params, timing_params, edge
                )
                config = daq.DigitalPwmMeasurementConfiguration(counter_channel_params, execution_type)

                meas.initialize(CHANNEL, TERMINAL)
                meas.configure_and_measure(config)

        min_semiperiod = 50.0e-9
        max_semiperiod = -50.0
        cycles = 10
        edge = daq.ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE
        execution_type = MeasurementExecutionType.CONFIGURE_AND_MEASURE

        with daq.DigitalPwmMeasurement() as meas:
            with self.assertRaises(ValueError):
                range_params = daq.DigitalPwmMeasurementRangeParameters(min_semiperiod, max_semiperiod)
                timing_params = daq.DigitalPwmMeasurementTimingParameters(cycles)
                counter_channel_params = daq.DigitalPwmMeasurementCounterChannelParameters(
                    range_params, timing_params, edge
                )
                config = daq.DigitalPwmMeasurementConfiguration(counter_channel_params, execution_type)

                meas.initialize(CHANNEL, TERMINAL)
                meas.configure_and_measure(config)

        min_semiperiod = 50.0e-9
        max_semiperiod = 50.0
        cycles = -10
        edge = daq.ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE
        execution_type = MeasurementExecutionType.CONFIGURE_AND_MEASURE

        with daq.DigitalPwmMeasurement() as meas:
            with self.assertRaises(ValueError):
                range_params = daq.DigitalPwmMeasurementRangeParameters(min_semiperiod, max_semiperiod)
                timing_params = daq.DigitalPwmMeasurementTimingParameters(cycles)
                counter_channel_params = daq.DigitalPwmMeasurementCounterChannelParameters(
                    range_params, timing_params, edge
                )
                config = daq.DigitalPwmMeasurementConfiguration(counter_channel_params, execution_type)

                meas.initialize(CHANNEL, TERMINAL)
                meas.configure_and_measure(config)

    def test_integration_digital_pwm_measurement_no_edge_defined(self):
        """Integration test of Digital PWM measurement that ensures an instance
        of DigitalPwmMeasurement is successfully executed when the user does not
        define an edge"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (318 > 100 characters) (auto-generated noqa)
        min_semiperiod = 50.0e-9
        max_semiperiod = 50.0
        cycles = 100
        execution_type = MeasurementExecutionType.CONFIGURE_AND_MEASURE

        range_params = daq.DigitalPwmMeasurementRangeParameters(min_semiperiod, max_semiperiod)
        timing_params = daq.DigitalPwmMeasurementTimingParameters(cycles)
        counter_channel_params = daq.DigitalPwmMeasurementCounterChannelParameters(
            range_params, timing_params
        )
        config = daq.DigitalPwmMeasurementConfiguration(counter_channel_params, execution_type)

        with daq.DigitalPwmMeasurement() as meas:
            meas.initialize(CHANNEL, TERMINAL)
            result_data = meas.configure_and_measure(configuration=config)
            meas.close()

        self.assertIsInstance(result_data, daq.DigitalPwmMeasurementResultData)

    def test_integration_digital_pwm_measurement_no_cycles_defined(self):
        """Integration test of Digital PWM measurement that ensures an instance
        of DigitalPwmMeasurement is successfully executed when the user does not
        define a value for cycles"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (329 > 100 characters) (auto-generated noqa)
        min_semiperiod = 50.0e-9
        max_semiperiod = 50.0
        edge = daq.ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE
        execution_type = MeasurementExecutionType.CONFIGURE_AND_MEASURE

        range_params = daq.DigitalPwmMeasurementRangeParameters(min_semiperiod, max_semiperiod)
        timing_params = daq.DigitalPwmMeasurementTimingParameters()
        counter_channel_params = daq.DigitalPwmMeasurementCounterChannelParameters(
            range_params, timing_params, edge
        )
        config = daq.DigitalPwmMeasurementConfiguration(counter_channel_params, execution_type)

        with daq.DigitalPwmMeasurement() as meas:
            meas.initialize(CHANNEL, TERMINAL)
            result_data = meas.configure_and_measure(configuration=config)
            meas.close()

        self.assertIsInstance(result_data, daq.DigitalPwmMeasurementResultData)

    def test_integration_digital_pwm_measurement_no_execution_type_defined(self):
        """Integration test of Digital PWM measurement that ensures an instance
        of DigitalPwmMeasurement is successfully executed when the user does not
        define a value for execution type"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (337 > 100 characters) (auto-generated noqa)
        min_semiperiod = 50.0e-9
        max_semiperiod = 50.0
        cycles = 100
        edge = daq.ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE

        range_params = daq.DigitalPwmMeasurementRangeParameters(min_semiperiod, max_semiperiod)
        timing_params = daq.DigitalPwmMeasurementTimingParameters(cycles)
        counter_channel_params = daq.DigitalPwmMeasurementCounterChannelParameters(
            range_params, timing_params, edge
        )
        config = daq.DigitalPwmMeasurementConfiguration(counter_channel_params)

        with daq.DigitalPwmMeasurement() as meas:
            meas.initialize(CHANNEL, TERMINAL)
            result_data = meas.configure_and_measure(configuration=config)
            meas.close()

        self.assertIsInstance(result_data, daq.DigitalPwmMeasurementResultData)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dmm_scan/__init__.py sha256=f9609a8283dad76fa5bee2243382d0fa9205def568af5fdabc4d597645a6fc80 bytes=62 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dmm_scan/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/dmm_scan/__init__.py`
- sha256: `f9609a8283dad76fa5bee2243382d0fa9205def568af5fdabc4d597645a6fc80`
- bytes: 62

````python
"""Provides integration tests for DMM Scan functionality."""
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dmm_scan/test_integration_dmm_scan_pmps_16V_15C.py sha256=777d9882c85d592df345deb5ff84272e7ec777d811a01533d014545c94a430e0 bytes=21009 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dmm_scan/test_integration_dmm_scan_pmps_16V_15C.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/dmm_scan/test_integration_dmm_scan_pmps_16V_15C.py`
- sha256: `777d9882c85d592df345deb5ff84272e7ec777d811a01533d014545c94a430e0`
- bytes: 21009

````python
# pylint: disable=C0301
"""This module provides comprehensive integration tests for DmmScanPMPS complete workflow."""

import importlib.metadata
import logging
import sys
import unittest
from io import StringIO
from unittest.mock import MagicMock, patch

from varname import nameof

from nipcbatt.pcbatt_library.dmm_scan.dmm_scan_pmps_16V_15C import (
    DmmScanPMPS,
    ScanResources,
    MeasurementResult,
)


class TestIntegrationDmmScanPMPSWorkflow(unittest.TestCase):
    """Defines a test fixture that checks the complete DmmScanPMPS workflow.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        """Set up test fixtures."""
        self.dmm_scan = DmmScanPMPS()

    def tearDown(self):
        """Tear down test fixtures."""
        pass

    @classmethod
    def setUpClass(cls):
        """Set up class-level fixtures."""
        print("Setup test fixture: TestIntegrationDmmScanPMPSWorkflow")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        """Tear down class-level fixtures."""
        print("Teardown fixture: TestIntegrationDmmScanPMPSWorkflow")

    @patch("nipcbatt.switch.StaticDigitalPathGeneration")
    @patch("nipcbatt.dmm.MixedMeasurement")
    def test_integration_complete_scan_workflow_with_single_measurement(
        self, mock_dmm_class, mock_switch_class
    ):
        """Integration test verifying complete scan workflow with single measurement."""
        mock_mux_instance = MagicMock()
        mock_shunt_instance = MagicMock()
        mock_dmm_instance = MagicMock()

        mock_switch_class.side_effect = [mock_mux_instance, mock_shunt_instance]
        mock_dmm_class.return_value = mock_dmm_instance

        mock_measurement = MagicMock()
        mock_measurement.measurement = {
            "Measured_Value": 5.125,
            "Unit": "V (dc)",
            "Formatted_Measurement": "5.125V (dc)"
        }
        mock_measurement.dmm_execution_settings = {
            "Function": "DC_VOLTS",
            "Range": 10,
            "Digits_Resolution": 5.5,
            "Aperture_Time(s)": "1m",
            "Settle_Time(s)": "1m",
            "Minimum_Frequency(Hz)": 40.0,
        }

        mock_dmm_instance.acquire_measurement.return_value = mock_measurement

        scan_resources = self.dmm_scan.initialize(
            mux_resource_name="Sim_MUX",
            dmm_resource_name="Sim_DMM",
            powerline_freq=50,
        )

        from nipcbatt import dmm as dmm_module
        scan_configuration = [
            [0, dmm_module.MixedRangeAndFunctions.DC_Voltage_Auto_Range, dmm_module.ResolutionInDigits.DIGITS_5_5],
        ]

        result = self.dmm_scan.configure_and_measure(
            resource_handles=scan_resources,
            scan_configuration=scan_configuration,
            verbose=False,
        )

        self.assertIsInstance(result, MeasurementResult)
        self.assertEqual(len(result.formatted_measurements), 1)
        self.assertEqual(len(result.raw_measurements), 1)
        self.assertEqual(len(result.execution_settings), 1)
        self.assertGreater(result.scan_time, 0)

        self.dmm_scan.close(scan_resources)

    @patch("nipcbatt.switch.StaticDigitalPathGeneration")
    @patch("nipcbatt.dmm.MixedMeasurement")
    def test_integration_scan_with_multiple_channels(
        self, mock_dmm_class, mock_switch_class
    ):
        """Integration test verifying scan with multiple channels."""
        mock_mux_instance = MagicMock()
        mock_shunt_instance = MagicMock()
        mock_dmm_instance = MagicMock()

        mock_switch_class.side_effect = [mock_mux_instance, mock_shunt_instance]
        mock_dmm_class.return_value = mock_dmm_instance

        mock_measurement = MagicMock()
        mock_measurement.measurement = {
            "Measured_Value": 0.0,
            "Unit": "V (dc)",
            "Formatted_Measurement": "0V (dc)"
        }
        mock_measurement.dmm_execution_settings = {
            "Function": "DC_VOLTS",
            "Range": 10,
            "Digits_Resolution": 5.5,
        }

        mock_dmm_instance.acquire_measurement.return_value = mock_measurement

        scan_resources = self.dmm_scan.initialize(powerline_freq=50)

        from nipcbatt import dmm as dmm_module
        scan_configuration = [
            [i, dmm_module.MixedRangeAndFunctions.DC_Voltage_Auto_Range, dmm_module.ResolutionInDigits.DIGITS_5_5]
            for i in range(5)
        ]

        result = self.dmm_scan.configure_and_measure(
            resource_handles=scan_resources,
            scan_configuration=scan_configuration,
            verbose=False,
        )

        self.assertEqual(len(result.formatted_measurements), 5)
        self.assertEqual(len(result.raw_measurements), 5)
        self.assertEqual(len(result.execution_settings), 5)

        self.dmm_scan.close(scan_resources)

    @patch("nipcbatt.switch.StaticDigitalPathGeneration")
    @patch("nipcbatt.dmm.MixedMeasurement")
    def test_integration_scan_with_voltage_measurement(
        self, mock_dmm_class, mock_switch_class
    ):
        """Integration test verifying scan with voltage measurements."""
        mock_mux_instance = MagicMock()
        mock_shunt_instance = MagicMock()
        mock_dmm_instance = MagicMock()

        mock_switch_class.side_effect = [mock_mux_instance, mock_shunt_instance]
        mock_dmm_class.return_value = mock_dmm_instance

        mock_measurement = MagicMock()
        mock_measurement.measurement = {
            "Measured_Value": 5.0,
            "Unit": "V (dc)",
            "Formatted_Measurement": "5V (dc)"
        }
        mock_measurement.dmm_execution_settings = {
            "Function": "DC_VOLTS",
            "Range": 100,
            "Digits_Resolution": 5.5,
        }

        mock_dmm_instance.acquire_measurement.return_value = mock_measurement

        scan_resources = self.dmm_scan.initialize()

        from nipcbatt import dmm as dmm_module
        scan_configuration = [
            [0, dmm_module.MixedRangeAndFunctions.DC_100V, dmm_module.ResolutionInDigits.DIGITS_5_5],
            [1, dmm_module.MixedRangeAndFunctions.DC_100V, dmm_module.ResolutionInDigits.DIGITS_5_5],
        ]

        result = self.dmm_scan.configure_and_measure(
            resource_handles=scan_resources,
            scan_configuration=scan_configuration,
            verbose=False,
        )

        self.assertEqual(len(result.formatted_measurements), 2)
        self.assertGreater(result.scan_time, 0)

        self.dmm_scan.close(scan_resources)


class TestIntegrationDmmScanPMPSScanConfiguration(unittest.TestCase):
    """Defines a test fixture for testing scan configuration handling.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        """Set up test fixtures."""
        self.dmm_scan = DmmScanPMPS()

    def tearDown(self):
        """Tear down test fixtures."""
        pass

    @classmethod
    def setUpClass(cls):
        """Set up class-level fixtures."""
        print("Setup test fixture: TestIntegrationDmmScanPMPSScanConfiguration")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    @classmethod
    def tearDownClass(cls):
        """Tear down class-level fixtures."""
        print("Teardown fixture: TestIntegrationDmmScanPMPSScanConfiguration")

    @patch("nipcbatt.switch.StaticDigitalPathGeneration")
    @patch("nipcbatt.dmm.MixedMeasurement")
    def test_integration_scan_configuration_with_mixed_ranges(
        self, mock_dmm_class, mock_switch_class
    ):
        """Integration test with mixed voltage ranges in single scan."""
        mock_mux_instance = MagicMock()
        mock_shunt_instance = MagicMock()
        mock_dmm_instance = MagicMock()

        mock_switch_class.side_effect = [mock_mux_instance, mock_shunt_instance]
        mock_dmm_class.return_value = mock_dmm_instance

        mock_measurement = MagicMock()
        mock_measurement.measurement = {
            "Measured_Value": 0.0,
            "Unit": "V (dc)",
            "Formatted_Measurement": "0V (dc)"
        }
        mock_measurement.dmm_execution_settings = {
            "Function": "DC_VOLTS",
            "Range": 10,
            "Digits_Resolution": 5.5,
        }

        mock_dmm_instance.acquire_measurement.return_value = mock_measurement

        scan_resources = self.dmm_scan.initialize()

        from nipcbatt import dmm as dmm_module
        scan_configuration = [
            [0, dmm_module.MixedRangeAndFunctions.DC_1V, dmm_module.ResolutionInDigits.DIGITS_5_5],
            [1, dmm_module.MixedRangeAndFunctions.DC_10V, dmm_module.ResolutionInDigits.DIGITS_5_5],
            [2, dmm_module.MixedRangeAndFunctions.DC_100V, dmm_module.ResolutionInDigits.DIGITS_5_5],
        ]

        result = self.dmm_scan.configure_and_measure(
            resource_handles=scan_resources,
            scan_configuration=scan_configuration,
            verbose=False,
        )

        self.assertEqual(len(result.formatted_measurements), 3)
        self.assertGreaterEqual(mock_dmm_instance.configure_measurement_function.call_count, 1)

        self.dmm_scan.close(scan_resources)


class TestIntegrationDmmScanPMPSWithVerboseOutput(unittest.TestCase):
    """Defines a test fixture for testing DmmScanPMPS with verbose output.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        """Set up test fixtures."""
        self.dmm_scan = DmmScanPMPS()

    def tearDown(self):
        """Tear down test fixtures."""
        pass

    @classmethod
    def setUpClass(cls):
        """Set up class-level fixtures."""
        print("Setup test fixture: TestIntegrationDmmScanPMPSWithVerboseOutput")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        """Tear down class-level fixtures."""
        print("Teardown fixture: TestIntegrationDmmScanPMPSWithVerboseOutput")

    @patch("nipcbatt.switch.StaticDigitalPathGeneration")
    @patch("nipcbatt.dmm.MixedMeasurement")
    def test_integration_scan_with_verbose_output(
        self, mock_dmm_class, mock_switch_class
    ):
        """Integration test verifying verbose output during scan."""
        mock_mux_instance = MagicMock()
        mock_shunt_instance = MagicMock()
        mock_dmm_instance = MagicMock()

        mock_switch_class.side_effect = [mock_mux_instance, mock_shunt_instance]
        mock_dmm_class.return_value = mock_dmm_instance

        mock_measurement = MagicMock()
        mock_measurement.measurement = {
            "Measured_Value": 5.125,
            "Unit": "V (dc)",
            "Formatted_Measurement": "5.125V (dc)"
        }
        mock_measurement.dmm_execution_settings = {
            "Function": "DC_VOLTS",
            "Range": 10,
            "Digits_Resolution": 5.5,
            "Aperture_Time(s)": "1m",
            "Settle_Time(s)": "1m",
            "Minimum_Frequency(Hz)": 40.0,
            "Absolute_Resolution": 0.0001,
            "Input_Resistance(Ohm)": 10000000.0,
            "Auto_Range_Value": -1.0,
        }

        mock_dmm_instance.acquire_measurement.return_value = mock_measurement

        scan_resources = self.dmm_scan.initialize()

        from nipcbatt import dmm as dmm_module
        scan_configuration = [
            [0, dmm_module.MixedRangeAndFunctions.DC_Voltage_Auto_Range, dmm_module.ResolutionInDigits.DIGITS_5_5],
            [1, dmm_module.MixedRangeAndFunctions.DC_Voltage_Auto_Range, dmm_module.ResolutionInDigits.DIGITS_5_5],
        ]

        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            result = self.dmm_scan.configure_and_measure(
                resource_handles=scan_resources,
                scan_configuration=scan_configuration,
                verbose=True,
            )

            sys.stdout = sys.__stdout__
            output_string = captured_output.getvalue()

            self.assertIsInstance(result, MeasurementResult)
            self.assertEqual(len(result.formatted_measurements), 2)

            self.assertIn("SCAN TIME", output_string)
            self.assertIn("FORMATTED MEASUREMENTS", output_string)
            self.assertIn("EXECUTION SETTINGS", output_string)
            self.assertIn("RAW MEASUREMENTS", output_string)

            self.dmm_scan.close(scan_resources)

        finally:
            sys.stdout = sys.__stdout__


class TestIntegrationDmmScanPMPSWithShuntHandling(unittest.TestCase):
    """Defines a test fixture for testing DmmScanPMPS with shunt handling.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        """Set up test fixtures."""
        self.dmm_scan = DmmScanPMPS()

    def tearDown(self):
        """Tear down test fixtures."""
        pass

    @classmethod
    def setUpClass(cls):
        """Set up class-level fixtures."""
        print("Setup test fixture: TestIntegrationDmmScanPMPSWithShuntHandling")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    @classmethod
    def tearDownClass(cls):
        """Tear down class-level fixtures."""
        print("Teardown fixture: TestIntegrationDmmScanPMPSWithShuntHandling")

    @patch("nipcbatt.switch.StaticDigitalPathGeneration")
    @patch("nipcbatt.dmm.MixedMeasurement")
    def test_integration_scan_with_current_channels_and_shunt_handling(
        self, mock_dmm_class, mock_switch_class
    ):
        """Integration test verifying shunt handling for current channels (16+)."""
        mock_mux_instance = MagicMock()
        mock_shunt_instance = MagicMock()
        mock_dmm_instance = MagicMock()

        mock_switch_class.side_effect = [mock_mux_instance, mock_shunt_instance]
        mock_dmm_class.return_value = mock_dmm_instance

        mock_measurement = MagicMock()
        mock_measurement.measurement = {
            "Measured_Value": 0.5,
            "Unit": "A (dc)",
            "Formatted_Measurement": "500mA (dc)"
        }
        mock_measurement.dmm_execution_settings = {
            "Function": "DC_CURRENT",
            "Range": 1.0,
            "Digits_Resolution": 5.5,
        }

        mock_dmm_instance.acquire_measurement.return_value = mock_measurement

        scan_resources = self.dmm_scan.initialize(close_all_shunts=True)

        from nipcbatt import dmm as dmm_module
        scan_configuration = [
            [16, dmm_module.MixedRangeAndFunctions.DC_Current_Auto_Range, dmm_module.ResolutionInDigits.DIGITS_5_5],
            [17, dmm_module.MixedRangeAndFunctions.DC_Current_Auto_Range, dmm_module.ResolutionInDigits.DIGITS_5_5],
        ]

        result = self.dmm_scan.configure_and_measure(
            resource_handles=scan_resources,
            scan_configuration=scan_configuration,
            verbose=False,
        )

        self.assertGreater(mock_shunt_instance.configure_and_generate.call_count, 0)
        self.assertEqual(len(result.formatted_measurements), 2)

        self.dmm_scan.close(scan_resources)

    @patch("nipcbatt.switch.StaticDigitalPathGeneration")
    @patch("nipcbatt.dmm.MixedMeasurement")
    def test_integration_scan_with_mixed_voltage_and_current_channels(
        self, mock_dmm_class, mock_switch_class
    ):
        """Integration test with mixed voltage and current channels in one scan."""
        mock_mux_instance = MagicMock()
        mock_shunt_instance = MagicMock()
        mock_dmm_instance = MagicMock()

        mock_switch_class.side_effect = [mock_mux_instance, mock_shunt_instance]
        mock_dmm_class.return_value = mock_dmm_instance

        mock_measurement = MagicMock()
        mock_measurement.dmm_execution_settings = {}

        def measurement_side_effect(*args, **kwargs):
            result_copy = MagicMock()
            result_copy.measurement = {
                "Measured_Value": 0.0,
                "Unit": "V (dc)",
                "Formatted_Measurement": "0V (dc)"
            }
            result_copy.dmm_execution_settings = {
                "Function": "DC_VOLTS",
                "Range": 10,
            }
            return result_copy

        mock_dmm_instance.acquire_measurement.side_effect = measurement_side_effect

        scan_resources = self.dmm_scan.initialize(close_all_shunts=True)

        from nipcbatt import dmm as dmm_module
        scan_configuration = [
            [0, dmm_module.MixedRangeAndFunctions.DC_Voltage_Auto_Range, dmm_module.ResolutionInDigits.DIGITS_5_5],
            [16, dmm_module.MixedRangeAndFunctions.DC_Current_Auto_Range, dmm_module.ResolutionInDigits.DIGITS_5_5],
            [1, dmm_module.MixedRangeAndFunctions.DC_Voltage_Auto_Range, dmm_module.ResolutionInDigits.DIGITS_5_5],
            [17, dmm_module.MixedRangeAndFunctions.DC_Current_Auto_Range, dmm_module.ResolutionInDigits.DIGITS_5_5],
        ]

        result = self.dmm_scan.configure_and_measure(
            resource_handles=scan_resources,
            scan_configuration=scan_configuration,
            verbose=False,
        )

        self.assertEqual(len(result.formatted_measurements), 4)
        self.assertEqual(len(result.raw_measurements), 4)

        self.dmm_scan.close(scan_resources)


class TestIntegrationDmmScanPMPSPerformance(unittest.TestCase):
    """Defines a test fixture for performance characteristics of DmmScanPMPS.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        """Set up test fixtures."""
        self.dmm_scan = DmmScanPMPS()

    def tearDown(self):
        """Tear down test fixtures."""
        pass

    @classmethod
    def setUpClass(cls):
        """Set up class-level fixtures."""
        print("Setup test fixture: TestIntegrationDmmScanPMPSPerformance")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    @classmethod
    def tearDownClass(cls):
        """Tear down class-level fixtures."""
        print("Teardown fixture: TestIntegrationDmmScanPMPSPerformance")

    @patch("nipcbatt.switch.StaticDigitalPathGeneration")
    @patch("nipcbatt.dmm.MixedMeasurement")
    def test_integration_scan_returns_valid_timing_information(
        self, mock_dmm_class, mock_switch_class
    ):
        """Integration test verifying scan returns valid timing information."""
        mock_mux_instance = MagicMock()
        mock_shunt_instance = MagicMock()
        mock_dmm_instance = MagicMock()

        mock_switch_class.side_effect = [mock_mux_instance, mock_shunt_instance]
        mock_dmm_class.return_value = mock_dmm_instance

        mock_measurement = MagicMock()
        mock_measurement.measurement = {
            "Measured_Value": 0.0,
            "Unit": "V (dc)",
            "Formatted_Measurement": "0V (dc)"
        }
        mock_measurement.dmm_execution_settings = {}

        mock_dmm_instance.acquire_measurement.return_value = mock_measurement

        scan_resources = self.dmm_scan.initialize()

        from nipcbatt import dmm as dmm_module
        scan_configuration = [
            [0, dmm_module.MixedRangeAndFunctions.DC_Voltage_Auto_Range, dmm_module.ResolutionInDigits.DIGITS_5_5],
        ]

        result = self.dmm_scan.configure_and_measure(
            resource_handles=scan_resources,
            scan_configuration=scan_configuration,
            verbose=False,
        )

        self.assertGreater(result.scan_time, 0)
        self.assertIsInstance(result.scan_time, float)
        self.assertLess(result.scan_time, 60)

        self.dmm_scan.close(scan_resources)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dynamic_digital_pattern_generations/__init__.py sha256=5af1b6660985f9de3b6c5130ba7f8d12f1114d0818c364dccf75eb7e9cdc542a bytes=483 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dynamic_digital_pattern_generations/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/dynamic_digital_pattern_generations/__init__.py`
- sha256: `5af1b6660985f9de3b6c5130ba7f8d12f1114d0818c364dccf75eb7e9cdc542a`
- bytes: 483

````python
"""Provides a set of integration tests for 
   nipcbatt.pcbatt_library.dynamic_digital_pattern_generations package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (366 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dynamic_digital_pattern_generations/test_integration_dynamic_digital_pattern_generation.py sha256=449ad5fd798227243662463cd8a79d482cbe8e18c888e89cdc8114262c6ee1a8 bytes=15186 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dynamic_digital_pattern_generations/test_integration_dynamic_digital_pattern_generation.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/dynamic_digital_pattern_generations/test_integration_dynamic_digital_pattern_generation.py`
- sha256: `449ad5fd798227243662463cd8a79d482cbe8e18c888e89cdc8114262c6ee1a8`
- bytes: 15186

````python
"""This module provides test of integration of DynamicDigitalPatternGeneration."""

import importlib
import importlib.metadata
import logging
import sys
import unittest

import nidaqmx.constants
import nidaqmx.stream_writers
import numpy as np
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    DynamicDigitalPatternTimingParameters,
)

import nipcbatt 
from nipcbatt import daq

# constants used across tests
CHANNEL = "TS1_DIO/port0/line0:7"
CLOCK_SOURCE = "OnboardClock"
TRIGGER_SOURCE = "/TS1_Core/PFI0"


class TestIntegrationDynamicDigitalPatternGeneration(unittest.TestCase):
    """Defines a test fixture to verify the integration of the
       'DynamicDigitalPatternGeneration' class

    Args:
        unittest: Base class for all tests
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

    def test_integration_dynamic_digital_pattern_gen_channel_expression_empty(self):
        """Integration test ensuring that if channel expression is empty then
        initialize() catches the error"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (411 > 100 characters) (auto-generated noqa)

        with daq.DynamicDigitalPatternGeneration() as gen:
            with self.assertRaises(ValueError):
                gen.initialize(channel_expression="")

            gen.close()

    def test_integration_dynamic_digital_pattern_gen_channel_expression_is_none(self):
        """Integration test ensuring that if channel expression
        is null then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.DynamicDigitalPatternGeneration() as gen:
            with self.assertRaises(ValueError):
                gen.initialize(channel_expression=None)

            gen.close()

    def test_integration_dynamic_digital_pattern_gen_configure_and_measure(self):
        """Integration test of Dynamic Digital Pattern Generation that ensures an instance
        of DynamicDigitalPatternGeneration is successfully executed when configure
        and measure is performed"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (405 > 100 characters) (auto-generated noqa)

        test_edge = daq.ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE
        test_sample_rate = 1000.0

        timing_params = DynamicDigitalPatternTimingParameters(
            sample_clock_source=CLOCK_SOURCE,
            number_of_samples_per_channel=100,
            active_edge=test_edge,
            sampling_rate_hertz=test_sample_rate,
        )

        trigger_params = daq.DynamicDigitalStartTriggerParameters(
            digital_start_trigger_source=TRIGGER_SOURCE,
            digital_start_trigger_edge=test_edge,
            trigger_type=nidaqmx.constants.TriggerType.DIGITAL_EDGE,
        )

        test_config = daq.DynamicDigitalPatternGenerationConfiguration(
            timing_parameters=timing_params,
            digital_start_trigger_parameters=trigger_params,
            pulse_signal=np.ndarray([0])
        )

        gen = daq.DynamicDigitalPatternGeneration()
        gen.initialize(CHANNEL)

        if gen.task.name is not None and gen.task.channel_names is not None:
            n = len(gen.task.channel_names)
        else:
            n = 11

        pattern = np.zeros((n, 10), dtype="uint32")

        gen.configure_and_generate(test_config)
        gen.close()

    def test_integration_dynamic_digital_pattern_rate_not_float(self):
        """Integration test of Dynamic Digital Pattern Generation that ensures an instance
        of DynamicDigitalPatternGeneration is not created if the given sample
        rate is not a float"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (400 > 100 characters) (auto-generated noqa)

        test_edge = daq.ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE
        test_sample_rate = 1000

        with self.assertRaises(ValueError):
            timing_params = DynamicDigitalPatternTimingParameters(
                sample_clock_source=CLOCK_SOURCE,
                number_of_samples_per_channel=100,
                active_edge=test_edge,
                sampling_rate_hertz=test_sample_rate,
            )

            trigger_params = daq.DynamicDigitalStartTriggerParameters(
                digital_start_trigger_source=TRIGGER_SOURCE,
                digital_start_trigger_edge=test_edge,
                trigger_type=nidaqmx.constants.TriggerType.DIGITAL_EDGE,
            )

            test_config = daq.DynamicDigitalPatternGenerationConfiguration(  # noqa: F841 - local variable 'test_config' is assigned to but never used (auto-generated noqa)
                timing_parameters=timing_params,
                digital_start_trigger_parameters=trigger_params,
                pulse_signal=np.array([0])
            )

            gen = (  # noqa: F841 - local variable 'gen' is assigned to but never used (auto-generated noqa)
                daq.DynamicDigitalPatternGeneration()
            )

    def test_integration_dynamic_digital_pattern_rate_negative(self):
        """Integration test of Dynamic Digital Pattern Generation that ensures an instance
        of DynamicDigitalPatternGeneration is not created if the given sample
        rate is a negative number"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (406 > 100 characters) (auto-generated noqa)

        test_edge = daq.ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE
        test_sample_rate = -1000.0

        with self.assertRaises(ValueError):
            timing_params = DynamicDigitalPatternTimingParameters(
                sample_clock_source=CLOCK_SOURCE,
                number_of_samples_per_channel=100,
                active_edge=test_edge,
                sampling_rate_hertz=test_sample_rate,
            )

            trigger_params = nipcbatt.DigitalStartTriggerParameters(
                digital_start_trigger_source=TRIGGER_SOURCE,
                digital_start_trigger_edge=test_edge,
                trigger_select=nidaqmx.constants.TriggerType.DIGITAL_EDGE,
            )

            test_config = daq.DynamicDigitalPatternGenerationConfiguration(  # noqa: F841 - local variable 'test_config' is assigned to but never used (auto-generated noqa)
                timing_parameters=timing_params,
                digital_start_trigger_parameters=trigger_params,
                pulse_signal=np.array([0])
            )

            gen = (  # noqa: F841 - local variable 'gen' is assigned to but never used (auto-generated noqa)
                daq.DynamicDigitalPatternGeneration()
            )

    def test_integration_dynamic_digital_pattern_signal_empty(self):
        """Integration test of Dynamic Digital Pattern Generation that ensures an instance
        of DynamicDigitalPatternGeneration is not created if the given signal is an empty
        array"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (386 > 100 characters) (auto-generated noqa)

        test_edge = daq.ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE
        test_sample_rate = 1000.0

        signal = np.array([])

        gen = daq.DynamicDigitalPatternGeneration()

        with self.assertRaises(ValueError):
            timing_params = DynamicDigitalPatternTimingParameters(
                sample_clock_source=CLOCK_SOURCE,
                number_of_samples_per_channel=100,
                active_edge=test_edge,
                sampling_rate_hertz=test_sample_rate,
            )

            trigger_params = daq.DynamicDigitalStartTriggerParameters(
                digital_start_trigger_source=TRIGGER_SOURCE,
                digital_start_trigger_edge=test_edge,
                trigger_type=nidaqmx.constants.TriggerType.DIGITAL_EDGE,
            )

            test_config = daq.DynamicDigitalPatternGenerationConfiguration(
                timing_parameters=timing_params,
                digital_start_trigger_parameters=trigger_params,
                pulse_signal=np.array([0])
            )

            gen.initialize(channel_expression=CHANNEL)
            gen.configure_and_generate(configuration=test_config)

        gen.close()

    def test_integration_dynamic_digital_pattern_signal_none(self):
        """Integration test of Dynamic Digital Pattern Generation that ensures an instance
        of DynamicDigitalPatternGeneration is not created if the given signal is an empty
        array"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (386 > 100 characters) (auto-generated noqa)

        test_edge = daq.ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE
        test_sample_rate = 1000.0

        signal = None

        with self.assertRaises(ValueError):
            timing_params = DynamicDigitalPatternTimingParameters(
                sample_clock_source=CLOCK_SOURCE,
                number_of_samples_per_channel=100,
                active_edge=test_edge,
                sampling_rate_hertz=test_sample_rate,
            )

            trigger_params = daq.DynamicDigitalStartTriggerParameters(
                digital_start_trigger_source=TRIGGER_SOURCE,
                digital_start_trigger_edge=test_edge,
                trigger_type=nidaqmx.constants.TriggerType.DIGITAL_EDGE,
            )

            test_config = daq.DynamicDigitalPatternGenerationConfiguration(
                timing_parameters=timing_params,
                digital_start_trigger_parameters=trigger_params,
                pulse_signal=np.array([0])
            )

            gen = daq.DynamicDigitalPatternGeneration()
            gen.initialize(channel_expression=CHANNEL)
            gen.configure_and_generate(configuration=test_config)
            gen.close()

    def test_integration_dynamic_digital_pattern_signal_wrong_shape(self):
        """Integration test of Dynamic Digital Pattern Generation that ensures an instance
        of DynamicDigitalPatternGeneration is not created if the given signal is the
        wrong shape"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (392 > 100 characters) (auto-generated noqa)

        test_edge = daq.ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE
        test_sample_rate = 1000.0

        # wrong shape of data array
        signal = np.zeros((10, 10))

        with self.assertRaises(Exception):
            timing_params = DynamicDigitalPatternTimingParameters(
                sample_clock_source=CLOCK_SOURCE,
                number_of_samples_per_channel=100,
                active_edge=test_edge,
                sampling_rate_hertz=test_sample_rate,
            )

            trigger_params = daq.DynamicDigitalStartTriggerParameters(
                digital_start_trigger_source=TRIGGER_SOURCE,
                digital_start_trigger_edge=test_edge,
                trigger_type=nidaqmx.constants.TriggerType.DIGITAL_EDGE,
            )

            test_config = daq.DynamicDigitalPatternGenerationConfiguration(
                timing_parameters=timing_params,
                digital_start_trigger_parameters=trigger_params,
                pulse_signal=np.array([0])
            )

            gen = daq.DynamicDigitalPatternGeneration()
            gen.initialize(channel_expression=CHANNEL)
            gen.configure_and_generate(configuration=test_config)
            gen.close()


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dynamic_digital_pattern_measurements/__init__.py sha256=a2447b1c6cb4879967bad4359dc4b489da9abdf2d756e4db6e30927ddcabb127 bytes=484 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dynamic_digital_pattern_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/dynamic_digital_pattern_measurements/__init__.py`
- sha256: `a2447b1c6cb4879967bad4359dc4b489da9abdf2d756e4db6e30927ddcabb127`
- bytes: 484

````python
"""Provides a set of integration tests for 
   nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (367 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/dynamic_digital_pattern_measurements/test_integration_dynamic_digital_pattern_measurement.py sha256=671602b90cd112def002edc24a166fd5de0bb523a945937da408aaba44b0a12e bytes=10614 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/dynamic_digital_pattern_measurements/test_integration_dynamic_digital_pattern_measurement.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/dynamic_digital_pattern_measurements/test_integration_dynamic_digital_pattern_measurement.py`
- sha256: `671602b90cd112def002edc24a166fd5de0bb523a945937da408aaba44b0a12e`
- bytes: 10614

````python
"""This module provides test of integration of DynamicDigitalPatternMeasurement."""

import importlib
import importlib.metadata
import logging
import sys
import unittest

import nidaqmx.constants
import nidaqmx.stream_writers  # noqa: F401 - 'nidaqmx.stream_writers' imported but unused (auto-generated noqa)
import numpy as np  # noqa: F401 - 'numpy as np' imported but unused (auto-generated noqa)
from varname import nameof

import nipcbatt
from nipcbatt import daq

class TestIntegrationDynamicDigitalPatternMeasurement(unittest.TestCase):
    """Defines a test fixture that check the integration of the
       'DynamicDigitalPatternMeasurement' class

    Args:
        unittest.TestCase: Base class of the unittest framework
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

    def test_integration_dynamic_digital_pattern_meas_channel_expression_empty(self):
        """Integration test ensuring that if channel expression is empty then
        initialize() catches the error"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (411 > 100 characters) (auto-generated noqa)

        with daq.DynamicDigitalPatternMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(channel_expression="")

            meas.close()

    def test_integration_dynamic_digital_pattern_meas_channel_expression_is_none(self):
        """Integration test ensuring that if channel expression
        is null then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.DynamicDigitalPatternMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(channel_expression=None)

            meas.close()

    def test_integration_test_dynamic_digital_pattern_measurement_configure_only(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements.dynamic_digital_pattern_measurement.
        DynamicDigitalPatternMeasurement with MeasurementExecutionType.CONFIGURE_ONLY
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.DynamicDigitalPatternMeasurement() as meas:
            meas.initialize(
                channel_expression="TS1_DIO/port0/line0:7",
            )
            timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
                sample_clock_source="OnboardClock",
                sampling_rate_hertz=10000.0,
                number_of_samples_per_channel=50,
                active_edge=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_ACTIVE_EDGE,
            )
            trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
                trigger_select=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_TRIGGER_TYPE,
                digital_start_trigger_source="/TS1_Core/PFI0",
                digital_start_trigger_edge=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE,
            )
            configuration = daq.DynamicDigitalPatternMeasurementConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                timing_parameters=timing_parameters,
                trigger_parameters=trigger_parameters,
            )
            results = meas.configure_and_measure(configuration=configuration)
            meas.close()

            print(f"parameters = {configuration}")
            print(f"results = {results}")
            self.assertIs(None, results)

    def test_integration_test_dynamic_digital_pattern_measurement_configure_and_measure(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements.dynamic_digital_pattern_measurement.
        DynamicDigitalPatternMeasurement with MeasurementExecutionType.CONFIGURE_AND_MEASURE
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.DynamicDigitalPatternMeasurement() as meas:
            meas.initialize(
                channel_expression="TS1_DIO/port0/line0:1",
            )
            timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
                sample_clock_source="OnboardClock",
                sampling_rate_hertz=10000.0,
                number_of_samples_per_channel=50,
                active_edge=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_ACTIVE_EDGE,
            )
            trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
                trigger_select=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_TRIGGER_TYPE,
                digital_start_trigger_source="/TS1_Core/PFI0",
                digital_start_trigger_edge=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE,
            )
            configuration = daq.DynamicDigitalPatternMeasurementConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                timing_parameters=timing_parameters,
                trigger_parameters=trigger_parameters,
            )
            results = meas.configure_and_measure(configuration=configuration)
            meas.close()

            print(f"parameters = {configuration}")
            print(f"results = {results}")
            print(type(results))
            self.assertIsInstance(results, daq.DynamicDigitalPatternMeasurementResultData)

    def test_integration_test_dynamic_digital_pattern_measurement_configure_only_and_measure_only(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements.dynamic_digital_pattern_measurement.
        DynamicDigitalPatternMeasurement with MeasurementExecutionType.MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (110 > 100 characters) (auto-generated noqa)

        with daq.DynamicDigitalPatternMeasurement() as meas:
            meas.initialize(
                channel_expression="TS1_DIO/port0/line0:7",
            )
            timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
                sample_clock_source="OnboardClock",
                sampling_rate_hertz=10000.0,
                number_of_samples_per_channel=50,
                active_edge=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_ACTIVE_EDGE,
            )
            trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
                trigger_select=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_TRIGGER_TYPE,
                digital_start_trigger_source="/TS1_Core/PFI0",
                digital_start_trigger_edge=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE,
            )
            configuration = daq.DynamicDigitalPatternMeasurementConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                timing_parameters=timing_parameters,
                trigger_parameters=trigger_parameters,
            )
            results = meas.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_ONLY, results = {results}"
            )
            self.assertIs(None, results)

            configuration = daq.DynamicDigitalPatternMeasurementConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                timing_parameters=timing_parameters,
                trigger_parameters=trigger_parameters,
            )
            results = meas.configure_and_measure(configuration=configuration)
            meas.close()

            print(
                f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
            )
            self.assertIsInstance(results, daq.DynamicDigitalPatternMeasurementResultData)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/frequency_domain_measurements/__init__.py sha256=5abfcf5348104c4f0f7b273ace2e94eb7f4d786ba721751410fd15a5a7c73b0b bytes=477 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/frequency_domain_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/frequency_domain_measurements/__init__.py`
- sha256: `5abfcf5348104c4f0f7b273ace2e94eb7f4d786ba721751410fd15a5a7c73b0b`
- bytes: 477

````python
"""Provides a set of integration tests for 
   nipcbatt.pcbatt_library.frequency_domain_measurements package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (360 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/frequency_domain_measurements/test_integration_frequency_domain_measurement.py sha256=8dd13e3c37360311ad04c9c8e9fc807c0f50a49756429a0ae32365ce48f772bf bytes=12848 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/frequency_domain_measurements/test_integration_frequency_domain_measurement.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/frequency_domain_measurements/test_integration_frequency_domain_measurement.py`
- sha256: `8dd13e3c37360311ad04c9c8e9fc807c0f50a49756429a0ae32365ce48f772bf`
- bytes: 12848

````python
"""This module provides test of integration of FrequencyDomainMeasurement."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt 
from nipcbatt import daq

'''from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
    _InterpreterDcRmsVoltageMeasurement,
)
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx_if_not_installed,
)'''


class TestIntegrationFrequencyDomainMeasurement(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `FrequencyDomainMeasurement` class.

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
        #_replace_daqmx_if_not_installed(_InterpreterDcRmsVoltageMeasurement)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_integration_frequency_domain_measurement_configure_only(self):
        """Integration test of
        nipcbatt.pcbatt_library.frequency_domain_measurements.frequency_domain_measurement.FrequencyDomainMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (425 > 100 characters) (auto-generated noqa)

        with daq.FrequencyDomainMeasurement() as measurement:
            measurement.initialize(
                analog_input_channel_expression=(
                    "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
                )
            )

            configuration = daq.FrequencyDomainMeasurementConfiguration(
                global_channel_parameters=(
                    daq.DEFAULT_FREQUENCY_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    daq.DEFAULT_FREQUENCY_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    daq.DEFAULT_FREQUENCY_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(f"results = {results}")
            self.assertIs(None, results)

    def test_integration_frequency_domain_measurement_configure_and_measure(self):
        """Integration test of
        nipcbatt.pcbatt_library.frequency_domain_measurements.frequency_domain_measurement.FrequencyDomainMeasurement
        with MeasurementExecutionType.CONFIGURE_AND_MEASURE"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (432 > 100 characters) (auto-generated noqa)

        with daq.FrequencyDomainMeasurement() as measurement:
            measurement.initialize(
                analog_input_channel_expression=(
                    "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
                )
            )

            print(f"parameters = {daq.DEFAULT_FREQUENCY_DOMAIN_MEASUREMENT_CONFIGURATION}")
            results = measurement.configure_and_measure(
                configuration=daq.DEFAULT_FREQUENCY_DOMAIN_MEASUREMENT_CONFIGURATION
            )

            print(f"results = {results}")
            self.assertIsInstance(results, daq.FrequencyDomainMeasurementResultData)

    def test_integration_frequency_domain_measurement_configure_only_and_measure_only(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.frequency_domain_measurements.frequency_domain_measurement.FrequencyDomainMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (422 > 100 characters) (auto-generated noqa)

        with daq.FrequencyDomainMeasurement() as measurement:
            measurement.initialize(
                analog_input_channel_expression=(
                    "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
                )
            )

            configuration = daq.FrequencyDomainMeasurementConfiguration(
                global_channel_parameters=(
                    daq.DEFAULT_FREQUENCY_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    daq.DEFAULT_FREQUENCY_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    daq.DEFAULT_FREQUENCY_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_ONLY, results = {results}"
            )
            self.assertIs(None, results)

            configuration = daq.FrequencyDomainMeasurementConfiguration(
                global_channel_parameters=(
                    daq.DEFAULT_FREQUENCY_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    daq.DEFAULT_FREQUENCY_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    daq.DEFAULT_FREQUENCY_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )

            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
            )
            self.assertIsInstance(results, daq.FrequencyDomainMeasurementResultData)

    def test_integration_time_domain_measurement_configure_only_and_measure_only_in_loop(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.time_domain_measurements.time_domain_measurement.TimeDomainMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (422 > 100 characters) (auto-generated noqa)

        channel_expressions = [
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3",
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai6",
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0, NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai15",
        ]
        for channel_expression in channel_expressions:
            with daq.FrequencyDomainMeasurement() as measurement:
                measurement.initialize(analog_input_channel_expression=channel_expression)

                configuration = daq.FrequencyDomainMeasurementConfiguration(
                    global_channel_parameters=(
                        daq.DEFAULT_FREQUENCY_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_options=nipcbatt.MeasurementOptions(
                        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                        measurement_analysis_requirement=(
                            nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS
                        ),
                    ),
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_FREQUENCY_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_FREQUENCY_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
                print(f"parameters = {configuration}")
                results = measurement.configure_and_measure(configuration=configuration)

                print(
                    f"after configuration with MeasurementExecutionType.CONFIGURE_ONLY, results = {results}"
                )
                self.assertIs(None, results)

                configuration = daq.FrequencyDomainMeasurementConfiguration(
                    global_channel_parameters=(
                        daq.DEFAULT_FREQUENCY_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_options=nipcbatt.MeasurementOptions(
                        execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                        measurement_analysis_requirement=(
                            nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
                        ),
                    ),
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_FREQUENCY_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_FREQUENCY_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )

                results = measurement.configure_and_measure(configuration=configuration)

                print(
                    f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
                )
                self.assertIsInstance(results, daq.FrequencyDomainMeasurementResultData)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/i2c_communications/__init__.py sha256=18f6163014bcbddbfe23542407d1ac127ff72fd656be2dd6e6035c7183427aed bytes=466 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/i2c_communications/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/i2c_communications/__init__.py`
- sha256: `18f6163014bcbddbfe23542407d1ac127ff72fd656be2dd6e6035c7183427aed`
- bytes: 466

````python
"""Provides a set of integration tests for 
   nipcbatt.pcbatt_library.i2c_communications package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (349 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/i2c_communications/test_integration_i2c_read_communication.py sha256=f2e0596f29f6dfd94541d581aa3549a7ca64ef2233d3f8433b7b38290430073c bytes=3935 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/i2c_communications/test_integration_i2c_read_communication.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/i2c_communications/test_integration_i2c_read_communication.py`
- sha256: `f2e0596f29f6dfd94541d581aa3549a7ca64ef2233d3f8433b7b38290430073c`
- bytes: 3935

````python
"""This module provides test of integration of I2CReadCommunication."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_communication_library._ni_845x_internal import _ni_845x_functions
from nipcbatt import communications


class TestIntegrationI2cReadCommunication(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `I2cReadCommunication` class.

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

    @unittest.skipIf(
        not (
            _ni_845x_functions.is_ni_845x_installed() and _ni_845x_functions.ni_845x_device_exists()
        ),
        "The execution of test is skipped"
        + " because Ni-845x driver is not installed or no NI 845x device found on system.",
    )
    def test_integration_i2c_read_communication(self):
        """Integration test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_read_communication.I2cReadCommunication
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with communications.I2cReadCommunication() as communication:
            communication.initialize("USB-8452")

            device_parameters = communications.I2cDeviceParameters(
                enable_i2c_pullup_resistor=False,
                voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_33,
            )
            communication_parameters = communications.I2cCommunicationParameters(
                device_address=73,
                clock_rate_kilohertz=400,
                addressing_type=nipcbatt.Ni845xI2cAddressingType.ADDRESSING_7_BIT,
                ack_poll_timeout_milliseconds=0,
            )
            read_parameters = communications.I2cReadParameters(
                number_of_bytes_to_read=2,
                memory_address_parameters=nipcbatt.MemoryAddressParameters(
                    memory_address=0,
                    address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE,
                    address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
                ),
            )
            configuration = communications.I2cReadCommunicationConfiguration(
                device_parameters=device_parameters,
                communication_parameters=communication_parameters,
                read_parameters=read_parameters,
            )

            print(f"parameters = {configuration}")
            results = communication.configure_and_read_data(configuration=communication)
            print(f"results = {results}")
            self.assertIsNotNone(None, results)
            self.assertIsInstance(results, communications.I2cReadCommunicationData)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/i2c_communications/test_integration_i2c_write_communication.py sha256=70df9b89aeda6e0269d333b4c8b63abf98bfcff80405111928ac17a030effa1c bytes=3919 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/i2c_communications/test_integration_i2c_write_communication.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/i2c_communications/test_integration_i2c_write_communication.py`
- sha256: `70df9b89aeda6e0269d333b4c8b63abf98bfcff80405111928ac17a030effa1c`
- bytes: 3919

````python
"""This module provides test of integration of I2CWriteCommunication."""

import importlib.metadata
import logging
import sys
import unittest

import numpy
from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_communication_library._ni_845x_internal import _ni_845x_functions
from nipcbatt import communications


class TestIntegrationI2cWriteCommunication(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `I2cWriteCommunication` class.

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

    @unittest.skipIf(
        not (
            _ni_845x_functions.is_ni_845x_installed() and _ni_845x_functions.ni_845x_device_exists()
        ),
        "The execution of test is skipped"
        + " because Ni-845x driver is not installed or no NI 845x device found on system.",
    )
    def test_integration_i2c_write_communication(self):
        """Integration test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_communication.I2cWriteCommunication
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with communications.I2cWriteCommunication() as communication:
            communication.initialize("USB-8452")

            device_parameters = communications.I2cDeviceParameters(
                enable_i2c_pullup_resistor=False,
                voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_33,
            )
            communication_parameters = communications.I2cCommunicationParameters(
                device_address=73,
                clock_rate_kilohertz=400,
                addressing_type=nipcbatt.Ni845xI2cAddressingType.ADDRESSING_7_BIT,
                ack_poll_timeout_milliseconds=0,
            )
            write_parameters = communications.I2cWriteParameters(
                number_of_bytes_per_page=2,
                delay_between_page_write_operations_milliseconds=10,
                data_to_be_written=numpy.array([26, 192, 30, 120, 50]),
                memory_address_parameters=nipcbatt.MemoryAddressParameters(
                    memory_address=0,
                    address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE,
                    address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
                ),
            )
            configuration = communications.I2cWriteCommunicationConfiguration(
                device_parameters=device_parameters,
                communication_parameters=communication_parameters,
                write_parameters=write_parameters,
            )

            print(f"parameters = {configuration}")
            communication.configure_and_write_data(configuration=configuration)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/mixed_measurement/__init__.py sha256=c4c22af682b998c3b9db3eddc87da30302d638ca483ff92a032efe2612746f33 bytes=96 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/mixed_measurement/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/mixed_measurement/__init__.py`
- sha256: `c4c22af682b998c3b9db3eddc87da30302d638ca483ff92a032efe2612746f33`
- bytes: 96

````python
"""Provides a set of integration tests for nipcbatt.pcbatt_library.mixed_measurements package"""
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/mixed_measurement/test_integration_dmm_mixed_measurement.py sha256=4ed5ba5fd58cab0fbfba63d7b1bb211fa0e7b2707e4c7ff90310115e3ab3a1d6 bytes=6247 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/mixed_measurement/test_integration_dmm_mixed_measurement.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/mixed_measurement/test_integration_dmm_mixed_measurement.py`
- sha256: `4ed5ba5fd58cab0fbfba63d7b1bb211fa0e7b2707e4c7ff90310115e3ab3a1d6`
- bytes: 6247

````python
"""This module provides integration tests for DMM mixed measurement."""

import importlib.metadata
import logging
import sys
import unittest

import nidmm
import nipcbatt
from nipcbatt import dmm


class TestIntegrationMixedMeasurement(unittest.TestCase):
	"""Defines integration checks for `dmm.MixedMeasurement`."""

	RESOURCE_NAME = "Sim_DMM"
	POWERLINE_FREQUENCY = 60.0

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

		try:
			used_nidmm_version = importlib.metadata.version("nidmm")
		except importlib.metadata.PackageNotFoundError:
			used_nidmm_version = "not installed"
		logging.debug("used_nidmm_version = %s", used_nidmm_version)

	@classmethod
	def tearDownClass(cls):
		print("Teardown fixture")

	def _create_initialized_uut(self) -> dmm.MixedMeasurement:
		uut = dmm.MixedMeasurement()
		try:
			uut.initialize(self.RESOURCE_NAME, self.POWERLINE_FREQUENCY)
		except nidmm.errors.DriverError as error:
			self.skipTest(f"NI-DMM resource '{self.RESOURCE_NAME}' not available: {error}")
		return uut

	def test_initialize_configure_measure_close_dc_voltage(self):
		"""Happy path: DC voltage mixed measurement configure and measure."""
		uut = self._create_initialized_uut()

		cfg = dmm.MixedMeasurementConfiguration(
			execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
			measurement_function_parameters=dmm.MixedMeasurementFunctionParameters(
				dmm.MixedRangeAndFunctions.DC_10V,
				dmm.ResolutionInDigits.DIGITS_5_5,
			),
			trigger_parameters=dmm.TriggerParameters(
				trigger_source=nidmm.TriggerSource.IMMEDIATE,
				trigger_delay=0.0,
				slope=dmm.Slope.RISING_EDGE,
				enable_trigger=True,
			),
			timing_parameters=dmm.TimingParameters(0.001, 0.01),
			ac_min_frequency=10.0,
		)

		try:
			result = uut.configure_and_measure(cfg)

			self.assertIsNotNone(result)
			self.assertIsInstance(result, dmm.MixedMeasurementResultData)
			self.assertIn("Measured_Value", result.measurement)
		finally:
			uut.close()

	def test_configure_only_returns_none(self):
		"""Ensures CONFIGURE_ONLY execution returns None."""
		uut = self._create_initialized_uut()

		cfg = dmm.MixedMeasurementConfiguration(
			execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
			measurement_function_parameters=dmm.MixedMeasurementFunctionParameters(
				dmm.MixedRangeAndFunctions.TWO_W_RES_1k_Ohm,
				dmm.ResolutionInDigits.DIGITS_4_5,
			),
			trigger_parameters=dmm.TriggerParameters(
				trigger_source=nidmm.TriggerSource.IMMEDIATE,
				trigger_delay=0.0,
				slope=dmm.Slope.RISING_EDGE,
				enable_trigger=False,
			),
			timing_parameters=dmm.TimingParameters(0.001, 0.01),
			ac_min_frequency=10.0,
		)

		try:
			result = uut.configure_and_measure(cfg)
			self.assertIsNone(result)
		finally:
			uut.close()

	def test_measure_only_reads_and_wraps_result(self):
		"""Ensures MEASURE_ONLY returns mixed measurement result data."""
		uut = self._create_initialized_uut()

		cfg = dmm.MixedMeasurementConfiguration(
			execution_type=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
			measurement_function_parameters=dmm.MixedMeasurementFunctionParameters(
				dmm.MixedRangeAndFunctions.DC_100mA,
				dmm.ResolutionInDigits.DIGITS_5_5,
			),
			trigger_parameters=dmm.TriggerParameters(
				trigger_source=nidmm.TriggerSource.IMMEDIATE,
				trigger_delay=0.0,
				slope=dmm.Slope.RISING_EDGE,
				enable_trigger=True,
			),
			timing_parameters=dmm.TimingParameters(0.001, 0.01),
			ac_min_frequency=10.0,
		)

		try:
			result = uut.configure_and_measure(cfg)
			self.assertIsNotNone(result)
			self.assertIsInstance(result.dmm_execution_settings, dict)
			self.assertIsInstance(result.measurement, dict)
		finally:
			uut.close()

	def test_ac_measurement_applies_ac_min_frequency(self):
		"""AC measurement path should apply configured AC minimum frequency."""
		uut = self._create_initialized_uut()

		cfg = dmm.MixedMeasurementConfiguration(
			execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
			measurement_function_parameters=dmm.MixedMeasurementFunctionParameters(
				dmm.MixedRangeAndFunctions.AC_20V,
				dmm.ResolutionInDigits.DIGITS_4_5,
			),
			trigger_parameters=dmm.TriggerParameters(
				trigger_source=nidmm.TriggerSource.IMMEDIATE,
				trigger_delay=0.0,
				slope=dmm.Slope.RISING_EDGE,
				enable_trigger=True,
			),
			timing_parameters=dmm.TimingParameters(0.001, 0.01),
			ac_min_frequency=55.0,
		)

		try:
			result = uut.configure_and_measure(cfg)
			self.assertIsNotNone(result)
			self.assertEqual(result.dmm_execution_settings["Minimum_Frequency(Hz)"], 55.0)
		finally:
			uut.close()

	def test_multiple_mixed_ranges(self):
		"""Verifies mixed measurement with multiple function/range settings."""
		uut = self._create_initialized_uut()

		test_ranges = [
			dmm.MixedRangeAndFunctions.DC_1V,
			dmm.MixedRangeAndFunctions.DC_10mA,
			dmm.MixedRangeAndFunctions.TWO_W_RES_10k_Ohm,
			dmm.MixedRangeAndFunctions.FOUR_W_RES_1k_Ohm,
		]

		try:
			for mixed_range in test_ranges:
				cfg = dmm.MixedMeasurementConfiguration(
					execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
					measurement_function_parameters=dmm.MixedMeasurementFunctionParameters(
						mixed_range,
						dmm.ResolutionInDigits.DIGITS_4_5,
					),
					trigger_parameters=dmm.TriggerParameters(
						trigger_source=nidmm.TriggerSource.IMMEDIATE,
						trigger_delay=0.0,
						slope=dmm.Slope.RISING_EDGE,
						enable_trigger=True,
					),
					timing_parameters=dmm.TimingParameters(0.001, 0.01),
					ac_min_frequency=10.0,
				)

				result = uut.configure_and_measure(cfg)
				self.assertIsNotNone(result)
				self.assertIn("Function", result.dmm_execution_settings)
				self.assertIn("Measured_Value", result.measurement)
		finally:
			uut.close()


if __name__ == "__main__":
	unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/power_supply_source_and_measurements/__init__.py sha256=288691e0b2f296928f1b3161648aacfae1d790f64ae13b017dce77f3a1f711e3 bytes=484 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/power_supply_source_and_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/power_supply_source_and_measurements/__init__.py`
- sha256: `288691e0b2f296928f1b3161648aacfae1d790f64ae13b017dce77f3a1f711e3`
- bytes: 484

````python
"""Provides a set of integration tests for 
   nipcbatt.pcbatt_library.power_supply_source_and_measurements package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (367 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/power_supply_source_and_measurements/test_integration_power_supply_source_and_measure.py sha256=46e265ce2817dd85f51179411b1599df69ce0c6d8c996fbd059980f68cbd5b2f bytes=12584 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/power_supply_source_and_measurements/test_integration_power_supply_source_and_measure.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/power_supply_source_and_measurements/test_integration_power_supply_source_and_measure.py`
- sha256: `46e265ce2817dd85f51179411b1599df69ce0c6d8c996fbd059980f68cbd5b2f`
- bytes: 12584

````python
"""This module provides test of integration of PowerSupplySourceAndMeasure check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt import daq

'''from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
    _InterpreterPowerSupplySourceAndMeasure,
)
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx_if_not_installed,
)'''


class TestIntegrationPowerSupplySourceAndMeasureMeasurement(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `PowerSupplySourceAndMeasure` class.

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
        #_replace_daqmx_if_not_installed(_InterpreterPowerSupplySourceAndMeasure)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_integration_power_supply_and_source_measurement_configure_only(self):
        """Integration test of
        nipcbatt.pcbatt_library.power_supply_source_and_measurements.power_supply_source_and_measure.PowerSupplySourceAndMeasure
         with MeasurementExecutionType.CONFIGURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (426 > 100 characters) (auto-generated noqa)

        with daq.PowerSupplySourceAndMeasure() as measurement:
            measurement.initialize(
                power_channel_name="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod5/power"
            )

            configuration = daq.PowerSupplySourceAndMeasureConfiguration(
                terminal_parameters=(
                    daq.DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_TERMINAL_PARAMETERS
                ),
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    daq.DEFAULT_POWER_SUPPLY_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    daq.DEFAULT_POWER_SUPPLY_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )

            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(f"results = {results}")
            self.assertIs(None, results)

            measurement.close()

    def test_integration_power_supply_and_source_measurement_configure_only_measure_only(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.power_supply_source_and_measurements.power_supply_source_and_measure.PowerSupplySourceAndMeasure
         with MeasurementExecutionType.CONFIGURE_ONLY and MeasurementExecutionType.MEASURE_ONLY
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.PowerSupplySourceAndMeasure() as measurement:
            measurement.initialize(
                power_channel_name="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod5/power"
            )

            configuration = daq.PowerSupplySourceAndMeasureConfiguration(
                terminal_parameters=(
                    daq.DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_TERMINAL_PARAMETERS
                ),
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    daq.DEFAULT_POWER_SUPPLY_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    daq.DEFAULT_POWER_SUPPLY_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )

            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(f"results = {results}")
            self.assertIs(None, results)

            configuration = daq.PowerSupplySourceAndMeasureConfiguration(
                terminal_parameters=(
                    daq.DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_TERMINAL_PARAMETERS
                ),
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    daq.DEFAULT_POWER_SUPPLY_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    daq.DEFAULT_POWER_SUPPLY_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )

            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
            )
            self.assertIsInstance(results, daq.PowerSupplySourceAndMeasureResultData)

            measurement.close()

    def test_integration_power_supply_and_source_measurement_configure_and_measure(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.power_supply_source_and_measurements.power_supply_source_and_measure.PowerSupplySourceAndMeasure
         with MeasurementExecutionType.CONFIGURE_AND_MEASURE
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with daq.PowerSupplySourceAndMeasure() as measurement:
            measurement.initialize(
                power_channel_name="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod5/power"
            )

            configuration = daq.PowerSupplySourceAndMeasureConfiguration(
                terminal_parameters=(
                    daq.DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_TERMINAL_PARAMETERS
                ),
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    daq.DEFAULT_POWER_SUPPLY_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    daq.DEFAULT_POWER_SUPPLY_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )

            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_AND_MEASURE and MeasurementAnalysisRequirement.SKIP_ANALYSIS, results = {results}"
            )
            self.assertIs(None, results)

            configuration = daq.PowerSupplySourceAndMeasureConfiguration(
                terminal_parameters=(
                    daq.DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_TERMINAL_PARAMETERS
                ),
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    daq.DEFAULT_POWER_SUPPLY_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    daq.DEFAULT_POWER_SUPPLY_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )

            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_AND_MEASURE and MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS, results = {results}"
            )
            self.assertIsInstance(results, daq.PowerSupplySourceAndMeasureResultData)

            measurement.close()

    def test_integration_power_supply_and_source_measurement_full_sequence_in_loop(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.power_supply_source_and_measurements.power_supply_source_and_measure.PowerSupplySourceAndMeasure
        for initialize, configure and measure and close to be called in loop with the same context.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        for _ in range(3):
            with daq.PowerSupplySourceAndMeasure() as measurement:
                measurement.initialize(
                    power_channel_name="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod5/power"
                )

                configuration = daq.PowerSupplySourceAndMeasureConfiguration(
                    terminal_parameters=(
                        daq.DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_TERMINAL_PARAMETERS
                    ),
                    measurement_options=daq.DEFAULT_POWER_SUPPLY_MEASUREMENT_OPTIONS,
                    sample_clock_timing_parameters=(
                        daq.DEFAULT_POWER_SUPPLY_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        daq.DEFAULT_POWER_SUPPLY_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )

                results = measurement.configure_and_measure(configuration=configuration)

                print(
                    f"after configuration with MeasurementExecutionType.CONFIGURE_AND_MEASURE and MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS, results = {results}"
                )
                self.assertIsInstance(results, daq.PowerSupplySourceAndMeasureResultData)

                measurement.close()


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/resistance_measurments/__init__.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/resistance_measurments/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/resistance_measurments/__init__.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/resistance_measurments/test_dmm_resistance_measurements.py sha256=4fbf0fcfadc99fecee5993e3c2887d3c51ce991b041ada96fee01df7352fa3b3 bytes=8867 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/resistance_measurments/test_dmm_resistance_measurements.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/resistance_measurments/test_dmm_resistance_measurements.py`
- sha256: `4fbf0fcfadc99fecee5993e3c2887d3c51ce991b041ada96fee01df7352fa3b3`
- bytes: 8867

````python
"""This module provides test of integration of DMM resistance measurement"""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nidmm
import nipcbatt
from nipcbatt import dmm

class TestIntegrationDmmResistanceMeasurement(unittest.TestCase):
    """Definte a test fixture that check the integration of 
    'DmmDCRmsVoltage'
    
    Args:
        unittest.TestCase: Base class from which this class inherits
    """

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

        used_niswitch_version = importlib.metadata.version("niswitch")
        logging.debug("%s = %s", nameof(used_niswitch_version), used_niswitch_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")


    def test_configure_only_resistance(self):
        """CONFIGURE_ONLY should not perform a measurement."""

        uut = dmm.DcRmsResistanceMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        meas_params = dmm.ResistanceMeasurementFunctionParameters(
            dmm.ResistanceRangeAndFunctions.TWO_W_RES_1k_Ohm,
            dmm.ResolutionInDigits.DIGITS_5_5
        )

        trig_params = dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.IMMEDIATE,
            trigger_delay=0.0,
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=False   # disabled ⇒ immediate/-1.0 path
        )

        timing_params = dmm.TimingParameters(
            aperture_time_seconds=0.001,
            settle_time_seconds=0.01
        )

        cfg = dmm.ResistanceMeasurementConfiguration(
            execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
            measurement_function_parameters=meas_params,
            trigger_parameters=trig_params,
            timing_parameters=timing_params,
        )

        result = uut.configure_and_measure(cfg)
        assert result is None  # configure-only should return None per implementation

        uut.close()


    def test_measure_only_resistance(self):
        """MEASURE_ONLY should read and return a result."""

        uut = dmm.DcRmsResistanceMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        meas_params = dmm.ResistanceMeasurementFunctionParameters(
            dmm.ResistanceRangeAndFunctions.TWO_W_RES_10k_Ohm,
            dmm.ResolutionInDigits.DIGITS_5_5
        )

        trig_params = dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.IMMEDIATE,
            trigger_delay=0.0,
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=True
        )

        timing_params = dmm.TimingParameters(
            aperture_time_seconds=0.002,
            settle_time_seconds=0.02
        )

        cfg = dmm.ResistanceMeasurementConfiguration(
            execution_type=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
            measurement_function_parameters=meas_params,
            trigger_parameters=trig_params,
            timing_parameters=timing_params,
        )

        result = uut.configure_and_measure(cfg)
        assert result is not None
        assert result.measurement is not None
        assert "Measured_Value" in result.measurement  # packaged by acquire_measurement 

        uut.close()

    
    def test_configure_and_measure_resistance_2w_trigger_disabled(self):
        """Trigger disabled forces IMMEDIATE and -1.0 delay."""

        uut = dmm.DcRmsResistanceMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        meas_params = dmm.ResistanceMeasurementFunctionParameters(
            dmm.ResistanceRangeAndFunctions.TWO_W_RES_100_Ohm,
            dmm.ResolutionInDigits.DIGITS_5_5
        )

        trig_params = dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.EXTERNAL,  # ignored when disabled
            trigger_delay=0.123,                            # ignored when disabled
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=False
        )

        timing_params = dmm.TimingParameters(
            aperture_time_seconds=0.0005,
            settle_time_seconds=0.005
        )

        cfg = dmm.ResistanceMeasurementConfiguration(
            execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            measurement_function_parameters=meas_params,
            trigger_parameters=trig_params,
            timing_parameters=timing_params,
        )

        result = uut.configure_and_measure(cfg)

        assert result is not None
        # Sanity checks on execution settings dictionary created in acquire_measurement
        for key in ["Function", "Aperture_Time(s)", "Settle_Time(s)", "Digits_Resolution"]:
            assert key in result.dmm_execution_settings  # fields produced by acquire_measurement 

        uut.close()


    def test_configure_and_measure_resistance_4w_trigger_enabled(self):
        """4-wire resistance with trigger enabled uses provided source/delay and slope."""

        uut = dmm.DcRmsResistanceMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        meas_params = dmm.ResistanceMeasurementFunctionParameters(
            dmm.ResistanceRangeAndFunctions.FOUR_W_RES_1k_Ohm,
            dmm.ResolutionInDigits.DIGITS_4_5
        )

        trig_params = dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.EXTERNAL,
            trigger_delay=0.001,
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=True
        )

        timing_params = dmm.TimingParameters(
            aperture_time_seconds=0.001,
            settle_time_seconds=0.01
        )

        cfg = dmm.ResistanceMeasurementConfiguration(
            execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            measurement_function_parameters=meas_params,
            trigger_parameters=trig_params,
            timing_parameters=timing_params,
        )

        result = uut.configure_and_measure(cfg)

        # Should get a measurement packaged by acquire_measurement
        assert result is not None
        assert result.measurement is not None
        assert "Measured_Value" in result.measurement  # produced by FormatMeasurement.measurement(...) 

        uut.close()


    def test_multiple_resistance_ranges_and_resolutions(self):
        """Exercise several 2W and 4W resistance ranges with a common resolution."""

        uut = dmm.DcRmsResistanceMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        test_ranges = [
            dmm.ResistanceRangeAndFunctions.TWO_W_Resistance_Auto_Range,
            dmm.ResistanceRangeAndFunctions.TWO_W_RES_1k_Ohm,
            dmm.ResistanceRangeAndFunctions.TWO_W_RES_1M_Ohm,
            dmm.ResistanceRangeAndFunctions.FOUR_W_Resistance_Auto_Range,
            dmm.ResistanceRangeAndFunctions.FOUR_W_RES_100_Ohm,
            dmm.ResistanceRangeAndFunctions.FOUR_W_RES_10k_Ohm,
        ]

        for rng in test_ranges:
            meas_params = dmm.ResistanceMeasurementFunctionParameters(
                rng,
                dmm.ResolutionInDigits.DIGITS_4_5
            )

            cfg = dmm.ResistanceMeasurementConfiguration(
                execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                measurement_function_parameters=meas_params,
                trigger_parameters=dmm.TriggerParameters(
                    trigger_source=nidmm.TriggerSource.IMMEDIATE,
                    trigger_delay=0.0,
                    slope=dmm.Slope.RISING_EDGE,
                    enable_trigger=True
                ),
                timing_parameters=dmm.TimingParameters(0.001, 0.01),
            )

            result = uut.configure_and_measure(cfg)
            assert result is not None
            assert "Measured_Value" in result.measurement  # validates measurement path and packaging 

        uut.close()


    def test_resistance_initialize_and_close_is_idempotent(self):
        """Initialize then close twice to ensure no error and powerline is set."""

        uut = dmm.DcRmsResistanceMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        # Power line frequency should be set onto the NI-DMM session
        assert uut.session.powerline_freq == 60.0  # assigned during initialize 
        # First close
        uut.close()

        # Second close should be a no-op (no exception)
        uut.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/serial_communications/__init__.py sha256=f24019a0ad079a8162a6047daa732a30acc3f465dc3785c71929e5e8fca3dd63 bytes=469 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/serial_communications/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/serial_communications/__init__.py`
- sha256: `f24019a0ad079a8162a6047daa732a30acc3f465dc3785c71929e5e8fca3dd63`
- bytes: 469

````python
"""Provides a set of integration tests for 
   nipcbatt.pcbatt_library.serial_communications package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (352 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/serial_communications/test_integration_serial_communication.py sha256=f6d42e9f423b860db924320f4ba03cca7097a5b0e3b9f4588a0edbd577644820 bytes=3258 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/serial_communications/test_integration_serial_communication.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/serial_communications/test_integration_serial_communication.py`
- sha256: `f6d42e9f423b860db924320f4ba03cca7097a5b0e3b9f4588a0edbd577644820`
- bytes: 3258

````python
"""This module provides test of integration of SerialCommunication."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt import communications

class TestIntegrationSerialCommunication(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `SerialCommunication` class.

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

    @unittest.skip(
        "The execution of test is skipped"
        + " because it requires a serial device that responds to VISA query.",
    )
    def test_integration_serial_communication(self):
        """Integration test of
        nipcbatt.pcbatt_library.serial_communications.serial_communication.SerialCommunication
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with communications.SerialCommunication() as communication:
            communication.initialize("ASRL7::INSTR")

            communication_parameters = communications.SerialCommunicationParameters(
                data_rate_bauds=9600,
                number_of_bits_in_data_frame=8,
                delay_before_receive_response_milliseconds=100,
                parity=communications.ConstantsForSerialCommunication.DEFAULT_PARITY,
                stop_bits=communications.ConstantsForSerialCommunication.DEFAULT_STOP_BITS,
                flow_control=communications.ConstantsForSerialCommunication.DEFAULT_FLOW_CONTROL_MODE,
            )
            configuration = communications.SerialCommunicationConfiguration(
                communication_parameters=communication_parameters,
                command_to_send="*IDN?",
            )

            print(f"parameters = {configuration}")
            results = communication.configure_then_send_command_and_receive_response(
                configuration=configuration
            )
            print(f"results = {results}")
            self.assertIsNotNone(results)
            self.assertIsInstance(results, communications.SerialCommunicationData)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/signal_voltage_generations/__init__.py sha256=4e031c3d3d4eae69a4652f69a2dc86a4e2c0c3f02b496e496f32f3230e7aabc1 bytes=474 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/signal_voltage_generations/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/signal_voltage_generations/__init__.py`
- sha256: `4e031c3d3d4eae69a4652f69a2dc86a4e2c0c3f02b496e496f32f3230e7aabc1`
- bytes: 474

````python
"""Provides a set of integration tests for 
   nipcbatt.pcbatt_library.signal_voltage_generations package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (357 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/signal_voltage_generations/test_integration_signal_voltage_generation.py sha256=0a77c0cab7cd6c1e0d36a3074d8244c99a25ef7f339f9fa63fb5d706209f5691 bytes=11421 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/signal_voltage_generations/test_integration_signal_voltage_generation.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/signal_voltage_generations/test_integration_signal_voltage_generation.py`
- sha256: `0a77c0cab7cd6c1e0d36a3074d8244c99a25ef7f339f9fa63fb5d706209f5691`
- bytes: 11421

````python
"""This module provides test of integration of SignalVoltageGeneration."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt import daq

'''from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
    _MockInterpreter,
)
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx,
)'''


class TestIntegrationSignalVoltageGeneration(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `SignalVoltageGeneration` class.

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
        #_replace_daqmx(_MockInterpreter)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_signal_voltage_generation_generate_only(self):
        """Checks if class `SignalVoltageGeneration' can generate
        with just the initial configurations"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (417 > 100 characters) (auto-generated noqa)

        generation = daq.SignalVoltageGeneration()
        generation.initialize(
            channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod3/ao0:1"
        )
        generation.generate_voltage_sine_waveform(
            signal_parameters=daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_PARAMETERS,
            timing_parameters=daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
        )
        generation.generate_voltage_square_waveform(
            signal_parameters=daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_SQUARE_WAVE_PARAMETERS,
            timing_parameters=daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
        )
        generation.generate_voltage_multi_tones_waveform(
            signal_parameters=daq.DEFAULT_MULTI_TONE_GENERATION_PARAMETERS,
            timing_parameters=daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
        )
        generation.close()

    def test_signal_voltage_generation_configure_and_generate_in_loop(self):
        """Checks if class `SignalVoltageGeneration' can configure and generate
        when they are called one after the other."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (345 > 100 characters) (auto-generated noqa)
        generation_channel_parameters_1 = daq.VoltageGenerationChannelParameters(
            range_min_volts=-5.0,
            range_max_volts=5.0,
        )
        sine_wave_parameters_1 = daq.SignalVoltageGenerationSineWaveParameters(
            generated_signal_offset_volts=0.01,
            generated_signal_tone_parameters=daq.ToneParameters(
                tone_frequency_hertz=100,
                tone_amplitude_volts=1.0,
                tone_phase_radians=0,
            ),
        )

        generation_channel_parameters_2 = daq.VoltageGenerationChannelParameters(
            range_min_volts=-8.0,
            range_max_volts=8.0,
        )
        sine_wave_parameters_2 = daq.SignalVoltageGenerationSineWaveParameters(
            generated_signal_offset_volts=0.02,
            generated_signal_tone_parameters=daq.ToneParameters(
                tone_frequency_hertz=1000,
                tone_amplitude_volts=2.0,
                tone_phase_radians=0.3,
            ),
        )

        test_parameter_list = []
        test_parameter_list.append((generation_channel_parameters_1, sine_wave_parameters_1))
        test_parameter_list.append((generation_channel_parameters_2, sine_wave_parameters_2))

        generation = daq.SignalVoltageGeneration()
        generation.initialize(
            channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod3/ao0:1"
        )

        for generation_parameters, sine_wave_parameters in test_parameter_list:
            generation.configure_all_channels(parameters=generation_parameters)
            generation.configure_timing(
                parameters=daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS
            )
            generation.generate_voltage_sine_waveform(
                signal_parameters=sine_wave_parameters,
                timing_parameters=daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
            )
        generation.close()

    def test_signal_voltage_generation_for_configure_and_generate_sine_wave(self):
        """Checks if class `SignalVoltageGeneration' can configure and generate sine wave."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (179 > 100 characters) (auto-generated noqa)

        generation = daq.SignalVoltageGeneration()
        generation.initialize(
            channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod3/ao0:1"
        )
        generation.configure_and_generate_sine_waveform(
            configuration=daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_CONFIGURATION
        )
        generation.close()

    def test_signal_voltage_generation_for_configure_and_generate_square_wave(self):
        """Checks if class `SignalVoltageGeneration' can configure and generate square wave."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (181 > 100 characters) (auto-generated noqa)

        generation = daq.SignalVoltageGeneration()
        generation.initialize(
            channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod3/ao0:1"
        )
        generation.configure_and_generate_square_waveform(
            configuration=daq.DEFAULT_SQUARE_WAVE_GENERATION_CONFIGURATION
        )
        generation.close()

    def test_signal_voltage_generation_for_configure_and_generate_multiple_tones_sine_signal(
        self,
    ):
        """Checks if class `SignalVoltageGeneration' can configure and generate
        multiple tones signal."""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (403 > 100 characters) (auto-generated noqa)

        generation = daq.SignalVoltageGeneration()
        generation.initialize(
            channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod3/ao0:1"
        )
        generation.configure_and_generate_multiple_tones_waveform(
            configuration=daq.DEFAULT_MULTI_TONE_GENERATION_CONFIGURATION
        )
        generation.close()

    def test_signal_voltage_generation_route_sample_clock_signal_to_terminal(self):
        """Checks if class `SignalVoltageGeneration' can configure and export the
        sample clock signal to the specified terminal"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (349 > 100 characters) (auto-generated noqa)
        generation = daq.SignalVoltageGeneration()
        generation.initialize(
            channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod3/ao0:1"
        )
        generation.configure_all_channels(
            parameters=daq.DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS
        )
        generation.configure_timing(
            parameters=daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS
        )
        generation.configure_trigger(parameters=daq.DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS)
        generation.route_sample_clock_signal_to_terminal(
            terminal_name="/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0"
        )
        generation.generate_voltage_multi_tones_waveform(
            signal_parameters=daq.DEFAULT_MULTI_TONE_GENERATION_PARAMETERS,
            timing_parameters=daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
        )
        generation.close()

    def test_signal_voltage_generation_route_digital_trigger_signal_to_terminal(self):
        """Checks if class `SignalVoltageGeneration' can configure and export the
        digital trigger signal to the specified terminal"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (429 > 100 characters) (auto-generated noqa)

        generation = daq.SignalVoltageGeneration()
        generation.initialize(
            channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod3/ao0:1"
        )
        generation.configure_all_channels(
            parameters=daq.DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS
        )
        generation.configure_timing(
            parameters=daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS
        )
        generation.route_start_trigger_signal_to_terminal(
            terminal_name="/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0"
        )
        generation.configure_trigger(parameters=daq.DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS)
        generation.generate_voltage_square_waveform(
            signal_parameters=daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_SQUARE_WAVE_PARAMETERS,
            timing_parameters=daq.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
        )
        generation.close()


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/spi_communications/__init__.py sha256=54dbf44d7a62bddf694a4921401b47c6ff1eb884e40debf36ea92d7f5f96051c bytes=466 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/spi_communications/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/spi_communications/__init__.py`
- sha256: `54dbf44d7a62bddf694a4921401b47c6ff1eb884e40debf36ea92d7f5f96051c`
- bytes: 466

````python
"""Provides a set of integration tests for 
   nipcbatt.pcbatt_library.spi_communications package"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (349 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/spi_communications/test_integration_spi_read_communication.py sha256=78addfd806d3a19a8992b177b8fa6ed01657521eda712f4b8ecdea42d4f46fa1 bytes=3934 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/spi_communications/test_integration_spi_read_communication.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/spi_communications/test_integration_spi_read_communication.py`
- sha256: `78addfd806d3a19a8992b177b8fa6ed01657521eda712f4b8ecdea42d4f46fa1`
- bytes: 3934

````python
"""This module provides test of integration of SpiReadCommunication."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_communication_library._ni_845x_internal import _ni_845x_functions
from nipcbatt import communications


class TestIntegrationSpiReadCommunication(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `SpiReadCommunication` class.

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

    @unittest.skipIf(
        not (
            _ni_845x_functions.is_ni_845x_installed() and _ni_845x_functions.ni_845x_device_exists()
        ),
        "The execution of test is skipped"
        + " because Ni-845x driver is not installed or no NI 845x device found on system.",
    )
    def test_integration_spi_read_communication(self):
        """Integration test of
        communications.pcbatt_library.spi_communications.spi_read_communication.SpiReadCommunication
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with communications.SpiReadCommunication() as communication:
            communication.initialize("USB-8452")

            device_parameters = communications.SpiDeviceParameters(
                voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_33,
            )
            communication_parameters = communications.SpiCommunicationParameters(
                chip_select=0,
                clock_rate_kilohertz=1000,
                clock_phase=nipcbatt.SpiConfigurationClockPhase.CLOCK_PHASE_FIRST_EDGE,
                clock_polarity=nipcbatt.SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW,
            )
            read_parameters = communications.SpiReadParameters(
                number_of_bytes_to_read=32,
                memory_address_parameters=nipcbatt.MemoryAddressParameters(
                    memory_address=0,
                    address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                    address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
                ),
            )
            configuration = communications.SpiReadCommunicationConfiguration(
                device_parameters=device_parameters,
                communication_parameters=communication_parameters,
                read_parameters=read_parameters,
            )

            print(f"parameters = {configuration}")
            results = communication.configure_and_read_data(configuration=configuration)
            print(f"results = {results}")
            self.assertIsNotNone(results)
            self.assertIsInstance(results, communications.SpiReadCommunicationData)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/spi_communications/test_integration_spi_write_communication.py sha256=15a330f2bc3451bff276576e77f846c7327694d873f262d547045435abfd6a7d bytes=4428 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/spi_communications/test_integration_spi_write_communication.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/spi_communications/test_integration_spi_write_communication.py`
- sha256: `15a330f2bc3451bff276576e77f846c7327694d873f262d547045435abfd6a7d`
- bytes: 4428

````python
"""This module provides test of integration of SpiWriteCommunication."""

import importlib.metadata
import logging
import sys
import unittest

import numpy
from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_communication_library._ni_845x_internal import _ni_845x_functions


class TestIntegrationSpiWriteCommunication(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `SpiWriteCommunication` class.

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

    @unittest.skipIf(
        not (
            _ni_845x_functions.is_ni_845x_installed() and _ni_845x_functions.ni_845x_device_exists()
        ),
        "The execution of test is skipped"
        + " because Ni-845x driver is not installed or no NI 845x device found on system.",
    )
    def test_integration_spi_write_communication(self):
        """Integration test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_communication.SpiWriteCommunication
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with nipcbatt.SpiWriteCommunication() as communication:
            communication.initialize("USB-8452")

            device_parameters = nipcbatt.SpiDeviceParameters(
                voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_33,
            )
            communication_parameters = nipcbatt.SpiCommunicationParameters(
                chip_select=0,
                clock_rate_kilohertz=1000,
                clock_phase=nipcbatt.SpiConfigurationClockPhase.CLOCK_PHASE_FIRST_EDGE,
                clock_polarity=nipcbatt.SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW,
            )
            write_parameters = nipcbatt.SpiWriteParameters(
                number_of_bytes_per_page=1,
                delay_between_page_write_operations_milliseconds=500,
                data_to_be_written=numpy.array(
                    [
                        175,
                        166,
                        174,
                        175,
                        129,
                        207,
                        174,
                        175,
                        1,
                        129,
                        32,
                        129,
                        96,
                        129,
                        96,
                        129,
                        207,
                        174,
                    ]
                ),
                memory_address_parameters=nipcbatt.MemoryAddressParameters(
                    memory_address=0,
                    address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                    address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
                ),
            )
            configuration = nipcbatt.SpiWriteCommunicationConfiguration(
                device_parameters=device_parameters,
                communication_parameters=communication_parameters,
                write_parameters=write_parameters,
            )

            print(f"parameters = {configuration}")
            communication.configure_and_write_data(configuration=configuration)


if __name__ == "__main__":
    unittest.main()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_path_generations/__init__.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_path_generations/__init__.py

- repository: `ni/nipcbatt`
- source_path: `tests/nipcbatt_tests/pcbatt_library_integration_tests/static_digital_path_generations/__init__.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````
