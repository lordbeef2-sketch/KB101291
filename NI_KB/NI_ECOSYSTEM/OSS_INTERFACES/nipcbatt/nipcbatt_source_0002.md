# NI OSS SOURCE SNAPSHOT: nipcbatt

<!--NI_OSS_SNAPSHOT repo=ni/nipcbatt commit=a26fcd38af55e0286aacff6cdc44bf53b2041111 -->

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/serial_communications/serial_data_types.py sha256=cfe2847373bdb0759cd562747533cee9e743b0bdd4796febba3b3422e29b8548 bytes=10064 -->
## FILE: src/nipcbatt/pcbatt_library/communications/serial_communications/serial_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/communications/serial_communications/serial_data_types.py`
- sha256: `cfe2847373bdb0759cd562747533cee9e743b0bdd4796febba3b3422e29b8548`
- bytes: 10064

````python
""" Serial communication data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (150 > 100 characters) (auto-generated noqa)

import pyvisa.constants
from varname import nameof

from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class SerialCommunicationParameters(PCBATestToolkitData):
    """Defines the parameters used to configure serial device for communications."""

    def __init__(
        self,
        data_rate_bauds: int,
        number_of_bits_in_data_frame: int,
        delay_before_receive_response_milliseconds: int,
        parity: pyvisa.constants.Parity,
        stop_bits: pyvisa.constants.StopBits,
        flow_control: pyvisa.constants.ControlFlow,
    ):
        """Initializes an instance of
        `SerialCommunicationParameters` with specific values.

        Args:
            data_rate_bauds (int):
                The baud rate of the communication.
            number_of_bits_in_data_frame (int):
                The number of data bits contained in each frame
                (4, 5, 6, 7, or 8).
            delay_before_receive_response (int):
                The delay time that occurs after the send of command
                and before the reception of response.
            parity (pyvisa.constants.Parity):
                The `pyvisa.constants.Parity` value representing
                the parity used with every frame transmitted and received.
            stop_bits (pyvisa.constants.StopBits):
                The `pyvisa.constants.StopBits` value representing
                the number of stop bits used to indicate the end of a frame.
            flow_control (pyvisa.constants.ControlFlow):
                The `pyvisa.constants.ControlFlow` value representing
                the flow control mechanism(s) used by the serial communication.

        Raises:
            ValueError:
                Raised when
                `data_rate_bauds` is negative or equal to zero,
                `number_of_bits_in_data_frame` is lower than 4 or greater than 8,
                `delay_before_receive_response_milliseconds` is negative or equal to zero.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_greater_than_zero(data_rate_bauds, nameof(data_rate_bauds))
        Guard.is_within_limits_included(
            number_of_bits_in_data_frame,
            4,
            8,
            nameof(number_of_bits_in_data_frame),
        )
        Guard.is_greater_than_zero(
            delay_before_receive_response_milliseconds,
            nameof(delay_before_receive_response_milliseconds),
        )

        self._data_rate_bauds = data_rate_bauds
        self._number_of_bits_in_data_frame = number_of_bits_in_data_frame
        self._delay_before_receive_response_milliseconds = (
            delay_before_receive_response_milliseconds
        )
        self._parity = parity
        self._stop_bits = stop_bits
        self._flow_control = flow_control

    @property
    def data_rate_bauds(self) -> int:
        """Gets the baud rate of the communication."""
        return self._data_rate_bauds

    @property
    def number_of_bits_in_data_frame(self) -> int:
        """Gets the number of data bits contained in each frame
        (4, 5, 6, 7, or 8)."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (323 > 100 characters) (auto-generated noqa)
        return self._number_of_bits_in_data_frame

    @property
    def delay_before_receive_response_milliseconds(self) -> int:
        """Gets the delay time that occurs after the send of command
        and before the reception of response."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (341 > 100 characters) (auto-generated noqa)
        return self._delay_before_receive_response_milliseconds

    @property
    def parity(self) -> pyvisa.constants.Parity:
        """Gets the `pyvisa.constants.Parity` value representing
        the parity used with every frame transmitted and received."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (362 > 100 characters) (auto-generated noqa)
        return self._parity

    @property
    def stop_bits(self) -> pyvisa.constants.StopBits:
        """Gets the `pyvisa.constants.StopBits` value representing
        the number of stop bits used to indicate the end of a frame."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (364 > 100 characters) (auto-generated noqa)
        return self._stop_bits

    @property
    def flow_control(self) -> pyvisa.constants.ControlFlow:
        """Gets the `pyvisa.constants.ControlFlow` value representing
        the flow control mechanism(s) used by the serial communication."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (367 > 100 characters) (auto-generated noqa)
        return self._flow_control


class SerialCommunicationConfiguration(PCBATestToolkitData):
    """Defines parameters used for configuration of the serial communication."""

    def __init__(
        self,
        communication_parameters: SerialCommunicationParameters,
        command_to_send: str,
    ):
        """Initializes an instance of
        `SerialCommunicationConfiguration` with specific values.

        Args:
            communication_parameters (SerialCommunicationParameters):
                An instance of `SerialCommunicationParameters`
                that represents the parameters used for settings of serial communication.
            command_to_send (str):
                The string representing the command to send.

        Raises:
            ValueError:
                Raised when
                `communication_parameters` is None,
                `command_to_send` is None or empty or whitespace.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(communication_parameters, nameof(communication_parameters))
        Guard.is_not_none_nor_empty_nor_whitespace(command_to_send, nameof(command_to_send))

        self._communication_parameters = communication_parameters
        self._command_to_send = command_to_send

    @property
    def communication_parameters(self) -> SerialCommunicationParameters:
        """Gets the instance of `SerialCommunicationParameters`
        that represents the parameters used for settings of serial communication."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (377 > 100 characters) (auto-generated noqa)
        return self._communication_parameters

    @property
    def command_to_send(self) -> str:
        """Gets the string representing the command to send."""
        return self._command_to_send


class SerialCommunicationData(PCBATestToolkitData):
    """Defines data obtained after serial communication on serial device."""

    def __init__(self, received_response: str):
        """Initializes an instance of
        `SerialCommunicationData` with specific values.

        Args:
            received_response (str):
                The received response after serial communication.

        Raises:
            ValueError:
                Raised when
                `received_response` is None or empty or whitespace.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_not_none_nor_empty_nor_whitespace(received_response, nameof(received_response))

        self._received_response = received_response

    @property
    def received_response(self) -> str:
        """Gets the received response after serial communication."""
        return self._received_response
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/spi_communications/__init__.py sha256=51c28ea6c7864428809600da8e926a55dbf1d855a7b47ceecd924c853b7ab664 bytes=240 -->
## FILE: src/nipcbatt/pcbatt_library/communications/spi_communications/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/communications/spi_communications/__init__.py`
- sha256: `51c28ea6c7864428809600da8e926a55dbf1d855a7b47ceecd924c853b7ab664`
- bytes: 240

````python
"""Provides nipcbatt library SPI communication modules"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (168 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/spi_communications/spi_communication_constants.py sha256=0baf5c7a967bfc77a7cdcd1e3a19c85ef685b2ed135dba403e96622a322c4cbd bytes=3844 -->
## FILE: src/nipcbatt/pcbatt_library/communications/spi_communications/spi_communication_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/communications/spi_communications/spi_communication_constants.py`
- sha256: `0baf5c7a967bfc77a7cdcd1e3a19c85ef685b2ed135dba403e96622a322c4cbd`
- bytes: 3844

````python
""" Constants data types for SPI communications."""

import dataclasses

import numpy

from nipcbatt.pcbatt_communication_library.ni_845x_data_types import (
    DataMemoryAddressEndianness,
    DataMemoryAddressType,
    Ni845xVoltageLevel,
    SpiConfigurationClockPhase,
    SpiConfigurationClockPolarity,
)
from nipcbatt.pcbatt_library.communications.common.communication_data_types import (
    MemoryAddressParameters,
)
from nipcbatt.pcbatt_library.communications.spi_communications.spi_data_types import (
    SpiCommunicationParameters,
    SpiDeviceParameters,
)
from nipcbatt.pcbatt_library.communications.spi_communications.spi_read_data_types import (
    SpiReadCommunicationConfiguration,
    SpiReadParameters,
)
from nipcbatt.pcbatt_library.communications.spi_communications.spi_write_data_types import (
    SpiWriteCommunicationConfiguration,
    SpiWriteParameters,
)


@dataclasses.dataclass
class ConstantsForSpiCommunication:
    """Constants used for SPI communication."""

    DEFAULT_VOLTAGE_LEVEL = Ni845xVoltageLevel.VOLTAGE_LEVEL_33
    DEFAULT_CHIP_SELECT = 0
    DEFAULT_CLOCK_RATE_KILOHERTZ = 100
    DEFAULT_CLOCK_PHASE = SpiConfigurationClockPhase.CLOCK_PHASE_FIRST_EDGE
    DEFAULT_CLOCK_POLARITY = SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW
    DEFAULT_NUMBER_OF_BYTES_TO_READ = 128
    DEFAULT_MEMORY_ADDRESS = 0
    DEFAULT_MEMORY_ADDRESS_TYPE = DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE
    DEFAULT_MEMORY_ADDRESS_ENDIANNESS = DataMemoryAddressEndianness.BIG_ENDIAN
    DEFAULT_NUMBER_OF_BYTES_PER_PAGE = 128
    DEFAULT_DELAY_BETWEEN_PAGE_WRITE_OPERATIONS_MILLISECONDS = 5


DEFAULT_SPI_DEVICE_PARAMETERS = SpiDeviceParameters(
    voltage_level=ConstantsForSpiCommunication.DEFAULT_VOLTAGE_LEVEL,
)

DEFAULT_SPI_COMMUNICATION_PARAMETERS = SpiCommunicationParameters(
    chip_select=ConstantsForSpiCommunication.DEFAULT_CHIP_SELECT,
    clock_rate_kilohertz=ConstantsForSpiCommunication.DEFAULT_CLOCK_RATE_KILOHERTZ,
    clock_phase=ConstantsForSpiCommunication.DEFAULT_CLOCK_PHASE,
    clock_polarity=ConstantsForSpiCommunication.DEFAULT_CLOCK_POLARITY,
)

DEFAULT_SPI_READ_PARAMETERS = SpiReadParameters(
    number_of_bytes_to_read=ConstantsForSpiCommunication.DEFAULT_NUMBER_OF_BYTES_TO_READ,
    memory_address_parameters=MemoryAddressParameters(
        memory_address=ConstantsForSpiCommunication.DEFAULT_MEMORY_ADDRESS,
        address_type=ConstantsForSpiCommunication.DEFAULT_MEMORY_ADDRESS_TYPE,
        address_endianness=ConstantsForSpiCommunication.DEFAULT_MEMORY_ADDRESS_ENDIANNESS,
    ),
)

DEFAULT_SPI_WRITE_PARAMETERS = SpiWriteParameters(
    number_of_bytes_per_page=ConstantsForSpiCommunication.DEFAULT_NUMBER_OF_BYTES_PER_PAGE,
    delay_between_page_write_operations_milliseconds=(
        ConstantsForSpiCommunication.DEFAULT_DELAY_BETWEEN_PAGE_WRITE_OPERATIONS_MILLISECONDS
    ),
    data_to_be_written=numpy.zeros(shape=1, dtype=numpy.ubyte),
    memory_address_parameters=MemoryAddressParameters(
        memory_address=ConstantsForSpiCommunication.DEFAULT_MEMORY_ADDRESS,
        address_type=ConstantsForSpiCommunication.DEFAULT_MEMORY_ADDRESS_TYPE,
        address_endianness=ConstantsForSpiCommunication.DEFAULT_MEMORY_ADDRESS_ENDIANNESS,
    ),
)

DEFAULT_SPI_READ_COMMUNICATION_CONFIGURATION = SpiReadCommunicationConfiguration(
    device_parameters=DEFAULT_SPI_DEVICE_PARAMETERS,
    communication_parameters=DEFAULT_SPI_COMMUNICATION_PARAMETERS,
    read_parameters=DEFAULT_SPI_READ_PARAMETERS,
)

DEFAULT_SPI_WRITE_COMMUNICATION_CONFIGURATION = SpiWriteCommunicationConfiguration(
    device_parameters=DEFAULT_SPI_DEVICE_PARAMETERS,
    communication_parameters=DEFAULT_SPI_COMMUNICATION_PARAMETERS,
    write_parameters=DEFAULT_SPI_WRITE_PARAMETERS,
)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/spi_communications/spi_data_types.py sha256=36a26a7f2fd640d60615d73f0dda95c377c89f97b371323ea09176a6969d4ca4 bytes=4907 -->
## FILE: src/nipcbatt/pcbatt_library/communications/spi_communications/spi_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/communications/spi_communications/spi_data_types.py`
- sha256: `36a26a7f2fd640d60615d73f0dda95c377c89f97b371323ea09176a6969d4ca4`
- bytes: 4907

````python
""" SPI communication data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (147 > 100 characters) (auto-generated noqa)

from varname import nameof

from nipcbatt.pcbatt_communication_library.ni_845x_data_types import (
    Ni845xVoltageLevel,
    SpiConfigurationClockPhase,
    SpiConfigurationClockPolarity,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class SpiDeviceParameters(PCBATestToolkitData):
    """Defines the parameters used to configure SPI device for communications."""

    def __init__(self, voltage_level: Ni845xVoltageLevel):
        """Initializes an instance of
        `SpiDeviceParameters` with specific values.

        Args:
            voltage_level (Ni845xVoltageLevel):
                The `Ni845xVoltageLevel` value
                representing the voltage level of signal
                sent or received during SPI communications.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._voltage_level = voltage_level

    @property
    def voltage_level(self) -> Ni845xVoltageLevel:
        """Gets the `Ni845xVoltageLevel` value."""
        return self._voltage_level


class SpiCommunicationParameters(PCBATestToolkitData):
    """Defines the parameters used to configure SPI communications."""

    def __init__(
        self,
        chip_select: int,
        clock_rate_kilohertz: int,
        clock_phase: SpiConfigurationClockPhase,
        clock_polarity: SpiConfigurationClockPolarity,
    ):
        """Initializes an instance of
        `SpiCommunicationParameters` with specific values.

        Args:
            chip_select (int):
                The chip select value for SPI configuration.
            clock_rate_kilohertz (int):
                The clock rate to apply to the device communication, in kilohertz.
            clock_phase (SpiConfigurationClockPhase):
                The SpiConfigurationClockPhase value representing
                the clock phase value for SPI configuration.
            clock_polarity (SpiConfigurationClockPolarity):
                The SpiConfigurationClockPolarity value representing
                the clock polarity value for SPI configuration.

        Raises:
            ValueError:
                Raised when
                `chip_select` is negative,
                `clock_rate_kilohertz` is negative or equal to zero,
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_greater_than_zero(clock_rate_kilohertz, nameof(clock_rate_kilohertz))

        self._chip_select = chip_select
        self._clock_rate_kilohertz = clock_rate_kilohertz
        self._clock_phase = clock_phase
        self._clock_polarity = clock_polarity

    @property
    def chip_select(self) -> int:
        """Gets the chip select value for SPI configuration."""
        return self._chip_select

    @property
    def clock_rate_kilohertz(self) -> int:
        """Gets the clock rate to apply to the device communication."""
        return self._clock_rate_kilohertz

    @property
    def clock_phase(self) -> SpiConfigurationClockPhase:
        """Gets the SpiConfigurationClockPhase value representing
        the clock phase value for SPI configuration."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (348 > 100 characters) (auto-generated noqa)
        return self._clock_phase

    @property
    def clock_polarity(self) -> SpiConfigurationClockPolarity:
        """Gets the SpiConfigurationClockPhase value representing
        the clock polarity value for SPI configuration."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (351 > 100 characters) (auto-generated noqa)
        return self._clock_polarity
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/spi_communications/spi_read_communication.py sha256=15e2250da02c775ebaae3c160dfa4bab5378fa28aff0d398d54e7362625e786d bytes=4749 -->
## FILE: src/nipcbatt/pcbatt_library/communications/spi_communications/spi_read_communication.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/communications/spi_communications/spi_read_communication.py`
- sha256: `15e2250da02c775ebaae3c160dfa4bab5378fa28aff0d398d54e7362625e786d`
- bytes: 4749

````python
""" Defines class used for SPI read communication on PCB points. """

from nipcbatt.pcbatt_library.communications.common.communication_functions import (
    create_command_for_spi_read_communication,
)
from nipcbatt.pcbatt_library.communications.spi_communications.spi_data_types import (
    SpiCommunicationParameters,
    SpiDeviceParameters,
)
from nipcbatt.pcbatt_library.communications.spi_communications.spi_read_data_types import (
    SpiReadCommunicationConfiguration,
    SpiReadCommunicationData,
    SpiReadParameters,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import (
    BuildingBlockUsingNi845xSpiDevice,
)


class SpiReadCommunication(BuildingBlockUsingNi845xSpiDevice):
    """Defines a way that allows you to perform a read operation from SPI device."""

    def initialize(self, device_name: str):
        """Initializes the communication with the specific NI 845x device.

        Args:
            device_name (str): The name of a communication device.
        """
        if self.is_devices_handler_initialized:
            return

        self.devices_handler.open(device_name=device_name)

    def close(self):
        """Closes communication procedure and releases internal resources."""
        if not self.is_devices_handler_initialized:
            return

        self.devices_handler.close()

    def configure_and_read_data(
        self,
        configuration: SpiReadCommunicationConfiguration,
    ) -> SpiReadCommunicationData:
        """Configures and performs read operation according to specific configuration parameters.

        Args:
            configuration (SpiReadCommunicationConfiguration):
                An instance of `SpiReadCommunicationConfiguration`,
                encapsulating parameters used to configure communication.

        Returns:
            SpiReadCommunicationData:
                An instance of `SpiReadCommunicationData`, encapsulating the data bytes read.
        """
        # Configuration of the device for SPI communications.
        self.configure_device_for_spi_communications(parameters=configuration.device_parameters)

        # Configuration of SPI communication.
        self.configure_spi_communication(parameters=configuration.communication_parameters)

        # Read of data bytes from SPI device.
        return self.read_data(parameters=configuration.read_parameters)

    def configure_device_for_spi_communications(self, parameters: SpiDeviceParameters) -> None:
        """Configures the device for SPI communications.

        Args:
            parameters (SpiDeviceParameters):
                A `SpiDeviceParameters` object used to configure the device for SPI communications.
        """
        self.devices_handler.set_input_output_voltage_level(voltage_level=parameters.voltage_level)

    def configure_spi_communication(self, parameters: SpiCommunicationParameters) -> None:
        """Configures the SPI communication.

        Args:
            parameters (SpiCommunicationParameters):
                A `SpiCommunicationParameters` object used to configure SPI communications.
        """
        self.devices_handler.configuration.chip_select = parameters.chip_select
        self.devices_handler.configuration.clock_rate_kilohertz = parameters.clock_rate_kilohertz
        self.devices_handler.configuration.clock_phase = parameters.clock_phase
        self.devices_handler.configuration.clock_polarity = parameters.clock_polarity

    def read_data(self, parameters: SpiReadParameters) -> SpiReadCommunicationData:
        """Reads data bytes from an SPI device.

        Args:
            parameters (SpiReadParameters):
                A `SpiReadParameters` object used
                to perform read operations on Spi device.

        Returns:
            SpiReadCommunicationData:
                An instance of `SpiReadCommunicationData`, encapsulating the data bytes read.
        """
        data_to_be_written = create_command_for_spi_read_communication(
            address_parameters=parameters.memory_address_parameters,
            number_of_bytes_to_read=parameters.number_of_bytes_to_read,
        )
        data_bytes_read = self.devices_handler.write_and_read_data(
            data_bytes_to_be_written=data_to_be_written,
            number_of_bytes_to_read=parameters.number_of_bytes_to_read,
        )

        if data_bytes_read.size > parameters.number_of_bytes_to_read:
            data_bytes_read.resize(
                new_shape=(data_bytes_read.size - parameters.number_of_bytes_to_read)
            )

        return SpiReadCommunicationData(data_bytes_read=data_bytes_read)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/spi_communications/spi_read_data_types.py sha256=9b3abd465fcf8117d90148037d6321971638497434f29147466f514334b2bb01 bytes=8621 -->
## FILE: src/nipcbatt/pcbatt_library/communications/spi_communications/spi_read_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/communications/spi_communications/spi_read_data_types.py`
- sha256: `9b3abd465fcf8117d90148037d6321971638497434f29147466f514334b2bb01`
- bytes: 8621

````python
""" SPI communication data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (147 > 100 characters) (auto-generated noqa)

import numpy
from varname import nameof

from nipcbatt.pcbatt_library.communications.common.communication_data_types import (
    MemoryAddressParameters,
)
from nipcbatt.pcbatt_library.communications.spi_communications.spi_data_types import (
    SpiCommunicationParameters,
    SpiDeviceParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class SpiReadParameters(PCBATestToolkitData):
    """Defines the settings used to perform read operations on SPI device."""

    def __init__(
        self,
        number_of_bytes_to_read: int,
        memory_address_parameters: MemoryAddressParameters,
    ):
        """Initializes an instance of
        `SpiReadParameters` with specific values.

        Args:
            number_of_bytes_to_read (int):
                The number of bytes to read.
            memory_address_parameters (MemoryAddressParameters):
                An instance of `MemoryAddressParameters` that specifies
                the format of memory address.

        Raises:
            ValueError:
                Raised when
                `number_of_bytes_per_page` is negative or equal to zero,
                `memory_address_parameters` is None.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_greater_than_zero(number_of_bytes_to_read, nameof(number_of_bytes_to_read))
        Guard.is_not_none(memory_address_parameters, nameof(memory_address_parameters))

        self._number_of_bytes_to_read = number_of_bytes_to_read
        self._memory_address_parameters = memory_address_parameters

    @property
    def number_of_bytes_to_read(self) -> int:
        """Gets the number of bytes to read."""
        return self._number_of_bytes_to_read

    @property
    def memory_address_parameters(self) -> MemoryAddressParameters:
        """Gets an instance of `MemoryAddressParameters` that specifies
        the format of memory address."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (333 > 100 characters) (auto-generated noqa)
        return self._memory_address_parameters


class SpiReadCommunicationConfiguration(PCBATestToolkitData):
    """Defines parameters used for configuration of the SPI Read communication."""

    def __init__(
        self,
        device_parameters: SpiDeviceParameters,
        communication_parameters: SpiCommunicationParameters,
        read_parameters: SpiReadParameters,
    ):
        """Initializes an instance of
        `SpiReadCommunicationConfiguration` with specific values.

        Args:
            device_parameters (SpiDeviceParameters):
                An instance of `SpiDeviceParameters` that represents
                the parameters used for settings of SPI device for communications.
            communication_parameters (SpiCommunicationParameters):
                An instance of `SPICommunicationParameters` that represents
                the parameters used for settings of SPI communication.
            read_parameters (SpiReadParameters):
                An instance of `SpiReadParameters` that represents
                the parameters used for settings of SPI Read communication.

        Raises:
            ValueError:
                Raised when
                `device_parameters` is None,
                `communication_parameters` is None,
                `communication_read_parameters` is None.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(device_parameters, nameof(device_parameters))
        Guard.is_not_none(communication_parameters, nameof(communication_parameters))
        Guard.is_not_none(read_parameters, nameof(read_parameters))

        self._device_parameters = device_parameters
        self._communication_parameters = communication_parameters
        self._read_parameters = read_parameters

    @property
    def device_parameters(self) -> SpiDeviceParameters:
        """Gets an instance of `SpiDeviceParameters` that represents
        the parameters used for settings of SPI device for communications."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (370 > 100 characters) (auto-generated noqa)
        return self._device_parameters

    @property
    def communication_parameters(self) -> SpiCommunicationParameters:
        """Gets an instance of `SpiCommunicationParameters` that represents
        the parameters used for settings of SPI communication."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (358 > 100 characters) (auto-generated noqa)
        return self._communication_parameters

    @property
    def read_parameters(self) -> SpiReadParameters:
        """Gets an instance of `SpiReadParameters` that represents
        the parameters used for settings of SPI Read communication."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (363 > 100 characters) (auto-generated noqa)
        return self._read_parameters


class SpiReadCommunicationData(PCBATestToolkitData):
    """Defines data obtained after SPI read communication on SPI device."""

    def __init__(self, data_bytes_read: numpy.ndarray[numpy.ubyte]):
        """Initializes an instance of
        `SpiReadCommunicationData` with specific values.

        Args:
            data_bytes_read (numpy.ndarray):
                The array of data bytes read from SPI Device.

        Raises:
            ValueError:
                Raised when `data_bytes_read` is None or empty,
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(data_bytes_read, nameof(data_bytes_read))
        Guard.is_not_empty(data_bytes_read, nameof(data_bytes_read))

        self._data_bytes_read = data_bytes_read

    def __eq__(self, value_to_compare: object) -> bool:
        """instances equality.

        Args:
            value_to_compare (object): the instance of `SpiReadCommunicationData` to compare.

        Returns:
            bool: True if equals to `value_to_compare`.
        """  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        if isinstance(value_to_compare, self.__class__):
            return numpy.allclose(self._data_bytes_read, value_to_compare._data_bytes_read)

        return False

    @property
    def data_bytes_read(self) -> numpy.ndarray[numpy.ubyte]:
        """Gets the array of data bytes read from SPI Device."""
        return self._data_bytes_read
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/spi_communications/spi_write_communication.py sha256=6845fe9261f20fed82964223f9192ed50fd684f43cebcb1c48faed0172dafe21 bytes=6234 -->
## FILE: src/nipcbatt/pcbatt_library/communications/spi_communications/spi_write_communication.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/communications/spi_communications/spi_write_communication.py`
- sha256: `6845fe9261f20fed82964223f9192ed50fd684f43cebcb1c48faed0172dafe21`
- bytes: 6234

````python
""" Defines class used for SPI write communication on PCB points. """

import time

import numpy

from nipcbatt.pcbatt_library.communications.common.communication_data_types import (
    MemoryAddressParameters,
)
from nipcbatt.pcbatt_library.communications.common.communication_functions import (
    compute_pages_characteristics,
    create_command_for_spi_write_communication,
)
from nipcbatt.pcbatt_library.communications.spi_communications.spi_data_types import (
    SpiCommunicationParameters,
    SpiDeviceParameters,
)
from nipcbatt.pcbatt_library.communications.spi_communications.spi_write_data_types import (
    SpiWriteCommunicationConfiguration,
    SpiWriteParameters,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import (
    BuildingBlockUsingNi845xSpiDevice,
)


class SpiWriteCommunication(BuildingBlockUsingNi845xSpiDevice):
    """Defines a way that allows you to perform a write operation to SPI device,"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (194 > 100 characters) (auto-generated noqa)

    def initialize(self, device_name: str):
        """Initializes the communication with the specific NI 845x device.

        Args:
            device_name (str): The name of a communication device.
        """
        if self.is_devices_handler_initialized:
            return

        self.devices_handler.open(device_name=device_name)

    def close(self):
        """Closes communication procedure and releases internal resources."""
        if not self.is_devices_handler_initialized:
            return

        self.devices_handler.close()

    def configure_and_write_data(self, configuration: SpiWriteCommunicationConfiguration) -> None:
        """Defines class used for SPI write communication on PCB points.

        Args:
            configuration (SpiWriteCommunicationConfiguration):
                An instance of `SpiWriteCommunicationConfiguration`,
                encapsulating parameters used to configure communication.
        """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

        # Configuration of the device for SPI communications.
        self.configure_device_for_spi_communications(parameters=configuration.device_parameters)

        # Configuration of SPI communication.
        self.configure_spi_communication(parameters=configuration.communication_parameters)

        # Write of data bytes to SPI device.
        self.write_data(parameters=configuration.write_parameters)

    def configure_device_for_spi_communications(self, parameters: SpiDeviceParameters) -> None:
        """Configures the device for SPI communications.

        Args:
            parameters (SpiDeviceParameters):
                A `SpiDeviceParameters` object used to configure the device for SPI communications.
        """
        self.devices_handler.set_input_output_voltage_level(parameters.voltage_level)

    def configure_spi_communication(self, parameters: SpiCommunicationParameters) -> None:
        """Configures the SPI communication.

        Args:
            parameters (SpiCommunicationParameters):
                A `SpiCommunicationParameters` object used to configure SPI communications.
        """
        self.devices_handler.configuration.chip_select = parameters.chip_select
        self.devices_handler.configuration.clock_rate_kilohertz = parameters.clock_rate_kilohertz
        self.devices_handler.configuration.clock_phase = parameters.clock_phase
        self.devices_handler.configuration.clock_polarity = parameters.clock_polarity

    def write_data(self, parameters: SpiWriteParameters) -> None:
        """Reads data bytes from an SPI device.

        Args:
            parameters (SpiWriteParameters):
                A `SpiWriteParameters` object used
                to perform read operations on SPI device.
        """
        pages_characteristics = compute_pages_characteristics(
            data_memory_start_address=parameters.memory_address_parameters.memory_address,
            number_of_bytes_to_write=parameters.data_to_be_written.size,
            number_of_bytes_per_page=parameters.number_of_bytes_per_page,
        )

        for page_characteristics in pages_characteristics:
            # Compute the address of the page as a data bytes collection.
            address_parameters = MemoryAddressParameters(
                memory_address=page_characteristics.data_memory_address,
                address_type=parameters.memory_address_parameters.address_type,
                address_endianness=parameters.memory_address_parameters.address_endianness,
            )

            data_to_be_written = create_command_for_spi_write_communication(
                address_parameters=address_parameters,
                number_of_bytes_to_write=page_characteristics.number_of_bytes_in_page,
            )

            # After the address where data will be stored, append the data bytes themselves.
            source_start_index = page_characteristics.index_in_data_bytes_array
            source_end_index = source_start_index + page_characteristics.number_of_bytes_in_page
            destination_start_index = (
                numpy.dtype(numpy.ubyte).itemsize + address_parameters.address_type.value
            )
            destination_end_index = (
                destination_start_index + page_characteristics.number_of_bytes_in_page
            )

            # Copy the data bytes of page to buffer
            numpy.put(
                data_to_be_written,
                range(destination_start_index, destination_end_index),
                parameters.data_to_be_written[source_start_index:source_end_index],
            )

            # Write the data.
            self.devices_handler.write_and_read_data(
                data_bytes_to_be_written=data_to_be_written,
                number_of_bytes_to_read=data_to_be_written.size,
            )

            time.sleep(parameters.delay_between_page_write_operations_milliseconds / 1000.0)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/communications/spi_communications/spi_write_data_types.py sha256=34228d6e0661920c313bb60e82a93f095aeb70c3c404255b1994c07154194c63 bytes=9723 -->
## FILE: src/nipcbatt/pcbatt_library/communications/spi_communications/spi_write_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/communications/spi_communications/spi_write_data_types.py`
- sha256: `34228d6e0661920c313bb60e82a93f095aeb70c3c404255b1994c07154194c63`
- bytes: 9723

````python
""" SPI communication data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (147 > 100 characters) (auto-generated noqa)

import numpy
from varname import nameof

from nipcbatt.pcbatt_library.communications.common.communication_data_types import (
    MemoryAddressParameters,
)
from nipcbatt.pcbatt_library.communications.spi_communications.spi_read_data_types import (
    SpiCommunicationParameters,
    SpiDeviceParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_library_core.pcbatt_library_messages import (
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class SpiWriteParameters(PCBATestToolkitData):
    """Defines the settings used to perform write operations on SPI device."""

    def __init__(
        self,
        number_of_bytes_per_page: int,
        delay_between_page_write_operations_milliseconds: int,
        data_to_be_written: numpy.ndarray[numpy.ubyte],
        memory_address_parameters: MemoryAddressParameters,
    ):
        """Initializes an instance of
        `SpiWriteParameters` with specific values.

        Args:
            number_of_bytes_per_page (int):
                The number of bytes per page.
            delay_between_page_write_operations_milliseconds (int):
                The delay time between two page write operations, in ms.
            data_to_be_written (numpy.ndarray[numpy.ubyte]):
                A numpy array containing the data to be written to SPI device.
            memory_address_parameters (MemoryAddressParameters):
                An instance of `MemoryAddressParameters` that specifies
                the format of memory address.

        Raises:
            TypeError:
                raised if the type of numpy array is not `numpy.ubyte`.
            ValueError:
                Raised when
                `number_of_bytes_per_page` is negative or equal to zero,
                `delay_between_page_write_operations_milliseconds` is negative,
                `memory_address_parameters` is None.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_greater_than_zero(number_of_bytes_per_page, nameof(number_of_bytes_per_page))
        Guard.is_greater_than_or_equal_to_zero(
            delay_between_page_write_operations_milliseconds,
            nameof(delay_between_page_write_operations_milliseconds),
        )
        Guard.is_not_none(memory_address_parameters, nameof(memory_address_parameters))
        Guard.is_not_none(data_to_be_written, nameof(data_to_be_written))
        Guard.is_not_empty(data_to_be_written, nameof(data_to_be_written))

        if data_to_be_written.dtype != numpy.ubyte:
            raise TypeError(
                PCBATTLibraryExceptionMessages.INVALID_NUMPY_ARRAY_TYPE_ARGS_1.format(numpy.ubyte)
            )

        self._number_of_bytes_per_page = number_of_bytes_per_page
        self._delay_between_page_write_operations_milliseconds = (
            delay_between_page_write_operations_milliseconds
        )
        self._data_to_be_written = data_to_be_written
        self._memory_address_parameters = memory_address_parameters

    def __eq__(self, value_to_compare: object) -> bool:
        """instances equality.

        Args:
            value_to_compare (object): the instance of `SpiWriteParameters` to compare.

        Returns:
            bool: True if equals to `value_to_compare`.
        """  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        if isinstance(value_to_compare, self.__class__):
            return (
                self._number_of_bytes_per_page == value_to_compare._number_of_bytes_per_page
                or self._delay_between_page_write_operations_milliseconds
                == value_to_compare._delay_between_page_write_operations_milliseconds
                or numpy.array_equal(self._data_to_be_written, value_to_compare._data_to_be_written)
                or self._memory_address_parameters == value_to_compare._memory_address_parameters
            )

        return False

    @property
    def number_of_bytes_per_page(self) -> int:
        """Gets the number of bytes per page."""
        return self._number_of_bytes_per_page

    @property
    def delay_between_page_write_operations_milliseconds(self) -> int:
        """Gets the delay time between two page write operations, in ms."""
        return self._delay_between_page_write_operations_milliseconds

    @property
    def data_to_be_written(self) -> numpy.ndarray[numpy.ubyte]:
        """Gets the numpy array containing the data to be written to SPI device."""
        return self._data_to_be_written

    @property
    def memory_address_parameters(self) -> MemoryAddressParameters:
        """Gets an instance of `MemoryAddressParameters` that specifies
        the format of memory address."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (333 > 100 characters) (auto-generated noqa)
        return self._memory_address_parameters


class SpiWriteCommunicationConfiguration(PCBATestToolkitData):
    """Defines parameters used for configuration of the SPI Write communication."""

    def __init__(
        self,
        device_parameters: SpiDeviceParameters,
        communication_parameters: SpiCommunicationParameters,
        write_parameters: SpiWriteParameters,
    ):
        """Initializes an instance of
        `SpiWriteCommunicationConfiguration` with specific values.

        Args:
            device_parameters (SpiDeviceParameters):
                An instance of `SpiDeviceParameters` that represents
                the parameters used for settings of SPI device for communications.
            communication_parameters (SpiCommunicationParameters):
                An instance of `SpiCommunicationParameters` that represents
                the parameters used for settings of SPI communication.
            write_parameters (SpiWriteParameters):
                An instance of `SpiWriteParameters` that represents
                the parameters used for settings of SPI Write communication.

        Raises:
            ValueError:
                Raised when
                `device_parameters` is None,
                `communication_parameters` is None,
                `write_parameters` is None.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(device_parameters, nameof(device_parameters))
        Guard.is_not_none(communication_parameters, nameof(communication_parameters))
        Guard.is_not_none(write_parameters, nameof(write_parameters))

        self._device_parameters = device_parameters
        self._communication_parameters = communication_parameters
        self._write_parameters = write_parameters

    @property
    def device_parameters(self) -> SpiDeviceParameters:
        """Gets an instance of `SpiDeviceParameters` that represents
        the parameters used for settings of SPI device for communications."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (370 > 100 characters) (auto-generated noqa)
        return self._device_parameters

    @property
    def communication_parameters(self) -> SpiCommunicationParameters:
        """Gets an instance of `SpiCommunicationParameters` that represents
        the parameters used for settings of SPI communication."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (358 > 100 characters) (auto-generated noqa)
        return self._communication_parameters

    @property
    def write_parameters(self) -> SpiWriteParameters:
        """Gets an instance of `SpiWriteParameters` that represents
        the parameters used for settings of SPI Write communication."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (364 > 100 characters) (auto-generated noqa)
        return self._write_parameters
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/__init__.py sha256=33e0a42634c507e9076a454b6ddee3c35edf6b324a4f0bd7982bec5dd63325ae bytes=13555 -->
## FILE: src/nipcbatt/pcbatt_library/daq/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/__init__.py`
- sha256: `33e0a42634c507e9076a454b6ddee3c35edf6b324a4f0bd7982bec5dd63325ae`
- bytes: 13555

````python
#pylint: disable=C0301

"""Provides nipcbatt library of measurement, generation and modules uaing DAQ hardware"""  
from nipcbatt.pcbatt_library.daq.dc_rms_current_measurements.dc_rms_current_constants import (
    DEFAULT_DC_RMS_CURRENT_DIGITAL_START_TRIGGER_PARAMETERS,
    DEFAULT_DC_RMS_CURRENT_MEASUREMENT_CONFIGURATION,
    DEFAULT_DC_RMS_CURRENT_MEASUREMENT_OPTIONS,
    DEFAULT_DC_RMS_CURRENT_MEASUREMENT_TERMINAL_RANGE_PARAMETERS,
    DEFAULT_DC_RMS_CURRENT_SAMPLE_CLOCK_TIMING_PARAMETERS,
    ConstantsForDcRmsCurrentMeasurement,
)

from nipcbatt.pcbatt_library.daq.dc_rms_current_measurements.dc_rms_current_data_types import (
    DcRmsCurrentMeasurementChannelAndTerminalRangeParameters,
    DcRmsCurrentMeasurementConfiguration,
    DcRmsCurrentMeasurementResultData,
    DcRmsCurrentMeasurementTerminalRangeParameters,
)
from nipcbatt.pcbatt_library.daq.dc_rms_current_measurements.dc_rms_current_measurement import (
    DcRmsCurrentMeasurement,
)
from nipcbatt.pcbatt_library.daq.dc_rms_voltage_measurements.dc_rms_voltage_constants import (
    DEFAULT_DC_RMS_VOLTAGE_DIGITAL_START_TRIGGER_PARAMETERS,
    DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION,
    DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_OPTIONS,
    DEFAULT_DC_RMS_VOLTAGE_RANGE_AND_TERMINAL_PARAMETERS,
    DEFAULT_DC_RMS_VOLTAGE_SAMPLE_CLOCK_TIMING_PARAMETERS,
    ConstantsForDcRmsVoltageMeasurement,
)

from nipcbatt.pcbatt_library.daq.common.voltage_constants import (
    ConstantsForVoltageMeasurement
)

from nipcbatt.pcbatt_library.daq.common.voltage_data_types import (
    VoltageGenerationChannelParameters,
    VoltageMeasurementChannelAndTerminalRangeParameters,
    VoltageRangeAndTerminalParameters,
)
from nipcbatt.pcbatt_library.daq.dc_rms_voltage_measurements.dc_rms_voltage_data_types import (
    DcRmsVoltageMeasurementConfiguration,
    DcRmsVoltageMeasurementResultData,
)
from nipcbatt.pcbatt_library.daq.dc_rms_voltage_measurements.dc_rms_voltage_measurement import (
    DcRmsVoltageMeasurement,
)
from nipcbatt.pcbatt_library.daq.dc_voltage_generations.dc_voltage_data_types import (
    DcVoltageGenerationConfiguration,
)
from nipcbatt.pcbatt_library.daq.dc_voltage_generations.dc_voltage_generation import (
    DcVoltageGeneration,
)
from nipcbatt.pcbatt_library.daq.dc_voltage_generations.dc_voltage_generation_constants import (
    DEFAULT_DC_VOLTAGE_GENERATION_CONFIGURATION,
    DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS,
    ConstantsForDcVoltageGeneration,
)
from nipcbatt.pcbatt_library.daq.digital_clock_generations.digital_clock_constants import (
    ConstantsForDigitalClockGeneration,
)
from nipcbatt.pcbatt_library.daq.digital_clock_generations.digital_clock_data_types import (
    DigitalClockGenerationConfiguration,
    DigitalClockGenerationCounterChannelParameters,
    DigitalClockGenerationData,
    DigitalClockGenerationTimingParameters,
)
from nipcbatt.pcbatt_library.daq.digital_clock_generations.digital_clock_generation import (
    DigitalClockGeneration,
)
from nipcbatt.pcbatt_library.daq.digital_edge_count_measurements.digital_edge_count_constants import (
    ConstantsForDigitalEdgeCountMeasurement,
)
from nipcbatt.pcbatt_library.daq.digital_edge_count_measurements.digital_edge_count_data_types import (
    DigitalEdgeCountHardwareTimerConfiguration,
    DigitalEdgeCountMeasurementCounterChannelParameters,
    DigitalEdgeCountMeasurementResultData,
    DigitalEdgeCountMeasurementTimingParameters,
    DigitalEdgeCountSoftwareTimerConfiguration,
)
from nipcbatt.pcbatt_library.daq.digital_edge_count_measurements.digital_edge_count_measurement_using_hardware_timer import (
    DigitalEdgeCountMeasurementUsingHardwareTimer,
)
from nipcbatt.pcbatt_library.daq.digital_edge_count_measurements.digital_edge_count_measurement_using_software_timer import (
    DigitalEdgeCountMeasurementUsingSoftwareTimer,
)
from nipcbatt.pcbatt_library.daq.digital_frequency_measurements.digital_frequency_constants import (
    ConstantsForDigitalFrequencyMeasurement,
)
from nipcbatt.pcbatt_library.daq.digital_frequency_measurements.digital_frequency_data_types import (
    DigitalFrequencyMeasurementConfiguration,
    DigitalFrequencyMeasurementCounterChannelParameters,
    DigitalFrequencyMeasurementResultData,
    DigitalFrequencyRangeParameters,
)
from nipcbatt.pcbatt_library.daq.digital_frequency_measurements.digital_frequency_measurement import (
    DigitalFrequencyMeasurement,
)
from nipcbatt.pcbatt_library.daq.digital_pulse_generations.digital_pulse_constants import (
    ConstantsForDigitalPulseGeneration,
)
from nipcbatt.pcbatt_library.daq.digital_pulse_generations.digital_pulse_data_types import (
    DigitalPulseGenerationConfiguration,
    DigitalPulseGenerationCounterChannelParameters,
    DigitalPulseGenerationData,
    DigitalPulseGenerationTimingParameters,
)
from nipcbatt.pcbatt_library.daq.digital_pulse_generations.digital_pulse_generation import (
    DigitalPulseGeneration,
)
from nipcbatt.pcbatt_library.daq.digital_pwm_measurements.digital_pwm_constants import (
    ConstantsForDigitalPwmMeasurement,
)
from nipcbatt.pcbatt_library.daq.digital_pwm_measurements.digital_pwm_data_types import (
    DigitalPwmMeasurementConfiguration,
    DigitalPwmMeasurementCounterChannelParameters,
    DigitalPwmMeasurementData,
    DigitalPwmMeasurementRangeParameters,
    DigitalPwmMeasurementResultData,
    DigitalPwmMeasurementTimingParameters,
)
from nipcbatt.pcbatt_library.daq.digital_pwm_measurements.digital_pwm_measurement import (
    DigitalPwmMeasurement,
)
from nipcbatt.pcbatt_library.daq.dynamic_digital_pattern_generations.dynamic_digital_pattern_constants import (
    ConstantsForDynamicDigitalPatternGeneration,
)
from nipcbatt.pcbatt_library.daq.dynamic_digital_pattern_generations.dynamic_digital_pattern_data_types import (
    DynamicDigitalPatternGenerationConfiguration,
    DynamicDigitalPatternGenerationData,
    DynamicDigitalStartTriggerParameters,
)
from nipcbatt.pcbatt_library.daq.dynamic_digital_pattern_generations.dynamic_digital_pattern_generation import (
    DynamicDigitalPatternGeneration,
)
from nipcbatt.pcbatt_library.daq.dynamic_digital_pattern_measurements.dynamic_digital_pattern_constants import (
    ConstantsForDynamicDigitalPatternMeasurement,
)
from nipcbatt.pcbatt_library.daq.dynamic_digital_pattern_measurements.dynamic_digital_pattern_data_types import (
    DynamicDigitalPatternMeasurementConfiguration,
    DynamicDigitalPatternMeasurementResultData,
)
from nipcbatt.pcbatt_library.daq.dynamic_digital_pattern_measurements.dynamic_digital_pattern_measurement import (
    DynamicDigitalPatternMeasurement,
)
from nipcbatt.pcbatt_library.daq.frequency_domain_measurements.frequency_domain_constants import (
    DEFAULT_FREQUENCY_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS,
    DEFAULT_FREQUENCY_DOMAIN_MEASUREMENT_CONFIGURATION,
    DEFAULT_FREQUENCY_DOMAIN_MEASUREMENT_OPTIONS,
    DEFAULT_FREQUENCY_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS,
    DEFAULT_FREQUENCY_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS,
    ConstantsForFrequencyDomainMeasurement,
)
from nipcbatt.pcbatt_library.daq.frequency_domain_measurements.frequency_domain_data_types import (
    FrequencyDomainMeasurementConfiguration,
    FrequencyDomainMeasurementResultData,
    MultipleTonesMeasurementResultData,
)
from nipcbatt.pcbatt_library.daq.frequency_domain_measurements.frequency_domain_measurement import (
    FrequencyDomainMeasurement,
)

from nipcbatt.pcbatt_library.daq.power_supply_source_and_measurements.power_supply_source_and_measure import (
    PowerSupplySourceAndMeasure,
)
from nipcbatt.pcbatt_library.daq.power_supply_source_and_measurements.power_supply_source_constants import (
    DEFAULT_POWER_SUPPLY_DIGITAL_START_TRIGGER_PARAMETERS,
    DEFAULT_POWER_SUPPLY_MEASUREMENT_OPTIONS,
    DEFAULT_POWER_SUPPLY_SAMPLE_CLOCK_TIMING_PARAMETERS,
    DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_CONFIGURATION,
    DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_TERMINAL_PARAMETERS,
    ConstantsForPowerSupplySourceMeasurement,
)
from nipcbatt.pcbatt_library.daq.power_supply_source_and_measurements.power_supply_source_data_types import (
    PowerSupplySourceAndMeasureConfiguration,
    PowerSupplySourceAndMeasureData,
    PowerSupplySourceAndMeasureResultData,
    PowerSupplySourceAndMeasureTerminalParameters,
)

from nipcbatt.pcbatt_library.daq.signal_voltage_generations.signal_voltage_data_types import (
    SignalVoltageGenerationMultipleTonesConfiguration,
    SignalVoltageGenerationMultipleTonesWaveParameters,
    SignalVoltageGenerationSineWaveConfiguration,
    SignalVoltageGenerationSineWaveParameters,
    SignalVoltageGenerationSquareWaveConfiguration,
    SignalVoltageGenerationSquareWaveParameters,
    SignalVoltageGenerationTimingParameters,
    ToneParameters,
)
from nipcbatt.pcbatt_library.daq.signal_voltage_generations.signal_voltage_generation import (
    SignalVoltageGeneration,
)
from nipcbatt.pcbatt_library.daq.signal_voltage_generations.signal_voltage_generation_constants import (
    DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
    DEFAULT_MULTI_TONE_GENERATION_CONFIGURATION,
    DEFAULT_MULTI_TONE_GENERATION_PARAMETERS,
    DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_CONFIGURATION,
    DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_PARAMETERS,
    DEFAULT_SIGNAL_VOLTAGE_GENERATION_SQUARE_WAVE_PARAMETERS,
    DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
    DEFAULT_SQUARE_WAVE_GENERATION_CONFIGURATION,
    DEFAULT_TONE_PARAMETERS,
    DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS,
    ConstantsForSignalVoltageGeneration,
)

from nipcbatt.pcbatt_library.daq.static_digital_state_generations.static_digital_state_data_types import (
    StaticDigitalStateGenerationConfiguration,
    StaticDigitalStateGenerationData,
)
from nipcbatt.pcbatt_library.daq.static_digital_state_generations.static_digital_state_generation import (
    StaticDigitalStateGeneration,
)
from nipcbatt.pcbatt_library.daq.static_digital_state_measurements.static_digital_state_data_types import (
    StaticDigitalStateMeasurementResultData,
)
from nipcbatt.pcbatt_library.daq.static_digital_state_measurements.static_digital_state_measurement import (
    StaticDigitalStateMeasurement,
)
from nipcbatt.pcbatt_library.daq.synchronizations.synchronization_signal_routing import (
    SynchronizationSignalRouting,
)
from nipcbatt.pcbatt_library.daq.temperature_measurements.temperature_constants import (
    DEFAULT_BETA_OEFFICIENT_AND_SENSOR_RESISTANCE_PARAMETERS,
    DEFAULT_COEFFICIENTS_STEINHART_HART_PARAMETERS,
    DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS,
    DEFAULT_TEMPERATURE_RTD_MEASUREMENT_CONFIGURATION,
    DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS,
    DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS,
    DEFAULT_TEMPERATURE_THERMISTOR_MEASUREMENT_CONFIGURATION,
    DEFAULT_TEMPERATURE_THERMISTOR_RANGE_AND_TERMINAL_PARAMETERS,
    DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_CONFIGURATION,
    DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS,
    ConstantsForTemperatureMeasurement,
    ConstantsForTemperatureMeasurementUsingRtd,
    ConstantsForTemperatureMeasurementUsingThermistor,
    ConstantsForTemperatureMeasurementUsingThermocouple,
)
from nipcbatt.pcbatt_library.daq.temperature_measurements.temperature_data_types import (
    BetaCoefficientAndSensorResistanceParameters,
    CoefficientsSteinhartHartParameters,
    SteinhartHartEquationOption,
    TemperatureMeasurementResultData,
    TemperatureRtdMeasurementChannelParameters,
    TemperatureRtdMeasurementConfiguration,
    TemperatureRtdMeasurementTerminalParameters,
    TemperatureThermistorChannelRangeAndTerminalParameters,
    TemperatureThermistorMeasurementConfiguration,
    TemperatureThermistorRangeAndTerminalParameters,
    TemperatureThermocoupleChannelRangeAndTerminalParameters,
    TemperatureThermocoupleMeasurementConfiguration,
    TemperatureThermocoupleMeasurementTerminalParameters,
    TemperatureThermocoupleRangeAndTerminalParameters,
)
from nipcbatt.pcbatt_library.daq.temperature_measurements.temperature_measurement import (
    TemperatureMeasurement,
)
from nipcbatt.pcbatt_library.daq.temperature_measurements.temperature_measurement_using_rtd import (
    TemperatureMeasurementUsingRtd,
)
from nipcbatt.pcbatt_library.daq.temperature_measurements.temperature_measurement_using_thermistor import (
    TemperatureMeasurementUsingThermistor,
)
from nipcbatt.pcbatt_library.daq.temperature_measurements.temperature_measurement_using_thermocouple import (
    TemperatureMeasurementUsingThermocouple,
)
from nipcbatt.pcbatt_library.daq.time_domain_measurements.time_domain_constants import (
    DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS,
    DEFAULT_TIME_DOMAIN_MEASUREMENT_CONFIGURATION,
    DEFAULT_TIME_DOMAIN_MEASUREMENT_OPTIONS,
    DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS,
    DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS,
    ConstantsForTimeDomainMeasurement,
)
from nipcbatt.pcbatt_library.daq.time_domain_measurements.time_domain_data_types import (
    TimeDomainMeasurementConfiguration,
    TimeDomainMeasurementResultData,
)
from nipcbatt.pcbatt_library.daq.time_domain_measurements.time_domain_measurement import (
    TimeDomainMeasurement,
)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/common/__init__.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: src/nipcbatt/pcbatt_library/daq/common/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/common/__init__.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/common/voltage_constants.py sha256=cad937b9276189f15ddb408f329511937f0656edc90fc0d828a728506c5a92a6 bytes=1541 -->
## FILE: src/nipcbatt/pcbatt_library/daq/common/voltage_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/common/voltage_constants.py`
- sha256: `cad937b9276189f15ddb408f329511937f0656edc90fc0d828a728506c5a92a6`
- bytes: 1541

````python
""" Constants data types for Voltage Measurements."""

import nidaqmx.constants

from nipcbatt.pcbatt_library.common.common_data_types import (
    MeasurementAnalysisRequirement,
    MeasurementExecutionType,
    SampleTimingEngine,
    StartTriggerType,
)


class ConstantsForVoltageMeasurement:
    """Constants used for Voltage measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)

    INITIAL_AI_TERMINAL_CONFIGURATION = nidaqmx.constants.TerminalConfiguration.DEFAULT
    INITIAL_VOLTAGE_MINIMUM_VALUE_VOLTS = -10.0
    INITIAL_VOLTAGE_MAXIMUM_VALUE_VOLTS = 10.0
    INITIAL_AI_VOLTAGE_UNITS = nidaqmx.constants.VoltageUnits.VOLTS

    DEFAULT_AI_TERMINAL_CONFIGURATION = nidaqmx.constants.TerminalConfiguration.RSE
    DEFAULT_VOLTAGE_MINIMUM_VALUE_VOLTS = -10.0
    DEFAULT_VOLTAGE_MAXIMUM_VALUE_VOLTS = 10.0

    DEFAULT_EXECUTION_TYPE = MeasurementExecutionType.CONFIGURE_AND_MEASURE
    DEFAULT_MEASUREMENT_ANALYSIS_REQUIREMENT = MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS

    DEFAULT_SAMPLE_CLOCK_SOURCE = "OnboardClock"
    DEFAULT_SAMPLING_RATE_HERTZ = 10000
    DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL = 1000
    DEFAULT_SAMPLE_TIMING_ENGINE = SampleTimingEngine.AUTO

    DEFAULT_TRIGGER_TYPE = StartTriggerType.NO_TRIGGER
    DEFAULT_DIGITAL_START_TRIGGER_SOURCE = ""
    DEFAULT_DIGITAL_START_TRIGGER_EDGE = nidaqmx.constants.Edge.RISING
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/common/voltage_data_types.py sha256=bcc4dabe5f77c86386bd0ea2874d8b6cc0886eff882e326f9eb83a2f810b7eda bytes=7588 -->
## FILE: src/nipcbatt/pcbatt_library/daq/common/voltage_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/common/voltage_data_types.py`
- sha256: `bcc4dabe5f77c86386bd0ea2874d8b6cc0886eff882e326f9eb83a2f810b7eda`
- bytes: 7588

````python
"""Defines datatypes that are common to DC-RMS Voltage,
   Frequency Domain and Time Domain Measurements."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (345 > 100 characters) (auto-generated noqa)

import nidaqmx.constants
from varname import nameof

from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class VoltageRangeAndTerminalParameters(PCBATestToolkitData):
    """Defines the parameters used to configure terminal
    of all channels for DC-RMS Voltage measurement."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (347 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        terminal_configuration: nidaqmx.constants.TerminalConfiguration,
        range_min_volts: float,
        range_max_volts: float,
    ) -> None:
        """Initializes an instance of `VoltageRangeAndTerminalParameters` with specific values.

        Args:
            terminal_configuration (nidaqmx.constants.TerminalConfiguration):
                The input terminal configuration parameter.
            range_min_volts (float):
                The minimum value expected for the measurement on the channel.
            range_max_volts (float):
                The maximum value expected for the measurement on the channel.
        """
        self._terminal_configuration = terminal_configuration
        self._range_min_volts = range_min_volts
        self._range_max_volts = range_max_volts

    @property
    def terminal_configuration(self) -> nidaqmx.constants.TerminalConfiguration:
        """
        :class:`nidaqmx.constants.TerminalConfiguration`:
            Gets the input terminal configuration parameter.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._terminal_configuration

    @property
    def range_min_volts(self) -> float:
        """
        :type:`float`: Gets the minimum value expected for the measurement on the channel.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        return self._range_min_volts

    @property
    def range_max_volts(self) -> float:
        """
        :type:`float`: Gets the maximum value expected for the measurement on the channel.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        return self._range_max_volts


class VoltageMeasurementChannelAndTerminalRangeParameters(PCBATestToolkitData):
    """Defines the parameters used to configure channels for DC-RMS Voltage measurement."""

    def __init__(
        self,
        channel_name: str,
        channel_parameters: VoltageRangeAndTerminalParameters,
    ) -> None:
        """Initializes an instance of `VoltageMeasurementChannelAndTerminalRangeParameters`
           with specific values.

        Args:
            channel_name (str):
                The name of the channel to configure.
            channel_parameters (VoltageRangeAndTerminalParameters):
                An instance of `VoltageRangeAndTerminalParameters` that specifies
                the parameters used to configure the channel.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._channel_name = channel_name
        self._channel_parameters = channel_parameters

    @property
    def channel_name(self) -> str:
        """
        :type:`str`: Gets the name of the channel to configure.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        return self._channel_name

    @property
    def channel_parameters(self) -> VoltageRangeAndTerminalParameters:
        """
        :class:`VoltageRangeAndTerminalParameters`:
            Gets an instance of `VoltageRangeAndTerminalParameters` that specifies
            the parameters used to configure the channel.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._channel_parameters


class VoltageGenerationChannelParameters(PCBATestToolkitData):
    """Defines the parameters used to configure terminal of all channels for Voltage Generation"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (209 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        range_min_volts: float,
        range_max_volts: float,
    ) -> None:
        """Initializes an instance of `VoltageGenerationChannelParameters` with specific values.

        Args:
            range_min_volts (float):
                Specifies the minimum voltage you expect to generate.
            range_max_volts (float):
                Specifies the maximum voltage you expect to generate.

        Raises:
            ValueError:
                Raised when `range_min_volts' is greater than or equal to `range_max_volts`.
        """
        Guard.is_less_than(range_min_volts, range_max_volts, nameof(range_min_volts))

        self._range_min_volts = range_min_volts
        self._range_max_volts = range_max_volts

    @property
    def range_min_volts(self) -> float:
        """
        :type:`float`: Gets the minimum voltage you expect to generate on the channels.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        return self._range_min_volts

    @property
    def range_max_volts(self) -> float:
        """
        :type:`float`: Gets the maximum voltage you expect to generate on the channels.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        return self._range_max_volts
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dc_rms_current_measurements/__init__.py sha256=61f6c9589b3cf5588c33237a8d6462e591b068b4b578ebe0aacaa4d36bb215c0 bytes=249 -->
## FILE: src/nipcbatt/pcbatt_library/daq/dc_rms_current_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/dc_rms_current_measurements/__init__.py`
- sha256: `61f6c9589b3cf5588c33237a8d6462e591b068b4b578ebe0aacaa4d36bb215c0`
- bytes: 249

````python
"""Provides nipcbatt library DC-RMS current measurement modules"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (177 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dc_rms_current_measurements/dc_rms_current_constants.py sha256=7f4607ef140803b955c6268788ccd3fe33d6f2cd1b4e0880da2e02f74f3930cc bytes=4404 -->
## FILE: src/nipcbatt/pcbatt_library/daq/dc_rms_current_measurements/dc_rms_current_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/dc_rms_current_measurements/dc_rms_current_constants.py`
- sha256: `7f4607ef140803b955c6268788ccd3fe33d6f2cd1b4e0880da2e02f74f3930cc`
- bytes: 4404

````python
""" Constants data types for DC-RMS Current  Measurements."""

import dataclasses

import nidaqmx.constants

from nipcbatt.pcbatt_analysis.waveform_analysis.dc_rms_analysis import (
    DcRmsProcessingWindow,
)
from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
    MeasurementAnalysisRequirement,
    MeasurementExecutionType,
    MeasurementOptions,
    SampleClockTimingParameters,
    SampleTimingEngine,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.daq.dc_rms_current_measurements.dc_rms_current_data_types import (
    DcRmsCurrentMeasurementConfiguration,
    DcRmsCurrentMeasurementTerminalRangeParameters,
)


@dataclasses.dataclass
class ConstantsForDcRmsCurrentMeasurement:
    """Constants used for Current measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)

    INITIAL_AI_TERMINAL_CONFIGURATION = nidaqmx.constants.TerminalConfiguration.DEFAULT
    INITIAL_CURRENT_RANGE_MINIMUM_AMPERES = -0.01
    INITIAL_CURRENT_RANGE_MAXIMUM_AMPERES = 0.01
    INITIAL_AI_CURRENT_UNITS = nidaqmx.constants.CurrentUnits.AMPS
    INITIAL_SHUNT_RESISTOR_LOCATION = nidaqmx.constants.CurrentShuntResistorLocation.EXTERNAL
    INITIAL_EXTERNAL_SHUNT_RESISTOR_VALUE_OHMS = 0.001

    DEFAULT_AI_TERMINAL_CONFIGURATION = nidaqmx.constants.TerminalConfiguration.RSE
    DEFAULT_CURRENT_RANGE_MINIMUM_AMPERES = -0.01
    DEFAULT_CURRENT_RANGE_MAXIMUM_AMPERES = 0.01
    DEFAULT_EXTERNAL_SHUNT_RESISTOR_VALUE_OHMS = 0.001

    DEFAULT_EXECUTION_TYPE = MeasurementExecutionType.CONFIGURE_AND_MEASURE
    DEFAULT_MEASUREMENT_ANALYSIS_REQUIREMENT = MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS

    DEFAULT_SAMPLE_CLOCK_SOURCE = "OnboardClock"
    DEFAULT_SAMPLING_RATE_HERTZ = 10000
    DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL = 1000
    DEFAULT_SAMPLE_TIMING_ENGINE = SampleTimingEngine.AUTO

    DEFAULT_TRIGGER_TYPE = StartTriggerType.NO_TRIGGER
    DEFAULT_DIGITAL_START_TRIGGER_SOURCE = ""
    DEFAULT_DIGITAL_START_TRIGGER_EDGE = nidaqmx.constants.Edge.RISING
    DEFAULT_DC_RMS_PROCESSING_WINDOW = DcRmsProcessingWindow.HANN


DEFAULT_DC_RMS_CURRENT_MEASUREMENT_TERMINAL_RANGE_PARAMETERS = DcRmsCurrentMeasurementTerminalRangeParameters(
    terminal_configuration=ConstantsForDcRmsCurrentMeasurement.DEFAULT_AI_TERMINAL_CONFIGURATION,
    range_min_amperes=ConstantsForDcRmsCurrentMeasurement.DEFAULT_CURRENT_RANGE_MINIMUM_AMPERES,
    range_max_amperes=ConstantsForDcRmsCurrentMeasurement.DEFAULT_CURRENT_RANGE_MAXIMUM_AMPERES,
    shunt_resistor_ohms=ConstantsForDcRmsCurrentMeasurement.DEFAULT_EXTERNAL_SHUNT_RESISTOR_VALUE_OHMS,
)

DEFAULT_DC_RMS_CURRENT_MEASUREMENT_OPTIONS = MeasurementOptions(
    execution_option=ConstantsForDcRmsCurrentMeasurement.DEFAULT_EXECUTION_TYPE,
    measurement_analysis_requirement=ConstantsForDcRmsCurrentMeasurement.DEFAULT_MEASUREMENT_ANALYSIS_REQUIREMENT,
)

DEFAULT_DC_RMS_CURRENT_SAMPLE_CLOCK_TIMING_PARAMETERS = SampleClockTimingParameters(
    sample_clock_source=ConstantsForDcRmsCurrentMeasurement.DEFAULT_SAMPLE_CLOCK_SOURCE,
    sampling_rate_hertz=ConstantsForDcRmsCurrentMeasurement.DEFAULT_SAMPLING_RATE_HERTZ,
    number_of_samples_per_channel=ConstantsForDcRmsCurrentMeasurement.DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL,
    sample_timing_engine=ConstantsForDcRmsCurrentMeasurement.DEFAULT_SAMPLE_TIMING_ENGINE,
)

DEFAULT_DC_RMS_CURRENT_DIGITAL_START_TRIGGER_PARAMETERS = DigitalStartTriggerParameters(
    trigger_select=ConstantsForDcRmsCurrentMeasurement.DEFAULT_TRIGGER_TYPE,
    digital_start_trigger_source=ConstantsForDcRmsCurrentMeasurement.DEFAULT_DIGITAL_START_TRIGGER_SOURCE,
    digital_start_trigger_edge=ConstantsForDcRmsCurrentMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE,
)

DEFAULT_DC_RMS_CURRENT_MEASUREMENT_CONFIGURATION = DcRmsCurrentMeasurementConfiguration(
    global_channel_parameters=DEFAULT_DC_RMS_CURRENT_MEASUREMENT_TERMINAL_RANGE_PARAMETERS,
    specific_channels_parameters=[],
    measurement_options=DEFAULT_DC_RMS_CURRENT_MEASUREMENT_OPTIONS,
    sample_clock_timing_parameters=DEFAULT_DC_RMS_CURRENT_SAMPLE_CLOCK_TIMING_PARAMETERS,
    digital_start_trigger_parameters=DEFAULT_DC_RMS_CURRENT_DIGITAL_START_TRIGGER_PARAMETERS,
)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dc_rms_current_measurements/dc_rms_current_data_types.py sha256=344299f4c8052823402090e26909dd0ea54a69f52cd9b6d36848c701ccce7926 bytes=20048 -->
## FILE: src/nipcbatt/pcbatt_library/daq/dc_rms_current_measurements/dc_rms_current_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/dc_rms_current_measurements/dc_rms_current_data_types.py`
- sha256: `344299f4c8052823402090e26909dd0ea54a69f52cd9b6d36848c701ccce7926`
- bytes: 20048

````python
""" DC-RMS current data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (144 > 100 characters) (auto-generated noqa)

from typing import List

import nidaqmx.constants
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    AnalogWaveform,
    DigitalStartTriggerParameters,
    MeasurementOptions,
    SampleClockTimingParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DcRmsCurrentMeasurementTerminalRangeParameters(PCBATestToolkitData):
    """Defines the parameters used to configure terminal of all channels for DC-RMS Current measurement"""  # noqa: W505, D415 - doc line too long (106 > 100 characters) (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)

    # The minimum value of shunt resitor value that Daqmx allows is 100e-9
    MINIMUM_ALLOWED_SHUNT_RESISTOR_VALUE_OHMS = 100e-9

    def __init__(
        self,
        terminal_configuration: nidaqmx.constants.TerminalConfiguration,
        range_min_amperes: float,
        range_max_amperes: float,
        shunt_resistor_ohms: float,
    ) -> None:
        """Initializes an instance of `DcRmsCurrentMeasurementTerminalRangeParameters` with specific values.

        Args:
            terminal_configuration (nidaqmx.constants.TerminalConfiguration):
                The settings of the terminal for all the current channels.
            range_min_amperes (float):
                The minimum current value im amperes expected for the measurement on the channel.
            range_max_amperes (float):
                The maximum current value in amperes expected for the measurement on the channel.
            shunt_resistor_ohms (float):
                The value in ohms of the external shunt resistor.

        Raises:
            ValueError when,
                    the value of `terminal_configuration` is set to None,
                    when `range_min_amperes` is greater or equal to `range_max_amperes`,
                    when `shunt_resistor_ohms` value is less than 'MINIMUM_ALLOWED_SHUNT_RESISTOR_VALUE_OHMS'.
        """  # noqa: W505 - doc line too long (108 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(terminal_configuration, nameof(terminal_configuration))
        Guard.is_greater_than(
            value=range_max_amperes,
            expected_smaller_value=range_min_amperes,
            value_name=nameof(range_max_amperes),
        )
        Guard.is_greater_than_or_equal_to(
            value=shunt_resistor_ohms,
            expected_smaller_value=DcRmsCurrentMeasurementTerminalRangeParameters.MINIMUM_ALLOWED_SHUNT_RESISTOR_VALUE_OHMS,
            value_name=nameof(shunt_resistor_ohms),
        )

        self._terminal_configuration = terminal_configuration
        self._range_min_amperes = range_min_amperes
        self._range_max_amperes = range_max_amperes
        self._shunt_resistor_ohms = shunt_resistor_ohms

    @property
    def terminal_configuration(self) -> nidaqmx.constants.TerminalConfiguration:
        """
        :class:`nidaqmx.constants.TerminalConfiguration`:
            Gets the input terminal configuration parameter.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._terminal_configuration

    @property
    def range_min_amperes(self) -> float:
        """
        :type:`float`: Gets the minimum value expected for the measurement on the channel.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        return self._range_min_amperes

    @property
    def range_max_amperes(self) -> float:
        """
        :type:`float`: Gets the maximum value expected for the measurement on the channel.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        return self._range_max_amperes

    @property
    def shunt_resistor_ohms(self) -> float:
        """
        :type:`float`: Gets the value in ohms of an external shunt resistor.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        return self._shunt_resistor_ohms


class DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(PCBATestToolkitData):
    """Defines the parameters used to configure channels for DC-RMS Current measurement."""

    def __init__(
        self,
        channel_name: str,
        channel_parameters: DcRmsCurrentMeasurementTerminalRangeParameters,
    ) -> None:
        """Initializes an instance of `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters`
           with specific values.

        Args:
            channel_name (str):
                The name of the channel to configure.
            channel_parameters (DcRmsCurrentMeasurementTerminalRangeParameters):
                An instance of `DcRmsCurrentMeasurementTerminalRangeParameters` that specifies
                the parameters used to configure the channel.

        Raises:
            ValueError when,
                    the value of `channel_name` is set to None or empty or whitespace,
                    when `channel_parameters` is None.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_not_none_nor_empty_nor_whitespace(channel_name, nameof(channel_name))
        Guard.is_not_none(channel_parameters, nameof(channel_parameters))

        self._channel_name = channel_name
        self._channel_parameters = channel_parameters

    @property
    def channel_name(self) -> str:
        """
        :type:`str`: Gets the name of the channel to configure.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        return self._channel_name

    @property
    def channel_parameters(self) -> DcRmsCurrentMeasurementTerminalRangeParameters:
        """
        :class:`DcRmsCurrentMeasurementTerminalRangeParameters`:
            Gets an instance of `DcRmsCurrentMeasurementTerminalRangeParameters` that specifies
            the parameters used to configure the channel.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._channel_parameters


class DcRmsCurrentMeasurementConfiguration(PCBATestToolkitData):
    """Defines parameters used for configuration of the DC-RMS current measurement."""

    def __init__(
        self,
        global_channel_parameters: DcRmsCurrentMeasurementTerminalRangeParameters,
        specific_channels_parameters: List[
            DcRmsCurrentMeasurementChannelAndTerminalRangeParameters
        ],
        measurement_options: MeasurementOptions,
        sample_clock_timing_parameters: SampleClockTimingParameters,
        digital_start_trigger_parameters: DigitalStartTriggerParameters,
    ) -> None:
        """Initializes an instance of
        `DcRmsCurrentMeasurementConfiguration` with specific values.

        Args:
            global_channel_parameters (DcRmsCurrentMeasurementTerminalRangeParameters):
                The settings of terminal for all channels.
            specific_channels_parameters (DcRmsCurrentMeasurementChannelAndTerminalRangeParameters):
                The list of instances of `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters` used to configure channels.
            measurement_options (MeasurementOptions):
                An instance of `MeasurementOptions` that represents the settings of options used for execution.
            sample_clock_timing_parameters (SampleClockTimingParameters):
                An instance of `SampleClockTimingParameters` that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters` that represents the settings of triggers.

        Raises:
            TypeError:
                Raised when `specific_channels_parameters`
                contains objects that are not type of `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters`.
            ValueError:
                Raised when `global_channel_parameters` is None,
                `specific_channels_parameters` is None,
                `measurement_options` is None,
                `sample_clock_timing_parameters` is None,
                `digital_start_trigger_parameters` is None,
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (127 > 100 characters) (auto-generated noqa)

        Guard.is_not_none(global_channel_parameters, nameof(global_channel_parameters))
        Guard.is_not_none(specific_channels_parameters, nameof(specific_channels_parameters))
        Guard.is_not_none(measurement_options, nameof(measurement_options))
        Guard.is_not_none(sample_clock_timing_parameters, nameof(sample_clock_timing_parameters))
        Guard.is_not_none(
            digital_start_trigger_parameters, nameof(digital_start_trigger_parameters)
        )
        Guard.all_elements_are_of_same_type(
            input_list=specific_channels_parameters,
            expected_type=DcRmsCurrentMeasurementChannelAndTerminalRangeParameters,
        )

        self._global_channel_parameters = global_channel_parameters
        self._specific_channels_parameters = specific_channels_parameters
        self._measurement_options = measurement_options
        self._sample_clock_timing_parameters = sample_clock_timing_parameters
        self._digital_start_trigger_parameters = digital_start_trigger_parameters

    @property
    def global_channel_parameters(
        self,
    ) -> DcRmsCurrentMeasurementTerminalRangeParameters:
        """
        :class:`DcRmsCurrentMeasurementTerminalRangeParameters`:
            Gets the settings of terminal for all channels."""  # noqa: D205, D209, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (444 > 100 characters) (auto-generated noqa)
        return self._global_channel_parameters

    @property
    def specific_channels_parameters(
        self,
    ) -> List[DcRmsCurrentMeasurementChannelAndTerminalRangeParameters]:
        """
        :class:`List[DcRmsCurrentMeasurementChannelAndTerminalRangeParameters]`:
            Gets the list of instances of
            `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters` used to configure channels.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._specific_channels_parameters

    @property
    def measurement_options(self) -> MeasurementOptions:
        """
        :class:`MeasurementOptions`:
            Gets a `MeasurementOptions` instance
            that represents the settings of options used for execution.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._measurement_options

    @property
    def sample_clock_timing_parameters(self) -> SampleClockTimingParameters:
        """
        :class:`SampleClockTimingParameters`:
            Gets a `SampleClockTimingParameters` instance
            that represents the settings of timing.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._sample_clock_timing_parameters

    @property
    def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters:
        """
        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._digital_start_trigger_parameters


class DcRmsCurrentMeasurementResultData(PCBATestToolkitData):
    """Defines the result values computed during analysis procedure for DC-RMS Current measurement."""  # noqa: W505 - doc line too long (102 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        waveforms: list[AnalogWaveform],
        acquisition_duration_seconds: float,
        dc_values_amperes: list[float],
        rms_values_amperes: list[float],
    ) -> None:
        """Initializes an instance of
        `DcRmsCurrentMeasurementResultData` with specific values.

        Args:
            waveforms (List[AnalogWaveform]):
                The list of waveforms acquired from channels defined for measurement and used to compute DC-RMS current.
            acquisition_duration_seconds (float):
                The duration of acquisition of samples for each configured channel.
            dc_values_amperes (List[float]):
                The list of DC value of the current computed for all configured channels, expressed in amperes.
            rms_values_amperes (List[float]):
                The list of RMS value of the current computed for all configured channels, expressed in amperes.

        Raises:
            TypeError when,
                `waveforms` containes objects that are not `AnalogWaveform',
                `dc_values_amperes` contains objects that are not `float',
                `rms_values_amperes` contains objects that are not `float'.
            ValueError when,
                `waveforms` is None.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (120 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(waveforms, nameof(waveforms))
        Guard.all_elements_are_of_same_type(input_list=waveforms, expected_type=AnalogWaveform)
        Guard.all_elements_are_of_same_type(input_list=dc_values_amperes, expected_type=float)
        Guard.all_elements_are_of_same_type(input_list=rms_values_amperes, expected_type=float)
        Guard.have_same_size(waveforms, nameof(waveforms), dc_values_amperes, nameof(dc_values_amperes))
        Guard.have_same_size(waveforms, nameof(waveforms), rms_values_amperes, nameof(rms_values_amperes))

        self._waveforms = waveforms
        self._acquisition_duration_seconds = acquisition_duration_seconds
        self._dc_values_amperes = dc_values_amperes
        self._rms_values_amperes = rms_values_amperes

    @property
    def waveforms(self) -> List[AnalogWaveform]:
        """
        :class:`List[AnalogWaveform]`:
            Gets the list of waveforms acquired from channels defined
            for measurement and used to compute DC-RMS current.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._waveforms

    @property
    def acquisition_duration_seconds(self) -> float:
        """
        :type:`float`:
            Gets the duration of acquisition of samples for each configured channel.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._acquisition_duration_seconds

    @property
    def dc_values_amperes(self) -> List[float]:
        """
        :class:`List[float]`:
            Gets the list of DC current computed for all configured channels, expressed in amperes.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._dc_values_amperes

    @property
    def rms_values_amperes(self) -> List[float]:
        """
        :class:`List[float]`:
            Gets the list of RMS current computed for all configured channels, expressed in amperes.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._rms_values_amperes
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dc_rms_current_measurements/dc_rms_current_measurement.py sha256=e897ec7984a3305468175ff1c87bdee351ea0e01a53a72fc215147da015cfb33 bytes=15003 -->
## FILE: src/nipcbatt/pcbatt_library/daq/dc_rms_current_measurements/dc_rms_current_measurement.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/dc_rms_current_measurements/dc_rms_current_measurement.py`
- sha256: `e897ec7984a3305468175ff1c87bdee351ea0e01a53a72fc215147da015cfb33`
- bytes: 15003

````python
# flake8: noqa
# noqa: E501
""" Defines class used for DC-RMS Current measurement on PCB points."""

from typing import Union

import nidaqmx.constants
import nidaqmx.stream_readers
import numpy
from varname import nameof

from nipcbatt.pcbatt_analysis.waveform_analysis.dc_rms_analysis import LabViewBasicDcRms
from nipcbatt.pcbatt_library.common.common_data_types import (
    AnalogWaveform,
    DigitalStartTriggerParameters,
    MeasurementAnalysisRequirement,
    MeasurementData,
    MeasurementExecutionType,
    SampleClockTimingParameters,
    SampleTimingEngine,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.daq.dc_rms_current_measurements.dc_rms_current_constants import (
    ConstantsForDcRmsCurrentMeasurement,
)
from nipcbatt.pcbatt_library.daq.dc_rms_current_measurements.dc_rms_current_data_types import (
    DcRmsCurrentMeasurementChannelAndTerminalRangeParameters,
    DcRmsCurrentMeasurementConfiguration,
    DcRmsCurrentMeasurementResultData,
    DcRmsCurrentMeasurementTerminalRangeParameters,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_utilities.guard_utilities import Guard
from nipcbatt.pcbatt_utilities.numeric_utilities import invert_value


class DcRmsCurrentMeasurement(BuildingBlockUsingDAQmx):
    """Defines a way that allows you to perform DC and RMS current measurements on PCB points."""

    using_specific_channel = False

    def initialize(self, analog_input_channel_expression: str, use_specific_channel: bool = False):
        """Initializes the measurement with the specific channels

        Args:
            analog_input_channel_expression (str):
                Expression representing the name of a physical channel,
                or a global channel in DAQ System.
        """
        if self.is_task_initialized:
            return

        self.using_specific_channel = use_specific_channel
        # If using_specific_channel is True skip the initialization.
        # This is required as Current channels do not allow overwriting of min and max range values
        # To overcome this, channels will be initialized in configure_specific_channel()
        if self.using_specific_channel is True:
            pass
        # Else initialize channels with default values
        else:
            # If the input channel_expression contains global channel, then add them as global channels
            # and verify if the global channels are configured for current measurement.
            if self.contains_only_global_virtual_channels(
                channel_expression=analog_input_channel_expression
            ):
                self.add_global_channels(global_channel_expression=analog_input_channel_expression)
                self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
                self.verify_measurement_type(nidaqmx.constants.UsageTypeAI.CURRENT)
            else:
                # Add the channel_expression to analog input current channel of the Daqmx task
                self.task.ai_channels.add_ai_current_chan(
                    physical_channel=analog_input_channel_expression,
                    name_to_assign_to_channel="",
                    terminal_config=ConstantsForDcRmsCurrentMeasurement.INITIAL_AI_TERMINAL_CONFIGURATION,
                    min_val=ConstantsForDcRmsCurrentMeasurement.INITIAL_CURRENT_RANGE_MINIMUM_AMPERES,
                    max_val=ConstantsForDcRmsCurrentMeasurement.INITIAL_CURRENT_RANGE_MAXIMUM_AMPERES,
                    units=ConstantsForDcRmsCurrentMeasurement.INITIAL_AI_CURRENT_UNITS,
                    shunt_resistor_loc=ConstantsForDcRmsCurrentMeasurement.INITIAL_SHUNT_RESISTOR_LOCATION,
                    ext_shunt_resistor_val=ConstantsForDcRmsCurrentMeasurement.INITIAL_EXTERNAL_SHUNT_RESISTOR_VALUE_OHMS,
                )

    def close(self):
        """Closes measurement procedure and releases internal resources."""

        if not self.is_task_initialized:
            return

        # Stop and close the DAQmx task
        self.task.stop()
        self.task.close()

    def configure_and_measure(
        self, configuration: DcRmsCurrentMeasurementConfiguration
    ) -> Union[None, DcRmsCurrentMeasurementResultData]:
        """Configures and/or performs a measurement
           according to specific configuration parameters.

        Args:
        configuration (DcRmsCurrentMeasurementConfiguration): An instance of
            `DcRmsCurrentMeasurementConfiguration` used to configure the measurement.

        Returns:
            DcRmsCurrentMeasurementResultData | None:
              An instance of `DcRmsCurrentMeasurementResultData`
              or `None` if no measure was performed.
        """

        if configuration.measurement_options.execution_option in (
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.CONFIGURE_ONLY,
        ):
            if self.using_specific_channel is True:
                for specific_channel_parameters in configuration.specific_channels_parameters:
                    self.configure_specific_channel(specific_channel_parameters)
            else:
                self.configure_all_channels(configuration.global_channel_parameters)

            self.configure_timing(configuration.sample_clock_timing_parameters)
            self.configure_trigger(configuration.digital_start_trigger_parameters)

        if configuration.measurement_options.execution_option in (
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.MEASURE_ONLY,
        ):
            self.task.start()
            data = self.acquire_data_for_measurement_analysis()
            return self.analyze_measurement_data(
                data, configuration.measurement_options.measurement_analysis_requirement
            )

        self.task.start()
        return None

    def configure_all_channels(
        self, parameters: DcRmsCurrentMeasurementTerminalRangeParameters
    ) -> None:
        """Configures all channels for DC-RMS Current measurement.

        Args:
            parameters (DcRmsCurrentMeasurementTerminalRangeParameters):
                An instance of `DcRmsCurrentMeasurementTerminalRangeParameters`
                used to configure the channels.
        """
        for channel in self.task.ai_channels:
            channel.ai_min = parameters.range_min_amperes
            channel.ai_max = parameters.range_max_amperes
            channel.ai_term_cfg = parameters.terminal_configuration
            channel.ai_current_shunt_resistance = parameters.shunt_resistor_ohms

    def configure_specific_channel(
        self, parameters: DcRmsCurrentMeasurementChannelAndTerminalRangeParameters
    ) -> None:
        """Configures the range and terminal configurations
           for specific channels used for DC-RMS current measurement.

        Args:
            parameters (DcRmsCurrentMeasurementChannelAndTerminalRangeParameters):
                An instance of `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters`
            used to configure the channels.
        """
        if self.contains_only_global_virtual_channels(channel_expression=parameters.channel_name):
            # Global virtual channel
            self.add_global_channels(global_channel_expression=parameters.channel_name)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
            self.verify_measurement_type(nidaqmx.constants.UsageTypeAI.CURRENT)

            channel = self.task.ai_channels[parameters.channel_name]
            channel.ai_min = parameters.channel_parameters.range_min_amperes
            channel.ai_max = parameters.channel_parameters.range_max_amperes
            channel.ai_term_cfg = parameters.channel_parameters.terminal_configuration
            channel.ai_current_shunt_resistance = parameters.channel_parameters.shunt_resistor_ohms

        else:
            # Physical channel
            self.task.ai_channels.add_ai_current_chan(
                physical_channel=parameters.channel_name,
                terminal_config=parameters.channel_parameters.terminal_configuration,
                min_val=parameters.channel_parameters.range_min_amperes,
                max_val=parameters.channel_parameters.range_max_amperes,
                units=ConstantsForDcRmsCurrentMeasurement.INITIAL_AI_CURRENT_UNITS,
                shunt_resistor_loc=ConstantsForDcRmsCurrentMeasurement.INITIAL_SHUNT_RESISTOR_LOCATION,
                ext_shunt_resistor_val=parameters.channel_parameters.shunt_resistor_ohms,
            )

    def configure_timing(self, parameters: SampleClockTimingParameters):
        """Configures the timing characteristics used for Current measurements.
        Args:
            parameters (SampleClockTimingParameters):
            An instance of `SampleClockTimingParameters`
            used to configure the timing.
        """
        self.task.timing.cfg_samp_clk_timing(
            rate=parameters.sampling_rate_hertz,
            sample_mode=nidaqmx.constants.AcquisitionType.FINITE,
            samps_per_chan=parameters.number_of_samples_per_channel,
            source=parameters.sample_clock_source,
        )

        # if the current timing engine setting is Auto
        # then delete the previous timing engine property
        # and let the task revert to the default setting of DAQmx
        # to automatically set the value of the timing engine
        if parameters.sample_timing_engine == SampleTimingEngine.AUTO:
            # Sample timing engine is auto selected
            ...
        else:
            self.task.timing.samp_timing_engine = parameters.sample_timing_engine.value

    def configure_trigger(self, parameters: DigitalStartTriggerParameters):
        """Configure the characteristics of triggers used for Current measurements.

        Args:
            parameters (DigitalStartTriggerParameters):
            An instance of `DigitalStartTriggerParameters`
            used to configure the channels.
        """
        if parameters.trigger_select == StartTriggerType.NO_TRIGGER:
            self.task.triggers.start_trigger.disable_start_trig()
        else:
            self.task.triggers.start_trigger.cfg_dig_edge_start_trig(
                trigger_source=parameters.digital_start_trigger_source,
                trigger_edge=parameters.digital_start_trigger_edge,
            )

    def acquire_data_for_measurement_analysis(self) -> MeasurementData:
        """Acquires Data from DAQ channel for measurement of Current.

        Returns:
            MeasurementData: An instance of `MeasurementData`
            that specifies the data acquired from DAQ channels.
        """
        number_of_channels = len(self.task.in_stream.channels_to_read.channel_names)
        number_of_samples_per_channel = self.task.timing.samp_quant_samp_per_chan
        data_to_read = numpy.zeros(
            shape=(number_of_channels, number_of_samples_per_channel),
            dtype=numpy.float64,
        )
        reader = nidaqmx.stream_readers.AnalogMultiChannelReader(self.task.in_stream)
        reader.read_many_sample(
            data=data_to_read,
            number_of_samples_per_channel=number_of_samples_per_channel,
        )

        return MeasurementData(data_to_read)

    def analyze_measurement_data(
        self,
        measurement_data: MeasurementData,
        measurement_analysis_requirement: MeasurementAnalysisRequirement,
    ) -> DcRmsCurrentMeasurementResultData:
        """Proceeds to the analysis of DC and RMS current from the measurement data.

        Args:
            data (MeasurementData):
                An instance of `MeasurementData`
                that specifies the data acquired from DAQ channels.
            measurement_analysis_requirement (MeasurementAnalysisRequirement):
                An instance of 'MeasurementAnalysisRequirement' that specifies
                whether to Skip Analysis or Proceed to Analysis.

        Returns:
            DcRmsCurrentMeasurementResultData:
            An instance of `DcRmsCurrentMeasurementResultData`
            that specifies the measurement results.
        """
        # Check if sampling rate is 0 and raise error to avoid divide by 0 error.
        Guard.is_greater_than_zero(
            self.task.timing.samp_clk_rate, nameof(self.task.timing.samp_clk_rate)
        )

        delta_time_seconds = invert_value(self.task.timing.samp_clk_rate)
        acquisition_duration = (
            self.task.timing.samp_quant_samp_per_chan / self.task.timing.samp_clk_rate
        )

        # Initialization for DcRmsCurrentMeasurementResultData instance creation.
        current_waveforms = []
        calculated_dc_values = []
        calculated_rms_values = []

        # Get the Analog Waveform and calculate the DC and RMS current measurements
        # for every channel in the task.
        for samples_per_channel, channel_name_read in zip(
            measurement_data.samples_per_channel,
            self.task.in_stream.channels_to_read.channel_names,
        ):
            # Creates an instance of AnalogWaveform for a channel and add it to waveforms.
            current_waveforms.append(
                AnalogWaveform(
                    channel_name=channel_name_read,
                    delta_time_seconds=delta_time_seconds,
                    samples=samples_per_channel,
                )
            )

            if (
                measurement_analysis_requirement
                == MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
            ):
                # DC and RMS processing.
                dc_rms_processing_result = LabViewBasicDcRms.process_single_waveform_dc_rms(
                    waveform_samples=samples_per_channel,
                    waveform_sampling_period_seconds=delta_time_seconds,
                    dc_rms_processing_window=ConstantsForDcRmsCurrentMeasurement.DEFAULT_DC_RMS_PROCESSING_WINDOW,
                )

                # Obtains the DC value for the acquired samples for a channel and append to the list
                calculated_dc_values.append(dc_rms_processing_result.dc_value)

                # Obtains the RMS value for the acquired samples for a channel and append to the list
                calculated_rms_values.append(dc_rms_processing_result.rms_value)

        return DcRmsCurrentMeasurementResultData(
            waveforms=current_waveforms,
            acquisition_duration_seconds=acquisition_duration,
            dc_values_amperes=calculated_dc_values,
            rms_values_amperes=calculated_rms_values,
        )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dc_rms_voltage_measurements/__init__.py sha256=aaf5c6804592ff8a78f2364c99b1b3142a89cbabb00f7de5daddad56647de785 bytes=249 -->
## FILE: src/nipcbatt/pcbatt_library/daq/dc_rms_voltage_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/dc_rms_voltage_measurements/__init__.py`
- sha256: `aaf5c6804592ff8a78f2364c99b1b3142a89cbabb00f7de5daddad56647de785`
- bytes: 249

````python
"""Provides nipcbatt library DC-RMS voltage measurement modules"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (177 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dc_rms_voltage_measurements/dc_rms_voltage_constants.py sha256=6b2e5c87926706510ea543d0f8d6fdfbb9dbf72c134e3d71927a01e95e17af17 bytes=3014 -->
## FILE: src/nipcbatt/pcbatt_library/daq/dc_rms_voltage_measurements/dc_rms_voltage_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/dc_rms_voltage_measurements/dc_rms_voltage_constants.py`
- sha256: `6b2e5c87926706510ea543d0f8d6fdfbb9dbf72c134e3d71927a01e95e17af17`
- bytes: 3014

````python
""" Constants data types for DC-RMS Voltage  Measurements."""

import dataclasses

from nipcbatt.pcbatt_analysis.waveform_analysis.dc_rms_analysis import (
    DcRmsProcessingWindow,
)
from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
    MeasurementOptions,
    SampleClockTimingParameters,
)
from nipcbatt.pcbatt_library.daq.common.voltage_constants import (
    ConstantsForVoltageMeasurement,
)
from nipcbatt.pcbatt_library.daq.common.voltage_data_types import (
    VoltageRangeAndTerminalParameters,
)
from nipcbatt.pcbatt_library.daq.dc_rms_voltage_measurements.dc_rms_voltage_data_types import (
    DcRmsVoltageMeasurementConfiguration,
)


@dataclasses.dataclass
class ConstantsForDcRmsVoltageMeasurement:
    """Constants used for Voltage measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)

    DEFAULT_DC_RMS_PROCESSING_WINDOW = DcRmsProcessingWindow.HANN


DEFAULT_DC_RMS_VOLTAGE_RANGE_AND_TERMINAL_PARAMETERS = VoltageRangeAndTerminalParameters(
    terminal_configuration=ConstantsForVoltageMeasurement.DEFAULT_AI_TERMINAL_CONFIGURATION,
    range_min_volts=ConstantsForVoltageMeasurement.DEFAULT_VOLTAGE_MINIMUM_VALUE_VOLTS,
    range_max_volts=ConstantsForVoltageMeasurement.DEFAULT_VOLTAGE_MAXIMUM_VALUE_VOLTS,
)

DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_OPTIONS = MeasurementOptions(
    execution_option=ConstantsForVoltageMeasurement.DEFAULT_EXECUTION_TYPE,
    measurement_analysis_requirement=ConstantsForVoltageMeasurement.DEFAULT_MEASUREMENT_ANALYSIS_REQUIREMENT,
)

DEFAULT_DC_RMS_VOLTAGE_SAMPLE_CLOCK_TIMING_PARAMETERS = SampleClockTimingParameters(
    sample_clock_source=ConstantsForVoltageMeasurement.DEFAULT_SAMPLE_CLOCK_SOURCE,
    sampling_rate_hertz=ConstantsForVoltageMeasurement.DEFAULT_SAMPLING_RATE_HERTZ,
    number_of_samples_per_channel=ConstantsForVoltageMeasurement.DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL,
    sample_timing_engine=ConstantsForVoltageMeasurement.DEFAULT_SAMPLE_TIMING_ENGINE,
)

DEFAULT_DC_RMS_VOLTAGE_DIGITAL_START_TRIGGER_PARAMETERS = DigitalStartTriggerParameters(
    trigger_select=ConstantsForVoltageMeasurement.DEFAULT_TRIGGER_TYPE,
    digital_start_trigger_source=ConstantsForVoltageMeasurement.DEFAULT_DIGITAL_START_TRIGGER_SOURCE,
    digital_start_trigger_edge=ConstantsForVoltageMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE,
)

DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION = DcRmsVoltageMeasurementConfiguration(
    global_channel_parameters=DEFAULT_DC_RMS_VOLTAGE_RANGE_AND_TERMINAL_PARAMETERS,
    specific_channels_parameters=[],
    measurement_options=DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_OPTIONS,
    sample_clock_timing_parameters=DEFAULT_DC_RMS_VOLTAGE_SAMPLE_CLOCK_TIMING_PARAMETERS,
    digital_start_trigger_parameters=DEFAULT_DC_RMS_VOLTAGE_DIGITAL_START_TRIGGER_PARAMETERS,
)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dc_rms_voltage_measurements/dc_rms_voltage_data_types.py sha256=467757e8fda9171db9237c83a378193f6c6b226da546a3b8ed3a58a66d02bf0d bytes=12981 -->
## FILE: src/nipcbatt/pcbatt_library/daq/dc_rms_voltage_measurements/dc_rms_voltage_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/dc_rms_voltage_measurements/dc_rms_voltage_data_types.py`
- sha256: `467757e8fda9171db9237c83a378193f6c6b226da546a3b8ed3a58a66d02bf0d`
- bytes: 12981

````python
# pylint: disable=C0301
""" DC-RMS Voltage data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (144 > 100 characters) (auto-generated noqa)

from typing import List

from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    AnalogWaveform,
    DigitalStartTriggerParameters,
    MeasurementOptions,
    SampleClockTimingParameters,
)
from nipcbatt.pcbatt_library.daq.common.voltage_data_types import (
    VoltageMeasurementChannelAndTerminalRangeParameters,
    VoltageRangeAndTerminalParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DcRmsVoltageMeasurementConfiguration(PCBATestToolkitData):
    """Defines parameters used for configuration of DC-RMS voltage measurement."""

    def __init__(
        self,
        global_channel_parameters: VoltageRangeAndTerminalParameters,
        specific_channels_parameters: List[VoltageMeasurementChannelAndTerminalRangeParameters],
        measurement_options: MeasurementOptions,
        sample_clock_timing_parameters: SampleClockTimingParameters,
        digital_start_trigger_parameters: DigitalStartTriggerParameters,
    ) -> None:
        """Initializes an instance of
        `DcRmsVoltageMeasurementConfiguration` with specific values.

        Args:
            global_channel_parameters (VoltageRangeAndTerminalParameters):
                The settings of terminal for all channels.
            specific_channels_parameters (List[VoltageMeasurementChannelAndTerminalRangeParameters]):
                The list of instances of `VoltageMeasurementChannelAndTerminalRangeParameters` used to configure channels.
            measurement_options (MeasurementOptions):
                An instance of `MeasurementOptions` that represents the settings of options used for execution.
            sample_clock_timing_parameters (SampleClockTimingParameters):
                An instance of `SampleClockTimingParameters` that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters` that represents the settings of triggers.

        Raises:
            TypeError:
                Raised when `specific_channels_parameters`
                contains objects that are not type of `VoltageMeasurementChannelAndTerminalRangeParameters`.
            ValueError:
                Raised when
                `specific_channels_parameters` is None,
                `global_channel_parameters` is None,
                `measurement_options` is None,
                `sample_clock_timing_parameters` is None,
                `digital_start_trigger_parameters` is None.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (101 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(global_channel_parameters, nameof(global_channel_parameters))
        Guard.is_not_none(specific_channels_parameters, nameof(specific_channels_parameters))
        Guard.all_elements_are_of_same_type(
            input_list=specific_channels_parameters,
            expected_type=VoltageMeasurementChannelAndTerminalRangeParameters,
        )
        Guard.is_not_none(measurement_options, nameof(measurement_options))
        Guard.is_not_none(sample_clock_timing_parameters, nameof(sample_clock_timing_parameters))
        Guard.is_not_none(
            digital_start_trigger_parameters, nameof(digital_start_trigger_parameters)
        )

        self._global_channel_parameters = global_channel_parameters
        self._specific_channels_parameters = specific_channels_parameters
        self._measurement_options = measurement_options
        self._sample_clock_timing_parameters = sample_clock_timing_parameters
        self._digital_start_trigger_parameters = digital_start_trigger_parameters

    @property
    def global_channel_parameters(
        self,
    ) -> VoltageRangeAndTerminalParameters:
        """
        :class:`VoltageRangeAndTerminalParameters`:
            Gets the settings of terminal for all channels."""  # noqa: D205, D209, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (444 > 100 characters) (auto-generated noqa)
        return self._global_channel_parameters

    @property
    def specific_channels_parameters(
        self,
    ) -> List[VoltageMeasurementChannelAndTerminalRangeParameters]:
        """
        :class:`List[VoltageMeasurementChannelAndTerminalRangeParameters]`:
            Gets the list of instances of
            `VoltageMeasurementChannelAndTerminalRangeParameters` used to configure channels.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._specific_channels_parameters

    @property
    def measurement_options(self) -> MeasurementOptions:
        """
        :class:`MeasurementOptions`:
            Gets a `MeasurementOptions` instance
            that represents the settings of options used for execution.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._measurement_options

    @property
    def sample_clock_timing_parameters(self) -> SampleClockTimingParameters:
        """
        :class:`SampleClockTimingParameters`:
            Gets a `SampleClockTimingParameters` instance
            that represents the settings of timing.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._sample_clock_timing_parameters

    @property
    def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters:
        """
        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._digital_start_trigger_parameters


class DcRmsVoltageMeasurementResultData(PCBATestToolkitData):
    """Defines voltage DC-RMS results obtained after waveform analysis."""

    def __init__(
        self,
        waveforms: List[AnalogWaveform],
        acquisition_duration_seconds: float,
        dc_values_volts: List[float],
        rms_values_volts: List[float],
    ) -> None:
        """Initializes an instance of
        `DcRmsVoltageMeasurementResultData` with specific values.

        Args:
            waveforms (List[AnalogWaveform]):
                The list of waveforms acquired from channels defined for measurement and used to compute DC-RMS voltage.
            acquisition_duration_seconds (float):
                The duration of acquisition of samples for each configured channel.
            dc_values_volts (List[float]):
                The list of DC voltages computed for all configured channels, expressed in Volts.
            rms_values_volts (List[float]):
                The list of RMS voltages computed for all configured channels, expressed in Volts.

        Raises:
            ValueError:
                Raised when `waveforms` is None or empty.
            TypeError:
                Raised when `waveforms` contains objects that are not `AnalogWaveform`,
                `dc_values_volts` contains objects that are not `float`,
                `rms_values_volts` contains objects that are not `float`
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (120 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(waveforms, nameof(waveforms))
        Guard.is_not_empty(waveforms, nameof(waveforms))

        Guard.is_not_none(dc_values_volts, nameof(dc_values_volts))
        Guard.is_not_empty(dc_values_volts, nameof(dc_values_volts))

        Guard.is_not_none(rms_values_volts, nameof(rms_values_volts))
        Guard.is_not_empty(rms_values_volts, nameof(rms_values_volts))

        Guard.all_elements_are_of_same_type(input_list=waveforms, expected_type=AnalogWaveform)
        Guard.all_elements_are_of_same_type(input_list=dc_values_volts, expected_type=float)
        Guard.all_elements_are_of_same_type(input_list=rms_values_volts, expected_type=float)

        self._waveforms = waveforms
        self._acquisition_duration_seconds = acquisition_duration_seconds
        self._dc_values_volts = dc_values_volts
        self._rms_values_volts = rms_values_volts

    @property
    def waveforms(self) -> List[AnalogWaveform]:
        """
        :class:`List[AnalogWaveform]`:
            Gets the list of waveforms acquired from channels defined
            for measurement and used to compute DC-RMS voltage.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._waveforms

    @property
    def acquisition_duration_seconds(self) -> float:
        """
        :type:`float`:
            Gets the duration of acquisition of samples for each configured channel.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._acquisition_duration_seconds

    @property
    def dc_values_volts(self) -> List[float]:
        """
        :class:`List[float]`:
            Gets the list of DC voltages computed for all configured channels, expressed in Volts.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._dc_values_volts

    @property
    def rms_values_volts(self) -> List[float]:
        """
        :class:`List[float]`:
            Gets the list of RMS voltages computed for all configured channels, expressed in Volts.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._rms_values_volts
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dc_rms_voltage_measurements/dc_rms_voltage_measurement.py sha256=9e9093bc79ac5b8bf7e57846baafe75e2cf175ef365a4f2919d5dab436ae0cae bytes=15919 -->
## FILE: src/nipcbatt/pcbatt_library/daq/dc_rms_voltage_measurements/dc_rms_voltage_measurement.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/dc_rms_voltage_measurements/dc_rms_voltage_measurement.py`
- sha256: `9e9093bc79ac5b8bf7e57846baafe75e2cf175ef365a4f2919d5dab436ae0cae`
- bytes: 15919

````python
# pylint: disable=W0613, C0301
# remove it when arguments of initialize are used.
""" Defines class used for DC-RMS Voltage measurement on PCB points."""

from typing import Union

import nidaqmx.constants
import nidaqmx.stream_readers
import numpy
from varname import nameof

from nipcbatt.pcbatt_analysis.waveform_analysis.dc_rms_analysis import LabViewBasicDcRms
from nipcbatt.pcbatt_library.common.common_data_types import (
    AnalogWaveform,
    DigitalStartTriggerParameters,
    MeasurementAnalysisRequirement,
    MeasurementData,
    MeasurementExecutionType,
    SampleClockTimingParameters,
    SampleTimingEngine,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.daq.common.voltage_constants import (
    ConstantsForVoltageMeasurement,
)
from nipcbatt.pcbatt_library.daq.common.voltage_data_types import (
    VoltageMeasurementChannelAndTerminalRangeParameters,
    VoltageRangeAndTerminalParameters,
)
from nipcbatt.pcbatt_library.daq.dc_rms_voltage_measurements.dc_rms_voltage_constants import (
    ConstantsForDcRmsVoltageMeasurement,
)
from nipcbatt.pcbatt_library.daq.dc_rms_voltage_measurements.dc_rms_voltage_data_types import (
    DcRmsVoltageMeasurementConfiguration,
    DcRmsVoltageMeasurementResultData,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_utilities.guard_utilities import Guard
from nipcbatt.pcbatt_utilities.numeric_utilities import invert_value


class DcRmsVoltageMeasurement(BuildingBlockUsingDAQmx):
    """Defines a way that allows you to perform DC-RMS voltage measurements on PCB points."""

    def initialize(self, analog_input_channel_expression: str):
        """Initializes the measurement with the specific channels

        Args:
            analog_input_channel_expression (str):
                Expression representing the name of a physical channel,
                or a global channel in DAQ System.
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        if self.is_task_initialized:
            return

        # If the input channel_expression contains global channel, then add them as global channels
        # and verify if the global channels are configured for current measurement.
        if self.contains_only_global_virtual_channels(
            channel_expression=analog_input_channel_expression
        ):
            self.add_global_channels(global_channel_expression=analog_input_channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
            self.verify_measurement_type(nidaqmx.constants.UsageTypeAI.VOLTAGE)
        else:
            # Add the channel_expression to analog input current channel of the Daqmx task
            self.task.ai_channels.add_ai_voltage_chan(
                physical_channel=analog_input_channel_expression,
                name_to_assign_to_channel="",
                terminal_config=ConstantsForVoltageMeasurement.INITIAL_AI_TERMINAL_CONFIGURATION,
                min_val=ConstantsForVoltageMeasurement.INITIAL_VOLTAGE_MINIMUM_VALUE_VOLTS,
                max_val=ConstantsForVoltageMeasurement.INITIAL_VOLTAGE_MAXIMUM_VALUE_VOLTS,
                units=ConstantsForVoltageMeasurement.INITIAL_AI_VOLTAGE_UNITS,
            )

    def close(self):
        """Closes measurement procedure and releases internal resources."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)

        if not self.is_task_initialized:
            return

        self.task.stop()
        self.task.close()

    def configure_and_measure(
        self, configuration: DcRmsVoltageMeasurementConfiguration
    ) -> Union[None, DcRmsVoltageMeasurementResultData]:
        """Configures and/or performs a measurement
           according to specific configuration parameters.

        Args:
            configuration (DcRmsVoltageMeasurementConfiguration):
            A instance of `DcRmsVoltageMeasurementConfiguration` used to configure the measurement.

        Returns:
            DcRmsVoltageMeasurementResultData | None: An instance of `DcRmsVoltageMeasurementResultData`
              or `None` if no measure was performed.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (104 > 100 characters) (auto-generated noqa)

        if configuration.measurement_options.execution_option in (
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.CONFIGURE_ONLY,
        ):
            self.task.stop()
            self.configure_all_channels(configuration.global_channel_parameters)
            for specific_channel_parameters in configuration.specific_channels_parameters:
                self.configure_specific_channel(specific_channel_parameters)
            self.configure_timing(configuration.sample_clock_timing_parameters)
            self.configure_trigger(configuration.digital_start_trigger_parameters)
            self.task.start()

        if configuration.measurement_options.execution_option in (
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.MEASURE_ONLY,
        ):
            data = self.acquire_data_for_measurement_analysis()
            return self.analyze_measurement_data(
                data, configuration.measurement_options.measurement_analysis_requirement
            )
        return None

    def configure_all_channels(self, parameters: VoltageRangeAndTerminalParameters):
        """Configures all channels used for voltage measurements.

        Args:
            parameters (VoltageRangeAndTerminalParameters):
            An instance of `VoltageRangeAndTerminalParameters` used to configure the channels.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        for channel in self.task.ai_channels:
            channel.ai_term_cfg = parameters.terminal_configuration
            channel.ai_min = parameters.range_min_volts
            channel.ai_max = parameters.range_max_volts

    def configure_specific_channel(
        self, parameters: VoltageMeasurementChannelAndTerminalRangeParameters
    ):
        """Configures the specific channels used for voltage measurements.

        Args:
            parameters (VoltageMeasurementChannelAndTerminalRangeParameters):
            An instance of `VoltageMeasurementChannelAndTerminalRangeParameters`
            used to configure the channels.

        If the user provides Global Virtual Channel name in Initialize(),
        then he/she has to provide the Virtual channel name in Specific channel parameters as well.

        Similarly, if the user provides Physical channel name in Initialize(),
        then he/she has to provide the Physical channel name in Specific channel parameters.
        """  # noqa: D202, D417, W505 - No blank lines allowed after function docstring (auto-generated noqa), Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

        if parameters.channel_name in (channel.name for channel in self.task.ai_channels):
            # if the specified channel is present in ai_channel_collection,
            # updates the voltage parameters of the channel
            self.task.ai_channels[
                parameters.channel_name
            ].ai_term_cfg = parameters.channel_parameters.terminal_configuration
            self.task.ai_channels[
                parameters.channel_name
            ].ai_min = parameters.channel_parameters.range_min_volts
            self.task.ai_channels[
                parameters.channel_name
            ].ai_max = parameters.channel_parameters.range_max_volts
        else:
            # otherwise, adds the channel.
            if self.contains_only_global_virtual_channels(
                channel_expression=parameters.channel_name
            ):
                # Global virtual channel
                self.add_global_channels(global_channel_expression=parameters.channel_name)
                self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
                self.verify_measurement_type(nidaqmx.constants.UsageTypeAI.VOLTAGE)
                for channel in self.task.ai_channels:
                    channel.ai_term_cfg = parameters.channel_parameters.terminal_configuration
                    channel.ai_min = parameters.channel_parameters.range_min_volts
                    channel.ai_max = parameters.channel_parameters.range_max_volts
            else:
                # Physical channel
                self.task.ai_channels.add_ai_voltage_chan(
                    physical_channel=parameters.channel_name,
                    terminal_config=parameters.channel_parameters.terminal_configuration,
                    min_val=parameters.channel_parameters.range_min_volts,
                    max_val=parameters.channel_parameters.range_max_volts,
                    units=ConstantsForVoltageMeasurement.INITIAL_AI_VOLTAGE_UNITS,
                )

    def configure_timing(self, parameters: SampleClockTimingParameters):
        """Configures the timing characteristics used for voltage measurements.

        Args:
            parameters (SampleClockTimingParameters):
            An instance of `SampleClockTimingParameters`
            used to configure the timing.
        """  # noqa: D202, D417, W505 - No blank lines allowed after function docstring (auto-generated noqa), Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

        self.task.timing.cfg_samp_clk_timing(
            rate=parameters.sampling_rate_hertz,
            sample_mode=nidaqmx.constants.AcquisitionType.FINITE,
            samps_per_chan=parameters.number_of_samples_per_channel,
            source=parameters.sample_clock_source,
        )

        # if the current timing engine setting is Auto
        # then delete the previous timing engine property
        # and let the task revert to the default setting of DAQmx
        # to automatically set the value of the timing engine
        if parameters.sample_timing_engine == SampleTimingEngine.AUTO:
            # Sample timing engine is auto selected
            ...
        else:
            self.task.timing.samp_timing_engine = parameters.sample_timing_engine.value

    def configure_trigger(self, parameters: DigitalStartTriggerParameters):
        """Configure the characteristics of triggers used for voltage measurements.

        Args:
            parameters (DigitalStartTriggerParameters):
            An instance of `DigitalStartTriggerParameters`
            used to configure the channels.
        """  # noqa: D202, D417, W505 - No blank lines allowed after function docstring (auto-generated noqa), Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

        if parameters.trigger_select == StartTriggerType.NO_TRIGGER:
            self.task.triggers.start_trigger.disable_start_trig()
        else:
            self.task.triggers.start_trigger.cfg_dig_edge_start_trig(
                trigger_source=parameters.digital_start_trigger_source,
                trigger_edge=parameters.digital_start_trigger_edge,
            )

    def acquire_data_for_measurement_analysis(self) -> MeasurementData:
        """Acquires Data from DAQ channel for measurement of voltage.

        Returns:
            MeasurementData: An instance of `MeasurementData`
            that specifies the data acquired from DAQ channels.
        """
        number_of_channels = len(self.task.in_stream.channels_to_read.channel_names)
        number_of_samples_per_channel = self.task.timing.samp_quant_samp_per_chan
        data_to_read = numpy.zeros(
            shape=(number_of_channels, number_of_samples_per_channel),
            dtype=numpy.float64,
        )
        reader = nidaqmx.stream_readers.AnalogMultiChannelReader(self.task.in_stream)
        reader.read_many_sample(
            data=data_to_read,
            number_of_samples_per_channel=number_of_samples_per_channel,
        )

        return MeasurementData(data_to_read)

    def analyze_measurement_data(
        self,
        measurement_data: MeasurementData,
        measurement_analysis_requirement: MeasurementAnalysisRequirement,
    ) -> DcRmsVoltageMeasurementResultData:
        """Proceeds to the analysis of DC Voltages from the measurement.

        Args:
             data (MeasurementData):
                An instance of `MeasurementData`
                that specifies the data acquired from DAQ channels.
            measurement_analysis_requirement (MeasurementAnalysisRequirement):
                An instance of 'MeasurementAnalysisRequirement' that specifies
                whether to Skip Analysis or Proceed to Analysis.

        Returns:
            DcRmsVoltageMeasurementResultData:
            An instance of `DcRmsVoltageMeasurementResultData`
            that specifies the measurement results.
        """
        # Check if sampling rate is 0 and raise error to avoid divide by 0 error.
        Guard.is_greater_than_zero(
            self.task.timing.samp_clk_rate, nameof(self.task.timing.samp_clk_rate)
        )
        delta_time_seconds = invert_value(self.task.timing.samp_clk_rate)

        # Initialization for DcRmsVoltageMeasurementResultData instance creation.
        voltage_waveforms = []
        acquisition_duration_seconds = 0.0
        dc_values_volts = []
        rms_values_volts = []

        for samples_per_channel, channel_name in zip(
            measurement_data.samples_per_channel,
            self.task.in_stream.channels_to_read.channel_names,
        ):
            # Creates an instance of AnalogWaveform and add it to waveforms.
            voltage_waveforms.append(
                AnalogWaveform(
                    channel_name=channel_name,
                    delta_time_seconds=delta_time_seconds,
                    samples=samples_per_channel,
                )
            )
            if (
                measurement_analysis_requirement
                == MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
            ):
                acquisition_duration_seconds += delta_time_seconds * len(samples_per_channel)
                # DC and RMS processing.
                dc_rms_processing_result = LabViewBasicDcRms.process_single_waveform_dc_rms(
                    waveform_samples=samples_per_channel,
                    waveform_sampling_period_seconds=delta_time_seconds,
                    dc_rms_processing_window=ConstantsForDcRmsVoltageMeasurement.DEFAULT_DC_RMS_PROCESSING_WINDOW,
                )

                dc_values_volts.append(dc_rms_processing_result.dc_value)
                rms_values_volts.append(dc_rms_processing_result.rms_value)

        return DcRmsVoltageMeasurementResultData(
            waveforms=voltage_waveforms,
            acquisition_duration_seconds=acquisition_duration_seconds,
            dc_values_volts=dc_values_volts,
            rms_values_volts=rms_values_volts,
        )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dc_voltage_generations/__init__.py sha256=5b68a96183c641757cc722fae07e3847c892f2c744f6bbc3751289821356bc81 bytes=244 -->
## FILE: src/nipcbatt/pcbatt_library/daq/dc_voltage_generations/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/dc_voltage_generations/__init__.py`
- sha256: `5b68a96183c641757cc722fae07e3847c892f2c744f6bbc3751289821356bc81`
- bytes: 244

````python
"""Provides nipcbatt library DC voltage generation modules"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (172 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dc_voltage_generations/dc_voltage_data_types.py sha256=a393589aa5953a7e73201b62078bcb3754da75cbca106ed3d986373e3d2db127 bytes=3534 -->
## FILE: src/nipcbatt/pcbatt_library/daq/dc_voltage_generations/dc_voltage_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/dc_voltage_generations/dc_voltage_data_types.py`
- sha256: `a393589aa5953a7e73201b62078bcb3754da75cbca106ed3d986373e3d2db127`
- bytes: 3534

````python
""" DC Voltage data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (140 > 100 characters) (auto-generated noqa)

from typing import List

from varname import nameof

from nipcbatt.pcbatt_library.daq.common.voltage_data_types import (
    VoltageGenerationChannelParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DcVoltageGenerationConfiguration(PCBATestToolkitData):
    """Defines parameters used for configuration of DC Voltage generation."""

    def __init__(
        self,
        voltage_generation_range_parameters: VoltageGenerationChannelParameters,
        output_voltages: List[float],
    ) -> None:
        """Initializes an instance of `DcVoltageGenerationConfiguration` with specific values.

        Args:
            voltage_generation_range_parameters (VoltageGenerationChannelParameters):
                The settings of the terminal for all channel for DC voltage generation.
            output_voltages (List[float]):
                specifies the actual output voltage to generate on the selected channel(s).
                Each element of the array corresponds to a channel in the task.
                The order of the channels in the array corresponds to the order in which you add the channels to the task in the Initialize method.

        Raises:
            ValueError:
                If the input `voltage_generation_range_parameters' does not contain a valid object.
                If the input `output_voltages' is an empty array.
        """  # noqa: W505 - doc line too long (147 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(
            voltage_generation_range_parameters,
            nameof(voltage_generation_range_parameters),
        )
        Guard.is_not_empty(output_voltages, nameof(output_voltages))

        self._voltage_generation_range_parameters = voltage_generation_range_parameters
        self._output_voltages = output_voltages

    @property
    def voltage_generation_range_parameters(self) -> VoltageGenerationChannelParameters:
        """
        :class:`VoltageGenerationChannelParameters`:
            Gets an instance of `VoltageGenerationChannelParameters'
            that represents the terminal settings for all channel for DC voltage generation.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._voltage_generation_range_parameters

    @property
    def output_voltages(self) -> List[float]:
        """
        :class:`List[float]`:
            Gets the list of output voltages to be generated at the selected channel(s).
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._output_voltages
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dc_voltage_generations/dc_voltage_generation.py sha256=358adc9789d782beeaa4140b5a190e76ca8a8bff8bc18a2f197b15ebda86686f bytes=5840 -->
## FILE: src/nipcbatt/pcbatt_library/daq/dc_voltage_generations/dc_voltage_generation.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/dc_voltage_generations/dc_voltage_generation.py`
- sha256: `358adc9789d782beeaa4140b5a190e76ca8a8bff8bc18a2f197b15ebda86686f`
- bytes: 5840

````python
# pylint: disable=W0613
# remove it when arguments of initialize are used.
""" Defines class used for generation of DC voltage on PCB points. """

from typing import List

import nidaqmx.constants
import nidaqmx.stream_writers
import numpy
from varname import nameof

from nipcbatt.pcbatt_library.daq.common.voltage_data_types import (
    VoltageGenerationChannelParameters,
)
from nipcbatt.pcbatt_library.daq.dc_voltage_generations.dc_voltage_data_types import (
    DcVoltageGenerationConfiguration,
)
from nipcbatt.pcbatt_library.daq.dc_voltage_generations.dc_voltage_generation_constants import (
    ConstantsForDcVoltageGeneration,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DcVoltageGeneration(BuildingBlockUsingDAQmx):
    """Defines a way for the user to configure the Analog Output pins for DC voltage generation."""

    def initialize(self, analog_output_channel_expression: str):
        """Initializes the DC voltage generation with the specific channels.

        Args:
            analog_output_channel_expression (str):
                Expression representing the name of an analog output physical channel,
                or a global channel in DAQ System.
        """
        if self.is_task_initialized:
            return

        # If the input analog_output_channel_expression contains global channel, then add them as global channels  # noqa: W505 - doc line too long (113 > 100 characters) (auto-generated noqa)
        # and verify if the global channels are configured for analog output voltage.
        if self.contains_only_global_virtual_channels(
            channel_expression=analog_output_channel_expression
        ):
            self.add_global_channels(global_channel_expression=analog_output_channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
            self.verify_generation_type(nidaqmx.constants.UsageTypeAO.VOLTAGE)
        else:
            # Add the analog_output_channel_expression to analog output channel of the Daqmx task
            self.task.ao_channels.add_ao_voltage_chan(
                physical_channel=analog_output_channel_expression,
                min_val=ConstantsForDcVoltageGeneration.INITIAL_RANGE_MIN_VOLTS,
                max_val=ConstantsForDcVoltageGeneration.INITIAL_RANGE_MAX_VOLTS,
                units=ConstantsForDcVoltageGeneration.INITIAL_AO_VOLTAGE_UNITS,
            )

    def configure_all_channels(
        self,
        parameters: VoltageGenerationChannelParameters,
    ) -> None:
        """Configures all analog output channels for DC Voltage generation.

        Args:
            parameters (VoltageGenerationChannelParameters):
                An instance of `VoltageGenerationChannelParameters' used to configure the channels.
        """
        self.task.stop()
        for channel in self.task.ao_channels:
            channel.ao_min = parameters.range_min_volts
            channel.ao_max = parameters.range_max_volts

    def generate_voltage(
        self,
        output_voltages: List[float],
    ) -> None:
        """Generates voltage at the DAQ channel.

        Args:
            output_voltages (List[float]):
                specifies the actual output voltage to generate on the selected channel(s).
                Each element of the array corresponds to a channel in the task.
                The order of the channels in the array corresponds to the order
                in which the channels have been added to the task in the initialize method.

        Raises:
            ValueError:
                If the `output_voltages` is an ampty array.
                If the size of `output_voltages` does not match with the number of channels in the Task.
        """  # noqa: W505 - doc line too long (104 > 100 characters) (auto-generated noqa)
        # Check if the output_voltages array is not empty and if it has same number of elements as the number of channels in the task.  # noqa: W505 - doc line too long (134 > 100 characters) (auto-generated noqa)
        Guard.is_not_empty(output_voltages, nameof(output_voltages))
        Guard.have_same_size(
            first_iterable_instance=output_voltages,
            first_iterable_name=nameof(output_voltages),
            second_iterable_instance=self.task.ao_channels.channel_names,
            second_iterable_name=nameof(self.task.ao_channels.count),
        )
        writer = nidaqmx.stream_writers.AnalogMultiChannelWriter(
            task_out_stream=self.task.out_stream,
            auto_start=True,
        )
        writer.write_one_sample(data=numpy.array(output_voltages))

    def configure_and_generate(
        self,
        configuration: DcVoltageGenerationConfiguration,
    ) -> None:
        """Configures and generates the DC Voltages according to the specific configuration.

        Args:
            configuration (DcVoltageGenerationConfiguration):
                An instance of 'DcVoltageGenerationConfiguration` used to configure the generation of DC voltage.

        Returns:
            None.
        """  # noqa: W505 - doc line too long (113 > 100 characters) (auto-generated noqa)
        self.configure_all_channels(parameters=configuration.voltage_generation_range_parameters)
        self.generate_voltage(
            output_voltages=configuration.output_voltages,
        )

    def close(self):
        """Stops and closes the generation task and releases the internal resources."""
        if not self.is_task_initialized:
            return

        # Stop and close the Daqmx task
        self.task.stop()
        self.task.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dc_voltage_generations/dc_voltage_generation_constants.py sha256=4a938ff6ac9bb945f70ff0cf7712fb264613245c70d4dd6aeaae6337f290bc4a bytes=1632 -->
## FILE: src/nipcbatt/pcbatt_library/daq/dc_voltage_generations/dc_voltage_generation_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/dc_voltage_generations/dc_voltage_generation_constants.py`
- sha256: `4a938ff6ac9bb945f70ff0cf7712fb264613245c70d4dd6aeaae6337f290bc4a`
- bytes: 1632

````python
"""Constants for DC voltage generation data types."""

import dataclasses

import nidaqmx.constants

from nipcbatt.pcbatt_library.daq.common.voltage_data_types import (
    VoltageGenerationChannelParameters,
)
from nipcbatt.pcbatt_library.daq.dc_voltage_generations.dc_voltage_data_types import (
    DcVoltageGenerationConfiguration,
)


@dataclasses.dataclass
class ConstantsForDcVoltageGeneration:
    """Constants used as Initial and defauls values for DC Voltage generation configuration"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (205 > 100 characters) (auto-generated noqa)

    INITIAL_AO_OUTPUT_TERMINAL_CONFIGURATION = nidaqmx.constants.TerminalConfiguration.RSE
    INITIAL_RANGE_MIN_VOLTS = 0.0
    INITIAL_RANGE_MAX_VOLTS = 1.0
    INITIAL_AO_VOLTAGE_UNITS = nidaqmx.constants.VoltageUnits.VOLTS

    DEFAULT_AO_OUTPUT_TERMINAL_CONFIGURATION = nidaqmx.constants.TerminalConfiguration.RSE
    DEFAULT_RANGE_MIN_VOLTS = -10.0
    DEFAULT_RANGE_MAX_VOLTS = 10.0
    DEFAULT_OUTPUT_VOLTAGES = [1.2]


DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS = VoltageGenerationChannelParameters(
    range_min_volts=ConstantsForDcVoltageGeneration.DEFAULT_RANGE_MIN_VOLTS,
    range_max_volts=ConstantsForDcVoltageGeneration.DEFAULT_RANGE_MAX_VOLTS,
)

DEFAULT_DC_VOLTAGE_GENERATION_CONFIGURATION = DcVoltageGenerationConfiguration(
    voltage_generation_range_parameters=DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS,
    output_voltages=ConstantsForDcVoltageGeneration.DEFAULT_OUTPUT_VOLTAGES,
)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_clock_generations/__init__.py sha256=b4bd3c2eb01468a5e35cb8d675fe4fac79fcf62a0e6dc91e23fb9ed86699c6c9 bytes=247 -->
## FILE: src/nipcbatt/pcbatt_library/daq/digital_clock_generations/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/digital_clock_generations/__init__.py`
- sha256: `b4bd3c2eb01468a5e35cb8d675fe4fac79fcf62a0e6dc91e23fb9ed86699c6c9`
- bytes: 247

````python
"""Provides nipcbatt library digital clock generation modules"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (175 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_clock_generations/digital_clock_constants.py sha256=52701001ed97b66976359368bbac87d5d047be0fd779578321c786a9c2b7ccdd bytes=889 -->
## FILE: src/nipcbatt/pcbatt_library/daq/digital_clock_generations/digital_clock_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/digital_clock_generations/digital_clock_constants.py`
- sha256: `52701001ed97b66976359368bbac87d5d047be0fd779578321c786a9c2b7ccdd`
- bytes: 889

````python
"Constant data types used in digital clock generation"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)

import dataclasses

import nidaqmx.constants


@dataclasses.dataclass
class ConstantsForDigitalClockGeneration:
    """Constants used in digital clock generation"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (163 > 100 characters) (auto-generated noqa)

    DEFAULT_FREQUENCY_GENERATION_UNIT = nidaqmx.constants.FrequencyUnits.HZ
    DEFAULT_GENERATION_IDLE_STATE = nidaqmx.constants.PowerUpStates.LOW
    DEFAULT_GENERATION_FREQUENCY = 1.0
    DEFAULT_GENERATION_DUTY_CYCLE = 0.5
    FINITE_SAMPLES = nidaqmx.constants.AcquisitionType.FINITE
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_clock_generations/digital_clock_data_types.py sha256=a28312dbca4b5fc0219a94e1a3d81eed04c41997428f36ed0322859506ba5674 bytes=11569 -->
## FILE: src/nipcbatt/pcbatt_library/daq/digital_clock_generations/digital_clock_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/digital_clock_generations/digital_clock_data_types.py`
- sha256: `a28312dbca4b5fc0219a94e1a3d81eed04c41997428f36ed0322859506ba5674`
- bytes: 11569

````python
""" digital clock data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (143 > 100 characters) (auto-generated noqa)

from varname import nameof

from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DigitalClockGenerationCounterChannelParameters(PCBATestToolkitData):
    """Defines the values to be used to set on the digital clock counter channel"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (194 > 100 characters) (auto-generated noqa)

    def __init__(self, frequency_hertz: float, duty_cycle_ratio: float) -> None:
        """Creates an instance of DigitalClockGenerationCounterChannelParameters

        Args:
            frequency_hertz (float): The intended frequency to generate
            duty_cycle_ratio (float): Intended high time % of clock cycle
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(frequency_hertz, nameof(frequency_hertz))
        Guard.is_greater_than_or_equal_to_zero(frequency_hertz, nameof(frequency_hertz))

        Guard.is_not_none(duty_cycle_ratio, nameof(duty_cycle_ratio))
        Guard.is_greater_than_or_equal_to_zero(duty_cycle_ratio, nameof(duty_cycle_ratio))
        Guard.is_less_than_or_equal_to(duty_cycle_ratio, 1.0, nameof(duty_cycle_ratio))

        # assign values
        self._frequency_hertz = frequency_hertz
        self._duty_cycle_ratio = duty_cycle_ratio

    @property
    def frequency_hertz(self) -> float:
        """
        :type:'float': Gets the frequency to generate
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._frequency_hertz

    @property
    def duty_cycle_ratio(self) -> float:
        """
        :type:float: Gets the duty cycle to generate
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._duty_cycle_ratio


class DigitalClockGenerationTimingParameters(PCBATestToolkitData):
    """Defines the timing values to be used in digital clock generation"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (185 > 100 characters) (auto-generated noqa)

    def __init__(self, clock_duration_seconds: float) -> None:
        """Creates an instance of DigitalClockGenerationTimingParameters

        Args:
            clock_duration_seconds (float): Clock generation time in seconds
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(clock_duration_seconds, nameof(clock_duration_seconds))
        Guard.is_greater_than_zero(clock_duration_seconds, nameof(clock_duration_seconds))

        # assign values
        self._clock_duration_seconds = clock_duration_seconds

    @property
    def clock_duration_seconds(self) -> float:
        """
        :type:float: Gets the length of the duration of the signal
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._clock_duration_seconds


class DigitalClockGenerationConfiguration(PCBATestToolkitData):
    """Defines values to be used in a digital clock generation configuration"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (190 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        counter_channel_parameters: DigitalClockGenerationCounterChannelParameters,
        timing_parameters: DigitalClockGenerationTimingParameters,
    ) -> None:
        """Creates an instance of DigitalClockGenerationConfiguration

        Args:
            counter_channel_parameters (DigitalClockGenerationCounterChannelParameters): An
                instance of DigitalClockGenerationCounterChannelParameters
            timing_parameters (DigitalClockGenerationTimingParameters): An instance of
                DigitalClockGenerationTimingParameters
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(counter_channel_parameters, nameof(counter_channel_parameters))
        Guard.is_not_none(timing_parameters, nameof(timing_parameters))

        # assign values
        self._counter_channel_parameters = counter_channel_parameters
        self._timing_parameters = timing_parameters

    @property
    def counter_channel_parameters(
        self,
    ) -> DigitalClockGenerationCounterChannelParameters:
        """
        :type:DigitalClockGenerationCounterChannelParameters: An instance of
            DigitalClockGenerationCounterChannelParameters
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._counter_channel_parameters

    @property
    def timing_parameters(self) -> DigitalClockGenerationTimingParameters:
        """
        :type: DigitalClockGenerationTimingParameters: An instance of
            DigitalClockGenerationTimingParameters
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._timing_parameters


class DigitalClockGenerationData(PCBATestToolkitData):
    "Defines the data that was actually used during digital clock generation"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (188 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        timebase_frequency_hertz: float,
        actual_clock_frequency_hertz: float,
        actual_clock_duty_cycle_ratio: float,
        actual_clock_duration_seconds: float,
    ) -> None:
        """Creates an instance of DigitalClockGenerationData

        Args:
            timebase_frequency_hertz (float): The timebase used during generation
            actual_clock_frequency_hertz (float): Actual clock frequency used during generation
            actual_clock_duty_cycle_ratio (float): Actual duty cycle used during generation
            actual_clock_duration_seconds (float): Actual clock duration implemented in generation
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(timebase_frequency_hertz, nameof(timebase_frequency_hertz))
        Guard.is_greater_than_zero(timebase_frequency_hertz, nameof(timebase_frequency_hertz))

        Guard.is_not_none(actual_clock_frequency_hertz, nameof(actual_clock_frequency_hertz))
        Guard.is_greater_than_zero(
            actual_clock_frequency_hertz, nameof(actual_clock_frequency_hertz)
        )

        Guard.is_not_none(actual_clock_duty_cycle_ratio, nameof(actual_clock_duty_cycle_ratio))
        Guard.is_greater_than_or_equal_to_zero(
            actual_clock_duty_cycle_ratio, nameof(actual_clock_duty_cycle_ratio)
        )

        Guard.is_not_none(actual_clock_duration_seconds, nameof(actual_clock_duration_seconds))
        Guard.is_greater_than_or_equal_to_zero(
            actual_clock_duration_seconds, nameof(actual_clock_duration_seconds)
        )

        # assign values
        self._timebase_frequency_hertz = timebase_frequency_hertz
        self._actual_clock_frequency_hertz = actual_clock_frequency_hertz
        self._actual_clock_duty_cycle_ratio = actual_clock_duty_cycle_ratio
        self._actual_clock_duration_seconds = actual_clock_duration_seconds

    @property
    def timebase_frequency_hertz(self) -> float:
        """
        :type:float:
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._timebase_frequency_hertz

    @property
    def actual_clock_frequency_hertz(self) -> float:
        """
        :type:float
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._actual_clock_frequency_hertz

    @property
    def actual_clock_duty_cycle_ratio(self) -> float:
        """
        :type:float
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._actual_clock_duty_cycle_ratio

    @property
    def actual_clock_duration_seconds(self) -> float:
        """
        :type:float
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._actual_clock_duration_seconds
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_clock_generations/digital_clock_generation.py sha256=a3b106143846597cd4f56e648e1549fc0234e4156557e0664d317dd4714b257a bytes=8698 -->
## FILE: src/nipcbatt/pcbatt_library/daq/digital_clock_generations/digital_clock_generation.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/digital_clock_generations/digital_clock_generation.py`
- sha256: `a3b106143846597cd4f56e648e1549fc0234e4156557e0664d317dd4714b257a`
- bytes: 8698

````python
# pylint: disable=W0613
# remove it when arguments of initialize are used.
"""Use this class to generate a digital clock"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)

import nidaqmx.constants
import nidaqmx.stream_writers
from varname import nameof

from nipcbatt.pcbatt_library.daq.digital_clock_generations.digital_clock_constants import (
    ConstantsForDigitalClockGeneration,
)
from nipcbatt.pcbatt_library.daq.digital_clock_generations.digital_clock_data_types import (
    DigitalClockGenerationConfiguration,
    DigitalClockGenerationCounterChannelParameters,
    DigitalClockGenerationData,
    DigitalClockGenerationTimingParameters,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryException,
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard

# when class are defined in module change to
# from digital_clock_data_types import ...
# import digital_clock_data_types


class DigitalClockGeneration(BuildingBlockUsingDAQmx):
    """Used to output a digital clock to the hardware

    Args:
        BuildingBlockUsingDAQmx: Base class for all testscale modules
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)

    def initialize(
        self,
        counter_channel_expression: str,
        output_terminal_name: str,
    ):
        """_summary_

        Args:
            counter_channel_expression (str): Physical channel of counter to use
            output_terminal_name (str): Terminal on which the signal is measured
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        if self.is_task_initialized:
            return

        # input validation on channel expression and output terminal
        Guard.is_not_none(counter_channel_expression, nameof(counter_channel_expression))
        Guard.is_not_empty(counter_channel_expression, nameof(counter_channel_expression))
        Guard.is_not_none(output_terminal_name, nameof(output_terminal_name))
        Guard.is_not_empty(output_terminal_name, nameof(output_terminal_name))

        # constant used for initialization
        frequency_initial = ConstantsForDigitalClockGeneration.DEFAULT_GENERATION_FREQUENCY
        duty_cycle_initial = ConstantsForDigitalClockGeneration.DEFAULT_GENERATION_DUTY_CYCLE
        idle_state_initial = ConstantsForDigitalClockGeneration.DEFAULT_GENERATION_IDLE_STATE
        units_initial = ConstantsForDigitalClockGeneration.DEFAULT_FREQUENCY_GENERATION_UNIT

        # check to see if task has only global channels
        if self.contains_only_global_virtual_channels(counter_channel_expression):
            # add global channels to task
            self.add_global_channels(counter_channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)

        else:
            # create virtual channel for clock generation
            self.task.co_channels.add_co_pulse_chan_freq(
                counter=counter_channel_expression,
                units=units_initial,
                idle_state=idle_state_initial,
                freq=frequency_initial,
                duty_cycle=duty_cycle_initial,
            )

        # raise execption if more than one channel is present
        if self.task.number_of_channels and self.task.number_of_channels > 1:
            raise PCBATTLibraryException(
                PCBATTLibraryExceptionMessages.MORE_THAN_ONE_CHANNEL_INVALID
            )

        # set output terminal
        self.task.channels.co_pulse_term = output_terminal_name

        # reserve counter and terminal
        self.task.control(nidaqmx.constants.TaskMode.TASK_RESERVE)

    # submethods -- not visible to end users
    def configure_counter_channel(
        self, parameters: DigitalClockGenerationCounterChannelParameters
    ) -> None:
        """Configures the counter channel used for digital clock generation

        Args:
            parameters (DigitalClockGenerationCounterChannelParameters): An instance
            of DigitalClockGenerationCounterChannelParameters containg frequency
            and duty cycle data
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(parameters, nameof(parameters))

        self.task.stop()
        # set channel parameters
        self.task.channels.co_pulse_freq = parameters.frequency_hertz
        self.task.channels.co_pulse_duty_cyc = parameters.duty_cycle_ratio

    # sets the timing property of the task
    def configure_timing(self, parameters: DigitalClockGenerationTimingParameters) -> None:
        """Defines timing settings used in digital clock generation

        Args:
            parameters (DigitalClockGenerationTimingParameters): Contains
            duration settings used for generation
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        # input validation
        Guard.is_not_none(parameters, nameof(parameters))

        # calculate samples per channel -- step 1: extract frequency
        frequency = self.task.channels.co_pulse_freq

        # step 2 -- calculate number of samples
        num_samples = int(frequency * parameters.clock_duration_seconds)

        # set timing property
        finite_samples = ConstantsForDigitalClockGeneration.FINITE_SAMPLES
        self.task.timing.cfg_implicit_timing(sample_mode=finite_samples, samps_per_chan=num_samples)

    # writes the signal to hardware
    def generate(
        self, timing: DigitalClockGenerationTimingParameters
    ) -> DigitalClockGenerationData:
        """Starts the clock signal generation

        Returns:
            DigitalClockGenerationData: Contains the settings that
            were actually written to the instrument
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        self.task.start()
        # return written data
        data_out = DigitalClockGenerationData(
            timebase_frequency_hertz=self.task.channels.co_ctr_timebase_rate,
            actual_clock_frequency_hertz=self.task.channels.co_pulse_freq,
            actual_clock_duty_cycle_ratio=self.task.channels.co_pulse_duty_cyc,
            actual_clock_duration_seconds=timing.clock_duration_seconds,
        )

        return data_out

    def configure_and_generate(self, configuration: DigitalClockGenerationConfiguration):
        """Generates a digital clock to the hardware based on the configuration provided

        Args:
            configuration (DigitalClockGenerationConfiguration): A instance of
            DigitalClockGenerationConfiguration containing the settings to be used
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        # configure channel
        self.configure_counter_channel(configuration.counter_channel_parameters)

        # configure timing
        self.configure_timing(configuration.timing_parameters)

        # generate clock signal
        data = self.generate(configuration.timing_parameters)

        return data

    def close(self):
        """_summary_"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (134 > 100 characters) (auto-generated noqa)
        if not self.is_task_initialized:
            return

        self.task.wait_until_done()
        self.task.stop()
        self.task.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_edge_count_measurements/__init__.py sha256=564384e1f884b3d5476cc58cb66cd89b2bc1a2162761f24d60dbb6cdefcce8b6 bytes=244 -->
## FILE: src/nipcbatt/pcbatt_library/daq/digital_edge_count_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/digital_edge_count_measurements/__init__.py`
- sha256: `564384e1f884b3d5476cc58cb66cd89b2bc1a2162761f24d60dbb6cdefcce8b6`
- bytes: 244

````python
"""Provides nipcbatt library digital edge counting modules"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (172 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_edge_count_measurements/digital_edge_count_constants.py sha256=357b0d550427ea4e8b68bdf5b565274f7c8a9e4577406381ce9e68afd90035e3 bytes=1476 -->
## FILE: src/nipcbatt/pcbatt_library/daq/digital_edge_count_measurements/digital_edge_count_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/digital_edge_count_measurements/digital_edge_count_constants.py`
- sha256: `357b0d550427ea4e8b68bdf5b565274f7c8a9e4577406381ce9e68afd90035e3`
- bytes: 1476

````python
"Constants used in digital edge count measurement"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)

import dataclasses

import nidaqmx.constants

from nipcbatt.pcbatt_library.common.common_data_types import (  # noqa: F401 - 'nipcbatt.pcbatt_library.common.common_data_types.DigitalStartTriggerParameters' imported but unused (auto-generated noqa)
    DigitalStartTriggerParameters,
    StartTriggerType,
)


@dataclasses.dataclass
class ConstantsForDigitalEdgeCountMeasurement:
    """Constants used in digital edge count measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (169 > 100 characters) (auto-generated noqa)

    DEFAULT_INITIAL_COUNT = 0
    DEFAULT_COUNT_DIRECTION = nidaqmx.constants.CountDirection.COUNT_UP
    DEFAULT_EDGE = nidaqmx.constants.Edge.RISING

    DEFAULT_LOW_TIME = 0.000001
    DEFAULT_HIGH_TIME = 0.001
    DEFAULT_TIME_UNITS = nidaqmx.constants.TimeUnits.SECONDS
    DEFAULT_IDLE_STATE = nidaqmx.constants.Level.LOW

    DEFAULT_PAUSE_TRIGGER_TYPE = nidaqmx.constants.TriggerType.DIGITAL_LEVEL
    DEFAULT_PAUSE_DIGITAL_LEVEL_STATE = nidaqmx.constants.Level.LOW
    DEFAULT_TRIGGER_TIMEOUT = 10.0

    FINITE_SAMPLES = nidaqmx.constants.AcquisitionType.FINITE
    TIME_OUT = 10.0
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_edge_count_measurements/digital_edge_count_data_types.py sha256=102ba0c3ffbde20a3c8531524856636a5ac1e9a5b83e75b949362ac0458b2719 bytes=15235 -->
## FILE: src/nipcbatt/pcbatt_library/daq/digital_edge_count_measurements/digital_edge_count_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/digital_edge_count_measurements/digital_edge_count_data_types.py`
- sha256: `102ba0c3ffbde20a3c8531524856636a5ac1e9a5b83e75b949362ac0458b2719`
- bytes: 15235

````python
"""  digital edge count data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (149 > 100 characters) (auto-generated noqa)

import nidaqmx.constants
import numpy as np  # noqa: F401 - 'numpy as np' imported but unused (auto-generated noqa)
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
    MeasurementOptions,
)
from nipcbatt.pcbatt_library.daq.digital_edge_count_measurements.digital_edge_count_constants import (
    ConstantsForDigitalEdgeCountMeasurement,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DigitalEdgeCountMeasurementCounterChannelParameters(PCBATestToolkitData):
    """Defines the settings counter channel edge for measurement."""

    def __init__(
        self,
        edge_type: nidaqmx.constants.Edge = ConstantsForDigitalEdgeCountMeasurement.DEFAULT_EDGE,
    ) -> None:
        """Used to initialize an instance of `DigitalEdgeCountMeasurementCounterChannelParameters`.

        Args:
            edge_type (nidaqmx.constants.Edge): The `nidaqmx.constants.Edge` value that specifies on which edge
            of a digital pulse the counter increments.

        Raises:
            ValueError:
                if 'active_edge' is None.
        """  # noqa: W505 - doc line too long (111 > 100 characters) (auto-generated noqa)
        # Input validation
        Guard.is_not_none(edge_type, nameof(edge_type))

        self._edge_type = edge_type

    @property
    def edge_type(self) -> nidaqmx.constants.Edge:
        """Gets the edge type for counter."""
        return self._edge_type


class DigitalEdgeCountMeasurementTimingParameters(PCBATestToolkitData):
    """Defines the timing settings for edge count measurement."""

    def __init__(
        self,
        edge_counting_duration: float = 0.1,
    ) -> None:
        """Used to initialize an instance of `DigitalEdgeCountMeasurementTimingParameters`.

        Args:
            edge_counting_duration (float): The value that specifies the duration of edge count measurement.

        Raises:
            ValueError:
                if 'edge_counting_duration' is less than zero and None.
        """  # noqa: W505 - doc line too long (108 > 100 characters) (auto-generated noqa)
        # Input validation
        Guard.is_not_none(edge_counting_duration, nameof(edge_counting_duration))
        Guard.is_greater_than_or_equal_to_zero(
            edge_counting_duration, nameof(edge_counting_duration)
        )

        self._edge_counting_duration = edge_counting_duration

    @property
    def edge_counting_duration(self) -> float:
        """Gets the duration for edge count measurement."""
        return self._edge_counting_duration


class DigitalEdgeCountHardwareTimerConfiguration(PCBATestToolkitData):
    """Defines a configuration for hardware timer digital edge count measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (194 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        measurement_options: MeasurementOptions,
        counter_channel_parameters: DigitalEdgeCountMeasurementCounterChannelParameters,
        timing_parameters: DigitalEdgeCountMeasurementTimingParameters,
        trigger_parameters: DigitalStartTriggerParameters,
    ) -> None:
        """Initializes an instance of
        `DigitalEdgeCountHardwareTimerConfiguration`.

        Args:
            measurement_options (MeasurementOptions):
                The type of measurement options selected by user.
            counter_channel_parameters (DigitalEdgeCountMeasurementCounterChannelParameters):
                An instance of `DigitalEdgeCountMeasurementCounterChannelParameters` that represents the settings of edge_type.
            timing_parameters (DigitalEdgeCountMeasurementTimingParameters):
                An instance of 'DigitalEdgeCountMeasurementTimingParameters' that represents the duration of edge count measurement.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters` that represents the settings of triggers.

        Raises:
            ValueError:
                'measurement_options' is None,
                `counter_channel_parameters` is None,
                'timing_parameters' is None or less than zero,
                `trigger_parameters` is None,
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (127 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(measurement_options, nameof(measurement_options))
        Guard.is_not_none(counter_channel_parameters, nameof(counter_channel_parameters))
        Guard.is_not_none(timing_parameters, nameof(timing_parameters))
        Guard.is_not_none(trigger_parameters, nameof(trigger_parameters))

        self._measurement_options = measurement_options
        self._counter_channel_parameters = counter_channel_parameters
        self._timing_parameters = timing_parameters
        self._trigger_parameters = trigger_parameters

    @property
    def measurement_options(self) -> MeasurementOptions:
        """
        :class:`MeasurementExecutionType`:
            Gets the type of measurement execution selected by user.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._measurement_options

    @property
    def counter_channel_parameters(self) -> DigitalEdgeCountMeasurementCounterChannelParameters:
        """
        :class:`DigitalEdgeCountMeasurementCounterChannelParameters`:
            Gets a `DigitalEdgeCountMeasurementCounterChannelParameters` instance
            that represents the settings of edge_type to be counted.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._counter_channel_parameters

    @property
    def timing_parameters(self) -> DigitalEdgeCountMeasurementTimingParameters:
        """
        :class:`DigitalEdgeCountMeasurementTimingParameters`:
            Gets a `DigitalEdgeCountMeasurementTimingParameters` instance
            that represents the settings of the time duration in which number of edges to be counted.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (101 > 100 characters) (auto-generated noqa)
        return self._timing_parameters

    @property
    def trigger_parameters(self) -> DigitalStartTriggerParameters:
        """
        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._trigger_parameters


class DigitalEdgeCountSoftwareTimerConfiguration(PCBATestToolkitData):
    """Defines a configuration for software timer digital edge count measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (194 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        measurement_options: MeasurementOptions,
        counter_channel_parameters: DigitalEdgeCountMeasurementCounterChannelParameters,
        timing_parameters: DigitalEdgeCountMeasurementTimingParameters,
    ) -> None:
        """Initializes an instance of
        `DynamicDigitalPatternMeasurementConfiguration`.

        Args:
            measurement_options (MeasurementOptions):
                The type of measurement options selected by user.
            counter_channel_parameters (DigitalEdgeCountMeasurementCounterChannelParameters):
                An instance of `DigitalEdgeCountMeasurementCounterChannelParameters` that represents the settings of edge_type.
            timing_parameters (DigitalEdgeCountMeasurementTimingParameters):
                An instance of 'DigitalEdgeCountMeasurementTimingParameters' that represents the duration of edge count measurement.

        Raises:
            ValueError:
                'measurement_options' is None,
                `counter_channel_parameters` is None,
                'timing_parameters' is None or less than zero,
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (127 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(measurement_options, nameof(measurement_options))
        Guard.is_not_none(counter_channel_parameters, nameof(counter_channel_parameters))
        Guard.is_not_none(timing_parameters, nameof(timing_parameters))

        self._measurement_options = measurement_options
        self._counter_channel_parameters = counter_channel_parameters
        self._timing_parameters = timing_parameters

    @property
    def measurement_options(self) -> MeasurementOptions:
        """
        :class:`MeasurementExecutionType`:
            Gets the type of measurement execution selected by user.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._measurement_options

    @property
    def counter_channel_parameters(self) -> DigitalEdgeCountMeasurementCounterChannelParameters:
        """
        :class:`DigitalEdgeCountMeasurementCounterChannelParameters`:
            Gets a `DigitalEdgeCountMeasurementCounterChannelParameters` instance
            that represents the settings of edge_type to be counted.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._counter_channel_parameters

    @property
    def timing_parameters(self) -> DigitalEdgeCountMeasurementTimingParameters:
        """
        :class:`DigitalEdgeCountMeasurementTimingParameters`:
            Gets a `DigitalEdgeCountMeasurementTimingParameters` instance
            that represents the settings of the time duration in which number of edges to be counted.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (101 > 100 characters) (auto-generated noqa)
        return self._timing_parameters


class DigitalEdgeCountMeasurementResultData(PCBATestToolkitData):
    """Defines the values returned from the digital edge count measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (188 > 100 characters) (auto-generated noqa)

    def __init__(self, edge_count: int, edge_type: nidaqmx.constants.Edge) -> None:
        """Initializes an instance of 'DigitalEdgeCountMeasurementResultData'
        with specific values

        Args:
            edge_count: int
           edge_type: nidaqmx.constants.Edge

        Raises: ValueError when,
            1) edge_count is None
            2) edge_count is less than zero
            3) edge_type is None
        """  # noqa: D202, D205, D415, D417, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (363 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(edge_count, nameof(edge_count))
        Guard.is_greater_than_or_equal_to_zero(edge_count, nameof(edge_count))
        Guard.is_not_none(edge_type, nameof(edge_type))

        # assign to member variable
        self._edge_count = edge_count
        self._edge_type = edge_type

    @property
    def edge_count(self) -> int:
        """
        :type:'int': Edge count data captured from the measurement
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._edge_count

    @property
    def edge_type(self) -> nidaqmx.constants.Edge:
        """
        :type:'nidaqmx.constants.Edge': Data captured from the measurement
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._edge_type
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_edge_count_measurements/digital_edge_count_measurement_using_hardware_timer.py sha256=79a9f78f4033d86b13c111ef69e4677419f9c55bc1c67459e7edd29e54c6c4d4 bytes=12678 -->
## FILE: src/nipcbatt/pcbatt_library/daq/digital_edge_count_measurements/digital_edge_count_measurement_using_hardware_timer.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/digital_edge_count_measurements/digital_edge_count_measurement_using_hardware_timer.py`
- sha256: `79a9f78f4033d86b13c111ef69e4677419f9c55bc1c67459e7edd29e54c6c4d4`
- bytes: 12678

````python
"""Use this class to measure digital edge count using hardware timer"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (182 > 100 characters) (auto-generated noqa)

import re
from typing import Union

import nidaqmx.constants
import nidaqmx.stream_readers
import nidaqmx.stream_writers
import nidaqmx.system
import nidaqmx.system.device
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (  # noqa: F401 - 'nipcbatt.pcbatt_library.common.common_data_types.MeasurementData' imported but unused (auto-generated noqa)
    DigitalStartTriggerParameters,
    MeasurementData,
    MeasurementExecutionType,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.daq.digital_edge_count_measurements.digital_edge_count_constants import (
    ConstantsForDigitalEdgeCountMeasurement,
)
from nipcbatt.pcbatt_library.daq.digital_edge_count_measurements.digital_edge_count_data_types import (
    DigitalEdgeCountHardwareTimerConfiguration,
    DigitalEdgeCountMeasurementCounterChannelParameters,
    DigitalEdgeCountMeasurementResultData,
    DigitalEdgeCountMeasurementTimingParameters,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryException,
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DigitalEdgeCountMeasurementUsingHardwareTimer(BuildingBlockUsingDAQmx):
    """class for performing digital edge count measurement using hardware timer

    Args:
        BuildingBlockUsingDAQmx (_type_): Parent class for all PCBATT classes
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)

    # define class variable as there are two seperate tasks for counter and timer
    counter_task = nidaqmx.Task()
    timer_task = nidaqmx.Task()

    def initialize(
        self,
        measurement_channel_expression: str,
        measurement_input_terminal_name: str,
        timer_channel_expression: str,
    ) -> None:
        """Creates an instance of DigitalEdgeCountMeasurementUsingHardwareTimer class

        Args:
            measurement_channel_expression (str): specifies the counter resource needed for Edge counting operation.
            measurement_input_terminal_name (str): specifies the input terminal on which to look for digital events / edges.
            timer_channel_expression (str): specifies the counter resource needed for Timer task.
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (116 > 100 characters) (auto-generated noqa)
        if self.is_task_initialized:
            return

        # input validation

        Guard.is_not_none_nor_empty_nor_whitespace(
            measurement_channel_expression, nameof(measurement_channel_expression)
        )
        Guard.is_not_none_nor_empty_nor_whitespace(
            measurement_input_terminal_name, nameof(measurement_input_terminal_name)
        )
        Guard.is_not_none_nor_empty_nor_whitespace(
            timer_channel_expression, nameof(timer_channel_expression)
        )

        # constants used for Initialization of counter
        initial_count = ConstantsForDigitalEdgeCountMeasurement.DEFAULT_INITIAL_COUNT
        count_direction = ConstantsForDigitalEdgeCountMeasurement.DEFAULT_COUNT_DIRECTION
        edge = ConstantsForDigitalEdgeCountMeasurement.DEFAULT_EDGE

        # create virtual channel for Edge counting
        self.counter_task.ci_channels.add_ci_count_edges_chan(
            counter=measurement_channel_expression,
            edge=edge,
            initial_count=initial_count,
            count_direction=count_direction,
        )
        # raise exception if more than one channel is present
        if self.counter_task.number_of_channels > 1:
            raise PCBATTLibraryException(
                PCBATTLibraryExceptionMessages.MORE_THAN_ONE_CHANNEL_INVALID
            )

        # set input terminal
        self.counter_task.channels.ci_count_edges_term = measurement_input_terminal_name

        # reserve counter and terminal
        self.counter_task.control(nidaqmx.constants.TaskMode.TASK_RESERVE)

        # constatnts used for initializaton of timer
        units = ConstantsForDigitalEdgeCountMeasurement.DEFAULT_TIME_UNITS
        idle_state = ConstantsForDigitalEdgeCountMeasurement.DEFAULT_IDLE_STATE
        min_value = ConstantsForDigitalEdgeCountMeasurement.DEFAULT_LOW_TIME
        max_value = ConstantsForDigitalEdgeCountMeasurement.DEFAULT_HIGH_TIME

        # create virtual channel for timing
        self.timer_task.co_channels.add_co_pulse_chan_time(
            counter=timer_channel_expression,
            units=units,
            idle_state=idle_state,
            low_time=min_value,
            high_time=max_value,
        )

        # add code to get pulse internal treminal

        ctr_channel_number = re.findall(r"[0-9]+$", self.timer_task.channel_names[0])[0]
        daqmx_device_terminals = []

        for i in range(len(self.timer_task.devices)):
            daqmx_device_terminals.extend(self.timer_task.devices[i].terminals)

        for i in range(len(daqmx_device_terminals)):
            if bool(
                re.search("Ctr%sInternalOutput" % (ctr_channel_number), daqmx_device_terminals[i])
            ):
                internal_counter_terminal = daqmx_device_terminals[i]

        # set pulse internal terminal
        self.timer_task.channels.co_pulse_term = internal_counter_terminal

        # reserve timer and terminal
        self.timer_task.control(nidaqmx.constants.TaskMode.TASK_RESERVE)

    def configure_and_measure(
        self, configuration: DigitalEdgeCountHardwareTimerConfiguration
    ) -> Union[None, DigitalEdgeCountMeasurementResultData]:
        """Configures and/or performs a measurement
           according to specific configuration parameters.

        Args:
            configuration (DigitalEdgeCountHardwareTimerConfiguration):
            A instance of `DigitalEdgeCountHardwareTimerConfiguration` used to configure the measurement.

        Returns:
            DigitalEdgeCountMeasurementResultData | None: An instance of `DigitalEdgeCountMeasurementResultData`
            or `None` if no measure was performed.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (105 > 100 characters) (auto-generated noqa)

        if (
            configuration.measurement_options.execution_option
            == MeasurementExecutionType.CONFIGURE_AND_MEASURE
            or configuration.measurement_options.execution_option
            == MeasurementExecutionType.CONFIGURE_ONLY
        ):
            self.configure_counter_channel(
                DigitalEdgeCountMeasurementCounterChannelParameters(
                    configuration.counter_channel_parameters.edge_type
                )
            )
            self.configure_timing(
                DigitalEdgeCountMeasurementTimingParameters(
                    configuration.timing_parameters.edge_counting_duration
                )
            )
            self.configure_trigger(configuration.trigger_parameters)

        if (
            configuration.measurement_options.execution_option
            == MeasurementExecutionType.CONFIGURE_AND_MEASURE
            or configuration.measurement_options.execution_option
            == MeasurementExecutionType.MEASURE_ONLY
        ):
            return self.acquire_data_for_measurement_analysis()

        else:
            return None

    def configure_counter_channel(
        self, parameters: DigitalEdgeCountMeasurementCounterChannelParameters
    ):
        """Configures the counter channel parameter for digital edge count measurement.

        Args:
            parameters (DigitalEdgeCountMeasurementCounterChannelParameters):
            An instance of `DigitalEdgeCountMeasurementCounterChannelParameters` used to configure the counter channel parameter.
        """  # noqa: D417, W505 - Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (129 > 100 characters) (auto-generated noqa)
        self.counter_task.stop()
        self.counter_task.channels.ci_count_edges_active_edge = parameters.edge_type

    def configure_timing(self, parameters: DigitalEdgeCountMeasurementTimingParameters):
        """Configures the edge counting duration for digital edge count measurement.

        Args:
            parameters (DigitalEdgeCountMeasurementTimingParameters):
            An instance of `DigitalEdgeCountMeasurementTimingParameters` used to configure the edge count duration.
        """  # noqa: D417, W505 - Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (115 > 100 characters) (auto-generated noqa)
        self.timer_task.stop()
        self.counter_task.triggers.pause_trigger.trig_type = (
            ConstantsForDigitalEdgeCountMeasurement.DEFAULT_PAUSE_TRIGGER_TYPE
        )
        self.counter_task.triggers.pause_trigger.dig_lvl_src = (
            self.timer_task.channels.co_pulse_term
        )
        self.counter_task.triggers.pause_trigger.dig_lvl_when = (
            ConstantsForDigitalEdgeCountMeasurement.DEFAULT_PAUSE_DIGITAL_LEVEL_STATE
        )
        self.timer_task.channels.co_pulse_high_time = parameters.edge_counting_duration

    def configure_trigger(self, parameters: DigitalStartTriggerParameters):
        """Configure the characteristics of triggers used for digital edge count measurements.

        Args:
            parameters (DigitalStartTriggerParameters):
            An instance of `DigitalStartTriggerParameters` used to configure the channels.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        if parameters.trigger_select == StartTriggerType.NO_TRIGGER:
            self.timer_task.triggers.start_trigger.disable_start_trig()
        else:
            self.timer_task.triggers.start_trigger.cfg_dig_edge_start_trig(
                trigger_source=parameters.digital_start_trigger_source,
                trigger_edge=parameters.digital_start_trigger_edge,
            )

        self.counter_task.start()
        self.timer_task.start()

    def acquire_data_for_measurement_analysis(self):
        """Acquires Data from DAQ channel for measurement of digital edge count.

        Returns:
            DigitalEdgeCountMeasurementResultData:
            An instance of `DigitalEdgeCountMeasurementResultData` that specifies the data acquired from DAQ channels.
        """  # noqa: W505 - doc line too long (118 > 100 characters) (auto-generated noqa)
        time_out = (
            self.timer_task.channels.co_pulse_high_time
            + ConstantsForDigitalEdgeCountMeasurement.DEFAULT_TRIGGER_TIMEOUT
        )
        self.timer_task.wait_until_done(time_out)
        reader = nidaqmx.stream_readers.CounterReader(self.counter_task.in_stream)
        edge_count = reader.read_one_sample_uint32(
            timeout=ConstantsForDigitalEdgeCountMeasurement.TIME_OUT
        )
        edge_type = self.counter_task.channels.ci_count_edges_active_edge
        decm_result = DigitalEdgeCountMeasurementResultData(
            edge_count=edge_count, edge_type=edge_type
        )
        return decm_result

    def close(self):
        """Closes the task and returns the hardware resources"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (175 > 100 characters) (auto-generated noqa)
        if not self.is_task_initialized:
            return

        # stop and close DAQmx counter_task
        self.counter_task.stop()
        self.counter_task.close()

        # stop and close DAQmx timer_task
        self.timer_task.wait_until_done()
        self.timer_task.stop()
        self.timer_task.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_edge_count_measurements/digital_edge_count_measurement_using_software_timer.py sha256=3ba63f59766f5c019274c4215e6b4cc86ed4244385c3eec11feacfc1b9da25c7 bytes=9333 -->
## FILE: src/nipcbatt/pcbatt_library/daq/digital_edge_count_measurements/digital_edge_count_measurement_using_software_timer.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/digital_edge_count_measurements/digital_edge_count_measurement_using_software_timer.py`
- sha256: `3ba63f59766f5c019274c4215e6b4cc86ed4244385c3eec11feacfc1b9da25c7`
- bytes: 9333

````python
"""Use this class to measure digital edge count using software timer"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (182 > 100 characters) (auto-generated noqa)

import time
from typing import Union

import nidaqmx.constants
import nidaqmx.stream_readers
import nidaqmx.system
import numpy as np  # noqa: F401 - 'numpy as np' imported but unused (auto-generated noqa)
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (  # noqa: F401 - 'nipcbatt.pcbatt_library.common.common_data_types.MeasurementData' imported but unused (auto-generated noqa)
    MeasurementData,
    MeasurementExecutionType,
)
from nipcbatt.pcbatt_library.daq.digital_edge_count_measurements.digital_edge_count_constants import (
    ConstantsForDigitalEdgeCountMeasurement,
)
from nipcbatt.pcbatt_library.daq.digital_edge_count_measurements.digital_edge_count_data_types import (
    DigitalEdgeCountMeasurementCounterChannelParameters,
    DigitalEdgeCountMeasurementResultData,
    DigitalEdgeCountMeasurementTimingParameters,
    DigitalEdgeCountSoftwareTimerConfiguration,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryException,
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DigitalEdgeCountMeasurementUsingSoftwareTimer(BuildingBlockUsingDAQmx):
    """class for performing digital edge count measurement using software timer

    Args:
        BuildingBlockUsingDAQmx (_type_): Parent class for all PCBATT classes
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)

    def initialize(
        self,
        measurement_channel_expression: str,
        measurement_input_terminal_name: str,
    ) -> None:
        """Creates an instance of DigitalEdgeCountMeasurementUsingSoftwareTimer class

        Args:
            measurement_channel_expression (str): specifies the counter resource needed for Edge counting operation.
            measurement_input_terminal_name (str): specifies the input terminal on which to look for digital events/edges.
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (116 > 100 characters) (auto-generated noqa)
        if self.is_task_initialized:
            return
        # input validation

        Guard.is_not_none_nor_empty_nor_whitespace(
            measurement_channel_expression, nameof(measurement_channel_expression)
        )
        Guard.is_not_none_nor_empty_nor_whitespace(
            measurement_input_terminal_name, nameof(measurement_input_terminal_name)
        )

        # Constants used for Initialization of counter
        initial_count = ConstantsForDigitalEdgeCountMeasurement.DEFAULT_INITIAL_COUNT
        count_direction = ConstantsForDigitalEdgeCountMeasurement.DEFAULT_COUNT_DIRECTION
        edge = ConstantsForDigitalEdgeCountMeasurement.DEFAULT_EDGE

        # Create virtual channel for Edge counting
        self.task.ci_channels.add_ci_count_edges_chan(
            counter=measurement_channel_expression,
            edge=edge,
            initial_count=initial_count,
            count_direction=count_direction,
        )
        # Raise exception if more than one channel is present
        if self.task.number_of_channels > 1:
            raise PCBATTLibraryException(
                PCBATTLibraryExceptionMessages.MORE_THAN_ONE_CHANNEL_INVALID
            )

        # Set input terminal
        self.task.channels.ci_count_edges_term = measurement_input_terminal_name

        # Reserve counter and terminal
        self.task.control(nidaqmx.constants.TaskMode.TASK_RESERVE)

    def configure_and_measure(
        self, configuration: DigitalEdgeCountSoftwareTimerConfiguration
    ) -> Union[None, DigitalEdgeCountMeasurementResultData]:
        """Configures and/or performs a measurement
           according to specific configuration parameters.

        Args:
            configuration (DigitalEdgeCountSoftwareTimerConfiguration):
            A instance of `DigitalEdgeCountSoftwareTimerConfiguration` used to configure the measurement.

        Returns:
            DigitalEdgeCountMeasurementResultData | None: An instance of `DigitalEdgeCountMeasurementResultData`
            or `None` if no measure was performed.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (105 > 100 characters) (auto-generated noqa)

        if (
            configuration.measurement_options.execution_option
            == MeasurementExecutionType.CONFIGURE_AND_MEASURE
            or configuration.measurement_options.execution_option
            == MeasurementExecutionType.CONFIGURE_ONLY
        ):
            self.configure_counter_channel(
                DigitalEdgeCountMeasurementCounterChannelParameters(
                    configuration.counter_channel_parameters.edge_type,
                )
            )
            self.configure_timing(
                DigitalEdgeCountMeasurementTimingParameters(
                    configuration.timing_parameters.edge_counting_duration,
                )
            )

        if (
            configuration.measurement_options.execution_option
            == MeasurementExecutionType.CONFIGURE_AND_MEASURE
            or configuration.measurement_options.execution_option
            == MeasurementExecutionType.MEASURE_ONLY
        ):
            self.meas_option = configuration.measurement_options
            return self.acquire_data_for_measurement_analysis(configuration)

        else:
            return None

    def configure_counter_channel(
        self, parameters: DigitalEdgeCountMeasurementCounterChannelParameters
    ):
        """Configures the counter channel parameter for digital edge count measurement.

        Args:
            parameters (DigitalEdgeCountMeasurementCounterChannelParameters):
            An instance of `DigitalEdgeCountMeasurementCounterChannelParameters` used to configure the counter channel parameter.
        """  # noqa: D417, W505 - Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (129 > 100 characters) (auto-generated noqa)
        self.task.stop()
        self.task.channels.ci_count_edges_active_edge = parameters.edge_type
        self.task.start()

    def configure_timing(self, parameters: DigitalEdgeCountMeasurementTimingParameters):
        """Configures the edge counting duration for digital edge count measurement.

        Args:
            parameters (DigitalEdgeCountMeasurementTimingParameters):
            An instance of `DigitalEdgeCountMeasurementTimingParameters` used to configure the edge count duration.
        """  # noqa: D417, W505 - Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (115 > 100 characters) (auto-generated noqa)
        wait_delay = (  # noqa: F841 - local variable 'wait_delay' is assigned to but never used (auto-generated noqa)
            parameters.edge_counting_duration
        )

    def acquire_data_for_measurement_analysis(
        self, configuration: DigitalEdgeCountSoftwareTimerConfiguration
    ):
        """Acquires Data from DAQ channel for measurement of digital edge count.

        Returns:
            DigitalEdgeCountMeasurementResultData:
            An instance of `DigitalEdgeCountMeasurementResultData` that specifies the data acquired from DAQ channels.
        """  # noqa: W505 - doc line too long (118 > 100 characters) (auto-generated noqa)
        if (
            configuration.measurement_options.execution_option
            == MeasurementExecutionType.CONFIGURE_AND_MEASURE
        ):
            time.sleep(configuration.timing_parameters.edge_counting_duration)

        reader = nidaqmx.stream_readers.CounterReader(self.task.in_stream)
        edge_count = reader.read_one_sample_uint32(
            timeout=ConstantsForDigitalEdgeCountMeasurement.TIME_OUT
        )
        edge_type = self.task.channels.ci_count_edges_active_edge
        decm_result = DigitalEdgeCountMeasurementResultData(
            edge_count=edge_count, edge_type=edge_type
        )
        return decm_result

    def close(self):
        """Closes the task and returns the hardware resources"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (175 > 100 characters) (auto-generated noqa)
        if not self.is_task_initialized:
            return

        # stop and close DAQmx task
        self.task.stop()
        self.task.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_frequency_measurements/__init__.py sha256=4b184ac00e5aa6d0aa4c660c2d821fbea68fe18dfe21052c88cb3ab29c5c88ae bytes=252 -->
## FILE: src/nipcbatt/pcbatt_library/daq/digital_frequency_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/digital_frequency_measurements/__init__.py`
- sha256: `4b184ac00e5aa6d0aa4c660c2d821fbea68fe18dfe21052c88cb3ab29c5c88ae`
- bytes: 252

````python
"""Provides nipcbatt library digital frequency measurement modules"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (180 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_frequency_measurements/digital_frequency_constants.py sha256=f13d3419c8a0019a705e927dc520a304d1cfc31901578a58d3bad89f03091ac4 bytes=1022 -->
## FILE: src/nipcbatt/pcbatt_library/daq/digital_frequency_measurements/digital_frequency_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/digital_frequency_measurements/digital_frequency_constants.py`
- sha256: `f13d3419c8a0019a705e927dc520a304d1cfc31901578a58d3bad89f03091ac4`
- bytes: 1022

````python
"Constant datatypes for use in digital frequency measurement"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (172 > 100 characters) (auto-generated noqa)

import dataclasses

import nidaqmx.constants


@dataclasses.dataclass
class ConstantsForDigitalFrequencyMeasurement:
    "Constants used in digital frequency measurement"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (164 > 100 characters) (auto-generated noqa)
    DEFAULT_FREQUENCY_COUNTER_METHOD = (
        nidaqmx.constants.CounterFrequencyMethod.LARGE_RANGE_2_COUNTERS
    )
    DEFAULT_FREQUENCY_MEASURE_UNIT = nidaqmx.constants.FrequencyUnits.HZ
    DEFAULT_FREQUENCY_STARTING_EDGE = nidaqmx.constants.Edge.RISING
    DEFAULT_MEAS_TIME = 0.001
    DEFAULT_MIN_VALUE = 1.0
    DEFAULT_MAX_VALUE = 2.0e6
    DEFAULT_TIME_OUT = 10.0
    DEFAULT_INPUT_DIVISOR = 4
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_frequency_measurements/digital_frequency_data_types.py sha256=d4a620b7d51ecdb24036936a5808f184d5afd4d6f64c1bcb99a11fb2db55aba8 bytes=11705 -->
## FILE: src/nipcbatt/pcbatt_library/daq/digital_frequency_measurements/digital_frequency_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/digital_frequency_measurements/digital_frequency_data_types.py`
- sha256: `d4a620b7d51ecdb24036936a5808f184d5afd4d6f64c1bcb99a11fb2db55aba8`
- bytes: 11705

````python
""" Digital Frequency Measurement data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)

from varname import nameof

from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DigitalFrequencyRangeParameters(PCBATestToolkitData):
    """Defines the values used to establish the frequency range"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (177 > 100 characters) (auto-generated noqa)

    def __init__(
        self, frequency_minimum_value_hertz: float, frequency_maximum_value_hertz: float
    ) -> None:
        """Initializes an instance of 'DigitalFrequencyRangeParameters'
           with specific values

        Args:
            frequency_minimum_value_hertz (float):
                The minimum value in the frequency range
            frequency_maximum_vlaue_hertz (float):
                The maximum value in the frequency range

        Raises: ValueError when,
            1) The value of frequency_minimum_value_hertz is None or is <= 0
            2) The value of frequency_maximum_vlue_hertz is None or is <= 0
        """  # noqa: D202, D205, D415, D417, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (363 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(frequency_minimum_value_hertz, nameof(frequency_minimum_value_hertz))
        Guard.is_greater_than_or_equal_to_zero(
            frequency_minimum_value_hertz, nameof(frequency_minimum_value_hertz)
        )

        Guard.is_not_none(frequency_maximum_value_hertz, nameof(frequency_maximum_value_hertz))
        Guard.is_greater_than_or_equal_to_zero(
            frequency_maximum_value_hertz, nameof(frequency_maximum_value_hertz)
        )

        # minimum frequency <= maximum frequency
        Guard.is_less_than_or_equal_to(
            frequency_minimum_value_hertz,
            frequency_maximum_value_hertz,
            "minimum frequency <= maximum frequency",
        )

        # assign to member variables
        self._frequency_minimum_value_hertz = frequency_minimum_value_hertz
        self._frequency_maximum_value_hertz = frequency_maximum_value_hertz

    @property
    def frequency_minimum_value_hertz(self) -> float:
        """
        :type:'float': Gets the minimum frquency in the range
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._frequency_minimum_value_hertz

    @property
    def frequency_maximum_value_hertz(self) -> float:
        """
        :type:'float': Gets the maximum frquency in the range
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._frequency_maximum_value_hertz


class DigitalFrequencyMeasurementCounterChannelParameters(PCBATestToolkitData):
    """Defines the values for frequency counter channels"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (170 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        range_parameters: DigitalFrequencyRangeParameters,
        input_divisor_for_frequency_measurement: int,
        measurement_duration_seconds: float,
    ) -> None:
        """Initializes an instance of DigitalFrequencyMeasurementCounterChannelParameters

        Args:
            range_parameters (DigitalFrequencyRangeParameters): frequency range used in
              measurement. Defined by min frequency and max frequency.
            input_divisor_for_frequency_measurement (float): Divisor used for measurements
            measurement_duration_seconds (float): Length of capture

        Raises: ValueError when,
            1) The value of frequency_minimum_value_hertz is None or <= 0
            2) The value of frequency_maximum_value_hertz is None or <= 0
            3) The value of input_divisor_for_frequency_measurement is None or <= 4
            4) The value of measurement_duration_seconds is None or <= 0
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(range_parameters, nameof(range_parameters))

        Guard.is_not_none(
            input_divisor_for_frequency_measurement,
            nameof(input_divisor_for_frequency_measurement),
        )
        Guard.is_greater_than_or_equal_to(
            input_divisor_for_frequency_measurement,
            4,
            nameof(input_divisor_for_frequency_measurement),
        )

        Guard.is_not_none(measurement_duration_seconds, nameof(measurement_duration_seconds))
        Guard.is_greater_than_zero(
            measurement_duration_seconds, nameof(measurement_duration_seconds)
        )

        # set member variables
        self._range_parameters = range_parameters
        self._input_divisor_for_frequency_measurement = input_divisor_for_frequency_measurement
        self._measurement_duration_seconds = measurement_duration_seconds

    @property
    def range_parameters(self) -> DigitalFrequencyRangeParameters:
        """
        :type:'DigitalFrequencyRangeParameters': Holds the frequency range
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._range_parameters

    @property
    def input_divisor_for_frequency_measurement(self) -> int:
        """
        :type:'int': The divisor used for measuring frequency
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._input_divisor_for_frequency_measurement

    @property
    def measurement_duration_seconds(self) -> float:
        """
        :type:'float': The duration of the measurement in seconds
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._measurement_duration_seconds


class DigitalFrequencyMeasurementConfiguration(PCBATestToolkitData):
    """Defines the values used in the creation of a Digital Frequency Measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (195 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        counter_channel_configuration_parameters: DigitalFrequencyMeasurementCounterChannelParameters,
    ) -> None:
        """Initializes an instance of 'DigitalFrequencyMeasurementConfiguration'
           with specific values

        Args:
            configuration_parameters: An instance of
            'DigitalFrequencyMeasurementCounterChannelParameters'

        Raises: ValueError when,
            1) The value of configuration_parameters is None
        """  # noqa: D202, D205, D415, D417, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (363 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(
            counter_channel_configuration_parameters,
            nameof(counter_channel_configuration_parameters),
        )

        # assign member variables
        self._configuration_parameters = counter_channel_configuration_parameters

    @property
    def counter_channel_configuration_parameters(
        self,
    ) -> DigitalFrequencyMeasurementCounterChannelParameters:
        """
        :type:'DigitalFrequencyMeasurementCounterChannelParameters': Holds the
        configuration parameters used for this measurement
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._configuration_parameters


class DigitalFrequencyMeasurementResultData:
    """Defines the values inside a digital frequency result"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

    def __init__(self, frequency: float):
        """Instantiates a DigitalFrequencyMeasurementResultData object
           with the value provided in the frequency argument

        Args:
            frequency (float): The measured digital frequency

        Raises:
            ValueError when the frequency is None or <= 0
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(frequency, nameof(frequency))
        Guard.is_greater_than_or_equal_to_zero(frequency, nameof(frequency))

        # set member variable
        self._frequency = frequency

    @property
    def frequency(self) -> float:
        """
        :type:'float': The frequency captured in the measurement
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._frequency
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_frequency_measurements/digital_frequency_measurement.py sha256=cc2201bb3b712e92000679e7024daa93e5749eac9414561bf59672db5af18ef0 bytes=8103 -->
## FILE: src/nipcbatt/pcbatt_library/daq/digital_frequency_measurements/digital_frequency_measurement.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/digital_frequency_measurements/digital_frequency_measurement.py`
- sha256: `cc2201bb3b712e92000679e7024daa93e5749eac9414561bf59672db5af18ef0`
- bytes: 8103

````python
# pylint: disable=W0613
# remove it when arguments of initialize are used.
"""Defines class used for digital frequency measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (169 > 100 characters) (auto-generated noqa)

import nidaqmx.constants
import nidaqmx.stream_readers
from varname import nameof

from nipcbatt.pcbatt_library.daq.digital_frequency_measurements.digital_frequency_constants import (
    ConstantsForDigitalFrequencyMeasurement,
)
from nipcbatt.pcbatt_library.daq.digital_frequency_measurements.digital_frequency_data_types import (
    DigitalFrequencyMeasurementConfiguration,
    DigitalFrequencyMeasurementCounterChannelParameters,
    DigitalFrequencyMeasurementResultData,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryException,
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DigitalFrequencyMeasurement(BuildingBlockUsingDAQmx):
    """This class is used to perform digital frequency meausrements
    Args:
        BuildingBlockUsingDAQmx: Parent class for all modules
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def initialize(
        self,
        channel_expression: str,
        input_terminal_name: str,
    ):
        """Creates a DigitalFrequencyMeasurement object with the
           given arguments

        Args:
            channel_expression (str): Channels to acquire
            input_terminal_name (str): Terminal to acquire
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        if self.is_task_initialized:
            return

        # input validation on channel expression and terminal
        Guard.is_not_none(channel_expression, nameof(channel_expression))
        Guard.is_not_empty(channel_expression, nameof(channel_expression))
        Guard.is_not_none(input_terminal_name, nameof(input_terminal_name))
        Guard.is_not_empty(input_terminal_name, nameof(input_terminal_name))

        # check to see if task has only global virtual channels
        if self.contains_only_global_virtual_channels(channel_expression):
            # add global channels to task
            self.add_global_channels(channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)

        else:
            # create virtual channel for counter input

            self.task.ci_channels.add_ci_freq_chan(
                counter=channel_expression,
                name_to_assign_to_channel="",
                min_val=ConstantsForDigitalFrequencyMeasurement.DEFAULT_MIN_VALUE,
                max_val=ConstantsForDigitalFrequencyMeasurement.DEFAULT_MAX_VALUE,
                units=ConstantsForDigitalFrequencyMeasurement.DEFAULT_FREQUENCY_MEASURE_UNIT,
                edge=ConstantsForDigitalFrequencyMeasurement.DEFAULT_FREQUENCY_STARTING_EDGE,
                meas_method=ConstantsForDigitalFrequencyMeasurement.DEFAULT_FREQUENCY_COUNTER_METHOD,
                meas_time=ConstantsForDigitalFrequencyMeasurement.DEFAULT_MEAS_TIME,
                divisor=ConstantsForDigitalFrequencyMeasurement.DEFAULT_INPUT_DIVISOR,
            )

        # raise exception if more than one channel is present
        if self.task.channel_names and len(self.task.channel_names) > 1:
            raise PCBATTLibraryException(
                PCBATTLibraryExceptionMessages.MORE_THAN_ONE_CHANNEL_INVALID
            )

        # set input terminal for frequency counter
        self.task.channels.ci_freq_term = input_terminal_name

        # reserve counter and input terminal
        self.task.control(nidaqmx.constants.TaskMode.TASK_RESERVE)

    def close(self):
        """Ends measurement process and releases internal resources"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (181 > 100 characters) (auto-generated noqa)
        if not self.is_task_initialized:
            return

        # Stop and close the DAQmx task
        self.task.stop()
        self.task.close()

    def configure_and_measure(self, configuration: DigitalFrequencyMeasurementConfiguration):
        """Configures and/or performs a digital frequency measurement
           according to specific configuration parameters.

        Args:
            configuration (DigitalFrequencyMeasurementConfiguration): An instance of
            `DigitalFrequencyMeasurementConfiguration` used to configure the measurement.

        Returns:
            DigitalFrequencyMeasurementResultData: An instance of
            `DigitalFrequencyMeasurementResultData`or `None` if no measure was performed.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self.configure_counter_channel(configuration.counter_channel_configuration_parameters)

        # extract frequency data
        digital_frequency = self.acquire_data_for_measurement_analysis()

        # return frequency data in DigitalFrequencyMeasurementResultData object
        # or implicitly return None if no measurement was performed
        if digital_frequency is not None:
            return DigitalFrequencyMeasurementResultData(digital_frequency)

    def configure_counter_channel(
        self, parameters: DigitalFrequencyMeasurementCounterChannelParameters
    ) -> None:
        """Configures a counter channel according to specific configuration parameters.

        Args:
        parameters (DigitalFrequencyMeasurementCounterChannelParameters): An instance of
            `DigitalFrequencyMeasurementCounterChannelParameters` used to configure the
             counter channel.
        """
        self.task.stop()

        # set parameters for measurement
        self.task.channels.ci_freq_meas_meth = (
            ConstantsForDigitalFrequencyMeasurement.DEFAULT_FREQUENCY_COUNTER_METHOD
        )
        self.task.channels.ci_max = parameters.range_parameters.frequency_maximum_value_hertz
        self.task.channels.ci_min = parameters.range_parameters.frequency_minimum_value_hertz

        self.task.channels.ci_freq_div = parameters.input_divisor_for_frequency_measurement

        self.task.channels.ci_freq_units = (
            ConstantsForDigitalFrequencyMeasurement.DEFAULT_FREQUENCY_MEASURE_UNIT
        )
        self.task.channels.ci_freq_starting_edge = (
            ConstantsForDigitalFrequencyMeasurement.DEFAULT_FREQUENCY_STARTING_EDGE
        )

        self.task.start()

    def acquire_data_for_measurement_analysis(self) -> float:
        """Acquires Data from DAQ channel for measurement of digital frequency.

        Args: None

        Returns:
            float: A digital frequency measurement result
        """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

        # create reader
        counter_reader = nidaqmx.stream_readers.CounterReader(self.task.in_stream)

        # read the data
        time_out = ConstantsForDigitalFrequencyMeasurement.DEFAULT_TIME_OUT
        digital_frequency = counter_reader.read_one_sample_double(time_out)

        return digital_frequency
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_pulse_generations/__init__.py sha256=d01143c914e5765011f961ef996df894f036a1ae0382792703eb55ff3b239112 bytes=247 -->
## FILE: src/nipcbatt/pcbatt_library/daq/digital_pulse_generations/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/digital_pulse_generations/__init__.py`
- sha256: `d01143c914e5765011f961ef996df894f036a1ae0382792703eb55ff3b239112`
- bytes: 247

````python
"""Provides nipcbatt library digital pulse generation modules"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (175 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_pulse_generations/digital_pulse_constants.py sha256=2cbc28187fef1c967b7c4d6c3c680685208ccf594b89011eb4beb0f713661f97 bytes=849 -->
## FILE: src/nipcbatt/pcbatt_library/daq/digital_pulse_generations/digital_pulse_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/digital_pulse_generations/digital_pulse_constants.py`
- sha256: `2cbc28187fef1c967b7c4d6c3c680685208ccf594b89011eb4beb0f713661f97`
- bytes: 849

````python
"Constants used in digital pulse generation"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (155 > 100 characters) (auto-generated noqa)

import dataclasses

import nidaqmx.constants


@dataclasses.dataclass
class ConstantsForDigitalPulseGeneration:
    """Constants used in digital pulse generation"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (163 > 100 characters) (auto-generated noqa)

    DEFAULT_GENERATION_IDLE_STATE = nidaqmx.constants.Level.LOW
    DEFAULT_FREQUENCY_GENERATION_UNIT = nidaqmx.constants.TimeUnits.SECONDS
    DEFAULT_LOW_TIME = 0.01
    DEFAULT_HIGH_TIME = 0.01
    FINITE_SAMPLES = nidaqmx.constants.AcquisitionType.FINITE
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_pulse_generations/digital_pulse_data_types.py sha256=e2b15f280700fddd7081dfbb37acaac7cd0b9ede54f30b9d5a17ce4682a1bfe8 bytes=12993 -->
## FILE: src/nipcbatt/pcbatt_library/daq/digital_pulse_generations/digital_pulse_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/digital_pulse_generations/digital_pulse_data_types.py`
- sha256: `e2b15f280700fddd7081dfbb37acaac7cd0b9ede54f30b9d5a17ce4682a1bfe8`
- bytes: 12993

````python
""" Digital pulse data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (143 > 100 characters) (auto-generated noqa)

import nidaqmx.constants
from varname import nameof

from nipcbatt.pcbatt_library.daq.digital_pulse_generations.digital_pulse_constants import (
    ConstantsForDigitalPulseGeneration,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DigitalPulseGenerationCounterChannelParameters(PCBATestToolkitData):
    """Defines the counter channel parameters used for digital pulse generation"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (193 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        pulse_idle_state: nidaqmx.constants.Level = ConstantsForDigitalPulseGeneration.DEFAULT_FREQUENCY_GENERATION_UNIT,
        low_time_seconds: float = 0.01,
        high_time_seconds: float = 0.01,
    ) -> None:
        """Creates an instance of DigitalPulseGenerationCounterChannelParameters

        Args:
            pulse_idle_state (Constant state): The intended idle state of the generation
            low_time_seconds (float): The intended duration of the low time of the pulse
            high_time_seconds (float): The intended duration of the high time of the pulse
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(pulse_idle_state, nameof(pulse_idle_state))

        Guard.is_not_none(low_time_seconds, nameof(low_time_seconds))
        Guard.is_greater_than_or_equal_to_zero(low_time_seconds, nameof(low_time_seconds))
        Guard.is_float(low_time_seconds, nameof(low_time_seconds))

        Guard.is_not_none(high_time_seconds, nameof(high_time_seconds))
        Guard.is_greater_than_or_equal_to_zero(high_time_seconds, nameof(high_time_seconds))
        Guard.is_float(high_time_seconds, nameof(high_time_seconds))

        # assign values
        self._pulse_idle_state = pulse_idle_state
        self._low_time_seconds = low_time_seconds
        self._high_time_seconds = high_time_seconds

    @property
    def pulse_idle_state(self) -> nidaqmx.constants.Level:
        """
        :type:'nidaqmx.constants.Level': The idle state of the pulse generation
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._pulse_idle_state

    @property
    def low_time_seconds(self) -> float:
        """
        :type:float: The low time of the pulse
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._low_time_seconds

    @property
    def high_time_seconds(self) -> float:
        """
        :type:float: The high time of the pulse
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._high_time_seconds


class DigitalPulseGenerationTimingParameters(PCBATestToolkitData):
    """Defines the pulses count used in digital pulse generation"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (178 > 100 characters) (auto-generated noqa)

    def __init__(self, pulses_count: int) -> None:
        """Creates an instance of DigitalPulseGenerationTimingParameters

        Args: pulses_count (int): The number of pulses to generate
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(pulses_count, nameof(pulses_count))
        Guard.is_greater_than_or_equal_to_zero(pulses_count, nameof(pulses_count))
        Guard.is_int(pulses_count, nameof(pulses_count))

        # assign values
        self._pulses_count = pulses_count

    @property
    def pulses_count(self) -> int:
        """
        :type:int: Gets the number of pulses to generate
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._pulses_count


class DigitalPulseGenerationConfiguration(PCBATestToolkitData):
    """Defines a configuration for digital pulse generation"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        counter_channel_parameters: DigitalPulseGenerationCounterChannelParameters,
        timing_parameters: DigitalPulseGenerationTimingParameters,
    ) -> None:
        """Creates an instance of DigitalPulseGenerationConfiguration

        Args:
            counter_channel_parameters:
                An valid instance of DigitalPulseGenerationCounterChannelParameters
            timing_parameters:
                An valid instance of DigitalPulseGenerationTimingParameters
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(counter_channel_parameters, nameof(counter_channel_parameters))
        Guard.is_not_none(timing_parameters, nameof(timing_parameters))

        # assign values
        self._counter_channel_parameters = counter_channel_parameters
        self._timing_parameters = timing_parameters

    @property
    def counter_channel_parameters(
        self,
    ) -> DigitalPulseGenerationCounterChannelParameters:
        """
        :type:DigitalPulseGenerationCounterChannelParameters: The instance of
            DigitalPulseGenerationCounterChannelParameters used for digital pulse generation
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._counter_channel_parameters

    @property
    def timing_parameters(self) -> DigitalPulseGenerationTimingParameters:
        """
        :type:DigitalPulseGenerationTimingParameters: The instance of
            DigitalPulseGenerationTimingParameters used for digital pulse generation
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._timing_parameters


class DigitalPulseGenerationData(PCBATestToolkitData):
    """Returns the values actually written to the hardware"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (172 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        timebase_frequency_hertz: float,
        actual_pulse_train_duration_seconds: float,
        actual_pulse_low_time_seconds: float,
        actual_pulse_high_time_seconds: float,
    ) -> None:
        """Creates an instance of DigitalPulseGenerationData"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (251 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(timebase_frequency_hertz, nameof(timebase_frequency_hertz))
        Guard.is_greater_than_or_equal_to_zero(
            timebase_frequency_hertz, nameof(timebase_frequency_hertz)
        )
        Guard.is_float(timebase_frequency_hertz, nameof(timebase_frequency_hertz))

        Guard.is_not_none(
            actual_pulse_train_duration_seconds,
            nameof(actual_pulse_train_duration_seconds),
        )
        Guard.is_greater_than_or_equal_to_zero(
            actual_pulse_train_duration_seconds,
            nameof(actual_pulse_train_duration_seconds),
        )
        Guard.is_float(
            actual_pulse_train_duration_seconds,
            nameof(actual_pulse_train_duration_seconds),
        )

        Guard.is_not_none(actual_pulse_low_time_seconds, nameof(actual_pulse_low_time_seconds))
        Guard.is_greater_than_or_equal_to_zero(
            actual_pulse_low_time_seconds, nameof(actual_pulse_low_time_seconds)
        )
        Guard.is_float(actual_pulse_low_time_seconds, nameof(actual_pulse_low_time_seconds))

        Guard.is_not_none(actual_pulse_high_time_seconds, nameof(actual_pulse_high_time_seconds))
        Guard.is_greater_than_or_equal_to_zero(
            actual_pulse_high_time_seconds, nameof(actual_pulse_high_time_seconds)
        )
        Guard.is_float(actual_pulse_high_time_seconds, nameof(actual_pulse_high_time_seconds))

        # assign values
        self._timebase_frequency_hertz = timebase_frequency_hertz
        self._actual_pulse_train_duration_seconds = actual_pulse_train_duration_seconds
        self._actual_pulse_low_time_seconds = actual_pulse_low_time_seconds
        self._actual_pulse_high_time_seconds = actual_pulse_high_time_seconds

    @property
    def timebase_frequency_hertz(self) -> float:
        """
        :type:float: The timebase frequecy used to generate the pulse(s)
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._timebase_frequency_hertz

    @property
    def actual_pulse_train_duration_seconds(self) -> float:
        """
        :type:float: The actual pulse train duration written to the hardware
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._actual_pulse_train_duration_seconds

    @property
    def actual_pulse_low_time_seconds(self) -> float:
        """
        :type:float: The actual pulse low time written to the hardware
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._actual_pulse_low_time_seconds

    @property
    def actual_pulse_high_time_seconds(self) -> float:
        """
        :type:float: The actual pulse high time written to the hardware
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._actual_pulse_high_time_seconds
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_pulse_generations/digital_pulse_generation.py sha256=e2468fdfefb97081dd788732fa3770de4e917d5f1f1818a083bba7e064ba996f bytes=8718 -->
## FILE: src/nipcbatt/pcbatt_library/daq/digital_pulse_generations/digital_pulse_generation.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/digital_pulse_generations/digital_pulse_generation.py`
- sha256: `e2468fdfefb97081dd788732fa3770de4e917d5f1f1818a083bba7e064ba996f`
- bytes: 8718

````python
# pylint: disable=W0613
# remove it when arguments of initialize are used.
"""Implementation of Digital Pulse Generation for TestScale and CompactDAQ"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (188 > 100 characters) (auto-generated noqa)

import nidaqmx.constants
import nidaqmx.stream_readers
import nidaqmx.stream_writers
from varname import nameof

from nipcbatt.pcbatt_library.daq.digital_pulse_generations.digital_pulse_constants import (
    ConstantsForDigitalPulseGeneration,
)
from nipcbatt.pcbatt_library.daq.digital_pulse_generations.digital_pulse_data_types import (
    DigitalPulseGenerationConfiguration,
    DigitalPulseGenerationCounterChannelParameters,
    DigitalPulseGenerationData,
    DigitalPulseGenerationTimingParameters,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryException,
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DigitalPulseGeneration(BuildingBlockUsingDAQmx):
    """Use this class for digital pulse generation

    Args:
        BuildingBlockUsingDAQmx (_type_): _description_
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)

    def initialize(
        self,
        channel_expression: str,
        output_terminal_name: str,
    ) -> None:
        """_summary_

        Args:
            channel_expression (str): Physical channel
            output_terminal_name (str): Channel to write
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        if self.is_task_initialized:
            return

        # Here implement initialization of task.
        Guard.is_not_none(channel_expression, nameof(channel_expression))
        Guard.is_not_empty(channel_expression, nameof(channel_expression))

        Guard.is_not_none(output_terminal_name, nameof(output_terminal_name))
        Guard.is_not_empty(output_terminal_name, nameof(output_terminal_name))

        # constants used for instantiation
        t_low = ConstantsForDigitalPulseGeneration.DEFAULT_LOW_TIME
        t_hi = ConstantsForDigitalPulseGeneration.DEFAULT_HIGH_TIME
        def_units = ConstantsForDigitalPulseGeneration.DEFAULT_FREQUENCY_GENERATION_UNIT
        def_idle_state = ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE

        # check to see if task has only global channels
        if self.contains_only_global_virtual_channels(channel_expression):
            # add global channels to task
            self.add_global_channels(channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)

        else:
            # create virtual channel for pulse generation
            self.task.co_channels.add_co_pulse_chan_time(
                counter=channel_expression,
                units=def_units,
                idle_state=def_idle_state,
                low_time=t_low,
                high_time=t_hi,
            )

        # raise exception if more than one channel is present
        if self.task.number_of_channels and self.task.number_of_channels > 1:
            raise PCBATTLibraryException(
                PCBATTLibraryExceptionMessages.MORE_THAN_ONE_CHANNEL_INVALID
            )

        # set output terminal
        self.task.channels.co_pulse_term = output_terminal_name

        # reserve counter and terminal
        self.task.control(nidaqmx.constants.TaskMode.TASK_RESERVE)

    def configure_counter_channel(
        self,
        parameters: DigitalPulseGenerationCounterChannelParameters,
    ) -> None:
        """Configuration of the digital channel used for pulse generations

        Args:
            parameters (DigitalPulseGenerationCounterChannelParameters): A valid instance
                of DigitalPulseGenerationCounterChannelParameters
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        # stop daq task and return it to previous state
        self.task.stop()

        # input validation
        Guard.is_not_none(parameters, nameof(parameters))

        # set channel parameters
        self.task.channels.co_pulse_low_time = parameters.low_time_seconds
        self.task.channels.co_pulse_high_time = parameters.high_time_seconds

    def configure_timing(self, parameters: DigitalPulseGenerationTimingParameters) -> None:
        """Configuration of pulse generation timing

        Args:
            parameters (DigitalPulseGenerationTimingParameters): A valid instance
                of DigitalPulseGenerationTimingParameters
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        # input validation
        Guard.is_not_none(parameters, nameof(parameters))

        # set timing configuration
        finite_samples = ConstantsForDigitalPulseGeneration.FINITE_SAMPLES
        self.task.timing.cfg_implicit_timing(
            sample_mode=finite_samples, samps_per_chan=parameters.pulses_count
        )

        self.task.start()

    def generate(
        self, parameters: DigitalPulseGenerationTimingParameters
    ) -> DigitalPulseGenerationData:
        """Generate digital pulse(s)

        Returns:
            DigitalPulseGenerationData: A valid instance of DigitalPulseGenerationData
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        # create stream writer
        # writer = nidaqmx.stream_writers.CounterWriter(
        #     task_out_stream=self.task.out_stream,
        #     auto_start=True
        # )

        # # write to hardware
        # writer.write_one_sample_pulse_time(
        #     high_time=self.task.channels.co_pulse_high_time,
        #     low_time=self.task.channels.co_pulse_low_time,
        #     timeout=10
        # )

        # compute generation time
        true_low_time = self.task.channels.co_pulse_low_time
        true_high_time = self.task.channels.co_pulse_high_time
        sum_time = true_low_time + true_high_time
        generation_time = sum_time * parameters.pulses_count

        # return written data
        data_out = DigitalPulseGenerationData(
            timebase_frequency_hertz=self.task.channels.co_ctr_timebase_rate,
            actual_pulse_train_duration_seconds=generation_time,
            actual_pulse_low_time_seconds=true_low_time,
            actual_pulse_high_time_seconds=true_high_time,
        )

        return data_out

    def configure_and_generate(
        self, configuration: DigitalPulseGenerationConfiguration
    ) -> DigitalPulseGenerationData:
        """Configuration of instruments and process to generation

        Args:
            configuration (DigitalPulseGenerationConfiguration): A valid instance
                of DigitalPulseGenerationConfiguration

        Returns:
            DigitalPulseGenerationData: The values written to hardware
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        self.configure_counter_channel(configuration.counter_channel_parameters)
        self.configure_timing(configuration.timing_parameters)

        return self.generate(configuration.timing_parameters)

    def close(self):
        """Stops and closes the DAQ task"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (154 > 100 characters) (auto-generated noqa)
        if not self.is_task_initialized:
            return

        self.task.wait_until_done()
        self.task.stop()
        self.task.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_pwm_measurements/__init__.py sha256=4828769712ba7cd1b60ff910243ce86d4fd1d49bf18f12fd1648a64330bba5c6 bytes=246 -->
## FILE: src/nipcbatt/pcbatt_library/daq/digital_pwm_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/digital_pwm_measurements/__init__.py`
- sha256: `4828769712ba7cd1b60ff910243ce86d4fd1d49bf18f12fd1648a64330bba5c6`
- bytes: 246

````python
"""Provides nipcbatt library digital pwm measurement modules"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (174 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_pwm_measurements/digital_pwm_constants.py sha256=e59e0b9aa075a33375a789fb2efedb60bdacb0d53f85ff7e2cc54373b69fde77 bytes=858 -->
## FILE: src/nipcbatt/pcbatt_library/daq/digital_pwm_measurements/digital_pwm_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/digital_pwm_measurements/digital_pwm_constants.py`
- sha256: `e59e0b9aa075a33375a789fb2efedb60bdacb0d53f85ff7e2cc54373b69fde77`
- bytes: 858

````python
"Constant datatypes for use in digital frequency measurement"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (172 > 100 characters) (auto-generated noqa)

import dataclasses

import nidaqmx.constants


@dataclasses.dataclass
class ConstantsForDigitalPwmMeasurement:
    "Constants used in digital pwm measurement"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (158 > 100 characters) (auto-generated noqa)
    DEFAULT_PWM_STARTING_EDGE = nidaqmx.constants.Edge.RISING
    DEFAULT_MIN_SEMIPERIOD = 20e-9
    DEFAULT_MAX_SEMIPERIOD = 42.949672
    DEFAULT_TIME_UNITS = nidaqmx.constants.TimeUnits.SECONDS
    FINITE_SAMPLES = nidaqmx.constants.AcquisitionType.FINITE
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_pwm_measurements/digital_pwm_data_types.py sha256=2c2b07b9b8018609da537534db3d38a6eb742398c4271ba05bff876f1683a36c bytes=20918 -->
## FILE: src/nipcbatt/pcbatt_library/daq/digital_pwm_measurements/digital_pwm_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/digital_pwm_measurements/digital_pwm_data_types.py`
- sha256: `2c2b07b9b8018609da537534db3d38a6eb742398c4271ba05bff876f1683a36c`
- bytes: 20918

````python
""" digital PWM data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (141 > 100 characters) (auto-generated noqa)

import nidaqmx.constants
import numpy as np
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
from nipcbatt.pcbatt_library.daq.digital_pwm_measurements.digital_pwm_constants import (
    ConstantsForDigitalPwmMeasurement,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DigitalPwmMeasurementRangeParameters(PCBATestToolkitData):
    """Defines the range between minimum and maximum pulse width"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (178 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        semi_period_minimum_value_seconds: float = 20e-9,
        semi_period_maximum_value_seconds: float = 42.949672,
    ) -> None:
        """Initializes an instance of 'DigitalPwmMeasurementRangeParameters'
           with the values provided in the arguments

        Args:
            semi_period_minimum_value_seconds (float):
                Minimum length of pwm semi-period
            semi_period_maximum_value_seconds (float):
                Maximum length of pwm semi-period

        Raises: ValueError when,
            1) The value of semi_period_minimum_value_seconds is less than or equal to zero
            2) The value of semi_period_maximum_value_seconds is less than or eqaul to zero
            3) semi_period_maximum_value_seconds < semi_period_minimum_value_seconds
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(
            semi_period_minimum_value_seconds, nameof(semi_period_minimum_value_seconds)
        )

        Guard.is_not_none(
            semi_period_maximum_value_seconds, nameof(semi_period_maximum_value_seconds)
        )

        Guard.is_less_than_or_equal_to(
            semi_period_minimum_value_seconds,
            semi_period_maximum_value_seconds,
            nameof(semi_period_minimum_value_seconds),
        )

        Guard.is_greater_than_or_equal_to_zero(
            semi_period_minimum_value_seconds, nameof(semi_period_minimum_value_seconds)
        )

        Guard.is_greater_than_or_equal_to_zero(
            semi_period_maximum_value_seconds, nameof(semi_period_maximum_value_seconds)
        )

        # assign member variables
        self._semi_period_minimum_value_seconds = semi_period_minimum_value_seconds
        self._semi_period_maximum_value_seconds = semi_period_maximum_value_seconds

    @property
    def semi_period_minimum_value_seconds(self) -> float:
        """
        :type:'float': Gets the minimum semi period value in seconds
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._semi_period_minimum_value_seconds

    @property
    def semi_period_maximum_value_seconds(self) -> float:
        """
        :type:'float': Gets the minimum semi period value in seconds
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._semi_period_maximum_value_seconds


class DigitalPwmMeasurementTimingParameters(PCBATestToolkitData):
    """Defines the desired number of cycles to capture"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (168 > 100 characters) (auto-generated noqa)

    def __init__(self, semi_period_counter_wanted_cycles_count: int = 2) -> None:
        """Initializes an instance of 'DigitalPwmMeasurementTimingParameters'
           with the values provided in the arguments

        Args:
            semi_period_counter_wanted_cycles_count(int):
                The desired number of cycles to capture

        Raises: ValueError when,
            1) The value of semi_period_counter_wanted_cycles_count is less than zero
            2) The value of semi_period_maximum_value_seconds is more than 2147483647
            3) The value of semi_period_counter_wanted_cycles_count does not exist (null)
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(
            semi_period_counter_wanted_cycles_count,
            nameof(semi_period_counter_wanted_cycles_count),
        )

        Guard.is_greater_than_or_equal_to_zero(
            semi_period_counter_wanted_cycles_count,
            nameof(semi_period_counter_wanted_cycles_count),
        )

        Guard.is_less_than_or_equal_to(
            semi_period_counter_wanted_cycles_count,
            2147483647,
            nameof(semi_period_counter_wanted_cycles_count),
        )

        # assign member variable
        self._semi_period_counter_wanted_cycles_count = semi_period_counter_wanted_cycles_count

    @property
    def semi_period_counter_wanted_cycles_count(self) -> int:
        """
        :type:'int': Gets the desired number of cycles to capture
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._semi_period_counter_wanted_cycles_count


class DigitalPwmMeasurementCounterChannelParameters(PCBATestToolkitData):
    """Holds all of the parameters for creating a PWM measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (179 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        range_parameters: DigitalPwmMeasurementRangeParameters,
        timing_parameters: DigitalPwmMeasurementTimingParameters,
        semi_period_counter_starting_edge: nidaqmx.constants.Edge = ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE,
    ) -> None:
        """Initializes an instance of 'DigitalPwmMeasurementCounterChannelParameters'
           with the values provided in the arguments

        Args:
            range_parameters(DigitalPwmMeasurementRangeParameters):
                An instance of DigitalPwmMeasurementRangeParameters
            timing_parameters(DigitalPwmMeasurementTimingParameters):
                An instance of DigitalPwmMeasurementTimingParameters
            semi_period_counter_starting_edge:
                Constant value representing the starting edge

        Raises: ValueError when,
            1) The value of range_parameters is None
            2) The value of timing_parameters is None
            3) The value of semi_period_counter_starting_edge is None"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (442 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(range_parameters, nameof(range_parameters))
        Guard.is_not_none(timing_parameters, nameof(timing_parameters))
        Guard.is_not_none(
            semi_period_counter_starting_edge, nameof(semi_period_counter_starting_edge)
        )

        # assign member variables
        self._range_parameters = range_parameters
        self._timing_parameters = timing_parameters
        self._semi_period_counter_starting_edge = semi_period_counter_starting_edge

    @property
    def range_parameters(self) -> DigitalPwmMeasurementRangeParameters:
        """
        :type:DigitalPwmMeasurementRangeParamters: The range parameters of the measurement
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._range_parameters

    @property
    def timing_parameters(self) -> DigitalPwmMeasurementTimingParameters:
        """
        :type:DigitalPwmMeasurementTimingParameters: The timing parameters of the measurement
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._timing_parameters

    @property
    def semi_period_counter_starting_edge(self) -> int:
        """
        :type:Constant int:The starting edge for the measurement
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._semi_period_counter_starting_edge


class DigitalPwmMeasurementConfiguration(PCBATestToolkitData):
    """Defines values for the configuration of a digital pwm measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (186 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        parameters: DigitalPwmMeasurementCounterChannelParameters,
        measurement_option: MeasurementExecutionType = MeasurementExecutionType.CONFIGURE_AND_MEASURE,
    ) -> None:
        """Creates an instance of DigitalPwmMeasurementConfiguration

        Args:
            parameters (DigitalPwmMeasurementCounterChannelParameters):
                A valid instance of DigitalPwmMeasurementCounterChannelParameters
            measurement_options (MeasurementExecutionType):
                A valid instance of MeasurementExecutionType
        """  # noqa: D202, D415, D417, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (275 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(parameters, nameof(parameters))
        Guard.is_not_none(measurement_option, nameof(measurement_option))

        # assign to member properties
        self._parameters = parameters
        self._measurement_option = measurement_option

    @property
    def parameters(self) -> DigitalPwmMeasurementCounterChannelParameters:
        """
        :type:DigitalPwmMeasurementCounterChannelParameters: Contains data
        range and timing parameters
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._parameters

    @property
    def measurement_option(self) -> MeasurementExecutionType:
        """
        :type:MeasurmentExecutionType: Contains the type of execution
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._measurement_option


class DigitalPwmMeasurementData(PCBATestToolkitData):
    """Defines the values returned from the capture"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)

    def __init__(self, data: np.ndarray) -> None:
        """Initializes an instance of 'DigitalPwmMeasurementData'
        with specific values

        Args:
            data: Numpy ndarray

        Raises: ValueError when,
            1) data is empty
            2) data is None
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(data, nameof(data))
        Guard.is_not_empty(data, nameof(data))

        # assign to member variable
        self._data = data

    @property
    def data(self) -> np.ndarray:
        """
        :type:'numpy.ndarray': Data captured from the measurement
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._data


class DigitalPwmMeasurementResultData(PCBATestToolkitData):
    """Defines the values returned by a digital PWM measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (177 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        actual_cycles_count: int,
        duty_cycle: float,
        period_duration: float,
        frequency: float,
        high_state_duration: float,
        low_state_duration: float,
    ) -> None:
        """Initializes an instance of 'DigitalPwmMeasurementResultData'
           with specific values

        Args:
            actual_cycles_count (int):
                The actual number of cycles measured
            duty_cycle (float):
                The measured duty cycle within the pwm measurement
            period_duration(float):
                The length of each period
            frequency(float):
                The measured frequency
            high_state_duration(float):
                The length of the high state
            low_state_duration(float):
                The length of the low state

        Raises: ValueError when,
            1) The value of actual_cycles_count is None or is < 0
            2) The value of duty_cycle is None or is < 0
            3) The value of period duration is None or is < 0
            4) The value of frequency is None or is < 0
            5) The value of high_state_duration is None or is < 0
            6) THe value of low_state_duration is None or is < 0
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(actual_cycles_count, nameof(actual_cycles_count))
        Guard.is_greater_than_or_equal_to_zero(actual_cycles_count, nameof(actual_cycles_count))

        Guard.is_not_none(duty_cycle, nameof(duty_cycle))
        Guard.is_greater_than_or_equal_to_zero(duty_cycle, nameof(duty_cycle))
        Guard.is_less_than_or_equal_to(duty_cycle, 1.0, nameof(duty_cycle))

        Guard.is_not_none(period_duration, nameof(period_duration))
        Guard.is_greater_than_or_equal_to_zero(period_duration, nameof(period_duration))

        Guard.is_not_none(frequency, nameof(frequency))
        Guard.is_greater_than_or_equal_to_zero(frequency, nameof(frequency))

        Guard.is_not_none(high_state_duration, nameof(high_state_duration))
        Guard.is_greater_than_or_equal_to_zero(high_state_duration, nameof(high_state_duration))

        Guard.is_not_none(low_state_duration, nameof(low_state_duration))
        Guard.is_greater_than_or_equal_to_zero(low_state_duration, nameof(low_state_duration))

        # assign to member variables
        self._actual_cycles_count = actual_cycles_count
        self._duty_cycle = duty_cycle
        self._period_duration = period_duration
        self._frequency = frequency
        self._high_state_duration = high_state_duration
        self._low_state_duration = low_state_duration

    @property
    def actual_cycles_count(self) -> int:
        """
        :type:'int': Gets the number of cycles
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._actual_cycles_count

    @property
    def duty_cycle(self) -> float:
        """
        :type:'float': Gets the measured duty cycle
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._duty_cycle

    @property
    def period_duration(self) -> float:
        """
        :type:'float': Gets the length of the period
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._period_duration

    @property
    def frequency(self) -> float:
        """
        :type:'float': Gets the measured frequency
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._frequency

    @property
    def high_state_duration(self) -> float:
        """
        :type:'float': Gets the length of the high state
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._high_state_duration

    @property
    def low_state_duration(self) -> float:
        """
        :type:'float': Gets the length of the low state
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._low_state_duration
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/digital_pwm_measurements/digital_pwm_measurement.py sha256=34868e436b34a714e2914c559b372444919799874621470b96976301c79e6a82 bytes=13272 -->
## FILE: src/nipcbatt/pcbatt_library/daq/digital_pwm_measurements/digital_pwm_measurement.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/digital_pwm_measurements/digital_pwm_measurement.py`
- sha256: `34868e436b34a714e2914c559b372444919799874621470b96976301c79e6a82`
- bytes: 13272

````python
# pylint: disable=W0613
# remove it when arguments of initialize are used.
"""Use this class for digital pulse width modulation measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (178 > 100 characters) (auto-generated noqa)
import nidaqmx.constants
import nidaqmx.stream_readers
import nidaqmx.stream_writers
import numpy as np
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
from nipcbatt.pcbatt_library.daq.digital_pwm_measurements.digital_pwm_constants import (
    ConstantsForDigitalPwmMeasurement,
)
from nipcbatt.pcbatt_library.daq.digital_pwm_measurements.digital_pwm_data_types import (
    DigitalPwmMeasurementConfiguration,
    DigitalPwmMeasurementCounterChannelParameters,
    DigitalPwmMeasurementData,
    DigitalPwmMeasurementResultData,
    DigitalPwmMeasurementTimingParameters,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryException,
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard

# when class are defined in module change to
# from digital_pwm_data_types import ...


class DigitalPwmMeasurement(BuildingBlockUsingDAQmx):
    """Class for performing a digital pulse width modulation measurement

    Args:
        BuildingBlockUsingDAQmx (_type_): Parent class for all PCBATT classes
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)

    def initialize(
        self,
        channel_expression: str,
        input_terminal_name: str,
    ) -> None:
        """Creates an instance of the DigitalPwmMeasurement class

        Args:
            channel_expression (str): The physical channel being measured
            input_terminal_name (str): The name of the paticular input terminal
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        if self.is_task_initialized:
            return

        # Here implement initialization of task.
        # input validation on channel expression and terminal
        Guard.is_not_none(channel_expression, nameof(channel_expression))
        Guard.is_not_empty(channel_expression, nameof(channel_expression))
        Guard.is_not_none(input_terminal_name, nameof(input_terminal_name))
        Guard.is_not_empty(input_terminal_name, nameof(input_terminal_name))

        # constants used for initialization
        min_semiperiod = ConstantsForDigitalPwmMeasurement.DEFAULT_MIN_SEMIPERIOD
        max_semiperiod = ConstantsForDigitalPwmMeasurement.DEFAULT_MAX_SEMIPERIOD
        default_units = ConstantsForDigitalPwmMeasurement.DEFAULT_TIME_UNITS

        # check to see if task has only global channels
        if self.contains_only_global_virtual_channels(channel_expression):
            # add global channels to task
            self.add_global_channels(channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)

        else:
            # create virtual channel for clock generation
            self.task.ci_channels.add_ci_semi_period_chan(
                counter=channel_expression,
                name_to_assign_to_channel="",
                min_val=min_semiperiod,
                max_val=max_semiperiod,
                units=default_units,
            )

        # raise execption if more than one channel is present
        if self.task.number_of_channels and self.task.number_of_channels > 1:
            raise PCBATTLibraryException(
                PCBATTLibraryExceptionMessages.MORE_THAN_ONE_CHANNEL_INVALID
            )

        # set input terminal
        self.task.channels.ci_semi_period_term = input_terminal_name

        # reserve counter and terminal
        self.task.control(nidaqmx.constants.TaskMode.TASK_RESERVE)

    def configure_counter_channel(
        self, parameters: DigitalPwmMeasurementCounterChannelParameters
    ) -> None:
        """This method uses the semi_period values within the
            DigitalPwmMeasurementCounterChannelParameters argument provided to set
            the configuration for the counter channel

        Args:
            parameters (DigitalPwmMeasurementCounterChannelParameters):
                An instance of DigitalPwmMeasurementCounterChannelParameters
                with correct values
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # stop daq task and return it to previous state
        self.task.stop()

        # input validation
        Guard.is_not_none(parameters, nameof(parameters))

        # set channel parameters
        self.task.channels.ci_semi_period_starting_edge = (
            parameters.semi_period_counter_starting_edge
        )
        self.task.channels.ci_max = parameters.range_parameters.semi_period_maximum_value_seconds
        self.task.channels.ci_min = parameters.range_parameters.semi_period_minimum_value_seconds

    def configure_timing(self, parameters: DigitalPwmMeasurementTimingParameters) -> None:
        """This method uses the cycles count within the DigitalPwmMeasurementTimingParameters
            argument to set the value in the task

        Args:
            parameters (DigitalPwmMeasurementTimingParameters):
                An instance of DigitalPwmMeasurementTimingParameters containing
                a valid value for semi_period_wounter_wanted_cycles_count
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(parameters, nameof(parameters))

        # calculate # of semiperiods to read
        # Always last cycles will be ignored for the calculations as it does not have complete cycle info  # noqa: W505 - doc line too long (105 > 100 characters) (auto-generated noqa)
        semiperiods_to_read = 2 * parameters.semi_period_counter_wanted_cycles_count - 1

        # set timing task
        finite_samples = ConstantsForDigitalPwmMeasurement.FINITE_SAMPLES
        self.task.timing.cfg_implicit_timing(
            sample_mode=finite_samples, samps_per_chan=semiperiods_to_read
        )

        self.task.start()

    def acquire_data_for_measurement_analysis(self) -> DigitalPwmMeasurementData:
        """Acquires data from the hardware and prepares it for analysis

        Returns:
            DigitalPwmMeasurementData: Numpy array of data to be processed"""  # noqa: D202, D209, D414, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), Section has no content (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (411 > 100 characters) (auto-generated noqa)

        num_samples_per_channel = self.task.timing.samp_quant_samp_per_chan

        # preallocate memory for samples
        double_nparray = np.zeros(shape=(num_samples_per_channel,), dtype=np.double)

        # read the counter line and populate memory
        reader = nidaqmx.stream_readers.CounterReader(self.task.in_stream)
        reader.read_many_sample_double(
            data=double_nparray, number_of_samples_per_channel=num_samples_per_channel
        )

        # create DigitalPwmMeasurementData object out of read data and return
        pwm_data = DigitalPwmMeasurementData(double_nparray)
        return pwm_data

    def analyze_measurement_data(
        self, measurement_data: DigitalPwmMeasurementData
    ) -> DigitalPwmMeasurementResultData:
        """This method analyzes the input data and prepares a
           DigitalPwmMeasurementResultData object which contains
           all of the measurements of interest

        Args:
            measurement_data (DigitalPwmMeasurementData): An instance of
            DigitalPwmMeasurementData with valid data

        Returns:
            DigitalPwmMeasurementResultData: Contains the data of interest
            from the PWM measurement
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        meas_data = measurement_data.data
        half_data_length = len(meas_data) // 2

        # create arrays to hold high & low time data -- each w/ half the total samples
        low_time_data = np.zeros(
            shape=max(1, half_data_length),
        )
        high_time_data = np.zeros(
            shape=max(1, half_data_length),
        )

        # decimate original array
        for n in range(2 * half_data_length):
            sample = meas_data[n]
            if n % 2 == 0:
                high_time_data[n // 2] = sample
            else:
                low_time_data[n // 2] = sample

        # derive the average low time
        low_time = np.mean(low_time_data)

        # derive the average high time
        high_time = np.mean(high_time_data)

        # derive the average period from the sum of high time and low time
        sum_array = np.add(low_time_data, high_time_data)
        time_period = np.mean(sum_array)

        # guard time period to avoid divide by zero
        if time_period < ConstantsForDigitalPwmMeasurement.DEFAULT_MIN_SEMIPERIOD:
            time_period = ConstantsForDigitalPwmMeasurement.DEFAULT_MIN_SEMIPERIOD

        # calculate duty cycle
        duty_cyc = high_time / time_period

        # calculate frequency
        freq = 1 / time_period

        # create output object
        result_data = DigitalPwmMeasurementResultData(
            actual_cycles_count=half_data_length + 1,
            duty_cycle=duty_cyc,
            period_duration=time_period,
            frequency=freq,
            high_state_duration=high_time,
            low_state_duration=low_time,
        )

        return result_data

    def configure_and_measure(
        self, configuration: DigitalPwmMeasurementConfiguration
    ) -> DigitalPwmMeasurementResultData:
        """Main method to create and execute a digital pwm measurement

        Args:
            configuration (DigitalPwmMeasurementConfiguration): An instance
            of DigitalPwmMeasurementConfiguration

        Returns:
            DigitalPwmMeasurementResultData:
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        if (
            configuration.measurement_option == MeasurementExecutionType.CONFIGURE_AND_MEASURE
            or configuration.measurement_option == MeasurementExecutionType.CONFIGURE_ONLY
        ):
            self.configure_counter_channel(
                DigitalPwmMeasurementCounterChannelParameters(
                    range_parameters=configuration.parameters.range_parameters,
                    timing_parameters=configuration.parameters.timing_parameters,
                    semi_period_counter_starting_edge=configuration.parameters.semi_period_counter_starting_edge,
                )
            )

            self.configure_timing(configuration.parameters.timing_parameters)

        if (
            configuration.measurement_option == MeasurementExecutionType.CONFIGURE_AND_MEASURE
            or configuration.measurement_option == MeasurementExecutionType.MEASURE_ONLY
        ):
            data = self.acquire_data_for_measurement_analysis()
            return self.analyze_measurement_data(data)
        else:
            return None

    def close(self):
        """_summary_"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (134 > 100 characters) (auto-generated noqa)
        if not self.is_task_initialized:
            return

        self.task.stop()
        self.task.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_generations/__init__.py sha256=c95354e859c88343844d209a10db796df25bdde62cfe40f719131aae1f954082 bytes=257 -->
## FILE: src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_generations/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_generations/__init__.py`
- sha256: `c95354e859c88343844d209a10db796df25bdde62cfe40f719131aae1f954082`
- bytes: 257

````python
"""Provides nipcbatt library dynamic digital pattern generation modules"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (185 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_generations/dynamic_digital_pattern_constants.py sha256=bafc1b1538688cf7c22a24b852eb36ac9aa2020ba25fe32380391189ba87b700 bytes=799 -->
## FILE: src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_generations/dynamic_digital_pattern_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_generations/dynamic_digital_pattern_constants.py`
- sha256: `bafc1b1538688cf7c22a24b852eb36ac9aa2020ba25fe32380391189ba87b700`
- bytes: 799

````python
"Constants used in dynamic digital pattern generation"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)

import dataclasses

import nidaqmx.constants


@dataclasses.dataclass
class ConstantsForDynamicDigitalPatternGeneration:
    """Constants used for dynamic digital pattern generation"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (174 > 100 characters) (auto-generated noqa)

    FINITE_SAMPLES = nidaqmx.constants.AcquisitionType.FINITE
    DEFAULT_TRIGGER_EDGE = nidaqmx.constants.Edge.RISING
    DEFAULT_TRIGGER_TYPE = nidaqmx.constants.TriggerType.NONE
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_generations/dynamic_digital_pattern_data_types.py sha256=1ad3e8bc126a39d0ae45dcacb54ee8a0b3e412884522be8d2ef0a1fd462aced7 bytes=9195 -->
## FILE: src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_generations/dynamic_digital_pattern_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_generations/dynamic_digital_pattern_data_types.py`
- sha256: `1ad3e8bc126a39d0ae45dcacb54ee8a0b3e412884522be8d2ef0a1fd462aced7`
- bytes: 9195

````python
""" Dynamic digital pattern data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (153 > 100 characters) (auto-generated noqa)

import nidaqmx.constants
import numpy as np
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    DynamicDigitalPatternTimingParameters,
)
from nipcbatt.pcbatt_library.daq.dynamic_digital_pattern_generations.dynamic_digital_pattern_constants import (
    ConstantsForDynamicDigitalPatternGeneration,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DynamicDigitalStartTriggerParameters(PCBATestToolkitData):
    """Defines parameters for dynamic digital pattern trigger start"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (181 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        digital_start_trigger_source: str,
        digital_start_trigger_edge: nidaqmx.constants.Edge = ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE,
        trigger_type: nidaqmx.constants.TriggerType = ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_TYPE,
    ) -> None:
        """Creates an instance of DynamicDigitalStartTriggerParameters

        Args:
            digital_start_trigger_source (str): The phyiscal line to obtain the trigger
            digital_start_trigger_edge (nidaqmx.constants.Edge, optional): The edge on which to trigger.
                Defaults to ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE.
            trigger_type (nidaqmx.constants.TriggerType, optional): The type of trigger being used.
                Defaults to ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_TYPE.
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (104 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(digital_start_trigger_source, nameof(digital_start_trigger_source))
        Guard.is_not_empty(digital_start_trigger_source, nameof(digital_start_trigger_source))
        Guard.is_not_none(digital_start_trigger_edge, nameof(digital_start_trigger_edge))
        Guard.is_not_none(trigger_type, nameof(trigger_type))

        # assign values
        self._digital_start_trigger_source = digital_start_trigger_source
        self._digital_start_trigger_edge = digital_start_trigger_edge
        self._trigger_type = trigger_type

    @property
    def digital_start_trigger_source(self) -> str:
        """
        :type:str: The source of the digital start trigger
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._digital_start_trigger_source

    @property
    def digital_start_trigger_edge(self) -> nidaqmx.constants.Edge:
        """
        :type:nidaqmx.constants.Edge: The edge on which to trigger
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._digital_start_trigger_edge

    @property
    def trigger_type(self) -> nidaqmx.constants.TriggerType:
        """
        :type:nidaqmx.constants.TriggerType: The type of trigger used
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._trigger_type


class DynamicDigitalPatternGenerationData(PCBATestToolkitData):
    """Contains the data returned from dynamic digital pattern generation"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (187 > 100 characters) (auto-generated noqa)

    def __init__(self, generation_time_seconds: float) -> None:
        """Creates an instance of DynamicDigitalPatternGenerationData

        Args:
            generation_time_seconds (float): The length of the generation time in seconds
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(generation_time_seconds, nameof(generation_time_seconds))
        Guard.is_float(generation_time_seconds, nameof(generation_time_seconds))
        Guard.is_greater_than_or_equal_to_zero(
            generation_time_seconds, nameof(generation_time_seconds)
        )

        # assign values
        self._generation_time_seconds = generation_time_seconds

    @property
    def generation_time_seconds(self) -> float:
        """
        :type:float: The length of the generation time in seconds
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._generation_time_seconds


class DynamicDigitalPatternGenerationConfiguration(PCBATestToolkitData):
    """Contains the parameters for configuration of digital pattern generation"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (192 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        timing_parameters: DynamicDigitalPatternTimingParameters,
        digital_start_trigger_parameters: DynamicDigitalStartTriggerParameters,
        pulse_signal: np.ndarray,
    ) -> None:
        """Creates an instance of DynamicDigitalPatternGenerationConfiguration

        Args:
            timing_parameters (DynamicDigitalPatternTimingParameters): A valid instance
                of DynamicDigitalPatternTimingParameters
            digital_start_trigger_parameters (DynamicDigitalStartTriggerParameters): A
                valid instance of DynamicDigitalStartTriggerParameters
        """  # noqa: D202, D415, D417, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (275 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(timing_parameters, nameof(timing_parameters))
        Guard.is_not_none(
            digital_start_trigger_parameters, nameof(digital_start_trigger_parameters)
        )

        # assign values
        self._timing_parameters = timing_parameters
        self._digital_start_trigger_parameters = digital_start_trigger_parameters
        self._pulse_signal = pulse_signal

    @property
    def timing_parameters(self) -> DynamicDigitalPatternTimingParameters:
        """
        :type:DynamicDigitalPatternTimingParameters
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._timing_parameters

    @property
    def digital_start_trigger_parameters(self) -> DynamicDigitalStartTriggerParameters:
        """
        :type: DynamicDigitalStartTriggerParameters
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._digital_start_trigger_parameters

    @property
    def pulse_signal(self) -> np.ndarray:
        """
        :type: Numpy array
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._pulse_signal
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_generations/dynamic_digital_pattern_generation.py sha256=84a7f1170080b5b9959fe523f4808145c3582bc6ec47532e7ce76cf9d12ea96d bytes=8944 -->
## FILE: src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_generations/dynamic_digital_pattern_generation.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_generations/dynamic_digital_pattern_generation.py`
- sha256: `84a7f1170080b5b9959fe523f4808145c3582bc6ec47532e7ce76cf9d12ea96d`
- bytes: 8944

````python
# pylint: disable=W0613
# remove it when arguments of initialize are used.
""" _summary_ """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (128 > 100 characters) (auto-generated noqa)

import nidaqmx.constants
import nidaqmx.stream_writers
import numpy as np
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (  # noqa: F401 - 'nipcbatt.pcbatt_library.common.common_data_types.DigitalStartTriggerParameters' imported but unused (auto-generated noqa)
    DigitalStartTriggerParameters,
    DynamicDigitalPatternTimingParameters,
    SampleClockTimingParameters,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.daq.digital_pulse_generations.digital_pulse_data_types import (  # noqa: F401 - 'nipcbatt.pcbatt_library.digital_pulse_generations.digital_pulse_data_types.ConstantsForDigitalPulseGeneration' imported but unused (auto-generated noqa)
    ConstantsForDigitalPulseGeneration,
)
from nipcbatt.pcbatt_library.daq.dynamic_digital_pattern_generations.dynamic_digital_pattern_constants import (
    ConstantsForDynamicDigitalPatternGeneration,
)
from nipcbatt.pcbatt_library.daq.dynamic_digital_pattern_generations.dynamic_digital_pattern_data_types import (
    DynamicDigitalPatternGenerationConfiguration,
    DynamicDigitalPatternGenerationData,
    DynamicDigitalStartTriggerParameters,
)
from nipcbatt.pcbatt_library.daq.synchronizations.synchronization_signal_routing import (
    SynchronizationSignalRouting,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import (  # noqa: F401 - 'nipcbatt.pcbatt_library_core.pcbatt_data_types.PCBATestToolkitData' imported but unused (auto-generated noqa)
    PCBATestToolkitData,
)
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryException,
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard

# when class are defined in module change to
# from dynamic_digital_pattern_data_types import ...


class DynamicDigitalPatternGeneration(SynchronizationSignalRouting):
    """Use this class to generate dynamic digital patterns"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (172 > 100 characters) (auto-generated noqa)

    def initialize(self, channel_expression: str):
        """Initializes a dynamic digital pattern generation sequence

        Args:
            channel_expression (str): The channel to generate on
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        # self.task.stop()

        if self.is_task_initialized:
            return

        # input validation
        Guard.is_not_none(channel_expression, nameof(channel_expression))
        Guard.is_not_empty(channel_expression, nameof(channel_expression))

        # check to see if task has only global virtual channels
        if self.contains_only_global_virtual_channels(channel_expression):
            # add global channels to task
            self.add_global_channels(channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)

            # check task for number of devices
            # device count > 2 indicates multiple modules are present
            if self.task.number_of_devices > 2:
                # notify user of error and modules listed
                raise PCBATTLibraryException(
                    PCBATTLibraryExceptionMessages.GLOBAL_CHANNEL_TOO_MANY_MODULES_ARGS_1.format(
                        self.task.devices
                    )
                )

        else:
            # create digital output task
            self.task.do_channels.add_do_chan(channel_expression)

            # reserve resources for task
            self.task.control(nidaqmx.constants.TaskMode.TASK_RESERVE)

    def configure_timing(self, parameters: DynamicDigitalPatternTimingParameters) -> None:
        """This method configures the timing of the generation

        Args:
            parameters (DynamicDigitalPatternTimingParameters): A valid instance
                of DynamicDigitalPatternTimingParameters
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(parameters, nameof(parameters))

        # set timing for task
        finite_samples = ConstantsForDynamicDigitalPatternGeneration.FINITE_SAMPLES
        self.task.timing.cfg_samp_clk_timing(
            rate=parameters.sampling_rate_hertz,
            source=parameters.sample_clock_source,
            active_edge=parameters.active_edge,
            sample_mode=finite_samples,
            samps_per_chan=parameters.number_of_samples_per_channel,
        )

    def configure_trigger(self, parameters: DynamicDigitalStartTriggerParameters) -> None:
        """This method configures the trigger of the generation

        Args:
            parameters (DynamicDigitalStartTriggerParameters): A valid instance of
                DynamicDigitalStartTriggerParameters
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(parameters, nameof(parameters))

        # set trigger settings

        if parameters.trigger_type is not StartTriggerType.NO_TRIGGER:
            self.task.triggers.start_trigger.cfg_dig_edge_start_trig(
                trigger_source=parameters.digital_start_trigger_source,
                trigger_edge=parameters.digital_start_trigger_edge,
            )

    def generate(self, pulse_signal: np.ndarray) -> float:
        """Generates the dynamic digital pattern

        Args:
            pulse_signal (np.ndarray): Numpy array of (shape=(number_of_channels), dtype=numpy.uint32)

        Returns:
            float: The total generation time
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (102 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(pulse_signal, nameof(pulse_signal))
        Guard.is_not_empty(pulse_signal, nameof(pulse_signal))

        # write data
        writer = nidaqmx.stream_writers.DigitalMultiChannelWriter(self.task.out_stream)
        writer.write_many_sample_port_uint32(pulse_signal)

        # calculate generation time
        sample_rate = self.task.timing.samp_clk_rate

        if len(pulse_signal.shape) == 1:
            num_samples = pulse_signal.shape[0]
        else:
            num_samples = pulse_signal.shape[1]

        generation_time = num_samples / sample_rate

        return generation_time

    def configure_and_generate(
        self,
        configuration: DynamicDigitalPatternGenerationConfiguration,
    ) -> DynamicDigitalPatternGenerationData:
        """_summary_

        Args:
            configuration (DynamicDigitalPatternGenerationConfiguration): An
                instance of DynamicDigitalPatternGenerationConfiguration

        Returns:
            An instance of DynamicDigitalPatternGenerationData
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        self.task.stop()
        self.configure_timing(configuration.timing_parameters)
        self.configure_trigger(configuration.digital_start_trigger_parameters)

        generation_time = self.generate(configuration.pulse_signal)
        data_out = DynamicDigitalPatternGenerationData(generation_time)
        self.task.start()

        return data_out

    def close(self):
        """_summary_"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (134 > 100 characters) (auto-generated noqa)
        if not self.is_task_initialized:
            return
        self.task.wait_until_done()
        self.task.stop()
        self.task.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_measurements/__init__.py sha256=d8624084a9bcebdc4da76a5145e4e690f05214bbcc952a7ef7680e6de1a7f8ce bytes=258 -->
## FILE: src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_measurements/__init__.py`
- sha256: `d8624084a9bcebdc4da76a5145e4e690f05214bbcc952a7ef7680e6de1a7f8ce`
- bytes: 258

````python
"""Provides nipcbatt library dynamic digital pattern measurement modules"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (186 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_measurements/dynamic_digital_pattern_constants.py sha256=0daf2694b61942bd7577ff59b650df465ef1163f20195e4fa981aaf99938dda0 bytes=1346 -->
## FILE: src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_measurements/dynamic_digital_pattern_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_measurements/dynamic_digital_pattern_constants.py`
- sha256: `0daf2694b61942bd7577ff59b650df465ef1163f20195e4fa981aaf99938dda0`
- bytes: 1346

````python
"Constants used in dynamic digital pattern measurement"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (166 > 100 characters) (auto-generated noqa)

import dataclasses

import nidaqmx.constants

from nipcbatt.pcbatt_library.common.common_data_types import (  # noqa: F401 - 'nipcbatt.pcbatt_library.common.common_data_types.DigitalStartTriggerParameters' imported but unused (auto-generated noqa)
    DigitalStartTriggerParameters,
    StartTriggerType,
)


@dataclasses.dataclass
class ConstantsForDynamicDigitalPatternMeasurement:
    """Constants used in dynamic didgital pattern measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (175 > 100 characters) (auto-generated noqa)

    DEFAULT_SAMPLE_CLOCK_SOURCE = "OnboardClock"
    DEFAULT_SAMPLING_RATE_HERTZ = 10000
    DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL = 1000
    DEFAULT_ACTIVE_EDGE = nidaqmx.constants.Edge.RISING

    DEFAULT_TRIGGER_TYPE = StartTriggerType.NO_TRIGGER
    DEFAULT_DIGITAL_START_TRIGGER_SOURCE = ""
    DEFAULT_DIGITAL_START_TRIGGER_EDGE = nidaqmx.constants.Edge.RISING

    FINITE_SAMPLES = nidaqmx.constants.AcquisitionType.FINITE
    TIME_OUT = 10.0
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_measurements/dynamic_digital_pattern_data_types.py sha256=6823c3206b1fae1fc45641d1ef0cf6174a9827dd8d48af6ac180ca2a6581e2f2 bytes=7366 -->
## FILE: src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_measurements/dynamic_digital_pattern_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_measurements/dynamic_digital_pattern_data_types.py`
- sha256: `6823c3206b1fae1fc45641d1ef0cf6174a9827dd8d48af6ac180ca2a6581e2f2`
- bytes: 7366

````python
""" Dynamic digital pattern data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (153 > 100 characters) (auto-generated noqa)

import nidaqmx.constants  # noqa: F401 - 'nidaqmx.constants' imported but unused (auto-generated noqa)
import numpy as np
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
    DynamicDigitalPatternTimingParameters,
    MeasurementOptions,
)

from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DynamicDigitalPatternMeasurementConfiguration(PCBATestToolkitData):
    """Defines a configuration for dynamic digital pattern measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (184 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        measurement_options: MeasurementOptions,
        timing_parameters: DynamicDigitalPatternTimingParameters,
        trigger_parameters: DigitalStartTriggerParameters,
    ) -> None:
        """Initializes an instance of
        `DynamicDigitalPatternMeasurementConfiguration`.

        Args:
            measurement_options (MeasurementOptions):
                The type of measurement options selected by user.
            timing_parameters (DynamicDigitalPatternTimingParameters):
                An instance of `DynamicDigitalPatternTimingParameters` that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters` that represents the settings of triggers.

        Raises:
            ValueError:
                'measurement_options' is None,
                `timing_parameters` is None,
                `trigger_parameters` is None,
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (110 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(measurement_options, nameof(measurement_options))
        Guard.is_not_none(timing_parameters, nameof(timing_parameters))
        Guard.is_not_none(trigger_parameters, nameof(trigger_parameters))

        self._measurement_options = measurement_options
        self._timing_parameters = timing_parameters
        self._trigger_parameters = trigger_parameters

    @property
    def measurement_options(self) -> MeasurementOptions:
        """
        :class:`MeasurementExecutionType`:
            Gets the type of measurement execution selected by user.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._measurement_options

    @property
    def timing_parameters(self) -> DynamicDigitalPatternTimingParameters:
        """
        :class:`DynamicDigitalPatternTimingParameters`:
            Gets a `DynamicDigitalPatternTimingParameters` instance
            that represents the settings of timing.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._timing_parameters

    @property
    def trigger_parameters(self) -> DigitalStartTriggerParameters:
        """
        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._trigger_parameters


class DynamicDigitalPatternMeasurementResultData(PCBATestToolkitData):
    """Defines the values returned from the capture"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)

    def __init__(self, daq_digital_waveform_from_port: np.ndarray, waveforms: np.ndarray) -> None:
        """Initializes an instance of 'DynamicDigitalPatternMeasurementData'
        with specific values

        Args:
            daq_digital_waveform_from_port: Numpy ndarray
            waveforms: Numpy ndarray

        Raises: ValueError when,
            1) daq_digital_waveform_from_port is empty
            2) daq_digital_waveform_from_port is None
            3) waveforms is empty
            4) waveforms is none
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(daq_digital_waveform_from_port, nameof(daq_digital_waveform_from_port))
        Guard.is_not_empty(daq_digital_waveform_from_port, nameof(daq_digital_waveform_from_port))
        Guard.is_not_none(waveforms, nameof(waveforms))
        Guard.is_not_empty(waveforms, nameof(waveforms))

        # assign to member variable
        self._daq_digital_waveform_from_port = daq_digital_waveform_from_port
        self._waveforms = waveforms

    @property
    def daq_digital_waveform_from_port(self) -> np.ndarray:
        """
        :type:'numpy.ndarray': Data captured from the measurement
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._daq_digital_waveform_from_port

    @property
    def waveforms(self) -> np.ndarray:
        """
        :type:'numpy.ndarray': Data captured from the measurement
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._waveforms
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_measurements/dynamic_digital_pattern_measurement.py sha256=27c536662460d48296564dc055b42339d10688712c2e8e1ffeb93bd239ceee6a bytes=10814 -->
## FILE: src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_measurements/dynamic_digital_pattern_measurement.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/dynamic_digital_pattern_measurements/dynamic_digital_pattern_measurement.py`
- sha256: `27c536662460d48296564dc055b42339d10688712c2e8e1ffeb93bd239ceee6a`
- bytes: 10814

````python
"""Use this class to measure dynamic digital pattern from a system"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (180 > 100 characters) (auto-generated noqa)

import re
from typing import (  # noqa: F401 - 'typing.List' imported but unused (auto-generated noqa)
    List,
    Union,
)

import nidaqmx.constants
import nidaqmx.errors
import nidaqmx.stream_readers
import nidaqmx.stream_writers
import nidaqmx.system
import nidaqmx.system.storage
import numpy as np
from nidaqmx.constants import LineGrouping
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (  # noqa: F401 - 'nipcbatt.pcbatt_library.common.common_data_types.MeasurementAnalysisRequirement' imported but unused (auto-generated noqa)
    DigitalStartTriggerParameters,
    DynamicDigitalPatternTimingParameters,
    MeasurementAnalysisRequirement,
    MeasurementData,
    MeasurementExecutionType,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.daq.dynamic_digital_pattern_measurements.dynamic_digital_pattern_constants import (
    ConstantsForDynamicDigitalPatternMeasurement,
)
from nipcbatt.pcbatt_library.daq.dynamic_digital_pattern_measurements.dynamic_digital_pattern_data_types import (
    DynamicDigitalPatternMeasurementConfiguration,
    DynamicDigitalPatternMeasurementResultData,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryException,
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DynamicDigitalPatternMeasurement(BuildingBlockUsingDAQmx):
    """class for performing dynamic digital pattern measurement

    Args:
        BuildingBlockUsingDAQmx (_type_): Parent class for all PCBATT classes
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)

    def initialize(
        self,
        channel_expression: str,
    ) -> None:
        """Creates an instance of DynamicDigitalPatternMeasurement class

        Args:
            channel_expression (str): The name of the lines/port where the data will be measured
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        if self.is_task_initialized:
            return

        # input validation on channel expression
        Guard.is_not_none_nor_empty_nor_whitespace(channel_expression, nameof(channel_expression))

        # check to see if task has only global virtual channels
        if self.contains_only_global_virtual_channels(channel_expression):
            # add global channels to task
            self.add_global_channels(channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)

            # check task for number of devices
            # device count > 2 indicates multiple modules are present
            if self.task.number_of_devices > 2:
                # notify user of error and modules listed
                raise PCBATTLibraryException(
                    PCBATTLibraryExceptionMessages.GLOBAL_CHANNEL_TOO_MANY_MODULES_ARGS_1.format(
                        self.task.devices
                    )
                )

        else:
            # create one virtual channel for all Digital In line
            # for channel in channels:
            self.task.di_channels.add_di_chan(
                channel_expression, "", LineGrouping.CHAN_FOR_ALL_LINES
            )

        # reserve lines for the task
        self.task.control(nidaqmx.constants.TaskMode.TASK_RESERVE)

    def close(self):
        """Closes the task and returns the hardware resources"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (175 > 100 characters) (auto-generated noqa)
        if not self.is_task_initialized:
            return

        # stop and close DAQmx task
        self.task.stop()
        self.task.close()

    def configure_and_measure(
        self, configuration: DynamicDigitalPatternMeasurementConfiguration
    ) -> Union[None, DynamicDigitalPatternMeasurementResultData]:
        """Configures and/or performs a measurement
           according to specific configuration parameters.

        Args:
            configuration (DynamicDigitalPatternMeasurementConfiguration):
            A instance of `DynamicDigitalPatternMeasurementConfiguration` used to configure the measurement.

        Returns:
            DynamicDigitalPatternMeasurementResultData | None: An instance of `DynamicDigitalPatternMeasurementResultData`
            or `None` if no measure was performed.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (108 > 100 characters) (auto-generated noqa)
            
        exec_type = configuration.measurement_options
        if exec_type in(
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.CONFIGURE_ONLY
        ):
            self.configure_timing(configuration.timing_parameters)
            self.configure_trigger(configuration.trigger_parameters)

        if exec_type in(
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.MEASURE_ONLY
        ):
            data = self.acquire_data_for_measurement_analysis()

            return self.analyze_measurement_data(data)

        else:
            return None

    def configure_timing(self, parameters: DynamicDigitalPatternTimingParameters):
        """Configures the timing parameters for dynamic digital pattern measurement.

        Args:
            parameters (DynamicDigitalPatternTimingParameters):
            An instance of `DynamicDigitalPatternTimingParameters` used to configure the timing.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        self.task.stop()

        self.task.timing.cfg_samp_clk_timing(
            rate=parameters.sampling_rate_hertz,
            source=parameters.sample_clock_source,
            active_edge=parameters.active_edge,
            sample_mode=ConstantsForDynamicDigitalPatternMeasurement.FINITE_SAMPLES,
            samps_per_chan=parameters.number_of_samples_per_channel,
        )

    def configure_trigger(self, parameters: DigitalStartTriggerParameters):
        """Configure the characteristics of triggers used for dynamic digital pattern measurements.

        Args:
            parameters (DigitalStartTriggerParameters):
            An instance of `DigitalStartTriggerParameters` used to configure the channels.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        if parameters.trigger_select == StartTriggerType.NO_TRIGGER:
            self.task.triggers.start_trigger.disable_start_trig()
        else:
            self.task.triggers.start_trigger.cfg_dig_edge_start_trig(
                trigger_source=parameters.digital_start_trigger_source,
                trigger_edge=parameters.digital_start_trigger_edge,
            )

        self.task.start()

    def acquire_data_for_measurement_analysis(self):
        """Acquires Data from DAQ channel for measurement of dynamic digital pattern

        Returns:
            MeasurementData:
            An instance of `MeasurementData` that specifies the data acquired from DAQ channels.
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        number_of_channels = len(self.task.in_stream.channels_to_read.channel_names)
        number_of_samples_per_channel = self.task.timing.samp_quant_samp_per_chan
        data_to_read = np.zeros(
            shape=(number_of_channels, number_of_samples_per_channel),
            dtype=np.uint32,
        )
        reader = nidaqmx.stream_readers.DigitalMultiChannelReader(self.task.in_stream)
        reader.read_many_sample_port_uint32(
            number_of_samples_per_channel=number_of_samples_per_channel,
            timeout=ConstantsForDynamicDigitalPatternMeasurement.TIME_OUT,
            data=data_to_read,
        )

        return data_to_read

    def analyze_measurement_data(
        self,
        measurement_data: MeasurementData,
    ) -> DynamicDigitalPatternMeasurementResultData:
        """Proceeds to the analysis of Digital port data from the measurement.

        Args:
            measurement_data (MeasurementData):
            An instance of `MeasurementData`
            that specifies the data acquired from DAQ channels.

        Returns:
            DynamicDigitalPatternMeasurementResultData:
            An instance of `DynamicDigitalPatternMeasurementResultData`
            that specifies the measurement results.
        """
        port_data = measurement_data[0]
        digital_pattern_data = []

        for samples in port_data:
            data_byte = samples
            bit_stream = []
            for _ in range(32):
                bit_stream.append(data_byte % 2)
                data_byte = data_byte // 2
            digital_pattern_data.append(bit_stream)

        number_of_lines = 0
        for d_channel in self.task.di_channels:
            number_of_lines = number_of_lines + d_channel.di_num_lines

        input_string = d_channel.name

        match = re.search(r"line(\d+)", input_string)
        if match:
            result = match.group(1)
            number_int = int(result)
        else:
            number_int = 0

        digital_pattern_data = np.transpose(digital_pattern_data)
        digital_pattern_data = digital_pattern_data[
            (number_int) : (number_int + number_of_lines), 0 : len(port_data)
        ]
        daq_digital_waveform_from_port = port_data[0 : len(port_data)]
        return DynamicDigitalPatternMeasurementResultData(
            daq_digital_waveform_from_port,
            waveforms=np.array(digital_pattern_data, dtype=np.uint32),
        )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/frequency_domain_measurements/__init__.py sha256=0562f9d5756a654581b44e310d77d0b7183bb496209581657b9d39a540239bf2 bytes=251 -->
## FILE: src/nipcbatt/pcbatt_library/daq/frequency_domain_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/frequency_domain_measurements/__init__.py`
- sha256: `0562f9d5756a654581b44e310d77d0b7183bb496209581657b9d39a540239bf2`
- bytes: 251

````python
"""Provides nipcbatt library frequency domain measurement modules"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (179 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/frequency_domain_measurements/frequency_domain_constants.py sha256=32bbe1062c6449efab38cbb31fb561630bbdd9327b0be456bc0e0089b36a2311 bytes=4135 -->
## FILE: src/nipcbatt/pcbatt_library/daq/frequency_domain_measurements/frequency_domain_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/frequency_domain_measurements/frequency_domain_constants.py`
- sha256: `32bbe1062c6449efab38cbb31fb561630bbdd9327b0be456bc0e0089b36a2311`
- bytes: 4135

````python
""" Constants data types for Frequency domain Measurements."""

import dataclasses

from nipcbatt.pcbatt_analysis.waveform_analysis.frequency_domain_analysis import (
    LabViewFftSpectrumWindow,
    LabViewTonesSortingMode,
    SpectrumPhaseUnit,
)
from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
    MeasurementOptions,
    SampleClockTimingParameters,
)
from nipcbatt.pcbatt_library.daq.common.voltage_constants import (
    ConstantsForVoltageMeasurement,
)
from nipcbatt.pcbatt_library.daq.common.voltage_data_types import (
    VoltageRangeAndTerminalParameters,
)
from nipcbatt.pcbatt_library.daq.frequency_domain_measurements.frequency_domain_data_types import (
    FrequencyDomainMeasurementConfiguration,
)


@dataclasses.dataclass
class ConstantsForFrequencyDomainMeasurement:
    """Constants used for Frequency Domain measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (168 > 100 characters) (auto-generated noqa)

    FILTERING_WINDOW_FOR_FFT = LabViewFftSpectrumWindow.HANNING
    """Specifies the time-domain window to apply to the time signal before performing FFT.
    1- Hanning"""

    VIEW_RESULTS_dB_ON = True
    """Specifies whether the results are expressed in decibels"""

    VIEW_RESULTS_PHASE_UNIT = SpectrumPhaseUnit.RADIAN
    """Specifies whether the phase results are expressed as radians or degrees."""

    DEFAULT_THRESHOLD_FOR_TONE_EXTRACTION = 0.010
    """Specifies the minimum amplitude that each tone must exceed 
    for this VI to extract it from time signal in."""

    DEFAULT_MAX_NUMBER_OF_TONES_TO_BE_EXTRACTED = None
    """Specifies the maximum number of tones that this VI extracts. 
    If you set max num tones to `None`, 
    tones processor will extract all tones whose amplitude exceeds threshold."""

    DEFAULT_SORTING_ORDER_OF_THE_EXTRACTED_TONES = LabViewTonesSortingMode.INCREASING_FREQUENCIES
    """Specifies the sorting order of the tones that this VI extracts, 
    `increasing frequencies` or `decreasing amplitudes`"""


DEFAULT_FREQUENCY_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS = VoltageRangeAndTerminalParameters(
    terminal_configuration=ConstantsForVoltageMeasurement.DEFAULT_AI_TERMINAL_CONFIGURATION,
    range_min_volts=ConstantsForVoltageMeasurement.DEFAULT_VOLTAGE_MINIMUM_VALUE_VOLTS,
    range_max_volts=ConstantsForVoltageMeasurement.DEFAULT_VOLTAGE_MAXIMUM_VALUE_VOLTS,
)

DEFAULT_FREQUENCY_DOMAIN_MEASUREMENT_OPTIONS = MeasurementOptions(
    execution_option=ConstantsForVoltageMeasurement.DEFAULT_EXECUTION_TYPE,
    measurement_analysis_requirement=ConstantsForVoltageMeasurement.DEFAULT_MEASUREMENT_ANALYSIS_REQUIREMENT,
)

DEFAULT_FREQUENCY_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS = SampleClockTimingParameters(
    sample_clock_source=ConstantsForVoltageMeasurement.DEFAULT_SAMPLE_CLOCK_SOURCE,
    sampling_rate_hertz=ConstantsForVoltageMeasurement.DEFAULT_SAMPLING_RATE_HERTZ,
    number_of_samples_per_channel=ConstantsForVoltageMeasurement.DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL,
    sample_timing_engine=ConstantsForVoltageMeasurement.DEFAULT_SAMPLE_TIMING_ENGINE,
)

DEFAULT_FREQUENCY_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS = DigitalStartTriggerParameters(
    trigger_select=ConstantsForVoltageMeasurement.DEFAULT_TRIGGER_TYPE,
    digital_start_trigger_source=ConstantsForVoltageMeasurement.DEFAULT_DIGITAL_START_TRIGGER_SOURCE,
    digital_start_trigger_edge=ConstantsForVoltageMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE,
)

DEFAULT_FREQUENCY_DOMAIN_MEASUREMENT_CONFIGURATION = FrequencyDomainMeasurementConfiguration(
    global_channel_parameters=DEFAULT_FREQUENCY_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS,
    specific_channels_parameters=[],
    measurement_options=DEFAULT_FREQUENCY_DOMAIN_MEASUREMENT_OPTIONS,
    sample_clock_timing_parameters=DEFAULT_FREQUENCY_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS,
    digital_start_trigger_parameters=DEFAULT_FREQUENCY_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS,
)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/frequency_domain_measurements/frequency_domain_data_types.py sha256=a3dcb8d4e23ebfa458ed8aecb760c9c4d44f672f066fef87021fad8623774ce8 bytes=17104 -->
## FILE: src/nipcbatt/pcbatt_library/daq/frequency_domain_measurements/frequency_domain_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/frequency_domain_measurements/frequency_domain_data_types.py`
- sha256: `a3dcb8d4e23ebfa458ed8aecb760c9c4d44f672f066fef87021fad8623774ce8`
- bytes: 17104

````python
""" Frequency domain data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (146 > 100 characters) (auto-generated noqa)

from typing import List

from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    AmplitudeSpectrum,
    AnalogWaveform,
    DigitalStartTriggerParameters,
    MeasurementOptions,
    SampleClockTimingParameters,
)
from nipcbatt.pcbatt_library.daq.common.voltage_data_types import (
    VoltageMeasurementChannelAndTerminalRangeParameters,
    VoltageRangeAndTerminalParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class FrequencyDomainMeasurementConfiguration(PCBATestToolkitData):
    """Defines parameters used for configuration of Time domain measurement."""

    def __init__(
        self,
        global_channel_parameters: VoltageRangeAndTerminalParameters,
        specific_channels_parameters: List[VoltageMeasurementChannelAndTerminalRangeParameters],
        measurement_options: MeasurementOptions,
        sample_clock_timing_parameters: SampleClockTimingParameters,
        digital_start_trigger_parameters: DigitalStartTriggerParameters,
    ) -> None:
        """Initializes an instance of
        `FrequencyDomainMeasurementConfiguration` with specific values.

        Args:
            global_channel_parameters (VoltageRangeAndTerminalParameters):
                The settings of terminal for all channels.
            specific_channels_parameters (List[VoltageMeasurementChannelAndTerminalRangeParameters]):
                The list of instances of `VoltageMeasurementChannelAndTerminalRangeParameters` used to configure channels.
            measurement_options (MeasurementOptions):
                An instance of `MeasurementOptions` that represents the settings of options used for execution.
            sample_clock_timing_parameters (SampleClockTimingParameters):
                An instance of `SampleClockTimingParameters` that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters` that represents the settings of triggers.

        Raises:
            TypeError:
                Raised when `specific_channels_parameters`
                contains objects that are not type of VoltageMeasurementChannelAndTerminalRangeParameters.
            ValueError:
                Raised when `global_channel_parameters` is None,
                `specific_channels_parameters` is None,
                `measurement_options` is None,
                `sample_clock_timing_parameters` is None,
                `digital_start_trigger_parameters` is None,
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (101 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(global_channel_parameters, nameof(global_channel_parameters))
        Guard.is_not_none(specific_channels_parameters, nameof(specific_channels_parameters))
        Guard.all_elements_are_of_same_type(
            input_list=specific_channels_parameters,
            expected_type=VoltageMeasurementChannelAndTerminalRangeParameters,
        )
        Guard.is_not_none(measurement_options, nameof(measurement_options))
        Guard.is_not_none(sample_clock_timing_parameters, nameof(sample_clock_timing_parameters))
        Guard.is_not_none(
            digital_start_trigger_parameters, nameof(digital_start_trigger_parameters)
        )

        self._global_channel_parameters = global_channel_parameters
        self._specific_channels_parameters = specific_channels_parameters
        self._measurement_options = measurement_options
        self._sample_clock_timing_parameters = sample_clock_timing_parameters
        self._digital_start_trigger_parameters = digital_start_trigger_parameters

    @property
    def global_channel_parameters(
        self,
    ) -> VoltageRangeAndTerminalParameters:
        """
        :class:`VoltageRangeAndTerminalParameters`:
            Gets the settings of terminal for all channels."""  # noqa: D205, D209, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (444 > 100 characters) (auto-generated noqa)
        return self._global_channel_parameters

    @property
    def specific_channels_parameters(
        self,
    ) -> List[VoltageMeasurementChannelAndTerminalRangeParameters]:
        """
        :class:`List[VoltageMeasurementChannelAndTerminalRangeParameters]`:
            Gets the list of instances of
            `VoltageMeasurementChannelAndTerminalRangeParameters` used to configure channels.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._specific_channels_parameters

    @property
    def measurement_options(self) -> MeasurementOptions:
        """
        :class:`MeasurementOptions`:
            Gets a `MeasurementOptions` instance
            that represents the settings of options used for execution.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._measurement_options

    @property
    def sample_clock_timing_parameters(self) -> SampleClockTimingParameters:
        """
        :class:`SampleClockTimingParameters`:
            Gets a `SampleClockTimingParameters` instance
            that represents the settings of timing.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._sample_clock_timing_parameters

    @property
    def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters:
        """
        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._digital_start_trigger_parameters


class MultipleTonesMeasurementResultData(PCBATestToolkitData):
    """Defines multiple tones measurement results obtained after waveform analysis."""

    def __init__(
        self,
        tones_frequencies_hertz: List[float],
        tones_amplitudes_volts: List[float],
    ) -> None:
        """Initializes an instance of "MultipleTonesMeasurementResultData" with specific values.

        Args:
            tones_frequencies_hertz (List[float]):
                A list of frequencies of detected tones for all analyzed waveforms.
            tones_amplitudes_volts (List[float]):
                A list of voltage peak amplitudes of detected tones for all analyzed waveforms.

        Raises:
            TypeError: Raised when,
                `tones_frequencies_hertz` containes objects that are not `float',
                `tones_amplitudes_volts` contains objects that are not `float'.

            ValueError: Raised when,
                `tones_frequencies_hertz` is None,
                `tones_amplitudes_volts` is None,
                `tones_frequencies_hertz` and `tones_amplitudes_volts` lists have different lengths.
        """
        Guard.is_not_none(tones_frequencies_hertz, nameof(tones_frequencies_hertz))
        Guard.is_not_none(tones_amplitudes_volts, nameof(tones_amplitudes_volts))
        Guard.all_elements_are_of_same_type(input_list=tones_frequencies_hertz, expected_type=float)
        Guard.all_elements_are_of_same_type(input_list=tones_amplitudes_volts, expected_type=float)
        Guard.have_same_size(
            first_iterable_instance=tones_amplitudes_volts,
            first_iterable_name=nameof(tones_amplitudes_volts),
            second_iterable_instance=tones_frequencies_hertz,
            second_iterable_name=nameof(tones_frequencies_hertz),
        )

        self._tones_frequencies_hertz = tones_frequencies_hertz
        self._tones_amplitudes_volts = tones_amplitudes_volts

    @property
    def tones_frequencies_hertz(self) -> List[float]:
        """
        :class:`List[float]`:
        Gets a List containing detected tones frequencies of all analyzed waveform.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._tones_frequencies_hertz

    @property
    def tones_amplitudes_volts(self) -> List[float]:
        """
        :class:`List[float]`:
        Gets a list containing detected tones peak amplitudes of all analyzed waveform.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._tones_amplitudes_volts


class FrequencyDomainMeasurementResultData(PCBATestToolkitData):
    """Defines frequency domain measurement results obtained after waveform analysis."""

    def __init__(
        self,
        waveforms: List[AnalogWaveform],
        magnitude_rms: List[AmplitudeSpectrum],
        magnitude_peak: List[AmplitudeSpectrum],
        detected_tones: List[MultipleTonesMeasurementResultData],
    ) -> None:
        """Initializes an instance of "FrequencyDomainMeasurementResultData" with specific values.

        Args:
            waveforms (List[AnalogWaveform]):
                A list of `AnalogWaveform` acquired from channels defined for measurement.
            magnitude_rms (List[AmplitudeSpectrum]):
                A list of `AmplitudeSpectrum` representing the frequency domain measurement RMS computed on all channels.
            magnitude_peak (List[AmplitudeSpectrum]):
                A list of `AmplitudeSpectrum` representing the frequency domain measurement Peak to Peak computed on all channels.
            detected_tones (List[MultipleTonesMeasurementResultData]):
                A list of `MultipleTonesMeasurementResultData` representing the detected tones in the waveform.

        Raises:
            TypeError: Raised when,
                `waveforms` contains objects that are not `AnalogWaveform`,
                `magnitude_rms' contains objects that are not 'AmplitudeSpectrum`,
                `magnitude_peak` contains objects that are not 'AmplitudeSpectrum`,
                `detected_tones` contains objects that are not `MultipleTonesMeasurementResultData`

            ValueError: Raised when,
                `waveforms` is None or empty.
        """  # noqa: W505 - doc line too long (121 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(waveforms, nameof(waveforms))
        Guard.is_not_empty(waveforms, nameof(waveforms))

        Guard.is_not_none(magnitude_rms, nameof(magnitude_rms))
        Guard.is_not_empty(magnitude_rms, nameof(magnitude_rms))

        Guard.is_not_none(magnitude_peak, nameof(magnitude_peak))
        Guard.is_not_empty(magnitude_peak, nameof(magnitude_peak))

        Guard.is_not_none(detected_tones, nameof(detected_tones))
        Guard.is_not_empty(detected_tones, nameof(detected_tones))

        

        Guard.all_elements_are_of_same_type(input_list=waveforms, expected_type=AnalogWaveform)
        Guard.all_elements_are_of_same_type(
            input_list=magnitude_peak, expected_type=AmplitudeSpectrum
        )
        Guard.all_elements_are_of_same_type(
            input_list=magnitude_rms, expected_type=AmplitudeSpectrum
        )
        Guard.all_elements_are_of_same_type(
            input_list=detected_tones, expected_type=MultipleTonesMeasurementResultData
        )

        Guard.have_same_size(waveforms, nameof(waveforms), magnitude_rms, nameof(magnitude_rms))
        Guard.have_same_size(waveforms, nameof(waveforms), magnitude_peak, nameof(magnitude_peak))
        Guard.have_same_size(waveforms, nameof(waveforms), detected_tones, nameof(detected_tones))
        Guard.have_same_size(magnitude_rms, nameof(magnitude_rms), magnitude_peak, nameof(magnitude_peak))

        self._waveforms = waveforms
        self._magnitude_rms = magnitude_rms
        self._magnitude_peak = magnitude_peak
        self._detected_tones = detected_tones

    @property
    def waveforms(self) -> List[AnalogWaveform]:
        """
        :class:`List[AnalogWaveform]`:
            Gets the list of waveforms acquired from channels defined
            for measurement and used to compute frequency domain results.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._waveforms

    @property
    def magnitude_rms(self) -> List[AmplitudeSpectrum]:
        """
        :calss: List[AmplitudeSpectrum]:
            Gets an array of RMS based spectrums computed for each channel waveform in `waveforms`.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._magnitude_rms

    @property
    def magnitude_peak(self) -> List[AmplitudeSpectrum]:
        """
        :calss: List[AmplitudeSpectrum]:
            Gets an array of Peak to Peak based spectrums computed for each channel waveform in `waveforms`.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (108 > 100 characters) (auto-generated noqa)
        return self._magnitude_peak

    @property
    def detected_tones(self) -> List[MultipleTonesMeasurementResultData]:
        """
        :calss: List[MultipleTonesMeasurementResultData]:
            Gets an array of multiple tones analysis results for each waveform contained in `waveforms`.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (104 > 100 characters) (auto-generated noqa)
        return self._detected_tones
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/frequency_domain_measurements/frequency_domain_measurement.py sha256=abf0e6188cd4d84d59be6903845963d1c9380a803b1cd86f961a96fec6639856 bytes=19419 -->
## FILE: src/nipcbatt/pcbatt_library/daq/frequency_domain_measurements/frequency_domain_measurement.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/frequency_domain_measurements/frequency_domain_measurement.py`
- sha256: `abf0e6188cd4d84d59be6903845963d1c9380a803b1cd86f961a96fec6639856`
- bytes: 19419

````python
# pylint: disable=W0613
# remove it when arguments of initialize are used.
"""  Defines class used for Frequency domain measurement on PCB points. """

import math
from typing import Union

import nidaqmx.constants
import nidaqmx.stream_readers
import numpy
from varname import nameof

from nipcbatt.pcbatt_analysis.waveform_analysis.frequency_domain_analysis import (
    LabViewFrequencyDomainProcessing,
)
from nipcbatt.pcbatt_analysis.waveform_transformation import scale_and_offset_waveform
from nipcbatt.pcbatt_library.common.common_data_types import (
    AmplitudeSpectrum,
    AnalogWaveform,
    DigitalStartTriggerParameters,
    MeasurementAnalysisRequirement,
    MeasurementData,
    MeasurementExecutionType,
    SampleClockTimingParameters,
    SampleTimingEngine,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.daq.common.voltage_constants import (
    ConstantsForVoltageMeasurement,
)
from nipcbatt.pcbatt_library.daq.common.voltage_data_types import (
    VoltageMeasurementChannelAndTerminalRangeParameters,
    VoltageRangeAndTerminalParameters,
)
from nipcbatt.pcbatt_library.daq.frequency_domain_measurements.frequency_domain_constants import (
    ConstantsForFrequencyDomainMeasurement,
)
from nipcbatt.pcbatt_library.daq.frequency_domain_measurements.frequency_domain_data_types import (
    FrequencyDomainMeasurementConfiguration,
    FrequencyDomainMeasurementResultData,
    MultipleTonesMeasurementResultData,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_utilities.guard_utilities import Guard
from nipcbatt.pcbatt_utilities.numeric_utilities import invert_value


class FrequencyDomainMeasurement(BuildingBlockUsingDAQmx):
    """Defines a way that allows you to perform Frequency domain measurement on PCB points."""

    def initialize(self, analog_input_channel_expression: str):
        """Initializes the measurement with the specific channels

        Args:
            analog_input_channel_expression (str):
                Expression representing the name of a physical channel,
                or a global channel in DAQ System.
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        if self.is_task_initialized:
            return

        if self.contains_only_global_virtual_channels(
            channel_expression=analog_input_channel_expression
        ):
            # If the input channel_expression contains global channel,
            # then add them as global channels
            # and verify if the global channels are configured for voltage measurement.
            self.add_global_channels(global_channel_expression=analog_input_channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
            self.verify_measurement_type(nidaqmx.constants.UsageTypeAI.VOLTAGE)
        else:
            # Add the channel_expression to analog input current channel of the Daqmx task
            self.task.ai_channels.add_ai_voltage_chan(
                physical_channel=analog_input_channel_expression,
                name_to_assign_to_channel="",
                terminal_config=ConstantsForVoltageMeasurement.INITIAL_AI_TERMINAL_CONFIGURATION,
                min_val=ConstantsForVoltageMeasurement.INITIAL_VOLTAGE_MINIMUM_VALUE_VOLTS,
                max_val=ConstantsForVoltageMeasurement.INITIAL_VOLTAGE_MAXIMUM_VALUE_VOLTS,
                units=ConstantsForVoltageMeasurement.INITIAL_AI_VOLTAGE_UNITS,
            )

    def close(self):
        """Closes measurement procedure and releases internal resources."""
        if not self.is_task_initialized:
            return

        # Stop and close the DAQmx task
        self.task.stop()
        self.task.close()

    def configure_and_measure(
        self, configuration: FrequencyDomainMeasurementConfiguration
    ) -> Union[None, FrequencyDomainMeasurementResultData]:
        """Configures and/or performs a measurement
           according to specific configuration parameters.

        Args:
            configuration (FrequencyDomainMeasurementConfiguration): An instance of
            `FrequencyDomainMeasurementConfiguration` used to configure the measurement.

        Returns:
            FrequencyDomainMeasurementResultData | None:
                An instance of `FrequencyDomainMeasurementResultData`
                or `None` if no measure was performed.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        if configuration.measurement_options.execution_option in (
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.CONFIGURE_ONLY,
        ):
            self.configure_all_channels(configuration.global_channel_parameters)
            for specific_channel_parameters in configuration.specific_channels_parameters:
                self.configure_specific_channel(specific_channel_parameters)
            self.configure_timing(configuration.sample_clock_timing_parameters)
            self.configure_trigger(configuration.digital_start_trigger_parameters)

        if configuration.measurement_options.execution_option in (
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.MEASURE_ONLY,
        ):
            data = self.acquire_data_for_measurement_analysis()
            return self.analyze_measurement_data(
                data, configuration.measurement_options.measurement_analysis_requirement
            )

        self.task.start()
        return None

    def configure_all_channels(self, parameters: VoltageRangeAndTerminalParameters):
        """Configures all channels used for voltage measurements.

        Args:
            parameters (VoltageRangeAndTerminalParameters):
            An instance of `VoltageRangeAndTerminalParameters` used to configure the channels.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        # for each channel defined in analog input channels list,
        # set terminal configuration and voltage range.
        for channel in self.task.ai_channels:
            channel.ai_term_cfg = parameters.terminal_configuration
            channel.ai_min = parameters.range_min_volts
            channel.ai_max = parameters.range_max_volts

    def configure_specific_channel(
        self, parameters: VoltageMeasurementChannelAndTerminalRangeParameters
    ):
        """Configures the specific channels used for voltage measurements.

        Args:
            parameters (VoltageMeasurementChannelAndTerminalRangeParameters):
            An instance of `VoltageMeasurementChannelAndTerminalRangeParameters`
            used to configure the channels.

        If the user provides Global Virtual Channel name in Initialize(),
        then he/she has to provide the Virtual channel name in Specific channel parameters as well.

        Similarly, if the user provides Physical channel name in Initialize(),
        then he/she has to provide the Physical channel name in Specific channel parameters.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        if parameters.channel_name in (channel.name for channel in self.task.ai_channels):
            # if the specified channel is present in ai_channel_collection,
            # update the voltage parameters of the channel
            self.task.ai_channels[
                parameters.channel_name
            ].ai_term_cfg = parameters.channel_parameters.terminal_configuration
            self.task.ai_channels[
                parameters.channel_name
            ].ai_min = parameters.channel_parameters.range_min_volts
            self.task.ai_channels[
                parameters.channel_name
            ].ai_max = parameters.channel_parameters.range_max_volts
        else:
            # otherwise, adds the channel.
            if self.contains_only_global_virtual_channels(
                channel_expression=parameters.channel_name
            ):
                # Global virtual channel
                self.add_global_channels(global_channel_expression=parameters.channel_name)
                self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
                self.verify_measurement_type(nidaqmx.constants.UsageTypeAI.VOLTAGE)
                for channel in self.task.ai_channels:
                    channel.ai_term_cfg = parameters.channel_parameters.terminal_configuration
                    channel.ai_min = parameters.channel_parameters.range_min_volts
                    channel.ai_max = parameters.channel_parameters.range_max_volts
            else:
                # Physical channel
                self.task.ai_channels.add_ai_voltage_chan(
                    physical_channel=parameters.channel_name,
                    terminal_config=parameters.channel_parameters.terminal_configuration,
                    min_val=parameters.channel_parameters.range_min_volts,
                    max_val=parameters.channel_parameters.range_max_volts,
                    units=ConstantsForVoltageMeasurement.INITIAL_AI_VOLTAGE_UNITS,
                )

    def configure_timing(self, parameters: SampleClockTimingParameters):
        """Configures the timing characteristics used for voltage measurements.

        Args:
            parameters (SampleClockTimingParameters):
            An instance of `SampleClockTimingParameters`
            used to configure the timing.
        """  # noqa: D202, D417, W505 - No blank lines allowed after function docstring (auto-generated noqa), Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

        self.task.timing.cfg_samp_clk_timing(
            rate=parameters.sampling_rate_hertz,
            sample_mode=nidaqmx.constants.AcquisitionType.FINITE,
            samps_per_chan=parameters.number_of_samples_per_channel,
            source=parameters.sample_clock_source,
        )

        # if the current timing engine setting is Auto
        # then delete the previous timing engine property
        # and let the task revert to the default setting of DAQmx
        # to automatically set the value of the timing engine
        if parameters.sample_timing_engine == SampleTimingEngine.AUTO:
            # Sample timing engine is auto selected
            ...
        else:
            self.task.timing.samp_timing_engine = parameters.sample_timing_engine.value

    def configure_trigger(self, parameters: DigitalStartTriggerParameters):
        """Configure the characteristics of triggers used for voltage measurements.

        Args:
            parameters (DigitalStartTriggerParameters):
            An instance of `DigitalStartTriggerParameters`
            used to configure the channels.
        """  # noqa: D202, D417, W505 - No blank lines allowed after function docstring (auto-generated noqa), Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

        if parameters.trigger_select == StartTriggerType.NO_TRIGGER:
            self.task.triggers.start_trigger.disable_start_trig()
        else:
            self.task.triggers.start_trigger.cfg_dig_edge_start_trig(
                trigger_source=parameters.digital_start_trigger_source,
                trigger_edge=parameters.digital_start_trigger_edge,
            )

    def acquire_data_for_measurement_analysis(self) -> MeasurementData:
        """Acquires Data from DAQ channel for measurement of voltage.

        Returns:
            MeasurementData: An instance of `MeasurementData`
            that specifies the data acquired from DAQ channels.
        """
        # Builds the shape of numpy array (number of channels, number of samples)
        number_of_channels = len(self.task.in_stream.channels_to_read.channel_names)
        number_of_samples_per_channel = self.task.timing.samp_quant_samp_per_chan

        # Build the numpy array.
        samples_array = numpy.zeros(
            shape=(number_of_channels, number_of_samples_per_channel),
            dtype=numpy.float64,
        )

        # Reads data and fill numpy array.
        reader = nidaqmx.stream_readers.AnalogMultiChannelReader(self.task.in_stream)
        reader.read_many_sample(
            data=samples_array,
            number_of_samples_per_channel=number_of_samples_per_channel,
        )

        return MeasurementData(samples_array)

    def analyze_measurement_data(
        self,
        measurement_data: MeasurementData,
        measurement_analysis_requirement: MeasurementAnalysisRequirement,
    ) -> FrequencyDomainMeasurementResultData:
        """Proceeds to the analysis of Voltages from the measurement.

        Args:
            data (MeasurementData):
                An instance of `MeasurementData`
                that specifies the data acquired from DAQ channels.
            measurement_analysis_requirement (MeasurementAnalysisRequirement):
                An instance of 'MeasurementAnalysisRequirement' that specifies
                whether to Skip Analysis or Proceed to Analysis.

        Returns:
            FrequencyDomainMeasurementResultData:
            An instance of `FrequencyDomainMeasurementResultData`
            that specifies the measurement results.
        """
        # Check if sampling rate is 0 and raise error to avoid divide by 0 error.
        Guard.is_greater_than_zero(
            self.task.timing.samp_clk_rate, nameof(self.task.timing.samp_clk_rate)
        )
        delta_time_seconds = invert_value(self.task.timing.samp_clk_rate)

        # Initialization for DcRmsVoltageMeasurementResultData instance creation.
        voltage_waveforms: list[AnalogWaveform] = []
        measured_magnitude_rms: list[AmplitudeSpectrum] = []
        measured_magtitude_peak: list[AmplitudeSpectrum] = []
        measured_detected_tones: list[MultipleTonesMeasurementResultData] = []

        for channel_samples, channel_name in zip(
            measurement_data.samples_per_channel,
            self.task.in_stream.channels_to_read.channel_names,
        ):
            # Creates an instance of AnalogWaveform and add it to waveforms.
            voltage_waveforms.append(
                AnalogWaveform(
                    channel_name=channel_name,
                    delta_time_seconds=delta_time_seconds,
                    samples=channel_samples,
                )
            )

            if (
                measurement_analysis_requirement
                == MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
            ):
                # Frequency domain processing
                fdvm_processing_results = LabViewFrequencyDomainProcessing.process_single_waveform_multiple_tones_and_amplitude_phase_spectrum(
                    waveform_samples=channel_samples,
                    waveform_sampling_period_seconds=delta_time_seconds,
                    spectrum_amplitude_must_be_db=(
                        ConstantsForFrequencyDomainMeasurement.VIEW_RESULTS_dB_ON
                    ),
                    spectrum_phase_unit=(
                        ConstantsForFrequencyDomainMeasurement.VIEW_RESULTS_PHASE_UNIT
                    ),
                    fft_spectrum_window=ConstantsForFrequencyDomainMeasurement.FILTERING_WINDOW_FOR_FFT,
                    tones_sorting_mode=(
                        ConstantsForFrequencyDomainMeasurement.DEFAULT_SORTING_ORDER_OF_THE_EXTRACTED_TONES
                    ),
                    tones_selection_threshold_peak_amplitude=(
                        ConstantsForFrequencyDomainMeasurement.DEFAULT_THRESHOLD_FOR_TONE_EXTRACTION
                    ),
                    tones_max_count=(
                        ConstantsForFrequencyDomainMeasurement.DEFAULT_MAX_NUMBER_OF_TONES_TO_BE_EXTRACTED
                    ),
                )

                fdvm_spectrum_result = fdvm_processing_results.amplitude_phase_spectrum
                fdvm_tones_result = fdvm_processing_results.multiple_tones_result

                # RMS spectrum results is default output of analysis library
                measured_magnitude_rms.append(
                    AmplitudeSpectrum(
                        channel_name=channel_name,
                        spectrum_start_frequency_hertz=fdvm_spectrum_result.spectrum_start_frequency,
                        spectrum_frequency_resolution_hertz=(
                            fdvm_spectrum_result.spectrum_frequency_resolution
                        ),
                        # RMS amplitudes
                        amplitudes=fdvm_spectrum_result.spectrum_amplitudes,
                    )
                )

                # PEAK spectrum results are obtained by converting RMS amplitudes
                measured_magtitude_peak.append(
                    AmplitudeSpectrum(
                        channel_name=channel_name,
                        spectrum_start_frequency_hertz=fdvm_spectrum_result.spectrum_start_frequency,
                        spectrum_frequency_resolution_hertz=(
                            fdvm_spectrum_result.spectrum_frequency_resolution
                        ),
                        # PEAK amplitudes
                        amplitudes=scale_and_offset_waveform.scale(
                            waveform_samples=fdvm_spectrum_result.spectrum_amplitudes,
                            scale_factor=math.sqrt(2),
                        ),
                    ),
                )

                # Multiple tones processing results
                measured_detected_tones.append(
                    MultipleTonesMeasurementResultData(
                        tones_frequencies_hertz=list(
                            map(
                                lambda waveform_tone: waveform_tone.frequency,
                                fdvm_tones_result.detected_tones,
                            )
                        ),
                        tones_amplitudes_volts=list(
                            map(
                                lambda waveform_tone: waveform_tone.amplitude,
                                fdvm_tones_result.detected_tones,
                            )
                        ),
                    )
                )

        # Return
        return FrequencyDomainMeasurementResultData(
            waveforms=voltage_waveforms,
            magnitude_rms=measured_magnitude_rms,
            magnitude_peak=measured_magtitude_peak,
            detected_tones=measured_detected_tones,
        )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/power_supply_source_and_measurements/__init__.py sha256=d8aaeeccc754432744fd072858fff6bc19f7d0220020c69ed9ce754c2a4857ee bytes=251 -->
## FILE: src/nipcbatt/pcbatt_library/daq/power_supply_source_and_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/power_supply_source_and_measurements/__init__.py`
- sha256: `d8aaeeccc754432744fd072858fff6bc19f7d0220020c69ed9ce754c2a4857ee`
- bytes: 251

````python
"""Provides nipcbatt library power source and measurement modules"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (179 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/power_supply_source_and_measurements/power_supply_source_and_measure.py sha256=9c18450f87b2af11a25ebf8579895bc8b0ec51659f861ec2c321d28f1ef0d7e0 bytes=13547 -->
## FILE: src/nipcbatt/pcbatt_library/daq/power_supply_source_and_measurements/power_supply_source_and_measure.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/power_supply_source_and_measurements/power_supply_source_and_measure.py`
- sha256: `9c18450f87b2af11a25ebf8579895bc8b0ec51659f861ec2c321d28f1ef0d7e0`
- bytes: 13547

````python
# pylint: disable=W0613
# remove it when arguments of initialize are used.
"""Defines class used for power supply source and measurement of voltage, current and power."""

import time  # noqa: F401 - 'time' imported but unused (auto-generated noqa)

import nidaqmx.constants
import nidaqmx.stream_readers
import numpy
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    AnalogWaveform,
    DigitalStartTriggerParameters,
    MeasurementAnalysisRequirement,
    MeasurementExecutionType,
    SampleClockTimingParameters,
    SampleTimingEngine,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.daq.power_supply_source_and_measurements.power_supply_source_constants import (
    ConstantsForPowerSupplySourceMeasurement,
)
from nipcbatt.pcbatt_library.daq.power_supply_source_and_measurements.power_supply_source_data_types import (
    PowerSupplySourceAndMeasureConfiguration,
    PowerSupplySourceAndMeasureData,
    PowerSupplySourceAndMeasureResultData,
    PowerSupplySourceAndMeasureTerminalParameters,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_utilities.guard_utilities import Guard
from nipcbatt.pcbatt_utilities.numeric_utilities import invert_value


class PowerSupplySourceAndMeasure(BuildingBlockUsingDAQmx):
    """Defines a way that allows you to configure and perform power supply using a source and measure resulting voltage and current.

    Args:
        BuildingBlockUsingDAQmx (_type_): _description_
    """  # noqa: W505 - doc line too long (132 > 100 characters) (auto-generated noqa)

    def initialize(self, power_channel_name: str):
        """Initializes the Power source and measurement with the specific channel

        Args:
            power_channel_name (str): Expression representing the name of a physical channel,
            or a global channel or the name of registered settings in DAQ System.
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        if self.is_task_initialized:
            return

        # There will be only once channel for Power Source and Measure
        # task at a time. Add the Power channel to the task.
        self.task.ai_channels.add_ai_power_chan(
            physical_channel=power_channel_name,
            voltage_setpoint=(
                ConstantsForPowerSupplySourceMeasurement.INITIAL_VOLTAGE_SETPOINT_VOLTS
            ),
            current_setpoint=(
                ConstantsForPowerSupplySourceMeasurement.INITIAL_CURRENT_SETPOINT_AMPERES
            ),
            output_enable=ConstantsForPowerSupplySourceMeasurement.INITIAL_OUTPUT_ENABLE,
        )

    def close(self):
        """Closes the measurement process and releases the internal resources"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (191 > 100 characters) (auto-generated noqa)
        if not self.is_task_initialized:
            return
        # Stop and close the daqmx task
        self.task.stop()
        self.task.close()

    def configure_and_measure(
        self, configuration: PowerSupplySourceAndMeasureConfiguration
    ) -> PowerSupplySourceAndMeasureResultData:
        """
        Configures and/or performs a measurement according to specific configuration parameters.

        Args:
            configuration (PowerSupplySourceAndMeasureConfiguration):
            A instance of `PowerSupplySourceAndMeasureConfiguration`
            used to configure the measurement.

        Returns:
            _type_: An instance of `PowerSupplySourceAndMeasureResultData
            ` or `None` if no measure was performed.
        """  # noqa: D202, D212, W505 - No blank lines allowed after function docstring (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (186 > 100 characters) (auto-generated noqa)

        if configuration.measurement_options.execution_option in (
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.CONFIGURE_ONLY,
        ):
            self.configure_all_channels(configuration.terminal_parameters)
            self.configure_timing(configuration.sample_clock_timing_parameters)
            self.configure_trigger(configuration.digital_start_trigger_parameters)

        if configuration.measurement_options.execution_option in (
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.MEASURE_ONLY,
        ):
            self.task.start()
            data = self.acquire_data_for_measurement_analysis()
            return self.analyze_measurement_data(
                data, configuration.measurement_options.measurement_analysis_requirement
            )

        self.task.start()
        return None

    def configure_all_channels(self, parameters: PowerSupplySourceAndMeasureTerminalParameters):
        """Configures all channels used for power supply source and measure measurements.

        Args:
            parameters (PowerSupplySourceAndMeasureTerminalParameters):
            An instance of `PowerSupplySourceAndMeasureTerminalParameters`
            used to configure the channels.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        for channel in self.task.ai_channels:
            channel.pwr_voltage_setpoint = parameters.voltage_setpoint_volts
            channel.pwr_current_setpoint = parameters.current_setpoint_amperes
            channel.pwr_remote_sense = parameters.power_sense
            channel.pwr_idle_output_behavior = parameters.idle_output_behaviour
            channel.pwr_output_enable = parameters.enable_output

    def configure_timing(self, parameters: SampleClockTimingParameters):
        """Configure the timing characteristics used for Power supply sourcing and measurement.

        Args:
            parameters (SampleClockTimingParameters):
            An instance of `SampleClockTimingParameters`
            used to configure the timing.
        """  # noqa: D202, D417, W505 - No blank lines allowed after function docstring (auto-generated noqa), Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

        self.task.timing.cfg_samp_clk_timing(
            rate=parameters.sampling_rate_hertz,
            sample_mode=nidaqmx.constants.AcquisitionType.FINITE,
            samps_per_chan=parameters.number_of_samples_per_channel,
            source=parameters.sample_clock_source,
        )

        # if the current timing engine setting is Auto
        # then delete the previous timing engine property
        # and let the task revert to the default setting of DAQmx
        # to automatically set the value of the timing engine
        if parameters.sample_timing_engine == SampleTimingEngine.AUTO:
            del self.task.timing.samp_timing_engine
        else:
            self.task.timing.samp_timing_engine = parameters.sample_timing_engine.value

    def configure_trigger(self, parameters: DigitalStartTriggerParameters):
        """Configure the characteristics of triggers used for Power supply sourcing and measurement.

        Args:
            parameters (DigitalStartTriggerParameters):
            An instance of `DigitalStartTriggerParameters`
            used to configure the channels.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        self.task.stop()
        if parameters.trigger_select == StartTriggerType.NO_TRIGGER:
            self.task.triggers.start_trigger.disable_start_trig()
        else:
            self.task.triggers.start_trigger.cfg_dig_edge_start_trig(
                trigger_source=parameters.digital_start_trigger_source,
                trigger_edge=parameters.digital_start_trigger_edge,
            )

    def acquire_data_for_measurement_analysis(self) -> PowerSupplySourceAndMeasureData:
        """Acquires the voltage and current data from the DAQ channel
        for measurement of Power supply.

        Returns:
            PowerSupplySourceAndMeasureData: An instance of `PowerSupplySourceAndMeasureData`
            that contains array of voltage and current samples acquired from DAQ channels.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel_to_read = self.task.timing.samp_quant_samp_per_chan
        # Create pre-allocated numpy array to read the voltage samples from the daqmx buffer.
        voltage_data_to_read = numpy.zeros(
            shape=(number_of_samples_per_channel_to_read),
            dtype=numpy.float64,
        )
        # Create pre-allocated numpy array to read the current samples from the daqmx buffer.
        current_data_to_read = numpy.zeros(
            shape=(number_of_samples_per_channel_to_read),
            dtype=numpy.float64,
        )

        # Read current and voltage samples from the task channel reader.
        reader = nidaqmx.stream_readers.PowerSingleChannelReader(self.task.in_stream)
        reader.read_many_sample(
            voltage_data=voltage_data_to_read,
            current_data=current_data_to_read,
            number_of_samples_per_channel=number_of_samples_per_channel_to_read,
            timeout=10,
        )

        # If there are NaN values in numpy array, set them as 0.
        # This is a bug in samples representation of Power.
        for index in range(0, number_of_samples_per_channel_to_read):
            if numpy.isnan(voltage_data_to_read[index]):
                voltage_data_to_read[index] = 0
            if numpy.isnan(current_data_to_read[index]):
                current_data_to_read[index] = 0

        # Create an instance of PowerSupplySourceAndMeasureData
        # with the voltage and current samples read above.
        return PowerSupplySourceAndMeasureData(
            source_name=self.task.channel_names[0],
            voltage_samples=voltage_data_to_read,
            current_samples=current_data_to_read,
            sampling_rate_hertz=self.task.timing.samp_clk_rate,
        )

    def analyze_measurement_data(
        self,
        measurement_data: PowerSupplySourceAndMeasureData,
        measurement_analysis_requirement: MeasurementAnalysisRequirement,
    ) -> PowerSupplySourceAndMeasureResultData:
        """Calls the analysis function for Power source and measure measurements.

        Args:
            data (PowerSupplySourceAndMeasureData):
                An instance of `PowerSupplySourceAndMeasureData`
                that specifies the voltage and current data acquired from DAQ channels.
            measurement_analysis_requirement (MeasurementAnalysisRequirement):
                An instance of 'MeasurementAnalysisRequirement' that specifies
                whether to Skip Analysis or Proceed to Analysis.

        Returns:
            PowerSupplySourceAndMeasureResultData:
                An instance of `PowerSupplySourceAndMeasureResultData`
                that specifies the measurement results.
        """
        Guard.is_not_none(measurement_data, nameof(measurement_data))

        # extract & convert sample rate to delta_t

        dt = invert_value(measurement_data.sampling_rate_hertz)

        # Generate voltage waveform
        voltage_waveform = AnalogWaveform("Voltage", dt, measurement_data.voltage_samples)

        # Generate current waveform
        current_waveform = AnalogWaveform("Current", dt, measurement_data.current_samples)

        max_voltage_level = 0.0
        max_current_level = 0.0
        max_power_level = 0.0
        average_power_level = 0.0
        acquisition_duration = 0.0

        if measurement_analysis_requirement == MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS:
            # Calculate max voltage level
            max_voltage_level = numpy.max(measurement_data.voltage_samples)

            # Calculate max current level
            max_current_level = numpy.max(measurement_data.current_samples)

            # generate power samples
            power_samples = numpy.multiply(
                measurement_data.voltage_samples, measurement_data.current_samples
            )

            # calculate power
            max_power_level = numpy.max(power_samples)
            average_power_level = numpy.mean(power_samples)

            # Calculate total duration
            acquisition_duration = dt * numpy.size(measurement_data.voltage_samples)

        # Create and return PowerSupplySourceAndMeasureData object
        return PowerSupplySourceAndMeasureResultData(
            voltage_waveform,
            current_waveform,
            max_voltage_level,
            max_current_level,
            max_power_level,
            average_power_level,
            acquisition_duration,
        )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/power_supply_source_and_measurements/power_supply_source_constants.py sha256=dd7fde2281b0673e639c2965795ed84f827b935bd13a5036f3f069776ceea743 bytes=4212 -->
## FILE: src/nipcbatt/pcbatt_library/daq/power_supply_source_and_measurements/power_supply_source_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/power_supply_source_and_measurements/power_supply_source_constants.py`
- sha256: `dd7fde2281b0673e639c2965795ed84f827b935bd13a5036f3f069776ceea743`
- bytes: 4212

````python
"""Constants for default values for Power Supply Source Measurements"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (182 > 100 characters) (auto-generated noqa)

import nidaqmx.constants

from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
    MeasurementAnalysisRequirement,
    MeasurementExecutionType,
    MeasurementOptions,
    SampleClockTimingParameters,
    SampleTimingEngine,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.daq.power_supply_source_and_measurements.power_supply_source_data_types import (
    PowerSupplySourceAndMeasureConfiguration,
    PowerSupplySourceAndMeasureTerminalParameters,
)


class ConstantsForPowerSupplySourceMeasurement:
    """Constants used for Power Supply measurements"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)

    INITIAL_VOLTAGE_SETPOINT_VOLTS = 0.0
    INITIAL_CURRENT_SETPOINT_AMPERES = 0.03
    INITIAL_OUTPUT_ENABLE = False

    DEFAULT_VOLTAGE_SETPOINT_VOLTS = 1.0
    DEFAULT_CURRENT_SETPOINT_AMPERES = 0.1
    DEFAULT_REMOTE_SENSE = nidaqmx.constants.Sense.LOCAL
    DEFAULT_IDLE_OUTPUT_BEHAVIOUR = nidaqmx.constants.PowerIdleOutputBehavior.OUTPUT_DISABLED
    DEFAULT_OUTPUT_ENABLE = True

    DEFAULT_EXECUTION_TYPE = MeasurementExecutionType.CONFIGURE_AND_MEASURE
    DEFAULT_MEASUREMENT_ANALYSIS_REQUIREMENT = MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS

    DEFAULT_SAMPLE_CLOCK_SOURCE = "OnboardClock"
    DEFAULT_SAMPLING_RATE_HERTZ = 10000
    DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL = 1000
    DEFAULT_SAMPLE_TIMING_ENGINE = SampleTimingEngine.AUTO

    DEFAULT_TRIGGER_TYPE = StartTriggerType.NO_TRIGGER
    DEFAULT_DIGITAL_START_TRIGGER_SOURCE = ""
    DEFAULT_DIGITAL_START_TRIGGER_EDGE = nidaqmx.constants.Edge.RISING


DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_TERMINAL_PARAMETERS = PowerSupplySourceAndMeasureTerminalParameters(
    voltage_setpoint_volts=ConstantsForPowerSupplySourceMeasurement.DEFAULT_VOLTAGE_SETPOINT_VOLTS,
    current_setpoint_amperes=ConstantsForPowerSupplySourceMeasurement.DEFAULT_CURRENT_SETPOINT_AMPERES,
    power_sense=ConstantsForPowerSupplySourceMeasurement.DEFAULT_REMOTE_SENSE,
    idle_output_behaviour=ConstantsForPowerSupplySourceMeasurement.DEFAULT_IDLE_OUTPUT_BEHAVIOUR,
    enable_output=ConstantsForPowerSupplySourceMeasurement.DEFAULT_OUTPUT_ENABLE,
)

DEFAULT_POWER_SUPPLY_MEASUREMENT_OPTIONS = MeasurementOptions(
    execution_option=ConstantsForPowerSupplySourceMeasurement.DEFAULT_EXECUTION_TYPE,
    measurement_analysis_requirement=ConstantsForPowerSupplySourceMeasurement.DEFAULT_MEASUREMENT_ANALYSIS_REQUIREMENT,
)

DEFAULT_POWER_SUPPLY_SAMPLE_CLOCK_TIMING_PARAMETERS = SampleClockTimingParameters(
    sample_clock_source=ConstantsForPowerSupplySourceMeasurement.DEFAULT_SAMPLE_CLOCK_SOURCE,
    sampling_rate_hertz=ConstantsForPowerSupplySourceMeasurement.DEFAULT_SAMPLING_RATE_HERTZ,
    number_of_samples_per_channel=ConstantsForPowerSupplySourceMeasurement.DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL,
    sample_timing_engine=ConstantsForPowerSupplySourceMeasurement.DEFAULT_SAMPLE_TIMING_ENGINE,
)

DEFAULT_POWER_SUPPLY_DIGITAL_START_TRIGGER_PARAMETERS = DigitalStartTriggerParameters(
    trigger_select=ConstantsForPowerSupplySourceMeasurement.DEFAULT_TRIGGER_TYPE,
    digital_start_trigger_source=ConstantsForPowerSupplySourceMeasurement.DEFAULT_DIGITAL_START_TRIGGER_SOURCE,
    digital_start_trigger_edge=ConstantsForPowerSupplySourceMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE,
)

DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_CONFIGURATION = PowerSupplySourceAndMeasureConfiguration(
    terminal_parameters=DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_TERMINAL_PARAMETERS,
    measurement_options=DEFAULT_POWER_SUPPLY_MEASUREMENT_OPTIONS,
    sample_clock_timing_parameters=DEFAULT_POWER_SUPPLY_SAMPLE_CLOCK_TIMING_PARAMETERS,
    digital_start_trigger_parameters=DEFAULT_POWER_SUPPLY_DIGITAL_START_TRIGGER_PARAMETERS,
)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/power_supply_source_and_measurements/power_supply_source_data_types.py sha256=ab95643e74bda4bffa464b1172f8bcca1458fa6ff842b1f5836681f5a2b44f08 bytes=21306 -->
## FILE: src/nipcbatt/pcbatt_library/daq/power_supply_source_and_measurements/power_supply_source_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/power_supply_source_and_measurements/power_supply_source_data_types.py`
- sha256: `ab95643e74bda4bffa464b1172f8bcca1458fa6ff842b1f5836681f5a2b44f08`
- bytes: 21306

````python
""" Power supply source data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (149 > 100 characters) (auto-generated noqa)

import nidaqmx.constants
import numpy
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    AnalogWaveform,
    DigitalStartTriggerParameters,
    MeasurementOptions,
    SampleClockTimingParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class PowerSupplySourceAndMeasureTerminalParameters(PCBATestToolkitData):
    """Defines parameters used for configuration of Power source and measurements"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (195 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        voltage_setpoint_volts: float,
        current_setpoint_amperes: float,
        power_sense: nidaqmx.constants.Sense,
        idle_output_behaviour: nidaqmx.constants.PowerIdleOutputBehavior,
        enable_output: bool,
    ) -> None:
        """Initializes an instance of `PowerSupplySourceAndMeasureTerminalParameters'
        with specific values

        Args:
            voltage_setpoint_volts (float):
                The constant output voltage, in volts, to be set for the terminal.
            current_setpoint_amperes (float):
                The constant output current, in amperes, to be set for the terminal.
            power_sense (nidaqmx.constants.Sense):
                Specifies whether to use local or remote sense to sense the output voltage.
            idle_output_behaviour (nidaqmx.constants.PowerIdleOutputBehavior):
                Specifies whether to disable the output or
                maintain the existing value after the task is uncommitted.
            enable_output (bool):
                Specifies whether to enable or disable power module output.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._voltage_setpoint_volts = voltage_setpoint_volts
        self._current_setpoint_amperes = current_setpoint_amperes
        self._power_sense = power_sense
        self._idle_output_behaviour = idle_output_behaviour
        self._enable_output = enable_output

    @property
    def voltage_setpoint_volts(self) -> float:
        """
        :type:`float`:Gets the output voltage setpoint in volts for the terminal
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._voltage_setpoint_volts

    @property
    def current_setpoint_amperes(self) -> float:
        """
        :type:`float`:Gets the output current setpoint in amperes for the terminal
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._current_setpoint_amperes

    @property
    def power_sense(self) -> nidaqmx.constants.Sense:
        """
        :class:`nidaqmx.constants.Sense`:
            Gets the remote sense value configured for the power measurement
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._power_sense

    @property
    def idle_output_behaviour(self) -> nidaqmx.constants.PowerIdleOutputBehavior:
        """
        :class:`nidaqmx.constants.PowerIdleOutputBehavior`:
            Gets the idle output behaviour value configured for the power channels
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._idle_output_behaviour

    @property
    def enable_output(self) -> bool:
        """
        :type:`bool`:Gets if the output is enabled or disabled
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._enable_output


class PowerSupplySourceAndMeasureConfiguration(PCBATestToolkitData):
    """Defines parameters used for configuration of Power measurements"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (184 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        terminal_parameters: PowerSupplySourceAndMeasureTerminalParameters,
        measurement_options: MeasurementOptions,
        sample_clock_timing_parameters: SampleClockTimingParameters,
        digital_start_trigger_parameters: DigitalStartTriggerParameters,
    ) -> None:
        """Initializes an instance of
        `PowerSupplySourceAndMeasureConfiguration` with specific values.

        Args:
            terminal_parameters (PowerSupplySourceAndMeasureTerminalParameters)
                The settings of terminal for all Power channels.
            measurement_options (MeasurementOptions):
                An instance of `MeasurementOptions` that represents
                the settings of options used for execution.
            sample_clock_timing_parameters (SampleClockTimingParameters):
                An instance of `SampleClockTimingParameters`
                that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters`
                that represents the settings of triggers.
        """  # noqa: D205, D415, D417, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (286 > 100 characters) (auto-generated noqa)
        self._measurement_options = measurement_options
        self._sample_clock_timing_parameters = sample_clock_timing_parameters
        self._digital_start_trigger_parameters = digital_start_trigger_parameters
        self._terminal_parameters = terminal_parameters

    @property
    def terminal_parameters(self) -> PowerSupplySourceAndMeasureTerminalParameters:
        """
        :class: `PowerSupplySourceAndMeasureTerminalParameters`:
            Gets the settings of Power terminal for all the channels.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._terminal_parameters

    @property
    def measurement_options(self) -> MeasurementOptions:
        """
        :class:`MeasurementOptions`:
            Gets a `MeasurementOptions` instance
            that represents the settings of options used for execution.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._measurement_options

    @property
    def sample_clock_timing_parameters(self) -> SampleClockTimingParameters:
        """
        :class:`SampleClockTimingParameters`:
            Gets a `SampleClockTimingParameters` instance
            that represents the settings of timing.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._sample_clock_timing_parameters

    @property
    def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters:
        """
        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._digital_start_trigger_parameters


class PowerSupplySourceAndMeasureResultData(PCBATestToolkitData):
    """Defines the result values computed after analysing
    voltage and current waveforms from Power Supply Source."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (355 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        voltage_waveform: AnalogWaveform,
        current_waveform: AnalogWaveform,
        max_voltage_level_volts: float,
        max_current_level_amperes: float,
        max_power_level_watts: float,
        average_power_value_watts: float,
        acquisition_duration_seconds: float,
    ) -> None:
        """Constructor that initializes
        a new object of PowerSupplySourceAndMeasureResultData with specific values.

        Args:
            voltage_waveform (AnalogWaveform):
                A collection of samples representing the voltage values captured in the waveform.
            current_waveform (AnalogWaveform):
                A collection of samples representing the current values captured in the waveform.
            max_voltage_level_volts (float):
                The maximum voltage level value (in Volts).
            max_current_level_amperes (float):
                The maximum current level value (in Amperes).
            max_power_level_watts (float):
                The maximum power level value (in Watts).
            average_power_value_watts (float):
                The average power value (in Watts).
            acquisition_duration_seconds (float):
                The total acquisition time by the instrument in seconds.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(voltage_waveform, nameof(voltage_waveform))
        Guard.is_not_none(current_waveform, nameof(current_waveform))

        self._voltage_waveform = voltage_waveform
        self._current_waveform = current_waveform
        self._max_voltage_level_volts = max_voltage_level_volts
        self._max_current_level_amperes = max_current_level_amperes
        self._max_power_level_watts = max_power_level_watts
        self._average_power_value_watts = average_power_value_watts
        self._acquisition_duration_seconds = acquisition_duration_seconds

    @property
    def voltage_waveform(self) -> AnalogWaveform:
        """
        :class:`AnalogWaveform`:
            Gets the voltage waveforms acquired from channels defined
            for measurement and used to compute power measurements.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._voltage_waveform

    @property
    def current_waveform(self) -> AnalogWaveform:
        """
        :class:`AnalogWaveform`:
            Gets the current waveforms acquired from channels defined
            for measurement and used to compute power measurements.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._current_waveform

    @property
    def max_voltage_level_volts(self) -> float:
        """
        :type:`float`:
            Gets the maximum voltage level value (in Volts).
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._max_voltage_level_volts

    @property
    def max_current_level_amperes(self) -> float:
        """
        :type:`float`:
            Gets the maximum current level value (in Amperes).
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._max_current_level_amperes

    @property
    def max_power_level_watts(self) -> float:
        """
        :type:`float`:
            Gets the maximum power level value (in Watts).
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._max_power_level_watts

    @property
    def average_power_value_watts(self) -> float:
        """
        :type:`float`:
            Gets the average power value (in Watts).
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._average_power_value_watts

    @property
    def acquisition_duration_seconds(self) -> float:
        """
        :type:`float`:
            Gets the duration of acquisition of samples for each of the power channel.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._acquisition_duration_seconds


class PowerSupplySourceAndMeasureData(PCBATestToolkitData):
    """
    Defines the voltage and current waveform acquired from power channels.
    """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (105 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        source_name: str,
        voltage_samples: numpy.ndarray,
        current_samples: numpy.ndarray,
        sampling_rate_hertz: int,
    ):
        """Initializes an instance of `PowerSupplySourceAndMeasureData`
           with specific values.

        Args:
            source_name (str): The name of channel on which waveform was captured.
            voltage_samples (numpy.ndarray): A collection of samples
            representing the voltage values captured in the waveform.
            Note: argument cannot be None or an empty array.

            current_samples (numpy.ndarray): A collection of samples
            representing the current values captured in the waveform.
            Note: argument cannot be None or an empty array.

            sampling_rate_hertz (int): The sampling rate (in Hz).
            Note: argument cannot be None or zero.

            voltage_samples, current_samples, and sampling_rate_hertz ca
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._source_name = source_name

        Guard.is_greater_than_zero(
            sampling_rate_hertz,
            nameof(sampling_rate_hertz),
        )
        self._sampling_rate_hertz = sampling_rate_hertz

        Guard.is_not_none(voltage_samples, nameof(voltage_samples))
        Guard.is_not_none(current_samples, nameof(current_samples))

        if numpy.size(voltage_samples) > 0:
            self._voltage_samples = voltage_samples
        else:
            raise ValueError("voltage_samples cannot be empty")

        if numpy.size(current_samples) > 0:
            self._current_samples = current_samples
        else:
            raise ValueError("current_samples cannot be empty")

    @property
    def source_name(self) -> str:
        """
        :type:`str`: Gets the name of channel on which waveform was captured.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        return self._source_name

    @property
    def voltage_samples(self) -> numpy.ndarray:
        """
        :class:`numpy.ndarray`:
            Gets the array of samples from the voltage waveform.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._voltage_samples

    @property
    def current_samples(self) -> numpy.ndarray:
        """
        :class:`numpy.ndarray`:
            Gets the array of samples from the current waveform.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._current_samples

    @property
    def sampling_rate_hertz(self) -> int:
        """Gets the sampling rate (in Hz)."""
        return self._sampling_rate_hertz
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/signal_voltage_generations/__init__.py sha256=6962f1dcaadd9759dbb810fcd1b25834d57e24fae07a2b81d9ce07bc82dca747 bytes=248 -->
## FILE: src/nipcbatt/pcbatt_library/daq/signal_voltage_generations/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/signal_voltage_generations/__init__.py`
- sha256: `6962f1dcaadd9759dbb810fcd1b25834d57e24fae07a2b81d9ce07bc82dca747`
- bytes: 248

````python
"""Provides nipcbatt library signal voltage generation modules"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (176 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/signal_voltage_generations/signal_voltage_data_types.py sha256=048690896f0b6c11c44e5883daec6ab13db0b9b049f86b05f5b1cd7baa9a8692 bytes=32011 -->
## FILE: src/nipcbatt/pcbatt_library/daq/signal_voltage_generations/signal_voltage_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/signal_voltage_generations/signal_voltage_data_types.py`
- sha256: `048690896f0b6c11c44e5883daec6ab13db0b9b049f86b05f5b1cd7baa9a8692`
- bytes: 32011

````python
""" Signal Voltage Generation data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (155 > 100 characters) (auto-generated noqa)

from typing import List

from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
)
from nipcbatt.pcbatt_library.daq.common.voltage_data_types import (
    VoltageGenerationChannelParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class ToneParameters(PCBATestToolkitData):
    """Defines the settings of a tone used to generate a signal."""

    def __init__(
        self,
        tone_frequency_hertz: float,
        tone_amplitude_volts: float,
        tone_phase_radians: float,
    ) -> None:
        """Initializes an instance of `ToneParameters` with specific values.

        Args:
            tone_frequency_hertz (float):
                The frequency value of the tone, in Hertz
            tone_amplitude_volts (float):
                The amplitude value of the tone, in Volts
            tone_phase_radians (float):
                The phase value of the tone, in Radians
        """
        Guard.is_greater_than_zero(tone_frequency_hertz, nameof(tone_frequency_hertz))
        Guard.is_greater_than_zero(tone_amplitude_volts, nameof(tone_amplitude_volts))

        self._tone_frequency_hertz = tone_frequency_hertz
        self._tone_amplitude_volts = tone_amplitude_volts
        self._tone_phase_radians = tone_phase_radians

    @property
    def tone_frequency_hertz(self) -> float:
        """Gets the frequency value of the tone, in Hertz."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (147 > 100 characters) (auto-generated noqa)

        return self._tone_frequency_hertz

    @property
    def tone_amplitude_volts(self) -> float:
        """Gets the amplitude value of the tone, in Volts"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (248 > 100 characters) (auto-generated noqa)

        return self._tone_amplitude_volts

    @property
    def tone_phase_radians(self) -> float:
        """Gets the phase value of the tone, in Radians."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (145 > 100 characters) (auto-generated noqa)

        return self._tone_phase_radians


class SignalVoltageGenerationTimingParameters(PCBATestToolkitData):
    """Defines the settings of sample clock timing for signal voltage generation."""

    def __init__(
        self,
        sample_clock_source: str,
        sampling_rate_hertz: int,
        generated_signal_duration_seconds: float,
    ) -> None:
        """Used to initialize an instance of `SampleClockTimingParameters`.

        Args:
            sample_clock_source (str): The source of the clock.
            sampling_rate_hertz (int): The sampling rate (in Hz).
            generated_signal_duration_seconds (float):
                The duration in seconds for which the signal needs to be generated.

        Raises:
            ValueError:
                Raised if `sample_clock_source` is None or empty or white space,
                if `sampling_rate_hertz` is less than or equal to zero.
                If the `generated_signal_duration_seconds' is less than or equal to zero.
        """
        Guard.is_not_none_nor_empty_nor_whitespace(sample_clock_source, nameof(sample_clock_source))
        Guard.is_greater_than_zero(sampling_rate_hertz, nameof(sampling_rate_hertz))
        Guard.is_greater_than_zero(
            generated_signal_duration_seconds, nameof(generated_signal_duration_seconds)
        )

        self._sample_clock_source = sample_clock_source
        self._sampling_rate_hertz = sampling_rate_hertz
        self._generated_signal_duration_seconds = generated_signal_duration_seconds

    @property
    def sample_clock_source(self) -> str:
        """Gets the source of the clock."""
        return self._sample_clock_source

    @property
    def sampling_rate_hertz(self) -> int:
        """Gets the sampling rate (in Hz)."""
        return self._sampling_rate_hertz

    @property
    def generated_signal_duration_seconds(self) -> float:
        """Gets the duration of the generated signal voltage."""
        return self._generated_signal_duration_seconds


class SignalVoltageGenerationSineWaveParameters(PCBATestToolkitData):
    """Defines the parameters used to configure generation of sine wave signal voltage."""

    def __init__(
        self,
        generated_signal_offset_volts: float,
        generated_signal_tone_parameters: ToneParameters,
    ) -> None:
        """Initializes an instance of `SignalVoltageGenerationSineWaveParameters` with specific values.

        Args:
            generated_signal_offset_volts (float):
                The offset of the generated signal voltage.
            generated_signal_tone_parameters (ToneParameters):
                The tone settings of the generated signal.

        Raises:
            ValueError:
                if the `generated_signal_tone_parameters' is None
        """  # noqa: W505 - doc line too long (103 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(
            generated_signal_tone_parameters, nameof(generated_signal_tone_parameters)
        )

        self._generated_signal_offset_volts = generated_signal_offset_volts
        self._generated_signal_tone_parameters = generated_signal_tone_parameters

    @property
    def generated_signal_offset_volts(self) -> float:
        """Gets the offset of the generated signal voltage."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (148 > 100 characters) (auto-generated noqa)

        return self._generated_signal_offset_volts

    @property
    def generated_signal_tone_parameters(self) -> ToneParameters:
        """Gets the tone settings of the generated signal"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (248 > 100 characters) (auto-generated noqa)

        return self._generated_signal_tone_parameters


class SignalVoltageGenerationSquareWaveParameters(PCBATestToolkitData):
    """Defines the parameters used to configure generation of square wave signal voltage."""

    def __init__(
        self,
        generated_signal_offset_volts: float,
        generated_signal_frequency_hertz: float,
        generated_signal_amplitude_volts: float,
        generated_signal_duty_cycle_percent: float,
        generated_signal_phase_radians: float,
    ) -> None:
        """Initializes an instance of `SignalVoltageGenerationSquareWaveParameters` with specific values.

        Args:
            generated_signal_offset_volts (float):
                The offset of the generated signal voltage in volts.
            generated_signal_frequency_hertz (float):
                The frequency value of the square wave, in Hertz
            generated_signal_amplitude_volts (float):
                The amplitude value of the square wave, in volts
            generated_signal_duty_cycle_percent (float):
                The duty cycle of the square wave, in percent.
            generated_signal_phase_radians(float):
                The phase value of the square wave, in radians

        Raises:
            ValueError:
                If the value of `generated_signal_frequency_hertz` is less than or equal to 0
                If the value of `generated_signal_amplitude_volts` is less than or equal to 0
                If the value of `generated_signal_duty_cycle_percent` is not between 0 and 100
        """  # noqa: W505 - doc line too long (105 > 100 characters) (auto-generated noqa)
        Guard.is_greater_than_zero(
            generated_signal_frequency_hertz, nameof(generated_signal_frequency_hertz)
        )
        Guard.is_greater_than_zero(
            generated_signal_amplitude_volts, nameof(generated_signal_amplitude_volts)
        )
        Guard.is_within_limits_excluded(
            value=generated_signal_duty_cycle_percent,
            lower_limit=0,
            upper_limit=100,
            value_name=nameof(generated_signal_duty_cycle_percent),
        )

        self._generated_signal_offset_volts = generated_signal_offset_volts
        self._generated_signal_frequency_hertz = generated_signal_frequency_hertz
        self._generated_signal_amplitude_volts = generated_signal_amplitude_volts
        self._generated_signal_duty_cycle_percent = generated_signal_duty_cycle_percent
        self._generated_signal_phase_radians = generated_signal_phase_radians

    @property
    def generated_signal_offset_volts(self) -> float:
        """Gets the offset of the generated signal voltage."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (148 > 100 characters) (auto-generated noqa)

        return self._generated_signal_offset_volts

    @property
    def generated_signal_frequency_hertz(self) -> float:
        """Gets the frequency value of the square wave, in Hertz."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (154 > 100 characters) (auto-generated noqa)

        return self._generated_signal_frequency_hertz

    @property
    def generated_signal_amplitude_volts(self) -> float:
        """Gets the amplitude value of the square wave, in Volts."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (154 > 100 characters) (auto-generated noqa)

        return self._generated_signal_amplitude_volts

    @property
    def generated_signal_duty_cycle_percent(self) -> float:
        """Gets the duty cycle of the square wave, in percent."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (151 > 100 characters) (auto-generated noqa)

        return self._generated_signal_duty_cycle_percent

    @property
    def generated_signal_phase_radians(self) -> float:
        """Gets the phase value of the square wave, in radians."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (152 > 100 characters) (auto-generated noqa)

        return self._generated_signal_phase_radians


class SignalVoltageGenerationMultipleTonesWaveParameters(PCBATestToolkitData):
    """Defines the parameters used to configure generation of (multi-tone)
    signal voltage with one or more sine waves (sum of sinusoid)."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (361 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        generated_signal_offset_volts: float,
        generated_signal_amplitude_volts: float,
        multiple_tones_parameters: List[ToneParameters],
    ) -> None:
        """Initializes an instance of `SignalVoltageGenerationMultipleTonesWaveParameters`
         with specific values.

        Args:
            generated_signal_offset_volts (float):
                The offset of the generated signal voltage.
            generated_signal_amplitude_volts (float):
                The Amplitude value used to rescale the resulted sine wave.
            multiple_tones_parameters (List[ToneParameters]):
                The List of `ToneParameters` representing the settings of each
                 sine wave in generated signal voltage.

        Raises:
            ValueError:
                If the `generated_signal_amplitude_volts' is less than or equal to zero.
                if the `generated_signal_tone_parameters' is None or empty List
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        Guard.is_greater_than_zero(
            generated_signal_amplitude_volts, nameof(generated_signal_amplitude_volts)
        )

        Guard.is_not_none(multiple_tones_parameters, nameof(multiple_tones_parameters))
        Guard.is_not_empty(multiple_tones_parameters, nameof(multiple_tones_parameters))

        self._generated_signal_offset_volts = generated_signal_offset_volts
        self._generated_signal_amplitude_volts = generated_signal_amplitude_volts
        self._multiple_tones_parameters = multiple_tones_parameters

    @property
    def generated_signal_offset_volts(self) -> float:
        """Gets the offset of the generated signal voltage."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (148 > 100 characters) (auto-generated noqa)

        return self._generated_signal_offset_volts

    @property
    def generated_signal_amplitude_volts(self) -> float:
        """Gets the Amplitude value used to rescale the resulted sine wave."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (164 > 100 characters) (auto-generated noqa)

        return self._generated_signal_amplitude_volts

    @property
    def multiple_tones_parameters(self) -> List[ToneParameters]:
        """Gets the List `ToneSettings` representing the settings of
        each sine wave in generated signal voltage."""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (424 > 100 characters) (auto-generated noqa)

        return self._multiple_tones_parameters


class SignalVoltageGenerationSineWaveConfiguration(PCBATestToolkitData):
    """Defines the parameters used for configuration of sine wave signal generation"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (197 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        voltage_generation_range_parameters: VoltageGenerationChannelParameters,
        waveform_parameters: SignalVoltageGenerationSineWaveParameters,
        timing_parameters: SignalVoltageGenerationTimingParameters,
        digital_start_trigger_parameters: DigitalStartTriggerParameters,
    ) -> None:
        """Initializes an instance of
        `SignalVoltageGenerationSineWaveConfiguration` with specific values.

        Args:
            voltage_generation_range_parameters (VoltageGenerationChannelParameters):
                An instance of `VoltageGenerationChannelParameters' used to configure the channels.
            waveform_parameters (SignalVoltageGenerationSineWaveParameters):
                An instance of `SignalVoltageGenerationSineWaveParameters`
                used to configure the generation of sine wave signal voltage.
            timing_parameters (SignalVoltageGenerationTimingParameters):
                An instance of SignalVoltageGenerationTimingParameters that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters` that represents the settings of triggers.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (110 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(
            voltage_generation_range_parameters,
            nameof(voltage_generation_range_parameters),
        )
        Guard.is_not_none(
            waveform_parameters,
            nameof(waveform_parameters),
        )
        Guard.is_not_none(
            timing_parameters,
            nameof(timing_parameters),
        )
        Guard.is_not_none(
            digital_start_trigger_parameters,
            nameof(digital_start_trigger_parameters),
        )

        self._voltage_generation_range_parameters = voltage_generation_range_parameters
        self._waveform_parameters = waveform_parameters
        self._timing_parameters = timing_parameters
        self._digital_start_trigger_parameters = digital_start_trigger_parameters

    @property
    def voltage_generation_range_parameters(self) -> VoltageGenerationChannelParameters:
        """
        :class:`VoltageGenerationChannelParameters`:
            Gets an instance of `VoltageGenerationChannelParameters'
            that represents the terminal settings for all channel for signal voltage generation.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._voltage_generation_range_parameters

    @property
    def waveform_parameters(
        self,
    ) -> SignalVoltageGenerationSineWaveParameters:
        """
        :class:`SignalVoltageGenerationSineWaveParameters`:
            Gets an instance of `SignalVoltageGenerationSineWaveParameters`
            used to configure the generation of sine wave signal voltage.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._waveform_parameters

    @property
    def timing_parameters(self) -> SignalVoltageGenerationTimingParameters:
        """
        :class:`SignalVoltageGenerationTimingParameters`:
            Gets a `SignalVoltageGenerationTimingParameters` instance
            that represents the settings of timing.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._timing_parameters

    @property
    def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters:
        """
        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._digital_start_trigger_parameters


class SignalVoltageGenerationSquareWaveConfiguration(PCBATestToolkitData):
    """Defines the parameters used for configuration of square wave signal generation"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        voltage_generation_range_parameters: VoltageGenerationChannelParameters,
        waveform_parameters: SignalVoltageGenerationSquareWaveParameters,
        timing_parameters: SignalVoltageGenerationTimingParameters,
        digital_start_trigger_parameters: DigitalStartTriggerParameters,
    ) -> None:
        """Initializes an instance of
        `SignalVoltageGenerationSquareWaveConfiguration` with specific values.

        Args:
            voltage_generation_range_parameters (VoltageGenerationChannelParameters):
                An instance of `VoltageGenerationChannelParameters' used to configure the channels.
            waveform_parameters (SignalVoltageGenerationSquareWaveParameters):
                An instance of `SignalVoltageGenerationSquareWaveParameters`
                used to configure the generation of square wave signal voltage.
            timing_parameters (SignalVoltageGenerationTimingParameters):
                An instance of SignalVoltageGenerationTimingParameters that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters` that represents the settings of triggers.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (110 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(
            voltage_generation_range_parameters,
            nameof(voltage_generation_range_parameters),
        )
        Guard.is_not_none(
            waveform_parameters,
            nameof(waveform_parameters),
        )
        Guard.is_not_none(
            timing_parameters,
            nameof(timing_parameters),
        )
        Guard.is_not_none(
            digital_start_trigger_parameters,
            nameof(digital_start_trigger_parameters),
        )

        self._voltage_generation_range_parameters = voltage_generation_range_parameters
        self._waveform_parameters = waveform_parameters
        self._timing_parameters = timing_parameters
        self._digital_start_trigger_parameters = digital_start_trigger_parameters

    @property
    def voltage_generation_range_parameters(self) -> VoltageGenerationChannelParameters:
        """
        :class:`VoltageGenerationChannelParameters`:
            Gets an instance of `VoltageGenerationChannelParameters'
            that represents the terminal settings for all channel for signal voltage generation.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._voltage_generation_range_parameters

    @property
    def waveform_parameters(
        self,
    ) -> SignalVoltageGenerationSquareWaveParameters:
        """
        :class:`SignalVoltageGenerationSquareWaveParameters`:
            Gets an instance of `SignalVoltageGenerationSquareWaveParameters`
            used to configure the generation of square wave signal voltage.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._waveform_parameters

    @property
    def timing_parameters(self) -> SignalVoltageGenerationTimingParameters:
        """
        :class:`SignalVoltageGenerationTimingParameters`:
            Gets a `SignalVoltageGenerationTimingParameters` instance
            that represents the settings of timing.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._timing_parameters

    @property
    def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters:
        """
        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._digital_start_trigger_parameters


class SignalVoltageGenerationMultipleTonesConfiguration(PCBATestToolkitData):
    """Defines the parameters used for configuration of multi-tone sine wave signal generation"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (208 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        voltage_generation_range_parameters: VoltageGenerationChannelParameters,
        waveform_parameters: SignalVoltageGenerationMultipleTonesWaveParameters,
        timing_parameters: SignalVoltageGenerationTimingParameters,
        digital_start_trigger_parameters: DigitalStartTriggerParameters,
    ) -> None:
        """Initializes an instance of
        `SignalVoltageGenerationMultipleTonesConfiguration` with specific values.

        Args:
            voltage_generation_range_parameters (VoltageGenerationChannelParameters):
                An instance of `VoltageGenerationChannelParameters' used to configure the channels.
            waveform_parameters (SignalVoltageGenerationMultipleTonesWaveParameters):
                An instance of `SignalVoltageGenerationMultipleTonesWaveParameters`
                used to configure the generation of sine wave signal voltage.
            timing_parameters (SignalVoltageGenerationTimingParameters):
                An instance of `SignalVoltageGenerationTimingParameters` that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters` that represents the settings of triggers.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (112 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(
            voltage_generation_range_parameters,
            nameof(voltage_generation_range_parameters),
        )
        Guard.is_not_none(
            waveform_parameters,
            nameof(waveform_parameters),
        )
        Guard.is_not_none(
            timing_parameters,
            nameof(timing_parameters),
        )
        Guard.is_not_none(
            digital_start_trigger_parameters,
            nameof(digital_start_trigger_parameters),
        )

        self._voltage_generation_range_parameters = voltage_generation_range_parameters
        self._waveform_parameters = waveform_parameters
        self._timing_parameters = timing_parameters
        self._digital_start_trigger_parameters = digital_start_trigger_parameters

    @property
    def voltage_generation_range_parameters(self) -> VoltageGenerationChannelParameters:
        """
        :class:`VoltageGenerationChannelParameters`:
            Gets an instance of `VoltageGenerationChannelParameters'
            that represents the terminal settings for all channel for signal voltage generation.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._voltage_generation_range_parameters

    @property
    def waveform_parameters(
        self,
    ) -> SignalVoltageGenerationMultipleTonesWaveParameters:
        """
        :class:`SignalVoltageGenerationMultipleTonesWaveParameters`:
            Gets an instance of `SignalVoltageGenerationMultipleTonesWaveParameters`
            used to configure the generation of multi-tone sine wave signal voltage.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._waveform_parameters

    @property
    def timing_parameters(self) -> SignalVoltageGenerationTimingParameters:
        """
        :class:`SignalVoltageGenerationTimingParameters`:
            Gets a `SignalVoltageGenerationTimingParameters` instance
            that represents the settings of timing.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._timing_parameters

    @property
    def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters:
        """
        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._digital_start_trigger_parameters
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/signal_voltage_generations/signal_voltage_generation.py sha256=ba1ae4e388ded095a65bbfb627b0972db60bce5008eecb760fb376eab7b47bf2 bytes=18702 -->
## FILE: src/nipcbatt/pcbatt_library/daq/signal_voltage_generations/signal_voltage_generation.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/signal_voltage_generations/signal_voltage_generation.py`
- sha256: `ba1ae4e388ded095a65bbfb627b0972db60bce5008eecb760fb376eab7b47bf2`
- bytes: 18702

````python
"""Defines class used for generation of signal voltage on PCB points."""

import math

import nidaqmx.constants
import nidaqmx.stream_writers
import numpy as np

from nipcbatt.pcbatt_analysis.waveform_creation import (
    multitones_waveform,
    sine_waveform,
    square_waveform,
)
from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.daq.common.voltage_data_types import (
    VoltageGenerationChannelParameters,
)
from nipcbatt.pcbatt_library.daq.signal_voltage_generations.signal_voltage_data_types import (
    SignalVoltageGenerationMultipleTonesConfiguration,
    SignalVoltageGenerationMultipleTonesWaveParameters,
    SignalVoltageGenerationSineWaveConfiguration,
    SignalVoltageGenerationSineWaveParameters,
    SignalVoltageGenerationSquareWaveConfiguration,
    SignalVoltageGenerationSquareWaveParameters,
    SignalVoltageGenerationTimingParameters,
)
from nipcbatt.pcbatt_library.daq.signal_voltage_generations.signal_voltage_generation_constants import (
    ConstantsForSignalVoltageGeneration,
)
from nipcbatt.pcbatt_library.daq.synchronizations.synchronization_signal_routing import (
    SynchronizationSignalRouting,
)
from nipcbatt.pcbatt_utilities import numeric_utilities


class SignalVoltageGeneration(SynchronizationSignalRouting):
    """Provides a way that allows you to generate signal voltage and apply it into PCB points."""

    def initialize(self, channel_expression: str):
        """Initializes the analog output channels and obtains
        the Daqmx Task for signal voltage generation.

        Args:
            channel_expression (str):
                Expression representing the name of an analog output physical channel,
                or a global channel in DAQ System.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        if self.is_task_initialized:
            return

        # If the input channel_expression contains global channel, then add them as global channels
        # and verify if the global channels are configured for analog output voltage.
        if self.contains_only_global_virtual_channels(channel_expression=channel_expression):
            self.add_global_channels(global_channel_expression=channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
            self.verify_generation_type(nidaqmx.constants.UsageTypeAO.VOLTAGE)
        else:
            # Add the channel_expression to analog output channel of the Daqmx task
            self.task.ao_channels.add_ao_voltage_chan(
                physical_channel=channel_expression,
                min_val=ConstantsForSignalVoltageGeneration.INITIAL_RANGE_MIN_VOLTS,
                max_val=ConstantsForSignalVoltageGeneration.INITIAL_RANGE_MAX_VOLTS,
                units=ConstantsForSignalVoltageGeneration.INITIAL_AO_VOLTAGE_UNITS,
            )

    def configure_all_channels(
        self,
        parameters: VoltageGenerationChannelParameters,
    ) -> None:
        """Configures all analog output channels for Signal Voltage generation.

        Args:
            parameters (VoltageGenerationChannelParameters):
            An instance of `VoltageGenerationChannelParameters` used
            to configure the analog output channels.
        """  # noqa: D202, D417, W505 - No blank lines allowed after function docstring (auto-generated noqa), Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

        for channel in self.task.ao_channels:
            channel.ao_min = parameters.range_min_volts
            channel.ao_max = parameters.range_max_volts
            # channel.ao_term_cfg = nidaqmx.constants.TerminalConfiguration.RSE

    def configure_timing(self, parameters: SignalVoltageGenerationTimingParameters):
        """Configures the timing characteristics used for Current measurements.

        Args:
            parameters (SampleClockTimingParameters): An instance of `SampleClockTimingParameters`
                used to configure the timing.
        """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

        self.task.timing.cfg_samp_clk_timing(
            rate=parameters.sampling_rate_hertz,
            sample_mode=nidaqmx.constants.AcquisitionType.FINITE,
            samps_per_chan=self._get_generated_signal_samples_count(
                sampling_rate_hertz=parameters.sampling_rate_hertz,
                generated_signal_duration_seconds=parameters.generated_signal_duration_seconds,
            ),
            source=parameters.sample_clock_source,
        )

    def _get_generated_signal_samples_count(
        self, sampling_rate_hertz, generated_signal_duration_seconds
    ) -> int:
        """Calculates the number of samples that will be in the generated signal"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (194 > 100 characters) (auto-generated noqa)
        return math.ceil(sampling_rate_hertz * generated_signal_duration_seconds)

    def configure_trigger(self, parameters: DigitalStartTriggerParameters):
        """Configure the characteristics of triggers used for Current measurements.

        Args:
            parameters (DigitalStartTriggerParameters):
            An instance of `DigitalStartTriggerParameters`
            used to configure the channels.
        """  # noqa: D202, D417, W505 - No blank lines allowed after function docstring (auto-generated noqa), Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

        if parameters.trigger_select == StartTriggerType.NO_TRIGGER:
            self.task.triggers.start_trigger.disable_start_trig()
        else:
            self.task.triggers.start_trigger.cfg_dig_edge_start_trig(
                trigger_source=parameters.digital_start_trigger_source,
                trigger_edge=parameters.digital_start_trigger_edge,
            )

    def generate_voltage_sine_waveform(
        self,
        signal_parameters: SignalVoltageGenerationSineWaveParameters,
        timing_parameters: SignalVoltageGenerationTimingParameters,
    ) -> None:
        """Generates a signal that is a sine wave according to `signal_parameters`.

        Args:
            signal_parameters (SignalVoltageGenerationSineWaveParameters):
                An instance of `SignalVoltageGenerationSineWaveParameters`
                used to configure the signal to generate.
            timing_parameters (SignalVoltageGenerationTimingParameters):
                An instance of `SignalVoltageGenerationTimingParameters` used
                to configure the sample rate and duration of the signal to be generated.
        """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

        waveform_samples_count = self._get_generated_signal_samples_count(
            sampling_rate_hertz=timing_parameters.sampling_rate_hertz,
            generated_signal_duration_seconds=timing_parameters.generated_signal_duration_seconds,
        )

        samples_to_write = sine_waveform.create_sine_waveform(
            amplitude=signal_parameters.generated_signal_tone_parameters.tone_amplitude_volts,
            frequency=signal_parameters.generated_signal_tone_parameters.tone_frequency_hertz,
            phase=signal_parameters.generated_signal_tone_parameters.tone_phase_radians,
            offset=signal_parameters.generated_signal_offset_volts,
            samples_count=waveform_samples_count,
            sampling_rate=timing_parameters.sampling_rate_hertz,
        )

        # build a numpy 2D array (number of row is the number of output channels)
        # from the numpy 1D array
        samples_to_write = np.tile(samples_to_write, (self.task.out_stream.num_chans, 1))

        writer = nidaqmx.stream_writers.AnalogMultiChannelWriter(
            self.task.out_stream, auto_start=True
        )
        writer.write_many_sample(samples_to_write)

    def generate_voltage_square_waveform(
        self,
        signal_parameters: SignalVoltageGenerationSquareWaveParameters,
        timing_parameters: SignalVoltageGenerationTimingParameters,
    ) -> None:
        """Creates a signal that is a square wave.

        Args:
            signal_parameters (SignalVoltageGenerationSquareWaveParameters):
                An instance of `SignalVoltageGenerationSquareWaveParameters`
                used to configure the signal to generate.
            timing_parameters (SignalVoltageGenerationTimingParameters):
                An instance of `SignalVoltageGenerationTimingParameters` used
                to configure the sample rate and duration of the signal to be generated.
        """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

        waveform_samples_count = self._get_generated_signal_samples_count(
            sampling_rate_hertz=timing_parameters.sampling_rate_hertz,
            generated_signal_duration_seconds=timing_parameters.generated_signal_duration_seconds,
        )

        samples_to_write = square_waveform.create_square_waveform(
            amplitude=signal_parameters.generated_signal_amplitude_volts,
            frequency=signal_parameters.generated_signal_frequency_hertz,
            duty_cycle=numeric_utilities.from_percent_to_decimal_ratio(
                percent=signal_parameters.generated_signal_duty_cycle_percent
            ),
            phase=signal_parameters.generated_signal_phase_radians,
            offset=signal_parameters.generated_signal_offset_volts,
            samples_count=waveform_samples_count,
            sampling_rate=timing_parameters.sampling_rate_hertz,
        )

        # build a numpy 2D array (number of row is the number of output channels)
        # from the numpy 1D array
        samples_to_write = np.tile(samples_to_write, (self.task.out_stream.num_chans, 1))

        writer = nidaqmx.stream_writers.AnalogMultiChannelWriter(
            self.task.out_stream, auto_start=True
        )
        writer.write_many_sample(data=samples_to_write)

    def generate_voltage_multi_tones_waveform(
        self,
        signal_parameters: SignalVoltageGenerationMultipleTonesWaveParameters,
        timing_parameters: SignalVoltageGenerationTimingParameters,
    ) -> None:
        """Generates a signal that contains sum of multiple sine waves at different tones
        (amplitudes and frequencies).

        Args:
            signal_parameters (SignalVoltageGenerationMultipleTonesWaveParameters):
                An instance of `SignalVoltageGenerationMultipleTonesWaveParameters`
                    used to configure the signal to generate.
            timing_parameters (SignalVoltageGenerationTimingParameters):
                An instance of `SignalVoltageGenerationTimingParameters` used
                to configure the sample rate and duration of the signal to be generated.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        waveform_samples_count = self._get_generated_signal_samples_count(
            sampling_rate_hertz=timing_parameters.sampling_rate_hertz,
            generated_signal_duration_seconds=timing_parameters.generated_signal_duration_seconds,
        )

        waveform_tones_input = list(
            map(
                lambda tone_parameters: multitones_waveform.WaveformTone(
                    frequency=tone_parameters.tone_frequency_hertz,
                    amplitude=tone_parameters.tone_amplitude_volts,
                    phase_radians=tone_parameters.tone_phase_radians,
                ),
                signal_parameters.multiple_tones_parameters,
            )
        )

        samples_to_write = multitones_waveform.create_multitones_waveform(
            multitones_amplitude=signal_parameters.generated_signal_amplitude_volts,
            waveform_tones=waveform_tones_input,
            samples_count=waveform_samples_count,
            sampling_rate=timing_parameters.sampling_rate_hertz,
        )

        # build a numpy 2D array (number of row is the number of output channels)
        # from the numpy 1D array
        samples_to_write = np.tile(samples_to_write, (self.task.out_stream.num_chans, 1))

        writer = nidaqmx.stream_writers.AnalogMultiChannelWriter(
            self.task.out_stream, auto_start=True
        )
        writer.write_many_sample(data=samples_to_write)

    def configure_and_generate_sine_waveform(
        self,
        configuration: SignalVoltageGenerationSineWaveConfiguration,
    ) -> None:
        """Configures and generates the Sine wave according to the specific configuration.

        Args:
            configuration (SignalVoltageGenerationSineWaveConfiguration):
                An instance of `SignalVoltageGenerationSineWaveConfiguration`
                used to configure the generation of single tone sine voltage signal at the channel.
        """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

        self.configure_all_channels(parameters=configuration.voltage_generation_range_parameters)

        self.configure_timing(
            parameters=SignalVoltageGenerationTimingParameters(
                sample_clock_source=configuration.timing_parameters.sample_clock_source,
                sampling_rate_hertz=configuration.timing_parameters.sampling_rate_hertz,
                generated_signal_duration_seconds=(
                    configuration.timing_parameters.generated_signal_duration_seconds
                ),
            )
        )
        self.configure_trigger(parameters=configuration.digital_start_trigger_parameters)

        self.generate_voltage_sine_waveform(
            signal_parameters=configuration.waveform_parameters,
            timing_parameters=configuration.timing_parameters,
        )

    def configure_and_generate_square_waveform(
        self,
        configuration: SignalVoltageGenerationSquareWaveConfiguration,
    ) -> None:
        """Configures and generates a Square wave voltage signal according
        to the specific configuration.

        Args:
            configuration (SignalVoltageGenerationSquareWaveConfiguration):
                An instance of `SignalVoltageGenerationSquareWaveConfiguration`
                used to configure the generation of square wave voltage signal at the channel.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        self.configure_all_channels(parameters=configuration.voltage_generation_range_parameters)

        self.configure_timing(
            parameters=SignalVoltageGenerationTimingParameters(
                sample_clock_source=configuration.timing_parameters.sample_clock_source,
                sampling_rate_hertz=configuration.timing_parameters.sampling_rate_hertz,
                generated_signal_duration_seconds=(
                    configuration.timing_parameters.generated_signal_duration_seconds
                ),
            )
        )
        self.configure_trigger(parameters=configuration.digital_start_trigger_parameters)

        self.generate_voltage_square_waveform(
            signal_parameters=configuration.waveform_parameters,
            timing_parameters=configuration.timing_parameters,
        )

    def configure_and_generate_multiple_tones_waveform(
        self,
        configuration: SignalVoltageGenerationMultipleTonesConfiguration,
    ) -> None:
        """Configures and generates a multi-tone sine wave voltage signal according
        to the specific configuration.

        Args:
            configuration (SignalVoltageGenerationMultipleTonesConfiguration):
                An instance of `SignalVoltageGenerationMultipleTonesConfiguration`
                used to configure the generation of multi-tones voltage waveform at the channel.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        self.configure_all_channels(parameters=configuration.voltage_generation_range_parameters)

        self.configure_timing(
            parameters=SignalVoltageGenerationTimingParameters(
                sample_clock_source=configuration.timing_parameters.sample_clock_source,
                sampling_rate_hertz=configuration.timing_parameters.sampling_rate_hertz,
                generated_signal_duration_seconds=(
                    configuration.timing_parameters.generated_signal_duration_seconds
                ),
            )
        )
        self.configure_trigger(parameters=configuration.digital_start_trigger_parameters)

        self.generate_voltage_multi_tones_waveform(
            signal_parameters=configuration.waveform_parameters,
            timing_parameters=configuration.timing_parameters,
        )

    def close(self):
        """Closes generation procedure and releases internal resources."""
        if not self.is_task_initialized:
            return
        # Wait until done
        self.task.wait_until_done()
        super().close()
        # Stop and close the DAQmx task
        self.task.stop()
        self.task.close()
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/signal_voltage_generations/signal_voltage_generation_constants.py sha256=99941cd4406dc70d6c292f7d44e5b24f5201918779f2be27b6f3cba80143e12d bytes=6118 -->
## FILE: src/nipcbatt/pcbatt_library/daq/signal_voltage_generations/signal_voltage_generation_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/signal_voltage_generations/signal_voltage_generation_constants.py`
- sha256: `99941cd4406dc70d6c292f7d44e5b24f5201918779f2be27b6f3cba80143e12d`
- bytes: 6118

````python
""" Constants data types for Signal Voltage Generation Data types."""

import dataclasses

import nidaqmx.constants

from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.daq.common.voltage_data_types import (
    VoltageGenerationChannelParameters,
)
from nipcbatt.pcbatt_library.daq.signal_voltage_generations.signal_voltage_data_types import (
    SignalVoltageGenerationMultipleTonesConfiguration,
    SignalVoltageGenerationMultipleTonesWaveParameters,
    SignalVoltageGenerationSineWaveConfiguration,
    SignalVoltageGenerationSineWaveParameters,
    SignalVoltageGenerationSquareWaveConfiguration,
    SignalVoltageGenerationSquareWaveParameters,
    SignalVoltageGenerationTimingParameters,
    ToneParameters,
)


@dataclasses.dataclass
class ConstantsForSignalVoltageGeneration:
    """Constants used for signal voltage generation."""

    INITIAL_AO_OUTPUT_TERMINAL_CONFIGURATION = nidaqmx.constants.TerminalConfiguration.RSE
    INITIAL_RANGE_MIN_VOLTS = -10.0
    INITIAL_RANGE_MAX_VOLTS = 10.0
    INITIAL_AO_VOLTAGE_UNITS = nidaqmx.constants.VoltageUnits.VOLTS

    DEFAULT_AO_OUTPUT_TERMINAL_CONFIGURATION = nidaqmx.constants.TerminalConfiguration.RSE
    DEFAULT_RANGE_MIN_VOLTS = -10.0
    DEFAULT_RANGE_MAX_VOLTS = 10.0

    DEFAULT_SIGNAL_DURATION_SECONDS = 0.1
    DEFAULT_SIGNAL_OFFSET_VOLTS = 0
    DEFAULT_SIGNAL_FREQUENCY_HERTZ = 100
    DEFAULT_SIGNAL_AMPLITUDE_VOLTS = 1.0
    DEFAULT_SIGNAL_PHASE_RADIANS = 0
    DEFAULT_SIGNAL_DUTY_CYCLE_PERCENT = 50.0

    DEFAULT_SAMPLE_CLOCK_SOURCE = "OnboardClock"
    DEFAULT_SAMPLING_RATE_HERTZ = 10000
    DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL = int(
        DEFAULT_SIGNAL_DURATION_SECONDS * DEFAULT_SAMPLING_RATE_HERTZ
    )

    DEFAULT_TRIGGER_TYPE = StartTriggerType.NO_TRIGGER
    DEFAULT_DIGITAL_START_TRIGGER_SOURCE = ""
    DEFAULT_DIGITAL_START_TRIGGER_EDGE = nidaqmx.constants.Edge.RISING


DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS = VoltageGenerationChannelParameters(
    range_min_volts=ConstantsForSignalVoltageGeneration.DEFAULT_RANGE_MIN_VOLTS,
    range_max_volts=ConstantsForSignalVoltageGeneration.DEFAULT_RANGE_MAX_VOLTS,
)

DEFAULT_TONE_PARAMETERS = ToneParameters(
    tone_frequency_hertz=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_FREQUENCY_HERTZ,
    tone_amplitude_volts=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_AMPLITUDE_VOLTS,
    tone_phase_radians=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_PHASE_RADIANS,
)

DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_PARAMETERS = SignalVoltageGenerationSineWaveParameters(
    generated_signal_offset_volts=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_OFFSET_VOLTS,
    generated_signal_tone_parameters=DEFAULT_TONE_PARAMETERS,
)

DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS = SignalVoltageGenerationTimingParameters(
    sample_clock_source=ConstantsForSignalVoltageGeneration.DEFAULT_SAMPLE_CLOCK_SOURCE,
    sampling_rate_hertz=ConstantsForSignalVoltageGeneration.DEFAULT_SAMPLING_RATE_HERTZ,
    generated_signal_duration_seconds=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_DURATION_SECONDS,
)

DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS = DigitalStartTriggerParameters(
    trigger_select=ConstantsForSignalVoltageGeneration.DEFAULT_TRIGGER_TYPE,
    digital_start_trigger_source=ConstantsForSignalVoltageGeneration.DEFAULT_DIGITAL_START_TRIGGER_SOURCE,
    digital_start_trigger_edge=ConstantsForSignalVoltageGeneration.DEFAULT_DIGITAL_START_TRIGGER_EDGE,
)

DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_CONFIGURATION = (
    SignalVoltageGenerationSineWaveConfiguration(
        voltage_generation_range_parameters=DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS,
        waveform_parameters=DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_PARAMETERS,
        timing_parameters=DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
        digital_start_trigger_parameters=DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
    )
)

DEFAULT_SIGNAL_VOLTAGE_GENERATION_SQUARE_WAVE_PARAMETERS = SignalVoltageGenerationSquareWaveParameters(
    generated_signal_amplitude_volts=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_AMPLITUDE_VOLTS,
    generated_signal_offset_volts=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_OFFSET_VOLTS,
    generated_signal_frequency_hertz=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_FREQUENCY_HERTZ,
    generated_signal_duty_cycle_percent=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_DUTY_CYCLE_PERCENT,
    generated_signal_phase_radians=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_PHASE_RADIANS,
)

DEFAULT_SQUARE_WAVE_GENERATION_CONFIGURATION = SignalVoltageGenerationSquareWaveConfiguration(
    voltage_generation_range_parameters=DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS,
    waveform_parameters=DEFAULT_SIGNAL_VOLTAGE_GENERATION_SQUARE_WAVE_PARAMETERS,
    timing_parameters=DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
    digital_start_trigger_parameters=DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
)

DEFAULT_MULTI_TONE_GENERATION_PARAMETERS = SignalVoltageGenerationMultipleTonesWaveParameters(
    generated_signal_offset_volts=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_OFFSET_VOLTS,
    generated_signal_amplitude_volts=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_AMPLITUDE_VOLTS,
    multiple_tones_parameters=[
        ToneParameters(tone_frequency_hertz=100, tone_amplitude_volts=1.0, tone_phase_radians=0),
        ToneParameters(tone_frequency_hertz=200, tone_amplitude_volts=0.5, tone_phase_radians=0.1),
    ],
)

DEFAULT_MULTI_TONE_GENERATION_CONFIGURATION = SignalVoltageGenerationMultipleTonesConfiguration(
    voltage_generation_range_parameters=DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS,
    waveform_parameters=DEFAULT_MULTI_TONE_GENERATION_PARAMETERS,
    timing_parameters=DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
    digital_start_trigger_parameters=DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/static_digital_state_generations/__init__.py sha256=244a835f52d8941085f19b3a2f852ebdbb1c44217a2ed5b7b7c9caacde4bc9fc bytes=254 -->
## FILE: src/nipcbatt/pcbatt_library/daq/static_digital_state_generations/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/static_digital_state_generations/__init__.py`
- sha256: `244a835f52d8941085f19b3a2f852ebdbb1c44217a2ed5b7b7c9caacde4bc9fc`
- bytes: 254

````python
"""Provides nipcbatt library static digital state generation modules"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (182 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/static_digital_state_generations/static_digital_state_data_types.py sha256=2f2bd819d636f1c2de2448768111c2fbbcb81b45ce08cc65a54caa1917a2bbfc bytes=3681 -->
## FILE: src/nipcbatt/pcbatt_library/daq/static_digital_state_generations/static_digital_state_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/static_digital_state_generations/static_digital_state_data_types.py`
- sha256: `2f2bd819d636f1c2de2448768111c2fbbcb81b45ce08cc65a54caa1917a2bbfc`
- bytes: 3681

````python
""" Static Digital State Generation data types"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (160 > 100 characters) (auto-generated noqa)

from typing import List

from varname import nameof

from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class StaticDigitalStateGenerationConfiguration(PCBATestToolkitData):
    """Defines the values used in the creation of Static Digital State Configuration"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (198 > 100 characters) (auto-generated noqa)

    def __init__(self, data_to_write: List[bool]) -> None:
        """Initializes an instance of 'StaticDigitalStateGenerationConfiguration
           with specific values.

        Args:
            data_to_write (array of boolean):
                The boolean state of each channel to write to the hardware
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # Input validation
        Guard.is_not_none(data_to_write, nameof(data_to_write))
        Guard.is_not_empty(data_to_write, nameof(data_to_write))

        # generate states
        self._data_to_write = data_to_write

    @property
    def data_to_write(self) -> List[bool]:
        """
        :type: array of 'bool': Holds the state of the write values to the DO channels
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._data_to_write


class StaticDigitalStateGenerationData(PCBATestToolkitData):
    """Defines the values used in the production of Static Digital State Generation Data"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (202 > 100 characters) (auto-generated noqa)

    def __init__(self, channel_identifiers: List[str]) -> None:
        """Initializes an instance of StaticDigitalStateGenerationData with specific values.

        Args:
            channel_identifiers (array of string):
                The list of channels to which the data to write is written
        """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

        # Input validation
        Guard.is_not_none(channel_identifiers, nameof(channel_identifiers))
        Guard.is_not_empty(channel_identifiers, nameof(channel_identifiers))

        # generate states
        self._channel_identifiers = channel_identifiers

    @property
    def channel_identifiers(self) -> List[str]:
        """
        :type: array of 'str': Holds the names of the digital output channels to write to
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._channel_identifiers
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/static_digital_state_generations/static_digital_state_generation.py sha256=7ac0bcabe59a81602f4cc1be0735b12eb07883ecf4b15aa48215c30b036d0d97 bytes=6303 -->
## FILE: src/nipcbatt/pcbatt_library/daq/static_digital_state_generations/static_digital_state_generation.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/static_digital_state_generations/static_digital_state_generation.py`
- sha256: `7ac0bcabe59a81602f4cc1be0735b12eb07883ecf4b15aa48215c30b036d0d97`
- bytes: 6303

````python
# pylint: disable=W0613
# remove it when arguments of initialize are used.
"""Use this class to generate digital states to output on system"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (178 > 100 characters) (auto-generated noqa)

from typing import List

import nidaqmx.constants
import nidaqmx.errors
import nidaqmx.stream_writers
import nidaqmx.system
import numpy as np
from nidaqmx.constants import LineGrouping
from varname import nameof

from nipcbatt.pcbatt_library.daq.static_digital_state_generations.static_digital_state_data_types import (
    StaticDigitalStateGenerationConfiguration,
    StaticDigitalStateGenerationData,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryException,
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class StaticDigitalStateGeneration(BuildingBlockUsingDAQmx):
    """This class represents the set of static digital states
       the user wishes to write to digital output lines

    Args:
        BuildingBlockUsingDAQmx (_type_): _description_
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def initialize(self, channel_expression: str):
        """Initializes the task to prepare for generation

        Args:
            channel_expression (str): The name of the lines/port
            where the data will be written
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        self.task.stop()

        if self.is_task_initialized:
            return

        # input validation
        Guard.is_not_none(channel_expression, nameof(channel_expression))
        Guard.is_not_empty(channel_expression, nameof(channel_expression))

        # check to seee if task has only global virtual channels
        if self.contains_only_global_virtual_channels(channel_expression):
            # add global channels to task
            self.add_global_channels(channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)

            # check for presence of global channel ports
            for do_channel in self.task.do_channels:
                if do_channel.do_num_lines != 1:
                    raise PCBATTLibraryException(
                        PCBATTLibraryExceptionMessages.GLOBAL_CHANNEL_PORT_NOT_SUPPORTED_ARGS_3.format(
                            do_channel.name, do_channel.di_num_lines, do_channel.name
                        )
                    )

        else:
            # create virtual channel for each Digital Out line
            self.task.do_channels.add_do_chan(channel_expression, "", LineGrouping.CHAN_PER_LINE)

    def close(self):
        """Closes the task and returns the hardware resource"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (174 > 100 characters) (auto-generated noqa)
        if not self.is_task_initialized:
            return

        # stop and close DAQmx task
        self.task.stop()
        self.task.close()

    def configure_and_generate(
        self, configuration: StaticDigitalStateGenerationConfiguration
    ) -> StaticDigitalStateGenerationData:
        """Uses the configuration provided to generate the digital
           states on the hardware

        Args:
            configuration (StaticDigitalStateGenerationConfiguration): An
            instance of an object that contains the states to generate

        Returns:
            StaticDigitalStateGenerationData: Contains an array of strings
            describing the lines that were written to
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        return self.generate_digital_states(configuration.data_to_write)

    def generate_digital_states(
        self, output_states: List[bool]
    ) -> StaticDigitalStateGenerationData:
        """This method takes the states the user wishes to generate
           and creates a StaticDigitalStateGenerationData object

        Args:
            output_states (List[bool]): The list of digital states
            to be generated

        Returns:
            StaticDigitalStateGenerationData: An array of strings
            describing the lines that were written to
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self.task.stop()

        # create values for memory declaration
        num_channels = len(self.task.do_channels.channel_names)
        num_samples_per_channel = 1

        # declare memory for write
        numpy_array_of_booleans = np.zeros(
            shape=(num_channels, num_samples_per_channel), dtype=bool
        )

        # populate boolean array with values
        for index, state in enumerate(output_states):
            numpy_array_of_booleans[index] = np.array([state])

        # write to the digital lines
        writer = nidaqmx.stream_writers.DigitalMultiChannelWriter(self.task.out_stream)
        writer.write_one_sample_multi_line(data=numpy_array_of_booleans)

        # get the channel names that have been used
        channel_names = self.task.channel_names

        # create the returned object
        return StaticDigitalStateGenerationData(channel_names)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/static_digital_state_measurements/__init__.py sha256=1c0d25b8b37942e0a38bada11ce73fd989eb1457412c7cb4737b03f29bcbe227 bytes=255 -->
## FILE: src/nipcbatt/pcbatt_library/daq/static_digital_state_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/static_digital_state_measurements/__init__.py`
- sha256: `1c0d25b8b37942e0a38bada11ce73fd989eb1457412c7cb4737b03f29bcbe227`
- bytes: 255

````python
"""Provides nipcbatt library static digital state measurement modules"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (183 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/static_digital_state_measurements/static_digital_state_data_types.py sha256=1d4822748f8214ddbe5f94a826b0dbc1373c3b25f203cb5a99a9117e716b4ff0 bytes=3733 -->
## FILE: src/nipcbatt/pcbatt_library/daq/static_digital_state_measurements/static_digital_state_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/static_digital_state_measurements/static_digital_state_data_types.py`
- sha256: `1d4822748f8214ddbe5f94a826b0dbc1373c3b25f203cb5a99a9117e716b4ff0`
- bytes: 3733

````python
"""Static digital state  data types"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (149 > 100 characters) (auto-generated noqa)

from typing import Dict, List

from varname import nameof

from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class StaticDigitalStateMeasurementResultData(PCBATestToolkitData):
    """Defines parameters used for configuration of static digital state measurements"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

    def __init__(self, digital_states: List[bool], channel_identifiers: List[str]) -> None:
        """Initializes an instance of `StaticDigitalStateMeasurementResultData'
        with specific values

        Args:
            digital_states (array of boolean):
                The boolean state of each corresponding channel in the measurement
            channel_identifiers (array of string):
                The channel ID of each channel in the measurement
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # input verification
        Guard.is_not_none(digital_states, nameof(digital_states))
        Guard.is_not_none(channel_identifiers, nameof(channel_identifiers))
        Guard.have_same_size(
            digital_states,
            nameof(digital_states),
            channel_identifiers,
            nameof(channel_identifiers),
        )

        # generate states_per_channels
        state_map: Dict[str, bool] = {}
        for i, state in enumerate(digital_states):
            state_map[channel_identifiers[i]] = state

        # class properties
        self._digital_states = digital_states
        self._channel_identifiers = channel_identifiers
        self._states_per_channels = state_map

    @property
    def digital_states(self) -> List[bool]:
        """
        :type: array of 'bool': Holds the state of each channel
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._digital_states

    @property
    def channel_identifiers(self) -> List[str]:
        """:type: array of 'str': Identifies each channel"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
        return self._channel_identifiers

    @property
    def states_per_channels(self) -> Dict[str, bool]:
        """:type: dictionary of 'str', 'bool' pairs
            maps each channel to its current state

        Returns:
            Dict[str, bool]: mapping of channel to digital state
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        return self._states_per_channels
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/static_digital_state_measurements/static_digital_state_measurement.py sha256=c2453d09f0281c285ed2b6fbb6bcd970ae88e44d65a46b3000af7cdb295d66d1 bytes=6243 -->
## FILE: src/nipcbatt/pcbatt_library/daq/static_digital_state_measurements/static_digital_state_measurement.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/static_digital_state_measurements/static_digital_state_measurement.py`
- sha256: `c2453d09f0281c285ed2b6fbb6bcd970ae88e44d65a46b3000af7cdb295d66d1`
- bytes: 6243

````python
# pylint: disable=W0613
# pylint: disable=W0612
# remove it when arguments of initialize are used.
""" _summary_ """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (128 > 100 characters) (auto-generated noqa)

from typing import List

# when class are defined in module change to
# from static_digital_state_data_types import ...
import nidaqmx.constants
import nidaqmx.errors
import nidaqmx.stream_readers
import nidaqmx.system
import numpy as np
from nidaqmx.constants import LineGrouping
from nidaqmx.utils import (  # noqa: F401 - 'nidaqmx.utils.unflatten_channel_string' imported but unused (auto-generated noqa)
    unflatten_channel_string,
)
from varname import nameof

from nipcbatt.pcbatt_library.daq.static_digital_state_measurements.static_digital_state_data_types import (
    StaticDigitalStateMeasurementResultData,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryException,
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class StaticDigitalStateMeasurement(BuildingBlockUsingDAQmx):
    """Defines the means for creating, configuring, and measuring
    the static digital state of a series of digital lines

    Args:
        BuildingBlockUsingDAQmx (_type_): _description_
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def initialize(self, channel_expression: str):
        """Initializes Digital input channels for static digital measurements for
        a DAQmx Task

        Args:
            channel_expression (str): Digital input channels to read off of the
            DAQmx task
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        if self.is_task_initialized:
            return

        # input validation on channel expression
        Guard.is_not_none(channel_expression, nameof(channel_expression))
        Guard.is_not_empty(channel_expression, nameof(channel_expression))

        # check to see if task has only global virtual channels
        if self.contains_only_global_virtual_channels(channel_expression):
            # add global channels to task
            self.add_global_channels(channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)

            # check for the presence of global channel ports
            for d_channel in self.task.di_channels:
                # presence of global channel port with # of lines > 1
                if d_channel.di_num_lines > 1:
                    raise PCBATTLibraryException(
                        PCBATTLibraryExceptionMessages.GLOBAL_CHANNEL_PORT_NOT_SUPPORTED_ARGS_3.format(
                            d_channel.name, d_channel.di_num_lines, d_channel.name
                        )
                    )

        else:
            # create virtual channel for each Digital In line
            # for channel in channels:
            self.task.di_channels.add_di_chan(channel_expression, "", LineGrouping.CHAN_PER_LINE)

    def close(self):
        """Closes the measurement process and releases the internal resources"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (191 > 100 characters) (auto-generated noqa)
        if not self.is_task_initialized:
            return

        # Stop and close DAQmx task
        self.task.stop()
        self.task.close()

    def configure_and_measure(self) -> StaticDigitalStateMeasurementResultData:
        """Configures and executes a measurement according to the current configuration parameters.

        Args:

        Returns:
            An instance of `StaticDigitalStateMeasurementResultData
            ` or `None` if no measure was performed.
        """
        return self.acquire_data_for_measurement_analysis()

    def acquire_data_for_measurement_analysis(
        self,
    ) -> StaticDigitalStateMeasurementResultData:
        """Processes digital data acquistion for measurement analysis

        Args:

        Returns:
            An instance of StaticDigitalStateMeasurementResultData"""  # noqa: D202, D209, D414, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), Section has no content (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (403 > 100 characters) (auto-generated noqa)

        # set values for memory declaration
        num_channels = len(self.task.in_stream.channels_to_read.channel_names)
        num_samples_per_channel = 1

        # declare memory for read
        booleans_nparray = np.zeros(
            shape=(num_channels, num_samples_per_channel),
            dtype=bool,
        )
        channel_ids: List[str] = []

        # populate channel IDs
        for d_channel in self.task.di_channels:
            channel_ids.append(d_channel.name)

        # read the digital lines
        reader = nidaqmx.stream_readers.DigitalMultiChannelReader(self.task.in_stream)
        reader.read_one_sample_multi_line(data=booleans_nparray)

        # extract list of booleans from read data
        digital_states: List[bool] = []
        for boolean_sample in booleans_nparray:
            digital_states.append(boolean_sample[0])

        # create the returned object
        return StaticDigitalStateMeasurementResultData(digital_states, channel_ids)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/synchronizations/__init__.py sha256=ae0f6038a81e0ff88d104a4380cff8b6c80cc613a45c7b70a925754a1815e20f bytes=253 -->
## FILE: src/nipcbatt/pcbatt_library/daq/synchronizations/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/synchronizations/__init__.py`
- sha256: `ae0f6038a81e0ff88d104a4380cff8b6c80cc613a45c7b70a925754a1815e20f`
- bytes: 253

````python
"""Provides nipcbatt library synchronization signal routing modules"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (181 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/synchronizations/synchronization_signal_routing.py sha256=598a324cc34045086475c781dc2bbecb27184ae21576b23f6b6942a1a81dd232 bytes=2144 -->
## FILE: src/nipcbatt/pcbatt_library/daq/synchronizations/synchronization_signal_routing.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/synchronizations/synchronization_signal_routing.py`
- sha256: `598a324cc34045086475c781dc2bbecb27184ae21576b23f6b6942a1a81dd232`
- bytes: 2144

````python
""" Defines class used for routing of synchronization signal."""

import nidaqmx.constants
from varname import nameof

from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class SynchronizationSignalRouting(BuildingBlockUsingDAQmx):
    """Defines a way that allows you to route synchronization signal
    (sample clock or start trigger) to specific terminal."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (353 > 100 characters) (auto-generated noqa)

    def route_sample_clock_signal_to_terminal(self, terminal_name: str):
        """Routes sample clock signal to the specified terminal.

        Args:
            terminal_name (str):
            The name of the terminal where the signal is routed.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        Guard.is_not_none_nor_empty_nor_whitespace(terminal_name, nameof(terminal_name))

        self.task.export_signals.export_signal(
            signal_id=nidaqmx.constants.Signal.SAMPLE_CLOCK,
            output_terminal=terminal_name,
        )

    def route_start_trigger_signal_to_terminal(self, terminal_name: str):
        """Routes start trigger signal to the specified terminal.

        Args:
            terminal_name (str):
            The name of the terminal where the signal is routed.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        Guard.is_not_none_nor_empty_nor_whitespace(terminal_name, nameof(terminal_name))

        self.task.export_signals.export_signal(
            signal_id=nidaqmx.constants.Signal.START_TRIGGER,
            output_terminal=terminal_name,
        )

    def close(self):
        """Closes signal routing procedure."""
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/temperature_measurements/__init__.py sha256=2b323032f2bc9a41637e7c333c06c8ea46a341df3a74dd82d32f931024373274 bytes=246 -->
## FILE: src/nipcbatt/pcbatt_library/daq/temperature_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/temperature_measurements/__init__.py`
- sha256: `2b323032f2bc9a41637e7c333c06c8ea46a341df3a74dd82d32f931024373274`
- bytes: 246

````python
"""Provides nipcbatt library temperature measurement modules"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (174 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_constants.py sha256=d813aaa39838b7e3d1f04ff488f7f12a22c07359e2a73e7329d0b86ccc19679f bytes=12175 -->
## FILE: src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_constants.py`
- sha256: `d813aaa39838b7e3d1f04ff488f7f12a22c07359e2a73e7329d0b86ccc19679f`
- bytes: 12175

````python
# pylint: disable=C0301
""" Constants data types for Temperature measurements."""
import dataclasses

import nidaqmx.constants

from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
    MeasurementExecutionType,
    SampleClockTimingParameters,
    SampleTimingEngine,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.daq.temperature_measurements.temperature_data_types import (
    BetaCoefficientAndSensorResistanceParameters,
    CoefficientsSteinhartHartParameters,
    SteinhartHartEquationOption,
    TemperatureRtdMeasurementConfiguration,
    TemperatureRtdMeasurementTerminalParameters,
    TemperatureThermistorMeasurementConfiguration,
    TemperatureThermistorRangeAndTerminalParameters,
    TemperatureThermocoupleMeasurementConfiguration,
    TemperatureThermocoupleMeasurementTerminalParameters,
)


@dataclasses.dataclass
class ConstantsForTemperatureMeasurement:
    """Constants used for Temperature measurements"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (164 > 100 characters) (auto-generated noqa)

    INITIAL_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES = 0.0
    INITIAL_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES = 100.0
    INITIAL_AI_TEMPERATURE_UNITS = nidaqmx.constants.TemperatureUnits.DEG_C

    DEFAULT_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES = 0.0
    DEFAULT_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES = 100.0

    DEFAULT_SAMPLE_CLOCK_SOURCE = "OnboardClock"
    DEFAULT_SAMPLING_RATE_HERTZ = 100
    DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL = 10
    DEFAULT_SAMPLE_TIMING_ENGINE = SampleTimingEngine.AUTO

    DEFAULT_TRIGGER_TYPE = StartTriggerType.NO_TRIGGER
    DEFAULT_DIGITAL_START_TRIGGER_SOURCE = ""
    DEFAULT_DIGITAL_START_TRIGGER_EDGE = nidaqmx.constants.Edge.RISING

    ABSOLUTE_ZERO_CELSIUS_DEGREES = -273.15


@dataclasses.dataclass
class ConstantsForTemperatureMeasurementUsingRtd:
    """Constants used for Temperature measurement using RTD"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

    INITIAL_CURRENT_EXCITATION_VALUE_AMPERES = 0.0025
    INITIAL_SENSOR_RESISTANCE_OHMS = 100.0
    INITIAL_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES = 0.0
    INITIAL_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES = 100.0
    INITIAL_RTD_RESISTANCE_CONFIGURATION = nidaqmx.constants.ResistanceConfiguration.THREE_WIRE
    INITIAL_AI_TEMPERATURE_UNITS = nidaqmx.constants.TemperatureUnits.DEG_C
    INITIAL_RTD_EXCITATION_SOURCE = nidaqmx.constants.ExcitationSource.INTERNAL
    INITIAL_RTD_TYPE = nidaqmx.constants.RTDType.PT_3750

    DEFAULT_RTD_TYPE = nidaqmx.constants.RTDType.PT_3750
    DEFAULT_SENSOR_RESISTANCE_OHMS = 100.0
    DEFAULT_RESISTANCE_CONFIGURATION = nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE
    DEFAULT_EXCITATION_SOURCE = nidaqmx.constants.ExcitationSource.INTERNAL
    DEFAULT_CURRENT_EXCITATION_VALUE_AMPERES = 0.001
    DEFAULT_ADC_TIMING_MODE = nidaqmx.constants.ADCTimingMode.AUTOMATIC


@dataclasses.dataclass
class ConstantsForTemperatureMeasurementUsingThermistor:
    """Constants used for Temperature measurement using Thermistor"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (180 > 100 characters) (auto-generated noqa)

    INITIAL_VOLTAGE_EXCITATION_VALUE_VOLTS = 2.5
    INITIAL_THERMISTOR_RESISTANCE_CONFIGURATION = (
        nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE
    )
    INITIAL_THERMISTOR_EXCITATION_SOURCE = nidaqmx.constants.ExcitationSource.EXTERNAL

    INITIAL_COEFFICIENT_STAINHART_HART_A = 0.001295361
    INITIAL_COEFFICIENT_STAINHART_HART_B = 0.0002343159
    INITIAL_COEFFICIENT_STAINHART_HART_C = 1.018703e-7
    INITIAL_THERMISTOR_RESISTOR_OHMS = 5000.0

    DEFAULT_VOLTAGE_EXCITATION_VALUE_VOLTS = 5.0
    DEFAULT_THERMISTOR_RESISTOR_OHMS = 1000.0
    DEFAULT_AI_TERMINAL_CONFIGURATION = nidaqmx.constants.TerminalConfiguration.RSE
    DEFAULT_STEINHART_HART_EQUATION_OPTION = (
        SteinhartHartEquationOption.USE_STEINHART_HART_COEFFICIENTS
    )

    DEFAULT_COEFFICIENT_STAINHART_HART_A = 0.0
    DEFAULT_COEFFICIENT_STAINHART_HART_B = 0.0
    DEFAULT_COEFFICIENT_STAINHART_HART_C = 0.0

    DEFAULT_COEFFICIENT_STAINHART_HART_BETA_KELVINS = 0
    DEFAULT_THERMISTOR_SENSOR_RESISTANCE_OHMS = 0.0

    THERMISTOR_REFERENCE_TEMPERATURE_KELVINS = 298.15


@dataclasses.dataclass
class ConstantsForTemperatureMeasurementUsingThermocouple:
    """Constants used for Temperature measurement using Thermocouple"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (182 > 100 characters) (auto-generated noqa)

    DEFAULT_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES = 0.0
    DEFAULT_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES = 100.0

    DEFAULT_THERMOCOUPLE_TYPE = nidaqmx.constants.ThermocoupleType.J
    DEFAULT_COLD_JUNCTION_COMPENSATION_TEMPERATURE = 25.00
    DEFAULT_COLD_JUNCTION_COMPENSATION_SOURCE = nidaqmx.constants.CJCSource.BUILT_IN
    INITIAL_COLD_JUNCTION_COMPENSATION_CHANNEL_NAME = ""

    DEFAULT_ENABLE_AUTOZERO = False
    DEFAULT_AUTOZERO_MODE = nidaqmx.constants.AutoZeroType.NONE


DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS = TemperatureRtdMeasurementTerminalParameters(
    temperature_minimum_value_celsius_degrees=(
        ConstantsForTemperatureMeasurement.DEFAULT_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES
    ),
    temperature_maximum_value_celsius_degrees=(
        ConstantsForTemperatureMeasurement.DEFAULT_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES
    ),
    current_excitation_value_amperes=(
        ConstantsForTemperatureMeasurementUsingRtd.DEFAULT_CURRENT_EXCITATION_VALUE_AMPERES
    ),
    sensor_resistance_ohms=ConstantsForTemperatureMeasurementUsingRtd.DEFAULT_SENSOR_RESISTANCE_OHMS,
    rtd_type=ConstantsForTemperatureMeasurementUsingRtd.DEFAULT_RTD_TYPE,
    excitation_source=ConstantsForTemperatureMeasurementUsingRtd.DEFAULT_EXCITATION_SOURCE,
    resistance_configuration=ConstantsForTemperatureMeasurementUsingRtd.DEFAULT_RESISTANCE_CONFIGURATION,
    adc_timing_mode=ConstantsForTemperatureMeasurementUsingRtd.DEFAULT_ADC_TIMING_MODE,
)

DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS = SampleClockTimingParameters(
    sample_clock_source=ConstantsForTemperatureMeasurement.DEFAULT_SAMPLE_CLOCK_SOURCE,
    sampling_rate_hertz=ConstantsForTemperatureMeasurement.DEFAULT_SAMPLING_RATE_HERTZ,
    number_of_samples_per_channel=(
        ConstantsForTemperatureMeasurement.DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL
    ),
    sample_timing_engine=ConstantsForTemperatureMeasurement.DEFAULT_SAMPLE_TIMING_ENGINE,
)

DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS = DigitalStartTriggerParameters(
    trigger_select=ConstantsForTemperatureMeasurement.DEFAULT_TRIGGER_TYPE,
    digital_start_trigger_source=(
        ConstantsForTemperatureMeasurement.DEFAULT_DIGITAL_START_TRIGGER_SOURCE
    ),
    digital_start_trigger_edge=(
        ConstantsForTemperatureMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE
    ),
)

DEFAULT_TEMPERATURE_RTD_MEASUREMENT_CONFIGURATION = TemperatureRtdMeasurementConfiguration(
    global_channel_parameters=DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS,
    specific_channels_parameters=[],
    measurement_execution_type=MeasurementExecutionType.CONFIGURE_AND_MEASURE,
    sample_clock_timing_parameters=DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS,
    digital_start_trigger_parameters=DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS,
)

DEFAULT_COEFFICIENTS_STEINHART_HART_PARAMETERS = CoefficientsSteinhartHartParameters(
    coefficient_steinhart_hart_a=(
        ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_COEFFICIENT_STAINHART_HART_A
    ),
    coefficient_steinhart_hart_b=(
        ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_COEFFICIENT_STAINHART_HART_B
    ),
    coefficient_steinhart_hart_c=(
        ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_COEFFICIENT_STAINHART_HART_C
    ),
)

DEFAULT_BETA_OEFFICIENT_AND_SENSOR_RESISTANCE_PARAMETERS = BetaCoefficientAndSensorResistanceParameters(
    coefficient_steinhart_hart_beta_kelvins=(
        ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_COEFFICIENT_STAINHART_HART_BETA_KELVINS
    ),
    sensor_resistance_ohms=(
        ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_THERMISTOR_SENSOR_RESISTANCE_OHMS
    ),
)

DEFAULT_TEMPERATURE_THERMISTOR_RANGE_AND_TERMINAL_PARAMETERS = (
    TemperatureThermistorRangeAndTerminalParameters(
        terminal_configuration=(
            ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_AI_TERMINAL_CONFIGURATION
        ),
        temperature_minimum_value_celsius_degrees=(
            ConstantsForTemperatureMeasurement.DEFAULT_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES
        ),
        temperature_maximum_value_celsius_degrees=(
            ConstantsForTemperatureMeasurement.DEFAULT_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES
        ),
        voltage_excitation_value_volts=(
            ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_VOLTAGE_EXCITATION_VALUE_VOLTS
        ),
        thermistor_resistor_ohms=(
            ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_THERMISTOR_RESISTOR_OHMS
        ),
        steinhart_hart_equation_option=(
            ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_STEINHART_HART_EQUATION_OPTION
        ),
        coefficients_steinhart_hart_parameters=(DEFAULT_COEFFICIENTS_STEINHART_HART_PARAMETERS),
        beta_coefficient_and_sensor_resistance_parameters=(
            DEFAULT_BETA_OEFFICIENT_AND_SENSOR_RESISTANCE_PARAMETERS
        ),
    )
)

DEFAULT_TEMPERATURE_THERMISTOR_MEASUREMENT_CONFIGURATION = (
    TemperatureThermistorMeasurementConfiguration(
        global_channel_parameters=(DEFAULT_TEMPERATURE_THERMISTOR_RANGE_AND_TERMINAL_PARAMETERS),
        specific_channels_parameters=[],
        measurement_execution_type=MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        sample_clock_timing_parameters=(DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS),
        digital_start_trigger_parameters=(DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS),
    )
)

DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS = TemperatureThermocoupleMeasurementTerminalParameters(
    temperature_minimum_value_celsius_degrees=(
        ConstantsForTemperatureMeasurementUsingThermocouple.DEFAULT_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES
    ),
    temperature_maximum_value_celsius_degrees=(
        ConstantsForTemperatureMeasurementUsingThermocouple.DEFAULT_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES
    ),
    thermocouple_type=(
        ConstantsForTemperatureMeasurementUsingThermocouple.DEFAULT_THERMOCOUPLE_TYPE
    ),
    cold_junction_compensation_temperature=(
        ConstantsForTemperatureMeasurementUsingThermocouple.DEFAULT_COLD_JUNCTION_COMPENSATION_TEMPERATURE
    ),
    perform_auto_zero_mode=(
        ConstantsForTemperatureMeasurementUsingThermocouple.DEFAULT_ENABLE_AUTOZERO
    ),
    auto_zero_mode=(ConstantsForTemperatureMeasurementUsingThermocouple.DEFAULT_AUTOZERO_MODE),
)


DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_CONFIGURATION = (
    TemperatureThermocoupleMeasurementConfiguration(
        global_channel_parameters=DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS,
        specific_channels_parameters=[],
        measurement_execution_type=MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        sample_clock_timing_parameters=DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS,
        digital_start_trigger_parameters=DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS,
    )
)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_data_types.py sha256=bf50f74523bc0e25ed9f5393b439fd442202bd23f41263ebc5e956c3453c71ef bytes=88274 -->
## FILE: src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_data_types.py`
- sha256: `bf50f74523bc0e25ed9f5393b439fd442202bd23f41263ebc5e956c3453c71ef`
- bytes: 88274

````python
# pylint: disable=C0301
""" Temperature data types"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (140 > 100 characters) (auto-generated noqa)

from enum import Enum
from typing import List

import nidaqmx.constants
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    AnalogWaveform,
    DigitalStartTriggerParameters,
    MeasurementExecutionType,
    SampleClockTimingParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class TemperatureRtdMeasurementTerminalParameters(PCBATestToolkitData):
    """Defines the parameters used to configure terminal
    of all channels for temperature measurement using RTD."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (354 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        temperature_minimum_value_celsius_degrees: float,
        temperature_maximum_value_celsius_degrees: float,
        current_excitation_value_amperes: float,
        sensor_resistance_ohms: float,
        rtd_type: nidaqmx.constants.RTDType,
        excitation_source: nidaqmx.constants.ExcitationSource,
        resistance_configuration: nidaqmx.constants.ResistanceConfiguration,
        adc_timing_mode: nidaqmx.constants.ADCTimingMode,
    ) -> None:
        """Initializes an instance of `TemperatureRtdMeasurementTerminalParameters`
           with specific values.

        Args:
            temperature_minimum_value_celsius_degrees (float):
                The minimum value expected from the measurement, expressed in °C.
            temperature_maximum_value_celsius_degrees (float):
                The maximum value expected from the measurement, expressed in °C.
            current_excitation_value_amperes (float): The amount of excitation
                to supply to the sensor, in Amperes.
                Refer to the sensor documentation to determine this value.
            sensor_resistance_ohms (float): The sensor resistance, in Ohms,
                at 0 degree Celsius (also called R0).
            rtd_type (nidaqmx.constants.RTDType):
                The type of `RTD <https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/measfunds/rtdtypes.html>`
                connected to the channel.
            excitation_source (nidaqmx.constants.ExcitationSource): The source of excitation.
            resistance_configuration (nidaqmx.constants.ResistanceConfiguration): The mode
                that represents the number of `wires <https://en.wikipedia.org/wiki/Resistance_thermometer#Wiring_configurations>`
                to use for resistive measurements.
            adc_timing_mode (nidaqmx.constants.ADCTimingMode): The
                `ADC Timing Mode <https://www.ni.com/docs/en-US/bundle/ni-daqmx-properties/page/daqmxprop/attr29f9.html>`.

        Raises:
            ValueError:
                Raised when `temperature_minimum_value_celsius_degrees'
                is greater than or equal to `temperature_maximum_value_celsius_degrees`.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (110 > 100 characters) (auto-generated noqa)
        Guard.is_less_than(
            temperature_minimum_value_celsius_degrees,
            temperature_maximum_value_celsius_degrees,
            nameof(temperature_minimum_value_celsius_degrees),
        )

        self._temperature_minimum_value_celsius_degrees = temperature_minimum_value_celsius_degrees
        self._temperature_maximum_value_celsius_degrees = temperature_maximum_value_celsius_degrees
        self._current_excitation_value_amperes = current_excitation_value_amperes
        self._sensor_resistance_ohms = sensor_resistance_ohms
        self._rtd_type = rtd_type
        self._excitation_source = excitation_source
        self._resistance_configuration = resistance_configuration
        self._adc_timing_mode = adc_timing_mode

    @property
    def temperature_minimum_value_celsius_degrees(self) -> float:
        """
        :type:`float`: Gets the minimum value expected from the measurement, expressed in °C.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        return self._temperature_minimum_value_celsius_degrees

    @property
    def temperature_maximum_value_celsius_degrees(self) -> float:
        """
        :type:`float`: Gets the minimum value expected from the measurement, expressed in °C.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        return self._temperature_maximum_value_celsius_degrees

    @property
    def current_excitation_value_amperes(self) -> float:
        """
        :type:`float`: Gets the amount of excitation to supply to the sensor, in Amperes.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        return self._current_excitation_value_amperes

    @property
    def sensor_resistance_ohms(self) -> float:
        """
        :type:`float`: Gets the sensor resistance, in Ohms,
                at 0 degree Celsius (also called R0).
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._sensor_resistance_ohms

    @property
    def rtd_type(self) -> nidaqmx.constants.RTDType:
        """
        :type:`float`: Gets the type of
            `RTD <https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/measfunds/rtdtypes.html>`
            connected to the channel.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._rtd_type

    @property
    def excitation_source(self) -> nidaqmx.constants.ExcitationSource:
        """
        :type:`float`: Gets the source of excitation.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        return self._excitation_source

    @property
    def resistance_configuration(self) -> nidaqmx.constants.ResistanceConfiguration:
        """
        :type:`float`: Gets the mode
            that represents the number of
            `wires <https://en.wikipedia.org/wiki/Resistance_thermometer#Wiring_configurations>`
            to use for resistive measurements.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._resistance_configuration

    @property
    def adc_timing_mode(self) -> nidaqmx.constants.ADCTimingMode:
        """
        :type:`float`: Gets the `ADC Timing Mode
            <https://www.ni.com/docs/en-US/bundle/ni-daqmx-properties/page/daqmxprop/attr29f9.html>`.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._adc_timing_mode


class TemperatureRtdMeasurementChannelParameters(PCBATestToolkitData):
    """Defines the parameters used to configure channels for temperature measurement using RTD."""

    def __init__(
        self,
        channel_name: str,
        sensor_resistance_ohms: float,
        current_excitation_value_amperes: float,
        rtd_type: nidaqmx.constants.RTDType,
        resistance_configuration: nidaqmx.constants.ResistanceConfiguration,
        excitation_source: nidaqmx.constants.ExcitationSource,
    ) -> None:
        """_summary_

        Args:
            channel_name (str):
                The name of the channel to configure.
            sensor_resistance_ohms (float): The sensor resistance, in Ohms,
                at 0 degree Celsius (also called R0).
            current_excitation_value_amperes (float): The amount of excitation
                to supply to the sensor, in Amperes.
                Refer to the sensor documentation to determine this value.
            rtd_type (nidaqmx.constants.RTDType):
                The type of `RTD <https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/measfunds/rtdtypes.html>`
                connected to the channel.
            resistance_configuration (nidaqmx.constants.ResistanceConfiguration): The mode
                that represents the number of
                `wires <https://en.wikipedia.org/wiki/Resistance_thermometer#Wiring_configurations>`
                to use for resistive measurements.
            excitation_source (nidaqmx.constants.ExcitationSource): The source of excitation.

        Raises:
            ValueError:
                Raised when `channel_name` is None or empty or whitespace.
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (110 > 100 characters) (auto-generated noqa)
        Guard.is_not_none_nor_empty_nor_whitespace(channel_name, nameof(channel_name))

        self._channel_name = channel_name
        self._sensor_resistance_ohms = sensor_resistance_ohms
        self._current_excitation_value_amperes = current_excitation_value_amperes
        self._rtd_type = rtd_type
        self._resistance_configuration = resistance_configuration
        self._excitation_source = excitation_source

    @property
    def channel_name(self) -> str:
        """
        :type:`str`: Gets the name of the channel to configure.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        return self._channel_name

    @property
    def sensor_resistance_ohms(self) -> float:
        """
        :type:`float`: Gets the sensor resistance, in Ohms,
                at 0 degree Celsius (also called R0).
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._sensor_resistance_ohms

    @property
    def current_excitation_value_amperes(self) -> float:
        """
        :type:`float`: Gets the amount of excitation to supply to the sensor, in Amperes.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        return self._current_excitation_value_amperes

    @property
    def rtd_type(self) -> nidaqmx.constants.RTDType:
        """
        :type:`float`: Gets the type of
            `RTD <https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/measfunds/rtdtypes.html>`
            connected to the channel.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._rtd_type

    @property
    def resistance_configuration(self) -> nidaqmx.constants.ResistanceConfiguration:
        """
        :type:`float`: Gets the mode
            that represents the number of
            `wires <https://en.wikipedia.org/wiki/Resistance_thermometer#Wiring_configurations>`
            to use for resistive measurements.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._resistance_configuration

    @property
    def excitation_source(self) -> nidaqmx.constants.ExcitationSource:
        """
        :type:`float`: Gets the source of excitation.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        return self._excitation_source


class TemperatureRtdMeasurementConfiguration(PCBATestToolkitData):
    """Defines parameters used for configuration of Temperature measurement using RTD."""

    def __init__(
        self,
        global_channel_parameters: TemperatureRtdMeasurementTerminalParameters,
        specific_channels_parameters: List[TemperatureRtdMeasurementChannelParameters],
        measurement_execution_type: MeasurementExecutionType,
        sample_clock_timing_parameters: SampleClockTimingParameters,
        digital_start_trigger_parameters: DigitalStartTriggerParameters,
    ) -> None:
        """Initializes an instance of
        `TemperatureRtdMeasurementConfiguration` with specific values.

        Args:
            global_channel_parameters (TemperatureRtdMeasurementTerminalParameters):
                The settings of terminal for all channels.
            specific_channels_parameters (List[TemperatureRtdMeasurementChannelParameters]):
                The list of instances of `TemperatureRtdMeasurementChannelParameters`
                used to configure channels.
            measurement_execution_type (MeasurementExecutionType):
                The type of measurement execution selected by user.
            sample_clock_timing_parameters (SampleClockTimingParameters):
                An instance of `SampleClockTimingParameters` that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters`
                that represents the settings of triggers.

        Raises:
            TypeError:
                Raised when `specific_channels_parameters`
                contains objects that are not type of TemperatureRtdMeasurementChannelParameters.
            ValueError:
                Raised when `global_channel_parameters` is None,
                `specific_channels_parameters` is None,
                `sample_clock_timing_parameters` is None,
                `digital_start_trigger_parameters` is None,
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(global_channel_parameters, nameof(global_channel_parameters))
        Guard.is_not_none(specific_channels_parameters, nameof(specific_channels_parameters))
        Guard.all_elements_are_of_same_type(
            input_list=specific_channels_parameters,
            expected_type=TemperatureRtdMeasurementChannelParameters,
        )
        Guard.is_not_none(sample_clock_timing_parameters, nameof(sample_clock_timing_parameters))
        Guard.is_not_none(
            digital_start_trigger_parameters, nameof(digital_start_trigger_parameters)
        )

        self._global_channel_parameters = global_channel_parameters
        self._specific_channels_parameters = specific_channels_parameters
        self._measurement_execution_type = measurement_execution_type
        self._sample_clock_timing_parameters = sample_clock_timing_parameters
        self._digital_start_trigger_parameters = digital_start_trigger_parameters

    @property
    def global_channel_parameters(
        self,
    ) -> TemperatureRtdMeasurementTerminalParameters:
        """
        :class:`TemperatureRtdMeasurementChannelParameters`:
            Gets the settings of terminal for all channels."""  # noqa: D205, D209, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (444 > 100 characters) (auto-generated noqa)
        return self._global_channel_parameters

    @property
    def specific_channels_parameters(
        self,
    ) -> List[TemperatureRtdMeasurementChannelParameters]:
        """
        :class:`List[VoltageMeasurementChannelAndTerminalRangeParameters]`:
            Gets the list of instances of
            `TemperatureRtdMeasurementChannelParameters` used to configure channels.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._specific_channels_parameters

    @property
    def measurement_execution_type(self) -> MeasurementExecutionType:
        """
        :class:`MeasurementExecutionType`:
            Gets the type of measurement execution selected by user.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._measurement_execution_type

    @property
    def sample_clock_timing_parameters(self) -> SampleClockTimingParameters:
        """
        :class:`SampleClockTimingParameters`:
            Gets a `SampleClockTimingParameters` instance
            that represents the settings of timing.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._sample_clock_timing_parameters

    @property
    def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters:
        """
        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._digital_start_trigger_parameters


class SteinhartHartEquationOption(Enum):
    """Defines the option of to use coefficients
    in Steinhart-Hart equation used during channels configuration."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (362 > 100 characters) (auto-generated noqa)

    USE_STEINHART_HART_COEFFICIENTS = 0
    """Use coefficients A, B and C of the
       `Steinhart-Hart <https://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation>` equation."""

    USE_COEFFICIENT_BETA_AND_SENSOR_RESISTANCE = 1
    """Use the `β coefficient <https://en.wikipedia.org/wiki/Thermistor#B_or_.CE.B2_parameter_equation>` and the sensor resistance."""  # noqa: W505 - doc line too long (134 > 100 characters) (auto-generated noqa)


class CoefficientsSteinhartHartParameters(PCBATestToolkitData):
    """Defines the parameters used to configure coefficients of
    the <Steinhart-Hart https://en.wikipedia.org/wiki/Thermistor#Steinhart.E2.80.93Hart_equation>
    for Temperature measurements."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (329 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        coefficient_steinhart_hart_a: float,
        coefficient_steinhart_hart_b: float,
        coefficient_steinhart_hart_c: float,
    ) -> None:
        """Initializes an instance of
        `CoefficientsSteinhartHartParameters` with specific values.

        Args:
            coefficient_steinhart_hart_a (float): The A coefficient in the
            `Steinhart-Hart <https://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation>` equation.
            coefficient_steinhart_hart_b (float): The B coefficient in the
            `Steinhart-Hart <https://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation>` equation.
            coefficient_steinhart_hart_c (float): The C coefficient in the
            `Steinhart-Hart <https://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation>` equation.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (102 > 100 characters) (auto-generated noqa)
        self._coefficient_steinhart_hart_a = coefficient_steinhart_hart_a
        self._coefficient_steinhart_hart_b = coefficient_steinhart_hart_b
        self._coefficient_steinhart_hart_c = coefficient_steinhart_hart_c

    @property
    def coefficient_steinhart_hart_a(self) -> float:
        """
        :type:`float`:
            Gets the A coefficient in the
            `Steinhart-Hart <https://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation>` equation.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (102 > 100 characters) (auto-generated noqa)
        return self._coefficient_steinhart_hart_a

    @property
    def coefficient_steinhart_hart_b(self) -> float:
        """
        :type:`float`:
            Gets the B coefficient in the
            `Steinhart-Hart <https://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation>` equation.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (102 > 100 characters) (auto-generated noqa)
        return self._coefficient_steinhart_hart_b

    @property
    def coefficient_steinhart_hart_c(self) -> float:
        """
        :type:`float`:
            Gets the C coefficient in the
            `Steinhart-Hart <https://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation>` equation.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (102 > 100 characters) (auto-generated noqa)
        return self._coefficient_steinhart_hart_c


class BetaCoefficientAndSensorResistanceParameters(PCBATestToolkitData):
    """Defines the parameters for coefficients
    (`β coefficient <https://en.wikipedia.org/wiki/Thermistor#B_or_.CE.B2_parameter_equation>` and sensor resistance)
    of Steinhart-Hart equation."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (117 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        coefficient_steinhart_hart_beta_kelvins: float,
        sensor_resistance_ohms: float,
    ) -> None:
        """Initializes an instance of
        `BetaCoefficientAndSensorResistanceParameters` with specific values.

        Args:
            coefficient_steinhart_hart_beta_kelvins (float):
            The `β coefficient <https://en.wikipedia.org/wiki/Thermistor#B_or_.CE.B2_parameter_equation>`
            used with the Steinhart-Hart equation, in Kelvins.
            Coefficients A, B and C of the equation are computed from this coefficient.
            sensor_resistance_ohms (float):
            The sensor resistance, in Ohms, at 25 degrees Celsius (298.15 Kelvins).
            Coefficients A, B and C of the equation are computed from this coefficient.
        """  # noqa: D205, D415, D417, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (105 > 100 characters) (auto-generated noqa)
        self._coefficient_steinhart_hart_beta_kelvins = coefficient_steinhart_hart_beta_kelvins
        self._sensor_resistance_ohms = sensor_resistance_ohms

    @property
    def coefficient_steinhart_hart_beta_kelvins(self) -> float:
        """
        :type:`float`:
            Gets the `β coefficient <https://en.wikipedia.org/wiki/Thermistor#B_or_.CE.B2_parameter_equation>`
            used with the Steinhart-Hart equation, in Kelvins.
            Coefficients A, B and C of the equation are computed from this coefficient.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (110 > 100 characters) (auto-generated noqa)
        return self._coefficient_steinhart_hart_beta_kelvins

    @property
    def sensor_resistance_ohms(self) -> float:
        """
        :type:`float`:
            Gets the sensor resistance, in Ohms, at 25 degrees Celsius (298.15 Kelvins).
            Coefficients A, B and C of the equation are computed from this coefficient.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._sensor_resistance_ohms


class TemperatureThermistorRangeAndTerminalParameters(PCBATestToolkitData):
    """Defines the parameters used to configure terminal
    of all channels for temperature measurement using Thermistor."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (361 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        terminal_configuration: nidaqmx.constants.TerminalConfiguration,
        temperature_minimum_value_celsius_degrees: float,
        temperature_maximum_value_celsius_degrees: float,
        voltage_excitation_value_volts: float,
        thermistor_resistor_ohms: float,
        steinhart_hart_equation_option: SteinhartHartEquationOption,
        coefficients_steinhart_hart_parameters: CoefficientsSteinhartHartParameters,
        beta_coefficient_and_sensor_resistance_parameters: BetaCoefficientAndSensorResistanceParameters,
    ) -> None:
        """Initializes an instance of
        `TemperatureThermistorRangeAndTerminalParameters` with specific values.

        Args:
            terminal_configuration (nidaqmx.constants.TerminalConfiguration):
                The input terminal configuration parameter.
            temperature_minimum_value_celsius_degrees (float):
                The minimum value expected from the measurement, expressed in °C.
            temperature_maximum_value_celsius_degrees (float):
                The maximum value expected from the measurement, expressed in °C.
            voltage_excitation_value_volts (float):
                The amount of voltage excitation to supply to the sensor, expressed in Volts.
                Refer to the sensor documentation to determine this value.
            thermistor_resistor_ohms (float):
                The reference resistor for the
                `thermistor <https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/measfunds/thermistors.html>`
                if you use voltage excitation, in Ohms.
            steinhart_hart_equation_option (SteinhartHartEquationOption):
                The option used to compute coefficients of Steinhart-Hart equation.
            coefficients_steinhart_hart_parameters (CoefficientsSteinhartHartParameters):
                An instance of `CoefficientsSteinhartHartParameters`
                representing the coefficients of the SteinHart-Hart equation.
            beta_coefficient_and_sensor_resistance_parameters (BetaCoefficientAndSensorResistanceParameters):
                An instance of `BetaCoefficientAndSensorResistanceParameters`
                representing the coefficients
                (`β coefficient <https://en.wikipedia.org/wiki/Thermistor#B_or_.CE.B2_parameter_equation>` and sensor resistance)
                of Steinhart-Hart equation.

        Raises:
            ValueError:
                Raised when `temperature_minimum_value_celsius_degrees`
                is greater than or equal to `temperature_maximum_value_celsius_degrees`,
                `coefficients_steinhart_hart_parameters` is None
                and `steinhart_hart_equation_option` is equal to
                `SteinhartHartEquationOption.USE_STEINHART_HART_COEFFICIENTS`,
                `beta_coefficient_and_sensor_resistance_parameters` is None
                and `steinhart_hart_equation_option` is equal to
                `SteinhartHartEquationOption.USE_COEFFICIENT_BETA_AND_SENSOR_RESISTANCE`.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (108 > 100 characters) (auto-generated noqa)
        Guard.is_less_than(
            temperature_minimum_value_celsius_degrees,
            temperature_maximum_value_celsius_degrees,
            nameof(temperature_minimum_value_celsius_degrees),
        )
        if (
            steinhart_hart_equation_option
            == SteinhartHartEquationOption.USE_STEINHART_HART_COEFFICIENTS
        ):
            Guard.is_not_none(
                coefficients_steinhart_hart_parameters,
                nameof(coefficients_steinhart_hart_parameters),
            )
        if (
            steinhart_hart_equation_option
            == SteinhartHartEquationOption.USE_COEFFICIENT_BETA_AND_SENSOR_RESISTANCE
        ):
            Guard.is_not_none(
                beta_coefficient_and_sensor_resistance_parameters,
                nameof(beta_coefficient_and_sensor_resistance_parameters),
            )

        self._terminal_configuration = terminal_configuration
        self._temperature_minimum_value_celsius_degrees = temperature_minimum_value_celsius_degrees
        self._temperature_maximum_value_celsius_degrees = temperature_maximum_value_celsius_degrees
        self._voltage_excitation_value_volts = voltage_excitation_value_volts
        self._thermistor_resistor_ohms = thermistor_resistor_ohms
        self._steinhart_hart_equation_option = steinhart_hart_equation_option
        self._coefficients_steinhart_hart_parameters = coefficients_steinhart_hart_parameters
        self._beta_coefficient_and_sensor_resistance_parameters = (
            beta_coefficient_and_sensor_resistance_parameters
        )

    @property
    def terminal_configuration(self) -> nidaqmx.constants.TerminalConfiguration:
        """
        :class:`nidaqmx.constants.TerminalConfiguration`:
            Gets the input terminal configuration parameter.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._terminal_configuration

    @property
    def temperature_minimum_value_celsius_degrees(self) -> float:
        """
        :type:`float`:
            Gets the minimum value expected from the measurement, expressed in °C.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._temperature_minimum_value_celsius_degrees

    @property
    def temperature_maximum_value_celsius_degrees(self) -> float:
        """
        :type:`float`:
            Gets the maximum value expected from the measurement, expressed in °C.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._temperature_maximum_value_celsius_degrees

    @property
    def voltage_excitation_value_volts(self) -> float:
        """
        :type:`float`:
            Gets the amount of voltage excitation to supply to the sensor, expressed in Volts.
            Refer to the sensor documentation to determine this value.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._voltage_excitation_value_volts

    @property
    def thermistor_resistor_ohms(self) -> float:
        """
        :type:`float`:
            Gets the reference resistor for the
            `thermistor <https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/measfunds/thermistors.html>`
            if you use voltage excitation, in Ohms.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (104 > 100 characters) (auto-generated noqa)
        return self._thermistor_resistor_ohms

    @property
    def steinhart_hart_equation_option(self) -> SteinhartHartEquationOption:
        """
        :class:`SteinhartHartEquationOption`:
            Gets the option used to compute coefficients of Steinhart-Hart equation.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._steinhart_hart_equation_option

    @property
    def coefficients_steinhart_hart_parameters(
        self,
    ) -> CoefficientsSteinhartHartParameters:
        """
        :class:`CoefficientsSteinhartHartParameters`:
            Gets an instance of `CoefficientsSteinhartHartParameters`
            representing the coefficients of the SteinHart-Hart equation.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._coefficients_steinhart_hart_parameters

    @property
    def beta_coefficient_and_sensor_resistance_parameters(self):
        """
        :class:`BetaCoefficientAndSensorResistanceParameters`:
            Gets an instance of `BetaCoefficientAndSensorResistanceParameters`
            representing the coefficients
            (`β coefficient <https://en.wikipedia.org/wiki/Thermistor#B_or_.CE.B2_parameter_equation>` and sensor resistance)
            of Steinhart-Hart equation.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (125 > 100 characters) (auto-generated noqa)
        return self._beta_coefficient_and_sensor_resistance_parameters


class TemperatureThermistorChannelRangeAndTerminalParameters(PCBATestToolkitData):
    """Defines settings for channel and terminal used to configure temperature measurement based on thermistor."""  # noqa: W505 - doc line too long (114 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        channel_name: str,
        channel_parameters: TemperatureThermistorRangeAndTerminalParameters,
    ) -> None:
        """Initializes an instance of
        `TemperatureThermistorChannelRangeAndTerminalParameters` with specific values.

        Args:
            channel_name (str):
                The name of the channel to configure.
            channel_parameters (TemperatureThermistorRangeAndTerminalParameters): The settings of the channel.

        Raises:
            ValueError:
                Raised when `channel_name` is None or empty or whitespace,
                `channel_parameters` is None.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (110 > 100 characters) (auto-generated noqa)
        Guard.is_not_none_nor_empty_nor_whitespace(channel_name, nameof(channel_name))
        Guard.is_not_none(channel_parameters, nameof(channel_parameters))

        self._channel_name = channel_name
        self._channel_parameters = channel_parameters

    @property
    def channel_name(self) -> str:
        """
        :type:`str`:
            Gets the name of the channel to configure.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._channel_name

    @property
    def channel_parameters(self) -> TemperatureThermistorRangeAndTerminalParameters:
        """
        :class:`TemperatureThermistorRangeAndTerminalParameters`:
            Gets the settings of the channel.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._channel_parameters


class TemperatureThermistorMeasurementConfiguration(PCBATestToolkitData):
    """Defines parameters used for configuration of Temperature measurement using Thermistor."""

    def __init__(
        self,
        global_channel_parameters: TemperatureThermistorRangeAndTerminalParameters,
        specific_channels_parameters: List[TemperatureThermistorChannelRangeAndTerminalParameters],
        measurement_execution_type: MeasurementExecutionType,
        sample_clock_timing_parameters: SampleClockTimingParameters,
        digital_start_trigger_parameters: DigitalStartTriggerParameters,
    ) -> None:
        """Initializes an instance of
        `TemperatureRtdMeasurementConfiguration` with specific values.

        Args:
            global_channel_parameters (TemperatureThermistorMeasurementTerminalParameters):
                The settings of terminal for all channels.
            specific_channels_parameters (List[TemperatureThermistorChannelRangeAndTerminalParameters]):
                The list of instances of `TemperatureThermistorChannelRangeAndTerminalParameters`
                used to configure channels.
            measurement_execution_type (MeasurementExecutionType):
                The type of measurement execution selected by user.
            sample_clock_timing_parameters (SampleClockTimingParameters):
                An instance of `SampleClockTimingParameters` that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters`
                that represents the settings of triggers.

        Raises:
            TypeError:
                Raised when `specific_channels_parameters`
                contains objects that are not type of TemperatureThermistorChannelRangeAndTerminalParameters.
            ValueError:
                Raised when `global_channel_parameters` is None,
                `specific_channels_parameters` is None,
                `sample_clock_timing_parameters` is None,
                `digital_start_trigger_parameters` is None,
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (104 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(global_channel_parameters, nameof(global_channel_parameters))
        Guard.is_not_none(specific_channels_parameters, nameof(specific_channels_parameters))
        Guard.all_elements_are_of_same_type(
            input_list=specific_channels_parameters,
            expected_type=TemperatureThermistorChannelRangeAndTerminalParameters,
        )
        Guard.is_not_none(sample_clock_timing_parameters, nameof(sample_clock_timing_parameters))
        Guard.is_not_none(
            digital_start_trigger_parameters, nameof(digital_start_trigger_parameters)
        )

        self._global_channel_parameters = global_channel_parameters
        self._specific_channels_parameters = specific_channels_parameters
        self._measurement_execution_type = measurement_execution_type
        self._sample_clock_timing_parameters = sample_clock_timing_parameters
        self._digital_start_trigger_parameters = digital_start_trigger_parameters

    @property
    def global_channel_parameters(
        self,
    ) -> TemperatureThermistorRangeAndTerminalParameters:
        """
        :class:`TemperatureThermistorRangeAndTerminalParameters`:
            Gets the settings of terminal for all channels.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._global_channel_parameters

    @property
    def specific_channels_parameters(
        self,
    ) -> List[TemperatureThermistorChannelRangeAndTerminalParameters]:
        """
        :class:`List[TemperatureThermistorChannelRangeAndTerminalParameters]`:
            Gets the list of instances of `TemperatureThermistorChannelRangeAndTerminalParameters`
            used to configure channels.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._specific_channels_parameters

    @property
    def measurement_execution_type(self) -> MeasurementExecutionType:
        """
        :class:`MeasurementExecutionType`:
            Gets the type of measurement execution selected by user.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._measurement_execution_type

    @property
    def sample_clock_timing_parameters(self) -> SampleClockTimingParameters:
        """
        :class:`SampleClockTimingParameters`:
            Gets a `SampleClockTimingParameters` instance
            that represents the settings of timing.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._sample_clock_timing_parameters

    @property
    def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters:
        """
        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._digital_start_trigger_parameters


class TemperatureThermocoupleMeasurementTerminalParameters(PCBATestToolkitData):
    """Defines the parameters used to configure terminal
    of all channels for temperature measurement using Thermocouple."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (363 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        temperature_minimum_value_celsius_degrees: float,
        temperature_maximum_value_celsius_degrees: float,
        thermocouple_type: nidaqmx.constants.ThermocoupleType,
        cold_junction_compensation_temperature: float,
        perform_auto_zero_mode: bool,
        auto_zero_mode: nidaqmx.constants.AutoZeroType,
    ) -> None:
        """Initializes an instance of
        `TemperatureThermocoupleMeasurementTerminalParameters` with specific values.

        Args:
            temperature_minimum_value_celsius_degrees (float):
                The minimum value expected from the measurement, expressed in °C.
            temperature_maximum_value_celsius_degrees (float):
                The maximum value expected from the measurement, expressed in °C.
            thermocouple_type (nidaqmx.constants.ThermocoupleType):
                Enum for ThermocoupleType: (B,E,J,K,N,R,S,T);
                Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.ThermocoupleType
            cold_junction_compensation_temperature (float):
                Specifies the temperature of the cold junction, expressed in °C;
                if cold_junction_compensation_source is set as 'CONSTANT_USER_VALUE'.
            perform_auto_zero_mode (bool):
                The option used to Enable or Disable Auto zero mode.
            auto_zero_mode (nidaqmx.constants.AutoZeroType):
                The option to set when to perform an auto zero during acquisition.
                Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.AutoZeroType


        Raises:
            ValueError:
                Raised when `temperature_minimum_value_celsius_degrees`
                is greater than or equal to `temperature_maximum_value_celsius_degrees`,
                `temperature_minimum_value_celsius_degrees` is None or not float,
                `temperature_maximum_value_celsius_degrees` is None or not float,
                `thermocouple_type` is None,
                'cold_junction_compensation_temperature' is None or not float,
                'perform_auto_zero_mode' is None,
                if 'perform_auto_zero_mode' is True and 'auto_zero_mode' is None.

        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (124 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(
            temperature_minimum_value_celsius_degrees,
            nameof(temperature_minimum_value_celsius_degrees),
        )
        Guard.is_float(
            temperature_minimum_value_celsius_degrees,
            nameof(temperature_minimum_value_celsius_degrees),
        )
        Guard.is_not_none(
            temperature_maximum_value_celsius_degrees,
            nameof(temperature_maximum_value_celsius_degrees),
        )
        Guard.is_float(
            temperature_maximum_value_celsius_degrees,
            nameof(temperature_maximum_value_celsius_degrees),
        )
        Guard.is_less_than(
            temperature_minimum_value_celsius_degrees,
            temperature_maximum_value_celsius_degrees,
            nameof(temperature_minimum_value_celsius_degrees),
        )
        Guard.is_not_none(
            thermocouple_type,
            nameof(thermocouple_type),
        )
        Guard.is_not_none(
            cold_junction_compensation_temperature,
            nameof(cold_junction_compensation_temperature),
        )
        Guard.is_float(
            cold_junction_compensation_temperature,
            nameof(cold_junction_compensation_temperature),
        )
        Guard.is_not_none(
            perform_auto_zero_mode,
            nameof(perform_auto_zero_mode),
        )
        if perform_auto_zero_mode is True:
            Guard.is_not_none(
                auto_zero_mode,
                nameof(auto_zero_mode),
            )

        self._temperature_minimum_value_celsius_degrees = temperature_minimum_value_celsius_degrees
        self._temperature_maximum_value_celsius_degrees = temperature_maximum_value_celsius_degrees
        self._thermocouple_type = thermocouple_type
        self._cold_junction_compensation_temperature = cold_junction_compensation_temperature
        self._perform_auto_zero_mode = perform_auto_zero_mode
        self._auto_zero_mode = auto_zero_mode

    @property
    def temperature_minimum_value_celsius_degrees(self) -> float:
        """
        :type:`float`:
            Gets the minimum value expected from the measurement, expressed in °C.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._temperature_minimum_value_celsius_degrees

    @property
    def temperature_maximum_value_celsius_degrees(self) -> float:
        """
        :type:`float`:
            Gets the maximum value expected from the measurement, expressed in °C.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._temperature_maximum_value_celsius_degrees

    @property
    def thermocouple_type(self) -> nidaqmx.constants.ThermocoupleType:
        """
        :type:`nidaqmx.constants.ThermocoupleType`:
            Enum for ThermocoupleType: (B,E,J,K,N,R,S,T);
            Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.ThermocoupleType
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (120 > 100 characters) (auto-generated noqa)
        return self._thermocouple_type

    @property
    def cold_junction_compensation_temperature(self) -> float:
        """
        :type:`float`:
           Cold junction compensation temperature, expressed in °C.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._cold_junction_compensation_temperature

    @property
    def perform_auto_zero_mode(self) -> bool:
        """
        :class:`bool`:
            The option used to Enable or Disable Auto zero mode.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._perform_auto_zero_mode

    @property
    def auto_zero_mode(
        self,
    ) -> nidaqmx.constants.AutoZeroType:
        """
        :class:`nidaqmx.constants.AutoZeroType`:
            The option to set when to perform an auto zero during acquisition.
                Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.AutoZeroType
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (120 > 100 characters) (auto-generated noqa)
        return self._auto_zero_mode


class TemperatureThermocoupleRangeAndTerminalParameters(PCBATestToolkitData):
    """Defines the parameters used to configure terminal
    of all channels for temperature measurement using Thermocouple."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (363 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        temperature_minimum_value_celsius_degrees: float,
        temperature_maximum_value_celsius_degrees: float,
        thermocouple_type: nidaqmx.constants.ThermocoupleType,
        cold_junction_compensation_source: nidaqmx.constants.CJCSource,
        cold_junction_compensation_temperature: float,
        cold_junction_compensation_channel_name: str,
        perform_auto_zero_mode: bool,
        auto_zero_mode: nidaqmx.constants.AutoZeroType,
    ) -> None:
        """Initializes an instance of
        `TemperatureThermocoupleRangeAndTerminalParameters` with specific values.

        Args:
            temperature_minimum_value_celsius_degrees (float):
                The minimum value expected from the measurement, expressed in °C.
            temperature_maximum_value_celsius_degrees (float):
                The maximum value expected from the measurement, expressed in °C.
            thermocouple_type (nidaqmx.constants.ThermocoupleType):
                Enum for ThermocoupleType: (B,E,J,K,N,R,S,T);
                Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.ThermocoupleType
            cold_junction_compensation_source (nidaqmx.constants.CJCSource):
                Specify the source for cold junction compensation: [CONSTANT_USER_VALUE, SCANNABLE_CHANNEL, BUILT_IN]
                Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.CJCSource
            cold_junction_compensation_temperature (float):
                Specifies the temperature of the cold junction, expressed in °C;
                if cold_junction_compensation_source is set as 'CONSTANT_USER_VALUE'.
            cold_junction_compensation_channel_name (str):
                Specifies the channel that acquires the temperature of the thermocouple cold-junction
                if cold_junction_compensation_source is set as 'SCANNABLE_CHANNEL'.
            perform_auto_zero_mode (bool):
                The option used to Enable or Disable Auto zero mode.
            auto_zero_mode (nidaqmx.constants.AutoZeroType):
                The option to set when to perform an auto zero during acquisition.
                Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.AutoZeroType


        Raises:
            ValueError:
                Raised when `temperature_minimum_value_celsius_degrees`
                is greater than or equal to `temperature_maximum_value_celsius_degrees`,
                `temperature_minimum_value_celsius_degrees` is None or not float,
                `temperature_maximum_value_celsius_degrees` is None or not float,
                `thermocouple_type` is None,
                'cold_junction_compensation_source' is None,
                if cold_junction_compensation_source==CONSTANT_USER_VALUE, then
                    'cold_junction_compensation_temperature' is None or not float,
                if cold_junction_compensation_source==SCANNABLE_CHANNEL, then
                    'cold_junction_compensation_channel_name' is None, empty or whitespace,
                'perform_auto_zero_mode' is None,
                if 'perform_auto_zero_mode' is True and 'auto_zero_mode' is None.

        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (124 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(
            temperature_minimum_value_celsius_degrees,
            nameof(temperature_minimum_value_celsius_degrees),
        )
        Guard.is_float(
            temperature_minimum_value_celsius_degrees,
            nameof(temperature_minimum_value_celsius_degrees),
        )
        Guard.is_not_none(
            temperature_maximum_value_celsius_degrees,
            nameof(temperature_maximum_value_celsius_degrees),
        )
        Guard.is_float(
            temperature_maximum_value_celsius_degrees,
            nameof(temperature_maximum_value_celsius_degrees),
        )
        Guard.is_less_than(
            temperature_minimum_value_celsius_degrees,
            temperature_maximum_value_celsius_degrees,
            nameof(temperature_minimum_value_celsius_degrees),
        )
        Guard.is_not_none(
            thermocouple_type,
            nameof(thermocouple_type),
        )
        Guard.is_not_none(
            cold_junction_compensation_source,
            nameof(cold_junction_compensation_source),
        )
        if cold_junction_compensation_source == nidaqmx.constants.CJCSource.CONSTANT_USER_VALUE:
            Guard.is_not_none(
                cold_junction_compensation_temperature,
                nameof(cold_junction_compensation_temperature),
            )
            Guard.is_float(
                cold_junction_compensation_temperature,
                nameof(cold_junction_compensation_temperature),
            )
        if cold_junction_compensation_source == nidaqmx.constants.CJCSource.SCANNABLE_CHANNEL:
            Guard.is_not_none_nor_empty_nor_whitespace(
                cold_junction_compensation_channel_name,
                nameof(cold_junction_compensation_channel_name),
            )
        Guard.is_not_none(
            perform_auto_zero_mode,
            nameof(perform_auto_zero_mode),
        )
        if perform_auto_zero_mode is True:
            Guard.is_not_none(
                auto_zero_mode,
                nameof(auto_zero_mode),
            )

        self._temperature_minimum_value_celsius_degrees = temperature_minimum_value_celsius_degrees
        self._temperature_maximum_value_celsius_degrees = temperature_maximum_value_celsius_degrees
        self._thermocouple_type = thermocouple_type
        self._cold_junction_compensation_source = cold_junction_compensation_source
        self._cold_junction_compensation_temperature = cold_junction_compensation_temperature
        self._cold_junction_compensation_channel_name = cold_junction_compensation_channel_name
        self._perform_auto_zero_mode = perform_auto_zero_mode
        self._auto_zero_mode = auto_zero_mode

    @property
    def temperature_minimum_value_celsius_degrees(self) -> float:
        """
        :type:`float`:
            Gets the minimum value expected from the measurement, expressed in °C.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._temperature_minimum_value_celsius_degrees

    @property
    def temperature_maximum_value_celsius_degrees(self) -> float:
        """
        :type:`float`:
            Gets the maximum value expected from the measurement, expressed in °C.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._temperature_maximum_value_celsius_degrees

    @property
    def thermocouple_type(self) -> nidaqmx.constants.ThermocoupleType:
        """
        :type:`nidaqmx.constants.ThermocoupleType`:
            Enum for ThermocoupleType: (B,E,J,K,N,R,S,T);
            Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.ThermocoupleType
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (120 > 100 characters) (auto-generated noqa)
        return self._thermocouple_type

    @property
    def cold_junction_compensation_source(self) -> nidaqmx.constants.CJCSource:
        """
        :type:`nidaqmx.constants.CJCSource`:
           Cold junction compensation Source.
           Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.CJCSource
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (112 > 100 characters) (auto-generated noqa)
        return self._cold_junction_compensation_source

    @property
    def cold_junction_compensation_temperature(self) -> float:
        """
        :type:`float`:
           Cold junction compensation temperature, expressed in °C.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._cold_junction_compensation_temperature

    @property
    def cold_junction_compensation_channel_name(self) -> str:
        """
        :type:`str`:
           Specify the channel to use for Cold junction compensation.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._cold_junction_compensation_channel_name

    @property
    def perform_auto_zero_mode(self) -> bool:
        """
        :class:`bool`:
            The option used to Enable or Disable Auto zero mode.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._perform_auto_zero_mode

    @property
    def auto_zero_mode(
        self,
    ) -> nidaqmx.constants.AutoZeroType:
        """
        :class:`nidaqmx.constants.AutoZeroType`:
            The option to set when to perform an auto zero during acquisition.
                Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.AutoZeroType
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (120 > 100 characters) (auto-generated noqa)
        return self._auto_zero_mode


class TemperatureThermocoupleChannelRangeAndTerminalParameters(PCBATestToolkitData):
    """Defines settings for channel and terminal used to configure temperature measurement based on thermocouple."""  # noqa: W505 - doc line too long (116 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        channel_name: str,
        channel_parameters: TemperatureThermocoupleRangeAndTerminalParameters,
    ) -> None:
        """Initializes an instance of
        `TemperatureThermocoupleChannelRangeAndTerminalParameters` with specific values.

        Args:
            channel_name (str):
                The name of the channel to configure.
            channel_parameters (TemperatureThermocoupleRangeAndTerminalParameters): The settings of the channel.

        Raises:
            ValueError:
                Raised when `channel_name` is None or empty or whitespace,
                `channel_parameters` is None.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (112 > 100 characters) (auto-generated noqa)
        Guard.is_not_none_nor_empty_nor_whitespace(channel_name, nameof(channel_name))
        Guard.is_not_none(channel_parameters, nameof(channel_parameters))

        self._channel_name = channel_name
        self._channel_parameters = channel_parameters

    @property
    def channel_name(self) -> str:
        """
        :type:`str`:
            Gets the name of the channel to configure.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._channel_name

    @property
    def channel_parameters(self) -> TemperatureThermocoupleRangeAndTerminalParameters:
        """
        :class:`TemperatureThermocoupleRangeAndTerminalParameters`:
            Gets the settings of the channel.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._channel_parameters


class TemperatureThermocoupleMeasurementConfiguration(PCBATestToolkitData):
    """Defines parameters used for configuration of Temperature measurement using Thermocouple."""

    def __init__(
        self,
        global_channel_parameters: TemperatureThermocoupleMeasurementTerminalParameters,
        specific_channels_parameters: List[
            TemperatureThermocoupleChannelRangeAndTerminalParameters
        ],
        measurement_execution_type: MeasurementExecutionType,
        sample_clock_timing_parameters: SampleClockTimingParameters,
        digital_start_trigger_parameters: DigitalStartTriggerParameters,
    ) -> None:
        """Initializes an instance of
        `TemperatureThermocoupleMeasurementConfiguration` with specific values.

        Args:
            global_channel_parameters (TemperatureThermocoupleMeasurementTerminalParameters):
                The settings of terminal for all channels.
            specific_channels_parameters (List[TemperatureThermocoupleChannelRangeAndTerminalParameters]):
                The list of instances of `TemperatureThermocoupleChannelRangeAndTerminalParameters`
                used to configure channels.
            measurement_execution_type (MeasurementExecutionType):
                The type of measurement execution selected by user.
            sample_clock_timing_parameters (SampleClockTimingParameters):
                An instance of `SampleClockTimingParameters` that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters`
                that represents the settings of triggers.

        Raises:
            TypeError:
                Raised when `specific_channels_parameters`
                contains objects that are not type of TemperatureThermocoupleChannelRangeAndTerminalParameters.
            ValueError:
                Raised when `global_channel_parameters` is None,
                `specific_channels_parameters` is None,
                `sample_clock_timing_parameters` is None,
                `digital_start_trigger_parameters` is None,
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (106 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(global_channel_parameters, nameof(global_channel_parameters))
        Guard.is_not_none(specific_channels_parameters, nameof(specific_channels_parameters))
        Guard.all_elements_are_of_same_type(
            input_list=specific_channels_parameters,
            expected_type=TemperatureThermocoupleChannelRangeAndTerminalParameters,
        )
        Guard.is_not_none(sample_clock_timing_parameters, nameof(sample_clock_timing_parameters))
        Guard.is_not_none(
            digital_start_trigger_parameters, nameof(digital_start_trigger_parameters)
        )

        self._global_channel_parameters = global_channel_parameters
        self._specific_channels_parameters = specific_channels_parameters
        self._measurement_execution_type = measurement_execution_type
        self._sample_clock_timing_parameters = sample_clock_timing_parameters
        self._digital_start_trigger_parameters = digital_start_trigger_parameters

    @property
    def global_channel_parameters(
        self,
    ) -> TemperatureThermocoupleMeasurementTerminalParameters:
        """
        :class:`TemperatureThermocoupleMeasurementTerminalParameters`:
            Gets the settings of terminal for all channels.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._global_channel_parameters

    @property
    def specific_channels_parameters(
        self,
    ) -> List[TemperatureThermocoupleChannelRangeAndTerminalParameters]:
        """
        :class:`List[TemperatureThermocoupleChannelRangeAndTerminalParameters]`:
            Gets the list of instances of `TemperatureThermocoupleChannelRangeAndTerminalParameters`
            used to configure channels.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._specific_channels_parameters

    @property
    def measurement_execution_type(self) -> MeasurementExecutionType:
        """
        :class:`MeasurementExecutionType`:
            Gets the type of measurement execution selected by user.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._measurement_execution_type

    @property
    def sample_clock_timing_parameters(self) -> SampleClockTimingParameters:
        """
        :class:`SampleClockTimingParameters`:
            Gets a `SampleClockTimingParameters` instance
            that represents the settings of timing.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._sample_clock_timing_parameters

    @property
    def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters:
        """
        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._digital_start_trigger_parameters


class TemperatureMeasurementResultData(PCBATestToolkitData):
    """Defines voltage temperature results obtained after waveform analysis."""

    def __init__(
        self,
        waveforms: List[AnalogWaveform],
        acquisition_duration_seconds: float,
        average_temperatures_celsius_degrees: List[float],
        average_temperatures_kelvin: List[float],
    ) -> None:
        """Initializes an instance of
           `TemperatureMeasurementResultData` with specific values.

        Args:
            waveforms (List[AnalogWaveform]):
                The list of waveforms acquired from channels defined for measurement
                and used to compute temperature.
            acquisition_duration_seconds (float):
                The duration of acquisition of samples for each configured channel.
            average_temperatures_celsius_degrees (List[float]):
                The list of average temperatures computed for each configured channel,
                expressed in celsius degrees.
            average_temperatures_kelvin (List[float]):
                The list of average temperatures computed for each configured channel,
                expressed in kelvin.

        Raises:
            ValueError:
                Raised when `waveforms` is None or empty,
                `average_temperatures_celsius` is None or empty,
                `average_temperatures_kelvin` is None or empty,
            TypeError:
                Raised when `waveforms` contains objects that are not `AnalogWaveform`,
                `acquisition_duration_seconds' is None,
                If the `acquisition_duration_seconds' is less than or equal to zero,
                `average_temperatures_celsius_degrees` contains objects that are not `float`,
                `average_temperatures_kelvin` contains objects that are not `float`
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(waveforms, nameof(waveforms))
        Guard.is_not_empty(waveforms, nameof(waveforms))
        Guard.is_not_none(
            acquisition_duration_seconds,
            nameof(acquisition_duration_seconds),
        )
        Guard.is_greater_than_zero(
            acquisition_duration_seconds, nameof(acquisition_duration_seconds)
        )
        Guard.is_not_none(
            average_temperatures_celsius_degrees,
            nameof(average_temperatures_celsius_degrees),
        )
        Guard.is_not_empty(
            average_temperatures_celsius_degrees,
            nameof(average_temperatures_celsius_degrees),
        )
        Guard.is_not_none(average_temperatures_kelvin, nameof(average_temperatures_kelvin))
        Guard.is_not_empty(average_temperatures_kelvin, nameof(average_temperatures_kelvin))
        Guard.all_elements_are_of_same_type(input_list=waveforms, expected_type=AnalogWaveform)
        Guard.all_elements_are_of_same_type(
            input_list=average_temperatures_celsius_degrees, expected_type=float
        )
        Guard.all_elements_are_of_same_type(
            input_list=average_temperatures_kelvin, expected_type=float
        )

        self._waveforms = waveforms
        self._acquisition_duration_seconds = acquisition_duration_seconds
        self._average_temperatures_celsius_degrees = average_temperatures_celsius_degrees
        self._average_temperatures_kelvin = average_temperatures_kelvin

    @property
    def waveforms(self) -> List[AnalogWaveform]:
        """
        :class:`List[AnalogWaveform]`:
            Gets list of waveforms acquired from channels defined for measurement
            and used to compute temperature.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._waveforms

    @property
    def acquisition_duration_seconds(self) -> float:
        """
        :type:`float`:
            Gets the duration of acquisition of samples for each configured channel.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._acquisition_duration_seconds

    @property
    def average_temperatures_celsius_degrees(self) -> List[float]:
        """
        :class:`List[float]`:
            Gets the list of average temperatures computed for each configured channel,
            expressed in celsius degrees.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._average_temperatures_celsius_degrees

    @property
    def average_temperatures_kelvin(self) -> List[float]:
        """
        :class:`List[float]`:
            Gets the list of average temperatures computed for each configured channel,
            expressed in kelvins.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._average_temperatures_kelvin
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_measurement.py sha256=999daaa3549b0015e14963e1cedc3636235764d50da15a4f03caee4dba50f26b bytes=7553 -->
## FILE: src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_measurement.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_measurement.py`
- sha256: `999daaa3549b0015e14963e1cedc3636235764d50da15a4f03caee4dba50f26b`
- bytes: 7553

````python
"""Defines class with common methods used for temperature measurements on PCB points."""

import nidaqmx.constants
import nidaqmx.stream_readers
import numpy
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    AnalogWaveform,
    DigitalStartTriggerParameters,
    MeasurementData,
    SampleClockTimingParameters,
    SampleTimingEngine,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.daq.temperature_measurements.temperature_constants import (
    ConstantsForTemperatureMeasurement,
)
from nipcbatt.pcbatt_library.daq.temperature_measurements.temperature_data_types import (
    TemperatureMeasurementResultData,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_utilities.guard_utilities import Guard
from nipcbatt.pcbatt_utilities.numeric_utilities import invert_value


class TemperatureMeasurement(BuildingBlockUsingDAQmx):
    """Defines a way that allows you to perform Temperature measurements on PCB points."""

    def close(self):
        """Closes measurement procedure and releases internal resources."""
        if not self.is_task_initialized:
            return

        # Stop and close the DAQmx task
        self.task.stop()
        self.task.close()

    def configure_timing(self, parameters: SampleClockTimingParameters):
        """Configures the timing characteristics used for temperature measurements.

        Args:
            parameters (SampleClockTimingParameters):
            An instance of `SampleClockTimingParameters`
            used to configure the timing.
        """  # noqa: D202, D417, W505 - No blank lines allowed after function docstring (auto-generated noqa), Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

        self.task.timing.cfg_samp_clk_timing(
            rate=parameters.sampling_rate_hertz,
            sample_mode=nidaqmx.constants.AcquisitionType.FINITE,
            samps_per_chan=parameters.number_of_samples_per_channel,
            source=parameters.sample_clock_source,
        )

        # if the current timing engine setting is Auto
        # then delete the previous timing engine property
        # and let the task revert to the default setting of DAQmx
        # to automatically set the value of the timing engine
        if parameters.sample_timing_engine == SampleTimingEngine.AUTO:
            # Sample timing engine is auto selected
            ...
        else:
            self.task.timing.samp_timing_engine = parameters.sample_timing_engine.value

    def configure_trigger(self, parameters: DigitalStartTriggerParameters):
        """Configure the characteristics of triggers used for temperature measurements.

        Args:
            parameters (DigitalStartTriggerParameters):
            An instance of `DigitalStartTriggerParameters`
            used to configure the channels.
        """  # noqa: D202, D417, W505 - No blank lines allowed after function docstring (auto-generated noqa), Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

        if parameters.trigger_select == StartTriggerType.NO_TRIGGER:
            self.task.triggers.start_trigger.disable_start_trig()
        else:
            self.task.triggers.start_trigger.cfg_dig_edge_start_trig(
                trigger_source=parameters.digital_start_trigger_source,
                trigger_edge=parameters.digital_start_trigger_edge,
            )

    def acquire_data_for_measurement_analysis(self) -> MeasurementData:
        """Acquires Data from DAQ channel for measurement of temperature.

        Returns:
            MeasurementData: An instance of `MeasurementData`
            that specifies the data acquired from DAQ channels.
        """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

        # Builds the shape of numpy array (number of channels, number of samples per channel)
        number_of_channels = len(self.task.in_stream.channels_to_read.channel_names)
        number_of_samples_per_channel = self.task.timing.samp_quant_samp_per_chan

        # Build the numpy array.
        data_to_read = numpy.zeros(
            shape=(number_of_channels, number_of_samples_per_channel),
            dtype=numpy.float64,
        )

        # Reads data and fill numpy array.
        reader = nidaqmx.stream_readers.AnalogMultiChannelReader(self.task.in_stream)
        reader.read_many_sample(
            data=data_to_read,
            number_of_samples_per_channel=number_of_samples_per_channel,
        )

        return MeasurementData(data_to_read)

    def analyze_measurement_data(
        self,
        measurement_data: MeasurementData,
    ) -> TemperatureMeasurementResultData:
        """Proceeds to the analysis of temperatures from the measurement.

        Args:
            measurement_data (MeasurementData): An instance of `MeasurementData`
            that specifies the data acquired from DAQ channels.

        Returns:
            TemperatureMeasurementResultData:
            An instance of `TemperatureMeasurementResultData`
            that specifies the measurement results.
        """
        # Check if sampling rate is 0 and raise error to avoid divide by 0 error.
        Guard.is_greater_than_zero(
            self.task.timing.samp_clk_rate, nameof(self.task.timing.samp_clk_rate)
        )
        delta_time_seconds = invert_value(self.task.timing.samp_clk_rate)

        # Initialization for TemperatureMeasurementResultData instance creation.
        waveform = []
        avg_temps_celsius_degrees = []
        avg_temps_kelvin = []
        acq_duration_seconds = 0.0

        for samples_per_channel, channel_name in zip(
            measurement_data.samples_per_channel,
            self.task.in_stream.channels_to_read.channel_names,
        ):
            # samples_per_channel contains samples captured
            # from the channel which name is channel_name.
            # Assures that the samples array is not empty and contain only float values.

            Guard.all_elements_are_of_same_type(samples_per_channel, float)
            Guard.is_not_empty(samples_per_channel, nameof(samples_per_channel))

            acq_duration_seconds = delta_time_seconds * len(samples_per_channel)

            # Creates an instance of AnalogWaveform and add it to waveforms.
            waveform.append(
                AnalogWaveform(
                    channel_name=channel_name,
                    delta_time_seconds=delta_time_seconds,
                    samples=samples_per_channel,
                )
            )

            mean_temperature_celsius_degrees = numpy.mean(samples_per_channel)
            avg_temps_celsius_degrees.append(mean_temperature_celsius_degrees)
            avg_temps_kelvin.append(
                mean_temperature_celsius_degrees
                - ConstantsForTemperatureMeasurement.ABSOLUTE_ZERO_CELSIUS_DEGREES
            )

        return TemperatureMeasurementResultData(
            waveforms=waveform,
            acquisition_duration_seconds=acq_duration_seconds,
            average_temperatures_celsius_degrees=avg_temps_celsius_degrees,
            average_temperatures_kelvin=avg_temps_kelvin,
        )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_measurement_using_rtd.py sha256=8eed9eb0c185de6ef9b5d14bfe53e3ead98439acba558063e73b76dd32dc6a78 bytes=11007 -->
## FILE: src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_measurement_using_rtd.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_measurement_using_rtd.py`
- sha256: `8eed9eb0c185de6ef9b5d14bfe53e3ead98439acba558063e73b76dd32dc6a78`
- bytes: 11007

````python
"""Defines class used for temperature measurement using RTD on PCB points."""

import nidaqmx
import nidaqmx.constants
import nidaqmx.stream_readers

from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
from nipcbatt.pcbatt_library.daq.temperature_measurements.temperature_constants import (
    ConstantsForTemperatureMeasurement,
    ConstantsForTemperatureMeasurementUsingRtd,
)
from nipcbatt.pcbatt_library.daq.temperature_measurements.temperature_data_types import (
    TemperatureRtdMeasurementChannelParameters,
    TemperatureRtdMeasurementConfiguration,
    TemperatureRtdMeasurementTerminalParameters,
)
from nipcbatt.pcbatt_library.daq.temperature_measurements.temperature_measurement import (
    TemperatureMeasurement,
)


class TemperatureMeasurementUsingRtd(TemperatureMeasurement):
    """Defines a way that allows you to perform Temperature measurements using RTD on PCB points."""

    def initialize(self, channel_expression: str):
        """Initializes the measurement with the specific channels

        Args:
            channel_expression (str):
                Expression representing the name of a physical channel,
                or a global channel in DAQ System.
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        if self.is_task_initialized:
            return

        # If the input channel_expression contains global channel, then add them as global channels
        # and verify if the global channels are configured for current measurement.
        if self.contains_only_global_virtual_channels(channel_expression=channel_expression):
            self.add_global_channels(global_channel_expression=channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
            self.verify_measurement_type(nidaqmx.constants.UsageTypeAI.TEMPERATURE_RTD)
        else:
            # Add the channel_expression to analog input current channel of the Daqmx task
            self.task.ai_channels.add_ai_rtd_chan(
                physical_channel=channel_expression,
                name_to_assign_to_channel="",
                min_val=(
                    ConstantsForTemperatureMeasurement.INITIAL_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES
                ),
                max_val=(
                    ConstantsForTemperatureMeasurement.DEFAULT_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES
                ),
                units=ConstantsForTemperatureMeasurement.INITIAL_AI_TEMPERATURE_UNITS,
                rtd_type=ConstantsForTemperatureMeasurementUsingRtd.INITIAL_RTD_TYPE,
                resistance_config=(
                    ConstantsForTemperatureMeasurementUsingRtd.INITIAL_RTD_RESISTANCE_CONFIGURATION
                ),
                current_excit_source=(
                    ConstantsForTemperatureMeasurementUsingRtd.INITIAL_RTD_EXCITATION_SOURCE
                ),
                current_excit_val=(
                    ConstantsForTemperatureMeasurementUsingRtd.DEFAULT_CURRENT_EXCITATION_VALUE_AMPERES
                ),
                r_0=ConstantsForTemperatureMeasurementUsingRtd.INITIAL_SENSOR_RESISTANCE_OHMS,
            )

    def configure_and_measure(self, configuration: TemperatureRtdMeasurementConfiguration):
        """Configures and/or performs a measurement
           according to specific configuration parameters.

        Args:
            configuration (TemperatureRtdMeasurementConfiguration):
            A instance of `TemperatureRtdMeasurementConfiguration`
            used to configure the measurement.

        Returns:
            TemperatureMeasurementResultData | None:
            An instance of `TemperatureMeasurementResultData`
            or `None` if no measure was performed.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        if configuration.measurement_execution_type in (
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.CONFIGURE_ONLY,
        ):
            self.configure_all_channels(configuration.global_channel_parameters)
            for specific_channel_parameters in configuration.specific_channels_parameters:
                self.configure_specific_channel(specific_channel_parameters)
            self.configure_timing(configuration.sample_clock_timing_parameters)
            self.configure_trigger(configuration.digital_start_trigger_parameters)

        if configuration.measurement_execution_type in (
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.MEASURE_ONLY,
        ):
            data = self.acquire_data_for_measurement_analysis()
            return self.analyze_measurement_data(data)

        return None

    def configure_all_channels(self, parameters: TemperatureRtdMeasurementTerminalParameters):
        """Configures all channels used for temperature measurements using RTD.

        Args:
            parameters (TemperatureRtdMeasurementTerminalParameters):
            An instance of `TemperatureRtdMeasurementTerminalParameters`
            used to configure the channels.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        self.task.ai_channels.all.ai_adc_timing_mode = parameters.adc_timing_mode
        for channel in self.task.ai_channels:
            channel.ai_min = parameters.temperature_minimum_value_celsius_degrees
            channel.ai_max = parameters.temperature_maximum_value_celsius_degrees
            channel.ai_rtd_type = parameters.rtd_type
            channel.ai_rtd_r0 = parameters.sensor_resistance_ohms
            channel.ai_excit_src = parameters.excitation_source
            channel.ai_excit_val = parameters.current_excitation_value_amperes
            channel.ai_excit_voltage_or_current = (
                nidaqmx.constants.ExcitationVoltageOrCurrent.USE_CURRENT
            )
            channel.ai_resistance_cfg = parameters.resistance_configuration

    def configure_specific_channel(self, parameters: TemperatureRtdMeasurementChannelParameters):
        """Configures the specific channels used for temperature measurements using RTD.

        Args:
            parameters (TemperatureRtdMeasurementChannelParameters):
            An instance of `TemperatureRtdMeasurementChannelParameters`
            used to configure the channels.

        If the user provides Global Virtual Channel name in Initialize(),
        then he/she has to provide the Virtual channel name in Specific channel parameters as well.

        Similarly, if the user provides Physical channel name in Initialize(),
        then he/she has to provide the Physical channel name in Specific channel parameters.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        if parameters.channel_name in (channel.name for channel in self.task.ai_channels):
            # if the specified channel is present in ai_channel_collection,
            # updates the voltage parameters of the channel
            self.task.ai_channels[parameters.channel_name].ai_rtd_type = parameters.rtd_type
            self.task.ai_channels[
                parameters.channel_name
            ].ai_rtd_r0 = parameters.sensor_resistance_ohms
            self.task.ai_channels[
                parameters.channel_name
            ].ai_resistance_cfg = parameters.resistance_configuration
            self.task.ai_channels[
                parameters.channel_name
            ].ai_excit_src = parameters.excitation_source
            self.task.ai_channels[
                parameters.channel_name
            ].ai_excit_val = parameters.current_excitation_value_amperes
            self.task.ai_channels[
                parameters.channel_name
            ].ai_excit_voltage_or_current = nidaqmx.constants.ExcitationVoltageOrCurrent.USE_CURRENT
        else:
            # otherwise, adds the channel.
            if self.contains_only_global_virtual_channels(
                channel_expression=parameters.channel_name
            ):
                # Global virtual channel
                self.add_global_channels(global_channel_expression=parameters.channel_name)
                self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
                self.verify_measurement_type(nidaqmx.constants.UsageTypeAI.TEMPERATURE_RTD)
                for channel in self.task.ai_channels:
                    channel.ai_min = (
                        ConstantsForTemperatureMeasurement.INITIAL_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES
                    )
                    channel.ai_max = (
                        ConstantsForTemperatureMeasurement.DEFAULT_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES
                    )
                    channel.ai_rtd_type = parameters.rtd_type
                    channel.ai_rtd_r0 = parameters.sensor_resistance_ohms
                    channel.ai_excit_src = parameters.excitation_source
                    channel.ai_excit_val = parameters.current_excitation_value_amperes
                    channel.ai_excit_voltage_or_current = (
                        nidaqmx.constants.ExcitationVoltageOrCurrent.USE_CURRENT
                    )
                    channel.ai_resistance_cfg = parameters.resistance_configuration
                    channel.ai_adc_timing_mode = (
                        ConstantsForTemperatureMeasurementUsingRtd.DEFAULT_ADC_TIMING_MODE
                    )

            else:
                # Physical channel
                self.task.ai_channels.add_ai_rtd_chan(
                    physical_channel=parameters.channel_name,
                    name_to_assign_to_channel="",
                    min_val=(
                        ConstantsForTemperatureMeasurement.INITIAL_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES
                    ),
                    max_val=(
                        ConstantsForTemperatureMeasurement.DEFAULT_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES
                    ),
                    units=ConstantsForTemperatureMeasurement.INITIAL_AI_TEMPERATURE_UNITS,
                    rtd_type=parameters.rtd_type,
                    resistance_config=parameters.resistance_configuration,
                    current_excit_source=parameters.excitation_source,
                    current_excit_val=parameters.current_excitation_value_amperes,
                    r_0=parameters.sensor_resistance_ohms,
                )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_measurement_using_thermistor.py sha256=33310733f9a373d443759e49f2448cd80537a7e0a3f62cf9defb881affb27a33 bytes=14349 -->
## FILE: src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_measurement_using_thermistor.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_measurement_using_thermistor.py`
- sha256: `33310733f9a373d443759e49f2448cd80537a7e0a3f62cf9defb881affb27a33`
- bytes: 14349

````python
# pylint: disable=C0301
# remove it when arguments of initialize are used.
"""Defines class used for temperature measurement using Thermistor on PCB points."""

import math

import nidaqmx.constants

from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
from nipcbatt.pcbatt_library.daq.temperature_measurements.temperature_constants import (
    ConstantsForTemperatureMeasurement,
    ConstantsForTemperatureMeasurementUsingThermistor,
)
from nipcbatt.pcbatt_library.daq.temperature_measurements.temperature_data_types import (
    CoefficientsSteinhartHartParameters,
    SteinhartHartEquationOption,
    TemperatureThermistorChannelRangeAndTerminalParameters,
    TemperatureThermistorMeasurementConfiguration,
    TemperatureThermistorRangeAndTerminalParameters,
)
from nipcbatt.pcbatt_library.daq.temperature_measurements.temperature_measurement import (
    TemperatureMeasurement,
)
from nipcbatt.pcbatt_utilities.numeric_utilities import invert_value


class TemperatureMeasurementUsingThermistor(TemperatureMeasurement):
    """Defines a way that allows you to perform Temperature measurements
    using Thermistor on PCB points."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (331 > 100 characters) (auto-generated noqa)

    def initialize(self, channel_expression: str):
        """Initializes the measurement with the specific channels
        Args:
            channel_expression (str):
                Expression representing the name of a physical channel,
                or a global channel in DAQ System.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        if self.is_task_initialized:
            return

        # If the input channel_expression contains global channel, then add them as global channels
        # and verify if the global channels are configured for current measurement.
        if self.contains_only_global_virtual_channels(channel_expression=channel_expression):
            self.add_global_channels(global_channel_expression=channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
            self.verify_measurement_type(nidaqmx.constants.UsageTypeAI.TEMPERATURE_THERMISTOR)
        else:
            # Add the channel_expression to analog input current channel of the Daqmx task
            self.task.ai_channels.add_ai_thrmstr_chan_vex(
                physical_channel=channel_expression,
                name_to_assign_to_channel="",
                min_val=(
                    ConstantsForTemperatureMeasurement.INITIAL_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES
                ),
                max_val=(
                    ConstantsForTemperatureMeasurement.INITIAL_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES
                ),
                units=ConstantsForTemperatureMeasurement.INITIAL_AI_TEMPERATURE_UNITS,
                resistance_config=(
                    ConstantsForTemperatureMeasurementUsingThermistor.INITIAL_THERMISTOR_RESISTANCE_CONFIGURATION
                ),
                voltage_excit_source=(
                    ConstantsForTemperatureMeasurementUsingThermistor.INITIAL_THERMISTOR_EXCITATION_SOURCE
                ),
                voltage_excit_val=(
                    ConstantsForTemperatureMeasurementUsingThermistor.INITIAL_VOLTAGE_EXCITATION_VALUE_VOLTS
                ),
                a=ConstantsForTemperatureMeasurementUsingThermistor.INITIAL_COEFFICIENT_STAINHART_HART_A,
                b=ConstantsForTemperatureMeasurementUsingThermistor.INITIAL_COEFFICIENT_STAINHART_HART_B,
                c=ConstantsForTemperatureMeasurementUsingThermistor.INITIAL_COEFFICIENT_STAINHART_HART_C,
                r_1=ConstantsForTemperatureMeasurementUsingThermistor.INITIAL_THERMISTOR_RESISTOR_OHMS,
            )

    def configure_and_measure(self, configuration: TemperatureThermistorMeasurementConfiguration):
        """Configures and/or performs a measurement
           according to specific configuration parameters.

        Args:
            configuration (TemperatureRtdMeasurementConfiguration):
            A instance of `TemperatureRtdMeasurementConfiguration`
            used to configure the measurement.

        Returns:
            TemperatureMeasurementResultData | None:
            An instance of `TemperatureMeasurementResultData`
            or `None` if no measure was performed.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        if configuration.measurement_execution_type in (
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.CONFIGURE_ONLY,
        ):
            self.configure_all_channels(configuration.global_channel_parameters)
            for specific_channel_parameters in configuration.specific_channels_parameters:
                self.configure_specific_channel(specific_channel_parameters)
            self.configure_timing(configuration.sample_clock_timing_parameters)
            self.configure_trigger(configuration.digital_start_trigger_parameters)

        if configuration.measurement_execution_type in (
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.MEASURE_ONLY,
        ):
            data = self.acquire_data_for_measurement_analysis()
            return self.analyze_measurement_data(data)

        return None

    def configure_all_channels(self, parameters: TemperatureThermistorRangeAndTerminalParameters):
        """Configures all channels used for temperature measurements using a Thermistor.

        Args:
            parameters (TemperatureThermistorRangeAndTerminalParameters):
            An instance of `TemperatureThermistorRangeAndTerminalParameters`
            used to configure the channels.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        for channel in self.task.ai_channels:
            channel.ai_min = parameters.temperature_minimum_value_celsius_degrees
            channel.ai_max = parameters.temperature_maximum_value_celsius_degrees
            channel.ai_term_cfg = parameters.terminal_configuration
            channel.ai_thrmstr_r1 = parameters.thermistor_resistor_ohms
            channel.ai_excit_val = parameters.voltage_excitation_value_volts
            stainhart_hart_coefficients = self._compute_steinhart_hart_coefficients_from_parameters(
                parameters
            )
            channel.ai_thrmstr_a = stainhart_hart_coefficients.coefficient_steinhart_hart_a
            channel.ai_thrmstr_b = stainhart_hart_coefficients.coefficient_steinhart_hart_b
            channel.ai_thrmstr_c = stainhart_hart_coefficients.coefficient_steinhart_hart_c

    def configure_specific_channel(
        self, parameters: TemperatureThermistorChannelRangeAndTerminalParameters
    ):
        """Configures the specific channels used for temperature measurements using a Thermistor.

        Args:
            parameters (TemperatureThermistorChannelRangeAndTerminalParameters):
            An instance of `TemperatureThermistorChannelRangeAndTerminalParameters`
            used to configure the channels.

        If the user provides Global Virtual Channel name in Initialize(),
        then he/she has to provide the Virtual channel name in Specific channel parameters as well.

        Similarly, if the user provides Physical channel name in Initialize(),
        then he/she has to provide the Physical channel name in Specific channel parameters.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        stainhart_hart_coefficients = self._compute_steinhart_hart_coefficients_from_parameters(
            parameters.channel_parameters
        )
        if parameters.channel_name in (channel.name for channel in self.task.ai_channels):
            # if the specified channel is present in ai_channel_collection,
            # updates the voltage parameters of the channel
            channel = self.task.ai_channels[parameters.channel_name]
            channel.ai_min = parameters.channel_parameters.temperature_minimum_value_celsius_degrees
            channel.ai_max = parameters.channel_parameters.temperature_maximum_value_celsius_degrees
            channel.ai_term_cfg = parameters.channel_parameters.terminal_configuration
            channel.ai_excit_val = parameters.channel_parameters.voltage_excitation_value_volts
            channel.ai_thrmstr_r1 = parameters.channel_parameters.thermistor_resistor_ohms
            channel.ai_thrmstr_a = stainhart_hart_coefficients.coefficient_steinhart_hart_a
            channel.ai_thrmstr_b = stainhart_hart_coefficients.coefficient_steinhart_hart_b
            channel.ai_thrmstr_c = stainhart_hart_coefficients.coefficient_steinhart_hart_c
        else:
            # otherwise, adds the channel.
            if self.contains_only_global_virtual_channels(
                channel_expression=parameters.channel_name
            ):
                # Global virtual channel
                self.add_global_channels(global_channel_expression=parameters.channel_name)
                self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
                self.verify_measurement_type(nidaqmx.constants.UsageTypeAI.TEMPERATURE_THERMISTOR)
                for channel in self.task.ai_channels:
                    channel.ai_min = (
                        parameters.channel_parameters.temperature_minimum_value_celsius_degrees
                    )
                    channel.ai_max = (
                        parameters.channel_parameters.temperature_maximum_value_celsius_degrees
                    )
                    channel.ai_term_cfg = parameters.channel_parameters.terminal_configuration
                    channel.ai_thrmstr_r1 = parameters.channel_parameters.thermistor_resistor_ohms
                    channel.ai_excit_val = (
                        parameters.channel_parameters.voltage_excitation_value_volts
                    )
                    channel.ai_thrmstr_a = stainhart_hart_coefficients.coefficient_steinhart_hart_a
                    channel.ai_thrmstr_b = stainhart_hart_coefficients.coefficient_steinhart_hart_b
                    channel.ai_thrmstr_c = stainhart_hart_coefficients.coefficient_steinhart_hart_c

            else:
                # physical channel
                channel = self.task.ai_channels.add_ai_thrmstr_chan_vex(
                    physical_channel=parameters.channel_name,
                    name_to_assign_to_channel="",
                    min_val=(
                        parameters.channel_parameters.temperature_minimum_value_celsius_degrees
                    ),
                    max_val=(
                        parameters.channel_parameters.temperature_maximum_value_celsius_degrees
                    ),
                    units=ConstantsForTemperatureMeasurement.INITIAL_AI_TEMPERATURE_UNITS,
                    resistance_config=(
                        ConstantsForTemperatureMeasurementUsingThermistor.INITIAL_THERMISTOR_RESISTANCE_CONFIGURATION
                    ),
                    voltage_excit_source=(
                        ConstantsForTemperatureMeasurementUsingThermistor.INITIAL_THERMISTOR_EXCITATION_SOURCE
                    ),
                    voltage_excit_val=(
                        parameters.channel_parameters.voltage_excitation_value_volts
                    ),
                    a=stainhart_hart_coefficients.coefficient_steinhart_hart_a,
                    b=stainhart_hart_coefficients.coefficient_steinhart_hart_b,
                    c=stainhart_hart_coefficients.coefficient_steinhart_hart_c,
                    r_1=parameters.channel_parameters.thermistor_resistor_ohms,
                )
                self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
                channel.ai_term_cfg = parameters.channel_parameters.terminal_configuration

    def _compute_steinhart_hart_coefficients_from_parameters(
        self, parameters: TemperatureThermistorRangeAndTerminalParameters
    ) -> CoefficientsSteinhartHartParameters:
        if (
            parameters.steinhart_hart_equation_option
            == SteinhartHartEquationOption.USE_STEINHART_HART_COEFFICIENTS
        ):
            return parameters.coefficients_steinhart_hart_parameters

        return self._compute_steinhart_hart_coefficients(
            parameters.beta_coefficient_and_sensor_resistance_parameters.coefficient_steinhart_hart_beta_kelvins,
            parameters.beta_coefficient_and_sensor_resistance_parameters.sensor_resistance_ohms,
        )

    def _compute_steinhart_hart_coefficients(
        self,
        coefficient_steinhart_hart_beta_kelvins: float,
        sensor_resistance_ohms: float,
    ) -> CoefficientsSteinhartHartParameters:
        """Computes coefficients of Steinhart-Hart equation."""
        return CoefficientsSteinhartHartParameters(
            coefficient_steinhart_hart_a=invert_value(
                ConstantsForTemperatureMeasurementUsingThermistor.THERMISTOR_REFERENCE_TEMPERATURE_KELVINS
            )
            - invert_value(coefficient_steinhart_hart_beta_kelvins)
            * math.log(sensor_resistance_ohms),
            coefficient_steinhart_hart_b=invert_value(coefficient_steinhart_hart_beta_kelvins),
            coefficient_steinhart_hart_c=0,
        )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_measurement_using_thermocouple.py sha256=5e668244086dc99339b460a8118704c5bbf782dd89f00c3bc560e5a2b9705b13 bytes=11646 -->
## FILE: src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_measurement_using_thermocouple.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/temperature_measurements/temperature_measurement_using_thermocouple.py`
- sha256: `5e668244086dc99339b460a8118704c5bbf782dd89f00c3bc560e5a2b9705b13`
- bytes: 11646

````python
"""Defines class used for temperature measurement using Thermocouple on PCB points."""

import nidaqmx.constants

from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
from nipcbatt.pcbatt_library.daq.temperature_measurements.temperature_constants import (
    ConstantsForTemperatureMeasurement,
    ConstantsForTemperatureMeasurementUsingThermocouple,
)
from nipcbatt.pcbatt_library.daq.temperature_measurements.temperature_data_types import (
    TemperatureThermocoupleChannelRangeAndTerminalParameters,
    TemperatureThermocoupleMeasurementConfiguration,
    TemperatureThermocoupleMeasurementTerminalParameters,
)
from nipcbatt.pcbatt_library.daq.temperature_measurements.temperature_measurement import (
    TemperatureMeasurement,
)


class TemperatureMeasurementUsingThermocouple(TemperatureMeasurement):
    """Defines a way that allows you to perform Temperature measurements
    using Thermocouple on PCB points."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (333 > 100 characters) (auto-generated noqa)

    def initialize(
        self,
        channel_expression: str,
        cold_junction_compensation_channel: str,
        cold_junction_compensation_source=nidaqmx.constants.CJCSource.BUILT_IN,
    ):
        """Initializes the measurement with the specific channels
        Args:
            channel_expression (str):
                Expression representing the name of a physical channel,
                or a global channel in DAQ System.
            cold_junction_compensation_channel (str):
                Expression representing channel for cold junction compensation when 'cold_junction_compensation_source'
                is specified as 'nidaqmx.constants.CJCSource.SCANNABLE_CHANNEL'.
            cold_junction_compensation_source (nidaqmx.constants.CJCSource):
                Specify the source for cold junction compensation: [CONSTANT_USER_VALUE, SCANNABLE_CHANNEL, BUILT_IN]
                Default value is set as BUILT_IN.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (119 > 100 characters) (auto-generated noqa)
        if self.is_task_initialized:
            return
        # If the input channel_expression contains global channel, then add them as global channels
        # and verify if the global channels are configured for temperature measurement.
        if self.contains_only_global_virtual_channels(channel_expression=channel_expression):
            self.add_global_channels(global_channel_expression=channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
            self.verify_measurement_type(nidaqmx.constants.UsageTypeAI.TEMPERATURE_THERMOCOUPLE)
        else:
            # Add the channel_expression to analog input temperature channel of the Daqmx task
            self.task.ai_channels.add_ai_thrmcpl_chan(
                physical_channel=channel_expression,
                name_to_assign_to_channel="",
                min_val=(
                    ConstantsForTemperatureMeasurement.DEFAULT_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES
                ),
                max_val=(
                    ConstantsForTemperatureMeasurement.DEFAULT_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES
                ),
                units=(ConstantsForTemperatureMeasurement.INITIAL_AI_TEMPERATURE_UNITS),
                thermocouple_type=(
                    ConstantsForTemperatureMeasurementUsingThermocouple.DEFAULT_THERMOCOUPLE_TYPE
                ),
                cjc_source=cold_junction_compensation_source,
                cjc_val=(
                    ConstantsForTemperatureMeasurementUsingThermocouple.DEFAULT_COLD_JUNCTION_COMPENSATION_TEMPERATURE
                ),
                cjc_channel=cold_junction_compensation_channel,
            )

    def configure_and_measure(self, configuration: TemperatureThermocoupleMeasurementConfiguration):
        """Configures and/or performs a measurement
           according to specific configuration parameters.

        Args:
            configuration (TemperatureThermocoupleMeasurementConfiguration):
            A instance of `TemperatureThermocoupleMeasurementConfiguration`
            used to configure the measurement.

        Returns:
            TemperatureMeasurementResultData | None:
            An instance of `TemperatureMeasurementResultData`
            or `None` if no measure was performed.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        if configuration.measurement_execution_type in (
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.CONFIGURE_ONLY,
        ):
            self.configure_all_channels(configuration.global_channel_parameters)
            for specific_channel_parameters in configuration.specific_channels_parameters:
                self.configure_specific_channel(specific_channel_parameters)
            self.configure_timing(configuration.sample_clock_timing_parameters)
            self.configure_trigger(configuration.digital_start_trigger_parameters)

        if configuration.measurement_execution_type in (
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.MEASURE_ONLY,
        ):
            data = self.acquire_data_for_measurement_analysis()
            return self.analyze_measurement_data(data)

        return None

    def configure_all_channels(
        self, parameters: TemperatureThermocoupleMeasurementTerminalParameters
    ):
        """Configures all channels used for temperature measurements using a Thermocouple.

        Args:
            parameters (TemperatureThermocoupleMeasurementTerminalParameters):
            An instance of `TemperatureThermocoupleMeasurementTerminalParameters`
            used to configure the channels.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        for channel in self.task.ai_channels:
            channel.ai_min = parameters.temperature_minimum_value_celsius_degrees
            channel.ai_max = parameters.temperature_maximum_value_celsius_degrees
            channel.ai_thrmcpl_type = parameters.thermocouple_type
            channel.ai_thrmcpl_cjc_val = parameters.cold_junction_compensation_temperature
            if parameters.perform_auto_zero_mode is True:
                channel.ai_auto_zero_mode = parameters.auto_zero_mode

    def configure_specific_channel(
        self, parameters: TemperatureThermocoupleChannelRangeAndTerminalParameters
    ):
        """Configures the specific channels used for temperature measurements using a Thermocouple.

        Args:
            parameters (TemperatureThermocoupleChannelRangeAndTerminalParameters):
            An instance of `TemperatureThermocoupleChannelRangeAndTerminalParameters`
            used to configure the channels.

        If the user provides Global Virtual Channel name in Initialize(),
        then he/she has to provide the Virtual channel name in Specific channel parameters as well.

        Similarly, if the user provides Physical channel name in Initialize(),
        then he/she has to provide the Physical channel name in Specific channel parameters.
        """  # noqa: D202, D417, W505 - No blank lines allowed after function docstring (auto-generated noqa), Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

        if parameters.channel_name in (channel.name for channel in self.task.ai_channels):
            # if the specified channel is present in ai_channel_collection,
            # updates the thermocouple parameters of the channel
            channel = self.task.ai_channels[parameters.channel_name]
            channel.ai_min = parameters.channel_parameters.temperature_minimum_value_celsius_degrees
            channel.ai_max = parameters.channel_parameters.temperature_maximum_value_celsius_degrees
            channel.ai_thrmcpl_type = parameters.channel_parameters.thermocouple_type
            channel.ai_thrmcpl_cjc_val = (
                parameters.channel_parameters.cold_junction_compensation_temperature
            )
            if parameters.channel_parameters.perform_auto_zero_mode is True:
                channel.ai_auto_zero_mode = parameters.channel_parameters.auto_zero_mode
        else:
            # otherwise, adds the channel.
            if self.contains_only_global_virtual_channels(
                channel_expression=parameters.channel_name
            ):
                # Global virtual channel
                self.add_global_channels(global_channel_expression=parameters.channel_name)
                self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
                self.verify_measurement_type(nidaqmx.constants.UsageTypeAI.TEMPERATURE_THERMOCOUPLE)
                for channel in self.task.ai_channels:
                    channel.ai_min = (
                        parameters.channel_parameters.temperature_minimum_value_celsius_degrees
                    )
                    channel.ai_max = (
                        parameters.channel_parameters.temperature_maximum_value_celsius_degrees
                    )
                    channel.ai_thrmcpl_type = parameters.channel_parameters.thermocouple_type
                    channel.ai_thrmcpl_cjc_val = (
                        parameters.channel_parameters.cold_junction_compensation_temperature
                    )
                    if parameters.channel_parameters.perform_auto_zero_mode is True:
                        channel.ai_auto_zero_mode = parameters.channel_parameters.auto_zero_mode
            else:
                # Physical channel
                channel = self.task.ai_channels.add_ai_thrmcpl_chan(
                    physical_channel=parameters.channel_name,
                    name_to_assign_to_channel="",
                    min_val=(
                        parameters.channel_parameters.temperature_minimum_value_celsius_degrees
                    ),
                    max_val=(
                        parameters.channel_parameters.temperature_maximum_value_celsius_degrees
                    ),
                    units=(ConstantsForTemperatureMeasurement.INITIAL_AI_TEMPERATURE_UNITS),
                    thermocouple_type=(parameters.channel_parameters.thermocouple_type),
                    cjc_source=parameters.channel_parameters.cold_junction_compensation_source,
                    cjc_val=(parameters.channel_parameters.cold_junction_compensation_temperature),
                    cjc_channel=parameters.channel_parameters.cold_junction_compensation_channel_name,
                )
                self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/time_domain_measurements/__init__.py sha256=a9ef1274a3c5739c8eb0445fabb00f87138b65e52e81d9381b77876a63dbf508 bytes=246 -->
## FILE: src/nipcbatt/pcbatt_library/daq/time_domain_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/time_domain_measurements/__init__.py`
- sha256: `a9ef1274a3c5739c8eb0445fabb00f87138b65e52e81d9381b77876a63dbf508`
- bytes: 246

````python
"""Provides nipcbatt library time domain measurement modules"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (174 > 100 characters) (auto-generated noqa)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/time_domain_measurements/time_domain_constants.py sha256=a9ad65b4b0bbf4e7e068554e2d96ed67fb337ceff278d11d31224f2c8d3391a8 bytes=4947 -->
## FILE: src/nipcbatt/pcbatt_library/daq/time_domain_measurements/time_domain_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/time_domain_measurements/time_domain_constants.py`
- sha256: `a9ad65b4b0bbf4e7e068554e2d96ed67fb337ceff278d11d31224f2c8d3391a8`
- bytes: 4947

````python
""" Constants data types for Time domain Measurements."""

import dataclasses

from nipcbatt.pcbatt_analysis.waveform_analysis.amplitude_and_levels_analysis import (
    AmplitudeAndLevelsProcessingMethod,
)
from nipcbatt.pcbatt_analysis.waveform_analysis.dc_rms_analysis import (
    DcRmsProcessingWindow,
)
from nipcbatt.pcbatt_analysis.waveform_analysis.pulse_analog_analysis import (
    PulseAnalogProcessingExportMode,
    PulseAnalogProcessingPolarity,
    PulseAnalogProcessingReferenceLevelsUnit,
)
from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
    MeasurementOptions,
    SampleClockTimingParameters,
)
from nipcbatt.pcbatt_library.daq.common.voltage_constants import (
    ConstantsForVoltageMeasurement,
)
from nipcbatt.pcbatt_library.daq.common.voltage_data_types import (
    VoltageRangeAndTerminalParameters,
)
from nipcbatt.pcbatt_library.daq.time_domain_measurements.time_domain_data_types import (
    TimeDomainMeasurementConfiguration,
)


@dataclasses.dataclass
class ConstantsForTimeDomainMeasurement:
    """Constants used for Time Domain measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (163 > 100 characters) (auto-generated noqa)

    DEFAULT_DC_RMS_PROCESSING_WINDOW = DcRmsProcessingWindow.HANN
    """Default window that will be used to process DC-RMS in time domain measurement class."""

    DEFAULT_AMPLITUDE_AND_LEVELS_PROCESSING_METHOD = AmplitudeAndLevelsProcessingMethod.AUTO_SELECT
    """Default amplitude and levels processing method that will 
    be used to process peak peak amplitude in time domain measurement class."""

    DEFAULT_AMPLITUDE_AND_LEVELS_PROCESSING_HISTOGRAM_SIZE = 256
    """Default histogram size that will be used to process peak peak 
    amplitude in time domain measurement class."""

    DEFAULT_PULSE_PROCESSING_POLARITY = PulseAnalogProcessingPolarity.HIGH
    """Default pulse processing polarity that will be used to process periodicity 
    of waveforms."""

    DEFAULT_PULSE_PROCESSING_EXPORT_MODE = PulseAnalogProcessingExportMode.ALL
    """Default pulse processing export mode."""

    DEFAULT_PULSE_PROCESSING_REFERENCE_LEVELS_UNIT = (
        PulseAnalogProcessingReferenceLevelsUnit.RELATIVE_PERCENT
    )
    """Default pulse processing reference levels unit that will be used to evaluate periodicity 
    of waveforms."""

    DEFAULT_PULSE_PROCESSING_REFERENCE_LEVEL_HIGH = 95
    """Default pulse processing high reference level that will be used to evaluate periodicity 
    of waveforms."""

    DEFAULT_PULSE_PROCESSING_REFERENCE_LEVEL_MIDDLE = 50
    """Default pulse processing middle reference level that will be used to evaluate periodicity 
    of waveforms."""

    DEFAULT_PULSE_PROCESSING_REFERENCE_LEVEL_LOW = 5
    """Default pulse processing low reference level that will be used to evaluate periodicity 
    of waveforms."""


DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS = VoltageRangeAndTerminalParameters(
    terminal_configuration=ConstantsForVoltageMeasurement.DEFAULT_AI_TERMINAL_CONFIGURATION,
    range_min_volts=ConstantsForVoltageMeasurement.DEFAULT_VOLTAGE_MINIMUM_VALUE_VOLTS,
    range_max_volts=ConstantsForVoltageMeasurement.DEFAULT_VOLTAGE_MAXIMUM_VALUE_VOLTS,
)

DEFAULT_TIME_DOMAIN_MEASUREMENT_OPTIONS = MeasurementOptions(
    execution_option=ConstantsForVoltageMeasurement.DEFAULT_EXECUTION_TYPE,
    measurement_analysis_requirement=ConstantsForVoltageMeasurement.DEFAULT_MEASUREMENT_ANALYSIS_REQUIREMENT,
)

DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS = SampleClockTimingParameters(
    sample_clock_source=ConstantsForVoltageMeasurement.DEFAULT_SAMPLE_CLOCK_SOURCE,
    sampling_rate_hertz=ConstantsForVoltageMeasurement.DEFAULT_SAMPLING_RATE_HERTZ,
    number_of_samples_per_channel=ConstantsForVoltageMeasurement.DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL,
    sample_timing_engine=ConstantsForVoltageMeasurement.DEFAULT_SAMPLE_TIMING_ENGINE,
)

DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS = DigitalStartTriggerParameters(
    trigger_select=ConstantsForVoltageMeasurement.DEFAULT_TRIGGER_TYPE,
    digital_start_trigger_source=ConstantsForVoltageMeasurement.DEFAULT_DIGITAL_START_TRIGGER_SOURCE,
    digital_start_trigger_edge=ConstantsForVoltageMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE,
)

DEFAULT_TIME_DOMAIN_MEASUREMENT_CONFIGURATION = TimeDomainMeasurementConfiguration(
    global_channel_parameters=DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS,
    specific_channels_parameters=[],
    measurement_options=DEFAULT_TIME_DOMAIN_MEASUREMENT_OPTIONS,
    sample_clock_timing_parameters=DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS,
    digital_start_trigger_parameters=DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS,
)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/time_domain_measurements/time_domain_data_types.py sha256=f798480e598c2fb7a69e05181062319136779e5e4aa6515b8f9945cd6795564b bytes=17308 -->
## FILE: src/nipcbatt/pcbatt_library/daq/time_domain_measurements/time_domain_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/time_domain_measurements/time_domain_data_types.py`
- sha256: `f798480e598c2fb7a69e05181062319136779e5e4aa6515b8f9945cd6795564b`
- bytes: 17308

````python
# pylint: disable=C0301
""" Time Domain data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (141 > 100 characters) (auto-generated noqa)

from typing import List

from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    AnalogWaveform,
    DigitalStartTriggerParameters,
    MeasurementOptions,
    SampleClockTimingParameters,
)
from nipcbatt.pcbatt_library.daq.common.voltage_data_types import (
    VoltageMeasurementChannelAndTerminalRangeParameters,
    VoltageRangeAndTerminalParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class TimeDomainMeasurementConfiguration(PCBATestToolkitData):
    """Defines parameters used for configuration of Time domain measurement."""

    def __init__(
        self,
        global_channel_parameters: VoltageRangeAndTerminalParameters,
        specific_channels_parameters: List[VoltageMeasurementChannelAndTerminalRangeParameters],
        measurement_options: MeasurementOptions,
        sample_clock_timing_parameters: SampleClockTimingParameters,
        digital_start_trigger_parameters: DigitalStartTriggerParameters,
    ) -> None:
        """Initializes an instance of
        `TimeDomainMeasurementConfiguration` with specific values.

        Args:
            global_channel_parameters (VoltageRangeAndTerminalParameters):
                The settings of terminal for all channels.
            specific_channels_parameters (List[VoltageMeasurementChannelAndTerminalRangeParameters]):
                The list of instances of `VoltageMeasurementChannelAndTerminalRangeParameters` used to configure channels.
            measurement_options (MeasurementOptions):
                An instance of `MeasurementOptions` that represents the settings of options used for execution.
            sample_clock_timing_parameters (SampleClockTimingParameters):
                An instance of `SampleClockTimingParameters` that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters` that represents the settings of triggers.

        Raises:
            TypeError:
                Raised when `specific_channels_parameters`
                contains objects that are not type of VoltageMeasurementChannelAndTerminalRangeParameters.
            ValueError:
                Raised when `global_channel_parameters` is None,
                `specific_channels_parameters` is None,
                `measurement_options` is None,
                `sample_clock_timing_parameters` is None,
                `digital_start_trigger_parameters` is None,
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (101 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(global_channel_parameters, nameof(global_channel_parameters))
        Guard.is_not_none(specific_channels_parameters, nameof(specific_channels_parameters))
        Guard.all_elements_are_of_same_type(
            input_list=specific_channels_parameters,
            expected_type=VoltageMeasurementChannelAndTerminalRangeParameters,
        )
        Guard.is_not_none(measurement_options, nameof(measurement_options))
        Guard.is_not_none(sample_clock_timing_parameters, nameof(sample_clock_timing_parameters))
        Guard.is_not_none(
            digital_start_trigger_parameters, nameof(digital_start_trigger_parameters)
        )

        self._global_channel_parameters = global_channel_parameters
        self._specific_channels_parameters = specific_channels_parameters
        self._measurement_options = measurement_options
        self._sample_clock_timing_parameters = sample_clock_timing_parameters
        self._digital_start_trigger_parameters = digital_start_trigger_parameters

    @property
    def global_channel_parameters(
        self,
    ) -> VoltageRangeAndTerminalParameters:
        """
        :class:`VoltageRangeAndTerminalParameters`:
            Gets the settings of terminal for all channels."""  # noqa: D205, D209, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (444 > 100 characters) (auto-generated noqa)
        return self._global_channel_parameters

    @property
    def specific_channels_parameters(
        self,
    ) -> List[VoltageMeasurementChannelAndTerminalRangeParameters]:
        """
        :class:`List[VoltageMeasurementChannelAndTerminalRangeParameters]`:
            Gets the list of instances of
            `VoltageMeasurementChannelAndTerminalRangeParameters` used to configure channels.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._specific_channels_parameters

    @property
    def measurement_options(self) -> MeasurementOptions:
        """
        :class:`MeasurementOptions`:
            Gets a `MeasurementOptions` instance
            that represents the settings of options used for execution.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._measurement_options

    @property
    def sample_clock_timing_parameters(self) -> SampleClockTimingParameters:
        """
        :class:`SampleClockTimingParameters`:
            Gets a `SampleClockTimingParameters` instance
            that represents the settings of timing.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._sample_clock_timing_parameters

    @property
    def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters:
        """
        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._digital_start_trigger_parameters


class TimeDomainMeasurementResultData(PCBATestToolkitData):
    """Defines voltage Time domain measurement results obtained after waveform analysis."""

    def __init__(
        self,
        waveforms: List[AnalogWaveform],
        acquisition_duration_seconds: float,
        mean_dc_voltage_values_volts: List[float],
        vpp_amplitudes_volts: List[float],
        voltage_waveforms_frequencies_hertz: List[float],
        voltage_waveforms_periods_seconds: List[float],
        voltage_waveforms_duty_cycles_percent: List[float],
    ) -> None:
        """Initializes an instance of
        `TimeDomainMeasurementResultData` with specific values.

        Args:
            waveforms (List[AnalogWaveform]):
                The list of waveforms acquired from channels defined for measurement and used to compute DC-RMS voltage.
            acquisition_duration_seconds (float):
                The duration of acquisition of samples for each configured channel.
            mean_dc_voltage_values_volts (List[float]):
                The list of mean DC voltages computed for all configured channels, expressed in Volts.
            vpp_amplitudes_volts (List[float]):
                The list of peak to peak voltage amplitudes computed for all configured channels, expressed in Volts.
            voltage_waveforms_frequencies_hertz (List[float]):
                The list of voltage waveforms frequencies computed for all configured channels, expressed in Hertz.
            voltage_waveforms_periods_seconds (List[float]):
                The list of voltage waveforms periods computed for all configured channels, expressed in seconds.
            voltage_waveforms_duty_cycles_percent (List[float]):
                The list of voltage waveforms duty cycles computed for all configured channels, expressed in %.

        Raises:
            TypeError:
                Raised when `waveforms` contains objects that are not `AnalogWaveform`,
                `mean_dc_voltage_values_volts` contains objects that are not `float`,
                `vpp_amplitudes_volts` contains objects that are not `float`,
                `voltage_waveforms_frequencies_hertz` contains objects that are not `float`,
                `voltage_waveforms_periods_seconds` contains objects that are not `float`,
                `voltage_waveforms_duty_cycles_percent` contains objects that are not `float`.
            ValueError:
                Raised when `waveforms` is None or empty.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (120 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(waveforms, nameof(waveforms))
        Guard.is_not_empty(waveforms, nameof(waveforms))

        Guard.is_not_empty(mean_dc_voltage_values_volts, nameof(mean_dc_voltage_values_volts))
        Guard.is_not_none(mean_dc_voltage_values_volts, nameof(mean_dc_voltage_values_volts))

        Guard.is_not_none(vpp_amplitudes_volts, nameof(vpp_amplitudes_volts))
        Guard.is_not_empty(vpp_amplitudes_volts, nameof(vpp_amplitudes_volts))
        
        Guard.is_not_none(voltage_waveforms_frequencies_hertz, nameof(voltage_waveforms_frequencies_hertz))
        
        Guard.is_not_none(voltage_waveforms_periods_seconds, nameof(voltage_waveforms_periods_seconds))
        
        Guard.is_not_none(voltage_waveforms_duty_cycles_percent, nameof(voltage_waveforms_duty_cycles_percent))        

        Guard.all_elements_are_of_same_type(input_list=waveforms, expected_type=AnalogWaveform)
        Guard.all_elements_are_of_same_type(
            input_list=mean_dc_voltage_values_volts, expected_type=float
        )
        Guard.all_elements_are_of_same_type(input_list=vpp_amplitudes_volts, expected_type=float)
        Guard.all_elements_are_of_same_type(
            input_list=voltage_waveforms_frequencies_hertz, expected_type=float
        )
        Guard.all_elements_are_of_same_type(
            input_list=voltage_waveforms_periods_seconds, expected_type=float
        )
        Guard.all_elements_are_of_same_type(
            input_list=voltage_waveforms_duty_cycles_percent, expected_type=float
        )

        self._waveforms = waveforms
        self._acquisition_duration_seconds = acquisition_duration_seconds
        self._mean_dc_voltage_values_volts = mean_dc_voltage_values_volts
        self._vpp_amplitudes_volts = vpp_amplitudes_volts
        self._voltage_waveforms_frequencies_hertz = voltage_waveforms_frequencies_hertz
        self._voltage_waveforms_periods_seconds = voltage_waveforms_periods_seconds
        self._voltage_waveforms_duty_cycles_percent = voltage_waveforms_duty_cycles_percent

    @property
    def waveforms(self) -> List[AnalogWaveform]:
        """
        :class:`List[AnalogWaveform]`:
            Gets the list of waveforms acquired from channels defined
            for measurement and used to compute time domain results.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._waveforms

    @property
    def acquisition_duration_seconds(self) -> float:
        """
        :type:`float`:
            Gets the duration of acquisition of samples for each configured channel.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._acquisition_duration_seconds

    @property
    def mean_dc_voltage_values_volts(self) -> List[float]:
        """
        :class:`List[float]`:
            Gets the list of mean DC voltages computed for all configured channels, expressed in Volts.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (103 > 100 characters) (auto-generated noqa)
        return self._mean_dc_voltage_values_volts

    @property
    def vpp_amplitudes_volts(self) -> List[float]:
        """
        :class:`List[float]`:
            Gets the list of peak to peak voltage amplitudes computed for all configured channels, expressed in Volts.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)
        return self._vpp_amplitudes_volts

    @property
    def voltage_waveforms_frequencies_hertz(self) -> List[float]:
        """
        :class:`List[float]`:
            Gets the list of voltage waveforms frequencies computed for all configured channels, expressed in Hertz.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (116 > 100 characters) (auto-generated noqa)
        return self._voltage_waveforms_frequencies_hertz

    @property
    def voltage_waveforms_periods_seconds(self) -> List[float]:
        """
        :class:`List[float]`:
            Gets the list of voltage waveforms periods computed for all configured channels, expressed in seconds.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (114 > 100 characters) (auto-generated noqa)
        return self._voltage_waveforms_periods_seconds

    @property
    def voltage_waveforms_duty_cycles_percent(self) -> List[float]:
        """
        :class:`List[float]`:
            Gets the list of voltage waveforms duty cycles computed for all configured channels, expressed in %.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (112 > 100 characters) (auto-generated noqa)
        return self._voltage_waveforms_duty_cycles_percent
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/daq/time_domain_measurements/time_domain_measurement.py sha256=3fe3109066d41b5933f40d4eea528d8db645030ba7d7e3c759f1dc16aa9a4f50 bytes=19008 -->
## FILE: src/nipcbatt/pcbatt_library/daq/time_domain_measurements/time_domain_measurement.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/daq/time_domain_measurements/time_domain_measurement.py`
- sha256: `3fe3109066d41b5933f40d4eea528d8db645030ba7d7e3c759f1dc16aa9a4f50`
- bytes: 19008

````python
""" Defines class used for Time domain measurement on PCB points."""

import nidaqmx.constants
import nidaqmx.stream_readers
import numpy
from varname import nameof

from nipcbatt.pcbatt_analysis.analysis_library_exceptions import PCBATTAnalysisException
from nipcbatt.pcbatt_analysis.waveform_analysis.amplitude_and_levels_analysis import (
    LabViewAmplitudeAndLevels,
)
from nipcbatt.pcbatt_analysis.waveform_analysis.dc_rms_analysis import LabViewBasicDcRms
from nipcbatt.pcbatt_analysis.waveform_analysis.pulse_analog_analysis import (
    LabViewPulseAnalogMeasurements,
    PulseAnalogMeasurementPercentLevelsSettings,
    PulseAnalogProcessingReferenceLevels,
)
from nipcbatt.pcbatt_library.common.common_data_types import (
    AnalogWaveform,
    DigitalStartTriggerParameters,
    MeasurementAnalysisRequirement,
    MeasurementData,
    MeasurementExecutionType,
    SampleClockTimingParameters,
    SampleTimingEngine,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.daq.common.voltage_constants import (
    ConstantsForVoltageMeasurement,
)
from nipcbatt.pcbatt_library.daq.common.voltage_data_types import (
    VoltageMeasurementChannelAndTerminalRangeParameters,
    VoltageRangeAndTerminalParameters,
)
from nipcbatt.pcbatt_library.daq.time_domain_measurements.time_domain_constants import (
    ConstantsForTimeDomainMeasurement,
)
from nipcbatt.pcbatt_library.daq.time_domain_measurements.time_domain_data_types import (
    TimeDomainMeasurementConfiguration,
    TimeDomainMeasurementResultData,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_utilities.guard_utilities import Guard
from nipcbatt.pcbatt_utilities.numeric_utilities import invert_value

# Temporary value. To be removed after implementation of Time domain analysis.
DEFAULT_NUMERIC_RESULT_VALUE = 0.0


class TimeDomainMeasurement(BuildingBlockUsingDAQmx):
    """Defines a way that allows you to perform Time domain measurements on PCB points."""

    def initialize(self, analog_input_channel_expression: str):
        """Initializes the measurement with the specific channels

        Args:
            analog_input_channel_expression (str):
                Expression representing the name of a physical channel,
                or a global channel in DAQ System.
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        if self.is_task_initialized:
            return

        if self.contains_only_global_virtual_channels(
            channel_expression=analog_input_channel_expression
        ):
            # If the input channel_expression contains global channel,
            # then add them as global channels
            # and verify if the global channels are configured for current measurement.
            self.add_global_channels(global_channel_expression=analog_input_channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
            self.verify_measurement_type(nidaqmx.constants.UsageTypeAI.VOLTAGE)
        else:
            # Add the channel_expression to analog input current channel of the Daqmx task
            self.task.ai_channels.add_ai_voltage_chan(
                physical_channel=analog_input_channel_expression,
                name_to_assign_to_channel="",
                terminal_config=ConstantsForVoltageMeasurement.INITIAL_AI_TERMINAL_CONFIGURATION,
                min_val=ConstantsForVoltageMeasurement.INITIAL_VOLTAGE_MINIMUM_VALUE_VOLTS,
                max_val=ConstantsForVoltageMeasurement.INITIAL_VOLTAGE_MAXIMUM_VALUE_VOLTS,
                units=ConstantsForVoltageMeasurement.INITIAL_AI_VOLTAGE_UNITS,
            )

    def close(self):
        """Closes measurement procedure and releases internal resources."""
        if not self.is_task_initialized:
            return

        # Stop and close the DAQmx task
        self.task.stop()
        self.task.close()

    def configure_and_measure(self, configuration: TimeDomainMeasurementConfiguration):
        """Configures and/or performs a measurement according to specific configuration parameters.

        Args:
            configuration (TimeDomainMeasurementConfiguration):
            A instance of `TimeDomainMeasurementConfiguration` used to configure the measurement.

        Returns:
            TimeDomainMeasurementResultData | None: An instance of `TimeDomainMeasurementResultData`
              or `None` if no measure was performed.
        """
        if configuration.measurement_options.execution_option in (
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.CONFIGURE_ONLY,
        ):
            self.configure_all_channels(configuration.global_channel_parameters)
            for specific_channel_parameters in configuration.specific_channels_parameters:
                self.configure_specific_channel(specific_channel_parameters)
            self.configure_timing(configuration.sample_clock_timing_parameters)
            self.configure_trigger(configuration.digital_start_trigger_parameters)

        if configuration.measurement_options.execution_option in (
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.MEASURE_ONLY,
        ):
            data = self.acquire_data_for_measurement_analysis()
            return self.analyze_measurement_data(
                data, configuration.measurement_options.measurement_analysis_requirement
            )

        self.task.start()
        return None

    def configure_all_channels(self, parameters: VoltageRangeAndTerminalParameters):
        """Configures all channels used for voltage measurements.

        Args:
            parameters (VoltageRangeAndTerminalParameters):
            An instance of `VoltageRangeAndTerminalParameters` used to configure the channels.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        # for each channel defined in analog input channels list,
        # sets terminal configuration and voltage range.
        for channel in self.task.ai_channels:
            channel.ai_term_cfg = parameters.terminal_configuration
            channel.ai_min = parameters.range_min_volts
            channel.ai_max = parameters.range_max_volts

    def configure_specific_channel(
        self, parameters: VoltageMeasurementChannelAndTerminalRangeParameters
    ):
        """Configures the specific channels used for voltage measurements.

        Args:
            parameters (VoltageMeasurementChannelAndTerminalRangeParameters):
            An instance of `VoltageMeasurementChannelAndTerminalRangeParameters`
            used to configure the channels.

        If the user provides Global Virtual Channel name in Initialize(),
        then he/she has to provide the Virtual channel name in Specific channel parameters as well.

        Similarly, if the user provides Physical channel name in Initialize(),
        then he/she has to provide the Physical channel name in Specific channel parameters.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        if parameters.channel_name in (channel.name for channel in self.task.ai_channels):
            # if the specified channel is present in ai_channel_collection,
            # updates the voltage parameters of the channel
            self.task.ai_channels[
                parameters.channel_name
            ].ai_term_cfg = parameters.channel_parameters.terminal_configuration
            self.task.ai_channels[
                parameters.channel_name
            ].ai_min = parameters.channel_parameters.range_min_volts
            self.task.ai_channels[
                parameters.channel_name
            ].ai_max = parameters.channel_parameters.range_max_volts
        else:
            # otherwise, adds the channel.
            if self.contains_only_global_virtual_channels(
                channel_expression=parameters.channel_name
            ):
                # Global virtual channel
                self.add_global_channels(global_channel_expression=parameters.channel_name)
                self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
                self.verify_measurement_type(nidaqmx.constants.UsageTypeAI.VOLTAGE)
                for channel in self.task.ai_channels:
                    channel.ai_term_cfg = parameters.channel_parameters.terminal_configuration
                    channel.ai_min = parameters.channel_parameters.range_min_volts
                    channel.ai_max = parameters.channel_parameters.range_max_volts
            else:
                # Physical channel
                self.task.ai_channels.add_ai_voltage_chan(
                    physical_channel=parameters.channel_name,
                    terminal_config=parameters.channel_parameters.terminal_configuration,
                    min_val=parameters.channel_parameters.range_min_volts,
                    max_val=parameters.channel_parameters.range_max_volts,
                    units=ConstantsForVoltageMeasurement.INITIAL_AI_VOLTAGE_UNITS,
                )

    def configure_timing(self, parameters: SampleClockTimingParameters) -> None:
        """Configures the timing characteristics used for time domain measurements.

        Args:
            parameters:An instance of `SampleClockTimingParameters` used to configure the timing.
        """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

        self.task.timing.cfg_samp_clk_timing(
            rate=parameters.sampling_rate_hertz,
            sample_mode=nidaqmx.constants.AcquisitionType.FINITE,
            samps_per_chan=parameters.number_of_samples_per_channel,
            source=parameters.sample_clock_source,
        )

        # if the current timing engine setting is Auto
        # then delete the previous timing engine property
        # and let the task revert to the default setting of DAQmx
        # to automatically set the value of the timing engine
        if parameters.sample_timing_engine == SampleTimingEngine.AUTO:
            # Sample timing engine is auto selected
            ...
        else:
            self.task.timing.samp_timing_engine = parameters.sample_timing_engine.value

    def configure_trigger(self, parameters: DigitalStartTriggerParameters) -> None:
        """Configures the characteristics of triggers used for time domain measurements.

        Args:
            parameters (DigitalStartTriggerParameters): An instance of
            `DigitalStartTriggerParameters` used to
        configure the channels.
        """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

        if parameters.trigger_select == StartTriggerType.NO_TRIGGER:
            self.task.triggers.start_trigger.disable_start_trig()
        else:
            self.task.triggers.start_trigger.cfg_dig_edge_start_trig(
                trigger_source=parameters.digital_start_trigger_source,
                trigger_edge=parameters.digital_start_trigger_edge,
            )

    def acquire_data_for_measurement_analysis(self) -> MeasurementData:
        """Acquires Data from DAQ channel for measurement of voltage.

        Returns:
            MeasurementData: An instance of `MeasurementData`
            that specifies the data acquired from DAQ channels.
        """
        # Builds the shape of numpy array (number of channels, number of samples)
        number_of_channels = len(self.task.in_stream.channels_to_read.channel_names)
        number_of_samples_per_channel = self.task.timing.samp_quant_samp_per_chan

        # Build the numpy array.
        samples_array = numpy.zeros(
            shape=(number_of_channels, number_of_samples_per_channel),
            dtype=numpy.float64,
        )

        # Reads data and fill numpy array.
        reader = nidaqmx.stream_readers.AnalogMultiChannelReader(self.task.in_stream)
        reader.read_many_sample(
            data=samples_array,
            number_of_samples_per_channel=number_of_samples_per_channel,
        )

        return MeasurementData(samples_array)

    def analyze_measurement_data(
        self,
        measurement_data: MeasurementData,
        measurement_analysis_requirement: MeasurementAnalysisRequirement,
    ) -> TimeDomainMeasurementResultData:
        """Proceeds to the analysis of Voltages from the measurement.

        Args:
            data (MeasurementData):
                An instance of `MeasurementData`
                that specifies the data acquired from DAQ channels.
            measurement_analysis_requirement (MeasurementAnalysisRequirement):
                An instance of 'MeasurementAnalysisRequirement' that specifies
                whether to Skip Analysis or Proceed to Analysis.

        Returns:
            TimeDomainMeasurementResultData:
                An instance of `TimeDomainMeasurementResultData`
                that specifies the measurement results.
        """
        # Check if sampling rate is 0 and raise error to avoid divide by 0 error.
        Guard.is_greater_than_zero(
            self.task.timing.samp_clk_rate, nameof(self.task.timing.samp_clk_rate)
        )
        delta_time_seconds = invert_value(self.task.timing.samp_clk_rate)

        # Initialization for DcRmsVoltageMeasurementResultData instance creation.
        waveforms = []
        acquisition_duration_seconds = 0.0
        mean_dc_voltage_values_volts = []
        vpp_amplitudes_volts = []
        voltage_waveforms_frequencies_hertz = []
        voltage_waveforms_periods_seconds = []
        voltage_waveforms_duty_cycles_percent = []

        for channel_samples, channel_name in zip(
            measurement_data.samples_per_channel,
            self.task.in_stream.channels_to_read.channel_names,
        ):
            # Creates an instance of AnalogWaveform and add it to waveforms.
            waveforms.append(
                AnalogWaveform(
                    channel_name=channel_name,
                    delta_time_seconds=delta_time_seconds,
                    samples=channel_samples,
                )
            )

            if (
                measurement_analysis_requirement
                == MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
            ):
                acquisition_duration_seconds += delta_time_seconds * len(channel_samples)

                # DC-RMS analysis
                current_channel_samples_dc_rms = LabViewBasicDcRms.process_single_waveform_dc_rms(
                    waveform_samples=channel_samples,
                    waveform_sampling_period_seconds=delta_time_seconds,
                    dc_rms_processing_window=ConstantsForTimeDomainMeasurement.DEFAULT_DC_RMS_PROCESSING_WINDOW,
                )

                mean_dc_voltage_values_volts.append(current_channel_samples_dc_rms.dc_value)

                # Amplitude and levels analysis
                current_channel_samples_amplitude_and_levels = LabViewAmplitudeAndLevels.process_single_waveform_amplitude_and_levels(
                    waveform_samples=channel_samples,
                    waveform_sampling_period_seconds=delta_time_seconds,
                    amplitude_and_levels_processing_method=ConstantsForTimeDomainMeasurement.DEFAULT_AMPLITUDE_AND_LEVELS_PROCESSING_METHOD,
                    histogram_size=ConstantsForTimeDomainMeasurement.DEFAULT_AMPLITUDE_AND_LEVELS_PROCESSING_HISTOGRAM_SIZE,
                )

                vpp_amplitudes_volts.append(current_channel_samples_amplitude_and_levels.amplitude)

                # Periodic waveform analysis (pulse + frequency + periods)
                try:
                    pulse_processing_result = LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements(
                        waveform_samples=channel_samples,
                        waveform_sampling_period_seconds=delta_time_seconds,
                        waveform_t0=0,
                        pulse_number=1,
                        processing_polarity=ConstantsForTimeDomainMeasurement.DEFAULT_PULSE_PROCESSING_POLARITY,
                        reference_levels_unit=ConstantsForTimeDomainMeasurement.DEFAULT_PULSE_PROCESSING_REFERENCE_LEVELS_UNIT,
                        reference_levels=PulseAnalogProcessingReferenceLevels(
                            reference_level_high=ConstantsForTimeDomainMeasurement.DEFAULT_PULSE_PROCESSING_REFERENCE_LEVEL_HIGH,
                            reference_level_middle=ConstantsForTimeDomainMeasurement.DEFAULT_PULSE_PROCESSING_REFERENCE_LEVEL_MIDDLE,
                            reference_level_low=ConstantsForTimeDomainMeasurement.DEFAULT_PULSE_PROCESSING_REFERENCE_LEVEL_LOW,
                        ),
                        export_mode=ConstantsForTimeDomainMeasurement.DEFAULT_PULSE_PROCESSING_EXPORT_MODE,
                        percent_levels_settings=PulseAnalogMeasurementPercentLevelsSettings(
                            amplitude_and_levels_processing_method=ConstantsForTimeDomainMeasurement.DEFAULT_AMPLITUDE_AND_LEVELS_PROCESSING_METHOD,
                            histogram_size=ConstantsForTimeDomainMeasurement.DEFAULT_AMPLITUDE_AND_LEVELS_PROCESSING_HISTOGRAM_SIZE,
                        ),
                    )

                    voltage_waveforms_frequencies_hertz.append(
                        pulse_processing_result.waveform_periodicity_processing_result.frequency
                    )
                    voltage_waveforms_periods_seconds.append(
                        pulse_processing_result.waveform_periodicity_processing_result.period
                    )
                    voltage_waveforms_duty_cycles_percent.append(
                        pulse_processing_result.waveform_periodicity_processing_result.duty_cycle_percent
                    )
                except PCBATTAnalysisException:
                    pass

        return TimeDomainMeasurementResultData(
            waveforms=waveforms,
            acquisition_duration_seconds=acquisition_duration_seconds,
            mean_dc_voltage_values_volts=mean_dc_voltage_values_volts,
            vpp_amplitudes_volts=vpp_amplitudes_volts,
            voltage_waveforms_frequencies_hertz=voltage_waveforms_frequencies_hertz,
            voltage_waveforms_periods_seconds=voltage_waveforms_periods_seconds,
            voltage_waveforms_duty_cycles_percent=voltage_waveforms_duty_cycles_percent,
        )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dcpower/__init__.py sha256=64e2cc0574d3abeb9ca36af35f2df0eea998047de6794ec81c490e763e54b92c bytes=2793 -->
## FILE: src/nipcbatt/pcbatt_library/dcpower/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dcpower/__init__.py`
- sha256: `64e2cc0574d3abeb9ca36af35f2df0eea998047de6794ec81c490e763e54b92c`
- bytes: 2793

````python
# pylint: disable=C0301

"""Contains SMU modules for pcbatt library."""

from nipcbatt.pcbatt_library.dcpower.dc_cv_source_and_measure.dc_cv_source_and_measure import (
    DCVoltageSourceAndMeasure,
)
from nipcbatt.pcbatt_library.dcpower.common.common_data_types import (
    EventSignalToExport,
    ExecutionSettings,
    ExportEvent,
    MeasurementExecutionType,
    SourceTriggerBehavior,
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library.dcpower.dc_cv_source_and_measure.dc_cv_source_and_measure_data_types import (
    DCVoltageSourceAndMeasureParameters,
    DCVoltageSourceAndMeasureResultData,
    VoltageChannelSettings,
)
from nipcbatt.pcbatt_library.dcpower.dc_cv_source_and_measure.dc_cv_source_and_measure_constants import (
    ConstantsForDCVoltageSourceAndMeasure,
    DEFAULT_DC_CV_CHANNEL_SETTINGS,
    DEFAULT_DC_CV_EXECUTION_SETTINGS,
    DEFAULT_DC_CV_SOURCE_AND_MEASURE_PARAMETERS,
    DEFAULT_DC_CV_TIMING_PARAMETERS,
    DEFAULT_DC_CV_TRIGGER_PARAMETERS,
)

# pylint: disable=C0301

"""Contains SMU modules for pcbatt library."""

from nipcbatt.pcbatt_library.dcpower.common.common_data_types import (
    EventSignalToExport,
    ExecutionSettings,
    ExportEvent,
    MeasurementExecutionType,
    SourceTriggerBehavior,
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library.dcpower.dc_cv_source_and_measure.dc_cv_source_and_measure import (
    DCVoltageSourceAndMeasure,
)
from nipcbatt.pcbatt_library.dcpower.dc_cv_source_and_measure.dc_cv_source_and_measure_data_types import (
    DCVoltageSourceAndMeasureParameters,
    DCVoltageSourceAndMeasureResultData,
    VoltageChannelSettings,
)
from nipcbatt.pcbatt_library.dcpower.dc_cv_source_and_measure.dc_cv_source_and_measure_constants import (
    ConstantsForDCVoltageSourceAndMeasure,
    DEFAULT_DC_CV_CHANNEL_SETTINGS,
    DEFAULT_DC_CV_EXECUTION_SETTINGS,
    DEFAULT_DC_CV_SOURCE_AND_MEASURE_PARAMETERS,
    DEFAULT_DC_CV_TIMING_PARAMETERS,
    DEFAULT_DC_CV_TRIGGER_PARAMETERS,
)
from nipcbatt.pcbatt_library.dcpower.dc_cc_source_and_measure.dc_cc_source_and_measure import (
    DCCurrentSourceAndMeasure,
)
from nipcbatt.pcbatt_library.dcpower.dc_cc_source_and_measure.dc_cc_source_and_measure_data_types import (
    CurrentChannelSettings,
    DCCurrentSourceAndMeasureParameters,
    DCCurrentSourceAndMeasureResultData,
)
from nipcbatt.pcbatt_library.dcpower.dc_cc_source_and_measure.dc_cc_source_and_measure_constants import (
    ConstantsForDCCurrentSourceAndMeasure,
    DEFAULT_DC_CC_CHANNEL_SETTINGS,
    DEFAULT_DC_CC_EXECUTION_SETTINGS,
    DEFAULT_DC_CC_SOURCE_AND_MEASURE_PARAMETERS,
    DEFAULT_DC_CC_TIMING_PARAMETERS,
    DEFAULT_DC_CC_TRIGGER_PARAMETERS,
)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dcpower/common/__init__.py sha256=784b6daeeafce666ff6f6ffd48502e8d0ab3c03eadda423c0b5527cb75645d08 bytes=63 -->
## FILE: src/nipcbatt/pcbatt_library/dcpower/common/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dcpower/common/__init__.py`
- sha256: `784b6daeeafce666ff6f6ffd48502e8d0ab3c03eadda423c0b5527cb75645d08`
- bytes: 63

````python
"""Provides common helper functions for DC power operations."""
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dcpower/common/common_data_types.py sha256=a3e08709ddd11c1000d938e699a02f983a4cbd7280b75c4ebb10c9603b4811df bytes=7522 -->
## FILE: src/nipcbatt/pcbatt_library/dcpower/common/common_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dcpower/common/common_data_types.py`
- sha256: `a3e08709ddd11c1000d938e699a02f983a4cbd7280b75c4ebb10c9603b4811df`
- bytes: 7522

````python
"""Common data types shared across DC power source and measure operations."""

from enum import Enum

import nidcpower

from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData


class MeasurementExecutionType(Enum):
    """Defines the execution type for DC source and measure operations."""

    CONFIGURE_SOURCE_AND_MEASURE = "CONFIGURE_SOURCE_AND_MEASURE"
    CONFIGURE_ONLY = "CONFIGURE_ONLY"
    START_SOURCE_ONLY = "START_SOURCE_ONLY"
    MEASURE_ONLY = "MEASURE_ONLY"


class SourceTriggerBehavior(Enum):
    """Defines the source trigger behavior enum."""

    Start_Source_Trigger = "Start_Source_Trigger"
    Disable_Source_Trigger = "Disable_Source_Trigger"


class ExportEvent(Enum):
    """Defines the export event enum."""

    NONE = "NONE"
    Route_Event = "Route_Event"


class EventSignalToExport(Enum):
    """Defines the NI-DCPower event or trigger signal to route to an output terminal enum.

    Each member's value is the corresponding NI-DCPower channel attribute name,
    used with ``setattr`` to configure the output terminal for that signal.
    """

    Source_Complete_Event = "source_complete_event_output_terminal"
    Measure_Complete_Event = "measure_complete_event_output_terminal"
    Sequence_Iteration_Complete_Event = "sequence_iteration_complete_event_output_terminal"
    Sequence_Engine_Done_Event = "sequence_engine_done_event_output_terminal"
    Pulse_Complete_Event = "pulse_complete_event_output_terminal"
    Ready_for_Pulse_Trigger_Event = "ready_for_pulse_trigger_event_output_terminal"
    Start_Trigger = "exported_start_trigger_output_terminal"
    Source_Trigger = "exported_source_trigger_output_terminal"
    Measure_Trigger = "exported_measure_trigger_output_terminal"
    Sequence_Advance_Trigger = "exported_sequence_advance_trigger_output_terminal"
    Pulse_Trigger = "exported_pulse_trigger_output_terminal"


class ExecutionSettings:
    """Defines execution settings for a DC source and measure operation."""

    def __init__(self, execution_type: MeasurementExecutionType, skip_analysis: bool) -> None:
        """Initializes the execution settings.

        Args:
            execution_type (MeasurementExecutionType):
                The execution type having values:
                - ``CONFIGURE_SOURCE_AND_MEASURE``,
                - ``CONFIGURE_ONLY``,
                - ``START_SOURCE_ONLY``, or
                - ``MEASURE_ONLY``.
            skip_analysis (bool):
                When ``True``, post-measurement analysis is skipped.
        """
        self._execution_type = execution_type
        self._skip_analysis = skip_analysis

    @property
    def execution_type(self) -> MeasurementExecutionType:
        """Gets the measurement execution type.

        Returns:
            MeasurementExecutionType: The configured execution type.
        """
        return self._execution_type

    @property
    def skip_analysis(self) -> bool:
        """Gets whether post-measurement analysis is skipped.

        Returns:
            bool: ``True`` if analysis is skipped;
            ``False`` if full analysis is performed.
        """
        return self._skip_analysis


class TimingParameters:
    """Defines timing settings for DC source and measure operations."""

    def __init__(
        self,
        source_delay: float,
        aperture_time: float,
        transient_response: nidcpower.TransientResponse,
    ) -> None:
        """Initializes the timing parameters.

        Args:
            source_delay (float):
                Defines source delay in seconds.
            aperture_time (float):
                Defines aperture time in seconds.
            transient_response (nidcpower.TransientResponse):
                Defines the transient response.
        """
        self._source_delay = source_delay
        self._aperture_time = aperture_time
        self._transient_response = transient_response

    @property
    def source_delay(self) -> float:
        """Gets the source delay.

        Returns:
            float: The source delay in seconds.
        """
        return self._source_delay

    @property
    def aperture_time(self) -> float:
        """Gets the aperture time.

        Returns:
            float: The aperture time in seconds.
        """
        return self._aperture_time

    @property
    def transient_response(self) -> nidcpower.TransientResponse:
        """Gets the transient response setting.

        Returns:
            nidcpower.TransientResponse: The transient response mode.
        """
        return self._transient_response


class TriggerParameters:
    """Defines trigger parameters and event signal routing settings for
    a DC source operation.
    """

    def __init__(
        self,
        source_trigger_behavior: SourceTriggerBehavior,
        start_source_name: str,
        export_event: ExportEvent,
        event_signal_to_export: EventSignalToExport,
        output_event_signal_terminal: str,
    ) -> None:
        """Initializes the trigger parameters.

        Args:
            source_trigger_behavior (SourceTriggerBehavior):
                Configures source trigger behavior.
            start_source_name (str):
                Configures the start source name.
                Ignored when ``source_trigger_behavior`` is ``Disable_Source_Trigger``.
            export_event (ExportEvent):
                Configures export event.
            event_signal_to_export (EventSignalToExport):
                Configures the event signal to export.
                Ignored when ``export_event`` is ``NONE``.
            output_event_signal_terminal (str):
                The output terminal name to which the event signal is routed.
                Ignored when ``export_event`` is ``NONE``.
        """
        self._source_trigger_behavior = source_trigger_behavior
        self._start_source_name = start_source_name
        self._export_event = export_event
        self._event_signal_to_export = event_signal_to_export
        self._output_event_signal_terminal = output_event_signal_terminal

    @property
    def source_trigger_behavior(self) -> SourceTriggerBehavior:
        """Gets the source trigger behavior.

        Returns:
            SourceTriggerBehavior: Configures source trigger behavior.
        """
        return self._source_trigger_behavior

    @property
    def start_source_name(self) -> str:
        """Gets the start source name.

        Returns:
            str: The start source name.
        """
        return self._start_source_name

    @property
    def export_event(self) -> ExportEvent:
        """Gets the export event setting.

        Returns:
            ExportEvent: Configures export event.
        """
        return self._export_event

    @property
    def event_signal_to_export(self) -> EventSignalToExport:
        """Gets the event signal to export.

        Returns:
            EventSignalToExport: Configures the event signal to export.
        """
        return self._event_signal_to_export

    @property
    def output_event_signal_terminal(self) -> str:
        """Gets the output event signal terminal.

        Returns:
            str: Configures the output event signal terminal.
        """
        return self._output_event_signal_terminal
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dcpower/common/helper_function.py sha256=a3a706c995f05bccc38b986361f8ca04c761f232fbbf57e4368b5763cc9996a5 bytes=1797 -->
## FILE: src/nipcbatt/pcbatt_library/dcpower/common/helper_function.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dcpower/common/helper_function.py`
- sha256: `a3a706c995f05bccc38b986361f8ca04c761f232fbbf57e4368b5763cc9996a5`
- bytes: 1797

````python
"""Helper functions for DC power instrument operations."""

import math

_SI_PREFIXES = {
    -24: "y",
    -21: "z",
    -18: "a",
    -15: "f",
    -12: "p",
    -9: "n",
    -6: "u",
    -3: "m",
    0: "",
    3: "k",
    6: "M",
    9: "G",
    12: "T",
    15: "P",
    18: "E",
}


def format_si_fixed_decimals(value: float, unit: str, decimal_places: int = 3) -> str:
    """Formats a numeric value in SI engineering notation with a fixed number of decimal places.

    Scales the value to engineering notation (exponent divisible by 3),
    applies the matching SI prefix, and appends the unit directly without a space.

    Args:
        value (float):
            The numeric value to format.
        unit (str):
            The unit string to append (e.g., ``"A"``, ``"W"``, ``"Ohm"``).
        decimal_places (int):
            Number of digits after the decimal point. Defaults to ``3``.

    Returns:
        str: Formatted string with SI prefix and unit attached.

    Examples:
        ``format_si_fixed_decimals(0.000958775, "A")`` → ``"958.775uA"``

        ``format_si_fixed_decimals(9.696e-5, "W")`` → ``"96.960uW"``

        ``format_si_fixed_decimals(105.477, "Ohm")`` → ``"105.477Ohm"``

        ``format_si_fixed_decimals(0.0, "V")`` → ``"0.000V"``
    """
    if math.isnan(value):
        return f"NaN{unit}"
    if math.isinf(value):
        sign = "+" if value > 0 else "-"
        return f"{sign}Inf{unit}"
    if value == 0.0:
        return f"0.{'0' * decimal_places}{unit}"

    exp = math.floor(math.log10(abs(value)))
    eng_exp = 3 * (exp // 3)
    scaled = value / (10**eng_exp)
    prefix = _SI_PREFIXES.get(eng_exp, f"e{eng_exp}")
    return f"{scaled:.{decimal_places}f}{prefix}{unit}"
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dcpower/dc_cc_source_and_measure/__init__.py sha256=8ae8936a93b59a900bc3b413560aa94e6f20aab5678b9471be4d43e705e6a8e1 bytes=79 -->
## FILE: src/nipcbatt/pcbatt_library/dcpower/dc_cc_source_and_measure/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dcpower/dc_cc_source_and_measure/__init__.py`
- sha256: `8ae8936a93b59a900bc3b413560aa94e6f20aab5678b9471be4d43e705e6a8e1`
- bytes: 79

````python
"""Provides DC current source and measure functionality using SMU and PPS."""
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dcpower/dc_cc_source_and_measure/dc_cc_source_and_measure.py sha256=96c1e8b37025a11e07aab4d681ca8116f15cf8a5e217dde07b944795b415c63a bytes=14760 -->
## FILE: src/nipcbatt/pcbatt_library/dcpower/dc_cc_source_and_measure/dc_cc_source_and_measure.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dcpower/dc_cc_source_and_measure/dc_cc_source_and_measure.py`
- sha256: `96c1e8b37025a11e07aab4d681ca8116f15cf8a5e217dde07b944795b415c63a`
- bytes: 14760

````python
"""Defines class used for DC constant current source and measurement on PCB points."""

import math

import nidcpower

from nipcbatt.pcbatt_library.dcpower.common.helper_function import (
    format_si_fixed_decimals as _si_fixed,
)
from nipcbatt.pcbatt_library.dcpower.dc_cc_source_and_measure.dc_cc_source_and_measure_data_types import (
    CurrentChannelSettings,
    DCCurrentSourceAndMeasureParameters,
    DCCurrentSourceAndMeasureResultData,
    ExportEvent,
    MeasurementExecutionType,
    SourceTriggerBehavior,
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import (
    BuildingBlockUsingNIDCPower,
)

_APERTURE_TIME_UNSUPPORTED_MODELS = frozenset(
    {"NI PXI-4110", "NI PXI-4130", "NI PXI-4131A", "NI PXIe-4154"}
)


class DCCurrentSourceAndMeasure(BuildingBlockUsingNIDCPower):
    """Defines a way that allows you to source DC current and perform measurements on PCB points."""

    def initialize(self, resource_name: str):
        """Initializes the NI DC Power session with the specified resource.

        Opens a new NI-DCPower session, resets the channel, configures
        the source mode to single-point, and sets the output function to DC current.
        Also initializes the ``_execution_settings`` and ``_measurement_results``
        instance dictionaries with ``NaN`` defaults so that state persists across the
        separated ``CONFIGURE_ONLY``, ``START_SOURCE_ONLY``, and ``MEASURE_ONLY`` calls.

        Args:
            resource_name (str): NI-DCPower resource name, e.g. ``"PPS1/0"``.
        """
        self._resource_name = resource_name
        # Open the NI-DCPower session for the given resource
        self._instrument = nidcpower.Session(resource_name=self._resource_name)

        self._channel_name = self.session.get_channel_names(0)[0]
        self.session.channels[self._channel_name].reset()
        self.session.channels[self._channel_name].source_mode = nidcpower.SourceMode.SINGLE_POINT
        self.session.channels[self._channel_name].output_function = (
            nidcpower.OutputFunction.DC_CURRENT
        )
        # Initialize result containers as instance state so values persist across
        # the separated CONFIGURE_ONLY, START_SOURCE_ONLY, and MEASURE_ONLY calls
        self._execution_settings = {
            "Current Level Setting (A)": math.nan,
            "Current Level Range (A)": math.nan,
            "Voltage Limit Setting (V)": math.nan,
            "Voltage Limit Range (V)": math.nan,
            "Aperture Time (Sec)": math.nan,
            "Output Function": nidcpower.OutputFunction.DC_CURRENT.name,
        }
        self._measurement_results = {
            "formatted_measurements": {
                "Voltage Measurement": math.nan,
                "Current Measurement": math.nan,
            },
            "raw_measurements": {
                "Voltage Measurement (V)": math.nan,
                "Current Measurement (A)": math.nan,
            },
            "Compliance/Limit Reached": False,
        }

    def enable_output(self, enable_output: bool) -> None:
        """Enables or disables the output of the channel.

        Args:
            enable_output (bool): True to enable output, False to disable.
        """
        self.session.channels[self._channel_name].output_enabled = enable_output

    def close(self):
        """Resets the channel and closes the NI-DCPower session, releasing all resources."""
        if self.is_session_initialized:
            self.session.channels[self._channel_name].reset()
            self.session.close()
            self._instrument = None

    def configure_and_measure(
        self, configuration: DCCurrentSourceAndMeasureParameters
    ) -> DCCurrentSourceAndMeasureResultData:
        """Configures and/or measures DC current. Behavior is set by ``execution_settings``.

        Behavior is controlled by the ``execution_settings`` :
        To source and measure all in one function call:
        - CONFIGURE_SOURCE_AND_MEASURE

        Or use separated steps calls to execute the same flow but sequentially with:
        - CONFIGURE_ONLY
        - START_SOURCE_ONLY
        - MEASURE_ONLY


        Args:
            configuration (DCCurrentSourceAndMeasureParameters): Channel, timing,
                trigger, and execution settings.

        Returns:
            DCCurrentSourceAndMeasureResultData: Hardware execution settings and
                measurement results held in instance state (``_execution_settings`` and
                ``_measurement_results``). Fields not populated by the current execution
                type retain the values set during ``initialize`` (``NaN`` by default).
        """
        # Apply channel, timing, and trigger settings for CONFIGURE_ONLY or
        # CONFIGURE_SOURCE_AND_MEASURE
        if configuration.execution_settings.execution_type in [
            MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
            MeasurementExecutionType.CONFIGURE_ONLY,
        ]:
            self.configure_range_and_terminal(
                current_channel_settings=configuration.current_channel_settings
            )
            self.session.channels[self._channel_name].source_delay = (
                configuration.timing_parameters.source_delay
            )
            self.session.channels[self._channel_name].sense = (
                configuration.current_channel_settings.sensing
            )
            self.session.channels[self._channel_name].output_enabled = (
                configuration.current_channel_settings.enable_output
            )
            self.configure_timing_settings(
                timing_parameters=configuration.timing_parameters,
                execution_settings=self._execution_settings,
            )
            self.configure_trigger_settings(trigger_parameters=configuration.trigger_parameters)
            self.session.commit()
            self._execution_settings.update(
                {
                    "Current Level Setting (A)": self.session.channels[
                        self._channel_name
                    ].current_level,
                    "Current Level Range (A)": self.session.channels[
                        self._channel_name
                    ].current_level_range,
                    "Voltage Limit Setting (V)": self.session.channels[
                        self._channel_name
                    ].voltage_limit,
                    "Voltage Limit Range (V)": self.session.channels[
                        self._channel_name
                    ].voltage_limit_range,
                    "Device Model": self.session.instrument_model,
                    "Output Function": self.session.channels[
                        self._channel_name
                    ].output_function.name,
                }
            )
            if self.session.instrument_model not in _APERTURE_TIME_UNSUPPORTED_MODELS:
                self._execution_settings.update(
                    {"Aperture Time (Sec)": self.session.channels[self._channel_name].aperture_time}
                )
            # For CONFIGURE_SOURCE_AND_MEASURE — initiate source immediately after commit
            if (
                configuration.execution_settings.execution_type
                == MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE
            ):
                self.session.initiate()
                self.session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE)

        # For START_SOURCE_ONLY, initiate and wait for event completion
        if (
            configuration.execution_settings.execution_type
            == MeasurementExecutionType.START_SOURCE_ONLY
        ):
            self.session.initiate()
            self.session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE)

        # Perform measurement for CONFIGURE_SOURCE_AND_MEASURE or MEASURE_ONLY
        if configuration.execution_settings.execution_type in [
            MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
            MeasurementExecutionType.MEASURE_ONLY,
        ]:
            measured_value = self.session.measure_multiple()
            in_compliance = self.session.query_in_compliance()
            self._measurement_results["Compliance/Limit Reached"] = in_compliance

            if configuration.execution_settings.skip_analysis:
                self._measurement_results["formatted_measurements"] = {
                    "Voltage Measurement": _si_fixed(measured_value[0].voltage, "V"),
                    "Current Measurement": _si_fixed(measured_value[0].current, "A"),
                }
                self._measurement_results["raw_measurements"] = {
                    "Voltage Measurement (V)": float(measured_value[0].voltage),
                    "Current Measurement (A)": float(measured_value[0].current),
                }
                return DCCurrentSourceAndMeasureResultData(
                    execution_settings=self._execution_settings,
                    measurement_results=self._measurement_results,
                )

            # Calculate power from the measured voltage and current
            power = measured_value[0].voltage * measured_value[0].current
            # Calculate Resistance from the measured voltage and current.
            # Avoid division by zero if current is zero.
            resistance = (
                abs(measured_value[0].voltage / measured_value[0].current)
                if measured_value[0].current != 0
                else math.inf
            )
            self._measurement_results["formatted_measurements"].update(
                {
                    "Voltage Measurement": _si_fixed(measured_value[0].voltage, "V"),
                    "Current Measurement": _si_fixed(measured_value[0].current, "A"),
                    "Power": _si_fixed(power, "W"),
                    "Resistance": _si_fixed(resistance, "Ohm"),
                }
            )
            self._measurement_results["raw_measurements"].update(
                {
                    "Voltage Measurement (V)": float(measured_value[0].voltage),
                    "Current Measurement (A)": float(measured_value[0].current),
                    "Power (W)": float(power),
                    "Resistance (Ohm)": float(resistance),
                }
            )

        return DCCurrentSourceAndMeasureResultData(
            execution_settings=self._execution_settings,
            measurement_results=self._measurement_results,
        )

    def configure_range_and_terminal(
        self, current_channel_settings: CurrentChannelSettings
    ) -> None:
        """Configures the current level, voltage limit, and their respective ranges on the channel.

        Args:
            current_channel_settings (CurrentChannelSettings): Channel settings to apply.
        """
        self.session.channels[self._channel_name].current_level = (
            current_channel_settings.current_level
        )
        self.session.channels[self._channel_name].voltage_limit = (
            current_channel_settings.voltage_limit
        )
        self.session.channels[self._channel_name].current_level_range = (
            current_channel_settings.current_level_range
        )
        self.session.channels[self._channel_name].voltage_limit_range = (
            current_channel_settings.voltage_limit_range
        )

    def configure_timing_settings(
        self, timing_parameters: TimingParameters, execution_settings: dict
    ) -> None:
        """Configures aperture time and transient response based on the instrument model.

        PXIe-4112/4113: aperture time only. PXI-4110/4130/4131A/4154: neither supported
        (``Aperture Time (Sec)`` set to ``NaN``). All other models: both supported.

        Args:
            timing_parameters (TimingParameters): Aperture time and transient response to apply.
            execution_settings (dict): Updated in-place; ``NaN`` set for unsupported models.
        """
        match self.session.instrument_model:
            case "NI PXIe-4112" | "NI PXIe-4113":
                self.session.channels[self._channel_name].aperture_time = (
                    timing_parameters.aperture_time
                )
                self.session.channels[self._channel_name].aperture_time_units = (
                    nidcpower.ApertureTimeUnits.SECONDS
                )
            case _ if self.session.instrument_model in _APERTURE_TIME_UNSUPPORTED_MODELS:
                execution_settings.update({"Aperture Time (Sec)": math.nan})
            case _:
                self.session.channels[self._channel_name].aperture_time = (
                    timing_parameters.aperture_time
                )
                self.session.channels[self._channel_name].aperture_time_units = (
                    nidcpower.ApertureTimeUnits.SECONDS
                )
                self.session.channels[self._channel_name].transient_response = (
                    timing_parameters.transient_response
                )

    def configure_trigger_settings(self, trigger_parameters: TriggerParameters) -> None:
        """Configures source trigger input and event signal routing.

        - ``Start_Source_Trigger``: source waits for a digital edge on ``start_source_name``.
        - ``Route_Event``: exports ``event_signal_to_export`` to ``output_event_signal_terminal``.
        - Not supported on all devices (e.g. NI PXI-4110 raises ``DriverError``).

        Args:
            trigger_parameters (TriggerParameters): Trigger and event routing settings.
        """
        # Configure digital-edge source trigger if enabled
        if trigger_parameters.source_trigger_behavior == SourceTriggerBehavior.Start_Source_Trigger:
            self.session.channels[self._channel_name].source_trigger_type = (
                nidcpower.TriggerType.DIGITAL_EDGE
            )
            self.session.channels[self._channel_name].digital_edge_source_trigger_input_terminal = (
                trigger_parameters.start_source_name
            )

        # Route the selected event signal to the specified output terminal
        if trigger_parameters.export_event == ExportEvent.Route_Event:
            setattr(
                self.session.channels[self._channel_name],
                trigger_parameters.event_signal_to_export.value,
                trigger_parameters.output_event_signal_terminal,
            )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dcpower/dc_cc_source_and_measure/dc_cc_source_and_measure_constants.py sha256=a8e1a13eaa24f1aafdc6863c9993e52d25a6baee4bce77bdab62bbcf81b80934 bytes=4248 -->
## FILE: src/nipcbatt/pcbatt_library/dcpower/dc_cc_source_and_measure/dc_cc_source_and_measure_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dcpower/dc_cc_source_and_measure/dc_cc_source_and_measure_constants.py`
- sha256: `a8e1a13eaa24f1aafdc6863c9993e52d25a6baee4bce77bdab62bbcf81b80934`
- bytes: 4248

````python
"""Constants for DC constant current source and measure operations."""

import dataclasses

import nidcpower

from nipcbatt.pcbatt_library.dcpower.dc_cc_source_and_measure.dc_cc_source_and_measure_data_types import (
    CurrentChannelSettings,
    DCCurrentSourceAndMeasureParameters,
    EventSignalToExport,
    ExecutionSettings,
    ExportEvent,
    MeasurementExecutionType,
    SourceTriggerBehavior,
    TimingParameters,
    TriggerParameters,
)


@dataclasses.dataclass
class ConstantsForDCCurrentSourceAndMeasure:
    """Default scalar constants for DC current source and measure operations."""

    DEFAULT_EXECUTION_TYPE = MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE
    DEFAULT_SKIP_ANALYSIS = False

    DEFAULT_CURRENT_LEVEL_AMPERES = 10e-6  # 10 uA — small value to protect hardware
    DEFAULT_CURRENT_LEVEL_RANGE_AMPERES = 0.1  # Must be >= current level
    DEFAULT_VOLTAGE_LIMIT_VOLTS = 1.0  # Small value to protect hardware
    DEFAULT_VOLTAGE_LIMIT_RANGE_VOLTS = 2.0  # Must be >= voltage limit
    DEFAULT_SENSING = nidcpower.Sense.REMOTE  # Not compatible with all devices; use LOCAL if needed
    DEFAULT_ENABLE_OUTPUT = True  # Set False to control output manually via enable_output()

    DEFAULT_SOURCE_DELAY_SECONDS = 0.1  # 100 ms; compatible with all PPS/SMU; use <=20 ms for SMUs
    DEFAULT_APERTURE_TIME_SECONDS = 0.02  # 20 ms for 50 Hz noise rejection; use 16.667 ms for 60 Hz
    DEFAULT_TRANSIENT_RESPONSE = nidcpower.TransientResponse.NORMAL  # Adjust based on DUT behavior

    DEFAULT_SOURCE_TRIGGER_BEHAVIOR = (
        SourceTriggerBehavior.Disable_Source_Trigger
    )  # Source trigger disabled by default
    DEFAULT_START_SOURCE_NAME = (
        ""  # Trigger input terminal, e.g. "/PXI1Slot2/PXI_Trig0"; ignored when trigger is disabled
    )
    DEFAULT_EXPORT_EVENT = (
        ExportEvent.NONE
    )  # Use Route_Event to route triggers and events to specified terminals; use None to disable exporting
    DEFAULT_EVENT_SIGNAL_TO_EXPORT = EventSignalToExport.Source_Complete_Event  # Signal to route
    DEFAULT_OUTPUT_EVENT_SIGNAL_TERMINAL = (
        ""  # Output terminal, e.g. "/PXI1Slot2/PXI_Trig1"; Ignored when using ExportEvent.NONE
    )


DEFAULT_DC_CC_EXECUTION_SETTINGS = ExecutionSettings(
    execution_type=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_EXECUTION_TYPE,
    skip_analysis=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_SKIP_ANALYSIS,
)

DEFAULT_DC_CC_CHANNEL_SETTINGS = CurrentChannelSettings(
    current_level=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_CURRENT_LEVEL_AMPERES,
    current_level_range=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_CURRENT_LEVEL_RANGE_AMPERES,
    voltage_limit=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_VOLTAGE_LIMIT_VOLTS,
    voltage_limit_range=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_VOLTAGE_LIMIT_RANGE_VOLTS,
    sensing=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_SENSING,
    enable_output=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_ENABLE_OUTPUT,
)

DEFAULT_DC_CC_TIMING_PARAMETERS = TimingParameters(
    source_delay=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_SOURCE_DELAY_SECONDS,
    aperture_time=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_APERTURE_TIME_SECONDS,
    transient_response=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_TRANSIENT_RESPONSE,
)

DEFAULT_DC_CC_TRIGGER_PARAMETERS = TriggerParameters(
    source_trigger_behavior=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_SOURCE_TRIGGER_BEHAVIOR,
    start_source_name=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_START_SOURCE_NAME,
    export_event=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_EXPORT_EVENT,
    event_signal_to_export=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_EVENT_SIGNAL_TO_EXPORT,
    output_event_signal_terminal=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_OUTPUT_EVENT_SIGNAL_TERMINAL,
)

DEFAULT_DC_CC_SOURCE_AND_MEASURE_PARAMETERS = DCCurrentSourceAndMeasureParameters(
    current_channel_settings=DEFAULT_DC_CC_CHANNEL_SETTINGS,
    execution_settings=DEFAULT_DC_CC_EXECUTION_SETTINGS,
    timing_parameters=DEFAULT_DC_CC_TIMING_PARAMETERS,
    trigger_parameters=DEFAULT_DC_CC_TRIGGER_PARAMETERS,
)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dcpower/dc_cc_source_and_measure/dc_cc_source_and_measure_data_types.py sha256=80ff7f341030efbdf68754e4b5b399145785c04f7203bad95aeefba7c433e1da bytes=7737 -->
## FILE: src/nipcbatt/pcbatt_library/dcpower/dc_cc_source_and_measure/dc_cc_source_and_measure_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dcpower/dc_cc_source_and_measure/dc_cc_source_and_measure_data_types.py`
- sha256: `80ff7f341030efbdf68754e4b5b399145785c04f7203bad95aeefba7c433e1da`
- bytes: 7737

````python
"""Data types used for DC constant current source and measurement on PCB points."""

import nidcpower

from nipcbatt.pcbatt_library.dcpower.common.common_data_types import (
    EventSignalToExport,
    ExecutionSettings,
    ExportEvent,
    MeasurementExecutionType,
    SourceTriggerBehavior,
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData

__all__ = [
    "EventSignalToExport",
    "ExecutionSettings",
    "ExportEvent",
    "MeasurementExecutionType",
    "SourceTriggerBehavior",
    "TimingParameters",
    "TriggerParameters",
    "CurrentChannelSettings",
    "DCCurrentSourceAndMeasureParameters",
    "DCCurrentSourceAndMeasureResultData",
]


class CurrentChannelSettings:
    """Defines the current level, voltage limit, sensing, and output enable
    settings for a channel.
    """

    def __init__(
        self,
        current_level: float,
        current_level_range: float,
        voltage_limit: float,
        voltage_limit_range: float,
        sensing: nidcpower.Sense,
        enable_output: bool,
    ) -> None:
        """Initializes the current channel settings.

        Args:
            current_level (float):
                The DC current level to source, in amperes.
            current_level_range (float):
                The current level range setting, in amperes.
            voltage_limit (float):
                The voltage limit for the output, in volts.
            voltage_limit_range (float):
                The voltage limit range setting, in volts.
            sensing (nidcpower.Sense):
                The sensing mode (``LOCAL`` or ``REMOTE``) for voltage measurement.
            enable_output (bool):
                Whether the channel output is enabled.
        """
        self._current_level = current_level
        self._current_level_range = current_level_range
        self._voltage_limit = voltage_limit
        self._voltage_limit_range = voltage_limit_range
        self._sensing = sensing
        self._enable_output = enable_output

    @property
    def current_level(self) -> float:
        """Gets the DC current level to source.

        Returns:
            float: The current level in amperes.
        """
        return self._current_level

    @property
    def current_level_range(self) -> float:
        """Gets the current level range.

        Returns:
            float: The current level range in amperes.
        """
        return self._current_level_range

    @property
    def voltage_limit(self) -> float:
        """Gets the voltage limit for the output.

        Returns:
            float: The voltage limit in volts.
        """
        return self._voltage_limit

    @property
    def voltage_limit_range(self) -> float:
        """Gets the voltage limit range.

        Returns:
            float: The voltage limit range in volts.
        """
        return self._voltage_limit_range

    @property
    def sensing(self) -> nidcpower.Sense:
        """Gets the sensing mode.

        Returns:
            nidcpower.Sense: The sensing mode (``LOCAL`` or ``REMOTE``).
        """
        return self._sensing

    @property
    def enable_output(self) -> bool:
        """Gets whether output is enabled.

        Returns:
            bool: ``True`` if the output is enabled, ``False`` otherwise.
        """
        return self._enable_output


class DCCurrentSourceAndMeasureParameters(PCBATestToolkitData):
    """Defines the full configuration for DC constant current source and measure operation."""

    def __init__(
        self,
        current_channel_settings: CurrentChannelSettings,
        execution_settings: ExecutionSettings,
        timing_parameters: TimingParameters,
        trigger_parameters: TriggerParameters,
    ) -> None:
        """Initializes the DC current source and measure parameters.

        Args:
            current_channel_settings (CurrentChannelSettings):
                Current level, voltage limit, sensing mode, and output enable settings.
            execution_settings (ExecutionSettings):
                Execution mode and analysis control settings.
            timing_parameters (TimingParameters):
                Source delay, aperture time, and transient response settings.
            trigger_parameters (TriggerParameters):
                Source trigger input and event signal routing settings.
        """
        self._current_channel_settings = current_channel_settings
        self._execution_settings = execution_settings
        self._timing_parameters = timing_parameters
        self._trigger_parameters = trigger_parameters

    @property
    def current_channel_settings(self) -> CurrentChannelSettings:
        """Gets the current channel settings.

        Returns:
            CurrentChannelSettings: Configures the current level, voltage limit,
            sensing, and output enable settings.
        """
        return self._current_channel_settings

    @property
    def execution_settings(self) -> ExecutionSettings:
        """Gets the execution settings.

        Returns:
            ExecutionSettings: Configures the execution mode and skip analysis settings.
        """
        return self._execution_settings

    @property
    def timing_parameters(self) -> TimingParameters:
        """Gets the timing parameters.

        Returns:
            TimingParameters: Configures the source delay, aperture time, and transient
            response settings.
        """
        return self._timing_parameters

    @property
    def trigger_parameters(self) -> TriggerParameters:
        """Gets the trigger parameters.

        Returns:
            TriggerParameters: Configures the source trigger input and event signal
            routing settings.
        """
        return self._trigger_parameters


class DCCurrentSourceAndMeasureResultData(PCBATestToolkitData):
    """Defines the results obtained from a DC constant current source and measure operation."""

    def __init__(
        self,
        execution_settings: dict,
        measurement_results: dict,
    ) -> None:
        """Initializes the DC current source and measure result data.

        Args:
            execution_settings (dict):
                Dictionary containing the applied hardware settings including current level,
                ranges, aperture time, device model, and output function.
                Fields are ``math.nan`` when configuration is not performed.
            measurement_results (dict):
                Dictionary containing the measured values including voltage, current,
                compliance state, power, and resistance.
                Fields are ``math.nan``/``False`` when measurement is not performed.
        """
        self._execution_settings = execution_settings
        self._measurement_results = measurement_results

    @property
    def execution_settings(self) -> dict:
        """Gets the applied hardware execution settings.

        Returns:
            dict: Applied hardware settings including current level, ranges, aperture time,
                device model, and output function.
        """
        return self._execution_settings

    @property
    def measurement_results(self) -> dict:
        """Gets the measurement results.

        Returns:
            dict: Measured values including voltage, current, compliance state, power,
                and resistance.
        """
        return self._measurement_results
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dcpower/dc_cv_source_and_measure/__init__.py sha256=c7d24bc2ffd26ca722078984426f3cc86e6e74aa2da52cd3d95f64b5d56be1ad bytes=79 -->
## FILE: src/nipcbatt/pcbatt_library/dcpower/dc_cv_source_and_measure/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dcpower/dc_cv_source_and_measure/__init__.py`
- sha256: `c7d24bc2ffd26ca722078984426f3cc86e6e74aa2da52cd3d95f64b5d56be1ad`
- bytes: 79

````python
"""Provides DC voltage source and measure functionality using SMU and PPS."""
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dcpower/dc_cv_source_and_measure/dc_cv_source_and_measure.py sha256=53f2d519df1f27745e7e9fa0ab826cbb57604b4eb20546b30ba8e1c5f2d041ba bytes=14760 -->
## FILE: src/nipcbatt/pcbatt_library/dcpower/dc_cv_source_and_measure/dc_cv_source_and_measure.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dcpower/dc_cv_source_and_measure/dc_cv_source_and_measure.py`
- sha256: `53f2d519df1f27745e7e9fa0ab826cbb57604b4eb20546b30ba8e1c5f2d041ba`
- bytes: 14760

````python
"""Defines class used for DC constant voltage source and measurement on PCB points."""

import math

import nidcpower

from nipcbatt.pcbatt_library.dcpower.common.helper_function import (
    format_si_fixed_decimals as _si_fixed,
)
from nipcbatt.pcbatt_library.dcpower.dc_cv_source_and_measure.dc_cv_source_and_measure_data_types import (
    DCVoltageSourceAndMeasureParameters,
    DCVoltageSourceAndMeasureResultData,
    ExportEvent,
    MeasurementExecutionType,
    SourceTriggerBehavior,
    TimingParameters,
    TriggerParameters,
    VoltageChannelSettings,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import (
    BuildingBlockUsingNIDCPower,
)

_APERTURE_TIME_UNSUPPORTED_MODELS = frozenset(
    {"NI PXI-4110", "NI PXI-4130", "NI PXI-4131A", "NI PXIe-4154"}
)


class DCVoltageSourceAndMeasure(BuildingBlockUsingNIDCPower):
    """Defines a way that allows you to source DC voltage and perform measurements on PCB points."""

    def initialize(self, resource_name: str):
        """Initializes the NI DC Power session with the specified resource.

        Opens a new NI-DCPower session, resets the channel, configures
        the source mode to single-point, and sets the output function to DC voltage.
        Also initializes the ``_execution_settings`` and ``_measurement_results``
        instance dictionaries with ``NaN`` defaults so that state persists across the
        separated ``CONFIGURE_ONLY``, ``START_SOURCE_ONLY``, and ``MEASURE_ONLY`` calls.

        Args:
            resource_name (str): NI-DCPower resource name, e.g. ``"PPS1/0"``.
        """
        self._resource_name = resource_name
        # Open the NI-DCPower session for the given resource
        self._instrument = nidcpower.Session(resource_name=self._resource_name)

        self._channel_name = self.session.get_channel_names(0)[0]
        self.session.channels[self._channel_name].reset()
        self.session.channels[self._channel_name].source_mode = nidcpower.SourceMode.SINGLE_POINT
        self.session.channels[self._channel_name].output_function = (
            nidcpower.OutputFunction.DC_VOLTAGE
        )
        # Initialize result containers as instance state so values persist across
        # the separated CONFIGURE_ONLY, START_SOURCE_ONLY, and MEASURE_ONLY calls
        self._execution_settings = {
            "Voltage Level Setting (V)": math.nan,
            "Voltage Level Range (V)": math.nan,
            "Current Limit Setting (A)": math.nan,
            "Current Limit Range (A)": math.nan,
            "Aperture Time (Sec)": math.nan,
            "Output Function": nidcpower.OutputFunction.DC_VOLTAGE.name,
        }
        self._measurement_results = {
            "formatted_measurements": {
                "Voltage Measurement": math.nan,
                "Current Measurement": math.nan,
            },
            "raw_measurements": {
                "Voltage Measurement (V)": math.nan,
                "Current Measurement (A)": math.nan,
            },
            "Compliance/Limit Reached": False,
        }

    def enable_output(self, enable_output: bool) -> None:
        """Enables or disables the output of the channel.

        Args:
            enable_output (bool): True to enable output, False to disable.
        """
        self.session.channels[self._channel_name].output_enabled = enable_output

    def close(self):
        """Resets the channel and closes the NI-DCPower session, releasing all resources."""
        if self.is_session_initialized:
            self.session.channels[self._channel_name].reset()
            self.session.close()
            self._instrument = None

    def configure_and_measure(
        self, configuration: DCVoltageSourceAndMeasureParameters
    ) -> DCVoltageSourceAndMeasureResultData:
        """Configures and/or measures DC voltage. Behavior is set by ``execution_settings``.

        Behavior is controlled by the ``execution_settings`` :
        To source and measure all in one function call:
        - CONFIGURE_SOURCE_AND_MEASURE

        Or use separated steps calls to execute the same flow but sequentially with:
        - CONFIGURE_ONLY
        - START_SOURCE_ONLY
        - MEASURE_ONLY


        Args:
            configuration (DCVoltageSourceAndMeasureParameters): Channel, timing,
                trigger, and execution settings.

        Returns:
            DCVoltageSourceAndMeasureResultData: Hardware execution settings and
                measurement results held in instance state (``_execution_settings`` and
                ``_measurement_results``). Fields not populated by the current execution
                type retain the values set during ``initialize`` (``NaN`` by default).
        """
        # Apply channel, timing, and trigger settings for CONFIGURE_ONLY or
        # CONFIGURE_SOURCE_AND_MEASURE
        if configuration.execution_settings.execution_type in [
            MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
            MeasurementExecutionType.CONFIGURE_ONLY,
        ]:
            self.configure_range_and_terminal(
                voltage_channel_settings=configuration.voltage_channel_settings
            )
            self.session.channels[self._channel_name].source_delay = (
                configuration.timing_parameters.source_delay
            )
            self.session.channels[self._channel_name].sense = (
                configuration.voltage_channel_settings.sensing
            )
            self.session.channels[self._channel_name].output_enabled = (
                configuration.voltage_channel_settings.enable_output
            )
            self.configure_timing_settings(
                timing_parameters=configuration.timing_parameters,
                execution_settings=self._execution_settings,
            )
            self.configure_trigger_settings(trigger_parameters=configuration.trigger_parameters)
            self.session.commit()
            self._execution_settings.update(
                {
                    "Voltage Level Setting (V)": self.session.channels[
                        self._channel_name
                    ].voltage_level,
                    "Voltage Level Range (V)": self.session.channels[
                        self._channel_name
                    ].voltage_level_range,
                    "Current Limit Setting (A)": self.session.channels[
                        self._channel_name
                    ].current_limit,
                    "Current Limit Range (A)": self.session.channels[
                        self._channel_name
                    ].current_limit_range,
                    "Device Model": self.session.instrument_model,
                    "Output Function": self.session.channels[
                        self._channel_name
                    ].output_function.name,
                }
            )
            if self.session.instrument_model not in _APERTURE_TIME_UNSUPPORTED_MODELS:
                self._execution_settings.update(
                    {"Aperture Time (Sec)": self.session.channels[self._channel_name].aperture_time}
                )
            # For CONFIGURE_SOURCE_AND_MEASURE — initiate source immediately after commit
            if (
                configuration.execution_settings.execution_type
                == MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE
            ):
                self.session.initiate()
                self.session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE)

        # For START_SOURCE_ONLY, initiate and wait for event completion
        if (
            configuration.execution_settings.execution_type
            == MeasurementExecutionType.START_SOURCE_ONLY
        ):
            self.session.initiate()
            self.session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE)

        # Perform measurement for CONFIGURE_SOURCE_AND_MEASURE or MEASURE_ONLY
        if configuration.execution_settings.execution_type in [
            MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
            MeasurementExecutionType.MEASURE_ONLY,
        ]:
            measured_value = self.session.measure_multiple()
            in_compliance = self.session.query_in_compliance()
            self._measurement_results["Compliance/Limit Reached"] = in_compliance

            if configuration.execution_settings.skip_analysis:
                self._measurement_results["formatted_measurements"] = {
                    "Voltage Measurement": _si_fixed(measured_value[0].voltage, "V"),
                    "Current Measurement": _si_fixed(measured_value[0].current, "A"),
                }
                self._measurement_results["raw_measurements"] = {
                    "Voltage Measurement (V)": float(measured_value[0].voltage),
                    "Current Measurement (A)": float(measured_value[0].current),
                }
                return DCVoltageSourceAndMeasureResultData(
                    execution_settings=self._execution_settings,
                    measurement_results=self._measurement_results,
                )

            # Calculate power from the measured voltage and current
            power = measured_value[0].voltage * measured_value[0].current
            # Calculate Resistance from the measured voltage and current.
            # Avoid division by zero if current is zero.
            resistance = (
                abs(measured_value[0].voltage / measured_value[0].current)
                if measured_value[0].current != 0
                else math.inf
            )
            self._measurement_results["formatted_measurements"].update(
                {
                    "Voltage Measurement": _si_fixed(measured_value[0].voltage, "V"),
                    "Current Measurement": _si_fixed(measured_value[0].current, "A"),
                    "Power": _si_fixed(power, "W"),
                    "Resistance": _si_fixed(resistance, "Ohm"),
                }
            )
            self._measurement_results["raw_measurements"].update(
                {
                    "Voltage Measurement (V)": float(measured_value[0].voltage),
                    "Current Measurement (A)": float(measured_value[0].current),
                    "Power (W)": float(power),
                    "Resistance (Ohm)": float(resistance),
                }
            )

        return DCVoltageSourceAndMeasureResultData(
            execution_settings=self._execution_settings,
            measurement_results=self._measurement_results,
        )

    def configure_range_and_terminal(
        self, voltage_channel_settings: VoltageChannelSettings
    ) -> None:
        """Configures the voltage level, current limit, and their respective ranges on the channel.

        Args:
            voltage_channel_settings (VoltageChannelSettings): Channel settings to apply.
        """
        self.session.channels[self._channel_name].voltage_level = (
            voltage_channel_settings.voltage_level
        )
        self.session.channels[self._channel_name].current_limit = (
            voltage_channel_settings.current_limit
        )
        self.session.channels[self._channel_name].voltage_level_range = (
            voltage_channel_settings.voltage_level_range
        )
        self.session.channels[self._channel_name].current_limit_range = (
            voltage_channel_settings.current_limit_range
        )

    def configure_timing_settings(
        self, timing_parameters: TimingParameters, execution_settings: dict
    ) -> None:
        """Configures aperture time and transient response based on the instrument model.

        PXIe-4112/4113: aperture time only. PXI-4110/4130/4131A/4154: neither supported
        (``Aperture Time (Sec)`` set to ``NaN``). All other models: both supported.

        Args:
            timing_parameters (TimingParameters): Aperture time and transient response to apply.
            execution_settings (dict): Updated in-place; ``NaN`` set for unsupported models.
        """
        match self.session.instrument_model:
            case "NI PXIe-4112" | "NI PXIe-4113":
                self.session.channels[self._channel_name].aperture_time = (
                    timing_parameters.aperture_time
                )
                self.session.channels[self._channel_name].aperture_time_units = (
                    nidcpower.ApertureTimeUnits.SECONDS
                )
            case _ if self.session.instrument_model in _APERTURE_TIME_UNSUPPORTED_MODELS:
                execution_settings.update({"Aperture Time (Sec)": math.nan})
            case _:
                self.session.channels[self._channel_name].aperture_time = (
                    timing_parameters.aperture_time
                )
                self.session.channels[self._channel_name].aperture_time_units = (
                    nidcpower.ApertureTimeUnits.SECONDS
                )
                self.session.channels[self._channel_name].transient_response = (
                    timing_parameters.transient_response
                )

    def configure_trigger_settings(self, trigger_parameters: TriggerParameters) -> None:
        """Configures source trigger input and event signal routing.

        - ``Start_Source_Trigger``: source waits for a digital edge on ``start_source_name``.
        - ``Route_Event``: exports ``event_signal_to_export`` to ``output_event_signal_terminal``.
        - Not supported on all devices (e.g. NI PXI-4110 raises ``DriverError``).

        Args:
            trigger_parameters (TriggerParameters): Trigger and event routing settings.
        """
        # Configure digital-edge source trigger if enabled
        if trigger_parameters.source_trigger_behavior == SourceTriggerBehavior.Start_Source_Trigger:
            self.session.channels[self._channel_name].source_trigger_type = (
                nidcpower.TriggerType.DIGITAL_EDGE
            )
            self.session.channels[self._channel_name].digital_edge_source_trigger_input_terminal = (
                trigger_parameters.start_source_name
            )

        # Route the selected event signal to the specified output terminal
        if trigger_parameters.export_event == ExportEvent.Route_Event:
            setattr(
                self.session.channels[self._channel_name],
                trigger_parameters.event_signal_to_export.value,
                trigger_parameters.output_event_signal_terminal,
            )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dcpower/dc_cv_source_and_measure/dc_cv_source_and_measure_constants.py sha256=143a55d3ce43efc82886d254ab87c34bdf240c5bff979abdc91f56f89d95f95a bytes=4247 -->
## FILE: src/nipcbatt/pcbatt_library/dcpower/dc_cv_source_and_measure/dc_cv_source_and_measure_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dcpower/dc_cv_source_and_measure/dc_cv_source_and_measure_constants.py`
- sha256: `143a55d3ce43efc82886d254ab87c34bdf240c5bff979abdc91f56f89d95f95a`
- bytes: 4247

````python
"""Constants for DC constant voltage source and measure operations."""

import dataclasses

import nidcpower

from nipcbatt.pcbatt_library.dcpower.dc_cv_source_and_measure.dc_cv_source_and_measure_data_types import (
    DCVoltageSourceAndMeasureParameters,
    EventSignalToExport,
    ExecutionSettings,
    ExportEvent,
    MeasurementExecutionType,
    SourceTriggerBehavior,
    TimingParameters,
    TriggerParameters,
    VoltageChannelSettings,
)


@dataclasses.dataclass
class ConstantsForDCVoltageSourceAndMeasure:
    """Default scalar constants for DC voltage source and measure operations."""

    DEFAULT_EXECUTION_TYPE = MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE
    DEFAULT_SKIP_ANALYSIS = False

    DEFAULT_VOLTAGE_LEVEL_VOLTS = 1.0  # Small value to protect hardware
    DEFAULT_VOLTAGE_LEVEL_RANGE_VOLTS = 1.0  # Must be >= voltage level
    DEFAULT_CURRENT_LIMIT_AMPERES = 0.01  # 10 mA — small value to protect hardware
    DEFAULT_CURRENT_LIMIT_RANGE_AMPERES = 0.1  # Must be >= current limit
    DEFAULT_SENSING = nidcpower.Sense.REMOTE  # Not compatible with all devices; use LOCAL if needed
    DEFAULT_ENABLE_OUTPUT = True  # Set False to control output manually via enable_output()

    DEFAULT_SOURCE_DELAY_SECONDS = 0.1  # 100 ms; compatible with all PPS/SMU; use <=20 ms for SMUs
    DEFAULT_APERTURE_TIME_SECONDS = 0.02  # 20 ms for 50 Hz noise rejection; use 16.667 ms for 60 Hz
    DEFAULT_TRANSIENT_RESPONSE = nidcpower.TransientResponse.NORMAL  # Adjust based on DUT behavior

    DEFAULT_SOURCE_TRIGGER_BEHAVIOR = (
        SourceTriggerBehavior.Disable_Source_Trigger
    )  # Source trigger disabled by default
    DEFAULT_START_SOURCE_NAME = (
        ""  # Trigger input terminal, e.g. "/PXI1Slot2/PXI_Trig0"; ignored when trigger is disabled
    )
    DEFAULT_EXPORT_EVENT = (
        ExportEvent.NONE
    )  # Use Route_Event to route triggers and events to specified terminals; use None to disable exporting
    DEFAULT_EVENT_SIGNAL_TO_EXPORT = EventSignalToExport.Source_Complete_Event  # Signal to route
    DEFAULT_OUTPUT_EVENT_SIGNAL_TERMINAL = (
        ""  # Output terminal, e.g. "/PXI1Slot2/PXI_Trig1"; Ignored when using ExportEvent.NONE
    )


DEFAULT_DC_CV_EXECUTION_SETTINGS = ExecutionSettings(
    execution_type=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_EXECUTION_TYPE,
    skip_analysis=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_SKIP_ANALYSIS,
)

DEFAULT_DC_CV_CHANNEL_SETTINGS = VoltageChannelSettings(
    voltage_level=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_VOLTAGE_LEVEL_VOLTS,
    voltage_level_range=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_VOLTAGE_LEVEL_RANGE_VOLTS,
    current_limit=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_CURRENT_LIMIT_AMPERES,
    current_limit_range=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_CURRENT_LIMIT_RANGE_AMPERES,
    sensing=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_SENSING,
    enable_output=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_ENABLE_OUTPUT,
)

DEFAULT_DC_CV_TIMING_PARAMETERS = TimingParameters(
    source_delay=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_SOURCE_DELAY_SECONDS,
    aperture_time=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_APERTURE_TIME_SECONDS,
    transient_response=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_TRANSIENT_RESPONSE,
)

DEFAULT_DC_CV_TRIGGER_PARAMETERS = TriggerParameters(
    source_trigger_behavior=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_SOURCE_TRIGGER_BEHAVIOR,
    start_source_name=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_START_SOURCE_NAME,
    export_event=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_EXPORT_EVENT,
    event_signal_to_export=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_EVENT_SIGNAL_TO_EXPORT,
    output_event_signal_terminal=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_OUTPUT_EVENT_SIGNAL_TERMINAL,
)

DEFAULT_DC_CV_SOURCE_AND_MEASURE_PARAMETERS = DCVoltageSourceAndMeasureParameters(
    voltage_channel_settings=DEFAULT_DC_CV_CHANNEL_SETTINGS,
    execution_settings=DEFAULT_DC_CV_EXECUTION_SETTINGS,
    timing_parameters=DEFAULT_DC_CV_TIMING_PARAMETERS,
    trigger_parameters=DEFAULT_DC_CV_TRIGGER_PARAMETERS,
)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dcpower/dc_cv_source_and_measure/dc_cv_source_and_measure_data_types.py sha256=9149e8dac92434c3fae861a8eef15abe03f7c39409079c05e549351fa9e74efc bytes=7737 -->
## FILE: src/nipcbatt/pcbatt_library/dcpower/dc_cv_source_and_measure/dc_cv_source_and_measure_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dcpower/dc_cv_source_and_measure/dc_cv_source_and_measure_data_types.py`
- sha256: `9149e8dac92434c3fae861a8eef15abe03f7c39409079c05e549351fa9e74efc`
- bytes: 7737

````python
"""Data types used for DC constant voltage source and measurement on PCB points."""

import nidcpower

from nipcbatt.pcbatt_library.dcpower.common.common_data_types import (
    EventSignalToExport,
    ExecutionSettings,
    ExportEvent,
    MeasurementExecutionType,
    SourceTriggerBehavior,
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData

__all__ = [
    "EventSignalToExport",
    "ExecutionSettings",
    "ExportEvent",
    "MeasurementExecutionType",
    "SourceTriggerBehavior",
    "TimingParameters",
    "TriggerParameters",
    "VoltageChannelSettings",
    "DCVoltageSourceAndMeasureParameters",
    "DCVoltageSourceAndMeasureResultData",
]


class VoltageChannelSettings:
    """Defines the voltage level, current limit, sensing, and output enable
    settings for a channel.
    """

    def __init__(
        self,
        voltage_level: float,
        voltage_level_range: float,
        current_limit: float,
        current_limit_range: float,
        sensing: nidcpower.Sense,
        enable_output: bool,
    ) -> None:
        """Initializes the voltage channel settings.

        Args:
            voltage_level (float):
                The DC voltage level to source, in volts.
            voltage_level_range (float):
                The voltage level range setting, in volts.
            current_limit (float):
                The current limit for the output, in amperes.
            current_limit_range (float):
                The current limit range setting, in amperes.
            sensing (nidcpower.Sense):
                The sensing mode (``LOCAL`` or ``REMOTE``) for voltage measurement.
            enable_output (bool):
                Whether the channel output is enabled.
        """
        self._voltage_level = voltage_level
        self._voltage_level_range = voltage_level_range
        self._current_limit = current_limit
        self._current_limit_range = current_limit_range
        self._sensing = sensing
        self._enable_output = enable_output

    @property
    def voltage_level(self) -> float:
        """Gets the DC voltage level to source.

        Returns:
            float: The voltage level in volts.
        """
        return self._voltage_level

    @property
    def voltage_level_range(self) -> float:
        """Gets the voltage level range.

        Returns:
            float: The voltage level range in volts.
        """
        return self._voltage_level_range

    @property
    def current_limit(self) -> float:
        """Gets the current limit for the output.

        Returns:
            float: The current limit in amperes.
        """
        return self._current_limit

    @property
    def current_limit_range(self) -> float:
        """Gets the current limit range.

        Returns:
            float: The current limit range in amperes.
        """
        return self._current_limit_range

    @property
    def sensing(self) -> nidcpower.Sense:
        """Gets the sensing mode.

        Returns:
            nidcpower.Sense: The sensing mode (``LOCAL`` or ``REMOTE``).
        """
        return self._sensing

    @property
    def enable_output(self) -> bool:
        """Gets whether output is enabled.

        Returns:
            bool: ``True`` if the output is enabled, ``False`` otherwise.
        """
        return self._enable_output


class DCVoltageSourceAndMeasureParameters(PCBATestToolkitData):
    """Defines the full configuration for DC constant voltage source and measure operation."""

    def __init__(
        self,
        voltage_channel_settings: VoltageChannelSettings,
        execution_settings: ExecutionSettings,
        timing_parameters: TimingParameters,
        trigger_parameters: TriggerParameters,
    ) -> None:
        """Initializes the DC voltage source and measure parameters.

        Args:
            voltage_channel_settings (VoltageChannelSettings):
                Voltage level, current limit, sensing mode, and output enable settings.
            execution_settings (ExecutionSettings):
                Execution mode and analysis control settings.
            timing_parameters (TimingParameters):
                Source delay, aperture time, and transient response settings.
            trigger_parameters (TriggerParameters):
                Source trigger input and event signal routing settings.
        """
        self._voltage_channel_settings = voltage_channel_settings
        self._execution_settings = execution_settings
        self._timing_parameters = timing_parameters
        self._trigger_parameters = trigger_parameters

    @property
    def voltage_channel_settings(self) -> VoltageChannelSettings:
        """Gets the voltage channel settings.

        Returns:
            VoltageChannelSettings: Configures the voltage level, current limit,
            sensing, and output enable settings.
        """
        return self._voltage_channel_settings

    @property
    def execution_settings(self) -> ExecutionSettings:
        """Gets the execution settings.

        Returns:
            ExecutionSettings: Configures the execution mode and skip analysis settings.
        """
        return self._execution_settings

    @property
    def timing_parameters(self) -> TimingParameters:
        """Gets the timing parameters.

        Returns:
            TimingParameters: Configures the source delay, aperture time, and transient
            response settings.
        """
        return self._timing_parameters

    @property
    def trigger_parameters(self) -> TriggerParameters:
        """Gets the trigger parameters.

        Returns:
            TriggerParameters: Configures the source trigger input and event signal
            routing settings.
        """
        return self._trigger_parameters


class DCVoltageSourceAndMeasureResultData(PCBATestToolkitData):
    """Defines the results obtained from a DC constant voltage source and measure operation."""

    def __init__(
        self,
        execution_settings: dict,
        measurement_results: dict,
    ) -> None:
        """Initializes the DC voltage source and measure result data.

        Args:
            execution_settings (dict):
                Dictionary containing the applied hardware settings including voltage level,
                ranges, aperture time, device model, and output function.
                Fields are ``math.nan`` when configuration is not performed.
            measurement_results (dict):
                Dictionary containing the measured values including voltage, current,
                compliance state, power, and resistance.
                Fields are ``math.nan``/``False`` when measurement is not performed.
        """
        self._execution_settings = execution_settings
        self._measurement_results = measurement_results

    @property
    def execution_settings(self) -> dict:
        """Gets the applied hardware execution settings.

        Returns:
            dict: Applied hardware settings including voltage level, ranges, aperture time,
                device model, and output function.
        """
        return self._execution_settings

    @property
    def measurement_results(self) -> dict:
        """Gets the measurement results.

        Returns:
            dict: Measured values including voltage, current, compliance state, power,
                and resistance.
        """
        return self._measurement_results
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/__init__.py sha256=afc980dcbac19278ddf40773b6d4e3e19658d27893a0bfe1247b6810a9c2bcbd bytes=3569 -->
## FILE: src/nipcbatt/pcbatt_library/dmm/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dmm/__init__.py`
- sha256: `afc980dcbac19278ddf40773b6d4e3e19658d27893a0bfe1247b6810a9c2bcbd`
- bytes: 3569

````python
# pylint: disable=C0301

"""Contains DMM modules for pcbatt library."""

from nipcbatt.pcbatt_library.dmm.common.common_data_types import (
    ResolutionInDigits,
    Slope,
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library.dmm.common.constants import (
    ConstantsForDcRmsMeasurements,
)
from nipcbatt.pcbatt_library.dmm.common.helper_functions import (
    FormatMeasurement,
    RangeAndMeasurementFunctionParameters,
)
from nipcbatt.pcbatt_library.dmm.dc_rms_current_measurements.dc_rms_current_constants import (
    DEFAULT_DC_RMS_CURRENT_AC_MIN_FREQUENCY,
    DEFAULT_DC_RMS_CURRENT_EXECUTION_TYPE,
    DEFAULT_DC_RMS_CURRENT_MEASUREMENT_CONFIGURATION,
    DEFAULT_DC_RMS_CURRENT_MEASUREMENT_PARAMETERS,
    DEFAULT_DC_RMS_CURRENT_TIMING_PARAMETERS,
    DEFAULT_DC_RMS_CURRENT_TRIGGER_PARAMETERS,
    ConstantsForDcRmsCurrentMeasurements,
)
from nipcbatt.pcbatt_library.dmm.dc_rms_current_measurements.dc_rms_current_data_types import (
    CurrentRangeAndFunctions,
    DcRmsCurrentMeasurementConfiguration,
    DcRmsCurrentMeasurementFunctionParameters,
    DcRmsCurrentMeasurementResultData,
)
from nipcbatt.pcbatt_library.dmm.dc_rms_current_measurements.dc_rms_current_measurement import (
    DcRmsCurrentMeasurement,
)
from nipcbatt.pcbatt_library.dmm.dc_rms_voltage_measurements.dc_rms_voltage_constants import (
    DEFAULT_DC_RMS_VOLTAGE_AC_MIN_FREQUENCY,
    DEFAULT_DC_RMS_VOLTAGE_EXECUTION_TYPE,
    DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION,
    DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_PARAMETERS,
    DEFAULT_DC_RMS_VOLTAGE_TIMING_PARAMETERS,
    DEFAULT_DC_RMS_VOLTAGE_TRIGGER_PARAMETERS,
    ConstantsForDcRmsVoltageMeasurements,
)
from nipcbatt.pcbatt_library.dmm.dc_rms_voltage_measurements.dc_rms_voltage_data_types import (
    DcRmsVoltageMeasurementConfiguration,
    DcRmsVoltageMeasurementFunctionParameters,
    DcRmsVoltageMeasurementResultData,
    VoltageRangeAndFunctions,
)
from nipcbatt.pcbatt_library.dmm.dc_rms_voltage_measurements.dc_rms_voltage_measurement import (
    DcRmsVoltageMeasurement,
)
from nipcbatt.pcbatt_library.dmm.mixed_measurements.mixed_measurement import (
    MixedMeasurement,
)
from nipcbatt.pcbatt_library.dmm.mixed_measurements.mixed_measurement_constants import (
    DEFAULT_MIXED_AC_MIN_FREQUENCY,
    DEFAULT_MIXED_EXECUTION_TYPE,
    DEFAULT_MIXED_MEASUREMENT_CONFIGURATION,
    DEFAULT_MIXED_MEASUREMENT_PARAMETERS,
    DEFAULT_MIXED_TIMING_PARAMETERS,
    DEFAULT_MIXED_TRIGGER_PARAMETERS,
    ConstantsForMixedMeasurements,
)
from nipcbatt.pcbatt_library.dmm.mixed_measurements.mixed_measurement_data_types import (
    MixedMeasurementConfiguration,
    MixedMeasurementFunctionParameters,
    MixedMeasurementResultData,
    MixedRangeAndFunctions,
)
from nipcbatt.pcbatt_library.dmm.resistance_measurements.resistance_constants import (
    DEFAULT_RESISTANCE_EXECUTION_TYPE,
    DEFAULT_RESISTANCE_MEASUREMENT_CONFIGURATION,
    DEFAULT_RESISTANCE_MEASUREMENT_PARAMETERS,
    DEFAULT_RESISTANCE_TIMING_PARAMETERS,
    DEFAULT_RESISTANCE_TRIGGER_PARAMETERS,
    ConstantsForDcRmsResistanceMeasurements,
)
from nipcbatt.pcbatt_library.dmm.resistance_measurements.resistance_data_types import (
    ResistanceMeasurementConfiguration,
    ResistanceMeasurementFunctionParameters,
    ResistanceMeasurementResultData,
    ResistanceRangeAndFunctions,
)
from nipcbatt.pcbatt_library.dmm.resistance_measurements.resistance_measurement import (
    DcRmsResistanceMeasurement,
)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/common/__init__.py sha256=f186952efc4b1ffa2920cf87d7f09fd029f7ed15af98c45ffd71337754422acb bytes=89 -->
## FILE: src/nipcbatt/pcbatt_library/dmm/common/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dmm/common/__init__.py`
- sha256: `f186952efc4b1ffa2920cf87d7f09fd029f7ed15af98c45ffd71337754422acb`
- bytes: 89

````python
"""Provides common data types, constants, and helper functions for DMM measurements."""
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/common/common_data_types.py sha256=86e03eb8f7b16edd1a15e5ec288779e4add75f854855324dfbd7a641429c1e43 bytes=3441 -->
## FILE: src/nipcbatt/pcbatt_library/dmm/common/common_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dmm/common/common_data_types.py`
- sha256: `86e03eb8f7b16edd1a15e5ec288779e4add75f854855324dfbd7a641429c1e43`
- bytes: 3441

````python
"""Common data types for DMM measurements."""

from enum import Enum

import nidmm


class ResolutionInDigits(Enum):
    """Defines the resolution settings for DMM measurements."""

    DIGITS_3_5 = 3.5
    DIGITS_4_5 = 4.5
    DIGITS_5_5 = 5.5
    DIGITS_6_5 = 6.5
    DIGITS_7_5 = 7.5


class Slope(Enum):
    """Defines the slope settings for DMM measurements."""

    RISING_EDGE = 0
    FALLING_EDGE = 1


class TriggerParameters:
    """Parameters for configuring trigger settings in DMM measurements."""

    def __init__(
        self,
        trigger_source: nidmm.TriggerSource,
        trigger_delay: float,
        slope: Slope,
        enable_trigger: bool,
    ) -> None:
        """Initializes the trigger parameters.

        Args:
            trigger_source (nidmm.TriggerSource):
                The trigger source for the measurement.
            trigger_delay (float):
                The delay in seconds between the trigger and the start of measurement.
            slope (Slope):
                The trigger slope (rising or falling edge).
            enable_trigger (bool):
                Whether triggering is enabled for the measurement.
        """
        self._trigger_source = trigger_source
        self._trigger_delay = trigger_delay
        self._slope = slope
        self._enable_trigger = enable_trigger

    @property
    def trigger_source(self) -> nidmm.TriggerSource:
        """Gets the trigger source.

        Returns:
            nidmm.TriggerSource: The trigger source for the measurement.
        """
        return self._trigger_source

    @property
    def trigger_delay(self) -> float:
        """Gets the trigger delay.

        Returns:
            float: The delay in seconds between trigger and measurement start.
        """
        return self._trigger_delay

    @property
    def trigger_slope(self) -> Slope:
        """Gets the trigger slope.

        Returns:
            Slope: The trigger slope (rising or falling edge).
        """
        return self._slope

    @property
    def enable_trigger(self) -> bool:
        """Gets whether triggering is enabled.

        Returns:
            bool: True if triggering is enabled, False otherwise.
        """
        return self._enable_trigger


class TimingParameters:
    """Parameters for configuring timing settings in DMM measurements."""

    def __init__(
        self,
        aperture_time_seconds: float,
        settle_time_seconds: float,
    ) -> None:
        """Initializes the timing parameters.

        Args:
            aperture_time_seconds (float):
                The aperture time in seconds for the measurement.
            settle_time_seconds (float):
                The settle time in seconds before taking a measurement.
        """
        self._aperture_time_seconds = aperture_time_seconds
        self._settle_time_seconds = settle_time_seconds

    @property
    def aperture_time_seconds(self) -> float:
        """Gets the aperture time.

        Returns:
            float: The aperture time in seconds.
        """
        return self._aperture_time_seconds

    @property
    def settle_time_seconds(self) -> float:
        """Gets the settle time.

        Returns:
            float: The settle time in seconds.
        """
        return self._settle_time_seconds
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/common/constants.py sha256=10bd1b317652a43594ecda857f1bec89c81049a1b3b0739b8bed78e41f0e5d69 bytes=843 -->
## FILE: src/nipcbatt/pcbatt_library/dmm/common/constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dmm/common/constants.py`
- sha256: `10bd1b317652a43594ecda857f1bec89c81049a1b3b0739b8bed78e41f0e5d69`
- bytes: 843

````python
"""Constants for DMM measurements."""

import nidmm

from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
from nipcbatt.pcbatt_library.dmm.common.common_data_types import (
    ResolutionInDigits,
    Slope,
)


class ConstantsForDcRmsMeasurements:
    """Encapsulates the constants for DMM measurements."""

    DEFAULT_POWERLINE_FREQUENCY = 50.0

    DEFAULT_RESOLUTION_IN_DIGITS = ResolutionInDigits.DIGITS_5_5

    DEFAULT_EXECUTION_TYPE = MeasurementExecutionType.CONFIGURE_AND_MEASURE

    DEFAULT_APERTURE_TIME_SECONDS = -1.0
    DEFAULT_SETTLE_TIME_SECONDS = -1.0
    DEFAULT_AC_MIN_FREQUENCY = 40.0

    DEFAULT_TRIGGER_SOURCE = nidmm.TriggerSource.IMMEDIATE
    DEFAULT_TRIGGER_DELAY = -1.0
    DEFAULT_ENABLE_TRIGGER = False
    DEFAULT_TRIGGER_SLOPE = Slope.RISING_EDGE
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/common/helper_functions.py sha256=09725f43b024727872dd66e7ef4b0c0aa389a4f77e05501115335af345795272 bytes=4772 -->
## FILE: src/nipcbatt/pcbatt_library/dmm/common/helper_functions.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dmm/common/helper_functions.py`
- sha256: `09725f43b024727872dd66e7ef4b0c0aa389a4f77e05501115335af345795272`
- bytes: 4772

````python
"""Helper functions and classes for DMM measurement operations."""

import math
from enum import Enum

import nidmm

from nipcbatt.pcbatt_library.common.helper_functions import (
    format_with_si_prefix as _format_with_si_prefix,
)


# Helper Class to extract nidmm.Function and range value from enum
class RangeAndMeasurementFunctionParameters:
    """Extracts measurement function and range from enum values with tuple format."""

    def __init__(self, range_function: Enum):
        """Initialize with an enum that has tuple values (function, range).

        Args:
            range_function: Enum with value as (nidmm.Function, float)
        """
        measurement_function, rangevalue = range_function.value
        self._measurement_function = measurement_function
        self._range_value = rangevalue

    @property
    def measurement_function(self) -> nidmm.Function:
        """Returns the measurement function extracted from the enum.

        Returns:
            nidmm.Function: The measurement function
        """
        return self._measurement_function

    @property
    def range_value(self) -> float:
        """Returns the range value extracted from the enum.

        Returns:
            float: The measurement range value
        """
        return self._range_value


# Helper Class to format measurement results after the readings are fetched from the DMM
class FormatMeasurement:
    """Formats measurement results based on resolution in digits."""

    # Mapping of nidmm.Function to measurement units
    UNIT_MAP = {
        nidmm.Function.DC_VOLTS: "V (dc)",
        nidmm.Function.AC_VOLTS: "V (ac)",
        nidmm.Function.DC_CURRENT: "A (dc)",
        nidmm.Function.AC_CURRENT: "A (ac)",
        nidmm.Function.TWO_WIRE_RES: "Ohm",
        nidmm.Function.FOUR_WIRE_RES: "Ohm",
    }

    @staticmethod
    def format_with_si_prefix(measured_value: float, total_digits: int) -> tuple[str, str]:
        """Formats a value in engineering notation with SI prefix.

        Args:
            measured_value: The numerical value to format
            total_digits: Total number of significant digits to display

        Returns:
            tuple: (formatted_number, si_prefix)
                - formatted_number: The scaled value as a string with appropriate decimal places
                - si_prefix: The SI prefix symbol (e.g., 'k', 'M', 'u', 'm') or exponential notation
        """
        return _format_with_si_prefix(measured_value, total_digits)

    @staticmethod
    def measurement(
        resolution_in_digits: float,
        measured_value: float,
        measurement_function: nidmm.Function = None,
    ) -> dict:
        """Formats the measurement value according to the specified resolution.

        Args:
            resolution_in_digits: Resolution in digits (e.g., 6.5 for 6.5 digit resolution)
            measured_value: The measured value to format
            measurement_function: Optional nidmm.Function to append appropriate unit

        Returns:
            dict: Dictionary containing:
                - 'Formatted_Measurement': Human-readable string with SI prefix and unit
                - 'Measured_Value': Original raw measured value
                - 'Unit': Base unit symbol
        """
        # Handle NaN and infinite values
        if math.isnan(measured_value):
            return {
                "Formatted_Measurement": "NaN",
                "Measured_Value": measured_value,
                "Unit": FormatMeasurement.UNIT_MAP.get(measurement_function, ""),
            }
        if math.isinf(measured_value):
            sign = "+" if measured_value > 0 else "-"

            unit = FormatMeasurement.UNIT_MAP.get(measurement_function, "")
            return {
                "Formatted_Measurement": f"{sign}Inf{unit}",
                "Measured_Value": measured_value,
                "Unit": unit,
            }
        if measured_value == 0:
            unit = FormatMeasurement.UNIT_MAP.get(measurement_function, "")
            return {
                "Formatted_Measurement": f"0{unit}",
                "Measured_Value": measured_value,
                "Unit": unit,
            }

        total_digits = int(resolution_in_digits) + 1
        formatted_number, prefix = FormatMeasurement.format_with_si_prefix(
            measured_value, total_digits
        )
        unit = FormatMeasurement.UNIT_MAP.get(measurement_function, "")
        measurement = f"{formatted_number}{prefix}{unit}"
        return {
            "Formatted_Measurement": measurement,
            "Measured_Value": measured_value,
            "Unit": unit,
        }
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/dc_rms_current_measurements/__init__.py sha256=a23fd4cb06793663165e0a20ade31bf359b81bb2501f8f53e89f40c38976e0ea bytes=72 -->
## FILE: src/nipcbatt/pcbatt_library/dmm/dc_rms_current_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dmm/dc_rms_current_measurements/__init__.py`
- sha256: `a23fd4cb06793663165e0a20ade31bf359b81bb2501f8f53e89f40c38976e0ea`
- bytes: 72

````python
"""Provides DC and RMS current measurement functionality using DMM."""
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/dc_rms_current_measurements/dc_rms_current_constants.py sha256=f29df558182caf6ad2b5a777f052d67d46ff0ee511266fe1715728e0fa9a1448 bytes=2708 -->
## FILE: src/nipcbatt/pcbatt_library/dmm/dc_rms_current_measurements/dc_rms_current_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dmm/dc_rms_current_measurements/dc_rms_current_constants.py`
- sha256: `f29df558182caf6ad2b5a777f052d67d46ff0ee511266fe1715728e0fa9a1448`
- bytes: 2708

````python
"""Constants for DC-RMS Current Measurements."""

import dataclasses

from nipcbatt.pcbatt_library.dmm.common.common_data_types import (
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library.dmm.common.constants import ConstantsForDcRmsMeasurements
from nipcbatt.pcbatt_library.dmm.dc_rms_current_measurements.dc_rms_current_data_types import (
    CurrentRangeAndFunctions,
    DcRmsCurrentMeasurementFunctionParameters,
    DcRmsCurrentMeasurementConfiguration,
)


@dataclasses.dataclass
class ConstantsForDcRmsCurrentMeasurements:
    """Constants used for Current measurement."""

    RANGE_AND_FUNCTION = CurrentRangeAndFunctions.DC_Current_Auto_Range


# Current measurement-specific range/function setting is defined
# in ConstantsForDcRmsCurrentMeasurements.
# Default execution type for current measurements.
DEFAULT_DC_RMS_CURRENT_EXECUTION_TYPE = ConstantsForDcRmsMeasurements.DEFAULT_EXECUTION_TYPE

# Default measurement function parameters including current range/function and resolution in digits.
DEFAULT_DC_RMS_CURRENT_MEASUREMENT_PARAMETERS = DcRmsCurrentMeasurementFunctionParameters(
    measurement_function=ConstantsForDcRmsCurrentMeasurements.RANGE_AND_FUNCTION,
    resolution_in_digits=ConstantsForDcRmsMeasurements.DEFAULT_RESOLUTION_IN_DIGITS,
)

# Default timing parameters including aperture time and settle time.
DEFAULT_DC_RMS_CURRENT_TIMING_PARAMETERS = TimingParameters(
    aperture_time_seconds=ConstantsForDcRmsMeasurements.DEFAULT_APERTURE_TIME_SECONDS,
    settle_time_seconds=ConstantsForDcRmsMeasurements.DEFAULT_SETTLE_TIME_SECONDS,
)

# Default AC minimum frequency
DEFAULT_DC_RMS_CURRENT_AC_MIN_FREQUENCY = ConstantsForDcRmsMeasurements.DEFAULT_AC_MIN_FREQUENCY

# Default trigger parameters including trigger source, trigger delay, and trigger enable setting.
DEFAULT_DC_RMS_CURRENT_TRIGGER_PARAMETERS = TriggerParameters(
    trigger_source=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_SOURCE,
    trigger_delay=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_DELAY,
    slope=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_SLOPE,
    enable_trigger=ConstantsForDcRmsMeasurements.DEFAULT_ENABLE_TRIGGER,
)

# Default DC-RMS current measurement configuration.
DEFAULT_DC_RMS_CURRENT_MEASUREMENT_CONFIGURATION = DcRmsCurrentMeasurementConfiguration(
    execution_type=DEFAULT_DC_RMS_CURRENT_EXECUTION_TYPE,
    measurement_function_parameters=DEFAULT_DC_RMS_CURRENT_MEASUREMENT_PARAMETERS,
    trigger_parameters=DEFAULT_DC_RMS_CURRENT_TRIGGER_PARAMETERS,
    timing_parameters=DEFAULT_DC_RMS_CURRENT_TIMING_PARAMETERS,
    ac_min_frequency=DEFAULT_DC_RMS_CURRENT_AC_MIN_FREQUENCY,
)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/dc_rms_current_measurements/dc_rms_current_data_types.py sha256=459d60ac7e78a74050c45bdf100f03900b9ae39d488fda9d6918e5e7ffab2e5d bytes=7287 -->
## FILE: src/nipcbatt/pcbatt_library/dmm/dc_rms_current_measurements/dc_rms_current_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dmm/dc_rms_current_measurements/dc_rms_current_data_types.py`
- sha256: `459d60ac7e78a74050c45bdf100f03900b9ae39d488fda9d6918e5e7ffab2e5d`
- bytes: 7287

````python
"""DC-RMS current data types."""

from enum import Enum
from typing import Union

import nidmm

from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
from nipcbatt.pcbatt_library.dmm.common.common_data_types import (
    ResolutionInDigits,
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData


class CurrentRangeAndFunctions(Enum):
    """Defines the measurement function and range settings for current measurement."""

    DC_Current_Auto_Range = (nidmm.Function.DC_CURRENT, -1.0)
    DC_1uA = (nidmm.Function.DC_CURRENT, 0.000001)
    DC_10uA = (nidmm.Function.DC_CURRENT, 0.00001)
    DC_100uA = (nidmm.Function.DC_CURRENT, 0.0001)
    DC_1mA = (nidmm.Function.DC_CURRENT, 0.001)
    DC_10mA = (nidmm.Function.DC_CURRENT, 0.01)
    DC_20mA = (nidmm.Function.DC_CURRENT, 0.02)
    DC_100mA = (nidmm.Function.DC_CURRENT, 0.1)
    DC_200mA = (nidmm.Function.DC_CURRENT, 0.2)
    DC_1A = (nidmm.Function.DC_CURRENT, 1)
    DC_3A = (nidmm.Function.DC_CURRENT, 3)

    AC_Current_Auto_Range = (nidmm.Function.AC_CURRENT, -1.0)
    AC_100uA = (nidmm.Function.AC_CURRENT, 0.0001)
    AC_1mA = (nidmm.Function.AC_CURRENT, 0.001)
    AC_10mA = (nidmm.Function.AC_CURRENT, 0.01)
    AC_100mA = (nidmm.Function.AC_CURRENT, 0.1)
    AC_500mA = (nidmm.Function.AC_CURRENT, 0.5)
    AC_1A = (nidmm.Function.AC_CURRENT, 1)
    AC_3A = (nidmm.Function.AC_CURRENT, 3)


class DcRmsCurrentMeasurementFunctionParameters:
    """Defines parameters used for configuration of DC-RMS current measurement."""

    def __init__(
        self,
        measurement_function: CurrentRangeAndFunctions,
        resolution_in_digits: ResolutionInDigits,
    ) -> None:
        """Initializes measurement function parameters.

        Args:
            measurement_function (CurrentRangeAndFunctions):
                The current measurement function and range setting.
            resolution_in_digits (ResolutionInDigits):
                The measurement resolution in digits.
        """
        self._measurement_function = measurement_function
        self._resolution_in_digits = resolution_in_digits

    @property
    def measurement_function(self) -> CurrentRangeAndFunctions:
        """Gets the current measurement function and range setting.

        Returns:
            CurrentRangeAndFunctions: The configured current range and function.
        """
        return self._measurement_function

    @property
    def resolution_in_digits(self) -> ResolutionInDigits:
        """Gets the measurement resolution in digits.

        Returns:
            ResolutionInDigits: The configured resolution setting.
        """
        return self._resolution_in_digits


class DcRmsCurrentMeasurementConfiguration(PCBATestToolkitData):
    """Defines configuration parameters for current DC-RMS measurements."""

    def __init__(
        self,
        execution_type: MeasurementExecutionType,
        measurement_function_parameters: DcRmsCurrentMeasurementFunctionParameters,
        trigger_parameters: TriggerParameters,
        timing_parameters: TimingParameters,
        ac_min_frequency: float,
    ) -> None:
        """Initializes the current measurement configuration.

        Args:
            execution_type (MeasurementExecutionType):
                Specifies whether to configure only, measure only, or both configure and measure.
            measurement_function_parameters (DcRmsCurrentMeasurementFunctionParameters):
                The measurement function settings including current range and resolution.
            trigger_parameters (TriggerParameters):
                Trigger configuration including source, delay, and enable/disable settings.
            timing_parameters (TimingParameters):
                Timing settings including aperture time and settle time.
            ac_min_frequency (float):
                Minimum frequency for AC current measurements in Hz (ignored for DC measurements).
        """
        self._execution_type = execution_type
        self._measurement_function_parameters = measurement_function_parameters
        self._trigger_parameters = trigger_parameters
        self._timing_parameters = timing_parameters
        self._ac_min_frequency = ac_min_frequency

    @property
    def execution_type(self) -> MeasurementExecutionType:
        """Gets the measurement execution type.

        Returns:
            MeasurementExecutionType: The execution mode (configure only, measure only, or both).
        """
        return self._execution_type

    @property
    def trigger_parameters(self) -> TriggerParameters:
        """Gets the trigger configuration parameters.

        Returns:
            TriggerParameters: The trigger settings for the measurement.
        """
        return self._trigger_parameters

    @property
    def measurement_function_parameters(self) -> DcRmsCurrentMeasurementFunctionParameters:
        """Gets the measurement function parameters.

        Returns:
            DcRmsCurrentMeasurementFunctionParameters: The current range, function,
            and resolution settings.
        """
        return self._measurement_function_parameters

    @property
    def timing_parameters(self) -> TimingParameters:
        """Gets the timing configuration parameters.

        Returns:
            TimingParameters: The aperture time and settle time settings.
        """
        return self._timing_parameters

    @property
    def ac_min_frequency(self) -> float:
        """Gets the minimum AC frequency setting.

        Returns:
            float: The minimum frequency for AC current measurements.
        """
        return self._ac_min_frequency


class DcRmsCurrentMeasurementResultData(PCBATestToolkitData):
    """Defines current DC-RMS results obtained from DMM DC-RMS Current Measurement."""

    def __init__(self, dmm_execution_settings: dict, measurement: Union[dict, None]) -> None:
        """Initializes the current measurement result data.

        Args:
            dmm_execution_settings (dict):
                Dictionary containing the DMM configuration used during measurement.
            measurement (dict | None):
                Dictionary containing the measurement results,
                or None if only configuration was performed.
        """
        self._dmm_execution_settings = dmm_execution_settings
        self._measurement = measurement

    @property
    def dmm_execution_settings(self) -> dict:
        """Gets the DMM execution settings used during the measurement.

        Returns:
            dict: Dictionary with labeled keys and values including units for each setting.
        """
        return self._dmm_execution_settings

    @property
    def measurement(self) -> Union[dict, None]:
        """Gets the measurement result data.

        Returns:
            dict | None: Dictionary containing 'Measured_Value', 'Unit', and
                'Formatted_Measurement' keys, or None if only configuration was performed.
        """
        return self._measurement
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/dc_rms_current_measurements/dc_rms_current_measurement.py sha256=d754e3486997c7a4204282d8e318b9c3334fb20cf2684b68878c3fb60e87dc58 bytes=8118 -->
## FILE: src/nipcbatt/pcbatt_library/dmm/dc_rms_current_measurements/dc_rms_current_measurement.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dmm/dc_rms_current_measurements/dc_rms_current_measurement.py`
- sha256: `d754e3486997c7a4204282d8e318b9c3334fb20cf2684b68878c3fb60e87dc58`
- bytes: 8118

````python
"""Defines class used for DC-RMS current measurement on PCB points."""

from typing import Union

import nidmm

from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
from nipcbatt.pcbatt_library.dmm.common.common_data_types import (
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library.dmm.common.helper_functions import (
    FormatMeasurement,
    RangeAndMeasurementFunctionParameters,
)
from nipcbatt.pcbatt_library.dmm.dc_rms_current_measurements.dc_rms_current_data_types import (
    DcRmsCurrentMeasurementConfiguration,
    DcRmsCurrentMeasurementFunctionParameters,
    DcRmsCurrentMeasurementResultData,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import (
    BuildingBlockUsingNIDMM,
)


class DcRmsCurrentMeasurement(BuildingBlockUsingNIDMM):
    """Defines a way that allows you to perform DC-RMS current measurements on PCB points."""

    def initialize(self, dmm_resource_name: str, powerline_frequency: float):
        """Initializes the DMM session with the specific resource name and powerline frequency.

        Args:
            dmm_resource_name (str):
                The resource name of the DMM device to use for measurements.
            powerline_frequency (float):
                The powerline frequency in Hz.
        """
        self._dmm_resource_name = dmm_resource_name
        self._powerline_frequency = powerline_frequency
        self._instrument = nidmm.Session(resource_name=self._dmm_resource_name)
        self.session.powerline_freq = self._powerline_frequency

    def configure_and_measure(
        self, configuration: DcRmsCurrentMeasurementConfiguration
    ) -> Union[DcRmsCurrentMeasurementResultData, None]:
        """Configures and/or performs a measurement according to specific configuration parameters.

        Args:
            configuration (DcRmsCurrentMeasurementConfiguration):
                An instance of `DcRmsCurrentMeasurementConfiguration` used to configure
                the measurement.

        Returns:
            DcRmsCurrentMeasurementResultData | None: An instance of
                `DcRmsCurrentMeasurementResultData` containing DMM execution settings
                and the measured current value, or None if only configuration was performed.
        """
        if configuration.execution_type in (
            MeasurementExecutionType.CONFIGURE_ONLY,
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        ):
            self.configure_measurement_function(
                parameters=configuration.measurement_function_parameters
            )
            self.configure_trigger(parameters=configuration.trigger_parameters)
            self.configure_timing(parameters=configuration.timing_parameters)
            if self.session.function == nidmm.Function.AC_CURRENT:
                self.session.ac_min_freq = configuration.ac_min_frequency

        if configuration.execution_type in (
            MeasurementExecutionType.MEASURE_ONLY,
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        ):
            return self.acquire_measurement(
                configuration.measurement_function_parameters.resolution_in_digits.value
            )
        return None

    def close(self):
        """Closes measurement procedure and releases internal resources."""
        if self.is_session_initialized:
            self.session.close()
            self._instrument = None

    def configure_measurement_function(self, parameters: DcRmsCurrentMeasurementFunctionParameters):
        """Configures the measurement function settings for the DMM.

        Args:
            parameters (DcRmsCurrentMeasurementFunctionParameters):
                An instance of `DcRmsCurrentMeasurementFunctionParameters` containing the
                measurement function type (DC/AC current) and resolution in digits to configure.
        """
        measurement_function_and_range = RangeAndMeasurementFunctionParameters(
            parameters.measurement_function
        )
        resolution_in_digits = parameters.resolution_in_digits.value
        self.session.configure_measurement_digits(
            measurement_function=measurement_function_and_range.measurement_function,
            range=measurement_function_and_range.range_value,
            resolution_digits=resolution_in_digits,
        )

    def configure_trigger(self, parameters: TriggerParameters):
        """Configure the characteristics of triggers used for current measurements.

        Args:
            parameters (TriggerParameters):
                An instance of `TriggerParameters` containing trigger source,
                trigger delay, slope, and enable/disable flag.
        """
        if not parameters.enable_trigger:
            self.session.configure_trigger(
                trigger_source=nidmm.TriggerSource.IMMEDIATE, trigger_delay=-1.0
            )
            return
        self.session.configure_trigger(
            trigger_source=nidmm.TriggerSource[parameters.trigger_source.name],
            trigger_delay=parameters.trigger_delay,
        )
        # Configure Slope only if trigger is enabled
        nidmm_trigger_slope_attribute_id = 1250334
        self.session._set_attribute_vi_int32(
            nidmm_trigger_slope_attribute_id, parameters.trigger_slope.value
        )

    def configure_timing(self, parameters: TimingParameters):
        """Configures the timing characteristics used for current measurements.

        Args:
            parameters (TimingParameters):
                An instance of `TimingParameters` containing aperture time and
                settle time settings.
        """
        self.session.aperture_time = parameters.aperture_time_seconds
        self.session.settle_time = parameters.settle_time_seconds

    def acquire_measurement(self, resolution_in_digits: float) -> DcRmsCurrentMeasurementResultData:
        """Acquires and formats the measurement result data.

        Args:
            resolution_in_digits (float):
                The resolution in digits used for formatting the measured value.

        Returns:
            DcRmsCurrentMeasurementResultData:
                An instance of `DcRmsCurrentMeasurementResultData` containing:
                - dmm_execution_settings: Dictionary with keys 'Function', 'Range',
                  'Digits_Resolution', 'Aperture_Time(s)', 'Settle_Time(s)',
                  'Minimum_Frequency(Hz)', 'Absolute_Resolution',
                  'Input_Resistance(Ohm)', and 'Auto_Range_Value'
                - measurement: Dictionary with keys 'Measured_Value', 'Unit', and
                  'Formatted_Measurement'
        """
        measured_value = self.session.read()
        measurement = FormatMeasurement.measurement(
            resolution_in_digits=resolution_in_digits,
            measured_value=measured_value,
            measurement_function=self.session.function,
        )
        aperture_time = "{}{}".format(
            *FormatMeasurement.format_with_si_prefix(self.session.aperture_time, 3)
        )
        settle_time = "{}{}".format(
            *FormatMeasurement.format_with_si_prefix(self.session.settle_time.total_seconds(), 3)
        )
        dmm_execution_settings = {
            "Function": self.session.function.name,
            "Range": self.session.range,
            "Digits_Resolution": self.session.resolution_digits,
            "Aperture_Time(s)": aperture_time,
            "Settle_Time(s)": settle_time,
            "Minimum_Frequency(Hz)": self.session.ac_min_freq,
            "Absolute_Resolution": self.session.resolution_absolute,
            "Input_Resistance(Ohm)": self.session.input_resistance,
            "Auto_Range_Value": self.session.auto_range_value,
        }
        return DcRmsCurrentMeasurementResultData(
            dmm_execution_settings=dmm_execution_settings, measurement=measurement
        )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/dc_rms_voltage_measurements/__init__.py sha256=df02581bb3b265e481111083868ad8d2b394dab4ea5de7ceb90b0ee896e1815d bytes=72 -->
## FILE: src/nipcbatt/pcbatt_library/dmm/dc_rms_voltage_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dmm/dc_rms_voltage_measurements/__init__.py`
- sha256: `df02581bb3b265e481111083868ad8d2b394dab4ea5de7ceb90b0ee896e1815d`
- bytes: 72

````python
"""Provides DC and RMS voltage measurement functionality using DMM."""
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/dc_rms_voltage_measurements/dc_rms_voltage_constants.py sha256=8e1642ef806b85db2ade53fc5cbd1eff3712d98cf126a8d6f6ce64813cdf82c5 bytes=2707 -->
## FILE: src/nipcbatt/pcbatt_library/dmm/dc_rms_voltage_measurements/dc_rms_voltage_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dmm/dc_rms_voltage_measurements/dc_rms_voltage_constants.py`
- sha256: `8e1642ef806b85db2ade53fc5cbd1eff3712d98cf126a8d6f6ce64813cdf82c5`
- bytes: 2707

````python
"""Constants for DC-RMS Voltage Measurements."""

import dataclasses

from nipcbatt.pcbatt_library.dmm.common.common_data_types import (
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library.dmm.common.constants import ConstantsForDcRmsMeasurements
from nipcbatt.pcbatt_library.dmm.dc_rms_voltage_measurements.dc_rms_voltage_data_types import (
    DcRmsVoltageMeasurementConfiguration,
    DcRmsVoltageMeasurementFunctionParameters,
    VoltageRangeAndFunctions,
)


@dataclasses.dataclass
class ConstantsForDcRmsVoltageMeasurements:
    """Constants used for Voltage measurement."""

    RANGE_AND_FUNCTION = VoltageRangeAndFunctions.DC_Voltage_Auto_Range


# Voltage measurement-specific range/function setting is defined
# in ConstantsForDcRmsVoltageMeasurements.
# Default execution type for voltage measurements.
DEFAULT_DC_RMS_VOLTAGE_EXECUTION_TYPE = ConstantsForDcRmsMeasurements.DEFAULT_EXECUTION_TYPE

# Default measurement function parameter including voltage range/function and resolution in digits.
DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_PARAMETERS = DcRmsVoltageMeasurementFunctionParameters(
    measurement_function=ConstantsForDcRmsVoltageMeasurements.RANGE_AND_FUNCTION,
    resolution_in_digits=ConstantsForDcRmsMeasurements.DEFAULT_RESOLUTION_IN_DIGITS,
)

# Default timing parameters including aperture time and settle time.
DEFAULT_DC_RMS_VOLTAGE_TIMING_PARAMETERS = TimingParameters(
    aperture_time_seconds=ConstantsForDcRmsMeasurements.DEFAULT_APERTURE_TIME_SECONDS,
    settle_time_seconds=ConstantsForDcRmsMeasurements.DEFAULT_SETTLE_TIME_SECONDS,
)

# Default AC minimum frequency
DEFAULT_DC_RMS_VOLTAGE_AC_MIN_FREQUENCY = ConstantsForDcRmsMeasurements.DEFAULT_AC_MIN_FREQUENCY

# Default trigger parameters including trigger source, trigger delay, and trigger enable setting.
DEFAULT_DC_RMS_VOLTAGE_TRIGGER_PARAMETERS = TriggerParameters(
    trigger_source=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_SOURCE,
    trigger_delay=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_DELAY,
    slope=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_SLOPE,
    enable_trigger=ConstantsForDcRmsMeasurements.DEFAULT_ENABLE_TRIGGER,
)

# Default DC-RMS voltage measurement configuration.
DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION = DcRmsVoltageMeasurementConfiguration(
    execution_type=DEFAULT_DC_RMS_VOLTAGE_EXECUTION_TYPE,
    measurement_function_parameters=DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_PARAMETERS,
    trigger_parameters=DEFAULT_DC_RMS_VOLTAGE_TRIGGER_PARAMETERS,
    timing_parameters=DEFAULT_DC_RMS_VOLTAGE_TIMING_PARAMETERS,
    ac_min_frequency=DEFAULT_DC_RMS_VOLTAGE_AC_MIN_FREQUENCY,
)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/dc_rms_voltage_measurements/dc_rms_voltage_data_types.py sha256=3e2b09e81217ee12ccd31d7b946476ac52cae38c3587b4e9d817930940e12be0 bytes=7063 -->
## FILE: src/nipcbatt/pcbatt_library/dmm/dc_rms_voltage_measurements/dc_rms_voltage_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dmm/dc_rms_voltage_measurements/dc_rms_voltage_data_types.py`
- sha256: `3e2b09e81217ee12ccd31d7b946476ac52cae38c3587b4e9d817930940e12be0`
- bytes: 7063

````python
"""DC-RMS voltage data types."""

from enum import Enum
from typing import Union

import nidmm

from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
from nipcbatt.pcbatt_library.dmm.common.common_data_types import (
    ResolutionInDigits,
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData


class VoltageRangeAndFunctions(Enum):
    """Defines the measurement function and range settings for voltage measurement."""

    DC_Voltage_Auto_Range = (nidmm.Function.DC_VOLTS, -1.0)
    DC_100mV = (nidmm.Function.DC_VOLTS, 0.1)
    DC_1V = (nidmm.Function.DC_VOLTS, 1)
    DC_10V = (nidmm.Function.DC_VOLTS, 10)
    DC_100V = (nidmm.Function.DC_VOLTS, 100)
    DC_300V = (nidmm.Function.DC_VOLTS, 300)

    AC_Voltage_Auto_Range = (nidmm.Function.AC_VOLTS, -1.0)
    AC_50mV = (nidmm.Function.AC_VOLTS, 0.05)
    AC_200mV = (nidmm.Function.AC_VOLTS, 0.2)
    AC_500mV = (nidmm.Function.AC_VOLTS, 0.5)
    AC_2V = (nidmm.Function.AC_VOLTS, 2)
    AC_5V = (nidmm.Function.AC_VOLTS, 5)
    AC_20V = (nidmm.Function.AC_VOLTS, 20)
    AC_50V = (nidmm.Function.AC_VOLTS, 50)
    AC_300V = (nidmm.Function.AC_VOLTS, 300)


class DcRmsVoltageMeasurementFunctionParameters(PCBATestToolkitData):
    """Defines parameters used for configuration of DC-RMS voltage measurement."""

    def __init__(
        self,
        measurement_function: VoltageRangeAndFunctions,
        resolution_in_digits: ResolutionInDigits,
    ) -> None:
        """Initializes measurement function parameters.

        Args:
            measurement_function (VoltageRangeAndFunctions):
                The voltage measurement function and range setting.
            resolution_in_digits (ResolutionInDigits):
                The measurement resolution in digits.
        """
        self._measurement_function = measurement_function
        self._resolution_in_digits = resolution_in_digits

    @property
    def measurement_function(self) -> VoltageRangeAndFunctions:
        """Gets the voltage measurement function and range setting.

        Returns:
            VoltageRangeAndFunctions: The configured voltage range and function.
        """
        return self._measurement_function

    @property
    def resolution_in_digits(self) -> ResolutionInDigits:
        """Gets the measurement resolution in digits.

        Returns:
            ResolutionInDigits: The configured resolution setting.
        """
        return self._resolution_in_digits


class DcRmsVoltageMeasurementConfiguration(PCBATestToolkitData):
    """Defines configuration parameters for voltage DC-RMS measurements."""

    def __init__(
        self,
        execution_type: MeasurementExecutionType,
        measurement_function_parameters: DcRmsVoltageMeasurementFunctionParameters,
        trigger_parameters: TriggerParameters,
        timing_parameters: TimingParameters,
        ac_min_frequency: float,
    ) -> None:
        """Initializes the voltage measurement configuration.

        Args:
            execution_type (MeasurementExecutionType):
                Specifies whether to configure only, measure only, or both configure and measure.
            measurement_function_parameters (DcRmsVoltageMeasurementFunctionParameters):
                The measurement function settings including voltage range and resolution.
            trigger_parameters (TriggerParameters):
                Trigger configuration including source, delay, and enable/disable settings.
            timing_parameters (TimingParameters):
                Timing settings including aperture time and settle time.
            ac_min_frequency (float):
                Minimum frequency for AC voltage measurements in Hz (ignored for DC measurements).
        """
        self._execution_type = execution_type
        self._measurement_function_parameters = measurement_function_parameters
        self._trigger_parameters = trigger_parameters
        self._timing_parameters = timing_parameters
        self._ac_min_frequency = ac_min_frequency

    @property
    def execution_type(self) -> MeasurementExecutionType:
        """Gets the measurement execution type.

        Returns:
            MeasurementExecutionType: The execution mode (configure only, measure only, or both).
        """
        return self._execution_type

    @property
    def trigger_parameters(self) -> TriggerParameters:
        """Gets the trigger configuration parameters.

        Returns:
            TriggerParameters: The trigger settings for the measurement.
        """
        return self._trigger_parameters

    @property
    def measurement_function_parameters(self) -> DcRmsVoltageMeasurementFunctionParameters:
        """Gets the measurement function parameters.

        Returns:
            DcRmsVoltageMeasurementFunctionParameters: The voltage range, function,
            and resolution settings.
        """
        return self._measurement_function_parameters

    @property
    def timing_parameters(self) -> TimingParameters:
        """Gets the timing configuration parameters.

        Returns:
            TimingParameters: The aperture time and settle time settings.
        """
        return self._timing_parameters

    @property
    def ac_min_frequency(self) -> float:
        """Gets the minimum AC frequency setting.

        Returns:
            float: The minimum frequency for AC voltage measurements.
        """
        return self._ac_min_frequency


class DcRmsVoltageMeasurementResultData(PCBATestToolkitData):
    """Defines voltage DC-RMS results obtained from DMM DC-RMS Voltage Measurement."""

    def __init__(self, dmm_execution_settings: dict, measurement: Union[dict, None]) -> None:
        """Initializes the voltage measurement result data.

        Args:
            dmm_execution_settings (dict):
                Dictionary containing the DMM configuration used during measurement.
            measurement (dict | None):
                Dictionary containing the measurement results,
                or None if only configuration was performed.
        """
        self._dmm_execution_settings = dmm_execution_settings
        self._measurement = measurement

    @property
    def dmm_execution_settings(self) -> dict:
        """Gets the DMM execution settings used during the measurement.

        Returns:
            dict: Dictionary with labeled keys and values including units for each setting.
        """
        return self._dmm_execution_settings

    @property
    def measurement(self) -> Union[dict, None]:
        """Gets the measurement result data.

        Returns:
            dict | None: Dictionary containing 'Measured_Value', 'Unit', and
                'Formatted_Measurement' keys, or None if only configuration was performed.
        """
        return self._measurement
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/dc_rms_voltage_measurements/dc_rms_voltage_measurement.py sha256=c80480ebafee699885a7e913969c976e5c867fec6f7c1f05ccca194eaafdc1fe bytes=8116 -->
## FILE: src/nipcbatt/pcbatt_library/dmm/dc_rms_voltage_measurements/dc_rms_voltage_measurement.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dmm/dc_rms_voltage_measurements/dc_rms_voltage_measurement.py`
- sha256: `c80480ebafee699885a7e913969c976e5c867fec6f7c1f05ccca194eaafdc1fe`
- bytes: 8116

````python
"""Defines class used for DC-RMS Voltage measurement on PCB points."""

from typing import Union

import nidmm

from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
from nipcbatt.pcbatt_library.dmm.common.common_data_types import (
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library.dmm.common.helper_functions import (
    FormatMeasurement,
    RangeAndMeasurementFunctionParameters,
)
from nipcbatt.pcbatt_library.dmm.dc_rms_voltage_measurements.dc_rms_voltage_data_types import (
    DcRmsVoltageMeasurementConfiguration,
    DcRmsVoltageMeasurementFunctionParameters,
    DcRmsVoltageMeasurementResultData,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import (
    BuildingBlockUsingNIDMM,
)


class DcRmsVoltageMeasurement(BuildingBlockUsingNIDMM):
    """Defines a way that allows you to perform DC-RMS voltage measurements on PCB points."""

    def initialize(self, dmm_resource_name: str, powerline_frequency: float):
        """Initializes the DMM session with the specific resource name and powerline frequency.

        Args:
            dmm_resource_name (str):
                The resource name of the DMM device to use for measurements.
            powerline_frequency (float):
                The powerline frequency in Hz.
        """
        self._dmm_resource_name = dmm_resource_name
        self._powerline_frequency = powerline_frequency
        self._instrument = nidmm.Session(resource_name=self._dmm_resource_name)
        self.session.powerline_freq = self._powerline_frequency

    def configure_and_measure(
        self, configuration: DcRmsVoltageMeasurementConfiguration
    ) -> Union[DcRmsVoltageMeasurementResultData, None]:
        """Configures and/or performs a measurement according to specific configuration parameters.

        Args:
            configuration (DcRmsVoltageMeasurementConfiguration):
                An instance of `DcRmsVoltageMeasurementConfiguration` used to configure
                the measurement.

        Returns:
            DcRmsVoltageMeasurementResultData | None: An instance of
                `DcRmsVoltageMeasurementResultData` containing DMM execution settings
                and the measured voltage value, or None if only configuration was performed.
        """
        if configuration.execution_type in (
            MeasurementExecutionType.CONFIGURE_ONLY,
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        ):
            self.configure_measurement_function(
                parameters=configuration.measurement_function_parameters
            )
            self.configure_trigger(parameters=configuration.trigger_parameters)
            self.configure_timing(parameters=configuration.timing_parameters)
            if self.session.function == nidmm.Function.AC_VOLTS:
                self.session.ac_min_freq = configuration.ac_min_frequency

        if configuration.execution_type in (
            MeasurementExecutionType.MEASURE_ONLY,
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        ):
            return self.acquire_measurement(
                configuration.measurement_function_parameters.resolution_in_digits.value
            )
        return None

    def close(self):
        """Closes measurement procedure and releases internal resources."""
        if self.is_session_initialized:
            self.session.close()
            self._instrument = None

    def configure_measurement_function(self, parameters: DcRmsVoltageMeasurementFunctionParameters):
        """Configures the measurement function settings for the DMM.

        Args:
            parameters (DcRmsVoltageMeasurementFunctionParameters):
                An instance of `DcRmsVoltageMeasurementFunctionParameters` containing the
                measurement function type (DC/AC voltage) and resolution in digits to configure.
        """
        measurement_function_and_range = RangeAndMeasurementFunctionParameters(
            parameters.measurement_function
        )
        resolution_in_digits = parameters.resolution_in_digits.value
        self.session.configure_measurement_digits(
            measurement_function=measurement_function_and_range.measurement_function,
            range=measurement_function_and_range.range_value,
            resolution_digits=resolution_in_digits,
        )

    def configure_trigger(self, parameters: TriggerParameters):
        """Configure the characteristics of triggers used for voltage measurements.

        Args:
            parameters (TriggerParameters):
                An instance of `TriggerParameters` containing trigger source,
                trigger delay, slope, and enable/disable flag.
        """
        if not parameters.enable_trigger:
            self.session.configure_trigger(
                trigger_source=nidmm.TriggerSource.IMMEDIATE, trigger_delay=-1.0
            )
            return
        self.session.configure_trigger(
            trigger_source=nidmm.TriggerSource[parameters.trigger_source.name],
            trigger_delay=parameters.trigger_delay,
        )
        # Configure Slope only if trigger is enabled
        nidmm_trigger_slope_attribute_id = 1250334
        self.session._set_attribute_vi_int32(
            nidmm_trigger_slope_attribute_id, parameters.trigger_slope.value
        )

    def configure_timing(self, parameters: TimingParameters):
        """Configures the timing characteristics used for voltage measurements.

        Args:
            parameters (TimingParameters):
                An instance of `TimingParameters` containing aperture time and
                settle time settings.
        """
        self.session.aperture_time = parameters.aperture_time_seconds
        self.session.settle_time = parameters.settle_time_seconds

    def acquire_measurement(self, resolution_in_digits: float) -> DcRmsVoltageMeasurementResultData:
        """Acquires and formats the measurement result data.

        Args:
            resolution_in_digits (float):
                The resolution in digits used for formatting the measured value.

        Returns:
            DcRmsVoltageMeasurementResultData:
                An instance of `DcRmsVoltageMeasurementResultData` containing:
                - dmm_execution_settings: Dictionary with keys 'Function', 'Range',
                  'Digits_Resolution', 'Aperture_Time(s)', 'Settle_Time(s)',
                  'Minimum_Frequency(Hz)', 'Absolute_Resolution',
                  'Input_Resistance(Ohm)', and 'Auto_Range_Value'
                - measurement: Dictionary with keys 'Measured_Value', 'Unit', and
                  'Formatted_Measurement'
        """
        measured_value = self.session.read()
        measurement = FormatMeasurement.measurement(
            resolution_in_digits=resolution_in_digits,
            measured_value=measured_value,
            measurement_function=self.session.function,
        )
        aperture_time = "{}{}".format(
            *FormatMeasurement.format_with_si_prefix(self.session.aperture_time, 3)
        )
        settle_time = "{}{}".format(
            *FormatMeasurement.format_with_si_prefix(self.session.settle_time.total_seconds(), 3)
        )
        dmm_execution_settings = {
            "Function": self.session.function.name,
            "Range": self.session.range,
            "Digits_Resolution": self.session.resolution_digits,
            "Aperture_Time(s)": aperture_time,
            "Settle_Time(s)": settle_time,
            "Minimum_Frequency(Hz)": self.session.ac_min_freq,
            "Absolute_Resolution": self.session.resolution_absolute,
            "Input_Resistance(Ohm)": self.session.input_resistance,
            "Auto_Range_Value": self.session.auto_range_value,
        }
        return DcRmsVoltageMeasurementResultData(
            dmm_execution_settings=dmm_execution_settings, measurement=measurement
        )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/mixed_measurements/__init__.py sha256=6072fe38ed228d80df16f23660f3b10b07aef0307ad6df5bd4ae1da85c19b97d bytes=59 -->
## FILE: src/nipcbatt/pcbatt_library/dmm/mixed_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dmm/mixed_measurements/__init__.py`
- sha256: `6072fe38ed228d80df16f23660f3b10b07aef0307ad6df5bd4ae1da85c19b97d`
- bytes: 59

````python
"""Provides mixed measurement functionality using DMM."""
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/mixed_measurements/mixed_measurement.py sha256=a70bde54d301a7ce76fc4b17443175c9bbcaa6b98d9c43a0334a2df7b26782b9 bytes=7945 -->
## FILE: src/nipcbatt/pcbatt_library/dmm/mixed_measurements/mixed_measurement.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dmm/mixed_measurements/mixed_measurement.py`
- sha256: `a70bde54d301a7ce76fc4b17443175c9bbcaa6b98d9c43a0334a2df7b26782b9`
- bytes: 7945

````python
"""Defines class used for mixed measurement on PCB points."""

from typing import Union

import nidmm

from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
from nipcbatt.pcbatt_library.dmm.common.common_data_types import (
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library.dmm.common.helper_functions import (
    FormatMeasurement,
    RangeAndMeasurementFunctionParameters,
)
from nipcbatt.pcbatt_library.dmm.mixed_measurements.mixed_measurement_data_types import (
    MixedMeasurementConfiguration,
    MixedMeasurementFunctionParameters,
    MixedMeasurementResultData,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import (
    BuildingBlockUsingNIDMM,
)


class MixedMeasurement(BuildingBlockUsingNIDMM):
    """Defines a way that allows you to perform mixed measurements on PCB points."""

    def initialize(self, dmm_resource_name: str, powerline_frequency: float):
        """Initializes the DMM session with the specific resource name and powerline frequency.

        Args:
            dmm_resource_name (str):
                The resource name of the DMM device to use for measurements.
            powerline_frequency (float):
                The powerline frequency in Hz.
        """
        self._dmm_resource_name = dmm_resource_name
        self._powerline_frequency = powerline_frequency
        self._instrument = nidmm.Session(resource_name=self._dmm_resource_name)
        self.session.powerline_freq = self._powerline_frequency

    def configure_and_measure(
        self, configuration: MixedMeasurementConfiguration
    ) -> Union[MixedMeasurementResultData, None]:
        """Configures and/or performs a measurement according to specific configuration parameters.

        Args:
            configuration (MixedMeasurementConfiguration):
                An instance of `MixedMeasurementConfiguration` used to configure
                the measurement.

        Returns:
            MixedMeasurementResultData | None: An instance of
                `MixedMeasurementResultData` containing DMM execution settings
                and the measured value, or None if only configuration was performed.
        """
        if configuration.execution_type in (
            MeasurementExecutionType.CONFIGURE_ONLY,
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        ):
            self.configure_measurement_function(
                parameters=configuration.measurement_function_parameters
            )
            self.configure_trigger(parameters=configuration.trigger_parameters)
            self.configure_timing(parameters=configuration.timing_parameters)
            if self.session.function == nidmm.Function.AC_VOLTS:
                self.session.ac_min_freq = configuration.ac_min_frequency

        if configuration.execution_type in (
            MeasurementExecutionType.MEASURE_ONLY,
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        ):
            return self.acquire_measurement(
                configuration.measurement_function_parameters.resolution_in_digits.value
            )
        return None

    def close(self):
        """Closes measurement procedure and releases internal resources."""
        if self.is_session_initialized:
            self.session.close()
            self._instrument = None

    def configure_measurement_function(self, parameters: MixedMeasurementFunctionParameters):
        """Configures the measurement function settings for the DMM.

        Args:
            parameters (MixedMeasurementFunctionParameters):
                An instance of `MixedMeasurementFunctionParameters` containing the
                measurement function type and resolution in digits to configure.
        """
        measurement_function_and_range = RangeAndMeasurementFunctionParameters(
            parameters.measurement_function
        )
        resolution_in_digits = parameters.resolution_in_digits.value
        self.session.configure_measurement_digits(
            measurement_function=measurement_function_and_range.measurement_function,
            range=measurement_function_and_range.range_value,
            resolution_digits=resolution_in_digits,
        )

    def configure_trigger(self, parameters: TriggerParameters):
        """Configure the characteristics of triggers used for mixed measurements.

        Args:
            parameters (TriggerParameters):
                An instance of `TriggerParameters` containing trigger source,
                trigger delay, slope, and enable/disable flag.
        """
        if not parameters.enable_trigger:
            self.session.configure_trigger(
                trigger_source=nidmm.TriggerSource.IMMEDIATE, trigger_delay=-1.0
            )
            return
        self.session.configure_trigger(
            trigger_source=nidmm.TriggerSource[parameters.trigger_source.name],
            trigger_delay=parameters.trigger_delay,
        )
        # Configure Slope only if trigger is enabled
        nidmm_trigger_slope_attribute_id = 1250334
        self.session._set_attribute_vi_int32(
            nidmm_trigger_slope_attribute_id, parameters.trigger_slope.value
        )

    def configure_timing(self, parameters: TimingParameters):
        """Configures the timing characteristics used for mixed measurements.

        Args:
            parameters (TimingParameters):
                An instance of `TimingParameters` containing aperture time and
                settle time settings.
        """
        self.session.aperture_time = parameters.aperture_time_seconds
        self.session.settle_time = parameters.settle_time_seconds

    def acquire_measurement(self, resolution_in_digits: float) -> MixedMeasurementResultData:
        """Acquires and formats the measurement result data.

        Args:
            resolution_in_digits (float):
                The resolution in digits used for formatting the measured value.

        Returns:
            MixedMeasurementResultData:
                An instance of `MixedMeasurementResultData` containing:
                - dmm_execution_settings: Dictionary with keys 'Function', 'Range',
                  'Digits_Resolution', 'Aperture_Time(s)', 'Settle_Time(s)',
                  'Minimum_Frequency(Hz)', 'Absolute_Resolution',
                  'Input_Resistance(Ohm)', and 'Auto_Range_Value'
                - measurement: Dictionary with keys 'Measured_Value', 'Unit', and
                  'Formatted_Measurement'
        """
        measured_value = self.session.read()
        measurement = FormatMeasurement.measurement(
            resolution_in_digits=resolution_in_digits,
            measured_value=measured_value,
            measurement_function=self.session.function,
        )
        aperture_time = "{}{}".format(
            *FormatMeasurement.format_with_si_prefix(self.session.aperture_time, 3)
        )
        settle_time = "{}{}".format(
            *FormatMeasurement.format_with_si_prefix(self.session.settle_time.total_seconds(), 3)
        )
        dmm_execution_settings = {
            "Function": self.session.function.name,
            "Range": self.session.range,
            "Digits_Resolution": self.session.resolution_digits,
            "Aperture_Time(s)": aperture_time,
            "Settle_Time(s)": settle_time,
            "Minimum_Frequency(Hz)": self.session.ac_min_freq,
            "Absolute_Resolution": self.session.resolution_absolute,
            "Input_Resistance(Ohm)": self.session.input_resistance,
            "Auto_Range_Value": self.session.auto_range_value,
        }
        return MixedMeasurementResultData(
            dmm_execution_settings=dmm_execution_settings, measurement=measurement
        )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/mixed_measurements/mixed_measurement_constants.py sha256=6534c8a3caaffa9e256fab88059aec091b6a7ad9eb0a4947e6e12ff51abe10e8 bytes=2529 -->
## FILE: src/nipcbatt/pcbatt_library/dmm/mixed_measurements/mixed_measurement_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dmm/mixed_measurements/mixed_measurement_constants.py`
- sha256: `6534c8a3caaffa9e256fab88059aec091b6a7ad9eb0a4947e6e12ff51abe10e8`
- bytes: 2529

````python
"""Constants for Mixed Measurements."""

import dataclasses

from nipcbatt.pcbatt_library.dmm.common.common_data_types import (
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library.dmm.common.constants import ConstantsForDcRmsMeasurements
from nipcbatt.pcbatt_library.dmm.mixed_measurements.mixed_measurement_data_types import (
    MixedMeasurementConfiguration,
    MixedMeasurementFunctionParameters,
    MixedRangeAndFunctions,
)


@dataclasses.dataclass
class ConstantsForMixedMeasurements:
    """Constants used for Mixed measurement."""

    RANGE_AND_FUNCTION = MixedRangeAndFunctions.DC_Voltage_Auto_Range


# Mixed measurement-specific range/function setting is defined
# in ConstantsForMixedMeasurements.
# Default execution type for Mixed measurements
DEFAULT_MIXED_EXECUTION_TYPE = ConstantsForDcRmsMeasurements.DEFAULT_EXECUTION_TYPE

# Default measurement function parameter including mixed range/function and resolution in digits.
DEFAULT_MIXED_MEASUREMENT_PARAMETERS = MixedMeasurementFunctionParameters(
    measurement_function=ConstantsForMixedMeasurements.RANGE_AND_FUNCTION,
    resolution_in_digits=ConstantsForDcRmsMeasurements.DEFAULT_RESOLUTION_IN_DIGITS,
)

# Default timing parameters including aperture time and settle time.
DEFAULT_MIXED_TIMING_PARAMETERS = TimingParameters(
    aperture_time_seconds=ConstantsForDcRmsMeasurements.DEFAULT_APERTURE_TIME_SECONDS,
    settle_time_seconds=ConstantsForDcRmsMeasurements.DEFAULT_SETTLE_TIME_SECONDS,
)

# Default AC minimum frequency
DEFAULT_MIXED_AC_MIN_FREQUENCY = ConstantsForDcRmsMeasurements.DEFAULT_AC_MIN_FREQUENCY

# Default trigger parameters including trigger source, trigger delay, and trigger enable setting.
DEFAULT_MIXED_TRIGGER_PARAMETERS = TriggerParameters(
    trigger_source=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_SOURCE,
    trigger_delay=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_DELAY,
    slope=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_SLOPE,
    enable_trigger=ConstantsForDcRmsMeasurements.DEFAULT_ENABLE_TRIGGER,
)

# Default DC-RMS mixed measurement configuration.
DEFAULT_MIXED_MEASUREMENT_CONFIGURATION = MixedMeasurementConfiguration(
    execution_type=DEFAULT_MIXED_EXECUTION_TYPE,
    measurement_function_parameters=DEFAULT_MIXED_MEASUREMENT_PARAMETERS,
    trigger_parameters=DEFAULT_MIXED_TRIGGER_PARAMETERS,
    timing_parameters=DEFAULT_MIXED_TIMING_PARAMETERS,
    ac_min_frequency=DEFAULT_MIXED_AC_MIN_FREQUENCY,
)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/mixed_measurements/mixed_measurement_data_types.py sha256=72fb2382791f7f4e0f003ce4d8e36be5654130eedb3fed1e7b9c2b2d509ba9c0 bytes=8977 -->
## FILE: src/nipcbatt/pcbatt_library/dmm/mixed_measurements/mixed_measurement_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dmm/mixed_measurements/mixed_measurement_data_types.py`
- sha256: `72fb2382791f7f4e0f003ce4d8e36be5654130eedb3fed1e7b9c2b2d509ba9c0`
- bytes: 8977

````python
"""Mixed measurement data types."""

from enum import Enum
from typing import Union

import nidmm

from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
from nipcbatt.pcbatt_library.dmm.common.common_data_types import (
    ResolutionInDigits,
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData


class MixedRangeAndFunctions(Enum):
    """Defines the measurement function and range settings for mixed measurement."""

    DC_Voltage_Auto_Range = (nidmm.Function.DC_VOLTS, -1.0)
    DC_100mV = (nidmm.Function.DC_VOLTS, 0.1)
    DC_1V = (nidmm.Function.DC_VOLTS, 1)
    DC_10V = (nidmm.Function.DC_VOLTS, 10)
    DC_100V = (nidmm.Function.DC_VOLTS, 100)
    DC_300V = (nidmm.Function.DC_VOLTS, 300)

    AC_Voltage_Auto_Range = (nidmm.Function.AC_VOLTS, -1.0)
    AC_50mV = (nidmm.Function.AC_VOLTS, 0.05)
    AC_200mV = (nidmm.Function.AC_VOLTS, 0.2)
    AC_500mV = (nidmm.Function.AC_VOLTS, 0.5)
    AC_2V = (nidmm.Function.AC_VOLTS, 2)
    AC_5V = (nidmm.Function.AC_VOLTS, 5)
    AC_20V = (nidmm.Function.AC_VOLTS, 20)
    AC_50V = (nidmm.Function.AC_VOLTS, 50)
    AC_300V = (nidmm.Function.AC_VOLTS, 300)

    DC_Current_Auto_Range = (nidmm.Function.DC_CURRENT, -1.0)
    DC_1uA = (nidmm.Function.DC_CURRENT, 0.000001)
    DC_10uA = (nidmm.Function.DC_CURRENT, 0.00001)
    DC_100uA = (nidmm.Function.DC_CURRENT, 0.0001)
    DC_1mA = (nidmm.Function.DC_CURRENT, 0.001)
    DC_10mA = (nidmm.Function.DC_CURRENT, 0.01)
    DC_20mA = (nidmm.Function.DC_CURRENT, 0.02)
    DC_100mA = (nidmm.Function.DC_CURRENT, 0.1)
    DC_200mA = (nidmm.Function.DC_CURRENT, 0.2)
    DC_1A = (nidmm.Function.DC_CURRENT, 1)
    DC_3A = (nidmm.Function.DC_CURRENT, 3)

    AC_Current_Auto_Range = (nidmm.Function.AC_CURRENT, -1.0)
    AC_100uA = (nidmm.Function.AC_CURRENT, 0.0001)
    AC_1mA = (nidmm.Function.AC_CURRENT, 0.001)
    AC_10mA = (nidmm.Function.AC_CURRENT, 0.01)
    AC_100mA = (nidmm.Function.AC_CURRENT, 0.1)
    AC_500mA = (nidmm.Function.AC_CURRENT, 0.5)
    AC_1A = (nidmm.Function.AC_CURRENT, 1)
    AC_3A = (nidmm.Function.AC_CURRENT, 3)

    TWO_W_Resistance_Auto_Range = (nidmm.Function.TWO_WIRE_RES, -1.0)
    TWO_W_RES_100_Ohm = (nidmm.Function.TWO_WIRE_RES, 100)
    TWO_W_RES_1k_Ohm = (nidmm.Function.TWO_WIRE_RES, 1000)
    TWO_W_RES_10k_Ohm = (nidmm.Function.TWO_WIRE_RES, 10000)
    TWO_W_RES_100k_Ohm = (nidmm.Function.TWO_WIRE_RES, 100000)
    TWO_W_RES_1M_Ohm = (nidmm.Function.TWO_WIRE_RES, 1000000)
    TWO_W_RES_10M_Ohm = (nidmm.Function.TWO_WIRE_RES, 10000000)
    TWO_W_RES_100M_Ohm = (nidmm.Function.TWO_WIRE_RES, 100000000)
    TWO_W_RES_5G_Ohm = (nidmm.Function.TWO_WIRE_RES, 5000000000)

    FOUR_W_Resistance_Auto_Range = (nidmm.Function.FOUR_WIRE_RES, -1.0)
    FOUR_W_RES_100_Ohm = (nidmm.Function.FOUR_WIRE_RES, 100)
    FOUR_W_RES_1k_Ohm = (nidmm.Function.FOUR_WIRE_RES, 1000)
    FOUR_W_RES_10k_Ohm = (nidmm.Function.FOUR_WIRE_RES, 10000)
    FOUR_W_RES_100k_Ohm = (nidmm.Function.FOUR_WIRE_RES, 100000)
    FOUR_W_RES_1M_Ohm = (nidmm.Function.FOUR_WIRE_RES, 1000000)
    FOUR_W_RES_10M_Ohm = (nidmm.Function.FOUR_WIRE_RES, 10000000)


class MixedMeasurementFunctionParameters:
    """Defines parameters used for configuration of mixed measurement."""

    def __init__(
        self,
        measurement_function: MixedRangeAndFunctions,
        resolution_in_digits: ResolutionInDigits,
    ) -> None:
        """Initializes measurement function parameters.

        Args:
            measurement_function (MixedRangeAndFunctions):
                The mixed measurement function and range setting.
            resolution_in_digits (ResolutionInDigits):
                The measurement resolution in digits.
        """
        self._measurement_function = measurement_function
        self._resolution_in_digits = resolution_in_digits

    @property
    def measurement_function(self) -> MixedRangeAndFunctions:
        """Gets the mixed measurement function and range setting.

        Returns:
            MixedRangeAndFunctions: The configured mixed range and function.
        """
        return self._measurement_function

    @property
    def resolution_in_digits(self) -> ResolutionInDigits:
        """Gets the measurement resolution in digits.

        Returns:
            ResolutionInDigits: The configured resolution setting.
        """
        return self._resolution_in_digits


class MixedMeasurementConfiguration(PCBATestToolkitData):
    """Defines configuration parameters for mixed measurements."""

    def __init__(
        self,
        execution_type: MeasurementExecutionType,
        measurement_function_parameters: MixedMeasurementFunctionParameters,
        trigger_parameters: TriggerParameters,
        timing_parameters: TimingParameters,
        ac_min_frequency: float,
    ) -> None:
        """Initializes the mixed measurement configuration.

        Args:
            execution_type (MeasurementExecutionType):
                Specifies whether to configure only, measure only, or both configure and measure.
            measurement_function_parameters (MixedMeasurementFunctionParameters):
                The measurement function settings including mixed range and resolution.
            trigger_parameters (TriggerParameters):
                Trigger configuration including source, delay, and enable/disable settings.
            timing_parameters (TimingParameters):
                Timing settings including aperture time and settle time.
            ac_min_frequency (float):
                Minimum frequency for AC Voltage, Current measurements in Hz
                (ignored for DC measurements).
        """
        self._execution_type = execution_type
        self._measurement_function_parameters = measurement_function_parameters
        self._trigger_parameters = trigger_parameters
        self._timing_parameters = timing_parameters
        self._ac_min_frequency = ac_min_frequency

    @property
    def execution_type(self) -> MeasurementExecutionType:
        """Gets the measurement execution type.

        Returns:
            MeasurementExecutionType: The execution mode (configure only, measure only, or both).
        """
        return self._execution_type

    @property
    def trigger_parameters(self) -> TriggerParameters:
        """Gets the trigger configuration parameters.

        Returns:
            TriggerParameters: The trigger settings for the measurement.
        """
        return self._trigger_parameters

    @property
    def measurement_function_parameters(self) -> MixedMeasurementFunctionParameters:
        """Gets the measurement function parameters.

        Returns:
            MixedMeasurementFunctionParameters: The mixed range, function,
            and resolution settings.
        """
        return self._measurement_function_parameters

    @property
    def timing_parameters(self) -> TimingParameters:
        """Gets the timing configuration parameters.

        Returns:
            TimingParameters: The aperture time and settle time settings.
        """
        return self._timing_parameters

    @property
    def ac_min_frequency(self) -> float:
        """Gets the minimum AC frequency setting.

        Returns:
            float: The minimum frequency for AC voltage, current measurements.
        """
        return self._ac_min_frequency


class MixedMeasurementResultData(PCBATestToolkitData):
    """Defines mixed measurement results obtained from DMM mixed measurement."""

    def __init__(self, dmm_execution_settings: dict, measurement: Union[dict, None]) -> None:
        """Initializes the mixed measurement result data.

        Args:
            dmm_execution_settings (dict):
                Dictionary containing the DMM configuration used during measurement.
            measurement (dict | None):
                Dictionary containing the measurement results,
                or None if only configuration was performed.
        """
        self._dmm_execution_settings = dmm_execution_settings
        self._measurement = measurement

    @property
    def dmm_execution_settings(self) -> dict:
        """Gets the DMM execution settings used during the measurement.

        Returns:
            dict: Dictionary with labeled keys and values including units for each setting.
        """
        return self._dmm_execution_settings

    @property
    def measurement(self) -> Union[dict, None]:
        """Gets the measurement result data.

        Returns:
            dict | None: Dictionary containing 'Measured_Value', 'Unit', and
                'Formatted_Measurement' keys, or None if only configuration was performed.
        """
        return self._measurement
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/resistance_measurements/__init__.py sha256=33652080c852caeefdf88f2d8342853d6296eebf3f8113b81994f098085fa0c5 bytes=64 -->
## FILE: src/nipcbatt/pcbatt_library/dmm/resistance_measurements/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dmm/resistance_measurements/__init__.py`
- sha256: `33652080c852caeefdf88f2d8342853d6296eebf3f8113b81994f098085fa0c5`
- bytes: 64

````python
"""Provides resistance measurement functionality using DMM."""
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/resistance_measurements/resistance_constants.py sha256=f619b5d4ea13bf60de986d243061eb30a009101f1da755145308ee0f04438921 bytes=2494 -->
## FILE: src/nipcbatt/pcbatt_library/dmm/resistance_measurements/resistance_constants.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dmm/resistance_measurements/resistance_constants.py`
- sha256: `f619b5d4ea13bf60de986d243061eb30a009101f1da755145308ee0f04438921`
- bytes: 2494

````python
"""Constants for Resistance Measurements."""

import dataclasses

from nipcbatt.pcbatt_library.dmm.common.common_data_types import (
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library.dmm.common.constants import ConstantsForDcRmsMeasurements
from nipcbatt.pcbatt_library.dmm.resistance_measurements.resistance_data_types import (
    ResistanceMeasurementConfiguration,
    ResistanceMeasurementFunctionParameters,
    ResistanceRangeAndFunctions,
)


@dataclasses.dataclass
class ConstantsForDcRmsResistanceMeasurements:
    """Constants used for Resistance measurement."""

    RANGE_AND_FUNCTION = ResistanceRangeAndFunctions.TWO_W_Resistance_Auto_Range


# Resistance measurement-specific range/function setting is defined
# in ConstantsForDcRmsResistanceMeasurements.
# Default execution type for resistance measurements
DEFAULT_RESISTANCE_EXECUTION_TYPE = ConstantsForDcRmsMeasurements.DEFAULT_EXECUTION_TYPE

# Default measurement function parameter including resistance range/function
# and resolution in digits.
DEFAULT_RESISTANCE_MEASUREMENT_PARAMETERS = ResistanceMeasurementFunctionParameters(
    measurement_function=ConstantsForDcRmsResistanceMeasurements.RANGE_AND_FUNCTION,
    resolution_in_digits=ConstantsForDcRmsMeasurements.DEFAULT_RESOLUTION_IN_DIGITS,
)

# Default timing parameters including aperture time and settle time.
DEFAULT_RESISTANCE_TIMING_PARAMETERS = TimingParameters(
    aperture_time_seconds=ConstantsForDcRmsMeasurements.DEFAULT_APERTURE_TIME_SECONDS,
    settle_time_seconds=ConstantsForDcRmsMeasurements.DEFAULT_SETTLE_TIME_SECONDS,
)

# Default trigger parameters including trigger source, trigger delay, and trigger enable setting.
DEFAULT_RESISTANCE_TRIGGER_PARAMETERS = TriggerParameters(
    trigger_source=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_SOURCE,
    trigger_delay=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_DELAY,
    enable_trigger=ConstantsForDcRmsMeasurements.DEFAULT_ENABLE_TRIGGER,
    slope=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_SLOPE,
)

# Default DC-RMS resistance measurement configuration.
DEFAULT_RESISTANCE_MEASUREMENT_CONFIGURATION = ResistanceMeasurementConfiguration(
    execution_type=DEFAULT_RESISTANCE_EXECUTION_TYPE,
    measurement_function_parameters=DEFAULT_RESISTANCE_MEASUREMENT_PARAMETERS,
    trigger_parameters=DEFAULT_RESISTANCE_TRIGGER_PARAMETERS,
    timing_parameters=DEFAULT_RESISTANCE_TIMING_PARAMETERS,
)
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/resistance_measurements/resistance_data_types.py sha256=a50957022ddb5b2fbbdeab0e9672da808cd3676132314518b01afca713e2f4f4 bytes=6925 -->
## FILE: src/nipcbatt/pcbatt_library/dmm/resistance_measurements/resistance_data_types.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dmm/resistance_measurements/resistance_data_types.py`
- sha256: `a50957022ddb5b2fbbdeab0e9672da808cd3676132314518b01afca713e2f4f4`
- bytes: 6925

````python
"""Resistance measurement data types."""

from enum import Enum
from typing import Union

import nidmm

from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
from nipcbatt.pcbatt_library.dmm.common.common_data_types import (
    ResolutionInDigits,
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData


class ResistanceRangeAndFunctions(Enum):
    """Defines the measurement function and range settings for resistance measurement."""

    TWO_W_Resistance_Auto_Range = (nidmm.Function.TWO_WIRE_RES, -1.0)
    TWO_W_RES_100_Ohm = (nidmm.Function.TWO_WIRE_RES, 100)
    TWO_W_RES_1k_Ohm = (nidmm.Function.TWO_WIRE_RES, 1000)
    TWO_W_RES_10k_Ohm = (nidmm.Function.TWO_WIRE_RES, 10000)
    TWO_W_RES_100k_Ohm = (nidmm.Function.TWO_WIRE_RES, 100000)
    TWO_W_RES_1M_Ohm = (nidmm.Function.TWO_WIRE_RES, 1000000)
    TWO_W_RES_10M_Ohm = (nidmm.Function.TWO_WIRE_RES, 10000000)
    TWO_W_RES_100M_Ohm = (nidmm.Function.TWO_WIRE_RES, 100000000)
    TWO_W_RES_5G_Ohm = (nidmm.Function.TWO_WIRE_RES, 5000000000)

    FOUR_W_Resistance_Auto_Range = (nidmm.Function.FOUR_WIRE_RES, -1.0)
    FOUR_W_RES_100_Ohm = (nidmm.Function.FOUR_WIRE_RES, 100)
    FOUR_W_RES_1k_Ohm = (nidmm.Function.FOUR_WIRE_RES, 1000)
    FOUR_W_RES_10k_Ohm = (nidmm.Function.FOUR_WIRE_RES, 10000)
    FOUR_W_RES_100k_Ohm = (nidmm.Function.FOUR_WIRE_RES, 100000)
    FOUR_W_RES_1M_Ohm = (nidmm.Function.FOUR_WIRE_RES, 1000000)
    FOUR_W_RES_10M_Ohm = (nidmm.Function.FOUR_WIRE_RES, 10000000)


class ResistanceMeasurementFunctionParameters:
    """Defines parameters used for configuration of resistance measurement."""

    def __init__(
        self,
        measurement_function: ResistanceRangeAndFunctions,
        resolution_in_digits: ResolutionInDigits,
    ) -> None:
        """Initializes measurement function parameters.

        Args:
            measurement_function (ResistanceRangeAndFunctions):
                The resistance measurement function and range setting.
            resolution_in_digits (ResolutionInDigits):
                The measurement resolution in digits.
        """
        self._measurement_function = measurement_function
        self._resolution_in_digits = resolution_in_digits

    @property
    def measurement_function(self) -> ResistanceRangeAndFunctions:
        """Gets the resistance measurement function and range setting.

        Returns:
            ResistanceRangeAndFunctions: The configured resistance range and function.
        """
        return self._measurement_function

    @property
    def resolution_in_digits(self) -> ResolutionInDigits:
        """Gets the measurement resolution in digits.

        Returns:
            ResolutionInDigits: The configured resolution setting.
        """
        return self._resolution_in_digits


class ResistanceMeasurementConfiguration(PCBATestToolkitData):
    """Defines configuration parameters for resistance measurements."""

    def __init__(
        self,
        execution_type: MeasurementExecutionType,
        measurement_function_parameters: ResistanceMeasurementFunctionParameters,
        trigger_parameters: TriggerParameters,
        timing_parameters: TimingParameters,
    ) -> None:
        """Initializes the resistance measurement configuration.

        Args:
            execution_type (MeasurementExecutionType):
                Specifies whether to configure only, measure only, or both configure and measure.
            measurement_function_parameters (ResistanceMeasurementFunctionParameters):
                The measurement function settings including resistance range and resolution.
            trigger_parameters (TriggerParameters):
                Trigger configuration including source, delay, and enable/disable settings.
            timing_parameters (TimingParameters):
                Timing settings including aperture time and settle time.
        """
        self._execution_type = execution_type
        self._measurement_function_parameters = measurement_function_parameters
        self._trigger_parameters = trigger_parameters
        self._timing_parameters = timing_parameters

    @property
    def execution_type(self) -> MeasurementExecutionType:
        """Gets the measurement execution type.

        Returns:
            MeasurementExecutionType: The execution mode (configure only, measure only, or both).
        """
        return self._execution_type

    @property
    def trigger_parameters(self) -> TriggerParameters:
        """Gets the trigger configuration parameters.

        Returns:
            TriggerParameters: The trigger settings for the measurement.
        """
        return self._trigger_parameters

    @property
    def measurement_function_parameters(self) -> ResistanceMeasurementFunctionParameters:
        """Gets the measurement function parameters.

        Returns:
            ResistanceMeasurementFunctionParameters: The resistance range, function,
            and resolution settings.
        """
        return self._measurement_function_parameters

    @property
    def timing_parameters(self) -> TimingParameters:
        """Gets the timing configuration parameters.

        Returns:
            TimingParameters: The aperture time and settle time settings.
        """
        return self._timing_parameters


class ResistanceMeasurementResultData(PCBATestToolkitData):
    """Defines resistance measurement results obtained from DMM Resistance Measurement."""

    def __init__(self, dmm_execution_settings: dict, measurement: Union[dict, None]) -> None:
        """Initializes the resistance measurement result data.

        Args:
            dmm_execution_settings (dict):
                Dictionary containing the DMM configuration used during measurement.
            measurement (dict | None):
                Dictionary containing the measurement results,
                or None if only configuration was performed.
        """
        self._dmm_execution_settings = dmm_execution_settings
        self._measurement = measurement

    @property
    def dmm_execution_settings(self) -> dict:
        """Gets the DMM execution settings used during the measurement.

        Returns:
            dict: Dictionary with labeled keys and values including units for each setting.
        """
        return self._dmm_execution_settings

    @property
    def measurement(self) -> Union[dict, None]:
        """Gets the measurement result data.

        Returns:
            dict | None: Dictionary containing 'Measured_Value', 'Unit', and
                'Formatted_Measurement' keys, or None if only configuration was performed.
        """
        return self._measurement
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm/resistance_measurements/resistance_measurement.py sha256=062070222671713f8b7a802c20f0e534600c85d39dbea8a175dd8b1c8b92bc8e bytes=7975 -->
## FILE: src/nipcbatt/pcbatt_library/dmm/resistance_measurements/resistance_measurement.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dmm/resistance_measurements/resistance_measurement.py`
- sha256: `062070222671713f8b7a802c20f0e534600c85d39dbea8a175dd8b1c8b92bc8e`
- bytes: 7975

````python
"""Defines class used for resistance measurement on PCB points."""

from typing import Union

import nidmm

from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
from nipcbatt.pcbatt_library.dmm.common.common_data_types import (
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library.dmm.common.helper_functions import (
    FormatMeasurement,
    RangeAndMeasurementFunctionParameters,
)
from nipcbatt.pcbatt_library.dmm.resistance_measurements.resistance_data_types import (
    ResistanceMeasurementConfiguration,
    ResistanceMeasurementFunctionParameters,
    ResistanceMeasurementResultData,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import (
    BuildingBlockUsingNIDMM,
)


class DcRmsResistanceMeasurement(BuildingBlockUsingNIDMM):
    """Defines a way that allows you to perform resistance measurements on PCB points."""

    def initialize(self, dmm_resource_name: str, powerline_frequency: float):
        """Initializes the DMM session with the specific resource name and powerline frequency.

        Args:
            dmm_resource_name (str):
                The resource name of the DMM device to use for measurements.
            powerline_frequency (float):
                The powerline frequency in Hz (typically 50.0 or 60.0).
        """
        self._dmm_resource_name = dmm_resource_name
        self._powerline_frequency = powerline_frequency
        self._instrument = nidmm.Session(resource_name=self._dmm_resource_name)
        self.session.powerline_freq = self._powerline_frequency

    def configure_and_measure(
        self, configuration: ResistanceMeasurementConfiguration
    ) -> Union[ResistanceMeasurementResultData, None]:
        """Configures and/or performs a measurement according to specific configuration parameters.

        Args:
            configuration (ResistanceMeasurementConfiguration):
                An instance of `ResistanceMeasurementConfiguration` used to configure
                the measurement.

        Returns:
            ResistanceMeasurementResultData | None: An instance of
                `ResistanceMeasurementResultData` containing DMM execution settings
                and the measured resistance value, or None if only configuration was performed.
        """
        if configuration.execution_type in (
            MeasurementExecutionType.CONFIGURE_ONLY,
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        ):
            self.configure_measurement_function(
                parameters=configuration.measurement_function_parameters
            )
            self.configure_trigger(parameters=configuration.trigger_parameters)
            self.configure_timing(parameters=configuration.timing_parameters)

        if configuration.execution_type in (
            MeasurementExecutionType.MEASURE_ONLY,
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        ):
            return self.acquire_measurement(
                configuration.measurement_function_parameters.resolution_in_digits.value
            )
        return None

    def close(self):
        """Closes measurement procedure and releases internal resources."""
        if self.is_session_initialized:
            self.session.close()
            self._instrument = None

    def configure_measurement_function(self, parameters: ResistanceMeasurementFunctionParameters):
        """Configures the measurement function settings for the DMM.

        Args:
            parameters (ResistanceMeasurementFunctionParameters):
                An instance of `ResistanceMeasurementFunctionParameters` containing the measurement
                function type (2-wire/4-wire resistance) and resolution in digits to configure.
        """
        measurement_function_and_range = RangeAndMeasurementFunctionParameters(
            parameters.measurement_function
        )
        resolution_in_digits = parameters.resolution_in_digits.value
        self.session.configure_measurement_digits(
            measurement_function=measurement_function_and_range.measurement_function,
            range=measurement_function_and_range.range_value,
            resolution_digits=resolution_in_digits,
        )

    def configure_trigger(self, parameters: TriggerParameters):
        """Configure the characteristics of triggers used for resistance measurements.

        Args:
            parameters (TriggerParameters):
                An instance of `TriggerParameters` containing trigger source,
                trigger delay, slope, and enable/disable flag.
        """
        if not parameters.enable_trigger:
            self.session.configure_trigger(
                trigger_source=nidmm.TriggerSource.IMMEDIATE, trigger_delay=-1.0
            )
            return
        self.session.configure_trigger(
            trigger_source=nidmm.TriggerSource[parameters.trigger_source.name],
            trigger_delay=parameters.trigger_delay,
        )
        # Configure Slope only if trigger is enabled
        nidmm_trigger_slope_attribute_id = 1250334
        self.session._set_attribute_vi_int32(
            nidmm_trigger_slope_attribute_id, parameters.trigger_slope.value
        )

    def configure_timing(self, parameters: TimingParameters):
        """Configures the timing characteristics used for resistance measurements.

        Args:
            parameters (TimingParameters):
                An instance of `TimingParameters` containing aperture time and
                settle time settings.
        """
        self.session.aperture_time = parameters.aperture_time_seconds
        self.session.settle_time = parameters.settle_time_seconds

    def acquire_measurement(self, resolution_in_digits: float) -> ResistanceMeasurementResultData:
        """Acquires and formats the measurement result data.

        Args:
            resolution_in_digits (float):
                The resolution in digits used for formatting the measured value.

        Returns:
            ResistanceMeasurementResultData:
                An instance of `ResistanceMeasurementResultData` containing:
                - dmm_execution_settings: Dictionary with keys 'Function', 'Range',
                  'Digits_Resolution', 'Aperture_Time(s)', 'Settle_Time(s)',
                  'Minimum_Frequency(Hz)', 'Absolute_Resolution',
                  'Input_Resistance(Ohm)', and 'Auto_Range_Value'
                - measurement: Dictionary with keys 'Measured_Value', 'Unit', and
                  'Formatted_Measurement'
        """
        measured_value = self.session.read()
        measurement = FormatMeasurement.measurement(
            resolution_in_digits=resolution_in_digits,
            measured_value=measured_value,
            measurement_function=self.session.function,
        )
        aperture_time = "{}{}".format(
            *FormatMeasurement.format_with_si_prefix(self.session.aperture_time, 3)
        )
        settle_time = "{}{}".format(
            *FormatMeasurement.format_with_si_prefix(self.session.settle_time.total_seconds(), 3)
        )
        dmm_execution_settings = {
            "Function": self.session.function.name,
            "Range": self.session.range,
            "Digits_Resolution": self.session.resolution_digits,
            "Aperture_Time(s)": aperture_time,
            "Settle_Time(s)": settle_time,
            "Minimum_Frequency(Hz)": self.session.ac_min_freq,
            "Absolute_Resolution": self.session.resolution_absolute,
            "Input_Resistance(Ohm)": self.session.input_resistance,
            "Auto_Range_Value": self.session.auto_range_value,
        }
        return ResistanceMeasurementResultData(
            dmm_execution_settings=dmm_execution_settings, measurement=measurement
        )
````

<!--NI_OSS_SOURCE repo=nipcbatt path=src/nipcbatt/pcbatt_library/dmm_scan/__init__.py sha256=bb459f21ecd342dc3ec83ae35ef8d0cc6f384de5624580a23950ad318d16d00b bytes=220 -->
## FILE: src/nipcbatt/pcbatt_library/dmm_scan/__init__.py

- repository: `ni/nipcbatt`
- source_path: `src/nipcbatt/pcbatt_library/dmm_scan/__init__.py`
- sha256: `bb459f21ecd342dc3ec83ae35ef8d0cc6f384de5624580a23950ad318d16d00b`
- bytes: 220

````python
# pylint: disable=C0200, C0103, C0301

"""Contains classes used in dmm scan."""

from nipcbatt.pcbatt_library.dmm_scan.dmm_scan_pmps_16V_15C import (
    DmmScanPMPS,
    MeasurementResult,
    ScanResources,
)
````
