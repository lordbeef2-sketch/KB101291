# NI PYTHON API DIGEST: nidaqmx-python

<!--NI_PYTHON_API_SNAPSHOT repo=ni/nidaqmx-python commit=03282e1b5c741b9f37e4a4e1b5de3a52ae72442e -->

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/stream_readers/_counter_reader.py -->
## PYTHON MODULE: src/handwritten/stream_readers/_counter_reader.py

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
        

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/stream_readers/_digital_multi_channel_reader.py -->
## PYTHON MODULE: src/handwritten/stream_readers/_digital_multi_channel_reader.py

### `class DigitalMultiChannelReader(ChannelReaderBase)`

Reads samples from one or more digital input channels in an NI-DAQmx task.

#### `def read_many_sample_port_byte(self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0)`

Reads one or more 8-bit unsigned integer samples from one or more digital input channel in a task.

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
        

#### `def read_many_sample_port_uint16(self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0)`

Reads one or more 16-bit unsigned integer samples from one or more digital input channels in a task.

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
        

#### `def read_many_sample_port_uint32(self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0)`

Reads one or more 32-bit unsigned integer samples from one or more digital input channels in a task.

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
        

#### `def read_one_sample_multi_line(self, data, timeout=10)`

Reads a single boolean sample from one or more digital input channels in a task.

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
        

#### `def read_one_sample_one_line(self, data, timeout=10)`

Reads a single boolean sample from one or more digital input channels in a task.

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
        

#### `def read_one_sample_port_byte(self, data, timeout=10)`

Reads a single 8-bit unsigned integer sample from one or more digital input channels in a task.

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
        

#### `def read_one_sample_port_uint16(self, data, timeout=10)`

Reads a single 16-bit unsigned integer sample from one or more digital input channels in a task.

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
        

#### `def read_one_sample_port_uint32(self, data, timeout=10)`

Reads a single 32-bit unsigned integer sample from one or more digital input channels in a task.

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
        

#### `def read_waveforms(self, waveforms: list[DigitalWaveform[Any]], number_of_samples_per_channel: int=READ_ALL_AVAILABLE, reallocation_policy: ReallocationPolicy=ReallocationPolicy.TO_GROW, timeout: float=10.0) -> int`

Reads one or more samples from one or more digital input channels into a list of waveforms.

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
        

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/stream_readers/_digital_single_channel_reader.py -->
## PYTHON MODULE: src/handwritten/stream_readers/_digital_single_channel_reader.py

### `class DigitalSingleChannelReader(ChannelReaderBase)`

Reads samples from a digital input channel in an NI-DAQmx task.

#### `def read_many_sample_port_byte(self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0)`

Reads one or more 8-bit unsigned integer samples from a single digital input channel in a task.

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
        

#### `def read_many_sample_port_uint16(self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0)`

Reads one or more 16-bit unsigned integer samples from a single digital input channel in a task.

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
        

#### `def read_many_sample_port_uint32(self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0)`

Reads one or more 32-bit unsigned integer samples from a single digital input channel in a task.

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
        

#### `def read_one_sample_multi_line(self, data, timeout=10)`

Reads a single boolean sample from a single digital input channel in a task.

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
        

#### `def read_one_sample_one_line(self, timeout=10)`

Reads a single boolean sample from a single digital input channel in a task.

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
        

#### `def read_one_sample_port_byte(self, timeout=10)`

Reads a single 8-bit unsigned integer sample from a single digital input channel in a task.

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
        

#### `def read_one_sample_port_uint16(self, timeout=10)`

Reads a single 16-bit unsigned integer sample from a single digital input channel in a task.

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
        

#### `def read_one_sample_port_uint32(self, timeout=10)`

Reads a single 32-bit unsigned integer sample from a single digital input channel in a task.

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
        

#### `def read_waveform(self, waveform: DigitalWaveform[Any], number_of_samples_per_channel: int=READ_ALL_AVAILABLE, reallocation_policy: ReallocationPolicy=ReallocationPolicy.TO_GROW, timeout: float=10.0) -> int`

Reads one or more digital samples from a single digital input channel into a waveform.

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
        

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/stream_readers/_power_readers.py -->
## PYTHON MODULE: src/handwritten/stream_readers/_power_readers.py

### `class PowerSingleChannelReader(ChannelReaderBase)`

Reads samples from an analog input power channel in an NI-DAQmx task.

#### `def read_many_sample(self, voltage_data, current_data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0)`

Reads one or more floating-point power samples from a single analog input power channel in a task.

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
        

#### `def read_one_sample(self, timeout=10)`

Reads a single floating-point power sample from a single analog input power channel in a task.

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
        

### `class PowerMultiChannelReader(ChannelReaderBase)`

Reads samples from one or more analog input power channels in an NI-DAQmx task.

#### `def read_many_sample(self, voltage_data, current_data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0)`

Reads one or more floating-point power samples from one or more analog input power channels in a task.

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
        

#### `def read_one_sample(self, voltage_data, current_data, timeout=10)`

Reads a single floating-point power sample from one or more analog input channels in a task.

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
        

### `class PowerBinaryReader(ChannelReaderBase)`

Reads binary samples from one or more analog input power channels in an NI-DAQmx task.

#### `def read_many_sample(self, voltage_data, current_data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0)`

Reads one or more binary int16 samples from one or more analog input power channel in a task.

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
        

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/stream_writers/__init__.py -->
## PYTHON MODULE: src/handwritten/stream_writers/__init__.py

### MODULE DOCSTRING

NI-DAQmx stream writers.

This package provides classes for writing samples to NI-DAQmx tasks.


- `__all__ = ['AnalogSingleChannelWriter', 'AnalogMultiChannelWriter', 'AnalogUnscaledWriter', 'CounterWriter', 'DigitalSingleChannelWriter', 'DigitalMultiChannelWriter', 'UnsetAutoStartSentinel', 'AUTO_START_UNSET']`

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/stream_writers/_analog_multi_channel_writer.py -->
## PYTHON MODULE: src/handwritten/stream_writers/_analog_multi_channel_writer.py

### `class AnalogMultiChannelWriter(ChannelWriterBase)`

Writes samples to one or more analog output channels in an NI-DAQmx task.

#### `def write_many_sample(self, data, timeout=10.0)`

Writes one or more floating-point samples to one or more analog output channels in a task.

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
        

#### `def write_one_sample(self, data, timeout=10)`

Writes a single floating-point sample to one or more analog output channels in a task.

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
        

#### `def write_waveforms(self, waveforms: Sequence[AnalogWaveform[Any]], timeout: float=10.0) -> int`

Writes waveforms to one or more analog output channels in a task.

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
        

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/stream_writers/_analog_single_channel_writer.py -->
## PYTHON MODULE: src/handwritten/stream_writers/_analog_single_channel_writer.py

### `class AnalogSingleChannelWriter(ChannelWriterBase)`

Writes samples to an analog output channel in an NI-DAQmx task.

#### `def write_many_sample(self, data, timeout=10.0)`

Writes one or more floating-point samples to a single analog output channel in a task.

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
        

#### `def write_one_sample(self, data, timeout=10)`

Writes a single floating-point sample to a single analog output channel in a task.

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
        

#### `def write_waveform(self, waveform: AnalogWaveform[Any], timeout: float=10.0) -> int`

Writes a waveform to a single analog output channel in a task.

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
        

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/stream_writers/_analog_unscaled_writer.py -->
## PYTHON MODULE: src/handwritten/stream_writers/_analog_unscaled_writer.py

### `class AnalogUnscaledWriter(ChannelWriterBase)`

Writes unscaled samples to one or more analog output channels in an NI-DAQmx task.

#### `def write_int16(self, data, timeout=10.0)`

Writes one or more unscaled 16-bit integer samples to one or more analog output channels in a task.

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
        

#### `def write_int32(self, data, timeout=10.0)`

Writes one or more unscaled 32-bit integer samples to one or more analog output channels in a task.

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
        

#### `def write_uint16(self, data, timeout=10.0)`

Writes one or more unscaled 16-bit unsigned integer samples to one or more analog output channels in a task.

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
        

#### `def write_uint32(self, data, timeout=10.0)`

Writes one or more unscaled 32-bit unsigned integer samples to one or more analog output channels in a task.

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
        

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/stream_writers/_channel_writer_base.py -->
## PYTHON MODULE: src/handwritten/stream_writers/_channel_writer_base.py

### `class UnsetAutoStartSentinel()`

Sentinel class for unset auto_start parameter.

#### `def __init__(self)`

- `AUTO_START_UNSET = object.__new__(UnsetAutoStartSentinel)`

### `class ChannelWriterBase()`

Defines base class for all NI-DAQmx stream writers.

#### `def __init__(self, task_out_stream, auto_start=AUTO_START_UNSET)`

Initialize a new ChannelWriterBase.

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
        

#### `def auto_start(self)`

bool: Specifies whether the write method automatically starts the task, if needed.

        If you do not specify a value for this parameter, NI-DAQmx
        determines its value based on the type of write method used.
        If you use a one sample write method, its value is True;
        conversely, if you use a many sample write method, its value
        is False.
        

#### `def auto_start(self, val)`

#### `def auto_start(self)`

#### `def verify_array_shape(self)`

bool: Specifies whether to verify the shape of NumPy arrays.

        Defaults to True when this object is instantiated.

        Setting this property to True may marginally adversely
        impact the performance of read methods.
        

#### `def verify_array_shape(self, val)`

#### `def _verify_array(self, data, is_many_chan, is_many_samp)`

Verifies the shape of a NumPy array.

        Verifies that the shape of the specified NumPy array can be used
        with the specified write method type, if the
        "verify_array_shape" property is set to True.

        Args:
            data (numpy.ndarray): Specifies the NumPy array to verify.
            is_many_chan (bool): Specifies if the write method is a many
                channel version.
            is_many_samp (bool): Specifies if the write method is a many
                sample version.
        

#### `def _verify_array_digital_lines(self, data, is_many_chan, is_many_line)`

Verify the shape of a NumPy array of digital lines.

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
        

#### `def _raise_error_if_invalid_write_dimensions(self, num_dimensions_expected, num_dimensions_in_data)`

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/stream_writers/_counter_writer.py -->
## PYTHON MODULE: src/handwritten/stream_writers/_counter_writer.py

### `class CounterWriter(ChannelWriterBase)`

Writes samples to a counter output channel in an NI-DAQmx task.

#### `def write_many_sample_pulse_frequency(self, frequencies, duty_cycles, timeout=10.0)`

Writes one or more pulse samples in terms of frequency to a single counter output channel in a task.

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
        

#### `def write_many_sample_pulse_ticks(self, high_ticks, low_ticks, timeout=10.0)`

Writes one or more pulse samples in terms of ticks to a single counter output channel in a task.

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
        

#### `def write_many_sample_pulse_time(self, high_times, low_times, timeout=10.0)`

Writes one or more pulse samples in terms of time to a single counter output channel in a task.

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
        

#### `def write_one_sample_pulse_frequency(self, frequency, duty_cycle, timeout=10)`

Writes a new pulse frequency and duty cycle to a single counter output channel in a task.

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
        

#### `def write_one_sample_pulse_ticks(self, high_ticks, low_ticks, timeout=10)`

Writes a new pulse high tick count and low tick count to a single counter output channel in a task.

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
        

#### `def write_one_sample_pulse_time(self, high_time, low_time, timeout=10)`

Writes a new pulse high time and low time to a single counter output channel in a task.

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
        

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/stream_writers/_digital_multi_channel_writer.py -->
## PYTHON MODULE: src/handwritten/stream_writers/_digital_multi_channel_writer.py

### `class DigitalMultiChannelWriter(ChannelWriterBase)`

Writes samples to one or more digital output channels in an NI-DAQmx task.

#### `def write_many_sample_port_byte(self, data, timeout=10.0)`

Writes 8-bit unsigned integer samples to one or more digital output channels in a task.

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
        

#### `def write_many_sample_port_uint16(self, data, timeout=10.0)`

Writes 16-bit unsigned integer samples to one or more digital output channels in a task.

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
        

#### `def write_many_sample_port_uint32(self, data, timeout=10.0)`

Writes 32-bit unsigned integer samples to one or more digital output channels in a task.

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
        

#### `def write_one_sample_multi_line(self, data, timeout=10)`

Writes a single boolean sample to one or more digital output channels in a task.

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
        

#### `def write_one_sample_one_line(self, data, timeout=10)`

Writes a single boolean sample to one or more digital output channels in a task.

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
        

#### `def write_one_sample_port_byte(self, data, timeout=10)`

Writes a single 8-bit unsigned integer sample to one or more digital output channels.

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
        

#### `def write_one_sample_port_uint16(self, data, timeout=10)`

Writes a single 16-bit unsigned integer sample to one or more digital output channels.

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
        

#### `def write_one_sample_port_uint32(self, data, timeout=10)`

Writes a single 32-bit unsigned integer sample to one or more digital output channels.

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
        

#### `def write_waveforms(self, waveforms: Sequence[DigitalWaveform[Any]], timeout: float=10.0) -> int`

Writes waveforms to one or more digital output channels in a task.

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
        

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/stream_writers/_digital_single_channel_writer.py -->
## PYTHON MODULE: src/handwritten/stream_writers/_digital_single_channel_writer.py

### `class DigitalSingleChannelWriter(ChannelWriterBase)`

Writes samples to a single digital output channel in an NI-DAQmx task.

#### `def write_many_sample_port_byte(self, data, timeout=10.0)`

Writes one or more 8-bit unsigned integer samples to a single digital output channel in a task.

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
        

#### `def write_many_sample_port_uint16(self, data, timeout=10.0)`

Writes one or more 16-bit unsigned integer samples to a single digital output channel in a task.

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
        

#### `def write_many_sample_port_uint32(self, data, timeout=10.0)`

Writes one or more 32-bit unsigned integer samples to a single digital output channel in a task.

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
        

#### `def write_one_sample_multi_line(self, data, timeout=10)`

Writes a single boolean sample to a single digital output channel in a task.

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
        

#### `def write_one_sample_one_line(self, data, timeout=10)`

Writes a single boolean sample to a single digital output channel in a task.

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
        

#### `def write_one_sample_port_byte(self, data, timeout=10)`

Writes a single 8-bit unsigned integer sample to a single digital output channel in a task.

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
        

#### `def write_one_sample_port_uint16(self, data, timeout=10)`

Writes a single 16-bit unsigned integer sample to a single digital output channel in a task.

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
        

#### `def write_one_sample_port_uint32(self, data, timeout=10)`

Writes a single 32-bit unsigned integer sample to a single digital output channel in a task.

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
        

#### `def write_waveform(self, waveform: DigitalWaveform[Any], timeout: float=10.0) -> int`

Writes a waveform to a single digital output channel in a task.

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
        

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/system/__init__.py -->
## PYTHON MODULE: src/handwritten/system/__init__.py

### MODULE DOCSTRING

NI-DAQmx system classes.

- `__all__ = ['system', 'device', 'physical_channel', 'storage', 'watchdog']`

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/system/_collections/device_collection.py -->
## PYTHON MODULE: src/handwritten/system/_collections/device_collection.py

### `class DeviceCollection(Sequence)`

Contains the collection of devices for a DAQmx system.

    This class defines methods that implements a container object.
    

#### `def __init__(self, interpreter)`

Do not construct this object directly; instead, call nidaqmx.system.System.local().devices.

#### `def __contains__(self, item)`

#### `def __eq__(self, other)`

#### `def __getitem__(self, index)`

Indexes a subset of devices on this device collection.

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
        

#### `def __iter__(self)`

#### `def __len__(self)`

#### `def __ne__(self, other)`

#### `def __reversed__(self)`

#### `def device_names(self)`

List[str]: Indicates the names of all devices on this device collection.

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/system/_collections/persisted_channel_collection.py -->
## PYTHON MODULE: src/handwritten/system/_collections/persisted_channel_collection.py

### `class PersistedChannelCollection(Sequence)`

Contains the collection of global channels for a DAQmx system.

    This class defines methods that implements a container object.
    

#### `def __init__(self, interpreter)`

Do not construct this object directly; instead, call nidaqmx.system.System.local().global_channels.

#### `def __contains__(self, item)`

#### `def __eq__(self, other)`

#### `def __getitem__(self, index)`

Indexes a subset of global channels on this global channel collection.

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
        

#### `def __iter__(self)`

#### `def __len__(self)`

#### `def __ne__(self, other)`

#### `def __reversed__(self)`

#### `def global_channel_names(self)`

List[str]: The names of all the global channels on this collection.

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/system/_collections/persisted_scale_collection.py -->
## PYTHON MODULE: src/handwritten/system/_collections/persisted_scale_collection.py

### `class PersistedScaleCollection(Sequence)`

Contains the collection of custom scales on a DAQmx system.

    This class defines methods that implements a container object.
    

#### `def __init__(self, interpreter)`

Do not construct this object directly; instead, call nidaqmx.system.System.local().scales.

#### `def __contains__(self, item)`

#### `def __eq__(self, other)`

#### `def __getitem__(self, index)`

Indexes a subset of custom scales on this collection.

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
        

#### `def __iter__(self)`

#### `def __len__(self)`

#### `def __ne__(self, other)`

#### `def __reversed__(self)`

#### `def scale_names(self)`

List[str]: Indicates the names of all the custom scales on this collection.

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/system/_collections/persisted_task_collection.py -->
## PYTHON MODULE: src/handwritten/system/_collections/persisted_task_collection.py

### `class PersistedTaskCollection(Sequence)`

Contains the collection of task saved on a DAQmx system.

    This class defines methods that implements a container object.
    

#### `def __init__(self, interpreter)`

Do not construct this object directly; instead, call nidaqmx.system.System.local().tasks.

#### `def __contains__(self, item)`

#### `def __eq__(self, other)`

#### `def __getitem__(self, index)`

Indexes a subset of saved tasks on this collection.

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
        

#### `def __iter__(self)`

#### `def __len__(self)`

#### `def __ne__(self, other)`

#### `def __reversed__(self)`

#### `def task_names(self)`

List[str]: Indicates the names of all the tasks on this collection.

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/system/_collections/physical_channel_collection.py -->
## PYTHON MODULE: src/handwritten/system/_collections/physical_channel_collection.py

### `class PhysicalChannelCollection(Sequence)`

Contains the collection of physical channels for a DAQmx device.

    This class defines methods that implements a container object.
    

#### `def __init__(self, device_name, interpreter)`

Do not construct this object directly; instead, construct a nidaqmx.system.Device and use the appropriate property, such as device.ai_physical_channels.

#### `def __contains__(self, item)`

#### `def __eq__(self, other)`

#### `def __getitem__(self, index)`

Indexes a subset of physical channels on this physical channel collection.

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
        

#### `def __iter__(self)`

#### `def __len__(self)`

#### `def __ne__(self, other)`

#### `def __reversed__(self)`

#### `def all(self)`

nidaqmx.system.physical_channel.PhysicalChannel: Specifies a physical channel object that represents the entire list of physical channels on this channel collection.

#### `def channel_names(self)`

List[str]: Specifies the entire list of physical channels in this collection.

### `class AIPhysicalChannelCollection(PhysicalChannelCollection)`

Contains the collection of analog input physical channels for a DAQmx device.

    This class defines methods that implements a container object.
    

#### `def channel_names(self)`

### `class AOPhysicalChannelCollection(PhysicalChannelCollection)`

Contains the collection of analog output physical channels for a DAQmx device.

    This class defines methods that implements a container object.
    

#### `def channel_names(self)`

### `class CIPhysicalChannelCollection(PhysicalChannelCollection)`

Contains the collection of counter input physical channels for a DAQmx device.

    This class defines methods that implements a container object.
    

#### `def channel_names(self)`

### `class COPhysicalChannelCollection(PhysicalChannelCollection)`

Contains the collection of counter output physical channels for a DAQmx device.

    This class defines methods that implements a container object.
    

#### `def channel_names(self)`

### `class DILinesCollection(PhysicalChannelCollection)`

Contains the collection of digital input lines for a DAQmx device.

    This class defines methods that implements a container object.
    

#### `def channel_names(self)`

### `class DOLinesCollection(PhysicalChannelCollection)`

Contains the collection of digital output lines for a DAQmx device.

    This class defines methods that implements a container object.
    

#### `def channel_names(self)`

### `class DIPortsCollection(PhysicalChannelCollection)`

Contains the collection of digital input ports for a DAQmx device.

    This class defines methods that implements a container object.
    

#### `def channel_names(self)`

### `class DOPortsCollection(PhysicalChannelCollection)`

Contains the collection of digital output ports for a DAQmx device.

    This class defines methods that implements a container object.
    

#### `def channel_names(self)`

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/system/_watchdog_modules/expiration_states_collection.py -->
## PYTHON MODULE: src/handwritten/system/_watchdog_modules/expiration_states_collection.py

### `class ExpirationStatesCollection()`

Contains the collection of expiration states for a DAQmx Watchdog Task.

    This class defines methods that implements a container object.
    

#### `def __init__(self, task_handle, interpreter)`

#### `def __eq__(self, other)`

#### `def __hash__(self)`

#### `def __ne__(self, other)`

#### `def __getitem__(self, index)`

Indexes an expiration state on this collection.

        Args:
            index (str): Name of the physical channel of which the
                expiration state to retrieve.

        Returns:
            nidaqmx.system._watchdog_modules.expiration_state.ExpirationState:

            The object representing the indexed expiration state.
        

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/system/storage/__init__.py -->
## PYTHON MODULE: src/handwritten/system/storage/__init__.py

### MODULE DOCSTRING

NI-DAQmx storage classes.

- `__all__ = ['persisted_channel', 'persisted_scale', 'persisted_task']`

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/system/storage/persisted_channel.py -->
## PYTHON MODULE: src/handwritten/system/storage/persisted_channel.py

### MODULE DOCSTRING

NI-DAQmx persisted channel classes.

- `__all__ = ['PersistedChannel']`

### `class PersistedChannel()`

Represents a saved DAQmx global channel.

    Use the DAQmx Persisted Channel properties to query information about
    programmatically saved global channels.
    

#### `def __init__(self, name, *, grpc_options=None)`

Initialize a new PersistedChannel.

        Args:
            name (str): Specifies the name of the global channel.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        

#### `def __eq__(self, other)`

#### `def __hash__(self)`

#### `def __ne__(self, other)`

#### `def __repr__(self)`

#### `def name(self)`

str: Indicates the name of the global channel.

#### `def author(self)`

str: Indicates the author of the global channel.

#### `def allow_interactive_editing(self)`

bool: Indicates whether the global channel can be edited in the DAQ Assistant.

#### `def allow_interactive_deletion(self)`

bool: Indicates whether the global channel can be deleted through MAX.

#### `def delete(self)`

Deletes this global channel from MAX.

        This function does not remove the global channel from tasks that
        use it.
        

### `class _PersistedChannelAlternateConstructor(PersistedChannel)`

Provide an alternate constructor for the PersistedChannel object.

    This is a private API used to instantiate a PersistedChannel with an existing interpreter.
    

#### `def __init__(self, name, interpreter)`

Initialize a new PersistedChannel with an existing interpreter.

        Args:
            name: Specifies the name of the PersistedChannel.
            interpreter: Specifies the interpreter instance.

        

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/system/storage/persisted_scale.py -->
## PYTHON MODULE: src/handwritten/system/storage/persisted_scale.py

### MODULE DOCSTRING

NI-DAQmx persisted scale classes.

- `__all__ = ['PersistedScale']`

### `class PersistedScale()`

Represents a saved DAQmx custom scale.

    Use the DAQmx Persisted Scale properties to query information about
    programmatically saved custom scales.
    

#### `def __init__(self, name, *, grpc_options=None)`

Initialize a new PersistedScale.

        Args:
            name (str): Specifies the name of the saved scale.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        

#### `def __eq__(self, other)`

#### `def __hash__(self)`

#### `def __ne__(self, other)`

#### `def __repr__(self)`

#### `def name(self)`

str: Indicates the name of the custom scale.

#### `def author(self)`

str: Indicates the author of the custom scale.

#### `def allow_interactive_editing(self)`

bool: Indicates whether the custom scale can be edited in the DAQ Assistant.

#### `def allow_interactive_deletion(self)`

bool: Indicates whether the custom scale can be deleted through MAX.

#### `def delete(self)`

Deletes this custom scale from MAX.

        This function does not remove the custom scale from virtual
        channels that use it.
        

#### `def load(self)`

Loads this custom scale.

        Returns:
            nidaqmx.scale.Scale: Indicates the loaded Scale object.
        

### `class _PersistedScaleAlternateConstructor(PersistedScale)`

Provide an alternate constructor for the PersistedScale object.

    This is a private API used to instantiate a PersistedScale with an existing interpreter.
    

#### `def __init__(self, name, interpreter)`

Initialize a new PersistedScale with an existing interpreter.

        Args:
            name: Specifies the name of the PersistedScale.
            interpreter: Specifies the interpreter instance.

        

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/system/storage/persisted_task.py -->
## PYTHON MODULE: src/handwritten/system/storage/persisted_task.py

### MODULE DOCSTRING

NI-DAQmx persisted task classes.

- `__all__ = ['PersistedTask']`

### `class PersistedTask()`

Represents a saved DAQmx task.

    Use the DAQmx Persisted Task properties to query information about
    programmatically saved tasks.
    

#### `def __init__(self, name, *, grpc_options=None)`

Initialize a new PersistedTask.

        Args:
            name (str): Specifies the name of the saved task.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        

#### `def __eq__(self, other)`

#### `def __hash__(self)`

#### `def __ne__(self, other)`

#### `def __repr__(self)`

#### `def name(self)`

str: Indicates the name of the task.

#### `def author(self)`

str: Indicates the author of the task.

#### `def allow_interactive_editing(self)`

bool: Indicates whether the task can be edited in the DAQ Assistant.

#### `def allow_interactive_deletion(self)`

bool: Indicates whether the task can be deleted through MAX.

#### `def delete(self)`

Deletes this task from MAX.

        This function does not clear the copy of the task stored in memory.
        Use the DAQmx Clear Task function to clear that copy of the task.
        

#### `def load(self)`

Loads this saved task.

        If you use this function to load a task, you must use DAQmx Clear
        Task to destroy it.

        Returns:
            nidaqmx.task.Task: Indicates the loaded Task object.
        

### `class _PersistedTaskAlternateConstructor(PersistedTask)`

Provide an alternate constructor for the PersistedTask object.

    This is a private API used to instantiate a PersistedTask with an existing interpreter.
    

#### `def __init__(self, name, interpreter)`

Initialize a new PersistedTask with an existing interpreter.

        Args:
            name: Specifies the name of the PersistedTask.
            interpreter: Specifies the interpreter instance.

        

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/task/__init__.py -->
## PYTHON MODULE: src/handwritten/task/__init__.py

### MODULE DOCSTRING

NI-DAQmx task and related classes.

- `__all__ = ['Task', 'InStream', 'OutStream', 'ExportSignals', 'Timing']`

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/task/_task.py -->
## PYTHON MODULE: src/handwritten/task/_task.py

- `__all__ = ['Task']`

### `class UnsetNumSamplesSentinel()`

### `class UnsetAutoStartSentinel()`

- `NUM_SAMPLES_UNSET = UnsetNumSamplesSentinel()`

- `AUTO_START_UNSET = UnsetAutoStartSentinel()`

### `class Task()`

Represents a DAQmx Task.

#### `def __init__(self, new_task_name='', *, grpc_options=None)`

Creates a DAQmx task.

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
        

#### `def __del__(self)`

#### `def __enter__(self)`

#### `def __eq__(self, other)`

#### `def __exit__(self, type, value, traceback)`

#### `def __hash__(self)`

#### `def __ne__(self, other)`

#### `def __repr__(self)`

#### `def name(self)`

str: Indicates the name of the task.

#### `def channels(self)`

:class:`nidaqmx.task.channels.Channel`: Specifies a channel object that represents the entire list of virtual channels in this task.

#### `def channel_names(self)`

List[str]: Indicates the names of all virtual channels in the task.

#### `def number_of_channels(self)`

int: Indicates the number of virtual channels in the task.

#### `def devices(self)`

List[:class:`nidaqmx.system.device.Device`]: Indicates a list of Device objects representing all the devices in the task.

#### `def number_of_devices(self)`

int: Indicates the number of devices in the task.

#### `def ai_channels(self) -> AIChannelCollection`

Gets the collection of analog input channels for this task.

#### `def ao_channels(self) -> AOChannelCollection`

Gets the collection of analog output channels for this task.

#### `def ci_channels(self) -> CIChannelCollection`

Gets the collection of counter input channels for this task.

#### `def co_channels(self) -> COChannelCollection`

Gets the collection of counter output channels for this task.

#### `def di_channels(self) -> DIChannelCollection`

Gets the collection of digital input channels for this task.

#### `def do_channels(self) -> DOChannelCollection`

Gets the collection of digital output channels for this task.

#### `def export_signals(self) -> ExportSignals`

Gets the exported signal configurations for the task.

#### `def in_stream(self) -> InStream`

Gets the read configurations for the task.

#### `def out_stream(self) -> OutStream`

Gets the write configurations for the task.

#### `def timing(self) -> Timing`

Gets the timing configurations for the task.

#### `def triggers(self) -> Triggers`

Gets the trigger configurations for the task.

#### `def _initialize(self, task_handle, interpreter)`

Instantiates and populates various attributes used by this task.

        Args:
            task_handle (TaskHandle): Specifies the handle for this task.
        

#### `def _calculate_num_samps_per_chan(self, num_samps_per_chan)`

Calculates the actual number of samples per channel to read.

        This method is necessary because the number of samples per channel
        can be set to NUM_SAMPLES_UNSET or -1, where each value entails a
        different method of calculating the actual number of samples per
        channel to read.

        Args:
            num_samps_per_chan (int): Specifies the number of samples per
                channel.
        

#### `def add_global_channels(self, global_channels)`

Adds global virtual channels from MAX to the given task.

        Args:
            global_channels (List[nidaqmx.system.storage.persisted_channel.PersistedChannel]):
                Specifies the channels to add to the task.

                These channels must be valid channels available from MAX.
                If you pass an invalid channel, NI-DAQmx returns an error.
                This value is ignored if it is empty.
        

#### `def close(self)`

Clears the task.

        Before clearing, this method aborts the task, if necessary,
        and releases any resources the task reserved. You cannot use a task
        after you clear it unless you recreate the task.

        If you create a DAQmx Task object within a loop, use this method
        within the loop after you are finished with the task to avoid
        allocating unnecessary memory.
        

#### `def control(self, action)`

Alters the state of a task according to the action you specify.

        Args:
            action (nidaqmx.constants.TaskMode): Specifies how to alter
                the task state.
        

#### `def is_task_done(self)`

Queries the status of the task and indicates if it completed execution.

        Use this function to ensure that the specified
        operation is complete before you stop the task.

        Returns:
            bool:

            Indicates if the measurement or generation completed.
        

#### `def perform_bridge_offset_nulling_cal(self, channel='', skip_unsupported_channels=False)`

Perform a bridge offset nulling calibration on the channels in the task.

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
        

#### `def perform_strain_shunt_cal(self, channel='', shunt_resistor_value=100000, shunt_resistor_location=ShuntElementLocation.R3, shunt_resistor_select=ShuntCalSelect.A, shunt_resistor_source=ShuntCalSource.DEFAULT, skip_unsupported_channels=False)`

Perform shunt calibration for the specified channels using a strain gage sensor.

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
        

#### `def perform_bridge_shunt_cal(self, channel='', shunt_resistor_value=100000, shunt_resistor_location=ShuntElementLocation.R3, shunt_resistor_select=ShuntCalSelect.A, shunt_resistor_source=ShuntCalSource.DEFAULT, bridge_resistance=120, skip_unsupported_channels=False)`

Perform shunt calibration for the specified channels using a bridge sensor.

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
        

#### `def perform_thrmcpl_lead_offset_nulling_cal(self, channel='', skip_unsupported_channels=False)`

Perform thermocouple lead offset nulling calibration on the channels in the task.

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
        

#### `def read(self, number_of_samples_per_channel=NUM_SAMPLES_UNSET, timeout=10.0)`

Reads samples from the task or virtual channels you specify.

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
        

#### `def _read_ctr_pulse(self, array_shape: tuple[int, ...], meas_type: UsageTypeCI, number_of_channels: int, number_of_samples_per_channel: int, num_samples_not_set: bool, timeout: float) -> CtrFreq | CtrTick | CtrTime | list[CtrFreq] | list[CtrTick] | list[CtrTime]`

#### `def _read_power(self, array_shape: tuple[int, ...], number_of_channels: int, number_of_samples_per_channel: int, timeout: float) -> PowerMeasurement | list[PowerMeasurement] | list[list[PowerMeasurement]]`

#### `def read_waveform(self, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0)`

Reads samples from the task or virtual channels you specify, and returns them as waveforms.

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
        

#### `def register_done_event(self, callback_method)`

Registers a callback function to receive an event when a task stops due to an error or when a finite acquisition task or finite generation task completes execution.

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
        

#### `def register_every_n_samples_acquired_into_buffer_event(self, sample_interval, callback_method)`

Registers a callback function to receive an event when the specified number of samples is written from the device to the buffer.

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
        

#### `def register_every_n_samples_transferred_from_buffer_event(self, sample_interval, callback_method)`

Registers a callback function to receive an event when the specified number of samples is written from the buffer to the device.

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
        

#### `def register_signal_event(self, signal_type, callback_method)`

Registers a callback function to receive an event when the specified hardware event occurs.

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
        

#### `def save(self, save_as='', author='', overwrite_existing_task=False, allow_interactive_editing=True, allow_interactive_deletion=True)`

Saves this task and any local channels it contains to MAX.

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
        

#### `def start(self)`

Start the task.

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
        

#### `def stop(self)`

Stop the task.

        This method stops the task and returns it to the state the task was in before the
        DAQmx Start Task method ran or the DAQmx Write method ran with the
        autostart input set to TRUE.

        If you do not use the DAQmx Start Task method and the DAQmx Stop Task
        method when you use the DAQmx Read method or the DAQmx Write method
        multiple times, such as in a loop, the task starts and stops
        repeatedly. Starting and stopping a task repeatedly reduces the
        performance of the application.
        

#### `def wait_for_valid_timestamp(self, timestamp_event, timeout=10.0)`

Wait until the specified timestamp has a value.

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
        

#### `def wait_until_done(self, timeout=10.0)`

Waits for the measurement or generation to complete.

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
        

#### `def _raise_invalid_num_lines_error(self, num_lines_expected, num_lines_in_data) -> NoReturn`

#### `def _raise_invalid_write_num_chans_error(self, number_of_channels, number_of_channels_in_data) -> NoReturn`

#### `def _raise_invalid_write_mixed_data_error(self) -> NoReturn`

#### `def _raise_no_output_channels_error(self) -> NoReturn`

#### `def _raise_unsupported_output_type_error(self, output_type) -> NoReturn`

#### `def write(self, data, auto_start=AUTO_START_UNSET, timeout=10.0)`

Writes samples to the task or virtual channels you specify.

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
        

#### `def _is_waveform_data(self, data)`

Check if data is waveform data (single waveform or list of waveforms).

#### `def write_waveform(self, waveforms: AnalogWaveform[Any] | DigitalWaveform[Any] | Sequence[AnalogWaveform[Any]] | Sequence[DigitalWaveform[Any]], auto_start=AUTO_START_UNSET, timeout: float=10.0) -> int`

Writes samples from one or more waveforms to the task or virtual channels you specify.

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
        

### `class _TaskAlternateConstructor(Task)`

Provide an alternate constructor for the Task object.

    This is a private API used to instantiate a Task with an existing task handle and interpreter.
    

#### `def __init__(self, task_handle, interpreter, close_on_exit)`

Initialize a new Task with an existing interpreter.

        Args:
            task_handle: Specifies the task handle from which to create a
                Task object.
            interpreter: Specifies the interpreter instance.
            close_on_exit: Specifies whether the task's context manager closes the task.
        

### `class _TaskEventType(Enum)`

Internal enum for task event bookkeeping.

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/task/channels/__init__.py -->
## PYTHON MODULE: src/handwritten/task/channels/__init__.py

### MODULE DOCSTRING

NI-DAQmx channel classes.

- `__all__ = ['Channel', 'AIChannel', 'AOChannel', 'CIChannel', 'COChannel', 'DIChannel', 'DOChannel']`

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/task/collections/__init__.py -->
## PYTHON MODULE: src/handwritten/task/collections/__init__.py

### MODULE DOCSTRING

NI-DAQmx channel collection classes.

- `__all__ = ['ChannelCollection', 'AIChannelCollection', 'AOChannelCollection', 'CIChannelCollection', 'COChannelCollection', 'DIChannelCollection', 'DOChannelCollection']`

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/task/collections/_channel_collection.py -->
## PYTHON MODULE: src/handwritten/task/collections/_channel_collection.py

### `class ChannelCollection(Sequence)`

Contains the collection of channels for a DAQmx Task.

    This class defines methods that implements a container object.
    

#### `def __init__(self, task_handle, interpreter)`

Do not construct this object directly; instead, construct a nidaqmx.Task and use the appropriate property, such as task.ai_channels.

#### `def __contains__(self, item)`

#### `def __eq__(self, other)`

#### `def __getitem__(self, index)`

Indexes a subset of virtual channels on this channel collection.

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
        

#### `def __hash__(self)`

#### `def __iter__(self)`

#### `def __len__(self)`

#### `def __ne__(self, other)`

#### `def __reversed__(self)`

#### `def all(self)`

:class:`nidaqmx.task.channels.Channel`: Specifies a channel object that represents the entire list of virtual channels on this channel collection.

#### `def channel_names(self)`

List[str]: Specifies the entire list of virtual channels on this channel collection.

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/task/triggering/__init__.py -->
## PYTHON MODULE: src/handwritten/task/triggering/__init__.py

### MODULE DOCSTRING

NI-DAQmx task triggering classes.

- `__all__ = ['Triggers', 'ArmStartTrigger', 'HandshakeTrigger', 'PauseTrigger', 'ReferenceTrigger', 'StartTrigger']`

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/types.py -->
## PYTHON MODULE: src/handwritten/types.py

### MODULE DOCSTRING

NI-DAQmx data types.

### `class IDPinContents(typing.NamedTuple)`

IDPinContents represent the contents of the memory connected to the ID pin.

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/utils.py -->
## PYTHON MODULE: src/handwritten/utils.py

### MODULE DOCSTRING

NI-DAQmx utility functions.

### `class _ChannelInfo()`

#### `def to_flattened_name(self) -> str`

Convert the channel info to a flattened channel name.

### `def flatten_channel_string(channel_names: list[str]) -> str`

Converts a list of channel names to a comma-delimited list of names.

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
    

### `def unflatten_channel_string(channel_names: str) -> list[str]`

Converts a comma-delimited list of channel names to a list of names.

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
    

### `def _select_interpreter(grpc_options: GrpcSessionOptions | None=None, interpreter: BaseInterpreter | None=None) -> BaseInterpreter`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/__init__.py -->
## PYTHON MODULE: tests/__init__.py

### MODULE DOCSTRING

Tests for the nidaqmx package.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/_event_utils.py -->
## PYTHON MODULE: tests/_event_utils.py

### `class DoneEvent(NamedTuple)`

Represents a Done event.

### `class EveryNSamplesEvent(NamedTuple)`

Represents an Every N Samples event.

### `class SignalEvent(NamedTuple)`

Represents a Signal event.

### `class BaseEventObserver(Generic[TEvent])`

Base class for event observers.

#### `def __init__(self, side_effect: SideEffect | None=None)`

Initializes the BaseEventObserver.

#### `def events(self) -> list[TEvent]`

Returns the list of observed events.

#### `def wait_for_events(self, count=1, timeout=10.0) -> None`

Waits for the specified number of events.

#### `def _invoke_side_effect(self) -> None`

### `class DoneEventObserver(BaseEventObserver[DoneEvent])`

An observer for Done events.

#### `def handle_done_event(self, task_handle: object, status: int, callback_data: object) -> int`

Handles a Done event.

### `class EveryNSamplesEventObserver(BaseEventObserver[EveryNSamplesEvent])`

An observer for Every N Samples events.

#### `def handle_every_n_samples_event(self, task_handle: object, every_n_samples_event_type: int, number_of_samples: int, callback_data: object) -> int`

Handles an Every N Samples event.

### `class SignalEventObserver(BaseEventObserver[SignalEvent])`

An observer for Signal events.

#### `def handle_signal_event(self, task_handle: object, signal_type: int, callback_data: object) -> int`

Handles a Signal event.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/_grpc_utils.py -->
## PYTHON MODULE: tests/_grpc_utils.py

### MODULE DOCSTRING

Helper functions to be used in nidaqmx tests.

### `class GrpcServerProcess()`

Maintains the processes involved in connecting to the gRPC device service.

#### `def __init__(self)`

Creates a GrpcServerProcess instance.

#### `def __enter__(self)`

Returns the GrpcServerProcess instance.

#### `def __exit__(self, exc_type, exc_val, exc_tb)`

Closes the GrpcServerProcess instance.

#### `def _get_grpc_server_exe(self)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/acceptance/__init__.py -->
## PYTHON MODULE: tests/acceptance/__init__.py

### MODULE DOCSTRING

Acceptance tests for the nidaqmx package.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/acceptance/test_examples.py -->
## PYTHON MODULE: tests/acceptance/test_examples.py

- `EXAMPLES_DIRECTORY = Path(__file__).parent.parent.parent / 'examples'`

- `EXAMPLE_PATHS = [p for p in EXAMPLES_DIRECTORY.glob('**/*.py') if p.name != '__init__.py']`

### `def test___shipping_example___run___no_errors(example_path: Path, system)`

### `def _find_device_names(source: str) -> set[str]`

### `def _find_physical_channel_names(source: str, device_name: str) -> set[str]`

### `def _has_physical_channel(device: nidaqmx.system.Device, physical_channel_name: str) -> bool`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/acceptance/test_internationalization.py -->
## PYTHON MODULE: tests/acceptance/test_internationalization.py

### `def ai_task(task, sim_6363_device)`

### `def _get_encoding(obj: Task | dict[str, Any]) -> str | None`

### `def test___supported_encoding___reset_nonexistent_device___returns_error_with_device_name(init_kwargs: dict[str, Any], device_name: str, supported_encodings: list[str])`

### `def test___supported_encoding___logging_file_path___returns_assigned_value(ai_task: Task, file_path: str, supported_encodings: list[str])`

### `def test___supported_encoding___configure_logging___returns_assigned_values(ai_task: Task, file_path: str, supported_encodings: list[str])`

### `def test___supported_encoding___start_new_file___returns_assigned_value(ai_task: Task, file_path: str, supported_encodings: list[str])`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/acceptance/test_multi_threading.py -->
## PYTHON MODULE: tests/acceptance/test_multi_threading.py

- `RUN_TIME = 1.0`

- `TIMEOUT = 10.0`

### `def test___single_task___get_set_float_properties___no_errors(task: Task, thread_pool_executor: ThreadPoolExecutor, multi_threading_test_devices: Sequence[Device], seed: int) -> None`

### `def test___single_task___get_set_float_and_string_properties___no_errors(task: Task, thread_pool_executor: ThreadPoolExecutor, multi_threading_test_devices: Sequence[Device], seed: int) -> None`

### `def test___multiple_tasks___get_set_float_and_string_properties___no_errors(generate_task: Callable[[], Task], thread_pool_executor: ThreadPoolExecutor, multi_threading_test_devices: Sequence[Device], seed: int) -> None`

### `def _get_set_property_thread_main(start_barrier: Barrier, stop_semaphore: Semaphore, channel: AIChannel, property_name: str, property_values: list[Any]) -> None`

### `def _check_for_exceptions(futures: Sequence[Future]) -> None`

### `def test___shared_interpreter___run_multiple_acquisitions_with_events___callbacks_invoked(init_kwargs, multi_threading_test_devices: Sequence[Device], system: System)`

### `def test___shared_interpreter___unregister_events_during_other_acquisitions_with_events___callbacks_invoked(init_kwargs, multi_threading_test_devices: Sequence[Device], system: System)`

### `def _create_ai_task_with_shared_interpreter(init_kwargs, system: System, task_name: str, physical_channel: str) -> Task`

### `def _configure_timing(tasks: list[Task], samples_per_chan: list[int]) -> None`

### `def _configure_events(tasks: list[Task], samples_per_chan: list[int]) -> tuple[list[int], list[threading.Event], list[int]]`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/benchmark/__init__.py -->
## PYTHON MODULE: tests/benchmark/__init__.py

### MODULE DOCSTRING

Benchmarks for the nidaqmx package.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/benchmark/conftest.py -->
## PYTHON MODULE: tests/benchmark/conftest.py

### MODULE DOCSTRING

Fixtures for benchmark tests.

- `_WAVEFORM_BENCHMARK_MODES = [WaveformAttributeMode.NONE, WaveformAttributeMode.TIMING, WaveformAttributeMode.TIMING | WaveformAttributeMode.EXTENDED_PROPERTIES]`

- `_WAVEFORM_BENCHMARK_MODE_IDS = ['NONE', 'TIMING', 'ALL']`

### `def _configure_timing(task: Task, num_samples: int) -> None`

### `def _start_input_task(task: Task) -> None`

### `def _commit_output_task(task: Task, num_samples: int) -> None`

### `def pytest_addoption(parser: pytest.Parser) -> None`

Add command line options to pytest.

### `def benchmark_device(system: System, request: pytest.FixtureRequest) -> Device`

Get device for benchmarking.

### `def ai_benchmark_task(task: Task, benchmark_device: Device, request: pytest.FixtureRequest) -> Task`

Configure an AI task for benchmarking.

### `def ao_benchmark_task(task: Task, real_x_series_multiplexed_device: Device, request: pytest.FixtureRequest) -> Task`

Configure a hardware-timed buffered AO task for benchmarking.

### `def di_lines_benchmark_task(task: Task, benchmark_device: Device, request: pytest.FixtureRequest) -> Task`

Configure a hardware-timed buffered DI task for benchmarking.

### `def di_port32_benchmark_task(task: Task, benchmark_device: Device, request: pytest.FixtureRequest) -> Task`

Configure a hardware-timed buffered DI task for benchmarking.

### `def do_lines_benchmark_task(task: Task, benchmark_device: Device, request: pytest.FixtureRequest) -> Task`

Configure a hardware-timed buffered DO task for benchmarking.

### `def do_port32_benchmark_task(task: Task, benchmark_device: Device, request: pytest.FixtureRequest) -> Task`

Configure a hardware-timed buffered DO task for benchmarking.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/benchmark/test_analog_stream_readers.py -->
## PYTHON MODULE: tests/benchmark/test_analog_stream_readers.py

### `def test___analog_single_channel_reader___read_one_sample(benchmark: BenchmarkFixture, ai_benchmark_task: Task) -> None`

### `def test___analog_single_channel_reader___read_many_sample(benchmark: BenchmarkFixture, ai_benchmark_task: Task, num_samples: int) -> None`

### `def test___analog_single_channel_reader___read_all_available(benchmark: BenchmarkFixture, ai_benchmark_task: Task, num_samples: int) -> None`

### `def test___analog_single_channel_reader___read_waveform(benchmark: BenchmarkFixture, ai_benchmark_task: Task, num_samples: int, waveform_attribute_mode: WaveformAttributeMode) -> None`

### `def test___analog_multi_channel_reader___read_one_sample(benchmark: BenchmarkFixture, ai_benchmark_task: Task, num_channels: int) -> None`

### `def test___analog_multi_channel_reader___read_many_sample(benchmark: BenchmarkFixture, ai_benchmark_task: Task, num_channels: int, num_samples: int) -> None`

### `def test___analog_multi_channel_reader___read_all_available(benchmark: BenchmarkFixture, ai_benchmark_task: Task, num_channels: int, num_samples: int) -> None`

### `def test___analog_multi_channel_reader___read_waveform(benchmark: BenchmarkFixture, ai_benchmark_task: Task, num_channels: int, num_samples: int, waveform_attribute_mode: WaveformAttributeMode) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/benchmark/test_analog_stream_writers.py -->
## PYTHON MODULE: tests/benchmark/test_analog_stream_writers.py

### `def test___analog_single_channel_writer___write_one_sample(benchmark: BenchmarkFixture, ao_benchmark_task: nidaqmx.Task) -> None`

### `def test___analog_single_channel_writer___write_many_sample(benchmark: BenchmarkFixture, ao_benchmark_task: nidaqmx.Task, num_samples: int) -> None`

### `def test___analog_single_channel_writer___write_waveform(benchmark: BenchmarkFixture, ao_benchmark_task: nidaqmx.Task, num_samples: int) -> None`

### `def test___analog_multi_channel_writer___write_one_sample(benchmark: BenchmarkFixture, ao_benchmark_task: nidaqmx.Task, num_channels: int) -> None`

### `def test___analog_multi_channel_writer___write_many_sample(benchmark: BenchmarkFixture, ao_benchmark_task: nidaqmx.Task, num_channels: int, num_samples: int) -> None`

### `def test___analog_multi_channel_writer___write_waveform(benchmark: BenchmarkFixture, ao_benchmark_task: nidaqmx.Task, num_channels: int, num_samples: int) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/benchmark/test_digital_stream_readers.py -->
## PYTHON MODULE: tests/benchmark/test_digital_stream_readers.py

### `def test___digital_single_channel_reader___read_one_sample_one_line(benchmark: BenchmarkFixture, di_lines_benchmark_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_reader___read_one_sample_multi_line(benchmark: BenchmarkFixture, di_lines_benchmark_task: nidaqmx.Task, num_lines: int) -> None`

### `def test___digital_single_channel_reader___read_many_sample_port_uint32(benchmark: BenchmarkFixture, di_port32_benchmark_task: nidaqmx.Task, num_samples: int) -> None`

### `def test___digital_single_channel_reader___read_waveform_lines(benchmark: BenchmarkFixture, di_lines_benchmark_task: nidaqmx.Task, num_samples: int, num_lines: int) -> None`

### `def test___digital_single_channel_reader___read_waveform_port(benchmark: BenchmarkFixture, di_port32_benchmark_task: nidaqmx.Task, num_samples: int) -> None`

### `def test___digital_multi_channel_reader___read_one_sample_one_line(benchmark: BenchmarkFixture, di_lines_benchmark_task: nidaqmx.Task, num_channels: int) -> None`

### `def test___digital_multi_channel_reader___read_one_sample_multi_line(benchmark: BenchmarkFixture, di_lines_benchmark_task: nidaqmx.Task, num_channels: int, num_lines: int) -> None`

### `def test___digital_multi_channel_reader___read_many_sample_port_uint32(benchmark: BenchmarkFixture, di_port32_benchmark_task: nidaqmx.Task, num_samples: int) -> None`

### `def test___digital_multi_channel_reader___read_waveform_lines(benchmark: BenchmarkFixture, di_lines_benchmark_task: nidaqmx.Task, num_channels: int, num_samples: int, num_lines: int) -> None`

### `def test___digital_multi_channel_reader___read_waveform_port(benchmark: BenchmarkFixture, di_port32_benchmark_task: nidaqmx.Task, num_samples: int) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/benchmark/test_digital_stream_writers.py -->
## PYTHON MODULE: tests/benchmark/test_digital_stream_writers.py

### `def test___digital_single_channel_writer___write_one_sample_one_line(benchmark: BenchmarkFixture, do_lines_benchmark_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_writer___write_one_sample_multi_line(benchmark: BenchmarkFixture, do_lines_benchmark_task: nidaqmx.Task, num_lines: int) -> None`

### `def test___digital_single_channel_writer___write_many_sample_port_uint32(benchmark: BenchmarkFixture, do_port32_benchmark_task: nidaqmx.Task, num_samples: int) -> None`

### `def test___digital_single_channel_writer___write_waveform_lines(benchmark: BenchmarkFixture, do_lines_benchmark_task: nidaqmx.Task, num_samples: int, num_lines: int) -> None`

### `def test___digital_single_channel_writer___write_waveform_port(benchmark: BenchmarkFixture, do_port32_benchmark_task: nidaqmx.Task, num_samples: int) -> None`

### `def test___digital_multi_channel_writer___write_one_sample_one_line(benchmark: BenchmarkFixture, do_lines_benchmark_task: nidaqmx.Task, num_channels: int) -> None`

### `def test___digital_multi_channel_writer___write_one_sample_multi_line(benchmark: BenchmarkFixture, do_lines_benchmark_task: nidaqmx.Task, num_channels: int, num_lines: int) -> None`

### `def test___digital_multi_channel_writer___write_many_sample_port_uint32(benchmark: BenchmarkFixture, do_port32_benchmark_task: nidaqmx.Task, num_samples: int) -> None`

### `def test___digital_multi_channel_writer___write_waveform_lines(benchmark: BenchmarkFixture, do_lines_benchmark_task: nidaqmx.Task, num_channels: int, num_samples: int, num_lines: int) -> None`

### `def test___digital_multi_channel_writer___write_waveform_port(benchmark: BenchmarkFixture, do_port32_benchmark_task: nidaqmx.Task, num_samples: int) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/benchmark/test_task.py -->
## PYTHON MODULE: tests/benchmark/test_task.py

### `def _create_analog_data(num_channels, num_samples)`

### `def _create_digital_data(num_channels, num_samples, num_lines)`

### `def test___task___read_analog(benchmark: BenchmarkFixture, ai_benchmark_task: Task, num_channels: int, num_samples: int) -> None`

### `def test___task___read_analog_waveform(benchmark: BenchmarkFixture, ai_benchmark_task: Task, num_channels: int, num_samples: int, waveform_attribute_mode: WaveformAttributeMode) -> None`

### `def test___task___write_analog(benchmark: BenchmarkFixture, ao_benchmark_task: Task, num_channels: int, num_samples: int) -> None`

### `def test___task___write_analog_waveform(benchmark: BenchmarkFixture, ao_benchmark_task: Task, num_channels: int, num_samples: int) -> None`

### `def test___task___read_digital_lines(benchmark: BenchmarkFixture, di_lines_benchmark_task: Task, num_channels: int, num_samples: int, num_lines: int) -> None`

### `def test___task___read_digital_port(benchmark: BenchmarkFixture, di_port32_benchmark_task: Task, num_samples: int) -> None`

### `def test___task___read_digital_lines_waveform(benchmark: BenchmarkFixture, di_lines_benchmark_task: Task, num_channels: int, num_samples: int, num_lines: int) -> None`

### `def test___task___read_digital_port_waveform(benchmark: BenchmarkFixture, di_port32_benchmark_task: Task, num_samples: int) -> None`

### `def test___task___write_digital_lines(benchmark: BenchmarkFixture, do_lines_benchmark_task: Task, num_channels: int, num_samples: int, num_lines: int) -> None`

### `def test___task___write_digital_port(benchmark: BenchmarkFixture, do_port32_benchmark_task: Task, num_samples: int) -> None`

### `def test___task___write_digital_lines_waveform(benchmark: BenchmarkFixture, do_lines_benchmark_task: Task, num_channels: int, num_samples: int, num_lines: int) -> None`

### `def test___task___write_digital_port_waveform(benchmark: BenchmarkFixture, do_port32_benchmark_task: Task, num_samples: int) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/__init__.py -->
## PYTHON MODULE: tests/component/__init__.py

### MODULE DOCSTRING

Component tests for the nidaqmx package.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/_analog_utils.py -->
## PYTHON MODULE: tests/component/_analog_utils.py

### MODULE DOCSTRING

Shared utilities for analog component tests.

### `def _get_voltage_offset_for_chan(chan_index: int) -> float`

### `def _get_voltage_setpoint_for_chan(chan_index: int) -> float`

### `def _get_current_setpoint_for_chan(chan_index: int) -> float`

### `def _get_expected_voltage_for_chan(chan_index: int) -> float`

### `def _volts_to_codes(volts: float, max_code: int=32767, max_voltage: float=10.0) -> int`

### `def _pwr_volts_to_codes(volts: float, codes_per_volt: int=4096) -> int`

### `def _pwr_current_to_codes(current: float, codes_per_amp: int=8192) -> int`

### `def _get_voltage_code_setpoint_for_chan(chan_index: int) -> int`

### `def _get_current_code_setpoint_for_chan(chan_index: int) -> int`

### `def _get_voltage_code_offset_for_chan(chan_index: int) -> int`

### `def _create_constant_waveform(num_samples: int) -> AnalogWaveform`

### `def _create_linear_ramp_waveform(num_samples: int, start_val: float, end_val: float) -> AnalogWaveform`

### `def _create_scaled_int32_ramp_waveform(num_samples: int) -> AnalogWaveform`

### `def _create_float32_ramp_waveform(num_samples: int, start_val: float, end_val: float) -> AnalogWaveform`

### `def _create_non_contiguous_waveform(num_samples: int, start_val: float, end_val: float) -> AnalogWaveform`

### `def _setup_synchronized_waveform_tasks(generate_task, device: nidaqmx.system.Device, num_samples: int, sample_rate: float, voltage_range: tuple[float, float]=(-5.0, 5.0), chan_index: int=0) -> tuple[nidaqmx.Task, nidaqmx.Task, nidaqmx.Task, str]`

Set up synchronized AO, AI, and sample clock tasks for waveform testing.

    Returns:
        tuple: (ao_task, ai_task, sample_clk_task, sample_clk_terminal)
    

### `def _setup_synchronized_multi_channel_waveform_tasks(generate_task, device: nidaqmx.system.Device, num_channels: int, num_samples: int, sample_rate: float, voltage_range: tuple[float, float]=(-5.0, 5.0)) -> tuple[nidaqmx.Task, nidaqmx.Task, nidaqmx.Task, str]`

Set up synchronized multi-channel AO, AI, and sample clock tasks for waveform testing.

    Returns:
        tuple: (ao_task, ai_task, sample_clk_task, sample_clk_terminal)
    

### `def _get_approx_final_value(waveform: AnalogWaveform[Any], epsilon: float)`

### `def _assert_equal_2d(data: list[list[float]], expected: list[list[float]], abs: float) -> None`

- `AI_VOLTAGE_EPSILON = 0.001`

- `AO_VOLTAGE_EPSILON = 0.01`

- `RAW_VOLTAGE_EPSILON = 0.1`

- `VOLTAGE_CODE_EPSILON = round(_volts_to_codes(AI_VOLTAGE_EPSILON))`

- `POWER_EPSILON = 0.001`

- `POWER_BINARY_EPSILON = 1`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/_digital_utils.py -->
## PYTHON MODULE: tests/component/_digital_utils.py

### MODULE DOCSTRING

Shared utilities for digital component tests.

- `_D = TypeVar('_D', bound=numpy.generic)`

### `def _start_di_task(task: nidaqmx.Task) -> None`

### `def _start_do_task(task: nidaqmx.Task, is_port: bool=False, num_chans: int=1) -> None`

### `def _get_num_di_lines_in_task(task: nidaqmx.Task) -> int`

### `def _get_num_do_lines_in_task(task: nidaqmx.Task) -> int`

### `def _get_digital_data_for_sample(num_lines: int, sample_number: int) -> int`

### `def _get_expected_data_for_line(num_samples: int, line_number: int) -> list[int]`

### `def _get_expected_data_for_lines(num_samples: int, first_line: int, num_lines: int) -> list[int]`

### `def _get_digital_data(num_lines: int, num_samples: int) -> list[int]`

### `def _get_expected_digital_port_data_port_major(task: nidaqmx.Task, num_samples: int) -> list[list[int]]`

### `def _get_expected_digital_port_data_sample_major(task: nidaqmx.Task, num_samples: int) -> list[list[int]]`

### `def _get_digital_port_data_for_sample(task: nidaqmx.Task, sample_number: int) -> list[int]`

### `def _get_digital_port_data_port_major(task: nidaqmx.Task, num_samples: int) -> list[list[int]]`

### `def _get_digital_port_data_sample_major(task: nidaqmx.Task, num_samples: int) -> list[list[int]]`

### `def _bool_array_to_int_lsb(bool_array: numpy.typing.NDArray[numpy.bool_]) -> int`

### `def _bool_array_to_int_msb(bool_array: numpy.typing.NDArray[numpy.bool_]) -> int`

### `def _int_to_bool_array(num_lines: int, input: int) -> numpy.typing.NDArray[numpy.bool_]`

### `def _get_waveform_data(waveform: DigitalWaveform[Any]) -> list[int]`

### `def _get_waveform_port_data(waveform: DigitalWaveform[Any]) -> list[int]`

### `def _create_digital_waveform_uint8(num_samples: int, num_lines: int=1, invert: bool=False) -> DigitalWaveform[numpy.uint8]`

### `def _create_digital_waveform(num_samples: int, num_lines: int, dtype: type[TDigitalState], invert: bool=False) -> DigitalWaveform[TDigitalState]`

### `def _create_waveform_for_line(num_samples: int, line_number: int) -> DigitalWaveform[numpy.uint8]`

### `def _create_waveform_for_lines(num_samples: int, first_line: int, num_lines: int, dtype: type[TDigitalState]) -> DigitalWaveform[TDigitalState]`

### `def _create_waveforms_for_mixed_lines(num_samples: int) -> list[DigitalWaveform[AnyDigitalState]]`

### `def _set_waveform_data(num_samples: int, num_lines: int, waveform: DigitalWaveform[Any], expected_data: list[int], invert: bool=False) -> None`

### `def _create_non_contiguous_digital_waveform(num_samples: int, first_line: int, num_lines: int) -> DigitalWaveform[numpy.uint8]`

### `def _read_and_copy(read_func: Callable[[numpy.typing.NDArray[_D]], None], array: numpy.typing.NDArray[_D]) -> numpy.typing.NDArray[_D]`

### `def _validate_waveform_signals(device: nidaqmx.system.device.Device, waveform: DigitalWaveform[Any], lines: list[int] | range) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/_utils.py -->
## PYTHON MODULE: tests/component/_utils.py

### MODULE DOCSTRING

Shared utilities for component tests.

### `def _is_timestamp_close_to_now(timestamp: AnyDateTime, tolerance_seconds: float=1.0) -> bool`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/conftest.py -->
## PYTHON MODULE: tests/component/conftest.py

### MODULE DOCSTRING

Shared fixtures for component tests.

### `def ai_single_channel_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-channel AI task.

### `def ai_single_channel_task_with_timing(ai_single_channel_task: nidaqmx.Task) -> nidaqmx.Task`

Configure a single-channel AI task with timing.

### `def ai_single_channel_task_with_high_rate(task: nidaqmx.Task, sim_charge_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-channel AI task with high sampling rate.

### `def ai_multi_channel_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a multi-channel AI task.

### `def ai_multi_channel_task_with_timing(ai_multi_channel_task: nidaqmx.Task) -> nidaqmx.Task`

Configure a multi-channel AI task with timing.

### `def pwr_single_channel_task(task: nidaqmx.Task, sim_ts_power_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-channel power task.

### `def pwr_multi_channel_task(task: nidaqmx.Task, sim_ts_power_devices: list[nidaqmx.system.Device]) -> nidaqmx.Task`

Configure a multi-channel power task.

### `def di_single_line_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-line digital input task.

### `def di_single_line_timing_task(di_single_line_task: nidaqmx.Task) -> nidaqmx.Task`

Configure timing for a single-line digital input task.

### `def di_single_line_high_rate_task(di_single_line_task: nidaqmx.Task) -> nidaqmx.Task`

Configure a high-rate single-line digital input task.

### `def di_single_channel_multi_line_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-channel multi-line digital input task.

### `def di_single_channel_multi_line_timing_task(di_single_channel_multi_line_task: nidaqmx.Task) -> nidaqmx.Task`

Configure timing for a single-channel multi-line digital input task.

### `def di_single_channel_timing_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure timing for a single-channel digital input task.

### `def di_single_chan_lines_and_port_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-channel multi-line digital input task.

### `def di_multi_channel_multi_line_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a multi-channel digital input task.

### `def di_multi_chan_multi_line_timing_task(di_multi_channel_multi_line_task: nidaqmx.Task) -> nidaqmx.Task`

Configure timing for a multi-channel digital input task.

### `def di_multi_chan_diff_lines_timing_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a multi-channel digital input task.

    This task has three channels made up of different numbers of lines.
    

### `def di_multi_chan_lines_and_port_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a multi-channel digital input task.

    This task has three channels made up of lines and one channel made up of a port.
    

### `def di_single_channel_port_byte_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-channel digital input task with a channel made up of an 8-line port.

### `def di_multi_channel_port_byte_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a multi-channel digital input task with channels made up of 8-line ports.

### `def di_single_channel_port_uint16_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-channel digital input task with a channel made up of an 8-line port.

### `def di_multi_channel_port_uint16_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a multi-channel digital input task with channels made up of 8-line ports.

### `def di_single_channel_port_uint32_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-channel digital input task with a channel made up of a 32-line port.

### `def di_single_channel_port_uint32_timing_task(di_single_channel_port_uint32_task: nidaqmx.Task) -> nidaqmx.Task`

Configure timing for a single-channel digital input task.

    This task has a channel made up of a 32-line port.
    

### `def di_multi_channel_port_uint32_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a multi-channel digital input task.

    This task has channels made up of a 32-line port and two 8-line ports.
    

### `def di_multi_channel_timing_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure timing for a multi-channel digital input task.

### `def ao_single_channel_task(generate_task: Callable[[], nidaqmx.Task], real_x_series_multiplexed_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-channel AO task.

### `def ao_single_channel_task_with_timing(generate_task: Callable[[], nidaqmx.Task], real_x_series_multiplexed_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-channel AO task with timing for waveform testing.

### `def ai_single_channel_loopback_task(generate_task: Callable[[], nidaqmx.Task], real_x_series_multiplexed_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-channel AI loopback task.

### `def ao_multi_channel_task(generate_task: Callable[[], nidaqmx.Task], real_x_series_multiplexed_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a multi-channel AO task.

### `def ao_multi_channel_task_with_timing(generate_task: Callable[[], nidaqmx.Task], real_x_series_multiplexed_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a multi-channel AO task with timing for waveform testing.

### `def ai_multi_channel_loopback_task(generate_task: Callable[[], nidaqmx.Task], real_x_series_multiplexed_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a multi-channel AI loopback task.

### `def do_single_line_task(generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-line DO task.

### `def do_single_line_task_with_timing(generate_task, real_x_series_multiplexed_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-line DO task with timing for waveform testing.

### `def do_single_channel_multi_line_task(generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-channel DO task.

### `def do_single_channel_multi_line_task_with_timing(generate_task, real_x_series_multiplexed_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-channel multi-line DO task with timing for waveform testing.

### `def do_multi_channel_multi_line_task(generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a multi-channel DO task.

### `def do_multi_channel_multi_line_task_with_timing(generate_task, real_x_series_multiplexed_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-channel multi-line DO task with timing for waveform testing.

### `def do_multi_channel_mixed_line_task(generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a multi-channel DO task with a mix of lines.

### `def do_port0_task(generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-channel DO task.

### `def do_port1_task(generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-channel DO task.

### `def do_multi_channel_port_task(generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a multi-channel DO task.

### `def do_multi_channel_port_and_lines_task(generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a multi-channel DO task.

### `def di_single_line_loopback_task(generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-line DI loopback task.

### `def di_multi_line_loopback_task(generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a multi-line DI loopback task.

### `def di_port0_loopback_task(generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-channel DI loopback task.

### `def di_port0_loopback_task_32dio(generate_task: Callable[[], nidaqmx.Task], real_x_series_device_32dio: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-channel DI loopback task.

### `def di_port1_loopback_task(generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-channel DI loopback task.

### `def di_port1_loopback_task_32dio(generate_task: Callable[[], nidaqmx.Task], real_x_series_device_32dio: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-channel DI loopback task.

### `def di_port2_loopback_task(generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-channel DI loopback task.

### `def di_port2_loopback_task_32dio(generate_task: Callable[[], nidaqmx.Task], real_x_series_device_32dio: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a single-channel DI loopback task.

### `def di_multi_channel_port_loopback_task(generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a multi-channel DI loopback task.

### `def di_multi_channel_port_and_lines_loopback_task(generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device) -> nidaqmx.Task`

Configure a multi-channel DI loopback task.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/stream_readers/__init__.py -->
## PYTHON MODULE: tests/component/stream_readers/__init__.py

### MODULE DOCSTRING

Stream readers test module.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/stream_readers/test_analog_multi_channel_reader.py -->
## PYTHON MODULE: tests/component/stream_readers/test_analog_multi_channel_reader.py

### `def test___analog_multi_channel_reader___read_one_sample___returns_valid_samples(ai_multi_channel_task: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_reader___read_one_sample_with_wrong_dtype___raises_error_with_correct_dtype(ai_multi_channel_task: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_reader___read_many_sample___returns_valid_samples(ai_multi_channel_task: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_reader___read_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(ai_multi_channel_task: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_reader___read_waveforms_feature_disabled___raises_feature_not_supported_error(ai_multi_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_reader___read_waveforms___returns_valid_waveforms(ai_multi_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_reader___read_waveforms_no_args___returns_valid_waveforms(ai_multi_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_reader___read_waveforms_in_place___populates_valid_waveforms(ai_multi_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_reader___read_into_undersized_waveforms_without_reallocation___throws_exception(ai_multi_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_reader___read_into_undersized_waveforms___returns_valid_waveforms(ai_multi_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_reader___reuse_waveform_in_place_with_different_sample_counts___populates_valid_waveforms(generate_task: Callable[[], nidaqmx.Task], sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___analog_multi_channel_reader___read_with_wrong_number_of_waveforms___throws_exception(ai_multi_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_reader_with_timing_flag___read_waveforms___only_includes_timing_data(ai_multi_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_reader_with_extended_properties_flag___read_waveforms___only_includes_extended_properties(ai_multi_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_reader_with_both_flags___read_waveforms___includes_both_timing_and_extended_properties(ai_multi_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_reader_with_none_flag___read_waveforms___minimal_waveform_data(ai_multi_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_reader___read_waveforms_read_all_available___returns_valid_waveforms(ai_multi_channel_task_with_timing: nidaqmx.Task) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/stream_readers/test_analog_single_channel_reader.py -->
## PYTHON MODULE: tests/component/stream_readers/test_analog_single_channel_reader.py

### `def test___analog_single_channel_reader___read_one_sample___returns_valid_samples(ai_single_channel_task: nidaqmx.Task) -> None`

### `def test___analog_single_channel_reader___read_many_sample___returns_valid_samples(ai_single_channel_task: nidaqmx.Task) -> None`

### `def test___analog_single_channel_reader___read_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(ai_single_channel_task: nidaqmx.Task) -> None`

### `def test___analog_single_channel_reader___read_waveform_feature_disabled___raises_feature_not_supported_error(ai_single_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_single_channel_reader___read_waveform___returns_valid_waveform(ai_single_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_single_channel_reader___read_waveform_no_args___returns_valid_waveform(ai_single_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_single_channel_reader___read_waveform_in_place___populates_valid_waveform(ai_single_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_single_channel_reader___reuse_waveform_in_place___overwrites_data_timing_and_attributes(generate_task: Callable[[], nidaqmx.Task], sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___analog_single_channel_reader___read_into_undersized_waveform_without_reallocation___throws_exception(ai_single_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_single_channel_reader___read_into_undersized_waveform___returns_valid_waveform(ai_single_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_single_channel_reader___reuse_waveform_in_place_with_different_sample_counts___populates_valid_waveforms(generate_task: Callable[[], nidaqmx.Task], sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___analog_single_channel_reader___read_waveform_high_sample_rate___returns_correct_sample_interval(ai_single_channel_task_with_high_rate: nidaqmx.Task) -> None`

### `def test___analog_single_channel_reader_with_timing_flag___read_waveform___only_includes_timing_data(ai_single_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_single_channel_reader_with_extended_properties_flag___read_waveform___only_includes_extended_properties(ai_single_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_single_channel_reader_with_both_flags___read_waveform___includes_both_timing_and_extended_properties(ai_single_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_single_channel_reader_with_none_flag___read_waveform___minimal_waveform_data(ai_single_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_single_channel_reader___read_waveform_read_all_available___returns_valid_waveform(ai_single_channel_task_with_timing: nidaqmx.Task) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/stream_readers/test_analog_unscaled_reader.py -->
## PYTHON MODULE: tests/component/stream_readers/test_analog_unscaled_reader.py

### `def test___analog_unscaled_reader___read_int16___returns_valid_samples(ai_multi_channel_task: nidaqmx.Task) -> None`

### `def test___analog_unscaled_reader___read_int16___raises_error_with_correct_dtype(ai_multi_channel_task: nidaqmx.Task) -> None`

### `def test___analog_unscaled_reader___read_uint16___returns_valid_samples(ai_multi_channel_task: nidaqmx.Task) -> None`

### `def test___analog_unscaled_reader___read_uint16___raises_error_with_correct_dtype(ai_multi_channel_task: nidaqmx.Task) -> None`

### `def test___analog_unscaled_reader___read_int32___returns_valid_samples(ai_multi_channel_task: nidaqmx.Task) -> None`

### `def test___analog_unscaled_reader___read_int32___raises_error_with_correct_dtype(ai_multi_channel_task: nidaqmx.Task) -> None`

### `def test___analog_unscaled_reader___read_uint32___returns_valid_samples(ai_multi_channel_task: nidaqmx.Task) -> None`

### `def test___analog_unscaled_reader___read_uint32___raises_error_with_correct_dtype(ai_multi_channel_task: nidaqmx.Task) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/stream_readers/test_digital_multi_channel_reader.py -->
## PYTHON MODULE: tests/component/stream_readers/test_digital_multi_channel_reader.py

### `def test___digital_multi_channel_reader___read_one_sample_one_line___returns_valid_samples(di_single_line_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_reader___read_one_sample_one_line_with_wrong_dtype___raises_error_with_correct_dtype(di_single_line_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_reader___read_one_sample_multi_line___returns_valid_samples(di_multi_channel_multi_line_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_reader___read_one_sample_multi_line_jagged___returns_valid_samples(di_multi_channel_port_uint32_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_reader___read_one_sample_multi_line_with_wrong_dtype___raises_error_with_correct_dtype(di_multi_channel_multi_line_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_reader___read_one_sample_port_byte___returns_valid_samples(di_multi_channel_port_byte_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_reader___read_one_sample_port_byte_with_wrong_dtype___raises_error_with_correct_dtype(di_multi_channel_port_byte_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_reader___read_many_sample_port_byte___returns_valid_samples(di_multi_channel_port_byte_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_reader___read_many_sample_port_byte_with_wrong_dtype___raises_error_with_correct_dtype(di_multi_channel_port_byte_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_reader___read_one_sample_port_uint16___returns_valid_samples(di_multi_channel_port_uint16_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_reader___read_one_sample_port_uint16_with_wrong_dtype___raises_error_with_correct_dtype(di_multi_channel_port_uint16_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_reader___read_many_sample_port_uint16___returns_valid_samples(di_multi_channel_port_uint16_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_reader___read_many_sample_port_uint16_with_wrong_dtype___raises_error_with_correct_dtype(di_multi_channel_port_uint16_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_reader___read_one_sample_port_uint32___returns_valid_samples(di_multi_channel_port_uint32_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_reader___read_one_sample_port_uint32_with_wrong_dtype___raises_error_with_correct_dtype(di_multi_channel_port_uint32_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_reader___read_many_sample_port_uint32___returns_valid_samples(di_multi_channel_port_uint32_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_reader___read_many_sample_port_uint32_with_wrong_dtype___raises_error_with_correct_dtype(di_multi_channel_port_uint32_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_multi_line_reader___read_waveforms_feature_disabled___raises_feature_not_supported_error(di_multi_chan_multi_line_timing_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_multi_line_reader___read_waveforms___returns_valid_waveforms(di_multi_chan_multi_line_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_multi_channel_different_lines_reader___read_waveforms___returns_valid_waveforms(di_multi_chan_diff_lines_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_multi_channel_lines_and_port_reader___read_waveforms___returns_valid_waveforms(di_multi_chan_lines_and_port_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_multi_channel_different_lines_reader___read_mismatched_waveforms___throws_exception(di_multi_chan_diff_lines_timing_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_multi_line_reader___read_waveforms_no_args___returns_valid_waveforms(di_multi_chan_multi_line_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_multi_channel_multi_line_reader___read_waveforms_in_place___populates_valid_waveforms(di_multi_chan_multi_line_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_multi_channel_multi_line_reader___reuse_waveform_in_place___overwrites_data_timing_and_attributes(generate_task: Callable[[], nidaqmx.Task], sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_multi_channel_multi_line_reader___read_into_undersized_waveforms_without_reallocation___throws_exception(di_multi_chan_multi_line_timing_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_multi_line_reader___read_into_undersized_waveforms___returns_valid_waveforms(di_multi_chan_multi_line_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_multi_channel_reader___reuse_waveform_in_place_with_different_sample_counts___populates_valid_waveforms(generate_task: Callable[[], nidaqmx.Task], sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_multi_channel_multi_line_reader___read_with_wrong_number_of_waveforms___throws_exception(di_multi_chan_multi_line_timing_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_multi_line_reader_with_timing_flag___read_waveforms___only_includes_timing_data(di_multi_chan_multi_line_timing_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_multi_line_reader_with_extended_properties_flag___read_waveforms___only_includes_extended_properties(di_multi_chan_multi_line_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_multi_channel_multi_line_reader_with_both_flags___read_waveforms___includes_both_timing_and_extended_properties(di_multi_chan_multi_line_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_multi_channel_multi_line_reader_with_none_flag___read_waveforms___minimal_waveform_data(di_multi_chan_multi_line_timing_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_multi_line_reader___read_waveform_all_dtypes___returns_valid_waveform(di_multi_chan_multi_line_timing_task: nidaqmx.Task, dtype, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_multi_channel_multi_line_reader___read_waveforms_read_all_available___returns_valid_waveforms(di_multi_chan_multi_line_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/stream_readers/test_digital_single_channel_reader.py -->
## PYTHON MODULE: tests/component/stream_readers/test_digital_single_channel_reader.py

### `def test___digital_single_channel_reader___read_one_sample_one_line___returns_valid_samples(di_single_line_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_reader___read_one_sample_multi_line___returns_valid_samples(di_single_channel_multi_line_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_reader___read_one_sample_multi_line_with_wrong_dtype___raises_error_with_correct_dtype(di_single_channel_multi_line_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_reader___read_one_sample_port_byte___returns_valid_samples(di_single_channel_port_byte_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_reader___read_one_sample_port_uint16___returns_valid_samples(di_single_channel_port_uint16_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_reader___read_one_sample_port_uint32___returns_valid_samples(di_single_channel_port_uint32_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_reader___read_many_sample_port_byte___returns_valid_samples(di_single_channel_port_byte_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_reader___read_many_sample_port_byte_with_wrong_dtype___raises_error_with_correct_dtype(di_single_channel_port_byte_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_reader___read_many_sample_port_uint16___returns_valid_samples(di_single_channel_port_uint16_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_reader___read_many_sample_port_uint16_with_wrong_dtype___raises_error_with_correct_dtype(di_single_channel_port_uint16_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_reader___read_many_sample_port_uint32___returns_valid_samples(di_single_channel_port_uint32_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_reader___read_many_sample_port_uint32_with_wrong_dtype___raises_error_with_correct_dtype(di_single_channel_port_uint32_task: nidaqmx.Task) -> None`

### `def test___digital_single_line_reader___read_waveform_feature_disabled___raises_feature_not_supported_error(di_single_line_timing_task: nidaqmx.Task) -> None`

### `def test___digital_single_line_reader___read_waveform___returns_valid_waveform(di_single_line_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_single_channel_multi_line_reader___read_waveform___returns_valid_waveform(di_single_channel_multi_line_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_single_line_reader___read_waveform_no_args___returns_valid_waveform(di_single_line_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_single_channel_multi_line_reader___read_waveform_no_args___returns_valid_waveform(di_single_channel_multi_line_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_single_line_reader___read_waveform_in_place___returns_valid_waveform(di_single_line_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_single_channel_multi_line_reader___read_waveform_in_place___returns_valid_waveform(di_single_channel_multi_line_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_single_line_reader___reuse_waveform_in_place___overwrites_data_timing_and_attributes(generate_task: Callable[[], nidaqmx.Task], sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_single_channel_multi_line_reader___reuse_waveform_in_place___overwrites_data_timing_and_attributes(generate_task: Callable[[], nidaqmx.Task], sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_single_line_reader___read_into_undersized_waveform_without_reallocation___throws_exception(di_single_line_timing_task: nidaqmx.Task) -> None`

### `def test___digital_single_line_reader___read_into_undersized_waveform___returns_valid_waveform(di_single_line_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_single_channel_reader___reuse_waveform_in_place_with_different_sample_counts___populates_valid_waveforms(generate_task: Callable[[], nidaqmx.Task], sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_single_line_reader___read_waveform_high_sample_rate___returns_correct_sample_interval(di_single_line_high_rate_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_single_line_reader_with_timing_flag___read_waveform___only_includes_timing_data(di_single_line_timing_task: nidaqmx.Task) -> None`

### `def test___digital_single_line_reader_with_extended_properties_flag___read_waveform___only_includes_extended_properties(di_single_line_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_single_line_reader_with_both_flags___read_waveform___includes_both_timing_and_extended_properties(di_single_line_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_single_line_reader_with_none_flag___read_waveform___minimal_waveform_data(di_single_line_timing_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_port_uint32_reader___read_waveform___returns_valid_waveform(di_single_channel_port_uint32_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_single_channel_lines_and_port___read_waveform___returns_valid_waveform(di_single_chan_lines_and_port_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_single_channel_multi_line_reader___read_waveform_all_dtypes___returns_valid_waveform(di_single_channel_multi_line_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device, dtype) -> None`

### `def test___digital_single_line_reader___read_waveform_read_all_available___returns_valid_waveform(di_single_line_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/stream_readers/test_power_readers_ai.py -->
## PYTHON MODULE: tests/component/stream_readers/test_power_readers_ai.py

### `def test___power_single_channel_reader___read_one_sample___returns_valid_samples(pwr_single_channel_task: nidaqmx.Task) -> None`

### `def test___power_single_channel_reader___read_many_sample___returns_valid_samples(pwr_single_channel_task: nidaqmx.Task) -> None`

### `def test___power_single_channel_reader___read_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(pwr_single_channel_task: nidaqmx.Task, voltage_dtype: numpy.typing.DTypeLike, current_dtype: numpy.typing.DTypeLike) -> None`

### `def test___power_multi_channel_reader___read_one_sample___returns_valid_samples(pwr_multi_channel_task: nidaqmx.Task) -> None`

### `def test___power_multi_channel_reader___read_one_sample_with_wrong_dtype___raises_error_with_correct_dtype(pwr_multi_channel_task: nidaqmx.Task, voltage_dtype: numpy.typing.DTypeLike, current_dtype: numpy.typing.DTypeLike) -> None`

### `def test___power_multi_channel_reader___read_many_sample___returns_valid_samples(pwr_multi_channel_task: nidaqmx.Task) -> None`

### `def test___power_multi_channel_reader___read_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(pwr_multi_channel_task: nidaqmx.Task, voltage_dtype: numpy.typing.DTypeLike, current_dtype: numpy.typing.DTypeLike) -> None`

### `def test___power_binary_reader___read_many_sample___returns_valid_samples(pwr_multi_channel_task: nidaqmx.Task) -> None`

### `def test___power_binary_reader___read_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(pwr_multi_channel_task: nidaqmx.Task, voltage_dtype: numpy.typing.DTypeLike, voltage_default: float | int, current_dtype: numpy.typing.DTypeLike, current_default: float | int) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/stream_writers/test_analog_multi_channel_writer.py -->
## PYTHON MODULE: tests/component/stream_writers/test_analog_multi_channel_writer.py

### `def test___analog_multi_channel_writer___write_one_sample___updates_output(ao_multi_channel_task: nidaqmx.Task, ai_multi_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_writer___write_one_sample_with_wrong_dtype___raises_error_with_correct_dtype(ao_multi_channel_task: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_writer___write_many_sample___updates_output(ao_multi_channel_task: nidaqmx.Task, ai_multi_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_writer___write_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(ao_multi_channel_task: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_writer___write_waveforms_feature_disabled___raises_feature_not_supported_error(ao_multi_channel_task: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_writer___write_waveforms___output_matches_final_values(ao_multi_channel_task: nidaqmx.Task, ai_multi_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_writer___write_waveforms_with_float32_dtype___output_matches_final_values(ao_multi_channel_task: nidaqmx.Task, ai_multi_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_writer___write_waveforms_with_scaling___output_matches_final_values(ao_multi_channel_task: nidaqmx.Task, ai_multi_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_writer___write_waveforms_with_non_contiguous_data___output_matches_final_values(ao_multi_channel_task: nidaqmx.Task, ai_multi_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_writer___write_waveforms_with_different_lengths___raises_error(ao_multi_channel_task: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_writer___write_waveforms_with_wrong_number_of_channels___raises_daq_error(ao_multi_channel_task: nidaqmx.Task) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/stream_writers/test_analog_single_channel_writer.py -->
## PYTHON MODULE: tests/component/stream_writers/test_analog_single_channel_writer.py

### `def test___analog_single_channel_writer___write_one_sample___updates_output(ao_single_channel_task: nidaqmx.Task, ai_single_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___analog_single_channel_writer___write_many_sample___updates_output(ao_single_channel_task: nidaqmx.Task, ai_single_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___analog_single_channel_writer___write_many_sample_with_wrong_dtype___raises_error_with_correct_dtype(ao_single_channel_task: nidaqmx.Task) -> None`

### `def test___analog_single_channel_reader___read_waveform_feature_disabled___raises_feature_not_supported_error(ao_single_channel_task: nidaqmx.Task) -> None`

### `def test___analog_single_channel_writer___write_waveform___output_matches_final_value(ao_single_channel_task: nidaqmx.Task, ai_single_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___analog_single_channel_writer___write_waveform_with_float32_dtype___output_matches_final_value(ao_single_channel_task: nidaqmx.Task, ai_single_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___analog_single_channel_writer___write_waveform_with_scaling___output_matches_final_value(ao_single_channel_task: nidaqmx.Task, ai_single_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___analog_single_channel_writer___write_waveform_with_non_contiguous_data___output_matches_final_value(ao_single_channel_task: nidaqmx.Task, ai_single_channel_loopback_task: nidaqmx.Task) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/stream_writers/test_analog_unscaled_writer.py -->
## PYTHON MODULE: tests/component/stream_writers/test_analog_unscaled_writer.py

### `def test___analog_unscaled_writer___write_int16___updates_output(ao_multi_channel_task: nidaqmx.Task, ai_multi_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___analog_unscaled_writer___write_int16_with_wrong_dtype___raises_error_with_correct_dtype(ao_multi_channel_task: nidaqmx.Task) -> None`

### `def test___analog_unscaled_writer___write_int32___updates_output(ao_multi_channel_task: nidaqmx.Task, ai_multi_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___analog_unscaled_writer___write_int32_with_wrong_dtype___raises_error_with_correct_dtype(ao_multi_channel_task: nidaqmx.Task) -> None`

### `def test___analog_unscaled_writer___write_uint16___updates_output(ao_multi_channel_task: nidaqmx.Task, ai_multi_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___analog_unscaled_writer___write_uint16_with_wrong_dtype___raises_error_with_correct_dtype(ao_multi_channel_task: nidaqmx.Task) -> None`

### `def test___analog_unscaled_writer___write_uint32___updates_output(ao_multi_channel_task: nidaqmx.Task, ai_multi_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___analog_unscaled_writer___write_uint32_with_wrong_dtype___raises_error_with_correct_dtype(ao_multi_channel_task: nidaqmx.Task) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/stream_writers/test_digital_multi_channel_writer.py -->
## PYTHON MODULE: tests/component/stream_writers/test_digital_multi_channel_writer.py

### `def test___digital_multi_channel_writer___write_one_sample_one_line___updates_output(do_single_line_task: nidaqmx.Task, di_single_line_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_writer___write_one_sample_multi_line___updates_output(do_multi_channel_multi_line_task: nidaqmx.Task, di_multi_line_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_writer___write_one_sample_multi_line_jagged___updates_output(di_port0_loopback_task_32dio: nidaqmx.Task, di_port1_loopback_task_32dio: nidaqmx.Task, di_port2_loopback_task_32dio: nidaqmx.Task, generate_task: Callable[[], nidaqmx.Task], real_x_series_device_32dio: nidaqmx.system.Device) -> None`

### `def test___digital_multi_channel_writer___write_one_sample_multi_line_with_wrong_dtype___raises_error_with_correct_dtype(do_multi_channel_multi_line_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_writer___write_one_sample_port_byte___updates_output(do_multi_channel_port_task: nidaqmx.Task, di_multi_channel_port_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_writer___write_one_sample_port_byte_with_wrong_dtype___raises_error_with_correct_dtype(do_multi_channel_port_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_writer___write_many_sample_port_byte___updates_output(do_multi_channel_port_task: nidaqmx.Task, di_multi_channel_port_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_writer___write_many_sample_port_byte_with_wrong_dtype___raises_error_with_correct_dtype(do_multi_channel_port_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_writer___write_one_sample_port_uint16___updates_output(do_multi_channel_port_task: nidaqmx.Task, di_multi_channel_port_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_writer___write_one_sample_port_uint16_with_wrong_dtype___raises_error_with_correct_dtype(do_multi_channel_port_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_writer___write_many_sample_port_uint16___updates_output(do_multi_channel_port_task: nidaqmx.Task, di_multi_channel_port_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_writer___write_many_sample_port_uint16_with_wrong_dtype___raises_error_with_correct_dtype(do_multi_channel_port_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_writer___write_one_sample_port_uint32___updates_output(do_multi_channel_port_task: nidaqmx.Task, di_multi_channel_port_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_writer___write_one_sample_port_uint32_with_wrong_dtype___raises_error_with_correct_dtype(do_multi_channel_port_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_writer___write_many_sample_port_uint32___updates_output(do_multi_channel_port_task: nidaqmx.Task, di_multi_channel_port_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_writer___write_many_sample_port_uint32_with_wrong_dtype___raises_error_with_correct_dtype(do_multi_channel_port_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_writer___write_waveforms_feature_disabled___raises_feature_not_supported_error(do_multi_channel_multi_line_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_writer___write_waveforms_single_lines___outputs_match_final_values(do_multi_channel_multi_line_task: nidaqmx.Task, di_multi_line_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_writer___write_waveforms_mixed_lines___outputs_match_final_values(do_multi_channel_mixed_line_task: nidaqmx.Task, di_multi_line_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_writer___write_waveforms_with_auto_start___output_matches_final_value(do_multi_channel_multi_line_task_with_timing: nidaqmx.Task, di_multi_line_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_writer___write_waveforms_ports___outputs_match_final_values(do_multi_channel_port_task: nidaqmx.Task, di_multi_channel_port_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_writer___write_waveforms_port_and_lines___outputs_match_final_values(do_multi_channel_port_and_lines_task: nidaqmx.Task, di_multi_channel_port_and_lines_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_writer___write_waveforms_with_non_contiguous_data___outputs_match_final_values(do_multi_channel_multi_line_task: nidaqmx.Task, di_multi_line_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_writer___write_waveforms_with_different_sample_counts___raises_error(do_multi_channel_port_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_writer___write_waveforms_with_too_many___raises_daq_error(do_multi_channel_port_task: nidaqmx.Task) -> None`

### `def test___digital_multi_channel_writer___write_waveforms_with_too_many_signals___raises_daq_error(do_multi_channel_port_task: nidaqmx.Task) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/stream_writers/test_digital_single_channel_writer.py -->
## PYTHON MODULE: tests/component/stream_writers/test_digital_single_channel_writer.py

### `def test___digital_single_channel_writer___write_one_sample_one_line___updates_output(do_single_line_task: nidaqmx.Task, di_single_line_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_writer___write_one_sample_multi_line___updates_output(do_single_channel_multi_line_task: nidaqmx.Task, di_multi_line_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_writer___write_one_sample_multi_line_with_wrong_dtype___raises_error_with_correct_dtype(do_single_channel_multi_line_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_writer___write_one_sample_port_byte___updates_output(do_port1_task: nidaqmx.Task, di_port1_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_writer___write_many_sample_port_byte___updates_output(do_port1_task: nidaqmx.Task, di_port1_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_writer___write_many_sample_port_byte_with_wrong_dtype___raises_error_with_correct_dtype(do_port1_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_writer___write_one_sample_port_uint16___updates_output(do_port1_task: nidaqmx.Task, di_port1_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_writer___write_many_sample_port_uint16___updates_output(do_port1_task: nidaqmx.Task, di_port1_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_writer___write_many_sample_port_uint16_with_wrong_dtype___raises_error_with_correct_dtype(do_port1_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_writer___write_one_sample_port_uint32___updates_output(do_port0_task: nidaqmx.Task, di_port0_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_writer___write_many_sample_port_uint32___updates_output(do_port0_task: nidaqmx.Task, di_port0_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_writer___write_many_sample_port_uint32_with_wrong_dtype___raises_error_with_correct_dtype(do_port0_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_writer___write_waveform_feature_disabled___raises_feature_not_supported_error(do_single_line_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_writer___write_waveform_single_line___outputs_match_final_values(do_single_line_task: nidaqmx.Task, di_single_line_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_writer___write_waveform_single_line_with_auto_start___output_matches_final_value(do_single_line_task_with_timing: nidaqmx.Task, di_single_line_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_writer___write_waveform_single_line_with_non_contiguous_data___outputs_match_final_values(do_single_line_task: nidaqmx.Task, di_single_line_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_writer___write_waveform_single_line_signal_count_mismatch___raises_daq_error(do_single_line_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_writer___write_waveform_single_line_all_dtypes___outputs_match_final_values(do_single_line_task: nidaqmx.Task, di_single_line_loopback_task: nidaqmx.Task, dtype) -> None`

### `def test___digital_single_channel_writer___write_waveform_multi_line___outputs_match_final_values(do_single_channel_multi_line_task: nidaqmx.Task, di_multi_line_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_writer___write_waveform_multi_line_with_auto_start___output_matches_final_value(do_single_channel_multi_line_task_with_timing: nidaqmx.Task, di_multi_line_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_writer___write_waveform_multi_line_with_non_contiguous_data___outputs_match_final_values(do_single_channel_multi_line_task: nidaqmx.Task, di_multi_line_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_writer___write_waveform_multi_line_all_dtypes___outputs_match_final_values(do_single_channel_multi_line_task: nidaqmx.Task, di_multi_line_loopback_task: nidaqmx.Task, dtype) -> None`

### `def test___digital_single_channel_writer___write_waveform_multi_line_signal_count_mismatch___raises_daq_error(do_single_channel_multi_line_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_writer___write_waveform_port_uint8___outputs_match_final_values(do_port1_task: nidaqmx.Task, di_port1_loopback_task: nidaqmx.Task) -> None`

### `def test___digital_single_channel_writer___write_waveform_port_uint32___outputs_match_final_values(do_port0_task: nidaqmx.Task, di_port0_loopback_task: nidaqmx.Task) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/system/__init__.py -->
## PYTHON MODULE: tests/component/system/__init__.py

### MODULE DOCSTRING

Component tests for nidaqmx.system.*.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/system/_collections/__init__.py -->
## PYTHON MODULE: tests/component/system/_collections/__init__.py

### MODULE DOCSTRING

Component tests for nidaqmx.system.storage._collections.*.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/system/_collections/test_device_collection.py -->
## PYTHON MODULE: tests/component/system/_collections/test_device_collection.py

### `def test___devices___getitem_int___forward_order(system: System)`

### `def test___devices___getitem_int___shared_interpreter(system: System)`

### `def test___devices___getitem_slice___forward_order(system: System)`

### `def test___devices___getitem_slice___shared_interpreter(system: System)`

### `def test___devices___getitem_str___shared_interpreter(system: System)`

### `def test___devices___getitem_str_list___shared_interpreter(system: System)`

### `def test___devices___iter___forward_order(system: System)`

### `def test___devices___iter___shared_interpreter(system: System)`

### `def test___devices___reversed___reverse_order(system: System)`

### `def test___devices___reversed___shared_interpreter(system: System)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/system/_collections/test_persisted_channel_collection.py -->
## PYTHON MODULE: tests/component/system/_collections/test_persisted_channel_collection.py

### `def test___global_channels___getitem_int___forward_order(system: System)`

### `def test___global_channels___getitem_int___shared_interpreter(system: System)`

### `def test___global_channels___getitem_slice___forward_order(system: System)`

### `def test___global_channels___getitem_slice___shared_interpreter(system: System)`

### `def test___global_channels___getitem_str___shared_interpreter(system: System)`

### `def test___global_channels___getitem_str_list___shared_interpreter(system: System)`

### `def test___global_channels___iter___forward_order(system: System)`

### `def test___global_channels___iter___shared_interpreter(system: System)`

### `def test___global_channels___reversed___reverse_order(system: System)`

### `def test___global_channels___reversed___shared_interpreter(system: System)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/system/_collections/test_persisted_scale_collection.py -->
## PYTHON MODULE: tests/component/system/_collections/test_persisted_scale_collection.py

### `def test___scales___getitem_int___forward_order(system: System)`

### `def test___scales___getitem_int___shared_interpreter(system: System)`

### `def test___scales___getitem_slice___forward_order(system: System)`

### `def test___scales___getitem_slice___shared_interpreter(system: System)`

### `def test___scales___getitem_str___shared_interpreter(system: System)`

### `def test___scales___getitem_str_list___shared_interpreter(system: System)`

### `def test___scales___iter___forward_order(system: System)`

### `def test___scales___iter___shared_interpreter(system: System)`

### `def test___scales___reversed___reverse_order(system: System)`

### `def test___scales___reversed___shared_interpreter(system: System)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/system/_collections/test_persisted_task_collection.py -->
## PYTHON MODULE: tests/component/system/_collections/test_persisted_task_collection.py

### `def test___tasks___getitem_int___forward_order(system: System)`

### `def test___tasks___getitem_int___shared_interpreter(system: System)`

### `def test___tasks___getitem_slice___forward_order(system: System)`

### `def test___tasks___getitem_slice___shared_interpreter(system: System)`

### `def test___tasks___getitem_str___shared_interpreter(system: System)`

### `def test___tasks___getitem_str_list___shared_interpreter(system: System)`

### `def test___tasks___iter___forward_order(system: System)`

### `def test___tasks___iter___shared_interpreter(system: System)`

### `def test___tasks___reversed___reverse_order(system: System)`

### `def test___tasks___reversed___shared_interpreter(system: System)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/system/_collections/test_physical_channel_collection.py -->
## PYTHON MODULE: tests/component/system/_collections/test_physical_channel_collection.py

- `COLLECTION_NAMES = ['ai_physical_chans', 'ao_physical_chans', 'ci_physical_chans', 'co_physical_chans', 'di_lines', 'di_ports', 'do_lines', 'do_ports']`

### `def test___physical_channels___getitem_int___forward_order(collection_name: str, sim_6363_device: Device)`

### `def test___physical_channels___getitem_int___shared_interpreter(collection_name: str, sim_6363_device: Device)`

### `def test___physical_channels___getitem_slice___forward_order(collection_name: str, sim_6363_device: Device)`

### `def test___physical_channels___getitem_slice___shared_interpreter(collection_name: str, sim_6363_device: Device)`

### `def test___physical_channels___getitem_unqualified_str___shared_interpreter(collection_name: str, sim_6363_device: Device)`

### `def test___physical_channels___getitem_unqualified_str_list___shared_interpreter(collection_name: str, sim_6363_device: Device)`

### `def test___physical_channels___getitem_unqualified_str___name(collection_name: str, sim_6363_device: Device)`

### `def test___physical_channels___getitem_unqualified_str_list___name(collection_name: str, sim_6363_device: Device)`

### `def test___physical_channels___getitem_qualified_str___shared_interpreter(collection_name: str, sim_6363_device: Device)`

### `def test___physical_channels___getitem_qualified_str_list___shared_interpreter(collection_name: str, sim_6363_device: Device)`

### `def test___physical_channels___getitem_qualified_str___name(collection_name: str, sim_6363_device: Device)`

### `def test___physical_channels___getitem_qualified_str_list___name(collection_name: str, sim_6363_device: Device)`

### `def test___physical_channels___getitem_mixed_str_list___shared_interpreter(collection_name: str, sim_6363_device: Device)`

### `def test___physical_channels___getitem_mixed_str_list___name(collection_name: str, sim_6363_device: Device)`

### `def test___physical_channels___getitem_qualified_internal_channel_list___name(collection_name: str, sim_6363_device: Device)`

### `def test___physical_channels___getitem_unqualified_internal_channel_list___name(collection_name: str, sim_6363_device: Device)`

### `def test___physical_channels___iter___forward_order(collection_name: str, sim_6363_device: Device)`

### `def test___physical_channels___iter___shared_interpreter(collection_name: str, sim_6363_device: Device)`

### `def test___physical_channels___reversed___reverse_order(collection_name: str, sim_6363_device: Device)`

### `def test___physical_channels___reversed___shared_interpreter(collection_name: str, sim_6363_device: Device)`

### `def test___physical_channels___all___forward_order(collection_name: str, sim_6363_device: Device)`

### `def test___physical_channels___all___shared_interpreter(collection_name: str, sim_6363_device: Device)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/system/storage/__init__.py -->
## PYTHON MODULE: tests/component/system/storage/__init__.py

### MODULE DOCSTRING

Component tests for nidaqmx.system.storage.*.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/system/storage/test_persisted_channel.py -->
## PYTHON MODULE: tests/component/system/storage/test_persisted_channel.py

### `def ai_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task`

Gets an AI task.

### `def test___persisted_channels_with_same_name___compare___equal(init_kwargs)`

### `def test___persisted_channels_with_different_names___compare___not_equal(init_kwargs)`

### `def test___persisted_channels_with_same_name___hash___equal(init_kwargs)`

### `def test___persisted_channels_with_different_names___hash___not_equal(init_kwargs)`

### `def test___save_persisted_channel___saves_persisted_channel_with_author(ai_task: nidaqmx.Task, init_kwargs: dict) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/system/storage/test_persisted_channel_properties.py -->
## PYTHON MODULE: tests/component/system/storage/test_persisted_channel_properties.py

### `def test___constructed_persisted_channel___get_property___returns_persisted_value(init_kwargs)`

### `def test___nonexistent_persisted_channel___get_property___raises_invalid_global_chan(init_kwargs)`

### `def test___persisted_channel___get_bool_property___returns_persisted_value(persisted_channel)`

### `def test___persisted_channel___get_string_property___returns_persisted_value(persisted_channel)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/system/storage/test_persisted_scale.py -->
## PYTHON MODULE: tests/component/system/storage/test_persisted_scale.py

### `def test___persisted_scales_with_same_name___compare___equal(init_kwargs)`

### `def test___persisted_scales_with_different_names___compare___not_equal(init_kwargs)`

### `def test___persisted_scales_with_same_name___hash___equal(init_kwargs)`

### `def test___persisted_scales_with_different_names___hash___not_equal(init_kwargs)`

### `def test___persisted_scale___load___shared_interpreter(persisted_scale: PersistedScale)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/system/storage/test_persisted_scale_properties.py -->
## PYTHON MODULE: tests/component/system/storage/test_persisted_scale_properties.py

### `def test___constructed_persisted_scale___get_property___returns_persisted_value(init_kwargs)`

### `def test___nonexistent_persisted_scale___get_property___raises_custom_scale_does_not_exist(init_kwargs)`

### `def test___persisted_scale___get_bool_property___returns_persisted_value(persisted_scale)`

### `def test___persisted_scale___get_string_property___returns_persisted_value(persisted_scale)`

### `def test___persisted_scale___load_and_get_float64_property___returns_persisted_value(persisted_scale)`

### `def test___persisted_scale___load_and_get_float64_list_property___returns_persisted_value(persisted_scale)`

### `def test___persisted_scale___load_and_get_string_property___returns_persisted_value(persisted_scale)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/system/storage/test_persisted_task.py -->
## PYTHON MODULE: tests/component/system/storage/test_persisted_task.py

### `def test___persisted_tasks_with_same_name___compare___equal(init_kwargs)`

### `def test___persisted_tasks_with_different_names___compare___not_equal(init_kwargs)`

### `def test___persisted_tasks_with_same_name___hash___equal(init_kwargs)`

### `def test___persisted_tasks_with_different_names___hash___not_equal(init_kwargs)`

### `def test___persisted_task___load_and_read___returns_persisted_sample_count(persisted_task: PersistedTask)`

### `def test___persisted_task___load_twice___raises_duplicate_task(persisted_task: PersistedTask)`

### `def test___grpc_session_initialization_behavior_auto___load_twice___returns_multiple_task_proxies(persisted_task: PersistedTask)`

### `def test___grpc_session_initialization_behavior_initialize_server_session___load_twice___raises_duplicate_task(persisted_task: PersistedTask)`

### `def test___persisted_task___load___shared_interpreter(persisted_task: PersistedTask)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/system/storage/test_persisted_task_properties.py -->
## PYTHON MODULE: tests/component/system/storage/test_persisted_task_properties.py

### `def test___constructed_persisted_task___get_property___returns_persisted_value(init_kwargs)`

### `def test___nonexistent_persisted_task___get_property___raises_task_not_in_data_neighborhood(init_kwargs)`

### `def test___persisted_task___get_bool_property___returns_persisted_value(persisted_task: PersistedTask)`

### `def test___persisted_task___get_string_property___returns_persisted_value(persisted_task: PersistedTask)`

### `def test___persisted_task___load_and_get_channel_properties___returns_persisted_values(persisted_task: PersistedTask)`

### `def test___persisted_task___load_and_get_task_properties___returns_persisted_values(persisted_task: PersistedTask)`

### `def test___persisted_task___load_and_get_timing_properties___returns_persisted_values(persisted_task: PersistedTask)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/system/test_device.py -->
## PYTHON MODULE: tests/component/system/test_device.py

### `def test___devices_with_same_name___compare___equal(init_kwargs)`

### `def test___devices_with_different_names___compare___not_equal(init_kwargs)`

### `def test___devices_with_same_name___hash___equal(init_kwargs)`

### `def test___devices_with_different_names___hash___not_equal(init_kwargs)`

### `def test___self_test_device___no_errors(sim_6363_device: Device) -> None`

### `def test___restore_last_ext_cal_const___no_errors(sim_6363_device: Device) -> None`

### `def test___self_cal___no_errors(sim_6363_device: Device) -> None`

### `def test___read_id_pin_memory___error(sim_6423_device: Device) -> None`

### `def test___write_id_pin_memory___error(sim_6423_device: Device) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/system/test_device_properties.py -->
## PYTHON MODULE: tests/component/system/test_device_properties.py

### `def test___constructed_device___get_property___returns_value(init_kwargs)`

### `def test___nonexistent_device___get_property___raises_invalid_device_id(init_kwargs)`

### `def test___device___bool_property___returns_value(device)`

### `def test___device___float_property___returns_value(device)`

### `def test___device___uint_property___returns_value(device)`

### `def test___device___string_property___returns_value(device)`

### `def test___device___enum_property___returns_value(device)`

### `def test___device___list_of_float_property___returns_value(device)`

### `def test___device___list_of_enum_property___returns_value(device)`

### `def test___device___list_of_uint_property___returns_value(device)`

### `def test___device___get_deprecated_properties___reports_warnings(device)`

### `def test___chassis___get_modules___returns_modules(device: Device)`

### `def test___chassis___get_modules___shared_interpreter(device: Device)`

### `def test___module___get_chassis___returns_chassis(device: Device)`

### `def test___module___get_chassis___shared_interpreter(device: Device)`

### `def test___ext_cal_last_date_and_time___no_errors(real_x_series_device: Device) -> None`

### `def test___self_cal_last_date_and_time___no_errors(real_x_series_device: Device) -> None`

### `def test___device_supports_cal___no_errors(real_x_series_device: Device) -> None`

### `def test___cal_acc_connection_count__raises_attr_not_supported(real_x_series_device: Device) -> None`

### `def test___cal_recommended_acc_connection_count_limit___raises_attr_not_supported(real_x_series_device: Device) -> None`

### `def test___cal_user_defined_info___no_errors(real_x_series_device: Device) -> None`

### `def test___cal_dev_temp___no_errors(sim_6363_device: Device) -> None`

### `def test___ext_cal_last_temp___no_errors(sim_6363_device: Device) -> None`

### `def test___ext_cal_recommended_interval___no_errors(sim_6363_device: Device) -> None`

### `def test___self_cal_last_temp___no_errors(sim_6363_device: Device) -> None`

### `def test___self_cal_supported___no_errors(real_x_series_device: Device) -> None`

### `def test___id_pin_mem_serial_nums___no_errors(sim_6423_device: Device) -> None`

### `def test___id_pin_mem_family_codes___no_errors(sim_6423_device: Device) -> None`

### `def test___id_pin_mem_sizes___no_errors(sim_6423_device: Device) -> None`

### `def test___id_pin_pin_names___no_errors(sim_6423_device: Device) -> None`

### `def test___id_pin_pin_statuses___no_errors(sim_6423_device: Device) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/system/test_physical_channel.py -->
## PYTHON MODULE: tests/component/system/test_physical_channel.py

### `def test___physical_channels_with_same_name___compare___equal(init_kwargs)`

### `def test___physical_channels_with_different_names___compare___not_equal(init_kwargs)`

### `def test___physical_channels_with_same_name___hash___equal(init_kwargs)`

### `def test___physical_channels_with_different_names___hash___not_equal(init_kwargs)`

### `def test___invalid_bitstream___write_to_teds_from_array___throws_data_error(sim_6363_device)`

### `def test___valid_bitstream___write_to_teds_from_array___throws_config_or_detection_error(sim_6363_device)`

### `def test___invalid_file_path___write_to_teds_from_file___throws_data_error(sim_6363_device)`

### `def test___valid_file_path___write_to_teds_from_array___throws_config_or_detection_error(sim_6363_device, voltage_teds_file_path)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/system/test_physical_channel_properties.py -->
## PYTHON MODULE: tests/component/system/test_physical_channel_properties.py

### `def test___constructed_physical_channel___get_property___returns_value(init_kwargs)`

### `def test___nonexistent_physical_channel___get_property___raises_physical_chan_does_not_exist(init_kwargs)`

### `def test___physical_channel___get_bool_property___returns_value(sim_6363_device)`

### `def test___physical_channel_with_teds___get_bit_stream___returns_configured_value(sim_6363_device, voltage_teds_file_path)`

### `def test___physical_channel___get_int32_array_property___returns_default_value(sim_6363_device)`

### `def test___physical_channel_with_teds___get_string_property___returns_configured_value(sim_6363_device, voltage_teds_file_path)`

### `def test___physical_channel_with_teds___get_uint32_array_property___returns_configured_value(sim_6363_device, voltage_teds_file_path)`

### `def test___physical_channel_with_teds___get_uint32_property___returns_configured_value(sim_6363_device, voltage_teds_file_path)`

### `def test___physical_channel___get_int32_property___returns_value()`

### `def test___physical_channel___set_int32_property___success()`

- `VALUES_IN_TED = [17, 64, 0, 32, 4, 57, 48, 0, 120, 0, 0, 0, 200, 194, 0, 0, 200, 66, 0, 0, 0, 0, 0, 0, 0, 0, 0, 48]`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/system/test_system.py -->
## PYTHON MODULE: tests/component/system/test_system.py

### `def test___get_analog_power_up_states_with_output_type___returns_power_up_states(system)`

### `def test_valid_power_up_states___set_analog_power_up_states_with_output_type___sets_power_up_states_without_errors(system)`

### `def test_invalid_power_up_states___set_analog_power_up_states_with_output_type___throws_invalid_attribute_value_error(system)`

### `def test___get_analog_power_up_states___returns_power_up_states(system)`

### `def test_valid_power_up_states___set_analog_power_up_states___sets_power_up_states_without_errors(system)`

### `def test_invalid_power_up_states___set_analog_power_up_states___throws_invalid_attribute_value_error(system)`

### `def test___system___set_nonexistent_property___raises_exception(system: System)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/system/test_watchdog_properties.py -->
## PYTHON MODULE: tests/component/system/test_watchdog_properties.py

### `def test___watchdog_task___get_expired___returns_false(watchdog_task)`

### `def test___watchdog_task___set_boolean_property___returns_assigned_value(watchdog_task)`

### `def test___watchdog_task___reset_boolean_property___returns_default_value(watchdog_task)`

### `def test___watchdog_task___task_not_running_get_expired_property____throws_daqerror(watchdog_task)`

### `def test___watchdog_task___get_enum_property___returns_value(sim_6363_device, watchdog_task)`

### `def test___watchdog_task___set_enum_property___returns_assigned_value(sim_6363_device, watchdog_task)`

### `def test___watchdog_task___reset_enum_property___returns_default_value(sim_6363_device, watchdog_task)`

### `def test___watchdog_task___get_float64_property___returns_value(sim_6363_device, watchdog_task)`

### `def test___watchdog_task___set_float64_property___returns_assigned_value(sim_6363_device, watchdog_task)`

### `def test___watchdog_task___reset_float64_property___returns_default_value(sim_6363_device, watchdog_task)`

### `def test___watchdog_task___get_string_property___returns_value(sim_6363_device, watchdog_task)`

### `def test___watchdog_task___set_string_property___returns_assigned_value(sim_6363_device, watchdog_task)`

### `def test___watchdog_task___reset_string_property___returns_default_value(sim_6363_device, watchdog_task)`

### `def test___watchdog_task___get_deprecated_properties___reports_warnings(sim_6363_device, watchdog_task)`

### `def test___watchdog_task___set_deprecated_properties___reports_warnings(sim_6363_device, watchdog_task)`

### `def test___watchdog_task___reset_deprecated_properties___reports_warnings(sim_6363_device, watchdog_task)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/task/__init__.py -->
## PYTHON MODULE: tests/component/task/__init__.py

### MODULE DOCSTRING

Component tests for nidaqmx.task.*.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/task/channels/__init__.py -->
## PYTHON MODULE: tests/component/task/channels/__init__.py

### MODULE DOCSTRING

Component tests for nidaqmx.task.channels.*.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/task/channels/test_ai_channel.py -->
## PYTHON MODULE: tests/component/task/channels/test_ai_channel.py

### `def test___task___add_ai_voltage_chan___sets_channel_attributes(task: Task, sim_6363_device: Device, desired_term_config: TerminalConfiguration, expected_term_cfg: TerminalConfiguration, min_val: float, max_val: float, units: VoltageUnits, custom_scale_name: str) -> None`

### `def test___task___add_teds_ai_voltage_chan___sets_channel_attributes(task: Task, sim_6363_device: Device, voltage_teds_file_path: pathlib.Path) -> None`

### `def test___task___add_ai_accel_4_wire_dc_voltage_chan___sets_channel_attributes(task: Task, sim_charge_device: Device, units: AccelUnits, sensitivity: float, sensitivity_units: AccelSensitivityUnits) -> None`

### `def test___task___add_ai_accel_chan___sets_channel_attributes(task: Task, sim_dsa_device: Device, units: AccelUnits, sensitivity: float, sensitivity_units: AccelSensitivityUnits) -> None`

### `def test___task___add_teds_ai_accel_chan___sets_channel_attributes(task: Task, sim_dsa_device: Device, accelerometer_teds_file_path: pathlib.Path, units: AccelUnits) -> None`

### `def test___task___add_ai_accel_charge_chan___sets_channel_attributes(task: Task, sim_charge_device: Device, units: AccelUnits, sensitivity: float, sensitivity_units: AccelChargeSensitivityUnits) -> None`

### `def test___task___add_ai_bridge_chan___sets_channel_attributes(task: Task, sim_bridge_device: Device, units: BridgeUnits, bridge_config: BridgeConfiguration, nominal_bridge_resistance: float) -> None`

### `def test___task___add_teds_ai_bridge_chan___sets_channel_attributes(task: Task, sim_bridge_device: Device, bridge_teds_file_path: pathlib.Path, voltage_excit_val: float) -> None`

### `def test___task___add_ai_charge_chan___sets_channel_attributes(task: Task, sim_charge_device: Device, units: ChargeUnits) -> None`

### `def test___task___add_ai_current_chan___sets_channel_attributes(task: Task, sim_6363_device: Device, shunt_resistor_loc: CurrentShuntResistorLocation, expected_shunt_resistor_loc: CurrentShuntResistorLocation, ext_shunt_resistor_val: float) -> None`

### `def test___task___add_teds_ai_current_chan___sets_channel_attributes(task: Task, sim_6363_device: Device, current_teds_file_path: pathlib.Path, shunt_resistor_loc: CurrentShuntResistorLocation, expected_shunt_resistor_loc: CurrentShuntResistorLocation, ext_shunt_resistor_val: float) -> None`

### `def test___task___add_ai_current_rms_chan___sets_channel_attributes(task: Task, sim_dmm_device: Device, shunt_resistor_loc: CurrentShuntResistorLocation, expected_shunt_resistor_loc: CurrentShuntResistorLocation) -> None`

### `def test___task___add_ai_force_bridge_polynomial_chan___sets_channel_attributes(task: Task, sim_bridge_device: Device, bridge_config: BridgeConfiguration, nominal_bridge_resistance: float, forward_coeffs: list[float], reverse_coeffs: list[float]) -> None`

### `def test___task___add_ai_force_bridge_table_chan___sets_channel_attributes(task: Task, sim_bridge_device: Device, bridge_config: BridgeConfiguration, nominal_bridge_resistance: float, electrical_vals: list[float], physical_vals: list[float]) -> None`

### `def test___task___add_ai_force_bridge_two_point_lin_chan___sets_channel_attributes(task: Task, sim_bridge_device: Device, bridge_config: BridgeConfiguration, nominal_bridge_resistance: float, first_electrical_val: float, second_electrical_val: float, first_physical_val: float, second_physical_val: float) -> None`

### `def test___task___add_teds_ai_force_bridge_chan___sets_channel_attributes(task: Task, sim_bridge_device: Device, force_bridge_teds_file_path: pathlib.Path) -> None`

### `def test___task___add_ai_force_iepe_chan___sets_channel_attributes(task: Task, sim_dsa_device: Device, units: ForceUnits, sensitivity: float, sensitivity_units: ForceIEPESensorSensitivityUnits) -> None`

### `def test___task___add_teds_ai_force_iepe_chan___sets_channel_attributes(task: Task, sim_dsa_device: Device, force_iepe_teds_file_path: pathlib.Path, units: ForceUnits) -> None`

### `def test___task___add_ai_microphone_chan___sets_channel_attributes(task: Task, sim_dsa_device: Device, mic_sensitivity: float, max_snd_press_level: float) -> None`

### `def test___task___add_teds_ai_microphone_chan___sets_channel_attributes(task: Task, sim_dsa_device: Device, microphone_teds_file_path: pathlib.Path, max_snd_press_level: float) -> None`

### `def test___task___add_ai_pos_eddy_curr_prox_probe_chan___sets_channel_attributes(task: Task, sim_dsa_device: Device, sensitivity_units: EddyCurrentProxProbeSensitivityUnits, sensitivity: float) -> None`

### `def test___task___add_ai_pos_lvdt_chan___sets_channel_attributes(task: Task, sim_position_device: Device, sensitivity_units: LVDTSensitivityUnits, sensitivity: float, ac_excit_wire_mode: ACExcitWireMode, voltage_excit_val: float, voltage_excit_freq: float) -> None`

### `def test___task___add_teds_ai_pos_lvdt_chan___sets_channel_attributes(task: Task, sim_position_device: Device) -> None`

### `def test___task___add_ai_pos_rvdt_chan___sets_channel_attributes(task: Task, sim_position_device: Device) -> None`

### `def test___task___add_teds_ai_pos_rvdt_chan___sets_channel_attributes(task: Task, sim_position_device: Device) -> None`

### `def test___task___add_ai_power_chan___sets_channel_attributes(task: Task, sim_ts_power_device: Device, voltage_setpoint: float, current_setpoint: float, output_enable: bool) -> None`

### `def test___task___add_ai_pressure_bridge_polynomial_chan___sets_channel_attributes(task: Task, sim_bridge_device: Device) -> None`

### `def test___task___add_ai_pressure_bridge_table_chan___sets_channel_attributes(task: Task, sim_bridge_device: Device) -> None`

### `def test___task___add_ai_pressure_bridge_two_point_lin_chan___sets_channel_attributes(task: Task, sim_bridge_device: Device) -> None`

### `def test___task___add_teds_ai_pressure_bridge_chan___sets_channel_attributes(task: Task, sim_bridge_device: Device, pressure_bridge_teds_file_path: pathlib.Path) -> None`

### `def test___task___add_ai_resistance_chan___sets_channel_attributes(task: Task, sim_6363_device: Device, resistance_config: ResistanceConfiguration) -> None`

### `def test___task___add_teds_ai_resistance_chan___sets_channel_attributes(task: Task, sim_6363_device: Device, resistance_teds_file_path: pathlib.Path, resistance_config: ResistanceConfiguration) -> None`

### `def test___task___add_ai_rosette_strain_gage_chan___sets_channel_attributes(task: Task, sim_bridge_device: Device) -> None`

### `def test___task___add_ai_rtd_chan___sets_channel_attributes(task: Task, sim_6363_device: Device, rtd_type: RTDType, resistance_config: ResistanceConfiguration) -> None`

### `def test___task___add_teds_ai_rtd_chan___sets_channel_attributes(task: Task, sim_6363_device: Device, rtd_teds_file_path: pathlib.Path, resistance_config: ResistanceConfiguration) -> None`

### `def test___task___add_ai_strain_gage_chan___sets_channel_attributes(task: Task, sim_bridge_device: Device, strain_config: StrainGageBridgeType, gage_factor: float, nominal_gage_resistance: float) -> None`

### `def test___task___add_ai_teds_strain_gage_chan___sets_channel_attributes(task: Task, sim_bridge_device: Device, strain_gage_teds_file_path: pathlib.Path) -> None`

### `def test___task___add_ai_temp_built_in_sensor_chan___sets_channel_attributes(task: Task, sim_6363_device: Device) -> None`

### `def test___task___add_ai_thrmcpl_chan___sets_channel_attributes(task: Task, sim_temperature_device: Device, thermocouple_type: ThermocoupleType, cjc_source: CJCSource, cjc_val: float) -> None`

### `def test___task___add_teds_ai_thrmcpl_chan___sets_channel_attributes(task: Task, sim_temperature_device: Device, thermocouple_teds_file_path: pathlib.Path, cjc_source: CJCSource, cjc_val: float) -> None`

### `def test___task___add_ai_thrmstr_chan_iex___sets_channel_attributes(task: Task, sim_6363_device: Device, resistance_config: ResistanceConfiguration, a: float, b: float, c: float) -> None`

### `def test___task___add_teds_ai_thrmstr_chan_iex___sets_channel_attributes(task: Task, sim_6363_device: Device, thermistor_iex_teds_file_path: pathlib.Path, resistance_config: ResistanceConfiguration) -> None`

### `def test___task___add_ai_thrmstr_chan_vex___sets_channel_attributes(task: Task, sim_6363_device: Device, units: TemperatureUnits, resistance_config: ResistanceConfiguration) -> None`

### `def test___task___add_teds_ai_thrmstr_chan_vex___sets_channel_attributes(task: Task, sim_6363_device: Device, thermistor_vex_teds_file_path: pathlib.Path, units: TemperatureUnits, resistance_config: ResistanceConfiguration) -> None`

### `def test___task___add_ai_torque_bridge_polynomial_chan___sets_channel_attributes(task: Task, sim_bridge_device: Device) -> None`

### `def test___task___add_ai_torque_bridge_table_chan___sets_channel_attributes(task: Task, sim_bridge_device: Device) -> None`

### `def test___task___add_ai_torque_bridge_two_point_lin_chan___sets_channel_attributes(task: Task, sim_bridge_device: Device) -> None`

### `def test___task___add_teds_ai_torque_bridge_chan___sets_channel_attributes(task: Task, sim_bridge_device: Device, torque_bridge_teds_file_path: pathlib.Path) -> None`

### `def test___task___add_ai_velocity_iepe_chan___sets_channel_attributes(task: Task, sim_dsa_device: Device) -> None`

### `def test___task___add_ai_voltage_chan_with_excit___sets_channel_attributes(task: Task, sim_6363_device: Device, min_val: float, max_val: float, bridge_config: BridgeConfiguration, voltage_excit_source: ExcitationSource, voltage_excit_val: float, use_excit_for_scaling: bool) -> None`

### `def test___task___add_teds_ai_voltage_chan_with_excit___sets_channel_attributes(task: Task, sim_bridge_device: Device, bridge_teds_file_path: pathlib.Path) -> None`

### `def test___task___add_ai_voltage_rms_chan___sets_channel_attributes(task: Task, sim_dmm_device: Device) -> None`

### `def test___task___add_teds_ai_voltage_chan_with_excit___raises_teds_sensor_not_detected(task: Task, sim_bridge_device: Device) -> None`

### `def test___task___add_ai_chans_with_name___sets_channel_name(task: Task, sim_6363_device: Device) -> None`

### `def test___task___add_ai_calculated_power_chan___sets_channel_attributes(task: Task, sim_4311_device: Device, voltage_min_val: float, voltage_max_val: float, current_min_val: float, current_max_val: float, units: PowerUnits, shunt_resistor_loc: CurrentShuntResistorLocation, expected_shunt_resistor_loc: CurrentShuntResistorLocation, custom_scale_name: str) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/task/channels/test_channel_properties.py -->
## PYTHON MODULE: tests/component/task/channels/test_channel_properties.py

### `def ai_voltage_chan_with_excit(task, sim_6363_device)`

Creates AI Channel object to measure voltage.

### `def ai_voltage_chan_with_scale(task, sim_6363_device)`

Creates AI Channel object to measure voltage with a custom scale.

### `def ai_power_chan(task, sim_ts_power_device)`

Creates AI Channel object to measure power.

### `def ai_rtd_chan(task, sim_6363_device)`

Creates AI Channel object that use an RTD to measure temperature.

### `def ci_pulse_width_chan(task, sim_6363_device)`

Creates CI Channel object to measure the width of a digital pulse.

### `def ci_count_edges_chan(task, sim_6363_device)`

Creates CI Channel object to count edges.

### `def test___channel___get_boolean_property___returns_default_value(ai_voltage_chan_with_excit: AIChannel)`

### `def test___channel___set_boolean_property___returns_assigned_value(ai_voltage_chan_with_excit: AIChannel)`

### `def test___channel___reset_boolean_property___returns_default_value(ai_voltage_chan_with_excit: AIChannel)`

### `def test___channel___get_enum_property___returns_default_value(ai_power_chan: AIChannel)`

### `def test___channel___set_enum_property___returns_assigned_value(ai_power_chan: AIChannel)`

### `def test___channel___reset_enum_property___returns_default_value(ai_power_chan: AIChannel)`

### `def test___channel___get_float_property___returns_default_value(ai_rtd_chan: AIChannel)`

### `def test___channel___set_float_property___returns_assigned_value(ai_rtd_chan: AIChannel)`

### `def test___channel___reset_float_property___returns_default_value(ai_rtd_chan: AIChannel)`

### `def test___channel___get_string_property___returns_default_value(ci_pulse_width_chan: CIChannel)`

### `def test___channel___set_string_property___returns_assigned_value(ci_pulse_width_chan: CIChannel)`

### `def test___channel___reset_string_property___returns_default_value(ci_pulse_width_chan: CIChannel)`

### `def test___channel___get_uint32_property___returns_default_value(ai_voltage_chan_with_excit: AIChannel)`

### `def test___channel___set_uint32_property___returns_assigned_value(ai_voltage_chan_with_excit: AIChannel)`

### `def test___channel___reset_uint32_property___returns_default_value(ai_voltage_chan_with_excit: AIChannel)`

### `def test___channel___get_deprecated_properties___reports_warnings(ai_rtd_chan: AIChannel)`

### `def test___channel___set_deprecated_properties___reports_warnings(ai_rtd_chan: AIChannel)`

### `def test___channel___reset_deprecated_properties___reports_warnings(ai_rtd_chan: AIChannel)`

### `def test___channel_with_scale___get_scale_property___returns_scale(ai_voltage_chan_with_scale: AIChannel)`

### `def test___channel_with_scale___get_scale_property___shared_interpreter(ai_voltage_chan_with_scale: AIChannel)`

### `def test___channel_with_scale___set_scale_property___returns_assigned_scale(ai_voltage_chan_with_scale: AIChannel, persisted_scale: PersistedScale)`

### `def test___channel_with_scale___reset_scale_property___returns_empty_scale(ai_voltage_chan_with_scale: AIChannel)`

### `def test___channel___get_physical_channel_property___returns_physical_channel(ai_rtd_chan: AIChannel, task: Task)`

### `def test___channel___get_physical_channel_property___shared_interpreter(ai_rtd_chan: AIChannel, task: Task)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/task/channels/test_ci_channel.py -->
## PYTHON MODULE: tests/component/task/channels/test_ci_channel.py

### `def test___task___add_ci_ang_encoder_chan___sets_channel_attributes(task: Task, sim_6363_device: Device, decoding_type: EncoderType, zidx_enable: bool, zidx_val: float, zidx_phase: EncoderZIndexPhase, units: AngleUnits, pulses_per_rev: int, initial_angle: float, custom_scale_name: str) -> None`

### `def test___task___add_ci_ang_velocity_chan___sets_channel_attributes(task: Task, sim_velocity_device: Device, decoding_type: EncoderType, pulses_per_rev: int) -> None`

### `def test___task___add_ci_count_edges_chan___sets_channel_attributes(task: Task, sim_6363_device: Device, edge: Edge, initial_count: int, count_direction: CountDirection) -> None`

### `def test___task___add_ci_duty_cycle_chan___sets_channel_attributes(task: Task, sim_velocity_device: Device, edge: Edge) -> None`

### `def test___task___add_ci_freq_chan___sets_channel_attributes(task: Task, sim_6363_device: Device, edge: Edge, meas_method: CounterFrequencyMethod, meas_time: float, divisor: int) -> None`

### `def test___task___add_ci_lin_encoder_chan___sets_channel_attributes(task: Task, sim_6363_device: Device, decoding_type: EncoderType, dist_per_pulse: float, initial_pos: float) -> None`

### `def test___task___add_ci_lin_velocity_chan___sets_channel_attributes(task: Task, sim_velocity_device: Device, decoding_type: EncoderType, dist_per_pulse: float) -> None`

### `def test___task___add_ci_period_chan___sets_channel_attributes(task: Task, sim_6363_device: Device, edge: Edge, meas_method: CounterFrequencyMethod, meas_time: float, divisor: int) -> None`

### `def test___task___add_ci_pulse_chan_ticks___sets_channel_attributes(task: Task, sim_6363_device: Device, source_terminal: str) -> None`

### `def test___task___add_ci_pulse_chan_time___sets_channel_attributes(task: Task, sim_6363_device: Device) -> None`

### `def test___task___add_ci_pulse_chan_freq___sets_channel_attributes(task: Task, sim_6363_device: Device) -> None`

### `def test___task___add_ci_pulse_width_chan___sets_channel_attributes(task: Task, sim_6363_device: Device, starting_edge: Edge) -> None`

### `def test___task___add_ci_semi_period_chan___sets_channel_attributes(task: Task, sim_6363_device: Device) -> None`

### `def test___task___add_ci_two_edge_sep_chan___sets_channel_attributes(task: Task, sim_6363_device: Device, first_edge: Edge, second_edge: Edge) -> None`

### `def test___task___add_ci_chans_with_name___sets_channel_name(task: Task, sim_6363_device: Device) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/task/channels/test_co_channel.py -->
## PYTHON MODULE: tests/component/task/channels/test_co_channel.py

### `def test___task___add_co_pulse_chan_freq___sets_channel_attributes(task: Task, sim_6363_device: Device, idle_state: Level, initial_delay: float, freq: float, duty_cycle: float) -> None`

### `def test___task___add_co_pulse_chan_ticks___sets_channel_attributes(task: Task, sim_6363_device: Device, source_terminal: str, idle_state: Level, initial_delay: float, low_ticks: int, high_ticks: int) -> None`

### `def test___task___add_co_pulse_chan_time___sets_channel_attributes(task: Task, sim_6363_device: Device, idle_state: Level, initial_delay: float, low_time: float, high_time: float) -> None`

### `def test___task___add_co_chans_with_name___sets_channel_name(task: Task, sim_6363_device: Device) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/task/channels/test_di_channel.py -->
## PYTHON MODULE: tests/component/task/channels/test_di_channel.py

### `def test___task___add_di_chan_chan_for_all_lines___sets_channel_attributes(task: Task, sim_6363_device: Device, num_lines: int) -> None`

### `def test___task___add_di_chan_chan_per_line___sets_channel_attributes(task: Task, sim_6363_device: Device, num_lines: int) -> None`

### `def _test___task___add_di_chans_with_name___sets_channel_name(task: Task, sim_6363_device: Device, phys_chan_list: list[str], line_grouping: LineGrouping, name_to_assign_to_lines: str, expected_virtual_channel_name: str, qualify_expected_virtual_channel_name: bool) -> None`

### `def test___task___add_di_chans_with_simple_name___sets_channel_name(task: Task, sim_6363_device: Device, phys_chan_list: list[str], line_grouping: LineGrouping, name_to_assign_to_lines: str, expected_virtual_channel_name: str, qualify_expected_virtual_channel_name: bool) -> None`

### `def test___task___add_di_chans_with_complex_name___sets_channel_name(task: Task, sim_6363_device: Device, phys_chan_list: list[str], line_grouping: LineGrouping, name_to_assign_to_lines: str, expected_virtual_channel_name: str, qualify_expected_virtual_channel_name: bool) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/task/channels/test_do_channel.py -->
## PYTHON MODULE: tests/component/task/channels/test_do_channel.py

### `def test___task___add_do_chan_chan_for_all_lines___sets_channel_attributes(task: Task, sim_6363_device: Device, num_lines: int) -> None`

### `def test___task___add_do_chan_chan_per_line___sets_channel_attributes(task: Task, sim_6363_device: Device, num_lines: int) -> None`

### `def test___task___add_do_chans_with_name___sets_channel_name(task: Task, sim_6363_device: Device) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/task/test_export_signals_properties.py -->
## PYTHON MODULE: tests/component/task/test_export_signals_properties.py

### `def ai_voltage_task(task, sim_6363_device)`

Gets AI voltage task.

### `def ao_voltage_task(task, sim_6363_device)`

Gets AO voltage task.

### `def test___ai_task___get_enum_property___returns_default_value(ai_voltage_task: Task)`

### `def test___ai_task___set_enum_property___returns_assigned_value(ai_voltage_task: Task)`

### `def test___ai_task___reset_enum_property___returns_default_value(ai_voltage_task: Task)`

### `def test___ai_task___get_string_property___returns_default_value(ai_voltage_task: Task)`

### `def test___ai_task___set_invalid_routing_destination___throws_daqerror(ai_voltage_task: Task)`

### `def test___ai_task___set_string_property___returns_assigned_value(ao_voltage_task: Task)`

### `def test___ai_task___reset_string_property___returns_default_value(ao_voltage_task: Task)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/task/test_in_stream.py -->
## PYTHON MODULE: tests/component/task/test_in_stream.py

- `SINE_VOLTAGE_MAX = 2.5`

- `SINE_VOLTAGE_MIN = -2.5`

- `SINE_RAW_MAX = 16383`

- `SINE_RAW_MIN = -16384`

- `FULL_SCALE_RAW_MAX = 32767`

- `FULL_SCALE_RAW_MIN = -32768`

### `def ai_task(task, sim_6363_device)`

### `def ai_sine_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device, request: pytest.FixtureRequest) -> nidaqmx.Task`

Returns an analog input task with varying number of channels and a simulated sine wave.

### `def _create_ai_sine_channels(task: nidaqmx.Task, device: nidaqmx.system.Device, number_of_channels: int) -> None`

Creates the specified number of analog input channels for a simulated sine wave.

### `def test___ai_task___read___returns_valid_samples_shape_and_dtype(ai_sine_task: nidaqmx.Task, samples_to_read: int) -> None`

### `def test___ai_finite_task___readall___returns_valid_samples_shape_and_dtype(ai_sine_task: nidaqmx.Task) -> None`

### `def test___ai_continuous_task___readall___returns_valid_samples_shape_and_dtype(ai_sine_task: nidaqmx.Task) -> None`

### `def test___valid_array___readinto___returns_valid_samples(ai_sine_task: nidaqmx.Task, samples_to_read: int) -> None`

### `def test___odd_sized_array___readinto___returns_whole_samples_and_clears_padding(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___ai_finite_task___read_all___returns_valid_samples_shape_and_dtype(ai_sine_task: nidaqmx.Task) -> None`

### `def test___ai_continuous_task___read_all___returns_valid_samples_shape_and_dtype(ai_sine_task: nidaqmx.Task) -> None`

### `def test___valid_array___read_into___returns_valid_samples(ai_sine_task: nidaqmx.Task, samples_to_read: int) -> None`

### `def test___odd_sized_array___read_into___returns_whole_samples_and_clears_padding(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___valid_path___configure_logging___returns_assigned_values(ai_task: nidaqmx.Task)`

### `def test___valid_path___start_new_file___returns_assigned_value(ai_task: nidaqmx.Task)`

### `def test___in_stream___set_nonexistent_property___raises_exception(task: nidaqmx.Task)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/task/test_in_stream_buffer_properties.py -->
## PYTHON MODULE: tests/component/task/test_in_stream_buffer_properties.py

### `def test___ai_task___set_int32_property___value_is_set(task, sim_6363_device)`

### `def test___ai_task___reset_int32_property___value_is_set_to_default(task, sim_6363_device)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/task/test_in_stream_read_properties.py -->
## PYTHON MODULE: tests/component/task/test_in_stream_read_properties.py

### `def ai_task(task, sim_6363_device)`

Gets AI voltage task.

### `def test___ai_task___get_int32_property___returns_default_value(ai_task: Task)`

### `def test___ai_task___set_int32_property___returns_assigned_value(ai_task: Task)`

### `def test___ai_task___reset_int32_property___returns_default_value(ai_task: Task)`

### `def test___ai_task___get_enum_property___returns_default_value(ai_task: Task)`

### `def test___ai_task___set_enum_property___returns_assigned_value(ai_task: Task)`

### `def test___ai_task___reset_enum_property___returns_default_value(ai_task: Task)`

### `def test___ai_task___get_float_property___returns_default_value(ai_task: Task)`

### `def test___ai_task___set_float_property___returns_assigned_value(ai_task: Task)`

### `def test___ai_task___reset_float_property___returns_default_value(ai_task: Task)`

### `def test___ai_task___get_uint32_property___returns_default_value(ai_task: Task)`

### `def test___ai_task___set_uint32_property___returns_assigned_value(ai_task: Task)`

### `def test___ai_task___reset_uint32_property___returns_default_value(ai_task: Task)`

### `def test___ai_task___get_uint64_property___returns_default_value(ai_task: Task)`

### `def test___ai_task___set_uint64_property___returns_assigned_value(ai_task: Task)`

### `def test___ai_task___reset_uint64_property___returns_default_value(ai_task: Task)`

### `def test___ai_task___get_bool_property___returns_default_value(ai_task: Task)`

### `def test___ai_task___set_bool_property___returns_assigned_value(ai_task: Task)`

### `def test___ai_task___reset_bool_property___returns_default_value(ai_task: Task)`

### `def test___ai_task___get_string_property___returns_default_value(ai_task: Task)`

### `def test___ai_task___set_string_property___returns_assigned_value(ai_task: Task)`

### `def test___ai_task___set_string_property_none___returns_default_value(ai_task: Task)`

### `def test___ai_task___reset_string_property___returns_default_value(ai_task: Task)`

### `def test___ai_task___get_deprecated_properties___reports_warnings(ai_task: Task)`

### `def test___ai_task___set_deprecated_properties___reports_warnings(ai_task: Task)`

### `def test___ai_task___reset_deprecated_properties___reports_warnings(ai_task: Task)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/task/test_out_stream.py -->
## PYTHON MODULE: tests/component/task/test_out_stream.py

### `def ao_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device, request: pytest.FixtureRequest) -> nidaqmx.Task`

Returns an analog output task with a varying number of channels.

### `def _create_ao_channels(task: nidaqmx.Task, device: nidaqmx.system.Device, number_of_channels: int) -> None`

Creates the specified number of analog output channels.

### `def test___valid_array___write___returns_samples_written(ao_task: nidaqmx.Task, samples_to_write: int) -> None`

### `def test___odd_sized_array___write___returns_whole_samples(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___out_stream___set_nonexistent_property___raises_exception(task: nidaqmx.Task)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/task/test_out_stream_buffer_properties.py -->
## PYTHON MODULE: tests/component/task/test_out_stream_buffer_properties.py

### `def test___ai_task___set_valid_value_to_unsupported_property___unsupported_error_raised(task, sim_6363_device)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/task/test_out_stream_write_properties.py -->
## PYTHON MODULE: tests/component/task/test_out_stream_write_properties.py

### `def ao_task(task, sim_6363_device)`

Gets AO voltage task.

### `def test___ao_task___get_int32_property___returns_default_value(ao_task: Task)`

### `def test___ao_task___set_int32_property___returns_assigned_value(ao_task: Task)`

### `def test___ao_task___reset_int32_property___returns_default_value(ao_task: Task)`

### `def test___ao_task___get_enum_property___returns_default_value(ao_task: Task)`

### `def test___ao_task___set_enum_property___returns_assigned_value(ao_task: Task)`

### `def test___ao_task___reset_enum_property___returns_default_value(ao_task: Task)`

### `def test___ao_task___get_float_property___returns_default_value(ao_task: Task)`

### `def test___ao_task___set_float_property___returns_assigned_value(ao_task: Task)`

### `def test___ao_task___reset_float_property___returns_default_value(ao_task: Task)`

### `def test___ao_task___get_uint32_property___returns_default_value(ao_task: Task)`

### `def test___ao_task___get_uint64_property___returns_default_value(ao_task: Task)`

### `def test___ao_current_task___get_bool_property___returns_default_value(task, device)`

### `def test___ao_current_task___get_string_list_property___returns_default_value(task, device)`

### `def test___ao_current_task__read_property___out_of_order___throws_daqerror(task, device)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/task/test_task_read_ai.py -->
## PYTHON MODULE: tests/component/task/test_task_read_ai.py

### `def test___analog_single_channel___read_unset_samples___returns_valid_scalar(ai_single_channel_task: nidaqmx.Task) -> None`

### `def test___analog_single_channel___read_one_sample___returns_valid_1d_samples(ai_single_channel_task: nidaqmx.Task) -> None`

### `def test___analog_single_channel___read_many_sample___returns_valid_1d_samples(ai_single_channel_task: nidaqmx.Task) -> None`

### `def test___analog_single_channel_finite___read_too_many_sample___returns_valid_1d_samples_truncated(ai_single_channel_task: nidaqmx.Task) -> None`

### `def test___analog_multi_channel___read_unset_samples___returns_1d_channels(ai_multi_channel_task: nidaqmx.Task) -> None`

### `def test___analog_multi_channel___read_one_sample___returns_valid_2d_channels_samples(ai_multi_channel_task: nidaqmx.Task) -> None`

### `def test___analog_multi_channel___read_many_sample___returns_valid_2d_channels_samples(ai_multi_channel_task: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_finite___read_too_many_sample___returns_valid_2d_channels_samples_truncated(ai_multi_channel_task: nidaqmx.Task) -> None`

### `def test___power_single_channel___read_unset_samples___returns_valid_scalar(pwr_single_channel_task: nidaqmx.Task) -> None`

### `def test___power_single_channel___read_one_sample___returns_valid_1d_samples(pwr_single_channel_task: nidaqmx.Task) -> None`

### `def test___power_single_channel___read_many_sample___returns_valid_1d_samples(pwr_single_channel_task: nidaqmx.Task) -> None`

### `def test___power_single_channel_finite___read_too_many_sample___returns_valid_1d_samples_truncated(pwr_single_channel_task: nidaqmx.Task) -> None`

### `def test___power_multi_channel___read_unset_samples___returns_valid_1d_channels(pwr_multi_channel_task: nidaqmx.Task) -> None`

### `def test___power_multi_channel___read_one_sample___returns_valid_2d_channels_samples(pwr_multi_channel_task: nidaqmx.Task) -> None`

### `def test___power_multi_channel___read_many_sample___returns_valid_2d_channels_samples(pwr_multi_channel_task: nidaqmx.Task) -> None`

### `def test___power_multi_channel_finite___read_too_many_sample___returns_valid_2d_channels_samples_truncated(pwr_multi_channel_task: nidaqmx.Task) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/task/test_task_read_waveform_ai.py -->
## PYTHON MODULE: tests/component/task/test_task_read_waveform_ai.py

### `def test___analog_single_channel___read_waveform___returns_valid_waveform(ai_single_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_single_channel___read_waveform_one_sample___returns_waveform_with_one_sample(ai_single_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_single_channel___read_waveform_many_sample___returns_waveform_with_many_samples(ai_single_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_single_channel_finite___read_waveform_too_many_samples___returns_waveform_with_correct_number_of_samples(ai_single_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_multi_channel___read_waveform___returns_valid_waveforms(ai_multi_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_multi_channel___read_waveform_one_sample___returns_waveforms_with_single_sample(ai_multi_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_multi_channel___read_waveform_many_samples___returns_waveforms_with_many_samples(ai_multi_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_multi_channel_finite___read_waveform_too_many_samples___returns_waveforms_with_correct_number_of_samples(ai_multi_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_single_channel___read_waveform_read_all_available___returns_valid_waveform(ai_single_channel_task_with_timing: nidaqmx.Task) -> None`

### `def test___analog_multi_channel___read_waveform_read_all_available___returns_valid_waveforms(ai_multi_channel_task_with_timing: nidaqmx.Task) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/task/test_task_read_waveform_di.py -->
## PYTHON MODULE: tests/component/task/test_task_read_waveform_di.py

### `def test___digital_single_channel___read_waveform___returns_valid_waveform(di_single_channel_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_single_channel___read_waveform_one_sample___returns_waveform_with_one_sample(di_single_channel_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_single_channel___read_waveform_many_sample___returns_waveform_with_many_samples(di_single_channel_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_single_channel___read_waveform_too_many_samples___returns_waveform_with_correct_number_of_samples(di_single_channel_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_single_channel___read_waveform_lines_and_port___returns_valid_waveform(di_single_chan_lines_and_port_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_multi_channel___read_waveform___returns_valid_waveforms(di_multi_channel_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_multi_channel___read_waveform_one_sample___returns_waveforms_with_single_sample(di_multi_channel_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_multi_channel___read_waveform_many_samples___returns_waveforms_with_many_samples(di_multi_channel_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_multi_channel___read_waveform_too_many_samples___returns_waveforms_with_correct_number_of_samples(di_multi_channel_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_multi_channel___read_waveform_different_lines___returns_valid_waveforms(di_multi_chan_diff_lines_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_multi_channel___read_waveform_lines_and_port___returns_valid_waveforms(di_multi_chan_lines_and_port_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_single_channel___read_waveform_read_all_available___returns_valid_waveform(di_single_channel_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

### `def test___digital_multi_channel___read_waveform_read_all_available___returns_valid_waveforms(di_multi_channel_timing_task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/task/test_task_write_waveform_ao.py -->
## PYTHON MODULE: tests/component/task/test_task_write_waveform_ao.py

### `def test___task___write_waveform_feature_disabled___raises_feature_not_supported_error(ao_single_channel_task: nidaqmx.Task) -> None`

### `def test___task___write_linear_ramp_waveform___output_matches_final_value(ao_single_channel_task: nidaqmx.Task, ai_single_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveform_as_list___output_matches_final_value(ao_single_channel_task: nidaqmx.Task, ai_single_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveform_with_write___output_matches_final_value(ao_single_channel_task: nidaqmx.Task, ai_single_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveform_with_auto_start___output_matches_final_value(ao_single_channel_task_with_timing: nidaqmx.Task, ai_single_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___task_with_multiple_channels___write_single_channel_waveform___raises_daq_error(ao_multi_channel_task: nidaqmx.Task) -> None`

### `def test___task___write_waveform_with_float32_dtype___output_matches_final_value(ao_single_channel_task: nidaqmx.Task, ai_single_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveform_with_scaling___output_matches_final_value(ao_single_channel_task: nidaqmx.Task, ai_single_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveform_with_non_contiguous_data___output_matches_final_value(ao_single_channel_task: nidaqmx.Task, ai_single_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveform_with_timing___all_samples_match_waveform_data(generate_task, real_x_series_multiplexed_device: nidaqmx.system.Device) -> None`

### `def test___task___write_waveforms_feature_disabled___raises_feature_not_supported_error(ao_multi_channel_task: nidaqmx.Task) -> None`

### `def test___task___write_waveforms___output_matches_final_values(ao_multi_channel_task: nidaqmx.Task, ai_multi_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveforms_with_write___output_matches_final_values(ao_multi_channel_task: nidaqmx.Task, ai_multi_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveforms_with_different_formulas___output_matches_final_values(ao_multi_channel_task: nidaqmx.Task, ai_multi_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___task_with_single_channel___write_multiple_waveforms___raises_daq_error(ao_single_channel_task: nidaqmx.Task) -> None`

### `def test___task___write_waveform_and_array___raises_value_error(ao_multi_channel_task: nidaqmx.Task) -> None`

### `def test___task___write_waveforms_with_different_lengths___raises_error(ao_multi_channel_task: nidaqmx.Task) -> None`

### `def test___task___write_waveforms_with_auto_start___output_matches_final_values(ao_multi_channel_task_with_timing: nidaqmx.Task, ai_multi_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveforms_with_float32_dtype___output_matches_final_values(ao_multi_channel_task: nidaqmx.Task, ai_multi_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveforms_with_scaling___output_matches_final_values(ao_multi_channel_task: nidaqmx.Task, ai_multi_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveforms_with_non_contiguous_data___output_matches_final_values(ao_multi_channel_task: nidaqmx.Task, ai_multi_channel_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveforms_with_timing___all_samples_match_waveform_data(generate_task, real_x_series_multiplexed_device: nidaqmx.system.Device) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/task/test_task_write_waveform_do.py -->
## PYTHON MODULE: tests/component/task/test_task_write_waveform_do.py

### `def test___task___write_waveform_feature_disabled___raises_feature_not_supported_error(do_single_line_task: nidaqmx.Task) -> None`

### `def test___task___write_waveform_single_line___outputs_match_final_values(do_single_line_task: nidaqmx.Task, di_single_line_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveform_single_line_with_write___outputs_match_final_values(do_single_line_task: nidaqmx.Task, di_single_line_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveform_single_line_with_auto_start___output_matches_final_value(do_single_line_task_with_timing: nidaqmx.Task, di_single_line_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveform_single_line_with_non_contiguous_data___outputs_match_final_values(do_single_line_task: nidaqmx.Task, di_single_line_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveform_single_line_all_dtypes___outputs_match_final_values(do_single_line_task: nidaqmx.Task, di_single_line_loopback_task: nidaqmx.Task, dtype) -> None`

### `def test___task___write_waveform_single_line_signal_count_mismatch___raises_daq_error(do_single_line_task: nidaqmx.Task) -> None`

### `def test___task___write_waveform_multi_line___outputs_match_final_values(do_single_channel_multi_line_task: nidaqmx.Task, di_multi_line_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveform_multi_line_with_write___outputs_match_final_values(do_single_channel_multi_line_task: nidaqmx.Task, di_multi_line_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveform_multi_line_with_auto_start___output_matches_final_value(do_single_channel_multi_line_task_with_timing: nidaqmx.Task, di_multi_line_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveform_multi_line_with_non_contiguous_data___outputs_match_final_values(do_single_channel_multi_line_task: nidaqmx.Task, di_multi_line_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveform_multi_line_all_dtypes___outputs_match_final_values(do_single_channel_multi_line_task: nidaqmx.Task, di_multi_line_loopback_task: nidaqmx.Task, dtype) -> None`

### `def test___task___write_waveform_multi_line_signal_count_mismatch___raises_daq_error(do_single_channel_multi_line_task: nidaqmx.Task) -> None`

### `def test___task___write_waveform_port_uint8___outputs_match_final_values(do_port1_task: nidaqmx.Task, di_port1_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveform_port_uint32___outputs_match_final_values(do_port0_task: nidaqmx.Task, di_port0_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveforms_feature_disabled___raises_feature_not_supported_error(do_multi_channel_multi_line_task: nidaqmx.Task) -> None`

### `def test___task___write_waveforms_single_lines___outputs_match_final_values(do_multi_channel_multi_line_task: nidaqmx.Task, di_multi_line_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveforms_with_write___outputs_match_final_values(do_multi_channel_multi_line_task: nidaqmx.Task, di_multi_line_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveforms_with_auto_start___output_matches_final_value(do_multi_channel_multi_line_task_with_timing: nidaqmx.Task, di_multi_line_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveforms_mixed_lines___outputs_match_final_values(do_multi_channel_mixed_line_task: nidaqmx.Task, di_multi_line_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveforms_ports___outputs_match_final_values(do_multi_channel_port_task: nidaqmx.Task, di_multi_channel_port_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveforms_port_and_lines___outputs_match_final_values(do_multi_channel_port_and_lines_task: nidaqmx.Task, di_multi_channel_port_and_lines_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveforms_with_non_contiguous_data___outputs_match_final_values(do_multi_channel_multi_line_task: nidaqmx.Task, di_multi_line_loopback_task: nidaqmx.Task) -> None`

### `def test___task___write_waveforms_with_different_sample_counts___raises_error(do_multi_channel_port_task: nidaqmx.Task) -> None`

### `def test___task___write_waveforms_with_too_many___raises_daq_error(do_multi_channel_port_task: nidaqmx.Task) -> None`

### `def test___task___write_waveforms_with_too_many_signals___raises_daq_error(do_multi_channel_port_task: nidaqmx.Task) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/task/test_timing.py -->
## PYTHON MODULE: tests/component/task/test_timing.py

### `def sim_6535_di_single_line_task(task: Task, sim_6535_device: Device) -> Task`

Gets DI task.

### `def test___timing___cfg_handshaking___sets_properties(sim_6535_di_single_line_task: Task) -> None`

### `def test___timing___cfg_change_detection___sets_properties(sim_6535_di_single_line_task: Task) -> None`

### `def test___timing___cfg_pipelined_samp_clk___sets_properties(sim_6535_di_single_line_task: Task, clk_source: str, active_edge: int) -> None`

### `def test___timing___cfg_burst_handshaking_import_clock___sets_properties(sim_6535_di_single_line_task: Task, clk_source: str, active_edge: int, pause_when: int, ready_event_active_level: int) -> None`

### `def test___timing___cfg_burst_handshaking_export_clock___sets_properties(sim_6535_di_single_line_task: Task, clk_outp_term: str, clk_pulse_polarity: int, pause_when: int, ready_event_active_level: int) -> None`

### `def test___timing___set_nonexistent_property___raises_exception(task: Task)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/task/test_timing_properties.py -->
## PYTHON MODULE: tests/component/task/test_timing_properties.py

### `def test___timing___get_boolean_property___returns_value(task, sim_6363_device)`

### `def test___timing___get_boolean_property_with_device_context___throw_daqerror(task, sim_6363_device)`

### `def test___timing___set_boolean_property___returns_assigned_value(task, sim_6363_device)`

### `def test___timing___set_boolean_property_with_device_context___throw_daqerror(task, sim_6363_device)`

### `def test___timing___reset_boolean_property___returns_default_value(task, sim_6363_device)`

### `def test___timing___reset_boolean_property_with_device_context___throw_daqerror(task, sim_6363_device)`

### `def test___timing___get_string_property___returns_value(task, sim_6363_device)`

### `def test___timing___get_string_property_with_device_context___throw_daqerror(task, sim_6363_device)`

### `def test___timing___set_string_property___returns_assigned_value(task, sim_6363_device)`

### `def test___timing___set_string_property_with_device_context___throw_daqerror(task, sim_6363_device)`

### `def test___timing___reset_string_property___returns_default_value(task, sim_6363_device)`

### `def test___timing___reset_string_property_with_device_context___throw_daqerror(task, sim_6363_device)`

### `def test___timing___set_invalid_source_terminal_name___throws_daqerror(task, sim_6363_device)`

### `def test___timing___get_enum_property___returns_value(task, sim_6363_device)`

### `def test___timing___get_enum_property_with_device_context___returns_value(task, sim_9205_device)`

### `def test___timing___get_enum_property_with_device_context___throws_daqerror(task, sim_6363_device)`

### `def test___timing___set_enum_property___returns_assigned_value(task, sim_6363_device)`

### `def test___timing___set_enum_property_with_device_context___returns_assigned_value(task, sim_9205_device)`

### `def test___timing___set_enum_property_with_device_context___throw_daqerror(task, sim_6363_device)`

### `def test___timing___reset_enum_property___returns_default_value(task, sim_6363_device)`

### `def test___timing___reset_enum_property_with_device_context___returns_default_value(task, sim_9205_device)`

### `def test___timing___reset_enum_property_with_device_context___throws_daqerror(task, sim_6363_device)`

### `def test___timing___get_float64_property___returns_value(task, sim_6363_device)`

### `def test___timing___get_float64_property_with_device_context___returns_value(task, sim_9205_device)`

### `def test___timing___get_float64_property_with_device_context___throws_daqerror(task, sim_6363_device)`

### `def test___timing___set_float64_property___returns_assigned_value(task, sim_6363_device)`

### `def test___timing___set_float64_property_with_device_context___returns_assigned_value(task, sim_9205_device)`

### `def test___timing___set_float64_property_with_device_context___throws_daqerror(task, sim_6363_device)`

### `def test___timing___reset_float64_property___returns_default_value(task, sim_6363_device)`

### `def test___timing___reset_float64_property_with_device_context___returns_default_value(task, sim_9205_device)`

### `def test___timing___reset_float64_property_with_device_context___throws_daqerror(task, sim_6363_device)`

### `def test___timing___get_uint32_property___returns_value(task, sim_6363_device)`

### `def test___timing___get_uint32_property_with_device_context___returns_value(task, sim_9205_device)`

### `def test___timing___get_uint32_property_with_device_context___throws_daqerror(task, sim_6363_device)`

### `def test___timing___set_uint32_property___returns_assigned_value(task, sim_6363_device)`

### `def test___timing___set_uint32_property_with_device_context___returns_assigned_value(task, sim_9205_device)`

### `def test___timing___set_uint32_property_with_device_context___throws_daqerror(task, sim_6363_device)`

### `def test___timing___reset_uint32_property___returns_default_value(task, sim_6363_device)`

### `def test___timing___reset_uint32_property_with_device_context___returns_default_value(task, sim_9205_device)`

### `def test___timing___reset_uint32_property_with_device_context___throws_daqerror(task, sim_6363_device)`

### `def test___timing___get_uint64_property___returns_value(task, sim_6363_device)`

### `def test___timing___get_uint64_property_with_device_context___throws_daqerror(task, sim_6363_device)`

### `def test___timing___set_uint64_property___returns_assigned_value(task, sim_6363_device)`

### `def test___timing___set_uint64_property_with_device_context___throws_daqerror(task, sim_6363_device)`

### `def test___timing___reset_uint64_property___returns_default_value(task, sim_6363_device)`

### `def test___timing___reset_uint64_property_with_device_context___throws_daqerror(task, sim_6363_device)`

### `def test___timing___set_uint64_property_out_of_range_value___throws_daqerror(task, sim_6363_device)`

### `def test___timing___get_timestamp_property___returns_value(task, sim_9205_device)`

### `def test___timing___get_timestamp_property_with_device_context___throws_daqerror(task, sim_9205_device)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/task/test_triggers.py -->
## PYTHON MODULE: tests/component/task/test_triggers.py

### `def ai_voltage_task(task, sim_time_aware_9215_device) -> Task`

Gets AI voltage task.

### `def ci_count_edges_task(task, sim_9189_device) -> Task`

### `def sim_6363_ai_voltage_task(task, sim_6363_device) -> Task`

Gets AI voltage task.

### `def sim_6535_di_single_line_task(task, sim_6535_device) -> Task`

Gets DI task.

### `def sim_9775_ai_voltage_multi_edge_task(task, sim_9775_device) -> Task`

Gets AI voltage multi edge task.

### `def test___default_arguments___cfg_time_start_trig___no_errors(ai_voltage_task: Task)`

### `def test___arguments_provided___cfg_time_start_trig___no_errors(ai_voltage_task: Task, timescale: Timescale)`

### `def test___start_trigger___wait_for_valid_timestamp___no_errors(ai_voltage_task: Task)`

### `def test___reference_trigger___wait_for_valid_timestamp___no_errors(ai_voltage_task: Task)`

### `def test___arm_start_trigger___wait_for_valid_timestamp___no_errors(ci_count_edges_task: Task)`

### `def test___first_sample_trigger___wait_for_valid_timestamp___no_errors(ai_voltage_task: Task)`

### `def test___timestamp_not_enabled___wait_for_valid_timestamp___throw_error(ai_voltage_task: Task)`

### `def test___start_trigger___cfg_anlg_edge_start_trig___no_errors(sim_6363_ai_voltage_task: Task, trig_src: str, trig_slope: Slope, trig_level: float)`

### `def test___start_trigger___cfg_anlg_window_start_trig___no_errors(sim_6363_ai_voltage_task: Task, window_top: float, window_bottom: float, trig_src: str, trig_when: int)`

### `def test___start_trigger___disable___no_errors(sim_6363_ai_voltage_task: Task)`

### `def test___reference_trigger___disable___no_errors(sim_6363_ai_voltage_task: Task)`

### `def test___reference_trigger___cfg_anlg_window_ref_trig___no_errors(sim_6363_ai_voltage_task: Task, window_top: float, window_bottom: float, pretrigger_samples: int, trig_src: str, trig_when: int)`

### `def test___start_trigger___cfg_anlg_multi_edge_start_trig___no_errors(sim_9775_ai_voltage_multi_edge_task: Task, trig_slopes: list[Slope], trig_levels: list[float])`

### `def test___start_trigger__cfg_dig_pattern_start_trig___no_errors(sim_6535_di_single_line_task: Task, trig_src: str, trig_pattern: str, trig_when: int)`

### `def test___reference_trigger___cfg_anlg_edge_ref_trig___no_errors(sim_6363_ai_voltage_task: Task, trig_src: str, pretrig_samples: int, trig_slope: Slope, trig_level: float)`

### `def test___reference_trigger___cfg_anlg_multi_edge_ref_trig___no_errors(sim_9775_ai_voltage_multi_edge_task: Task, pretrig_samples: int, trig_slopes: list[Slope], trig_levels: list[float])`

### `def test___reference_trigger___cfg_dig_edge_ref_trig___no_errors(sim_6363_ai_voltage_task: Task, trig_src: str, pretrig_samples: int, trig_edge: Edge)`

### `def test___reference_trigger__cfg_dig_pattern_ref_trig___no_errors(sim_6535_di_single_line_task: Task, trig_src: str, trig_pattern: str, pretrig_samples: int, trig_when: int)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/task/test_triggers_properties.py -->
## PYTHON MODULE: tests/component/task/test_triggers_properties.py

### `def ai_voltage_task(task, sim_6363_device)`

Gets AI voltage task.

### `def ai_voltage_time_aware_task(task, sim_time_aware_9215_device)`

Gets AI voltage task.

### `def test___ai_task___get_float_property___returns_default_value(ai_voltage_task: Task)`

### `def test___ai_task___set_float_property___returns_assigned_value(ai_voltage_task: Task)`

### `def test___ai_task___reset_float_property___returns_default_value(ai_voltage_task: Task)`

### `def test___ai_task___get_string_property___returns_default_value(ai_voltage_task: Task)`

### `def test___ai_task___set_string_property___returns_assigned_value(ai_voltage_task: Task)`

### `def test___ai_task___reset_string_property___returns_default_value(ai_voltage_task: Task)`

### `def test___ai_task___get_enum_property___returns_default_value(ai_voltage_task: Task)`

### `def test___ai_task_without_cfg_samp_clk___set_trig_type___throws_daqerror(ai_voltage_task: Task)`

### `def test___ai_task___set_enum_property___returns_assigned_value(ai_voltage_task: Task)`

### `def test___ai_task___reset_enum_property___returns_default_value(ai_voltage_task: Task)`

### `def test___ai_task___get_uint32_property___returns_default_value(ai_voltage_task: Task)`

### `def test___ai_task___set_uint32_property___returns_assigned_value(ai_voltage_task: Task)`

### `def test___ai_task___reset_uint32_property___returns_default_value(ai_voltage_task: Task)`

### `def test___ai_voltage_time_aware_task___get_timestamp_property___returns_default_value(ai_voltage_time_aware_task: Task)`

### `def test___ai_voltage_time_aware_task___set_timestamp_property___returns_assigned_value(ai_voltage_time_aware_task: Task)`

### `def test___ai_voltage_time_aware_task___reset_timestamp_property___returns_default_value(ai_voltage_time_aware_task: Task)`

### `def test___trigger___set_nonexistent_property___raises_exception(task: Task)`

### `def test___arm_start_trigger___set_nonexistent_property___raises_exception(task: Task)`

### `def test___handshake_trigger___set_nonexistent_property___raises_exception(task: Task)`

### `def test___pause_trigger___set_nonexistent_property___raises_exception(task: Task)`

### `def test___reference_trigger___set_nonexistent_property___raises_exception(task: Task)`

### `def test___start_trigger___set_nonexistent_property___raises_exception(task: Task)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/test_export_signals.py -->
## PYTHON MODULE: tests/component/test_export_signals.py

### `def test___export_signals___set_nonexistent_property___raises_exception(task: nidaqmx.Task)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/test_interpreter.py -->
## PYTHON MODULE: tests/component/test_interpreter.py

### `def test___known_error_code___get_error_string___returns_known_error_message(interpreter: BaseInterpreter) -> None`

### `def test___unknown_error_code___get_error_string___returns_unable_to_locate_error_resources(interpreter: BaseInterpreter) -> None`

### `def test___grpc_channel_with_errors___get_error_string___returns_failed_to_retrieve_error_description(interpreter: BaseInterpreter) -> None`

### `def test___error_code_with_hardcoded_error_message___get_error_string___returns_hardcoded_error_message(interpreter: BaseInterpreter, error_code: DAQmxErrors) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/test_scale.py -->
## PYTHON MODULE: tests/component/test_scale.py

### `def test___polynomial___calculate_reverse_poly_coeff___returns_reverse_coeff(init_kwargs)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/test_scale_properties.py -->
## PYTHON MODULE: tests/component/test_scale_properties.py

### `def test___scale___get_float64_property___returns_assigned_value(init_kwargs)`

### `def test___scale___set_float64_property___returns_assigned_value(init_kwargs)`

### `def test___scale___get_float64_list_property___returns_assigned_value(init_kwargs)`

### `def test___scale___set_float64_list_property___returns_assigned_value(init_kwargs)`

### `def test___linear_scale___get_poly_scale_property___throws_daqerror(init_kwargs)`

### `def test___scale___get_enum_property___returns_assigned_value(init_kwargs)`

### `def test___scale___set_enum_property___returns_assigned_value(init_kwargs)`

### `def test___scale___get_string_property___returns_assigned_value(init_kwargs)`

### `def test___scale___set_string_property___returns_assigned_value(init_kwargs)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/test_stream_readers_ci.py -->
## PYTHON MODULE: tests/component/test_stream_readers_ci.py

- `SIGNAL_TO_MEASURE = '100kHzTimebase'`

- `EXPECTED_FREQUENCY = 100000.0`

- `EXPECTED_FREQUENCY_TOLERANCE = 1e-06`

- `EXPECTED_DUTY_CYCLE = 0.5`

- `EXPECTED_DUTY_CYCLE_TOLERANCE = 1e-06`

- `EXPECTED_HIGH_TIME = 1.0 / EXPECTED_FREQUENCY * EXPECTED_DUTY_CYCLE`

- `EXPECTED_LOW_TIME = 1.0 / EXPECTED_FREQUENCY * (1.0 - EXPECTED_DUTY_CYCLE)`

- `EXPECTED_TIME_TOLERANCE = 1e-06`

- `EXPECTED_HIGH_TICKS = int(100000000.0 / EXPECTED_FREQUENCY * EXPECTED_DUTY_CYCLE)`

- `EXPECTED_LOW_TICKS = int(100000000.0 / EXPECTED_FREQUENCY * (1.0 - EXPECTED_DUTY_CYCLE))`

- `EXPECTED_TICKS_TOLERANCE = 1`

### `def _validate_count_edges_data(data: numpy.typing.NDArray[numpy.uint32]) -> None`

### `def _validate_frequency_data(data: numpy.typing.NDArray[numpy.float64]) -> None`

### `def _validate_pulse_frequency_data(frequency_data: numpy.typing.NDArray[numpy.float64], duty_cycle_data: numpy.typing.NDArray[numpy.float64]) -> None`

### `def _validate_pulse_time_data(high_time_data: numpy.typing.NDArray[numpy.float64], low_time_data: numpy.typing.NDArray[numpy.float64]) -> None`

### `def _validate_pulse_tick_data(high_tick_data: numpy.typing.NDArray[numpy.uint32], low_tick_data: numpy.typing.NDArray[numpy.uint32]) -> None`

### `def ci_count_edges_task(task: nidaqmx.Task, real_x_series_device: nidaqmx.system.Device) -> nidaqmx.Task`

### `def ci_frequency_task(task: nidaqmx.Task, real_x_series_device: nidaqmx.system.Device) -> nidaqmx.Task`

### `def ci_pulse_frequency_task(task: nidaqmx.Task, real_x_series_device: nidaqmx.system.Device) -> nidaqmx.Task`

### `def ci_pulse_time_task(task: nidaqmx.Task, real_x_series_device: nidaqmx.system.Device) -> nidaqmx.Task`

### `def ci_pulse_ticks_task(task: nidaqmx.Task, real_x_series_device: nidaqmx.system.Device) -> nidaqmx.Task`

### `def test___counter_reader___read_one_sample_uint32___returns_valid_samples(ci_count_edges_task: nidaqmx.Task) -> None`

### `def test___counter_reader___read_many_sample_uint32___returns_valid_samples(ci_count_edges_task: nidaqmx.Task) -> None`

### `def test___counter_reader___read_many_sample_uint32_with_wrong_dtype___raises_error_with_correct_dtype(ci_count_edges_task: nidaqmx.Task) -> None`

### `def test___counter_reader___read_one_sample_double___returns_valid_samples(ci_frequency_task: nidaqmx.Task) -> None`

### `def test___counter_reader___read_many_sample_double___returns_valid_samples(ci_frequency_task: nidaqmx.Task) -> None`

### `def test___counter_reader___read_many_sample_double_with_wrong_dtype___raises_error_with_correct_dtype(ci_frequency_task: nidaqmx.Task) -> None`

### `def test___counter_reader___read_one_sample_pulse_frequency___returns_valid_samples(ci_pulse_frequency_task: nidaqmx.Task) -> None`

### `def test___counter_reader___read_many_sample_pulse_frequency___returns_valid_samples(ci_pulse_frequency_task: nidaqmx.Task) -> None`

### `def test___counter_reader___read_many_sample_pulse_frequency_with_wrong_dtype___raises_error_with_correct_dtype(ci_pulse_frequency_task: nidaqmx.Task, frequency_dtype, duty_cycle_dtype) -> None`

### `def test___counter_reader___read_one_sample_pulse_time___returns_valid_samples(ci_pulse_time_task: nidaqmx.Task) -> None`

### `def test___counter_reader___read_many_sample_pulse_time___returns_valid_samples(ci_pulse_time_task: nidaqmx.Task) -> None`

### `def test___counter_reader___read_many_sample_pulse_time_with_wrong_dtype___raises_error_with_correct_dtype(ci_pulse_time_task: nidaqmx.Task, high_time_dtype: numpy.typing.DTypeLike, low_time_dtype: numpy.typing.DTypeLike) -> None`

### `def test___counter_reader___read_one_sample_pulse_ticks___returns_valid_samples(ci_pulse_ticks_task: nidaqmx.Task) -> None`

### `def test___counter_reader___read_many_sample_pulse_ticks___returns_valid_samples(ci_pulse_ticks_task: nidaqmx.Task) -> None`

### `def test___counter_reader___read_many_sample_pulse_ticks_with_wrong_dtype___raises_error_with_correct_dtype(ci_pulse_ticks_task: nidaqmx.Task, high_ticks_dtype: numpy.typing.DTypeLike, high_ticks_default: float | int, low_ticks_dtype: numpy.typing.DTypeLike, low_ticks_default: float | int) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/test_stream_writers_co.py -->
## PYTHON MODULE: tests/component/test_stream_writers_co.py

- `START_DUTY_CYCLE = 0.1`

- `END_DUTY_CYCLE = 0.9`

- `START_FREQUENCY = 10000.0`

- `END_FREQUENCY = 100000.0`

- `TIMEBASE_NAME = '100MHzTimebase'`

- `TIMEBASE_FREQUENCY = 100000000.0`

- `EXPECTED_FREQUENCY_TOLERANCE = 1e-06`

- `EXPECTED_DUTY_CYCLE_TOLERANCE = 1e-06`

### `def _configure_and_start_co_task(task: nidaqmx.Task) -> None`

### `def co_freq_task(generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device) -> nidaqmx.Task`

### `def co_time_task(generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device) -> nidaqmx.Task`

### `def co_ticks_task(generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device) -> nidaqmx.Task`

### `def ci_freq_loopback_task(generate_task: Callable[[], nidaqmx.Task], real_x_series_device: nidaqmx.system.Device) -> nidaqmx.Task`

### `def _get_counter_freq_data(num_samples: int) -> list[CtrFreq]`

### `def _to_time(freq: CtrFreq) -> CtrTime`

### `def _to_ticks(freq: CtrFreq) -> CtrTick`

### `def test___counter_writer___write_one_sample_pulse_frequency___updates_output(co_freq_task: nidaqmx.Task, ci_freq_loopback_task: nidaqmx.Task) -> None`

### `def test___counter_writer___write_many_sample_pulse_frequency___updates_output(co_freq_task: nidaqmx.Task, ci_freq_loopback_task: nidaqmx.Task) -> None`

### `def test___counter_writer___write_many_sample_pulse_frequency_with_wrong_dtype___raises_error_with_correct_dtype(co_freq_task: nidaqmx.Task, freq_dtype: numpy.typing.DTypeLike, duty_cycle_dtype: numpy.typing.DTypeLike) -> None`

### `def test___counter_writer___write_one_sample_pulse_time___updates_output(co_time_task: nidaqmx.Task, ci_freq_loopback_task: nidaqmx.Task) -> None`

### `def test___counter_writer___write_many_sample_pulse_time___updates_output(co_time_task: nidaqmx.Task, ci_freq_loopback_task: nidaqmx.Task) -> None`

### `def test___counter_writer___write_many_sample_pulse_time_with_wrong_dtype___raises_error_with_correct_dtype(co_time_task: nidaqmx.Task, high_time_dtype: numpy.typing.DTypeLike, low_time_dtype: numpy.typing.DTypeLike) -> None`

### `def test___counter_writer___write_one_sample_pulse_ticks___updates_output(co_ticks_task: nidaqmx.Task, ci_freq_loopback_task: nidaqmx.Task) -> None`

### `def test___counter_writer___write_many_sample_pulse_ticks___updates_output(co_ticks_task: nidaqmx.Task, ci_freq_loopback_task: nidaqmx.Task) -> None`

### `def test___counter_writer___write_many_sample_pulse_ticks_with_wrong_dtype___raises_error_with_correct_dtype(co_ticks_task: nidaqmx.Task, high_ticks_dtype: numpy.typing.DTypeLike, low_ticks_dtype: numpy.typing.DTypeLike) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/test_task.py -->
## PYTHON MODULE: tests/component/test_task.py

### `def ai_bridge_task(task: nidaqmx.Task, device) -> nidaqmx.Task`

### `def ai_strain_gage_task(task: nidaqmx.Task, device) -> nidaqmx.Task`

### `def ai_thermocouple_task(task: nidaqmx.Task, device) -> nidaqmx.Task`

### `def ai_on_demand_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task`

Gets an AI task.

### `def test___task___create_task_with_same_name___raises_duplicate_task(init_kwargs)`

### `def test___tasks_with_different_names___compare___not_equal(generate_task)`

### `def test___tasks_with_different_names___hash___not_equal(generate_task)`

### `def test___arguments_specified___perform_bridge_offset_nulling_cal___no_errors(ai_bridge_task: nidaqmx.Task, skip_unsupported_channels) -> None`

### `def test___default_arguments___perform_bridge_offset_nulling_cal___no_errors(ai_bridge_task: nidaqmx.Task) -> None`

### `def test___perform_bridge_shunt_cal___no_errors(ai_bridge_task: nidaqmx.Task, shunt_resistor_value, shunt_resistor_location, shunt_resistor_select, shunt_resistor_source, bridge_resistance, skip_unsupported_channels) -> None`

### `def test___perform_bridge_shunt_cal_default___no_errors(ai_bridge_task: nidaqmx.Task) -> None`

### `def test___perform_strain_shunt_cal___no_errors(ai_strain_gage_task: nidaqmx.Task, shunt_resistor_value, shunt_resistor_location, shunt_resistor_select, shunt_resistor_source, skip_unsupported_channels) -> None`

### `def test___perform_strain_shunt_cal_default___no_errors(ai_strain_gage_task: nidaqmx.Task) -> None`

### `def test___arguments_specified___perform_thrmcpl_lead_offset_nulling_cal___no_errors(ai_thermocouple_task: nidaqmx.Task, skip_unsupported_channels) -> None`

### `def test___default_arguments___perform_thrmcpl_lead_offset_nulling_cal___no_errors(ai_thermocouple_task: nidaqmx.Task) -> None`

### `def test___on_demand_task_is_done___is_task_done___returns_true(ai_on_demand_task: nidaqmx.Task)`

### `def test___task___add_global_channels___adds_to_channel_names(task: nidaqmx.Task)`

### `def test___task___create_weakref___succeeds(task: nidaqmx.Task)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/test_task_events.py -->
## PYTHON MODULE: tests/component/test_task_events.py

### `def ai_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task`

### `def ai_task_with_real_device(task: nidaqmx.Task, real_x_series_device: nidaqmx.system.Device) -> nidaqmx.Task`

### `def ao_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task`

### `def test___done_event_registered___run_finite_acquisition___callback_invoked_once_with_success_status(ai_task: nidaqmx.Task) -> None`

### `def test___done_event_registered___call_stop_close_in_callback___task_closed_with_success_status(sim_6363_device: nidaqmx.system.Device, init_kwargs: dict) -> None`

### `def test___every_n_samples_event_registered___call_stop_close_in_callback___task_closed_with_success_status(sim_6363_device: nidaqmx.system.Device, init_kwargs: dict) -> None`

### `def test___every_n_samples_event_registered___run_finite_acquisition___callback_invoked_n_times_with_type_and_num_samples(ai_task: nidaqmx.Task) -> None`

### `def test___signal_event_registered___run_finite_acquisition___callback_invoked_n_times_with_type(ai_task_with_real_device: nidaqmx.Task) -> None`

### `def test___done_event_unregistered___run_finite_acquisition___callback_not_invoked(ai_task: nidaqmx.Task) -> None`

### `def test___every_n_samples_event_unregistered___run_finite_acquisition___callback_not_invoked(ai_task: nidaqmx.Task) -> None`

### `def test___signal_event_unregistered___run_finite_acquisition___callback_not_invoked(ai_task_with_real_device: nidaqmx.Task) -> None`

### `def test___done_and_every_n_samples_events_registered___run_finite_acquisition___callbacks_invoked(ai_task: nidaqmx.Task) -> None`

### `def test___done_and_every_n_samples_events_registered___run_multiple_finite_acquisitions___callbacks_invoked(ai_task: nidaqmx.Task) -> None`

### `def test___ai_task____run_multiple_finite_acquisitions_with_varying_every_n_samples_event_interval___callbacks_invoked(ai_task: nidaqmx.Task) -> None`

### `def test___done_event_registered___register_done_event___already_registered_error_raised(ai_task: nidaqmx.Task) -> None`

### `def test___every_n_samples_acquired_into_buffer_event_registered___register_every_n_samples_acquired_into_buffer_event___already_registered_error_raised(ai_task: nidaqmx.Task) -> None`

### `def test___every_n_samples_transferred_from_buffer_event_registered___register_every_n_samples_transferred_from_buffer_event___already_registered_error_raised(ao_task: nidaqmx.Task) -> None`

### `def test___signal_event_registered___register_signal_event___already_registered_error_raised(ai_task: nidaqmx.Task) -> None`

### `def test___ai_task___register_wrong_every_n_samples_event___not_supported_by_device_error_raised(ai_task: nidaqmx.Task) -> None`

### `def test___ao_task___register_wrong_every_n_samples_event___not_supported_by_device_error_raised(ao_task: nidaqmx.Task) -> None`

### `def test___task___register_unregister_done_event___callback_not_invoked(ai_task: nidaqmx.Task) -> None`

### `def test___task___register_unregister_every_n_samples_acquired_into_buffer_event___callback_not_invoked(ai_task: nidaqmx.Task) -> None`

### `def test___task___register_unregister_every_n_samples_transferred_from_buffer_event___callback_not_invoked(ao_task: nidaqmx.Task) -> None`

### `def test___task___register_unregister_signal_event___callback_not_invoked(ai_task: nidaqmx.Task) -> None`

### `def test___events_registered_and_grpc_channel_closed___close_task___events_cleaned_up_and_clear_task_error_raised(ai_task: nidaqmx.Task, grpc_channel)`

### `def test___event_callback_that_raises_exceptions___run_finite_acquisition___exceptions_ignored(ai_task: nidaqmx.Task) -> None`

### `def test___event_callback_that_raises_exceptions___run_finite_acquisition___exceptions_logged(ai_task: nidaqmx.Task, caplog: pytest.LogCaptureFixture) -> None`

### `def _exception_matches(e1: BaseException, e2: BaseException) -> bool`

### `def _get_exception(record: LogRecord) -> BaseException`

### `def _wait_for_log_records(caplog: pytest.LogCaptureFixture, message_substring: str, expected_count: int, timeout=10.0) -> list[LogRecord]`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/test_task_properties.py -->
## PYTHON MODULE: tests/component/test_task_properties.py

### `def ai_task(task: Task, sim_6363_device: Device) -> Task`

Gets an AI task.

### `def test___get_channels___returns_channels(ai_task: Task)`

### `def test___get_channels___shared_interpreter(ai_task: Task)`

### `def test___get_devices___returns_devices(ai_task: Task, sim_6363_device: Device)`

### `def test___get_devices___shared_interpreter(ai_task: Task)`

### `def test___task___set_nonexistent_property___raises_exception(task: Task)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/test_task_resource_warnings.py -->
## PYTHON MODULE: tests/component/test_task_resource_warnings.py

### `def test___unclosed_task___leak_task___resource_warning_raised(task)`

### `def test___grpc_task___leak_task___resource_warning_not_raised(task)`

### `def test___closed_task___del_task___resource_warning_not_raised(init_kwargs)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/component/test_watchdog.py -->
## PYTHON MODULE: tests/component/test_watchdog.py

### `def test___watchdog_task___cfg_watchdog_ao_expir_states___no_error(generate_watchdog_task: Callable[..., WatchdogTask], sim_9189_device: Device, sim_9263_device: Device)`

### `def test___watchdog_task___cfg_watchdog_co_expir_states___no_error(generate_watchdog_task: Callable[..., WatchdogTask], sim_9189_device: Device, sim_9401_device: Device)`

### `def test___watchdog_task___clear_expiration___no_error(generate_watchdog_task: Callable[..., WatchdogTask], sim_9189_device: Device, sim_9263_device: Device)`

### `def test___watchdog_task___create_weakref___succeeds(generate_watchdog_task: Callable[..., WatchdogTask], sim_9189_device: Device)`

### `def test___watchdog_task___set_nonexistent_property___raises_exception(generate_watchdog_task: Callable[..., WatchdogTask], sim_9189_device: Device)`

### `def test___watchdog_expiration_states___set_nonexistent_property___raises_exception(generate_watchdog_task: Callable[..., WatchdogTask], sim_9189_device: Device, sim_9263_device: Device)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/conftest.py -->
## PYTHON MODULE: tests/conftest.py

### MODULE DOCSTRING

Fixtures used in the DAQmx tests.

### `class Error(Exception)`

Base error class.

### `class NoFixtureDetectedError(Error)`

Custom error class when no fixtures are available.

### `class DeviceType(Enum)`

Device Type.

### `class SamplingType(Enum)`

Sampling Type.

### `def pytest_generate_tests(metafunc: pytest.Metafunc) -> None`

Parametrizes the "init_kwargs" fixture by examining the the markers set for a test.

    This is used to decide if tests for gRPC or Library interpreters should be run.
    This is done based on the custom markers @pytest.mark.grpc_only and @pytest.mark.library_only.
    

### `def system(init_kwargs) -> nidaqmx.system.System`

Gets system instance based on the grpc options.

### `def _x_series_device(device_type: DeviceType, system: nidaqmx.system.System, sampling_type: SamplingType=SamplingType.ANY, min_num_lines: int=8) -> nidaqmx.system.Device`

### `def _device_by_product_type(product_type: str, device_type: DeviceType, system: nidaqmx.system.System) -> nidaqmx.system.Device`

### `def _cdaq_module_by_product_type(product_type: str, cdaq_chassis: nidaqmx.system.Device) -> nidaqmx.system.Device`

### `def real_x_series_device(system: nidaqmx.system.System) -> nidaqmx.system.Device`

Gets real X Series device information.

### `def real_x_series_device_32dio(system: nidaqmx.system.System) -> nidaqmx.system.Device`

Gets real 32 DIO X Series device information.

### `def real_x_series_multiplexed_device(system: nidaqmx.system.System) -> nidaqmx.system.Device`

Gets device information for a real X Series device with multiplexed sampling.

### `def sim_4311_device(system: nidaqmx.system.System) -> nidaqmx.system.Device`

Gets 4311 device information.

### `def sim_6363_device(system: nidaqmx.system.System) -> nidaqmx.system.Device`

Gets simulated 6363 device information.

### `def sim_6423_device(system: nidaqmx.system.System) -> nidaqmx.system.Device`

Gets simulated 6423 device information.

### `def sim_6535_device(system: nidaqmx.system.System) -> nidaqmx.system.Device`

Gets simulated 6535 device information.

### `def sim_9189_device(system: nidaqmx.system.System) -> nidaqmx.system.Device`

Gets simulated 9185 device information.

### `def sim_9205_device(sim_9189_device: nidaqmx.system.Device) -> nidaqmx.system.Device`

Gets device information for a simulated 9205 device within a 9185.

### `def sim_time_aware_9215_device(sim_9189_device: nidaqmx.system.Device) -> nidaqmx.system.Device`

Gets device information for a simulated 9215 device within a 9185.

### `def sim_9263_device(sim_9189_device: nidaqmx.system.Device) -> nidaqmx.system.Device`

Gets device information for a simulated 9263 device within a 9185.

### `def sim_9401_device(sim_9189_device: nidaqmx.system.Device) -> nidaqmx.system.Device`

Gets device information for a simulated 9401 device within a 9185.

### `def sim_9775_device(sim_9189_device: nidaqmx.system.Device) -> nidaqmx.system.Device`

Gets device information for a simulated 9775 device within a 9185.

### `def sim_ts_chassis(system: nidaqmx.system.System) -> nidaqmx.system.Device`

Gets simulated TestScale chassis information.

### `def sim_ts_power_device(sim_ts_chassis: nidaqmx.system.Device) -> nidaqmx.system.Device`

Gets simulated power device information.

### `def sim_ts_voltage_device(sim_ts_chassis: nidaqmx.system.Device) -> nidaqmx.system.Device`

Gets simulated voltage device information.

### `def sim_ts_power_devices(sim_ts_chassis: nidaqmx.system.Device) -> list[nidaqmx.system.Device]`

Gets simulated power devices information.

### `def sim_charge_device(system: nidaqmx.system.System) -> nidaqmx.system.Device`

Gets a simulated 4480.

### `def sim_dsa_device(system: nidaqmx.system.System) -> nidaqmx.system.Device`

Gets a simulated 4466.

### `def sim_dmm_device(system: nidaqmx.system.System) -> nidaqmx.system.Device`

Gets a simulated myDAQ.

### `def sim_bridge_device(system: nidaqmx.system.System) -> nidaqmx.system.Device`

Gets a simulated 4431.

### `def sim_position_device(system: nidaqmx.system.System) -> nidaqmx.system.Device`

Gets a simulated 4340.

### `def sim_temperature_device(system: nidaqmx.system.System) -> nidaqmx.system.Device`

Gets a simulated 4353.

### `def sim_velocity_device(system: nidaqmx.system.System) -> nidaqmx.system.Device`

Gets a simulated 9361.

### `def multi_threading_test_devices(system: nidaqmx.system.System) -> list[nidaqmx.system.Device]`

Gets multi threading test devices information.

### `def device(request, system: nidaqmx.system.System) -> nidaqmx.system.Device`

Gets the device information based on the device name.

### `def test_assets_directory() -> pathlib.Path`

Gets path to test_assets directory.

### `def grpc_server_process() -> Generator[GrpcServerProcess]`

Gets the grpc server process.

### `def grpc_channel(request: pytest.FixtureRequest) -> grpc.Channel`

Gets a gRPC channel.

### `def shared_grpc_channel(grpc_server_process: GrpcServerProcess) -> Generator[grpc.Channel]`

Gets the shared gRPC channel.

### `def temporary_grpc_channel(request: pytest.FixtureRequest, grpc_server_process: GrpcServerProcess) -> Generator[grpc.Channel]`

Gets a temporary gRPC channel (not shared with other tests).

### `def grpc_init_kwargs(request: pytest.FixtureRequest, grpc_channel: grpc.Channel) -> dict`

Gets the keyword arguments required for creating the gRPC interpreter.

### `def library_init_kwargs()`

Gets the keyword arguments required for creating the library interpreter.

### `def init_kwargs(request)`

Gets the keyword arguments to create a nidaqmx session.

### `def task(request, generate_task) -> nidaqmx.Task`

Gets a task instance.

    The closure of task objects will be done by this fixture once the test is complete.
    This fixture owns the task. Do not use it for test cases that destroy the task, or else you
    may get double-close warnings.
    

### `def generate_task(init_kwargs) -> Generator[Callable[..., nidaqmx.Task]]`

Gets a factory function which can be used to generate new tasks.

    The closure of task objects will be done by this fixture once the test is complete.
    This fixture owns the task. Do not use it for test cases that destroy the task, or else you
    may get double-close warnings.
    

### `def persisted_task(request, system: nidaqmx.system.System) -> nidaqmx.system.storage.PersistedTask`

Gets the persisted task based on the task name.

### `def persisted_scale(request, system: nidaqmx.system.System) -> nidaqmx.system.storage.PersistedScale`

Gets the persisted scale based on the scale name.

### `def persisted_channel(request, system: nidaqmx.system.System) -> nidaqmx.system.storage.PersistedChannel`

Gets the persisted channel based on the channel name.

### `def watchdog_task(request, sim_6363_device, generate_watchdog_task) -> nidaqmx.system.WatchdogTask`

Gets a watchdog task instance.

### `def generate_watchdog_task(init_kwargs) -> Generator[Callable[..., nidaqmx.system.WatchdogTask]]`

Gets a factory function which can be used to generate new watchdog tasks.

    The closure of task objects will be done by this fixture once the test is complete.
    This fixture owns the task. Do not use it for test cases that destroy the task, or else you
    may get double-close warnings.
    

### `def _get_marker_value(request, marker_name, default=None)`

Gets the value of a pytest marker based on the marker name.

### `def thread_pool_executor() -> Generator[ThreadPoolExecutor]`

Creates a thread pool executor.

    When the test completes, this fixture shuts down the thread pool executor. If any futures are
    still running at this time, shutting down the thread pool executor will wait for them to
    complete.
    

### `def interpreter(system: nidaqmx.system.System) -> BaseInterpreter`

Gets an interpreter.

### `def teds_assets_directory(test_assets_directory: pathlib.Path) -> pathlib.Path`

Returns the path to TEDS assets.

### `def voltage_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path`

Returns a TEDS file path.

### `def accelerometer_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path`

Returns a TEDS file path.

### `def bridge_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path`

Returns a TEDS file path.

### `def force_bridge_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path`

Returns a TEDS file path.

### `def current_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path`

Returns a TEDS file path.

### `def force_iepe_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path`

Returns a TEDS file path.

### `def microphone_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path`

Returns a TEDS file path.

### `def lvdt_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path`

Returns a TEDS file path.

### `def rvdt_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path`

Returns a TEDS file path.

### `def pressure_bridge_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path`

Returns a TEDS file path.

### `def torque_bridge_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path`

Returns a TEDS file path.

### `def resistance_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path`

Returns a TEDS file path.

### `def rtd_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path`

Returns a TEDS file path.

### `def strain_gage_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path`

Returns a TEDS file path.

### `def thermocouple_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path`

Returns a TEDS file path.

### `def thermistor_iex_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path`

Returns a TEDS file path.

### `def thermistor_vex_teds_file_path(teds_assets_directory: pathlib.Path) -> pathlib.Path`

Returns a TEDS file path.

### `def feature_toggles(monkeypatch: pytest.MonkeyPatch, request: pytest.FixtureRequest) -> None`

Test fixture that disables or enables feature toggles.

### `def pytest_collection_modifyitems(items: list[pytest.Item]) -> None`

Hook to inject fixtures based on marks.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/helpers.py -->
## PYTHON MODULE: tests/helpers.py

### MODULE DOCSTRING

This contains the helpers methods used in the DAQmx tests.

- `POWER_ABS_EPSILON = 0.001`

### `def generate_random_seed()`

Creates a random integer.

### `def configure_teds(phys_chan: PhysicalChannel, teds_file_path: str | pathlib.PurePath | None=None) -> Generator[PhysicalChannel]`

Yields a physical channel with TEDS configured and then clears it after the test is done.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/legacy/__init__.py -->
## PYTHON MODULE: tests/legacy/__init__.py

### MODULE DOCSTRING

Legacy tests that do not follow NI's Python testing conventions.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/legacy/test_channel_creation.py -->
## PYTHON MODULE: tests/legacy/test_channel_creation.py

### MODULE DOCSTRING

Tests for creating channels.

### `class TestAnalogCreateChannels()`

Contains a collection of pytest tests.

    These validate the analog Create Channel functions in the NI-DAQmx Python API.
    These tests simply call create channel functions with some valid values
    for function parameters, and then read properties to verify that the
    parameter values were set properly.
    

#### `def test_create_ai_voltage_chan(self, task, sim_6363_device, seed)`

Test for creating AI voltage channel.

#### `def test_create_ai_current_chan(self, task, sim_6363_device, seed)`

Test for creating AI current channel.

#### `def test_create_ai_rtd_chan(self, task, sim_6363_device, seed)`

Test for creating AI RTD channel.

#### `def test_create_ai_thrmstr_chan_iex(self, task, sim_6363_device, seed)`

Test for creating AI thermistor channel with current excitation.

#### `def test_create_ai_thrmstr_chan_vex(self, task, sim_6363_device, seed)`

Test for creating AI thermistor channel with voltage excitation.

#### `def test_create_ai_resistance_chan(self, task, sim_6363_device, seed)`

Test for creating AI resistance channel.

#### `def test_ai_strain_gage_chan(self, task, sim_6363_device, seed)`

Test for creating AI strain gage channel.

#### `def test_create_ai_voltage_chan_with_excit(self, task, sim_6363_device, seed)`

Test for creating AI voltage channel.

#### `def test_create_ai_power_chan(self, task, sim_ts_power_device, seed)`

Test for creating AI power channel.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/legacy/test_channels.py -->
## PYTHON MODULE: tests/legacy/test_channels.py

### MODULE DOCSTRING

Tests for validating the channel objects.

### `class TestChannels()`

Contains a collection of pytest tests.

    This validate the channel objects in the NI-DAQmx Python API.
    

#### `def test_ai_channel(self, task, sim_6363_device)`

Tests for creating ai channel.

#### `def test_ao_channel(self, task, sim_6363_device)`

Tests for creating ao channel.

#### `def test_ci_channel(self, task, real_x_series_device)`

Tests for creating ci channel.

#### `def test_co_channel(self, task, sim_6363_device)`

Tests for creating co channel.

#### `def test_di_channel(self, task, sim_6363_device)`

Tests for creating di channel.

#### `def test_do_channel(self, task, sim_6363_device)`

Tests for creating do channel.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/legacy/test_container_operations.py -->
## PYTHON MODULE: tests/legacy/test_container_operations.py

### MODULE DOCSTRING

Tests for validating the container operations.

### `class TestContainerOperations()`

Contains a collection of pytest tests.

    This validate the container operations in the Python NI-DAQmx API.
    

#### `def test_concatenate_operations(self, task, sim_6363_device, seed)`

Test for concatenate operation.

#### `def test_equality_operations(self, task, sim_6363_device, seed)`

Test for equality operation.

#### `def test_hash_operations(self, generate_task, sim_6363_device, seed)`

Test for hash operation.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/legacy/test_enum_bitfields.py -->
## PYTHON MODULE: tests/legacy/test_enum_bitfields.py

### MODULE DOCSTRING

Tests for validating the bitfield enums.

### `def test_coupling_bitfield()`

Test for coupling bitfield.

### `def test_terminal_configuration_bitfield()`

Test for terminal configuration bitfield.

### `def test_trigger_usage_bitfield()`

Test for trigger usage bitfield.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/legacy/test_events.py -->
## PYTHON MODULE: tests/legacy/test_events.py

### MODULE DOCSTRING

Tests for validating the NI-DAQmx events.

### `class TestEvents()`

Contains a collection of pytest tests.

    This validate the NI-DAQmx events functionality in the Python NI-DAQmx API.
    

#### `def test_every_n_samples_event(self, task, sim_6363_device, seed)`

Test for validating every n samples event.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/legacy/test_export_signals.py -->
## PYTHON MODULE: tests/legacy/test_export_signals.py

### MODULE DOCSTRING

Tests for validating export signals functionality.

### `class TestExportSignals(TestDAQmxIOBase)`

Contains a collection of pytest tests.

    These validate the export signals functionality in the NI-DAQmx Python API.
    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    

#### `def test_export_signals(self, task, sim_6363_device, seed)`

Test for validating export signals.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/legacy/test_invalid_reads.py -->
## PYTHON MODULE: tests/legacy/test_invalid_reads.py

### MODULE DOCSTRING

Tests for validating invalid read functionality.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/legacy/test_invalid_writes.py -->
## PYTHON MODULE: tests/legacy/test_invalid_writes.py

### MODULE DOCSTRING

Tests for validating invalid write functionality.

### `class TestInvalidWrites()`

Contains a collection of pytest tests.

    These validate the write functionality with improper data.
    

#### `def test_insufficient_write_data(self, task, sim_6363_device, seed)`

Test for validating write functionality with insufficient data.

#### `def test_insufficient_numpy_write_data(self, task, sim_6363_device, seed)`

Test for validating write functionality with insufficient data.

#### `def test_extraneous_write_data(self, task, sim_6363_device, seed)`

Test for validating write functionality with extraneous data.

#### `def test_extraneous_numpy_write_data(self, task, sim_6363_device, seed)`

Test for validating write functionality with extraneous data.

#### `def test_numpy_write_incorrectly_shaped_data(self, task, sim_6363_device, seed)`

Test for validating write functionality with incorrectly shaped data.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/legacy/test_multi_threading.py -->
## PYTHON MODULE: tests/legacy/test_multi_threading.py

### MODULE DOCSTRING

Tests for validating multi-thread reading functionality.

### `class Error(Exception)`

Base error class.

### `class NoFixtureDetectedError(Error)`

Custom error class when no fixtures are available.

### `class DAQmxReaderActor(pykka.ThreadingActor)`

A proxy for reading samples.

#### `def __init__(self, task)`

A proxy for reading samples.

#### `def read(self, samples_per_read, number_of_reads, timeout=10)`

Reads the samples from the thread.

### `class TestMultiThreadedReads()`

Contains a collection of pytest tests.

    This validates multi-threaded reads using the NI-DAQmx Python API.
    These tests create multiple tasks, each of which uses one of 4 simulated
    X Series devices.
    

#### `def test_multi_threaded_analog_read(self, multi_threading_test_devices, seed, init_kwargs)`

Test for validating multi-thread read operation.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/legacy/test_power_up_states.py -->
## PYTHON MODULE: tests/legacy/test_power_up_states.py

### MODULE DOCSTRING

Tests for validating power up states functions.

### `class TestPowerUpStates()`

Contains a collection of pytest tests.

    This validate the power up states functions in the Python NI-DAQmx API.
    

#### `def test_digital_power_up_states(self, real_x_series_device, system)`

Test for validating digital power up states.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/legacy/test_properties.py -->
## PYTHON MODULE: tests/legacy/test_properties.py

### MODULE DOCSTRING

Tests for validating properties for different basic data types.

### `class TestPropertyBasicDataTypes()`

Contains a collection of pytest tests.

    This validates the property getter,setter and deleter methods for different basic data types.
    

#### `def test_boolean_property(self, task, sim_6363_device)`

Test for validating boolean property.

#### `def test_enum_property(self, task, sim_6363_device)`

Test for validating enum property.

#### `def test_float_property(self, task, sim_6363_device)`

Test for validating float property.

#### `def test_int_property(self, task, sim_6363_device, seed)`

Test for validating integer property.

#### `def test_string_property(self, task, sim_6363_device)`

Test for validating string property.

#### `def test_uint_property(self, task, sim_6363_device, seed)`

Test for validating uint property.

### `class TestPropertyListDataTypes()`

Contains a collection of pytest tests.

    This validates the property getter, setter, and deleter methods for list data types.
    There are almost no setter and deleter methods for properties that have
    list data types.
    

#### `def test_list_of_strings_property(self, sim_6363_device)`

Test for validating list of strings property.

#### `def test_list_of_enums_property(self, sim_6363_device)`

Test for validating list of enums property.

#### `def test_list_of_floats_property(self, task, device, seed)`

Test for validating list of float property.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/legacy/test_read_exceptions.py -->
## PYTHON MODULE: tests/legacy/test_read_exceptions.py

### MODULE DOCSTRING

Tests for validating read error behavior.

### `class TestReadExceptions()`

Contains a collection of pytest tests.

    This validates the Read error behavior in the NI-DAQmx Python API.
    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    

#### `def test_timeout(self, generate_task, real_x_series_device)`

Test for validating read timeout.

#### `def test_timeout_raw(self, generate_task, real_x_series_device)`

Test for validating read timeout.

#### `def test_timeout_stream(self, generate_task, real_x_series_device)`

Test for validating read timeout.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/legacy/test_read_write.py -->
## PYTHON MODULE: tests/legacy/test_read_write.py

### MODULE DOCSTRING

Tests for validating read and write operation.

### `class Error(Exception)`

Base error class.

### `class NoFixtureDetectedError(Error)`

Custom error class when no fixtures are available.

### `class TestDAQmxIOBase()`

Contains a collection of methods that are used in read and write tests.

    Classes which validate the Task Read and Write functions in the NI-DAQmx Python API
    uses these methods.These tests use only a single X Series device by utilizing the
    internal loopback routes on the device.
    

#### `def _get_device_counters(self, device)`

#### `def _get_device_pfi_lines(self, device)`

#### `def _get_analog_loopback_channels(self, device)`

### `class TestAnalogReadWrite(TestDAQmxIOBase)`

Contains a collection of pytest tests.

    These validate the analog Read and Write functions in the NI-DAQmx Python API.
    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    

#### `def test_1_chan_1_samp(self, generate_task, real_x_series_device, seed)`

Test to validate reading and writing a sample data .

#### `def test_n_chan_1_samp(self, generate_task, real_x_series_device, seed)`

Test to validate reading and writing sample data .

#### `def test_1_chan_n_samp(self, generate_task, real_x_series_device, seed)`

Test to validate reading and writing sample data .

#### `def test_n_chan_n_samp(self, generate_task, real_x_series_device, seed)`

Test to validate reading and writing sample data .

### `class TestDigitalReadWrite(TestDAQmxIOBase)`

Contains a collection of pytest tests.

    These validate the digital Read and Write functions in the NI-DAQmx Python API.
    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    

#### `def test_bool_1_chan_1_samp(self, task, real_x_series_device, seed)`

Test to validate reading and writing boolean data .

#### `def test_bool_n_chan_1_samp(self, task, real_x_series_device, seed)`

Test to validate reading and writing boolean data .

#### `def test_uint_1_chan_1_samp(self, task, real_x_series_device, seed)`

Test to validate reading and writing uint data .

#### `def test_uint_multi_port(self, task, real_x_series_device, seed)`

Test to validate reading and writing uint data .

### `class TestCounterReadWrite(TestDAQmxIOBase)`

Contains a collection of pytest tests.

    These validate the counter Read and Write functions in the NI-DAQmx Python API.
    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    

#### `def test_count_edges_1_samp(self, generate_task, real_x_series_device, seed)`

Test to validate the set and read operations of edge count.

#### `def test_count_edges_n_samp(self, generate_task, real_x_series_device, seed)`

Test to validate the set and read operations of edge count.

#### `def test_pulse_freq_1_samp(self, generate_task, real_x_series_device, seed)`

Test to validate the set and read operations of pulse frequency.

#### `def test_pulse_time_1_samp(self, generate_task, real_x_series_device, seed)`

Test to validate the set and read operations of pulse time.

#### `def test_pulse_ticks_1_samp(self, generate_task, real_x_series_device, seed)`

Test to validate the set and read operations of pulse ticks.

### `class TestPowerRead(TestDAQmxIOBase)`

Contains a collection of pytest tests.

    These validate the power Read and Write functions in the NI-DAQmx Python API.
    These tests use simulated TestScale PPS device(s), TS-15200.
    

#### `def test_power_1_chan_1_samp(self, task, sim_ts_power_device, seed, output_enable)`

Test to validate the set and read operations of power.

#### `def test_power_n_chan_1_samp(self, task, sim_ts_power_devices, seed, output_enables)`

Test to validate the set and read operations of power.

#### `def test_power_1_chan_n_samp(self, task, sim_ts_power_device, seed, output_enable)`

Test to validate the set and read operations of power.

#### `def test_power_n_chan_n_samp(self, task, sim_ts_power_devices, seed, output_enables)`

Test to validate the set and read operations of power.

#### `def test_mixed_chans(self, task, sim_6363_device, seed)`

Test to validate mixed channels.

#### `def test_mixed_chans_with_power(self, task, sim_ts_power_device, sim_ts_voltage_device, seed)`

Test to validate mixed channels with power.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/legacy/test_resource_warnings.py -->
## PYTHON MODULE: tests/legacy/test_resource_warnings.py

### MODULE DOCSTRING

Tests for validating resource warning behavior.

### `class TestResourceWarnings()`

Contains a collection of pytest tests.

    These validate the ResourceWarning behavior of the Python NI-DAQmx API.
    

#### `def test_task_double_close(self, init_kwargs)`

Test to validate double closure of tasks.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/legacy/test_stream_analog_readers_writers.py -->
## PYTHON MODULE: tests/legacy/test_stream_analog_readers_writers.py

### MODULE DOCSTRING

Tests for validating analog read and write operation.

### `class Error(Exception)`

Base error class.

### `class NoFixtureDetectedError(Error)`

Custom error class when no fixtures are available.

### `class TestAnalogSingleChannelReaderWriter(TestDAQmxIOBase)`

Contains a collection of pytest tests.

    These validate the analog single channel stream reader and writer in the NI-DAQmx Python API.
    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    

#### `def test_one_sample(self, generate_task, real_x_series_device, seed)`

Test to validate read and write analog data .

#### `def test_many_sample(self, generate_task, real_x_series_device, seed)`

Test to validate read and write analog data .

### `class TestAnalogMultiChannelReaderWriter(TestDAQmxIOBase)`

Contains a collection of pytest tests.

    These validate the analog multi channel stream reader and writer in the NI-DAQmx Python API.
    These tests use only a single X Series device by utilizing the internal loopback routes
    on the device.
    

#### `def test_one_sample(self, generate_task, real_x_series_device, seed)`

Test to validate read and write multichannel analog data .

#### `def test_many_sample(self, generate_task, real_x_series_device, seed)`

Test to validate read and write multichannel analog data .

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/legacy/test_stream_counter_readers_writers.py -->
## PYTHON MODULE: tests/legacy/test_stream_counter_readers_writers.py

### MODULE DOCSTRING

Tests for validating counter read and write operation.

### `class TestCounterReaderWriter(TestDAQmxIOBase)`

Contains a collection of pytest tests.

    These validate the counter Read and Write functions in the NI-DAQmx Python API.
    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    

#### `def test_one_sample_uint32(self, generate_task, real_x_series_device, seed)`

Test to validate counter read and write operation with sample data .

#### `def test_multi_sample_uint32(self, generate_task, real_x_series_device, seed)`

Test to validate counter read and write operation with sample data .

#### `def test_one_sample_double(self, generate_task, real_x_series_device, seed)`

Test to validate counter read and write operation with sample data .

#### `def test_multi_sample_double(self, generate_task, real_x_series_device, seed)`

Test to validate counter read and write operation with sample data .

#### `def test_one_sample_pulse_freq(self, generate_task, real_x_series_device, seed)`

Test to validate counter read and write operation with sample data .

#### `def test_many_sample_pulse_freq(self, generate_task, real_x_series_device, seed)`

Test to validate counter read and write operation with sample data .

#### `def test_one_sample_pulse_time(self, generate_task, real_x_series_device, seed)`

Test to validate counter read and write operation with sample data .

#### `def test_many_sample_pulse_time(self, generate_task, real_x_series_device, seed)`

Test to validate counter read and write operation with sample data .

#### `def test_pulse_ticks_1_samp(self, generate_task, real_x_series_device, seed)`

Test to validate counter read and write operation with pulse ticks.

#### `def test_many_sample_pulse_ticks(self, generate_task, real_x_series_device, seed)`

Test to validate counter read and write operation with pulse ticks.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/legacy/test_stream_digital_readers_writers.py -->
## PYTHON MODULE: tests/legacy/test_stream_digital_readers_writers.py

### MODULE DOCSTRING

Tests for validating digital read and write operation.

### `class TestDigitalSingleChannelReaderWriter(TestDAQmxIOBase)`

Contains a collection of pytest tests.

    These validate the digital single channel readers and writers in the NI-DAQmx Python API.
    These tests use only a single X Series device by both writing to and reading from ONLY
    the digital output lines.
    

#### `def test_one_sample_one_line(self, task, real_x_series_device, seed)`

Test to validate digital read and write operation with sample data.

#### `def test_one_sample_multi_line(self, task, real_x_series_device, seed)`

Test to validate digital read and write operation with sample data.

#### `def test_one_sample_port_byte(self, task, real_x_series_device, seed)`

Test to validate digital read and write operation with sample port byte.

#### `def test_one_sample_port_uint16(self, task, real_x_series_device, seed)`

Test to validate digital read and write operation with sample uint16.

#### `def test_one_sample_port_uint32(self, task, real_x_series_device, seed)`

Test to validate digital read and write operation with sample uint32.

#### `def test_many_sample_port_byte(self, task, real_x_series_device, seed)`

Test to validate digital read and write operation with sample byte.

#### `def test_many_sample_port_uint16(self, task, real_x_series_device, seed)`

Test to validate digital read and write operation with sample uint16.

#### `def test_many_sample_port_uint32(self, task, real_x_series_device, seed)`

Test to validate digital read and write operation with sample uint32.

### `class TestDigitalMultiChannelReaderWriter(TestDAQmxIOBase)`

Contains a collection of pytest tests.

    These validate the digital multi channel readers and writers in the NI-DAQmx Python API.
    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    

#### `def test_one_sample_one_line(self, task, real_x_series_device, seed)`

Test to validate digital multichannel read and write operation with sample data.

#### `def test_one_sample_multi_line(self, task, real_x_series_device, seed)`

Test to validate digital multichannel read and write operation with sample data.

#### `def test_one_sample_port_byte(self, task, real_x_series_device, seed)`

Test to validate digital multichannel read and write operation with sample bytes.

#### `def test_one_sample_port_uint16(self, task, real_x_series_device, seed)`

Test to validate digital multichannel read and write operation with uint16.

#### `def test_one_sample_port_uint32(self, task, real_x_series_device, seed)`

Test to validate digital multichannel read and write operation with uint32.

#### `def test_many_sample_port_byte(self, task, real_x_series_device, seed)`

Test to validate digital multichannel read and write operation with sample bytes.

#### `def test_many_sample_port_uint16(self, task, real_x_series_device, seed)`

Test to validate digital multichannel read and write operation with uint16.

#### `def test_many_sample_port_uint32(self, task, real_x_series_device, seed)`

Test to validate digital multichannel read and write operation with uint32.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/legacy/test_stream_power_readers.py -->
## PYTHON MODULE: tests/legacy/test_stream_power_readers.py

### MODULE DOCSTRING

Tests for validating power read operation.

### `class TestPowerSingleChannelReader(TestDAQmxIOBase)`

Contains a collection of pytest tests.

    These validate power single channel stream reader in the NI-DAQmx Python API.
    These tests use simulated TestScale PPS device(s), TS-15200.
    

#### `def test_power_1_chan_1_samp(self, task, sim_ts_power_device, seed, output_enable)`

Test to validate power read operation with sample data.

#### `def test_power_1_chan_n_samp(self, task, sim_ts_power_device, seed, output_enable)`

Test to validate power read operation with sample data.

### `class TestPowerMultiChannelReader(TestDAQmxIOBase)`

Contains a collection of pytest tests.

    These validate power multi channel stream reader in the NI-DAQmx Python API.
    These tests use simulated TestScale PPS device(s), TS-15200.
    

#### `def test_power_n_chan_1_samp(self, task, sim_ts_power_devices, seed, output_enables)`

Test to validate multi channel power read operation with sample data.

#### `def test_power_n_chan_n_samp(self, task, sim_ts_power_devices, seed, output_enables)`

Test to validate multi channel power read operation with sample data.

### `class TestPowerBinaryReader(TestDAQmxIOBase)`

Contains a collection of pytest tests.

    These validate power binary stream reader in the NI-DAQmx Python API.
    These tests use simulated TestScale PPS device(s), TS-15200.
    

#### `def test_power_1_chan_n_samp_binary(self, task, sim_ts_power_device, seed, output_enable)`

Test to validate power binary read operation with sample binary data.

#### `def test_power_n_chan_many_sample_binary(self, task, sim_ts_power_devices, seed, output_enables)`

Test to validate power binary read operation with sample binary data.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/legacy/test_system_collections.py -->
## PYTHON MODULE: tests/legacy/test_system_collections.py

### MODULE DOCSTRING

Tests for validating systems collections.

### `class TestSystemCollections()`

Contains a collection of pytest tests.

    These validate the system collections functionality in the NI-DAQmx Python API.
    

#### `def test_devices_collection_property(self, system)`

Test to validate device collection property.

#### `def test_persisted_scale_collection_property(self, system)`

Test to validate persisted scale property.

#### `def test_persisted_task_collection_property(self, system)`

Test to validate persisted task collection property.

#### `def test_persisted_channel_collection_property(self, system)`

Test to validate persisted channel collection property.

#### `def test_physical_channel_collection_property(self, sim_6363_device)`

Test to validate physical channel collection property.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/legacy/test_teds.py -->
## PYTHON MODULE: tests/legacy/test_teds.py

### MODULE DOCSTRING

Tests for validating TEDS functionality.

### `class TestTEDS()`

Contains a collection of pytest tests.

    These validate the TEDS functionality in the NI-DAQmx Python API.
    

#### `def test_create_teds_ai_voltage_chan(self, task, sim_6363_device, seed, voltage_teds_file_path)`

Test to validate TEDS functionality.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/legacy/test_triggers.py -->
## PYTHON MODULE: tests/legacy/test_triggers.py

### MODULE DOCSTRING

Tests for validating trigger functionality.

### `class TestTriggers(TestDAQmxIOBase)`

Contains a collection of pytest tests.

    These validate the triggers functionality in the NI-DAQmx Python API.
    

#### `def test_arm_start_trigger(self, task, sim_6363_device, seed)`

Test to validate start trigger functionality.

#### `def test_handshake_trigger(self, task, sim_6363_device, seed)`

Test to validate trigger handshake.

#### `def test_pause_trigger(self, task, sim_6363_device, seed)`

Test to validate pause trigger.

#### `def test_reference_trigger(self, task, sim_6363_device, seed)`

Test to validate reference trigger.

#### `def test_start_trigger(self, task, sim_6363_device, seed)`

Test to validate start trigger functionality.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/legacy/test_utils.py -->
## PYTHON MODULE: tests/legacy/test_utils.py

### MODULE DOCSTRING

Tests for validating utilities functionality.

### `class TestUtils()`

Contains a collection of pytest tests.

    These validate the utilities functionality in the NI-DAQmx Python API.
    

#### `def test_basic_flatten_flatten_and_unflatten(self)`

Test to validate flatten and unflatten channel string function.

#### `def test_backwards_flatten_flatten_and_unflatten(self)`

Test to validate unflatten and flatten channel string function.

#### `def test_empty_flatten_flatten_and_unflatten(self)`

Test to validate flatten and unflatten empty channel.

#### `def test_leading_zeros_flatten_and_unflatten(self)`

Test to validate leading zeros in flatten and unflatten string function.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/legacy/test_watchdog.py -->
## PYTHON MODULE: tests/legacy/test_watchdog.py

### MODULE DOCSTRING

Tests for validating watchdog functionality.

### `class TestWatchdog()`

Contains a collection of pytest tests.

    These validate the watchdog functionality in the NI-DAQmx Python API.
    

#### `def test_watchdog_task(self, real_x_series_device, seed, generate_watchdog_task)`

Test to validate watchdog task.

#### `def test_watchdog_expir_state(self, real_x_series_device, seed, generate_watchdog_task)`

Test to validate watchdog expiration state.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/legacy/test_write_exceptions.py -->
## PYTHON MODULE: tests/legacy/test_write_exceptions.py

### MODULE DOCSTRING

Tests for validating write error behavior.

### `class TestWriteExceptions()`

Contains a collection of pytest tests.

    These validate the Write error behavior in the NI-DAQmx Python API.
    These tests use only a single X Series device by utilizing the internal
    loopback routes on the device.
    

#### `def test_overwrite(self, task, real_x_series_device)`

Test to validate overwrite functionality.

#### `def test_overwrite_during_prime(self, task, real_x_series_device)`

Test to validate overwrite functionality during prime.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/unit/__init__.py -->
## PYTHON MODULE: tests/unit/__init__.py

### MODULE DOCSTRING

Unit tests for the nidaqmx package.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/unit/_grpc_utils.py -->
## PYTHON MODULE: tests/unit/_grpc_utils.py

### MODULE DOCSTRING

gRPC helper functions.

### `def create_grpc_options(mocker: MockerFixture, session_name='') -> nidaqmx.GrpcSessionOptions`

Create a GrpcSessionOptions object.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/unit/_task_utils.py -->
## PYTHON MODULE: tests/unit/_task_utils.py

### MODULE DOCSTRING

Task helper functions.

### `def expect_create_task(interpreter: Mock, task_handle='SomeTaskHandle', new_session_initialized=True)`

Expect a call to interpreter.create_task.

### `def expect_load_task(interpreter: Mock, task_handle='SomeTaskHandle', new_session_initialized=True)`

Expect a call to interpreter.load_task.

### `def expect_get_task_name(interpreter: Mock, name: str)`

Expect a call to get the task name.

### `def register_event_handler(mocker: MockerFixture, task: Task, event_type: _TaskEventType) -> Mock`

Register a mock event handler.

### `def register_event_handlers(mocker: MockerFixture, task: Task, event_types: Iterable[_TaskEventType]) -> dict[_TaskEventType, Mock]`

Register mock event handlers and return a dictionary mapping event name -> handler.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/unit/_time_utils.py -->
## PYTHON MODULE: tests/unit/_time_utils.py

- `JAN_01_2002_TIMESTAMP_1970_EPOCH = 1009843200`

- `JAN_01_1850_TIMESTAMP_1970_EPOCH = -3786825600`

- `JAN_01_2002_TIMESTAMP_1904_EPOCH = 3092688000`

- `JAN_01_1904_TIMESTAMP_1904_EPOCH = 0`

- `JAN_01_1850_TIMESTAMP_1904_EPOCH = -1703980800`

- `JAN_01_2002_DATETIME = std_datetime(2002, 1, 1, tzinfo=timezone.utc)`

- `JAN_01_2002_HIGHTIME = ht_datetime(2002, 1, 1, tzinfo=timezone.utc)`

- `JAN_01_1904_DATETIME = std_datetime(1904, 1, 1, tzinfo=timezone.utc)`

- `JAN_01_1904_HIGHTIME = ht_datetime(1904, 1, 1, tzinfo=timezone.utc)`

- `JAN_01_1850_DATETIME = std_datetime(1850, 1, 1, tzinfo=timezone.utc)`

- `JAN_01_1850_HIGHTIME = ht_datetime(1850, 1, 1, tzinfo=timezone.utc)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/unit/conftest.py -->
## PYTHON MODULE: tests/unit/conftest.py

### MODULE DOCSTRING

Fixtures used in the DAQmx unit tests.

### `def interpreter(mocker: MockerFixture) -> Mock`

Create a mock interpreter.

### `def task(interpreter: Mock) -> Generator[Task]`

Create a DAQmx task.

    This fixture owns the task. Do not use it for test cases that destroy the task, or else you
    may get double-close warnings.
    

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/unit/system/__init__.py -->
## PYTHON MODULE: tests/unit/system/__init__.py

### MODULE DOCSTRING

Unit tests for nidaqmx.system.*.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/unit/system/storage/__init__.py -->
## PYTHON MODULE: tests/unit/system/storage/__init__.py

### MODULE DOCSTRING

Unit tests for nidaqmx.system.storage.*.

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/unit/system/storage/test_persisted_task.py -->
## PYTHON MODULE: tests/unit/system/storage/test_persisted_task.py

### `def test___persisted_task___load___specified_name_saved(interpreter: Mock)`

### `def test___persisted_task___load___load_task_called(interpreter: Mock, new_session_initialized: bool)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/unit/test_dotenv_path.py -->
## PYTHON MODULE: tests/unit/test_dotenv_path.py

### `def test___dotenv_exists_varies___has_dotenv_file___matches_dotenv_exists(dotenv_exists: bool, tmp_path: Path) -> None`

### `def test___get_caller_path___returns_this_modules_path() -> None`

### `def test___get_package_path___returns_package_dir() -> None`

### `def test___get_script_or_exe_path___returns_pytest_path() -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/unit/test_feature_toggles.py -->
## PYTHON MODULE: tests/unit/test_feature_toggles.py

- `RELEASE_FEATURE = FeatureToggle('RELEASE_FEATURE', CodeReadiness.RELEASE)`

- `NEXT_RELEASE_FEATURE = FeatureToggle('NEXT_RELEASE_FEATURE', CodeReadiness.NEXT_RELEASE)`

- `INCOMPLETE_FEATURE = FeatureToggle('INCOMPLETE_FEATURE', CodeReadiness.INCOMPLETE)`

- `PROTOTYPE_FEATURE = FeatureToggle('PROTOTYPE_FEATURE', CodeReadiness.PROTOTYPE)`

### `def _prototype_function(x: int, y: str, z: list[int]) -> str`

### `def _prototype_function_impl(x: int, y: str, z: list[int]) -> str`

### `def test___default_code_readiness_level___get_code_readiness_level___equals_prototype() -> None`

### `def test___use_release_readiness___get_code_readiness_level___equals_release() -> None`

### `def test___use_next_release_readiness___get_code_readiness_level___equals_next_release() -> None`

### `def test___default_code_readiness_level___is_enabled___returns_true() -> None`

### `def test___use_incomplete_readiness___is_enabled___reflects_code_readiness_level() -> None`

### `def test___use_next_release_readiness___is_enabled___reflects_code_readiness_level() -> None`

### `def test___release_readiness_level___is_enabled___reflects_code_readiness_level() -> None`

### `def test___feature_toggle_enabled___is_enabled___returns_true() -> None`

### `def test___feature_toggle_disabled___is_enabled___returns_false() -> None`

### `def test___feature_toggle_enabled___call_decorated_function___impl_called(mocker: MockerFixture) -> None`

### `def test___feature_toggle_disabled___call_decorated_function___error_raised(mocker: MockerFixture) -> None`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/unit/test_grpc_time.py -->
## PYTHON MODULE: tests/unit/test_grpc_time.py

### `def test___utc_datetime_after_1970___convert_to_timestamp___is_reversible(from_dt)`

### `def test___utc_datetime_before_1970___convert_to_timestamp___is_reversible(from_dt)`

### `def test___utc_datetime_after_1970___convert_to_grpc_request___succeeds(request_dt)`

### `def test___utc_datetime_before_1970___convert_to_grpc_request___succeeds(request_dt)`

### `def test___grpc_response_after_1970___convert_to_timestamp___succeeds(response_dt)`

### `def test___grpc_response_before_1970___convert_to_timestamp___succeeds(response_dt)`

### `def test___utc_datetime___convert_to_timestamp_with_dst___is_reversible(date)`

### `def test___tz_datetime_after_1970___convert_to_timestamp___is_reversible(datetime_cls, tzinfo, expected_offset)`

### `def test___tz_datetime_before_1970___convert_to_timestamp___is_reversible(datetime_cls, tzinfo, expected_offset)`

### `def test___datetime_after_1970_with_microseconds___convert_to_timestamp___is_reversible(base_dt, microsecond, nanoseconds)`

### `def test___datetime_before_1970_with_microseconds___convert_to_timestamp___is_reversible(base_dt, microsecond, nanoseconds)`

### `def test___datetime_after_1970_with_femtoseconds___convert_to_timestamp___is_reversible(base_dt, femtosecond, nanoseconds)`

### `def test___datetime_before_1970_with_femtoseconds___convert_to_timestamp___is_reversible(base_dt, femtosecond, nanoseconds)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/unit/test_lib_time.py -->
## PYTHON MODULE: tests/unit/test_lib_time.py

- `JAN_01_2002_LIB = LibTimestamp(lsb=0, msb=JAN_01_2002_TIMESTAMP_1904_EPOCH)`

- `JAN_01_1904_LIB = LibTimestamp(lsb=0, msb=JAN_01_1904_TIMESTAMP_1904_EPOCH)`

- `JAN_01_1850_LIB = LibTimestamp(lsb=0, msb=JAN_01_1850_TIMESTAMP_1904_EPOCH)`

### `def test___timestamps___sort___is_ordered()`

### `def test___utc_datetime_after_1904___convert_to_timestamp___is_reversible(from_dt)`

### `def test___utc_datetime_on_1904___convert_to_timestamp___is_reversible(from_dt)`

### `def test___utc_datetime_before_1904___convert_to_timestamp___is_reversible(from_dt)`

### `def test___utc_datetime___convert_to_timestamp_with_dst___is_reversible(date)`

### `def test___utc_datetime_with_femtoseconds___convert_to_timestamp_with_dst___is_reversible(base_dt, femtosecond, subseconds)`

### `def test___utc_datetime_with_yoctoseconds___convert_to_timestamp_with_dst___is_reversible(base_dt, yoctosecond, subseconds)`

### `def test___tz_datetime_after_1904___convert_to_timestamp___is_reversible(datetime_cls, tzinfo, expected_offset)`

### `def test___tz_datetime_before_1904___convert_to_timestamp___is_reversible(datetime_cls, tzinfo, expected_offset)`

### `def test___datetime_after_1904_with_microseconds___convert_to_timestamp___is_reversible(base_dt, microsecond, subseconds)`

### `def test___datetime_before_1904_with_microseconds___convert_to_timestamp___is_reversible(base_dt, microsecond, subseconds)`

### `def test___datetime_with_femtoseconds___convert_to_timestamp___is_reversible(base_dt, femtosecond, subseconds)`

### `def test___datetime_before_1904_with_femtoseconds___convert_to_timestamp___is_reversible(base_dt, femtosecond, subseconds)`

### `def test___datetime_after_1904_with_yoctoseconds___convert_to_timestamp___is_reversible(base_dt, yoctosecond, subseconds, yoctosecond_round_trip)`

### `def test___datetime_before_1904_with_yoctoseconds___convert_to_timestamp___is_reversible(base_dt, yoctosecond, subseconds, yoctosecond_round_trip)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/unit/test_task.py -->
## PYTHON MODULE: tests/unit/test_task.py

### `def test___init___generated_name_saved(interpreter: Mock)`

### `def test___init_with_name___specified_name_saved(interpreter: Mock)`

### `def test___init_with_grpc_options___select_interpreter_called_with_grpc_options(interpreter: Mock, mocker: MockerFixture)`

### `def test___init_with_name_and_grpc_options___specified_name_saved(interpreter: Mock, mocker: MockerFixture)`

### `def test___init_with_name_and_grpc_options_with_specified_name___specified_name_saved(interpreter: Mock, mocker: MockerFixture)`

### `def test___init_with_name_and_grpc_options_with_mismatched_name___daqerror_raised(interpreter: Mock, mocker: MockerFixture)`

### `def test___init_with_name___create_task_called(interpreter: Mock, new_session_initialized: bool)`

### `def test___call_alternate_constructor___create_task_not_called(interpreter: Mock, new_session_initialized: bool)`

### `def test___varying_close_on_exit___close___clear_task_called(interpreter: Mock, close_on_exit: bool)`

### `def test___close_on_exit___context_manager___clear_task_called(interpreter: Mock)`

### `def test___no_close_on_exit___context_manager___clear_task_not_called(interpreter: Mock)`

### `def test___close_on_exit___leak_task___raises_resource_warning(interpreter: Mock)`

### `def test___close_on_exit_with_grpc_options___leak_task___resource_warning_not_raised(interpreter: Mock, mocker: MockerFixture)`

### `def test___close_on_exit_with_alternate_constructor___leak_task___raises_resource_warning(interpreter: Mock)`

### `def test___close_on_exit_with_alternate_constructor_and_grpc_options___leak_task___resource_warning_not_raised(interpreter: Mock, mocker: MockerFixture)`

<!--NI_PYTHON_API repo=nidaqmx-python path=tests/unit/test_task_events.py -->
## PYTHON MODULE: tests/unit/test_task_events.py

### `def test___grpc_event_registered___leak_task___raises_resource_warning(event_type: _TaskEventType, interpreter: Mock, mocker: MockerFixture)`

### `def test___events_registered_and_clear_task_error_raised___close___task_resources_cleaned_up_and_clear_task_error_raised(interpreter: Mock, mocker: MockerFixture)`

### `def test___events_registered_and_close_event_handler_error_raised___close___task_resources_cleaned_up_and_close_event_handler_error_raised(event_type: _TaskEventType, interpreter: Mock, mocker: MockerFixture)`

### `def test___events_registered_and_multiple_errors_raised___close___task_resources_cleaned_up_and_first_error_raised(interpreter: Mock, mocker: MockerFixture)`

### `def _assert_task_resources_cleaned_up(task: Task, interpreter: Mock, event_handlers: dict[_TaskEventType, Mock]) -> None`
