# NI PYTHON API DIGEST: grpc-device

<!--NI_PYTHON_API_SNAPSHOT repo=ni/grpc-device commit=13c1d30177e5da4b0c444b2ceab74506ca3847fb -->

<!--NI_PYTHON_API repo=grpc-device path=examples/nidaqmx/analog-input-every-n-samples-aio.py -->
## PYTHON MODULE: examples/nidaqmx/analog-input-every-n-samples-aio.py

### MODULE DOCSTRING

Acquire analog data using the grpc asyncio API and RegisterEveryNSamplesEvent.

The gRPC API is built from the C API. NI-DAQmx documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\NI-DAQ\docs\cdaqmx.chm

Getting Started:

To run this example, install "NI-DAQmx Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI DAQmx gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-DAQMX-C-Function-Reference

To run this example without hardware: create a simulated device in NI MAX on the server (Windows
only).

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python analog-input-every-n-samples-aio.py <server_address> <port_number> <physical_channel_name>
To acquire data from multiple channels, pass in a list or range of channels (i.e., Dev1/ai0:3).
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "Dev1/ai0" as the physical channel name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `PHYSICAL_CHANNEL = 'Dev1/ai0'`

### `async def _main()`

<!--NI_PYTHON_API repo=grpc-device path=examples/nidaqmx/analog-input-every-n-samples.py -->
## PYTHON MODULE: examples/nidaqmx/analog-input-every-n-samples.py

### MODULE DOCSTRING

Acquire analog data using futures and RegisterEveryNSamplesEvent.

The gRPC API is built from the C API. NI-DAQmx documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\NI-DAQ\docs\cdaqmx.chm

Getting Started:

To run this example, install "NI-DAQmx Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI DAQmx gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-DAQMX-C-Function-Reference

To run this example without hardware: create a simulated device in NI MAX on the server (Windows
only).

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python analog-input-every-n-samples.py <server_address> <port_number> <physical_channel_name>
To acquire data from multiple channels, pass in a list or range of channels (i.e., Dev1/ai0:3).
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "Dev1/ai0" as the physical channel name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `PHYSICAL_CHANNEL = 'Dev1/ai0'`

### `def _main()`

<!--NI_PYTHON_API repo=grpc-device path=examples/nidaqmx/analog-input.py -->
## PYTHON MODULE: examples/nidaqmx/analog-input.py

### MODULE DOCSTRING

Acquire a finite amount of data using the DAQ device's internal clock.

The gRPC API is built from the C API. NI-DAQmx documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\NI-DAQ\docs\cdaqmx.chm

Getting Started:

To run this example, install "NI-DAQmx Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI DAQmx gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-DAQMX-C-Function-Reference

To run this example without hardware: create a simulated device in NI MAX on the server (Windows
only).

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python analog-input.py <server_address> <port_number> <physical_channel_name>
To acquire data from multiple channels, pass in a list or range of channels (i.e., Dev1/ai0:3).
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "Dev1/ai0" as the physical channel name..


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `PHYSICAL_CHANNEL = 'Dev1/ai0'`

### `def check_for_warning(response)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nidaqmx/analog-output.py -->
## PYTHON MODULE: examples/nidaqmx/analog-output.py

### MODULE DOCSTRING

Output a single Voltage Update (Sample) to an Analog Output Channel.

The gRPC API is built from the C API. NI-DAQmx documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\NI-DAQ\docs\cdaqmx.chm

Getting Started:

To run this example, install "NI-DAQmx Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI DAQmx gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-DAQMX-C-Function-Reference

To run this example without hardware: create a simulated device in NI MAX on the server (Windows
only).

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python analog-output.py <server_address> <port_number> <physical_channel_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "Dev1/ao0" as the physical channel name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `PHYSICAL_CHANNEL = 'Dev1/ao0'`

### `def check_for_warning(response)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nidaqmx/counter-input.py -->
## PYTHON MODULE: examples/nidaqmx/counter-input.py

### MODULE DOCSTRING

Measure frequency using one counter on a Counter Input Channel.

The gRPC API is built from the C API. NI-DAQmx documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\NI-DAQ\docs\cdaqmx.chm

Getting Started:

To run this example, install "NI-DAQmx Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI DAQmx gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-DAQMX-C-Function-Reference

To run this example without hardware: create a simulated device in NI MAX on the server (Windows
only).

Running from command line:

Server machine's IP address, port number, and counter name can be passed as separate command line
arguments.
  > python counter-input.py <server_address> <port_number> <counter_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "Dev1/ctr0" as the counter name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `COUNTER_NAME = 'Dev1/ctr0'`

### `def check_for_warning(response)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nidaqmx/counter-output.py -->
## PYTHON MODULE: examples/nidaqmx/counter-output.py

### MODULE DOCSTRING

Generate a single digital pulse from a Counter Output Channel.

The gRPC API is built from the C API. NI-DAQmx documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\NI-DAQ\docs\cdaqmx.chm

Getting Started:

To run this example, install "NI-DAQmx Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI DAQmx gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-DAQMX-C-Function-Reference

To run this example without hardware: create a simulated device in NI MAX on the server (Windows
only).

Running from command line:

Server machine's IP address, port number, and counter name can be passed as separate command line
arguments.
  > python counter-output.py <server_address> <port_number> <counter_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "Dev1/ctr0" as the counter name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `COUNTER_NAME = 'Dev1/ctr0'`

### `def check_for_warning(response)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nidaqmx/digital-input.py -->
## PYTHON MODULE: examples/nidaqmx/digital-input.py

### MODULE DOCSTRING

Read values from a digital input port.

The gRPC API is built from the C API. NI-DAQmx documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\NI-DAQ\docs\cdaqmx.chm

Getting Started:

To run this example, install "NI-DAQmx Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI DAQmx gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-DAQMX-C-Function-Reference

To run this example without hardware: create a simulated device in NI MAX on the server (Windows
only).

Running from command line:

Server machine's IP address, port number, and lines name can be passed as separate command line
arguments.
  > python digital-input.py <server_address> <port_number> <lines_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "Dev1/port0" as the lines name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `LINES = 'Dev1/port0'`

### `def check_for_warning(response)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nidaqmx/digital-output.py -->
## PYTHON MODULE: examples/nidaqmx/digital-output.py

### MODULE DOCSTRING

Write values to a digital output port.

The gRPC API is built from the C API. NI-DAQmx documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\NI-DAQ\docs\cdaqmx.chm

Getting Started:

To run this example, install "NI-DAQmx Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI DAQmx gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-DAQMX-C-Function-Reference

To run this example without hardware: create a simulated device in NI MAX on the server (Windows
only).

Running from command line:

Server machine's IP address, port number, and lines name can be passed as separate command line
arguments.
  > python digital-output.py <server_address> <port_number> <lines_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "Dev1/port0" as the lines name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `LINES = 'Dev1/port0'`

### `def check_for_warning(response)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nidaqmx/dsa-shared-timebase-and-trig-analog-input-and-output-aio.py -->
## PYTHON MODULE: examples/nidaqmx/dsa-shared-timebase-and-trig-analog-input-and-output-aio.py

### MODULE DOCSTRING

Configure a total of four tasks on two PXI Dynamic Signal Acquistion (DSA) devices.

Each device runs a task for analog input and another for analog output. This example illustrates
continuous analog input and output operations.

Instructions for Running:
  1. Select which type of Synchronization method you want to use.
  2. Select the physical channel corresponding to the input signal on the DAQ device.
  3. Enter the minimum and maximum expected voltage for the input and output operations on each
     device.
     Note: For optimal accuracy, match the input range to the expected voltage level of the
           measured signal (for input) and generated signal (for output).
  4. Set the number of samples to acquire per channel. This parameter determines how many points
     will be read and generated with each iteration.
  5. Set the rate of the acquisition and generation. The same sampling rate is employed for input
     and output operations on each device.
  Note: The sampling rate should be at least 2.2 times the maximum frequency component of the
        signal being acquired on analog input and the signal being generated on analog output.
        Frequency components beyond about 0.47 times the sampling rate will be eliminated by the
        alias and imaging protection on the DSA device.

Steps:
  1. Create a task.
  2. Create an analog input and output channel for both the leader and follower devices.
  3. Set timing parameters for a continuous acquisition. The sample rate and block size are set to
     the same values for each device.
  4. There are two types of synchronization available on DSA devices. The first method shares the
     Sample Clock Timebase across the PXI_Star bus. It also uses the Sync Pulse which is shared
     across the PXI_Trig / RTSI bus. The second method uses the Sync Pulse in conjunction with the
     PXI Reference clock 10 on the PXI backplane.
  5. Call the Get Terminal Name with Device Prefix utility function. This will take a Task and a
     terminal and create a properly formatted device + terminal name. This signal is then used as an
     output generation trigger on the leader as well as and acquisition start trigger and generation
     start trigger on the follower. The signal is shared along the PXI_Trig / RTSI bus.
  6. Synthesize a standard sine waveform and load this data into the output RAM buffer for each
     device.
  7. Call the Start function to start the acquisition.
  8. Read all of the data continuously. The 'Samples per Channel' control will specify how many
     samples per channel are read each time. If either device reports an error or the user presses
     Enter, the acquisition will stop.
  9. Call the Clear Task function to clear the task.
  10. Display an error if any.

I/O Connections Overview:
  Make sure your signal input and output terminals matches the Physical Channel I/O controls.

  It is important to ensure that your PXI chassis has been properly configured in MAX. If your
  chassis has not been configured in software before running the example, your devices may fail to
  synchronize properly.


The gRPC API is built from the C API. NI-DAQmx documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\NI-DAQ\docs\cdaqmx.chm

Getting Started:

To run this example, install "NI-DAQmx Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-daqmx.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI DAQmx gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-DAQMX-C-Function-Reference

This example requires physical hardware.

Running from command line:

Server machine's IP address, port number, leader_device, and follower_device can be passed as
separate command line arguments.
  > python dsa-shared-timebase-and-trig-analog-input-and-output-aio.py <server_address> <port_number> <leader_device> <follower_device>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "Dev1" as the leader device and "Dev2" as the follower device.


- `SYNCHRONIZATION_TYPE_IS_REFERENCE_CLOCK = False`

- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `LEADER_DEVICE = 'Dev1'`

- `FOLLOWER_DEVICE = 'Dev2'`

- `LEADER_INPUT_CHANNEL = f'{LEADER_DEVICE}/ai0'`

- `LEADER_OUTPUT_CHANNEL = f'{LEADER_DEVICE}/ao0'`

- `FOLLOWER_INPUT_CHANNEL = f'{FOLLOWER_DEVICE}/ai0'`

- `FOLLOWER_OUTPUT_CHANNEL = f'{FOLLOWER_DEVICE}/ao0'`

### `def check_for_warning(response)`

Print to console if the status indicates a warning.

### `async def _main()`

### `async def _cleanup()`

<!--NI_PYTHON_API repo=grpc-device path=examples/nidcpower/measure-record.py -->
## PYTHON MODULE: examples/nidcpower/measure-record.py

### MODULE DOCSTRING

Perform continuous measure record.

The gRPC API is built from the C API. NI-DCPower documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niDCPower\Documentation\NIDCPowerCref.chm

Getting Started:

To run this example, install "NI-DCPower Driver" on the server machine:
  https://www.ni.com/en-in/support/downloads/drivers/download.ni-dcpower.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI DCPOWER gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-DCPOWER-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and resource name can be passed as separate command line
arguments.
  > python measure-record.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDCPower" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'NI-DCPower-Session'`

- `RESOURCE = 'SimulatedDCPower'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:4147;BoardType:PXIe'`

- `CHANNELS = '0'`

- `RECORD_LENGTH = 10`

- `BUFFER_MULTIPLIER = 10`

- `VOLTAGE_LEVEL = 5.0`

### `def check_for_warning(response, vi)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nidigitalpattern/configure-voltage-levels-and-termination-voltage.py -->
## PYTHON MODULE: examples/nidigitalpattern/configure-voltage-levels-and-termination-voltage.py

### MODULE DOCSTRING

Create an instrument session, configure various voltage levels, and then burst a pattern.

The VOL, VOH, VIH, VIL, VTERM, IOL, IOH, and VCOM values are configurable parameters and the user
can select from High-Z (h), Active Load (a) and Three-Level Drive (t) termination options in
TERM_SELECT.

The gRPC API is built from the C API. NI-Digital Pattern Driver Pattern documentation is installed
with the driver at:
  C:\Users\Public\Documents\National Instruments\NI-Digital-Pattern-Driver\Documentation\Digital Pattern Help.chm

Copy the .pinmap, .specs, .digitiming & .digipat files that come with this example to a folder on
the server machine & copy-paste the path of the folder to the DIRECTORY_PATH variable below.

Use the NI Digital Pattern Editor to create or modify pin or channel map files:
  https://www.ni.com/documentation/en/ni-digital/20.6/digital-pattern-editor/pin-channel-map-editor/

Getting Started:

To run this example, install "NI-Digital Pattern Driver" on the server machine:
  https://www.ni.com/en-in/support/downloads/drivers/download.ni-digital-pattern-driver.html#367315

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-Digital Pattern Driver gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-DIGITAL-PATTERN-DRIVER-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and resource name can be passed as separate command line
arguments.
  > python configure-voltage-levels-and-termination-voltage.py <server_address> <port_number> <resource>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "PXI1Slot2" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'NI-Digital-Pattern-Driver-Session'`

- `RESOURCE = 'PXI1Slot2'`

- `OPTIONS = 'Simulate=1, DriverSetup=Model:6570'`

- `DIRECTORY_PATH = ''`

- `CHANNEL_LIST = 'PinGroup1'`

- `VIL = 0`

- `VIH = 5`

- `VOL = 3`

- `VOH = 2`

- `VTERM = 5`

- `IOL = 0.015`

- `IOH = -0.024`

- `VCOM = 2`

- `TERM_SELECT = 'h'`

### `def check_for_warning(response, vi)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nidmm/continuous-acquire-graph-multiple-points.py -->
## PYTHON MODULE: examples/nidmm/continuous-acquire-graph-multiple-points.py

### MODULE DOCSTRING

Perform continuous multipoint acquisition; print the number of points read and average value.

The gRPC API is built from the C API. NI-DMM documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niDMM\Documentation\English\DMM.chm

Getting Started:

To run this example, install "NI-DMM Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-dmm.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI DMM gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-DMM-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and resource name can be passed as separate command line
arguments.
  > python continuous-acquire-graph-multiple-points.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDMM" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'NI-DMM-Session'`

- `RESOURCE = 'SimulatedDMM'`

- `OPTIONS = 'Simulate=1, DriverSetup=Model:4080; BoardType:PXIe'`

- `MAX_PTS_TO_READ = 1000`

- `CONFIG_RANGE = 10.0`

- `RESOLUTION = 5.5`

- `MEASUREMENT_TYPE = nidmm_types.Function.FUNCTION_NIDMM_VAL_DC_VOLTS`

- `POWERLINE_FREQ = nidmm_types.PowerLineFrequencies.POWER_LINE_FREQUENCIES_NIDMM_VAL_60_HERTZ`

### `def check_for_warning(response, vi)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nifgen/basic-arbitrary-waveform.py -->
## PYTHON MODULE: examples/nifgen/basic-arbitrary-waveform.py

### MODULE DOCSTRING

Generate a basic arbitrary waveform with Arbitrary Waveform Mode.

The gRPC API is built from the C API. NI-FGEN documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niFgen\documentation\English\SigGenHelp.chm

Getting Started:

To run this example, install "NI-FGEN Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-fgen.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Running from command line:

Server machine's IP address, port number, and resource name can be passed as separate command line
arguments.
  > python basic-arbitrary-waveform.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedFGEN" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'NI-FGEN-Session'`

- `RESOURCE = 'SimulatedFGEN'`

- `OPTIONS = 'Simulate=1, DriverSetup=Model:5441; BoardType:PXI'`

- `CHANNEL_NAME = '0'`

- `SAMPLE_RATE = 40000000.0`

- `GAIN = 1.0`

- `DC_OFFSET = 0.0`

- `WAVEFORM_SIZE = 64`

- `SINE = [math.sin(i / WAVEFORM_SIZE * 2 * math.pi) for i in range(WAVEFORM_SIZE)]`

### `def check_for_warning(response, vi)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nifpga/read_write_array_example.py -->
## PYTHON MODULE: examples/nifpga/read_write_array_example.py

### MODULE DOCSTRING

Read and Write to Arrays.

The gRPC API is built from the C API. NI-FPGA documentation is installed with the driver at:
    C:\Program Files (x86)\National Instruments\FPGA Interface C API\capi.chm

Getting Started:

To run this example with your VI, you need to configure the values below.
Additionally, ensure you have a VI that includes arrays and update the references for them below.
Make sure the R-Series drivers are installed on the system where the gRPC-device server is running.
You will also need LABVIEW and the LABVIEW FPGA module to configure the VIs.

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Server machine's IP address, port number, and resource name can be passed as separate command line
arguments.
  > python read_write_example.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "FPGA" as the resource name.

This example attempts to read and write values to an array.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'NI-FPGA-Session'`

- `RESOURCE = 'FPGA'`

- `NI_FPGA_EXAMPLE_BITFILE_PATH = 'C:\\DemoExample.lvbitx'`

- `NI_FPGA_EXAMPLE_SIGNATURE = '11F1FF1D11F1FF1F1F111FF11F11F111'`

- `EXAMPLE_ARRAY_CONTROL = 65540`

- `EXAMPLE_ARRAY_CONTROL_SIZE = 4`

### `def check_for_warning(response)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nifpga/read_write_fifo_example.py -->
## PYTHON MODULE: examples/nifpga/read_write_fifo_example.py

### MODULE DOCSTRING

Read and Write to controls and FIFO.

The gRPC API is built from the C API. NI-FPGA documentation is installed with the driver at:
    C:\Program Files (x86)\National Instruments\FPGA Interface C API\capi.chm

Getting Started:

To run this example with your VI, you need to configure the values below.
Additionally, you should have a VI that includes controls and FIFOs, and update the
references for them below. Ensure that the R-Series drivers are installed on the system
where the gRPC-device server is running. You will also need LABVIEW and the LABVIEW FPGA
module to configure the VIs.

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Server machine's IP address, port number, and resource name can be passed as separate command line
arguments.
  > python read_write_example.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "FPGA" as the resource name.

In this example, we specify the number of elements to write to the FIFO and provide
a multiplier as input. We then read elements from another FIFO, which contains the multiplied
values of the elements from the first FIFO.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'NI-FPGA-Session'`

- `RESOURCE = 'FPGA'`

- `EXAMPLE_BITFILE_PATH = 'C:\\DemoExample.lvbitx'`

- `EXAMPLE_SIGNATURE = '11F1FF1D11F1FF1F1F111FF11F11F111'`

- `EXAMPLE_NUMERIC_CONTROL = 65546`

- `EXAMPLE_TARGET_TO_HOST_FIFO = 0`

- `EXAMPLE_HOST_TO_TARGET_FIFO = 1`

### `def check_for_warning(response)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirf/rfsa-rfsg-NR-analysis-only-modacc.py -->
## PYTHON MODULE: examples/nirf/rfsa-rfsg-NR-analysis-only-modacc.py

### MODULE DOCSTRING

Demonstration on how to use RFSA, RFSG and RFmx in Analysis Only mode.

This example shows how to generate a TDMS waveform using RFSG, to capture the raw IQ data using
RFSA and to demodulate it using RFmx Analysis Only mode.

The gRPC API is built from the C API. NI-RFSG documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niRFSG\documentation\English\RFSG.chm

The gRPC API is built from the C API. NI-RFSA documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niRFSG\documentation\English\RFSA.chm

The gRPC API is built from the C API. RFmx NR documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\NR\Documentation\rfmxnrcvi.chm

Getting Started:

To run this example, install "RFmx NR", "RFSA" and "RFSG" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-nr.html
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-rfsa.html
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-rfsg.html


For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxNR gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxNR-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python rfsa-rfsg-NR-analysis-only-modacc.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `RFMXSESSION_NAME = 'RFmxNRSession'`

- `RFSASESSION_NAME = 'RfsaSession'`

- `RFSGSESSION_NAME = 'RfsgSession'`

- `RESOURCE = '5840_1'`

- `RFMXOPTIONS = 'AnalysisOnly=1'`

- `RFSAOPTIONS = 'DriverSetup=SFPSessionAccess:1'`

- `RFSGOPTIONS = ''`

### `def raise_if_initialization_error(response)`

Raise an exception if an error was returned from Initialize.

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirf/specan-nr-txp-example.py -->
## PYTHON MODULE: examples/nirf/specan-nr-txp-example.py

### MODULE DOCSTRING

Multi Rfmx Personality Example with SpecAn and NR.

Steps:
  1. Open only one RFmx Session. No need to open every personality.
  2. Configure Frequency Reference.
  3. Configure Selected Ports.
  4. Configure basic signal properties(Center Frequency, Reference Level and External Attenuation).
  5. Configure Link Direction, Frequency Range, Carrier Bandwidthand Subcarrier Spacing.
  6. Select NR TXP and SpecAn TXP measurement and enable Traces.
  7. Configure Measurement Offset & Measurement Length Parameters and Averaging Parameters for TXP
     measurement.
  9. Initiate NR Measurement.
  10. Fetch NR Measurements and Traces.
  11. Initiate SpecAn Measurement.
  12. Fetch SpecAn Measurements and Traces.
  13. Close RFmx Session.

The gRPC API is built from the C API. RFmx NR documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\NR\Documentation\rfmxnrcvi.chm

Getting Started:

To run this example, install "RFmx NR" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-nr.html

To run this example, install "RFmx SpecAn" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-specan.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxNR gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxNR-C-Function-Reference

Refer to the NI-RFmxSpecAn gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxSpecAn-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python txp-single-carrier.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxNRSession'`

- `RESOURCE = '5840_1'`

- `OPTIONS = ''`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxbluetooth/acp-basic.py -->
## PYTHON MODULE: examples/nirfmxbluetooth/acp-basic.py

### MODULE DOCSTRING

Fetch ACP data.

Steps:
  1. Open a new RFmx Session.
  2. Configure Frequency Reference.
  3. Configure basic signal properties(Center Frequency, Reference Level and External Attenuation).
  4. Configure Trigger Type and Trigger Parameters.
  5. Configure Packet Type.
  6. Configure Data Rate.
  7. Configure Payload Length.
  8. Select ACP measurement and enable Traces.
  9. Configure ACP Burst Sync Type.
  10. Configure Averaging Parameters for ACP measurement.
  11. Configure Number of Offsets or Channel Number depending on Offset Channel Mode.
  12. Initiate the Measurement.
  13. Fetch ACP Measurements and Trace.
  14. Close RFmx Session.

The gRPC API is built from the C API. RFmx Bluetooth documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\BT\Documentation\rfmxbtcvi.chm

Getting Started:

To run this example, install "RFmx Bluetooth" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-bluetooth.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxBluetooth gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxBluetooth-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python acp-basic.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxBluetoothSession'`

- `RESOURCE = 'SimulatedDevice'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxbluetooth/txp-basic.py -->
## PYTHON MODULE: examples/nirfmxbluetooth/txp-basic.py

### MODULE DOCSTRING

Fetch TXP data.

Steps:
  1. Open a new RFmx Session.
  2. Configure Frequency Reference.
  3. Configure basic signal properties(Center Frequency and External Attenuation).
  4. Configure Trigger Type and Trigger Parameters.
  5. Configure Packet Type.
  6. Configure Data Rate.
  7. Configure Payload Length.
  8. Configure Direction Finding.
  9. Configure Reference Level.
  10. Select TXP measurement and enable Traces.
  11. Configure TXP Burst Synchronization Type.
  12. Configure Averaging Parameters for TXP measurement.
  13. Initiate the Measurement.
  14. Fetch TXP Measurements and Trace.
  15. Close RFmx Session.

The gRPC API is built from the C API. RFmx Bluetooth documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\BT\Documentation\rfmxbtcvi.chm

Getting Started:

To run this example, install "RFmx Bluetooth" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-bluetooth.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxBluetooth gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxBluetooth-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python txp-basic.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxBluetoothSession'`

- `RESOURCE = 'SimulatedDevice'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxcdma2k/acp.py -->
## PYTHON MODULE: examples/nirfmxcdma2k/acp.py

### MODULE DOCSTRING

Fetch ACP data.

Steps:
1. Open a new RFmx session
2. Configure Reference Clock
3. Configure the basic signal properties  (Center Frequency, Reference Level and External
   Attenuation)
4. Configure RF Attenuation
5. Configure Trigger
6. Configure Band Class
7. Set Measurement to ACP
8. Configure Number of Offsets
9. Set Noise Compensation
10. Set Dynamic Range Mode
11. Configure Sweep Time
12. Configure Averaging Parameters
13. Commit Settings and Initiate Measurement
14. Fetch diverse ACP Measurement Results
15. Close the RFmx Session

The gRPC API is built from the C API. RFmx CDMA2k documentation is installed with the driver at:
C:\Program Files (x86)\National Instruments\RFmx\CDMA2k\Documentation\cdma2kcvi.chm

Getting Started:

To run this example, install "RFmx CDMA2k" on the server machine.
Link: https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-cdma2k.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a
gRPC Client" wiki page.
Link: https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxCDMA2k gRPC Wiki for the latest C Function Reference:
Link: https://github.com/ni/grpc-device/wiki/NI-RFmxCDMA2k-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python RFmxCdma2kAcp.c <server_address> <port_number> <physical_channel_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxCDMA2kSession'`

- `RESOURCE = 'SimulatedDevice'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

- `NUMBER_OF_OFFSETS = 2`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxcdma2k/modacc.py -->
## PYTHON MODULE: examples/nirfmxcdma2k/modacc.py

### MODULE DOCSTRING

Fetch ModAcc data.

Steps:
1. Open a new RFmx session
2. Configure Reference Clock
3. Configure the basic signal properties  (Center Frequency, Reference Level and External
   Attenuation)
4. Configure Trigger
5. Configure Radio Configuration
6. Configure Long Code Mask
7. Set Measurement to ModAcc
8. Configure Synchronization mode
9. Commit Settings and Initiate Measurement
10. Fetch diverse ModAcc Measurement Results
11. Close the RFmx Session

The gRPC API is built from the C API. RFmx CDMA2k documentation is installed with the driver at:
C:\Program Files (x86)\National Instruments\RFmx\CDMA2k\Documentation\cdma2kcvi.chm

Getting Started:

To run this example, install "RFmx CDMA2k" on the server machine.
Link: https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-cdma2k.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page.
Link: https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxCDMA2k gRPC Wiki for the latest C Function Reference:
Link: https://github.com/ni/grpc-device/wiki/NI-RFmxCDMA2k-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python RFmxCdma2kModAcc.c <server_address> <port_number> <physical_channel_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxCDMA2kSession'`

- `RESOURCE = 'SimulatedDevice'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxdemod/ADemod-AM-basic.py -->
## PYTHON MODULE: examples/nirfmxdemod/ADemod-AM-basic.py

### MODULE DOCSTRING

ADemod AM example.

Steps:
1. Open a new RFmxInstrMX session and create a Demod Signal
2. Configure Selected Ports
3. Configure basic signal properties (Center Frequency, Reference Level and External Attenuation)
4. Configure ADemod rbw, Measurement Interval, AM Carrier Suppressed and Averaging
5. Read ADemod AM Measurement Results
6. Dispose Demod Signal and Close the RFmxInstrMX Session

The gRPC API is built from the C API. RFmx Demod documentation is installed with the driver at:
C:\Program Files (x86)\National Instruments\RFmx\Demod\Documentation\demodcvi.chm

Getting Started:

To run this example, install "RFmx Demod" on the server machine.
Link: https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-demod.html

For instructions on how to use protoc to generate gRPC client interfaces, see our
"Creating a gRPC Client" wiki page.
Link: https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxDemod gRPC Wiki for the latest C Function Reference:
Link: https://github.com/ni/grpc-device/wiki/NI-RFmxDemod-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python ADemod-AM-basic.py <server_address> <port_number> <physical_channel_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxDemodSession'`

- `RESOURCE = 'SimulatedDevice'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxdemod/DDemod-QAM-basic.py -->
## PYTHON MODULE: examples/nirfmxdemod/DDemod-QAM-basic.py

### MODULE DOCSTRING

DDemod QAM example.

Steps:
1. Open a new RFmxInstrMX session and create a Demod Signal
2. Configure Selected Ports
3. Configure basic signal properties (Center Frequency, Reference Level and External Attenuation)
4. Select QAM Modulation and M
5. Configure DDemod Symbol Rate, Number of Symbols and Pulse Shaping Filter
6. Configure DDemod Measurement Filter Type as Auto
7. Configure DDemod Averaging
8. Read DDemod Measurement Results
9. Dispose Demod Signal and Close the RFmxInstrMX Session

The gRPC API is built from the C API. RFmx Demod documentation is installed with the driver at:
C:\Program Files (x86)\National Instruments\RFmx\Demod\Documentation\demodcvi.chm

Getting Started:

To run this example, install "RFmx Demod" on the server machine.
Link: https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-demod.html

For instructions on how to use protoc to generate gRPC client interfaces, see our
"Creating a gRPC Client" wiki page.
Link: https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxDemod gRPC Wiki for the latest C Function Reference:
Link: https://github.com/ni/grpc-device/wiki/NI-RFmxDemod-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python DDemod-QAM-basic.py <server_address> <port_number> <physical_channel_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxDemodSession'`

- `RESOURCE = 'SimulatedDevice'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxgsm/evm.py -->
## PYTHON MODULE: examples/nirfmxgsm/evm.py

### MODULE DOCSTRING

EVM example.

Steps:
1. Open a new RFmx Session.
2. Configure Frequency Reference.
3. Configure basic signal properties (Center Frequency, Reference Level and External Attenuation).
4. Configure Trigger Parameters for IQ Power Edge Trigger.
5. Configure Number of Timeslots.
6. Configure Auto tsc Detection Enabled.
7. Configure Signal Type.
8. Configure tsc.
9. Select ModAcc measurement and enable Traces.
10. Configure Averaging Parameters for ModAcc measurement.
11. Initiate the Measurement.
12. Fetch ModAcc Measurements and Traces.
13. Close RFmx Session.

The gRPC API is built from the C API. RFmx GSM documentation is installed with the driver at:
C:\Program Files (x86)\National Instruments\RFmx\GSM\Documentation\rfmxgsmcvi.chm

Getting Started:

To run this example, install "RFmx GSM" on the server machine.
Link: https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-gsm-edge-.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page.
Link: https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmx GSM gRPC Wiki for the latest C Function Reference:
Link: https://github.com/ni/grpc-device/wiki/NI-RFmx-GSM-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python evm.py <server_address> <port_number> <physical_channel_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxGSMSession'`

- `RESOURCE = 'SimulatedDevice'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

- `NUMBER_OF_TIMESLOTS = 1`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxgsm/orfs.py -->
## PYTHON MODULE: examples/nirfmxgsm/orfs.py

### MODULE DOCSTRING

ORFS example.

Steps:
1. Open a new RFmx Session.
2. Configure Frequency Reference.
3. Configure External Attenuation.
4. Configure Center Frequency.
5. Configure Link Direction.
6. Configure Trigger Parameters for IQ Power Edge Trigger.
7. Configure Number of Timeslots.
8. Configure Signal Type.
9. Configure Auto Level.
10. Configure Auto tsc Detection Enabled.
11. Configure tsc.
12. Select  ORFS  measurement and enable Traces.
13. Configure Noise Compensation Enabled.
14. Configure Measurement Type.
15. Configure Offset Frequency Mode.
16. Configure Evaluation Symbols.
17. Configure Averaging Parameters.
18. Initiate the Measurement.
19. Fetch ORFS Measurements and Traces.
20. Close RFmx Session.

The gRPC API is built from the C API. RFmx GSM documentation is installed with the driver at:
C:\Program Files (x86)\National Instruments\RFmx\GSM\Documentation\rfmxgsmcvi.chm

Getting Started:

To run this example, install "RFmx GSM" on the server machine.
Link: https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-gsm-edge-.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page.
Link: https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmx GSM gRPC Wiki for the latest C Function Reference:
Link: https://github.com/ni/grpc-device/wiki/NI-RFmx-GSM-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python orfs.py <server_address> <port_number> <physical_channel_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxGSMSession'`

- `RESOURCE = 'SimulatedDevice'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxlte/acp-single-carrier.py -->
## PYTHON MODULE: examples/nirfmxlte/acp-single-carrier.py

### MODULE DOCSTRING

Fetch ACP data.

Steps:
  1. Open a new RFmx Session.
  2. Configure Frequency Reference.
  3. Configure basic signal properties(Center Frequency, RF Attenuation and External Attenuation).
  4. Configure Trigger Type and Trigger Parameters.
  5. Configure Carrier Bandwidth.
  6. Configure Reference Level.
  7. Configure Duplex Mode.
  8. Configure Link Direction.
  9. Select ACP measurement and enable Traces.
  10. Configure Measurement Method.
  11. Configure Averaging Parameters for ACP measurement.
  12. Configure Sweep Time Parameters.
  13. Configure Noise Compensation Parameter.
  14. Initiate the Measurement.
  15. Fetch ACP Measurements and Traces.
  16. Close RFmx Session.

The gRPC API is built from the C API. RFmx LTE documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\LTE\Documentation\ltecvi.chm

Getting Started:

To run this example, install "RFmx LTE" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-lte.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxLTE gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxLTE-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python acp-single-carrier.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxLTESession'`

- `RESOURCE = 'SimulatedDevice'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

- `NUMBER_OF_OFFSETS = 3`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxlte/ul-modacc-single-carrier.py -->
## PYTHON MODULE: examples/nirfmxlte/ul-modacc-single-carrier.py

### MODULE DOCSTRING

Fetch UL ModAcc data.

Steps:
  1. Open a new RFmx Session.
  2. Configure Frequency Reference.
  3. Configure basic signal properties (Center Frequency, Reference Level and External Attenuation).
  4. Configure Trigger Type and Trigger Parameters.
  5. Configure Carrier Bandwidth.
  6. Configure operating Band.
  7. Configure Duplex Mode.
  8. Configure Auto DMRS Detection Enabled.
  9. Select ModAcc measurement and enable Traces.
  10. Configure Synchronization Mode and Measurement Interval.
  11. Configure EVM Unit.
  12. Configure In-Band Emission Mask Type.
  13. Configure Averaging Parameters for ModAcc measurement.
  14. Initiate the Measurement.
  15. Fetch ModAcc Measurements and Traces.
  16. Close RFmx Session.

The gRPC API is built from the C API. RFmx LTE documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\LTE\Documentation\ltecvi.chm

Getting Started:

To run this example, install "RFmx LTE" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-lte.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxLTE gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxLTE-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python ul-modacc-single-carrier.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxLTESession'`

- `RESOURCE = 'SimulatedDevice'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxnr/acp-single-carrier.py -->
## PYTHON MODULE: examples/nirfmxnr/acp-single-carrier.py

### MODULE DOCSTRING

Fetch ACP data.

Steps:
  1. Open a new RFmx Session.
  2. Configure Frequency Reference.
  3. Configure Selected Ports.
  4. Configure basic signal properties (Center Frequency, RF Attenuation and External Attenuation).
  5. Configure Trigger Parameters for IQ Power Edge Trigger.
  6. Configure Link Direction, Frequency Range and Carrier Bandwidth and Subcarrier Spacing.
  7. Configure Reference Level.
  8. Select ACP measurement and enable Traces.
  9. Configure Measurement Method.
  10. Configure Noise Compensation Parameter.
  11. Configure Sweep Time Parameters.
  12. Configure Averaging Parameters for ACP measurement.
  13. Initiate the Measurement.
  14. Fetch ACP Measurements and Traces.
  15. Close RFmx Session.

The gRPC API is built from the C API. RFmx NR documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\NR\Documentation\rfmxnrcvi.chm

Getting Started:

To run this example, install "RFmx NR" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-nr.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxNR gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxNR-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python acp-single-carrier.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxNRSession'`

- `RESOURCE = 'SimulatedDevice'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxnr/acp-txp-modacc-single-carrier.py -->
## PYTHON MODULE: examples/nirfmxnr/acp-txp-modacc-single-carrier.py

### MODULE DOCSTRING

Fetch ACP, ModAcc, and TXP data.

Steps:
  1. Open a new RFmx Session.
  2. Configure Frequency Reference.
  3. Configure Selected Ports.
  4. Configure basic signal properties (Center Frequency, RF Attenuation and External Attenuation).
  5. Configure Trigger Type and Trigger Parameters.
  6. Configure Link Direction, Frequency Range and Carrier Bandwidth and Subcarrier Spacing.
  7. Configure Reference Level.
  8. Select ACP, ModAcc, and TXP measurements and enable Traces.
  9. Configure ACP Measurement Method.
  10. Configure ACP Noise Compensation Parameter.
  11. Configure ACP Sweep Time Parameters.
  12. Configure ACP Averaging Parameters.
  13. Configure TXP Measurement Interval.
  14. Configure TXP Averaging Parameters.
  15. Configure ModAcc Measurement Interval.
  16. Configure ModAcc Averaging Parameters.
  17. Initiate the Measurement.
  18. Fetch ACP, TXP, and ModAcc Measurements.
  19. Close RFmx Session.

The gRPC API is built from the C API. RFmx NR documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\NR\Documentation\rfmxnrcvi.chm

Getting Started:

To run this example, install "RFmx NR" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-nr.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxNR gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxNR-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python acp-txp-modacc-single-carrier.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxWLANSession'`

- `RESOURCE = 'SimulatedDevice'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxnr/modacc-noncontiguous-multicarrier.py -->
## PYTHON MODULE: examples/nirfmxnr/modacc-noncontiguous-multicarrier.py

### MODULE DOCSTRING

Fetch ACP, ModAcc, and TXP data.

Steps:
1. Open a new RFmx Session.
2. Configure Frequency Reference.
3. Configure Selected Ports.
4. Configure basic signal properties (Center Frequency, Reference Level and External Attenuation).
5. Configure Trigger Type and Trigger Parameters.
6. Configure Auto Increment Cell ID Enabled, Auto RB Detection Enabled and Number of Subblocks.
7. Configure Subblocks and Carriers.
8. Configure PUSCH for all Carriers in each Subblock.
9. Configure PUSCH DMRS for all Carriers in each Subblock.
10. Select ModAcc measurement and enable Traces.
11. Configure Synchronization Mode for ModAcc measurement.
12. Configure Measurement Interval.
13. Initiate the Measurement.
14. Fetch ModAcc Measurements.
15. Close RFmx Session.

The gRPC API is built from the C API. RFmx NR documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\NR\Documentation\rfmxnrcvi.chm

Getting Started:

To run this example, install "RFmx NR" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-nr.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxNR gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxNR-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python modacc-noncontiguous-multicarrier.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxWLANSession'`

- `RESOURCE = 'SimulatedDevice'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

- `NUMBER_OF_SUBBLOCKS = 2`

- `SUBBLOCK_FREQUENCY = [0, 200000000.0]`

- `NUMBER_OF_COMPONENT_CARRIERS = 2`

- `BAND = [78, 78]`

- `COMPONENT_CARRIER_SPACING_TYPE = [nirfmxnr_types.NIRFMXNR_INT32_COMPONENT_CARRIER_SPACING_TYPE_NOMINAL, nirfmxnr_types.NIRFMXNR_INT32_COMPONENT_CARRIER_SPACING_TYPE_NOMINAL]`

- `COMPONENT_CARRIER_AT_CENTER_FREQUENCY = [-1, -1]`

- `CHANNEL_RASTER = [15000.0, 15000.0]`

- `COMPONENT_CARRIER_BANDWIDTH = [[100000000.0, 100000000.0], [100000000.0, 100000000.0]]`

- `COMPONENT_CARRIER_FREQUENCY = [[-49980000.0, 49980000.0], [-49980000.0, 49980000.0]]`

- `CELL_ID = [[0, 1], [0, 1]]`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxnr/txp-single-carrier.py -->
## PYTHON MODULE: examples/nirfmxnr/txp-single-carrier.py

### MODULE DOCSTRING

Fetch TXP data.

Steps:
  1. Open a new RFmx Session.
  2. Configure Frequency Reference.
  3. Configure Selected Ports.
  4. Configure basic signal properties(Center Frequency, Reference Level and External Attenuation).
  5. Configure Trigger Parameters for Digital Edge Trigger.
  6. Configure Link Direction, Frequency Range, Carrier Bandwidthand Subcarrier Spacing.
  7. Select TXP measurement and enable Traces.
  8. Configure Measurement Offset & Measurement Length Parameters and Averaging Parameters for TXP
     measurement.
  9. Initiate the Measurement.
  10. Fetch TXP Measurements and Traces.
  11. Close RFmx Session.

The gRPC API is built from the C API. RFmx NR documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\NR\Documentation\rfmxnrcvi.chm

Getting Started:

To run this example, install "RFmx NR" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-nr.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxNR gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxNR-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python txp-single-carrier.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxNRSession'`

- `RESOURCE = 'SimulatedDevice'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxspecan/acp-basic.py -->
## PYTHON MODULE: examples/nirfmxspecan/acp-basic.py

### MODULE DOCSTRING

Fetch ACP data.

Steps:
  1. Open a new RFmx session
  2. Configure Selected Ports
  3. Configure the basic signal properties  (Center Frequency, Reference Level and External
     Attenuation)
  4. Configure ACP Averaging Parameters
  5. Configure ACP Integration BW, Number of Offset Channels and Channel Spacing
     This function configures a Carrier Channel with Offset Channels as specified by the Number of
     Offsets.
  6. Read ACP Measurement Results
     This function returns Absolute Power for the Carrier Channel and Relative Powers for two Offset
     Channels.
  7. Close the RFmx Session

The gRPC API is built from the C API. RFmx SpecAn documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\SpecAn\Documentation\rfmxspecancvi.chm

Getting Started:

To run this example, install "RFmx SpecAn" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-specan.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxSpecAn gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxSpecAn-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python acp-basic.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxSpecAnSession'`

- `RESOURCE = 'SimulatedDevice'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxspecan/spectrum-basic.py -->
## PYTHON MODULE: examples/nirfmxspecan/spectrum-basic.py

### MODULE DOCSTRING

Read a spectrum.

Steps:
  1. Open a new RFmx session
  2. Configure the basic signal properties  (Center Frequency, Reference Level and External
     Attenuation)
  3. Configure Spectrum Span
  4. Configure Spectrum RBW filter
  5. Configure Spectrum Averaging
  6. Read Spectrum Measurement Results
  7. Close the RFmx Session

The gRPC API is built from the C API. RFmx SpecAn documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\SpecAn\Documentation\rfmxspecancvi.chm

Getting Started:

To run this example, install "RFmx SpecAn" on the server machine:
  # https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-specan.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxSpecAn gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxSpecAn-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python spectrum-basic.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedRFSA" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'NI-RFSASession'`

- `RESOURCE = 'SimulatedRFSA'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

### `def _format_frequency(f)`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxspecan/txp-basic.py -->
## PYTHON MODULE: examples/nirfmxspecan/txp-basic.py

### MODULE DOCSTRING

Fetch TXP data.

Steps:
  1. Open a new RFmx session
  2. Configure Selected Ports
  3. Configure the basic signal properties  (Center Frequency, Reference Level and External
     Attenuation)
  4. Configure TXP rbw
  5. Configure TXP Measurement Interval
  6. Configure TXP Averaging
  7. Read TXP Measurement Results
  8. Close the RFmx Session

The gRPC API is built from the C API. RFmx SpecAn documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\SpecAn\Documentation\rfmxspecancvi.chm

Getting Started:

To run this example, install "RFmx SpecAn" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-specan.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxSpecAn gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxSpecAn-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python txp-basic.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxSpecAnSession'`

- `RESOURCE = 'SimulatedDevice'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxtdscdma/acp.py -->
## PYTHON MODULE: examples/nirfmxtdscdma/acp.py

### MODULE DOCSTRING

Acp example.

Steps:
1. Open a new RFmx session.
2. Configure Frequency Reference.
3. Configure External Attenuation.
4. Configure the Center Frequency directly or via Channel Number.
5. Configure Trigger Type and Trigger Parameters.
6. Configure the Reference Level directly or via Auto Level.
7. Select ACP measurement and enable traces.
8. Configure Averaging parameters.
9. Configure Sweep Time parameters.
10. Configure Noise Compensation parameter.
11. Configure Number of Offset Channels.
12. Initiate the Measurement.
13[A-E]. Fetch ACP Measurements and Traces.
14. Close the RFmx session.

The gRPC API is built from the C API. RFmx TDSCDMA documentation is installed with the driver at:
C:\Program Files (x86)\National Instruments\RFmx\TDSCDMA\Documentation\tdscdmacvi.chm

Getting Started:

To run this example, install "RFmx TDSCDMA" on the server machine.
Link: https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-tdscdma.html

For instructions on how to use protoc to generate gRPC client interfaces,
see our "Creating a gRPC Client" wiki page.
Link: https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxTDSCDMA gRPC Wiki for the latest C Function Reference:
Link: https://github.com/ni/grpc-device/wiki/NI-RFmxTDSCDMA-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python acp.py <server_address> <port_number> <physical_channel_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxTDSCDMASession'`

- `RESOURCE = 'SimulatedDevice'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

- `NUMBER_OF_OFFSETS = 2`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxtdscdma/modacc.py -->
## PYTHON MODULE: examples/nirfmxtdscdma/modacc.py

### MODULE DOCSTRING

ModAcc example.

Steps:
1. Open a new RFmx session.
2. Configure Frequency Reference.
3. Configure basic signal properties (Center Frequency, Reference Level and External Attenuation).
4. Configure Trigger Type and Trigger Parameters..
5. Select ModAcc measurement and enable traces.
6. Configure Uplink Scrambling Code.
7. Configure Synchronization Mode and Measurement Interval.
8. Configure Midamble Parameters.
9. Initiate the Measurement.
10. Fetch ModAcc Measurements and Traces.
11. Close the RFmx session.

The gRPC API is built from the C API. RFmx TDSCDMA documentation is installed with the driver at:
C:\Program Files (x86)\National Instruments\RFmx\TDSCDMA\Documentation\tdscdmacvi.chm

Getting Started:

To run this example, install "RFmx TDSCDMA" on the server machine.
Link: https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-tdscdma.html

For instructions on how to use protoc to generate gRPC client interfaces, see our
"Creating a gRPC Client" wiki page.
Link: https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxTDSCDMA gRPC Wiki for the latest C Function Reference:
Link: https://github.com/ni/grpc-device/wiki/NI-RFmxTDSCDMA-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python modacc.py <server_address> <port_number> <physical_channel_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxTDSCDMASession'`

- `RESOURCE = 'SimulatedDevice'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxwcdma/acp-single-carrier.py -->
## PYTHON MODULE: examples/nirfmxwcdma/acp-single-carrier.py

### MODULE DOCSTRING

Fetch ACP data.

Steps:
1. Open a new RFmx Session.
2. Configure Frequency Reference.
3. Configure basic signal properties (Center Frequency, RF Attenuation and External Attenuation)
4. Configure Trigger Type and Trigger Parameters.
5. Configure Reference Level.
6. Select ACP measurement and enable Traces.
7. Configure Measurement Method.
8. Configure Averaging Parameters for ACP measurement.
9. Configure Sweep Time Parameters.
10. Configure Noise Compensation Parameter.
11. Configure Number of offset channels.
12. Initiate the Measurement.
13. Fetch ACP Measurements and Traces.
14. Close RFmx Session.


The gRPC API is built from the C API. RFmx WCDMA documentation is installed with the driver at:
C:\Program Files (x86)\National Instruments\RFmx\WCDMA\Documentation\wcdmacvi.chm

Getting Started:

To run this example, install "RFmx WCDMA" on the server machine.
Link: https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-wcdma.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a
gRPC Client" wiki page.
Link: https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxWCDMA gRPC Wiki for the latest C Function Reference:
Link: https://github.com/ni/grpc-device/wiki/NI-RFmxWCDMA-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python acp-single-carrier.py <server_address> <port_number> <physical_channel_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxWCDMASession'`

- `RESOURCE = 'SimulatedDevice'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

- `NUMBER_OF_OFFSETS = 2`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxwcdma/modacc-single-carrier.py -->
## PYTHON MODULE: examples/nirfmxwcdma/modacc-single-carrier.py

### MODULE DOCSTRING

Fetch ModAcc data.

Steps:
1. Open a new RFmx Session.
2. Configure Frequency Reference.
3. Configure basic signal properties (Center Frequency, Reference Level and External Attenuation).
4. Configure Trigger Type and Trigger Parameters.
5. Configure Uplink Scrambling.
6. Select ModAcc measurement and enable Traces.
7. Configure Synchronization Mode and Measurement Interval.
8. Initiate the Measurement.
9. Fetch ModAcc Measurements and Traces.
10. Close RFmx Session.


The gRPC API is built from the C API. RFmx WCDMA documentation is installed with the driver at:
C:\Program Files (x86)\National Instruments\RFmx\WCDMA\Documentation\wcdmacvi.chm

Getting Started:

To run this example, install "RFmx WCDMA" on the server machine.
Link: https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-wcdma.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a
gRPC Client" wiki page.
Link: https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxWCDMA gRPC Wiki for the latest C Function Reference:
Link: https://github.com/ni/grpc-device/wiki/NI-RFmxWCDMA-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python RFmxWcdmaModAccSingleCarrier.c <server_address> <port_number> <physical_channel_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxWCDMASession'`

- `RESOURCE = 'SimulatedDevice'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxwlan/ofdm-modacc-evm-based-autolevel.py -->
## PYTHON MODULE: examples/nirfmxwlan/ofdm-modacc-evm-based-autolevel.py

### MODULE DOCSTRING

Fetch OFDM ModAcc data.

Steps:
  1. Open a new RFmx session.
  2. Configure the Frequency Reference properties (Clock Source and Clock Frequency).
  3. Configure the basic signal properties  (Center Frequency, Reference Level and External
     Attenuation).
  4. Configure IQ Power Edge Trigger properties (Trigger Delay, IQ Power Edge Level, Minimum Quiet
     Time).
  5. Configure Standard and Channel Bandwidth Properties.
  6. Select OFDMModAcc measurement and enable the traces.
  7. Configure the Measurement Interval.
  8. Configure Frequency Error Estimation Method.
  9. Configure Amplitude Tracking Enabled.
  10. Configure Phase Tracking Enabled.
  11. Configure Symbol Clock Error Correction Enabled.
  12. Configure Channel Estimation Type.
  13. Configure Averaging parameters.
  14. Perform EVM-based Auto Level
  15. Initiate Measurement.
  16. Fetch OFDMModAcc Measurements.
  17. Close the RFmx Session.

The gRPC API is built from the C API. RFmx WLAN documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\WLAN\Documentation\rfmxwlancvi.chm

Getting Started:

To run this example, install "RFmx WLAN" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-wlan.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxWLAN gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxWLAN-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python ofdm-modacc-evm-based_autoLevel.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxWLANSession'`

- `RESOURCE = 'SimulatedDevice'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxwlan/ofdm-modacc-txp-composite.py -->
## PYTHON MODULE: examples/nirfmxwlan/ofdm-modacc-txp-composite.py

### MODULE DOCSTRING

Fetch TXP and OFDM ModAcc data.

Steps:
  1. Open a new RFmx session.
  2. Configure the Frequency Reference properties (Clock Source and Clock Frequency).
  3. Configure the basic signal properties  (Center Frequency, Reference Level and External
     Attenuation).
  4. Configure IQ Power Edge Trigger properties (Trigger Delay, IQ Power Edge Level, Minimum Quiet
     Time).
  5. Configure Standard and Channel Bandwidth Properties.
  6. Select TXP and OFDMModAcc measurements and enable the traces.
  7. Configure the Measurement Interval.
  8. Configure Averaging.
  9. Configure Frequency Error Estimation Method.
  10. Configure Amplitude Tracking Enabled.
  11. Configure Phase Tracking Enabled.
  12. Configure Symbol Clock Error Correction Enabled.
  13. Configure Channel Estimation Type.
  14. Configure Averaging parameters.
  15. Initiate Measurement.
  16. Fetch TXP and OFDMModAcc Measurements.
  17. Close the RFmx Session.

The gRPC API is built from the C API. RFmx WLAN documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\WLAN\Documentation\rfmxwlancvi.chm

Getting Started:

To run this example, install "RFmx WLAN" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-wlan.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxWLAN gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxWLAN-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python ofdm-modacc-txp-composite.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxWLANSession'`

- `RESOURCE = 'SimulatedDevice'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxwlan/ofdm-modacc.py -->
## PYTHON MODULE: examples/nirfmxwlan/ofdm-modacc.py

### MODULE DOCSTRING

Fetch OFDM ModAcc data.

Steps:
  1. Open a new RFmx session.
  2. Configure the Frequency Reference properties (Clock Source and Clock Frequency).
  3. Configure the basic signal properties  (Center Frequency, Reference Level and External
     Attenuation).
  4. Configure IQ Power Edge Trigger properties (Trigger Delay, IQ Power Edge Level, Minimum Quiet
     Time).
  5. Configure Standard and Channel Bandwidth Properties.
  6. Select OFDMModAcc measurement and enable the traces.
  7. Configure the Measurement Interval.
  8. Configure Frequency Error Estimation Method.
  9. Configure Amplitude Tracking Enabled.
  10. Configure Phase Tracking Enabled.
  11. Configure Symbol Clock Error Correction Enabled.
  12. Configure Channel Estimation Type.
  13. Configure Averaging parameters.
  14. Initiate Measurement.
  15. Fetch OFDMModAcc Measurements.
  16. Close the RFmx Session.

The gRPC API is built from the C API. RFmx WLAN documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\WLAN\Documentation\rfmxwlancvi.chm

Getting Started:

To run this example, install "RFmx WLAN" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-wlan.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxWLAN gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxWLAN-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python ofdm-modacc.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxWLANSession'`

- `RESOURCE = 'SimulatedDevice'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxwlan/sem.py -->
## PYTHON MODULE: examples/nirfmxwlan/sem.py

### MODULE DOCSTRING

Fetch SEM data.

Steps:
  1. Open a new RFmx session.
  2. Configure the frequency reference properties (Clock Source and Clock Frequency).
  3. Configure the basic signal properties (Center Frequency and External Attenuation).
  4. Configure IQ Power Edge Trigger properties (Trigger Delay, IQ Power Edge Level, Minimum Quiet
     Time).
  5. Configure Standard and Channel Bandwidth Properties.
  6. Configure Reference Level.
  7. Select SEM measurement and enable the traces.
  8. Configure Averaging parameters.
  9. Configure Mask Type.
  10. Configure Sweep Time.
  11. Configure Span.
  12. Initiate the Measurement.
  13. Fetch SEM Measurements.
  14. Close the RFmx Session.

The gRPC API is built from the C API. RFmx WLAN documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\WLAN\Documentation\rfmxwlancvi.chm

Getting Started:

To run this example, install "RFmx WLAN" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-wlan.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxWLAN gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxWLAN-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python sem
  .py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxWLANSession'`

- `RESOURCE = 'SimulatedDevice'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfmxwlan/txp-basic.py -->
## PYTHON MODULE: examples/nirfmxwlan/txp-basic.py

### MODULE DOCSTRING

Fetch TXP data.

Steps:
  1. Open a new RFmx session.
  2. Configure the frequency reference properties (Clock Source and Clock Frequency).
  3. Configure the basic signal properties (Center Frequency and External Attenuation).
  4. Configure IQ Power Edge Trigger properties (Trigger Delay, IQ Power Edge Level, Minimum Quiet
     Time).
  5. Configure Standard and Channel Bandwidth Properties.
  6. Configure Reference Level.
  7. Select TXP measurement and enable the traces.
  8. Configure the Measurement Interval.
  9. Configure Averaging parameters.
  10. Initiate Measurement.
  11. Fetch TXP Traces and Measurements.
  12. Close the RFmx Session.

The gRPC API is built from the C API. RFmx WLAN documentation is installed with the driver at:
  C:\Program Files (x86)\National Instruments\RFmx\WLAN\Documentation\rfmxwlancvi.chm

Getting Started:

To run this example, install "RFmx WLAN" on the server machine:
  https://www.ni.com/en-us/support/downloads/software-products/download.rfmx-wlan.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFmxWLAN gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFmxWLAN-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python txp-basic.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedDevice" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'RFmxWLANSession'`

- `RESOURCE = 'SimulatedDevice'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

### `def check_for_warning(response, instrument)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfsa/getting-started-iq.py -->
## PYTHON MODULE: examples/nirfsa/getting-started-iq.py

### MODULE DOCSTRING

Configure I/Q parameters; read and print the I/Q data.

The following parameters of I/Q acquisition are configured:
 * reference clock, reference level, carrier frequency, I/Q rate, number of samples per record,
   and I/Q acquisition type.

The gRPC API is built from the C API. NI-RFSA documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niRFSA\documentation\English\nirfsa.chm

Getting Started:

To run this example, install "NI-RFSA Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-rfsa.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFSA gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFSA-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python getting-started-iq.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedRFSA" as the physical channel name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'NI-RFSA-Session'`

- `RESOURCE = 'SimulatedRFSA'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

- `NUMBER_OF_SAMPLES = 1000`

### `def check_for_warning(response, vi)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfsa/getting-started-spectrum.py -->
## PYTHON MODULE: examples/nirfsa/getting-started-spectrum.py

### MODULE DOCSTRING

Configure a spectrum acquisition.

The following parameters of the spectrum acquisition are configured:
 * reference clock source, reference level, start and stop frequencies, resolution bandwidth, and
   the spectrum acquisition type.

If you configure the spectrum span (Stop Frequency - Start Frequency) to a value larger than the
instantaneous bandwidth of the device, NI-RFSA performs multiple acquisitions and combines them into
one spectrum of the size you requested.

The gRPC API is built from the C API. NI-RFSA documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niRFSA\documentation\English\nirfsa.chm

Getting Started:

To run this example, install "NI-RFSA Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-rfsa.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFSA gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFSA-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python getting-started-spectrum.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedRFSA" as the physical channel name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'NI-RFSA-Session'`

- `RESOURCE = 'SimulatedRFSA'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5663'`

- `NUMBER_OF_SAMPLES = 1000`

### `def check_for_warning(response, vi)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfsg/attenuation-tables-generation.py -->
## PYTHON MODULE: examples/nirfsg/attenuation-tables-generation.py

### MODULE DOCSTRING

Download S-parameters from an attenuation per frequency table.

The code shows how to convert attenuation into simple s-parameter table to be used with RFSG.

The gRPC API is built from the C API. NI-RFSG documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niRFSG\documentation\English\RFSG.chm

Getting Started:

To run this example, install "NI-RFSG Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-rfsg.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFSG gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFSG-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python attenuation-tables-generation.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedRFSG" as the physical channel name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'NI-RFSG-Session'`

- `RESOURCE = '5840_1'`

- `OPTIONS = ''`

### `def raise_if_error(response)`

Raise an exception if an error was returned.

### `def raise_if_initialization_error(response)`

Raise an exception if an error was returned from Initialize.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfsg/generate-from-tdms.py -->
## PYTHON MODULE: examples/nirfsg/generate-from-tdms.py

### MODULE DOCSTRING

Generate a waveform from a TDMS file at a specified frequency and power.

The gRPC API is built from the C API. NI-RFSG documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niRFSG\documentation\English\RFSG.chm

Getting Started:

To run this example, install "NI-RFSG Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-rfsg.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFSG gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFSG-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python getting-started-single-tone-generation.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedRFSG" as the physical channel name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'NI-RFSG-Session'`

- `RESOURCE = 'SimulatedRFSG'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5652'`

- `FILE_PATH = 'C:/Users/Public/Documents/National Instruments/NI-RFSG/Examples/Waveforms/FileWithSingleWaveform.tdms'`

- `SCRIPT = 'script GenerateWfm repeat forever generate waveform marker0(0) end repeat end script'`

### `def check_for_warning(response, vi)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfsg/getting-started-single-tone-generation.py -->
## PYTHON MODULE: examples/nirfsg/getting-started-single-tone-generation.py

### MODULE DOCSTRING

Generate a single tone CW at a specified frequency and power.

The niRFSG_Abort function is used to quickly change from one configuration to another.

The gRPC API is built from the C API. NI-RFSG documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niRFSG\documentation\English\RFSG.chm

Getting Started:

To run this example, install "NI-RFSG Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-rfsg.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFSG gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFSG-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python getting-started-single-tone-generation.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedRFSG" as the physical channel name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'NI-RFSG-Session'`

- `RESOURCE = 'SimulatedRFSG'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5652'`

### `def check_for_warning(response, vi)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfsg/reference-clock.py -->
## PYTHON MODULE: examples/nirfsg/reference-clock.py

### MODULE DOCSTRING

Route the reference clock source during a simple sine wave generation.

The gRPC API is built from the C API. NI-RFSG documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niRFSG\documentation\English\RFSG.chm

Getting Started:

To run this example, install "NI-RFSG Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-rfsg.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFSG gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFSG-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python reference-clock.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedRFSG" as the physical channel name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'NI-RFSG-Session'`

- `RESOURCE = 'SimulatedRFSG'`

- `OPTIONS = 'Simulate=1,DriverSetup=Model:5652'`

### `def check_for_warning(response, vi)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nirfsg/rfsg-multitone-example.py -->
## PYTHON MODULE: examples/nirfsg/rfsg-multitone-example.py

### MODULE DOCSTRING

Generate any number and power of tones using RFSG.

At least one tone needs to be at 0 dB. Use Power level to set the power of all the tones relative to their selected power.
The minimum separation is mandated by a variable below. A smaller number needs more samples to meet the needs.
The maximum separation is mandated by the instrument used.

The gRPC API is built from the C API. NI-RFSG documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niRFSG\documentation\English\RFSG.chm

Getting Started:

To run this example, install "NI-RFSG Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-rfsg.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-RFSG gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-RFSG-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and physical channel name can be passed as separate
command line arguments.
  > python getting-started-single-tone-generation.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedRFSG" as the physical channel name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `SESSION_NAME = 'NI-RFSG-Session'`

- `RESOURCE = '5840_1'`

- `OPTIONS = ''`

### `def check_for_warning(response, vi)`

Print to console if the status indicates a warning.

### `class Tone()`

Class definition for tones.

    Define the tone with relative offset from the carrier frequency in Hz (relative to the
     generator center frequency).
    Relative power level in dBc (relative to the generator defined power level).
    

#### `def __init__(self, offset_hz, gain_db)`

Construct each tone using a relative offset in Hz and relative power in dBc.

#### `def __repr__(self)`

Make a string with Tones information.

### `def gcd(my_list)`

Return the greatest common denominator.

    Given a list of numbers find the smallest number that can divide them all.
    

<!--NI_PYTHON_API repo=grpc-device path=examples/niscope/fetch-continuous.py -->
## PYTHON MODULE: examples/niscope/fetch-continuous.py

### MODULE DOCSTRING

Initiate an acquisition and continuously fetches waveform samples per channel.

The gRPC API is built from the C API. NI-SCOPE documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niScope\Documentation\English\Digitizers.chm

A version of this .chm is available online at:
  https://zone.ni.com/reference/en-XX/help/370592AB-01/

Getting Started:

To run this example, install "NI-SCOPE Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-scope.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-SCOPE gRPC Wiki to determine the valid channel and resource names for your NI-SCOPE
module:
  https://github.com/ni/grpc-device/wiki/NI-SCOPE-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and resource name can be passed as separate command line
arguments.
  > python fetch-continuous.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedScope" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `RESOURCE = 'SimulatedScope'`

- `OPTIONS = 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe'`

- `CHANNELS = '0,1'`

- `TOTAL_ACQUISITION_TIME_IN_SECONDS = 10`

- `SAMPLE_RATE_IN_HZ = 1000`

### `def check_for_warning(response, vi)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/niscope/fetch.py -->
## PYTHON MODULE: examples/niscope/fetch.py

### MODULE DOCSTRING

Initiate an acquisition and fetch a waveform for each specified channel.

The gRPC API is built from the C API. NI-SCOPE documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niScope\Documentation\English\Digitizers.chm

A version of this .chm is available online at:
  https://zone.ni.com/reference/en-XX/help/370592AB-01/

Getting Started:

To run this example, install "NI-SCOPE Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-scope.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-SCOPE gRPC Wiki to determine the valid channel and resource names for your NI-SCOPE
module:
  https://github.com/ni/grpc-device/wiki/NI-SCOPE-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and resource name can be passed as separate command line
arguments.
  > python fetch.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedScope" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `RESOURCE = 'SimulatedScope'`

- `OPTIONS = 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe'`

- `CHANNELS = '0'`

### `def check_for_warning(response, vi)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/niscope/graph-measurement.py -->
## PYTHON MODULE: examples/niscope/graph-measurement.py

### MODULE DOCSTRING

Read waveforms from an NI-SCOPE device.

Tested with a 100 kHz tone input to channel 0.

The gRPC API is built from the C API. NI-SCOPE documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niScope\Documentation\English\Digitizers.chm

A version of this .chm is available online at:
  https://zone.ni.com/reference/en-XX/help/370592AB-01/

Getting Started:

To run this example, install "NI-SCOPE Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-scope.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-SCOPE gRPC Wiki to determine the valid channel and resource names for your NI-SCOPE
module:
  https://github.com/ni/grpc-device/wiki/NI-SCOPE-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and resource name can be passed as separate command line
arguments.
  > python graph-measurement.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedScope" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `RESOURCE = 'SimulatedScope'`

- `OPTIONS = 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe; MemorySize:1610612736'`

- `CHANNELS = '0'`

### `def check_for_warning(response, vi)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/niscope/plot-read-waveform.py -->
## PYTHON MODULE: examples/niscope/plot-read-waveform.py

### MODULE DOCSTRING

Continuously read and plot waveform data from an NI-SCOPE device.

The gRPC API is built from the C API. NI-SCOPE documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niScope\Documentation\English\Digitizers.chm

A version of this .chm is available online at:
  https://zone.ni.com/reference/en-XX/help/370592AB-01/

Getting Started:

To run this example, install "NI-SCOPE Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-scope.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-SCOPE gRPC Wiki to determine the valid channel and resource names for your NI-SCOPE
module:
  https://github.com/ni/grpc-device/wiki/NI-SCOPE-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and resource name can be passed as separate command line
arguments.
  > python plot-read-waveform.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedScope" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `RESOURCE = 'SimulatedScope'`

- `OPTIONS = 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe; MemorySize:1610612736'`

- `CHANNELS = '0'`

### `def check_for_warning(response, vi)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/niswitch/controlling-an-individual-relay.py -->
## PYTHON MODULE: examples/niswitch/controlling-an-individual-relay.py

### MODULE DOCSTRING

Control an individual relay on a module.

The gRPC API is built from the C API. NI-SWITCH documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niSwitch\Documentation\English\SWITCH.chm

A version of this .chm is available online at:
  https://zone.ni.com/reference/en-XX/help/375472H-01/

Getting Started:

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-SWITCH Help to determine topology, relay names, and resource names.

Refer to the NI-SWITCH gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-SWITCH-C-Function-Reference

Running from command line:

Server machine's IP address and port number can be passed as separate command line arguments.
  > python controlling-an-individual-relay.py <server_address> <port_number>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763".
To successfully run this example, the resource name, topology, and relay name must be hard coded
in this file.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `RESOURCE = ''`

- `TOPOLOGY_STRING = '2571/66-SPDT'`

- `RELAY_NAME = 'k15'`

- `SIMULATION = True`

- `MAX_DEBOUNCE_TIME = 1000`

- `SESSION_NAME = 'NI-Switch-Session-1'`

<!--NI_PYTHON_API repo=grpc-device path=examples/niswitch/software-scanning.py -->
## PYTHON MODULE: examples/niswitch/software-scanning.py

### MODULE DOCSTRING

Scan a series of channels on a module using software scanning.

The gRPC API is built from the C API. NI-SWITCH documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niSwitch\Documentation\English\SWITCH.chm

A version of this .chm is available online at:
  https://zone.ni.com/reference/en-XX/help/375472H-01/

Getting Started:

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-SWITCH Help to determine if your module supports scanning, the scan list syntax,
valid channel names and valid resource names.

Refer to the NI-SWITCH gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-SWITCH-C-Function-Reference

Running from command line:

Server machine's IP address and port numbercan be passed as separate command line arguments.
  > python software-scanning.py <server_address> <port_number>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763".
To successfully run this example, the resource name, topology, and scan list must be hard coded in
this file.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `RESOURCE = ''`

- `TOPOLOGY_STRING = '2529/2-Wire Dual 4x16 Matrix'`

- `SCAN_LIST = 'b0r1->b0c1;b0r1->b0c2;b0r2->b0c3'`

- `SIMULATION = True`

- `SESSION_NAME = 'NI-Switch-Session-1'`

### `def check_for_warning(response, vi)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nitclk/multi-device-configured-acquisition-tclk.py -->
## PYTHON MODULE: examples/nitclk/multi-device-configured-acquisition-tclk.py

### MODULE DOCSTRING

Read synchronized waveforms from multiple NI-SCOPE devices.

Tested with a 100 kHz tone input to channel 0.

The gRPC API is built from the C API. NI-SCOPE documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niScope\Documentation\English\Digitizers.chm

A version of this .chm is available online at:
  https://zone.ni.com/reference/en-XX/help/370592AB-01/

Getting Started:

To run this example, install "NI-SCOPE Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-scope.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-SCOPE gRPC Wiki to determine the valid channel and resource names for your NI-SCOPE
module:
  https://github.com/ni/grpc-device/wiki/NI-SCOPE-C-Function-Reference

Refer to the NI-TClk gRPC Wiki to determine the valid channel and resource names for your NI-TClk
module:
  https://github.com/ni/grpc-device/wiki/NI-TClk-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and multiple comma separated resource names can be
passed as separate command line arguments.
  > python multi-device-configured-acquisition-tclk.py <server_address> <port_number> <resource_name1,resource_name2>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedScope1" and "SimulatedScope2" as the resource names.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `OPTIONS = 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe;'`

- `RESOURCES = ['SimulatedScope1', 'SimulatedScope2']`

- `CHANNELS = '0'`

### `def check_for_scope_warning(response, vi)`

Print to console if the status indicates a warning.

### `def check_for_tclk_warning(response)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nitclk/synchronize-tclk.py -->
## PYTHON MODULE: examples/nitclk/synchronize-tclk.py

### MODULE DOCSTRING

Configure multiple NI Arbitrary Waveform Generators to generate synchronized waveforms.

The gRPC API is built from the C API. NI-FGEN documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niFgen\documentation\English\SigGenHelp.chm

NI-TClk documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niTClk\documentation\English\nitclk.chm

Getting Started:

To run this example, install "NI-FGEN Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-fgen.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Running from command line:

Server machine's IP address, port number, and multiple comma separated resource names can be
passed as separate command line arguments.
  > python synchronize-tclk.py <server_address> <port_number> <resource_name1,resource_name2>
This example is not supported in simulation mode, hence these arguments are mandatory.


- `SAMPLE_RATE = 20000000.0`

- `WAVEFORM_SIZE = 16`

- `WAVEFORM_DATA = [0.0 if i < WAVEFORM_SIZE // 2 else 1.0 for i in range(WAVEFORM_SIZE)]`

### `def check_for_tclk_warning(response)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nixnet/can-signal-single-point-output.py -->
## PYTHON MODULE: examples/nixnet/can-signal-single-point-output.py

### MODULE DOCSTRING

Write Signal Data.

 This example writes a signal value for 10 times.
 This is used to demonstrate a signal single point output session.
 This example uses hardcoded signal names that use the NIXNET_example database.
 To use your own database, you need to add an alias to your database file using the NI-XNET
 Database Editor and then modify the database name and signals used here.
 Also ensure that the transceivers are externally powered when using C Series modules.

The gRPC API is built from the C API. NI-XNET documentation is installed with the driver at:
  C:\Users\Public\Documents\National Instruments\NI-XNET\Documentation\NI-XNET Manual.chm
Getting Started:

To run this example, install "NI-XNET Driver" on the server machine:
  https://www.ni.com/en-in/support/downloads/drivers/download.ni-xnet.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI XNET gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-XNET-C-Function-Reference

Running from command line:
Server machine's IP address, port number, and interface name can be passed as separate command line
arguments.
  > python can-signal-single-point-output.py <server_address> <port_number> <interface_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763"


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `INTERFACE = 'CAN1'`

- `DATABASE = 'NIXNET_example'`

- `CLUSTER = 'CAN_Cluster'`

- `SIGNAL_LIST = 'CANEventSignal1,CANEventSignal2'`

- `NUM_SIGNALS = 2`

### `def check_for_warning(response)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nixnet/ethernet-frame-stream-input-reader.py -->
## PYTHON MODULE: examples/nixnet/ethernet-frame-stream-input-reader.py

### MODULE DOCSTRING

Reads all the frame on network.

  This example reads all the frames on the network and displays them.
  This is used to demonstrate a frame input stream session.
  Ensure that you have connected the selected interface to another Ethernet interface that is
  transmitting data.

The gRPC API is built from the C API. NI-XNET documentation is installed with the driver at:
  C:\Users\Public\Documents\National Instruments\NI-XNET\Documentation\NI-XNET Manual.chm

Getting Started:
To run this example, install "NI-XNET Driver" on the server machine:
  https://www.ni.com/en-in/support/downloads/drivers/download.ni-xnet.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI XNET gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-XNET-C-Function-Reference

Running from command line:
Server machine's IP address, port number, and interface name can be passed as separate command line
arguments.
  > python ethernet-frame-stream-input-reader.py <server_address> <port_number> <interface_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763"


- `CHOOSE_MONITOR_OR_ENDPOINT_TEXT = "\nPress 'm' followed by enter to configure the input stream session to use the monitor path to monitor all network traffic else press any other key followed by enter to use the endpoint path which filters traffic based on VLAN ID and priority. :"`

- `FRAME_CHECK_SEQUENCE_SIZE = 4`

- `MAX_ENET_FRAME_SIZE = 1518`

- `NUM_OF_FRAMES = 1`

- `MAX_PAYLOAD_PER_FRAME = MAX_ENET_FRAME_SIZE + FRAME_CHECK_SEQUENCE_SIZE`

- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `INTERFACE = 'ENET1'`

### `def check_for_error(status)`

Raise an exception if the status indicates an error.

### `def print_timestamp(timestamp)`

Print a timestamp to console.

### `def check_for_warning(response)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nixnet/flexray-signal-single-point-input.py -->
## PYTHON MODULE: examples/nixnet/flexray-signal-single-point-input.py

### MODULE DOCSTRING

Read Signal Data.

 This example reads a signal value for 10 times.
 This is used to demonstrate a signal single point input session.
 This example uses hardcoded signal names that use the NIXNET_example database.
 To use your own database, you need to add an alias to your database file using the NI-XNET
 Database Editor and then modify the database name and signals used here.
 Also ensure that the bus is properly terminated as this example does not enable the on-board
 termination.

The gRPC API is built from the C API. NI-XNET documentation is installed with the driver at:
  C:\Users\Public\Documents\National Instruments\NI-XNET\Documentation\NI-XNET Manual.chm

Getting Started:
To run this example, install "NI-XNET Driver" on the server machine:
  https://www.ni.com/en-in/support/downloads/drivers/download.ni-xnet.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI XNET gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-XNET-C-Function-Reference

Running from command line:
Server machine's IP address, port number, and interface name can be passed as separate command line
arguments.
  > python flexray-signal-single-point-input.py <server_address> <port_number> <interface_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763"


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `INTERFACE = 'FlexRay2'`

- `DATABASE = 'NIXNET_example'`

- `CLUSTER = 'FlexRay_Cluster'`

- `SIGNAL_LIST = 'FlexRayEventSignal1,FlexRayEventSignal2'`

- `NUM_SIGNALS = 2`

### `def check_for_warning(response)`

Print to console if the status indicates a warning.

<!--NI_PYTHON_API repo=grpc-device path=examples/nixnet/lin-signal-single-point-output.py -->
## PYTHON MODULE: examples/nixnet/lin-signal-single-point-output.py

### MODULE DOCSTRING

Write Signal Data.

 This example writes a signal value for 10 times.
 This is used to demonstrate a signal single point output session.
 This example uses hardcoded signal names that use the NIXNET_exampleLDF database.
 To use your own database, you need to add an alias to your database file using the NI-XNET
 Database Editor and then modify the database name and signals used here.
 Also ensure that the transceivers are externally powered when using C Series modules.

The gRPC API is built from the C API. NI-XNET documentation is installed with the driver at:
  C:\Users\Public\Documents\National Instruments\NI-XNET\Documentation\NI-XNET Manual.chm

Getting Started:
To run this example, install "NI-XNET Driver" on the server machine:
  https://www.ni.com/en-in/support/downloads/drivers/download.ni-xnet.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI XNET gRPC Wiki for the latest C Function Reference:
  https://github.com/ni/grpc-device/wiki/NI-XNET-C-Function-Reference

Running from command line:
Server machine's IP address, port number, and interface name can be passed as separate command line
arguments.
  > python lin-signal-single-point-output.py <server_address> <port_number> <interface_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763"


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `INTERFACE = 'LIN1'`

- `DATABASE = 'NIXNET_exampleLDF'`

- `CLUSTER = 'Cluster'`

- `SIGNAL_LIST = 'MasterSignal1_U16,MasterSignal2_U16'`

- `NUM_SIGNALS = 2`

### `def check_for_warning(response)`

Print to console if the status indicates a warning.

- `IS_MASTER = 1`

- `SCHEDULE_INDEX = 0`

<!--NI_PYTHON_API repo=grpc-device path=examples/session/session-reservation.py -->
## PYTHON MODULE: examples/session/session-reservation.py

### MODULE DOCSTRING

Initiate a session and exercise some common reservation operations on the session.

This particular example is using NI-SCOPE but the session reservation API should work for any driver
session.

The gRPC API is built from the C API. NI-SCOPE documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\IVI\Drivers\niScope\Documentation\English\Digitizers.chm

A version of this .chm is available online at:
  https://zone.ni.com/reference/en-XX/help/370592AB-01/

Getting Started:

To run this example, install "NI-SCOPE Driver" on the server machine:
  https://www.ni.com/en-us/support/downloads/drivers/download.ni-scope.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Refer to the NI-SCOPE gRPC Wiki to determine the valid channel and resource names for your NI-SCOPE
module:
  https://github.com/ni/grpc-device/wiki/NI-SCOPE-C-Function-Reference

Running from command line:

Server machine's IP address, port number, and resource name can be passed as separate command line
arguments.
  > python session-reservation.py <server_address> <port_number> <resource_name>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763", with "SimulatedScope" as the resource name.


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

- `RESOURCE = 'SimulatedScope'`

- `OPTIONS = 'Simulate=1, DriverSetup=Model:5164; BoardType:PXIe'`

- `CLIENT_1_ID = 'Client1'`

- `CLIENT_2_ID = 'Client2'`

<!--NI_PYTHON_API repo=grpc-device path=examples/session/session-utilities.py -->
## PYTHON MODULE: examples/session/session-utilities.py

### MODULE DOCSTRING

Commands that can get information about the server.

Getting Started:

To run this example, install NI System Configuration on the server machine:
  https://www.ni.com/en-in/support/downloads/drivers/download.system-configuration.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Running from the command line:

usage: session-utilities.py [-h]
                   [server_address] [port_number]
                   {enumerate-devices,enumerate-software} ...

positional arguments:
  server_address        The IP address or machine name of the server. The default is localhost.
  port_number           The port number of the server. The default is 31763.

optional arguments:
  -h, --help            show the help message and exit

subcommands:
  {enumerate-devices,enumerate-software}
    enumerate-devices   Prints the list of devices connected to the server.
    enumerate-software  Prints the list of NI software packages installed on the server.


### `def main(args)`

Open a connection to the server, then run the command specified in args.

### `def enumerate_devices(client)`

Retrieve and print a list of devices (simulated and physical) connected to the server.

### `def enumerate_software(client, show_hidden_packages)`

Retrieve and print a list of NI packages installed on the server.

### `def print_devices(devices)`

Print device info.

### `def print_software(software)`

Print software info.

<!--NI_PYTHON_API repo=grpc-device path=examples/visa/find-resources.py -->
## PYTHON MODULE: examples/visa/find-resources.py

### MODULE DOCSTRING

Perform continuous measure record.

The gRPC API is built from the C API. NI-VISA documentation is installed with the driver at:
  C:\Program Files (x86)\IVI Foundation\VISA\WinNT\NIvisa\ni-visa.chm

Getting Started:

To run this example, install "NI-VISA" on the server machine:
  https://www.ni.com/en/support/downloads/drivers/download.ni-visa.html

For instructions on how to use protoc to generate gRPC client interfaces, see our "Creating a gRPC
Client" wiki page:
  https://github.com/ni/grpc-device/wiki/Creating-a-gRPC-Client

Running from command line:

Server machine's IP address, port number, and resource name can be passed as separate command line
arguments.
  > python find-resources.py <server_address> <port_number>
If they are not passed in as command line arguments, then by default the server address will be
"localhost:31763".


- `SERVER_ADDRESS = 'localhost'`

- `SERVER_PORT = '31763'`

<!--NI_PYTHON_API repo=grpc-device path=source/codegen/__init__.py -->
## PYTHON MODULE: source/codegen/__init__.py

### MODULE DOCSTRING

Codegen package.

<!--NI_PYTHON_API repo=grpc-device path=source/codegen/client_helpers.py -->
## PYTHON MODULE: source/codegen/client_helpers.py

### MODULE DOCSTRING

Helpers for creating client .h/.cpp files.

### `class ParamMechanism(Enum)`

Enumeration of parameter mechanisms supported by client codegen.

- `PROTOBUF_PRIM_TYPES = ['bool', 'double', 'float']`

- `PROTOBUF_TYPE_TO_CPP_TYPE = {'double': 'double', 'float': 'float', 'int32': 'int32', 'int64': 'int64', 'uint32': 'uint32', 'uint64': 'uint64', 'sint32': 'int32', 'sint64': 'int64', 'fixed32': 'uint32', 'fixed64': 'uint64', 'sfixed32': 'int32', 'sfixed64': 'int64', 'bool': 'bool', 'string': 'string', 'bytes': 'string'}`

- `NIDEVICE_ENUMS = ['nidevice_grpc.SessionInitializationBehavior']`

### `def _to_parameter_for_list(client_param: ClientParam, for_header: bool) -> str`

### `def _to_parameter_list(client_params: List[ClientParam], for_header: bool) -> List[str]`

### `def stub_param() -> str`

Get the C++ stub parameter.

### `def create_streaming_params(client_params: List[ClientParam], for_header: bool) -> str`

Build the C++ parameter list for streaming functions.

### `def create_unary_params(client_params: List[ClientParam], for_header: bool) -> str`

Build the C++ parameter list for normal functions.

### `def _is_basic_type(grpc_type: str) -> bool`

### `def protobuf_namespace_alias() -> str`

Get the protobuf namespace alias.

### `def _get_cpp_client_param_type(param: dict, enums: dict) -> str`

### `def _get_cpp_type_for_protobuf_type(protobuf_type: str) -> str`

### `def _const_ref_t(t: str) -> str`

### `def _get_param_mechanism(param: dict) -> ParamMechanism`

### `def _get_param_default(param: dict) -> str`

### `def _create_client_param(param: dict, enums: dict) -> ClientParam`

### `def _is_grpc_array(param: dict) -> bool`

### `def stub_ptr_alias()`

Get the stub pointer alias.

### `def get_client_parameters(func: dict, enums: dict) -> List[ClientParam]`

Create a list of ClientParam objects for the given function.

### `def _split_types_from_variant(variant_type: str) -> Tuple[str, str]`

### `def get_enum_value_type(param: ClientParam) -> str`

Get the enum name of the given enum ClientParam.

### `def get_enum_raw_type(param: ClientParam) -> str`

Get the raw C++ value_type of the given enum ClientParam.

### `def streaming_response_type(response_type: str) -> str`

Wrap the given response type with a reader for streaming functions.

### `def filter_functions_to_include_in_client(functions: dict) -> dict`

Include only those functions which dont have 'include_in_client' tag in metadata.

<!--NI_PYTHON_API repo=grpc-device path=source/codegen/common_helpers.py -->
## PYTHON MODULE: source/codegen/common_helpers.py

### MODULE DOCSTRING

Common helpers.

- `_NIDEVICE_COMMON_MESSAGE_TYPES = ('nidevice_grpc.NIComplexNumber', 'nidevice_grpc.NIComplexNumberF32', 'nidevice_grpc.NIComplexI16', 'nidevice_grpc.SmtSpectrumInfo')`

- `_WELL_KNOWN_MESSAGE_TYPES = ('google.protobuf.Timestamp',)`

- `SPECIAL_CASE_PASCAL_TOKENS = [PascalTokenSubstitution('Uint', 'UInt')]`

### `def is_output_parameter(parameter)`

Whether the parameter is an output parameter.

### `def is_input_parameter(parameter)`

Whether the parameter is an input parameter.

### `def get_first_streaming_parameter(parameters: List[Dict]) -> Optional[Dict]`

Get the streaming parameter from the list of parameters.

### `def levels_of_pointer_indirection(parameter: dict) -> int`

Levels of pointer indirection for pointer. I.e. number of '*'s.

### `def is_repeated_varargs_parameter(parameter: dict)`

Whether the parameter is a repeated varargs parameter.

    This means the parameter follows a specific varargs convention where the user can pass in an
    arbitrary repetition of fixed arguments.
    

### `def is_proto_only_parameter(parameter: dict)`

Whether the parameter is only included in the proto file and not the driver API.

### `def is_repeating_parameter(parameter: dict)`

Whether the parameter is a repeating parameter.

    This means the parameter can be repeated as many times as desired. See also
    is_repeated_varargs_parameter().
    

### `def is_array(data_type: str)`

Whether the parameter is an array parameter.

### `def get_bitfield_enum_type(parameter: dict) -> str`

Get the enum type for a bitfield represented as an enum array.

### `def is_bitfield_as_enum_array(parameter: dict) -> bool`

Whether the parameter is a bitfield represented as an enum array.

### `def is_enum(parameter: dict)`

Whether the parameter's type is an enum.

### `def _is_custom_struct(parameter: dict) -> bool`

### `def uses_nidevice_common_message_types(config: dict, functions: dict) -> bool`

Whether a custom_type or function has any parameters whose type is a common nidevice type.

### `def _is_nidevice_common_message_type(parameter: dict) -> bool`

### `def _is_supported_well_known_type(parameter: dict) -> bool`

### `def is_struct(parameter: dict) -> bool`

Whether the parameter's type is a struct.

### `def is_driver_typedef_with_same_size_but_different_qualifiers(type: str) -> bool`

Whether the type has different per-platform qualifiers.

    Some of the drivers use different qualifiers for integers of same size on windows vs linux. We
    need to reinterpret_cast in the generated code to get the correct value.
    

### `def _has_copy_convert_tag(parameter)`

### `def supports_standard_copy_conversion_routines(parameter: dict) -> bool`

Whether the parameter can be converted with convert_from_grpc and convert_to_grpc.

### `def supports_standard_output_allocation_routines(parameter: dict) -> bool`

Whether the parameter can be allocated as an output param with allocate_output_storage.

### `def _any_function_uses_grpc_type(functions, type_name)`

### `def list_external_proto_dependencies(functions: dict) -> List[str]`

Return a list of external proto files required by the functions dictionary.

### `def get_custom_types(config: dict) -> List[Dict[str, Any]]`

Get the custom_types config setting.

### `def get_input_and_output_custom_types(config, functions)`

Return a set of custom types used by input and output parameters separately.

### `def _get_nested_types(config, type_name)`

### `def _is_null_terminated_in_c(parameter)`

### `def is_string_arg(parameter)`

Whether the parameter's type is string or bytes.

### `def is_nidevice_enum_parameter(grpc_type)`

Whether the grpc_type is one of the enums in nidevice_grpc.

### `def strip_repeated_from_grpc_type(grpc_type)`

Strip "repeated" from the grpc_type.

### `def get_underlying_type_name(parameter_type: str) -> str`

Get the underlying type name of the given type.

    Strip away information from type name like brackets for arrays, leading "struct ", etc. leaving
    just the underlying type name.
    

### `def _get_underlying_grpc_type_name(grpc_type: str) -> str`

### `def get_underlying_type(parameter_or_attribute: dict) -> str`

Get the underlying type name of the given parameter or attribute.

### `def _get_underlying_grpc_type(parameter: dict) -> str`

### `def has_unsupported_parameter(function)`

Whether the given function has a parameter that's not supported.

    Examples of unsupported parameters:
        * Parameters with an unsupported size mechanism
        * Output array parameters whose type is an enum whose underlying type is not a string or
          32-bit int
    

### `def _is_unsupported_parameter(parameter)`

### `def is_unsupported_size_mechanism(parameter: dict) -> bool`

Whether the parameter has a size that uses an unsupported mechanism.

### `def is_unsupported_size_mechanism_type(size_mechanism: str) -> bool`

Whether the given size mechanism is unknown/unsupported.

### `def _is_unsupported_scalar_array(parameter)`

### `def _is_unsupported_enum_array(parameter)`

### `def _is_supported_enum_array_output_type(parameter)`

### `def is_static_castable_enum_type(parameter)`

Whether the underlying type of the parameter's enum is static_castable.

### `def _normalize_special_pascal_tokens(pascal_or_camel_string: str) -> str`

### `def _insert_special_case_pascal_tokens(normal_pascal_string: str) -> str`

### `def _insert_leading_special_case_pascal_tokens(camel_string: str) -> str`

### `def _normalize_leading_special_case_pascal_tokens(pascal_string: str) -> str`

### `def _is_actually_pascal(camel_or_pascal_string: str) -> bool`

### `def camel_to_snake(camel_string: str) -> str`

Return a snake_string for a given camelString.

    External callers should use/create a wrapper instead (i.e. get_grpc_field_name).
    

### `def snake_to_pascal(snake_string)`

Return a PascalString for a given snake_string.

### `def _pascal_to_camel(pascal_string)`

Return a camelString for a given PascalString.

### `def ensure_pascal_case(pascal_or_camel_string)`

Ensure that a camel/pascal case string is pascal case.

    NOTE: does not distinguish leading all-caps acronyms.
    

### `def pascal_to_snake(pascal_string)`

Return a snake_string for a given PascalString.

### `def filter_proto_rpc_functions(functions)`

Return function metadata only for functions to include for generating proto rpc methods.

### `def filter_proto_rpc_functions_for_message(functions)`

Return function metadata only for functions to include for generating proto rpc messages.

### `def get_attribute_enums_by_type(attributes)`

Return a dict of attribute data types that use enum, along with set of enums used.

### `def get_function_enums(functions, enums: List[dict])`

Get a list of the enums used by functions.

### `def _get_force_include_enums(enums: List[dict])`

### `def has_viboolean_array_param(functions)`

Whether at least one function has parameter of type ViBoolean[].

### `def has_enum_array_string_out_param(functions)`

Whether at least one function has an output parameter that is a string-based enum.

### `def get_size_mechanism(parameter: dict) -> Optional[str]`

Get the size mechanism of the given parameter.

### `def get_size_param(parameter: dict) -> Optional[str]`

Get the size of the given parameter.

### `def _get_ivi_dance_twist_param_name(parameter: dict) -> Optional[str]`

### `def has_size_mechanism_tag(parameter: dict, tag: str) -> bool`

Whether the given parameter specifies a size mechanism.

### `def _has_strlen_bug(parameter: dict) -> bool`

Return whether the parameter is a string output whose size mechanism has the 'strlen bug'.

    Reports strlen instead of strlen + 1 for the required buffersize.

    We assume that this bug may some day be fixed, so the implementation needs to allocate the extra
    character but also trim it off if it's an extra null.
    

### `def has_optional_size_tag(parameter: dict) -> bool`

Whether the given parameter has a size mechanism tag "optional".

### `def get_buffer_size_expression(parameter: dict) -> str`

Return the C++ size expression for the underlying C API buffer for a string/array parameter.

    Unlike get_size_expression, this will include the trailing null terminator for strings (which is
    in the size reported by driver APIs).
    

### `def get_size_expression(parameter: dict) -> str`

Return the C++ size expression for sizing the C++ container type for a given parameter.

### `def _is_ivi_dance_array_param(parameter)`

### `def has_ivi_dance_param(parameters)`

Whether any parameter uses the ivi-dance size mechanism.

### `def is_two_dimension_array_param(parameter)`

Whether the given parameter is a two-dimensional array.

### `def has_two_dimension_array_param(parameters)`

Whether any parameter is a two-dimensional array.

### `def has_repeated_varargs_parameter(parameters)`

Whether any parameter is a repeated varargs parameter.

### `def can_mock_function(parameters)`

Whether a function with the given parameters can be mocked by googlemock.

    Google Mock can't handle the case where a function has a variable number of arguments and
    there's also a limit on the max number of arguments.
    

### `def get_ivi_dance_params(parameters)`

Get the relevant parameters for the first ivi-dance parameter, if any.

### `def is_ivi_dance_array_with_a_twist_param(parameter)`

Whether the given parameter is an ivi-dance-with-a-twist parameter.

### `def has_ivi_dance_with_a_twist_param(parameters)`

Whether any parameter is an ivi-dance-with-a-twist parameter.

### `def get_param_with_name(parameters: List[dict], name: str) -> dict`

Get the parameter that has the given name.

### `def get_first_session_param(parameters: List[dict]) -> dict`

Get the first parameter whose type is a Session.

### `class IviDanceWithATwistParamSet(NamedTuple)`

#### `def all_params(self)`

All parameters in the set.

#### `def size_param_name(self) -> str`

Size parameter.

#### `def twist_param_name(self) -> str`

Twist parameter.

#### `def is_in_out_twist(self) -> bool`

Return whether this is an "in-out" twist.

        An "in-out" twist is a rare variant of ivi-dance-with-a-twist where the size and the twist
        are the same param used as an in-out param, rather than separate input and output params.
        

### `def _make_ivi_twist_param_set(twist_param_name: str, parameters: List[dict]) -> IviDanceWithATwistParamSet`

### `def _unique_twist_params(parameters) -> List[str]`

### `def get_ivi_dance_with_a_twist_params(parameters: List[dict]) -> List[IviDanceWithATwistParamSet]`

Get the ivi-dance-with-a-twist parameters.

### `def get_params_not_in_ivi_twist(parameters: List[dict], ivi_param_sets: List[IviDanceWithATwistParamSet]) -> List[dict]`

Get the parameters that are not involved with an ivi-dance-with-a-twist mechanism.

### `def is_init_method(function_data)`

Whether the function is an init_method.

### `def _get_session_output_param(function_data)`

### `def is_init_array_method(function_data)`

Whether the function is an init_method with a repeated Session output parameter.

### `def is_cross_driver_init_method(function_data: dict) -> bool`

Whether the function is an init_method for a cross_driver_session.

### `def has_streaming_response(function_data)`

Whether the function has a stream_response.

### `def _has_callback_param(function_data)`

### `def has_async_streaming_response(function_data)`

Whether the function has an async stream_response.

### `def get_library_interface_type_name(config)`

Get the LibraryInterface type name, based on the service_class_prefix config setting.

### `def indent(level)`

For use as a mako filter.

    Returns a function that indents a block of text to the provided level.
    

### `def trim_trailing_comma()`

For use as a mako filter.

    Returns a function that removes the last comma from a block of text (preserves newlines).
    Consider this as an alternative to str.join when it allows preserving context in the mako file.
    

### `def os_conditional_compile_block(config)`

For use as a mako filter.

    That wraps a block of text in #if blocks based on the config's OS support.
    

### `def filter_parameters_for_grpc_fields(parameters_or_fields: List[dict])`

Filter out the parameters that shouldn't be represented by a field on a grpc message.

    For example, get rid of any parameters whose values should be determined from another parameter.
    

### `class AttributeGroup()`

#### `def __init__(self, name, attributes, config)`

#### `def get_attributes_split_by_sub_group(self)`

Split attributes by type, with an added "Reset" sub-group for resettable attributes.

### `def get_attribute_enum_suffix(config: dict) -> str`

Get the name suffix of the enum whose values are the attributes.

### `def get_attribute_enum_name(group_name: str, data_type: str, config: dict) -> str`

Get the name of the enum whose values are the attributes.

### `def get_attribute_groups(data)`

Get the attribute groups.

### `def strip_prefix(s: str, prefix: str) -> str`

Strip the given prefix, if present, and return the resulting string.

### `def strip_suffix(s: str, suffix: str) -> str`

Strip the given suffix, if present, and return the resulting string.

### `def _replace_prefix(s: str, prefix: str, sub: str) -> str`

### `def get_grpc_type_name_for_identifier(data_type, config)`

Create an identifier string based on the grpc_type.

    i.e., double -> Double. repeated double -> DoubleArray.
    

### `def _get_grpc_type_from_ivi(type: str, is_array: bool, driver_name_pascal: str, config: dict) -> str`

### `def get_grpc_type(data_type, config)`

Get the grpc_type for the given type.

### `def _use_legacy_attribute_prefix(config: dict) -> bool`

### `def get_split_attributes_by_type(config)`

Get the split_attributes_by_type config setting.

### `def supports_raw_attributes(config: dict) -> bool`

Get the supports_raw_attributes config setting.

### `def get_enum_value_cpp_type(enum: dict) -> str`

Use the python datatype of the first value in the enum to infer the C++ type.

    Used for mapped enums.
    

### `def is_regular_string_arg(parameter: dict) -> bool`

Return whether the parameter is a "regular" string.

    This excludes byte arrays.
    

### `def is_regular_byte_array_arg(parameter: dict) -> bool`

Return whether the parameter is a "regular" byte array.

    This excludes byte arrays that are mapped to enums.
    

### `def get_additional_headers(config: dict, including_from_file: str) -> List[str]`

Get the list of additional headers required by the given file.

### `def get_enum_value_prefix(enum_name: str, enum: dict) -> str`

Get the enum value prefix for the given enum.

### `def get_driver_readiness(config: dict) -> str`

Get the code_readiness config setting.

### `def is_driver_restricted(config: dict) -> str`

Get the is_restricted config setting.

### `def get_grpc_field_name(param: dict) -> str`

Get the name of the protobuf field for the given param.

    This will be a snake_case_string, that can be used in the proto
    definition itself, as well as in C++ code that accesses the field
    from a Request/Response message.
    

### `def get_grpc_client_field_name(param: dict) -> str`

Get the name of the protobuf field for the given param.

    This will be a snake_case_string, that can be used in the client generated files.
    

### `def get_grpc_field_name_from_str(field_name: str) -> str`

Get the default grpc_name for the given parameter name.

### `def get_cpp_local_name(param: dict) -> str`

Return a similar token to get_grpc_field_name, but ensure it is valid as a C++ variable name.

    NOTE: this is not used consistently to differentiate from get_grpc_field_name.  For that reason,
    the field respects the "grpc_name" override so that the two will match in the vast majority of
    cases where "name" is not a reserved keyword.  If "grpc_name" is a reserved keyword, this may be
    an issue (but don't use reserved grpc_name!).
    

### `def get_grpc_field_names_for_param_names(params: List[dict], names: List[str]) -> List[str]`

Get the grpc field name for the corresponding param in params given a list of names.

### `def is_return_value(parameter: dict) -> bool`

Whether the parameter is marked as a return_value.

### `def is_get_last_error_output_param(parameter: dict) -> bool`

Return True if parameter is a get_last_error parameter.

### `def is_optional_param(parameter: dict) -> bool`

Whether the parameter is marked is_optional.

### `def get_driver_api_params(parameters: List[dict]) -> List[dict]`

Return all parameters that are passed as parameters to the driver API.

    Excludes:
    * Return values.
    * Outputs that are calculated/populated after the API call.
    * Proto only params.
    

### `def get_params_needing_initialization(parameters: List[dict]) -> List[dict]`

Return all parameters that need to be initialized before the API call.

    Excludes:
    * Return values.
    * Outputs that are calculated/populated after the API call.
    

### `def filter_moniker_streaming_functions(functions: dict, functions_to_generate: List[str]) -> List[str]`

Return streaming functions that need to be generated.

### `def is_moniker_streaming_function(function: dict) -> bool`

Whether this function is for streaming data through moniker.

### `def get_data_moniker_function_name(function_name: str) -> str`

Return the corresponding moniker function name for the given C API function.

### `def get_data_moniker_struct_name(begin_function_name: str) -> str`

Return the Moniker function name.

    Input expected is Begin* streaming API name.
    

### `def get_data_moniker_request_message_type(begin_function_name: str) -> str`

Return the request message type for Moniker functions.

    Input expected is Begin* streaming API name.
    

### `def get_data_moniker_response_message_type(begin_function_name: str) -> str`

Return the response message type for Moniker functions.

    Input expected is Begin* streaming API name.
    

### `def get_data_moniker_function_parameters(function: dict) -> Tuple[List[dict], List[dict]]`

Return moniker function parameters split into input/output.

    Input expected is equivalent non-streaming function.
    Add a default "status" output parameter if there isn't one already.
    

### `def is_function_in_streaming_functions(function_name: str, streaming_functions_to_generate: List[str])`

Check if a function name is in the streaming functions to generate.

### `def _is_streaming_param_input_array(streaming_param: dict) -> bool`

Check if the streaming parameter is an input array.

### `def get_non_streaming_input_parameters(parameters: List[dict]) -> List[dict]`

Determine if a parameter should be passed from Begin streaming API to Moniker function.

### `def extend_input_params_with_size_params(input_parameters: List[dict], function_metadata: dict)`

Return the input_parameters list with size parameters added to it.

### `def has_value_converted_to_c_representation(parameters: List[dict], parameter: dict) -> bool`

Check if the parameter contains a casted name.

### `def get_value_converted_to_c_representation(parameters: List[dict], parameter: dict) -> str`

Get the casted name of the parameter.

<!--NI_PYTHON_API repo=grpc-device path=source/codegen/format_mi_metadata.py -->
## PYTHON MODULE: source/codegen/format_mi_metadata.py

### MODULE DOCSTRING

Script for formatting mi-driver metadata in same style as hapigen output.

### `class _Formatter(object)`

#### `def __init__(self)`

#### `def _set_formatter(self, obj, callback)`

#### `def _get_formatter(self, value)`

#### `def __call__(self, value, **args)`

#### `def _format_object(self, value, indent)`

#### `def _format_enum(self, value, indent)`

#### `def _format_dict(self, value, indent)`

#### `def _format_list(self, value, indent)`

#### `def _format_tuple(self, value, indent)`

### `def _format_mi_metadata(metadata_dir: str)`

<!--NI_PYTHON_API repo=grpc-device path=source/codegen/generate_server_capabilities.py -->
## PYTHON MODULE: source/codegen/generate_server_capabilities.py

### MODULE DOCSTRING

Service information generation.

### `def _generate_file(metadata_dir: Path, output_dir: Path) -> None`

<!--NI_PYTHON_API repo=grpc-device path=source/codegen/generate_service.py -->
## PYTHON MODULE: source/codegen/generate_service.py

### MODULE DOCSTRING

Service generation.

### `def _generate_service_file_with_mako(metadata, template, generated_file_suffix, gen_dir)`

### `def _generate_service_file(metadata, template_file_name, generated_file_suffix, gen_dir)`

### `def _generate_all(metadata_dir: str, gen_dir: str, validate_only: bool)`

<!--NI_PYTHON_API repo=grpc-device path=source/codegen/generate_shared_service_files.py -->
## PYTHON MODULE: source/codegen/generate_shared_service_files.py

### MODULE DOCSTRING

Shared service file generation.

### `def _generate_register_all_services(metadata_dir: Path, output_dir: Path) -> None`

<!--NI_PYTHON_API repo=grpc-device path=source/codegen/metadata_mutation.py -->
## PYTHON MODULE: source/codegen/metadata_mutation.py

### MODULE DOCSTRING

Metadata mutation.

- `RESERVED_WORDS = ['abstract', 'as', 'base', 'bool', 'break', 'byte', 'case', 'catch', 'char', 'checked', 'class', 'const', 'continue', 'decimal', 'default', 'delegate', 'do', 'double', 'else', 'enum', 'event', 'explicit', 'extern', 'false', 'finally', 'fixed', 'float', 'for', 'foreach', 'goto', 'if', 'implicit', 'in', 'int', 'interface', 'internal', 'is', 'lock', 'long', 'namespace', 'new', 'null', 'object', 'operator', 'out', 'override', 'params', 'private', 'protected', 'public', 'readonly', 'ref', 'return', 'sbyte', 'sealed', 'short', 'sizeof', 'stackalloc', 'static', 'string', 'struct', 'switch', 'this', 'throw', 'true', 'try', 'typeof', 'uint', 'ulong', 'unchecked', 'unsafe', 'ushort', 'using', 'virtual', 'void', 'volatile', 'while']`

- `KNOWN_COERCED_NARROW_NUMERIC_TYPES = ['int8', 'int8_t', 'uint8_t', 'int16', 'int16_t', 'uInt16', 'uint16_t']`

- `_ALREADY_MUTATED = ('NI-DCPower', 'NI-Digital Pattern Driver', 'NI-DMM', 'NI-FAKE', 'NI-FGEN', 'NI-SCOPE', 'NI-SWITCH', 'NI-TClk')`

### `def mutate(metadata: dict)`

Mutate the given metadata.

### `def generate_streaming_metadata(function: dict) -> dict`

Generate the streaming API metadata for a given function.

### `def sanitize_names(parameters)`

Sanitize name fields on a list of parameter objects.

    Also, populate the cppname field with the sanitized value.
    

### `def set_var_args_types(parameters, config)`

Set information about varargs parameters in the metadata.

### `def mark_size_params(parameters)`

Mark the size parameters in the metadata.

### `def mark_coerced_narrow_numeric_parameters(parameters: dict) -> None`

Mark parameters with narrow numeric types as coerced.

### `def mark_non_proto_params(parameters)`

Mark the parameters that shouldn't be included in the proto request message.

    Their values should be derived from other sources in the service handlers.
    

### `def _get_size_param(param, parameters)`

### `def mark_mapped_enum_params(parameters, enums)`

Mark enum paramaters as mapped-enum if the enum has mappings.

### `def populate_grpc_types(parameters, config)`

Set the grpc_type of each parameter that doesn't already have it set.

### `def set_grpc_type_for_custom_type_fields(fields, config)`

Set the grpc_type for each field of a custom type.

### `def _get_short_enum_type_name(typename: str) -> str`

### `def _remove_leading_group_name(enum_value_name, group_name)`

### `def _add_leading_enum_name(enum_value_name, enum_name, enum)`

### `def _add_attribute_values_enums(enums, attribute_enums_by_type, group_name)`

Add new enums to enums metadata, for use as the value parameter of SetAttribute APIs.

### `class AttributeAccessorExpander()`

Wraps an _attribute_type_map of: group -> type -> attributes.

    Also implements the metadata_mutations to _add_attribute_values_enums,
    _expand_attribute_function_value_param, and patch_attribute_enum_type.
    

#### `def __init__(self, metadata)`

#### `def _get_attribute_reference_parameter(self, parameters) -> Optional[AttributeReferencingParameter]`

Get the parameter that references an attribute, if there is one.

#### `def patch_attribute_enum_type(self, function_name, func)`

Update the attribute parameter to point to the proper enum name.

        Only applies for drivers that splits attribute enums by type.

        For example, DAQmx has a Get/Set/ResetBufferAttributeUInt32 functions. The parameter that
        selects _which_ attribute needs to use the proper attribute enum. The input says that the
        grpc_type is BufferAttribute, but the generated code splits the enums by type, with a
        special group for Reset functions. So in this example, the Get and Set functions' attribute
        enum would be BufferUInt32Attribute, and the Reset function's attribute enum would be
        BufferResetAttribute.
        

#### `def expand_attribute_value_params(self, func)`

Update the attrVal parameter to use the proper enum, if available.

### `def _expand_attribute_function_value_param(function, enums, attribute_enums_by_type, service_class_prefix)`

For SetAttribute and CheckAttribute, update function metadata to mark value param as enum.

### `def _get_attribute_function_value_param(function)`

### `def _get_attribute_values_enum_name(group_name, type, is_mapped=False)`

### `def _add_enum(enum_name, enum_values, enums, enum_value_prefix, is_mapped=False)`

### `def move_zero_enums_to_front(enums: dict) -> None`

Put the enum value with value 0 _first_ if there is one, or else add UNSPECIFIED enum value.

    protobuf requires that the first enum value be zero. For enums missing a zero value,
    we will add an UNSPECIFIED enum value to the front (this is the best practice). But if
    there already is a zero enum, make sure that pre-existing zero value is at the front.
    

### `def add_get_last_error_params_if_needed(function_data: Dict[str, Any], config: dict) -> None`

Add get_last_error parameters to the list if any are specified in config.

<!--NI_PYTHON_API repo=grpc-device path=source/codegen/metadata_validation.py -->
## PYTHON MODULE: source/codegen/metadata_validation.py

### MODULE DOCSTRING

Metadata validation.

- `_ALREADY_MUTATED = ('NI-DCPower', 'NI-Digital Pattern Driver', 'NI-DMM', 'NI-FAKE', 'NI-FGEN', 'NI-SCOPE', 'NI-SWITCH', 'NI-TClk')`

### `class RULES()`

Rules that can be suppressed.

- `DOCUMENTATION_SCHEMA = Schema({'description': str, Optional('python_description'): str, Optional('note'): str, Optional('table_body'): list, Optional('caution'): str})`

- `SIZE_SCHEMA = Schema({'mechanism': And(str, lambda s: not common_helpers.is_unsupported_size_mechanism_type(s)), 'value': Or(str, int), Optional('value_twist'): str, Optional('tags'): [str], Optional('python_value'): str})`

- `PARAM_SCHEMA = Schema({'direction': And(str, lambda s: s in ('in', 'out')), 'name': str, Optional('type'): str, Optional('grpc_type'): str, Optional('documentation'): DOCUMENTATION_SCHEMA, Optional('bitfield_as_enum_array'): str, Optional('enum'): str, Optional('size'): SIZE_SCHEMA, Optional('default_value'): Or(str, bool, int, float, None), Optional('is_repeated_capability'): bool, Optional('repeated_capability_type'): str, Optional('use_array'): bool, Optional('numpy'): bool, Optional('grpc_field_number'): And(str, Use(int)), Optional('grpc_raw_field_number'): And(str, Use(int)), Optional('grpc_mapped_field_number'): And(str, Use(int)), Optional('type_in_documentation'): str, Optional('include_in_proto'): bool, Optional('proto_only'): bool, Optional('is_session_handle'): bool, Optional('is_session_name'): bool, Optional('repeating_argument'): bool, Optional('python_api_converter_name'): str, Optional('attribute'): str, Optional('hardcoded_value'): str, Optional('is_compound_type'): bool, Optional('max_length'): int, Optional('repeated_var_args'): bool, Optional('pointer'): bool, Optional('coerced'): bool, Optional('callback_params'): [dict], Optional('callback_token'): bool, Optional('use_in_python_api'): bool, Optional('cross_driver_session'): str, Optional('cpp_local_name'): str, Optional('grpc_name'): str, Optional('return_value'): bool, Optional('supports_standard_copy_convert'): bool, Optional('supports_standard_output_allocation'): bool, Optional('get_last_error'): str, Optional('additional_arguments_to_copy_convert'): [str], Optional('additional_arguments_to_output_allocation'): [str], Optional('proto_only'): bool, Optional('input_passed_by_ptr'): bool, Optional('cppName'): str, Optional('determine_size_from'): [str], Optional('is_size_param'): bool, Optional('linked_params_are_optional'): bool, Optional('mapped-enum'): str, Optional('is_optional'): bool, Optional('is_optional_in_python'): bool, Optional('ctypes_data_type'): Or(str, None), Optional('has_explicit_buffer_size'): bool, Optional('is_list'): bool, Optional('python_data_type'): str, Optional('python_type_annotation'): str, Optional('python_description'): str, Optional('python_default_value'): Or(str, bool, int, float, None), Optional('is_grpc_enum'): bool, Optional('return_on_error_key'): str, Optional('is_streaming_type'): bool, Optional('value_converted_to_c_representation'): str})`

- `FUNCTION_SCHEMA = Schema({'parameters': [PARAM_SCHEMA], 'returns': str, Optional('cname'): str, Optional('codegen_method'): And(str, lambda s: s in ('public', 'private', 'CustomCode', 'no', 'python-only', 'CustomCodeCustomProtoMessage', 'CustomCodeNoLibrary')), Optional('python_codegen_method'): And(str, lambda s: s in ('CustomCode', 'no')), Optional('init_method'): bool, Optional('stream_response'): bool, Optional('is_error_handling'): bool, Optional('render_in_session_base'): bool, Optional('method_name_for_documentation'): str, Optional('use_session_lock'): bool, Optional('documentation'): DOCUMENTATION_SCHEMA, Optional('method_templates'): list, Optional('custom_close'): str, Optional('custom_close_method'): bool, Optional('python_name'): str, Optional('status_expression'): str, Optional('include_in_client'): bool, Optional('exclude_from_get_last_error'): bool, Optional('calling_convention'): str, Optional('python_class_name'): str, Optional('handle_parameter'): dict, Optional('adaptor_parameter'): dict, Optional('is_python_factory'): bool, Optional('python_description'): str, Optional('timeout_error'): str, Optional('supports_streaming'): bool, Optional('moniker_streaming_type'): str})`

- `ATTRIBUTE_SCHEMA = Schema({'name': str, Optional('access'): And(str, lambda s: s in ['read', 'read only', 'write', 'write only', 'read-write']), 'type': str, Optional('resettable'): bool, Optional('enum'): str, Optional('python_enum'): str, Optional('channel_based'): bool, Optional('attribute_class'): str, Optional('type_in_documentation'): str, Optional('documentation'): DOCUMENTATION_SCHEMA, Optional('lv_property'): str, Optional('repeated_capability_type'): str, Optional('python_type'): str, Optional('python_name'): str, Optional('codegen_method'): str, Optional('grpc_type'): str, Optional('c_function_name'): str, Optional('calling_convention'): str, Optional('bitfield_enum'): str, Optional('ctypes_data_type'): str, Optional('handle_parameters'): dict, Optional('python_object_constructor_params'): dict, Optional('has_explicit_read_buffer_size'): bool, Optional('python_object_has_factory'): bool, Optional('python_object_module_location'): str, Optional('python_object_type'): str, Optional('has_explicit_write_buffer_size'): bool, Optional('is_list'): bool, Optional('is_python_object'): bool, Optional('lv_filter'): list, Optional('python_class_name'): str, Optional('python_data_type'): str, Optional('python_description'): str})`

- `SIMPLE_ATTRIBUTE_SCHEMA = Schema({'name': str})`

- `ENUM_SCHEMA = Schema({Optional('python_name'): str, 'values': [{'name': str, 'value': Or(str, int, float), Optional('order'): int, Optional('python_name'): str, Optional('documentation'): DOCUMENTATION_SCHEMA, Optional('type'): str}], Optional('generate-mappings'): bool, Optional('enum-value-prefix'): str, Optional('generate-mapping-type'): bool, Optional('force-include'): bool, Optional('codegen_method'): str})`

### `def validate_metadata(metadata: dict)`

Validate the given metadata.

### `def _rule_is_suppressed(metadata: dict, rule: str, path: List[str]) -> bool`

### `def _parameter_name_exists(function: dict, name: str) -> bool`

### `def _validate_function(function_name: str, metadata: dict)`

### `def _validate_attribute(attribute: dict, metadata: dict)`

### `def _validate_enum(enum_name: str, used_enums: Set[str], metadata: dict)`

### `def _validate_parameter_size(parameter: dict, function_name: str, metadata: dict)`

### `def _get_attribute_enums(metadata: dict) -> Set[str]`

### `def _is_string_type(parameter: dict, metadata: dict) -> bool`

<!--NI_PYTHON_API repo=grpc-device path=source/codegen/proto_helpers.py -->
## PYTHON MODULE: source/codegen/proto_helpers.py

### MODULE DOCSTRING

Helpers for creating .proto files.

### `def _is_attribute_values(enum_name)`

### `def _should_add_unspecified_enum_value(enum_name, enum_values_metadata)`

Return whether an UNSPECIFIED zero-value enum should be added to enum_values_metadata.

    UNSPECIFIED zero-values are a best practice in protobuf. BUT they're not helpful if there
    is some other zero-value. In that case they introduce an unnecessary alias and don't serve
    their purpose of ensuring a neutral default value.

    AttributeValues are aggregate enums that maybe have multiple zero value enums that may not
    be at the front of the list (also a requirement for protobuf). They always get an UNSPECIFIED
    value.
    

### `def _should_allow_alias(enum_values_metadata)`

### `def generate_parameter_field_number(parameter, used_indexes, field_name_suffix='')`

Get unique field number for field corresponding to this parameter in proto file.

    If field number is not stored in metadata of parameter, get the next unused integer value.
    

### `def get_enum_definitions(enums_to_define, enums)`

Get a simplified definition for enums and the values in it.

    This is intended to be used for defining enums in the proto file.
    

### `def _is_array_input(parameter: dict)`

### `def _is_decomposable_enum(parameter: dict)`

Return whether the parameter is a decomposable enum.

    Enums are typically decomposed from a single param into an enum param and an _raw param.
    The exception is array_inputs which are left as single enum param.
    This is because protobuf does not support oneof on repeated types, so the standard input
    decomposition does not work for arrays.
    

### `def get_message_parameter_definitions(parameters)`

Get a simplified list of all parameters.

    This is intended to be used for defining requests/response messages in proto file.
    

### `def _get_enum_parameters(parameter, parameter_name, parameter_type, is_array, used_indexes)`

Get list of mapped/unmapped/raw parameters for enums as applicable.

### `def _get_parameter_type(parameter)`

### `def is_session_name(parameter)`

Whether the parameter is a session name parameter.

### `def _prepend_proto_only_session_name_parameter_if_necessary(func, input_parameters: List[dict]) -> None`

### `def get_parameters(function)`

Filter the parameters to ones we use in gRPC, and split into input/output parameters.

    Add a default "status" output parameter if there isn't one already.
    

### `def _get_callback_output_params(function)`

Look for a parameter that specifies callback_params and return those params.

    These will be used as the outputs of a streaming response.
    

### `def get_streaming_response_qualifier(function)`

Get a qualifier to add to the function's returned response object if it uses streaming.

<!--NI_PYTHON_API repo=grpc-device path=source/codegen/service_helpers.py -->
## PYTHON MODULE: source/codegen/service_helpers.py

### MODULE DOCSTRING

Helpers for creating service .h/.cpp files.

### `def get_include_guard_name(config, suffix)`

Get an appropriate #include guard name.

### `def get_c_element_type_for_array_that_needs_coercion(parameter)`

Get the C element type for the given parameter, if it's an array that needs coercion.

### `def get_c_element_type(parameter)`

Get the C element type for the given parameter.

### `def is_scalar_input_that_needs_coercion(parameter: dict) -> bool`

Whether the parameter is a scalar input that needs coercion.

### `def is_input_array_that_needs_coercion(parameter)`

Whether the parameter is an input array that needs coercion.

### `def _is_input_that_needs_coercion(parameter, custom_types: list)`

### `def is_output_array_that_needs_coercion(parameter)`

Whether the parameter is an output array that needs coercion.

### `def create_args_for_callback(parameters)`

Get the args needed for a CallbackRouter handler.

### `def _is_array_that_requires_conversion(parameter)`

Return whether the protobuf representation is not the same as the C API representation.

### `def _create_standard_arg(parameter)`

### `def create_args(parameters)`

Get the args needed to call the library function.

### `def create_args_for_ivi_dance(parameters)`

Get the args needed to call the ivi-dance library function.

### `def create_args_for_ivi_dance_with_a_twist(parameters)`

Get the args needed to call the ivi-dance-with-a-twist library function.

### `def create_params(parameters, expand_varargs=True)`

Get the params needed for defining the library function.

### `def _get_array_param_size(parameter) -> str`

### `def expand_varargs_parameters(parameters)`

Get a modified list of parameters, with repeating_parameters repeated max_length times.

    The max_length value comes from the first repeated_var_args parameter. Each repeated parameter
    gets a number (starting at zero) appended to the parameter name.
    

### `def _create_param(parameter, expand_varargs=True, repeated_parameters=None)`

### `def _format_value(value)`

### `def get_input_lookup_values(enum_data)`

Get an initializer list for a std::map that maps enum value index to enum value value.

### `def get_output_lookup_values(enum_data)`

Get an initializer list for a std::map that maps enum value value to enum value index.

### `def generate_enum_oneof_selector_map(enum_data)`

 "Get an initializer list for a std::map that maps enum value value to enum value type.

### `def filter_api_functions(functions, only_mockable_functions=True)`

Filter function metadata to only include those to be generated into the API library.

### `def filter_proto_rpc_functions_to_generate(functions)`

Return function metadata only for functions to include for generating proto rpc methods.

### `def get_cname(functions, method_name, c_function_prefix)`

Get the C name of the function.

### `def is_private_method(function_data)`

Whether the function is private.

### `def is_custom_close_method(function_data)`

Whether the function is a custom_close_method.

### `def requires_checked_conversion(parameters, custom_types)`

Whether any parameter needs coercion.

### `def get_request_param(method_name)`

Get a parameter for taking in a Request object for the function with the given name.

### `def get_request_type(method_name)`

Get the name of the Request class for the function with the given name.

### `def get_response_param(method_name)`

Get a parameter for taking in a Response object for the function with the given name.

### `def get_response_type(method_name)`

Get the name of the Response class for the function with the given name.

### `def get_async_functions(functions)`

Filter the functions to include only async functions (those with a streaming response).

### `def get_functions_with_two_dimension_param(functions)`

Filter the functions to include only those with a two-dimension array parameter.

### `def get_callback_method_parameters(function_data)`

Get the parameters of the given function's callback function parameter.

### `def create_param_type_list(parameters)`

Get a comma-separated list of parameter types.

### `def get_feature_toggles(config: dict) -> Dict[str, str]`

Get the feature_toggles config setting.

### `def get_toggle_member_name(fully_qualified_toggle_name: str) -> str`

Get the member name to use for the given toggle, in the FeatureToggles class.

### `def get_driver_service_readiness(config: dict) -> str`

Get the C++ constant representing the driver's code_readiness.

### `def is_restricted_driver_service(config)`

Whether the driver service is restricted.

### `def to_cpp_readiness(user_readiness: str) -> str`

Get the C++ constant representing the given code_readiness.

### `def get_enums_to_map(functions: dict, enums: dict) -> List[str]`

Get a list of the enums used by functions, for which mappings should be generated.

### `def generate_mapping_enums_to_type(enums: dict) -> List[str]`

Get a list of the enums used by functions, for which mappings should be generated.

### `def get_distinct_types_from_enums(enums: dict) -> str`

Return a comma seperated string of different data types used in enums value type field.

### `def get_bitfield_value_to_name_mapping(parameter: dict, enums: dict) -> Dict[int, str]`

Get a mapping from bitfield values to the corresponding C++ enum value constants.

### `def get_resource_handle_types(config: dict) -> List[str]`

Get the resource_handle_type config setting.

### `def _get_shared_resource_repository_ptr_type(resource_handle_type: str) -> str`

### `class CrossDriverSessionDependency(NamedTuple)`

### `def get_driver_shared_resource_repository_ptr_deps(driver_config: dict, functions: dict) -> SessionRepositoryHandleTypeDependencyMap`

Get handle-type to CrossDriverSessionDependency map used by this driver.

    Combine resource_handle_type and cross_driver_session types in single map since both
    of them together decide repositories required by driver. Combining into single map also
    helps remove duplicates.
    

### `def _create_cross_driver_session_dependency(resource_handle_type: str) -> CrossDriverSessionDependency`

### `def _get_cross_driver_session_type(parameter: dict) -> Optional[str]`

### `def get_cross_driver_session_dependencies(functions: dict) -> List[CrossDriverSessionDependency]`

Get a list of cross-driver session dependencies needed by any function parameter.

### `def get_cross_driver_session_dependency(parameter: dict) -> CrossDriverSessionDependency`

Get the cross-driver session dependency needed by the given parameter.

### `def session_repository_field_name(param: dict, config: dict) -> str`

Get the name of the session repository field used for the given parameter.

### `def list_session_repository_handle_types(driver_configs: List[dict]) -> SessionRepositoryHandleTypeMap`

Get per-handle type config info, for the resource handle types used by the given configs.

    The included config info keys are: local_name and windows_only.
    

### `def get_function_return_type(function_data: dict) -> str`

Get the return type for function_data.

### `def _get_return_value_parameter(parameters: List[dict]) -> Optional[dict]`

### `def get_return_value_name(function_data: dict) -> str`

Get the name of the return value for function_data. The default is "status".

### `def has_status_expression(function_data: dict) -> bool`

Whether function_data has a custom status_expression.

### `def get_status_expression(function_data: dict) -> str`

Get the custom status_expression for function_data.

    The default is to use the value of status returned from the driver function.

    Raises if "status_expression" is not present.
    

### `def get_library_ptr_for_potentially_unmockable_function(config: dict, parameters: List[dict])`

Get the variable or expression for the library pointer.

    Returns library_ if parameters can be mocked and called through the shared interface,
    otherwise typecasts library to the concrete type.
    

### `def is_session_returned_from_function(parameters: List[dict]) -> bool`

Whether parameters includes a return_value parameter with grpc_type nidevice_grpc.Session.

### `def should_copy_to_response(parameter: dict) -> bool`

Whether the value of parameter should be copied to the Response message.

### `def is_size_param_passed_by_ptr(parameter: dict) -> bool`

Return whether parameters is a size param passed-by-pointer.

### `def get_last_error_output_params(parameters: List[dict]) -> List[dict]`

Return list of get_last_error parameters.

### `def get_protobuf_cpplib_type(grpc_type: str) -> str`

Return the C++ type used grpc generated code for the given protobuf type.

    Note: this implementation is incomplete. It only handles the default case
    where the grpc_type name is the same as the cpplib typename and repeated
    message types. Add other mappings as needed.
    

<!--NI_PYTHON_API repo=grpc-device path=source/codegen/stage_client_files.py -->
## PYTHON MODULE: source/codegen/stage_client_files.py

### MODULE DOCSTRING

Stage client files.

### `class _ArtifactReadiness()`

Class to determine whether a Path with a module-named artifact directory is release-ready.

#### `def __init__(self, metadata_dir: Path, ignore_release_readiness: bool)`

#### `def is_release_ready(self, module_path: Path) -> bool`

Determine release-readiness.

        Do so by checking the name of the module_path directory against code_readiness for the
        module_name in config.py.
        

#### `def get_release_ready_subdirs(self, directory: Path) -> Iterable[Path]`

Return all subdirectories of directory for which is_release_ready is True.

### `class _ArtifactLocations()`

#### `def __init__(self, repo_root: Path)`

#### `def examples(self) -> Path`

#### `def generated_files(self) -> Path`

#### `def shared_imported_protos(self) -> Path`

#### `def shared_source_protos(self) -> Path`

#### `def restricted_protos(self) -> Path`

#### `def grpcdevice_protos(self) -> Path`

#### `def protobuftypes_protos(self) -> Path`

#### `def metadata_dir(self) -> Path`

#### `def config_dir(self) -> Path`

### `def _get_release_proto_files(artifact_locations: _ArtifactLocations, readiness: _ArtifactReadiness) -> List[Path]`

### `def _get_release_example_directories(artifact_locations: _ArtifactLocations, readiness: _ArtifactReadiness) -> Iterable[Path]`

### `def stage_client_files(output_path: Path, ignore_release_readiness: bool)`

Stage the client files into the given output path.

<!--NI_PYTHON_API repo=grpc-device path=source/codegen/template_helpers.py -->
## PYTHON MODULE: source/codegen/template_helpers.py

### MODULE DOCSTRING

Helpers for mako templates.

### `def instantiate_mako_template(template_file_name: str) -> Template`

Instantiate the mako template in the given file.

### `def write_if_changed(output_file_path: Union[Path, str], new_contents: str) -> None`

Write new_contents to output_file_path if new_contents != the contents of output_file_path.

    This prevents downstream recompiles when codegen runs but does not change a given file.
    

### `def load_metadata(metadata_dir: Union[Path, str]) -> dict`

Load the metadata from the given directory.

### `def _read_file_contents(output_file_path: Union[Path, str]) -> str`

<!--NI_PYTHON_API repo=grpc-device path=source/codegen/validate_examples.py -->
## PYTHON MODULE: source/codegen/validate_examples.py

### MODULE DOCSTRING

Script for validating the examples.

### `class _CommandRecord(NamedTuple)`

- `_FAILED_COMMANDS = []`

### `def _system(command)`

Capture the result of any failed system calls in _FAILED_COMMANDS.

### `def _create_stage_dir(staging_dir)`

### `def _stage_client_files(artifact_location: Optional[str], staging_dir: Path) -> None`

### `def _validate_examples(driver_glob_expression: str, exclude: str, ip_address: str, device_name: str, artifact_location: Optional[str]) -> None`

<!--NI_PYTHON_API repo=grpc-device path=source/codegen/validate_imported_protos.py -->
## PYTHON MODULE: source/codegen/validate_imported_protos.py

### MODULE DOCSTRING

Script validating that any imported proto file matches its corresponding generated one.

Expects import path as source/codegen/metadata and generated folder path.

Background:
All MI driver metadata is being imported from hapigen. We're also creating .proto files
based on the metadata in that component. So when an MI driver is updated, the export will have
a metadata folder with [attributes.py, config.py, enums.py, functions.py, <driver-name>.proto].
Someone will import those five files to grpc-device's source/codegen/metadata folder.

Purpose:
Since, at the moment, we have both grpc-device and hapigen generating the driver .proto files
we want a way to validate that they're creating equivalent ones. This script will check imported
.proto files (copied out of hapigen-based driver exports) against their corresponding .proto file
that gets generated in grpc-device to make sure they match.

On Mismatch:
1. Make sure .proto from driver export is copied over to grpc-device
2. Make sure you built grpc-device locally to get any generated folder changes
   (specifically .proto files there)
3. The proto generators (mako and helper python files) likely changed between grpc-device and
   hapigen and need to be synced up.


### `def _check_mismatched_protos(imported: str, generated: str)`

<!--NI_PYTHON_API repo=grpc-device path=source/codegen/validate_linux_rt.py -->
## PYTHON MODULE: source/codegen/validate_linux_rt.py

### MODULE DOCSTRING

Script for validating if a set of changed files warrants updating the Linux RT Feed.

Expects output of git diff --name-only <last-release-commit> <current-commit>
to be piped in so it can be read from sys.stdin


### `def _get_codegen_changes(changed_files: Set[str]) -> Set[str]`

### `def _get_test_changes(changed_files: Set[str]) -> Set[str]`

### `def _get_import_changes(changed_files: Set[str]) -> Set[str]`

### `def _get_markdown_changes(changed_files: Set[str]) -> Set[str]`

### `def _get_non_rt_driver_changes(driver_name: str, changed_files: Set[str]) -> Set[str]`

### `def _need_linux_rt_feed_update(metadata_dir: str, changed_files: Set[str]) -> bool`

### `def _print_changed_files(title: str, changed_files: Set[str])`
