# NI OSS SOURCE SNAPSHOT: measurement-plugin-python

<!--NI_OSS_SNAPSHOT repo=ni/measurement-plugin-python commit=2e57ec3e5bd703abc8690f8a46df62b28f0380e2 -->

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/fake_rpc_error.py sha256=b3678a386b2d7b65785f7f4e85a9568dd39c130c529decaad3ba765721ba7b8a bytes=557 -->
## FILE: packages/service/tests/utilities/fake_rpc_error.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/fake_rpc_error.py`
- sha256: `b3678a386b2d7b65785f7f4e85a9568dd39c130c529decaad3ba765721ba7b8a`
- bytes: 557

````python
"""A throwable version of grpc.RpcError for testing."""

import grpc


class FakeRpcError(grpc.RpcError):
    """A throwable version of grpc.RpcError for testing."""

    def __init__(self, code: grpc.StatusCode, details: str) -> None:
        """Construct a FakeRpcError."""
        self._code = code
        self._details = details

    def code(self) -> grpc.StatusCode:
        """Get the gRPC status code."""
        return self._code

    def details(self) -> str:
        """Get the error details."""
        return self._details
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/__init__.py sha256=4aecea293944730886837467665e01cdffc928b2106c6e1fc1093d2ecf4f6020 bytes=26 -->
## FILE: packages/service/tests/utilities/measurements/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/__init__.py`
- sha256: `4aecea293944730886837467665e01cdffc928b2106c6e1fc1093d2ecf4f6020`
- bytes: 26

````python
"""Test measurements."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/loopback_measurement/__init__.py sha256=f47b2e98b72bc65ef66a7314a6702ef83f5975abeae45653389aee5be51faf0a bytes=2950 -->
## FILE: packages/service/tests/utilities/measurements/loopback_measurement/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/loopback_measurement/__init__.py`
- sha256: `f47b2e98b72bc65ef66a7314a6702ef83f5975abeae45653389aee5be51faf0a`
- bytes: 2950

````python
"""Contains utility functions to test loopback measurement service."""

from __future__ import annotations

import pathlib
from collections.abc import Iterable
from enum import Enum
from typing import Tuple

import ni_measurement_plugin_sdk_service as nims
from tests.utilities.measurements.sample_measurement._stubs import color_pb2


class Color(Enum):
    """Primary colors used for example enum-typed config and output."""

    NONE = 0
    RED = 1
    GREEN = 2
    BLUE = 3


service_directory = pathlib.Path(__file__).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "LoopbackMeasurement.serviceconfig",
    ui_file_paths=[
        service_directory,
    ],
)


@measurement_service.register_measurement
@measurement_service.configuration("Float In", nims.DataType.Float, 0.06)
@measurement_service.configuration("Double Array In", nims.DataType.DoubleArray1D, [0.1, 0.2, 0.3])
@measurement_service.configuration("Bool In", nims.DataType.Boolean, False)
@measurement_service.configuration("String In", nims.DataType.String, "sample string")
@measurement_service.configuration("Enum In", nims.DataType.Enum, Color.BLUE, enum_type=Color)
@measurement_service.configuration(
    "Protobuf Enum In",
    nims.DataType.Enum,
    color_pb2.ProtobufColor.BLACK,
    enum_type=color_pb2.ProtobufColor,
)
@measurement_service.configuration(
    "String Array In", nims.DataType.StringArray1D, ["String1", "String2"]
)
@measurement_service.output("Float out", nims.DataType.Float)
@measurement_service.output("Double Array out", nims.DataType.DoubleArray1D)
@measurement_service.output("Bool out", nims.DataType.Boolean)
@measurement_service.output("String out", nims.DataType.String)
@measurement_service.output("Enum out", nims.DataType.Enum, enum_type=Color)
@measurement_service.output(
    "Protobuf Enum out", nims.DataType.Enum, enum_type=color_pb2.ProtobufColor
)
@measurement_service.output("String Array out", nims.DataType.StringArray1D)
def measure(
    float_input: float,
    double_array_input: Iterable[float],
    bool_input: bool,
    string_input: str,
    enum_input: Color,
    protobuf_enum_input: color_pb2.ProtobufColor.ValueType,
    string_array_in: Iterable[str],
) -> tuple[
    float, Iterable[float], bool, str, Color, color_pb2.ProtobufColor.ValueType, Iterable[str]
]:
    """Perform a loopback measurement with various data types."""
    float_output = float_input
    float_array_output = double_array_input
    bool_output = bool_input
    string_output = string_input
    enum_output = enum_input
    protobuf_enum_output = protobuf_enum_input
    string_array_out = string_array_in

    return (
        float_output,
        float_array_output,
        bool_output,
        string_output,
        enum_output,
        protobuf_enum_output,
        string_array_out,
    )
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/loopback_measurement/LoopbackMeasurement.serviceconfig sha256=e565247978ba58f176f5ffea48a5bfbd212af564332d323f21e1d7af625576de bytes=656 -->
## FILE: packages/service/tests/utilities/measurements/loopback_measurement/LoopbackMeasurement.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/loopback_measurement/LoopbackMeasurement.serviceconfig`
- sha256: `e565247978ba58f176f5ffea48a5bfbd212af564332d323f21e1d7af625576de`
- bytes: 656

````json
{
  "services": [
    {
      "displayName": "Loopback Measurement (Py)",
      "serviceClass": "ni.tests.LoopbackMeasurement_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "version": "1.2.3.4",
      "path": "start.bat",
      "annotations": {
        "ni/service.description": "Measurement plug-in test service that performs a loopback measurement with various data types.",
        "ni/service.collection": "NI.Tests",
        "ni/service.tags": []
      }

    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/nidaqmx_measurement/__init__.py sha256=ddade557b51a246bd17fae5faf096a1dfbed2b373f8d9ea1f5c23cd0a7df9c39 bytes=3993 -->
## FILE: packages/service/tests/utilities/measurements/nidaqmx_measurement/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/nidaqmx_measurement/__init__.py`
- sha256: `ddade557b51a246bd17fae5faf096a1dfbed2b373f8d9ea1f5c23cd0a7df9c39`
- bytes: 3993

````python
"""NI-DAQmx measurement plug-in test service."""

from __future__ import annotations

import pathlib
from collections.abc import Iterable, Sequence
from typing import List

import nidaqmx
from ni.measurementlink.sessionmanagement.v1.client import TypedSessionInformation

import ni_measurement_plugin_sdk_service as nims

service_directory = pathlib.Path(__file__).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "NIDAQmxMeasurement.serviceconfig",
    ui_file_paths=[
        service_directory,
    ],
)


@measurement_service.register_measurement
@measurement_service.configuration("pin_names", nims.DataType.IOResourceArray1D, ["Pin1"])
@measurement_service.configuration("multi_session", nims.DataType.Boolean, False)
@measurement_service.output("session_names", nims.DataType.StringArray1D)
@measurement_service.output("resource_names", nims.DataType.StringArray1D)
@measurement_service.output("channel_lists", nims.DataType.StringArray1D)
@measurement_service.output("connected_channels", nims.DataType.StringArray1D)
@measurement_service.output("voltage_values", nims.DataType.DoubleArray1D)
def measure(
    pin_names: Iterable[str],
    multi_session: bool,
) -> tuple[list[str], list[str], list[str], list[str], list[float]]:
    """NI-DAQmx measurement plug-in test service."""
    if multi_session:
        with measurement_service.context.reserve_sessions(pin_names) as reservation:
            with reservation.create_nidaqmx_tasks() as session_infos:
                connections = reservation.get_nidaqmx_connections(pin_names)
                assert all([session_info.session is not None for session_info in session_infos])
                voltage_values = _read_voltage_values(session_infos)

                return (
                    [session_info.session_name for session_info in session_infos],
                    [session_info.resource_name for session_info in session_infos],
                    [session_info.channel_list for session_info in session_infos],
                    [connection.channel_name for connection in connections],
                    voltage_values,
                )

    else:
        with measurement_service.context.reserve_session(pin_names) as reservation:
            with reservation.create_nidaqmx_task() as session_info:
                connection = reservation.get_nidaqmx_connection(list(pin_names)[0])
                assert session_info.session is not None
                voltage_values = _read_voltage_values([session_info])

                return (
                    [session_info.resource_name],
                    [session_info.resource_name],
                    [session_info.channel_list],
                    [connection.channel_name],
                    voltage_values,
                )


def _read_voltage_values(
    session_infos: Sequence[TypedSessionInformation[nidaqmx.Task]],
) -> list[float]:
    sample_rate = 1000.0
    number_of_samples = 2
    number_of_samples_to_read = 1

    voltage_values = []
    for session_info in session_infos:
        task = session_info.session

        # If we created a new DAQmx task, we must also add channels to it.
        if not session_info.session_exists:
            task.ai_channels.add_ai_voltage_chan(session_info.channel_list)

        task.timing.cfg_samp_clk_timing(
            rate=sample_rate,
            samps_per_chan=number_of_samples,
        )

    for session_info in session_infos:
        session_info.session.start()

    for session_info in session_infos:
        task = session_info.session
        timeout = min(measurement_service.context.time_remaining, 10.0)
        voltage_value = task.read(number_of_samples_to_read, timeout)[0]
        voltage_values.append(voltage_value)

    for session_info in session_infos:
        session_info.session.stop()

    return voltage_values
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/nidaqmx_measurement/NIDAQmxMeasurement.serviceconfig sha256=33ec626c2c3003047dca13e43016175adb30470114f88898c699a810b7046cbe bytes=621 -->
## FILE: packages/service/tests/utilities/measurements/nidaqmx_measurement/NIDAQmxMeasurement.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/nidaqmx_measurement/NIDAQmxMeasurement.serviceconfig`
- sha256: `33ec626c2c3003047dca13e43016175adb30470114f88898c699a810b7046cbe`
- bytes: 621

````json
{
  "services": [
    {
      "displayName": "NI-DAQmx Analog Input (Py)",
      "serviceClass": "ni.tests.NIDAQmxAnalogInput_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "annotations": {
        "ni/service.description": "Measurement plug-in example that performs a finite analog input measurement with NI-DAQmx.",
        "ni/service.collection": "NI.Tests",
        "ni/service.tags": []
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/nidcpower_measurement/__init__.py sha256=f4ffc13be6f0100d344dc0859cff5464bab0e3a4d326ea073e681816a6f65e81 bytes=4741 -->
## FILE: packages/service/tests/utilities/measurements/nidcpower_measurement/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/nidcpower_measurement/__init__.py`
- sha256: `f4ffc13be6f0100d344dc0859cff5464bab0e3a4d326ea073e681816a6f65e81`
- bytes: 4741

````python
"""NI-DCPower measurement plug-in test service."""

from __future__ import annotations

import pathlib
from collections.abc import Iterable, Sequence
from contextlib import ExitStack
from typing import List

import hightime
import nidcpower
from ni.measurementlink.sessionmanagement.v1.client import TypedConnection

import ni_measurement_plugin_sdk_service as nims

service_directory = pathlib.Path(__file__).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "NIDCPowerMeasurement.serviceconfig",
    ui_file_paths=[
        service_directory,
    ],
)


@measurement_service.register_measurement
@measurement_service.configuration("pin_names", nims.DataType.IOResourceArray1D, ["Pin1"])
@measurement_service.configuration("multi_session", nims.DataType.Boolean, False)
@measurement_service.output("session_names", nims.DataType.StringArray1D)
@measurement_service.output("resource_names", nims.DataType.StringArray1D)
@measurement_service.output("channel_lists", nims.DataType.StringArray1D)
@measurement_service.output("connected_channels", nims.DataType.StringArray1D)
@measurement_service.output("voltage_measurements", nims.DataType.DoubleArray1D)
@measurement_service.output("current_measurements", nims.DataType.DoubleArray1D)
def measure(
    pin_names: Iterable[str],
    multi_session: bool,
) -> tuple[
    Iterable[str], Iterable[str], Iterable[str], Iterable[str], Iterable[float], Iterable[float]
]:
    """NI-DCPower measurement plug-in test service."""
    if multi_session:
        with measurement_service.context.reserve_sessions(pin_names) as reservation:
            with reservation.initialize_nidcpower_sessions() as session_infos:
                connections = reservation.get_nidcpower_connections(pin_names)
                assert all([session_info.session is not None for session_info in session_infos])
                voltage_measurements, current_measurements = _source_measure_dc_voltage(connections)

                return (
                    [session_info.session_name for session_info in session_infos],
                    [session_info.resource_name for session_info in session_infos],
                    [session_info.channel_list for session_info in session_infos],
                    [connection.channel_name for connection in connections],
                    voltage_measurements,
                    current_measurements,
                )
    else:
        with measurement_service.context.reserve_session(pin_names) as reservation:
            with reservation.initialize_nidcpower_session() as session_info:
                connection = reservation.get_nidcpower_connection(list(pin_names)[0])
                assert session_info.session is not None
                voltage_measurements, current_measurements = _source_measure_dc_voltage(
                    [connection]
                )

                return (
                    [session_info.resource_name],
                    [session_info.resource_name],
                    [session_info.channel_list],
                    [connection.channel_name],
                    [voltage_measurements[0]],
                    [current_measurements[0]],
                )


def _source_measure_dc_voltage(
    connections: Sequence[TypedConnection[nidcpower.Session]],
) -> tuple[list[float], list[float]]:
    for connection in connections:
        channel = connection.session.channels[connection.channel_name]
        channel.source_mode = nidcpower.SourceMode.SINGLE_POINT
        channel.output_function = nidcpower.OutputFunction.DC_VOLTAGE
        channel.current_limit = 0.01
        channel.voltage_level_range = 10.0
        channel.current_limit_range = 0.01
        channel.source_delay = hightime.timedelta(seconds=0.1)
        channel.voltage_level = 5.0

    voltage_measurements, current_measurements = [], []
    with ExitStack() as stack:
        for connection in connections:
            channel = connection.session.channels[connection.channel_name]
            stack.enter_context(channel.initiate())

        for connection in connections:
            channel = connection.session.channels[connection.channel_name]
            channel.wait_for_event(nidcpower.enums.Event.SOURCE_COMPLETE, timeout=10.0)

        for connection in connections:
            channel = connection.session.channels[connection.channel_name]
            measurement = channel.measure_multiple()[0]
            voltage_measurements.append(measurement.voltage)
            current_measurements.append(measurement.current)

    return (voltage_measurements, current_measurements)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/nidcpower_measurement/NIDCPowerMeasurement.serviceconfig sha256=26258063de1ae256fbe7158ce94f83b8124ba865deec71023c8c00a44fa7064a bytes=578 -->
## FILE: packages/service/tests/utilities/measurements/nidcpower_measurement/NIDCPowerMeasurement.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/nidcpower_measurement/NIDCPowerMeasurement.serviceconfig`
- sha256: `26258063de1ae256fbe7158ce94f83b8124ba865deec71023c8c00a44fa7064a`
- bytes: 578

````json
{
  "services": [
    {
      "displayName": "NI-DCPower Measurement (Py)",
      "serviceClass": "ni.tests.NIDCPowerMeasurement_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "annotations": {
        "ni/service.description": "NI-DCPower measurement plug-in test service.",
        "ni/service.collection": "NI.Tests",
        "ni/service.tags": []
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/nidigital_measurement/__init__.py sha256=118032dce2bf4fad0a9b55a8825d4ebd2bf545a57ed07c4f16378e1649bbb3d0 bytes=6271 -->
## FILE: packages/service/tests/utilities/measurements/nidigital_measurement/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/nidigital_measurement/__init__.py`
- sha256: `118032dce2bf4fad0a9b55a8825d4ebd2bf545a57ed07c4f16378e1649bbb3d0`
- bytes: 6271

````python
"""NI-Digital measurement plug-in test service."""

from __future__ import annotations

import pathlib
from collections.abc import Iterable, Sequence
from itertools import groupby
from typing import Tuple

import nidigital
from ni.measurementlink.sessionmanagement.v1.client import (
    TypedConnection,
    TypedSessionInformation,
)

import ni_measurement_plugin_sdk_service as nims

service_directory = pathlib.Path(__file__).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "NIDigitalMeasurement.serviceconfig",
    ui_file_paths=[
        service_directory,
    ],
)


@measurement_service.register_measurement
@measurement_service.configuration("pin_names", nims.DataType.StringArray1D, ["CS"])
@measurement_service.configuration("multi_session", nims.DataType.Boolean, False)
@measurement_service.output("session_names", nims.DataType.StringArray1D)
@measurement_service.output("resource_names", nims.DataType.StringArray1D)
@measurement_service.output("channel_lists", nims.DataType.StringArray1D)
@measurement_service.output("connected_channels", nims.DataType.StringArray1D)
@measurement_service.output("passing_sites", nims.DataType.Int32Array1D)
@measurement_service.output("failing_sites", nims.DataType.Int32Array1D)
def measure(
    pin_names: Iterable[str],
    multi_session: bool,
) -> tuple[
    Iterable[str], Iterable[str], Iterable[str], Iterable[str], Iterable[int], Iterable[int]
]:
    """NI-Digital measurement plug-in test service."""
    if multi_session:
        with measurement_service.context.reserve_sessions(pin_names) as reservation:
            with reservation.initialize_nidigital_sessions() as session_infos:
                connections = reservation.get_nidigital_connections(pin_names)
                assert all([session_info.session is not None for session_info in session_infos])
                passing_sites, failing_sites = _burst_spi_pattern(session_infos)
                connections_by_session = [
                    list(g) for _, g in groupby(sorted(connections, key=_key_func), key=_key_func)
                ]

                return (
                    [session_info.session_name for session_info in session_infos],
                    [session_info.resource_name for session_info in session_infos],
                    [session_info.channel_list for session_info in session_infos],
                    [
                        ", ".join(conn.channel_name for conn in conns)
                        for conns in connections_by_session
                    ],
                    passing_sites,
                    failing_sites,
                )
    else:
        with measurement_service.context.reserve_session(pin_names) as reservation:
            with reservation.initialize_nidigital_session() as session_info:
                connection = reservation.get_nidigital_connection(list(pin_names)[0])
                assert session_info.session is not None
                passing_sites, failing_sites = _burst_spi_pattern([session_info])

                return (
                    [session_info.session_name],
                    [session_info.resource_name],
                    [session_info.channel_list],
                    [connection.channel_name],
                    passing_sites,
                    failing_sites,
                )


def _burst_spi_pattern(
    session_infos: Sequence[TypedSessionInformation[nidigital.Session]],
) -> tuple[list[int], list[int]]:
    specifications_file_path = "Specifications.specs"
    levels_file_path = "PinLevels.digilevels"
    timing_file_path = "Timing.digitiming"
    pattern_file_path = "Pattern.digipat"
    pin_map_context = measurement_service.context.pin_map_context
    selected_sites_string = ",".join(f"site{i}" for i in pin_map_context.sites or [])

    passing_sites_list, failing_sites_list = [], []
    for session_info in session_infos:
        session = session_info.session
        selected_sites = session.sites[selected_sites_string]

        if not session_info.session_exists:
            session.load_pin_map(pin_map_context.pin_map_id)
            session.load_specifications_levels_and_timing(
                str(_resolve_relative_path(service_directory, specifications_file_path)),
                str(_resolve_relative_path(service_directory, levels_file_path)),
                str(_resolve_relative_path(service_directory, timing_file_path)),
            )
            session.load_pattern(
                str(_resolve_relative_path(service_directory, pattern_file_path)),
            )

    levels_file_name = pathlib.Path(levels_file_path).stem
    timing_file_name = pathlib.Path(timing_file_path).stem

    for session_info in session_infos:
        selected_sites = session_info.session.sites[selected_sites_string]
        selected_sites.apply_levels_and_timing(levels_file_name, timing_file_name)

    for session_info in session_infos:
        selected_sites = session_info.session.sites[selected_sites_string]
        selected_sites.burst_pattern(start_label="SPI_Pattern", wait_until_done=False)

    for session_info in session_infos:
        selected_sites = session_info.session.sites[selected_sites_string]
        session_info.session.wait_until_done()
        site_pass_fail = selected_sites.get_site_pass_fail()
        passing_sites = [site for site, pass_fail in site_pass_fail.items() if pass_fail]
        failing_sites = [site for site, pass_fail in site_pass_fail.items() if not pass_fail]
        passing_sites_list.extend(passing_sites)
        failing_sites_list.extend(failing_sites)
        session.selected_function = nidigital.SelectedFunction.DISCONNECT

    return (passing_sites_list, failing_sites_list)


def _resolve_relative_path(
    directory_path: pathlib.Path, file_path: str | pathlib.Path
) -> pathlib.Path:
    file_path = pathlib.Path(file_path)
    if file_path.is_absolute():
        return file_path
    else:
        return (directory_path / file_path).resolve()


def _key_func(conn: TypedConnection[nidigital.Session]) -> str:
    return conn.session_info.session_name
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/nidigital_measurement/NIDigitalMeasurement.serviceconfig sha256=516ddb63e235d4459b7fbd1669981157c43aef23b42c37e1400769b128081950 bytes=578 -->
## FILE: packages/service/tests/utilities/measurements/nidigital_measurement/NIDigitalMeasurement.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/nidigital_measurement/NIDigitalMeasurement.serviceconfig`
- sha256: `516ddb63e235d4459b7fbd1669981157c43aef23b42c37e1400769b128081950`
- bytes: 578

````json
{
  "services": [
    {
      "displayName": "NI-Digital Measurement (Py)",
      "serviceClass": "ni.tests.NIDigitalMeasurement_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "annotations": {
        "ni/service.description": "NI-Digital measurement plug-in test service.",
        "ni/service.collection": "NI.Tests",
        "ni/service.tags": []
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/nidigital_measurement/PinLevels.digilevels sha256=736ee06c9eb56920fffc3849d2d8c575f4a9c43daeb9c6e2bd53b66bb5894f31 bytes=1632 -->
## FILE: packages/service/tests/utilities/measurements/nidigital_measurement/PinLevels.digilevels

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/nidigital_measurement/PinLevels.digilevels`
- sha256: `736ee06c9eb56920fffc3849d2d8c575f4a9c43daeb9c6e2bd53b66bb5894f31`
- bytes: 1632

````text
<?xml version="1.0" encoding="utf-8"?>
<PinLevelsFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/PinLevels">
  <PinLevelsSheet>
    <DigitalPinLevelSets>
      <DigitalPinLevelSet pin="CS">
        <Vil>dc.vcc * 0.7</Vil>
        <Vih>0</Vih>
        <Vol>2.5</Vol>
        <Voh>0.5</Voh>
        <Iol>1.5 m</Iol>
        <Ioh>-1.5 m</Ioh>
        <Vcom>0</Vcom>
        <Vterm>0</Vterm>
        <TerminationMode>HighZ</TerminationMode>
      </DigitalPinLevelSet>
      <DigitalPinLevelSet pin="SCLK">
        <Vil>dc.vcc * 0.7</Vil>
        <Vih>0</Vih>
        <Vol>2.5</Vol>
        <Voh>0.5</Voh>
        <Iol>1.5 m</Iol>
        <Ioh>-1.5 m</Ioh>
        <Vcom>0</Vcom>
        <Vterm>0</Vterm>
        <TerminationMode>HighZ</TerminationMode>
      </DigitalPinLevelSet>
      <DigitalPinLevelSet pin="MOSI">
        <Vil>dc.vcc * 0.7</Vil>
        <Vih>0</Vih>
        <Vol>2.5</Vol>
        <Voh>0.5</Voh>
        <Iol>1.5 m</Iol>
        <Ioh>-1.5 m</Ioh>
        <Vcom>0</Vcom>
        <Vterm>0</Vterm>
        <TerminationMode>HighZ</TerminationMode>
      </DigitalPinLevelSet>
      <DigitalPinLevelSet pin="MISO">
        <Vil>dc.vcc * 0.7</Vil>
        <Vih>0</Vih>
        <Vol>2.5</Vol>
        <Voh>0.5</Voh>
        <Iol>1.5 m</Iol>
        <Ioh>-1.5 m</Ioh>
        <Vcom>0</Vcom>
        <Vterm>0</Vterm>
        <TerminationMode>HighZ</TerminationMode>
      </DigitalPinLevelSet>
    </DigitalPinLevelSets>
  </PinLevelsSheet>
</PinLevelsFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/nidigital_measurement/Specifications.specs sha256=52670a64f710ba837694327d5f532b8e6406b7872be001e9d461ab533c3a02a9 bytes=586 -->
## FILE: packages/service/tests/utilities/measurements/nidigital_measurement/Specifications.specs

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/nidigital_measurement/Specifications.specs`
- sha256: `52670a64f710ba837694327d5f532b8e6406b7872be001e9d461ab533c3a02a9`
- bytes: 586

````text
<?xml version="1.0" encoding="utf-8"?>
<Specifications xmlns:f="http://www.ni.com/schemas/Semiconductor/Formula.xsd" schemaVersion="1.0" xmlns="http://www.ni.com/schemas/Semiconductor/Specifications.xsd">
  <Section name="dc">
    <f:Formula symbol="vcc">
      <f:Definition>5</f:Definition>
      <f:Description>V</f:Description>
    </f:Formula>
  </Section>
  <Section name="ac">
    <f:Formula symbol="period">
      <f:Definition>1 / 1000000</f:Definition>
      <f:Description>1 MHz</f:Description>
    </f:Formula>
  </Section>
  <Description />
</Specifications>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/nidigital_measurement/Timing.digitiming sha256=f142d9372d74e6116a91f0b9e462dd486843a001aa69d5a957767115eb9160d2 bytes=1938 -->
## FILE: packages/service/tests/utilities/measurements/nidigital_measurement/Timing.digitiming

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/nidigital_measurement/Timing.digitiming`
- sha256: `f142d9372d74e6116a91f0b9e462dd486843a001aa69d5a957767115eb9160d2`
- bytes: 1938

````text
<?xml version="1.0" encoding="utf-8"?>
<TimingFile xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.0" xmlns="http://www.ni.com/Semiconductor/Timing">
  <TimingSheet>
    <TimeSets>
      <TimeSet name="SPI">
        <Period>ac.period</Period>
        <PinEdges>
          <PinEdge pin="CS">
            <DriveNonReturn>
              <On>0</On>
              <Data>0</Data>
              <Off>ac.period</Off>
            </DriveNonReturn>
            <CompareStrobe>
              <Strobe>(3 * ac.period) / 4</Strobe>
            </CompareStrobe>
            <DataSource>Pattern</DataSource>
          </PinEdge>
          <PinEdge pin="SCLK">
            <ReturnToLow>
              <On>ac.period / 2</On>
              <Data>ac.period / 2</Data>
              <Return>ac.period</Return>
              <Off>ac.period</Off>
            </ReturnToLow>
            <CompareStrobe>
              <Strobe>(3 * ac.period) / 4</Strobe>
            </CompareStrobe>
            <DataSource>Pattern</DataSource>
          </PinEdge>
          <PinEdge pin="MOSI">
            <DriveNonReturn>
              <On>0</On>
              <Data>0</Data>
              <Off>ac.period</Off>
            </DriveNonReturn>
            <CompareStrobe>
              <Strobe>(3 * ac.period) / 4</Strobe>
            </CompareStrobe>
            <DataSource>Pattern</DataSource>
          </PinEdge>
          <PinEdge pin="MISO">
            <DriveNonReturn>
              <On>0</On>
              <Data>0</Data>
              <Off>ac.period</Off>
            </DriveNonReturn>
            <CompareStrobe>
              <Strobe>(3 * ac.period) / 4</Strobe>
            </CompareStrobe>
            <DataSource>Pattern</DataSource>
          </PinEdge>
        </PinEdges>
      </TimeSet>
    </TimeSets>
  </TimingSheet>
</TimingFile>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/nidmm_measurement/__init__.py sha256=40d1d44d20a3d52b288ef27079ea9f9a31948d4386ec19666b2fa37f4296274e bytes=4045 -->
## FILE: packages/service/tests/utilities/measurements/nidmm_measurement/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/nidmm_measurement/__init__.py`
- sha256: `40d1d44d20a3d52b288ef27079ea9f9a31948d4386ec19666b2fa37f4296274e`
- bytes: 4045

````python
"""NI-DMM measurement plug-in test service."""

from __future__ import annotations

import math
import pathlib
from collections.abc import Iterable, Sequence
from typing import List

import nidmm
from ni.measurementlink.sessionmanagement.v1.client import TypedSessionInformation

import ni_measurement_plugin_sdk_service as nims

service_directory = pathlib.Path(__file__).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "NIDmmMeasurement.serviceconfig",
    ui_file_paths=[
        service_directory,
    ],
)


@measurement_service.register_measurement
@measurement_service.configuration("pin_names", nims.DataType.IOResourceArray1D, ["Pin1"])
@measurement_service.configuration("multi_session", nims.DataType.Boolean, False)
@measurement_service.output("session_names", nims.DataType.StringArray1D)
@measurement_service.output("resource_names", nims.DataType.StringArray1D)
@measurement_service.output("channel_lists", nims.DataType.StringArray1D)
@measurement_service.output("connected_channels", nims.DataType.StringArray1D)
@measurement_service.output("signals_out_of_range", nims.DataType.BooleanArray1D)
@measurement_service.output("absolute_resolutions", nims.DataType.DoubleArray1D)
def measure(
    pin_names: Iterable[str],
    multi_session: bool,
) -> tuple[list[str], list[str], list[str], list[str], list[bool], list[float]]:
    """NI-DMM measurement plug-in test service."""
    if multi_session:
        with measurement_service.context.reserve_sessions(pin_names) as reservation:
            with reservation.initialize_nidmm_sessions() as session_infos:
                connections = reservation.get_nidmm_connections(pin_names)
                assert all([session_info.session is not None for session_info in session_infos])
                signals_out_of_range, absolute_resolutions = _get_dmm_readings(session_infos)

                return (
                    [session_info.session_name for session_info in session_infos],
                    [session_info.resource_name for session_info in session_infos],
                    [session_info.channel_list for session_info in session_infos],
                    [connection.channel_name for connection in connections],
                    signals_out_of_range,
                    absolute_resolutions,
                )

    else:
        with measurement_service.context.reserve_session(pin_names) as reservation:
            with reservation.initialize_nidmm_session() as session_info:
                connection = reservation.get_nidmm_connection(list(pin_names)[0])
                assert session_info.session is not None
                signals_out_of_range, absolute_resolutions = _get_dmm_readings([session_info])

                return (
                    [session_info.resource_name],
                    [session_info.resource_name],
                    [session_info.channel_list],
                    [connection.channel_name],
                    signals_out_of_range,
                    absolute_resolutions,
                )


def _get_dmm_readings(
    session_infos: Sequence[TypedSessionInformation[nidmm.Session]],
) -> tuple[list[bool], list[float]]:
    nidmm_function = nidmm.Function(nidmm.Function.DC_VOLTS.value)
    range = 10.0
    resolution_digits = 5.5

    signals_out_of_range, absolute_resolutions = [], []
    for session_info in session_infos:
        session_info.session.configure_measurement_digits(nidmm_function, range, resolution_digits)

    for session_info in session_infos:
        session = session_info.session
        measured_value = session.read()
        signal_out_of_range = math.isnan(measured_value) or math.isinf(measured_value)
        absolute_resolution = session.resolution_absolute
        signals_out_of_range.append(signal_out_of_range)
        absolute_resolutions.append(absolute_resolution)

    return (signals_out_of_range, absolute_resolutions)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/nidmm_measurement/NIDmmMeasurement.serviceconfig sha256=507b7256aa2193b009917cd1f8752fa3fd0bc497df99917063481cb8a5a7653e bytes=566 -->
## FILE: packages/service/tests/utilities/measurements/nidmm_measurement/NIDmmMeasurement.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/nidmm_measurement/NIDmmMeasurement.serviceconfig`
- sha256: `507b7256aa2193b009917cd1f8752fa3fd0bc497df99917063481cb8a5a7653e`
- bytes: 566

````json
{
  "services": [
    {
      "displayName": "NI-DMM Measurement (Py)",
      "serviceClass": "ni.tests.NIDMMMeasurement_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "annotations": {
        "ni/service.description": "NI-DMM measurement plug-in test service.",
        "ni/service.collection": "NI.Tests",
        "ni/service.tags": []
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/nifgen_measurement/__init__.py sha256=36ac447e6e978d7f2b7761253902d76c7f9accab0683a288ce740d70465239c0 bytes=3284 -->
## FILE: packages/service/tests/utilities/measurements/nifgen_measurement/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/nifgen_measurement/__init__.py`
- sha256: `36ac447e6e978d7f2b7761253902d76c7f9accab0683a288ce740d70465239c0`
- bytes: 3284

````python
"""NI-FGEN measurement plug-in test service."""

from __future__ import annotations

import pathlib
from collections.abc import Iterable, Sequence
from contextlib import ExitStack
from typing import Tuple

import nifgen
from ni.measurementlink.sessionmanagement.v1.client import TypedSessionInformation

import ni_measurement_plugin_sdk_service as nims

service_directory = pathlib.Path(__file__).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "NIFgenMeasurement.serviceconfig",
    ui_file_paths=[
        service_directory,
    ],
)


@measurement_service.register_measurement
@measurement_service.configuration("pin_names", nims.DataType.IOResourceArray1D, ["Pin1"])
@measurement_service.configuration("multi_session", nims.DataType.Boolean, False)
@measurement_service.output("session_names", nims.DataType.StringArray1D)
@measurement_service.output("resource_names", nims.DataType.StringArray1D)
@measurement_service.output("channel_lists", nims.DataType.StringArray1D)
@measurement_service.output("connected_channels", nims.DataType.StringArray1D)
def measure(
    pin_names: Iterable[str], multi_session: bool
) -> tuple[Iterable[str], Iterable[str], Iterable[str], Iterable[str]]:
    """NI-FGEN measurement plug-in test service."""
    if multi_session:
        with measurement_service.context.reserve_sessions(pin_names) as reservation:
            with reservation.initialize_nifgen_sessions() as session_infos:
                assert all([session_info.session is not None for session_info in session_infos])
                connections = reservation.get_nifgen_connections(pin_names)
                _generate_standard_waveform(session_infos)

                return (
                    [session_info.session_name for session_info in session_infos],
                    [session_info.resource_name for session_info in session_infos],
                    [session_info.channel_list for session_info in session_infos],
                    [connection.channel_name for connection in connections],
                )
    else:
        with measurement_service.context.reserve_session(pin_names) as reservation:
            with reservation.initialize_nifgen_session() as session_info:
                assert session_info.session is not None
                connection = reservation.get_nifgen_connection(list(pin_names)[0])
                _generate_standard_waveform([session_info])

                return (
                    [session_info.resource_name],
                    [session_info.resource_name],
                    [session_info.channel_list],
                    [connection.channel_name],
                )


def _generate_standard_waveform(
    session_infos: Sequence[TypedSessionInformation[nifgen.Session]],
) -> None:
    for session_info in session_infos:
        session_info.session.output_mode = nifgen.OutputMode.FUNC
        channels = session_info.session.channels[session_info.channel_list]
        channels.configure_standard_waveform(nifgen.Waveform.SINE, 2.0, 1.0e6)

    with ExitStack() as stack:
        for session_info in session_infos:
            stack.enter_context(session_info.session.initiate())
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/nifgen_measurement/NIFgenMeasurement.serviceconfig sha256=22bb941ffd9ba97fa72b17dad085d9cc6dda972ce8b1196f7f8e6dd5bb9ab7ac bytes=569 -->
## FILE: packages/service/tests/utilities/measurements/nifgen_measurement/NIFgenMeasurement.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/nifgen_measurement/NIFgenMeasurement.serviceconfig`
- sha256: `22bb941ffd9ba97fa72b17dad085d9cc6dda972ce8b1196f7f8e6dd5bb9ab7ac`
- bytes: 569

````json
{
  "services": [
    {
      "displayName": "NI-FGEN Measurement (Py)",
      "serviceClass": "ni.tests.NIFgenMeasurement_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "annotations": {
        "ni/service.description": "NI-FGEN measurement plug-in test service.",
        "ni/service.collection": "NI.Tests",
        "ni/service.tags": []
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/niscope_measurement/__init__.py sha256=79edd3a9dc93bff453dc7dd2af0ee80faf073ba8b9543ab247967bc09cc908ae bytes=4382 -->
## FILE: packages/service/tests/utilities/measurements/niscope_measurement/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/niscope_measurement/__init__.py`
- sha256: `79edd3a9dc93bff453dc7dd2af0ee80faf073ba8b9543ab247967bc09cc908ae`
- bytes: 4382

````python
"""NI-SCOPE measurement plug-in test service."""

from __future__ import annotations

import pathlib
from collections.abc import Iterable, Sequence
from contextlib import ExitStack
from typing import List

import niscope
from ni.measurementlink.sessionmanagement.v1.client import TypedSessionInformation

import ni_measurement_plugin_sdk_service as nims

service_directory = pathlib.Path(__file__).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "NIScopeMeasurement.serviceconfig",
    ui_file_paths=[
        service_directory,
    ],
)


@measurement_service.register_measurement
@measurement_service.configuration("pin_names", nims.DataType.IOResourceArray1D, ["Pin1"])
@measurement_service.configuration("multi_session", nims.DataType.Boolean, False)
@measurement_service.output("session_names", nims.DataType.StringArray1D)
@measurement_service.output("resource_names", nims.DataType.StringArray1D)
@measurement_service.output("channel_lists", nims.DataType.StringArray1D)
@measurement_service.output("connected_channels", nims.DataType.StringArray1D)
@measurement_service.output("waveform", nims.DataType.DoubleArray1D)
def measure(
    pin_names: Iterable[str], multi_session: bool
) -> tuple[Iterable[str], Iterable[str], Iterable[str], Iterable[str], Iterable[float]]:
    """NI-SCOPE measurement plug-in test service."""
    if multi_session:
        with measurement_service.context.reserve_sessions(pin_names) as reservation:
            with reservation.initialize_niscope_sessions() as session_infos:
                assert all([session_info.session is not None for session_info in session_infos])
                connections = reservation.get_niscope_connections(pin_names)
                waveforms = _acquire_waveforms(session_infos)

                return (
                    [session_info.session_name for session_info in session_infos],
                    [session_info.resource_name for session_info in session_infos],
                    [session_info.channel_list for session_info in session_infos],
                    [connection.channel_name for connection in connections],
                    waveforms[0],
                )
    else:
        with measurement_service.context.reserve_session(pin_names) as reservation:
            with reservation.initialize_niscope_session() as session_info:
                assert session_info.session is not None
                connection = reservation.get_niscope_connection(list(pin_names)[0])
                waveforms = _acquire_waveforms([session_info])

                return (
                    [session_info.resource_name],
                    [session_info.resource_name],
                    [session_info.channel_list],
                    [connection.channel_name],
                    waveforms[0],
                )


def _acquire_waveforms(
    session_infos: Sequence[TypedSessionInformation[niscope.Session]],
) -> list[list[float]]:
    for session_info in session_infos:
        channel_order = session_info.channel_list
        trigger_channel = session_info.channel_list.split(",")[0]

        session_info.session.channels[channel_order].configure_vertical(
            5.0, niscope.VerticalCoupling.DC, enabled=True
        )
        session_info.session.channels[channel_order].configure_chan_characteristics(
            1e6, max_input_frequency=0.0
        )
        session_info.session.configure_horizontal_timing(
            10e6,
            5,
            ref_position=50.0,
            num_records=1,
            enforce_realtime=True,
        )
        session_info.session.configure_trigger_edge(
            trigger_channel,
            0.5,
            niscope.TriggerCoupling.DC,
            niscope.TriggerSlope.POSITIVE,
        )
        session_info.session.trigger_modifier = niscope.TriggerModifier.NO_TRIGGER_MOD

    waveforms = []
    with ExitStack() as stack:
        for session_info in session_infos:
            stack.enter_context(session_info.session.initiate())

        for session_info in session_infos:
            waveform_infos = session_info.session.channels[channel_order].fetch()
            for w in waveform_infos:
                waveforms.append(w.samples)

    return waveforms
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/niscope_measurement/NIScopeMeasurement.serviceconfig sha256=7693c378bd63daa59a9faa8a9b1f8133781fa1d02fa7773184c1406333fd90e0 bytes=572 -->
## FILE: packages/service/tests/utilities/measurements/niscope_measurement/NIScopeMeasurement.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/niscope_measurement/NIScopeMeasurement.serviceconfig`
- sha256: `7693c378bd63daa59a9faa8a9b1f8133781fa1d02fa7773184c1406333fd90e0`
- bytes: 572

````json
{
  "services": [
    {
      "displayName": "NI-SCOPE Measurement (Py)",
      "serviceClass": "ni.tests.NIScopeMeasurement_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "annotations": {
        "ni/service.description": "NI-SCOPE measurement plug-in test service.",
        "ni/service.collection": "NI.Tests",
        "ni/service.tags": []
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/niswitch_measurement/__init__.py sha256=9b24b3b268afe11a4006e1d106fd37b1f3e4cbea2448ee7718afca4a90d46fd8 bytes=3104 -->
## FILE: packages/service/tests/utilities/measurements/niswitch_measurement/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/niswitch_measurement/__init__.py`
- sha256: `9b24b3b268afe11a4006e1d106fd37b1f3e4cbea2448ee7718afca4a90d46fd8`
- bytes: 3104

````python
"""NI-SWITCH measurement plug-in test service."""

from __future__ import annotations

import pathlib
from collections.abc import Iterable, Sequence
from typing import Tuple

import niswitch
from ni.measurementlink.sessionmanagement.v1.client import TypedSessionInformation

import ni_measurement_plugin_sdk_service as nims

service_directory = pathlib.Path(__file__).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "NISwitchMeasurement.serviceconfig",
    ui_file_paths=[
        service_directory,
    ],
)


@measurement_service.register_measurement
@measurement_service.configuration("relay_names", nims.DataType.StringArray1D, ["SiteRelay1"])
@measurement_service.configuration("multi_session", nims.DataType.Boolean, False)
@measurement_service.output("session_names", nims.DataType.StringArray1D)
@measurement_service.output("resource_names", nims.DataType.StringArray1D)
@measurement_service.output("channel_lists", nims.DataType.StringArray1D)
@measurement_service.output("connected_channels", nims.DataType.StringArray1D)
def measure(
    relay_names: Iterable[str],
    multi_session: bool,
) -> tuple[Iterable[str], Iterable[str], Iterable[str], Iterable[str]]:
    """NI-SWITCH measurement plug-in test service."""
    if multi_session:
        with measurement_service.context.reserve_sessions(relay_names) as reservation:
            with reservation.initialize_niswitch_sessions() as session_infos:
                connections = reservation.get_niswitch_connections(relay_names)
                assert all([session_info.session is not None for session_info in session_infos])
                _control_relays(session_infos)

                return (
                    [session_info.session_name for session_info in session_infos],
                    [session_info.resource_name for session_info in session_infos],
                    [session_info.channel_list for session_info in session_infos],
                    [connection.channel_name for connection in connections],
                )
    else:
        with measurement_service.context.reserve_session(relay_names) as reservation:
            with reservation.initialize_niswitch_session() as session_info:
                connection = reservation.get_niswitch_connection(list(relay_names)[0])
                assert session_info.session is not None
                _control_relays([session_info])

                return (
                    [session_info.session_name],
                    [session_info.resource_name],
                    [session_info.channel_list],
                    [connection.channel_name],
                )


def _control_relays(
    session_infos: Sequence[TypedSessionInformation[niswitch.Session]],
) -> None:
    for session_info in session_infos:
        session_info.session.relay_control(
            session_info.channel_list, niswitch.enums.RelayAction.CLOSE
        )

    for session_info in session_infos:
        session_info.session.wait_for_debounce()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/niswitch_measurement/NISwitchMeasurement.serviceconfig sha256=e30833e4c084cd9391ab30b66eadd9bf715d565e2a51fc7ca9190de96645c116 bytes=575 -->
## FILE: packages/service/tests/utilities/measurements/niswitch_measurement/NISwitchMeasurement.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/niswitch_measurement/NISwitchMeasurement.serviceconfig`
- sha256: `e30833e4c084cd9391ab30b66eadd9bf715d565e2a51fc7ca9190de96645c116`
- bytes: 575

````json
{
  "services": [
    {
      "displayName": "NI-SWITCH Measurement (Py)",
      "serviceClass": "ni.tests.NISwitchMeasurement_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "annotations": {
        "ni/service.description": "NI-SWITCH measurement plug-in test service.",
        "ni/service.collection": "NI.Tests",
        "ni/service.tags": []
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/niswitch_multiplexer_measurement/__init__.py sha256=784499f5c7afcfdc76256478dbdb0af5377d0da63823f7eb9b1c2b8d96c2efad bytes=3651 -->
## FILE: packages/service/tests/utilities/measurements/niswitch_multiplexer_measurement/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/niswitch_multiplexer_measurement/__init__.py`
- sha256: `784499f5c7afcfdc76256478dbdb0af5377d0da63823f7eb9b1c2b8d96c2efad`
- bytes: 3651

````python
"""NI-SWITCH multiplexer measurement plug-in test service."""

from __future__ import annotations

import pathlib
from collections.abc import Iterable, Sequence
from typing import Tuple

import niswitch
from ni.measurementlink.sessionmanagement.v1.client import (
    TypedConnectionWithMultiplexer,
)

import ni_measurement_plugin_sdk_service as nims

service_directory = pathlib.Path(__file__).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "NISwitchMultiplexerMeasurement.serviceconfig",
    ui_file_paths=[
        service_directory,
    ],
)


@measurement_service.register_measurement
@measurement_service.configuration("pin_names", nims.DataType.IOResourceArray1D, ["Pin1"])
@measurement_service.configuration("multi_session", nims.DataType.Boolean, False)
@measurement_service.output("multiplexer_session_names", nims.DataType.StringArray1D)
@measurement_service.output("multiplexer_resource_names", nims.DataType.StringArray1D)
@measurement_service.output("multiplexer_routes", nims.DataType.StringArray1D)
@measurement_service.output("connected_channels", nims.DataType.StringArray1D)
def measure(
    pin_names: Iterable[str],
    multi_session: bool,
) -> tuple[Iterable[str], Iterable[str], Iterable[str], Iterable[str]]:
    """NI-SWITCH multiplexer measurement plug-in test service."""
    if multi_session:
        with measurement_service.context.reserve_session(pin_names) as reservation:
            with reservation.initialize_niswitch_multiplexer_sessions() as multiplexer_session_infos:
                connections = reservation.get_connections_with_multiplexer(
                    object, niswitch.Session, pin_names
                )
                assert all(
                    [session_info.session is not None for session_info in multiplexer_session_infos]
                )
                _control_relays(connections)

                return (
                    [session_info.session_name for session_info in multiplexer_session_infos],
                    [session_info.resource_name for session_info in multiplexer_session_infos],
                    [connection.multiplexer_route for connection in connections],
                    [connection.channel_name for connection in connections],
                )
    else:
        with measurement_service.context.reserve_session(pin_names) as reservation:
            with reservation.initialize_niswitch_multiplexer_session() as multiplexer_session_info:
                connection = reservation.get_connection_with_multiplexer(
                    object, niswitch.Session, list(pin_names)[0]
                )
                assert multiplexer_session_info.session is not None
                _control_relays([connection])

                return (
                    [multiplexer_session_info.resource_name],
                    [multiplexer_session_info.resource_name],
                    [connection.multiplexer_route],
                    [connection.channel_name],
                )


def _control_relays(
    connections: Sequence[TypedConnectionWithMultiplexer],
) -> None:
    for connection in connections:
        connection.multiplexer_session.connect_multiple(connection.multiplexer_route)

    for connection in connections:
        connection.multiplexer_session.wait_for_debounce()

    for connection in connections:
        connection.multiplexer_session.disconnect_multiple(connection.multiplexer_route)

    for connection in connections:
        connection.multiplexer_session.wait_for_debounce()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/niswitch_multiplexer_measurement/NISwitchMultiplexerMeasurement.serviceconfig sha256=178dacd13b864de6fc8f8bd935186a319cb1dd4ff0b0ee1f00c0ee686dae9dc6 bytes=610 -->
## FILE: packages/service/tests/utilities/measurements/niswitch_multiplexer_measurement/NISwitchMultiplexerMeasurement.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/niswitch_multiplexer_measurement/NISwitchMultiplexerMeasurement.serviceconfig`
- sha256: `178dacd13b864de6fc8f8bd935186a319cb1dd4ff0b0ee1f00c0ee686dae9dc6`
- bytes: 610

````json
{
  "services": [
    {
      "displayName": "NI-SWITCH Multiplexer Measurement (Py)",
      "serviceClass": "ni.tests.NISwitchMultiplexerMeasurement_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "annotations": {
        "ni/service.description": "NI-SWITCH multiplexer measurement plug-in test service.",
        "ni/service.collection": "NI.Tests",
        "ni/service.tags": []
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/pin_aware_measurement/__init__.py sha256=b339fab2c2d6808f567d49e9f5cbdace7729cc415fe710f4f9a156397c486740 bytes=2171 -->
## FILE: packages/service/tests/utilities/measurements/pin_aware_measurement/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/pin_aware_measurement/__init__.py`
- sha256: `b339fab2c2d6808f567d49e9f5cbdace7729cc415fe710f4f9a156397c486740`
- bytes: 2171

````python
"""Pin-aware measurement plug-in test service."""

from __future__ import annotations

import pathlib
from collections.abc import Iterable
from typing import Tuple

import ni_measurement_plugin_sdk_service as nims

service_directory = pathlib.Path(__file__).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "PinAwareMeasurement.serviceconfig",
    ui_file_paths=[
        service_directory,
    ],
)


@measurement_service.register_measurement
@measurement_service.configuration("pin_names", nims.DataType.IOResourceArray1D, ["Pin1"])
@measurement_service.configuration("multi_session", nims.DataType.Boolean, False)
@measurement_service.output("pin_map_id", nims.DataType.String)
@measurement_service.output("sites", nims.DataType.Int32Array1D)
@measurement_service.output("session_names", nims.DataType.StringArray1D)
@measurement_service.output("resource_names", nims.DataType.StringArray1D)
@measurement_service.output("channel_lists", nims.DataType.StringArray1D)
def measure(
    pin_names: Iterable[str],
    multi_session: bool,
) -> tuple[str, Iterable[int], Iterable[str], Iterable[str], Iterable[str]]:
    """Pin-aware measurement plug-in test service."""
    pin_map_context = measurement_service.context.pin_map_context
    if multi_session:
        with measurement_service.context.reserve_sessions(pin_names) as reservation:
            return (
                pin_map_context.pin_map_id,
                pin_map_context.sites or [],
                [s.session_name for s in reservation.session_info],
                [s.resource_name for s in reservation.session_info],
                [s.channel_list for s in reservation.session_info],
            )
    else:
        with measurement_service.context.reserve_session(pin_names) as reservation:
            return (
                pin_map_context.pin_map_id,
                pin_map_context.sites or [],
                [reservation.session_info.resource_name],
                [reservation.session_info.resource_name],
                [reservation.session_info.channel_list],
            )
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/pin_aware_measurement/PinAwareMeasurement.serviceconfig sha256=f5c0d26b8a680a7d0acf57bbd5894b91646cde6e9ef7d40f95d75f4a73de2708 bytes=577 -->
## FILE: packages/service/tests/utilities/measurements/pin_aware_measurement/PinAwareMeasurement.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/pin_aware_measurement/PinAwareMeasurement.serviceconfig`
- sha256: `f5c0d26b8a680a7d0acf57bbd5894b91646cde6e9ef7d40f95d75f4a73de2708`
- bytes: 577

````json
{
  "services": [
    {
      "displayName": "Pin Aware Measurement (Py)",
      "serviceClass": "ni.tests.PinAwareMeasurement_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "annotations": {
        "ni/service.description": "Pin-aware measurement plug-in test service.",
        "ni/service.collection": "NI.Tests",
        "ni/service.tags": []
      }

    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/sample_measurement/_stubs/__init__.py sha256=b51b6d6919cd92fa4a9bf965dd516905e90de8d734eebb55421dd3c578e8c83d bytes=50 -->
## FILE: packages/service/tests/utilities/measurements/sample_measurement/_stubs/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/sample_measurement/_stubs/__init__.py`
- sha256: `b51b6d6919cd92fa4a9bf965dd516905e90de8d734eebb55421dd3c578e8c83d`
- bytes: 50

````python
"""Stubs for sample_measurement's color enum."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/sample_measurement/_stubs/color_pb2.py sha256=5e967013765aae5f600faf3a90e71f0756631c1c90b9d8e4f1a02c1b9fde781b bytes=1266 -->
## FILE: packages/service/tests/utilities/measurements/sample_measurement/_stubs/color_pb2.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/sample_measurement/_stubs/color_pb2.py`
- sha256: `5e967013765aae5f600faf3a90e71f0756631c1c90b9d8e4f1a02c1b9fde781b`
- bytes: 1266

````python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: color.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x63olor.proto\x12\x34ni.measurementlink.measurement.sample_measurement.v1*9\n\rProtobufColor\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04PINK\x10\x01\x12\t\n\x05WHITE\x10\x02\x12\t\n\x05\x42LACK\x10\x03\x42\x37\xaa\x02\x34NationalInstruments.MeasurementServices.Measurementsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'color_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\0024NationalInstruments.MeasurementServices.Measurements'
  _PROTOBUFCOLOR._serialized_start=69
  _PROTOBUFCOLOR._serialized_end=126
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/sample_measurement/_stubs/color_pb2.pyi sha256=ae022e6385440099d15b5249d95117c037e9384bb813ce59bcbdf9c38b3deb02 bytes=1451 -->
## FILE: packages/service/tests/utilities/measurements/sample_measurement/_stubs/color_pb2.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/sample_measurement/_stubs/color_pb2.pyi`
- sha256: `ae022e6385440099d15b5249d95117c037e9384bb813ce59bcbdf9c38b3deb02`
- bytes: 1451

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
---------------------------------------------------------------------
---------------------------------------------------------------------
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ProtobufColor:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ProtobufColorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ProtobufColor.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NONE: _ProtobufColor.ValueType  # 0
    PINK: _ProtobufColor.ValueType  # 1
    WHITE: _ProtobufColor.ValueType  # 2
    BLACK: _ProtobufColor.ValueType  # 3

class ProtobufColor(_ProtobufColor, metaclass=_ProtobufColorEnumTypeWrapper):
    """---------------------------------------------------------------------
    ---------------------------------------------------------------------
    """

NONE: ProtobufColor.ValueType  # 0
PINK: ProtobufColor.ValueType  # 1
WHITE: ProtobufColor.ValueType  # 2
BLACK: ProtobufColor.ValueType  # 3
global___ProtobufColor = ProtobufColor
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/sample_measurement/_stubs/color_pb2_grpc.py sha256=fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb bytes=163 -->
## FILE: packages/service/tests/utilities/measurements/sample_measurement/_stubs/color_pb2_grpc.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/sample_measurement/_stubs/color_pb2_grpc.py`
- sha256: `fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb`
- bytes: 163

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/sample_measurement/_stubs/color_pb2_grpc.pyi sha256=39f27912762651cdfd22fbf10b6fab35499643cf2bb1f9c5e250ec103697973f bytes=222 -->
## FILE: packages/service/tests/utilities/measurements/sample_measurement/_stubs/color_pb2_grpc.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/sample_measurement/_stubs/color_pb2_grpc.pyi`
- sha256: `39f27912762651cdfd22fbf10b6fab35499643cf2bb1f9c5e250ec103697973f`
- bytes: 222

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
---------------------------------------------------------------------
---------------------------------------------------------------------
"""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/streaming_data_measurement/__init__.py sha256=c84b9823c2692dd70d64fb3714ef536f6ffee9fa2d38b52b88dad849ae0a1d88 bytes=2624 -->
## FILE: packages/service/tests/utilities/measurements/streaming_data_measurement/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/streaming_data_measurement/__init__.py`
- sha256: `c84b9823c2692dd70d64fb3714ef536f6ffee9fa2d38b52b88dad849ae0a1d88`
- bytes: 2624

````python
"""Contains utility functions to test a v2 measurement service that streams data."""

from __future__ import annotations

import pathlib
import threading
import time
from collections.abc import Generator
from typing import List, Tuple

import grpc

import ni_measurement_plugin_sdk_service as nims

service_directory = pathlib.Path(__file__).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "StreamingDataMeasurement.serviceconfig",
    ui_file_paths=[
        service_directory,
    ],
)


Outputs = tuple[str, int, list[int]]


@measurement_service.register_measurement
@measurement_service.configuration("name", nims.DataType.String, "<Name>")
@measurement_service.configuration("num_responses", nims.DataType.Int32, 10)
@measurement_service.configuration("data_size", nims.DataType.Int32, 1)
@measurement_service.configuration("cumulative_data", nims.DataType.Boolean, True)
@measurement_service.configuration("response_interval_in_ms", nims.DataType.Int32, 1000)
@measurement_service.configuration("error_on_index", nims.DataType.Int32, -1)
@measurement_service.output("name", nims.DataType.String)
@measurement_service.output("index", nims.DataType.Int32)
@measurement_service.output("data", nims.DataType.Int32Array1D)
def measure(
    name: str,
    num_responses: int,
    data_size: int,
    cumulative_data: bool,
    response_interval_in_ms: int,
    error_on_index: int,
) -> Generator[Outputs]:
    """Returns the number of responses requested at the requested interval."""
    cancellation_event = threading.Event()
    measurement_service.context.add_cancel_callback(cancellation_event.set)

    data: list[int] = []

    response_interval_in_seconds = response_interval_in_ms / 1000.0

    for index in range(0, num_responses):
        update_time = time.monotonic()

        if index == error_on_index:
            measurement_service.context.abort(
                grpc.StatusCode.UNKNOWN,
                f"Errored at index {error_on_index}",
            )

        if not cumulative_data:
            data.clear()

        data.extend(index for i in range(data_size))

        yield (name, index, data)

        # Delay for the remaining portion of the requested interval and check for cancellation.
        delay = max(0.0, response_interval_in_seconds - (time.monotonic() - update_time))
        if cancellation_event.wait(delay):
            measurement_service.context.abort(
                grpc.StatusCode.CANCELLED, "Client requested cancellation."
            )
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/streaming_data_measurement/StreamingDataMeasurement.serviceconfig sha256=e0154ff12a670a4cf90a4eab5635e331dc4830566c58fdc40349973341e77bcc bytes=554 -->
## FILE: packages/service/tests/utilities/measurements/streaming_data_measurement/StreamingDataMeasurement.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/streaming_data_measurement/StreamingDataMeasurement.serviceconfig`
- sha256: `e0154ff12a670a4cf90a4eab5635e331dc4830566c58fdc40349973341e77bcc`
- bytes: 554

````json
{
  "services": [
    {
      "displayName": "Streaming Data Measurement (Py)",
      "serviceClass": "ni.tests.StreamingDataMeasurement_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "annotations": {
        "ni/service.description": "Measurement plug-in test service that generates a predictable stream of data.",
        "ni/service.collection": "NI.Tests",
        "ni/service.tags": []
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/unknown_interface_measurement/__init__.py sha256=33937206b5a0327691f545a2a4e509eb3da682feff9d6b863c80c0cf5066f50a bytes=806 -->
## FILE: packages/service/tests/utilities/measurements/unknown_interface_measurement/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/unknown_interface_measurement/__init__.py`
- sha256: `33937206b5a0327691f545a2a4e509eb3da682feff9d6b863c80c0cf5066f50a`
- bytes: 806

````python
"""Contains utility functions to test loopback measurement service."""

from __future__ import annotations

import pathlib
from typing import Tuple

import ni_measurement_plugin_sdk_service as nims

service_directory = pathlib.Path(__file__).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "unknown_interface.serviceconfig",
    ui_file_paths=[
        service_directory,
    ],
)


@measurement_service.register_measurement
@measurement_service.configuration("Float In", nims.DataType.Float, 0.06)
@measurement_service.output("Float out", nims.DataType.Float)
def measure(float_input: float) -> tuple[float]:
    """Loopback measurement on the float input."""
    float_output = float_input

    return (float_output,)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/unknown_interface_measurement/unknown_interface.serviceconfig sha256=0d51abe80c74ac389a8491ed2ce680b49f698b5405de850d8df6babcdabd6b46 bytes=527 -->
## FILE: packages/service/tests/utilities/measurements/unknown_interface_measurement/unknown_interface.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/unknown_interface_measurement/unknown_interface.serviceconfig`
- sha256: `0d51abe80c74ac389a8491ed2ce680b49f698b5405de850d8df6babcdabd6b46`
- bytes: 527

````json
{
  "services": [
    {
      "displayName": "Unknown Interface Measurement (Py)",
      "serviceClass": "ni.tests.UnknownInterface_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "acme.unknown.measurement.interface.V1"
      ],
      "path": "start.bat",
      "annotations": {
        "ni/service.description": "Measurement plug-in test service that provides an unknown interface.",
        "ni/service.collection": "NI.Tests",
        "ni/service.tags": []
      }

    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/v1_only_measurement/__init__.py sha256=c2e5d3d631f93f0e7c5c27744cb43d6225bcadd2499d043576266dac36b8bb84 bytes=796 -->
## FILE: packages/service/tests/utilities/measurements/v1_only_measurement/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/v1_only_measurement/__init__.py`
- sha256: `c2e5d3d631f93f0e7c5c27744cb43d6225bcadd2499d043576266dac36b8bb84`
- bytes: 796

````python
"""Contains utility functions to test loopback measurement service."""

from __future__ import annotations

import pathlib
from typing import Tuple

import ni_measurement_plugin_sdk_service as nims

service_directory = pathlib.Path(__file__).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "v1_only.serviceconfig",
    ui_file_paths=[
        service_directory,
    ],
)


@measurement_service.register_measurement
@measurement_service.configuration("Float In", nims.DataType.Float, 0.06)
@measurement_service.output("Float out", nims.DataType.Float)
def measure(float_input: float) -> tuple[float]:
    """Loopback measurement on the float input."""
    float_output = float_input

    return (float_output,)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/v1_only_measurement/v1_only.serviceconfig sha256=1229a1916de33ef53bef50fbe3a4cd9730627795543f67506a9b581efc1fbac1 bytes=525 -->
## FILE: packages/service/tests/utilities/measurements/v1_only_measurement/v1_only.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/v1_only_measurement/v1_only.serviceconfig`
- sha256: `1229a1916de33ef53bef50fbe3a4cd9730627795543f67506a9b581efc1fbac1`
- bytes: 525

````json
{
  "services": [
    {
      "displayName": "V1 Measurement (Py)",
      "serviceClass": "ni.tests.V1Measurement_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService"
      ],
      "path": "start.bat",
      "annotations": {
        "ni/service.description": "Measurement plug-in test service that only supports a v1 measurement.",
        "ni/service.collection": "NI.Tests",
        "ni/service.tags": []
      }

    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/v2_only_measurement/__init__.py sha256=81bbf6a7a41523f6e9087d70c8e0892d8aca25b60ffdcfb9a65bf674c30d728c bytes=796 -->
## FILE: packages/service/tests/utilities/measurements/v2_only_measurement/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/v2_only_measurement/__init__.py`
- sha256: `81bbf6a7a41523f6e9087d70c8e0892d8aca25b60ffdcfb9a65bf674c30d728c`
- bytes: 796

````python
"""Contains utility functions to test loopback measurement service."""

from __future__ import annotations

import pathlib
from typing import Tuple

import ni_measurement_plugin_sdk_service as nims

service_directory = pathlib.Path(__file__).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "v2_only.serviceconfig",
    ui_file_paths=[
        service_directory,
    ],
)


@measurement_service.register_measurement
@measurement_service.configuration("Float In", nims.DataType.Float, 0.06)
@measurement_service.output("Float out", nims.DataType.Float)
def measure(float_input: float) -> tuple[float]:
    """Loopback measurement on the float input."""
    float_output = float_input

    return (float_output,)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/v2_only_measurement/v2_only.serviceconfig sha256=bc6150f6c64f4101419c7bffeae028c2cb25bce3ed0577cac2f043a3564d85ef bytes=525 -->
## FILE: packages/service/tests/utilities/measurements/v2_only_measurement/v2_only.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/v2_only_measurement/v2_only.serviceconfig`
- sha256: `bc6150f6c64f4101419c7bffeae028c2cb25bce3ed0577cac2f043a3564d85ef`
- bytes: 525

````json
{
  "services": [
    {
      "displayName": "V2 Measurement (Py)",
      "serviceClass": "ni.tests.V2Measurement_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "annotations": {
        "ni/service.description": "Measurement plug-in test service that only supports a v2 measurement.",
        "ni/service.collection": "NI.Tests",
        "ni/service.tags": []
      }

    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/yield_vs_return_measurement/__init__.py sha256=f3e8d6a19b5fd56a857260329853596e295843f0bf4d1f04ed97a83186cd7f28 bytes=3273 -->
## FILE: packages/service/tests/utilities/measurements/yield_vs_return_measurement/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/yield_vs_return_measurement/__init__.py`
- sha256: `f3e8d6a19b5fd56a857260329853596e295843f0bf4d1f04ed97a83186cd7f28`
- bytes: 3273

````python
"""Contains utility functions to test that yield and return are supported in measurements."""

from __future__ import annotations

import pathlib
import random
import threading
import time
from collections.abc import Generator
from typing import List

import grpc

import ni_measurement_plugin_sdk_service as nims

RANDOM_NUMBERS_PER_SECOND = 100.0
RANDOM_NUMBER_RANGE = 10.0
UI_UPDATE_INTERVAL_IN_SECONDS = 100e-3

service_directory = pathlib.Path(__file__).resolve().parent
measurement_service = nims.MeasurementService(
    service_config_path=service_directory / "UIProgressUpdates.serviceconfig",
    ui_file_paths=[
        service_directory,
    ],
)


Outputs = tuple[float, list[float], str]


@measurement_service.register_measurement
@measurement_service.configuration("time_in_seconds", nims.DataType.Double, 10.0)
@measurement_service.output("elapsed_time_in_seconds", nims.DataType.Double)
@measurement_service.output("random_numbers", nims.DataType.DoubleArray1D)
@measurement_service.output("status", nims.DataType.String)
def measure(time_in_seconds: float) -> Generator[Outputs, None, Outputs]:
    """Generates random numbers and updates the measurement UI to show progress."""
    cancellation_event = threading.Event()
    measurement_service.context.add_cancel_callback(cancellation_event.set)

    if time_in_seconds < 0.0:
        measurement_service.context.abort(
            grpc.StatusCode.INVALID_ARGUMENT, "time_in_seconds must be non-negative."
        )

    elapsed_time_in_seconds = 0.0
    random_numbers: list[float] = []
    status = ""

    start_time = time.monotonic()
    stop_len = int(time_in_seconds * RANDOM_NUMBERS_PER_SECOND)
    update_number = 1
    while len(random_numbers) < stop_len:
        update_time = time.monotonic()
        elapsed_time_in_seconds = update_time - start_time

        status = f"Update: {update_number}"
        update_number += 1

        desired_len = int(elapsed_time_in_seconds * RANDOM_NUMBERS_PER_SECOND)
        desired_len = max(0, min(desired_len, stop_len))
        random_numbers.extend(_generate_random_numbers(desired_len - len(random_numbers)))

        # Use yield to send incremental updates to an interactive client such as
        # InstrumentStudio.
        yield (elapsed_time_in_seconds, random_numbers, status)

        # Delay for the remaining portion of the UI update interval and check for cancellation.
        delay = max(0.0, UI_UPDATE_INTERVAL_IN_SECONDS - (time.monotonic() - update_time))
        if cancellation_event.wait(delay):
            measurement_service.context.abort(
                grpc.StatusCode.CANCELLED, "Client requested cancellation."
            )

    # Non-interactive clients such as TestStand only use the measurement's final
    # update. You may use either yield or return to send the final update.
    status = f"Total updates: {update_number}"
    return (elapsed_time_in_seconds, random_numbers, status)


def _generate_random_numbers(count: int) -> Generator[float]:
    """Generate random numbers between -RANDOM_NUMBER_RANGE and +RANDOM_NUMBER_RANGE."""
    for _ in range(count):
        yield RANDOM_NUMBER_RANGE * (2.0 * random.random() - 1.0)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/yield_vs_return_measurement/UIProgressUpdates.serviceconfig sha256=58a6e2e1cc453cc0174decf8aecc63c7f3d97d7829c4517f8001bd6b9a915f37 bytes=639 -->
## FILE: packages/service/tests/utilities/measurements/yield_vs_return_measurement/UIProgressUpdates.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/measurements/yield_vs_return_measurement/UIProgressUpdates.serviceconfig`
- sha256: `58a6e2e1cc453cc0174decf8aecc63c7f3d97d7829c4517f8001bd6b9a915f37`
- bytes: 639

````json
{
  "services": [
    {
      "displayName": "UI Progress Updates (Py)",
      "serviceClass": "ni.tests.UIProgressUpdates_Python",
      "descriptionUrl": "",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "annotations": {
        "ni/service.description": "Measurement plug-in test service that generates random numbers and updates the measurement UI to show progress.",
        "ni/service.collection": "NI.Tests",
        "ni/service.tags": []
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/__init__.py sha256=6b8633e3b4868086a9b007d445d75572ddfc0bedfb22cfb4b3b5300fe6aba250 bytes=34 -->
## FILE: packages/service/tests/utilities/stubs/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/__init__.py`
- sha256: `6b8633e3b4868086a9b007d445d75572ddfc0bedfb22cfb4b3b5300fe6aba250`
- bytes: 34

````python
"""Auto generated gRPC files."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/loopback/__init__.py sha256=e82aa7d0562edb25fdb852946848936a77c99ddd9ad62e03f8a2c8f3db6ffc84 bytes=59 -->
## FILE: packages/service/tests/utilities/stubs/loopback/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/loopback/__init__.py`
- sha256: `e82aa7d0562edb25fdb852946848936a77c99ddd9ad62e03f8a2c8f3db6ffc84`
- bytes: 59

````python
"""Auto generated gRPC files for loopback measurement."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/loopback/types.proto sha256=52e40d4388ff621bdd98736c6f4cabea9ac1cf72216977c7c4f6b71ed7bf942b bytes=500 -->
## FILE: packages/service/tests/utilities/stubs/loopback/types.proto

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/loopback/types.proto`
- sha256: `52e40d4388ff621bdd98736c6f4cabea9ac1cf72216977c7c4f6b71ed7bf942b`
- bytes: 500

````protobuf
syntax = "proto3";
package ni.measurementlink.measurement.tests.loopback;

enum Color {
    NONE = 0;
    RED = 1;
    GREEN = 2;
    BLUE = 3;
}

enum ProtobufColor {
    COLORLESS = 0;
    PINK = 1;
    WHITE = 2;
    BLACK = 3;
}

message Parameters {
    float float_in = 1;
    repeated double double_array_in = 2;
    bool bool_in = 3;
    string string_in = 4;
    Color enum_in = 5;
    ProtobufColor protobuf_enum_in = 6;
    repeated string string_array_in = 7;
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/loopback/types_pb2.py sha256=426aaf73f0ddef10476dcdc51b4a5e0f5263b847840326b8064701341e9f676e bytes=1819 -->
## FILE: packages/service/tests/utilities/stubs/loopback/types_pb2.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/loopback/types_pb2.py`
- sha256: `426aaf73f0ddef10476dcdc51b4a5e0f5263b847840326b8064701341e9f676e`
- bytes: 1819

````python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: loopback/types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14loopback/types.proto\x12-ni.measurementlink.measurement.tests.loopback\"\x93\x02\n\nParameters\x12\x10\n\x08\x66loat_in\x18\x01 \x01(\x02\x12\x17\n\x0f\x64ouble_array_in\x18\x02 \x03(\x01\x12\x0f\n\x07\x62ool_in\x18\x03 \x01(\x08\x12\x11\n\tstring_in\x18\x04 \x01(\t\x12\x45\n\x07\x65num_in\x18\x05 \x01(\x0e\x32\x34.ni.measurementlink.measurement.tests.loopback.Color\x12V\n\x10protobuf_enum_in\x18\x06 \x01(\x0e\x32<.ni.measurementlink.measurement.tests.loopback.ProtobufColor\x12\x17\n\x0fstring_array_in\x18\x07 \x03(\t*/\n\x05\x43olor\x12\x08\n\x04NONE\x10\x00\x12\x07\n\x03RED\x10\x01\x12\t\n\x05GREEN\x10\x02\x12\x08\n\x04\x42LUE\x10\x03*>\n\rProtobufColor\x12\r\n\tCOLORLESS\x10\x00\x12\x08\n\x04PINK\x10\x01\x12\t\n\x05WHITE\x10\x02\x12\t\n\x05\x42LACK\x10\x03\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'loopback.types_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COLOR._serialized_start=349
  _COLOR._serialized_end=396
  _PROTOBUFCOLOR._serialized_start=398
  _PROTOBUFCOLOR._serialized_end=460
  _PARAMETERS._serialized_start=72
  _PARAMETERS._serialized_end=347
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/loopback/types_pb2.pyi sha256=02c00abac00020ff0cfa2f0511cac0099e6f5649f6aee5cebddde5c0685b9a80 bytes=3570 -->
## FILE: packages/service/tests/utilities/stubs/loopback/types_pb2.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/loopback/types_pb2.pyi`
- sha256: `02c00abac00020ff0cfa2f0511cac0099e6f5649f6aee5cebddde5c0685b9a80`
- bytes: 3570

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Color:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ColorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Color.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NONE: _Color.ValueType  # 0
    RED: _Color.ValueType  # 1
    GREEN: _Color.ValueType  # 2
    BLUE: _Color.ValueType  # 3

class Color(_Color, metaclass=_ColorEnumTypeWrapper): ...

NONE: Color.ValueType  # 0
RED: Color.ValueType  # 1
GREEN: Color.ValueType  # 2
BLUE: Color.ValueType  # 3
global___Color = Color

class _ProtobufColor:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ProtobufColorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ProtobufColor.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    COLORLESS: _ProtobufColor.ValueType  # 0
    PINK: _ProtobufColor.ValueType  # 1
    WHITE: _ProtobufColor.ValueType  # 2
    BLACK: _ProtobufColor.ValueType  # 3

class ProtobufColor(_ProtobufColor, metaclass=_ProtobufColorEnumTypeWrapper): ...

COLORLESS: ProtobufColor.ValueType  # 0
PINK: ProtobufColor.ValueType  # 1
WHITE: ProtobufColor.ValueType  # 2
BLACK: ProtobufColor.ValueType  # 3
global___ProtobufColor = ProtobufColor

@typing.final
class Parameters(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FLOAT_IN_FIELD_NUMBER: builtins.int
    DOUBLE_ARRAY_IN_FIELD_NUMBER: builtins.int
    BOOL_IN_FIELD_NUMBER: builtins.int
    STRING_IN_FIELD_NUMBER: builtins.int
    ENUM_IN_FIELD_NUMBER: builtins.int
    PROTOBUF_ENUM_IN_FIELD_NUMBER: builtins.int
    STRING_ARRAY_IN_FIELD_NUMBER: builtins.int
    float_in: builtins.float
    bool_in: builtins.bool
    string_in: builtins.str
    enum_in: global___Color.ValueType
    protobuf_enum_in: global___ProtobufColor.ValueType
    @property
    def double_array_in(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    @property
    def string_array_in(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        float_in: builtins.float = ...,
        double_array_in: collections.abc.Iterable[builtins.float] | None = ...,
        bool_in: builtins.bool = ...,
        string_in: builtins.str = ...,
        enum_in: global___Color.ValueType = ...,
        protobuf_enum_in: global___ProtobufColor.ValueType = ...,
        string_array_in: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["bool_in", b"bool_in", "double_array_in", b"double_array_in", "enum_in", b"enum_in", "float_in", b"float_in", "protobuf_enum_in", b"protobuf_enum_in", "string_array_in", b"string_array_in", "string_in", b"string_in"]) -> None: ...

global___Parameters = Parameters
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/loopback/types_pb2_grpc.py sha256=fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb bytes=163 -->
## FILE: packages/service/tests/utilities/stubs/loopback/types_pb2_grpc.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/loopback/types_pb2_grpc.py`
- sha256: `fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb`
- bytes: 163

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/loopback/types_pb2_grpc.pyi sha256=f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed bytes=430 -->
## FILE: packages/service/tests/utilities/stubs/loopback/types_pb2_grpc.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/loopback/types_pb2_grpc.pyi`
- sha256: `f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed`
- bytes: 430

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidaqmx/__init__.py sha256=3b0078104854e833d2fd67d911eab324a3110572bda7d2822323898f51589218 bytes=63 -->
## FILE: packages/service/tests/utilities/stubs/nidaqmx/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nidaqmx/__init__.py`
- sha256: `3b0078104854e833d2fd67d911eab324a3110572bda7d2822323898f51589218`
- bytes: 63

````python
"""Auto generated gRPC files for nidaqmx test measurement."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidaqmx/types.proto sha256=b281f7a4022365cc7266d367accf244d4d47c3dbd5e62b97d9d835a085166278 bytes=400 -->
## FILE: packages/service/tests/utilities/stubs/nidaqmx/types.proto

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nidaqmx/types.proto`
- sha256: `b281f7a4022365cc7266d367accf244d4d47c3dbd5e62b97d9d835a085166278`
- bytes: 400

````protobuf
syntax = "proto3";
package ni.measurementlink.measurement.tests.nidaqmx;

message Configurations {
    repeated string pin_names = 1;
    bool multi_session = 2;
}

message Outputs {
    repeated string session_names = 1;
    repeated string resource_names = 2;
    repeated string channel_lists = 3;
    repeated string connected_channels = 4;
    repeated double voltage_values = 5;
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidaqmx/types_pb2.py sha256=a54bc48cc29454a7c52715c117e21b9ef94c70d5c9d8ee11e561b6af2e303074 bytes=1402 -->
## FILE: packages/service/tests/utilities/stubs/nidaqmx/types_pb2.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nidaqmx/types_pb2.py`
- sha256: `a54bc48cc29454a7c52715c117e21b9ef94c70d5c9d8ee11e561b6af2e303074`
- bytes: 1402

````python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nidaqmx/types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13nidaqmx/types.proto\x12,ni.measurementlink.measurement.tests.nidaqmx\":\n\x0e\x43onfigurations\x12\x11\n\tpin_names\x18\x01 \x03(\t\x12\x15\n\rmulti_session\x18\x02 \x01(\x08\"\x83\x01\n\x07Outputs\x12\x15\n\rsession_names\x18\x01 \x03(\t\x12\x16\n\x0eresource_names\x18\x02 \x03(\t\x12\x15\n\rchannel_lists\x18\x03 \x03(\t\x12\x1a\n\x12\x63onnected_channels\x18\x04 \x03(\t\x12\x16\n\x0evoltage_values\x18\x05 \x03(\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nidaqmx.types_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONFIGURATIONS._serialized_start=69
  _CONFIGURATIONS._serialized_end=127
  _OUTPUTS._serialized_start=130
  _OUTPUTS._serialized_end=261
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidaqmx/types_pb2.pyi sha256=5d30f90d0131682f35810881f609a1948f78bbd1317316fc7b24ecf09a6d10af bytes=2812 -->
## FILE: packages/service/tests/utilities/stubs/nidaqmx/types_pb2.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nidaqmx/types_pb2.pyi`
- sha256: `5d30f90d0131682f35810881f609a1948f78bbd1317316fc7b24ecf09a6d10af`
- bytes: 2812

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Configurations(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PIN_NAMES_FIELD_NUMBER: builtins.int
    MULTI_SESSION_FIELD_NUMBER: builtins.int
    multi_session: builtins.bool
    @property
    def pin_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        pin_names: collections.abc.Iterable[builtins.str] | None = ...,
        multi_session: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["multi_session", b"multi_session", "pin_names", b"pin_names"]) -> None: ...

global___Configurations = Configurations

@typing.final
class Outputs(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SESSION_NAMES_FIELD_NUMBER: builtins.int
    RESOURCE_NAMES_FIELD_NUMBER: builtins.int
    CHANNEL_LISTS_FIELD_NUMBER: builtins.int
    CONNECTED_CHANNELS_FIELD_NUMBER: builtins.int
    VOLTAGE_VALUES_FIELD_NUMBER: builtins.int
    @property
    def session_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def resource_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def channel_lists(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def connected_channels(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def voltage_values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    def __init__(
        self,
        *,
        session_names: collections.abc.Iterable[builtins.str] | None = ...,
        resource_names: collections.abc.Iterable[builtins.str] | None = ...,
        channel_lists: collections.abc.Iterable[builtins.str] | None = ...,
        connected_channels: collections.abc.Iterable[builtins.str] | None = ...,
        voltage_values: collections.abc.Iterable[builtins.float] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["channel_lists", b"channel_lists", "connected_channels", b"connected_channels", "resource_names", b"resource_names", "session_names", b"session_names", "voltage_values", b"voltage_values"]) -> None: ...

global___Outputs = Outputs
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidaqmx/types_pb2_grpc.py sha256=fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb bytes=163 -->
## FILE: packages/service/tests/utilities/stubs/nidaqmx/types_pb2_grpc.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nidaqmx/types_pb2_grpc.py`
- sha256: `fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb`
- bytes: 163

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidaqmx/types_pb2_grpc.pyi sha256=f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed bytes=430 -->
## FILE: packages/service/tests/utilities/stubs/nidaqmx/types_pb2_grpc.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nidaqmx/types_pb2_grpc.pyi`
- sha256: `f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed`
- bytes: 430

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidcpower/__init__.py sha256=72696d7a78c486851792b5b2a3c68fa9f14fee396540bf0c7a10adbf95f52602 bytes=65 -->
## FILE: packages/service/tests/utilities/stubs/nidcpower/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nidcpower/__init__.py`
- sha256: `72696d7a78c486851792b5b2a3c68fa9f14fee396540bf0c7a10adbf95f52602`
- bytes: 65

````python
"""Auto generated gRPC files for nidcpower test measurement."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidcpower/types.proto sha256=d4f4b305e5c815b901f811a7b73972b3e514129e684b5cbfc1acf612de15d385 bytes=457 -->
## FILE: packages/service/tests/utilities/stubs/nidcpower/types.proto

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nidcpower/types.proto`
- sha256: `d4f4b305e5c815b901f811a7b73972b3e514129e684b5cbfc1acf612de15d385`
- bytes: 457

````protobuf
syntax = "proto3";
package ni.measurementlink.measurement.tests.nidcpower;

message Configurations {
    repeated string pin_names = 1;
    bool multi_session = 2;
}

message Outputs {
    repeated string session_names = 1;
    repeated string resource_names = 2;
    repeated string channel_lists = 3;
    repeated string connected_channels = 4;
    repeated double voltage_measurements = 5;
    repeated double current_measurements = 6;
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidcpower/types_pb2.py sha256=a27745f4371585e19595c13d67bec443f38037a89ae2c33772e874e43fe51a9d bytes=1471 -->
## FILE: packages/service/tests/utilities/stubs/nidcpower/types_pb2.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nidcpower/types_pb2.py`
- sha256: `a27745f4371585e19595c13d67bec443f38037a89ae2c33772e874e43fe51a9d`
- bytes: 1471

````python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nidcpower/types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15nidcpower/types.proto\x12.ni.measurementlink.measurement.tests.nidcpower\":\n\x0e\x43onfigurations\x12\x11\n\tpin_names\x18\x01 \x03(\t\x12\x15\n\rmulti_session\x18\x02 \x01(\x08\"\xa7\x01\n\x07Outputs\x12\x15\n\rsession_names\x18\x01 \x03(\t\x12\x16\n\x0eresource_names\x18\x02 \x03(\t\x12\x15\n\rchannel_lists\x18\x03 \x03(\t\x12\x1a\n\x12\x63onnected_channels\x18\x04 \x03(\t\x12\x1c\n\x14voltage_measurements\x18\x05 \x03(\x01\x12\x1c\n\x14\x63urrent_measurements\x18\x06 \x03(\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nidcpower.types_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONFIGURATIONS._serialized_start=73
  _CONFIGURATIONS._serialized_end=131
  _OUTPUTS._serialized_start=134
  _OUTPUTS._serialized_end=301
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidcpower/types_pb2.pyi sha256=e6cfe03413fbcb0d7736cd080e6b295c89b71199334b189eed053f276a6a2838 bytes=3170 -->
## FILE: packages/service/tests/utilities/stubs/nidcpower/types_pb2.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nidcpower/types_pb2.pyi`
- sha256: `e6cfe03413fbcb0d7736cd080e6b295c89b71199334b189eed053f276a6a2838`
- bytes: 3170

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Configurations(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PIN_NAMES_FIELD_NUMBER: builtins.int
    MULTI_SESSION_FIELD_NUMBER: builtins.int
    multi_session: builtins.bool
    @property
    def pin_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        pin_names: collections.abc.Iterable[builtins.str] | None = ...,
        multi_session: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["multi_session", b"multi_session", "pin_names", b"pin_names"]) -> None: ...

global___Configurations = Configurations

@typing.final
class Outputs(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SESSION_NAMES_FIELD_NUMBER: builtins.int
    RESOURCE_NAMES_FIELD_NUMBER: builtins.int
    CHANNEL_LISTS_FIELD_NUMBER: builtins.int
    CONNECTED_CHANNELS_FIELD_NUMBER: builtins.int
    VOLTAGE_MEASUREMENTS_FIELD_NUMBER: builtins.int
    CURRENT_MEASUREMENTS_FIELD_NUMBER: builtins.int
    @property
    def session_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def resource_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def channel_lists(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def connected_channels(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def voltage_measurements(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    @property
    def current_measurements(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    def __init__(
        self,
        *,
        session_names: collections.abc.Iterable[builtins.str] | None = ...,
        resource_names: collections.abc.Iterable[builtins.str] | None = ...,
        channel_lists: collections.abc.Iterable[builtins.str] | None = ...,
        connected_channels: collections.abc.Iterable[builtins.str] | None = ...,
        voltage_measurements: collections.abc.Iterable[builtins.float] | None = ...,
        current_measurements: collections.abc.Iterable[builtins.float] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["channel_lists", b"channel_lists", "connected_channels", b"connected_channels", "current_measurements", b"current_measurements", "resource_names", b"resource_names", "session_names", b"session_names", "voltage_measurements", b"voltage_measurements"]) -> None: ...

global___Outputs = Outputs
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidcpower/types_pb2_grpc.py sha256=fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb bytes=163 -->
## FILE: packages/service/tests/utilities/stubs/nidcpower/types_pb2_grpc.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nidcpower/types_pb2_grpc.py`
- sha256: `fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb`
- bytes: 163

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidcpower/types_pb2_grpc.pyi sha256=f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed bytes=430 -->
## FILE: packages/service/tests/utilities/stubs/nidcpower/types_pb2_grpc.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nidcpower/types_pb2_grpc.pyi`
- sha256: `f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed`
- bytes: 430

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidigital/__init__.py sha256=102f03d10b7ff79ea15e5a30ba58d64611c0a5a348366d38f1633e8bc7c278e6 bytes=65 -->
## FILE: packages/service/tests/utilities/stubs/nidigital/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nidigital/__init__.py`
- sha256: `102f03d10b7ff79ea15e5a30ba58d64611c0a5a348366d38f1633e8bc7c278e6`
- bytes: 65

````python
"""Auto generated gRPC files for nidigital test measurement."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidigital/types.proto sha256=65ef9629be89e42dd5e84bfa3d41b9956e2965b83676e242c963e0633b973a44 bytes=439 -->
## FILE: packages/service/tests/utilities/stubs/nidigital/types.proto

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nidigital/types.proto`
- sha256: `65ef9629be89e42dd5e84bfa3d41b9956e2965b83676e242c963e0633b973a44`
- bytes: 439

````protobuf
syntax = "proto3";
package ni.measurementlink.measurement.tests.nidigital;

message Configurations {
    repeated string pin_names = 1;
    bool multi_session = 2;
}

message Outputs {
    repeated string session_names = 1;
    repeated string resource_names = 2;
    repeated string channel_lists = 3;
    repeated string connected_channels = 4;
    repeated int32 passing_sites = 5;
    repeated int32 failing_sites = 6;
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidigital/types_pb2.py sha256=55a3e86af1be5765f5c3e0c9fc084245d7a83901caf73156789a25556ed0422e bytes=1450 -->
## FILE: packages/service/tests/utilities/stubs/nidigital/types_pb2.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nidigital/types_pb2.py`
- sha256: `55a3e86af1be5765f5c3e0c9fc084245d7a83901caf73156789a25556ed0422e`
- bytes: 1450

````python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nidigital/types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15nidigital/types.proto\x12.ni.measurementlink.measurement.tests.nidigital\":\n\x0e\x43onfigurations\x12\x11\n\tpin_names\x18\x01 \x03(\t\x12\x15\n\rmulti_session\x18\x02 \x01(\x08\"\x99\x01\n\x07Outputs\x12\x15\n\rsession_names\x18\x01 \x03(\t\x12\x16\n\x0eresource_names\x18\x02 \x03(\t\x12\x15\n\rchannel_lists\x18\x03 \x03(\t\x12\x1a\n\x12\x63onnected_channels\x18\x04 \x03(\t\x12\x15\n\rpassing_sites\x18\x05 \x03(\x05\x12\x15\n\rfailing_sites\x18\x06 \x03(\x05\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nidigital.types_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONFIGURATIONS._serialized_start=73
  _CONFIGURATIONS._serialized_end=131
  _OUTPUTS._serialized_start=134
  _OUTPUTS._serialized_end=287
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidigital/types_pb2.pyi sha256=3455c0a55b82b9a0af6907e900d37471066164b476f45c35b54eeb70cc9a5645 bytes=3092 -->
## FILE: packages/service/tests/utilities/stubs/nidigital/types_pb2.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nidigital/types_pb2.pyi`
- sha256: `3455c0a55b82b9a0af6907e900d37471066164b476f45c35b54eeb70cc9a5645`
- bytes: 3092

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Configurations(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PIN_NAMES_FIELD_NUMBER: builtins.int
    MULTI_SESSION_FIELD_NUMBER: builtins.int
    multi_session: builtins.bool
    @property
    def pin_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        pin_names: collections.abc.Iterable[builtins.str] | None = ...,
        multi_session: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["multi_session", b"multi_session", "pin_names", b"pin_names"]) -> None: ...

global___Configurations = Configurations

@typing.final
class Outputs(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SESSION_NAMES_FIELD_NUMBER: builtins.int
    RESOURCE_NAMES_FIELD_NUMBER: builtins.int
    CHANNEL_LISTS_FIELD_NUMBER: builtins.int
    CONNECTED_CHANNELS_FIELD_NUMBER: builtins.int
    PASSING_SITES_FIELD_NUMBER: builtins.int
    FAILING_SITES_FIELD_NUMBER: builtins.int
    @property
    def session_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def resource_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def channel_lists(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def connected_channels(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def passing_sites(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def failing_sites(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        session_names: collections.abc.Iterable[builtins.str] | None = ...,
        resource_names: collections.abc.Iterable[builtins.str] | None = ...,
        channel_lists: collections.abc.Iterable[builtins.str] | None = ...,
        connected_channels: collections.abc.Iterable[builtins.str] | None = ...,
        passing_sites: collections.abc.Iterable[builtins.int] | None = ...,
        failing_sites: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["channel_lists", b"channel_lists", "connected_channels", b"connected_channels", "failing_sites", b"failing_sites", "passing_sites", b"passing_sites", "resource_names", b"resource_names", "session_names", b"session_names"]) -> None: ...

global___Outputs = Outputs
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidigital/types_pb2_grpc.py sha256=fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb bytes=163 -->
## FILE: packages/service/tests/utilities/stubs/nidigital/types_pb2_grpc.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nidigital/types_pb2_grpc.py`
- sha256: `fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb`
- bytes: 163

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidigital/types_pb2_grpc.pyi sha256=f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed bytes=430 -->
## FILE: packages/service/tests/utilities/stubs/nidigital/types_pb2_grpc.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nidigital/types_pb2_grpc.pyi`
- sha256: `f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed`
- bytes: 430

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidmm/__init__.py sha256=cf19f63b49ab4491967c03d4ab043490d0bc1ebf447fff77cc05cf0ada824d8e bytes=61 -->
## FILE: packages/service/tests/utilities/stubs/nidmm/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nidmm/__init__.py`
- sha256: `cf19f63b49ab4491967c03d4ab043490d0bc1ebf447fff77cc05cf0ada824d8e`
- bytes: 61

````python
"""Auto generated gRPC files for nidmm test measurement."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidmm/types.proto sha256=0c3c01e54193340bf3e8782b4dc87c7d2c4e2b137b86d6acb277dd9a465ddb6e bytes=449 -->
## FILE: packages/service/tests/utilities/stubs/nidmm/types.proto

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nidmm/types.proto`
- sha256: `0c3c01e54193340bf3e8782b4dc87c7d2c4e2b137b86d6acb277dd9a465ddb6e`
- bytes: 449

````protobuf
syntax = "proto3";
package ni.measurementlink.measurement.tests.nidmm;

message Configurations {
    repeated string pin_names = 1;
    bool multi_session = 2;
}

message Outputs {
    repeated string session_names = 1;
    repeated string resource_names = 2;
    repeated string channel_lists = 3;
    repeated string connected_channels = 4;
    repeated bool signals_out_of_range = 5;
    repeated double absolute_resolutions = 6;
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidmm/types_pb2.py sha256=d37a3c42fe91bdec5c445ff54ae395afbcdfdee46b4a10e7a144ad68fdc507bf bytes=1458 -->
## FILE: packages/service/tests/utilities/stubs/nidmm/types_pb2.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nidmm/types_pb2.py`
- sha256: `d37a3c42fe91bdec5c445ff54ae395afbcdfdee46b4a10e7a144ad68fdc507bf`
- bytes: 1458

````python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nidmm/types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11nidmm/types.proto\x12*ni.measurementlink.measurement.tests.nidmm\":\n\x0e\x43onfigurations\x12\x11\n\tpin_names\x18\x01 \x03(\t\x12\x15\n\rmulti_session\x18\x02 \x01(\x08\"\xa7\x01\n\x07Outputs\x12\x15\n\rsession_names\x18\x01 \x03(\t\x12\x16\n\x0eresource_names\x18\x02 \x03(\t\x12\x15\n\rchannel_lists\x18\x03 \x03(\t\x12\x1a\n\x12\x63onnected_channels\x18\x04 \x03(\t\x12\x1c\n\x14signals_out_of_range\x18\x05 \x03(\x08\x12\x1c\n\x14\x61\x62solute_resolutions\x18\x06 \x03(\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nidmm.types_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONFIGURATIONS._serialized_start=65
  _CONFIGURATIONS._serialized_end=123
  _OUTPUTS._serialized_start=126
  _OUTPUTS._serialized_end=293
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidmm/types_pb2.pyi sha256=47d40439e6deac440e625ebbd57b9cae860fed1ead962ae08d7a965038cfc480 bytes=3168 -->
## FILE: packages/service/tests/utilities/stubs/nidmm/types_pb2.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nidmm/types_pb2.pyi`
- sha256: `47d40439e6deac440e625ebbd57b9cae860fed1ead962ae08d7a965038cfc480`
- bytes: 3168

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Configurations(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PIN_NAMES_FIELD_NUMBER: builtins.int
    MULTI_SESSION_FIELD_NUMBER: builtins.int
    multi_session: builtins.bool
    @property
    def pin_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        pin_names: collections.abc.Iterable[builtins.str] | None = ...,
        multi_session: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["multi_session", b"multi_session", "pin_names", b"pin_names"]) -> None: ...

global___Configurations = Configurations

@typing.final
class Outputs(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SESSION_NAMES_FIELD_NUMBER: builtins.int
    RESOURCE_NAMES_FIELD_NUMBER: builtins.int
    CHANNEL_LISTS_FIELD_NUMBER: builtins.int
    CONNECTED_CHANNELS_FIELD_NUMBER: builtins.int
    SIGNALS_OUT_OF_RANGE_FIELD_NUMBER: builtins.int
    ABSOLUTE_RESOLUTIONS_FIELD_NUMBER: builtins.int
    @property
    def session_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def resource_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def channel_lists(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def connected_channels(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def signals_out_of_range(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bool]: ...
    @property
    def absolute_resolutions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    def __init__(
        self,
        *,
        session_names: collections.abc.Iterable[builtins.str] | None = ...,
        resource_names: collections.abc.Iterable[builtins.str] | None = ...,
        channel_lists: collections.abc.Iterable[builtins.str] | None = ...,
        connected_channels: collections.abc.Iterable[builtins.str] | None = ...,
        signals_out_of_range: collections.abc.Iterable[builtins.bool] | None = ...,
        absolute_resolutions: collections.abc.Iterable[builtins.float] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["absolute_resolutions", b"absolute_resolutions", "channel_lists", b"channel_lists", "connected_channels", b"connected_channels", "resource_names", b"resource_names", "session_names", b"session_names", "signals_out_of_range", b"signals_out_of_range"]) -> None: ...

global___Outputs = Outputs
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidmm/types_pb2_grpc.py sha256=fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb bytes=163 -->
## FILE: packages/service/tests/utilities/stubs/nidmm/types_pb2_grpc.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nidmm/types_pb2_grpc.py`
- sha256: `fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb`
- bytes: 163

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidmm/types_pb2_grpc.pyi sha256=f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed bytes=430 -->
## FILE: packages/service/tests/utilities/stubs/nidmm/types_pb2_grpc.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nidmm/types_pb2_grpc.pyi`
- sha256: `f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed`
- bytes: 430

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nifgen/__init__.py sha256=57454a74686c74a48aab7e5864e77cbca2528bbe29a14aeea0fbb038293461fa bytes=62 -->
## FILE: packages/service/tests/utilities/stubs/nifgen/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nifgen/__init__.py`
- sha256: `57454a74686c74a48aab7e5864e77cbca2528bbe29a14aeea0fbb038293461fa`
- bytes: 62

````python
"""Auto generated gRPC files for nifgen test measurement."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nifgen/types.proto sha256=722ebdbeaae5a27cd0e81ac627f30f5df79a32a60ebd16ea890fafc7fe2bc4ec bytes=360 -->
## FILE: packages/service/tests/utilities/stubs/nifgen/types.proto

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nifgen/types.proto`
- sha256: `722ebdbeaae5a27cd0e81ac627f30f5df79a32a60ebd16ea890fafc7fe2bc4ec`
- bytes: 360

````protobuf
syntax = "proto3";
package ni.measurementlink.measurement.tests.nifgen;

message Configurations {
    repeated string pin_names = 1;
    bool multi_session = 2;
}

message Outputs {
    repeated string session_names = 1;
    repeated string resource_names = 2;
    repeated string channel_lists = 3;
    repeated string connected_channels = 4;
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nifgen/types_pb2.py sha256=70fb5518dfd051d6423660188bbc83bcfd0862c26bb6e1c3b623f8167f96ce10 bytes=1342 -->
## FILE: packages/service/tests/utilities/stubs/nifgen/types_pb2.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nifgen/types_pb2.py`
- sha256: `70fb5518dfd051d6423660188bbc83bcfd0862c26bb6e1c3b623f8167f96ce10`
- bytes: 1342

````python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nifgen/types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12nifgen/types.proto\x12+ni.measurementlink.measurement.tests.nifgen\":\n\x0e\x43onfigurations\x12\x11\n\tpin_names\x18\x01 \x03(\t\x12\x15\n\rmulti_session\x18\x02 \x01(\x08\"k\n\x07Outputs\x12\x15\n\rsession_names\x18\x01 \x03(\t\x12\x16\n\x0eresource_names\x18\x02 \x03(\t\x12\x15\n\rchannel_lists\x18\x03 \x03(\t\x12\x1a\n\x12\x63onnected_channels\x18\x04 \x03(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nifgen.types_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONFIGURATIONS._serialized_start=67
  _CONFIGURATIONS._serialized_end=125
  _OUTPUTS._serialized_start=127
  _OUTPUTS._serialized_end=234
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nifgen/types_pb2.pyi sha256=20ea7af0b8b33b8bb91b2909b4f8c5d15dbb29ebb7961576c75044046d8ff08e bytes=2514 -->
## FILE: packages/service/tests/utilities/stubs/nifgen/types_pb2.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nifgen/types_pb2.pyi`
- sha256: `20ea7af0b8b33b8bb91b2909b4f8c5d15dbb29ebb7961576c75044046d8ff08e`
- bytes: 2514

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Configurations(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PIN_NAMES_FIELD_NUMBER: builtins.int
    MULTI_SESSION_FIELD_NUMBER: builtins.int
    multi_session: builtins.bool
    @property
    def pin_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        pin_names: collections.abc.Iterable[builtins.str] | None = ...,
        multi_session: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["multi_session", b"multi_session", "pin_names", b"pin_names"]) -> None: ...

global___Configurations = Configurations

@typing.final
class Outputs(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SESSION_NAMES_FIELD_NUMBER: builtins.int
    RESOURCE_NAMES_FIELD_NUMBER: builtins.int
    CHANNEL_LISTS_FIELD_NUMBER: builtins.int
    CONNECTED_CHANNELS_FIELD_NUMBER: builtins.int
    @property
    def session_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def resource_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def channel_lists(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def connected_channels(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        session_names: collections.abc.Iterable[builtins.str] | None = ...,
        resource_names: collections.abc.Iterable[builtins.str] | None = ...,
        channel_lists: collections.abc.Iterable[builtins.str] | None = ...,
        connected_channels: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["channel_lists", b"channel_lists", "connected_channels", b"connected_channels", "resource_names", b"resource_names", "session_names", b"session_names"]) -> None: ...

global___Outputs = Outputs
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nifgen/types_pb2_grpc.py sha256=fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb bytes=163 -->
## FILE: packages/service/tests/utilities/stubs/nifgen/types_pb2_grpc.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nifgen/types_pb2_grpc.py`
- sha256: `fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb`
- bytes: 163

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nifgen/types_pb2_grpc.pyi sha256=f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed bytes=430 -->
## FILE: packages/service/tests/utilities/stubs/nifgen/types_pb2_grpc.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/nifgen/types_pb2_grpc.pyi`
- sha256: `f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed`
- bytes: 430

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/niscope/__init__.py sha256=3eb4b2322c573338d7a6c9b348a1ab27a53f886d010f31efb6cfdfbdb3a32eb6 bytes=63 -->
## FILE: packages/service/tests/utilities/stubs/niscope/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/niscope/__init__.py`
- sha256: `3eb4b2322c573338d7a6c9b348a1ab27a53f886d010f31efb6cfdfbdb3a32eb6`
- bytes: 63

````python
"""Auto generated gRPC files for niscope test measurement."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/niscope/types.proto sha256=f1ea84b906ddf1899dc749bc31bf83b9b935e27a2758e4552b1e32826cee5f8d bytes=396 -->
## FILE: packages/service/tests/utilities/stubs/niscope/types.proto

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/niscope/types.proto`
- sha256: `f1ea84b906ddf1899dc749bc31bf83b9b935e27a2758e4552b1e32826cee5f8d`
- bytes: 396

````protobuf
syntax = "proto3";
package ni.measurementlink.measurement.tests.niscope;

message Configurations {
    repeated string pin_names = 1;
    bool multi_session = 2;
}

message Outputs {
    repeated string session_names = 1;
    repeated string resource_names = 2;
    repeated string channel_lists = 3;
    repeated string connected_channels = 4;
    repeated double waveform = 5;
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/niscope/types_pb2.py sha256=d288187b26ac10c4bcb053be5e3cb5d722390142aa96680335afa6bb59342166 bytes=1389 -->
## FILE: packages/service/tests/utilities/stubs/niscope/types_pb2.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/niscope/types_pb2.py`
- sha256: `d288187b26ac10c4bcb053be5e3cb5d722390142aa96680335afa6bb59342166`
- bytes: 1389

````python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: niscope/types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13niscope/types.proto\x12,ni.measurementlink.measurement.tests.niscope\":\n\x0e\x43onfigurations\x12\x11\n\tpin_names\x18\x01 \x03(\t\x12\x15\n\rmulti_session\x18\x02 \x01(\x08\"}\n\x07Outputs\x12\x15\n\rsession_names\x18\x01 \x03(\t\x12\x16\n\x0eresource_names\x18\x02 \x03(\t\x12\x15\n\rchannel_lists\x18\x03 \x03(\t\x12\x1a\n\x12\x63onnected_channels\x18\x04 \x03(\t\x12\x10\n\x08waveform\x18\x05 \x03(\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'niscope.types_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONFIGURATIONS._serialized_start=69
  _CONFIGURATIONS._serialized_end=127
  _OUTPUTS._serialized_start=129
  _OUTPUTS._serialized_end=254
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/niscope/types_pb2.pyi sha256=82c4a5aea07344b5fb9f6cbc75382a8f3662438bea7744ef878059e8cfdf4976 bytes=2782 -->
## FILE: packages/service/tests/utilities/stubs/niscope/types_pb2.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/niscope/types_pb2.pyi`
- sha256: `82c4a5aea07344b5fb9f6cbc75382a8f3662438bea7744ef878059e8cfdf4976`
- bytes: 2782

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Configurations(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PIN_NAMES_FIELD_NUMBER: builtins.int
    MULTI_SESSION_FIELD_NUMBER: builtins.int
    multi_session: builtins.bool
    @property
    def pin_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        pin_names: collections.abc.Iterable[builtins.str] | None = ...,
        multi_session: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["multi_session", b"multi_session", "pin_names", b"pin_names"]) -> None: ...

global___Configurations = Configurations

@typing.final
class Outputs(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SESSION_NAMES_FIELD_NUMBER: builtins.int
    RESOURCE_NAMES_FIELD_NUMBER: builtins.int
    CHANNEL_LISTS_FIELD_NUMBER: builtins.int
    CONNECTED_CHANNELS_FIELD_NUMBER: builtins.int
    WAVEFORM_FIELD_NUMBER: builtins.int
    @property
    def session_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def resource_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def channel_lists(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def connected_channels(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def waveform(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    def __init__(
        self,
        *,
        session_names: collections.abc.Iterable[builtins.str] | None = ...,
        resource_names: collections.abc.Iterable[builtins.str] | None = ...,
        channel_lists: collections.abc.Iterable[builtins.str] | None = ...,
        connected_channels: collections.abc.Iterable[builtins.str] | None = ...,
        waveform: collections.abc.Iterable[builtins.float] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["channel_lists", b"channel_lists", "connected_channels", b"connected_channels", "resource_names", b"resource_names", "session_names", b"session_names", "waveform", b"waveform"]) -> None: ...

global___Outputs = Outputs
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/niscope/types_pb2_grpc.py sha256=fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb bytes=163 -->
## FILE: packages/service/tests/utilities/stubs/niscope/types_pb2_grpc.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/niscope/types_pb2_grpc.py`
- sha256: `fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb`
- bytes: 163

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/niscope/types_pb2_grpc.pyi sha256=f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed bytes=430 -->
## FILE: packages/service/tests/utilities/stubs/niscope/types_pb2_grpc.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/niscope/types_pb2_grpc.pyi`
- sha256: `f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed`
- bytes: 430

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/niswitch/__init__.py sha256=8238c3c035148eaa904864116bab30b4842ab9498ed31ed86a6d3db3acb066a3 bytes=64 -->
## FILE: packages/service/tests/utilities/stubs/niswitch/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/niswitch/__init__.py`
- sha256: `8238c3c035148eaa904864116bab30b4842ab9498ed31ed86a6d3db3acb066a3`
- bytes: 64

````python
"""Auto generated gRPC files for niswitch test measurement."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/niswitch/types.proto sha256=3970f5ca927c0597e60cf967e01076ba03a5b57d8466d8308ea14c148f55de1a bytes=362 -->
## FILE: packages/service/tests/utilities/stubs/niswitch/types.proto

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/niswitch/types.proto`
- sha256: `3970f5ca927c0597e60cf967e01076ba03a5b57d8466d8308ea14c148f55de1a`
- bytes: 362

````protobuf
syntax = "proto3";
package ni.measurementlink.measurement.tests.niswitch;

message Configurations {
    repeated string relay_names = 1;
    bool multi_session = 2;
}

message Outputs {
    repeated string session_names = 1;
    repeated string resource_names = 2;
    repeated string channel_lists = 3;
    repeated string connected_channels = 4;
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/niswitch/types_pb2.py sha256=97b78dcce37ce9a57bc7d200c2e84a1161ddb622fc8c94c1ba877519d6c3a12c bytes=1354 -->
## FILE: packages/service/tests/utilities/stubs/niswitch/types_pb2.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/niswitch/types_pb2.py`
- sha256: `97b78dcce37ce9a57bc7d200c2e84a1161ddb622fc8c94c1ba877519d6c3a12c`
- bytes: 1354

````python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: niswitch/types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14niswitch/types.proto\x12-ni.measurementlink.measurement.tests.niswitch\"<\n\x0e\x43onfigurations\x12\x13\n\x0brelay_names\x18\x01 \x03(\t\x12\x15\n\rmulti_session\x18\x02 \x01(\x08\"k\n\x07Outputs\x12\x15\n\rsession_names\x18\x01 \x03(\t\x12\x16\n\x0eresource_names\x18\x02 \x03(\t\x12\x15\n\rchannel_lists\x18\x03 \x03(\t\x12\x1a\n\x12\x63onnected_channels\x18\x04 \x03(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'niswitch.types_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONFIGURATIONS._serialized_start=71
  _CONFIGURATIONS._serialized_end=131
  _OUTPUTS._serialized_start=133
  _OUTPUTS._serialized_end=240
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/niswitch/types_pb2.pyi sha256=ebd2d5f7500e8ffa048c891a30e1380ba9688368763aa71250c13903220387cd bytes=2524 -->
## FILE: packages/service/tests/utilities/stubs/niswitch/types_pb2.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/niswitch/types_pb2.pyi`
- sha256: `ebd2d5f7500e8ffa048c891a30e1380ba9688368763aa71250c13903220387cd`
- bytes: 2524

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Configurations(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RELAY_NAMES_FIELD_NUMBER: builtins.int
    MULTI_SESSION_FIELD_NUMBER: builtins.int
    multi_session: builtins.bool
    @property
    def relay_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        relay_names: collections.abc.Iterable[builtins.str] | None = ...,
        multi_session: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["multi_session", b"multi_session", "relay_names", b"relay_names"]) -> None: ...

global___Configurations = Configurations

@typing.final
class Outputs(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SESSION_NAMES_FIELD_NUMBER: builtins.int
    RESOURCE_NAMES_FIELD_NUMBER: builtins.int
    CHANNEL_LISTS_FIELD_NUMBER: builtins.int
    CONNECTED_CHANNELS_FIELD_NUMBER: builtins.int
    @property
    def session_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def resource_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def channel_lists(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def connected_channels(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        session_names: collections.abc.Iterable[builtins.str] | None = ...,
        resource_names: collections.abc.Iterable[builtins.str] | None = ...,
        channel_lists: collections.abc.Iterable[builtins.str] | None = ...,
        connected_channels: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["channel_lists", b"channel_lists", "connected_channels", b"connected_channels", "resource_names", b"resource_names", "session_names", b"session_names"]) -> None: ...

global___Outputs = Outputs
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/niswitch/types_pb2_grpc.py sha256=fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb bytes=163 -->
## FILE: packages/service/tests/utilities/stubs/niswitch/types_pb2_grpc.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/niswitch/types_pb2_grpc.py`
- sha256: `fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb`
- bytes: 163

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/niswitch/types_pb2_grpc.pyi sha256=f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed bytes=430 -->
## FILE: packages/service/tests/utilities/stubs/niswitch/types_pb2_grpc.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/niswitch/types_pb2_grpc.pyi`
- sha256: `f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed`
- bytes: 430

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/niswitchmultiplexer/types.proto sha256=94cd85189571d4bb3a74f321261fe0b0fea19d591a5901f30fd4776336d87144 bytes=400 -->
## FILE: packages/service/tests/utilities/stubs/niswitchmultiplexer/types.proto

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/niswitchmultiplexer/types.proto`
- sha256: `94cd85189571d4bb3a74f321261fe0b0fea19d591a5901f30fd4776336d87144`
- bytes: 400

````protobuf
syntax = "proto3";
package ni.measurementlink.measurement.tests.niswitchmultiplexer;

message Configurations {
    repeated string pin_names = 1;
    bool multi_session = 2;
}

message Outputs {
    repeated string multiplexer_session_names = 1;
    repeated string multiplexer_resource_names = 2;
    repeated string multiplexer_routes = 3;
    repeated string connected_channels = 4;
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/niswitchmultiplexer/types_pb2.py sha256=a405a5ab3fa577a895d43f3fb1389bbff074695d124b054b9308d6e4b788c119 bytes=1432 -->
## FILE: packages/service/tests/utilities/stubs/niswitchmultiplexer/types_pb2.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/niswitchmultiplexer/types_pb2.py`
- sha256: `a405a5ab3fa577a895d43f3fb1389bbff074695d124b054b9308d6e4b788c119`
- bytes: 1432

````python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: niswitchmultiplexer/types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fniswitchmultiplexer/types.proto\x12\x38ni.measurementlink.measurement.tests.niswitchmultiplexer\":\n\x0e\x43onfigurations\x12\x11\n\tpin_names\x18\x01 \x03(\t\x12\x15\n\rmulti_session\x18\x02 \x01(\x08\"\x88\x01\n\x07Outputs\x12!\n\x19multiplexer_session_names\x18\x01 \x03(\t\x12\"\n\x1amultiplexer_resource_names\x18\x02 \x03(\t\x12\x1a\n\x12multiplexer_routes\x18\x03 \x03(\t\x12\x1a\n\x12\x63onnected_channels\x18\x04 \x03(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'niswitchmultiplexer.types_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONFIGURATIONS._serialized_start=93
  _CONFIGURATIONS._serialized_end=151
  _OUTPUTS._serialized_start=154
  _OUTPUTS._serialized_end=290
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/niswitchmultiplexer/types_pb2.pyi sha256=2bee3f8243af04cfa90f4830370640f07f2b3dbc985b57df03818264a02af483 bytes=2659 -->
## FILE: packages/service/tests/utilities/stubs/niswitchmultiplexer/types_pb2.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/niswitchmultiplexer/types_pb2.pyi`
- sha256: `2bee3f8243af04cfa90f4830370640f07f2b3dbc985b57df03818264a02af483`
- bytes: 2659

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Configurations(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PIN_NAMES_FIELD_NUMBER: builtins.int
    MULTI_SESSION_FIELD_NUMBER: builtins.int
    multi_session: builtins.bool
    @property
    def pin_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        pin_names: collections.abc.Iterable[builtins.str] | None = ...,
        multi_session: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["multi_session", b"multi_session", "pin_names", b"pin_names"]) -> None: ...

global___Configurations = Configurations

@typing.final
class Outputs(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MULTIPLEXER_SESSION_NAMES_FIELD_NUMBER: builtins.int
    MULTIPLEXER_RESOURCE_NAMES_FIELD_NUMBER: builtins.int
    MULTIPLEXER_ROUTES_FIELD_NUMBER: builtins.int
    CONNECTED_CHANNELS_FIELD_NUMBER: builtins.int
    @property
    def multiplexer_session_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def multiplexer_resource_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def multiplexer_routes(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def connected_channels(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        multiplexer_session_names: collections.abc.Iterable[builtins.str] | None = ...,
        multiplexer_resource_names: collections.abc.Iterable[builtins.str] | None = ...,
        multiplexer_routes: collections.abc.Iterable[builtins.str] | None = ...,
        connected_channels: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["connected_channels", b"connected_channels", "multiplexer_resource_names", b"multiplexer_resource_names", "multiplexer_routes", b"multiplexer_routes", "multiplexer_session_names", b"multiplexer_session_names"]) -> None: ...

global___Outputs = Outputs
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/niswitchmultiplexer/types_pb2_grpc.py sha256=fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb bytes=163 -->
## FILE: packages/service/tests/utilities/stubs/niswitchmultiplexer/types_pb2_grpc.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/niswitchmultiplexer/types_pb2_grpc.py`
- sha256: `fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb`
- bytes: 163

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/niswitchmultiplexer/types_pb2_grpc.pyi sha256=f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed bytes=430 -->
## FILE: packages/service/tests/utilities/stubs/niswitchmultiplexer/types_pb2_grpc.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/niswitchmultiplexer/types_pb2_grpc.pyi`
- sha256: `f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed`
- bytes: 430

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/pinaware/__init__.py sha256=4345dfe9f7f17c9e4eaab3fe3d51efae9627c266eabd6a8436fdceeadd8713d1 bytes=60 -->
## FILE: packages/service/tests/utilities/stubs/pinaware/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/pinaware/__init__.py`
- sha256: `4345dfe9f7f17c9e4eaab3fe3d51efae9627c266eabd6a8436fdceeadd8713d1`
- bytes: 60

````python
"""Auto generated gRPC files for pin-aware measurement."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/pinaware/types.proto sha256=414f626f8ba58db68271eb71169a8ac57419a8e43b75506cecef73274a11435e bytes=376 -->
## FILE: packages/service/tests/utilities/stubs/pinaware/types.proto

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/pinaware/types.proto`
- sha256: `414f626f8ba58db68271eb71169a8ac57419a8e43b75506cecef73274a11435e`
- bytes: 376

````protobuf
syntax = "proto3";
package ni.measurementlink.measurement.tests.pinaware;

message Configurations {
    repeated string pin_names = 1;
    bool multi_session = 2;
}

message Outputs {
    string pin_map_id = 1;
    repeated int32 sites = 2;
    repeated string session_names = 3;
    repeated string resource_names = 4;
    repeated string channel_lists = 5;
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/pinaware/types_pb2.py sha256=10bb544d13ab661219764d3bc7b1ba096de1aafa9ff32e7e51e763990c3c6f90 bytes=1372 -->
## FILE: packages/service/tests/utilities/stubs/pinaware/types_pb2.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/pinaware/types_pb2.py`
- sha256: `10bb544d13ab661219764d3bc7b1ba096de1aafa9ff32e7e51e763990c3c6f90`
- bytes: 1372

````python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pinaware/types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14pinaware/types.proto\x12-ni.measurementlink.measurement.tests.pinaware\":\n\x0e\x43onfigurations\x12\x11\n\tpin_names\x18\x01 \x03(\t\x12\x15\n\rmulti_session\x18\x02 \x01(\x08\"r\n\x07Outputs\x12\x12\n\npin_map_id\x18\x01 \x01(\t\x12\r\n\x05sites\x18\x02 \x03(\x05\x12\x15\n\rsession_names\x18\x03 \x03(\t\x12\x16\n\x0eresource_names\x18\x04 \x03(\t\x12\x15\n\rchannel_lists\x18\x05 \x03(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pinaware.types_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONFIGURATIONS._serialized_start=71
  _CONFIGURATIONS._serialized_end=129
  _OUTPUTS._serialized_start=131
  _OUTPUTS._serialized_end=245
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/pinaware/types_pb2.pyi sha256=09d0677d080565cc0784f1b9356ac8219120c6a28217122b67f52bd0cb2b8c2d bytes=2592 -->
## FILE: packages/service/tests/utilities/stubs/pinaware/types_pb2.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/pinaware/types_pb2.pyi`
- sha256: `09d0677d080565cc0784f1b9356ac8219120c6a28217122b67f52bd0cb2b8c2d`
- bytes: 2592

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Configurations(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PIN_NAMES_FIELD_NUMBER: builtins.int
    MULTI_SESSION_FIELD_NUMBER: builtins.int
    multi_session: builtins.bool
    @property
    def pin_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        pin_names: collections.abc.Iterable[builtins.str] | None = ...,
        multi_session: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["multi_session", b"multi_session", "pin_names", b"pin_names"]) -> None: ...

global___Configurations = Configurations

@typing.final
class Outputs(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PIN_MAP_ID_FIELD_NUMBER: builtins.int
    SITES_FIELD_NUMBER: builtins.int
    SESSION_NAMES_FIELD_NUMBER: builtins.int
    RESOURCE_NAMES_FIELD_NUMBER: builtins.int
    CHANNEL_LISTS_FIELD_NUMBER: builtins.int
    pin_map_id: builtins.str
    @property
    def sites(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def session_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def resource_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def channel_lists(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        pin_map_id: builtins.str = ...,
        sites: collections.abc.Iterable[builtins.int] | None = ...,
        session_names: collections.abc.Iterable[builtins.str] | None = ...,
        resource_names: collections.abc.Iterable[builtins.str] | None = ...,
        channel_lists: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["channel_lists", b"channel_lists", "pin_map_id", b"pin_map_id", "resource_names", b"resource_names", "session_names", b"session_names", "sites", b"sites"]) -> None: ...

global___Outputs = Outputs
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/pinaware/types_pb2_grpc.py sha256=fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb bytes=163 -->
## FILE: packages/service/tests/utilities/stubs/pinaware/types_pb2_grpc.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/pinaware/types_pb2_grpc.py`
- sha256: `fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb`
- bytes: 163

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/pinaware/types_pb2_grpc.pyi sha256=f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed bytes=430 -->
## FILE: packages/service/tests/utilities/stubs/pinaware/types_pb2_grpc.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/pinaware/types_pb2_grpc.pyi`
- sha256: `f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed`
- bytes: 430

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/serialization/__init__.py sha256=bee4aa141aed8371ec690c41ccebddb41d0552b1868072271c46c2d6dab7b7da bytes=58 -->
## FILE: packages/service/tests/utilities/stubs/serialization/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/serialization/__init__.py`
- sha256: `bee4aa141aed8371ec690c41ccebddb41d0552b1868072271c46c2d6dab7b7da`
- bytes: 58

````python
"""Auto generated gRPC files for serialization tests."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/serialization/bigmessage.proto sha256=4555ff17af0bafa56dcef13ba5acc7d983afb7467df76224d39c5654bb70f0ed bytes=2490 -->
## FILE: packages/service/tests/utilities/stubs/serialization/bigmessage.proto

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/serialization/bigmessage.proto`
- sha256: `4555ff17af0bafa56dcef13ba5acc7d983afb7467df76224d39c5654bb70f0ed`
- bytes: 2490

````protobuf
syntax = "proto3";
package ni.measurementlink.measurement.tests.serialization;

message BigMessage {
  double field1 = 1;
  double field2 = 2;
  double field3 = 3;
  double field4 = 4;
  double field5 = 5;
  double field6 = 6;
  double field7 = 7;
  double field8 = 8;
  double field9 = 9;
  double field10 = 10;
  double field11 = 11;
  double field12 = 12;
  double field13 = 13;
  double field14 = 14;
  double field15 = 15;
  double field16 = 16;
  double field17 = 17;
  double field18 = 18;
  double field19 = 19;
  double field20 = 20;
  double field21 = 21;
  double field22 = 22;
  double field23 = 23;
  double field24 = 24;
  double field25 = 25;
  double field26 = 26;
  double field27 = 27;
  double field28 = 28;
  double field29 = 29;
  double field30 = 30;
  double field31 = 31;
  double field32 = 32;
  double field33 = 33;
  double field34 = 34;
  double field35 = 35;
  double field36 = 36;
  double field37 = 37;
  double field38 = 38;
  double field39 = 39;
  double field40 = 40;
  double field41 = 41;
  double field42 = 42;
  double field43 = 43;
  double field44 = 44;
  double field45 = 45;
  double field46 = 46;
  double field47 = 47;
  double field48 = 48;
  double field49 = 49;
  double field50 = 50;
  double field51 = 51;
  double field52 = 52;
  double field53 = 53;
  double field54 = 54;
  double field55 = 55;
  double field56 = 56;
  double field57 = 57;
  double field58 = 58;
  double field59 = 59;
  double field60 = 60;
  double field61 = 61;
  double field62 = 62;
  double field63 = 63;
  double field64 = 64;
  double field65 = 65;
  double field66 = 66;
  double field67 = 67;
  double field68 = 68;
  double field69 = 69;
  double field70 = 70;
  double field71 = 71;
  double field72 = 72;
  double field73 = 73;
  double field74 = 74;
  double field75 = 75;
  double field76 = 76;
  double field77 = 77;
  double field78 = 78;
  double field79 = 79;
  double field80 = 80;
  double field81 = 81;
  double field82 = 82;
  double field83 = 83;
  double field84 = 84;
  double field85 = 85;
  double field86 = 86;
  double field87 = 87;
  double field88 = 88;
  double field89 = 89;
  double field90 = 90;
  double field91 = 91;
  double field92 = 92;
  double field93 = 93;
  double field94 = 94;
  double field95 = 95;
  double field96 = 96;
  double field97 = 97;
  double field98 = 98;
  double field99 = 99;
  double field100 = 100;
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/serialization/bigmessage_pb2.py sha256=8dff09881aa3629443aab4b5306d0fc63d57044b457c0e5adcd8fe3038bfad41 bytes=5083 -->
## FILE: packages/service/tests/utilities/stubs/serialization/bigmessage_pb2.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/serialization/bigmessage_pb2.py`
- sha256: `8dff09881aa3629443aab4b5306d0fc63d57044b457c0e5adcd8fe3038bfad41`
- bytes: 5083

````python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: serialization/bigmessage.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eserialization/bigmessage.proto\x12\x32ni.measurementlink.measurement.tests.serialization\"\xa8\r\n\nBigMessage\x12\x0e\n\x06\x66ield1\x18\x01 \x01(\x01\x12\x0e\n\x06\x66ield2\x18\x02 \x01(\x01\x12\x0e\n\x06\x66ield3\x18\x03 \x01(\x01\x12\x0e\n\x06\x66ield4\x18\x04 \x01(\x01\x12\x0e\n\x06\x66ield5\x18\x05 \x01(\x01\x12\x0e\n\x06\x66ield6\x18\x06 \x01(\x01\x12\x0e\n\x06\x66ield7\x18\x07 \x01(\x01\x12\x0e\n\x06\x66ield8\x18\x08 \x01(\x01\x12\x0e\n\x06\x66ield9\x18\t \x01(\x01\x12\x0f\n\x07\x66ield10\x18\n \x01(\x01\x12\x0f\n\x07\x66ield11\x18\x0b \x01(\x01\x12\x0f\n\x07\x66ield12\x18\x0c \x01(\x01\x12\x0f\n\x07\x66ield13\x18\r \x01(\x01\x12\x0f\n\x07\x66ield14\x18\x0e \x01(\x01\x12\x0f\n\x07\x66ield15\x18\x0f \x01(\x01\x12\x0f\n\x07\x66ield16\x18\x10 \x01(\x01\x12\x0f\n\x07\x66ield17\x18\x11 \x01(\x01\x12\x0f\n\x07\x66ield18\x18\x12 \x01(\x01\x12\x0f\n\x07\x66ield19\x18\x13 \x01(\x01\x12\x0f\n\x07\x66ield20\x18\x14 \x01(\x01\x12\x0f\n\x07\x66ield21\x18\x15 \x01(\x01\x12\x0f\n\x07\x66ield22\x18\x16 \x01(\x01\x12\x0f\n\x07\x66ield23\x18\x17 \x01(\x01\x12\x0f\n\x07\x66ield24\x18\x18 \x01(\x01\x12\x0f\n\x07\x66ield25\x18\x19 \x01(\x01\x12\x0f\n\x07\x66ield26\x18\x1a \x01(\x01\x12\x0f\n\x07\x66ield27\x18\x1b \x01(\x01\x12\x0f\n\x07\x66ield28\x18\x1c \x01(\x01\x12\x0f\n\x07\x66ield29\x18\x1d \x01(\x01\x12\x0f\n\x07\x66ield30\x18\x1e \x01(\x01\x12\x0f\n\x07\x66ield31\x18\x1f \x01(\x01\x12\x0f\n\x07\x66ield32\x18  \x01(\x01\x12\x0f\n\x07\x66ield33\x18! \x01(\x01\x12\x0f\n\x07\x66ield34\x18\" \x01(\x01\x12\x0f\n\x07\x66ield35\x18# \x01(\x01\x12\x0f\n\x07\x66ield36\x18$ \x01(\x01\x12\x0f\n\x07\x66ield37\x18% \x01(\x01\x12\x0f\n\x07\x66ield38\x18& \x01(\x01\x12\x0f\n\x07\x66ield39\x18\' \x01(\x01\x12\x0f\n\x07\x66ield40\x18( \x01(\x01\x12\x0f\n\x07\x66ield41\x18) \x01(\x01\x12\x0f\n\x07\x66ield42\x18* \x01(\x01\x12\x0f\n\x07\x66ield43\x18+ \x01(\x01\x12\x0f\n\x07\x66ield44\x18, \x01(\x01\x12\x0f\n\x07\x66ield45\x18- \x01(\x01\x12\x0f\n\x07\x66ield46\x18. \x01(\x01\x12\x0f\n\x07\x66ield47\x18/ \x01(\x01\x12\x0f\n\x07\x66ield48\x18\x30 \x01(\x01\x12\x0f\n\x07\x66ield49\x18\x31 \x01(\x01\x12\x0f\n\x07\x66ield50\x18\x32 \x01(\x01\x12\x0f\n\x07\x66ield51\x18\x33 \x01(\x01\x12\x0f\n\x07\x66ield52\x18\x34 \x01(\x01\x12\x0f\n\x07\x66ield53\x18\x35 \x01(\x01\x12\x0f\n\x07\x66ield54\x18\x36 \x01(\x01\x12\x0f\n\x07\x66ield55\x18\x37 \x01(\x01\x12\x0f\n\x07\x66ield56\x18\x38 \x01(\x01\x12\x0f\n\x07\x66ield57\x18\x39 \x01(\x01\x12\x0f\n\x07\x66ield58\x18: \x01(\x01\x12\x0f\n\x07\x66ield59\x18; \x01(\x01\x12\x0f\n\x07\x66ield60\x18< \x01(\x01\x12\x0f\n\x07\x66ield61\x18= \x01(\x01\x12\x0f\n\x07\x66ield62\x18> \x01(\x01\x12\x0f\n\x07\x66ield63\x18? \x01(\x01\x12\x0f\n\x07\x66ield64\x18@ \x01(\x01\x12\x0f\n\x07\x66ield65\x18\x41 \x01(\x01\x12\x0f\n\x07\x66ield66\x18\x42 \x01(\x01\x12\x0f\n\x07\x66ield67\x18\x43 \x01(\x01\x12\x0f\n\x07\x66ield68\x18\x44 \x01(\x01\x12\x0f\n\x07\x66ield69\x18\x45 \x01(\x01\x12\x0f\n\x07\x66ield70\x18\x46 \x01(\x01\x12\x0f\n\x07\x66ield71\x18G \x01(\x01\x12\x0f\n\x07\x66ield72\x18H \x01(\x01\x12\x0f\n\x07\x66ield73\x18I \x01(\x01\x12\x0f\n\x07\x66ield74\x18J \x01(\x01\x12\x0f\n\x07\x66ield75\x18K \x01(\x01\x12\x0f\n\x07\x66ield76\x18L \x01(\x01\x12\x0f\n\x07\x66ield77\x18M \x01(\x01\x12\x0f\n\x07\x66ield78\x18N \x01(\x01\x12\x0f\n\x07\x66ield79\x18O \x01(\x01\x12\x0f\n\x07\x66ield80\x18P \x01(\x01\x12\x0f\n\x07\x66ield81\x18Q \x01(\x01\x12\x0f\n\x07\x66ield82\x18R \x01(\x01\x12\x0f\n\x07\x66ield83\x18S \x01(\x01\x12\x0f\n\x07\x66ield84\x18T \x01(\x01\x12\x0f\n\x07\x66ield85\x18U \x01(\x01\x12\x0f\n\x07\x66ield86\x18V \x01(\x01\x12\x0f\n\x07\x66ield87\x18W \x01(\x01\x12\x0f\n\x07\x66ield88\x18X \x01(\x01\x12\x0f\n\x07\x66ield89\x18Y \x01(\x01\x12\x0f\n\x07\x66ield90\x18Z \x01(\x01\x12\x0f\n\x07\x66ield91\x18[ \x01(\x01\x12\x0f\n\x07\x66ield92\x18\\ \x01(\x01\x12\x0f\n\x07\x66ield93\x18] \x01(\x01\x12\x0f\n\x07\x66ield94\x18^ \x01(\x01\x12\x0f\n\x07\x66ield95\x18_ \x01(\x01\x12\x0f\n\x07\x66ield96\x18` \x01(\x01\x12\x0f\n\x07\x66ield97\x18\x61 \x01(\x01\x12\x0f\n\x07\x66ield98\x18\x62 \x01(\x01\x12\x0f\n\x07\x66ield99\x18\x63 \x01(\x01\x12\x10\n\x08\x66ield100\x18\x64 \x01(\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'serialization.bigmessage_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BIGMESSAGE._serialized_start=87
  _BIGMESSAGE._serialized_end=1791
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/serialization/bigmessage_pb2.pyi sha256=d26c2b5a8aa41af3affe528d93162c650296f9643998b264bd19f63e902d27cf bytes=13693 -->
## FILE: packages/service/tests/utilities/stubs/serialization/bigmessage_pb2.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/serialization/bigmessage_pb2.pyi`
- sha256: `d26c2b5a8aa41af3affe528d93162c650296f9643998b264bd19f63e902d27cf`
- bytes: 13693

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class BigMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FIELD1_FIELD_NUMBER: builtins.int
    FIELD2_FIELD_NUMBER: builtins.int
    FIELD3_FIELD_NUMBER: builtins.int
    FIELD4_FIELD_NUMBER: builtins.int
    FIELD5_FIELD_NUMBER: builtins.int
    FIELD6_FIELD_NUMBER: builtins.int
    FIELD7_FIELD_NUMBER: builtins.int
    FIELD8_FIELD_NUMBER: builtins.int
    FIELD9_FIELD_NUMBER: builtins.int
    FIELD10_FIELD_NUMBER: builtins.int
    FIELD11_FIELD_NUMBER: builtins.int
    FIELD12_FIELD_NUMBER: builtins.int
    FIELD13_FIELD_NUMBER: builtins.int
    FIELD14_FIELD_NUMBER: builtins.int
    FIELD15_FIELD_NUMBER: builtins.int
    FIELD16_FIELD_NUMBER: builtins.int
    FIELD17_FIELD_NUMBER: builtins.int
    FIELD18_FIELD_NUMBER: builtins.int
    FIELD19_FIELD_NUMBER: builtins.int
    FIELD20_FIELD_NUMBER: builtins.int
    FIELD21_FIELD_NUMBER: builtins.int
    FIELD22_FIELD_NUMBER: builtins.int
    FIELD23_FIELD_NUMBER: builtins.int
    FIELD24_FIELD_NUMBER: builtins.int
    FIELD25_FIELD_NUMBER: builtins.int
    FIELD26_FIELD_NUMBER: builtins.int
    FIELD27_FIELD_NUMBER: builtins.int
    FIELD28_FIELD_NUMBER: builtins.int
    FIELD29_FIELD_NUMBER: builtins.int
    FIELD30_FIELD_NUMBER: builtins.int
    FIELD31_FIELD_NUMBER: builtins.int
    FIELD32_FIELD_NUMBER: builtins.int
    FIELD33_FIELD_NUMBER: builtins.int
    FIELD34_FIELD_NUMBER: builtins.int
    FIELD35_FIELD_NUMBER: builtins.int
    FIELD36_FIELD_NUMBER: builtins.int
    FIELD37_FIELD_NUMBER: builtins.int
    FIELD38_FIELD_NUMBER: builtins.int
    FIELD39_FIELD_NUMBER: builtins.int
    FIELD40_FIELD_NUMBER: builtins.int
    FIELD41_FIELD_NUMBER: builtins.int
    FIELD42_FIELD_NUMBER: builtins.int
    FIELD43_FIELD_NUMBER: builtins.int
    FIELD44_FIELD_NUMBER: builtins.int
    FIELD45_FIELD_NUMBER: builtins.int
    FIELD46_FIELD_NUMBER: builtins.int
    FIELD47_FIELD_NUMBER: builtins.int
    FIELD48_FIELD_NUMBER: builtins.int
    FIELD49_FIELD_NUMBER: builtins.int
    FIELD50_FIELD_NUMBER: builtins.int
    FIELD51_FIELD_NUMBER: builtins.int
    FIELD52_FIELD_NUMBER: builtins.int
    FIELD53_FIELD_NUMBER: builtins.int
    FIELD54_FIELD_NUMBER: builtins.int
    FIELD55_FIELD_NUMBER: builtins.int
    FIELD56_FIELD_NUMBER: builtins.int
    FIELD57_FIELD_NUMBER: builtins.int
    FIELD58_FIELD_NUMBER: builtins.int
    FIELD59_FIELD_NUMBER: builtins.int
    FIELD60_FIELD_NUMBER: builtins.int
    FIELD61_FIELD_NUMBER: builtins.int
    FIELD62_FIELD_NUMBER: builtins.int
    FIELD63_FIELD_NUMBER: builtins.int
    FIELD64_FIELD_NUMBER: builtins.int
    FIELD65_FIELD_NUMBER: builtins.int
    FIELD66_FIELD_NUMBER: builtins.int
    FIELD67_FIELD_NUMBER: builtins.int
    FIELD68_FIELD_NUMBER: builtins.int
    FIELD69_FIELD_NUMBER: builtins.int
    FIELD70_FIELD_NUMBER: builtins.int
    FIELD71_FIELD_NUMBER: builtins.int
    FIELD72_FIELD_NUMBER: builtins.int
    FIELD73_FIELD_NUMBER: builtins.int
    FIELD74_FIELD_NUMBER: builtins.int
    FIELD75_FIELD_NUMBER: builtins.int
    FIELD76_FIELD_NUMBER: builtins.int
    FIELD77_FIELD_NUMBER: builtins.int
    FIELD78_FIELD_NUMBER: builtins.int
    FIELD79_FIELD_NUMBER: builtins.int
    FIELD80_FIELD_NUMBER: builtins.int
    FIELD81_FIELD_NUMBER: builtins.int
    FIELD82_FIELD_NUMBER: builtins.int
    FIELD83_FIELD_NUMBER: builtins.int
    FIELD84_FIELD_NUMBER: builtins.int
    FIELD85_FIELD_NUMBER: builtins.int
    FIELD86_FIELD_NUMBER: builtins.int
    FIELD87_FIELD_NUMBER: builtins.int
    FIELD88_FIELD_NUMBER: builtins.int
    FIELD89_FIELD_NUMBER: builtins.int
    FIELD90_FIELD_NUMBER: builtins.int
    FIELD91_FIELD_NUMBER: builtins.int
    FIELD92_FIELD_NUMBER: builtins.int
    FIELD93_FIELD_NUMBER: builtins.int
    FIELD94_FIELD_NUMBER: builtins.int
    FIELD95_FIELD_NUMBER: builtins.int
    FIELD96_FIELD_NUMBER: builtins.int
    FIELD97_FIELD_NUMBER: builtins.int
    FIELD98_FIELD_NUMBER: builtins.int
    FIELD99_FIELD_NUMBER: builtins.int
    FIELD100_FIELD_NUMBER: builtins.int
    field1: builtins.float
    field2: builtins.float
    field3: builtins.float
    field4: builtins.float
    field5: builtins.float
    field6: builtins.float
    field7: builtins.float
    field8: builtins.float
    field9: builtins.float
    field10: builtins.float
    field11: builtins.float
    field12: builtins.float
    field13: builtins.float
    field14: builtins.float
    field15: builtins.float
    field16: builtins.float
    field17: builtins.float
    field18: builtins.float
    field19: builtins.float
    field20: builtins.float
    field21: builtins.float
    field22: builtins.float
    field23: builtins.float
    field24: builtins.float
    field25: builtins.float
    field26: builtins.float
    field27: builtins.float
    field28: builtins.float
    field29: builtins.float
    field30: builtins.float
    field31: builtins.float
    field32: builtins.float
    field33: builtins.float
    field34: builtins.float
    field35: builtins.float
    field36: builtins.float
    field37: builtins.float
    field38: builtins.float
    field39: builtins.float
    field40: builtins.float
    field41: builtins.float
    field42: builtins.float
    field43: builtins.float
    field44: builtins.float
    field45: builtins.float
    field46: builtins.float
    field47: builtins.float
    field48: builtins.float
    field49: builtins.float
    field50: builtins.float
    field51: builtins.float
    field52: builtins.float
    field53: builtins.float
    field54: builtins.float
    field55: builtins.float
    field56: builtins.float
    field57: builtins.float
    field58: builtins.float
    field59: builtins.float
    field60: builtins.float
    field61: builtins.float
    field62: builtins.float
    field63: builtins.float
    field64: builtins.float
    field65: builtins.float
    field66: builtins.float
    field67: builtins.float
    field68: builtins.float
    field69: builtins.float
    field70: builtins.float
    field71: builtins.float
    field72: builtins.float
    field73: builtins.float
    field74: builtins.float
    field75: builtins.float
    field76: builtins.float
    field77: builtins.float
    field78: builtins.float
    field79: builtins.float
    field80: builtins.float
    field81: builtins.float
    field82: builtins.float
    field83: builtins.float
    field84: builtins.float
    field85: builtins.float
    field86: builtins.float
    field87: builtins.float
    field88: builtins.float
    field89: builtins.float
    field90: builtins.float
    field91: builtins.float
    field92: builtins.float
    field93: builtins.float
    field94: builtins.float
    field95: builtins.float
    field96: builtins.float
    field97: builtins.float
    field98: builtins.float
    field99: builtins.float
    field100: builtins.float
    def __init__(
        self,
        *,
        field1: builtins.float = ...,
        field2: builtins.float = ...,
        field3: builtins.float = ...,
        field4: builtins.float = ...,
        field5: builtins.float = ...,
        field6: builtins.float = ...,
        field7: builtins.float = ...,
        field8: builtins.float = ...,
        field9: builtins.float = ...,
        field10: builtins.float = ...,
        field11: builtins.float = ...,
        field12: builtins.float = ...,
        field13: builtins.float = ...,
        field14: builtins.float = ...,
        field15: builtins.float = ...,
        field16: builtins.float = ...,
        field17: builtins.float = ...,
        field18: builtins.float = ...,
        field19: builtins.float = ...,
        field20: builtins.float = ...,
        field21: builtins.float = ...,
        field22: builtins.float = ...,
        field23: builtins.float = ...,
        field24: builtins.float = ...,
        field25: builtins.float = ...,
        field26: builtins.float = ...,
        field27: builtins.float = ...,
        field28: builtins.float = ...,
        field29: builtins.float = ...,
        field30: builtins.float = ...,
        field31: builtins.float = ...,
        field32: builtins.float = ...,
        field33: builtins.float = ...,
        field34: builtins.float = ...,
        field35: builtins.float = ...,
        field36: builtins.float = ...,
        field37: builtins.float = ...,
        field38: builtins.float = ...,
        field39: builtins.float = ...,
        field40: builtins.float = ...,
        field41: builtins.float = ...,
        field42: builtins.float = ...,
        field43: builtins.float = ...,
        field44: builtins.float = ...,
        field45: builtins.float = ...,
        field46: builtins.float = ...,
        field47: builtins.float = ...,
        field48: builtins.float = ...,
        field49: builtins.float = ...,
        field50: builtins.float = ...,
        field51: builtins.float = ...,
        field52: builtins.float = ...,
        field53: builtins.float = ...,
        field54: builtins.float = ...,
        field55: builtins.float = ...,
        field56: builtins.float = ...,
        field57: builtins.float = ...,
        field58: builtins.float = ...,
        field59: builtins.float = ...,
        field60: builtins.float = ...,
        field61: builtins.float = ...,
        field62: builtins.float = ...,
        field63: builtins.float = ...,
        field64: builtins.float = ...,
        field65: builtins.float = ...,
        field66: builtins.float = ...,
        field67: builtins.float = ...,
        field68: builtins.float = ...,
        field69: builtins.float = ...,
        field70: builtins.float = ...,
        field71: builtins.float = ...,
        field72: builtins.float = ...,
        field73: builtins.float = ...,
        field74: builtins.float = ...,
        field75: builtins.float = ...,
        field76: builtins.float = ...,
        field77: builtins.float = ...,
        field78: builtins.float = ...,
        field79: builtins.float = ...,
        field80: builtins.float = ...,
        field81: builtins.float = ...,
        field82: builtins.float = ...,
        field83: builtins.float = ...,
        field84: builtins.float = ...,
        field85: builtins.float = ...,
        field86: builtins.float = ...,
        field87: builtins.float = ...,
        field88: builtins.float = ...,
        field89: builtins.float = ...,
        field90: builtins.float = ...,
        field91: builtins.float = ...,
        field92: builtins.float = ...,
        field93: builtins.float = ...,
        field94: builtins.float = ...,
        field95: builtins.float = ...,
        field96: builtins.float = ...,
        field97: builtins.float = ...,
        field98: builtins.float = ...,
        field99: builtins.float = ...,
        field100: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["field1", b"field1", "field10", b"field10", "field100", b"field100", "field11", b"field11", "field12", b"field12", "field13", b"field13", "field14", b"field14", "field15", b"field15", "field16", b"field16", "field17", b"field17", "field18", b"field18", "field19", b"field19", "field2", b"field2", "field20", b"field20", "field21", b"field21", "field22", b"field22", "field23", b"field23", "field24", b"field24", "field25", b"field25", "field26", b"field26", "field27", b"field27", "field28", b"field28", "field29", b"field29", "field3", b"field3", "field30", b"field30", "field31", b"field31", "field32", b"field32", "field33", b"field33", "field34", b"field34", "field35", b"field35", "field36", b"field36", "field37", b"field37", "field38", b"field38", "field39", b"field39", "field4", b"field4", "field40", b"field40", "field41", b"field41", "field42", b"field42", "field43", b"field43", "field44", b"field44", "field45", b"field45", "field46", b"field46", "field47", b"field47", "field48", b"field48", "field49", b"field49", "field5", b"field5", "field50", b"field50", "field51", b"field51", "field52", b"field52", "field53", b"field53", "field54", b"field54", "field55", b"field55", "field56", b"field56", "field57", b"field57", "field58", b"field58", "field59", b"field59", "field6", b"field6", "field60", b"field60", "field61", b"field61", "field62", b"field62", "field63", b"field63", "field64", b"field64", "field65", b"field65", "field66", b"field66", "field67", b"field67", "field68", b"field68", "field69", b"field69", "field7", b"field7", "field70", b"field70", "field71", b"field71", "field72", b"field72", "field73", b"field73", "field74", b"field74", "field75", b"field75", "field76", b"field76", "field77", b"field77", "field78", b"field78", "field79", b"field79", "field8", b"field8", "field80", b"field80", "field81", b"field81", "field82", b"field82", "field83", b"field83", "field84", b"field84", "field85", b"field85", "field86", b"field86", "field87", b"field87", "field88", b"field88", "field89", b"field89", "field9", b"field9", "field90", b"field90", "field91", b"field91", "field92", b"field92", "field93", b"field93", "field94", b"field94", "field95", b"field95", "field96", b"field96", "field97", b"field97", "field98", b"field98", "field99", b"field99"]) -> None: ...

global___BigMessage = BigMessage
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/serialization/bigmessage_pb2_grpc.py sha256=fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb bytes=163 -->
## FILE: packages/service/tests/utilities/stubs/serialization/bigmessage_pb2_grpc.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/serialization/bigmessage_pb2_grpc.py`
- sha256: `fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb`
- bytes: 163

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/serialization/bigmessage_pb2_grpc.pyi sha256=f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed bytes=430 -->
## FILE: packages/service/tests/utilities/stubs/serialization/bigmessage_pb2_grpc.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/serialization/bigmessage_pb2_grpc.pyi`
- sha256: `f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed`
- bytes: 430

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/serialization/test.proto sha256=0efe2246d6e044b32a4a00d42a3452726fb2d95ab821a33507484f3633e57dda bytes=1194 -->
## FILE: packages/service/tests/utilities/stubs/serialization/test.proto

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/serialization/test.proto`
- sha256: `0efe2246d6e044b32a4a00d42a3452726fb2d95ab821a33507484f3633e57dda`
- bytes: 1194

````protobuf
syntax = "proto3";
package ni.measurementlink.measurement.tests.serialization;

import "ni/protobuf/types/xydata.proto";

enum DifferentColor
{
  PURPLE = 0;
  ORANGE = 1;
  TEAL = 2;
  BROWN = 3;
}

enum Countries
{
  AMERICA = 0;
  TAIWAN = 1;
  AUSTRALIA = 2;
  CANADA = 3;
}

message MeasurementParameter {
    float float_data = 1;
    double double_data = 2;
    int32 int32_data = 3;
    uint32 uint32_data = 4;
    int64 int64_data = 5;
    uint64 uint64_data = 6;
    bool bool_data = 7;
    string string_data = 8;
    repeated double double_array_data = 9;
    repeated float float_array_data = 10;
    repeated int32 int32_array_data = 11;
    repeated uint32 uint32_array_data = 12;
    repeated int64 int64_array_data = 13;
    repeated uint64 uint64_array_data = 14;
    repeated bool bool_array_data = 15;
    repeated string string_array_data = 16;
    DifferentColor enum_data = 17;
    repeated DifferentColor enum_array_data = 18;
    Countries int_enum_data = 19;
    repeated Countries int_enum_array_data = 20;
    ni.protobuf.types.DoubleXYData xy_data = 21;
    repeated ni.protobuf.types.DoubleXYData xy_data_array = 22;
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/serialization/test_pb2.py sha256=20d0e3b0b3a39e1baa8f7597dad6c31fc4d990e9bc7e80dfdbfba532d3fdd66f bytes=2925 -->
## FILE: packages/service/tests/utilities/stubs/serialization/test_pb2.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/serialization/test_pb2.py`
- sha256: `20d0e3b0b3a39e1baa8f7597dad6c31fc4d990e9bc7e80dfdbfba532d3fdd66f`
- bytes: 2925

````python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: serialization/test.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ni.protobuf.types import xydata_pb2 as ni_dot_protobuf_dot_types_dot_xydata__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18serialization/test.proto\x12\x32ni.measurementlink.measurement.tests.serialization\x1a\x1eni/protobuf/types/xydata.proto\"\xdc\x06\n\x14MeasurementParameter\x12\x12\n\nfloat_data\x18\x01 \x01(\x02\x12\x13\n\x0b\x64ouble_data\x18\x02 \x01(\x01\x12\x12\n\nint32_data\x18\x03 \x01(\x05\x12\x13\n\x0buint32_data\x18\x04 \x01(\r\x12\x12\n\nint64_data\x18\x05 \x01(\x03\x12\x13\n\x0buint64_data\x18\x06 \x01(\x04\x12\x11\n\tbool_data\x18\x07 \x01(\x08\x12\x13\n\x0bstring_data\x18\x08 \x01(\t\x12\x19\n\x11\x64ouble_array_data\x18\t \x03(\x01\x12\x18\n\x10\x66loat_array_data\x18\n \x03(\x02\x12\x18\n\x10int32_array_data\x18\x0b \x03(\x05\x12\x19\n\x11uint32_array_data\x18\x0c \x03(\r\x12\x18\n\x10int64_array_data\x18\r \x03(\x03\x12\x19\n\x11uint64_array_data\x18\x0e \x03(\x04\x12\x17\n\x0f\x62ool_array_data\x18\x0f \x03(\x08\x12\x19\n\x11string_array_data\x18\x10 \x03(\t\x12U\n\tenum_data\x18\x11 \x01(\x0e\x32\x42.ni.measurementlink.measurement.tests.serialization.DifferentColor\x12[\n\x0f\x65num_array_data\x18\x12 \x03(\x0e\x32\x42.ni.measurementlink.measurement.tests.serialization.DifferentColor\x12T\n\rint_enum_data\x18\x13 \x01(\x0e\x32=.ni.measurementlink.measurement.tests.serialization.Countries\x12Z\n\x13int_enum_array_data\x18\x14 \x03(\x0e\x32=.ni.measurementlink.measurement.tests.serialization.Countries\x12\x30\n\x07xy_data\x18\x15 \x01(\x0b\x32\x1f.ni.protobuf.types.DoubleXYData\x12\x36\n\rxy_data_array\x18\x16 \x03(\x0b\x32\x1f.ni.protobuf.types.DoubleXYData*=\n\x0e\x44ifferentColor\x12\n\n\x06PURPLE\x10\x00\x12\n\n\x06ORANGE\x10\x01\x12\x08\n\x04TEAL\x10\x02\x12\t\n\x05\x42ROWN\x10\x03*?\n\tCountries\x12\x0b\n\x07\x41MERICA\x10\x00\x12\n\n\x06TAIWAN\x10\x01\x12\r\n\tAUSTRALIA\x10\x02\x12\n\n\x06\x43\x41NADA\x10\x03\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'serialization.test_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DIFFERENTCOLOR._serialized_start=975
  _DIFFERENTCOLOR._serialized_end=1036
  _COUNTRIES._serialized_start=1038
  _COUNTRIES._serialized_end=1101
  _MEASUREMENTPARAMETER._serialized_start=113
  _MEASUREMENTPARAMETER._serialized_end=973
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/serialization/test_pb2.pyi sha256=54bd50fabde5c9ab96029512dc660b95dcd36f2e88a482f69449076d3477894e bytes=7725 -->
## FILE: packages/service/tests/utilities/stubs/serialization/test_pb2.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/serialization/test_pb2.pyi`
- sha256: `54bd50fabde5c9ab96029512dc660b95dcd36f2e88a482f69449076d3477894e`
- bytes: 7725

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import ni.protobuf.types.xydata_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _DifferentColor:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _DifferentColorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_DifferentColor.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    PURPLE: _DifferentColor.ValueType  # 0
    ORANGE: _DifferentColor.ValueType  # 1
    TEAL: _DifferentColor.ValueType  # 2
    BROWN: _DifferentColor.ValueType  # 3

class DifferentColor(_DifferentColor, metaclass=_DifferentColorEnumTypeWrapper): ...

PURPLE: DifferentColor.ValueType  # 0
ORANGE: DifferentColor.ValueType  # 1
TEAL: DifferentColor.ValueType  # 2
BROWN: DifferentColor.ValueType  # 3
global___DifferentColor = DifferentColor

class _Countries:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _CountriesEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Countries.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    AMERICA: _Countries.ValueType  # 0
    TAIWAN: _Countries.ValueType  # 1
    AUSTRALIA: _Countries.ValueType  # 2
    CANADA: _Countries.ValueType  # 3

class Countries(_Countries, metaclass=_CountriesEnumTypeWrapper): ...

AMERICA: Countries.ValueType  # 0
TAIWAN: Countries.ValueType  # 1
AUSTRALIA: Countries.ValueType  # 2
CANADA: Countries.ValueType  # 3
global___Countries = Countries

@typing.final
class MeasurementParameter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FLOAT_DATA_FIELD_NUMBER: builtins.int
    DOUBLE_DATA_FIELD_NUMBER: builtins.int
    INT32_DATA_FIELD_NUMBER: builtins.int
    UINT32_DATA_FIELD_NUMBER: builtins.int
    INT64_DATA_FIELD_NUMBER: builtins.int
    UINT64_DATA_FIELD_NUMBER: builtins.int
    BOOL_DATA_FIELD_NUMBER: builtins.int
    STRING_DATA_FIELD_NUMBER: builtins.int
    DOUBLE_ARRAY_DATA_FIELD_NUMBER: builtins.int
    FLOAT_ARRAY_DATA_FIELD_NUMBER: builtins.int
    INT32_ARRAY_DATA_FIELD_NUMBER: builtins.int
    UINT32_ARRAY_DATA_FIELD_NUMBER: builtins.int
    INT64_ARRAY_DATA_FIELD_NUMBER: builtins.int
    UINT64_ARRAY_DATA_FIELD_NUMBER: builtins.int
    BOOL_ARRAY_DATA_FIELD_NUMBER: builtins.int
    STRING_ARRAY_DATA_FIELD_NUMBER: builtins.int
    ENUM_DATA_FIELD_NUMBER: builtins.int
    ENUM_ARRAY_DATA_FIELD_NUMBER: builtins.int
    INT_ENUM_DATA_FIELD_NUMBER: builtins.int
    INT_ENUM_ARRAY_DATA_FIELD_NUMBER: builtins.int
    XY_DATA_FIELD_NUMBER: builtins.int
    XY_DATA_ARRAY_FIELD_NUMBER: builtins.int
    float_data: builtins.float
    double_data: builtins.float
    int32_data: builtins.int
    uint32_data: builtins.int
    int64_data: builtins.int
    uint64_data: builtins.int
    bool_data: builtins.bool
    string_data: builtins.str
    enum_data: global___DifferentColor.ValueType
    int_enum_data: global___Countries.ValueType
    @property
    def double_array_data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    @property
    def float_array_data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    @property
    def int32_array_data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def uint32_array_data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def int64_array_data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def uint64_array_data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    @property
    def bool_array_data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bool]: ...
    @property
    def string_array_data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def enum_array_data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___DifferentColor.ValueType]: ...
    @property
    def int_enum_array_data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___Countries.ValueType]: ...
    @property
    def xy_data(self) -> ni.protobuf.types.xydata_pb2.DoubleXYData: ...
    @property
    def xy_data_array(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ni.protobuf.types.xydata_pb2.DoubleXYData]: ...
    def __init__(
        self,
        *,
        float_data: builtins.float = ...,
        double_data: builtins.float = ...,
        int32_data: builtins.int = ...,
        uint32_data: builtins.int = ...,
        int64_data: builtins.int = ...,
        uint64_data: builtins.int = ...,
        bool_data: builtins.bool = ...,
        string_data: builtins.str = ...,
        double_array_data: collections.abc.Iterable[builtins.float] | None = ...,
        float_array_data: collections.abc.Iterable[builtins.float] | None = ...,
        int32_array_data: collections.abc.Iterable[builtins.int] | None = ...,
        uint32_array_data: collections.abc.Iterable[builtins.int] | None = ...,
        int64_array_data: collections.abc.Iterable[builtins.int] | None = ...,
        uint64_array_data: collections.abc.Iterable[builtins.int] | None = ...,
        bool_array_data: collections.abc.Iterable[builtins.bool] | None = ...,
        string_array_data: collections.abc.Iterable[builtins.str] | None = ...,
        enum_data: global___DifferentColor.ValueType = ...,
        enum_array_data: collections.abc.Iterable[global___DifferentColor.ValueType] | None = ...,
        int_enum_data: global___Countries.ValueType = ...,
        int_enum_array_data: collections.abc.Iterable[global___Countries.ValueType] | None = ...,
        xy_data: ni.protobuf.types.xydata_pb2.DoubleXYData | None = ...,
        xy_data_array: collections.abc.Iterable[ni.protobuf.types.xydata_pb2.DoubleXYData] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["xy_data", b"xy_data"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["bool_array_data", b"bool_array_data", "bool_data", b"bool_data", "double_array_data", b"double_array_data", "double_data", b"double_data", "enum_array_data", b"enum_array_data", "enum_data", b"enum_data", "float_array_data", b"float_array_data", "float_data", b"float_data", "int32_array_data", b"int32_array_data", "int32_data", b"int32_data", "int64_array_data", b"int64_array_data", "int64_data", b"int64_data", "int_enum_array_data", b"int_enum_array_data", "int_enum_data", b"int_enum_data", "string_array_data", b"string_array_data", "string_data", b"string_data", "uint32_array_data", b"uint32_array_data", "uint32_data", b"uint32_data", "uint64_array_data", b"uint64_array_data", "uint64_data", b"uint64_data", "xy_data", b"xy_data", "xy_data_array", b"xy_data_array"]) -> None: ...

global___MeasurementParameter = MeasurementParameter
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/serialization/test_pb2_grpc.py sha256=fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb bytes=163 -->
## FILE: packages/service/tests/utilities/stubs/serialization/test_pb2_grpc.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/serialization/test_pb2_grpc.py`
- sha256: `fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb`
- bytes: 163

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/serialization/test_pb2_grpc.pyi sha256=f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed bytes=430 -->
## FILE: packages/service/tests/utilities/stubs/serialization/test_pb2_grpc.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/serialization/test_pb2_grpc.pyi`
- sha256: `f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed`
- bytes: 430

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/streamingdata/__init__.py sha256=8a6e3a2b576cdac969160c04316a4243eca71e7f45081275b51001f6c5b432c0 bytes=65 -->
## FILE: packages/service/tests/utilities/stubs/streamingdata/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/streamingdata/__init__.py`
- sha256: `8a6e3a2b576cdac969160c04316a4243eca71e7f45081275b51001f6c5b432c0`
- bytes: 65

````python
"""Auto generated gRPC files for streaming data measurement."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/streamingdata/types.proto sha256=836a470c8c8b64ee82f756f84b1971d2d1cde1cacb18057e9d79667c4f29a84b bytes=372 -->
## FILE: packages/service/tests/utilities/stubs/streamingdata/types.proto

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/streamingdata/types.proto`
- sha256: `836a470c8c8b64ee82f756f84b1971d2d1cde1cacb18057e9d79667c4f29a84b`
- bytes: 372

````protobuf
syntax = "proto3";
package ni.measurementlink.measurement.tests.streamingdata;

message Configurations {
  string name = 1;
  int32 num_responses = 2;
  int32 data_size = 3;
  bool cumulative_data = 4;
  int32 response_interval_in_ms = 5;
  int32 error_on_index = 6;
}

message Outputs {
  string name = 1;
  int32 index = 2;
  repeated int32 data = 3;
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/streamingdata/types_pb2.py sha256=c6eb1c82e329afb8022e40513dcb7363033f50a3891250296c8e68c68a65ccf9 bytes=1507 -->
## FILE: packages/service/tests/utilities/stubs/streamingdata/types_pb2.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/streamingdata/types_pb2.py`
- sha256: `c6eb1c82e329afb8022e40513dcb7363033f50a3891250296c8e68c68a65ccf9`
- bytes: 1507

````python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamingdata/types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19streamingdata/types.proto\x12\x32ni.measurementlink.measurement.tests.streamingdata\"\x9a\x01\n\x0e\x43onfigurations\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rnum_responses\x18\x02 \x01(\x05\x12\x11\n\tdata_size\x18\x03 \x01(\x05\x12\x17\n\x0f\x63umulative_data\x18\x04 \x01(\x08\x12\x1f\n\x17response_interval_in_ms\x18\x05 \x01(\x05\x12\x16\n\x0e\x65rror_on_index\x18\x06 \x01(\x05\"4\n\x07Outputs\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x03 \x03(\x05\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'streamingdata.types_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONFIGURATIONS._serialized_start=82
  _CONFIGURATIONS._serialized_end=236
  _OUTPUTS._serialized_start=238
  _OUTPUTS._serialized_end=290
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/streamingdata/types_pb2.pyi sha256=afecc1caa0bc4cba297d4e188123378d1ea0f250d454fe19c8fdd55de7ff94b3 bytes=2324 -->
## FILE: packages/service/tests/utilities/stubs/streamingdata/types_pb2.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/streamingdata/types_pb2.pyi`
- sha256: `afecc1caa0bc4cba297d4e188123378d1ea0f250d454fe19c8fdd55de7ff94b3`
- bytes: 2324

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Configurations(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    NUM_RESPONSES_FIELD_NUMBER: builtins.int
    DATA_SIZE_FIELD_NUMBER: builtins.int
    CUMULATIVE_DATA_FIELD_NUMBER: builtins.int
    RESPONSE_INTERVAL_IN_MS_FIELD_NUMBER: builtins.int
    ERROR_ON_INDEX_FIELD_NUMBER: builtins.int
    name: builtins.str
    num_responses: builtins.int
    data_size: builtins.int
    cumulative_data: builtins.bool
    response_interval_in_ms: builtins.int
    error_on_index: builtins.int
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        num_responses: builtins.int = ...,
        data_size: builtins.int = ...,
        cumulative_data: builtins.bool = ...,
        response_interval_in_ms: builtins.int = ...,
        error_on_index: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cumulative_data", b"cumulative_data", "data_size", b"data_size", "error_on_index", b"error_on_index", "name", b"name", "num_responses", b"num_responses", "response_interval_in_ms", b"response_interval_in_ms"]) -> None: ...

global___Configurations = Configurations

@typing.final
class Outputs(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    INDEX_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    name: builtins.str
    index: builtins.int
    @property
    def data(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        index: builtins.int = ...,
        data: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["data", b"data", "index", b"index", "name", b"name"]) -> None: ...

global___Outputs = Outputs
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/streamingdata/types_pb2_grpc.py sha256=fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb bytes=163 -->
## FILE: packages/service/tests/utilities/stubs/streamingdata/types_pb2_grpc.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/streamingdata/types_pb2_grpc.py`
- sha256: `fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb`
- bytes: 163

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/streamingdata/types_pb2_grpc.pyi sha256=f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed bytes=430 -->
## FILE: packages/service/tests/utilities/stubs/streamingdata/types_pb2_grpc.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/streamingdata/types_pb2_grpc.pyi`
- sha256: `f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed`
- bytes: 430

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/yieldvsreturn/__init__.py sha256=709e910d68fc49f6bc3b0e1bda407bee3903177d532d08eef748222fa904b9b0 bytes=67 -->
## FILE: packages/service/tests/utilities/stubs/yieldvsreturn/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/yieldvsreturn/__init__.py`
- sha256: `709e910d68fc49f6bc3b0e1bda407bee3903177d532d08eef748222fa904b9b0`
- bytes: 67

````python
"""Auto generated gRPC files for yield vs. return measurement."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/yieldvsreturn/types.proto sha256=65480ec69851d9c70b00a1b047439852010106146f8a82863359dcea6153adbd bytes=275 -->
## FILE: packages/service/tests/utilities/stubs/yieldvsreturn/types.proto

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/yieldvsreturn/types.proto`
- sha256: `65480ec69851d9c70b00a1b047439852010106146f8a82863359dcea6153adbd`
- bytes: 275

````protobuf
syntax = "proto3";
package ni.measurementlink.measurement.tests.yieldvsreturn;

message Configurations {
    double time_in_seconds = 1;
}

message Outputs {
    double elapsed_time_in_seconds = 1;
    repeated double random_numbers = 2;
    string status = 3;
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/yieldvsreturn/types_pb2.py sha256=02dc8da5b6f7831e9def9c0b12a64a5a7db9c461f023edf56c50487a1b261f80 bytes=1303 -->
## FILE: packages/service/tests/utilities/stubs/yieldvsreturn/types_pb2.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/yieldvsreturn/types_pb2.py`
- sha256: `02dc8da5b6f7831e9def9c0b12a64a5a7db9c461f023edf56c50487a1b261f80`
- bytes: 1303

````python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yieldvsreturn/types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19yieldvsreturn/types.proto\x12\x32ni.measurementlink.measurement.tests.yieldvsreturn\")\n\x0e\x43onfigurations\x12\x17\n\x0ftime_in_seconds\x18\x01 \x01(\x01\"R\n\x07Outputs\x12\x1f\n\x17\x65lapsed_time_in_seconds\x18\x01 \x01(\x01\x12\x16\n\x0erandom_numbers\x18\x02 \x03(\x01\x12\x0e\n\x06status\x18\x03 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yieldvsreturn.types_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONFIGURATIONS._serialized_start=81
  _CONFIGURATIONS._serialized_end=122
  _OUTPUTS._serialized_start=124
  _OUTPUTS._serialized_end=206
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/yieldvsreturn/types_pb2.pyi sha256=5bba1acc3430c5b3bec30dce250cca11176990d11ae241f564d104d8199602ed bytes=1704 -->
## FILE: packages/service/tests/utilities/stubs/yieldvsreturn/types_pb2.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/yieldvsreturn/types_pb2.pyi`
- sha256: `5bba1acc3430c5b3bec30dce250cca11176990d11ae241f564d104d8199602ed`
- bytes: 1704

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Configurations(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIME_IN_SECONDS_FIELD_NUMBER: builtins.int
    time_in_seconds: builtins.float
    def __init__(
        self,
        *,
        time_in_seconds: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["time_in_seconds", b"time_in_seconds"]) -> None: ...

global___Configurations = Configurations

@typing.final
class Outputs(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ELAPSED_TIME_IN_SECONDS_FIELD_NUMBER: builtins.int
    RANDOM_NUMBERS_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    elapsed_time_in_seconds: builtins.float
    status: builtins.str
    @property
    def random_numbers(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    def __init__(
        self,
        *,
        elapsed_time_in_seconds: builtins.float = ...,
        random_numbers: collections.abc.Iterable[builtins.float] | None = ...,
        status: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["elapsed_time_in_seconds", b"elapsed_time_in_seconds", "random_numbers", b"random_numbers", "status", b"status"]) -> None: ...

global___Outputs = Outputs
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/yieldvsreturn/types_pb2_grpc.py sha256=fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb bytes=163 -->
## FILE: packages/service/tests/utilities/stubs/yieldvsreturn/types_pb2_grpc.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/yieldvsreturn/types_pb2_grpc.py`
- sha256: `fdb5e84b4db915c5ab5d1d44ff7321e061c1d5132f833f252298adf80c277feb`
- bytes: 163

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/yieldvsreturn/types_pb2_grpc.pyi sha256=f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed bytes=430 -->
## FILE: packages/service/tests/utilities/stubs/yieldvsreturn/types_pb2_grpc.pyi

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/stubs/yieldvsreturn/types_pb2_grpc.pyi`
- sha256: `f74b59d7b8424feb9094545f4d353ed8d55f9dbb750a07bda249e2b05f1f4bed`
- bytes: 430

````python
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tox.ini sha256=5efa29dd5598996723f7d6cdb79fbfb2fec757d508dd6daf9071e176845905d1 bytes=873 -->
## FILE: packages/service/tox.ini

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tox.ini`
- sha256: `5efa29dd5598996723f7d6cdb79fbfb2fec757d508dd6daf9071e176845905d1`
- bytes: 873

````ini
# Tox (http://tox.testrun.org/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox" from this directory.

[tox]
isolated_build = true
envlist = clean, py{310,311,312,313,314}-all-extras, py310-{pb4,pb5,pb6}

[testenv]
skip_install = true
allowlist_externals = poetry
passenv = RUNNER_NAME
commands =
   poetry run python --version
   poetry install -v --all-extras
   pb4: poetry run pip install protobuf==4.25.6
   pb5: poetry run pip install protobuf==5.29.3
   pb6: poetry run pip install protobuf==6.30.0
   poetry run pytest -v --cov=ni_measurement_plugin_sdk_service --cov-append --cov-report= --junitxml=test_results/nims-{env:RUNNER_NAME}-{envname}.xml

[testenv:clean]
commands = poetry run coverage erase
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=README.md sha256=0ba9cb35f0166f05ca9d47d7eceecd0d2be6cab6096390e2a41e6bc1991370f7 bytes=24450 -->
## FILE: README.md

- repository: `ni/measurement-plugin-python`
- source_path: `README.md`
- sha256: `0ba9cb35f0166f05ca9d47d7eceecd0d2be6cab6096390e2a41e6bc1991370f7`
- bytes: 24450

````markdown
# Measurement Plug-In SDK for Python

- [Measurement Plug-In SDK for Python](#measurement-plug-in-sdk-for-python)
  - [Introduction](#introduction)
  - [Dependencies](#dependencies)
  - [Documentation](#documentation)
  - [System Configuration](#system-configuration)
    - [Enable Win32 Long Paths](#enable-win32-long-paths)
  - [Examples](#examples)
  - [Developing Measurements: Quick Start](#developing-measurements-quick-start)
    - [Installation](#installation)
    - [Developing a minimal Python measurement](#developing-a-minimal-python-measurement)
  - [Steps to Run/Debug the Measurement Service](#steps-to-rundebug-the-measurement-service)
  - [Generating Measurement Clients: Quick Start](#generating-measurement-clients-quick-start)
    - [Installation](#installation-1)
    - [Generating a Minimal Python Measurement Client](#generating-a-minimal-python-measurement-client)
  - [Steps to Run/Debug the Measurement Client](#steps-to-rundebug-the-measurement-client)
  - [Static Registration of Python Measurements](#static-registration-of-python-measurements)
    - [Create a batch file that runs a Python measurement](#create-a-batch-file-that-runs-a-python-measurement)
    - [Create Executable for Python Scripts](#create-executable-for-python-scripts)
  - [Troubleshooting](#troubleshooting)
    - ["File not found" or "No such file or directory" errors when copying or running a measurement service](#file-not-found-or-no-such-file-or-directory-errors-when-copying-or-running-a-measurement-service)
  - [Appendix: Managing Measurement with Python](#appendix-managing-measurement-with-python)
    - [Create and Manage Python Measurement using Poetry](#create-and-manage-python-measurement-using-poetry)
    - [Create and Manage Python Measurement using `venv`](#create-and-manage-python-measurement-using-venv)
    - [Create and Manage Python Measurement by directly installing `ni-measurement-plugin-sdk` as a system-level package](#create-and-manage-python-measurement-by-directly-installing-ni-measurement-plugin-sdk-as-a-system-level-package)

---

## Introduction

Measurement Plug-In SDK for Python (`ni-measurement-plugin-sdk`) is a Python
framework that helps you create reusable measurement plug-ins using gRPC
services. Deploy your measurement plug-ins to perform interactive validation in
InstrumentStudio and automated testing in TestStand.

---

## Dependencies

- [Python >= 3.10](https://www.python.org/downloads/release/python-3100/)
- [grpcio >= 1.49.1, < 2.x](https://pypi.org/project/grpcio/1.49.1/)
- [protobuf >= 4.21](https://pypi.org/project/protobuf/4.21.0/)
- [pywin32 >= 303 (Only for Windows)](https://pypi.org/project/pywin32/303/)

---

## Documentation

- [Measurement Plug-In SDK Manual](https://www.ni.com/docs/en-US/bundle/measurementplugins/)
- [API Reference](https://ni.github.io/measurement-plugin-python/)

---

## System Configuration

### Enable Win32 Long Paths

By default, Windows has a path length limit of 260 characters. NI recommends enabling support for long paths when developing and deploying Python measurement services.

There are three ways to do this:
- When installing Python using the Python for Windows installer, click `Disable path length limit` at the end of the installation.
- Set the `Enable Win32 long paths` group policy:
  - Run `gpedit.msc`.
  - Expand `Computer Configuration` » `Administrative Templates` » `All Settings`.
  - Find `Enable Win32 long paths` in the list, double-click it, and set it to `Enabled`.
- In the Windows registry, set `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem\LongPathsEnabled` (type: `REG_DWORD`) to 1. For more details, see [Maximum Path Length Limitation](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation).

---

## Examples

The `examples` directory contains example measurements for use with InstrumentStudio 2026 Q1 or later.

For more information on setting up and running the example measurements, see the included `README.md` file.

For best results, use the example measurements corresponding to the version of InstrumentStudio
that you are using. Newer examples may demonstrate features that are not available in older
versions of InstrumentStudio.

| InstrumentStudio Version | Release | Download |
| ------------------------ | -------- | ------- |
| 2026 Q1                  | [3.1.0](https://github.com/ni/measurement-plugin-python/releases/tag/3.1.0) | [measurement-plugin-python-examples-3.1.0.zip](https://github.com/ni/measurement-plugin-python/releases/download/3.1.0/measurement-plugin-python-examples-3.1.0.zip) |
| 2025 Q4                  | [3.0.1](https://github.com/ni/measurement-plugin-python/releases/tag/3.0.1) | [measurement-plugin-python-examples-3.0.1.zip](https://github.com/ni/measurement-plugin-python/releases/download/3.0.1/measurement-plugin-python-examples-3.0.1.zip) |
| 2025 Q3                  | [2.3.1](https://github.com/ni/measurement-plugin-python/releases/tag/2.3.1) | [measurement-plugin-python-examples-2.3.1.zip](https://github.com/ni/measurement-plugin-python/releases/download/2.3.1/measurement-plugin-python-examples-2.3.1.zip) |
| 2025 Q2                  | [2.3.0](https://github.com/ni/measurement-plugin-python/releases/tag/2.3.0) | [measurement-plugin-python-examples-2.3.0.zip](https://github.com/ni/measurement-plugin-python/releases/download/2.3.0/measurement-plugin-python-examples-2.3.0.zip) |
| 2025 Q1                  | [2.2.0](https://github.com/ni/measurement-plugin-python/releases/tag/2.2.0) | [measurement-plugin-python-examples-2.2.0.zip](https://github.com/ni/measurement-plugin-python/releases/download/2.2.0/measurement-plugin-python-examples-2.2.0.zip) |
| 2024 Q4                  | [2.1.0](https://github.com/ni/measurement-plugin-python/releases/tag/2.1.0) | [measurement-plugin-python-examples-2.1.0.zip](https://github.com/ni/measurement-plugin-python/releases/download/2.1.0/measurement-plugin-python-examples-2.1.0.zip) |
| 2024 Q3                  | [2.0.0](https://github.com/ni/measurement-plugin-python/releases/tag/2.0.0) | [measurement-plugin-python-examples-2.0.0.zip](https://github.com/ni/measurement-plugin-python/releases/download/2.0.0/measurement-plugin-python-examples-2.0.0.zip) |
| 2024 Q2                  | [1.4.0](https://github.com/ni/measurement-plugin-python/releases/tag/1.4.0) | [measurementlink-python-examples-1.4.0.zip](https://github.com/ni/measurement-plugin-python/releases/download/1.4.0/measurementlink-python-examples-1.4.0.zip) |
| Older versions | | See [releases](https://github.com/ni/measurement-plugin-python/releases) page |

---

## Developing Measurements: Quick Start

This section provides instructions to develop custom measurement services in Python using Measurement Plug-In SDK for Python.

### Installation

Make sure the system has the recommended Python version installed. Install Measurement Plug-In SDK for Python using [pip](https://pip.pypa.io/).

``` cmd
REM Activate the required virtual environment if any.
pip install ni-measurement-plugin-sdk
```

Check if you have installed the expected version of Measurement Plug-In SDK for Python installed by running the below command:

```cmd
pip show ni-measurement-plugin-sdk
```

### Developing a minimal Python measurement

1. Run the `ni-measurement-plugin-generator` tool. Use command line arguments to specify the `display-name` and optionally the `version`, `measurement-type`, and `product-type`.

    1. Running `ni-measurement-plugin-generator` without optional arguments:

    `ni-measurement-plugin-generator SampleMeasurement`

    'SampleMeasurement' is the display name of your measurement service. Without the optional arguments,
    the other arguments are generated for you based on the display name.

    2. Running `ni-measurement-plugin-generator` with optional arguments for `measurement-version`, `ui-file`,
    `service-class`, and `description-url`:

    `ni-measurement-plugin-generator SampleMeasurement --measurement-version 0.1.0.0 --ui-file MeasurementUI.measui --service-class SampleMeasurement_Python --description-url https://www.example.com/SampleMeasurement.html`

    3. Running `ni-measurement-plugin-generator` with optional argument for `directory-out`

    `ni-measurement-plugin-generator SampleMeasurement --directory-out <new_path_for_created_files>`

    If no output directory is specified, the files will
    be placed in a new folder under the current directory
    named after the display name without spaces.

2. To customize the created measurement, provide metadata of the measurement's configuration (input parameters) and outputs (output parameters) in `measurement.py`.
    1. Use the `configuration()` decorator to provide metadata about the configurations.**The order of the configuration decorator must match with the order of the parameters defined in the function signature.**

        ``` python
        @foo_measurement_service.register_measurement
        #Display Names can not contains backslash or front slash.
        @foo_measurement_service.configuration("DisplayNameForInput1", DataType.String, "DefaultValueForInput1")
        @foo_measurement_service.configuration("DisplayNameForInput2", DataType.String, "DefaultValueForInput2")
        def measure(input_1, input_2):
            ''' A simple Measurement method'''
            return ["foo", "bar"]
        ```

    2. Use the `output()` decorator to provide metadata about the output.**The order of the output decorators from top to bottom must match the order of the values of the list returned by the function.**

        ``` python
        @foo_measurement_service.register_measurement
        @foo_measurement_service.configuration("DisplayNameForInput1", nims.DataType.String, "DefaultValueForInput1")
        @foo_measurement_service.configuration("DisplayNameForInput2", nims.DataType.String, "DefaultValueForInput2")
        @foo_measurement_service.output("DisplayNameForOutput1", nims.DataType.String)
        @foo_measurement_service.output("DisplayNameForOutput2", nims.DataType.String)
        def measure(input_1, input_2):
            return ["foo", "bar"]
        ```

3. Run/Debug the created measurement by following the steps discussed in the section ["Steps to Run/Debug the Measurement Service".](#steps-to-rundebug-the-measurement-service)

---

## Steps to Run/Debug the Measurement Service

1. Start the discovery service if not already started.

2. (Optional) Activate related virtual environments. Measurement developers can skip this step if they are not using any [virtual environments](#create-and-manage-python-measurement-using-venv) or [poetry-based projects.](#create-and-manage-python-measurement-using-poetry)

    ```cmd
    .venv\scripts\activate
    ```

    - After successful activation, you can see the name of the environment, `(.venv)` is added to the command prompt.
    - If you face an access issue when trying to activate, retry after allowing scripts to run as Administrator by executing the below command in Windows PowerShell:

        ```cmd
        Set-ExecutionPolicy RemoteSigned
        ```

3. [Run](https://code.visualstudio.com/docs/python/python-tutorial#_run-hello-world)/[Debug](https://code.visualstudio.com/docs/python/debugging#_basic-debugging) the measurement Python file.

4. To stop the running measurement service, press `Enter` in the terminal to properly close the service.

5. (Optional) After the usage of measurement, deactivate the virtual environment. Measurement developers can skip this step if they are not using any [virtual environments](#create-and-manage-python-measurement-using-venv) or [poetry-based projects.](#create-and-manage-python-measurement-using-poetry)

    ```cmd
    deactivate
    ```

---

## Generating Measurement Clients: Quick Start

This section provides instructions to generate custom measurement clients in Python using Measurement Plug-In SDK for Python.

### Installation

Install Measurement Plug-In SDK by following the instructions in section ["Measurement Plug-In SDK Installation"](#installation).

### Generating a Minimal Python Measurement Client

Run the `ni-measurement-plugin-client-generator` tool.

1. To create measurement clients for specific measurements, use this command with optional arguments:

    ```ni-measurement-plugin-client-generator --measurement-service-class "ni.examples.SampleMeasurement_Python" [--module-name "sample_measurement_client"]  [--class-name "SampleMeasurementClient"] [--directory-out <new_path_for_created_files>]```

    - `--measurement-service-class` specifies the measurement service class for which the client is being generated.

    - Optional arguments:
        - `--module-name` and `--class-name` define the module and class names of the generated client. If not specified, they are derived from the measurement service class name.

        - `--directory-out` specifies the output directory for the generated files. If not specified, files are placed in the current directory.

    > **Note**: When generating multiple measurement clients, `--module-name` and `--class-name` are ignored and derived from the service class of each measurement. So, ensure that the measurement service class name adheres to proper naming conventions.

2. To create measurement clients for all registered measurements, use this command:

    `ni-measurement-plugin-client-generator --all [--directory-out <new_path_for_created_files>]`

3. To interactively create measurement clients for any registered measurements, use this command:

    `ni-measurement-plugin-client-generator --interactive`

The generated client includes four APIs: `measure`, `stream_measure`, `register_pin_map`, and `cancel`. The usage of these APIs is discussed in the ["Steps to Run/Debug the Measurement Client"](#steps-to-rundebug-the-measurement-client) section.

> **Note**:
> - The Measurement Plug-In Client is compatible with all datatypes supported by the Measurement Plug-In.
> - The Double XY datatype is not supported for measurement configurations (inputs).
> - For Enum datatypes, the generated enum class names will be the measurement parameter name suffixed with 'Enum'. For instance, if the measurement parameter name is 'Enum In', the generated enum in the client will be `EnumInEnum'.
> - Ring control in LabVIEW measurements will be represented as numeric datatypes in the generated client.

---

## Steps to Run/Debug the Measurement Client

1. Make sure the required measurement service is running before interacting with it via the client.

2. Use the client APIs from the ["Generating a Minimal Python Measurement Client"](#generating-a-minimal-python-measurement-client) section.

    1. For non-streaming measurements, use the `measure` method.

        ``` python
        from sample_measurement_client import SampleMeasurementClient
        
        client = SampleMeasurementClient()
        outputs = client.measure()
        print(outputs)
        ```

    2. For streaming measurements, use the `stream_measure` method.

        ``` python
        from sample_measurement_client import SampleMeasurementClient
        
        client = SampleMeasurementClient()
        outputs_itr = client.stream_measure()
        for index, outputs in enumerate(outputs_itr):
            print(f"outputs[{index}] = {outputs}")
        ```

    3. If a measurement requires a pin map, it can be registered using the `register_pin_map` method. By default, `sites` is set to [0].

        ``` python
        from sample_measurement_client import SampleMeasurementClient
        
        client = SampleMeasurementClient()
        client.register_pin_map(pin_map_path)
        outputs = client.measure()
        print(outputs)
        ```
        - Alternatively, when calling a measurement service from another measurement, you can pass the first measurement's pin map context to the second measurement's pin map context through the `pin_map_context` property. Sites can also be provided through the `sites` property.

        ``` python
        from sample_measurement_client import SampleMeasurementClient
        
        client = SampleMeasurementClient()
        client.pin_map_context = available_pin_map_context
        client.sites = [0, 1]
        outputs = client.measure()
        print(outputs)
        ```

    4. Cancel an ongoing `measure` or `stream_measure` call using the `cancel` method.

        ``` python
        from concurrent.futures import ThreadPoolExecutor
        from sample_measurement_client import SampleMeasurementClient
        
        client = SampleMeasurementClient()
        with ThreadPoolExecutor() as executor:
            future = executor.submit(client.measure)
            client.cancel()
            outputs = future.result()  # Raises grpc.RpcException with status code "CANCELLED" 
        ```

---

## Static Registration of Python Measurements

The NI Discovery Service provides a registry of other services, and can discover and activate other services on the system. These features allow the discovery service to distinguish, manage, and describe measurement services on the system.

To statically register a measurement service with the NI Discovery Service, do the following:

1. Create a [startup batch file](#create-a-batch-file-that-runs-a-python-measurement) or [executable](#create-executable-for-python-scripts) for the measurement service.

2. Edit the measurement service's `.serviceconfig` file and set the `path` value to the filename of the startup batch file or executable.

3. Copy the measurement service's directory (including the `.serviceconfig` file and startup batch file) to a subdirectory of `C:\ProgramData\National Instruments\Plug-Ins\Measurements`.
> **Note**
> If you are using a virtual environment, do not copy the `.venv` subdirectory&mdash;the virtual environment must be re-created in the new location.

Once your measurement service is statically registered, the NI Discovery Service makes it visible in supported NI applications.

### Create a batch file that runs a Python measurement

The batch file used for static registration is responsible for starting the Python Scripts.

Typical Batch File:

``` cmd
"<path_to_python_exe>" "<path_to_measurement_file>"
```

Examples to start the fictitious file named `foo_measurement.py`:

1. Using the Python system distribution

    ```cmd
    python foo_measurement.py
    ```

2. Using the virtual environment

    ```cmd
    REM Windows
    .\.venv\Scripts\python.exe foo_measurement.py

    REM Linux
    .venv/bin/python foo_measurement.py
    ```

### Create Executable for Python Scripts

To create an executable from a measurement, you can use the [pyinstaller](https://www.pyinstaller.org/) tooling. If you are using a Poetry project, add `pyinstaller` to its `dev-dependencies`. When statically registering the service, install the EXE into a unique directory along with its .serviceconfig and UI files.

Typical PyInstaller command to build executable:

```cmd
pyinstaller --onefile --console --paths .venv\Lib\site-packages measurement.py
```

## Troubleshooting

### "File not found" or "No such file or directory" errors when copying or running a measurement service

If copying or running a measurement service produces "File not found" or "No such file or directory" errors, make sure to [enable Win32 long paths](#enable-win32-long-paths). If you are unable to enable Win32 long paths, consider deploying the measurement service to a directory with a shorter path.

## Appendix: Managing Measurement with Python

A measurement and its related files can be maintained in different ways in Python. The basic components of any Python measurement are:

1. Measurement Python module (`.py` file)
    - This file contains all the details related to the measurement and also contains the logic for the measurement execution.
    - This file is run to start the measurement as a service.

2. UI File
    - UI file for the measurement. Types of supported UI files are:
        - Measurement UI (`.measui`): created using the **Measurement Plug-In UI Editor** application.
        - LabVIEW UI (`.vi`)
    - The path of this file is configured by `ui_file_path` in `measurement_info` variable definition in measurement Python module (`.py`).

Python communities have different ways of managing Python projects and their dependencies. It is up to the measurement developer to decide how to maintain the project and dependencies. Measurement developers can choose from a few common approaches discussed below based on their requirements.

### Create and Manage Python Measurement using Poetry

1. Install `poetry` (one-time setup)

    1. Make sure the system has the recommended Python version installed.

    2. Install `poetry` using the installation steps given in <https://python-poetry.org/docs/#installation>.

2. Create a new Python project and add `ni-measurement-plugin-sdk` as a dependency to the project.

    1. Open a command prompt, and change the working directory to the directory of your choice where you want to create the project.

        ``` cmd
        cd <path_of_directory_of_your_choice>
        ```

    2. Create a Poetry project using the `poetry new` command. Poetry will create boilerplate files and folders that are commonly needed for a Python project.

        ``` cmd
        poetry new <name_of_the_project>
        ```

    3. Add the `ni-measurement-plugin-sdk` package as a dependency using the [`poetry add`](https://python-poetry.org/docs/cli/#add) command.

        ``` cmd
        cd <name_of_the_project>
        poetry add ni-measurement-plugin-sdk
        ```

    4. The virtual environment will be auto-created by poetry.

    5. Create measurement modules as described in ["Developing a minimal Python measurement"](#developing-a-minimal-python-measurement)
        - Any additional dependencies required by measurement can be added using [add command](https://python-poetry.org/docs/cli/#add).

            ``` cmd
            poetry add <dependency_package_name>
            ```

For detailed info on managing projects using poetry [refer to the official documentation](https://python-poetry.org/docs/cli/).

### Create and Manage Python Measurement using `venv`

1. Make sure the system has the recommended Python version installed.

2. Open a command prompt, and change the working directory to the directory of your choice where you want to create a project.

    ``` cmd
    cd <path_of_directory_of_your_choice>
    ```

3. Create a virtual environment.

    ``` cmd
    REM This creates a virtual environment named .venv
    python -m venv .venv
    ```

4. Activate the virtual environment. After successful activation

    ``` cmd
    .venv\scripts\activate
    REM Optionally upgrade the pip within the venv by executing the command
    python -m pip install -U pip
    ```

5. Install the `ni-measurement-plugin-sdk` package into the virtual environment.

    ``` cmd
    pip install ni-measurement-plugin-sdk
    ```

6. Create measurement modules as described in ["Developing a minimal Python measurement"](#developing-a-minimal-python-measurement)
    - Any additional dependencies required by measurement can be added pip install.

        ``` cmd
        pip install <dependency_package_name>
        ```

For detailed info on managing projects with a virtual environment, refer to the [official documentation](https://docs.python.org/3/tutorial/venv.html).

### Create and Manage Python Measurement by directly installing `ni-measurement-plugin-sdk` as a system-level package

Measurement developers can also install `ni-measurement-plugin-sdk` as a system package if necessary.

1. Install the `ni-measurement-plugin-sdk` package from the command prompt

    ``` cmd
    pip install ni-measurement-plugin-sdk
    ```

2. Create measurement modules as described in ["Developing a minimal Python measurement"](#developing-a-minimal-python-measurement)

---
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=SECURITY.md sha256=902fdb6117cc80678811544ea01d98ec9e3afdde21c15b3940883623f71efb11 bytes=1330 -->
## FILE: SECURITY.md

- repository: `ni/measurement-plugin-python`
- source_path: `SECURITY.md`
- sha256: `902fdb6117cc80678811544ea01d98ec9e3afdde21c15b3940883623f71efb11`
- bytes: 1330

````markdown
<!-- Begin NI SECURITY.md V1.0 -->

# Security

NI views the security of our software products as an important part of our commitment to our users.  This includes source code repositories managed through the [NI](https://github.com/ni) GitHub organization.

## Reporting Security Issues

We encourage you to report security vulnerabilities to us privately so we can follow the principle of [Coordinated Vulnerability Disclosure (CVD)](https://vuls.cert.org/confluence/display/CVD).  This allows us time to thoroughly investigate security issues and publicly disclose them when appropriate.

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them by sending an email to [security@ni.com](mailto:security@ni.com) with sufficient details about the type of issue, the impact of the issue, and how to reproduce the issue.  You may use the [NI PGP key](https://www.ni.com/en/support/security/pgp.html) to encrypt any sensitive communications you send to us. When you notify us of a potential security issue, our remediation process includes acknowledging receipt and coordinating any necessary response activities with you. 

## Learn More

To learn more about NI Security, please see [https://ni.com/security](https://ni.com/security)

<!-- End NI SECURITY.md -->
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=ThirdPartyNotices.txt sha256=48d9d445fe2f5da20e8f4b50e83ebb3314cd17bb03eda3dd38398c46b21e162d bytes=2632 -->
## FILE: ThirdPartyNotices.txt

- repository: `ni/measurement-plugin-python`
- source_path: `ThirdPartyNotices.txt`
- sha256: `48d9d445fe2f5da20e8f4b50e83ebb3314cd17bb03eda3dd38398c46b21e162d`
- bytes: 2632

````text
THIRD-PARTY SOFTWARE NOTICES AND INFORMATION
Do Not Translate or Localize

Measurement Plug-In Support for Python uses third party material from the projects listed below.

****** gRPC (https://github.com/grpc/grpc) ******

Copyright 2014 gRPC authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

****** protobuf (https://github.com/protocolbuffers/protobuf) ******
Copyright 2008 Google Inc.  All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

    * Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above
copyright notice, this list of conditions and the following disclaimer
in the documentation and/or other materials provided with the
distribution.
    * Neither the name of Google Inc. nor the names of its
contributors may be used to endorse or promote products derived from
this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Code generated by the Protocol Buffer compiler is owned by the owner
of the input file used when generating it.  This code is not
standalone and requires a support library to be linked with it.  This
support library is itself covered by the above license.
````
