# NI PYTHON API DIGEST: nidaqmx-python

<!--NI_PYTHON_API_SNAPSHOT repo=ni/nidaqmx-python commit=03282e1b5c741b9f37e4a4e1b5de3a52ae72442e -->

<!--NI_PYTHON_API repo=nidaqmx-python path=docs/conf.py -->
## PYTHON MODULE: docs/conf.py

### MODULE DOCSTRING

Sphinx Configuration File.

<!--NI_PYTHON_API repo=nidaqmx-python path=examples/analog_in/ai_multi_task_pxie_ref_clk.py -->
## PYTHON MODULE: examples/analog_in/ai_multi_task_pxie_ref_clk.py

### MODULE DOCSTRING

Example of AI multitask operation.

<!--NI_PYTHON_API repo=nidaqmx-python path=examples/analog_in/ai_raw.py -->
## PYTHON MODULE: examples/analog_in/ai_raw.py

### MODULE DOCSTRING

Example of AI raw operation.

<!--NI_PYTHON_API repo=nidaqmx-python path=examples/analog_in/calculated_power_acq_int_clk.py -->
## PYTHON MODULE: examples/analog_in/calculated_power_acq_int_clk.py

### MODULE DOCSTRING

Example of analog input calculated power acquisition.

This example demonstrates how to acquire a finite amount
of calculated power data using the DAQ device's internal clock.

Supported Devices:

- PXIe-4311 (DAQmx 26.3.0 or later)


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/analog_in/cont_calculated_power_acq_int_clk.py -->
## PYTHON MODULE: examples/analog_in/cont_calculated_power_acq_int_clk.py

### MODULE DOCSTRING

Example of analog input calculated power acquisition.

This example demonstrates how to acquire a continuous amount of
calculated power data using the DAQ device's internal clock.

Supported Devices:

- PXIe-4311 (DAQmx 26.3.0 or later)


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/analog_in/cont_thrmcpl_samples_int_clk.py -->
## PYTHON MODULE: examples/analog_in/cont_thrmcpl_samples_int_clk.py

### MODULE DOCSTRING

Example of continuous temperature acquisition.

This example demonstrates how to make continuous, hardware-timed
temperature measurement using a thermocouple.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/analog_in/cont_voltage_acq_int_clk.py -->
## PYTHON MODULE: examples/analog_in/cont_voltage_acq_int_clk.py

### MODULE DOCSTRING

Example of analog input voltage acquisition.

This example demonstrates how to acquire a continuous amount of data
using the DAQ device's internal clock.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/analog_in/cont_voltage_acq_int_clk_dig_start.py -->
## PYTHON MODULE: examples/analog_in/cont_voltage_acq_int_clk_dig_start.py

### MODULE DOCSTRING

Example of analog input voltage acquisition with a digital start trigger.

This example demonstrates how to acquire a continuous amount of
data using an external sample clock, started by a digital edge.


### `def main()`

Continuously acquires data started by a digital edge.

<!--NI_PYTHON_API repo=nidaqmx-python path=examples/analog_in/cont_voltage_acq_int_clk_dig_start_retrig.py -->
## PYTHON MODULE: examples/analog_in/cont_voltage_acq_int_clk_dig_start_retrig.py

### MODULE DOCSTRING

Example of analog input voltage acquisition with retriggering.

This example demonstrates how to acquire finite amounts of data
on each digital trigger.


### `def main()`

Acquires data on each digital trigger.

<!--NI_PYTHON_API repo=nidaqmx-python path=examples/analog_in/cont_voltage_acq_int_clk_every_n_samples_event.py -->
## PYTHON MODULE: examples/analog_in/cont_voltage_acq_int_clk_every_n_samples_event.py

### MODULE DOCSTRING

Example of analog input voltage acquisition with events.

This example demonstrates how to use Every N Samples events to
acquire a continuous amount of data using the DAQ device's
internal clock. The Every N Samples events indicate when data is
available from DAQmx.


### `def main()`

Continuously acquires data using an Every N Samples event.

<!--NI_PYTHON_API repo=nidaqmx-python path=examples/analog_in/thrmcpl_sample.py -->
## PYTHON MODULE: examples/analog_in/thrmcpl_sample.py

### MODULE DOCSTRING

Example of analog input temperature acquisition.

This example demonstrates how to acquire thermocouple measurement using
software timing.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/analog_in/voltage_acq_int_clk.py -->
## PYTHON MODULE: examples/analog_in/voltage_acq_int_clk.py

### MODULE DOCSTRING

Example of analog input voltage acquisition.

This example demonstrates how to acquire a finite amount
of data using the DAQ device's internal clock.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/analog_in/voltage_acq_int_clk_dig_ref.py -->
## PYTHON MODULE: examples/analog_in/voltage_acq_int_clk_dig_ref.py

### MODULE DOCSTRING

Example of analog input voltage acquisition with reference trigger.

This example demonstrates how to acquire a finite amount of data
using a digital reference trigger.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/analog_in/voltage_acq_int_clk_dig_start_ref.py -->
## PYTHON MODULE: examples/analog_in/voltage_acq_int_clk_dig_start_ref.py

### MODULE DOCSTRING

Example of analog input voltage acquisition with digital start and reference trigger.

This example demonstrates how to acquire a finite amount of data
using an internal clock and a digital start and reference
trigger.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/analog_in/voltage_acq_int_clk_plot_data.py -->
## PYTHON MODULE: examples/analog_in/voltage_acq_int_clk_plot_data.py

### MODULE DOCSTRING

Example of generating visualizations for acquired data.

This example demonstrates how to plot the acquired data.
This example requires the matplotlib module.
Run 'pip install matplotlib' to install the matplotlib module.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/analog_in/voltage_acq_int_clk_plot_wfm.py -->
## PYTHON MODULE: examples/analog_in/voltage_acq_int_clk_plot_wfm.py

### MODULE DOCSTRING

Example of generating visualizations for acquired data using the AnalogWaveform data type.

This example demonstrates how to plot the acquired waveform data.
This example requires the matplotlib module.
Run 'pip install matplotlib' to install the matplotlib module.


### `def plot_analog_waveform(waveform, min_start_time=None)`

Plot a single analog waveform.

<!--NI_PYTHON_API repo=nidaqmx-python path=examples/analog_in/voltage_acq_int_clk_tdms_logging.py -->
## PYTHON MODULE: examples/analog_in/voltage_acq_int_clk_tdms_logging.py

### MODULE DOCSTRING

Example of logging acquired data to TDMS file and read back.

This example demonstrates how to log the acquired data to a TDMS file
and then read the data from the file.
This example requires the nptdms module.
Run 'pip install nptdms' to install the nptdms module.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/analog_in/voltage_acq_int_clk_wfm.py -->
## PYTHON MODULE: examples/analog_in/voltage_acq_int_clk_wfm.py

### MODULE DOCSTRING

Example of analog input voltage waveform acquisition.

This example demonstrates how to acquire a finite amount
of data using the DAQ device's internal clock.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/analog_in/voltage_sample.py -->
## PYTHON MODULE: examples/analog_in/voltage_sample.py

### MODULE DOCSTRING

Example of analog input voltage acquisition.

This example demonstrates how to acquire a voltage measurement using software timing.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/analog_out/cont_gen_voltage_wfm_int_clk.py -->
## PYTHON MODULE: examples/analog_out/cont_gen_voltage_wfm_int_clk.py

### MODULE DOCSTRING

Example of analog output voltage generation.

This example demonstrates how to output a continuous periodic
waveform using an internal sample clock.


### `def generate_sine_wave(frequency: float, amplitude: float, sampling_rate: float, number_of_samples: int, phase_in: float=0.0) -> tuple[numpy.typing.NDArray[numpy.double], float]`

Generates a sine wave with a specified phase.

    Args:
        frequency: Specifies the frequency of the sine wave.
        amplitude: Specifies the amplitude of the sine wave.
        sampling_rate: Specifies the sampling rate of the sine wave.
        number_of_samples: Specifies the number of samples to generate.
        phase_in: Specifies the phase of the sine wave in radians.

    Returns:
        Indicates a tuple containing the generated data and the phase
        of the sine wave after generation.
    

### `def main()`

Continuously generates a sine wave.

<!--NI_PYTHON_API repo=nidaqmx-python path=examples/analog_out/cont_gen_voltage_wfm_int_clk_every_n_samples_event.py -->
## PYTHON MODULE: examples/analog_out/cont_gen_voltage_wfm_int_clk_every_n_samples_event.py

### MODULE DOCSTRING

Example of analog output voltage generation with events.

This example demonstrates how to use a Every N Samples events to output a
continuous periodic waveform to an Analog Output Channel
using an internal sample clock. The Every N Samples events indicate when
the specified number of samples generation is complete.


### `def generate_sine_wave(frequency: float, amplitude: float, sampling_rate: float, number_of_samples: int, phase_in: float=0.0) -> tuple[numpy.typing.NDArray[numpy.double], float]`

Generates a sine wave with a specified phase.

    Args:
        frequency: Specifies the frequency of the sine wave.
        amplitude: Specifies the amplitude of the sine wave.
        sampling_rate: Specifies the sampling rate of the sine wave.
        number_of_samples: Specifies the number of samples to generate.
        phase_in: Specifies the phase of the sine wave in radians.

    Returns:
        Indicates a tuple containing the generated data and the phase
        of the sine wave after generation.
    

### `def main()`

Continuously generates a sine wave using an Every N Samples event.

<!--NI_PYTHON_API repo=nidaqmx-python path=examples/analog_out/cont_gen_voltage_wfm_int_clk_non_regen.py -->
## PYTHON MODULE: examples/analog_out/cont_gen_voltage_wfm_int_clk_non_regen.py

### MODULE DOCSTRING

Example of analog output voltage generation.

This example demonstrates how to continuously generate an
analog output waveform by providing new data to the output buffer
as the task is running.

This example is useful if you want to generate a non-repeating waveform,
make updates on-the-fly, or generate a frequency that is not an
even divide-down of your sample clock. In this example,
the default frequency value is 17.0 to demonstrate that non-regenerative output
can be used to create a signal with a frequency that is not an even divide-down
of your sample clock.


### `def generate_sine_wave(frequency: float, amplitude: float, sampling_rate: float, number_of_samples: int, phase_in: float=0.0) -> tuple[numpy.typing.NDArray[numpy.double], float]`

Generates a sine wave with a specified phase.

    Args:
        frequency: Specifies the frequency of the sine wave.
        amplitude: Specifies the amplitude of the sine wave.
        sampling_rate: Specifies the sampling rate of the sine wave.
        number_of_samples: Specifies the number of samples to generate.
        phase_in: Specifies the phase of the sine wave in radians.

    Returns:
        Indicates a tuple containing the generated data and the phase
        of the sine wave after generation.
    

### `def main()`

Generate a continuous voltage waveform using an analog output channel of a NI-DAQmx device.

    This function sets up a task to generate a continuous voltage waveform using the specified
    analog output channel of a NI-DAQmx device. It configures the sampling rate, number of samples,
    and regeneration mode of the task. It then enters a loop where it continuously generates a
    sine wave with a specified frequency, amplitude, and phase, and writes the waveform to the
    analog output channel.
    The loop continues until the user interrupts the program by pressing Ctrl+C.

    Args:
        None

    Returns:
        None
    

<!--NI_PYTHON_API repo=nidaqmx-python path=examples/analog_out/gen_voltage_wfm_int_clk.py -->
## PYTHON MODULE: examples/analog_out/gen_voltage_wfm_int_clk.py

### MODULE DOCSTRING

Example of analog output voltage generation.

This example demonstrates how to output a finite number of
voltage samples to an Analog Output Channel using an internal
sample clock.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/analog_out/voltage_update.py -->
## PYTHON MODULE: examples/analog_out/voltage_update.py

### MODULE DOCSTRING

Example of analog output voltage generation.

This example demonstrates how to output a single Voltage Update
(Sample) to an Analog Output Channel.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/channel_properties.py -->
## PYTHON MODULE: examples/channel_properties.py

### MODULE DOCSTRING

Example for using channel properties.

<!--NI_PYTHON_API repo=nidaqmx-python path=examples/counter_in/cnt_dig_event.py -->
## PYTHON MODULE: examples/counter_in/cnt_dig_event.py

### MODULE DOCSTRING

Example of counter input edge count operation.

This example demonstrates how to count digital events on a
Counter Input Channel. The Initial Count, Count Direction, and
Edge are all configurable.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/counter_in/cont_cnt_buff_event_ext_clk.py -->
## PYTHON MODULE: examples/counter_in/cont_cnt_buff_event_ext_clk.py

### MODULE DOCSTRING

Example of counter input edge count operation.

This example demonstrates how to count buffered digital events
on a Counter Input Channel. The Initial Count, Count Direction,
Edge, and Sample Clock Source are all configurable.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/counter_in/cont_read_buff_freq.py -->
## PYTHON MODULE: examples/counter_in/cont_read_buff_freq.py

### MODULE DOCSTRING

Example of counter input frequency acquisition.

This example demonstrates how to continuously measure buffered frequency
using one counter on a Counter Input Channel. The Edge, Minimum Value
and Maximum Value are all configurable.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/counter_in/read_freq.py -->
## PYTHON MODULE: examples/counter_in/read_freq.py

### MODULE DOCSTRING

Example of counter input frequency acquisition.

This example demonstrates how to measure frequency using one
counter on a Counter Input Channel. The Edge, Minimum Value and
Maximum Value are all configurable.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/counter_in/read_pulse_freq.py -->
## PYTHON MODULE: examples/counter_in/read_pulse_freq.py

### MODULE DOCSTRING

Example of CI pulse frequency operation.

This example demonstrates how to configure a pulse measurement to acquire frequency and duty cycle.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/counter_out/cont_gen_dig_pulse_train.py -->
## PYTHON MODULE: examples/counter_out/cont_gen_dig_pulse_train.py

### MODULE DOCSTRING

Example for continuously generating digital pulse train.

This example demonstrates how to generate a continuous digital
pulse train from a Counter Output Channel. The Frequency, Duty
Cycle, and Idle State are all configurable.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/counter_out/cont_gen_dig_pulse_train_buff_ext_clk.py -->
## PYTHON MODULE: examples/counter_out/cont_gen_dig_pulse_train_buff_ext_clk.py

### MODULE DOCSTRING

Example for continuously generating digital pulse train with external timing.

This example demonstrates how to generate a continuous buffered
sample clocked digital pulse train from a Counter Output
Channel. The Frequency, Duty Cycle, and Idle State are all
configurable. The default data generated is a pulse train with a
fixed frequency but a duty cycle that varies based on the Duty
Cycle Max/Min and the signal type. The duty cycle will update
with each sample clock edge.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/counter_out/cont_gen_dig_pulse_train_buff_implicit.py -->
## PYTHON MODULE: examples/counter_out/cont_gen_dig_pulse_train_buff_implicit.py

### MODULE DOCSTRING

Example for continuously generating digital pulse train with implicit timing.

This example demonstrates how to generate a continuous buffered
implicit timed digital pulse train from a Counter Output
Channel. The Frequency, Duty Cycle, and Idle State are all
configurable. The default data generated is a pulse train with a
fixed frequency but a duty cycle that varies based on the Duty
Cycle Max/Min and the signal type. The duty cycle will update
with each sample generated.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/counter_out/write_single_dig_pulse.py -->
## PYTHON MODULE: examples/counter_out/write_single_dig_pulse.py

### MODULE DOCSTRING

Example for generating a single digital pulse.

This example demonstrates how to generate a single digital pulse
from a Counter Output Channel. The Initial Delay, High Time, Low
Time, and Idle State are all configurable.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/digital_in/acq_dig_port_int_clk.py -->
## PYTHON MODULE: examples/digital_in/acq_dig_port_int_clk.py

### MODULE DOCSTRING

Example for reading digital signals.

This example demonstrates how to input a finite digital pattern
using the DAQ device's internal clock.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/digital_in/acq_dig_port_int_clk_wfm.py -->
## PYTHON MODULE: examples/digital_in/acq_dig_port_int_clk_wfm.py

### MODULE DOCSTRING

Example for reading digital signals.

This example demonstrates how to input a finite digital pattern
using the DAQ device's internal clock.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/digital_in/cont_acq_dig_lines_int_clk.py -->
## PYTHON MODULE: examples/digital_in/cont_acq_dig_lines_int_clk.py

### MODULE DOCSTRING

Example for reading digital signals.

This example demonstrates how to acquire a continuous digital
waveform using the DAQ device's internal clock.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/digital_in/read_dig_lines.py -->
## PYTHON MODULE: examples/digital_in/read_dig_lines.py

### MODULE DOCSTRING

Example for reading digital signals.

This example demonstrates how to read values from one or more
digital input channels.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/digital_in/read_dig_port.py -->
## PYTHON MODULE: examples/digital_in/read_dig_port.py

### MODULE DOCSTRING

Example for reading a digital signal.

This example demonstrates how to read values from a digital
input port.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/digital_out/cont_gen_dig_port_int_clk.py -->
## PYTHON MODULE: examples/digital_out/cont_gen_dig_port_int_clk.py

### MODULE DOCSTRING

Example for generating digital signals.

This example demonstrates how to output a continuous digital
pattern using the DAQ device's clock.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/digital_out/cont_gen_dig_port_int_clk_wfm.py -->
## PYTHON MODULE: examples/digital_out/cont_gen_dig_port_int_clk_wfm.py

### MODULE DOCSTRING

Example for generating digital signals using the DigitalWaveform data type.

This example demonstrates how to output a continuous digital
pattern using the DAQ device's clock.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/digital_out/gen_dig_line_int_clk.py -->
## PYTHON MODULE: examples/digital_out/gen_dig_line_int_clk.py

### MODULE DOCSTRING

Example for generating digital signals.

This example demonstrates how to output a finite digital
waveform using the DAQ device's internal clock.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/digital_out/write_dig_lines.py -->
## PYTHON MODULE: examples/digital_out/write_dig_lines.py

### MODULE DOCSTRING

Example for generating digital signals.

This example demonstrates how to write values to a digital
output channel.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/digital_out/write_dig_port.py -->
## PYTHON MODULE: examples/digital_out/write_dig_port.py

### MODULE DOCSTRING

Example for generating digital signals.

This example demonstrates how to write values to a digital
output port.


<!--NI_PYTHON_API repo=nidaqmx-python path=examples/every_n_samples_event.py -->
## PYTHON MODULE: examples/every_n_samples_event.py

### MODULE DOCSTRING

Example for reading signals for every n samples.

<!--NI_PYTHON_API repo=nidaqmx-python path=examples/nidaqmx_warnings.py -->
## PYTHON MODULE: examples/nidaqmx_warnings.py

### MODULE DOCSTRING

Example for catching warnings in DAQmx.

<!--NI_PYTHON_API repo=nidaqmx-python path=examples/playrec.py -->
## PYTHON MODULE: examples/playrec.py

### MODULE DOCSTRING

Simultaneous read and write with NI USB-4431 or similar device.

### `def query_devices()`

Queries all the device information connected to the local system.

### `def play_record(data, sample_rate, input_mapping, output_mapping)`

Simultaneous playback and recording though NI device.

    Parameters:
    -----------
    data: array_like, shape (num_samples, len(output_mapping))
      Data to be send to output channels.
    sample_rate: int
      Sample rate
    input_mapping: list of str
      Input device channels
    output_mapping: list of str
      Output device channels

    Returns
    -------
    ndarray, shape (num_samples, len(input_mapping))
      Recorded data

    

<!--NI_PYTHON_API repo=nidaqmx-python path=examples/pwr_hw_timed.py -->
## PYTHON MODULE: examples/pwr_hw_timed.py

### MODULE DOCSTRING

Examples for hw timed power operation.

<!--NI_PYTHON_API repo=nidaqmx-python path=examples/pwr_hw_timed_stream.py -->
## PYTHON MODULE: examples/pwr_hw_timed_stream.py

### MODULE DOCSTRING

Examples for hw timed power stream operation.

<!--NI_PYTHON_API repo=nidaqmx-python path=examples/pwr_sw_timed.py -->
## PYTHON MODULE: examples/pwr_sw_timed.py

### MODULE DOCSTRING

Examples for sw timed power operation.

<!--NI_PYTHON_API repo=nidaqmx-python path=examples/synchronization/multi_function/ai_ao_sync.py -->
## PYTHON MODULE: examples/synchronization/multi_function/ai_ao_sync.py

### MODULE DOCSTRING

Example of analog input and output synchronization.

This example demonstrates how to continuously acquire and
generate data at the same time, synchronized with one another.


### `def get_terminal_name_with_dev_prefix(task: nidaqmx.Task, terminal_name: str) -> str`

Gets the terminal name with the device prefix.

    Args:
        task: Specifies the task to get the device name from.
        terminal_name: Specifies the terminal name to get.

    Returns:
        Indicates the terminal name with the device prefix.
    

### `def generate_sine_wave(frequency: float, amplitude: float, sampling_rate: float, number_of_samples: int, phase_in: float=0.0) -> tuple[numpy.typing.NDArray[numpy.double], float]`

Generates a sine wave with a specified phase.

    Args:
        frequency: Specifies the frequency of the sine wave.
        amplitude: Specifies the amplitude of the sine wave.
        sampling_rate: Specifies the sampling rate of the sine wave.
        number_of_samples: Specifies the number of samples to generate.
        phase_in: Specifies the phase of the sine wave in radians.

    Returns:
        Indicates a tuple containing the generated data and the phase
        of the sine wave after generation.
    

### `def main()`

Continuously acquires and generate data at the same time.

<!--NI_PYTHON_API repo=nidaqmx-python path=examples/synchronization/multi_function/cont_ai_ci_tdms_sync.py -->
## PYTHON MODULE: examples/synchronization/multi_function/cont_ai_ci_tdms_sync.py

### MODULE DOCSTRING

Example of logging multiple synchronized tasks to a single TDMS file using a queue.

This example demonstrates how to:
1. Synchronize multiple DAQmx tasks using a shared clock
2. Use a producer-consumer pattern with a queue
3. Log data from multiple tasks to a single TDMS file


- `SAMPLE_RATE = 1000`

- `SAMPLES_PER_CHANNEL = 1000`

- `TIMEOUT = 10.0`

- `DEVICE_NAME = 'Dev1'`

### `def producer(tasks: Sequence[nidaqmx.Task], data_queue: queue.Queue[TaskData | None], stop_event: threading.Event) -> None`

Producer function that reads data from DAQmx tasks and puts it in the queue.

### `def consumer(data_queue: queue.Queue[TaskData | None], tdms_path: str, group_names: Sequence[str], channel_names: Sequence[Sequence[str]], stop_event: threading.Event) -> None`

Consumer function that writes data from the queue to a TDMS file.

### `def main()`

Run the synchronized data acquisition and logging example.

    Creates multiple synchronized DAQmx tasks:
    - A counter output task for the sample clock
    - An analog input task reading from two voltage channels
    - A counter input task counting edges

    Data is acquired continuously until user presses Enter, then saved to a TDMS file
    using a producer-consumer pattern with a queue for thread-safe data transfer.
    

<!--NI_PYTHON_API repo=nidaqmx-python path=examples/synchronization/multi_function/cont_ai_di_acq.py -->
## PYTHON MODULE: examples/synchronization/multi_function/cont_ai_di_acq.py

### MODULE DOCSTRING

Example of analog and digital data acquisition at the same time.

This example demonstrates how to continuously acquire analog and
digital data at the same time, synchronized with one another on
the same device.


### `def get_terminal_name_with_dev_prefix(task: nidaqmx.Task, terminal_name: str) -> str`

Gets the terminal name with the device prefix.

    Args:
        task: Specifies the task to get the device name from.
        terminal_name: Specifies the terminal name to get.

    Returns:
        Indicates the terminal name with the device prefix.
    

### `def main()`

Continuously acquire analog and digital data at the same time.

<!--NI_PYTHON_API repo=nidaqmx-python path=examples/system_properties.py -->
## PYTHON MODULE: examples/system_properties.py

### MODULE DOCSTRING

Examples for using system properties in DAQmx.

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/__init__.py -->
## PYTHON MODULE: generated/nidaqmx/__init__.py

### MODULE DOCSTRING

The NI-DAQmx API for Python.

- `__all__ = ['errors', 'scale', 'stream_readers', 'stream_writers', 'task']`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/__main__.py -->
## PYTHON MODULE: generated/nidaqmx/__main__.py

### MODULE DOCSTRING

'nidaqmx' command line utility.

### `def main(verbosity: int) -> None`

### `def installdriver()`

### `def _configure_logging(verbosity: int) -> None`

Configure logging for this process.

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/_base_interpreter.py -->
## PYTHON MODULE: generated/nidaqmx/_base_interpreter.py

### `class BaseEventHandler(abc.ABC)`

Interpreter-specific object that is returned from register_*_event().

#### `def close(self) -> None`

Release resources used by the event handler.

        After releasing the resources, this method may report handler-specific errors
        (e.g. gRPC stream errors) by raising an exception.
        

### `class BaseInterpreter(abc.ABC)`


    Contains signature of functions for all DAQmx APIs.
    

#### `def add_cdaq_sync_connection(self, port_list)`

#### `def add_global_chans_to_task(self, task, channel_names)`

#### `def add_network_device(self, ip_address, device_name, attempt_reservation, timeout)`

#### `def are_configured_cdaq_sync_ports_disconnected(self, chassis_devices_ports, timeout)`

#### `def auto_configure_cdaq_sync_connections(self, chassis_devices_ports, timeout)`

#### `def calculate_reverse_poly_coeff(self, forward_coeffs, min_val_x, max_val_x, num_points_to_compute, reverse_poly_order)`

#### `def cfg_anlg_edge_ref_trig(self, task, trigger_source, pretrigger_samples, trigger_slope, trigger_level)`

#### `def cfg_anlg_edge_start_trig(self, task, trigger_source, trigger_slope, trigger_level)`

#### `def cfg_anlg_multi_edge_ref_trig(self, task, trigger_sources, pretrigger_samples, trigger_slope_array, trigger_level_array)`

#### `def cfg_anlg_multi_edge_start_trig(self, task, trigger_sources, trigger_slope_array, trigger_level_array)`

#### `def cfg_anlg_window_ref_trig(self, task, trigger_source, window_top, window_bottom, pretrigger_samples, trigger_when)`

#### `def cfg_anlg_window_start_trig(self, task, window_top, window_bottom, trigger_source, trigger_when)`

#### `def cfg_burst_handshaking_timing_export_clock(self, task, sample_clk_rate, sample_clk_outp_term, sample_mode, samps_per_chan, sample_clk_pulse_polarity, pause_when, ready_event_active_level)`

#### `def cfg_burst_handshaking_timing_import_clock(self, task, sample_clk_rate, sample_clk_src, sample_mode, samps_per_chan, sample_clk_active_edge, pause_when, ready_event_active_level)`

#### `def cfg_change_detection_timing(self, task, rising_edge_chan, falling_edge_chan, sample_mode, samps_per_chan)`

#### `def cfg_dig_edge_ref_trig(self, task, trigger_source, pretrigger_samples, trigger_edge)`

#### `def cfg_dig_edge_start_trig(self, task, trigger_source, trigger_edge)`

#### `def cfg_dig_pattern_ref_trig(self, task, trigger_source, trigger_pattern, pretrigger_samples, trigger_when)`

#### `def cfg_dig_pattern_start_trig(self, task, trigger_source, trigger_pattern, trigger_when)`

#### `def cfg_handshaking_timing(self, task, sample_mode, samps_per_chan)`

#### `def cfg_implicit_timing(self, task, sample_mode, samps_per_chan)`

#### `def cfg_pipelined_samp_clk_timing(self, task, rate, source, active_edge, sample_mode, samps_per_chan)`

#### `def cfg_samp_clk_timing(self, task, rate, source, active_edge, sample_mode, samps_per_chan)`

#### `def cfg_time_start_trig(self, task, when, timescale)`

#### `def cfg_watchdog_ao_expir_states(self, task, channel_names, expir_state_array, output_type_array)`

#### `def cfg_watchdog_co_expir_states(self, task, channel_names, expir_state_array)`

#### `def cfg_watchdog_do_expir_states(self, task, channel_names, expir_state_array)`

#### `def clear_task(self, task)`

#### `def clear_teds(self, physical_channel)`

#### `def configure_logging(self, task, file_path, logging_mode, group_name, operation)`

#### `def configure_teds(self, physical_channel, file_path)`

#### `def connect_terms(self, source_terminal, destination_terminal, signal_modifiers)`

#### `def control_watchdog_task(self, task, action)`

#### `def create_ai_accel4_wire_dc_voltage_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, sensitivity, sensitivity_units, voltage_excit_source, voltage_excit_val, use_excit_for_scaling, custom_scale_name)`

#### `def create_ai_accel_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, sensitivity, sensitivity_units, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_ai_accel_charge_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, sensitivity, sensitivity_units, custom_scale_name)`

#### `def create_ai_bridge_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, custom_scale_name)`

#### `def create_ai_calculated_power_chan(self, task, voltage_physical_channel, current_physical_channel, name_to_assign_to_channel, terminal_config, voltage_min_val, voltage_max_val, current_min_val, current_max_val, units, shunt_resistor_loc, ext_shunt_resistor_val, custom_scale_name)`

#### `def create_ai_charge_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, custom_scale_name)`

#### `def create_ai_current_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, shunt_resistor_loc, ext_shunt_resistor_val, custom_scale_name)`

#### `def create_ai_current_rms_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, shunt_resistor_loc, ext_shunt_resistor_val, custom_scale_name)`

#### `def create_ai_force_bridge_polynomial_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, forward_coeffs, reverse_coeffs, electrical_units, physical_units, custom_scale_name)`

#### `def create_ai_force_bridge_table_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, electrical_vals, electrical_units, physical_vals, physical_units, custom_scale_name)`

#### `def create_ai_force_bridge_two_point_lin_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, first_electrical_val, second_electrical_val, electrical_units, first_physical_val, second_physical_val, physical_units, custom_scale_name)`

#### `def create_ai_force_iepe_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, sensitivity, sensitivity_units, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_ai_freq_voltage_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, threshold_level, hysteresis, custom_scale_name)`

#### `def create_ai_microphone_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, units, mic_sensitivity, max_snd_press_level, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_ai_pos_eddy_curr_prox_probe_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, sensitivity, sensitivity_units, custom_scale_name)`

#### `def create_ai_pos_lvdt_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, sensitivity, sensitivity_units, voltage_excit_source, voltage_excit_val, voltage_excit_freq, ac_excit_wire_mode, custom_scale_name)`

#### `def create_ai_pos_rvdt_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, sensitivity, sensitivity_units, voltage_excit_source, voltage_excit_val, voltage_excit_freq, ac_excit_wire_mode, custom_scale_name)`

#### `def create_ai_power_chan(self, task, physical_channel, voltage_setpoint, current_setpoint, output_enable, name_to_assign_to_channel)`

#### `def create_ai_pressure_bridge_polynomial_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, forward_coeffs, reverse_coeffs, electrical_units, physical_units, custom_scale_name)`

#### `def create_ai_pressure_bridge_table_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, electrical_vals, electrical_units, physical_vals, physical_units, custom_scale_name)`

#### `def create_ai_pressure_bridge_two_point_lin_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, first_electrical_val, second_electrical_val, electrical_units, first_physical_val, second_physical_val, physical_units, custom_scale_name)`

#### `def create_ai_resistance_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, resistance_config, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_ai_rosette_strain_gage_chan(self, task, physical_channel, rosette_type, gage_orientation, rosette_meas_types, name_to_assign_to_channel, min_val, max_val, strain_config, voltage_excit_source, voltage_excit_val, gage_factor, nominal_gage_resistance, poisson_ratio, lead_wire_resistance)`

#### `def create_ai_strain_gage_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, strain_config, voltage_excit_source, voltage_excit_val, gage_factor, initial_bridge_voltage, nominal_gage_resistance, poisson_ratio, lead_wire_resistance, custom_scale_name)`

#### `def create_ai_temp_built_in_sensor_chan(self, task, physical_channel, name_to_assign_to_channel, units)`

#### `def create_ai_thrmcpl_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, thermocouple_type, cjc_source, cjc_val, cjc_channel)`

#### `def create_ai_thrmstr_chan_iex(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, resistance_config, current_excit_source, current_excit_val, a, b, c)`

#### `def create_ai_thrmstr_chan_vex(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, resistance_config, voltage_excit_source, voltage_excit_val, a, b, c, r_1)`

#### `def create_ai_torque_bridge_polynomial_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, forward_coeffs, reverse_coeffs, electrical_units, physical_units, custom_scale_name)`

#### `def create_ai_torque_bridge_table_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, electrical_vals, electrical_units, physical_vals, physical_units, custom_scale_name)`

#### `def create_ai_torque_bridge_two_point_lin_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, first_electrical_val, second_electrical_val, electrical_units, first_physical_val, second_physical_val, physical_units, custom_scale_name)`

#### `def create_ai_velocity_iepe_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, sensitivity, sensitivity_units, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_ai_voltage_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, custom_scale_name)`

#### `def create_ai_voltage_chan_with_excit(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, use_excit_for_scaling, custom_scale_name)`

#### `def create_ai_voltage_rms_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, custom_scale_name)`

#### `def create_airtd_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, rtd_type, resistance_config, current_excit_source, current_excit_val, r_0)`

#### `def create_ao_current_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, custom_scale_name)`

#### `def create_ao_func_gen_chan(self, task, physical_channel, name_to_assign_to_channel, type, freq, amplitude, offset)`

#### `def create_ao_voltage_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, custom_scale_name)`

#### `def create_ci_ang_encoder_chan(self, task, counter, name_to_assign_to_channel, decoding_type, zidx_enable, zidx_val, zidx_phase, units, pulses_per_rev, initial_angle, custom_scale_name)`

#### `def create_ci_ang_velocity_chan(self, task, counter, name_to_assign_to_channel, min_val, max_val, decoding_type, units, pulses_per_rev, custom_scale_name)`

#### `def create_ci_count_edges_chan(self, task, counter, name_to_assign_to_channel, edge, initial_count, count_direction)`

#### `def create_ci_duty_cycle_chan(self, task, counter, name_to_assign_to_channel, min_freq, max_freq, edge, custom_scale_name)`

#### `def create_ci_freq_chan(self, task, counter, name_to_assign_to_channel, min_val, max_val, units, edge, meas_method, meas_time, divisor, custom_scale_name)`

#### `def create_ci_lin_encoder_chan(self, task, counter, name_to_assign_to_channel, decoding_type, zidx_enable, zidx_val, zidx_phase, units, dist_per_pulse, initial_pos, custom_scale_name)`

#### `def create_ci_lin_velocity_chan(self, task, counter, name_to_assign_to_channel, min_val, max_val, decoding_type, units, dist_per_pulse, custom_scale_name)`

#### `def create_ci_period_chan(self, task, counter, name_to_assign_to_channel, min_val, max_val, units, edge, meas_method, meas_time, divisor, custom_scale_name)`

#### `def create_ci_pulse_chan_freq(self, task, counter, name_to_assign_to_channel, min_val, max_val, units)`

#### `def create_ci_pulse_chan_ticks(self, task, counter, name_to_assign_to_channel, source_terminal, min_val, max_val)`

#### `def create_ci_pulse_chan_time(self, task, counter, name_to_assign_to_channel, min_val, max_val, units)`

#### `def create_ci_pulse_width_chan(self, task, counter, name_to_assign_to_channel, min_val, max_val, units, starting_edge, custom_scale_name)`

#### `def create_ci_semi_period_chan(self, task, counter, name_to_assign_to_channel, min_val, max_val, units, custom_scale_name)`

#### `def create_ci_two_edge_sep_chan(self, task, counter, name_to_assign_to_channel, min_val, max_val, units, first_edge, second_edge, custom_scale_name)`

#### `def create_cigps_timestamp_chan(self, task, counter, name_to_assign_to_channel, units, sync_method, custom_scale_name)`

#### `def create_co_pulse_chan_freq(self, task, counter, name_to_assign_to_channel, units, idle_state, initial_delay, freq, duty_cycle)`

#### `def create_co_pulse_chan_ticks(self, task, counter, source_terminal, name_to_assign_to_channel, idle_state, initial_delay, low_ticks, high_ticks)`

#### `def create_co_pulse_chan_time(self, task, counter, name_to_assign_to_channel, units, idle_state, initial_delay, low_time, high_time)`

#### `def create_di_chan(self, task, lines, name_to_assign_to_lines, line_grouping)`

#### `def create_do_chan(self, task, lines, name_to_assign_to_lines, line_grouping)`

#### `def create_lin_scale(self, name, slope, y_intercept, pre_scaled_units, scaled_units)`

#### `def create_map_scale(self, name, prescaled_min, prescaled_max, scaled_min, scaled_max, pre_scaled_units, scaled_units)`

#### `def create_polynomial_scale(self, name, forward_coeffs, reverse_coeffs, pre_scaled_units, scaled_units)`

#### `def create_table_scale(self, name, prescaled_vals, scaled_vals, pre_scaled_units, scaled_units)`

#### `def create_task(self, session_name)`

#### `def create_tedsai_accel_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_tedsai_bridge_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, voltage_excit_source, voltage_excit_val, custom_scale_name)`

#### `def create_tedsai_current_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, shunt_resistor_loc, ext_shunt_resistor_val, custom_scale_name)`

#### `def create_tedsai_force_bridge_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, voltage_excit_source, voltage_excit_val, custom_scale_name)`

#### `def create_tedsai_force_iepe_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_tedsai_microphone_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, units, max_snd_press_level, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_tedsai_pos_lvdt_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, voltage_excit_source, voltage_excit_val, voltage_excit_freq, ac_excit_wire_mode, custom_scale_name)`

#### `def create_tedsai_pos_rvdt_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, voltage_excit_source, voltage_excit_val, voltage_excit_freq, ac_excit_wire_mode, custom_scale_name)`

#### `def create_tedsai_pressure_bridge_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, voltage_excit_source, voltage_excit_val, custom_scale_name)`

#### `def create_tedsai_resistance_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, resistance_config, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_tedsai_strain_gage_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, voltage_excit_source, voltage_excit_val, initial_bridge_voltage, lead_wire_resistance, custom_scale_name)`

#### `def create_tedsai_thrmcpl_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, cjc_source, cjc_val, cjc_channel)`

#### `def create_tedsai_thrmstr_chan_iex(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, resistance_config, current_excit_source, current_excit_val)`

#### `def create_tedsai_thrmstr_chan_vex(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, resistance_config, voltage_excit_source, voltage_excit_val, r_1)`

#### `def create_tedsai_torque_bridge_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, voltage_excit_source, voltage_excit_val, custom_scale_name)`

#### `def create_tedsai_voltage_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, custom_scale_name)`

#### `def create_tedsai_voltage_chan_with_excit(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, voltage_excit_source, voltage_excit_val, custom_scale_name)`

#### `def create_tedsairtd_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, resistance_config, current_excit_source, current_excit_val)`

#### `def create_watchdog_timer_task_ex(self, device_name, session_name, timeout)`

#### `def delete_network_device(self, device_name)`

#### `def delete_saved_global_chan(self, channel_name)`

#### `def delete_saved_scale(self, scale_name)`

#### `def delete_saved_task(self, task_name)`

#### `def device_supports_cal(self, device_name)`

#### `def disable_ref_trig(self, task)`

#### `def disable_start_trig(self, task)`

#### `def disconnect_terms(self, source_terminal, destination_terminal)`

#### `def export_signal(self, task, signal_id, output_terminal)`

#### `def get_analog_power_up_states_with_output_type(self, channel_names, array_size)`

#### `def get_auto_configured_cdaq_sync_connections(self)`

#### `def get_buffer_attribute_uint32(self, task, attribute)`

#### `def get_cal_info_attribute_bool(self, device_name, attribute)`

#### `def get_cal_info_attribute_double(self, device_name, attribute)`

#### `def get_cal_info_attribute_string(self, device_name, attribute)`

#### `def get_cal_info_attribute_uint32(self, device_name, attribute)`

#### `def get_chan_attribute_bool(self, task, channel, attribute)`

#### `def get_chan_attribute_double(self, task, channel, attribute)`

#### `def get_chan_attribute_double_array(self, task, channel, attribute)`

#### `def get_chan_attribute_int32(self, task, channel, attribute)`

#### `def get_chan_attribute_string(self, task, channel, attribute)`

#### `def get_chan_attribute_uint32(self, task, channel, attribute)`

#### `def get_device_attribute_bool(self, device_name, attribute)`

#### `def get_device_attribute_double(self, device_name, attribute)`

#### `def get_device_attribute_double_array(self, device_name, attribute)`

#### `def get_device_attribute_int32(self, device_name, attribute)`

#### `def get_device_attribute_int32_array(self, device_name, attribute)`

#### `def get_device_attribute_string(self, device_name, attribute)`

#### `def get_device_attribute_uint32(self, device_name, attribute)`

#### `def get_device_attribute_uint32_array(self, device_name, attribute)`

#### `def get_digital_logic_family_power_up_state(self, device_name)`

#### `def get_digital_power_up_states(self, device_name, channel_name)`

#### `def get_digital_pull_up_pull_down_states(self, device_name, channel_name)`

#### `def get_disconnected_cdaq_sync_ports(self)`

#### `def get_error_string(self, error_code)`

#### `def get_exported_signal_attribute_bool(self, task, attribute)`

#### `def get_exported_signal_attribute_double(self, task, attribute)`

#### `def get_exported_signal_attribute_int32(self, task, attribute)`

#### `def get_exported_signal_attribute_string(self, task, attribute)`

#### `def get_exported_signal_attribute_uint32(self, task, attribute)`

#### `def get_ext_cal_last_date_and_time(self, device_name)`

#### `def get_persisted_chan_attribute_bool(self, channel, attribute)`

#### `def get_persisted_chan_attribute_string(self, channel, attribute)`

#### `def get_persisted_scale_attribute_bool(self, scale_name, attribute)`

#### `def get_persisted_scale_attribute_string(self, scale_name, attribute)`

#### `def get_persisted_task_attribute_bool(self, task_name, attribute)`

#### `def get_persisted_task_attribute_string(self, task_name, attribute)`

#### `def get_physical_chan_attribute_bool(self, physical_channel, attribute)`

#### `def get_physical_chan_attribute_bytes(self, physical_channel, attribute)`

#### `def get_physical_chan_attribute_double(self, physical_channel, attribute)`

#### `def get_physical_chan_attribute_double_array(self, physical_channel, attribute)`

#### `def get_physical_chan_attribute_int32(self, physical_channel, attribute)`

#### `def get_physical_chan_attribute_int32_array(self, physical_channel, attribute)`

#### `def get_physical_chan_attribute_string(self, physical_channel, attribute)`

#### `def get_physical_chan_attribute_uint32(self, physical_channel, attribute)`

#### `def get_physical_chan_attribute_uint32_array(self, physical_channel, attribute)`

#### `def get_read_attribute_bool(self, task, attribute)`

#### `def get_read_attribute_double(self, task, attribute)`

#### `def get_read_attribute_int32(self, task, attribute)`

#### `def get_read_attribute_string(self, task, attribute, size_hint=0)`

#### `def get_read_attribute_uint32(self, task, attribute)`

#### `def get_read_attribute_uint64(self, task, attribute)`

#### `def get_scale_attribute_double(self, scale_name, attribute)`

#### `def get_scale_attribute_double_array(self, scale_name, attribute)`

#### `def get_scale_attribute_int32(self, scale_name, attribute)`

#### `def get_scale_attribute_string(self, scale_name, attribute)`

#### `def get_self_cal_last_date_and_time(self, device_name)`

#### `def get_system_info_attribute_string(self, attribute)`

#### `def get_system_info_attribute_uint32(self, attribute)`

#### `def get_task_attribute_bool(self, task, attribute)`

#### `def get_task_attribute_string(self, task, attribute)`

#### `def get_task_attribute_uint32(self, task, attribute)`

#### `def get_timing_attribute_bool(self, task, attribute)`

#### `def get_timing_attribute_double(self, task, attribute)`

#### `def get_timing_attribute_ex_bool(self, task, device_names, attribute)`

#### `def get_timing_attribute_ex_double(self, task, device_names, attribute)`

#### `def get_timing_attribute_ex_int32(self, task, device_names, attribute)`

#### `def get_timing_attribute_ex_string(self, task, device_names, attribute)`

#### `def get_timing_attribute_ex_uint32(self, task, device_names, attribute)`

#### `def get_timing_attribute_ex_uint64(self, task, device_names, attribute)`

#### `def get_timing_attribute_int32(self, task, attribute)`

#### `def get_timing_attribute_string(self, task, attribute)`

#### `def get_timing_attribute_timestamp(self, task, attribute)`

#### `def get_timing_attribute_uint32(self, task, attribute)`

#### `def get_timing_attribute_uint64(self, task, attribute)`

#### `def get_trig_attribute_bool(self, task, attribute)`

#### `def get_trig_attribute_double(self, task, attribute)`

#### `def get_trig_attribute_double_array(self, task, attribute)`

#### `def get_trig_attribute_int32(self, task, attribute)`

#### `def get_trig_attribute_int32_array(self, task, attribute)`

#### `def get_trig_attribute_string(self, task, attribute)`

#### `def get_trig_attribute_timestamp(self, task, attribute)`

#### `def get_trig_attribute_uint32(self, task, attribute)`

#### `def get_watchdog_attribute_bool(self, task, lines, attribute)`

#### `def get_watchdog_attribute_double(self, task, lines, attribute)`

#### `def get_watchdog_attribute_int32(self, task, lines, attribute)`

#### `def get_watchdog_attribute_string(self, task, lines, attribute)`

#### `def get_write_attribute_bool(self, task, attribute)`

#### `def get_write_attribute_double(self, task, attribute)`

#### `def get_write_attribute_int32(self, task, attribute)`

#### `def get_write_attribute_string(self, task, attribute, size_hint=0)`

#### `def get_write_attribute_uint32(self, task, attribute)`

#### `def get_write_attribute_uint64(self, task, attribute)`

#### `def internal_get_last_created_chan(self)`

#### `def is_task_done(self, task)`

#### `def load_task(self, session_name)`

#### `def perform_bridge_offset_nulling_cal_ex(self, task, channel, skip_unsupported_channels)`

#### `def perform_bridge_shunt_cal_ex(self, task, channel, shunt_resistor_value, shunt_resistor_location, shunt_resistor_select, shunt_resistor_source, bridge_resistance, skip_unsupported_channels)`

#### `def perform_strain_shunt_cal_ex(self, task, channel, shunt_resistor_value, shunt_resistor_location, shunt_resistor_select, shunt_resistor_source, skip_unsupported_channels)`

#### `def perform_thrmcpl_lead_offset_nulling_cal(self, task, channel, skip_unsupported_channels)`

#### `def read_analog_f64(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_analog_scalar_f64(self, task, timeout)`

#### `def read_binary_i16(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_binary_i32(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_binary_u16(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_binary_u32(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_counter_f64(self, task, num_samps_per_chan, timeout, read_array)`

#### `def read_counter_f64_ex(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_counter_scalar_f64(self, task, timeout)`

#### `def read_counter_scalar_u32(self, task, timeout)`

#### `def read_counter_u32(self, task, num_samps_per_chan, timeout, read_array)`

#### `def read_counter_u32_ex(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_ctr_freq(self, task, num_samps_per_chan, timeout, interleaved, read_array_frequency, read_array_duty_cycle)`

#### `def read_ctr_freq_scalar(self, task, timeout)`

#### `def read_ctr_ticks(self, task, num_samps_per_chan, timeout, interleaved, read_array_high_ticks, read_array_low_ticks)`

#### `def read_ctr_ticks_scalar(self, task, timeout)`

#### `def read_ctr_time(self, task, num_samps_per_chan, timeout, interleaved, read_array_high_time, read_array_low_time)`

#### `def read_ctr_time_scalar(self, task, timeout)`

#### `def read_digital_lines(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_digital_scalar_u32(self, task, timeout)`

#### `def read_digital_u16(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_digital_u32(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_digital_u8(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_id_pin_memory(self, device_name, id_pin_name)`

#### `def read_power_binary_i16(self, task, num_samps_per_chan, timeout, fill_mode, read_array_voltage, read_array_current)`

#### `def read_power_f64(self, task, num_samps_per_chan, timeout, fill_mode, read_array_voltage, read_array_current)`

#### `def read_power_scalar_f64(self, task, timeout)`

#### `def read_raw(self, task, num_samps_per_chan, timeout, read_array)`

#### `def register_done_event(self, task, options, callback_function, callback_data)`

#### `def register_every_n_samples_event(self, task, every_n_samples_event_type, n_samples, options, callback_function, callback_data)`

#### `def register_signal_event(self, task, signal_id, options, callback_function, callback_data)`

#### `def remove_cdaq_sync_connection(self, port_list)`

#### `def reserve_network_device(self, device_name, override_reservation)`

#### `def reset_buffer_attribute(self, task, attribute)`

#### `def reset_chan_attribute(self, task, channel, attribute)`

#### `def reset_device(self, device_name)`

#### `def reset_exported_signal_attribute(self, task, attribute)`

#### `def reset_read_attribute(self, task, attribute)`

#### `def reset_timing_attribute(self, task, attribute)`

#### `def reset_timing_attribute_ex(self, task, device_names, attribute)`

#### `def reset_trig_attribute(self, task, attribute)`

#### `def reset_watchdog_attribute(self, task, lines, attribute)`

#### `def reset_write_attribute(self, task, attribute)`

#### `def restore_last_ext_cal_const(self, device_name)`

#### `def save_global_chan(self, task, channel_name, save_as, author, options)`

#### `def save_scale(self, scale_name, save_as, author, options)`

#### `def save_task(self, task, save_as, author, options)`

#### `def self_cal(self, device_name)`

#### `def self_test_device(self, device_name)`

#### `def set_analog_power_up_states(self, device_name, channel_names, state, channel_type)`

#### `def set_analog_power_up_states_with_output_type(self, channel_names, state_array, channel_type_array)`

#### `def set_buffer_attribute_uint32(self, task, attribute, value)`

#### `def set_cal_info_attribute_bool(self, device_name, attribute, value)`

#### `def set_cal_info_attribute_double(self, device_name, attribute, value)`

#### `def set_cal_info_attribute_string(self, device_name, attribute, value)`

#### `def set_cal_info_attribute_uint32(self, device_name, attribute, value)`

#### `def set_chan_attribute_bool(self, task, channel, attribute, value)`

#### `def set_chan_attribute_double(self, task, channel, attribute, value)`

#### `def set_chan_attribute_double_array(self, task, channel, attribute, value)`

#### `def set_chan_attribute_int32(self, task, channel, attribute, value)`

#### `def set_chan_attribute_string(self, task, channel, attribute, value)`

#### `def set_chan_attribute_uint32(self, task, channel, attribute, value)`

#### `def set_digital_logic_family_power_up_state(self, device_name, logic_family)`

#### `def set_digital_power_up_states(self, device_name, channel_names, state)`

#### `def set_digital_pull_up_pull_down_states(self, device_name, channel_names, state)`

#### `def set_exported_signal_attribute_bool(self, task, attribute, value)`

#### `def set_exported_signal_attribute_double(self, task, attribute, value)`

#### `def set_exported_signal_attribute_int32(self, task, attribute, value)`

#### `def set_exported_signal_attribute_string(self, task, attribute, value)`

#### `def set_exported_signal_attribute_uint32(self, task, attribute, value)`

#### `def set_read_attribute_bool(self, task, attribute, value)`

#### `def set_read_attribute_double(self, task, attribute, value)`

#### `def set_read_attribute_int32(self, task, attribute, value)`

#### `def set_read_attribute_string(self, task, attribute, value)`

#### `def set_read_attribute_uint32(self, task, attribute, value)`

#### `def set_read_attribute_uint64(self, task, attribute, value)`

#### `def set_runtime_environment(self, environment, environment_version, reserved_1, reserved_2)`

#### `def set_scale_attribute_double(self, scale_name, attribute, value)`

#### `def set_scale_attribute_double_array(self, scale_name, attribute, value)`

#### `def set_scale_attribute_int32(self, scale_name, attribute, value)`

#### `def set_scale_attribute_string(self, scale_name, attribute, value)`

#### `def set_timing_attribute_bool(self, task, attribute, value)`

#### `def set_timing_attribute_double(self, task, attribute, value)`

#### `def set_timing_attribute_ex_bool(self, task, device_names, attribute, value)`

#### `def set_timing_attribute_ex_double(self, task, device_names, attribute, value)`

#### `def set_timing_attribute_ex_int32(self, task, device_names, attribute, value)`

#### `def set_timing_attribute_ex_string(self, task, device_names, attribute, value)`

#### `def set_timing_attribute_ex_uint32(self, task, device_names, attribute, value)`

#### `def set_timing_attribute_ex_uint64(self, task, device_names, attribute, value)`

#### `def set_timing_attribute_int32(self, task, attribute, value)`

#### `def set_timing_attribute_string(self, task, attribute, value)`

#### `def set_timing_attribute_uint32(self, task, attribute, value)`

#### `def set_timing_attribute_uint64(self, task, attribute, value)`

#### `def set_trig_attribute_bool(self, task, attribute, value)`

#### `def set_trig_attribute_double(self, task, attribute, value)`

#### `def set_trig_attribute_double_array(self, task, attribute, value)`

#### `def set_trig_attribute_int32(self, task, attribute, value)`

#### `def set_trig_attribute_int32_array(self, task, attribute, value)`

#### `def set_trig_attribute_string(self, task, attribute, value)`

#### `def set_trig_attribute_timestamp(self, task, attribute, value)`

#### `def set_trig_attribute_uint32(self, task, attribute, value)`

#### `def set_watchdog_attribute_bool(self, task, lines, attribute, value)`

#### `def set_watchdog_attribute_double(self, task, lines, attribute, value)`

#### `def set_watchdog_attribute_int32(self, task, lines, attribute, value)`

#### `def set_watchdog_attribute_string(self, task, lines, attribute, value)`

#### `def set_write_attribute_bool(self, task, attribute, value)`

#### `def set_write_attribute_double(self, task, attribute, value)`

#### `def set_write_attribute_int32(self, task, attribute, value)`

#### `def set_write_attribute_string(self, task, attribute, value)`

#### `def set_write_attribute_uint32(self, task, attribute, value)`

#### `def set_write_attribute_uint64(self, task, attribute, value)`

#### `def start_new_file(self, task, file_path)`

#### `def start_task(self, task)`

#### `def stop_task(self, task)`

#### `def task_control(self, task, action)`

#### `def tristate_output_term(self, output_terminal)`

#### `def unregister_done_event(self, task)`

#### `def unregister_every_n_samples_event(self, task, every_n_samples_event_type)`

#### `def unregister_signal_event(self, task, signal_id)`

#### `def unreserve_network_device(self, device_name)`

#### `def wait_for_valid_timestamp(self, task, timestamp_event, timeout)`

#### `def wait_until_task_done(self, task, time_to_wait)`

#### `def write_analog_f64(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_analog_scalar_f64(self, task, auto_start, timeout, value)`

#### `def write_binary_i16(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_binary_i32(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_binary_u16(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_binary_u32(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_ctr_freq(self, task, num_samps_per_chan, auto_start, timeout, data_layout, frequency, duty_cycle)`

#### `def write_ctr_freq_scalar(self, task, auto_start, timeout, frequency, duty_cycle)`

#### `def write_ctr_ticks(self, task, num_samps_per_chan, auto_start, timeout, data_layout, high_ticks, low_ticks)`

#### `def write_ctr_ticks_scalar(self, task, auto_start, timeout, high_ticks, low_ticks)`

#### `def write_ctr_time(self, task, num_samps_per_chan, auto_start, timeout, data_layout, high_time, low_time)`

#### `def write_ctr_time_scalar(self, task, auto_start, timeout, high_time, low_time)`

#### `def write_digital_lines(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_digital_scalar_u32(self, task, auto_start, timeout, value)`

#### `def write_digital_u16(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_digital_u32(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_digital_u8(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_id_pin_memory(self, device_name, id_pin_name, data, format_code)`

#### `def write_raw(self, task, num_samps, auto_start, timeout, write_array)`

#### `def write_to_teds_from_array(self, physical_channel, bit_stream, basic_teds_options)`

#### `def write_to_teds_from_file(self, physical_channel, file_path, basic_teds_options)`

#### `def hash_task_handle(self, task_handle)`

#### `def driver_version(self)`

#### `def read_analog_waveform(self, task_handle: object, number_of_samples_per_channel: int, timeout: float, waveform: AnalogWaveform[numpy.float64], waveform_attribute_mode: WaveformAttributeMode) -> int`

#### `def read_analog_waveforms(self, task_handle: object, number_of_samples_per_channel: int, timeout: float, waveforms: Sequence[AnalogWaveform[numpy.float64]], waveform_attribute_mode: WaveformAttributeMode) -> int`

#### `def read_digital_waveform(self, task_handle: object, number_of_samples_per_channel: int, timeout: float, waveform: DigitalWaveform[Any], waveform_attribute_mode: WaveformAttributeMode) -> int`

#### `def read_digital_waveforms(self, task_handle: object, channel_count: int, number_of_samples_per_channel: int, number_of_signals_per_sample: int, timeout: float, waveforms: Sequence[DigitalWaveform[Any]], waveform_attribute_mode: WaveformAttributeMode) -> int`

#### `def read_new_digital_waveforms(self, task_handle: object, channel_count: int, number_of_samples_per_channel: int, number_of_signals_per_sample: int, timeout: float, waveform_attribute_mode: WaveformAttributeMode) -> Sequence[DigitalWaveform[numpy.uint8]]`

#### `def write_analog_waveform(self, task_handle: object, waveform: AnalogWaveform[Any], auto_start: bool, timeout: float) -> int`

#### `def write_analog_waveforms(self, task_handle: object, waveforms: Sequence[AnalogWaveform[Any]], auto_start: bool, timeout: float) -> int`

#### `def write_digital_waveform(self, task_handle: object, waveform: DigitalWaveform[Any], auto_start: bool, timeout: float) -> int`

#### `def write_digital_waveforms(self, task_handle: object, waveform: Sequence[DigitalWaveform[Any]], auto_start: bool, timeout: float) -> int`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/_bitfield_utils.py -->
## PYTHON MODULE: generated/nidaqmx/_bitfield_utils.py

### `def enum_bitfield_to_list(bitfield_value, bitfield_enum_type, actual_enum_type)`

Converts a bitfield value to a list of enums.

    Args:
        bitfield_value (int): Specifies the value of the bitfield.
        bitfield_enum_type (enum.Enum): Specifies the bitfield enum type
            from which to mask and extract the enum values.
        actual_enum_type (enum.Enum): Specifies the actual enum type.

    Returns:
        List[enum.Enum]: Indicates the converted list of enums.
    

### `def enum_list_to_bitfield(enum_list, bitfield_enum_type)`

Converts a list of enums to a bitfield value.

    Args:
        enum_list (List[enum.Enum]): Specifies the list of enums.
        bitfield_enum_type (enum.Enum): Specifies the bitfield enum type
            from which to mask and extract the enum values.

    Returns:
        int: Indicates the value of the bitfield.
    

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/_dotenv_path.py -->
## PYTHON MODULE: generated/nidaqmx/_dotenv_path.py

### `def get_dotenv_search_path() -> Path`

Get the search path for loading the `.env` file.

### `def _has_dotenv_file(dir: Path) -> bool`

Check whether the dir or its parents contains a `.env` file.

### `def _get_script_or_exe_path() -> Path | None`

Get the path of the top-level script or PyInstaller EXE, if possible.

### `def _get_caller_path() -> Path | None`

Get the path of the module calling into this package, if possible.

### `def _get_package_path() -> Path`

Get the path of this package.

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/_feature_toggles.py -->
## PYTHON MODULE: generated/nidaqmx/_feature_toggles.py

### MODULE DOCSTRING

nidaqmx feature toggles.

- `_PREFIX = 'NIDAQMX'`

### `class _OrderedEnum(Enum)`

#### `def __ge__(self, other: Self) -> bool`

#### `def __gt__(self, other: Self) -> bool`

#### `def __le__(self, other: Self) -> bool`

#### `def __lt__(self, other: Self) -> bool`

### `class CodeReadiness(_OrderedEnum)`

Indicates whether code is ready to be supported.

### `def _init_code_readiness_level() -> CodeReadiness`

- `_CODE_READINESS_LEVEL = _init_code_readiness_level()`

### `def get_code_readiness_level() -> CodeReadiness`

Get the current code readiness level.

    You can override this in tests by specifying the ``use_code_readiness``
    mark.
    

### `class FeatureToggle()`

A run-time feature toggle.

#### `def __init__(self, name: str, readiness: CodeReadiness) -> None`

Initialize the feature toggle.

#### `def is_enabled(self) -> bool`

Indicates whether the feature is currently enabled.

        You can enable/disable features in tests by specifying the
        ``enable_feature_toggle`` or ``disable_feature_toggle`` marks.
        

#### `def raise_if_disabled(self) -> None`

Raises an error if the feature is disabled.

### `def requires_feature(feature_toggle: FeatureToggle) -> Callable[[Callable[_P, _T]], Callable[_P, _T]]`

Decorator specifying that the function requires the specified feature toggle.

- `WAVEFORM_SUPPORT = FeatureToggle('WAVEFORM_SUPPORT', CodeReadiness.RELEASE)`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/_grpc_interpreter.py -->
## PYTHON MODULE: generated/nidaqmx/_grpc_interpreter.py

- `_UNABLE_TO_LOCATE_ERROR_RESOURCES_ERROR_MESSAGE = 'Error code could not be found. Reinstalling the driver might fix the issue. Otherwise, contact National Instruments technical support.'`

### `class GrpcEventHandler(BaseEventHandler, Generic[TEventResponse])`

Manage the lifetime of a gRPC event stream.

#### `def __init__(self, event_name: str, interpreter: GrpcStubInterpreter, event_stream: grpc._CallIterator[TEventResponse], event_callback: Callable[[TEventResponse], None]) -> None`

#### `def close(self) -> None`

#### `def _thread_main(self) -> None`

### `class GrpcStubInterpreter(BaseInterpreter)`

Interpreter for interacting with a gRPC Stub class

#### `def __init__(self, grpc_options)`

#### `def _invoke(self, func, request, metadata=None)`

#### `def _handle_rpc_error(self, rpc_error)`

#### `def _check_for_error_from_response(self, error_code, samps_per_chan_written=None, samps_per_chan_read=None)`

#### `def _raise_error(self, error_code, error_message, samps_per_chan_written=None, samps_per_chan_read=None)`

#### `def _check_for_event_registration_error(self, event_stream)`

#### `def driver_version(self)`

#### `def add_cdaq_sync_connection(self, port_list)`

#### `def add_global_chans_to_task(self, task, channel_names)`

#### `def add_network_device(self, ip_address, device_name, attempt_reservation, timeout)`

#### `def are_configured_cdaq_sync_ports_disconnected(self, chassis_devices_ports, timeout)`

#### `def auto_configure_cdaq_sync_connections(self, chassis_devices_ports, timeout)`

#### `def calculate_reverse_poly_coeff(self, forward_coeffs, min_val_x, max_val_x, num_points_to_compute, reverse_poly_order)`

#### `def cfg_anlg_edge_ref_trig(self, task, trigger_source, pretrigger_samples, trigger_slope, trigger_level)`

#### `def cfg_anlg_edge_start_trig(self, task, trigger_source, trigger_slope, trigger_level)`

#### `def cfg_anlg_multi_edge_ref_trig(self, task, trigger_sources, pretrigger_samples, trigger_slope_array, trigger_level_array)`

#### `def cfg_anlg_multi_edge_start_trig(self, task, trigger_sources, trigger_slope_array, trigger_level_array)`

#### `def cfg_anlg_window_ref_trig(self, task, trigger_source, window_top, window_bottom, pretrigger_samples, trigger_when)`

#### `def cfg_anlg_window_start_trig(self, task, window_top, window_bottom, trigger_source, trigger_when)`

#### `def cfg_burst_handshaking_timing_export_clock(self, task, sample_clk_rate, sample_clk_outp_term, sample_mode, samps_per_chan, sample_clk_pulse_polarity, pause_when, ready_event_active_level)`

#### `def cfg_burst_handshaking_timing_import_clock(self, task, sample_clk_rate, sample_clk_src, sample_mode, samps_per_chan, sample_clk_active_edge, pause_when, ready_event_active_level)`

#### `def cfg_change_detection_timing(self, task, rising_edge_chan, falling_edge_chan, sample_mode, samps_per_chan)`

#### `def cfg_dig_edge_ref_trig(self, task, trigger_source, pretrigger_samples, trigger_edge)`

#### `def cfg_dig_edge_start_trig(self, task, trigger_source, trigger_edge)`

#### `def cfg_dig_pattern_ref_trig(self, task, trigger_source, trigger_pattern, pretrigger_samples, trigger_when)`

#### `def cfg_dig_pattern_start_trig(self, task, trigger_source, trigger_pattern, trigger_when)`

#### `def cfg_handshaking_timing(self, task, sample_mode, samps_per_chan)`

#### `def cfg_implicit_timing(self, task, sample_mode, samps_per_chan)`

#### `def cfg_pipelined_samp_clk_timing(self, task, rate, source, active_edge, sample_mode, samps_per_chan)`

#### `def cfg_samp_clk_timing(self, task, rate, source, active_edge, sample_mode, samps_per_chan)`

#### `def cfg_time_start_trig(self, task, when, timescale)`

#### `def cfg_watchdog_ao_expir_states(self, task, channel_names, expir_state_array, output_type_array)`

#### `def cfg_watchdog_co_expir_states(self, task, channel_names, expir_state_array)`

#### `def cfg_watchdog_do_expir_states(self, task, channel_names, expir_state_array)`

#### `def clear_task(self, task)`

#### `def clear_teds(self, physical_channel)`

#### `def configure_logging(self, task, file_path, logging_mode, group_name, operation)`

#### `def configure_teds(self, physical_channel, file_path)`

#### `def connect_terms(self, source_terminal, destination_terminal, signal_modifiers)`

#### `def control_watchdog_task(self, task, action)`

#### `def create_ai_accel4_wire_dc_voltage_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, sensitivity, sensitivity_units, voltage_excit_source, voltage_excit_val, use_excit_for_scaling, custom_scale_name)`

#### `def create_ai_accel_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, sensitivity, sensitivity_units, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_ai_accel_charge_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, sensitivity, sensitivity_units, custom_scale_name)`

#### `def create_ai_bridge_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, custom_scale_name)`

#### `def create_ai_calculated_power_chan(self, task, voltage_physical_channel, current_physical_channel, name_to_assign_to_channel, terminal_config, voltage_min_val, voltage_max_val, current_min_val, current_max_val, units, shunt_resistor_loc, ext_shunt_resistor_val, custom_scale_name)`

#### `def create_ai_charge_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, custom_scale_name)`

#### `def create_ai_current_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, shunt_resistor_loc, ext_shunt_resistor_val, custom_scale_name)`

#### `def create_ai_current_rms_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, shunt_resistor_loc, ext_shunt_resistor_val, custom_scale_name)`

#### `def create_ai_force_bridge_polynomial_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, forward_coeffs, reverse_coeffs, electrical_units, physical_units, custom_scale_name)`

#### `def create_ai_force_bridge_table_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, electrical_vals, electrical_units, physical_vals, physical_units, custom_scale_name)`

#### `def create_ai_force_bridge_two_point_lin_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, first_electrical_val, second_electrical_val, electrical_units, first_physical_val, second_physical_val, physical_units, custom_scale_name)`

#### `def create_ai_force_iepe_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, sensitivity, sensitivity_units, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_ai_freq_voltage_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, threshold_level, hysteresis, custom_scale_name)`

#### `def create_ai_microphone_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, units, mic_sensitivity, max_snd_press_level, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_ai_pos_eddy_curr_prox_probe_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, sensitivity, sensitivity_units, custom_scale_name)`

#### `def create_ai_pos_lvdt_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, sensitivity, sensitivity_units, voltage_excit_source, voltage_excit_val, voltage_excit_freq, ac_excit_wire_mode, custom_scale_name)`

#### `def create_ai_pos_rvdt_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, sensitivity, sensitivity_units, voltage_excit_source, voltage_excit_val, voltage_excit_freq, ac_excit_wire_mode, custom_scale_name)`

#### `def create_ai_power_chan(self, task, physical_channel, voltage_setpoint, current_setpoint, output_enable, name_to_assign_to_channel)`

#### `def create_ai_pressure_bridge_polynomial_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, forward_coeffs, reverse_coeffs, electrical_units, physical_units, custom_scale_name)`

#### `def create_ai_pressure_bridge_table_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, electrical_vals, electrical_units, physical_vals, physical_units, custom_scale_name)`

#### `def create_ai_pressure_bridge_two_point_lin_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, first_electrical_val, second_electrical_val, electrical_units, first_physical_val, second_physical_val, physical_units, custom_scale_name)`

#### `def create_ai_resistance_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, resistance_config, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_ai_rosette_strain_gage_chan(self, task, physical_channel, rosette_type, gage_orientation, rosette_meas_types, name_to_assign_to_channel, min_val, max_val, strain_config, voltage_excit_source, voltage_excit_val, gage_factor, nominal_gage_resistance, poisson_ratio, lead_wire_resistance)`

#### `def create_ai_strain_gage_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, strain_config, voltage_excit_source, voltage_excit_val, gage_factor, initial_bridge_voltage, nominal_gage_resistance, poisson_ratio, lead_wire_resistance, custom_scale_name)`

#### `def create_ai_temp_built_in_sensor_chan(self, task, physical_channel, name_to_assign_to_channel, units)`

#### `def create_ai_thrmcpl_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, thermocouple_type, cjc_source, cjc_val, cjc_channel)`

#### `def create_ai_thrmstr_chan_iex(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, resistance_config, current_excit_source, current_excit_val, a, b, c)`

#### `def create_ai_thrmstr_chan_vex(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, resistance_config, voltage_excit_source, voltage_excit_val, a, b, c, r_1)`

#### `def create_ai_torque_bridge_polynomial_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, forward_coeffs, reverse_coeffs, electrical_units, physical_units, custom_scale_name)`

#### `def create_ai_torque_bridge_table_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, electrical_vals, electrical_units, physical_vals, physical_units, custom_scale_name)`

#### `def create_ai_torque_bridge_two_point_lin_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, first_electrical_val, second_electrical_val, electrical_units, first_physical_val, second_physical_val, physical_units, custom_scale_name)`

#### `def create_ai_velocity_iepe_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, sensitivity, sensitivity_units, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_ai_voltage_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, custom_scale_name)`

#### `def create_ai_voltage_chan_with_excit(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, use_excit_for_scaling, custom_scale_name)`

#### `def create_ai_voltage_rms_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, custom_scale_name)`

#### `def create_airtd_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, rtd_type, resistance_config, current_excit_source, current_excit_val, r_0)`

#### `def create_ao_current_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, custom_scale_name)`

#### `def create_ao_func_gen_chan(self, task, physical_channel, name_to_assign_to_channel, type, freq, amplitude, offset)`

#### `def create_ao_voltage_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, custom_scale_name)`

#### `def create_ci_ang_encoder_chan(self, task, counter, name_to_assign_to_channel, decoding_type, zidx_enable, zidx_val, zidx_phase, units, pulses_per_rev, initial_angle, custom_scale_name)`

#### `def create_ci_ang_velocity_chan(self, task, counter, name_to_assign_to_channel, min_val, max_val, decoding_type, units, pulses_per_rev, custom_scale_name)`

#### `def create_ci_count_edges_chan(self, task, counter, name_to_assign_to_channel, edge, initial_count, count_direction)`

#### `def create_ci_duty_cycle_chan(self, task, counter, name_to_assign_to_channel, min_freq, max_freq, edge, custom_scale_name)`

#### `def create_ci_freq_chan(self, task, counter, name_to_assign_to_channel, min_val, max_val, units, edge, meas_method, meas_time, divisor, custom_scale_name)`

#### `def create_ci_lin_encoder_chan(self, task, counter, name_to_assign_to_channel, decoding_type, zidx_enable, zidx_val, zidx_phase, units, dist_per_pulse, initial_pos, custom_scale_name)`

#### `def create_ci_lin_velocity_chan(self, task, counter, name_to_assign_to_channel, min_val, max_val, decoding_type, units, dist_per_pulse, custom_scale_name)`

#### `def create_ci_period_chan(self, task, counter, name_to_assign_to_channel, min_val, max_val, units, edge, meas_method, meas_time, divisor, custom_scale_name)`

#### `def create_ci_pulse_chan_freq(self, task, counter, name_to_assign_to_channel, min_val, max_val, units)`

#### `def create_ci_pulse_chan_ticks(self, task, counter, name_to_assign_to_channel, source_terminal, min_val, max_val)`

#### `def create_ci_pulse_chan_time(self, task, counter, name_to_assign_to_channel, min_val, max_val, units)`

#### `def create_ci_pulse_width_chan(self, task, counter, name_to_assign_to_channel, min_val, max_val, units, starting_edge, custom_scale_name)`

#### `def create_ci_semi_period_chan(self, task, counter, name_to_assign_to_channel, min_val, max_val, units, custom_scale_name)`

#### `def create_ci_two_edge_sep_chan(self, task, counter, name_to_assign_to_channel, min_val, max_val, units, first_edge, second_edge, custom_scale_name)`

#### `def create_cigps_timestamp_chan(self, task, counter, name_to_assign_to_channel, units, sync_method, custom_scale_name)`

#### `def create_co_pulse_chan_freq(self, task, counter, name_to_assign_to_channel, units, idle_state, initial_delay, freq, duty_cycle)`

#### `def create_co_pulse_chan_ticks(self, task, counter, source_terminal, name_to_assign_to_channel, idle_state, initial_delay, low_ticks, high_ticks)`

#### `def create_co_pulse_chan_time(self, task, counter, name_to_assign_to_channel, units, idle_state, initial_delay, low_time, high_time)`

#### `def create_di_chan(self, task, lines, name_to_assign_to_lines, line_grouping)`

#### `def create_do_chan(self, task, lines, name_to_assign_to_lines, line_grouping)`

#### `def create_lin_scale(self, name, slope, y_intercept, pre_scaled_units, scaled_units)`

#### `def create_map_scale(self, name, prescaled_min, prescaled_max, scaled_min, scaled_max, pre_scaled_units, scaled_units)`

#### `def create_polynomial_scale(self, name, forward_coeffs, reverse_coeffs, pre_scaled_units, scaled_units)`

#### `def create_table_scale(self, name, prescaled_vals, scaled_vals, pre_scaled_units, scaled_units)`

#### `def create_task(self, session_name)`

#### `def create_tedsai_accel_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_tedsai_bridge_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, voltage_excit_source, voltage_excit_val, custom_scale_name)`

#### `def create_tedsai_current_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, shunt_resistor_loc, ext_shunt_resistor_val, custom_scale_name)`

#### `def create_tedsai_force_bridge_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, voltage_excit_source, voltage_excit_val, custom_scale_name)`

#### `def create_tedsai_force_iepe_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_tedsai_microphone_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, units, max_snd_press_level, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_tedsai_pos_lvdt_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, voltage_excit_source, voltage_excit_val, voltage_excit_freq, ac_excit_wire_mode, custom_scale_name)`

#### `def create_tedsai_pos_rvdt_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, voltage_excit_source, voltage_excit_val, voltage_excit_freq, ac_excit_wire_mode, custom_scale_name)`

#### `def create_tedsai_pressure_bridge_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, voltage_excit_source, voltage_excit_val, custom_scale_name)`

#### `def create_tedsai_resistance_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, resistance_config, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_tedsai_strain_gage_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, voltage_excit_source, voltage_excit_val, initial_bridge_voltage, lead_wire_resistance, custom_scale_name)`

#### `def create_tedsai_thrmcpl_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, cjc_source, cjc_val, cjc_channel)`

#### `def create_tedsai_thrmstr_chan_iex(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, resistance_config, current_excit_source, current_excit_val)`

#### `def create_tedsai_thrmstr_chan_vex(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, resistance_config, voltage_excit_source, voltage_excit_val, r_1)`

#### `def create_tedsai_torque_bridge_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, voltage_excit_source, voltage_excit_val, custom_scale_name)`

#### `def create_tedsai_voltage_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, custom_scale_name)`

#### `def create_tedsai_voltage_chan_with_excit(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, voltage_excit_source, voltage_excit_val, custom_scale_name)`

#### `def create_tedsairtd_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, resistance_config, current_excit_source, current_excit_val)`

#### `def create_watchdog_timer_task_ex(self, device_name, session_name, timeout)`

#### `def delete_network_device(self, device_name)`

#### `def delete_saved_global_chan(self, channel_name)`

#### `def delete_saved_scale(self, scale_name)`

#### `def delete_saved_task(self, task_name)`

#### `def device_supports_cal(self, device_name)`

#### `def disable_ref_trig(self, task)`

#### `def disable_start_trig(self, task)`

#### `def disconnect_terms(self, source_terminal, destination_terminal)`

#### `def export_signal(self, task, signal_id, output_terminal)`

#### `def get_analog_power_up_states_with_output_type(self, channel_names, array_size)`

#### `def get_auto_configured_cdaq_sync_connections(self)`

#### `def get_buffer_attribute_uint32(self, task, attribute)`

#### `def get_cal_info_attribute_bool(self, device_name, attribute)`

#### `def get_cal_info_attribute_double(self, device_name, attribute)`

#### `def get_cal_info_attribute_string(self, device_name, attribute)`

#### `def get_cal_info_attribute_uint32(self, device_name, attribute)`

#### `def get_chan_attribute_bool(self, task, channel, attribute)`

#### `def get_chan_attribute_double(self, task, channel, attribute)`

#### `def get_chan_attribute_double_array(self, task, channel, attribute)`

#### `def get_chan_attribute_int32(self, task, channel, attribute)`

#### `def get_chan_attribute_string(self, task, channel, attribute)`

#### `def get_chan_attribute_uint32(self, task, channel, attribute)`

#### `def get_device_attribute_bool(self, device_name, attribute)`

#### `def get_device_attribute_double(self, device_name, attribute)`

#### `def get_device_attribute_double_array(self, device_name, attribute)`

#### `def get_device_attribute_int32(self, device_name, attribute)`

#### `def get_device_attribute_int32_array(self, device_name, attribute)`

#### `def get_device_attribute_string(self, device_name, attribute)`

#### `def get_device_attribute_uint32(self, device_name, attribute)`

#### `def get_device_attribute_uint32_array(self, device_name, attribute)`

#### `def get_digital_logic_family_power_up_state(self, device_name)`

#### `def get_digital_power_up_states(self, device_name, channel_name)`

#### `def get_digital_pull_up_pull_down_states(self, device_name, channel_name)`

#### `def get_disconnected_cdaq_sync_ports(self)`

#### `def get_exported_signal_attribute_bool(self, task, attribute)`

#### `def get_exported_signal_attribute_double(self, task, attribute)`

#### `def get_exported_signal_attribute_int32(self, task, attribute)`

#### `def get_exported_signal_attribute_string(self, task, attribute)`

#### `def get_exported_signal_attribute_uint32(self, task, attribute)`

#### `def get_ext_cal_last_date_and_time(self, device_name)`

#### `def get_persisted_chan_attribute_bool(self, channel, attribute)`

#### `def get_persisted_chan_attribute_string(self, channel, attribute)`

#### `def get_persisted_scale_attribute_bool(self, scale_name, attribute)`

#### `def get_persisted_scale_attribute_string(self, scale_name, attribute)`

#### `def get_persisted_task_attribute_bool(self, task_name, attribute)`

#### `def get_persisted_task_attribute_string(self, task_name, attribute)`

#### `def get_physical_chan_attribute_bool(self, physical_channel, attribute)`

#### `def get_physical_chan_attribute_bytes(self, physical_channel, attribute)`

#### `def get_physical_chan_attribute_double(self, physical_channel, attribute)`

#### `def get_physical_chan_attribute_double_array(self, physical_channel, attribute)`

#### `def get_physical_chan_attribute_int32(self, physical_channel, attribute)`

#### `def get_physical_chan_attribute_int32_array(self, physical_channel, attribute)`

#### `def get_physical_chan_attribute_string(self, physical_channel, attribute)`

#### `def get_physical_chan_attribute_uint32(self, physical_channel, attribute)`

#### `def get_physical_chan_attribute_uint32_array(self, physical_channel, attribute)`

#### `def get_read_attribute_bool(self, task, attribute)`

#### `def get_read_attribute_double(self, task, attribute)`

#### `def get_read_attribute_int32(self, task, attribute)`

#### `def get_read_attribute_string(self, task, attribute, size_hint=0)`

#### `def get_read_attribute_uint32(self, task, attribute)`

#### `def get_read_attribute_uint64(self, task, attribute)`

#### `def get_scale_attribute_double(self, scale_name, attribute)`

#### `def get_scale_attribute_double_array(self, scale_name, attribute)`

#### `def get_scale_attribute_int32(self, scale_name, attribute)`

#### `def get_scale_attribute_string(self, scale_name, attribute)`

#### `def get_self_cal_last_date_and_time(self, device_name)`

#### `def get_system_info_attribute_string(self, attribute)`

#### `def get_system_info_attribute_uint32(self, attribute)`

#### `def get_task_attribute_bool(self, task, attribute)`

#### `def get_task_attribute_string(self, task, attribute)`

#### `def get_task_attribute_uint32(self, task, attribute)`

#### `def get_timing_attribute_bool(self, task, attribute)`

#### `def get_timing_attribute_double(self, task, attribute)`

#### `def get_timing_attribute_ex_bool(self, task, device_names, attribute)`

#### `def get_timing_attribute_ex_double(self, task, device_names, attribute)`

#### `def get_timing_attribute_ex_int32(self, task, device_names, attribute)`

#### `def get_timing_attribute_ex_string(self, task, device_names, attribute)`

#### `def get_timing_attribute_ex_uint32(self, task, device_names, attribute)`

#### `def get_timing_attribute_ex_uint64(self, task, device_names, attribute)`

#### `def get_timing_attribute_int32(self, task, attribute)`

#### `def get_timing_attribute_string(self, task, attribute)`

#### `def get_timing_attribute_timestamp(self, task, attribute)`

#### `def get_timing_attribute_uint32(self, task, attribute)`

#### `def get_timing_attribute_uint64(self, task, attribute)`

#### `def get_trig_attribute_bool(self, task, attribute)`

#### `def get_trig_attribute_double(self, task, attribute)`

#### `def get_trig_attribute_double_array(self, task, attribute)`

#### `def get_trig_attribute_int32(self, task, attribute)`

#### `def get_trig_attribute_int32_array(self, task, attribute)`

#### `def get_trig_attribute_string(self, task, attribute)`

#### `def get_trig_attribute_timestamp(self, task, attribute)`

#### `def get_trig_attribute_uint32(self, task, attribute)`

#### `def get_watchdog_attribute_bool(self, task, lines, attribute)`

#### `def get_watchdog_attribute_double(self, task, lines, attribute)`

#### `def get_watchdog_attribute_int32(self, task, lines, attribute)`

#### `def get_watchdog_attribute_string(self, task, lines, attribute)`

#### `def get_write_attribute_bool(self, task, attribute)`

#### `def get_write_attribute_double(self, task, attribute)`

#### `def get_write_attribute_int32(self, task, attribute)`

#### `def get_write_attribute_string(self, task, attribute, size_hint=0)`

#### `def get_write_attribute_uint32(self, task, attribute)`

#### `def get_write_attribute_uint64(self, task, attribute)`

#### `def is_task_done(self, task)`

#### `def load_task(self, session_name)`

#### `def perform_bridge_offset_nulling_cal_ex(self, task, channel, skip_unsupported_channels)`

#### `def perform_bridge_shunt_cal_ex(self, task, channel, shunt_resistor_value, shunt_resistor_location, shunt_resistor_select, shunt_resistor_source, bridge_resistance, skip_unsupported_channels)`

#### `def perform_strain_shunt_cal_ex(self, task, channel, shunt_resistor_value, shunt_resistor_location, shunt_resistor_select, shunt_resistor_source, skip_unsupported_channels)`

#### `def perform_thrmcpl_lead_offset_nulling_cal(self, task, channel, skip_unsupported_channels)`

#### `def read_analog_f64(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_analog_scalar_f64(self, task, timeout)`

#### `def read_binary_i16(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_binary_i32(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_binary_u16(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_binary_u32(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_counter_f64(self, task, num_samps_per_chan, timeout, read_array)`

#### `def read_counter_f64_ex(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_counter_scalar_f64(self, task, timeout)`

#### `def read_counter_scalar_u32(self, task, timeout)`

#### `def read_counter_u32(self, task, num_samps_per_chan, timeout, read_array)`

#### `def read_counter_u32_ex(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_ctr_freq(self, task, num_samps_per_chan, timeout, interleaved, read_array_frequency, read_array_duty_cycle)`

#### `def read_ctr_freq_scalar(self, task, timeout)`

#### `def read_ctr_ticks(self, task, num_samps_per_chan, timeout, interleaved, read_array_high_ticks, read_array_low_ticks)`

#### `def read_ctr_ticks_scalar(self, task, timeout)`

#### `def read_ctr_time(self, task, num_samps_per_chan, timeout, interleaved, read_array_high_time, read_array_low_time)`

#### `def read_ctr_time_scalar(self, task, timeout)`

#### `def read_digital_lines(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_digital_scalar_u32(self, task, timeout)`

#### `def read_digital_u16(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_digital_u32(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_digital_u8(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_power_binary_i16(self, task, num_samps_per_chan, timeout, fill_mode, read_array_voltage, read_array_current)`

#### `def read_power_f64(self, task, num_samps_per_chan, timeout, fill_mode, read_array_voltage, read_array_current)`

#### `def read_power_scalar_f64(self, task, timeout)`

#### `def read_raw(self, task, num_samps_per_chan, timeout, read_array)`

#### `def register_done_event(self, task, options, callback_function, callback_data)`

#### `def register_every_n_samples_event(self, task, every_n_samples_event_type, n_samples, options, callback_function, callback_data)`

#### `def register_signal_event(self, task, signal_id, options, callback_function, callback_data)`

#### `def remove_cdaq_sync_connection(self, port_list)`

#### `def reserve_network_device(self, device_name, override_reservation)`

#### `def reset_buffer_attribute(self, task, attribute)`

#### `def reset_chan_attribute(self, task, channel, attribute)`

#### `def reset_device(self, device_name)`

#### `def reset_exported_signal_attribute(self, task, attribute)`

#### `def reset_read_attribute(self, task, attribute)`

#### `def reset_timing_attribute(self, task, attribute)`

#### `def reset_timing_attribute_ex(self, task, device_names, attribute)`

#### `def reset_trig_attribute(self, task, attribute)`

#### `def reset_watchdog_attribute(self, task, lines, attribute)`

#### `def reset_write_attribute(self, task, attribute)`

#### `def restore_last_ext_cal_const(self, device_name)`

#### `def save_global_chan(self, task, channel_name, save_as, author, options)`

#### `def save_scale(self, scale_name, save_as, author, options)`

#### `def save_task(self, task, save_as, author, options)`

#### `def self_cal(self, device_name)`

#### `def self_test_device(self, device_name)`

#### `def set_analog_power_up_states(self, device_name, channel_names, state, channel_type)`

#### `def set_analog_power_up_states_with_output_type(self, channel_names, state_array, channel_type_array)`

#### `def set_buffer_attribute_uint32(self, task, attribute, value)`

#### `def set_cal_info_attribute_bool(self, device_name, attribute, value)`

#### `def set_cal_info_attribute_double(self, device_name, attribute, value)`

#### `def set_cal_info_attribute_string(self, device_name, attribute, value)`

#### `def set_cal_info_attribute_uint32(self, device_name, attribute, value)`

#### `def set_chan_attribute_bool(self, task, channel, attribute, value)`

#### `def set_chan_attribute_double(self, task, channel, attribute, value)`

#### `def set_chan_attribute_double_array(self, task, channel, attribute, value)`

#### `def set_chan_attribute_int32(self, task, channel, attribute, value)`

#### `def set_chan_attribute_string(self, task, channel, attribute, value)`

#### `def set_chan_attribute_uint32(self, task, channel, attribute, value)`

#### `def set_digital_logic_family_power_up_state(self, device_name, logic_family)`

#### `def set_digital_power_up_states(self, device_name, channel_names, state)`

#### `def set_digital_pull_up_pull_down_states(self, device_name, channel_names, state)`

#### `def set_exported_signal_attribute_bool(self, task, attribute, value)`

#### `def set_exported_signal_attribute_double(self, task, attribute, value)`

#### `def set_exported_signal_attribute_int32(self, task, attribute, value)`

#### `def set_exported_signal_attribute_string(self, task, attribute, value)`

#### `def set_exported_signal_attribute_uint32(self, task, attribute, value)`

#### `def set_read_attribute_bool(self, task, attribute, value)`

#### `def set_read_attribute_double(self, task, attribute, value)`

#### `def set_read_attribute_int32(self, task, attribute, value)`

#### `def set_read_attribute_string(self, task, attribute, value)`

#### `def set_read_attribute_uint32(self, task, attribute, value)`

#### `def set_read_attribute_uint64(self, task, attribute, value)`

#### `def set_scale_attribute_double(self, scale_name, attribute, value)`

#### `def set_scale_attribute_double_array(self, scale_name, attribute, value)`

#### `def set_scale_attribute_int32(self, scale_name, attribute, value)`

#### `def set_scale_attribute_string(self, scale_name, attribute, value)`

#### `def set_timing_attribute_bool(self, task, attribute, value)`

#### `def set_timing_attribute_double(self, task, attribute, value)`

#### `def set_timing_attribute_ex_bool(self, task, device_names, attribute, value)`

#### `def set_timing_attribute_ex_double(self, task, device_names, attribute, value)`

#### `def set_timing_attribute_ex_int32(self, task, device_names, attribute, value)`

#### `def set_timing_attribute_ex_string(self, task, device_names, attribute, value)`

#### `def set_timing_attribute_ex_uint32(self, task, device_names, attribute, value)`

#### `def set_timing_attribute_ex_uint64(self, task, device_names, attribute, value)`

#### `def set_timing_attribute_int32(self, task, attribute, value)`

#### `def set_timing_attribute_string(self, task, attribute, value)`

#### `def set_timing_attribute_uint32(self, task, attribute, value)`

#### `def set_timing_attribute_uint64(self, task, attribute, value)`

#### `def set_trig_attribute_bool(self, task, attribute, value)`

#### `def set_trig_attribute_double(self, task, attribute, value)`

#### `def set_trig_attribute_double_array(self, task, attribute, value)`

#### `def set_trig_attribute_int32(self, task, attribute, value)`

#### `def set_trig_attribute_int32_array(self, task, attribute, value)`

#### `def set_trig_attribute_string(self, task, attribute, value)`

#### `def set_trig_attribute_timestamp(self, task, attribute, value)`

#### `def set_trig_attribute_uint32(self, task, attribute, value)`

#### `def set_watchdog_attribute_bool(self, task, lines, attribute, value)`

#### `def set_watchdog_attribute_double(self, task, lines, attribute, value)`

#### `def set_watchdog_attribute_int32(self, task, lines, attribute, value)`

#### `def set_watchdog_attribute_string(self, task, lines, attribute, value)`

#### `def set_write_attribute_bool(self, task, attribute, value)`

#### `def set_write_attribute_double(self, task, attribute, value)`

#### `def set_write_attribute_int32(self, task, attribute, value)`

#### `def set_write_attribute_string(self, task, attribute, value)`

#### `def set_write_attribute_uint32(self, task, attribute, value)`

#### `def set_write_attribute_uint64(self, task, attribute, value)`

#### `def start_new_file(self, task, file_path)`

#### `def start_task(self, task)`

#### `def stop_task(self, task)`

#### `def task_control(self, task, action)`

#### `def tristate_output_term(self, output_terminal)`

#### `def unregister_done_event(self, task)`

#### `def unregister_every_n_samples_event(self, task, every_n_samples_event_type)`

#### `def unregister_signal_event(self, task, signal_id)`

#### `def unreserve_network_device(self, device_name)`

#### `def wait_for_valid_timestamp(self, task, timestamp_event, timeout)`

#### `def wait_until_task_done(self, task, time_to_wait)`

#### `def write_analog_f64(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_analog_scalar_f64(self, task, auto_start, timeout, value)`

#### `def write_binary_i16(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_binary_i32(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_binary_u16(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_binary_u32(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_ctr_freq(self, task, num_samps_per_chan, auto_start, timeout, data_layout, frequency, duty_cycle)`

#### `def write_ctr_freq_scalar(self, task, auto_start, timeout, frequency, duty_cycle)`

#### `def write_ctr_ticks(self, task, num_samps_per_chan, auto_start, timeout, data_layout, high_ticks, low_ticks)`

#### `def write_ctr_ticks_scalar(self, task, auto_start, timeout, high_ticks, low_ticks)`

#### `def write_ctr_time(self, task, num_samps_per_chan, auto_start, timeout, data_layout, high_time, low_time)`

#### `def write_ctr_time_scalar(self, task, auto_start, timeout, high_time, low_time)`

#### `def write_digital_lines(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_digital_scalar_u32(self, task, auto_start, timeout, value)`

#### `def write_digital_u16(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_digital_u32(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_digital_u8(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_id_pin_memory(self, device_name, id_pin_name, data, format_code)`

#### `def write_raw(self, task, num_samps, auto_start, timeout, write_array)`

#### `def write_to_teds_from_array(self, physical_channel, bit_stream, basic_teds_options)`

#### `def write_to_teds_from_file(self, physical_channel, file_path, basic_teds_options)`

#### `def hash_task_handle(self, task_handle)`

#### `def get_error_string(self, error_code)`

#### `def read_id_pin_memory(self, device_name, id_pin_name)`

#### `def set_runtime_environment(self, environment, environment_version, reserved_1, reserved_2)`

#### `def internal_get_last_created_chan(self)`

#### `def read_analog_waveform(self, task_handle: object, number_of_samples_per_channel: int, timeout: float, waveform: AnalogWaveform[numpy.float64], waveform_attribute_mode: WaveformAttributeMode) -> int`

#### `def read_analog_waveforms(self, task_handle: object, number_of_samples_per_channel: int, timeout: float, waveforms: Sequence[AnalogWaveform[numpy.float64]], waveform_attribute_mode: WaveformAttributeMode) -> int`

#### `def read_digital_waveform(self, task_handle: object, number_of_samples_per_channel: int, timeout: float, waveform: DigitalWaveform[Any], waveform_attribute_mode: WaveformAttributeMode) -> int`

#### `def read_digital_waveforms(self, task_handle: object, channel_count: int, number_of_samples_per_channel: int, number_of_signals_per_sample: int, timeout: float, waveforms: Sequence[DigitalWaveform[Any]], waveform_attribute_mode: WaveformAttributeMode) -> int`

#### `def read_new_digital_waveforms(self, task_handle: object, channel_count: int, number_of_samples_per_channel: int, number_of_signals_per_sample: int, timeout: float, waveform_attribute_mode: WaveformAttributeMode) -> Sequence[DigitalWaveform[numpy.uint8]]`

#### `def write_analog_waveform(self, task_handle: object, waveform: AnalogWaveform[typing.Any], auto_start: bool, timeout: float) -> int`

#### `def write_analog_waveforms(self, task_handle: object, waveforms: Sequence[AnalogWaveform[typing.Any]], auto_start: bool, timeout: float) -> int`

#### `def write_digital_waveform(self, task_handle: object, waveform: DigitalWaveform[Any], auto_start: bool, timeout: float) -> int`

#### `def write_digital_waveforms(self, task_handle: object, waveforms: Sequence[DigitalWaveform[Any]], auto_start: bool, timeout: float) -> int`

### `def _assign_numpy_array(numpy_array, grpc_array)`


    Assigns grpc array to numpy array maintaining the original shape.

    Checks for the instance of grpc_array with bytes, if validated to True,
    the numpy array is assigned to a 1D array of the grpc array.
    

### `def _validate_array_dtype(numpy_array, expected_numpy_array_dtype)`

Raises TypeError if array type doesn't match with expected numpy.dtype

### `def _is_cancelled(ex: Exception) -> bool`

Returns True if the given exception is a cancelled RPC exception.

- `_ERROR_MESSAGES = {DAQmxErrors.SAMPLES_NOT_YET_AVAILABLE: 'Some or all of the samples requested have not yet been acquired.\n\nTo wait for the samples to become available use a longer read timeout or read later in your program. To make the samples available sooner, increase the sample rate. If your task uses a start trigger, make sure that your start trigger is configured correctly. It is also possible that you configured the task for external timing, and no clock was supplied. If this is the case, supply an external clock.'}`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/_grpc_time.py -->
## PYTHON MODULE: generated/nidaqmx/_grpc_time.py

- `_BIAS_FROM_1970_EPOCH = 2082844800`

- `_NS_PER_S = 10 ** 9`

- `_NS_PER_US = 10 ** 3`

- `_YS_PER_US = 10 ** 18`

- `_YS_PER_NS = 10 ** 15`

- `_YS_PER_FS = 10 ** 9`

- `_EPOCH_1970 = ht_datetime(1970, 1, 1, tzinfo=timezone.utc)`

### `def convert_time_to_timestamp(dt: std_datetime | ht_datetime, ts: GrpcTimestamp | None=None) -> GrpcTimestamp`

### `def convert_timestamp_to_time(ts: GrpcTimestamp, tzinfo: dt_tzinfo | None=None) -> ht_datetime`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/_install_daqmx.py -->
## PYTHON MODULE: generated/nidaqmx/_install_daqmx.py

- `METADATA_FILE = '_installer_metadata.json'`

- `_NETWORK_TIMEOUT_IN_SECONDS = 60`

### `def _parse_version(version: str) -> tuple[int, ...]`

Split the version string into a tuple of integers.

    >>> _parse_version("23.8.0")
    (23, 8, 0)
    >>> _parse_version("24.0.0")
    (24, 0, 0)
    >>> _parse_version("invalid_version")
    Traceback (most recent call last):
    ...
    click.exceptions.ClickException: Invalid version format found
    

### `def _get_daqmx_installed_version() -> str | None`

Check for existing installation of NI-DAQmx.

### `def _multi_access_temp_file(*, suffix: str='.exe', delete: bool=True) -> Generator[str]`

Context manager for creating a temporary file.

### `def _load_data(json_data: str, platform: str) -> tuple[str | None, str | None, str | None, list[str] | None]`

Load data from JSON string and extract Windows metadata.

    >>> json_data = '{"Windows": [{"Location": "path/to/windows/driver", "Version": "24.0", "Release": "2024Q1", "supportedOS": ["Windows 11"]}], "Linux": []}'
    >>> _load_data(json_data, "Windows")
    ('path/to/windows/driver', '24.0', '2024Q1', ['Windows 11'])

    >>> json_data = '{"Windows": [], "Linux": [{"Location": "path/to/linux/driver", "Version": "24.0", "Release": "2024Q1", "supportedOS": ["ubuntu 20.04 ", "rhel 9"]}]}'
    >>> _load_data(json_data, "Linux")
    ('path/to/linux/driver', '24.0', '2024Q1', ['ubuntu 20.04', 'rhel 9'])

    >>> json_data = '{"Windows": [{"Location": "path/to/windows/driver", "Version": "24.0", "Release": "2024Q1", "supportedOS": ["Windows 11"]}], "Linux": []}'
    >>> _load_data(json_data, "Linux")
    Traceback (most recent call last):
    click.exceptions.ClickException: Unable to fetch driver details

    >>> json_data = 'invalid json'
    >>> _load_data(json_data, "Windows")
    Traceback (most recent call last):
    click.exceptions.ClickException: Failed to parse the driver metadata.
    Details: Expecting value: line 1 column 1 (char 0)

    >>> json_data = '{"Windows": [{"Location": "path/to/windows/driver", "Version": "24.0", "Release": "2024Q1", "supportedOS": ["Windows 11"]}], "Linux": []}'
    >>> _load_data(json_data, "macOS")
    Traceback (most recent call last):
    click.exceptions.ClickException: Unsupported os 'macOS'

    

### `def _get_driver_details(platform: str) -> tuple[str | None, str | None, str | None, list[str] | None]`

Parse the JSON data and retrieve the download link and version information.

### `def _install_daqmx_driver_windows_core(download_url: str) -> None`

Download and launch NI-DAQmx Driver installation in an interactive mode.

### `def _install_daqmx_driver_linux_core(download_url: str, release: str) -> None`

Download NI Linux Device Drivers and install NI-DAQmx on Linux OS.

### `def _validate_download_url(download_url: str) -> None`

Validate that the download URL uses https and points to a trusted site.

### `def _ask_user_confirmation(user_message: str) -> bool`

Prompt for user confirmation.

### `def _upgrade_daqmx_user_confirmation(installed_version: str, latest_version: str, release: str) -> bool`

Confirm with the user and return the user response.

### `def _fresh_install_daqmx_user_confirmation(latest_version: str, release: str) -> bool`

Confirm with the user and return the user response.

### `def _is_distribution_supported() -> None`

Raises an exception if the linux distribution and its version are not supported.

### `def _install_daqmx_driver()`

Install the NI-DAQmx driver.

### `def installdriver() -> None`

Download and launch NI-DAQmx Driver installation in an interactive mode.

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/_lib.py -->
## PYTHON MODULE: generated/nidaqmx/_lib.py

- `_DAQ_NOT_FOUND_MESSAGE = 'Could not find an installation of NI-DAQmx. Please ensure that NI-DAQmx is installed on this machine or contact National Instruments for support.'`

- `_DAQ_NOT_SUPPORTED_MESSAGE = 'NI-DAQmx Python is not supported on this platform: {0}. Please direct any questions or feedback to National Instruments.'`

- `_FUNCTION_NOT_SUPPORTED_MESSAGE = 'The NI-DAQmx function "{0}" is not supported in this version of NI-DAQmx. Visit ni.com/downloads to upgrade.'`

### `class c_bool32(ctypes.c_uint)`

Specifies a custom ctypes data type to represent 32-bit booleans.

#### `def _getter(self)`

#### `def _setter(self, val)`

### `class CtypesByteString()`

Custom argtype that automatically converts unicode strings to encoding used by the C API.

#### `def from_param(cls, param)`

### `def wrapped_ndpointer(*args, **kwargs)`

Wraps numpy.ctypeslib.ndpointer in order to allow passing None.

    Taken from http://stackoverflow.com/questions/32120178
    

### `class DaqFunctionImporter()`

Wraps the function getter function of a ctypes library.

    Allows the NI-DAQmx Python API to fail elegantly if a function is not
    supported in the current version of the API.
    

#### `def __init__(self, library)`

Initialize a new DaqFunctionImporter.

#### `def __getattr__(self, function)`

### `def get_encoding_from_locale() -> str`

Gets the current locale encoding handling cases where it is unset.

### `class DaqLibImporter()`

Encapsulates NI-DAQmx library importing and handle type parsing logic.

#### `def __init__(self)`

Initialize a new DaqLibImporter.

#### `def windll(self)`

#### `def cdll(self)`

#### `def task_handle(self) -> type`

#### `def cal_handle(self) -> type`

#### `def encoding(self)`

#### `def _import_lib(self)`

Determines the location of and loads the NI-DAQmx CAI DLL.

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/_lib_time.py -->
## PYTHON MODULE: generated/nidaqmx/_lib_time.py

### `class AbsoluteTime(ctypes.Structure)`

#### `def from_datetime(cls, dt: std_datetime | ht_datetime) -> AbsoluteTime`

#### `def to_datetime(self, tzinfo: dt_tzinfo | None=None) -> ht_datetime`

#### `def __str__(self) -> str`

#### `def __eq__(self, other) -> bool`

#### `def __lt__(self, other) -> bool`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/_library_interpreter.py -->
## PYTHON MODULE: generated/nidaqmx/_library_interpreter.py

- `_INT64_WFM_SEC_PER_TICK = 1e-07`

- `_T0_EPOCH = ht_datetime(1, 1, 1, tzinfo=timezone.utc)`

### `class WfmAttrType(Enum)`

### `class LibraryEventHandler(BaseEventHandler)`

Manage the lifetime of a ctypes callback method pointer.

    If DAQmx invokes a callback method pointer that has been garbage collected, the Python
    interpreter will crash.
    

#### `def __init__(self, callback_method_ptr: object) -> None`

#### `def close(self) -> None`

### `class LibraryInterpreter(BaseInterpreter)`


    Library C<->Python interpreter.
    This class is responsible for interpreting the Library's C API.

    

#### `def __init__(self)`

#### `def driver_version(self)`

#### `def add_cdaq_sync_connection(self, port_list)`

#### `def add_global_chans_to_task(self, task, channel_names)`

#### `def add_network_device(self, ip_address, device_name, attempt_reservation, timeout)`

#### `def are_configured_cdaq_sync_ports_disconnected(self, chassis_devices_ports, timeout)`

#### `def auto_configure_cdaq_sync_connections(self, chassis_devices_ports, timeout)`

#### `def calculate_reverse_poly_coeff(self, forward_coeffs, min_val_x, max_val_x, num_points_to_compute, reverse_poly_order)`

#### `def cfg_anlg_edge_ref_trig(self, task, trigger_source, pretrigger_samples, trigger_slope, trigger_level)`

#### `def cfg_anlg_edge_start_trig(self, task, trigger_source, trigger_slope, trigger_level)`

#### `def cfg_anlg_multi_edge_ref_trig(self, task, trigger_sources, pretrigger_samples, trigger_slope_array, trigger_level_array)`

#### `def cfg_anlg_multi_edge_start_trig(self, task, trigger_sources, trigger_slope_array, trigger_level_array)`

#### `def cfg_anlg_window_ref_trig(self, task, trigger_source, window_top, window_bottom, pretrigger_samples, trigger_when)`

#### `def cfg_anlg_window_start_trig(self, task, window_top, window_bottom, trigger_source, trigger_when)`

#### `def cfg_burst_handshaking_timing_export_clock(self, task, sample_clk_rate, sample_clk_outp_term, sample_mode, samps_per_chan, sample_clk_pulse_polarity, pause_when, ready_event_active_level)`

#### `def cfg_burst_handshaking_timing_import_clock(self, task, sample_clk_rate, sample_clk_src, sample_mode, samps_per_chan, sample_clk_active_edge, pause_when, ready_event_active_level)`

#### `def cfg_change_detection_timing(self, task, rising_edge_chan, falling_edge_chan, sample_mode, samps_per_chan)`

#### `def cfg_dig_edge_ref_trig(self, task, trigger_source, pretrigger_samples, trigger_edge)`

#### `def cfg_dig_edge_start_trig(self, task, trigger_source, trigger_edge)`

#### `def cfg_dig_pattern_ref_trig(self, task, trigger_source, trigger_pattern, pretrigger_samples, trigger_when)`

#### `def cfg_dig_pattern_start_trig(self, task, trigger_source, trigger_pattern, trigger_when)`

#### `def cfg_handshaking_timing(self, task, sample_mode, samps_per_chan)`

#### `def cfg_implicit_timing(self, task, sample_mode, samps_per_chan)`

#### `def cfg_pipelined_samp_clk_timing(self, task, rate, source, active_edge, sample_mode, samps_per_chan)`

#### `def cfg_samp_clk_timing(self, task, rate, source, active_edge, sample_mode, samps_per_chan)`

#### `def cfg_time_start_trig(self, task, when, timescale)`

#### `def cfg_watchdog_ao_expir_states(self, task, channel_names, expir_state_array, output_type_array)`

#### `def cfg_watchdog_co_expir_states(self, task, channel_names, expir_state_array)`

#### `def cfg_watchdog_do_expir_states(self, task, channel_names, expir_state_array)`

#### `def clear_task(self, task)`

#### `def clear_teds(self, physical_channel)`

#### `def configure_logging(self, task, file_path, logging_mode, group_name, operation)`

#### `def configure_teds(self, physical_channel, file_path)`

#### `def connect_terms(self, source_terminal, destination_terminal, signal_modifiers)`

#### `def control_watchdog_task(self, task, action)`

#### `def create_ai_accel4_wire_dc_voltage_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, sensitivity, sensitivity_units, voltage_excit_source, voltage_excit_val, use_excit_for_scaling, custom_scale_name)`

#### `def create_ai_accel_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, sensitivity, sensitivity_units, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_ai_accel_charge_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, sensitivity, sensitivity_units, custom_scale_name)`

#### `def create_ai_bridge_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, custom_scale_name)`

#### `def create_ai_calculated_power_chan(self, task, voltage_physical_channel, current_physical_channel, name_to_assign_to_channel, terminal_config, voltage_min_val, voltage_max_val, current_min_val, current_max_val, units, shunt_resistor_loc, ext_shunt_resistor_val, custom_scale_name)`

#### `def create_ai_charge_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, custom_scale_name)`

#### `def create_ai_current_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, shunt_resistor_loc, ext_shunt_resistor_val, custom_scale_name)`

#### `def create_ai_current_rms_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, shunt_resistor_loc, ext_shunt_resistor_val, custom_scale_name)`

#### `def create_ai_force_bridge_polynomial_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, forward_coeffs, reverse_coeffs, electrical_units, physical_units, custom_scale_name)`

#### `def create_ai_force_bridge_table_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, electrical_vals, electrical_units, physical_vals, physical_units, custom_scale_name)`

#### `def create_ai_force_bridge_two_point_lin_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, first_electrical_val, second_electrical_val, electrical_units, first_physical_val, second_physical_val, physical_units, custom_scale_name)`

#### `def create_ai_force_iepe_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, sensitivity, sensitivity_units, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_ai_freq_voltage_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, threshold_level, hysteresis, custom_scale_name)`

#### `def create_ai_microphone_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, units, mic_sensitivity, max_snd_press_level, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_ai_pos_eddy_curr_prox_probe_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, sensitivity, sensitivity_units, custom_scale_name)`

#### `def create_ai_pos_lvdt_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, sensitivity, sensitivity_units, voltage_excit_source, voltage_excit_val, voltage_excit_freq, ac_excit_wire_mode, custom_scale_name)`

#### `def create_ai_pos_rvdt_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, sensitivity, sensitivity_units, voltage_excit_source, voltage_excit_val, voltage_excit_freq, ac_excit_wire_mode, custom_scale_name)`

#### `def create_ai_power_chan(self, task, physical_channel, voltage_setpoint, current_setpoint, output_enable, name_to_assign_to_channel)`

#### `def create_ai_pressure_bridge_polynomial_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, forward_coeffs, reverse_coeffs, electrical_units, physical_units, custom_scale_name)`

#### `def create_ai_pressure_bridge_table_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, electrical_vals, electrical_units, physical_vals, physical_units, custom_scale_name)`

#### `def create_ai_pressure_bridge_two_point_lin_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, first_electrical_val, second_electrical_val, electrical_units, first_physical_val, second_physical_val, physical_units, custom_scale_name)`

#### `def create_ai_resistance_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, resistance_config, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_ai_rosette_strain_gage_chan(self, task, physical_channel, rosette_type, gage_orientation, rosette_meas_types, name_to_assign_to_channel, min_val, max_val, strain_config, voltage_excit_source, voltage_excit_val, gage_factor, nominal_gage_resistance, poisson_ratio, lead_wire_resistance)`

#### `def create_ai_strain_gage_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, strain_config, voltage_excit_source, voltage_excit_val, gage_factor, initial_bridge_voltage, nominal_gage_resistance, poisson_ratio, lead_wire_resistance, custom_scale_name)`

#### `def create_ai_temp_built_in_sensor_chan(self, task, physical_channel, name_to_assign_to_channel, units)`

#### `def create_ai_thrmcpl_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, thermocouple_type, cjc_source, cjc_val, cjc_channel)`

#### `def create_ai_thrmstr_chan_iex(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, resistance_config, current_excit_source, current_excit_val, a, b, c)`

#### `def create_ai_thrmstr_chan_vex(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, resistance_config, voltage_excit_source, voltage_excit_val, a, b, c, r_1)`

#### `def create_ai_torque_bridge_polynomial_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, forward_coeffs, reverse_coeffs, electrical_units, physical_units, custom_scale_name)`

#### `def create_ai_torque_bridge_table_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, electrical_vals, electrical_units, physical_vals, physical_units, custom_scale_name)`

#### `def create_ai_torque_bridge_two_point_lin_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, nominal_bridge_resistance, first_electrical_val, second_electrical_val, electrical_units, first_physical_val, second_physical_val, physical_units, custom_scale_name)`

#### `def create_ai_velocity_iepe_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, sensitivity, sensitivity_units, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_ai_voltage_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, custom_scale_name)`

#### `def create_ai_voltage_chan_with_excit(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, bridge_config, voltage_excit_source, voltage_excit_val, use_excit_for_scaling, custom_scale_name)`

#### `def create_ai_voltage_rms_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, custom_scale_name)`

#### `def create_airtd_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, rtd_type, resistance_config, current_excit_source, current_excit_val, r_0)`

#### `def create_ao_current_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, custom_scale_name)`

#### `def create_ao_func_gen_chan(self, task, physical_channel, name_to_assign_to_channel, type, freq, amplitude, offset)`

#### `def create_ao_voltage_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, custom_scale_name)`

#### `def create_ci_ang_encoder_chan(self, task, counter, name_to_assign_to_channel, decoding_type, zidx_enable, zidx_val, zidx_phase, units, pulses_per_rev, initial_angle, custom_scale_name)`

#### `def create_ci_ang_velocity_chan(self, task, counter, name_to_assign_to_channel, min_val, max_val, decoding_type, units, pulses_per_rev, custom_scale_name)`

#### `def create_ci_count_edges_chan(self, task, counter, name_to_assign_to_channel, edge, initial_count, count_direction)`

#### `def create_ci_duty_cycle_chan(self, task, counter, name_to_assign_to_channel, min_freq, max_freq, edge, custom_scale_name)`

#### `def create_ci_freq_chan(self, task, counter, name_to_assign_to_channel, min_val, max_val, units, edge, meas_method, meas_time, divisor, custom_scale_name)`

#### `def create_ci_lin_encoder_chan(self, task, counter, name_to_assign_to_channel, decoding_type, zidx_enable, zidx_val, zidx_phase, units, dist_per_pulse, initial_pos, custom_scale_name)`

#### `def create_ci_lin_velocity_chan(self, task, counter, name_to_assign_to_channel, min_val, max_val, decoding_type, units, dist_per_pulse, custom_scale_name)`

#### `def create_ci_period_chan(self, task, counter, name_to_assign_to_channel, min_val, max_val, units, edge, meas_method, meas_time, divisor, custom_scale_name)`

#### `def create_ci_pulse_chan_freq(self, task, counter, name_to_assign_to_channel, min_val, max_val, units)`

#### `def create_ci_pulse_chan_ticks(self, task, counter, name_to_assign_to_channel, source_terminal, min_val, max_val)`

#### `def create_ci_pulse_chan_time(self, task, counter, name_to_assign_to_channel, min_val, max_val, units)`

#### `def create_ci_pulse_width_chan(self, task, counter, name_to_assign_to_channel, min_val, max_val, units, starting_edge, custom_scale_name)`

#### `def create_ci_semi_period_chan(self, task, counter, name_to_assign_to_channel, min_val, max_val, units, custom_scale_name)`

#### `def create_ci_two_edge_sep_chan(self, task, counter, name_to_assign_to_channel, min_val, max_val, units, first_edge, second_edge, custom_scale_name)`

#### `def create_cigps_timestamp_chan(self, task, counter, name_to_assign_to_channel, units, sync_method, custom_scale_name)`

#### `def create_co_pulse_chan_freq(self, task, counter, name_to_assign_to_channel, units, idle_state, initial_delay, freq, duty_cycle)`

#### `def create_co_pulse_chan_ticks(self, task, counter, source_terminal, name_to_assign_to_channel, idle_state, initial_delay, low_ticks, high_ticks)`

#### `def create_co_pulse_chan_time(self, task, counter, name_to_assign_to_channel, units, idle_state, initial_delay, low_time, high_time)`

#### `def create_di_chan(self, task, lines, name_to_assign_to_lines, line_grouping)`

#### `def create_do_chan(self, task, lines, name_to_assign_to_lines, line_grouping)`

#### `def create_lin_scale(self, name, slope, y_intercept, pre_scaled_units, scaled_units)`

#### `def create_map_scale(self, name, prescaled_min, prescaled_max, scaled_min, scaled_max, pre_scaled_units, scaled_units)`

#### `def create_polynomial_scale(self, name, forward_coeffs, reverse_coeffs, pre_scaled_units, scaled_units)`

#### `def create_table_scale(self, name, prescaled_vals, scaled_vals, pre_scaled_units, scaled_units)`

#### `def create_task(self, session_name)`

#### `def create_tedsai_accel_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_tedsai_bridge_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, voltage_excit_source, voltage_excit_val, custom_scale_name)`

#### `def create_tedsai_current_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, shunt_resistor_loc, ext_shunt_resistor_val, custom_scale_name)`

#### `def create_tedsai_force_bridge_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, voltage_excit_source, voltage_excit_val, custom_scale_name)`

#### `def create_tedsai_force_iepe_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_tedsai_microphone_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, units, max_snd_press_level, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_tedsai_pos_lvdt_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, voltage_excit_source, voltage_excit_val, voltage_excit_freq, ac_excit_wire_mode, custom_scale_name)`

#### `def create_tedsai_pos_rvdt_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, voltage_excit_source, voltage_excit_val, voltage_excit_freq, ac_excit_wire_mode, custom_scale_name)`

#### `def create_tedsai_pressure_bridge_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, voltage_excit_source, voltage_excit_val, custom_scale_name)`

#### `def create_tedsai_resistance_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, resistance_config, current_excit_source, current_excit_val, custom_scale_name)`

#### `def create_tedsai_strain_gage_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, voltage_excit_source, voltage_excit_val, initial_bridge_voltage, lead_wire_resistance, custom_scale_name)`

#### `def create_tedsai_thrmcpl_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, cjc_source, cjc_val, cjc_channel)`

#### `def create_tedsai_thrmstr_chan_iex(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, resistance_config, current_excit_source, current_excit_val)`

#### `def create_tedsai_thrmstr_chan_vex(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, resistance_config, voltage_excit_source, voltage_excit_val, r_1)`

#### `def create_tedsai_torque_bridge_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, voltage_excit_source, voltage_excit_val, custom_scale_name)`

#### `def create_tedsai_voltage_chan(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, custom_scale_name)`

#### `def create_tedsai_voltage_chan_with_excit(self, task, physical_channel, name_to_assign_to_channel, terminal_config, min_val, max_val, units, voltage_excit_source, voltage_excit_val, custom_scale_name)`

#### `def create_tedsairtd_chan(self, task, physical_channel, name_to_assign_to_channel, min_val, max_val, units, resistance_config, current_excit_source, current_excit_val)`

#### `def create_watchdog_timer_task_ex(self, device_name, session_name, timeout)`

#### `def delete_network_device(self, device_name)`

#### `def delete_saved_global_chan(self, channel_name)`

#### `def delete_saved_scale(self, scale_name)`

#### `def delete_saved_task(self, task_name)`

#### `def device_supports_cal(self, device_name)`

#### `def disable_ref_trig(self, task)`

#### `def disable_start_trig(self, task)`

#### `def disconnect_terms(self, source_terminal, destination_terminal)`

#### `def export_signal(self, task, signal_id, output_terminal)`

#### `def get_analog_power_up_states_with_output_type(self, channel_names, array_size)`

#### `def get_auto_configured_cdaq_sync_connections(self)`

#### `def get_buffer_attribute_uint32(self, task, attribute)`

#### `def get_cal_info_attribute_bool(self, device_name, attribute)`

#### `def get_cal_info_attribute_double(self, device_name, attribute)`

#### `def get_cal_info_attribute_string(self, device_name, attribute)`

#### `def get_cal_info_attribute_uint32(self, device_name, attribute)`

#### `def get_chan_attribute_bool(self, task, channel, attribute)`

#### `def get_chan_attribute_double(self, task, channel, attribute)`

#### `def get_chan_attribute_double_array(self, task, channel, attribute)`

#### `def get_chan_attribute_int32(self, task, channel, attribute)`

#### `def get_chan_attribute_string(self, task, channel, attribute)`

#### `def get_chan_attribute_uint32(self, task, channel, attribute)`

#### `def get_device_attribute_bool(self, device_name, attribute)`

#### `def get_device_attribute_double(self, device_name, attribute)`

#### `def get_device_attribute_double_array(self, device_name, attribute)`

#### `def get_device_attribute_int32(self, device_name, attribute)`

#### `def get_device_attribute_int32_array(self, device_name, attribute)`

#### `def get_device_attribute_string(self, device_name, attribute)`

#### `def get_device_attribute_uint32(self, device_name, attribute)`

#### `def get_device_attribute_uint32_array(self, device_name, attribute)`

#### `def get_digital_logic_family_power_up_state(self, device_name)`

#### `def get_digital_power_up_states(self, device_name, channel_name)`

#### `def get_digital_pull_up_pull_down_states(self, device_name, channel_name)`

#### `def get_disconnected_cdaq_sync_ports(self)`

#### `def get_exported_signal_attribute_bool(self, task, attribute)`

#### `def get_exported_signal_attribute_double(self, task, attribute)`

#### `def get_exported_signal_attribute_int32(self, task, attribute)`

#### `def get_exported_signal_attribute_string(self, task, attribute)`

#### `def get_exported_signal_attribute_uint32(self, task, attribute)`

#### `def get_ext_cal_last_date_and_time(self, device_name)`

#### `def get_persisted_chan_attribute_bool(self, channel, attribute)`

#### `def get_persisted_chan_attribute_string(self, channel, attribute)`

#### `def get_persisted_scale_attribute_bool(self, scale_name, attribute)`

#### `def get_persisted_scale_attribute_string(self, scale_name, attribute)`

#### `def get_persisted_task_attribute_bool(self, task_name, attribute)`

#### `def get_persisted_task_attribute_string(self, task_name, attribute)`

#### `def get_physical_chan_attribute_bool(self, physical_channel, attribute)`

#### `def get_physical_chan_attribute_bytes(self, physical_channel, attribute)`

#### `def get_physical_chan_attribute_double(self, physical_channel, attribute)`

#### `def get_physical_chan_attribute_double_array(self, physical_channel, attribute)`

#### `def get_physical_chan_attribute_int32(self, physical_channel, attribute)`

#### `def get_physical_chan_attribute_int32_array(self, physical_channel, attribute)`

#### `def get_physical_chan_attribute_string(self, physical_channel, attribute)`

#### `def get_physical_chan_attribute_uint32(self, physical_channel, attribute)`

#### `def get_physical_chan_attribute_uint32_array(self, physical_channel, attribute)`

#### `def get_read_attribute_bool(self, task, attribute)`

#### `def get_read_attribute_double(self, task, attribute)`

#### `def get_read_attribute_int32(self, task, attribute)`

#### `def get_read_attribute_string(self, task, attribute, size_hint=0)`

#### `def get_read_attribute_uint32(self, task, attribute)`

#### `def get_read_attribute_uint64(self, task, attribute)`

#### `def get_scale_attribute_double(self, scale_name, attribute)`

#### `def get_scale_attribute_double_array(self, scale_name, attribute)`

#### `def get_scale_attribute_int32(self, scale_name, attribute)`

#### `def get_scale_attribute_string(self, scale_name, attribute)`

#### `def get_self_cal_last_date_and_time(self, device_name)`

#### `def get_system_info_attribute_string(self, attribute)`

#### `def get_system_info_attribute_uint32(self, attribute)`

#### `def get_task_attribute_bool(self, task, attribute)`

#### `def get_task_attribute_string(self, task, attribute)`

#### `def get_task_attribute_uint32(self, task, attribute)`

#### `def get_timing_attribute_bool(self, task, attribute)`

#### `def get_timing_attribute_double(self, task, attribute)`

#### `def get_timing_attribute_ex_bool(self, task, device_names, attribute)`

#### `def get_timing_attribute_ex_double(self, task, device_names, attribute)`

#### `def get_timing_attribute_ex_int32(self, task, device_names, attribute)`

#### `def get_timing_attribute_ex_string(self, task, device_names, attribute)`

#### `def get_timing_attribute_ex_uint32(self, task, device_names, attribute)`

#### `def get_timing_attribute_ex_uint64(self, task, device_names, attribute)`

#### `def get_timing_attribute_int32(self, task, attribute)`

#### `def get_timing_attribute_string(self, task, attribute)`

#### `def get_timing_attribute_timestamp(self, task, attribute)`

#### `def get_timing_attribute_uint32(self, task, attribute)`

#### `def get_timing_attribute_uint64(self, task, attribute)`

#### `def get_trig_attribute_bool(self, task, attribute)`

#### `def get_trig_attribute_double(self, task, attribute)`

#### `def get_trig_attribute_double_array(self, task, attribute)`

#### `def get_trig_attribute_int32(self, task, attribute)`

#### `def get_trig_attribute_int32_array(self, task, attribute)`

#### `def get_trig_attribute_string(self, task, attribute)`

#### `def get_trig_attribute_timestamp(self, task, attribute)`

#### `def get_trig_attribute_uint32(self, task, attribute)`

#### `def get_watchdog_attribute_bool(self, task, lines, attribute)`

#### `def get_watchdog_attribute_double(self, task, lines, attribute)`

#### `def get_watchdog_attribute_int32(self, task, lines, attribute)`

#### `def get_watchdog_attribute_string(self, task, lines, attribute)`

#### `def get_write_attribute_bool(self, task, attribute)`

#### `def get_write_attribute_double(self, task, attribute)`

#### `def get_write_attribute_int32(self, task, attribute)`

#### `def get_write_attribute_string(self, task, attribute, size_hint=0)`

#### `def get_write_attribute_uint32(self, task, attribute)`

#### `def get_write_attribute_uint64(self, task, attribute)`

#### `def internal_get_last_created_chan(self)`

#### `def is_task_done(self, task)`

#### `def load_task(self, session_name)`

#### `def perform_bridge_offset_nulling_cal_ex(self, task, channel, skip_unsupported_channels)`

#### `def perform_bridge_shunt_cal_ex(self, task, channel, shunt_resistor_value, shunt_resistor_location, shunt_resistor_select, shunt_resistor_source, bridge_resistance, skip_unsupported_channels)`

#### `def perform_strain_shunt_cal_ex(self, task, channel, shunt_resistor_value, shunt_resistor_location, shunt_resistor_select, shunt_resistor_source, skip_unsupported_channels)`

#### `def perform_thrmcpl_lead_offset_nulling_cal(self, task, channel, skip_unsupported_channels)`

#### `def read_analog_f64(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_analog_scalar_f64(self, task, timeout)`

#### `def read_binary_i16(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_binary_i32(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_binary_u16(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_binary_u32(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_counter_f64(self, task, num_samps_per_chan, timeout, read_array)`

#### `def read_counter_f64_ex(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_counter_scalar_f64(self, task, timeout)`

#### `def read_counter_scalar_u32(self, task, timeout)`

#### `def read_counter_u32(self, task, num_samps_per_chan, timeout, read_array)`

#### `def read_counter_u32_ex(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_ctr_freq(self, task, num_samps_per_chan, timeout, interleaved, read_array_frequency, read_array_duty_cycle)`

#### `def read_ctr_freq_scalar(self, task, timeout)`

#### `def read_ctr_ticks(self, task, num_samps_per_chan, timeout, interleaved, read_array_high_ticks, read_array_low_ticks)`

#### `def read_ctr_ticks_scalar(self, task, timeout)`

#### `def read_ctr_time(self, task, num_samps_per_chan, timeout, interleaved, read_array_high_time, read_array_low_time)`

#### `def read_ctr_time_scalar(self, task, timeout)`

#### `def read_digital_lines(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_digital_scalar_u32(self, task, timeout)`

#### `def read_digital_u16(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_digital_u32(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_digital_u8(self, task, num_samps_per_chan, timeout, fill_mode, read_array)`

#### `def read_power_scalar_f64(self, task, timeout)`

#### `def register_done_event(self, task, options, callback_function, callback_data)`

#### `def register_every_n_samples_event(self, task, every_n_samples_event_type, n_samples, options, callback_function, callback_data)`

#### `def register_signal_event(self, task, signal_id, options, callback_function, callback_data)`

#### `def remove_cdaq_sync_connection(self, port_list)`

#### `def reserve_network_device(self, device_name, override_reservation)`

#### `def reset_buffer_attribute(self, task, attribute)`

#### `def reset_chan_attribute(self, task, channel, attribute)`

#### `def reset_device(self, device_name)`

#### `def reset_exported_signal_attribute(self, task, attribute)`

#### `def reset_read_attribute(self, task, attribute)`

#### `def reset_timing_attribute(self, task, attribute)`

#### `def reset_timing_attribute_ex(self, task, device_names, attribute)`

#### `def reset_trig_attribute(self, task, attribute)`

#### `def reset_watchdog_attribute(self, task, lines, attribute)`

#### `def reset_write_attribute(self, task, attribute)`

#### `def restore_last_ext_cal_const(self, device_name)`

#### `def save_global_chan(self, task, channel_name, save_as, author, options)`

#### `def save_scale(self, scale_name, save_as, author, options)`

#### `def save_task(self, task, save_as, author, options)`

#### `def self_cal(self, device_name)`

#### `def self_test_device(self, device_name)`

#### `def set_analog_power_up_states(self, device_name, channel_names, state, channel_type)`

#### `def set_analog_power_up_states_with_output_type(self, channel_names, state_array, channel_type_array)`

#### `def set_buffer_attribute_uint32(self, task, attribute, value)`

#### `def set_cal_info_attribute_bool(self, device_name, attribute, value)`

#### `def set_cal_info_attribute_double(self, device_name, attribute, value)`

#### `def set_cal_info_attribute_string(self, device_name, attribute, value)`

#### `def set_cal_info_attribute_uint32(self, device_name, attribute, value)`

#### `def set_chan_attribute_bool(self, task, channel, attribute, value)`

#### `def set_chan_attribute_double(self, task, channel, attribute, value)`

#### `def set_chan_attribute_double_array(self, task, channel, attribute, value)`

#### `def set_chan_attribute_int32(self, task, channel, attribute, value)`

#### `def set_chan_attribute_string(self, task, channel, attribute, value)`

#### `def set_chan_attribute_uint32(self, task, channel, attribute, value)`

#### `def set_digital_logic_family_power_up_state(self, device_name, logic_family)`

#### `def set_digital_power_up_states(self, device_name, channel_names, state)`

#### `def set_digital_pull_up_pull_down_states(self, device_name, channel_names, state)`

#### `def set_exported_signal_attribute_bool(self, task, attribute, value)`

#### `def set_exported_signal_attribute_double(self, task, attribute, value)`

#### `def set_exported_signal_attribute_int32(self, task, attribute, value)`

#### `def set_exported_signal_attribute_string(self, task, attribute, value)`

#### `def set_exported_signal_attribute_uint32(self, task, attribute, value)`

#### `def set_read_attribute_bool(self, task, attribute, value)`

#### `def set_read_attribute_double(self, task, attribute, value)`

#### `def set_read_attribute_int32(self, task, attribute, value)`

#### `def set_read_attribute_string(self, task, attribute, value)`

#### `def set_read_attribute_uint32(self, task, attribute, value)`

#### `def set_read_attribute_uint64(self, task, attribute, value)`

#### `def set_runtime_environment(self, environment, environment_version, reserved_1, reserved_2)`

#### `def set_scale_attribute_double(self, scale_name, attribute, value)`

#### `def set_scale_attribute_double_array(self, scale_name, attribute, value)`

#### `def set_scale_attribute_int32(self, scale_name, attribute, value)`

#### `def set_scale_attribute_string(self, scale_name, attribute, value)`

#### `def set_timing_attribute_bool(self, task, attribute, value)`

#### `def set_timing_attribute_double(self, task, attribute, value)`

#### `def set_timing_attribute_ex_bool(self, task, device_names, attribute, value)`

#### `def set_timing_attribute_ex_double(self, task, device_names, attribute, value)`

#### `def set_timing_attribute_ex_int32(self, task, device_names, attribute, value)`

#### `def set_timing_attribute_ex_string(self, task, device_names, attribute, value)`

#### `def set_timing_attribute_ex_uint32(self, task, device_names, attribute, value)`

#### `def set_timing_attribute_ex_uint64(self, task, device_names, attribute, value)`

#### `def set_timing_attribute_int32(self, task, attribute, value)`

#### `def set_timing_attribute_string(self, task, attribute, value)`

#### `def set_timing_attribute_uint32(self, task, attribute, value)`

#### `def set_timing_attribute_uint64(self, task, attribute, value)`

#### `def set_trig_attribute_bool(self, task, attribute, value)`

#### `def set_trig_attribute_double(self, task, attribute, value)`

#### `def set_trig_attribute_double_array(self, task, attribute, value)`

#### `def set_trig_attribute_int32(self, task, attribute, value)`

#### `def set_trig_attribute_int32_array(self, task, attribute, value)`

#### `def set_trig_attribute_string(self, task, attribute, value)`

#### `def set_trig_attribute_timestamp(self, task, attribute, value)`

#### `def set_trig_attribute_uint32(self, task, attribute, value)`

#### `def set_watchdog_attribute_bool(self, task, lines, attribute, value)`

#### `def set_watchdog_attribute_double(self, task, lines, attribute, value)`

#### `def set_watchdog_attribute_int32(self, task, lines, attribute, value)`

#### `def set_watchdog_attribute_string(self, task, lines, attribute, value)`

#### `def set_write_attribute_bool(self, task, attribute, value)`

#### `def set_write_attribute_double(self, task, attribute, value)`

#### `def set_write_attribute_int32(self, task, attribute, value)`

#### `def set_write_attribute_string(self, task, attribute, value)`

#### `def set_write_attribute_uint32(self, task, attribute, value)`

#### `def set_write_attribute_uint64(self, task, attribute, value)`

#### `def start_new_file(self, task, file_path)`

#### `def start_task(self, task)`

#### `def stop_task(self, task)`

#### `def task_control(self, task, action)`

#### `def tristate_output_term(self, output_terminal)`

#### `def unregister_done_event(self, task)`

#### `def unregister_every_n_samples_event(self, task, every_n_samples_event_type)`

#### `def unregister_signal_event(self, task, signal_id)`

#### `def unreserve_network_device(self, device_name)`

#### `def wait_for_valid_timestamp(self, task, timestamp_event, timeout)`

#### `def wait_until_task_done(self, task, time_to_wait)`

#### `def write_analog_f64(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_analog_scalar_f64(self, task, auto_start, timeout, value)`

#### `def write_binary_i16(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_binary_i32(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_binary_u16(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_binary_u32(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_ctr_freq(self, task, num_samps_per_chan, auto_start, timeout, data_layout, frequency, duty_cycle)`

#### `def write_ctr_freq_scalar(self, task, auto_start, timeout, frequency, duty_cycle)`

#### `def write_ctr_ticks(self, task, num_samps_per_chan, auto_start, timeout, data_layout, high_ticks, low_ticks)`

#### `def write_ctr_ticks_scalar(self, task, auto_start, timeout, high_ticks, low_ticks)`

#### `def write_ctr_time(self, task, num_samps_per_chan, auto_start, timeout, data_layout, high_time, low_time)`

#### `def write_ctr_time_scalar(self, task, auto_start, timeout, high_time, low_time)`

#### `def write_digital_lines(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_digital_scalar_u32(self, task, auto_start, timeout, value)`

#### `def write_digital_u16(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_digital_u32(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_digital_u8(self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array)`

#### `def write_id_pin_memory(self, device_name, id_pin_name, data, format_code)`

#### `def write_to_teds_from_array(self, physical_channel, bit_stream, basic_teds_options)`

#### `def write_to_teds_from_file(self, physical_channel, file_path, basic_teds_options)`

#### `def get_error_string(self, error_code)`

#### `def get_extended_error_info(self)`

#### `def read_analog_waveform(self, task_handle: object, number_of_samples_per_channel: int, timeout: float, waveform: AnalogWaveform[numpy.float64], waveform_attribute_mode: WaveformAttributeMode) -> int`

Read an analog waveform with timing and attributes.

#### `def read_analog_waveforms(self, task_handle: object, number_of_samples_per_channel: int, timeout: float, waveforms: Sequence[AnalogWaveform[numpy.float64]], waveform_attribute_mode: WaveformAttributeMode) -> int`

Read a set of analog waveforms with timing and attributes. All of the waveforms must be the same size.

#### `def _internal_read_analog_waveform_ex(self, task_handle: object, number_of_samples_per_channel: int, timeout: float, fill_mode: int, read_array: numpy.typing.NDArray[numpy.float64], properties: Sequence[ExtendedPropertyDictionary] | None, t0_array: numpy.typing.NDArray[numpy.int64] | None, dt_array: numpy.typing.NDArray[numpy.int64] | None) -> tuple[int, int]`

#### `def _internal_read_analog_waveform_per_chan(self, task_handle: object, num_samps_per_chan: int, timeout: float, read_arrays: Sequence[numpy.typing.NDArray[numpy.float64]], properties: Sequence[ExtendedPropertyDictionary] | None, t0_array: numpy.typing.NDArray[numpy.int64] | None, dt_array: numpy.typing.NDArray[numpy.int64] | None) -> tuple[int, int]`

#### `def _get_wfm_attr_callback(self, properties)`

#### `def _get_wfm_attr_value(self, attribute_type: int, value: ctypes.c_void_p, value_size_in_bytes: int) -> ExtendedPropertyValue`

#### `def _get_wfm_attr_callback_ptr(self, set_wfm_attr_callback: SetWfmAttrCallback) -> ctypes._FuncPointer`

#### `def _set_waveform_timings(self, waveforms: Sequence[AnalogWaveform[numpy.float64] | DigitalWaveform[numpy.uint8]], t0_array: numpy.typing.NDArray[numpy.int64], dt_array: numpy.typing.NDArray[numpy.int64]) -> None`

#### `def read_digital_waveform(self, task_handle: object, number_of_samples_per_channel: int, timeout: float, waveform: DigitalWaveform[Any], waveform_attribute_mode: WaveformAttributeMode) -> int`

Read a digital waveform with timing and attributes.

#### `def _get_digital_read_array(self, waveform: DigitalWaveform[Any]) -> numpy.typing.NDArray[numpy.uint8]`

#### `def read_digital_waveforms(self, task_handle: object, channel_count: int, number_of_samples_per_channel: int, number_of_signals_per_sample: int, timeout: float, waveforms: Sequence[DigitalWaveform[Any]], waveform_attribute_mode: WaveformAttributeMode) -> int`

Read a digital waveform with timing and attributes.

#### `def read_new_digital_waveforms(self, task_handle: object, channel_count: int, number_of_samples_per_channel: int, number_of_signals_per_sample: int, timeout: float, waveform_attribute_mode: WaveformAttributeMode) -> Sequence[DigitalWaveform[numpy.uint8]]`

Read a digital waveform with timing and attributes.

#### `def _internal_read_digital_waveform(self, task_handle: object, number_of_samples_per_channel: int, timeout: float, fill_mode: int, read_array: numpy.typing.NDArray[numpy.uint8], properties: Sequence[ExtendedPropertyDictionary] | None, t0_array: numpy.typing.NDArray[numpy.int64] | None, dt_array: numpy.typing.NDArray[numpy.int64] | None, bytes_per_chan_array: numpy.typing.NDArray[numpy.uint32] | None=None) -> tuple[int, int]`

#### `def read_id_pin_memory(self, device_name, id_pin_name)`

#### `def read_power_binary_i16(self, task, num_samps_per_chan, timeout, fill_mode, read_voltage_array, read_current_array)`

#### `def read_power_f64(self, task, num_samps_per_chan, timeout, fill_mode, read_voltage_array, read_current_array)`

#### `def read_raw(self, task, num_samps_per_chan, timeout, read_array)`

#### `def write_analog_waveform(self, task_handle: object, waveform: AnalogWaveform[Any], auto_start: bool, timeout: float) -> int`

Write an analog waveform.

#### `def write_analog_waveforms(self, task_handle: object, waveforms: Sequence[AnalogWaveform[Any]], auto_start: bool, timeout: float) -> int`

Write analog waveforms.

#### `def _get_analog_write_array(self, waveform: AnalogWaveform[Any]) -> numpy.typing.NDArray[numpy.float64]`

#### `def _internal_write_analog_waveform_per_chan(self, task_handle: object, num_samps_per_chan: int, auto_start: bool, timeout: float, write_arrays: Sequence[numpy.typing.NDArray[numpy.float64]]) -> tuple[int, int]`

#### `def write_digital_waveform(self, task_handle: object, waveform: DigitalWaveform[Any], auto_start: bool, timeout: float) -> int`

Write a digital waveform.

#### `def _get_digital_write_array(self, waveform: DigitalWaveform[Any]) -> numpy.typing.NDArray[numpy.uint8]`

#### `def write_digital_waveforms(self, task_handle: object, waveforms: Sequence[DigitalWaveform[Any]], auto_start: bool, timeout: float) -> int`

Write digital waveforms.

#### `def _internal_write_digital_waveform(self, task_handle: object, num_samps_per_chan: int, auto_start: bool, timeout: float, data_layout: int, write_array: numpy.typing.NDArray[numpy.uint8], bytes_per_chan_array: numpy.typing.NDArray[numpy.uint32] | None=None) -> tuple[int, int]`

#### `def write_raw(self, task_handle, num_samps_per_chan, auto_start, timeout, numpy_array)`

#### `def hash_task_handle(self, task_handle)`

#### `def check_for_error(self, error_code, samps_per_chan_written=None, samps_per_chan_read=None)`

### `def is_string_buffer_too_small(error_code)`

### `def is_array_buffer_too_small(error_code)`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/_linux_installation_commands.py -->
## PYTHON MODULE: generated/nidaqmx/_linux_installation_commands.py

### `def _get_version_ubuntu(dist_version: str) -> str`

### `def _get_version_opensuse(dist_version: str) -> str`

### `def _get_version_rhel(dist_version: str) -> str`

- `_APT_INSTALL_COMMANDS = [['apt', 'update'], ['apt', 'install', '{directory}/NILinux{release}DeviceDrivers/ni-ubuntu{version}-drivers-{release}.deb'], ['apt', 'update'], ['apt', 'install', 'ni-daqmx'], ['dkms', 'autoinstall']]`

- `_ZYPPER_INSTALL_COMMANDS = [['zypper', 'update'], ['zypper', 'install', 'insserv'], ['zypper', '--no-gpg-checks', 'install', '{directory}/NILinux{release}DeviceDrivers/ni-opensuse{version}-drivers-{release}.rpm'], ['zypper', 'refresh'], ['zypper', 'install', 'ni-daqmx'], ['dkms', 'autoinstall']]`

- `_YUM_INSTALL_COMMANDS = [['yum', 'update'], ['yum', 'install', 'chkconfig'], ['yum', 'install', '{directory}/NILinux{release}DeviceDrivers/ni-rhel{version}-drivers-{release}.rpm'], ['yum', 'install', 'ni-daqmx'], ['dkms', 'autoinstall']]`

- `_DEBIAN_DAQMX_VERSION_COMMAND = ['dpkg', '-l', 'ni-daqmx']`

- `_RPM_DAQMX_VERSION_COMMAND = ['rpm', '-q', 'ni-daqmx']`

### `class DistroInfo()`

- `LINUX_COMMANDS = {'ubuntu': DistroInfo(_get_version_ubuntu, _DEBIAN_DAQMX_VERSION_COMMAND, _APT_INSTALL_COMMANDS), 'opensuse': DistroInfo(_get_version_opensuse, _RPM_DAQMX_VERSION_COMMAND, _ZYPPER_INSTALL_COMMANDS), 'rhel': DistroInfo(_get_version_rhel, _RPM_DAQMX_VERSION_COMMAND, _YUM_INSTALL_COMMANDS)}`

### `def get_linux_installation_commands(_directory_to_extract_to: str, dist_name: str, dist_version: str, _release_string: str) -> list[list[str]]`

Get the installation commands for Linux based on the distribution.

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/_stubs/__init__.py -->
## PYTHON MODULE: generated/nidaqmx/_stubs/__init__.py

### MODULE DOCSTRING

Auto generated gRPC files.

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/_stubs/data_moniker_pb2.py -->
## PYTHON MODULE: generated/nidaqmx/_stubs/data_moniker_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12data_moniker.proto\x12\x10ni.data_monikers\x1a\x19google/protobuf/any.proto"\x8a\x01\n!BeginMonikerSidebandStreamRequest\x124\n\x08strategy\x18\x01 \x01(\x0e2".ni.data_monikers.SidebandStrategy\x12/\n\x08monikers\x18\x02 \x01(\x0b2\x1d.ni.data_monikers.MonikerList"\xa4\x01\n"BeginMonikerSidebandStreamResponse\x124\n\x08strategy\x18\x01 \x01(\x0e2".ni.data_monikers.SidebandStrategy\x12\x16\n\x0econnection_url\x18\x02 \x01(\t\x12\x1b\n\x13sideband_identifier\x18\x03 \x01(\t\x12\x13\n\x0bbuffer_size\x18\x04 \x01(\x12"O\n\x07Moniker\x12\x18\n\x10service_location\x18\x01 \x01(\t\x12\x13\n\x0bdata_source\x18\x02 \x01(\t\x12\x15\n\rdata_instance\x18\x03 \x01(\x03"\x87\x01\n\x13MonikerWriteRequest\x121\n\x08monikers\x18\x01 \x01(\x0b2\x1d.ni.data_monikers.MonikerListH\x00\x12/\n\x04data\x18\x02 \x01(\x0b2\x1f.ni.data_monikers.MonikerValuesH\x00B\x0c\n\nwrite_data"D\n\x13MonikerReadResponse\x12-\n\x04data\x18\x01 \x01(\x0b2\x1f.ni.data_monikers.MonikerValues"r\n\x0bMonikerList\x120\n\rread_monikers\x18\x02 \x03(\x0b2\x19.ni.data_monikers.Moniker\x121\n\x0ewrite_monikers\x18\x03 \x03(\x0b2\x19.ni.data_monikers.Moniker"5\n\rMonikerValues\x12$\n\x06values\x18\x01 \x03(\x0b2\x14.google.protobuf.Any"W\n\x14SidebandWriteRequest\x12\x0e\n\x06cancel\x18\x01 \x01(\x08\x12/\n\x06values\x18\x02 \x01(\x0b2\x1f.ni.data_monikers.MonikerValues"W\n\x14SidebandReadResponse\x12\x0e\n\x06cancel\x18\x01 \x01(\x08\x12/\n\x06values\x18\x02 \x01(\x0b2\x1f.ni.data_monikers.MonikerValues"\x15\n\x13StreamWriteResponse*\xbd\x01\n\x10SidebandStrategy\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04GRPC\x10\x01\x12\x11\n\rSHARED_MEMORY\x10\x02\x12!\n\x1dDOUBLE_BUFFERED_SHARED_MEMORY\x10\x03\x12\x0b\n\x07SOCKETS\x10\x04\x12\x17\n\x13SOCKETS_LOW_LATENCY\x10\x05\x12\x16\n\x12HYPERVISOR_SOCKETS\x10\x06\x12\x08\n\x04RDMA\x10\x07\x12\x14\n\x10RDMA_LOW_LATENCY\x10\x082\xb4\x03\n\x0bDataMoniker\x12\x82\x01\n\x13BeginSidebandStream\x123.ni.data_monikers.BeginMonikerSidebandStreamRequest\x1a4.ni.data_monikers.BeginMonikerSidebandStreamResponse"\x00\x12e\n\x0fStreamReadWrite\x12%.ni.data_monikers.MonikerWriteRequest\x1a%.ni.data_monikers.MonikerReadResponse"\x00(\x010\x01\x12V\n\nStreamRead\x12\x1d.ni.data_monikers.MonikerList\x1a%.ni.data_monikers.MonikerReadResponse"\x000\x01\x12a\n\x0bStreamWrite\x12%.ni.data_monikers.MonikerWriteRequest\x1a%.ni.data_monikers.StreamWriteResponse"\x00(\x010\x01B&\xf8\x01\x01\xaa\x02 NationalInstruments.DataMonikersb\x06proto3')`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/_stubs/data_moniker_pb2_grpc.py -->
## PYTHON MODULE: generated/nidaqmx/_stubs/data_moniker_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

### `class DataMonikerStub(object)`

Missing associated documentation comment in .proto file.

#### `def __init__(self, channel)`

Constructor.

        Args:
            channel: A grpc.Channel.
        

### `class DataMonikerServicer(object)`

Missing associated documentation comment in .proto file.

#### `def BeginSidebandStream(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def StreamReadWrite(self, request_iterator, context)`

Missing associated documentation comment in .proto file.

#### `def StreamRead(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def StreamWrite(self, request_iterator, context)`

Missing associated documentation comment in .proto file.

### `def add_DataMonikerServicer_to_server(servicer, server)`

### `class DataMoniker(object)`

Missing associated documentation comment in .proto file.

#### `def BeginSidebandStream(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def StreamReadWrite(request_iterator, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def StreamRead(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def StreamWrite(request_iterator, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/_stubs/nidaqmx_pb2.py -->
## PYTHON MODULE: generated/nidaqmx/_stubs/nidaqmx_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rnidaqmx.proto\x12\x0cnidaqmx_grpc\x1a\rsession.proto\x1a\x12data_moniker.proto\x1a ni/protobuf/types/waveform.proto\x1a\x1fgoogle/protobuf/timestamp.proto"}\n\x1dAnalogPowerUpChannelsAndState\x12\x15\n\rchannel_names\x18\x01 \x01(\t\x12\r\n\x05state\x18\x02 \x01(\x01\x126\n\x0cchannel_type\x18\x03 \x01(\x0e2 .nidaqmx_grpc.PowerUpChannelType"_\n\x1bWatchdogExpChannelsAndState\x12\r\n\x05lines\x18\x01 \x01(\t\x121\n\texp_state\x18\x02 \x01(\x0e2\x1e.nidaqmx_grpc.DigitalLineState"`\n\x1cDigitalPowerUpTypeAndChannel\x12\x14\n\x0cchannel_name\x18\x01 \x01(\t\x12*\n\x05state\x18\x02 \x01(\x0e2\x1b.nidaqmx_grpc.PowerUpStates"c\n\x1eDigitalPowerUpChannelsAndState\x12\x15\n\rchannel_names\x18\x01 \x01(\t\x12*\n\x05state\x18\x02 \x01(\x0e2\x1b.nidaqmx_grpc.PowerUpStates"j\n%DigitalPullUpPullDownChannelsAndState\x12\x15\n\rchannel_names\x18\x01 \x01(\t\x12*\n\x05state\x18\x02 \x01(\x0e2\x1b.nidaqmx_grpc.ResistorState"k\n\x1bAnalogPowerUpChannelAndType\x12\x14\n\x0cchannel_name\x18\x01 \x01(\t\x126\n\x0cchannel_type\x18\x02 \x01(\x0e2 .nidaqmx_grpc.PowerUpChannelType"1\n\x1cAddCDAQSyncConnectionRequest\x12\x11\n\tport_list\x18\x01 \x01(\t"/\n\x1dAddCDAQSyncConnectionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"Z\n\x1bAddGlobalChansToTaskRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rchannel_names\x18\x02 \x01(\t".\n\x1cAddGlobalChansToTaskResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"p\n\x17AddNetworkDeviceRequest\x12\x12\n\nip_address\x18\x01 \x01(\t\x12\x13\n\x0bdevice_name\x18\x02 \x01(\t\x12\x1b\n\x13attempt_reservation\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01"C\n\x18AddNetworkDeviceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fdevice_name_out\x18\x02 \x01(\t"_\n-AreConfiguredCDAQSyncPortsDisconnectedRequest\x12\x1d\n\x15chassis_devices_ports\x18\x01 \x01(\t\x12\x0f\n\x07timeout\x18\x02 \x01(\x01"b\n.AreConfiguredCDAQSyncPortsDisconnectedResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12 \n\x18disconnected_ports_exist\x18\x02 \x01(\x08"Y\n\'AutoConfigureCDAQSyncConnectionsRequest\x12\x1d\n\x15chassis_devices_ports\x18\x01 \x01(\t\x12\x0f\n\x07timeout\x18\x02 \x01(\x01":\n(AutoConfigureCDAQSyncConnectionsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x9b\x01\n CalculateReversePolyCoeffRequest\x12\x16\n\x0eforward_coeffs\x18\x01 \x03(\x01\x12\x11\n\tmin_val_x\x18\x02 \x01(\x01\x12\x11\n\tmax_val_x\x18\x03 \x01(\x01\x12\x1d\n\x15num_points_to_compute\x18\x04 \x01(\x05\x12\x1a\n\x12reverse_poly_order\x18\x05 \x01(\x05"K\n!CalculateReversePolyCoeffResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x16\n\x0ereverse_coeffs\x18\x02 \x03(\x01"\xee\x01\n\x19CfgAnlgEdgeRefTrigRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0etrigger_source\x18\x02 \x01(\t\x12-\n\rtrigger_slope\x18\x03 \x01(\x0e2\x14.nidaqmx_grpc.Slope1H\x00\x12\x1b\n\x11trigger_slope_raw\x18\x04 \x01(\x05H\x00\x12\x15\n\rtrigger_level\x18\x05 \x01(\x01\x12\x1a\n\x12pretrigger_samples\x18\x06 \x01(\rB\x14\n\x12trigger_slope_enum",\n\x1aCfgAnlgEdgeRefTrigResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd4\x01\n\x1bCfgAnlgEdgeStartTrigRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0etrigger_source\x18\x02 \x01(\t\x12-\n\rtrigger_slope\x18\x03 \x01(\x0e2\x14.nidaqmx_grpc.Slope1H\x00\x12\x1b\n\x11trigger_slope_raw\x18\x04 \x01(\x05H\x00\x12\x15\n\rtrigger_level\x18\x05 \x01(\x01B\x14\n\x12trigger_slope_enum".\n\x1cCfgAnlgEdgeStartTrigResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xcb\x01\n\x1eCfgAnlgMultiEdgeRefTrigRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x17\n\x0ftrigger_sources\x18\x02 \x01(\t\x121\n\x13trigger_slope_array\x18\x03 \x03(\x0e2\x14.nidaqmx_grpc.Slope1\x12\x1b\n\x13trigger_level_array\x18\x04 \x03(\x01\x12\x1a\n\x12pretrigger_samples\x18\x05 \x01(\r"1\n\x1fCfgAnlgMultiEdgeRefTrigResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb1\x01\n CfgAnlgMultiEdgeStartTrigRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x17\n\x0ftrigger_sources\x18\x02 \x01(\t\x121\n\x13trigger_slope_array\x18\x03 \x03(\x0e2\x14.nidaqmx_grpc.Slope1\x12\x1b\n\x13trigger_level_array\x18\x04 \x03(\x01"3\n!CfgAnlgMultiEdgeStartTrigResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x92\x02\n\x1bCfgAnlgWindowRefTrigRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0etrigger_source\x18\x02 \x01(\t\x12=\n\x0ctrigger_when\x18\x03 \x01(\x0e2%.nidaqmx_grpc.WindowTriggerCondition1H\x00\x12\x1a\n\x10trigger_when_raw\x18\x04 \x01(\x05H\x00\x12\x12\n\nwindow_top\x18\x05 \x01(\x01\x12\x15\n\rwindow_bottom\x18\x06 \x01(\x01\x12\x1a\n\x12pretrigger_samples\x18\x07 \x01(\rB\x13\n\x11trigger_when_enum".\n\x1cCfgAnlgWindowRefTrigResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xf8\x01\n\x1dCfgAnlgWindowStartTrigRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0etrigger_source\x18\x02 \x01(\t\x12=\n\x0ctrigger_when\x18\x03 \x01(\x0e2%.nidaqmx_grpc.WindowTriggerCondition1H\x00\x12\x1a\n\x10trigger_when_raw\x18\x04 \x01(\x05H\x00\x12\x12\n\nwindow_top\x18\x05 \x01(\x01\x12\x15\n\rwindow_bottom\x18\x06 \x01(\x01B\x13\n\x11trigger_when_enum"0\n\x1eCfgAnlgWindowStartTrigResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xef\x04\n+CfgBurstHandshakingTimingExportClockRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x124\n\x0bsample_mode\x18\x02 \x01(\x0e2\x1d.nidaqmx_grpc.AcquisitionTypeH\x00\x12\x19\n\x0fsample_mode_raw\x18\x03 \x01(\x05H\x00\x12\x16\n\x0esamps_per_chan\x18\x04 \x01(\x04\x12\x17\n\x0fsample_clk_rate\x18\x05 \x01(\x01\x12\x1c\n\x14sample_clk_outp_term\x18\x06 \x01(\t\x12<\n\x19sample_clk_pulse_polarity\x18\x07 \x01(\x0e2\x17.nidaqmx_grpc.Polarity2H\x01\x12\'\n\x1dsample_clk_pulse_polarity_raw\x18\x08 \x01(\x05H\x01\x12*\n\npause_when\x18\t \x01(\x0e2\x14.nidaqmx_grpc.Level1H\x02\x12\x18\n\x0epause_when_raw\x18\n \x01(\x05H\x02\x12;\n\x18ready_event_active_level\x18\x0b \x01(\x0e2\x17.nidaqmx_grpc.Polarity2H\x03\x12&\n\x1cready_event_active_level_raw\x18\x0c \x01(\x05H\x03B\x12\n\x10sample_mode_enumB \n\x1esample_clk_pulse_polarity_enumB\x11\n\x0fpause_when_enumB\x1f\n\x1dready_event_active_level_enum">\n,CfgBurstHandshakingTimingExportClockResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xdc\x04\n+CfgBurstHandshakingTimingImportClockRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x124\n\x0bsample_mode\x18\x02 \x01(\x0e2\x1d.nidaqmx_grpc.AcquisitionTypeH\x00\x12\x19\n\x0fsample_mode_raw\x18\x03 \x01(\x05H\x00\x12\x16\n\x0esamps_per_chan\x18\x04 \x01(\x04\x12\x17\n\x0fsample_clk_rate\x18\x05 \x01(\x01\x12\x16\n\x0esample_clk_src\x18\x06 \x01(\t\x125\n\x16sample_clk_active_edge\x18\x07 \x01(\x0e2\x13.nidaqmx_grpc.Edge1H\x01\x12$\n\x1asample_clk_active_edge_raw\x18\x08 \x01(\x05H\x01\x12*\n\npause_when\x18\t \x01(\x0e2\x14.nidaqmx_grpc.Level1H\x02\x12\x18\n\x0epause_when_raw\x18\n \x01(\x05H\x02\x12;\n\x18ready_event_active_level\x18\x0b \x01(\x0e2\x17.nidaqmx_grpc.Polarity2H\x03\x12&\n\x1cready_event_active_level_raw\x18\x0c \x01(\x05H\x03B\x12\n\x10sample_mode_enumB\x1d\n\x1bsample_clk_active_edge_enumB\x11\n\x0fpause_when_enumB\x1f\n\x1dready_event_active_level_enum">\n,CfgBurstHandshakingTimingImportClockResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xf9\x01\n\x1fCfgChangeDetectionTimingRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10rising_edge_chan\x18\x02 \x01(\t\x12\x19\n\x11falling_edge_chan\x18\x03 \x01(\t\x124\n\x0bsample_mode\x18\x04 \x01(\x0e2\x1d.nidaqmx_grpc.AcquisitionTypeH\x00\x12\x19\n\x0fsample_mode_raw\x18\x05 \x01(\x05H\x00\x12\x16\n\x0esamps_per_chan\x18\x06 \x01(\x04B\x12\n\x10sample_mode_enum"2\n CfgChangeDetectionTimingResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd2\x01\n\x18CfgDigEdgeRefTrigRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0etrigger_source\x18\x02 \x01(\t\x12+\n\x0ctrigger_edge\x18\x03 \x01(\x0e2\x13.nidaqmx_grpc.Edge1H\x00\x12\x1a\n\x10trigger_edge_raw\x18\x04 \x01(\x05H\x00\x12\x1a\n\x12pretrigger_samples\x18\x05 \x01(\rB\x13\n\x11trigger_edge_enum"+\n\x19CfgDigEdgeRefTrigResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb8\x01\n\x1aCfgDigEdgeStartTrigRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0etrigger_source\x18\x02 \x01(\t\x12+\n\x0ctrigger_edge\x18\x03 \x01(\x0e2\x13.nidaqmx_grpc.Edge1H\x00\x12\x1a\n\x10trigger_edge_raw\x18\x04 \x01(\x05H\x00B\x13\n\x11trigger_edge_enum"-\n\x1bCfgDigEdgeStartTrigResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x81\x02\n\x1bCfgDigPatternRefTrigRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0etrigger_source\x18\x02 \x01(\t\x12\x17\n\x0ftrigger_pattern\x18\x03 \x01(\t\x12>\n\x0ctrigger_when\x18\x04 \x01(\x0e2&.nidaqmx_grpc.DigitalPatternCondition1H\x00\x12\x1a\n\x10trigger_when_raw\x18\x05 \x01(\x05H\x00\x12\x1a\n\x12pretrigger_samples\x18\x06 \x01(\rB\x13\n\x11trigger_when_enum".\n\x1cCfgDigPatternRefTrigResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xe7\x01\n\x1dCfgDigPatternStartTrigRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0etrigger_source\x18\x02 \x01(\t\x12\x17\n\x0ftrigger_pattern\x18\x03 \x01(\t\x12>\n\x0ctrigger_when\x18\x04 \x01(\x0e2&.nidaqmx_grpc.DigitalPatternCondition1H\x00\x12\x1a\n\x10trigger_when_raw\x18\x05 \x01(\x05H\x00B\x13\n\x11trigger_when_enum"0\n\x1eCfgDigPatternStartTrigResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc0\x01\n\x1bCfgHandshakingTimingRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x124\n\x0bsample_mode\x18\x02 \x01(\x0e2\x1d.nidaqmx_grpc.AcquisitionTypeH\x00\x12\x19\n\x0fsample_mode_raw\x18\x03 \x01(\x05H\x00\x12\x16\n\x0esamps_per_chan\x18\x04 \x01(\x04B\x12\n\x10sample_mode_enum".\n\x1cCfgHandshakingTimingResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xbd\x01\n\x18CfgImplicitTimingRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x124\n\x0bsample_mode\x18\x02 \x01(\x0e2\x1d.nidaqmx_grpc.AcquisitionTypeH\x00\x12\x19\n\x0fsample_mode_raw\x18\x03 \x01(\x05H\x00\x12\x16\n\x0esamps_per_chan\x18\x04 \x01(\x04B\x12\n\x10sample_mode_enum"+\n\x19CfgImplicitTimingResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"Y\n\x15CfgInputBufferRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\r"(\n\x16CfgInputBufferResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"Z\n\x16CfgOutputBufferRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\r")\n\x17CfgOutputBufferResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xbe\x02\n CfgPipelinedSampClkTimingRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0e\n\x06source\x18\x02 \x01(\t\x12\x0c\n\x04rate\x18\x03 \x01(\x01\x12*\n\x0bactive_edge\x18\x04 \x01(\x0e2\x13.nidaqmx_grpc.Edge1H\x00\x12\x19\n\x0factive_edge_raw\x18\x05 \x01(\x05H\x00\x124\n\x0bsample_mode\x18\x06 \x01(\x0e2\x1d.nidaqmx_grpc.AcquisitionTypeH\x01\x12\x19\n\x0fsample_mode_raw\x18\x07 \x01(\x05H\x01\x12\x16\n\x0esamps_per_chan\x18\x08 \x01(\x04B\x12\n\x10active_edge_enumB\x12\n\x10sample_mode_enum"3\n!CfgPipelinedSampClkTimingResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb5\x02\n\x17CfgSampClkTimingRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0e\n\x06source\x18\x02 \x01(\t\x12\x0c\n\x04rate\x18\x03 \x01(\x01\x12*\n\x0bactive_edge\x18\x04 \x01(\x0e2\x13.nidaqmx_grpc.Edge1H\x00\x12\x19\n\x0factive_edge_raw\x18\x05 \x01(\x05H\x00\x124\n\x0bsample_mode\x18\x06 \x01(\x0e2\x1d.nidaqmx_grpc.AcquisitionTypeH\x01\x12\x19\n\x0fsample_mode_raw\x18\x07 \x01(\x05H\x01\x12\x16\n\x0esamps_per_chan\x18\x08 \x01(\x04B\x12\n\x10active_edge_enumB\x12\n\x10sample_mode_enum"*\n\x18CfgSampClkTimingResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc3\x01\n\x17CfgTimeStartTrigRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12(\n\x04when\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12-\n\ttimescale\x18\x03 \x01(\x0e2\x18.nidaqmx_grpc.Timescale2H\x00\x12\x17\n\rtimescale_raw\x18\x04 \x01(\x05H\x00B\x10\n\x0etimescale_enum"*\n\x18CfgTimeStartTrigResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb8\x01\n\x1fCfgWatchdogAOExpirStatesRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rchannel_names\x18\x02 \x01(\t\x12\x19\n\x11expir_state_array\x18\x03 \x03(\x01\x12=\n\x11output_type_array\x18\x04 \x03(\x0e2".nidaqmx_grpc.WatchdogAOOutputType"2\n CfgWatchdogAOExpirStatesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x9d\x01\n\x1fCfgWatchdogCOExpirStatesRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rchannel_names\x18\x02 \x01(\t\x12=\n\x11expir_state_array\x18\x03 \x03(\x0e2".nidaqmx_grpc.WatchdogCOExpirState"2\n CfgWatchdogCOExpirStatesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x99\x01\n\x1fCfgWatchdogDOExpirStatesRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rchannel_names\x18\x02 \x01(\t\x129\n\x11expir_state_array\x18\x03 \x03(\x0e2\x1e.nidaqmx_grpc.DigitalLineState"2\n CfgWatchdogDOExpirStatesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05",\n\x10ClearTEDSRequest\x12\x18\n\x10physical_channel\x18\x01 \x01(\t"#\n\x11ClearTEDSResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"8\n\x10ClearTaskRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"#\n\x11ClearTaskResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xaa\x02\n\x17ConfigureLoggingRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t\x121\n\x0clogging_mode\x18\x03 \x01(\x0e2\x19.nidaqmx_grpc.LoggingModeH\x00\x12\x1a\n\x10logging_mode_raw\x18\x04 \x01(\x05H\x00\x12\x12\n\ngroup_name\x18\x05 \x01(\t\x123\n\toperation\x18\x06 \x01(\x0e2\x1e.nidaqmx_grpc.LoggingOperationH\x01\x12\x17\n\roperation_raw\x18\x07 \x01(\x05H\x01B\x13\n\x11logging_mode_enumB\x10\n\x0eoperation_enum"*\n\x18ConfigureLoggingResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"C\n\x14ConfigureTEDSRequest\x12\x18\n\x10physical_channel\x18\x01 \x01(\t\x12\x11\n\tfile_path\x18\x02 \x01(\t"\'\n\x15ConfigureTEDSResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xbf\x01\n\x13ConnectTermsRequest\x12\x17\n\x0fsource_terminal\x18\x01 \x01(\t\x12\x1c\n\x14destination_terminal\x18\x02 \x01(\t\x128\n\x10signal_modifiers\x18\x03 \x01(\x0e2\x1c.nidaqmx_grpc.InvertPolarityH\x00\x12\x1e\n\x14signal_modifiers_raw\x18\x04 \x01(\x05H\x00B\x17\n\x15signal_modifiers_enum"&\n\x14ConnectTermsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x9e\x01\n\x1aControlWatchdogTaskRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x125\n\x06action\x18\x02 \x01(\x0e2#.nidaqmx_grpc.WatchdogControlActionH\x00\x12\x14\n\naction_raw\x18\x03 \x01(\x05H\x00B\r\n\x0baction_enum"-\n\x1bControlWatchdogTaskResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xde\x05\n&CreateAIAccel4WireDCVoltageChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12@\n\x0fterminal_config\x18\x04 \x01(\x0e2%.nidaqmx_grpc.InputTermCfgWithDefaultH\x00\x12\x1d\n\x13terminal_config_raw\x18\x05 \x01(\x05H\x00\x12\x0f\n\x07min_val\x18\x06 \x01(\x01\x12\x0f\n\x07max_val\x18\x07 \x01(\x01\x12*\n\x05units\x18\x08 \x01(\x0e2\x19.nidaqmx_grpc.AccelUnits2H\x01\x12\x13\n\tunits_raw\x18\t \x01(\x05H\x01\x12\x13\n\x0bsensitivity\x18\n \x01(\x01\x12A\n\x11sensitivity_units\x18\x0b \x01(\x0e2$.nidaqmx_grpc.AccelSensitivityUnits1H\x02\x12\x1f\n\x15sensitivity_units_raw\x18\x0c \x01(\x05H\x02\x12>\n\x14voltage_excit_source\x18\r \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x03\x12"\n\x18voltage_excit_source_raw\x18\x0e \x01(\x05H\x03\x12\x19\n\x11voltage_excit_val\x18\x0f \x01(\x01\x12\x1d\n\x15use_excit_for_scaling\x18\x10 \x01(\x08\x12\x19\n\x11custom_scale_name\x18\x11 \x01(\tB\x16\n\x14terminal_config_enumB\x0c\n\nunits_enumB\x18\n\x16sensitivity_units_enumB\x1b\n\x19voltage_excit_source_enum"9\n\'CreateAIAccel4WireDCVoltageChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb1\x05\n\x18CreateAIAccelChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12@\n\x0fterminal_config\x18\x04 \x01(\x0e2%.nidaqmx_grpc.InputTermCfgWithDefaultH\x00\x12\x1d\n\x13terminal_config_raw\x18\x05 \x01(\x05H\x00\x12\x0f\n\x07min_val\x18\x06 \x01(\x01\x12\x0f\n\x07max_val\x18\x07 \x01(\x01\x12*\n\x05units\x18\x08 \x01(\x0e2\x19.nidaqmx_grpc.AccelUnits2H\x01\x12\x13\n\tunits_raw\x18\t \x01(\x05H\x01\x12\x13\n\x0bsensitivity\x18\n \x01(\x01\x12A\n\x11sensitivity_units\x18\x0b \x01(\x0e2$.nidaqmx_grpc.AccelSensitivityUnits1H\x02\x12\x1f\n\x15sensitivity_units_raw\x18\x0c \x01(\x05H\x02\x12>\n\x14current_excit_source\x18\r \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x03\x12"\n\x18current_excit_source_raw\x18\x0e \x01(\x05H\x03\x12\x19\n\x11current_excit_val\x18\x0f \x01(\x01\x12\x19\n\x11custom_scale_name\x18\x10 \x01(\tB\x16\n\x14terminal_config_enumB\x0c\n\nunits_enumB\x18\n\x16sensitivity_units_enumB\x1b\n\x19current_excit_source_enum"+\n\x19CreateAIAccelChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa0\x04\n\x1eCreateAIAccelChargeChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12@\n\x0fterminal_config\x18\x04 \x01(\x0e2%.nidaqmx_grpc.InputTermCfgWithDefaultH\x00\x12\x1d\n\x13terminal_config_raw\x18\x05 \x01(\x05H\x00\x12\x0f\n\x07min_val\x18\x06 \x01(\x01\x12\x0f\n\x07max_val\x18\x07 \x01(\x01\x12*\n\x05units\x18\x08 \x01(\x0e2\x19.nidaqmx_grpc.AccelUnits2H\x01\x12\x13\n\tunits_raw\x18\t \x01(\x05H\x01\x12\x13\n\x0bsensitivity\x18\n \x01(\x01\x12F\n\x11sensitivity_units\x18\x0b \x01(\x0e2).nidaqmx_grpc.AccelChargeSensitivityUnitsH\x02\x12\x1f\n\x15sensitivity_units_raw\x18\x0c \x01(\x05H\x02\x12\x19\n\x11custom_scale_name\x18\r \x01(\tB\x16\n\x14terminal_config_enumB\x0c\n\nunits_enumB\x18\n\x16sensitivity_units_enum"1\n\x1fCreateAIAccelChargeChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb9\x04\n\x19CreateAIBridgeChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12*\n\x05units\x18\x06 \x01(\x0e2\x19.nidaqmx_grpc.BridgeUnitsH\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12;\n\rbridge_config\x18\x08 \x01(\x0e2".nidaqmx_grpc.BridgeConfiguration1H\x01\x12\x1b\n\x11bridge_config_raw\x18\t \x01(\x05H\x01\x12>\n\x14voltage_excit_source\x18\n \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18voltage_excit_source_raw\x18\x0b \x01(\x05H\x02\x12\x19\n\x11voltage_excit_val\x18\x0c \x01(\x01\x12!\n\x19nominal_bridge_resistance\x18\r \x01(\x01\x12\x19\n\x11custom_scale_name\x18\x0e \x01(\tB\x0c\n\nunits_enumB\x14\n\x12bridge_config_enumB\x1b\n\x19voltage_excit_source_enum",\n\x1aCreateAIBridgeChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa9\x05\n"CreateAICalculatedPowerChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12 \n\x18voltage_physical_channel\x18\x02 \x01(\t\x12 \n\x18current_physical_channel\x18\x03 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x04 \x01(\t\x12@\n\x0fterminal_config\x18\x05 \x01(\x0e2%.nidaqmx_grpc.InputTermCfgWithDefaultH\x00\x12\x1d\n\x13terminal_config_raw\x18\x06 \x01(\x05H\x00\x12\x17\n\x0fvoltage_min_val\x18\x07 \x01(\x01\x12\x17\n\x0fvoltage_max_val\x18\x08 \x01(\x01\x12\x17\n\x0fcurrent_min_val\x18\t \x01(\x01\x12\x17\n\x0fcurrent_max_val\x18\n \x01(\x01\x12)\n\x05units\x18\x0b \x01(\x0e2\x18.nidaqmx_grpc.PowerUnitsH\x01\x12\x13\n\tunits_raw\x18\x0c \x01(\x05H\x01\x12S\n\x12shunt_resistor_loc\x18\r \x01(\x0e25.nidaqmx_grpc.CurrentShuntResistorLocationWithDefaultH\x02\x12 \n\x16shunt_resistor_loc_raw\x18\x0e \x01(\x05H\x02\x12\x1e\n\x16ext_shunt_resistor_val\x18\x0f \x01(\x01\x12\x19\n\x11custom_scale_name\x18\x10 \x01(\tB\x16\n\x14terminal_config_enumB\x0c\n\nunits_enumB\x19\n\x17shunt_resistor_loc_enum"5\n#CreateAICalculatedPowerChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x83\x03\n\x19CreateAIChargeChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12@\n\x0fterminal_config\x18\x04 \x01(\x0e2%.nidaqmx_grpc.InputTermCfgWithDefaultH\x00\x12\x1d\n\x13terminal_config_raw\x18\x05 \x01(\x05H\x00\x12\x0f\n\x07min_val\x18\x06 \x01(\x01\x12\x0f\n\x07max_val\x18\x07 \x01(\x01\x12*\n\x05units\x18\x08 \x01(\x0e2\x19.nidaqmx_grpc.ChargeUnitsH\x01\x12\x13\n\tunits_raw\x18\t \x01(\x05H\x01\x12\x19\n\x11custom_scale_name\x18\n \x01(\tB\x16\n\x14terminal_config_enumB\x0c\n\nunits_enum",\n\x1aCreateAIChargeChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb8\x04\n\x1aCreateAICurrentChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12@\n\x0fterminal_config\x18\x04 \x01(\x0e2%.nidaqmx_grpc.InputTermCfgWithDefaultH\x00\x12\x1d\n\x13terminal_config_raw\x18\x05 \x01(\x05H\x00\x12\x0f\n\x07min_val\x18\x06 \x01(\x01\x12\x0f\n\x07max_val\x18\x07 \x01(\x01\x12,\n\x05units\x18\x08 \x01(\x0e2\x1b.nidaqmx_grpc.CurrentUnits2H\x01\x12\x13\n\tunits_raw\x18\t \x01(\x05H\x01\x12S\n\x12shunt_resistor_loc\x18\n \x01(\x0e25.nidaqmx_grpc.CurrentShuntResistorLocationWithDefaultH\x02\x12 \n\x16shunt_resistor_loc_raw\x18\x0b \x01(\x05H\x02\x12\x1e\n\x16ext_shunt_resistor_val\x18\x0c \x01(\x01\x12\x19\n\x11custom_scale_name\x18\r \x01(\tB\x16\n\x14terminal_config_enumB\x0c\n\nunits_enumB\x19\n\x17shunt_resistor_loc_enum"-\n\x1bCreateAICurrentChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xbb\x04\n\x1dCreateAICurrentRMSChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12@\n\x0fterminal_config\x18\x04 \x01(\x0e2%.nidaqmx_grpc.InputTermCfgWithDefaultH\x00\x12\x1d\n\x13terminal_config_raw\x18\x05 \x01(\x05H\x00\x12\x0f\n\x07min_val\x18\x06 \x01(\x01\x12\x0f\n\x07max_val\x18\x07 \x01(\x01\x12,\n\x05units\x18\x08 \x01(\x0e2\x1b.nidaqmx_grpc.CurrentUnits2H\x01\x12\x13\n\tunits_raw\x18\t \x01(\x05H\x01\x12S\n\x12shunt_resistor_loc\x18\n \x01(\x0e25.nidaqmx_grpc.CurrentShuntResistorLocationWithDefaultH\x02\x12 \n\x16shunt_resistor_loc_raw\x18\x0b \x01(\x05H\x02\x12\x1e\n\x16ext_shunt_resistor_val\x18\x0c \x01(\x01\x12\x19\n\x11custom_scale_name\x18\r \x01(\tB\x16\n\x14terminal_config_enumB\x0c\n\nunits_enumB\x19\n\x17shunt_resistor_loc_enum"0\n\x1eCreateAICurrentRMSChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xe3\x06\n(CreateAIForceBridgePolynomialChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12)\n\x05units\x18\x06 \x01(\x0e2\x18.nidaqmx_grpc.ForceUnitsH\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12;\n\rbridge_config\x18\x08 \x01(\x0e2".nidaqmx_grpc.BridgeConfiguration1H\x01\x12\x1b\n\x11bridge_config_raw\x18\t \x01(\x05H\x01\x12>\n\x14voltage_excit_source\x18\n \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18voltage_excit_source_raw\x18\x0b \x01(\x05H\x02\x12\x19\n\x11voltage_excit_val\x18\x0c \x01(\x01\x12!\n\x19nominal_bridge_resistance\x18\r \x01(\x01\x12\x16\n\x0eforward_coeffs\x18\x0e \x03(\x01\x12\x16\n\x0ereverse_coeffs\x18\x0f \x03(\x01\x12?\n\x10electrical_units\x18\x10 \x01(\x0e2#.nidaqmx_grpc.BridgeElectricalUnitsH\x03\x12\x1e\n\x14electrical_units_raw\x18\x11 \x01(\x05H\x03\x12;\n\x0ephysical_units\x18\x12 \x01(\x0e2!.nidaqmx_grpc.BridgePhysicalUnitsH\x04\x12\x1c\n\x12physical_units_raw\x18\x13 \x01(\x05H\x04\x12\x19\n\x11custom_scale_name\x18\x14 \x01(\tB\x0c\n\nunits_enumB\x14\n\x12bridge_config_enumB\x1b\n\x19voltage_excit_source_enumB\x17\n\x15electrical_units_enumB\x15\n\x13physical_units_enum";\n)CreateAIForceBridgePolynomialChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xde\x06\n#CreateAIForceBridgeTableChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12)\n\x05units\x18\x06 \x01(\x0e2\x18.nidaqmx_grpc.ForceUnitsH\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12;\n\rbridge_config\x18\x08 \x01(\x0e2".nidaqmx_grpc.BridgeConfiguration1H\x01\x12\x1b\n\x11bridge_config_raw\x18\t \x01(\x05H\x01\x12>\n\x14voltage_excit_source\x18\n \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18voltage_excit_source_raw\x18\x0b \x01(\x05H\x02\x12\x19\n\x11voltage_excit_val\x18\x0c \x01(\x01\x12!\n\x19nominal_bridge_resistance\x18\r \x01(\x01\x12\x17\n\x0felectrical_vals\x18\x0e \x03(\x01\x12?\n\x10electrical_units\x18\x0f \x01(\x0e2#.nidaqmx_grpc.BridgeElectricalUnitsH\x03\x12\x1e\n\x14electrical_units_raw\x18\x10 \x01(\x05H\x03\x12\x15\n\rphysical_vals\x18\x11 \x03(\x01\x12;\n\x0ephysical_units\x18\x12 \x01(\x0e2!.nidaqmx_grpc.BridgePhysicalUnitsH\x04\x12\x1c\n\x12physical_units_raw\x18\x13 \x01(\x05H\x04\x12\x19\n\x11custom_scale_name\x18\x14 \x01(\tB\x0c\n\nunits_enumB\x14\n\x12bridge_config_enumB\x1b\n\x19voltage_excit_source_enumB\x17\n\x15electrical_units_enumB\x15\n\x13physical_units_enum"6\n$CreateAIForceBridgeTableChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xaa\x07\n)CreateAIForceBridgeTwoPointLinChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12)\n\x05units\x18\x06 \x01(\x0e2\x18.nidaqmx_grpc.ForceUnitsH\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12;\n\rbridge_config\x18\x08 \x01(\x0e2".nidaqmx_grpc.BridgeConfiguration1H\x01\x12\x1b\n\x11bridge_config_raw\x18\t \x01(\x05H\x01\x12>\n\x14voltage_excit_source\x18\n \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18voltage_excit_source_raw\x18\x0b \x01(\x05H\x02\x12\x19\n\x11voltage_excit_val\x18\x0c \x01(\x01\x12!\n\x19nominal_bridge_resistance\x18\r \x01(\x01\x12\x1c\n\x14first_electrical_val\x18\x0e \x01(\x01\x12\x1d\n\x15second_electrical_val\x18\x0f \x01(\x01\x12?\n\x10electrical_units\x18\x10 \x01(\x0e2#.nidaqmx_grpc.BridgeElectricalUnitsH\x03\x12\x1e\n\x14electrical_units_raw\x18\x11 \x01(\x05H\x03\x12\x1a\n\x12first_physical_val\x18\x12 \x01(\x01\x12\x1b\n\x13second_physical_val\x18\x13 \x01(\x01\x12;\n\x0ephysical_units\x18\x14 \x01(\x0e2!.nidaqmx_grpc.BridgePhysicalUnitsH\x04\x12\x1c\n\x12physical_units_raw\x18\x15 \x01(\x05H\x04\x12\x19\n\x11custom_scale_name\x18\x16 \x01(\tB\x0c\n\nunits_enumB\x14\n\x12bridge_config_enumB\x1b\n\x19voltage_excit_source_enumB\x17\n\x15electrical_units_enumB\x15\n\x13physical_units_enum"<\n*CreateAIForceBridgeTwoPointLinChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc1\x05\n\x1cCreateAIForceIEPEChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12@\n\x0fterminal_config\x18\x04 \x01(\x0e2%.nidaqmx_grpc.InputTermCfgWithDefaultH\x00\x12\x1d\n\x13terminal_config_raw\x18\x05 \x01(\x05H\x00\x12\x0f\n\x07min_val\x18\x06 \x01(\x01\x12\x0f\n\x07max_val\x18\x07 \x01(\x01\x12-\n\x05units\x18\x08 \x01(\x0e2\x1c.nidaqmx_grpc.ForceIEPEUnitsH\x01\x12\x13\n\tunits_raw\x18\t \x01(\x05H\x01\x12\x13\n\x0bsensitivity\x18\n \x01(\x01\x12J\n\x11sensitivity_units\x18\x0b \x01(\x0e2-.nidaqmx_grpc.ForceIEPESensorSensitivityUnitsH\x02\x12\x1f\n\x15sensitivity_units_raw\x18\x0c \x01(\x05H\x02\x12>\n\x14current_excit_source\x18\r \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x03\x12"\n\x18current_excit_source_raw\x18\x0e \x01(\x05H\x03\x12\x19\n\x11current_excit_val\x18\x0f \x01(\x01\x12\x19\n\x11custom_scale_name\x18\x10 \x01(\tB\x16\n\x14terminal_config_enumB\x0c\n\nunits_enumB\x18\n\x16sensitivity_units_enumB\x1b\n\x19current_excit_source_enum"/\n\x1dCreateAIForceIEPEChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xbf\x02\n\x1eCreateAIFreqVoltageChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12-\n\x05units\x18\x06 \x01(\x0e2\x1c.nidaqmx_grpc.FrequencyUnitsH\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12\x17\n\x0fthreshold_level\x18\x08 \x01(\x01\x12\x12\n\nhysteresis\x18\t \x01(\x01\x12\x19\n\x11custom_scale_name\x18\n \x01(\tB\x0c\n\nunits_enum"1\n\x1fCreateAIFreqVoltageChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xbf\x04\n\x1dCreateAIMicrophoneChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12@\n\x0fterminal_config\x18\x04 \x01(\x0e2%.nidaqmx_grpc.InputTermCfgWithDefaultH\x00\x12\x1d\n\x13terminal_config_raw\x18\x05 \x01(\x05H\x00\x122\n\x05units\x18\x06 \x01(\x0e2!.nidaqmx_grpc.SoundPressureUnits1H\x01\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x01\x12\x17\n\x0fmic_sensitivity\x18\x08 \x01(\x01\x12\x1b\n\x13max_snd_press_level\x18\t \x01(\x01\x12>\n\x14current_excit_source\x18\n \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18current_excit_source_raw\x18\x0b \x01(\x05H\x02\x12\x19\n\x11current_excit_val\x18\x0c \x01(\x01\x12\x19\n\x11custom_scale_name\x18\r \x01(\tB\x16\n\x14terminal_config_enumB\x0c\n\nunits_enumB\x1b\n\x19current_excit_source_enum"0\n\x1eCreateAIMicrophoneChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xba\x03\n\'CreateAIPosEddyCurrProxProbeChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12+\n\x05units\x18\x06 \x01(\x0e2\x1a.nidaqmx_grpc.LengthUnits2H\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12\x13\n\x0bsensitivity\x18\x08 \x01(\x01\x12O\n\x11sensitivity_units\x18\t \x01(\x0e22.nidaqmx_grpc.EddyCurrentProxProbeSensitivityUnitsH\x01\x12\x1f\n\x15sensitivity_units_raw\x18\n \x01(\x05H\x01\x12\x19\n\x11custom_scale_name\x18\x0b \x01(\tB\x0c\n\nunits_enumB\x18\n\x16sensitivity_units_enum":\n(CreateAIPosEddyCurrProxProbeChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd0\x05\n\x1aCreateAIPosLVDTChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12+\n\x05units\x18\x06 \x01(\x0e2\x1a.nidaqmx_grpc.LengthUnits2H\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12\x13\n\x0bsensitivity\x18\x08 \x01(\x01\x12@\n\x11sensitivity_units\x18\t \x01(\x0e2#.nidaqmx_grpc.LVDTSensitivityUnits1H\x01\x12\x1f\n\x15sensitivity_units_raw\x18\n \x01(\x05H\x01\x12>\n\x14voltage_excit_source\x18\x0b \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18voltage_excit_source_raw\x18\x0c \x01(\x05H\x02\x12\x19\n\x11voltage_excit_val\x18\r \x01(\x01\x12\x1a\n\x12voltage_excit_freq\x18\x0e \x01(\x01\x12;\n\x12ac_excit_wire_mode\x18\x0f \x01(\x0e2\x1d.nidaqmx_grpc.ACExcitWireModeH\x03\x12 \n\x16ac_excit_wire_mode_raw\x18\x10 \x01(\x05H\x03\x12\x19\n\x11custom_scale_name\x18\x11 \x01(\tB\x0c\n\nunits_enumB\x18\n\x16sensitivity_units_enumB\x1b\n\x19voltage_excit_source_enumB\x19\n\x17ac_excit_wire_mode_enum"-\n\x1bCreateAIPosLVDTChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xcf\x05\n\x1aCreateAIPosRVDTChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12*\n\x05units\x18\x06 \x01(\x0e2\x19.nidaqmx_grpc.AngleUnits1H\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12\x13\n\x0bsensitivity\x18\x08 \x01(\x01\x12@\n\x11sensitivity_units\x18\t \x01(\x0e2#.nidaqmx_grpc.RVDTSensitivityUnits1H\x01\x12\x1f\n\x15sensitivity_units_raw\x18\n \x01(\x05H\x01\x12>\n\x14voltage_excit_source\x18\x0b \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18voltage_excit_source_raw\x18\x0c \x01(\x05H\x02\x12\x19\n\x11voltage_excit_val\x18\r \x01(\x01\x12\x1a\n\x12voltage_excit_freq\x18\x0e \x01(\x01\x12;\n\x12ac_excit_wire_mode\x18\x0f \x01(\x0e2\x1d.nidaqmx_grpc.ACExcitWireModeH\x03\x12 \n\x16ac_excit_wire_mode_raw\x18\x10 \x01(\x05H\x03\x12\x19\n\x11custom_scale_name\x18\x11 \x01(\tB\x0c\n\nunits_enumB\x18\n\x16sensitivity_units_enumB\x1b\n\x19voltage_excit_source_enumB\x19\n\x17ac_excit_wire_mode_enum"-\n\x1bCreateAIPosRVDTChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc8\x01\n\x18CreateAIPowerChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x18\n\x10voltage_setpoint\x18\x04 \x01(\x01\x12\x18\n\x10current_setpoint\x18\x05 \x01(\x01\x12\x15\n\routput_enable\x18\x06 \x01(\x08"+\n\x19CreateAIPowerChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xe9\x06\n+CreateAIPressureBridgePolynomialChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12,\n\x05units\x18\x06 \x01(\x0e2\x1b.nidaqmx_grpc.PressureUnitsH\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12;\n\rbridge_config\x18\x08 \x01(\x0e2".nidaqmx_grpc.BridgeConfiguration1H\x01\x12\x1b\n\x11bridge_config_raw\x18\t \x01(\x05H\x01\x12>\n\x14voltage_excit_source\x18\n \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18voltage_excit_source_raw\x18\x0b \x01(\x05H\x02\x12\x19\n\x11voltage_excit_val\x18\x0c \x01(\x01\x12!\n\x19nominal_bridge_resistance\x18\r \x01(\x01\x12\x16\n\x0eforward_coeffs\x18\x0e \x03(\x01\x12\x16\n\x0ereverse_coeffs\x18\x0f \x03(\x01\x12?\n\x10electrical_units\x18\x10 \x01(\x0e2#.nidaqmx_grpc.BridgeElectricalUnitsH\x03\x12\x1e\n\x14electrical_units_raw\x18\x11 \x01(\x05H\x03\x12;\n\x0ephysical_units\x18\x12 \x01(\x0e2!.nidaqmx_grpc.BridgePhysicalUnitsH\x04\x12\x1c\n\x12physical_units_raw\x18\x13 \x01(\x05H\x04\x12\x19\n\x11custom_scale_name\x18\x14 \x01(\tB\x0c\n\nunits_enumB\x14\n\x12bridge_config_enumB\x1b\n\x19voltage_excit_source_enumB\x17\n\x15electrical_units_enumB\x15\n\x13physical_units_enum">\n,CreateAIPressureBridgePolynomialChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xe4\x06\n&CreateAIPressureBridgeTableChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12,\n\x05units\x18\x06 \x01(\x0e2\x1b.nidaqmx_grpc.PressureUnitsH\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12;\n\rbridge_config\x18\x08 \x01(\x0e2".nidaqmx_grpc.BridgeConfiguration1H\x01\x12\x1b\n\x11bridge_config_raw\x18\t \x01(\x05H\x01\x12>\n\x14voltage_excit_source\x18\n \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18voltage_excit_source_raw\x18\x0b \x01(\x05H\x02\x12\x19\n\x11voltage_excit_val\x18\x0c \x01(\x01\x12!\n\x19nominal_bridge_resistance\x18\r \x01(\x01\x12\x17\n\x0felectrical_vals\x18\x0e \x03(\x01\x12?\n\x10electrical_units\x18\x0f \x01(\x0e2#.nidaqmx_grpc.BridgeElectricalUnitsH\x03\x12\x1e\n\x14electrical_units_raw\x18\x10 \x01(\x05H\x03\x12\x15\n\rphysical_vals\x18\x11 \x03(\x01\x12;\n\x0ephysical_units\x18\x12 \x01(\x0e2!.nidaqmx_grpc.BridgePhysicalUnitsH\x04\x12\x1c\n\x12physical_units_raw\x18\x13 \x01(\x05H\x04\x12\x19\n\x11custom_scale_name\x18\x14 \x01(\tB\x0c\n\nunits_enumB\x14\n\x12bridge_config_enumB\x1b\n\x19voltage_excit_source_enumB\x17\n\x15electrical_units_enumB\x15\n\x13physical_units_enum"9\n\'CreateAIPressureBridgeTableChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb0\x07\n,CreateAIPressureBridgeTwoPointLinChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12,\n\x05units\x18\x06 \x01(\x0e2\x1b.nidaqmx_grpc.PressureUnitsH\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12;\n\rbridge_config\x18\x08 \x01(\x0e2".nidaqmx_grpc.BridgeConfiguration1H\x01\x12\x1b\n\x11bridge_config_raw\x18\t \x01(\x05H\x01\x12>\n\x14voltage_excit_source\x18\n \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18voltage_excit_source_raw\x18\x0b \x01(\x05H\x02\x12\x19\n\x11voltage_excit_val\x18\x0c \x01(\x01\x12!\n\x19nominal_bridge_resistance\x18\r \x01(\x01\x12\x1c\n\x14first_electrical_val\x18\x0e \x01(\x01\x12\x1d\n\x15second_electrical_val\x18\x0f \x01(\x01\x12?\n\x10electrical_units\x18\x10 \x01(\x0e2#.nidaqmx_grpc.BridgeElectricalUnitsH\x03\x12\x1e\n\x14electrical_units_raw\x18\x11 \x01(\x05H\x03\x12\x1a\n\x12first_physical_val\x18\x12 \x01(\x01\x12\x1b\n\x13second_physical_val\x18\x13 \x01(\x01\x12;\n\x0ephysical_units\x18\x14 \x01(\x0e2!.nidaqmx_grpc.BridgePhysicalUnitsH\x04\x12\x1c\n\x12physical_units_raw\x18\x15 \x01(\x05H\x04\x12\x19\n\x11custom_scale_name\x18\x16 \x01(\tB\x0c\n\nunits_enumB\x14\n\x12bridge_config_enumB\x1b\n\x19voltage_excit_source_enumB\x17\n\x15electrical_units_enumB\x15\n\x13physical_units_enum"?\n-CreateAIPressureBridgeTwoPointLinChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xed\x04\n\x16CreateAIRTDChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12/\n\x05units\x18\x06 \x01(\x0e2\x1e.nidaqmx_grpc.TemperatureUnitsH\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12*\n\x08rtd_type\x18\x08 \x01(\x0e2\x16.nidaqmx_grpc.RTDType1H\x01\x12\x16\n\x0crtd_type_raw\x18\t \x01(\x05H\x01\x12B\n\x11resistance_config\x18\n \x01(\x0e2%.nidaqmx_grpc.ResistanceConfigurationH\x02\x12\x1f\n\x15resistance_config_raw\x18\x0b \x01(\x05H\x02\x12>\n\x14current_excit_source\x18\x0c \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x03\x12"\n\x18current_excit_source_raw\x18\r \x01(\x05H\x03\x12\x19\n\x11current_excit_val\x18\x0e \x01(\x01\x12\n\n\x02r0\x18\x0f \x01(\x01B\x0c\n\nunits_enumB\x0f\n\rrtd_type_enumB\x18\n\x16resistance_config_enumB\x1b\n\x19current_excit_source_enum")\n\x17CreateAIRTDChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xae\x04\n\x1dCreateAIResistanceChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12/\n\x05units\x18\x06 \x01(\x0e2\x1e.nidaqmx_grpc.ResistanceUnits2H\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12B\n\x11resistance_config\x18\x08 \x01(\x0e2%.nidaqmx_grpc.ResistanceConfigurationH\x01\x12\x1f\n\x15resistance_config_raw\x18\t \x01(\x05H\x01\x12>\n\x14current_excit_source\x18\n \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18current_excit_source_raw\x18\x0b \x01(\x05H\x02\x12\x19\n\x11current_excit_val\x18\x0c \x01(\x01\x12\x19\n\x11custom_scale_name\x18\r \x01(\tB\x0c\n\nunits_enumB\x18\n\x16resistance_config_enumB\x1b\n\x19current_excit_source_enum"0\n\x1eCreateAIResistanceChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xf7\x05\n$CreateAIRosetteStrainGageChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12;\n\x0crosette_type\x18\x06 \x01(\x0e2#.nidaqmx_grpc.StrainGageRosetteTypeH\x00\x12\x1a\n\x10rosette_type_raw\x18\x07 \x01(\x05H\x00\x12\x18\n\x10gage_orientation\x18\x08 \x01(\x01\x12J\n\x12rosette_meas_types\x18\t \x03(\x0e2..nidaqmx_grpc.StrainGageRosetteMeasurementType\x12<\n\rstrain_config\x18\n \x01(\x0e2#.nidaqmx_grpc.StrainGageBridgeType1H\x01\x12\x1b\n\x11strain_config_raw\x18\x0b \x01(\x05H\x01\x12>\n\x14voltage_excit_source\x18\x0c \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18voltage_excit_source_raw\x18\r \x01(\x05H\x02\x12\x19\n\x11voltage_excit_val\x18\x0e \x01(\x01\x12\x13\n\x0bgage_factor\x18\x0f \x01(\x01\x12\x1f\n\x17nominal_gage_resistance\x18\x10 \x01(\x01\x12\x15\n\rpoisson_ratio\x18\x11 \x01(\x01\x12\x1c\n\x14lead_wire_resistance\x18\x12 \x01(\x01B\x13\n\x11rosette_type_enumB\x14\n\x12strain_config_enumB\x1b\n\x19voltage_excit_source_enum"7\n%CreateAIRosetteStrainGageChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa7\x05\n\x1dCreateAIStrainGageChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12+\n\x05units\x18\x06 \x01(\x0e2\x1a.nidaqmx_grpc.StrainUnits1H\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12<\n\rstrain_config\x18\x08 \x01(\x0e2#.nidaqmx_grpc.StrainGageBridgeType1H\x01\x12\x1b\n\x11strain_config_raw\x18\t \x01(\x05H\x01\x12>\n\x14voltage_excit_source\x18\n \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18voltage_excit_source_raw\x18\x0b \x01(\x05H\x02\x12\x19\n\x11voltage_excit_val\x18\x0c \x01(\x01\x12\x13\n\x0bgage_factor\x18\r \x01(\x01\x12\x1e\n\x16initial_bridge_voltage\x18\x0e \x01(\x01\x12\x1f\n\x17nominal_gage_resistance\x18\x0f \x01(\x01\x12\x15\n\rpoisson_ratio\x18\x10 \x01(\x01\x12\x1c\n\x14lead_wire_resistance\x18\x11 \x01(\x01\x12\x19\n\x11custom_scale_name\x18\x12 \x01(\tB\x0c\n\nunits_enumB\x14\n\x12strain_config_enumB\x1b\n\x19voltage_excit_source_enum"0\n\x1eCreateAIStrainGageChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xdd\x01\n$CreateAITempBuiltInSensorChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12/\n\x05units\x18\x04 \x01(\x0e2\x1e.nidaqmx_grpc.TemperatureUnitsH\x00\x12\x13\n\tunits_raw\x18\x05 \x01(\x05H\x00B\x0c\n\nunits_enum"7\n%CreateAITempBuiltInSensorChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xf1\x03\n\x1aCreateAIThrmcplChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12/\n\x05units\x18\x06 \x01(\x0e2\x1e.nidaqmx_grpc.TemperatureUnitsH\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12<\n\x11thermocouple_type\x18\x08 \x01(\x0e2\x1f.nidaqmx_grpc.ThermocoupleType1H\x01\x12\x1f\n\x15thermocouple_type_raw\x18\t \x01(\x05H\x01\x12.\n\ncjc_source\x18\n \x01(\x0e2\x18.nidaqmx_grpc.CJCSource1H\x02\x12\x18\n\x0ecjc_source_raw\x18\x0b \x01(\x05H\x02\x12\x0f\n\x07cjc_val\x18\x0c \x01(\x01\x12\x13\n\x0bcjc_channel\x18\r \x01(\tB\x0c\n\nunits_enumB\x18\n\x16thermocouple_type_enumB\x11\n\x0fcjc_source_enum"-\n\x1bCreateAIThrmcplChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb4\x04\n\x1dCreateAIThrmstrChanIexRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12/\n\x05units\x18\x06 \x01(\x0e2\x1e.nidaqmx_grpc.TemperatureUnitsH\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12B\n\x11resistance_config\x18\x08 \x01(\x0e2%.nidaqmx_grpc.ResistanceConfigurationH\x01\x12\x1f\n\x15resistance_config_raw\x18\t \x01(\x05H\x01\x12>\n\x14current_excit_source\x18\n \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18current_excit_source_raw\x18\x0b \x01(\x05H\x02\x12\x19\n\x11current_excit_val\x18\x0c \x01(\x01\x12\t\n\x01a\x18\r \x01(\x01\x12\t\n\x01b\x18\x0e \x01(\x01\x12\t\n\x01c\x18\x0f \x01(\x01B\x0c\n\nunits_enumB\x18\n\x16resistance_config_enumB\x1b\n\x19current_excit_source_enum"0\n\x1eCreateAIThrmstrChanIexResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc0\x04\n\x1dCreateAIThrmstrChanVexRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12/\n\x05units\x18\x06 \x01(\x0e2\x1e.nidaqmx_grpc.TemperatureUnitsH\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12B\n\x11resistance_config\x18\x08 \x01(\x0e2%.nidaqmx_grpc.ResistanceConfigurationH\x01\x12\x1f\n\x15resistance_config_raw\x18\t \x01(\x05H\x01\x12>\n\x14voltage_excit_source\x18\n \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18voltage_excit_source_raw\x18\x0b \x01(\x05H\x02\x12\x19\n\x11voltage_excit_val\x18\x0c \x01(\x01\x12\t\n\x01a\x18\r \x01(\x01\x12\t\n\x01b\x18\x0e \x01(\x01\x12\t\n\x01c\x18\x0f \x01(\x01\x12\n\n\x02r1\x18\x10 \x01(\x01B\x0c\n\nunits_enumB\x18\n\x16resistance_config_enumB\x1b\n\x19voltage_excit_source_enum"0\n\x1eCreateAIThrmstrChanVexResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xe5\x06\n)CreateAITorqueBridgePolynomialChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12*\n\x05units\x18\x06 \x01(\x0e2\x19.nidaqmx_grpc.TorqueUnitsH\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12;\n\rbridge_config\x18\x08 \x01(\x0e2".nidaqmx_grpc.BridgeConfiguration1H\x01\x12\x1b\n\x11bridge_config_raw\x18\t \x01(\x05H\x01\x12>\n\x14voltage_excit_source\x18\n \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18voltage_excit_source_raw\x18\x0b \x01(\x05H\x02\x12\x19\n\x11voltage_excit_val\x18\x0c \x01(\x01\x12!\n\x19nominal_bridge_resistance\x18\r \x01(\x01\x12\x16\n\x0eforward_coeffs\x18\x0e \x03(\x01\x12\x16\n\x0ereverse_coeffs\x18\x0f \x03(\x01\x12?\n\x10electrical_units\x18\x10 \x01(\x0e2#.nidaqmx_grpc.BridgeElectricalUnitsH\x03\x12\x1e\n\x14electrical_units_raw\x18\x11 \x01(\x05H\x03\x12;\n\x0ephysical_units\x18\x12 \x01(\x0e2!.nidaqmx_grpc.BridgePhysicalUnitsH\x04\x12\x1c\n\x12physical_units_raw\x18\x13 \x01(\x05H\x04\x12\x19\n\x11custom_scale_name\x18\x14 \x01(\tB\x0c\n\nunits_enumB\x14\n\x12bridge_config_enumB\x1b\n\x19voltage_excit_source_enumB\x17\n\x15electrical_units_enumB\x15\n\x13physical_units_enum"<\n*CreateAITorqueBridgePolynomialChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xe0\x06\n$CreateAITorqueBridgeTableChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12*\n\x05units\x18\x06 \x01(\x0e2\x19.nidaqmx_grpc.TorqueUnitsH\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12;\n\rbridge_config\x18\x08 \x01(\x0e2".nidaqmx_grpc.BridgeConfiguration1H\x01\x12\x1b\n\x11bridge_config_raw\x18\t \x01(\x05H\x01\x12>\n\x14voltage_excit_source\x18\n \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18voltage_excit_source_raw\x18\x0b \x01(\x05H\x02\x12\x19\n\x11voltage_excit_val\x18\x0c \x01(\x01\x12!\n\x19nominal_bridge_resistance\x18\r \x01(\x01\x12\x17\n\x0felectrical_vals\x18\x0e \x03(\x01\x12?\n\x10electrical_units\x18\x0f \x01(\x0e2#.nidaqmx_grpc.BridgeElectricalUnitsH\x03\x12\x1e\n\x14electrical_units_raw\x18\x10 \x01(\x05H\x03\x12\x15\n\rphysical_vals\x18\x11 \x03(\x01\x12;\n\x0ephysical_units\x18\x12 \x01(\x0e2!.nidaqmx_grpc.BridgePhysicalUnitsH\x04\x12\x1c\n\x12physical_units_raw\x18\x13 \x01(\x05H\x04\x12\x19\n\x11custom_scale_name\x18\x14 \x01(\tB\x0c\n\nunits_enumB\x14\n\x12bridge_config_enumB\x1b\n\x19voltage_excit_source_enumB\x17\n\x15electrical_units_enumB\x15\n\x13physical_units_enum"7\n%CreateAITorqueBridgeTableChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xac\x07\n*CreateAITorqueBridgeTwoPointLinChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12*\n\x05units\x18\x06 \x01(\x0e2\x19.nidaqmx_grpc.TorqueUnitsH\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12;\n\rbridge_config\x18\x08 \x01(\x0e2".nidaqmx_grpc.BridgeConfiguration1H\x01\x12\x1b\n\x11bridge_config_raw\x18\t \x01(\x05H\x01\x12>\n\x14voltage_excit_source\x18\n \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18voltage_excit_source_raw\x18\x0b \x01(\x05H\x02\x12\x19\n\x11voltage_excit_val\x18\x0c \x01(\x01\x12!\n\x19nominal_bridge_resistance\x18\r \x01(\x01\x12\x1c\n\x14first_electrical_val\x18\x0e \x01(\x01\x12\x1d\n\x15second_electrical_val\x18\x0f \x01(\x01\x12?\n\x10electrical_units\x18\x10 \x01(\x0e2#.nidaqmx_grpc.BridgeElectricalUnitsH\x03\x12\x1e\n\x14electrical_units_raw\x18\x11 \x01(\x05H\x03\x12\x1a\n\x12first_physical_val\x18\x12 \x01(\x01\x12\x1b\n\x13second_physical_val\x18\x13 \x01(\x01\x12;\n\x0ephysical_units\x18\x14 \x01(\x0e2!.nidaqmx_grpc.BridgePhysicalUnitsH\x04\x12\x1c\n\x12physical_units_raw\x18\x15 \x01(\x05H\x04\x12\x19\n\x11custom_scale_name\x18\x16 \x01(\tB\x0c\n\nunits_enumB\x14\n\x12bridge_config_enumB\x1b\n\x19voltage_excit_source_enumB\x17\n\x15electrical_units_enumB\x15\n\x13physical_units_enum"=\n+CreateAITorqueBridgeTwoPointLinChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc6\x05\n\x1fCreateAIVelocityIEPEChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12@\n\x0fterminal_config\x18\x04 \x01(\x0e2%.nidaqmx_grpc.InputTermCfgWithDefaultH\x00\x12\x1d\n\x13terminal_config_raw\x18\x05 \x01(\x05H\x00\x12\x0f\n\x07min_val\x18\x06 \x01(\x01\x12\x0f\n\x07max_val\x18\x07 \x01(\x01\x12,\n\x05units\x18\x08 \x01(\x0e2\x1b.nidaqmx_grpc.VelocityUnitsH\x01\x12\x13\n\tunits_raw\x18\t \x01(\x05H\x01\x12\x13\n\x0bsensitivity\x18\n \x01(\x01\x12M\n\x11sensitivity_units\x18\x0b \x01(\x0e20.nidaqmx_grpc.VelocityIEPESensorSensitivityUnitsH\x02\x12\x1f\n\x15sensitivity_units_raw\x18\x0c \x01(\x05H\x02\x12>\n\x14current_excit_source\x18\r \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x03\x12"\n\x18current_excit_source_raw\x18\x0e \x01(\x05H\x03\x12\x19\n\x11current_excit_val\x18\x0f \x01(\x01\x12\x19\n\x11custom_scale_name\x18\x10 \x01(\tB\x16\n\x14terminal_config_enumB\x0c\n\nunits_enumB\x18\n\x16sensitivity_units_enumB\x1b\n\x19current_excit_source_enum"2\n CreateAIVelocityIEPEChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x86\x03\n\x1aCreateAIVoltageChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12@\n\x0fterminal_config\x18\x04 \x01(\x0e2%.nidaqmx_grpc.InputTermCfgWithDefaultH\x00\x12\x1d\n\x13terminal_config_raw\x18\x05 \x01(\x05H\x00\x12\x0f\n\x07min_val\x18\x06 \x01(\x01\x12\x0f\n\x07max_val\x18\x07 \x01(\x01\x12,\n\x05units\x18\x08 \x01(\x0e2\x1b.nidaqmx_grpc.VoltageUnits2H\x01\x12\x13\n\tunits_raw\x18\t \x01(\x05H\x01\x12\x19\n\x11custom_scale_name\x18\n \x01(\tB\x16\n\x14terminal_config_enumB\x0c\n\nunits_enum"-\n\x1bCreateAIVoltageChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xba\x05\n#CreateAIVoltageChanWithExcitRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12@\n\x0fterminal_config\x18\x04 \x01(\x0e2%.nidaqmx_grpc.InputTermCfgWithDefaultH\x00\x12\x1d\n\x13terminal_config_raw\x18\x05 \x01(\x05H\x00\x12\x0f\n\x07min_val\x18\x06 \x01(\x01\x12\x0f\n\x07max_val\x18\x07 \x01(\x01\x12,\n\x05units\x18\x08 \x01(\x0e2\x1b.nidaqmx_grpc.VoltageUnits2H\x01\x12\x13\n\tunits_raw\x18\t \x01(\x05H\x01\x12;\n\rbridge_config\x18\n \x01(\x0e2".nidaqmx_grpc.BridgeConfiguration1H\x02\x12\x1b\n\x11bridge_config_raw\x18\x0b \x01(\x05H\x02\x12>\n\x14voltage_excit_source\x18\x0c \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x03\x12"\n\x18voltage_excit_source_raw\x18\r \x01(\x05H\x03\x12\x19\n\x11voltage_excit_val\x18\x0e \x01(\x01\x12\x1d\n\x15use_excit_for_scaling\x18\x0f \x01(\x08\x12\x19\n\x11custom_scale_name\x18\x10 \x01(\tB\x16\n\x14terminal_config_enumB\x0c\n\nunits_enumB\x14\n\x12bridge_config_enumB\x1b\n\x19voltage_excit_source_enum"6\n$CreateAIVoltageChanWithExcitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x89\x03\n\x1dCreateAIVoltageRMSChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12@\n\x0fterminal_config\x18\x04 \x01(\x0e2%.nidaqmx_grpc.InputTermCfgWithDefaultH\x00\x12\x1d\n\x13terminal_config_raw\x18\x05 \x01(\x05H\x00\x12\x0f\n\x07min_val\x18\x06 \x01(\x01\x12\x0f\n\x07max_val\x18\x07 \x01(\x01\x12,\n\x05units\x18\x08 \x01(\x0e2\x1b.nidaqmx_grpc.VoltageUnits2H\x01\x12\x13\n\tunits_raw\x18\t \x01(\x05H\x01\x12\x19\n\x11custom_scale_name\x18\n \x01(\tB\x16\n\x14terminal_config_enumB\x0c\n\nunits_enum"0\n\x1eCreateAIVoltageRMSChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x8d\x02\n\x1aCreateAOCurrentChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12,\n\x05units\x18\x06 \x01(\x0e2\x1b.nidaqmx_grpc.CurrentUnits2H\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12\x19\n\x11custom_scale_name\x18\x08 \x01(\tB\x0c\n\nunits_enum"-\n\x1bCreateAOCurrentChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xfc\x01\n\x1aCreateAOFuncGenChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12)\n\x04type\x18\x04 \x01(\x0e2\x19.nidaqmx_grpc.FuncGenTypeH\x00\x12\x12\n\x08type_raw\x18\x05 \x01(\x05H\x00\x12\x0c\n\x04freq\x18\x06 \x01(\x01\x12\x11\n\tamplitude\x18\x07 \x01(\x01\x12\x0e\n\x06offset\x18\x08 \x01(\x01B\x0b\n\ttype_enum"-\n\x1bCreateAOFuncGenChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x8d\x02\n\x1aCreateAOVoltageChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12,\n\x05units\x18\x06 \x01(\x0e2\x1b.nidaqmx_grpc.VoltageUnits2H\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12\x19\n\x11custom_scale_name\x18\x08 \x01(\tB\x0c\n\nunits_enum"-\n\x1bCreateAOVoltageChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x87\x04\n\x1dCreateCIAngEncoderChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07counter\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x123\n\rdecoding_type\x18\x04 \x01(\x0e2\x1a.nidaqmx_grpc.EncoderType2H\x00\x12\x1b\n\x11decoding_type_raw\x18\x05 \x01(\x05H\x00\x12\x13\n\x0bzidx_enable\x18\x06 \x01(\x08\x12\x10\n\x08zidx_val\x18\x07 \x01(\x01\x127\n\nzidx_phase\x18\x08 \x01(\x0e2!.nidaqmx_grpc.EncoderZIndexPhase1H\x01\x12\x18\n\x0ezidx_phase_raw\x18\t \x01(\x05H\x01\x12*\n\x05units\x18\n \x01(\x0e2\x19.nidaqmx_grpc.AngleUnits2H\x02\x12\x13\n\tunits_raw\x18\x0b \x01(\x05H\x02\x12\x16\n\x0epulses_per_rev\x18\x0c \x01(\r\x12\x15\n\rinitial_angle\x18\r \x01(\x01\x12\x19\n\x11custom_scale_name\x18\x0e \x01(\tB\x14\n\x12decoding_type_enumB\x11\n\x0fzidx_phase_enumB\x0c\n\nunits_enum"0\n\x1eCreateCIAngEncoderChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x8f\x03\n\x1eCreateCIAngVelocityChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07counter\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x123\n\rdecoding_type\x18\x06 \x01(\x0e2\x1a.nidaqmx_grpc.EncoderType2H\x00\x12\x1b\n\x11decoding_type_raw\x18\x07 \x01(\x05H\x00\x123\n\x05units\x18\x08 \x01(\x0e2".nidaqmx_grpc.AngularVelocityUnitsH\x01\x12\x13\n\tunits_raw\x18\t \x01(\x05H\x01\x12\x16\n\x0epulses_per_rev\x18\n \x01(\r\x12\x19\n\x11custom_scale_name\x18\x0b \x01(\tB\x14\n\x12decoding_type_enumB\x0c\n\nunits_enum"1\n\x1fCreateCIAngVelocityChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc7\x02\n\x1dCreateCICountEdgesChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07counter\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12#\n\x04edge\x18\x04 \x01(\x0e2\x13.nidaqmx_grpc.Edge1H\x00\x12\x12\n\x08edge_raw\x18\x05 \x01(\x05H\x00\x12\x15\n\rinitial_count\x18\x06 \x01(\r\x128\n\x0fcount_direction\x18\x07 \x01(\x0e2\x1d.nidaqmx_grpc.CountDirection1H\x01\x12\x1d\n\x13count_direction_raw\x18\x08 \x01(\x05H\x01B\x0b\n\tedge_enumB\x16\n\x14count_direction_enum"0\n\x1eCreateCICountEdgesChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xfd\x01\n\x1cCreateCIDutyCycleChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07counter\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x10\n\x08min_freq\x18\x04 \x01(\x01\x12\x10\n\x08max_freq\x18\x05 \x01(\x01\x12#\n\x04edge\x18\x06 \x01(\x0e2\x13.nidaqmx_grpc.Edge1H\x00\x12\x12\n\x08edge_raw\x18\x07 \x01(\x05H\x00\x12\x19\n\x11custom_scale_name\x18\x08 \x01(\tB\x0b\n\tedge_enum"/\n\x1dCreateCIDutyCycleChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd9\x03\n\x17CreateCIFreqChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07counter\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12.\n\x05units\x18\x06 \x01(\x0e2\x1d.nidaqmx_grpc.FrequencyUnits3H\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12#\n\x04edge\x18\x08 \x01(\x0e2\x13.nidaqmx_grpc.Edge1H\x01\x12\x12\n\x08edge_raw\x18\t \x01(\x05H\x01\x12;\n\x0bmeas_method\x18\n \x01(\x0e2$.nidaqmx_grpc.CounterFrequencyMethodH\x02\x12\x19\n\x0fmeas_method_raw\x18\x0b \x01(\x05H\x02\x12\x11\n\tmeas_time\x18\x0c \x01(\x01\x12\x0f\n\x07divisor\x18\r \x01(\r\x12\x19\n\x11custom_scale_name\x18\x0e \x01(\tB\x0c\n\nunits_enumB\x0b\n\tedge_enumB\x12\n\x10meas_method_enum"*\n\x18CreateCIFreqChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc7\x02\n\x1fCreateCIGPSTimestampChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07counter\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12(\n\x05units\x18\x04 \x01(\x0e2\x17.nidaqmx_grpc.TimeUnitsH\x00\x12\x13\n\tunits_raw\x18\x05 \x01(\x05H\x00\x123\n\x0bsync_method\x18\x06 \x01(\x0e2\x1c.nidaqmx_grpc.GpsSignalType1H\x01\x12\x19\n\x0fsync_method_raw\x18\x07 \x01(\x05H\x01\x12\x19\n\x11custom_scale_name\x18\x08 \x01(\tB\x0c\n\nunits_enumB\x12\n\x10sync_method_enum"2\n CreateCIGPSTimestampChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x86\x04\n\x1dCreateCILinEncoderChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07counter\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x123\n\rdecoding_type\x18\x04 \x01(\x0e2\x1a.nidaqmx_grpc.EncoderType2H\x00\x12\x1b\n\x11decoding_type_raw\x18\x05 \x01(\x05H\x00\x12\x13\n\x0bzidx_enable\x18\x06 \x01(\x08\x12\x10\n\x08zidx_val\x18\x07 \x01(\x01\x127\n\nzidx_phase\x18\x08 \x01(\x0e2!.nidaqmx_grpc.EncoderZIndexPhase1H\x01\x12\x18\n\x0ezidx_phase_raw\x18\t \x01(\x05H\x01\x12+\n\x05units\x18\n \x01(\x0e2\x1a.nidaqmx_grpc.LengthUnits3H\x02\x12\x13\n\tunits_raw\x18\x0b \x01(\x05H\x02\x12\x16\n\x0edist_per_pulse\x18\x0c \x01(\x01\x12\x13\n\x0binitial_pos\x18\r \x01(\x01\x12\x19\n\x11custom_scale_name\x18\x0e \x01(\tB\x14\n\x12decoding_type_enumB\x11\n\x0fzidx_phase_enumB\x0c\n\nunits_enum"0\n\x1eCreateCILinEncoderChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x88\x03\n\x1eCreateCILinVelocityChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07counter\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x123\n\rdecoding_type\x18\x06 \x01(\x0e2\x1a.nidaqmx_grpc.EncoderType2H\x00\x12\x1b\n\x11decoding_type_raw\x18\x07 \x01(\x05H\x00\x12,\n\x05units\x18\x08 \x01(\x0e2\x1b.nidaqmx_grpc.VelocityUnitsH\x01\x12\x13\n\tunits_raw\x18\t \x01(\x05H\x01\x12\x16\n\x0edist_per_pulse\x18\n \x01(\x01\x12\x19\n\x11custom_scale_name\x18\x0b \x01(\tB\x14\n\x12decoding_type_enumB\x0c\n\nunits_enum"1\n\x1fCreateCILinVelocityChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd6\x03\n\x19CreateCIPeriodChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07counter\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12)\n\x05units\x18\x06 \x01(\x0e2\x18.nidaqmx_grpc.TimeUnits3H\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12#\n\x04edge\x18\x08 \x01(\x0e2\x13.nidaqmx_grpc.Edge1H\x01\x12\x12\n\x08edge_raw\x18\t \x01(\x05H\x01\x12;\n\x0bmeas_method\x18\n \x01(\x0e2$.nidaqmx_grpc.CounterFrequencyMethodH\x02\x12\x19\n\x0fmeas_method_raw\x18\x0b \x01(\x05H\x02\x12\x11\n\tmeas_time\x18\x0c \x01(\x01\x12\x0f\n\x07divisor\x18\r \x01(\r\x12\x19\n\x11custom_scale_name\x18\x0e \x01(\tB\x0c\n\nunits_enumB\x0b\n\tedge_enumB\x12\n\x10meas_method_enum",\n\x1aCreateCIPeriodChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xed\x01\n\x1cCreateCIPulseChanFreqRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07counter\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12.\n\x05units\x18\x06 \x01(\x0e2\x1d.nidaqmx_grpc.FrequencyUnits2H\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00B\x0c\n\nunits_enum"/\n\x1dCreateCIPulseChanFreqResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb4\x01\n\x1dCreateCIPulseChanTicksRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07counter\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x17\n\x0fsource_terminal\x18\x04 \x01(\t\x12\x0f\n\x07min_val\x18\x05 \x01(\x01\x12\x0f\n\x07max_val\x18\x06 \x01(\x01"0\n\x1eCreateCIPulseChanTicksResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xf0\x01\n\x1cCreateCIPulseChanTimeRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07counter\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x121\n\x05units\x18\x06 \x01(\x0e2 .nidaqmx_grpc.DigitalWidthUnits3H\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00B\x0c\n\nunits_enum"/\n\x1dCreateCIPulseChanTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xe5\x02\n\x1dCreateCIPulseWidthChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07counter\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12)\n\x05units\x18\x06 \x01(\x0e2\x18.nidaqmx_grpc.TimeUnits3H\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12,\n\rstarting_edge\x18\x08 \x01(\x0e2\x13.nidaqmx_grpc.Edge1H\x01\x12\x1b\n\x11starting_edge_raw\x18\t \x01(\x05H\x01\x12\x19\n\x11custom_scale_name\x18\n \x01(\tB\x0c\n\nunits_enumB\x14\n\x12starting_edge_enum"0\n\x1eCreateCIPulseWidthChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x84\x02\n\x1dCreateCISemiPeriodChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07counter\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12)\n\x05units\x18\x06 \x01(\x0e2\x18.nidaqmx_grpc.TimeUnits3H\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12\x19\n\x11custom_scale_name\x18\x08 \x01(\tB\x0c\n\nunits_enum"0\n\x1eCreateCISemiPeriodChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb7\x03\n\x1dCreateCITwoEdgeSepChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07counter\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12)\n\x05units\x18\x06 \x01(\x0e2\x18.nidaqmx_grpc.TimeUnits3H\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12)\n\nfirst_edge\x18\x08 \x01(\x0e2\x13.nidaqmx_grpc.Edge1H\x01\x12\x18\n\x0efirst_edge_raw\x18\t \x01(\x05H\x01\x12*\n\x0bsecond_edge\x18\n \x01(\x0e2\x13.nidaqmx_grpc.Edge1H\x02\x12\x19\n\x0fsecond_edge_raw\x18\x0b \x01(\x05H\x02\x12\x19\n\x11custom_scale_name\x18\x0c \x01(\tB\x0c\n\nunits_enumB\x11\n\x0ffirst_edge_enumB\x12\n\x10second_edge_enum"0\n\x1eCreateCITwoEdgeSepChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xdd\x02\n\x1cCreateCOPulseChanFreqRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07counter\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12.\n\x05units\x18\x04 \x01(\x0e2\x1d.nidaqmx_grpc.FrequencyUnits2H\x00\x12\x13\n\tunits_raw\x18\x05 \x01(\x05H\x00\x12*\n\nidle_state\x18\x06 \x01(\x0e2\x14.nidaqmx_grpc.Level1H\x01\x12\x18\n\x0eidle_state_raw\x18\x07 \x01(\x05H\x01\x12\x15\n\rinitial_delay\x18\x08 \x01(\x01\x12\x0c\n\x04freq\x18\t \x01(\x01\x12\x12\n\nduty_cycle\x18\n \x01(\x01B\x0c\n\nunits_enumB\x11\n\x0fidle_state_enum"/\n\x1dCreateCOPulseChanFreqResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa9\x02\n\x1dCreateCOPulseChanTicksRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07counter\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x17\n\x0fsource_terminal\x18\x04 \x01(\t\x12*\n\nidle_state\x18\x05 \x01(\x0e2\x14.nidaqmx_grpc.Level1H\x00\x12\x18\n\x0eidle_state_raw\x18\x06 \x01(\x05H\x00\x12\x15\n\rinitial_delay\x18\x07 \x01(\x05\x12\x11\n\tlow_ticks\x18\x08 \x01(\x05\x12\x12\n\nhigh_ticks\x18\t \x01(\x05B\x11\n\x0fidle_state_enum"0\n\x1eCreateCOPulseChanTicksResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xe3\x02\n\x1cCreateCOPulseChanTimeRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07counter\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x121\n\x05units\x18\x04 \x01(\x0e2 .nidaqmx_grpc.DigitalWidthUnits3H\x00\x12\x13\n\tunits_raw\x18\x05 \x01(\x05H\x00\x12*\n\nidle_state\x18\x06 \x01(\x0e2\x14.nidaqmx_grpc.Level1H\x01\x12\x18\n\x0eidle_state_raw\x18\x07 \x01(\x05H\x01\x12\x15\n\rinitial_delay\x18\x08 \x01(\x01\x12\x10\n\x08low_time\x18\t \x01(\x01\x12\x11\n\thigh_time\x18\n \x01(\x01B\x0c\n\nunits_enumB\x11\n\x0fidle_state_enum"/\n\x1dCreateCOPulseChanTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd3\x01\n\x13CreateDIChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05lines\x18\x02 \x01(\t\x12\x1f\n\x17name_to_assign_to_lines\x18\x03 \x01(\t\x123\n\rline_grouping\x18\x04 \x01(\x0e2\x1a.nidaqmx_grpc.LineGroupingH\x00\x12\x1b\n\x11line_grouping_raw\x18\x05 \x01(\x05H\x00B\x14\n\x12line_grouping_enum"&\n\x14CreateDIChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd3\x01\n\x13CreateDOChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05lines\x18\x02 \x01(\t\x12\x1f\n\x17name_to_assign_to_lines\x18\x03 \x01(\t\x123\n\rline_grouping\x18\x04 \x01(\x0e2\x1a.nidaqmx_grpc.LineGroupingH\x00\x12\x1b\n\x11line_grouping_raw\x18\x05 \x01(\x05H\x00B\x14\n\x12line_grouping_enum"&\n\x14CreateDOChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd2\x01\n\x15CreateLinScaleRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05slope\x18\x02 \x01(\x01\x12\x13\n\x0by_intercept\x18\x03 \x01(\x01\x128\n\x10pre_scaled_units\x18\x04 \x01(\x0e2\x1c.nidaqmx_grpc.UnitsPreScaledH\x00\x12\x1e\n\x14pre_scaled_units_raw\x18\x05 \x01(\x05H\x00\x12\x14\n\x0cscaled_units\x18\x06 \x01(\tB\x17\n\x15pre_scaled_units_enum"(\n\x16CreateLinScaleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x84\x02\n\x15CreateMapScaleRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rprescaled_min\x18\x02 \x01(\x01\x12\x15\n\rprescaled_max\x18\x03 \x01(\x01\x12\x12\n\nscaled_min\x18\x04 \x01(\x01\x12\x12\n\nscaled_max\x18\x05 \x01(\x01\x128\n\x10pre_scaled_units\x18\x06 \x01(\x0e2\x1c.nidaqmx_grpc.UnitsPreScaledH\x00\x12\x1e\n\x14pre_scaled_units_raw\x18\x07 \x01(\x05H\x00\x12\x14\n\x0cscaled_units\x18\x08 \x01(\tB\x17\n\x15pre_scaled_units_enum"(\n\x16CreateMapScaleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xe5\x01\n\x1cCreatePolynomialScaleRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0eforward_coeffs\x18\x02 \x03(\x01\x12\x16\n\x0ereverse_coeffs\x18\x03 \x03(\x01\x128\n\x10pre_scaled_units\x18\x04 \x01(\x0e2\x1c.nidaqmx_grpc.UnitsPreScaledH\x00\x12\x1e\n\x14pre_scaled_units_raw\x18\x05 \x01(\x05H\x00\x12\x14\n\x0cscaled_units\x18\x06 \x01(\tB\x17\n\x15pre_scaled_units_enum"/\n\x1dCreatePolynomialScaleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa2\x04\n\x1cCreateTEDSAIAccelChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12@\n\x0fterminal_config\x18\x04 \x01(\x0e2%.nidaqmx_grpc.InputTermCfgWithDefaultH\x00\x12\x1d\n\x13terminal_config_raw\x18\x05 \x01(\x05H\x00\x12\x0f\n\x07min_val\x18\x06 \x01(\x01\x12\x0f\n\x07max_val\x18\x07 \x01(\x01\x12*\n\x05units\x18\x08 \x01(\x0e2\x19.nidaqmx_grpc.AccelUnits2H\x01\x12\x13\n\tunits_raw\x18\t \x01(\x05H\x01\x12>\n\x14current_excit_source\x18\n \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18current_excit_source_raw\x18\x0b \x01(\x05H\x02\x12\x19\n\x11current_excit_val\x18\x0c \x01(\x01\x12\x19\n\x11custom_scale_name\x18\r \x01(\tB\x16\n\x14terminal_config_enumB\x0c\n\nunits_enumB\x1b\n\x19current_excit_source_enum"/\n\x1dCreateTEDSAIAccelChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa8\x03\n\x1dCreateTEDSAIBridgeChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12(\n\x05units\x18\x06 \x01(\x0e2\x17.nidaqmx_grpc.TEDSUnitsH\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12>\n\x14voltage_excit_source\x18\x08 \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x01\x12"\n\x18voltage_excit_source_raw\x18\t \x01(\x05H\x01\x12\x19\n\x11voltage_excit_val\x18\n \x01(\x01\x12\x19\n\x11custom_scale_name\x18\x0b \x01(\tB\x0c\n\nunits_enumB\x1b\n\x19voltage_excit_source_enum"0\n\x1eCreateTEDSAIBridgeChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb8\x04\n\x1eCreateTEDSAICurrentChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12@\n\x0fterminal_config\x18\x04 \x01(\x0e2%.nidaqmx_grpc.InputTermCfgWithDefaultH\x00\x12\x1d\n\x13terminal_config_raw\x18\x05 \x01(\x05H\x00\x12\x0f\n\x07min_val\x18\x06 \x01(\x01\x12\x0f\n\x07max_val\x18\x07 \x01(\x01\x12(\n\x05units\x18\x08 \x01(\x0e2\x17.nidaqmx_grpc.TEDSUnitsH\x01\x12\x13\n\tunits_raw\x18\t \x01(\x05H\x01\x12S\n\x12shunt_resistor_loc\x18\n \x01(\x0e25.nidaqmx_grpc.CurrentShuntResistorLocationWithDefaultH\x02\x12 \n\x16shunt_resistor_loc_raw\x18\x0b \x01(\x05H\x02\x12\x1e\n\x16ext_shunt_resistor_val\x18\x0c \x01(\x01\x12\x19\n\x11custom_scale_name\x18\r \x01(\tB\x16\n\x14terminal_config_enumB\x0c\n\nunits_enumB\x19\n\x17shunt_resistor_loc_enum"1\n\x1fCreateTEDSAICurrentChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xae\x03\n"CreateTEDSAIForceBridgeChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12)\n\x05units\x18\x06 \x01(\x0e2\x18.nidaqmx_grpc.ForceUnitsH\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12>\n\x14voltage_excit_source\x18\x08 \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x01\x12"\n\x18voltage_excit_source_raw\x18\t \x01(\x05H\x01\x12\x19\n\x11voltage_excit_val\x18\n \x01(\x01\x12\x19\n\x11custom_scale_name\x18\x0b \x01(\tB\x0c\n\nunits_enumB\x1b\n\x19voltage_excit_source_enum"5\n#CreateTEDSAIForceBridgeChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa9\x04\n CreateTEDSAIForceIEPEChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12@\n\x0fterminal_config\x18\x04 \x01(\x0e2%.nidaqmx_grpc.InputTermCfgWithDefaultH\x00\x12\x1d\n\x13terminal_config_raw\x18\x05 \x01(\x05H\x00\x12\x0f\n\x07min_val\x18\x06 \x01(\x01\x12\x0f\n\x07max_val\x18\x07 \x01(\x01\x12-\n\x05units\x18\x08 \x01(\x0e2\x1c.nidaqmx_grpc.ForceIEPEUnitsH\x01\x12\x13\n\tunits_raw\x18\t \x01(\x05H\x01\x12>\n\x14current_excit_source\x18\n \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18current_excit_source_raw\x18\x0b \x01(\x05H\x02\x12\x19\n\x11current_excit_val\x18\x0c \x01(\x01\x12\x19\n\x11custom_scale_name\x18\r \x01(\tB\x16\n\x14terminal_config_enumB\x0c\n\nunits_enumB\x1b\n\x19current_excit_source_enum"3\n!CreateTEDSAIForceIEPEChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xaa\x04\n!CreateTEDSAIMicrophoneChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12@\n\x0fterminal_config\x18\x04 \x01(\x0e2%.nidaqmx_grpc.InputTermCfgWithDefaultH\x00\x12\x1d\n\x13terminal_config_raw\x18\x05 \x01(\x05H\x00\x122\n\x05units\x18\x06 \x01(\x0e2!.nidaqmx_grpc.SoundPressureUnits1H\x01\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x01\x12\x1b\n\x13max_snd_press_level\x18\x08 \x01(\x01\x12>\n\x14current_excit_source\x18\t \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18current_excit_source_raw\x18\n \x01(\x05H\x02\x12\x19\n\x11current_excit_val\x18\x0b \x01(\x01\x12\x19\n\x11custom_scale_name\x18\x0c \x01(\tB\x16\n\x14terminal_config_enumB\x0c\n\nunits_enumB\x1b\n\x19current_excit_source_enum"4\n"CreateTEDSAIMicrophoneChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc2\x04\n\x1eCreateTEDSAIPosLVDTChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12+\n\x05units\x18\x06 \x01(\x0e2\x1a.nidaqmx_grpc.LengthUnits2H\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12>\n\x14voltage_excit_source\x18\x08 \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x01\x12"\n\x18voltage_excit_source_raw\x18\t \x01(\x05H\x01\x12\x19\n\x11voltage_excit_val\x18\n \x01(\x01\x12\x1a\n\x12voltage_excit_freq\x18\x0b \x01(\x01\x12;\n\x12ac_excit_wire_mode\x18\x0c \x01(\x0e2\x1d.nidaqmx_grpc.ACExcitWireModeH\x02\x12 \n\x16ac_excit_wire_mode_raw\x18\r \x01(\x05H\x02\x12\x19\n\x11custom_scale_name\x18\x0e \x01(\tB\x0c\n\nunits_enumB\x1b\n\x19voltage_excit_source_enumB\x19\n\x17ac_excit_wire_mode_enum"1\n\x1fCreateTEDSAIPosLVDTChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc1\x04\n\x1eCreateTEDSAIPosRVDTChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12*\n\x05units\x18\x06 \x01(\x0e2\x19.nidaqmx_grpc.AngleUnits1H\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12>\n\x14voltage_excit_source\x18\x08 \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x01\x12"\n\x18voltage_excit_source_raw\x18\t \x01(\x05H\x01\x12\x19\n\x11voltage_excit_val\x18\n \x01(\x01\x12\x1a\n\x12voltage_excit_freq\x18\x0b \x01(\x01\x12;\n\x12ac_excit_wire_mode\x18\x0c \x01(\x0e2\x1d.nidaqmx_grpc.ACExcitWireModeH\x02\x12 \n\x16ac_excit_wire_mode_raw\x18\r \x01(\x05H\x02\x12\x19\n\x11custom_scale_name\x18\x0e \x01(\tB\x0c\n\nunits_enumB\x1b\n\x19voltage_excit_source_enumB\x19\n\x17ac_excit_wire_mode_enum"1\n\x1fCreateTEDSAIPosRVDTChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb4\x03\n%CreateTEDSAIPressureBridgeChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12,\n\x05units\x18\x06 \x01(\x0e2\x1b.nidaqmx_grpc.PressureUnitsH\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12>\n\x14voltage_excit_source\x18\x08 \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x01\x12"\n\x18voltage_excit_source_raw\x18\t \x01(\x05H\x01\x12\x19\n\x11voltage_excit_val\x18\n \x01(\x01\x12\x19\n\x11custom_scale_name\x18\x0b \x01(\tB\x0c\n\nunits_enumB\x1b\n\x19voltage_excit_source_enum"8\n&CreateTEDSAIPressureBridgeChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x90\x04\n\x1aCreateTEDSAIRTDChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12/\n\x05units\x18\x06 \x01(\x0e2\x1e.nidaqmx_grpc.TemperatureUnitsH\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12B\n\x11resistance_config\x18\x08 \x01(\x0e2%.nidaqmx_grpc.ResistanceConfigurationH\x01\x12\x1f\n\x15resistance_config_raw\x18\t \x01(\x05H\x01\x12>\n\x14current_excit_source\x18\n \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18current_excit_source_raw\x18\x0b \x01(\x05H\x02\x12\x19\n\x11current_excit_val\x18\x0c \x01(\x01B\x0c\n\nunits_enumB\x18\n\x16resistance_config_enumB\x1b\n\x19current_excit_source_enum"-\n\x1bCreateTEDSAIRTDChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xab\x04\n!CreateTEDSAIResistanceChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12(\n\x05units\x18\x06 \x01(\x0e2\x17.nidaqmx_grpc.TEDSUnitsH\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12B\n\x11resistance_config\x18\x08 \x01(\x0e2%.nidaqmx_grpc.ResistanceConfigurationH\x01\x12\x1f\n\x15resistance_config_raw\x18\t \x01(\x05H\x01\x12>\n\x14current_excit_source\x18\n \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18current_excit_source_raw\x18\x0b \x01(\x05H\x02\x12\x19\n\x11current_excit_val\x18\x0c \x01(\x01\x12\x19\n\x11custom_scale_name\x18\r \x01(\tB\x0c\n\nunits_enumB\x18\n\x16resistance_config_enumB\x1b\n\x19current_excit_source_enum"4\n"CreateTEDSAIResistanceChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xed\x03\n!CreateTEDSAIStrainGageChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12+\n\x05units\x18\x06 \x01(\x0e2\x1a.nidaqmx_grpc.StrainUnits1H\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12>\n\x14voltage_excit_source\x18\x08 \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x01\x12"\n\x18voltage_excit_source_raw\x18\t \x01(\x05H\x01\x12\x19\n\x11voltage_excit_val\x18\n \x01(\x01\x12\x1e\n\x16initial_bridge_voltage\x18\x0b \x01(\x01\x12\x1c\n\x14lead_wire_resistance\x18\x0c \x01(\x01\x12\x19\n\x11custom_scale_name\x18\r \x01(\tB\x0c\n\nunits_enumB\x1b\n\x19voltage_excit_source_enum"4\n"CreateTEDSAIStrainGageChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xfc\x02\n\x1eCreateTEDSAIThrmcplChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12/\n\x05units\x18\x06 \x01(\x0e2\x1e.nidaqmx_grpc.TemperatureUnitsH\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12.\n\ncjc_source\x18\x08 \x01(\x0e2\x18.nidaqmx_grpc.CJCSource1H\x01\x12\x18\n\x0ecjc_source_raw\x18\t \x01(\x05H\x01\x12\x0f\n\x07cjc_val\x18\n \x01(\x01\x12\x13\n\x0bcjc_channel\x18\x0b \x01(\tB\x0c\n\nunits_enumB\x11\n\x0fcjc_source_enum"1\n\x1fCreateTEDSAIThrmcplChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x97\x04\n!CreateTEDSAIThrmstrChanIexRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12/\n\x05units\x18\x06 \x01(\x0e2\x1e.nidaqmx_grpc.TemperatureUnitsH\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12B\n\x11resistance_config\x18\x08 \x01(\x0e2%.nidaqmx_grpc.ResistanceConfigurationH\x01\x12\x1f\n\x15resistance_config_raw\x18\t \x01(\x05H\x01\x12>\n\x14current_excit_source\x18\n \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18current_excit_source_raw\x18\x0b \x01(\x05H\x02\x12\x19\n\x11current_excit_val\x18\x0c \x01(\x01B\x0c\n\nunits_enumB\x18\n\x16resistance_config_enumB\x1b\n\x19current_excit_source_enum"4\n"CreateTEDSAIThrmstrChanIexResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa3\x04\n!CreateTEDSAIThrmstrChanVexRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12/\n\x05units\x18\x06 \x01(\x0e2\x1e.nidaqmx_grpc.TemperatureUnitsH\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12B\n\x11resistance_config\x18\x08 \x01(\x0e2%.nidaqmx_grpc.ResistanceConfigurationH\x01\x12\x1f\n\x15resistance_config_raw\x18\t \x01(\x05H\x01\x12>\n\x14voltage_excit_source\x18\n \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18voltage_excit_source_raw\x18\x0b \x01(\x05H\x02\x12\x19\n\x11voltage_excit_val\x18\x0c \x01(\x01\x12\n\n\x02r1\x18\r \x01(\x01B\x0c\n\nunits_enumB\x18\n\x16resistance_config_enumB\x1b\n\x19voltage_excit_source_enum"4\n"CreateTEDSAIThrmstrChanVexResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb0\x03\n#CreateTEDSAITorqueBridgeChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12\x0f\n\x07min_val\x18\x04 \x01(\x01\x12\x0f\n\x07max_val\x18\x05 \x01(\x01\x12*\n\x05units\x18\x06 \x01(\x0e2\x19.nidaqmx_grpc.TorqueUnitsH\x00\x12\x13\n\tunits_raw\x18\x07 \x01(\x05H\x00\x12>\n\x14voltage_excit_source\x18\x08 \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x01\x12"\n\x18voltage_excit_source_raw\x18\t \x01(\x05H\x01\x12\x19\n\x11voltage_excit_val\x18\n \x01(\x01\x12\x19\n\x11custom_scale_name\x18\x0b \x01(\tB\x0c\n\nunits_enumB\x1b\n\x19voltage_excit_source_enum"6\n$CreateTEDSAITorqueBridgeChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x86\x03\n\x1eCreateTEDSAIVoltageChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12@\n\x0fterminal_config\x18\x04 \x01(\x0e2%.nidaqmx_grpc.InputTermCfgWithDefaultH\x00\x12\x1d\n\x13terminal_config_raw\x18\x05 \x01(\x05H\x00\x12\x0f\n\x07min_val\x18\x06 \x01(\x01\x12\x0f\n\x07max_val\x18\x07 \x01(\x01\x12(\n\x05units\x18\x08 \x01(\x0e2\x17.nidaqmx_grpc.TEDSUnitsH\x01\x12\x13\n\tunits_raw\x18\t \x01(\x05H\x01\x12\x19\n\x11custom_scale_name\x18\n \x01(\tB\x16\n\x14terminal_config_enumB\x0c\n\nunits_enum"1\n\x1fCreateTEDSAIVoltageChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xab\x04\n\'CreateTEDSAIVoltageChanWithExcitRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10physical_channel\x18\x02 \x01(\t\x12!\n\x19name_to_assign_to_channel\x18\x03 \x01(\t\x12@\n\x0fterminal_config\x18\x04 \x01(\x0e2%.nidaqmx_grpc.InputTermCfgWithDefaultH\x00\x12\x1d\n\x13terminal_config_raw\x18\x05 \x01(\x05H\x00\x12\x0f\n\x07min_val\x18\x06 \x01(\x01\x12\x0f\n\x07max_val\x18\x07 \x01(\x01\x12(\n\x05units\x18\x08 \x01(\x0e2\x17.nidaqmx_grpc.TEDSUnitsH\x01\x12\x13\n\tunits_raw\x18\t \x01(\x05H\x01\x12>\n\x14voltage_excit_source\x18\n \x01(\x0e2\x1e.nidaqmx_grpc.ExcitationSourceH\x02\x12"\n\x18voltage_excit_source_raw\x18\x0b \x01(\x05H\x02\x12\x19\n\x11voltage_excit_val\x18\x0c \x01(\x01\x12\x19\n\x11custom_scale_name\x18\r \x01(\tB\x16\n\x14terminal_config_enumB\x0c\n\nunits_enumB\x1b\n\x19voltage_excit_source_enum":\n(CreateTEDSAIVoltageChanWithExcitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xdd\x01\n\x17CreateTableScaleRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0eprescaled_vals\x18\x02 \x03(\x01\x12\x13\n\x0bscaled_vals\x18\x03 \x03(\x01\x128\n\x10pre_scaled_units\x18\x04 \x01(\x0e2\x1c.nidaqmx_grpc.UnitsPreScaledH\x00\x12\x1e\n\x14pre_scaled_units_raw\x18\x05 \x01(\x05H\x00\x12\x14\n\x0cscaled_units\x18\x06 \x01(\tB\x17\n\x15pre_scaled_units_enum"*\n\x18CreateTableScaleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"x\n\x11CreateTaskRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12M\n\x17initialization_behavior\x18\x02 \x01(\x0e2,.nidevice_grpc.SessionInitializationBehavior"k\n\x12CreateTaskResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12$\n\x04task\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1f\n\x17new_session_initialized\x18\x03 \x01(\x08"\xea\x01\n\x1eCreateWatchdogTimerTaskRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x12\x14\n\x0csession_name\x18\x02 \x01(\t\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12=\n\nexp_states\x18\x04 \x03(\x0b2).nidaqmx_grpc.WatchdogExpChannelsAndState\x12M\n\x17initialization_behavior\x18\x05 \x01(\x0e2,.nidevice_grpc.SessionInitializationBehavior"x\n\x1fCreateWatchdogTimerTaskResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12$\n\x04task\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1f\n\x17new_session_initialized\x18\x03 \x01(\x08"\xad\x01\n CreateWatchdogTimerTaskExRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x12\x14\n\x0csession_name\x18\x02 \x01(\t\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12M\n\x17initialization_behavior\x18\x04 \x01(\x0e2,.nidevice_grpc.SessionInitializationBehavior"z\n!CreateWatchdogTimerTaskExResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12$\n\x04task\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1f\n\x17new_session_initialized\x18\x03 \x01(\x08"1\n\x1aDeleteNetworkDeviceRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t"-\n\x1bDeleteNetworkDeviceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"4\n\x1cDeleteSavedGlobalChanRequest\x12\x14\n\x0cchannel_name\x18\x01 \x01(\t"/\n\x1dDeleteSavedGlobalChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"-\n\x17DeleteSavedScaleRequest\x12\x12\n\nscale_name\x18\x01 \x01(\t"*\n\x18DeleteSavedScaleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"+\n\x16DeleteSavedTaskRequest\x12\x11\n\ttask_name\x18\x01 \x01(\t")\n\x17DeleteSavedTaskResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"/\n\x18DeviceSupportsCalRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t"B\n\x19DeviceSupportsCalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rcal_supported\x18\x02 \x01(\x08"=\n\x15DisableRefTrigRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"(\n\x16DisableRefTrigResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"?\n\x17DisableStartTrigRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"*\n\x18DisableStartTrigResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"O\n\x16DisconnectTermsRequest\x12\x17\n\x0fsource_terminal\x18\x01 \x01(\t\x12\x1c\n\x14destination_terminal\x18\x02 \x01(\t")\n\x17DisconnectTermsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xaa\x01\n\x13ExportSignalRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12)\n\tsignal_id\x18\x02 \x01(\x0e2\x14.nidaqmx_grpc.SignalH\x00\x12\x17\n\rsignal_id_raw\x18\x03 \x01(\x05H\x00\x12\x17\n\x0foutput_terminal\x18\x04 \x01(\tB\x10\n\x0esignal_id_enum"&\n\x14ExportSignalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"X\n\x1aGetAIChanCalCalDateRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"u\n\x1bGetAIChanCalCalDateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04year\x18\x02 \x01(\r\x12\r\n\x05month\x18\x03 \x01(\r\x12\x0b\n\x03day\x18\x04 \x01(\r\x12\x0c\n\x04hour\x18\x05 \x01(\r\x12\x0e\n\x06minute\x18\x06 \x01(\r"X\n\x1aGetAIChanCalExpDateRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"u\n\x1bGetAIChanCalExpDateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04year\x18\x02 \x01(\r\x12\r\n\x05month\x18\x03 \x01(\r\x12\x0b\n\x03day\x18\x04 \x01(\r\x12\x0c\n\x04hour\x18\x05 \x01(\r\x12\x0e\n\x06minute\x18\x06 \x01(\r"q\n\x1dGetAnalogPowerUpStatesRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x12;\n\x08channels\x18\x02 \x03(\x0b2).nidaqmx_grpc.AnalogPowerUpChannelAndType"I\n\x1eGetAnalogPowerUpStatesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fpower_up_states\x18\x02 \x03(\x01"X\n+GetAnalogPowerUpStatesWithOutputTypeRequest\x12\x15\n\rchannel_names\x18\x01 \x01(\t\x12\x12\n\narray_size\x18\x02 \x01(\r"\xb1\x01\n,GetAnalogPowerUpStatesWithOutputTypeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0bstate_array\x18\x02 \x03(\x01\x12<\n\x12channel_type_array\x18\x03 \x03(\x0e2 .nidaqmx_grpc.PowerUpChannelType\x12\x1e\n\x16channel_type_array_raw\x18\x04 \x03(\x05"J\n"GetArmStartTrigTimestampValRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"_\n#GetArmStartTrigTimestampValResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12(\n\x04data\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"F\n\x1eGetArmStartTrigTrigWhenRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"[\n\x1fGetArmStartTrigTrigWhenResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12(\n\x04data\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"-\n+GetAutoConfiguredCDAQSyncConnectionsRequest"Q\n,GetAutoConfiguredCDAQSyncConnectionsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\tport_list\x18\x02 \x01(\t"\xac\x01\n\x1fGetBufferAttributeUInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x128\n\tattribute\x18\x02 \x01(\x0e2#.nidaqmx_grpc.BufferUInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"A\n GetBufferAttributeUInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\r"\xa1\x01\n\x1eGetCalInfoAttributeBoolRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x12?\n\tattribute\x18\x02 \x01(\x0e2*.nidaqmx_grpc.CalibrationInfoBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"@\n\x1fGetCalInfoAttributeBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08"\xa5\x01\n GetCalInfoAttributeDoubleRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x12A\n\tattribute\x18\x02 \x01(\x0e2,.nidaqmx_grpc.CalibrationInfoDoubleAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"B\n!GetCalInfoAttributeDoubleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01"\xa5\x01\n GetCalInfoAttributeStringRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x12A\n\tattribute\x18\x02 \x01(\x0e2,.nidaqmx_grpc.CalibrationInfoStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"B\n!GetCalInfoAttributeStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t"\xa5\x01\n GetCalInfoAttributeUInt32Request\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x12A\n\tattribute\x18\x02 \x01(\x0e2,.nidaqmx_grpc.CalibrationInfoUInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"B\n!GetCalInfoAttributeUInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\r"\xb8\x01\n\x1bGetChanAttributeBoolRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07channel\x18\x02 \x01(\t\x127\n\tattribute\x18\x03 \x01(\x0e2".nidaqmx_grpc.ChannelBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00B\x10\n\x0eattribute_enum"=\n\x1cGetChanAttributeBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08"\xbc\x01\n\x1dGetChanAttributeDoubleRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07channel\x18\x02 \x01(\t\x129\n\tattribute\x18\x03 \x01(\x0e2$.nidaqmx_grpc.ChannelDoubleAttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00B\x10\n\x0eattribute_enum"?\n\x1eGetChanAttributeDoubleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01"\xc6\x01\n"GetChanAttributeDoubleArrayRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07channel\x18\x02 \x01(\t\x12>\n\tattribute\x18\x03 \x01(\x0e2).nidaqmx_grpc.ChannelDoubleArrayAttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00B\x10\n\x0eattribute_enum"D\n#GetChanAttributeDoubleArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x03(\x01"\xba\x01\n\x1cGetChanAttributeInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07channel\x18\x02 \x01(\t\x128\n\tattribute\x18\x03 \x01(\x0e2#.nidaqmx_grpc.ChannelInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00B\x10\n\x0eattribute_enum"|\n\x1dGetChanAttributeInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x128\n\x05value\x18\x02 \x01(\x0e2).nidaqmx_grpc.ChannelInt32AttributeValues\x12\x11\n\tvalue_raw\x18\x03 \x01(\x05"\xbc\x01\n\x1dGetChanAttributeStringRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07channel\x18\x02 \x01(\t\x129\n\tattribute\x18\x03 \x01(\x0e2$.nidaqmx_grpc.ChannelStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00B\x10\n\x0eattribute_enum"?\n\x1eGetChanAttributeStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t"\xbc\x01\n\x1dGetChanAttributeUInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07channel\x18\x02 \x01(\t\x129\n\tattribute\x18\x03 \x01(\x0e2$.nidaqmx_grpc.ChannelUInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00B\x10\n\x0eattribute_enum"?\n\x1eGetChanAttributeUInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\r"\x97\x01\n\x1dGetDeviceAttributeBoolRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x126\n\tattribute\x18\x02 \x01(\x0e2!.nidaqmx_grpc.DeviceBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"?\n\x1eGetDeviceAttributeBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08"\x9b\x01\n\x1fGetDeviceAttributeDoubleRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x128\n\tattribute\x18\x02 \x01(\x0e2#.nidaqmx_grpc.DeviceDoubleAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"A\n GetDeviceAttributeDoubleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01"\xa5\x01\n$GetDeviceAttributeDoubleArrayRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x12=\n\tattribute\x18\x02 \x01(\x0e2(.nidaqmx_grpc.DeviceDoubleArrayAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"F\n%GetDeviceAttributeDoubleArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x03(\x01"\x99\x01\n\x1eGetDeviceAttributeInt32Request\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x127\n\tattribute\x18\x02 \x01(\x0e2".nidaqmx_grpc.DeviceInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"}\n\x1fGetDeviceAttributeInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x127\n\x05value\x18\x02 \x01(\x0e2(.nidaqmx_grpc.DeviceInt32AttributeValues\x12\x11\n\tvalue_raw\x18\x03 \x01(\x05"\xa3\x01\n#GetDeviceAttributeInt32ArrayRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x12<\n\tattribute\x18\x02 \x01(\x0e2\'.nidaqmx_grpc.DeviceInt32ArrayAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"\x82\x01\n$GetDeviceAttributeInt32ArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x127\n\x05value\x18\x02 \x03(\x0e2(.nidaqmx_grpc.DeviceInt32AttributeValues\x12\x11\n\tvalue_raw\x18\x03 \x03(\x05"\x9b\x01\n\x1fGetDeviceAttributeStringRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x128\n\tattribute\x18\x02 \x01(\x0e2#.nidaqmx_grpc.DeviceStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"A\n GetDeviceAttributeStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t"\x9b\x01\n\x1fGetDeviceAttributeUInt32Request\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x128\n\tattribute\x18\x02 \x01(\x0e2#.nidaqmx_grpc.DeviceUInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"A\n GetDeviceAttributeUInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\r"\xa5\x01\n$GetDeviceAttributeUInt32ArrayRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x12=\n\tattribute\x18\x02 \x01(\x0e2(.nidaqmx_grpc.DeviceUInt32ArrayAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"F\n%GetDeviceAttributeUInt32ArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x03(\r"?\n(GetDigitalLogicFamilyPowerUpStateRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t"Q\n)GetDigitalLogicFamilyPowerUpStateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x14\n\x0clogic_family\x18\x02 \x01(\x05"K\n\x1eGetDigitalPowerUpStatesRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x12\x14\n\x0cchannel_name\x18\x02 \x03(\t"g\n\x1fGetDigitalPowerUpStatesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x124\n\x0fpower_up_states\x18\x02 \x03(\x0e2\x1b.nidaqmx_grpc.PowerUpStates"R\n%GetDigitalPullUpPullDownStatesRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x12\x14\n\x0cchannel_name\x18\x02 \x03(\t"w\n&GetDigitalPullUpPullDownStatesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12=\n\x18pull_up_pull_down_states\x18\x02 \x03(\x0e2\x1b.nidaqmx_grpc.ResistorState"%\n#GetDisconnectedCDAQSyncPortsRequest"I\n$GetDisconnectedCDAQSyncPortsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\tport_list\x18\x02 \x01(\t"+\n\x15GetErrorStringRequest\x12\x12\n\nerror_code\x18\x01 \x01(\x05">\n\x16GetErrorStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x14\n\x0cerror_string\x18\x02 \x01(\t"\xb6\x01\n%GetExportedSignalAttributeBoolRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12<\n\tattribute\x18\x02 \x01(\x0e2\'.nidaqmx_grpc.ExportSignalBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"G\n&GetExportedSignalAttributeBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08"\xba\x01\n\'GetExportedSignalAttributeDoubleRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12>\n\tattribute\x18\x02 \x01(\x0e2).nidaqmx_grpc.ExportSignalDoubleAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"I\n(GetExportedSignalAttributeDoubleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01"\xb8\x01\n&GetExportedSignalAttributeInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12=\n\tattribute\x18\x02 \x01(\x0e2(.nidaqmx_grpc.ExportSignalInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"\x8b\x01\n\'GetExportedSignalAttributeInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12=\n\x05value\x18\x02 \x01(\x0e2..nidaqmx_grpc.ExportSignalInt32AttributeValues\x12\x11\n\tvalue_raw\x18\x03 \x01(\x05"\xba\x01\n\'GetExportedSignalAttributeStringRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12>\n\tattribute\x18\x02 \x01(\x0e2).nidaqmx_grpc.ExportSignalStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"I\n(GetExportedSignalAttributeStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t"\xba\x01\n\'GetExportedSignalAttributeUInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12>\n\tattribute\x18\x02 \x01(\x0e2).nidaqmx_grpc.ExportSignalUInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"I\n(GetExportedSignalAttributeUInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\r"6\n\x1fGetExtCalLastDateAndTimeRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t"z\n GetExtCalLastDateAndTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04year\x18\x02 \x01(\r\x12\r\n\x05month\x18\x03 \x01(\r\x12\x0b\n\x03day\x18\x04 \x01(\r\x12\x0c\n\x04hour\x18\x05 \x01(\r\x12\x0e\n\x06minute\x18\x06 \x01(\r"B\n\x1aGetFirstSampClkWhenRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"W\n\x1bGetFirstSampClkWhenResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12(\n\x04data\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"G\n\x1fGetFirstSampTimestampValRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\\\n GetFirstSampTimestampValResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12(\n\x04data\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"O\n\x18GetNthTaskChannelRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05index\x18\x02 \x01(\r";\n\x19GetNthTaskChannelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06buffer\x18\x02 \x01(\t"N\n\x17GetNthTaskDeviceRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05index\x18\x02 \x01(\r":\n\x18GetNthTaskDeviceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06buffer\x18\x02 \x01(\t"S\n\x1cGetNthTaskReadChannelRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05index\x18\x02 \x01(\r"?\n\x1dGetNthTaskReadChannelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06buffer\x18\x02 \x01(\t"\xa4\x01\n$GetPersistedChanAttributeBoolRequest\x12\x0f\n\x07channel\x18\x01 \x01(\t\x12@\n\tattribute\x18\x02 \x01(\x0e2+.nidaqmx_grpc.PersistedChannelBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"F\n%GetPersistedChanAttributeBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08"\xa8\x01\n&GetPersistedChanAttributeStringRequest\x12\x0f\n\x07channel\x18\x01 \x01(\t\x12B\n\tattribute\x18\x02 \x01(\x0e2-.nidaqmx_grpc.PersistedChannelStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"H\n\'GetPersistedChanAttributeStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t"\xa6\x01\n%GetPersistedScaleAttributeBoolRequest\x12\x12\n\nscale_name\x18\x01 \x01(\t\x12>\n\tattribute\x18\x02 \x01(\x0e2).nidaqmx_grpc.PersistedScaleBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"G\n&GetPersistedScaleAttributeBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08"\xaa\x01\n\'GetPersistedScaleAttributeStringRequest\x12\x12\n\nscale_name\x18\x01 \x01(\t\x12@\n\tattribute\x18\x02 \x01(\x0e2+.nidaqmx_grpc.PersistedScaleStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"I\n(GetPersistedScaleAttributeStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t"\xa3\x01\n$GetPersistedTaskAttributeBoolRequest\x12\x11\n\ttask_name\x18\x01 \x01(\t\x12=\n\tattribute\x18\x02 \x01(\x0e2(.nidaqmx_grpc.PersistedTaskBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"F\n%GetPersistedTaskAttributeBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08"\xa7\x01\n&GetPersistedTaskAttributeStringRequest\x12\x11\n\ttask_name\x18\x01 \x01(\t\x12?\n\tattribute\x18\x02 \x01(\x0e2*.nidaqmx_grpc.PersistedTaskStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"H\n\'GetPersistedTaskAttributeStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t"\xab\x01\n#GetPhysicalChanAttributeBoolRequest\x12\x18\n\x10physical_channel\x18\x01 \x01(\t\x12?\n\tattribute\x18\x02 \x01(\x0e2*.nidaqmx_grpc.PhysicalChannelBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"E\n$GetPhysicalChanAttributeBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08"\xad\x01\n$GetPhysicalChanAttributeBytesRequest\x12\x18\n\x10physical_channel\x18\x01 \x01(\t\x12@\n\tattribute\x18\x02 \x01(\x0e2+.nidaqmx_grpc.PhysicalChannelBytesAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"F\n%GetPhysicalChanAttributeBytesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x0c"\xaf\x01\n%GetPhysicalChanAttributeDoubleRequest\x12\x18\n\x10physical_channel\x18\x01 \x01(\t\x12A\n\tattribute\x18\x02 \x01(\x0e2,.nidaqmx_grpc.PhysicalChannelDoubleAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"G\n&GetPhysicalChanAttributeDoubleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01"\xb9\x01\n*GetPhysicalChanAttributeDoubleArrayRequest\x12\x18\n\x10physical_channel\x18\x01 \x01(\t\x12F\n\tattribute\x18\x02 \x01(\x0e21.nidaqmx_grpc.PhysicalChannelDoubleArrayAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"L\n+GetPhysicalChanAttributeDoubleArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x03(\x01"\xad\x01\n$GetPhysicalChanAttributeInt32Request\x12\x18\n\x10physical_channel\x18\x01 \x01(\t\x12@\n\tattribute\x18\x02 \x01(\x0e2+.nidaqmx_grpc.PhysicalChannelInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"\x8c\x01\n%GetPhysicalChanAttributeInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12@\n\x05value\x18\x02 \x01(\x0e21.nidaqmx_grpc.PhysicalChannelInt32AttributeValues\x12\x11\n\tvalue_raw\x18\x03 \x01(\x05"\xb7\x01\n)GetPhysicalChanAttributeInt32ArrayRequest\x12\x18\n\x10physical_channel\x18\x01 \x01(\t\x12E\n\tattribute\x18\x02 \x01(\x0e20.nidaqmx_grpc.PhysicalChannelInt32ArrayAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"\x91\x01\n*GetPhysicalChanAttributeInt32ArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12@\n\x05value\x18\x02 \x03(\x0e21.nidaqmx_grpc.PhysicalChannelInt32AttributeValues\x12\x11\n\tvalue_raw\x18\x03 \x03(\x05"\xaf\x01\n%GetPhysicalChanAttributeStringRequest\x12\x18\n\x10physical_channel\x18\x01 \x01(\t\x12A\n\tattribute\x18\x02 \x01(\x0e2,.nidaqmx_grpc.PhysicalChannelStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"G\n&GetPhysicalChanAttributeStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t"\xaf\x01\n%GetPhysicalChanAttributeUInt32Request\x12\x18\n\x10physical_channel\x18\x01 \x01(\t\x12A\n\tattribute\x18\x02 \x01(\x0e2,.nidaqmx_grpc.PhysicalChannelUInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"G\n&GetPhysicalChanAttributeUInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\r"\xb9\x01\n*GetPhysicalChanAttributeUInt32ArrayRequest\x12\x18\n\x10physical_channel\x18\x01 \x01(\t\x12F\n\tattribute\x18\x02 \x01(\x0e21.nidaqmx_grpc.PhysicalChannelUInt32ArrayAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"L\n+GetPhysicalChanAttributeUInt32ArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x03(\r"\xa4\x01\n\x1bGetReadAttributeBoolRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x124\n\tattribute\x18\x02 \x01(\x0e2\x1f.nidaqmx_grpc.ReadBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"=\n\x1cGetReadAttributeBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08"\xa8\x01\n\x1dGetReadAttributeDoubleRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x126\n\tattribute\x18\x02 \x01(\x0e2!.nidaqmx_grpc.ReadDoubleAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"?\n\x1eGetReadAttributeDoubleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01"\xa6\x01\n\x1cGetReadAttributeInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x125\n\tattribute\x18\x02 \x01(\x0e2 .nidaqmx_grpc.ReadInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"y\n\x1dGetReadAttributeInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x125\n\x05value\x18\x02 \x01(\x0e2&.nidaqmx_grpc.ReadInt32AttributeValues\x12\x11\n\tvalue_raw\x18\x03 \x01(\x05"\xa8\x01\n\x1dGetReadAttributeStringRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x126\n\tattribute\x18\x02 \x01(\x0e2!.nidaqmx_grpc.ReadStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"?\n\x1eGetReadAttributeStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t"\xa8\x01\n\x1dGetReadAttributeUInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x126\n\tattribute\x18\x02 \x01(\x0e2!.nidaqmx_grpc.ReadUInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"?\n\x1eGetReadAttributeUInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\r"\xa8\x01\n\x1dGetReadAttributeUInt64Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x126\n\tattribute\x18\x02 \x01(\x0e2!.nidaqmx_grpc.ReadUInt64AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"?\n\x1eGetReadAttributeUInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x04"\xac\x01\n\x1fGetRealTimeAttributeBoolRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x128\n\tattribute\x18\x02 \x01(\x0e2#.nidaqmx_grpc.RealTimeBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"A\n GetRealTimeAttributeBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08"\xae\x01\n GetRealTimeAttributeInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x129\n\tattribute\x18\x02 \x01(\x0e2$.nidaqmx_grpc.RealTimeInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"\x81\x01\n!GetRealTimeAttributeInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x129\n\x05value\x18\x02 \x01(\x0e2*.nidaqmx_grpc.RealTimeInt32AttributeValues\x12\x11\n\tvalue_raw\x18\x03 \x01(\x05"\xb0\x01\n!GetRealTimeAttributeUInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12:\n\tattribute\x18\x02 \x01(\x0e2%.nidaqmx_grpc.RealTimeUInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"C\n"GetRealTimeAttributeUInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\r"E\n\x1dGetRefTrigTimestampValRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"Z\n\x1eGetRefTrigTimestampValResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12(\n\x04data\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x98\x01\n\x1eGetScaleAttributeDoubleRequest\x12\x12\n\nscale_name\x18\x01 \x01(\t\x127\n\tattribute\x18\x02 \x01(\x0e2".nidaqmx_grpc.ScaleDoubleAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"@\n\x1fGetScaleAttributeDoubleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01"\xa2\x01\n#GetScaleAttributeDoubleArrayRequest\x12\x12\n\nscale_name\x18\x01 \x01(\t\x12<\n\tattribute\x18\x02 \x01(\x0e2\'.nidaqmx_grpc.ScaleDoubleArrayAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"E\n$GetScaleAttributeDoubleArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x03(\x01"\x96\x01\n\x1dGetScaleAttributeInt32Request\x12\x12\n\nscale_name\x18\x01 \x01(\t\x126\n\tattribute\x18\x02 \x01(\x0e2!.nidaqmx_grpc.ScaleInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"{\n\x1eGetScaleAttributeInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x126\n\x05value\x18\x02 \x01(\x0e2\'.nidaqmx_grpc.ScaleInt32AttributeValues\x12\x11\n\tvalue_raw\x18\x03 \x01(\x05"\x98\x01\n\x1eGetScaleAttributeStringRequest\x12\x12\n\nscale_name\x18\x01 \x01(\t\x127\n\tattribute\x18\x02 \x01(\x0e2".nidaqmx_grpc.ScaleStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"@\n\x1fGetScaleAttributeStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t"7\n GetSelfCalLastDateAndTimeRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t"{\n!GetSelfCalLastDateAndTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04year\x18\x02 \x01(\r\x12\r\n\x05month\x18\x03 \x01(\r\x12\x0b\n\x03day\x18\x04 \x01(\r\x12\x0c\n\x04hour\x18\x05 \x01(\r\x12\x0e\n\x06minute\x18\x06 \x01(\r"G\n\x1fGetStartTrigTimestampValRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\\\n GetStartTrigTimestampValResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12(\n\x04data\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"C\n\x1bGetStartTrigTrigWhenRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"X\n\x1cGetStartTrigTrigWhenResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12(\n\x04data\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"C\n\x1bGetSyncPulseTimeWhenRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"X\n\x1cGetSyncPulseTimeWhenResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12(\n\x04data\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x8a\x01\n#GetSystemInfoAttributeStringRequest\x128\n\tattribute\x18\x01 \x01(\x0e2#.nidaqmx_grpc.SystemStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x02 \x01(\x05H\x00B\x10\n\x0eattribute_enum"E\n$GetSystemInfoAttributeStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t"\x8a\x01\n#GetSystemInfoAttributeUInt32Request\x128\n\tattribute\x18\x01 \x01(\x0e2#.nidaqmx_grpc.SystemUInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x02 \x01(\x05H\x00B\x10\n\x0eattribute_enum"E\n$GetSystemInfoAttributeUInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\r"\xa4\x01\n\x1bGetTaskAttributeBoolRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x124\n\tattribute\x18\x02 \x01(\x0e2\x1f.nidaqmx_grpc.TaskBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"=\n\x1cGetTaskAttributeBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08"\xa8\x01\n\x1dGetTaskAttributeStringRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x126\n\tattribute\x18\x02 \x01(\x0e2!.nidaqmx_grpc.TaskStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"?\n\x1eGetTaskAttributeStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t"\xa8\x01\n\x1dGetTaskAttributeUInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x126\n\tattribute\x18\x02 \x01(\x0e2!.nidaqmx_grpc.TaskUInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"?\n\x1eGetTaskAttributeUInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\r"\xa8\x01\n\x1dGetTimingAttributeBoolRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x126\n\tattribute\x18\x02 \x01(\x0e2!.nidaqmx_grpc.TimingBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"?\n\x1eGetTimingAttributeBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08"\xac\x01\n\x1fGetTimingAttributeDoubleRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x128\n\tattribute\x18\x02 \x01(\x0e2#.nidaqmx_grpc.TimingDoubleAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"A\n GetTimingAttributeDoubleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01"\xc0\x01\n\x1fGetTimingAttributeExBoolRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cdevice_names\x18\x02 \x01(\t\x126\n\tattribute\x18\x03 \x01(\x0e2!.nidaqmx_grpc.TimingBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00B\x10\n\x0eattribute_enum"A\n GetTimingAttributeExBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08"\xc4\x01\n!GetTimingAttributeExDoubleRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cdevice_names\x18\x02 \x01(\t\x128\n\tattribute\x18\x03 \x01(\x0e2#.nidaqmx_grpc.TimingDoubleAttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00B\x10\n\x0eattribute_enum"C\n"GetTimingAttributeExDoubleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01"\xc2\x01\n GetTimingAttributeExInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cdevice_names\x18\x02 \x01(\t\x127\n\tattribute\x18\x03 \x01(\x0e2".nidaqmx_grpc.TimingInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00B\x10\n\x0eattribute_enum"\x7f\n!GetTimingAttributeExInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x127\n\x05value\x18\x02 \x01(\x0e2(.nidaqmx_grpc.TimingInt32AttributeValues\x12\x11\n\tvalue_raw\x18\x03 \x01(\x05"\xc4\x01\n!GetTimingAttributeExStringRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cdevice_names\x18\x02 \x01(\t\x128\n\tattribute\x18\x03 \x01(\x0e2#.nidaqmx_grpc.TimingStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00B\x10\n\x0eattribute_enum"C\n"GetTimingAttributeExStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t"\xca\x01\n$GetTimingAttributeExTimestampRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cdevice_names\x18\x02 \x01(\t\x12;\n\tattribute\x18\x03 \x01(\x0e2&.nidaqmx_grpc.TimingTimestampAttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00B\x10\n\x0eattribute_enum"b\n%GetTimingAttributeExTimestampResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12)\n\x05value\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xc4\x01\n!GetTimingAttributeExUInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cdevice_names\x18\x02 \x01(\t\x128\n\tattribute\x18\x03 \x01(\x0e2#.nidaqmx_grpc.TimingUInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00B\x10\n\x0eattribute_enum"C\n"GetTimingAttributeExUInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\r"\xc4\x01\n!GetTimingAttributeExUInt64Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cdevice_names\x18\x02 \x01(\t\x128\n\tattribute\x18\x03 \x01(\x0e2#.nidaqmx_grpc.TimingUInt64AttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00B\x10\n\x0eattribute_enum"C\n"GetTimingAttributeExUInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x04"\xaa\x01\n\x1eGetTimingAttributeInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x127\n\tattribute\x18\x02 \x01(\x0e2".nidaqmx_grpc.TimingInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"}\n\x1fGetTimingAttributeInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x127\n\x05value\x18\x02 \x01(\x0e2(.nidaqmx_grpc.TimingInt32AttributeValues\x12\x11\n\tvalue_raw\x18\x03 \x01(\x05"\xac\x01\n\x1fGetTimingAttributeStringRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x128\n\tattribute\x18\x02 \x01(\x0e2#.nidaqmx_grpc.TimingStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"A\n GetTimingAttributeStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t"\xb2\x01\n"GetTimingAttributeTimestampRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12;\n\tattribute\x18\x02 \x01(\x0e2&.nidaqmx_grpc.TimingTimestampAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"`\n#GetTimingAttributeTimestampResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12)\n\x05value\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xac\x01\n\x1fGetTimingAttributeUInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x128\n\tattribute\x18\x02 \x01(\x0e2#.nidaqmx_grpc.TimingUInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"A\n GetTimingAttributeUInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\r"\xac\x01\n\x1fGetTimingAttributeUInt64Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x128\n\tattribute\x18\x02 \x01(\x0e2#.nidaqmx_grpc.TimingUInt64AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"A\n GetTimingAttributeUInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x04"\xa7\x01\n\x1bGetTrigAttributeBoolRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x127\n\tattribute\x18\x02 \x01(\x0e2".nidaqmx_grpc.TriggerBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"=\n\x1cGetTrigAttributeBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08"\xab\x01\n\x1dGetTrigAttributeDoubleRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x129\n\tattribute\x18\x02 \x01(\x0e2$.nidaqmx_grpc.TriggerDoubleAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"?\n\x1eGetTrigAttributeDoubleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01"\xb5\x01\n"GetTrigAttributeDoubleArrayRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12>\n\tattribute\x18\x02 \x01(\x0e2).nidaqmx_grpc.TriggerDoubleArrayAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"D\n#GetTrigAttributeDoubleArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x03(\x01"\xa9\x01\n\x1cGetTrigAttributeInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x128\n\tattribute\x18\x02 \x01(\x0e2#.nidaqmx_grpc.TriggerInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"|\n\x1dGetTrigAttributeInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x128\n\x05value\x18\x02 \x01(\x0e2).nidaqmx_grpc.TriggerInt32AttributeValues\x12\x11\n\tvalue_raw\x18\x03 \x01(\x05"\xb3\x01\n!GetTrigAttributeInt32ArrayRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12=\n\tattribute\x18\x02 \x01(\x0e2(.nidaqmx_grpc.TriggerInt32ArrayAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"\x81\x01\n"GetTrigAttributeInt32ArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x128\n\x05value\x18\x02 \x03(\x0e2).nidaqmx_grpc.TriggerInt32AttributeValues\x12\x11\n\tvalue_raw\x18\x03 \x03(\x05"\xab\x01\n\x1dGetTrigAttributeStringRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x129\n\tattribute\x18\x02 \x01(\x0e2$.nidaqmx_grpc.TriggerStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"?\n\x1eGetTrigAttributeStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t"\xb1\x01\n GetTrigAttributeTimestampRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12<\n\tattribute\x18\x02 \x01(\x0e2\'.nidaqmx_grpc.TriggerTimestampAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"^\n!GetTrigAttributeTimestampResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12)\n\x05value\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xab\x01\n\x1dGetTrigAttributeUInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x129\n\tattribute\x18\x02 \x01(\x0e2$.nidaqmx_grpc.TriggerUInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"?\n\x1eGetTrigAttributeUInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\r"\xbb\x01\n\x1fGetWatchdogAttributeBoolRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05lines\x18\x02 \x01(\t\x128\n\tattribute\x18\x03 \x01(\x0e2#.nidaqmx_grpc.WatchdogBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00B\x10\n\x0eattribute_enum"A\n GetWatchdogAttributeBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08"\xbf\x01\n!GetWatchdogAttributeDoubleRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05lines\x18\x02 \x01(\t\x12:\n\tattribute\x18\x03 \x01(\x0e2%.nidaqmx_grpc.WatchdogDoubleAttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00B\x10\n\x0eattribute_enum"C\n"GetWatchdogAttributeDoubleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01"\xbd\x01\n GetWatchdogAttributeInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05lines\x18\x02 \x01(\t\x129\n\tattribute\x18\x03 \x01(\x0e2$.nidaqmx_grpc.WatchdogInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00B\x10\n\x0eattribute_enum"\x81\x01\n!GetWatchdogAttributeInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x129\n\x05value\x18\x02 \x01(\x0e2*.nidaqmx_grpc.WatchdogInt32AttributeValues\x12\x11\n\tvalue_raw\x18\x03 \x01(\x05"\xbf\x01\n!GetWatchdogAttributeStringRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05lines\x18\x02 \x01(\t\x12:\n\tattribute\x18\x03 \x01(\x0e2%.nidaqmx_grpc.WatchdogStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00B\x10\n\x0eattribute_enum"C\n"GetWatchdogAttributeStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t"\xa6\x01\n\x1cGetWriteAttributeBoolRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x125\n\tattribute\x18\x02 \x01(\x0e2 .nidaqmx_grpc.WriteBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum">\n\x1dGetWriteAttributeBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08"\xaa\x01\n\x1eGetWriteAttributeDoubleRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x127\n\tattribute\x18\x02 \x01(\x0e2".nidaqmx_grpc.WriteDoubleAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"@\n\x1fGetWriteAttributeDoubleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01"\xa8\x01\n\x1dGetWriteAttributeInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x126\n\tattribute\x18\x02 \x01(\x0e2!.nidaqmx_grpc.WriteInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"{\n\x1eGetWriteAttributeInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x126\n\x05value\x18\x02 \x01(\x0e2\'.nidaqmx_grpc.WriteInt32AttributeValues\x12\x11\n\tvalue_raw\x18\x03 \x01(\x05"\xaa\x01\n\x1eGetWriteAttributeStringRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x127\n\tattribute\x18\x02 \x01(\x0e2".nidaqmx_grpc.WriteStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"@\n\x1fGetWriteAttributeStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t"\xaa\x01\n\x1eGetWriteAttributeUInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x127\n\tattribute\x18\x02 \x01(\x0e2".nidaqmx_grpc.WriteUInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"@\n\x1fGetWriteAttributeUInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\r"\xaa\x01\n\x1eGetWriteAttributeUInt64Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x127\n\tattribute\x18\x02 \x01(\x0e2".nidaqmx_grpc.WriteUInt64AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"@\n\x1fGetWriteAttributeUInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x04"9\n\x11IsTaskDoneRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session":\n\x12IsTaskDoneResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x14\n\x0cis_task_done\x18\x02 \x01(\x08"v\n\x0fLoadTaskRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12M\n\x17initialization_behavior\x18\x02 \x01(\x0e2,.nidevice_grpc.SessionInitializationBehavior"i\n\x10LoadTaskResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12$\n\x04task\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1f\n\x17new_session_initialized\x18\x03 \x01(\x08"\x82\x01\n&PerformBridgeOffsetNullingCalExRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07channel\x18\x02 \x01(\t\x12!\n\x19skip_unsupported_channels\x18\x03 \x01(\x08"9\n\'PerformBridgeOffsetNullingCalExResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc5\x04\n\x1ePerformBridgeShuntCalExRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07channel\x18\x02 \x01(\t\x12\x1c\n\x14shunt_resistor_value\x18\x03 \x01(\x01\x12E\n\x17shunt_resistor_location\x18\x04 \x01(\x0e2".nidaqmx_grpc.ShuntElementLocationH\x00\x12%\n\x1bshunt_resistor_location_raw\x18\x05 \x01(\x05H\x00\x12=\n\x15shunt_resistor_select\x18\x06 \x01(\x0e2\x1c.nidaqmx_grpc.ShuntCalSelectH\x01\x12#\n\x19shunt_resistor_select_raw\x18\x07 \x01(\x05H\x01\x12=\n\x15shunt_resistor_source\x18\x08 \x01(\x0e2\x1c.nidaqmx_grpc.ShuntCalSourceH\x02\x12#\n\x19shunt_resistor_source_raw\x18\t \x01(\x05H\x02\x12\x19\n\x11bridge_resistance\x18\n \x01(\x01\x12!\n\x19skip_unsupported_channels\x18\x0b \x01(\x08B\x1e\n\x1cshunt_resistor_location_enumB\x1c\n\x1ashunt_resistor_select_enumB\x1c\n\x1ashunt_resistor_source_enum"1\n\x1fPerformBridgeShuntCalExResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xaa\x04\n\x1ePerformStrainShuntCalExRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07channel\x18\x02 \x01(\t\x12\x1c\n\x14shunt_resistor_value\x18\x03 \x01(\x01\x12E\n\x17shunt_resistor_location\x18\x04 \x01(\x0e2".nidaqmx_grpc.ShuntElementLocationH\x00\x12%\n\x1bshunt_resistor_location_raw\x18\x05 \x01(\x05H\x00\x12=\n\x15shunt_resistor_select\x18\x06 \x01(\x0e2\x1c.nidaqmx_grpc.ShuntCalSelectH\x01\x12#\n\x19shunt_resistor_select_raw\x18\x07 \x01(\x05H\x01\x12=\n\x15shunt_resistor_source\x18\x08 \x01(\x0e2\x1c.nidaqmx_grpc.ShuntCalSourceH\x02\x12#\n\x19shunt_resistor_source_raw\x18\t \x01(\x05H\x02\x12!\n\x19skip_unsupported_channels\x18\n \x01(\x08B\x1e\n\x1cshunt_resistor_location_enumB\x1c\n\x1ashunt_resistor_select_enumB\x1c\n\x1ashunt_resistor_source_enum"1\n\x1fPerformStrainShuntCalExResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x85\x01\n)PerformThrmcplLeadOffsetNullingCalRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07channel\x18\x02 \x01(\t\x12!\n\x19skip_unsupported_channels\x18\x03 \x01(\x08"<\n*PerformThrmcplLeadOffsetNullingCalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xdd\x01\n\x14ReadAnalogF64Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"X\n\x15ReadAnalogF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x03(\x01\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"\xe2\x01\n\x19BeginReadAnalogF64Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"X\n\x1aBeginReadAnalogF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"_\n\x1cMonikerReadAnalogF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x03(\x01\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"S\n\x1aReadAnalogScalarF64Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07timeout\x18\x02 \x01(\x01"<\n\x1bReadAnalogScalarF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01"X\n\x1fBeginReadAnalogScalarF64Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07timeout\x18\x02 \x01(\x01"^\n BeginReadAnalogScalarF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"C\n"MonikerReadAnalogScalarF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01"\xdd\x01\n\x14ReadBinaryI16Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"X\n\x15ReadBinaryI16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x03(\x05\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"\xe2\x01\n\x19BeginReadBinaryI16Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"X\n\x1aBeginReadBinaryI16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"_\n\x1cMonikerReadBinaryI16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x03(\x05\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"\xdd\x01\n\x14ReadBinaryI32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"X\n\x15ReadBinaryI32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x03(\x05\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"\xe2\x01\n\x19BeginReadBinaryI32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"X\n\x1aBeginReadBinaryI32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"_\n\x1cMonikerReadBinaryI32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x03(\x05\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"\xdd\x01\n\x14ReadBinaryU16Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"X\n\x15ReadBinaryU16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x03(\r\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"\xe2\x01\n\x19BeginReadBinaryU16Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"X\n\x1aBeginReadBinaryU16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"_\n\x1cMonikerReadBinaryU16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x03(\r\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"\xdd\x01\n\x14ReadBinaryU32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"X\n\x15ReadBinaryU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x03(\r\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"\xe2\x01\n\x19BeginReadBinaryU32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"X\n\x1aBeginReadBinaryU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"_\n\x1cMonikerReadBinaryU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x03(\r\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"\x87\x01\n\x15ReadCounterF64Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12\x1b\n\x13array_size_in_samps\x18\x04 \x01(\r"Y\n\x16ReadCounterF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x03(\x01\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"\x8c\x01\n\x1aBeginReadCounterF64Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12\x1b\n\x13array_size_in_samps\x18\x04 \x01(\r"Y\n\x1bBeginReadCounterF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"`\n\x1dMonikerReadCounterF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x03(\x01\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"\xe0\x01\n\x17ReadCounterF64ExRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"[\n\x18ReadCounterF64ExResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x03(\x01\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"\xe5\x01\n\x1cBeginReadCounterF64ExRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"[\n\x1dBeginReadCounterF64ExResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"b\n\x1fMonikerReadCounterF64ExResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x03(\x01\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"T\n\x1bReadCounterScalarF64Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07timeout\x18\x02 \x01(\x01"=\n\x1cReadCounterScalarF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01"Y\n BeginReadCounterScalarF64Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07timeout\x18\x02 \x01(\x01"_\n!BeginReadCounterScalarF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"D\n#MonikerReadCounterScalarF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01"T\n\x1bReadCounterScalarU32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07timeout\x18\x02 \x01(\x01"=\n\x1cReadCounterScalarU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\r"Y\n BeginReadCounterScalarU32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07timeout\x18\x02 \x01(\x01"_\n!BeginReadCounterScalarU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"D\n#MonikerReadCounterScalarU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\r"\x87\x01\n\x15ReadCounterU32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12\x1b\n\x13array_size_in_samps\x18\x04 \x01(\r"Y\n\x16ReadCounterU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x03(\r\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"\x8c\x01\n\x1aBeginReadCounterU32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12\x1b\n\x13array_size_in_samps\x18\x04 \x01(\r"Y\n\x1bBeginReadCounterU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"`\n\x1dMonikerReadCounterU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x03(\r\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"\xe0\x01\n\x17ReadCounterU32ExRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"[\n\x18ReadCounterU32ExResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x03(\r\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"\xe5\x01\n\x1cBeginReadCounterU32ExRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"[\n\x1dBeginReadCounterU32ExResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"b\n\x1fMonikerReadCounterU32ExResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x03(\r\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"\xe1\x01\n\x12ReadCtrFreqRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12,\n\x0binterleaved\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0finterleaved_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x12\n\x10interleaved_enum"\x7f\n\x13ReadCtrFreqResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1c\n\x14read_array_frequency\x18\x02 \x03(\x01\x12\x1d\n\x15read_array_duty_cycle\x18\x03 \x03(\x01\x12\x1b\n\x13samps_per_chan_read\x18\x04 \x01(\x05"\xe6\x01\n\x17BeginReadCtrFreqRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12,\n\x0binterleaved\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0finterleaved_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x12\n\x10interleaved_enum"V\n\x18BeginReadCtrFreqResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"\x86\x01\n\x1aMonikerReadCtrFreqResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1c\n\x14read_array_frequency\x18\x02 \x03(\x01\x12\x1d\n\x15read_array_duty_cycle\x18\x03 \x03(\x01\x12\x1b\n\x13samps_per_chan_read\x18\x04 \x01(\x05"Q\n\x18ReadCtrFreqScalarRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07timeout\x18\x02 \x01(\x01"R\n\x19ReadCtrFreqScalarResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\tfrequency\x18\x02 \x01(\x01\x12\x12\n\nduty_cycle\x18\x03 \x01(\x01"V\n\x1dBeginReadCtrFreqScalarRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07timeout\x18\x02 \x01(\x01"\\\n\x1eBeginReadCtrFreqScalarResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"Y\n MonikerReadCtrFreqScalarResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\tfrequency\x18\x02 \x01(\x01\x12\x12\n\nduty_cycle\x18\x03 \x01(\x01"\xe2\x01\n\x13ReadCtrTicksRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12,\n\x0binterleaved\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0finterleaved_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x12\n\x10interleaved_enum"\x80\x01\n\x14ReadCtrTicksResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1d\n\x15read_array_high_ticks\x18\x02 \x03(\r\x12\x1c\n\x14read_array_low_ticks\x18\x03 \x03(\r\x12\x1b\n\x13samps_per_chan_read\x18\x04 \x01(\x05"\xe7\x01\n\x18BeginReadCtrTicksRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12,\n\x0binterleaved\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0finterleaved_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x12\n\x10interleaved_enum"W\n\x19BeginReadCtrTicksResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"\x87\x01\n\x1bMonikerReadCtrTicksResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1d\n\x15read_array_high_ticks\x18\x02 \x03(\r\x12\x1c\n\x14read_array_low_ticks\x18\x03 \x03(\r\x12\x1b\n\x13samps_per_chan_read\x18\x04 \x01(\x05"R\n\x19ReadCtrTicksScalarRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07timeout\x18\x02 \x01(\x01"S\n\x1aReadCtrTicksScalarResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nhigh_ticks\x18\x02 \x01(\r\x12\x11\n\tlow_ticks\x18\x03 \x01(\r"W\n\x1eBeginReadCtrTicksScalarRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07timeout\x18\x02 \x01(\x01"]\n\x1fBeginReadCtrTicksScalarResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"Z\n!MonikerReadCtrTicksScalarResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nhigh_ticks\x18\x02 \x01(\r\x12\x11\n\tlow_ticks\x18\x03 \x01(\r"\xe1\x01\n\x12ReadCtrTimeRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12,\n\x0binterleaved\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0finterleaved_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x12\n\x10interleaved_enum"}\n\x13ReadCtrTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1c\n\x14read_array_high_time\x18\x02 \x03(\x01\x12\x1b\n\x13read_array_low_time\x18\x03 \x03(\x01\x12\x1b\n\x13samps_per_chan_read\x18\x04 \x01(\x05"\xe6\x01\n\x17BeginReadCtrTimeRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12,\n\x0binterleaved\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0finterleaved_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x12\n\x10interleaved_enum"V\n\x18BeginReadCtrTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"\x84\x01\n\x1aMonikerReadCtrTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1c\n\x14read_array_high_time\x18\x02 \x03(\x01\x12\x1b\n\x13read_array_low_time\x18\x03 \x03(\x01\x12\x1b\n\x13samps_per_chan_read\x18\x04 \x01(\x05"Q\n\x18ReadCtrTimeScalarRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07timeout\x18\x02 \x01(\x01"P\n\x19ReadCtrTimeScalarResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\thigh_time\x18\x02 \x01(\x01\x12\x10\n\x08low_time\x18\x03 \x01(\x01"V\n\x1dBeginReadCtrTimeScalarRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07timeout\x18\x02 \x01(\x01"\\\n\x1eBeginReadCtrTimeScalarResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"W\n MonikerReadCtrTimeScalarResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\thigh_time\x18\x02 \x01(\x01\x12\x10\n\x08low_time\x18\x03 \x01(\x01"\xe0\x01\n\x17ReadDigitalLinesRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_bytes\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"w\n\x18ReadDigitalLinesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x01(\x0c\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05\x12\x1a\n\x12num_bytes_per_samp\x18\x04 \x01(\x05"\xe5\x01\n\x1cBeginReadDigitalLinesRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_bytes\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"w\n\x1dBeginReadDigitalLinesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1a\n\x12num_bytes_per_samp\x18\x02 \x01(\x05\x12*\n\x07moniker\x18\x03 \x01(\x0b2\x19.ni.data_monikers.Moniker"~\n\x1fMonikerReadDigitalLinesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x01(\x0c\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05\x12\x1a\n\x12num_bytes_per_samp\x18\x04 \x01(\x05"T\n\x1bReadDigitalScalarU32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07timeout\x18\x02 \x01(\x01"=\n\x1cReadDigitalScalarU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\r"Y\n BeginReadDigitalScalarU32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07timeout\x18\x02 \x01(\x01"_\n!BeginReadDigitalScalarU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"D\n#MonikerReadDigitalScalarU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\r"\xde\x01\n\x15ReadDigitalU16Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"Y\n\x16ReadDigitalU16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x03(\r\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"\xe3\x01\n\x1aBeginReadDigitalU16Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"Y\n\x1bBeginReadDigitalU16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"`\n\x1dMonikerReadDigitalU16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x03(\r\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"\xde\x01\n\x15ReadDigitalU32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"Y\n\x16ReadDigitalU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x03(\r\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"\xe3\x01\n\x1aBeginReadDigitalU32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"Y\n\x1bBeginReadDigitalU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"`\n\x1dMonikerReadDigitalU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x03(\r\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"\xdd\x01\n\x14ReadDigitalU8Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"X\n\x15ReadDigitalU8Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x01(\x0c\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"\xe2\x01\n\x19BeginReadDigitalU8Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"X\n\x1aBeginReadDigitalU8Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"_\n\x1cMonikerReadDigitalU8Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x01(\x0c\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"V\n\x16ReadIDPinMemoryRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x12\x13\n\x0bid_pin_name\x18\x02 \x01(\t\x12\x12\n\narray_size\x18\x03 \x01(\r"f\n\x17ReadIDPinMemoryResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04data\x18\x02 \x01(\x0c\x12\x18\n\x10data_length_read\x18\x03 \x01(\r\x12\x13\n\x0bformat_code\x18\x04 \x01(\r"\xe2\x01\n\x19ReadPowerBinaryI16Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"\x81\x01\n\x1aReadPowerBinaryI16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1a\n\x12read_array_voltage\x18\x02 \x03(\x05\x12\x1a\n\x12read_array_current\x18\x03 \x03(\x05\x12\x1b\n\x13samps_per_chan_read\x18\x04 \x01(\x05"\xe7\x01\n\x1eBeginReadPowerBinaryI16Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"]\n\x1fBeginReadPowerBinaryI16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"\x88\x01\n!MonikerReadPowerBinaryI16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1a\n\x12read_array_voltage\x18\x02 \x03(\x05\x12\x1a\n\x12read_array_current\x18\x03 \x03(\x05\x12\x1b\n\x13samps_per_chan_read\x18\x04 \x01(\x05"\xdc\x01\n\x13ReadPowerF64Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"{\n\x14ReadPowerF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1a\n\x12read_array_voltage\x18\x02 \x03(\x01\x12\x1a\n\x12read_array_current\x18\x03 \x03(\x01\x12\x1b\n\x13samps_per_chan_read\x18\x04 \x01(\x05"\xe1\x01\n\x18BeginReadPowerF64Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12*\n\tfill_mode\x18\x04 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x17\n\rfill_mode_raw\x18\x05 \x01(\x05H\x00\x12\x1b\n\x13array_size_in_samps\x18\x06 \x01(\rB\x10\n\x0efill_mode_enum"W\n\x19BeginReadPowerF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"\x82\x01\n\x1bMonikerReadPowerF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1a\n\x12read_array_voltage\x18\x02 \x03(\x01\x12\x1a\n\x12read_array_current\x18\x03 \x03(\x01\x12\x1b\n\x13samps_per_chan_read\x18\x04 \x01(\x05"R\n\x19ReadPowerScalarF64Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07timeout\x18\x02 \x01(\x01"N\n\x1aReadPowerScalarF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07voltage\x18\x02 \x01(\x01\x12\x0f\n\x07current\x18\x03 \x01(\x01"W\n\x1eBeginReadPowerScalarF64Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07timeout\x18\x02 \x01(\x01"]\n\x1fBeginReadPowerScalarF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"U\n!MonikerReadPowerScalarF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07voltage\x18\x02 \x01(\x01\x12\x0f\n\x07current\x18\x03 \x01(\x01"\x80\x01\n\x0eReadRawRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12\x1b\n\x13array_size_in_bytes\x18\x04 \x01(\r"e\n\x0fReadRawResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x01(\x0c\x12\x12\n\nsamps_read\x18\x03 \x01(\x05\x12\x1a\n\x12num_bytes_per_samp\x18\x04 \x01(\x05"\x85\x01\n\x13BeginReadRawRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12\x1b\n\x13array_size_in_bytes\x18\x04 \x01(\r"R\n\x14BeginReadRawResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"l\n\x16MonikerReadRawResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nread_array\x18\x02 \x01(\x0c\x12\x12\n\nsamps_read\x18\x03 \x01(\x05\x12\x1a\n\x12num_bytes_per_samp\x18\x04 \x01(\x05"@\n\x18RegisterDoneEventRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"+\n\x19RegisterDoneEventResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xf5\x01\n!RegisterEveryNSamplesEventRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12J\n\x1aevery_n_samples_event_type\x18\x02 \x01(\x0e2$.nidaqmx_grpc.EveryNSamplesEventTypeH\x00\x12(\n\x1eevery_n_samples_event_type_raw\x18\x03 \x01(\x05H\x00\x12\x11\n\tn_samples\x18\x04 \x01(\rB!\n\x1fevery_n_samples_event_type_enum"\xb9\x01\n"RegisterEveryNSamplesEventResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12H\n\x1aevery_n_samples_event_type\x18\x02 \x01(\x0e2$.nidaqmx_grpc.EveryNSamplesEventType\x12&\n\x1eevery_n_samples_event_type_raw\x18\x03 \x01(\x05\x12\x11\n\tn_samples\x18\x04 \x01(\r"\x99\x01\n\x1aRegisterSignalEventRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12*\n\tsignal_id\x18\x02 \x01(\x0e2\x15.nidaqmx_grpc.Signal2H\x00\x12\x17\n\rsignal_id_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0esignal_id_enum"@\n\x1bRegisterSignalEventResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\tsignal_id\x18\x02 \x01(\x05"4\n\x1fRemoveCDAQSyncConnectionRequest\x12\x11\n\tport_list\x18\x01 \x01(\t"2\n RemoveCDAQSyncConnectionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"P\n\x1bReserveNetworkDeviceRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x12\x1c\n\x14override_reservation\x18\x02 \x01(\x08".\n\x1cReserveNetworkDeviceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa7\x01\n\x1bResetBufferAttributeRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x127\n\tattribute\x18\x02 \x01(\x0e2".nidaqmx_grpc.BufferResetAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum".\n\x1cResetBufferAttributeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb7\x01\n\x19ResetChanAttributeRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07channel\x18\x02 \x01(\t\x128\n\tattribute\x18\x03 \x01(\x0e2#.nidaqmx_grpc.ChannelResetAttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00B\x10\n\x0eattribute_enum",\n\x1aResetChanAttributeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05")\n\x12ResetDeviceRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t"%\n\x13ResetDeviceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb5\x01\n#ResetExportedSignalAttributeRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12=\n\tattribute\x18\x02 \x01(\x0e2(.nidaqmx_grpc.ExportSignalResetAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"6\n$ResetExportedSignalAttributeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa3\x01\n\x19ResetReadAttributeRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x125\n\tattribute\x18\x02 \x01(\x0e2 .nidaqmx_grpc.ReadResetAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum",\n\x1aResetReadAttributeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xab\x01\n\x1dResetRealTimeAttributeRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x129\n\tattribute\x18\x02 \x01(\x0e2$.nidaqmx_grpc.RealTimeResetAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"0\n\x1eResetRealTimeAttributeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa7\x01\n\x1bResetTimingAttributeRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x127\n\tattribute\x18\x02 \x01(\x0e2".nidaqmx_grpc.TimingResetAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum".\n\x1cResetTimingAttributeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xbf\x01\n\x1dResetTimingAttributeExRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cdevice_names\x18\x02 \x01(\t\x127\n\tattribute\x18\x03 \x01(\x0e2".nidaqmx_grpc.TimingResetAttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00B\x10\n\x0eattribute_enum"0\n\x1eResetTimingAttributeExResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa6\x01\n\x19ResetTrigAttributeRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x128\n\tattribute\x18\x02 \x01(\x0e2#.nidaqmx_grpc.TriggerResetAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum",\n\x1aResetTrigAttributeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xba\x01\n\x1dResetWatchdogAttributeRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05lines\x18\x02 \x01(\t\x129\n\tattribute\x18\x03 \x01(\x0e2$.nidaqmx_grpc.WatchdogResetAttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00B\x10\n\x0eattribute_enum"0\n\x1eResetWatchdogAttributeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa5\x01\n\x1aResetWriteAttributeRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x126\n\tattribute\x18\x02 \x01(\x0e2!.nidaqmx_grpc.WriteResetAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0eattribute_enum"-\n\x1bResetWriteAttributeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"4\n\x1dRestoreLastExtCalConstRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t"0\n\x1eRestoreLastExtCalConstResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc9\x01\n\x15SaveGlobalChanRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x0f\n\x07save_as\x18\x03 \x01(\t\x12\x0e\n\x06author\x18\x04 \x01(\t\x12,\n\x07options\x18\x05 \x01(\x0e2\x19.nidaqmx_grpc.SaveOptionsH\x00\x12\x15\n\x0boptions_raw\x18\x06 \x01(\rH\x00B\x0e\n\x0coptions_enum"(\n\x16SaveGlobalChanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x9c\x01\n\x10SaveScaleRequest\x12\x12\n\nscale_name\x18\x01 \x01(\t\x12\x0f\n\x07save_as\x18\x02 \x01(\t\x12\x0e\n\x06author\x18\x03 \x01(\t\x12,\n\x07options\x18\x04 \x01(\x0e2\x19.nidaqmx_grpc.SaveOptionsH\x00\x12\x15\n\x0boptions_raw\x18\x05 \x01(\rH\x00B\x0e\n\x0coptions_enum"#\n\x11SaveScaleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xad\x01\n\x0fSaveTaskRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07save_as\x18\x02 \x01(\t\x12\x0e\n\x06author\x18\x03 \x01(\t\x12,\n\x07options\x18\x04 \x01(\x0e2\x19.nidaqmx_grpc.SaveOptionsH\x00\x12\x15\n\x0boptions_raw\x18\x05 \x01(\rH\x00B\x0e\n\x0coptions_enum""\n\x10SaveTaskResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"%\n\x0eSelfCalRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t"!\n\x0fSelfCalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05",\n\x15SelfTestDeviceRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t"(\n\x16SelfTestDeviceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa0\x01\n\x1aSetAIChanCalCalDateRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x0c\n\x04year\x18\x03 \x01(\r\x12\r\n\x05month\x18\x04 \x01(\r\x12\x0b\n\x03day\x18\x05 \x01(\r\x12\x0c\n\x04hour\x18\x06 \x01(\r\x12\x0e\n\x06minute\x18\x07 \x01(\r"-\n\x1bSetAIChanCalCalDateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa0\x01\n\x1aSetAIChanCalExpDateRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x0c\n\x04year\x18\x03 \x01(\r\x12\r\n\x05month\x18\x04 \x01(\r\x12\x0b\n\x03day\x18\x05 \x01(\r\x12\x0c\n\x04hour\x18\x06 \x01(\r\x12\x0e\n\x06minute\x18\x07 \x01(\r"-\n\x1bSetAIChanCalExpDateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"z\n\x1dSetAnalogPowerUpStatesRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x12D\n\x0fpower_up_states\x18\x02 \x03(\x0b2+.nidaqmx_grpc.AnalogPowerUpChannelsAndState"0\n\x1eSetAnalogPowerUpStatesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x97\x01\n+SetAnalogPowerUpStatesWithOutputTypeRequest\x12\x15\n\rchannel_names\x18\x01 \x01(\t\x12\x13\n\x0bstate_array\x18\x02 \x03(\x01\x12<\n\x12channel_type_array\x18\x03 \x03(\x0e2 .nidaqmx_grpc.PowerUpChannelType">\n,SetAnalogPowerUpStatesWithOutputTypeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"p\n\x1eSetArmStartTrigTrigWhenRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12(\n\x04data\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"1\n\x1fSetArmStartTrigTrigWhenResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xbb\x01\n\x1fSetBufferAttributeUInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x128\n\tattribute\x18\x02 \x01(\x0e2#.nidaqmx_grpc.BufferUInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\rB\x10\n\x0eattribute_enum"2\n SetBufferAttributeUInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb0\x01\n\x1eSetCalInfoAttributeBoolRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x12?\n\tattribute\x18\x02 \x01(\x0e2*.nidaqmx_grpc.CalibrationInfoBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\x08B\x10\n\x0eattribute_enum"1\n\x1fSetCalInfoAttributeBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb4\x01\n SetCalInfoAttributeDoubleRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x12A\n\tattribute\x18\x02 \x01(\x0e2,.nidaqmx_grpc.CalibrationInfoDoubleAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\x01B\x10\n\x0eattribute_enum"3\n!SetCalInfoAttributeDoubleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb4\x01\n SetCalInfoAttributeStringRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x12A\n\tattribute\x18\x02 \x01(\x0e2,.nidaqmx_grpc.CalibrationInfoStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\tB\x10\n\x0eattribute_enum"3\n!SetCalInfoAttributeStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb4\x01\n SetCalInfoAttributeUInt32Request\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x12A\n\tattribute\x18\x02 \x01(\x0e2,.nidaqmx_grpc.CalibrationInfoUInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\rB\x10\n\x0eattribute_enum"3\n!SetCalInfoAttributeUInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc7\x01\n\x1bSetChanAttributeBoolRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07channel\x18\x02 \x01(\t\x127\n\tattribute\x18\x03 \x01(\x0e2".nidaqmx_grpc.ChannelBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00\x12\r\n\x05value\x18\x05 \x01(\x08B\x10\n\x0eattribute_enum".\n\x1cSetChanAttributeBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xcb\x01\n\x1dSetChanAttributeDoubleRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07channel\x18\x02 \x01(\t\x129\n\tattribute\x18\x03 \x01(\x0e2$.nidaqmx_grpc.ChannelDoubleAttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00\x12\r\n\x05value\x18\x05 \x01(\x01B\x10\n\x0eattribute_enum"0\n\x1eSetChanAttributeDoubleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd5\x01\n"SetChanAttributeDoubleArrayRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07channel\x18\x02 \x01(\t\x12>\n\tattribute\x18\x03 \x01(\x0e2).nidaqmx_grpc.ChannelDoubleArrayAttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00\x12\r\n\x05value\x18\x05 \x03(\x01B\x10\n\x0eattribute_enum"5\n#SetChanAttributeDoubleArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x99\x02\n\x1cSetChanAttributeInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07channel\x18\x02 \x01(\t\x128\n\tattribute\x18\x03 \x01(\x0e2#.nidaqmx_grpc.ChannelInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00\x12:\n\x05value\x18\x05 \x01(\x0e2).nidaqmx_grpc.ChannelInt32AttributeValuesH\x01\x12\x13\n\tvalue_raw\x18\x06 \x01(\x05H\x01B\x10\n\x0eattribute_enumB\x0c\n\nvalue_enum"/\n\x1dSetChanAttributeInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xcb\x01\n\x1dSetChanAttributeStringRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07channel\x18\x02 \x01(\t\x129\n\tattribute\x18\x03 \x01(\x0e2$.nidaqmx_grpc.ChannelStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00\x12\r\n\x05value\x18\x05 \x01(\tB\x10\n\x0eattribute_enum"0\n\x1eSetChanAttributeStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xcb\x01\n\x1dSetChanAttributeUInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07channel\x18\x02 \x01(\t\x129\n\tattribute\x18\x03 \x01(\x0e2$.nidaqmx_grpc.ChannelUInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00\x12\r\n\x05value\x18\x05 \x01(\rB\x10\n\x0eattribute_enum"0\n\x1eSetChanAttributeUInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa3\x01\n(SetDigitalLogicFamilyPowerUpStateRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x121\n\x0clogic_family\x18\x02 \x01(\x0e2\x19.nidaqmx_grpc.LogicFamilyH\x00\x12\x1a\n\x10logic_family_raw\x18\x03 \x01(\x05H\x00B\x13\n\x11logic_family_enum";\n)SetDigitalLogicFamilyPowerUpStateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"|\n\x1eSetDigitalPowerUpStatesRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x12E\n\x0fpower_up_states\x18\x02 \x03(\x0b2,.nidaqmx_grpc.DigitalPowerUpChannelsAndState"1\n\x1fSetDigitalPowerUpStatesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x93\x01\n%SetDigitalPullUpPullDownStatesRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x12U\n\x18pull_up_pull_down_states\x18\x02 \x03(\x0b23.nidaqmx_grpc.DigitalPullUpPullDownChannelsAndState"8\n&SetDigitalPullUpPullDownStatesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc5\x01\n%SetExportedSignalAttributeBoolRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12<\n\tattribute\x18\x02 \x01(\x0e2\'.nidaqmx_grpc.ExportSignalBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\x08B\x10\n\x0eattribute_enum"8\n&SetExportedSignalAttributeBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc9\x01\n\'SetExportedSignalAttributeDoubleRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12>\n\tattribute\x18\x02 \x01(\x0e2).nidaqmx_grpc.ExportSignalDoubleAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\x01B\x10\n\x0eattribute_enum":\n(SetExportedSignalAttributeDoubleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x9c\x02\n&SetExportedSignalAttributeInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12=\n\tattribute\x18\x02 \x01(\x0e2(.nidaqmx_grpc.ExportSignalInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12?\n\x05value\x18\x04 \x01(\x0e2..nidaqmx_grpc.ExportSignalInt32AttributeValuesH\x01\x12\x13\n\tvalue_raw\x18\x05 \x01(\x05H\x01B\x10\n\x0eattribute_enumB\x0c\n\nvalue_enum"9\n\'SetExportedSignalAttributeInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc9\x01\n\'SetExportedSignalAttributeStringRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12>\n\tattribute\x18\x02 \x01(\x0e2).nidaqmx_grpc.ExportSignalStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\tB\x10\n\x0eattribute_enum":\n(SetExportedSignalAttributeStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc9\x01\n\'SetExportedSignalAttributeUInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12>\n\tattribute\x18\x02 \x01(\x0e2).nidaqmx_grpc.ExportSignalUInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\rB\x10\n\x0eattribute_enum":\n(SetExportedSignalAttributeUInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"l\n\x1aSetFirstSampClkWhenRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12(\n\x04data\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"-\n\x1bSetFirstSampClkWhenResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb3\x01\n\x1bSetReadAttributeBoolRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x124\n\tattribute\x18\x02 \x01(\x0e2\x1f.nidaqmx_grpc.ReadBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\x08B\x10\n\x0eattribute_enum".\n\x1cSetReadAttributeBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb7\x01\n\x1dSetReadAttributeDoubleRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x126\n\tattribute\x18\x02 \x01(\x0e2!.nidaqmx_grpc.ReadDoubleAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\x01B\x10\n\x0eattribute_enum"0\n\x1eSetReadAttributeDoubleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x82\x02\n\x1cSetReadAttributeInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x125\n\tattribute\x18\x02 \x01(\x0e2 .nidaqmx_grpc.ReadInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x127\n\x05value\x18\x04 \x01(\x0e2&.nidaqmx_grpc.ReadInt32AttributeValuesH\x01\x12\x13\n\tvalue_raw\x18\x05 \x01(\x05H\x01B\x10\n\x0eattribute_enumB\x0c\n\nvalue_enum"/\n\x1dSetReadAttributeInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb7\x01\n\x1dSetReadAttributeStringRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x126\n\tattribute\x18\x02 \x01(\x0e2!.nidaqmx_grpc.ReadStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\tB\x10\n\x0eattribute_enum"0\n\x1eSetReadAttributeStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb7\x01\n\x1dSetReadAttributeUInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x126\n\tattribute\x18\x02 \x01(\x0e2!.nidaqmx_grpc.ReadUInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\rB\x10\n\x0eattribute_enum"0\n\x1eSetReadAttributeUInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb7\x01\n\x1dSetReadAttributeUInt64Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x126\n\tattribute\x18\x02 \x01(\x0e2!.nidaqmx_grpc.ReadUInt64AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\x04B\x10\n\x0eattribute_enum"0\n\x1eSetReadAttributeUInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xbb\x01\n\x1fSetRealTimeAttributeBoolRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x128\n\tattribute\x18\x02 \x01(\x0e2#.nidaqmx_grpc.RealTimeBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\x08B\x10\n\x0eattribute_enum"2\n SetRealTimeAttributeBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x8e\x02\n SetRealTimeAttributeInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x129\n\tattribute\x18\x02 \x01(\x0e2$.nidaqmx_grpc.RealTimeInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12;\n\x05value\x18\x04 \x01(\x0e2*.nidaqmx_grpc.RealTimeInt32AttributeValuesH\x01\x12\x13\n\tvalue_raw\x18\x05 \x01(\x05H\x01B\x10\n\x0eattribute_enumB\x0c\n\nvalue_enum"3\n!SetRealTimeAttributeInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xbf\x01\n!SetRealTimeAttributeUInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12:\n\tattribute\x18\x02 \x01(\x0e2%.nidaqmx_grpc.RealTimeUInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\rB\x10\n\x0eattribute_enum"4\n"SetRealTimeAttributeUInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa7\x01\n\x1eSetScaleAttributeDoubleRequest\x12\x12\n\nscale_name\x18\x01 \x01(\t\x127\n\tattribute\x18\x02 \x01(\x0e2".nidaqmx_grpc.ScaleDoubleAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\x01B\x10\n\x0eattribute_enum"1\n\x1fSetScaleAttributeDoubleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb1\x01\n#SetScaleAttributeDoubleArrayRequest\x12\x12\n\nscale_name\x18\x01 \x01(\t\x12<\n\tattribute\x18\x02 \x01(\x0e2\'.nidaqmx_grpc.ScaleDoubleArrayAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x03(\x01B\x10\n\x0eattribute_enum"6\n$SetScaleAttributeDoubleArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xf3\x01\n\x1dSetScaleAttributeInt32Request\x12\x12\n\nscale_name\x18\x01 \x01(\t\x126\n\tattribute\x18\x02 \x01(\x0e2!.nidaqmx_grpc.ScaleInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x128\n\x05value\x18\x04 \x01(\x0e2\'.nidaqmx_grpc.ScaleInt32AttributeValuesH\x01\x12\x13\n\tvalue_raw\x18\x05 \x01(\x05H\x01B\x10\n\x0eattribute_enumB\x0c\n\nvalue_enum"0\n\x1eSetScaleAttributeInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa7\x01\n\x1eSetScaleAttributeStringRequest\x12\x12\n\nscale_name\x18\x01 \x01(\t\x127\n\tattribute\x18\x02 \x01(\x0e2".nidaqmx_grpc.ScaleStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\tB\x10\n\x0eattribute_enum"1\n\x1fSetScaleAttributeStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"m\n\x1bSetStartTrigTrigWhenRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12(\n\x04data\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp".\n\x1cSetStartTrigTrigWhenResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"m\n\x1bSetSyncPulseTimeWhenRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12(\n\x04data\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp".\n\x1cSetSyncPulseTimeWhenResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb7\x01\n\x1dSetTimingAttributeBoolRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x126\n\tattribute\x18\x02 \x01(\x0e2!.nidaqmx_grpc.TimingBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\x08B\x10\n\x0eattribute_enum"0\n\x1eSetTimingAttributeBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xbb\x01\n\x1fSetTimingAttributeDoubleRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x128\n\tattribute\x18\x02 \x01(\x0e2#.nidaqmx_grpc.TimingDoubleAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\x01B\x10\n\x0eattribute_enum"2\n SetTimingAttributeDoubleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xcf\x01\n\x1fSetTimingAttributeExBoolRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cdevice_names\x18\x02 \x01(\t\x126\n\tattribute\x18\x03 \x01(\x0e2!.nidaqmx_grpc.TimingBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00\x12\r\n\x05value\x18\x05 \x01(\x08B\x10\n\x0eattribute_enum"2\n SetTimingAttributeExBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd3\x01\n!SetTimingAttributeExDoubleRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cdevice_names\x18\x02 \x01(\t\x128\n\tattribute\x18\x03 \x01(\x0e2#.nidaqmx_grpc.TimingDoubleAttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00\x12\r\n\x05value\x18\x05 \x01(\x01B\x10\n\x0eattribute_enum"4\n"SetTimingAttributeExDoubleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa0\x02\n SetTimingAttributeExInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cdevice_names\x18\x02 \x01(\t\x127\n\tattribute\x18\x03 \x01(\x0e2".nidaqmx_grpc.TimingInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00\x129\n\x05value\x18\x05 \x01(\x0e2(.nidaqmx_grpc.TimingInt32AttributeValuesH\x01\x12\x13\n\tvalue_raw\x18\x06 \x01(\x05H\x01B\x10\n\x0eattribute_enumB\x0c\n\nvalue_enum"3\n!SetTimingAttributeExInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd3\x01\n!SetTimingAttributeExStringRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cdevice_names\x18\x02 \x01(\t\x128\n\tattribute\x18\x03 \x01(\x0e2#.nidaqmx_grpc.TimingStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00\x12\r\n\x05value\x18\x05 \x01(\tB\x10\n\x0eattribute_enum"4\n"SetTimingAttributeExStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xf5\x01\n$SetTimingAttributeExTimestampRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cdevice_names\x18\x02 \x01(\t\x12;\n\tattribute\x18\x03 \x01(\x0e2&.nidaqmx_grpc.TimingTimestampAttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00\x12)\n\x05value\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x10\n\x0eattribute_enum"7\n%SetTimingAttributeExTimestampResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd3\x01\n!SetTimingAttributeExUInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cdevice_names\x18\x02 \x01(\t\x128\n\tattribute\x18\x03 \x01(\x0e2#.nidaqmx_grpc.TimingUInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00\x12\r\n\x05value\x18\x05 \x01(\rB\x10\n\x0eattribute_enum"4\n"SetTimingAttributeExUInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd3\x01\n!SetTimingAttributeExUInt64Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cdevice_names\x18\x02 \x01(\t\x128\n\tattribute\x18\x03 \x01(\x0e2#.nidaqmx_grpc.TimingUInt64AttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00\x12\r\n\x05value\x18\x05 \x01(\x04B\x10\n\x0eattribute_enum"4\n"SetTimingAttributeExUInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x88\x02\n\x1eSetTimingAttributeInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x127\n\tattribute\x18\x02 \x01(\x0e2".nidaqmx_grpc.TimingInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x129\n\x05value\x18\x04 \x01(\x0e2(.nidaqmx_grpc.TimingInt32AttributeValuesH\x01\x12\x13\n\tvalue_raw\x18\x05 \x01(\x05H\x01B\x10\n\x0eattribute_enumB\x0c\n\nvalue_enum"1\n\x1fSetTimingAttributeInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xbb\x01\n\x1fSetTimingAttributeStringRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x128\n\tattribute\x18\x02 \x01(\x0e2#.nidaqmx_grpc.TimingStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\tB\x10\n\x0eattribute_enum"2\n SetTimingAttributeStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xdd\x01\n"SetTimingAttributeTimestampRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12;\n\tattribute\x18\x02 \x01(\x0e2&.nidaqmx_grpc.TimingTimestampAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12)\n\x05value\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x10\n\x0eattribute_enum"5\n#SetTimingAttributeTimestampResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xbb\x01\n\x1fSetTimingAttributeUInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x128\n\tattribute\x18\x02 \x01(\x0e2#.nidaqmx_grpc.TimingUInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\rB\x10\n\x0eattribute_enum"2\n SetTimingAttributeUInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xbb\x01\n\x1fSetTimingAttributeUInt64Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x128\n\tattribute\x18\x02 \x01(\x0e2#.nidaqmx_grpc.TimingUInt64AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\x04B\x10\n\x0eattribute_enum"2\n SetTimingAttributeUInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb6\x01\n\x1bSetTrigAttributeBoolRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x127\n\tattribute\x18\x02 \x01(\x0e2".nidaqmx_grpc.TriggerBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\x08B\x10\n\x0eattribute_enum".\n\x1cSetTrigAttributeBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xba\x01\n\x1dSetTrigAttributeDoubleRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x129\n\tattribute\x18\x02 \x01(\x0e2$.nidaqmx_grpc.TriggerDoubleAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\x01B\x10\n\x0eattribute_enum"0\n\x1eSetTrigAttributeDoubleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc4\x01\n"SetTrigAttributeDoubleArrayRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12>\n\tattribute\x18\x02 \x01(\x0e2).nidaqmx_grpc.TriggerDoubleArrayAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x03(\x01B\x10\n\x0eattribute_enum"5\n#SetTrigAttributeDoubleArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x88\x02\n\x1cSetTrigAttributeInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x128\n\tattribute\x18\x02 \x01(\x0e2#.nidaqmx_grpc.TriggerInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12:\n\x05value\x18\x04 \x01(\x0e2).nidaqmx_grpc.TriggerInt32AttributeValuesH\x01\x12\x13\n\tvalue_raw\x18\x05 \x01(\x05H\x01B\x10\n\x0eattribute_enumB\x0c\n\nvalue_enum"/\n\x1dSetTrigAttributeInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc2\x01\n!SetTrigAttributeInt32ArrayRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12=\n\tattribute\x18\x02 \x01(\x0e2(.nidaqmx_grpc.TriggerInt32ArrayAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x03(\x05B\x10\n\x0eattribute_enum"4\n"SetTrigAttributeInt32ArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xba\x01\n\x1dSetTrigAttributeStringRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x129\n\tattribute\x18\x02 \x01(\x0e2$.nidaqmx_grpc.TriggerStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\tB\x10\n\x0eattribute_enum"0\n\x1eSetTrigAttributeStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xdc\x01\n SetTrigAttributeTimestampRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12<\n\tattribute\x18\x02 \x01(\x0e2\'.nidaqmx_grpc.TriggerTimestampAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12)\n\x05value\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x10\n\x0eattribute_enum"3\n!SetTrigAttributeTimestampResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xba\x01\n\x1dSetTrigAttributeUInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x129\n\tattribute\x18\x02 \x01(\x0e2$.nidaqmx_grpc.TriggerUInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\rB\x10\n\x0eattribute_enum"0\n\x1eSetTrigAttributeUInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xca\x01\n\x1fSetWatchdogAttributeBoolRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05lines\x18\x02 \x01(\t\x128\n\tattribute\x18\x03 \x01(\x0e2#.nidaqmx_grpc.WatchdogBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00\x12\r\n\x05value\x18\x05 \x01(\x08B\x10\n\x0eattribute_enum"2\n SetWatchdogAttributeBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xce\x01\n!SetWatchdogAttributeDoubleRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05lines\x18\x02 \x01(\t\x12:\n\tattribute\x18\x03 \x01(\x0e2%.nidaqmx_grpc.WatchdogDoubleAttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00\x12\r\n\x05value\x18\x05 \x01(\x01B\x10\n\x0eattribute_enum"4\n"SetWatchdogAttributeDoubleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x9d\x02\n SetWatchdogAttributeInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05lines\x18\x02 \x01(\t\x129\n\tattribute\x18\x03 \x01(\x0e2$.nidaqmx_grpc.WatchdogInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00\x12;\n\x05value\x18\x05 \x01(\x0e2*.nidaqmx_grpc.WatchdogInt32AttributeValuesH\x01\x12\x13\n\tvalue_raw\x18\x06 \x01(\x05H\x01B\x10\n\x0eattribute_enumB\x0c\n\nvalue_enum"3\n!SetWatchdogAttributeInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xce\x01\n!SetWatchdogAttributeStringRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05lines\x18\x02 \x01(\t\x12:\n\tattribute\x18\x03 \x01(\x0e2%.nidaqmx_grpc.WatchdogStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x04 \x01(\x05H\x00\x12\r\n\x05value\x18\x05 \x01(\tB\x10\n\x0eattribute_enum"4\n"SetWatchdogAttributeStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb5\x01\n\x1cSetWriteAttributeBoolRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x125\n\tattribute\x18\x02 \x01(\x0e2 .nidaqmx_grpc.WriteBoolAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\x08B\x10\n\x0eattribute_enum"/\n\x1dSetWriteAttributeBoolResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb9\x01\n\x1eSetWriteAttributeDoubleRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x127\n\tattribute\x18\x02 \x01(\x0e2".nidaqmx_grpc.WriteDoubleAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\x01B\x10\n\x0eattribute_enum"1\n\x1fSetWriteAttributeDoubleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x85\x02\n\x1dSetWriteAttributeInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x126\n\tattribute\x18\x02 \x01(\x0e2!.nidaqmx_grpc.WriteInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x128\n\x05value\x18\x04 \x01(\x0e2\'.nidaqmx_grpc.WriteInt32AttributeValuesH\x01\x12\x13\n\tvalue_raw\x18\x05 \x01(\x05H\x01B\x10\n\x0eattribute_enumB\x0c\n\nvalue_enum"0\n\x1eSetWriteAttributeInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb9\x01\n\x1eSetWriteAttributeStringRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x127\n\tattribute\x18\x02 \x01(\x0e2".nidaqmx_grpc.WriteStringAttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\tB\x10\n\x0eattribute_enum"1\n\x1fSetWriteAttributeStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb9\x01\n\x1eSetWriteAttributeUInt32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x127\n\tattribute\x18\x02 \x01(\x0e2".nidaqmx_grpc.WriteUInt32AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\rB\x10\n\x0eattribute_enum"1\n\x1fSetWriteAttributeUInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb9\x01\n\x1eSetWriteAttributeUInt64Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x127\n\tattribute\x18\x02 \x01(\x0e2".nidaqmx_grpc.WriteUInt64AttributeH\x00\x12\x17\n\rattribute_raw\x18\x03 \x01(\x05H\x00\x12\r\n\x05value\x18\x04 \x01(\x04B\x10\n\x0eattribute_enum"1\n\x1fSetWriteAttributeUInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"N\n\x13StartNewFileRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t"&\n\x14StartNewFileResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"8\n\x10StartTaskRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"#\n\x11StartTaskResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"7\n\x0fStopTaskRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session""\n\x10StopTaskResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x92\x01\n\x12TaskControlRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x121\n\x06action\x18\x02 \x01(\x0e2\x1f.nidaqmx_grpc.TaskControlActionH\x00\x12\x14\n\naction_raw\x18\x03 \x01(\x05H\x00B\r\n\x0baction_enum"%\n\x13TaskControlResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"4\n\x19TristateOutputTermRequest\x12\x17\n\x0foutput_terminal\x18\x01 \x01(\t",\n\x1aTristateOutputTermResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"B\n\x1aUnregisterDoneEventRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"-\n\x1bUnregisterDoneEventResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xe4\x01\n#UnregisterEveryNSamplesEventRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12J\n\x1aevery_n_samples_event_type\x18\x02 \x01(\x0e2$.nidaqmx_grpc.EveryNSamplesEventTypeH\x00\x12(\n\x1eevery_n_samples_event_type_raw\x18\x03 \x01(\x05H\x00B!\n\x1fevery_n_samples_event_type_enum"6\n$UnregisterEveryNSamplesEventResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x9b\x01\n\x1cUnregisterSignalEventRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12*\n\tsignal_id\x18\x02 \x01(\x0e2\x15.nidaqmx_grpc.Signal2H\x00\x12\x17\n\rsignal_id_raw\x18\x03 \x01(\x05H\x00B\x10\n\x0esignal_id_enum"/\n\x1dUnregisterSignalEventResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"4\n\x1dUnreserveNetworkDeviceRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t"0\n\x1eUnreserveNetworkDeviceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"V\n\x1dWaitForNextSampleClockRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07timeout\x18\x02 \x01(\x01"A\n\x1eWaitForNextSampleClockResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07is_late\x18\x02 \x01(\x08"[\n"BeginWaitForNextSampleClockRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07timeout\x18\x02 \x01(\x01"a\n#BeginWaitForNextSampleClockResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"H\n%MonikerWaitForNextSampleClockResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07is_late\x18\x02 \x01(\x08"\xc5\x01\n\x1cWaitForValidTimestampRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x127\n\x0ftimestamp_event\x18\x02 \x01(\x0e2\x1c.nidaqmx_grpc.TimestampEventH\x00\x12\x1d\n\x13timestamp_event_raw\x18\x03 \x01(\x05H\x00\x12\x0f\n\x07timeout\x18\x04 \x01(\x01B\x16\n\x14timestamp_event_enum"^\n\x1dWaitForValidTimestampResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12-\n\ttimestamp\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"V\n\x18WaitUntilTaskDoneRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0ctime_to_wait\x18\x02 \x01(\x01"+\n\x19WaitUntilTaskDoneResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xf0\x01\n\x15WriteAnalogF64Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12,\n\x0bdata_layout\x18\x05 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0fdata_layout_raw\x18\x06 \x01(\x05H\x00\x12\x13\n\x0bwrite_array\x18\x07 \x03(\x01B\x12\n\x10data_layout_enum"H\n\x16WriteAnalogF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1e\n\x16samps_per_chan_written\x18\x02 \x01(\x05"\xe0\x01\n\x1aBeginWriteAnalogF64Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12,\n\x0bdata_layout\x18\x05 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0fdata_layout_raw\x18\x06 \x01(\x05H\x00B\x12\n\x10data_layout_enum"Y\n\x1bBeginWriteAnalogF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"3\n\x1cMonikerWriteAnalogF64Request\x12\x13\n\x0bwrite_array\x18\x01 \x03(\x01"O\n\x1dMonikerWriteAnalogF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1e\n\x16samps_per_chan_written\x18\x02 \x01(\x05"w\n\x1bWriteAnalogScalarF64Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nauto_start\x18\x02 \x01(\x08\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12\r\n\x05value\x18\x04 \x01(\x01".\n\x1cWriteAnalogScalarF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"m\n BeginWriteAnalogScalarF64Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nauto_start\x18\x02 \x01(\x08\x12\x0f\n\x07timeout\x18\x03 \x01(\x01"_\n!BeginWriteAnalogScalarF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"3\n"MonikerWriteAnalogScalarF64Request\x12\r\n\x05value\x18\x01 \x01(\x01"5\n#MonikerWriteAnalogScalarF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xf0\x01\n\x15WriteBinaryI16Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12,\n\x0bdata_layout\x18\x05 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0fdata_layout_raw\x18\x06 \x01(\x05H\x00\x12\x13\n\x0bwrite_array\x18\x07 \x03(\x05B\x12\n\x10data_layout_enum"H\n\x16WriteBinaryI16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1e\n\x16samps_per_chan_written\x18\x02 \x01(\x05"\xe0\x01\n\x1aBeginWriteBinaryI16Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12,\n\x0bdata_layout\x18\x05 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0fdata_layout_raw\x18\x06 \x01(\x05H\x00B\x12\n\x10data_layout_enum"Y\n\x1bBeginWriteBinaryI16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"3\n\x1cMonikerWriteBinaryI16Request\x12\x13\n\x0bwrite_array\x18\x01 \x03(\x05"O\n\x1dMonikerWriteBinaryI16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1e\n\x16samps_per_chan_written\x18\x02 \x01(\x05"\xf0\x01\n\x15WriteBinaryI32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12,\n\x0bdata_layout\x18\x05 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0fdata_layout_raw\x18\x06 \x01(\x05H\x00\x12\x13\n\x0bwrite_array\x18\x07 \x03(\x05B\x12\n\x10data_layout_enum"H\n\x16WriteBinaryI32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1e\n\x16samps_per_chan_written\x18\x02 \x01(\x05"\xe0\x01\n\x1aBeginWriteBinaryI32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12,\n\x0bdata_layout\x18\x05 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0fdata_layout_raw\x18\x06 \x01(\x05H\x00B\x12\n\x10data_layout_enum"Y\n\x1bBeginWriteBinaryI32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"3\n\x1cMonikerWriteBinaryI32Request\x12\x13\n\x0bwrite_array\x18\x01 \x03(\x05"O\n\x1dMonikerWriteBinaryI32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1e\n\x16samps_per_chan_written\x18\x02 \x01(\x05"\xf0\x01\n\x15WriteBinaryU16Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12,\n\x0bdata_layout\x18\x05 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0fdata_layout_raw\x18\x06 \x01(\x05H\x00\x12\x13\n\x0bwrite_array\x18\x07 \x03(\rB\x12\n\x10data_layout_enum"H\n\x16WriteBinaryU16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1e\n\x16samps_per_chan_written\x18\x02 \x01(\x05"\xe0\x01\n\x1aBeginWriteBinaryU16Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12,\n\x0bdata_layout\x18\x05 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0fdata_layout_raw\x18\x06 \x01(\x05H\x00B\x12\n\x10data_layout_enum"Y\n\x1bBeginWriteBinaryU16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"3\n\x1cMonikerWriteBinaryU16Request\x12\x13\n\x0bwrite_array\x18\x01 \x03(\r"O\n\x1dMonikerWriteBinaryU16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1e\n\x16samps_per_chan_written\x18\x02 \x01(\x05"\xf0\x01\n\x15WriteBinaryU32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12,\n\x0bdata_layout\x18\x05 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0fdata_layout_raw\x18\x06 \x01(\x05H\x00\x12\x13\n\x0bwrite_array\x18\x07 \x03(\rB\x12\n\x10data_layout_enum"H\n\x16WriteBinaryU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1e\n\x16samps_per_chan_written\x18\x02 \x01(\x05"\xe0\x01\n\x1aBeginWriteBinaryU32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12,\n\x0bdata_layout\x18\x05 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0fdata_layout_raw\x18\x06 \x01(\x05H\x00B\x12\n\x10data_layout_enum"Y\n\x1bBeginWriteBinaryU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"3\n\x1cMonikerWriteBinaryU32Request\x12\x13\n\x0bwrite_array\x18\x01 \x03(\r"O\n\x1dMonikerWriteBinaryU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1e\n\x16samps_per_chan_written\x18\x02 \x01(\x05"\x80\x02\n\x13WriteCtrFreqRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12,\n\x0bdata_layout\x18\x05 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0fdata_layout_raw\x18\x06 \x01(\x05H\x00\x12\x11\n\tfrequency\x18\x07 \x03(\x01\x12\x12\n\nduty_cycle\x18\x08 \x03(\x01B\x12\n\x10data_layout_enum"J\n\x14WriteCtrFreqResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x1anum_samps_per_chan_written\x18\x02 \x01(\x05"\xde\x01\n\x18BeginWriteCtrFreqRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12,\n\x0bdata_layout\x18\x05 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0fdata_layout_raw\x18\x06 \x01(\x05H\x00B\x12\n\x10data_layout_enum"W\n\x19BeginWriteCtrFreqResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"C\n\x1aMonikerWriteCtrFreqRequest\x12\x11\n\tfrequency\x18\x01 \x03(\x01\x12\x12\n\nduty_cycle\x18\x02 \x03(\x01"Q\n\x1bMonikerWriteCtrFreqResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x1anum_samps_per_chan_written\x18\x02 \x01(\x05"\x8d\x01\n\x19WriteCtrFreqScalarRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nauto_start\x18\x02 \x01(\x08\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12\x11\n\tfrequency\x18\x04 \x01(\x01\x12\x12\n\nduty_cycle\x18\x05 \x01(\x01",\n\x1aWriteCtrFreqScalarResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"k\n\x1eBeginWriteCtrFreqScalarRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nauto_start\x18\x02 \x01(\x08\x12\x0f\n\x07timeout\x18\x03 \x01(\x01"]\n\x1fBeginWriteCtrFreqScalarResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"I\n MonikerWriteCtrFreqScalarRequest\x12\x11\n\tfrequency\x18\x01 \x01(\x01\x12\x12\n\nduty_cycle\x18\x02 \x01(\x01"3\n!MonikerWriteCtrFreqScalarResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x81\x02\n\x14WriteCtrTicksRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12,\n\x0bdata_layout\x18\x05 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0fdata_layout_raw\x18\x06 \x01(\x05H\x00\x12\x12\n\nhigh_ticks\x18\x07 \x03(\r\x12\x11\n\tlow_ticks\x18\x08 \x03(\rB\x12\n\x10data_layout_enum"K\n\x15WriteCtrTicksResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x1anum_samps_per_chan_written\x18\x02 \x01(\x05"\xdf\x01\n\x19BeginWriteCtrTicksRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12,\n\x0bdata_layout\x18\x05 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0fdata_layout_raw\x18\x06 \x01(\x05H\x00B\x12\n\x10data_layout_enum"X\n\x1aBeginWriteCtrTicksResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"D\n\x1bMonikerWriteCtrTicksRequest\x12\x12\n\nhigh_ticks\x18\x01 \x03(\r\x12\x11\n\tlow_ticks\x18\x02 \x03(\r"R\n\x1cMonikerWriteCtrTicksResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x1anum_samps_per_chan_written\x18\x02 \x01(\x05"\x8e\x01\n\x1aWriteCtrTicksScalarRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nauto_start\x18\x02 \x01(\x08\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12\x12\n\nhigh_ticks\x18\x04 \x01(\r\x12\x11\n\tlow_ticks\x18\x05 \x01(\r"-\n\x1bWriteCtrTicksScalarResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"l\n\x1fBeginWriteCtrTicksScalarRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nauto_start\x18\x02 \x01(\x08\x12\x0f\n\x07timeout\x18\x03 \x01(\x01"^\n BeginWriteCtrTicksScalarResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"J\n!MonikerWriteCtrTicksScalarRequest\x12\x12\n\nhigh_ticks\x18\x01 \x01(\r\x12\x11\n\tlow_ticks\x18\x02 \x01(\r"4\n"MonikerWriteCtrTicksScalarResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xfe\x01\n\x13WriteCtrTimeRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12,\n\x0bdata_layout\x18\x05 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0fdata_layout_raw\x18\x06 \x01(\x05H\x00\x12\x11\n\thigh_time\x18\x07 \x03(\x01\x12\x10\n\x08low_time\x18\x08 \x03(\x01B\x12\n\x10data_layout_enum"J\n\x14WriteCtrTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x1anum_samps_per_chan_written\x18\x02 \x01(\x05"\xde\x01\n\x18BeginWriteCtrTimeRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12,\n\x0bdata_layout\x18\x05 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0fdata_layout_raw\x18\x06 \x01(\x05H\x00B\x12\n\x10data_layout_enum"W\n\x19BeginWriteCtrTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"A\n\x1aMonikerWriteCtrTimeRequest\x12\x11\n\thigh_time\x18\x01 \x03(\x01\x12\x10\n\x08low_time\x18\x02 \x03(\x01"Q\n\x1bMonikerWriteCtrTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x1anum_samps_per_chan_written\x18\x02 \x01(\x05"\x8b\x01\n\x19WriteCtrTimeScalarRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nauto_start\x18\x02 \x01(\x08\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12\x11\n\thigh_time\x18\x04 \x01(\x01\x12\x10\n\x08low_time\x18\x05 \x01(\x01",\n\x1aWriteCtrTimeScalarResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"k\n\x1eBeginWriteCtrTimeScalarRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nauto_start\x18\x02 \x01(\x08\x12\x0f\n\x07timeout\x18\x03 \x01(\x01"]\n\x1fBeginWriteCtrTimeScalarResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"G\n MonikerWriteCtrTimeScalarRequest\x12\x11\n\thigh_time\x18\x01 \x01(\x01\x12\x10\n\x08low_time\x18\x02 \x01(\x01"3\n!MonikerWriteCtrTimeScalarResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xf3\x01\n\x18WriteDigitalLinesRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12,\n\x0bdata_layout\x18\x05 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0fdata_layout_raw\x18\x06 \x01(\x05H\x00\x12\x13\n\x0bwrite_array\x18\x07 \x01(\x0cB\x12\n\x10data_layout_enum"K\n\x19WriteDigitalLinesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1e\n\x16samps_per_chan_written\x18\x02 \x01(\x05"\xe3\x01\n\x1dBeginWriteDigitalLinesRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12,\n\x0bdata_layout\x18\x05 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0fdata_layout_raw\x18\x06 \x01(\x05H\x00B\x12\n\x10data_layout_enum"\\\n\x1eBeginWriteDigitalLinesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"6\n\x1fMonikerWriteDigitalLinesRequest\x12\x13\n\x0bwrite_array\x18\x01 \x01(\x0c"R\n MonikerWriteDigitalLinesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1e\n\x16samps_per_chan_written\x18\x02 \x01(\x05"x\n\x1cWriteDigitalScalarU32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nauto_start\x18\x02 \x01(\x08\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12\r\n\x05value\x18\x04 \x01(\r"/\n\x1dWriteDigitalScalarU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"n\n!BeginWriteDigitalScalarU32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nauto_start\x18\x02 \x01(\x08\x12\x0f\n\x07timeout\x18\x03 \x01(\x01"`\n"BeginWriteDigitalScalarU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"4\n#MonikerWriteDigitalScalarU32Request\x12\r\n\x05value\x18\x01 \x01(\r"6\n$MonikerWriteDigitalScalarU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xf1\x01\n\x16WriteDigitalU16Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12,\n\x0bdata_layout\x18\x05 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0fdata_layout_raw\x18\x06 \x01(\x05H\x00\x12\x13\n\x0bwrite_array\x18\x07 \x03(\rB\x12\n\x10data_layout_enum"I\n\x17WriteDigitalU16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1e\n\x16samps_per_chan_written\x18\x02 \x01(\x05"\xe1\x01\n\x1bBeginWriteDigitalU16Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12,\n\x0bdata_layout\x18\x05 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0fdata_layout_raw\x18\x06 \x01(\x05H\x00B\x12\n\x10data_layout_enum"Z\n\x1cBeginWriteDigitalU16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"4\n\x1dMonikerWriteDigitalU16Request\x12\x13\n\x0bwrite_array\x18\x01 \x03(\r"P\n\x1eMonikerWriteDigitalU16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1e\n\x16samps_per_chan_written\x18\x02 \x01(\x05"\xf1\x01\n\x16WriteDigitalU32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12,\n\x0bdata_layout\x18\x05 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0fdata_layout_raw\x18\x06 \x01(\x05H\x00\x12\x13\n\x0bwrite_array\x18\x07 \x03(\rB\x12\n\x10data_layout_enum"I\n\x17WriteDigitalU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1e\n\x16samps_per_chan_written\x18\x02 \x01(\x05"\xe1\x01\n\x1bBeginWriteDigitalU32Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12,\n\x0bdata_layout\x18\x05 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0fdata_layout_raw\x18\x06 \x01(\x05H\x00B\x12\n\x10data_layout_enum"Z\n\x1cBeginWriteDigitalU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"4\n\x1dMonikerWriteDigitalU32Request\x12\x13\n\x0bwrite_array\x18\x01 \x03(\r"P\n\x1eMonikerWriteDigitalU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1e\n\x16samps_per_chan_written\x18\x02 \x01(\x05"\xf0\x01\n\x15WriteDigitalU8Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12,\n\x0bdata_layout\x18\x05 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0fdata_layout_raw\x18\x06 \x01(\x05H\x00\x12\x13\n\x0bwrite_array\x18\x07 \x01(\x0cB\x12\n\x10data_layout_enum"H\n\x16WriteDigitalU8Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1e\n\x16samps_per_chan_written\x18\x02 \x01(\x05"\xe0\x01\n\x1aBeginWriteDigitalU8Request\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12,\n\x0bdata_layout\x18\x05 \x01(\x0e2\x15.nidaqmx_grpc.GroupByH\x00\x12\x19\n\x0fdata_layout_raw\x18\x06 \x01(\x05H\x00B\x12\n\x10data_layout_enum"Y\n\x1bBeginWriteDigitalU8Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"3\n\x1cMonikerWriteDigitalU8Request\x12\x13\n\x0bwrite_array\x18\x01 \x01(\x0c"O\n\x1dMonikerWriteDigitalU8Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1e\n\x16samps_per_chan_written\x18\x02 \x01(\x05"f\n\x17WriteIDPinMemoryRequest\x12\x13\n\x0bdevice_name\x18\x01 \x01(\t\x12\x13\n\x0bid_pin_name\x18\x02 \x01(\t\x12\x0c\n\x04data\x18\x03 \x01(\x0c\x12\x13\n\x0bformat_code\x18\x04 \x01(\r"*\n\x18WriteIDPinMemoryResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x84\x01\n\x0fWriteRawRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tnum_samps\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01\x12\x13\n\x0bwrite_array\x18\x05 \x01(\x0c"B\n\x10WriteRawResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1e\n\x16samps_per_chan_written\x18\x02 \x01(\x05"t\n\x14BeginWriteRawRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tnum_samps\x18\x02 \x01(\x05\x12\x12\n\nauto_start\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\x01"S\n\x15BeginWriteRawResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x07moniker\x18\x02 \x01(\x0b2\x19.ni.data_monikers.Moniker"-\n\x16MonikerWriteRawRequest\x12\x13\n\x0bwrite_array\x18\x01 \x01(\x0c"I\n\x17MonikerWriteRawResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1e\n\x16samps_per_chan_written\x18\x02 \x01(\x05"\xcb\x01\n\x1bWriteToTEDSFromArrayRequest\x12\x18\n\x10physical_channel\x18\x01 \x01(\t\x12\x12\n\nbit_stream\x18\x02 \x01(\x0c\x12A\n\x12basic_teds_options\x18\x03 \x01(\x0e2#.nidaqmx_grpc.WriteBasicTEDSOptionsH\x00\x12 \n\x16basic_teds_options_raw\x18\x04 \x01(\x05H\x00B\x19\n\x17basic_teds_options_enum".\n\x1cWriteToTEDSFromArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc9\x01\n\x1aWriteToTEDSFromFileRequest\x12\x18\n\x10physical_channel\x18\x01 \x01(\t\x12\x11\n\tfile_path\x18\x02 \x01(\t\x12A\n\x12basic_teds_options\x18\x03 \x01(\x0e2#.nidaqmx_grpc.WriteBasicTEDSOptionsH\x00\x12 \n\x16basic_teds_options_raw\x18\x04 \x01(\x05H\x00B\x19\n\x17basic_teds_options_enum"-\n\x1bWriteToTEDSFromFileResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xfe\x01\n\x1aReadAnalogWaveformsRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12F\n\x17waveform_attribute_mode\x18\x04 \x01(\x0e2#.nidaqmx_grpc.WaveformAttributeModeH\x00\x12%\n\x1bwaveform_attribute_mode_raw\x18\x05 \x01(\x05H\x00B\x1e\n\x1cwaveform_attribute_mode_enum"\x86\x01\n\x1bReadAnalogWaveformsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12:\n\twaveforms\x18\x02 \x03(\x0b2\'.ni.protobuf.types.DoubleAnalogWaveform\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"\xff\x01\n\x1bReadDigitalWaveformsRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12num_samps_per_chan\x18\x02 \x01(\x05\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12F\n\x17waveform_attribute_mode\x18\x04 \x01(\x0e2#.nidaqmx_grpc.WaveformAttributeModeH\x00\x12%\n\x1bwaveform_attribute_mode_raw\x18\x05 \x01(\x05H\x00B\x1e\n\x1cwaveform_attribute_mode_enum"\x82\x01\n\x1cReadDigitalWaveformsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x125\n\twaveforms\x18\x02 \x03(\x0b2".ni.protobuf.types.DigitalWaveform\x12\x1b\n\x13samps_per_chan_read\x18\x03 \x01(\x05"\xa4\x01\n\x1bWriteAnalogWaveformsRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nauto_start\x18\x02 \x01(\x08\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12:\n\twaveforms\x18\x04 \x03(\x0b2\'.ni.protobuf.types.DoubleAnalogWaveform"N\n\x1cWriteAnalogWaveformsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1e\n\x16samps_per_chan_written\x18\x02 \x01(\x05"\xa0\x01\n\x1cWriteDigitalWaveformsRequest\x12$\n\x04task\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nauto_start\x18\x02 \x01(\x08\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x125\n\twaveforms\x18\x04 \x03(\x0b2".ni.protobuf.types.DigitalWaveform"O\n\x1dWriteDigitalWaveformsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1e\n\x16samps_per_chan_written\x18\x02 \x01(\x05*\xe6\x01\n\x15BufferUInt32Attribute\x12\'\n#BUFFER_UINT32_ATTRIBUTE_UNSPECIFIED\x10\x00\x12$\n\x1fBUFFER_ATTRIBUTE_INPUT_BUF_SIZE\x10\xec0\x12%\n BUFFER_ATTRIBUTE_OUTPUT_BUF_SIZE\x10\xed0\x12*\n%BUFFER_ATTRIBUTE_INPUT_ONBRD_BUF_SIZE\x10\x8aF\x12+\n&BUFFER_ATTRIBUTE_OUTPUT_ONBRD_BUF_SIZE\x10\x8bF*\xca\x01\n\x14BufferResetAttribute\x12&\n"BUFFER_RESET_ATTRIBUTE_UNSPECIFIED\x10\x00\x12*\n%BUFFER_RESET_ATTRIBUTE_INPUT_BUF_SIZE\x10\xec0\x12+\n&BUFFER_RESET_ATTRIBUTE_OUTPUT_BUF_SIZE\x10\xed0\x121\n,BUFFER_RESET_ATTRIBUTE_OUTPUT_ONBRD_BUF_SIZE\x10\x8bF*\x81\x01\n\x1cCalibrationInfoBoolAttribute\x12.\n*CALIBRATIONINFO_BOOL_ATTRIBUTE_UNSPECIFIED\x10\x00\x121\n,CALIBRATIONINFO_ATTRIBUTE_SELF_CAL_SUPPORTED\x10\xe00*\x88\x01\n\x1eCalibrationInfoStringAttribute\x120\n,CALIBRATIONINFO_STRING_ATTRIBUTE_UNSPECIFIED\x10\x00\x124\n/CALIBRATIONINFO_ATTRIBUTE_CAL_USER_DEFINED_INFO\x10\xe10*\xe4\x01\n\x1eCalibrationInfoDoubleAttribute\x120\n,CALIBRATIONINFO_DOUBLE_ATTRIBUTE_UNSPECIFIED\x10\x00\x121\n,CALIBRATIONINFO_ATTRIBUTE_SELF_CAL_LAST_TEMP\x10\xe40\x120\n+CALIBRATIONINFO_ATTRIBUTE_EXT_CAL_LAST_TEMP\x10\xe70\x12+\n&CALIBRATIONINFO_ATTRIBUTE_CAL_DEV_TEMP\x10\xbbD*\xd2\x02\n\x1eCalibrationInfoUInt32Attribute\x120\n,CALIBRATIONINFO_UINT32_ATTRIBUTE_UNSPECIFIED\x10\x00\x12;\n6CALIBRATIONINFO_ATTRIBUTE_EXT_CAL_RECOMMENDED_INTERVAL\x10\xe80\x12=\n8CALIBRATIONINFO_ATTRIBUTE_CAL_USER_DEFINED_INFO_MAX_SIZE\x10\x9c2\x127\n2CALIBRATIONINFO_ATTRIBUTE_CAL_ACC_CONNECTION_COUNT\x10\xeb_\x12I\nDCALIBRATIONINFO_ATTRIBUTE_CAL_RECOMMENDED_ACC_CONNECTION_COUNT_LIMIT\x10\xec_*\xefK\n\x15ChannelInt32Attribute\x12\'\n#CHANNEL_INT32_ATTRIBUTE_UNSPECIFIED\x10\x00\x12/\n+CHANNEL_ATTRIBUTE_AI_RAW_SAMP_JUSTIFICATION\x10P\x12!\n\x1dCHANNEL_ATTRIBUTE_AI_COUPLING\x10d\x12$\n\x1fCHANNEL_ATTRIBUTE_AI_BRIDGE_CFG\x10\x87\x01\x12%\n CHANNEL_ATTRIBUTE_AO_DAC_REF_SRC\x10\xb2\x02\x12(\n#CHANNEL_ATTRIBUTE_AO_DATA_XFER_MECH\x10\xb4\x02\x122\n-CHANNEL_ATTRIBUTE_CI_CTR_TIMEBASE_ACTIVE_EDGE\x10\xc2\x02\x12(\n#CHANNEL_ATTRIBUTE_CI_FREQ_MEAS_METH\x10\xc4\x02\x12&\n!CHANNEL_ATTRIBUTE_CI_OUTPUT_STATE\x10\xc9\x02\x12(\n#CHANNEL_ATTRIBUTE_CI_DATA_XFER_MECH\x10\x80\x04\x12&\n!CHANNEL_ATTRIBUTE_CO_OUTPUT_STATE\x10\x94\x05\x122\n-CHANNEL_ATTRIBUTE_CO_CTR_TIMEBASE_ACTIVE_EDGE\x10\xc1\x06\x12%\n CHANNEL_ATTRIBUTE_AI_ACCEL_UNITS\x10\xf3\x0c\x12#\n\x1eCHANNEL_ATTRIBUTE_AI_MEAS_TYPE\x10\x95\r\x12)\n$CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_DIR\x10\x96\r\x121\n,CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_ACTIVE_EDGE\x10\x97\r\x12\'\n"CHANNEL_ATTRIBUTE_AI_CURRENT_UNITS\x10\x81\x0e\x12,\n\'CHANNEL_ATTRIBUTE_CI_FREQ_STARTING_EDGE\x10\x99\x0f\x12$\n\x1fCHANNEL_ATTRIBUTE_AI_FREQ_UNITS\x10\x86\x10\x12+\n&CHANNEL_ATTRIBUTE_CI_PULSE_WIDTH_UNITS\x10\xa3\x10\x123\n.CHANNEL_ATTRIBUTE_CI_PULSE_WIDTH_STARTING_EDGE\x10\xa5\x10\x121\n,CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_EDGE\x10\xb3\x10\x122\n-CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_EDGE\x10\xb4\x10\x12.\n)CHANNEL_ATTRIBUTE_CI_PERIOD_STARTING_EDGE\x10\xd2\x10\x12$\n\x1fCHANNEL_ATTRIBUTE_AI_RVDT_UNITS\x10\xf7\x10\x12/\n*CHANNEL_ATTRIBUTE_CI_ENCODER_Z_INDEX_PHASE\x10\x89\x11\x12$\n\x1fCHANNEL_ATTRIBUTE_AI_LVDT_UNITS\x10\x90\x12\x12*\n%CHANNEL_ATTRIBUTE_AI_RESISTANCE_UNITS\x10\xd5\x12\x12&\n!CHANNEL_ATTRIBUTE_AI_STRAIN_UNITS\x10\x81\x13\x12)\n$CHANNEL_ATTRIBUTE_AI_STRAIN_GAGE_CFG\x10\x82\x13\x12"\n\x1dCHANNEL_ATTRIBUTE_AI_RTD_TYPE\x10\xb2 \x12$\n\x1fCHANNEL_ATTRIBUTE_AI_TEMP_UNITS\x10\xb3 \x12)\n$CHANNEL_ATTRIBUTE_AI_THRMCPL_CJC_SRC\x10\xb5 \x12&\n!CHANNEL_ATTRIBUTE_AI_THRMCPL_TYPE\x10\xd0 \x12)\n$CHANNEL_ATTRIBUTE_CI_GPS_SYNC_METHOD\x10\x92!\x12\'\n"CHANNEL_ATTRIBUTE_AI_VOLTAGE_UNITS\x10\x94!\x12"\n\x1dCHANNEL_ATTRIBUTE_AI_TERM_CFG\x10\x97!\x12%\n CHANNEL_ATTRIBUTE_AO_OUTPUT_TYPE\x10\x88"\x12\'\n"CHANNEL_ATTRIBUTE_AO_CURRENT_UNITS\x10\x89"\x12+\n&CHANNEL_ATTRIBUTE_DO_OUTPUT_DRIVE_TYPE\x10\xb7"\x12*\n%CHANNEL_ATTRIBUTE_CO_PULSE_IDLE_STATE\x10\xf0"\x12\'\n"CHANNEL_ATTRIBUTE_AO_VOLTAGE_UNITS\x10\x84#\x12.\n)CHANNEL_ATTRIBUTE_AI_SOUND_PRESSURE_UNITS\x10\xa8*\x12(\n#CHANNEL_ATTRIBUTE_AI_AUTO_ZERO_MODE\x10\xe0.\x12*\n%CHANNEL_ATTRIBUTE_AI_RESOLUTION_UNITS\x10\xe4.\x12-\n(CHANNEL_ATTRIBUTE_AI_VOLTAGE_ACRMS_UNITS\x10\xe2/\x12-\n(CHANNEL_ATTRIBUTE_AI_CURRENT_ACRMS_UNITS\x10\xe3/\x123\n.CHANNEL_ATTRIBUTE_AI_BRIDGE_BALANCE_COARSE_POT\x10\xf1/\x12+\n&CHANNEL_ATTRIBUTE_AI_CURRENT_SHUNT_LOC\x10\xf2/\x12#\n\x1eCHANNEL_ATTRIBUTE_AI_EXCIT_SRC\x10\xf4/\x122\n-CHANNEL_ATTRIBUTE_AI_EXCIT_VOLTAGE_OR_CURRENT\x10\xf6/\x12(\n#CHANNEL_ATTRIBUTE_AI_EXCIT_D_COR_AC\x10\xfb/\x12\'\n"CHANNEL_ATTRIBUTE_AI_HIGHPASS_TYPE\x10\x880\x12\'\n"CHANNEL_ATTRIBUTE_AI_BANDPASS_TYPE\x10\x8d0\x12$\n\x1fCHANNEL_ATTRIBUTE_AI_NOTCH_TYPE\x10\x910\x12(\n#CHANNEL_ATTRIBUTE_AI_DATA_XFER_MECH\x10\xa10\x12*\n%CHANNEL_ATTRIBUTE_AO_RESOLUTION_UNITS\x10\xab0\x12,\n\'CHANNEL_ATTRIBUTE_AO_DATA_XFER_REQ_COND\x10\xbc0\x12 \n\x1bCHANNEL_ATTRIBUTE_CHAN_TYPE\x10\xff0\x12(\n#CHANNEL_ATTRIBUTE_AI_RESISTANCE_CFG\x10\x811\x124\n/CHANNEL_ATTRIBUTE_AI_LOWPASS_SWITCH_CAP_CLK_SRC\x10\x841\x12,\n\'CHANNEL_ATTRIBUTE_AI_DATA_XFER_REQ_COND\x10\x8b1\x12"\n\x1dCHANNEL_ATTRIBUTE_AO_TERM_CFG\x10\x8e1\x12#\n\x1eCHANNEL_ATTRIBUTE_CI_MEAS_TYPE\x10\xa01\x12$\n\x1fCHANNEL_ATTRIBUTE_CI_FREQ_UNITS\x10\xa11\x12&\n!CHANNEL_ATTRIBUTE_CI_PERIOD_UNITS\x10\xa31\x12+\n&CHANNEL_ATTRIBUTE_CI_ANG_ENCODER_UNITS\x10\xa61\x12+\n&CHANNEL_ATTRIBUTE_CI_LIN_ENCODER_UNITS\x10\xa91\x12,\n\'CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_UNITS\x10\xac1\x12+\n&CHANNEL_ATTRIBUTE_CI_SEMI_PERIOD_UNITS\x10\xaf1\x12%\n CHANNEL_ATTRIBUTE_CO_OUTPUT_TYPE\x10\xb51\x12,\n\'CHANNEL_ATTRIBUTE_AI_AC_EXCIT_WIRE_MODE\x10\xcd1\x12*\n%CHANNEL_ATTRIBUTE_CO_PULSE_FREQ_UNITS\x10\xd51\x12*\n%CHANNEL_ATTRIBUTE_CO_PULSE_TIME_UNITS\x10\xd61\x121\n,CHANNEL_ATTRIBUTE_AI_BRIDGE_BALANCE_FINE_POT\x10\xf41\x12*\n%CHANNEL_ATTRIBUTE_CI_PERIOD_MEAS_METH\x10\xac2\x120\n+CHANNEL_ATTRIBUTE_AI_LVDT_SENSITIVITY_UNITS\x10\x9aC\x120\n+CHANNEL_ATTRIBUTE_AI_RVDT_SENSITIVITY_UNITS\x10\x9bC\x121\n,CHANNEL_ATTRIBUTE_AI_ACCEL_SENSITIVITY_UNITS\x10\x9cC\x121\n,CHANNEL_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SELECT\x10\xd5C\x12/\n*CHANNEL_ATTRIBUTE_CI_ENCODER_DECODING_TYPE\x10\xe6C\x12.\n)CHANNEL_ATTRIBUTE_AO_IDLE_OUTPUT_BEHAVIOR\x10\xc0D\x12(\n#CHANNEL_ATTRIBUTE_AO_DAC_OFFSET_SRC\x10\xd3D\x12(\n#CHANNEL_ATTRIBUTE_DI_DATA_XFER_MECH\x10\xe3D\x12,\n\'CHANNEL_ATTRIBUTE_DI_DATA_XFER_REQ_COND\x10\xe4D\x12(\n#CHANNEL_ATTRIBUTE_DO_DATA_XFER_MECH\x10\xe6D\x12,\n\'CHANNEL_ATTRIBUTE_DO_DATA_XFER_REQ_COND\x10\xe7D\x12-\n(CHANNEL_ATTRIBUTE_AI_CHAN_CAL_SCALE_TYPE\x10\x9cE\x12)\n$CHANNEL_ATTRIBUTE_CI_TIMESTAMP_UNITS\x10\xb3E\x123\n.CHANNEL_ATTRIBUTE_AI_RAW_DATA_COMPRESSION_TYPE\x10\xd8E\x123\n.CHANNEL_ATTRIBUTE_CI_SEMI_PERIOD_STARTING_EDGE\x10\xfeE\x12$\n\x1fCHANNEL_ATTRIBUTE_DI_ACQUIRE_ON\x10\xe6R\x122\n-CHANNEL_ATTRIBUTE_DO_LINE_STATES_PAUSED_STATE\x10\xe7R\x120\n+CHANNEL_ATTRIBUTE_DO_LINE_STATES_DONE_STATE\x10\xe8R\x12%\n CHANNEL_ATTRIBUTE_DO_GENERATE_ON\x10\xe9R\x12&\n!CHANNEL_ATTRIBUTE_DI_LOGIC_FAMILY\x10\xedR\x12&\n!CHANNEL_ATTRIBUTE_DO_LOGIC_FAMILY\x10\xeeR\x121\n,CHANNEL_ATTRIBUTE_DO_LINE_STATES_START_STATE\x10\xf2R\x12,\n\'CHANNEL_ATTRIBUTE_AI_THRMCPL_SCALE_TYPE\x10\xd0S\x12.\n)CHANNEL_ATTRIBUTE_CO_CONSTRAINED_GEN_MODE\x10\xf2S\x12)\n$CHANNEL_ATTRIBUTE_AI_ADC_TIMING_MODE\x10\xf9S\x12\'\n"CHANNEL_ATTRIBUTE_AO_FUNC_GEN_TYPE\x10\x98T\x122\n-CHANNEL_ATTRIBUTE_AO_FUNC_GEN_MODULATION_TYPE\x10\xa2T\x12C\n>CHANNEL_ATTRIBUTE_AI_EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS\x10\xbfU\x127\n2CHANNEL_ATTRIBUTE_AI_EDDY_CURRENT_PROX_PROBE_UNITS\x10\xc0U\x12(\n#CHANNEL_ATTRIBUTE_CO_DATA_XFER_MECH\x10\xcc]\x12,\n\'CHANNEL_ATTRIBUTE_CO_DATA_XFER_REQ_COND\x10\xcd]\x12,\n\'CHANNEL_ATTRIBUTE_CI_DATA_XFER_REQ_COND\x10\xfb]\x12/\n*CHANNEL_ATTRIBUTE_CI_PULSE_FREQ_START_EDGE\x10\x85^\x12*\n%CHANNEL_ATTRIBUTE_CI_PULSE_FREQ_UNITS\x10\x8b^\x12/\n*CHANNEL_ATTRIBUTE_CI_PULSE_TIME_START_EDGE\x10\x8d^\x12*\n%CHANNEL_ATTRIBUTE_CI_PULSE_TIME_UNITS\x10\x93^\x120\n+CHANNEL_ATTRIBUTE_CI_PULSE_TICKS_START_EDGE\x10\x95^\x12%\n CHANNEL_ATTRIBUTE_AI_FORCE_UNITS\x10\xf5^\x12(\n#CHANNEL_ATTRIBUTE_AI_PRESSURE_UNITS\x10\xf6^\x12&\n!CHANNEL_ATTRIBUTE_AI_TORQUE_UNITS\x10\xf7^\x12=\n8CHANNEL_ATTRIBUTE_AI_FORCE_IEPE_SENSOR_SENSITIVITY_UNITS\x10\x82_\x121\n,CHANNEL_ATTRIBUTE_AI_BRIDGE_ELECTRICAL_UNITS\x10\x87_\x12/\n*CHANNEL_ATTRIBUTE_AI_BRIDGE_PHYSICAL_UNITS\x10\x88_\x12+\n&CHANNEL_ATTRIBUTE_AI_BRIDGE_SCALE_TYPE\x10\x89_\x12&\n!CHANNEL_ATTRIBUTE_AI_BRIDGE_UNITS\x10\x92_\x12=\n8CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_ACTIVE_EDGE\x10\xb2_\x12(\n#CHANNEL_ATTRIBUTE_AI_VELOCITY_UNITS\x10\xf4_\x12@\n;CHANNEL_ATTRIBUTE_AI_VELOCITY_IEPE_SENSOR_SENSITIVITY_UNITS\x10\xf7_\x12?\n:CHANNEL_ATTRIBUTE_AI_ROSETTE_STRAIN_GAGE_ROSETTE_MEAS_TYPE\x10\xfd_\x12:\n5CHANNEL_ATTRIBUTE_AI_ROSETTE_STRAIN_GAGE_ROSETTE_TYPE\x10\xfe_\x12(\n#CHANNEL_ATTRIBUTE_CI_TIMESTAMP_EDGE\x10\xba`\x12-\n(CHANNEL_ATTRIBUTE_CI_TIMESTAMP_TIMESCALE\x10\xbb`\x12$\n\x1fCHANNEL_ATTRIBUTE_NAV_MEAS_TYPE\x10\xbd`\x12$\n\x1fCHANNEL_ATTRIBUTE_NAV_ALT_UNITS\x10\xbe`\x12$\n\x1fCHANNEL_ATTRIBUTE_NAV_LAT_UNITS\x10\xbf`\x12%\n CHANNEL_ATTRIBUTE_NAV_LONG_UNITS\x10\xc0`\x122\n-CHANNEL_ATTRIBUTE_NAV_SPEED_OVER_GROUND_UNITS\x10\xc1`\x12&\n!CHANNEL_ATTRIBUTE_NAV_TRACK_UNITS\x10\xc2`\x12.\n)CHANNEL_ATTRIBUTE_NAV_VERT_VELOCITY_UNITS\x10\xc3`\x12*\n%CHANNEL_ATTRIBUTE_NAV_TIMESTAMP_UNITS\x10\xc4`\x12.\n)CHANNEL_ATTRIBUTE_NAV_TIMESTAMP_TIMESCALE\x10\xc5`\x12,\n\'CHANNEL_ATTRIBUTE_AI_FILTER_DELAY_UNITS\x10\xf1`\x12,\n\'CHANNEL_ATTRIBUTE_AO_FILTER_DELAY_UNITS\x10\xf6`\x122\n-CHANNEL_ATTRIBUTE_CI_DUTY_CYCLE_STARTING_EDGE\x10\x92a\x123\n.CHANNEL_ATTRIBUTE_CI_SAMP_CLK_OVERRUN_BEHAVIOR\x10\x93a\x127\n2CHANNEL_ATTRIBUTE_CI_SAMP_CLK_OVERRUN_SENTINEL_VAL\x10\x94a\x12\'\n"CHANNEL_ATTRIBUTE_CI_FREQ_TERM_CFG\x10\x97a\x121\n,CHANNEL_ATTRIBUTE_CI_FREQ_LOGIC_LVL_BEHAVIOR\x10\x98a\x12)\n$CHANNEL_ATTRIBUTE_CI_PERIOD_TERM_CFG\x10\x99a\x123\n.CHANNEL_ATTRIBUTE_CI_PERIOD_LOGIC_LVL_BEHAVIOR\x10\x9aa\x12.\n)CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_TERM_CFG\x10\x9ba\x128\n3CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_LOGIC_LVL_BEHAVIOR\x10\x9ca\x128\n3CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_TERM_CFG\x10\x9da\x12B\n=CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_LOGIC_LVL_BEHAVIOR\x10\x9ea\x12:\n5CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_TERM_CFG\x10\x9fa\x12D\n?CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_LOGIC_LVL_BEHAVIOR\x10\xa0a\x12-\n(CHANNEL_ATTRIBUTE_CI_DUTY_CYCLE_TERM_CFG\x10\xa1a\x127\n2CHANNEL_ATTRIBUTE_CI_DUTY_CYCLE_LOGIC_LVL_BEHAVIOR\x10\xa2a\x122\n-CHANNEL_ATTRIBUTE_CI_ENCODER_A_INPUT_TERM_CFG\x10\xa3a\x12<\n7CHANNEL_ATTRIBUTE_CI_ENCODER_A_INPUT_LOGIC_LVL_BEHAVIOR\x10\xa4a\x122\n-CHANNEL_ATTRIBUTE_CI_ENCODER_B_INPUT_TERM_CFG\x10\xa5a\x12<\n7CHANNEL_ATTRIBUTE_CI_ENCODER_B_INPUT_LOGIC_LVL_BEHAVIOR\x10\xa6a\x122\n-CHANNEL_ATTRIBUTE_CI_ENCODER_Z_INPUT_TERM_CFG\x10\xa7a\x12<\n7CHANNEL_ATTRIBUTE_CI_ENCODER_Z_INPUT_LOGIC_LVL_BEHAVIOR\x10\xa8a\x12.\n)CHANNEL_ATTRIBUTE_CI_PULSE_WIDTH_TERM_CFG\x10\xa9a\x128\n3CHANNEL_ATTRIBUTE_CI_PULSE_WIDTH_LOGIC_LVL_BEHAVIOR\x10\xaaa\x125\n0CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_TERM_CFG\x10\xaba\x12?\n:CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_LOGIC_LVL_BEHAVIOR\x10\xaca\x126\n1CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_TERM_CFG\x10\xada\x12@\n;CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_LOGIC_LVL_BEHAVIOR\x10\xaea\x12.\n)CHANNEL_ATTRIBUTE_CI_SEMI_PERIOD_TERM_CFG\x10\xafa\x128\n3CHANNEL_ATTRIBUTE_CI_SEMI_PERIOD_LOGIC_LVL_BEHAVIOR\x10\xb0a\x12-\n(CHANNEL_ATTRIBUTE_CI_PULSE_FREQ_TERM_CFG\x10\xb1a\x127\n2CHANNEL_ATTRIBUTE_CI_PULSE_FREQ_LOGIC_LVL_BEHAVIOR\x10\xb2a\x12-\n(CHANNEL_ATTRIBUTE_CI_PULSE_TIME_TERM_CFG\x10\xb3a\x127\n2CHANNEL_ATTRIBUTE_CI_PULSE_TIME_LOGIC_LVL_BEHAVIOR\x10\xb4a\x12.\n)CHANNEL_ATTRIBUTE_CI_PULSE_TICKS_TERM_CFG\x10\xb5a\x128\n3CHANNEL_ATTRIBUTE_CI_PULSE_TICKS_LOGIC_LVL_BEHAVIOR\x10\xb6a\x124\n/CHANNEL_ATTRIBUTE_AI_EXCIT_IDLE_OUTPUT_BEHAVIOR\x10\xb8a\x12\'\n"CHANNEL_ATTRIBUTE_AI_DIG_FLTR_TYPE\x10\xbea\x12+\n&CHANNEL_ATTRIBUTE_AI_DIG_FLTR_RESPONSE\x10\xbfa\x12:\n5CHANNEL_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_A_SRC\x10\xcaa\x124\n/CHANNEL_ATTRIBUTE_CI_VELOCITY_ANG_ENCODER_UNITS\x10\xd8a\x124\n/CHANNEL_ATTRIBUTE_CI_VELOCITY_LIN_ENCODER_UNITS\x10\xdaa\x128\n3CHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_DECODING_TYPE\x10\xdca\x12;\n6CHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_TERM_CFG\x10\xdea\x12E\n@CHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_LOGIC_LVL_BEHAVIOR\x10\xdfa\x12;\n6CHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_TERM_CFG\x10\xe5a\x12E\n@CHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_LOGIC_LVL_BEHAVIOR\x10\xe6a\x123\n.CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_GATE_TERM_CFG\x10\xefa\x12=\n8CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_GATE_LOGIC_LVL_BEHAVIOR\x10\xf0a\x12/\n*CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_GATE_WHEN\x10\xf5a\x12:\n5CHANNEL_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_B_SRC\x10\xf7a\x12%\n CHANNEL_ATTRIBUTE_AI_EXCIT_SENSE\x10\xfda\x12&\n!CHANNEL_ATTRIBUTE_AI_CHARGE_UNITS\x10\x92b\x128\n3CHANNEL_ATTRIBUTE_AI_ACCEL_CHARGE_SENSITIVITY_UNITS\x10\x94b\x12C\n>CHANNEL_ATTRIBUTE_AI_ACCEL_4_WIRE_DC_VOLTAGE_SENSITIVITY_UNITS\x10\x96b\x120\n+CHANNEL_ATTRIBUTE_CHAN_SYNC_UNLOCK_BEHAVIOR\x10\xbcb\x12*\n%CHANNEL_ATTRIBUTE_AI_SENSOR_POWER_CFG\x10\xeab\x12+\n&CHANNEL_ATTRIBUTE_AI_SENSOR_POWER_TYPE\x10\xebb\x12)\n$CHANNEL_ATTRIBUTE_AI_FILTER_RESPONSE\x10\xf5b\x12)\n$CHANNEL_ATTRIBUTE_CI_FILTER_RESPONSE\x10\xb9c\x12,\n\'CHANNEL_ATTRIBUTE_CI_FILTER_DELAY_UNITS\x10\xbcc\x12\'\n"CHANNEL_ATTRIBUTE_PWR_OUTPUT_STATE\x10\xd7c\x12/\n*CHANNEL_ATTRIBUTE_PWR_IDLE_OUTPUT_BEHAVIOR\x10\xd8c\x12\'\n"CHANNEL_ATTRIBUTE_PWR_REMOTE_SENSE\x10\xdbc\x12%\n CHANNEL_ATTRIBUTE_AI_POWER_UNITS\x10\xecc*\x9cJ\n\x16ChannelDoubleAttribute\x12(\n$CHANNEL_DOUBLE_ATTRIBUTE_UNSPECIFIED\x10\x00\x12"\n\x1eCHANNEL_ATTRIBUTE_AI_IMPEDANCE\x10b\x12\'\n"CHANNEL_ATTRIBUTE_AI_AC_EXCIT_FREQ\x10\x81\x02\x12\x1e\n\x19CHANNEL_ATTRIBUTE_AO_GAIN\x10\x98\x02\x12(\n#CHANNEL_ATTRIBUTE_AO_LOAD_IMPEDANCE\x10\xa1\x02\x12(\n#CHANNEL_ATTRIBUTE_CI_FREQ_MEAS_TIME\x10\xc5\x02\x122\n-CHANNEL_ATTRIBUTE_CO_PULSE_FREQ_INITIAL_DELAY\x10\x99\x05\x12+\n&CHANNEL_ATTRIBUTE_AI_ACCEL_SENSITIVITY\x10\x92\r\x12#\n\x1eCHANNEL_ATTRIBUTE_AI_FREQ_HYST\x10\x94\x10\x12-\n(CHANNEL_ATTRIBUTE_AI_FREQ_THRESH_VOLTAGE\x10\x95\x10\x123\n.CHANNEL_ATTRIBUTE_CI_ANG_ENCODER_INITIAL_ANGLE\x10\x81\x11\x12-\n(CHANNEL_ATTRIBUTE_CI_ENCODER_Z_INDEX_VAL\x10\x88\x11\x12*\n%CHANNEL_ATTRIBUTE_AI_RVDT_SENSITIVITY\x10\x83\x12\x124\n/CHANNEL_ATTRIBUTE_CI_LIN_ENCODER_DIST_PER_PULSE\x10\x91\x12\x121\n,CHANNEL_ATTRIBUTE_CI_LIN_ENCODER_INITIAL_POS\x10\x95\x12\x12*\n%CHANNEL_ATTRIBUTE_AI_LVDT_SENSITIVITY\x10\xb9\x12\x121\n,CHANNEL_ATTRIBUTE_AI_STRAIN_GAGE_GAGE_FACTOR\x10\x94\x13\x123\n.CHANNEL_ATTRIBUTE_AI_STRAIN_GAGE_POISSON_RATIO\x10\x98\x13\x12\x1f\n\x1aCHANNEL_ATTRIBUTE_AI_RTD_A\x10\x90 \x12\x1f\n\x1aCHANNEL_ATTRIBUTE_AI_RTD_B\x10\x91 \x12\x1f\n\x1aCHANNEL_ATTRIBUTE_AI_RTD_C\x10\x93 \x12 \n\x1bCHANNEL_ATTRIBUTE_AI_RTD_R0\x10\xb0 \x12)\n$CHANNEL_ATTRIBUTE_AI_THRMCPL_CJC_VAL\x10\xb6 \x12$\n\x1fCHANNEL_ATTRIBUTE_AI_THRMSTR_R1\x10\xe1 \x12(\n#CHANNEL_ATTRIBUTE_CO_PULSE_DUTY_CYC\x10\xf6"\x12$\n\x1fCHANNEL_ATTRIBUTE_CO_PULSE_FREQ\x10\xf8"\x12\x1d\n\x18CHANNEL_ATTRIBUTE_AO_MAX\x10\x86#\x12\x1d\n\x18CHANNEL_ATTRIBUTE_AO_MIN\x10\x87#\x12*\n%CHANNEL_ATTRIBUTE_AO_OUTPUT_IMPEDANCE\x10\x90)\x120\n+CHANNEL_ATTRIBUTE_AI_MICROPHONE_SENSITIVITY\x10\xb6*\x12$\n\x1fCHANNEL_ATTRIBUTE_AI_RESOLUTION\x10\xe5.\x12\x1d\n\x18CHANNEL_ATTRIBUTE_AI_MAX\x10\xdd/\x12\x1d\n\x18CHANNEL_ATTRIBUTE_AI_MIN\x10\xde/\x12/\n*CHANNEL_ATTRIBUTE_AI_BRIDGE_NOM_RESISTANCE\x10\xec/\x120\n+CHANNEL_ATTRIBUTE_AI_BRIDGE_INITIAL_VOLTAGE\x10\xed/\x12.\n)CHANNEL_ATTRIBUTE_AI_LEAD_WIRE_RESISTANCE\x10\xee/\x122\n-CHANNEL_ATTRIBUTE_AI_CURRENT_SHUNT_RESISTANCE\x10\xf3/\x12#\n\x1eCHANNEL_ATTRIBUTE_AI_EXCIT_VAL\x10\xf5/\x12\x1f\n\x1aCHANNEL_ATTRIBUTE_AI_ATTEN\x10\x810\x12-\n(CHANNEL_ATTRIBUTE_AI_LOWPASS_CUTOFF_FREQ\x10\x830\x12.\n)CHANNEL_ATTRIBUTE_AI_HIGHPASS_CUTOFF_FREQ\x10\x870\x12.\n)CHANNEL_ATTRIBUTE_AI_BANDPASS_CENTER_FREQ\x10\x8c0\x12(\n#CHANNEL_ATTRIBUTE_AI_BANDPASS_WIDTH\x10\x8e0\x12+\n&CHANNEL_ATTRIBUTE_AI_NOTCH_CENTER_FREQ\x10\x900\x12%\n CHANNEL_ATTRIBUTE_AI_NOTCH_WIDTH\x10\x920\x12"\n\x1dCHANNEL_ATTRIBUTE_AI_RNG_HIGH\x10\x950\x12!\n\x1cCHANNEL_ATTRIBUTE_AI_RNG_LOW\x10\x960\x12\x1e\n\x19CHANNEL_ATTRIBUTE_AI_GAIN\x10\x980\x12$\n\x1fCHANNEL_ATTRIBUTE_AO_RESOLUTION\x10\xac0\x12%\n CHANNEL_ATTRIBUTE_AO_DAC_RNG_LOW\x10\xad0\x12&\n!CHANNEL_ATTRIBUTE_AO_DAC_RNG_HIGH\x10\xae0\x12%\n CHANNEL_ATTRIBUTE_AO_DAC_REF_VAL\x10\xb20\x12*\n%CHANNEL_ATTRIBUTE_AI_EXCIT_ACTUAL_VAL\x10\x831\x129\n4CHANNEL_ATTRIBUTE_AI_LOWPASS_SWITCH_CAP_EXT_CLK_FREQ\x10\x851\x12\x1d\n\x18CHANNEL_ATTRIBUTE_CI_MAX\x10\x9c1\x12\x1d\n\x18CHANNEL_ATTRIBUTE_CI_MIN\x10\x9d1\x12+\n&CHANNEL_ATTRIBUTE_CI_CTR_TIMEBASE_RATE\x10\xb21\x12)\n$CHANNEL_ATTRIBUTE_CO_PULSE_HIGH_TIME\x10\xba1\x12(\n#CHANNEL_ATTRIBUTE_CO_PULSE_LOW_TIME\x10\xbb1\x122\n-CHANNEL_ATTRIBUTE_CO_PULSE_TIME_INITIAL_DELAY\x10\xbc1\x12+\n&CHANNEL_ATTRIBUTE_CO_CTR_TIMEBASE_RATE\x10\xc21\x12#\n\x1eCHANNEL_ATTRIBUTE_AI_THRMSTR_A\x10\xc91\x12#\n\x1eCHANNEL_ATTRIBUTE_AI_THRMSTR_C\x10\xca1\x12#\n\x1eCHANNEL_ATTRIBUTE_AI_THRMSTR_B\x10\xcb1\x12*\n%CHANNEL_ATTRIBUTE_CI_PERIOD_MEAS_TIME\x10\xad2\x126\n1CHANNEL_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_GAIN_ADJUST\x10\xbf2\x122\n-CHANNEL_ATTRIBUTE_DI_DIG_FLTR_MIN_PULSE_WIDTH\x10\xd7C\x127\n2CHANNEL_ATTRIBUTE_CI_FREQ_DIG_FLTR_MIN_PULSE_WIDTH\x10\xe8C\x125\n0CHANNEL_ATTRIBUTE_CI_FREQ_DIG_FLTR_TIMEBASE_RATE\x10\xeaC\x129\n4CHANNEL_ATTRIBUTE_CI_PERIOD_DIG_FLTR_MIN_PULSE_WIDTH\x10\xedC\x127\n2CHANNEL_ATTRIBUTE_CI_PERIOD_DIG_FLTR_TIMEBASE_RATE\x10\xefC\x12H\nCCHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_DIG_FLTR_MIN_PULSE_WIDTH\x10\xf2C\x12F\nACHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_DIG_FLTR_TIMEBASE_RATE\x10\xf4C\x12>\n9CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_DIG_FLTR_MIN_PULSE_WIDTH\x10\xf7C\x12<\n7CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_DIG_FLTR_TIMEBASE_RATE\x10\xf9C\x12B\n=CHANNEL_ATTRIBUTE_CI_ENCODER_A_INPUT_DIG_FLTR_MIN_PULSE_WIDTH\x10\xfcC\x12@\n;CHANNEL_ATTRIBUTE_CI_ENCODER_A_INPUT_DIG_FLTR_TIMEBASE_RATE\x10\xfeC\x12B\n=CHANNEL_ATTRIBUTE_CI_ENCODER_B_INPUT_DIG_FLTR_MIN_PULSE_WIDTH\x10\x81D\x12@\n;CHANNEL_ATTRIBUTE_CI_ENCODER_B_INPUT_DIG_FLTR_TIMEBASE_RATE\x10\x83D\x12B\n=CHANNEL_ATTRIBUTE_CI_ENCODER_Z_INPUT_DIG_FLTR_MIN_PULSE_WIDTH\x10\x86D\x12@\n;CHANNEL_ATTRIBUTE_CI_ENCODER_Z_INPUT_DIG_FLTR_TIMEBASE_RATE\x10\x88D\x12>\n9CHANNEL_ATTRIBUTE_CI_PULSE_WIDTH_DIG_FLTR_MIN_PULSE_WIDTH\x10\x8bD\x12<\n7CHANNEL_ATTRIBUTE_CI_PULSE_WIDTH_DIG_FLTR_TIMEBASE_RATE\x10\x8dD\x12E\n@CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_DIG_FLTR_MIN_PULSE_WIDTH\x10\x90D\x12C\n>CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_DIG_FLTR_TIMEBASE_RATE\x10\x92D\x12F\nACHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_DIG_FLTR_MIN_PULSE_WIDTH\x10\x95D\x12D\n?CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_DIG_FLTR_TIMEBASE_RATE\x10\x97D\x12>\n9CHANNEL_ATTRIBUTE_CI_SEMI_PERIOD_DIG_FLTR_MIN_PULSE_WIDTH\x10\x9aD\x12<\n7CHANNEL_ATTRIBUTE_CI_SEMI_PERIOD_DIG_FLTR_TIMEBASE_RATE\x10\x9cD\x12?\n:CHANNEL_ATTRIBUTE_AI_SOUND_PRESSURE_MAX_SOUND_PRESSURE_LVL\x10\xbaD\x12(\n#CHANNEL_ATTRIBUTE_AO_DAC_OFFSET_VAL\x10\xd5D\x12?\n:CHANNEL_ATTRIBUTE_CI_CTR_TIMEBASE_DIG_FLTR_MIN_PULSE_WIDTH\x10\xf2D\x12=\n8CHANNEL_ATTRIBUTE_CI_CTR_TIMEBASE_DIG_FLTR_TIMEBASE_RATE\x10\xf4D\x12?\n:CHANNEL_ATTRIBUTE_CO_CTR_TIMEBASE_DIG_FLTR_MIN_PULSE_WIDTH\x10\xf7D\x12=\n8CHANNEL_ATTRIBUTE_CO_CTR_TIMEBASE_DIG_FLTR_TIMEBASE_RATE\x10\xf9D\x12(\n#CHANNEL_ATTRIBUTE_AI_VOLTAGE_DB_REF\x10\xb0S\x12/\n*CHANNEL_ATTRIBUTE_AI_SOUND_PRESSURE_DB_REF\x10\xb1S\x12&\n!CHANNEL_ATTRIBUTE_AI_ACCEL_DB_REF\x10\xb2S\x12\'\n"CHANNEL_ATTRIBUTE_AO_FUNC_GEN_FREQ\x10\x99T\x12,\n\'CHANNEL_ATTRIBUTE_AO_FUNC_GEN_AMPLITUDE\x10\x9aT\x12)\n$CHANNEL_ATTRIBUTE_AO_FUNC_GEN_OFFSET\x10\x9bT\x124\n/CHANNEL_ATTRIBUTE_AO_FUNC_GEN_SQUARE_DUTY_CYCLE\x10\x9cT\x12/\n*CHANNEL_ATTRIBUTE_AO_VOLTAGE_CURRENT_LIMIT\x10\x9dT\x12/\n*CHANNEL_ATTRIBUTE_AO_FUNC_GEN_FM_DEVIATION\x10\xa3T\x12+\n&CHANNEL_ATTRIBUTE_DO_OVERCURRENT_LIMIT\x10\x85U\x125\n0CHANNEL_ATTRIBUTE_DO_OVERCURRENT_REENABLE_PERIOD\x10\x87U\x12%\n CHANNEL_ATTRIBUTE_AI_PROBE_ATTEN\x10\x88U\x12#\n\x1eCHANNEL_ATTRIBUTE_AI_DC_OFFSET\x10\x89U\x12=\n8CHANNEL_ATTRIBUTE_AI_EDDY_CURRENT_PROX_PROBE_SENSITIVITY\x10\xbeU\x120\n+CHANNEL_ATTRIBUTE_DI_DIG_FLTR_TIMEBASE_RATE\x10\xd5]\x12=\n8CHANNEL_ATTRIBUTE_CI_PULSE_FREQ_DIG_FLTR_MIN_PULSE_WIDTH\x10\x87^\x12;\n6CHANNEL_ATTRIBUTE_CI_PULSE_FREQ_DIG_FLTR_TIMEBASE_RATE\x10\x89^\x12=\n8CHANNEL_ATTRIBUTE_CI_PULSE_TIME_DIG_FLTR_MIN_PULSE_WIDTH\x10\x8f^\x12;\n6CHANNEL_ATTRIBUTE_CI_PULSE_TIME_DIG_FLTR_TIMEBASE_RATE\x10\x91^\x12>\n9CHANNEL_ATTRIBUTE_CI_PULSE_TICKS_DIG_FLTR_MIN_PULSE_WIDTH\x10\x97^\x12<\n7CHANNEL_ATTRIBUTE_CI_PULSE_TICKS_DIG_FLTR_TIMEBASE_RATE\x10\x99^\x12A\n<CHANNEL_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_A_RESISTANCE\x10\xf8^\x12H\nCCHANNEL_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_A_ACTUAL_RESISTANCE\x10\xf9^\x12A\n<CHANNEL_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_B_RESISTANCE\x10\xfa^\x12H\nCCHANNEL_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_B_ACTUAL_RESISTANCE\x10\xfb^\x127\n2CHANNEL_ATTRIBUTE_AI_FORCE_IEPE_SENSOR_SENSITIVITY\x10\x81_\x12.\n)CHANNEL_ATTRIBUTE_AI_BRIDGE_INITIAL_RATIO\x10\x86_\x12C\n>CHANNEL_ATTRIBUTE_AI_BRIDGE_TWO_POINT_LIN_FIRST_ELECTRICAL_VAL\x10\x8a_\x12A\n<CHANNEL_ATTRIBUTE_AI_BRIDGE_TWO_POINT_LIN_FIRST_PHYSICAL_VAL\x10\x8b_\x12D\n?CHANNEL_ATTRIBUTE_AI_BRIDGE_TWO_POINT_LIN_SECOND_ELECTRICAL_VAL\x10\x8c_\x12B\n=CHANNEL_ATTRIBUTE_AI_BRIDGE_TWO_POINT_LIN_SECOND_PHYSICAL_VAL\x10\x8d_\x12J\nECHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_DIG_FLTR_MIN_PULSE_WIDTH\x10\xb4_\x12H\nCCHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_DIG_FLTR_TIMEBASE_RATE\x10\xb6_\x125\n0CHANNEL_ATTRIBUTE_AI_THRMCPL_LEAD_OFFSET_VOLTAGE\x10\xb8_\x12&\n!CHANNEL_ATTRIBUTE_AI_FILTER_DELAY\x10\xed_\x125\n0CHANNEL_ATTRIBUTE_AI_VELOCITY_IEPE_SENSOR_DB_REF\x10\xf5_\x12:\n5CHANNEL_ATTRIBUTE_AI_VELOCITY_IEPE_SENSOR_SENSITIVITY\x10\xf6_\x129\n4CHANNEL_ATTRIBUTE_AI_ROSETTE_STRAIN_GAGE_ORIENTATION\x10\xfc_\x121\n,CHANNEL_ATTRIBUTE_AO_FILTER_DELAY_ADJUSTMENT\x10\xf2`\x121\n,CHANNEL_ATTRIBUTE_AI_FILTER_DELAY_ADJUSTMENT\x10\xf4`\x12&\n!CHANNEL_ATTRIBUTE_AO_FILTER_DELAY\x10\xf5`\x12=\n8CHANNEL_ATTRIBUTE_CI_DUTY_CYCLE_DIG_FLTR_MIN_PULSE_WIDTH\x10\x8fa\x12;\n6CHANNEL_ATTRIBUTE_CI_DUTY_CYCLE_DIG_FLTR_TIMEBASE_RATE\x10\x91a\x12)\n$CHANNEL_ATTRIBUTE_CI_MAX_MEAS_PERIOD\x10\x95a\x12(\n#CHANNEL_ATTRIBUTE_CI_THRESH_VOLTAGE\x10\xb7a\x126\n1CHANNEL_ATTRIBUTE_AI_DIG_FLTR_LOWPASS_CUTOFF_FREQ\x10\xc1a\x127\n2CHANNEL_ATTRIBUTE_AI_DIG_FLTR_HIGHPASS_CUTOFF_FREQ\x10\xc2a\x127\n2CHANNEL_ATTRIBUTE_AI_DIG_FLTR_BANDPASS_CENTER_FREQ\x10\xc3a\x121\n,CHANNEL_ATTRIBUTE_AI_DIG_FLTR_BANDPASS_WIDTH\x10\xc4a\x124\n/CHANNEL_ATTRIBUTE_AI_DIG_FLTR_NOTCH_CENTER_FREQ\x10\xc5a\x12.\n)CHANNEL_ATTRIBUTE_AI_DIG_FLTR_NOTCH_WIDTH\x10\xc6a\x12=\n8CHANNEL_ATTRIBUTE_CI_VELOCITY_LIN_ENCODER_DIST_PER_PULSE\x10\xdba\x12K\nFCHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_DIG_FLTR_MIN_PULSE_WIDTH\x10\xe1a\x12I\nDCHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_DIG_FLTR_TIMEBASE_RATE\x10\xe3a\x12K\nFCHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_DIG_FLTR_MIN_PULSE_WIDTH\x10\xe8a\x12I\nDCHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_DIG_FLTR_TIMEBASE_RATE\x10\xeaa\x12,\n\'CHANNEL_ATTRIBUTE_CI_VELOCITY_MEAS_TIME\x10\xeba\x12C\n>CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_GATE_DIG_FLTR_MIN_PULSE_WIDTH\x10\xf2a\x12A\n<CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_GATE_DIG_FLTR_TIMEBASE_RATE\x10\xf4a\x122\n-CHANNEL_ATTRIBUTE_AI_ACCEL_CHARGE_SENSITIVITY\x10\x93b\x12=\n8CHANNEL_ATTRIBUTE_AI_ACCEL_4_WIRE_DC_VOLTAGE_SENSITIVITY\x10\x95b\x12,\n\'CHANNEL_ATTRIBUTE_AI_DATA_XFER_MAX_RATE\x10\x97b\x12.\n)CHANNEL_ATTRIBUTE_AI_SENSOR_POWER_VOLTAGE\x10\xe9b\x12%\n CHANNEL_ATTRIBUTE_AI_FILTER_FREQ\x10\xf4b\x12?\n:CHANNEL_ATTRIBUTE_AI_INPUT_LIMITS_FAULT_DETECT_UPPER_LIMIT\x10\x8cc\x12?\n:CHANNEL_ATTRIBUTE_AI_INPUT_LIMITS_FAULT_DETECT_LOWER_LIMIT\x10\x8dc\x12-\n(CHANNEL_ATTRIBUTE_CI_FREQ_THRESH_VOLTAGE\x10\xabc\x12#\n\x1eCHANNEL_ATTRIBUTE_CI_FREQ_HYST\x10\xacc\x12/\n*CHANNEL_ATTRIBUTE_CI_PERIOD_THRESH_VOLTAGE\x10\xadc\x12%\n CHANNEL_ATTRIBUTE_CI_PERIOD_HYST\x10\xaec\x124\n/CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_THRESH_VOLTAGE\x10\xafc\x12*\n%CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_HYST\x10\xb0c\x12>\n9CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_THRESH_VOLTAGE\x10\xb1c\x124\n/CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_HYST\x10\xb2c\x12@\n;CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_THRESH_VOLTAGE\x10\xb3c\x126\n1CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_HYST\x10\xb4c\x129\n4CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_GATE_THRESH_VOLTAGE\x10\xb5c\x12/\n*CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_GATE_HYST\x10\xb6c\x12%\n CHANNEL_ATTRIBUTE_CI_FILTER_FREQ\x10\xb8c\x12&\n!CHANNEL_ATTRIBUTE_CI_FILTER_DELAY\x10\xbbc\x12.\n)CHANNEL_ATTRIBUTE_AO_FUNC_GEN_START_PHASE\x10\xc4c\x12,\n\'CHANNEL_ATTRIBUTE_AO_COMMON_MODE_OFFSET\x10\xccc\x12+\n&CHANNEL_ATTRIBUTE_PWR_VOLTAGE_SETPOINT\x10\xd4c\x12+\n&CHANNEL_ATTRIBUTE_PWR_CURRENT_SETPOINT\x10\xd5c\x126\n1CHANNEL_ATTRIBUTE_AI_CALCULATED_POWER_VOLTAGE_MAX\x10\xedc\x126\n1CHANNEL_ATTRIBUTE_AI_CALCULATED_POWER_VOLTAGE_MIN\x10\xeec\x126\n1CHANNEL_ATTRIBUTE_AI_CALCULATED_POWER_CURRENT_MAX\x10\xefc\x126\n1CHANNEL_ATTRIBUTE_AI_CALCULATED_POWER_CURRENT_MIN\x10\xf0c*\xf8\xf8\x01\n\x15ChannelResetAttribute\x12\'\n#CHANNEL_RESET_ATTRIBUTE_UNSPECIFIED\x10\x00\x12(\n$CHANNEL_RESET_ATTRIBUTE_AI_IMPEDANCE\x10b\x12\'\n#CHANNEL_RESET_ATTRIBUTE_AI_COUPLING\x10d\x12,\n(CHANNEL_RESET_ATTRIBUTE_AI_DITHER_ENABLE\x10h\x12*\n%CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_CFG\x10\x87\x01\x127\n2CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_ENABLE\x10\x94\x01\x12-\n(CHANNEL_RESET_ATTRIBUTE_AI_AC_EXCIT_FREQ\x10\x81\x02\x124\n/CHANNEL_RESET_ATTRIBUTE_AI_AC_EXCIT_SYNC_ENABLE\x10\x82\x02\x12$\n\x1fCHANNEL_RESET_ATTRIBUTE_AO_GAIN\x10\x98\x02\x12.\n)CHANNEL_RESET_ATTRIBUTE_AO_LOAD_IMPEDANCE\x10\xa1\x02\x123\n.CHANNEL_RESET_ATTRIBUTE_AO_DAC_REF_CONN_TO_GND\x10\xb0\x02\x12+\n&CHANNEL_RESET_ATTRIBUTE_AO_DAC_REF_SRC\x10\xb2\x02\x12/\n*CHANNEL_RESET_ATTRIBUTE_AO_REGLITCH_ENABLE\x10\xb3\x02\x12.\n)CHANNEL_RESET_ATTRIBUTE_AO_DATA_XFER_MECH\x10\xb4\x02\x128\n3CHANNEL_RESET_ATTRIBUTE_CI_CTR_TIMEBASE_ACTIVE_EDGE\x10\xc2\x02\x120\n+CHANNEL_RESET_ATTRIBUTE_CI_CTR_TIMEBASE_SRC\x10\xc3\x02\x12.\n)CHANNEL_RESET_ATTRIBUTE_CI_FREQ_MEAS_METH\x10\xc4\x02\x12.\n)CHANNEL_RESET_ATTRIBUTE_CI_FREQ_MEAS_TIME\x10\xc5\x02\x12(\n#CHANNEL_RESET_ATTRIBUTE_CI_FREQ_DIV\x10\xc7\x02\x12.\n)CHANNEL_RESET_ATTRIBUTE_CI_DATA_XFER_MECH\x10\x80\x04\x12-\n(CHANNEL_RESET_ATTRIBUTE_CO_AUTO_INCR_CNT\x10\x95\x05\x129\n4CHANNEL_RESET_ATTRIBUTE_CO_PULSE_TICKS_INITIAL_DELAY\x10\x98\x05\x128\n3CHANNEL_RESET_ATTRIBUTE_CO_PULSE_FREQ_INITIAL_DELAY\x10\x99\x05\x120\n+CHANNEL_RESET_ATTRIBUTE_CO_CTR_TIMEBASE_SRC\x10\xb9\x06\x128\n3CHANNEL_RESET_ATTRIBUTE_CO_CTR_TIMEBASE_ACTIVE_EDGE\x10\xc1\x06\x12+\n&CHANNEL_RESET_ATTRIBUTE_AI_ACCEL_UNITS\x10\xf3\x0c\x121\n,CHANNEL_RESET_ATTRIBUTE_AI_ACCEL_SENSITIVITY\x10\x92\r\x12/\n*CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_DIR\x10\x96\r\x127\n2CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_ACTIVE_EDGE\x10\x97\r\x127\n2CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_INITIAL_CNT\x10\x98\r\x12-\n(CHANNEL_RESET_ATTRIBUTE_AI_CURRENT_UNITS\x10\x81\x0e\x12,\n\'CHANNEL_RESET_ATTRIBUTE_DI_INVERT_LINES\x10\x93\x0f\x122\n-CHANNEL_RESET_ATTRIBUTE_CI_FREQ_STARTING_EDGE\x10\x99\x0f\x12*\n%CHANNEL_RESET_ATTRIBUTE_AI_FREQ_UNITS\x10\x86\x10\x12)\n$CHANNEL_RESET_ATTRIBUTE_AI_FREQ_HYST\x10\x94\x10\x123\n.CHANNEL_RESET_ATTRIBUTE_AI_FREQ_THRESH_VOLTAGE\x10\x95\x10\x121\n,CHANNEL_RESET_ATTRIBUTE_CI_PULSE_WIDTH_UNITS\x10\xa3\x10\x129\n4CHANNEL_RESET_ATTRIBUTE_CI_PULSE_WIDTH_STARTING_EDGE\x10\xa5\x10\x127\n2CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_EDGE\x10\xb3\x10\x128\n3CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_EDGE\x10\xb4\x10\x124\n/CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_STARTING_EDGE\x10\xd2\x10\x12:\n5CHANNEL_RESET_ATTRIBUTE_CI_ANG_ENCODER_PULSES_PER_REV\x10\xf5\x10\x12*\n%CHANNEL_RESET_ATTRIBUTE_AI_RVDT_UNITS\x10\xf7\x10\x129\n4CHANNEL_RESET_ATTRIBUTE_CI_ANG_ENCODER_INITIAL_ANGLE\x10\x81\x11\x123\n.CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_Z_INDEX_VAL\x10\x88\x11\x125\n0CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_Z_INDEX_PHASE\x10\x89\x11\x126\n1CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_Z_INDEX_ENABLE\x10\x90\x11\x120\n+CHANNEL_RESET_ATTRIBUTE_AI_RVDT_SENSITIVITY\x10\x83\x12\x12*\n%CHANNEL_RESET_ATTRIBUTE_AI_LVDT_UNITS\x10\x90\x12\x12:\n5CHANNEL_RESET_ATTRIBUTE_CI_LIN_ENCODER_DIST_PER_PULSE\x10\x91\x12\x127\n2CHANNEL_RESET_ATTRIBUTE_CI_LIN_ENCODER_INITIAL_POS\x10\x95\x12\x120\n+CHANNEL_RESET_ATTRIBUTE_AI_LVDT_SENSITIVITY\x10\xb9\x12\x120\n+CHANNEL_RESET_ATTRIBUTE_AI_RESISTANCE_UNITS\x10\xd5\x12\x12,\n\'CHANNEL_RESET_ATTRIBUTE_AI_STRAIN_UNITS\x10\x81\x13\x12/\n*CHANNEL_RESET_ATTRIBUTE_AI_STRAIN_GAGE_CFG\x10\x82\x13\x127\n2CHANNEL_RESET_ATTRIBUTE_AI_STRAIN_GAGE_GAGE_FACTOR\x10\x94\x13\x129\n4CHANNEL_RESET_ATTRIBUTE_AI_STRAIN_GAGE_POISSON_RATIO\x10\x98\x13\x12%\n CHANNEL_RESET_ATTRIBUTE_AI_RTD_A\x10\x90 \x12%\n CHANNEL_RESET_ATTRIBUTE_AI_RTD_B\x10\x91 \x12%\n CHANNEL_RESET_ATTRIBUTE_AI_RTD_C\x10\x93 \x12&\n!CHANNEL_RESET_ATTRIBUTE_AI_RTD_R0\x10\xb0 \x12(\n#CHANNEL_RESET_ATTRIBUTE_AI_RTD_TYPE\x10\xb2 \x12*\n%CHANNEL_RESET_ATTRIBUTE_AI_TEMP_UNITS\x10\xb3 \x12/\n*CHANNEL_RESET_ATTRIBUTE_AI_THRMCPL_CJC_VAL\x10\xb6 \x12,\n\'CHANNEL_RESET_ATTRIBUTE_AI_THRMCPL_TYPE\x10\xd0 \x12*\n%CHANNEL_RESET_ATTRIBUTE_AI_THRMSTR_R1\x10\xe1 \x12/\n*CHANNEL_RESET_ATTRIBUTE_CI_GPS_SYNC_METHOD\x10\x92!\x12,\n\'CHANNEL_RESET_ATTRIBUTE_CI_GPS_SYNC_SRC\x10\x93!\x12-\n(CHANNEL_RESET_ATTRIBUTE_AI_VOLTAGE_UNITS\x10\x94!\x12(\n#CHANNEL_RESET_ATTRIBUTE_AI_TERM_CFG\x10\x97!\x12-\n(CHANNEL_RESET_ATTRIBUTE_AO_CURRENT_UNITS\x10\x89"\x12,\n\'CHANNEL_RESET_ATTRIBUTE_DO_INVERT_LINES\x10\xb3"\x121\n,CHANNEL_RESET_ATTRIBUTE_DO_OUTPUT_DRIVE_TYPE\x10\xb7"\x120\n+CHANNEL_RESET_ATTRIBUTE_CO_PULSE_HIGH_TICKS\x10\xe9"\x120\n+CHANNEL_RESET_ATTRIBUTE_CO_PULSE_IDLE_STATE\x10\xf0"\x12/\n*CHANNEL_RESET_ATTRIBUTE_CO_PULSE_LOW_TICKS\x10\xf1"\x12.\n)CHANNEL_RESET_ATTRIBUTE_CO_PULSE_DUTY_CYC\x10\xf6"\x12*\n%CHANNEL_RESET_ATTRIBUTE_CO_PULSE_FREQ\x10\xf8"\x12-\n(CHANNEL_RESET_ATTRIBUTE_AO_VOLTAGE_UNITS\x10\x84#\x12#\n\x1eCHANNEL_RESET_ATTRIBUTE_AO_MAX\x10\x86#\x12#\n\x1eCHANNEL_RESET_ATTRIBUTE_AO_MIN\x10\x87#\x121\n,CHANNEL_RESET_ATTRIBUTE_AO_CUSTOM_SCALE_NAME\x10\x88#\x120\n+CHANNEL_RESET_ATTRIBUTE_AO_OUTPUT_IMPEDANCE\x10\x90)\x124\n/CHANNEL_RESET_ATTRIBUTE_AI_SOUND_PRESSURE_UNITS\x10\xa8*\x126\n1CHANNEL_RESET_ATTRIBUTE_AI_MICROPHONE_SENSITIVITY\x10\xb6*\x12.\n)CHANNEL_RESET_ATTRIBUTE_AI_AUTO_ZERO_MODE\x10\xe0.\x12#\n\x1eCHANNEL_RESET_ATTRIBUTE_AI_MAX\x10\xdd/\x12#\n\x1eCHANNEL_RESET_ATTRIBUTE_AI_MIN\x10\xde/\x121\n,CHANNEL_RESET_ATTRIBUTE_AI_CUSTOM_SCALE_NAME\x10\xe0/\x123\n.CHANNEL_RESET_ATTRIBUTE_AI_VOLTAGE_ACRMS_UNITS\x10\xe2/\x123\n.CHANNEL_RESET_ATTRIBUTE_AI_CURRENT_ACRMS_UNITS\x10\xe3/\x125\n0CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_NOM_RESISTANCE\x10\xec/\x126\n1CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_INITIAL_VOLTAGE\x10\xed/\x124\n/CHANNEL_RESET_ATTRIBUTE_AI_LEAD_WIRE_RESISTANCE\x10\xee/\x129\n4CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_BALANCE_COARSE_POT\x10\xf1/\x121\n,CHANNEL_RESET_ATTRIBUTE_AI_CURRENT_SHUNT_LOC\x10\xf2/\x128\n3CHANNEL_RESET_ATTRIBUTE_AI_CURRENT_SHUNT_RESISTANCE\x10\xf3/\x12)\n$CHANNEL_RESET_ATTRIBUTE_AI_EXCIT_SRC\x10\xf4/\x12)\n$CHANNEL_RESET_ATTRIBUTE_AI_EXCIT_VAL\x10\xf5/\x128\n3CHANNEL_RESET_ATTRIBUTE_AI_EXCIT_VOLTAGE_OR_CURRENT\x10\xf6/\x12.\n)CHANNEL_RESET_ATTRIBUTE_AI_EXCIT_D_COR_AC\x10\xfb/\x125\n0CHANNEL_RESET_ATTRIBUTE_AI_EXCIT_USE_FOR_SCALING\x10\xfc/\x12%\n CHANNEL_RESET_ATTRIBUTE_AI_ATTEN\x10\x810\x12.\n)CHANNEL_RESET_ATTRIBUTE_AI_LOWPASS_ENABLE\x10\x820\x123\n.CHANNEL_RESET_ATTRIBUTE_AI_LOWPASS_CUTOFF_FREQ\x10\x830\x12/\n*CHANNEL_RESET_ATTRIBUTE_AI_HIGHPASS_ENABLE\x10\x860\x124\n/CHANNEL_RESET_ATTRIBUTE_AI_HIGHPASS_CUTOFF_FREQ\x10\x870\x12-\n(CHANNEL_RESET_ATTRIBUTE_AI_HIGHPASS_TYPE\x10\x880\x12.\n)CHANNEL_RESET_ATTRIBUTE_AI_HIGHPASS_ORDER\x10\x890\x12/\n*CHANNEL_RESET_ATTRIBUTE_AI_BANDPASS_ENABLE\x10\x8b0\x124\n/CHANNEL_RESET_ATTRIBUTE_AI_BANDPASS_CENTER_FREQ\x10\x8c0\x12-\n(CHANNEL_RESET_ATTRIBUTE_AI_BANDPASS_TYPE\x10\x8d0\x12.\n)CHANNEL_RESET_ATTRIBUTE_AI_BANDPASS_WIDTH\x10\x8e0\x121\n,CHANNEL_RESET_ATTRIBUTE_AI_NOTCH_CENTER_FREQ\x10\x900\x12*\n%CHANNEL_RESET_ATTRIBUTE_AI_NOTCH_TYPE\x10\x910\x12+\n&CHANNEL_RESET_ATTRIBUTE_AI_NOTCH_WIDTH\x10\x920\x12(\n#CHANNEL_RESET_ATTRIBUTE_AI_RNG_HIGH\x10\x950\x12\'\n"CHANNEL_RESET_ATTRIBUTE_AI_RNG_LOW\x10\x960\x12$\n\x1fCHANNEL_RESET_ATTRIBUTE_AI_GAIN\x10\x980\x124\n/CHANNEL_RESET_ATTRIBUTE_AI_SAMP_AND_HOLD_ENABLE\x10\x9a0\x12.\n)CHANNEL_RESET_ATTRIBUTE_AI_DATA_XFER_MECH\x10\xa10\x120\n+CHANNEL_RESET_ATTRIBUTE_AO_RESOLUTION_UNITS\x10\xab0\x12+\n&CHANNEL_RESET_ATTRIBUTE_AO_DAC_RNG_LOW\x10\xad0\x12,\n\'CHANNEL_RESET_ATTRIBUTE_AO_DAC_RNG_HIGH\x10\xae0\x129\n4CHANNEL_RESET_ATTRIBUTE_AO_DAC_REF_ALLOW_CONN_TO_GND\x10\xb00\x12+\n&CHANNEL_RESET_ATTRIBUTE_AO_DAC_REF_VAL\x10\xb20\x123\n.CHANNEL_RESET_ATTRIBUTE_AO_USE_ONLY_ON_BRD_MEM\x10\xba0\x122\n-CHANNEL_RESET_ATTRIBUTE_AO_DATA_XFER_REQ_COND\x10\xbc0\x12.\n)CHANNEL_RESET_ATTRIBUTE_AI_RESISTANCE_CFG\x10\x811\x120\n+CHANNEL_RESET_ATTRIBUTE_AI_EXCIT_ACTUAL_VAL\x10\x831\x12:\n5CHANNEL_RESET_ATTRIBUTE_AI_LOWPASS_SWITCH_CAP_CLK_SRC\x10\x841\x12?\n:CHANNEL_RESET_ATTRIBUTE_AI_LOWPASS_SWITCH_CAP_EXT_CLK_FREQ\x10\x851\x12>\n9CHANNEL_RESET_ATTRIBUTE_AI_LOWPASS_SWITCH_CAP_EXT_CLK_DIV\x10\x861\x12>\n9CHANNEL_RESET_ATTRIBUTE_AI_LOWPASS_SWITCH_CAP_OUT_CLK_DIV\x10\x871\x122\n-CHANNEL_RESET_ATTRIBUTE_AI_DATA_XFER_REQ_COND\x10\x8b1\x12.\n)CHANNEL_RESET_ATTRIBUTE_AI_MEM_MAP_ENABLE\x10\x8c1\x12(\n#CHANNEL_RESET_ATTRIBUTE_AO_TERM_CFG\x10\x8e1\x12.\n)CHANNEL_RESET_ATTRIBUTE_AO_MEM_MAP_ENABLE\x10\x8f1\x12(\n#CHANNEL_RESET_ATTRIBUTE_DI_TRISTATE\x10\x901\x12#\n\x1eCHANNEL_RESET_ATTRIBUTE_CI_MAX\x10\x9c1\x12#\n\x1eCHANNEL_RESET_ATTRIBUTE_CI_MIN\x10\x9d1\x121\n,CHANNEL_RESET_ATTRIBUTE_CI_CUSTOM_SCALE_NAME\x10\x9e1\x12*\n%CHANNEL_RESET_ATTRIBUTE_CI_FREQ_UNITS\x10\xa11\x12)\n$CHANNEL_RESET_ATTRIBUTE_CI_FREQ_TERM\x10\xa21\x12,\n\'CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_UNITS\x10\xa31\x12+\n&CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_TERM\x10\xa41\x121\n,CHANNEL_RESET_ATTRIBUTE_CI_ANG_ENCODER_UNITS\x10\xa61\x121\n,CHANNEL_RESET_ATTRIBUTE_CI_LIN_ENCODER_UNITS\x10\xa91\x120\n+CHANNEL_RESET_ATTRIBUTE_CI_PULSE_WIDTH_TERM\x10\xaa1\x122\n-CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_UNITS\x10\xac1\x127\n2CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_TERM\x10\xad1\x128\n3CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_TERM\x10\xae1\x121\n,CHANNEL_RESET_ATTRIBUTE_CI_SEMI_PERIOD_UNITS\x10\xaf1\x120\n+CHANNEL_RESET_ATTRIBUTE_CI_SEMI_PERIOD_TERM\x10\xb01\x121\n,CHANNEL_RESET_ATTRIBUTE_CI_CTR_TIMEBASE_RATE\x10\xb21\x12@\n;CHANNEL_RESET_ATTRIBUTE_CI_CTR_TIMEBASE_MASTER_TIMEBASE_DIV\x10\xb31\x12/\n*CHANNEL_RESET_ATTRIBUTE_CO_PULSE_HIGH_TIME\x10\xba1\x12.\n)CHANNEL_RESET_ATTRIBUTE_CO_PULSE_LOW_TIME\x10\xbb1\x128\n3CHANNEL_RESET_ATTRIBUTE_CO_PULSE_TIME_INITIAL_DELAY\x10\xbc1\x121\n,CHANNEL_RESET_ATTRIBUTE_CO_CTR_TIMEBASE_RATE\x10\xc21\x12@\n;CHANNEL_RESET_ATTRIBUTE_CO_CTR_TIMEBASE_MASTER_TIMEBASE_DIV\x10\xc31\x120\n+CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_TERM\x10\xc71\x12)\n$CHANNEL_RESET_ATTRIBUTE_AI_THRMSTR_A\x10\xc91\x12)\n$CHANNEL_RESET_ATTRIBUTE_AI_THRMSTR_C\x10\xca1\x12)\n$CHANNEL_RESET_ATTRIBUTE_AI_THRMSTR_B\x10\xcb1\x122\n-CHANNEL_RESET_ATTRIBUTE_AI_AC_EXCIT_WIRE_MODE\x10\xcd1\x120\n+CHANNEL_RESET_ATTRIBUTE_CO_PULSE_FREQ_UNITS\x10\xd51\x120\n+CHANNEL_RESET_ATTRIBUTE_CO_PULSE_TIME_UNITS\x10\xd61\x12*\n%CHANNEL_RESET_ATTRIBUTE_CO_PULSE_TERM\x10\xe11\x12(\n#CHANNEL_RESET_ATTRIBUTE_DO_TRISTATE\x10\xf31\x127\n2CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_BALANCE_FINE_POT\x10\xf41\x124\n/CHANNEL_RESET_ATTRIBUTE_AI_FORCE_READ_FROM_CHAN\x10\xf81\x12\'\n"CHANNEL_RESET_ATTRIBUTE_CHAN_DESCR\x10\xa62\x120\n+CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_MEAS_METH\x10\xac2\x120\n+CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_MEAS_TIME\x10\xad2\x12*\n%CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_DIV\x10\xae2\x12<\n7CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_GAIN_ADJUST\x10\xbf2\x125\n0CHANNEL_RESET_ATTRIBUTE_AI_EXCIT_USE_MULTIPLEXED\x10\x80C\x12)\n$CHANNEL_RESET_ATTRIBUTE_AI_INPUT_SRC\x10\x98C\x126\n1CHANNEL_RESET_ATTRIBUTE_AI_LVDT_SENSITIVITY_UNITS\x10\x9aC\x126\n1CHANNEL_RESET_ATTRIBUTE_AI_RVDT_SENSITIVITY_UNITS\x10\x9bC\x127\n2CHANNEL_RESET_ATTRIBUTE_AI_ACCEL_SENSITIVITY_UNITS\x10\x9cC\x124\n/CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_A_INPUT_TERM\x10\x9dC\x124\n/CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_B_INPUT_TERM\x10\x9eC\x124\n/CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_Z_INPUT_TERM\x10\x9fC\x121\n,CHANNEL_RESET_ATTRIBUTE_CI_DUP_COUNT_PREVENT\x10\xacC\x127\n2CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SELECT\x10\xd5C\x12/\n*CHANNEL_RESET_ATTRIBUTE_DI_DIG_FLTR_ENABLE\x10\xd6C\x128\n3CHANNEL_RESET_ATTRIBUTE_DI_DIG_FLTR_MIN_PULSE_WIDTH\x10\xd7C\x124\n/CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_DIR_TERM\x10\xe1C\x125\n0CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_DECODING_TYPE\x10\xe6C\x124\n/CHANNEL_RESET_ATTRIBUTE_CI_FREQ_DIG_FLTR_ENABLE\x10\xe7C\x12=\n8CHANNEL_RESET_ATTRIBUTE_CI_FREQ_DIG_FLTR_MIN_PULSE_WIDTH\x10\xe8C\x12:\n5CHANNEL_RESET_ATTRIBUTE_CI_FREQ_DIG_FLTR_TIMEBASE_SRC\x10\xe9C\x12;\n6CHANNEL_RESET_ATTRIBUTE_CI_FREQ_DIG_FLTR_TIMEBASE_RATE\x10\xeaC\x124\n/CHANNEL_RESET_ATTRIBUTE_CI_FREQ_DIG_SYNC_ENABLE\x10\xebC\x126\n1CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_DIG_FLTR_ENABLE\x10\xecC\x12?\n:CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_DIG_FLTR_MIN_PULSE_WIDTH\x10\xedC\x12<\n7CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_DIG_FLTR_TIMEBASE_SRC\x10\xeeC\x12=\n8CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_DIG_FLTR_TIMEBASE_RATE\x10\xefC\x126\n1CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_DIG_SYNC_ENABLE\x10\xf0C\x12E\n@CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_DIG_FLTR_ENABLE\x10\xf1C\x12N\nICHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_DIG_FLTR_MIN_PULSE_WIDTH\x10\xf2C\x12K\nFCHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_DIG_FLTR_TIMEBASE_SRC\x10\xf3C\x12L\nGCHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_DIG_FLTR_TIMEBASE_RATE\x10\xf4C\x12E\n@CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_DIG_SYNC_ENABLE\x10\xf5C\x12;\n6CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_DIG_FLTR_ENABLE\x10\xf6C\x12D\n?CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_DIG_FLTR_MIN_PULSE_WIDTH\x10\xf7C\x12A\n<CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_DIG_FLTR_TIMEBASE_SRC\x10\xf8C\x12B\n=CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_DIG_FLTR_TIMEBASE_RATE\x10\xf9C\x12;\n6CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_DIG_SYNC_ENABLE\x10\xfaC\x12?\n:CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_A_INPUT_DIG_FLTR_ENABLE\x10\xfbC\x12H\nCCHANNEL_RESET_ATTRIBUTE_CI_ENCODER_A_INPUT_DIG_FLTR_MIN_PULSE_WIDTH\x10\xfcC\x12E\n@CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_A_INPUT_DIG_FLTR_TIMEBASE_SRC\x10\xfdC\x12F\nACHANNEL_RESET_ATTRIBUTE_CI_ENCODER_A_INPUT_DIG_FLTR_TIMEBASE_RATE\x10\xfeC\x12?\n:CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_A_INPUT_DIG_SYNC_ENABLE\x10\xffC\x12?\n:CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_B_INPUT_DIG_FLTR_ENABLE\x10\x80D\x12H\nCCHANNEL_RESET_ATTRIBUTE_CI_ENCODER_B_INPUT_DIG_FLTR_MIN_PULSE_WIDTH\x10\x81D\x12E\n@CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_B_INPUT_DIG_FLTR_TIMEBASE_SRC\x10\x82D\x12F\nACHANNEL_RESET_ATTRIBUTE_CI_ENCODER_B_INPUT_DIG_FLTR_TIMEBASE_RATE\x10\x83D\x12?\n:CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_B_INPUT_DIG_SYNC_ENABLE\x10\x84D\x12?\n:CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_Z_INPUT_DIG_FLTR_ENABLE\x10\x85D\x12H\nCCHANNEL_RESET_ATTRIBUTE_CI_ENCODER_Z_INPUT_DIG_FLTR_MIN_PULSE_WIDTH\x10\x86D\x12E\n@CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_Z_INPUT_DIG_FLTR_TIMEBASE_SRC\x10\x87D\x12F\nACHANNEL_RESET_ATTRIBUTE_CI_ENCODER_Z_INPUT_DIG_FLTR_TIMEBASE_RATE\x10\x88D\x12?\n:CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_Z_INPUT_DIG_SYNC_ENABLE\x10\x89D\x12;\n6CHANNEL_RESET_ATTRIBUTE_CI_PULSE_WIDTH_DIG_FLTR_ENABLE\x10\x8aD\x12D\n?CHANNEL_RESET_ATTRIBUTE_CI_PULSE_WIDTH_DIG_FLTR_MIN_PULSE_WIDTH\x10\x8bD\x12A\n<CHANNEL_RESET_ATTRIBUTE_CI_PULSE_WIDTH_DIG_FLTR_TIMEBASE_SRC\x10\x8cD\x12B\n=CHANNEL_RESET_ATTRIBUTE_CI_PULSE_WIDTH_DIG_FLTR_TIMEBASE_RATE\x10\x8dD\x12;\n6CHANNEL_RESET_ATTRIBUTE_CI_PULSE_WIDTH_DIG_SYNC_ENABLE\x10\x8eD\x12B\n=CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_DIG_FLTR_ENABLE\x10\x8fD\x12K\nFCHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_DIG_FLTR_MIN_PULSE_WIDTH\x10\x90D\x12H\nCCHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_DIG_FLTR_TIMEBASE_SRC\x10\x91D\x12I\nDCHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_DIG_FLTR_TIMEBASE_RATE\x10\x92D\x12B\n=CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_DIG_SYNC_ENABLE\x10\x93D\x12C\n>CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_DIG_FLTR_ENABLE\x10\x94D\x12L\nGCHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_DIG_FLTR_MIN_PULSE_WIDTH\x10\x95D\x12I\nDCHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_DIG_FLTR_TIMEBASE_SRC\x10\x96D\x12J\nECHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_DIG_FLTR_TIMEBASE_RATE\x10\x97D\x12C\n>CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_DIG_SYNC_ENABLE\x10\x98D\x12;\n6CHANNEL_RESET_ATTRIBUTE_CI_SEMI_PERIOD_DIG_FLTR_ENABLE\x10\x99D\x12D\n?CHANNEL_RESET_ATTRIBUTE_CI_SEMI_PERIOD_DIG_FLTR_MIN_PULSE_WIDTH\x10\x9aD\x12A\n<CHANNEL_RESET_ATTRIBUTE_CI_SEMI_PERIOD_DIG_FLTR_TIMEBASE_SRC\x10\x9bD\x12B\n=CHANNEL_RESET_ATTRIBUTE_CI_SEMI_PERIOD_DIG_FLTR_TIMEBASE_RATE\x10\x9cD\x12;\n6CHANNEL_RESET_ATTRIBUTE_CI_SEMI_PERIOD_DIG_SYNC_ENABLE\x10\x9dD\x12)\n$CHANNEL_RESET_ATTRIBUTE_CI_PRESCALER\x10\xb9D\x12E\n@CHANNEL_RESET_ATTRIBUTE_AI_SOUND_PRESSURE_MAX_SOUND_PRESSURE_LVL\x10\xbaD\x124\n/CHANNEL_RESET_ATTRIBUTE_AO_IDLE_OUTPUT_BEHAVIOR\x10\xc0D\x12?\n:CHANNEL_RESET_ATTRIBUTE_AO_ENHANCED_IMAGE_REJECTION_ENABLE\x10\xc1D\x12/\n*CHANNEL_RESET_ATTRIBUTE_AO_DAC_REF_EXT_SRC\x10\xd2D\x12.\n)CHANNEL_RESET_ATTRIBUTE_AO_DAC_OFFSET_SRC\x10\xd3D\x122\n-CHANNEL_RESET_ATTRIBUTE_AO_DAC_OFFSET_EXT_SRC\x10\xd4D\x12.\n)CHANNEL_RESET_ATTRIBUTE_AO_DAC_OFFSET_VAL\x10\xd5D\x12.\n)CHANNEL_RESET_ATTRIBUTE_DI_DATA_XFER_MECH\x10\xe3D\x122\n-CHANNEL_RESET_ATTRIBUTE_DI_DATA_XFER_REQ_COND\x10\xe4D\x123\n.CHANNEL_RESET_ATTRIBUTE_DO_USE_ONLY_ON_BRD_MEM\x10\xe5D\x12.\n)CHANNEL_RESET_ATTRIBUTE_DO_DATA_XFER_MECH\x10\xe6D\x122\n-CHANNEL_RESET_ATTRIBUTE_DO_DATA_XFER_REQ_COND\x10\xe7D\x12)\n$CHANNEL_RESET_ATTRIBUTE_CO_PRESCALER\x10\xedD\x12<\n7CHANNEL_RESET_ATTRIBUTE_CI_CTR_TIMEBASE_DIG_FLTR_ENABLE\x10\xf1D\x12E\n@CHANNEL_RESET_ATTRIBUTE_CI_CTR_TIMEBASE_DIG_FLTR_MIN_PULSE_WIDTH\x10\xf2D\x12B\n=CHANNEL_RESET_ATTRIBUTE_CI_CTR_TIMEBASE_DIG_FLTR_TIMEBASE_SRC\x10\xf3D\x12C\n>CHANNEL_RESET_ATTRIBUTE_CI_CTR_TIMEBASE_DIG_FLTR_TIMEBASE_RATE\x10\xf4D\x12<\n7CHANNEL_RESET_ATTRIBUTE_CI_CTR_TIMEBASE_DIG_SYNC_ENABLE\x10\xf5D\x12<\n7CHANNEL_RESET_ATTRIBUTE_CO_CTR_TIMEBASE_DIG_FLTR_ENABLE\x10\xf6D\x12E\n@CHANNEL_RESET_ATTRIBUTE_CO_CTR_TIMEBASE_DIG_FLTR_MIN_PULSE_WIDTH\x10\xf7D\x12B\n=CHANNEL_RESET_ATTRIBUTE_CO_CTR_TIMEBASE_DIG_FLTR_TIMEBASE_SRC\x10\xf8D\x12C\n>CHANNEL_RESET_ATTRIBUTE_CO_CTR_TIMEBASE_DIG_FLTR_TIMEBASE_RATE\x10\xf9D\x12<\n7CHANNEL_RESET_ATTRIBUTE_CO_CTR_TIMEBASE_DIG_SYNC_ENABLE\x10\xfaD\x12?\n:CHANNEL_RESET_ATTRIBUTE_AI_ENHANCED_ALIAS_REJECTION_ENABLE\x10\x94E\x123\n.CHANNEL_RESET_ATTRIBUTE_AI_CHAN_CAL_ENABLE_CAL\x10\x98E\x129\n4CHANNEL_RESET_ATTRIBUTE_AI_CHAN_CAL_APPLY_CAL_IF_EXP\x10\x99E\x123\n.CHANNEL_RESET_ATTRIBUTE_AI_CHAN_CAL_SCALE_TYPE\x10\x9cE\x12>\n9CHANNEL_RESET_ATTRIBUTE_AI_CHAN_CAL_TABLE_PRE_SCALED_VALS\x10\x9dE\x12:\n5CHANNEL_RESET_ATTRIBUTE_AI_CHAN_CAL_TABLE_SCALED_VALS\x10\x9eE\x12;\n6CHANNEL_RESET_ATTRIBUTE_AI_CHAN_CAL_POLY_FORWARD_COEFF\x10\x9fE\x12;\n6CHANNEL_RESET_ATTRIBUTE_AI_CHAN_CAL_POLY_REVERSE_COEFF\x10\xa0E\x127\n2CHANNEL_RESET_ATTRIBUTE_AI_CHAN_CAL_VERIF_REF_VALS\x10\xa1E\x127\n2CHANNEL_RESET_ATTRIBUTE_AI_CHAN_CAL_VERIF_ACQ_VALS\x10\xa2E\x126\n1CHANNEL_RESET_ATTRIBUTE_AI_CHAN_CAL_OPERATOR_NAME\x10\xa3E\x12-\n(CHANNEL_RESET_ATTRIBUTE_AI_CHAN_CAL_DESC\x10\xa4E\x12/\n*CHANNEL_RESET_ATTRIBUTE_CI_TIMESTAMP_UNITS\x10\xb3E\x129\n4CHANNEL_RESET_ATTRIBUTE_CI_TIMESTAMP_INITIAL_SECONDS\x10\xb4E\x129\n4CHANNEL_RESET_ATTRIBUTE_AI_RAW_DATA_COMPRESSION_TYPE\x10\xd8E\x12F\nACHANNEL_RESET_ATTRIBUTE_AI_LOSSY_LSB_REMOVAL_COMPRESSED_SAMP_SIZE\x10\xd9E\x129\n4CHANNEL_RESET_ATTRIBUTE_CI_SEMI_PERIOD_STARTING_EDGE\x10\xfeE\x12:\n5CHANNEL_RESET_ATTRIBUTE_AI_DATA_XFER_CUSTOM_THRESHOLD\x10\x8cF\x12*\n%CHANNEL_RESET_ATTRIBUTE_DI_ACQUIRE_ON\x10\xe6R\x128\n3CHANNEL_RESET_ATTRIBUTE_DO_LINE_STATES_PAUSED_STATE\x10\xe7R\x126\n1CHANNEL_RESET_ATTRIBUTE_DO_LINE_STATES_DONE_STATE\x10\xe8R\x12+\n&CHANNEL_RESET_ATTRIBUTE_DO_GENERATE_ON\x10\xe9R\x12.\n)CHANNEL_RESET_ATTRIBUTE_DI_MEM_MAP_ENABLE\x10\xeaR\x12.\n)CHANNEL_RESET_ATTRIBUTE_DO_MEM_MAP_ENABLE\x10\xebR\x12,\n\'CHANNEL_RESET_ATTRIBUTE_DI_LOGIC_FAMILY\x10\xedR\x12,\n\'CHANNEL_RESET_ATTRIBUTE_DO_LOGIC_FAMILY\x10\xeeR\x127\n2CHANNEL_RESET_ATTRIBUTE_DO_LINE_STATES_START_STATE\x10\xf2R\x12.\n)CHANNEL_RESET_ATTRIBUTE_AI_VOLTAGE_DB_REF\x10\xb0S\x125\n0CHANNEL_RESET_ATTRIBUTE_AI_SOUND_PRESSURE_DB_REF\x10\xb1S\x12,\n\'CHANNEL_RESET_ATTRIBUTE_AI_ACCEL_DB_REF\x10\xb2S\x122\n-CHANNEL_RESET_ATTRIBUTE_AI_THRMCPL_SCALE_TYPE\x10\xd0S\x124\n/CHANNEL_RESET_ATTRIBUTE_CO_CONSTRAINED_GEN_MODE\x10\xf2S\x12/\n*CHANNEL_RESET_ATTRIBUTE_AI_ADC_TIMING_MODE\x10\xf9S\x12-\n(CHANNEL_RESET_ATTRIBUTE_AO_FUNC_GEN_TYPE\x10\x98T\x12-\n(CHANNEL_RESET_ATTRIBUTE_AO_FUNC_GEN_FREQ\x10\x99T\x122\n-CHANNEL_RESET_ATTRIBUTE_AO_FUNC_GEN_AMPLITUDE\x10\x9aT\x12/\n*CHANNEL_RESET_ATTRIBUTE_AO_FUNC_GEN_OFFSET\x10\x9bT\x12:\n5CHANNEL_RESET_ATTRIBUTE_AO_FUNC_GEN_SQUARE_DUTY_CYCLE\x10\x9cT\x125\n0CHANNEL_RESET_ATTRIBUTE_AO_VOLTAGE_CURRENT_LIMIT\x10\x9dT\x128\n3CHANNEL_RESET_ATTRIBUTE_AO_FUNC_GEN_MODULATION_TYPE\x10\xa2T\x125\n0CHANNEL_RESET_ATTRIBUTE_AO_FUNC_GEN_FM_DEVIATION\x10\xa3T\x121\n,CHANNEL_RESET_ATTRIBUTE_DO_OVERCURRENT_LIMIT\x10\x85U\x129\n4CHANNEL_RESET_ATTRIBUTE_DO_OVERCURRENT_AUTO_REENABLE\x10\x86U\x12;\n6CHANNEL_RESET_ATTRIBUTE_DO_OVERCURRENT_REENABLE_PERIOD\x10\x87U\x12+\n&CHANNEL_RESET_ATTRIBUTE_AI_PROBE_ATTEN\x10\x88U\x12)\n$CHANNEL_RESET_ATTRIBUTE_AI_DC_OFFSET\x10\x89U\x121\n,CHANNEL_RESET_ATTRIBUTE_AI_USB_XFER_REQ_SIZE\x10\x8eU\x121\n,CHANNEL_RESET_ATTRIBUTE_AO_USB_XFER_REQ_SIZE\x10\x8fU\x121\n,CHANNEL_RESET_ATTRIBUTE_DI_USB_XFER_REQ_SIZE\x10\x90U\x121\n,CHANNEL_RESET_ATTRIBUTE_DO_USB_XFER_REQ_SIZE\x10\x91U\x121\n,CHANNEL_RESET_ATTRIBUTE_CI_USB_XFER_REQ_SIZE\x10\x92U\x121\n,CHANNEL_RESET_ATTRIBUTE_CO_USB_XFER_REQ_SIZE\x10\x93U\x12C\n>CHANNEL_RESET_ATTRIBUTE_AI_EDDY_CURRENT_PROX_PROBE_SENSITIVITY\x10\xbeU\x12I\nDCHANNEL_RESET_ATTRIBUTE_AI_EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS\x10\xbfU\x12=\n8CHANNEL_RESET_ATTRIBUTE_AI_EDDY_CURRENT_PROX_PROBE_UNITS\x10\xc0U\x12A\n<CHANNEL_RESET_ATTRIBUTE_CO_ENABLE_INITIAL_DELAY_ON_RETRIGGER\x10\xc9]\x123\n.CHANNEL_RESET_ATTRIBUTE_CO_USE_ONLY_ON_BRD_MEM\x10\xcb]\x12.\n)CHANNEL_RESET_ATTRIBUTE_CO_DATA_XFER_MECH\x10\xcc]\x122\n-CHANNEL_RESET_ATTRIBUTE_CO_DATA_XFER_REQ_COND\x10\xcd]\x125\n0CHANNEL_RESET_ATTRIBUTE_CI_FREQ_ENABLE_AVERAGING\x10\xd0]\x127\n2CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_ENABLE_AVERAGING\x10\xd1]\x12.\n)CHANNEL_RESET_ATTRIBUTE_CI_MEM_MAP_ENABLE\x10\xd2]\x12.\n)CHANNEL_RESET_ATTRIBUTE_CO_MEM_MAP_ENABLE\x10\xd3]\x125\n0CHANNEL_RESET_ATTRIBUTE_DI_DIG_FLTR_TIMEBASE_SRC\x10\xd4]\x126\n1CHANNEL_RESET_ATTRIBUTE_DI_DIG_FLTR_TIMEBASE_RATE\x10\xd5]\x12/\n*CHANNEL_RESET_ATTRIBUTE_DI_DIG_SYNC_ENABLE\x10\xd6]\x122\n-CHANNEL_RESET_ATTRIBUTE_CI_DATA_XFER_REQ_COND\x10\xfb]\x128\n3CHANNEL_RESET_ATTRIBUTE_DI_DIG_FLTR_ENABLE_BUS_MODE\x10\xfe]\x12/\n*CHANNEL_RESET_ATTRIBUTE_CI_PULSE_FREQ_TERM\x10\x84^\x125\n0CHANNEL_RESET_ATTRIBUTE_CI_PULSE_FREQ_START_EDGE\x10\x85^\x12:\n5CHANNEL_RESET_ATTRIBUTE_CI_PULSE_FREQ_DIG_FLTR_ENABLE\x10\x86^\x12C\n>CHANNEL_RESET_ATTRIBUTE_CI_PULSE_FREQ_DIG_FLTR_MIN_PULSE_WIDTH\x10\x87^\x12@\n;CHANNEL_RESET_ATTRIBUTE_CI_PULSE_FREQ_DIG_FLTR_TIMEBASE_SRC\x10\x88^\x12A\n<CHANNEL_RESET_ATTRIBUTE_CI_PULSE_FREQ_DIG_FLTR_TIMEBASE_RATE\x10\x89^\x12:\n5CHANNEL_RESET_ATTRIBUTE_CI_PULSE_FREQ_DIG_SYNC_ENABLE\x10\x8a^\x120\n+CHANNEL_RESET_ATTRIBUTE_CI_PULSE_FREQ_UNITS\x10\x8b^\x12/\n*CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TIME_TERM\x10\x8c^\x125\n0CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TIME_START_EDGE\x10\x8d^\x12:\n5CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TIME_DIG_FLTR_ENABLE\x10\x8e^\x12C\n>CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TIME_DIG_FLTR_MIN_PULSE_WIDTH\x10\x8f^\x12@\n;CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TIME_DIG_FLTR_TIMEBASE_SRC\x10\x90^\x12A\n<CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TIME_DIG_FLTR_TIMEBASE_RATE\x10\x91^\x12:\n5CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TIME_DIG_SYNC_ENABLE\x10\x92^\x120\n+CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TIME_UNITS\x10\x93^\x120\n+CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TICKS_TERM\x10\x94^\x126\n1CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TICKS_START_EDGE\x10\x95^\x12;\n6CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TICKS_DIG_FLTR_ENABLE\x10\x96^\x12D\n?CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TICKS_DIG_FLTR_MIN_PULSE_WIDTH\x10\x97^\x12A\n<CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TICKS_DIG_FLTR_TIMEBASE_SRC\x10\x98^\x12B\n=CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TICKS_DIG_FLTR_TIMEBASE_RATE\x10\x99^\x12;\n6CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TICKS_DIG_SYNC_ENABLE\x10\x9a^\x126\n1CHANNEL_RESET_ATTRIBUTE_AI_ADC_CUSTOM_TIMING_MODE\x10\xeb^\x12:\n5CHANNEL_RESET_ATTRIBUTE_AI_OPEN_THRMCPL_DETECT_ENABLE\x10\xf2^\x12+\n&CHANNEL_RESET_ATTRIBUTE_AI_FORCE_UNITS\x10\xf5^\x12.\n)CHANNEL_RESET_ATTRIBUTE_AI_PRESSURE_UNITS\x10\xf6^\x12,\n\'CHANNEL_RESET_ATTRIBUTE_AI_TORQUE_UNITS\x10\xf7^\x12G\nBCHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_A_RESISTANCE\x10\xf8^\x12N\nICHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_A_ACTUAL_RESISTANCE\x10\xf9^\x12G\nBCHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_B_RESISTANCE\x10\xfa^\x12N\nICHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_B_ACTUAL_RESISTANCE\x10\xfb^\x12=\n8CHANNEL_RESET_ATTRIBUTE_AI_FORCE_IEPE_SENSOR_SENSITIVITY\x10\x81_\x12C\n>CHANNEL_RESET_ATTRIBUTE_AI_FORCE_IEPE_SENSOR_SENSITIVITY_UNITS\x10\x82_\x124\n/CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_INITIAL_RATIO\x10\x86_\x127\n2CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_ELECTRICAL_UNITS\x10\x87_\x125\n0CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_PHYSICAL_UNITS\x10\x88_\x121\n,CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_SCALE_TYPE\x10\x89_\x12I\nDCHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_TWO_POINT_LIN_FIRST_ELECTRICAL_VAL\x10\x8a_\x12G\nBCHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_TWO_POINT_LIN_FIRST_PHYSICAL_VAL\x10\x8b_\x12J\nECHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_TWO_POINT_LIN_SECOND_ELECTRICAL_VAL\x10\x8c_\x12H\nCCHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_TWO_POINT_LIN_SECOND_PHYSICAL_VAL\x10\x8d_\x12<\n7CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_TABLE_ELECTRICAL_VALS\x10\x8e_\x12:\n5CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_TABLE_PHYSICAL_VALS\x10\x8f_\x129\n4CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_POLY_FORWARD_COEFF\x10\x90_\x129\n4CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_POLY_REVERSE_COEFF\x10\x91_\x12,\n\'CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_UNITS\x10\x92_\x12>\n9CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_ENABLE\x10\xaf_\x12C\n>CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_RESET_COUNT\x10\xb0_\x12<\n7CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_TERM\x10\xb1_\x12C\n>CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_ACTIVE_EDGE\x10\xb2_\x12G\nBCHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_DIG_FLTR_ENABLE\x10\xb3_\x12P\nKCHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_DIG_FLTR_MIN_PULSE_WIDTH\x10\xb4_\x12M\nHCHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_DIG_FLTR_TIMEBASE_SRC\x10\xb5_\x12N\nICHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_DIG_FLTR_TIMEBASE_RATE\x10\xb6_\x12G\nBCHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_DIG_SYNC_ENABLE\x10\xb7_\x12;\n6CHANNEL_RESET_ATTRIBUTE_AI_THRMCPL_LEAD_OFFSET_VOLTAGE\x10\xb8_\x123\n.CHANNEL_RESET_ATTRIBUTE_AI_REMOVE_FILTER_DELAY\x10\xbd_\x122\n-CHANNEL_RESET_ATTRIBUTE_AI_AVERAGING_WIN_SIZE\x10\xee_\x12.\n)CHANNEL_RESET_ATTRIBUTE_AI_VELOCITY_UNITS\x10\xf4_\x12;\n6CHANNEL_RESET_ATTRIBUTE_AI_VELOCITY_IEPE_SENSOR_DB_REF\x10\xf5_\x12@\n;CHANNEL_RESET_ATTRIBUTE_AI_VELOCITY_IEPE_SENSOR_SENSITIVITY\x10\xf6_\x12F\nACHANNEL_RESET_ATTRIBUTE_AI_VELOCITY_IEPE_SENSOR_SENSITIVITY_UNITS\x10\xf7_\x12@\n;CHANNEL_RESET_ATTRIBUTE_AI_STRAIN_GAGE_FORCE_READ_FROM_CHAN\x10\xfa_\x12?\n:CHANNEL_RESET_ATTRIBUTE_AI_ROSETTE_STRAIN_GAGE_ORIENTATION\x10\xfc_\x12E\n@CHANNEL_RESET_ATTRIBUTE_AI_ROSETTE_STRAIN_GAGE_ROSETTE_MEAS_TYPE\x10\xfd_\x122\n-CHANNEL_RESET_ATTRIBUTE_AI_USB_XFER_REQ_COUNT\x10\x80`\x122\n-CHANNEL_RESET_ATTRIBUTE_AO_USB_XFER_REQ_COUNT\x10\x81`\x122\n-CHANNEL_RESET_ATTRIBUTE_DI_USB_XFER_REQ_COUNT\x10\x82`\x122\n-CHANNEL_RESET_ATTRIBUTE_DO_USB_XFER_REQ_COUNT\x10\x83`\x122\n-CHANNEL_RESET_ATTRIBUTE_CI_USB_XFER_REQ_COUNT\x10\x84`\x122\n-CHANNEL_RESET_ATTRIBUTE_CO_USB_XFER_REQ_COUNT\x10\x85`\x12.\n)CHANNEL_RESET_ATTRIBUTE_CI_TIMESTAMP_TERM\x10\xb9`\x12.\n)CHANNEL_RESET_ATTRIBUTE_CI_TIMESTAMP_EDGE\x10\xba`\x123\n.CHANNEL_RESET_ATTRIBUTE_CI_TIMESTAMP_TIMESCALE\x10\xbb`\x122\n-CHANNEL_RESET_ATTRIBUTE_NAV_CUSTOM_SCALE_NAME\x10\xbc`\x12*\n%CHANNEL_RESET_ATTRIBUTE_NAV_ALT_UNITS\x10\xbe`\x12*\n%CHANNEL_RESET_ATTRIBUTE_NAV_LAT_UNITS\x10\xbf`\x12+\n&CHANNEL_RESET_ATTRIBUTE_NAV_LONG_UNITS\x10\xc0`\x128\n3CHANNEL_RESET_ATTRIBUTE_NAV_SPEED_OVER_GROUND_UNITS\x10\xc1`\x12,\n\'CHANNEL_RESET_ATTRIBUTE_NAV_TRACK_UNITS\x10\xc2`\x124\n/CHANNEL_RESET_ATTRIBUTE_NAV_VERT_VELOCITY_UNITS\x10\xc3`\x120\n+CHANNEL_RESET_ATTRIBUTE_NAV_TIMESTAMP_UNITS\x10\xc4`\x124\n/CHANNEL_RESET_ATTRIBUTE_NAV_TIMESTAMP_TIMESCALE\x10\xc5`\x122\n-CHANNEL_RESET_ATTRIBUTE_AI_FILTER_DELAY_UNITS\x10\xf1`\x127\n2CHANNEL_RESET_ATTRIBUTE_AO_FILTER_DELAY_ADJUSTMENT\x10\xf2`\x127\n2CHANNEL_RESET_ATTRIBUTE_AI_FILTER_DELAY_ADJUSTMENT\x10\xf4`\x12,\n\'CHANNEL_RESET_ATTRIBUTE_AO_FILTER_DELAY\x10\xf5`\x122\n-CHANNEL_RESET_ATTRIBUTE_AO_FILTER_DELAY_UNITS\x10\xf6`\x12/\n*CHANNEL_RESET_ATTRIBUTE_CI_DUTY_CYCLE_TERM\x10\x8da\x12:\n5CHANNEL_RESET_ATTRIBUTE_CI_DUTY_CYCLE_DIG_FLTR_ENABLE\x10\x8ea\x12C\n>CHANNEL_RESET_ATTRIBUTE_CI_DUTY_CYCLE_DIG_FLTR_MIN_PULSE_WIDTH\x10\x8fa\x12@\n;CHANNEL_RESET_ATTRIBUTE_CI_DUTY_CYCLE_DIG_FLTR_TIMEBASE_SRC\x10\x90a\x12A\n<CHANNEL_RESET_ATTRIBUTE_CI_DUTY_CYCLE_DIG_FLTR_TIMEBASE_RATE\x10\x91a\x128\n3CHANNEL_RESET_ATTRIBUTE_CI_DUTY_CYCLE_STARTING_EDGE\x10\x92a\x129\n4CHANNEL_RESET_ATTRIBUTE_CI_SAMP_CLK_OVERRUN_BEHAVIOR\x10\x93a\x12=\n8CHANNEL_RESET_ATTRIBUTE_CI_SAMP_CLK_OVERRUN_SENTINEL_VAL\x10\x94a\x12/\n*CHANNEL_RESET_ATTRIBUTE_CI_MAX_MEAS_PERIOD\x10\x95a\x12-\n(CHANNEL_RESET_ATTRIBUTE_CI_FREQ_TERM_CFG\x10\x97a\x127\n2CHANNEL_RESET_ATTRIBUTE_CI_FREQ_LOGIC_LVL_BEHAVIOR\x10\x98a\x12/\n*CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_TERM_CFG\x10\x99a\x129\n4CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_LOGIC_LVL_BEHAVIOR\x10\x9aa\x124\n/CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_TERM_CFG\x10\x9ba\x12>\n9CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_LOGIC_LVL_BEHAVIOR\x10\x9ca\x12>\n9CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_TERM_CFG\x10\x9da\x12H\nCCHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_LOGIC_LVL_BEHAVIOR\x10\x9ea\x12@\n;CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_TERM_CFG\x10\x9fa\x12J\nECHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_LOGIC_LVL_BEHAVIOR\x10\xa0a\x123\n.CHANNEL_RESET_ATTRIBUTE_CI_DUTY_CYCLE_TERM_CFG\x10\xa1a\x12=\n8CHANNEL_RESET_ATTRIBUTE_CI_DUTY_CYCLE_LOGIC_LVL_BEHAVIOR\x10\xa2a\x128\n3CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_A_INPUT_TERM_CFG\x10\xa3a\x12B\n=CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_A_INPUT_LOGIC_LVL_BEHAVIOR\x10\xa4a\x128\n3CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_B_INPUT_TERM_CFG\x10\xa5a\x12B\n=CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_B_INPUT_LOGIC_LVL_BEHAVIOR\x10\xa6a\x128\n3CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_Z_INPUT_TERM_CFG\x10\xa7a\x12B\n=CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_Z_INPUT_LOGIC_LVL_BEHAVIOR\x10\xa8a\x124\n/CHANNEL_RESET_ATTRIBUTE_CI_PULSE_WIDTH_TERM_CFG\x10\xa9a\x12>\n9CHANNEL_RESET_ATTRIBUTE_CI_PULSE_WIDTH_LOGIC_LVL_BEHAVIOR\x10\xaaa\x12;\n6CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_TERM_CFG\x10\xaba\x12E\n@CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_LOGIC_LVL_BEHAVIOR\x10\xaca\x12<\n7CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_TERM_CFG\x10\xada\x12F\nACHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_LOGIC_LVL_BEHAVIOR\x10\xaea\x124\n/CHANNEL_RESET_ATTRIBUTE_CI_SEMI_PERIOD_TERM_CFG\x10\xafa\x12>\n9CHANNEL_RESET_ATTRIBUTE_CI_SEMI_PERIOD_LOGIC_LVL_BEHAVIOR\x10\xb0a\x123\n.CHANNEL_RESET_ATTRIBUTE_CI_PULSE_FREQ_TERM_CFG\x10\xb1a\x12=\n8CHANNEL_RESET_ATTRIBUTE_CI_PULSE_FREQ_LOGIC_LVL_BEHAVIOR\x10\xb2a\x123\n.CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TIME_TERM_CFG\x10\xb3a\x12=\n8CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TIME_LOGIC_LVL_BEHAVIOR\x10\xb4a\x124\n/CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TICKS_TERM_CFG\x10\xb5a\x12>\n9CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TICKS_LOGIC_LVL_BEHAVIOR\x10\xb6a\x12.\n)CHANNEL_RESET_ATTRIBUTE_CI_THRESH_VOLTAGE\x10\xb7a\x12:\n5CHANNEL_RESET_ATTRIBUTE_AI_EXCIT_IDLE_OUTPUT_BEHAVIOR\x10\xb8a\x12/\n*CHANNEL_RESET_ATTRIBUTE_AI_DIG_FLTR_ENABLE\x10\xbda\x12-\n(CHANNEL_RESET_ATTRIBUTE_AI_DIG_FLTR_TYPE\x10\xbea\x121\n,CHANNEL_RESET_ATTRIBUTE_AI_DIG_FLTR_RESPONSE\x10\xbfa\x12.\n)CHANNEL_RESET_ATTRIBUTE_AI_DIG_FLTR_ORDER\x10\xc0a\x12<\n7CHANNEL_RESET_ATTRIBUTE_AI_DIG_FLTR_LOWPASS_CUTOFF_FREQ\x10\xc1a\x12=\n8CHANNEL_RESET_ATTRIBUTE_AI_DIG_FLTR_HIGHPASS_CUTOFF_FREQ\x10\xc2a\x12=\n8CHANNEL_RESET_ATTRIBUTE_AI_DIG_FLTR_BANDPASS_CENTER_FREQ\x10\xc3a\x127\n2CHANNEL_RESET_ATTRIBUTE_AI_DIG_FLTR_BANDPASS_WIDTH\x10\xc4a\x12:\n5CHANNEL_RESET_ATTRIBUTE_AI_DIG_FLTR_NOTCH_CENTER_FREQ\x10\xc5a\x124\n/CHANNEL_RESET_ATTRIBUTE_AI_DIG_FLTR_NOTCH_WIDTH\x10\xc6a\x12.\n)CHANNEL_RESET_ATTRIBUTE_AI_DIG_FLTR_COEFF\x10\xc7a\x12@\n;CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_A_SRC\x10\xcaa\x12:\n5CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ANG_ENCODER_UNITS\x10\xd8a\x12C\n>CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ANG_ENCODER_PULSES_PER_REV\x10\xd9a\x12:\n5CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_LIN_ENCODER_UNITS\x10\xdaa\x12C\n>CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_LIN_ENCODER_DIST_PER_PULSE\x10\xdba\x12>\n9CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_DECODING_TYPE\x10\xdca\x12=\n8CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_TERM\x10\xdda\x12A\n<CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_TERM_CFG\x10\xdea\x12K\nFCHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_LOGIC_LVL_BEHAVIOR\x10\xdfa\x12H\nCCHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_DIG_FLTR_ENABLE\x10\xe0a\x12Q\nLCHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_DIG_FLTR_MIN_PULSE_WIDTH\x10\xe1a\x12N\nICHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_DIG_FLTR_TIMEBASE_SRC\x10\xe2a\x12O\nJCHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_DIG_FLTR_TIMEBASE_RATE\x10\xe3a\x12=\n8CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_TERM\x10\xe4a\x12A\n<CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_TERM_CFG\x10\xe5a\x12K\nFCHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_LOGIC_LVL_BEHAVIOR\x10\xe6a\x12H\nCCHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_DIG_FLTR_ENABLE\x10\xe7a\x12Q\nLCHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_DIG_FLTR_MIN_PULSE_WIDTH\x10\xe8a\x12N\nICHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_DIG_FLTR_TIMEBASE_SRC\x10\xe9a\x12O\nJCHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_DIG_FLTR_TIMEBASE_RATE\x10\xeaa\x122\n-CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_MEAS_TIME\x10\xeba\x12,\n\'CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_DIV\x10\xeca\x127\n2CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_GATE_ENABLE\x10\xeda\x125\n0CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_GATE_TERM\x10\xeea\x129\n4CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_GATE_TERM_CFG\x10\xefa\x12C\n>CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_GATE_LOGIC_LVL_BEHAVIOR\x10\xf0a\x12@\n;CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_GATE_DIG_FLTR_ENABLE\x10\xf1a\x12I\nDCHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_GATE_DIG_FLTR_MIN_PULSE_WIDTH\x10\xf2a\x12F\nACHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_GATE_DIG_FLTR_TIMEBASE_SRC\x10\xf3a\x12G\nBCHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_GATE_DIG_FLTR_TIMEBASE_RATE\x10\xf4a\x125\n0CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_GATE_WHEN\x10\xf5a\x12@\n;CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_B_SRC\x10\xf7a\x12+\n&CHANNEL_RESET_ATTRIBUTE_AI_EXCIT_SENSE\x10\xfda\x127\n2CHANNEL_RESET_ATTRIBUTE_AI_OPEN_CHAN_DETECT_ENABLE\x10\xffa\x12,\n\'CHANNEL_RESET_ATTRIBUTE_AI_CHARGE_UNITS\x10\x92b\x128\n3CHANNEL_RESET_ATTRIBUTE_AI_ACCEL_CHARGE_SENSITIVITY\x10\x93b\x12>\n9CHANNEL_RESET_ATTRIBUTE_AI_ACCEL_CHARGE_SENSITIVITY_UNITS\x10\x94b\x12C\n>CHANNEL_RESET_ATTRIBUTE_AI_ACCEL_4_WIRE_DC_VOLTAGE_SENSITIVITY\x10\x95b\x12I\nDCHANNEL_RESET_ATTRIBUTE_AI_ACCEL_4_WIRE_DC_VOLTAGE_SENSITIVITY_UNITS\x10\x96b\x122\n-CHANNEL_RESET_ATTRIBUTE_AI_DATA_XFER_MAX_RATE\x10\x97b\x126\n1CHANNEL_RESET_ATTRIBUTE_CHAN_SYNC_UNLOCK_BEHAVIOR\x10\xbcb\x12+\n&CHANNEL_RESET_ATTRIBUTE_AI_CHOP_ENABLE\x10\xc3b\x124\n/CHANNEL_RESET_ATTRIBUTE_AI_SENSOR_POWER_VOLTAGE\x10\xe9b\x120\n+CHANNEL_RESET_ATTRIBUTE_AI_SENSOR_POWER_CFG\x10\xeab\x121\n,CHANNEL_RESET_ATTRIBUTE_AI_SENSOR_POWER_TYPE\x10\xebb\x12-\n(CHANNEL_RESET_ATTRIBUTE_AI_FILTER_ENABLE\x10\xf3b\x12+\n&CHANNEL_RESET_ATTRIBUTE_AI_FILTER_FREQ\x10\xf4b\x12/\n*CHANNEL_RESET_ATTRIBUTE_AI_FILTER_RESPONSE\x10\xf5b\x12,\n\'CHANNEL_RESET_ATTRIBUTE_AI_FILTER_ORDER\x10\xf6b\x12E\n@CHANNEL_RESET_ATTRIBUTE_AI_INPUT_LIMITS_FAULT_DETECT_UPPER_LIMIT\x10\x8cc\x12E\n@CHANNEL_RESET_ATTRIBUTE_AI_INPUT_LIMITS_FAULT_DETECT_LOWER_LIMIT\x10\x8dc\x12@\n;CHANNEL_RESET_ATTRIBUTE_AI_INPUT_LIMITS_FAULT_DETECT_ENABLE\x10\x8ec\x12@\n;CHANNEL_RESET_ATTRIBUTE_AI_POWER_SUPPLY_FAULT_DETECT_ENABLE\x10\x91c\x129\n4CHANNEL_RESET_ATTRIBUTE_AI_OVERCURRENT_DETECT_ENABLE\x10\x94c\x123\n.CHANNEL_RESET_ATTRIBUTE_CI_FREQ_THRESH_VOLTAGE\x10\xabc\x12)\n$CHANNEL_RESET_ATTRIBUTE_CI_FREQ_HYST\x10\xacc\x125\n0CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_THRESH_VOLTAGE\x10\xadc\x12+\n&CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_HYST\x10\xaec\x12:\n5CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_THRESH_VOLTAGE\x10\xafc\x120\n+CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_HYST\x10\xb0c\x12D\n?CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_THRESH_VOLTAGE\x10\xb1c\x12:\n5CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_HYST\x10\xb2c\x12F\nACHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_THRESH_VOLTAGE\x10\xb3c\x12<\n7CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_HYST\x10\xb4c\x12?\n:CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_GATE_THRESH_VOLTAGE\x10\xb5c\x125\n0CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_GATE_HYST\x10\xb6c\x12-\n(CHANNEL_RESET_ATTRIBUTE_CI_FILTER_ENABLE\x10\xb7c\x12+\n&CHANNEL_RESET_ATTRIBUTE_CI_FILTER_FREQ\x10\xb8c\x12/\n*CHANNEL_RESET_ATTRIBUTE_CI_FILTER_RESPONSE\x10\xb9c\x12,\n\'CHANNEL_RESET_ATTRIBUTE_CI_FILTER_ORDER\x10\xbac\x122\n-CHANNEL_RESET_ATTRIBUTE_CI_FILTER_DELAY_UNITS\x10\xbcc\x124\n/CHANNEL_RESET_ATTRIBUTE_AO_FUNC_GEN_START_PHASE\x10\xc4c\x122\n-CHANNEL_RESET_ATTRIBUTE_AO_COMMON_MODE_OFFSET\x10\xccc\x121\n,CHANNEL_RESET_ATTRIBUTE_PWR_VOLTAGE_SETPOINT\x10\xd4c\x121\n,CHANNEL_RESET_ATTRIBUTE_PWR_CURRENT_SETPOINT\x10\xd5c\x12.\n)CHANNEL_RESET_ATTRIBUTE_PWR_OUTPUT_ENABLE\x10\xd6c\x125\n0CHANNEL_RESET_ATTRIBUTE_PWR_IDLE_OUTPUT_BEHAVIOR\x10\xd8c\x12-\n(CHANNEL_RESET_ATTRIBUTE_PWR_REMOTE_SENSE\x10\xdbc\x12+\n&CHANNEL_RESET_ATTRIBUTE_AI_POWER_UNITS\x10\xecc\x12<\n7CHANNEL_RESET_ATTRIBUTE_AI_CALCULATED_POWER_VOLTAGE_MAX\x10\xedc\x12<\n7CHANNEL_RESET_ATTRIBUTE_AI_CALCULATED_POWER_VOLTAGE_MIN\x10\xeec\x12<\n7CHANNEL_RESET_ATTRIBUTE_AI_CALCULATED_POWER_CURRENT_MAX\x10\xefc\x12<\n7CHANNEL_RESET_ATTRIBUTE_AI_CALCULATED_POWER_CURRENT_MIN\x10\xf0c*\x9a\'\n\x14ChannelBoolAttribute\x12&\n"CHANNEL_BOOL_ATTRIBUTE_UNSPECIFIED\x10\x00\x12&\n"CHANNEL_ATTRIBUTE_AI_DITHER_ENABLE\x10h\x121\n,CHANNEL_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_ENABLE\x10\x94\x01\x12.\n)CHANNEL_ATTRIBUTE_AI_AC_EXCIT_SYNC_ENABLE\x10\x82\x02\x12-\n(CHANNEL_ATTRIBUTE_AO_DAC_REF_CONN_TO_GND\x10\xb0\x02\x12)\n$CHANNEL_ATTRIBUTE_AO_REGLITCH_ENABLE\x10\xb3\x02\x12$\n\x1fCHANNEL_ATTRIBUTE_CI_TC_REACHED\x10\xd0\x02\x12&\n!CHANNEL_ATTRIBUTE_DI_INVERT_LINES\x10\x93\x0f\x120\n+CHANNEL_ATTRIBUTE_CI_ENCODER_Z_INDEX_ENABLE\x10\x90\x11\x12&\n!CHANNEL_ATTRIBUTE_DO_INVERT_LINES\x10\xb3"\x12/\n*CHANNEL_ATTRIBUTE_AI_EXCIT_USE_FOR_SCALING\x10\xfc/\x12(\n#CHANNEL_ATTRIBUTE_AI_LOWPASS_ENABLE\x10\x820\x12)\n$CHANNEL_ATTRIBUTE_AI_HIGHPASS_ENABLE\x10\x860\x12)\n$CHANNEL_ATTRIBUTE_AI_BANDPASS_ENABLE\x10\x8b0\x12.\n)CHANNEL_ATTRIBUTE_AI_SAMP_AND_HOLD_ENABLE\x10\x9a0\x123\n.CHANNEL_ATTRIBUTE_AO_DAC_REF_ALLOW_CONN_TO_GND\x10\xb00\x12-\n(CHANNEL_ATTRIBUTE_AO_USE_ONLY_ON_BRD_MEM\x10\xba0\x12(\n#CHANNEL_ATTRIBUTE_AI_MEM_MAP_ENABLE\x10\x8c1\x12(\n#CHANNEL_ATTRIBUTE_AO_MEM_MAP_ENABLE\x10\x8f1\x12"\n\x1dCHANNEL_ATTRIBUTE_DI_TRISTATE\x10\x901\x12"\n\x1dCHANNEL_ATTRIBUTE_DO_TRISTATE\x10\xf31\x12.\n)CHANNEL_ATTRIBUTE_AI_FORCE_READ_FROM_CHAN\x10\xf81\x12$\n\x1fCHANNEL_ATTRIBUTE_CO_PULSE_DONE\x10\x8e2\x12/\n*CHANNEL_ATTRIBUTE_AI_EXCIT_USE_MULTIPLEXED\x10\x80C\x12+\n&CHANNEL_ATTRIBUTE_CI_DUP_COUNT_PREVENT\x10\xacC\x12)\n$CHANNEL_ATTRIBUTE_DI_DIG_FLTR_ENABLE\x10\xd6C\x12.\n)CHANNEL_ATTRIBUTE_CI_FREQ_DIG_FLTR_ENABLE\x10\xe7C\x12.\n)CHANNEL_ATTRIBUTE_CI_FREQ_DIG_SYNC_ENABLE\x10\xebC\x120\n+CHANNEL_ATTRIBUTE_CI_PERIOD_DIG_FLTR_ENABLE\x10\xecC\x120\n+CHANNEL_ATTRIBUTE_CI_PERIOD_DIG_SYNC_ENABLE\x10\xf0C\x12?\n:CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_DIG_FLTR_ENABLE\x10\xf1C\x12?\n:CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_DIG_SYNC_ENABLE\x10\xf5C\x125\n0CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_DIG_FLTR_ENABLE\x10\xf6C\x125\n0CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_DIG_SYNC_ENABLE\x10\xfaC\x129\n4CHANNEL_ATTRIBUTE_CI_ENCODER_A_INPUT_DIG_FLTR_ENABLE\x10\xfbC\x129\n4CHANNEL_ATTRIBUTE_CI_ENCODER_A_INPUT_DIG_SYNC_ENABLE\x10\xffC\x129\n4CHANNEL_ATTRIBUTE_CI_ENCODER_B_INPUT_DIG_FLTR_ENABLE\x10\x80D\x129\n4CHANNEL_ATTRIBUTE_CI_ENCODER_B_INPUT_DIG_SYNC_ENABLE\x10\x84D\x129\n4CHANNEL_ATTRIBUTE_CI_ENCODER_Z_INPUT_DIG_FLTR_ENABLE\x10\x85D\x129\n4CHANNEL_ATTRIBUTE_CI_ENCODER_Z_INPUT_DIG_SYNC_ENABLE\x10\x89D\x125\n0CHANNEL_ATTRIBUTE_CI_PULSE_WIDTH_DIG_FLTR_ENABLE\x10\x8aD\x125\n0CHANNEL_ATTRIBUTE_CI_PULSE_WIDTH_DIG_SYNC_ENABLE\x10\x8eD\x12<\n7CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_DIG_FLTR_ENABLE\x10\x8fD\x12<\n7CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_DIG_SYNC_ENABLE\x10\x93D\x12=\n8CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_DIG_FLTR_ENABLE\x10\x94D\x12=\n8CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_DIG_SYNC_ENABLE\x10\x98D\x125\n0CHANNEL_ATTRIBUTE_CI_SEMI_PERIOD_DIG_FLTR_ENABLE\x10\x99D\x125\n0CHANNEL_ATTRIBUTE_CI_SEMI_PERIOD_DIG_SYNC_ENABLE\x10\x9dD\x129\n4CHANNEL_ATTRIBUTE_AO_ENHANCED_IMAGE_REJECTION_ENABLE\x10\xc1D\x12-\n(CHANNEL_ATTRIBUTE_DO_USE_ONLY_ON_BRD_MEM\x10\xe5D\x126\n1CHANNEL_ATTRIBUTE_CI_CTR_TIMEBASE_DIG_FLTR_ENABLE\x10\xf1D\x126\n1CHANNEL_ATTRIBUTE_CI_CTR_TIMEBASE_DIG_SYNC_ENABLE\x10\xf5D\x126\n1CHANNEL_ATTRIBUTE_CO_CTR_TIMEBASE_DIG_FLTR_ENABLE\x10\xf6D\x126\n1CHANNEL_ATTRIBUTE_CO_CTR_TIMEBASE_DIG_SYNC_ENABLE\x10\xfaD\x129\n4CHANNEL_ATTRIBUTE_AI_ENHANCED_ALIAS_REJECTION_ENABLE\x10\x94E\x125\n0CHANNEL_ATTRIBUTE_AI_CHAN_CAL_HAS_VALID_CAL_INFO\x10\x97E\x12-\n(CHANNEL_ATTRIBUTE_AI_CHAN_CAL_ENABLE_CAL\x10\x98E\x123\n.CHANNEL_ATTRIBUTE_AI_CHAN_CAL_APPLY_CAL_IF_EXP\x10\x99E\x12)\n$CHANNEL_ATTRIBUTE_CO_RDY_FOR_NEW_VAL\x10\xffE\x12%\n CHANNEL_ATTRIBUTE_CHAN_IS_GLOBAL\x10\x84F\x12(\n#CHANNEL_ATTRIBUTE_DI_MEM_MAP_ENABLE\x10\xeaR\x12(\n#CHANNEL_ATTRIBUTE_DO_MEM_MAP_ENABLE\x10\xebR\x12!\n\x1cCHANNEL_ATTRIBUTE_AI_IS_TEDS\x10\x83S\x123\n.CHANNEL_ATTRIBUTE_DO_OVERCURRENT_AUTO_REENABLE\x10\x86U\x12;\n6CHANNEL_ATTRIBUTE_CO_ENABLE_INITIAL_DELAY_ON_RETRIGGER\x10\xc9]\x12-\n(CHANNEL_ATTRIBUTE_CO_USE_ONLY_ON_BRD_MEM\x10\xcb]\x12/\n*CHANNEL_ATTRIBUTE_CI_FREQ_ENABLE_AVERAGING\x10\xd0]\x121\n,CHANNEL_ATTRIBUTE_CI_PERIOD_ENABLE_AVERAGING\x10\xd1]\x12(\n#CHANNEL_ATTRIBUTE_CI_MEM_MAP_ENABLE\x10\xd2]\x12(\n#CHANNEL_ATTRIBUTE_CO_MEM_MAP_ENABLE\x10\xd3]\x12)\n$CHANNEL_ATTRIBUTE_DI_DIG_SYNC_ENABLE\x10\xd6]\x122\n-CHANNEL_ATTRIBUTE_DI_DIG_FLTR_ENABLE_BUS_MODE\x10\xfe]\x124\n/CHANNEL_ATTRIBUTE_CI_PULSE_FREQ_DIG_FLTR_ENABLE\x10\x86^\x124\n/CHANNEL_ATTRIBUTE_CI_PULSE_FREQ_DIG_SYNC_ENABLE\x10\x8a^\x124\n/CHANNEL_ATTRIBUTE_CI_PULSE_TIME_DIG_FLTR_ENABLE\x10\x8e^\x124\n/CHANNEL_ATTRIBUTE_CI_PULSE_TIME_DIG_SYNC_ENABLE\x10\x92^\x125\n0CHANNEL_ATTRIBUTE_CI_PULSE_TICKS_DIG_FLTR_ENABLE\x10\x96^\x125\n0CHANNEL_ATTRIBUTE_CI_PULSE_TICKS_DIG_SYNC_ENABLE\x10\x9a^\x124\n/CHANNEL_ATTRIBUTE_AI_OPEN_THRMCPL_DETECT_ENABLE\x10\xf2^\x128\n3CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_ENABLE\x10\xaf_\x12A\n<CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_DIG_FLTR_ENABLE\x10\xb3_\x12A\n<CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_DIG_SYNC_ENABLE\x10\xb7_\x12-\n(CHANNEL_ATTRIBUTE_AI_REMOVE_FILTER_DELAY\x10\xbd_\x12:\n5CHANNEL_ATTRIBUTE_AI_STRAIN_GAGE_FORCE_READ_FROM_CHAN\x10\xfa_\x124\n/CHANNEL_ATTRIBUTE_CI_DUTY_CYCLE_DIG_FLTR_ENABLE\x10\x8ea\x12)\n$CHANNEL_ATTRIBUTE_AI_DIG_FLTR_ENABLE\x10\xbda\x12B\n=CHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_DIG_FLTR_ENABLE\x10\xe0a\x12B\n=CHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_DIG_FLTR_ENABLE\x10\xe7a\x121\n,CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_GATE_ENABLE\x10\xeda\x12:\n5CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_GATE_DIG_FLTR_ENABLE\x10\xf1a\x121\n,CHANNEL_ATTRIBUTE_AI_OPEN_CHAN_DETECT_ENABLE\x10\xffa\x12%\n CHANNEL_ATTRIBUTE_AI_CHOP_ENABLE\x10\xc3b\x12\'\n"CHANNEL_ATTRIBUTE_AI_FILTER_ENABLE\x10\xf3b\x12:\n5CHANNEL_ATTRIBUTE_AI_INPUT_LIMITS_FAULT_DETECT_ENABLE\x10\x8ec\x12:\n5CHANNEL_ATTRIBUTE_AI_POWER_SUPPLY_FAULT_DETECT_ENABLE\x10\x91c\x123\n.CHANNEL_ATTRIBUTE_AI_OVERCURRENT_DETECT_ENABLE\x10\x94c\x12\'\n"CHANNEL_ATTRIBUTE_CI_FILTER_ENABLE\x10\xb7c\x12(\n#CHANNEL_ATTRIBUTE_PWR_OUTPUT_ENABLE\x10\xd6c*\xf0\x18\n\x16ChannelStringAttribute\x12(\n$CHANNEL_STRING_ATTRIBUTE_UNSPECIFIED\x10\x00\x12*\n%CHANNEL_ATTRIBUTE_CI_CTR_TIMEBASE_SRC\x10\xc3\x02\x12*\n%CHANNEL_ATTRIBUTE_CO_CTR_TIMEBASE_SRC\x10\xb9\x06\x12*\n%CHANNEL_ATTRIBUTE_AI_THRMCPL_CJC_CHAN\x10\xb4 \x12&\n!CHANNEL_ATTRIBUTE_CI_GPS_SYNC_SRC\x10\x93!\x12+\n&CHANNEL_ATTRIBUTE_AO_CUSTOM_SCALE_NAME\x10\x88#\x12+\n&CHANNEL_ATTRIBUTE_AI_CUSTOM_SCALE_NAME\x10\xe0/\x12+\n&CHANNEL_ATTRIBUTE_CI_CUSTOM_SCALE_NAME\x10\x9e1\x12#\n\x1eCHANNEL_ATTRIBUTE_CI_FREQ_TERM\x10\xa21\x12%\n CHANNEL_ATTRIBUTE_CI_PERIOD_TERM\x10\xa41\x12*\n%CHANNEL_ATTRIBUTE_CI_PULSE_WIDTH_TERM\x10\xaa1\x121\n,CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_TERM\x10\xad1\x122\n-CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_TERM\x10\xae1\x12*\n%CHANNEL_ATTRIBUTE_CI_SEMI_PERIOD_TERM\x10\xb01\x12*\n%CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_TERM\x10\xc71\x12$\n\x1fCHANNEL_ATTRIBUTE_CO_PULSE_TERM\x10\xe11\x12)\n$CHANNEL_ATTRIBUTE_PHYSICAL_CHAN_NAME\x10\xf51\x12!\n\x1cCHANNEL_ATTRIBUTE_CHAN_DESCR\x10\xa62\x12#\n\x1eCHANNEL_ATTRIBUTE_AI_INPUT_SRC\x10\x98C\x12.\n)CHANNEL_ATTRIBUTE_CI_ENCODER_A_INPUT_TERM\x10\x9dC\x12.\n)CHANNEL_ATTRIBUTE_CI_ENCODER_B_INPUT_TERM\x10\x9eC\x12.\n)CHANNEL_ATTRIBUTE_CI_ENCODER_Z_INPUT_TERM\x10\x9fC\x12$\n\x1fCHANNEL_ATTRIBUTE_AI_TEDS_UNITS\x10\xe0C\x12.\n)CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_DIR_TERM\x10\xe1C\x124\n/CHANNEL_ATTRIBUTE_CI_FREQ_DIG_FLTR_TIMEBASE_SRC\x10\xe9C\x126\n1CHANNEL_ATTRIBUTE_CI_PERIOD_DIG_FLTR_TIMEBASE_SRC\x10\xeeC\x12E\n@CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_DIG_FLTR_TIMEBASE_SRC\x10\xf3C\x12;\n6CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_DIG_FLTR_TIMEBASE_SRC\x10\xf8C\x12?\n:CHANNEL_ATTRIBUTE_CI_ENCODER_A_INPUT_DIG_FLTR_TIMEBASE_SRC\x10\xfdC\x12?\n:CHANNEL_ATTRIBUTE_CI_ENCODER_B_INPUT_DIG_FLTR_TIMEBASE_SRC\x10\x82D\x12?\n:CHANNEL_ATTRIBUTE_CI_ENCODER_Z_INPUT_DIG_FLTR_TIMEBASE_SRC\x10\x87D\x12;\n6CHANNEL_ATTRIBUTE_CI_PULSE_WIDTH_DIG_FLTR_TIMEBASE_SRC\x10\x8cD\x12B\n=CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_DIG_FLTR_TIMEBASE_SRC\x10\x91D\x12C\n>CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_DIG_FLTR_TIMEBASE_SRC\x10\x96D\x12;\n6CHANNEL_ATTRIBUTE_CI_SEMI_PERIOD_DIG_FLTR_TIMEBASE_SRC\x10\x9bD\x12)\n$CHANNEL_ATTRIBUTE_AO_DAC_REF_EXT_SRC\x10\xd2D\x12,\n\'CHANNEL_ATTRIBUTE_AO_DAC_OFFSET_EXT_SRC\x10\xd4D\x12<\n7CHANNEL_ATTRIBUTE_CI_CTR_TIMEBASE_DIG_FLTR_TIMEBASE_SRC\x10\xf3D\x12<\n7CHANNEL_ATTRIBUTE_CO_CTR_TIMEBASE_DIG_FLTR_TIMEBASE_SRC\x10\xf8D\x120\n+CHANNEL_ATTRIBUTE_AI_CHAN_CAL_OPERATOR_NAME\x10\xa3E\x12\'\n"CHANNEL_ATTRIBUTE_AI_CHAN_CAL_DESC\x10\xa4E\x12/\n*CHANNEL_ATTRIBUTE_DI_DIG_FLTR_TIMEBASE_SRC\x10\xd4]\x12)\n$CHANNEL_ATTRIBUTE_CI_PULSE_FREQ_TERM\x10\x84^\x12:\n5CHANNEL_ATTRIBUTE_CI_PULSE_FREQ_DIG_FLTR_TIMEBASE_SRC\x10\x88^\x12)\n$CHANNEL_ATTRIBUTE_CI_PULSE_TIME_TERM\x10\x8c^\x12:\n5CHANNEL_ATTRIBUTE_CI_PULSE_TIME_DIG_FLTR_TIMEBASE_SRC\x10\x90^\x12*\n%CHANNEL_ATTRIBUTE_CI_PULSE_TICKS_TERM\x10\x94^\x12;\n6CHANNEL_ATTRIBUTE_CI_PULSE_TICKS_DIG_FLTR_TIMEBASE_SRC\x10\x98^\x126\n1CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_TERM\x10\xb1_\x12G\nBCHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_DIG_FLTR_TIMEBASE_SRC\x10\xb5_\x12:\n5CHANNEL_ATTRIBUTE_AI_ROSETTE_STRAIN_GAGE_STRAIN_CHANS\x10\xfb_\x12(\n#CHANNEL_ATTRIBUTE_CI_TIMESTAMP_TERM\x10\xb9`\x12,\n\'CHANNEL_ATTRIBUTE_NAV_CUSTOM_SCALE_NAME\x10\xbc`\x12)\n$CHANNEL_ATTRIBUTE_CI_DUTY_CYCLE_TERM\x10\x8da\x12:\n5CHANNEL_ATTRIBUTE_CI_DUTY_CYCLE_DIG_FLTR_TIMEBASE_SRC\x10\x90a\x127\n2CHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_TERM\x10\xdda\x12H\nCCHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_DIG_FLTR_TIMEBASE_SRC\x10\xe2a\x127\n2CHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_TERM\x10\xe4a\x12H\nCCHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_DIG_FLTR_TIMEBASE_SRC\x10\xe9a\x12/\n*CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_GATE_TERM\x10\xeea\x12@\n;CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_GATE_DIG_FLTR_TIMEBASE_SRC\x10\xf3a*\xc4\x10\n\x16ChannelUInt32Attribute\x12(\n$CHANNEL_UINT32_ATTRIBUTE_UNSPECIFIED\x10\x00\x12"\n\x1dCHANNEL_ATTRIBUTE_CI_FREQ_DIV\x10\xc7\x02\x12\x1f\n\x1aCHANNEL_ATTRIBUTE_CI_COUNT\x10\xc8\x02\x12\x1f\n\x1aCHANNEL_ATTRIBUTE_CO_COUNT\x10\x93\x05\x12\'\n"CHANNEL_ATTRIBUTE_CO_AUTO_INCR_CNT\x10\x95\x05\x123\n.CHANNEL_ATTRIBUTE_CO_PULSE_TICKS_INITIAL_DELAY\x10\x98\x05\x121\n,CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_INITIAL_CNT\x10\x98\r\x124\n/CHANNEL_ATTRIBUTE_CI_ANG_ENCODER_PULSES_PER_REV\x10\xf5\x10\x12*\n%CHANNEL_ATTRIBUTE_CO_PULSE_HIGH_TICKS\x10\xe9"\x12)\n$CHANNEL_ATTRIBUTE_CO_PULSE_LOW_TICKS\x10\xf1"\x12(\n#CHANNEL_ATTRIBUTE_AI_HIGHPASS_ORDER\x10\x890\x128\n3CHANNEL_ATTRIBUTE_AI_LOWPASS_SWITCH_CAP_EXT_CLK_DIV\x10\x861\x128\n3CHANNEL_ATTRIBUTE_AI_LOWPASS_SWITCH_CAP_OUT_CLK_DIV\x10\x871\x12:\n5CHANNEL_ATTRIBUTE_CI_CTR_TIMEBASE_MASTER_TIMEBASE_DIV\x10\xb31\x12:\n5CHANNEL_ATTRIBUTE_CO_CTR_TIMEBASE_MASTER_TIMEBASE_DIV\x10\xc31\x12$\n\x1fCHANNEL_ATTRIBUTE_CI_PERIOD_DIV\x10\xae2\x124\n/CHANNEL_ATTRIBUTE_CI_NUM_POSSIBLY_INVALID_SAMPS\x10\xbc2\x12#\n\x1eCHANNEL_ATTRIBUTE_DI_NUM_LINES\x10\xf8B\x12#\n\x1eCHANNEL_ATTRIBUTE_DO_NUM_LINES\x10\xf9B\x12#\n\x1eCHANNEL_ATTRIBUTE_CI_PRESCALER\x10\xb9D\x12#\n\x1eCHANNEL_ATTRIBUTE_CO_PRESCALER\x10\xedD\x123\n.CHANNEL_ATTRIBUTE_CI_TIMESTAMP_INITIAL_SECONDS\x10\xb4E\x12@\n;CHANNEL_ATTRIBUTE_AI_LOSSY_LSB_REMOVAL_COMPRESSED_SAMP_SIZE\x10\xd9E\x12\'\n"CHANNEL_ATTRIBUTE_AI_RAW_SAMP_SIZE\x10\xdaE\x124\n/CHANNEL_ATTRIBUTE_AI_DATA_XFER_CUSTOM_THRESHOLD\x10\x8cF\x12+\n&CHANNEL_ATTRIBUTE_AI_USB_XFER_REQ_SIZE\x10\x8eU\x12+\n&CHANNEL_ATTRIBUTE_AO_USB_XFER_REQ_SIZE\x10\x8fU\x12+\n&CHANNEL_ATTRIBUTE_DI_USB_XFER_REQ_SIZE\x10\x90U\x12+\n&CHANNEL_ATTRIBUTE_DO_USB_XFER_REQ_SIZE\x10\x91U\x12+\n&CHANNEL_ATTRIBUTE_CI_USB_XFER_REQ_SIZE\x10\x92U\x12+\n&CHANNEL_ATTRIBUTE_CO_USB_XFER_REQ_SIZE\x10\x93U\x120\n+CHANNEL_ATTRIBUTE_AI_ADC_CUSTOM_TIMING_MODE\x10\xeb^\x12=\n8CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_RESET_COUNT\x10\xb0_\x12,\n\'CHANNEL_ATTRIBUTE_AI_AVERAGING_WIN_SIZE\x10\xee_\x12,\n\'CHANNEL_ATTRIBUTE_AI_USB_XFER_REQ_COUNT\x10\x80`\x12,\n\'CHANNEL_ATTRIBUTE_AO_USB_XFER_REQ_COUNT\x10\x81`\x12,\n\'CHANNEL_ATTRIBUTE_DI_USB_XFER_REQ_COUNT\x10\x82`\x12,\n\'CHANNEL_ATTRIBUTE_DO_USB_XFER_REQ_COUNT\x10\x83`\x12,\n\'CHANNEL_ATTRIBUTE_CI_USB_XFER_REQ_COUNT\x10\x84`\x12,\n\'CHANNEL_ATTRIBUTE_CO_USB_XFER_REQ_COUNT\x10\x85`\x12(\n#CHANNEL_ATTRIBUTE_AI_DIG_FLTR_ORDER\x10\xc0a\x12=\n8CHANNEL_ATTRIBUTE_CI_VELOCITY_ANG_ENCODER_PULSES_PER_REV\x10\xd9a\x12&\n!CHANNEL_ATTRIBUTE_CI_VELOCITY_DIV\x10\xeca\x12&\n!CHANNEL_ATTRIBUTE_AI_FILTER_ORDER\x10\xf6b\x12&\n!CHANNEL_ATTRIBUTE_CI_FILTER_ORDER\x10\xbac*\xd9\x06\n\x1bChannelDoubleArrayAttribute\x12.\n*CHANNEL_DOUBLE_ARRAY_ATTRIBUTE_UNSPECIFIED\x10\x00\x12+\n&CHANNEL_ATTRIBUTE_AI_DEV_SCALING_COEFF\x10\xb02\x12+\n&CHANNEL_ATTRIBUTE_AO_DEV_SCALING_COEFF\x10\xb12\x128\n3CHANNEL_ATTRIBUTE_AI_CHAN_CAL_TABLE_PRE_SCALED_VALS\x10\x9dE\x124\n/CHANNEL_ATTRIBUTE_AI_CHAN_CAL_TABLE_SCALED_VALS\x10\x9eE\x125\n0CHANNEL_ATTRIBUTE_AI_CHAN_CAL_POLY_FORWARD_COEFF\x10\x9fE\x125\n0CHANNEL_ATTRIBUTE_AI_CHAN_CAL_POLY_REVERSE_COEFF\x10\xa0E\x121\n,CHANNEL_ATTRIBUTE_AI_CHAN_CAL_VERIF_REF_VALS\x10\xa1E\x121\n,CHANNEL_ATTRIBUTE_AI_CHAN_CAL_VERIF_ACQ_VALS\x10\xa2E\x126\n1CHANNEL_ATTRIBUTE_AI_BRIDGE_TABLE_ELECTRICAL_VALS\x10\x8e_\x124\n/CHANNEL_ATTRIBUTE_AI_BRIDGE_TABLE_PHYSICAL_VALS\x10\x8f_\x123\n.CHANNEL_ATTRIBUTE_AI_BRIDGE_POLY_FORWARD_COEFF\x10\x90_\x123\n.CHANNEL_ATTRIBUTE_AI_BRIDGE_POLY_REVERSE_COEFF\x10\x91_\x12(\n#CHANNEL_ATTRIBUTE_AI_DIG_FLTR_COEFF\x10\xc7a\x124\n/CHANNEL_ATTRIBUTE_PWR_VOLTAGE_DEV_SCALING_COEFF\x10\xd9c\x124\n/CHANNEL_ATTRIBUTE_PWR_CURRENT_DEV_SCALING_COEFF\x10\xdac*\xc2\x07\n\x15DeviceStringAttribute\x12\'\n#DEVICE_STRING_ATTRIBUTE_UNSPECIFIED\x10\x00\x12"\n\x1dDEVICE_ATTRIBUTE_PRODUCT_TYPE\x10\xb1\x0c\x12\'\n"DEVICE_ATTRIBUTE_AI_PHYSICAL_CHANS\x10\x9eF\x12\'\n"DEVICE_ATTRIBUTE_AO_PHYSICAL_CHANS\x10\x9fF\x12\x1e\n\x19DEVICE_ATTRIBUTE_DI_LINES\x10\xa0F\x12\x1e\n\x19DEVICE_ATTRIBUTE_DI_PORTS\x10\xa1F\x12\x1e\n\x19DEVICE_ATTRIBUTE_DO_LINES\x10\xa2F\x12\x1e\n\x19DEVICE_ATTRIBUTE_DO_PORTS\x10\xa3F\x12\'\n"DEVICE_ATTRIBUTE_CI_PHYSICAL_CHANS\x10\xa4F\x12\'\n"DEVICE_ATTRIBUTE_CO_PHYSICAL_CHANS\x10\xa5F\x12.\n)DEVICE_ATTRIBUTE_CHASSIS_MODULE_DEV_NAMES\x10\xb6S\x122\n-DEVICE_ATTRIBUTE_COMPACT_DAQ_CHASSIS_DEV_NAME\x10\xb7S\x12\x1f\n\x1aDEVICE_ATTRIBUTE_TERMINALS\x10\xc0T\x12$\n\x1fDEVICE_ATTRIBUTE_TCPIP_HOSTNAME\x10\x8bU\x12\'\n"DEVICE_ATTRIBUTE_TCPIP_ETHERNET_IP\x10\x8cU\x12\'\n"DEVICE_ATTRIBUTE_TCPIP_WIRELESS_IP\x10\x8dU\x12-\n(DEVICE_ATTRIBUTE_ACCESSORY_PRODUCT_TYPES\x10\xed^\x12(\n#DEVICE_ATTRIBUTE_NAV_PHYSICAL_CHANS\x10\xa2`\x122\n-DEVICE_ATTRIBUTE_COMPACT_RIO_CHASSIS_DEV_NAME\x10\xe1b\x12(\n#DEVICE_ATTRIBUTE_FIELD_DAQ_DEV_NAME\x10\xf1b\x12.\n)DEVICE_ATTRIBUTE_FIELD_DAQ_BANK_DEV_NAMES\x10\xf8b\x12&\n!DEVICE_ATTRIBUTE_ID_PIN_PIN_NAMES\x10\xf1c\x12,\n\'DEVICE_ATTRIBUTE_ID_PIN_MEM_SERIAL_NUMS\x10\xf4c*\xfc\x07\n\x15DeviceUInt32Attribute\x12\'\n#DEVICE_UINT32_ATTRIBUTE_UNSPECIFIED\x10\x00\x12 \n\x1bDEVICE_ATTRIBUTE_SERIAL_NUM\x10\xb2\x0c\x12!\n\x1cDEVICE_ATTRIBUTE_PRODUCT_NUM\x10\x9dF\x12!\n\x1cDEVICE_ATTRIBUTE_PCI_BUS_NUM\x10\xa7F\x12!\n\x1cDEVICE_ATTRIBUTE_PCI_DEV_NUM\x10\xa8F\x12%\n DEVICE_ATTRIBUTE_PXI_CHASSIS_NUM\x10\xa9F\x12"\n\x1dDEVICE_ATTRIBUTE_PXI_SLOT_NUM\x10\xaaF\x12#\n\x1eDEVICE_ATTRIBUTE_NUM_DMA_CHANS\x10\xbcF\x12!\n\x1cDEVICE_ATTRIBUTE_CI_MAX_SIZE\x10\x9fS\x12!\n\x1cDEVICE_ATTRIBUTE_CO_MAX_SIZE\x10\xa1S\x12*\n%DEVICE_ATTRIBUTE_COMPACT_DAQ_SLOT_NUM\x10\xb8S\x12(\n#DEVICE_ATTRIBUTE_CARRIER_SERIAL_NUM\x10\x8aU\x12*\n%DEVICE_ATTRIBUTE_NAV_NUM_SURVEY_FIXES\x10\xab`\x120\n+DEVICE_ATTRIBUTE_NAV_REMAINING_SURVEY_FIXES\x10\xac`\x12"\n\x1dDEVICE_ATTRIBUTE_NAV_NUM_SATS\x10\xb1`\x12$\n\x1fDEVICE_ATTRIBUTE_NUM_TIME_TRIGS\x10\xc1b\x12+\n&DEVICE_ATTRIBUTE_NUM_TIMESTAMP_ENGINES\x10\xc2b\x12*\n%DEVICE_ATTRIBUTE_COMPACT_RIO_SLOT_NUM\x10\xe2b\x120\n+DEVICE_ATTRIBUTE_AI_NUM_SAMP_TIMING_ENGINES\x10\xe3b\x12,\n\'DEVICE_ATTRIBUTE_AI_NUM_SYNC_PULSE_SRCS\x10\xe4b\x120\n+DEVICE_ATTRIBUTE_AO_NUM_SAMP_TIMING_ENGINES\x10\xe5b\x12,\n\'DEVICE_ATTRIBUTE_AO_NUM_SYNC_PULSE_SRCS\x10\xe6b\x120\n+DEVICE_ATTRIBUTE_DI_NUM_SAMP_TIMING_ENGINES\x10\xe7b\x120\n+DEVICE_ATTRIBUTE_DO_NUM_SAMP_TIMING_ENGINES\x10\xe8b*\xc8\x04\n\x13DeviceBoolAttribute\x12%\n!DEVICE_BOOL_ATTRIBUTE_UNSPECIFIED\x10\x00\x12"\n\x1dDEVICE_ATTRIBUTE_IS_SIMULATED\x10\xcaE\x12)\n$DEVICE_ATTRIBUTE_ANLG_TRIG_SUPPORTED\x10\x84S\x12(\n#DEVICE_ATTRIBUTE_DIG_TRIG_SUPPORTED\x10\x85S\x128\n3DEVICE_ATTRIBUTE_AI_SIMULTANEOUS_SAMPLING_SUPPORTED\x10\x8fS\x12+\n&DEVICE_ATTRIBUTE_AO_SAMP_CLK_SUPPORTED\x10\x96S\x12+\n&DEVICE_ATTRIBUTE_CI_SAMP_CLK_SUPPORTED\x10\x9eS\x12+\n&DEVICE_ATTRIBUTE_CO_SAMP_CLK_SUPPORTED\x10\xdb^\x12+\n&DEVICE_ATTRIBUTE_TEDS_HWTEDS_SUPPORTED\x10\xd6_\x12)\n$DEVICE_ATTRIBUTE_TIME_TRIG_SUPPORTED\x10\x9f`\x12)\n$DEVICE_ATTRIBUTE_CI_UTC_OFFSET_READY\x10\xa1`\x12!\n\x1cDEVICE_ATTRIBUTE_NAV_HAS_FIX\x10\xad`\x12*\n%DEVICE_ATTRIBUTE_NAV_UTC_OFFSET_READY\x10\xaf`*\xcc\x04\n\x14DeviceInt32Attribute\x12&\n"DEVICE_INT32_ATTRIBUTE_UNSPECIFIED\x10\x00\x12\x1e\n\x19DEVICE_ATTRIBUTE_BUS_TYPE\x10\xa6F\x12#\n\x1eDEVICE_ATTRIBUTE_AI_TRIG_USAGE\x10\x86S\x12#\n\x1eDEVICE_ATTRIBUTE_AO_TRIG_USAGE\x10\x87S\x12#\n\x1eDEVICE_ATTRIBUTE_DI_TRIG_USAGE\x10\x88S\x12#\n\x1eDEVICE_ATTRIBUTE_DO_TRIG_USAGE\x10\x89S\x12#\n\x1eDEVICE_ATTRIBUTE_CI_TRIG_USAGE\x10\x8aS\x12#\n\x1eDEVICE_ATTRIBUTE_CO_TRIG_USAGE\x10\x8bS\x12"\n\x1dDEVICE_ATTRIBUTE_AI_COUPLINGS\x10\x94S\x12&\n!DEVICE_ATTRIBUTE_PRODUCT_CATEGORY\x10\xa9S\x12+\n&DEVICE_ATTRIBUTE_CI_CURRENT_UTC_OFFSET\x10\xa0`\x12\x1e\n\x19DEVICE_ATTRIBUTE_NAV_MODE\x10\xa5`\x12!\n\x1cDEVICE_ATTRIBUTE_NAV_ALT_REF\x10\xa9`\x12$\n\x1fDEVICE_ATTRIBUTE_NAV_ANT_STATUS\x10\xae`\x12,\n\'DEVICE_ATTRIBUTE_NAV_CURRENT_UTC_OFFSET\x10\xb0`*\x93\x05\n\x15DeviceDoubleAttribute\x12\'\n#DEVICE_DOUBLE_ATTRIBUTE_UNSPECIFIED\x10\x00\x12-\n(DEVICE_ATTRIBUTE_AI_MAX_SINGLE_CHAN_RATE\x10\x8cS\x12,\n\'DEVICE_ATTRIBUTE_AI_MAX_MULTI_CHAN_RATE\x10\x8dS\x12!\n\x1cDEVICE_ATTRIBUTE_AI_MIN_RATE\x10\x8eS\x12!\n\x1cDEVICE_ATTRIBUTE_AO_MAX_RATE\x10\x97S\x12!\n\x1cDEVICE_ATTRIBUTE_AO_MIN_RATE\x10\x98S\x12!\n\x1cDEVICE_ATTRIBUTE_DI_MAX_RATE\x10\x99S\x12!\n\x1cDEVICE_ATTRIBUTE_DO_MAX_RATE\x10\x9aS\x12%\n DEVICE_ATTRIBUTE_CI_MAX_TIMEBASE\x10\xa0S\x12%\n DEVICE_ATTRIBUTE_CO_MAX_TIMEBASE\x10\xa2S\x12$\n\x1fDEVICE_ATTRIBUTE_NAV_PRESET_LAT\x10\xa6`\x12%\n DEVICE_ATTRIBUTE_NAV_PRESET_LONG\x10\xa7`\x12$\n\x1fDEVICE_ATTRIBUTE_NAV_PRESET_ALT\x10\xa8`\x12$\n\x1fDEVICE_ATTRIBUTE_NAV_PPS_COMPEN\x10\xaa`\x12\x1e\n\x19DEVICE_ATTRIBUTE_NAV_PDOP\x10\xb2`\x12\x1e\n\x19DEVICE_ATTRIBUTE_NAV_HDOP\x10\xb3`\x12\x1e\n\x19DEVICE_ATTRIBUTE_NAV_VDOP\x10\xb4`*\xe8\x06\n\x1aDeviceDoubleArrayAttribute\x12-\n)DEVICE_DOUBLE_ARRAY_ATTRIBUTE_UNSPECIFIED\x10\x00\x12%\n DEVICE_ATTRIBUTE_AI_VOLTAGE_RNGS\x10\x90S\x12%\n DEVICE_ATTRIBUTE_AI_CURRENT_RNGS\x10\x91S\x12"\n\x1dDEVICE_ATTRIBUTE_AI_FREQ_RNGS\x10\x92S\x12\x1e\n\x19DEVICE_ATTRIBUTE_AI_GAINS\x10\x93S\x12:\n5DEVICE_ATTRIBUTE_AI_LOWPASS_CUTOFF_FREQ_DISCRETE_VALS\x10\x95S\x12%\n DEVICE_ATTRIBUTE_AO_VOLTAGE_RNGS\x10\x9bS\x12%\n DEVICE_ATTRIBUTE_AO_CURRENT_RNGS\x10\x9cS\x12\x1e\n\x19DEVICE_ATTRIBUTE_AO_GAINS\x10\x9dS\x128\n3DEVICE_ATTRIBUTE_AI_VOLTAGE_INT_EXCIT_DISCRETE_VALS\x10\xc9S\x125\n0DEVICE_ATTRIBUTE_AI_VOLTAGE_INT_EXCIT_RANGE_VALS\x10\xcaS\x128\n3DEVICE_ATTRIBUTE_AI_CURRENT_INT_EXCIT_DISCRETE_VALS\x10\xcbS\x127\n2DEVICE_ATTRIBUTE_AI_LOWPASS_CUTOFF_FREQ_RANGE_VALS\x10\xcfS\x12(\n#DEVICE_ATTRIBUTE_AI_RESISTANCE_RNGS\x10\x95T\x12$\n\x1fDEVICE_ATTRIBUTE_AI_BRIDGE_RNGS\x10\xd0_\x12C\n>DEVICE_ATTRIBUTE_AI_DIG_FLTR_LOWPASS_CUTOFF_FREQ_DISCRETE_VALS\x10\xc8a\x12@\n;DEVICE_ATTRIBUTE_AI_DIG_FLTR_LOWPASS_CUTOFF_FREQ_RANGE_VALS\x10\xc9a\x12$\n\x1fDEVICE_ATTRIBUTE_AI_CHARGE_RNGS\x10\x91b*\xfd\x01\n\x1aDeviceUInt32ArrayAttribute\x12-\n)DEVICE_UINT32_ARRAY_ATTRIBUTE_UNSPECIFIED\x10\x00\x12,\n\'DEVICE_ATTRIBUTE_ACCESSORY_PRODUCT_NUMS\x10\xee^\x12+\n&DEVICE_ATTRIBUTE_ACCESSORY_SERIAL_NUMS\x10\xef^\x12-\n(DEVICE_ATTRIBUTE_ID_PIN_MEM_FAMILY_CODES\x10\xf3c\x12&\n!DEVICE_ATTRIBUTE_ID_PIN_MEM_SIZES\x10\xf5c*\xc7\x04\n\x19DeviceInt32ArrayAttribute\x12,\n(DEVICE_INT32_ARRAY_ATTRIBUTE_UNSPECIFIED\x10\x00\x12-\n(DEVICE_ATTRIBUTE_AI_SUPPORTED_MEAS_TYPES\x10\xd2_\x12/\n*DEVICE_ATTRIBUTE_AO_SUPPORTED_OUTPUT_TYPES\x10\xd3_\x12-\n(DEVICE_ATTRIBUTE_CI_SUPPORTED_MEAS_TYPES\x10\xd4_\x12/\n*DEVICE_ATTRIBUTE_CO_SUPPORTED_OUTPUT_TYPES\x10\xd5_\x12#\n\x1eDEVICE_ATTRIBUTE_AI_SAMP_MODES\x10\xdc_\x12#\n\x1eDEVICE_ATTRIBUTE_AO_SAMP_MODES\x10\xdd_\x12#\n\x1eDEVICE_ATTRIBUTE_CI_SAMP_MODES\x10\xde_\x12#\n\x1eDEVICE_ATTRIBUTE_CO_SAMP_MODES\x10\xdf_\x12.\n)DEVICE_ATTRIBUTE_NAV_SUPPORTED_MEAS_TYPES\x10\xa3`\x12$\n\x1fDEVICE_ATTRIBUTE_NAV_TRIG_USAGE\x10\xa4`\x12\'\n"DEVICE_ATTRIBUTE_AI_DIG_FLTR_TYPES\x10\x87b\x12)\n$DEVICE_ATTRIBUTE_ID_PIN_PIN_STATUSES\x10\xf2c*\x9d\x07\n\x1bExportSignalDoubleAttribute\x12-\n)EXPORTSIGNAL_DOUBLE_ATTRIBUTE_UNSPECIFIED\x10\x00\x12,\n\'EXPORTSIGNAL_ATTRIBUTE_START_TRIG_DELAY\x10\x81\x0b\x122\n-EXPORTSIGNAL_ATTRIBUTE_START_TRIG_PULSE_WIDTH\x10\x86\x0b\x129\n4EXPORTSIGNAL_ATTRIBUTE_RDY_FOR_REF_EVENT_PULSE_WIDTH\x10\xa4,\x120\n+EXPORTSIGNAL_ATTRIBUTE_ADV_TRIG_PULSE_WIDTH\x10\xc8,\x127\n2EXPORTSIGNAL_ATTRIBUTE_ADV_CMPLT_EVENT_PULSE_WIDTH\x10\xd4,\x127\n2EXPORTSIGNAL_ATTRIBUTE_20_MHZ_TIMEBASE_PULSE_WIDTH\x10\xe0,\x120\n+EXPORTSIGNAL_ATTRIBUTE_SAMP_CLK_PULSE_WIDTH\x10\xe6,\x123\n.EXPORTSIGNAL_ATTRIBUTE_AI_CONV_CLK_PULSE_WIDTH\x10\x90-\x124\n/EXPORTSIGNAL_ATTRIBUTE_FREQ_OUT_CLK_PULSE_WIDTH\x10\x94.\x125\n0EXPORTSIGNAL_ATTRIBUTE_CTR_OUT_EVENT_PULSE_WIDTH\x10\xa0.\x12/\n*EXPORTSIGNAL_ATTRIBUTE_REF_CLK_PULSE_WIDTH\x10\xb8.\x121\n,EXPORTSIGNAL_ATTRIBUTE_ADV_CMPLT_EVENT_DELAY\x10\xd7.\x121\n,EXPORTSIGNAL_ATTRIBUTE_SAMP_CLK_DELAY_OFFSET\x10\xc4C\x12,\n\'EXPORTSIGNAL_ATTRIBUTE_HSHK_EVENT_DELAY\x10\xbcE\x12A\n<EXPORTSIGNAL_ATTRIBUTE_HSHK_EVENT_INTERLOCKED_DEASSERT_DELAY\x10\xbfE\x122\n-EXPORTSIGNAL_ATTRIBUTE_HSHK_EVENT_PULSE_WIDTH\x10\xc1E*\xba\t\n\x1bExportSignalStringAttribute\x12-\n)EXPORTSIGNAL_STRING_ATTRIBUTE_UNSPECIFIED\x10\x00\x122\n-EXPORTSIGNAL_ATTRIBUTE_START_TRIG_OUTPUT_TERM\x10\x84\x0b\x120\n+EXPORTSIGNAL_ATTRIBUTE_REF_TRIG_OUTPUT_TERM\x10\x90\x0b\x12;\n6EXPORTSIGNAL_ATTRIBUTE_RDY_FOR_START_EVENT_OUTPUT_TERM\x10\x89,\x122\n-EXPORTSIGNAL_ATTRIBUTE_PAUSE_TRIG_OUTPUT_TERM\x10\x95,\x129\n4EXPORTSIGNAL_ATTRIBUTE_DATA_ACTIVE_EVENT_OUTPUT_TERM\x10\xb3,\x120\n+EXPORTSIGNAL_ATTRIBUTE_ADV_TRIG_OUTPUT_TERM\x10\xc5,\x127\n2EXPORTSIGNAL_ATTRIBUTE_ADV_CMPLT_EVENT_OUTPUT_TERM\x10\xd1,\x127\n2EXPORTSIGNAL_ATTRIBUTE_20_MHZ_TIMEBASE_OUTPUT_TERM\x10\xd7,\x120\n+EXPORTSIGNAL_ATTRIBUTE_SAMP_CLK_OUTPUT_TERM\x10\xe3,\x123\n.EXPORTSIGNAL_ATTRIBUTE_AI_CONV_CLK_OUTPUT_TERM\x10\x87-\x125\n0EXPORTSIGNAL_ATTRIBUTE_CTR_OUT_EVENT_OUTPUT_TERM\x10\x97.\x12;\n6EXPORTSIGNAL_ATTRIBUTE_AI_HOLD_CMPLT_EVENT_OUTPUT_TERM\x10\xed1\x129\n4EXPORTSIGNAL_ATTRIBUTE_SAMP_CLK_TIMEBASE_OUTPUT_TERM\x10\xf91\x12;\n6EXPORTSIGNAL_ATTRIBUTE_CHANGE_DETECT_EVENT_OUTPUT_TERM\x10\x97C\x12A\n<EXPORTSIGNAL_ATTRIBUTE_DIVIDED_SAMP_CLK_TIMEBASE_OUTPUT_TERM\x10\xa1C\x12>\n9EXPORTSIGNAL_ATTRIBUTE_WATCHDOG_EXPIRED_EVENT_OUTPUT_TERM\x10\xaaC\x128\n3EXPORTSIGNAL_ATTRIBUTE_SYNC_PULSE_EVENT_OUTPUT_TERM\x10\xbcD\x126\n1EXPORTSIGNAL_ATTRIBUTE_10_MHZ_REF_CLK_OUTPUT_TERM\x10\xeeD\x12:\n5EXPORTSIGNAL_ATTRIBUTE_RDY_FOR_XFER_EVENT_OUTPUT_TERM\x10\xb5E\x122\n-EXPORTSIGNAL_ATTRIBUTE_HSHK_EVENT_OUTPUT_TERM\x10\xbaE*\xcb\x1f\n\x1aExportSignalResetAttribute\x12,\n(EXPORTSIGNAL_RESET_ATTRIBUTE_UNSPECIFIED\x10\x00\x128\n3EXPORTSIGNAL_RESET_ATTRIBUTE_START_TRIG_OUTPUT_TERM\x10\x84\x0b\x12;\n6EXPORTSIGNAL_RESET_ATTRIBUTE_START_TRIG_PULSE_POLARITY\x10\x85\x0b\x126\n1EXPORTSIGNAL_RESET_ATTRIBUTE_REF_TRIG_OUTPUT_TERM\x10\x90\x0b\x129\n4EXPORTSIGNAL_RESET_ATTRIBUTE_REF_TRIG_PULSE_POLARITY\x10\x91\x0b\x12>\n9EXPORTSIGNAL_RESET_ATTRIBUTE_START_TRIG_PULSE_WIDTH_UNITS\x10\x82,\x12A\n<EXPORTSIGNAL_RESET_ATTRIBUTE_RDY_FOR_START_EVENT_OUTPUT_TERM\x10\x89,\x128\n3EXPORTSIGNAL_RESET_ATTRIBUTE_PAUSE_TRIG_OUTPUT_TERM\x10\x95,\x12;\n6EXPORTSIGNAL_RESET_ATTRIBUTE_PAUSE_TRIG_LVL_ACTIVE_LVL\x10\x96,\x12E\n@EXPORTSIGNAL_RESET_ATTRIBUTE_RDY_FOR_REF_EVENT_PULSE_WIDTH_UNITS\x10\xa3,\x12?\n:EXPORTSIGNAL_RESET_ATTRIBUTE_DATA_ACTIVE_EVENT_OUTPUT_TERM\x10\xb3,\x12B\n=EXPORTSIGNAL_RESET_ATTRIBUTE_DATA_ACTIVE_EVENT_LVL_ACTIVE_LVL\x10\xb4,\x126\n1EXPORTSIGNAL_RESET_ATTRIBUTE_ADV_TRIG_OUTPUT_TERM\x10\xc5,\x12<\n7EXPORTSIGNAL_RESET_ATTRIBUTE_ADV_TRIG_PULSE_WIDTH_UNITS\x10\xc7,\x126\n1EXPORTSIGNAL_RESET_ATTRIBUTE_ADV_TRIG_PULSE_WIDTH\x10\xc8,\x128\n3EXPORTSIGNAL_RESET_ATTRIBUTE_ADV_CMPLT_EVENT_ENABLE\x10\xca,\x12=\n8EXPORTSIGNAL_RESET_ATTRIBUTE_ADV_CMPLT_EVENT_OUTPUT_TERM\x10\xd1,\x12@\n;EXPORTSIGNAL_RESET_ATTRIBUTE_ADV_CMPLT_EVENT_PULSE_POLARITY\x10\xd2,\x12C\n>EXPORTSIGNAL_RESET_ATTRIBUTE_ADV_CMPLT_EVENT_PULSE_WIDTH_UNITS\x10\xd3,\x12=\n8EXPORTSIGNAL_RESET_ATTRIBUTE_ADV_CMPLT_EVENT_PULSE_WIDTH\x10\xd4,\x12B\n=EXPORTSIGNAL_RESET_ATTRIBUTE_20_MHZ_TIMEBASE_DIVIDE_DOWN_BY_N\x10\xd6,\x12=\n8EXPORTSIGNAL_RESET_ATTRIBUTE_20_MHZ_TIMEBASE_OUTPUT_TERM\x10\xd7,\x12C\n>EXPORTSIGNAL_RESET_ATTRIBUTE_20_MHZ_TIMEBASE_PULSE_WIDTH_UNITS\x10\xd9,\x126\n1EXPORTSIGNAL_RESET_ATTRIBUTE_SAMP_CLK_OUTPUT_TERM\x10\xe3,\x129\n4EXPORTSIGNAL_RESET_ATTRIBUTE_SAMP_CLK_PULSE_POLARITY\x10\xe4,\x12<\n7EXPORTSIGNAL_RESET_ATTRIBUTE_SAMP_CLK_PULSE_WIDTH_UNITS\x10\xe5,\x129\n4EXPORTSIGNAL_RESET_ATTRIBUTE_AI_CONV_CLK_OUTPUT_TERM\x10\x87-\x12?\n:EXPORTSIGNAL_RESET_ATTRIBUTE_AI_CONV_CLK_PULSE_WIDTH_UNITS\x10\x89-\x12@\n;EXPORTSIGNAL_RESET_ATTRIBUTE_FREQ_OUT_CLK_PULSE_WIDTH_UNITS\x10\x93.\x12;\n6EXPORTSIGNAL_RESET_ATTRIBUTE_CTR_OUT_EVENT_OUTPUT_TERM\x10\x97.\x12>\n9EXPORTSIGNAL_RESET_ATTRIBUTE_CTR_OUT_EVENT_PULSE_POLARITY\x10\x98.\x12A\n<EXPORTSIGNAL_RESET_ATTRIBUTE_CTR_OUT_EVENT_PULSE_WIDTH_UNITS\x10\x99.\x12;\n6EXPORTSIGNAL_RESET_ATTRIBUTE_REF_CLK_PULSE_WIDTH_UNITS\x10\xb7.\x12<\n7EXPORTSIGNAL_RESET_ATTRIBUTE_START_TRIG_OUTPUT_BEHAVIOR\x10\xc3.\x12A\n<EXPORTSIGNAL_RESET_ATTRIBUTE_START_TRIG_TOGGLE_INITIAL_STATE\x10\xc4.\x128\n3EXPORTSIGNAL_RESET_ATTRIBUTE_START_TRIG_DELAY_UNITS\x10\xcd.\x12?\n:EXPORTSIGNAL_RESET_ATTRIBUTE_CTR_OUT_EVENT_OUTPUT_BEHAVIOR\x10\xcf.\x12D\n?EXPORTSIGNAL_RESET_ATTRIBUTE_RDY_FOR_START_EVENT_LVL_ACTIVE_LVL\x10\xd1.\x127\n2EXPORTSIGNAL_RESET_ATTRIBUTE_ADV_CMPLT_EVENT_DELAY\x10\xd7.\x12A\n<EXPORTSIGNAL_RESET_ATTRIBUTE_CTR_OUT_EVENT_TOGGLE_IDLE_STATE\x10\xea0\x12:\n5EXPORTSIGNAL_RESET_ATTRIBUTE_SAMP_CLK_OUTPUT_BEHAVIOR\x10\xeb0\x12A\n<EXPORTSIGNAL_RESET_ATTRIBUTE_AI_HOLD_CMPLT_EVENT_OUTPUT_TERM\x10\xed1\x12D\n?EXPORTSIGNAL_RESET_ATTRIBUTE_AI_HOLD_CMPLT_EVENT_PULSE_POLARITY\x10\xee1\x12?\n:EXPORTSIGNAL_RESET_ATTRIBUTE_SAMP_CLK_TIMEBASE_OUTPUT_TERM\x10\xf91\x12A\n<EXPORTSIGNAL_RESET_ATTRIBUTE_CHANGE_DETECT_EVENT_OUTPUT_TERM\x10\x97C\x12G\nBEXPORTSIGNAL_RESET_ATTRIBUTE_DIVIDED_SAMP_CLK_TIMEBASE_OUTPUT_TERM\x10\xa1C\x12D\n?EXPORTSIGNAL_RESET_ATTRIBUTE_WATCHDOG_EXPIRED_EVENT_OUTPUT_TERM\x10\xaaC\x127\n2EXPORTSIGNAL_RESET_ATTRIBUTE_SAMP_CLK_DELAY_OFFSET\x10\xc4C\x12>\n9EXPORTSIGNAL_RESET_ATTRIBUTE_SYNC_PULSE_EVENT_OUTPUT_TERM\x10\xbcD\x12<\n7EXPORTSIGNAL_RESET_ATTRIBUTE_10_MHZ_REF_CLK_OUTPUT_TERM\x10\xeeD\x12@\n;EXPORTSIGNAL_RESET_ATTRIBUTE_RDY_FOR_XFER_EVENT_OUTPUT_TERM\x10\xb5E\x12C\n>EXPORTSIGNAL_RESET_ATTRIBUTE_RDY_FOR_XFER_EVENT_LVL_ACTIVE_LVL\x10\xb6E\x128\n3EXPORTSIGNAL_RESET_ATTRIBUTE_HSHK_EVENT_OUTPUT_TERM\x10\xbaE\x12<\n7EXPORTSIGNAL_RESET_ATTRIBUTE_HSHK_EVENT_OUTPUT_BEHAVIOR\x10\xbbE\x122\n-EXPORTSIGNAL_RESET_ATTRIBUTE_HSHK_EVENT_DELAY\x10\xbcE\x12E\n@EXPORTSIGNAL_RESET_ATTRIBUTE_HSHK_EVENT_INTERLOCKED_ASSERTED_LVL\x10\xbdE\x12H\nCEXPORTSIGNAL_RESET_ATTRIBUTE_HSHK_EVENT_INTERLOCKED_ASSERT_ON_START\x10\xbeE\x12G\nBEXPORTSIGNAL_RESET_ATTRIBUTE_HSHK_EVENT_INTERLOCKED_DEASSERT_DELAY\x10\xbfE\x12;\n6EXPORTSIGNAL_RESET_ATTRIBUTE_HSHK_EVENT_PULSE_POLARITY\x10\xc0E\x128\n3EXPORTSIGNAL_RESET_ATTRIBUTE_HSHK_EVENT_PULSE_WIDTH\x10\xc1E\x12D\n?EXPORTSIGNAL_RESET_ATTRIBUTE_CHANGE_DETECT_EVENT_PULSE_POLARITY\x10\x83F\x12B\n=EXPORTSIGNAL_RESET_ATTRIBUTE_RDY_FOR_XFER_EVENT_DEASSERT_COND\x10\xe3R\x12S\nNEXPORTSIGNAL_RESET_ATTRIBUTE_RDY_FOR_XFER_EVENT_DEASSERT_COND_CUSTOM_THRESHOLD\x10\xe4R*\xfa\x11\n\x1aExportSignalInt32Attribute\x12,\n(EXPORTSIGNAL_INT32_ATTRIBUTE_UNSPECIFIED\x10\x00\x125\n0EXPORTSIGNAL_ATTRIBUTE_START_TRIG_PULSE_POLARITY\x10\x85\x0b\x123\n.EXPORTSIGNAL_ATTRIBUTE_REF_TRIG_PULSE_POLARITY\x10\x91\x0b\x128\n3EXPORTSIGNAL_ATTRIBUTE_START_TRIG_PULSE_WIDTH_UNITS\x10\x82,\x125\n0EXPORTSIGNAL_ATTRIBUTE_PAUSE_TRIG_LVL_ACTIVE_LVL\x10\x96,\x12<\n7EXPORTSIGNAL_ATTRIBUTE_RDY_FOR_REF_EVENT_PULSE_POLARITY\x10\xa2,\x12?\n:EXPORTSIGNAL_ATTRIBUTE_RDY_FOR_REF_EVENT_PULSE_WIDTH_UNITS\x10\xa3,\x12<\n7EXPORTSIGNAL_ATTRIBUTE_DATA_ACTIVE_EVENT_LVL_ACTIVE_LVL\x10\xb4,\x123\n.EXPORTSIGNAL_ATTRIBUTE_ADV_TRIG_PULSE_POLARITY\x10\xc6,\x126\n1EXPORTSIGNAL_ATTRIBUTE_ADV_TRIG_PULSE_WIDTH_UNITS\x10\xc7,\x12:\n5EXPORTSIGNAL_ATTRIBUTE_ADV_CMPLT_EVENT_PULSE_POLARITY\x10\xd2,\x12=\n8EXPORTSIGNAL_ATTRIBUTE_ADV_CMPLT_EVENT_PULSE_WIDTH_UNITS\x10\xd3,\x12:\n5EXPORTSIGNAL_ATTRIBUTE_20_MHZ_TIMEBASE_PULSE_POLARITY\x10\xd8,\x12=\n8EXPORTSIGNAL_ATTRIBUTE_20_MHZ_TIMEBASE_PULSE_WIDTH_UNITS\x10\xd9,\x123\n.EXPORTSIGNAL_ATTRIBUTE_SAMP_CLK_PULSE_POLARITY\x10\xe4,\x126\n1EXPORTSIGNAL_ATTRIBUTE_SAMP_CLK_PULSE_WIDTH_UNITS\x10\xe5,\x126\n1EXPORTSIGNAL_ATTRIBUTE_AI_CONV_CLK_PULSE_POLARITY\x10\x88-\x129\n4EXPORTSIGNAL_ATTRIBUTE_AI_CONV_CLK_PULSE_WIDTH_UNITS\x10\x89-\x127\n2EXPORTSIGNAL_ATTRIBUTE_FREQ_OUT_CLK_PULSE_POLARITY\x10\x92.\x12:\n5EXPORTSIGNAL_ATTRIBUTE_FREQ_OUT_CLK_PULSE_WIDTH_UNITS\x10\x93.\x128\n3EXPORTSIGNAL_ATTRIBUTE_CTR_OUT_EVENT_PULSE_POLARITY\x10\x98.\x12;\n6EXPORTSIGNAL_ATTRIBUTE_CTR_OUT_EVENT_PULSE_WIDTH_UNITS\x10\x99.\x122\n-EXPORTSIGNAL_ATTRIBUTE_REF_CLK_PULSE_POLARITY\x10\xb6.\x125\n0EXPORTSIGNAL_ATTRIBUTE_REF_CLK_PULSE_WIDTH_UNITS\x10\xb7.\x126\n1EXPORTSIGNAL_ATTRIBUTE_START_TRIG_OUTPUT_BEHAVIOR\x10\xc3.\x12;\n6EXPORTSIGNAL_ATTRIBUTE_START_TRIG_TOGGLE_INITIAL_STATE\x10\xc4.\x122\n-EXPORTSIGNAL_ATTRIBUTE_START_TRIG_DELAY_UNITS\x10\xcd.\x129\n4EXPORTSIGNAL_ATTRIBUTE_CTR_OUT_EVENT_OUTPUT_BEHAVIOR\x10\xcf.\x126\n1EXPORTSIGNAL_ATTRIBUTE_CTR_OUT_EVENT_LVL_POLARITY\x10\xd0.\x12>\n9EXPORTSIGNAL_ATTRIBUTE_RDY_FOR_START_EVENT_LVL_ACTIVE_LVL\x10\xd1.\x12;\n6EXPORTSIGNAL_ATTRIBUTE_CTR_OUT_EVENT_TOGGLE_IDLE_STATE\x10\xea0\x124\n/EXPORTSIGNAL_ATTRIBUTE_SAMP_CLK_OUTPUT_BEHAVIOR\x10\xeb0\x12>\n9EXPORTSIGNAL_ATTRIBUTE_AI_HOLD_CMPLT_EVENT_PULSE_POLARITY\x10\xee1\x12=\n8EXPORTSIGNAL_ATTRIBUTE_RDY_FOR_XFER_EVENT_LVL_ACTIVE_LVL\x10\xb6E\x126\n1EXPORTSIGNAL_ATTRIBUTE_HSHK_EVENT_OUTPUT_BEHAVIOR\x10\xbbE\x12?\n:EXPORTSIGNAL_ATTRIBUTE_HSHK_EVENT_INTERLOCKED_ASSERTED_LVL\x10\xbdE\x125\n0EXPORTSIGNAL_ATTRIBUTE_HSHK_EVENT_PULSE_POLARITY\x10\xc0E\x12>\n9EXPORTSIGNAL_ATTRIBUTE_CHANGE_DETECT_EVENT_PULSE_POLARITY\x10\x83F\x12<\n7EXPORTSIGNAL_ATTRIBUTE_RDY_FOR_XFER_EVENT_DEASSERT_COND\x10\xe3R*\xc0\x01\n\x19ExportSignalBoolAttribute\x12+\n\'EXPORTSIGNAL_BOOL_ATTRIBUTE_UNSPECIFIED\x10\x00\x122\n-EXPORTSIGNAL_ATTRIBUTE_ADV_CMPLT_EVENT_ENABLE\x10\xca,\x12B\n=EXPORTSIGNAL_ATTRIBUTE_HSHK_EVENT_INTERLOCKED_ASSERT_ON_START\x10\xbeE*\xd9\x01\n\x1bExportSignalUInt32Attribute\x12-\n)EXPORTSIGNAL_UINT32_ATTRIBUTE_UNSPECIFIED\x10\x00\x12<\n7EXPORTSIGNAL_ATTRIBUTE_20_MHZ_TIMEBASE_DIVIDE_DOWN_BY_N\x10\xd6,\x12M\nHEXPORTSIGNAL_ATTRIBUTE_RDY_FOR_XFER_EVENT_DEASSERT_COND_CUSTOM_THRESHOLD\x10\xe4R*\xa9\x01\n\x1fPersistedChannelStringAttribute\x121\n-PERSISTEDCHANNEL_STRING_ATTRIBUTE_UNSPECIFIED\x10\x00\x12+\n&PERSISTEDCHANNEL_ATTRIBUTE_ACTIVE_CHAN\x10\xcfE\x12&\n!PERSISTEDCHANNEL_ATTRIBUTE_AUTHOR\x10\xd0E*\xc7\x01\n\x1dPersistedChannelBoolAttribute\x12/\n+PERSISTEDCHANNEL_BOOL_ATTRIBUTE_UNSPECIFIED\x10\x00\x129\n4PERSISTEDCHANNEL_ATTRIBUTE_ALLOW_INTERACTIVE_EDITING\x10\xd1E\x12:\n5PERSISTEDCHANNEL_ATTRIBUTE_ALLOW_INTERACTIVE_DELETION\x10\xd2E*\xa2\x01\n\x1dPersistedScaleStringAttribute\x12/\n+PERSISTEDSCALE_STRING_ATTRIBUTE_UNSPECIFIED\x10\x00\x12*\n%PERSISTEDSCALE_ATTRIBUTE_ACTIVE_SCALE\x10\xd3E\x12$\n\x1fPERSISTEDSCALE_ATTRIBUTE_AUTHOR\x10\xd4E*\xbf\x01\n\x1bPersistedScaleBoolAttribute\x12-\n)PERSISTEDSCALE_BOOL_ATTRIBUTE_UNSPECIFIED\x10\x00\x127\n2PERSISTEDSCALE_ATTRIBUTE_ALLOW_INTERACTIVE_EDITING\x10\xd5E\x128\n3PERSISTEDSCALE_ATTRIBUTE_ALLOW_INTERACTIVE_DELETION\x10\xd6E*\x9d\x01\n\x1cPersistedTaskStringAttribute\x12.\n*PERSISTEDTASK_STRING_ATTRIBUTE_UNSPECIFIED\x10\x00\x12(\n#PERSISTEDTASK_ATTRIBUTE_ACTIVE_TASK\x10\xcbE\x12#\n\x1ePERSISTEDTASK_ATTRIBUTE_AUTHOR\x10\xccE*\xbb\x01\n\x1aPersistedTaskBoolAttribute\x12,\n(PERSISTEDTASK_BOOL_ATTRIBUTE_UNSPECIFIED\x10\x00\x126\n1PERSISTEDTASK_ATTRIBUTE_ALLOW_INTERACTIVE_EDITING\x10\xcdE\x127\n2PERSISTEDTASK_ATTRIBUTE_ALLOW_INTERACTIVE_DELETION\x10\xceE*\xbe\x03\n\x1ePhysicalChannelUInt32Attribute\x120\n,PHYSICALCHANNEL_UINT32_ATTRIBUTE_UNSPECIFIED\x10\x00\x128\n3PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_TEDS_MFG_ID\x10\xdaC\x12;\n6PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_TEDS_MODEL_NUM\x10\xdbC\x12<\n7PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_TEDS_SERIAL_NUM\x10\xdcC\x12=\n8PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_TEDS_VERSION_NUM\x10\xddC\x12:\n5PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_DI_PORT_WIDTH\x10\xa4S\x12:\n5PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_DO_PORT_WIDTH\x10\xa7S*\xd0\x01\n\x1ePhysicalChannelStringAttribute\x120\n,PHYSICALCHANNEL_STRING_ATTRIBUTE_UNSPECIFIED\x10\x00\x12@\n;PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_TEDS_VERSION_LETTER\x10\xdeC\x12:\n5PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AI_INPUT_SRCS\x10\xd8_*\x8e\x01\n\x1dPhysicalChannelBytesAttribute\x12/\n+PHYSICALCHANNEL_BYTES_ATTRIBUTE_UNSPECIFIED\x10\x00\x12<\n7PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_TEDS_BIT_STREAM\x10\xdfC*\x9e\x01\n#PhysicalChannelUInt32ArrayAttribute\x126\n2PHYSICALCHANNEL_UINT32_ARRAY_ATTRIBUTE_UNSPECIFIED\x10\x00\x12?\n:PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_TEDS_TEMPLATE_I_DS\x10\x8fE*\xce\x02\n\x1dPhysicalChannelInt32Attribute\x12/\n+PHYSICALCHANNEL_INT32_ATTRIBUTE_UNSPECIFIED\x10\x00\x129\n4PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AI_TERM_CFGS\x10\xc2F\x129\n4PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AO_TERM_CFGS\x10\xa3S\x12B\n=PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AI_POWER_CONTROL_TYPE\x10\xeeb\x12B\n=PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_DIG_PORT_LOGIC_FAMILY\x10\xebc*\x82\x06\n\x1cPhysicalChannelBoolAttribute\x12.\n*PHYSICALCHANNEL_BOOL_ATTRIBUTE_UNSPECIFIED\x10\x00\x12B\n=PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_DI_SAMP_CLK_SUPPORTED\x10\xa5S\x12G\nBPHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_DI_CHANGE_DETECT_SUPPORTED\x10\xa6S\x12B\n=PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_DO_SAMP_CLK_SUPPORTED\x10\xa8S\x12E\n@PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AO_MANUAL_CONTROL_ENABLE\x10\x9eT\x12M\nHPHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AO_MANUAL_CONTROL_SHORT_DETECTED\x10\xc3]\x12:\n5PHYSICALCHANNEL_ATTRIBUTE_AO_POWER_AMP_CHANNEL_ENABLE\x10\xe2`\x127\n2PHYSICALCHANNEL_ATTRIBUTE_AO_POWER_AMP_OVERCURRENT\x10\xe4`\x12D\n?PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AI_POWER_CONTROL_ENABLE\x10\xedb\x12F\nAPHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AI_SENSOR_POWER_OPEN_CHAN\x10\xfcb\x12H\nCPHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AI_SENSOR_POWER_OVERCURRENT\x10\xfdb*\x8c\x04\n\x1dPhysicalChannelResetAttribute\x12/\n+PHYSICALCHANNEL_RESET_ATTRIBUTE_UNSPECIFIED\x10\x00\x12K\nFPHYSICALCHANNEL_RESET_ATTRIBUTE_PHYSICAL_CHAN_AO_MANUAL_CONTROL_ENABLE\x10\x9eT\x12@\n;PHYSICALCHANNEL_RESET_ATTRIBUTE_AO_POWER_AMP_CHANNEL_ENABLE\x10\xe2`\x12K\nFPHYSICALCHANNEL_RESET_ATTRIBUTE_PHYSICAL_CHAN_AI_POWER_CONTROL_VOLTAGE\x10\xecb\x12J\nEPHYSICALCHANNEL_RESET_ATTRIBUTE_PHYSICAL_CHAN_AI_POWER_CONTROL_ENABLE\x10\xedb\x12H\nCPHYSICALCHANNEL_RESET_ATTRIBUTE_PHYSICAL_CHAN_AI_POWER_CONTROL_TYPE\x10\xeeb\x12H\nCPHYSICALCHANNEL_RESET_ATTRIBUTE_PHYSICAL_CHAN_DIG_PORT_LOGIC_FAMILY\x10\xebc*\x8e\x03\n\x1ePhysicalChannelDoubleAttribute\x120\n,PHYSICALCHANNEL_DOUBLE_ATTRIBUTE_UNSPECIFIED\x10\x00\x12H\nCPHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AO_MANUAL_CONTROL_AMPLITUDE\x10\x9fT\x12C\n>PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AO_MANUAL_CONTROL_FREQ\x10\xa0T\x120\n+PHYSICALCHANNEL_ATTRIBUTE_AO_POWER_AMP_GAIN\x10\xe5`\x122\n-PHYSICALCHANNEL_ATTRIBUTE_AO_POWER_AMP_OFFSET\x10\xe6`\x12E\n@PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AI_POWER_CONTROL_VOLTAGE\x10\xecb*\xcb\x05\n"PhysicalChannelInt32ArrayAttribute\x125\n1PHYSICALCHANNEL_INT32_ARRAY_ATTRIBUTE_UNSPECIFIED\x10\x00\x12D\n?PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AI_SUPPORTED_MEAS_TYPES\x10\xd7_\x12F\nAPHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AO_SUPPORTED_OUTPUT_TYPES\x10\xd9_\x12D\n?PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_CI_SUPPORTED_MEAS_TYPES\x10\xda_\x12F\nAPHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_CO_SUPPORTED_OUTPUT_TYPES\x10\xdb_\x12:\n5PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_DI_SAMP_MODES\x10\xe0_\x12:\n5PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_DO_SAMP_MODES\x10\xe1_\x12E\n@PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_NAV_SUPPORTED_MEAS_TYPES\x10\xb7`\x12O\nJPHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AO_SUPPORTED_POWER_UP_OUTPUT_TYPES\x10\xce`\x12B\n=PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AI_SENSOR_POWER_TYPES\x10\xf9b*\xe9\x01\n#PhysicalChannelDoubleArrayAttribute\x126\n2PHYSICALCHANNEL_DOUBLE_ARRAY_ATTRIBUTE_UNSPECIFIED\x10\x00\x129\n4PHYSICALCHANNEL_ATTRIBUTE_AO_POWER_AMP_SCALING_COEFF\x10\xe3`\x12O\nJPHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AI_SENSOR_POWER_VOLTAGE_RANGE_VALS\x10\xfab*\x83\x02\n\x12ReadInt32Attribute\x12$\n READ_INT32_ATTRIBUTE_UNSPECIFIED\x10\x00\x12\x1d\n\x18READ_ATTRIBUTE_OVERWRITE\x10\x91$\x12\x1f\n\x1aREAD_ATTRIBUTE_RELATIVE_TO\x10\x8a2\x12\x1a\n\x15READ_ATTRIBUTE_OFFSET\x10\x8b2\x12\x1d\n\x18READ_ATTRIBUTE_WAIT_MODE\x10\xb2D\x12 \n\x1bREAD_ATTRIBUTE_LOGGING_MODE\x10\xc5]\x12*\n%READ_ATTRIBUTE_LOGGING_TDMS_OPERATION\x10\xc7]*\xf7\x05\n\x12ReadResetAttribute\x12$\n READ_RESET_ATTRIBUTE_UNSPECIFIED\x10\x00\x12#\n\x1eREAD_RESET_ATTRIBUTE_OVERWRITE\x10\x91$\x12-\n(READ_RESET_ATTRIBUTE_READ_ALL_AVAIL_SAMP\x10\x95$\x12*\n%READ_RESET_ATTRIBUTE_CHANNELS_TO_READ\x10\xa30\x12$\n\x1fREAD_RESET_ATTRIBUTE_AUTO_START\x10\xa60\x12%\n READ_RESET_ATTRIBUTE_RELATIVE_TO\x10\x8a2\x12 \n\x1bREAD_RESET_ATTRIBUTE_OFFSET\x10\x8b2\x12#\n\x1eREAD_RESET_ATTRIBUTE_WAIT_MODE\x10\xb2D\x12$\n\x1fREAD_RESET_ATTRIBUTE_SLEEP_TIME\x10\xb0E\x12+\n&READ_RESET_ATTRIBUTE_LOGGING_FILE_PATH\x10\xc4]\x12&\n!READ_RESET_ATTRIBUTE_LOGGING_MODE\x10\xc5]\x121\n,READ_RESET_ATTRIBUTE_LOGGING_TDMS_GROUP_NAME\x10\xc6]\x120\n+READ_RESET_ATTRIBUTE_LOGGING_TDMS_OPERATION\x10\xc7]\x121\n,READ_RESET_ATTRIBUTE_LOGGING_FILE_WRITE_SIZE\x10\xc3_\x129\n4READ_RESET_ATTRIBUTE_LOGGING_FILE_PREALLOCATION_SIZE\x10\xc6_\x12\'\n"READ_RESET_ATTRIBUTE_LOGGING_PAUSE\x10\xe3_\x120\n+READ_RESET_ATTRIBUTE_LOGGING_SAMPS_PER_FILE\x10\xe4_*\x8d\x08\n\x11ReadBoolAttribute\x12#\n\x1fREAD_BOOL_ATTRIBUTE_UNSPECIFIED\x10\x00\x12\'\n"READ_ATTRIBUTE_READ_ALL_AVAIL_SAMP\x10\x95$\x12\x1e\n\x19READ_ATTRIBUTE_AUTO_START\x10\xa60\x12*\n%READ_ATTRIBUTE_OVERLOADED_CHANS_EXIST\x10\xf4B\x120\n+READ_ATTRIBUTE_CHANGE_DETECT_HAS_OVERFLOWED\x10\x94C\x12+\n&READ_ATTRIBUTE_OVERCURRENT_CHANS_EXIST\x10\xe6S\x121\n,READ_ATTRIBUTE_OPEN_CURRENT_LOOP_CHANS_EXIST\x10\x89T\x12,\n\'READ_ATTRIBUTE_OPEN_THRMCPL_CHANS_EXIST\x10\x96U\x127\n2READ_ATTRIBUTE_COMMON_MODE_RANGE_ERROR_CHANS_EXIST\x10\x98U\x12;\n6READ_ATTRIBUTE_ACCESSORY_INSERTION_OR_REMOVAL_DETECTED\x10\xf0^\x12!\n\x1cREAD_ATTRIBUTE_LOGGING_PAUSE\x10\xe3_\x12 \n\x1bREAD_ATTRIBUTE_NAV_FIX_LOST\x10\xb5`\x12/\n*READ_ATTRIBUTE_OVERTEMPERATURE_CHANS_EXIST\x10\x81a\x12+\n&READ_ATTRIBUTE_EXCIT_FAULT_CHANS_EXIST\x10\x88a\x12$\n\x1fREAD_ATTRIBUTE_OPEN_CHANS_EXIST\x10\x80b\x12,\n\'READ_ATTRIBUTE_PLL_UNLOCKED_CHANS_EXIST\x10\x98b\x12-\n(READ_ATTRIBUTE_SYNC_UNLOCKED_CHANS_EXIST\x10\xbdb\x122\n-READ_ATTRIBUTE_INPUT_LIMITS_FAULT_CHANS_EXIST\x10\x8fc\x122\n-READ_ATTRIBUTE_POWER_SUPPLY_FAULT_CHANS_EXIST\x10\x92c\x122\n-READ_ATTRIBUTE_REMOTE_SENSE_ERROR_CHANS_EXIST\x10\xddc\x12/\n*READ_ATTRIBUTE_AUX_POWER_ERROR_CHANS_EXIST\x10\xdfc\x125\n0READ_ATTRIBUTE_REVERSE_VOLTAGE_ERROR_CHANS_EXIST\x10\xe6c*\xf2\x01\n\x13ReadUInt64Attribute\x12%\n!READ_UINT64_ATTRIBUTE_UNSPECIFIED\x10\x00\x12!\n\x1cREAD_ATTRIBUTE_CURR_READ_POS\x10\xa1$\x120\n+READ_ATTRIBUTE_TOTAL_SAMP_PER_CHAN_ACQUIRED\x10\xaa2\x123\n.READ_ATTRIBUTE_LOGGING_FILE_PREALLOCATION_SIZE\x10\xc6_\x12*\n%READ_ATTRIBUTE_LOGGING_SAMPS_PER_FILE\x10\xe4_*\x87\x02\n\x13ReadUInt32Attribute\x12%\n!READ_UINT32_ATTRIBUTE_UNSPECIFIED\x10\x00\x12\'\n"READ_ATTRIBUTE_AVAIL_SAMP_PER_CHAN\x10\xa3$\x12"\n\x1dREAD_ATTRIBUTE_RAW_DATA_WIDTH\x10\xfaB\x12\x1d\n\x18READ_ATTRIBUTE_NUM_CHANS\x10\xfbB\x120\n+READ_ATTRIBUTE_DIGITAL_LINES_BYTES_PER_CHAN\x10\xfcB\x12+\n&READ_ATTRIBUTE_LOGGING_FILE_WRITE_SIZE\x10\xc3_*\x9b\x07\n\x13ReadStringAttribute\x12%\n!READ_STRING_ATTRIBUTE_UNSPECIFIED\x10\x00\x12$\n\x1fREAD_ATTRIBUTE_CHANNELS_TO_READ\x10\xa30\x12$\n\x1fREAD_ATTRIBUTE_OVERLOADED_CHANS\x10\xf5B\x12%\n READ_ATTRIBUTE_OVERCURRENT_CHANS\x10\xe7S\x12+\n&READ_ATTRIBUTE_OPEN_CURRENT_LOOP_CHANS\x10\x8aT\x12&\n!READ_ATTRIBUTE_OPEN_THRMCPL_CHANS\x10\x97U\x121\n,READ_ATTRIBUTE_COMMON_MODE_RANGE_ERROR_CHANS\x10\x99U\x12%\n READ_ATTRIBUTE_LOGGING_FILE_PATH\x10\xc4]\x12+\n&READ_ATTRIBUTE_LOGGING_TDMS_GROUP_NAME\x10\xc6]\x12=\n8READ_ATTRIBUTE_DEVS_WITH_INSERTED_OR_REMOVED_ACCESSORIES\x10\xf1^\x12)\n$READ_ATTRIBUTE_OVERTEMPERATURE_CHANS\x10\x82a\x12%\n READ_ATTRIBUTE_EXCIT_FAULT_CHANS\x10\x89a\x12\x1e\n\x19READ_ATTRIBUTE_OPEN_CHANS\x10\x81b\x12&\n!READ_ATTRIBUTE_OPEN_CHANS_DETAILS\x10\x82b\x12&\n!READ_ATTRIBUTE_PLL_UNLOCKED_CHANS\x10\x99b\x12\'\n"READ_ATTRIBUTE_SYNC_UNLOCKED_CHANS\x10\xbeb\x12,\n\'READ_ATTRIBUTE_INPUT_LIMITS_FAULT_CHANS\x10\x90c\x12,\n\'READ_ATTRIBUTE_POWER_SUPPLY_FAULT_CHANS\x10\x93c\x12,\n\'READ_ATTRIBUTE_REMOTE_SENSE_ERROR_CHANS\x10\xdec\x12)\n$READ_ATTRIBUTE_AUX_POWER_ERROR_CHANS\x10\xe0c\x12/\n*READ_ATTRIBUTE_REVERSE_VOLTAGE_ERROR_CHANS\x10\xe7c*\\\n\x13ReadDoubleAttribute\x12%\n!READ_DOUBLE_ATTRIBUTE_UNSPECIFIED\x10\x00\x12\x1e\n\x19READ_ATTRIBUTE_SLEEP_TIME\x10\xb0E*q\n\x17RealTimeUInt32Attribute\x12)\n%REALTIME_UINT32_ATTRIBUTE_UNSPECIFIED\x10\x00\x12+\n&REALTIME_ATTRIBUTE_NUM_OF_WARMUP_ITERS\x10\xedE*\xd6\x02\n\x16RealTimeResetAttribute\x12(\n$REALTIME_RESET_ATTRIBUTE_UNSPECIFIED\x10\x00\x121\n,REALTIME_RESET_ATTRIBUTE_NUM_OF_WARMUP_ITERS\x10\xedE\x12:\n5REALTIME_RESET_ATTRIBUTE_CONV_LATE_ERRORS_TO_WARNINGS\x10\xeeE\x12>\n9REALTIME_RESET_ATTRIBUTE_WAIT_FOR_NEXT_SAMP_CLK_WAIT_MODE\x10\xefE\x120\n+REALTIME_RESET_ATTRIBUTE_REPORT_MISSED_SAMP\x10\x99F\x121\n,REALTIME_RESET_ATTRIBUTE_WRITE_RECOVERY_MODE\x10\x9aF*\xa2\x01\n\x15RealTimeBoolAttribute\x12\'\n#REALTIME_BOOL_ATTRIBUTE_UNSPECIFIED\x10\x00\x124\n/REALTIME_ATTRIBUTE_CONV_LATE_ERRORS_TO_WARNINGS\x10\xeeE\x12*\n%REALTIME_ATTRIBUTE_REPORT_MISSED_SAMP\x10\x99F*\xa9\x01\n\x16RealTimeInt32Attribute\x12(\n$REALTIME_INT32_ATTRIBUTE_UNSPECIFIED\x10\x00\x128\n3REALTIME_ATTRIBUTE_WAIT_FOR_NEXT_SAMP_CLK_WAIT_MODE\x10\xefE\x12+\n&REALTIME_ATTRIBUTE_WRITE_RECOVERY_MODE\x10\x9aF*}\n\x14ScaleStringAttribute\x12&\n"SCALE_STRING_ATTRIBUTE_UNSPECIFIED\x10\x00\x12\x1a\n\x15SCALE_ATTRIBUTE_DESCR\x10\xa6$\x12!\n\x1cSCALE_ATTRIBUTE_SCALED_UNITS\x10\x9b2*\xa0\x02\n\x14ScaleDoubleAttribute\x12&\n"SCALE_DOUBLE_ATTRIBUTE_UNSPECIFIED\x10\x00\x12\x1e\n\x19SCALE_ATTRIBUTE_LIN_SLOPE\x10\xa7$\x12$\n\x1fSCALE_ATTRIBUTE_LIN_Y_INTERCEPT\x10\xa8$\x12#\n\x1eSCALE_ATTRIBUTE_MAP_SCALED_MAX\x10\xa9$\x12#\n\x1eSCALE_ATTRIBUTE_MAP_SCALED_MIN\x10\xb0$\x12\'\n"SCALE_ATTRIBUTE_MAP_PRE_SCALED_MAX\x10\xb1$\x12\'\n"SCALE_ATTRIBUTE_MAP_PRE_SCALED_MIN\x10\xb2$*\xef\x01\n\x19ScaleDoubleArrayAttribute\x12,\n(SCALE_DOUBLE_ARRAY_ATTRIBUTE_UNSPECIFIED\x10\x00\x12\'\n"SCALE_ATTRIBUTE_POLY_FORWARD_COEFF\x10\xb4$\x12\'\n"SCALE_ATTRIBUTE_POLY_REVERSE_COEFF\x10\xb5$\x12&\n!SCALE_ATTRIBUTE_TABLE_SCALED_VALS\x10\xb6$\x12*\n%SCALE_ATTRIBUTE_TABLE_PRE_SCALED_VALS\x10\xb7$*~\n\x13ScaleInt32Attribute\x12%\n!SCALE_INT32_ATTRIBUTE_UNSPECIFIED\x10\x00\x12%\n SCALE_ATTRIBUTE_PRE_SCALED_UNITS\x10\xf71\x12\x19\n\x14SCALE_ATTRIBUTE_TYPE\x10\xa92*\xc0\x01\n\x15SystemStringAttribute\x12\'\n#SYSTEM_STRING_ATTRIBUTE_UNSPECIFIED\x10\x00\x12"\n\x1dSYSTEM_ATTRIBUTE_GLOBAL_CHANS\x10\xe5$\x12\x1c\n\x17SYSTEM_ATTRIBUTE_SCALES\x10\xe6$\x12\x1b\n\x16SYSTEM_ATTRIBUTE_TASKS\x10\xe7$\x12\x1f\n\x1aSYSTEM_ATTRIBUTE_DEV_NAMES\x10\xbb2*\xc2\x01\n\x15SystemUInt32Attribute\x12\'\n#SYSTEM_UINT32_ATTRIBUTE_UNSPECIFIED\x10\x00\x12)\n$SYSTEM_ATTRIBUTE_NIDAQ_MAJOR_VERSION\x10\xf2$\x12)\n$SYSTEM_ATTRIBUTE_NIDAQ_MINOR_VERSION\x10\xa32\x12*\n%SYSTEM_ATTRIBUTE_NIDAQ_UPDATE_VERSION\x10\xa2^*\x91\x01\n\x13TaskStringAttribute\x12%\n!TASK_STRING_ATTRIBUTE_UNSPECIFIED\x10\x00\x12\x1c\n\x17TASK_ATTRIBUTE_CHANNELS\x10\xf3$\x12\x18\n\x13TASK_ATTRIBUTE_NAME\x10\xf6$\x12\x1b\n\x16TASK_ATTRIBUTE_DEVICES\x10\x8eF*V\n\x11TaskBoolAttribute\x12#\n\x1fTASK_BOOL_ATTRIBUTE_UNSPECIFIED\x10\x00\x12\x1c\n\x17TASK_ATTRIBUTE_COMPLETE\x10\xf4$*|\n\x13TaskUInt32Attribute\x12%\n!TASK_UINT32_ATTRIBUTE_UNSPECIFIED\x10\x00\x12\x1d\n\x18TASK_ATTRIBUTE_NUM_CHANS\x10\x81C\x12\x1f\n\x1aTASK_ATTRIBUTE_NUM_DEVICES\x10\xbaS*\xb0\x06\n\x14TimingInt32Attribute\x12&\n"TIMING_INT32_ATTRIBUTE_UNSPECIFIED\x10\x00\x12*\n%TIMING_ATTRIBUTE_SAMP_QUANT_SAMP_MODE\x10\x80&\x12*\n%TIMING_ATTRIBUTE_SAMP_CLK_ACTIVE_EDGE\x10\x81&\x125\n0TIMING_ATTRIBUTE_DELAY_FROM_SAMP_CLK_DELAY_UNITS\x10\x84&\x12*\n%TIMING_ATTRIBUTE_AI_CONV_TIMEBASE_SRC\x10\xb9&\x12&\n!TIMING_ATTRIBUTE_SAMP_TIMING_TYPE\x10\xc7&\x12)\n$TIMING_ATTRIBUTE_AI_CONV_ACTIVE_EDGE\x10\xd30\x123\n.TIMING_ATTRIBUTE_SAMP_CLK_TIMEBASE_ACTIVE_EDGE\x10\xec1\x12%\n TIMING_ATTRIBUTE_HSHK_START_COND\x10\xc3E\x121\n,TIMING_ATTRIBUTE_HSHK_SAMPLE_INPUT_DATA_WHEN\x10\xc4E\x121\n,TIMING_ATTRIBUTE_SAMP_CLK_UNDERFLOW_BEHAVIOR\x10\xe1R\x12/\n*TIMING_ATTRIBUTE_SAMP_CLK_OVERRUN_BEHAVIOR\x10\xfc]\x121\n,TIMING_ATTRIBUTE_IMPLICIT_UNDERFLOW_BEHAVIOR\x10\xfd]\x12%\n TIMING_ATTRIBUTE_SYNC_PULSE_TYPE\x10\xb6b\x12/\n*TIMING_ATTRIBUTE_SYNC_PULSE_TIME_TIMESCALE\x10\xb8b\x124\n/TIMING_ATTRIBUTE_FIRST_SAMP_TIMESTAMP_TIMESCALE\x10\xbbb\x12.\n)TIMING_ATTRIBUTE_FIRST_SAMP_CLK_TIMESCALE\x10\x83c*\xa9\x18\n\x14TimingResetAttribute\x12&\n"TIMING_RESET_ATTRIBUTE_UNSPECIFIED\x10\x00\x120\n+TIMING_RESET_ATTRIBUTE_SAMP_QUANT_SAMP_MODE\x10\x80&\x120\n+TIMING_RESET_ATTRIBUTE_SAMP_CLK_ACTIVE_EDGE\x10\x81&\x122\n-TIMING_RESET_ATTRIBUTE_SAMP_CLK_TIMEBASE_RATE\x10\x83&\x12;\n6TIMING_RESET_ATTRIBUTE_DELAY_FROM_SAMP_CLK_DELAY_UNITS\x10\x84&\x12A\n<TIMING_RESET_ATTRIBUTE_SAMP_CLK_TIMEBASE_MASTER_TIMEBASE_DIV\x10\x85&\x121\n,TIMING_RESET_ATTRIBUTE_SAMP_CLK_TIMEBASE_SRC\x10\x88&\x124\n/TIMING_RESET_ATTRIBUTE_SAMP_QUANT_SAMP_PER_CHAN\x10\x90&\x12(\n#TIMING_RESET_ATTRIBUTE_REF_CLK_RATE\x10\x95&\x12\'\n"TIMING_RESET_ATTRIBUTE_REF_CLK_SRC\x10\x96&\x125\n0TIMING_RESET_ATTRIBUTE_DELAY_FROM_SAMP_CLK_DELAY\x10\x97&\x120\n+TIMING_RESET_ATTRIBUTE_AI_CONV_TIMEBASE_DIV\x10\xb5&\x120\n+TIMING_RESET_ATTRIBUTE_AI_CONV_TIMEBASE_SRC\x10\xb9&\x12/\n*TIMING_RESET_ATTRIBUTE_MASTER_TIMEBASE_SRC\x10\xc3&\x12)\n$TIMING_RESET_ATTRIBUTE_SAMP_CLK_RATE\x10\xc4&\x12,\n\'TIMING_RESET_ATTRIBUTE_SAMP_TIMING_TYPE\x10\xc7&\x120\n+TIMING_RESET_ATTRIBUTE_MASTER_TIMEBASE_RATE\x10\x95)\x12\'\n"TIMING_RESET_ATTRIBUTE_AI_CONV_SRC\x10\x82*\x12(\n#TIMING_RESET_ATTRIBUTE_AI_CONV_RATE\x10\xc80\x12(\n#TIMING_RESET_ATTRIBUTE_SAMP_CLK_SRC\x10\xd20\x12/\n*TIMING_RESET_ATTRIBUTE_AI_CONV_ACTIVE_EDGE\x10\xd30\x121\n,TIMING_RESET_ATTRIBUTE_SAMP_CLK_TIMEBASE_DIV\x10\xeb1\x129\n4TIMING_RESET_ATTRIBUTE_SAMP_CLK_TIMEBASE_ACTIVE_EDGE\x10\xec1\x12G\nBTIMING_RESET_ATTRIBUTE_CHANGE_DETECT_DI_RISING_EDGE_PHYSICAL_CHANS\x10\x95C\x12H\nCTIMING_RESET_ATTRIBUTE_CHANGE_DETECT_DI_FALLING_EDGE_PHYSICAL_CHANS\x10\x96C\x12<\n7TIMING_RESET_ATTRIBUTE_ON_DEMAND_SIMULTANEOUS_AO_ENABLE\x10\xa0C\x124\n/TIMING_RESET_ATTRIBUTE_SAMP_CLK_DIG_FLTR_ENABLE\x10\x9eD\x12=\n8TIMING_RESET_ATTRIBUTE_SAMP_CLK_DIG_FLTR_MIN_PULSE_WIDTH\x10\x9fD\x12:\n5TIMING_RESET_ATTRIBUTE_SAMP_CLK_DIG_FLTR_TIMEBASE_SRC\x10\xa0D\x12;\n6TIMING_RESET_ATTRIBUTE_SAMP_CLK_DIG_FLTR_TIMEBASE_RATE\x10\xa1D\x124\n/TIMING_RESET_ATTRIBUTE_SAMP_CLK_DIG_SYNC_ENABLE\x10\xa2D\x12*\n%TIMING_RESET_ATTRIBUTE_SYNC_PULSE_SRC\x10\xbdD\x129\n4TIMING_RESET_ATTRIBUTE_SYNC_PULSE_MIN_DELAY_TO_START\x10\xbfD\x121\n,TIMING_RESET_ATTRIBUTE_HSHK_DELAY_AFTER_XFER\x10\xc2E\x12+\n&TIMING_RESET_ATTRIBUTE_HSHK_START_COND\x10\xc3E\x127\n2TIMING_RESET_ATTRIBUTE_HSHK_SAMPLE_INPUT_DATA_WHEN\x10\xc4E\x127\n2TIMING_RESET_ATTRIBUTE_SAMP_CLK_UNDERFLOW_BEHAVIOR\x10\xe1R\x12.\n)TIMING_RESET_ATTRIBUTE_SAMP_TIMING_ENGINE\x10\xa6T\x123\n.TIMING_RESET_ATTRIBUTE_AI_CONV_DIG_FLTR_ENABLE\x10\xdc]\x12<\n7TIMING_RESET_ATTRIBUTE_AI_CONV_DIG_FLTR_MIN_PULSE_WIDTH\x10\xdd]\x129\n4TIMING_RESET_ATTRIBUTE_AI_CONV_DIG_FLTR_TIMEBASE_SRC\x10\xde]\x12:\n5TIMING_RESET_ATTRIBUTE_AI_CONV_DIG_FLTR_TIMEBASE_RATE\x10\xdf]\x123\n.TIMING_RESET_ATTRIBUTE_AI_CONV_DIG_SYNC_ENABLE\x10\xe0]\x125\n0TIMING_RESET_ATTRIBUTE_CHANGE_DETECT_DI_TRISTATE\x10\xfa]\x125\n0TIMING_RESET_ATTRIBUTE_SAMP_CLK_OVERRUN_BEHAVIOR\x10\xfc]\x127\n2TIMING_RESET_ATTRIBUTE_IMPLICIT_UNDERFLOW_BEHAVIOR\x10\xfd]\x122\n-TIMING_RESET_ATTRIBUTE_SYNC_PULSE_RESET_DELAY\x10\xfd^\x12-\n(TIMING_RESET_ATTRIBUTE_SYNC_CLK_INTERVAL\x10\xfe^\x123\n.TIMING_RESET_ATTRIBUTE_TIMING_SYNC_PULSE_FORCE\x10\xbaa\x12A\n<TIMING_RESET_ATTRIBUTE_SAMP_CLK_WRITE_WFM_USE_INITIAL_WFM_DT\x10\xfca\x12+\n&TIMING_RESET_ATTRIBUTE_SYNC_PULSE_TYPE\x10\xb6b\x120\n+TIMING_RESET_ATTRIBUTE_SYNC_PULSE_TIME_WHEN\x10\xb7b\x125\n0TIMING_RESET_ATTRIBUTE_SYNC_PULSE_TIME_TIMESCALE\x10\xb8b\x127\n2TIMING_RESET_ATTRIBUTE_FIRST_SAMP_TIMESTAMP_ENABLE\x10\xb9b\x12:\n5TIMING_RESET_ATTRIBUTE_FIRST_SAMP_TIMESTAMP_TIMESCALE\x10\xbbb\x12/\n*TIMING_RESET_ATTRIBUTE_FIRST_SAMP_CLK_WHEN\x10\x82c\x124\n/TIMING_RESET_ATTRIBUTE_FIRST_SAMP_CLK_TIMESCALE\x10\x83c\x121\n,TIMING_RESET_ATTRIBUTE_FIRST_SAMP_CLK_OFFSET\x10\xaac*\xfd\x06\n\x15TimingDoubleAttribute\x12\'\n#TIMING_DOUBLE_ATTRIBUTE_UNSPECIFIED\x10\x00\x12,\n\'TIMING_ATTRIBUTE_SAMP_CLK_TIMEBASE_RATE\x10\x83&\x12"\n\x1dTIMING_ATTRIBUTE_REF_CLK_RATE\x10\x95&\x12/\n*TIMING_ATTRIBUTE_DELAY_FROM_SAMP_CLK_DELAY\x10\x97&\x12#\n\x1eTIMING_ATTRIBUTE_SAMP_CLK_RATE\x10\xc4&\x12*\n%TIMING_ATTRIBUTE_MASTER_TIMEBASE_RATE\x10\x95)\x12"\n\x1dTIMING_ATTRIBUTE_AI_CONV_RATE\x10\xc80\x127\n2TIMING_ATTRIBUTE_SAMP_CLK_DIG_FLTR_MIN_PULSE_WIDTH\x10\x9fD\x125\n0TIMING_ATTRIBUTE_SAMP_CLK_DIG_FLTR_TIMEBASE_RATE\x10\xa1D\x12*\n%TIMING_ATTRIBUTE_SYNC_PULSE_SYNC_TIME\x10\xbeD\x123\n.TIMING_ATTRIBUTE_SYNC_PULSE_MIN_DELAY_TO_START\x10\xbfD\x12+\n&TIMING_ATTRIBUTE_HSHK_DELAY_AFTER_XFER\x10\xc2E\x12\'\n"TIMING_ATTRIBUTE_SAMP_CLK_MAX_RATE\x10\xc8E\x12&\n!TIMING_ATTRIBUTE_AI_CONV_MAX_RATE\x10\xc9E\x126\n1TIMING_ATTRIBUTE_AI_CONV_DIG_FLTR_MIN_PULSE_WIDTH\x10\xdd]\x124\n/TIMING_ATTRIBUTE_AI_CONV_DIG_FLTR_TIMEBASE_RATE\x10\xdf]\x12+\n&TIMING_ATTRIBUTE_SYNC_PULSE_RESET_TIME\x10\xfc^\x12,\n\'TIMING_ATTRIBUTE_SYNC_PULSE_RESET_DELAY\x10\xfd^\x12+\n&TIMING_ATTRIBUTE_FIRST_SAMP_CLK_OFFSET\x10\xaac*\xa9\x02\n\x15TimingUInt32Attribute\x12\'\n#TIMING_UINT32_ATTRIBUTE_UNSPECIFIED\x10\x00\x12;\n6TIMING_ATTRIBUTE_SAMP_CLK_TIMEBASE_MASTER_TIMEBASE_DIV\x10\x85&\x12*\n%TIMING_ATTRIBUTE_AI_CONV_TIMEBASE_DIV\x10\xb5&\x12+\n&TIMING_ATTRIBUTE_SAMP_CLK_TIMEBASE_DIV\x10\xeb1\x12(\n#TIMING_ATTRIBUTE_SAMP_TIMING_ENGINE\x10\xa6T\x12\'\n"TIMING_ATTRIBUTE_SYNC_CLK_INTERVAL\x10\xfe^*\x94\x05\n\x15TimingStringAttribute\x12\'\n#TIMING_STRING_ATTRIBUTE_UNSPECIFIED\x10\x00\x12+\n&TIMING_ATTRIBUTE_SAMP_CLK_TIMEBASE_SRC\x10\x88&\x12!\n\x1cTIMING_ATTRIBUTE_REF_CLK_SRC\x10\x96&\x12)\n$TIMING_ATTRIBUTE_MASTER_TIMEBASE_SRC\x10\xc3&\x12!\n\x1cTIMING_ATTRIBUTE_AI_CONV_SRC\x10\x82*\x12"\n\x1dTIMING_ATTRIBUTE_SAMP_CLK_SRC\x10\xd20\x12A\n<TIMING_ATTRIBUTE_CHANGE_DETECT_DI_RISING_EDGE_PHYSICAL_CHANS\x10\x95C\x12B\n=TIMING_ATTRIBUTE_CHANGE_DETECT_DI_FALLING_EDGE_PHYSICAL_CHANS\x10\x96C\x124\n/TIMING_ATTRIBUTE_SAMP_CLK_DIG_FLTR_TIMEBASE_SRC\x10\xa0D\x12$\n\x1fTIMING_ATTRIBUTE_SYNC_PULSE_SRC\x10\xbdD\x123\n.TIMING_ATTRIBUTE_AI_CONV_DIG_FLTR_TIMEBASE_SRC\x10\xde]\x12#\n\x1eTIMING_ATTRIBUTE_SAMP_CLK_TERM\x10\x9b^\x12,\n\'TIMING_ATTRIBUTE_SAMP_CLK_TIMEBASE_TERM\x10\x9c^\x12%\n TIMING_ATTRIBUTE_SYNC_PULSE_TERM\x10\x85_*p\n\x15TimingUInt64Attribute\x12\'\n#TIMING_UINT64_ATTRIBUTE_UNSPECIFIED\x10\x00\x12.\n)TIMING_ATTRIBUTE_SAMP_QUANT_SAMP_PER_CHAN\x10\x90&*\x82\x04\n\x13TimingBoolAttribute\x12%\n!TIMING_BOOL_ATTRIBUTE_UNSPECIFIED\x10\x00\x126\n1TIMING_ATTRIBUTE_ON_DEMAND_SIMULTANEOUS_AO_ENABLE\x10\xa0C\x12.\n)TIMING_ATTRIBUTE_SAMP_CLK_DIG_FLTR_ENABLE\x10\x9eD\x12.\n)TIMING_ATTRIBUTE_SAMP_CLK_DIG_SYNC_ENABLE\x10\xa2D\x12-\n(TIMING_ATTRIBUTE_AI_CONV_DIG_FLTR_ENABLE\x10\xdc]\x12-\n(TIMING_ATTRIBUTE_AI_CONV_DIG_SYNC_ENABLE\x10\xe0]\x12/\n*TIMING_ATTRIBUTE_CHANGE_DETECT_DI_TRISTATE\x10\xfa]\x12-\n(TIMING_ATTRIBUTE_TIMING_SYNC_PULSE_FORCE\x10\xbaa\x12;\n6TIMING_ATTRIBUTE_SAMP_CLK_WRITE_WFM_USE_INITIAL_WFM_DT\x10\xfca\x121\n,TIMING_ATTRIBUTE_FIRST_SAMP_TIMESTAMP_ENABLE\x10\xb9b*\xcd\x01\n\x18TimingTimestampAttribute\x12*\n&TIMING_TIMESTAMP_ATTRIBUTE_UNSPECIFIED\x10\x00\x12*\n%TIMING_ATTRIBUTE_SYNC_PULSE_TIME_WHEN\x10\xb7b\x12.\n)TIMING_ATTRIBUTE_FIRST_SAMP_TIMESTAMP_VAL\x10\xbab\x12)\n$TIMING_ATTRIBUTE_FIRST_SAMP_CLK_WHEN\x10\x82c*\xb8\r\n\x15TriggerInt32Attribute\x12\'\n#TRIGGER_INT32_ATTRIBUTE_UNSPECIFIED\x10\x00\x12-\n(TRIGGER_ATTRIBUTE_DIG_EDGE_ADV_TRIG_EDGE\x10\xe0&\x12$\n\x1fTRIGGER_ATTRIBUTE_ADV_TRIG_TYPE\x10\xe5&\x12&\n!TRIGGER_ATTRIBUTE_PAUSE_TRIG_TYPE\x10\xe6&\x12/\n*TRIGGER_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_WHEN\x10\xf1&\x12/\n*TRIGGER_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_WHEN\x10\xf4&\x12.\n)TRIGGER_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_WHEN\x10\x80\'\x12&\n!TRIGGER_ATTRIBUTE_START_TRIG_TYPE\x10\x93\'\x121\n,TRIGGER_ATTRIBUTE_ANLG_EDGE_START_TRIG_SLOPE\x10\x97\'\x12/\n*TRIGGER_ATTRIBUTE_ANLG_WIN_START_TRIG_WHEN\x10\x81(\x12/\n*TRIGGER_ATTRIBUTE_DIG_EDGE_START_TRIG_EDGE\x10\x84(\x122\n-TRIGGER_ATTRIBUTE_DIG_PATTERN_START_TRIG_WHEN\x10\x91(\x12*\n%TRIGGER_ATTRIBUTE_ARM_START_TRIG_TYPE\x10\x94(\x123\n.TRIGGER_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_EDGE\x10\x95(\x12$\n\x1fTRIGGER_ATTRIBUTE_REF_TRIG_TYPE\x10\x99(\x12/\n*TRIGGER_ATTRIBUTE_ANLG_EDGE_REF_TRIG_SLOPE\x10\xa3(\x12-\n(TRIGGER_ATTRIBUTE_ANLG_WIN_REF_TRIG_WHEN\x10\xa7(\x12-\n(TRIGGER_ATTRIBUTE_DIG_EDGE_REF_TRIG_EDGE\x10\xb0(\x120\n+TRIGGER_ATTRIBUTE_DIG_PATTERN_REF_TRIG_WHEN\x10\xb8(\x121\n,TRIGGER_ATTRIBUTE_ANLG_WIN_REF_TRIG_COUPLING\x10\xd70\x12-\n(TRIGGER_ATTRIBUTE_START_TRIG_DELAY_UNITS\x10\xc81\x122\n-TRIGGER_ATTRIBUTE_DIG_PATTERN_PAUSE_TRIG_WHEN\x10\xf0B\x124\n/TRIGGER_ATTRIBUTE_ANLG_EDGE_START_TRIG_COUPLING\x10\xb3D\x123\n.TRIGGER_ATTRIBUTE_ANLG_WIN_START_TRIG_COUPLING\x10\xb4D\x122\n-TRIGGER_ATTRIBUTE_ANLG_EDGE_REF_TRIG_COUPLING\x10\xb5D\x123\n.TRIGGER_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_COUPLING\x10\xb6D\x123\n.TRIGGER_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_COUPLING\x10\xb7D\x12%\n TRIGGER_ATTRIBUTE_HSHK_TRIG_TYPE\x10\xb7E\x129\n4TRIGGER_ATTRIBUTE_INTERLOCKED_HSHK_TRIG_ASSERTED_LVL\x10\xb9E\x12(\n#TRIGGER_ATTRIBUTE_TRIGGER_SYNC_TYPE\x10\x80_\x12+\n&TRIGGER_ATTRIBUTE_START_TRIG_TIMESCALE\x10\xb6`\x125\n0TRIGGER_ATTRIBUTE_START_TRIG_TIMESTAMP_TIMESCALE\x10\xadb\x123\n.TRIGGER_ATTRIBUTE_REF_TRIG_TIMESTAMP_TIMESCALE\x10\xb0b\x12/\n*TRIGGER_ATTRIBUTE_ARM_START_TRIG_TIMESCALE\x10\xb2b\x129\n4TRIGGER_ATTRIBUTE_ARM_START_TRIG_TIMESTAMP_TIMESCALE\x10\xb5b*\xaeD\n\x15TriggerResetAttribute\x12\'\n#TRIGGER_RESET_ATTRIBUTE_UNSPECIFIED\x10\x00\x123\n.TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_ADV_TRIG_EDGE\x10\xe0&\x122\n-TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_ADV_TRIG_SRC\x10\xe2&\x12*\n%TRIGGER_RESET_ATTRIBUTE_ADV_TRIG_TYPE\x10\xe5&\x12,\n\'TRIGGER_RESET_ATTRIBUTE_PAUSE_TRIG_TYPE\x10\xe6&\x125\n0TRIGGER_RESET_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_HYST\x10\xe8&\x124\n/TRIGGER_RESET_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_LVL\x10\xe9&\x124\n/TRIGGER_RESET_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_SRC\x10\xf0&\x125\n0TRIGGER_RESET_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_WHEN\x10\xf1&\x124\n/TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_SRC\x10\xf3&\x125\n0TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_WHEN\x10\xf4&\x124\n/TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_BTM\x10\xf5&\x124\n/TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_TOP\x10\xf6&\x123\n.TRIGGER_RESET_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_SRC\x10\xf9&\x124\n/TRIGGER_RESET_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_WHEN\x10\x80\'\x12,\n\'TRIGGER_RESET_ATTRIBUTE_START_TRIG_TYPE\x10\x93\'\x126\n1TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_START_TRIG_HYST\x10\x95\'\x125\n0TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_START_TRIG_LVL\x10\x96\'\x127\n2TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_START_TRIG_SLOPE\x10\x97\'\x125\n0TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_START_TRIG_SRC\x10\x98\'\x124\n/TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_START_TRIG_SRC\x10\x80(\x125\n0TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_START_TRIG_WHEN\x10\x81(\x124\n/TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_START_TRIG_BTM\x10\x82(\x124\n/TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_START_TRIG_TOP\x10\x83(\x125\n0TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_START_TRIG_EDGE\x10\x84(\x124\n/TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_START_TRIG_SRC\x10\x87(\x127\n2TRIGGER_RESET_ATTRIBUTE_DIG_PATTERN_START_TRIG_SRC\x10\x90(\x128\n3TRIGGER_RESET_ATTRIBUTE_DIG_PATTERN_START_TRIG_WHEN\x10\x91(\x120\n+TRIGGER_RESET_ATTRIBUTE_ARM_START_TRIG_TYPE\x10\x94(\x129\n4TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_EDGE\x10\x95(\x128\n3TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_SRC\x10\x97(\x12*\n%TRIGGER_RESET_ATTRIBUTE_REF_TRIG_TYPE\x10\x99(\x124\n/TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_REF_TRIG_HYST\x10\xa1(\x123\n.TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_REF_TRIG_LVL\x10\xa2(\x125\n0TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_REF_TRIG_SLOPE\x10\xa3(\x123\n.TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_REF_TRIG_SRC\x10\xa4(\x122\n-TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_REF_TRIG_SRC\x10\xa6(\x123\n.TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_REF_TRIG_WHEN\x10\xa7(\x122\n-TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_REF_TRIG_BTM\x10\xa8(\x122\n-TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_REF_TRIG_TOP\x10\xa9(\x123\n.TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_REF_TRIG_EDGE\x10\xb0(\x122\n-TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_REF_TRIG_SRC\x10\xb4(\x125\n0TRIGGER_RESET_ATTRIBUTE_DIG_PATTERN_REF_TRIG_SRC\x10\xb7(\x126\n1TRIGGER_RESET_ATTRIBUTE_DIG_PATTERN_REF_TRIG_WHEN\x10\xb8(\x125\n0TRIGGER_RESET_ATTRIBUTE_REF_TRIG_PRETRIG_SAMPLES\x10\xc5(\x12+\n&TRIGGER_RESET_ATTRIBUTE_REF_TRIG_DELAY\x10\x83)\x12-\n(TRIGGER_RESET_ATTRIBUTE_START_TRIG_DELAY\x10\xd60\x127\n2TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_REF_TRIG_COUPLING\x10\xd70\x123\n.TRIGGER_RESET_ATTRIBUTE_START_TRIG_DELAY_UNITS\x10\xc81\x125\n0TRIGGER_RESET_ATTRIBUTE_START_TRIG_RETRIGGERABLE\x10\x8f2\x127\n2TRIGGER_RESET_ATTRIBUTE_DIG_PATTERN_PAUSE_TRIG_SRC\x10\xefB\x128\n3TRIGGER_RESET_ATTRIBUTE_DIG_PATTERN_PAUSE_TRIG_WHEN\x10\xf0B\x12;\n6TRIGGER_RESET_ATTRIBUTE_DIG_PATTERN_START_TRIG_PATTERN\x10\x86C\x129\n4TRIGGER_RESET_ATTRIBUTE_DIG_PATTERN_REF_TRIG_PATTERN\x10\x87C\x12;\n6TRIGGER_RESET_ATTRIBUTE_DIG_PATTERN_PAUSE_TRIG_PATTERN\x10\x88C\x12@\n;TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_START_TRIG_DIG_FLTR_ENABLE\x10\xa3D\x12I\nDTRIGGER_RESET_ATTRIBUTE_DIG_EDGE_START_TRIG_DIG_FLTR_MIN_PULSE_WIDTH\x10\xa4D\x12F\nATRIGGER_RESET_ATTRIBUTE_DIG_EDGE_START_TRIG_DIG_FLTR_TIMEBASE_SRC\x10\xa5D\x12G\nBTRIGGER_RESET_ATTRIBUTE_DIG_EDGE_START_TRIG_DIG_FLTR_TIMEBASE_RATE\x10\xa6D\x12@\n;TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_START_TRIG_DIG_SYNC_ENABLE\x10\xa7D\x12?\n:TRIGGER_RESET_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_DIG_FLTR_ENABLE\x10\xa8D\x12H\nCTRIGGER_RESET_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_DIG_FLTR_MIN_PULSE_WIDTH\x10\xa9D\x12E\n@TRIGGER_RESET_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_DIG_FLTR_TIMEBASE_SRC\x10\xaaD\x12F\nATRIGGER_RESET_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_DIG_FLTR_TIMEBASE_RATE\x10\xabD\x12?\n:TRIGGER_RESET_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_DIG_SYNC_ENABLE\x10\xacD\x12D\n?TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_DIG_FLTR_ENABLE\x10\xadD\x12M\nHTRIGGER_RESET_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_DIG_FLTR_MIN_PULSE_WIDTH\x10\xaeD\x12J\nETRIGGER_RESET_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_DIG_FLTR_TIMEBASE_SRC\x10\xafD\x12K\nFTRIGGER_RESET_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_DIG_FLTR_TIMEBASE_RATE\x10\xb0D\x12D\n?TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_DIG_SYNC_ENABLE\x10\xb1D\x12:\n5TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_START_TRIG_COUPLING\x10\xb3D\x129\n4TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_START_TRIG_COUPLING\x10\xb4D\x128\n3TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_REF_TRIG_COUPLING\x10\xb5D\x129\n4TRIGGER_RESET_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_COUPLING\x10\xb6D\x129\n4TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_COUPLING\x10\xb7D\x12>\n9TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_ADV_TRIG_DIG_FLTR_ENABLE\x10\xb8D\x12+\n&TRIGGER_RESET_ATTRIBUTE_HSHK_TRIG_TYPE\x10\xb7E\x126\n1TRIGGER_RESET_ATTRIBUTE_INTERLOCKED_HSHK_TRIG_SRC\x10\xb8E\x12?\n:TRIGGER_RESET_ATTRIBUTE_INTERLOCKED_HSHK_TRIG_ASSERTED_LVL\x10\xb9E\x126\n1TRIGGER_RESET_ATTRIBUTE_REF_TRIG_AUTO_TRIG_ENABLE\x10\xc1]\x12>\n9TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_REF_TRIG_DIG_FLTR_ENABLE\x10\xd7]\x12G\nBTRIGGER_RESET_ATTRIBUTE_DIG_EDGE_REF_TRIG_DIG_FLTR_MIN_PULSE_WIDTH\x10\xd8]\x12D\n?TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_REF_TRIG_DIG_FLTR_TIMEBASE_SRC\x10\xd9]\x12E\n@TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_REF_TRIG_DIG_FLTR_TIMEBASE_RATE\x10\xda]\x12>\n9TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_REF_TRIG_DIG_SYNC_ENABLE\x10\xdb]\x12A\n<TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_START_TRIG_DIG_FLTR_ENABLE\x10\xe1]\x12J\nETRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_START_TRIG_DIG_FLTR_MIN_PULSE_WIDTH\x10\xe2]\x12G\nBTRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_START_TRIG_DIG_FLTR_TIMEBASE_SRC\x10\xe3]\x12H\nCTRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_START_TRIG_DIG_FLTR_TIMEBASE_RATE\x10\xe4]\x12A\n<TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_START_TRIG_DIG_SYNC_ENABLE\x10\xe5]\x12?\n:TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_REF_TRIG_DIG_FLTR_ENABLE\x10\xe6]\x12H\nCTRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_REF_TRIG_DIG_FLTR_MIN_PULSE_WIDTH\x10\xe7]\x12E\n@TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_REF_TRIG_DIG_FLTR_TIMEBASE_SRC\x10\xe8]\x12F\nATRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_REF_TRIG_DIG_FLTR_TIMEBASE_RATE\x10\xe9]\x12?\n:TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_REF_TRIG_DIG_SYNC_ENABLE\x10\xea]\x12>\n9TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_REF_TRIG_DIG_FLTR_ENABLE\x10\xeb]\x12G\nBTRIGGER_RESET_ATTRIBUTE_ANLG_WIN_REF_TRIG_DIG_FLTR_MIN_PULSE_WIDTH\x10\xec]\x12D\n?TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_REF_TRIG_DIG_FLTR_TIMEBASE_SRC\x10\xed]\x12E\n@TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_REF_TRIG_DIG_FLTR_TIMEBASE_RATE\x10\xee]\x12>\n9TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_REF_TRIG_DIG_SYNC_ENABLE\x10\xef]\x12@\n;TRIGGER_RESET_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_DIG_FLTR_ENABLE\x10\xf0]\x12I\nDTRIGGER_RESET_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_DIG_FLTR_MIN_PULSE_WIDTH\x10\xf1]\x12F\nATRIGGER_RESET_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_DIG_FLTR_TIMEBASE_SRC\x10\xf2]\x12G\nBTRIGGER_RESET_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_DIG_FLTR_TIMEBASE_RATE\x10\xf3]\x12@\n;TRIGGER_RESET_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_DIG_SYNC_ENABLE\x10\xf4]\x12@\n;TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_DIG_FLTR_ENABLE\x10\xf5]\x12I\nDTRIGGER_RESET_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_DIG_FLTR_MIN_PULSE_WIDTH\x10\xf6]\x12F\nATRIGGER_RESET_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_DIG_FLTR_TIMEBASE_SRC\x10\xf7]\x12G\nBTRIGGER_RESET_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_DIG_FLTR_TIMEBASE_RATE\x10\xf8]\x12@\n;TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_DIG_SYNC_ENABLE\x10\xf9]\x12@\n;TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_START_TRIG_DIG_FLTR_ENABLE\x10\xff]\x12I\nDTRIGGER_RESET_ATTRIBUTE_ANLG_WIN_START_TRIG_DIG_FLTR_MIN_PULSE_WIDTH\x10\x80^\x12F\nATRIGGER_RESET_ATTRIBUTE_ANLG_WIN_START_TRIG_DIG_FLTR_TIMEBASE_SRC\x10\x81^\x12G\nBTRIGGER_RESET_ATTRIBUTE_ANLG_WIN_START_TRIG_DIG_FLTR_TIMEBASE_RATE\x10\x82^\x12@\n;TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_START_TRIG_DIG_SYNC_ENABLE\x10\x83^\x12.\n)TRIGGER_RESET_ATTRIBUTE_TRIGGER_SYNC_TYPE\x10\x80_\x120\n+TRIGGER_RESET_ATTRIBUTE_TIME_START_TRIG_SRC\x10\x9d`\x121\n,TRIGGER_RESET_ATTRIBUTE_START_TRIG_TIMESCALE\x10\xb6`\x121\n,TRIGGER_RESET_ATTRIBUTE_START_TRIG_TRIG_WHEN\x10\xcd`\x120\n+TRIGGER_RESET_ATTRIBUTE_START_TRIG_TRIG_WIN\x10\x9ab\x125\n0TRIGGER_RESET_ATTRIBUTE_START_TRIG_RETRIGGER_WIN\x10\x9bb\x12?\n:TRIGGER_RESET_ATTRIBUTE_START_TRIG_MAX_NUM_TRIGS_TO_DETECT\x10\x9cb\x123\n.TRIGGER_RESET_ATTRIBUTE_REF_TRIG_RETRIGGERABLE\x10\x9db\x12.\n)TRIGGER_RESET_ATTRIBUTE_REF_TRIG_TRIG_WIN\x10\x9eb\x123\n.TRIGGER_RESET_ATTRIBUTE_REF_TRIG_RETRIGGER_WIN\x10\x9fb\x12=\n8TRIGGER_RESET_ATTRIBUTE_REF_TRIG_MAX_NUM_TRIGS_TO_DETECT\x10\xa0b\x12<\n7TRIGGER_RESET_ATTRIBUTE_ANLG_MULTI_EDGE_START_TRIG_SRCS\x10\xa1b\x12>\n9TRIGGER_RESET_ATTRIBUTE_ANLG_MULTI_EDGE_START_TRIG_SLOPES\x10\xa2b\x12<\n7TRIGGER_RESET_ATTRIBUTE_ANLG_MULTI_EDGE_START_TRIG_LVLS\x10\xa3b\x12=\n8TRIGGER_RESET_ATTRIBUTE_ANLG_MULTI_EDGE_START_TRIG_HYSTS\x10\xa4b\x12A\n<TRIGGER_RESET_ATTRIBUTE_ANLG_MULTI_EDGE_START_TRIG_COUPLINGS\x10\xa5b\x12:\n5TRIGGER_RESET_ATTRIBUTE_ANLG_MULTI_EDGE_REF_TRIG_SRCS\x10\xa6b\x12<\n7TRIGGER_RESET_ATTRIBUTE_ANLG_MULTI_EDGE_REF_TRIG_SLOPES\x10\xa7b\x12:\n5TRIGGER_RESET_ATTRIBUTE_ANLG_MULTI_EDGE_REF_TRIG_LVLS\x10\xa8b\x12;\n6TRIGGER_RESET_ATTRIBUTE_ANLG_MULTI_EDGE_REF_TRIG_HYSTS\x10\xa9b\x12?\n:TRIGGER_RESET_ATTRIBUTE_ANLG_MULTI_EDGE_REF_TRIG_COUPLINGS\x10\xaab\x12;\n6TRIGGER_RESET_ATTRIBUTE_START_TRIG_TIMESTAMP_TIMESCALE\x10\xadb\x126\n1TRIGGER_RESET_ATTRIBUTE_REF_TRIG_TIMESTAMP_ENABLE\x10\xaeb\x129\n4TRIGGER_RESET_ATTRIBUTE_REF_TRIG_TIMESTAMP_TIMESCALE\x10\xb0b\x125\n0TRIGGER_RESET_ATTRIBUTE_ARM_START_TRIG_TRIG_WHEN\x10\xb1b\x125\n0TRIGGER_RESET_ATTRIBUTE_ARM_START_TRIG_TIMESCALE\x10\xb2b\x12<\n7TRIGGER_RESET_ATTRIBUTE_ARM_START_TRIG_TIMESTAMP_ENABLE\x10\xb3b\x12?\n:TRIGGER_RESET_ATTRIBUTE_ARM_START_TRIG_TIMESTAMP_TIMESCALE\x10\xb5b\x128\n3TRIGGER_RESET_ATTRIBUTE_START_TRIG_TIMESTAMP_ENABLE\x10\xcab*\x85\x0f\n\x16TriggerStringAttribute\x12(\n$TRIGGER_STRING_ATTRIBUTE_UNSPECIFIED\x10\x00\x12,\n\'TRIGGER_ATTRIBUTE_DIG_EDGE_ADV_TRIG_SRC\x10\xe2&\x12.\n)TRIGGER_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_SRC\x10\xf0&\x12.\n)TRIGGER_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_SRC\x10\xf3&\x12-\n(TRIGGER_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_SRC\x10\xf9&\x12/\n*TRIGGER_ATTRIBUTE_ANLG_EDGE_START_TRIG_SRC\x10\x98\'\x12.\n)TRIGGER_ATTRIBUTE_ANLG_WIN_START_TRIG_SRC\x10\x80(\x12.\n)TRIGGER_ATTRIBUTE_DIG_EDGE_START_TRIG_SRC\x10\x87(\x121\n,TRIGGER_ATTRIBUTE_DIG_PATTERN_START_TRIG_SRC\x10\x90(\x122\n-TRIGGER_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_SRC\x10\x97(\x12-\n(TRIGGER_ATTRIBUTE_ANLG_EDGE_REF_TRIG_SRC\x10\xa4(\x12,\n\'TRIGGER_ATTRIBUTE_ANLG_WIN_REF_TRIG_SRC\x10\xa6(\x12,\n\'TRIGGER_ATTRIBUTE_DIG_EDGE_REF_TRIG_SRC\x10\xb4(\x12/\n*TRIGGER_ATTRIBUTE_DIG_PATTERN_REF_TRIG_SRC\x10\xb7(\x121\n,TRIGGER_ATTRIBUTE_DIG_PATTERN_PAUSE_TRIG_SRC\x10\xefB\x125\n0TRIGGER_ATTRIBUTE_DIG_PATTERN_START_TRIG_PATTERN\x10\x86C\x123\n.TRIGGER_ATTRIBUTE_DIG_PATTERN_REF_TRIG_PATTERN\x10\x87C\x125\n0TRIGGER_ATTRIBUTE_DIG_PATTERN_PAUSE_TRIG_PATTERN\x10\x88C\x12@\n;TRIGGER_ATTRIBUTE_DIG_EDGE_START_TRIG_DIG_FLTR_TIMEBASE_SRC\x10\xa5D\x12?\n:TRIGGER_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_DIG_FLTR_TIMEBASE_SRC\x10\xaaD\x12D\n?TRIGGER_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_DIG_FLTR_TIMEBASE_SRC\x10\xafD\x120\n+TRIGGER_ATTRIBUTE_INTERLOCKED_HSHK_TRIG_SRC\x10\xb8E\x12>\n9TRIGGER_ATTRIBUTE_DIG_EDGE_REF_TRIG_DIG_FLTR_TIMEBASE_SRC\x10\xd9]\x12A\n<TRIGGER_ATTRIBUTE_ANLG_EDGE_START_TRIG_DIG_FLTR_TIMEBASE_SRC\x10\xe3]\x12?\n:TRIGGER_ATTRIBUTE_ANLG_EDGE_REF_TRIG_DIG_FLTR_TIMEBASE_SRC\x10\xe8]\x12>\n9TRIGGER_ATTRIBUTE_ANLG_WIN_REF_TRIG_DIG_FLTR_TIMEBASE_SRC\x10\xed]\x12@\n;TRIGGER_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_DIG_FLTR_TIMEBASE_SRC\x10\xf2]\x12@\n;TRIGGER_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_DIG_FLTR_TIMEBASE_SRC\x10\xf7]\x12@\n;TRIGGER_ATTRIBUTE_ANLG_WIN_START_TRIG_DIG_FLTR_TIMEBASE_SRC\x10\x81^\x12&\n!TRIGGER_ATTRIBUTE_START_TRIG_TERM\x10\x9e^\x12$\n\x1fTRIGGER_ATTRIBUTE_REF_TRIG_TERM\x10\x9f^\x12&\n!TRIGGER_ATTRIBUTE_PAUSE_TRIG_TERM\x10\xa0^\x12%\n TRIGGER_ATTRIBUTE_ARM_START_TERM\x10\xff^\x12*\n%TRIGGER_ATTRIBUTE_TIME_START_TRIG_SRC\x10\x9d`\x126\n1TRIGGER_ATTRIBUTE_ANLG_MULTI_EDGE_START_TRIG_SRCS\x10\xa1b\x124\n/TRIGGER_ATTRIBUTE_ANLG_MULTI_EDGE_REF_TRIG_SRCS\x10\xa6b*\xd5\x11\n\x16TriggerDoubleAttribute\x12(\n$TRIGGER_DOUBLE_ATTRIBUTE_UNSPECIFIED\x10\x00\x12/\n*TRIGGER_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_HYST\x10\xe8&\x12.\n)TRIGGER_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_LVL\x10\xe9&\x12.\n)TRIGGER_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_BTM\x10\xf5&\x12.\n)TRIGGER_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_TOP\x10\xf6&\x120\n+TRIGGER_ATTRIBUTE_ANLG_EDGE_START_TRIG_HYST\x10\x95\'\x12/\n*TRIGGER_ATTRIBUTE_ANLG_EDGE_START_TRIG_LVL\x10\x96\'\x12.\n)TRIGGER_ATTRIBUTE_ANLG_WIN_START_TRIG_BTM\x10\x82(\x12.\n)TRIGGER_ATTRIBUTE_ANLG_WIN_START_TRIG_TOP\x10\x83(\x12.\n)TRIGGER_ATTRIBUTE_ANLG_EDGE_REF_TRIG_HYST\x10\xa1(\x12-\n(TRIGGER_ATTRIBUTE_ANLG_EDGE_REF_TRIG_LVL\x10\xa2(\x12,\n\'TRIGGER_ATTRIBUTE_ANLG_WIN_REF_TRIG_BTM\x10\xa8(\x12,\n\'TRIGGER_ATTRIBUTE_ANLG_WIN_REF_TRIG_TOP\x10\xa9(\x12%\n TRIGGER_ATTRIBUTE_REF_TRIG_DELAY\x10\x83)\x12\'\n"TRIGGER_ATTRIBUTE_START_TRIG_DELAY\x10\xd60\x12C\n>TRIGGER_ATTRIBUTE_DIG_EDGE_START_TRIG_DIG_FLTR_MIN_PULSE_WIDTH\x10\xa4D\x12A\n<TRIGGER_ATTRIBUTE_DIG_EDGE_START_TRIG_DIG_FLTR_TIMEBASE_RATE\x10\xa6D\x12B\n=TRIGGER_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_DIG_FLTR_MIN_PULSE_WIDTH\x10\xa9D\x12@\n;TRIGGER_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_DIG_FLTR_TIMEBASE_RATE\x10\xabD\x12G\nBTRIGGER_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_DIG_FLTR_MIN_PULSE_WIDTH\x10\xaeD\x12E\n@TRIGGER_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_DIG_FLTR_TIMEBASE_RATE\x10\xb0D\x12A\n<TRIGGER_ATTRIBUTE_DIG_EDGE_REF_TRIG_DIG_FLTR_MIN_PULSE_WIDTH\x10\xd8]\x12?\n:TRIGGER_ATTRIBUTE_DIG_EDGE_REF_TRIG_DIG_FLTR_TIMEBASE_RATE\x10\xda]\x12D\n?TRIGGER_ATTRIBUTE_ANLG_EDGE_START_TRIG_DIG_FLTR_MIN_PULSE_WIDTH\x10\xe2]\x12B\n=TRIGGER_ATTRIBUTE_ANLG_EDGE_START_TRIG_DIG_FLTR_TIMEBASE_RATE\x10\xe4]\x12B\n=TRIGGER_ATTRIBUTE_ANLG_EDGE_REF_TRIG_DIG_FLTR_MIN_PULSE_WIDTH\x10\xe7]\x12@\n;TRIGGER_ATTRIBUTE_ANLG_EDGE_REF_TRIG_DIG_FLTR_TIMEBASE_RATE\x10\xe9]\x12A\n<TRIGGER_ATTRIBUTE_ANLG_WIN_REF_TRIG_DIG_FLTR_MIN_PULSE_WIDTH\x10\xec]\x12?\n:TRIGGER_ATTRIBUTE_ANLG_WIN_REF_TRIG_DIG_FLTR_TIMEBASE_RATE\x10\xee]\x12C\n>TRIGGER_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_DIG_FLTR_MIN_PULSE_WIDTH\x10\xf1]\x12A\n<TRIGGER_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_DIG_FLTR_TIMEBASE_RATE\x10\xf3]\x12C\n>TRIGGER_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_DIG_FLTR_MIN_PULSE_WIDTH\x10\xf6]\x12A\n<TRIGGER_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_DIG_FLTR_TIMEBASE_RATE\x10\xf8]\x12C\n>TRIGGER_ATTRIBUTE_ANLG_WIN_START_TRIG_DIG_FLTR_MIN_PULSE_WIDTH\x10\x80^\x12A\n<TRIGGER_ATTRIBUTE_ANLG_WIN_START_TRIG_DIG_FLTR_TIMEBASE_RATE\x10\x82^\x12*\n%TRIGGER_ATTRIBUTE_START_TRIG_TRIG_WIN\x10\x9ab\x12/\n*TRIGGER_ATTRIBUTE_START_TRIG_RETRIGGER_WIN\x10\x9bb\x12(\n#TRIGGER_ATTRIBUTE_REF_TRIG_TRIG_WIN\x10\x9eb\x12-\n(TRIGGER_ATTRIBUTE_REF_TRIG_RETRIGGER_WIN\x10\x9fb*\xe7\x01\n\x16TriggerUInt32Attribute\x12(\n$TRIGGER_UINT32_ATTRIBUTE_UNSPECIFIED\x10\x00\x12/\n*TRIGGER_ATTRIBUTE_REF_TRIG_PRETRIG_SAMPLES\x10\xc5(\x129\n4TRIGGER_ATTRIBUTE_START_TRIG_MAX_NUM_TRIGS_TO_DETECT\x10\x9cb\x127\n2TRIGGER_ATTRIBUTE_REF_TRIG_MAX_NUM_TRIGS_TO_DETECT\x10\xa0b*\x86\r\n\x14TriggerBoolAttribute\x12&\n"TRIGGER_BOOL_ATTRIBUTE_UNSPECIFIED\x10\x00\x12/\n*TRIGGER_ATTRIBUTE_START_TRIG_RETRIGGERABLE\x10\x8f2\x12:\n5TRIGGER_ATTRIBUTE_DIG_EDGE_START_TRIG_DIG_FLTR_ENABLE\x10\xa3D\x12:\n5TRIGGER_ATTRIBUTE_DIG_EDGE_START_TRIG_DIG_SYNC_ENABLE\x10\xa7D\x129\n4TRIGGER_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_DIG_FLTR_ENABLE\x10\xa8D\x129\n4TRIGGER_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_DIG_SYNC_ENABLE\x10\xacD\x12>\n9TRIGGER_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_DIG_FLTR_ENABLE\x10\xadD\x12>\n9TRIGGER_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_DIG_SYNC_ENABLE\x10\xb1D\x128\n3TRIGGER_ATTRIBUTE_DIG_EDGE_ADV_TRIG_DIG_FLTR_ENABLE\x10\xb8D\x120\n+TRIGGER_ATTRIBUTE_REF_TRIG_AUTO_TRIG_ENABLE\x10\xc1]\x12.\n)TRIGGER_ATTRIBUTE_REF_TRIG_AUTO_TRIGGERED\x10\xc2]\x128\n3TRIGGER_ATTRIBUTE_DIG_EDGE_REF_TRIG_DIG_FLTR_ENABLE\x10\xd7]\x128\n3TRIGGER_ATTRIBUTE_DIG_EDGE_REF_TRIG_DIG_SYNC_ENABLE\x10\xdb]\x12;\n6TRIGGER_ATTRIBUTE_ANLG_EDGE_START_TRIG_DIG_FLTR_ENABLE\x10\xe1]\x12;\n6TRIGGER_ATTRIBUTE_ANLG_EDGE_START_TRIG_DIG_SYNC_ENABLE\x10\xe5]\x129\n4TRIGGER_ATTRIBUTE_ANLG_EDGE_REF_TRIG_DIG_FLTR_ENABLE\x10\xe6]\x129\n4TRIGGER_ATTRIBUTE_ANLG_EDGE_REF_TRIG_DIG_SYNC_ENABLE\x10\xea]\x128\n3TRIGGER_ATTRIBUTE_ANLG_WIN_REF_TRIG_DIG_FLTR_ENABLE\x10\xeb]\x128\n3TRIGGER_ATTRIBUTE_ANLG_WIN_REF_TRIG_DIG_SYNC_ENABLE\x10\xef]\x12:\n5TRIGGER_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_DIG_FLTR_ENABLE\x10\xf0]\x12:\n5TRIGGER_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_DIG_SYNC_ENABLE\x10\xf4]\x12:\n5TRIGGER_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_DIG_FLTR_ENABLE\x10\xf5]\x12:\n5TRIGGER_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_DIG_SYNC_ENABLE\x10\xf9]\x12:\n5TRIGGER_ATTRIBUTE_ANLG_WIN_START_TRIG_DIG_FLTR_ENABLE\x10\xff]\x12:\n5TRIGGER_ATTRIBUTE_ANLG_WIN_START_TRIG_DIG_SYNC_ENABLE\x10\x83^\x12-\n(TRIGGER_ATTRIBUTE_REF_TRIG_RETRIGGERABLE\x10\x9db\x120\n+TRIGGER_ATTRIBUTE_REF_TRIG_TIMESTAMP_ENABLE\x10\xaeb\x126\n1TRIGGER_ATTRIBUTE_ARM_START_TRIG_TIMESTAMP_ENABLE\x10\xb3b\x122\n-TRIGGER_ATTRIBUTE_START_TRIG_TIMESTAMP_ENABLE\x10\xcab*\xbb\x02\n\x19TriggerTimestampAttribute\x12+\n\'TRIGGER_TIMESTAMP_ATTRIBUTE_UNSPECIFIED\x10\x00\x12+\n&TRIGGER_ATTRIBUTE_START_TRIG_TRIG_WHEN\x10\xcd`\x12-\n(TRIGGER_ATTRIBUTE_REF_TRIG_TIMESTAMP_VAL\x10\xafb\x12/\n*TRIGGER_ATTRIBUTE_ARM_START_TRIG_TRIG_WHEN\x10\xb1b\x123\n.TRIGGER_ATTRIBUTE_ARM_START_TRIG_TIMESTAMP_VAL\x10\xb4b\x12/\n*TRIGGER_ATTRIBUTE_START_TRIG_TIMESTAMP_VAL\x10\xcbb*\xb5\x02\n\x1aTriggerInt32ArrayAttribute\x12-\n)TRIGGER_INT32_ARRAY_ATTRIBUTE_UNSPECIFIED\x10\x00\x128\n3TRIGGER_ATTRIBUTE_ANLG_MULTI_EDGE_START_TRIG_SLOPES\x10\xa2b\x12;\n6TRIGGER_ATTRIBUTE_ANLG_MULTI_EDGE_START_TRIG_COUPLINGS\x10\xa5b\x126\n1TRIGGER_ATTRIBUTE_ANLG_MULTI_EDGE_REF_TRIG_SLOPES\x10\xa7b\x129\n4TRIGGER_ATTRIBUTE_ANLG_MULTI_EDGE_REF_TRIG_COUPLINGS\x10\xaab*\xab\x02\n\x1bTriggerDoubleArrayAttribute\x12.\n*TRIGGER_DOUBLE_ARRAY_ATTRIBUTE_UNSPECIFIED\x10\x00\x126\n1TRIGGER_ATTRIBUTE_ANLG_MULTI_EDGE_START_TRIG_LVLS\x10\xa3b\x127\n2TRIGGER_ATTRIBUTE_ANLG_MULTI_EDGE_START_TRIG_HYSTS\x10\xa4b\x124\n/TRIGGER_ATTRIBUTE_ANLG_MULTI_EDGE_REF_TRIG_LVLS\x10\xa8b\x125\n0TRIGGER_ATTRIBUTE_ANLG_MULTI_EDGE_REF_TRIG_HYSTS\x10\xa9b*\x9e\x02\n\x16WatchdogInt32Attribute\x12(\n$WATCHDOG_INT32_ATTRIBUTE_UNSPECIFIED\x10\x00\x12\'\n"WATCHDOG_ATTRIBUTE_EXPIR_TRIG_TYPE\x10\xa3C\x129\n4WATCHDOG_ATTRIBUTE_DIG_EDGE_WATCHDOG_EXPIR_TRIG_EDGE\x10\xa5C\x12&\n!WATCHDOG_ATTRIBUTE_DO_EXPIR_STATE\x10\xa7C\x12&\n!WATCHDOG_ATTRIBUTE_AO_OUTPUT_TYPE\x10\xde`\x12&\n!WATCHDOG_ATTRIBUTE_CO_EXPIR_STATE\x10\xe0`*\x95\x04\n\x16WatchdogResetAttribute\x12(\n$WATCHDOG_RESET_ATTRIBUTE_UNSPECIFIED\x10\x00\x12-\n(WATCHDOG_RESET_ATTRIBUTE_EXPIR_TRIG_TYPE\x10\xa3C\x12>\n9WATCHDOG_RESET_ATTRIBUTE_DIG_EDGE_WATCHDOG_EXPIR_TRIG_SRC\x10\xa4C\x12?\n:WATCHDOG_RESET_ATTRIBUTE_DIG_EDGE_WATCHDOG_EXPIR_TRIG_EDGE\x10\xa5C\x12,\n\'WATCHDOG_RESET_ATTRIBUTE_DO_EXPIR_STATE\x10\xa7C\x12%\n WATCHDOG_RESET_ATTRIBUTE_TIMEOUT\x10\xa9C\x12B\n=WATCHDOG_RESET_ATTRIBUTE_EXPIR_TRIG_TRIG_ON_NETWORK_CONN_LOSS\x10\xdd`\x12,\n\'WATCHDOG_RESET_ATTRIBUTE_AO_OUTPUT_TYPE\x10\xde`\x12,\n\'WATCHDOG_RESET_ATTRIBUTE_AO_EXPIR_STATE\x10\xdf`\x12,\n\'WATCHDOG_RESET_ATTRIBUTE_CO_EXPIR_STATE\x10\xe0`*~\n\x17WatchdogStringAttribute\x12)\n%WATCHDOG_STRING_ATTRIBUTE_UNSPECIFIED\x10\x00\x128\n3WATCHDOG_ATTRIBUTE_DIG_EDGE_WATCHDOG_EXPIR_TRIG_SRC\x10\xa4C*\xa3\x01\n\x15WatchdogBoolAttribute\x12\'\n#WATCHDOG_BOOL_ATTRIBUTE_UNSPECIFIED\x10\x00\x12#\n\x1eWATCHDOG_ATTRIBUTE_HAS_EXPIRED\x10\xa8C\x12<\n7WATCHDOG_ATTRIBUTE_EXPIR_TRIG_TRIG_ON_NETWORK_CONN_LOSS\x10\xdd`*\x8d\x01\n\x17WatchdogDoubleAttribute\x12)\n%WATCHDOG_DOUBLE_ATTRIBUTE_UNSPECIFIED\x10\x00\x12\x1f\n\x1aWATCHDOG_ATTRIBUTE_TIMEOUT\x10\xa9C\x12&\n!WATCHDOG_ATTRIBUTE_AO_EXPIR_STATE\x10\xdf`*\xbc\x01\n\x13WriteInt32Attribute\x12%\n!WRITE_INT32_ATTRIBUTE_UNSPECIFIED\x10\x00\x12\x1f\n\x1aWRITE_ATTRIBUTE_REGEN_MODE\x10\xd3(\x12 \n\x1bWRITE_ATTRIBUTE_RELATIVE_TO\x10\x8c2\x12\x1b\n\x16WRITE_ATTRIBUTE_OFFSET\x10\x8d2\x12\x1e\n\x19WRITE_ATTRIBUTE_WAIT_MODE\x10\xb1E*\xaa\x02\n\x13WriteResetAttribute\x12%\n!WRITE_RESET_ATTRIBUTE_UNSPECIFIED\x10\x00\x12%\n WRITE_RESET_ATTRIBUTE_REGEN_MODE\x10\xd3(\x12&\n!WRITE_RESET_ATTRIBUTE_RELATIVE_TO\x10\x8c2\x12!\n\x1cWRITE_RESET_ATTRIBUTE_OFFSET\x10\x8d2\x12$\n\x1fWRITE_RESET_ATTRIBUTE_WAIT_MODE\x10\xb1E\x12%\n WRITE_RESET_ATTRIBUTE_SLEEP_TIME\x10\xb2E\x12-\n(WRITE_RESET_ATTRIBUTE_NEXT_WRITE_IS_LAST\x10\xecR*\x97\x01\n\x14WriteUInt64Attribute\x12&\n"WRITE_UINT64_ATTRIBUTE_UNSPECIFIED\x10\x00\x12#\n\x1eWRITE_ATTRIBUTE_CURR_WRITE_POS\x10\xd8(\x122\n-WRITE_ATTRIBUTE_TOTAL_SAMP_PER_CHAN_GENERATED\x10\xab2*\xd8\x01\n\x14WriteUInt32Attribute\x12&\n"WRITE_UINT32_ATTRIBUTE_UNSPECIFIED\x10\x00\x12 \n\x1bWRITE_ATTRIBUTE_SPACE_AVAIL\x10\xe0(\x12#\n\x1eWRITE_ATTRIBUTE_RAW_DATA_WIDTH\x10\xfdB\x12\x1e\n\x19WRITE_ATTRIBUTE_NUM_CHANS\x10\xfeB\x121\n,WRITE_ATTRIBUTE_DIGITAL_LINES_BYTES_PER_CHAN\x10\xffB*_\n\x14WriteDoubleAttribute\x12&\n"WRITE_DOUBLE_ATTRIBUTE_UNSPECIFIED\x10\x00\x12\x1f\n\x1aWRITE_ATTRIBUTE_SLEEP_TIME\x10\xb2E*\xfe\x03\n\x12WriteBoolAttribute\x12$\n WRITE_BOOL_ATTRIBUTE_UNSPECIFIED\x10\x00\x12\'\n"WRITE_ATTRIBUTE_NEXT_WRITE_IS_LAST\x10\xecR\x12,\n\'WRITE_ATTRIBUTE_OVERCURRENT_CHANS_EXIST\x10\xe8S\x122\n-WRITE_ATTRIBUTE_OPEN_CURRENT_LOOP_CHANS_EXIST\x10\xeaS\x123\n.WRITE_ATTRIBUTE_POWER_SUPPLY_FAULT_CHANS_EXIST\x10\xecS\x120\n+WRITE_ATTRIBUTE_OVERTEMPERATURE_CHANS_EXIST\x10\x84U\x12<\n7WRITE_ATTRIBUTE_ACCESSORY_INSERTION_OR_REMOVAL_DETECTED\x10\xd3`\x12+\n&WRITE_ATTRIBUTE_OVERLOADED_CHANS_EXIST\x10\x84a\x125\n0WRITE_ATTRIBUTE_EXTERNAL_OVERVOLTAGE_CHANS_EXIST\x10\xbba\x12.\n)WRITE_ATTRIBUTE_SYNC_UNLOCKED_CHANS_EXIST\x10\xbfb*\xb1\x03\n\x14WriteStringAttribute\x12&\n"WRITE_STRING_ATTRIBUTE_UNSPECIFIED\x10\x00\x12&\n!WRITE_ATTRIBUTE_OVERCURRENT_CHANS\x10\xe9S\x12,\n\'WRITE_ATTRIBUTE_OPEN_CURRENT_LOOP_CHANS\x10\xebS\x12-\n(WRITE_ATTRIBUTE_POWER_SUPPLY_FAULT_CHANS\x10\xedS\x12>\n9WRITE_ATTRIBUTE_DEVS_WITH_INSERTED_OR_REMOVED_ACCESSORIES\x10\xd4`\x12*\n%WRITE_ATTRIBUTE_OVERTEMPERATURE_CHANS\x10\x83a\x12%\n WRITE_ATTRIBUTE_OVERLOADED_CHANS\x10\x85a\x12/\n*WRITE_ATTRIBUTE_EXTERNAL_OVERVOLTAGE_CHANS\x10\xbca\x12(\n#WRITE_ATTRIBUTE_SYNC_UNLOCKED_CHANS\x10\xc0b*\x92\x01\n\x0fACExcitWireMode\x12"\n\x1eAC_EXCIT_WIRE_MODE_UNSPECIFIED\x10\x00\x12\x1d\n\x19AC_EXCIT_WIRE_MODE_4_WIRE\x10\x04\x12\x1d\n\x19AC_EXCIT_WIRE_MODE_5_WIRE\x10\x05\x12\x1d\n\x19AC_EXCIT_WIRE_MODE_6_WIRE\x10\x06*\xa8\x02\n\x1bAccelChargeSensitivityUnits\x12.\n*ACCEL_CHARGE_SENSITIVITY_UNITS_UNSPECIFIED\x10\x00\x127\n2ACCEL_CHARGE_SENSITIVITY_UNITS_PICO_COULOMBS_PER_G\x10\xe3}\x12O\nJACCEL_CHARGE_SENSITIVITY_UNITS_PICO_COULOMBS_PER_METERS_PER_SECOND_SQUARED\x10\xe4}\x12O\nJACCEL_CHARGE_SENSITIVITY_UNITS_PICO_COULOMBS_PER_INCHES_PER_SECOND_SQUARED\x10\xe5}*\x9a\x01\n\x16AccelSensitivityUnits1\x12(\n$ACCEL_SENSITIVITY_UNITS1_UNSPECIFIED\x10\x00\x12+\n&ACCEL_SENSITIVITY_UNITS1_M_VOLTS_PER_G\x10\xdda\x12)\n$ACCEL_SENSITIVITY_UNITS1_VOLTS_PER_G\x10\xdea*\xca\x01\n\x0bAccelUnits2\x12\x1c\n\x18ACCEL_UNITS2_UNSPECIFIED\x10\x00\x12\x1e\n\x19ACCEL_UNITS2_ACCEL_UNIT_G\x10\xcaO\x12+\n&ACCEL_UNITS2_METERS_PER_SECOND_SQUARED\x10\xb6a\x12+\n&ACCEL_UNITS2_INCHES_PER_SECOND_SQUARED\x10\xb7a\x12#\n\x1eACCEL_UNITS2_FROM_CUSTOM_SCALE\x10\xd1N*\xa6\x01\n\x0fAcquisitionType\x12 \n\x1cACQUISITION_TYPE_UNSPECIFIED\x10\x00\x12"\n\x1dACQUISITION_TYPE_FINITE_SAMPS\x10\xc2O\x12 \n\x1bACQUISITION_TYPE_CONT_SAMPS\x10\x8bO\x12+\n&ACQUISITION_TYPE_HW_TIMED_SINGLE_POINT\x10\xeaa*\x86\x01\n\x0bAngleUnits1\x12\x1c\n\x18ANGLE_UNITS1_UNSPECIFIED\x10\x00\x12\x19\n\x14ANGLE_UNITS1_DEGREES\x10\xa2O\x12\x19\n\x14ANGLE_UNITS1_RADIANS\x10\xa1P\x12#\n\x1eANGLE_UNITS1_FROM_CUSTOM_SCALE\x10\xd1N*\x9f\x01\n\x0bAngleUnits2\x12\x1c\n\x18ANGLE_UNITS2_UNSPECIFIED\x10\x00\x12\x19\n\x14ANGLE_UNITS2_DEGREES\x10\xa2O\x12\x19\n\x14ANGLE_UNITS2_RADIANS\x10\xa1P\x12\x17\n\x12ANGLE_UNITS2_TICKS\x10\xc0P\x12#\n\x1eANGLE_UNITS2_FROM_CUSTOM_SCALE\x10\xd1N*\xee\x01\n\x14AngularVelocityUnits\x12&\n"ANGULAR_VELOCITY_UNITS_UNSPECIFIED\x10\x00\x12\x1f\n\x1aANGULAR_VELOCITY_UNITS_RPM\x10\xd0}\x12.\n)ANGULAR_VELOCITY_UNITS_RADIANS_PER_SECOND\x10\xd1}\x12.\n)ANGULAR_VELOCITY_UNITS_DEGREES_PER_SECOND\x10\xd2}\x12-\n(ANGULAR_VELOCITY_UNITS_FROM_CUSTOM_SCALE\x10\xd1N*\xde\x01\n\x14BridgeConfiguration1\x12%\n!BRIDGE_CONFIGURATION1_UNSPECIFIED\x10\x00\x12&\n!BRIDGE_CONFIGURATION1_FULL_BRIDGE\x10\xc6O\x12&\n!BRIDGE_CONFIGURATION1_HALF_BRIDGE\x10\xcbO\x12)\n$BRIDGE_CONFIGURATION1_QUARTER_BRIDGE\x10\x9eP\x12$\n\x1fBRIDGE_CONFIGURATION1_NO_BRIDGE\x10\xf4O*\x9c\x01\n\x15BridgeElectricalUnits\x12\'\n#BRIDGE_ELECTRICAL_UNITS_UNSPECIFIED\x10\x00\x12+\n&BRIDGE_ELECTRICAL_UNITS_VOLTS_PER_VOLT\x10\x98|\x12-\n(BRIDGE_ELECTRICAL_UNITS_M_VOLTS_PER_VOLT\x10\x99|*\xc7\x03\n\x13BridgePhysicalUnits\x12%\n!BRIDGE_PHYSICAL_UNITS_UNSPECIFIED\x10\x00\x12"\n\x1dBRIDGE_PHYSICAL_UNITS_NEWTONS\x10\x83|\x12!\n\x1cBRIDGE_PHYSICAL_UNITS_POUNDS\x10\x84|\x12)\n$BRIDGE_PHYSICAL_UNITS_KILOGRAM_FORCE\x10\x85|\x12"\n\x1dBRIDGE_PHYSICAL_UNITS_PASCALS\x10\xe1N\x121\n,BRIDGE_PHYSICAL_UNITS_POUNDS_PER_SQUARE_INCH\x10\x87|\x12\x1e\n\x19BRIDGE_PHYSICAL_UNITS_BAR\x10\x88|\x12(\n#BRIDGE_PHYSICAL_UNITS_NEWTON_METERS\x10\x89|\x12&\n!BRIDGE_PHYSICAL_UNITS_INCH_OUNCES\x10\x8a|\x12&\n!BRIDGE_PHYSICAL_UNITS_INCH_POUNDS\x10\x8b|\x12&\n!BRIDGE_PHYSICAL_UNITS_FOOT_POUNDS\x10\x8c|*\xb3\x01\n\x0bBridgeUnits\x12\x1c\n\x18BRIDGE_UNITS_UNSPECIFIED\x10\x00\x12 \n\x1bBRIDGE_UNITS_VOLTS_PER_VOLT\x10\x98|\x12"\n\x1dBRIDGE_UNITS_M_VOLTS_PER_VOLT\x10\x99|\x12#\n\x1eBRIDGE_UNITS_FROM_CUSTOM_SCALE\x10\xd1N\x12\x1b\n\x16BRIDGE_UNITS_FROM_TEDS\x10\xe4a*w\n\nCJCSource1\x12\x1b\n\x17CJC_SOURCE1_UNSPECIFIED\x10\x00\x12\x19\n\x14CJC_SOURCE1_BUILT_IN\x10\xd8O\x12\x1a\n\x15CJC_SOURCE1_CONST_VAL\x10\x84O\x12\x15\n\x10CJC_SOURCE1_CHAN\x10\x81O*\x8d\x01\n\x0bChargeUnits\x12\x1c\n\x18CHARGE_UNITS_UNSPECIFIED\x10\x00\x12\x1a\n\x15CHARGE_UNITS_COULOMBS\x10\xe6}\x12\x1f\n\x1aCHARGE_UNITS_PICO_COULOMBS\x10\xe7}\x12#\n\x1eCHARGE_UNITS_FROM_CUSTOM_SCALE\x10\xd1N*\x9b\x01\n\x0fCountDirection1\x12 \n\x1cCOUNT_DIRECTION1_UNSPECIFIED\x10\x00\x12\x1e\n\x19COUNT_DIRECTION1_COUNT_UP\x10\x90O\x12 \n\x1bCOUNT_DIRECTION1_COUNT_DOWN\x10\x8cO\x12$\n\x1fCOUNT_DIRECTION1_EXT_CONTROLLED\x10\xd6P*\xf5\x01\n\x16CounterFrequencyMethod\x12(\n$COUNTER_FREQUENCY_METHOD_UNSPECIFIED\x10\x00\x12,\n\'COUNTER_FREQUENCY_METHOD_LOW_FREQ_1_CTR\x10\xf9N\x12-\n(COUNTER_FREQUENCY_METHOD_HIGH_FREQ_2_CTR\x10\xadO\x12-\n(COUNTER_FREQUENCY_METHOD_LARGE_RNG_2_CTR\x10\xddO\x12%\n COUNTER_FREQUENCY_METHOD_DYN_AVG\x10\xc1}*\xa2\x02\n\'CurrentShuntResistorLocationWithDefault\x12<\n8CURRENT_SHUNT_RESISTOR_LOCATION_WITH_DEFAULT_UNSPECIFIED\x10\x00\x12A\n4CURRENT_SHUNT_RESISTOR_LOCATION_WITH_DEFAULT_DEFAULT\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12:\n5CURRENT_SHUNT_RESISTOR_LOCATION_WITH_DEFAULT_INTERNAL\x10\xd8O\x12:\n5CURRENT_SHUNT_RESISTOR_LOCATION_WITH_DEFAULT_EXTERNAL\x10\xb7O*p\n\rCurrentUnits2\x12\x1e\n\x1aCURRENT_UNITS2_UNSPECIFIED\x10\x00\x12\x18\n\x13CURRENT_UNITS2_AMPS\x10\xe6P\x12%\n CURRENT_UNITS2_FROM_CUSTOM_SCALE\x10\xd1N*\xb6\x01\n\x10DigitalLineState\x12"\n\x1eDIGITAL_LINE_STATE_UNSPECIFIED\x10\x00\x12\x1c\n\x17DIGITAL_LINE_STATE_HIGH\x10\xd0O\x12\x1b\n\x16DIGITAL_LINE_STATE_LOW\x10\xe6O\x12 \n\x1bDIGITAL_LINE_STATE_TRISTATE\x10\xc6P\x12!\n\x1cDIGITAL_LINE_STATE_NO_CHANGE\x10\xb0O*\xaf\x01\n\x18DigitalPatternCondition1\x12*\n&DIGITAL_PATTERN_CONDITION1_UNSPECIFIED\x10\x00\x12/\n*DIGITAL_PATTERN_CONDITION1_PATTERN_MATCHES\x10\x8eP\x126\n1DIGITAL_PATTERN_CONDITION1_PATTERN_DOES_NOT_MATCH\x10\x8dP*]\n\x12DigitalWidthUnits3\x12$\n DIGITAL_WIDTH_UNITS3_UNSPECIFIED\x10\x00\x12!\n\x1cDIGITAL_WIDTH_UNITS3_SECONDS\x10\xfcP*\xae\x03\n$EddyCurrentProxProbeSensitivityUnits\x129\n5EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS_UNSPECIFIED\x10\x00\x12>\n9EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS_M_VOLTS_PER_MIL\x10\xf4s\x12<\n7EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS_VOLTS_PER_MIL\x10\xf5s\x12E\n@EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS_M_VOLTS_PER_MILLIMETER\x10\xf6s\x12C\n>EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS_VOLTS_PER_MILLIMETER\x10\xf7s\x12A\n<EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS_M_VOLTS_PER_MICRON\x10\xf8s*E\n\x05Edge1\x12\x15\n\x11EDGE1_UNSPECIFIED\x10\x00\x12\x11\n\x0cEDGE1_RISING\x10\xa8P\x12\x12\n\rEDGE1_FALLING\x10\xbbO*\x99\x01\n\x0cEncoderType2\x12\x1d\n\x19ENCODER_TYPE2_UNSPECIFIED\x10\x00\x12\x15\n\x10ENCODER_TYPE2_X1\x10\xeaN\x12\x15\n\x10ENCODER_TYPE2_X2\x10\xebN\x12\x15\n\x10ENCODER_TYPE2_X4\x10\xecN\x12%\n ENCODER_TYPE2_TWO_PULSE_COUNTING\x10\xc9P*\xe5\x01\n\x13EncoderZIndexPhase1\x12&\n"ENCODER_Z_INDEX_PHASE1_UNSPECIFIED\x10\x00\x12)\n$ENCODER_Z_INDEX_PHASE1_A_HIGH_B_HIGH\x10\xb8N\x12(\n#ENCODER_Z_INDEX_PHASE1_A_HIGH_B_LOW\x10\xb9N\x12(\n#ENCODER_Z_INDEX_PHASE1_A_LOW_B_HIGH\x10\xbaN\x12\'\n"ENCODER_Z_INDEX_PHASE1_A_LOW_B_LOW\x10\xbbN*\xb1\x01\n\x16EveryNSamplesEventType\x12*\n&EVERY_N_SAMPLES_EVENT_TYPE_UNSPECIFIED\x10\x00\x123\n/EVERY_N_SAMPLES_EVENT_TYPE_ACQUIRED_INTO_BUFFER\x10\x01\x126\n2EVERY_N_SAMPLES_EVENT_TYPE_TRANSFERRED_FROM_BUFFER\x10\x02*\x94\x01\n\x10ExcitationSource\x12!\n\x1dEXCITATION_SOURCE_UNSPECIFIED\x10\x00\x12\x1f\n\x1aEXCITATION_SOURCE_INTERNAL\x10\xd8O\x12\x1f\n\x1aEXCITATION_SOURCE_EXTERNAL\x10\xb7O\x12\x1b\n\x16EXCITATION_SOURCE_NONE\x10\xf6O*\xcf\x01\n\x1fForceIEPESensorSensitivityUnits\x123\n/FORCE_IEPE_SENSOR_SENSITIVITY_UNITS_UNSPECIFIED\x10\x00\x12;\n6FORCE_IEPE_SENSOR_SENSITIVITY_UNITS_M_VOLTS_PER_NEWTON\x10\x93|\x12:\n5FORCE_IEPE_SENSOR_SENSITIVITY_UNITS_M_VOLTS_PER_POUND\x10\x94|*\x98\x01\n\x0eForceIEPEUnits\x12 \n\x1cFORCE_IEPE_UNITS_UNSPECIFIED\x10\x00\x12\x1d\n\x18FORCE_IEPE_UNITS_NEWTONS\x10\x83|\x12\x1c\n\x17FORCE_IEPE_UNITS_POUNDS\x10\x84|\x12\'\n"FORCE_IEPE_UNITS_FROM_CUSTOM_SCALE\x10\xd1N*\xa1\x01\n\nForceUnits\x12\x1b\n\x17FORCE_UNITS_UNSPECIFIED\x10\x00\x12\x18\n\x13FORCE_UNITS_NEWTONS\x10\x83|\x12\x17\n\x12FORCE_UNITS_POUNDS\x10\x84|\x12\x1f\n\x1aFORCE_UNITS_KILOGRAM_FORCE\x10\x85|\x12"\n\x1dFORCE_UNITS_FROM_CUSTOM_SCALE\x10\xd1N*r\n\x0eFrequencyUnits\x12\x1f\n\x1bFREQUENCY_UNITS_UNSPECIFIED\x10\x00\x12\x17\n\x12FREQUENCY_UNITS_HZ\x10\x85Q\x12&\n!FREQUENCY_UNITS_FROM_CUSTOM_SCALE\x10\xd1N*M\n\x0fFrequencyUnits2\x12 \n\x1cFREQUENCY_UNITS2_UNSPECIFIED\x10\x00\x12\x18\n\x13FREQUENCY_UNITS2_HZ\x10\x85Q*\x93\x01\n\x0fFrequencyUnits3\x12 \n\x1cFREQUENCY_UNITS3_UNSPECIFIED\x10\x00\x12\x18\n\x13FREQUENCY_UNITS3_HZ\x10\x85Q\x12\x1b\n\x16FREQUENCY_UNITS3_TICKS\x10\xc0P\x12\'\n"FREQUENCY_UNITS3_FROM_CUSTOM_SCALE\x10\xd1N*\x9a\x01\n\x0bFuncGenType\x12\x1d\n\x19FUNC_GEN_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x12FUNC_GEN_TYPE_SINE\x10\x9fs\x12\x1b\n\x16FUNC_GEN_TYPE_TRIANGLE\x10\xa0s\x12\x19\n\x14FUNC_GEN_TYPE_SQUARE\x10\xa1s\x12\x1b\n\x16FUNC_GEN_TYPE_SAWTOOTH\x10\xa2s*\x86\x01\n\x0eGpsSignalType1\x12 \n\x1cGPS_SIGNAL_TYPE1_UNSPECIFIED\x10\x00\x12\x1b\n\x16GPS_SIGNAL_TYPE1_IRIGB\x10\xd6N\x12\x19\n\x14GPS_SIGNAL_TYPE1_PPS\x10\xe0N\x12\x1a\n\x15GPS_SIGNAL_TYPE1_NONE\x10\xf6O*K\n\x07GroupBy\x12\x1d\n\x19GROUP_BY_GROUP_BY_CHANNEL\x10\x00\x12!\n\x1dGROUP_BY_GROUP_BY_SCAN_NUMBER\x10\x01*\x9e\x02\n\x17InputTermCfgWithDefault\x12+\n\'INPUT_TERM_CFG_WITH_DEFAULT_UNSPECIFIED\x10\x00\x124\n\'INPUT_TERM_CFG_WITH_DEFAULT_CFG_DEFAULT\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12$\n\x1fINPUT_TERM_CFG_WITH_DEFAULT_RSE\x10\xe3N\x12%\n INPUT_TERM_CFG_WITH_DEFAULT_NRSE\x10\xdeN\x12%\n INPUT_TERM_CFG_WITH_DEFAULT_DIFF\x10\xfaN\x12,\n\'INPUT_TERM_CFG_WITH_DEFAULT_PSEUDO_DIFF\x10\xf1a*a\n\x0eInvertPolarity\x12*\n&INVERT_POLARITY_DO_NOT_INVERT_POLARITY\x10\x00\x12#\n\x1fINVERT_POLARITY_INVERT_POLARITY\x10\x01*\xbc\x01\n\x15LVDTSensitivityUnits1\x12\'\n#LVDT_SENSITIVITY_UNITS1_UNSPECIFIED\x10\x00\x12<\n7LVDT_SENSITIVITY_UNITS1_M_VOLTS_PER_VOLT_PER_MILLIMETER\x10\xdaa\x12<\n7LVDT_SENSITIVITY_UNITS1_M_VOLTS_PER_VOLT_PER_MILLI_INCH\x10\xd9a*\x89\x01\n\x0cLengthUnits2\x12\x1d\n\x19LENGTH_UNITS2_UNSPECIFIED\x10\x00\x12\x19\n\x14LENGTH_UNITS2_METERS\x10\xebO\x12\x19\n\x14LENGTH_UNITS2_INCHES\x10\x8bQ\x12$\n\x1fLENGTH_UNITS2_FROM_CUSTOM_SCALE\x10\xd1N*\xa3\x01\n\x0cLengthUnits3\x12\x1d\n\x19LENGTH_UNITS3_UNSPECIFIED\x10\x00\x12\x19\n\x14LENGTH_UNITS3_METERS\x10\xebO\x12\x19\n\x14LENGTH_UNITS3_INCHES\x10\x8bQ\x12\x18\n\x13LENGTH_UNITS3_TICKS\x10\xc0P\x12$\n\x1fLENGTH_UNITS3_FROM_CUSTOM_SCALE\x10\xd1N*C\n\x06Level1\x12\x16\n\x12LEVEL1_UNSPECIFIED\x10\x00\x12\x10\n\x0bLEVEL1_HIGH\x10\xd0O\x12\x0f\n\nLEVEL1_LOW\x10\xe6O*U\n\x0cLineGrouping\x12\x1f\n\x1bLINE_GROUPING_CHAN_PER_LINE\x10\x00\x12$\n LINE_GROUPING_CHAN_FOR_ALL_LINES\x10\x01*y\n\x0bLoggingMode\x12\x1c\n\x18LOGGING_MODE_UNSPECIFIED\x10\x00\x12\x15\n\x10LOGGING_MODE_OFF\x10\xf7O\x12\x15\n\x10LOGGING_MODE_LOG\x10\xe4{\x12\x1e\n\x19LOGGING_MODE_LOG_AND_READ\x10\xe2{*\xc2\x01\n\x10LoggingOperation\x12!\n\x1dLOGGING_OPERATION_UNSPECIFIED\x10\x00\x12\x1b\n\x16LOGGING_OPERATION_OPEN\x10\xc5Q\x12%\n LOGGING_OPERATION_OPEN_OR_CREATE\x10\xe6{\x12(\n#LOGGING_OPERATION_CREATE_OR_REPLACE\x10\xe7{\x12\x1d\n\x18LOGGING_OPERATION_CREATE\x10\xe8{*\x9c\x01\n\x0bLogicFamily\x12\x1c\n\x18LOGIC_FAMILY_UNSPECIFIED\x10\x00\x12\x1c\n\x17LOGIC_FAMILY_1POINT_8_V\x10\xb8~\x12\x1c\n\x17LOGIC_FAMILY_2POINT_5_V\x10\x9cr\x12\x1c\n\x17LOGIC_FAMILY_3POINT_3_V\x10\x9dr\x12\x15\n\x10LOGIC_FAMILY_5_V\x10\x9br*]\n\tPolarity2\x12\x19\n\x15POLARITY2_UNSPECIFIED\x10\x00\x12\x1a\n\x15POLARITY2_ACTIVE_HIGH\x10\xefN\x12\x19\n\x14POLARITY2_ACTIVE_LOW\x10\xf0N*e\n\nPowerUnits\x12\x1b\n\x17POWER_UNITS_UNSPECIFIED\x10\x00\x12\x16\n\x11POWER_UNITS_WATTS\x10\xcb~\x12"\n\x1dPOWER_UNITS_FROM_CUSTOM_SCALE\x10\xd1N*\x9c\x01\n\x12PowerUpChannelType\x12)\n%POWER_UP_CHANNEL_TYPE_CHANNEL_VOLTAGE\x10\x00\x12)\n%POWER_UP_CHANNEL_TYPE_CHANNEL_CURRENT\x10\x01\x120\n,POWER_UP_CHANNEL_TYPE_CHANNEL_HIGH_IMPEDANCE\x10\x02*\x84\x01\n\rPowerUpStates\x12\x1f\n\x1bPOWER_UP_STATES_UNSPECIFIED\x10\x00\x12\x19\n\x14POWER_UP_STATES_HIGH\x10\xd0O\x12\x18\n\x13POWER_UP_STATES_LOW\x10\xe6O\x12\x1d\n\x18POWER_UP_STATES_TRISTATE\x10\xc6P*\xb8\x01\n\rPressureUnits\x12\x1e\n\x1aPRESSURE_UNITS_UNSPECIFIED\x10\x00\x12\x1b\n\x16PRESSURE_UNITS_PASCALS\x10\xe1N\x12*\n%PRESSURE_UNITS_POUNDS_PER_SQUARE_INCH\x10\x87|\x12\x17\n\x12PRESSURE_UNITS_BAR\x10\x88|\x12%\n PRESSURE_UNITS_FROM_CUSTOM_SCALE\x10\xd1N*\xcc\x01\n\x08RTDType1\x12\x19\n\x15RTD_TYPE1_UNSPECIFIED\x10\x00\x12\x16\n\x11RTD_TYPE1_PT_3750\x10\xc1a\x12\x16\n\x11RTD_TYPE1_PT_3851\x10\xd7N\x12\x16\n\x11RTD_TYPE1_PT_3911\x10\xc2a\x12\x16\n\x11RTD_TYPE1_PT_3916\x10\xd5N\x12\x16\n\x11RTD_TYPE1_PT_3920\x10\xc5N\x12\x16\n\x11RTD_TYPE1_PT_3928\x10\xc3a\x12\x15\n\x10RTD_TYPE1_CUSTOM\x10\x99O*\xb4\x01\n\x15RVDTSensitivityUnits1\x12\'\n#RVDT_SENSITIVITY_UNITS1_UNSPECIFIED\x10\x00\x128\n3RVDT_SENSITIVITY_UNITS1_M_VOLTS_PER_VOLT_PER_DEGREE\x10\xdba\x128\n3RVDT_SENSITIVITY_UNITS1_M_VOLTS_PER_VOLT_PER_RADIAN\x10\xdca*\xb2\x01\n\x17ResistanceConfiguration\x12(\n$RESISTANCE_CONFIGURATION_UNSPECIFIED\x10\x00\x12#\n\x1fRESISTANCE_CONFIGURATION_2_WIRE\x10\x02\x12#\n\x1fRESISTANCE_CONFIGURATION_3_WIRE\x10\x03\x12#\n\x1fRESISTANCE_CONFIGURATION_4_WIRE\x10\x04*|\n\x10ResistanceUnits2\x12!\n\x1dRESISTANCE_UNITS2_UNSPECIFIED\x10\x00\x12\x1b\n\x16RESISTANCE_UNITS2_OHMS\x10\x90Q\x12(\n#RESISTANCE_UNITS2_FROM_CUSTOM_SCALE\x10\xd1N*k\n\rResistorState\x12\x1e\n\x1aRESISTOR_STATE_UNSPECIFIED\x10\x00\x12\x1b\n\x16RESISTOR_STATE_PULL_UP\x10\xce|\x12\x1d\n\x18RESISTOR_STATE_PULL_DOWN\x10\xcf|*\xa0\x01\n\x0bSaveOptions\x12\x1c\n\x18SAVE_OPTIONS_UNSPECIFIED\x10\x00\x12\x1a\n\x16SAVE_OPTIONS_OVERWRITE\x10\x01\x12*\n&SAVE_OPTIONS_ALLOW_INTERACTIVE_EDITING\x10\x02\x12+\n\'SAVE_OPTIONS_ALLOW_INTERACTIVE_DELETION\x10\x04*\x83\x01\n\x0eShuntCalSelect\x12 \n\x1cSHUNT_CAL_SELECT_UNSPECIFIED\x10\x00\x12\x17\n\x12SHUNT_CAL_SELECT_A\x10\xe1a\x12\x17\n\x12SHUNT_CAL_SELECT_B\x10\xe2a\x12\x1d\n\x18SHUNT_CAL_SELECT_A_AND_B\x10\xe3a*\x9e\x01\n\x0eShuntCalSource\x12 \n\x1cSHUNT_CAL_SOURCE_UNSPECIFIED\x10\x00\x12%\n\x18SHUNT_CAL_SOURCE_DEFAULT\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1e\n\x19SHUNT_CAL_SOURCE_BUILT_IN\x10\xd8O\x12#\n\x1eSHUNT_CAL_SOURCE_USER_PROVIDED\x10\xb7O*\xe0\x01\n\x14ShuntElementLocation\x12&\n"SHUNT_ELEMENT_LOCATION_UNSPECIFIED\x10\x00\x12\x1e\n\x19SHUNT_ELEMENT_LOCATION_R1\x10\xb1a\x12\x1e\n\x19SHUNT_ELEMENT_LOCATION_R2\x10\xb2a\x12\x1e\n\x19SHUNT_ELEMENT_LOCATION_R3\x10\xb3a\x12\x1e\n\x19SHUNT_ELEMENT_LOCATION_R4\x10\xdds\x12 \n\x1bSHUNT_ELEMENT_LOCATION_NONE\x10\xf6O*\x93\x03\n\x06Signal\x12\x16\n\x12SIGNAL_UNSPECIFIED\x10\x00\x12\x1c\n\x17SIGNAL_AI_CONVERT_CLOCK\x10\xc4a\x12\x1c\n\x17SIGNAL_10_MHZ_REF_CLOCK\x10\xf8a\x12!\n\x1cSIGNAL_20_MHZ_TIMEBASE_CLOCK\x10\xc6a\x12\x18\n\x13SIGNAL_SAMPLE_CLOCK\x10\xc7a\x12\x1b\n\x16SIGNAL_ADVANCE_TRIGGER\x10\xc8a\x12\x1d\n\x18SIGNAL_REFERENCE_TRIGGER\x10\xcaa\x12\x19\n\x14SIGNAL_START_TRIGGER\x10\xcba\x12\x1b\n\x16SIGNAL_ADV_CMPLT_EVENT\x10\xcca\x12\x1f\n\x1aSIGNAL_AI_HOLD_CMPLT_EVENT\x10\xcda\x12 \n\x1bSIGNAL_COUNTER_OUTPUT_EVENT\x10\xcea\x12"\n\x1dSIGNAL_CHANGE_DETECTION_EVENT\x10\xdfa\x12\x1d\n\x18SIGNAL_WDT_EXPIRED_EVENT\x10\xe0a*\xa9\x01\n\x07Signal2\x12\x17\n\x13SIGNAL2_UNSPECIFIED\x10\x00\x12"\n\x1dSIGNAL2_SAMPLE_COMPLETE_EVENT\x10\xf2a\x12!\n\x1cSIGNAL2_COUNTER_OUTPUT_EVENT\x10\xcea\x12#\n\x1eSIGNAL2_CHANGE_DETECTION_EVENT\x10\xdfa\x12\x19\n\x14SIGNAL2_SAMPLE_CLOCK\x10\xc7a*U\n\x06Slope1\x12\x16\n\x12SLOPE1_UNSPECIFIED\x10\x00\x12\x18\n\x13SLOPE1_RISING_SLOPE\x10\xa8P\x12\x19\n\x14SLOPE1_FALLING_SLOPE\x10\xbbO*\x8e\x01\n\x13SoundPressureUnits1\x12%\n!SOUND_PRESSURE_UNITS1_UNSPECIFIED\x10\x00\x12"\n\x1dSOUND_PRESSURE_UNITS1_PASCALS\x10\xe1N\x12,\n\'SOUND_PRESSURE_UNITS1_FROM_CUSTOM_SCALE\x10\xd1N*\x87\x03\n\x15StrainGageBridgeType1\x12(\n$STRAIN_GAGE_BRIDGE_TYPE1_UNSPECIFIED\x10\x00\x12+\n&STRAIN_GAGE_BRIDGE_TYPE1_FULL_BRIDGE_I\x10\xc7O\x12,\n\'STRAIN_GAGE_BRIDGE_TYPE1_FULL_BRIDGE_II\x10\xc8O\x12-\n(STRAIN_GAGE_BRIDGE_TYPE1_FULL_BRIDGE_III\x10\xc9O\x12+\n&STRAIN_GAGE_BRIDGE_TYPE1_HALF_BRIDGE_I\x10\xccO\x12,\n\'STRAIN_GAGE_BRIDGE_TYPE1_HALF_BRIDGE_II\x10\xcdO\x12.\n)STRAIN_GAGE_BRIDGE_TYPE1_QUARTER_BRIDGE_I\x10\x9fP\x12/\n*STRAIN_GAGE_BRIDGE_TYPE1_QUARTER_BRIDGE_II\x10\xa0P*\xd5\x04\n StrainGageRosetteMeasurementType\x124\n0STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_UNSPECIFIED\x10\x00\x12<\n7STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_PRINCIPAL_STRAIN_1\x10\xe3|\x12<\n7STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_PRINCIPAL_STRAIN_2\x10\xe4|\x12@\n;STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_PRINCIPAL_STRAIN_ANGLE\x10\xe5|\x12<\n7STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_CARTESIAN_STRAIN_X\x10\xe6|\x12<\n7STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_CARTESIAN_STRAIN_Y\x10\xe7|\x12C\n>STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_CARTESIAN_SHEAR_STRAIN_XY\x10\xe8|\x12:\n5STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_MAX_SHEAR_STRAIN\x10\xe9|\x12@\n;STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_MAX_SHEAR_STRAIN_ANGLE\x10\xea|*\xcc\x01\n\x15StrainGageRosetteType\x12(\n$STRAIN_GAGE_ROSETTE_TYPE_UNSPECIFIED\x10\x00\x121\n,STRAIN_GAGE_ROSETTE_TYPE_RECTANGULAR_ROSETTE\x10\xe0|\x12+\n&STRAIN_GAGE_ROSETTE_TYPE_DELTA_ROSETTE\x10\xe1|\x12)\n$STRAIN_GAGE_ROSETTE_TYPE_TEE_ROSETTE\x10\xe2|*n\n\x0cStrainUnits1\x12\x1d\n\x19STRAIN_UNITS1_UNSPECIFIED\x10\x00\x12\x19\n\x14STRAIN_UNITS1_STRAIN\x10\xbbP\x12$\n\x1fSTRAIN_UNITS1_FROM_CUSTOM_SCALE\x10\xd1N*e\n\tTEDSUnits\x12\x1a\n\x16TEDS_UNITS_UNSPECIFIED\x10\x00\x12!\n\x1cTEDS_UNITS_FROM_CUSTOM_SCALE\x10\xd1N\x12\x19\n\x14TEDS_UNITS_FROM_TEDS\x10\xe4a*\x96\x02\n\x11TaskControlAction\x12"\n\x1eTASK_CONTROL_ACTION_TASK_START\x10\x00\x12!\n\x1dTASK_CONTROL_ACTION_TASK_STOP\x10\x01\x12#\n\x1fTASK_CONTROL_ACTION_TASK_VERIFY\x10\x02\x12#\n\x1fTASK_CONTROL_ACTION_TASK_COMMIT\x10\x03\x12$\n TASK_CONTROL_ACTION_TASK_RESERVE\x10\x04\x12&\n"TASK_CONTROL_ACTION_TASK_UNRESERVE\x10\x05\x12"\n\x1eTASK_CONTROL_ACTION_TASK_ABORT\x10\x06*\xaf\x01\n\x10TemperatureUnits\x12!\n\x1dTEMPERATURE_UNITS_UNSPECIFIED\x10\x00\x12\x1c\n\x17TEMPERATURE_UNITS_DEG_C\x10\x9fO\x12\x1c\n\x17TEMPERATURE_UNITS_DEG_F\x10\xa0O\x12\x1e\n\x19TEMPERATURE_UNITS_KELVINS\x10\xd5P\x12\x1c\n\x17TEMPERATURE_UNITS_DEG_R\x10\xa1O*\x95\x03\n\x11ThermocoupleType1\x12"\n\x1eTHERMOCOUPLE_TYPE1_UNSPECIFIED\x10\x00\x12!\n\x1cTHERMOCOUPLE_TYPE1_J_TYPE_TC\x10\xd8N\x12!\n\x1cTHERMOCOUPLE_TYPE1_K_TYPE_TC\x10\xd9N\x12!\n\x1cTHERMOCOUPLE_TYPE1_N_TYPE_TC\x10\xddN\x12!\n\x1cTHERMOCOUPLE_TYPE1_R_TYPE_TC\x10\xe2N\x12!\n\x1cTHERMOCOUPLE_TYPE1_S_TYPE_TC\x10\xe5N\x12!\n\x1cTHERMOCOUPLE_TYPE1_T_TYPE_TC\x10\xe6N\x12!\n\x1cTHERMOCOUPLE_TYPE1_B_TYPE_TC\x10\xbfN\x12!\n\x1cTHERMOCOUPLE_TYPE1_E_TYPE_TC\x10\xc7N\x12!\n\x1cTHERMOCOUPLE_TYPE1_A_TYPE_TC\x10\xd0~\x12!\n\x1cTHERMOCOUPLE_TYPE1_C_TYPE_TC\x10\xd1~*c\n\tTimeUnits\x12\x1a\n\x16TIME_UNITS_UNSPECIFIED\x10\x00\x12\x17\n\x12TIME_UNITS_SECONDS\x10\xfcP\x12!\n\x1cTIME_UNITS_FROM_CUSTOM_SCALE\x10\xd1N*\x7f\n\nTimeUnits3\x12\x1b\n\x17TIME_UNITS3_UNSPECIFIED\x10\x00\x12\x18\n\x13TIME_UNITS3_SECONDS\x10\xfcP\x12\x16\n\x11TIME_UNITS3_TICKS\x10\xc0P\x12"\n\x1dTIME_UNITS3_FROM_CUSTOM_SCALE\x10\xd1N*c\n\nTimescale2\x12\x1a\n\x16TIMESCALE2_UNSPECIFIED\x10\x00\x12\x19\n\x14TIMESCALE2_HOST_TIME\x10\xfe}\x12\x1e\n\x19TIMESCALE2_IO_DEVICE_TIME\x10\xff}*\xd2\x01\n\x0eTimestampEvent\x12\x1f\n\x1bTIMESTAMP_EVENT_UNSPECIFIED\x10\x00\x12"\n\x1dTIMESTAMP_EVENT_START_TRIGGER\x10\xcba\x12&\n!TIMESTAMP_EVENT_REFERENCE_TRIGGER\x10\xcaa\x12&\n!TIMESTAMP_EVENT_ARM_START_TRIGGER\x10\xb1r\x12+\n&TIMESTAMP_EVENT_FIRST_SAMPLE_TIMESTAMP\x10\x82~*\xce\x01\n\x0bTorqueUnits\x12\x1c\n\x18TORQUE_UNITS_UNSPECIFIED\x10\x00\x12\x1f\n\x1aTORQUE_UNITS_NEWTON_METERS\x10\x89|\x12\x1d\n\x18TORQUE_UNITS_INCH_OUNCES\x10\x8a|\x12\x1d\n\x18TORQUE_UNITS_INCH_POUNDS\x10\x8b|\x12\x1d\n\x18TORQUE_UNITS_FOOT_POUNDS\x10\x8c|\x12#\n\x1eTORQUE_UNITS_FROM_CUSTOM_SCALE\x10\xd1N*\xb4\n\n\x0eUnitsPreScaled\x12 \n\x1cUNITS_PRE_SCALED_UNSPECIFIED\x10\x00\x12\x1b\n\x16UNITS_PRE_SCALED_VOLTS\x10\xecP\x12\x1a\n\x15UNITS_PRE_SCALED_AMPS\x10\xe6P\x12\x1b\n\x16UNITS_PRE_SCALED_DEG_F\x10\xa0O\x12\x1b\n\x16UNITS_PRE_SCALED_DEG_C\x10\x9fO\x12\x1b\n\x16UNITS_PRE_SCALED_DEG_R\x10\xa1O\x12\x1d\n\x18UNITS_PRE_SCALED_KELVINS\x10\xd5P\x12\x1c\n\x17UNITS_PRE_SCALED_STRAIN\x10\xbbP\x12\x1a\n\x15UNITS_PRE_SCALED_OHMS\x10\x90Q\x12\x18\n\x13UNITS_PRE_SCALED_HZ\x10\x85Q\x12\x1d\n\x18UNITS_PRE_SCALED_SECONDS\x10\xfcP\x12\x1c\n\x17UNITS_PRE_SCALED_METERS\x10\xebO\x12\x1c\n\x17UNITS_PRE_SCALED_INCHES\x10\x8bQ\x12\x1d\n\x18UNITS_PRE_SCALED_DEGREES\x10\xa2O\x12\x1d\n\x18UNITS_PRE_SCALED_RADIANS\x10\xa1P\x12\x1b\n\x16UNITS_PRE_SCALED_TICKS\x10\xc0P\x12\x19\n\x14UNITS_PRE_SCALED_RPM\x10\xd0}\x12(\n#UNITS_PRE_SCALED_RADIANS_PER_SECOND\x10\xd1}\x12(\n#UNITS_PRE_SCALED_DEGREES_PER_SECOND\x10\xd2}\x12\x17\n\x12UNITS_PRE_SCALED_G\x10\xcaO\x12/\n*UNITS_PRE_SCALED_METERS_PER_SECOND_SQUARED\x10\xb6a\x12/\n*UNITS_PRE_SCALED_INCHES_PER_SECOND_SQUARED\x10\xb7a\x12\'\n"UNITS_PRE_SCALED_METERS_PER_SECOND\x10\xd7|\x12\'\n"UNITS_PRE_SCALED_INCHES_PER_SECOND\x10\xd8|\x12\x1d\n\x18UNITS_PRE_SCALED_PASCALS\x10\xe1N\x12\x1d\n\x18UNITS_PRE_SCALED_NEWTONS\x10\x83|\x12\x1c\n\x17UNITS_PRE_SCALED_POUNDS\x10\x84|\x12$\n\x1fUNITS_PRE_SCALED_KILOGRAM_FORCE\x10\x85|\x12,\n\'UNITS_PRE_SCALED_POUNDS_PER_SQUARE_INCH\x10\x87|\x12\x19\n\x14UNITS_PRE_SCALED_BAR\x10\x88|\x12#\n\x1eUNITS_PRE_SCALED_NEWTON_METERS\x10\x89|\x12!\n\x1cUNITS_PRE_SCALED_INCH_OUNCES\x10\x8a|\x12!\n\x1cUNITS_PRE_SCALED_INCH_POUNDS\x10\x8b|\x12!\n\x1cUNITS_PRE_SCALED_FOOT_POUNDS\x10\x8c|\x12$\n\x1fUNITS_PRE_SCALED_VOLTS_PER_VOLT\x10\x98|\x12&\n!UNITS_PRE_SCALED_M_VOLTS_PER_VOLT\x10\x99|\x12\x1e\n\x19UNITS_PRE_SCALED_COULOMBS\x10\xe6}\x12#\n\x1eUNITS_PRE_SCALED_PICO_COULOMBS\x10\xe7}\x12\x1f\n\x1aUNITS_PRE_SCALED_FROM_TEDS\x10\xe4a*\xfb\x01\n"VelocityIEPESensorSensitivityUnits\x126\n2VELOCITY_IEPE_SENSOR_SENSITIVITY_UNITS_UNSPECIFIED\x10\x00\x12P\nKVELOCITY_IEPE_SENSOR_SENSITIVITY_UNITS_MILLIVOLTS_PER_MILLIMETER_PER_SECOND\x10\xdb|\x12K\nFVELOCITY_IEPE_SENSOR_SENSITIVITY_UNITS_MILLI_VOLTS_PER_INCH_PER_SECOND\x10\xdc|*\xa4\x01\n\rVelocityUnits\x12\x1e\n\x1aVELOCITY_UNITS_UNSPECIFIED\x10\x00\x12%\n VELOCITY_UNITS_METERS_PER_SECOND\x10\xd7|\x12%\n VELOCITY_UNITS_INCHES_PER_SECOND\x10\xd8|\x12%\n VELOCITY_UNITS_FROM_CUSTOM_SCALE\x10\xd1N*q\n\rVoltageUnits2\x12\x1e\n\x1aVOLTAGE_UNITS2_UNSPECIFIED\x10\x00\x12\x19\n\x14VOLTAGE_UNITS2_VOLTS\x10\xecP\x12%\n VOLTAGE_UNITS2_FROM_CUSTOM_SCALE\x10\xd1N*\xb3\x01\n\x14WatchdogAOOutputType\x12\'\n#WATCHDOG_AO_OUTPUT_TYPE_UNSPECIFIED\x10\x00\x12$\n\x1fWATCHDOG_AO_OUTPUT_TYPE_VOLTAGE\x10\xd2P\x12$\n\x1fWATCHDOG_AO_OUTPUT_TYPE_CURRENT\x10\x96O\x12&\n!WATCHDOG_AO_OUTPUT_TYPE_NO_CHANGE\x10\xb0O*\xac\x01\n\x14WatchdogCOExpirState\x12\'\n#WATCHDOG_CO_EXPIR_STATE_UNSPECIFIED\x10\x00\x12 \n\x1bWATCHDOG_CO_EXPIR_STATE_LOW\x10\xe6O\x12!\n\x1cWATCHDOG_CO_EXPIR_STATE_HIGH\x10\xd0O\x12&\n!WATCHDOG_CO_EXPIR_STATE_NO_CHANGE\x10\xb0O*n\n\x15WatchdogControlAction\x12\'\n#WATCHDOG_CONTROL_ACTION_RESET_TIMER\x10\x00\x12,\n(WATCHDOG_CONTROL_ACTION_CLEAR_EXPIRATION\x10\x01*\x9d\x01\n\x17WindowTriggerCondition1\x12)\n%WINDOW_TRIGGER_CONDITION1_UNSPECIFIED\x10\x00\x12+\n&WINDOW_TRIGGER_CONDITION1_ENTERING_WIN\x10\xb3O\x12*\n%WINDOW_TRIGGER_CONDITION1_LEAVING_WIN\x10\xe0O*\xc9\x01\n\x15WriteBasicTEDSOptions\x12(\n$WRITE_BASIC_TEDS_OPTIONS_UNSPECIFIED\x10\x00\x12-\n(WRITE_BASIC_TEDS_OPTIONS_WRITE_TO_EEPROM\x10\xfaa\x12+\n&WRITE_BASIC_TEDS_OPTIONS_WRITE_TO_PROM\x10\xfba\x12*\n%WRITE_BASIC_TEDS_OPTIONS_DO_NOT_WRITE\x10\xfca*\x8e\x01\n\x15WaveformAttributeMode\x12 \n\x1cWAVEFORM_ATTRIBUTE_MODE_NONE\x10\x00\x12"\n\x1eWAVEFORM_ATTRIBUTE_MODE_TIMING\x10\x01\x12/\n+WAVEFORM_ATTRIBUTE_MODE_EXTENDED_PROPERTIES\x10\x02*\xfb\x9a\x01\n\x1bChannelInt32AttributeValues\x12\x1d\n\x19CHANNEL_INT32_UNSPECIFIED\x10\x00\x12+\n\'CHANNEL_INT32_AC_EXCIT_WIRE_MODE_4_WIRE\x10\x04\x12+\n\'CHANNEL_INT32_AC_EXCIT_WIRE_MODE_5_WIRE\x10\x05\x12+\n\'CHANNEL_INT32_AC_EXCIT_WIRE_MODE_6_WIRE\x10\x06\x12,\n\'CHANNEL_INT32_ADC_TIMING_MODE_AUTOMATIC\x10\xe1}\x122\n-CHANNEL_INT32_ADC_TIMING_MODE_HIGH_RESOLUTION\x10\xd3O\x12-\n(CHANNEL_INT32_ADC_TIMING_MODE_HIGH_SPEED\x10\xf8r\x127\n2CHANNEL_INT32_ADC_TIMING_MODE_BEST_50_HZ_REJECTION\x10\xf9r\x127\n2CHANNEL_INT32_ADC_TIMING_MODE_BEST_60_HZ_REJECTION\x10\xfar\x12)\n$CHANNEL_INT32_ADC_TIMING_MODE_CUSTOM\x10\x99O\x12.\n)CHANNEL_INT32_AI_MEASUREMENT_TYPE_VOLTAGE\x10\xd2P\x122\n-CHANNEL_INT32_AI_MEASUREMENT_TYPE_VOLTAGE_RMS\x10\xeeP\x12.\n)CHANNEL_INT32_AI_MEASUREMENT_TYPE_CURRENT\x10\x96O\x122\n-CHANNEL_INT32_AI_MEASUREMENT_TYPE_CURRENT_RMS\x10\xefP\x12E\n@CHANNEL_INT32_AI_MEASUREMENT_TYPE_VOLTAGE_CUSTOM_WITH_EXCITATION\x10\xd3P\x12-\n(CHANNEL_INT32_AI_MEASUREMENT_TYPE_BRIDGE\x10\xa4|\x123\n.CHANNEL_INT32_AI_MEASUREMENT_TYPE_FREQ_VOLTAGE\x10\xc5O\x121\n,CHANNEL_INT32_AI_MEASUREMENT_TYPE_RESISTANCE\x10\xa6P\x12.\n)CHANNEL_INT32_AI_MEASUREMENT_TYPE_TEMP_TC\x10\xbfP\x123\n.CHANNEL_INT32_AI_MEASUREMENT_TYPE_TEMP_THRMSTR\x10\xbeP\x12/\n*CHANNEL_INT32_AI_MEASUREMENT_TYPE_TEMP_RTD\x10\xbdP\x12;\n6CHANNEL_INT32_AI_MEASUREMENT_TYPE_TEMP_BUILT_IN_SENSOR\x10\xc7P\x122\n-CHANNEL_INT32_AI_MEASUREMENT_TYPE_STRAIN_GAGE\x10\xbcP\x12:\n5CHANNEL_INT32_AI_MEASUREMENT_TYPE_ROSETTE_STRAIN_GAGE\x10\xec|\x124\n/CHANNEL_INT32_AI_MEASUREMENT_TYPE_POSITION_LVDT\x10\xf0P\x124\n/CHANNEL_INT32_AI_MEASUREMENT_TYPE_POSITION_RVDT\x10\xf1P\x12L\nGCHANNEL_INT32_AI_MEASUREMENT_TYPE_POSITION_EDDY_CURRENT_PROXIMITY_PROBE\x10\xf3s\x124\n/CHANNEL_INT32_AI_MEASUREMENT_TYPE_ACCELEROMETER\x10\xf4P\x12:\n5CHANNEL_INT32_AI_MEASUREMENT_TYPE_ACCELERATION_CHARGE\x10\xe8}\x12E\n@CHANNEL_INT32_AI_MEASUREMENT_TYPE_ACCELERATION_4_WIRE_DC_VOLTAGE\x10\xea}\x12;\n6CHANNEL_INT32_AI_MEASUREMENT_TYPE_VELOCITY_IEPE_SENSOR\x10\xde|\x123\n.CHANNEL_INT32_AI_MEASUREMENT_TYPE_FORCE_BRIDGE\x10\x9b|\x128\n3CHANNEL_INT32_AI_MEASUREMENT_TYPE_FORCE_IEPE_SENSOR\x10\x97|\x126\n1CHANNEL_INT32_AI_MEASUREMENT_TYPE_PRESSURE_BRIDGE\x10\x9e|\x12@\n;CHANNEL_INT32_AI_MEASUREMENT_TYPE_SOUND_PRESSURE_MICROPHONE\x10\xf2P\x124\n/CHANNEL_INT32_AI_MEASUREMENT_TYPE_TORQUE_BRIDGE\x10\xa1|\x122\n-CHANNEL_INT32_AI_MEASUREMENT_TYPE_TEDS_SENSOR\x10\xf3a\x12-\n(CHANNEL_INT32_AI_MEASUREMENT_TYPE_CHARGE\x10\xe9}\x12,\n\'CHANNEL_INT32_AI_MEASUREMENT_TYPE_POWER\x10\xc9~\x127\n2CHANNEL_INT32_AI_MEASUREMENT_TYPE_CALCULATED_POWER\x10\xcc~\x125\n0CHANNEL_INT32_AO_IDLE_OUTPUT_BEHAVIOR_ZERO_VOLTS\x10\xeea\x129\n4CHANNEL_INT32_AO_IDLE_OUTPUT_BEHAVIOR_HIGH_IMPEDANCE\x10\xefa\x12B\n=CHANNEL_INT32_AO_IDLE_OUTPUT_BEHAVIOR_MAINTAIN_EXISTING_VALUE\x10\xf0a\x121\n,CHANNEL_INT32_AO_OUTPUT_CHANNEL_TYPE_VOLTAGE\x10\xd2P\x121\n,CHANNEL_INT32_AO_OUTPUT_CHANNEL_TYPE_CURRENT\x10\x96O\x122\n-CHANNEL_INT32_AO_OUTPUT_CHANNEL_TYPE_FUNC_GEN\x10\x9es\x12E\n@CHANNEL_INT32_ACCEL_CHARGE_SENSITIVITY_UNITS_PICO_COULOMBS_PER_G\x10\xe3}\x12]\nXCHANNEL_INT32_ACCEL_CHARGE_SENSITIVITY_UNITS_PICO_COULOMBS_PER_METERS_PER_SECOND_SQUARED\x10\xe4}\x12]\nXCHANNEL_INT32_ACCEL_CHARGE_SENSITIVITY_UNITS_PICO_COULOMBS_PER_INCHES_PER_SECOND_SQUARED\x10\xe5}\x129\n4CHANNEL_INT32_ACCEL_SENSITIVITY_UNITS1_M_VOLTS_PER_G\x10\xdda\x127\n2CHANNEL_INT32_ACCEL_SENSITIVITY_UNITS1_VOLTS_PER_G\x10\xdea\x12,\n\'CHANNEL_INT32_ACCEL_UNITS2_ACCEL_UNIT_G\x10\xcaO\x129\n4CHANNEL_INT32_ACCEL_UNITS2_METERS_PER_SECOND_SQUARED\x10\xb6a\x129\n4CHANNEL_INT32_ACCEL_UNITS2_INCHES_PER_SECOND_SQUARED\x10\xb7a\x121\n,CHANNEL_INT32_ACCEL_UNITS2_FROM_CUSTOM_SCALE\x10\xd1N\x12\'\n"CHANNEL_INT32_ANGLE_UNITS1_DEGREES\x10\xa2O\x12\'\n"CHANNEL_INT32_ANGLE_UNITS1_RADIANS\x10\xa1P\x121\n,CHANNEL_INT32_ANGLE_UNITS1_FROM_CUSTOM_SCALE\x10\xd1N\x12\'\n"CHANNEL_INT32_ANGLE_UNITS2_DEGREES\x10\xa2O\x12\'\n"CHANNEL_INT32_ANGLE_UNITS2_RADIANS\x10\xa1P\x12%\n CHANNEL_INT32_ANGLE_UNITS2_TICKS\x10\xc0P\x121\n,CHANNEL_INT32_ANGLE_UNITS2_FROM_CUSTOM_SCALE\x10\xd1N\x12\'\n"CHANNEL_INT32_ANGLE_UNITS3_DEGREES\x10\xa2O\x121\n,CHANNEL_INT32_ANGLE_UNITS3_FROM_CUSTOM_SCALE\x10\xd1N\x12-\n(CHANNEL_INT32_ANGULAR_VELOCITY_UNITS_RPM\x10\xd0}\x12<\n7CHANNEL_INT32_ANGULAR_VELOCITY_UNITS_RADIANS_PER_SECOND\x10\xd1}\x12<\n7CHANNEL_INT32_ANGULAR_VELOCITY_UNITS_DEGREES_PER_SECOND\x10\xd2}\x12;\n6CHANNEL_INT32_ANGULAR_VELOCITY_UNITS_FROM_CUSTOM_SCALE\x10\xd1N\x12\'\n"CHANNEL_INT32_AUTO_ZERO_TYPE1_NONE\x10\xf6O\x12\'\n"CHANNEL_INT32_AUTO_ZERO_TYPE1_ONCE\x10\x84P\x12/\n*CHANNEL_INT32_AUTO_ZERO_TYPE1_EVERY_SAMPLE\x10\xb4O\x124\n/CHANNEL_INT32_BRIDGE_CONFIGURATION1_FULL_BRIDGE\x10\xc6O\x124\n/CHANNEL_INT32_BRIDGE_CONFIGURATION1_HALF_BRIDGE\x10\xcbO\x127\n2CHANNEL_INT32_BRIDGE_CONFIGURATION1_QUARTER_BRIDGE\x10\x9eP\x122\n-CHANNEL_INT32_BRIDGE_CONFIGURATION1_NO_BRIDGE\x10\xf4O\x129\n4CHANNEL_INT32_BRIDGE_ELECTRICAL_UNITS_VOLTS_PER_VOLT\x10\x98|\x12;\n6CHANNEL_INT32_BRIDGE_ELECTRICAL_UNITS_M_VOLTS_PER_VOLT\x10\x99|\x120\n+CHANNEL_INT32_BRIDGE_PHYSICAL_UNITS_NEWTONS\x10\x83|\x12/\n*CHANNEL_INT32_BRIDGE_PHYSICAL_UNITS_POUNDS\x10\x84|\x127\n2CHANNEL_INT32_BRIDGE_PHYSICAL_UNITS_KILOGRAM_FORCE\x10\x85|\x120\n+CHANNEL_INT32_BRIDGE_PHYSICAL_UNITS_PASCALS\x10\xe1N\x12?\n:CHANNEL_INT32_BRIDGE_PHYSICAL_UNITS_POUNDS_PER_SQUARE_INCH\x10\x87|\x12,\n\'CHANNEL_INT32_BRIDGE_PHYSICAL_UNITS_BAR\x10\x88|\x126\n1CHANNEL_INT32_BRIDGE_PHYSICAL_UNITS_NEWTON_METERS\x10\x89|\x124\n/CHANNEL_INT32_BRIDGE_PHYSICAL_UNITS_INCH_OUNCES\x10\x8a|\x124\n/CHANNEL_INT32_BRIDGE_PHYSICAL_UNITS_INCH_POUNDS\x10\x8b|\x124\n/CHANNEL_INT32_BRIDGE_PHYSICAL_UNITS_FOOT_POUNDS\x10\x8c|\x123\n.CHANNEL_INT32_BRIDGE_SHUNT_CAL_SOURCE_BUILT_IN\x10\xd8O\x128\n3CHANNEL_INT32_BRIDGE_SHUNT_CAL_SOURCE_USER_PROVIDED\x10\xb7O\x12.\n)CHANNEL_INT32_BRIDGE_UNITS_VOLTS_PER_VOLT\x10\x98|\x120\n+CHANNEL_INT32_BRIDGE_UNITS_M_VOLTS_PER_VOLT\x10\x99|\x121\n,CHANNEL_INT32_BRIDGE_UNITS_FROM_CUSTOM_SCALE\x10\xd1N\x12)\n$CHANNEL_INT32_BRIDGE_UNITS_FROM_TEDS\x10\xe4a\x122\n-CHANNEL_INT32_CI_MEASUREMENT_TYPE_COUNT_EDGES\x10\x8dO\x12+\n&CHANNEL_INT32_CI_MEASUREMENT_TYPE_FREQ\x10\xc3O\x12-\n(CHANNEL_INT32_CI_MEASUREMENT_TYPE_PERIOD\x10\x90P\x122\n-CHANNEL_INT32_CI_MEASUREMENT_TYPE_PULSE_WIDTH\x10\xf7P\x122\n-CHANNEL_INT32_CI_MEASUREMENT_TYPE_SEMI_PERIOD\x10\xb1P\x126\n1CHANNEL_INT32_CI_MEASUREMENT_TYPE_PULSE_FREQUENCY\x10\xf8{\x121\n,CHANNEL_INT32_CI_MEASUREMENT_TYPE_PULSE_TIME\x10\xf9{\x122\n-CHANNEL_INT32_CI_MEASUREMENT_TYPE_PULSE_TICKS\x10\xfa{\x121\n,CHANNEL_INT32_CI_MEASUREMENT_TYPE_DUTY_CYCLE\x10\xc6}\x12;\n6CHANNEL_INT32_CI_MEASUREMENT_TYPE_POSITION_ANG_ENCODER\x10\xf8P\x12;\n6CHANNEL_INT32_CI_MEASUREMENT_TYPE_POSITION_LIN_ENCODER\x10\xf9P\x12;\n6CHANNEL_INT32_CI_MEASUREMENT_TYPE_VELOCITY_ANG_ENCODER\x10\xce}\x12;\n6CHANNEL_INT32_CI_MEASUREMENT_TYPE_VELOCITY_LIN_ENCODER\x10\xcf}\x123\n.CHANNEL_INT32_CI_MEASUREMENT_TYPE_TWO_EDGE_SEP\x10\x9bP\x124\n/CHANNEL_INT32_CI_MEASUREMENT_TYPE_GPS_TIMESTAMP\x10\xfaP\x12\'\n"CHANNEL_INT32_CJC_SOURCE1_BUILT_IN\x10\xd8O\x12(\n#CHANNEL_INT32_CJC_SOURCE1_CONST_VAL\x10\x84O\x12#\n\x1eCHANNEL_INT32_CJC_SOURCE1_CHAN\x10\x81O\x12,\n\'CHANNEL_INT32_CO_OUTPUT_TYPE_PULSE_TIME\x10\x9dP\x12,\n\'CHANNEL_INT32_CO_OUTPUT_TYPE_PULSE_FREQ\x10\x87O\x12-\n(CHANNEL_INT32_CO_OUTPUT_TYPE_PULSE_TICKS\x10\x9cP\x12"\n\x1dCHANNEL_INT32_CHANNEL_TYPE_AI\x10\xf4N\x12"\n\x1dCHANNEL_INT32_CHANNEL_TYPE_AO\x10\xf6N\x12"\n\x1dCHANNEL_INT32_CHANNEL_TYPE_DI\x10\xa7O\x12"\n\x1dCHANNEL_INT32_CHANNEL_TYPE_DO\x10\xa9O\x12"\n\x1dCHANNEL_INT32_CHANNEL_TYPE_CI\x10\x93O\x12"\n\x1dCHANNEL_INT32_CHANNEL_TYPE_CO\x10\x94O\x12(\n#CHANNEL_INT32_CHARGE_UNITS_COULOMBS\x10\xe6}\x12-\n(CHANNEL_INT32_CHARGE_UNITS_PICO_COULOMBS\x10\xe7}\x121\n,CHANNEL_INT32_CHARGE_UNITS_FROM_CUSTOM_SCALE\x10\xd1N\x125\n0CHANNEL_INT32_CONSTRAINED_GEN_MODE_UNCONSTRAINED\x10\xf4r\x127\n2CHANNEL_INT32_CONSTRAINED_GEN_MODE_FIXED_HIGH_FREQ\x10\xf5r\x126\n1CHANNEL_INT32_CONSTRAINED_GEN_MODE_FIXED_LOW_FREQ\x10\xf6r\x12C\n>CHANNEL_INT32_CONSTRAINED_GEN_MODE_FIXED_50_PERCENT_DUTY_CYCLE\x10\xf7r\x12,\n\'CHANNEL_INT32_COUNT_DIRECTION1_COUNT_UP\x10\x90O\x12.\n)CHANNEL_INT32_COUNT_DIRECTION1_COUNT_DOWN\x10\x8cO\x122\n-CHANNEL_INT32_COUNT_DIRECTION1_EXT_CONTROLLED\x10\xd6P\x12:\n5CHANNEL_INT32_COUNTER_FREQUENCY_METHOD_LOW_FREQ_1_CTR\x10\xf9N\x12;\n6CHANNEL_INT32_COUNTER_FREQUENCY_METHOD_HIGH_FREQ_2_CTR\x10\xadO\x12;\n6CHANNEL_INT32_COUNTER_FREQUENCY_METHOD_LARGE_RNG_2_CTR\x10\xddO\x123\n.CHANNEL_INT32_COUNTER_FREQUENCY_METHOD_DYN_AVG\x10\xc1}\x12\x1f\n\x1aCHANNEL_INT32_COUPLING1_AC\x10\xbdN\x12\x1f\n\x1aCHANNEL_INT32_COUPLING1_DC\x10\xc2N\x12 \n\x1bCHANNEL_INT32_COUPLING1_GND\x10\xd2N\x12<\n7CHANNEL_INT32_CURRENT_SHUNT_RESISTOR_LOCATION1_INTERNAL\x10\xd8O\x12<\n7CHANNEL_INT32_CURRENT_SHUNT_RESISTOR_LOCATION1_EXTERNAL\x10\xb7O\x12&\n!CHANNEL_INT32_CURRENT_UNITS1_AMPS\x10\xe6P\x123\n.CHANNEL_INT32_CURRENT_UNITS1_FROM_CUSTOM_SCALE\x10\xd1N\x12+\n&CHANNEL_INT32_CURRENT_UNITS1_FROM_TEDS\x10\xe4a\x126\n1CHANNEL_INT32_DATA_JUSTIFICATION1_RIGHT_JUSTIFIED\x10\xa7P\x125\n0CHANNEL_INT32_DATA_JUSTIFICATION1_LEFT_JUSTIFIED\x10\xe1O\x12.\n)CHANNEL_INT32_DATA_TRANSFER_MECHANISM_DMA\x10\xc6N\x125\n0CHANNEL_INT32_DATA_TRANSFER_MECHANISM_INTERRUPTS\x10\xdcO\x128\n3CHANNEL_INT32_DATA_TRANSFER_MECHANISM_PROGRAMMED_IO\x10\x98P\x123\n.CHANNEL_INT32_DATA_TRANSFER_MECHANISM_US_BBULK\x10\xaeb\x122\n-CHANNEL_INT32_DIGITAL_DRIVE_TYPE_ACTIVE_DRIVE\x10\x9db\x124\n/CHANNEL_INT32_DIGITAL_DRIVE_TYPE_OPEN_COLLECTOR\x10\x9eb\x12*\n%CHANNEL_INT32_DIGITAL_LINE_STATE_HIGH\x10\xd0O\x12)\n$CHANNEL_INT32_DIGITAL_LINE_STATE_LOW\x10\xe6O\x12.\n)CHANNEL_INT32_DIGITAL_LINE_STATE_TRISTATE\x10\xc6P\x12/\n*CHANNEL_INT32_DIGITAL_LINE_STATE_NO_CHANGE\x10\xb0O\x12/\n*CHANNEL_INT32_DIGITAL_WIDTH_UNITS4_SECONDS\x10\xfcP\x12:\n5CHANNEL_INT32_DIGITAL_WIDTH_UNITS4_SAMPLE_CLK_PERIODS\x10\xaeP\x12L\nGCHANNEL_INT32_EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS_M_VOLTS_PER_MIL\x10\xf4s\x12J\nECHANNEL_INT32_EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS_VOLTS_PER_MIL\x10\xf5s\x12S\nNCHANNEL_INT32_EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS_M_VOLTS_PER_MILLIMETER\x10\xf6s\x12Q\nLCHANNEL_INT32_EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS_VOLTS_PER_MILLIMETER\x10\xf7s\x12O\nJCHANNEL_INT32_EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS_M_VOLTS_PER_MICRON\x10\xf8s\x12\x1f\n\x1aCHANNEL_INT32_EDGE1_RISING\x10\xa8P\x12 \n\x1bCHANNEL_INT32_EDGE1_FALLING\x10\xbbO\x12#\n\x1eCHANNEL_INT32_ENCODER_TYPE2_X1\x10\xeaN\x12#\n\x1eCHANNEL_INT32_ENCODER_TYPE2_X2\x10\xebN\x12#\n\x1eCHANNEL_INT32_ENCODER_TYPE2_X4\x10\xecN\x123\n.CHANNEL_INT32_ENCODER_TYPE2_TWO_PULSE_COUNTING\x10\xc9P\x127\n2CHANNEL_INT32_ENCODER_Z_INDEX_PHASE1_A_HIGH_B_HIGH\x10\xb8N\x126\n1CHANNEL_INT32_ENCODER_Z_INDEX_PHASE1_A_HIGH_B_LOW\x10\xb9N\x126\n1CHANNEL_INT32_ENCODER_Z_INDEX_PHASE1_A_LOW_B_HIGH\x10\xbaN\x125\n0CHANNEL_INT32_ENCODER_Z_INDEX_PHASE1_A_LOW_B_LOW\x10\xbbN\x12)\n$CHANNEL_INT32_EXCITATION_D_COR_AC_DC\x10\xc2N\x12)\n$CHANNEL_INT32_EXCITATION_D_COR_AC_AC\x10\xbdN\x12E\n@CHANNEL_INT32_EXCITATION_IDLE_OUTPUT_BEHAVIOR_ZERO_VOLTS_OR_AMPS\x10\xeea\x12J\nECHANNEL_INT32_EXCITATION_IDLE_OUTPUT_BEHAVIOR_MAINTAIN_EXISTING_VALUE\x10\xf0a\x12-\n(CHANNEL_INT32_EXCITATION_SOURCE_INTERNAL\x10\xd8O\x12-\n(CHANNEL_INT32_EXCITATION_SOURCE_EXTERNAL\x10\xb7O\x12)\n$CHANNEL_INT32_EXCITATION_SOURCE_NONE\x10\xf6O\x128\n3CHANNEL_INT32_EXCITATION_VOLTAGE_OR_CURRENT_VOLTAGE\x10\xd2P\x128\n3CHANNEL_INT32_EXCITATION_VOLTAGE_OR_CURRENT_CURRENT\x10\x96O\x127\n2CHANNEL_INT32_FILTER_RESPONSE_CONSTANT_GROUP_DELAY\x10\xcb}\x12.\n)CHANNEL_INT32_FILTER_RESPONSE_BUTTERWORTH\x10\xcc}\x12-\n(CHANNEL_INT32_FILTER_RESPONSE_ELLIPTICAL\x10\xcd}\x123\n.CHANNEL_INT32_FILTER_RESPONSE_HARDWARE_DEFINED\x10\xcfO\x12(\n#CHANNEL_INT32_FILTER_RESPONSE1_COMB\x10\x98~\x12*\n%CHANNEL_INT32_FILTER_RESPONSE1_BESSEL\x10\x99~\x12-\n(CHANNEL_INT32_FILTER_RESPONSE1_BRICKWALL\x10\x9b~\x12/\n*CHANNEL_INT32_FILTER_RESPONSE1_BUTTERWORTH\x10\xcc}\x120\n+CHANNEL_INT32_FILTER_TYPE1_HARDWARE_DEFINED\x10\xcfO\x12\'\n"CHANNEL_INT32_FILTER_TYPE2_LOWPASS\x10\xc7}\x12(\n#CHANNEL_INT32_FILTER_TYPE2_HIGHPASS\x10\xc8}\x12(\n#CHANNEL_INT32_FILTER_TYPE2_BANDPASS\x10\xc9}\x12%\n CHANNEL_INT32_FILTER_TYPE2_NOTCH\x10\xca}\x12&\n!CHANNEL_INT32_FILTER_TYPE2_CUSTOM\x10\x99O\x12I\nDCHANNEL_INT32_FORCE_IEPE_SENSOR_SENSITIVITY_UNITS_M_VOLTS_PER_NEWTON\x10\x93|\x12H\nCCHANNEL_INT32_FORCE_IEPE_SENSOR_SENSITIVITY_UNITS_M_VOLTS_PER_POUND\x10\x94|\x12&\n!CHANNEL_INT32_FORCE_UNITS_NEWTONS\x10\x83|\x12%\n CHANNEL_INT32_FORCE_UNITS_POUNDS\x10\x84|\x12-\n(CHANNEL_INT32_FORCE_UNITS_KILOGRAM_FORCE\x10\x85|\x120\n+CHANNEL_INT32_FORCE_UNITS_FROM_CUSTOM_SCALE\x10\xd1N\x12%\n CHANNEL_INT32_FREQUENCY_UNITS_HZ\x10\x85Q\x124\n/CHANNEL_INT32_FREQUENCY_UNITS_FROM_CUSTOM_SCALE\x10\xd1N\x12&\n!CHANNEL_INT32_FREQUENCY_UNITS2_HZ\x10\x85Q\x12&\n!CHANNEL_INT32_FREQUENCY_UNITS3_HZ\x10\x85Q\x12)\n$CHANNEL_INT32_FREQUENCY_UNITS3_TICKS\x10\xc0P\x125\n0CHANNEL_INT32_FREQUENCY_UNITS3_FROM_CUSTOM_SCALE\x10\xd1N\x12%\n CHANNEL_INT32_FUNC_GEN_TYPE_SINE\x10\x9fs\x12)\n$CHANNEL_INT32_FUNC_GEN_TYPE_TRIANGLE\x10\xa0s\x12\'\n"CHANNEL_INT32_FUNC_GEN_TYPE_SQUARE\x10\xa1s\x12)\n$CHANNEL_INT32_FUNC_GEN_TYPE_SAWTOOTH\x10\xa2s\x12)\n$CHANNEL_INT32_GPS_SIGNAL_TYPE1_IRIGB\x10\xd6N\x12\'\n"CHANNEL_INT32_GPS_SIGNAL_TYPE1_PPS\x10\xe0N\x12(\n#CHANNEL_INT32_GPS_SIGNAL_TYPE1_NONE\x10\xf6O\x12O\nJCHANNEL_INT32_INPUT_DATA_TRANSFER_CONDITION_ON_BRD_MEM_MORE_THAN_HALF_FULL\x10\xfdO\x12E\n@CHANNEL_INT32_INPUT_DATA_TRANSFER_CONDITION_ON_BRD_MEM_NOT_EMPTY\x10\x81P\x12K\nFCHANNEL_INT32_INPUT_DATA_TRANSFER_CONDITION_ONBRD_MEM_CUSTOM_THRESHOLD\x10\xa1b\x12B\n=CHANNEL_INT32_INPUT_DATA_TRANSFER_CONDITION_WHEN_ACQ_COMPLETE\x10\x82b\x12%\n CHANNEL_INT32_INPUT_TERM_CFG_RSE\x10\xe3N\x12&\n!CHANNEL_INT32_INPUT_TERM_CFG_NRSE\x10\xdeN\x12&\n!CHANNEL_INT32_INPUT_TERM_CFG_DIFF\x10\xfaN\x12-\n(CHANNEL_INT32_INPUT_TERM_CFG_PSEUDO_DIFF\x10\xf1a\x12\'\n"CHANNEL_INT32_INPUT_TERM_CFG2_DIFF\x10\xfaN\x12&\n!CHANNEL_INT32_INPUT_TERM_CFG2_RSE\x10\xe3N\x12J\nECHANNEL_INT32_LVDT_SENSITIVITY_UNITS1_M_VOLTS_PER_VOLT_PER_MILLIMETER\x10\xdaa\x12J\nECHANNEL_INT32_LVDT_SENSITIVITY_UNITS1_M_VOLTS_PER_VOLT_PER_MILLI_INCH\x10\xd9a\x12\'\n"CHANNEL_INT32_LENGTH_UNITS2_METERS\x10\xebO\x12\'\n"CHANNEL_INT32_LENGTH_UNITS2_INCHES\x10\x8bQ\x122\n-CHANNEL_INT32_LENGTH_UNITS2_FROM_CUSTOM_SCALE\x10\xd1N\x12\'\n"CHANNEL_INT32_LENGTH_UNITS3_METERS\x10\xebO\x12\'\n"CHANNEL_INT32_LENGTH_UNITS3_INCHES\x10\x8bQ\x12&\n!CHANNEL_INT32_LENGTH_UNITS3_TICKS\x10\xc0P\x122\n-CHANNEL_INT32_LENGTH_UNITS3_FROM_CUSTOM_SCALE\x10\xd1N\x12\'\n"CHANNEL_INT32_LENGTH_UNITS4_METERS\x10\xebO\x12%\n CHANNEL_INT32_LENGTH_UNITS4_FEET\x10\x8cQ\x122\n-CHANNEL_INT32_LENGTH_UNITS4_FROM_CUSTOM_SCALE\x10\xd1N\x12\x1e\n\x19CHANNEL_INT32_LEVEL1_HIGH\x10\xd0O\x12\x1d\n\x18CHANNEL_INT32_LEVEL1_LOW\x10\xe6O\x12*\n%CHANNEL_INT32_LOGIC_FAMILY_1POINT_8_V\x10\xb8~\x12*\n%CHANNEL_INT32_LOGIC_FAMILY_2POINT_5_V\x10\x9cr\x12*\n%CHANNEL_INT32_LOGIC_FAMILY_3POINT_3_V\x10\x9dr\x12#\n\x1eCHANNEL_INT32_LOGIC_FAMILY_5_V\x10\x9br\x129\n4CHANNEL_INT32_LOGIC_LVL_BEHAVIOR_LOGIC_LEVEL_PULL_UP\x10\xc0}\x12*\n%CHANNEL_INT32_LOGIC_LVL_BEHAVIOR_NONE\x10\xf6O\x12%\n CHANNEL_INT32_MODULATION_TYPE_AM\x10\xa4s\x12%\n CHANNEL_INT32_MODULATION_TYPE_FM\x10\xa5s\x12\'\n"CHANNEL_INT32_MODULATION_TYPE_NONE\x10\xf6O\x120\n+CHANNEL_INT32_NAV_MEASUREMENT_TYPE_ALTITUDE\x10\xfd|\x121\n,CHANNEL_INT32_NAV_MEASUREMENT_TYPE_LONGITUDE\x10\xfe|\x120\n+CHANNEL_INT32_NAV_MEASUREMENT_TYPE_LATITUDE\x10\xff|\x129\n4CHANNEL_INT32_NAV_MEASUREMENT_TYPE_SPEED_OVER_GROUND\x10\x80}\x12-\n(CHANNEL_INT32_NAV_MEASUREMENT_TYPE_TRACK\x10\x81}\x121\n,CHANNEL_INT32_NAV_MEASUREMENT_TYPE_TIMESTAMP\x10\xf2|\x125\n0CHANNEL_INT32_NAV_MEASUREMENT_TYPE_VERT_VELOCITY\x10\x83}\x12B\n=CHANNEL_INT32_OUTPUT_DATA_TRANSFER_CONDITION_ON_BRD_MEM_EMPTY\x10\xfbO\x12N\nICHANNEL_INT32_OUTPUT_DATA_TRANSFER_CONDITION_ON_BRD_MEM_HALF_FULL_OR_LESS\x10\xffO\x12E\n@CHANNEL_INT32_OUTPUT_DATA_TRANSFER_CONDITION_ON_BRD_MEM_NOT_FULL\x10\x82P\x12&\n!CHANNEL_INT32_OUTPUT_TERM_CFG_RSE\x10\xe3N\x12\'\n"CHANNEL_INT32_OUTPUT_TERM_CFG_DIFF\x10\xfaN\x12.\n)CHANNEL_INT32_OUTPUT_TERM_CFG_PSEUDO_DIFF\x10\xf1a\x12=\n8CHANNEL_INT32_POWER_IDLE_OUTPUT_BEHAVIOR_OUTPUT_DISABLED\x10\x8fy\x12E\n@CHANNEL_INT32_POWER_IDLE_OUTPUT_BEHAVIOR_MAINTAIN_EXISTING_VALUE\x10\xf0a\x126\n1CHANNEL_INT32_POWER_OUTPUT_STATE_CONSTANT_VOLTAGE\x10\x8cy\x126\n1CHANNEL_INT32_POWER_OUTPUT_STATE_CONSTANT_CURRENT\x10\x8dy\x121\n,CHANNEL_INT32_POWER_OUTPUT_STATE_OVERVOLTAGE\x10\x8ey\x125\n0CHANNEL_INT32_POWER_OUTPUT_STATE_OUTPUT_DISABLED\x10\x8fy\x12$\n\x1fCHANNEL_INT32_POWER_UNITS_WATTS\x10\xcb~\x120\n+CHANNEL_INT32_POWER_UNITS_FROM_CUSTOM_SCALE\x10\xd1N\x12)\n$CHANNEL_INT32_PRESSURE_UNITS_PASCALS\x10\xe1N\x128\n3CHANNEL_INT32_PRESSURE_UNITS_POUNDS_PER_SQUARE_INCH\x10\x87|\x12%\n CHANNEL_INT32_PRESSURE_UNITS_BAR\x10\x88|\x123\n.CHANNEL_INT32_PRESSURE_UNITS_FROM_CUSTOM_SCALE\x10\xd1N\x12$\n\x1fCHANNEL_INT32_RTD_TYPE1_PT_3750\x10\xc1a\x12$\n\x1fCHANNEL_INT32_RTD_TYPE1_PT_3851\x10\xd7N\x12$\n\x1fCHANNEL_INT32_RTD_TYPE1_PT_3911\x10\xc2a\x12$\n\x1fCHANNEL_INT32_RTD_TYPE1_PT_3916\x10\xd5N\x12$\n\x1fCHANNEL_INT32_RTD_TYPE1_PT_3920\x10\xc5N\x12$\n\x1fCHANNEL_INT32_RTD_TYPE1_PT_3928\x10\xc3a\x12#\n\x1eCHANNEL_INT32_RTD_TYPE1_CUSTOM\x10\x99O\x12F\nACHANNEL_INT32_RVDT_SENSITIVITY_UNITS1_M_VOLTS_PER_VOLT_PER_DEGREE\x10\xdba\x12F\nACHANNEL_INT32_RVDT_SENSITIVITY_UNITS1_M_VOLTS_PER_VOLT_PER_RADIAN\x10\xdca\x121\n,CHANNEL_INT32_RAW_DATA_COMPRESSION_TYPE_NONE\x10\xf6O\x12=\n8CHANNEL_INT32_RAW_DATA_COMPRESSION_TYPE_LOSSLESS_PACKING\x10\x8bb\x12>\n9CHANNEL_INT32_RAW_DATA_COMPRESSION_TYPE_LOSSY_LSB_REMOVAL\x10\x8cb\x121\n-CHANNEL_INT32_RESISTANCE_CONFIGURATION_2_WIRE\x10\x02\x121\n-CHANNEL_INT32_RESISTANCE_CONFIGURATION_3_WIRE\x10\x03\x121\n-CHANNEL_INT32_RESISTANCE_CONFIGURATION_4_WIRE\x10\x04\x12)\n$CHANNEL_INT32_RESISTANCE_UNITS1_OHMS\x10\x90Q\x126\n1CHANNEL_INT32_RESISTANCE_UNITS1_FROM_CUSTOM_SCALE\x10\xd1N\x12.\n)CHANNEL_INT32_RESISTANCE_UNITS1_FROM_TEDS\x10\xe4a\x12(\n#CHANNEL_INT32_RESOLUTION_TYPE1_BITS\x10\xfdN\x12:\n5CHANNEL_INT32_SAMP_CLK_OVERRUN_BEHAVIOR_REPEATED_DATA\x10\xbe}\x12;\n6CHANNEL_INT32_SAMP_CLK_OVERRUN_BEHAVIOR_SENTINEL_VALUE\x10\xbf}\x12V\nQCHANNEL_INT32_SAMPLE_CLOCK_ACTIVE_OR_INACTIVE_EDGE_SELECTION_SAMP_CLK_ACTIVE_EDGE\x10\x99r\x12X\nSCHANNEL_INT32_SAMPLE_CLOCK_ACTIVE_OR_INACTIVE_EDGE_SELECTION_SAMP_CLK_INACTIVE_EDGE\x10\x9ar\x12)\n$CHANNEL_INT32_SCALE_TYPE2_POLYNOMIAL\x10\xd1Q\x12$\n\x1fCHANNEL_INT32_SCALE_TYPE2_TABLE\x10\xd2Q\x12)\n$CHANNEL_INT32_SCALE_TYPE3_POLYNOMIAL\x10\xd1Q\x12$\n\x1fCHANNEL_INT32_SCALE_TYPE3_TABLE\x10\xd2Q\x12#\n\x1eCHANNEL_INT32_SCALE_TYPE3_NONE\x10\xf6O\x12#\n\x1eCHANNEL_INT32_SCALE_TYPE4_NONE\x10\xf6O\x12/\n*CHANNEL_INT32_SCALE_TYPE4_TWO_POINT_LINEAR\x10\x9a|\x12$\n\x1fCHANNEL_INT32_SCALE_TYPE4_TABLE\x10\xd2Q\x12)\n$CHANNEL_INT32_SCALE_TYPE4_POLYNOMIAL\x10\xd1Q\x12\x1e\n\x19CHANNEL_INT32_SENSE_LOCAL\x10\xdf}\x12\x1f\n\x1aCHANNEL_INT32_SENSE_REMOTE\x10\xe0}\x12-\n(CHANNEL_INT32_SENSOR_POWER_CFG_NO_CHANGE\x10\xb0O\x12+\n&CHANNEL_INT32_SENSOR_POWER_CFG_ENABLED\x10\x91~\x12,\n\'CHANNEL_INT32_SENSOR_POWER_CFG_DISABLED\x10\x92~\x12\'\n"CHANNEL_INT32_SENSOR_POWER_TYPE_DC\x10\xc2N\x12\'\n"CHANNEL_INT32_SENSOR_POWER_TYPE_AC\x10\xbdN\x12/\n*CHANNEL_INT32_SENSOR_POWER_TYPE_BIPOLAR_DC\x10\x93~\x12%\n CHANNEL_INT32_SHUNT_CAL_SELECT_A\x10\xe1a\x12%\n CHANNEL_INT32_SHUNT_CAL_SELECT_B\x10\xe2a\x12+\n&CHANNEL_INT32_SHUNT_CAL_SELECT_A_AND_B\x10\xe3a\x120\n+CHANNEL_INT32_SOUND_PRESSURE_UNITS1_PASCALS\x10\xe1N\x12:\n5CHANNEL_INT32_SOUND_PRESSURE_UNITS1_FROM_CUSTOM_SCALE\x10\xd1N\x12,\n\'CHANNEL_INT32_SOURCE_SELECTION_INTERNAL\x10\xd8O\x12,\n\'CHANNEL_INT32_SOURCE_SELECTION_EXTERNAL\x10\xb7O\x129\n4CHANNEL_INT32_STRAIN_GAGE_BRIDGE_TYPE1_FULL_BRIDGE_I\x10\xc7O\x12:\n5CHANNEL_INT32_STRAIN_GAGE_BRIDGE_TYPE1_FULL_BRIDGE_II\x10\xc8O\x12;\n6CHANNEL_INT32_STRAIN_GAGE_BRIDGE_TYPE1_FULL_BRIDGE_III\x10\xc9O\x129\n4CHANNEL_INT32_STRAIN_GAGE_BRIDGE_TYPE1_HALF_BRIDGE_I\x10\xccO\x12:\n5CHANNEL_INT32_STRAIN_GAGE_BRIDGE_TYPE1_HALF_BRIDGE_II\x10\xcdO\x12<\n7CHANNEL_INT32_STRAIN_GAGE_BRIDGE_TYPE1_QUARTER_BRIDGE_I\x10\x9fP\x12=\n8CHANNEL_INT32_STRAIN_GAGE_BRIDGE_TYPE1_QUARTER_BRIDGE_II\x10\xa0P\x12J\nECHANNEL_INT32_STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_PRINCIPAL_STRAIN_1\x10\xe3|\x12J\nECHANNEL_INT32_STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_PRINCIPAL_STRAIN_2\x10\xe4|\x12N\nICHANNEL_INT32_STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_PRINCIPAL_STRAIN_ANGLE\x10\xe5|\x12J\nECHANNEL_INT32_STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_CARTESIAN_STRAIN_X\x10\xe6|\x12J\nECHANNEL_INT32_STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_CARTESIAN_STRAIN_Y\x10\xe7|\x12Q\nLCHANNEL_INT32_STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_CARTESIAN_SHEAR_STRAIN_XY\x10\xe8|\x12H\nCCHANNEL_INT32_STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_MAX_SHEAR_STRAIN\x10\xe9|\x12N\nICHANNEL_INT32_STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_MAX_SHEAR_STRAIN_ANGLE\x10\xea|\x12?\n:CHANNEL_INT32_STRAIN_GAGE_ROSETTE_TYPE_RECTANGULAR_ROSETTE\x10\xe0|\x129\n4CHANNEL_INT32_STRAIN_GAGE_ROSETTE_TYPE_DELTA_ROSETTE\x10\xe1|\x127\n2CHANNEL_INT32_STRAIN_GAGE_ROSETTE_TYPE_TEE_ROSETTE\x10\xe2|\x12\'\n"CHANNEL_INT32_STRAIN_UNITS1_STRAIN\x10\xbbP\x122\n-CHANNEL_INT32_STRAIN_UNITS1_FROM_CUSTOM_SCALE\x10\xd1N\x12;\n6CHANNEL_INT32_SYNC_UNLOCK_BEHAVIOR_STOP_TASK_AND_ERROR\x10\xf6{\x12=\n8CHANNEL_INT32_SYNC_UNLOCK_BEHAVIOR_IGNORE_LOST_SYNC_LOCK\x10\x81~\x12+\n&CHANNEL_INT32_TEMPERATURE_UNITS1_DEG_C\x10\x9fO\x12+\n&CHANNEL_INT32_TEMPERATURE_UNITS1_DEG_F\x10\xa0O\x12-\n(CHANNEL_INT32_TEMPERATURE_UNITS1_KELVINS\x10\xd5P\x12+\n&CHANNEL_INT32_TEMPERATURE_UNITS1_DEG_R\x10\xa1O\x127\n2CHANNEL_INT32_TEMPERATURE_UNITS1_FROM_CUSTOM_SCALE\x10\xd1N\x12/\n*CHANNEL_INT32_THERMOCOUPLE_TYPE1_J_TYPE_TC\x10\xd8N\x12/\n*CHANNEL_INT32_THERMOCOUPLE_TYPE1_K_TYPE_TC\x10\xd9N\x12/\n*CHANNEL_INT32_THERMOCOUPLE_TYPE1_N_TYPE_TC\x10\xddN\x12/\n*CHANNEL_INT32_THERMOCOUPLE_TYPE1_R_TYPE_TC\x10\xe2N\x12/\n*CHANNEL_INT32_THERMOCOUPLE_TYPE1_S_TYPE_TC\x10\xe5N\x12/\n*CHANNEL_INT32_THERMOCOUPLE_TYPE1_T_TYPE_TC\x10\xe6N\x12/\n*CHANNEL_INT32_THERMOCOUPLE_TYPE1_B_TYPE_TC\x10\xbfN\x12/\n*CHANNEL_INT32_THERMOCOUPLE_TYPE1_E_TYPE_TC\x10\xc7N\x12/\n*CHANNEL_INT32_THERMOCOUPLE_TYPE1_A_TYPE_TC\x10\xd0~\x12/\n*CHANNEL_INT32_THERMOCOUPLE_TYPE1_C_TYPE_TC\x10\xd1~\x12%\n CHANNEL_INT32_TIME_UNITS_SECONDS\x10\xfcP\x12/\n*CHANNEL_INT32_TIME_UNITS_FROM_CUSTOM_SCALE\x10\xd1N\x12&\n!CHANNEL_INT32_TIME_UNITS2_SECONDS\x10\xfcP\x12&\n!CHANNEL_INT32_TIME_UNITS3_SECONDS\x10\xfcP\x12$\n\x1fCHANNEL_INT32_TIME_UNITS3_TICKS\x10\xc0P\x120\n+CHANNEL_INT32_TIME_UNITS3_FROM_CUSTOM_SCALE\x10\xd1N\x12 \n\x1bCHANNEL_INT32_TIMESCALE_TAI\x10\xf4|\x12 \n\x1bCHANNEL_INT32_TIMESCALE_UTC\x10\xf3|\x12-\n(CHANNEL_INT32_TORQUE_UNITS_NEWTON_METERS\x10\x89|\x12+\n&CHANNEL_INT32_TORQUE_UNITS_INCH_OUNCES\x10\x8a|\x12+\n&CHANNEL_INT32_TORQUE_UNITS_INCH_POUNDS\x10\x8b|\x12+\n&CHANNEL_INT32_TORQUE_UNITS_FOOT_POUNDS\x10\x8c|\x121\n,CHANNEL_INT32_TORQUE_UNITS_FROM_CUSTOM_SCALE\x10\xd1N\x12^\nYCHANNEL_INT32_VELOCITY_IEPE_SENSOR_SENSITIVITY_UNITS_MILLIVOLTS_PER_MILLIMETER_PER_SECOND\x10\xdb|\x12Y\nTCHANNEL_INT32_VELOCITY_IEPE_SENSOR_SENSITIVITY_UNITS_MILLI_VOLTS_PER_INCH_PER_SECOND\x10\xdc|\x123\n.CHANNEL_INT32_VELOCITY_UNITS_METERS_PER_SECOND\x10\xd7|\x123\n.CHANNEL_INT32_VELOCITY_UNITS_INCHES_PER_SECOND\x10\xd8|\x123\n.CHANNEL_INT32_VELOCITY_UNITS_FROM_CUSTOM_SCALE\x10\xd1N\x124\n/CHANNEL_INT32_VELOCITY_UNITS2_METERS_PER_SECOND\x10\xd7|\x126\n1CHANNEL_INT32_VELOCITY_UNITS2_KILOMETERS_PER_HOUR\x10\x87}\x122\n-CHANNEL_INT32_VELOCITY_UNITS2_FEET_PER_SECOND\x10\x88}\x121\n,CHANNEL_INT32_VELOCITY_UNITS2_MILES_PER_HOUR\x10\x89}\x12(\n#CHANNEL_INT32_VELOCITY_UNITS2_KNOTS\x10\x8a}\x124\n/CHANNEL_INT32_VELOCITY_UNITS2_FROM_CUSTOM_SCALE\x10\xd1N\x12\'\n"CHANNEL_INT32_VOLTAGE_UNITS1_VOLTS\x10\xecP\x123\n.CHANNEL_INT32_VOLTAGE_UNITS1_FROM_CUSTOM_SCALE\x10\xd1N\x12+\n&CHANNEL_INT32_VOLTAGE_UNITS1_FROM_TEDS\x10\xe4a\x12\'\n"CHANNEL_INT32_VOLTAGE_UNITS2_VOLTS\x10\xecP\x123\n.CHANNEL_INT32_VOLTAGE_UNITS2_FROM_CUSTOM_SCALE\x10\xd1N\x1a\x02\x10\x01*\xb92\n\x1aDeviceInt32AttributeValues\x12\x1c\n\x18DEVICE_INT32_UNSPECIFIED\x10\x00\x12-\n(DEVICE_INT32_AI_MEASUREMENT_TYPE_VOLTAGE\x10\xd2P\x121\n,DEVICE_INT32_AI_MEASUREMENT_TYPE_VOLTAGE_RMS\x10\xeeP\x12-\n(DEVICE_INT32_AI_MEASUREMENT_TYPE_CURRENT\x10\x96O\x121\n,DEVICE_INT32_AI_MEASUREMENT_TYPE_CURRENT_RMS\x10\xefP\x12D\n?DEVICE_INT32_AI_MEASUREMENT_TYPE_VOLTAGE_CUSTOM_WITH_EXCITATION\x10\xd3P\x12,\n\'DEVICE_INT32_AI_MEASUREMENT_TYPE_BRIDGE\x10\xa4|\x122\n-DEVICE_INT32_AI_MEASUREMENT_TYPE_FREQ_VOLTAGE\x10\xc5O\x120\n+DEVICE_INT32_AI_MEASUREMENT_TYPE_RESISTANCE\x10\xa6P\x12-\n(DEVICE_INT32_AI_MEASUREMENT_TYPE_TEMP_TC\x10\xbfP\x122\n-DEVICE_INT32_AI_MEASUREMENT_TYPE_TEMP_THRMSTR\x10\xbeP\x12.\n)DEVICE_INT32_AI_MEASUREMENT_TYPE_TEMP_RTD\x10\xbdP\x12:\n5DEVICE_INT32_AI_MEASUREMENT_TYPE_TEMP_BUILT_IN_SENSOR\x10\xc7P\x121\n,DEVICE_INT32_AI_MEASUREMENT_TYPE_STRAIN_GAGE\x10\xbcP\x129\n4DEVICE_INT32_AI_MEASUREMENT_TYPE_ROSETTE_STRAIN_GAGE\x10\xec|\x123\n.DEVICE_INT32_AI_MEASUREMENT_TYPE_POSITION_LVDT\x10\xf0P\x123\n.DEVICE_INT32_AI_MEASUREMENT_TYPE_POSITION_RVDT\x10\xf1P\x12K\nFDEVICE_INT32_AI_MEASUREMENT_TYPE_POSITION_EDDY_CURRENT_PROXIMITY_PROBE\x10\xf3s\x123\n.DEVICE_INT32_AI_MEASUREMENT_TYPE_ACCELEROMETER\x10\xf4P\x129\n4DEVICE_INT32_AI_MEASUREMENT_TYPE_ACCELERATION_CHARGE\x10\xe8}\x12D\n?DEVICE_INT32_AI_MEASUREMENT_TYPE_ACCELERATION_4_WIRE_DC_VOLTAGE\x10\xea}\x12:\n5DEVICE_INT32_AI_MEASUREMENT_TYPE_VELOCITY_IEPE_SENSOR\x10\xde|\x122\n-DEVICE_INT32_AI_MEASUREMENT_TYPE_FORCE_BRIDGE\x10\x9b|\x127\n2DEVICE_INT32_AI_MEASUREMENT_TYPE_FORCE_IEPE_SENSOR\x10\x97|\x125\n0DEVICE_INT32_AI_MEASUREMENT_TYPE_PRESSURE_BRIDGE\x10\x9e|\x12?\n:DEVICE_INT32_AI_MEASUREMENT_TYPE_SOUND_PRESSURE_MICROPHONE\x10\xf2P\x123\n.DEVICE_INT32_AI_MEASUREMENT_TYPE_TORQUE_BRIDGE\x10\xa1|\x121\n,DEVICE_INT32_AI_MEASUREMENT_TYPE_TEDS_SENSOR\x10\xf3a\x12,\n\'DEVICE_INT32_AI_MEASUREMENT_TYPE_CHARGE\x10\xe9}\x12+\n&DEVICE_INT32_AI_MEASUREMENT_TYPE_POWER\x10\xc9~\x126\n1DEVICE_INT32_AI_MEASUREMENT_TYPE_CALCULATED_POWER\x10\xcc~\x120\n+DEVICE_INT32_AO_OUTPUT_CHANNEL_TYPE_VOLTAGE\x10\xd2P\x120\n+DEVICE_INT32_AO_OUTPUT_CHANNEL_TYPE_CURRENT\x10\x96O\x121\n,DEVICE_INT32_AO_OUTPUT_CHANNEL_TYPE_FUNC_GEN\x10\x9es\x12/\n*DEVICE_INT32_ACQUISITION_TYPE_FINITE_SAMPS\x10\xc2O\x12-\n(DEVICE_INT32_ACQUISITION_TYPE_CONT_SAMPS\x10\x8bO\x128\n3DEVICE_INT32_ACQUISITION_TYPE_HW_TIMED_SINGLE_POINT\x10\xeaa\x12\x1d\n\x18DEVICE_INT32_ALT_REF_MSL\x10\x85}\x12\x1d\n\x18DEVICE_INT32_ALT_REF_HAE\x10\x86}\x12$\n\x1fDEVICE_INT32_ANT_STATUS_UNKNOWN\x10\xacb\x12#\n\x1eDEVICE_INT32_ANT_STATUS_NORMAL\x10\xdbQ\x12#\n\x1eDEVICE_INT32_ANT_STATUS_ABSENT\x10\xfa|\x12(\n#DEVICE_INT32_ANT_STATUS_OVERCURRENT\x10\xfb|\x12\x1e\n\x19DEVICE_INT32_BUS_TYPE_PCI\x10\xa6b\x12\x1f\n\x1aDEVICE_INT32_BUS_TYPE_PCIE\x10\xacj\x12\x1e\n\x19DEVICE_INT32_BUS_TYPE_PXI\x10\xa7b\x12\x1f\n\x1aDEVICE_INT32_BUS_TYPE_PXIE\x10\xf2r\x12\x1f\n\x1aDEVICE_INT32_BUS_TYPE_SCXI\x10\xa8b\x12\x1e\n\x19DEVICE_INT32_BUS_TYPE_SCC\x10\xf3r\x12"\n\x1dDEVICE_INT32_BUS_TYPE_PC_CARD\x10\xa9b\x12\x1e\n\x19DEVICE_INT32_BUS_TYPE_USB\x10\xaab\x12&\n!DEVICE_INT32_BUS_TYPE_COMPACT_DAQ\x10\xadr\x12&\n!DEVICE_INT32_BUS_TYPE_COMPACT_RIO\x10\x8f~\x12 \n\x1bDEVICE_INT32_BUS_TYPE_TCPIP\x10\xecs\x12"\n\x1dDEVICE_INT32_BUS_TYPE_UNKNOWN\x10\xacb\x12\'\n"DEVICE_INT32_BUS_TYPE_SWITCH_BLOCK\x10\xfe{\x121\n,DEVICE_INT32_CI_MEASUREMENT_TYPE_COUNT_EDGES\x10\x8dO\x12*\n%DEVICE_INT32_CI_MEASUREMENT_TYPE_FREQ\x10\xc3O\x12,\n\'DEVICE_INT32_CI_MEASUREMENT_TYPE_PERIOD\x10\x90P\x121\n,DEVICE_INT32_CI_MEASUREMENT_TYPE_PULSE_WIDTH\x10\xf7P\x121\n,DEVICE_INT32_CI_MEASUREMENT_TYPE_SEMI_PERIOD\x10\xb1P\x125\n0DEVICE_INT32_CI_MEASUREMENT_TYPE_PULSE_FREQUENCY\x10\xf8{\x120\n+DEVICE_INT32_CI_MEASUREMENT_TYPE_PULSE_TIME\x10\xf9{\x121\n,DEVICE_INT32_CI_MEASUREMENT_TYPE_PULSE_TICKS\x10\xfa{\x120\n+DEVICE_INT32_CI_MEASUREMENT_TYPE_DUTY_CYCLE\x10\xc6}\x12:\n5DEVICE_INT32_CI_MEASUREMENT_TYPE_POSITION_ANG_ENCODER\x10\xf8P\x12:\n5DEVICE_INT32_CI_MEASUREMENT_TYPE_POSITION_LIN_ENCODER\x10\xf9P\x12:\n5DEVICE_INT32_CI_MEASUREMENT_TYPE_VELOCITY_ANG_ENCODER\x10\xce}\x12:\n5DEVICE_INT32_CI_MEASUREMENT_TYPE_VELOCITY_LIN_ENCODER\x10\xcf}\x122\n-DEVICE_INT32_CI_MEASUREMENT_TYPE_TWO_EDGE_SEP\x10\x9bP\x123\n.DEVICE_INT32_CI_MEASUREMENT_TYPE_GPS_TIMESTAMP\x10\xfaP\x12+\n&DEVICE_INT32_CO_OUTPUT_TYPE_PULSE_TIME\x10\x9dP\x12+\n&DEVICE_INT32_CO_OUTPUT_TYPE_PULSE_FREQ\x10\x87O\x12,\n\'DEVICE_INT32_CO_OUTPUT_TYPE_PULSE_TICKS\x10\x9cP\x12"\n\x1eDEVICE_INT32_COUPLING_TYPES_AC\x10\x01\x12"\n\x1eDEVICE_INT32_COUPLING_TYPES_DC\x10\x02\x12&\n"DEVICE_INT32_COUPLING_TYPES_GROUND\x10\x04\x12)\n%DEVICE_INT32_COUPLING_TYPES_HF_REJECT\x10\x08\x12)\n%DEVICE_INT32_COUPLING_TYPES_LF_REJECT\x10\x10\x12,\n(DEVICE_INT32_COUPLING_TYPES_NOISE_REJECT\x10 \x12&\n!DEVICE_INT32_FILTER_TYPE2_LOWPASS\x10\xc7}\x12\'\n"DEVICE_INT32_FILTER_TYPE2_HIGHPASS\x10\xc8}\x12\'\n"DEVICE_INT32_FILTER_TYPE2_BANDPASS\x10\xc9}\x12$\n\x1fDEVICE_INT32_FILTER_TYPE2_NOTCH\x10\xca}\x12%\n DEVICE_INT32_FILTER_TYPE2_CUSTOM\x10\x99O\x122\n-DEVICE_INT32_ID_PIN_STATUS_MEMORY_NOT_PRESENT\x10\xcd~\x12.\n)DEVICE_INT32_ID_PIN_STATUS_MEMORY_PRESENT\x10\xce~\x12/\n*DEVICE_INT32_NAV_MEASUREMENT_TYPE_ALTITUDE\x10\xfd|\x120\n+DEVICE_INT32_NAV_MEASUREMENT_TYPE_LONGITUDE\x10\xfe|\x12/\n*DEVICE_INT32_NAV_MEASUREMENT_TYPE_LATITUDE\x10\xff|\x128\n3DEVICE_INT32_NAV_MEASUREMENT_TYPE_SPEED_OVER_GROUND\x10\x80}\x12,\n\'DEVICE_INT32_NAV_MEASUREMENT_TYPE_TRACK\x10\x81}\x120\n+DEVICE_INT32_NAV_MEASUREMENT_TYPE_TIMESTAMP\x10\xf2|\x124\n/DEVICE_INT32_NAV_MEASUREMENT_TYPE_VERT_VELOCITY\x10\x83}\x12!\n\x1cDEVICE_INT32_NAV_MODE_MOBILE\x10\xf5|\x121\n,DEVICE_INT32_NAV_MODE_STATIONARY_WITH_SURVEY\x10\xf6|\x12:\n5DEVICE_INT32_NAV_MODE_STATIONARY_WITH_PRESET_LOCATION\x10\xf7|\x12/\n*DEVICE_INT32_PRODUCT_CATEGORY_M_SERIES_DAQ\x10\xb3r\x12/\n*DEVICE_INT32_PRODUCT_CATEGORY_X_SERIES_DAQ\x10\xf2{\x12/\n*DEVICE_INT32_PRODUCT_CATEGORY_E_SERIES_DAQ\x10\xb2r\x12/\n*DEVICE_INT32_PRODUCT_CATEGORY_S_SERIES_DAQ\x10\xb4r\x12/\n*DEVICE_INT32_PRODUCT_CATEGORY_B_SERIES_DAQ\x10\xc6r\x120\n+DEVICE_INT32_PRODUCT_CATEGORY_SC_SERIES_DAQ\x10\xb5r\x12)\n$DEVICE_INT32_PRODUCT_CATEGORY_USBDAQ\x10\xb6r\x12,\n\'DEVICE_INT32_PRODUCT_CATEGORY_AO_SERIES\x10\xb7r\x12-\n(DEVICE_INT32_PRODUCT_CATEGORY_DIGITAL_IO\x10\xb8r\x12-\n(DEVICE_INT32_PRODUCT_CATEGORY_TIO_SERIES\x10\xc5r\x12=\n8DEVICE_INT32_PRODUCT_CATEGORY_DYNAMIC_SIGNAL_ACQUISITION\x10\xb9r\x12+\n&DEVICE_INT32_PRODUCT_CATEGORY_SWITCHES\x10\xbar\x126\n1DEVICE_INT32_PRODUCT_CATEGORY_COMPACT_DAQ_CHASSIS\x10\xc2r\x126\n1DEVICE_INT32_PRODUCT_CATEGORY_COMPACT_RIO_CHASSIS\x10\x90~\x122\n-DEVICE_INT32_PRODUCT_CATEGORY_C_SERIES_MODULE\x10\xc3r\x12.\n)DEVICE_INT32_PRODUCT_CATEGORY_SCXI_MODULE\x10\xc4r\x126\n1DEVICE_INT32_PRODUCT_CATEGORY_SCC_CONNECTOR_BLOCK\x10\xf0r\x12-\n(DEVICE_INT32_PRODUCT_CATEGORY_SCC_MODULE\x10\xf1r\x12*\n%DEVICE_INT32_PRODUCT_CATEGORY_NIELVIS\x10\xa3s\x12.\n)DEVICE_INT32_PRODUCT_CATEGORY_NETWORK_DAQ\x10\xeds\x12-\n(DEVICE_INT32_PRODUCT_CATEGORY_SC_EXPRESS\x10\x8e|\x12,\n\'DEVICE_INT32_PRODUCT_CATEGORY_FIELD_DAQ\x10\x97~\x125\n0DEVICE_INT32_PRODUCT_CATEGORY_TEST_SCALE_CHASSIS\x10\xb4~\x124\n/DEVICE_INT32_PRODUCT_CATEGORY_TEST_SCALE_MODULE\x10\xb5~\x12*\n%DEVICE_INT32_PRODUCT_CATEGORY_MIO_DAQ\x10\xb6~\x12*\n%DEVICE_INT32_PRODUCT_CATEGORY_UNKNOWN\x10\xacb\x12\'\n"DEVICE_INT32_TRIGGER_USAGE_ADVANCE\x10\xc8a\x12%\n DEVICE_INT32_TRIGGER_USAGE_PAUSE\x10\xc9a\x12)\n$DEVICE_INT32_TRIGGER_USAGE_REFERENCE\x10\xcaa\x12%\n DEVICE_INT32_TRIGGER_USAGE_START\x10\xcba\x12)\n$DEVICE_INT32_TRIGGER_USAGE_HANDSHAKE\x10\x95Q\x12)\n$DEVICE_INT32_TRIGGER_USAGE_ARM_START\x10\xb1r\x12,\n(DEVICE_INT32_TRIGGER_USAGE_TYPES_ADVANCE\x10\x01\x12*\n&DEVICE_INT32_TRIGGER_USAGE_TYPES_PAUSE\x10\x02\x12.\n*DEVICE_INT32_TRIGGER_USAGE_TYPES_REFERENCE\x10\x04\x12*\n&DEVICE_INT32_TRIGGER_USAGE_TYPES_START\x10\x08\x12.\n*DEVICE_INT32_TRIGGER_USAGE_TYPES_HANDSHAKE\x10\x10\x12.\n*DEVICE_INT32_TRIGGER_USAGE_TYPES_ARM_START\x10 \x1a\x02\x10\x01*\xc3\x08\n ExportSignalInt32AttributeValues\x12"\n\x1eEXPORTSIGNAL_INT32_UNSPECIFIED\x10\x00\x12H\nCEXPORTSIGNAL_INT32_DEASSERT_CONDITION_ONBRD_MEM_MORE_THAN_HALF_FULL\x10\xfdO\x129\n4EXPORTSIGNAL_INT32_DEASSERT_CONDITION_ONBRD_MEM_FULL\x10\xfcO\x12E\n@EXPORTSIGNAL_INT32_DEASSERT_CONDITION_ONBRD_MEM_CUSTOM_THRESHOLD\x10\xa1b\x12=\n8EXPORTSIGNAL_INT32_DIGITAL_WIDTH_UNITS1_SAMP_CLK_PERIODS\x10\xaeP\x124\n/EXPORTSIGNAL_INT32_DIGITAL_WIDTH_UNITS1_SECONDS\x10\xfcP\x122\n-EXPORTSIGNAL_INT32_DIGITAL_WIDTH_UNITS1_TICKS\x10\xc0P\x124\n/EXPORTSIGNAL_INT32_DIGITAL_WIDTH_UNITS3_SECONDS\x10\xfcP\x12,\n\'EXPORTSIGNAL_INT32_EXPORT_ACTIONS_PULSE\x10\x99P\x12-\n(EXPORTSIGNAL_INT32_EXPORT_ACTIONS_TOGGLE\x10\xc3P\x12*\n%EXPORTSIGNAL_INT32_EXPORT_ACTIONS_LVL\x10\xe2O\x12-\n(EXPORTSIGNAL_INT32_EXPORT_ACTIONS2_PULSE\x10\x99P\x12.\n)EXPORTSIGNAL_INT32_EXPORT_ACTIONS2_TOGGLE\x10\xc3P\x12-\n(EXPORTSIGNAL_INT32_EXPORT_ACTIONS3_PULSE\x10\x99P\x12+\n&EXPORTSIGNAL_INT32_EXPORT_ACTIONS3_LVL\x10\xe2O\x123\n.EXPORTSIGNAL_INT32_EXPORT_ACTIONS5_INTERLOCKED\x10\x85b\x12-\n(EXPORTSIGNAL_INT32_EXPORT_ACTIONS5_PULSE\x10\x99P\x12#\n\x1eEXPORTSIGNAL_INT32_LEVEL1_HIGH\x10\xd0O\x12"\n\x1dEXPORTSIGNAL_INT32_LEVEL1_LOW\x10\xe6O\x12-\n(EXPORTSIGNAL_INT32_POLARITY2_ACTIVE_HIGH\x10\xefN\x12,\n\'EXPORTSIGNAL_INT32_POLARITY2_ACTIVE_LOW\x10\xf0N\x1a\x02\x10\x01*\xe5#\n#PhysicalChannelInt32AttributeValues\x12%\n!PHYSICALCHANNEL_INT32_UNSPECIFIED\x10\x00\x126\n1PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_VOLTAGE\x10\xd2P\x12:\n5PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_VOLTAGE_RMS\x10\xeeP\x126\n1PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_CURRENT\x10\x96O\x12:\n5PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_CURRENT_RMS\x10\xefP\x12M\nHPHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_VOLTAGE_CUSTOM_WITH_EXCITATION\x10\xd3P\x125\n0PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_BRIDGE\x10\xa4|\x12;\n6PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_FREQ_VOLTAGE\x10\xc5O\x129\n4PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_RESISTANCE\x10\xa6P\x126\n1PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_TEMP_TC\x10\xbfP\x12;\n6PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_TEMP_THRMSTR\x10\xbeP\x127\n2PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_TEMP_RTD\x10\xbdP\x12C\n>PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_TEMP_BUILT_IN_SENSOR\x10\xc7P\x12:\n5PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_STRAIN_GAGE\x10\xbcP\x12B\n=PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_ROSETTE_STRAIN_GAGE\x10\xec|\x12<\n7PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_POSITION_LVDT\x10\xf0P\x12<\n7PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_POSITION_RVDT\x10\xf1P\x12T\nOPHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_POSITION_EDDY_CURRENT_PROXIMITY_PROBE\x10\xf3s\x12<\n7PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_ACCELEROMETER\x10\xf4P\x12B\n=PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_ACCELERATION_CHARGE\x10\xe8}\x12M\nHPHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_ACCELERATION_4_WIRE_DC_VOLTAGE\x10\xea}\x12C\n>PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_VELOCITY_IEPE_SENSOR\x10\xde|\x12;\n6PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_FORCE_BRIDGE\x10\x9b|\x12@\n;PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_FORCE_IEPE_SENSOR\x10\x97|\x12>\n9PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_PRESSURE_BRIDGE\x10\x9e|\x12H\nCPHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_SOUND_PRESSURE_MICROPHONE\x10\xf2P\x12<\n7PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_TORQUE_BRIDGE\x10\xa1|\x12:\n5PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_TEDS_SENSOR\x10\xf3a\x125\n0PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_CHARGE\x10\xe9}\x124\n/PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_POWER\x10\xc9~\x12?\n:PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_CALCULATED_POWER\x10\xcc~\x129\n4PHYSICALCHANNEL_INT32_AO_OUTPUT_CHANNEL_TYPE_VOLTAGE\x10\xd2P\x129\n4PHYSICALCHANNEL_INT32_AO_OUTPUT_CHANNEL_TYPE_CURRENT\x10\x96O\x12:\n5PHYSICALCHANNEL_INT32_AO_OUTPUT_CHANNEL_TYPE_FUNC_GEN\x10\x9es\x12>\n9PHYSICALCHANNEL_INT32_AO_POWER_UP_OUTPUT_BEHAVIOR_VOLTAGE\x10\xd2P\x12>\n9PHYSICALCHANNEL_INT32_AO_POWER_UP_OUTPUT_BEHAVIOR_CURRENT\x10\x96O\x12E\n@PHYSICALCHANNEL_INT32_AO_POWER_UP_OUTPUT_BEHAVIOR_HIGH_IMPEDANCE\x10\xefa\x128\n3PHYSICALCHANNEL_INT32_ACQUISITION_TYPE_FINITE_SAMPS\x10\xc2O\x126\n1PHYSICALCHANNEL_INT32_ACQUISITION_TYPE_CONT_SAMPS\x10\x8bO\x12A\n<PHYSICALCHANNEL_INT32_ACQUISITION_TYPE_HW_TIMED_SINGLE_POINT\x10\xeaa\x12:\n5PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_COUNT_EDGES\x10\x8dO\x123\n.PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_FREQ\x10\xc3O\x125\n0PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_PERIOD\x10\x90P\x12:\n5PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_PULSE_WIDTH\x10\xf7P\x12:\n5PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_SEMI_PERIOD\x10\xb1P\x12>\n9PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_PULSE_FREQUENCY\x10\xf8{\x129\n4PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_PULSE_TIME\x10\xf9{\x12:\n5PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_PULSE_TICKS\x10\xfa{\x129\n4PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_DUTY_CYCLE\x10\xc6}\x12C\n>PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_POSITION_ANG_ENCODER\x10\xf8P\x12C\n>PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_POSITION_LIN_ENCODER\x10\xf9P\x12C\n>PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_VELOCITY_ANG_ENCODER\x10\xce}\x12C\n>PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_VELOCITY_LIN_ENCODER\x10\xcf}\x12;\n6PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_TWO_EDGE_SEP\x10\x9bP\x12<\n7PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_GPS_TIMESTAMP\x10\xfaP\x124\n/PHYSICALCHANNEL_INT32_CO_OUTPUT_TYPE_PULSE_TIME\x10\x9dP\x124\n/PHYSICALCHANNEL_INT32_CO_OUTPUT_TYPE_PULSE_FREQ\x10\x87O\x125\n0PHYSICALCHANNEL_INT32_CO_OUTPUT_TYPE_PULSE_TICKS\x10\x9cP\x122\n-PHYSICALCHANNEL_INT32_LOGIC_FAMILY_1POINT_8_V\x10\xb8~\x122\n-PHYSICALCHANNEL_INT32_LOGIC_FAMILY_2POINT_5_V\x10\x9cr\x122\n-PHYSICALCHANNEL_INT32_LOGIC_FAMILY_3POINT_3_V\x10\x9dr\x12+\n&PHYSICALCHANNEL_INT32_LOGIC_FAMILY_5_V\x10\x9br\x128\n3PHYSICALCHANNEL_INT32_NAV_MEASUREMENT_TYPE_ALTITUDE\x10\xfd|\x129\n4PHYSICALCHANNEL_INT32_NAV_MEASUREMENT_TYPE_LONGITUDE\x10\xfe|\x128\n3PHYSICALCHANNEL_INT32_NAV_MEASUREMENT_TYPE_LATITUDE\x10\xff|\x12A\n<PHYSICALCHANNEL_INT32_NAV_MEASUREMENT_TYPE_SPEED_OVER_GROUND\x10\x80}\x125\n0PHYSICALCHANNEL_INT32_NAV_MEASUREMENT_TYPE_TRACK\x10\x81}\x129\n4PHYSICALCHANNEL_INT32_NAV_MEASUREMENT_TYPE_TIMESTAMP\x10\xf2|\x12=\n8PHYSICALCHANNEL_INT32_NAV_MEASUREMENT_TYPE_VERT_VELOCITY\x10\x83}\x12/\n*PHYSICALCHANNEL_INT32_SENSOR_POWER_TYPE_DC\x10\xc2N\x12/\n*PHYSICALCHANNEL_INT32_SENSOR_POWER_TYPE_AC\x10\xbdN\x127\n2PHYSICALCHANNEL_INT32_SENSOR_POWER_TYPE_BIPOLAR_DC\x10\x93~\x12&\n"PHYSICALCHANNEL_INT32_TERM_CFG_RSE\x10\x01\x12\'\n#PHYSICALCHANNEL_INT32_TERM_CFG_NRSE\x10\x02\x12\'\n#PHYSICALCHANNEL_INT32_TERM_CFG_DIFF\x10\x04\x12.\n*PHYSICALCHANNEL_INT32_TERM_CFG_PSEUDO_DIFF\x10\x08\x1a\x02\x10\x01*\xd7\x06\n\x18ReadInt32AttributeValues\x12\x1a\n\x16READ_INT32_UNSPECIFIED\x10\x00\x12 \n\x1bREAD_INT32_LOGGING_MODE_OFF\x10\xf7O\x12 \n\x1bREAD_INT32_LOGGING_MODE_LOG\x10\xe4{\x12)\n$READ_INT32_LOGGING_MODE_LOG_AND_READ\x10\xe2{\x12&\n!READ_INT32_LOGGING_OPERATION_OPEN\x10\xc5Q\x120\n+READ_INT32_LOGGING_OPERATION_OPEN_OR_CREATE\x10\xe6{\x123\n.READ_INT32_LOGGING_OPERATION_CREATE_OR_REPLACE\x10\xe7{\x12(\n#READ_INT32_LOGGING_OPERATION_CREATE\x10\xe8{\x126\n1READ_INT32_OVERWRITE_MODE1_OVERWRITE_UNREAD_SAMPS\x10\x8cP\x12=\n8READ_INT32_OVERWRITE_MODE1_DO_NOT_OVERWRITE_UNREAD_SAMPS\x10\xafO\x12-\n(READ_INT32_READ_RELATIVE_TO_FIRST_SAMPLE\x10\xb8Q\x12.\n)READ_INT32_READ_RELATIVE_TO_CURR_READ_POS\x10\xb9Q\x12)\n$READ_INT32_READ_RELATIVE_TO_REF_TRIG\x10\xbaQ\x123\n.READ_INT32_READ_RELATIVE_TO_FIRST_PRETRIG_SAMP\x10\xbbQ\x121\n,READ_INT32_READ_RELATIVE_TO_MOST_RECENT_SAMP\x10\xbcQ\x12,\n\'READ_INT32_WAIT_MODE_WAIT_FOR_INTERRUPT\x10\xeba\x12\x1e\n\x19READ_INT32_WAIT_MODE_POLL\x10\xeca\x12\x1f\n\x1aREAD_INT32_WAIT_MODE_YIELD\x10\xeda\x12\x1f\n\x1aREAD_INT32_WAIT_MODE_SLEEP\x10\x83b*\xf2\x01\n\x1cRealTimeInt32AttributeValues\x12\x1e\n\x1aREALTIME_INT32_UNSPECIFIED\x10\x00\x121\n,REALTIME_INT32_WAIT_MODE3_WAIT_FOR_INTERRUPT\x10\xeba\x12#\n\x1eREALTIME_INT32_WAIT_MODE3_POLL\x10\xeca\x121\n,REALTIME_INT32_WAIT_MODE4_WAIT_FOR_INTERRUPT\x10\xeba\x12#\n\x1eREALTIME_INT32_WAIT_MODE4_POLL\x10\xeca\x1a\x02\x10\x01*\x99\x0f\n\x19ScaleInt32AttributeValues\x12\x1b\n\x17SCALE_INT32_UNSPECIFIED\x10\x00\x12"\n\x1dSCALE_INT32_SCALE_TYPE_LINEAR\x10\xcfQ\x12&\n!SCALE_INT32_SCALE_TYPE_MAP_RANGES\x10\xd0Q\x12&\n!SCALE_INT32_SCALE_TYPE_POLYNOMIAL\x10\xd1Q\x12!\n\x1cSCALE_INT32_SCALE_TYPE_TABLE\x10\xd2Q\x12\'\n"SCALE_INT32_UNITS_PRE_SCALED_VOLTS\x10\xecP\x12&\n!SCALE_INT32_UNITS_PRE_SCALED_AMPS\x10\xe6P\x12\'\n"SCALE_INT32_UNITS_PRE_SCALED_DEG_F\x10\xa0O\x12\'\n"SCALE_INT32_UNITS_PRE_SCALED_DEG_C\x10\x9fO\x12\'\n"SCALE_INT32_UNITS_PRE_SCALED_DEG_R\x10\xa1O\x12)\n$SCALE_INT32_UNITS_PRE_SCALED_KELVINS\x10\xd5P\x12(\n#SCALE_INT32_UNITS_PRE_SCALED_STRAIN\x10\xbbP\x12&\n!SCALE_INT32_UNITS_PRE_SCALED_OHMS\x10\x90Q\x12$\n\x1fSCALE_INT32_UNITS_PRE_SCALED_HZ\x10\x85Q\x12)\n$SCALE_INT32_UNITS_PRE_SCALED_SECONDS\x10\xfcP\x12(\n#SCALE_INT32_UNITS_PRE_SCALED_METERS\x10\xebO\x12(\n#SCALE_INT32_UNITS_PRE_SCALED_INCHES\x10\x8bQ\x12)\n$SCALE_INT32_UNITS_PRE_SCALED_DEGREES\x10\xa2O\x12)\n$SCALE_INT32_UNITS_PRE_SCALED_RADIANS\x10\xa1P\x12\'\n"SCALE_INT32_UNITS_PRE_SCALED_TICKS\x10\xc0P\x12%\n SCALE_INT32_UNITS_PRE_SCALED_RPM\x10\xd0}\x124\n/SCALE_INT32_UNITS_PRE_SCALED_RADIANS_PER_SECOND\x10\xd1}\x124\n/SCALE_INT32_UNITS_PRE_SCALED_DEGREES_PER_SECOND\x10\xd2}\x12#\n\x1eSCALE_INT32_UNITS_PRE_SCALED_G\x10\xcaO\x12;\n6SCALE_INT32_UNITS_PRE_SCALED_METERS_PER_SECOND_SQUARED\x10\xb6a\x12;\n6SCALE_INT32_UNITS_PRE_SCALED_INCHES_PER_SECOND_SQUARED\x10\xb7a\x123\n.SCALE_INT32_UNITS_PRE_SCALED_METERS_PER_SECOND\x10\xd7|\x123\n.SCALE_INT32_UNITS_PRE_SCALED_INCHES_PER_SECOND\x10\xd8|\x12)\n$SCALE_INT32_UNITS_PRE_SCALED_PASCALS\x10\xe1N\x12)\n$SCALE_INT32_UNITS_PRE_SCALED_NEWTONS\x10\x83|\x12(\n#SCALE_INT32_UNITS_PRE_SCALED_POUNDS\x10\x84|\x120\n+SCALE_INT32_UNITS_PRE_SCALED_KILOGRAM_FORCE\x10\x85|\x128\n3SCALE_INT32_UNITS_PRE_SCALED_POUNDS_PER_SQUARE_INCH\x10\x87|\x12%\n SCALE_INT32_UNITS_PRE_SCALED_BAR\x10\x88|\x12/\n*SCALE_INT32_UNITS_PRE_SCALED_NEWTON_METERS\x10\x89|\x12-\n(SCALE_INT32_UNITS_PRE_SCALED_INCH_OUNCES\x10\x8a|\x12-\n(SCALE_INT32_UNITS_PRE_SCALED_INCH_POUNDS\x10\x8b|\x12-\n(SCALE_INT32_UNITS_PRE_SCALED_FOOT_POUNDS\x10\x8c|\x120\n+SCALE_INT32_UNITS_PRE_SCALED_VOLTS_PER_VOLT\x10\x98|\x122\n-SCALE_INT32_UNITS_PRE_SCALED_M_VOLTS_PER_VOLT\x10\x99|\x12*\n%SCALE_INT32_UNITS_PRE_SCALED_COULOMBS\x10\xe6}\x12/\n*SCALE_INT32_UNITS_PRE_SCALED_PICO_COULOMBS\x10\xe7}\x12+\n&SCALE_INT32_UNITS_PRE_SCALED_FROM_TEDS\x10\xe4a*\xd5\x0e\n\x1aTimingInt32AttributeValues\x12\x1c\n\x18TIMING_INT32_UNSPECIFIED\x10\x00\x12/\n*TIMING_INT32_ACQUISITION_TYPE_FINITE_SAMPS\x10\xc2O\x12-\n(TIMING_INT32_ACQUISITION_TYPE_CONT_SAMPS\x10\x8bO\x128\n3TIMING_INT32_ACQUISITION_TYPE_HW_TIMED_SINGLE_POINT\x10\xeaa\x12.\n)TIMING_INT32_DIGITAL_WIDTH_UNITS2_SECONDS\x10\xfcP\x12,\n\'TIMING_INT32_DIGITAL_WIDTH_UNITS2_TICKS\x10\xc0P\x12\x1e\n\x19TIMING_INT32_EDGE1_RISING\x10\xa8P\x12\x1f\n\x1aTIMING_INT32_EDGE1_FALLING\x10\xbbO\x125\n0TIMING_INT32_HANDSHAKE_START_CONDITION_IMMEDIATE\x10\xd6O\x12M\nHTIMING_INT32_HANDSHAKE_START_CONDITION_WAIT_FOR_HANDSHAKE_TRIGGER_ASSERT\x10\x86b\x12O\nJTIMING_INT32_HANDSHAKE_START_CONDITION_WAIT_FOR_HANDSHAKE_TRIGGER_DEASSERT\x10\x87b\x12<\n7TIMING_INT32_MIOAI_CONVERT_TB_SRC_SAME_AS_SAMP_TIMEBASE\x10\xacP\x12>\n9TIMING_INT32_MIOAI_CONVERT_TB_SRC_SAME_AS_MASTER_TIMEBASE\x10\xaaP\x127\n2TIMING_INT32_MIOAI_CONVERT_TB_SRC_100_MHZ_TIMEBASE\x10\xf1{\x126\n1TIMING_INT32_MIOAI_CONVERT_TB_SRC_80_MHZ_TIMEBASE\x10\xacr\x126\n1TIMING_INT32_MIOAI_CONVERT_TB_SRC_20_MHZ_TIMEBASE\x10\xf9a\x125\n0TIMING_INT32_MIOAI_CONVERT_TB_SRC_8_MHZ_TIMEBASE\x10\x97}\x127\n2TIMING_INT32_OVERFLOW_BEHAVIOR_STOP_TASK_AND_ERROR\x10\xf6{\x123\n.TIMING_INT32_OVERFLOW_BEHAVIOR_IGNORE_OVERRUNS\x10\xf7{\x12B\n=TIMING_INT32_SAMPLE_INPUT_DATA_WHEN_HANDSHAKE_TRIGGER_ASSERTS\x10\x88b\x12D\n?TIMING_INT32_SAMPLE_INPUT_DATA_WHEN_HANDSHAKE_TRIGGER_DEASSERTS\x10\x89b\x12-\n(TIMING_INT32_SAMPLE_TIMING_TYPE_SAMP_CLK\x10\x94Q\x124\n/TIMING_INT32_SAMPLE_TIMING_TYPE_BURST_HANDSHAKE\x10\x84b\x12.\n)TIMING_INT32_SAMPLE_TIMING_TYPE_HANDSHAKE\x10\x95Q\x12-\n(TIMING_INT32_SAMPLE_TIMING_TYPE_IMPLICIT\x10\xd3Q\x12.\n)TIMING_INT32_SAMPLE_TIMING_TYPE_ON_DEMAND\x10\x96Q\x125\n0TIMING_INT32_SAMPLE_TIMING_TYPE_CHANGE_DETECTION\x10\xd8a\x127\n2TIMING_INT32_SAMPLE_TIMING_TYPE_PIPELINED_SAMP_CLK\x10\xccr\x12)\n$TIMING_INT32_SYNC_PULSE_TYPE_ONBOARD\x10\x80~\x12*\n%TIMING_INT32_SYNC_PULSE_TYPE_DIG_EDGE\x10\xa6O\x12&\n!TIMING_INT32_SYNC_PULSE_TYPE_TIME\x10\xfc|\x12&\n!TIMING_INT32_TIMESCALE2_HOST_TIME\x10\xfe}\x12+\n&TIMING_INT32_TIMESCALE2_IO_DEVICE_TIME\x10\xff}\x12:\n5TIMING_INT32_UNDERFLOW_BEHAVIOR_HALT_OUTPUT_AND_ERROR\x10\x97r\x12?\n:TIMING_INT32_UNDERFLOW_BEHAVIOR_PAUSE_UNTIL_DATA_AVAILABLE\x10\x98r*\xfc\x11\n\x1bTriggerInt32AttributeValues\x12\x1d\n\x19TRIGGER_INT32_UNSPECIFIED\x10\x00\x12)\n$TRIGGER_INT32_ACTIVE_LEVEL_ABOVE_LVL\x10\xedN\x12)\n$TRIGGER_INT32_ACTIVE_LEVEL_BELOW_LVL\x10\xfbN\x12\x1f\n\x1aTRIGGER_INT32_COUPLING2_AC\x10\xbdN\x12\x1f\n\x1aTRIGGER_INT32_COUPLING2_DC\x10\xc2N\x12=\n8TRIGGER_INT32_DIGITAL_PATTERN_CONDITION1_PATTERN_MATCHES\x10\x8eP\x12D\n?TRIGGER_INT32_DIGITAL_PATTERN_CONDITION1_PATTERN_DOES_NOT_MATCH\x10\x8dP\x128\n3TRIGGER_INT32_DIGITAL_WIDTH_UNITS1_SAMP_CLK_PERIODS\x10\xaeP\x12/\n*TRIGGER_INT32_DIGITAL_WIDTH_UNITS1_SECONDS\x10\xfcP\x12-\n(TRIGGER_INT32_DIGITAL_WIDTH_UNITS1_TICKS\x10\xc0P\x12\x1f\n\x1aTRIGGER_INT32_EDGE1_RISING\x10\xa8P\x12 \n\x1bTRIGGER_INT32_EDGE1_FALLING\x10\xbbO\x12\x1e\n\x19TRIGGER_INT32_LEVEL1_HIGH\x10\xd0O\x12\x1d\n\x18TRIGGER_INT32_LEVEL1_LOW\x10\xe6O\x12&\n!TRIGGER_INT32_SLOPE1_RISING_SLOPE\x10\xa8P\x12\'\n"TRIGGER_INT32_SLOPE1_FALLING_SLOPE\x10\xbbO\x12!\n\x1cTRIGGER_INT32_SYNC_TYPE_NONE\x10\xf6O\x12#\n\x1eTRIGGER_INT32_SYNC_TYPE_MASTER\x10\x90|\x12"\n\x1dTRIGGER_INT32_SYNC_TYPE_SLAVE\x10\x91|\x12\'\n"TRIGGER_INT32_TIMESCALE2_HOST_TIME\x10\xfe}\x12,\n\'TRIGGER_INT32_TIMESCALE2_IO_DEVICE_TIME\x10\xff}\x12+\n&TRIGGER_INT32_TRIGGER_TYPE10_ANLG_EDGE\x10\xf3N\x121\n,TRIGGER_INT32_TRIGGER_TYPE10_ANLG_MULTI_EDGE\x10\xec}\x12*\n%TRIGGER_INT32_TRIGGER_TYPE10_DIG_EDGE\x10\xa6O\x12-\n(TRIGGER_INT32_TRIGGER_TYPE10_DIG_PATTERN\x10\x9eQ\x12*\n%TRIGGER_INT32_TRIGGER_TYPE10_ANLG_WIN\x10\xf7N\x12&\n!TRIGGER_INT32_TRIGGER_TYPE10_TIME\x10\xfc|\x12&\n!TRIGGER_INT32_TRIGGER_TYPE10_NONE\x10\xf6O\x12)\n$TRIGGER_INT32_TRIGGER_TYPE4_DIG_EDGE\x10\xa6O\x12%\n TRIGGER_INT32_TRIGGER_TYPE4_TIME\x10\xfc|\x12%\n TRIGGER_INT32_TRIGGER_TYPE4_NONE\x10\xf6O\x12)\n$TRIGGER_INT32_TRIGGER_TYPE5_DIG_EDGE\x10\xa6O\x12)\n$TRIGGER_INT32_TRIGGER_TYPE5_SOFTWARE\x10\xb4P\x12%\n TRIGGER_INT32_TRIGGER_TYPE5_NONE\x10\xf6O\x12)\n$TRIGGER_INT32_TRIGGER_TYPE6_ANLG_LVL\x10\xf5N\x12)\n$TRIGGER_INT32_TRIGGER_TYPE6_ANLG_WIN\x10\xf7N\x12(\n#TRIGGER_INT32_TRIGGER_TYPE6_DIG_LVL\x10\xa8O\x12,\n\'TRIGGER_INT32_TRIGGER_TYPE6_DIG_PATTERN\x10\x9eQ\x12%\n TRIGGER_INT32_TRIGGER_TYPE6_NONE\x10\xf6O\x12*\n%TRIGGER_INT32_TRIGGER_TYPE8_ANLG_EDGE\x10\xf3N\x120\n+TRIGGER_INT32_TRIGGER_TYPE8_ANLG_MULTI_EDGE\x10\xec}\x12)\n$TRIGGER_INT32_TRIGGER_TYPE8_DIG_EDGE\x10\xa6O\x12,\n\'TRIGGER_INT32_TRIGGER_TYPE8_DIG_PATTERN\x10\x9eQ\x12)\n$TRIGGER_INT32_TRIGGER_TYPE8_ANLG_WIN\x10\xf7N\x12%\n TRIGGER_INT32_TRIGGER_TYPE8_TIME\x10\xfc|\x12%\n TRIGGER_INT32_TRIGGER_TYPE8_NONE\x10\xf6O\x12,\n\'TRIGGER_INT32_TRIGGER_TYPE9_INTERLOCKED\x10\x85b\x12%\n TRIGGER_INT32_TRIGGER_TYPE9_NONE\x10\xf6O\x129\n4TRIGGER_INT32_WINDOW_TRIGGER_CONDITION1_ENTERING_WIN\x10\xb3O\x128\n3TRIGGER_INT32_WINDOW_TRIGGER_CONDITION1_LEAVING_WIN\x10\xe0O\x127\n2TRIGGER_INT32_WINDOW_TRIGGER_CONDITION2_INSIDE_WIN\x10\xd7O\x128\n3TRIGGER_INT32_WINDOW_TRIGGER_CONDITION2_OUTSIDE_WIN\x10\x8bP\x1a\x02\x10\x01*\xfa\x05\n\x1cWatchdogInt32AttributeValues\x12\x1e\n\x1aWATCHDOG_INT32_UNSPECIFIED\x10\x00\x12+\n&WATCHDOG_INT32_DIGITAL_LINE_STATE_HIGH\x10\xd0O\x12*\n%WATCHDOG_INT32_DIGITAL_LINE_STATE_LOW\x10\xe6O\x12/\n*WATCHDOG_INT32_DIGITAL_LINE_STATE_TRISTATE\x10\xc6P\x120\n+WATCHDOG_INT32_DIGITAL_LINE_STATE_NO_CHANGE\x10\xb0O\x12 \n\x1bWATCHDOG_INT32_EDGE1_RISING\x10\xa8P\x12!\n\x1cWATCHDOG_INT32_EDGE1_FALLING\x10\xbbO\x12*\n%WATCHDOG_INT32_TRIGGER_TYPE4_DIG_EDGE\x10\xa6O\x12&\n!WATCHDOG_INT32_TRIGGER_TYPE4_TIME\x10\xfc|\x12&\n!WATCHDOG_INT32_TRIGGER_TYPE4_NONE\x10\xf6O\x123\n.WATCHDOG_INT32_WATCHDOG_AO_EXPIR_STATE_VOLTAGE\x10\xd2P\x123\n.WATCHDOG_INT32_WATCHDOG_AO_EXPIR_STATE_CURRENT\x10\x96O\x125\n0WATCHDOG_INT32_WATCHDOG_AO_EXPIR_STATE_NO_CHANGE\x10\xb0O\x12/\n*WATCHDOG_INT32_WATCHDOG_CO_EXPIR_STATE_LOW\x10\xe6O\x120\n+WATCHDOG_INT32_WATCHDOG_CO_EXPIR_STATE_HIGH\x10\xd0O\x125\n0WATCHDOG_INT32_WATCHDOG_CO_EXPIR_STATE_NO_CHANGE\x10\xb0O\x1a\x02\x10\x01*\xed\x02\n\x19WriteInt32AttributeValues\x12\x1b\n\x17WRITE_INT32_UNSPECIFIED\x10\x00\x12/\n*WRITE_INT32_REGENERATION_MODE1_ALLOW_REGEN\x10\xf1N\x126\n1WRITE_INT32_REGENERATION_MODE1_DO_NOT_ALLOW_REGEN\x10\xaeO\x12 \n\x1bWRITE_INT32_WAIT_MODE2_POLL\x10\xeca\x12!\n\x1cWRITE_INT32_WAIT_MODE2_YIELD\x10\xeda\x12!\n\x1cWRITE_INT32_WAIT_MODE2_SLEEP\x10\x83b\x12/\n*WRITE_INT32_WRITE_RELATIVE_TO_FIRST_SAMPLE\x10\xb8Q\x121\n,WRITE_INT32_WRITE_RELATIVE_TO_CURR_WRITE_POS\x10\xbeQ2\xaa\x9b\x03\n\x07NiDAQmx\x12p\n\x15AddCDAQSyncConnection\x12*.nidaqmx_grpc.AddCDAQSyncConnectionRequest\x1a+.nidaqmx_grpc.AddCDAQSyncConnectionResponse\x12m\n\x14AddGlobalChansToTask\x12).nidaqmx_grpc.AddGlobalChansToTaskRequest\x1a*.nidaqmx_grpc.AddGlobalChansToTaskResponse\x12a\n\x10AddNetworkDevice\x12%.nidaqmx_grpc.AddNetworkDeviceRequest\x1a&.nidaqmx_grpc.AddNetworkDeviceResponse\x12\xa3\x01\n&AreConfiguredCDAQSyncPortsDisconnected\x12;.nidaqmx_grpc.AreConfiguredCDAQSyncPortsDisconnectedRequest\x1a<.nidaqmx_grpc.AreConfiguredCDAQSyncPortsDisconnectedResponse\x12\x91\x01\n AutoConfigureCDAQSyncConnections\x125.nidaqmx_grpc.AutoConfigureCDAQSyncConnectionsRequest\x1a6.nidaqmx_grpc.AutoConfigureCDAQSyncConnectionsResponse\x12|\n\x19CalculateReversePolyCoeff\x12..nidaqmx_grpc.CalculateReversePolyCoeffRequest\x1a/.nidaqmx_grpc.CalculateReversePolyCoeffResponse\x12g\n\x12CfgAnlgEdgeRefTrig\x12\'.nidaqmx_grpc.CfgAnlgEdgeRefTrigRequest\x1a(.nidaqmx_grpc.CfgAnlgEdgeRefTrigResponse\x12m\n\x14CfgAnlgEdgeStartTrig\x12).nidaqmx_grpc.CfgAnlgEdgeStartTrigRequest\x1a*.nidaqmx_grpc.CfgAnlgEdgeStartTrigResponse\x12v\n\x17CfgAnlgMultiEdgeRefTrig\x12,.nidaqmx_grpc.CfgAnlgMultiEdgeRefTrigRequest\x1a-.nidaqmx_grpc.CfgAnlgMultiEdgeRefTrigResponse\x12|\n\x19CfgAnlgMultiEdgeStartTrig\x12..nidaqmx_grpc.CfgAnlgMultiEdgeStartTrigRequest\x1a/.nidaqmx_grpc.CfgAnlgMultiEdgeStartTrigResponse\x12m\n\x14CfgAnlgWindowRefTrig\x12).nidaqmx_grpc.CfgAnlgWindowRefTrigRequest\x1a*.nidaqmx_grpc.CfgAnlgWindowRefTrigResponse\x12s\n\x16CfgAnlgWindowStartTrig\x12+.nidaqmx_grpc.CfgAnlgWindowStartTrigRequest\x1a,.nidaqmx_grpc.CfgAnlgWindowStartTrigResponse\x12\x9d\x01\n$CfgBurstHandshakingTimingExportClock\x129.nidaqmx_grpc.CfgBurstHandshakingTimingExportClockRequest\x1a:.nidaqmx_grpc.CfgBurstHandshakingTimingExportClockResponse\x12\x9d\x01\n$CfgBurstHandshakingTimingImportClock\x129.nidaqmx_grpc.CfgBurstHandshakingTimingImportClockRequest\x1a:.nidaqmx_grpc.CfgBurstHandshakingTimingImportClockResponse\x12y\n\x18CfgChangeDetectionTiming\x12-.nidaqmx_grpc.CfgChangeDetectionTimingRequest\x1a..nidaqmx_grpc.CfgChangeDetectionTimingResponse\x12d\n\x11CfgDigEdgeRefTrig\x12&.nidaqmx_grpc.CfgDigEdgeRefTrigRequest\x1a\'.nidaqmx_grpc.CfgDigEdgeRefTrigResponse\x12j\n\x13CfgDigEdgeStartTrig\x12(.nidaqmx_grpc.CfgDigEdgeStartTrigRequest\x1a).nidaqmx_grpc.CfgDigEdgeStartTrigResponse\x12m\n\x14CfgDigPatternRefTrig\x12).nidaqmx_grpc.CfgDigPatternRefTrigRequest\x1a*.nidaqmx_grpc.CfgDigPatternRefTrigResponse\x12s\n\x16CfgDigPatternStartTrig\x12+.nidaqmx_grpc.CfgDigPatternStartTrigRequest\x1a,.nidaqmx_grpc.CfgDigPatternStartTrigResponse\x12m\n\x14CfgHandshakingTiming\x12).nidaqmx_grpc.CfgHandshakingTimingRequest\x1a*.nidaqmx_grpc.CfgHandshakingTimingResponse\x12d\n\x11CfgImplicitTiming\x12&.nidaqmx_grpc.CfgImplicitTimingRequest\x1a\'.nidaqmx_grpc.CfgImplicitTimingResponse\x12[\n\x0eCfgInputBuffer\x12#.nidaqmx_grpc.CfgInputBufferRequest\x1a$.nidaqmx_grpc.CfgInputBufferResponse\x12^\n\x0fCfgOutputBuffer\x12$.nidaqmx_grpc.CfgOutputBufferRequest\x1a%.nidaqmx_grpc.CfgOutputBufferResponse\x12|\n\x19CfgPipelinedSampClkTiming\x12..nidaqmx_grpc.CfgPipelinedSampClkTimingRequest\x1a/.nidaqmx_grpc.CfgPipelinedSampClkTimingResponse\x12a\n\x10CfgSampClkTiming\x12%.nidaqmx_grpc.CfgSampClkTimingRequest\x1a&.nidaqmx_grpc.CfgSampClkTimingResponse\x12a\n\x10CfgTimeStartTrig\x12%.nidaqmx_grpc.CfgTimeStartTrigRequest\x1a&.nidaqmx_grpc.CfgTimeStartTrigResponse\x12y\n\x18CfgWatchdogAOExpirStates\x12-.nidaqmx_grpc.CfgWatchdogAOExpirStatesRequest\x1a..nidaqmx_grpc.CfgWatchdogAOExpirStatesResponse\x12y\n\x18CfgWatchdogCOExpirStates\x12-.nidaqmx_grpc.CfgWatchdogCOExpirStatesRequest\x1a..nidaqmx_grpc.CfgWatchdogCOExpirStatesResponse\x12y\n\x18CfgWatchdogDOExpirStates\x12-.nidaqmx_grpc.CfgWatchdogDOExpirStatesRequest\x1a..nidaqmx_grpc.CfgWatchdogDOExpirStatesResponse\x12L\n\tClearTEDS\x12\x1e.nidaqmx_grpc.ClearTEDSRequest\x1a\x1f.nidaqmx_grpc.ClearTEDSResponse\x12L\n\tClearTask\x12\x1e.nidaqmx_grpc.ClearTaskRequest\x1a\x1f.nidaqmx_grpc.ClearTaskResponse\x12a\n\x10ConfigureLogging\x12%.nidaqmx_grpc.ConfigureLoggingRequest\x1a&.nidaqmx_grpc.ConfigureLoggingResponse\x12X\n\rConfigureTEDS\x12".nidaqmx_grpc.ConfigureTEDSRequest\x1a#.nidaqmx_grpc.ConfigureTEDSResponse\x12U\n\x0cConnectTerms\x12!.nidaqmx_grpc.ConnectTermsRequest\x1a".nidaqmx_grpc.ConnectTermsResponse\x12j\n\x13ControlWatchdogTask\x12(.nidaqmx_grpc.ControlWatchdogTaskRequest\x1a).nidaqmx_grpc.ControlWatchdogTaskResponse\x12\x8e\x01\n\x1fCreateAIAccel4WireDCVoltageChan\x124.nidaqmx_grpc.CreateAIAccel4WireDCVoltageChanRequest\x1a5.nidaqmx_grpc.CreateAIAccel4WireDCVoltageChanResponse\x12d\n\x11CreateAIAccelChan\x12&.nidaqmx_grpc.CreateAIAccelChanRequest\x1a\'.nidaqmx_grpc.CreateAIAccelChanResponse\x12v\n\x17CreateAIAccelChargeChan\x12,.nidaqmx_grpc.CreateAIAccelChargeChanRequest\x1a-.nidaqmx_grpc.CreateAIAccelChargeChanResponse\x12g\n\x12CreateAIBridgeChan\x12\'.nidaqmx_grpc.CreateAIBridgeChanRequest\x1a(.nidaqmx_grpc.CreateAIBridgeChanResponse\x12\x82\x01\n\x1bCreateAICalculatedPowerChan\x120.nidaqmx_grpc.CreateAICalculatedPowerChanRequest\x1a1.nidaqmx_grpc.CreateAICalculatedPowerChanResponse\x12g\n\x12CreateAIChargeChan\x12\'.nidaqmx_grpc.CreateAIChargeChanRequest\x1a(.nidaqmx_grpc.CreateAIChargeChanResponse\x12j\n\x13CreateAICurrentChan\x12(.nidaqmx_grpc.CreateAICurrentChanRequest\x1a).nidaqmx_grpc.CreateAICurrentChanResponse\x12s\n\x16CreateAICurrentRMSChan\x12+.nidaqmx_grpc.CreateAICurrentRMSChanRequest\x1a,.nidaqmx_grpc.CreateAICurrentRMSChanResponse\x12\x94\x01\n!CreateAIForceBridgePolynomialChan\x126.nidaqmx_grpc.CreateAIForceBridgePolynomialChanRequest\x1a7.nidaqmx_grpc.CreateAIForceBridgePolynomialChanResponse\x12\x85\x01\n\x1cCreateAIForceBridgeTableChan\x121.nidaqmx_grpc.CreateAIForceBridgeTableChanRequest\x1a2.nidaqmx_grpc.CreateAIForceBridgeTableChanResponse\x12\x97\x01\n"CreateAIForceBridgeTwoPointLinChan\x127.nidaqmx_grpc.CreateAIForceBridgeTwoPointLinChanRequest\x1a8.nidaqmx_grpc.CreateAIForceBridgeTwoPointLinChanResponse\x12p\n\x15CreateAIForceIEPEChan\x12*.nidaqmx_grpc.CreateAIForceIEPEChanRequest\x1a+.nidaqmx_grpc.CreateAIForceIEPEChanResponse\x12v\n\x17CreateAIFreqVoltageChan\x12,.nidaqmx_grpc.CreateAIFreqVoltageChanRequest\x1a-.nidaqmx_grpc.CreateAIFreqVoltageChanResponse\x12s\n\x16CreateAIMicrophoneChan\x12+.nidaqmx_grpc.CreateAIMicrophoneChanRequest\x1a,.nidaqmx_grpc.CreateAIMicrophoneChanResponse\x12\x91\x01\n CreateAIPosEddyCurrProxProbeChan\x125.nidaqmx_grpc.CreateAIPosEddyCurrProxProbeChanRequest\x1a6.nidaqmx_grpc.CreateAIPosEddyCurrProxProbeChanResponse\x12j\n\x13CreateAIPosLVDTChan\x12(.nidaqmx_grpc.CreateAIPosLVDTChanRequest\x1a).nidaqmx_grpc.CreateAIPosLVDTChanResponse\x12j\n\x13CreateAIPosRVDTChan\x12(.nidaqmx_grpc.CreateAIPosRVDTChanRequest\x1a).nidaqmx_grpc.CreateAIPosRVDTChanResponse\x12d\n\x11CreateAIPowerChan\x12&.nidaqmx_grpc.CreateAIPowerChanRequest\x1a\'.nidaqmx_grpc.CreateAIPowerChanResponse\x12\x9d\x01\n$CreateAIPressureBridgePolynomialChan\x129.nidaqmx_grpc.CreateAIPressureBridgePolynomialChanRequest\x1a:.nidaqmx_grpc.CreateAIPressureBridgePolynomialChanResponse\x12\x8e\x01\n\x1fCreateAIPressureBridgeTableChan\x124.nidaqmx_grpc.CreateAIPressureBridgeTableChanRequest\x1a5.nidaqmx_grpc.CreateAIPressureBridgeTableChanResponse\x12\xa0\x01\n%CreateAIPressureBridgeTwoPointLinChan\x12:.nidaqmx_grpc.CreateAIPressureBridgeTwoPointLinChanRequest\x1a;.nidaqmx_grpc.CreateAIPressureBridgeTwoPointLinChanResponse\x12^\n\x0fCreateAIRTDChan\x12$.nidaqmx_grpc.CreateAIRTDChanRequest\x1a%.nidaqmx_grpc.CreateAIRTDChanResponse\x12s\n\x16CreateAIResistanceChan\x12+.nidaqmx_grpc.CreateAIResistanceChanRequest\x1a,.nidaqmx_grpc.CreateAIResistanceChanResponse\x12\x88\x01\n\x1dCreateAIRosetteStrainGageChan\x122.nidaqmx_grpc.CreateAIRosetteStrainGageChanRequest\x1a3.nidaqmx_grpc.CreateAIRosetteStrainGageChanResponse\x12s\n\x16CreateAIStrainGageChan\x12+.nidaqmx_grpc.CreateAIStrainGageChanRequest\x1a,.nidaqmx_grpc.CreateAIStrainGageChanResponse\x12\x88\x01\n\x1dCreateAITempBuiltInSensorChan\x122.nidaqmx_grpc.CreateAITempBuiltInSensorChanRequest\x1a3.nidaqmx_grpc.CreateAITempBuiltInSensorChanResponse\x12j\n\x13CreateAIThrmcplChan\x12(.nidaqmx_grpc.CreateAIThrmcplChanRequest\x1a).nidaqmx_grpc.CreateAIThrmcplChanResponse\x12s\n\x16CreateAIThrmstrChanIex\x12+.nidaqmx_grpc.CreateAIThrmstrChanIexRequest\x1a,.nidaqmx_grpc.CreateAIThrmstrChanIexResponse\x12s\n\x16CreateAIThrmstrChanVex\x12+.nidaqmx_grpc.CreateAIThrmstrChanVexRequest\x1a,.nidaqmx_grpc.CreateAIThrmstrChanVexResponse\x12\x97\x01\n"CreateAITorqueBridgePolynomialChan\x127.nidaqmx_grpc.CreateAITorqueBridgePolynomialChanRequest\x1a8.nidaqmx_grpc.CreateAITorqueBridgePolynomialChanResponse\x12\x88\x01\n\x1dCreateAITorqueBridgeTableChan\x122.nidaqmx_grpc.CreateAITorqueBridgeTableChanRequest\x1a3.nidaqmx_grpc.CreateAITorqueBridgeTableChanResponse\x12\x9a\x01\n#CreateAITorqueBridgeTwoPointLinChan\x128.nidaqmx_grpc.CreateAITorqueBridgeTwoPointLinChanRequest\x1a9.nidaqmx_grpc.CreateAITorqueBridgeTwoPointLinChanResponse\x12y\n\x18CreateAIVelocityIEPEChan\x12-.nidaqmx_grpc.CreateAIVelocityIEPEChanRequest\x1a..nidaqmx_grpc.CreateAIVelocityIEPEChanResponse\x12j\n\x13CreateAIVoltageChan\x12(.nidaqmx_grpc.CreateAIVoltageChanRequest\x1a).nidaqmx_grpc.CreateAIVoltageChanResponse\x12\x85\x01\n\x1cCreateAIVoltageChanWithExcit\x121.nidaqmx_grpc.CreateAIVoltageChanWithExcitRequest\x1a2.nidaqmx_grpc.CreateAIVoltageChanWithExcitResponse\x12s\n\x16CreateAIVoltageRMSChan\x12+.nidaqmx_grpc.CreateAIVoltageRMSChanRequest\x1a,.nidaqmx_grpc.CreateAIVoltageRMSChanResponse\x12j\n\x13CreateAOCurrentChan\x12(.nidaqmx_grpc.CreateAOCurrentChanRequest\x1a).nidaqmx_grpc.CreateAOCurrentChanResponse\x12j\n\x13CreateAOFuncGenChan\x12(.nidaqmx_grpc.CreateAOFuncGenChanRequest\x1a).nidaqmx_grpc.CreateAOFuncGenChanResponse\x12j\n\x13CreateAOVoltageChan\x12(.nidaqmx_grpc.CreateAOVoltageChanRequest\x1a).nidaqmx_grpc.CreateAOVoltageChanResponse\x12s\n\x16CreateCIAngEncoderChan\x12+.nidaqmx_grpc.CreateCIAngEncoderChanRequest\x1a,.nidaqmx_grpc.CreateCIAngEncoderChanResponse\x12v\n\x17CreateCIAngVelocityChan\x12,.nidaqmx_grpc.CreateCIAngVelocityChanRequest\x1a-.nidaqmx_grpc.CreateCIAngVelocityChanResponse\x12s\n\x16CreateCICountEdgesChan\x12+.nidaqmx_grpc.CreateCICountEdgesChanRequest\x1a,.nidaqmx_grpc.CreateCICountEdgesChanResponse\x12p\n\x15CreateCIDutyCycleChan\x12*.nidaqmx_grpc.CreateCIDutyCycleChanRequest\x1a+.nidaqmx_grpc.CreateCIDutyCycleChanResponse\x12a\n\x10CreateCIFreqChan\x12%.nidaqmx_grpc.CreateCIFreqChanRequest\x1a&.nidaqmx_grpc.CreateCIFreqChanResponse\x12y\n\x18CreateCIGPSTimestampChan\x12-.nidaqmx_grpc.CreateCIGPSTimestampChanRequest\x1a..nidaqmx_grpc.CreateCIGPSTimestampChanResponse\x12s\n\x16CreateCILinEncoderChan\x12+.nidaqmx_grpc.CreateCILinEncoderChanRequest\x1a,.nidaqmx_grpc.CreateCILinEncoderChanResponse\x12v\n\x17CreateCILinVelocityChan\x12,.nidaqmx_grpc.CreateCILinVelocityChanRequest\x1a-.nidaqmx_grpc.CreateCILinVelocityChanResponse\x12g\n\x12CreateCIPeriodChan\x12\'.nidaqmx_grpc.CreateCIPeriodChanRequest\x1a(.nidaqmx_grpc.CreateCIPeriodChanResponse\x12p\n\x15CreateCIPulseChanFreq\x12*.nidaqmx_grpc.CreateCIPulseChanFreqRequest\x1a+.nidaqmx_grpc.CreateCIPulseChanFreqResponse\x12s\n\x16CreateCIPulseChanTicks\x12+.nidaqmx_grpc.CreateCIPulseChanTicksRequest\x1a,.nidaqmx_grpc.CreateCIPulseChanTicksResponse\x12p\n\x15CreateCIPulseChanTime\x12*.nidaqmx_grpc.CreateCIPulseChanTimeRequest\x1a+.nidaqmx_grpc.CreateCIPulseChanTimeResponse\x12s\n\x16CreateCIPulseWidthChan\x12+.nidaqmx_grpc.CreateCIPulseWidthChanRequest\x1a,.nidaqmx_grpc.CreateCIPulseWidthChanResponse\x12s\n\x16CreateCISemiPeriodChan\x12+.nidaqmx_grpc.CreateCISemiPeriodChanRequest\x1a,.nidaqmx_grpc.CreateCISemiPeriodChanResponse\x12s\n\x16CreateCITwoEdgeSepChan\x12+.nidaqmx_grpc.CreateCITwoEdgeSepChanRequest\x1a,.nidaqmx_grpc.CreateCITwoEdgeSepChanResponse\x12p\n\x15CreateCOPulseChanFreq\x12*.nidaqmx_grpc.CreateCOPulseChanFreqRequest\x1a+.nidaqmx_grpc.CreateCOPulseChanFreqResponse\x12s\n\x16CreateCOPulseChanTicks\x12+.nidaqmx_grpc.CreateCOPulseChanTicksRequest\x1a,.nidaqmx_grpc.CreateCOPulseChanTicksResponse\x12p\n\x15CreateCOPulseChanTime\x12*.nidaqmx_grpc.CreateCOPulseChanTimeRequest\x1a+.nidaqmx_grpc.CreateCOPulseChanTimeResponse\x12U\n\x0cCreateDIChan\x12!.nidaqmx_grpc.CreateDIChanRequest\x1a".nidaqmx_grpc.CreateDIChanResponse\x12U\n\x0cCreateDOChan\x12!.nidaqmx_grpc.CreateDOChanRequest\x1a".nidaqmx_grpc.CreateDOChanResponse\x12[\n\x0eCreateLinScale\x12#.nidaqmx_grpc.CreateLinScaleRequest\x1a$.nidaqmx_grpc.CreateLinScaleResponse\x12[\n\x0eCreateMapScale\x12#.nidaqmx_grpc.CreateMapScaleRequest\x1a$.nidaqmx_grpc.CreateMapScaleResponse\x12p\n\x15CreatePolynomialScale\x12*.nidaqmx_grpc.CreatePolynomialScaleRequest\x1a+.nidaqmx_grpc.CreatePolynomialScaleResponse\x12p\n\x15CreateTEDSAIAccelChan\x12*.nidaqmx_grpc.CreateTEDSAIAccelChanRequest\x1a+.nidaqmx_grpc.CreateTEDSAIAccelChanResponse\x12s\n\x16CreateTEDSAIBridgeChan\x12+.nidaqmx_grpc.CreateTEDSAIBridgeChanRequest\x1a,.nidaqmx_grpc.CreateTEDSAIBridgeChanResponse\x12v\n\x17CreateTEDSAICurrentChan\x12,.nidaqmx_grpc.CreateTEDSAICurrentChanRequest\x1a-.nidaqmx_grpc.CreateTEDSAICurrentChanResponse\x12\x82\x01\n\x1bCreateTEDSAIForceBridgeChan\x120.nidaqmx_grpc.CreateTEDSAIForceBridgeChanRequest\x1a1.nidaqmx_grpc.CreateTEDSAIForceBridgeChanResponse\x12|\n\x19CreateTEDSAIForceIEPEChan\x12..nidaqmx_grpc.CreateTEDSAIForceIEPEChanRequest\x1a/.nidaqmx_grpc.CreateTEDSAIForceIEPEChanResponse\x12\x7f\n\x1aCreateTEDSAIMicrophoneChan\x12/.nidaqmx_grpc.CreateTEDSAIMicrophoneChanRequest\x1a0.nidaqmx_grpc.CreateTEDSAIMicrophoneChanResponse\x12v\n\x17CreateTEDSAIPosLVDTChan\x12,.nidaqmx_grpc.CreateTEDSAIPosLVDTChanRequest\x1a-.nidaqmx_grpc.CreateTEDSAIPosLVDTChanResponse\x12v\n\x17CreateTEDSAIPosRVDTChan\x12,.nidaqmx_grpc.CreateTEDSAIPosRVDTChanRequest\x1a-.nidaqmx_grpc.CreateTEDSAIPosRVDTChanResponse\x12\x8b\x01\n\x1eCreateTEDSAIPressureBridgeChan\x123.nidaqmx_grpc.CreateTEDSAIPressureBridgeChanRequest\x1a4.nidaqmx_grpc.CreateTEDSAIPressureBridgeChanResponse\x12j\n\x13CreateTEDSAIRTDChan\x12(.nidaqmx_grpc.CreateTEDSAIRTDChanRequest\x1a).nidaqmx_grpc.CreateTEDSAIRTDChanResponse\x12\x7f\n\x1aCreateTEDSAIResistanceChan\x12/.nidaqmx_grpc.CreateTEDSAIResistanceChanRequest\x1a0.nidaqmx_grpc.CreateTEDSAIResistanceChanResponse\x12\x7f\n\x1aCreateTEDSAIStrainGageChan\x12/.nidaqmx_grpc.CreateTEDSAIStrainGageChanRequest\x1a0.nidaqmx_grpc.CreateTEDSAIStrainGageChanResponse\x12v\n\x17CreateTEDSAIThrmcplChan\x12,.nidaqmx_grpc.CreateTEDSAIThrmcplChanRequest\x1a-.nidaqmx_grpc.CreateTEDSAIThrmcplChanResponse\x12\x7f\n\x1aCreateTEDSAIThrmstrChanIex\x12/.nidaqmx_grpc.CreateTEDSAIThrmstrChanIexRequest\x1a0.nidaqmx_grpc.CreateTEDSAIThrmstrChanIexResponse\x12\x7f\n\x1aCreateTEDSAIThrmstrChanVex\x12/.nidaqmx_grpc.CreateTEDSAIThrmstrChanVexRequest\x1a0.nidaqmx_grpc.CreateTEDSAIThrmstrChanVexResponse\x12\x85\x01\n\x1cCreateTEDSAITorqueBridgeChan\x121.nidaqmx_grpc.CreateTEDSAITorqueBridgeChanRequest\x1a2.nidaqmx_grpc.CreateTEDSAITorqueBridgeChanResponse\x12v\n\x17CreateTEDSAIVoltageChan\x12,.nidaqmx_grpc.CreateTEDSAIVoltageChanRequest\x1a-.nidaqmx_grpc.CreateTEDSAIVoltageChanResponse\x12\x91\x01\n CreateTEDSAIVoltageChanWithExcit\x125.nidaqmx_grpc.CreateTEDSAIVoltageChanWithExcitRequest\x1a6.nidaqmx_grpc.CreateTEDSAIVoltageChanWithExcitResponse\x12a\n\x10CreateTableScale\x12%.nidaqmx_grpc.CreateTableScaleRequest\x1a&.nidaqmx_grpc.CreateTableScaleResponse\x12O\n\nCreateTask\x12\x1f.nidaqmx_grpc.CreateTaskRequest\x1a .nidaqmx_grpc.CreateTaskResponse\x12v\n\x17CreateWatchdogTimerTask\x12,.nidaqmx_grpc.CreateWatchdogTimerTaskRequest\x1a-.nidaqmx_grpc.CreateWatchdogTimerTaskResponse\x12|\n\x19CreateWatchdogTimerTaskEx\x12..nidaqmx_grpc.CreateWatchdogTimerTaskExRequest\x1a/.nidaqmx_grpc.CreateWatchdogTimerTaskExResponse\x12j\n\x13DeleteNetworkDevice\x12(.nidaqmx_grpc.DeleteNetworkDeviceRequest\x1a).nidaqmx_grpc.DeleteNetworkDeviceResponse\x12p\n\x15DeleteSavedGlobalChan\x12*.nidaqmx_grpc.DeleteSavedGlobalChanRequest\x1a+.nidaqmx_grpc.DeleteSavedGlobalChanResponse\x12a\n\x10DeleteSavedScale\x12%.nidaqmx_grpc.DeleteSavedScaleRequest\x1a&.nidaqmx_grpc.DeleteSavedScaleResponse\x12^\n\x0fDeleteSavedTask\x12$.nidaqmx_grpc.DeleteSavedTaskRequest\x1a%.nidaqmx_grpc.DeleteSavedTaskResponse\x12d\n\x11DeviceSupportsCal\x12&.nidaqmx_grpc.DeviceSupportsCalRequest\x1a\'.nidaqmx_grpc.DeviceSupportsCalResponse\x12[\n\x0eDisableRefTrig\x12#.nidaqmx_grpc.DisableRefTrigRequest\x1a$.nidaqmx_grpc.DisableRefTrigResponse\x12a\n\x10DisableStartTrig\x12%.nidaqmx_grpc.DisableStartTrigRequest\x1a&.nidaqmx_grpc.DisableStartTrigResponse\x12^\n\x0fDisconnectTerms\x12$.nidaqmx_grpc.DisconnectTermsRequest\x1a%.nidaqmx_grpc.DisconnectTermsResponse\x12U\n\x0cExportSignal\x12!.nidaqmx_grpc.ExportSignalRequest\x1a".nidaqmx_grpc.ExportSignalResponse\x12j\n\x13GetAIChanCalCalDate\x12(.nidaqmx_grpc.GetAIChanCalCalDateRequest\x1a).nidaqmx_grpc.GetAIChanCalCalDateResponse\x12j\n\x13GetAIChanCalExpDate\x12(.nidaqmx_grpc.GetAIChanCalExpDateRequest\x1a).nidaqmx_grpc.GetAIChanCalExpDateResponse\x12s\n\x16GetAnalogPowerUpStates\x12+.nidaqmx_grpc.GetAnalogPowerUpStatesRequest\x1a,.nidaqmx_grpc.GetAnalogPowerUpStatesResponse\x12\x9d\x01\n$GetAnalogPowerUpStatesWithOutputType\x129.nidaqmx_grpc.GetAnalogPowerUpStatesWithOutputTypeRequest\x1a:.nidaqmx_grpc.GetAnalogPowerUpStatesWithOutputTypeResponse\x12\x82\x01\n\x1bGetArmStartTrigTimestampVal\x120.nidaqmx_grpc.GetArmStartTrigTimestampValRequest\x1a1.nidaqmx_grpc.GetArmStartTrigTimestampValResponse\x12v\n\x17GetArmStartTrigTrigWhen\x12,.nidaqmx_grpc.GetArmStartTrigTrigWhenRequest\x1a-.nidaqmx_grpc.GetArmStartTrigTrigWhenResponse\x12\x9d\x01\n$GetAutoConfiguredCDAQSyncConnections\x129.nidaqmx_grpc.GetAutoConfiguredCDAQSyncConnectionsRequest\x1a:.nidaqmx_grpc.GetAutoConfiguredCDAQSyncConnectionsResponse\x12y\n\x18GetBufferAttributeUInt32\x12-.nidaqmx_grpc.GetBufferAttributeUInt32Request\x1a..nidaqmx_grpc.GetBufferAttributeUInt32Response\x12v\n\x17GetCalInfoAttributeBool\x12,.nidaqmx_grpc.GetCalInfoAttributeBoolRequest\x1a-.nidaqmx_grpc.GetCalInfoAttributeBoolResponse\x12|\n\x19GetCalInfoAttributeDouble\x12..nidaqmx_grpc.GetCalInfoAttributeDoubleRequest\x1a/.nidaqmx_grpc.GetCalInfoAttributeDoubleResponse\x12|\n\x19GetCalInfoAttributeString\x12..nidaqmx_grpc.GetCalInfoAttributeStringRequest\x1a/.nidaqmx_grpc.GetCalInfoAttributeStringResponse\x12|\n\x19GetCalInfoAttributeUInt32\x12..nidaqmx_grpc.GetCalInfoAttributeUInt32Request\x1a/.nidaqmx_grpc.GetCalInfoAttributeUInt32Response\x12m\n\x14GetChanAttributeBool\x12).nidaqmx_grpc.GetChanAttributeBoolRequest\x1a*.nidaqmx_grpc.GetChanAttributeBoolResponse\x12s\n\x16GetChanAttributeDouble\x12+.nidaqmx_grpc.GetChanAttributeDoubleRequest\x1a,.nidaqmx_grpc.GetChanAttributeDoubleResponse\x12\x82\x01\n\x1bGetChanAttributeDoubleArray\x120.nidaqmx_grpc.GetChanAttributeDoubleArrayRequest\x1a1.nidaqmx_grpc.GetChanAttributeDoubleArrayResponse\x12p\n\x15GetChanAttributeInt32\x12*.nidaqmx_grpc.GetChanAttributeInt32Request\x1a+.nidaqmx_grpc.GetChanAttributeInt32Response\x12s\n\x16GetChanAttributeString\x12+.nidaqmx_grpc.GetChanAttributeStringRequest\x1a,.nidaqmx_grpc.GetChanAttributeStringResponse\x12s\n\x16GetChanAttributeUInt32\x12+.nidaqmx_grpc.GetChanAttributeUInt32Request\x1a,.nidaqmx_grpc.GetChanAttributeUInt32Response\x12s\n\x16GetDeviceAttributeBool\x12+.nidaqmx_grpc.GetDeviceAttributeBoolRequest\x1a,.nidaqmx_grpc.GetDeviceAttributeBoolResponse\x12y\n\x18GetDeviceAttributeDouble\x12-.nidaqmx_grpc.GetDeviceAttributeDoubleRequest\x1a..nidaqmx_grpc.GetDeviceAttributeDoubleResponse\x12\x88\x01\n\x1dGetDeviceAttributeDoubleArray\x122.nidaqmx_grpc.GetDeviceAttributeDoubleArrayRequest\x1a3.nidaqmx_grpc.GetDeviceAttributeDoubleArrayResponse\x12v\n\x17GetDeviceAttributeInt32\x12,.nidaqmx_grpc.GetDeviceAttributeInt32Request\x1a-.nidaqmx_grpc.GetDeviceAttributeInt32Response\x12\x85\x01\n\x1cGetDeviceAttributeInt32Array\x121.nidaqmx_grpc.GetDeviceAttributeInt32ArrayRequest\x1a2.nidaqmx_grpc.GetDeviceAttributeInt32ArrayResponse\x12y\n\x18GetDeviceAttributeString\x12-.nidaqmx_grpc.GetDeviceAttributeStringRequest\x1a..nidaqmx_grpc.GetDeviceAttributeStringResponse\x12y\n\x18GetDeviceAttributeUInt32\x12-.nidaqmx_grpc.GetDeviceAttributeUInt32Request\x1a..nidaqmx_grpc.GetDeviceAttributeUInt32Response\x12\x88\x01\n\x1dGetDeviceAttributeUInt32Array\x122.nidaqmx_grpc.GetDeviceAttributeUInt32ArrayRequest\x1a3.nidaqmx_grpc.GetDeviceAttributeUInt32ArrayResponse\x12\x94\x01\n!GetDigitalLogicFamilyPowerUpState\x126.nidaqmx_grpc.GetDigitalLogicFamilyPowerUpStateRequest\x1a7.nidaqmx_grpc.GetDigitalLogicFamilyPowerUpStateResponse\x12v\n\x17GetDigitalPowerUpStates\x12,.nidaqmx_grpc.GetDigitalPowerUpStatesRequest\x1a-.nidaqmx_grpc.GetDigitalPowerUpStatesResponse\x12\x8b\x01\n\x1eGetDigitalPullUpPullDownStates\x123.nidaqmx_grpc.GetDigitalPullUpPullDownStatesRequest\x1a4.nidaqmx_grpc.GetDigitalPullUpPullDownStatesResponse\x12\x85\x01\n\x1cGetDisconnectedCDAQSyncPorts\x121.nidaqmx_grpc.GetDisconnectedCDAQSyncPortsRequest\x1a2.nidaqmx_grpc.GetDisconnectedCDAQSyncPortsResponse\x12[\n\x0eGetErrorString\x12#.nidaqmx_grpc.GetErrorStringRequest\x1a$.nidaqmx_grpc.GetErrorStringResponse\x12\x8b\x01\n\x1eGetExportedSignalAttributeBool\x123.nidaqmx_grpc.GetExportedSignalAttributeBoolRequest\x1a4.nidaqmx_grpc.GetExportedSignalAttributeBoolResponse\x12\x91\x01\n GetExportedSignalAttributeDouble\x125.nidaqmx_grpc.GetExportedSignalAttributeDoubleRequest\x1a6.nidaqmx_grpc.GetExportedSignalAttributeDoubleResponse\x12\x8e\x01\n\x1fGetExportedSignalAttributeInt32\x124.nidaqmx_grpc.GetExportedSignalAttributeInt32Request\x1a5.nidaqmx_grpc.GetExportedSignalAttributeInt32Response\x12\x91\x01\n GetExportedSignalAttributeString\x125.nidaqmx_grpc.GetExportedSignalAttributeStringRequest\x1a6.nidaqmx_grpc.GetExportedSignalAttributeStringResponse\x12\x91\x01\n GetExportedSignalAttributeUInt32\x125.nidaqmx_grpc.GetExportedSignalAttributeUInt32Request\x1a6.nidaqmx_grpc.GetExportedSignalAttributeUInt32Response\x12y\n\x18GetExtCalLastDateAndTime\x12-.nidaqmx_grpc.GetExtCalLastDateAndTimeRequest\x1a..nidaqmx_grpc.GetExtCalLastDateAndTimeResponse\x12j\n\x13GetFirstSampClkWhen\x12(.nidaqmx_grpc.GetFirstSampClkWhenRequest\x1a).nidaqmx_grpc.GetFirstSampClkWhenResponse\x12y\n\x18GetFirstSampTimestampVal\x12-.nidaqmx_grpc.GetFirstSampTimestampValRequest\x1a..nidaqmx_grpc.GetFirstSampTimestampValResponse\x12d\n\x11GetNthTaskChannel\x12&.nidaqmx_grpc.GetNthTaskChannelRequest\x1a\'.nidaqmx_grpc.GetNthTaskChannelResponse\x12a\n\x10GetNthTaskDevice\x12%.nidaqmx_grpc.GetNthTaskDeviceRequest\x1a&.nidaqmx_grpc.GetNthTaskDeviceResponse\x12p\n\x15GetNthTaskReadChannel\x12*.nidaqmx_grpc.GetNthTaskReadChannelRequest\x1a+.nidaqmx_grpc.GetNthTaskReadChannelResponse\x12\x88\x01\n\x1dGetPersistedChanAttributeBool\x122.nidaqmx_grpc.GetPersistedChanAttributeBoolRequest\x1a3.nidaqmx_grpc.GetPersistedChanAttributeBoolResponse\x12\x8e\x01\n\x1fGetPersistedChanAttributeString\x124.nidaqmx_grpc.GetPersistedChanAttributeStringRequest\x1a5.nidaqmx_grpc.GetPersistedChanAttributeStringResponse\x12\x8b\x01\n\x1eGetPersistedScaleAttributeBool\x123.nidaqmx_grpc.GetPersistedScaleAttributeBoolRequest\x1a4.nidaqmx_grpc.GetPersistedScaleAttributeBoolResponse\x12\x91\x01\n GetPersistedScaleAttributeString\x125.nidaqmx_grpc.GetPersistedScaleAttributeStringRequest\x1a6.nidaqmx_grpc.GetPersistedScaleAttributeStringResponse\x12\x88\x01\n\x1dGetPersistedTaskAttributeBool\x122.nidaqmx_grpc.GetPersistedTaskAttributeBoolRequest\x1a3.nidaqmx_grpc.GetPersistedTaskAttributeBoolResponse\x12\x8e\x01\n\x1fGetPersistedTaskAttributeString\x124.nidaqmx_grpc.GetPersistedTaskAttributeStringRequest\x1a5.nidaqmx_grpc.GetPersistedTaskAttributeStringResponse\x12\x85\x01\n\x1cGetPhysicalChanAttributeBool\x121.nidaqmx_grpc.GetPhysicalChanAttributeBoolRequest\x1a2.nidaqmx_grpc.GetPhysicalChanAttributeBoolResponse\x12\x88\x01\n\x1dGetPhysicalChanAttributeBytes\x122.nidaqmx_grpc.GetPhysicalChanAttributeBytesRequest\x1a3.nidaqmx_grpc.GetPhysicalChanAttributeBytesResponse\x12\x8b\x01\n\x1eGetPhysicalChanAttributeDouble\x123.nidaqmx_grpc.GetPhysicalChanAttributeDoubleRequest\x1a4.nidaqmx_grpc.GetPhysicalChanAttributeDoubleResponse\x12\x9a\x01\n#GetPhysicalChanAttributeDoubleArray\x128.nidaqmx_grpc.GetPhysicalChanAttributeDoubleArrayRequest\x1a9.nidaqmx_grpc.GetPhysicalChanAttributeDoubleArrayResponse\x12\x88\x01\n\x1dGetPhysicalChanAttributeInt32\x122.nidaqmx_grpc.GetPhysicalChanAttributeInt32Request\x1a3.nidaqmx_grpc.GetPhysicalChanAttributeInt32Response\x12\x97\x01\n"GetPhysicalChanAttributeInt32Array\x127.nidaqmx_grpc.GetPhysicalChanAttributeInt32ArrayRequest\x1a8.nidaqmx_grpc.GetPhysicalChanAttributeInt32ArrayResponse\x12\x8b\x01\n\x1eGetPhysicalChanAttributeString\x123.nidaqmx_grpc.GetPhysicalChanAttributeStringRequest\x1a4.nidaqmx_grpc.GetPhysicalChanAttributeStringResponse\x12\x8b\x01\n\x1eGetPhysicalChanAttributeUInt32\x123.nidaqmx_grpc.GetPhysicalChanAttributeUInt32Request\x1a4.nidaqmx_grpc.GetPhysicalChanAttributeUInt32Response\x12\x9a\x01\n#GetPhysicalChanAttributeUInt32Array\x128.nidaqmx_grpc.GetPhysicalChanAttributeUInt32ArrayRequest\x1a9.nidaqmx_grpc.GetPhysicalChanAttributeUInt32ArrayResponse\x12m\n\x14GetReadAttributeBool\x12).nidaqmx_grpc.GetReadAttributeBoolRequest\x1a*.nidaqmx_grpc.GetReadAttributeBoolResponse\x12s\n\x16GetReadAttributeDouble\x12+.nidaqmx_grpc.GetReadAttributeDoubleRequest\x1a,.nidaqmx_grpc.GetReadAttributeDoubleResponse\x12p\n\x15GetReadAttributeInt32\x12*.nidaqmx_grpc.GetReadAttributeInt32Request\x1a+.nidaqmx_grpc.GetReadAttributeInt32Response\x12s\n\x16GetReadAttributeString\x12+.nidaqmx_grpc.GetReadAttributeStringRequest\x1a,.nidaqmx_grpc.GetReadAttributeStringResponse\x12s\n\x16GetReadAttributeUInt32\x12+.nidaqmx_grpc.GetReadAttributeUInt32Request\x1a,.nidaqmx_grpc.GetReadAttributeUInt32Response\x12s\n\x16GetReadAttributeUInt64\x12+.nidaqmx_grpc.GetReadAttributeUInt64Request\x1a,.nidaqmx_grpc.GetReadAttributeUInt64Response\x12y\n\x18GetRealTimeAttributeBool\x12-.nidaqmx_grpc.GetRealTimeAttributeBoolRequest\x1a..nidaqmx_grpc.GetRealTimeAttributeBoolResponse\x12|\n\x19GetRealTimeAttributeInt32\x12..nidaqmx_grpc.GetRealTimeAttributeInt32Request\x1a/.nidaqmx_grpc.GetRealTimeAttributeInt32Response\x12\x7f\n\x1aGetRealTimeAttributeUInt32\x12/.nidaqmx_grpc.GetRealTimeAttributeUInt32Request\x1a0.nidaqmx_grpc.GetRealTimeAttributeUInt32Response\x12s\n\x16GetRefTrigTimestampVal\x12+.nidaqmx_grpc.GetRefTrigTimestampValRequest\x1a,.nidaqmx_grpc.GetRefTrigTimestampValResponse\x12v\n\x17GetScaleAttributeDouble\x12,.nidaqmx_grpc.GetScaleAttributeDoubleRequest\x1a-.nidaqmx_grpc.GetScaleAttributeDoubleResponse\x12\x85\x01\n\x1cGetScaleAttributeDoubleArray\x121.nidaqmx_grpc.GetScaleAttributeDoubleArrayRequest\x1a2.nidaqmx_grpc.GetScaleAttributeDoubleArrayResponse\x12s\n\x16GetScaleAttributeInt32\x12+.nidaqmx_grpc.GetScaleAttributeInt32Request\x1a,.nidaqmx_grpc.GetScaleAttributeInt32Response\x12v\n\x17GetScaleAttributeString\x12,.nidaqmx_grpc.GetScaleAttributeStringRequest\x1a-.nidaqmx_grpc.GetScaleAttributeStringResponse\x12|\n\x19GetSelfCalLastDateAndTime\x12..nidaqmx_grpc.GetSelfCalLastDateAndTimeRequest\x1a/.nidaqmx_grpc.GetSelfCalLastDateAndTimeResponse\x12y\n\x18GetStartTrigTimestampVal\x12-.nidaqmx_grpc.GetStartTrigTimestampValRequest\x1a..nidaqmx_grpc.GetStartTrigTimestampValResponse\x12m\n\x14GetStartTrigTrigWhen\x12).nidaqmx_grpc.GetStartTrigTrigWhenRequest\x1a*.nidaqmx_grpc.GetStartTrigTrigWhenResponse\x12m\n\x14GetSyncPulseTimeWhen\x12).nidaqmx_grpc.GetSyncPulseTimeWhenRequest\x1a*.nidaqmx_grpc.GetSyncPulseTimeWhenResponse\x12\x85\x01\n\x1cGetSystemInfoAttributeString\x121.nidaqmx_grpc.GetSystemInfoAttributeStringRequest\x1a2.nidaqmx_grpc.GetSystemInfoAttributeStringResponse\x12\x85\x01\n\x1cGetSystemInfoAttributeUInt32\x121.nidaqmx_grpc.GetSystemInfoAttributeUInt32Request\x1a2.nidaqmx_grpc.GetSystemInfoAttributeUInt32Response\x12m\n\x14GetTaskAttributeBool\x12).nidaqmx_grpc.GetTaskAttributeBoolRequest\x1a*.nidaqmx_grpc.GetTaskAttributeBoolResponse\x12s\n\x16GetTaskAttributeString\x12+.nidaqmx_grpc.GetTaskAttributeStringRequest\x1a,.nidaqmx_grpc.GetTaskAttributeStringResponse\x12s\n\x16GetTaskAttributeUInt32\x12+.nidaqmx_grpc.GetTaskAttributeUInt32Request\x1a,.nidaqmx_grpc.GetTaskAttributeUInt32Response\x12s\n\x16GetTimingAttributeBool\x12+.nidaqmx_grpc.GetTimingAttributeBoolRequest\x1a,.nidaqmx_grpc.GetTimingAttributeBoolResponse\x12y\n\x18GetTimingAttributeDouble\x12-.nidaqmx_grpc.GetTimingAttributeDoubleRequest\x1a..nidaqmx_grpc.GetTimingAttributeDoubleResponse\x12y\n\x18GetTimingAttributeExBool\x12-.nidaqmx_grpc.GetTimingAttributeExBoolRequest\x1a..nidaqmx_grpc.GetTimingAttributeExBoolResponse\x12\x7f\n\x1aGetTimingAttributeExDouble\x12/.nidaqmx_grpc.GetTimingAttributeExDoubleRequest\x1a0.nidaqmx_grpc.GetTimingAttributeExDoubleResponse\x12|\n\x19GetTimingAttributeExInt32\x12..nidaqmx_grpc.GetTimingAttributeExInt32Request\x1a/.nidaqmx_grpc.GetTimingAttributeExInt32Response\x12\x7f\n\x1aGetTimingAttributeExString\x12/.nidaqmx_grpc.GetTimingAttributeExStringRequest\x1a0.nidaqmx_grpc.GetTimingAttributeExStringResponse\x12\x88\x01\n\x1dGetTimingAttributeExTimestamp\x122.nidaqmx_grpc.GetTimingAttributeExTimestampRequest\x1a3.nidaqmx_grpc.GetTimingAttributeExTimestampResponse\x12\x7f\n\x1aGetTimingAttributeExUInt32\x12/.nidaqmx_grpc.GetTimingAttributeExUInt32Request\x1a0.nidaqmx_grpc.GetTimingAttributeExUInt32Response\x12\x7f\n\x1aGetTimingAttributeExUInt64\x12/.nidaqmx_grpc.GetTimingAttributeExUInt64Request\x1a0.nidaqmx_grpc.GetTimingAttributeExUInt64Response\x12v\n\x17GetTimingAttributeInt32\x12,.nidaqmx_grpc.GetTimingAttributeInt32Request\x1a-.nidaqmx_grpc.GetTimingAttributeInt32Response\x12y\n\x18GetTimingAttributeString\x12-.nidaqmx_grpc.GetTimingAttributeStringRequest\x1a..nidaqmx_grpc.GetTimingAttributeStringResponse\x12\x82\x01\n\x1bGetTimingAttributeTimestamp\x120.nidaqmx_grpc.GetTimingAttributeTimestampRequest\x1a1.nidaqmx_grpc.GetTimingAttributeTimestampResponse\x12y\n\x18GetTimingAttributeUInt32\x12-.nidaqmx_grpc.GetTimingAttributeUInt32Request\x1a..nidaqmx_grpc.GetTimingAttributeUInt32Response\x12y\n\x18GetTimingAttributeUInt64\x12-.nidaqmx_grpc.GetTimingAttributeUInt64Request\x1a..nidaqmx_grpc.GetTimingAttributeUInt64Response\x12m\n\x14GetTrigAttributeBool\x12).nidaqmx_grpc.GetTrigAttributeBoolRequest\x1a*.nidaqmx_grpc.GetTrigAttributeBoolResponse\x12s\n\x16GetTrigAttributeDouble\x12+.nidaqmx_grpc.GetTrigAttributeDoubleRequest\x1a,.nidaqmx_grpc.GetTrigAttributeDoubleResponse\x12\x82\x01\n\x1bGetTrigAttributeDoubleArray\x120.nidaqmx_grpc.GetTrigAttributeDoubleArrayRequest\x1a1.nidaqmx_grpc.GetTrigAttributeDoubleArrayResponse\x12p\n\x15GetTrigAttributeInt32\x12*.nidaqmx_grpc.GetTrigAttributeInt32Request\x1a+.nidaqmx_grpc.GetTrigAttributeInt32Response\x12\x7f\n\x1aGetTrigAttributeInt32Array\x12/.nidaqmx_grpc.GetTrigAttributeInt32ArrayRequest\x1a0.nidaqmx_grpc.GetTrigAttributeInt32ArrayResponse\x12s\n\x16GetTrigAttributeString\x12+.nidaqmx_grpc.GetTrigAttributeStringRequest\x1a,.nidaqmx_grpc.GetTrigAttributeStringResponse\x12|\n\x19GetTrigAttributeTimestamp\x12..nidaqmx_grpc.GetTrigAttributeTimestampRequest\x1a/.nidaqmx_grpc.GetTrigAttributeTimestampResponse\x12s\n\x16GetTrigAttributeUInt32\x12+.nidaqmx_grpc.GetTrigAttributeUInt32Request\x1a,.nidaqmx_grpc.GetTrigAttributeUInt32Response\x12y\n\x18GetWatchdogAttributeBool\x12-.nidaqmx_grpc.GetWatchdogAttributeBoolRequest\x1a..nidaqmx_grpc.GetWatchdogAttributeBoolResponse\x12\x7f\n\x1aGetWatchdogAttributeDouble\x12/.nidaqmx_grpc.GetWatchdogAttributeDoubleRequest\x1a0.nidaqmx_grpc.GetWatchdogAttributeDoubleResponse\x12|\n\x19GetWatchdogAttributeInt32\x12..nidaqmx_grpc.GetWatchdogAttributeInt32Request\x1a/.nidaqmx_grpc.GetWatchdogAttributeInt32Response\x12\x7f\n\x1aGetWatchdogAttributeString\x12/.nidaqmx_grpc.GetWatchdogAttributeStringRequest\x1a0.nidaqmx_grpc.GetWatchdogAttributeStringResponse\x12p\n\x15GetWriteAttributeBool\x12*.nidaqmx_grpc.GetWriteAttributeBoolRequest\x1a+.nidaqmx_grpc.GetWriteAttributeBoolResponse\x12v\n\x17GetWriteAttributeDouble\x12,.nidaqmx_grpc.GetWriteAttributeDoubleRequest\x1a-.nidaqmx_grpc.GetWriteAttributeDoubleResponse\x12s\n\x16GetWriteAttributeInt32\x12+.nidaqmx_grpc.GetWriteAttributeInt32Request\x1a,.nidaqmx_grpc.GetWriteAttributeInt32Response\x12v\n\x17GetWriteAttributeString\x12,.nidaqmx_grpc.GetWriteAttributeStringRequest\x1a-.nidaqmx_grpc.GetWriteAttributeStringResponse\x12v\n\x17GetWriteAttributeUInt32\x12,.nidaqmx_grpc.GetWriteAttributeUInt32Request\x1a-.nidaqmx_grpc.GetWriteAttributeUInt32Response\x12v\n\x17GetWriteAttributeUInt64\x12,.nidaqmx_grpc.GetWriteAttributeUInt64Request\x1a-.nidaqmx_grpc.GetWriteAttributeUInt64Response\x12O\n\nIsTaskDone\x12\x1f.nidaqmx_grpc.IsTaskDoneRequest\x1a .nidaqmx_grpc.IsTaskDoneResponse\x12I\n\x08LoadTask\x12\x1d.nidaqmx_grpc.LoadTaskRequest\x1a\x1e.nidaqmx_grpc.LoadTaskResponse\x12\x8e\x01\n\x1fPerformBridgeOffsetNullingCalEx\x124.nidaqmx_grpc.PerformBridgeOffsetNullingCalExRequest\x1a5.nidaqmx_grpc.PerformBridgeOffsetNullingCalExResponse\x12v\n\x17PerformBridgeShuntCalEx\x12,.nidaqmx_grpc.PerformBridgeShuntCalExRequest\x1a-.nidaqmx_grpc.PerformBridgeShuntCalExResponse\x12v\n\x17PerformStrainShuntCalEx\x12,.nidaqmx_grpc.PerformStrainShuntCalExRequest\x1a-.nidaqmx_grpc.PerformStrainShuntCalExResponse\x12\x97\x01\n"PerformThrmcplLeadOffsetNullingCal\x127.nidaqmx_grpc.PerformThrmcplLeadOffsetNullingCalRequest\x1a8.nidaqmx_grpc.PerformThrmcplLeadOffsetNullingCalResponse\x12X\n\rReadAnalogF64\x12".nidaqmx_grpc.ReadAnalogF64Request\x1a#.nidaqmx_grpc.ReadAnalogF64Response\x12g\n\x12BeginReadAnalogF64\x12\'.nidaqmx_grpc.BeginReadAnalogF64Request\x1a(.nidaqmx_grpc.BeginReadAnalogF64Response\x12j\n\x13ReadAnalogScalarF64\x12(.nidaqmx_grpc.ReadAnalogScalarF64Request\x1a).nidaqmx_grpc.ReadAnalogScalarF64Response\x12y\n\x18BeginReadAnalogScalarF64\x12-.nidaqmx_grpc.BeginReadAnalogScalarF64Request\x1a..nidaqmx_grpc.BeginReadAnalogScalarF64Response\x12X\n\rReadBinaryI16\x12".nidaqmx_grpc.ReadBinaryI16Request\x1a#.nidaqmx_grpc.ReadBinaryI16Response\x12g\n\x12BeginReadBinaryI16\x12\'.nidaqmx_grpc.BeginReadBinaryI16Request\x1a(.nidaqmx_grpc.BeginReadBinaryI16Response\x12X\n\rReadBinaryI32\x12".nidaqmx_grpc.ReadBinaryI32Request\x1a#.nidaqmx_grpc.ReadBinaryI32Response\x12g\n\x12BeginReadBinaryI32\x12\'.nidaqmx_grpc.BeginReadBinaryI32Request\x1a(.nidaqmx_grpc.BeginReadBinaryI32Response\x12X\n\rReadBinaryU16\x12".nidaqmx_grpc.ReadBinaryU16Request\x1a#.nidaqmx_grpc.ReadBinaryU16Response\x12g\n\x12BeginReadBinaryU16\x12\'.nidaqmx_grpc.BeginReadBinaryU16Request\x1a(.nidaqmx_grpc.BeginReadBinaryU16Response\x12X\n\rReadBinaryU32\x12".nidaqmx_grpc.ReadBinaryU32Request\x1a#.nidaqmx_grpc.ReadBinaryU32Response\x12g\n\x12BeginReadBinaryU32\x12\'.nidaqmx_grpc.BeginReadBinaryU32Request\x1a(.nidaqmx_grpc.BeginReadBinaryU32Response\x12[\n\x0eReadCounterF64\x12#.nidaqmx_grpc.ReadCounterF64Request\x1a$.nidaqmx_grpc.ReadCounterF64Response\x12j\n\x13BeginReadCounterF64\x12(.nidaqmx_grpc.BeginReadCounterF64Request\x1a).nidaqmx_grpc.BeginReadCounterF64Response\x12a\n\x10ReadCounterF64Ex\x12%.nidaqmx_grpc.ReadCounterF64ExRequest\x1a&.nidaqmx_grpc.ReadCounterF64ExResponse\x12p\n\x15BeginReadCounterF64Ex\x12*.nidaqmx_grpc.BeginReadCounterF64ExRequest\x1a+.nidaqmx_grpc.BeginReadCounterF64ExResponse\x12m\n\x14ReadCounterScalarF64\x12).nidaqmx_grpc.ReadCounterScalarF64Request\x1a*.nidaqmx_grpc.ReadCounterScalarF64Response\x12|\n\x19BeginReadCounterScalarF64\x12..nidaqmx_grpc.BeginReadCounterScalarF64Request\x1a/.nidaqmx_grpc.BeginReadCounterScalarF64Response\x12m\n\x14ReadCounterScalarU32\x12).nidaqmx_grpc.ReadCounterScalarU32Request\x1a*.nidaqmx_grpc.ReadCounterScalarU32Response\x12|\n\x19BeginReadCounterScalarU32\x12..nidaqmx_grpc.BeginReadCounterScalarU32Request\x1a/.nidaqmx_grpc.BeginReadCounterScalarU32Response\x12[\n\x0eReadCounterU32\x12#.nidaqmx_grpc.ReadCounterU32Request\x1a$.nidaqmx_grpc.ReadCounterU32Response\x12j\n\x13BeginReadCounterU32\x12(.nidaqmx_grpc.BeginReadCounterU32Request\x1a).nidaqmx_grpc.BeginReadCounterU32Response\x12a\n\x10ReadCounterU32Ex\x12%.nidaqmx_grpc.ReadCounterU32ExRequest\x1a&.nidaqmx_grpc.ReadCounterU32ExResponse\x12p\n\x15BeginReadCounterU32Ex\x12*.nidaqmx_grpc.BeginReadCounterU32ExRequest\x1a+.nidaqmx_grpc.BeginReadCounterU32ExResponse\x12R\n\x0bReadCtrFreq\x12 .nidaqmx_grpc.ReadCtrFreqRequest\x1a!.nidaqmx_grpc.ReadCtrFreqResponse\x12a\n\x10BeginReadCtrFreq\x12%.nidaqmx_grpc.BeginReadCtrFreqRequest\x1a&.nidaqmx_grpc.BeginReadCtrFreqResponse\x12d\n\x11ReadCtrFreqScalar\x12&.nidaqmx_grpc.ReadCtrFreqScalarRequest\x1a\'.nidaqmx_grpc.ReadCtrFreqScalarResponse\x12s\n\x16BeginReadCtrFreqScalar\x12+.nidaqmx_grpc.BeginReadCtrFreqScalarRequest\x1a,.nidaqmx_grpc.BeginReadCtrFreqScalarResponse\x12U\n\x0cReadCtrTicks\x12!.nidaqmx_grpc.ReadCtrTicksRequest\x1a".nidaqmx_grpc.ReadCtrTicksResponse\x12d\n\x11BeginReadCtrTicks\x12&.nidaqmx_grpc.BeginReadCtrTicksRequest\x1a\'.nidaqmx_grpc.BeginReadCtrTicksResponse\x12g\n\x12ReadCtrTicksScalar\x12\'.nidaqmx_grpc.ReadCtrTicksScalarRequest\x1a(.nidaqmx_grpc.ReadCtrTicksScalarResponse\x12v\n\x17BeginReadCtrTicksScalar\x12,.nidaqmx_grpc.BeginReadCtrTicksScalarRequest\x1a-.nidaqmx_grpc.BeginReadCtrTicksScalarResponse\x12R\n\x0bReadCtrTime\x12 .nidaqmx_grpc.ReadCtrTimeRequest\x1a!.nidaqmx_grpc.ReadCtrTimeResponse\x12a\n\x10BeginReadCtrTime\x12%.nidaqmx_grpc.BeginReadCtrTimeRequest\x1a&.nidaqmx_grpc.BeginReadCtrTimeResponse\x12d\n\x11ReadCtrTimeScalar\x12&.nidaqmx_grpc.ReadCtrTimeScalarRequest\x1a\'.nidaqmx_grpc.ReadCtrTimeScalarResponse\x12s\n\x16BeginReadCtrTimeScalar\x12+.nidaqmx_grpc.BeginReadCtrTimeScalarRequest\x1a,.nidaqmx_grpc.BeginReadCtrTimeScalarResponse\x12a\n\x10ReadDigitalLines\x12%.nidaqmx_grpc.ReadDigitalLinesRequest\x1a&.nidaqmx_grpc.ReadDigitalLinesResponse\x12p\n\x15BeginReadDigitalLines\x12*.nidaqmx_grpc.BeginReadDigitalLinesRequest\x1a+.nidaqmx_grpc.BeginReadDigitalLinesResponse\x12m\n\x14ReadDigitalScalarU32\x12).nidaqmx_grpc.ReadDigitalScalarU32Request\x1a*.nidaqmx_grpc.ReadDigitalScalarU32Response\x12|\n\x19BeginReadDigitalScalarU32\x12..nidaqmx_grpc.BeginReadDigitalScalarU32Request\x1a/.nidaqmx_grpc.BeginReadDigitalScalarU32Response\x12[\n\x0eReadDigitalU16\x12#.nidaqmx_grpc.ReadDigitalU16Request\x1a$.nidaqmx_grpc.ReadDigitalU16Response\x12j\n\x13BeginReadDigitalU16\x12(.nidaqmx_grpc.BeginReadDigitalU16Request\x1a).nidaqmx_grpc.BeginReadDigitalU16Response\x12[\n\x0eReadDigitalU32\x12#.nidaqmx_grpc.ReadDigitalU32Request\x1a$.nidaqmx_grpc.ReadDigitalU32Response\x12j\n\x13BeginReadDigitalU32\x12(.nidaqmx_grpc.BeginReadDigitalU32Request\x1a).nidaqmx_grpc.BeginReadDigitalU32Response\x12X\n\rReadDigitalU8\x12".nidaqmx_grpc.ReadDigitalU8Request\x1a#.nidaqmx_grpc.ReadDigitalU8Response\x12g\n\x12BeginReadDigitalU8\x12\'.nidaqmx_grpc.BeginReadDigitalU8Request\x1a(.nidaqmx_grpc.BeginReadDigitalU8Response\x12^\n\x0fReadIDPinMemory\x12$.nidaqmx_grpc.ReadIDPinMemoryRequest\x1a%.nidaqmx_grpc.ReadIDPinMemoryResponse\x12g\n\x12ReadPowerBinaryI16\x12\'.nidaqmx_grpc.ReadPowerBinaryI16Request\x1a(.nidaqmx_grpc.ReadPowerBinaryI16Response\x12v\n\x17BeginReadPowerBinaryI16\x12,.nidaqmx_grpc.BeginReadPowerBinaryI16Request\x1a-.nidaqmx_grpc.BeginReadPowerBinaryI16Response\x12U\n\x0cReadPowerF64\x12!.nidaqmx_grpc.ReadPowerF64Request\x1a".nidaqmx_grpc.ReadPowerF64Response\x12d\n\x11BeginReadPowerF64\x12&.nidaqmx_grpc.BeginReadPowerF64Request\x1a\'.nidaqmx_grpc.BeginReadPowerF64Response\x12g\n\x12ReadPowerScalarF64\x12\'.nidaqmx_grpc.ReadPowerScalarF64Request\x1a(.nidaqmx_grpc.ReadPowerScalarF64Response\x12v\n\x17BeginReadPowerScalarF64\x12,.nidaqmx_grpc.BeginReadPowerScalarF64Request\x1a-.nidaqmx_grpc.BeginReadPowerScalarF64Response\x12F\n\x07ReadRaw\x12\x1c.nidaqmx_grpc.ReadRawRequest\x1a\x1d.nidaqmx_grpc.ReadRawResponse\x12U\n\x0cBeginReadRaw\x12!.nidaqmx_grpc.BeginReadRawRequest\x1a".nidaqmx_grpc.BeginReadRawResponse\x12f\n\x11RegisterDoneEvent\x12&.nidaqmx_grpc.RegisterDoneEventRequest\x1a\'.nidaqmx_grpc.RegisterDoneEventResponse0\x01\x12\x81\x01\n\x1aRegisterEveryNSamplesEvent\x12/.nidaqmx_grpc.RegisterEveryNSamplesEventRequest\x1a0.nidaqmx_grpc.RegisterEveryNSamplesEventResponse0\x01\x12l\n\x13RegisterSignalEvent\x12(.nidaqmx_grpc.RegisterSignalEventRequest\x1a).nidaqmx_grpc.RegisterSignalEventResponse0\x01\x12y\n\x18RemoveCDAQSyncConnection\x12-.nidaqmx_grpc.RemoveCDAQSyncConnectionRequest\x1a..nidaqmx_grpc.RemoveCDAQSyncConnectionResponse\x12m\n\x14ReserveNetworkDevice\x12).nidaqmx_grpc.ReserveNetworkDeviceRequest\x1a*.nidaqmx_grpc.ReserveNetworkDeviceResponse\x12m\n\x14ResetBufferAttribute\x12).nidaqmx_grpc.ResetBufferAttributeRequest\x1a*.nidaqmx_grpc.ResetBufferAttributeResponse\x12g\n\x12ResetChanAttribute\x12\'.nidaqmx_grpc.ResetChanAttributeRequest\x1a(.nidaqmx_grpc.ResetChanAttributeResponse\x12R\n\x0bResetDevice\x12 .nidaqmx_grpc.ResetDeviceRequest\x1a!.nidaqmx_grpc.ResetDeviceResponse\x12\x85\x01\n\x1cResetExportedSignalAttribute\x121.nidaqmx_grpc.ResetExportedSignalAttributeRequest\x1a2.nidaqmx_grpc.ResetExportedSignalAttributeResponse\x12g\n\x12ResetReadAttribute\x12\'.nidaqmx_grpc.ResetReadAttributeRequest\x1a(.nidaqmx_grpc.ResetReadAttributeResponse\x12s\n\x16ResetRealTimeAttribute\x12+.nidaqmx_grpc.ResetRealTimeAttributeRequest\x1a,.nidaqmx_grpc.ResetRealTimeAttributeResponse\x12m\n\x14ResetTimingAttribute\x12).nidaqmx_grpc.ResetTimingAttributeRequest\x1a*.nidaqmx_grpc.ResetTimingAttributeResponse\x12s\n\x16ResetTimingAttributeEx\x12+.nidaqmx_grpc.ResetTimingAttributeExRequest\x1a,.nidaqmx_grpc.ResetTimingAttributeExResponse\x12g\n\x12ResetTrigAttribute\x12\'.nidaqmx_grpc.ResetTrigAttributeRequest\x1a(.nidaqmx_grpc.ResetTrigAttributeResponse\x12s\n\x16ResetWatchdogAttribute\x12+.nidaqmx_grpc.ResetWatchdogAttributeRequest\x1a,.nidaqmx_grpc.ResetWatchdogAttributeResponse\x12j\n\x13ResetWriteAttribute\x12(.nidaqmx_grpc.ResetWriteAttributeRequest\x1a).nidaqmx_grpc.ResetWriteAttributeResponse\x12s\n\x16RestoreLastExtCalConst\x12+.nidaqmx_grpc.RestoreLastExtCalConstRequest\x1a,.nidaqmx_grpc.RestoreLastExtCalConstResponse\x12[\n\x0eSaveGlobalChan\x12#.nidaqmx_grpc.SaveGlobalChanRequest\x1a$.nidaqmx_grpc.SaveGlobalChanResponse\x12L\n\tSaveScale\x12\x1e.nidaqmx_grpc.SaveScaleRequest\x1a\x1f.nidaqmx_grpc.SaveScaleResponse\x12I\n\x08SaveTask\x12\x1d.nidaqmx_grpc.SaveTaskRequest\x1a\x1e.nidaqmx_grpc.SaveTaskResponse\x12F\n\x07SelfCal\x12\x1c.nidaqmx_grpc.SelfCalRequest\x1a\x1d.nidaqmx_grpc.SelfCalResponse\x12[\n\x0eSelfTestDevice\x12#.nidaqmx_grpc.SelfTestDeviceRequest\x1a$.nidaqmx_grpc.SelfTestDeviceResponse\x12j\n\x13SetAIChanCalCalDate\x12(.nidaqmx_grpc.SetAIChanCalCalDateRequest\x1a).nidaqmx_grpc.SetAIChanCalCalDateResponse\x12j\n\x13SetAIChanCalExpDate\x12(.nidaqmx_grpc.SetAIChanCalExpDateRequest\x1a).nidaqmx_grpc.SetAIChanCalExpDateResponse\x12s\n\x16SetAnalogPowerUpStates\x12+.nidaqmx_grpc.SetAnalogPowerUpStatesRequest\x1a,.nidaqmx_grpc.SetAnalogPowerUpStatesResponse\x12\x9d\x01\n$SetAnalogPowerUpStatesWithOutputType\x129.nidaqmx_grpc.SetAnalogPowerUpStatesWithOutputTypeRequest\x1a:.nidaqmx_grpc.SetAnalogPowerUpStatesWithOutputTypeResponse\x12v\n\x17SetArmStartTrigTrigWhen\x12,.nidaqmx_grpc.SetArmStartTrigTrigWhenRequest\x1a-.nidaqmx_grpc.SetArmStartTrigTrigWhenResponse\x12y\n\x18SetBufferAttributeUInt32\x12-.nidaqmx_grpc.SetBufferAttributeUInt32Request\x1a..nidaqmx_grpc.SetBufferAttributeUInt32Response\x12v\n\x17SetCalInfoAttributeBool\x12,.nidaqmx_grpc.SetCalInfoAttributeBoolRequest\x1a-.nidaqmx_grpc.SetCalInfoAttributeBoolResponse\x12|\n\x19SetCalInfoAttributeDouble\x12..nidaqmx_grpc.SetCalInfoAttributeDoubleRequest\x1a/.nidaqmx_grpc.SetCalInfoAttributeDoubleResponse\x12|\n\x19SetCalInfoAttributeString\x12..nidaqmx_grpc.SetCalInfoAttributeStringRequest\x1a/.nidaqmx_grpc.SetCalInfoAttributeStringResponse\x12|\n\x19SetCalInfoAttributeUInt32\x12..nidaqmx_grpc.SetCalInfoAttributeUInt32Request\x1a/.nidaqmx_grpc.SetCalInfoAttributeUInt32Response\x12m\n\x14SetChanAttributeBool\x12).nidaqmx_grpc.SetChanAttributeBoolRequest\x1a*.nidaqmx_grpc.SetChanAttributeBoolResponse\x12s\n\x16SetChanAttributeDouble\x12+.nidaqmx_grpc.SetChanAttributeDoubleRequest\x1a,.nidaqmx_grpc.SetChanAttributeDoubleResponse\x12\x82\x01\n\x1bSetChanAttributeDoubleArray\x120.nidaqmx_grpc.SetChanAttributeDoubleArrayRequest\x1a1.nidaqmx_grpc.SetChanAttributeDoubleArrayResponse\x12p\n\x15SetChanAttributeInt32\x12*.nidaqmx_grpc.SetChanAttributeInt32Request\x1a+.nidaqmx_grpc.SetChanAttributeInt32Response\x12s\n\x16SetChanAttributeString\x12+.nidaqmx_grpc.SetChanAttributeStringRequest\x1a,.nidaqmx_grpc.SetChanAttributeStringResponse\x12s\n\x16SetChanAttributeUInt32\x12+.nidaqmx_grpc.SetChanAttributeUInt32Request\x1a,.nidaqmx_grpc.SetChanAttributeUInt32Response\x12\x94\x01\n!SetDigitalLogicFamilyPowerUpState\x126.nidaqmx_grpc.SetDigitalLogicFamilyPowerUpStateRequest\x1a7.nidaqmx_grpc.SetDigitalLogicFamilyPowerUpStateResponse\x12v\n\x17SetDigitalPowerUpStates\x12,.nidaqmx_grpc.SetDigitalPowerUpStatesRequest\x1a-.nidaqmx_grpc.SetDigitalPowerUpStatesResponse\x12\x8b\x01\n\x1eSetDigitalPullUpPullDownStates\x123.nidaqmx_grpc.SetDigitalPullUpPullDownStatesRequest\x1a4.nidaqmx_grpc.SetDigitalPullUpPullDownStatesResponse\x12\x8b\x01\n\x1eSetExportedSignalAttributeBool\x123.nidaqmx_grpc.SetExportedSignalAttributeBoolRequest\x1a4.nidaqmx_grpc.SetExportedSignalAttributeBoolResponse\x12\x91\x01\n SetExportedSignalAttributeDouble\x125.nidaqmx_grpc.SetExportedSignalAttributeDoubleRequest\x1a6.nidaqmx_grpc.SetExportedSignalAttributeDoubleResponse\x12\x8e\x01\n\x1fSetExportedSignalAttributeInt32\x124.nidaqmx_grpc.SetExportedSignalAttributeInt32Request\x1a5.nidaqmx_grpc.SetExportedSignalAttributeInt32Response\x12\x91\x01\n SetExportedSignalAttributeString\x125.nidaqmx_grpc.SetExportedSignalAttributeStringRequest\x1a6.nidaqmx_grpc.SetExportedSignalAttributeStringResponse\x12\x91\x01\n SetExportedSignalAttributeUInt32\x125.nidaqmx_grpc.SetExportedSignalAttributeUInt32Request\x1a6.nidaqmx_grpc.SetExportedSignalAttributeUInt32Response\x12j\n\x13SetFirstSampClkWhen\x12(.nidaqmx_grpc.SetFirstSampClkWhenRequest\x1a).nidaqmx_grpc.SetFirstSampClkWhenResponse\x12m\n\x14SetReadAttributeBool\x12).nidaqmx_grpc.SetReadAttributeBoolRequest\x1a*.nidaqmx_grpc.SetReadAttributeBoolResponse\x12s\n\x16SetReadAttributeDouble\x12+.nidaqmx_grpc.SetReadAttributeDoubleRequest\x1a,.nidaqmx_grpc.SetReadAttributeDoubleResponse\x12p\n\x15SetReadAttributeInt32\x12*.nidaqmx_grpc.SetReadAttributeInt32Request\x1a+.nidaqmx_grpc.SetReadAttributeInt32Response\x12s\n\x16SetReadAttributeString\x12+.nidaqmx_grpc.SetReadAttributeStringRequest\x1a,.nidaqmx_grpc.SetReadAttributeStringResponse\x12s\n\x16SetReadAttributeUInt32\x12+.nidaqmx_grpc.SetReadAttributeUInt32Request\x1a,.nidaqmx_grpc.SetReadAttributeUInt32Response\x12s\n\x16SetReadAttributeUInt64\x12+.nidaqmx_grpc.SetReadAttributeUInt64Request\x1a,.nidaqmx_grpc.SetReadAttributeUInt64Response\x12y\n\x18SetRealTimeAttributeBool\x12-.nidaqmx_grpc.SetRealTimeAttributeBoolRequest\x1a..nidaqmx_grpc.SetRealTimeAttributeBoolResponse\x12|\n\x19SetRealTimeAttributeInt32\x12..nidaqmx_grpc.SetRealTimeAttributeInt32Request\x1a/.nidaqmx_grpc.SetRealTimeAttributeInt32Response\x12\x7f\n\x1aSetRealTimeAttributeUInt32\x12/.nidaqmx_grpc.SetRealTimeAttributeUInt32Request\x1a0.nidaqmx_grpc.SetRealTimeAttributeUInt32Response\x12v\n\x17SetScaleAttributeDouble\x12,.nidaqmx_grpc.SetScaleAttributeDoubleRequest\x1a-.nidaqmx_grpc.SetScaleAttributeDoubleResponse\x12\x85\x01\n\x1cSetScaleAttributeDoubleArray\x121.nidaqmx_grpc.SetScaleAttributeDoubleArrayRequest\x1a2.nidaqmx_grpc.SetScaleAttributeDoubleArrayResponse\x12s\n\x16SetScaleAttributeInt32\x12+.nidaqmx_grpc.SetScaleAttributeInt32Request\x1a,.nidaqmx_grpc.SetScaleAttributeInt32Response\x12v\n\x17SetScaleAttributeString\x12,.nidaqmx_grpc.SetScaleAttributeStringRequest\x1a-.nidaqmx_grpc.SetScaleAttributeStringResponse\x12m\n\x14SetStartTrigTrigWhen\x12).nidaqmx_grpc.SetStartTrigTrigWhenRequest\x1a*.nidaqmx_grpc.SetStartTrigTrigWhenResponse\x12m\n\x14SetSyncPulseTimeWhen\x12).nidaqmx_grpc.SetSyncPulseTimeWhenRequest\x1a*.nidaqmx_grpc.SetSyncPulseTimeWhenResponse\x12s\n\x16SetTimingAttributeBool\x12+.nidaqmx_grpc.SetTimingAttributeBoolRequest\x1a,.nidaqmx_grpc.SetTimingAttributeBoolResponse\x12y\n\x18SetTimingAttributeDouble\x12-.nidaqmx_grpc.SetTimingAttributeDoubleRequest\x1a..nidaqmx_grpc.SetTimingAttributeDoubleResponse\x12y\n\x18SetTimingAttributeExBool\x12-.nidaqmx_grpc.SetTimingAttributeExBoolRequest\x1a..nidaqmx_grpc.SetTimingAttributeExBoolResponse\x12\x7f\n\x1aSetTimingAttributeExDouble\x12/.nidaqmx_grpc.SetTimingAttributeExDoubleRequest\x1a0.nidaqmx_grpc.SetTimingAttributeExDoubleResponse\x12|\n\x19SetTimingAttributeExInt32\x12..nidaqmx_grpc.SetTimingAttributeExInt32Request\x1a/.nidaqmx_grpc.SetTimingAttributeExInt32Response\x12\x7f\n\x1aSetTimingAttributeExString\x12/.nidaqmx_grpc.SetTimingAttributeExStringRequest\x1a0.nidaqmx_grpc.SetTimingAttributeExStringResponse\x12\x88\x01\n\x1dSetTimingAttributeExTimestamp\x122.nidaqmx_grpc.SetTimingAttributeExTimestampRequest\x1a3.nidaqmx_grpc.SetTimingAttributeExTimestampResponse\x12\x7f\n\x1aSetTimingAttributeExUInt32\x12/.nidaqmx_grpc.SetTimingAttributeExUInt32Request\x1a0.nidaqmx_grpc.SetTimingAttributeExUInt32Response\x12\x7f\n\x1aSetTimingAttributeExUInt64\x12/.nidaqmx_grpc.SetTimingAttributeExUInt64Request\x1a0.nidaqmx_grpc.SetTimingAttributeExUInt64Response\x12v\n\x17SetTimingAttributeInt32\x12,.nidaqmx_grpc.SetTimingAttributeInt32Request\x1a-.nidaqmx_grpc.SetTimingAttributeInt32Response\x12y\n\x18SetTimingAttributeString\x12-.nidaqmx_grpc.SetTimingAttributeStringRequest\x1a..nidaqmx_grpc.SetTimingAttributeStringResponse\x12\x82\x01\n\x1bSetTimingAttributeTimestamp\x120.nidaqmx_grpc.SetTimingAttributeTimestampRequest\x1a1.nidaqmx_grpc.SetTimingAttributeTimestampResponse\x12y\n\x18SetTimingAttributeUInt32\x12-.nidaqmx_grpc.SetTimingAttributeUInt32Request\x1a..nidaqmx_grpc.SetTimingAttributeUInt32Response\x12y\n\x18SetTimingAttributeUInt64\x12-.nidaqmx_grpc.SetTimingAttributeUInt64Request\x1a..nidaqmx_grpc.SetTimingAttributeUInt64Response\x12m\n\x14SetTrigAttributeBool\x12).nidaqmx_grpc.SetTrigAttributeBoolRequest\x1a*.nidaqmx_grpc.SetTrigAttributeBoolResponse\x12s\n\x16SetTrigAttributeDouble\x12+.nidaqmx_grpc.SetTrigAttributeDoubleRequest\x1a,.nidaqmx_grpc.SetTrigAttributeDoubleResponse\x12\x82\x01\n\x1bSetTrigAttributeDoubleArray\x120.nidaqmx_grpc.SetTrigAttributeDoubleArrayRequest\x1a1.nidaqmx_grpc.SetTrigAttributeDoubleArrayResponse\x12p\n\x15SetTrigAttributeInt32\x12*.nidaqmx_grpc.SetTrigAttributeInt32Request\x1a+.nidaqmx_grpc.SetTrigAttributeInt32Response\x12\x7f\n\x1aSetTrigAttributeInt32Array\x12/.nidaqmx_grpc.SetTrigAttributeInt32ArrayRequest\x1a0.nidaqmx_grpc.SetTrigAttributeInt32ArrayResponse\x12s\n\x16SetTrigAttributeString\x12+.nidaqmx_grpc.SetTrigAttributeStringRequest\x1a,.nidaqmx_grpc.SetTrigAttributeStringResponse\x12|\n\x19SetTrigAttributeTimestamp\x12..nidaqmx_grpc.SetTrigAttributeTimestampRequest\x1a/.nidaqmx_grpc.SetTrigAttributeTimestampResponse\x12s\n\x16SetTrigAttributeUInt32\x12+.nidaqmx_grpc.SetTrigAttributeUInt32Request\x1a,.nidaqmx_grpc.SetTrigAttributeUInt32Response\x12y\n\x18SetWatchdogAttributeBool\x12-.nidaqmx_grpc.SetWatchdogAttributeBoolRequest\x1a..nidaqmx_grpc.SetWatchdogAttributeBoolResponse\x12\x7f\n\x1aSetWatchdogAttributeDouble\x12/.nidaqmx_grpc.SetWatchdogAttributeDoubleRequest\x1a0.nidaqmx_grpc.SetWatchdogAttributeDoubleResponse\x12|\n\x19SetWatchdogAttributeInt32\x12..nidaqmx_grpc.SetWatchdogAttributeInt32Request\x1a/.nidaqmx_grpc.SetWatchdogAttributeInt32Response\x12\x7f\n\x1aSetWatchdogAttributeString\x12/.nidaqmx_grpc.SetWatchdogAttributeStringRequest\x1a0.nidaqmx_grpc.SetWatchdogAttributeStringResponse\x12p\n\x15SetWriteAttributeBool\x12*.nidaqmx_grpc.SetWriteAttributeBoolRequest\x1a+.nidaqmx_grpc.SetWriteAttributeBoolResponse\x12v\n\x17SetWriteAttributeDouble\x12,.nidaqmx_grpc.SetWriteAttributeDoubleRequest\x1a-.nidaqmx_grpc.SetWriteAttributeDoubleResponse\x12s\n\x16SetWriteAttributeInt32\x12+.nidaqmx_grpc.SetWriteAttributeInt32Request\x1a,.nidaqmx_grpc.SetWriteAttributeInt32Response\x12v\n\x17SetWriteAttributeString\x12,.nidaqmx_grpc.SetWriteAttributeStringRequest\x1a-.nidaqmx_grpc.SetWriteAttributeStringResponse\x12v\n\x17SetWriteAttributeUInt32\x12,.nidaqmx_grpc.SetWriteAttributeUInt32Request\x1a-.nidaqmx_grpc.SetWriteAttributeUInt32Response\x12v\n\x17SetWriteAttributeUInt64\x12,.nidaqmx_grpc.SetWriteAttributeUInt64Request\x1a-.nidaqmx_grpc.SetWriteAttributeUInt64Response\x12U\n\x0cStartNewFile\x12!.nidaqmx_grpc.StartNewFileRequest\x1a".nidaqmx_grpc.StartNewFileResponse\x12L\n\tStartTask\x12\x1e.nidaqmx_grpc.StartTaskRequest\x1a\x1f.nidaqmx_grpc.StartTaskResponse\x12I\n\x08StopTask\x12\x1d.nidaqmx_grpc.StopTaskRequest\x1a\x1e.nidaqmx_grpc.StopTaskResponse\x12R\n\x0bTaskControl\x12 .nidaqmx_grpc.TaskControlRequest\x1a!.nidaqmx_grpc.TaskControlResponse\x12g\n\x12TristateOutputTerm\x12\'.nidaqmx_grpc.TristateOutputTermRequest\x1a(.nidaqmx_grpc.TristateOutputTermResponse\x12j\n\x13UnregisterDoneEvent\x12(.nidaqmx_grpc.UnregisterDoneEventRequest\x1a).nidaqmx_grpc.UnregisterDoneEventResponse\x12\x85\x01\n\x1cUnregisterEveryNSamplesEvent\x121.nidaqmx_grpc.UnregisterEveryNSamplesEventRequest\x1a2.nidaqmx_grpc.UnregisterEveryNSamplesEventResponse\x12p\n\x15UnregisterSignalEvent\x12*.nidaqmx_grpc.UnregisterSignalEventRequest\x1a+.nidaqmx_grpc.UnregisterSignalEventResponse\x12s\n\x16UnreserveNetworkDevice\x12+.nidaqmx_grpc.UnreserveNetworkDeviceRequest\x1a,.nidaqmx_grpc.UnreserveNetworkDeviceResponse\x12s\n\x16WaitForNextSampleClock\x12+.nidaqmx_grpc.WaitForNextSampleClockRequest\x1a,.nidaqmx_grpc.WaitForNextSampleClockResponse\x12\x82\x01\n\x1bBeginWaitForNextSampleClock\x120.nidaqmx_grpc.BeginWaitForNextSampleClockRequest\x1a1.nidaqmx_grpc.BeginWaitForNextSampleClockResponse\x12p\n\x15WaitForValidTimestamp\x12*.nidaqmx_grpc.WaitForValidTimestampRequest\x1a+.nidaqmx_grpc.WaitForValidTimestampResponse\x12d\n\x11WaitUntilTaskDone\x12&.nidaqmx_grpc.WaitUntilTaskDoneRequest\x1a\'.nidaqmx_grpc.WaitUntilTaskDoneResponse\x12[\n\x0eWriteAnalogF64\x12#.nidaqmx_grpc.WriteAnalogF64Request\x1a$.nidaqmx_grpc.WriteAnalogF64Response\x12j\n\x13BeginWriteAnalogF64\x12(.nidaqmx_grpc.BeginWriteAnalogF64Request\x1a).nidaqmx_grpc.BeginWriteAnalogF64Response\x12m\n\x14WriteAnalogScalarF64\x12).nidaqmx_grpc.WriteAnalogScalarF64Request\x1a*.nidaqmx_grpc.WriteAnalogScalarF64Response\x12|\n\x19BeginWriteAnalogScalarF64\x12..nidaqmx_grpc.BeginWriteAnalogScalarF64Request\x1a/.nidaqmx_grpc.BeginWriteAnalogScalarF64Response\x12[\n\x0eWriteBinaryI16\x12#.nidaqmx_grpc.WriteBinaryI16Request\x1a$.nidaqmx_grpc.WriteBinaryI16Response\x12j\n\x13BeginWriteBinaryI16\x12(.nidaqmx_grpc.BeginWriteBinaryI16Request\x1a).nidaqmx_grpc.BeginWriteBinaryI16Response\x12[\n\x0eWriteBinaryI32\x12#.nidaqmx_grpc.WriteBinaryI32Request\x1a$.nidaqmx_grpc.WriteBinaryI32Response\x12j\n\x13BeginWriteBinaryI32\x12(.nidaqmx_grpc.BeginWriteBinaryI32Request\x1a).nidaqmx_grpc.BeginWriteBinaryI32Response\x12[\n\x0eWriteBinaryU16\x12#.nidaqmx_grpc.WriteBinaryU16Request\x1a$.nidaqmx_grpc.WriteBinaryU16Response\x12j\n\x13BeginWriteBinaryU16\x12(.nidaqmx_grpc.BeginWriteBinaryU16Request\x1a).nidaqmx_grpc.BeginWriteBinaryU16Response\x12[\n\x0eWriteBinaryU32\x12#.nidaqmx_grpc.WriteBinaryU32Request\x1a$.nidaqmx_grpc.WriteBinaryU32Response\x12j\n\x13BeginWriteBinaryU32\x12(.nidaqmx_grpc.BeginWriteBinaryU32Request\x1a).nidaqmx_grpc.BeginWriteBinaryU32Response\x12U\n\x0cWriteCtrFreq\x12!.nidaqmx_grpc.WriteCtrFreqRequest\x1a".nidaqmx_grpc.WriteCtrFreqResponse\x12d\n\x11BeginWriteCtrFreq\x12&.nidaqmx_grpc.BeginWriteCtrFreqRequest\x1a\'.nidaqmx_grpc.BeginWriteCtrFreqResponse\x12g\n\x12WriteCtrFreqScalar\x12\'.nidaqmx_grpc.WriteCtrFreqScalarRequest\x1a(.nidaqmx_grpc.WriteCtrFreqScalarResponse\x12v\n\x17BeginWriteCtrFreqScalar\x12,.nidaqmx_grpc.BeginWriteCtrFreqScalarRequest\x1a-.nidaqmx_grpc.BeginWriteCtrFreqScalarResponse\x12X\n\rWriteCtrTicks\x12".nidaqmx_grpc.WriteCtrTicksRequest\x1a#.nidaqmx_grpc.WriteCtrTicksResponse\x12g\n\x12BeginWriteCtrTicks\x12\'.nidaqmx_grpc.BeginWriteCtrTicksRequest\x1a(.nidaqmx_grpc.BeginWriteCtrTicksResponse\x12j\n\x13WriteCtrTicksScalar\x12(.nidaqmx_grpc.WriteCtrTicksScalarRequest\x1a).nidaqmx_grpc.WriteCtrTicksScalarResponse\x12y\n\x18BeginWriteCtrTicksScalar\x12-.nidaqmx_grpc.BeginWriteCtrTicksScalarRequest\x1a..nidaqmx_grpc.BeginWriteCtrTicksScalarResponse\x12U\n\x0cWriteCtrTime\x12!.nidaqmx_grpc.WriteCtrTimeRequest\x1a".nidaqmx_grpc.WriteCtrTimeResponse\x12d\n\x11BeginWriteCtrTime\x12&.nidaqmx_grpc.BeginWriteCtrTimeRequest\x1a\'.nidaqmx_grpc.BeginWriteCtrTimeResponse\x12g\n\x12WriteCtrTimeScalar\x12\'.nidaqmx_grpc.WriteCtrTimeScalarRequest\x1a(.nidaqmx_grpc.WriteCtrTimeScalarResponse\x12v\n\x17BeginWriteCtrTimeScalar\x12,.nidaqmx_grpc.BeginWriteCtrTimeScalarRequest\x1a-.nidaqmx_grpc.BeginWriteCtrTimeScalarResponse\x12d\n\x11WriteDigitalLines\x12&.nidaqmx_grpc.WriteDigitalLinesRequest\x1a\'.nidaqmx_grpc.WriteDigitalLinesResponse\x12s\n\x16BeginWriteDigitalLines\x12+.nidaqmx_grpc.BeginWriteDigitalLinesRequest\x1a,.nidaqmx_grpc.BeginWriteDigitalLinesResponse\x12p\n\x15WriteDigitalScalarU32\x12*.nidaqmx_grpc.WriteDigitalScalarU32Request\x1a+.nidaqmx_grpc.WriteDigitalScalarU32Response\x12\x7f\n\x1aBeginWriteDigitalScalarU32\x12/.nidaqmx_grpc.BeginWriteDigitalScalarU32Request\x1a0.nidaqmx_grpc.BeginWriteDigitalScalarU32Response\x12^\n\x0fWriteDigitalU16\x12$.nidaqmx_grpc.WriteDigitalU16Request\x1a%.nidaqmx_grpc.WriteDigitalU16Response\x12m\n\x14BeginWriteDigitalU16\x12).nidaqmx_grpc.BeginWriteDigitalU16Request\x1a*.nidaqmx_grpc.BeginWriteDigitalU16Response\x12^\n\x0fWriteDigitalU32\x12$.nidaqmx_grpc.WriteDigitalU32Request\x1a%.nidaqmx_grpc.WriteDigitalU32Response\x12m\n\x14BeginWriteDigitalU32\x12).nidaqmx_grpc.BeginWriteDigitalU32Request\x1a*.nidaqmx_grpc.BeginWriteDigitalU32Response\x12[\n\x0eWriteDigitalU8\x12#.nidaqmx_grpc.WriteDigitalU8Request\x1a$.nidaqmx_grpc.WriteDigitalU8Response\x12j\n\x13BeginWriteDigitalU8\x12(.nidaqmx_grpc.BeginWriteDigitalU8Request\x1a).nidaqmx_grpc.BeginWriteDigitalU8Response\x12a\n\x10WriteIDPinMemory\x12%.nidaqmx_grpc.WriteIDPinMemoryRequest\x1a&.nidaqmx_grpc.WriteIDPinMemoryResponse\x12I\n\x08WriteRaw\x12\x1d.nidaqmx_grpc.WriteRawRequest\x1a\x1e.nidaqmx_grpc.WriteRawResponse\x12X\n\rBeginWriteRaw\x12".nidaqmx_grpc.BeginWriteRawRequest\x1a#.nidaqmx_grpc.BeginWriteRawResponse\x12m\n\x14WriteToTEDSFromArray\x12).nidaqmx_grpc.WriteToTEDSFromArrayRequest\x1a*.nidaqmx_grpc.WriteToTEDSFromArrayResponse\x12j\n\x13WriteToTEDSFromFile\x12(.nidaqmx_grpc.WriteToTEDSFromFileRequest\x1a).nidaqmx_grpc.WriteToTEDSFromFileResponse\x12j\n\x13ReadAnalogWaveforms\x12(.nidaqmx_grpc.ReadAnalogWaveformsRequest\x1a).nidaqmx_grpc.ReadAnalogWaveformsResponse\x12m\n\x14ReadDigitalWaveforms\x12).nidaqmx_grpc.ReadDigitalWaveformsRequest\x1a*.nidaqmx_grpc.ReadDigitalWaveformsResponse\x12m\n\x14WriteAnalogWaveforms\x12).nidaqmx_grpc.WriteAnalogWaveformsRequest\x1a*.nidaqmx_grpc.WriteAnalogWaveformsResponse\x12p\n\x15WriteDigitalWaveforms\x12*.nidaqmx_grpc.WriteDigitalWaveformsRequest\x1a+.nidaqmx_grpc.WriteDigitalWaveformsResponseBF\n\x13com.ni.grpc.nidaqmxB\x07NiDAQmxP\x01\xf8\x01\x01\xaa\x02 NationalInstruments.Grpc.NiDAQmxb\x06proto3')`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/_stubs/nidaqmx_pb2_grpc.py -->
## PYTHON MODULE: generated/nidaqmx/_stubs/nidaqmx_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

### `class NiDAQmxStub(object)`

Missing associated documentation comment in .proto file.

#### `def __init__(self, channel)`

Constructor.

        Args:
            channel: A grpc.Channel.
        

### `class NiDAQmxServicer(object)`

Missing associated documentation comment in .proto file.

#### `def AddCDAQSyncConnection(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def AddGlobalChansToTask(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def AddNetworkDevice(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def AreConfiguredCDAQSyncPortsDisconnected(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def AutoConfigureCDAQSyncConnections(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CalculateReversePolyCoeff(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CfgAnlgEdgeRefTrig(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CfgAnlgEdgeStartTrig(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CfgAnlgMultiEdgeRefTrig(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CfgAnlgMultiEdgeStartTrig(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CfgAnlgWindowRefTrig(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CfgAnlgWindowStartTrig(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CfgBurstHandshakingTimingExportClock(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CfgBurstHandshakingTimingImportClock(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CfgChangeDetectionTiming(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CfgDigEdgeRefTrig(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CfgDigEdgeStartTrig(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CfgDigPatternRefTrig(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CfgDigPatternStartTrig(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CfgHandshakingTiming(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CfgImplicitTiming(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CfgInputBuffer(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CfgOutputBuffer(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CfgPipelinedSampClkTiming(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CfgSampClkTiming(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CfgTimeStartTrig(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CfgWatchdogAOExpirStates(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CfgWatchdogCOExpirStates(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CfgWatchdogDOExpirStates(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClearTEDS(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClearTask(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureLogging(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureTEDS(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConnectTerms(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ControlWatchdogTask(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIAccel4WireDCVoltageChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIAccelChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIAccelChargeChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIBridgeChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAICalculatedPowerChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIChargeChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAICurrentChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAICurrentRMSChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIForceBridgePolynomialChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIForceBridgeTableChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIForceBridgeTwoPointLinChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIForceIEPEChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIFreqVoltageChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIMicrophoneChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIPosEddyCurrProxProbeChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIPosLVDTChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIPosRVDTChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIPowerChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIPressureBridgePolynomialChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIPressureBridgeTableChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIPressureBridgeTwoPointLinChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIRTDChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIResistanceChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIRosetteStrainGageChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIStrainGageChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAITempBuiltInSensorChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIThrmcplChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIThrmstrChanIex(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIThrmstrChanVex(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAITorqueBridgePolynomialChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAITorqueBridgeTableChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAITorqueBridgeTwoPointLinChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIVelocityIEPEChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIVoltageChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIVoltageChanWithExcit(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAIVoltageRMSChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAOCurrentChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAOFuncGenChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAOVoltageChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateCIAngEncoderChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateCIAngVelocityChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateCICountEdgesChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateCIDutyCycleChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateCIFreqChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateCIGPSTimestampChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateCILinEncoderChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateCILinVelocityChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateCIPeriodChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateCIPulseChanFreq(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateCIPulseChanTicks(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateCIPulseChanTime(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateCIPulseWidthChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateCISemiPeriodChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateCITwoEdgeSepChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateCOPulseChanFreq(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateCOPulseChanTicks(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateCOPulseChanTime(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateDIChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateDOChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateLinScale(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateMapScale(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreatePolynomialScale(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateTEDSAIAccelChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateTEDSAIBridgeChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateTEDSAICurrentChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateTEDSAIForceBridgeChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateTEDSAIForceIEPEChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateTEDSAIMicrophoneChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateTEDSAIPosLVDTChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateTEDSAIPosRVDTChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateTEDSAIPressureBridgeChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateTEDSAIRTDChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateTEDSAIResistanceChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateTEDSAIStrainGageChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateTEDSAIThrmcplChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateTEDSAIThrmstrChanIex(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateTEDSAIThrmstrChanVex(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateTEDSAITorqueBridgeChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateTEDSAIVoltageChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateTEDSAIVoltageChanWithExcit(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateTableScale(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateTask(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateWatchdogTimerTask(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateWatchdogTimerTaskEx(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DeleteNetworkDevice(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DeleteSavedGlobalChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DeleteSavedScale(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DeleteSavedTask(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DeviceSupportsCal(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisableRefTrig(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisableStartTrig(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisconnectTerms(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ExportSignal(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAIChanCalCalDate(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAIChanCalExpDate(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAnalogPowerUpStates(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAnalogPowerUpStatesWithOutputType(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetArmStartTrigTimestampVal(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetArmStartTrigTrigWhen(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAutoConfiguredCDAQSyncConnections(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetBufferAttributeUInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetCalInfoAttributeBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetCalInfoAttributeDouble(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetCalInfoAttributeString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetCalInfoAttributeUInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetChanAttributeBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetChanAttributeDouble(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetChanAttributeDoubleArray(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetChanAttributeInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetChanAttributeString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetChanAttributeUInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetDeviceAttributeBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetDeviceAttributeDouble(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetDeviceAttributeDoubleArray(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetDeviceAttributeInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetDeviceAttributeInt32Array(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetDeviceAttributeString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetDeviceAttributeUInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetDeviceAttributeUInt32Array(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetDigitalLogicFamilyPowerUpState(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetDigitalPowerUpStates(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetDigitalPullUpPullDownStates(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetDisconnectedCDAQSyncPorts(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetErrorString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetExportedSignalAttributeBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetExportedSignalAttributeDouble(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetExportedSignalAttributeInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetExportedSignalAttributeString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetExportedSignalAttributeUInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetExtCalLastDateAndTime(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetFirstSampClkWhen(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetFirstSampTimestampVal(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetNthTaskChannel(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetNthTaskDevice(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetNthTaskReadChannel(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetPersistedChanAttributeBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetPersistedChanAttributeString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetPersistedScaleAttributeBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetPersistedScaleAttributeString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetPersistedTaskAttributeBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetPersistedTaskAttributeString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetPhysicalChanAttributeBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetPhysicalChanAttributeBytes(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetPhysicalChanAttributeDouble(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetPhysicalChanAttributeDoubleArray(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetPhysicalChanAttributeInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetPhysicalChanAttributeInt32Array(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetPhysicalChanAttributeString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetPhysicalChanAttributeUInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetPhysicalChanAttributeUInt32Array(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetReadAttributeBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetReadAttributeDouble(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetReadAttributeInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetReadAttributeString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetReadAttributeUInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetReadAttributeUInt64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetRealTimeAttributeBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetRealTimeAttributeInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetRealTimeAttributeUInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetRefTrigTimestampVal(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetScaleAttributeDouble(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetScaleAttributeDoubleArray(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetScaleAttributeInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetScaleAttributeString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetSelfCalLastDateAndTime(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetStartTrigTimestampVal(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetStartTrigTrigWhen(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetSyncPulseTimeWhen(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetSystemInfoAttributeString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetSystemInfoAttributeUInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTaskAttributeBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTaskAttributeString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTaskAttributeUInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTimingAttributeBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTimingAttributeDouble(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTimingAttributeExBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTimingAttributeExDouble(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTimingAttributeExInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTimingAttributeExString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTimingAttributeExTimestamp(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTimingAttributeExUInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTimingAttributeExUInt64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTimingAttributeInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTimingAttributeString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTimingAttributeTimestamp(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTimingAttributeUInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTimingAttributeUInt64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTrigAttributeBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTrigAttributeDouble(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTrigAttributeDoubleArray(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTrigAttributeInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTrigAttributeInt32Array(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTrigAttributeString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTrigAttributeTimestamp(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTrigAttributeUInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetWatchdogAttributeBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetWatchdogAttributeDouble(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetWatchdogAttributeInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetWatchdogAttributeString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetWriteAttributeBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetWriteAttributeDouble(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetWriteAttributeInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetWriteAttributeString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetWriteAttributeUInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetWriteAttributeUInt64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def IsTaskDone(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def LoadTask(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def PerformBridgeOffsetNullingCalEx(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def PerformBridgeShuntCalEx(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def PerformStrainShuntCalEx(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def PerformThrmcplLeadOffsetNullingCal(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadAnalogF64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadAnalogF64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadAnalogScalarF64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadAnalogScalarF64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadBinaryI16(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadBinaryI16(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadBinaryI32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadBinaryI32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadBinaryU16(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadBinaryU16(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadBinaryU32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadBinaryU32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadCounterF64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadCounterF64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadCounterF64Ex(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadCounterF64Ex(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadCounterScalarF64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadCounterScalarF64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadCounterScalarU32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadCounterScalarU32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadCounterU32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadCounterU32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadCounterU32Ex(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadCounterU32Ex(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadCtrFreq(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadCtrFreq(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadCtrFreqScalar(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadCtrFreqScalar(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadCtrTicks(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadCtrTicks(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadCtrTicksScalar(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadCtrTicksScalar(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadCtrTime(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadCtrTime(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadCtrTimeScalar(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadCtrTimeScalar(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadDigitalLines(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadDigitalLines(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadDigitalScalarU32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadDigitalScalarU32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadDigitalU16(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadDigitalU16(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadDigitalU32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadDigitalU32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadDigitalU8(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadDigitalU8(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadIDPinMemory(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadPowerBinaryI16(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadPowerBinaryI16(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadPowerF64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadPowerF64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadPowerScalarF64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadPowerScalarF64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadRaw(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginReadRaw(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def RegisterDoneEvent(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def RegisterEveryNSamplesEvent(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def RegisterSignalEvent(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def RemoveCDAQSyncConnection(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReserveNetworkDevice(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetBufferAttribute(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetChanAttribute(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetDevice(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetExportedSignalAttribute(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetReadAttribute(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetRealTimeAttribute(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetTimingAttribute(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetTimingAttributeEx(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetTrigAttribute(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetWatchdogAttribute(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetWriteAttribute(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def RestoreLastExtCalConst(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SaveGlobalChan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SaveScale(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SaveTask(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SelfCal(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SelfTestDevice(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAIChanCalCalDate(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAIChanCalExpDate(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAnalogPowerUpStates(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAnalogPowerUpStatesWithOutputType(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetArmStartTrigTrigWhen(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetBufferAttributeUInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetCalInfoAttributeBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetCalInfoAttributeDouble(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetCalInfoAttributeString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetCalInfoAttributeUInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetChanAttributeBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetChanAttributeDouble(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetChanAttributeDoubleArray(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetChanAttributeInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetChanAttributeString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetChanAttributeUInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetDigitalLogicFamilyPowerUpState(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetDigitalPowerUpStates(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetDigitalPullUpPullDownStates(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetExportedSignalAttributeBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetExportedSignalAttributeDouble(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetExportedSignalAttributeInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetExportedSignalAttributeString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetExportedSignalAttributeUInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetFirstSampClkWhen(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetReadAttributeBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetReadAttributeDouble(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetReadAttributeInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetReadAttributeString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetReadAttributeUInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetReadAttributeUInt64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetRealTimeAttributeBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetRealTimeAttributeInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetRealTimeAttributeUInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetScaleAttributeDouble(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetScaleAttributeDoubleArray(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetScaleAttributeInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetScaleAttributeString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetStartTrigTrigWhen(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetSyncPulseTimeWhen(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetTimingAttributeBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetTimingAttributeDouble(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetTimingAttributeExBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetTimingAttributeExDouble(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetTimingAttributeExInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetTimingAttributeExString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetTimingAttributeExTimestamp(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetTimingAttributeExUInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetTimingAttributeExUInt64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetTimingAttributeInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetTimingAttributeString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetTimingAttributeTimestamp(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetTimingAttributeUInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetTimingAttributeUInt64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetTrigAttributeBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetTrigAttributeDouble(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetTrigAttributeDoubleArray(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetTrigAttributeInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetTrigAttributeInt32Array(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetTrigAttributeString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetTrigAttributeTimestamp(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetTrigAttributeUInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetWatchdogAttributeBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetWatchdogAttributeDouble(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetWatchdogAttributeInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetWatchdogAttributeString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetWriteAttributeBool(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetWriteAttributeDouble(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetWriteAttributeInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetWriteAttributeString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetWriteAttributeUInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetWriteAttributeUInt64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def StartNewFile(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def StartTask(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def StopTask(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def TaskControl(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def TristateOutputTerm(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def UnregisterDoneEvent(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def UnregisterEveryNSamplesEvent(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def UnregisterSignalEvent(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def UnreserveNetworkDevice(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WaitForNextSampleClock(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginWaitForNextSampleClock(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WaitForValidTimestamp(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WaitUntilTaskDone(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteAnalogF64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginWriteAnalogF64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteAnalogScalarF64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginWriteAnalogScalarF64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteBinaryI16(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginWriteBinaryI16(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteBinaryI32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginWriteBinaryI32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteBinaryU16(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginWriteBinaryU16(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteBinaryU32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginWriteBinaryU32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteCtrFreq(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginWriteCtrFreq(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteCtrFreqScalar(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginWriteCtrFreqScalar(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteCtrTicks(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginWriteCtrTicks(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteCtrTicksScalar(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginWriteCtrTicksScalar(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteCtrTime(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginWriteCtrTime(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteCtrTimeScalar(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginWriteCtrTimeScalar(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteDigitalLines(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginWriteDigitalLines(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteDigitalScalarU32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginWriteDigitalScalarU32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteDigitalU16(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginWriteDigitalU16(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteDigitalU32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginWriteDigitalU32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteDigitalU8(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginWriteDigitalU8(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteIDPinMemory(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteRaw(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BeginWriteRaw(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteToTEDSFromArray(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteToTEDSFromFile(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadAnalogWaveforms(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadDigitalWaveforms(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteAnalogWaveforms(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteDigitalWaveforms(self, request, context)`

Missing associated documentation comment in .proto file.

### `def add_NiDAQmxServicer_to_server(servicer, server)`

### `class NiDAQmx(object)`

Missing associated documentation comment in .proto file.

#### `def AddCDAQSyncConnection(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def AddGlobalChansToTask(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def AddNetworkDevice(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def AreConfiguredCDAQSyncPortsDisconnected(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def AutoConfigureCDAQSyncConnections(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CalculateReversePolyCoeff(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CfgAnlgEdgeRefTrig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CfgAnlgEdgeStartTrig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CfgAnlgMultiEdgeRefTrig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CfgAnlgMultiEdgeStartTrig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CfgAnlgWindowRefTrig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CfgAnlgWindowStartTrig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CfgBurstHandshakingTimingExportClock(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CfgBurstHandshakingTimingImportClock(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CfgChangeDetectionTiming(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CfgDigEdgeRefTrig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CfgDigEdgeStartTrig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CfgDigPatternRefTrig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CfgDigPatternStartTrig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CfgHandshakingTiming(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CfgImplicitTiming(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CfgInputBuffer(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CfgOutputBuffer(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CfgPipelinedSampClkTiming(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CfgSampClkTiming(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CfgTimeStartTrig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CfgWatchdogAOExpirStates(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CfgWatchdogCOExpirStates(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CfgWatchdogDOExpirStates(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClearTEDS(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClearTask(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureLogging(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureTEDS(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConnectTerms(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ControlWatchdogTask(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIAccel4WireDCVoltageChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIAccelChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIAccelChargeChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIBridgeChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAICalculatedPowerChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIChargeChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAICurrentChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAICurrentRMSChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIForceBridgePolynomialChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIForceBridgeTableChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIForceBridgeTwoPointLinChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIForceIEPEChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIFreqVoltageChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIMicrophoneChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIPosEddyCurrProxProbeChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIPosLVDTChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIPosRVDTChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIPowerChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIPressureBridgePolynomialChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIPressureBridgeTableChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIPressureBridgeTwoPointLinChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIRTDChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIResistanceChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIRosetteStrainGageChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIStrainGageChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAITempBuiltInSensorChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIThrmcplChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIThrmstrChanIex(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIThrmstrChanVex(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAITorqueBridgePolynomialChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAITorqueBridgeTableChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAITorqueBridgeTwoPointLinChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIVelocityIEPEChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIVoltageChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIVoltageChanWithExcit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAIVoltageRMSChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAOCurrentChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAOFuncGenChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAOVoltageChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateCIAngEncoderChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateCIAngVelocityChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateCICountEdgesChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateCIDutyCycleChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateCIFreqChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateCIGPSTimestampChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateCILinEncoderChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateCILinVelocityChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateCIPeriodChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateCIPulseChanFreq(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateCIPulseChanTicks(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateCIPulseChanTime(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateCIPulseWidthChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateCISemiPeriodChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateCITwoEdgeSepChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateCOPulseChanFreq(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateCOPulseChanTicks(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateCOPulseChanTime(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateDIChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateDOChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateLinScale(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateMapScale(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreatePolynomialScale(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateTEDSAIAccelChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateTEDSAIBridgeChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateTEDSAICurrentChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateTEDSAIForceBridgeChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateTEDSAIForceIEPEChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateTEDSAIMicrophoneChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateTEDSAIPosLVDTChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateTEDSAIPosRVDTChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateTEDSAIPressureBridgeChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateTEDSAIRTDChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateTEDSAIResistanceChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateTEDSAIStrainGageChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateTEDSAIThrmcplChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateTEDSAIThrmstrChanIex(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateTEDSAIThrmstrChanVex(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateTEDSAITorqueBridgeChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateTEDSAIVoltageChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateTEDSAIVoltageChanWithExcit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateTableScale(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateTask(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateWatchdogTimerTask(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateWatchdogTimerTaskEx(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DeleteNetworkDevice(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DeleteSavedGlobalChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DeleteSavedScale(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DeleteSavedTask(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DeviceSupportsCal(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisableRefTrig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisableStartTrig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisconnectTerms(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ExportSignal(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAIChanCalCalDate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAIChanCalExpDate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAnalogPowerUpStates(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAnalogPowerUpStatesWithOutputType(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetArmStartTrigTimestampVal(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetArmStartTrigTrigWhen(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAutoConfiguredCDAQSyncConnections(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetBufferAttributeUInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetCalInfoAttributeBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetCalInfoAttributeDouble(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetCalInfoAttributeString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetCalInfoAttributeUInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetChanAttributeBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetChanAttributeDouble(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetChanAttributeDoubleArray(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetChanAttributeInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetChanAttributeString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetChanAttributeUInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetDeviceAttributeBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetDeviceAttributeDouble(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetDeviceAttributeDoubleArray(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetDeviceAttributeInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetDeviceAttributeInt32Array(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetDeviceAttributeString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetDeviceAttributeUInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetDeviceAttributeUInt32Array(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetDigitalLogicFamilyPowerUpState(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetDigitalPowerUpStates(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetDigitalPullUpPullDownStates(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetDisconnectedCDAQSyncPorts(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetErrorString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetExportedSignalAttributeBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetExportedSignalAttributeDouble(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetExportedSignalAttributeInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetExportedSignalAttributeString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetExportedSignalAttributeUInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetExtCalLastDateAndTime(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetFirstSampClkWhen(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetFirstSampTimestampVal(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetNthTaskChannel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetNthTaskDevice(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetNthTaskReadChannel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetPersistedChanAttributeBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetPersistedChanAttributeString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetPersistedScaleAttributeBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetPersistedScaleAttributeString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetPersistedTaskAttributeBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetPersistedTaskAttributeString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetPhysicalChanAttributeBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetPhysicalChanAttributeBytes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetPhysicalChanAttributeDouble(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetPhysicalChanAttributeDoubleArray(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetPhysicalChanAttributeInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetPhysicalChanAttributeInt32Array(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetPhysicalChanAttributeString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetPhysicalChanAttributeUInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetPhysicalChanAttributeUInt32Array(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetReadAttributeBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetReadAttributeDouble(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetReadAttributeInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetReadAttributeString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetReadAttributeUInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetReadAttributeUInt64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetRealTimeAttributeBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetRealTimeAttributeInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetRealTimeAttributeUInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetRefTrigTimestampVal(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetScaleAttributeDouble(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetScaleAttributeDoubleArray(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetScaleAttributeInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetScaleAttributeString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetSelfCalLastDateAndTime(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetStartTrigTimestampVal(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetStartTrigTrigWhen(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetSyncPulseTimeWhen(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetSystemInfoAttributeString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetSystemInfoAttributeUInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTaskAttributeBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTaskAttributeString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTaskAttributeUInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTimingAttributeBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTimingAttributeDouble(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTimingAttributeExBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTimingAttributeExDouble(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTimingAttributeExInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTimingAttributeExString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTimingAttributeExTimestamp(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTimingAttributeExUInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTimingAttributeExUInt64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTimingAttributeInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTimingAttributeString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTimingAttributeTimestamp(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTimingAttributeUInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTimingAttributeUInt64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTrigAttributeBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTrigAttributeDouble(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTrigAttributeDoubleArray(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTrigAttributeInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTrigAttributeInt32Array(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTrigAttributeString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTrigAttributeTimestamp(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTrigAttributeUInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetWatchdogAttributeBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetWatchdogAttributeDouble(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetWatchdogAttributeInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetWatchdogAttributeString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetWriteAttributeBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetWriteAttributeDouble(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetWriteAttributeInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetWriteAttributeString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetWriteAttributeUInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetWriteAttributeUInt64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def IsTaskDone(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def LoadTask(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PerformBridgeOffsetNullingCalEx(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PerformBridgeShuntCalEx(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PerformStrainShuntCalEx(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PerformThrmcplLeadOffsetNullingCal(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadAnalogF64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadAnalogF64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadAnalogScalarF64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadAnalogScalarF64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadBinaryI16(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadBinaryI16(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadBinaryI32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadBinaryI32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadBinaryU16(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadBinaryU16(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadBinaryU32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadBinaryU32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadCounterF64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadCounterF64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadCounterF64Ex(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadCounterF64Ex(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadCounterScalarF64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadCounterScalarF64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadCounterScalarU32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadCounterScalarU32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadCounterU32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadCounterU32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadCounterU32Ex(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadCounterU32Ex(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadCtrFreq(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadCtrFreq(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadCtrFreqScalar(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadCtrFreqScalar(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadCtrTicks(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadCtrTicks(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadCtrTicksScalar(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadCtrTicksScalar(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadCtrTime(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadCtrTime(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadCtrTimeScalar(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadCtrTimeScalar(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadDigitalLines(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadDigitalLines(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadDigitalScalarU32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadDigitalScalarU32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadDigitalU16(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadDigitalU16(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadDigitalU32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadDigitalU32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadDigitalU8(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadDigitalU8(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadIDPinMemory(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadPowerBinaryI16(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadPowerBinaryI16(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadPowerF64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadPowerF64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadPowerScalarF64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadPowerScalarF64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadRaw(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginReadRaw(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def RegisterDoneEvent(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def RegisterEveryNSamplesEvent(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def RegisterSignalEvent(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def RemoveCDAQSyncConnection(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReserveNetworkDevice(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetBufferAttribute(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetChanAttribute(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetDevice(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetExportedSignalAttribute(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetReadAttribute(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetRealTimeAttribute(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetTimingAttribute(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetTimingAttributeEx(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetTrigAttribute(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetWatchdogAttribute(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetWriteAttribute(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def RestoreLastExtCalConst(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SaveGlobalChan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SaveScale(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SaveTask(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SelfCal(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SelfTestDevice(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAIChanCalCalDate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAIChanCalExpDate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAnalogPowerUpStates(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAnalogPowerUpStatesWithOutputType(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetArmStartTrigTrigWhen(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetBufferAttributeUInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetCalInfoAttributeBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetCalInfoAttributeDouble(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetCalInfoAttributeString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetCalInfoAttributeUInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetChanAttributeBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetChanAttributeDouble(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetChanAttributeDoubleArray(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetChanAttributeInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetChanAttributeString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetChanAttributeUInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetDigitalLogicFamilyPowerUpState(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetDigitalPowerUpStates(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetDigitalPullUpPullDownStates(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetExportedSignalAttributeBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetExportedSignalAttributeDouble(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetExportedSignalAttributeInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetExportedSignalAttributeString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetExportedSignalAttributeUInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetFirstSampClkWhen(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetReadAttributeBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetReadAttributeDouble(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetReadAttributeInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetReadAttributeString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetReadAttributeUInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetReadAttributeUInt64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetRealTimeAttributeBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetRealTimeAttributeInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetRealTimeAttributeUInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetScaleAttributeDouble(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetScaleAttributeDoubleArray(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetScaleAttributeInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetScaleAttributeString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetStartTrigTrigWhen(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetSyncPulseTimeWhen(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetTimingAttributeBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetTimingAttributeDouble(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetTimingAttributeExBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetTimingAttributeExDouble(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetTimingAttributeExInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetTimingAttributeExString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetTimingAttributeExTimestamp(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetTimingAttributeExUInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetTimingAttributeExUInt64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetTimingAttributeInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetTimingAttributeString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetTimingAttributeTimestamp(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetTimingAttributeUInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetTimingAttributeUInt64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetTrigAttributeBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetTrigAttributeDouble(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetTrigAttributeDoubleArray(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetTrigAttributeInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetTrigAttributeInt32Array(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetTrigAttributeString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetTrigAttributeTimestamp(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetTrigAttributeUInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetWatchdogAttributeBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetWatchdogAttributeDouble(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetWatchdogAttributeInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetWatchdogAttributeString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetWriteAttributeBool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetWriteAttributeDouble(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetWriteAttributeInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetWriteAttributeString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetWriteAttributeUInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetWriteAttributeUInt64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def StartNewFile(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def StartTask(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def StopTask(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def TaskControl(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def TristateOutputTerm(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def UnregisterDoneEvent(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def UnregisterEveryNSamplesEvent(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def UnregisterSignalEvent(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def UnreserveNetworkDevice(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WaitForNextSampleClock(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginWaitForNextSampleClock(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WaitForValidTimestamp(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WaitUntilTaskDone(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteAnalogF64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginWriteAnalogF64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteAnalogScalarF64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginWriteAnalogScalarF64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteBinaryI16(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginWriteBinaryI16(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteBinaryI32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginWriteBinaryI32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteBinaryU16(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginWriteBinaryU16(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteBinaryU32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginWriteBinaryU32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteCtrFreq(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginWriteCtrFreq(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteCtrFreqScalar(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginWriteCtrFreqScalar(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteCtrTicks(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginWriteCtrTicks(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteCtrTicksScalar(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginWriteCtrTicksScalar(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteCtrTime(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginWriteCtrTime(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteCtrTimeScalar(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginWriteCtrTimeScalar(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteDigitalLines(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginWriteDigitalLines(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteDigitalScalarU32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginWriteDigitalScalarU32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteDigitalU16(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginWriteDigitalU16(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteDigitalU32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginWriteDigitalU32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteDigitalU8(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginWriteDigitalU8(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteIDPinMemory(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteRaw(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BeginWriteRaw(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteToTEDSFromArray(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteToTEDSFromFile(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadAnalogWaveforms(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadDigitalWaveforms(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteAnalogWaveforms(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteDigitalWaveforms(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/_time.py -->
## PYTHON MODULE: generated/nidaqmx/_time.py

### `def _convert_to_desired_timezone(expected_time_utc: ht_datetime, tzinfo: dt_tzinfo | None=None) -> ht_datetime`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/_waveform_utils.py -->
## PYTHON MODULE: generated/nidaqmx/_waveform_utils.py

### `def get_num_samps_per_chan(waveforms: Sequence[AnalogWaveform[Any] | DigitalWaveform[Any]]) -> int`

Validate that all waveforms have the same sample count and return it.

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/constants.py -->
## PYTHON MODULE: generated/nidaqmx/constants.py

- `AUTO = -1`

- `CFG_DEFAULT = -1`

- `DEFAULT = -1`

- `READ_ALL_AVAILABLE = -1`

- `WAIT_INFINITELY = -1.0`

### `class ACExcitWireMode(Enum)`

### `class ADCTimingMode(Enum)`

### `class AOIdleOutputBehavior(Enum)`

### `class AOPowerUpOutputBehavior(Enum)`

### `class AccelChargeSensitivityUnits(Enum)`

### `class AccelSensitivityUnits(Enum)`

### `class AccelUnits(Enum)`

### `class AcquisitionType(Enum)`

### `class ActiveLevel(Enum)`

### `class ActiveOrInactiveEdgeSelection(Enum)`

### `class AngleUnits(Enum)`

### `class AngularVelocityUnits(Enum)`

### `class AutoZeroType(Enum)`

### `class BridgeConfiguration(Enum)`

### `class BridgeElectricalUnits(Enum)`

### `class BridgePhysicalUnits(Enum)`

### `class BridgeShuntCalSource(Enum)`

### `class BridgeUnits(Enum)`

### `class BusType(Enum)`

### `class CJCSource(Enum)`

### `class ChannelType(Enum)`

### `class ChargeUnits(Enum)`

### `class ConstrainedGenMode(Enum)`

### `class CountDirection(Enum)`

### `class CounterFrequencyMethod(Enum)`

### `class Coupling(Enum)`

### `class CurrentShuntResistorLocation(Enum)`

### `class CurrentUnits(Enum)`

### `class DataJustification(Enum)`

### `class DataTransferActiveTransferMode(Enum)`

### `class DeassertCondition(Enum)`

### `class DigitalDriveType(Enum)`

### `class DigitalPatternCondition(Enum)`

### `class DigitalWidthUnits(Enum)`

### `class EddyCurrentProxProbeSensitivityUnits(Enum)`

### `class Edge(Enum)`

### `class EncoderType(Enum)`

### `class EncoderZIndexPhase(Enum)`

### `class EveryNSamplesEventType(Enum)`

### `class ExcitationDCorAC(Enum)`

### `class ExcitationIdleOutputBehavior(Enum)`

### `class ExcitationSource(Enum)`

### `class ExcitationVoltageOrCurrent(Enum)`

### `class ExportAction(Enum)`

### `class FillMode(Enum)`

### `class FilterResponse(Enum)`

### `class FilterType(Enum)`

### `class ForceIEPESensorSensitivityUnits(Enum)`

### `class ForceUnits(Enum)`

### `class FrequencyUnits(Enum)`

### `class FuncGenType(Enum)`

### `class GpsSignalType(Enum)`

### `class HandshakeStartCondition(Enum)`

### `class IDPinStatus(Enum)`

### `class Impedance1(Enum)`

### `class InputDataTransferCondition(Enum)`

### `class InvertPolarity(Enum)`

### `class LVDTSensitivityUnits(Enum)`

### `class LengthUnits(Enum)`

### `class Level(Enum)`

### `class LineGrouping(Enum)`

### `class LoggingMode(Enum)`

### `class LoggingOperation(Enum)`

### `class LogicFamily(Enum)`

### `class LogicLvlBehavior(Enum)`

### `class MIOAIConvertTimebaseSource(Enum)`

### `class ModulationType(Enum)`

### `class OutputDataTransferCondition(Enum)`

### `class OverflowBehavior(Enum)`

### `class OverwriteMode(Enum)`

### `class Polarity(Enum)`

### `class PowerIdleOutputBehavior(Enum)`

### `class PowerOutputState(Enum)`

### `class PowerUnits(Enum)`

### `class PowerUpChannelType(Enum)`

### `class PowerUpStates(Enum)`

### `class PressureUnits(Enum)`

### `class ProductCategory(Enum)`

### `class RTDType(Enum)`

### `class RVDTSensitivityUnits(Enum)`

### `class RawDataCompressionType(Enum)`

### `class ReadRelativeTo(Enum)`

### `class RegenerationMode(Enum)`

### `class ResistanceConfiguration(Enum)`

### `class ResistanceUnits(Enum)`

### `class ResistorState(Enum)`

### `class ResolutionType(Enum)`

### `class SampClkOverrunBehavior(Enum)`

### `class SampleInputDataWhen(Enum)`

### `class SampleTimingType(Enum)`

### `class ScaleType(Enum)`

### `class Sense(Enum)`

### `class SensorPowerCfg(Enum)`

### `class SensorPowerType(Enum)`

### `class ShuntCalSelect(Enum)`

### `class ShuntCalSource(Enum)`

### `class ShuntElementLocation(Enum)`

### `class Signal(Enum)`

### `class SignalModifiers(Enum)`

### `class Slope(Enum)`

### `class SoundPressureUnits(Enum)`

### `class SourceSelection(Enum)`

### `class StrainGageBridgeType(Enum)`

### `class StrainGageRosetteMeasurementType(Enum)`

### `class StrainGageRosetteType(Enum)`

### `class StrainUnits(Enum)`

### `class SyncPulseType(Enum)`

### `class SyncType(Enum)`

### `class SyncUnlockBehavior(Enum)`

### `class TEDSUnits(Enum)`

### `class TaskMode(Enum)`

### `class TemperatureUnits(Enum)`

### `class TerminalConfiguration(Enum)`

### `class ThermocoupleType(Enum)`

### `class TimeUnits(Enum)`

### `class Timescale(Enum)`

### `class TimestampEvent(Enum)`

### `class TorqueUnits(Enum)`

### `class TriggerType(Enum)`

### `class TriggerUsage(Enum)`

### `class UnderflowBehavior(Enum)`

### `class UnitsPreScaled(Enum)`

### `class UsageTypeAI(Enum)`

### `class UsageTypeAO(Enum)`

### `class UsageTypeCI(Enum)`

### `class UsageTypeCO(Enum)`

### `class VelocityIEPESensorSensitivityUnits(Enum)`

### `class VelocityUnits(Enum)`

### `class VoltageUnits(Enum)`

### `class WDTTaskAction(Enum)`

### `class WaitMode(Enum)`

### `class WatchdogAOExpirState(Enum)`

### `class WatchdogCOExpirState(Enum)`

### `class WindowTriggerCondition1(Enum)`

### `class WindowTriggerCondition2(Enum)`

### `class WriteBasicTEDSOptions(Enum)`

### `class WriteRelativeTo(Enum)`

### `class _CouplingTypes(Enum)`

### `class _Save(Enum)`

### `class _TermCfg(Enum)`

### `class _TriggerUsageTypes(Enum)`

### `class ReallocationPolicy(Enum)`

### `class WaveformAttributeMode(Flag)`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/error_codes.py -->
## PYTHON MODULE: generated/nidaqmx/error_codes.py

- `__all__ = ['DAQmxErrors', 'DAQmxWarnings']`

### `class DAQmxErrors(IntEnum)`

### `class DAQmxWarnings(IntEnum)`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/errors.py -->
## PYTHON MODULE: generated/nidaqmx/errors.py

### MODULE DOCSTRING

NI-DAQmx error classes.

- `__all__ = ['DaqError', 'DaqReadError', 'DaqWriteError', 'DaqWarning', 'DaqResourceWarning']`

### `class Error(Exception)`

Base error class for module.

### `class DaqNotFoundError(Error)`

Error raised when NI-DAQmx driver is not installed.

### `class DaqNotSupportedError(Error)`

Error raised when DAQmx is not supported on this platform.

### `class DaqFunctionNotSupportedError(Error)`

Error raised when a specific function isn't supported by the installed NI-DAQmx driver.

### `class DaqError(Error)`

Error raised by any DAQmx method.

#### `def __init__(self, message, error_code, task_name='')`

Initialize a new DaqError.

        Args:
            message (string): Specifies the error message.
            error_code (int): Specifies the NI-DAQmx error code.
        

#### `def error_code(self)`

int: Specifies the NI-DAQmx error code.

#### `def error_type(self)`

:class:`nidaqmx.error_codes.DAQmxErrors`: Specifies the NI-DAQmx error type.

### `class DaqReadError(DaqError)`

Error raised by DAQmx write method that includes the amount of data that was read.

#### `def __init__(self, message, error_code, samps_per_chan_read, task_name='')`

Initialize a new DaqReadError.

        Args:
            message (string): Specifies the error message.
            error_code (int): Specifies the NI-DAQmx error code.
        

#### `def samps_per_chan_read(self)`

int: Indicates the number of samples successfully read.

### `class DaqWriteError(DaqError)`

Error raised by DAQmx write method that includes the amount of data that was written.

#### `def __init__(self, message, error_code, samps_per_chan_written, task_name='')`

Initialize a new DaqWriteError.

        Args:
            message (string): Specifies the error message.
            error_code (int): Specifies the NI-DAQmx error code.
            samps_per_chan_written (int): Specifies the number of samples written.
        

#### `def samps_per_chan_written(self)`

int: Indicates the number of samples successfully written.

### `class DaqWarning(Warning)`

Warning raised by any NI-DAQmx method.

#### `def __init__(self, message, error_code)`

Initialize a new DaqWarning.

        Args:
            message (string): Specifies the warning message.
            error_code (int): Specifies the NI-DAQmx error code.
        

#### `def error_code(self)`

int: Specifies the NI-DAQmx error code.

#### `def error_type(self)`

:class:`nidaqmx.error_codes.DAQmxWarnings`: Specifies the NI-DAQmx error type.

### `class DaqResourceWarning(ResourceWarning)`

Warning about DAQ resource usage, such as a leaking an NI-DAQmx task.

### `def check_for_error(error_code, samps_per_chan_written=None, samps_per_chan_read=None)`

### `def is_string_buffer_too_small(error_code)`

### `def is_array_buffer_too_small(error_code)`

### `class RpcError(Error)`

An error specific to sessions to the NI gRPC Device Server.

#### `def __init__(self, rpc_code, description)`

Initialize a new RpcError.

### `class FeatureNotSupportedError(Exception)`

The feature is not supported at the current code readiness level.

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/grpc_session_options.py -->
## PYTHON MODULE: generated/nidaqmx/grpc_session_options.py

### MODULE DOCSTRING

NI-DAQmx gRPC session options.

- `GRPC_SERVICE_INTERFACE_NAME = 'nidaqmx_grpc.NiDAQmx'`

- `MEASUREMENTLINK_23Q1_NIDAQMX_PYTHON_API_KEY = '147D9BA7-BE75-4B29-8591-BA4A737AA8CF'`

### `class SessionInitializationBehavior(IntEnum)`

Specifies how to initialize sessions on the server.

### `class GrpcSessionOptions()`

Collection of options that specifies session behaviors related to gRPC.

#### `def __init__(self, grpc_channel: grpc.Channel, session_name: str, *, api_key=MEASUREMENTLINK_23Q1_NIDAQMX_PYTHON_API_KEY, initialization_behavior=SessionInitializationBehavior.AUTO)`

Initialize a new GrpcSessionOptions.

        Args:
            grpc_channel (grpc.Channel): Specifies the channel to the NI gRPC Device Server.
            session_name (str): User-specified name that identifies the driver session on the NI gRPC Device
                Server. This is different from the resource name parameter many APIs take as a separate
                parameter. Specifying a name makes it easy to share sessions across multiple gRPC clients.
                You can use an empty string if you want to always initialize a new session on the server.
                To attach to an existing session, you must specify the session name it was initialized with.
            api_key (str): Specifies the API license key required by the NI gRPC Device Server.
            initialization_behavior (enum): Specifies whether it is acceptable to initialize a new
                session or attach to an existing one, or if only one of the behaviors is desired.
                The driver session exists on the NI gRPC Device Server.
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/scale.py -->
## PYTHON MODULE: generated/nidaqmx/scale.py

- `__all__ = ['Scale']`

### `class Scale()`


    Represents a DAQmx scale.
    

#### `def __init__(self, name, *, grpc_options=None)`


        Args:
            name (str): Specifies the name of the scale to create.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        

#### `def __eq__(self, other)`

#### `def __hash__(self)`

#### `def __ne__(self, other)`

#### `def __repr__(self)`

#### `def name(self)`


        str: Specifies the name of this scale.
        

#### `def description(self)`


        str: Specifies a description for the scale.
        

#### `def description(self, val)`

#### `def lin_slope(self)`


        float: Specifies the slope, m, in the equation y=mx+b.
        

#### `def lin_slope(self, val)`

#### `def lin_y_intercept(self)`


        float: Specifies the y-intercept, b, in the equation y=mx+b.
        

#### `def lin_y_intercept(self, val)`

#### `def map_pre_scaled_max(self)`


        float: Specifies the largest value in the range of pre-scaled
            values. NI-DAQmx maps this value to **map_scaled_max**.
        

#### `def map_pre_scaled_max(self, val)`

#### `def map_pre_scaled_min(self)`


        float: Specifies the smallest value in the range of pre-scaled
            values. NI-DAQmx maps this value to **map_scaled_min**.
        

#### `def map_pre_scaled_min(self, val)`

#### `def map_scaled_max(self)`


        float: Specifies the largest value in the range of scaled
            values. NI-DAQmx maps this value to **map_pre_scaled_max**.
            Reads coerce samples that are larger than this value to
            match this value. Writes generate errors for samples that
            are larger than this value.
        

#### `def map_scaled_max(self, val)`

#### `def map_scaled_min(self)`


        float: Specifies the smallest value in the range of scaled
            values. NI-DAQmx maps this value to **map_pre_scaled_min**.
            Reads coerce samples that are smaller than this value to
            match this value. Writes generate errors for samples that
            are smaller than this value.
        

#### `def map_scaled_min(self, val)`

#### `def poly_forward_coeff(self)`


        List[float]: Specifies a list of coefficients for the polynomial
            that converts pre-scaled values to scaled values. Each
            element of the list corresponds to a term of the equation.
            For example, if index three of the list is 9, the fourth
            term of the equation is 9x^3.
        

#### `def poly_forward_coeff(self, val)`

#### `def poly_reverse_coeff(self)`


        List[float]: Specifies a list of coefficients for the polynomial
            that converts scaled values to pre-scaled values. Each
            element of the list corresponds to a term of the equation.
            For example, if index three of the list is 9, the fourth
            term of the equation is 9y^3.
        

#### `def poly_reverse_coeff(self, val)`

#### `def pre_scaled_units(self)`


        :class:`nidaqmx.constants.UnitsPreScaled`: Specifies the units
            of the values that you want to scale.
        

#### `def pre_scaled_units(self, val)`

#### `def scale_type(self)`


        :class:`nidaqmx.constants.ScaleType`: Indicates the method or
            equation form that the custom scale uses.
        

#### `def scaled_units(self)`


        str: Specifies the units to use for scaled values. You can use
            an arbitrary string.
        

#### `def scaled_units(self, val)`

#### `def table_pre_scaled_vals(self)`


        List[float]: Specifies a list of pre-scaled values. These values
            map directly to the values in **table_scaled_vals**.
        

#### `def table_pre_scaled_vals(self, val)`

#### `def table_scaled_vals(self)`


        List[float]: Specifies a list of scaled values. These values map
            directly to the values in **table_pre_scaled_vals**.
        

#### `def table_scaled_vals(self, val)`

#### `def calculate_reverse_poly_coeff(forward_coeffs, min_val_x=-5.0, max_val_x=5.0, num_points_to_compute=1000, reverse_poly_order=-1, *, grpc_options=None)`


        Computes a set of coefficients for a polynomial that
        approximates the inverse of the polynomial with the coefficients
        you specify with the "forward_coeffs" input. This function
        generates a table of x versus y values over the range of x. This
        function then finds a polynomial fit, using the least squares
        method to compute a polynomial that computes x when given a
        value for y.

        Args:
            forward_coeffs (List[float]): Is the list of coefficients
                for the polynomial that computes y given a value of x.
                Each element of the list corresponds to a term of the
                equation.
            min_val_x (Optional[float]): Is the minimum value of x for
                which you use the polynomial. This is the smallest value
                of x for which the function generates a y value in the
                table.
            max_val_x (Optional[float]): Is the maximum value of x for
                which you use the polynomial. This is the largest value
                of x for which the function generates a y value in the
                table.
            num_points_to_compute (Optional[int]): Is the number of
                points in the table of x versus y values. The function
                spaces the values evenly between "min_val_x" and
                "max_val_x".
            reverse_poly_order (Optional[int]): Is the order of the
                reverse polynomial to compute. For example, an input of
                3 indicates a 3rd order polynomial. A value of -1
                indicates a reverse polynomial of the same order as the
                forward polynomial.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        Returns:
            List[float]:

            Specifies the list of coefficients for the reverse
            polynomial. Each element of the list corresponds to a term
            of the equation. For example, if index three of the list is
            9, the fourth term of the equation is 9y^3.
        

#### `def create_lin_scale(scale_name, slope, y_intercept=0.0, pre_scaled_units=UnitsPreScaled.VOLTS, scaled_units=None, *, grpc_options=None)`


        Creates a custom scale that uses the equation y=mx+b, where x is
        a pre-scaled value, and y is a scaled value. The equation is
        identical for input and output. If the equation is in the form
        x=my+b, you must first solve for y in terms of x.

        Args:
            scale_name (str): Specifies the name of the scale to create.
            slope (float): Is the slope, m, in the equation.
            y_intercept (Optional[float]): Is the y-intercept, b, in the
                equation.
            pre_scaled_units (Optional[nidaqmx.constants.UnitsPreScaled]):
                Is the units of the values to scale.
            scaled_units (Optional[str]): Is the units to use for the
                scaled value. You can use an arbitrary string. NI-DAQmx
                uses the units to label a graph or chart.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        Returns:
            nidaqmx.scale.Scale:

            Indicates an object that represents the created custom scale.
        

#### `def create_map_scale(scale_name, prescaled_min, prescaled_max, scaled_min, scaled_max, pre_scaled_units=UnitsPreScaled.VOLTS, scaled_units=None, *, grpc_options=None)`


        Creates a custom scale that scales values proportionally from a
        range of pre-scaled values to a range of scaled values.

        Args:
            scale_name (str): Specifies the name of the scale to create.
            prescaled_min (float): Is the smallest value in the range of
                pre-scaled values. NI-DAQmx maps this value to
                "scaled_min".
            prescaled_max (float): Is the largest value in the range of
                pre-scaled values. NI-DAQmx maps this value to
                "scaled_max".
            scaled_min (float): Is the smallest value in the range of
                scaled values. NI-DAQmx maps this value to
                "prescaled_min". Read operations clip samples that are
                smaller than this value. Write operations generate
                errors for samples that are smaller than this value.
            scaled_max (float): Is the largest value in the range of
                scaled values. NI-DAQmx maps this value to
                "prescaled_max". Read operations clip samples that are
                larger than this value. Write operations generate errors
                for samples that are larger than this value.
            pre_scaled_units (Optional[nidaqmx.constants.UnitsPreScaled]):
                Is the units of the values to scale.
            scaled_units (Optional[str]): Is the units to use for the
                scaled value. You can use an arbitrary string. NI-DAQmx
                uses the units to label a graph or chart.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        Returns:
            nidaqmx.scale.Scale:

            Indicates an object that represents the created custom scale.
        

#### `def create_polynomial_scale(scale_name, forward_coeffs, reverse_coeffs, pre_scaled_units=UnitsPreScaled.VOLTS, scaled_units=None, *, grpc_options=None)`


        Creates a custom scale that uses an nth order polynomial
        equation. NI-DAQmx requires both a polynomial to convert pre-
        scaled values to scaled values (forward) and a polynomial to
        convert scaled values to pre-scaled values (reverse). If you
        only know one set of coefficients, use the DAQmx Compute Reverse
        Polynomial Coefficients function to generate the other set.

        Args:
            scale_name (str): Specifies the name of the scale to create.
            forward_coeffs (List[float]): Is an list of coefficients for
                the polynomial that converts pre-scaled values to scaled
                values. Each element of the list corresponds to a term
                of the equation.
            reverse_coeffs (List[float]): Is an list of coefficients for
                the polynomial that converts scaled values to pre-scaled
                values. Each element of the list corresponds to a term
                of the equation.
            pre_scaled_units (Optional[nidaqmx.constants.UnitsPreScaled]):
                Is the units of the values to scale.
            scaled_units (Optional[str]): Is the units to use for the
                scaled value. You can use an arbitrary string. NI-DAQmx
                uses the units to label a graph or chart.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        Returns:
            nidaqmx.scale.Scale:

            Indicates an object that represents the created custom scale.
        

#### `def create_table_scale(scale_name, prescaled_vals, scaled_vals, pre_scaled_units=UnitsPreScaled.VOLTS, scaled_units=None, *, grpc_options=None)`


        Creates a custom scale that maps an list of pre-scaled values to
        an list of corresponding scaled values. NI-DAQmx applies linear
        interpolation to values that fall between the values in the
        table. Read operations clip scaled samples that are outside the
        maximum and minimum scaled values found in the table. Write
        operations generate errors for samples that are outside the
        minimum and maximum scaled values found in the table.

        Args:
            scale_name (str): Specifies the name of the scale to create.
            prescaled_vals (List[float]): Is the list of pre-scaled
                values that map to the values in "scaled_vals".
            scaled_vals (List[float]): Is the list of scaled values that
                map to the values in "prescaled_vals".
            pre_scaled_units (Optional[nidaqmx.constants.UnitsPreScaled]):
                Is the units of the values to scale.
            scaled_units (Optional[str]): Is the units to use for the
                scaled value. You can use an arbitrary string. NI-DAQmx
                uses the units to label a graph or chart.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        Returns:
            nidaqmx.scale.Scale:

            Indicates an object that represents the created custom scale.
        

#### `def save(self, save_as='', author='', overwrite_existing_scale=False, allow_interactive_editing=True, allow_interactive_deletion=True)`


        Saves this custom scale to MAX.

        Args:
            save_as (Optional[str]): Is the name to save the task,
                global channel, or custom scale as. If you do not
                specify a value for this input, NI-DAQmx uses the name
                currently assigned to the task, global channel, or
                custom scale.
            author (Optional[str]): Is a name to store with the task,
                global channel, or custom scale.
            options (Optional[int]): Specifies whether to allow the
                task, global channel, or custom scale to be deleted
                through MAX.
            overwrite_existing_scale (Optional[bool]): Specifies whether to
                overwrite a custom scale of the same name if one is already
                saved in MAX. If this input is False and a custom scale of
                the same name is already saved in MAX, this function returns
                an error.
            allow_interactive_editing (Optional[bool]): Specifies whether to
                allow the task, global channel, or custom scale to be edited
                in the DAQ Assistant. If allow_interactive_editing is True,
                the DAQ Assistant must support all task or global channel
                settings.
            allow_interactive_deletion (Optional[bool]): Specifies whether
                to allow the task, global channel, or custom scale to be
                deleted through MAX.
        

### `class _ScaleAlternateConstructor(Scale)`


    Provide an alternate constructor for the Scale object.

    This is a private API used to instantiate a Scale with an existing interpreter.
    

#### `def __init__(self, name, interpreter)`


        Args:
            name: Specifies the name of the Scale.
            interpreter: Specifies the interpreter instance.

        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/stream_readers/__init__.py -->
## PYTHON MODULE: generated/nidaqmx/stream_readers/__init__.py

### MODULE DOCSTRING

NI-DAQmx stream readers.

This package provides classes for reading samples from NI-DAQmx tasks.


- `__all__ = ['AnalogSingleChannelReader', 'AnalogMultiChannelReader', 'AnalogUnscaledReader', 'CounterReader', 'DigitalSingleChannelReader', 'DigitalMultiChannelReader', 'PowerSingleChannelReader', 'PowerMultiChannelReader', 'PowerBinaryReader']`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/stream_readers/_analog_multi_channel_reader.py -->
## PYTHON MODULE: generated/nidaqmx/stream_readers/_analog_multi_channel_reader.py

### `class AnalogMultiChannelReader(ChannelReaderBase)`

Reads samples from one or more analog input channels in an NI-DAQmx task.

#### `def read_many_sample(self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0)`

Reads one or more floating-point samples from one or more analog input channels in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 2D NumPy
                array of floating-point values to hold the samples
                requested. The size of the array must be large enough to
                hold all requested samples from all channels in the
                task; otherwise, an error is thrown.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample from each channel. The
                order of the channels in the array corresponds to the
                order in which you add the channels to the task or to
                the order of the channels you specify with the
                "channels_to_read" property.

                If the size of the array is too large or the array is
                shaped incorrectly, the previous statement may not hold
                true as the samples read may not be separated into rows
                and columns properly. Set the "verify_array_shape"
                property on this channel reader object to True to
                validate that the NumPy array object is shaped properly.
                Setting this property to True may marginally adversely
                impact the performance of the method.
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read.

                If you set this input to nidaqmx.constants.
                READ_ALL_AVAILABLE, NI-DAQmx determines how many samples
                to read based on if the task acquires samples
                continuously or acquires a finite number of samples.

                If the task acquires samples continuously and you set
                this input to nidaqmx.constants.READ_ALL_AVAILABLE, this
                method reads all the samples currently available in the
                buffer.

                If the task acquires a finite number of samples and you
                set this input to nidaqmx.constants.READ_ALL_AVAILABLE,
                the method waits for the task to acquire all requested
                samples, then reads those samples. If you set the
                "read_all_avail_samp" property to True, the method reads
                the samples currently available in the buffer and does
                not wait for the task to acquire all requested samples.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            int:

            Indicates the number of samples acquired by each channel.
            NI-DAQmx returns a single value because this value is the
            same for all channels.
        

#### `def read_one_sample(self, data, timeout=10)`

Reads a single floating-point sample from one or more analog input channels in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of floating-point values to hold the samples
                requested.

                Each element in the array corresponds to a sample from
                each channel. The size of the array must be large enough
                to hold all requested samples from the channel in the
                task; otherwise, an error is thrown.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.
        

#### `def read_waveforms(self, waveforms: list[AnalogWaveform[numpy.float64]], number_of_samples_per_channel: int=READ_ALL_AVAILABLE, reallocation_policy: ReallocationPolicy=ReallocationPolicy.TO_GROW, timeout: float=10.0) -> int`

Reads one or more floating-point samples from one or more analog input channels into a list of waveforms.

        This read method optionally accepts a preallocated list of waveforms to hold
        the samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated list of waveforms is valuable in continuous
        acquisition scenarios, where the same waveforms can be used
        repeatedly in each call to the method.

        Args:
            waveforms (list[AnalogWaveform]): Specifies a list of AnalogWaveform
                objects to use for reading samples into.
                The list must contain one waveform for each channel in the task.
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read.

                If you set this input to nidaqmx.constants.
                READ_ALL_AVAILABLE, NI-DAQmx determines how many samples
                to read based on if the task acquires samples
                continuously or acquires a finite number of samples.

                If the task acquires samples continuously and you set
                this input to nidaqmx.constants.READ_ALL_AVAILABLE, this
                method reads all the samples currently available in the
                buffer.

                If the task acquires a finite number of samples and you
                set this input to nidaqmx.constants.READ_ALL_AVAILABLE,
                the method waits for the task to acquire all requested
                samples, then reads those samples. If you set the
                "read_all_avail_samp" property to True, the method reads
                the samples currently available in the buffer and does
                not wait for the task to acquire all requested samples.
            reallocation_policy (Optional[ReallocationPolicy]): Specifies
                the reallocation policy to use when the read yields more
                samples than the current capacity of the waveform.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            int:

            Indicates the number of samples acquired by each channel.
            NI-DAQmx returns a single value because this value is the
            same for all channels.
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/stream_readers/_analog_single_channel_reader.py -->
## PYTHON MODULE: generated/nidaqmx/stream_readers/_analog_single_channel_reader.py

### `class AnalogSingleChannelReader(ChannelReaderBase)`

Reads samples from an analog input channel in an NI-DAQmx task.

#### `def read_many_sample(self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0)`

Reads one or more floating-point samples from a single analog input channel in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of floating-point values to hold the samples
                requested.

                Each element in the array corresponds to a sample from
                the channel. The size of the array must be large enough
                to hold all requested samples from the channel in the
                task; otherwise, an error is thrown.
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read.

                If you set this input to nidaqmx.constants.
                READ_ALL_AVAILABLE, NI-DAQmx determines how many samples
                to read based on if the task acquires samples
                continuously or acquires a finite number of samples.

                If the task acquires samples continuously and you set
                this input to nidaqmx.constants.READ_ALL_AVAILABLE, this
                method reads all the samples currently available in the
                buffer.

                If the task acquires a finite number of samples and you
                set this input to nidaqmx.constants.READ_ALL_AVAILABLE,
                the method waits for the task to acquire all requested
                samples, then reads those samples. If you set the
                "read_all_avail_samp" property to True, the method reads
                the samples currently available in the buffer and does
                not wait for the task to acquire all requested samples.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            int:

            Indicates the number of samples acquired by each channel.
            NI-DAQmx returns a single value because this value is the
            same for all channels.
        

#### `def read_one_sample(self, timeout=10)`

Reads a single floating-point sample from a single analog input channel in a task.

        Args:
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            float:

            Indicates a single floating-point sample from the task.
        

#### `def read_waveform(self, waveform: AnalogWaveform[numpy.float64], number_of_samples_per_channel: int=READ_ALL_AVAILABLE, reallocation_policy: ReallocationPolicy=ReallocationPolicy.TO_GROW, timeout: float=10.0) -> int`

Reads one or more floating-point samples from a single analog input channel into a waveform.

        This read method optionally accepts a preallocated waveform to hold
        the samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated waveform is valuable in continuous
        acquisition scenarios, where the same waveform can be used
        repeatedly in each call to the method.

        Args:
            waveform (AnalogWaveform): Specifies an AnalogWaveform object
                to use for reading samples into.
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read.

                If you set this input to nidaqmx.constants.
                READ_ALL_AVAILABLE, NI-DAQmx determines how many samples
                to read based on if the task acquires samples
                continuously or acquires a finite number of samples.

                If the task acquires samples continuously and you set
                this input to nidaqmx.constants.READ_ALL_AVAILABLE, this
                method reads all the samples currently available in the
                buffer.

                If the task acquires a finite number of samples and you
                set this input to nidaqmx.constants.READ_ALL_AVAILABLE,
                the method waits for the task to acquire all requested
                samples, then reads those samples. If you set the
                "read_all_avail_samp" property to True, the method reads
                the samples currently available in the buffer and does
                not wait for the task to acquire all requested samples.
            reallocation_policy (Optional[ReallocationPolicy]): Specifies
                the reallocation policy to use when the read yields more
                samples than the current capacity of the waveform.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            int:

            Indicates the number of samples acquired.
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/stream_readers/_analog_unscaled_reader.py -->
## PYTHON MODULE: generated/nidaqmx/stream_readers/_analog_unscaled_reader.py

### `class AnalogUnscaledReader(ChannelReaderBase)`

Reads unscaled samples from one or more analog input channels in an NI-DAQmx task.

#### `def read_int16(self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0)`

Reads one or more unscaled 16-bit integer samples from one or more analog input channels in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 2D NumPy
                array of unscaled 16-bit integer values to hold the
                samples requested. The size of the array must be large
                enough to hold all requested samples from all channels
                in the task; otherwise, an error is thrown.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample from each channel. The
                order of the channels in the array corresponds to the
                order in which you add the channels to the task or to
                the order of the channels you specify with the
                "channels_to_read" property.

                If the size of the array is too large or the array is
                shaped incorrectly, the previous statement may not hold
                true as the samples read may not be separated into rows
                and columns properly. Set the "verify_array_shape"
                property on this channel reader object to True to
                validate that the NumPy array object is shaped properly.
                Setting this property may marginally adversely impact
                the performance of the method.
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read.

                If you set this input to nidaqmx.constants.
                READ_ALL_AVAILABLE, NI-DAQmx determines how many samples
                to read based on if the task acquires samples
                continuously or acquires a finite number of samples.

                If the task acquires samples continuously and you set
                this input to nidaqmx.constants.READ_ALL_AVAILABLE, this
                method reads all the samples currently available in the
                buffer.

                If the task acquires a finite number of samples and you
                set this input to nidaqmx.constants.READ_ALL_AVAILABLE,
                the method waits for the task to acquire all requested
                samples, then reads those samples. If you set the
                "read_all_avail_samp" property to True, the method reads
                the samples currently available in the buffer and does
                not wait for the task to acquire all requested samples.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            int:

            Indicates the number of samples acquired by each channel.
            NI-DAQmx returns a single value because this value is the
            same for all channels.
        

#### `def read_int32(self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0)`

Reads one or more unscaled 32-bit integer samples from one or more analog input channels in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 2D NumPy
                array of unscaled 32-bit integer values to hold the
                samples requested. The size of the array must be large
                enough to hold all requested samples from all channels
                in the task; otherwise, an error is thrown.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample from each channel. The
                order of the channels in the array corresponds to the
                order in which you add the channels to the task or to
                the order of the channels you specify with the
                "channels_to_read" property.

                If the size of the array is too large or the array is
                shaped incorrectly, the previous statement may not hold
                true as the samples read may not be separated into rows
                and columns properly. Set the "verify_array_shape"
                property on this channel reader object to True to
                validate that the NumPy array object is shaped properly.
                Setting this property may marginally adversely impact
                the performance of the method.
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read.

                If you set this input to nidaqmx.constants.
                READ_ALL_AVAILABLE, NI-DAQmx determines how many samples
                to read based on if the task acquires samples
                continuously or acquires a finite number of samples.

                If the task acquires samples continuously and you set
                this input to nidaqmx.constants.READ_ALL_AVAILABLE, this
                method reads all the samples currently available in the
                buffer.

                If the task acquires a finite number of samples and you
                set this input to nidaqmx.constants.READ_ALL_AVAILABLE,
                the method waits for the task to acquire all requested
                samples, then reads those samples. If you set the
                "read_all_avail_samp" property to True, the method reads
                the samples currently available in the buffer and does
                not wait for the task to acquire all requested samples.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            int:

            Indicates the number of samples acquired by each channel.
            NI-DAQmx returns a single value because this value is the
            same for all channels.
        

#### `def read_uint16(self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0)`

Reads one or more unscaled 16-bit unsigned integer samples from one or more analog input channels in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 2D NumPy
                array of unscaled 16-bit unsigned integer values to
                hold the samples requested. The size of the array must
                be large enough to hold all requested samples from all
                channels in the task; otherwise, an error is thrown.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample from each channel. The
                order of the channels in the array corresponds to the
                order in which you add the channels to the task or to
                the order of the channels you specify with the
                "channels_to_read" property.

                If the size of the array is too large or the array is
                shaped incorrectly, the previous statement may not hold
                true as the samples read may not be separated into rows
                and columns properly. Set the "verify_array_shape"
                property on this channel reader object to True to
                validate that the NumPy array object is shaped properly.
                Setting this property may marginally adversely impact
                the performance of the method.
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read.

                If you set this input to nidaqmx.constants.
                READ_ALL_AVAILABLE, NI-DAQmx determines how many samples
                to read based on if the task acquires samples
                continuously or acquires a finite number of samples.

                If the task acquires samples continuously and you set
                this input to nidaqmx.constants.READ_ALL_AVAILABLE, this
                method reads all the samples currently available in the
                buffer.

                If the task acquires a finite number of samples and you
                set this input to nidaqmx.constants.READ_ALL_AVAILABLE,
                the method waits for the task to acquire all requested
                samples, then reads those samples. If you set the
                "read_all_avail_samp" property to True, the method reads
                the samples currently available in the buffer and does
                not wait for the task to acquire all requested samples.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            int:

            Indicates the number of samples acquired by each channel.
            NI-DAQmx returns a single value because this value is the
            same for all channels.
        

#### `def read_uint32(self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0)`

Reads one or more unscaled unsigned 32-bit integer samples from one or more analog input channels in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 2D NumPy
                array of unscaled 32-bit unsigned integer values to
                hold the samples requested. The size of the array must
                be large enough to hold all requested samples from all
                channels in the task; otherwise, an error is thrown.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample from each channel. The
                order of the channels in the array corresponds to the
                order in which you add the channels to the task or to
                the order of the channels you specify with the
                "channels_to_read" property.

                If the size of the array is too large or the array is
                shaped incorrectly, the previous statement may not hold
                true as the samples read may not be separated into rows
                and columns properly. Set the "verify_array_shape"
                property on this channel reader object to True to
                validate that the NumPy array object is shaped properly.
                Setting this property may marginally adversely impact
                the performance of the method.
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read.

                If you set this input to nidaqmx.constants.
                READ_ALL_AVAILABLE, NI-DAQmx determines how many samples
                to read based on if the task acquires samples
                continuously or acquires a finite number of samples.

                If the task acquires samples continuously and you set
                this input to nidaqmx.constants.READ_ALL_AVAILABLE, this
                method reads all the samples currently available in the
                buffer.

                If the task acquires a finite number of samples and you
                set this input to nidaqmx.constants.READ_ALL_AVAILABLE,
                the method waits for the task to acquire all requested
                samples, then reads those samples. If you set the
                "read_all_avail_samp" property to True, the method reads
                the samples currently available in the buffer and does
                not wait for the task to acquire all requested samples.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            int:

            Indicates the number of samples acquired by each channel.
            NI-DAQmx returns a single value because this value is the
            same for all channels.
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/stream_readers/_channel_reader_base.py -->
## PYTHON MODULE: generated/nidaqmx/stream_readers/_channel_reader_base.py

### `class ChannelReaderBase()`

Defines base class for all NI-DAQmx stream readers.

#### `def __init__(self, task_in_stream)`

Initialize a new ChannelReaderBase.

        Args:
            task_in_stream: Specifies the input stream associated with
                an NI-DAQmx task from which to read samples.
        

#### `def verify_array_shape(self)`

bool: Specifies whether to verify the shape of NumPy arrays.

        Defaults to True when this object is instantiated.

        Setting this property to True may marginally adversely
        impact the performance of read methods.
        

#### `def verify_array_shape(self, val)`

#### `def _verify_array(self, data, number_of_samples_per_channel, is_many_chan, is_many_samp)`

Verify the shape of a NumPy array.

        Verifies that the shape of the specified NumPy array can be used
        to read multiple samples from the current task which contains
        one or more channels, if the "verify_array_shape" property is
        set to True.

        Args:
            data (numpy.ndarray): Specifies the NumPy array to verify.
            number_of_samples_per_channel (int): Specifies the number of
                samples per channel requested.
            is_many_chan (bool): Specifies if the read method is a many
                channel version.
            is_many_samp (bool): Specifies if the read method is a many
                samples version.
        

#### `def _verify_array_digital_lines(self, data, is_many_chan, is_many_line)`

Verify the shape of a NumPy array of digital lines.

        Verifies that the shape of the specified NumPy array can be used
        to read samples from the current task which contains one or more
        channels that have one or more digital lines per channel, if the
        "verify_array_shape" property is set to True.

        Args:
            data (numpy.ndarray): Specifies the NumPy array to verify.
            is_many_chan (bool): Specifies if the read method is a
                many channel version.
            is_many_line (bool): Specifies if the read method is a
                many line version.
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/stream_readers/_counter_reader.py -->
## PYTHON MODULE: generated/nidaqmx/stream_readers/_counter_reader.py

### `class CounterReader(ChannelReaderBase)`

Reads samples from a counter input channel in an NI-DAQmx task.

#### `def read_many_sample_double(self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0)`

Reads one or more floating-point samples from a single counter input channel in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of floating-point values to hold the samples
                requested.

                Each element in the array corresponds to a sample from
                the channel. The size of the array must be large enough
                to hold all requested samples from the channel in the
                task; otherwise, an error is thrown.
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read.

                If you set this input to nidaqmx.constants.
                READ_ALL_AVAILABLE, NI-DAQmx determines how many samples
                to read based on if the task acquires samples
                continuously or acquires a finite number of samples.

                If the task acquires samples continuously and you set
                this input to nidaqmx.constants.READ_ALL_AVAILABLE, this
                method reads all the samples currently available in the
                buffer.

                If the task acquires a finite number of samples and you
                set this input to nidaqmx.constants.READ_ALL_AVAILABLE,
                the method waits for the task to acquire all requested
                samples, then reads those samples. If you set the
                "read_all_avail_samp" property to True, the method reads
                the samples currently available in the buffer and does
                not wait for the task to acquire all requested samples.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            int:

            Indicates the number of samples acquired by each channel.
            NI-DAQmx returns a single value because this value is the
            same for all channels.
        

#### `def read_many_sample_pulse_frequency(self, frequencies, duty_cycles, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0)`

Reads one or more pulse samples in terms of frequency from a single counter input channel in a task.

        This read method accepts preallocated NumPy arrays to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in preallocated arrays is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            frequencies (numpy.ndarray): Specifies a preallocated 1D
                NumPy array of floating-point values to hold the frequency
                portion of the pulse samples requested.

                Each element in the array corresponds to a sample from
                the channel. The size of the array must be large enough
                to hold all requested samples from the channel in the
                task; otherwise, an error is thrown.
            duty_cycles (numpy.ndarray): Specifies a preallocated 1D
                NumPy array of floating-point values to hold the duty
                cycle portion of the pulse samples requested.

                Each element in the array corresponds to a sample from
                the channel. The size of the array must be large enough
                to hold all requested samples from the channel in the
                task; otherwise, an error is thrown.
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read.

                If you set this input to nidaqmx.constants.
                READ_ALL_AVAILABLE, NI-DAQmx determines how many samples
                to read based on if the task acquires samples
                continuously or acquires a finite number of samples.

                If the task acquires samples continuously and you set
                this input to nidaqmx.constants.READ_ALL_AVAILABLE, this
                method reads all the samples currently available in the
                buffer.

                If the task acquires a finite number of samples and you
                set this input to nidaqmx.constants.READ_ALL_AVAILABLE,
                the method waits for the task to acquire all requested
                samples, then reads those samples. If you set the
                "read_all_avail_samp" property to True, the method reads
                the samples currently available in the buffer and does
                not wait for the task to acquire all requested samples.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            int:

            Indicates the number of samples acquired by each channel.
            NI-DAQmx returns a single value because this value is the
            same for all channels.
        

#### `def read_many_sample_pulse_ticks(self, high_ticks, low_ticks, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0)`

Reads one or more pulse samples in terms of ticks from a single counter input channel in a task.

        This read method accepts preallocated NumPy arrays to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in preallocated arrays is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            high_ticks (numpy.ndarray): Specifies a preallocated 1D
                NumPy array of 32-bit unsigned integer values to hold
                the high ticks portion of the pulse samples requested.

                Each element in the array corresponds to a sample from
                the channel. The size of the array must be large enough
                to hold all requested samples from the channel in the
                task; otherwise, an error is thrown.
            low_ticks (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of 32-bit unsigned integer values to hold the low
                ticks portion of the pulse samples requested.

                Each element in the array corresponds to a sample from
                the channel. The size of the array must be large enough
                to hold all requested samples from the channel in the
                task; otherwise, an error is thrown.
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read.

                If you set this input to nidaqmx.constants.
                READ_ALL_AVAILABLE, NI-DAQmx determines how many samples
                to read based on if the task acquires samples
                continuously or acquires a finite number of samples.

                If the task acquires samples continuously and you set
                this input to nidaqmx.constants.READ_ALL_AVAILABLE, this
                method reads all the samples currently available in the
                buffer.

                If the task acquires a finite number of samples and you
                set this input to nidaqmx.constants.READ_ALL_AVAILABLE,
                the method waits for the task to acquire all requested
                samples, then reads those samples. If you set the
                "read_all_avail_samp" property to True, the method reads
                the samples currently available in the buffer and does
                not wait for the task to acquire all requested samples.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            int:

            Indicates the number of samples acquired by each channel.
            NI-DAQmx returns a single value because this value is the
            same for all channels.
        

#### `def read_many_sample_pulse_time(self, high_times, low_times, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0)`

Reads one or more pulse samples in terms of time from a single counter input channel in a task.

        This read method accepts preallocated NumPy arrays to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in preallocated arrays is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            high_times (numpy.ndarray): Specifies a preallocated 1D
                NumPy array of floating-point values to hold the high
                time portion of the pulse samples requested.

                Each element in the array corresponds to a sample from
                the channel. The size of the array must be large enough
                to hold all requested samples from the channel in the
                task; otherwise, an error is thrown.
            low_times (numpy.ndarray): Specifies a preallocated 1D
                NumPy array of floating-point values to hold the low
                time portion of the pulse samples requested.

                Each element in the array corresponds to a sample from
                the channel. The size of the array must be large enough
                to hold all requested samples from the channel in the
                task; otherwise, an error is thrown.
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read.

                If you set this input to nidaqmx.constants.
                READ_ALL_AVAILABLE, NI-DAQmx determines how many samples
                to read based on if the task acquires samples
                continuously or acquires a finite number of samples.

                If the task acquires samples continuously and you set
                this input to nidaqmx.constants.READ_ALL_AVAILABLE, this
                method reads all the samples currently available in the
                buffer.

                If the task acquires a finite number of samples and you
                set this input to nidaqmx.constants.READ_ALL_AVAILABLE,
                the method waits for the task to acquire all requested
                samples, then reads those samples. If you set the
                "read_all_avail_samp" property to True, the method reads
                the samples currently available in the buffer and does
                not wait for the task to acquire all requested samples.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            int:

            Indicates the number of samples acquired by each channel.
            NI-DAQmx returns a single value because this value is the
            same for all channels.
        

#### `def read_many_sample_uint32(self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0)`

Reads one or more 32-bit unsigned integer samples from a single counter input channel in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of 32-bit unsigned integer values to hold the
                samples requested.

                Each element in the array corresponds to a sample from
                the channel. The size of the array must be large enough
                to hold all requested samples from the channel in the
                task; otherwise, an error is thrown.
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read.

                If you set this input to nidaqmx.constants.
                READ_ALL_AVAILABLE, NI-DAQmx determines how many samples
                to read based on if the task acquires samples
                continuously or acquires a finite number of samples.

                If the task acquires samples continuously and you set
                this input to nidaqmx.constants.READ_ALL_AVAILABLE, this
                method reads all the samples currently available in the
                buffer.

                If the task acquires a finite number of samples and you
                set this input to nidaqmx.constants.READ_ALL_AVAILABLE,
                the method waits for the task to acquire all requested
                samples, then reads those samples. If you set the
                "read_all_avail_samp" property to True, the method reads
                the samples currently available in the buffer and does
                not wait for the task to acquire all requested samples.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            int:

            Indicates the number of samples acquired by each channel.
            NI-DAQmx returns a single value because this value is the
            same for all channels.
        

#### `def read_one_sample_double(self, timeout=10)`

Reads a single floating-point sample from a single counter input channel in a task.

        Args:
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            float: Indicates a single floating-point sample from the
                task.
        

#### `def read_one_sample_pulse_frequency(self, timeout=10)`

Reads a pulse sample in terms of frequency from a single counter input channel in a task.

        Args:
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            nidaqmx.types.CtrFreq:

            Indicates a pulse sample in terms of frequency from the task.
        

#### `def read_one_sample_pulse_ticks(self, timeout=10)`

Reads a pulse sample in terms of ticks from a single counter input channel in a task.

        Args:
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            nidaqmx.types.CtrTick:

            Indicates a pulse sample in terms of ticks from the task.
        

#### `def read_one_sample_pulse_time(self, timeout=10)`

Reads a pulse sample in terms of time from a single counter input channel in a task.

        Args:
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            nidaqmx.types.CtrTime:

            Indicates a pulse sample in terms of time from the task.
        

#### `def read_one_sample_uint32(self, timeout=10)`

Reads a single 32-bit unsigned integer sample from a single counter input channel in a task.

        Args:
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            int:

            Indicates a single 32-bit unsigned integer sample from the
            task.
        
