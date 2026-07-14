# NI OSS SOURCE SNAPSHOT: nidaqmx-python

<!--NI_OSS_SNAPSHOT repo=ni/nidaqmx-python commit=03282e1b5c741b9f37e4a4e1b5de3a52ae72442e -->

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/stream_readers/_counter_reader.py sha256=e1d4cbf29f438afb096e1c34f9354ba9bcd65adcee2f5b8ef2608cdb3fe88e30 bytes=25555 -->
## FILE: src/handwritten/stream_readers/_counter_reader.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/stream_readers/_counter_reader.py`
- sha256: `e1d4cbf29f438afb096e1c34f9354ba9bcd65adcee2f5b8ef2608cdb3fe88e30`
- bytes: 25555

````python
from __future__ import annotations

from nidaqmx.constants import READ_ALL_AVAILABLE, FillMode
from nidaqmx.stream_readers._channel_reader_base import ChannelReaderBase
from nidaqmx.types import CtrFreq, CtrTick, CtrTime


class CounterReader(ChannelReaderBase):
    """Reads samples from a counter input channel in an NI-DAQmx task."""

    def read_many_sample_double(
        self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0
    ):
        """Reads one or more floating-point samples from a single counter input channel in a task.

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
        """
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(data, number_of_samples_per_channel, False, True)

        _, samps_per_chan_read = self._interpreter.read_counter_f64_ex(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            data,
        )

        return samps_per_chan_read

    def read_many_sample_pulse_frequency(
        self,
        frequencies,
        duty_cycles,
        number_of_samples_per_channel=READ_ALL_AVAILABLE,
        timeout=10.0,
    ):
        """Reads one or more pulse samples in terms of frequency from a single counter input channel in a task.

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
        """  # noqa: W505 - doc line too long (111 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(frequencies, number_of_samples_per_channel, False, True)
        self._verify_array(duty_cycles, number_of_samples_per_channel, False, True)

        _, _, samps_per_chan_read = self._interpreter.read_ctr_freq(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            frequencies,
            duty_cycles,
        )

        return samps_per_chan_read

    def read_many_sample_pulse_ticks(
        self, high_ticks, low_ticks, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0
    ):
        """Reads one or more pulse samples in terms of ticks from a single counter input channel in a task.

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
        """  # noqa: W505 - doc line too long (107 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(high_ticks, number_of_samples_per_channel, False, True)
        self._verify_array(low_ticks, number_of_samples_per_channel, False, True)

        _, _, samps_per_chan_read = self._interpreter.read_ctr_ticks(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            high_ticks,
            low_ticks,
        )

        return samps_per_chan_read

    def read_many_sample_pulse_time(
        self, high_times, low_times, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0
    ):
        """Reads one or more pulse samples in terms of time from a single counter input channel in a task.

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
        """  # noqa: W505 - doc line too long (106 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(high_times, number_of_samples_per_channel, False, True)
        self._verify_array(low_times, number_of_samples_per_channel, False, True)

        _, _, samps_per_chan_read = self._interpreter.read_ctr_time(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            high_times,
            low_times,
        )

        return samps_per_chan_read

    def read_many_sample_uint32(
        self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0
    ):
        """Reads one or more 32-bit unsigned integer samples from a single counter input channel in a task.

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
        """  # noqa: W505 - doc line too long (107 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(data, number_of_samples_per_channel, False, True)

        _, samps_per_chan_read = self._interpreter.read_counter_u32_ex(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            data,
        )

        return samps_per_chan_read

    def read_one_sample_double(self, timeout=10):
        """Reads a single floating-point sample from a single counter input channel in a task.

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
        """
        return self._interpreter.read_counter_scalar_f64(self._handle, timeout)

    def read_one_sample_pulse_frequency(self, timeout=10):
        """Reads a pulse sample in terms of frequency from a single counter input channel in a task.

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
        """
        freq, duty_cycle = self._interpreter.read_ctr_freq_scalar(self._handle, timeout)

        return CtrFreq(freq, duty_cycle)

    def read_one_sample_pulse_ticks(self, timeout=10):
        """Reads a pulse sample in terms of ticks from a single counter input channel in a task.

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
        """
        high_ticks, low_ticks = self._interpreter.read_ctr_ticks_scalar(self._handle, timeout)

        return CtrTick(high_ticks, low_ticks)

    def read_one_sample_pulse_time(self, timeout=10):
        """Reads a pulse sample in terms of time from a single counter input channel in a task.

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
        """
        high_time, low_time = self._interpreter.read_ctr_time_scalar(self._handle, timeout)

        return CtrTime(high_time, low_time)

    def read_one_sample_uint32(self, timeout=10):
        """Reads a single 32-bit unsigned integer sample from a single counter input channel in a task.

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
        """  # noqa: W505 - doc line too long (103 > 100 characters) (auto-generated noqa)
        return self._interpreter.read_counter_scalar_u32(self._handle, timeout)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/stream_readers/_digital_multi_channel_reader.py sha256=0614e4a29e118ba58285914646597a81abbe245ac3ee97a2271b4d5a7bc19cf1 bytes=29381 -->
## FILE: src/handwritten/stream_readers/_digital_multi_channel_reader.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/stream_readers/_digital_multi_channel_reader.py`
- sha256: `0614e4a29e118ba58285914646597a81abbe245ac3ee97a2271b4d5a7bc19cf1`
- bytes: 29381

````python
from __future__ import annotations

from typing import Any

from nitypes.waveform import DigitalWaveform

from nidaqmx import DaqError
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, requires_feature
from nidaqmx.constants import READ_ALL_AVAILABLE, FillMode, ReallocationPolicy
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.stream_readers._channel_reader_base import ChannelReaderBase


class DigitalMultiChannelReader(ChannelReaderBase):
    """Reads samples from one or more digital input channels in an NI-DAQmx task."""

    def read_many_sample_port_byte(
        self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0
    ):
        """Reads one or more 8-bit unsigned integer samples from one or more digital input channel in a task.

        Use this method for devices with up to 8 lines per port.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 2D NumPy
                array of 8-bit unsigned integer values to hold the
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
        """  # noqa: W505 - doc line too long (109 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(data, number_of_samples_per_channel, True, True)

        _, samps_per_chan_read = self._interpreter.read_digital_u8(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            data,
        )

        return samps_per_chan_read

    def read_many_sample_port_uint16(
        self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0
    ):
        """Reads one or more 16-bit unsigned integer samples from one or more digital input channels in a task.

        Use this method for devices with up to 16 lines per port.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 2D NumPy
                array of 16-bit unsigned integer values to hold the
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
        """  # noqa: W505 - doc line too long (111 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(data, number_of_samples_per_channel, True, True)

        _, samps_per_chan_read = self._interpreter.read_digital_u16(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            data,
        )

        return samps_per_chan_read

    def read_many_sample_port_uint32(
        self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0
    ):
        """Reads one or more 32-bit unsigned integer samples from one or more digital input channels in a task.

        Use this method for devices with up to 32 lines per port.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 2D NumPy
                array of 32-bit unsigned integer values to hold the
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
        """  # noqa: W505 - doc line too long (111 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(data, number_of_samples_per_channel, True, True)

        _, samps_per_chan_read = self._interpreter.read_digital_u32(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            data,
        )

        return samps_per_chan_read

    def read_one_sample_multi_line(self, data, timeout=10):
        """Reads a single boolean sample from one or more digital input channels in a task.

        The channels can contain multiple digital lines.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 2D NumPy
                array of boolean values to hold the samples requested.
                The size of the array must be large enough to hold all
                requested samples from all channels in the task;
                otherwise, an error is thrown.

                Each row corresponds to a channel in the task. Each
                column corresponds to a line from each channel. The
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
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.
        """
        self._verify_array_digital_lines(data, True, True)

        _, samps_per_chan_read, num_bytes_per_samp = self._interpreter.read_digital_lines(
            self._handle, 1, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def read_one_sample_one_line(self, data, timeout=10):
        """Reads a single boolean sample from one or more digital input channels in a task.

        The channel can contain only one digital line.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of boolean values to hold the samples requested.

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
        """
        self._verify_array_digital_lines(data, True, False)

        _, samps_per_chan_read, num_bytes_per_samp = self._interpreter.read_digital_lines(
            self._handle, 1, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def read_one_sample_port_byte(self, data, timeout=10):
        """Reads a single 8-bit unsigned integer sample from one or more digital input channels in a task.

        Use this method for devices with up to 8 lines per port.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of 8-bit unsigned integer values to hold the
                samples requested.

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
        """  # noqa: W505 - doc line too long (106 > 100 characters) (auto-generated noqa)
        self._verify_array(data, 1, True, False)

        self._interpreter.read_digital_u8(
            self._handle, 1, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def read_one_sample_port_uint16(self, data, timeout=10):
        """Reads a single 16-bit unsigned integer sample from one or more digital input channels in a task.

        Use this method for devices with up to 16 lines per port.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of 16-bit unsigned integer values to hold the
                samples requested.

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
        """  # noqa: W505 - doc line too long (107 > 100 characters) (auto-generated noqa)
        self._verify_array(data, 1, True, False)

        self._interpreter.read_digital_u16(
            self._handle, 1, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def read_one_sample_port_uint32(self, data, timeout=10):
        """Reads a single 32-bit unsigned integer sample from one or more digital input channels in a task.

        Use this method for devices with up to 32 lines per port.

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
        """  # noqa: W505 - doc line too long (107 > 100 characters) (auto-generated noqa)
        self._verify_array(data, 1, True, False)

        self._interpreter.read_digital_u32(
            self._handle, 1, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    @requires_feature(WAVEFORM_SUPPORT)
    def read_waveforms(
        self,
        waveforms: list[DigitalWaveform[Any]],
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        reallocation_policy: ReallocationPolicy = ReallocationPolicy.TO_GROW,
        timeout: float = 10.0,
    ) -> int:
        """Reads one or more samples from one or more digital input channels into a list of waveforms.

        Args:
            waveforms (list[DigitalWaveform[Any]]): Specifies an existing
                list of DigitalWaveform objects to use for reading samples into.
                The list must contain one waveform
                for each channel in the task.
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
        """  # noqa: W505 - doc line too long (102 > 100 characters) (auto-generated noqa)
        number_of_channels = self._in_stream.num_chans
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        if len(waveforms) != number_of_channels:
            raise DaqError(
                f"The number of waveforms provided ({len(waveforms)}) does not match "
                f"the number of channels in the task ({number_of_channels}). Please provide "
                "one waveform for each channel.",
                DAQmxErrors.MISMATCHED_INPUT_ARRAY_SIZES,
                task_name=self._task.name,
            )

        for i, waveform in enumerate(waveforms):
            if waveform.start_index + number_of_samples_per_channel > waveform.capacity:
                if reallocation_policy == ReallocationPolicy.TO_GROW:
                    waveform.capacity = waveform.start_index + number_of_samples_per_channel
                else:
                    raise DaqError(
                        f"The waveform at index {i} does not have enough space ({waveform.capacity - waveform.start_index}) to hold "
                        f"the requested number of samples ({number_of_samples_per_channel}). Please provide larger "
                        "waveforms or adjust the number of samples requested.",
                        DAQmxErrors.READ_BUFFER_TOO_SMALL,
                        task_name=self._task.name,
                    )

        return self._interpreter.read_digital_waveforms(
            self._handle,
            number_of_channels,
            number_of_samples_per_channel,
            self._in_stream.di_num_booleans_per_chan,
            timeout,
            waveforms,
            self._in_stream.waveform_attribute_mode,
        )
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/stream_readers/_digital_single_channel_reader.py sha256=db8e0ea60e170137e689970d9887f3f67fe7605940231f0d428ba295ff92bbb8 bytes=22344 -->
## FILE: src/handwritten/stream_readers/_digital_single_channel_reader.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/stream_readers/_digital_single_channel_reader.py`
- sha256: `db8e0ea60e170137e689970d9887f3f67fe7605940231f0d428ba295ff92bbb8`
- bytes: 22344

````python
from __future__ import annotations

from typing import Any

import numpy
from nitypes.waveform import DigitalWaveform

from nidaqmx import DaqError
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, requires_feature
from nidaqmx.constants import READ_ALL_AVAILABLE, FillMode, ReallocationPolicy
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.stream_readers._channel_reader_base import ChannelReaderBase


class DigitalSingleChannelReader(ChannelReaderBase):
    """Reads samples from a digital input channel in an NI-DAQmx task."""

    def read_many_sample_port_byte(
        self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0
    ):
        """Reads one or more 8-bit unsigned integer samples from a single digital input channel in a task.

        Use this method for devices with up to 8 lines per port.

        This read method accepts a preallocated NumPy array to hold
        the samples requested, which can be advantageous for performance
        and interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of 8-bit unsigned integer values to hold the
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
        """  # noqa: W505 - doc line too long (106 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(data, number_of_samples_per_channel, False, True)

        _, samps_per_chan_read = self._interpreter.read_digital_u8(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            data,
        )

        return samps_per_chan_read

    def read_many_sample_port_uint16(
        self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0
    ):
        """Reads one or more 16-bit unsigned integer samples from a single digital input channel in a task.

        Use this method for devices with up to 16 lines per port.

        This read method accepts a preallocated NumPy array to hold
        the samples requested, which can be advantageous for performance
        and interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of 16-bit unsigned integer values to hold the
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
        """  # noqa: W505 - doc line too long (107 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(data, number_of_samples_per_channel, False, True)

        _, samps_per_chan_read = self._interpreter.read_digital_u16(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            data,
        )

        return samps_per_chan_read

    def read_many_sample_port_uint32(
        self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0
    ):
        """Reads one or more 32-bit unsigned integer samples from a single digital input channel in a task.

        Use this method for devices with up to 32 lines per port.

        This read method accepts a preallocated NumPy array to hold
        the samples requested, which can be advantageous for performance
        and interoperability with NumPy and SciPy.

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
        """  # noqa: W505 - doc line too long (107 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(data, number_of_samples_per_channel, False, True)

        _, samps_per_chan_read = self._interpreter.read_digital_u32(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            data,
        )

        return samps_per_chan_read

    def read_one_sample_multi_line(self, data, timeout=10):
        """Reads a single boolean sample from a single digital input channel in a task.

        The channel can contain multiple digital lines.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of boolean values to hold the samples requested.

                Each element in the array corresponds to a sample from
                a line in the channel. The size of the array must be
                large enough to hold all requested samples from the
                channel in the task; otherwise, an error is thrown.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.
        """
        self._verify_array_digital_lines(data, False, True)

        _, samps_per_chan_read, num_bytes_per_samp = self._interpreter.read_digital_lines(
            self._handle, 1, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def read_one_sample_one_line(self, timeout=10):
        """Reads a single boolean sample from a single digital input channel in a task.

        The channel can contain only one digital line.

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
            bool:

            Indicates a single boolean sample from the task.
        """
        data = numpy.zeros(1, dtype=bool)
        _, samps_per_chan_read, num_bytes_per_samp = self._interpreter.read_digital_lines(
            self._handle, 1, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

        return bool(data[0])

    def read_one_sample_port_byte(self, timeout=10):
        """Reads a single 8-bit unsigned integer sample from a single digital input channel in a task.

        Use this method for devices with up to 8 lines per port.

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

            Indicates a single 8-bit unsigned integer sample from the
            task.
        """  # noqa: W505 - doc line too long (102 > 100 characters) (auto-generated noqa)
        data = numpy.zeros(1, dtype=numpy.uint8)
        _, samps_per_chan_read = self._interpreter.read_digital_u8(
            self._handle, 1, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

        return int(data[0])

    def read_one_sample_port_uint16(self, timeout=10):
        """Reads a single 16-bit unsigned integer sample from a single digital input channel in a task.

        Use this method for devices with up to 16 lines per port.

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

            Indicates a single 16-bit unsigned integer sample from the
            task.
        """  # noqa: W505 - doc line too long (103 > 100 characters) (auto-generated noqa)
        data = numpy.zeros(1, dtype=numpy.uint16)
        _, samps_per_read_chan = self._interpreter.read_digital_u16(
            self._handle, 1, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

        return int(data[0])

    def read_one_sample_port_uint32(self, timeout=10):
        """Reads a single 32-bit unsigned integer sample from a single digital input channel in a task.

        Use this method for devices with up to 32 lines per port.

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
        """  # noqa: W505 - doc line too long (103 > 100 characters) (auto-generated noqa)
        return self._interpreter.read_digital_scalar_u32(self._handle, timeout)

    @requires_feature(WAVEFORM_SUPPORT)
    def read_waveform(
        self,
        waveform: DigitalWaveform[Any],
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        reallocation_policy: ReallocationPolicy = ReallocationPolicy.TO_GROW,
        timeout: float = 10.0,
    ) -> int:
        """Reads one or more digital samples from a single digital input channel into a waveform.

        Args:
            waveform (DigitalWaveform[Any]): Specifies a
                preallocated DigitalWaveform object to hold the samples
                requested.
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
        """
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        if waveform.start_index + number_of_samples_per_channel > waveform.capacity:
            if reallocation_policy == ReallocationPolicy.TO_GROW:
                waveform.capacity = waveform.start_index + number_of_samples_per_channel
            else:
                raise DaqError(
                    f"The waveform does not have enough space ({waveform.capacity - waveform.start_index}) to hold "
                    f"the requested number of samples ({number_of_samples_per_channel}). Please "
                    "provide a larger waveform or adjust the number of samples requested.",
                    DAQmxErrors.READ_BUFFER_TOO_SMALL,
                    task_name=self._task.name,
                )

        return self._interpreter.read_digital_waveform(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            waveform,
            self._in_stream.waveform_attribute_mode,
        )
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/stream_readers/_power_readers.py sha256=a1ad513d56376e38e37522f76f865a0e00154a68dfd960f7d8f717bd2ee21e75 bytes=20006 -->
## FILE: src/handwritten/stream_readers/_power_readers.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/stream_readers/_power_readers.py`
- sha256: `a1ad513d56376e38e37522f76f865a0e00154a68dfd960f7d8f717bd2ee21e75`
- bytes: 20006

````python
from __future__ import annotations

from nidaqmx.constants import READ_ALL_AVAILABLE, FillMode
from nidaqmx.stream_readers._channel_reader_base import ChannelReaderBase
from nidaqmx.types import PowerMeasurement


class PowerSingleChannelReader(ChannelReaderBase):
    """Reads samples from an analog input power channel in an NI-DAQmx task."""

    def read_many_sample(
        self,
        voltage_data,
        current_data,
        number_of_samples_per_channel=READ_ALL_AVAILABLE,
        timeout=10.0,
    ):
        """Reads one or more floating-point power samples from a single analog input power channel in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            voltage_data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of floating-point values to hold the voltage samples
                requested.

                Each element in the array corresponds to a sample from
                the channel. The size of the array must be large enough
                to hold all requested samples from the channel in the
                task; otherwise, an error is thrown.
            current_data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of floating-point values to hold the current samples
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
        """  # noqa: W505 - doc line too long (109 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(voltage_data, number_of_samples_per_channel, False, True)
        self._verify_array(current_data, number_of_samples_per_channel, False, True)

        _, _, samps_per_chan_read = self._interpreter.read_power_f64(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            voltage_data,
            current_data,
        )

        return samps_per_chan_read

    def read_one_sample(self, timeout=10):
        """Reads a single floating-point power sample from a single analog input power channel in a task.

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

            Indicates a single floating-point power sample from the task.
        """  # noqa: W505 - doc line too long (105 > 100 characters) (auto-generated noqa)
        voltage, current = self._interpreter.read_power_scalar_f64(self._handle, timeout)
        return PowerMeasurement(voltage=voltage, current=current)


class PowerMultiChannelReader(ChannelReaderBase):
    """Reads samples from one or more analog input power channels in an NI-DAQmx task."""

    def read_many_sample(
        self,
        voltage_data,
        current_data,
        number_of_samples_per_channel=READ_ALL_AVAILABLE,
        timeout=10.0,
    ):
        """Reads one or more floating-point power samples from one or more analog input power channels in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            voltage_data (numpy.ndarray): Specifies a preallocated 2D NumPy
                array of floating-point values to hold the voltage samples
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
            current_data (numpy.ndarray): Specifies a preallocated 2D NumPy
                array of floating-point values to hold the current samples
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
        """  # noqa: W505 - doc line too long (113 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(voltage_data, number_of_samples_per_channel, True, True)
        self._verify_array(current_data, number_of_samples_per_channel, True, True)

        _, _, samps_per_chan_read = self._interpreter.read_power_f64(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            voltage_data,
            current_data,
        )

        return samps_per_chan_read

    def read_one_sample(self, voltage_data, current_data, timeout=10):
        """Reads a single floating-point power sample from one or more analog input channels in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            voltage_data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of floating-point values to hold the voltage samples
                requested.

                Each element in the array corresponds to a sample from
                each channel. The size of the array must be large enough
                to hold all requested samples from the channel in the
                task; otherwise, an error is thrown.
            current_data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of floating-point values to hold the voltage samples
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
        """  # noqa: W505 - doc line too long (103 > 100 characters) (auto-generated noqa)
        self._verify_array(voltage_data, 1, True, False)
        self._verify_array(current_data, 1, True, False)

        self._interpreter.read_power_f64(
            self._handle, 1, timeout, FillMode.GROUP_BY_CHANNEL.value, voltage_data, current_data
        )


class PowerBinaryReader(ChannelReaderBase):
    """Reads binary samples from one or more analog input power channels in an NI-DAQmx task."""

    def read_many_sample(
        self,
        voltage_data,
        current_data,
        number_of_samples_per_channel=READ_ALL_AVAILABLE,
        timeout=10.0,
    ):
        """Reads one or more binary int16 samples from one or more analog input power channel in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            voltage_data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of i16 values to hold the voltage samples requested.

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
            current_data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of i16 values to hold the current samples requested.

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
        """  # noqa: W505 - doc line too long (104 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(voltage_data, number_of_samples_per_channel, True, True)
        self._verify_array(current_data, number_of_samples_per_channel, True, True)

        _, _, samps_per_chan_read = self._interpreter.read_power_binary_i16(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            voltage_data,
            current_data,
        )

        return samps_per_chan_read
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/stream_writers/__init__.py sha256=ef6326a50eb71aae2f07f7da699ef2c0f06a2dfb207d6b6910ca48e497962521 bytes=1069 -->
## FILE: src/handwritten/stream_writers/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/stream_writers/__init__.py`
- sha256: `ef6326a50eb71aae2f07f7da699ef2c0f06a2dfb207d6b6910ca48e497962521`
- bytes: 1069

````python
"""NI-DAQmx stream writers.

This package provides classes for writing samples to NI-DAQmx tasks.
"""

from __future__ import annotations

from nidaqmx.stream_writers._analog_multi_channel_writer import AnalogMultiChannelWriter
from nidaqmx.stream_writers._analog_single_channel_writer import (
    AnalogSingleChannelWriter,
)
from nidaqmx.stream_writers._analog_unscaled_writer import AnalogUnscaledWriter
from nidaqmx.stream_writers._channel_writer_base import (
    AUTO_START_UNSET,
    UnsetAutoStartSentinel,
)
from nidaqmx.stream_writers._counter_writer import CounterWriter
from nidaqmx.stream_writers._digital_multi_channel_writer import (
    DigitalMultiChannelWriter,
)
from nidaqmx.stream_writers._digital_single_channel_writer import (
    DigitalSingleChannelWriter,
)

__all__ = [
    "AnalogSingleChannelWriter",
    "AnalogMultiChannelWriter",
    "AnalogUnscaledWriter",
    "CounterWriter",
    "DigitalSingleChannelWriter",
    "DigitalMultiChannelWriter",
    "UnsetAutoStartSentinel",
    "AUTO_START_UNSET",
]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/stream_writers/_analog_multi_channel_writer.py sha256=7e852f33534e67bdc453b55431d72589a6a40a87b8b9ac7eedc3b88df18c6469 bytes=6892 -->
## FILE: src/handwritten/stream_writers/_analog_multi_channel_writer.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/stream_writers/_analog_multi_channel_writer.py`
- sha256: `7e852f33534e67bdc453b55431d72589a6a40a87b8b9ac7eedc3b88df18c6469`
- bytes: 6892

````python
from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from nitypes.waveform import AnalogWaveform

from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, requires_feature
from nidaqmx.constants import FillMode
from nidaqmx.stream_writers._channel_writer_base import (
    AUTO_START_UNSET,
    ChannelWriterBase,
)


class AnalogMultiChannelWriter(ChannelWriterBase):
    """Writes samples to one or more analog output channels in an NI-DAQmx task."""

    def write_many_sample(self, data, timeout=10.0):
        """Writes one or more floating-point samples to one or more analog output channels in a task.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 2D NumPy array of
                floating-point samples to write to the task.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample to write to each channel.
                The order of the channels in the array corresponds to
                the order in which you add the channels to the task.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.

        Returns:
            int: Specifies the actual number of samples this method
            successfully wrote to each channel in the task.
        """  # noqa: W505 - doc line too long (101 > 100 characters) (auto-generated noqa)
        self._verify_array(data, True, True)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_analog_f64(
            self._handle, data.shape[1], auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def write_one_sample(self, data, timeout=10):
        """Writes a single floating-point sample to one or more analog output channels in a task.

        Args:
            data (numpy.ndarray): Contains a 1D NumPy array of
                floating-point samples to write to the task.

                Each element of the array corresponds to a channel in
                the task. The order of the channels in the array
                corresponds to the order in which you add the channels
                to the task.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.
        """
        self._verify_array(data, True, False)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else True

        return self._interpreter.write_analog_f64(
            self._handle, 1, auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    @requires_feature(WAVEFORM_SUPPORT)
    def write_waveforms(
        self, waveforms: Sequence[AnalogWaveform[Any]], timeout: float = 10.0
    ) -> int:
        """Writes waveforms to one or more analog output channels in a task.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            waveforms (Sequence[AnalogWaveform[Any]]): Contains one or
                more waveforms to write to the task. All waveforms must
                have the same number of samples.

                Each waveform corresponds to a channel in the task.
                The order of the waveforms corresponds to
                the order in which you add the channels to the task.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.

        Returns:
            int: Specifies the actual number of samples this method
            successfully wrote to each channel in the task.
        """
        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_analog_waveforms(
            self._handle, waveforms, auto_start, timeout
        )
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/stream_writers/_analog_single_channel_writer.py sha256=b628d1f094ab475a8a26bd6bbdb8ab9dfe5e182486166a9afa61b1fbe26c1712 bytes=5997 -->
## FILE: src/handwritten/stream_writers/_analog_single_channel_writer.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/stream_writers/_analog_single_channel_writer.py`
- sha256: `b628d1f094ab475a8a26bd6bbdb8ab9dfe5e182486166a9afa61b1fbe26c1712`
- bytes: 5997

````python
from __future__ import annotations

from typing import Any

from nitypes.waveform import AnalogWaveform

from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, requires_feature
from nidaqmx.constants import FillMode
from nidaqmx.stream_writers._channel_writer_base import (
    AUTO_START_UNSET,
    ChannelWriterBase,
)


class AnalogSingleChannelWriter(ChannelWriterBase):
    """Writes samples to an analog output channel in an NI-DAQmx task."""

    def write_many_sample(self, data, timeout=10.0):
        """Writes one or more floating-point samples to a single analog output channel in a task.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 1D NumPy array of
                floating-point samples to write to the task. Each
                element of the array corresponds to a sample to write.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.

        Returns:
            int:

            Specifies the actual number of samples this method
            successfully wrote.
        """
        self._verify_array(data, False, True)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_analog_f64(
            self._handle, data.shape[0], auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def write_one_sample(self, data, timeout=10):
        """Writes a single floating-point sample to a single analog output channel in a task.

        Args:
            data (float): Specifies the floating-point sample to write
                to the task.
            auto_start (Optional[bool]): Specifies if this method
                automatically starts the task if you did not explicitly
                start it with the DAQmx Start Task method.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.
        """
        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else True

        return self._interpreter.write_analog_scalar_f64(self._handle, auto_start, timeout, data)

    @requires_feature(WAVEFORM_SUPPORT)
    def write_waveform(self, waveform: AnalogWaveform[Any], timeout: float = 10.0) -> int:
        """Writes a waveform to a single analog output channel in a task.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            waveform (AnalogWaveform[Any]): Specifies the
                waveform to write to the task.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.

        Returns:
            int: Specifies the actual number of samples this method
            successfully wrote.
        """
        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_analog_waveform(self._handle, waveform, auto_start, timeout)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/stream_writers/_analog_unscaled_writer.py sha256=108e6cc0885aac21d4f39918e16dff0803829c4ed03d6b4c432f365b0d6d56dc bytes=9629 -->
## FILE: src/handwritten/stream_writers/_analog_unscaled_writer.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/stream_writers/_analog_unscaled_writer.py`
- sha256: `108e6cc0885aac21d4f39918e16dff0803829c4ed03d6b4c432f365b0d6d56dc`
- bytes: 9629

````python
from nidaqmx.constants import FillMode
from nidaqmx.stream_writers._channel_writer_base import (
    AUTO_START_UNSET,
    ChannelWriterBase,
)


class AnalogUnscaledWriter(ChannelWriterBase):
    """Writes unscaled samples to one or more analog output channels in an NI-DAQmx task."""

    def write_int16(self, data, timeout=10.0):
        """Writes one or more unscaled 16-bit integer samples to one or more analog output channels in a task.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 2D NumPy array of unscaled
                16-bit integer samples to write to the task.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample to write to each channel.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.

        Returns:
            int:

            Specifies the actual number of samples this method
            successfully wrote to each channel in the task.
        """  # noqa: W505 - doc line too long (110 > 100 characters) (auto-generated noqa)
        self._verify_array(data, True, True)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_binary_i16(
            self._handle, data.shape[1], auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def write_int32(self, data, timeout=10.0):
        """Writes one or more unscaled 32-bit integer samples to one or more analog output channels in a task.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 2D NumPy array of unscaled
                32-bit integer samples to write to the task.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample to write to each channel.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.

        Returns:
            int:

            Specifies the actual number of samples this method
            successfully wrote to each channel in the task.
        """  # noqa: W505 - doc line too long (110 > 100 characters) (auto-generated noqa)
        self._verify_array(data, True, True)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_binary_i32(
            self._handle, data.shape[1], auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def write_uint16(self, data, timeout=10.0):
        """Writes one or more unscaled 16-bit unsigned integer samples to one or more analog output channels in a task.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 2D NumPy array of unscaled
                16-bit unsigned integer samples to write to the task.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample to write to each channel.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.

        Returns:
            int:

            Specifies the actual number of samples this method
            successfully wrote to each channel in the task.
        """  # noqa: W505 - doc line too long (119 > 100 characters) (auto-generated noqa)
        self._verify_array(data, True, True)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_binary_u16(
            self._handle, data.shape[1], auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def write_uint32(self, data, timeout=10.0):
        """Writes one or more unscaled 32-bit unsigned integer samples to one or more analog output channels in a task.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 2D NumPy array of unscaled
                32-bit unsigned integer samples to write to the task.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample to write to each channel.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.

        Returns:
            int:

            Specifies the actual number of samples this method
            successfully wrote to each channel in the task.
        """  # noqa: W505 - doc line too long (119 > 100 characters) (auto-generated noqa)
        self._verify_array(data, True, True)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_binary_u32(
            self._handle, data.shape[1], auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/stream_writers/_channel_writer_base.py sha256=db0cea87bad6f247a7151114aae783bc58902b0db087266943dbfc773cfd434a bytes=6797 -->
## FILE: src/handwritten/stream_writers/_channel_writer_base.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/stream_writers/_channel_writer_base.py`
- sha256: `db0cea87bad6f247a7151114aae783bc58902b0db087266943dbfc773cfd434a`
- bytes: 6797

````python
from nidaqmx import DaqError
from nidaqmx.error_codes import DAQmxErrors


class UnsetAutoStartSentinel:
    """Sentinel class for unset auto_start parameter."""

    def __init__(self):  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        raise RuntimeError(
            "Cannot instantiate UnsetAutoStartSentinel. Use AUTO_START_UNSET instead."
        )


AUTO_START_UNSET = object.__new__(UnsetAutoStartSentinel)


class ChannelWriterBase:
    """Defines base class for all NI-DAQmx stream writers."""

    def __init__(self, task_out_stream, auto_start=AUTO_START_UNSET):
        """Initialize a new ChannelWriterBase.

        Args:
            task_out_stream: Specifies the output stream associated with
                an NI-DAQmx task which to write samples.
            auto_start (Optional[bool]): Specifies if the write method
                automatically starts the task if you did not explicitly
                start it with the DAQmx Start Task method.

                If you do not specify a value for this parameter,
                NI-DAQmx determines its value based on the type of write
                method used. If you use a one sample write method, the
                value is True; conversely, if you use a many sample
                write method, the value is False.
        """
        self._out_stream = task_out_stream
        self._task = task_out_stream._task
        self._handle = task_out_stream._task._handle
        self._interpreter = task_out_stream._task._interpreter

        self._verify_array_shape = True
        self._auto_start = auto_start

    @property
    def auto_start(self):
        """bool: Specifies whether the write method automatically starts the task, if needed.

        If you do not specify a value for this parameter, NI-DAQmx
        determines its value based on the type of write method used.
        If you use a one sample write method, its value is True;
        conversely, if you use a many sample write method, its value
        is False.
        """
        return self._auto_start

    @auto_start.setter
    def auto_start(self, val):
        self._auto_start = val

    @auto_start.deleter
    def auto_start(self):
        self._auto_start = AUTO_START_UNSET

    @property
    def verify_array_shape(self):
        """bool: Specifies whether to verify the shape of NumPy arrays.

        Defaults to True when this object is instantiated.

        Setting this property to True may marginally adversely
        impact the performance of read methods.
        """
        return self._verify_array_shape

    @verify_array_shape.setter
    def verify_array_shape(self, val):
        self._verify_array_shape = val

    def _verify_array(self, data, is_many_chan, is_many_samp):
        """Verifies the shape of a NumPy array.

        Verifies that the shape of the specified NumPy array can be used
        with the specified write method type, if the
        "verify_array_shape" property is set to True.

        Args:
            data (numpy.ndarray): Specifies the NumPy array to verify.
            is_many_chan (bool): Specifies if the write method is a many
                channel version.
            is_many_samp (bool): Specifies if the write method is a many
                sample version.
        """
        if not self._verify_array_shape:
            return

        number_of_channels = self._out_stream.num_chans

        expected_num_dimensions = None
        if is_many_chan:
            if is_many_samp:
                expected_num_dimensions = 2
            else:
                expected_num_dimensions = 1

            if data.shape[0] != number_of_channels:
                self._task._raise_invalid_write_num_chans_error(number_of_channels, data.shape[0])
        else:
            if is_many_samp:
                expected_num_dimensions = 1

        if expected_num_dimensions is not None:
            self._raise_error_if_invalid_write_dimensions(expected_num_dimensions, len(data.shape))

    def _verify_array_digital_lines(self, data, is_many_chan, is_many_line):
        """Verify the shape of a NumPy array of digital lines.

        Verifies that the shape of the specified NumPy array can be used
        to read samples from the current task which contains one or more
        channels that have one or more digital lines per channel, if the
        "verify_array_shape" property is set to True.

        Args:
            data (numpy.ndarray): Specifies the NumPy array to verify.
            is_many_chan (bool): Specifies if the write method is a
                many channel version.
            is_many_line (bool): Specifies if the write method is a
                many line version.
        """
        if not self._verify_array_shape:
            return

        number_of_channels = self._out_stream.num_chans
        number_of_lines = self._out_stream.do_num_booleans_per_chan

        expected_num_dimensions = None
        if is_many_chan:
            if data.shape[0] != number_of_channels:
                self._task._raise_invalid_write_num_chans_error(number_of_channels, data.shape[0])

            if is_many_line:
                expected_num_dimensions = 2
                if data.shape[1] != number_of_lines:
                    self._task._raise_invalid_num_lines_error(number_of_lines, data.shape[1])
            else:
                expected_num_dimensions = 1
        else:
            if is_many_line:
                expected_num_dimensions = 1
                if data.shape[0] != number_of_lines:
                    self._task._raise_invalid_num_lines_error(number_of_lines, data.shape[0])

        if expected_num_dimensions is not None:
            self._raise_error_if_invalid_write_dimensions(expected_num_dimensions, len(data.shape))

    def _raise_error_if_invalid_write_dimensions(
        self, num_dimensions_expected, num_dimensions_in_data
    ):
        if num_dimensions_expected != num_dimensions_in_data:
            raise DaqError(
                "Write cannot be performed because the NumPy array passed "
                "into this function is not shaped correctly. "
                "You must pass in a NumPy array of the correct number of "
                "dimensions based on the write method you use.\n\n"
                "No. of dimensions of NumPy Array provided: {}\n"
                "No. of dimensions of NumPy Array required: {}".format(
                    num_dimensions_in_data, num_dimensions_expected
                ),
                DAQmxErrors.UNKNOWN,
                task_name=self._task.name,
            )
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/stream_writers/_counter_writer.py sha256=96aa74486749b7f0e914a1136b9c59fe8f0895038cb92e48f7624d81ac0a19f0 bytes=13240 -->
## FILE: src/handwritten/stream_writers/_counter_writer.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/stream_writers/_counter_writer.py`
- sha256: `96aa74486749b7f0e914a1136b9c59fe8f0895038cb92e48f7624d81ac0a19f0`
- bytes: 13240

````python
from nidaqmx.constants import FillMode
from nidaqmx.stream_writers._channel_writer_base import (
    AUTO_START_UNSET,
    ChannelWriterBase,
)


class CounterWriter(ChannelWriterBase):
    """Writes samples to a counter output channel in an NI-DAQmx task."""

    def write_many_sample_pulse_frequency(self, frequencies, duty_cycles, timeout=10.0):
        """Writes one or more pulse samples in terms of frequency to a single counter output channel in a task.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            frequencies (numpy.ndarray): Contains a 1D NumPy array of
                floating-point values that holds the frequency portion
                of the pulse samples to write to the task. Each element
                of the array corresponds to a sample to write.
            duty_cycles (numpy.ndarray): Contains a 1D NumPy array of
                floating-point values that holds the duty cycle portion
                of the pulse samples to write to the task. Each element
                of the array corresponds to a sample to write.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.

        Returns:
            int:

            Specifies the actual number of samples this method
            successfully wrote.
        """  # noqa: W505 - doc line too long (111 > 100 characters) (auto-generated noqa)
        self._verify_array(frequencies, False, True)
        self._verify_array(duty_cycles, False, True)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_ctr_freq(
            self._handle,
            frequencies.shape[0],
            auto_start,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            frequencies,
            duty_cycles,
        )

    def write_many_sample_pulse_ticks(self, high_ticks, low_ticks, timeout=10.0):
        """Writes one or more pulse samples in terms of ticks to a single counter output channel in a task.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            high_ticks (numpy.ndarray): Contains a 1D NumPy array of
                32-bit unsigned integer values that holds the high ticks
                portion of the pulse samples to write to the task. Each
                element of the array corresponds to a sample to write.
            low_ticks (numpy.ndarray): Contains a 1D NumPy array of
                32-bit unsigned integer values that holds the low ticks
                portion of the pulse samples to write to the task. Each
                element of the array corresponds to a sample to write.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.

        Returns:
            int:

            Specifies the actual number of samples this method
            successfully wrote.
        """  # noqa: W505 - doc line too long (107 > 100 characters) (auto-generated noqa)
        self._verify_array(high_ticks, False, True)
        self._verify_array(low_ticks, False, True)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_ctr_ticks(
            self._handle,
            high_ticks.shape[0],
            auto_start,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            high_ticks,
            low_ticks,
        )

    def write_many_sample_pulse_time(self, high_times, low_times, timeout=10.0):
        """Writes one or more pulse samples in terms of time to a single counter output channel in a task.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            high_times (numpy.ndarray): Contains a 1D NumPy array of
                floating-point values that holds the high time portion
                of the pulse samples to write to the task. Each element
                of the array corresponds to a sample to write.
            low_times (numpy.ndarray): Contains a 1D NumPy array of
                floating-point values that holds the low time portion
                of the pulse samples to write to the task. Each element
                of the array corresponds to a sample to write.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.

        Returns:
            int:

            Specifies the actual number of samples this method
            successfully wrote.
        """  # noqa: W505 - doc line too long (106 > 100 characters) (auto-generated noqa)
        self._verify_array(high_times, False, True)
        self._verify_array(low_times, False, True)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_ctr_time(
            self._handle,
            high_times.shape[0],
            auto_start,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            high_times,
            low_times,
        )

    def write_one_sample_pulse_frequency(self, frequency, duty_cycle, timeout=10):
        """Writes a new pulse frequency and duty cycle to a single counter output channel in a task.

        Args:
            frequency (float): Specifies at what frequency to generate
                pulses.
            duty_cycle (float): Specifies the width of the pulse divided
                by the pulse period. NI-DAQmx uses this ratio combined
                with frequency to determine pulse width and the interval
                between pulses.
            auto_start (Optional[bool]): Specifies if this method
                automatically starts the task if you did not explicitly
                start it with the DAQmx Start Task method.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.
        """
        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else True

        return self._interpreter.write_ctr_freq_scalar(
            self._handle, auto_start, timeout, frequency, duty_cycle
        )

    def write_one_sample_pulse_ticks(self, high_ticks, low_ticks, timeout=10):
        """Writes a new pulse high tick count and low tick count to a single counter output channel in a task.

        Args:
            high_ticks (float): Specifies the number of ticks the pulse
                is high.
            low_ticks (float): Specifies the number of ticks the pulse
                is low.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.
        """  # noqa: W505 - doc line too long (110 > 100 characters) (auto-generated noqa)
        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else True

        return self._interpreter.write_ctr_ticks_scalar(
            self._handle, auto_start, timeout, high_ticks, low_ticks
        )

    def write_one_sample_pulse_time(self, high_time, low_time, timeout=10):
        """Writes a new pulse high time and low time to a single counter output channel in a task.

        Args:
            high_time (float): Specifies the amount of time the pulse
                is high.
            low_time (float): Specifies the amount of time the pulse
                is low.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.
        """
        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else True

        return self._interpreter.write_ctr_time_scalar(
            self._handle, auto_start, timeout, high_time, low_time
        )
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/stream_writers/_digital_multi_channel_writer.py sha256=2612756d644ab2fb5cd4b86bfe31fa0a7b631fd0112b1e900392512ec851ae62 bytes=18411 -->
## FILE: src/handwritten/stream_writers/_digital_multi_channel_writer.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/stream_writers/_digital_multi_channel_writer.py`
- sha256: `2612756d644ab2fb5cd4b86bfe31fa0a7b631fd0112b1e900392512ec851ae62`
- bytes: 18411

````python
from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from nitypes.waveform import DigitalWaveform

from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, requires_feature
from nidaqmx.constants import FillMode
from nidaqmx.stream_writers._channel_writer_base import (
    AUTO_START_UNSET,
    ChannelWriterBase,
)


class DigitalMultiChannelWriter(ChannelWriterBase):
    """Writes samples to one or more digital output channels in an NI-DAQmx task."""

    def write_many_sample_port_byte(self, data, timeout=10.0):
        """Writes 8-bit unsigned integer samples to one or more digital output channels in a task.

        Use this method for devices with up to 8 lines per port.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 2D NumPy array of 8-bit
                unsigned integer samples to write to the task.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample to write to each channel.
                The order of the channels in the array corresponds to
                the order in which you add the channels to the task.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.

        Returns:
            int:

            Specifies the actual number of samples this method
            successfully wrote to each channel in the task.
        """
        self._verify_array(data, True, True)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_digital_u8(
            self._handle, data.shape[1], auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def write_many_sample_port_uint16(self, data, timeout=10.0):
        """Writes 16-bit unsigned integer samples to one or more digital output channels in a task.

        Use this method for devices with up to 16 lines per port.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 2D NumPy array of 16-bit
                unsigned integer samples to write to the task.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample to write to each channel.
                The order of the channels in the array corresponds to
                the order in which you add the channels to the task.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.

        Returns:
            int:

            Specifies the actual number of samples this method
            successfully wrote to each channel in the task.
        """
        self._verify_array(data, True, True)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_digital_u16(
            self._handle, data.shape[1], auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def write_many_sample_port_uint32(self, data, timeout=10.0):
        """Writes 32-bit unsigned integer samples to one or more digital output channels in a task.

        Use this method for devices with up to 32 lines per port.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 2D NumPy array of 32-bit
                unsigned integer samples to write to the task.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample to write to each channel.
                The order of the channels in the array corresponds to
                the order in which you add the channels to the task.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.

        Returns:
            int:

            Specifies the actual number of samples this method
            successfully wrote to each channel in the task.
        """
        self._verify_array(data, True, True)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_digital_u32(
            self._handle, data.shape[1], auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def write_one_sample_multi_line(self, data, timeout=10):
        """Writes a single boolean sample to one or more digital output channels in a task.

        The channel can contain multiple digital lines.

        Args:
            data (numpy.ndarray): Contains a 2D NumPy array of boolean
                samples to write to the task.

                Each row corresponds to a channel in the task. Each
                column corresponds to a line from each channel. The
                order of the channels in the array corresponds to the
                order in which you add the channels to the task.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.
        """
        self._verify_array_digital_lines(data, True, True)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else True

        return self._interpreter.write_digital_lines(
            self._handle, 1, auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def write_one_sample_one_line(self, data, timeout=10):
        """Writes a single boolean sample to one or more digital output channels in a task.

        The channel can contain only one digital line.

        Args:
            data (numpy.ndarray): Contains a 1D NumPy array of boolean
                samples to write to the task.

                Each element in the array corresponds to a channel in
                the task. The order of the channels in the array
                corresponds to the order in which you add the channels
                to the task.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.
        """
        self._verify_array_digital_lines(data, True, False)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else True

        return self._interpreter.write_digital_lines(
            self._handle, 1, auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def write_one_sample_port_byte(self, data, timeout=10):
        """Writes a single 8-bit unsigned integer sample to one or more digital output channels.

        Use this method for devices with up to 8 lines per port.

        Args:
            data (numpy.ndarray): Contains a 1D NumPy array of 8-bit
                unsigned integer samples to write to the task.

                Each element in the array corresponds to a channel in
                the task. The order of the channels in the array
                corresponds to the order in which you add the channels
                to the task.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.
        """
        self._verify_array(data, True, False)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else True

        return self._interpreter.write_digital_u8(
            self._handle, 1, auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def write_one_sample_port_uint16(self, data, timeout=10):
        """Writes a single 16-bit unsigned integer sample to one or more digital output channels.

        Use this method for devices with up to 16 lines per port.

        Args:
            data (numpy.ndarray): Contains a 1D NumPy array of 16-bit
                unsigned integer samples to write to the task.

                Each element in the array corresponds to a channel in
                the task. The order of the channels in the array
                corresponds to the order in which you add the channels
                to the task.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.
        """
        self._verify_array(data, True, False)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else True

        return self._interpreter.write_digital_u16(
            self._handle, 1, auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def write_one_sample_port_uint32(self, data, timeout=10):
        """Writes a single 32-bit unsigned integer sample to one or more digital output channels.

        Use this method for devices with up to 32 lines per port.

        Args:
            data (numpy.ndarray): Contains a 1D NumPy array of 32-bit
                unsigned integer samples to write to the task.

                Each element in the array corresponds to a channel in
                the task. The order of the channels in the array
                corresponds to the order in which you add the channels
                to the task.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.
        """
        self._verify_array(data, True, False)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else True

        return self._interpreter.write_digital_u32(
            self._handle, 1, auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    @requires_feature(WAVEFORM_SUPPORT)
    def write_waveforms(
        self, waveforms: Sequence[DigitalWaveform[Any]], timeout: float = 10.0
    ) -> int:
        """Writes waveforms to one or more digital output channels in a task.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            waveforms (Sequence[DigitalWaveform[Any]]): Specifies the
                waveforms to write to the task.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.

        Returns:
            int: Specifies the actual number of samples per channel this method
            successfully wrote.
        """
        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_digital_waveforms(
            self._handle, waveforms, auto_start, timeout
        )
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/stream_writers/_digital_single_channel_writer.py sha256=3a04fe35b0f6ca0d48935a0f251adb4d0c2340dcc35da2b1c0311ef8a400fee7 bytes=16790 -->
## FILE: src/handwritten/stream_writers/_digital_single_channel_writer.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/stream_writers/_digital_single_channel_writer.py`
- sha256: `3a04fe35b0f6ca0d48935a0f251adb4d0c2340dcc35da2b1c0311ef8a400fee7`
- bytes: 16790

````python
from __future__ import annotations

from typing import Any

import numpy
from nitypes.waveform import DigitalWaveform

from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, requires_feature
from nidaqmx.constants import FillMode
from nidaqmx.stream_writers._channel_writer_base import (
    AUTO_START_UNSET,
    ChannelWriterBase,
)


class DigitalSingleChannelWriter(ChannelWriterBase):
    """Writes samples to a single digital output channel in an NI-DAQmx task."""

    def write_many_sample_port_byte(self, data, timeout=10.0):
        """Writes one or more 8-bit unsigned integer samples to a single digital output channel in a task.

        Use this method for devices with up to 8 lines per port.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 1D NumPy array of 8-bit
                unsigned integer samples to write to the task. Each
                element of the array corresponds to a sample to write.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.

        Returns:
            int:

            Specifies the actual number of samples this method
            successfully wrote.
        """  # noqa: W505 - doc line too long (106 > 100 characters) (auto-generated noqa)
        self._verify_array(data, False, True)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_digital_u8(
            self._handle, data.shape[0], auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def write_many_sample_port_uint16(self, data, timeout=10.0):
        """Writes one or more 16-bit unsigned integer samples to a single digital output channel in a task.

        Use this method for devices with up to 16 lines per port.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 1D NumPy array of 16-bit
                unsigned integer samples to write to the task. Each
                element of the array corresponds to a sample to write.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.

        Returns:
            int:

            Specifies the actual number of samples this method
            successfully wrote.
        """  # noqa: W505 - doc line too long (107 > 100 characters) (auto-generated noqa)
        self._verify_array(data, False, True)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_digital_u16(
            self._handle, data.shape[0], auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def write_many_sample_port_uint32(self, data, timeout=10.0):
        """Writes one or more 32-bit unsigned integer samples to a single digital output channel in a task.

        Use this method for devices with up to 32 lines per port.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 1D NumPy array of 32-bit
                unsigned integer samples to write to the task. Each
                element of the array corresponds to a sample to write.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.

        Returns:
            int:

            Specifies the actual number of samples this method
            successfully wrote.
        """  # noqa: W505 - doc line too long (107 > 100 characters) (auto-generated noqa)
        self._verify_array(data, False, True)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_digital_u32(
            self._handle, data.shape[0], auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def write_one_sample_multi_line(self, data, timeout=10):
        """Writes a single boolean sample to a single digital output channel in a task.

        The channel can contain multiple digital lines.

        Args:
            data (numpy.ndarray): Contains a 1D NumPy array of boolean
                samples to write to the task. Each element of the array
                corresponds to a line in the channel.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.
        """
        self._verify_array_digital_lines(data, False, True)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else True

        return self._interpreter.write_digital_lines(
            self._handle, 1, auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def write_one_sample_one_line(self, data, timeout=10):
        """Writes a single boolean sample to a single digital output channel in a task.

        The channel can contain only one digital line.

        Args:
            data (int): Specifies the boolean sample to write to the
                task.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.
        """
        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else True

        numpy_array = numpy.asarray([data], dtype=bool)

        return self._interpreter.write_digital_lines(
            self._handle, 1, auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, numpy_array
        )

    def write_one_sample_port_byte(self, data, timeout=10):
        """Writes a single 8-bit unsigned integer sample to a single digital output channel in a task.

        Use this method for devices with up to 8 lines per port.

        Args:
            data (int): Specifies the 8-bit unsigned integer sample to
                write to the task.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.
        """  # noqa: W505 - doc line too long (102 > 100 characters) (auto-generated noqa)
        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else True

        numpy_array = numpy.asarray([data], dtype=numpy.uint8)

        return self._interpreter.write_digital_u8(
            self._handle, 1, auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, numpy_array
        )

    def write_one_sample_port_uint16(self, data, timeout=10):
        """Writes a single 16-bit unsigned integer sample to a single digital output channel in a task.

        Use this method for devices with up to 16 lines per port.

        Args:
            data (int): Specifies the 16-bit unsigned integer sample to
                write to the task.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.
        """  # noqa: W505 - doc line too long (103 > 100 characters) (auto-generated noqa)
        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else True

        numpy_array = numpy.asarray([data], dtype=numpy.uint16)

        return self._interpreter.write_digital_u16(
            self._handle, 1, auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, numpy_array
        )

    def write_one_sample_port_uint32(self, data, timeout=10):
        """Writes a single 32-bit unsigned integer sample to a single digital output channel in a task.

        Use this method for devices with up to 32 lines per port.

        Args:
            data (int): Specifies the 32-bit unsigned integer sample to
                write to the task.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.
        """  # noqa: W505 - doc line too long (103 > 100 characters) (auto-generated noqa)
        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else True

        return self._interpreter.write_digital_scalar_u32(self._handle, auto_start, timeout, data)

    @requires_feature(WAVEFORM_SUPPORT)
    def write_waveform(self, waveform: DigitalWaveform[Any], timeout: float = 10.0) -> int:
        """Writes a waveform to a single digital output channel in a task.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            waveform (DigitalWaveform[Any]): Specifies the
                waveform to write to the task.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.

        Returns:
            int: Specifies the actual number of samples this method
            successfully wrote.
        """
        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_digital_waveform(self._handle, waveform, auto_start, timeout)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/system/__init__.py sha256=396a76eed40818da0da21cc578add6628122ba2100cc7dbb2c4ee7757ee47542 bytes=532 -->
## FILE: src/handwritten/system/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/system/__init__.py`
- sha256: `396a76eed40818da0da21cc578add6628122ba2100cc7dbb2c4ee7757ee47542`
- bytes: 532

````python
"""NI-DAQmx system classes."""

from nidaqmx.system import storage
from nidaqmx.system.device import Device
from nidaqmx.system.physical_channel import PhysicalChannel
from nidaqmx.system.system import (
    AOPowerUpState,
    CDAQSyncConnection,
    DOPowerUpState,
    DOResistorPowerUpState,
    System,
)
from nidaqmx.system.watchdog import (
    AOExpirationState,
    COExpirationState,
    DOExpirationState,
    WatchdogTask,
)

__all__ = ["system", "device", "physical_channel", "storage", "watchdog"]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/system/_collections/__init__.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: src/handwritten/system/_collections/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/system/_collections/__init__.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/system/_collections/device_collection.py sha256=98d1c842ceb25ec20356db78dcf4545567602df20f25fe2987b0174640d85173 bytes=4071 -->
## FILE: src/handwritten/system/_collections/device_collection.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/system/_collections/device_collection.py`
- sha256: `98d1c842ceb25ec20356db78dcf4545567602df20f25fe2987b0174640d85173`
- bytes: 4071

````python
from collections.abc import Sequence

from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError
from nidaqmx.system.device import Device, _DeviceAlternateConstructor
from nidaqmx.utils import unflatten_channel_string


class DeviceCollection(Sequence):
    """Contains the collection of devices for a DAQmx system.

    This class defines methods that implements a container object.
    """

    def __init__(self, interpreter):
        """Do not construct this object directly; instead, call nidaqmx.system.System.local().devices."""  # noqa: W505 - doc line too long (105 > 100 characters) (auto-generated noqa)
        self._interpreter = interpreter

    def __contains__(  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        self, item
    ):
        device_names = self.device_names

        if isinstance(item, str):
            items = unflatten_channel_string(item)
            return all([i in device_names for i in items])
        elif isinstance(item, Device):
            return item.name in device_names
        return False

    def __eq__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        if isinstance(other, self.__class__):
            return True
        return False

    def __getitem__(self, index):
        """Indexes a subset of devices on this device collection.

        Args:
            index: The value of the index. The following index types are
                supported:
                - str: Name of the device. You also can specify a string
                    that contains a list or range of names to this input.
                    If you have a list of names, use the DAQmx Flatten
                    Channel String function to convert the list to a
                    string.
                - int: Index/position of the device in the collection.
                - slice: Range of the indexes/positions of devices in the
                    collection.

        Returns:
            List[nidaqmx.system.device.Device]:

            Indicates the subset of devices indexed.
        """
        if isinstance(index, int):
            return _DeviceAlternateConstructor(self.device_names[index], self._interpreter)
        elif isinstance(index, slice):
            return [
                _DeviceAlternateConstructor(name, self._interpreter)
                for name in self.device_names[index]
            ]
        elif isinstance(index, str):
            device_names = unflatten_channel_string(index)
            if len(device_names) == 1:
                return _DeviceAlternateConstructor(device_names[0], self._interpreter)
            return [_DeviceAlternateConstructor(name, self._interpreter) for name in device_names]
        else:
            raise DaqError(
                f'Invalid index type "{type(index)}" used to access collection.',
                DAQmxErrors.UNKNOWN,
            )

    def __iter__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        for device_name in self.device_names:
            yield _DeviceAlternateConstructor(device_name, self._interpreter)

    def __len__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return len(self.device_names)

    def __ne__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return not self.__eq__(other)

    def __reversed__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        device_names = self.device_names
        device_names.reverse()

        for device_name in device_names:
            yield _DeviceAlternateConstructor(device_name, self._interpreter)

    @property
    def device_names(self):
        """List[str]: Indicates the names of all devices on this device collection."""
        val = self._interpreter.get_system_info_attribute_string(0x193B)
        return unflatten_channel_string(val)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/system/_collections/persisted_channel_collection.py sha256=860e83deabdafb061bac84835c8fca7b1216a30af343ddc9c55741f79fad8eff bytes=4389 -->
## FILE: src/handwritten/system/_collections/persisted_channel_collection.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/system/_collections/persisted_channel_collection.py`
- sha256: `860e83deabdafb061bac84835c8fca7b1216a30af343ddc9c55741f79fad8eff`
- bytes: 4389

````python
from collections.abc import Sequence

from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError
from nidaqmx.system.storage.persisted_channel import (
    PersistedChannel,
    _PersistedChannelAlternateConstructor,
)
from nidaqmx.utils import unflatten_channel_string


class PersistedChannelCollection(Sequence):
    """Contains the collection of global channels for a DAQmx system.

    This class defines methods that implements a container object.
    """

    def __init__(self, interpreter):
        """Do not construct this object directly; instead, call nidaqmx.system.System.local().global_channels."""  # noqa: W505 - doc line too long (113 > 100 characters) (auto-generated noqa)
        self._interpreter = interpreter

    def __contains__(  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        self, item
    ):
        channel_names = self.global_channel_names

        if isinstance(item, str):
            items = unflatten_channel_string(item)
            return all([i in channel_names for i in items])
        elif isinstance(item, PersistedChannel):
            return item._name in channel_names

    def __eq__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        if isinstance(other, self.__class__):
            return True
        return False

    def __getitem__(self, index):
        """Indexes a subset of global channels on this global channel collection.

        Args:
            index: The value of the index. The following index types
                are supported:
                - str: Name of the global channel. You also can specify
                    a string that contains a list or range of names to
                    this input. If you have a list of names, use the
                    DAQmx Flatten Channel String function to convert
                    the list to a string.
                - int: Index/position of the global channel in the
                    collection.
                - slice: Range of the indexes/positions of global
                    channels in the collection.

        Returns:
            List[nidaqmx.system.storage.persisted_channel.PersistedChannel]:

            Indicates the of global channels indexed.
        """
        if isinstance(index, int):
            return _PersistedChannelAlternateConstructor(
                self.global_channel_names[index], self._interpreter
            )
        elif isinstance(index, slice):
            return [
                _PersistedChannelAlternateConstructor(name, self._interpreter)
                for name in self.global_channel_names[index]
            ]
        elif isinstance(index, str):
            names = unflatten_channel_string(index)
            if len(names) == 1:
                return _PersistedChannelAlternateConstructor(names[0], self._interpreter)
            return [
                _PersistedChannelAlternateConstructor(name, self._interpreter) for name in names
            ]
        else:
            raise DaqError(
                f'Invalid index type "{type(index)}" used to access collection.',
                DAQmxErrors.UNKNOWN,
            )

    def __iter__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        for channel_name in self.global_channel_names:
            yield _PersistedChannelAlternateConstructor(channel_name, self._interpreter)

    def __len__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return len(self.global_channel_names)

    def __ne__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return not self.__eq__(other)

    def __reversed__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        channel_names = self.global_channel_names
        channel_names.reverse()

        for channel_name in channel_names:
            yield _PersistedChannelAlternateConstructor(channel_name, self._interpreter)

    @property
    def global_channel_names(self):
        """List[str]: The names of all the global channels on this collection."""
        val = self._interpreter.get_system_info_attribute_string(0x1265)
        return unflatten_channel_string(val)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/system/_collections/persisted_scale_collection.py sha256=57d751e099f6d6f41ee451c7e5e63b6b2ed2be3cbcb2e5adff202a32de769c77 bytes=4194 -->
## FILE: src/handwritten/system/_collections/persisted_scale_collection.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/system/_collections/persisted_scale_collection.py`
- sha256: `57d751e099f6d6f41ee451c7e5e63b6b2ed2be3cbcb2e5adff202a32de769c77`
- bytes: 4194

````python
from collections.abc import Sequence

from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError
from nidaqmx.system.storage.persisted_scale import (
    PersistedScale,
    _PersistedScaleAlternateConstructor,
)
from nidaqmx.utils import unflatten_channel_string


class PersistedScaleCollection(Sequence):
    """Contains the collection of custom scales on a DAQmx system.

    This class defines methods that implements a container object.
    """

    def __init__(self, interpreter):
        """Do not construct this object directly; instead, call nidaqmx.system.System.local().scales."""  # noqa: W505 - doc line too long (104 > 100 characters) (auto-generated noqa)
        self._interpreter = interpreter

    def __contains__(  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        self, item
    ):
        scale_names = self.scale_names

        if isinstance(item, str):
            items = unflatten_channel_string(item)
            return all([i in scale_names for i in items])
        elif isinstance(item, PersistedScale):
            return item._name in scale_names

    def __eq__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        if isinstance(other, self.__class__):
            return True
        return False

    def __getitem__(self, index):
        """Indexes a subset of custom scales on this collection.

        Args:
            index: The value of the index. The following index types
                are supported:
                - str: Name of the custom scale. You also can specify
                    a string that contains a list or range of names to
                    this input. If you have a list of names, use the
                    DAQmx Flatten Channel String function to convert
                    the list to a string.
                - int: Index/position of the custom scale in the
                    collection.
                - slice: Range of the indexes/positions of custom scales
                    in the collection.

        Returns:
            List[nidaqmx.system.storage.persisted_scale.PersistedScale]:

            Indicates the subset of custom scales indexed.
        """
        if isinstance(index, int):
            return _PersistedScaleAlternateConstructor(self.scale_names[index], self._interpreter)
        elif isinstance(index, slice):
            return [
                _PersistedScaleAlternateConstructor(name, self._interpreter)
                for name in self.scale_names[index]
            ]
        elif isinstance(index, str):
            names = unflatten_channel_string(index)
            if len(names) == 1:
                return _PersistedScaleAlternateConstructor(names[0], self._interpreter)
            return [_PersistedScaleAlternateConstructor(name, self._interpreter) for name in names]
        else:
            raise DaqError(
                f'Invalid index type "{type(index)}" used to access collection.',
                DAQmxErrors.UNKNOWN,
            )

    def __iter__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        for scale_name in self.scale_names:
            yield _PersistedScaleAlternateConstructor(scale_name, self._interpreter)

    def __len__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return len(self.scale_names)

    def __ne__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return not self.__eq__(other)

    def __reversed__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        scale_names = self.scale_names
        scale_names.reverse()

        for scale_name in scale_names:
            yield _PersistedScaleAlternateConstructor(scale_name, self._interpreter)

    @property
    def scale_names(self):
        """List[str]: Indicates the names of all the custom scales on this collection."""
        val = self._interpreter.get_system_info_attribute_string(0x1266)
        return unflatten_channel_string(val)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/system/_collections/persisted_task_collection.py sha256=25ec625c8098c52aacf1967d0c92cd55d832a5c66ff02c9ea9f5bafbd6a3ded3 bytes=4142 -->
## FILE: src/handwritten/system/_collections/persisted_task_collection.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/system/_collections/persisted_task_collection.py`
- sha256: `25ec625c8098c52aacf1967d0c92cd55d832a5c66ff02c9ea9f5bafbd6a3ded3`
- bytes: 4142

````python
from collections.abc import Sequence

from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError
from nidaqmx.system.storage.persisted_task import (
    PersistedTask,
    _PersistedTaskAlternateConstructor,
)
from nidaqmx.utils import unflatten_channel_string


class PersistedTaskCollection(Sequence):
    """Contains the collection of task saved on a DAQmx system.

    This class defines methods that implements a container object.
    """

    def __init__(self, interpreter):
        """Do not construct this object directly; instead, call nidaqmx.system.System.local().tasks."""  # noqa: W505 - doc line too long (103 > 100 characters) (auto-generated noqa)
        self._interpreter = interpreter

    def __contains__(  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        self, item
    ):
        task_names = self.task_names

        if isinstance(item, str):
            items = unflatten_channel_string(item)
            return all([i in task_names for i in items])
        elif isinstance(item, PersistedTask):
            return item._name in task_names

    def __eq__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        if isinstance(other, self.__class__):
            return True
        return False

    def __getitem__(self, index):
        """Indexes a subset of saved tasks on this collection.

        Args:
            index: The value of the index. The following index types
                are supported:
                - str: Name of the saved task. You also can specify
                    a string that contains a list or range of names to
                    this input. If you have a list of names, use the
                    DAQmx Flatten Channel String function to convert
                    the list to a string.
                - int: Index/position of the saved task in the
                    collection.
                - slice: Range of the indexes/positions of saved tasks
                    in the collection.

        Returns:
            List[nidaqmx.system.storage.persisted_task.PersistedTask]:

            Indicates the subset of saved tasks indexed.
        """
        if isinstance(index, int):
            return _PersistedTaskAlternateConstructor(self.task_names[index], self._interpreter)
        elif isinstance(index, slice):
            return [
                _PersistedTaskAlternateConstructor(name, self._interpreter)
                for name in self.task_names[index]
            ]
        elif isinstance(index, str):
            names = unflatten_channel_string(index)
            if len(names) == 1:
                return _PersistedTaskAlternateConstructor(names[0], self._interpreter)
            return [_PersistedTaskAlternateConstructor(name, self._interpreter) for name in names]
        else:
            raise DaqError(
                f'Invalid index type "{type(index)}" used to access collection.',
                DAQmxErrors.UNKNOWN,
            )

    def __iter__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        for task_name in self.task_names:
            yield _PersistedTaskAlternateConstructor(task_name, self._interpreter)

    def __len__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return len(self.task_names)

    def __ne__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return not self.__eq__(other)

    def __reversed__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        task_names = self.task_names
        task_names.reverse()

        for task_name in task_names:
            yield _PersistedTaskAlternateConstructor(task_name, self._interpreter)

    @property
    def task_names(self):
        """List[str]: Indicates the names of all the tasks on this collection."""
        val = self._interpreter.get_system_info_attribute_string(0x1267)
        return unflatten_channel_string(val)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/system/_collections/physical_channel_collection.py sha256=9f47d2a543012efbb6f07f89504f7355ac418bdf364e71fccc3ba8936f9d7bee bytes=9413 -->
## FILE: src/handwritten/system/_collections/physical_channel_collection.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/system/_collections/physical_channel_collection.py`
- sha256: `9f47d2a543012efbb6f07f89504f7355ac418bdf364e71fccc3ba8936f9d7bee`
- bytes: 9413

````python
from collections.abc import Sequence

from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError
from nidaqmx.system.physical_channel import (
    PhysicalChannel,
    _PhysicalChannelAlternateConstructor,
)
from nidaqmx.utils import flatten_channel_string, unflatten_channel_string


class PhysicalChannelCollection(Sequence):
    """Contains the collection of physical channels for a DAQmx device.

    This class defines methods that implements a container object.
    """

    def __init__(self, device_name, interpreter):
        """Do not construct this object directly; instead, construct a nidaqmx.system.Device and use the appropriate property, such as device.ai_physical_channels."""  # noqa: W505 - doc line too long (166 > 100 characters) (auto-generated noqa)
        self._name = device_name
        self._interpreter = interpreter

    def __contains__(  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        self, item
    ):
        channel_names = self.channel_names

        if isinstance(item, str):
            items = unflatten_channel_string(item)
            return all([i in channel_names for i in items])
        elif isinstance(item, PhysicalChannel):
            return item._name in channel_names
        return False

    def __eq__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        if isinstance(other, self.__class__):
            return self._name == other._name
        return False

    def __getitem__(self, index):
        """Indexes a subset of physical channels on this physical channel collection.

        Args:
            index: The value of the index. The following index types
                are supported:
                - str: Name of the physical channel, without the
                    device name prefix, e.g. 'ai0'. You also can
                    specify a string that contains a list or range of
                    names to this input. If you have a list of names,
                    use the DAQmx Flatten Channel String function to
                    convert the list to a string.
                - int: Index/position of the physical channel in the
                    collection.
                - slice: Range of the indexes/positions of physical
                    channels in the collection.

        Returns:
            nidaqmx.system.physical_channel.PhysicalChannel:

            Indicates the subset of physical channels indexed.
        """
        if isinstance(index, int):
            return _PhysicalChannelAlternateConstructor(
                self.channel_names[index], self._interpreter
            )
        elif isinstance(index, slice):
            return [
                _PhysicalChannelAlternateConstructor(channel, self._interpreter)
                for channel in self.channel_names[index]
            ]
        elif isinstance(index, str):
            requested_channels = unflatten_channel_string(index)
            # Ensure the channel names are fully qualified. If the channel is invalid, the user will get errors from the  # noqa: W505 - doc line too long (120 > 100 characters) (auto-generated noqa)
            # channel objects on use.
            channels_to_use = []
            for channel in requested_channels:
                if channel.startswith(f"{self._name}/"):
                    channels_to_use.append(channel)
                else:
                    channels_to_use.append(f"{self._name}/{channel}")

            if len(channels_to_use) == 1:
                return _PhysicalChannelAlternateConstructor(channels_to_use[0], self._interpreter)
            return [
                _PhysicalChannelAlternateConstructor(channel, self._interpreter)
                for channel in channels_to_use
            ]
        else:
            raise DaqError(
                f'Invalid index type "{type(index)}" used to access collection.',
                DAQmxErrors.UNKNOWN,
            )

    def __iter__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        for channel_name in self.channel_names:
            yield _PhysicalChannelAlternateConstructor(channel_name, self._interpreter)

    def __len__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return len(self.channel_names)

    def __ne__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return not self.__eq__(other)

    def __reversed__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        channel_names = self.channel_names
        channel_names.reverse()

        for channel_name in channel_names:
            yield _PhysicalChannelAlternateConstructor(channel_name, self._interpreter)

    @property
    def all(self):
        """nidaqmx.system.physical_channel.PhysicalChannel: Specifies a physical channel object that represents the entire list of physical channels on this channel collection."""  # noqa: W505 - doc line too long (179 > 100 characters) (auto-generated noqa)
        return _PhysicalChannelAlternateConstructor(
            flatten_channel_string(self.channel_names), self._interpreter
        )

    @property
    def channel_names(self):
        """List[str]: Specifies the entire list of physical channels in this collection."""
        raise NotImplementedError()


class AIPhysicalChannelCollection(PhysicalChannelCollection):
    """Contains the collection of analog input physical channels for a DAQmx device.

    This class defines methods that implements a container object.
    """

    @property
    def channel_names(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ):
        val = self._interpreter.get_device_attribute_string(self._name, 0x231E)
        return unflatten_channel_string(val)


class AOPhysicalChannelCollection(PhysicalChannelCollection):
    """Contains the collection of analog output physical channels for a DAQmx device.

    This class defines methods that implements a container object.
    """

    @property
    def channel_names(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ):
        val = self._interpreter.get_device_attribute_string(self._name, 0x231F)
        return unflatten_channel_string(val)


class CIPhysicalChannelCollection(PhysicalChannelCollection):
    """Contains the collection of counter input physical channels for a DAQmx device.

    This class defines methods that implements a container object.
    """

    @property
    def channel_names(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ):
        val = self._interpreter.get_device_attribute_string(self._name, 0x2324)
        return unflatten_channel_string(val)


class COPhysicalChannelCollection(PhysicalChannelCollection):
    """Contains the collection of counter output physical channels for a DAQmx device.

    This class defines methods that implements a container object.
    """

    @property
    def channel_names(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ):
        val = self._interpreter.get_device_attribute_string(self._name, 0x2325)
        return unflatten_channel_string(val)


class DILinesCollection(PhysicalChannelCollection):
    """Contains the collection of digital input lines for a DAQmx device.

    This class defines methods that implements a container object.
    """

    @property
    def channel_names(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ):
        val = self._interpreter.get_device_attribute_string(self._name, 0x2320)
        return unflatten_channel_string(val)


class DOLinesCollection(PhysicalChannelCollection):
    """Contains the collection of digital output lines for a DAQmx device.

    This class defines methods that implements a container object.
    """

    @property
    def channel_names(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ):
        val = self._interpreter.get_device_attribute_string(self._name, 0x2322)
        return unflatten_channel_string(val)


class DIPortsCollection(PhysicalChannelCollection):
    """Contains the collection of digital input ports for a DAQmx device.

    This class defines methods that implements a container object.
    """

    @property
    def channel_names(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ):
        val = self._interpreter.get_device_attribute_string(self._name, 0x2321)
        return unflatten_channel_string(val)


class DOPortsCollection(PhysicalChannelCollection):
    """Contains the collection of digital output ports for a DAQmx device.

    This class defines methods that implements a container object.
    """

    @property
    def channel_names(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ):
        val = self._interpreter.get_device_attribute_string(self._name, 0x2323)
        return unflatten_channel_string(val)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/system/_watchdog_modules/__init__.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: src/handwritten/system/_watchdog_modules/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/system/_watchdog_modules/__init__.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/system/_watchdog_modules/expiration_states_collection.py sha256=26b284fa45c135c5074b72e930438d3f3d5cf4e12d5acfd8e324553388856dea bytes=1733 -->
## FILE: src/handwritten/system/_watchdog_modules/expiration_states_collection.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/system/_watchdog_modules/expiration_states_collection.py`
- sha256: `26b284fa45c135c5074b72e930438d3f3d5cf4e12d5acfd8e324553388856dea`
- bytes: 1733

````python
from nidaqmx.errors import DaqError
from nidaqmx.system._watchdog_modules.expiration_state import ExpirationState


class ExpirationStatesCollection:
    """Contains the collection of expiration states for a DAQmx Watchdog Task.

    This class defines methods that implements a container object.
    """

    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self, task_handle, interpreter
    ):
        self._handle = task_handle
        self._interpreter = interpreter

    def __eq__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        if isinstance(other, self.__class__):
            return self._handle == other._handle
        return False

    def __hash__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return self._interpreter.hash_task_handle(self._handle)

    def __ne__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return not self.__eq__(other)

    def __getitem__(self, index):
        """Indexes an expiration state on this collection.

        Args:
            index (str): Name of the physical channel of which the
                expiration state to retrieve.

        Returns:
            nidaqmx.system._watchdog_modules.expiration_state.ExpirationState:

            The object representing the indexed expiration state.
        """
        if isinstance(index, str):
            return ExpirationState(self._handle, index, self._interpreter)
        else:
            raise DaqError(
                f'Invalid index type "{type(index)}" used to access expiration states.', -1
            )
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/system/storage/__init__.py sha256=4a57e1d6bda99369e4dd13abf17295feaf531155f358366eb3ec02cd91990330 bytes=310 -->
## FILE: src/handwritten/system/storage/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/system/storage/__init__.py`
- sha256: `4a57e1d6bda99369e4dd13abf17295feaf531155f358366eb3ec02cd91990330`
- bytes: 310

````python
"""NI-DAQmx storage classes."""

from nidaqmx.system.storage.persisted_channel import PersistedChannel
from nidaqmx.system.storage.persisted_scale import PersistedScale
from nidaqmx.system.storage.persisted_task import PersistedTask

__all__ = ["persisted_channel", "persisted_scale", "persisted_task"]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/system/storage/persisted_channel.py sha256=87a58966b6c79ad866015bbe5cda83bec86d48483e4aa5525bfd6f59b1abeedf bytes=3576 -->
## FILE: src/handwritten/system/storage/persisted_channel.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/system/storage/persisted_channel.py`
- sha256: `87a58966b6c79ad866015bbe5cda83bec86d48483e4aa5525bfd6f59b1abeedf`
- bytes: 3576

````python
"""NI-DAQmx persisted channel classes."""

from nidaqmx import utils

__all__ = ["PersistedChannel"]


class PersistedChannel:
    """Represents a saved DAQmx global channel.

    Use the DAQmx Persisted Channel properties to query information about
    programmatically saved global channels.
    """

    __slots__ = ["_name", "_interpreter", "__weakref__"]

    def __init__(self, name, *, grpc_options=None):
        """Initialize a new PersistedChannel.

        Args:
            name (str): Specifies the name of the global channel.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        """
        self._name = name
        self._interpreter = utils._select_interpreter(grpc_options)

    def __eq__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        if isinstance(other, self.__class__):
            return self._name == other._name
        return False

    def __hash__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return hash(self._name)

    def __ne__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return not self.__eq__(other)

    def __repr__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return f"PersistedChannel(name={self._name})"

    @property
    def name(self):
        """str: Indicates the name of the global channel."""
        return self._name

    @property
    def author(self):
        """str: Indicates the author of the global channel."""
        val = self._interpreter.get_persisted_chan_attribute_string(self._name, 0x22D0)
        return val

    @property
    def allow_interactive_editing(self):
        """bool: Indicates whether the global channel can be edited in the DAQ Assistant."""
        val = self._interpreter.get_persisted_chan_attribute_bool(self._name, 0x22D1)
        return val

    @property
    def allow_interactive_deletion(self):
        """bool: Indicates whether the global channel can be deleted through MAX."""
        val = self._interpreter.get_persisted_chan_attribute_bool(self._name, 0x22D2)
        return val

    def delete(self):
        """Deletes this global channel from MAX.

        This function does not remove the global channel from tasks that
        use it.
        """
        self._interpreter.delete_saved_global_chan(self._name)


class _PersistedChannelAlternateConstructor(PersistedChannel):
    """Provide an alternate constructor for the PersistedChannel object.

    This is a private API used to instantiate a PersistedChannel with an existing interpreter.
    """

    # Setting __slots__ avoids TypeError: __class__ assignment: 'Base' object layout differs from 'Derived'.  # noqa: W505 - doc line too long (108 > 100 characters) (auto-generated noqa)
    __slots__ = ()

    def __init__(self, name, interpreter):
        """Initialize a new PersistedChannel with an existing interpreter.

        Args:
            name: Specifies the name of the PersistedChannel.
            interpreter: Specifies the interpreter instance.

        """
        self._name = name
        self._interpreter = interpreter

        # Use meta-programming to change the type of this object to PersistedChannel,
        # so the user isn't confused when doing introspection.
        self.__class__ = PersistedChannel  # type: ignore[assignment]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/system/storage/persisted_scale.py sha256=c740f7a5218ebe3abde5bd376c3819a4531a7816d115ee845fd858ec8fb1be58 bytes=3827 -->
## FILE: src/handwritten/system/storage/persisted_scale.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/system/storage/persisted_scale.py`
- sha256: `c740f7a5218ebe3abde5bd376c3819a4531a7816d115ee845fd858ec8fb1be58`
- bytes: 3827

````python
"""NI-DAQmx persisted scale classes."""

from nidaqmx import utils
from nidaqmx.scale import _ScaleAlternateConstructor

__all__ = ["PersistedScale"]


class PersistedScale:
    """Represents a saved DAQmx custom scale.

    Use the DAQmx Persisted Scale properties to query information about
    programmatically saved custom scales.
    """

    __slots__ = ["_name", "_interpreter", "__weakref__"]

    def __init__(self, name, *, grpc_options=None):
        """Initialize a new PersistedScale.

        Args:
            name (str): Specifies the name of the saved scale.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        """
        self._name = name
        self._interpreter = utils._select_interpreter(grpc_options)

    def __eq__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        if isinstance(other, self.__class__):
            return self._name == other._name
        return False

    def __hash__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return hash(self._name)

    def __ne__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return not self.__eq__(other)

    def __repr__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return f"PersistedScale(name={self._name})"

    @property
    def name(self):
        """str: Indicates the name of the custom scale."""
        return self._name

    @property
    def author(self):
        """str: Indicates the author of the custom scale."""
        val = self._interpreter.get_persisted_scale_attribute_string(self._name, 0x22D4)
        return val

    @property
    def allow_interactive_editing(self):
        """bool: Indicates whether the custom scale can be edited in the DAQ Assistant."""
        val = self._interpreter.get_persisted_scale_attribute_bool(self._name, 0x22D5)
        return val

    @property
    def allow_interactive_deletion(self):
        """bool: Indicates whether the custom scale can be deleted through MAX."""
        val = self._interpreter.get_persisted_scale_attribute_bool(self._name, 0x22D6)
        return val

    def delete(self):
        """Deletes this custom scale from MAX.

        This function does not remove the custom scale from virtual
        channels that use it.
        """
        self._interpreter.delete_saved_scale(self._name)

    def load(self):
        """Loads this custom scale.

        Returns:
            nidaqmx.scale.Scale: Indicates the loaded Scale object.
        """
        return _ScaleAlternateConstructor(self._name, self._interpreter)


class _PersistedScaleAlternateConstructor(PersistedScale):
    """Provide an alternate constructor for the PersistedScale object.

    This is a private API used to instantiate a PersistedScale with an existing interpreter.
    """

    # Setting __slots__ avoids TypeError: __class__ assignment: 'Base' object layout differs from 'Derived'.  # noqa: W505 - doc line too long (108 > 100 characters) (auto-generated noqa)
    __slots__ = ()

    def __init__(self, name, interpreter):
        """Initialize a new PersistedScale with an existing interpreter.

        Args:
            name: Specifies the name of the PersistedScale.
            interpreter: Specifies the interpreter instance.

        """
        self._name = name
        self._interpreter = interpreter

        # Use meta-programming to change the type of this object to PersistedScale,
        # so the user isn't confused when doing introspection.
        self.__class__ = PersistedScale  # type: ignore[assignment]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/system/storage/persisted_task.py sha256=f49e75ad977b2ef63b9e15145f10be4fdfe438c08ea077806dbf08548d16810d bytes=3949 -->
## FILE: src/handwritten/system/storage/persisted_task.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/system/storage/persisted_task.py`
- sha256: `f49e75ad977b2ef63b9e15145f10be4fdfe438c08ea077806dbf08548d16810d`
- bytes: 3949

````python
"""NI-DAQmx persisted task classes."""

from nidaqmx import task, utils

__all__ = ["PersistedTask"]


class PersistedTask:
    """Represents a saved DAQmx task.

    Use the DAQmx Persisted Task properties to query information about
    programmatically saved tasks.
    """

    __slots__ = ["_name", "_interpreter", "__weakref__"]

    def __init__(self, name, *, grpc_options=None):
        """Initialize a new PersistedTask.

        Args:
            name (str): Specifies the name of the saved task.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        """
        self._name = name
        self._interpreter = utils._select_interpreter(grpc_options)

    def __eq__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        if isinstance(other, self.__class__):
            return self._name == other._name
        return False

    def __hash__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return hash(self._name)

    def __ne__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return not self.__eq__(other)

    def __repr__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return f"PersistedTask(name={self._name})"

    @property
    def name(self):
        """str: Indicates the name of the task."""
        return self._name

    @property
    def author(self):
        """str: Indicates the author of the task."""
        val = self._interpreter.get_persisted_task_attribute_string(self._name, 0x22CC)
        return val

    @property
    def allow_interactive_editing(self):
        """bool: Indicates whether the task can be edited in the DAQ Assistant."""
        val = self._interpreter.get_persisted_task_attribute_bool(self._name, 0x22CD)
        return val

    @property
    def allow_interactive_deletion(self):
        """bool: Indicates whether the task can be deleted through MAX."""
        val = self._interpreter.get_persisted_task_attribute_bool(self._name, 0x22CE)
        return val

    def delete(self):
        """Deletes this task from MAX.

        This function does not clear the copy of the task stored in memory.
        Use the DAQmx Clear Task function to clear that copy of the task.
        """
        self._interpreter.delete_saved_task(self._name)

    def load(self):
        """Loads this saved task.

        If you use this function to load a task, you must use DAQmx Clear
        Task to destroy it.

        Returns:
            nidaqmx.task.Task: Indicates the loaded Task object.
        """
        task_handle, close_on_exit = self._interpreter.load_task(self._name)

        return task._TaskAlternateConstructor(task_handle, self._interpreter, close_on_exit)


class _PersistedTaskAlternateConstructor(PersistedTask):
    """Provide an alternate constructor for the PersistedTask object.

    This is a private API used to instantiate a PersistedTask with an existing interpreter.
    """

    # Setting __slots__ avoids TypeError: __class__ assignment: 'Base' object layout differs from 'Derived'.  # noqa: W505 - doc line too long (108 > 100 characters) (auto-generated noqa)
    __slots__ = ()

    def __init__(self, name, interpreter):
        """Initialize a new PersistedTask with an existing interpreter.

        Args:
            name: Specifies the name of the PersistedTask.
            interpreter: Specifies the interpreter instance.

        """
        self._name = name
        self._interpreter = interpreter

        # Use meta-programming to change the type of this object to Scale,
        # so the user isn't confused when doing introspection.
        self.__class__ = PersistedTask  # type: ignore[assignment]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/task/__init__.py sha256=64998c8bc1b3d0e5f0134b1346a9195bd5917dec8ff158a3772eb8d63d4758a2 bytes=418 -->
## FILE: src/handwritten/task/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/task/__init__.py`
- sha256: `64998c8bc1b3d0e5f0134b1346a9195bd5917dec8ff158a3772eb8d63d4758a2`
- bytes: 418

````python
"""NI-DAQmx task and related classes."""

from nidaqmx.task._export_signals import ExportSignals
from nidaqmx.task._in_stream import InStream
from nidaqmx.task._out_stream import OutStream
from nidaqmx.task._task import Task, _TaskAlternateConstructor, _TaskEventType
from nidaqmx.task._timing import Timing

__all__ = [
    "Task",
    "InStream",
    "OutStream",
    "ExportSignals",
    "Timing",
]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/task/_task.py sha256=9e213a5b22cc18135d1e0c4bb22badd72ff9d2e0867570f0386957b9dbbd6dc4 bytes=78927 -->
## FILE: src/handwritten/task/_task.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/task/_task.py`
- sha256: `9e213a5b22cc18135d1e0c4bb22badd72ff9d2e0867570f0386957b9dbbd6dc4`
- bytes: 78927

````python
from __future__ import annotations

import threading
import warnings
from collections.abc import Iterable, Sequence
from enum import Enum
from typing import Any, NoReturn

import numpy
from nitypes.waveform import AnalogWaveform, DigitalWaveform

from nidaqmx import utils
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, requires_feature
from nidaqmx.constants import (
    READ_ALL_AVAILABLE,
    AcquisitionType,
    ChannelType,
    EveryNSamplesEventType,
    FillMode,
    ShuntCalSelect,
    ShuntCalSource,
    ShuntElementLocation,
    UsageTypeAI,
    UsageTypeCI,
    UsageTypeCO,
    _Save,
)
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError, DaqResourceWarning
from nidaqmx.system.device import _DeviceAlternateConstructor
from nidaqmx.task._export_signals import ExportSignals
from nidaqmx.task._in_stream import InStream
from nidaqmx.task._out_stream import OutStream
from nidaqmx.task._timing import Timing
from nidaqmx.task.channels._channel import Channel
from nidaqmx.task.collections._ai_channel_collection import AIChannelCollection
from nidaqmx.task.collections._ao_channel_collection import AOChannelCollection
from nidaqmx.task.collections._ci_channel_collection import CIChannelCollection
from nidaqmx.task.collections._co_channel_collection import COChannelCollection
from nidaqmx.task.collections._di_channel_collection import DIChannelCollection
from nidaqmx.task.collections._do_channel_collection import DOChannelCollection
from nidaqmx.task.triggering._triggers import Triggers
from nidaqmx.types import CtrFreq, CtrTick, CtrTime, PowerMeasurement
from nidaqmx.utils import flatten_channel_string, unflatten_channel_string

__all__ = ["Task"]


class UnsetNumSamplesSentinel:
    pass


class UnsetAutoStartSentinel:
    pass


NUM_SAMPLES_UNSET = UnsetNumSamplesSentinel()
AUTO_START_UNSET = UnsetAutoStartSentinel()

del UnsetNumSamplesSentinel
del UnsetAutoStartSentinel


class Task:
    """Represents a DAQmx Task."""

    __slots__ = (
        "_handle",
        "_close_on_exit",
        "_saved_name",
        "_grpc_options",
        "_event_handlers",
        "_interpreter",
        "_ai_channels",
        "_ao_channels",
        "_ci_channels",
        "_co_channels",
        "_di_channels",
        "_do_channels",
        "_export_signals",
        "_in_stream",
        "_timing",
        "_triggers",
        "_out_stream",
        "_event_handler_lock",
        "__weakref__",
    )

    def __init__(self, new_task_name="", *, grpc_options=None):
        """Creates a DAQmx task.

        Args:
            new_task_name (Optional[str]): Specifies the name to assign to
                the task.

                If you use this method in a loop and specify a name for the
                task, you must use the DAQmx Clear Task method within the loop
                after you are finished with the task. Otherwise, NI-DAQmx
                attempts to create multiple tasks with the same name, which
                results in an error.

            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        """
        # Initialize the fields that __del__ accesses so it doesn't crash when __init__ raises an exception.  # noqa: W505 - doc line too long (108 > 100 characters) (auto-generated noqa)
        self._handle = None
        self._close_on_exit = False
        self._saved_name = new_task_name  # _initialize sets this to the name assigned by DAQmx.
        self._grpc_options = grpc_options
        self._event_handlers = {}

        if grpc_options and not (
            grpc_options.session_name == "" or grpc_options.session_name == new_task_name
        ):
            raise DaqError(
                f'Unsupported session name: "{grpc_options.session_name}". If a session name is specified, it must match the task name.',
                DAQmxErrors.UNKNOWN,
                task_name=new_task_name,
            )

        self._interpreter = utils._select_interpreter(grpc_options)
        self._handle, self._close_on_exit = self._interpreter.create_task(new_task_name)

        self._initialize(self._handle, self._interpreter)

    def __del__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        if self._handle is not None and self._close_on_exit and self._grpc_options is None:
            warnings.warn(
                'Task of name "{}" was not explicitly closed before it was '
                "destructed. Resources on the task device may still be "
                "reserved.".format(self._saved_name),
                DaqResourceWarning,
            )
        elif self._grpc_options is not None and self._event_handlers:
            warnings.warn(
                'Task of name "{}" was not explicitly closed before it was '
                "destructed. Event handlers may still be active.".format(self._saved_name),
                DaqResourceWarning,
            )

    def __enter__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return self

    def __eq__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        if isinstance(other, self.__class__):
            return self._handle == other._handle
        return False

    def __exit__(  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        self, type, value, traceback
    ):
        if self._close_on_exit:
            self.close()

    def __hash__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return self._interpreter.hash_task_handle(self._handle)

    def __ne__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return not self.__eq__(other)

    def __repr__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return f"Task(name={self._saved_name})"

    @property
    def name(self):
        """str: Indicates the name of the task."""
        val = self._interpreter.get_task_attribute_string(self._handle, 0x1276)
        return val

    @property
    def channels(self):
        """:class:`nidaqmx.task.channels.Channel`: Specifies a channel object that represents the entire list of virtual channels in this task."""  # noqa: W505 - doc line too long (146 > 100 characters) (auto-generated noqa)
        return Channel._factory(
            self._handle, flatten_channel_string(self.channel_names), self._interpreter
        )

    @property
    def channel_names(self):
        """List[str]: Indicates the names of all virtual channels in the task."""
        val = self._interpreter.get_task_attribute_string(self._handle, 0x1273)
        return unflatten_channel_string(val)

    @property
    def number_of_channels(self):
        """int: Indicates the number of virtual channels in the task."""
        val = self._interpreter.get_task_attribute_uint32(self._handle, 0x2181)
        return val

    @property
    def devices(self):
        """List[:class:`nidaqmx.system.device.Device`]: Indicates a list of Device objects representing all the devices in the task."""  # noqa: W505 - doc line too long (135 > 100 characters) (auto-generated noqa)
        val = self._interpreter.get_task_attribute_string(self._handle, 0x230E)
        return [
            _DeviceAlternateConstructor(v, self._interpreter) for v in unflatten_channel_string(val)
        ]

    @property
    def number_of_devices(self):
        """int: Indicates the number of devices in the task."""
        val = self._interpreter.get_task_attribute_uint32(self._handle, 0x29BA)
        return val

    @property
    def ai_channels(self) -> AIChannelCollection:
        """Gets the collection of analog input channels for this task."""
        return self._ai_channels

    @property
    def ao_channels(self) -> AOChannelCollection:
        """Gets the collection of analog output channels for this task."""
        return self._ao_channels

    @property
    def ci_channels(self) -> CIChannelCollection:
        """Gets the collection of counter input channels for this task."""
        return self._ci_channels

    @property
    def co_channels(self) -> COChannelCollection:
        """Gets the collection of counter output channels for this task."""
        return self._co_channels

    @property
    def di_channels(self) -> DIChannelCollection:
        """Gets the collection of digital input channels for this task."""
        return self._di_channels

    @property
    def do_channels(self) -> DOChannelCollection:
        """Gets the collection of digital output channels for this task."""
        return self._do_channels

    @property
    def export_signals(self) -> ExportSignals:
        """Gets the exported signal configurations for the task."""
        return self._export_signals

    @property
    def in_stream(self) -> InStream:
        """Gets the read configurations for the task."""
        return self._in_stream

    @property
    def out_stream(self) -> OutStream:
        """Gets the write configurations for the task."""
        return self._out_stream

    @property
    def timing(self) -> Timing:
        """Gets the timing configurations for the task."""
        return self._timing

    @property
    def triggers(self) -> Triggers:
        """Gets the trigger configurations for the task."""
        return self._triggers

    def _initialize(self, task_handle, interpreter):
        """Instantiates and populates various attributes used by this task.

        Args:
            task_handle (TaskHandle): Specifies the handle for this task.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        # Saved name is used in self.close() to throw graceful error on
        # double closes.
        self._saved_name = self.name

        self._ai_channels = AIChannelCollection(task_handle, interpreter)
        self._ao_channels = AOChannelCollection(task_handle, interpreter)
        self._ci_channels = CIChannelCollection(task_handle, interpreter)
        self._co_channels = COChannelCollection(task_handle, interpreter)
        self._di_channels = DIChannelCollection(task_handle, interpreter)
        self._do_channels = DOChannelCollection(task_handle, interpreter)
        self._export_signals = ExportSignals(task_handle, interpreter)
        self._in_stream = InStream(self, interpreter)
        self._timing = Timing(task_handle, interpreter)
        self._triggers = Triggers(task_handle, interpreter)
        self._out_stream = OutStream(self, interpreter)

        self._event_handler_lock = threading.Lock()

    def _calculate_num_samps_per_chan(self, num_samps_per_chan):
        """Calculates the actual number of samples per channel to read.

        This method is necessary because the number of samples per channel
        can be set to NUM_SAMPLES_UNSET or -1, where each value entails a
        different method of calculating the actual number of samples per
        channel to read.

        Args:
            num_samps_per_chan (int): Specifies the number of samples per
                channel.
        """
        if num_samps_per_chan is NUM_SAMPLES_UNSET:
            return 1
        elif num_samps_per_chan == READ_ALL_AVAILABLE:
            if self._interpreter.driver_version >= (24, 5):
                # DAQmx_DefaultNumberOfSamplesToRead is 0x31E8
                return self._interpreter.get_read_attribute_uint32(self._handle, 0x31E8)
            else:
                acq_type = self.timing.samp_quant_samp_mode

                if acq_type == AcquisitionType.FINITE and not self.in_stream.read_all_avail_samp:
                    return self.timing.samp_quant_samp_per_chan
                else:
                    return self.in_stream.avail_samp_per_chan
        else:
            return num_samps_per_chan

    def add_global_channels(self, global_channels):
        """Adds global virtual channels from MAX to the given task.

        Args:
            global_channels (List[nidaqmx.system.storage.persisted_channel.PersistedChannel]):
                Specifies the channels to add to the task.

                These channels must be valid channels available from MAX.
                If you pass an invalid channel, NI-DAQmx returns an error.
                This value is ignored if it is empty.
        """
        channels = flatten_channel_string([g._name for g in global_channels])

        self._interpreter.add_global_chans_to_task(self._handle, channels)

    def close(self):
        """Clears the task.

        Before clearing, this method aborts the task, if necessary,
        and releases any resources the task reserved. You cannot use a task
        after you clear it unless you recreate the task.

        If you create a DAQmx Task object within a loop, use this method
        within the loop after you are finished with the task to avoid
        allocating unnecessary memory.
        """
        if self._handle is None:
            warnings.warn(
                'Attempted to close NI-DAQmx task of name "{}" but task was '
                "already closed.".format(self._saved_name),
                DaqResourceWarning,
            )
            return

        first_exception = None
        try:
            self._interpreter.clear_task(self._handle)
        except Exception as ex:
            first_exception = first_exception or ex
        self._handle = None

        with self._event_handler_lock:
            event_handlers = self._event_handlers
            self._event_handlers = {}

        for event_handler in event_handlers.values():
            try:
                event_handler.close()
            except Exception as ex:
                first_exception = first_exception or ex

        if first_exception:
            raise first_exception

    def control(self, action):
        """Alters the state of a task according to the action you specify.

        Args:
            action (nidaqmx.constants.TaskMode): Specifies how to alter
                the task state.
        """
        self._interpreter.task_control(self._handle, action.value)

    def is_task_done(self):
        """Queries the status of the task and indicates if it completed execution.

        Use this function to ensure that the specified
        operation is complete before you stop the task.

        Returns:
            bool:

            Indicates if the measurement or generation completed.
        """
        is_task_done = self._interpreter.is_task_done(self._handle)

        return is_task_done

    def perform_bridge_offset_nulling_cal(self, channel="", skip_unsupported_channels=False):
        """Perform a bridge offset nulling calibration on the channels in the task.

        If the task measures both bridge-based sensors and non-bridge-based sensors,
        use the channels input to specify the names of the channels that measure
        bridge-based sensors.

        Args:
            channel: is a subset of virtual channels in the task that you want to calibrate.
                Use this input if you do not want to calibrate all the channels in the task or
                if some channels in the task have open thermocouple detection disabled.
                If the input is empty, this VI attempts to calibrate all virtual channels in the task.

            skip_unsupported_channels: specifies whether or not to skip channels that do not
                support calibration.
                If skip unsupported channels is TRUE, this VI calibrates only supported channels.
                If FALSE, this VI calibrates the channels specified by channels. The default is FALSE.
        """  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (102 > 100 characters) (auto-generated noqa)

        self._interpreter.perform_bridge_offset_nulling_cal_ex(
            self._handle, channel, skip_unsupported_channels
        )

    def perform_strain_shunt_cal(
        self,
        channel="",
        shunt_resistor_value=100000,
        shunt_resistor_location=ShuntElementLocation.R3,
        shunt_resistor_select=ShuntCalSelect.A,
        shunt_resistor_source=ShuntCalSource.DEFAULT,
        skip_unsupported_channels=False,
    ):
        """Perform shunt calibration for the specified channels using a strain gage sensor.

        Refer to the calibration procedure for your module for detailed
        calibration instructions.

        Args:
            channel: Specifies a subset of virtual channels in the task that you
                want to calibrate. Use this input if you do not want to calibrate
                all the channels in the task or if some channels in the task measure
                non-bridge-based sensors. If the input is empty, this method attempts
                to calibrate all virtual channels in the task.
            shunt_resistor_value: Specifies the shunt resistance in ohms.
            shunt_resistor_location: Specifies the location of the shunt resistor.
            shunt_resistor_select: Specifies which shunt calibration switch to enable.
            shunt_resistor_source: Specifies which shunt to use.
            skip_unsupported_channels: Specifies whether or not to skip channels that
                do not support calibration. If skip_unsupported_channels is True, this
                method calibrates only supported channels. If False, this method calibrates
                the channels specified by channels. The default is False.
        """
        self._interpreter.perform_strain_shunt_cal_ex(
            self._handle,
            channel,
            shunt_resistor_value,
            shunt_resistor_location.value,
            shunt_resistor_select.value,
            shunt_resistor_source.value,
            skip_unsupported_channels,
        )

    def perform_bridge_shunt_cal(
        self,
        channel="",
        shunt_resistor_value=100000,
        shunt_resistor_location=ShuntElementLocation.R3,
        shunt_resistor_select=ShuntCalSelect.A,
        shunt_resistor_source=ShuntCalSource.DEFAULT,
        bridge_resistance=120,
        skip_unsupported_channels=False,
    ):
        """Perform shunt calibration for the specified channels using a bridge sensor.

        Refer to the calibration procedure for your module for detailed
        calibration instructions.

        Args:
            channel: Specifies a subset of virtual channels in the task that you
                want to calibrate. Use this input if you do not want to calibrate
                all the channels in the task or if some channels in the task measure
                non-bridge-based sensors. If the input is empty, this method attempts
                to calibrate all virtual channels in the task.
            shunt_resistor_value: Specifies the shunt resistance in ohms.
            shunt_resistor_location: Specifies the location of the shunt resistor.
            shunt_resistor_select: Specifies which shunt calibration switch to enable.
            shunt_resistor_source: Specifies which shunt to use.
            bridge_resistance: Specifies the bridge resistance in ohms. A value of -1
                means to use the nominal bridge resistance specified when you created
                the virtual channel.
            skip_unsupported_channels: Specifies whether or not to skip channels that
                do not support calibration. If skip_unsupported_channels is True, this
                method calibrates only supported channels. If False, this method calibrates
                the channels specified by channels. The default is False.
        """
        self._interpreter.perform_bridge_shunt_cal_ex(
            self._handle,
            channel,
            shunt_resistor_value,
            shunt_resistor_location.value,
            shunt_resistor_select.value,
            shunt_resistor_source.value,
            bridge_resistance,
            skip_unsupported_channels,
        )

    def perform_thrmcpl_lead_offset_nulling_cal(self, channel="", skip_unsupported_channels=False):
        """Perform thermocouple lead offset nulling calibration on the channels in the task.

        This is to compensate for offsets introduced by open thermocouple detection.
        Keep the measured temperature as constant as possible while performing this
        adjustment.

        Args:
            channel: is a subset of virtual channels in the task that you want to calibrate.
                Use this input if you do not want to calibrate all the channels in the task or
                if some channels in the task have open thermocouple detection disabled.
                If the input is empty, this VI attempts to calibrate all virtual channels in the task.

            skip_unsupported_channels: specifies whether or not to skip channels that do not
                support calibration.
                If skip unsupported channels is TRUE, this VI calibrates only supported channels.
                If FALSE, this VI calibrates the channels specified by channels. The default is FALSE.
        """  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (102 > 100 characters) (auto-generated noqa)

        self._interpreter.perform_thrmcpl_lead_offset_nulling_cal(
            self._handle, channel, skip_unsupported_channels
        )

    def read(self, number_of_samples_per_channel=NUM_SAMPLES_UNSET, timeout=10.0):
        """Reads samples from the task or virtual channels you specify.

        This read method is dynamic, and is capable of inferring an appropriate
        return type based on these factors:

        - The channel type of the task.
        - The number of channels to read.
        - The number of samples per channel.

        The data type of the samples returned is independently determined by
        the channel type of the task.

        For digital input measurements, the data type of the samples returned
        is determined by the line grouping format of the digital lines.
        If the line grouping format is set to "one channel for all lines", the
        data type of the samples returned is int. If the line grouping
        format is set to "one channel per line", the data type of the samples
        returned is boolean.

        If you do not set the number of samples per channel, this method
        assumes one sample was requested. This method then returns either a
        scalar (1 channel to read) or a list (N channels to read).

        If you set the number of samples per channel to ANY value (even 1),
        this method assumes multiple samples were requested. This method then
        returns either a list (1 channel to read) or a list of lists (N
        channels to read).

        Args:
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read. If this input is not set,
                assumes samples to read is 1. Conversely, if this input
                is set, assumes there are multiple samples to read.

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
            dynamic:

            The samples requested in the form of a scalar, a list, or a
            list of lists. See method docstring for more info.

            NI-DAQmx scales the data to the units of the measurement,
            including any custom scaling you apply to the channels. Use a
            DAQmx Create Channel method to specify these units.

        Example:
            >>> task = Task()
            >>> task.ai_channels.add_ai_voltage_chan('Dev1/ai0:3')
            >>> data = task.read()
            >>> type(data)
            <type 'list'>
            >>> type(data[0])
            <type 'float'>
        """
        channels_to_read = self.in_stream.channels_to_read
        number_of_channels = len(channels_to_read.channel_names)
        read_chan_type = channels_to_read.chan_type

        num_samples_not_set = number_of_samples_per_channel is NUM_SAMPLES_UNSET

        number_of_samples_per_channel = self._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        # Determine the array shape and size to create
        if number_of_channels > 1:
            if not num_samples_not_set:
                array_shape: tuple[int, ...] = (number_of_channels, number_of_samples_per_channel)
            else:
                array_shape = (number_of_channels,)
        else:
            array_shape = (number_of_samples_per_channel,)

        if read_chan_type == ChannelType.ANALOG_INPUT:
            if any(chan.ai_meas_type == UsageTypeAI.POWER for chan in channels_to_read):
                return self._read_power(
                    array_shape, number_of_channels, number_of_samples_per_channel, timeout
                )
            else:
                data: numpy.typing.NDArray = numpy.zeros(array_shape, dtype=numpy.float64)
                _, samples_read = self._interpreter.read_analog_f64(
                    self._handle,
                    number_of_samples_per_channel,
                    timeout,
                    FillMode.GROUP_BY_CHANNEL.value,
                    data,
                )

        elif (
            read_chan_type == ChannelType.DIGITAL_INPUT
            or read_chan_type == ChannelType.DIGITAL_OUTPUT
        ):
            if self.in_stream.di_num_booleans_per_chan == 1:
                data = numpy.zeros(array_shape, dtype=bool)
                _, samples_read, _ = self._interpreter.read_digital_lines(
                    self._handle,
                    number_of_samples_per_channel,
                    timeout,
                    FillMode.GROUP_BY_CHANNEL.value,
                    data,
                )
            else:
                data = numpy.zeros(array_shape, dtype=numpy.uint32)
                _, samples_read = self._interpreter.read_digital_u32(
                    self._handle,
                    number_of_samples_per_channel,
                    timeout,
                    FillMode.GROUP_BY_CHANNEL.value,
                    data,
                )

        elif read_chan_type == ChannelType.COUNTER_INPUT:
            meas_type = channels_to_read.ci_meas_type

            if meas_type in [
                UsageTypeCI.PULSE_FREQ,
                UsageTypeCI.PULSE_TIME,
                UsageTypeCI.PULSE_TICKS,
            ]:
                return self._read_ctr_pulse(
                    array_shape,
                    meas_type,
                    number_of_channels,
                    number_of_samples_per_channel,
                    num_samples_not_set,
                    timeout,
                )

            else:
                data = numpy.zeros(array_shape, dtype=numpy.float64)

                _, samples_read = self._interpreter.read_counter_f64_ex(
                    self._handle,
                    number_of_samples_per_channel,
                    timeout,
                    FillMode.GROUP_BY_CHANNEL.value,
                    data,
                )
        else:
            raise DaqError(
                "Read failed, because there are no channels in this task from "
                "which data can be read.",
                DAQmxErrors.READ_NO_INPUT_CHANS_IN_TASK,
                task_name=self.name,
            )

        if num_samples_not_set and array_shape == (1,):
            return data.tolist()[0]

        if samples_read != number_of_samples_per_channel:
            if number_of_channels > 1:
                return data[:, :samples_read].tolist()
            else:
                return data[:samples_read].tolist()

        return data.tolist()

    def _read_ctr_pulse(
        self,
        array_shape: tuple[int, ...],
        meas_type: UsageTypeCI,
        number_of_channels: int,
        number_of_samples_per_channel: int,
        num_samples_not_set: bool,
        timeout: float,
    ) -> CtrFreq | CtrTick | CtrTime | list[CtrFreq] | list[CtrTick] | list[CtrTime]:
        if meas_type == UsageTypeCI.PULSE_FREQ:
            frequencies = numpy.zeros(array_shape, dtype=numpy.float64)
            duty_cycles = numpy.zeros(array_shape, dtype=numpy.float64)

            _, _, samples_read = self._interpreter.read_ctr_freq(
                self._handle,
                number_of_samples_per_channel,
                timeout,
                FillMode.GROUP_BY_CHANNEL.value,
                frequencies,
                duty_cycles,
            )

            data: list[CtrFreq] | list[CtrTick] | list[CtrTime] = [
                CtrFreq(freq=f, duty_cycle=d) for f, d in zip(frequencies, duty_cycles)
            ]

        elif meas_type == UsageTypeCI.PULSE_TIME:
            high_times = numpy.zeros(array_shape, dtype=numpy.float64)
            low_times = numpy.zeros(array_shape, dtype=numpy.float64)

            _, _, samples_read = self._interpreter.read_ctr_time(
                self._handle,
                number_of_samples_per_channel,
                timeout,
                FillMode.GROUP_BY_CHANNEL.value,
                high_times,
                low_times,
            )
            data = [CtrTime(high_time=h, low_time=l) for h, l in zip(high_times, low_times)]

        elif meas_type == UsageTypeCI.PULSE_TICKS:
            high_ticks = numpy.zeros(array_shape, dtype=numpy.uint32)
            low_ticks = numpy.zeros(array_shape, dtype=numpy.uint32)

            _, _, samples_read = self._interpreter.read_ctr_ticks(
                self._handle,
                number_of_samples_per_channel,
                timeout,
                FillMode.GROUP_BY_CHANNEL.value,
                high_ticks,
                low_ticks,
            )
            data = [CtrTick(high_tick=h, low_tick=l) for h, l in zip(high_ticks, low_ticks)]

        else:
            assert False, f"{meas_type} is not a counter pulse measurement type."

        if num_samples_not_set and array_shape == (1,):
            return data[0]

        # Counter pulse measurements should not have N channel versions.
        #
        # https://github.com/ni/nidaqmx-python/issues/498 - Missing support for
        # multi-channel counter reads in stream_readers and task
        if samples_read != number_of_samples_per_channel:
            assert number_of_channels == 1
            return data[:samples_read]

        return data

    def _read_power(
        self,
        array_shape: tuple[int, ...],
        number_of_channels: int,
        number_of_samples_per_channel: int,
        timeout: float,
    ) -> PowerMeasurement | list[PowerMeasurement] | list[list[PowerMeasurement]]:
        voltages = numpy.zeros(array_shape, dtype=numpy.float64)
        currents = numpy.zeros(array_shape, dtype=numpy.float64)

        _, _, samples_read = self._interpreter.read_power_f64(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            voltages,
            currents,
        )

        if number_of_channels > 1:
            if number_of_samples_per_channel == 1:
                # n channel, 1 sample
                return [PowerMeasurement(voltage=v, current=i) for v, i in zip(voltages, currents)]
            else:
                # n channel, n samples
                return [
                    [
                        PowerMeasurement(voltage=v, current=i)
                        for v, i in zip(voltages[channel_index], currents[channel_index])
                    ]
                    for channel_index in range(number_of_channels)
                ]
        else:
            if number_of_samples_per_channel == 1:
                # 1 channel, 1 sample
                return PowerMeasurement(voltage=voltages[0], current=currents[0])
            else:
                # 1 channel, n samples
                return [PowerMeasurement(voltage=v, current=i) for v, i in zip(voltages, currents)][
                    :samples_read
                ]

    @requires_feature(WAVEFORM_SUPPORT)
    def read_waveform(self, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0):
        """Reads samples from the task or virtual channels you specify, and returns them as waveforms.

        This read method is dynamic, and is capable of inferring an appropriate
        return type based on these factors:

        - The channel type of the task.
        - The number of channels to read.
        - The number of samples per channel.

        The data type of the samples returned is independently determined by
        the channel type of the task.

        If you do not set the number of samples per channel, this method
        reads all available data for each channel.

        Args:
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read. If this input is not set,
                it defaults to nidaqmx.constants.READ_ALL_AVAILABLE.

                If this input is nidaqmx.constants.READ_ALL_AVAILABLE,
                NI-DAQmx determines how many samples
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
            dynamic:

            The samples requested in the form of a waveform (for a single channel)
            or a list of waveforms (for multiple channels).
            See method docstring for more info.

            NI-DAQmx scales the data to the units of the measurement,
            including any custom scaling you apply to the channels. Use a
            DAQmx Create Channel method to specify these units.

        Example:
            >>> task = Task()
            >>> task.ai_channels.add_ai_voltage_chan('Dev1/ai0')
            >>> data = task.read_waveform()
            >>> type(data)
            <type 'AnalogWaveform'>
        """  # noqa: W505 - doc line too long (102 > 100 characters) (auto-generated noqa)
        channels_to_read = self.in_stream.channels_to_read
        number_of_channels = len(channels_to_read.channel_names)
        read_chan_type = channels_to_read.chan_type

        number_of_samples_per_channel = self._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        if read_chan_type == ChannelType.ANALOG_INPUT:
            if number_of_channels == 1:
                analog_waveform = AnalogWaveform(number_of_samples_per_channel)
                self._interpreter.read_analog_waveform(
                    self._handle,
                    number_of_samples_per_channel,
                    timeout,
                    analog_waveform,
                    self._in_stream.waveform_attribute_mode,
                )
                return analog_waveform
            else:
                analog_waveforms = [
                    AnalogWaveform(number_of_samples_per_channel) for _ in range(number_of_channels)
                ]
                self._interpreter.read_analog_waveforms(
                    self._handle,
                    number_of_samples_per_channel,
                    timeout,
                    analog_waveforms,
                    self._in_stream.waveform_attribute_mode,
                )
                return analog_waveforms

        elif (
            read_chan_type == ChannelType.DIGITAL_INPUT
            or read_chan_type == ChannelType.DIGITAL_OUTPUT
        ):
            if number_of_channels == 1:
                digital_waveform = DigitalWaveform(
                    number_of_samples_per_channel, self.in_stream.di_num_booleans_per_chan
                )
                self._interpreter.read_digital_waveform(
                    self._handle,
                    number_of_samples_per_channel,
                    timeout,
                    digital_waveform,
                    self._in_stream.waveform_attribute_mode,
                )
                return digital_waveform
            else:
                return self._interpreter.read_new_digital_waveforms(
                    self._handle,
                    number_of_channels,
                    number_of_samples_per_channel,
                    self.in_stream.di_num_booleans_per_chan,
                    timeout,
                    self._in_stream.waveform_attribute_mode,
                )

        else:
            raise DaqError(
                "Read failed, because there are no channels in this task from "
                "which data can be read.",
                DAQmxErrors.READ_NO_INPUT_CHANS_IN_TASK,
                task_name=self.name,
            )

    def register_done_event(self, callback_method):
        """Registers a callback function to receive an event when a task stops due to an error or when a finite acquisition task or finite generation task completes execution.

        A Done event does not occur when a task is stopped explicitly, such as by calling DAQmx Stop Task.

        Args:
            callback_method (function): Specifies the function that you want
                DAQmx to call when the event occurs. The function you pass in
                this parameter must have the following prototype:

                >>> def callback(task_handle, status, callback_data):
                >>>     return 0

                Upon entry to the callback, the task_handle parameter contains
                the handle to the task on which the event occurred. The status
                parameter contains the status of the task when the event
                occurred. If the status value is negative, it indicates an
                error. If the status value is zero, it indicates no error.
                If the status value is positive, it indicates a warning. The
                callbackData parameter contains the value you passed in the
                callbackData parameter of this function.

                Passing None for this parameter unregisters the event callback
                function.
        """  # noqa: W505 - doc line too long (175 > 100 characters) (auto-generated noqa)
        if callback_method is not None:
            # If the event is already registered, the interpreter should raise DaqError with code
            # DAQmxErrors.DONE_EVENT_ALREADY_REGISTERED.
            event_handler = self._interpreter.register_done_event(
                self._handle, 0, callback_method, None
            )
            with self._event_handler_lock:
                assert _TaskEventType.DONE not in self._event_handlers, "Event already registered."
                self._event_handlers[_TaskEventType.DONE] = event_handler
        else:
            self._interpreter.unregister_done_event(self._handle)
            with self._event_handler_lock:
                event_handler = self._event_handlers.pop(_TaskEventType.DONE, None)
            if event_handler is not None:
                event_handler.close()  # may raise an exception

    def register_every_n_samples_acquired_into_buffer_event(self, sample_interval, callback_method):
        """Registers a callback function to receive an event when the specified number of samples is written from the device to the buffer.

        This function only works with devices that support buffered tasks.

        When you stop a task explicitly any pending events are discarded. For
        example, if you call DAQmx Stop Task then you do not receive any
        pending events.

        Args:
            sample_interval (int): Specifies the number of samples after
                which each event should occur.
            callback_method (function): Specifies the function that you want
                DAQmx to call when the event occurs. The function you pass in
                this parameter must have the following prototype:

                >>> def callback(task_handle, every_n_samples_event_type,
                >>>         number_of_samples, callback_data):
                >>>     return 0

                Upon entry to the callback, the task_handle parameter contains
                the handle to the task on which the event occurred. The
                every_n_samples_event_type parameter contains the
                EveryNSamplesEventType.ACQUIRED_INTO_BUFFER value. The
                number_of_samples parameter contains the value you passed in
                the sample_interval parameter of this function. The
                callback_data parameter contains the value you passed in the
                callback_data parameter of this function.

                Passing None for this parameter unregisters the event callback
                function.
        """  # noqa: W505 - doc line too long (139 > 100 characters) (auto-generated noqa)
        if callback_method is not None:
            # If the event is already registered, the interpreter should raise DaqError with code
            # DAQmxErrors.EVERY_N_SAMPS_ACQ_INTO_BUFFER_EVENT_ALREADY_REGISTERED.
            event_handler = self._interpreter.register_every_n_samples_event(
                self._handle,
                EveryNSamplesEventType.ACQUIRED_INTO_BUFFER.value,
                sample_interval,
                0,
                callback_method,
                None,
            )
            with self._event_handler_lock:
                assert (
                    _TaskEventType.EVERY_N_SAMPLES_ACQUIRED_INTO_BUFFER not in self._event_handlers
                ), "Event already registered."
                self._event_handlers[_TaskEventType.EVERY_N_SAMPLES_ACQUIRED_INTO_BUFFER] = (
                    event_handler
                )
        else:
            self._interpreter.unregister_every_n_samples_event(
                self._handle, EveryNSamplesEventType.ACQUIRED_INTO_BUFFER.value
            )
            with self._event_handler_lock:
                event_handler = self._event_handlers.pop(
                    _TaskEventType.EVERY_N_SAMPLES_ACQUIRED_INTO_BUFFER, None
                )
            if event_handler is not None:
                event_handler.close()  # may raise an exception

    def register_every_n_samples_transferred_from_buffer_event(
        self, sample_interval, callback_method
    ):
        """Registers a callback function to receive an event when the specified number of samples is written from the buffer to the device.

        This function only works with devices that support buffered tasks.

        When you stop a task explicitly any pending events are discarded. For
        example, if you call DAQmx Stop Task then you do not receive any
        pending events.

        Args:
            sample_interval (int): Specifies the number of samples after
                which each event should occur.
            callback_method (function): Specifies the function that you want
                DAQmx to call when the event occurs. The function you pass in
                this parameter must have the following prototype:

                >>> def callback(task_handle, every_n_samples_event_type,
                >>>         number_of_samples, callback_data):
                >>>     return 0

                Upon entry to the callback, the task_handle parameter contains
                the handle to the task on which the event occurred. The
                every_n_samples_event_type parameter contains the
                EveryNSamplesEventType.TRANSFERRED_FROM_BUFFER value. The
                number_of_samples parameter contains the value you passed in
                the sample_interval parameter of this function. The
                callback_data parameter contains the value you passed in the
                callback_data parameter of this function.

                Passing None for this parameter unregisters the event callback
                function.
        """  # noqa: W505 - doc line too long (139 > 100 characters) (auto-generated noqa)
        if callback_method is not None:
            # If the event is already registered, the interpreter should raise DaqError with code
            # DAQmxErrors.EVERY_N_SAMPS_TRANSFERRED_FROM_BUFFER_EVENT_ALREADY_REGISTERED.
            event_handler = self._interpreter.register_every_n_samples_event(
                self._handle,
                EveryNSamplesEventType.TRANSFERRED_FROM_BUFFER.value,
                sample_interval,
                0,
                callback_method,
                None,
            )
            with self._event_handler_lock:
                assert (
                    _TaskEventType.EVERY_N_SAMPLES_TRANSFERRED_FROM_BUFFER
                    not in self._event_handlers
                ), "Event already registered."
                self._event_handlers[_TaskEventType.EVERY_N_SAMPLES_TRANSFERRED_FROM_BUFFER] = (
                    event_handler
                )
        else:
            self._interpreter.unregister_every_n_samples_event(
                self._handle, EveryNSamplesEventType.TRANSFERRED_FROM_BUFFER.value
            )
            with self._event_handler_lock:
                event_handler = self._event_handlers.pop(
                    _TaskEventType.EVERY_N_SAMPLES_TRANSFERRED_FROM_BUFFER, None
                )
            if event_handler is not None:
                event_handler.close()  # may raise an exception

    def register_signal_event(self, signal_type, callback_method):
        """Registers a callback function to receive an event when the specified hardware event occurs.

        When you stop a task explicitly any pending events are discarded. For
        example, if you call DAQmx Stop Task then you do not receive any
        pending events.

        Args:
            signal_type (nidaqmx.constants.Signal): Specifies the type of
                signal for which you want to receive results.
            callback_method (function): Specifies the function that you want
                DAQmx to call when the event occurs. The function you pass in
                this parameter must have the following prototype:

                >>> def callback(task_handle, signal_type, callback_data):
                >>>     return 0

                Upon entry to the callback, the task_handle parameter contains
                the handle to the task on which the event occurred. The
                signal_type parameter contains the integer value you passed in
                the signal_type parameter of this function. The callback_data
                parameter contains the value you passed in the callback_data
                parameter of this function.

                Passing None for this parameter unregisters the event callback
                function.
        """  # noqa: W505 - doc line too long (102 > 100 characters) (auto-generated noqa)
        if callback_method is not None:
            # If the event is already registered, the interpreter should raise DaqError with code
            # DAQmxErrors.SIGNAL_EVENT_ALREADY_REGISTERED.
            event_handler = self._interpreter.register_signal_event(
                self._handle, signal_type.value, 0, callback_method, None
            )
            with self._event_handler_lock:
                assert (
                    _TaskEventType.SIGNAL not in self._event_handlers
                ), "Event already registered."
                self._event_handlers[_TaskEventType.SIGNAL] = event_handler
        else:
            self._interpreter.unregister_signal_event(self._handle, signal_type.value)
            with self._event_handler_lock:
                event_handler = self._event_handlers.pop(_TaskEventType.SIGNAL, None)
            if event_handler is not None:
                event_handler.close()  # may raise an exception

    def save(
        self,
        save_as="",
        author="",
        overwrite_existing_task=False,
        allow_interactive_editing=True,
        allow_interactive_deletion=True,
    ):
        """Saves this task and any local channels it contains to MAX.

        This function does not save global channels. Use the DAQmx Save
        Global Channel function to save global channels.

        Args:
            save_as (Optional[str]): Is the name to save the task,
                global channel, or custom scale as. If you do not
                specify a value for this input, NI-DAQmx uses the name
                currently assigned to the task, global channel, or
                custom scale.
            author (Optional[str]): Is a name to store with the task,
                global channel, or custom scale.
            overwrite_existing_task (Optional[bool]): Specifies whether to
                overwrite a task of the same name if one is already saved in
                MAX. If this input is False and a task of the same name is
                already saved in MAX, this function returns an error.
            allow_interactive_editing (Optional[bool]): Specifies whether to
                allow the task, global channel, or custom scale to be edited
                in the DAQ Assistant. If allow_interactive_editing is True,
                the DAQ Assistant must support all task or global channel
                settings.
            allow_interactive_deletion (Optional[bool]): Specifies whether
                to allow the task, global channel, or custom scale to be
                deleted through MAX.
        """
        options = 0
        if overwrite_existing_task:
            options |= _Save.OVERWRITE.value
        if allow_interactive_editing:
            options |= _Save.ALLOW_INTERACTIVE_EDITING.value
        if allow_interactive_deletion:
            options |= _Save.ALLOW_INTERACTIVE_DELETION.value

        self._interpreter.save_task(self._handle, save_as, author, options)

    def start(self):
        """Start the task.

        This method transitions the task to the running state to begin the measurement or
        generation. Using this method is required for some applications and
        is optional for others.

        If you do not use this method, a measurement task starts automatically
        when the DAQmx Read method runs. The autostart input of the DAQmx Write
        method determines if a generation task starts automatically when the
        DAQmx Write method runs.

        If you do not use the DAQmx Start Task method and the DAQmx Stop Task
        method when you use the DAQmx Read method or the DAQmx Write method
        multiple times, such as in a loop, the task starts and stops
        repeatedly. Starting and stopping a task repeatedly reduces the
        performance of the application.
        """
        self._interpreter.start_task(self._handle)

    def stop(self):
        """Stop the task.

        This method stops the task and returns it to the state the task was in before the
        DAQmx Start Task method ran or the DAQmx Write method ran with the
        autostart input set to TRUE.

        If you do not use the DAQmx Start Task method and the DAQmx Stop Task
        method when you use the DAQmx Read method or the DAQmx Write method
        multiple times, such as in a loop, the task starts and stops
        repeatedly. Starting and stopping a task repeatedly reduces the
        performance of the application.
        """
        self._interpreter.stop_task(self._handle)

    def wait_for_valid_timestamp(self, timestamp_event, timeout=10.0):
        """Wait until the specified timestamp has a value.

        Use this method to ensure the timestamp has a valid value to prevent an error when querying a timestamp value.

        Args:
            timestamp_event(nidaqmx.constants.TimestampEvent): Specifies the timestamp type to wait on.
            timeout (float): Specifies the maximum amount of time in
                seconds to wait for a valid timestamp.
                This method returns an error if the time elapses. The
                default is 10. If you set timeout (sec) to
                nidaqmx.WAIT_INFINITELY, the method waits indefinitely.

        Returns:
            datetime:

            The timestamp value of timestamp_event.
        """  # noqa: W505 - doc line too long (118 > 100 characters) (auto-generated noqa)
        return self._interpreter.wait_for_valid_timestamp(
            self._handle, timestamp_event.value, timeout
        )

    def wait_until_done(self, timeout=10.0):
        """Waits for the measurement or generation to complete.

        Use this method to ensure that the specified operation is complete
        before you stop the task.

        Args:
            timeout (Optional[float]): Specifies the maximum amount of time in
                seconds to wait for the measurement or generation to complete.
                This method returns an error if the time elapses. The
                default is 10. If you set timeout (sec) to
                nidaqmx.WAIT_INFINITELY, the method waits indefinitely. If you
                set timeout (sec) to 0, the method checks once and returns
                an error if the measurement or generation is not done.
        """
        self._interpreter.wait_until_task_done(self._handle, timeout)

    def _raise_invalid_num_lines_error(self, num_lines_expected, num_lines_in_data) -> NoReturn:
        raise DaqError(
            "Specified read or write operation failed, because the number "
            "of lines in the data for a channel does not match the number "
            "of lines in the channel.\n\n"
            "If you are using boolean data, make sure the array dimension "
            "for lines in the data matches the number of lines in the "
            "channel.\n\n"
            "Number of Lines Per Channel in Task: {}\n"
            "Number of Lines Per Channel in Data: {}".format(num_lines_expected, num_lines_in_data),
            DAQmxErrors.NUM_LINES_MISMATCH_IN_READ_OR_WRITE,
            task_name=self.name,
        )

    def _raise_invalid_write_num_chans_error(
        self, number_of_channels, number_of_channels_in_data
    ) -> NoReturn:

        raise DaqError(
            "Write cannot be performed, because the number of channels in the "
            "data does not match the number of channels in the task.\n\n"
            "When writing, supply data for all channels in the task. "
            "Alternatively, modify the task to contain the same number of "
            "channels as the data written.\n\n"
            "Number of Channels in Task: {}\n"
            "Number of Channels in Data: {}".format(number_of_channels, number_of_channels_in_data),
            DAQmxErrors.WRITE_NUM_CHANS_MISMATCH,
            task_name=self.name,
        )

    def _raise_invalid_write_mixed_data_error(self) -> NoReturn:
        raise DaqError(
            "Write cannot be performed, because the list contains a mix of "
            "AnalogWaveform and non-AnalogWaveform objects. All elements in "
            "the list must be the same type.",
            DAQmxErrors.UNKNOWN,
            task_name=self.name,
        )

    def _raise_no_output_channels_error(self) -> NoReturn:
        raise DaqError(
            "Write failed, because there are no output channels in this "
            "task to which data can be written.",
            DAQmxErrors.WRITE_NO_OUTPUT_CHANS_IN_TASK,
            task_name=self.name,
        )

    def _raise_unsupported_output_type_error(self, output_type) -> NoReturn:
        raise DaqError(
            "Write failed, because the output type is not supported.\n\n"
            f"Output type: {output_type}",
            DAQmxErrors.UNKNOWN,
            task_name=self.name,
        )

    def write(self, data, auto_start=AUTO_START_UNSET, timeout=10.0):
        """Writes samples to the task or virtual channels you specify.

        This write method is dynamic, and is capable of accepting the
        samples to write in the various forms for most operations:

        - Scalar: Single sample for 1 channel.
        - List/1D numpy.ndarray: Multiple samples for 1 channel or 1
          sample for multiple channels.
        - List of lists/2D numpy.ndarray: Multiple samples for multiple
          channels.
        - AnalogWaveform: Waveform data for a single analog output channel.
        - DigitalWaveform: Waveform data for a single digital output channel.
        - List of AnalogWaveform: Waveform data for multiple analog output channels.

        The data type of the samples passed in must be appropriate for
        the channel type of the task.

        For counter output pulse operations, this write method only
        accepts samples in these forms:

        - Scalar CtrFreq, CtrTime, CtrTick (from nidaqmx.types):
          Single sample for 1 channel.
        - List of CtrFreq, CtrTime, CtrTick (from nidaqmx.types):
          Multiple samples for 1 channel or 1 sample for multiple
          channels.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (dynamic): Contains the samples to write to the task.

                The data you write must be in the units of the
                generation, including any custom scales. Use the DAQmx
                Create Channel methods to specify these units.
            auto_start (Optional[bool]): Specifies if this method
                automatically starts the task if you did not explicitly
                start it with the DAQmx Start Task method.

                The default value of this parameter depends on whether
                you specify one sample or many samples to write to each
                channel. If one sample per channel was specified, the
                default value is True. If multiple samples per channel
                were specified, the default value is False.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.

        Returns:
            int:

            Specifies the actual number of samples this method
            successfully wrote.
        """
        if self._is_waveform_data(data):
            return self.write_waveform(data, auto_start, timeout)

        channels_to_write = self.channels
        number_of_channels = len(channels_to_write.channel_names)
        write_chan_type = channels_to_write.chan_type

        element = None
        if number_of_channels == 1:
            if isinstance(data, list):
                if isinstance(data[0], list):
                    self._raise_invalid_write_num_chans_error(number_of_channels, len(data))

                number_of_samples_per_channel = len(data)
                element = data[0]

            elif isinstance(data, numpy.ndarray):
                if len(data.shape) == 2:
                    self._raise_invalid_write_num_chans_error(number_of_channels, data.shape[0])

                number_of_samples_per_channel = len(data)
                element = data[0]

            else:
                number_of_samples_per_channel = 1
                element = data

        else:
            if isinstance(data, list):
                if len(data) != number_of_channels:
                    self._raise_invalid_write_num_chans_error(number_of_channels, len(data))

                if isinstance(data[0], list):
                    number_of_samples_per_channel = len(data[0])
                    element = data[0][0]
                else:
                    number_of_samples_per_channel = 1
                    element = data[0]

            elif isinstance(data, numpy.ndarray):
                if data.shape[0] != number_of_channels:
                    self._raise_invalid_write_num_chans_error(number_of_channels, data.shape[0])

                if len(data.shape) == 2:
                    number_of_samples_per_channel = data.shape[1]
                    element = data[0][0]
                else:
                    number_of_samples_per_channel = 1
                    element = data[0]

            else:
                self._raise_invalid_write_num_chans_error(number_of_channels, 1)

        if auto_start is AUTO_START_UNSET:
            if number_of_samples_per_channel > 1:
                auto_start = False
            else:
                auto_start = True

        if write_chan_type == ChannelType.ANALOG_OUTPUT:
            data = numpy.asarray(data, dtype=numpy.float64)
            return self._interpreter.write_analog_f64(
                self._handle,
                number_of_samples_per_channel,
                auto_start,
                timeout,
                FillMode.GROUP_BY_CHANNEL.value,
                data,
            )

        elif write_chan_type == ChannelType.DIGITAL_OUTPUT:
            if self.out_stream.do_num_booleans_per_chan == 1:
                if not isinstance(element, bool) and not isinstance(element, numpy.bool_):
                    raise DaqError(
                        "Write failed, because this write method only accepts "
                        "boolean samples when there is one digital line per "
                        "channel in a task.\n\n"
                        "Requested sample type: {}".format(type(element)),
                        DAQmxErrors.UNKNOWN,
                        task_name=self.name,
                    )

                data = numpy.asarray(data, dtype=bool)
                return self._interpreter.write_digital_lines(
                    self._handle,
                    number_of_samples_per_channel,
                    auto_start,
                    timeout,
                    FillMode.GROUP_BY_CHANNEL.value,
                    data,
                )
            else:
                if not isinstance(element, int) and not isinstance(element, numpy.uint32):
                    raise DaqError(
                        "Write failed, because this write method only accepts "
                        "unsigned 32-bit integer samples when there are "
                        "multiple digital lines per channel in a task.\n\n"
                        "Requested sample type: {}".format(type(element)),
                        DAQmxErrors.UNKNOWN,
                        task_name=self.name,
                    )

                data = numpy.asarray(data, dtype=numpy.uint32)
                return self._interpreter.write_digital_u32(
                    self._handle,
                    number_of_samples_per_channel,
                    auto_start,
                    timeout,
                    FillMode.GROUP_BY_CHANNEL.value,
                    data,
                )

        elif write_chan_type == ChannelType.COUNTER_OUTPUT:
            output_type = channels_to_write.co_output_type

            if number_of_samples_per_channel == 1:
                data = [data]
            elif not isinstance(data, Iterable):
                raise DaqError(
                    "Write failed, because the provided data type is not supported "
                    "for counter output channels.",
                    DAQmxErrors.UNKNOWN,
                    task_name=self.name,
                )

            if output_type == UsageTypeCO.PULSE_FREQUENCY:
                if not all(isinstance(sample, CtrFreq) for sample in data):
                    raise TypeError(f"Output type {output_type} requires samples of type CtrFreq.")

                frequencies = numpy.array([sample.freq for sample in data], dtype=numpy.float64)
                duty_cycles = numpy.array(
                    [sample.duty_cycle for sample in data], dtype=numpy.float64
                )

                return self._interpreter.write_ctr_freq(
                    self._handle,
                    number_of_samples_per_channel,
                    auto_start,
                    timeout,
                    FillMode.GROUP_BY_CHANNEL.value,
                    frequencies,
                    duty_cycles,
                )

            elif output_type == UsageTypeCO.PULSE_TIME:
                if not all(isinstance(sample, CtrTime) for sample in data):
                    raise TypeError(f"Output type {output_type} requires samples of type CtrTime.")

                high_times = numpy.array([sample.high_time for sample in data], dtype=numpy.float64)
                low_times = numpy.array([sample.low_time for sample in data], dtype=numpy.float64)

                return self._interpreter.write_ctr_time(
                    self._handle,
                    number_of_samples_per_channel,
                    auto_start,
                    timeout,
                    FillMode.GROUP_BY_CHANNEL.value,
                    high_times,
                    low_times,
                )

            elif output_type == UsageTypeCO.PULSE_TICKS:
                if not all(isinstance(sample, CtrTick) for sample in data):
                    raise TypeError(f"Output type {output_type} requires samples of type CtrTick.")

                high_ticks = numpy.array([sample.high_tick for sample in data], dtype=numpy.uint32)
                low_ticks = numpy.array([sample.low_tick for sample in data], dtype=numpy.uint32)

                return self._interpreter.write_ctr_ticks(
                    self._handle,
                    number_of_samples_per_channel,
                    auto_start,
                    timeout,
                    FillMode.GROUP_BY_CHANNEL.value,
                    high_ticks,
                    low_ticks,
                )

            else:
                self._raise_unsupported_output_type_error(output_type)

        else:
            self._raise_no_output_channels_error()

    def _is_waveform_data(self, data):
        """Check if data is waveform data (single waveform or list of waveforms)."""
        if isinstance(data, (AnalogWaveform, DigitalWaveform)):
            return True

        if not isinstance(data, list) or not data:
            return False

        return all(isinstance(wf, AnalogWaveform) for wf in data) or all(
            isinstance(wf, DigitalWaveform) for wf in data
        )

    @requires_feature(WAVEFORM_SUPPORT)
    def write_waveform(
        self,
        waveforms: (
            AnalogWaveform[Any]
            | DigitalWaveform[Any]
            | Sequence[AnalogWaveform[Any]]
            | Sequence[DigitalWaveform[Any]]
        ),
        auto_start=AUTO_START_UNSET,
        timeout: float = 10.0,
    ) -> int:
        """Writes samples from one or more waveforms to the task or virtual channels you specify.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            waveforms (AnalogWaveform[Any] or DigitalWaveform[Any] or
                Sequence[AnalogWaveform[Any]]):
                Contains the waveforms to write to the task.

                The data you write must be in the units of the
                generation, including any custom scales. Use the DAQmx
                Create Channel methods to specify these units.
            auto_start (Optional[bool]): Specifies if this method
                automatically starts the task if you did not explicitly
                start it with the DAQmx Start Task method.

                The default value of this parameter depends on whether
                you specify one sample or many samples to write to each
                channel. If one sample per channel was specified, the
                default value is True. If multiple samples per channel
                were specified, the default value is False.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.

        Returns:
            int:

            Specifies the actual number of samples this method
            successfully wrote.
        """
        channels_to_write = self.channels
        number_of_channels = len(channels_to_write.channel_names)
        write_chan_type = channels_to_write.chan_type

        if isinstance(waveforms, AnalogWaveform) or isinstance(waveforms, DigitalWaveform):
            number_of_samples_per_channel = waveforms.sample_count
        elif isinstance(waveforms, list):
            number_of_samples_per_channel = waveforms[0].sample_count
        else:
            number_of_samples_per_channel = 1

        if auto_start is AUTO_START_UNSET:
            if number_of_samples_per_channel > 1:
                auto_start = False
            else:
                auto_start = True

        if write_chan_type == ChannelType.ANALOG_OUTPUT:
            if isinstance(waveforms, AnalogWaveform):
                if number_of_channels != 1:
                    self._raise_invalid_write_num_chans_error(number_of_channels, 1)
                return self._interpreter.write_analog_waveform(
                    self._handle, waveforms, auto_start, timeout
                )
            elif isinstance(waveforms, list) and isinstance(waveforms[0], AnalogWaveform):
                if number_of_channels != len(waveforms):
                    self._raise_invalid_write_num_chans_error(number_of_channels, len(waveforms))
                return self._interpreter.write_analog_waveforms(
                    self._handle, waveforms, auto_start, timeout
                )
            else:
                self._raise_unsupported_output_type_error(type(waveforms))

        elif write_chan_type == ChannelType.DIGITAL_OUTPUT:
            if isinstance(waveforms, DigitalWaveform):
                if number_of_channels != 1:
                    self._raise_invalid_write_num_chans_error(number_of_channels, 1)
                return self._interpreter.write_digital_waveform(
                    self._handle, waveforms, auto_start, timeout
                )
            elif isinstance(waveforms, list) and isinstance(waveforms[0], DigitalWaveform):
                if number_of_channels != len(waveforms):
                    self._raise_invalid_write_num_chans_error(number_of_channels, len(waveforms))
                return self._interpreter.write_digital_waveforms(
                    self._handle, waveforms, auto_start, timeout
                )
            else:
                self._raise_unsupported_output_type_error(type(waveforms))

        else:
            self._raise_no_output_channels_error()


class _TaskAlternateConstructor(Task):
    """Provide an alternate constructor for the Task object.

    This is a private API used to instantiate a Task with an existing task handle and interpreter.
    """

    # Setting __slots__ avoids TypeError: __class__ assignment: 'Base' object layout differs from 'Derived'.  # noqa: W505 - doc line too long (108 > 100 characters) (auto-generated noqa)
    __slots__ = ()

    def __init__(self, task_handle, interpreter, close_on_exit):
        """Initialize a new Task with an existing interpreter.

        Args:
            task_handle: Specifies the task handle from which to create a
                Task object.
            interpreter: Specifies the interpreter instance.
            close_on_exit: Specifies whether the task's context manager closes the task.
        """
        # Initialize the fields that __del__ accesses so it doesn't crash when _initialize raises an exception.  # noqa: W505 - doc line too long (111 > 100 characters) (auto-generated noqa)
        self._handle = task_handle
        self._close_on_exit = close_on_exit
        self._saved_name = ""  # _initialize sets this to the name assigned by DAQmx.
        self._grpc_options = getattr(interpreter, "_grpc_options", None)
        self._event_handlers = {}

        self._interpreter = interpreter
        self._initialize(self._handle, self._interpreter)

        # Use meta-programming to change the type of this object to Task,
        # so the user isn't confused when doing introspection.
        self.__class__ = Task  # type: ignore[assignment]


class _TaskEventType(Enum):
    """Internal enum for task event bookkeeping."""

    DONE = 1
    EVERY_N_SAMPLES_ACQUIRED_INTO_BUFFER = 2
    EVERY_N_SAMPLES_TRANSFERRED_FROM_BUFFER = 3
    SIGNAL = 4
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/task/channels/__init__.py sha256=839e6ceacbfcf1f97f851d51868b9275f2aee345e8c9794ca160f3064fadac06 bytes=571 -->
## FILE: src/handwritten/task/channels/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/task/channels/__init__.py`
- sha256: `839e6ceacbfcf1f97f851d51868b9275f2aee345e8c9794ca160f3064fadac06`
- bytes: 571

````python
"""NI-DAQmx channel classes."""

from nidaqmx.task.channels._ai_channel import AIChannel
from nidaqmx.task.channels._ao_channel import AOChannel
from nidaqmx.task.channels._channel import Channel
from nidaqmx.task.channels._ci_channel import CIChannel
from nidaqmx.task.channels._co_channel import COChannel
from nidaqmx.task.channels._di_channel import DIChannel
from nidaqmx.task.channels._do_channel import DOChannel

__all__ = [
    "Channel",
    "AIChannel",
    "AOChannel",
    "CIChannel",
    "COChannel",
    "DIChannel",
    "DOChannel",
]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/task/collections/__init__.py sha256=a6e64ed5353fbf78657f241f1ce76e252372d5a6a073b23438e3fb1ca0ecc126 bytes=820 -->
## FILE: src/handwritten/task/collections/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/task/collections/__init__.py`
- sha256: `a6e64ed5353fbf78657f241f1ce76e252372d5a6a073b23438e3fb1ca0ecc126`
- bytes: 820

````python
"""NI-DAQmx channel collection classes."""

from nidaqmx.task.collections._ai_channel_collection import AIChannelCollection
from nidaqmx.task.collections._ao_channel_collection import AOChannelCollection
from nidaqmx.task.collections._channel_collection import ChannelCollection
from nidaqmx.task.collections._ci_channel_collection import CIChannelCollection
from nidaqmx.task.collections._co_channel_collection import COChannelCollection
from nidaqmx.task.collections._di_channel_collection import DIChannelCollection
from nidaqmx.task.collections._do_channel_collection import DOChannelCollection

__all__ = [
    "ChannelCollection",
    "AIChannelCollection",
    "AOChannelCollection",
    "CIChannelCollection",
    "COChannelCollection",
    "DIChannelCollection",
    "DOChannelCollection",
]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/task/collections/_channel_collection.py sha256=97be1a9a302b08bde9d9a7f3e0d04cfcc6b7b182f5766c50c641bde03bf436d5 bytes=4821 -->
## FILE: src/handwritten/task/collections/_channel_collection.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/task/collections/_channel_collection.py`
- sha256: `97be1a9a302b08bde9d9a7f3e0d04cfcc6b7b182f5766c50c641bde03bf436d5`
- bytes: 4821

````python
from collections.abc import Sequence

from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError
from nidaqmx.task.channels._channel import Channel
from nidaqmx.utils import flatten_channel_string, unflatten_channel_string


class ChannelCollection(Sequence):
    """Contains the collection of channels for a DAQmx Task.

    This class defines methods that implements a container object.
    """

    def __init__(self, task_handle, interpreter):
        """Do not construct this object directly; instead, construct a nidaqmx.Task and use the appropriate property, such as task.ai_channels."""  # noqa: W505 - doc line too long (146 > 100 characters) (auto-generated noqa)
        self._handle = task_handle
        self._interpreter = interpreter

    def __contains__(  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        self, item
    ):
        channel_names = self.channel_names

        if isinstance(item, str):
            items = unflatten_channel_string(item)
        elif isinstance(item, Channel):
            items = item.channel_names

        return all([item in channel_names for item in items])

    def __eq__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        if isinstance(other, self.__class__):
            return self._handle == other._handle
        return False

    def __getitem__(self, index):
        """Indexes a subset of virtual channels on this channel collection.

        Args:
            index: The value of the index. The following index types are
                supported:
                - str: Name of the virtual channel. You also can specify a
                    string that contains a list or range of names to this
                    input. If you have a list of names, use the DAQmx
                    Flatten Channel String function to convert the list to a
                    string.
                - int: Index/position of the virtual channel in the collection.
                - slice: Range of the indexes/positions of virtual channels in
                    the collection.

        Returns:
            nidaqmx.task.channels.Channel:

            Indicates a channel object representing the subset of virtual
            channels indexed.
        """
        if isinstance(index, int):
            channel_names = self.channel_names[index]
        elif isinstance(index, slice):
            channel_names = flatten_channel_string(self.channel_names[index])
        elif isinstance(index, str):
            channel_names = index
        else:
            raise DaqError(
                f'Invalid index type "{type(index)}" used to access channels.',
                DAQmxErrors.UNKNOWN,
            )

        if channel_names:
            return Channel._factory(self._handle, channel_names, self._interpreter)
        else:
            raise DaqError(
                "You cannot specify an empty index when indexing channels.\n"
                "Index used: {}".format(index),
                DAQmxErrors.UNKNOWN,
            )

    def __hash__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return self._interpreter.hash_task_handle(self._handle)

    def __iter__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        for channel_name in self.channel_names:
            yield Channel._factory(self._handle, channel_name, self._interpreter)

    def __len__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return len(self.channel_names)

    def __ne__(self, other):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return not self.__eq__(other)

    def __reversed__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        channel_names = self.channel_names
        channel_names.reverse()

        for channel_name in channel_names:
            yield Channel._factory(self._handle, channel_name, self._interpreter)

    @property
    def all(self):
        """:class:`nidaqmx.task.channels.Channel`: Specifies a channel object that represents the entire list of virtual channels on this channel collection."""  # noqa: W505 - doc line too long (160 > 100 characters) (auto-generated noqa)
        # Passing a blank string means all channels.
        return Channel._factory(self._handle, "", self._interpreter)

    @property
    def channel_names(self):
        """List[str]: Specifies the entire list of virtual channels on this channel collection."""
        val = self._interpreter.get_task_attribute_string(self._handle, 0x1273)
        return unflatten_channel_string(val)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/task/triggering/__init__.py sha256=0ace23866dee1982ac6ca89d0ee4186629191cc3cb2b3d7279ccfbd6631c615a bytes=598 -->
## FILE: src/handwritten/task/triggering/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/task/triggering/__init__.py`
- sha256: `0ace23866dee1982ac6ca89d0ee4186629191cc3cb2b3d7279ccfbd6631c615a`
- bytes: 598

````python
"""NI-DAQmx task triggering classes."""

from nidaqmx.task.triggering._arm_start_trigger import ArmStartTrigger
from nidaqmx.task.triggering._handshake_trigger import HandshakeTrigger
from nidaqmx.task.triggering._pause_trigger import PauseTrigger
from nidaqmx.task.triggering._reference_trigger import ReferenceTrigger
from nidaqmx.task.triggering._start_trigger import StartTrigger
from nidaqmx.task.triggering._triggers import Triggers

__all__ = [
    "Triggers",
    "ArmStartTrigger",
    "HandshakeTrigger",
    "PauseTrigger",
    "ReferenceTrigger",
    "StartTrigger",
]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/types.py sha256=b7d4fcb53a87fb6d40926989d5c056a6251015ec40597014b0f8543d325a3ab9 bytes=1916 -->
## FILE: src/handwritten/types.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/types.py`
- sha256: `b7d4fcb53a87fb6d40926989d5c056a6251015ec40597014b0f8543d325a3ab9`
- bytes: 1916

````python
"""NI-DAQmx data types."""

import collections
import typing

# region Task Counter IO named tuples

CtrFreq = collections.namedtuple("CtrFreq", ["freq", "duty_cycle"])

CtrTick = collections.namedtuple("CtrTick", ["high_tick", "low_tick"])

CtrTime = collections.namedtuple("CtrTime", ["high_time", "low_time"])

# endregion

# region Power IO named tuples

PowerMeasurement = collections.namedtuple("PowerMeasurement", ["voltage", "current"])

# endregion

# region Watchdog named tuples

AOExpirationState = collections.namedtuple(
    "AOExpirationState", ["physical_channel", "expiration_state", "output_type"]
)

COExpirationState = collections.namedtuple(
    "COExpirationState", ["physical_channel", "expiration_state"]
)

DOExpirationState = collections.namedtuple(
    "DOExpirationState", ["physical_channel", "expiration_state"]
)

# endregion

# region Power Up States named tuples

AOPowerUpState = collections.namedtuple(
    "AOPowerUpState", ["physical_channel", "power_up_state", "channel_type"]
)

DOPowerUpState = collections.namedtuple("DOPowerUpState", ["physical_channel", "power_up_state"])

DOResistorPowerUpState = collections.namedtuple(
    "DOResistorPowerUpState", ["physical_channel", "power_up_state"]
)

# endregion

# region System named tuples

CDAQSyncConnection = collections.namedtuple("CDAQSyncConnection", ["output_port", "input_port"])

DriverVersion = collections.namedtuple(
    "DriverVersion", ["major_version", "minor_version", "update_version"]
)

# endregion

# region ID Pin named tuples


class IDPinContents(typing.NamedTuple):
    """IDPinContents represent the contents of the memory connected to the ID pin."""

    data: list[int]
    """The binary data stored on the memory connected to the ID pin."""

    format_code: int
    """The format code of the binary data."""


# endregion
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/utils.py sha256=917ce90b80c7a08e405a04e008edf8f8e0564bea2867b0f26ec2a1003288a368 bytes=9010 -->
## FILE: src/handwritten/utils.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/utils.py`
- sha256: `917ce90b80c7a08e405a04e008edf8f8e0564bea2867b0f26ec2a1003288a368`
- bytes: 9010

````python
"""NI-DAQmx utility functions."""

from __future__ import annotations

import re
from dataclasses import dataclass

from nidaqmx._base_interpreter import BaseInterpreter
from nidaqmx.errors import DaqError
from nidaqmx.grpc_session_options import GrpcSessionOptions

# Method logic adapted from
# cspell:disable-next-line
# //Measurements/Infrastructure/dmxf/trunk/2.5/source/nimuck/parseUtilities.cpp

_invalid_range_syntax_message = (
    "Syntax for a range of objects in the input string is invalid.\n\n"
    "For ranges of objects, specify a number immediately before and after "
    "every colon (':') in the input string. Or, if a name is specified after "
    "the colon, it must be identical to the name specified immediately before "
    "the colon. Colons are not allowed within the names of the individual "
    "objects."
)


@dataclass
class _ChannelInfo:
    base_name: str = ""
    start_index: int = -1
    start_index_str: str = ""
    end_index: int = -1
    end_index_str: str = ""

    def to_flattened_name(self) -> str:
        """Convert the channel info to a flattened channel name."""
        if self.start_index == -1:
            return self.base_name
        elif self.start_index == self.end_index:
            return f"{self.base_name}{self.start_index_str}"
        else:
            return f"{self.base_name}{self.start_index_str}:{self.end_index_str}"


def flatten_channel_string(channel_names: list[str]) -> str:
    """Converts a list of channel names to a comma-delimited list of names.

    You can use this method to convert a list of physical or virtual channel
    names to a single string prior to using the DAQmx Create Channel methods or
    instantiating a DAQmx Task object.

    Note: For simplicity, this implementation is not fully compatible with the
    NI-DAQmx driver implementation, which is generally more permissive. For
    example, the driver is more graceful with whitespace padding. It was deemed
    valuable to implement this natively in Python, so it can be leveraged in
    workflows that don't have the driver installed. If we have specific examples
    where this approximation is a problem, we can revisit this in the future.

    Args:
        channel_names: The list of physical or virtual channel names.

    Returns:
        The resulting comma-delimited list of physical or virtual channel names.
    """
    unflattened_channel_names = []
    for channel_name in channel_names:
        unflattened_channel_names.extend(unflatten_channel_string(channel_name))

    # Go through the channel names and flatten them.
    flattened_channel_list = []
    previous = _ChannelInfo()
    for channel_name in unflattened_channel_names:
        m = re.search("(.*[^0-9])?([0-9]+)$", channel_name)
        if not m:
            # If the channel name doesn't end in a valid number, just use the
            # channel name as-is.
            flattened_channel_list.append(previous.to_flattened_name())
            previous = _ChannelInfo(channel_name)
        else:
            # If the channel name ends in a valid number, we may need to flatten
            # this channel with subsequent channels in the x:y format.
            current_base_name = m.group(1)
            current_index_str = m.group(2)
            current_index = int(current_index_str)

            if current_base_name == previous.base_name and (
                (
                    current_index == previous.end_index + 1
                    and previous.end_index >= previous.start_index
                )
                or (
                    current_index == previous.end_index - 1
                    and previous.end_index <= previous.start_index
                )
            ):
                # If the current channel name has the same base name as the
                # previous and it's end index differs by 1, change the end
                # index value. It gets flattened later.
                previous.end_index = current_index
                previous.end_index_str = current_index_str
            else:
                # If the current channel name has the same base name as the
                # previous or it's end index differs by more than 1, it doesn't
                # get flattened with the previous channel.
                flattened_channel_list.append(previous.to_flattened_name())
                previous = _ChannelInfo(
                    current_base_name,
                    current_index,
                    current_index_str,
                    current_index,
                    current_index_str,
                )

    # Convert the final channel dictionary to a flattened string
    flattened_channel_list.append(previous.to_flattened_name())

    # Remove empty strings in list, convert to comma-delimited string, then trim
    # whitespace.
    return ",".join([_f for _f in flattened_channel_list if _f]).strip()


def unflatten_channel_string(channel_names: str) -> list[str]:
    """Converts a comma-delimited list of channel names to a list of names.

    You can use this method to convert a comma-delimited list or range of
    physical or virtual channels into a list of physical or virtual channel
    names.

    Note: For simplicity, this implementation is not fully compatible with the
    NI-DAQmx driver implementation, which is generally more permissive. For
    example, the driver is more graceful with whitespace padding. It was deemed
    valuable to implement this natively in Python, so it can be leveraged in
    workflows that don't have the driver installed. If we have specific examples
    where this approximation is a problem, we can revisit this in the future.

    Args:
        channel_names: The list or range of physical or virtual channels.

    Returns:
        The list of physical or virtual channel names.

        Each element of the list contains a single channel.
    """
    channel_list_to_return = []
    channel_list = [c for c in channel_names.strip().split(",") if c]

    for channel in channel_list:
        channel = channel.strip()
        colon_index = channel.find(":")

        if colon_index == -1:
            channel_list_to_return.append(channel)
        else:
            before = channel[:colon_index]
            after = channel[colon_index + 1 :]

            m_before = re.match("(.*?)([0-9]+)$", before)
            m_after = re.match("(.*?)([0-9]+)$", after)

            if not m_before or not m_after:
                raise DaqError(_invalid_range_syntax_message, error_code=-200498)

            if m_after.group(1) and (m_before.group(1).lower() != m_after.group(1).lower()):
                raise DaqError(_invalid_range_syntax_message, error_code=-200498)

            num_before_str = m_before.group(2)
            num_before = int(num_before_str)
            num_after_str = m_after.group(2)
            num_after = int(num_after_str)

            num_min_width = 0
            # If there are any leading 0s in the first number, we want to ensure
            # match that width. This is established precedence in the DAQmx
            # algorithm.
            if num_before > 0 and len(num_before_str.lstrip("0")) < len(num_before_str):
                num_min_width = len(num_before_str)

            num_max = max([num_before, num_after])
            num_min = min([num_before, num_after])
            number_of_channels = (num_max - num_min) + 1

            if number_of_channels >= 15000:
                raise DaqError(_invalid_range_syntax_message, error_code=-200498)

            colon_expanded_channel = []
            for i in range(number_of_channels):
                current_number = num_min + i
                if num_min_width > 0:
                    # Using f-strings to create format strings. Braces for days!
                    zero_padded_format_specifier = f"{{:0{num_min_width}d}}"
                    current_number_str = zero_padded_format_specifier.format(current_number)
                else:
                    current_number_str = str(current_number)
                colon_expanded_channel.append(f"{m_before.group(1)}{current_number_str}")

            if num_after < num_before:
                colon_expanded_channel.reverse()

            channel_list_to_return.extend(colon_expanded_channel)

    return channel_list_to_return


def _select_interpreter(
    grpc_options: GrpcSessionOptions | None = None, interpreter: BaseInterpreter | None = None
) -> BaseInterpreter:
    if interpreter:
        return interpreter
    else:
        if grpc_options:
            from nidaqmx._grpc_interpreter import GrpcStubInterpreter

            return GrpcStubInterpreter(grpc_options)
        else:
            from nidaqmx._library_interpreter import LibraryInterpreter

            return LibraryInterpreter()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/__init__.py sha256=a24d392cd815dab33ae50516eb86f3b035632f61753a5b6b0b54f6a0f07711a7 bytes=38 -->
## FILE: tests/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/__init__.py`
- sha256: `a24d392cd815dab33ae50516eb86f3b035632f61753a5b6b0b54f6a0f07711a7`
- bytes: 38

````python
"""Tests for the nidaqmx package."""
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/_event_utils.py sha256=c3b710abb4ae7dbcef4e49dc33d699752f2539c0cb124c331271e6d7b36aad7c bytes=3358 -->
## FILE: tests/_event_utils.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/_event_utils.py`
- sha256: `c3b710abb4ae7dbcef4e49dc33d699752f2539c0cb124c331271e6d7b36aad7c`
- bytes: 3358

````python
from __future__ import annotations

import threading
import time
from collections.abc import Callable
from typing import Generic, NamedTuple, TypeVar, Union


class DoneEvent(NamedTuple):
    """Represents a Done event."""

    status: int


class EveryNSamplesEvent(NamedTuple):
    """Represents an Every N Samples event."""

    event_type: int
    number_of_samples: int


class SignalEvent(NamedTuple):
    """Represents a Signal event."""

    signal_type: int


TEvent = TypeVar("TEvent", bound=Union[DoneEvent, EveryNSamplesEvent, SignalEvent])

SideEffect = Union[Callable[[], None], BaseException]


class BaseEventObserver(Generic[TEvent]):
    """Base class for event observers."""

    def __init__(self, side_effect: SideEffect | None = None):
        """Initializes the BaseEventObserver."""
        self._lock = threading.Lock()
        self._event_semaphore = threading.Semaphore(value=0)
        self._events: list[TEvent] = []
        self._side_effect = side_effect

    @property
    def events(self) -> list[TEvent]:
        """Returns the list of observed events."""
        with self._lock:
            return self._events[:]

    def wait_for_events(self, count=1, timeout=10.0) -> None:
        """Waits for the specified number of events."""
        timeout_time = time.monotonic() + timeout
        for _ in range(count):
            remaining_time = max(0.0, timeout_time - time.monotonic())
            if not self._event_semaphore.acquire(timeout=remaining_time):
                raise TimeoutError("Event observer did not observe the expected number of events.")

    def _invoke_side_effect(self) -> None:
        if isinstance(self._side_effect, BaseException):
            raise self._side_effect
        elif self._side_effect is not None:
            self._side_effect()


class DoneEventObserver(BaseEventObserver[DoneEvent]):
    """An observer for Done events."""

    def handle_done_event(self, task_handle: object, status: int, callback_data: object) -> int:
        """Handles a Done event."""
        with self._lock:
            self._events.append(DoneEvent(status))
            self._event_semaphore.release()
            self._invoke_side_effect()
        return 0


class EveryNSamplesEventObserver(BaseEventObserver[EveryNSamplesEvent]):
    """An observer for Every N Samples events."""

    def handle_every_n_samples_event(
        self,
        task_handle: object,
        every_n_samples_event_type: int,
        number_of_samples: int,
        callback_data: object,
    ) -> int:
        """Handles an Every N Samples event."""
        with self._lock:
            self._events.append(EveryNSamplesEvent(every_n_samples_event_type, number_of_samples))
            self._event_semaphore.release()
            self._invoke_side_effect()
        return 0


class SignalEventObserver(BaseEventObserver[SignalEvent]):
    """An observer for Signal events."""

    def handle_signal_event(
        self, task_handle: object, signal_type: int, callback_data: object
    ) -> int:
        """Handles a Signal event."""
        with self._lock:
            self._events.append(SignalEvent(signal_type))
            self._event_semaphore.release()
            self._invoke_side_effect()
        return 0
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/_grpc_utils.py sha256=9f50e4df77f9cbd8462dd8f79d191a9d1aab0a9065e036b0b0fde981189f3def bytes=2743 -->
## FILE: tests/_grpc_utils.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/_grpc_utils.py`
- sha256: `9f50e4df77f9cbd8462dd8f79d191a9d1aab0a9065e036b0b0fde981189f3def`
- bytes: 2743

````python
"""Helper functions to be used in nidaqmx tests."""

import pathlib
import re
import subprocess
import sys
import threading

import pytest


class GrpcServerProcess:
    """Maintains the processes involved in connecting to the gRPC device service."""

    def __init__(self):
        """Creates a GrpcServerProcess instance."""
        server_exe = self._get_grpc_server_exe()
        self._proc = subprocess.Popen([str(server_exe)], stdout=subprocess.PIPE)
        assert self._proc.stdout is not None

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

            self._stdout_thread = threading.Thread(
                target=self._proc.communicate, args=(), daemon=True
            )
            self._stdout_thread.start()
        except Exception:
            self._proc.kill()
            # Use communicate() to close the stdout pipe and wait for the server process to exit.
            _, _ = self._proc.communicate()
            raise

    def __enter__(self):
        """Returns the GrpcServerProcess instance."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Closes the GrpcServerProcess instance."""
        self._proc.kill()
        self._stdout_thread.join()

    def _get_grpc_server_exe(self):
        if sys.platform == "win32":
            import winreg

            try:
                reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
                read64key = winreg.KEY_READ | winreg.KEY_WOW64_64KEY
                with winreg.OpenKey(
                    reg, r"SOFTWARE\National Instruments\Common\Installer", access=read64key
                ) as key:
                    shared_dir, _ = winreg.QueryValueEx(key, "NISHAREDDIR64")
            except OSError:
                pytest.skip("NI gRPC Device Server not installed")
            server_exe = (
                pathlib.Path(shared_dir) / "NI gRPC Device Server" / "ni_grpc_device_server.exe"
            )
            if not server_exe.exists():
                pytest.skip("NI gRPC Device Server not installed")
            return server_exe
        else:
            pytest.skip("Only supported on Windows")
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/acceptance/__init__.py sha256=96780a1636077ff8a8b2614cb8b105cd324535e9cfc6562c056fec25d0ead250 bytes=49 -->
## FILE: tests/acceptance/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/acceptance/__init__.py`
- sha256: `96780a1636077ff8a8b2614cb8b105cd324535e9cfc6562c056fec25d0ead250`
- bytes: 49

````python
"""Acceptance tests for the nidaqmx package."""
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/acceptance/test_examples.py sha256=6f1fda65273524f77821399802844f705312b44a21454b80e247dab99e0f8a11 bytes=3169 -->
## FILE: tests/acceptance/test_examples.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/acceptance/test_examples.py`
- sha256: `6f1fda65273524f77821399802844f705312b44a21454b80e247dab99e0f8a11`
- bytes: 3169

````python
from __future__ import annotations

import contextlib
import re
import runpy
import warnings
from pathlib import Path

import pytest

import nidaqmx
import nidaqmx.system

EXAMPLES_DIRECTORY = Path(__file__).parent.parent.parent / "examples"
EXAMPLE_PATHS = [p for p in EXAMPLES_DIRECTORY.glob("**/*.py") if p.name != "__init__.py"]


@pytest.mark.parametrize("example_path", EXAMPLE_PATHS)
@pytest.mark.library_only(reason="The examples don't support gRPC.")
def test___shipping_example___run___no_errors(example_path: Path, system):
    example_source = example_path.read_text()
    for device_name in _find_device_names(example_source):
        if device_name not in system.devices:
            pytest.skip(f"Cannot find device {device_name}.")
        device = system.devices[device_name]
        for physical_channel_name in _find_physical_channel_names(example_source, device_name):
            if not _has_physical_channel(device, physical_channel_name):
                pytest.skip(
                    f"Device {device_name} does not have physical channel {physical_channel_name}"
                )
    if example_path.name in ["read_freq.py", "read_pulse_freq.py"]:
        pytest.skip("Example times out if there is no signal.")
    if example_path.name in [
        "voltage_acq_int_clk_dig_start_ref.py",
        "voltage_acq_int_clk_dig_ref.py",
    ]:
        pytest.skip("Example times out if there is no trigger signal.")
    if re.search(r"\binput\(|\bKeyboardInterrupt\b", example_source):
        pytest.skip("Example waits for keyboard input.")
    if re.search(r"\bmatplotlib\b", example_source):
        pytest.skip("Example plots waveform.")
    if re.search(r"\bnptdms\b", example_source):
        pytest.skip("Example performs TDMS logging.")
    if example_path.name == "nidaqmx_warnings.py":
        # Ignore warnings from this example.
        context_manager: contextlib.AbstractContextManager = warnings.catch_warnings(record=True)
    else:
        context_manager = contextlib.nullcontext()

    with context_manager:
        runpy.run_path(str(example_path))


def _find_device_names(source: str) -> set[str]:
    return set(re.findall(r"\b(?:cDAQ\d+Mod\d+|Dev\d+|PXI\d+Slot\d+|TS\d+Mod\d+)\b", source))


def _find_physical_channel_names(source: str, device_name: str) -> set[str]:
    return set(
        re.findall(
            r"\b" + device_name + r"/(?:ai\d+|ao\d+|ctr\d+|port\d+(?:/line\d+)?|power)(?::\d+)?\b",
            source,
        )
    )


def _has_physical_channel(device: nidaqmx.system.Device, physical_channel_name: str) -> bool:
    if (
        physical_channel_name.endswith("/power")
        and nidaqmx.constants.UsageTypeAI.POWER in device.ai_meas_types
    ):
        return True
    collections = [
        device.ai_physical_chans,
        device.ao_physical_chans,
        device.ci_physical_chans,
        device.co_physical_chans,
        device.di_ports,
        device.di_lines,
        device.do_ports,
        device.do_lines,
    ]
    return any(physical_channel_name in collection for collection in collections)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/acceptance/test_internationalization.py sha256=d17cfad83ec5452df4b42f5726e4f34b5f6dc207bc5fb81300ad43f2c42efb27 bytes=4111 -->
## FILE: tests/acceptance/test_internationalization.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/acceptance/test_internationalization.py`
- sha256: `d17cfad83ec5452df4b42f5726e4f34b5f6dc207bc5fb81300ad43f2c42efb27`
- bytes: 4111

````python
# cspell:ignore appareil Daten Données Gerät prüfende
from __future__ import annotations

import pathlib
from typing import Any

import pytest

from nidaqmx._lib import get_encoding_from_locale, lib_importer
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError
from nidaqmx.system import Device
from nidaqmx.task import Task


@pytest.fixture()
def ai_task(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    return task


def _get_encoding(obj: Task | dict[str, Any]) -> str | None:
    if getattr(obj, "_grpc_options", None) or (isinstance(obj, dict) and "grpc_options" in obj):
        # gRPC server limited to MBCS encoding
        return get_encoding_from_locale()
    else:
        return lib_importer.encoding


@pytest.mark.parametrize(
    "device_name, supported_encodings",
    [
        ("Gerät", ["1252", "iso-8859-1", "utf-8"]),
        ("l' appareil", ["1252", "iso-8859-1", "utf-8"]),
        ("デバイス", ["932", "shift-jis", "utf-8"]),
        ("장치", ["utf-8", "euc-kr"]),
        ("设备", ["utf-8", "gbk"]),
    ],
)
def test___supported_encoding___reset_nonexistent_device___returns_error_with_device_name(
    init_kwargs: dict[str, Any], device_name: str, supported_encodings: list[str]
):
    if _get_encoding(init_kwargs) not in supported_encodings:
        pytest.skip("requires compatible encoding")
    with pytest.raises(DaqError) as exc_info:
        Device(device_name, **init_kwargs).reset_device()

    assert f"Device Specified: {device_name}\n" in exc_info.value.args[0]
    assert exc_info.value.error_code == DAQmxErrors.INVALID_DEVICE_ID


@pytest.mark.parametrize(
    "file_path, supported_encodings",
    [
        ("Zu prüfende Daten.tdms", ["1252", "iso-8859-1", "utf-8"]),
        ("Données de test.tdms", ["1252", "iso-8859-1", "utf-8"]),
        ("テストデータ.tdms", ["932", "shift-jis", "utf-8"]),
        ("테스트 데이터.tdms", ["utf-8", "euc-kr"]),
        ("测试数据.tdms", ["utf-8", "gbk"]),
    ],
)
def test___supported_encoding___logging_file_path___returns_assigned_value(
    ai_task: Task, file_path: str, supported_encodings: list[str]
):
    if _get_encoding(ai_task) not in supported_encodings:
        pytest.skip("requires compatible encoding")
    ai_task.in_stream.logging_file_path = file_path

    assert ai_task.in_stream.logging_file_path == pathlib.Path(file_path)


@pytest.mark.parametrize(
    "file_path, supported_encodings",
    [
        ("Zu prüfende Daten.tdms", ["1252", "iso-8859-1", "utf-8"]),
        ("Données de test.tdms", ["1252", "iso-8859-1", "utf-8"]),
        ("テストデータ.tdms", ["932", "shift-jis", "utf-8"]),
        ("테스트 데이터.tdms", ["utf-8", "euc-kr"]),
        ("测试数据.tdms", ["utf-8", "gbk"]),
    ],
)
def test___supported_encoding___configure_logging___returns_assigned_values(
    ai_task: Task, file_path: str, supported_encodings: list[str]
):
    if _get_encoding(ai_task) not in supported_encodings:
        pytest.skip("requires compatible encoding")

    ai_task.in_stream.configure_logging(file_path)

    assert ai_task.in_stream.logging_file_path == pathlib.Path(file_path)


@pytest.mark.parametrize(
    "file_path, supported_encodings",
    [
        ("Zu prüfende Daten.tdms", ["1252", "iso-8859-1", "utf-8"]),
        ("Données de test.tdms", ["1252", "iso-8859-1", "utf-8"]),
        ("テストデータ.tdms", ["932", "shift-jis", "utf-8"]),
        ("테스트 데이터.tdms", ["utf-8", "euc-kr"]),
        ("测试数据.tdms", ["utf-8", "gbk"]),
    ],
)
def test___supported_encoding___start_new_file___returns_assigned_value(
    ai_task: Task, file_path: str, supported_encodings: list[str]
):
    if _get_encoding(ai_task) not in supported_encodings:
        pytest.skip("requires compatible encoding")
    ai_task.in_stream.start_new_file(file_path)

    assert ai_task.in_stream.logging_file_path == pathlib.Path(file_path)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/acceptance/test_multi_threading.py sha256=4b1ff888a0810be322b4a2f265780640306a5c16a636398281a85816f8a202ee bytes=9600 -->
## FILE: tests/acceptance/test_multi_threading.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/acceptance/test_multi_threading.py`
- sha256: `4b1ff888a0810be322b4a2f265780640306a5c16a636398281a85816f8a202ee`
- bytes: 9600

````python
from __future__ import annotations

import concurrent.futures
import functools
import random
import threading
import time
from collections.abc import Callable, Sequence
from concurrent.futures import Future, ThreadPoolExecutor
from contextlib import ExitStack
from threading import Barrier, Semaphore
from typing import Any

import pytest

from nidaqmx import Task
from nidaqmx.constants import AcquisitionType
from nidaqmx.system import Device, System
from nidaqmx.task.channels import AIChannel
from tests.helpers import generate_random_seed

RUN_TIME = 1.0
TIMEOUT = 10.0


@pytest.mark.parametrize("seed", [generate_random_seed()])
def test___single_task___get_set_float_properties___no_errors(
    task: Task,
    thread_pool_executor: ThreadPoolExecutor,
    multi_threading_test_devices: Sequence[Device],
    seed: int,
) -> None:
    random.seed(seed)
    num_channels = 2
    start_barrier = threading.Barrier(num_channels + 1)
    stop_semaphore = threading.Semaphore(0)
    for i in range(num_channels):
        task.ai_channels.add_ai_voltage_chan(
            multi_threading_test_devices[0].ai_physical_chans[i].name, min_val=-1.0, max_val=1.0
        )
    futures = [
        thread_pool_executor.submit(
            _get_set_property_thread_main,
            start_barrier,
            stop_semaphore,
            task.ai_channels[i],
            "ai_max",
            [1.0, 2.0, 5.0, 10.0],
        )
        for i in range(num_channels)
    ]

    start_barrier.wait(timeout=TIMEOUT)
    time.sleep(RUN_TIME)
    stop_semaphore.release(num_channels)

    concurrent.futures.wait(futures)
    _check_for_exceptions(futures)


@pytest.mark.parametrize("seed", [generate_random_seed()])
def test___single_task___get_set_float_and_string_properties___no_errors(
    task: Task,
    thread_pool_executor: ThreadPoolExecutor,
    multi_threading_test_devices: Sequence[Device],
    seed: int,
) -> None:
    random.seed(seed)
    num_channels = 2
    start_barrier = threading.Barrier(num_channels + 1)
    stop_semaphore = threading.Semaphore(0)
    for i in range(num_channels):
        task.ai_channels.add_ai_voltage_chan(
            multi_threading_test_devices[0].ai_physical_chans[i].name, min_val=-1.0, max_val=1.0
        )
    futures = [
        thread_pool_executor.submit(
            _get_set_property_thread_main,
            start_barrier,
            stop_semaphore,
            task.ai_channels[0],
            "ai_max",
            [1.0, 2.0, 5.0, 10.0],
        ),
        thread_pool_executor.submit(
            _get_set_property_thread_main,
            start_barrier,
            stop_semaphore,
            task.ai_channels[1],
            "description",
            ["ABC", "DEF", "GHI", "JKL"],
        ),
    ]

    start_barrier.wait(timeout=TIMEOUT)
    time.sleep(RUN_TIME)
    stop_semaphore.release(num_channels)

    concurrent.futures.wait(futures)
    _check_for_exceptions(futures)


@pytest.mark.parametrize("seed", [generate_random_seed()])
def test___multiple_tasks___get_set_float_and_string_properties___no_errors(
    generate_task: Callable[[], Task],
    thread_pool_executor: ThreadPoolExecutor,
    multi_threading_test_devices: Sequence[Device],
    seed: int,
) -> None:
    random.seed(seed)
    num_tasks = 2
    start_barrier = threading.Barrier(num_tasks + 1)
    stop_semaphore = threading.Semaphore(0)
    tasks = []
    futures = []
    for i in range(num_tasks):
        task = generate_task()
        channel = task.ai_channels.add_ai_voltage_chan(
            multi_threading_test_devices[i].ai_physical_chans[0].name, min_val=-1.0, max_val=1.0
        )
        tasks.append(task)
        if i % 2 == 0:
            future = thread_pool_executor.submit(
                _get_set_property_thread_main,
                start_barrier,
                stop_semaphore,
                channel,
                "ai_max",
                [1.0, 2.0, 5.0, 10.0],
            )
        else:
            future = thread_pool_executor.submit(
                _get_set_property_thread_main,
                start_barrier,
                stop_semaphore,
                channel,
                "description",
                ["ABC", "DEF", "GHI", "JKL"],
            )
        futures.append(future)

    start_barrier.wait(timeout=TIMEOUT)
    time.sleep(RUN_TIME)
    stop_semaphore.release(num_tasks)

    concurrent.futures.wait(futures)
    _check_for_exceptions(futures)


def _get_set_property_thread_main(
    start_barrier: Barrier,
    stop_semaphore: Semaphore,
    channel: AIChannel,
    property_name: str,
    property_values: list[Any],
) -> None:
    start_barrier.wait(timeout=TIMEOUT)
    while not stop_semaphore.acquire(timeout=0.0):
        value = random.choice(property_values)
        setattr(channel, property_name, value)
        assert getattr(channel, property_name) == value


def _check_for_exceptions(futures: Sequence[Future]) -> None:
    for future in futures:
        _ = future.result()


def test___shared_interpreter___run_multiple_acquisitions_with_events___callbacks_invoked(
    init_kwargs,
    multi_threading_test_devices: Sequence[Device],
    system: System,
):
    with ExitStack() as stack:
        tasks = [
            stack.enter_context(
                _create_ai_task_with_shared_interpreter(
                    init_kwargs, system, f"EventTask{i}", device.ai_physical_chans[0].name
                )
            )
            for i, device in enumerate(multi_threading_test_devices)
        ]
        samples_per_chan = [1000 for _ in tasks]
        _configure_timing(tasks, samples_per_chan)
        samples_acquired, done_events, done_statuses = _configure_events(tasks, samples_per_chan)

        for task in tasks:
            task.start()
        for i, task in enumerate(tasks):
            done_events[i].wait(timeout=10.0)
            task.stop()

        assert samples_acquired == samples_per_chan
        assert all(status == 0 for status in done_statuses)


def test___shared_interpreter___unregister_events_during_other_acquisitions_with_events___callbacks_invoked(
    init_kwargs,
    multi_threading_test_devices: Sequence[Device],
    system: System,
):
    with ExitStack() as stack:
        tasks = [
            stack.enter_context(
                _create_ai_task_with_shared_interpreter(
                    init_kwargs, system, f"EventTask{i}", device.ai_physical_chans[0].name
                )
            )
            for i, device in enumerate(multi_threading_test_devices)
        ]
        samples_per_chan = [1000 for _ in tasks]
        samples_per_chan[0] = 100
        _configure_timing(tasks, samples_per_chan)
        samples_acquired, done_events, done_statuses = _configure_events(tasks, samples_per_chan)

        for task in tasks:
            task.start()
        done_events[0].wait(timeout=10.0)
        tasks[0].stop()
        tasks[0].register_every_n_samples_acquired_into_buffer_event(100, None)
        tasks[0].register_done_event(None)
        for i in range(1, len(tasks)):
            done_events[i].wait(timeout=10.0)
            tasks[i].stop()

        assert samples_acquired == samples_per_chan
        assert all(status == 0 for status in done_statuses)


def _create_ai_task_with_shared_interpreter(
    init_kwargs, system: System, task_name: str, physical_channel: str
) -> Task:
    with Task(task_name, **init_kwargs) as task:
        task.ai_channels.add_ai_voltage_chan(physical_channel)
        task.save(overwrite_existing_task=True)

    persisted_task = system.tasks[task_name]
    task = persisted_task.load()
    assert task._interpreter is system._interpreter
    persisted_task.delete()
    return task


def _configure_timing(tasks: list[Task], samples_per_chan: list[int]) -> None:
    assert len(tasks) == len(samples_per_chan)

    for i in range(len(tasks)):
        tasks[i].timing.cfg_samp_clk_timing(
            rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=samples_per_chan[i]
        )


def _configure_events(
    tasks: list[Task], samples_per_chan: list[int]
) -> tuple[list[int], list[threading.Event], list[int]]:
    assert len(tasks) == len(samples_per_chan)

    samples_acquired = [0 for _ in tasks]
    done_events = [threading.Event() for _ in tasks]
    done_statuses = [0 for _ in tasks]

    for i in range(len(tasks)):

        def _every_n_samples_callback(
            i: int,
            task_handle: object,
            every_n_samples_event_type: int,
            number_of_samples: int,
            callback_data: object,
        ) -> int:
            samples_acquired[i] += len(tasks[i].read(number_of_samples))
            if samples_acquired[i] >= samples_per_chan[i]:
                done_events[i].set()
            return 0

        def _done_event_callback(
            i: int, task_handle: object, status: int, callback_data: object
        ) -> int:
            done_statuses[i] = status
            if status != 0:
                done_events[i].set()
            return 0

        tasks[i].register_every_n_samples_acquired_into_buffer_event(
            100, functools.partial(_every_n_samples_callback, i)
        )
        tasks[i].register_done_event(functools.partial(_done_event_callback, i))

    return samples_acquired, done_events, done_statuses
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/benchmark/__init__.py sha256=28f6fda61aaaee5df806e814f4e1300654b0f69d6de6ec4dd7342c8fe8bb2a0c bytes=43 -->
## FILE: tests/benchmark/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/benchmark/__init__.py`
- sha256: `28f6fda61aaaee5df806e814f4e1300654b0f69d6de6ec4dd7342c8fe8bb2a0c`
- bytes: 43

````python
"""Benchmarks for the nidaqmx package."""
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/benchmark/conftest.py sha256=d9adb61498411b2b526e2ae58c0921083b75f1254741f61e395a634f75779c00 bytes=6171 -->
## FILE: tests/benchmark/conftest.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/benchmark/conftest.py`
- sha256: `d9adb61498411b2b526e2ae58c0921083b75f1254741f61e395a634f75779c00`
- bytes: 6171

````python
"""Fixtures for benchmark tests."""

from __future__ import annotations

import pytest

from nidaqmx import Task
from nidaqmx.constants import (
    AcquisitionType,
    Edge,
    LineGrouping,
    ReadRelativeTo,
    TaskMode,
    WaveformAttributeMode,
)
from nidaqmx.system import Device, System
from tests.conftest import DeviceType, _device_by_product_type


_WAVEFORM_BENCHMARK_MODES = [
    WaveformAttributeMode.NONE,
    WaveformAttributeMode.TIMING,
    WaveformAttributeMode.TIMING | WaveformAttributeMode.EXTENDED_PROPERTIES,
]

_WAVEFORM_BENCHMARK_MODE_IDS = ["NONE", "TIMING", "ALL"]


def _configure_timing(task: Task, num_samples: int) -> None:
    task.timing.cfg_samp_clk_timing(
        rate=25000.0,
        active_edge=Edge.RISING,
        sample_mode=AcquisitionType.FINITE,
        samps_per_chan=num_samples * 2,
    )


def _start_input_task(task: Task) -> None:
    task.start()
    task.wait_until_done(timeout=10.0)
    task.in_stream.relative_to = ReadRelativeTo.FIRST_SAMPLE


def _commit_output_task(task: Task, num_samples: int) -> None:
    task.out_stream.output_buf_size = num_samples * 2
    task.control(TaskMode.TASK_COMMIT)
    task.out_stream.relative_to = ReadRelativeTo.FIRST_SAMPLE


def pytest_addoption(parser: pytest.Parser) -> None:
    """Add command line options to pytest."""
    parser.addoption("--device", action="store", default=None, help="Device name for benchmarks")


@pytest.fixture
def benchmark_device(system: System, request: pytest.FixtureRequest) -> Device:
    """Get device for benchmarking."""
    device: str | None = request.config.getoption("--device")
    if device is not None:
        return system.devices[device]

    return _device_by_product_type("PCIe-6363", DeviceType.ANY, system)


@pytest.fixture
def ai_benchmark_task(
    task: Task,
    benchmark_device: Device,
    request: pytest.FixtureRequest,
) -> Task:
    """Configure an AI task for benchmarking."""
    num_channels = request.node.callspec.params.get("num_channels", 1)
    num_samples = request.node.callspec.params.get("num_samples", 1)

    for chan in range(num_channels):
        task.ai_channels.add_ai_voltage_chan(
            benchmark_device.ai_physical_chans[chan].name,
            min_val=-5.0,
            max_val=5.0,
        )

    _configure_timing(task, num_samples)
    _start_input_task(task)

    return task


@pytest.fixture
def ao_benchmark_task(
    task: Task,
    real_x_series_multiplexed_device: Device,
    request: pytest.FixtureRequest,
) -> Task:
    """Configure a hardware-timed buffered AO task for benchmarking."""
    num_channels = request.node.callspec.params.get("num_channels", 1)
    num_samples = request.node.callspec.params.get("num_samples", 1)

    for chan in range(num_channels):
        task.ao_channels.add_ao_voltage_chan(
            real_x_series_multiplexed_device.ao_physical_chans[chan].name,
            min_val=-10.0,
            max_val=10.0,
        )

    _configure_timing(task, num_samples)
    _commit_output_task(task, num_samples)

    return task


@pytest.fixture
def di_lines_benchmark_task(
    task: Task,
    benchmark_device: Device,
    request: pytest.FixtureRequest,
) -> Task:
    """Configure a hardware-timed buffered DI task for benchmarking."""
    num_channels = request.node.callspec.params.get("num_channels", 1)
    num_samples = request.node.callspec.params.get("num_samples", 1)
    num_lines = request.node.callspec.params.get("num_lines", 1)

    for chan in range(num_channels):
        line_names = [
            chan.name
            for chan in benchmark_device.di_lines[chan * num_lines : (chan + 1) * num_lines]
        ]
        physical_channel_string = ",".join(line_names)
        task.di_channels.add_di_chan(
            physical_channel_string, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
        )

    _configure_timing(task, num_samples)
    _start_input_task(task)

    return task


@pytest.fixture
def di_port32_benchmark_task(
    task: Task,
    benchmark_device: Device,
    request: pytest.FixtureRequest,
) -> Task:
    """Configure a hardware-timed buffered DI task for benchmarking."""
    num_samples = request.node.callspec.params.get("num_samples", 1)

    # port 0 is the only port that supports buffered operations
    task.di_channels.add_di_chan(
        benchmark_device.di_ports[0].name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )

    _configure_timing(task, num_samples)
    _start_input_task(task)

    return task


@pytest.fixture
def do_lines_benchmark_task(
    task: Task,
    benchmark_device: Device,
    request: pytest.FixtureRequest,
) -> Task:
    """Configure a hardware-timed buffered DO task for benchmarking."""
    num_channels = request.node.callspec.params.get("num_channels", 1)
    num_samples = request.node.callspec.params.get("num_samples", 1)
    num_lines = request.node.callspec.params.get("num_lines", 1)

    for chan in range(num_channels):
        line_names = [
            chan.name
            for chan in benchmark_device.do_lines[chan * num_lines : (chan + 1) * num_lines]
        ]
        physical_channel_string = ",".join(line_names)
        task.do_channels.add_do_chan(
            physical_channel_string, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
        )

    _configure_timing(task, num_samples)
    _commit_output_task(task, num_samples)

    return task


@pytest.fixture
def do_port32_benchmark_task(
    task: Task,
    benchmark_device: Device,
    request: pytest.FixtureRequest,
) -> Task:
    """Configure a hardware-timed buffered DO task for benchmarking."""
    num_samples = request.node.callspec.params.get("num_samples", 1)

    # port 0 is the only port that supports buffered operations
    task.do_channels.add_do_chan(
        benchmark_device.do_ports[0].name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )

    _configure_timing(task, num_samples)
    _commit_output_task(task, num_samples)

    return task
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/benchmark/test_analog_stream_readers.py sha256=1a0fbacb67adddb1ca84cd8da1f37d39a0f0b98221665120d1841287ee73fb69 bytes=4941 -->
## FILE: tests/benchmark/test_analog_stream_readers.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/benchmark/test_analog_stream_readers.py`
- sha256: `1a0fbacb67adddb1ca84cd8da1f37d39a0f0b98221665120d1841287ee73fb69`
- bytes: 4941

````python
from __future__ import annotations

import math

import numpy
import pytest
from nitypes.waveform import AnalogWaveform
from pytest_benchmark.fixture import BenchmarkFixture

from nidaqmx import Task
from nidaqmx.constants import READ_ALL_AVAILABLE, WaveformAttributeMode
from nidaqmx.stream_readers._analog_multi_channel_reader import AnalogMultiChannelReader
from nidaqmx.stream_readers._analog_single_channel_reader import (
    AnalogSingleChannelReader,
)
from tests.benchmark.conftest import (
    _WAVEFORM_BENCHMARK_MODE_IDS,
    _WAVEFORM_BENCHMARK_MODES,
)


@pytest.mark.benchmark(group="analog_readers")
def test___analog_single_channel_reader___read_one_sample(
    benchmark: BenchmarkFixture, ai_benchmark_task: Task
) -> None:
    reader = AnalogSingleChannelReader(ai_benchmark_task.in_stream)

    benchmark(reader.read_one_sample)


@pytest.mark.benchmark(group="analog_readers")
@pytest.mark.parametrize("num_samples", [1, 1000])
def test___analog_single_channel_reader___read_many_sample(
    benchmark: BenchmarkFixture, ai_benchmark_task: Task, num_samples: int
) -> None:
    reader = AnalogSingleChannelReader(ai_benchmark_task.in_stream)
    data = numpy.full(num_samples, math.inf, dtype=numpy.float64)

    benchmark(reader.read_many_sample, data, num_samples)


@pytest.mark.benchmark(group="analog_readers")
@pytest.mark.parametrize("num_samples", [1, 1000])
def test___analog_single_channel_reader___read_all_available(
    benchmark: BenchmarkFixture, ai_benchmark_task: Task, num_samples: int
) -> None:
    reader = AnalogSingleChannelReader(ai_benchmark_task.in_stream)
    # This test reads the whole buffer, which is 2x num_samples.
    data = numpy.full(num_samples * 2, math.inf, dtype=numpy.float64)

    benchmark(reader.read_many_sample, data, READ_ALL_AVAILABLE)


@pytest.mark.benchmark(group="analog_readers")
@pytest.mark.parametrize("num_samples", [1, 1000])
@pytest.mark.parametrize(
    "waveform_attribute_mode", _WAVEFORM_BENCHMARK_MODES, ids=_WAVEFORM_BENCHMARK_MODE_IDS
)
def test___analog_single_channel_reader___read_waveform(
    benchmark: BenchmarkFixture,
    ai_benchmark_task: Task,
    num_samples: int,
    waveform_attribute_mode: WaveformAttributeMode,
) -> None:
    ai_benchmark_task.in_stream.waveform_attribute_mode = waveform_attribute_mode
    reader = AnalogSingleChannelReader(ai_benchmark_task.in_stream)
    waveform = AnalogWaveform(num_samples)

    benchmark(reader.read_waveform, waveform, num_samples)


@pytest.mark.benchmark(group="analog_readers")
@pytest.mark.parametrize("num_channels", [1, 2, 8])
def test___analog_multi_channel_reader___read_one_sample(
    benchmark: BenchmarkFixture, ai_benchmark_task: Task, num_channels: int
) -> None:
    reader = AnalogMultiChannelReader(ai_benchmark_task.in_stream)
    data = numpy.full(num_channels, math.inf, dtype=numpy.float64)

    benchmark(reader.read_one_sample, data)


@pytest.mark.benchmark(group="analog_readers")
@pytest.mark.parametrize("num_channels", [1, 2, 8])
@pytest.mark.parametrize("num_samples", [1, 1000])
def test___analog_multi_channel_reader___read_many_sample(
    benchmark: BenchmarkFixture, ai_benchmark_task: Task, num_channels: int, num_samples: int
) -> None:
    reader = AnalogMultiChannelReader(ai_benchmark_task.in_stream)
    data = numpy.full((num_channels, num_samples), math.inf, dtype=numpy.float64)

    benchmark(reader.read_many_sample, data, num_samples)


@pytest.mark.benchmark(group="analog_readers")
@pytest.mark.parametrize("num_channels", [1, 2, 8])
@pytest.mark.parametrize("num_samples", [1, 1000])
def test___analog_multi_channel_reader___read_all_available(
    benchmark: BenchmarkFixture, ai_benchmark_task: Task, num_channels: int, num_samples: int
) -> None:
    reader = AnalogMultiChannelReader(ai_benchmark_task.in_stream)
    # This test reads the whole buffer, which is 2x num_samples.
    data = numpy.full((num_channels, num_samples * 2), math.inf, dtype=numpy.float64)

    benchmark(reader.read_many_sample, data, READ_ALL_AVAILABLE)


@pytest.mark.benchmark(group="analog_readers")
@pytest.mark.parametrize("num_channels", [1, 2, 8])
@pytest.mark.parametrize("num_samples", [1, 1000])
@pytest.mark.parametrize(
    "waveform_attribute_mode", _WAVEFORM_BENCHMARK_MODES, ids=_WAVEFORM_BENCHMARK_MODE_IDS
)
def test___analog_multi_channel_reader___read_waveform(
    benchmark: BenchmarkFixture,
    ai_benchmark_task: Task,
    num_channels: int,
    num_samples: int,
    waveform_attribute_mode: WaveformAttributeMode,
) -> None:
    ai_benchmark_task.in_stream.waveform_attribute_mode = waveform_attribute_mode
    reader = AnalogMultiChannelReader(ai_benchmark_task.in_stream)
    waveforms = [AnalogWaveform(num_samples) for _ in range(num_channels)]

    benchmark(reader.read_waveforms, waveforms, num_samples)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/benchmark/test_analog_stream_writers.py sha256=397b76f761b873b8d766f5a6fa3b604a2279bee8baf633ab53bb57f2ab548997 bytes=3239 -->
## FILE: tests/benchmark/test_analog_stream_writers.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/benchmark/test_analog_stream_writers.py`
- sha256: `397b76f761b873b8d766f5a6fa3b604a2279bee8baf633ab53bb57f2ab548997`
- bytes: 3239

````python
from __future__ import annotations

import numpy
import pytest
from nitypes.waveform import AnalogWaveform
from pytest_benchmark.fixture import BenchmarkFixture

import nidaqmx
from nidaqmx.stream_writers._analog_multi_channel_writer import AnalogMultiChannelWriter
from nidaqmx.stream_writers._analog_single_channel_writer import (
    AnalogSingleChannelWriter,
)


@pytest.mark.benchmark(group="analog_writers")
def test___analog_single_channel_writer___write_one_sample(
    benchmark: BenchmarkFixture,
    ao_benchmark_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_benchmark_task.out_stream, auto_start=False)

    benchmark(writer.write_one_sample, 1.0)


@pytest.mark.benchmark(group="analog_writers")
@pytest.mark.parametrize("num_samples", [1, 1000])
def test___analog_single_channel_writer___write_many_sample(
    benchmark: BenchmarkFixture,
    ao_benchmark_task: nidaqmx.Task,
    num_samples: int,
) -> None:
    writer = AnalogSingleChannelWriter(ao_benchmark_task.out_stream, auto_start=False)
    data = numpy.linspace(0.0, 1.0, num=num_samples, dtype=numpy.float64)

    benchmark(writer.write_many_sample, data)


@pytest.mark.benchmark(group="analog_writers")
@pytest.mark.parametrize("num_samples", [1, 1000])
def test___analog_single_channel_writer___write_waveform(
    benchmark: BenchmarkFixture,
    ao_benchmark_task: nidaqmx.Task,
    num_samples: int,
) -> None:
    writer = AnalogSingleChannelWriter(ao_benchmark_task.out_stream, auto_start=False)
    waveform = AnalogWaveform(num_samples)

    benchmark(writer.write_waveform, waveform)


@pytest.mark.benchmark(group="analog_writers")
@pytest.mark.parametrize("num_channels", [1, 2])
def test___analog_multi_channel_writer___write_one_sample(
    benchmark: BenchmarkFixture,
    ao_benchmark_task: nidaqmx.Task,
    num_channels: int,
) -> None:
    writer = AnalogMultiChannelWriter(ao_benchmark_task.out_stream, auto_start=False)
    data = numpy.asarray([1.0] * num_channels, dtype=numpy.float64)

    benchmark(writer.write_one_sample, data)


@pytest.mark.benchmark(group="analog_writers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.parametrize("num_samples", [1, 1000])
def test___analog_multi_channel_writer___write_many_sample(
    benchmark: BenchmarkFixture,
    ao_benchmark_task: nidaqmx.Task,
    num_channels: int,
    num_samples: int,
) -> None:
    writer = AnalogMultiChannelWriter(ao_benchmark_task.out_stream, auto_start=False)
    data = numpy.full((num_channels, num_samples), 1.0, dtype=numpy.float64)

    benchmark(writer.write_many_sample, data)


@pytest.mark.benchmark(group="analog_writers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.parametrize("num_samples", [1, 1000])
def test___analog_multi_channel_writer___write_waveform(
    benchmark: BenchmarkFixture,
    ao_benchmark_task: nidaqmx.Task,
    num_channels: int,
    num_samples: int,
) -> None:
    writer = AnalogMultiChannelWriter(ao_benchmark_task.out_stream, auto_start=False)
    waveforms = [AnalogWaveform(num_samples) for _ in range(num_channels)]

    benchmark(writer.write_waveforms, waveforms)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/benchmark/test_digital_stream_readers.py sha256=27060ea114904d61563048dacfda5979e3ed02cc5755924025139e27cd047fbe bytes=5491 -->
## FILE: tests/benchmark/test_digital_stream_readers.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/benchmark/test_digital_stream_readers.py`
- sha256: `27060ea114904d61563048dacfda5979e3ed02cc5755924025139e27cd047fbe`
- bytes: 5491

````python
from __future__ import annotations

import numpy
import pytest
from nitypes.waveform import DigitalWaveform
from pytest_benchmark.fixture import BenchmarkFixture

import nidaqmx
from nidaqmx.stream_readers._digital_multi_channel_reader import (
    DigitalMultiChannelReader,
)
from nidaqmx.stream_readers._digital_single_channel_reader import (
    DigitalSingleChannelReader,
)


@pytest.mark.benchmark(group="digital_readers")
def test___digital_single_channel_reader___read_one_sample_one_line(
    benchmark: BenchmarkFixture,
    di_lines_benchmark_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_lines_benchmark_task.in_stream)

    benchmark(reader.read_one_sample_one_line)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_lines", [1, 2, 8])
def test___digital_single_channel_reader___read_one_sample_multi_line(
    benchmark: BenchmarkFixture,
    di_lines_benchmark_task: nidaqmx.Task,
    num_lines: int,
) -> None:
    reader = DigitalSingleChannelReader(di_lines_benchmark_task.in_stream)
    data = numpy.full(num_lines, False, dtype=numpy.bool_)

    benchmark(reader.read_one_sample_multi_line, data)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_samples", [1, 100])
def test___digital_single_channel_reader___read_many_sample_port_uint32(
    benchmark: BenchmarkFixture,
    di_port32_benchmark_task: nidaqmx.Task,
    num_samples: int,
) -> None:
    reader = DigitalSingleChannelReader(di_port32_benchmark_task.in_stream)
    data = numpy.full(num_samples, numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)

    benchmark(reader.read_many_sample_port_uint32, data, num_samples)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.parametrize("num_lines", [1, 2, 8])
def test___digital_single_channel_reader___read_waveform_lines(
    benchmark: BenchmarkFixture,
    di_lines_benchmark_task: nidaqmx.Task,
    num_samples: int,
    num_lines: int,
) -> None:
    reader = DigitalSingleChannelReader(di_lines_benchmark_task.in_stream)
    waveform = DigitalWaveform(num_samples, num_lines)

    benchmark(reader.read_waveform, waveform, num_samples)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_samples", [1, 100])
def test___digital_single_channel_reader___read_waveform_port(
    benchmark: BenchmarkFixture,
    di_port32_benchmark_task: nidaqmx.Task,
    num_samples: int,
) -> None:
    reader = DigitalSingleChannelReader(di_port32_benchmark_task.in_stream)
    waveform = DigitalWaveform(num_samples, signal_count=32)

    benchmark(reader.read_waveform, waveform, num_samples)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_channels", [1, 2])
def test___digital_multi_channel_reader___read_one_sample_one_line(
    benchmark: BenchmarkFixture,
    di_lines_benchmark_task: nidaqmx.Task,
    num_channels: int,
) -> None:
    reader = DigitalMultiChannelReader(di_lines_benchmark_task.in_stream)
    data = numpy.full(num_channels, False, dtype=numpy.bool_)

    benchmark(reader.read_one_sample_one_line, data)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.parametrize("num_lines", [1, 2, 8])
def test___digital_multi_channel_reader___read_one_sample_multi_line(
    benchmark: BenchmarkFixture,
    di_lines_benchmark_task: nidaqmx.Task,
    num_channels: int,
    num_lines: int,
) -> None:
    reader = DigitalMultiChannelReader(di_lines_benchmark_task.in_stream)
    data = numpy.full((num_channels, num_lines), False, dtype=numpy.bool_)

    benchmark(reader.read_one_sample_multi_line, data)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_samples", [1, 100])
def test___digital_multi_channel_reader___read_many_sample_port_uint32(
    benchmark: BenchmarkFixture,
    di_port32_benchmark_task: nidaqmx.Task,
    num_samples: int,
) -> None:
    reader = DigitalMultiChannelReader(di_port32_benchmark_task.in_stream)
    data = numpy.full((1, num_samples), numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)

    benchmark(reader.read_many_sample_port_uint32, data, num_samples)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.parametrize("num_lines", [1, 2, 8])
def test___digital_multi_channel_reader___read_waveform_lines(
    benchmark: BenchmarkFixture,
    di_lines_benchmark_task: nidaqmx.Task,
    num_channels: int,
    num_samples: int,
    num_lines: int,
) -> None:
    reader = DigitalMultiChannelReader(di_lines_benchmark_task.in_stream)
    waveforms = [DigitalWaveform(num_samples, num_lines) for _ in range(num_channels)]

    benchmark(reader.read_waveforms, waveforms, num_samples)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_samples", [1, 100])
def test___digital_multi_channel_reader___read_waveform_port(
    benchmark: BenchmarkFixture,
    di_port32_benchmark_task: nidaqmx.Task,
    num_samples: int,
) -> None:
    reader = DigitalMultiChannelReader(di_port32_benchmark_task.in_stream)
    waveforms = [DigitalWaveform(num_samples, signal_count=32)]

    benchmark(reader.read_waveforms, waveforms, num_samples)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/benchmark/test_digital_stream_writers.py sha256=122437beae0ba3924567e73ac5e3bfc987f6f27d2e88ec29d386d8efa3de743e bytes=5650 -->
## FILE: tests/benchmark/test_digital_stream_writers.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/benchmark/test_digital_stream_writers.py`
- sha256: `122437beae0ba3924567e73ac5e3bfc987f6f27d2e88ec29d386d8efa3de743e`
- bytes: 5650

````python
from __future__ import annotations

import numpy
import pytest
from nitypes.waveform import DigitalWaveform
from pytest_benchmark.fixture import BenchmarkFixture

import nidaqmx
from nidaqmx.stream_writers._digital_multi_channel_writer import (
    DigitalMultiChannelWriter,
)
from nidaqmx.stream_writers._digital_single_channel_writer import (
    DigitalSingleChannelWriter,
)


@pytest.mark.benchmark(group="digital_writers")
def test___digital_single_channel_writer___write_one_sample_one_line(
    benchmark: BenchmarkFixture,
    do_lines_benchmark_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_lines_benchmark_task.out_stream, auto_start=False)

    benchmark(writer.write_one_sample_one_line, True)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_lines", [1, 2, 8])
def test___digital_single_channel_writer___write_one_sample_multi_line(
    benchmark: BenchmarkFixture,
    do_lines_benchmark_task: nidaqmx.Task,
    num_lines: int,
) -> None:
    writer = DigitalSingleChannelWriter(do_lines_benchmark_task.out_stream, auto_start=False)
    data = numpy.full(num_lines, True, dtype=numpy.bool_)

    benchmark(writer.write_one_sample_multi_line, data)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_samples", [1, 100])
def test___digital_single_channel_writer___write_many_sample_port_uint32(
    benchmark: BenchmarkFixture,
    do_port32_benchmark_task: nidaqmx.Task,
    num_samples: int,
) -> None:
    writer = DigitalSingleChannelWriter(do_port32_benchmark_task.out_stream, auto_start=False)
    data = numpy.full(num_samples, numpy.uint32(1), dtype=numpy.uint32)

    benchmark(writer.write_many_sample_port_uint32, data)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.parametrize("num_lines", [1, 2, 8])
def test___digital_single_channel_writer___write_waveform_lines(
    benchmark: BenchmarkFixture,
    do_lines_benchmark_task: nidaqmx.Task,
    num_samples: int,
    num_lines: int,
) -> None:
    writer = DigitalSingleChannelWriter(do_lines_benchmark_task.out_stream, auto_start=False)
    waveform = DigitalWaveform(num_samples, num_lines)

    benchmark(writer.write_waveform, waveform)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_samples", [1, 100])
def test___digital_single_channel_writer___write_waveform_port(
    benchmark: BenchmarkFixture,
    do_port32_benchmark_task: nidaqmx.Task,
    num_samples: int,
) -> None:
    writer = DigitalSingleChannelWriter(do_port32_benchmark_task.out_stream, auto_start=False)
    waveform = DigitalWaveform(num_samples, signal_count=32)

    benchmark(writer.write_waveform, waveform)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_channels", [1, 2])
def test___digital_multi_channel_writer___write_one_sample_one_line(
    benchmark: BenchmarkFixture,
    do_lines_benchmark_task: nidaqmx.Task,
    num_channels: int,
) -> None:
    writer = DigitalMultiChannelWriter(do_lines_benchmark_task.out_stream, auto_start=False)
    data = numpy.full(num_channels, False, dtype=numpy.bool_)

    benchmark(writer.write_one_sample_one_line, data)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.parametrize("num_lines", [1, 2, 8])
def test___digital_multi_channel_writer___write_one_sample_multi_line(
    benchmark: BenchmarkFixture,
    do_lines_benchmark_task: nidaqmx.Task,
    num_channels: int,
    num_lines: int,
) -> None:
    writer = DigitalMultiChannelWriter(do_lines_benchmark_task.out_stream, auto_start=False)
    data = numpy.full((num_channels, num_lines), False, dtype=numpy.bool_)

    benchmark(writer.write_one_sample_multi_line, data)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_samples", [1, 100])
def test___digital_multi_channel_writer___write_many_sample_port_uint32(
    benchmark: BenchmarkFixture,
    do_port32_benchmark_task: nidaqmx.Task,
    num_samples: int,
) -> None:
    writer = DigitalMultiChannelWriter(do_port32_benchmark_task.in_stream, auto_start=False)
    data = numpy.full((1, num_samples), numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)

    benchmark(writer.write_many_sample_port_uint32, data, num_samples)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.parametrize("num_lines", [1, 2, 8])
def test___digital_multi_channel_writer___write_waveform_lines(
    benchmark: BenchmarkFixture,
    do_lines_benchmark_task: nidaqmx.Task,
    num_channels: int,
    num_samples: int,
    num_lines: int,
) -> None:
    writer = DigitalMultiChannelWriter(do_lines_benchmark_task.in_stream, auto_start=False)
    waveforms = [DigitalWaveform(num_samples, num_lines) for _ in range(num_channels)]

    benchmark(writer.write_waveforms, waveforms, num_samples)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_samples", [1, 100])
def test___digital_multi_channel_writer___write_waveform_port(
    benchmark: BenchmarkFixture,
    do_port32_benchmark_task: nidaqmx.Task,
    num_samples: int,
) -> None:
    writer = DigitalMultiChannelWriter(do_port32_benchmark_task.in_stream, auto_start=False)
    waveforms = [DigitalWaveform(num_samples, signal_count=32)]

    benchmark(writer.write_waveforms, waveforms, num_samples)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/benchmark/test_task.py sha256=2d39152541879613fc4c4b8fbb133dedf1efcd5fe6aba268f0cbd16a2525ffaf bytes=6516 -->
## FILE: tests/benchmark/test_task.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/benchmark/test_task.py`
- sha256: `2d39152541879613fc4c4b8fbb133dedf1efcd5fe6aba268f0cbd16a2525ffaf`
- bytes: 6516

````python
from __future__ import annotations

from typing import Any

import numpy
import pytest
from nitypes.waveform import AnalogWaveform, DigitalWaveform
from pytest_benchmark.fixture import BenchmarkFixture

from nidaqmx import Task
from nidaqmx.constants import WaveformAttributeMode
from tests.benchmark.conftest import (
    _WAVEFORM_BENCHMARK_MODE_IDS,
    _WAVEFORM_BENCHMARK_MODES,
)


def _create_analog_data(num_channels, num_samples):
    if num_channels == 1:
        if num_samples == 1:
            return 1.0
        return numpy.full((num_samples), 1.0, numpy.float64)
    else:
        return numpy.full((num_channels, num_samples), 1.0, numpy.float64)


def _create_digital_data(num_channels, num_samples, num_lines):
    if num_lines == 1:
        dtype: Any = numpy.bool_
        value: Any = True
    else:
        dtype = numpy.uint32
        value = 1

    if num_channels == 1:
        if num_samples == 1:
            return value
        return numpy.full((num_samples), value, dtype)
    else:
        return numpy.full((num_channels, num_samples), value, dtype)


@pytest.mark.benchmark(group="analog_readers")
@pytest.mark.parametrize("num_channels", [1, 2, 8])
@pytest.mark.parametrize("num_samples", [1, 1000])
def test___task___read_analog(
    benchmark: BenchmarkFixture, ai_benchmark_task: Task, num_channels: int, num_samples: int
) -> None:
    benchmark(ai_benchmark_task.read, num_samples)


@pytest.mark.benchmark(group="analog_readers")
@pytest.mark.parametrize("num_channels", [1, 2, 8])
@pytest.mark.parametrize("num_samples", [1, 1000])
@pytest.mark.parametrize(
    "waveform_attribute_mode", _WAVEFORM_BENCHMARK_MODES, ids=_WAVEFORM_BENCHMARK_MODE_IDS
)
def test___task___read_analog_waveform(
    benchmark: BenchmarkFixture,
    ai_benchmark_task: Task,
    num_channels: int,
    num_samples: int,
    waveform_attribute_mode: WaveformAttributeMode,
) -> None:
    ai_benchmark_task.in_stream.waveform_attribute_mode = waveform_attribute_mode
    benchmark(ai_benchmark_task.read_waveform, num_samples)


@pytest.mark.benchmark(group="analog_writers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.parametrize("num_samples", [1, 1000])
def test___task___write_analog(
    benchmark: BenchmarkFixture,
    ao_benchmark_task: Task,
    num_channels: int,
    num_samples: int,
) -> None:
    data = _create_analog_data(num_channels, num_samples)
    ao_benchmark_task.write(data, auto_start=False)
    benchmark(ao_benchmark_task.write, data, auto_start=False)


@pytest.mark.benchmark(group="analog_writers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.parametrize("num_samples", [1, 1000])
def test___task___write_analog_waveform(
    benchmark: BenchmarkFixture,
    ao_benchmark_task: Task,
    num_channels: int,
    num_samples: int,
) -> None:
    waveforms = [AnalogWaveform(num_samples) for _ in range(num_channels)]

    benchmark(ao_benchmark_task.write_waveform, waveforms, auto_start=False)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.parametrize("num_lines", [1, 2, 8])
def test___task___read_digital_lines(
    benchmark: BenchmarkFixture,
    di_lines_benchmark_task: Task,
    num_channels: int,
    num_samples: int,
    num_lines: int,
) -> None:
    benchmark(di_lines_benchmark_task.read, num_samples)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_samples", [1, 100])
def test___task___read_digital_port(
    benchmark: BenchmarkFixture,
    di_port32_benchmark_task: Task,
    num_samples: int,
) -> None:
    benchmark(di_port32_benchmark_task.read, num_samples)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.parametrize("num_lines", [1, 2, 8])
def test___task___read_digital_lines_waveform(
    benchmark: BenchmarkFixture,
    di_lines_benchmark_task: Task,
    num_channels: int,
    num_samples: int,
    num_lines: int,
) -> None:
    benchmark(di_lines_benchmark_task.read_waveform, num_samples)


@pytest.mark.benchmark(group="digital_readers")
@pytest.mark.parametrize("num_samples", [1, 100])
def test___task___read_digital_port_waveform(
    benchmark: BenchmarkFixture,
    di_port32_benchmark_task: Task,
    num_samples: int,
) -> None:
    benchmark(di_port32_benchmark_task.read_waveform, num_samples)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.parametrize("num_lines", [1, 2, 8])
def test___task___write_digital_lines(
    benchmark: BenchmarkFixture,
    do_lines_benchmark_task: Task,
    num_channels: int,
    num_samples: int,
    num_lines: int,
) -> None:
    data = _create_digital_data(num_channels, num_samples, num_lines)
    benchmark(do_lines_benchmark_task.write, data, auto_start=False)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_samples", [1, 100])
def test___task___write_digital_port(
    benchmark: BenchmarkFixture,
    do_port32_benchmark_task: Task,
    num_samples: int,
) -> None:
    data = _create_digital_data(1, num_samples, 32)
    benchmark(do_port32_benchmark_task.write, data, auto_start=False)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_channels", [1, 2])
@pytest.mark.parametrize("num_samples", [1, 100])
@pytest.mark.parametrize("num_lines", [1, 2, 8])
def test___task___write_digital_lines_waveform(
    benchmark: BenchmarkFixture,
    do_lines_benchmark_task: Task,
    num_channels: int,
    num_samples: int,
    num_lines: int,
) -> None:
    waveforms = [DigitalWaveform(num_samples, num_lines) for _ in range(num_channels)]
    benchmark(do_lines_benchmark_task.write_waveform, waveforms, auto_start=False)


@pytest.mark.benchmark(group="digital_writers")
@pytest.mark.parametrize("num_samples", [1, 100])
def test___task___write_digital_port_waveform(
    benchmark: BenchmarkFixture,
    do_port32_benchmark_task: Task,
    num_samples: int,
) -> None:
    waveforms = [DigitalWaveform(num_samples, signal_count=32)]
    benchmark(do_port32_benchmark_task.write_waveform, waveforms, auto_start=False)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/__init__.py sha256=86f7e4d2070e5bddb1675e9476e1d10b38afa8ecb647496c8d7096922e23e709 bytes=48 -->
## FILE: tests/component/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/__init__.py`
- sha256: `86f7e4d2070e5bddb1675e9476e1d10b38afa8ecb647496c8d7096922e23e709`
- bytes: 48

````python
"""Component tests for the nidaqmx package."""
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/_analog_utils.py sha256=b6bb9f50ca4c723616901e3017e6e2b3b6ae9be438ef9a5619f4b4b38bcb508a bytes=8458 -->
## FILE: tests/component/_analog_utils.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/_analog_utils.py`
- sha256: `b6bb9f50ca4c723616901e3017e6e2b3b6ae9be438ef9a5619f4b4b38bcb508a`
- bytes: 8458

````python
"""Shared utilities for analog component tests."""

from __future__ import annotations

from typing import Any

import numpy as np
import pytest
from nitypes.waveform import AnalogWaveform, LinearScaleMode

import nidaqmx
import nidaqmx.system


# Simulated DAQ voltage data is a noisy sine wave within the range of the minimum and maximum values
# of the virtual channel. We can leverage this behavior to validate we get the correct data from
# the Python bindings.
def _get_voltage_offset_for_chan(chan_index: int) -> float:
    return float(chan_index + 1)


def _get_voltage_setpoint_for_chan(chan_index: int) -> float:
    return float(chan_index + 1)


def _get_current_setpoint_for_chan(chan_index: int) -> float:
    return float(chan_index + 1)


def _get_expected_voltage_for_chan(chan_index: int) -> float:
    return float(chan_index + 1)


def _volts_to_codes(volts: float, max_code: int = 32767, max_voltage: float = 10.0) -> int:
    return int(volts * max_code / max_voltage)


def _pwr_volts_to_codes(volts: float, codes_per_volt: int = 4096) -> int:
    return int(volts * codes_per_volt)


def _pwr_current_to_codes(current: float, codes_per_amp: int = 8192) -> int:
    return int(current * codes_per_amp)


def _get_voltage_code_setpoint_for_chan(chan_index: int) -> int:
    return _pwr_volts_to_codes(_get_voltage_setpoint_for_chan(chan_index))


def _get_current_code_setpoint_for_chan(chan_index: int) -> int:
    return _pwr_current_to_codes(_get_current_setpoint_for_chan(chan_index))


# Note: Since we only use positive voltages, this works fine for both signed and unsigned reads.
def _get_voltage_code_offset_for_chan(chan_index: int) -> int:
    voltage_limits = _get_voltage_offset_for_chan(chan_index)
    return _volts_to_codes(voltage_limits)


def _create_constant_waveform(num_samples: int) -> AnalogWaveform:
    samples = np.full(num_samples, 1, dtype=np.float64)
    return AnalogWaveform.from_array_1d(samples)


def _create_linear_ramp_waveform(
    num_samples: int, start_val: float, end_val: float
) -> AnalogWaveform:
    samples = np.linspace(start_val, end_val, num_samples, dtype=np.float64)
    return AnalogWaveform.from_array_1d(samples)


def _create_scaled_int32_ramp_waveform(num_samples: int) -> AnalogWaveform:
    samples = np.arange(0, num_samples, dtype=np.int32)
    return AnalogWaveform.from_array_1d(samples, scale_mode=LinearScaleMode(gain=0.02, offset=0.2))


def _create_float32_ramp_waveform(
    num_samples: int, start_val: float, end_val: float
) -> AnalogWaveform:
    samples = np.linspace(start_val, end_val, num_samples, dtype=np.float32)
    return AnalogWaveform.from_array_1d(samples)


def _create_non_contiguous_waveform(
    num_samples: int, start_val: float, end_val: float
) -> AnalogWaveform:
    larger_array_size = num_samples * 2
    large_samples = np.linspace(start_val, end_val, larger_array_size, dtype=np.float64)
    non_contiguous_samples = large_samples[::2]
    waveform = AnalogWaveform(sample_count=num_samples, raw_data=non_contiguous_samples)
    assert not waveform.raw_data.flags.c_contiguous
    assert waveform.sample_count == num_samples
    return waveform


def _setup_synchronized_waveform_tasks(
    generate_task,
    device: nidaqmx.system.Device,
    num_samples: int,
    sample_rate: float,
    voltage_range: tuple[float, float] = (-5.0, 5.0),
    chan_index: int = 0,
) -> tuple[nidaqmx.Task, nidaqmx.Task, nidaqmx.Task, str]:
    """Set up synchronized AO, AI, and sample clock tasks for waveform testing.

    Returns:
        tuple: (ao_task, ai_task, sample_clk_task, sample_clk_terminal)
    """
    from nidaqmx import constants

    ao_task = generate_task()
    ai_task = generate_task()
    sample_clk_task = generate_task()

    min_voltage, max_voltage = voltage_range

    # Set up sample clock task
    sample_clk_task.co_channels.add_co_pulse_chan_freq(f"{device.name}/ctr0", freq=sample_rate)
    sample_clk_task.timing.cfg_implicit_timing(samps_per_chan=num_samples)
    sample_clk_task.control(constants.TaskMode.TASK_COMMIT)

    sample_clk_terminal = f"/{device.name}/Ctr0InternalOutput"

    # Set up AO task
    ao_task.ao_channels.add_ao_voltage_chan(
        device.ao_physical_chans[chan_index].name,
        min_val=min_voltage,
        max_val=max_voltage,
    )
    ao_task.timing.cfg_samp_clk_timing(
        rate=sample_rate,
        source=sample_clk_terminal,
        active_edge=constants.Edge.RISING,
        samps_per_chan=num_samples,
    )

    # Set up AI task for loopback
    ai_task.ai_channels.add_ai_voltage_chan(
        f"{device.name}/_ao{chan_index}_vs_aognd",
        min_val=min_voltage,
        max_val=max_voltage,
    )
    ai_task.timing.cfg_samp_clk_timing(
        rate=sample_rate,
        source=sample_clk_terminal,
        active_edge=constants.Edge.FALLING,
        samps_per_chan=num_samples,
    )

    return ao_task, ai_task, sample_clk_task, sample_clk_terminal


def _setup_synchronized_multi_channel_waveform_tasks(
    generate_task,
    device: nidaqmx.system.Device,
    num_channels: int,
    num_samples: int,
    sample_rate: float,
    voltage_range: tuple[float, float] = (-5.0, 5.0),
) -> tuple[nidaqmx.Task, nidaqmx.Task, nidaqmx.Task, str]:
    """Set up synchronized multi-channel AO, AI, and sample clock tasks for waveform testing.

    Returns:
        tuple: (ao_task, ai_task, sample_clk_task, sample_clk_terminal)
    """
    from nidaqmx import constants

    ao_task = generate_task()
    ai_task = generate_task()
    sample_clk_task = generate_task()

    min_voltage, max_voltage = voltage_range

    # Set up sample clock task
    sample_clk_task.co_channels.add_co_pulse_chan_freq(f"{device.name}/ctr0", freq=sample_rate)
    sample_clk_task.timing.cfg_implicit_timing(samps_per_chan=num_samples)
    sample_clk_task.control(constants.TaskMode.TASK_COMMIT)

    sample_clk_terminal = f"/{device.name}/Ctr0InternalOutput"

    # Set up AO task with multiple channels
    for chan_index in range(num_channels):
        ao_task.ao_channels.add_ao_voltage_chan(
            device.ao_physical_chans[chan_index].name,
            min_val=min_voltage,
            max_val=max_voltage,
        )
    ao_task.timing.cfg_samp_clk_timing(
        rate=sample_rate,
        source=sample_clk_terminal,
        active_edge=constants.Edge.RISING,
        samps_per_chan=num_samples,
    )

    # Set up AI task for loopback with multiple channels
    for chan_index in range(num_channels):
        ai_task.ai_channels.add_ai_voltage_chan(
            f"{device.name}/_ao{chan_index}_vs_aognd",
            min_val=min_voltage,
            max_val=max_voltage,
        )
    ai_task.timing.cfg_samp_clk_timing(
        rate=sample_rate,
        source=sample_clk_terminal,
        active_edge=constants.Edge.FALLING,
        samps_per_chan=num_samples,
    )

    return ao_task, ai_task, sample_clk_task, sample_clk_terminal


def _get_approx_final_value(waveform: AnalogWaveform[Any], epsilon: float):
    expected_value = waveform.scaled_data[-1]
    return pytest.approx(expected_value, abs=epsilon)


def _assert_equal_2d(data: list[list[float]], expected: list[list[float]], abs: float) -> None:
    assert len(data) == len(expected)
    for i in range(len(data)):
        assert data[i] == pytest.approx(expected[i], abs=abs)


# NOTE: We use simulated signals for AI validation, so we can be fairly strict here.
AI_VOLTAGE_EPSILON = 1e-3

# NOTE: We must use real signals for AO validation, but we aren't validating hardware accuracy here.
# This should be wide enough tolerance to allow for uncalibrated boards while still ensuring we are
# correctly configuring hardware.
AO_VOLTAGE_EPSILON = 1e-2

# NOTE: You can't scale from volts to codes correctly without knowing the internal calibration
# constants. The internal reference has a healthy amount of overrange to ensure we can calibrate to
# device specifications. I've used 10.1 volts above to approximate that, but 100mv of accuracy is
# also fine since the expected output of each channel value will be 1 volt apart.
RAW_VOLTAGE_EPSILON = 1e-1

VOLTAGE_CODE_EPSILON = round(_volts_to_codes(AI_VOLTAGE_EPSILON))
POWER_EPSILON = 1e-3
POWER_BINARY_EPSILON = 1
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/_digital_utils.py sha256=4bd71c494dabb6e67fa29995210cddc4883f27f7b3d220d54ef4829432b07743 bytes=9480 -->
## FILE: tests/component/_digital_utils.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/_digital_utils.py`
- sha256: `4bd71c494dabb6e67fa29995210cddc4883f27f7b3d220d54ef4829432b07743`
- bytes: 9480

````python
"""Shared utilities for digital component tests."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any, TypeVar

import numpy
from nitypes.waveform import DigitalWaveform
from nitypes.waveform.typing import AnyDigitalState, TDigitalState

import nidaqmx
import nidaqmx.system

_D = TypeVar("_D", bound=numpy.generic)


def _start_di_task(task: nidaqmx.Task) -> None:
    # Don't reserve the lines, so we can read what DO is writing.
    task.di_channels.all.di_tristate = False
    task.start()


def _start_do_task(task: nidaqmx.Task, is_port: bool = False, num_chans: int = 1) -> None:
    # We'll be doing on-demand, so start the task and drive all lines low
    task.start()
    if is_port:
        if num_chans == 8:
            task.write(0)
        else:
            task.write([0] * num_chans)
    else:
        if num_chans == 1:
            task.write(False)
        else:
            task.write([False] * num_chans)


def _get_num_di_lines_in_task(task: nidaqmx.Task) -> int:
    return sum([chan.di_num_lines for chan in task.channels])


def _get_num_do_lines_in_task(task: nidaqmx.Task) -> int:
    return sum([chan.do_num_lines for chan in task.channels])


def _get_digital_data_for_sample(num_lines: int, sample_number: int) -> int:
    result = 0
    # Simulated digital signals "count" from 0 in binary within each group of 8 lines.
    for _ in range((num_lines + 7) // 8):
        result = (result << 8) | sample_number

    line_mask = (2**num_lines) - 1
    return result & line_mask


def _get_expected_data_for_line(num_samples: int, line_number: int) -> list[int]:
    data = []
    # Simulated digital signals "count" from 0 in binary within each group of 8 lines.
    # Each line represents a bit in the binary representation of the sample number.
    # - line 0 represents bit 0 (LSB) - alternates every sample: 0,1,0,1,0,1,0,1...
    # - line 1 represents bit 1 - alternates every 2 samples:    0,0,1,1,0,0,1,1...
    # - line 2 represents bit 2 - alternates every 4 samples:    0,0,0,0,1,1,1,1...
    line_number %= 8
    for sample_num in range(num_samples):
        bit_value = (sample_num >> line_number) & 1
        data.append(bit_value)
    return data


def _get_expected_data_for_lines(num_samples: int, first_line: int, num_lines: int) -> list[int]:
    data = []
    # Simulated digital signals "count" from 0 in binary within each group of 8 lines.
    # Each line represents a bit in the binary representation of the sample number.
    # This function combines multiple lines into integer values where each bit represents a line.
    for sample_num in range(num_samples):
        result = 0
        for line_num in range(first_line, first_line + num_lines):
            line_index = line_num % 8
            bit_value = (sample_num >> line_index) & 1
            # Set the bit at position (line_num - first_line) in the result
            if bit_value:
                result |= 1 << (line_num - first_line)
        data.append(result)
    return data


def _get_digital_data(num_lines: int, num_samples: int) -> list[int]:
    return [
        _get_digital_data_for_sample(num_lines, sample_number)
        for sample_number in range(num_samples)
    ]


def _get_expected_digital_port_data_port_major(
    task: nidaqmx.Task, num_samples: int
) -> list[list[int]]:
    return [_get_digital_data(chan.di_num_lines, num_samples) for chan in task.channels]


def _get_expected_digital_port_data_sample_major(
    task: nidaqmx.Task, num_samples: int
) -> list[list[int]]:
    result = _get_expected_digital_port_data_port_major(task, num_samples)
    return numpy.transpose(result).tolist()


def _get_digital_port_data_for_sample(task: nidaqmx.Task, sample_number: int) -> list[int]:
    return [
        _get_digital_data_for_sample(chan.do_num_lines, sample_number) for chan in task.channels
    ]


def _get_digital_port_data_port_major(task: nidaqmx.Task, num_samples: int) -> list[list[int]]:
    return [_get_digital_data(chan.do_num_lines, num_samples) for chan in task.channels]


def _get_digital_port_data_sample_major(task: nidaqmx.Task, num_samples: int) -> list[list[int]]:
    result = _get_digital_port_data_port_major(task, num_samples)
    return numpy.transpose(result).tolist()


def _bool_array_to_int_lsb(bool_array: numpy.typing.NDArray[numpy.bool_]) -> int:
    result = 0
    # Interpret data as little-endian
    for bit in bool_array[::-1]:
        result = (result << 1) | int(bit)
    return result


def _bool_array_to_int_msb(bool_array: numpy.typing.NDArray[numpy.bool_]) -> int:
    result = 0
    # Interpret data as big-endian
    for bit in bool_array:
        result = (result << 1) | int(bit)
    return result


def _int_to_bool_array(num_lines: int, input: int) -> numpy.typing.NDArray[numpy.bool_]:
    result = numpy.full(num_lines, True, dtype=numpy.bool_)
    for bit in range(num_lines):
        result[bit] = (input & (1 << bit)) != 0
    return result


def _get_waveform_data(waveform: DigitalWaveform[Any]) -> list[int]:
    assert isinstance(waveform, DigitalWaveform)
    return [_bool_array_to_int_lsb(sample) for sample in waveform.data]


def _get_waveform_port_data(waveform: DigitalWaveform[Any]) -> list[int]:
    assert isinstance(waveform, DigitalWaveform)
    return [_bool_array_to_int_msb(sample) for sample in waveform.data]


def _create_digital_waveform_uint8(
    num_samples: int, num_lines: int = 1, invert: bool = False
) -> DigitalWaveform[numpy.uint8]:
    return _create_digital_waveform(num_samples, num_lines, invert=invert, dtype=numpy.uint8)


def _create_digital_waveform(
    num_samples: int,
    num_lines: int,
    dtype: type[TDigitalState],
    invert: bool = False,
) -> DigitalWaveform[TDigitalState]:
    waveform = DigitalWaveform(num_samples, num_lines, dtype=dtype)
    expected_data = _get_digital_data(num_lines, num_samples)
    _set_waveform_data(num_samples, num_lines, waveform, expected_data, invert=invert)
    return waveform


def _create_waveform_for_line(num_samples: int, line_number: int) -> DigitalWaveform[numpy.uint8]:
    waveform = DigitalWaveform(num_samples, 1)
    expected_data = _get_expected_data_for_line(num_samples, line_number)
    _set_waveform_data(num_samples, 1, waveform, expected_data)
    return waveform


def _create_waveform_for_lines(
    num_samples: int, first_line: int, num_lines: int, dtype: type[TDigitalState]
) -> DigitalWaveform[TDigitalState]:
    waveform = DigitalWaveform(num_samples, num_lines, dtype=dtype)
    expected_data = _get_expected_data_for_lines(num_samples, first_line, num_lines)
    _set_waveform_data(num_samples, num_lines, waveform, expected_data)
    return waveform


def _create_waveforms_for_mixed_lines(num_samples: int) -> list[DigitalWaveform[AnyDigitalState]]:
    # create waveforms for lines 2-4, 0-1, and 5-7, matching the channel configuration
    # in the do_multi_channel_mixed_line_task fixture
    return [
        _create_waveform_for_lines(num_samples, first_line=2, num_lines=3, dtype=numpy.uint8),
        _create_waveform_for_lines(num_samples, first_line=0, num_lines=2, dtype=numpy.int8),
        _create_waveform_for_lines(num_samples, first_line=5, num_lines=3, dtype=numpy.bool),
    ]


def _set_waveform_data(
    num_samples: int,
    num_lines: int,
    waveform: DigitalWaveform[Any],
    expected_data: list[int],
    invert: bool = False,
) -> None:
    for i in range(num_samples):
        bool_array = _int_to_bool_array(num_lines, expected_data[i])
        if invert:
            bool_array = numpy.logical_not(bool_array)
        waveform.data[i] = bool_array


def _create_non_contiguous_digital_waveform(
    num_samples: int, first_line: int, num_lines: int
) -> DigitalWaveform[numpy.uint8]:
    digital_data = _get_expected_data_for_lines(num_samples, first_line, num_lines)
    interleaved_data = numpy.zeros((num_samples * 2, num_lines), dtype=numpy.uint8)

    for i in range(num_samples):
        bool_array = _int_to_bool_array(num_lines, digital_data[i])
        interleaved_data[i * 2] = bool_array

    non_contiguous_samples = interleaved_data[::2]
    waveform = DigitalWaveform(num_samples, num_lines, data=non_contiguous_samples)
    assert not waveform.data.flags.c_contiguous
    assert waveform.sample_count == num_samples
    return waveform


def _read_and_copy(
    read_func: Callable[[numpy.typing.NDArray[_D]], None], array: numpy.typing.NDArray[_D]
) -> numpy.typing.NDArray[_D]:
    read_func(array)
    return array.copy()


def _validate_waveform_signals(
    device: nidaqmx.system.device.Device,
    waveform: DigitalWaveform[Any],
    lines: list[int] | range,  # signal index to line index mapping
) -> None:
    lines_list = list(lines)
    signal_count = waveform.signal_count
    sample_count = waveform.sample_count
    assert signal_count == len(lines_list)
    for signal_index in range(signal_count):
        line_index = lines_list[signal_index]
        signal = waveform.signals[signal_index]
        assert signal.signal_index == signal_index
        assert signal.name == device.di_lines[line_index].name
        assert signal.data.tolist() == _get_expected_data_for_line(sample_count, line_index)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/_utils.py sha256=2f62c121afb5cba43807ec780110d5d67566a975b4e6ba20386e678bc4aec110 bytes=468 -->
## FILE: tests/component/_utils.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/_utils.py`
- sha256: `2f62c121afb5cba43807ec780110d5d67566a975b4e6ba20386e678bc4aec110`
- bytes: 468

````python
"""Shared utilities for component tests."""

from __future__ import annotations

from datetime import timezone

from hightime import datetime as ht_datetime
from nitypes.time.typing import AnyDateTime


def _is_timestamp_close_to_now(timestamp: AnyDateTime, tolerance_seconds: float = 1.0) -> bool:
    current_time = ht_datetime.now(timezone.utc)
    time_diff = abs((timestamp - current_time).total_seconds())
    return time_diff <= tolerance_seconds
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/conftest.py sha256=06c10dff3d3460a9dab1bfa00d42f55bc93ed79e76c836e428935aca2f278f6c bytes=29817 -->
## FILE: tests/component/conftest.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/conftest.py`
- sha256: `06c10dff3d3460a9dab1bfa00d42f55bc93ed79e76c836e428935aca2f278f6c`
- bytes: 29817

````python
"""Shared fixtures for component tests."""

from __future__ import annotations

from collections.abc import Callable

import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import AcquisitionType, LineGrouping
from nidaqmx.utils import flatten_channel_string
from tests.component._analog_utils import (
    AI_VOLTAGE_EPSILON,
    AO_VOLTAGE_EPSILON,
    _get_current_setpoint_for_chan,
    _get_expected_voltage_for_chan,
    _get_voltage_offset_for_chan,
    _get_voltage_setpoint_for_chan,
)
from tests.component._digital_utils import _start_di_task, _start_do_task


@pytest.fixture
def ai_single_channel_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel AI task."""
    offset = _get_voltage_offset_for_chan(0)
    task.ai_channels.add_ai_voltage_chan(
        sim_6363_device.ai_physical_chans[0].name,
        min_val=offset,
        max_val=offset + AI_VOLTAGE_EPSILON,
    )
    return task


@pytest.fixture
def ai_single_channel_task_with_timing(
    ai_single_channel_task: nidaqmx.Task,
) -> nidaqmx.Task:
    """Configure a single-channel AI task with timing."""
    ai_single_channel_task.timing.cfg_samp_clk_timing(
        1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50
    )
    return ai_single_channel_task


@pytest.fixture
def ai_single_channel_task_with_high_rate(
    task: nidaqmx.Task, sim_charge_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel AI task with high sampling rate."""
    offset = _get_voltage_offset_for_chan(0)
    task.ai_channels.add_ai_voltage_chan(
        sim_charge_device.ai_physical_chans[0].name,
        min_val=offset,
        max_val=offset + AI_VOLTAGE_EPSILON,
    )
    task.timing.cfg_samp_clk_timing(
        rate=10_000_000, sample_mode=AcquisitionType.FINITE, samps_per_chan=50
    )
    return task


@pytest.fixture
def ai_multi_channel_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel AI task."""
    for chan_index in range(3):
        offset = _get_voltage_offset_for_chan(chan_index)
        chan = task.ai_channels.add_ai_voltage_chan(
            sim_6363_device.ai_physical_chans[chan_index].name,
            min_val=offset,
            # min and max must be different, so add a small epsilon
            max_val=offset + AI_VOLTAGE_EPSILON,
        )
        # forcing the maximum range for binary read scaling to be predictable
        chan.ai_rng_high = 10
        chan.ai_rng_low = -10

    return task


@pytest.fixture
def ai_multi_channel_task_with_timing(
    ai_multi_channel_task: nidaqmx.Task,
) -> nidaqmx.Task:
    """Configure a multi-channel AI task with timing."""
    ai_multi_channel_task.timing.cfg_samp_clk_timing(
        1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50
    )
    return ai_multi_channel_task


@pytest.fixture
def pwr_single_channel_task(
    task: nidaqmx.Task, sim_ts_power_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel power task."""
    task.ai_channels.add_ai_power_chan(
        f"{sim_ts_power_device.name}/power",
        _get_voltage_setpoint_for_chan(0),
        _get_current_setpoint_for_chan(0),
        True,  # output enable
    )
    return task


@pytest.fixture
def pwr_multi_channel_task(
    task: nidaqmx.Task, sim_ts_power_devices: list[nidaqmx.system.Device]
) -> nidaqmx.Task:
    """Configure a multi-channel power task."""
    for chan_index, sim_ts_power_device in enumerate(sim_ts_power_devices):
        task.ai_channels.add_ai_power_chan(
            f"{sim_ts_power_device.name}/power",
            _get_voltage_setpoint_for_chan(chan_index),
            _get_current_setpoint_for_chan(chan_index),
            True,  # output enable
        )
    return task


@pytest.fixture
def di_single_line_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task:
    """Configure a single-line digital input task."""
    task.di_channels.add_di_chan(
        sim_6363_device.di_lines[0].name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )
    return task


@pytest.fixture
def di_single_line_timing_task(di_single_line_task: nidaqmx.Task) -> nidaqmx.Task:
    """Configure timing for a single-line digital input task."""
    di_single_line_task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50
    )
    return di_single_line_task


@pytest.fixture
def di_single_line_high_rate_task(di_single_line_task: nidaqmx.Task) -> nidaqmx.Task:
    """Configure a high-rate single-line digital input task."""
    di_single_line_task.timing.cfg_samp_clk_timing(
        rate=10_000_000, sample_mode=AcquisitionType.FINITE, samps_per_chan=50
    )
    return di_single_line_task


@pytest.fixture
def di_single_channel_multi_line_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel multi-line digital input task."""
    task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_single_channel_multi_line_timing_task(
    di_single_channel_multi_line_task: nidaqmx.Task,
) -> nidaqmx.Task:
    """Configure timing for a single-channel multi-line digital input task."""
    di_single_channel_multi_line_task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50
    )
    return di_single_channel_multi_line_task


@pytest.fixture
def di_single_channel_timing_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure timing for a single-channel digital input task."""
    task.di_channels.add_di_chan(
        sim_6363_device.di_lines[0].name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)
    return task


@pytest.fixture
def di_single_chan_lines_and_port_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel multi-line digital input task."""
    task.di_channels.add_di_chan(
        flatten_channel_string(
            sim_6363_device.di_lines.channel_names[0:3] + [sim_6363_device.di_ports[1].name]
        ),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_multi_channel_multi_line_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel digital input task."""
    task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_PER_LINE,
    )
    return task


@pytest.fixture
def di_multi_chan_multi_line_timing_task(
    di_multi_channel_multi_line_task: nidaqmx.Task,
) -> nidaqmx.Task:
    """Configure timing for a multi-channel digital input task."""
    di_multi_channel_multi_line_task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50
    )
    return di_multi_channel_multi_line_task


@pytest.fixture
def di_multi_chan_diff_lines_timing_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel digital input task.

    This task has three channels made up of different numbers of lines.
    """
    task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[0:1]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[1:3]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[3:7]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50
    )
    return task


@pytest.fixture
def di_multi_chan_lines_and_port_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel digital input task.

    This task has three channels made up of lines and one channel made up of a port.
    """
    task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[0:1]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[1:3]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[3:7]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_single_channel_port_byte_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel digital input task with a channel made up of an 8-line port."""
    # 6363 port 1 has 8 lines
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_multi_channel_port_byte_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel digital input task with channels made up of 8-line ports."""
    # 6363 port 1 has 8 lines
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    # 6363 port 2 has 8 lines
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[2].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_single_channel_port_uint16_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel digital input task with a channel made up of an 8-line port."""
    # 6363 port 1 has 8 lines, and DAQ will happily extend the data to the larger type.
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_multi_channel_port_uint16_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel digital input task with channels made up of 8-line ports."""
    # 6363 port 1 has 8 lines, and DAQ will happily extend the data to the larger type.
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    # 6363 port 2 has 8 lines, and DAQ will happily extend the data to the larger type.
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[2].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_single_channel_port_uint32_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel digital input task with a channel made up of a 32-line port."""
    # 6363 port 0 has 32 lines
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[0].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_single_channel_port_uint32_timing_task(
    di_single_channel_port_uint32_task: nidaqmx.Task,
) -> nidaqmx.Task:
    """Configure timing for a single-channel digital input task.

    This task has a channel made up of a 32-line port.
    """
    di_single_channel_port_uint32_task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50
    )
    return di_single_channel_port_uint32_task


@pytest.fixture
def di_multi_channel_port_uint32_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel digital input task.

    This task has channels made up of a 32-line port and two 8-line ports.
    """
    # 6363 port 0 has 32 lines
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[0].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    # 6363 port 1 has 8 lines, and DAQ will happily extend the data to the larger type.
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    # 6363 port 2 has 8 lines, and DAQ will happily extend the data to the larger type.
    task.di_channels.add_di_chan(
        sim_6363_device.di_ports[2].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    return task


@pytest.fixture
def di_multi_channel_timing_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure timing for a multi-channel digital input task."""
    task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_PER_LINE,
    )
    task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)
    return task


@pytest.fixture
def ao_single_channel_task(
    generate_task: Callable[[], nidaqmx.Task],
    real_x_series_multiplexed_device: nidaqmx.system.Device,
) -> nidaqmx.Task:
    """Configure a single-channel AO task."""
    task = generate_task()
    chan_index = 0
    offset = _get_expected_voltage_for_chan(chan_index)
    chan = task.ao_channels.add_ao_voltage_chan(
        real_x_series_multiplexed_device.ao_physical_chans[chan_index].name,
        min_val=0.0,
        max_val=offset + AO_VOLTAGE_EPSILON,
    )
    # forcing the maximum range for binary read scaling to be predictable
    chan.ao_dac_rng_high = 10
    chan.ao_dac_rng_low = -10

    # we'll be doing simple on-demand, so start the task now
    task.start()

    # set the output to a known initial value
    task.write(0.0)

    return task


@pytest.fixture
def ao_single_channel_task_with_timing(
    generate_task: Callable[[], nidaqmx.Task],
    real_x_series_multiplexed_device: nidaqmx.system.Device,
) -> nidaqmx.Task:
    """Configure a single-channel AO task with timing for waveform testing."""
    task = generate_task()
    task.ao_channels.add_ao_voltage_chan(
        real_x_series_multiplexed_device.ao_physical_chans[0].name,
        min_val=0.0,
        max_val=3.0,
    )
    task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=100
    )
    return task


@pytest.fixture
def ai_single_channel_loopback_task(
    generate_task: Callable[[], nidaqmx.Task],
    real_x_series_multiplexed_device: nidaqmx.system.Device,
) -> nidaqmx.Task:
    """Configure a single-channel AI loopback task."""
    task = generate_task()
    chan_index = 0
    task.ai_channels.add_ai_voltage_chan(
        f"{real_x_series_multiplexed_device.name}/_ao{chan_index}_vs_aognd",
        min_val=-10,
        max_val=10,
    )

    # we'll be doing simple on-demand, so start the task now
    task.start()

    return task


@pytest.fixture
def ao_multi_channel_task(
    generate_task: Callable[[], nidaqmx.Task],
    real_x_series_multiplexed_device: nidaqmx.system.Device,
) -> nidaqmx.Task:
    """Configure a multi-channel AO task."""
    task = generate_task()
    num_chans = 2
    for chan_index in range(num_chans):
        offset = _get_expected_voltage_for_chan(chan_index)
        chan = task.ao_channels.add_ao_voltage_chan(
            real_x_series_multiplexed_device.ao_physical_chans[chan_index].name,
            min_val=0.0,
            max_val=offset + AO_VOLTAGE_EPSILON,
        )
        # forcing the maximum range for binary read scaling to be predictable
        chan.ao_dac_rng_high = 10
        chan.ao_dac_rng_low = -10

    # we'll be doing simple on-demand, so start the task now
    task.start()

    # set the output to a known initial value
    task.write([0.0] * num_chans)

    return task


@pytest.fixture
def ao_multi_channel_task_with_timing(
    generate_task: Callable[[], nidaqmx.Task],
    real_x_series_multiplexed_device: nidaqmx.system.Device,
) -> nidaqmx.Task:
    """Configure a multi-channel AO task with timing for waveform testing."""
    task = generate_task()
    num_chans = 2
    for chan_index in range(num_chans):
        task.ao_channels.add_ao_voltage_chan(
            real_x_series_multiplexed_device.ao_physical_chans[chan_index].name,
            min_val=0.0,
            max_val=3.0,
        )

    task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=100
    )

    return task


@pytest.fixture
def ai_multi_channel_loopback_task(
    generate_task: Callable[[], nidaqmx.Task],
    real_x_series_multiplexed_device: nidaqmx.system.Device,
) -> nidaqmx.Task:
    """Configure a multi-channel AI loopback task."""
    task = generate_task()
    num_chans = 2
    for chan_index in range(num_chans):
        task.ai_channels.add_ai_voltage_chan(
            f"{real_x_series_multiplexed_device.name}/_ao{chan_index}_vs_aognd",
            min_val=-10,
            max_val=10,
        )

    # we'll be doing simple on-demand, so start the task now
    task.start()

    return task


@pytest.fixture
def do_single_line_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-line DO task."""
    task = generate_task()
    task.do_channels.add_do_chan(
        real_x_series_device.do_lines[0].name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )
    _start_do_task(task)
    return task


@pytest.fixture
def do_single_line_task_with_timing(
    generate_task, real_x_series_multiplexed_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-line DO task with timing for waveform testing."""
    task = generate_task()
    task.do_channels.add_do_chan(
        real_x_series_multiplexed_device.do_lines[0].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=100
    )
    return task


@pytest.fixture
def do_single_channel_multi_line_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel DO task."""
    task = generate_task()
    chan = task.do_channels.add_do_chan(
        flatten_channel_string(real_x_series_device.do_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_do_task(task, num_chans=chan.do_num_lines)
    return task


@pytest.fixture
def do_single_channel_multi_line_task_with_timing(
    generate_task, real_x_series_multiplexed_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel multi-line DO task with timing for waveform testing."""
    task = generate_task()
    task.do_channels.add_do_chan(
        flatten_channel_string(real_x_series_multiplexed_device.do_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=100
    )
    return task


@pytest.fixture
def do_multi_channel_multi_line_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel DO task."""
    task = generate_task()
    task.do_channels.add_do_chan(
        flatten_channel_string(real_x_series_device.do_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_PER_LINE,
    )
    _start_do_task(task, num_chans=task.number_of_channels)
    return task


@pytest.fixture
def do_multi_channel_multi_line_task_with_timing(
    generate_task, real_x_series_multiplexed_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel multi-line DO task with timing for waveform testing."""
    task = generate_task()
    task.do_channels.add_do_chan(
        flatten_channel_string(real_x_series_multiplexed_device.do_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_PER_LINE,
    )
    task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=100
    )
    return task


@pytest.fixture
def do_multi_channel_mixed_line_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel DO task with a mix of lines."""
    task = generate_task()
    task.do_channels.add_do_chan(
        flatten_channel_string(real_x_series_device.do_lines.channel_names[2:5]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.do_channels.add_do_chan(
        flatten_channel_string(real_x_series_device.do_lines.channel_names[0:2]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.do_channels.add_do_chan(
        flatten_channel_string(real_x_series_device.do_lines.channel_names[5:8]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_do_task(task, num_chans=task.number_of_channels)
    return task


@pytest.fixture
def do_port0_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel DO task."""
    task = generate_task()
    # X Series port 0 has either 32 or 8 lines. The former can only be used with 32-bit writes. The
    # latter can be used with any sized port write.
    task.do_channels.add_do_chan(
        real_x_series_device.do_ports[0].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_do_task(task, is_port=True)
    return task


@pytest.fixture
def do_port1_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel DO task."""
    task = generate_task()
    # X Series port 1 has 8 lines, and can be used with any sized port write.
    task.do_channels.add_do_chan(
        real_x_series_device.do_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_do_task(task, is_port=True)
    return task


@pytest.fixture
def do_multi_channel_port_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel DO task."""
    task = generate_task()
    # X Series port 1 has 8 lines, and can be used with any sized port write
    task.do_channels.add_do_chan(
        real_x_series_device.do_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    # X Series port 2 has 8 lines, and can be used with any sized port write
    task.do_channels.add_do_chan(
        real_x_series_device.do_ports[2].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_do_task(task, is_port=True, num_chans=task.number_of_channels)
    return task


@pytest.fixture
def do_multi_channel_port_and_lines_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel DO task."""
    task = generate_task()
    # X Series port 1 has 8 lines, and can be used with any sized port write
    task.do_channels.add_do_chan(
        real_x_series_device.do_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.do_channels.add_do_chan(
        flatten_channel_string(real_x_series_device.do_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_do_task(task, is_port=True, num_chans=task.number_of_channels)
    return task


@pytest.fixture
def di_single_line_loopback_task(
    generate_task: Callable[[], nidaqmx.Task],
    real_x_series_device: nidaqmx.system.Device,
) -> nidaqmx.Task:
    """Configure a single-line DI loopback task."""
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device.di_lines[0].name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )
    _start_di_task(task)
    return task


@pytest.fixture
def di_multi_line_loopback_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-line DI loopback task."""
    task = generate_task()
    task.di_channels.add_di_chan(
        flatten_channel_string(real_x_series_device.di_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task


@pytest.fixture
def di_port0_loopback_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel DI loopback task."""
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device.di_ports[0].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task


@pytest.fixture
def di_port0_loopback_task_32dio(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device_32dio: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel DI loopback task."""
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device_32dio.di_ports[0].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task


@pytest.fixture
def di_port1_loopback_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel DI loopback task."""
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task


@pytest.fixture
def di_port1_loopback_task_32dio(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device_32dio: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel DI loopback task."""
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device_32dio.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task


@pytest.fixture
def di_port2_loopback_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel DI loopback task."""
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device.di_ports[2].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task


@pytest.fixture
def di_port2_loopback_task_32dio(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device_32dio: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a single-channel DI loopback task."""
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device_32dio.di_ports[2].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task


@pytest.fixture
def di_multi_channel_port_loopback_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel DI loopback task."""
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.di_channels.add_di_chan(
        real_x_series_device.di_ports[2].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task


@pytest.fixture
def di_multi_channel_port_and_lines_loopback_task(
    generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device
) -> nidaqmx.Task:
    """Configure a multi-channel DI loopback task."""
    task = generate_task()
    task.di_channels.add_di_chan(
        real_x_series_device.di_ports[1].name,
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    task.di_channels.add_di_chan(
        flatten_channel_string(real_x_series_device.di_lines.channel_names[:8]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )
    _start_di_task(task)
    return task
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/stream_readers/__init__.py sha256=6406416d8e974b84b0fa00878b60d18cf54d1c03daf7b2898864e53c384d61a7 bytes=35 -->
## FILE: tests/component/stream_readers/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/stream_readers/__init__.py`
- sha256: `6406416d8e974b84b0fa00878b60d18cf54d1c03daf7b2898864e53c384d61a7`
- bytes: 35

````python
"""Stream readers test module."""
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/stream_readers/test_analog_multi_channel_reader.py sha256=036b20db0b45cba244443d4d0c08d543a2566c5dd831e0e49af65529aa8a020d bytes=20096 -->
## FILE: tests/component/stream_readers/test_analog_multi_channel_reader.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/stream_readers/test_analog_multi_channel_reader.py`
- sha256: `036b20db0b45cba244443d4d0c08d543a2566c5dd831e0e49af65529aa8a020d`
- bytes: 20096

````python
from __future__ import annotations

import ctypes
import math
from collections.abc import Callable

import numpy
import pytest
from hightime import timedelta as ht_timedelta
from nitypes.waveform import AnalogWaveform, SampleIntervalMode

import nidaqmx
import nidaqmx.system
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, FeatureNotSupportedError
from nidaqmx.constants import (
    READ_ALL_AVAILABLE,
    AcquisitionType,
    ReallocationPolicy,
    WaveformAttributeMode,
)
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.stream_readers import AnalogMultiChannelReader, DaqError
from tests.component._analog_utils import (
    AI_VOLTAGE_EPSILON,
    _get_voltage_offset_for_chan,
)
from tests.component._utils import _is_timestamp_close_to_now


def test___analog_multi_channel_reader___read_one_sample___returns_valid_samples(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    data = numpy.full(num_channels, math.inf, dtype=numpy.float64)

    reader.read_one_sample(data)

    expected = [_get_voltage_offset_for_chan(chan_index) for chan_index in range(num_channels)]
    assert data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


def test___analog_multi_channel_reader___read_one_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    data = numpy.full(num_channels, math.inf, dtype=numpy.float32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample(data)

    assert "float64" in exc_info.value.args[0]


def test___analog_multi_channel_reader___read_many_sample___returns_valid_samples(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10
    data = numpy.full((num_channels, samples_to_read), math.inf, dtype=numpy.float64)

    samples_read = reader.read_many_sample(data, samples_to_read)

    assert samples_read == samples_to_read
    expected_vals = [_get_voltage_offset_for_chan(chan_index) for chan_index in range(num_channels)]
    assert data == pytest.approx(expected_vals, abs=AI_VOLTAGE_EPSILON)


def test___analog_multi_channel_reader___read_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10
    data = numpy.full((num_channels, samples_to_read), math.inf, dtype=numpy.float32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample(data, samples_to_read)

    assert "float64" in exc_info.value.args[0]


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
def test___analog_multi_channel_reader___read_waveforms_feature_disabled___raises_feature_not_supported_error(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task_with_timing.in_stream)
    num_channels = ai_multi_channel_task_with_timing.number_of_channels
    samples_to_read = 10
    waveforms = [AnalogWaveform(samples_to_read) for _ in range(num_channels)]

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        reader.read_waveforms(waveforms)

    error_message = exc_info.value.args[0]
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message
    assert "NIDAQMX_ENABLE_WAVEFORM_SUPPORT" in error_message


def test___analog_multi_channel_reader___read_waveforms___returns_valid_waveforms(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task_with_timing.in_stream)
    num_channels = ai_multi_channel_task_with_timing.number_of_channels
    samples_to_read = 10
    waveforms = [AnalogWaveform(samples_to_read) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 3
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan_index, waveform in enumerate(waveforms):
        assert isinstance(waveform, AnalogWaveform)
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
        assert _is_timestamp_close_to_now(waveform.timing.timestamp)
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert (
            waveform.channel_name == ai_multi_channel_task_with_timing.ai_channels[chan_index].name
        )
        assert waveform.units == "Volts"
        assert waveform.sample_count == samples_to_read


def test___analog_multi_channel_reader___read_waveforms_no_args___returns_valid_waveforms(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task_with_timing.in_stream)
    num_channels = ai_multi_channel_task_with_timing.number_of_channels
    waveforms = [AnalogWaveform(50) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms)

    assert samples_read == 50
    assert num_channels == 3
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan_index, waveform in enumerate(waveforms):
        assert isinstance(waveform, AnalogWaveform)
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
        assert _is_timestamp_close_to_now(waveform.timing.timestamp)
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert (
            waveform.channel_name == ai_multi_channel_task_with_timing.ai_channels[chan_index].name
        )
        assert waveform.units == "Volts"
        assert waveform.sample_count == 50


def test___analog_multi_channel_reader___read_waveforms_in_place___populates_valid_waveforms(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task_with_timing.in_stream)
    num_channels = ai_multi_channel_task_with_timing.number_of_channels
    samples_to_read = 10

    waveforms = [
        AnalogWaveform(samples_to_read),
        AnalogWaveform(samples_to_read),
        AnalogWaveform(samples_to_read),
    ]
    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 3
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan_index, waveform in enumerate(waveforms):
        assert isinstance(waveform, AnalogWaveform)
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
        assert _is_timestamp_close_to_now(waveform.timing.timestamp)
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert (
            waveform.channel_name == ai_multi_channel_task_with_timing.ai_channels[chan_index].name
        )
        assert waveform.units == "Volts"
        assert waveform.sample_count == samples_to_read


def test___analog_multi_channel_reader___read_into_undersized_waveforms_without_reallocation___throws_exception(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task_with_timing.in_stream)
    samples_to_read = 10

    waveforms = [
        AnalogWaveform(samples_to_read),
        AnalogWaveform(samples_to_read - 1),
        AnalogWaveform(samples_to_read - 5),
    ]
    with pytest.raises(DaqError) as exc_info:
        reader.read_waveforms(waveforms, samples_to_read, ReallocationPolicy.DO_NOT_REALLOCATE)

    assert exc_info.value.error_code == DAQmxErrors.READ_BUFFER_TOO_SMALL
    assert exc_info.value.args[0].startswith("The waveform at index 1 does not have enough space")


def test___analog_multi_channel_reader___read_into_undersized_waveforms___returns_valid_waveforms(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task_with_timing.in_stream)
    num_channels = ai_multi_channel_task_with_timing.number_of_channels
    samples_to_read = 10

    waveforms = [
        AnalogWaveform(samples_to_read),
        AnalogWaveform(samples_to_read - 1),
        AnalogWaveform(samples_to_read - 5),
    ]
    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 3
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan_index, waveform in enumerate(waveforms):
        assert isinstance(waveform, AnalogWaveform)
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
        assert _is_timestamp_close_to_now(waveform.timing.timestamp)
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert (
            waveform.channel_name == ai_multi_channel_task_with_timing.ai_channels[chan_index].name
        )
        assert waveform.units == "Volts"
        assert waveform.sample_count == samples_to_read


def test___analog_multi_channel_reader___reuse_waveform_in_place_with_different_sample_counts___populates_valid_waveforms(
    generate_task: Callable[[], nidaqmx.Task], sim_6363_device: nidaqmx.system.Device
) -> None:
    def _make_multi_channel_reader(chan_a_index, chan_b_index, samps_per_chan):
        task = generate_task()
        task.ai_channels.add_ai_voltage_chan(
            sim_6363_device.ai_physical_chans[chan_a_index].name,
            min_val=chan_a_index,
            max_val=chan_a_index + AI_VOLTAGE_EPSILON,
        )
        task.ai_channels.add_ai_voltage_chan(
            sim_6363_device.ai_physical_chans[chan_b_index].name,
            min_val=chan_b_index,
            max_val=chan_b_index + AI_VOLTAGE_EPSILON,
        )
        task.timing.cfg_samp_clk_timing(
            1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=samps_per_chan
        )
        return AnalogMultiChannelReader(task.in_stream)

    reader0 = _make_multi_channel_reader(chan_a_index=0, chan_b_index=1, samps_per_chan=5)
    reader1 = _make_multi_channel_reader(chan_a_index=2, chan_b_index=3, samps_per_chan=10)
    reader2 = _make_multi_channel_reader(chan_a_index=4, chan_b_index=5, samps_per_chan=15)
    waveforms = [
        AnalogWaveform(10),
        AnalogWaveform(10, start_index=3, capacity=13),
    ]

    reader0.read_waveforms(waveforms, 5)
    assert waveforms[0].sample_count == 5
    assert waveforms[0].scaled_data == pytest.approx(0, abs=AI_VOLTAGE_EPSILON)
    assert waveforms[0].channel_name == f"{sim_6363_device.name}/ai0"
    assert waveforms[1].sample_count == 5
    assert waveforms[1].scaled_data == pytest.approx(1, abs=AI_VOLTAGE_EPSILON)
    assert waveforms[1].channel_name == f"{sim_6363_device.name}/ai1"

    reader1.read_waveforms(waveforms, 10)
    assert waveforms[0].sample_count == 10
    assert waveforms[0].scaled_data == pytest.approx(2, abs=AI_VOLTAGE_EPSILON)
    assert waveforms[0].channel_name == f"{sim_6363_device.name}/ai2"
    assert waveforms[1].sample_count == 10
    assert waveforms[1].scaled_data == pytest.approx(3, abs=AI_VOLTAGE_EPSILON)
    assert waveforms[1].channel_name == f"{sim_6363_device.name}/ai3"

    reader2.read_waveforms(waveforms, 15)
    assert waveforms[0].sample_count == 15
    assert waveforms[0].scaled_data == pytest.approx(4, abs=AI_VOLTAGE_EPSILON)
    assert waveforms[0].channel_name == f"{sim_6363_device.name}/ai4"
    assert waveforms[1].sample_count == 15
    assert waveforms[1].scaled_data == pytest.approx(5, abs=AI_VOLTAGE_EPSILON)
    assert waveforms[1].channel_name == f"{sim_6363_device.name}/ai5"


def test___analog_multi_channel_reader___read_with_wrong_number_of_waveforms___throws_exception(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task_with_timing.in_stream)
    samples_to_read = 10

    waveforms = [
        AnalogWaveform(samples_to_read),
        AnalogWaveform(samples_to_read),
    ]
    with pytest.raises(DaqError) as exc_info:
        reader.read_waveforms(waveforms, samples_to_read)

    assert exc_info.value.error_code == DAQmxErrors.MISMATCHED_INPUT_ARRAY_SIZES
    assert "does not match the number of channels" in exc_info.value.args[0]


def test___analog_multi_channel_reader_with_timing_flag___read_waveforms___only_includes_timing_data(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    in_stream = ai_multi_channel_task_with_timing.in_stream
    in_stream.waveform_attribute_mode = WaveformAttributeMode.TIMING
    reader = AnalogMultiChannelReader(in_stream)
    num_channels = ai_multi_channel_task_with_timing.number_of_channels
    samples_to_read = 10
    waveforms = [AnalogWaveform(samples_to_read) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 3
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan_index, waveform in enumerate(waveforms):
        assert isinstance(waveform, AnalogWaveform)
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
        assert _is_timestamp_close_to_now(waveform.timing.timestamp)
        assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert waveform.channel_name == ""
        assert waveform.units == ""
        assert waveform.sample_count == samples_to_read


def test___analog_multi_channel_reader_with_extended_properties_flag___read_waveforms___only_includes_extended_properties(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    in_stream = ai_multi_channel_task_with_timing.in_stream
    in_stream.waveform_attribute_mode = WaveformAttributeMode.EXTENDED_PROPERTIES
    reader = AnalogMultiChannelReader(in_stream)
    num_channels = ai_multi_channel_task_with_timing.number_of_channels
    samples_to_read = 10
    waveforms = [AnalogWaveform(samples_to_read) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 3
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan_index, waveform in enumerate(waveforms):
        assert isinstance(waveform, AnalogWaveform)
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
        assert waveform.timing.sample_interval_mode == SampleIntervalMode.NONE
        assert (
            waveform.channel_name == ai_multi_channel_task_with_timing.ai_channels[chan_index].name
        )
        assert waveform.units == "Volts"
        assert waveform.sample_count == samples_to_read


def test___analog_multi_channel_reader_with_both_flags___read_waveforms___includes_both_timing_and_extended_properties(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    in_stream = ai_multi_channel_task_with_timing.in_stream
    in_stream.waveform_attribute_mode = (
        WaveformAttributeMode.TIMING | WaveformAttributeMode.EXTENDED_PROPERTIES
    )
    reader = AnalogMultiChannelReader(in_stream)
    num_channels = ai_multi_channel_task_with_timing.number_of_channels
    samples_to_read = 10
    waveforms = [AnalogWaveform(samples_to_read) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 3
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan_index, waveform in enumerate(waveforms):
        assert isinstance(waveform, AnalogWaveform)
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
        assert _is_timestamp_close_to_now(waveform.timing.timestamp)
        assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert (
            waveform.channel_name == ai_multi_channel_task_with_timing.ai_channels[chan_index].name
        )
        assert waveform.units == "Volts"
        assert waveform.sample_count == samples_to_read


def test___analog_multi_channel_reader_with_none_flag___read_waveforms___minimal_waveform_data(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    in_stream = ai_multi_channel_task_with_timing.in_stream
    in_stream.waveform_attribute_mode = WaveformAttributeMode.NONE
    reader = AnalogMultiChannelReader(in_stream)
    num_channels = ai_multi_channel_task_with_timing.number_of_channels
    samples_to_read = 10
    waveforms = [AnalogWaveform(samples_to_read) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 3
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan_index, waveform in enumerate(waveforms):
        assert isinstance(waveform, AnalogWaveform)
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
        assert waveform.timing.sample_interval_mode == SampleIntervalMode.NONE
        assert waveform.channel_name == ""
        assert waveform.units == ""
        assert waveform.sample_count == samples_to_read


def test___analog_multi_channel_reader___read_waveforms_read_all_available___returns_valid_waveforms(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogMultiChannelReader(ai_multi_channel_task_with_timing.in_stream)
    num_channels = ai_multi_channel_task_with_timing.number_of_channels
    waveforms = [AnalogWaveform(100) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms, READ_ALL_AVAILABLE)

    assert samples_read == 50
    assert num_channels == 3
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan_index, waveform in enumerate(waveforms):
        assert isinstance(waveform, AnalogWaveform)
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
        assert _is_timestamp_close_to_now(waveform.timing.timestamp)
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert (
            waveform.channel_name == ai_multi_channel_task_with_timing.ai_channels[chan_index].name
        )
        assert waveform.units == "Volts"
        assert waveform.sample_count == samples_read
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/stream_readers/test_analog_single_channel_reader.py sha256=5dc476dbb4a840a1f2ca38faf4129879afc7fa694d1f39fced31351778961a05 bytes=16639 -->
## FILE: tests/component/stream_readers/test_analog_single_channel_reader.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/stream_readers/test_analog_single_channel_reader.py`
- sha256: `5dc476dbb4a840a1f2ca38faf4129879afc7fa694d1f39fced31351778961a05`
- bytes: 16639

````python
from __future__ import annotations

import ctypes
import math
from collections.abc import Callable

import numpy
import pytest
from hightime import timedelta as ht_timedelta
from nitypes.waveform import AnalogWaveform, SampleIntervalMode

import nidaqmx
import nidaqmx.system
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, FeatureNotSupportedError
from nidaqmx.constants import (
    READ_ALL_AVAILABLE,
    AcquisitionType,
    ReallocationPolicy,
    WaveformAttributeMode,
)
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.stream_readers import AnalogSingleChannelReader, DaqError
from tests.component._analog_utils import (
    AI_VOLTAGE_EPSILON,
    _get_voltage_offset_for_chan,
)
from tests.component._utils import _is_timestamp_close_to_now


def test___analog_single_channel_reader___read_one_sample___returns_valid_samples(
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task.in_stream)

    data = reader.read_one_sample()

    expected = _get_voltage_offset_for_chan(0)
    assert data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


def test___analog_single_channel_reader___read_many_sample___returns_valid_samples(
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task.in_stream)
    samples_to_read = 10
    data = numpy.full(samples_to_read, math.inf, dtype=numpy.float64)

    samples_read = reader.read_many_sample(data, samples_to_read)

    assert samples_read == samples_to_read
    expected = _get_voltage_offset_for_chan(0)
    assert data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


def test___analog_single_channel_reader___read_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task.in_stream)
    samples_to_read = 10
    data = numpy.full(samples_to_read, math.inf, dtype=numpy.float32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample(data, samples_to_read)

    assert "float64" in exc_info.value.args[0]


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
def test___analog_single_channel_reader___read_waveform_feature_disabled___raises_feature_not_supported_error(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task_with_timing.in_stream)
    waveform = AnalogWaveform(50)

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        reader.read_waveform(waveform)

    error_message = exc_info.value.args[0]
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message
    assert "NIDAQMX_ENABLE_WAVEFORM_SUPPORT" in error_message


def test___analog_single_channel_reader___read_waveform___returns_valid_waveform(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task_with_timing.in_stream)
    samples_to_read = 10
    waveform = AnalogWaveform(samples_to_read)

    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    assert isinstance(waveform, AnalogWaveform)
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == ai_single_channel_task_with_timing.ai_channels[0].name
    assert waveform.units == "Volts"
    assert waveform.sample_count == samples_to_read


def test___analog_single_channel_reader___read_waveform_no_args___returns_valid_waveform(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task_with_timing.in_stream)
    waveform = AnalogWaveform(50)

    samples_read = reader.read_waveform(waveform)

    assert samples_read == 50
    assert isinstance(waveform, AnalogWaveform)
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == ai_single_channel_task_with_timing.ai_channels[0].name
    assert waveform.units == "Volts"
    assert waveform.sample_count == 50


def test___analog_single_channel_reader___read_waveform_in_place___populates_valid_waveform(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task_with_timing.in_stream)
    samples_to_read = 10

    waveform = AnalogWaveform(samples_to_read)
    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    assert isinstance(waveform, AnalogWaveform)
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == ai_single_channel_task_with_timing.ai_channels[0].name
    assert waveform.units == "Volts"
    assert waveform.sample_count == samples_to_read


def test___analog_single_channel_reader___reuse_waveform_in_place___overwrites_data_timing_and_attributes(
    generate_task: Callable[[], nidaqmx.Task], sim_6363_device: nidaqmx.system.Device
) -> None:
    def _make_single_channel_reader(chan_index, offset, rate):
        task = generate_task()
        task.ai_channels.add_ai_voltage_chan(
            sim_6363_device.ai_physical_chans[chan_index].name,
            min_val=offset,
            max_val=offset + AI_VOLTAGE_EPSILON,
        )
        task.timing.cfg_samp_clk_timing(rate, sample_mode=AcquisitionType.FINITE, samps_per_chan=10)
        return AnalogSingleChannelReader(task.in_stream)

    reader0 = _make_single_channel_reader(chan_index=0, offset=0, rate=1000.0)
    reader1 = _make_single_channel_reader(chan_index=1, offset=1, rate=2000.0)
    waveform = AnalogWaveform(10)

    reader0.read_waveform(waveform, 10)
    timestamp1 = waveform.timing.timestamp
    assert waveform.scaled_data == pytest.approx(0, abs=AI_VOLTAGE_EPSILON)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == f"{sim_6363_device.name}/ai0"

    reader1.read_waveform(waveform, 10)
    timestamp2 = waveform.timing.timestamp
    assert waveform.scaled_data == pytest.approx(1, abs=AI_VOLTAGE_EPSILON)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 2000)
    assert waveform.channel_name == f"{sim_6363_device.name}/ai1"

    assert timestamp2 > timestamp1


def test___analog_single_channel_reader___read_into_undersized_waveform_without_reallocation___throws_exception(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task_with_timing.in_stream)
    samples_to_read = 10

    waveform = AnalogWaveform(samples_to_read - 1)
    with pytest.raises(DaqError) as exc_info:
        reader.read_waveform(waveform, samples_to_read, ReallocationPolicy.DO_NOT_REALLOCATE)

    assert exc_info.value.error_code == DAQmxErrors.READ_BUFFER_TOO_SMALL
    assert exc_info.value.args[0].startswith("The provided waveform does not have enough space")


def test___analog_single_channel_reader___read_into_undersized_waveform___returns_valid_waveform(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task_with_timing.in_stream)
    samples_to_read = 10

    waveform = AnalogWaveform(samples_to_read - 1)
    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    assert isinstance(waveform, AnalogWaveform)
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == ai_single_channel_task_with_timing.ai_channels[0].name
    assert waveform.units == "Volts"
    assert waveform.sample_count == samples_to_read


def test___analog_single_channel_reader___reuse_waveform_in_place_with_different_sample_counts___populates_valid_waveforms(
    generate_task: Callable[[], nidaqmx.Task], sim_6363_device: nidaqmx.system.Device
) -> None:
    def _make_single_channel_reader(chan_index, offset, samps_per_chan):
        task = generate_task()
        task.ai_channels.add_ai_voltage_chan(
            sim_6363_device.ai_physical_chans[chan_index].name,
            min_val=offset,
            max_val=offset + AI_VOLTAGE_EPSILON,
        )
        task.timing.cfg_samp_clk_timing(
            1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=samps_per_chan
        )
        return AnalogSingleChannelReader(task.in_stream)

    reader0 = _make_single_channel_reader(chan_index=0, offset=0, samps_per_chan=5)
    reader1 = _make_single_channel_reader(chan_index=1, offset=1, samps_per_chan=10)
    reader2 = _make_single_channel_reader(chan_index=2, offset=2, samps_per_chan=15)
    waveform = AnalogWaveform(10, start_index=3, capacity=13)

    reader0.read_waveform(waveform, 5)
    assert waveform.sample_count == 5
    assert waveform.scaled_data == pytest.approx(0, abs=AI_VOLTAGE_EPSILON)
    assert waveform.channel_name == f"{sim_6363_device.name}/ai0"

    reader1.read_waveform(waveform, 10)
    assert waveform.sample_count == 10
    assert waveform.scaled_data == pytest.approx(1, abs=AI_VOLTAGE_EPSILON)
    assert waveform.channel_name == f"{sim_6363_device.name}/ai1"

    reader2.read_waveform(waveform, 15)
    assert waveform.sample_count == 15
    assert waveform.scaled_data == pytest.approx(2, abs=AI_VOLTAGE_EPSILON)
    assert waveform.channel_name == f"{sim_6363_device.name}/ai2"


def test___analog_single_channel_reader___read_waveform_high_sample_rate___returns_correct_sample_interval(
    ai_single_channel_task_with_high_rate: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task_with_high_rate.in_stream)
    samples_to_read = 50
    waveform = AnalogWaveform(samples_to_read)

    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    assert isinstance(waveform, AnalogWaveform)
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 10_000_000)
    assert waveform.channel_name == ai_single_channel_task_with_high_rate.ai_channels[0].name
    assert waveform.units == "Volts"
    assert waveform.sample_count == samples_to_read


def test___analog_single_channel_reader_with_timing_flag___read_waveform___only_includes_timing_data(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    in_stream = ai_single_channel_task_with_timing.in_stream
    in_stream.waveform_attribute_mode = WaveformAttributeMode.TIMING
    reader = AnalogSingleChannelReader(in_stream)
    samples_to_read = 10
    waveform = AnalogWaveform(samples_to_read)

    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    assert isinstance(waveform, AnalogWaveform)
    assert waveform.sample_count == samples_to_read
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == ""
    assert waveform.units == ""


def test___analog_single_channel_reader_with_extended_properties_flag___read_waveform___only_includes_extended_properties(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    in_stream = ai_single_channel_task_with_timing.in_stream
    in_stream.waveform_attribute_mode = WaveformAttributeMode.EXTENDED_PROPERTIES
    reader = AnalogSingleChannelReader(in_stream)
    samples_to_read = 10
    waveform = AnalogWaveform(samples_to_read)

    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    assert isinstance(waveform, AnalogWaveform)
    assert waveform.sample_count == samples_to_read
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.NONE
    assert waveform.channel_name == ai_single_channel_task_with_timing.ai_channels[0].name
    assert waveform.units == "Volts"


def test___analog_single_channel_reader_with_both_flags___read_waveform___includes_both_timing_and_extended_properties(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    in_stream = ai_single_channel_task_with_timing.in_stream
    in_stream.waveform_attribute_mode = (
        WaveformAttributeMode.TIMING | WaveformAttributeMode.EXTENDED_PROPERTIES
    )
    reader = AnalogSingleChannelReader(in_stream)
    samples_to_read = 10
    waveform = AnalogWaveform(samples_to_read)

    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    assert isinstance(waveform, AnalogWaveform)
    assert waveform.sample_count == samples_to_read
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == ai_single_channel_task_with_timing.ai_channels[0].name
    assert waveform.units == "Volts"


def test___analog_single_channel_reader_with_none_flag___read_waveform___minimal_waveform_data(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    in_stream = ai_single_channel_task_with_timing.in_stream
    in_stream.waveform_attribute_mode = WaveformAttributeMode.NONE
    reader = AnalogSingleChannelReader(in_stream)
    samples_to_read = 10
    waveform = AnalogWaveform(samples_to_read)

    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    assert isinstance(waveform, AnalogWaveform)
    assert waveform.sample_count == samples_to_read
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.NONE
    assert waveform.channel_name == ""
    assert waveform.units == ""


def test___analog_single_channel_reader___read_waveform_read_all_available___returns_valid_waveform(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    reader = AnalogSingleChannelReader(ai_single_channel_task_with_timing.in_stream)
    waveform = AnalogWaveform(100)

    samples_read = reader.read_waveform(waveform, READ_ALL_AVAILABLE)

    assert samples_read == 50
    assert isinstance(waveform, AnalogWaveform)
    assert waveform.sample_count == samples_read
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.scaled_data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == ai_single_channel_task_with_timing.ai_channels[0].name
    assert waveform.units == "Volts"
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/stream_readers/test_analog_unscaled_reader.py sha256=e0d8877a4d6c314cf7778be630ef53287106b732ce41ae500d937af4dae32e36 bytes=5811 -->
## FILE: tests/component/stream_readers/test_analog_unscaled_reader.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/stream_readers/test_analog_unscaled_reader.py`
- sha256: `e0d8877a4d6c314cf7778be630ef53287106b732ce41ae500d937af4dae32e36`
- bytes: 5811

````python
from __future__ import annotations

import ctypes
import math

import numpy
import pytest

import nidaqmx
from nidaqmx.stream_readers import AnalogUnscaledReader
from tests.component._analog_utils import (
    VOLTAGE_CODE_EPSILON,
    _get_voltage_code_offset_for_chan,
)


def test___analog_unscaled_reader___read_int16___returns_valid_samples(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogUnscaledReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.int16).min, dtype=numpy.int16
    )

    samples_read = reader.read_int16(data, number_of_samples_per_channel=samples_to_read)

    assert samples_read == samples_to_read
    expected_vals = [
        _get_voltage_code_offset_for_chan(chan_index) for chan_index in range(num_channels)
    ]
    assert data == pytest.approx(expected_vals, abs=VOLTAGE_CODE_EPSILON)


def test___analog_unscaled_reader___read_int16___raises_error_with_correct_dtype(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogUnscaledReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10
    data = numpy.full((num_channels, samples_to_read), math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_int16(data, number_of_samples_per_channel=samples_to_read)

    assert "int16" in exc_info.value.args[0]


def test___analog_unscaled_reader___read_uint16___returns_valid_samples(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogUnscaledReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.uint16).min, dtype=numpy.uint16
    )

    samples_read = reader.read_uint16(data, number_of_samples_per_channel=samples_to_read)

    assert samples_read == samples_to_read
    expected_vals = [
        _get_voltage_code_offset_for_chan(chan_index) for chan_index in range(num_channels)
    ]
    # Promote to larger signed type to avoid overflow w/NumPy 2.0+.
    assert data.astype(numpy.int32) == pytest.approx(expected_vals, abs=VOLTAGE_CODE_EPSILON)


def test___analog_unscaled_reader___read_uint16___raises_error_with_correct_dtype(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogUnscaledReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10
    data = numpy.full((num_channels, samples_to_read), math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_uint16(data, number_of_samples_per_channel=samples_to_read)

    assert "uint16" in exc_info.value.args[0]


def test___analog_unscaled_reader___read_int32___returns_valid_samples(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogUnscaledReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.int32).min, dtype=numpy.int32
    )

    samples_read = reader.read_int32(data, number_of_samples_per_channel=samples_to_read)

    assert samples_read == samples_to_read
    expected_vals = [
        _get_voltage_code_offset_for_chan(chan_index) for chan_index in range(num_channels)
    ]
    assert data == pytest.approx(expected_vals, abs=VOLTAGE_CODE_EPSILON)


def test___analog_unscaled_reader___read_int32___raises_error_with_correct_dtype(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogUnscaledReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10
    data = numpy.full((num_channels, samples_to_read), math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_int32(data, number_of_samples_per_channel=samples_to_read)

    assert "int32" in exc_info.value.args[0]


def test___analog_unscaled_reader___read_uint32___returns_valid_samples(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogUnscaledReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32
    )

    samples_read = reader.read_uint32(data, number_of_samples_per_channel=samples_to_read)

    assert samples_read == samples_to_read
    expected_vals = [
        _get_voltage_code_offset_for_chan(chan_index) for chan_index in range(num_channels)
    ]
    # Promote to larger signed type to avoid overflow w/NumPy 2.0+.
    assert data.astype(numpy.int64) == pytest.approx(expected_vals, abs=VOLTAGE_CODE_EPSILON)


def test___analog_unscaled_reader___read_uint32___raises_error_with_correct_dtype(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = AnalogUnscaledReader(ai_multi_channel_task.in_stream)
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10
    data = numpy.full((num_channels, samples_to_read), math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_uint32(data, number_of_samples_per_channel=samples_to_read)

    assert "uint32" in exc_info.value.args[0]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/stream_readers/test_digital_multi_channel_reader.py sha256=dc94a29c5354b62c2962839d5c1358741b9a8090296015ea2fabfcb4bfab6125 bytes=38972 -->
## FILE: tests/component/stream_readers/test_digital_multi_channel_reader.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/stream_readers/test_digital_multi_channel_reader.py`
- sha256: `dc94a29c5354b62c2962839d5c1358741b9a8090296015ea2fabfcb4bfab6125`
- bytes: 38972

````python
from __future__ import annotations

import ctypes
import math
from collections.abc import Callable

import numpy
import pytest
from hightime import timedelta as ht_timedelta
from nitypes.waveform import DigitalWaveform, SampleIntervalMode

import nidaqmx
import nidaqmx.system
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, FeatureNotSupportedError
from nidaqmx.constants import (
    READ_ALL_AVAILABLE,
    AcquisitionType,
    LineGrouping,
    ReallocationPolicy,
    WaveformAttributeMode,
)
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.stream_readers import DaqError, DigitalMultiChannelReader
from nidaqmx.utils import flatten_channel_string
from tests.component._digital_utils import (
    _bool_array_to_int_lsb,
    _get_digital_data,
    _get_expected_data_for_line,
    _get_expected_digital_port_data_port_major,
    _get_expected_digital_port_data_sample_major,
    _get_num_di_lines_in_task,
    _get_waveform_data,
    _get_waveform_port_data,
    _read_and_copy,
    _validate_waveform_signals,
)
from tests.component._utils import _is_timestamp_close_to_now


def test___digital_multi_channel_reader___read_one_sample_one_line___returns_valid_samples(
    di_single_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_single_line_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_line_task)
    samples_to_read = 256
    sample = numpy.full(num_lines, False, dtype=numpy.bool_)

    data = [_read_and_copy(reader.read_one_sample_one_line, sample) for _ in range(samples_to_read)]

    assert [_bool_array_to_int_lsb(sample) for sample in data] == _get_digital_data(
        num_lines, samples_to_read
    )


def test___digital_multi_channel_reader___read_one_sample_one_line_with_wrong_dtype___raises_error_with_correct_dtype(
    di_single_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_single_line_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_line_task)
    data = numpy.full(num_lines, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample_one_line(data)

    assert "bool" in exc_info.value.args[0]


def test___digital_multi_channel_reader___read_one_sample_multi_line___returns_valid_samples(
    di_multi_channel_multi_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_multi_line_task.in_stream)
    num_channels = di_multi_channel_multi_line_task.number_of_channels
    samples_to_read = 256
    sample = numpy.full((num_channels, 1), False, dtype=numpy.bool_)

    data = [
        _read_and_copy(reader.read_one_sample_multi_line, sample) for _ in range(samples_to_read)
    ]

    assert [_bool_array_to_int_lsb(sample[:, 0]) for sample in data] == _get_digital_data(
        num_channels, samples_to_read
    )


def test___digital_multi_channel_reader___read_one_sample_multi_line_jagged___returns_valid_samples(
    di_multi_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint32_task.in_stream)
    num_channels = di_multi_channel_port_uint32_task.number_of_channels
    samples_to_read = 256
    sample = numpy.full((num_channels, 32), False, dtype=numpy.bool_)

    data = [
        _read_and_copy(reader.read_one_sample_multi_line, sample) for _ in range(samples_to_read)
    ]

    assert [
        [_bool_array_to_int_lsb(sample[chan, :]) for chan in range(num_channels)] for sample in data
    ] == _get_expected_digital_port_data_sample_major(
        di_multi_channel_port_uint32_task, samples_to_read
    )


def test___digital_multi_channel_reader___read_one_sample_multi_line_with_wrong_dtype___raises_error_with_correct_dtype(
    di_multi_channel_multi_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_multi_line_task.in_stream)
    num_channels = di_multi_channel_multi_line_task.number_of_channels
    data = numpy.full((num_channels, 1), math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample_multi_line(data)

    assert "bool" in exc_info.value.args[0]


def test___digital_multi_channel_reader___read_one_sample_port_byte___returns_valid_samples(
    di_multi_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_byte_task.in_stream)
    num_channels = di_multi_channel_port_byte_task.number_of_channels
    samples_to_read = 256
    sample = numpy.full(num_channels, numpy.iinfo(numpy.uint8).min, dtype=numpy.uint8)

    data = [
        _read_and_copy(reader.read_one_sample_port_byte, sample).tolist()
        for _ in range(samples_to_read)
    ]

    assert data == _get_expected_digital_port_data_sample_major(
        di_multi_channel_port_byte_task, samples_to_read
    )


def test___digital_multi_channel_reader___read_one_sample_port_byte_with_wrong_dtype___raises_error_with_correct_dtype(
    di_multi_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_byte_task.in_stream)
    num_channels = di_multi_channel_port_byte_task.number_of_channels
    data = numpy.full(num_channels, numpy.iinfo(numpy.uint16).min, dtype=numpy.uint16)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample_port_byte(data)

    assert "uint8" in exc_info.value.args[0]


def test___digital_multi_channel_reader___read_many_sample_port_byte___returns_valid_samples(
    di_multi_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_byte_task.in_stream)
    num_channels = di_multi_channel_port_byte_task.number_of_channels
    samples_to_read = 256
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.uint8).min, dtype=numpy.uint8
    )

    samples_read = reader.read_many_sample_port_byte(
        data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    assert data.tolist() == _get_expected_digital_port_data_port_major(
        di_multi_channel_port_byte_task, samples_to_read
    )


def test___digital_multi_channel_reader___read_many_sample_port_byte_with_wrong_dtype___raises_error_with_correct_dtype(
    di_multi_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_byte_task.in_stream)
    num_channels = di_multi_channel_port_byte_task.number_of_channels
    samples_to_read = 256
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.uint16).min, dtype=numpy.uint16
    )

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_port_byte(data, number_of_samples_per_channel=samples_to_read)

    assert "uint8" in exc_info.value.args[0]


def test___digital_multi_channel_reader___read_one_sample_port_uint16___returns_valid_samples(
    di_multi_channel_port_uint16_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint16_task.in_stream)
    num_channels = di_multi_channel_port_uint16_task.number_of_channels
    samples_to_read = 256
    sample = numpy.full(num_channels, numpy.iinfo(numpy.uint16).min, dtype=numpy.uint16)

    data = [
        _read_and_copy(reader.read_one_sample_port_uint16, sample).tolist()
        for _ in range(samples_to_read)
    ]

    assert data == _get_expected_digital_port_data_sample_major(
        di_multi_channel_port_uint16_task, samples_to_read
    )


def test___digital_multi_channel_reader___read_one_sample_port_uint16_with_wrong_dtype___raises_error_with_correct_dtype(
    di_multi_channel_port_uint16_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint16_task.in_stream)
    num_channels = di_multi_channel_port_uint16_task.number_of_channels
    data = numpy.full(num_channels, numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample_port_uint16(data)

    assert "uint16" in exc_info.value.args[0]


def test___digital_multi_channel_reader___read_many_sample_port_uint16___returns_valid_samples(
    di_multi_channel_port_uint16_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint16_task.in_stream)
    num_channels = di_multi_channel_port_uint16_task.number_of_channels
    samples_to_read = 256
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.uint16).min, dtype=numpy.uint16
    )

    samples_read = reader.read_many_sample_port_uint16(
        data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    assert data.tolist() == _get_expected_digital_port_data_port_major(
        di_multi_channel_port_uint16_task, samples_to_read
    )


def test___digital_multi_channel_reader___read_many_sample_port_uint16_with_wrong_dtype___raises_error_with_correct_dtype(
    di_multi_channel_port_uint16_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint16_task.in_stream)
    num_channels = di_multi_channel_port_uint16_task.number_of_channels
    samples_to_read = 256
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32
    )

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_port_uint16(data, number_of_samples_per_channel=samples_to_read)

    assert "uint16" in exc_info.value.args[0]


def test___digital_multi_channel_reader___read_one_sample_port_uint32___returns_valid_samples(
    di_multi_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint32_task.in_stream)
    num_channels = di_multi_channel_port_uint32_task.number_of_channels
    samples_to_read = 256
    sample = numpy.full(num_channels, numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)

    data = [
        _read_and_copy(reader.read_one_sample_port_uint32, sample).tolist()
        for _ in range(samples_to_read)
    ]

    assert data == _get_expected_digital_port_data_sample_major(
        di_multi_channel_port_uint32_task, samples_to_read
    )


def test___digital_multi_channel_reader___read_one_sample_port_uint32_with_wrong_dtype___raises_error_with_correct_dtype(
    di_multi_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint32_task.in_stream)
    num_channels = di_multi_channel_port_uint32_task.number_of_channels
    data = numpy.full(num_channels, numpy.iinfo(numpy.uint8).min, dtype=numpy.uint8)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample_port_uint32(data)

    assert "uint32" in exc_info.value.args[0]


def test___digital_multi_channel_reader___read_many_sample_port_uint32___returns_valid_samples(
    di_multi_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint32_task.in_stream)
    num_channels = di_multi_channel_port_uint32_task.number_of_channels
    samples_to_read = 256
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32
    )

    samples_read = reader.read_many_sample_port_uint32(
        data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    assert data.tolist() == _get_expected_digital_port_data_port_major(
        di_multi_channel_port_uint32_task, samples_to_read
    )


def test___digital_multi_channel_reader___read_many_sample_port_uint32_with_wrong_dtype___raises_error_with_correct_dtype(
    di_multi_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_channel_port_uint32_task.in_stream)
    num_channels = di_multi_channel_port_uint32_task.number_of_channels
    samples_to_read = 256
    data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.uint8).min, dtype=numpy.uint8
    )

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_port_uint32(data, number_of_samples_per_channel=samples_to_read)

    assert "uint32" in exc_info.value.args[0]


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
def test___digital_multi_channel_multi_line_reader___read_waveforms_feature_disabled___raises_feature_not_supported_error(
    di_multi_chan_multi_line_timing_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_chan_multi_line_timing_task.in_stream)
    waveforms = [DigitalWaveform(50) for _ in range(8)]

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        reader.read_waveforms(waveforms)

    error_message = exc_info.value.args[0]
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message
    assert "NIDAQMX_ENABLE_WAVEFORM_SUPPORT" in error_message


def test___digital_multi_channel_multi_line_reader___read_waveforms___returns_valid_waveforms(
    di_multi_chan_multi_line_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_chan_multi_line_timing_task.in_stream)
    num_channels = di_multi_chan_multi_line_timing_task.number_of_channels
    num_lines = _get_num_di_lines_in_task(di_multi_chan_multi_line_timing_task)
    samples_to_read = 10
    waveforms = [DigitalWaveform(samples_to_read) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 8
    assert num_lines == 8
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(samples_to_read, chan)
        assert _is_timestamp_close_to_now(waveform.timing.timestamp)
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert waveform.channel_name == di_multi_chan_multi_line_timing_task.di_channels[chan].name
        assert waveform.sample_count == samples_to_read
        _validate_waveform_signals(sim_6363_device, waveform, [chan])


def test___digital_multi_channel_different_lines_reader___read_waveforms___returns_valid_waveforms(
    di_multi_chan_diff_lines_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_chan_diff_lines_timing_task.in_stream)
    num_channels = di_multi_chan_diff_lines_timing_task.number_of_channels
    num_lines = _get_num_di_lines_in_task(di_multi_chan_diff_lines_timing_task)
    samples_to_read = 10
    waveforms = [
        DigitalWaveform(samples_to_read, 1),
        DigitalWaveform(samples_to_read, 2),
        DigitalWaveform(samples_to_read, 4),
    ]

    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 3
    assert num_lines == 7
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert _get_waveform_data(waveforms[0]) == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    assert _is_timestamp_close_to_now(waveforms[0].timing.timestamp)
    assert waveforms[0].sample_count == samples_to_read
    assert waveforms[0].timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveforms[0].channel_name == di_multi_chan_diff_lines_timing_task.di_channels[0].name
    _validate_waveform_signals(sim_6363_device, waveforms[0], [0])
    assert _get_waveform_data(waveforms[1]) == [0, 0, 1, 1, 2, 2, 3, 3, 0, 0]
    assert _is_timestamp_close_to_now(waveforms[1].timing.timestamp)
    assert waveforms[1].sample_count == samples_to_read
    assert waveforms[1].timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveforms[1].channel_name == di_multi_chan_diff_lines_timing_task.di_channels[1].name
    _validate_waveform_signals(sim_6363_device, waveforms[1], [2, 1])
    assert _get_waveform_data(waveforms[2]) == [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
    assert _is_timestamp_close_to_now(waveforms[2].timing.timestamp)
    assert waveforms[2].sample_count == samples_to_read
    assert waveforms[2].timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveforms[2].channel_name == di_multi_chan_diff_lines_timing_task.di_channels[2].name
    _validate_waveform_signals(sim_6363_device, waveforms[2], [6, 5, 4, 3])


def test___digital_multi_channel_lines_and_port_reader___read_waveforms___returns_valid_waveforms(
    di_multi_chan_lines_and_port_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_chan_lines_and_port_task.in_stream)
    num_channels = di_multi_chan_lines_and_port_task.number_of_channels
    num_lines = _get_num_di_lines_in_task(di_multi_chan_lines_and_port_task)
    samples_to_read = 10
    waveforms = [
        DigitalWaveform(samples_to_read, 1),
        DigitalWaveform(samples_to_read, 2),
        DigitalWaveform(samples_to_read, 4),
        DigitalWaveform(samples_to_read, 8),
    ]

    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 4
    assert num_lines == 15
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert _get_waveform_data(waveforms[0]) == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    assert _is_timestamp_close_to_now(waveforms[0].timing.timestamp)
    assert waveforms[0].sample_count == samples_to_read
    assert waveforms[0].channel_name == di_multi_chan_lines_and_port_task.di_channels[0].name
    _validate_waveform_signals(sim_6363_device, waveforms[0], [0])
    assert _get_waveform_data(waveforms[1]) == [0, 0, 1, 1, 2, 2, 3, 3, 0, 0]
    assert _is_timestamp_close_to_now(waveforms[1].timing.timestamp)
    assert waveforms[1].sample_count == samples_to_read
    assert waveforms[1].channel_name == di_multi_chan_lines_and_port_task.di_channels[1].name
    _validate_waveform_signals(sim_6363_device, waveforms[1], [2, 1])
    assert _get_waveform_data(waveforms[2]) == [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
    assert _is_timestamp_close_to_now(waveforms[2].timing.timestamp)
    assert waveforms[2].sample_count == samples_to_read
    assert waveforms[2].channel_name == di_multi_chan_lines_and_port_task.di_channels[2].name
    _validate_waveform_signals(sim_6363_device, waveforms[2], [6, 5, 4, 3])
    assert _get_waveform_port_data(waveforms[3]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert _is_timestamp_close_to_now(waveforms[3].timing.timestamp)
    assert waveforms[3].sample_count == samples_to_read
    assert waveforms[3].channel_name == di_multi_chan_lines_and_port_task.di_channels[3].name
    _validate_waveform_signals(sim_6363_device, waveforms[3], range(32, 40))


def test___digital_multi_channel_different_lines_reader___read_mismatched_waveforms___throws_exception(
    di_multi_chan_diff_lines_timing_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_chan_diff_lines_timing_task.in_stream)
    samples_to_read = 10
    waveforms = [
        DigitalWaveform(samples_to_read, 1),
        DigitalWaveform(
            samples_to_read, 3
        ),  # mismatch - actually only two signals for this channel
        DigitalWaveform(samples_to_read, 4),
    ]

    with pytest.raises(ValueError) as exc_info:
        reader.read_waveforms(waveforms, samples_to_read)

    error_message = exc_info.value.args[0]
    assert "2" in error_message


def test___digital_multi_channel_multi_line_reader___read_waveforms_no_args___returns_valid_waveforms(
    di_multi_chan_multi_line_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_chan_multi_line_timing_task.in_stream)
    num_channels = di_multi_chan_multi_line_timing_task.number_of_channels
    num_lines = _get_num_di_lines_in_task(di_multi_chan_multi_line_timing_task)
    waveforms = [DigitalWaveform(50) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms)

    assert samples_read == 50
    assert num_channels == 8
    assert num_lines == 8
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(50, chan)
        assert _is_timestamp_close_to_now(waveform.timing.timestamp)
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert waveform.channel_name == di_multi_chan_multi_line_timing_task.di_channels[chan].name
        assert waveform.sample_count == 50
        _validate_waveform_signals(sim_6363_device, waveform, [chan])


def test___digital_multi_channel_multi_line_reader___read_waveforms_in_place___populates_valid_waveforms(
    di_multi_chan_multi_line_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_chan_multi_line_timing_task.in_stream)
    num_channels = di_multi_chan_multi_line_timing_task.number_of_channels
    num_lines = _get_num_di_lines_in_task(di_multi_chan_multi_line_timing_task)
    samples_to_read = 10

    waveforms = [DigitalWaveform(samples_to_read) for _ in range(num_channels)]
    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 8
    assert num_lines == 8
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(samples_to_read, chan)
        assert _is_timestamp_close_to_now(waveform.timing.timestamp)
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert waveform.channel_name == di_multi_chan_multi_line_timing_task.di_channels[chan].name
        assert waveform.sample_count == samples_to_read
        _validate_waveform_signals(sim_6363_device, waveform, [chan])


def test___digital_multi_channel_multi_line_reader___reuse_waveform_in_place___overwrites_data_timing_and_attributes(
    generate_task: Callable[[], nidaqmx.Task], sim_6363_device: nidaqmx.system.Device
) -> None:
    def _make_multi_channel_multi_line_reader(lines_start, rate):
        task = generate_task()
        task.di_channels.add_di_chan(
            flatten_channel_string(
                sim_6363_device.di_lines.channel_names[lines_start : lines_start + 4]
            ),
            line_grouping=LineGrouping.CHAN_PER_LINE,
        )
        task.timing.cfg_samp_clk_timing(rate, sample_mode=AcquisitionType.FINITE, samps_per_chan=10)
        return DigitalMultiChannelReader(task.in_stream)

    sample_count = 10
    num_channels = 4
    reader0 = _make_multi_channel_multi_line_reader(lines_start=0, rate=1000.0)
    reader1 = _make_multi_channel_multi_line_reader(lines_start=1, rate=2000.0)
    waveforms = [DigitalWaveform(sample_count) for _ in range(num_channels)]

    reader0.read_waveforms(waveforms, sample_count)
    timestamps0 = [wf.timing.timestamp for wf in waveforms]
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(sample_count, chan)
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert waveform.channel_name == sim_6363_device.di_lines[chan].name
        _validate_waveform_signals(sim_6363_device, waveform, [chan])

    reader1.read_waveforms(waveforms, sample_count)
    timestamps1 = [wf.timing.timestamp for wf in waveforms]
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(sample_count, chan + 1)
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 2000)
        assert waveform.channel_name == sim_6363_device.di_lines[chan + 1].name
        _validate_waveform_signals(sim_6363_device, waveform, [chan + 1])

    for ts0, ts1 in zip(timestamps0, timestamps1):
        assert ts1 > ts0


def test___digital_multi_channel_multi_line_reader___read_into_undersized_waveforms_without_reallocation___throws_exception(
    di_multi_chan_multi_line_timing_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_chan_multi_line_timing_task.in_stream)
    num_channels = di_multi_chan_multi_line_timing_task.number_of_channels
    samples_to_read = 10

    waveforms = [DigitalWaveform(samples_to_read - 1) for _ in range(num_channels)]
    with pytest.raises(DaqError) as exc_info:
        reader.read_waveforms(waveforms, samples_to_read, ReallocationPolicy.DO_NOT_REALLOCATE)

    assert exc_info.value.error_code == DAQmxErrors.READ_BUFFER_TOO_SMALL
    assert exc_info.value.args[0].startswith("The waveform at index 0 does not have enough space")


def test___digital_multi_channel_multi_line_reader___read_into_undersized_waveforms___returns_valid_waveforms(
    di_multi_chan_multi_line_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_chan_multi_line_timing_task.in_stream)
    num_channels = di_multi_chan_multi_line_timing_task.number_of_channels
    num_lines = _get_num_di_lines_in_task(di_multi_chan_multi_line_timing_task)
    samples_to_read = 10

    waveforms = [DigitalWaveform(samples_to_read - 1) for _ in range(num_channels)]
    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 8
    assert num_lines == 8
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(samples_to_read, chan)
        assert _is_timestamp_close_to_now(waveform.timing.timestamp)
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert waveform.channel_name == di_multi_chan_multi_line_timing_task.di_channels[chan].name
        assert waveform.sample_count == samples_to_read
        _validate_waveform_signals(sim_6363_device, waveform, [chan])


def test___digital_multi_channel_reader___reuse_waveform_in_place_with_different_sample_counts___populates_valid_waveforms(
    generate_task: Callable[[], nidaqmx.Task], sim_6363_device: nidaqmx.system.Device
) -> None:
    def _make_multi_channel_reader(chan_a_index, chan_b_index, samps_per_chan):
        task = generate_task()
        task.di_channels.add_di_chan(
            sim_6363_device.di_lines[chan_a_index].name,
            line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
        )
        task.di_channels.add_di_chan(
            sim_6363_device.di_lines[chan_b_index].name,
            line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
        )
        task.timing.cfg_samp_clk_timing(
            1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=samps_per_chan
        )
        return DigitalMultiChannelReader(task.in_stream)

    reader0 = _make_multi_channel_reader(chan_a_index=0, chan_b_index=1, samps_per_chan=5)
    reader1 = _make_multi_channel_reader(chan_a_index=2, chan_b_index=3, samps_per_chan=10)
    reader2 = _make_multi_channel_reader(chan_a_index=4, chan_b_index=5, samps_per_chan=15)
    waveforms = [
        DigitalWaveform(10),
        DigitalWaveform(10, start_index=3, capacity=13),
    ]

    reader0.read_waveforms(waveforms, 5)
    assert waveforms[0].sample_count == 5
    assert _get_waveform_data(waveforms[0]) == _get_expected_data_for_line(5, 0)
    _validate_waveform_signals(sim_6363_device, waveforms[0], [0])
    assert waveforms[0].channel_name == f"{sim_6363_device.name}/port0/line0"
    assert waveforms[1].sample_count == 5
    assert _get_waveform_data(waveforms[1]) == _get_expected_data_for_line(5, 1)
    _validate_waveform_signals(sim_6363_device, waveforms[1], [1])
    assert waveforms[1].channel_name == f"{sim_6363_device.name}/port0/line1"

    reader1.read_waveforms(waveforms, 10)
    assert waveforms[0].sample_count == 10
    assert _get_waveform_data(waveforms[0]) == _get_expected_data_for_line(10, 2)
    _validate_waveform_signals(sim_6363_device, waveforms[0], [2])
    assert waveforms[0].channel_name == f"{sim_6363_device.name}/port0/line2"
    assert waveforms[1].sample_count == 10
    assert _get_waveform_data(waveforms[1]) == _get_expected_data_for_line(10, 3)
    _validate_waveform_signals(sim_6363_device, waveforms[1], [3])
    assert waveforms[1].channel_name == f"{sim_6363_device.name}/port0/line3"

    reader2.read_waveforms(waveforms, 15)
    assert waveforms[0].sample_count == 15
    assert _get_waveform_data(waveforms[0]) == _get_expected_data_for_line(15, 4)
    _validate_waveform_signals(sim_6363_device, waveforms[0], [4])
    assert waveforms[0].channel_name == f"{sim_6363_device.name}/port0/line4"
    assert waveforms[1].sample_count == 15
    assert _get_waveform_data(waveforms[1]) == _get_expected_data_for_line(15, 5)
    _validate_waveform_signals(sim_6363_device, waveforms[1], [5])
    assert waveforms[1].channel_name == f"{sim_6363_device.name}/port0/line5"


def test___digital_multi_channel_multi_line_reader___read_with_wrong_number_of_waveforms___throws_exception(
    di_multi_chan_multi_line_timing_task: nidaqmx.Task,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_chan_multi_line_timing_task.in_stream)
    num_channels = di_multi_chan_multi_line_timing_task.number_of_channels
    samples_to_read = 10

    waveforms = [DigitalWaveform(samples_to_read) for _ in range(num_channels - 1)]
    with pytest.raises(DaqError) as exc_info:
        reader.read_waveforms(waveforms, samples_to_read)

    assert exc_info.value.error_code == DAQmxErrors.MISMATCHED_INPUT_ARRAY_SIZES
    assert "does not match the number of channels" in exc_info.value.args[0]


def test___digital_multi_channel_multi_line_reader_with_timing_flag___read_waveforms___only_includes_timing_data(
    di_multi_chan_multi_line_timing_task: nidaqmx.Task,
) -> None:
    in_stream = di_multi_chan_multi_line_timing_task.in_stream
    in_stream.waveform_attribute_mode = WaveformAttributeMode.TIMING
    reader = DigitalMultiChannelReader(in_stream)
    num_channels = di_multi_chan_multi_line_timing_task.number_of_channels
    num_lines = _get_num_di_lines_in_task(di_multi_chan_multi_line_timing_task)
    samples_to_read = 10
    waveforms = [DigitalWaveform(samples_to_read) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 8
    assert num_lines == 8
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(samples_to_read, chan)
        assert _is_timestamp_close_to_now(waveform.timing.timestamp)
        assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert waveform.channel_name == ""
        assert waveform.sample_count == samples_to_read


def test___digital_multi_channel_multi_line_reader_with_extended_properties_flag___read_waveforms___only_includes_extended_properties(
    di_multi_chan_multi_line_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    in_stream = di_multi_chan_multi_line_timing_task.in_stream
    in_stream.waveform_attribute_mode = WaveformAttributeMode.EXTENDED_PROPERTIES
    reader = DigitalMultiChannelReader(in_stream)
    num_channels = di_multi_chan_multi_line_timing_task.number_of_channels
    num_lines = _get_num_di_lines_in_task(di_multi_chan_multi_line_timing_task)
    samples_to_read = 10
    waveforms = [DigitalWaveform(samples_to_read) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 8
    assert num_lines == 8
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(samples_to_read, chan)
        assert waveform.timing.sample_interval_mode == SampleIntervalMode.NONE
        assert waveform.channel_name == di_multi_chan_multi_line_timing_task.di_channels[chan].name
        assert waveform.sample_count == samples_to_read
        _validate_waveform_signals(sim_6363_device, waveform, [chan])


def test___digital_multi_channel_multi_line_reader_with_both_flags___read_waveforms___includes_both_timing_and_extended_properties(
    di_multi_chan_multi_line_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    in_stream = di_multi_chan_multi_line_timing_task.in_stream
    in_stream.waveform_attribute_mode = (
        WaveformAttributeMode.TIMING | WaveformAttributeMode.EXTENDED_PROPERTIES
    )
    reader = DigitalMultiChannelReader(in_stream)
    num_channels = di_multi_chan_multi_line_timing_task.number_of_channels
    num_lines = _get_num_di_lines_in_task(di_multi_chan_multi_line_timing_task)
    samples_to_read = 10
    waveforms = [DigitalWaveform(samples_to_read) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 8
    assert num_lines == 8
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(samples_to_read, chan)
        assert _is_timestamp_close_to_now(waveform.timing.timestamp)
        assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert waveform.channel_name == di_multi_chan_multi_line_timing_task.di_channels[chan].name
        assert waveform.sample_count == samples_to_read
        _validate_waveform_signals(sim_6363_device, waveform, [chan])


def test___digital_multi_channel_multi_line_reader_with_none_flag___read_waveforms___minimal_waveform_data(
    di_multi_chan_multi_line_timing_task: nidaqmx.Task,
) -> None:
    in_stream = di_multi_chan_multi_line_timing_task.in_stream
    in_stream.waveform_attribute_mode = WaveformAttributeMode.NONE
    reader = DigitalMultiChannelReader(in_stream)
    num_channels = di_multi_chan_multi_line_timing_task.number_of_channels
    num_lines = _get_num_di_lines_in_task(di_multi_chan_multi_line_timing_task)
    samples_to_read = 10
    waveforms = [DigitalWaveform(samples_to_read) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms, samples_to_read)

    assert samples_read == samples_to_read
    assert num_channels == 8
    assert num_lines == 8
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(samples_to_read, chan)
        assert waveform.timing.sample_interval_mode == SampleIntervalMode.NONE
        assert waveform.channel_name == ""
        assert waveform.sample_count == samples_to_read


@pytest.mark.parametrize(
    "dtype",
    [
        numpy.bool,
        numpy.int8,
        numpy.uint8,
    ],
)
def test___digital_multi_channel_multi_line_reader___read_waveform_all_dtypes___returns_valid_waveform(
    di_multi_chan_multi_line_timing_task: nidaqmx.Task,
    dtype,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    in_stream = di_multi_chan_multi_line_timing_task.in_stream
    reader = DigitalMultiChannelReader(in_stream)
    num_channels = 8
    num_samples = 10
    waveforms = [DigitalWaveform(num_samples, dtype=dtype) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms, num_samples)

    assert samples_read == num_samples
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(num_samples, chan)
        _validate_waveform_signals(sim_6363_device, waveform, [chan])


def test___digital_multi_channel_multi_line_reader___read_waveforms_read_all_available___returns_valid_waveforms(
    di_multi_chan_multi_line_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    reader = DigitalMultiChannelReader(di_multi_chan_multi_line_timing_task.in_stream)
    num_channels = di_multi_chan_multi_line_timing_task.number_of_channels
    num_lines = _get_num_di_lines_in_task(di_multi_chan_multi_line_timing_task)
    waveforms = [DigitalWaveform(100) for _ in range(num_channels)]

    samples_read = reader.read_waveforms(waveforms, READ_ALL_AVAILABLE)

    assert samples_read == 50
    assert num_channels == 8
    assert num_lines == 8
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(samples_read, chan)
        assert _is_timestamp_close_to_now(waveform.timing.timestamp)
        assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
        assert waveform.channel_name == di_multi_chan_multi_line_timing_task.di_channels[chan].name
        assert waveform.sample_count == samples_read
        _validate_waveform_signals(sim_6363_device, waveform, [chan])
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/stream_readers/test_digital_single_channel_reader.py sha256=e1a16c5c6d28dfdcb5216f7a087f716d37dbb9cfcb5642864793e0b67c93c43d bytes=29514 -->
## FILE: tests/component/stream_readers/test_digital_single_channel_reader.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/stream_readers/test_digital_single_channel_reader.py`
- sha256: `e1a16c5c6d28dfdcb5216f7a087f716d37dbb9cfcb5642864793e0b67c93c43d`
- bytes: 29514

````python
from __future__ import annotations

import ctypes
import math
from collections.abc import Callable

import numpy
import pytest
from hightime import timedelta as ht_timedelta
from nitypes.waveform import DigitalWaveform, SampleIntervalMode

import nidaqmx
import nidaqmx.system
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, FeatureNotSupportedError
from nidaqmx.constants import (
    READ_ALL_AVAILABLE,
    AcquisitionType,
    LineGrouping,
    ReallocationPolicy,
    WaveformAttributeMode,
)
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.stream_readers import DaqError, DigitalSingleChannelReader
from nidaqmx.utils import flatten_channel_string
from tests.component._digital_utils import (
    _bool_array_to_int_lsb,
    _get_digital_data,
    _get_expected_data_for_line,
    _get_num_di_lines_in_task,
    _get_waveform_data,
    _get_waveform_port_data,
    _read_and_copy,
    _validate_waveform_signals,
)
from tests.component._utils import _is_timestamp_close_to_now


def test___digital_single_channel_reader___read_one_sample_one_line___returns_valid_samples(
    di_single_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_line_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_line_task)
    samples_to_read = 256

    data = [reader.read_one_sample_one_line() for _ in range(samples_to_read)]

    assert data == _get_digital_data(num_lines, samples_to_read)


def test___digital_single_channel_reader___read_one_sample_multi_line___returns_valid_samples(
    di_single_channel_multi_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_multi_line_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_channel_multi_line_task)
    samples_to_read = 256
    sample = numpy.full(num_lines, False, dtype=numpy.bool_)

    data = [
        _read_and_copy(reader.read_one_sample_multi_line, sample) for _ in range(samples_to_read)
    ]

    assert [_bool_array_to_int_lsb(sample) for sample in data] == _get_digital_data(
        num_lines, samples_to_read
    )


def test___digital_single_channel_reader___read_one_sample_multi_line_with_wrong_dtype___raises_error_with_correct_dtype(
    di_single_channel_multi_line_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_multi_line_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_channel_multi_line_task)
    data = numpy.full(num_lines, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample_multi_line(data)

    assert "bool" in exc_info.value.args[0]


def test___digital_single_channel_reader___read_one_sample_port_byte___returns_valid_samples(
    di_single_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_byte_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_channel_port_byte_task)
    samples_to_read = 256

    data = [reader.read_one_sample_port_byte() for _ in range(samples_to_read)]

    assert data == _get_digital_data(num_lines, samples_to_read)


def test___digital_single_channel_reader___read_one_sample_port_uint16___returns_valid_samples(
    di_single_channel_port_uint16_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_uint16_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_channel_port_uint16_task)
    samples_to_read = 256

    data = [reader.read_one_sample_port_uint16() for _ in range(samples_to_read)]

    assert data == _get_digital_data(num_lines, samples_to_read)


def test___digital_single_channel_reader___read_one_sample_port_uint32___returns_valid_samples(
    di_single_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_uint32_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_channel_port_uint32_task)
    samples_to_read = 256

    data = [reader.read_one_sample_port_uint32() for _ in range(samples_to_read)]

    assert data == _get_digital_data(num_lines, samples_to_read)


def test___digital_single_channel_reader___read_many_sample_port_byte___returns_valid_samples(
    di_single_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_byte_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_channel_port_byte_task)
    samples_to_read = 256
    data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint8).min, dtype=numpy.uint8)

    samples_read = reader.read_many_sample_port_byte(
        data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    assert data.tolist() == _get_digital_data(num_lines, samples_to_read)


def test___digital_single_channel_reader___read_many_sample_port_byte_with_wrong_dtype___raises_error_with_correct_dtype(
    di_single_channel_port_byte_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_byte_task.in_stream)
    samples_to_read = 256
    data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint16).min, dtype=numpy.uint16)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_port_byte(data, number_of_samples_per_channel=samples_to_read)

    assert "uint8" in exc_info.value.args[0]


def test___digital_single_channel_reader___read_many_sample_port_uint16___returns_valid_samples(
    di_single_channel_port_uint16_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_uint16_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_channel_port_uint16_task)
    samples_to_read = 256
    data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint16).min, dtype=numpy.uint16)

    samples_read = reader.read_many_sample_port_uint16(
        data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    assert data.tolist() == _get_digital_data(num_lines, samples_to_read)


def test___digital_single_channel_reader___read_many_sample_port_uint16_with_wrong_dtype___raises_error_with_correct_dtype(
    di_single_channel_port_uint16_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_uint16_task.in_stream)
    samples_to_read = 256
    data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_port_uint16(data, number_of_samples_per_channel=samples_to_read)

    assert "uint16" in exc_info.value.args[0]


def test___digital_single_channel_reader___read_many_sample_port_uint32___returns_valid_samples(
    di_single_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_uint32_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_channel_port_uint32_task)
    samples_to_read = 256
    data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint32).min, dtype=numpy.uint32)

    samples_read = reader.read_many_sample_port_uint32(
        data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    assert data.tolist() == _get_digital_data(num_lines, samples_to_read)


def test___digital_single_channel_reader___read_many_sample_port_uint32_with_wrong_dtype___raises_error_with_correct_dtype(
    di_single_channel_port_uint32_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_uint32_task.in_stream)
    samples_to_read = 256
    data = numpy.full(samples_to_read, numpy.iinfo(numpy.uint8).min, dtype=numpy.uint8)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample_port_uint32(data, number_of_samples_per_channel=samples_to_read)

    assert "uint32" in exc_info.value.args[0]


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
def test___digital_single_line_reader___read_waveform_feature_disabled___raises_feature_not_supported_error(
    di_single_line_timing_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_line_timing_task.in_stream)
    waveform = DigitalWaveform(50)

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        reader.read_waveform(waveform)

    error_message = exc_info.value.args[0]
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message
    assert "NIDAQMX_ENABLE_WAVEFORM_SUPPORT" in error_message


def test___digital_single_line_reader___read_waveform___returns_valid_waveform(
    di_single_line_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    reader = DigitalSingleChannelReader(di_single_line_timing_task.in_stream)
    samples_to_read = 10
    waveform = DigitalWaveform(samples_to_read)

    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    assert _get_waveform_data(waveform) == _get_digital_data(1, samples_to_read)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.channel_name == di_single_line_timing_task.di_channels[0].name
    _validate_waveform_signals(sim_6363_device, waveform, [0])


def test___digital_single_channel_multi_line_reader___read_waveform___returns_valid_waveform(
    di_single_channel_multi_line_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_multi_line_timing_task.in_stream)
    samples_to_read = 10
    num_lines = _get_num_di_lines_in_task(di_single_channel_multi_line_timing_task)
    waveform = DigitalWaveform(samples_to_read, num_lines)

    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    assert _get_waveform_data(waveform) == _get_digital_data(num_lines, samples_to_read)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.channel_name == di_single_channel_multi_line_timing_task.di_channels[0].name
    _validate_waveform_signals(sim_6363_device, waveform, [7, 6, 5, 4, 3, 2, 1, 0])


def test___digital_single_line_reader___read_waveform_no_args___returns_valid_waveform(
    di_single_line_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    reader = DigitalSingleChannelReader(di_single_line_timing_task.in_stream)
    waveform = DigitalWaveform(50)

    samples_read = reader.read_waveform(waveform)

    assert samples_read == 50
    assert _get_waveform_data(waveform) == _get_digital_data(1, 50)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.channel_name == di_single_line_timing_task.di_channels[0].name
    _validate_waveform_signals(sim_6363_device, waveform, [0])


def test___digital_single_channel_multi_line_reader___read_waveform_no_args___returns_valid_waveform(
    di_single_channel_multi_line_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_multi_line_timing_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_channel_multi_line_timing_task)
    waveform = DigitalWaveform(50, num_lines)

    samples_read = reader.read_waveform(waveform)

    assert samples_read == 50
    assert _get_waveform_data(waveform) == _get_digital_data(num_lines, 50)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.channel_name == di_single_channel_multi_line_timing_task.di_channels[0].name
    _validate_waveform_signals(sim_6363_device, waveform, range(num_lines)[::-1])


def test___digital_single_line_reader___read_waveform_in_place___returns_valid_waveform(
    di_single_line_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    reader = DigitalSingleChannelReader(di_single_line_timing_task.in_stream)
    waveform = DigitalWaveform(50)

    samples_read = reader.read_waveform(waveform)

    assert samples_read == 50
    assert _get_waveform_data(waveform) == _get_digital_data(1, 50)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == di_single_line_timing_task.di_channels[0].name
    _validate_waveform_signals(sim_6363_device, waveform, [0])


def test___digital_single_channel_multi_line_reader___read_waveform_in_place___returns_valid_waveform(
    di_single_channel_multi_line_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_multi_line_timing_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_channel_multi_line_timing_task)
    waveform = DigitalWaveform(sample_count=50, signal_count=8)

    samples_read = reader.read_waveform(waveform)

    assert samples_read == 50
    assert _get_waveform_data(waveform) == _get_digital_data(num_lines, 50)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == di_single_channel_multi_line_timing_task.di_channels[0].name
    _validate_waveform_signals(sim_6363_device, waveform, range(num_lines)[::-1])


def test___digital_single_line_reader___reuse_waveform_in_place___overwrites_data_timing_and_attributes(
    generate_task: Callable[[], nidaqmx.Task], sim_6363_device: nidaqmx.system.Device
) -> None:
    def _make_single_line_reader(chan_index, rate):
        task = generate_task()
        task.di_channels.add_di_chan(
            sim_6363_device.di_lines[chan_index].name,
            line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
        )
        task.timing.cfg_samp_clk_timing(rate, sample_mode=AcquisitionType.FINITE, samps_per_chan=10)
        return DigitalSingleChannelReader(task.in_stream)

    sample_count = 10
    reader0 = _make_single_line_reader(chan_index=0, rate=1000.0)
    reader1 = _make_single_line_reader(chan_index=1, rate=2000.0)
    waveform = DigitalWaveform(sample_count)

    reader0.read_waveform(waveform, sample_count)
    timestamp0 = waveform.timing.timestamp
    assert _get_waveform_data(waveform) == _get_expected_data_for_line(sample_count, 0)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == sim_6363_device.di_lines[0].name
    _validate_waveform_signals(sim_6363_device, waveform, [0])

    reader1.read_waveform(waveform, sample_count)
    timestamp1 = waveform.timing.timestamp
    assert _get_waveform_data(waveform) == _get_expected_data_for_line(sample_count, 1)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 2000)
    assert waveform.channel_name == sim_6363_device.di_lines[1].name
    _validate_waveform_signals(sim_6363_device, waveform, [1])

    assert timestamp1 > timestamp0


def test___digital_single_channel_multi_line_reader___reuse_waveform_in_place___overwrites_data_timing_and_attributes(
    generate_task: Callable[[], nidaqmx.Task], sim_6363_device: nidaqmx.system.Device
) -> None:
    def _make_single_channel_multi_line_reader(lines_start, rate):
        task = generate_task()
        task.di_channels.add_di_chan(
            flatten_channel_string(
                sim_6363_device.di_lines.channel_names[lines_start : lines_start + 4]
            ),
            line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
        )
        task.timing.cfg_samp_clk_timing(rate, sample_mode=AcquisitionType.FINITE, samps_per_chan=10)
        return DigitalSingleChannelReader(task.in_stream)

    sample_count = 10
    signal_count = 4
    reader0 = _make_single_channel_multi_line_reader(lines_start=0, rate=1000.0)
    reader1 = _make_single_channel_multi_line_reader(lines_start=1, rate=2000.0)
    waveform = DigitalWaveform(sample_count, signal_count)

    reader0.read_waveform(waveform, sample_count)
    timestamp0 = waveform.timing.timestamp
    assert _get_waveform_data(waveform) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == f"{sim_6363_device.di_lines[0].name}..."
    _validate_waveform_signals(sim_6363_device, waveform, [3, 2, 1, 0])

    reader1.read_waveform(waveform, sample_count)
    timestamp1 = waveform.timing.timestamp
    assert _get_waveform_data(waveform) == [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 2000)
    assert waveform.channel_name == f"{sim_6363_device.di_lines[1].name}..."
    _validate_waveform_signals(sim_6363_device, waveform, [4, 3, 2, 1])

    assert timestamp1 > timestamp0


def test___digital_single_line_reader___read_into_undersized_waveform_without_reallocation___throws_exception(
    di_single_line_timing_task: nidaqmx.Task,
) -> None:
    reader = DigitalSingleChannelReader(di_single_line_timing_task.in_stream)
    samples_to_read = 10

    waveform = DigitalWaveform(samples_to_read - 1)
    with pytest.raises(DaqError) as exc_info:
        reader.read_waveform(waveform, samples_to_read, ReallocationPolicy.DO_NOT_REALLOCATE)

    assert exc_info.value.error_code == DAQmxErrors.READ_BUFFER_TOO_SMALL
    assert exc_info.value.args[0].startswith(
        "The waveform does not have enough space (9) to hold the requested number of samples (10)."
    )


def test___digital_single_line_reader___read_into_undersized_waveform___returns_valid_waveform(
    di_single_line_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    reader = DigitalSingleChannelReader(di_single_line_timing_task.in_stream)
    samples_to_read = 10

    waveform = DigitalWaveform(samples_to_read - 1)
    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    assert _get_waveform_data(waveform) == _get_digital_data(1, samples_to_read)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.channel_name == di_single_line_timing_task.di_channels[0].name
    _validate_waveform_signals(sim_6363_device, waveform, [0])


def test___digital_single_channel_reader___reuse_waveform_in_place_with_different_sample_counts___populates_valid_waveforms(
    generate_task: Callable[[], nidaqmx.Task], sim_6363_device: nidaqmx.system.Device
) -> None:
    def _make_single_channel_reader(chan_index, samps_per_chan):
        task = generate_task()
        task.di_channels.add_di_chan(
            sim_6363_device.di_lines[chan_index].name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
        )
        task.timing.cfg_samp_clk_timing(
            1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=samps_per_chan
        )
        return DigitalSingleChannelReader(task.in_stream)

    reader0 = _make_single_channel_reader(chan_index=0, samps_per_chan=5)
    reader1 = _make_single_channel_reader(chan_index=1, samps_per_chan=10)
    reader2 = _make_single_channel_reader(chan_index=2, samps_per_chan=15)
    waveform = DigitalWaveform(10, start_index=3, capacity=13)

    reader0.read_waveform(waveform, 5)
    assert waveform.sample_count == 5
    assert _get_waveform_data(waveform) == _get_expected_data_for_line(5, 0)
    assert waveform.channel_name == f"{sim_6363_device.name}/port0/line0"
    _validate_waveform_signals(sim_6363_device, waveform, [0])

    reader1.read_waveform(waveform, 10)
    assert waveform.sample_count == 10
    assert _get_waveform_data(waveform) == _get_expected_data_for_line(10, 1)
    assert waveform.channel_name == f"{sim_6363_device.name}/port0/line1"
    _validate_waveform_signals(sim_6363_device, waveform, [1])

    reader2.read_waveform(waveform, 15)
    assert waveform.sample_count == 15
    assert _get_waveform_data(waveform) == _get_expected_data_for_line(15, 2)
    assert waveform.channel_name == f"{sim_6363_device.name}/port0/line2"
    _validate_waveform_signals(sim_6363_device, waveform, [2])


def test___digital_single_line_reader___read_waveform_high_sample_rate___returns_correct_sample_interval(
    di_single_line_high_rate_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> None:
    reader = DigitalSingleChannelReader(di_single_line_high_rate_task.in_stream)
    samples_to_read = 50
    waveform = DigitalWaveform(samples_to_read)

    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    assert _get_waveform_data(waveform) == _get_digital_data(1, 50)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 10_000_000)
    assert waveform.sample_count == samples_to_read
    assert waveform.channel_name == di_single_line_high_rate_task.di_channels[0].name
    _validate_waveform_signals(sim_6363_device, waveform, [0])


def test___digital_single_line_reader_with_timing_flag___read_waveform___only_includes_timing_data(
    di_single_line_timing_task: nidaqmx.Task,
) -> None:
    in_stream = di_single_line_timing_task.in_stream
    in_stream.waveform_attribute_mode = WaveformAttributeMode.TIMING
    reader = DigitalSingleChannelReader(in_stream)
    waveform = DigitalWaveform(50)

    samples_read = reader.read_waveform(waveform)

    assert samples_read == 50
    assert _get_waveform_data(waveform) == _get_digital_data(1, 50)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == ""


def test___digital_single_line_reader_with_extended_properties_flag___read_waveform___only_includes_extended_properties(
    di_single_line_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> None:
    in_stream = di_single_line_timing_task.in_stream
    in_stream.waveform_attribute_mode = WaveformAttributeMode.EXTENDED_PROPERTIES
    reader = DigitalSingleChannelReader(in_stream)
    waveform = DigitalWaveform(50)

    samples_read = reader.read_waveform(waveform)

    assert samples_read == 50
    assert _get_waveform_data(waveform) == _get_digital_data(1, 50)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.NONE
    assert waveform.channel_name == di_single_line_timing_task.di_channels[0].name
    _validate_waveform_signals(sim_6363_device, waveform, [0])


def test___digital_single_line_reader_with_both_flags___read_waveform___includes_both_timing_and_extended_properties(
    di_single_line_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> None:
    in_stream = di_single_line_timing_task.in_stream
    in_stream.waveform_attribute_mode = (
        WaveformAttributeMode.TIMING | WaveformAttributeMode.EXTENDED_PROPERTIES
    )
    reader = DigitalSingleChannelReader(in_stream)
    waveform = DigitalWaveform(50)

    samples_read = reader.read_waveform(waveform)

    assert samples_read == 50
    assert _get_waveform_data(waveform) == _get_digital_data(1, 50)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.channel_name == di_single_line_timing_task.di_channels[0].name
    _validate_waveform_signals(sim_6363_device, waveform, [0])


def test___digital_single_line_reader_with_none_flag___read_waveform___minimal_waveform_data(
    di_single_line_timing_task: nidaqmx.Task,
) -> None:
    in_stream = di_single_line_timing_task.in_stream
    in_stream.waveform_attribute_mode = WaveformAttributeMode.NONE
    reader = DigitalSingleChannelReader(in_stream)
    waveform = DigitalWaveform(50)

    samples_read = reader.read_waveform(waveform)

    assert samples_read == 50
    assert _get_waveform_data(waveform) == _get_digital_data(1, 50)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.NONE
    assert waveform.channel_name == ""


def test___digital_single_channel_port_uint32_reader___read_waveform___returns_valid_waveform(
    di_single_channel_port_uint32_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_port_uint32_timing_task.in_stream)
    num_lines = 32
    num_samples = 10
    waveform = DigitalWaveform(num_samples, num_lines)

    samples_read = reader.read_waveform(waveform, num_samples)

    assert samples_read == num_samples
    assert _get_waveform_port_data(waveform) == _get_digital_data(num_lines, num_samples)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.channel_name == di_single_channel_port_uint32_timing_task.di_channels[0].name
    _validate_waveform_signals(sim_6363_device, waveform, range(num_lines))


def test___digital_single_channel_lines_and_port___read_waveform___returns_valid_waveform(
    di_single_chan_lines_and_port_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    reader = DigitalSingleChannelReader(di_single_chan_lines_and_port_task.in_stream)
    num_lines = _get_num_di_lines_in_task(di_single_chan_lines_and_port_task)
    samples_to_read = 10
    waveform = DigitalWaveform(samples_to_read, num_lines)

    samples_read = reader.read_waveform(waveform, samples_to_read)

    assert samples_read == samples_to_read
    assert _get_waveform_port_data(waveform) == [
        0b00000000000,
        0b10000000001,
        0b01000000010,
        0b11000000011,
        0b00100000100,
        0b10100000101,
        0b01100000110,
        0b11100000111,
        0b00000001000,
        0b10000001001,
    ]
    assert waveform.sample_count == samples_to_read
    assert waveform.channel_name == di_single_chan_lines_and_port_task.di_channels[0].name
    _validate_waveform_signals(sim_6363_device, waveform, [32, 33, 34, 35, 36, 37, 38, 39, 2, 1, 0])


@pytest.mark.parametrize(
    "dtype",
    [
        numpy.bool,
        numpy.int8,
        numpy.uint8,
    ],
)
def test___digital_single_channel_multi_line_reader___read_waveform_all_dtypes___returns_valid_waveform(
    di_single_channel_multi_line_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
    dtype,
) -> None:
    reader = DigitalSingleChannelReader(di_single_channel_multi_line_timing_task.in_stream)
    num_lines = 8
    num_samples = 10
    waveform = DigitalWaveform(num_samples, num_lines, dtype=dtype)

    samples_read = reader.read_waveform(waveform, num_samples)

    assert samples_read == num_samples
    assert _get_waveform_data(waveform) == _get_digital_data(num_lines, num_samples)
    _validate_waveform_signals(sim_6363_device, waveform, [7, 6, 5, 4, 3, 2, 1, 0])


def test___digital_single_line_reader___read_waveform_read_all_available___returns_valid_waveform(
    di_single_line_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    reader = DigitalSingleChannelReader(di_single_line_timing_task.in_stream)
    waveform = DigitalWaveform(100)

    samples_read = reader.read_waveform(waveform, READ_ALL_AVAILABLE)

    assert samples_read == 50
    assert _get_waveform_data(waveform) == _get_digital_data(1, samples_read)
    assert _is_timestamp_close_to_now(waveform.timing.timestamp)
    assert waveform.timing.sample_interval == ht_timedelta(seconds=1 / 1000)
    assert waveform.timing.sample_interval_mode == SampleIntervalMode.REGULAR
    assert waveform.channel_name == di_single_line_timing_task.di_channels[0].name
    _validate_waveform_signals(sim_6363_device, waveform, [0])
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/stream_readers/test_power_readers_ai.py sha256=119b3f6405fc91a8c0ebe2991b7f46387049065b196ab8d118a8d528101343b0 bytes=9004 -->
## FILE: tests/component/stream_readers/test_power_readers_ai.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/stream_readers/test_power_readers_ai.py`
- sha256: `119b3f6405fc91a8c0ebe2991b7f46387049065b196ab8d118a8d528101343b0`
- bytes: 9004

````python
from __future__ import annotations

import ctypes
import math

import numpy
import numpy.typing
import pytest

import nidaqmx
from nidaqmx.stream_readers import (
    PowerBinaryReader,
    PowerMultiChannelReader,
    PowerSingleChannelReader,
)
from tests.component._analog_utils import (
    POWER_BINARY_EPSILON,
    POWER_EPSILON,
    _get_current_code_setpoint_for_chan,
    _get_current_setpoint_for_chan,
    _get_voltage_code_setpoint_for_chan,
    _get_voltage_setpoint_for_chan,
)


def test___power_single_channel_reader___read_one_sample___returns_valid_samples(
    pwr_single_channel_task: nidaqmx.Task,
) -> None:
    reader = PowerSingleChannelReader(pwr_single_channel_task.in_stream)

    data = reader.read_one_sample()

    assert data.voltage == pytest.approx(_get_voltage_setpoint_for_chan(0), abs=POWER_EPSILON)
    assert data.current == pytest.approx(_get_current_setpoint_for_chan(0), abs=POWER_EPSILON)


def test___power_single_channel_reader___read_many_sample___returns_valid_samples(
    pwr_single_channel_task: nidaqmx.Task,
) -> None:
    reader = PowerSingleChannelReader(pwr_single_channel_task.in_stream)
    samples_to_read = 10
    voltage_data = numpy.full(samples_to_read, math.inf, dtype=numpy.float64)
    current_data = numpy.full(samples_to_read, math.inf, dtype=numpy.float64)

    samples_read = reader.read_many_sample(voltage_data, current_data, samples_to_read)

    assert samples_read == samples_to_read
    assert voltage_data == pytest.approx(_get_voltage_setpoint_for_chan(0), abs=POWER_EPSILON)
    assert current_data == pytest.approx(_get_current_setpoint_for_chan(0), abs=POWER_EPSILON)


@pytest.mark.parametrize(
    "voltage_dtype, current_dtype",
    [
        (numpy.float32, numpy.float64),
        (numpy.float64, numpy.float32),
        (numpy.float32, numpy.float32),
    ],
)
def test___power_single_channel_reader___read_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    pwr_single_channel_task: nidaqmx.Task,
    voltage_dtype: numpy.typing.DTypeLike,
    current_dtype: numpy.typing.DTypeLike,
) -> None:
    reader = PowerSingleChannelReader(pwr_single_channel_task.in_stream)
    samples_to_read = 10
    voltage_data = numpy.full(samples_to_read, math.inf, dtype=voltage_dtype)
    current_data = numpy.full(samples_to_read, math.inf, dtype=current_dtype)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample(voltage_data, current_data, samples_to_read)

    assert "float64" in exc_info.value.args[0]


def test___power_multi_channel_reader___read_one_sample___returns_valid_samples(
    pwr_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = PowerMultiChannelReader(pwr_multi_channel_task.in_stream)
    num_channels = pwr_multi_channel_task.number_of_channels
    voltage_data = numpy.full(num_channels, math.inf, dtype=numpy.float64)
    current_data = numpy.full(num_channels, math.inf, dtype=numpy.float64)

    reader.read_one_sample(voltage_data, current_data)

    assert voltage_data == pytest.approx(
        [_get_voltage_setpoint_for_chan(chan_index) for chan_index in range(num_channels)],
        abs=POWER_EPSILON,
    )
    assert current_data == pytest.approx(
        [_get_current_setpoint_for_chan(chan_index) for chan_index in range(num_channels)],
        abs=POWER_EPSILON,
    )


@pytest.mark.parametrize(
    "voltage_dtype, current_dtype",
    [
        (numpy.float32, numpy.float64),
        (numpy.float64, numpy.float32),
        (numpy.float32, numpy.float32),
    ],
)
def test___power_multi_channel_reader___read_one_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    pwr_multi_channel_task: nidaqmx.Task,
    voltage_dtype: numpy.typing.DTypeLike,
    current_dtype: numpy.typing.DTypeLike,
) -> None:
    reader = PowerMultiChannelReader(pwr_multi_channel_task.in_stream)
    num_channels = pwr_multi_channel_task.number_of_channels
    voltage_data = numpy.full(num_channels, math.inf, dtype=voltage_dtype)
    current_data = numpy.full(num_channels, math.inf, dtype=current_dtype)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        reader.read_one_sample(voltage_data, current_data)

    assert "float64" in exc_info.value.args[0]


def test___power_multi_channel_reader___read_many_sample___returns_valid_samples(
    pwr_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = PowerMultiChannelReader(pwr_multi_channel_task.in_stream)
    num_channels = pwr_multi_channel_task.number_of_channels
    samples_to_read = 10
    voltage_data = numpy.full((num_channels, samples_to_read), math.inf, dtype=numpy.float64)
    current_data = numpy.full((num_channels, samples_to_read), math.inf, dtype=numpy.float64)

    samples_read = reader.read_many_sample(
        voltage_data, current_data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    expected_voltage_vals = [
        _get_voltage_setpoint_for_chan(chan_index) for chan_index in range(num_channels)
    ]
    expected_current_vals = [
        _get_current_setpoint_for_chan(chan_index) for chan_index in range(num_channels)
    ]
    assert voltage_data == pytest.approx(expected_voltage_vals, abs=POWER_EPSILON)
    assert current_data == pytest.approx(expected_current_vals, abs=POWER_EPSILON)


@pytest.mark.parametrize(
    "voltage_dtype, current_dtype",
    [
        (numpy.float32, numpy.float64),
        (numpy.float64, numpy.float32),
        (numpy.float32, numpy.float32),
    ],
)
def test___power_multi_channel_reader___read_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    pwr_multi_channel_task: nidaqmx.Task,
    voltage_dtype: numpy.typing.DTypeLike,
    current_dtype: numpy.typing.DTypeLike,
) -> None:
    reader = PowerMultiChannelReader(pwr_multi_channel_task.in_stream)
    num_channels = pwr_multi_channel_task.number_of_channels
    samples_to_read = 10
    voltage_data = numpy.full((num_channels, samples_to_read), math.inf, dtype=voltage_dtype)
    current_data = numpy.full((num_channels, samples_to_read), math.inf, dtype=current_dtype)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample(
            voltage_data, current_data, number_of_samples_per_channel=samples_to_read
        )

    assert "float64" in exc_info.value.args[0]


def test___power_binary_reader___read_many_sample___returns_valid_samples(
    pwr_multi_channel_task: nidaqmx.Task,
) -> None:
    reader = PowerBinaryReader(pwr_multi_channel_task.in_stream)
    num_channels = pwr_multi_channel_task.number_of_channels
    samples_to_read = 10
    voltage_data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.int16).min, dtype=numpy.int16
    )
    current_data = numpy.full(
        (num_channels, samples_to_read), numpy.iinfo(numpy.int16).min, dtype=numpy.int16
    )

    samples_read = reader.read_many_sample(
        voltage_data, current_data, number_of_samples_per_channel=samples_to_read
    )

    assert samples_read == samples_to_read
    expected_voltage_vals = [
        _get_voltage_code_setpoint_for_chan(chan_index) for chan_index in range(num_channels)
    ]
    expected_current_vals = [
        _get_current_code_setpoint_for_chan(chan_index) for chan_index in range(num_channels)
    ]
    assert voltage_data == pytest.approx(expected_voltage_vals, abs=POWER_BINARY_EPSILON)
    assert current_data == pytest.approx(expected_current_vals, abs=POWER_BINARY_EPSILON)


@pytest.mark.parametrize(
    "voltage_dtype, voltage_default, current_dtype, current_default",
    [
        (numpy.float64, math.inf, numpy.int16, numpy.iinfo(numpy.int16).min),
        (numpy.int16, numpy.iinfo(numpy.int16).min, numpy.float64, math.inf),
        (numpy.float64, math.inf, numpy.float64, math.inf),
    ],
)
def test___power_binary_reader___read_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    pwr_multi_channel_task: nidaqmx.Task,
    voltage_dtype: numpy.typing.DTypeLike,
    voltage_default: float | int,
    current_dtype: numpy.typing.DTypeLike,
    current_default: float | int,
) -> None:
    reader = PowerBinaryReader(pwr_multi_channel_task.in_stream)
    num_channels = pwr_multi_channel_task.number_of_channels
    samples_to_read = 10
    voltage_data = numpy.full((num_channels, samples_to_read), voltage_default, dtype=voltage_dtype)
    current_data = numpy.full((num_channels, samples_to_read), current_default, dtype=current_dtype)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = reader.read_many_sample(
            voltage_data, current_data, number_of_samples_per_channel=samples_to_read
        )

    assert "int16" in exc_info.value.args[0]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/stream_writers/test_analog_multi_channel_writer.py sha256=38599467e3cae4656eba1a7a335d5548b6f9dea78e50e7a64dbd60eb949e155a bytes=8326 -->
## FILE: tests/component/stream_writers/test_analog_multi_channel_writer.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/stream_writers/test_analog_multi_channel_writer.py`
- sha256: `38599467e3cae4656eba1a7a335d5548b6f9dea78e50e7a64dbd60eb949e155a`
- bytes: 8326

````python
from __future__ import annotations

import ctypes

import numpy
import pytest

import nidaqmx
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, FeatureNotSupportedError
from nidaqmx.stream_writers import AnalogMultiChannelWriter
from tests.component._analog_utils import (
    AO_VOLTAGE_EPSILON,
    _create_constant_waveform,
    _create_float32_ramp_waveform,
    _create_linear_ramp_waveform,
    _create_non_contiguous_waveform,
    _create_scaled_int32_ramp_waveform,
    _get_approx_final_value,
    _get_expected_voltage_for_chan,
)


def test___analog_multi_channel_writer___write_one_sample___updates_output(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    expected = [_get_expected_voltage_for_chan(chan_index) for chan_index in range(num_channels)]
    data = numpy.asarray(expected, dtype=numpy.float64)

    writer.write_one_sample(data)

    assert ai_multi_channel_loopback_task.read() == pytest.approx(expected, abs=AO_VOLTAGE_EPSILON)


def test___analog_multi_channel_writer___write_one_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    data = numpy.full(num_channels, 0.0, dtype=numpy.float32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_one_sample(data)

    assert "float64" in exc_info.value.args[0]


def test___analog_multi_channel_writer___write_many_sample___updates_output(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    expected = [_get_expected_voltage_for_chan(chan_index) for chan_index in range(num_channels)]
    # sweep up to the expected values, the only one we'll validate
    data = numpy.ascontiguousarray(
        numpy.transpose(
            numpy.linspace(
                [0.0] * num_channels,
                expected,
                num=samples_to_write,
                dtype=numpy.float64,
            )
        )
    )

    samples_written = writer.write_many_sample(data)

    assert samples_written == samples_to_write
    assert ai_multi_channel_loopback_task.read() == pytest.approx(expected, abs=AO_VOLTAGE_EPSILON)


def test___analog_multi_channel_writer___write_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    data = numpy.full((num_channels, samples_to_write), 0.0, dtype=numpy.float32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = writer.write_many_sample(data)

    assert "float64" in exc_info.value.args[0]


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
def test___analog_multi_channel_writer___write_waveforms_feature_disabled___raises_feature_not_supported_error(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_samples = 10
    waveforms = [
        _create_constant_waveform(num_samples),
        _create_constant_waveform(num_samples),
    ]

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        writer.write_waveforms(waveforms)

    error_message = exc_info.value.args[0]
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message
    assert "NIDAQMX_ENABLE_WAVEFORM_SUPPORT" in error_message


def test___analog_multi_channel_writer___write_waveforms___output_matches_final_values(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_samples = 50
    waveforms = [
        _create_linear_ramp_waveform(num_samples, 0.0, 0.5),
        _create_linear_ramp_waveform(num_samples, 0.5, 1.0),
    ]

    samples_written = writer.write_waveforms(waveforms)

    assert samples_written == num_samples
    read_data = ai_multi_channel_loopback_task.read()
    for i, waveform in enumerate(waveforms):
        assert read_data[i] == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


def test___analog_multi_channel_writer___write_waveforms_with_float32_dtype___output_matches_final_values(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_samples = 50
    waveforms = [
        _create_float32_ramp_waveform(num_samples, 0.0, 0.5),
        _create_float32_ramp_waveform(num_samples, 0.5, 1.0),
    ]

    samples_written = writer.write_waveforms(waveforms)

    assert samples_written == num_samples
    read_data = ai_multi_channel_loopback_task.read()
    for i, waveform in enumerate(waveforms):
        assert read_data[i] == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


def test___analog_multi_channel_writer___write_waveforms_with_scaling___output_matches_final_values(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_samples = 20
    waveforms = [
        _create_scaled_int32_ramp_waveform(num_samples),
        _create_scaled_int32_ramp_waveform(num_samples),
    ]

    samples_written = writer.write_waveforms(waveforms)

    assert samples_written == num_samples
    read_data = ai_multi_channel_loopback_task.read()
    for i, waveform in enumerate(waveforms):
        assert read_data[i] == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


def test___analog_multi_channel_writer___write_waveforms_with_non_contiguous_data___output_matches_final_values(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_samples = 50
    waveforms = [
        _create_non_contiguous_waveform(num_samples, 0.0, 0.05),
        _create_non_contiguous_waveform(num_samples, 0.05, 0.1),
    ]

    samples_written = writer.write_waveforms(waveforms)

    assert samples_written == num_samples
    read_data = ai_multi_channel_loopback_task.read()
    for i, waveform in enumerate(waveforms):
        assert read_data[i] == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


def test___analog_multi_channel_writer___write_waveforms_with_different_lengths___raises_error(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    waveforms = [
        _create_constant_waveform(10),
        _create_constant_waveform(20),
    ]

    with pytest.raises(ValueError) as exc_info:
        writer.write_waveforms(waveforms)

    error_message = exc_info.value.args[0]
    assert "The waveforms must all have the same sample count" in error_message


def test___analog_multi_channel_writer___write_waveforms_with_wrong_number_of_channels___raises_daq_error(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogMultiChannelWriter(ao_multi_channel_task.out_stream)
    num_samples = 10
    waveforms = [
        _create_constant_waveform(num_samples),
        _create_constant_waveform(num_samples),
        _create_constant_waveform(num_samples),
    ]

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        writer.write_waveforms(waveforms)

    error_message = exc_info.value.args[0]
    assert (
        "Write cannot be performed, because the number of channels in the data does not match the number of channels in the task"
        in error_message
    )
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/stream_writers/test_analog_single_channel_writer.py sha256=1de345af1300956a3070bfd029392e144569dfde1b03f8c7114d33149fa5780a bytes=5462 -->
## FILE: tests/component/stream_writers/test_analog_single_channel_writer.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/stream_writers/test_analog_single_channel_writer.py`
- sha256: `1de345af1300956a3070bfd029392e144569dfde1b03f8c7114d33149fa5780a`
- bytes: 5462

````python
from __future__ import annotations

import ctypes

import numpy
import pytest

import nidaqmx
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, FeatureNotSupportedError
from nidaqmx.stream_writers import AnalogSingleChannelWriter
from tests.component._analog_utils import (
    AO_VOLTAGE_EPSILON,
    _create_constant_waveform,
    _create_float32_ramp_waveform,
    _create_linear_ramp_waveform,
    _create_non_contiguous_waveform,
    _create_scaled_int32_ramp_waveform,
    _get_approx_final_value,
    _get_expected_voltage_for_chan,
)


def test___analog_single_channel_writer___write_one_sample___updates_output(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_single_channel_task.out_stream)
    expected = _get_expected_voltage_for_chan(0)

    writer.write_one_sample(expected)

    assert ai_single_channel_loopback_task.read() == pytest.approx(expected, abs=AO_VOLTAGE_EPSILON)


def test___analog_single_channel_writer___write_many_sample___updates_output(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_single_channel_task.out_stream)
    samples_to_write = 10
    expected = _get_expected_voltage_for_chan(0)
    data = numpy.linspace(0.0, expected, num=samples_to_write, dtype=numpy.float64)

    samples_written = writer.write_many_sample(data)

    assert samples_written == samples_to_write
    assert ai_single_channel_loopback_task.read() == pytest.approx(expected, abs=AO_VOLTAGE_EPSILON)


def test___analog_single_channel_writer___write_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(
    ao_single_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_single_channel_task.out_stream)
    samples_to_write = 10
    expected = _get_expected_voltage_for_chan(0)
    data = numpy.full(samples_to_write, expected, dtype=numpy.float32)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = writer.write_many_sample(data)

    assert "float64" in exc_info.value.args[0]


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
def test___analog_single_channel_reader___read_waveform_feature_disabled___raises_feature_not_supported_error(
    ao_single_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_single_channel_task.out_stream)
    waveform = _create_constant_waveform(20)

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        writer.write_waveform(waveform)

    error_message = exc_info.value.args[0]
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message
    assert "NIDAQMX_ENABLE_WAVEFORM_SUPPORT" in error_message


def test___analog_single_channel_writer___write_waveform___output_matches_final_value(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_single_channel_task.out_stream)
    num_samples = 20
    start_value = 0.0
    end_value = 1.0
    waveform = _create_linear_ramp_waveform(num_samples, start_value, end_value)

    samples_written = writer.write_waveform(waveform)

    assert samples_written == num_samples
    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


def test___analog_single_channel_writer___write_waveform_with_float32_dtype___output_matches_final_value(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_single_channel_task.out_stream)
    num_samples = 20
    start_value = 0.0
    end_value = 1.0
    waveform = _create_float32_ramp_waveform(num_samples, start_value, end_value)

    samples_written = writer.write_waveform(waveform)

    assert samples_written == num_samples
    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


def test___analog_single_channel_writer___write_waveform_with_scaling___output_matches_final_value(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_single_channel_task.out_stream)
    num_samples = 20
    waveform = _create_scaled_int32_ramp_waveform(num_samples)

    samples_written = writer.write_waveform(waveform)

    assert samples_written == num_samples
    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


def test___analog_single_channel_writer___write_waveform_with_non_contiguous_data___output_matches_final_value(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogSingleChannelWriter(ao_single_channel_task.out_stream)
    num_samples = 20
    waveform = _create_non_contiguous_waveform(num_samples, -0.0, 0.1)

    samples_written = writer.write_waveform(waveform)

    assert samples_written == num_samples
    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/stream_writers/test_analog_unscaled_writer.py sha256=1ec74e27ec82f69de8cd3eaab2aecbed4ce95a40a244a3ffd37254e5d5d219c9 bytes=6524 -->
## FILE: tests/component/stream_writers/test_analog_unscaled_writer.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/stream_writers/test_analog_unscaled_writer.py`
- sha256: `1ec74e27ec82f69de8cd3eaab2aecbed4ce95a40a244a3ffd37254e5d5d219c9`
- bytes: 6524

````python
from __future__ import annotations

import ctypes

import numpy
import pytest

import nidaqmx
from nidaqmx.stream_writers import AnalogUnscaledWriter
from tests.component._analog_utils import (
    RAW_VOLTAGE_EPSILON,
    _get_expected_voltage_for_chan,
    _volts_to_codes,
)


def test___analog_unscaled_writer___write_int16___updates_output(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogUnscaledWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    expected = [_get_expected_voltage_for_chan(chan_index) for chan_index in range(num_channels)]
    # sweep up to the expected values, the only one we'll validate
    data = numpy.ascontiguousarray(
        numpy.transpose(
            numpy.linspace(
                [0] * num_channels,
                [_volts_to_codes(v) for v in expected],
                num=samples_to_write,
                dtype=numpy.int16,
            )
        )
    )

    samples_written = writer.write_int16(data)

    assert samples_written == samples_to_write
    assert ai_multi_channel_loopback_task.read() == pytest.approx(expected, abs=RAW_VOLTAGE_EPSILON)


def test___analog_unscaled_writer___write_int16_with_wrong_dtype___raises_error_with_correct_dtype(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogUnscaledWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    data = numpy.full((num_channels, samples_to_write), 0.0, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = writer.write_int16(data)

    assert "int16" in exc_info.value.args[0]


def test___analog_unscaled_writer___write_int32___updates_output(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogUnscaledWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    expected = [_get_expected_voltage_for_chan(chan_index) for chan_index in range(num_channels)]
    # sweep up to the expected values, the only one we'll validate
    data = numpy.ascontiguousarray(
        numpy.transpose(
            numpy.linspace(
                [0] * num_channels,
                [_volts_to_codes(v) for v in expected],
                num=samples_to_write,
                dtype=numpy.int32,
            )
        )
    )

    samples_written = writer.write_int32(data)

    assert samples_written == samples_to_write
    assert ai_multi_channel_loopback_task.read() == pytest.approx(expected, abs=RAW_VOLTAGE_EPSILON)


def test___analog_unscaled_writer___write_int32_with_wrong_dtype___raises_error_with_correct_dtype(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogUnscaledWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    data = numpy.full((num_channels, samples_to_write), 0.0, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = writer.write_int32(data)

    assert "int32" in exc_info.value.args[0]


def test___analog_unscaled_writer___write_uint16___updates_output(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogUnscaledWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    expected = [_get_expected_voltage_for_chan(chan_index) for chan_index in range(num_channels)]
    # sweep up to the expected values, the only one we'll validate
    data = numpy.ascontiguousarray(
        numpy.transpose(
            numpy.linspace(
                [0] * num_channels,
                [_volts_to_codes(v) for v in expected],
                num=samples_to_write,
                dtype=numpy.uint16,
            )
        )
    )

    samples_written = writer.write_uint16(data)

    assert samples_written == samples_to_write
    assert ai_multi_channel_loopback_task.read() == pytest.approx(expected, abs=RAW_VOLTAGE_EPSILON)


def test___analog_unscaled_writer___write_uint16_with_wrong_dtype___raises_error_with_correct_dtype(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogUnscaledWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    data = numpy.full((num_channels, samples_to_write), 0.0, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = writer.write_uint16(data)

    assert "uint16" in exc_info.value.args[0]


def test___analog_unscaled_writer___write_uint32___updates_output(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    writer = AnalogUnscaledWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    expected = [_get_expected_voltage_for_chan(chan_index) for chan_index in range(num_channels)]
    # sweep up to the expected values, the only one we'll validate
    data = numpy.ascontiguousarray(
        numpy.transpose(
            numpy.linspace(
                [0] * num_channels,
                [_volts_to_codes(v) for v in expected],
                num=samples_to_write,
                dtype=numpy.uint32,
            )
        )
    )

    samples_written = writer.write_uint32(data)

    assert samples_written == samples_to_write
    assert ai_multi_channel_loopback_task.read() == pytest.approx(expected, abs=RAW_VOLTAGE_EPSILON)


def test___analog_unscaled_writer___write_uint32_with_wrong_dtype___raises_error_with_correct_dtype(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    writer = AnalogUnscaledWriter(ao_multi_channel_task.out_stream)
    num_channels = ao_multi_channel_task.number_of_channels
    samples_to_write = 10
    data = numpy.full((num_channels, samples_to_write), 0.0, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        _ = writer.write_uint32(data)

    assert "uint32" in exc_info.value.args[0]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/stream_writers/test_digital_multi_channel_writer.py sha256=3a947e545ea7e3032291e5c2919f52cf85829d014fe2d916cb1e1b55f4bdecfb bytes=20693 -->
## FILE: tests/component/stream_writers/test_digital_multi_channel_writer.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/stream_writers/test_digital_multi_channel_writer.py`
- sha256: `3a947e545ea7e3032291e5c2919f52cf85829d014fe2d916cb1e1b55f4bdecfb`
- bytes: 20693

````python
from __future__ import annotations

import ctypes
import math
from collections.abc import Callable

import numpy
import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, FeatureNotSupportedError
from nidaqmx.constants import LineGrouping
from nidaqmx.errors import DaqError
from nidaqmx.stream_writers import DigitalMultiChannelWriter
from tests.component._digital_utils import (
    _create_digital_waveform_uint8,
    _create_non_contiguous_digital_waveform,
    _create_waveform_for_line,
    _create_waveforms_for_mixed_lines,
    _get_digital_data,
    _get_digital_port_data_for_sample,
    _get_digital_port_data_port_major,
    _get_digital_port_data_sample_major,
    _get_num_do_lines_in_task,
    _get_waveform_data,
    _get_waveform_port_data,
    _int_to_bool_array,
    _start_do_task,
)


def test___digital_multi_channel_writer___write_one_sample_one_line___updates_output(
    do_single_line_task: nidaqmx.Task,
    di_single_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_single_line_task.out_stream)
    num_lines = _get_num_do_lines_in_task(do_single_line_task)
    samples_to_write = 256

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_digital_data(num_lines, samples_to_write):
        writer.write_one_sample_one_line(_int_to_bool_array(num_lines, datum))

    assert di_single_line_loopback_task.read() == datum


def test___digital_multi_channel_writer___write_one_sample_multi_line___updates_output(
    do_multi_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_multi_line_task.out_stream)
    num_channels = do_multi_channel_multi_line_task.number_of_channels
    samples_to_write = 256

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_digital_data(num_channels, samples_to_write):
        data_to_write = _int_to_bool_array(num_channels, datum).reshape((num_channels, 1))
        writer.write_one_sample_multi_line(data_to_write)

    assert di_multi_line_loopback_task.read() == datum


def test___digital_multi_channel_writer___write_one_sample_multi_line_jagged___updates_output(
    di_port0_loopback_task_32dio: nidaqmx.Task,
    di_port1_loopback_task_32dio: nidaqmx.Task,
    di_port2_loopback_task_32dio: nidaqmx.Task,
    generate_task: Callable[[], nidaqmx.Task],
    real_x_series_device_32dio: nidaqmx.system.Device,
) -> None:
    task = generate_task()
    for port in real_x_series_device_32dio.do_ports:
        task.do_channels.add_do_chan(
            port.name,
            line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
        )
    _start_do_task(task, is_port=True, num_chans=task.number_of_channels)
    writer = DigitalMultiChannelWriter(task.out_stream)
    num_channels = task.number_of_channels
    samples_to_write = 0xA5

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_digital_data(num_channels * 32, samples_to_write):
        data_to_write = _int_to_bool_array(num_channels * 32, datum).reshape((num_channels, 32))
        writer.write_one_sample_multi_line(data_to_write)

    assert di_port0_loopback_task_32dio.read() == datum & 0xFFFFFFFF
    assert di_port1_loopback_task_32dio.read() == (datum >> 32) & 0xFF
    assert di_port2_loopback_task_32dio.read() == (datum >> 64) & 0xFF


def test___digital_multi_channel_writer___write_one_sample_multi_line_with_wrong_dtype___raises_error_with_correct_dtype(
    do_multi_channel_multi_line_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_multi_line_task.out_stream)
    num_channels = do_multi_channel_multi_line_task.number_of_channels
    sample = numpy.full((num_channels, 1), math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_one_sample_multi_line(sample)

    assert "bool" in exc_info.value.args[0]


def test___digital_multi_channel_writer___write_one_sample_port_byte___updates_output(
    do_multi_channel_port_task: nidaqmx.Task,
    di_multi_channel_port_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    samples_to_write = 256

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_digital_port_data_sample_major(do_multi_channel_port_task, samples_to_write):
        writer.write_one_sample_port_byte(numpy.array(datum, dtype=numpy.uint8))

    assert di_multi_channel_port_loopback_task.read() == datum


def test___digital_multi_channel_writer___write_one_sample_port_byte_with_wrong_dtype___raises_error_with_correct_dtype(
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    num_channels = do_multi_channel_port_task.number_of_channels
    data = numpy.full(num_channels, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_one_sample_port_byte(data)

    assert "uint8" in exc_info.value.args[0]


def test___digital_multi_channel_writer___write_many_sample_port_byte___updates_output(
    do_multi_channel_port_task: nidaqmx.Task,
    di_multi_channel_port_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    samples_to_write = 256

    # "sweep" up to the final value, the only one we'll validate
    data = _get_digital_port_data_port_major(do_multi_channel_port_task, samples_to_write)
    writer.write_many_sample_port_byte(numpy.array(data, dtype=numpy.uint8))

    assert di_multi_channel_port_loopback_task.read() == _get_digital_port_data_for_sample(
        do_multi_channel_port_task, samples_to_write - 1
    )


def test___digital_multi_channel_writer___write_many_sample_port_byte_with_wrong_dtype___raises_error_with_correct_dtype(
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    num_channels = do_multi_channel_port_task.number_of_channels
    samples_to_write = 256
    data = numpy.full((num_channels, samples_to_write), math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_many_sample_port_byte(data)

    assert "uint8" in exc_info.value.args[0]


def test___digital_multi_channel_writer___write_one_sample_port_uint16___updates_output(
    do_multi_channel_port_task: nidaqmx.Task,
    di_multi_channel_port_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    samples_to_write = 256

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_digital_port_data_sample_major(do_multi_channel_port_task, samples_to_write):
        writer.write_one_sample_port_uint16(numpy.array(datum, dtype=numpy.uint16))

    assert di_multi_channel_port_loopback_task.read() == datum


def test___digital_multi_channel_writer___write_one_sample_port_uint16_with_wrong_dtype___raises_error_with_correct_dtype(
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    num_channels = do_multi_channel_port_task.number_of_channels
    data = numpy.full(num_channels, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_one_sample_port_uint16(data)

    assert "uint16" in exc_info.value.args[0]


def test___digital_multi_channel_writer___write_many_sample_port_uint16___updates_output(
    do_multi_channel_port_task: nidaqmx.Task,
    di_multi_channel_port_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    samples_to_write = 256

    # "sweep" up to the final value, the only one we'll validate
    data = _get_digital_port_data_port_major(do_multi_channel_port_task, samples_to_write)
    writer.write_many_sample_port_uint16(numpy.array(data, dtype=numpy.uint16))

    assert di_multi_channel_port_loopback_task.read() == _get_digital_port_data_for_sample(
        do_multi_channel_port_task, samples_to_write - 1
    )


def test___digital_multi_channel_writer___write_many_sample_port_uint16_with_wrong_dtype___raises_error_with_correct_dtype(
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    num_channels = do_multi_channel_port_task.number_of_channels
    samples_to_write = 256
    data = numpy.full((num_channels, samples_to_write), math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_many_sample_port_uint16(data)

    assert "uint16" in exc_info.value.args[0]


def test___digital_multi_channel_writer___write_one_sample_port_uint32___updates_output(
    do_multi_channel_port_task: nidaqmx.Task,
    di_multi_channel_port_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    samples_to_write = 256

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_digital_port_data_sample_major(do_multi_channel_port_task, samples_to_write):
        writer.write_one_sample_port_uint32(numpy.array(datum, dtype=numpy.uint32))

    assert di_multi_channel_port_loopback_task.read() == datum


def test___digital_multi_channel_writer___write_one_sample_port_uint32_with_wrong_dtype___raises_error_with_correct_dtype(
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    num_channels = do_multi_channel_port_task.number_of_channels
    data = numpy.full(num_channels, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_one_sample_port_uint32(data)

    assert "uint32" in exc_info.value.args[0]


def test___digital_multi_channel_writer___write_many_sample_port_uint32___updates_output(
    do_multi_channel_port_task: nidaqmx.Task,
    di_multi_channel_port_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    samples_to_write = 256

    # "sweep" up to the final value, the only one we'll validate
    data = _get_digital_port_data_port_major(do_multi_channel_port_task, samples_to_write)
    writer.write_many_sample_port_uint32(numpy.array(data, dtype=numpy.uint32))

    assert di_multi_channel_port_loopback_task.read() == _get_digital_port_data_for_sample(
        do_multi_channel_port_task, samples_to_write - 1
    )


def test___digital_multi_channel_writer___write_many_sample_port_uint32_with_wrong_dtype___raises_error_with_correct_dtype(
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    num_channels = do_multi_channel_port_task.number_of_channels
    samples_to_write = 256
    data = numpy.full((num_channels, samples_to_write), math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_many_sample_port_uint32(data)

    assert "uint32" in exc_info.value.args[0]


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
def test___digital_multi_channel_writer___write_waveforms_feature_disabled___raises_feature_not_supported_error(
    do_multi_channel_multi_line_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_multi_line_task.out_stream)
    waveforms = [_create_digital_waveform_uint8(20), _create_digital_waveform_uint8(20)]

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        writer.write_waveforms(waveforms)

    error_message = exc_info.value.args[0]
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message
    assert "NIDAQMX_ENABLE_WAVEFORM_SUPPORT" in error_message


def test___digital_multi_channel_writer___write_waveforms_single_lines___outputs_match_final_values(
    do_multi_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_multi_line_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 50):
        num_samples = i
        num_channels = 8
        waveforms = [_create_waveform_for_line(num_samples, chan) for chan in range(num_channels)]

        samples_written = writer.write_waveforms(waveforms)

        assert samples_written == num_samples
        actual_value = di_multi_line_loopback_task.read()
        assert actual_value == i - 1
        assert actual_value == _get_digital_data(num_channels, num_samples)[i - 1]


def test___digital_multi_channel_writer___write_waveforms_mixed_lines___outputs_match_final_values(
    do_multi_channel_mixed_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_mixed_line_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 10):
        num_samples = i
        num_channels = 8
        waveforms = _create_waveforms_for_mixed_lines(num_samples)

        samples_written = writer.write_waveforms(waveforms)

        assert samples_written == num_samples
        actual_value = di_multi_line_loopback_task.read()
        assert actual_value == _get_digital_data(num_channels, num_samples)[i - 1]


def test___digital_multi_channel_writer___write_waveforms_with_auto_start___output_matches_final_value(
    do_multi_channel_multi_line_task_with_timing: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    out_stream = do_multi_channel_multi_line_task_with_timing.out_stream
    writer = DigitalMultiChannelWriter(out_stream, auto_start=True)
    num_samples = 5
    num_channels = 8
    waveforms = [_create_waveform_for_line(num_samples, chan) for chan in range(num_channels)]

    samples_written = writer.write_waveforms(waveforms)

    assert samples_written == num_samples
    do_multi_channel_multi_line_task_with_timing.wait_until_done(timeout=2.0)
    actual_value = di_multi_line_loopback_task.read()
    assert actual_value == _get_digital_data(num_channels, num_samples)[-1]


def test___digital_multi_channel_writer___write_waveforms_ports___outputs_match_final_values(
    do_multi_channel_port_task: nidaqmx.Task,
    di_multi_channel_port_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 50):
        num_samples = i
        num_lines = 8
        waveforms = [
            _create_digital_waveform_uint8(num_samples, num_lines),
            _create_digital_waveform_uint8(num_samples, num_lines, invert=True),
        ]

        samples_written = writer.write_waveforms(waveforms)

        assert samples_written == num_samples
        actual_value = di_multi_channel_port_loopback_task.read()
        assert actual_value[0] != actual_value[1]
        assert actual_value == [
            _get_waveform_port_data(waveforms[0])[-1],
            _get_waveform_port_data(waveforms[1])[-1],
        ]


def test___digital_multi_channel_writer___write_waveforms_port_and_lines___outputs_match_final_values(
    do_multi_channel_port_and_lines_task: nidaqmx.Task,
    di_multi_channel_port_and_lines_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_and_lines_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 50):
        num_samples = i
        num_lines = 8
        waveforms = [
            _create_digital_waveform_uint8(num_samples, num_lines),
            _create_digital_waveform_uint8(num_samples, num_lines, invert=True),
        ]

        samples_written = writer.write_waveforms(waveforms)

        assert samples_written == num_samples
        actual_value = di_multi_channel_port_and_lines_loopback_task.read()
        assert actual_value == [
            _get_waveform_port_data(waveforms[0])[-1],
            _get_waveform_data(waveforms[1])[-1],
        ]


def test___digital_multi_channel_writer___write_waveforms_with_non_contiguous_data___outputs_match_final_values(
    do_multi_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_multi_line_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(2, 50):
        num_samples = i
        num_lines = 8
        waveforms = [
            _create_non_contiguous_digital_waveform(num_samples, first_line=i, num_lines=1)
            for i in range(num_lines)
        ]

        samples_written = writer.write_waveforms(waveforms)

        assert samples_written == num_samples
        actual_value = di_multi_line_loopback_task.read()
        assert actual_value == _get_digital_data(num_lines, num_samples)[-1]


def test___digital_multi_channel_writer___write_waveforms_with_different_sample_counts___raises_error(
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    num_lines = 8
    waveforms = [
        _create_digital_waveform_uint8(10, num_lines),
        _create_digital_waveform_uint8(11, num_lines),
    ]

    with pytest.raises(ValueError) as exc_info:
        writer.write_waveforms(waveforms)

    error_message = exc_info.value.args[0]
    assert "The waveforms must all have the same sample count." in error_message


def test___digital_multi_channel_writer___write_waveforms_with_too_many___raises_daq_error(
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    num_lines = 8
    waveforms = [
        _create_digital_waveform_uint8(10, num_lines),
        _create_digital_waveform_uint8(10, num_lines),
        _create_digital_waveform_uint8(10, num_lines),
    ]

    with pytest.raises(DaqError) as exc_info:
        writer.write_waveforms(waveforms)

    error_message = exc_info.value.args[0]
    assert "Write cannot be performed, because the number of channels" in error_message


def test___digital_multi_channel_writer___write_waveforms_with_too_many_signals___raises_daq_error(
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    writer = DigitalMultiChannelWriter(do_multi_channel_port_task.out_stream)
    num_samples = 10
    waveforms = [
        _create_digital_waveform_uint8(num_samples, 8),
        _create_digital_waveform_uint8(num_samples, 10),
    ]

    with pytest.raises(DaqError) as exc_info:
        writer.write_waveforms(waveforms)

    error_message = exc_info.value.args[0]
    assert "Specified read or write operation failed, because the number of lines" in error_message
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/stream_writers/test_digital_single_channel_writer.py sha256=d2c8d53d2b9d9251088e1ab22bf97a2e411e34e80a789e9c57b083dc729e2017 bytes=18511 -->
## FILE: tests/component/stream_writers/test_digital_single_channel_writer.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/stream_writers/test_digital_single_channel_writer.py`
- sha256: `d2c8d53d2b9d9251088e1ab22bf97a2e411e34e80a789e9c57b083dc729e2017`
- bytes: 18511

````python
from __future__ import annotations

import ctypes
import math

import numpy
import pytest

import nidaqmx
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, FeatureNotSupportedError
from nidaqmx.errors import DaqError
from nidaqmx.stream_writers import DigitalSingleChannelWriter
from tests.component._digital_utils import (
    _create_digital_waveform,
    _create_digital_waveform_uint8,
    _create_non_contiguous_digital_waveform,
    _get_digital_data,
    _get_num_do_lines_in_task,
    _get_waveform_data,
    _get_waveform_port_data,
    _int_to_bool_array,
)


def test___digital_single_channel_writer___write_one_sample_one_line___updates_output(
    do_single_line_task: nidaqmx.Task,
    di_single_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_line_task.out_stream)
    sample = True

    writer.write_one_sample_one_line(sample)

    assert di_single_line_loopback_task.read() == sample


def test___digital_single_channel_writer___write_one_sample_multi_line___updates_output(
    do_single_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_channel_multi_line_task.out_stream)
    num_lines = _get_num_do_lines_in_task(do_single_channel_multi_line_task)
    samples_to_write = 256

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_digital_data(num_lines, samples_to_write):
        writer.write_one_sample_multi_line(_int_to_bool_array(num_lines, datum))

    assert di_multi_line_loopback_task.read() == datum


def test___digital_single_channel_writer___write_one_sample_multi_line_with_wrong_dtype___raises_error_with_correct_dtype(
    do_single_channel_multi_line_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_channel_multi_line_task.out_stream)
    num_lines = _get_num_do_lines_in_task(do_single_channel_multi_line_task)
    sample = numpy.full(num_lines, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_one_sample_multi_line(sample)

    assert "bool" in exc_info.value.args[0]


def test___digital_single_channel_writer___write_one_sample_port_byte___updates_output(
    do_port1_task: nidaqmx.Task,
    di_port1_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port1_task.out_stream)
    num_lines = _get_num_do_lines_in_task(do_port1_task)
    samples_to_write = 256

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_digital_data(num_lines, samples_to_write):
        writer.write_one_sample_port_byte(datum)

    assert di_port1_loopback_task.read() == datum


def test___digital_single_channel_writer___write_many_sample_port_byte___updates_output(
    do_port1_task: nidaqmx.Task,
    di_port1_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port1_task.out_stream)
    num_lines = _get_num_do_lines_in_task(do_port1_task)
    samples_to_write = 256
    data = numpy.array(_get_digital_data(num_lines, samples_to_write), dtype=numpy.uint8)

    # "sweep" up to the final value, the only one we'll validate
    writer.write_many_sample_port_byte(data)

    assert di_port1_loopback_task.read() == data[-1]


def test___digital_single_channel_writer___write_many_sample_port_byte_with_wrong_dtype___raises_error_with_correct_dtype(
    do_port1_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port1_task.out_stream)
    samples_to_write = 256
    data = numpy.full(samples_to_write, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_many_sample_port_byte(data)

    assert "uint8" in exc_info.value.args[0]


def test___digital_single_channel_writer___write_one_sample_port_uint16___updates_output(
    do_port1_task: nidaqmx.Task,
    di_port1_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port1_task.out_stream)
    num_lines = _get_num_do_lines_in_task(do_port1_task)
    samples_to_write = 256

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_digital_data(num_lines, samples_to_write):
        writer.write_one_sample_port_uint16(datum)

    assert di_port1_loopback_task.read() == datum


def test___digital_single_channel_writer___write_many_sample_port_uint16___updates_output(
    do_port1_task: nidaqmx.Task,
    di_port1_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port1_task.out_stream)
    num_lines = _get_num_do_lines_in_task(do_port1_task)
    samples_to_write = 256
    data = numpy.array(_get_digital_data(num_lines, samples_to_write), dtype=numpy.uint16)

    # "sweep" up to the final value, the only one we'll validate
    writer.write_many_sample_port_uint16(data)

    assert di_port1_loopback_task.read() == data[-1]


def test___digital_single_channel_writer___write_many_sample_port_uint16_with_wrong_dtype___raises_error_with_correct_dtype(
    do_port1_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port1_task.out_stream)
    samples_to_write = 256
    data = numpy.full(samples_to_write, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_many_sample_port_uint16(data)

    assert "uint16" in exc_info.value.args[0]


def test___digital_single_channel_writer___write_one_sample_port_uint32___updates_output(
    do_port0_task: nidaqmx.Task,
    di_port0_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port0_task.out_stream)
    num_lines = _get_num_do_lines_in_task(do_port0_task)
    samples_to_write = 256

    # "sweep" up to the final value, the only one we'll validate
    for datum in _get_digital_data(num_lines, samples_to_write):
        writer.write_one_sample_port_uint32(datum)

    assert di_port0_loopback_task.read() == datum


def test___digital_single_channel_writer___write_many_sample_port_uint32___updates_output(
    do_port0_task: nidaqmx.Task,
    di_port0_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port0_task.out_stream)
    num_lines = _get_num_do_lines_in_task(do_port0_task)
    samples_to_write = 256
    data = numpy.array(_get_digital_data(num_lines, samples_to_write), dtype=numpy.uint32)

    # "sweep" up to the final value, the only one we'll validate
    writer.write_many_sample_port_uint32(data)

    assert di_port0_loopback_task.read() == data[-1]


def test___digital_single_channel_writer___write_many_sample_port_uint32_with_wrong_dtype___raises_error_with_correct_dtype(
    do_port0_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port0_task.out_stream)
    samples_to_write = 256
    data = numpy.full(samples_to_write, math.inf, dtype=numpy.float64)

    with pytest.raises((ctypes.ArgumentError, TypeError)) as exc_info:
        writer.write_many_sample_port_uint32(data)

    assert "uint32" in exc_info.value.args[0]


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
def test___digital_single_channel_writer___write_waveform_feature_disabled___raises_feature_not_supported_error(
    do_single_line_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_line_task.out_stream)
    waveform = _create_digital_waveform_uint8(20)

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        writer.write_waveform(waveform)

    error_message = exc_info.value.args[0]
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message
    assert "NIDAQMX_ENABLE_WAVEFORM_SUPPORT" in error_message


def test___digital_single_channel_writer___write_waveform_single_line___outputs_match_final_values(
    do_single_line_task: nidaqmx.Task,
    di_single_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_line_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 10):
        num_samples = i
        waveform = _create_digital_waveform_uint8(num_samples, 1)

        samples_written = writer.write_waveform(waveform)

        assert samples_written == num_samples
        assert di_single_line_loopback_task.read() == _get_waveform_data(waveform)[i - 1]


def test___digital_single_channel_writer___write_waveform_single_line_with_auto_start___output_matches_final_value(
    do_single_line_task_with_timing: nidaqmx.Task,
    di_single_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_line_task_with_timing.out_stream, auto_start=True)
    num_samples = 10
    waveform = _create_digital_waveform_uint8(num_samples, 1)

    samples_written = writer.write_waveform(waveform)

    assert samples_written == num_samples
    do_single_line_task_with_timing.wait_until_done(timeout=2.0)
    actual_value = di_single_line_loopback_task.read()
    assert actual_value == _get_waveform_data(waveform)[-1]


def test___digital_single_channel_writer___write_waveform_single_line_with_non_contiguous_data___outputs_match_final_values(
    do_single_line_task: nidaqmx.Task,
    di_single_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_line_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(2, 10):
        num_samples = i
        waveform = _create_non_contiguous_digital_waveform(num_samples, 0, 1)

        samples_written = writer.write_waveform(waveform)

        assert samples_written == num_samples
        assert di_single_line_loopback_task.read() == _get_waveform_data(waveform)[i - 1]


def test___digital_single_channel_writer___write_waveform_single_line_signal_count_mismatch___raises_daq_error(
    do_single_line_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_line_task.out_stream)
    num_samples = 20
    num_lines = 3
    waveform = _create_digital_waveform_uint8(num_samples, num_lines)

    with pytest.raises(DaqError) as exc_info:
        writer.write_waveform(waveform)

    error_message = exc_info.value.args[0]
    assert (
        "Specified read or write operation failed, because the number of lines in the data"
        in error_message
    )


@pytest.mark.parametrize(
    "dtype",
    [
        numpy.bool,
        numpy.int8,
        numpy.uint8,
    ],
)
def test___digital_single_channel_writer___write_waveform_single_line_all_dtypes___outputs_match_final_values(
    do_single_line_task: nidaqmx.Task,
    di_single_line_loopback_task: nidaqmx.Task,
    dtype,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_line_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 10):
        num_samples = i
        waveform = _create_digital_waveform(num_samples, 1, dtype=dtype)

        samples_written = writer.write_waveform(waveform)

        assert samples_written == num_samples
        assert di_single_line_loopback_task.read() == _get_waveform_data(waveform)[i - 1]


def test___digital_single_channel_writer___write_waveform_multi_line___outputs_match_final_values(
    do_single_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_channel_multi_line_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 10):
        num_samples = i
        num_lines = 8
        waveform = _create_digital_waveform_uint8(num_samples, num_lines)

        samples_written = writer.write_waveform(waveform)

        assert samples_written == num_samples
        assert di_multi_line_loopback_task.read() == _get_waveform_data(waveform)[i - 1]


def test___digital_single_channel_writer___write_waveform_multi_line_with_auto_start___output_matches_final_value(
    do_single_channel_multi_line_task_with_timing: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(
        do_single_channel_multi_line_task_with_timing.out_stream, auto_start=True
    )
    num_samples = 20
    num_lines = 8
    waveform = _create_digital_waveform_uint8(num_samples, num_lines)

    samples_written = writer.write_waveform(waveform)

    assert samples_written == num_samples
    do_single_channel_multi_line_task_with_timing.wait_until_done(timeout=2.0)
    actual_value = di_multi_line_loopback_task.read()
    assert actual_value == _get_waveform_data(waveform)[-1]


def test___digital_single_channel_writer___write_waveform_multi_line_with_non_contiguous_data___outputs_match_final_values(
    do_single_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_channel_multi_line_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(2, 20):
        num_samples = i
        num_lines = 8
        waveform = _create_non_contiguous_digital_waveform(num_samples, 0, num_lines)

        samples_written = writer.write_waveform(waveform)

        assert samples_written == num_samples
        actual_value = di_multi_line_loopback_task.read()
        assert actual_value == _get_waveform_data(waveform)[i - 1]


@pytest.mark.parametrize(
    "dtype",
    [
        numpy.bool,
        numpy.int8,
        numpy.uint8,
    ],
)
def test___digital_single_channel_writer___write_waveform_multi_line_all_dtypes___outputs_match_final_values(
    do_single_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
    dtype,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_channel_multi_line_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 10):
        num_samples = i
        num_lines = 8
        waveform = _create_digital_waveform(num_samples, num_lines, dtype=dtype)

        samples_written = writer.write_waveform(waveform)

        assert samples_written == num_samples
        assert di_multi_line_loopback_task.read() == _get_waveform_data(waveform)[i - 1]


def test___digital_single_channel_writer___write_waveform_multi_line_signal_count_mismatch___raises_daq_error(
    do_single_channel_multi_line_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_single_channel_multi_line_task.out_stream)
    num_samples = 20
    num_lines = 1
    waveform = _create_digital_waveform_uint8(num_samples, num_lines)

    with pytest.raises(DaqError) as exc_info:
        writer.write_waveform(waveform)

    error_message = exc_info.value.args[0]
    assert (
        "Specified read or write operation failed, because the number of lines in the data"
        in error_message
    )


def test___digital_single_channel_writer___write_waveform_port_uint8___outputs_match_final_values(
    do_port1_task: nidaqmx.Task,
    di_port1_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port1_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 10):
        num_samples = i
        num_lines = 8
        assert num_lines == _get_num_do_lines_in_task(do_port1_task)
        waveform = _create_digital_waveform_uint8(num_samples, num_lines)

        samples_written = writer.write_waveform(waveform)

        actual_value = di_port1_loopback_task.read()
        assert samples_written == num_samples
        assert waveform.signal_count == num_lines
        assert actual_value == _get_waveform_port_data(waveform)[i - 1]


def test___digital_single_channel_writer___write_waveform_port_uint32___outputs_match_final_values(
    do_port0_task: nidaqmx.Task,
    di_port0_loopback_task: nidaqmx.Task,
) -> None:
    writer = DigitalSingleChannelWriter(do_port0_task.out_stream)
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 10):
        num_samples = i
        num_lines = 32
        assert num_lines == _get_num_do_lines_in_task(do_port0_task)
        waveform = _create_digital_waveform_uint8(num_samples, num_lines)

        samples_written = writer.write_waveform(waveform)

        actual_value = di_port0_loopback_task.read()
        assert samples_written == num_samples
        assert waveform.signal_count == num_lines
        assert actual_value == _get_waveform_port_data(waveform)[i - 1]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/system/__init__.py sha256=655afcd1a3d92256e674ac9ddf71b6f05fdb01e11418c98bb1f2d4429f9b6cb3 bytes=45 -->
## FILE: tests/component/system/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/system/__init__.py`
- sha256: `655afcd1a3d92256e674ac9ddf71b6f05fdb01e11418c98bb1f2d4429f9b6cb3`
- bytes: 45

````python
"""Component tests for nidaqmx.system.*."""
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/system/_collections/__init__.py sha256=cf1b5a47ce939e9766ac7efcadb8cdc63f552ce989ef0d04ba7e9c334627b74a bytes=66 -->
## FILE: tests/component/system/_collections/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/system/_collections/__init__.py`
- sha256: `cf1b5a47ce939e9766ac7efcadb8cdc63f552ce989ef0d04ba7e9c334627b74a`
- bytes: 66

````python
"""Component tests for nidaqmx.system.storage._collections.*."""
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/system/_collections/test_device_collection.py sha256=5a9456594636a68b1771bb502dc9cac6cc742e3aae4108d6a0eaf5e7efb346b2 bytes=2171 -->
## FILE: tests/component/system/_collections/test_device_collection.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/system/_collections/test_device_collection.py`
- sha256: `5a9456594636a68b1771bb502dc9cac6cc742e3aae4108d6a0eaf5e7efb346b2`
- bytes: 2171

````python
import pytest

from nidaqmx.system import System


def test___devices___getitem_int___forward_order(system: System):
    devices = [system.devices[i] for i in range(len(system.devices))]

    assert [dev.name for dev in devices] == system.devices.device_names


def test___devices___getitem_int___shared_interpreter(system: System):
    devices = [system.devices[i] for i in range(len(system.devices))]

    assert all(dev._interpreter is system._interpreter for dev in devices)


def test___devices___getitem_slice___forward_order(system: System):
    devices = system.devices[:]

    assert [dev.name for dev in devices] == system.devices.device_names


def test___devices___getitem_slice___shared_interpreter(system: System):
    devices = system.devices[:]

    assert all(dev._interpreter is system._interpreter for dev in devices)


def test___devices___getitem_str___shared_interpreter(system: System):
    devices = [system.devices[name] for name in system.devices.device_names]

    assert all(dev._interpreter is system._interpreter for dev in devices)


def test___devices___getitem_str_list___shared_interpreter(system: System):
    if len(system.devices) < 2:
        pytest.skip("This test requires two or more devices.")

    devices = system.devices[",".join(system.devices.device_names)]

    assert all(dev._interpreter is system._interpreter for dev in devices)


def test___devices___iter___forward_order(system: System):
    devices = iter(system.devices)

    assert [dev.name for dev in devices] == system.devices.device_names


def test___devices___iter___shared_interpreter(system: System):
    devices = iter(system.devices)

    assert all(dev._interpreter is system._interpreter for dev in devices)


def test___devices___reversed___reverse_order(system: System):
    devices = reversed(system.devices)

    assert [dev.name for dev in devices] == list(reversed(system.devices.device_names))


def test___devices___reversed___shared_interpreter(system: System):
    devices = reversed(system.devices)

    assert all(dev._interpreter is system._interpreter for dev in devices)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/system/_collections/test_persisted_channel_collection.py sha256=e128081293b193896a9bad263ff7a9a1c74961878f8d848296a38a13915dea55 bytes=2531 -->
## FILE: tests/component/system/_collections/test_persisted_channel_collection.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/system/_collections/test_persisted_channel_collection.py`
- sha256: `e128081293b193896a9bad263ff7a9a1c74961878f8d848296a38a13915dea55`
- bytes: 2531

````python
import pytest

from nidaqmx.system import System


def test___global_channels___getitem_int___forward_order(system: System):
    channels = [system.global_channels[i] for i in range(len(system.global_channels))]

    assert [chan.name for chan in channels] == system.global_channels.global_channel_names


def test___global_channels___getitem_int___shared_interpreter(system: System):
    channels = [system.global_channels[i] for i in range(len(system.global_channels))]

    assert all(chan._interpreter is system._interpreter for chan in channels)


def test___global_channels___getitem_slice___forward_order(system: System):
    channels = system.global_channels[:]

    assert [chan.name for chan in channels] == system.global_channels.global_channel_names


def test___global_channels___getitem_slice___shared_interpreter(system: System):
    channels = system.global_channels[:]

    assert all(chan._interpreter is system._interpreter for chan in channels)


def test___global_channels___getitem_str___shared_interpreter(system: System):
    channels = [
        system.global_channels[name] for name in system.global_channels.global_channel_names
    ]

    assert all(chan._interpreter is system._interpreter for chan in channels)


def test___global_channels___getitem_str_list___shared_interpreter(system: System):
    if len(system.global_channels) < 2:
        pytest.skip("This test requires two or more global channels.")

    channels = system.global_channels[",".join(system.global_channels.global_channel_names)]

    assert all(chan._interpreter is system._interpreter for chan in channels)


def test___global_channels___iter___forward_order(system: System):
    channels = iter(system.global_channels)

    assert [chan.name for chan in channels] == system.global_channels.global_channel_names


def test___global_channels___iter___shared_interpreter(system: System):
    channels = iter(system.global_channels)

    assert all(chan._interpreter is system._interpreter for chan in channels)


def test___global_channels___reversed___reverse_order(system: System):
    channels = reversed(system.global_channels)

    assert [chan.name for chan in channels] == list(
        reversed(system.global_channels.global_channel_names)
    )


def test___global_channels___reversed___shared_interpreter(system: System):
    channels = reversed(system.global_channels)

    assert all(chan._interpreter is system._interpreter for chan in channels)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/system/_collections/test_persisted_scale_collection.py sha256=f622d8e6178a3788b0d907b9f11bdd1bfb7391764826c8434ee29cf998aa7885 bytes=2165 -->
## FILE: tests/component/system/_collections/test_persisted_scale_collection.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/system/_collections/test_persisted_scale_collection.py`
- sha256: `f622d8e6178a3788b0d907b9f11bdd1bfb7391764826c8434ee29cf998aa7885`
- bytes: 2165

````python
import pytest

from nidaqmx.system import System


def test___scales___getitem_int___forward_order(system: System):
    scales = [system.scales[i] for i in range(len(system.scales))]

    assert [scale.name for scale in scales] == system.scales.scale_names


def test___scales___getitem_int___shared_interpreter(system: System):
    scales = [system.scales[i] for i in range(len(system.scales))]

    assert all(scale._interpreter is system._interpreter for scale in scales)


def test___scales___getitem_slice___forward_order(system: System):
    scales = system.scales[:]

    assert [scale.name for scale in scales] == system.scales.scale_names


def test___scales___getitem_slice___shared_interpreter(system: System):
    scales = system.scales[:]

    assert all(scale._interpreter is system._interpreter for scale in scales)


def test___scales___getitem_str___shared_interpreter(system: System):
    scales = [system.scales[name] for name in system.scales.scale_names]

    assert all(scale._interpreter is system._interpreter for scale in scales)


def test___scales___getitem_str_list___shared_interpreter(system: System):
    if len(system.scales) < 2:
        pytest.skip("This test requires two or more persisted scales.")

    scales = system.scales[",".join(system.scales.scale_names)]

    assert all(scale._interpreter is system._interpreter for scale in scales)


def test___scales___iter___forward_order(system: System):
    scales = iter(system.scales)

    assert [scale.name for scale in scales] == system.scales.scale_names


def test___scales___iter___shared_interpreter(system: System):
    scales = iter(system.scales)

    assert all(scale._interpreter is system._interpreter for scale in scales)


def test___scales___reversed___reverse_order(system: System):
    scales = reversed(system.scales)

    assert [scale.name for scale in scales] == list(reversed(system.scales.scale_names))


def test___scales___reversed___shared_interpreter(system: System):
    scales = reversed(system.scales)

    assert all(scale._interpreter is system._interpreter for scale in scales)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/system/_collections/test_persisted_task_collection.py sha256=77efa9fdfebcb5be58acab282a6c0666db4993101ff3ed00bccd2e343aecdf5c bytes=2089 -->
## FILE: tests/component/system/_collections/test_persisted_task_collection.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/system/_collections/test_persisted_task_collection.py`
- sha256: `77efa9fdfebcb5be58acab282a6c0666db4993101ff3ed00bccd2e343aecdf5c`
- bytes: 2089

````python
import pytest

from nidaqmx.system import System


def test___tasks___getitem_int___forward_order(system: System):
    tasks = [system.tasks[i] for i in range(len(system.tasks))]

    assert [task.name for task in tasks] == system.tasks.task_names


def test___tasks___getitem_int___shared_interpreter(system: System):
    tasks = [system.tasks[i] for i in range(len(system.tasks))]

    assert all(task._interpreter is system._interpreter for task in tasks)


def test___tasks___getitem_slice___forward_order(system: System):
    tasks = system.tasks[:]

    assert [task.name for task in tasks] == system.tasks.task_names


def test___tasks___getitem_slice___shared_interpreter(system: System):
    tasks = system.tasks[:]

    assert all(task._interpreter is system._interpreter for task in tasks)


def test___tasks___getitem_str___shared_interpreter(system: System):
    tasks = [system.tasks[name] for name in system.tasks.task_names]

    assert all(task._interpreter is system._interpreter for task in tasks)


def test___tasks___getitem_str_list___shared_interpreter(system: System):
    if len(system.tasks) < 2:
        pytest.skip("This test requires two or more persisted tasks.")

    tasks = system.tasks[",".join(system.tasks.task_names)]

    assert all(task._interpreter is system._interpreter for task in tasks)


def test___tasks___iter___forward_order(system: System):
    tasks = iter(system.tasks)

    assert [task.name for task in tasks] == system.tasks.task_names


def test___tasks___iter___shared_interpreter(system: System):
    tasks = iter(system.tasks)

    assert all(task._interpreter is system._interpreter for task in tasks)


def test___tasks___reversed___reverse_order(system: System):
    tasks = reversed(system.tasks)

    assert [task.name for task in tasks] == list(reversed(system.tasks.task_names))


def test___tasks___reversed___shared_interpreter(system: System):
    tasks = reversed(system.tasks)

    assert all(task._interpreter is system._interpreter for task in tasks)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/system/_collections/test_physical_channel_collection.py sha256=e11057001632a476b6671c454001dd23c38eb5ab9b81320ee169c108c94e1110 bytes=11042 -->
## FILE: tests/component/system/_collections/test_physical_channel_collection.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/system/_collections/test_physical_channel_collection.py`
- sha256: `e11057001632a476b6671c454001dd23c38eb5ab9b81320ee169c108c94e1110`
- bytes: 11042

````python
import pytest

import nidaqmx.utils
from nidaqmx.system import Device

COLLECTION_NAMES = [
    "ai_physical_chans",
    "ao_physical_chans",
    "ci_physical_chans",
    "co_physical_chans",
    "di_lines",
    "di_ports",
    "do_lines",
    "do_ports",
]


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___getitem_int___forward_order(
    collection_name: str, sim_6363_device: Device
):
    physical_channels = getattr(sim_6363_device, collection_name)

    channels = [physical_channels[i] for i in range(len(physical_channels))]

    assert [chan.name for chan in channels] == physical_channels.channel_names


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___getitem_int___shared_interpreter(
    collection_name: str, sim_6363_device: Device
):
    physical_channels = getattr(sim_6363_device, collection_name)

    channels = [physical_channels[i] for i in range(len(physical_channels))]

    assert all(chan._interpreter is sim_6363_device._interpreter for chan in channels)


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___getitem_slice___forward_order(
    collection_name: str, sim_6363_device: Device
):
    physical_channels = getattr(sim_6363_device, collection_name)

    channels = physical_channels[:]

    assert [chan.name for chan in channels] == physical_channels.channel_names


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___getitem_slice___shared_interpreter(
    collection_name: str, sim_6363_device: Device
):
    physical_channels = getattr(sim_6363_device, collection_name)

    channels = physical_channels[:]

    assert all(chan._interpreter is sim_6363_device._interpreter for chan in channels)


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___getitem_unqualified_str___shared_interpreter(
    collection_name: str, sim_6363_device: Device
):
    physical_channels = getattr(sim_6363_device, collection_name)
    device_name = sim_6363_device.name
    unqualified_channel_names = [
        name.replace(device_name + "/", "") for name in physical_channels.channel_names
    ]

    channels = [physical_channels[name] for name in unqualified_channel_names]

    assert all(chan._interpreter is sim_6363_device._interpreter for chan in channels)


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___getitem_unqualified_str_list___shared_interpreter(
    collection_name: str, sim_6363_device: Device
):
    physical_channels = getattr(sim_6363_device, collection_name)
    device_name = sim_6363_device.name
    unqualified_channel_names = [
        name.replace(device_name + "/", "") for name in physical_channels.channel_names
    ]

    channels = physical_channels[",".join(unqualified_channel_names)]

    assert all(chan._interpreter is sim_6363_device._interpreter for chan in channels)


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___getitem_unqualified_str___name(
    collection_name: str, sim_6363_device: Device
):
    physical_channels = getattr(sim_6363_device, collection_name)
    device_name = sim_6363_device.name
    unqualified_channel_names = [
        name.replace(device_name + "/", "") for name in physical_channels.channel_names
    ]

    channels = [physical_channels[name] for name in unqualified_channel_names]

    assert all(chan.name == name for chan, name in zip(channels, physical_channels.channel_names))


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___getitem_unqualified_str_list___name(
    collection_name: str, sim_6363_device: Device
):
    physical_channels = getattr(sim_6363_device, collection_name)
    device_name = sim_6363_device.name
    unqualified_channel_names = [
        name.replace(device_name + "/", "") for name in physical_channels.channel_names
    ]

    channels = physical_channels[",".join(unqualified_channel_names)]

    assert all(chan.name == name for chan, name in zip(channels, physical_channels.channel_names))


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___getitem_qualified_str___shared_interpreter(
    collection_name: str, sim_6363_device: Device
):
    physical_channels = getattr(sim_6363_device, collection_name)

    channels = [physical_channels[name] for name in physical_channels.channel_names]

    assert all(chan._interpreter is sim_6363_device._interpreter for chan in channels)


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___getitem_qualified_str_list___shared_interpreter(
    collection_name: str, sim_6363_device: Device
):
    physical_channels = getattr(sim_6363_device, collection_name)

    channels = physical_channels[",".join(physical_channels.channel_names)]

    assert all(chan._interpreter is sim_6363_device._interpreter for chan in channels)


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___getitem_qualified_str___name(
    collection_name: str, sim_6363_device: Device
):
    physical_channels = getattr(sim_6363_device, collection_name)

    channels = [physical_channels[name] for name in physical_channels.channel_names]

    assert all(chan.name == name for chan, name in zip(channels, physical_channels.channel_names))


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___getitem_qualified_str_list___name(
    collection_name: str, sim_6363_device: Device
):
    physical_channels = getattr(sim_6363_device, collection_name)

    channels = physical_channels[",".join(physical_channels.channel_names)]

    assert all(chan.name == name for chan, name in zip(channels, physical_channels.channel_names))


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___getitem_mixed_str_list___shared_interpreter(
    collection_name: str, sim_6363_device: Device
):
    physical_channels = getattr(sim_6363_device, collection_name)
    device_name = sim_6363_device.name
    qualified_channel_names = physical_channels.channel_names
    unqualified_channel_names = [
        name.replace(device_name + "/", "") for name in qualified_channel_names
    ]
    middle_idx = len(qualified_channel_names) // 2
    mixed_channel_names = (
        physical_channels.channel_names[:middle_idx] + unqualified_channel_names[middle_idx:]
    )

    channels = physical_channels[",".join(mixed_channel_names)]

    assert all(chan._interpreter is sim_6363_device._interpreter for chan in channels)


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___getitem_mixed_str_list___name(
    collection_name: str, sim_6363_device: Device
):
    physical_channels = getattr(sim_6363_device, collection_name)
    device_name = sim_6363_device.name
    qualified_channel_names = physical_channels.channel_names
    unqualified_channel_names = [
        name.replace(device_name + "/", "") for name in qualified_channel_names
    ]
    middle_idx = len(qualified_channel_names) // 2
    mixed_channel_names = (
        physical_channels.channel_names[:middle_idx] + unqualified_channel_names[middle_idx:]
    )

    channels = physical_channels[",".join(mixed_channel_names)]

    assert all(chan.name == name for chan, name in zip(channels, physical_channels.channel_names))


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___getitem_qualified_internal_channel_list___name(
    collection_name: str, sim_6363_device: Device
):
    physical_channels = getattr(sim_6363_device, collection_name)
    internal_channel_names = [f"{sim_6363_device.name}/_ao{x}_vs_aognd" for x in range(4)]

    channels = physical_channels[",".join(internal_channel_names)]

    assert all(chan.name == name for chan, name in zip(channels, internal_channel_names))


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___getitem_unqualified_internal_channel_list___name(
    collection_name: str, sim_6363_device: Device
):
    physical_channels = getattr(sim_6363_device, collection_name)
    internal_channel_names = ["_ao{x}_vs_aognd" for x in range(4)]

    channels = physical_channels[",".join(internal_channel_names)]

    assert all(
        chan.name == f"{sim_6363_device.name}/{name}"
        for chan, name in zip(channels, internal_channel_names)
    )


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___iter___forward_order(collection_name: str, sim_6363_device: Device):
    physical_channels = getattr(sim_6363_device, collection_name)

    channels = iter(physical_channels)

    assert [chan.name for chan in channels] == physical_channels.channel_names


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___iter___shared_interpreter(
    collection_name: str, sim_6363_device: Device
):
    physical_channels = getattr(sim_6363_device, collection_name)

    channels = iter(physical_channels)

    assert all(chan._interpreter is sim_6363_device._interpreter for chan in channels)


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___reversed___reverse_order(
    collection_name: str, sim_6363_device: Device
):
    physical_channels = getattr(sim_6363_device, collection_name)

    channels = reversed(physical_channels)

    assert [chan.name for chan in channels] == list(reversed(physical_channels.channel_names))


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___reversed___shared_interpreter(
    collection_name: str, sim_6363_device: Device
):
    physical_channels = getattr(sim_6363_device, collection_name)

    channels = reversed(physical_channels)

    assert all(chan._interpreter is sim_6363_device._interpreter for chan in channels)


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___all___forward_order(collection_name: str, sim_6363_device: Device):
    physical_channels = getattr(sim_6363_device, collection_name)

    channel = physical_channels.all

    assert channel.name == nidaqmx.utils.flatten_channel_string(physical_channels.channel_names)


@pytest.mark.parametrize("collection_name", COLLECTION_NAMES)
def test___physical_channels___all___shared_interpreter(
    collection_name: str, sim_6363_device: Device
):
    physical_channels = getattr(sim_6363_device, collection_name)

    channel = physical_channels.all

    assert channel._interpreter is sim_6363_device._interpreter
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/system/storage/__init__.py sha256=f3620aa194368870a2bc7c2cebb30859e6e71b79d32c3047dad11574508e5831 bytes=53 -->
## FILE: tests/component/system/storage/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/system/storage/__init__.py`
- sha256: `f3620aa194368870a2bc7c2cebb30859e6e71b79d32c3047dad11574508e5831`
- bytes: 53

````python
"""Component tests for nidaqmx.system.storage.*."""
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/system/storage/test_persisted_channel.py sha256=cd57e5382fd78c440e95b57c8fc413c9c91cc45efe827f6b8a09f5d9aa5e8d2f bytes=2645 -->
## FILE: tests/component/system/storage/test_persisted_channel.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/system/storage/test_persisted_channel.py`
- sha256: `cd57e5382fd78c440e95b57c8fc413c9c91cc45efe827f6b8a09f5d9aa5e8d2f`
- bytes: 2645

````python
import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.system.storage import PersistedChannel


@pytest.fixture
def ai_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task:
    """Gets an AI task."""
    task.ai_channels.add_ai_voltage_chan(
        f"{sim_6363_device.name}/ai0:3", name_to_assign_to_channel="TestChannel"
    )
    return task


def test___persisted_channels_with_same_name___compare___equal(init_kwargs):
    persisted_channel1 = PersistedChannel("Channel1", **init_kwargs)
    persisted_channel2 = PersistedChannel("Channel1", **init_kwargs)

    assert persisted_channel1 is not persisted_channel2
    assert persisted_channel1 == persisted_channel2


def test___persisted_channels_with_different_names___compare___not_equal(init_kwargs):
    persisted_channel1 = PersistedChannel("Channel1", **init_kwargs)
    persisted_channel2 = PersistedChannel("Channel2", **init_kwargs)

    assert persisted_channel1 != persisted_channel2


def test___persisted_channels_with_same_name___hash___equal(init_kwargs):
    persisted_channel1 = PersistedChannel("Channel1", **init_kwargs)
    persisted_channel2 = PersistedChannel("Channel1", **init_kwargs)

    assert persisted_channel1 is not persisted_channel2
    assert hash(persisted_channel1) == hash(persisted_channel2)


def test___persisted_channels_with_different_names___hash___not_equal(init_kwargs):
    persisted_channel1 = PersistedChannel("Channel1", **init_kwargs)
    persisted_channel2 = PersistedChannel("Channel2", **init_kwargs)

    assert hash(persisted_channel1) != hash(persisted_channel2)


def test___save_persisted_channel___saves_persisted_channel_with_author(
    ai_task: nidaqmx.Task, init_kwargs: dict
) -> None:
    persisted_channel_name = "PersistedChannelSaveTest"
    persisted_channel_author = "test___save_persisted_channel___no_error"
    # We first need to check if the channel exists and delete it if it does
    # We test by trying to access the author property
    persisted_channel = PersistedChannel(persisted_channel_name, **init_kwargs)
    try:
        _ = persisted_channel.author
        persisted_channel.delete()
    except Exception:
        pass
    # Now we need to create a channel associated with a task, then we can save it
    channel = ai_task.ai_channels[0]

    channel.save(save_as=persisted_channel_name, author=persisted_channel_author)

    persisted_channel = PersistedChannel(persisted_channel_name, **init_kwargs)
    assert persisted_channel.author == persisted_channel_author
    persisted_channel.delete()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/system/storage/test_persisted_channel_properties.py sha256=3339cd01afec00ceaa93a1a7060a3ddfbf643c39ccef6ec18f3b0c4d589b2858 bytes=1142 -->
## FILE: tests/component/system/storage/test_persisted_channel_properties.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/system/storage/test_persisted_channel_properties.py`
- sha256: `3339cd01afec00ceaa93a1a7060a3ddfbf643c39ccef6ec18f3b0c4d589b2858`
- bytes: 1142

````python
import pytest

from nidaqmx import DaqError
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system.storage import PersistedChannel


def test___constructed_persisted_channel___get_property___returns_persisted_value(init_kwargs):
    persisted_channel = PersistedChannel("VoltageTesterChannel", **init_kwargs)

    assert persisted_channel.author == "Test Author"


def test___nonexistent_persisted_channel___get_property___raises_invalid_global_chan(init_kwargs):
    persisted_channel = PersistedChannel("NonexistentChannel", **init_kwargs)

    with pytest.raises(DaqError) as exc_info:
        _ = persisted_channel.author

    assert exc_info.value.error_code == DAQmxErrors.INVALID_GLOBAL_CHAN


@pytest.mark.channel_name("VoltageTesterChannel")
def test___persisted_channel___get_bool_property___returns_persisted_value(persisted_channel):
    assert persisted_channel.allow_interactive_editing


@pytest.mark.channel_name("VoltageTesterChannel")
def test___persisted_channel___get_string_property___returns_persisted_value(persisted_channel):
    assert persisted_channel.author == "Test Author"
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/system/storage/test_persisted_scale.py sha256=57314636ad65fbbda0ab305c37025a74b0e0e28b9975d6cc5fabe1f86719eb34 bytes=1489 -->
## FILE: tests/component/system/storage/test_persisted_scale.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/system/storage/test_persisted_scale.py`
- sha256: `57314636ad65fbbda0ab305c37025a74b0e0e28b9975d6cc5fabe1f86719eb34`
- bytes: 1489

````python
import pytest

from nidaqmx.system.storage import PersistedScale


def test___persisted_scales_with_same_name___compare___equal(init_kwargs):
    persisted_scale1 = PersistedScale("Scale1", **init_kwargs)
    persisted_scale2 = PersistedScale("Scale1", **init_kwargs)

    assert persisted_scale1 is not persisted_scale2
    assert persisted_scale1 == persisted_scale2


def test___persisted_scales_with_different_names___compare___not_equal(init_kwargs):
    persisted_scale1 = PersistedScale("Scale1", **init_kwargs)
    persisted_scale2 = PersistedScale("Scale2", **init_kwargs)

    assert persisted_scale1 != persisted_scale2


def test___persisted_scales_with_same_name___hash___equal(init_kwargs):
    persisted_scale1 = PersistedScale("Scale1", **init_kwargs)
    persisted_scale2 = PersistedScale("Scale1", **init_kwargs)

    assert persisted_scale1 is not persisted_scale2
    assert hash(persisted_scale1) == hash(persisted_scale2)


def test___persisted_scales_with_different_names___hash___not_equal(init_kwargs):
    persisted_scale1 = PersistedScale("Scale1", **init_kwargs)
    persisted_scale2 = PersistedScale("Scale2", **init_kwargs)

    assert hash(persisted_scale1) != hash(persisted_scale2)


@pytest.mark.scale_name("double_gain_scale")
def test___persisted_scale___load___shared_interpreter(persisted_scale: PersistedScale):
    scale = persisted_scale.load()

    assert scale._interpreter is persisted_scale._interpreter
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/system/storage/test_persisted_scale_properties.py sha256=de87d0460705244a82984fb0ca233e0922e787cf7de74b2b85c5f09ecf17669d bytes=1801 -->
## FILE: tests/component/system/storage/test_persisted_scale_properties.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/system/storage/test_persisted_scale_properties.py`
- sha256: `de87d0460705244a82984fb0ca233e0922e787cf7de74b2b85c5f09ecf17669d`
- bytes: 1801

````python
import pytest

from nidaqmx import DaqError
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system.storage import PersistedScale


def test___constructed_persisted_scale___get_property___returns_persisted_value(init_kwargs):
    persisted_scale = PersistedScale("double_gain_scale", **init_kwargs)

    assert persisted_scale.author == "Test Author"


def test___nonexistent_persisted_scale___get_property___raises_custom_scale_does_not_exist(
    init_kwargs,
):
    persisted_scale = PersistedScale("NonexistentScale", **init_kwargs)

    with pytest.raises(DaqError) as exc_info:
        _ = persisted_scale.author

    assert exc_info.value.error_code == DAQmxErrors.CUSTOM_SCALE_DOES_NOT_EXIST


@pytest.mark.scale_name("double_gain_scale")
def test___persisted_scale___get_bool_property___returns_persisted_value(persisted_scale):
    assert persisted_scale.allow_interactive_editing


@pytest.mark.scale_name("double_gain_scale")
def test___persisted_scale___get_string_property___returns_persisted_value(persisted_scale):
    assert persisted_scale.author == "Test Author"


@pytest.mark.scale_name("double_gain_scale")
def test___persisted_scale___load_and_get_float64_property___returns_persisted_value(
    persisted_scale,
):
    assert persisted_scale.load().lin_slope == 2.0


@pytest.mark.scale_name("polynomial_scale")
def test___persisted_scale___load_and_get_float64_list_property___returns_persisted_value(
    persisted_scale,
):
    assert persisted_scale.load().poly_forward_coeff == [0.0, 1.0]


@pytest.mark.scale_name("double_gain_scale")
def test___persisted_scale___load_and_get_string_property___returns_persisted_value(
    persisted_scale,
):
    assert persisted_scale.load().description == "Twice the gain"
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/system/storage/test_persisted_task.py sha256=b194e165146c7234ea74eb1278470d74faf6660330b64b7a0b2236f3d9c2a315 bytes=3857 -->
## FILE: tests/component/system/storage/test_persisted_task.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/system/storage/test_persisted_task.py`
- sha256: `b194e165146c7234ea74eb1278470d74faf6660330b64b7a0b2236f3d9c2a315`
- bytes: 3857

````python
import pytest

from nidaqmx import DaqError, SessionInitializationBehavior
from nidaqmx.constants import READ_ALL_AVAILABLE
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import RpcError
from nidaqmx.system.storage import PersistedTask


def test___persisted_tasks_with_same_name___compare___equal(init_kwargs):
    persisted_task1 = PersistedTask("Task1", **init_kwargs)
    persisted_task2 = PersistedTask("Task1", **init_kwargs)

    assert persisted_task1 is not persisted_task2
    assert persisted_task1 == persisted_task2


def test___persisted_tasks_with_different_names___compare___not_equal(init_kwargs):
    persisted_task1 = PersistedTask("Task1", **init_kwargs)
    persisted_task2 = PersistedTask("Task2", **init_kwargs)

    assert persisted_task1 != persisted_task2


def test___persisted_tasks_with_same_name___hash___equal(init_kwargs):
    persisted_task1 = PersistedTask("Task1", **init_kwargs)
    persisted_task2 = PersistedTask("Task1", **init_kwargs)

    assert persisted_task1 is not persisted_task2
    assert hash(persisted_task1) == hash(persisted_task2)


def test___persisted_tasks_with_different_names___hash___not_equal(init_kwargs):
    persisted_task1 = PersistedTask("Task1", **init_kwargs)
    persisted_task2 = PersistedTask("Task2", **init_kwargs)

    assert hash(persisted_task1) != hash(persisted_task2)


@pytest.mark.task_name("VoltageTesterTask")
def test___persisted_task___load_and_read___returns_persisted_sample_count(
    persisted_task: PersistedTask,
):
    with persisted_task.load() as task:
        samples = task.read(READ_ALL_AVAILABLE)

    assert len(samples) == 100
    assert all(-10.0 <= s <= 10.0 for s in samples)


@pytest.mark.task_name("VoltageTesterTask")
@pytest.mark.library_only(reason="Default gRPC initialization behavior is auto (create or attach)")
def test___persisted_task___load_twice___raises_duplicate_task(persisted_task: PersistedTask):
    with persisted_task.load():
        with pytest.raises(DaqError) as exc_info:
            with persisted_task.load():
                pass

    assert exc_info.value.error_code == DAQmxErrors.DUPLICATE_TASK


@pytest.mark.task_name("VoltageTesterTask")
@pytest.mark.grpc_only(reason="Default gRPC initialization behavior is auto (create or attach)")
@pytest.mark.grpc_session_initialization_behavior(SessionInitializationBehavior.AUTO)
def test___grpc_session_initialization_behavior_auto___load_twice___returns_multiple_task_proxies(
    persisted_task: PersistedTask,
):
    with persisted_task.load() as task1:
        with persisted_task.load() as task2:
            same_object = task1 is task2
            task1_name = task1.name
            task2_name = task2.name

    assert not same_object
    assert task1_name == task2_name


@pytest.mark.task_name("VoltageTesterTask")
@pytest.mark.grpc_only(reason="Default gRPC initialization behavior is auto (create or attach)")
@pytest.mark.grpc_session_initialization_behavior(
    SessionInitializationBehavior.INITIALIZE_SERVER_SESSION
)
def test___grpc_session_initialization_behavior_initialize_server_session___load_twice___raises_duplicate_task(
    persisted_task: PersistedTask,
):
    import grpc

    with persisted_task.load():
        with pytest.raises(RpcError) as exc_info:
            with persisted_task.load():
                pass

    assert exc_info.value.rpc_code == grpc.StatusCode.ALREADY_EXISTS
    assert "VoltageTesterTask" in exc_info.value.args[0]


@pytest.mark.task_name("VoltageTesterTask")
def test___persisted_task___load___shared_interpreter(
    persisted_task: PersistedTask,
):
    with persisted_task.load() as task:
        task_interpreter = task._interpreter

    assert task_interpreter is persisted_task._interpreter
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/system/storage/test_persisted_task_properties.py sha256=a5b0f96edc1a6f5d8f4c2448623dec8e67d30698a9b478272ce9941638ff168f bytes=2743 -->
## FILE: tests/component/system/storage/test_persisted_task_properties.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/system/storage/test_persisted_task_properties.py`
- sha256: `a5b0f96edc1a6f5d8f4c2448623dec8e67d30698a9b478272ce9941638ff168f`
- bytes: 2743

````python
import pytest

from nidaqmx import DaqError
from nidaqmx.constants import (
    AcquisitionType,
    TerminalConfiguration,
    UsageTypeAI,
)
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system.storage import PersistedTask


def test___constructed_persisted_task___get_property___returns_persisted_value(init_kwargs):
    persisted_task = PersistedTask("VoltageTesterTask", **init_kwargs)

    assert persisted_task.author == "Test Author"


def test___nonexistent_persisted_task___get_property___raises_task_not_in_data_neighborhood(
    init_kwargs,
):
    persisted_task = PersistedTask("NonexistentTask", **init_kwargs)

    with pytest.raises(DaqError) as exc_info:
        _ = persisted_task.author

    assert exc_info.value.error_code == DAQmxErrors.TASK_NOT_IN_DATA_NEIGHBORHOOD


@pytest.mark.task_name("VoltageTesterTask")
def test___persisted_task___get_bool_property___returns_persisted_value(
    persisted_task: PersistedTask,
):
    assert persisted_task.allow_interactive_editing


@pytest.mark.task_name("VoltageTesterTask")
def test___persisted_task___get_string_property___returns_persisted_value(
    persisted_task: PersistedTask,
):
    assert persisted_task.author == "Test Author"


@pytest.mark.task_name("VoltageTesterTask")
def test___persisted_task___load_and_get_channel_properties___returns_persisted_values(
    persisted_task: PersistedTask,
):
    with persisted_task.load() as task:
        ai_meas_type = task.ai_channels[0].ai_meas_type
        ai_term_cfg = task.ai_channels[0].ai_term_cfg
        ai_max = task.ai_channels[0].ai_max

    assert ai_meas_type == UsageTypeAI.VOLTAGE
    assert ai_term_cfg == TerminalConfiguration.DIFF
    assert ai_max == 10.0


@pytest.mark.task_name("VoltageTesterTask")
def test___persisted_task___load_and_get_task_properties___returns_persisted_values(
    persisted_task: PersistedTask,
):
    with persisted_task.load() as task:
        channel_names = task.channel_names

    assert channel_names == ["Voltage_0"]


# Don't test samp_clk_src because it requires reserving the task and returns a coerced value,
# not the persisted value.
@pytest.mark.task_name("VoltageTesterTask")
def test___persisted_task___load_and_get_timing_properties___returns_persisted_values(
    persisted_task: PersistedTask,
):
    with persisted_task.load() as task:
        samp_clk_rate = task.timing.samp_clk_rate
        samp_quant_samp_mode = task.timing.samp_quant_samp_mode
        samp_quant_samp_per_chan = task.timing.samp_quant_samp_per_chan

    assert samp_clk_rate == 1000.0
    assert samp_quant_samp_mode == AcquisitionType.FINITE
    assert samp_quant_samp_per_chan == 100
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/system/test_device.py sha256=be3b4117429035c356696129d59c601e3dca329d04682be2895b4b7a5fd2d7f1 bytes=2152 -->
## FILE: tests/component/system/test_device.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/system/test_device.py`
- sha256: `be3b4117429035c356696129d59c601e3dca329d04682be2895b4b7a5fd2d7f1`
- bytes: 2152

````python
import sys

import pytest

from nidaqmx import DaqError
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system import Device


def test___devices_with_same_name___compare___equal(init_kwargs):
    device1 = Device("bridgeTester", **init_kwargs)
    device2 = Device("bridgeTester", **init_kwargs)

    assert device1 is not device2
    assert device1 == device2


def test___devices_with_different_names___compare___not_equal(init_kwargs):
    device1 = Device("bridgeTester", **init_kwargs)
    device2 = Device("tsVoltageTester1", **init_kwargs)

    assert device1 != device2


def test___devices_with_same_name___hash___equal(init_kwargs):
    device1 = Device("bridgeTester", **init_kwargs)
    device2 = Device("bridgeTester", **init_kwargs)

    assert device1 is not device2
    assert hash(device1) == hash(device2)


def test___devices_with_different_names___hash___not_equal(init_kwargs):
    device1 = Device("bridgeTester", **init_kwargs)
    device2 = Device("tsVoltageTester1", **init_kwargs)

    assert hash(device1) != hash(device2)


def test___self_test_device___no_errors(sim_6363_device: Device) -> None:
    sim_6363_device.self_test_device()


def test___restore_last_ext_cal_const___no_errors(sim_6363_device: Device) -> None:
    sim_6363_device.restore_last_ext_cal_const()


def test___self_cal___no_errors(sim_6363_device: Device) -> None:
    sim_6363_device.self_cal()


@pytest.mark.skipif(not sys.platform.startswith("win"), reason="mioDAQ support Windows-only")
def test___read_id_pin_memory___error(sim_6423_device: Device) -> None:
    with pytest.raises(DaqError) as exc_info:
        sim_6423_device.read_id_pin_memory("id0")

    assert exc_info.value.error_code == DAQmxErrors.ID_PIN_NO_EEPROM


@pytest.mark.skipif(not sys.platform.startswith("win"), reason="mioDAQ support Windows-only")
def test___write_id_pin_memory___error(sim_6423_device: Device) -> None:
    with pytest.raises(DaqError) as exc_info:
        sim_6423_device.write_id_pin_memory("id0", [0], 1)

    assert exc_info.value.error_code == DAQmxErrors.ID_PIN_NO_EEPROM
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/system/test_device_properties.py sha256=d178be8341f800a05718a0b4ec3fd7d67c366b3dc68ed243dee54112676411ec bytes=8382 -->
## FILE: tests/component/system/test_device_properties.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/system/test_device_properties.py`
- sha256: `d178be8341f800a05718a0b4ec3fd7d67c366b3dc68ed243dee54112676411ec`
- bytes: 8382

````python
import sys
from datetime import datetime

import pytest

from nidaqmx import DaqError
from nidaqmx.constants import BusType, IDPinStatus, TriggerUsage
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system import Device


def test___constructed_device___get_property___returns_value(init_kwargs):
    device = Device("bridgeTester", **init_kwargs)

    assert device.product_type == "PXIe-4331"


def test___nonexistent_device___get_property___raises_invalid_device_id(init_kwargs):
    device = Device("NonexistentDevice", **init_kwargs)

    with pytest.raises(DaqError) as exc_info:
        _ = device.product_type

    assert exc_info.value.error_code == DAQmxErrors.INVALID_DEVICE_ID


@pytest.mark.device_name("bridgeTester")
def test___device___bool_property___returns_value(device):
    # The PXIe-4331 supports analog triggering
    assert device.anlg_trig_supported


@pytest.mark.device_name("bridgeTester")
def test___device___float_property___returns_value(device):
    # The ai max single channel rate of the NI PXIe-4331 device is 102400.0
    assert device.ai_max_single_chan_rate == 102400.0


@pytest.mark.device_name("bridgeTester")
def test___device___uint_property___returns_value(device):
    assert device.product_num == 0x74A9C4C4


@pytest.mark.device_name("bridgeTester")
def test___device___string_property___returns_value(device):
    assert device.product_type == "PXIe-4331"


@pytest.mark.device_name("bridgeTester")
def test___device___enum_property___returns_value(device):
    assert device.bus_type == BusType.PXIE


@pytest.mark.device_name("bridgeTester")
def test___device___list_of_float_property___returns_value(device):
    ai_bridge_ranges = device.ai_bridge_rngs

    assert isinstance(ai_bridge_ranges, list)
    assert ai_bridge_ranges == [-0.025, 0.025, -0.1, 0.1]


@pytest.mark.device_name("bridgeTester")
def test___device___list_of_enum_property___returns_value(device):
    ai_trigger_usage = device.ai_trig_usage

    assert isinstance(ai_trigger_usage, list)
    assert ai_trigger_usage == [TriggerUsage.REFERENCE, TriggerUsage.START]


@pytest.mark.device_name("bridgeTester")
def test___device___list_of_uint_property___returns_value(device):
    accessory_product_numbers = device.accessory_product_nums

    assert isinstance(accessory_product_numbers, list)
    assert accessory_product_numbers == [0x7992]


@pytest.mark.device_name("bridgeTester")
def test___device___get_deprecated_properties___reports_warnings(device):
    with pytest.deprecated_call():
        assert device.is_simulated == device.dev_is_simulated
    with pytest.deprecated_call():
        assert device.serial_num == device.dev_serial_num
    with pytest.deprecated_call():
        assert device.hwteds_supported == device.tedshwteds_supported


@pytest.mark.device_name("tsChassisTester")
def test___chassis___get_modules___returns_modules(device: Device):
    modules = device.chassis_module_devices

    assert [mod.name for mod in modules] == ["tsPowerTester1", "tsPowerTester2", "tsVoltageTester1"]


@pytest.mark.device_name("tsChassisTester")
def test___chassis___get_modules___shared_interpreter(device: Device):
    modules = device.chassis_module_devices

    assert all(mod._interpreter is device._interpreter for mod in modules)


@pytest.mark.device_name("tsVoltageTester1")
def test___module___get_chassis___returns_chassis(device: Device):
    chassis = device.compact_daq_chassis_device

    assert chassis.name == "tsChassisTester"


@pytest.mark.device_name("tsVoltageTester1")
def test___module___get_chassis___shared_interpreter(device: Device):
    chassis = device.compact_daq_chassis_device

    assert chassis._interpreter is device._interpreter


def test___ext_cal_last_date_and_time___no_errors(real_x_series_device: Device) -> None:
    last_date_and_time = real_x_series_device.ext_cal_last_date_and_time

    assert type(last_date_and_time) is datetime
    assert last_date_and_time.year >= 2009
    assert last_date_and_time.month >= 1
    assert last_date_and_time.day > 0
    assert last_date_and_time.hour >= 0
    assert last_date_and_time.minute >= 0


def test___self_cal_last_date_and_time___no_errors(real_x_series_device: Device) -> None:
    last_date_and_time = real_x_series_device.self_cal_last_date_and_time

    assert type(last_date_and_time) is datetime
    assert last_date_and_time.year >= 2009
    assert last_date_and_time.month >= 1
    assert last_date_and_time.day > 0
    assert last_date_and_time.hour >= 0
    assert last_date_and_time.minute >= 0


def test___device_supports_cal___no_errors(real_x_series_device: Device) -> None:
    is_cal_supported = real_x_series_device.device_supports_cal

    assert is_cal_supported is True


def test___cal_acc_connection_count__raises_attr_not_supported(
    real_x_series_device: Device,
) -> None:
    with pytest.raises(DaqError) as exc_info:
        _ = real_x_series_device.cal_acc_connection_count

    assert exc_info.value.error_code == DAQmxErrors.ATTR_NOT_SUPPORTED


def test___cal_recommended_acc_connection_count_limit___raises_attr_not_supported(
    real_x_series_device: Device,
) -> None:
    with pytest.raises(DaqError) as exc_info:
        _ = real_x_series_device.cal_recommended_acc_connection_count_limit

    assert exc_info.value.error_code == DAQmxErrors.ATTR_NOT_SUPPORTED


def test___cal_user_defined_info___no_errors(real_x_series_device: Device) -> None:
    try:
        user_defined_info = real_x_series_device.cal_user_defined_info
        info_max_size = real_x_series_device.cal_user_defined_info_max_size

        test_value = "my test value"[:info_max_size]
        real_x_series_device.cal_user_defined_info = test_value
        value = real_x_series_device.cal_user_defined_info

        assert info_max_size == len(value)
        assert value in test_value
    finally:
        real_x_series_device.cal_user_defined_info = user_defined_info


def test___cal_dev_temp___no_errors(sim_6363_device: Device) -> None:
    temperature = sim_6363_device.cal_dev_temp

    assert 0.0 == temperature


def test___ext_cal_last_temp___no_errors(sim_6363_device: Device) -> None:
    temperature = sim_6363_device.ext_cal_last_temp

    assert 0.0 == temperature


def test___ext_cal_recommended_interval___no_errors(sim_6363_device: Device) -> None:
    interval = sim_6363_device.ext_cal_recommended_interval

    assert 24 == interval


def test___self_cal_last_temp___no_errors(sim_6363_device: Device) -> None:
    temperature = sim_6363_device.self_cal_last_temp

    assert 0.0 == temperature


def test___self_cal_supported___no_errors(real_x_series_device: Device) -> None:
    is_cal_supported = real_x_series_device.self_cal_supported

    assert is_cal_supported is True


@pytest.mark.skipif(not sys.platform.startswith("win"), reason="mioDAQ support Windows-only")
def test___id_pin_mem_serial_nums___no_errors(sim_6423_device: Device) -> None:
    mem_serial_nums = sim_6423_device.id_pin_mem_serial_nums

    assert mem_serial_nums == ["", ""]


@pytest.mark.skipif(not sys.platform.startswith("win"), reason="mioDAQ support Windows-only")
def test___id_pin_mem_family_codes___no_errors(sim_6423_device: Device) -> None:
    mem_family_codes = sim_6423_device.id_pin_mem_family_codes

    assert mem_family_codes == [0, 0]


@pytest.mark.skipif(not sys.platform.startswith("win"), reason="mioDAQ support Windows-only")
def test___id_pin_mem_sizes___no_errors(sim_6423_device: Device) -> None:
    mem_sizes = sim_6423_device.id_pin_mem_sizes

    assert mem_sizes == [0, 0]


@pytest.mark.skipif(not sys.platform.startswith("win"), reason="mioDAQ support Windows-only")
def test___id_pin_pin_names___no_errors(sim_6423_device: Device) -> None:
    pin_names = sim_6423_device.id_pin_pin_names

    assert pin_names == ["id0", "id1"]


@pytest.mark.skipif(not sys.platform.startswith("win"), reason="mioDAQ support Windows-only")
def test___id_pin_pin_statuses___no_errors(sim_6423_device: Device) -> None:
    pin_statuses = sim_6423_device.id_pin_pin_statuses

    assert pin_statuses == [IDPinStatus.MEMORY_NOT_PRESENT, IDPinStatus.MEMORY_NOT_PRESENT]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/system/test_physical_channel.py sha256=56c2b53e01109312ab90b15c41176fa43935d8472054a3450dcb1ff9506b5dc0 bytes=3232 -->
## FILE: tests/component/system/test_physical_channel.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/system/test_physical_channel.py`
- sha256: `56c2b53e01109312ab90b15c41176fa43935d8472054a3450dcb1ff9506b5dc0`
- bytes: 3232

````python
import pytest

import nidaqmx
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system import PhysicalChannel
from tests.component.system.test_physical_channel_properties import VALUES_IN_TED


def test___physical_channels_with_same_name___compare___equal(init_kwargs):
    phys_chan1 = PhysicalChannel("bridgeTester/ai2", **init_kwargs)
    phys_chan2 = PhysicalChannel("bridgeTester/ai2", **init_kwargs)

    assert phys_chan1 is not phys_chan2
    assert phys_chan1 == phys_chan2


def test___physical_channels_with_different_names___compare___not_equal(
    init_kwargs,
):
    phys_chan1 = PhysicalChannel("bridgeTester/ai2", **init_kwargs)
    phys_chan2 = PhysicalChannel("bridgeTester/ai3", **init_kwargs)
    phys_chan3 = PhysicalChannel("tsVoltageTester1/ai2", **init_kwargs)

    assert phys_chan1 != phys_chan2
    assert phys_chan1 != phys_chan3


def test___physical_channels_with_same_name___hash___equal(init_kwargs):
    phys_chan1 = PhysicalChannel("bridgeTester/ai2", **init_kwargs)
    phys_chan2 = PhysicalChannel("bridgeTester/ai2", **init_kwargs)

    assert phys_chan1 is not phys_chan2
    assert hash(phys_chan1) == hash(phys_chan2)


def test___physical_channels_with_different_names___hash___not_equal(
    init_kwargs,
):
    phys_chan1 = PhysicalChannel("bridgeTester/ai2", **init_kwargs)
    phys_chan2 = PhysicalChannel("bridgeTester/ai3", **init_kwargs)
    phys_chan3 = PhysicalChannel("tsVoltageTester1/ai2", **init_kwargs)

    assert hash(phys_chan1) != hash(phys_chan2)
    assert hash(phys_chan1) != hash(phys_chan3)


def test___invalid_bitstream___write_to_teds_from_array___throws_data_error(
    sim_6363_device,
):
    phys_chan = sim_6363_device.ai_physical_chans["ai0"]

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        phys_chan.write_to_teds_from_array([1, 2, 3, 4])

    assert exc_info.value.error_code == DAQmxErrors.TEDS_SENSOR_DATA_ERROR


def test___valid_bitstream___write_to_teds_from_array___throws_config_or_detection_error(
    sim_6363_device,
):
    phys_chan = sim_6363_device.ai_physical_chans["ai0"]

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        phys_chan.write_to_teds_from_array(VALUES_IN_TED)

    assert exc_info.value.error_code in [
        DAQmxErrors.CANT_CONFIGURE_TEDS_FOR_CHAN,
        DAQmxErrors.TEDS_SENSOR_NOT_DETECTED,
    ]


def test___invalid_file_path___write_to_teds_from_file___throws_data_error(
    sim_6363_device,
):
    phys_chan = sim_6363_device.ai_physical_chans["ai0"]

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        phys_chan.write_to_teds_from_file()

    assert exc_info.value.error_code == DAQmxErrors.TEDS_SENSOR_DATA_ERROR


def test___valid_file_path___write_to_teds_from_array___throws_config_or_detection_error(
    sim_6363_device, voltage_teds_file_path
):
    phys_chan = sim_6363_device.ai_physical_chans["ai0"]

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        phys_chan.write_to_teds_from_file(voltage_teds_file_path)

    assert exc_info.value.error_code in [
        DAQmxErrors.CANT_CONFIGURE_TEDS_FOR_CHAN,
        DAQmxErrors.TEDS_SENSOR_NOT_DETECTED,
    ]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/system/test_physical_channel_properties.py sha256=b08e7f55469c588ef34787a9c58548dc759fd2651c270d8d3134553c1fbe3dc6 bytes=3744 -->
## FILE: tests/component/system/test_physical_channel_properties.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/system/test_physical_channel_properties.py`
- sha256: `b08e7f55469c588ef34787a9c58548dc759fd2651c270d8d3134553c1fbe3dc6`
- bytes: 3744

````python
import sys

import numpy
import pytest

from nidaqmx import DaqError
from nidaqmx.constants import LogicFamily, TerminalConfiguration, UsageTypeAI
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system import PhysicalChannel
from tests.helpers import configure_teds


def test___constructed_physical_channel___get_property___returns_value(init_kwargs):
    phys_chan = PhysicalChannel("bridgeTester/ai2", **init_kwargs)

    assert UsageTypeAI.BRIDGE in phys_chan.ai_meas_types


def test___nonexistent_physical_channel___get_property___raises_physical_chan_does_not_exist(
    init_kwargs,
):
    phys_chan = PhysicalChannel("bridgeTester/ai1234", **init_kwargs)

    with pytest.raises(DaqError) as exc_info:
        _ = phys_chan.ai_meas_types

    assert exc_info.value.error_code == DAQmxErrors.PHYSICAL_CHAN_DOES_NOT_EXIST


def test___physical_channel___get_bool_property___returns_value(sim_6363_device):
    phys_chans = sim_6363_device.di_lines

    assert phys_chans[0].di_change_detect_supported


def test___physical_channel_with_teds___get_bit_stream___returns_configured_value(
    sim_6363_device, voltage_teds_file_path
):
    expected_value = numpy.array(VALUES_IN_TED, dtype=numpy.uint8)

    with configure_teds(
        sim_6363_device.ai_physical_chans["ai0"], voltage_teds_file_path
    ) as phys_chan:
        assert (phys_chan.teds_bit_stream == expected_value).all()


def test___physical_channel___get_int32_array_property___returns_default_value(
    sim_6363_device,
):
    phys_chans = sim_6363_device.ai_physical_chans
    ai_channel = phys_chans["ai0"]
    expected_configs = [
        TerminalConfiguration.RSE,
        TerminalConfiguration.NRSE,
        TerminalConfiguration.DIFF,
    ]

    assert ai_channel.ai_term_cfgs == expected_configs


def test___physical_channel_with_teds___get_string_property___returns_configured_value(
    sim_6363_device, voltage_teds_file_path
):
    with configure_teds(
        sim_6363_device.ai_physical_chans["ai0"], voltage_teds_file_path
    ) as phys_chan:
        assert phys_chan.teds_version_letter == "A"


def test___physical_channel_with_teds___get_uint32_array_property___returns_configured_value(
    sim_6363_device, voltage_teds_file_path
):
    with configure_teds(
        sim_6363_device.ai_physical_chans["ai0"], voltage_teds_file_path
    ) as phys_chan:
        assert phys_chan.teds_template_ids == [30]


def test___physical_channel_with_teds___get_uint32_property___returns_configured_value(
    sim_6363_device, voltage_teds_file_path
):
    with configure_teds(
        sim_6363_device.ai_physical_chans["ai0"], voltage_teds_file_path
    ) as phys_chan:
        assert phys_chan.teds_mfg_id == 17


@pytest.mark.skipif(not sys.platform.startswith("win"), reason="mioDAQ support Windows-only")
def test___physical_channel___get_int32_property___returns_value():
    phys_chans = PhysicalChannel("mioDAQ/port0")

    assert phys_chans.dig_port_logic_family in LogicFamily


@pytest.mark.skipif(not sys.platform.startswith("win"), reason="mioDAQ support Windows-only")
@pytest.mark.library_only(
    reason="AB#2375679: gRPC interpreter doesn't support setting physical channel property."
)
def test___physical_channel___set_int32_property___success():
    phys_chans = PhysicalChannel("mioDAQ/port0")

    phys_chans.dig_port_logic_family = LogicFamily.ONE_POINT_EIGHT_V


VALUES_IN_TED = [
    17,
    64,
    0,
    32,
    4,
    57,
    48,
    0,
    120,
    0,
    0,
    0,
    200,
    194,
    0,
    0,
    200,
    66,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    48,
]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/system/test_system.py sha256=a468d49c5554c1f423f1c4f0dfc15a7e65f551bd2f90f6a52360bd083fc4d0b2 bytes=4582 -->
## FILE: tests/component/system/test_system.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/system/test_system.py`
- sha256: `a468d49c5554c1f423f1c4f0dfc15a7e65f551bd2f90f6a52360bd083fc4d0b2`
- bytes: 4582

````python
import sys

import pytest

import nidaqmx
from nidaqmx.constants import PowerUpChannelType
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system import System
from nidaqmx.types import AOPowerUpState


def test___get_analog_power_up_states_with_output_type___returns_power_up_states(system):
    channel_names = ["aoTester/ao0", "aoTester/ao1"]

    power_up_states = system.get_analog_power_up_states_with_output_type(channel_names)

    assert len(power_up_states) == len(channel_names)
    for i in range(len(channel_names)):
        assert channel_names[i] == power_up_states[i].physical_channel
        assert 0.0 == power_up_states[i].power_up_state
        assert PowerUpChannelType.CHANNEL_HIGH_IMPEDANCE == power_up_states[i].channel_type


def test_valid_power_up_states___set_analog_power_up_states_with_output_type___sets_power_up_states_without_errors(
    system,
):
    channel_names = ["aoTester/ao0", "aoTester/ao1"]
    power_up_states = [
        AOPowerUpState(
            physical_channel=channel_name,
            power_up_state=-1.0,
            channel_type=PowerUpChannelType.CHANNEL_HIGH_IMPEDANCE,
        )
        for channel_name in channel_names
    ]

    system.set_analog_power_up_states_with_output_type(power_up_states)


def test_invalid_power_up_states___set_analog_power_up_states_with_output_type___throws_invalid_attribute_value_error(
    system,
):
    power_up_states = [
        AOPowerUpState(
            physical_channel="aoTester/ao0",
            power_up_state=1,
            channel_type=PowerUpChannelType.CHANNEL_VOLTAGE,
        ),
        AOPowerUpState(
            physical_channel="aoTester/ao1",
            power_up_state=20,
            channel_type=PowerUpChannelType.CHANNEL_VOLTAGE,
        ),
    ]

    with pytest.raises(nidaqmx.DaqError) as exc_info:
        system.set_analog_power_up_states_with_output_type(power_up_states)

    assert exc_info.value.error_code == DAQmxErrors.INVALID_ATTRIBUTE_VALUE


@pytest.mark.skipif(
    not sys.platform.startswith("win"), reason="DAQmxGetAnalogPowerUpStates is Windows-only"
)
def test___get_analog_power_up_states___returns_power_up_states(system):
    device_name = "aoTester"

    with pytest.deprecated_call():
        power_up_states = system.get_analog_power_up_states(device_name)

    channel_names = system.devices[device_name].ao_physical_chans.channel_names
    assert len(power_up_states) == len(channel_names)
    for i in range(len(channel_names)):
        assert power_up_states[i].physical_channel == channel_names[i]
        assert power_up_states[i].power_up_state == 0.0
        assert power_up_states[i].channel_type == PowerUpChannelType.CHANNEL_HIGH_IMPEDANCE


@pytest.mark.skipif(
    not sys.platform.startswith("win"), reason="DAQmxSetAnalogPowerUpStates is Windows-only"
)
def test_valid_power_up_states___set_analog_power_up_states___sets_power_up_states_without_errors(
    system,
):
    device_name = "aoTester"
    channel_names = ["aoTester/ao0", "aoTester/ao1"]
    power_up_states = [
        AOPowerUpState(
            physical_channel=channel_name,
            power_up_state=-1.0,
            channel_type=PowerUpChannelType.CHANNEL_VOLTAGE,
        )
        for channel_name in channel_names
    ]

    with pytest.deprecated_call():
        system.set_analog_power_up_states(device_name, power_up_states)


@pytest.mark.skipif(
    not sys.platform.startswith("win"), reason="DAQmxSetAnalogPowerUpStates is Windows-only"
)
def test_invalid_power_up_states___set_analog_power_up_states___throws_invalid_attribute_value_error(
    system,
):
    device_name = "aoTester"
    power_up_states = [
        AOPowerUpState(
            physical_channel="aoTester/ao0",
            power_up_state=1,
            channel_type=PowerUpChannelType.CHANNEL_VOLTAGE,
        ),
        AOPowerUpState(
            physical_channel="aoTester/ao1",
            power_up_state=20,
            channel_type=PowerUpChannelType.CHANNEL_VOLTAGE,
        ),
    ]

    with pytest.deprecated_call():
        with pytest.raises(nidaqmx.DaqError) as exc_info:
            system.set_analog_power_up_states(device_name, power_up_states)

    assert exc_info.value.error_code == DAQmxErrors.INVALID_ATTRIBUTE_VALUE


def test___system___set_nonexistent_property___raises_exception(system: System):
    with pytest.raises(AttributeError):
        system.nonexistent_property = "foo"  # type: ignore[attr-defined]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/system/test_watchdog_properties.py sha256=33ed31ce637c36bc1ace165ab9b0376a809637ceaa59de12c1c9ab80ccfe7263 bytes=6679 -->
## FILE: tests/component/system/test_watchdog_properties.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/system/test_watchdog_properties.py`
- sha256: `33ed31ce637c36bc1ace165ab9b0376a809637ceaa59de12c1c9ab80ccfe7263`
- bytes: 6679

````python
import pytest

from nidaqmx.constants import Edge, Level
from nidaqmx.errors import DaqError, DAQmxErrors
from nidaqmx.system.watchdog import DOExpirationState


def test___watchdog_task___get_expired___returns_false(watchdog_task):
    watchdog_task.start()

    assert not watchdog_task.expired


@pytest.mark.device_name("cdaqChassisTester")
def test___watchdog_task___set_boolean_property___returns_assigned_value(watchdog_task):
    watchdog_task.expir_trig_trig_on_network_conn_loss = True

    assert watchdog_task.expir_trig_trig_on_network_conn_loss


@pytest.mark.device_name("cdaqChassisTester")
def test___watchdog_task___reset_boolean_property___returns_default_value(watchdog_task):
    watchdog_task.expir_trig_trig_on_network_conn_loss = True

    del watchdog_task.expir_trig_trig_on_network_conn_loss

    assert not watchdog_task.expir_trig_trig_on_network_conn_loss


def test___watchdog_task___task_not_running_get_expired_property____throws_daqerror(watchdog_task):
    with pytest.raises(DaqError) as exc_info:
        _ = watchdog_task.expired

    assert (
        exc_info.value.error_type
        == DAQmxErrors.CANNOT_GET_PROPERTY_WHEN_TASK_NOT_RESERVED_COMMITTED_OR_RUNNING
    )


def test___watchdog_task___get_enum_property___returns_value(sim_6363_device, watchdog_task):
    do_line = sim_6363_device.do_lines[0]
    expir_states = [
        DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
    ]
    watchdog_task.cfg_watchdog_do_expir_states(expir_states)

    assert watchdog_task.expir_trig_dig_edge_edge == Edge.RISING


def test___watchdog_task___set_enum_property___returns_assigned_value(
    sim_6363_device, watchdog_task
):
    do_line = sim_6363_device.do_lines[0]
    expir_states = [
        DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
    ]
    watchdog_task.cfg_watchdog_do_expir_states(expir_states)

    watchdog_task.expir_trig_dig_edge_edge = Edge.FALLING

    assert watchdog_task.expir_trig_dig_edge_edge == Edge.FALLING


def test___watchdog_task___reset_enum_property___returns_default_value(
    sim_6363_device, watchdog_task
):
    do_line = sim_6363_device.do_lines[0]
    expir_states = [
        DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
    ]
    watchdog_task.cfg_watchdog_do_expir_states(expir_states)
    watchdog_task.expir_trig_dig_edge_edge = Edge.FALLING

    del watchdog_task.expir_trig_dig_edge_edge

    assert watchdog_task.expir_trig_dig_edge_edge == Edge.RISING


def test___watchdog_task___get_float64_property___returns_value(sim_6363_device, watchdog_task):
    do_line = sim_6363_device.do_lines[0]
    expir_states = [
        DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
    ]
    watchdog_task.cfg_watchdog_do_expir_states(expir_states)

    assert watchdog_task.timeout == 0.5


def test___watchdog_task___set_float64_property___returns_assigned_value(
    sim_6363_device, watchdog_task
):
    do_line = sim_6363_device.do_lines[0]
    expir_states = [
        DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
    ]
    watchdog_task.cfg_watchdog_do_expir_states(expir_states)

    watchdog_task.timeout = 2

    assert watchdog_task.timeout == 2


def test___watchdog_task___reset_float64_property___returns_default_value(
    sim_6363_device, watchdog_task
):
    do_line = sim_6363_device.do_lines[0]
    expir_states = [
        DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
    ]
    watchdog_task.cfg_watchdog_do_expir_states(expir_states)

    del watchdog_task.timeout

    assert watchdog_task.timeout == 10


def test___watchdog_task___get_string_property___returns_value(sim_6363_device, watchdog_task):
    do_line = sim_6363_device.do_lines[0]
    expir_states = [
        DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
    ]
    watchdog_task.cfg_watchdog_do_expir_states(expir_states)

    assert watchdog_task.expir_trig_dig_edge_src == ""


def test___watchdog_task___set_string_property___returns_assigned_value(
    sim_6363_device, watchdog_task
):
    do_line = sim_6363_device.do_lines[0]
    expir_states = [
        DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
    ]
    watchdog_task.cfg_watchdog_do_expir_states(expir_states)

    watchdog_task.expir_trig_dig_edge_src = "PFI0"

    assert watchdog_task.expir_trig_dig_edge_src == "PFI0"


def test___watchdog_task___reset_string_property___returns_default_value(
    sim_6363_device, watchdog_task
):
    do_line = sim_6363_device.do_lines[0]
    expir_states = [
        DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
    ]
    watchdog_task.cfg_watchdog_do_expir_states(expir_states)
    watchdog_task.expir_trig_dig_edge_src = "PFI0"

    del watchdog_task.expir_trig_dig_edge_src

    assert watchdog_task.expir_trig_dig_edge_src == ""


def test___watchdog_task___get_deprecated_properties___reports_warnings(
    sim_6363_device, watchdog_task
):
    do_line = sim_6363_device.do_lines[0]
    expir_states = [
        DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
    ]
    watchdog_task.cfg_watchdog_do_expir_states(expir_states)

    with pytest.deprecated_call():
        assert (
            watchdog_task.expiration_states[do_line.name].do_state
            == watchdog_task.expiration_states[do_line.name].expir_states_do_state
        )


def test___watchdog_task___set_deprecated_properties___reports_warnings(
    sim_6363_device, watchdog_task
):
    do_line = sim_6363_device.do_lines[0]
    expir_states = [
        DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
    ]
    watchdog_task.cfg_watchdog_do_expir_states(expir_states)

    with pytest.deprecated_call():
        watchdog_task.expiration_states[do_line.name].expir_states_do_state = Level.HIGH


def test___watchdog_task___reset_deprecated_properties___reports_warnings(
    sim_6363_device, watchdog_task
):
    do_line = sim_6363_device.do_lines[0]
    expir_states = [
        DOExpirationState(physical_channel=do_line.name, expiration_state=Level.TRISTATE)
    ]
    watchdog_task.cfg_watchdog_do_expir_states(expir_states)

    with pytest.deprecated_call():
        del watchdog_task.expiration_states[do_line.name].expir_states_do_state
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/task/__init__.py sha256=73c065d4b913d4ac8f759984bb3dff25f5cc6f31658ff57505d55635bea22ad3 bytes=43 -->
## FILE: tests/component/task/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/task/__init__.py`
- sha256: `73c065d4b913d4ac8f759984bb3dff25f5cc6f31658ff57505d55635bea22ad3`
- bytes: 43

````python
"""Component tests for nidaqmx.task.*."""
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/task/channels/__init__.py sha256=8414a3948bb808a694474c533d5b296e87c20acc6a243fdfa8703f7150e8ee6b bytes=52 -->
## FILE: tests/component/task/channels/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/task/channels/__init__.py`
- sha256: `8414a3948bb808a694474c533d5b296e87c20acc6a243fdfa8703f7150e8ee6b`
- bytes: 52

````python
"""Component tests for nidaqmx.task.channels.*."""
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/task/channels/test_ai_channel.py sha256=024f16622b59d27dd01af3ab899d3c9279b76dd8148daf0393ea4451b1d6c442 bytes=49958 -->
## FILE: tests/component/task/channels/test_ai_channel.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/task/channels/test_ai_channel.py`
- sha256: `024f16622b59d27dd01af3ab899d3c9279b76dd8148daf0393ea4451b1d6c442`
- bytes: 49958

````python
from __future__ import annotations

import pathlib

import pytest

from nidaqmx import Task
from nidaqmx.constants import (
    AccelChargeSensitivityUnits,
    AccelSensitivityUnits,
    AccelUnits,
    ACExcitWireMode,
    BridgeConfiguration,
    BridgeUnits,
    ChargeUnits,
    CJCSource,
    CurrentShuntResistorLocation,
    CurrentUnits,
    EddyCurrentProxProbeSensitivityUnits,
    ExcitationSource,
    ForceIEPESensorSensitivityUnits,
    ForceUnits,
    LVDTSensitivityUnits,
    PowerUnits,
    ResistanceConfiguration,
    RTDType,
    StrainGageBridgeType,
    StrainGageRosetteMeasurementType,
    StrainGageRosetteType,
    TemperatureUnits,
    TerminalConfiguration,
    ThermocoupleType,
    UsageTypeAI,
    VoltageUnits,
)
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError
from nidaqmx.system import Device, System
from nidaqmx.task.channels import AIChannel
from nidaqmx.utils import unflatten_channel_string
from tests.helpers import configure_teds


# Note: Tests for other channel types will be less complete given that the underlying Python
# implementation is code-generated and the underlying C API implementation is well unit-tested.
@pytest.mark.parametrize(
    "desired_term_config, expected_term_cfg",
    [
        (TerminalConfiguration.DEFAULT, TerminalConfiguration.DIFF),
        (TerminalConfiguration.DIFF, TerminalConfiguration.DIFF),
        (TerminalConfiguration.RSE, TerminalConfiguration.RSE),
    ],
)
@pytest.mark.parametrize("min_val, max_val", [(-10, 10), (-5, 5)])
@pytest.mark.parametrize(
    "units, custom_scale_name",
    [(VoltageUnits.VOLTS, ""), (VoltageUnits.FROM_CUSTOM_SCALE, "no_scaling_scale")],
)
def test___task___add_ai_voltage_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    desired_term_config: TerminalConfiguration,
    expected_term_cfg: TerminalConfiguration,
    min_val: float,
    max_val: float,
    units: VoltageUnits,
    custom_scale_name: str,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_voltage_chan(
        sim_6363_device.ai_physical_chans[0].name,
        terminal_config=desired_term_config,
        min_val=min_val,
        max_val=max_val,
        units=units,
        custom_scale_name=custom_scale_name,
    )

    assert chan.ai_meas_type == UsageTypeAI.VOLTAGE
    assert chan.ai_term_cfg == expected_term_cfg
    assert chan.ai_min == min_val
    assert chan.ai_max == max_val
    assert chan.ai_voltage_units == units
    assert chan.ai_custom_scale.name == custom_scale_name


def test___task___add_teds_ai_voltage_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    voltage_teds_file_path: pathlib.Path,
) -> None:
    with configure_teds(sim_6363_device.ai_physical_chans[0], voltage_teds_file_path) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_voltage_chan(
            phys_chan.name,
        )

        assert chan.ai_meas_type == UsageTypeAI.VOLTAGE
        assert chan.ai_teds_is_teds
        # units come from TEDS file
        assert chan.ai_voltage_units == VoltageUnits.FROM_TEDS
        assert chan.ai_teds_units == "Kelvin"


@pytest.mark.parametrize(
    "units, sensitivity, sensitivity_units",
    [
        (AccelUnits.G, 1000.0, AccelSensitivityUnits.MILLIVOLTS_PER_G),
        (AccelUnits.METERS_PER_SECOND_SQUARED, 0.5, AccelSensitivityUnits.VOLTS_PER_G),
    ],
)
def test___task___add_ai_accel_4_wire_dc_voltage_chan___sets_channel_attributes(
    task: Task,
    sim_charge_device: Device,
    units: AccelUnits,
    sensitivity: float,
    sensitivity_units: AccelSensitivityUnits,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_accel_4_wire_dc_voltage_chan(
        sim_charge_device.ai_physical_chans[0].name,
        units=units,
        sensitivity=sensitivity,
        sensitivity_units=sensitivity_units,
    )

    assert chan.ai_meas_type == UsageTypeAI.ACCELERATION_4_WIRE_DC_VOLTAGE
    assert chan.ai_accel_units == units
    assert chan.ai_accel_4_wire_dc_voltage_sensitivity == sensitivity
    assert chan.ai_accel_4_wire_dc_voltage_sensitivity_units == sensitivity_units


@pytest.mark.parametrize(
    "units, sensitivity, sensitivity_units",
    [
        (AccelUnits.G, 1000.0, AccelSensitivityUnits.MILLIVOLTS_PER_G),
        (AccelUnits.METERS_PER_SECOND_SQUARED, 0.5, AccelSensitivityUnits.VOLTS_PER_G),
    ],
)
def test___task___add_ai_accel_chan___sets_channel_attributes(
    task: Task,
    sim_dsa_device: Device,
    units: AccelUnits,
    sensitivity: float,
    sensitivity_units: AccelSensitivityUnits,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_accel_chan(
        sim_dsa_device.ai_physical_chans[0].name,
        units=units,
        sensitivity=sensitivity,
        sensitivity_units=sensitivity_units,
    )

    assert chan.ai_meas_type == UsageTypeAI.ACCELERATION_ACCELEROMETER_CURRENT_INPUT
    assert chan.ai_accel_units == units
    assert chan.ai_accel_sensitivity == sensitivity
    assert chan.ai_accel_sensitivity_units == sensitivity_units


@pytest.mark.parametrize(
    "units",
    [
        AccelUnits.G,
        AccelUnits.METERS_PER_SECOND_SQUARED,
    ],
)
def test___task___add_teds_ai_accel_chan___sets_channel_attributes(
    task: Task,
    sim_dsa_device: Device,
    accelerometer_teds_file_path: pathlib.Path,
    units: AccelUnits,
) -> None:
    with configure_teds(
        sim_dsa_device.ai_physical_chans[0], accelerometer_teds_file_path
    ) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_accel_chan(
            phys_chan.name, min_val=-800e-3, max_val=800e-3, units=units
        )

        assert chan.ai_meas_type == UsageTypeAI.ACCELERATION_ACCELEROMETER_CURRENT_INPUT
        assert chan.ai_teds_is_teds
        assert chan.ai_accel_units == units
        # sensitivity and sensitivity units came from the TEDS file
        assert chan.ai_accel_sensitivity == pytest.approx(49.03, abs=0.01)
        assert chan.ai_accel_sensitivity_units == AccelSensitivityUnits.VOLTS_PER_G


@pytest.mark.parametrize(
    "units, sensitivity, sensitivity_units",
    [
        (AccelUnits.G, 100.0, AccelChargeSensitivityUnits.PICO_COULOMBS_PER_G),
        (
            AccelUnits.METERS_PER_SECOND_SQUARED,
            0.5,
            AccelChargeSensitivityUnits.PICO_COULOMBS_PER_METERS_PER_SECOND_SQUARED,
        ),
    ],
)
def test___task___add_ai_accel_charge_chan___sets_channel_attributes(
    task: Task,
    sim_charge_device: Device,
    units: AccelUnits,
    sensitivity: float,
    sensitivity_units: AccelChargeSensitivityUnits,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_accel_charge_chan(
        sim_charge_device.ai_physical_chans[0].name,
        units=units,
        sensitivity=sensitivity,
        sensitivity_units=sensitivity_units,
    )

    assert chan.ai_meas_type == UsageTypeAI.ACCELERATION_CHARGE
    assert chan.ai_accel_units == units
    assert chan.ai_accel_charge_sensitivity == sensitivity
    assert chan.ai_accel_charge_sensitivity_units == sensitivity_units


@pytest.mark.parametrize(
    "units, bridge_config, nominal_bridge_resistance",
    [
        (BridgeUnits.VOLTS_PER_VOLT, BridgeConfiguration.FULL_BRIDGE, 350.0),
        (BridgeUnits.MILLIVOLTS_PER_VOLT, BridgeConfiguration.QUARTER_BRIDGE, 120.0),
    ],
)
def test___task___add_ai_bridge_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
    units: BridgeUnits,
    bridge_config: BridgeConfiguration,
    nominal_bridge_resistance: float,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_bridge_chan(
        sim_bridge_device.ai_physical_chans[0].name,
        units=units,
        bridge_config=bridge_config,
        nominal_bridge_resistance=nominal_bridge_resistance,
    )

    assert chan.ai_meas_type == UsageTypeAI.BRIDGE
    assert chan.ai_bridge_units == units
    assert chan.ai_bridge_cfg == bridge_config
    assert chan.ai_bridge_nom_resistance == nominal_bridge_resistance


@pytest.mark.parametrize(
    "voltage_excit_val",
    [
        2.5,
        2.75,
    ],
)
def test___task___add_teds_ai_bridge_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
    bridge_teds_file_path: pathlib.Path,
    voltage_excit_val: float,
) -> None:
    with configure_teds(sim_bridge_device.ai_physical_chans[0], bridge_teds_file_path) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_bridge_chan(
            phys_chan.name, voltage_excit_val=voltage_excit_val
        )

        assert chan.ai_meas_type == UsageTypeAI.BRIDGE
        assert chan.ai_teds_is_teds
        assert chan.ai_excit_val == voltage_excit_val
        # units, bridge cfg, and nominal resistance come from the TEDS file
        assert chan.ai_bridge_units == BridgeUnits.FROM_TEDS
        assert chan.ai_teds_units == "forcelb"
        assert chan.ai_bridge_cfg == BridgeConfiguration.FULL_BRIDGE
        assert chan.ai_bridge_nom_resistance == 350.0


@pytest.mark.parametrize("units", [ChargeUnits.COULOMBS, ChargeUnits.PICO_COULOMBS])
def test___task___add_ai_charge_chan___sets_channel_attributes(
    task: Task,
    sim_charge_device: Device,
    units: ChargeUnits,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_charge_chan(
        sim_charge_device.ai_physical_chans[0].name, units=units
    )

    assert chan.ai_meas_type == UsageTypeAI.CHARGE
    assert chan.ai_charge_units == units


@pytest.mark.parametrize(
    "shunt_resistor_loc, expected_shunt_resistor_loc, ext_shunt_resistor_val",
    [
        (
            CurrentShuntResistorLocation.LET_DRIVER_CHOOSE,
            CurrentShuntResistorLocation.EXTERNAL,
            249.0,
        ),
        (CurrentShuntResistorLocation.EXTERNAL, CurrentShuntResistorLocation.EXTERNAL, 99.0),
    ],
)
def test___task___add_ai_current_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    shunt_resistor_loc: CurrentShuntResistorLocation,
    expected_shunt_resistor_loc: CurrentShuntResistorLocation,
    ext_shunt_resistor_val: float,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_current_chan(
        sim_6363_device.ai_physical_chans[0].name,
        shunt_resistor_loc=shunt_resistor_loc,
        ext_shunt_resistor_val=ext_shunt_resistor_val,
    )

    assert chan.ai_meas_type == UsageTypeAI.CURRENT
    assert chan.ai_current_shunt_loc == expected_shunt_resistor_loc
    assert chan.ai_current_shunt_resistance == ext_shunt_resistor_val


@pytest.mark.parametrize(
    "shunt_resistor_loc, expected_shunt_resistor_loc, ext_shunt_resistor_val",
    [
        (
            CurrentShuntResistorLocation.LET_DRIVER_CHOOSE,
            CurrentShuntResistorLocation.EXTERNAL,
            249.0,
        ),
        (CurrentShuntResistorLocation.EXTERNAL, CurrentShuntResistorLocation.EXTERNAL, 99.0),
    ],
)
def test___task___add_teds_ai_current_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    current_teds_file_path: pathlib.Path,
    shunt_resistor_loc: CurrentShuntResistorLocation,
    expected_shunt_resistor_loc: CurrentShuntResistorLocation,
    ext_shunt_resistor_val: float,
) -> None:
    with configure_teds(sim_6363_device.ai_physical_chans[0], current_teds_file_path) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_current_chan(
            phys_chan.name,
            shunt_resistor_loc=shunt_resistor_loc,
            ext_shunt_resistor_val=ext_shunt_resistor_val,
        )

        assert chan.ai_meas_type == UsageTypeAI.CURRENT
        assert chan.ai_teds_is_teds
        assert chan.ai_current_shunt_loc == expected_shunt_resistor_loc
        assert chan.ai_current_shunt_resistance == ext_shunt_resistor_val
        # units comes from TEDS file
        assert chan.ai_current_units == CurrentUnits.FROM_TEDS
        assert chan.ai_teds_units == "Kelvin"


@pytest.mark.parametrize(
    "shunt_resistor_loc, expected_shunt_resistor_loc",
    [
        (CurrentShuntResistorLocation.LET_DRIVER_CHOOSE, CurrentShuntResistorLocation.INTERNAL),
        (CurrentShuntResistorLocation.INTERNAL, CurrentShuntResistorLocation.INTERNAL),
    ],
)
def test___task___add_ai_current_rms_chan___sets_channel_attributes(
    task: Task,
    sim_dmm_device: Device,
    shunt_resistor_loc: CurrentShuntResistorLocation,
    expected_shunt_resistor_loc: CurrentShuntResistorLocation,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_current_rms_chan(
        f"{sim_dmm_device.name}/dmm",
        # dmm is unipolar, defaults don't work
        min_val=0.0,
        max_val=1.0,
        shunt_resistor_loc=shunt_resistor_loc,
    )

    assert chan.ai_meas_type == UsageTypeAI.CURRENT_ACRMS
    assert chan.ai_current_shunt_loc == expected_shunt_resistor_loc


@pytest.mark.parametrize(
    "bridge_config, nominal_bridge_resistance, forward_coeffs, reverse_coeffs",
    [
        (BridgeConfiguration.FULL_BRIDGE, 350.0, [0.0, 1.0], [0.0, 1.0]),
        (BridgeConfiguration.QUARTER_BRIDGE, 120.0, [1.0, 2.0], [-0.5, 0.5]),
    ],
)
def test___task___add_ai_force_bridge_polynomial_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
    bridge_config: BridgeConfiguration,
    nominal_bridge_resistance: float,
    forward_coeffs: list[float],
    reverse_coeffs: list[float],
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_force_bridge_polynomial_chan(
        sim_bridge_device.ai_physical_chans[0].name,
        bridge_config=bridge_config,
        nominal_bridge_resistance=nominal_bridge_resistance,
        forward_coeffs=forward_coeffs,
        reverse_coeffs=reverse_coeffs,
    )

    assert chan.ai_meas_type == UsageTypeAI.FORCE_BRIDGE
    assert chan.ai_bridge_cfg == bridge_config
    assert chan.ai_bridge_nom_resistance == nominal_bridge_resistance
    assert chan.ai_bridge_poly_forward_coeff == forward_coeffs
    assert chan.ai_bridge_poly_reverse_coeff == reverse_coeffs


@pytest.mark.parametrize(
    "bridge_config, nominal_bridge_resistance, electrical_vals, physical_vals",
    [
        (BridgeConfiguration.FULL_BRIDGE, 350.0, [-1.0, 0.0, 1.0], [-100.0, 0.0, 100.0]),
        (BridgeConfiguration.QUARTER_BRIDGE, 120.0, [-2.0, 0.0, 2.0], [-200.0, 0.0, 200.0]),
    ],
)
def test___task___add_ai_force_bridge_table_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
    bridge_config: BridgeConfiguration,
    nominal_bridge_resistance: float,
    electrical_vals: list[float],
    physical_vals: list[float],
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_force_bridge_table_chan(
        sim_bridge_device.ai_physical_chans[0].name,
        bridge_config=bridge_config,
        nominal_bridge_resistance=nominal_bridge_resistance,
        electrical_vals=electrical_vals,
        physical_vals=physical_vals,
    )

    assert chan.ai_meas_type == UsageTypeAI.FORCE_BRIDGE
    assert chan.ai_bridge_cfg == bridge_config
    assert chan.ai_bridge_nom_resistance == nominal_bridge_resistance
    assert chan.ai_bridge_table_electrical_vals == electrical_vals
    assert chan.ai_bridge_table_physical_vals == physical_vals


@pytest.mark.parametrize(
    "bridge_config, nominal_bridge_resistance, first_electrical_val, second_electrical_val, first_physical_val, second_physical_val",
    [
        (BridgeConfiguration.FULL_BRIDGE, 350.0, 0.0, 2.0, 0.0, 100.0),
        (BridgeConfiguration.QUARTER_BRIDGE, 120.0, 0.0, 4.0, 0.0, 200.0),
    ],
)
def test___task___add_ai_force_bridge_two_point_lin_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
    bridge_config: BridgeConfiguration,
    nominal_bridge_resistance: float,
    first_electrical_val: float,
    second_electrical_val: float,
    first_physical_val: float,
    second_physical_val: float,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_force_bridge_two_point_lin_chan(
        sim_bridge_device.ai_physical_chans[0].name,
        bridge_config=bridge_config,
        nominal_bridge_resistance=nominal_bridge_resistance,
        first_electrical_val=first_electrical_val,
        second_electrical_val=second_electrical_val,
        first_physical_val=first_physical_val,
        second_physical_val=second_physical_val,
    )

    assert chan.ai_meas_type == UsageTypeAI.FORCE_BRIDGE
    assert chan.ai_bridge_cfg == bridge_config
    assert chan.ai_bridge_nom_resistance == nominal_bridge_resistance
    assert chan.ai_bridge_two_point_lin_first_electrical_val == first_electrical_val
    assert chan.ai_bridge_two_point_lin_second_electrical_val == second_electrical_val
    assert chan.ai_bridge_two_point_lin_first_physical_val == first_physical_val
    assert chan.ai_bridge_two_point_lin_second_physical_val == second_physical_val


def test___task___add_teds_ai_force_bridge_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
    force_bridge_teds_file_path: pathlib.Path,
) -> None:
    with configure_teds(
        sim_bridge_device.ai_physical_chans[0], force_bridge_teds_file_path
    ) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_force_bridge_chan(
            phys_chan.name, min_val=-5.0, max_val=5.0
        )

        assert chan.ai_meas_type == UsageTypeAI.FORCE_BRIDGE
        assert chan.ai_teds_is_teds
        # bridge cfg and nominal resistance come from the TEDS file
        assert chan.ai_bridge_cfg == BridgeConfiguration.FULL_BRIDGE
        assert chan.ai_bridge_nom_resistance == 350.0


@pytest.mark.parametrize(
    "units, sensitivity, sensitivity_units",
    [
        (ForceUnits.NEWTONS, 2.25, ForceIEPESensorSensitivityUnits.MILLIVOLTS_PER_NEWTON),
        (ForceUnits.POUNDS, 1.25, ForceIEPESensorSensitivityUnits.MILLIVOLTS_PER_POUND),
    ],
)
def test___task___add_ai_force_iepe_chan___sets_channel_attributes(
    task: Task,
    sim_dsa_device: Device,
    units: ForceUnits,
    sensitivity: float,
    sensitivity_units: ForceIEPESensorSensitivityUnits,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_force_iepe_chan(
        sim_dsa_device.ai_physical_chans[0].name,
        units=units,
        sensitivity=sensitivity,
        sensitivity_units=sensitivity_units,
    )

    assert chan.ai_meas_type == UsageTypeAI.FORCE_IEPE_SENSOR
    assert chan.ai_force_units == units
    assert chan.ai_force_iepe_sensor_sensitivity == sensitivity
    assert chan.ai_force_iepe_sensor_sensitivity_units == sensitivity_units


@pytest.mark.parametrize(
    "units",
    [
        ForceUnits.NEWTONS,
        ForceUnits.POUNDS,
    ],
)
def test___task___add_teds_ai_force_iepe_chan___sets_channel_attributes(
    task: Task,
    sim_dsa_device: Device,
    force_iepe_teds_file_path: pathlib.Path,
    units: ForceUnits,
) -> None:
    with configure_teds(
        sim_dsa_device.ai_physical_chans[0], force_iepe_teds_file_path
    ) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_force_iepe_chan(
            phys_chan.name,
            units=units,
        )

        assert chan.ai_meas_type == UsageTypeAI.FORCE_IEPE_SENSOR
        assert chan.ai_teds_is_teds
        assert chan.ai_force_units == units
        # Sensitivity and sensitivity units come from the TEDS file
        assert chan.ai_force_iepe_sensor_sensitivity == pytest.approx(3.25, abs=0.01)
        assert (
            chan.ai_force_iepe_sensor_sensitivity_units
            == ForceIEPESensorSensitivityUnits.MILLIVOLTS_PER_NEWTON
        )


# No active DAQmx devices support add_ai_freq_voltage_chan


@pytest.mark.parametrize(
    "mic_sensitivity, max_snd_press_level",
    [
        (5.0, 50.0),
        (10.0, 100.0),
    ],
)
def test___task___add_ai_microphone_chan___sets_channel_attributes(
    task: Task,
    sim_dsa_device: Device,
    mic_sensitivity: float,
    max_snd_press_level: float,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_microphone_chan(
        sim_dsa_device.ai_physical_chans[0].name,
        mic_sensitivity=mic_sensitivity,
        max_snd_press_level=max_snd_press_level,
    )

    assert chan.ai_meas_type == UsageTypeAI.SOUND_PRESSURE_MICROPHONE
    assert chan.ai_microphone_sensitivity == mic_sensitivity
    assert chan.ai_sound_pressure_max_sound_pressure_lvl == max_snd_press_level


@pytest.mark.parametrize(
    "max_snd_press_level",
    [
        50.0,
        100.0,
    ],
)
def test___task___add_teds_ai_microphone_chan___sets_channel_attributes(
    task: Task,
    sim_dsa_device: Device,
    microphone_teds_file_path: pathlib.Path,
    max_snd_press_level: float,
) -> None:
    with configure_teds(
        sim_dsa_device.ai_physical_chans[0], microphone_teds_file_path
    ) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_microphone_chan(
            phys_chan.name,
            max_snd_press_level=max_snd_press_level,
        )

        assert chan.ai_meas_type == UsageTypeAI.SOUND_PRESSURE_MICROPHONE
        assert chan.ai_teds_is_teds
        assert chan.ai_sound_pressure_max_sound_pressure_lvl == max_snd_press_level
        # mic sensitivity comes from the TEDS file
        assert chan.ai_microphone_sensitivity == pytest.approx(1999.81, abs=0.01)


@pytest.mark.parametrize(
    "sensitivity_units, sensitivity",
    [
        (EddyCurrentProxProbeSensitivityUnits.MILLIVOLTS_PER_MIL, 200.0),
        (EddyCurrentProxProbeSensitivityUnits.VOLTS_PER_MIL, 0.2),
    ],
)
def test___task___add_ai_pos_eddy_curr_prox_probe_chan___sets_channel_attributes(
    task: Task,
    sim_dsa_device: Device,
    sensitivity_units: EddyCurrentProxProbeSensitivityUnits,
    sensitivity: float,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_pos_eddy_curr_prox_probe_chan(
        sim_dsa_device.ai_physical_chans[0].name,
        sensitivity_units=sensitivity_units,
        sensitivity=sensitivity,
    )

    assert chan.ai_meas_type == UsageTypeAI.POSITION_EDDY_CURRENT_PROX_PROBE
    assert chan.ai_eddy_current_prox_sensitivity_units == sensitivity_units
    assert chan.ai_eddy_current_prox_sensitivity == sensitivity


@pytest.mark.parametrize(
    "sensitivity_units, sensitivity, ac_excit_wire_mode, voltage_excit_val, voltage_excit_freq",
    [
        (
            LVDTSensitivityUnits.MILLIVOLTS_PER_VOLT_PER_MILLIMETER,
            50.0,
            ACExcitWireMode.FOUR_WIRE,
            1.0,
            2500.0,
        ),
        (
            LVDTSensitivityUnits.MILLIVOLTS_PER_VOLT_PER_MILLI_INCH,
            0.5,
            ACExcitWireMode.FIVE_WIRE,
            1.5,
            2000.0,
        ),
    ],
)
def test___task___add_ai_pos_lvdt_chan___sets_channel_attributes(
    task: Task,
    sim_position_device: Device,
    sensitivity_units: LVDTSensitivityUnits,
    sensitivity: float,
    ac_excit_wire_mode: ACExcitWireMode,
    voltage_excit_val: float,
    voltage_excit_freq: float,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_pos_lvdt_chan(
        sim_position_device.ai_physical_chans[0].name,
        sensitivity_units=sensitivity_units,
        sensitivity=sensitivity,
        ac_excit_wire_mode=ac_excit_wire_mode,
        voltage_excit_val=voltage_excit_val,
        voltage_excit_freq=voltage_excit_freq,
    )

    assert chan.ai_meas_type == UsageTypeAI.POSITION_LINEAR_LVDT
    assert chan.ai_lvdt_sensitivity_units == sensitivity_units
    assert chan.ai_lvdt_sensitivity == sensitivity
    assert chan.ai_ac_excit_wire_mode == ac_excit_wire_mode
    assert chan.ai_excit_val == voltage_excit_val
    assert chan.ai_ac_excit_freq == voltage_excit_freq


def test___task___add_teds_ai_pos_lvdt_chan___sets_channel_attributes(
    task: Task,
    sim_position_device: Device,
) -> None:
    # A bug in the driver prevents us from testing the full functionality of this method.
    # AB#2647979: Devices that don't support Voltage, Custom Voltage with Excitation, Resistance, or
    # RTD inadvertently don't support TEDS (e.g. PXIe-4340)
    with pytest.raises(DaqError) as exc_info:
        task.ai_channels.add_teds_ai_pos_lvdt_chan(
            sim_position_device.ai_physical_chans[0].name,
        )

    assert exc_info.value.error_type == DAQmxErrors.TEDS_SENSOR_NOT_DETECTED


# Nothing novel here vs. lvdt channels.
def test___task___add_ai_pos_rvdt_chan___sets_channel_attributes(
    task: Task,
    sim_position_device: Device,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_pos_rvdt_chan(
        sim_position_device.ai_physical_chans[0].name
    )

    assert chan.ai_meas_type == UsageTypeAI.POSITION_ANGULAR_RVDT


def test___task___add_teds_ai_pos_rvdt_chan___sets_channel_attributes(
    task: Task,
    sim_position_device: Device,
) -> None:
    # A bug in the driver prevents us from testing the full functionality of this method.
    # AB#2647979: Devices that don't support Voltage, Custom Voltage with Excitation, Resistance, or
    # RTD inadvertently don't support TEDS (e.g. PXIe-4340)
    with pytest.raises(DaqError) as exc_info:
        task.ai_channels.add_teds_ai_pos_rvdt_chan(
            sim_position_device.ai_physical_chans[0].name,
        )

    assert exc_info.value.error_type == DAQmxErrors.TEDS_SENSOR_NOT_DETECTED


@pytest.mark.parametrize(
    "voltage_setpoint, current_setpoint, output_enable",
    [
        (0.0, 0.5, False),
        (2.5, 1.0, True),
    ],
)
def test___task___add_ai_power_chan___sets_channel_attributes(
    task: Task,
    sim_ts_power_device: Device,
    voltage_setpoint: float,
    current_setpoint: float,
    output_enable: bool,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_power_chan(
        f"{sim_ts_power_device.name}/power",
        voltage_setpoint=voltage_setpoint,
        current_setpoint=current_setpoint,
        output_enable=output_enable,
    )

    assert chan.ai_meas_type == UsageTypeAI.POWER
    assert chan.pwr_voltage_setpoint == voltage_setpoint
    assert chan.pwr_current_setpoint == current_setpoint
    assert chan.pwr_output_enable == output_enable


# Nothing novel here vs. other bridge-based channels.
def test___task___add_ai_pressure_bridge_polynomial_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_pressure_bridge_polynomial_chan(
        sim_bridge_device.ai_physical_chans[0].name,
    )

    assert chan.ai_meas_type == UsageTypeAI.PRESSURE_BRIDGE
    assert chan.ai_bridge_poly_forward_coeff == [0.0, 50]
    assert chan.ai_bridge_poly_reverse_coeff == [0.0, 0.02]


# Nothing novel here vs. other bridge-based channels.
def test___task___add_ai_pressure_bridge_table_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_pressure_bridge_table_chan(
        sim_bridge_device.ai_physical_chans[0].name,
    )

    assert chan.ai_meas_type == UsageTypeAI.PRESSURE_BRIDGE
    assert chan.ai_bridge_table_electrical_vals == [-2.0, 0.0, 2.0]
    assert chan.ai_bridge_table_physical_vals == [-100.0, 0.0, 100.0]


# Nothing novel here vs. other bridge-based channels.
def test___task___add_ai_pressure_bridge_two_point_lin_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_pressure_bridge_two_point_lin_chan(
        sim_bridge_device.ai_physical_chans[0].name
    )

    assert chan.ai_meas_type == UsageTypeAI.PRESSURE_BRIDGE


def test___task___add_teds_ai_pressure_bridge_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
    pressure_bridge_teds_file_path: pathlib.Path,
) -> None:
    with configure_teds(
        sim_bridge_device.ai_physical_chans[0], pressure_bridge_teds_file_path
    ) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_pressure_bridge_chan(
            phys_chan.name, min_val=-1.25, max_val=1.25
        )

        assert chan.ai_meas_type == UsageTypeAI.PRESSURE_BRIDGE
        assert chan.ai_teds_is_teds
        # bridge cfg and nominal resistance come from the TEDS file
        assert chan.ai_bridge_cfg == BridgeConfiguration.FULL_BRIDGE
        assert chan.ai_bridge_nom_resistance == 350.0


@pytest.mark.parametrize(
    "resistance_config",
    [
        (ResistanceConfiguration.TWO_WIRE),
        (ResistanceConfiguration.THREE_WIRE),
    ],
)
def test___task___add_ai_resistance_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    resistance_config: ResistanceConfiguration,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_resistance_chan(
        sim_6363_device.ai_physical_chans[0].name, resistance_config=resistance_config
    )

    assert chan.ai_meas_type == UsageTypeAI.RESISTANCE
    assert chan.ai_resistance_cfg == resistance_config


@pytest.mark.parametrize(
    "resistance_config",
    [
        (ResistanceConfiguration.TWO_WIRE),
        (ResistanceConfiguration.THREE_WIRE),
    ],
)
def test___task___add_teds_ai_resistance_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    resistance_teds_file_path: pathlib.Path,
    resistance_config: ResistanceConfiguration,
) -> None:
    with configure_teds(
        sim_6363_device.ai_physical_chans[0], resistance_teds_file_path
    ) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_resistance_chan(
            phys_chan.name, resistance_config=resistance_config
        )

        assert chan.ai_meas_type == UsageTypeAI.RESISTANCE
        assert chan.ai_teds_is_teds
        assert chan.ai_resistance_cfg == resistance_config


# Rosette is very complicated, so I'm not parametrizing this test.
def test___task___add_ai_rosette_strain_gage_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
) -> None:
    task.ai_channels.add_ai_rosette_strain_gage_chan(
        ",".join(sim_bridge_device.ai_physical_chans.channel_names[0:2]),
        StrainGageRosetteType.TEE,
        0.0,
        [StrainGageRosetteMeasurementType.PRINCIPAL_STRAIN_1],
    )
    chan: AIChannel = task.ai_channels["rosette0_principalStrain1"]
    assert chan.ai_meas_type == UsageTypeAI.ROSETTE_STRAIN_GAGE


@pytest.mark.parametrize(
    "rtd_type, resistance_config",
    [
        (RTDType.PT_3750, ResistanceConfiguration.TWO_WIRE),
        (RTDType.PT_3851, ResistanceConfiguration.THREE_WIRE),
    ],
)
def test___task___add_ai_rtd_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    rtd_type: RTDType,
    resistance_config: ResistanceConfiguration,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_rtd_chan(
        sim_6363_device.ai_physical_chans[0].name,
        rtd_type=rtd_type,
        resistance_config=resistance_config,
    )

    assert chan.ai_meas_type == UsageTypeAI.TEMPERATURE_RTD
    assert chan.ai_rtd_type == rtd_type
    assert chan.ai_resistance_cfg == resistance_config


@pytest.mark.parametrize(
    "resistance_config",
    [
        ResistanceConfiguration.TWO_WIRE,
        ResistanceConfiguration.THREE_WIRE,
    ],
)
def test___task___add_teds_ai_rtd_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    rtd_teds_file_path: pathlib.Path,
    resistance_config: ResistanceConfiguration,
) -> None:
    with configure_teds(sim_6363_device.ai_physical_chans[0], rtd_teds_file_path) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_rtd_chan(
            phys_chan.name, resistance_config=resistance_config
        )

        assert chan.ai_meas_type == UsageTypeAI.TEMPERATURE_RTD
        assert chan.ai_resistance_cfg == resistance_config
        assert chan.ai_teds_is_teds
        # rtd type and coefficients come from the TEDS file
        assert chan.ai_rtd_type == RTDType.CUSTOM
        assert chan.ai_rtd_a == pytest.approx(3.81e-3, abs=1e-5)
        assert chan.ai_rtd_b == pytest.approx(-6.02e-7, abs=1e-9)
        assert chan.ai_rtd_c == pytest.approx(-6e-12, abs=1e-14)


@pytest.mark.parametrize(
    "strain_config, gage_factor, nominal_gage_resistance",
    [
        (StrainGageBridgeType.FULL_BRIDGE_I, 2.1, 350.0),
        (StrainGageBridgeType.QUARTER_BRIDGE_I, 1.1, 120.0),
    ],
)
def test___task___add_ai_strain_gage_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
    strain_config: StrainGageBridgeType,
    gage_factor: float,
    nominal_gage_resistance: float,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_strain_gage_chan(
        sim_bridge_device.ai_physical_chans[0].name,
        strain_config=strain_config,
        gage_factor=gage_factor,
        nominal_gage_resistance=nominal_gage_resistance,
    )

    assert chan.ai_meas_type == UsageTypeAI.STRAIN_STRAIN_GAGE
    assert chan.ai_strain_gage_cfg == strain_config
    assert chan.ai_strain_gage_gage_factor == gage_factor
    assert chan.ai_bridge_nom_resistance == nominal_gage_resistance


def test___task___add_ai_teds_strain_gage_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
    strain_gage_teds_file_path: pathlib.Path,
) -> None:
    with configure_teds(
        sim_bridge_device.ai_physical_chans[0], strain_gage_teds_file_path
    ) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_strain_gage_chan(
            phys_chan.name,
        )

        assert chan.ai_meas_type == UsageTypeAI.STRAIN_STRAIN_GAGE
        assert chan.ai_teds_is_teds
        # strain config, gage factor, and nominal resistance come from the TEDS file
        assert chan.ai_strain_gage_cfg == StrainGageBridgeType.HALF_BRIDGE_I
        assert chan.ai_strain_gage_gage_factor == pytest.approx(2.01, abs=0.01)
        assert chan.ai_bridge_nom_resistance == pytest.approx(120.0, abs=0.01)


def test___task___add_ai_temp_built_in_sensor_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_temp_built_in_sensor_chan(
        f"{sim_6363_device.name}/_boardTempSensor_vs_aignd"
    )

    assert chan.ai_meas_type == UsageTypeAI.TEMPERATURE_BUILT_IN_SENSOR


@pytest.mark.parametrize(
    "thermocouple_type, cjc_source, cjc_val",
    [
        (ThermocoupleType.J, CJCSource.CONSTANT_USER_VALUE, 25.0),
        (ThermocoupleType.K, CJCSource.BUILT_IN, 0.0),
    ],
)
def test___task___add_ai_thrmcpl_chan___sets_channel_attributes(
    task: Task,
    sim_temperature_device: Device,
    thermocouple_type: ThermocoupleType,
    cjc_source: CJCSource,
    cjc_val: float,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_thrmcpl_chan(
        sim_temperature_device.ai_physical_chans[0].name,
        thermocouple_type=thermocouple_type,
        cjc_source=cjc_source,
        cjc_val=cjc_val,
    )

    assert chan.ai_meas_type == UsageTypeAI.TEMPERATURE_THERMOCOUPLE
    assert chan.ai_thrmcpl_type == thermocouple_type
    assert chan.ai_thrmcpl_cjc_src == cjc_source
    assert chan.ai_thrmcpl_cjc_val == cjc_val


@pytest.mark.parametrize(
    "cjc_source, cjc_val",
    [
        (CJCSource.CONSTANT_USER_VALUE, 25.0),
        (CJCSource.BUILT_IN, 0.0),
    ],
)
def test___task___add_teds_ai_thrmcpl_chan___sets_channel_attributes(
    task: Task,
    sim_temperature_device: Device,
    thermocouple_teds_file_path: pathlib.Path,
    cjc_source: CJCSource,
    cjc_val: float,
) -> None:
    with configure_teds(
        sim_temperature_device.ai_physical_chans[0], thermocouple_teds_file_path
    ) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_thrmcpl_chan(
            phys_chan.name,
            cjc_source=cjc_source,
            cjc_val=cjc_val,
        )

        assert chan.ai_meas_type == UsageTypeAI.TEMPERATURE_THERMOCOUPLE
        assert chan.ai_thrmcpl_cjc_src == cjc_source
        assert chan.ai_thrmcpl_cjc_val == cjc_val
        assert chan.ai_teds_is_teds
        # thermocouple type comes from the TEDS file
        assert chan.ai_thrmcpl_type == ThermocoupleType.K


@pytest.mark.parametrize(
    "resistance_config, a, b, c",
    [
        (ResistanceConfiguration.TWO_WIRE, 0.1, 0.2, 0.3),
        (ResistanceConfiguration.FOUR_WIRE, 0.2, 0.3, 0.4),
    ],
)
def test___task___add_ai_thrmstr_chan_iex___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    resistance_config: ResistanceConfiguration,
    a: float,
    b: float,
    c: float,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_thrmstr_chan_iex(
        sim_6363_device.ai_physical_chans[0].name,
        resistance_config=resistance_config,
        a=a,
        b=b,
        c=c,
    )

    assert chan.ai_meas_type == UsageTypeAI.TEMPERATURE_THERMISTOR
    assert chan.ai_resistance_cfg == resistance_config
    assert chan.ai_thrmstr_a == a
    assert chan.ai_thrmstr_b == b
    assert chan.ai_thrmstr_c == c


@pytest.mark.parametrize(
    "resistance_config",
    [
        ResistanceConfiguration.TWO_WIRE,
        ResistanceConfiguration.FOUR_WIRE,
    ],
)
def test___task___add_teds_ai_thrmstr_chan_iex___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    thermistor_iex_teds_file_path: pathlib.Path,
    resistance_config: ResistanceConfiguration,
) -> None:
    with configure_teds(
        sim_6363_device.ai_physical_chans[0], thermistor_iex_teds_file_path
    ) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_thrmstr_chan_iex(
            phys_chan.name,
            resistance_config=resistance_config,
        )

        assert chan.ai_meas_type == UsageTypeAI.TEMPERATURE_THERMISTOR
        assert chan.ai_teds_is_teds
        assert chan.ai_resistance_cfg == resistance_config
        # a, b, and c come from the TEDS file
        assert chan.ai_thrmstr_a == pytest.approx(1.3e-3, abs=1.0e-5)
        assert chan.ai_thrmstr_b == pytest.approx(2.3e-4, abs=1.0e-6)
        assert chan.ai_thrmstr_c == pytest.approx(1.0e-7, abs=1.0e-9)


@pytest.mark.parametrize(
    "units, resistance_config",
    [
        (TemperatureUnits.DEG_C, ResistanceConfiguration.THREE_WIRE),
        (TemperatureUnits.DEG_F, ResistanceConfiguration.FOUR_WIRE),
    ],
)
def test___task___add_ai_thrmstr_chan_vex___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    units: TemperatureUnits,
    resistance_config: ResistanceConfiguration,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_thrmstr_chan_vex(
        sim_6363_device.ai_physical_chans[0].name, units=units, resistance_config=resistance_config
    )

    assert chan.ai_meas_type == UsageTypeAI.TEMPERATURE_THERMISTOR
    assert chan.ai_temp_units == units
    assert chan.ai_resistance_cfg == resistance_config


@pytest.mark.parametrize(
    "units, resistance_config",
    [
        (TemperatureUnits.DEG_C, ResistanceConfiguration.THREE_WIRE),
        (TemperatureUnits.DEG_F, ResistanceConfiguration.FOUR_WIRE),
    ],
)
def test___task___add_teds_ai_thrmstr_chan_vex___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    thermistor_vex_teds_file_path: pathlib.Path,
    units: TemperatureUnits,
    resistance_config: ResistanceConfiguration,
) -> None:
    with configure_teds(
        sim_6363_device.ai_physical_chans[0], thermistor_vex_teds_file_path
    ) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_thrmstr_chan_vex(
            phys_chan.name,
            units=units,
            resistance_config=resistance_config,
        )

        assert chan.ai_meas_type == UsageTypeAI.TEMPERATURE_THERMISTOR
        assert chan.ai_teds_is_teds
        assert chan.ai_temp_units == units
        assert chan.ai_resistance_cfg == resistance_config
        # a, b, and c come from the TEDS file
        assert chan.ai_thrmstr_a == pytest.approx(1.3e-3, abs=1.0e-5)
        assert chan.ai_thrmstr_b == pytest.approx(2.3e-4, abs=1.0e-6)
        assert chan.ai_thrmstr_c == pytest.approx(1.0e-7, abs=1.0e-9)


# Nothing novel here vs. other bridge-based channels.
def test___task___add_ai_torque_bridge_polynomial_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_torque_bridge_polynomial_chan(
        sim_bridge_device.ai_physical_chans[0].name,
    )

    assert chan.ai_meas_type == UsageTypeAI.TORQUE_BRIDGE
    assert chan.ai_bridge_poly_forward_coeff == [0.0, 50]
    assert chan.ai_bridge_poly_reverse_coeff == [0.0, 0.02]


# Nothing novel here vs. other bridge-based channels.
def test___task___add_ai_torque_bridge_table_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_torque_bridge_table_chan(
        sim_bridge_device.ai_physical_chans[0].name,
    )

    assert chan.ai_meas_type == UsageTypeAI.TORQUE_BRIDGE
    assert chan.ai_bridge_table_electrical_vals == [-2.0, 0.0, 2.0]
    assert chan.ai_bridge_table_physical_vals == [-100.0, 0.0, 100.0]


# Nothing novel here vs. other bridge-based channels.
def test___task___add_ai_torque_bridge_two_point_lin_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_torque_bridge_two_point_lin_chan(
        sim_bridge_device.ai_physical_chans[0].name
    )

    assert chan.ai_meas_type == UsageTypeAI.TORQUE_BRIDGE


def test___task___add_teds_ai_torque_bridge_chan___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
    torque_bridge_teds_file_path: pathlib.Path,
) -> None:
    with configure_teds(
        sim_bridge_device.ai_physical_chans[0], torque_bridge_teds_file_path
    ) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_torque_bridge_chan(
            phys_chan.name, min_val=-44.0, max_val=44.0
        )

        assert chan.ai_meas_type == UsageTypeAI.TORQUE_BRIDGE
        assert chan.ai_teds_is_teds
        # bridge cfg and nominal resistance come from the TEDS file
        assert chan.ai_bridge_cfg == BridgeConfiguration.FULL_BRIDGE
        assert chan.ai_bridge_nom_resistance == 350.0


# Nothing novel here vs. other iepe channels.
def test___task___add_ai_velocity_iepe_chan___sets_channel_attributes(
    task: Task,
    sim_dsa_device: Device,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_velocity_iepe_chan(
        sim_dsa_device.ai_physical_chans[0].name
    )

    assert chan.ai_meas_type == UsageTypeAI.VELOCITY_IEPE_SENSOR


@pytest.mark.parametrize(
    "min_val, max_val, bridge_config, voltage_excit_source, voltage_excit_val, use_excit_for_scaling",
    [
        (-10.0, 10.0, BridgeConfiguration.FULL_BRIDGE, ExcitationSource.EXTERNAL, 5.0, False),
        (-2.0, 2.0, BridgeConfiguration.HALF_BRIDGE, ExcitationSource.EXTERNAL, 5.0, True),
    ],
)
def test___task___add_ai_voltage_chan_with_excit___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    min_val: float,
    max_val: float,
    bridge_config: BridgeConfiguration,
    voltage_excit_source: ExcitationSource,
    voltage_excit_val: float,
    use_excit_for_scaling: bool,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_voltage_chan_with_excit(
        sim_6363_device.ai_physical_chans[0].name,
        min_val=min_val,
        max_val=max_val,
        bridge_config=bridge_config,
        voltage_excit_source=voltage_excit_source,
        voltage_excit_val=voltage_excit_val,
        use_excit_for_scaling=use_excit_for_scaling,
    )

    assert chan.ai_meas_type == UsageTypeAI.VOLTAGE_CUSTOM_WITH_EXCITATION
    assert chan.ai_min == min_val
    assert chan.ai_max == max_val
    assert chan.ai_bridge_cfg == bridge_config
    assert chan.ai_excit_src == voltage_excit_source
    assert chan.ai_excit_val == voltage_excit_val
    assert chan.ai_excit_use_for_scaling == use_excit_for_scaling


def test___task___add_teds_ai_voltage_chan_with_excit___sets_channel_attributes(
    task: Task,
    sim_bridge_device: Device,
    bridge_teds_file_path: pathlib.Path,
) -> None:
    with configure_teds(sim_bridge_device.ai_physical_chans[0], bridge_teds_file_path) as phys_chan:
        chan: AIChannel = task.ai_channels.add_teds_ai_voltage_chan_with_excit(
            phys_chan.name,
            min_val=-1.25,
            max_val=1.25,
            voltage_excit_source=ExcitationSource.INTERNAL,
            voltage_excit_val=5.0,
        )

        assert chan.ai_meas_type == UsageTypeAI.VOLTAGE_CUSTOM_WITH_EXCITATION
        assert chan.ai_teds_is_teds
        assert chan.ai_excit_src == ExcitationSource.INTERNAL
        assert chan.ai_excit_val == 5.0
        # bridge config and use excitation for scaling come from the TEDS file
        assert chan.ai_bridge_cfg == BridgeConfiguration.FULL_BRIDGE
        assert chan.ai_excit_use_for_scaling


def test___task___add_ai_voltage_rms_chan___sets_channel_attributes(
    task: Task,
    sim_dmm_device: Device,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_voltage_rms_chan(
        f"{sim_dmm_device.name}/dmm", min_val=0.0, max_val=1.0
    )

    assert chan.ai_meas_type == UsageTypeAI.VOLTAGE_ACRMS


def test___task___add_teds_ai_voltage_chan_with_excit___raises_teds_sensor_not_detected(
    task: Task,
    sim_bridge_device: Device,
) -> None:
    with pytest.raises(DaqError) as exc_info:
        with configure_teds(sim_bridge_device.ai_physical_chans[0]) as phys_chan:
            _ = task.ai_channels.add_teds_ai_voltage_chan_with_excit(
                phys_chan.name,
                min_val=-1.25,
                max_val=1.25,
                voltage_excit_source=ExcitationSource.INTERNAL,
                voltage_excit_val=5.0,
            )

    assert exc_info.value.error_code == DAQmxErrors.TEDS_SENSOR_NOT_DETECTED


# For more extensive virtual channel name testing, refer to test_di_channel.py
@pytest.mark.skipif(
    System.local().driver_version < (24, 5, 0),
    reason="The fix for this test requires DAQmx 24.5.0 and later",
)
@pytest.mark.grpc_xfail(
    reason="The fix for this test isn't supported on gRPC",
)
def test___task___add_ai_chans_with_name___sets_channel_name(
    task: Task,
    sim_6363_device: Device,
) -> None:
    chan: AIChannel = task.ai_channels.add_ai_voltage_chan(
        f"{sim_6363_device.name}/ai0:3", name_to_assign_to_channel="myChan09"
    )

    assert unflatten_channel_string(chan.name) == unflatten_channel_string("myChan09:12")


@pytest.mark.parametrize(
    "voltage_min_val, voltage_max_val",
    [
        (-0.15, 0.15),
        (0.0, 6.0),
        (0.0, 25.0),
    ],
)
@pytest.mark.parametrize(
    "current_min_val, current_max_val",
    [
        (-0.0015, 0.0015),
        (0.0, 0.06),
        (0.0, 0.25),
    ],
)
@pytest.mark.parametrize(
    "units, custom_scale_name",
    [
        (PowerUnits.WATTS, ""),
        (PowerUnits.FROM_CUSTOM_SCALE, "power_scale"),
    ],
)
@pytest.mark.parametrize(
    "shunt_resistor_loc, expected_shunt_resistor_loc",
    [
        (CurrentShuntResistorLocation.LET_DRIVER_CHOOSE, CurrentShuntResistorLocation.EXTERNAL),
        (CurrentShuntResistorLocation.EXTERNAL, CurrentShuntResistorLocation.EXTERNAL),
    ],
)
def test___task___add_ai_calculated_power_chan___sets_channel_attributes(
    task: Task,
    sim_4311_device: Device,
    voltage_min_val: float,
    voltage_max_val: float,
    current_min_val: float,
    current_max_val: float,
    units: PowerUnits,
    shunt_resistor_loc: CurrentShuntResistorLocation,
    expected_shunt_resistor_loc: CurrentShuntResistorLocation,
    custom_scale_name: str,
) -> None:
    expected_shunt_resistor_value = 100.0
    chan: AIChannel = task.ai_channels.add_ai_calculated_power_chan(
        sim_4311_device.ai_physical_chans[0].name,
        sim_4311_device.ai_physical_chans[1].name,
        voltage_min_val=voltage_min_val,
        voltage_max_val=voltage_max_val,
        current_min_val=current_min_val,
        current_max_val=current_max_val,
        units=units,
        shunt_resistor_loc=shunt_resistor_loc,
        ext_shunt_resistor_val=expected_shunt_resistor_value,
        custom_scale_name=custom_scale_name,
    )

    assert chan.ai_meas_type == UsageTypeAI.CALCULATED_POWER
    assert chan.ai_calculated_power_voltage_min == voltage_min_val
    assert chan.ai_calculated_power_voltage_max == voltage_max_val
    assert chan.ai_calculated_power_current_min == current_min_val
    assert chan.ai_calculated_power_current_max == current_max_val
    assert chan.ai_power_units == units
    assert chan.ai_current_shunt_loc == expected_shunt_resistor_loc
    assert chan.ai_current_shunt_resistance == expected_shunt_resistor_value
    assert chan.ai_custom_scale.name == custom_scale_name
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/task/channels/test_channel_properties.py sha256=8ba97cd64f2481bc0918eec2a2b64ac17826c20acf901850db68d54ec2e79a80 bytes=8430 -->
## FILE: tests/component/task/channels/test_channel_properties.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/task/channels/test_channel_properties.py`
- sha256: `8ba97cd64f2481bc0918eec2a2b64ac17826c20acf901850db68d54ec2e79a80`
- bytes: 8430

````python
import pytest

from nidaqmx import Task
from nidaqmx.constants import (
    ExcitationSource,
    PowerIdleOutputBehavior,
    RTDType,
    VoltageUnits,
)
from nidaqmx.system.storage import PersistedScale
from nidaqmx.task.channels import AIChannel, CIChannel


@pytest.fixture(scope="function")
def ai_voltage_chan_with_excit(task, sim_6363_device):
    """Creates AI Channel object to measure voltage."""
    ai_channel = task.ai_channels.add_ai_voltage_chan_with_excit(
        sim_6363_device.ai_physical_chans[0].name,
        voltage_excit_source=ExcitationSource.EXTERNAL,
        voltage_excit_val=0.1,
    )
    yield ai_channel


@pytest.fixture(scope="function")
def ai_voltage_chan_with_scale(task, sim_6363_device):
    """Creates AI Channel object to measure voltage with a custom scale."""
    ai_channel = task.ai_channels.add_ai_voltage_chan(
        sim_6363_device.ai_physical_chans[0].name,
        units=VoltageUnits.FROM_CUSTOM_SCALE,
        custom_scale_name="double_gain_scale",
    )
    yield ai_channel


@pytest.fixture(scope="function")
def ai_power_chan(task, sim_ts_power_device):
    """Creates AI Channel object to measure power."""
    ai_pwr_channel = task.ai_channels.add_ai_power_chan(
        f"{sim_ts_power_device.name}/power",
        voltage_setpoint=6.0,
        current_setpoint=3.0,
        output_enable=True,
    )
    yield ai_pwr_channel


@pytest.fixture(scope="function")
def ai_rtd_chan(task, sim_6363_device):
    """Creates AI Channel object that use an RTD to measure temperature."""
    ai_channel = task.ai_channels.add_ai_rtd_chan(
        sim_6363_device.ai_physical_chans[0].name,
        rtd_type=RTDType.PT_3750,
    )
    yield ai_channel


@pytest.fixture(scope="function")
def ci_pulse_width_chan(task, sim_6363_device):
    """Creates CI Channel object to measure the width of a digital pulse."""
    ci_channel = task.ci_channels.add_ci_pulse_width_chan(
        sim_6363_device.ci_physical_chans[0].name,
    )
    yield ci_channel


@pytest.fixture(scope="function")
def ci_count_edges_chan(task, sim_6363_device):
    """Creates CI Channel object to count edges."""
    ci_channel = task.ci_channels.add_ci_count_edges_chan(
        sim_6363_device.ci_physical_chans[0].name,
    )
    yield ci_channel


def test___channel___get_boolean_property___returns_default_value(
    ai_voltage_chan_with_excit: AIChannel,
):
    assert not ai_voltage_chan_with_excit.ai_excit_use_for_scaling


def test___channel___set_boolean_property___returns_assigned_value(
    ai_voltage_chan_with_excit: AIChannel,
):
    ai_voltage_chan_with_excit.ai_excit_use_for_scaling = True

    assert ai_voltage_chan_with_excit.ai_excit_use_for_scaling


def test___channel___reset_boolean_property___returns_default_value(
    ai_voltage_chan_with_excit: AIChannel,
):
    ai_voltage_chan_with_excit.ai_excit_use_for_scaling = True

    del ai_voltage_chan_with_excit.ai_excit_use_for_scaling

    assert not ai_voltage_chan_with_excit.ai_excit_use_for_scaling


def test___channel___get_enum_property___returns_default_value(ai_power_chan: AIChannel):
    assert ai_power_chan.pwr_idle_output_behavior == PowerIdleOutputBehavior.MAINTAIN_EXISTING_VALUE


def test___channel___set_enum_property___returns_assigned_value(ai_power_chan: AIChannel):
    ai_power_chan.pwr_idle_output_behavior = PowerIdleOutputBehavior.OUTPUT_DISABLED

    assert ai_power_chan.pwr_idle_output_behavior == PowerIdleOutputBehavior.OUTPUT_DISABLED


def test___channel___reset_enum_property___returns_default_value(ai_power_chan: AIChannel):
    ai_power_chan.pwr_idle_output_behavior = PowerIdleOutputBehavior.OUTPUT_DISABLED

    del ai_power_chan.pwr_idle_output_behavior

    assert ai_power_chan.pwr_idle_output_behavior == PowerIdleOutputBehavior.MAINTAIN_EXISTING_VALUE


def test___channel___get_float_property___returns_default_value(ai_rtd_chan: AIChannel):
    assert ai_rtd_chan.ai_rtd_a == 0.00381


def test___channel___set_float_property___returns_assigned_value(ai_rtd_chan: AIChannel):
    value_to_set = 0.058388
    ai_rtd_chan.ai_rtd_a = value_to_set

    assert ai_rtd_chan.ai_rtd_a == value_to_set


def test___channel___reset_float_property___returns_default_value(ai_rtd_chan: AIChannel):
    ai_rtd_chan.ai_rtd_a = 0.058388

    del ai_rtd_chan.ai_rtd_a

    assert ai_rtd_chan.ai_rtd_a == 0.00381


def test___channel___get_string_property___returns_default_value(ci_pulse_width_chan: CIChannel):
    assert ci_pulse_width_chan.ci_ctr_timebase_dig_fltr_timebase_src == "100MHzTimebase"


def test___channel___set_string_property___returns_assigned_value(ci_pulse_width_chan: CIChannel):
    value_to_set = "20MHzTimebase"
    ci_pulse_width_chan.ci_ctr_timebase_dig_fltr_timebase_src = value_to_set

    assert ci_pulse_width_chan.ci_ctr_timebase_dig_fltr_timebase_src == value_to_set


def test___channel___reset_string_property___returns_default_value(ci_pulse_width_chan: CIChannel):
    ci_pulse_width_chan.ci_ctr_timebase_dig_fltr_timebase_src = "20MHzTimebase"

    del ci_pulse_width_chan.ci_ctr_timebase_dig_fltr_timebase_src

    assert ci_pulse_width_chan.ci_ctr_timebase_dig_fltr_timebase_src == "100MHzTimebase"


def test___channel___get_uint32_property___returns_default_value(
    ai_voltage_chan_with_excit: AIChannel,
):
    assert ai_voltage_chan_with_excit.ai_lossy_lsb_removal_compressed_samp_size == 16


def test___channel___set_uint32_property___returns_assigned_value(
    ai_voltage_chan_with_excit: AIChannel,
):
    value_to_set = 15
    ai_voltage_chan_with_excit.ai_lossy_lsb_removal_compressed_samp_size = value_to_set

    assert ai_voltage_chan_with_excit.ai_lossy_lsb_removal_compressed_samp_size == value_to_set


def test___channel___reset_uint32_property___returns_default_value(
    ai_voltage_chan_with_excit: AIChannel,
):
    ai_voltage_chan_with_excit.ai_lossy_lsb_removal_compressed_samp_size = 15

    del ai_voltage_chan_with_excit.ai_lossy_lsb_removal_compressed_samp_size

    assert ai_voltage_chan_with_excit.ai_lossy_lsb_removal_compressed_samp_size == 16


def test___channel___get_deprecated_properties___reports_warnings(ai_rtd_chan: AIChannel):
    with pytest.deprecated_call():
        assert ai_rtd_chan.ai_rtd_r0 == ai_rtd_chan.ai_rtd_r_0


def test___channel___set_deprecated_properties___reports_warnings(ai_rtd_chan: AIChannel):
    with pytest.deprecated_call():
        ai_rtd_chan.ai_rtd_r_0 = 1000.0


def test___channel___reset_deprecated_properties___reports_warnings(ai_rtd_chan: AIChannel):
    with pytest.deprecated_call():
        del ai_rtd_chan.ai_rtd_r_0


def test___channel_with_scale___get_scale_property___returns_scale(
    ai_voltage_chan_with_scale: AIChannel,
):
    scale = ai_voltage_chan_with_scale.ai_custom_scale

    assert scale.name == "double_gain_scale"


def test___channel_with_scale___get_scale_property___shared_interpreter(
    ai_voltage_chan_with_scale: AIChannel,
):
    scale = ai_voltage_chan_with_scale.ai_custom_scale

    assert scale._interpreter is ai_voltage_chan_with_scale._interpreter


@pytest.mark.scale_name("polynomial_scale")
def test___channel_with_scale___set_scale_property___returns_assigned_scale(
    ai_voltage_chan_with_scale: AIChannel, persisted_scale: PersistedScale
):
    ai_voltage_chan_with_scale.ai_custom_scale = persisted_scale.load()

    assert ai_voltage_chan_with_scale.ai_custom_scale.name == "polynomial_scale"


def test___channel_with_scale___reset_scale_property___returns_empty_scale(
    ai_voltage_chan_with_scale: AIChannel,
):
    del ai_voltage_chan_with_scale.ai_custom_scale
    ai_voltage_chan_with_scale.ai_voltage_units = VoltageUnits.VOLTS

    assert ai_voltage_chan_with_scale.ai_custom_scale.name == ""


def test___channel___get_physical_channel_property___returns_physical_channel(
    ai_rtd_chan: AIChannel, task: Task
):
    physical_channel = ai_rtd_chan.physical_channel

    assert physical_channel.name == f"{task.devices[0].name}/ai0"


def test___channel___get_physical_channel_property___shared_interpreter(
    ai_rtd_chan: AIChannel, task: Task
):
    physical_channel = ai_rtd_chan.physical_channel

    assert physical_channel._interpreter is task._interpreter
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/task/channels/test_ci_channel.py sha256=093d53da0c5c98a9ca6b7e544d75c0c7532543840d758415cd705fdea132b272 bytes=12653 -->
## FILE: tests/component/task/channels/test_ci_channel.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/task/channels/test_ci_channel.py`
- sha256: `093d53da0c5c98a9ca6b7e544d75c0c7532543840d758415cd705fdea132b272`
- bytes: 12653

````python
import pytest

from nidaqmx import Task
from nidaqmx.constants import (
    AngleUnits,
    CountDirection,
    CounterFrequencyMethod,
    Edge,
    EncoderType,
    EncoderZIndexPhase,
    UsageTypeCI,
)
from nidaqmx.system import Device
from nidaqmx.task.channels import CIChannel


# Note: Tests for other channel types will be less complete given that the underlying Python
# implementation is code-generated and the underlying C API implementation is well unit-tested.
@pytest.mark.parametrize(
    "decoding_type, zidx_enable, zidx_val, zidx_phase, units, pulses_per_rev, initial_angle, custom_scale_name",
    [
        (
            EncoderType.TWO_PULSE_COUNTING,
            True,
            30.0,
            EncoderZIndexPhase.AHIGH_BHIGH,
            AngleUnits.DEGREES,
            24,
            15.0,
            "",
        ),
        (
            EncoderType.X_2,
            False,
            0.0,
            EncoderZIndexPhase.AHIGH_BLOW,
            AngleUnits.RADIANS,
            12,
            0.0,
            "",
        ),
        (
            EncoderType.X_4,
            False,
            0.0,
            EncoderZIndexPhase.AHIGH_BLOW,
            AngleUnits.FROM_CUSTOM_SCALE,
            8,
            0.0,
            "degrees_scale",
        ),
    ],
)
def test___task___add_ci_ang_encoder_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    decoding_type: EncoderType,
    zidx_enable: bool,
    zidx_val: float,
    zidx_phase: EncoderZIndexPhase,
    units: AngleUnits,
    pulses_per_rev: int,
    initial_angle: float,
    custom_scale_name: str,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_ang_encoder_chan(
        sim_6363_device.ci_physical_chans[0].name,
        decoding_type=decoding_type,
        zidx_enable=zidx_enable,
        zidx_val=zidx_val,
        zidx_phase=zidx_phase,
        units=units,
        pulses_per_rev=pulses_per_rev,
        initial_angle=initial_angle,
        custom_scale_name=custom_scale_name,
    )

    assert chan.ci_meas_type == UsageTypeCI.POSITION_ANGULAR_ENCODER
    assert chan.ci_encoder_decoding_type == decoding_type
    assert chan.ci_encoder_z_index_enable == zidx_enable
    assert chan.ci_encoder_z_index_val == zidx_val
    assert chan.ci_encoder_z_index_phase == zidx_phase
    assert chan.ci_ang_encoder_units == units
    assert chan.ci_ang_encoder_pulses_per_rev == pulses_per_rev
    assert chan.ci_ang_encoder_initial_angle == initial_angle
    assert chan.ci_custom_scale.name == custom_scale_name


@pytest.mark.parametrize(
    "decoding_type, pulses_per_rev",
    [
        (EncoderType.TWO_PULSE_COUNTING, 24),
        (EncoderType.X_2, 12),
        (EncoderType.X_4, 8),
    ],
)
def test___task___add_ci_ang_velocity_chan___sets_channel_attributes(
    task: Task,
    sim_velocity_device: Device,
    decoding_type: EncoderType,
    pulses_per_rev: int,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_ang_velocity_chan(
        sim_velocity_device.ci_physical_chans[0].name,
        decoding_type=decoding_type,
        pulses_per_rev=pulses_per_rev,
    )

    assert chan.ci_meas_type == UsageTypeCI.VELOCITY_ANGULAR_ENCODER
    assert chan.ci_velocity_encoder_decoding_type == decoding_type
    assert chan.ci_velocity_ang_encoder_pulses_per_rev == pulses_per_rev


@pytest.mark.parametrize(
    "edge, initial_count, count_direction",
    [
        (Edge.RISING, 0, CountDirection.COUNT_UP),
        (Edge.FALLING, 1, CountDirection.COUNT_DOWN),
    ],
)
def test___task___add_ci_count_edges_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    edge: Edge,
    initial_count: int,
    count_direction: CountDirection,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_count_edges_chan(
        sim_6363_device.ci_physical_chans[0].name,
        edge=edge,
        initial_count=initial_count,
        count_direction=count_direction,
    )

    assert chan.ci_meas_type == UsageTypeCI.COUNT_EDGES
    assert chan.ci_count_edges_active_edge
    assert chan.ci_count_edges_initial_cnt == initial_count
    assert chan.ci_count_edges_dir == count_direction


@pytest.mark.parametrize(
    "edge",
    [Edge.RISING, Edge.FALLING],
)
def test___task___add_ci_duty_cycle_chan___sets_channel_attributes(
    task: Task,
    sim_velocity_device: Device,
    edge: Edge,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_duty_cycle_chan(
        sim_velocity_device.ci_physical_chans[0].name,
        edge=edge,
    )

    assert chan.ci_meas_type == UsageTypeCI.DUTY_CYCLE
    assert chan.ci_duty_cycle_starting_edge == edge


@pytest.mark.parametrize(
    "edge, meas_method, meas_time, divisor",
    [
        (Edge.RISING, CounterFrequencyMethod.LOW_FREQUENCY_1_COUNTER, 0.001, 4),
        (Edge.FALLING, CounterFrequencyMethod.HIGH_FREQUENCY_2_COUNTERS, 0.002, 4),
        (Edge.RISING, CounterFrequencyMethod.LARGE_RANGE_2_COUNTERS, 0.001, 8),
    ],
)
def test___task___add_ci_freq_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    edge: Edge,
    meas_method: CounterFrequencyMethod,
    meas_time: float,
    divisor: int,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_freq_chan(
        sim_6363_device.ci_physical_chans[0].name,
        edge=edge,
        meas_method=meas_method,
        meas_time=meas_time,
        divisor=divisor,
    )

    assert chan.ci_meas_type == UsageTypeCI.FREQUENCY
    assert chan.ci_freq_starting_edge == edge
    assert chan.ci_freq_meas_meth == meas_method
    # these properties are only relevant for certain measurement methods, and
    # otherwise the coercion behavior is hard to rationalize
    if meas_method == CounterFrequencyMethod.HIGH_FREQUENCY_2_COUNTERS:
        assert chan.ci_freq_meas_time == meas_time
    elif meas_method == CounterFrequencyMethod.LARGE_RANGE_2_COUNTERS:
        assert chan.ci_freq_div == divisor


# No active devices support the GPS Timestamp channel.
@pytest.mark.parametrize(
    "decoding_type, dist_per_pulse, initial_pos",
    [
        (
            EncoderType.TWO_PULSE_COUNTING,
            0.001,
            0.0,
        ),
        (
            EncoderType.X_2,
            0.002,
            0.002,
        ),
        (
            EncoderType.X_4,
            0.004,
            0.0,
        ),
    ],
)
def test___task___add_ci_lin_encoder_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    decoding_type: EncoderType,
    dist_per_pulse: float,
    initial_pos: float,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_lin_encoder_chan(
        sim_6363_device.ci_physical_chans[0].name,
        decoding_type=decoding_type,
        dist_per_pulse=dist_per_pulse,
        initial_pos=initial_pos,
    )

    assert chan.ci_meas_type == UsageTypeCI.POSITION_LINEAR_ENCODER
    assert chan.ci_encoder_decoding_type == decoding_type
    assert chan.ci_lin_encoder_dist_per_pulse == dist_per_pulse
    assert chan.ci_lin_encoder_initial_pos == initial_pos


@pytest.mark.parametrize(
    "decoding_type, dist_per_pulse",
    [
        (EncoderType.TWO_PULSE_COUNTING, 0.001),
        (EncoderType.X_2, 0.002),
        (EncoderType.X_4, 0.004),
    ],
)
def test___task___add_ci_lin_velocity_chan___sets_channel_attributes(
    task: Task,
    sim_velocity_device: Device,
    decoding_type: EncoderType,
    dist_per_pulse: float,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_lin_velocity_chan(
        sim_velocity_device.ci_physical_chans[0].name,
        decoding_type=decoding_type,
        dist_per_pulse=dist_per_pulse,
    )

    assert chan.ci_meas_type == UsageTypeCI.VELOCITY_LINEAR_ENCODER
    assert chan.ci_velocity_encoder_decoding_type == decoding_type
    assert chan.ci_velocity_lin_encoder_dist_per_pulse == dist_per_pulse


@pytest.mark.parametrize(
    "edge, meas_method, meas_time, divisor",
    [
        (Edge.RISING, CounterFrequencyMethod.LOW_FREQUENCY_1_COUNTER, 0.001, 4),
        (Edge.FALLING, CounterFrequencyMethod.HIGH_FREQUENCY_2_COUNTERS, 0.002, 4),
        (Edge.RISING, CounterFrequencyMethod.LARGE_RANGE_2_COUNTERS, 0.001, 8),
    ],
)
def test___task___add_ci_period_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    edge: Edge,
    meas_method: CounterFrequencyMethod,
    meas_time: float,
    divisor: int,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_period_chan(
        sim_6363_device.ci_physical_chans[0].name,
        edge=edge,
        meas_method=meas_method,
        meas_time=meas_time,
        divisor=divisor,
    )

    assert chan.ci_meas_type == UsageTypeCI.PERIOD
    assert chan.ci_period_starting_edge == edge
    assert chan.ci_period_meas_meth == meas_method
    # these properties are only relevant for certain measurement methods, and
    # otherwise the coercion behavior is hard to rationalize
    if meas_method == CounterFrequencyMethod.HIGH_FREQUENCY_2_COUNTERS:
        assert chan.ci_period_meas_time == meas_time
    elif meas_method == CounterFrequencyMethod.LARGE_RANGE_2_COUNTERS:
        assert chan.ci_period_div == divisor


@pytest.mark.parametrize(
    "source_terminal",
    ["PFI0", "PFI1"],
)
def test___task___add_ci_pulse_chan_ticks___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    source_terminal: str,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_pulse_chan_ticks(
        sim_6363_device.ci_physical_chans[0].name,
        source_terminal=source_terminal,
    )

    assert chan.ci_meas_type == UsageTypeCI.PULSE_TICKS
    # terminal will be fully qualified
    assert source_terminal in chan.ci_ctr_timebase_src


# Nothing novel here vs. ticks
def test___task___add_ci_pulse_chan_time___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_pulse_chan_time(
        sim_6363_device.ci_physical_chans[0].name,
    )

    assert chan.ci_meas_type == UsageTypeCI.PULSE_TIME


# Nothing novel here vs. ticks
def test___task___add_ci_pulse_chan_freq___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_pulse_chan_freq(
        sim_6363_device.ci_physical_chans[0].name,
    )

    assert chan.ci_meas_type == UsageTypeCI.PULSE_FREQ


@pytest.mark.parametrize(
    "starting_edge",
    [Edge.RISING, Edge.FALLING],
)
def test___task___add_ci_pulse_width_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    starting_edge: Edge,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_pulse_width_chan(
        sim_6363_device.ci_physical_chans[0].name,
        starting_edge=starting_edge,
    )

    assert chan.ci_meas_type == UsageTypeCI.PULSE_WIDTH_DIGITAL
    assert chan.ci_pulse_width_starting_edge == starting_edge


def test___task___add_ci_semi_period_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_semi_period_chan(
        sim_6363_device.ci_physical_chans[0].name,
    )

    assert chan.ci_meas_type == UsageTypeCI.PULSE_WIDTH_DIGITAL_SEMI_PERIOD


@pytest.mark.parametrize(
    "first_edge, second_edge",
    [(Edge.RISING, Edge.FALLING), (Edge.FALLING, Edge.RISING)],
)
def test___task___add_ci_two_edge_sep_chan___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    first_edge: Edge,
    second_edge: Edge,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_two_edge_sep_chan(
        sim_6363_device.ci_physical_chans[0].name,
        first_edge=first_edge,
        second_edge=second_edge,
    )

    assert chan.ci_meas_type == UsageTypeCI.PULSE_WIDTH_DIGITAL_TWO_EDGE_SEPARATION
    assert chan.ci_two_edge_sep_first_edge == first_edge
    assert chan.ci_two_edge_sep_second_edge == second_edge


# For more extensive virtual channel name testing, refer to test_di_channel.py
def test___task___add_ci_chans_with_name___sets_channel_name(
    task: Task,
    sim_6363_device: Device,
) -> None:
    chan: CIChannel = task.ci_channels.add_ci_count_edges_chan(
        sim_6363_device.ci_physical_chans[0].name, name_to_assign_to_channel="myChan"
    )

    assert chan.name == "myChan"
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/task/channels/test_co_channel.py sha256=30788df51e2ce7bf24bb922880dd85e7e57cf0ee75dad845909135a410c0c0a6 bytes=3561 -->
## FILE: tests/component/task/channels/test_co_channel.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/task/channels/test_co_channel.py`
- sha256: `30788df51e2ce7bf24bb922880dd85e7e57cf0ee75dad845909135a410c0c0a6`
- bytes: 3561

````python
import pytest

from nidaqmx import Task
from nidaqmx.constants import Level, UsageTypeCO
from nidaqmx.system import Device
from nidaqmx.task.channels import COChannel


@pytest.mark.parametrize(
    "idle_state, initial_delay, freq, duty_cycle",
    [
        (Level.LOW, 0.001, 1.0, 0.25),
        (Level.HIGH, 0.002, 100.0, 0.75),
    ],
)
def test___task___add_co_pulse_chan_freq___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    idle_state: Level,
    initial_delay: float,
    freq: float,
    duty_cycle: float,
) -> None:
    chan: COChannel = task.co_channels.add_co_pulse_chan_freq(
        sim_6363_device.ci_physical_chans[0].name,
        idle_state=idle_state,
        initial_delay=initial_delay,
        freq=freq,
        duty_cycle=duty_cycle,
    )

    assert chan.co_output_type == UsageTypeCO.PULSE_FREQUENCY
    assert chan.co_pulse_idle_state == idle_state
    assert chan.co_pulse_freq_initial_delay == initial_delay
    assert chan.co_pulse_freq == freq
    assert chan.co_pulse_duty_cyc == duty_cycle


@pytest.mark.parametrize(
    "source_terminal, idle_state, initial_delay, low_ticks, high_ticks",
    [
        ("PFI0", Level.LOW, 2, 75, 25),
        ("100khzTimebase", Level.HIGH, 4, 250, 750),
    ],
)
def test___task___add_co_pulse_chan_ticks___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    source_terminal: str,
    idle_state: Level,
    initial_delay: float,
    low_ticks: int,
    high_ticks: int,
) -> None:
    chan: COChannel = task.co_channels.add_co_pulse_chan_ticks(
        sim_6363_device.ci_physical_chans[0].name,
        source_terminal=source_terminal,
        idle_state=idle_state,
        initial_delay=initial_delay,
        low_ticks=low_ticks,
        high_ticks=high_ticks,
    )

    assert chan.co_output_type == UsageTypeCO.PULSE_TICKS
    # terminal will be fully qualified
    assert source_terminal in chan.co_ctr_timebase_src
    assert chan.co_pulse_idle_state == idle_state
    assert chan.co_pulse_ticks_initial_delay == initial_delay
    assert chan.co_pulse_low_ticks == low_ticks
    assert chan.co_pulse_high_ticks == high_ticks


@pytest.mark.parametrize(
    "idle_state, initial_delay, low_time, high_time",
    [
        (Level.LOW, 0.001, 0.75, 0.25),
        (Level.HIGH, 0.002, 0.0025, 0.0075),
    ],
)
def test___task___add_co_pulse_chan_time___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    idle_state: Level,
    initial_delay: float,
    low_time: float,
    high_time: float,
) -> None:
    chan: COChannel = task.co_channels.add_co_pulse_chan_time(
        sim_6363_device.ci_physical_chans[0].name,
        idle_state=idle_state,
        initial_delay=initial_delay,
        low_time=low_time,
        high_time=high_time,
    )

    assert chan.co_output_type == UsageTypeCO.PULSE_TIME
    assert chan.co_pulse_idle_state == idle_state
    assert chan.co_pulse_time_initial_delay == initial_delay
    assert chan.co_pulse_low_time == low_time
    assert chan.co_pulse_high_time == high_time


# For more extensive virtual channel name testing, refer to test_di_channel.py
def test___task___add_co_chans_with_name___sets_channel_name(
    task: Task,
    sim_6363_device: Device,
) -> None:
    chan: COChannel = task.co_channels.add_co_pulse_chan_freq(
        sim_6363_device.co_physical_chans[0].name, name_to_assign_to_channel="myChan"
    )

    assert chan.name == "myChan"
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/task/channels/test_di_channel.py sha256=3cc5a0f134d8483411529ba51ed95cbf4440b64dcb9925f294f8ff2bbccfb8df bytes=8042 -->
## FILE: tests/component/task/channels/test_di_channel.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/task/channels/test_di_channel.py`
- sha256: `3cc5a0f134d8483411529ba51ed95cbf4440b64dcb9925f294f8ff2bbccfb8df`
- bytes: 8042

````python
import pytest

from nidaqmx import Task
from nidaqmx.constants import ChannelType, LineGrouping
from nidaqmx.system import Device, System
from nidaqmx.task.channels import DIChannel
from nidaqmx.utils import flatten_channel_string, unflatten_channel_string


@pytest.mark.parametrize(
    "num_lines",
    [1, 2, 8],
)
def test___task___add_di_chan_chan_for_all_lines___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    num_lines: int,
) -> None:
    chan: DIChannel = task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[:num_lines]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )

    assert len(chan) == 1
    assert chan.chan_type == ChannelType.DIGITAL_INPUT
    assert chan.di_num_lines == num_lines


@pytest.mark.parametrize(
    "num_lines",
    [1, 2, 8],
)
def test___task___add_di_chan_chan_per_line___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    num_lines: int,
) -> None:
    chans: DIChannel = task.di_channels.add_di_chan(
        flatten_channel_string(sim_6363_device.di_lines.channel_names[:num_lines]),
        line_grouping=LineGrouping.CHAN_PER_LINE,
    )

    assert len(chans) == num_lines
    for chan in chans:
        assert chan.chan_type == ChannelType.DIGITAL_INPUT
        assert chan.di_num_lines == 1


def _test___task___add_di_chans_with_name___sets_channel_name(
    task: Task,
    sim_6363_device: Device,
    phys_chan_list: list[str],
    line_grouping: LineGrouping,
    name_to_assign_to_lines: str,
    expected_virtual_channel_name: str,
    qualify_expected_virtual_channel_name: bool,
) -> None:
    qualified_physical_channel_name = flatten_channel_string(
        [f"{sim_6363_device.name}/{chan}" for chan in phys_chan_list]
    )
    chan: DIChannel = task.di_channels.add_di_chan(
        qualified_physical_channel_name,
        line_grouping=line_grouping,
        name_to_assign_to_lines=name_to_assign_to_lines,
    )

    # If a user doesn't specify a virtual channel name, DAQmx will use the physical channel name,
    # which we now need to fully quality.
    if qualify_expected_virtual_channel_name:
        expected_virtual_channel_name = f"{sim_6363_device.name}/{expected_virtual_channel_name}"

    assert unflatten_channel_string(chan.name) == unflatten_channel_string(
        expected_virtual_channel_name
    )


@pytest.mark.parametrize(
    "phys_chan_list, line_grouping, name_to_assign_to_lines, expected_virtual_channel_name, qualify_expected_virtual_channel_name",
    [
        (["port0/line0"], LineGrouping.CHAN_PER_LINE, "", "port0/line0", True),
        (["port0/line0"], LineGrouping.CHAN_FOR_ALL_LINES, "", "port0/line0", True),
        (
            ["port0/line0", "port0/line1"],
            LineGrouping.CHAN_PER_LINE,
            "",
            "port0/line0:1",
            True,
        ),
        (
            ["port0/line0", "port0/line1"],
            LineGrouping.CHAN_FOR_ALL_LINES,
            "",
            "port0/line0...",
            True,
        ),
        (["port0/line0"], LineGrouping.CHAN_PER_LINE, "myChan", "myChan", False),
        (["port0/line0"], LineGrouping.CHAN_FOR_ALL_LINES, "myChan", "myChan", False),
        (["port0/line0:7"], LineGrouping.CHAN_PER_LINE, "myChan", "myChan0:7", False),
        (["port0/line0:7"], LineGrouping.CHAN_FOR_ALL_LINES, "myChan", "myChan", False),
        (["port0/line0:7"], LineGrouping.CHAN_FOR_ALL_LINES, "myChan0", "myChan0", False),
    ],
)
def test___task___add_di_chans_with_simple_name___sets_channel_name(
    task: Task,
    sim_6363_device: Device,
    phys_chan_list: list[str],
    line_grouping: LineGrouping,
    name_to_assign_to_lines: str,
    expected_virtual_channel_name: str,
    qualify_expected_virtual_channel_name: bool,
) -> None:
    _test___task___add_di_chans_with_name___sets_channel_name(
        task,
        sim_6363_device,
        phys_chan_list,
        line_grouping,
        name_to_assign_to_lines,
        expected_virtual_channel_name,
        qualify_expected_virtual_channel_name,
    )


@pytest.mark.skipif(
    System.local().driver_version < (24, 5, 0),
    reason="The fix for this test requires DAQmx 24.5.0 and later",
)
@pytest.mark.grpc_xfail(
    reason="The fix for this test isn't supported on gRPC",
)
@pytest.mark.parametrize(
    "phys_chan_list, line_grouping, name_to_assign_to_lines, expected_virtual_channel_name, qualify_expected_virtual_channel_name",
    [
        (["port0/line0"], LineGrouping.CHAN_PER_LINE, " ", "port0/line0", True),
        (["port0/line0"], LineGrouping.CHAN_FOR_ALL_LINES, " ", "port0/line0", True),
        (["port0/line0"], LineGrouping.CHAN_PER_LINE, " myChan ", "myChan", False),
        (["port0/line0"], LineGrouping.CHAN_FOR_ALL_LINES, " myChan ", "myChan", False),
        (["port0/line0:7"], LineGrouping.CHAN_PER_LINE, "myChan0", "myChan0:7", False),
        (["port0/line0:7"], LineGrouping.CHAN_PER_LINE, " myChan0 ", "myChan0:7", False),
        (["port0/line0:7"], LineGrouping.CHAN_FOR_ALL_LINES, " myChan0 ", "myChan0", False),
        (["port0/line0:7"], LineGrouping.CHAN_PER_LINE, " myChan 0 ", "myChan0:7", False),
        (["port0/line0:7"], LineGrouping.CHAN_FOR_ALL_LINES, " myChan 0 ", "myChan 0", False),
        (["port0/line0:7"], LineGrouping.CHAN_PER_LINE, "myChan8", "myChan8:15", False),
        (["port0/line0:7"], LineGrouping.CHAN_PER_LINE, "myChan008", "myChan008:015", False),
        (
            ["port0/line0:1"],
            LineGrouping.CHAN_PER_LINE,
            "myFirstChan,mySecondChan",
            "myFirstChan, mySecondChan",
            False,
        ),
        (
            ["port0/line0:1"],
            LineGrouping.CHAN_PER_LINE,
            "  myFirstChan  ,  mySecondChan  ",
            "myFirstChan, mySecondChan",
            False,
        ),
        (
            ["port0/line0:1"],
            LineGrouping.CHAN_PER_LINE,
            "myFirstChan, , mySecondChan",
            "myFirstChan, mySecondChan",
            False,
        ),
        (
            ["port0/line0:7"],
            LineGrouping.CHAN_PER_LINE,
            "myFirstChan,mySecondChan",
            "myFirstChan, mySecondChan0:6",
            False,
        ),
        (
            ["port0/line0:7"],
            LineGrouping.CHAN_PER_LINE,
            "myFirstChan2:5,mySecondChan34",
            "myFirstChan2:5, mySecondChan34:37",
            False,
        ),
        (
            ["port0/line0:7"],
            LineGrouping.CHAN_PER_LINE,
            "myFirstChan0:9",
            "myFirstChan0:7",
            False,
        ),
        (
            ["port0/line0:7"],
            LineGrouping.CHAN_FOR_ALL_LINES,
            "myFirstChan0:9",
            "myFirstChan0",
            False,
        ),
        (
            ["port0/line0:7"],
            LineGrouping.CHAN_PER_LINE,
            "myFirstChan0:6, mySecondChan, myThirdChan",
            "myFirstChan0:6, mySecondChan",
            False,
        ),
        (
            ["port0/line0:7"],
            LineGrouping.CHAN_PER_LINE,
            "myFirstChan0:5, mySecondChan0:5",
            "myFirstChan0:5, mySecondChan0:1",
            False,
        ),
    ],
)
def test___task___add_di_chans_with_complex_name___sets_channel_name(
    task: Task,
    sim_6363_device: Device,
    phys_chan_list: list[str],
    line_grouping: LineGrouping,
    name_to_assign_to_lines: str,
    expected_virtual_channel_name: str,
    qualify_expected_virtual_channel_name: bool,
) -> None:
    _test___task___add_di_chans_with_name___sets_channel_name(
        task,
        sim_6363_device,
        phys_chan_list,
        line_grouping,
        name_to_assign_to_lines,
        expected_virtual_channel_name,
        qualify_expected_virtual_channel_name,
    )
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/task/channels/test_do_channel.py sha256=a8cb77dc945f3e181b4027f68fc625a1d1ca1d5459b490884472fd2034015795 bytes=2135 -->
## FILE: tests/component/task/channels/test_do_channel.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/task/channels/test_do_channel.py`
- sha256: `a8cb77dc945f3e181b4027f68fc625a1d1ca1d5459b490884472fd2034015795`
- bytes: 2135

````python
import pytest

from nidaqmx import Task
from nidaqmx.constants import ChannelType, LineGrouping
from nidaqmx.system import Device, System
from nidaqmx.task.channels import DOChannel
from nidaqmx.utils import flatten_channel_string, unflatten_channel_string


@pytest.mark.parametrize(
    "num_lines",
    [1, 2, 8],
)
def test___task___add_do_chan_chan_for_all_lines___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    num_lines: int,
) -> None:
    chan: DOChannel = task.do_channels.add_do_chan(
        flatten_channel_string(sim_6363_device.do_lines.channel_names[:num_lines]),
        line_grouping=LineGrouping.CHAN_FOR_ALL_LINES,
    )

    assert len(chan) == 1
    assert chan.chan_type == ChannelType.DIGITAL_OUTPUT
    assert chan.do_num_lines == num_lines


@pytest.mark.parametrize(
    "num_lines",
    [1, 2, 8],
)
def test___task___add_do_chan_chan_per_line___sets_channel_attributes(
    task: Task,
    sim_6363_device: Device,
    num_lines: int,
) -> None:
    chans: DOChannel = task.do_channels.add_do_chan(
        flatten_channel_string(sim_6363_device.do_lines.channel_names[:num_lines]),
        line_grouping=LineGrouping.CHAN_PER_LINE,
    )

    assert len(chans) == num_lines
    for chan in chans:
        assert chan.chan_type == ChannelType.DIGITAL_OUTPUT
        assert chan.do_num_lines == 1


# For more extensive virtual channel name testing, refer to test_di_channel.py
@pytest.mark.skipif(
    System.local().driver_version < (24, 5, 0),
    reason="The fix for this test requires DAQmx 24.5.0 and later",
)
@pytest.mark.library_only(
    reason="The fix for this test isn't supported on gRPC",
)
def test___task___add_do_chans_with_name___sets_channel_name(
    task: Task,
    sim_6363_device: Device,
) -> None:
    chan: DOChannel = task.do_channels.add_do_chan(
        f"{sim_6363_device.name}/port0/line0:7",
        line_grouping=LineGrouping.CHAN_PER_LINE,
        name_to_assign_to_lines="myChan0",
    )

    assert unflatten_channel_string(chan.name) == unflatten_channel_string("myChan0:7")
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/task/test_export_signals_properties.py sha256=b2fe1ddcd63920198879097f7749bf32040f280741421bedffe52e52f1d1a324 bytes=2560 -->
## FILE: tests/component/task/test_export_signals_properties.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/task/test_export_signals_properties.py`
- sha256: `b2fe1ddcd63920198879097f7749bf32040f280741421bedffe52e52f1d1a324`
- bytes: 2560

````python
import pytest

from nidaqmx.constants import ExportAction, TaskMode
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError
from nidaqmx.task import Task


@pytest.fixture()
def ai_voltage_task(task, sim_6363_device):
    """Gets AI voltage task."""
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    yield task


@pytest.fixture()
def ao_voltage_task(task, sim_6363_device):
    """Gets AO voltage task."""
    task.ao_channels.add_ao_voltage_chan(sim_6363_device.ao_physical_chans[0].name)
    yield task


def test___ai_task___get_enum_property___returns_default_value(ai_voltage_task: Task):
    assert ai_voltage_task.export_signals.samp_clk_output_behavior == ExportAction.PULSE


def test___ai_task___set_enum_property___returns_assigned_value(ai_voltage_task: Task):
    value_to_set = ExportAction.LEVEL
    ai_voltage_task.export_signals.samp_clk_output_behavior = value_to_set

    assert ai_voltage_task.export_signals.samp_clk_output_behavior == value_to_set


def test___ai_task___reset_enum_property___returns_default_value(ai_voltage_task: Task):
    ai_voltage_task.export_signals.samp_clk_output_behavior == ExportAction.INTERLOCKED

    del ai_voltage_task.export_signals.samp_clk_output_behavior

    assert ai_voltage_task.export_signals.samp_clk_output_behavior == ExportAction.PULSE


def test___ai_task___get_string_property___returns_default_value(ai_voltage_task: Task):
    assert ai_voltage_task.export_signals.start_trig_output_term == ""


def test___ai_task___set_invalid_routing_destination___throws_daqerror(
    ai_voltage_task: Task,
):
    with pytest.raises(DaqError) as exc_info:
        ai_voltage_task.export_signals.start_trig_output_term = "RTSI"
        ai_voltage_task.control(TaskMode.TASK_VERIFY)

    assert (
        exc_info.value.error_type == DAQmxErrors.INVALID_ROUTING_DESTINATION_TERMINAL_NAME_ROUTING
    )


def test___ai_task___set_string_property___returns_assigned_value(ao_voltage_task: Task):
    value_to_set = "RSE"
    ao_voltage_task.export_signals.start_trig_output_term = value_to_set

    assert ao_voltage_task.export_signals.start_trig_output_term == value_to_set


def test___ai_task___reset_string_property___returns_default_value(ao_voltage_task: Task):
    ao_voltage_task.export_signals.start_trig_output_term = "DIFF"

    del ao_voltage_task.export_signals.start_trig_output_term

    assert ao_voltage_task.export_signals.start_trig_output_term == ""
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/task/test_in_stream.py sha256=74f9454db56ed03ec7121b090077287c4ca3ec006d9945425dd5bf09677b30d6 bytes=8771 -->
## FILE: tests/component/task/test_in_stream.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/task/test_in_stream.py`
- sha256: `74f9454db56ed03ec7121b090077287c4ca3ec006d9945425dd5bf09677b30d6`
- bytes: 8771

````python
import pathlib
import time

import numpy
import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import AcquisitionType, LoggingMode, LoggingOperation

# With a simulated X Series, setting ai_max/min to +/-2.5 V coerces the hardware range
# to +/-5 V and generates a noisy sine wave with range +/-2.5 V (raw: about +/-16383).
# The noisy sine wave should not produce full-scale readings.
SINE_VOLTAGE_MAX = 2.5
SINE_VOLTAGE_MIN = -2.5
SINE_RAW_MAX = 16383
SINE_RAW_MIN = -16384
FULL_SCALE_RAW_MAX = 32767
FULL_SCALE_RAW_MIN = -32768


@pytest.fixture()
def ai_task(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    return task


@pytest.fixture(params=[1, 2, 3])
def ai_sine_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device, request: pytest.FixtureRequest
) -> nidaqmx.Task:
    """Returns an analog input task with varying number of channels and a simulated sine wave."""
    _create_ai_sine_channels(task, sim_6363_device, number_of_channels=request.param)
    return task


def _create_ai_sine_channels(
    task: nidaqmx.Task, device: nidaqmx.system.Device, number_of_channels: int
) -> None:
    """Creates the specified number of analog input channels for a simulated sine wave."""
    for i in range(number_of_channels):
        task.ai_channels.add_ai_voltage_chan(
            device.ai_physical_chans[i].name,
            min_val=SINE_VOLTAGE_MIN,
            max_val=SINE_VOLTAGE_MAX,
        )

    # The driver's coerced ai_max/min should be wider than the desired ai_max/min.
    assert task.ai_channels.all.ai_min < SINE_VOLTAGE_MIN
    assert task.ai_channels.all.ai_max > SINE_VOLTAGE_MAX

    # This test assumes the data format is int16.
    assert task.ai_channels.all.ai_raw_samp_size == 16
    assert task.ai_channels.all.ai_rng_low < 0


@pytest.mark.parametrize("samples_to_read", [1, 10])
def test___ai_task___read___returns_valid_samples_shape_and_dtype(
    ai_sine_task: nidaqmx.Task, samples_to_read: int
) -> None:
    data = ai_sine_task.in_stream.read(samples_to_read)

    assert data.shape == (ai_sine_task.number_of_channels * samples_to_read,)
    assert data.dtype == numpy.int16
    assert (SINE_RAW_MIN <= data).all() and (data <= SINE_RAW_MAX).all()


def test___ai_finite_task___readall___returns_valid_samples_shape_and_dtype(
    ai_sine_task: nidaqmx.Task,
) -> None:
    ai_sine_task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=100
    )

    with pytest.deprecated_call():
        data = ai_sine_task.in_stream.readall()

    assert data.shape == (ai_sine_task.number_of_channels * 100,)
    assert data.dtype == numpy.int16
    assert (SINE_RAW_MIN <= data).all() and (data <= SINE_RAW_MAX).all()


def test___ai_continuous_task___readall___returns_valid_samples_shape_and_dtype(
    ai_sine_task: nidaqmx.Task,
) -> None:
    ai_sine_task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.CONTINUOUS, samps_per_chan=1000
    )
    ai_sine_task.start()
    # Wait until there are some samples to read.
    min_samples_per_channel = 100
    while ai_sine_task.in_stream.avail_samp_per_chan < min_samples_per_channel:
        time.sleep(10e-3)

    with pytest.deprecated_call():
        data = ai_sine_task.in_stream.readall()

    assert data.shape[0] >= ai_sine_task.number_of_channels * min_samples_per_channel
    assert data.shape[0] % ai_sine_task.number_of_channels == 0
    assert data.dtype == numpy.int16
    assert (SINE_RAW_MIN <= data).all() and (data <= SINE_RAW_MAX).all()


@pytest.mark.parametrize("samples_to_read", [1, 10])
def test___valid_array___readinto___returns_valid_samples(
    ai_sine_task: nidaqmx.Task, samples_to_read: int
) -> None:
    # Initialize the array to full-scale readings to ensure it is overwritten.
    data = numpy.full(
        ai_sine_task.number_of_channels * samples_to_read, FULL_SCALE_RAW_MAX, dtype=numpy.int16
    )

    with pytest.deprecated_call():
        samples_read = ai_sine_task.in_stream.readinto(data)

    assert samples_read == samples_to_read
    assert (SINE_RAW_MIN <= data).all() and (data <= SINE_RAW_MAX).all()


def test___odd_sized_array___readinto___returns_whole_samples_and_clears_padding(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> None:
    _create_ai_sine_channels(task, sim_6363_device, number_of_channels=2)
    # Initialize the array to full-scale readings to ensure it is overwritten.
    data = numpy.full(19, FULL_SCALE_RAW_MIN, dtype=numpy.int16)

    with pytest.deprecated_call():
        samples_read = task.in_stream.readinto(data)

    assert samples_read == 9
    assert (SINE_RAW_MIN <= data[:-1]).all() and (data[:-1] <= SINE_RAW_MAX).all()
    assert data[-1] == 0  # not FULL_SCALE_RAW_MIN


def test___ai_finite_task___read_all___returns_valid_samples_shape_and_dtype(
    ai_sine_task: nidaqmx.Task,
) -> None:
    ai_sine_task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=100
    )

    data = ai_sine_task.in_stream.read_all()

    assert data.shape == (ai_sine_task.number_of_channels * 100,)
    assert data.dtype == numpy.int16
    assert (SINE_RAW_MIN <= data).all() and (data <= SINE_RAW_MAX).all()


def test___ai_continuous_task___read_all___returns_valid_samples_shape_and_dtype(
    ai_sine_task: nidaqmx.Task,
) -> None:
    ai_sine_task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.CONTINUOUS, samps_per_chan=1000
    )
    ai_sine_task.start()
    # Wait until there are some samples to read.
    min_samples_per_channel = 100
    while ai_sine_task.in_stream.avail_samp_per_chan < min_samples_per_channel:
        time.sleep(10e-3)

    data = ai_sine_task.in_stream.read_all()

    assert data.shape[0] >= ai_sine_task.number_of_channels * min_samples_per_channel
    assert data.shape[0] % ai_sine_task.number_of_channels == 0
    assert data.dtype == numpy.int16
    assert (SINE_RAW_MIN <= data).all() and (data <= SINE_RAW_MAX).all()


@pytest.mark.parametrize("samples_to_read", [1, 10])
def test___valid_array___read_into___returns_valid_samples(
    ai_sine_task: nidaqmx.Task, samples_to_read: int
) -> None:
    # Initialize the array to full-scale readings to ensure it is overwritten.
    data = numpy.full(
        ai_sine_task.number_of_channels * samples_to_read, FULL_SCALE_RAW_MAX, dtype=numpy.int16
    )

    samples_read = ai_sine_task.in_stream.read_into(data)

    assert samples_read == samples_to_read
    assert (SINE_RAW_MIN <= data).all() and (data <= SINE_RAW_MAX).all()


def test___odd_sized_array___read_into___returns_whole_samples_and_clears_padding(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> None:
    _create_ai_sine_channels(task, sim_6363_device, number_of_channels=2)
    # Initialize the array to full-scale readings to ensure it is overwritten.
    data = numpy.full(19, FULL_SCALE_RAW_MIN, dtype=numpy.int16)

    samples_read = task.in_stream.read_into(data)

    assert samples_read == 9
    assert (SINE_RAW_MIN <= data[:-1]).all() and (data[:-1] <= SINE_RAW_MAX).all()
    assert data[-1] == 0  # not FULL_SCALE_RAW_MIN


def test___valid_path___configure_logging___returns_assigned_values(ai_task: nidaqmx.Task):
    expected_file_path = "Testing File.tdms"
    expected_group_name = "Task"
    expected_logging_mode = LoggingMode.LOG_AND_READ
    expected_logging_operation = LoggingOperation.CREATE_OR_REPLACE

    ai_task.in_stream.configure_logging(
        expected_file_path,
        logging_mode=expected_logging_mode,
        group_name=expected_group_name,
        operation=expected_logging_operation,
    )

    assert ai_task.in_stream.logging_file_path == pathlib.Path(expected_file_path)
    assert ai_task.in_stream.logging_mode == expected_logging_mode
    assert ai_task.in_stream.logging_tdms_group_name == expected_group_name
    assert ai_task.in_stream.logging_tdms_operation == expected_logging_operation


def test___valid_path___start_new_file___returns_assigned_value(ai_task: nidaqmx.Task):
    expected_file_path = "Testing File.tdms"
    ai_task.in_stream.start_new_file(expected_file_path)

    assert ai_task.in_stream.logging_file_path == pathlib.Path(expected_file_path)


def test___in_stream___set_nonexistent_property___raises_exception(task: nidaqmx.Task):
    with pytest.raises(AttributeError):
        task.in_stream.nonexistent_property = "foo"  # type: ignore[attr-defined]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/task/test_in_stream_buffer_properties.py sha256=040fea5437b6e55e70cb3eb6117157049faab504a89c7a8c4f256b180da14f7e bytes=942 -->
## FILE: tests/component/task/test_in_stream_buffer_properties.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/task/test_in_stream_buffer_properties.py`
- sha256: `040fea5437b6e55e70cb3eb6117157049faab504a89c7a8c4f256b180da14f7e`
- bytes: 942

````python
from nidaqmx.constants import SampleTimingType


def test___ai_task___set_int32_property___value_is_set(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.samp_timing_type = SampleTimingType.SAMPLE_CLOCK

    # Setting a valid input buffer size of type int32
    task.in_stream.input_buf_size = 2000000000

    assert task.in_stream.input_buf_size == 2000000000


def test___ai_task___reset_int32_property___value_is_set_to_default(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.samp_timing_type = SampleTimingType.SAMPLE_CLOCK
    default_buffer_size = task.in_stream.input_buf_size
    task.in_stream.input_buf_size = 2000000000

    # Resetting input buffer size
    del task.in_stream.input_buf_size

    assert task.in_stream.input_buf_size == default_buffer_size
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/task/test_in_stream_read_properties.py sha256=55a2b729c7dc68c58df5dbbd4639aab6288c075f0919df540648af6b03d3b3c0 bytes=5256 -->
## FILE: tests/component/task/test_in_stream_read_properties.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/task/test_in_stream_read_properties.py`
- sha256: `55a2b729c7dc68c58df5dbbd4639aab6288c075f0919df540648af6b03d3b3c0`
- bytes: 5256

````python
import pathlib

import pytest

from nidaqmx.constants import OverwriteMode, ReadRelativeTo
from nidaqmx.task import Task


@pytest.fixture()
def ai_task(task, sim_6363_device):
    """Gets AI voltage task."""
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    yield task


def test___ai_task___get_int32_property___returns_default_value(ai_task: Task):
    assert ai_task.in_stream.offset == 0


def test___ai_task___set_int32_property___returns_assigned_value(ai_task: Task):
    ai_task.in_stream.offset = 1

    assert ai_task.in_stream.offset == 1


def test___ai_task___reset_int32_property___returns_default_value(ai_task: Task):
    ai_task.in_stream.offset = 2

    del ai_task.in_stream.offset

    assert ai_task.in_stream.offset == 0


def test___ai_task___get_enum_property___returns_default_value(ai_task: Task):
    assert ai_task.in_stream.relative_to == ReadRelativeTo.CURRENT_READ_POSITION


def test___ai_task___set_enum_property___returns_assigned_value(ai_task: Task):
    ai_task.in_stream.relative_to = ReadRelativeTo.FIRST_SAMPLE

    assert ai_task.in_stream.relative_to == ReadRelativeTo.FIRST_SAMPLE


def test___ai_task___reset_enum_property___returns_default_value(ai_task: Task):
    ai_task.in_stream.relative_to = ReadRelativeTo.FIRST_SAMPLE

    del ai_task.in_stream.relative_to

    assert ai_task.in_stream.relative_to == ReadRelativeTo.CURRENT_READ_POSITION


def test___ai_task___get_float_property___returns_default_value(ai_task: Task):
    assert ai_task.in_stream.sleep_time == 0.001


def test___ai_task___set_float_property___returns_assigned_value(ai_task: Task):
    ai_task.in_stream.sleep_time = 1.5

    assert ai_task.in_stream.sleep_time == 1.5


def test___ai_task___reset_float_property___returns_default_value(ai_task: Task):
    ai_task.in_stream.sleep_time = 3.5

    del ai_task.in_stream.sleep_time

    assert ai_task.in_stream.sleep_time == 0.001


def test___ai_task___get_uint32_property___returns_default_value(ai_task: Task):
    assert ai_task.in_stream.num_chans == 1


def test___ai_task___set_uint32_property___returns_assigned_value(ai_task: Task):
    ai_task.in_stream.logging_file_write_size = 50000

    assert ai_task.in_stream.logging_file_write_size == 50000


def test___ai_task___reset_uint32_property___returns_default_value(ai_task: Task):
    default_value = ai_task.in_stream.logging_file_write_size
    ai_task.in_stream.logging_file_write_size = 30000

    del ai_task.in_stream.logging_file_write_size

    assert ai_task.in_stream.logging_file_write_size == default_value


def test___ai_task___get_uint64_property___returns_default_value(ai_task: Task):
    assert ai_task.in_stream.logging_file_preallocation_size == 0


def test___ai_task___set_uint64_property___returns_assigned_value(ai_task: Task):
    ai_task.in_stream.logging_file_preallocation_size = 100

    assert ai_task.in_stream.logging_file_preallocation_size == 100


def test___ai_task___reset_uint64_property___returns_default_value(ai_task: Task):
    ai_task.in_stream.logging_file_preallocation_size = 100

    del ai_task.in_stream.logging_file_preallocation_size

    assert ai_task.in_stream.logging_file_preallocation_size == 0


def test___ai_task___get_bool_property___returns_default_value(ai_task: Task):
    assert not ai_task.in_stream.logging_pause


def test___ai_task___set_bool_property___returns_assigned_value(ai_task: Task):
    ai_task.in_stream.logging_pause = True

    assert ai_task.in_stream.logging_pause


def test___ai_task___reset_bool_property___returns_default_value(ai_task: Task):
    ai_task.in_stream.logging_pause = True

    del ai_task.in_stream.logging_pause

    assert not ai_task.in_stream.logging_pause


def test___ai_task___get_string_property___returns_default_value(ai_task: Task):
    assert ai_task.in_stream.logging_file_path is None


def test___ai_task___set_string_property___returns_assigned_value(ai_task: Task):
    ai_task.in_stream.logging_file_path = "TestData.tdms"

    assert ai_task.in_stream.logging_file_path == pathlib.Path("TestData.tdms")


def test___ai_task___set_string_property_none___returns_default_value(ai_task: Task):
    ai_task.in_stream.logging_file_path = None

    assert ai_task.in_stream.logging_file_path is None


def test___ai_task___reset_string_property___returns_default_value(ai_task: Task):
    ai_task.in_stream.logging_file_path = "TestData.tdms"

    del ai_task.in_stream.logging_file_path

    assert ai_task.in_stream.logging_file_path is None


def test___ai_task___get_deprecated_properties___reports_warnings(ai_task: Task):
    with pytest.deprecated_call():
        assert ai_task.in_stream.overwrite == ai_task.in_stream.over_write


def test___ai_task___set_deprecated_properties___reports_warnings(ai_task: Task):
    with pytest.deprecated_call():
        ai_task.in_stream.over_write = OverwriteMode.DO_NOT_OVERWRITE_UNREAD_SAMPLES


def test___ai_task___reset_deprecated_properties___reports_warnings(ai_task: Task):
    with pytest.deprecated_call():
        del ai_task.in_stream.over_write
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/task/test_out_stream.py sha256=2e15b8abfd7e4f262349fb00928b3e71990e12a3e6188a9ac1cbc102b5847efb bytes=1863 -->
## FILE: tests/component/task/test_out_stream.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/task/test_out_stream.py`
- sha256: `2e15b8abfd7e4f262349fb00928b3e71990e12a3e6188a9ac1cbc102b5847efb`
- bytes: 1863

````python
import numpy
import pytest

import nidaqmx
import nidaqmx.system


@pytest.fixture(params=[1, 2])
def ao_task(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device, request: pytest.FixtureRequest
) -> nidaqmx.Task:
    """Returns an analog output task with a varying number of channels."""
    _create_ao_channels(task, sim_6363_device, number_of_channels=request.param)
    return task


def _create_ao_channels(
    task: nidaqmx.Task, device: nidaqmx.system.Device, number_of_channels: int
) -> None:
    """Creates the specified number of analog output channels."""
    for i in range(number_of_channels):
        task.ao_channels.add_ao_voltage_chan(device.ao_physical_chans[i].name)

    # This test assumes the data format is int16.
    assert task.ao_channels.all.ao_resolution == 16


@pytest.mark.parametrize("samples_to_write", [1, 10])
def test___valid_array___write___returns_samples_written(
    ao_task: nidaqmx.Task, samples_to_write: int
) -> None:
    ao_task.out_stream.auto_start = True
    data = numpy.full(ao_task.number_of_channels * samples_to_write, 0x1234, dtype=numpy.int16)

    samples_written = ao_task.out_stream.write(data)

    assert samples_written == samples_to_write


def test___odd_sized_array___write___returns_whole_samples(
    task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device
) -> None:
    _create_ao_channels(task, sim_6363_device, number_of_channels=2)
    task.out_stream.auto_start = True
    data = numpy.full(19, 0x1234, dtype=numpy.int16)

    samples_written = task.out_stream.write(data)

    assert samples_written == 9


def test___out_stream___set_nonexistent_property___raises_exception(task: nidaqmx.Task):
    with pytest.raises(AttributeError):
        task.out_stream.nonexistent_property = "foo"  # type: ignore[attr-defined]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/task/test_out_stream_buffer_properties.py sha256=05345548195cd4a862da8468884d025539c7291c912ca397028029b5e66d1480 bytes=621 -->
## FILE: tests/component/task/test_out_stream_buffer_properties.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/task/test_out_stream_buffer_properties.py`
- sha256: `05345548195cd4a862da8468884d025539c7291c912ca397028029b5e66d1480`
- bytes: 621

````python
import pytest

from nidaqmx.constants import SampleTimingType
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError


def test___ai_task___set_valid_value_to_unsupported_property___unsupported_error_raised(
    task,
    sim_6363_device,
):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.samp_timing_type = SampleTimingType.SAMPLE_CLOCK

    with pytest.raises(DaqError) as exc_info:
        task.out_stream.output_buf_size = 2000

    assert exc_info.value.error_code == DAQmxErrors.ATTRIBUTE_NOT_SUPPORTED_IN_TASK_CONTEXT
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/task/test_out_stream_write_properties.py sha256=e6a901e8511663ef3bbe226f681f9ce7bfe57ddc20cfc008fabefb2721c8d942 bytes=3799 -->
## FILE: tests/component/task/test_out_stream_write_properties.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/task/test_out_stream_write_properties.py`
- sha256: `e6a901e8511663ef3bbe226f681f9ce7bfe57ddc20cfc008fabefb2721c8d942`
- bytes: 3799

````python
import pytest

from nidaqmx.constants import WriteRelativeTo
from nidaqmx.errors import DaqError, DAQmxErrors
from nidaqmx.task import Task


@pytest.fixture()
def ao_task(task, sim_6363_device):
    """Gets AO voltage task."""
    task.ao_channels.add_ao_voltage_chan(sim_6363_device.ao_physical_chans[0].name)
    yield task


def test___ao_task___get_int32_property___returns_default_value(ao_task: Task):
    assert ao_task.out_stream.offset == 0


def test___ao_task___set_int32_property___returns_assigned_value(ao_task: Task):
    ao_task.out_stream.offset = 1

    assert ao_task.out_stream.offset == 1


def test___ao_task___reset_int32_property___returns_default_value(ao_task: Task):
    ao_task.out_stream.offset = 2

    del ao_task.out_stream.offset

    assert ao_task.out_stream.offset == 0


def test___ao_task___get_enum_property___returns_default_value(ao_task: Task):
    assert ao_task.out_stream.relative_to == WriteRelativeTo.CURRENT_WRITE_POSITION


def test___ao_task___set_enum_property___returns_assigned_value(ao_task: Task):
    ao_task.out_stream.relative_to = WriteRelativeTo.FIRST_SAMPLE

    assert ao_task.out_stream.relative_to == WriteRelativeTo.FIRST_SAMPLE


def test___ao_task___reset_enum_property___returns_default_value(ao_task: Task):
    ao_task.out_stream.relative_to = WriteRelativeTo.FIRST_SAMPLE

    del ao_task.out_stream.relative_to

    assert ao_task.out_stream.relative_to == WriteRelativeTo.CURRENT_WRITE_POSITION


def test___ao_task___get_float_property___returns_default_value(ao_task: Task):
    assert ao_task.out_stream.sleep_time == 0.001


def test___ao_task___set_float_property___returns_assigned_value(ao_task: Task):
    ao_task.out_stream.sleep_time = 1

    assert ao_task.out_stream.sleep_time == 1


def test___ao_task___reset_float_property___returns_default_value(ao_task: Task):
    ao_task.out_stream.sleep_time = 3

    del ao_task.out_stream.sleep_time

    assert ao_task.out_stream.sleep_time == 0.001


def test___ao_task___get_uint32_property___returns_default_value(ao_task: Task):
    assert ao_task.out_stream.num_chans == 1


def test___ao_task___get_uint64_property___returns_default_value(ao_task: Task):
    ao_task.start()

    assert ao_task.out_stream.curr_write_pos == 0


@pytest.mark.xfail(reason="https://github.com/ni/nidaqmx-python/issues/833")
@pytest.mark.device_name("aoTester")
def test___ao_current_task___get_bool_property___returns_default_value(task, device):
    task.ao_channels.add_ao_current_chan(device.ao_physical_chans[0].name)
    task.start()

    assert not task.out_stream.open_current_loop_chans_exist


@pytest.mark.xfail(reason="https://github.com/ni/nidaqmx-python/issues/833")
@pytest.mark.grpc_xfail(
    reason="AB#2393824: DAQmx read/write status properties return errors when called from C, Python, or grpc-device.",
    raises=DaqError,
)
@pytest.mark.device_name("aoTester")
def test___ao_current_task___get_string_list_property___returns_default_value(task, device):
    task.ao_channels.add_ao_current_chan(device.ao_physical_chans[0].name)
    task.start()
    _ = task.out_stream.open_current_loop_chans_exist

    assert task.out_stream.open_current_loop_chans == []


@pytest.mark.xfail(reason="https://github.com/ni/nidaqmx-python/issues/833")
@pytest.mark.device_name("aoTester")
def test___ao_current_task__read_property___out_of_order___throws_daqerror(task, device):
    task.ao_channels.add_ao_current_chan(device.ao_physical_chans[0].name)
    task.start()

    with pytest.raises(DaqError) as exc_info:
        _ = task.out_stream.open_current_loop_chans

    assert exc_info.value.error_type == DAQmxErrors.TWO_PART_ATTRIBUTE_CALLED_OUT_OF_ORDER
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/task/test_task_read_ai.py sha256=275006763746fc304c109b659a4bc1f4f7a4597cd421916654997bc6169e84a8 bytes=9970 -->
## FILE: tests/component/task/test_task_read_ai.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/task/test_task_read_ai.py`
- sha256: `275006763746fc304c109b659a4bc1f4f7a4597cd421916654997bc6169e84a8`
- bytes: 9970

````python
from __future__ import annotations

import pytest

import nidaqmx
from nidaqmx.constants import AcquisitionType
from tests.component._analog_utils import (
    POWER_EPSILON,
    AI_VOLTAGE_EPSILON,
    _assert_equal_2d,
    _get_current_setpoint_for_chan,
    _get_voltage_offset_for_chan,
    _get_voltage_setpoint_for_chan,
)


def test___analog_single_channel___read_unset_samples___returns_valid_scalar(
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    data = ai_single_channel_task.read()

    expected = _get_voltage_offset_for_chan(0)
    assert data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


def test___analog_single_channel___read_one_sample___returns_valid_1d_samples(
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    data = ai_single_channel_task.read(1)

    expected = [_get_voltage_offset_for_chan(0)]
    assert data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


def test___analog_single_channel___read_many_sample___returns_valid_1d_samples(
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    samples_to_read = 10

    data = ai_single_channel_task.read(samples_to_read)

    expected = [_get_voltage_offset_for_chan(0) for _ in range(samples_to_read)]
    assert data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


def test___analog_single_channel_finite___read_too_many_sample___returns_valid_1d_samples_truncated(
    ai_single_channel_task: nidaqmx.Task,
) -> None:
    samples_to_acquire = 5
    ai_single_channel_task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=samples_to_acquire
    )
    samples_to_read = 10

    data = ai_single_channel_task.read(samples_to_read)

    expected = [_get_voltage_offset_for_chan(0) for _ in range(samples_to_acquire)]
    assert data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


def test___analog_multi_channel___read_unset_samples___returns_1d_channels(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    num_channels = ai_multi_channel_task.number_of_channels

    data = ai_multi_channel_task.read()

    expected = [_get_voltage_offset_for_chan(chan_index) for chan_index in range(num_channels)]
    assert data == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


def test___analog_multi_channel___read_one_sample___returns_valid_2d_channels_samples(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    num_channels = ai_multi_channel_task.number_of_channels

    data = ai_multi_channel_task.read(1)

    expected = [[_get_voltage_offset_for_chan(chan_index)] for chan_index in range(num_channels)]
    _assert_equal_2d(data, expected, abs=AI_VOLTAGE_EPSILON)


def test___analog_multi_channel___read_many_sample___returns_valid_2d_channels_samples(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10

    data = ai_multi_channel_task.read(samples_to_read)

    expected = [
        [_get_voltage_offset_for_chan(chan_index) for _ in range(samples_to_read)]
        for chan_index in range(num_channels)
    ]
    _assert_equal_2d(data, expected, abs=AI_VOLTAGE_EPSILON)


@pytest.mark.xfail(
    reason="Task.read interprets data incorrectly for short reads - https://github.com/ni/nidaqmx-python/issues/528",
    raises=AssertionError,
)
def test___analog_multi_channel_finite___read_too_many_sample___returns_valid_2d_channels_samples_truncated(
    ai_multi_channel_task: nidaqmx.Task,
) -> None:
    samples_to_acquire = 5
    ai_multi_channel_task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=samples_to_acquire
    )
    num_channels = ai_multi_channel_task.number_of_channels
    samples_to_read = 10

    data = ai_multi_channel_task.read(samples_to_read)

    expected = [
        [_get_voltage_offset_for_chan(chan_index) for _ in range(samples_to_acquire)]
        for chan_index in range(num_channels)
    ]
    _assert_equal_2d(data, expected, abs=AI_VOLTAGE_EPSILON)


def test___power_single_channel___read_unset_samples___returns_valid_scalar(
    pwr_single_channel_task: nidaqmx.Task,
) -> None:
    data = pwr_single_channel_task.read()

    assert data.voltage == pytest.approx(_get_voltage_setpoint_for_chan(0), abs=POWER_EPSILON)
    assert data.current == pytest.approx(_get_current_setpoint_for_chan(0), abs=POWER_EPSILON)


@pytest.mark.xfail(
    reason="Task.read has inconsistent return type between normal AI and power channels - https://github.com/ni/nidaqmx-python/issues/527",
    raises=AttributeError,
)
def test___power_single_channel___read_one_sample___returns_valid_1d_samples(
    pwr_single_channel_task: nidaqmx.Task,
) -> None:
    data = pwr_single_channel_task.read(1)

    assert [d.voltage for d in data] == pytest.approx(
        [_get_voltage_setpoint_for_chan(0)], abs=POWER_EPSILON
    )
    assert [d.current for d in data] == pytest.approx(
        [_get_current_setpoint_for_chan(0)], abs=POWER_EPSILON
    )


def test___power_single_channel___read_many_sample___returns_valid_1d_samples(
    pwr_single_channel_task: nidaqmx.Task,
) -> None:
    samples_to_read = 10

    data = pwr_single_channel_task.read(samples_to_read)

    assert [d.voltage for d in data] == pytest.approx(
        [_get_voltage_setpoint_for_chan(0) for _ in range(samples_to_read)], abs=POWER_EPSILON
    )
    assert [d.current for d in data] == pytest.approx(
        [_get_current_setpoint_for_chan(0) for _ in range(samples_to_read)], abs=POWER_EPSILON
    )


def test___power_single_channel_finite___read_too_many_sample___returns_valid_1d_samples_truncated(
    pwr_single_channel_task: nidaqmx.Task,
) -> None:
    samples_to_acquire = 5
    pwr_single_channel_task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=samples_to_acquire
    )
    samples_to_read = 10

    data = pwr_single_channel_task.read(samples_to_read)

    assert [d.voltage for d in data] == pytest.approx(
        [_get_voltage_setpoint_for_chan(0) for _ in range(samples_to_acquire)], abs=POWER_EPSILON
    )
    assert [d.current for d in data] == pytest.approx(
        [_get_current_setpoint_for_chan(0) for _ in range(samples_to_acquire)], abs=POWER_EPSILON
    )


def test___power_multi_channel___read_unset_samples___returns_valid_1d_channels(
    pwr_multi_channel_task: nidaqmx.Task,
) -> None:
    num_channels = pwr_multi_channel_task.number_of_channels

    data = pwr_multi_channel_task.read(1)

    assert [d.voltage for d in data] == pytest.approx(
        [_get_voltage_setpoint_for_chan(chan_index) for chan_index in range(num_channels)],
        abs=POWER_EPSILON,
    )
    assert [d.current for d in data] == pytest.approx(
        [_get_current_setpoint_for_chan(chan_index) for chan_index in range(num_channels)],
        abs=POWER_EPSILON,
    )


@pytest.mark.xfail(
    reason="Task.read has inconsistent return type between normal AI and power channels - https://github.com/ni/nidaqmx-python/issues/527",
    raises=AttributeError,
)
def test___power_multi_channel___read_one_sample___returns_valid_2d_channels_samples(
    pwr_multi_channel_task: nidaqmx.Task,
) -> None:
    num_channels = pwr_multi_channel_task.number_of_channels

    data = pwr_multi_channel_task.read(1)

    _assert_equal_2d(
        [[e.voltage for e in d] for d in data],
        [[_get_voltage_setpoint_for_chan(chan_index)] for chan_index in range(num_channels)],
        abs=POWER_EPSILON,
    )
    _assert_equal_2d(
        [[e.current for e in d] for d in data],
        [[_get_current_setpoint_for_chan(chan_index)] for chan_index in range(num_channels)],
        abs=POWER_EPSILON,
    )


def test___power_multi_channel___read_many_sample___returns_valid_2d_channels_samples(
    pwr_multi_channel_task: nidaqmx.Task,
) -> None:
    num_channels = pwr_multi_channel_task.number_of_channels
    samples_to_read = 10

    data = pwr_multi_channel_task.read(samples_to_read)

    _assert_equal_2d(
        [[e.voltage for e in d] for d in data],
        [
            [_get_voltage_setpoint_for_chan(chan_index) for _ in range(samples_to_read)]
            for chan_index in range(num_channels)
        ],
        abs=POWER_EPSILON,
    )
    _assert_equal_2d(
        [[e.current for e in d] for d in data],
        [
            [_get_current_setpoint_for_chan(chan_index) for _ in range(samples_to_read)]
            for chan_index in range(num_channels)
        ],
        abs=POWER_EPSILON,
    )


@pytest.mark.xfail(
    reason="Task.read does not return short reads for multi-channel power - https://github.com/ni/nidaqmx-python/issues/529",
    raises=AssertionError,
)
def test___power_multi_channel_finite___read_too_many_sample___returns_valid_2d_channels_samples_truncated(
    pwr_multi_channel_task: nidaqmx.Task,
) -> None:
    samples_to_acquire = 5
    pwr_multi_channel_task.timing.cfg_samp_clk_timing(
        rate=1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=samples_to_acquire
    )
    num_channels = pwr_multi_channel_task.number_of_channels
    samples_to_read = 10

    data = pwr_multi_channel_task.read(samples_to_read)

    _assert_equal_2d(
        [[e.voltage for e in d] for d in data],
        [
            [_get_voltage_setpoint_for_chan(chan_index) for _ in range(samples_to_acquire)]
            for chan_index in range(num_channels)
        ],
        abs=POWER_EPSILON,
    )
    _assert_equal_2d(
        [[e.current for e in d] for d in data],
        [
            [_get_current_setpoint_for_chan(chan_index) for _ in range(samples_to_acquire)]
            for chan_index in range(num_channels)
        ],
        abs=POWER_EPSILON,
    )
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/task/test_task_read_waveform_ai.py sha256=9220c9dd3e806326d9619870dc1a58e7699615b7c2d5c97e154f472d213ad87a bytes=6444 -->
## FILE: tests/component/task/test_task_read_waveform_ai.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/task/test_task_read_waveform_ai.py`
- sha256: `9220c9dd3e806326d9619870dc1a58e7699615b7c2d5c97e154f472d213ad87a`
- bytes: 6444

````python
from __future__ import annotations

import pytest
from nitypes.waveform import AnalogWaveform

import nidaqmx
from nidaqmx.constants import READ_ALL_AVAILABLE
from tests.component._analog_utils import (
    AI_VOLTAGE_EPSILON,
    _get_voltage_offset_for_chan,
)


def test___analog_single_channel___read_waveform___returns_valid_waveform(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    waveform = ai_single_channel_task_with_timing.read_waveform()

    assert isinstance(waveform, AnalogWaveform)
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.sample_count == 50
    assert waveform.raw_data[0] == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


def test___analog_single_channel___read_waveform_one_sample___returns_waveform_with_one_sample(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    waveform = ai_single_channel_task_with_timing.read_waveform(1)

    assert isinstance(waveform, AnalogWaveform)
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.sample_count == 1
    assert waveform.raw_data[0] == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


def test___analog_single_channel___read_waveform_many_sample___returns_waveform_with_many_samples(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    samples_to_read = 10

    waveform = ai_single_channel_task_with_timing.read_waveform(samples_to_read)

    assert isinstance(waveform, AnalogWaveform)
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.sample_count == samples_to_read
    assert waveform.raw_data[0] == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


def test___analog_single_channel_finite___read_waveform_too_many_samples___returns_waveform_with_correct_number_of_samples(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    samples_to_read = 100
    samples_available = 50

    waveform = ai_single_channel_task_with_timing.read_waveform(samples_to_read)

    assert isinstance(waveform, AnalogWaveform)
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.sample_count == samples_available
    assert waveform.raw_data[0] == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


def test___analog_multi_channel___read_waveform___returns_valid_waveforms(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    num_channels = ai_multi_channel_task_with_timing.number_of_channels

    waveforms = ai_multi_channel_task_with_timing.read_waveform()

    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert all(isinstance(waveform, AnalogWaveform) for waveform in waveforms)
    for chan_index, waveform in enumerate(waveforms):
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.sample_count == 50
        assert waveform.raw_data[0] == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


def test___analog_multi_channel___read_waveform_one_sample___returns_waveforms_with_single_sample(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    num_channels = ai_multi_channel_task_with_timing.number_of_channels

    waveforms = ai_multi_channel_task_with_timing.read_waveform(1)

    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert all(isinstance(waveform, AnalogWaveform) for waveform in waveforms)
    for chan_index, waveform in enumerate(waveforms):
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.sample_count == 1
        assert waveform.raw_data[0] == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


def test___analog_multi_channel___read_waveform_many_samples___returns_waveforms_with_many_samples(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    num_channels = ai_multi_channel_task_with_timing.number_of_channels
    samples_to_read = 10

    waveforms = ai_multi_channel_task_with_timing.read_waveform(samples_to_read)

    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert all(isinstance(waveform, AnalogWaveform) for waveform in waveforms)
    for chan_index, waveform in enumerate(waveforms):
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.sample_count == samples_to_read
        assert waveform.raw_data[0] == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


def test___analog_multi_channel_finite___read_waveform_too_many_samples___returns_waveforms_with_correct_number_of_samples(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    samples_to_read = 100
    samples_available = 50

    waveforms = ai_multi_channel_task_with_timing.read_waveform(samples_to_read)

    assert isinstance(waveforms, list)
    assert len(waveforms) == ai_multi_channel_task_with_timing.number_of_channels
    assert all(isinstance(waveform, AnalogWaveform) for waveform in waveforms)
    for chan_index, waveform in enumerate(waveforms):
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.sample_count == samples_available
        assert waveform.raw_data[0] == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


def test___analog_single_channel___read_waveform_read_all_available___returns_valid_waveform(
    ai_single_channel_task_with_timing: nidaqmx.Task,
) -> None:
    waveform = ai_single_channel_task_with_timing.read_waveform(READ_ALL_AVAILABLE)

    assert isinstance(waveform, AnalogWaveform)
    expected = _get_voltage_offset_for_chan(0)
    assert waveform.sample_count == 50
    assert waveform.raw_data[0] == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)


def test___analog_multi_channel___read_waveform_read_all_available___returns_valid_waveforms(
    ai_multi_channel_task_with_timing: nidaqmx.Task,
) -> None:
    waveforms = ai_multi_channel_task_with_timing.read_waveform(READ_ALL_AVAILABLE)

    assert isinstance(waveforms, list)
    assert len(waveforms) == ai_multi_channel_task_with_timing.number_of_channels
    assert all(isinstance(waveform, AnalogWaveform) for waveform in waveforms)
    for chan_index, waveform in enumerate(waveforms):
        expected = _get_voltage_offset_for_chan(chan_index)
        assert waveform.sample_count == 50
        assert waveform.raw_data[0] == pytest.approx(expected, abs=AI_VOLTAGE_EPSILON)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/task/test_task_read_waveform_di.py sha256=92bb37439a06f88c569428cd8ceeda86b3bd2dc507cb759a7f95cd65c37b521a bytes=10708 -->
## FILE: tests/component/task/test_task_read_waveform_di.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/task/test_task_read_waveform_di.py`
- sha256: `92bb37439a06f88c569428cd8ceeda86b3bd2dc507cb759a7f95cd65c37b521a`
- bytes: 10708

````python
from __future__ import annotations

from nitypes.waveform import DigitalWaveform

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import READ_ALL_AVAILABLE
from tests.component._digital_utils import (
    _get_expected_data_for_line,
    _get_waveform_data,
    _get_waveform_port_data,
    _validate_waveform_signals,
)


def test___digital_single_channel___read_waveform___returns_valid_waveform(
    di_single_channel_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    waveform = di_single_channel_timing_task.read_waveform()

    assert isinstance(waveform, DigitalWaveform)
    assert _get_waveform_data(waveform) == _get_expected_data_for_line(50, 0)
    _validate_waveform_signals(sim_6363_device, waveform, [0])


def test___digital_single_channel___read_waveform_one_sample___returns_waveform_with_one_sample(
    di_single_channel_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    waveform = di_single_channel_timing_task.read_waveform(1)

    assert isinstance(waveform, DigitalWaveform)
    assert _get_waveform_data(waveform) == _get_expected_data_for_line(1, 0)
    _validate_waveform_signals(sim_6363_device, waveform, [0])


def test___digital_single_channel___read_waveform_many_sample___returns_waveform_with_many_samples(
    di_single_channel_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    samples_to_read = 10

    waveform = di_single_channel_timing_task.read_waveform(samples_to_read)

    assert isinstance(waveform, DigitalWaveform)
    assert _get_waveform_data(waveform) == _get_expected_data_for_line(samples_to_read, 0)
    _validate_waveform_signals(sim_6363_device, waveform, [0])


def test___digital_single_channel___read_waveform_too_many_samples___returns_waveform_with_correct_number_of_samples(
    di_single_channel_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    samples_to_read = 100
    samples_available = 50

    waveform = di_single_channel_timing_task.read_waveform(samples_to_read)

    assert isinstance(waveform, DigitalWaveform)
    assert waveform.sample_count == samples_available
    assert _get_waveform_data(waveform) == _get_expected_data_for_line(samples_available, 0)
    _validate_waveform_signals(sim_6363_device, waveform, [0])


def test___digital_single_channel___read_waveform_lines_and_port___returns_valid_waveform(
    di_single_chan_lines_and_port_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    samples_to_read = 10

    waveform = di_single_chan_lines_and_port_task.read_waveform(samples_to_read)

    assert _get_waveform_port_data(waveform) == [
        0b00000000000,
        0b10000000001,
        0b01000000010,
        0b11000000011,
        0b00100000100,
        0b10100000101,
        0b01100000110,
        0b11100000111,
        0b00000001000,
        0b10000001001,
    ]
    assert waveform.sample_count == samples_to_read
    assert waveform.channel_name == di_single_chan_lines_and_port_task.di_channels[0].name
    _validate_waveform_signals(sim_6363_device, waveform, [32, 33, 34, 35, 36, 37, 38, 39, 2, 1, 0])


def test___digital_multi_channel___read_waveform___returns_valid_waveforms(
    di_multi_channel_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    num_channels = di_multi_channel_timing_task.number_of_channels

    waveforms = di_multi_channel_timing_task.read_waveform()

    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert all(isinstance(waveform, DigitalWaveform) for waveform in waveforms)
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(50, chan)
        _validate_waveform_signals(sim_6363_device, waveform, [chan])


def test___digital_multi_channel___read_waveform_one_sample___returns_waveforms_with_single_sample(
    di_multi_channel_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    num_channels = di_multi_channel_timing_task.number_of_channels

    waveforms = di_multi_channel_timing_task.read_waveform(1)

    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert all(isinstance(waveform, DigitalWaveform) for waveform in waveforms)
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(1, chan)
        _validate_waveform_signals(sim_6363_device, waveform, [chan])


def test___digital_multi_channel___read_waveform_many_samples___returns_waveforms_with_many_samples(
    di_multi_channel_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    num_channels = di_multi_channel_timing_task.number_of_channels
    samples_to_read = 10

    waveforms = di_multi_channel_timing_task.read_waveform(samples_to_read)

    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert all(isinstance(waveform, DigitalWaveform) for waveform in waveforms)
    for chan, waveform in enumerate(waveforms):
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(10, chan)
        _validate_waveform_signals(sim_6363_device, waveform, [chan])


def test___digital_multi_channel___read_waveform_too_many_samples___returns_waveforms_with_correct_number_of_samples(
    di_multi_channel_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    num_channels = di_multi_channel_timing_task.number_of_channels
    samples_to_read = 100
    samples_available = 50

    waveforms = di_multi_channel_timing_task.read_waveform(samples_to_read)

    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert all(isinstance(waveform, DigitalWaveform) for waveform in waveforms)
    for chan, waveform in enumerate(waveforms):
        assert waveform.sample_count == samples_available
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(samples_available, chan)
        _validate_waveform_signals(sim_6363_device, waveform, [chan])


def test___digital_multi_channel___read_waveform_different_lines___returns_valid_waveforms(
    di_multi_chan_diff_lines_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    num_channels = di_multi_chan_diff_lines_timing_task.number_of_channels
    samples_to_read = 10

    waveforms = di_multi_chan_diff_lines_timing_task.read_waveform(samples_to_read)

    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert num_channels == 3
    assert all(isinstance(waveform, DigitalWaveform) for waveform in waveforms)
    assert _get_waveform_data(waveforms[0]) == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    assert waveforms[0].channel_name == di_multi_chan_diff_lines_timing_task.di_channels[0].name
    _validate_waveform_signals(sim_6363_device, waveforms[0], [0])
    assert _get_waveform_data(waveforms[1]) == [0, 0, 1, 1, 2, 2, 3, 3, 0, 0]
    assert waveforms[1].channel_name == di_multi_chan_diff_lines_timing_task.di_channels[1].name
    _validate_waveform_signals(sim_6363_device, waveforms[1], [2, 1])
    assert _get_waveform_data(waveforms[2]) == [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
    assert waveforms[2].channel_name == di_multi_chan_diff_lines_timing_task.di_channels[2].name
    _validate_waveform_signals(sim_6363_device, waveforms[2], [6, 5, 4, 3])


def test___digital_multi_channel___read_waveform_lines_and_port___returns_valid_waveforms(
    di_multi_chan_lines_and_port_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    num_channels = di_multi_chan_lines_and_port_task.number_of_channels
    samples_to_read = 10

    waveforms = di_multi_chan_lines_and_port_task.read_waveform(samples_to_read)

    assert num_channels == 4
    assert isinstance(waveforms, list)
    assert len(waveforms) == num_channels
    assert _get_waveform_data(waveforms[0]) == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    assert waveforms[0].sample_count == samples_to_read
    assert waveforms[0].channel_name == di_multi_chan_lines_and_port_task.di_channels[0].name
    _validate_waveform_signals(sim_6363_device, waveforms[0], [0])
    assert _get_waveform_data(waveforms[1]) == [0, 0, 1, 1, 2, 2, 3, 3, 0, 0]
    assert waveforms[1].sample_count == samples_to_read
    assert waveforms[1].channel_name == di_multi_chan_lines_and_port_task.di_channels[1].name
    _validate_waveform_signals(sim_6363_device, waveforms[1], [2, 1])
    assert _get_waveform_data(waveforms[2]) == [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
    assert waveforms[2].sample_count == samples_to_read
    assert waveforms[2].channel_name == di_multi_chan_lines_and_port_task.di_channels[2].name
    _validate_waveform_signals(sim_6363_device, waveforms[2], [6, 5, 4, 3])
    assert _get_waveform_port_data(waveforms[3]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert waveforms[3].sample_count == samples_to_read
    assert waveforms[3].channel_name == di_multi_chan_lines_and_port_task.di_channels[3].name
    _validate_waveform_signals(sim_6363_device, waveforms[3], range(32, 40))


def test___digital_single_channel___read_waveform_read_all_available___returns_valid_waveform(
    di_single_channel_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    waveform = di_single_channel_timing_task.read_waveform(READ_ALL_AVAILABLE)

    assert isinstance(waveform, DigitalWaveform)
    assert waveform.sample_count == 50
    assert _get_waveform_data(waveform) == _get_expected_data_for_line(waveform.sample_count, 0)
    _validate_waveform_signals(sim_6363_device, waveform, [0])


def test___digital_multi_channel___read_waveform_read_all_available___returns_valid_waveforms(
    di_multi_channel_timing_task: nidaqmx.Task,
    sim_6363_device: nidaqmx.system.Device,
) -> None:
    waveforms = di_multi_channel_timing_task.read_waveform(READ_ALL_AVAILABLE)

    assert isinstance(waveforms, list)
    assert len(waveforms) == di_multi_channel_timing_task.number_of_channels
    assert all(isinstance(waveform, DigitalWaveform) for waveform in waveforms)
    for chan, waveform in enumerate(waveforms):
        assert waveform.sample_count == 50
        assert _get_waveform_data(waveform) == _get_expected_data_for_line(
            waveform.sample_count, chan
        )
        _validate_waveform_signals(sim_6363_device, waveform, [chan])
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/task/test_task_write_waveform_ao.py sha256=819f8a0b0f576a985fb760b58b9dbe879b9e79d6384c14fb4728d32db5f2464e bytes=14475 -->
## FILE: tests/component/task/test_task_write_waveform_ao.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/task/test_task_write_waveform_ao.py`
- sha256: `819f8a0b0f576a985fb760b58b9dbe879b9e79d6384c14fb4728d32db5f2464e`
- bytes: 14475

````python
from __future__ import annotations

import numpy as np
import pytest

import nidaqmx
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, FeatureNotSupportedError
from tests.component._analog_utils import (
    AO_VOLTAGE_EPSILON,
    _create_constant_waveform,
    _create_float32_ramp_waveform,
    _create_linear_ramp_waveform,
    _create_non_contiguous_waveform,
    _create_scaled_int32_ramp_waveform,
    _get_approx_final_value,
    _setup_synchronized_multi_channel_waveform_tasks,
    _setup_synchronized_waveform_tasks,
)


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
def test___task___write_waveform_feature_disabled___raises_feature_not_supported_error(
    ao_single_channel_task: nidaqmx.Task,
) -> None:
    waveform = _create_constant_waveform(10)

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        ao_single_channel_task.write_waveform(waveform)

    error_message = exc_info.value.args[0]
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message
    assert "NIDAQMX_ENABLE_WAVEFORM_SUPPORT" in error_message


def test___task___write_linear_ramp_waveform___output_matches_final_value(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveform = _create_linear_ramp_waveform(num_samples, 0.0, 1.0)

    samples_written = ao_single_channel_task.write_waveform(waveform)

    assert samples_written == num_samples
    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


def test___task___write_waveform_as_list___output_matches_final_value(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveform = _create_linear_ramp_waveform(num_samples, 0.0, 1.0)

    samples_written = ao_single_channel_task.write_waveform([waveform])

    assert samples_written == num_samples
    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


def test___task___write_waveform_with_write___output_matches_final_value(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveform = _create_linear_ramp_waveform(num_samples, 0.0, 1.0)

    samples_written = ao_single_channel_task.write([waveform])

    assert samples_written == num_samples
    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


def test___task___write_waveform_with_auto_start___output_matches_final_value(
    ao_single_channel_task_with_timing: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveform = _create_linear_ramp_waveform(num_samples, 0.0, 1.0)

    samples_written = ao_single_channel_task_with_timing.write_waveform(waveform, auto_start=True)

    assert samples_written == num_samples
    ao_single_channel_task_with_timing.wait_until_done(timeout=2.0)
    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


def test___task_with_multiple_channels___write_single_channel_waveform___raises_daq_error(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    single_channel_waveform = _create_constant_waveform(10)

    with pytest.raises(nidaqmx.errors.DaqError) as exc_info:
        ao_multi_channel_task.write_waveform(single_channel_waveform)

    error_message = exc_info.value.args[0]
    assert (
        "Write cannot be performed, because the number of channels in the data does not match the number of channels in the task"
        in error_message
    )


def test___task___write_waveform_with_float32_dtype___output_matches_final_value(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveform = _create_float32_ramp_waveform(num_samples, 0.0, 1.0)

    samples_written = ao_single_channel_task.write_waveform(waveform)

    assert samples_written == num_samples
    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


def test___task___write_waveform_with_scaling___output_matches_final_value(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveform = _create_scaled_int32_ramp_waveform(num_samples)

    samples_written = ao_single_channel_task.write_waveform(waveform)

    assert samples_written == num_samples
    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


def test___task___write_waveform_with_non_contiguous_data___output_matches_final_value(
    ao_single_channel_task: nidaqmx.Task,
    ai_single_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveform = _create_non_contiguous_waveform(num_samples, -0.0, 0.1)

    samples_written = ao_single_channel_task.write_waveform(waveform)

    assert samples_written == num_samples
    actual_value = ai_single_channel_loopback_task.read()
    assert actual_value == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


def test___task___write_waveform_with_timing___all_samples_match_waveform_data(
    generate_task,
    real_x_series_multiplexed_device: nidaqmx.system.Device,
) -> None:
    num_samples = 50
    sample_rate = 1000.0
    voltage_range = (-5.0, 5.0)
    ao_task, ai_task, sample_clk_task, _ = _setup_synchronized_waveform_tasks(
        generate_task, real_x_series_multiplexed_device, num_samples, sample_rate, voltage_range
    )
    waveform = _create_linear_ramp_waveform(num_samples, -4.0, 4.0)

    ao_task.write_waveform(waveform)

    ai_task.start()
    ao_task.start()
    sample_clk_task.start()
    actual_values = ai_task.read(number_of_samples_per_channel=num_samples, timeout=2.0)
    np.testing.assert_allclose(actual_values, waveform.scaled_data, atol=AO_VOLTAGE_EPSILON)


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
def test___task___write_waveforms_feature_disabled___raises_feature_not_supported_error(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    num_samples = 10
    waveforms = [
        _create_constant_waveform(num_samples),
        _create_constant_waveform(num_samples),
    ]

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        ao_multi_channel_task.write_waveform(waveforms)

    error_message = exc_info.value.args[0]
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message


def test___task___write_waveforms___output_matches_final_values(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveforms = [
        _create_linear_ramp_waveform(num_samples, 0.0, 0.5),
        _create_linear_ramp_waveform(num_samples, 0.5, 1.0),
    ]

    samples_written = ao_multi_channel_task.write_waveform(waveforms)

    assert samples_written == num_samples
    actual_values = ai_multi_channel_loopback_task.read()
    for i, waveform in enumerate(waveforms):
        assert actual_values[i] == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


def test___task___write_waveforms_with_write___output_matches_final_values(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveforms = [
        _create_linear_ramp_waveform(num_samples, 0.0, 0.5),
        _create_linear_ramp_waveform(num_samples, 0.5, 1.0),
    ]

    samples_written = ao_multi_channel_task.write(waveforms)

    assert samples_written == num_samples
    actual_values = ai_multi_channel_loopback_task.read()
    for i, waveform in enumerate(waveforms):
        assert actual_values[i] == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


def test___task___write_waveforms_with_different_formulas___output_matches_final_values(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveforms = [
        _create_constant_waveform(num_samples),
        _create_linear_ramp_waveform(num_samples, 0.1, 0.7),
    ]

    samples_written = ao_multi_channel_task.write_waveform(waveforms)

    assert samples_written == num_samples
    actual_values = ai_multi_channel_loopback_task.read()
    for i, waveform in enumerate(waveforms):
        assert actual_values[i] == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


def test___task_with_single_channel___write_multiple_waveforms___raises_daq_error(
    ao_single_channel_task: nidaqmx.Task,
) -> None:
    num_samples = 10
    waveforms = [
        _create_constant_waveform(num_samples),
        _create_constant_waveform(num_samples),
    ]

    with pytest.raises(nidaqmx.errors.DaqError) as exc_info:
        ao_single_channel_task.write_waveform(waveforms)

    error_message = exc_info.value.args[0]
    assert (
        "Write cannot be performed, because the number of channels in the data does not match the number of channels in the task"
        in error_message
    )


def test___task___write_waveform_and_array___raises_value_error(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    mixed_data = [_create_constant_waveform(10), [1.0, 2.0, 3.0]]

    with pytest.raises(ValueError) as exc_info:
        ao_multi_channel_task.write(mixed_data)

    error_message = exc_info.value.args[0]
    assert (
        "setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions."
        in error_message
    )


def test___task___write_waveforms_with_different_lengths___raises_error(
    ao_multi_channel_task: nidaqmx.Task,
) -> None:
    waveforms_different_lengths = [_create_constant_waveform(10), _create_constant_waveform(20)]

    with pytest.raises(ValueError) as exc_info:
        ao_multi_channel_task.write_waveform(waveforms_different_lengths)

    error_message = exc_info.value.args[0]
    assert "The waveforms must all have the same sample count." in error_message


def test___task___write_waveforms_with_auto_start___output_matches_final_values(
    ao_multi_channel_task_with_timing: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 100
    waveforms = [
        _create_linear_ramp_waveform(num_samples, 0.0, 0.5),
        _create_linear_ramp_waveform(num_samples, 0.5, 1.0),
    ]

    samples_written = ao_multi_channel_task_with_timing.write(waveforms, auto_start=True)

    assert samples_written == num_samples
    ao_multi_channel_task_with_timing.wait_until_done(timeout=2.0)
    actual_values = ai_multi_channel_loopback_task.read()
    for i, waveform in enumerate(waveforms):
        assert actual_values[i] == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


def test___task___write_waveforms_with_float32_dtype___output_matches_final_values(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 200
    waveforms = [
        _create_float32_ramp_waveform(num_samples, 0.0, 0.1),
        _create_float32_ramp_waveform(num_samples, 0.1, 0.2),
    ]

    samples_written = ao_multi_channel_task.write_waveform(waveforms)

    assert samples_written == num_samples
    actual_values = ai_multi_channel_loopback_task.read()
    for i, waveform in enumerate(waveforms):
        assert actual_values[i] == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


def test___task___write_waveforms_with_scaling___output_matches_final_values(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveforms = [
        _create_scaled_int32_ramp_waveform(num_samples),
        _create_scaled_int32_ramp_waveform(num_samples),
    ]

    samples_written = ao_multi_channel_task.write_waveform(waveforms)

    assert samples_written == num_samples
    actual_values = ai_multi_channel_loopback_task.read()
    for i, waveform in enumerate(waveforms):
        assert actual_values[i] == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


def test___task___write_waveforms_with_non_contiguous_data___output_matches_final_values(
    ao_multi_channel_task: nidaqmx.Task,
    ai_multi_channel_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveforms = [
        _create_non_contiguous_waveform(num_samples, 0.0, 0.05),
        _create_non_contiguous_waveform(num_samples, 0.05, 0.1),
    ]

    samples_written = ao_multi_channel_task.write_waveform(waveforms)

    assert samples_written == num_samples
    actual_values = ai_multi_channel_loopback_task.read()
    for i, waveform in enumerate(waveforms):
        assert actual_values[i] == _get_approx_final_value(waveform, AO_VOLTAGE_EPSILON)


def test___task___write_waveforms_with_timing___all_samples_match_waveform_data(
    generate_task,
    real_x_series_multiplexed_device: nidaqmx.system.Device,
) -> None:
    num_channels = 2
    num_samples = 50
    sample_rate = 1000.0
    voltage_range = (-5.0, 5.0)
    ao_task, ai_task, sample_clk_task, _ = _setup_synchronized_multi_channel_waveform_tasks(
        generate_task,
        real_x_series_multiplexed_device,
        num_channels,
        num_samples,
        sample_rate,
        voltage_range,
    )
    waveforms = [
        _create_linear_ramp_waveform(num_samples, 0.0, 0.5),
        _create_linear_ramp_waveform(num_samples, 0.5, 1.0),
    ]

    ao_task.write_waveform(waveforms)

    ai_task.start()
    ao_task.start()
    sample_clk_task.start()
    actual_values = ai_task.read(number_of_samples_per_channel=num_samples, timeout=2.0)
    for chan_index in range(num_channels):
        np.testing.assert_allclose(
            actual_values[chan_index], waveforms[chan_index].scaled_data, atol=AO_VOLTAGE_EPSILON
        )
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/task/test_task_write_waveform_do.py sha256=0eecc2c8b18375052383dc8b38ace4a641651de328eb7edd97ee3bd21578f644 bytes=21122 -->
## FILE: tests/component/task/test_task_write_waveform_do.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/task/test_task_write_waveform_do.py`
- sha256: `0eecc2c8b18375052383dc8b38ace4a641651de328eb7edd97ee3bd21578f644`
- bytes: 21122

````python
from __future__ import annotations

import numpy
import pytest

import nidaqmx
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, FeatureNotSupportedError
from nidaqmx.errors import DaqError
from tests.component._digital_utils import (
    _create_digital_waveform,
    _create_digital_waveform_uint8,
    _create_non_contiguous_digital_waveform,
    _create_waveform_for_line,
    _create_waveforms_for_mixed_lines,
    _get_digital_data,
    _get_waveform_data,
    _get_waveform_port_data,
)


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
def test___task___write_waveform_feature_disabled___raises_feature_not_supported_error(
    do_single_line_task: nidaqmx.Task,
) -> None:
    waveform = _create_digital_waveform_uint8(10)

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        do_single_line_task.write_waveform(waveform)

    error_message = exc_info.value.args[0]
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message
    assert "NIDAQMX_ENABLE_WAVEFORM_SUPPORT" in error_message


def test___task___write_waveform_single_line___outputs_match_final_values(
    do_single_line_task: nidaqmx.Task,
    di_single_line_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 20):
        num_samples = i
        waveform = _create_digital_waveform_uint8(num_samples, 1)

        samples_written = do_single_line_task.write_waveform(waveform)

        assert samples_written == num_samples
        actual_value = di_single_line_loopback_task.read()
        assert actual_value == _get_waveform_data(waveform)[i - 1]


def test___task___write_waveform_single_line_with_write___outputs_match_final_values(
    do_single_line_task: nidaqmx.Task,
    di_single_line_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 20):
        num_samples = i
        waveform = _create_digital_waveform_uint8(num_samples, 1)

        samples_written = do_single_line_task.write(waveform)

        assert samples_written == num_samples
        actual_value = di_single_line_loopback_task.read()
        assert actual_value == _get_waveform_data(waveform)[i - 1]


def test___task___write_waveform_single_line_with_auto_start___output_matches_final_value(
    do_single_line_task_with_timing: nidaqmx.Task,
    di_single_line_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    waveform = _create_digital_waveform_uint8(num_samples, 1)

    samples_written = do_single_line_task_with_timing.write_waveform(waveform, auto_start=True)

    assert samples_written == num_samples
    do_single_line_task_with_timing.wait_until_done(timeout=2.0)
    actual_value = di_single_line_loopback_task.read()
    assert actual_value == _get_waveform_data(waveform)[-1]


def test___task___write_waveform_single_line_with_non_contiguous_data___outputs_match_final_values(
    do_single_line_task: nidaqmx.Task,
    di_single_line_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(2, 20):
        num_samples = i
        waveform = _create_non_contiguous_digital_waveform(num_samples, 0, 1)

        samples_written = do_single_line_task.write_waveform(waveform)

        assert samples_written == num_samples
        actual_value = di_single_line_loopback_task.read()
        assert actual_value == _get_waveform_data(waveform)[i - 1]


@pytest.mark.parametrize(
    "dtype",
    [
        numpy.bool,
        numpy.int8,
        numpy.uint8,
    ],
)
def test___task___write_waveform_single_line_all_dtypes___outputs_match_final_values(
    do_single_line_task: nidaqmx.Task,
    di_single_line_loopback_task: nidaqmx.Task,
    dtype,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 10):
        num_samples = i
        waveform = _create_digital_waveform(num_samples, 1, dtype=dtype)

        samples_written = do_single_line_task.write_waveform(waveform)

        assert samples_written == num_samples
        assert di_single_line_loopback_task.read() == _get_waveform_data(waveform)[i - 1]


def test___task___write_waveform_single_line_signal_count_mismatch___raises_daq_error(
    do_single_line_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    num_lines = 3
    waveform = _create_digital_waveform_uint8(num_samples, num_lines)

    with pytest.raises(DaqError) as exc_info:
        do_single_line_task.write_waveform(waveform)

    error_message = exc_info.value.args[0]
    assert (
        "Specified read or write operation failed, because the number of lines in the data"
        in error_message
    )


def test___task___write_waveform_multi_line___outputs_match_final_values(
    do_single_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 20):
        num_samples = i
        num_lines = 8
        waveform = _create_digital_waveform_uint8(num_samples, num_lines)

        samples_written = do_single_channel_multi_line_task.write_waveform(waveform)

        assert samples_written == num_samples
        actual_value = di_multi_line_loopback_task.read()
        assert actual_value == _get_waveform_data(waveform)[i - 1]


def test___task___write_waveform_multi_line_with_write___outputs_match_final_values(
    do_single_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 20):
        num_samples = i
        num_lines = 8
        waveform = _create_digital_waveform_uint8(num_samples, num_lines)

        samples_written = do_single_channel_multi_line_task.write(waveform)

        assert samples_written == num_samples
        actual_value = di_multi_line_loopback_task.read()
        assert actual_value == _get_waveform_data(waveform)[i - 1]


def test___task___write_waveform_multi_line_with_auto_start___output_matches_final_value(
    do_single_channel_multi_line_task_with_timing: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    num_lines = 8
    waveform = _create_digital_waveform_uint8(num_samples, num_lines)

    samples_written = do_single_channel_multi_line_task_with_timing.write_waveform(
        waveform, auto_start=True
    )

    assert samples_written == num_samples
    do_single_channel_multi_line_task_with_timing.wait_until_done(timeout=2.0)
    actual_value = di_multi_line_loopback_task.read()
    assert actual_value == _get_waveform_data(waveform)[-1]


def test___task___write_waveform_multi_line_with_non_contiguous_data___outputs_match_final_values(
    do_single_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(2, 20):
        num_samples = i
        num_lines = 8
        waveform = _create_non_contiguous_digital_waveform(num_samples, 0, num_lines)

        samples_written = do_single_channel_multi_line_task.write_waveform(waveform)

        assert samples_written == num_samples
        actual_value = di_multi_line_loopback_task.read()
        assert actual_value == _get_waveform_data(waveform)[i - 1]


@pytest.mark.parametrize(
    "dtype",
    [
        numpy.bool,
        numpy.int8,
        numpy.uint8,
    ],
)
def test___task___write_waveform_multi_line_all_dtypes___outputs_match_final_values(
    do_single_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
    dtype,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 10):
        num_samples = i
        num_lines = 8
        waveform = _create_digital_waveform(num_samples, num_lines, dtype=dtype)

        samples_written = do_single_channel_multi_line_task.write_waveform(waveform)

        assert samples_written == num_samples
        assert di_multi_line_loopback_task.read() == _get_waveform_data(waveform)[i - 1]


def test___task___write_waveform_multi_line_signal_count_mismatch___raises_daq_error(
    do_single_channel_multi_line_task: nidaqmx.Task,
) -> None:
    num_samples = 20
    num_lines = 1
    waveform = _create_digital_waveform_uint8(num_samples, num_lines)

    with pytest.raises(DaqError) as exc_info:
        do_single_channel_multi_line_task.write_waveform(waveform)

    error_message = exc_info.value.args[0]
    assert (
        "Specified read or write operation failed, because the number of lines in the data"
        in error_message
    )


def test___task___write_waveform_port_uint8___outputs_match_final_values(
    do_port1_task: nidaqmx.Task,
    di_port1_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 20):
        num_samples = i
        num_lines = 8
        waveform = _create_digital_waveform_uint8(num_samples, num_lines)

        samples_written = do_port1_task.write_waveform(waveform)

        assert samples_written == num_samples
        actual_value = di_port1_loopback_task.read()
        assert actual_value == _get_waveform_port_data(waveform)[i - 1]


def test___task___write_waveform_port_uint32___outputs_match_final_values(
    do_port0_task: nidaqmx.Task,
    di_port0_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 20):
        num_samples = i
        num_lines = 32
        waveform = _create_digital_waveform_uint8(num_samples, num_lines)

        samples_written = do_port0_task.write_waveform(waveform)

        assert samples_written == num_samples
        actual_value = di_port0_loopback_task.read()
        assert actual_value == _get_waveform_port_data(waveform)[i - 1]


@pytest.mark.disable_feature_toggle(WAVEFORM_SUPPORT)
def test___task___write_waveforms_feature_disabled___raises_feature_not_supported_error(
    do_multi_channel_multi_line_task: nidaqmx.Task,
) -> None:
    waveforms = [_create_digital_waveform_uint8(20), _create_digital_waveform_uint8(20)]

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        do_multi_channel_multi_line_task.write_waveform(waveforms)

    error_message = exc_info.value.args[0]
    assert "WAVEFORM_SUPPORT feature is not supported" in error_message
    assert "NIDAQMX_ENABLE_WAVEFORM_SUPPORT" in error_message


def test___task___write_waveforms_single_lines___outputs_match_final_values(
    do_multi_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 50):
        num_samples = i
        num_channels = 8
        waveforms = [_create_waveform_for_line(num_samples, chan) for chan in range(num_channels)]

        samples_written = do_multi_channel_multi_line_task.write_waveform(waveforms)

        assert samples_written == num_samples
        actual_value = di_multi_line_loopback_task.read()
        assert actual_value == i - 1
        assert actual_value == _get_digital_data(num_channels, num_samples)[i - 1]


def test___task___write_waveforms_with_write___outputs_match_final_values(
    do_multi_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 50):
        num_samples = i
        num_channels = 8
        waveforms = [_create_waveform_for_line(num_samples, chan) for chan in range(num_channels)]

        samples_written = do_multi_channel_multi_line_task.write(waveforms)

        assert samples_written == num_samples
        actual_value = di_multi_line_loopback_task.read()
        assert actual_value == i - 1
        assert actual_value == _get_digital_data(num_channels, num_samples)[i - 1]


def test___task___write_waveforms_with_auto_start___output_matches_final_value(
    do_multi_channel_multi_line_task_with_timing: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    num_samples = 5
    num_channels = 8
    waveforms = [_create_waveform_for_line(num_samples, chan) for chan in range(num_channels)]

    samples_written = do_multi_channel_multi_line_task_with_timing.write_waveform(
        waveforms, auto_start=True
    )

    assert samples_written == num_samples
    do_multi_channel_multi_line_task_with_timing.wait_until_done(timeout=2.0)
    actual_value = di_multi_line_loopback_task.read()
    assert actual_value == _get_digital_data(num_channels, num_samples)[-1]


def test___task___write_waveforms_mixed_lines___outputs_match_final_values(
    do_multi_channel_mixed_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 10):
        num_samples = i
        num_channels = 8
        waveforms = _create_waveforms_for_mixed_lines(num_samples)

        samples_written = do_multi_channel_mixed_line_task.write_waveform(waveforms)

        assert samples_written == num_samples
        actual_value = di_multi_line_loopback_task.read()
        assert actual_value == _get_digital_data(num_channels, num_samples)[i - 1]


def test___task___write_waveforms_ports___outputs_match_final_values(
    do_multi_channel_port_task: nidaqmx.Task,
    di_multi_channel_port_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 50):
        num_samples = i
        num_lines = 8
        waveforms = [
            _create_digital_waveform_uint8(num_samples, num_lines),
            _create_digital_waveform_uint8(num_samples, num_lines, invert=True),
        ]

        samples_written = do_multi_channel_port_task.write_waveform(waveforms)

        assert samples_written == num_samples
        actual_value = di_multi_channel_port_loopback_task.read()
        assert actual_value[0] != actual_value[1]
        assert actual_value == [
            _get_waveform_port_data(waveforms[0])[-1],
            _get_waveform_port_data(waveforms[1])[-1],
        ]


def test___task___write_waveforms_port_and_lines___outputs_match_final_values(
    do_multi_channel_port_and_lines_task: nidaqmx.Task,
    di_multi_channel_port_and_lines_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(1, 50):
        num_samples = i
        num_lines = 8
        waveforms = [
            _create_digital_waveform_uint8(num_samples, num_lines),
            _create_digital_waveform_uint8(num_samples, num_lines, invert=True),
        ]

        samples_written = do_multi_channel_port_and_lines_task.write_waveform(waveforms)

        assert samples_written == num_samples
        actual_value = di_multi_channel_port_and_lines_loopback_task.read()
        assert actual_value == [
            _get_waveform_port_data(waveforms[0])[-1],
            _get_waveform_data(waveforms[1])[-1],
        ]


def test___task___write_waveforms_with_non_contiguous_data___outputs_match_final_values(
    do_multi_channel_multi_line_task: nidaqmx.Task,
    di_multi_line_loopback_task: nidaqmx.Task,
) -> None:
    # Since digital outputs don't have built-in loopback channels like analog outputs,
    # we can only read back the last value. So to verify the whole signal, we must
    # write waveforms of increasing length and verify the final value each time.
    for i in range(2, 50):
        num_samples = i
        num_lines = 8
        waveforms = [
            _create_non_contiguous_digital_waveform(num_samples, first_line=i, num_lines=1)
            for i in range(num_lines)
        ]

        samples_written = do_multi_channel_multi_line_task.write_waveform(waveforms)

        assert samples_written == num_samples
        actual_value = di_multi_line_loopback_task.read()
        assert actual_value == _get_digital_data(num_lines, num_samples)[-1]


def test___task___write_waveforms_with_different_sample_counts___raises_error(
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    num_lines = 8
    waveforms = [
        _create_digital_waveform_uint8(10, num_lines),
        _create_digital_waveform_uint8(11, num_lines),
    ]

    with pytest.raises(ValueError) as exc_info:
        do_multi_channel_port_task.write_waveform(waveforms)

    error_message = exc_info.value.args[0]
    assert "The waveforms must all have the same sample count." in error_message


def test___task___write_waveforms_with_too_many___raises_daq_error(
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    num_lines = 8
    waveforms = [
        _create_digital_waveform_uint8(10, num_lines),
        _create_digital_waveform_uint8(10, num_lines),
        _create_digital_waveform_uint8(10, num_lines),
    ]

    with pytest.raises(DaqError) as exc_info:
        do_multi_channel_port_task.write_waveform(waveforms)

    error_message = exc_info.value.args[0]
    assert "Write cannot be performed, because the number of channels" in error_message


def test___task___write_waveforms_with_too_many_signals___raises_daq_error(
    do_multi_channel_port_task: nidaqmx.Task,
) -> None:
    num_samples = 10
    waveforms = [
        _create_digital_waveform_uint8(num_samples, 8),
        _create_digital_waveform_uint8(num_samples, 10),
    ]

    with pytest.raises(DaqError) as exc_info:
        do_multi_channel_port_task.write_waveform(waveforms)

    error_message = exc_info.value.args[0]
    assert "Specified read or write operation failed, because the number of lines" in error_message
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=tests/component/task/test_timing.py sha256=9690d0bf9778e360d4f86e657857bf9bba7dcd26a824daddfca9c2573a9221b8 bytes=6451 -->
## FILE: tests/component/task/test_timing.py

- repository: `ni/nidaqmx-python`
- source_path: `tests/component/task/test_timing.py`
- sha256: `9690d0bf9778e360d4f86e657857bf9bba7dcd26a824daddfca9c2573a9221b8`
- bytes: 6451

````python
import pytest

from nidaqmx.constants import (
    AcquisitionType,
    Edge,
    Level,
    LineGrouping,
    Polarity,
    SampleTimingType,
)
from nidaqmx.system import Device
from nidaqmx.task import Task


@pytest.fixture()
def sim_6535_di_single_line_task(task: Task, sim_6535_device: Device) -> Task:
    """Gets DI task."""
    task.di_channels.add_di_chan(
        sim_6535_device.di_lines[0].name, line_grouping=LineGrouping.CHAN_FOR_ALL_LINES
    )
    return task


def test___timing___cfg_handshaking___sets_properties(
    sim_6535_di_single_line_task: Task,
) -> None:
    sim_6535_di_single_line_task.timing.cfg_handshaking_timing(
        AcquisitionType.FINITE, samps_per_chan=2000
    )

    assert sim_6535_di_single_line_task.timing.samp_timing_type == SampleTimingType.HANDSHAKE
    assert sim_6535_di_single_line_task.timing.samp_quant_samp_mode == AcquisitionType.FINITE
    assert sim_6535_di_single_line_task.timing.samp_quant_samp_per_chan == 2000


def test___timing___cfg_change_detection___sets_properties(
    sim_6535_di_single_line_task: Task,
) -> None:
    sim_6535_di_single_line_task.timing.cfg_change_detection_timing(
        "port0/line0:1", "port0/line3:5", AcquisitionType.FINITE, samps_per_chan=2000
    )

    assert (
        sim_6535_di_single_line_task.timing.change_detect_di_rising_edge_physical_chans.name
        == "port0/line0, port0/line1"
    )
    assert (
        sim_6535_di_single_line_task.timing.change_detect_di_falling_edge_physical_chans.name
        == "port0/line3, port0/line4, port0/line5"
    )
    assert sim_6535_di_single_line_task.timing.samp_timing_type == SampleTimingType.CHANGE_DETECTION
    assert sim_6535_di_single_line_task.timing.samp_quant_samp_mode == AcquisitionType.FINITE
    assert sim_6535_di_single_line_task.timing.samp_quant_samp_per_chan == 2000


@pytest.mark.parametrize(
    "clk_source, active_edge",
    [
        ("PFI5", Edge.RISING),
        ("RTSI7", Edge.FALLING),
    ],
)
def test___timing___cfg_pipelined_samp_clk___sets_properties(
    sim_6535_di_single_line_task: Task,
    clk_source: str,
    active_edge: int,
) -> None:
    sim_6535_di_single_line_task.timing.cfg_pipelined_samp_clk_timing(
        rate=32000.0,
        source=clk_source,
        active_edge=active_edge,
        sample_mode=AcquisitionType.FINITE,
        samps_per_chan=2000,
    )

    assert sim_6535_di_single_line_task.timing.samp_clk_src == clk_source
    assert sim_6535_di_single_line_task.timing.samp_clk_active_edge == active_edge
    assert (
        sim_6535_di_single_line_task.timing.samp_timing_type
        == SampleTimingType.PIPELINED_SAMPLE_CLOCK
    )
    assert sim_6535_di_single_line_task.timing.samp_quant_samp_mode == AcquisitionType.FINITE
    assert sim_6535_di_single_line_task.timing.samp_quant_samp_per_chan == 2000


@pytest.mark.parametrize(
    "clk_source, active_edge, pause_when, ready_event_active_level",
    [
        ("PFI5", Edge.RISING, Level.HIGH, Polarity.ACTIVE_HIGH),
        ("PFI5", Edge.FALLING, Level.HIGH, Polarity.ACTIVE_LOW),
        ("RTSI7", Edge.FALLING, Level.LOW, Polarity.ACTIVE_LOW),
    ],
)
def test___timing___cfg_burst_handshaking_import_clock___sets_properties(
    sim_6535_di_single_line_task: Task,
    clk_source: str,
    active_edge: int,
    pause_when: int,
    ready_event_active_level: int,
) -> None:
    sim_6535_di_single_line_task.timing.cfg_burst_handshaking_timing_import_clock(
        sample_clk_rate=32000.0,
        sample_clk_src=clk_source,
        sample_mode=AcquisitionType.FINITE,
        samps_per_chan=2000,
        sample_clk_active_edge=active_edge,
        pause_when=pause_when,
        ready_event_active_level=ready_event_active_level,
    )

    assert sim_6535_di_single_line_task.timing.samp_timing_type == SampleTimingType.BURST_HANDSHAKE
    assert sim_6535_di_single_line_task.timing.samp_quant_samp_mode == AcquisitionType.FINITE
    assert sim_6535_di_single_line_task.timing.samp_quant_samp_per_chan == 2000
    assert sim_6535_di_single_line_task.timing.samp_clk_rate == 32000
    assert sim_6535_di_single_line_task.timing.samp_clk_src == clk_source
    assert sim_6535_di_single_line_task.timing.samp_clk_active_edge == active_edge
    assert sim_6535_di_single_line_task.triggers.pause_trigger.dig_lvl_when == pause_when
    assert (
        sim_6535_di_single_line_task.export_signals.rdy_for_xfer_event_lvl_active_lvl
        == ready_event_active_level
    )


@pytest.mark.parametrize(
    "clk_outp_term, clk_pulse_polarity, pause_when, ready_event_active_level",
    [
        ("PFI0", Polarity.ACTIVE_HIGH, Level.HIGH, Polarity.ACTIVE_HIGH),
        ("PFI1", Polarity.ACTIVE_HIGH, Level.HIGH, Polarity.ACTIVE_LOW),
        ("PFI1", Polarity.ACTIVE_LOW, Level.LOW, Polarity.ACTIVE_LOW),
    ],
)
def test___timing___cfg_burst_handshaking_export_clock___sets_properties(
    sim_6535_di_single_line_task: Task,
    clk_outp_term: str,
    clk_pulse_polarity: int,
    pause_when: int,
    ready_event_active_level: int,
) -> None:
    sim_6535_di_single_line_task.timing.cfg_burst_handshaking_timing_export_clock(
        sample_clk_rate=32000.0,
        sample_clk_outp_term=clk_outp_term,
        sample_mode=AcquisitionType.FINITE,
        samps_per_chan=2000,
        sample_clk_pulse_polarity=clk_pulse_polarity,
        pause_when=pause_when,
        ready_event_active_level=ready_event_active_level,
    )

    assert sim_6535_di_single_line_task.timing.samp_timing_type == SampleTimingType.BURST_HANDSHAKE
    assert sim_6535_di_single_line_task.timing.samp_quant_samp_mode == AcquisitionType.FINITE
    assert sim_6535_di_single_line_task.timing.samp_quant_samp_per_chan == 2000
    assert sim_6535_di_single_line_task.timing.samp_clk_rate == 32000
    assert sim_6535_di_single_line_task.export_signals.samp_clk_pulse_polarity == clk_pulse_polarity
    assert sim_6535_di_single_line_task.triggers.pause_trigger.dig_lvl_when == pause_when
    assert (
        sim_6535_di_single_line_task.export_signals.rdy_for_xfer_event_lvl_active_lvl
        == ready_event_active_level
    )


def test___timing___set_nonexistent_property___raises_exception(task: Task):
    with pytest.raises(AttributeError):
        task.timing.nonexistent_property = "foo"  # type: ignore[attr-defined]
````
