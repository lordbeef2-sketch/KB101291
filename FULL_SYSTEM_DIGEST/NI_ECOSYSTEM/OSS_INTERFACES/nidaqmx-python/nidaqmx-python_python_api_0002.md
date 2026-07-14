# NI PYTHON API DIGEST: nidaqmx-python

<!--NI_PYTHON_API_SNAPSHOT repo=ni/nidaqmx-python commit=03282e1b5c741b9f37e4a4e1b5de3a52ae72442e -->

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/stream_readers/_digital_multi_channel_reader.py -->
## PYTHON MODULE: generated/nidaqmx/stream_readers/_digital_multi_channel_reader.py

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
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/stream_readers/_digital_single_channel_reader.py -->
## PYTHON MODULE: generated/nidaqmx/stream_readers/_digital_single_channel_reader.py

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
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/stream_readers/_power_readers.py -->
## PYTHON MODULE: generated/nidaqmx/stream_readers/_power_readers.py

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
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/stream_writers/__init__.py -->
## PYTHON MODULE: generated/nidaqmx/stream_writers/__init__.py

### MODULE DOCSTRING

NI-DAQmx stream writers.

This package provides classes for writing samples to NI-DAQmx tasks.


- `__all__ = ['AnalogSingleChannelWriter', 'AnalogMultiChannelWriter', 'AnalogUnscaledWriter', 'CounterWriter', 'DigitalSingleChannelWriter', 'DigitalMultiChannelWriter', 'UnsetAutoStartSentinel', 'AUTO_START_UNSET']`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/stream_writers/_analog_multi_channel_writer.py -->
## PYTHON MODULE: generated/nidaqmx/stream_writers/_analog_multi_channel_writer.py

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
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/stream_writers/_analog_single_channel_writer.py -->
## PYTHON MODULE: generated/nidaqmx/stream_writers/_analog_single_channel_writer.py

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
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/stream_writers/_analog_unscaled_writer.py -->
## PYTHON MODULE: generated/nidaqmx/stream_writers/_analog_unscaled_writer.py

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
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/stream_writers/_channel_writer_base.py -->
## PYTHON MODULE: generated/nidaqmx/stream_writers/_channel_writer_base.py

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

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/stream_writers/_counter_writer.py -->
## PYTHON MODULE: generated/nidaqmx/stream_writers/_counter_writer.py

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
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/stream_writers/_digital_multi_channel_writer.py -->
## PYTHON MODULE: generated/nidaqmx/stream_writers/_digital_multi_channel_writer.py

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
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/stream_writers/_digital_single_channel_writer.py -->
## PYTHON MODULE: generated/nidaqmx/stream_writers/_digital_single_channel_writer.py

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
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/system/__init__.py -->
## PYTHON MODULE: generated/nidaqmx/system/__init__.py

### MODULE DOCSTRING

NI-DAQmx system classes.

- `__all__ = ['system', 'device', 'physical_channel', 'storage', 'watchdog']`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/system/_collections/device_collection.py -->
## PYTHON MODULE: generated/nidaqmx/system/_collections/device_collection.py

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

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/system/_collections/persisted_channel_collection.py -->
## PYTHON MODULE: generated/nidaqmx/system/_collections/persisted_channel_collection.py

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

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/system/_collections/persisted_scale_collection.py -->
## PYTHON MODULE: generated/nidaqmx/system/_collections/persisted_scale_collection.py

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

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/system/_collections/persisted_task_collection.py -->
## PYTHON MODULE: generated/nidaqmx/system/_collections/persisted_task_collection.py

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

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/system/_collections/physical_channel_collection.py -->
## PYTHON MODULE: generated/nidaqmx/system/_collections/physical_channel_collection.py

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

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/system/_watchdog_modules/expiration_state.py -->
## PYTHON MODULE: generated/nidaqmx/system/_watchdog_modules/expiration_state.py

### `class ExpirationState()`


    Represents a DAQmx Watchdog expiration state.
    

#### `def __init__(self, task_handle, physical_channel, interpreter)`

#### `def __eq__(self, other)`

#### `def __hash__(self)`

#### `def __ne__(self, other)`

#### `def ao_output_type(self)`


        :class:`nidaqmx.constants.WatchdogAOExpirState`: Specifies the
            output type of the analog output physical channels when the
            watchdog task expires.
        

#### `def ao_output_type(self, val)`

#### `def ao_output_type(self)`

#### `def ao_state(self)`


        float: Specifies the state to set the analog output physical
            channels when the watchdog task expires.
        

#### `def ao_state(self, val)`

#### `def ao_state(self)`

#### `def co_state(self)`


        :class:`nidaqmx.constants.WatchdogCOExpirState`: Specifies the
            state to set the counter output channel terminal when the
            watchdog task expires.
        

#### `def co_state(self, val)`

#### `def co_state(self)`

#### `def do_state(self)`


        :class:`nidaqmx.constants.Level`: Specifies the state to which
            to set the digital physical channels when the watchdog task
            expires.  You cannot modify the expiration state of
            dedicated digital input physical channels.
        

#### `def do_state(self, val)`

#### `def do_state(self)`

#### `def expir_states_ao_type(self)`

#### `def expir_states_ao_type(self, val)`

#### `def expir_states_ao_type(self)`

#### `def expir_states_co_state(self)`

#### `def expir_states_co_state(self, val)`

#### `def expir_states_co_state(self)`

#### `def expir_states_do_state(self)`

#### `def expir_states_do_state(self, val)`

#### `def expir_states_do_state(self)`

#### `def expir_states_ao_state(self)`

#### `def expir_states_ao_state(self, val)`

#### `def expir_states_ao_state(self)`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/system/_watchdog_modules/expiration_states_collection.py -->
## PYTHON MODULE: generated/nidaqmx/system/_watchdog_modules/expiration_states_collection.py

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
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/system/device.py -->
## PYTHON MODULE: generated/nidaqmx/system/device.py

- `__all__ = ['Device']`

### `class Device()`


    Represents a DAQmx device.
    

#### `def __init__(self, name, *, grpc_options=None)`


        Args:
            name (str): Specifies the name of the device.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        

#### `def __eq__(self, other)`

#### `def __hash__(self)`

#### `def __ne__(self, other)`

#### `def __repr__(self)`

#### `def name(self)`


        str: Specifies the name of this device.
        

#### `def ai_physical_chans(self)`


        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the analog input
            physical channels available on the device.
        

#### `def ao_physical_chans(self)`


        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the analog output
            physical channels available on the device.
        

#### `def ci_physical_chans(self)`


        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the counter input
            physical channels available on the device.
        

#### `def co_physical_chans(self)`


        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the counter output
            physical channels available on the device.
        

#### `def di_lines(self)`


        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the digital input
            lines available on the device.
        

#### `def di_ports(self)`


        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the digital input
            ports available on the device.
        

#### `def do_lines(self)`


        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the digital output
            lines available on the device.
        

#### `def do_ports(self)`


        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the digital output
            ports available on the device.
        

#### `def ext_cal_last_date_and_time(self)`


        datetime: Indicates the last date and time that the device underwent an
        external calibration.
        

#### `def self_cal_last_date_and_time(self)`


        datetime: Indicates the last date and time that the device underwent a
        self-calibration.
        

#### `def device_supports_cal(self)`


        Indicates if the device supports calibration.
        

#### `def id_pin_mem_serial_nums(self)`


        List[str]: Indicates the serial number of the memory connected
            to each ID Pin. Each list element corresponds to an ID Pin.
            The list contains an empty string for each ID Pin with no
            memory connected.
        

#### `def accessory_product_nums(self)`


        List[int]: Indicates the unique hardware identification number
            for accessories connected to the device. Each list element
            corresponds to a connector. For example, index 0 corresponds
            to connector 0. The list contains 0 for each connector with
            no accessory connected.
        

#### `def accessory_product_types(self)`


        List[str]: Indicates the model names of accessories connected to
            the device. Each list element corresponds to a connector.
            For example, index 0 corresponds to connector 0. The list
            contains an empty string for each connector with no
            accessory connected.
        

#### `def accessory_serial_nums(self)`


        List[int]: Indicates the serial number for accessories connected
            to the device. Each list element corresponds to a connector.
            For example, index 0 corresponds to connector 0. The list
            contains 0 for each connector with no accessory connected.
        

#### `def ai_bridge_rngs(self)`


        List[float]: Indicates pairs of input voltage ratio ranges, in
            volts per volt, supported by devices that acquire using
            ratiometric measurements. Each pair consists of the low
            value followed by the high value.
        

#### `def ai_charge_rngs(self)`


        List[float]: Indicates in coulombs pairs of input charge ranges
            for the device. Each pair consists of the low value followed
            by the high value.
        

#### `def ai_couplings(self)`


        List[:class:`nidaqmx.constants.Coupling`]: Indicates the
            coupling types supported by this device.
        

#### `def ai_current_int_excit_discrete_vals(self)`


        List[float]: Indicates the set of discrete internal current
            excitation values supported by this device.
        

#### `def ai_current_rngs(self)`


        List[float]: Indicates the pairs of current input ranges
            supported by this device. Each pair consists of the low
            value, followed by the high value.
        

#### `def ai_dig_fltr_lowpass_cutoff_freq_discrete_vals(self)`


        List[float]: Indicates the set of discrete lowpass cutoff
            frequencies supported by this device. If the device supports
            ranges of lowpass cutoff frequencies, use
            AI.DigFltr.Lowpass.CutoffFreq.RangeVals to determine
            supported frequencies.
        

#### `def ai_dig_fltr_lowpass_cutoff_freq_range_vals(self)`


        List[float]: Indicates pairs of lowpass cutoff frequency ranges
            supported by this device. Each pair consists of the low
            value, followed by the high value. If the device supports a
            set of discrete lowpass cutoff frequencies, use
            AI.DigFltr.Lowpass.CutoffFreq.DiscreteVals to determine the
            supported frequencies.
        

#### `def ai_dig_fltr_types(self)`


        List[:class:`nidaqmx.constants.FilterType`]: Indicates the AI
            digital filter types supported by the device.
        

#### `def ai_freq_rngs(self)`


        List[float]: Indicates the pairs of frequency input ranges
            supported by this device. Each pair consists of the low
            value, followed by the high value.
        

#### `def ai_gains(self)`


        List[float]: Indicates the input gain settings supported by this
            device.
        

#### `def ai_lowpass_cutoff_freq_discrete_vals(self)`


        List[float]: Indicates the set of discrete lowpass cutoff
            frequencies supported by this device. If the device supports
            ranges of lowpass cutoff frequencies, use
            **ai_lowpass_cutoff_freq_range_vals** to determine supported
            frequencies.
        

#### `def ai_lowpass_cutoff_freq_range_vals(self)`


        List[float]: Indicates pairs of lowpass cutoff frequency ranges
            supported by this device. Each pair consists of the low
            value, followed by the high value. If the device supports a
            set of discrete lowpass cutoff frequencies, use
            **ai_lowpass_cutoff_freq_discrete_vals** to determine the
            supported  frequencies.
        

#### `def ai_max_multi_chan_rate(self)`


        float: Indicates the maximum sampling rate for an analog input
            task from this device. To find the maximum rate for the
            task, take the minimum of **ai_max_single_chan_rate** or the
            indicated sampling rate of this device divided by the number
            of channels to acquire data from (including cold-junction
            compensation and autozero channels).
        

#### `def ai_max_single_chan_rate(self)`


        float: Indicates the maximum rate for an analog input task if
            the task contains only a single channel from this device.
        

#### `def ai_meas_types(self)`


        List[:class:`nidaqmx.constants.UsageTypeAI`]: Indicates the
            measurement types supported by the physical channels of the
            device. Refer to **ai_meas_types** for information on
            specific channels.
        

#### `def ai_min_rate(self)`


        float: Indicates the minimum rate for an analog input task on
            this device. NI-DAQmx returns a warning or error if you
            attempt to sample at a slower rate.
        

#### `def ai_num_samp_timing_engines(self)`


        int: Indicates the number of Analog Input sample timing engines
            supported by the device.
        

#### `def ai_num_sync_pulse_srcs(self)`


        int: Indicates the number of Analog Input synchronization pulse
            sources supported by the device.
        

#### `def ai_resistance_rngs(self)`


        List[float]: Indicates pairs of input resistance ranges, in
            ohms, supported by devices that have the necessary signal
            conditioning to measure resistances. Each pair consists of
            the low value followed by the high value.
        

#### `def ai_samp_modes(self)`


        List[:class:`nidaqmx.constants.AcquisitionType`]: Indicates
            sample modes supported by devices that support sample
            clocked analog input.
        

#### `def ai_simultaneous_sampling_supported(self)`


        bool: Indicates if the device supports simultaneous sampling.
        

#### `def ai_trig_usage(self)`


        List[:class:`nidaqmx.constants.TriggerUsage`]: Indicates the
            triggers supported by this device for an analog input task.
        

#### `def ai_voltage_int_excit_discrete_vals(self)`


        List[float]: Indicates the set of discrete internal voltage
            excitation values supported by this device. If the device
            supports ranges of internal excitation values, use
            **ai_voltage_int_excit_range_vals** to determine supported
            excitation values.
        

#### `def ai_voltage_int_excit_range_vals(self)`


        List[float]: Indicates pairs of internal voltage excitation
            ranges supported by this device. Each pair consists of the
            low value, followed by the high value. If the device
            supports a set of discrete internal excitation values, use
            **ai_voltage_int_excit_discrete_vals** to determine the
            supported excitation values.
        

#### `def ai_voltage_rngs(self)`


        List[float]: Indicates pairs of input voltage ranges supported
            by this device. Each pair consists of the low value,
            followed by the high value.
        

#### `def anlg_trig_supported(self)`


        bool: Indicates if the device supports analog triggering.
        

#### `def ao_current_rngs(self)`


        List[float]: Indicates pairs of output current ranges supported
            by this device. Each pair consists of the low value,
            followed by the high value.
        

#### `def ao_gains(self)`


        List[float]: Indicates the output gain settings supported by
            this device.
        

#### `def ao_max_rate(self)`


        float: Indicates the maximum analog output rate of the device.
        

#### `def ao_min_rate(self)`


        float: Indicates the minimum analog output rate of the device.
        

#### `def ao_num_samp_timing_engines(self)`


        int: Indicates the number of Analog Output sample timing engines
            supported by the device.
        

#### `def ao_num_sync_pulse_srcs(self)`


        int: Indicates the number of Analog Output synchronization pulse
            sources supported by the device.
        

#### `def ao_output_types(self)`


        List[:class:`nidaqmx.constants.UsageTypeAO`]: Indicates the
            generation types supported by the physical channels of the
            device. Refer to **ao_output_types** for information on
            specific channels.
        

#### `def ao_samp_clk_supported(self)`


        bool: Indicates if the device supports the sample clock timing
            type for analog output tasks.
        

#### `def ao_samp_modes(self)`


        List[:class:`nidaqmx.constants.AcquisitionType`]: Indicates
            sample modes supported by devices that support sample
            clocked analog output.
        

#### `def ao_trig_usage(self)`


        List[:class:`nidaqmx.constants.TriggerUsage`]: Indicates the
            triggers supported by this device for analog output tasks.
        

#### `def ao_voltage_rngs(self)`


        List[float]: Indicates pairs of output voltage ranges supported
            by this device. Each pair consists of the low value,
            followed by the high value.
        

#### `def bus_type(self)`


        :class:`nidaqmx.constants.BusType`: Indicates the bus type of
            the device.
        

#### `def cal_acc_connection_count(self)`


        int: Specifies the number of times a particular connection that
            results in tangible wear and tear of onboard components has
            been made on the accessory. This connection count is useful
            for tracking accessory life and usage.
        

#### `def cal_acc_connection_count(self, val)`

#### `def cal_dev_temp(self)`


        float: Indicates in degrees Celsius the current temperature of
            the device.
        

#### `def cal_recommended_acc_connection_count_limit(self)`


        int: Indicates the recommended connection count limit for an
            accessory. If the accessory connection count exceeds this
            limit, the accessory could require maintenance.
        

#### `def cal_user_defined_info(self)`


        str: Specifies a string that contains arbitrary, user-defined
            information. This number of characters in this string can be
            no more than **cal_user_defined_info_max_size**.
        

#### `def cal_user_defined_info(self, val)`

#### `def cal_user_defined_info_max_size(self)`


        int: Indicates the maximum length in characters of
            **cal_user_defined_info**.
        

#### `def carrier_serial_num(self)`


        int: Indicates the serial number of the device carrier. This
            value is zero if the carrier does not have a serial number.
        

#### `def chassis_module_devices(self)`


        List[:class:`nidaqmx.system.device.Device`]: Indicates a list
            containing the names of the modules in the chassis.
        

#### `def ci_max_size(self)`


        int: Indicates in bits the size of the counters on the device.
        

#### `def ci_max_timebase(self)`


        float: Indicates in hertz the maximum counter timebase
            frequency.
        

#### `def ci_meas_types(self)`


        List[:class:`nidaqmx.constants.UsageTypeCI`]: Indicates the
            measurement types supported by the physical channels of the
            device. Refer to **ci_meas_types** for information on
            specific channels.
        

#### `def ci_samp_clk_supported(self)`


        bool: Indicates if the device supports the sample clock timing
            type for counter input tasks.
        

#### `def ci_samp_modes(self)`


        List[:class:`nidaqmx.constants.AcquisitionType`]: Indicates
            sample modes supported by devices that support sample
            clocked counter input.
        

#### `def ci_trig_usage(self)`


        List[:class:`nidaqmx.constants.TriggerUsage`]: Indicates the
            triggers supported by this device for counter input tasks.
        

#### `def co_max_size(self)`


        int: Indicates in bits the size of the counters on the device.
        

#### `def co_max_timebase(self)`


        float: Indicates in hertz the maximum counter timebase
            frequency.
        

#### `def co_output_types(self)`


        List[:class:`nidaqmx.constants.UsageTypeCO`]: Indicates the
            generation types supported by the physical channels of the
            device. Refer to **co_output_types** for information on
            specific channels.
        

#### `def co_samp_clk_supported(self)`


        bool: Indicates if the device supports Sample Clock timing for
            counter output tasks.
        

#### `def co_samp_modes(self)`


        List[:class:`nidaqmx.constants.AcquisitionType`]: Indicates
            sample modes supported by devices that support sample
            clocked counter output.
        

#### `def co_trig_usage(self)`


        List[:class:`nidaqmx.constants.TriggerUsage`]: Indicates the
            triggers supported by this device for counter output tasks.
        

#### `def compact_daq_chassis_device(self)`


        :class:`nidaqmx.system.device.Device`: Indicates the name of the
            CompactDAQ chassis that contains this module.
        

#### `def compact_daq_slot_num(self)`


        int: Indicates the slot number in which this module is located
            in the CompactDAQ chassis.
        

#### `def compact_rio_chassis_device(self)`


        :class:`nidaqmx.system.device.Device`: Indicates the name of the
            CompactRIO chassis that contains this module.
        

#### `def compact_rio_slot_num(self)`


        int: Indicates the slot number of the CompactRIO chassis where
            this module is located.
        

#### `def di_max_rate(self)`


        float: Indicates the maximum digital input rate of the device.
        

#### `def di_num_samp_timing_engines(self)`


        int: Indicates the number of Digital Input sample timing engines
            supported by the device.
        

#### `def di_trig_usage(self)`


        List[:class:`nidaqmx.constants.TriggerUsage`]: Indicates the
            triggers supported by this device for digital input tasks.
        

#### `def dig_trig_supported(self)`


        bool: Indicates if the device supports digital triggering.
        

#### `def do_max_rate(self)`


        float: Indicates the maximum digital output rate of the device.
        

#### `def do_num_samp_timing_engines(self)`


        int: Indicates the number of Digital Output synchronization
            pulse sources supported by the device.
        

#### `def do_trig_usage(self)`


        List[:class:`nidaqmx.constants.TriggerUsage`]: Indicates the
            triggers supported by this device for digital output tasks.
        

#### `def ext_cal_last_temp(self)`


        float: Indicates in degrees Celsius the temperature of the
            device at the time of the last external calibration. Compare
            this temperature to the current onboard temperature to
            determine if you should perform another calibration.
        

#### `def ext_cal_recommended_interval(self)`


        int: Indicates in months the National Instruments recommended
            interval between each external calibration of the device.
        

#### `def field_daq_bank_devices(self)`


        List[:class:`nidaqmx.system.device.Device`]: Indicates a list
            containing the names of the banks in the FieldDAQ.
        

#### `def field_daq_device(self)`


        :class:`nidaqmx.system.device.Device`: Indicates the parent
            device which this bank is located in.
        

#### `def hwteds_supported(self)`


        bool: Indicates whether the device supports hardware TEDS.
        

#### `def id_pin_mem_family_codes(self)`


        List[int]: Indicates the family code of the memory connected to
            each ID Pin. Each list element corresponds to an ID Pin. The
            list contains 0 for each ID Pin with no memory connected.
        

#### `def id_pin_mem_sizes(self)`


        List[int]: Indicates the size in bytes of the memory connected
            to each ID Pin. Each list element corresponds to an ID Pin.
            The list contains 0 for each ID Pin with no memory
            connected.
        

#### `def id_pin_pin_names(self)`


        List[str]: Indicates the names of all the ID Pins on this
            device.
        

#### `def id_pin_pin_statuses(self)`


        List[:class:`nidaqmx.constants.IDPinStatus`]: Indicates status
            of each ID Pin.
        

#### `def is_simulated(self)`


        bool: Indicates if the device is a simulated device.
        

#### `def num_dma_chans(self)`


        int: Indicates the number of DMA channels on the device.
        

#### `def num_time_trigs(self)`


        int: Indicates the number of time triggers available on the
            device.
        

#### `def num_timestamp_engines(self)`


        int: Indicates the number of timestamp engines available on the
            device.
        

#### `def pci_bus_num(self)`


        int: Indicates the PCI bus number of the device.
        

#### `def pci_dev_num(self)`


        int: Indicates the PCI slot number of the device.
        

#### `def product_category(self)`


        :class:`nidaqmx.constants.ProductCategory`: Indicates the
            product category of the device. This category corresponds to
            the category displayed in MAX when creating NI-DAQmx
            simulated devices.
        

#### `def product_num(self)`


        int: Indicates the unique hardware identification number for the
            device.
        

#### `def product_type(self)`


        str: Indicates the product name of the device.
        

#### `def pxi_chassis_num(self)`


        int: Indicates the PXI chassis number of the device, as
            identified in MAX.
        

#### `def pxi_slot_num(self)`


        int: Indicates the PXI slot number of the device.
        

#### `def self_cal_last_temp(self)`


        float: Indicates in degrees Celsius the temperature of the
            device at the time of the last self-calibration. Compare
            this temperature to the current onboard temperature to
            determine if you should perform another calibration.
        

#### `def self_cal_supported(self)`


        bool: Indicates whether the device supports self-calibration.
        

#### `def serial_num(self)`


        int: Indicates the serial number of the device. This value is
            zero if the device does not have a serial number.
        

#### `def tcpip_ethernet_ip(self)`


        str: Indicates the IPv4 address of the Ethernet interface in
            dotted decimal format. This property returns 0.0.0.0 if the
            Ethernet interface cannot acquire an address.
        

#### `def tcpip_hostname(self)`


        str: Indicates the IPv4 hostname of the device.
        

#### `def tcpip_wireless_ip(self)`


        str: Indicates the IPv4 address of the 802.11 wireless interface
            in dotted decimal format. This property returns 0.0.0.0 if
            the wireless interface cannot acquire an address.
        

#### `def terminals(self)`


        List[str]: Indicates a list of all terminals on the device.
        

#### `def time_trig_supported(self)`


        bool: Indicates whether the device supports time triggering.
        

#### `def dev_is_simulated(self)`

#### `def dev_serial_num(self)`

#### `def tedshwteds_supported(self)`

#### `def reset_device(self)`


        Immediately aborts all active tasks associated with a device,
        disconnects any routes, and returns the device to an initialized
        state. Aborting a task immediately terminates the currently
        active operation, such as a read or a write. Aborting a task
        puts the task into an unstable but recoverable state. To recover
        the task, use DAQmx Start to restart the task or use DAQmx Stop
        to reset the task without starting it.
        

#### `def restore_last_ext_cal_const(self)`


        Sets the self-calibration constants of the device to the
        external calibration constants. NI sets the external calibration
        constants at the factory, and those constants remain in effect
        until you perform a new external calibration on the device.
        

#### `def self_cal(self)`


        Measures the onboard reference voltage of the device and adjusts
        the self-calibration constants to account for any errors caused
        by short-term fluctuations in the operating environment. When
        you self-calibrate a device, no external signal connections are
        necessary.
        

#### `def self_test_device(self)`


        Performs a brief test of device resources. If a failure occurs,
        refer to your device documentation for more information.
        

#### `def write_id_pin_memory(self, id_pin_name, data, format_code)`


        Writes the supplied data and format code to the EEPROM connected
        to the specified ID pin.

        Args:
            id_pin_name (str): Is the name of the ID Pin to access (ex:
                id0)
            data (List[int]): Is the 1D list of 8-bit unsigned integers
                to write to the memory
            format_code (int): Specifies the type and structure of the
                data being written. User to define the meaning of the
                format code.
        

#### `def read_id_pin_memory(self, id_pin_name)`


        Reads and returns the data stored in the memory attached to the
        specified ID Pin.

        Args:
            id_pin_name (str): Is the name of the ID Pin to access (ex:
                id0)

        Returns:
            nidaqmx.types.IDPinContents:

            Contains the data read from the memory and the format code.
        

#### `def add_network_device(ip_address, device_name='', attempt_reservation=False, timeout=10.0, *, grpc_options=None)`


        Adds a Network cDAQ device to the system and, if specified,
        attempts to reserve it.

        Args:
            ip_address (str): Specifies the string containing the IP
                address (in dotted decimal notation) or hostname of the
                device to add to the system.
            device_name (Optional[str]): Indicates the name to assign to
                the device. If unspecified, NI-DAQmx chooses the device
                name.
            attempt_reservation (Optional[bool]): Indicates if a
                reservation should be attempted after the device is
                successfully added. By default, this parameter is set to
                False.
            timeout (Optional[float]): Specifies the time in seconds to
                wait for the device to respond before timing out.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        Returns:
            nidaqmx.system.device.Device:

            Specifies the object that represents the device this
            operation applied to.
        

#### `def delete_network_device(self)`


        Deletes a Network DAQ device previously added to the host. If
        the device is reserved, it is unreserved before it is removed.
        

#### `def reserve_network_device(self, override_reservation=None)`


        Reserves the Network DAQ device for the current host.
        Reservation is required to run NI-DAQmx tasks, and the device
        must be added in MAX before it can be reserved.

        Args:
            override_reservation (Optional[bool]): Indicates if an
                existing reservation on the device should be overridden
                by this reservation. By default, this parameter is set
                to false.
        

#### `def unreserve_network_device(self)`


        Unreserves or releases a Network DAQ device previously reserved
        by the host.
        

### `class _DeviceAlternateConstructor(Device)`


    Provide an alternate constructor for the Device object.

    This is a private API used to instantiate a Device with an existing interpreter.
    

#### `def __init__(self, name, interpreter)`


        Args:
            name: Specifies the name of the Device.
            interpreter: Specifies the interpreter instance.

        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/system/physical_channel.py -->
## PYTHON MODULE: generated/nidaqmx/system/physical_channel.py

- `__all__ = ['PhysicalChannel']`

### `class PhysicalChannel()`


    Represents a DAQmx physical channel.
    

#### `def __init__(self, name, *, grpc_options=None)`


        Args:
            name (str): Specifies the name of the physical channel.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        

#### `def __eq__(self, other)`

#### `def __hash__(self)`

#### `def __ne__(self, other)`

#### `def __repr__(self)`

#### `def name(self)`


        str: Specifies the name of this physical channel.
        

#### `def ai_input_srcs(self)`


        List[str]: Indicates the list of input sources supported by the
            channel. Channels may support using the signal from the I/O
            connector or one of several calibration signals.
        

#### `def ai_meas_types(self)`


        List[:class:`nidaqmx.constants.UsageTypeAI`]: Indicates the
            measurement types supported by the channel.
        

#### `def ai_power_control_enable(self)`


        bool: Specifies whether to turn on the sensor's power supply.
        

#### `def ai_power_control_enable(self, val)`

#### `def ai_power_control_enable(self)`

#### `def ai_power_control_type(self)`


        :class:`nidaqmx.constants.SensorPowerType`: Specifies the type
            of power supplied to the sensor.
        

#### `def ai_power_control_type(self, val)`

#### `def ai_power_control_type(self)`

#### `def ai_power_control_voltage(self)`


        float: Specifies the voltage level for the sensor's power
            supply.
        

#### `def ai_power_control_voltage(self, val)`

#### `def ai_power_control_voltage(self)`

#### `def ai_sensor_power_open_chan(self)`


        bool: Indicates whether there is an open channel or undercurrent
            condition on the channel.
        

#### `def ai_sensor_power_overcurrent(self)`


        bool: Indicates whether there is an overcurrent condition on the
            channel.
        

#### `def ai_sensor_power_types(self)`


        List[:class:`nidaqmx.constants.SensorPowerType`]: Indicates the
            types of power supplied to the sensor supported by this
            channel.
        

#### `def ai_sensor_power_voltage_range_vals(self)`


        List[float]: Indicates pairs of sensor power voltage ranges
            supported by this channel. Each pair consists of the low
            value followed by the high value.
        

#### `def ai_term_cfgs(self)`


        List[:class:`nidaqmx.constants.TerminalConfiguration`]:
            Indicates the list of terminal configurations supported by
            the channel.
        

#### `def ao_manual_control_amplitude(self)`


        float: Indicates the current value of the front panel amplitude
            control for the physical channel in volts.
        

#### `def ao_manual_control_enable(self)`


        bool: Specifies if you can control the physical channel
            externally via a manual control located on the device. You
            cannot simultaneously control a channel manually and with
            NI-DAQmx.
        

#### `def ao_manual_control_enable(self, val)`

#### `def ao_manual_control_enable(self)`

#### `def ao_manual_control_freq(self)`


        float: Indicates the current value of the front panel frequency
            control for the physical channel in hertz.
        

#### `def ao_manual_control_short_detected(self)`


        bool: Indicates whether the physical channel is currently
            disabled due to a short detected on the channel.
        

#### `def ao_output_types(self)`


        List[:class:`nidaqmx.constants.UsageTypeAO`]: Indicates the
            output types supported by the channel.
        

#### `def ao_power_amp_channel_enable(self)`


        bool: Specifies whether to enable or disable a channel for
            amplification. This property can also be used to check if a
            channel is enabled.
        

#### `def ao_power_amp_channel_enable(self, val)`

#### `def ao_power_amp_channel_enable(self)`

#### `def ao_power_amp_gain(self)`


        float: Indicates the calibrated gain of the channel.
        

#### `def ao_power_amp_offset(self)`


        float: Indicates the calibrated offset of the channel in volts.
        

#### `def ao_power_amp_overcurrent(self)`


        bool: Indicates if the channel detected an overcurrent
            condition.
        

#### `def ao_power_amp_scaling_coeff(self)`


        List[float]: Indicates the coefficients of a polynomial equation
            used to scale from pre-amplified values.
        

#### `def ao_supported_power_up_output_types(self)`


        List[:class:`nidaqmx.constants.AOPowerUpOutputBehavior`]:
            Indicates the power up output types supported by the
            channel.
        

#### `def ao_term_cfgs(self)`


        List[:class:`nidaqmx.constants.TerminalConfiguration`]:
            Indicates the list of terminal configurations supported by
            the channel.
        

#### `def ci_meas_types(self)`


        List[:class:`nidaqmx.constants.UsageTypeCI`]: Indicates the
            measurement types supported by the channel.
        

#### `def co_output_types(self)`


        List[:class:`nidaqmx.constants.UsageTypeCO`]: Indicates the
            output types supported by the channel.
        

#### `def di_change_detect_supported(self)`


        bool: Indicates if the change detection timing type is supported
            for the digital input physical channel.
        

#### `def di_port_width(self)`


        int: Indicates in bits the width of digital input port.
        

#### `def di_samp_clk_supported(self)`


        bool: Indicates if the sample clock timing type is supported for
            the digital input physical channel.
        

#### `def di_samp_modes(self)`


        List[:class:`nidaqmx.constants.AcquisitionType`]: Indicates the
            sample modes supported by devices that support sample
            clocked digital input.
        

#### `def dig_port_logic_family(self)`


        :class:`nidaqmx.constants.LogicFamily`: Specifies the digital
            port logic family to use for acquisition and generation. A
            logic family corresponds to voltage thresholds that are
            compatible with a group of voltage standards. Refer to the
            device documentation for information on the logic high and
            logic low voltages for these logic families.
        

#### `def dig_port_logic_family(self, val)`

#### `def dig_port_logic_family(self)`

#### `def do_port_width(self)`


        int: Indicates in bits the width of digital output port.
        

#### `def do_samp_clk_supported(self)`


        bool: Indicates if the sample clock timing type is supported for
            the digital output physical channel.
        

#### `def do_samp_modes(self)`


        List[:class:`nidaqmx.constants.AcquisitionType`]: Indicates the
            sample modes supported by devices that support sample
            clocked digital output.
        

#### `def teds_bit_stream(self)`


        List[int]: Indicates the TEDS binary bitstream without
            checksums.
        

#### `def teds_mfg_id(self)`


        int: Indicates the manufacturer ID of the sensor.
        

#### `def teds_model_num(self)`


        int: Indicates the model number of the sensor.
        

#### `def teds_serial_num(self)`


        int: Indicates the serial number of the sensor.
        

#### `def teds_template_ids(self)`


        List[int]: Indicates the IDs of the templates in the bitstream
            in **teds_bit_stream**.
        

#### `def teds_version_letter(self)`


        str: Indicates the version letter of the sensor.
        

#### `def teds_version_num(self)`


        int: Indicates the version number of the sensor.
        

#### `def clear_teds(self)`


        Removes TEDS information from the physical channel you specify.
        This function temporarily overrides any TEDS configuration for
        the physical channel that you performed in MAX.
        

#### `def configure_teds(self, file_path: str | pathlib.PurePath | None=None)`


        Associates TEDS information with the physical channel you
        specify. If you do not specify the filename of a data sheet in
        the **file_path** input, this function attempts to find a TEDS
        sensor connected to the physical channel. This function
        temporarily overrides any TEDS configuration for the physical
        channel that you performed in MAX.

        Args:
            file_path: Is the path to a Virtual TEDS data sheet that
                you want to associate with the physical channel. If you
                do not specify anything for this input, this function
                attempts to find a TEDS sensor connected to the physical
                channel.
        

#### `def write_to_teds_from_array(self, bit_stream=None, basic_teds_options=WriteBasicTEDSOptions.DO_NOT_WRITE)`


        Writes data from a 1D list of 8-bit unsigned integers to the
        TEDS sensor.

        Args:
            bit_stream (Optional[List[int]]): Is the TEDS bitstream to
                write to the sensor. This bitstream must be constructed
                according to the IEEE 1451.4 specification.
            basic_teds_options (Optional[nidaqmx.constants.WriteBasicTEDSOptions]): 
                Specifies how to handle basic TEDS data in the
                bitstream.
        

#### `def write_to_teds_from_file(self, file_path: str | pathlib.PurePath | None=None, basic_teds_options=WriteBasicTEDSOptions.DO_NOT_WRITE)`


        Writes data from a virtual TEDS file to the TEDS sensor.

        Args:
            file_path: Specifies the filename of a virtual TEDS file
                that contains the bitstream to write.
            basic_teds_options (Optional[nidaqmx.constants.WriteBasicTEDSOptions]): 
                Specifies how to handle basic TEDS data in the
                bitstream.
        

### `class _PhysicalChannelAlternateConstructor(PhysicalChannel)`


    Provide an alternate constructor for the PhysicalChannel object.

    This is a private API used to instantiate a PhysicalChannel with an existing interpreter.
    

#### `def __init__(self, name, interpreter)`


        Args:
            name: Specifies the name of the Physical Channel.
            interpreter: Specifies the interpreter instance.

        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/system/storage/__init__.py -->
## PYTHON MODULE: generated/nidaqmx/system/storage/__init__.py

### MODULE DOCSTRING

NI-DAQmx storage classes.

- `__all__ = ['persisted_channel', 'persisted_scale', 'persisted_task']`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/system/storage/persisted_channel.py -->
## PYTHON MODULE: generated/nidaqmx/system/storage/persisted_channel.py

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

        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/system/storage/persisted_scale.py -->
## PYTHON MODULE: generated/nidaqmx/system/storage/persisted_scale.py

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

        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/system/storage/persisted_task.py -->
## PYTHON MODULE: generated/nidaqmx/system/storage/persisted_task.py

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

        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/system/system.py -->
## PYTHON MODULE: generated/nidaqmx/system/system.py

- `__all__ = ['System']`

### `class System()`


    Represents a DAQmx system.

    Contains static properties that access tasks, scales, and global channels
    stored in Measurement Automation Explorer (MAX), performs immediate
    operations on DAQ hardware, and creates classes from which you can get
    information about the hardware.
    

#### `def __init__(self, grpc_options=None)`


        Args:
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        

#### `def local()`


        nidaqmx.system.system.System: Represents the local DAQmx system.
        

#### `def remote(grpc_options)`


        nidaqmx.system.system.System: Represents the remote DAQmx system.

        Args:
            grpc_options (:class:`~nidaqmx.GrpcSessionOptions`): Specifies
                the gRPC session options.
        

#### `def devices(self)`


        nidaqmx.system._collections.DeviceCollection: Indicates the
            collection of devices for this DAQmx system.
        

#### `def driver_version(self)`


        collections.namedtuple: Indicates the major, minor and update
            portions of the installed version of NI-DAQmx.

            - major_version (int): Indicates the major portion of the
              installed version of NI-DAQmx, such as 7 for version 7.0.
            - minor_version (int): Indicates the minor portion of the
              installed version of NI-DAQmx, such as 0 for version 7.0.
            - update_version (int): Indicates the update portion of the
              installed version of NI-DAQmx, such as 1 for version 9.0.1.
        

#### `def global_channels(self)`


        nidaqmx.system._collections.PersistedChannelCollection: Indicates
            the collection of global channels for this DAQmx system.
        

#### `def scales(self)`


        nidaqmx.system._collections.PersistedScaleCollection: Indicates
            the collection of custom scales for this DAQmx system.
        

#### `def tasks(self)`


        nidaqmx.system._collections.PersistedTaskCollection: Indicates
            the collection of saved tasks for this DAQmx system.
        

#### `def _major_version(self)`


        int: Indicates the major portion of the installed version of NI-
            DAQmx, such as 7 for version 7.0.
        

#### `def _minor_version(self)`


        int: Indicates the minor portion of the installed version of NI-
            DAQmx, such as 0 for version 7.0.
        

#### `def _update_version(self)`


        int: Indicates the update portion of the installed version of
            NI-DAQmx, such as 1 for version 9.0.1.
        

#### `def connect_terms(self, source_terminal, destination_terminal, signal_modifiers=SignalModifiers.DO_NOT_INVERT_POLARITY)`


        Creates a route between a source and destination terminal. The
        route can carry a variety of digital signals, such as triggers,
        clocks, and hardware events.

        Args:
            source_terminal (str): Specifies the originating terminal of
                the route. A DAQmx terminal constant lists all terminals
                available on devices installed in the system. You also
                can specify a source terminal by specifying a string
                that contains a terminal name.
            destination_terminal (str): Specifies the receiving terminal
                of the route. A DAQmx terminal constant provides a list
                of all terminals available on devices installed in the
                system. You also can specify a destination terminal by
                specifying a string that contains a terminal name.
            signal_modifiers (Optional[nidaqmx.constants.SignalModifiers]): 
                Specifies whether to invert the signal this function
                routes from the source terminal to the destination
                terminal.
        

#### `def disconnect_terms(self, source_terminal, destination_terminal)`


        Removes signal routes you created by using the DAQmx Connect
        Terminals function. The DAQmx Disconnect Terminals function
        cannot remove task-based routes, such as those you create
        through timing and triggering configuration.

        Args:
            source_terminal (str): Specifies the originating terminal of
                the route. A DAQmx terminal constant lists all terminals
                available on devices installed in the system. You also
                can specify a source terminal by specifying a string
                that contains a terminal name.
            destination_terminal (str): Specifies the receiving terminal
                of the route. A DAQmx terminal constant provides a list
                of all terminals available on devices installed in the
                system. You also can specify a destination terminal by
                specifying a string that contains a terminal name.
        

#### `def tristate_output_term(self, output_terminal)`


        Sets a terminal to high-impedance state. If you connect an
        external signal to a terminal on the I/O connector, the terminal
        must be in high-impedance state. Otherwise, the device could
        double-drive the terminal and damage the hardware. If you use
        this function on a terminal in an active route, the function
        fails and returns an error.

        Args:
            output_terminal (str): Specifies the terminal on the I/O
                connector to set to high-impedance state. A DAQmx
                terminal constant lists all available terminals on
                installed devices. You also can specify an output
                terminal by using a string that contains a terminal
                name.
        

#### `def set_digital_power_up_states(self, device_name, power_up_states)`


        Updates power up states for digital physical channels.

        Args:
            device_name (str): Specifies the name as configured in MAX
                of the device to which this operation applies.
            power_up_states (List[nidaqmx.types.DOPowerUpState]):
                Contains the physical channels and power up states to
                set. Each element of the list contains a physical channel
                and the power up state to set for that physical channel.

                - physical_channel (str): Specifies the digital line or
                  port to modify. You cannot modify dedicated digital
                  input lines.
                - power_up_state (:class:`nidaqmx.constants.PowerUpStates`):
                  Specifies the power up state to set for the physical
                  channel specified with the **physical_channel** input.
        

#### `def get_digital_power_up_states(self, device_name)`


        Gets the power up states for digital physical lines.

        Args:
            device_name (str): Specifies the name as configured in MAX
                of the device to which this operation applies.
        Returns:
            List[nidaqmx.types.DOPowerUpState]:

            Contains the physical channels and power up states set. Each
            element of the list contains a physical channel and the power
            up state set for that physical channel.

            - physical_channel (str): Indicates the physical channel that
              was modified.
            - power_up_state (:class:`nidaqmx.constants.PowerUpStates`):
              Indicates the power up state set for the physical channel
              specified with the **physical_channel** output.
        

#### `def set_digital_pull_up_pull_down_states(self, device_name, power_up_states)`


        Sets the resistor level to pull up or pull down for lines when
        they are in tristate logic.

        Args:
            device_name (str): Specifies the name as configured in MAX
                of the device to which this operation applies.
            power_up_states (List[nidaqmx.types.DOResistorPowerUpState]):
                Contains the physical channels and power up states to
                set. Each element of the list contains a physical channel
                and the power up state to set for that physical channel.

                - physical_channel (str): Specifies the digital line or
                  port to modify.  You cannot modify dedicated digital
                  input lines.
                - power_up_state (:class:`nidaqmx.constants.ResistorState`):
                  Specifies the power up state to set for the physical
                  channel specified with the **physical_channel** input.
        

#### `def get_digital_pull_up_pull_down_states(self, device_name)`


        Gets the resistor level for lines when they are in tristate
        logic.

        Args:
            device_name (str): Specifies the name as configured in MAX
                of the device to which this operation applies.
        Returns:
            List[nidaqmx.types.DOResistorPowerUpState]:

            Contains the physical channels and power up states set. Each
            element of the list contains a physical channel and the power
            up state set for that physical channel.

            - physical_channel (str): Indicates the physical channel that
              was modified.
            - power_up_state (:class:`nidaqmx.constants.ResistorState`):
              Indicates the power up state set for the physical channel
              specified with the **physical_channel** output.
        

#### `def set_analog_power_up_states(self, device_name, power_up_states)`


        Updates power up states for analog physical channels.

        Args:
            device_name (str): Specifies the name as configured in MAX
                of the device to which this operation applies.
            power_up_states (List[nidaqmx.types.AOPowerUpState]):
                Contains the physical channels and power up states to
                set. Each element of the list contains a physical channel
                and the power up state to set for that physical channel.

                - physical_channel (str): Specifies the physical channel
                  to modify.
                - power_up_state (float): Specifies the power up state to
                  set for the physical channel specified with the
                  **physical_channel** input.
                - channel_type (:class:`nidaqmx.constants.AOPowerUpOutputBehavior`):
                  Specifies the output type for the physical channel
                  specified with the **physical_channel** input.
        

#### `def set_analog_power_up_states_with_output_type(self, power_up_states)`


        Updates power up states for analog physical channels.

        Args:
            power_up_states (List[nidaqmx.types.AOPowerUpState]):
                Contains the physical channels and power up states to
                set. Each element of the list contains a physical channel
                and the power up state to set for that physical channel.

                - physical_channel (str): Specifies the physical channel to
                  modify.
                - power_up_state (float): Specifies the power up state
                  to set for the physical channel specified with the
                  **physical_channel** input.
                - channel_type (:class:`nidaqmx.constants.AOPowerUpOutputBehavior`):
                  Specifies the output type for the physical channel
                  specified with the **physical_channel** input.
        

#### `def get_analog_power_up_states(self, device_name)`


        Gets the power up states for analog physical channels.

        Args:
            device_name (str): Specifies the name as configured in MAX
                of the device to which this operation applies.
        Returns:
            power_up_states (List[nidaqmx.types.AOPowerUpState]):

            Contains the physical channels and power up states set. Each
            element of the list contains a physical channel and the
            power up state set for that physical channel.

            - physical_channel (str): Specifies the physical channel that
              was modified.
            - power_up_state (float): Specifies the power up state set
              for the physical channel specified with the
              **physical_channel** input.
            - channel_type (:class:`nidaqmx.constants.AOPowerUpOutputBehavior`):
              Specifies the output type for the physical channel
              specified with the **physical_channel** input.
        

#### `def get_analog_power_up_states_with_output_type(self, physical_channels)`


        Gets the power up states for analog physical channels.

        Args:
            physical_channels (List[str]): Indicates the physical
                channels that were modified.
        Returns:
            power_up_states (List[nidaqmx.types.AOPowerUpState]):

            Contains the physical channels and power up states set. Each
            element of the list contains a physical channel and the
            power up state set for that physical channel.

            - physical_channel (str): Specifies the physical channel that
              was modified.
            - power_up_state (float): Specifies the power up state set
              for the physical channel specified with the
              **physical_channel** input.
            - channel_type (:class:`nidaqmx.constants.AOPowerUpOutputBehavior`):
              Specifies the output type for the physical channel
              specified with the **physical_channel** input.
        

#### `def set_digital_logic_family_power_up_state(self, device_name, logic_family)`


        Sets the digital logic family to use when the device powers up.

        Args:
            device_name (str): Specifies the name as configured in MAX
                of the device to which this operation applies.
            logic_family (nidaqmx.constants.LogicFamily): Specifies the
                logic family set to the device to when it powers up. A
                logic family corresponds to voltage thresholds that are
                compatible with a group of voltage standards. Refer to
                device documentation for information on the logic high
                and logic low voltages for these logic families.
        

#### `def get_digital_logic_family_power_up_state(self, device_name)`


        Gets the digital logic family for a device.

        Args:
            device_name (str): Specifies the name as configured in MAX
                of the device to which this operation applies.
        Returns:
            nidaqmx.constants.LogicFamily:

            Specifies the logic family to set the device to when it powers
            up. A logic family corresponds to voltage thresholds that are
            compatible with a group of voltage standards. Refer to device
            documentation for information on the logic high and logic low
            voltages for these logic families.
        

#### `def auto_configure_cdaq_sync_connections(self, chassis_devices_ports='', timeout=WAIT_INFINITELY)`


        Detects and configures cDAQ Sync connections between devices.
        Stop all NI-DAQmx tasks running on the devices prior to running
        this function because any running tasks cause auto-configuration
        to fail.

        Args:
            chassis_devices_ports (Optional[str]): Specifies the names of the
                CompactDAQ chassis, C Series modules, or cDAQ Sync ports in
                comma separated form to search. If no names are specified, all
                cDAQ Sync ports on connected, non-simulated devices are
                scanned.
            timeout (Optional[float]): Specifies the time in seconds to
                wait for the device to respond before timing out. If a
                timeout occurs, no configuration is changed.
        Returns:
            List[nidaqmx.types.CDAQSyncConnection]:

            Returns the configured port-to-port connections.
        

#### `def are_configured_cdaq_sync_ports_disconnected(self, chassis_devices_ports='', timeout=WAIT_INFINITELY)`


        Verifies configured cDAQ Sync connections between devices.
        Failures generally indicate a wiring issue or that a device has
        been powered off or removed. Stop all NI-DAQmx tasks running on
        the devices prior to running this function because any running
        tasks cause the verification process to fail.

        Args:
            chassis_devices_ports (Optional[str]): Specifies the names
                of the CompactDAQ chassis, C Series modules, or cDAQ
                Sync ports in comma separated form to search. If no
                names are specified, all cDAQ Sync ports on connected,
                non-simulated devices are scanned.
            timeout (Optional[float]): Specifies the time in seconds to
                wait for the device to respond before timing out.
        Returns:
            List[nidaqmx.types.CDAQSyncConnection]:

            Returns the port-to-port connections that failed verification.
        

#### `def add_cdaq_sync_connection(self, ports_to_connect)`


        Adds a cDAQ Sync connection between devices. The connection is
        not verified.

        Args:
            ports_to_connect (nidaqmx.types.CDAQSyncConnection):
                Specifies the cDAQ Sync ports to connect.
        

#### `def remove_cdaq_sync_connection(self, ports_to_disconnect)`


        Removes a cDAQ Sync connection between devices. The connection
        is not verified.

        Args:
            ports_to_disconnect (nidaqmx.types.CDAQSyncConnection):
                Specifies the cDAQ Sync ports to disconnect.
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/system/watchdog.py -->
## PYTHON MODULE: generated/nidaqmx/system/watchdog.py

- `__all__ = ['WatchdogTask']`

### `class WatchdogTask()`


    Represents the watchdog configurations for a DAQmx task.
    

#### `def __init__(self, device_name, task_name='', timeout=10, grpc_options=None)`


        Creates and configures a task that controls the watchdog timer of a
        device. The timer activates when you start the task.

        Use the DAQmx Configure Watchdog Expiration States functions to
        configure channel expiration states. This class does not program
        the watchdog timer on a real-time controller.

        Args:
            device_name (str): Specifies is the name as configured in MAX of
                the device to which this operation applies.
            task_name (str): Specifies the name to assign to the task. If you
                use this constructor in a loop and specify a name for the task,
                you must use the DAQmx Clear Task method within the loop after
                you are finished with the task. Otherwise, NI-DAQmx attempts to
                create multiple tasks with the same name, which results in an
                error.
            timeout (float): Specifies the amount of time in seconds until the
                watchdog timer expires. A value of -1 means the internal timer
                never expires. Set this input to -1 if you use an Expiration
                Trigger to expire the watchdog task. If this time elapses, the
                device sets the physical channels to the states you specify
                with the digital physical channel expiration states input.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        

#### `def __del__(self)`

#### `def __enter__(self)`

#### `def __exit__(self, type, value, traceback)`

#### `def expiration_states(self)`


        :class:`nidaqmx.system._watchdog_modules.expiration_states_collection.ExpirationStatesCollection`: Gets
            the collection of expiration states for this watchdog task.
        

#### `def expir_trig_dig_edge_edge(self)`


        :class:`nidaqmx.constants.Edge`: Specifies on which edge of a
            digital signal to expire the watchdog task.
        

#### `def expir_trig_dig_edge_edge(self, val)`

#### `def expir_trig_dig_edge_edge(self)`

#### `def expir_trig_dig_edge_src(self)`


        str: Specifies the name of a terminal where a digital signal
            exists to use as the source of the Expiration Trigger.
        

#### `def expir_trig_dig_edge_src(self, val)`

#### `def expir_trig_dig_edge_src(self)`

#### `def expir_trig_trig_on_network_conn_loss(self)`


        bool: Specifies the watchdog timer behavior when the network
            connection is lost between the host and the chassis. If set
            to true, the watchdog timer expires when the chassis detects
            the loss of network connection.
        

#### `def expir_trig_trig_on_network_conn_loss(self, val)`

#### `def expir_trig_trig_on_network_conn_loss(self)`

#### `def expir_trig_trig_type(self)`


        :class:`nidaqmx.constants.TriggerType`: Specifies the type of
            trigger to use to expire a watchdog task.
        

#### `def expir_trig_trig_type(self, val)`

#### `def expir_trig_trig_type(self)`

#### `def expired(self)`


        bool: Indicates if the watchdog timer expired. You can read this
            property only while the task is running.
        

#### `def timeout(self)`


        float: Specifies in seconds the amount of time until the
            watchdog timer expires. A value of -1 means the internal
            timer never expires. Set this input to -1 if you use an
            Expiration Trigger to expire the watchdog task.
        

#### `def timeout(self, val)`

#### `def timeout(self)`

#### `def name(self)`


        str: Indicates the name of the task.
        

#### `def _control_watchdog_task(self, action)`


        Controls the watchdog timer task according to the action you
        specify. This function does not program the watchdog timer on a
        real-time controller. Use the Real-Time Watchdog VIs to program
        the watchdog timer on a real-time controller.

        Args:
            action (nidaqmx.constants.WDTTaskAction): Specifies how to
                control the watchdog timer task.
        

#### `def cfg_watchdog_ao_expir_states(self, expiration_states)`


        Configures the expiration states for an analog watchdog timer task.

        Args:
            expiration_states
                (List[nidaqmx.system.watchdog.AOExpirationState]):
                Contains the states to which to set analog physical channels
                when the watchdog timer expires. Each element of the list
                contains an analog physical channel name, the corresponding
                expiration state, and the output type for that analog
                physical channel. The units of "expiration state" must be
                specified in volts for an analog output voltage expiration
                state, or amps for an analog output current expiration state.

                physical_channel (str): Specifies the analog output channel to
                    modify. You cannot modify dedicated analog input lines.
                expiration_state (float): Specifies the value to set the
                    channel to upon expiration.
                output_type (nidaqmx.constants.WatchdogAOExpirState):
                    Specifies the output type of the physical channel.
        Returns:
            List[nidaqmx.system._watchdog_modules.expiration_state.ExpirationState]:

            Indicates the list of objects representing the configured
            expiration states.
        

#### `def cfg_watchdog_co_expir_states(self, expiration_states)`


        Configures the expiration states for a counter watchdog timer task.

        Args:
            expiration_states
                (List[nidaqmx.system.watchdog.COExpirationState]):
                Contains the states to which to set counter physical channels
                when the watchdog timer expires. Each element of the list
                contains a counter physical channel name and the corresponding
                state for that counter physical channel.

                physical_channel (str): Specifies the counter output channel to
                    modify. You cannot modify dedicated counter input lines.
                expiration_state (nidaqmx.constants.WatchdogCOExpirState):
                    Specifies the value to set the channel to upon expiration.
        Returns:
            List[nidaqmx.system._watchdog_modules.expiration_state.ExpirationState]:

            Indicates the list of objects representing the configured
            expiration states.
        

#### `def cfg_watchdog_do_expir_states(self, expiration_states)`


        Configures the expiration states for a digital watchdog timer task.

        Args:
            expiration_states
                (List[nidaqmx.system.watchdog.DOExpirationState]):
                Contains the states to which to set digital physical channels
                when the watchdog timer expires. Each element of the list
                contains a digital physical channel name and the corresponding
                state for that digital physical channel.

                physical_channel (str): Specifies the digital output channel to
                    modify. You cannot modify dedicated digital input lines.
                expiration_state (nidaqmx.constants.Level): Specifies the
                    value to set the channel to upon expiration.
        Returns:
            List[nidaqmx.system._watchdog_modules.expiration_state.ExpirationState]:

            Indicates the list of objects representing the configured
            expiration states.
        

#### `def clear_expiration(self)`


        Unlock a device whose watchdog timer expired.

        This function does not program the watchdog timer on a real-time
        controller. Use the Real-Time Watchdog VIs to program the watchdog
        timer on a real-time controller.
        

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
        

#### `def reset_timer(self)`


        Reset the internal timer. You must continually reset the internal
        timer to prevent it from timing out and locking the device.

        This function does not program the watchdog timer on a real-time
        controller. Use the Real-Time Watchdog VIs to program the watchdog
        timer on a real-time controller.
        

#### `def start(self)`


        Transitions the task to the running state to begin the measurement
        or generation. Using this method is required for some applications and
        is optional for others.
        

#### `def stop(self)`


        Stops the task and returns it to the state the task was in before the
        DAQmx Start Task method ran.
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/__init__.py -->
## PYTHON MODULE: generated/nidaqmx/task/__init__.py

### MODULE DOCSTRING

NI-DAQmx task and related classes.

- `__all__ = ['Task', 'InStream', 'OutStream', 'ExportSignals', 'Timing']`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/_export_signals.py -->
## PYTHON MODULE: generated/nidaqmx/task/_export_signals.py

### `class ExportSignals()`


    Represents the exported signal configurations for a DAQmx task.
    

#### `def __init__(self, task_handle, interpreter)`

#### `def adv_cmplt_event_delay(self)`


        float: Specifies the output signal delay in periods of the
            sample clock.
        

#### `def adv_cmplt_event_delay(self, val)`

#### `def adv_cmplt_event_delay(self)`

#### `def adv_cmplt_event_output_term(self)`


        str: Specifies the terminal to which to route the Advance
            Complete Event.
        

#### `def adv_cmplt_event_output_term(self, val)`

#### `def adv_cmplt_event_output_term(self)`

#### `def adv_cmplt_event_pulse_polarity(self)`


        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            the exported Advance Complete Event.
        

#### `def adv_cmplt_event_pulse_polarity(self, val)`

#### `def adv_cmplt_event_pulse_polarity(self)`

#### `def adv_cmplt_event_pulse_width(self)`


        float: Specifies the width of the exported Advance Complete
            Event pulse.
        

#### `def adv_cmplt_event_pulse_width(self, val)`

#### `def adv_cmplt_event_pulse_width(self)`

#### `def adv_trig_output_term(self)`


        str: Specifies the terminal to which to route the Advance
            Trigger.
        

#### `def adv_trig_output_term(self, val)`

#### `def adv_trig_output_term(self)`

#### `def adv_trig_pulse_polarity(self)`


        :class:`nidaqmx.constants.Polarity`: Indicates the polarity of
            the exported Advance Trigger.
        

#### `def adv_trig_pulse_width(self)`


        float: Specifies the width of an exported Advance Trigger pulse.
            Specify this value in the units you specify with
            **adv_trig_pulse_width_units**.
        

#### `def adv_trig_pulse_width(self, val)`

#### `def adv_trig_pulse_width(self)`

#### `def adv_trig_pulse_width_units(self)`


        :class:`nidaqmx.constants.DigitalWidthUnits`: Specifies the
            units of **adv_trig_pulse_width**.
        

#### `def adv_trig_pulse_width_units(self, val)`

#### `def adv_trig_pulse_width_units(self)`

#### `def ai_conv_clk_output_term(self)`


        str: Specifies the terminal to which to route the AI Convert
            Clock.
        

#### `def ai_conv_clk_output_term(self, val)`

#### `def ai_conv_clk_output_term(self)`

#### `def ai_conv_clk_pulse_polarity(self)`


        :class:`nidaqmx.constants.Polarity`: Indicates the polarity of
            the exported AI Convert Clock. The polarity is fixed and
            independent of the active edge of the source of the AI
            Convert Clock.
        

#### `def ai_hold_cmplt_event_output_term(self)`


        str: Specifies the terminal to which to route the AI Hold
            Complete Event.
        

#### `def ai_hold_cmplt_event_output_term(self, val)`

#### `def ai_hold_cmplt_event_output_term(self)`

#### `def ai_hold_cmplt_event_pulse_polarity(self)`


        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            an exported AI Hold Complete Event pulse.
        

#### `def ai_hold_cmplt_event_pulse_polarity(self, val)`

#### `def ai_hold_cmplt_event_pulse_polarity(self)`

#### `def change_detect_event_output_term(self)`


        str: Specifies the terminal to which to route the Change
            Detection Event.
        

#### `def change_detect_event_output_term(self, val)`

#### `def change_detect_event_output_term(self)`

#### `def change_detect_event_pulse_polarity(self)`


        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            an exported Change Detection Event pulse.
        

#### `def change_detect_event_pulse_polarity(self, val)`

#### `def change_detect_event_pulse_polarity(self)`

#### `def ctr_out_event_output_behavior(self)`


        :class:`nidaqmx.constants.ExportAction`: Specifies whether the
            exported Counter Output Event pulses or changes from one
            state to the other when the counter reaches terminal count.
        

#### `def ctr_out_event_output_behavior(self, val)`

#### `def ctr_out_event_output_behavior(self)`

#### `def ctr_out_event_output_term(self)`


        str: Specifies the terminal to which to route the Counter Output
            Event.
        

#### `def ctr_out_event_output_term(self, val)`

#### `def ctr_out_event_output_term(self)`

#### `def ctr_out_event_pulse_polarity(self)`


        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            the pulses at the output terminal of the counter when
            **ctr_out_event_output_behavior** is
            **ExportActions2.PULSE**. NI-DAQmx ignores this property if
            **ctr_out_event_output_behavior** is
            **ExportActions2.TOGGLE**.
        

#### `def ctr_out_event_pulse_polarity(self, val)`

#### `def ctr_out_event_pulse_polarity(self)`

#### `def ctr_out_event_toggle_idle_state(self)`


        :class:`nidaqmx.constants.Level`: Specifies the initial state of
            the output terminal of the counter when
            **ctr_out_event_output_behavior** is
            **ExportActions2.TOGGLE**. The terminal enters this state
            when NI-DAQmx commits the task.
        

#### `def ctr_out_event_toggle_idle_state(self, val)`

#### `def ctr_out_event_toggle_idle_state(self)`

#### `def data_active_event_lvl_active_lvl(self)`


        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            the exported Data Active Event.
        

#### `def data_active_event_lvl_active_lvl(self, val)`

#### `def data_active_event_lvl_active_lvl(self)`

#### `def data_active_event_output_term(self)`


        str: Specifies the terminal to which to export the Data Active
            Event.
        

#### `def data_active_event_output_term(self, val)`

#### `def data_active_event_output_term(self)`

#### `def divided_samp_clk_timebase_output_term(self)`


        str: Specifies the terminal to which to route the Divided Sample
            Clock Timebase.
        

#### `def divided_samp_clk_timebase_output_term(self, val)`

#### `def divided_samp_clk_timebase_output_term(self)`

#### `def exported_10_mhz_ref_clk_output_term(self)`


        str: Specifies the terminal to which to route the 10MHz Clock.
        

#### `def exported_10_mhz_ref_clk_output_term(self, val)`

#### `def exported_10_mhz_ref_clk_output_term(self)`

#### `def exported_20_mhz_timebase_output_term(self)`


        str: Specifies the terminal to which to route the 20MHz
            Timebase.
        

#### `def exported_20_mhz_timebase_output_term(self, val)`

#### `def exported_20_mhz_timebase_output_term(self)`

#### `def hshk_event_delay(self)`


        float: Specifies the number of seconds to delay after the
            Handshake Trigger deasserts before asserting the Handshake
            Event.
        

#### `def hshk_event_delay(self, val)`

#### `def hshk_event_delay(self)`

#### `def hshk_event_interlocked_assert_on_start(self)`


        bool: Specifies to assert the Handshake Event when the task
            starts if **hshk_event_output_behavior** is
            **ExportActions5.INTERLOCKED**.
        

#### `def hshk_event_interlocked_assert_on_start(self, val)`

#### `def hshk_event_interlocked_assert_on_start(self)`

#### `def hshk_event_interlocked_asserted_lvl(self)`


        :class:`nidaqmx.constants.Level`: Specifies the asserted level
            of the exported Handshake Event if
            **hshk_event_output_behavior** is
            **ExportActions5.INTERLOCKED**.
        

#### `def hshk_event_interlocked_asserted_lvl(self, val)`

#### `def hshk_event_interlocked_asserted_lvl(self)`

#### `def hshk_event_interlocked_deassert_delay(self)`


        float: Specifies in seconds the amount of time to wait after the
            Handshake Trigger asserts before deasserting the Handshake
            Event if **hshk_event_output_behavior** is
            **ExportActions5.INTERLOCKED**.
        

#### `def hshk_event_interlocked_deassert_delay(self, val)`

#### `def hshk_event_interlocked_deassert_delay(self)`

#### `def hshk_event_output_behavior(self)`


        :class:`nidaqmx.constants.ExportAction`: Specifies the output
            behavior of the Handshake Event.
        

#### `def hshk_event_output_behavior(self, val)`

#### `def hshk_event_output_behavior(self)`

#### `def hshk_event_output_term(self)`


        str: Specifies the terminal to which to route the Handshake
            Event.
        

#### `def hshk_event_output_term(self, val)`

#### `def hshk_event_output_term(self)`

#### `def hshk_event_pulse_polarity(self)`


        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            the exported Handshake Event if
            **hshk_event_output_behavior** is **ExportActions5.PULSE**.
        

#### `def hshk_event_pulse_polarity(self, val)`

#### `def hshk_event_pulse_polarity(self)`

#### `def hshk_event_pulse_width(self)`


        float: Specifies in seconds the pulse width of the exported
            Handshake Event if **hshk_event_output_behavior** is
            **ExportActions5.PULSE**.
        

#### `def hshk_event_pulse_width(self, val)`

#### `def hshk_event_pulse_width(self)`

#### `def pause_trig_lvl_active_lvl(self)`


        :class:`nidaqmx.constants.Polarity`: Specifies the active level
            of the exported Pause Trigger.
        

#### `def pause_trig_lvl_active_lvl(self, val)`

#### `def pause_trig_lvl_active_lvl(self)`

#### `def pause_trig_output_term(self)`


        str: Specifies the terminal to which to route the Pause Trigger.
        

#### `def pause_trig_output_term(self, val)`

#### `def pause_trig_output_term(self)`

#### `def rdy_for_start_event_lvl_active_lvl(self)`


        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            the exported Ready for Start Event.
        

#### `def rdy_for_start_event_lvl_active_lvl(self, val)`

#### `def rdy_for_start_event_lvl_active_lvl(self)`

#### `def rdy_for_start_event_output_term(self)`


        str: Specifies the terminal to which to route the Ready for
            Start Event.
        

#### `def rdy_for_start_event_output_term(self, val)`

#### `def rdy_for_start_event_output_term(self)`

#### `def rdy_for_xfer_event_deassert_cond(self)`


        :class:`nidaqmx.constants.DeassertCondition`: Specifies when the
            ready for transfer event deasserts.
        

#### `def rdy_for_xfer_event_deassert_cond(self, val)`

#### `def rdy_for_xfer_event_deassert_cond(self)`

#### `def rdy_for_xfer_event_deassert_cond_custom_threshold(self)`


        int: Specifies in samples the threshold below which the Ready
            for Transfer Event deasserts. This threshold is an amount of
            space available in the onboard memory of the device.
            **rdy_for_xfer_event_deassert_cond** must be
            **DeassertCondition.ONBOARD_MEMORY_CUSTOM_THRESHOLD** to use
            a custom threshold.
        

#### `def rdy_for_xfer_event_deassert_cond_custom_threshold(self, val)`

#### `def rdy_for_xfer_event_deassert_cond_custom_threshold(self)`

#### `def rdy_for_xfer_event_lvl_active_lvl(self)`


        :class:`nidaqmx.constants.Polarity`: Specifies the active level
            of the exported Ready for Transfer Event.
        

#### `def rdy_for_xfer_event_lvl_active_lvl(self, val)`

#### `def rdy_for_xfer_event_lvl_active_lvl(self)`

#### `def rdy_for_xfer_event_output_term(self)`


        str: Specifies the terminal to which to route the Ready for
            Transfer Event.
        

#### `def rdy_for_xfer_event_output_term(self, val)`

#### `def rdy_for_xfer_event_output_term(self)`

#### `def ref_trig_output_term(self)`


        str: Specifies the terminal to which to route the Reference
            Trigger.
        

#### `def ref_trig_output_term(self, val)`

#### `def ref_trig_output_term(self)`

#### `def ref_trig_pulse_polarity(self)`


        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            the exported Reference Trigger.
        

#### `def ref_trig_pulse_polarity(self, val)`

#### `def ref_trig_pulse_polarity(self)`

#### `def samp_clk_delay_offset(self)`


        float: Specifies in seconds the amount of time to offset the
            exported Sample clock.  Refer to timing diagrams for
            generation applications in the device documentation for more
            information about this value.
        

#### `def samp_clk_delay_offset(self, val)`

#### `def samp_clk_delay_offset(self)`

#### `def samp_clk_output_behavior(self)`


        :class:`nidaqmx.constants.ExportAction`: Specifies whether the
            exported Sample Clock issues a pulse at the beginning of a
            sample or changes to a high state for the duration of the
            sample.
        

#### `def samp_clk_output_behavior(self, val)`

#### `def samp_clk_output_behavior(self)`

#### `def samp_clk_output_term(self)`


        str: Specifies the terminal to which to route the Sample Clock.
        

#### `def samp_clk_output_term(self, val)`

#### `def samp_clk_output_term(self)`

#### `def samp_clk_pulse_polarity(self)`


        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            the exported Sample Clock if **samp_clk_output_behavior** is
            **ExportActions3.PULSE**.
        

#### `def samp_clk_pulse_polarity(self, val)`

#### `def samp_clk_pulse_polarity(self)`

#### `def samp_clk_timebase_output_term(self)`


        str: Specifies the terminal to which to route the Sample Clock
            Timebase.
        

#### `def samp_clk_timebase_output_term(self, val)`

#### `def samp_clk_timebase_output_term(self)`

#### `def start_trig_output_term(self)`


        str: Specifies the terminal to which to route the Start Trigger.
        

#### `def start_trig_output_term(self, val)`

#### `def start_trig_output_term(self)`

#### `def start_trig_pulse_polarity(self)`


        :class:`nidaqmx.constants.Polarity`: Specifies the polarity of
            the exported Start Trigger.
        

#### `def start_trig_pulse_polarity(self, val)`

#### `def start_trig_pulse_polarity(self)`

#### `def sync_pulse_event_output_term(self)`


        str: Specifies the terminal to which to route the
            Synchronization Pulse Event.
        

#### `def sync_pulse_event_output_term(self, val)`

#### `def sync_pulse_event_output_term(self)`

#### `def watchdog_expired_event_output_term(self)`


        str: Specifies the terminal  to which to route the Watchdog
            Timer Expired Event.
        

#### `def watchdog_expired_event_output_term(self, val)`

#### `def watchdog_expired_event_output_term(self)`

#### `def export_signal(self, signal_id, output_terminal)`


        Routes a control signal to the terminal you specify. The output
        terminal can reside on the device that generates the control
        signal or on a different device. You can use this function to
        share clocks and triggers among multiple tasks and devices. The
        routes this function creates are task-based routes.

        Args:
            signal_id (nidaqmx.constants.Signal): Is the name of the
                trigger, clock, or event to export.
            output_terminal (str): Is the destination of the exported
                signal. A DAQmx terminal constant lists all terminals on
                installed devices. You can also specify a string
                containing a comma-delimited list of terminal names.
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/_in_stream.py -->
## PYTHON MODULE: generated/nidaqmx/task/_in_stream.py

### `class InStream()`


    Exposes an input data stream on a DAQmx task.

    The input data stream be used to control reading behavior and can be
    used in conjunction with reader classes to read samples from an
    NI-DAQmx task.
    

#### `def __init__(self, task, interpreter)`

#### `def __eq__(self, other)`

#### `def __hash__(self)`

#### `def __ne__(self, other)`

#### `def __repr__(self)`

#### `def timeout(self)`


        float: Specifies the amount of time in seconds to wait for
            samples to become available. If the time elapses, the read
            method returns an error and any samples read before the
            timeout elapsed. The default timeout is 10 seconds. If you
            set timeout to nidaqmx.WAIT_INFINITELY, the read method
            waits indefinitely. If you set timeout to 0, the read method
            tries once to read the requested samples and returns an error
            if it is unable to.
        

#### `def timeout(self, val)`

#### `def timeout(self)`

#### `def accessory_insertion_or_removal_detected(self)`


        bool: Indicates if any device(s) in the task detected the
            insertion or removal of an accessory since the task started.
            Reading this property clears the accessory change status for
            all channels in the task. You must read this property before
            you read **devs_with_inserted_or_removed_accessories**.
            Otherwise, you will receive an error.
        

#### `def auto_start(self)`


        bool: Specifies if DAQmx Read automatically starts the task  if
            you did not start the task explicitly by using DAQmx Start.
            The default value is True. When  DAQmx Read starts a finite
            acquisition task, it also stops the task after reading the
            last sample.
        

#### `def auto_start(self, val)`

#### `def auto_start(self)`

#### `def aux_power_error_chans(self)`


        List[str]: Indicates a list of names of any virtual channels in
            the task for which an auxiliary power supply error condition
            has been detected. You must read the Aux Power Error
            Channels Exist property before you read this property.
            Otherwise, you will receive an error.
        

#### `def aux_power_error_chans_exist(self)`


        bool: Indicates if the device(s) detected an auxiliary power
            supply error condition for any channel in the task. Reading
            this property clears the error condition status for all
            channels in the task. You must read this property before you
            read the Aux Power Error Channels property. Otherwise, you
            will receive an error.
        

#### `def avail_samp_per_chan(self)`


        int: Indicates the number of samples available to read per
            channel. This value is the same for all channels in the
            task.
        

#### `def change_detect_overflowed(self)`


        bool: Indicates if samples were missed because change detection
            events occurred faster than the device could handle them.
            Some devices detect overflows differently than others.
        

#### `def channels_to_read(self)`


        :class:`nidaqmx.task.channels.Channel`: Specifies a subset of
            channels in the task from which to read.
        

#### `def channels_to_read(self, val)`

#### `def channels_to_read(self)`

#### `def common_mode_range_error_chans(self)`


        List[str]: Indicates a list of names of any virtual channels in
            the task for which the device(s) detected a common mode
            range violation. You must read
            **common_mode_range_error_chans_exist** before you read this
            property. Otherwise, you will receive an error.
        

#### `def common_mode_range_error_chans_exist(self)`


        bool: Indicates if the device(s) detected a common mode range
            violation for any virtual channel in the task. Common mode
            range violation occurs when the voltage of either the
            positive terminal or negative terminal to ground are out of
            range. Reading this property clears the common mode range
            violation status for all channels in the task. You must read
            this property before you read
            **common_mode_range_error_chans**. Otherwise, you will
            receive an error.
        

#### `def curr_read_pos(self)`


        int: Indicates in samples per channel the current position in
            the buffer.
        

#### `def devs_with_inserted_or_removed_accessories(self)`


        List[str]: Indicates the names of any devices that detected the
            insertion or removal of an accessory since the task started.
            You must read **accessory_insertion_or_removal_detected**
            before you read this property. Otherwise, you will receive
            an error.
        

#### `def di_num_booleans_per_chan(self)`


        int: Indicates the number of booleans per channel that NI-DAQmx
            returns in a sample for line-based reads. If a channel has
            fewer lines than this number, the extra booleans are False.
        

#### `def excit_fault_chans(self)`


        List[str]: Indicates a list of names of any virtual channels in
            the task for which the device(s) detected an excitation
            fault condition. You must read **excit_fault_chans_exist**
            before you read this property. Otherwise, you will receive
            an error.
        

#### `def excit_fault_chans_exist(self)`


        bool: Indicates if the device(s) detected an excitation fault
            condition for any virtual channel in the task. Reading this
            property clears the excitation fault status for all channels
            in the task. You must read this property before you read
            **excit_fault_chans**. Otherwise, you will receive an error.
        

#### `def input_buf_size(self)`


        int: Specifies the number of samples the input buffer can hold
            for each channel in the task. Zero indicates to allocate no
            buffer. Use a buffer size of 0 to perform a hardware-timed
            operation without using a buffer. Setting this property
            overrides the automatic input buffer allocation that NI-
            DAQmx performs.
        

#### `def input_buf_size(self, val)`

#### `def input_buf_size(self)`

#### `def input_limits_fault_chans(self)`


        List[str]: Indicates the virtual channels that have detected
            samples outside the upper or lower limits configured for
            each channel in the task. You must read
            **input_limits_fault_chans_exist** before you read this
            property. Otherwise, you will receive an error.
        

#### `def input_limits_fault_chans_exist(self)`


        bool: Indicates if the device or devices detected a sample that
            was outside the upper or lower limits configured for each
            channel in the task. Reading this property clears the input
            limits fault channel status for all channels in the task.
            You must read this property before you read
            **input_limits_fault_chans**. Otherwise, you will receive an
            error. Note: Fault detection applies to both positive and
            negative inputs. For instance, if you specify a lower limit
            of 2 mA and an upper limit of 12 mA, NI-DAQmx detects a
            fault at 15 mA and -15 mA, but not at -6 mA because it is in
            the range of -12 mA to -2 mA.
        

#### `def input_onbrd_buf_size(self)`


        int: Indicates in samples per channel the size of the onboard
            input buffer of the device.
        

#### `def logging_file_path(self) -> pathlib.Path | None`


        pathlib.Path: Specifies the path to the TDMS file to which you
            want to log data.  If the file path is changed while the
            task is running, this takes effect on the next sample
            interval (if Logging.SampsPerFile has been set) or when
            DAQmx Start New File is called. New file paths can be
            specified by ending with "\" or "/". Files created after
            specifying a new file path retain the same name and
            numbering sequence.
        

#### `def logging_file_path(self, val: str | pathlib.PurePath | None)`

#### `def logging_file_path(self)`

#### `def logging_file_preallocation_size(self)`


        int: Specifies a size in samples to be used to pre-allocate
            space on disk.  Pre-allocation can improve file I/O
            performance, especially in situations where multiple files
            are being written to disk.  For finite tasks, the default
            behavior is to pre-allocate the file based on the number of
            samples you configure the task to acquire.
        

#### `def logging_file_preallocation_size(self, val)`

#### `def logging_file_preallocation_size(self)`

#### `def logging_file_write_size(self)`


        int: Specifies the size, in samples, in which data will be
            written to disk.  The size must be evenly divisible by the
            volume sector size, in bytes.
        

#### `def logging_file_write_size(self, val)`

#### `def logging_file_write_size(self)`

#### `def logging_mode(self)`


        :class:`nidaqmx.constants.LoggingMode`: Specifies whether to
            enable logging and whether to allow reading data while
            logging. Log mode allows for the best performance. However,
            you cannot read data while logging if you specify this mode.
            If you want to read data while logging, specify Log and Read
            mode.
        

#### `def logging_mode(self, val)`

#### `def logging_mode(self)`

#### `def logging_pause(self)`


        bool: Specifies whether logging is paused while a task is
            executing. If **logging_mode** is set to Log and Read mode,
            this value is taken into consideration on the next call to
            DAQmx Read, where data is written to disk. If
            **logging_mode** is set to Log Only mode, this value is
            taken into consideration the next time that data is written
            to disk. A new TDMS group is written when logging is resumed
            from a paused state.
        

#### `def logging_pause(self, val)`

#### `def logging_pause(self)`

#### `def logging_samps_per_file(self)`


        int: Specifies how many samples to write to each file. When the
            file reaches the number of samples specified, a new file is
            created with the naming convention of <filename>_####.tdms,
            where #### starts at 0001 and increments automatically with
            each new file. For example, if the file specified is
            C:\data.tdms, the next file name used is
            C:\data_0001.tdms. To disable file spanning behavior, set
            this attribute to 0. If **logging_file_path** is changed
            while this attribute is set, the new file path takes effect
            on the next file created.
        

#### `def logging_samps_per_file(self, val)`

#### `def logging_samps_per_file(self)`

#### `def logging_tdms_group_name(self)`


        str: Specifies the name of the group to create within the TDMS
            file for data from this task. If you append data to an
            existing file and the specified group already exists, NI-
            DAQmx appends a number symbol and a number to the group
            name, incrementing that number until finding a group name
            that does not exist. For example, if you specify a group
            name of Voltage Task, and that group already exists, NI-
            DAQmx assigns the group name Voltage Task #1, then Voltage
            Task #2.
        

#### `def logging_tdms_group_name(self, val)`

#### `def logging_tdms_group_name(self)`

#### `def logging_tdms_operation(self)`


        :class:`nidaqmx.constants.LoggingOperation`: Specifies how to
            open the TDMS file.
        

#### `def logging_tdms_operation(self, val)`

#### `def logging_tdms_operation(self)`

#### `def num_chans(self)`


        int: Indicates the number of channels that DAQmx Read reads from
            the task. This value is the number of channels in the task
            or the number of channels you specify with
            **channels_to_read**.
        

#### `def offset(self)`


        int: Specifies an offset in samples per channel at which to
            begin a read operation. This offset is relative to the
            location you specify with **relative_to**.
        

#### `def offset(self, val)`

#### `def offset(self)`

#### `def open_chans(self)`


        List[str]: Indicates a list of names of any open virtual
            channels. You must read **open_chans_exist** before you read
            this property. Otherwise you will receive an error.
        

#### `def open_chans_details(self)`


        List[str]: Indicates a list of details of any open virtual
            channels. You must read **open_chans_exist** before you read
            this property. Otherwise you will receive an error.
        

#### `def open_chans_exist(self)`


        bool: Indicates if the device or devices detected an open
            channel condition in any virtual channel in the task.
            Reading this property clears the open channel status for all
            channels in this task. You must read this property before
            you read **open_chans**. Otherwise, you will receive an
            error.
        

#### `def open_current_loop_chans(self)`


        List[str]: Indicates a list of names of any virtual channels in
            the task for which the device(s) detected an open current
            loop. You must read **open_current_loop_chans_exist** before
            you read this property. Otherwise, you will receive an
            error.
        

#### `def open_current_loop_chans_exist(self)`


        bool: Indicates if the device(s) detected an open current loop
            for any virtual channel in the task. Reading this property
            clears the open current loop status for all channels in the
            task. You must read this property before you read
            **open_current_loop_chans**. Otherwise, you will receive an
            error.
        

#### `def open_thrmcpl_chans(self)`


        List[str]: Indicates a list of names of any virtual channels in
            the task for which the device(s) detected an open
            thermocouple. You must read **open_thrmcpl_chans_exist**
            before you read this property. Otherwise, you will receive
            an error.
        

#### `def open_thrmcpl_chans_exist(self)`


        bool: Indicates if the device(s) detected an open thermocouple
            connected to any virtual channel in the task. Reading this
            property clears the open thermocouple status for all
            channels in the task. You must read this property before you
            read **open_thrmcpl_chans**. Otherwise, you will receive an
            error.
        

#### `def overcurrent_chans(self)`


        List[str]: Indicates a list of names of any virtual channels in
            the task for which the device(s) detected an overcurrent
            condition. You must read **overcurrent_chans_exist** before
            you read this property. Otherwise, you will receive an
            error. On some devices, you must restart the task for all
            overcurrent channels to recover.
        

#### `def overcurrent_chans_exist(self)`


        bool: Indicates if the device(s) detected an overcurrent
            condition for any virtual channel in the task. Reading this
            property clears the overcurrent status for all channels in
            the task. You must read this property before you read
            **overcurrent_chans**. Otherwise, you will receive an error.
        

#### `def overloaded_chans(self)`


        List[str]: Indicates a list of names of any overloaded virtual
            channels in the task. You must read
            **overloaded_chans_exist** before you read this property.
            Otherwise, you will receive an error.
        

#### `def overloaded_chans_exist(self)`


        bool: Indicates if the device(s) detected an overload in any
            virtual channel in the task. Reading this property clears
            the overload status for all channels in the task. You must
            read this property before you read **overloaded_chans**.
            Otherwise, you will receive an error.
        

#### `def overtemperature_chans(self)`


        List[str]: Indicates a list of names of any overtemperature
            virtual channels. You must read
            **overtemperature_chans_exist** before you read this
            property. Otherwise, you will receive an error.
        

#### `def overtemperature_chans_exist(self)`


        bool: Indicates if the device(s) detected an overtemperature
            condition in any virtual channel in the task. Reading this
            property clears the overtemperature status for all channels
            in the task. You must read this property before you read
            **overtemperature_chans**. Otherwise, you will receive an
            error.
        

#### `def overwrite(self)`


        :class:`nidaqmx.constants.OverwriteMode`: Specifies whether to
            overwrite samples in the buffer that you have not yet read.
        

#### `def overwrite(self, val)`

#### `def overwrite(self)`

#### `def pll_unlocked_chans(self)`


        List[str]: Indicates the channels that had their PLLs unlock.
        

#### `def pll_unlocked_chans_exist(self)`


        bool: Indicates whether the PLL is currently locked, or whether
            it became unlocked during the previous acquisition. Devices
            may report PLL Unlock either during acquisition or after
            acquisition.
        

#### `def power_supply_fault_chans(self)`


        List[str]: Indicates the virtual channels that have detected a
            power supply fault. You must read
            **power_supply_fault_chans_exist** before you read this
            property. Otherwise, you will receive an error.
        

#### `def power_supply_fault_chans_exist(self)`


        bool: Indicates if the device or devices detected a power supply
            fault condition in any virtual channel in the task. Reading
            this property clears the power supply fault status for all
            channels in this task. You must read this property before
            you read **power_supply_fault_chans**. Otherwise, you will
            receive an error.
        

#### `def raw_data_width(self)`


        int: Indicates in bytes the size of a raw sample from the task.
        

#### `def read_all_avail_samp(self)`


        bool: Specifies whether subsequent read operations read all
            samples currently available in the buffer or wait for the
            buffer to become full before reading. NI-DAQmx uses this
            setting for finite acquisitions and only when the number of
            samples to read is -1. For continuous acquisitions when the
            number of samples to read is -1, a read operation always
            reads all samples currently available in the buffer.
        

#### `def read_all_avail_samp(self, val)`

#### `def read_all_avail_samp(self)`

#### `def relative_to(self)`


        :class:`nidaqmx.constants.ReadRelativeTo`: Specifies the point
            in the buffer at which to begin a read operation. If you
            also specify an offset with **offset**, the read operation
            begins at that offset relative to the point you select with
            this property. The default value is
            **ReadRelativeTo.CURRENT_READ_POSITION** unless you
            configure a Reference Trigger for the task. If you configure
            a Reference Trigger, the default value is
            **ReadRelativeTo.FIRST_PRETRIGGER_SAMPLE**.
        

#### `def relative_to(self, val)`

#### `def relative_to(self)`

#### `def remote_sense_error_chans(self)`


        List[str]: Indicates a list of names of any virtual channels in
            the task for which a remote sense connection error condition
            has been detected. You must read Remote Sense Error Channels
            Exist before you read this property. Otherwise, you will
            receive an error.
        

#### `def remote_sense_error_chans_exist(self)`


        bool: Indicates if the device(s) detected an error condition of
            the remote sense connection for any channel in the task. You
            must disable the output and resolve the hardware connection
            issue to clear the error condition. You must read this
            property before you read the Remote Sense Error Channels
            property. Otherwise, you will receive an error.
        

#### `def reverse_voltage_error_chans(self)`


        List[str]: Indicates a list of names of all virtual channels in
            the task for which reverse voltage error condition has been
            detected. You must read the Reverse Voltage Error Channels
            Exist property before you read this property. Otherwise, you
            will receive an error.
        

#### `def reverse_voltage_error_chans_exist(self)`


        bool: Indicates if the device(s) detected reverse voltage error
            for any of the channels in the task. Reverse voltage error
            occurs if the local voltage is equal to the negative
            saturated voltage. Reading this property clears the error
            condition status for all channels in the task. You must read
            this property before you read the Reverse Voltage Error
            Channels property. Otherwise, you will receive an error.
        

#### `def sleep_time(self)`


        float: Specifies in seconds the amount of time to sleep after
            checking for available samples if **wait_mode** is
            **WaitMode.SLEEP**.
        

#### `def sleep_time(self, val)`

#### `def sleep_time(self)`

#### `def sync_unlocked_chans(self)`


        List[str]: Indicates the channels from devices in an unlocked
            target.
        

#### `def sync_unlocked_chans_exist(self)`


        bool: Indicates whether the target is currently locked to the
            grand master. Devices may report PLL Unlock either during
            acquisition or after acquisition.
        

#### `def total_samp_per_chan_acquired(self)`


        int: Indicates the total number of samples acquired by each
            channel. NI-DAQmx returns a single value because this value
            is the same for all channels. For retriggered acquisitions,
            this value is the cumulative number of samples across all
            retriggered acquisitions.
        

#### `def wait_mode(self)`


        :class:`nidaqmx.constants.WaitMode`: Specifies how DAQmx Read
            waits for samples to become available.
        

#### `def wait_mode(self, val)`

#### `def wait_mode(self)`

#### `def get_channels_buffer_size(self)`

#### `def _calculate_num_samps_per_chan(self, num_samps_per_chan)`

#### `def configure_logging(self, file_path: str | pathlib.PurePath, logging_mode=LoggingMode.LOG_AND_READ, group_name='', operation=LoggingOperation.OPEN_OR_CREATE)`


        Configures TDMS file logging for the task.

        Args:
            file_path: Specifies the path to the TDMS file to
                which you want to log data.
            logging_mode (Optional[nidaqmx.constants.LoggingMode]):
                Specifies whether to enable logging and whether to allow
                reading data while logging. "log" mode allows for the
                best performance. However, you cannot read data while
                logging if you specify this mode. If you want to read
                data while logging, specify "LOG_AND_READ" mode.
            group_name (Optional[str]): Specifies the name of the group
                to create within the TDMS file for data from this task.
                If you append data to an existing file and the specified
                group already exists, NI-DAQmx appends a number symbol
                and a number to the group name, incrementing that number
                until finding a group name that does not exist. For
                example, if you specify a group name of Voltage Task,
                and that group already exists, NI-DAQmx assigns the
                group name Voltage Task #1, then Voltage Task #2. If you
                do not specify a group name, NI-DAQmx uses the name of
                the task.
            operation (Optional[nidaqmx.constants.LoggingOperation]):
                Specifies how to open the TDMS file.
        

#### `def read(self, number_of_samples_per_channel=READ_ALL_AVAILABLE)`


        Reads raw samples from the task or virtual channels you specify.

        Raw samples constitute the internal representation of samples in a
        device, read directly from the device or buffer without scaling or
        reordering. The native format of a device can be an 8-, 16-, or
        32-bit integer, signed or unsigned.

        NI-DAQmx does not separate raw data into channels. It returns data
        in an interleaved or non-interleaved 1D array, depending on the
        raw ordering of the device. Refer to your device documentation for
        more information.

        This method determines a NumPy array of appropriate size and data
        type to create and return based on your device specifications.

        Use the "timeout" property on the stream to specify the amount of
        time in seconds to wait for samples to become available. If the
        time elapses, the method returns an error and any samples read
        before the timeout elapsed. The default timeout is 10 seconds.
        If you set timeout to nidaqmx.WAIT_INFINITELY, the method waits
        indefinitely. If you set timeout to 0, the method tries once to
        read the requested samples and returns an error if it is unable
        to.

        Args:
            number_of_samples_per_channel (int): Specifies the number of
                samples to read.

                If you set this input to nidaqmx.READ_ALL_AVAILABLE,
                NI-DAQmx determines how many samples to read based on if
                the task acquires samples continuously or acquires a
                finite number of samples.

                If the task acquires samples continuously and you set
                this input to nidaqmx.READ_ALL_AVAILABLE, this method
                reads all the samples currently available in the buffer.

                If the task acquires a finite number of samples and you
                set this input to nidaqmx.READ_ALL_AVAILABLE, the method
                waits for the task to acquire all requested samples,
                then reads those samples. If you set the
                "read_all_avail_samp" property to TRUE, the method reads
                the samples currently available in the buffer and does
                not wait for the task to acquire all requested samples.
        Returns:
            numpy.ndarray:

            The samples requested in the form of a 1D NumPy array. This
            method determines a NumPy array of appropriate size and data
            type to create and return based on your device specifications.
        

#### `def readall(self)`

#### `def read_all(self)`


        Reads all available raw samples from the task or virtual channels
        you specify.

        NI-DAQmx determines how many samples to read based on if the task
        acquires samples continuously or acquires a finite number of
        samples.

        If the task acquires samples continuously, this method reads all
        the samples currently available in the buffer.

        If the task acquires a finite number of samples, the method
        waits for the task to acquire all requested samples, then reads
        those samples. If you set the "read_all_avail_samp" property to
        TRUE, the method reads the samples currently available in the
        buffer and does not wait for the task to acquire all requested
        samples.

        Raw samples constitute the internal representation of samples in a
        device, read directly from the device or buffer without scaling or
        reordering. The native format of a device can be an 8-, 16-, or
        32-bit integer, signed or unsigned.

        NI-DAQmx does not separate raw data into channels. It returns data
        in an interleaved or non-interleaved 1D array, depending on the
        raw ordering of the device. Refer to your device documentation for
        more information.

        This method determines a NumPy array of appropriate size and data
        type to create and return based on your device specifications.

        Use the "timeout" property on the stream to specify the amount of
        time in seconds to wait for samples to become available. If the
        time elapses, the method returns an error and any samples read
        before the timeout elapsed. The default timeout is 10 seconds.
        If you set timeout to nidaqmx.WAIT_INFINITELY, the method waits
        indefinitely. If you set timeout to 0, the method tries once to
        read the requested samples and returns an error if it is unable
        to.

        Returns:
            numpy.ndarray:

            The samples requested in the form of a 1D NumPy array. This
            method determines a NumPy array of appropriate size and data
            type to create and return based on your device specifications.
        

#### `def readinto(self, numpy_array)`

#### `def read_into(self, numpy_array)`


        Reads raw samples from the task or virtual channels you specify
        into numpy_array.

        The object numpy_array should be a pre-allocated, writable 1D
        numpy array.

        The number of samples per channel to read is determined using
        the following equation:

        number_of_samples_per_channel = math.floor(
            numpy_array_size_in_bytes / (
                number_of_channels_to_read * raw_sample_size_in_bytes))

        Raw samples constitute the internal representation of samples in a
        device, read directly from the device or buffer without scaling or
        reordering. The native format of a device can be an 8-, 16-, or
        32-bit integer, signed or unsigned.

        If you use a different integer size than the native format of the
        device, one integer can contain multiple samples or one sample can
        stretch across multiple integers. For example, if you use 32-bit
        integers, but the device uses 8-bit samples, one integer contains
        up to four samples. If you use 8-bit integers, but the device uses
        16-bit samples, a sample might require two integers. This behavior
        varies from device to device. Refer to your device documentation
        for more information.

        NI-DAQmx does not separate raw data into channels. It returns data
        in an interleaved or non-interleaved 1D array, depending on the
        raw ordering of the device. Refer to your device documentation for
        more information.

        Use the "timeout" property on the stream to specify the amount of
        time in seconds to wait for samples to become available. If the
        time elapses, the method returns an error and any samples read
        before the timeout elapsed. The default timeout is 10 seconds.
        If you set timeout to -1, the method waits indefinitely. If you
        set timeout to 0, the method tries once to read the requested
        samples and returns an error if it is unable to.

        Args:
            numpy_array: Specifies the 1D NumPy array object into which
                the samples requested are read.
        Returns:
            int: Indicates the total number of samples read.
        

#### `def start_new_file(self, file_path: str | pathlib.PurePath)`


        Starts a new TDMS file the next time data is written to disk.

        Args:
            file_path: Specifies the path to the TDMS file to
                which you want to log data.
        

#### `def over_write(self)`

#### `def over_write(self, val)`

#### `def over_write(self)`

#### `def waveform_attribute_mode(self)`


        :class:`nidaqmx.constants.WaveformAttributeMode`: Specifies the type of information returned from waveform reads.
        

#### `def waveform_attribute_mode(self, val)`

#### `def waveform_attribute_mode(self)`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/_out_stream.py -->
## PYTHON MODULE: generated/nidaqmx/task/_out_stream.py

### `class OutStream()`


    Exposes an output data stream on a DAQmx task.

    The output data stream be used to control writing behavior and can be
    used in conjunction with writer classes to write samples to an
    NI-DAQmx task.
    

#### `def __init__(self, task, interpreter)`

#### `def __eq__(self, other)`

#### `def __hash__(self)`

#### `def __ne__(self, other)`

#### `def __repr__(self)`

#### `def auto_start(self)`


        bool: Specifies if the "write" method automatically starts the
            stream's owning task if you did not explicitly start it
            with the DAQmx Start Task method.
        

#### `def auto_start(self, val)`

#### `def auto_start(self)`

#### `def timeout(self)`


        float: Specifies the amount of time in seconds to wait for
            the write method to write all samples. NI-DAQmx performs a
            timeout check only if the write method must wait before it
            writes data. The write method returns an error if the time
            elapses. The default timeout is 10 seconds. If you set
            "timeout" to nidaqmx.WAIT_INFINITELY, the write method
            waits indefinitely. If you set timeout to 0, the write
            method tries once to write the submitted samples. If the
            write method could not write all the submitted samples, it
            returns an error and the number of samples successfully
            written in the number of samples written per channel
            output.
        

#### `def timeout(self, val)`

#### `def timeout(self)`

#### `def accessory_insertion_or_removal_detected(self)`


        bool: Indicates if any devices in the task detected the
            insertion or removal of an accessory since the task started.
            Reading this property clears the accessory change status for
            all channels in the task. You must read this property before
            you read **devs_with_inserted_or_removed_accessories**.
            Otherwise, you will receive an error.
        

#### `def curr_write_pos(self)`


        int: Indicates the position in the buffer of the next sample to
            generate. This value is identical for all channels in the
            task.
        

#### `def devs_with_inserted_or_removed_accessories(self)`


        List[str]: Indicates the names of any devices that detected the
            insertion or removal of an accessory since the task started.
            You must read **accessory_insertion_or_removal_detected**
            before you read this property. Otherwise, you will receive
            an error.
        

#### `def do_num_booleans_per_chan(self)`


        int: Indicates the number of Boolean values expected per channel
            in a sample for line-based writes. This property is
            determined by the channel in the task with the most digital
            lines. If a channel has fewer lines than this number, NI-
            DAQmx ignores the extra Boolean values.
        

#### `def external_overvoltage_chans(self)`


        List[str]: Indicates a list of names of any virtual channels in
            the task for which an External Overvoltage condition has
            been detected. You must read External OvervoltageChansExist
            before you read this property. Otherwise, you will receive
            an error.
        

#### `def external_overvoltage_chans_exist(self)`


        bool: Indicates if the device(s) detected an External
            Overvoltage condition for any channel in the task. Reading
            this property clears the External Overvoltage status for all
            channels in the task. You must read this property before you
            read External OvervoltageChans. Otherwise, you will receive
            an error.
        

#### `def num_chans(self)`


        int: Indicates the number of channels that DAQmx Write writes to
            the task. This value is the number of channels in the task.
        

#### `def offset(self)`


        int: Specifies in samples per channel an offset at which a write
            operation begins. This offset is relative to the location
            you specify with **relative_to**.
        

#### `def offset(self, val)`

#### `def offset(self)`

#### `def open_current_loop_chans(self)`


        List[str]: Indicates a list of names of any virtual channels in
            the task for which the device(s) detected an open current
            loop. You must read **open_current_loop_chans_exist** before
            you read this property. Otherwise, you will receive an
            error.
        

#### `def open_current_loop_chans_exist(self)`


        bool: Indicates if the device(s) detected an open current loop
            for any channel in the task. Reading this property clears
            the open current loop status for all channels in the task.
            You must read this property before you read
            **open_current_loop_chans**. Otherwise, you will receive an
            error.
        

#### `def output_buf_size(self)`


        int: Specifies the number of samples the output buffer can hold
            for each channel in the task. Zero indicates to allocate no
            buffer. Use a buffer size of 0 to perform a hardware-timed
            operation without using a buffer. Setting this property
            overrides the automatic output buffer allocation that NI-
            DAQmx performs.
        

#### `def output_buf_size(self, val)`

#### `def output_buf_size(self)`

#### `def output_onbrd_buf_size(self)`


        int: Specifies in samples per channel the size of the onboard
            output buffer of the device.
        

#### `def output_onbrd_buf_size(self, val)`

#### `def output_onbrd_buf_size(self)`

#### `def overcurrent_chans(self)`


        List[str]: Indicates a list of names of any virtual channels in
            the task for which an overcurrent condition has been
            detected. You must read **overcurrent_chans_exist** before
            you read this property. Otherwise, you will receive an
            error.
        

#### `def overcurrent_chans_exist(self)`


        bool: Indicates if the device(s) detected an overcurrent
            condition for any channel in the task. Reading this property
            clears the overcurrent status for all channels in the task.
            You must read this property before you read
            **overcurrent_chans**. Otherwise, you will receive an error.
        

#### `def overloaded_chans(self)`


        List[str]: Indicates a list of names of any overloaded virtual
            channels in the task. You must read
            **overloaded_chans_exist** before you read this property.
            Otherwise, you will receive an error.
        

#### `def overloaded_chans_exist(self)`


        bool: Indicates if the device(s) detected an overload in any
            virtual channel in the task. Reading this property clears
            the overload status for all channels in the task. You must
            read this property before you read **overloaded_chans**.
            Otherwise, you will receive an error.
        

#### `def overtemperature_chans(self)`


        List[str]: Indicates a list of names of any overtemperature
            virtual channels. You must read
            **overtemperature_chans_exist** before you read this
            property. Otherwise, you will receive an error. The list of
            names may be empty if the device cannot determine the source
            of the overtemperature.
        

#### `def overtemperature_chans_exist(self)`


        bool: Indicates if the device(s) detected an overtemperature
            condition in any virtual channel in the task. Reading this
            property clears the overtemperature status for all channels
            in the task. You must read this property before you read
            **overtemperature_chans**. Otherwise, you will receive an
            error.
        

#### `def power_supply_fault_chans(self)`


        List[str]: Indicates a list of names of any virtual channels in
            the task that have a power supply fault. You must read
            **power_supply_fault_chans_exist** before you read this
            property. Otherwise, you will receive an error.
        

#### `def power_supply_fault_chans_exist(self)`


        bool: Indicates if the device(s) detected a power supply fault
            for any channel in the task. Reading this property clears
            the power supply fault status for all channels in the task.
            You must read this property before you read
            **power_supply_fault_chans**. Otherwise, you will receive an
            error.
        

#### `def raw_data_width(self)`


        int: Indicates in bytes the required size of a raw sample to
            write to the task.
        

#### `def regen_mode(self)`


        :class:`nidaqmx.constants.RegenerationMode`: Specifies whether
            to allow NI-DAQmx to generate the same data multiple times.
        

#### `def regen_mode(self, val)`

#### `def regen_mode(self)`

#### `def relative_to(self)`


        :class:`nidaqmx.constants.WriteRelativeTo`: Specifies the point
            in the buffer at which to write data. If you also specify an
            offset with **offset**, the write operation begins at that
            offset relative to this point you select with this property.
        

#### `def relative_to(self, val)`

#### `def relative_to(self)`

#### `def sleep_time(self)`


        float: Specifies in seconds the amount of time to sleep after
            checking for available buffer space if **wait_mode** is
            **WaitMode2.SLEEP**.
        

#### `def sleep_time(self, val)`

#### `def sleep_time(self)`

#### `def space_avail(self)`


        int: Indicates in samples per channel the amount of available
            space in the buffer.
        

#### `def sync_unlocked_chans(self)`


        List[str]: Indicates the channels from devices in an unlocked
            target.
        

#### `def sync_unlocked_chans_exist(self)`


        bool: Indicates whether the target is currently locked to the
            grand master. Devices may report PLL Unlock either during
            acquisition or after acquisition.
        

#### `def total_samp_per_chan_generated(self)`


        int: Indicates the total number of samples generated by each
            channel in the task. This value is identical for all
            channels in the task.
        

#### `def wait_mode(self)`


        :class:`nidaqmx.constants.WaitMode`: Specifies how DAQmx Write
            waits for space to become available in the buffer.
        

#### `def wait_mode(self, val)`

#### `def wait_mode(self)`

#### `def write(self, numpy_array)`


        Writes raw samples to the task or virtual channels you specify.

        The number of samples per channel to write is determined using the
        following equation:

        number_of_samples_per_channel = math.floor(
            numpy_array_size_in_bytes / (
                number_of_channels_to_write * raw_sample_size_in_bytes))

        Raw samples constitute the internal representation of samples in a
        device, read directly from the device or buffer without scaling or
        reordering. The native format of a device can be an 8-, 16-, or 32-bit
        integer, signed or unsigned.

        If you use a different integer size than the native format of the
        device, one integer can contain multiple samples or one sample can
        stretch across multiple integers. For example, if you use 32-bit
        integers, but the device uses 8-bit samples, one integer contains up to
        four samples. If you use 8-bit integers, but the device uses 16-bit
        samples, a sample might require two integers. This behavior varies from
        device to device. Refer to your device documentation for more
        information.

        NI-DAQmx does not separate raw data into channels. It accepts data in
        an interleaved or non-interleaved 1D array, depending on the raw
        ordering of the device. Refer to your device documentation for more
        information.

        If the task uses on-demand timing, this method returns only after the
        device generates all samples. On-demand is the default timing type if
        you do not use the timing property on the task to configure a sample
        timing type. If the task uses any timing type other than on-demand,
        this method returns immediately and does not wait for the device to
        generate all samples. Your application must determine if the task is
        done to ensure that the device generated all samples.

        Use the "auto_start" property on the stream to specify if this method
        automatically starts the stream's owning task if you did not explicitly
        start it with the DAQmx Start Task method.

        Use the "timeout" property on the stream to specify the amount of
        time in seconds to wait for the method to write all samples. NI-DAQmx
        performs a timeout check only if the method must wait before it writes
        data. This method returns an error if the time elapses. The default
        timeout is 10 seconds. If you set timeout to nidaqmx.WAIT_INFINITELY,
        the method waits indefinitely. If you set timeout to 0, the method
        tries once to write the submitted samples. If the method could not
        write all the submitted samples, it returns an error and the number of
        samples successfully written.

        Args:
            numpy_array (numpy.ndarray): Specifies a 1D NumPy array that
                contains the raw samples to write to the task.
        Returns:
            int:

            Specifies the actual number of samples per channel successfully
            written to the buffer.
        

#### `def get_channels_buffer_size(self)`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/_task.py -->
## PYTHON MODULE: generated/nidaqmx/task/_task.py

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

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/_timing.py -->
## PYTHON MODULE: generated/nidaqmx/task/_timing.py

### `class Timing()`


    Represents the timing configurations for a DAQmx task.
    

#### `def __init__(self, task_handle, interpreter, active_devs: str | Device | None=None)`

#### `def __getitem__(self, dev: str | Device) -> Timing`

#### `def _raise_device_context_not_supported_error(self) -> NoReturn`

#### `def ai_conv_active_edge(self)`


        :class:`nidaqmx.constants.Edge`: Specifies on which edge of the
            clock pulse an analog-to-digital conversion takes place.
        

#### `def ai_conv_active_edge(self, val)`

#### `def ai_conv_active_edge(self)`

#### `def ai_conv_dig_fltr_enable(self)`


        bool: Specifies whether to apply a digital filter to the AI
            Convert Clock.
        

#### `def ai_conv_dig_fltr_enable(self, val)`

#### `def ai_conv_dig_fltr_enable(self)`

#### `def ai_conv_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def ai_conv_dig_fltr_min_pulse_width(self, val)`

#### `def ai_conv_dig_fltr_min_pulse_width(self)`

#### `def ai_conv_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def ai_conv_dig_fltr_timebase_rate(self, val)`

#### `def ai_conv_dig_fltr_timebase_rate(self)`

#### `def ai_conv_dig_fltr_timebase_src(self)`


        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        

#### `def ai_conv_dig_fltr_timebase_src(self, val)`

#### `def ai_conv_dig_fltr_timebase_src(self)`

#### `def ai_conv_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def ai_conv_dig_sync_enable(self, val)`

#### `def ai_conv_dig_sync_enable(self)`

#### `def ai_conv_max_rate(self)`


        float: Indicates the maximum convert rate supported by the task,
            given the current devices and channel count.
        

#### `def ai_conv_rate(self)`


        float: Specifies in Hertz the rate at which to clock the analog-
            to-digital converter. This clock is specific to the analog
            input section of multiplexed devices.
        

#### `def ai_conv_rate(self, val)`

#### `def ai_conv_rate(self)`

#### `def ai_conv_src(self)`


        str: Specifies the terminal of the signal to use as the AI
            Convert Clock.
        

#### `def ai_conv_src(self, val)`

#### `def ai_conv_src(self)`

#### `def ai_conv_timebase_div(self)`


        int: Specifies the number of AI Convert Clock Timebase pulses
            needed to produce a single AI Convert Clock pulse.
        

#### `def ai_conv_timebase_div(self, val)`

#### `def ai_conv_timebase_div(self)`

#### `def ai_conv_timebase_src(self)`


        :class:`nidaqmx.constants.MIOAIConvertTimebaseSource`: Specifies
            the terminal  of the signal to use as the AI Convert Clock
            Timebase.
        

#### `def ai_conv_timebase_src(self, val)`

#### `def ai_conv_timebase_src(self)`

#### `def change_detect_di_falling_edge_physical_chans(self)`


        :class:`nidaqmx.system.physical_channel.PhysicalChannel`:
            Specifies the names of the digital lines or ports on which
            to detect falling edges. The lines or ports must be used by
            virtual channels in the task. You also can specify a string
            that contains a list or range of digital lines or ports.
        

#### `def change_detect_di_falling_edge_physical_chans(self, val)`

#### `def change_detect_di_falling_edge_physical_chans(self)`

#### `def change_detect_di_rising_edge_physical_chans(self)`


        :class:`nidaqmx.system.physical_channel.PhysicalChannel`:
            Specifies the names of the digital lines or ports on which
            to detect rising edges. The lines or ports must be used by
            virtual channels in the task. You also can specify a string
            that contains a list or range of digital lines or ports.
        

#### `def change_detect_di_rising_edge_physical_chans(self, val)`

#### `def change_detect_di_rising_edge_physical_chans(self)`

#### `def change_detect_di_tristate(self)`


        bool: Specifies whether to tristate lines specified with
            **change_detect_di_rising_edge_physical_chans** and
            **change_detect_di_falling_edge_physical_chans** that are
            not in a virtual channel in the task. If you set this
            property to True, NI-DAQmx tristates rising/falling edge
            lines that are not in a virtual channel in the task. If you
            set this property to False, NI-DAQmx does not modify the
            configuration of rising/falling edge lines that are not in a
            virtual channel in the task, even if the lines were
            previously tristated. Set this property to False to detect
            changes on lines in other tasks or to detect changes on
            output-only lines.
        

#### `def change_detect_di_tristate(self, val)`

#### `def change_detect_di_tristate(self)`

#### `def delay_from_samp_clk_delay(self)`


        float: Specifies the amount of time to wait after receiving a
            Sample Clock edge before beginning to acquire the sample.
            This value is in the units you specify with
            **delay_from_samp_clk_delay_units**.
        

#### `def delay_from_samp_clk_delay(self, val)`

#### `def delay_from_samp_clk_delay(self)`

#### `def delay_from_samp_clk_delay_units(self)`


        :class:`nidaqmx.constants.DigitalWidthUnits`: Specifies the
            units of **delay_from_samp_clk_delay**.
        

#### `def delay_from_samp_clk_delay_units(self, val)`

#### `def delay_from_samp_clk_delay_units(self)`

#### `def first_samp_clk_offset(self)`


        float: Specifies, in seconds, the offset to apply to the
            **first_samp_clk_when** value. This offset modifies when the
            first sample clock occurs and is used to account for known
            delays in the signal path.
        

#### `def first_samp_clk_offset(self, val)`

#### `def first_samp_clk_offset(self)`

#### `def first_samp_clk_timescale(self)`


        :class:`nidaqmx.constants.Timescale`: Specifies the timescale to
            be used for the value of **first_samp_clk_when**.
        

#### `def first_samp_clk_timescale(self, val)`

#### `def first_samp_clk_timescale(self)`

#### `def first_samp_clk_when(self)`


        datetime: Specifies the time of the first sample clock pulse.
        

#### `def first_samp_clk_when(self, val)`

#### `def first_samp_clk_when(self)`

#### `def first_samp_timestamp_enable(self)`


        bool: Specifies whether to enable the first sample timestamp.
        

#### `def first_samp_timestamp_enable(self, val)`

#### `def first_samp_timestamp_enable(self)`

#### `def first_samp_timestamp_timescale(self)`


        :class:`nidaqmx.constants.Timescale`: Specifies the timescale to
            be used for the first sample timestamp.
        

#### `def first_samp_timestamp_timescale(self, val)`

#### `def first_samp_timestamp_timescale(self)`

#### `def first_samp_timestamp_val(self)`


        datetime: Indicates the timestamp of the first sample.
        

#### `def hshk_delay_after_xfer(self)`


        float: Specifies the number of seconds to wait after a handshake
            cycle before starting a new handshake cycle.
        

#### `def hshk_delay_after_xfer(self, val)`

#### `def hshk_delay_after_xfer(self)`

#### `def hshk_sample_input_data_when(self)`


        :class:`nidaqmx.constants.SampleInputDataWhen`: Specifies on
            which edge of the Handshake Trigger an input task latches
            the data from the peripheral device.
        

#### `def hshk_sample_input_data_when(self, val)`

#### `def hshk_sample_input_data_when(self)`

#### `def hshk_start_cond(self)`


        :class:`nidaqmx.constants.HandshakeStartCondition`: Specifies
            the point in the handshake cycle that the device is in when
            the task starts.
        

#### `def hshk_start_cond(self, val)`

#### `def hshk_start_cond(self)`

#### `def implicit_underflow_behavior(self)`


        :class:`nidaqmx.constants.UnderflowBehavior`: Specifies the
            action to take when the onboard memory of the device becomes
            empty.
        

#### `def implicit_underflow_behavior(self, val)`

#### `def implicit_underflow_behavior(self)`

#### `def master_timebase_rate(self)`


        float: Specifies the rate of the Master Timebase.
        

#### `def master_timebase_rate(self, val)`

#### `def master_timebase_rate(self)`

#### `def master_timebase_src(self)`


        str: Specifies the terminal of the signal to use as the Master
            Timebase. On an E Series device, you can choose only between
            the onboard 20MHz Timebase or the RTSI7 terminal.
        

#### `def master_timebase_src(self, val)`

#### `def master_timebase_src(self)`

#### `def ref_clk_rate(self)`


        float: Specifies the frequency of the Reference Clock.
        

#### `def ref_clk_rate(self, val)`

#### `def ref_clk_rate(self)`

#### `def ref_clk_src(self)`


        str: Specifies the terminal of the signal to use as the
            Reference Clock.
        

#### `def ref_clk_src(self, val)`

#### `def ref_clk_src(self)`

#### `def samp_clk_active_edge(self)`


        :class:`nidaqmx.constants.Edge`: Specifies on which edge of a
            clock pulse sampling takes place. This property is useful
            primarily when the signal you use as the Sample Clock is not
            a periodic clock.
        

#### `def samp_clk_active_edge(self, val)`

#### `def samp_clk_active_edge(self)`

#### `def samp_clk_dig_fltr_enable(self)`


        bool: Specifies whether to apply the pulse width filter to the
            signal.
        

#### `def samp_clk_dig_fltr_enable(self, val)`

#### `def samp_clk_dig_fltr_enable(self)`

#### `def samp_clk_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def samp_clk_dig_fltr_min_pulse_width(self, val)`

#### `def samp_clk_dig_fltr_min_pulse_width(self)`

#### `def samp_clk_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def samp_clk_dig_fltr_timebase_rate(self, val)`

#### `def samp_clk_dig_fltr_timebase_rate(self)`

#### `def samp_clk_dig_fltr_timebase_src(self)`


        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        

#### `def samp_clk_dig_fltr_timebase_src(self, val)`

#### `def samp_clk_dig_fltr_timebase_src(self)`

#### `def samp_clk_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def samp_clk_dig_sync_enable(self, val)`

#### `def samp_clk_dig_sync_enable(self)`

#### `def samp_clk_max_rate(self)`


        float: Indicates the maximum Sample Clock rate supported by the
            task, based on other timing settings. For output tasks, the
            maximum Sample Clock rate is the maximum rate of the DAC.
            For input tasks, NI-DAQmx calculates the maximum sampling
            rate differently for multiplexed devices than simultaneous
            sampling devices.
        

#### `def samp_clk_overrun_behavior(self)`


        :class:`nidaqmx.constants.OverflowBehavior`: Specifies the
            action to take if Sample Clock edges occur faster than the
            device can handle them.
        

#### `def samp_clk_overrun_behavior(self, val)`

#### `def samp_clk_overrun_behavior(self)`

#### `def samp_clk_rate(self)`


        float: Specifies the sampling rate in samples per channel per
            second. If you use an external source for the Sample Clock,
            set this input to the maximum expected rate of that clock.
        

#### `def samp_clk_rate(self, val)`

#### `def samp_clk_rate(self)`

#### `def samp_clk_src(self)`


        str: Specifies the terminal of the signal to use as the Sample
            Clock.
        

#### `def samp_clk_src(self, val)`

#### `def samp_clk_src(self)`

#### `def samp_clk_term(self)`


        str: Indicates the name of the internal Sample Clock terminal
            for the task. This property does not return the name of the
            Sample Clock source terminal specified with
            **samp_clk_src**.
        

#### `def samp_clk_timebase_active_edge(self)`


        :class:`nidaqmx.constants.Edge`: Specifies on which edge to
            recognize a Sample Clock Timebase pulse. This property is
            useful primarily when the signal you use as the Sample Clock
            Timebase is not a periodic clock.
        

#### `def samp_clk_timebase_active_edge(self, val)`

#### `def samp_clk_timebase_active_edge(self)`

#### `def samp_clk_timebase_div(self)`


        int: Specifies the number of Sample Clock Timebase pulses needed
            to produce a single Sample Clock pulse.
        

#### `def samp_clk_timebase_div(self, val)`

#### `def samp_clk_timebase_div(self)`

#### `def samp_clk_timebase_master_timebase_div(self)`


        int: Specifies the number of pulses of the Master Timebase
            needed to produce a single pulse of the Sample Clock
            Timebase.
        

#### `def samp_clk_timebase_master_timebase_div(self, val)`

#### `def samp_clk_timebase_master_timebase_div(self)`

#### `def samp_clk_timebase_rate(self)`


        float: Specifies the rate of the Sample Clock Timebase. Some
            applications require that you specify a rate when you use
            any signal other than the onboard Sample Clock Timebase. NI-
            DAQmx requires this rate to calculate other timing
            parameters.
        

#### `def samp_clk_timebase_rate(self, val)`

#### `def samp_clk_timebase_rate(self)`

#### `def samp_clk_timebase_src(self)`


        str: Specifies the terminal of the signal to use as the Sample
            Clock Timebase.
        

#### `def samp_clk_timebase_src(self, val)`

#### `def samp_clk_timebase_src(self)`

#### `def samp_clk_timebase_term(self)`


        str: Indicates the name of the internal Sample Clock Timebase
            terminal for the task. This property does not return the
            name of the Sample Clock Timebase source terminal specified
            with **samp_clk_timebase_src**.
        

#### `def samp_clk_underflow_behavior(self)`


        :class:`nidaqmx.constants.UnderflowBehavior`: Specifies the
            action to take when the onboard memory of the device becomes
            empty. In either case, the sample clock does not stop.
        

#### `def samp_clk_underflow_behavior(self, val)`

#### `def samp_clk_underflow_behavior(self)`

#### `def samp_clk_write_wfm_use_initial_wfm_dt(self)`


        bool: Specifies that the value of **samp_clk_rate** will be
            determined by the dt component of the initial DAQmx Write
            waveform input for Output tasks.
        

#### `def samp_clk_write_wfm_use_initial_wfm_dt(self, val)`

#### `def samp_clk_write_wfm_use_initial_wfm_dt(self)`

#### `def samp_quant_samp_mode(self)`


        :class:`nidaqmx.constants.AcquisitionType`: Specifies if a task
            acquires or generates a finite number of samples or if it
            continuously acquires or generates samples.
        

#### `def samp_quant_samp_mode(self, val)`

#### `def samp_quant_samp_mode(self)`

#### `def samp_quant_samp_per_chan(self)`


        int: Specifies the number of samples to acquire or generate for
            each channel if **samp_quant_samp_mode** is
            **AcquisitionType.FINITE**. If **samp_quant_samp_mode** is
            **AcquisitionType.CONTINUOUS**, NI-DAQmx uses this value to
            determine the buffer size.
        

#### `def samp_quant_samp_per_chan(self, val)`

#### `def samp_quant_samp_per_chan(self)`

#### `def samp_timing_engine(self)`


        int: Specifies which timing engine to use for the task.
        

#### `def samp_timing_engine(self, val)`

#### `def samp_timing_engine(self)`

#### `def samp_timing_type(self)`


        :class:`nidaqmx.constants.SampleTimingType`: Specifies the type
            of sample timing to use for the task.
        

#### `def samp_timing_type(self, val)`

#### `def samp_timing_type(self)`

#### `def simultaneous_ao_enable(self)`


        bool: Specifies whether to update all channels in the task
            simultaneously, rather than updating channels independently
            when you write a sample to that channel.
        

#### `def simultaneous_ao_enable(self, val)`

#### `def simultaneous_ao_enable(self)`

#### `def sync_clk_interval(self)`


        int: Specifies the interval, in Sample Clock periods, between
            each internal Synchronization Clock pulse. NI-DAQmx uses
            this pulse for synchronization of triggers between multiple
            devices at different rates. Refer to device documentation
            for information about how to calculate this value.
        

#### `def sync_clk_interval(self, val)`

#### `def sync_clk_interval(self)`

#### `def sync_pulse_min_delay_to_start(self)`


        float: Specifies in seconds the amount of time that elapses
            after the master device issues the synchronization pulse
            before the task starts.
        

#### `def sync_pulse_min_delay_to_start(self, val)`

#### `def sync_pulse_min_delay_to_start(self)`

#### `def sync_pulse_reset_delay(self)`


        float: Specifies in seconds the amount of time to wait after the
            Synchronization Pulse before resetting the ADCs or DACs on
            the device. When synchronizing devices, query
            **sync_pulse_reset_time** on all devices and note the
            largest reset time. Then, for each device, subtract the
            reset time from the largest reset time and set this property
            to the resulting value.
        

#### `def sync_pulse_reset_delay(self, val)`

#### `def sync_pulse_reset_delay(self)`

#### `def sync_pulse_reset_time(self)`


        float: Indicates in seconds the amount of time required for the
            ADCs or DACs on the device to reset. When synchronizing
            devices, query this property on all devices and note the
            largest reset time. Then, for each device, subtract the
            value of this property from the largest reset time and set
            **sync_pulse_reset_delay** to the resulting value.
        

#### `def sync_pulse_src(self)`


        str: Specifies the terminal of the signal to use as the
            synchronization pulse. The synchronization pulse resets the
            clock dividers and the ADCs/DACs on the device.
        

#### `def sync_pulse_src(self, val)`

#### `def sync_pulse_src(self)`

#### `def sync_pulse_sync_time(self)`


        float: Indicates in seconds the delay required to reset the
            ADCs/DACs after the device receives the synchronization
            pulse.
        

#### `def sync_pulse_term(self)`


        str: Indicates the name of the internal Synchronization Pulse
            terminal for the task. This property does not return the
            name of the source terminal.
        

#### `def sync_pulse_time_timescale(self)`


        :class:`nidaqmx.constants.Timescale`: Specifies the timescale to
            be used for timestamps for a sync pulse.
        

#### `def sync_pulse_time_timescale(self, val)`

#### `def sync_pulse_time_timescale(self)`

#### `def sync_pulse_time_when(self)`


        datetime: Specifies the start time of the sync pulse.
        

#### `def sync_pulse_time_when(self, val)`

#### `def sync_pulse_time_when(self)`

#### `def sync_pulse_type(self)`


        :class:`nidaqmx.constants.SyncPulseType`: Specifies the type of
            sync pulse used in the task.
        

#### `def sync_pulse_type(self, val)`

#### `def sync_pulse_type(self)`

#### `def cfg_burst_handshaking_timing_export_clock(self, sample_clk_rate, sample_clk_outp_term, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000, sample_clk_pulse_polarity=Polarity.ACTIVE_HIGH, pause_when=Level.HIGH, ready_event_active_level=Polarity.ACTIVE_HIGH)`


        Configures when the DAQ device transfers data to a peripheral
        device, using the onboard Sample Clock of the DAQ device to
        control burst handshake timing and exporting that clock for use
        by the peripheral device.

        Args:
            sample_clk_rate (float): Specifies in hertz the rate of the
                Sample Clock.
            sample_clk_outp_term (str): Specifies the terminal to which
                to export the Sample Clock.
            sample_mode (Optional[nidaqmx.constants.AcquisitionType]): 
                Specifies if the task acquires or generates samples
                continuously or if it acquires or generates a finite
                number of samples.
            samps_per_chan (Optional[int]): Specifies the number of
                samples to acquire or generate for each channel in the
                task if **sample_mode** is **FINITE_SAMPLES**. If
                **sample_mode** is **CONTINUOUS_SAMPLES**, NI-DAQmx uses
                this value to determine the buffer size. This function
                returns an error if the specified value is negative.
            sample_clk_pulse_polarity (Optional[nidaqmx.constants.Polarity]): 
                Specifies the polarity of the exported Sample Clock.
            pause_when (Optional[nidaqmx.constants.Level]): Specifies
                whether the task pauses while the trigger signal is high
                or low.
            ready_event_active_level (Optional[nidaqmx.constants.Polarity]): 
                Specifies the polarity of the Ready for Transfer Event.
        

#### `def cfg_burst_handshaking_timing_import_clock(self, sample_clk_rate, sample_clk_src, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000, sample_clk_active_edge=Edge.RISING, pause_when=Level.HIGH, ready_event_active_level=Polarity.ACTIVE_HIGH)`


        Configures when the DAQ device transfers data to a peripheral
        device, using an imported sample clock to control burst
        handshake timing.

        Args:
            sample_clk_rate (float): Specifies in hertz the rate of the
                Sample Clock.
            sample_clk_src (str): Specifies the source terminal of the
                Sample Clock. Leave this input unspecified to use the
                default onboard clock of the device.
            sample_mode (Optional[nidaqmx.constants.AcquisitionType]): 
                Specifies if the task acquires or generates samples
                continuously or if it acquires or generates a finite
                number of samples.
            samps_per_chan (Optional[int]): Specifies the number of
                samples to acquire or generate for each channel in the
                task if **sample_mode** is **FINITE_SAMPLES**. If
                **sample_mode** is **CONTINUOUS_SAMPLES**, NI-DAQmx uses
                this value to determine the buffer size. This function
                returns an error if the specified value is negative.
            sample_clk_active_edge (Optional[nidaqmx.constants.Edge]): 
                Specifies on which edges of Sample Clock pulses to
                acquire or generate samples.
            pause_when (Optional[nidaqmx.constants.Level]): Specifies
                whether the task pauses while the trigger signal is high
                or low.
            ready_event_active_level (Optional[nidaqmx.constants.Polarity]): 
                Specifies the polarity of the Ready for Transfer Event.
        

#### `def cfg_change_detection_timing(self, rising_edge_chan='', falling_edge_chan='', sample_mode=AcquisitionType.FINITE, samps_per_chan=1000)`


        Configures the task to acquire samples on the rising and/or
        falling edges of the lines or ports you specify. To detect both
        rising and falling edges on a line or port, specify the name of
        that line or port to both **rising_edge_chan** and
        **falling_edge_chan**.

        Args:
            rising_edge_chan (Optional[str]): Specifies the names of the
                digital lines or ports on which to detect rising edges.
                The DAQmx physical channel constant lists all lines and
                ports for devices installed in your system.
            falling_edge_chan (Optional[str]): Specifies the names of
                the digital lines or ports on which to detect falling
                edges. The DAQmx physical channel constant lists all
                lines and ports for devices installed in your system.
            sample_mode (Optional[nidaqmx.constants.AcquisitionType]): 
                Specifies if the task acquires samples continuously or
                if it acquires a finite number of samples.
            samps_per_chan (Optional[int]): Specifies the number of
                samples to acquire from each channel in the task if
                **sample_mode** is **FINITE_SAMPLES**. This function
                returns an error if the specified value is negative.
        

#### `def cfg_handshaking_timing(self, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000)`


        Determines the number of digital samples to acquire or generate
        using digital handshaking between the device and a peripheral
        device.

        Args:
            sample_mode (Optional[nidaqmx.constants.AcquisitionType]): 
                Specifies if the task acquires or generates samples
                continuously or if it acquires or generates a finite
                number of samples.
            samps_per_chan (Optional[int]): Specifies the number of
                samples to acquire or generate for each channel in the
                task if **sample_mode** is **FINITE_SAMPLES**. If
                **sample_mode** is **CONTINUOUS_SAMPLES**, NI-DAQmx uses
                this value to determine the buffer size. This function
                returns an error if the specified value is negative.
        

#### `def cfg_implicit_timing(self, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000)`


        Sets only the number of samples to acquire or generate without
        specifying timing. Typically, you should use this instance when
        the task does not require sample timing, such as tasks that use
        counters for buffered frequency measurement, buffered period
        measurement, or pulse train generation. For finite counter
        output tasks, **samps_per_chan** is the number of pulses to
        generate.

        Args:
            sample_mode (Optional[nidaqmx.constants.AcquisitionType]): 
                Specifies if the task acquires or generates samples
                continuously or if it acquires or generates a finite
                number of samples.
            samps_per_chan (Optional[int]): Specifies the number of
                samples to acquire or generate for each channel in the
                task if **sample_mode** is **FINITE_SAMPLES**. If
                **sample_mode** is **CONTINUOUS_SAMPLES**, NI-DAQmx uses
                this value to determine the buffer size. This function
                returns an error if the specified value is negative.
        

#### `def cfg_pipelined_samp_clk_timing(self, rate, source='', active_edge=Edge.RISING, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000)`


        Sets the source of the Sample Clock, the rate of the Sample
        Clock, and the number of samples to acquire or generate. The
        device acquires or generates samples on each Sample Clock edge,
        but it does not respond to certain triggers until a few Sample
        Clock edges later. Pipelining allows higher data transfer rates
        at the cost of increased trigger response latency. Refer to the
        device documentation for information about which triggers
        pipelining affects.  This timing type allows handshaking using
        the Pause trigger and either the Ready for Transfer event or the
        Data Active event. Refer to the device documentation for more
        information.  This timing type is supported only by the NI 6536
        and NI 6537.

        Args:
            rate (float): Specifies the sampling rate in samples per
                channel per second. If you use an external source for
                the Sample Clock, set this input to the maximum expected
                rate of that clock.
            source (Optional[str]): Specifies the source terminal of the
                Sample Clock. Leave this input unspecified to use the
                default onboard clock of the device.
            active_edge (Optional[nidaqmx.constants.Edge]): Specifies on
                which edges of Sample Clock pulses to acquire or
                generate samples.
            sample_mode (Optional[nidaqmx.constants.AcquisitionType]): 
                Specifies if the task acquires or generates samples
                continuously or if it acquires or generates a finite
                number of samples.
            samps_per_chan (Optional[int]): Specifies the number of
                samples to acquire or generate for each channel in the
                task if **sample_mode** is **FINITE_SAMPLES**. If
                **sample_mode** is **CONTINUOUS_SAMPLES**, NI-DAQmx uses
                this value to determine the buffer size. This function
                returns an error if the specified value is negative.
        

#### `def cfg_samp_clk_timing(self, rate, source='', active_edge=Edge.RISING, sample_mode=AcquisitionType.FINITE, samps_per_chan=1000)`


        Sets the source of the Sample Clock, the rate of the Sample
        Clock, and the number of samples to acquire or generate.

        Args:
            rate (float): Specifies the sampling rate in samples per
                channel per second. If you use an external source for
                the Sample Clock, set this input to the maximum expected
                rate of that clock.
            source (Optional[str]): Specifies the source terminal of the
                Sample Clock. Leave this input unspecified to use the
                default onboard clock of the device.
            active_edge (Optional[nidaqmx.constants.Edge]): Specifies on
                which edges of Sample Clock pulses to acquire or
                generate samples.
            sample_mode (Optional[nidaqmx.constants.AcquisitionType]): 
                Specifies if the task acquires or generates samples
                continuously or if it acquires or generates a finite
                number of samples.
            samps_per_chan (Optional[int]): Specifies the number of
                samples to acquire or generate for each channel in the
                task if **sample_mode** is **FINITE_SAMPLES**. If
                **sample_mode** is **CONTINUOUS_SAMPLES**, NI-DAQmx uses
                this value to determine the buffer size. This function
                returns an error if the specified value is negative.
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/channels/__init__.py -->
## PYTHON MODULE: generated/nidaqmx/task/channels/__init__.py

### MODULE DOCSTRING

NI-DAQmx channel classes.

- `__all__ = ['Channel', 'AIChannel', 'AOChannel', 'CIChannel', 'COChannel', 'DIChannel', 'DOChannel']`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/channels/_ai_channel.py -->
## PYTHON MODULE: generated/nidaqmx/task/channels/_ai_channel.py

### `class AIChannel(Channel)`


    Represents one or more analog input virtual channels and their properties.
    

#### `def __repr__(self)`

#### `def ai_ac_excit_freq(self)`


        float: Specifies the AC excitation frequency in Hertz.
        

#### `def ai_ac_excit_freq(self, val)`

#### `def ai_ac_excit_freq(self)`

#### `def ai_ac_excit_sync_enable(self)`


        bool: Specifies whether to synchronize the AC excitation source
            of the channel to that of another channel. Synchronize the
            excitation sources of multiple channels to use multichannel
            sensors. Set this property to False for the master channel
            and to True for the slave channels.
        

#### `def ai_ac_excit_sync_enable(self, val)`

#### `def ai_ac_excit_sync_enable(self)`

#### `def ai_ac_excit_wire_mode(self)`


        :class:`nidaqmx.constants.ACExcitWireMode`: Specifies the number
            of leads on the LVDT or RVDT. Some sensors require you to
            tie leads together to create a four- or five- wire sensor.
            Refer to the sensor documentation for more information.
        

#### `def ai_ac_excit_wire_mode(self, val)`

#### `def ai_ac_excit_wire_mode(self)`

#### `def ai_accel_4_wire_dc_voltage_sensitivity(self)`


        float: Specifies the sensitivity of the 4 wire DC voltage
            acceleration sensor connected to the channel. This value is
            the units you specify with
            AI.Accel.4WireDCVoltage.SensitivityUnits. Refer to the
            sensor documentation to determine this value.
        

#### `def ai_accel_4_wire_dc_voltage_sensitivity(self, val)`

#### `def ai_accel_4_wire_dc_voltage_sensitivity(self)`

#### `def ai_accel_4_wire_dc_voltage_sensitivity_units(self)`


        :class:`nidaqmx.constants.AccelSensitivityUnits`: Specifies the
            units of AI.Accel.4WireDCVoltage.Sensitivity.
        

#### `def ai_accel_4_wire_dc_voltage_sensitivity_units(self, val)`

#### `def ai_accel_4_wire_dc_voltage_sensitivity_units(self)`

#### `def ai_accel_charge_sensitivity(self)`


        float: Specifies the sensitivity of the charge acceleration
            sensor connected to the channel. This value is the units you
            specify with AI.Accel.Charge.SensitivityUnits. Refer to the
            sensor documentation to determine this value.
        

#### `def ai_accel_charge_sensitivity(self, val)`

#### `def ai_accel_charge_sensitivity(self)`

#### `def ai_accel_charge_sensitivity_units(self)`


        :class:`nidaqmx.constants.AccelChargeSensitivityUnits`:
            Specifies the units of AI.Accel.Charge.Sensitivity.
        

#### `def ai_accel_charge_sensitivity_units(self, val)`

#### `def ai_accel_charge_sensitivity_units(self)`

#### `def ai_accel_db_ref(self)`


        float: Specifies the decibel reference level in the units of the
            channel. When you read samples as a waveform, the decibel
            reference level is included in the waveform attributes.
        

#### `def ai_accel_db_ref(self, val)`

#### `def ai_accel_db_ref(self)`

#### `def ai_accel_sensitivity(self)`


        float: Specifies the sensitivity of the accelerometer. This
            value is in the units you specify with
            **ai_accel_sensitivity_units**. Refer to the sensor
            documentation to determine this value.
        

#### `def ai_accel_sensitivity(self, val)`

#### `def ai_accel_sensitivity(self)`

#### `def ai_accel_sensitivity_units(self)`


        :class:`nidaqmx.constants.AccelSensitivityUnits`: Specifies the
            units of **ai_accel_sensitivity**.
        

#### `def ai_accel_sensitivity_units(self, val)`

#### `def ai_accel_sensitivity_units(self)`

#### `def ai_accel_units(self)`


        :class:`nidaqmx.constants.AccelUnits`: Specifies the units to
            use to return acceleration measurements from the channel.
        

#### `def ai_accel_units(self, val)`

#### `def ai_accel_units(self)`

#### `def ai_adc_custom_timing_mode(self)`


        int: Specifies the timing mode of the ADC when
            **ai_adc_timing_mode** is **ADCTimingMode.CUSTOM**.
        

#### `def ai_adc_custom_timing_mode(self, val)`

#### `def ai_adc_custom_timing_mode(self)`

#### `def ai_adc_timing_mode(self)`


        :class:`nidaqmx.constants.ADCTimingMode`: Specifies the ADC
            timing mode, controlling the tradeoff between speed and
            effective resolution. Some ADC timing modes provide
            increased powerline noise rejection. On devices that have an
            AI Convert clock, this setting affects both the maximum and
            default values for **ai_conv_rate**. You must use the same
            ADC timing mode for all channels on a device, but you can
            use different ADC timing modes for different devices in the
            same task.
        

#### `def ai_adc_timing_mode(self, val)`

#### `def ai_adc_timing_mode(self)`

#### `def ai_atten(self)`


        float: Specifies the amount of attenuation to use.
        

#### `def ai_atten(self, val)`

#### `def ai_atten(self)`

#### `def ai_auto_zero_mode(self)`


        :class:`nidaqmx.constants.AutoZeroType`: Specifies how often to
            measure ground. NI-DAQmx subtracts the measured ground
            voltage from every sample.
        

#### `def ai_auto_zero_mode(self, val)`

#### `def ai_auto_zero_mode(self)`

#### `def ai_averaging_win_size(self)`


        int: Specifies the number of samples to average while acquiring
            data. Increasing the number of samples to average reduces
            noise in your measurement.
        

#### `def ai_averaging_win_size(self, val)`

#### `def ai_averaging_win_size(self)`

#### `def ai_bridge_balance_coarse_pot(self)`


        int: Specifies by how much to compensate for offset in the
            signal. This value can be between 0 and 127.
        

#### `def ai_bridge_balance_coarse_pot(self, val)`

#### `def ai_bridge_balance_coarse_pot(self)`

#### `def ai_bridge_balance_fine_pot(self)`


        int: Specifies by how much to compensate for offset in the
            signal. This value can be between 0 and 4095.
        

#### `def ai_bridge_balance_fine_pot(self, val)`

#### `def ai_bridge_balance_fine_pot(self)`

#### `def ai_bridge_cfg(self)`


        :class:`nidaqmx.constants.BridgeConfiguration`: Specifies the
            type of Wheatstone bridge connected to the channel.
        

#### `def ai_bridge_cfg(self, val)`

#### `def ai_bridge_cfg(self)`

#### `def ai_bridge_electrical_units(self)`


        :class:`nidaqmx.constants.BridgeElectricalUnits`: Specifies from
            which electrical unit to scale data. Select  the same unit
            that the sensor data sheet or calibration certificate uses
            for electrical values.
        

#### `def ai_bridge_electrical_units(self, val)`

#### `def ai_bridge_electrical_units(self)`

#### `def ai_bridge_initial_ratio(self)`


        float: Specifies in volts per volt the ratio of output voltage
            from the bridge to excitation voltage supplied to the bridge
            while not under load. NI-DAQmx subtracts this value from any
            measurements before applying scaling equations. If you set
            **ai_bridge_initial_voltage**, NI-DAQmx coerces this
            property  to **ai_bridge_initial_voltage** divided by
            **ai_excit_actual_val**. If you set this property, NI-DAQmx
            coerces **ai_bridge_initial_voltage** to the value of this
            property times **ai_excit_actual_val**. If you set both this
            property and **ai_bridge_initial_voltage**, and their values
            conflict, NI-DAQmx returns an error.  To avoid this error,
            reset one property to its default value before setting the
            other.
        

#### `def ai_bridge_initial_ratio(self, val)`

#### `def ai_bridge_initial_ratio(self)`

#### `def ai_bridge_initial_voltage(self)`


        float: Specifies in volts the output voltage of the bridge while
            not under load. NI-DAQmx subtracts this value from any
            measurements before applying scaling equations.  If you set
            **ai_bridge_initial_ratio**, NI-DAQmx coerces this property
            to **ai_bridge_initial_ratio** times
            **ai_excit_actual_val**. This property is set by DAQmx
            Perform Bridge Offset Nulling Calibration. If you set this
            property, NI-DAQmx coerces **ai_bridge_initial_ratio** to
            the value of this property divided by
            **ai_excit_actual_val**. If you set both this property and
            **ai_bridge_initial_ratio**, and their values conflict, NI-
            DAQmx returns an error. To avoid this error, reset one
            property to its default value before setting the other.
        

#### `def ai_bridge_initial_voltage(self, val)`

#### `def ai_bridge_initial_voltage(self)`

#### `def ai_bridge_nom_resistance(self)`


        float: Specifies in ohms the resistance of the bridge while not
            under load.
        

#### `def ai_bridge_nom_resistance(self, val)`

#### `def ai_bridge_nom_resistance(self)`

#### `def ai_bridge_physical_units(self)`


        :class:`nidaqmx.constants.BridgePhysicalUnits`: Specifies to
            which physical unit to scale electrical data. Select the
            same unit that the sensor data sheet or calibration
            certificate uses for physical values.
        

#### `def ai_bridge_physical_units(self, val)`

#### `def ai_bridge_physical_units(self)`

#### `def ai_bridge_poly_forward_coeff(self)`


        List[float]: Specifies an list of coefficients for the
            polynomial that converts electrical values to physical
            values. Each element of the list corresponds to a term of
            the equation. For example, if index three of the list is 9,
            the fourth term of the equation is 9x^3.
        

#### `def ai_bridge_poly_forward_coeff(self, val)`

#### `def ai_bridge_poly_forward_coeff(self)`

#### `def ai_bridge_poly_reverse_coeff(self)`


        List[float]: Specifies an list of coefficients for the
            polynomial that converts physical values to electrical
            values. Each element of the list corresponds to a term of
            the equation. For example, if index three of the list is 9,
            the fourth term of the equation is 9x^3.
        

#### `def ai_bridge_poly_reverse_coeff(self, val)`

#### `def ai_bridge_poly_reverse_coeff(self)`

#### `def ai_bridge_scale_type(self)`


        :class:`nidaqmx.constants.ScaleType`: Specifies the scaling type
            to use when scaling electrical values from the sensor to
            physical units.
        

#### `def ai_bridge_scale_type(self, val)`

#### `def ai_bridge_scale_type(self)`

#### `def ai_bridge_shunt_cal_enable(self)`


        bool: Specifies whether to enable a shunt calibration switch.
            Use **ai_bridge_shunt_cal_select** to select the switch(es)
            to enable.
        

#### `def ai_bridge_shunt_cal_enable(self, val)`

#### `def ai_bridge_shunt_cal_enable(self)`

#### `def ai_bridge_shunt_cal_gain_adjust(self)`


        float: Specifies the result of a shunt calibration. This
            property is set by DAQmx Perform Shunt Calibration. NI-DAQmx
            multiplies data read from the channel by the value of this
            property. This value should be close to 1.0.
        

#### `def ai_bridge_shunt_cal_gain_adjust(self, val)`

#### `def ai_bridge_shunt_cal_gain_adjust(self)`

#### `def ai_bridge_shunt_cal_select(self)`


        :class:`nidaqmx.constants.ShuntCalSelect`: Specifies which shunt
            calibration switch(es) to enable.  Use
            **ai_bridge_shunt_cal_enable** to enable the switch(es) you
            specify with this property.
        

#### `def ai_bridge_shunt_cal_select(self, val)`

#### `def ai_bridge_shunt_cal_select(self)`

#### `def ai_bridge_shunt_cal_shunt_cal_a_actual_resistance(self)`


        float: Specifies in ohms the actual value of the internal shunt
            calibration A resistor.
        

#### `def ai_bridge_shunt_cal_shunt_cal_a_actual_resistance(self, val)`

#### `def ai_bridge_shunt_cal_shunt_cal_a_actual_resistance(self)`

#### `def ai_bridge_shunt_cal_shunt_cal_a_resistance(self)`


        float: Specifies in ohms the desired value of the internal shunt
            calibration A resistor.
        

#### `def ai_bridge_shunt_cal_shunt_cal_a_resistance(self, val)`

#### `def ai_bridge_shunt_cal_shunt_cal_a_resistance(self)`

#### `def ai_bridge_shunt_cal_shunt_cal_a_src(self)`


        :class:`nidaqmx.constants.BridgeShuntCalSource`: Specifies
            whether to use internal or external shunt when Shunt Cal A
            is selected.
        

#### `def ai_bridge_shunt_cal_shunt_cal_a_src(self, val)`

#### `def ai_bridge_shunt_cal_shunt_cal_a_src(self)`

#### `def ai_bridge_shunt_cal_shunt_cal_b_actual_resistance(self)`


        float: Specifies in ohms the actual value of the internal shunt
            calibration B resistor.
        

#### `def ai_bridge_shunt_cal_shunt_cal_b_actual_resistance(self, val)`

#### `def ai_bridge_shunt_cal_shunt_cal_b_actual_resistance(self)`

#### `def ai_bridge_shunt_cal_shunt_cal_b_resistance(self)`


        float: Specifies in ohms the desired value of the internal shunt
            calibration B resistor.
        

#### `def ai_bridge_shunt_cal_shunt_cal_b_resistance(self, val)`

#### `def ai_bridge_shunt_cal_shunt_cal_b_resistance(self)`

#### `def ai_bridge_table_electrical_vals(self)`


        List[float]: Specifies the list of electrical values that map to
            the values in **ai_bridge_table_physical_vals**. Specify
            this value in the unit indicated by
            **ai_bridge_electrical_units**.
        

#### `def ai_bridge_table_electrical_vals(self, val)`

#### `def ai_bridge_table_electrical_vals(self)`

#### `def ai_bridge_table_physical_vals(self)`


        List[float]: Specifies the list of physical values that map to
            the values in **ai_bridge_table_electrical_vals**. Specify
            this value in the unit indicated by
            **ai_bridge_physical_units**.
        

#### `def ai_bridge_table_physical_vals(self, val)`

#### `def ai_bridge_table_physical_vals(self)`

#### `def ai_bridge_two_point_lin_first_electrical_val(self)`


        float: Specifies the first electrical value, corresponding to
            **ai_bridge_two_point_lin_first_physical_val**. Specify this
            value in the unit indicated by
            **ai_bridge_electrical_units**.
        

#### `def ai_bridge_two_point_lin_first_electrical_val(self, val)`

#### `def ai_bridge_two_point_lin_first_electrical_val(self)`

#### `def ai_bridge_two_point_lin_first_physical_val(self)`


        float: Specifies the first physical value, corresponding to
            **ai_bridge_two_point_lin_first_electrical_val**. Specify
            this value in the unit indicated by
            **ai_bridge_physical_units**.
        

#### `def ai_bridge_two_point_lin_first_physical_val(self, val)`

#### `def ai_bridge_two_point_lin_first_physical_val(self)`

#### `def ai_bridge_two_point_lin_second_electrical_val(self)`


        float: Specifies the second electrical value, corresponding to
            **ai_bridge_two_point_lin_second_physical_val**. Specify
            this value in the unit indicated by
            **ai_bridge_electrical_units**.
        

#### `def ai_bridge_two_point_lin_second_electrical_val(self, val)`

#### `def ai_bridge_two_point_lin_second_electrical_val(self)`

#### `def ai_bridge_two_point_lin_second_physical_val(self)`


        float: Specifies the second physical value, corresponding to
            **ai_bridge_two_point_lin_second_electrical_val**. Specify
            this value in the unit indicated by
            **ai_bridge_physical_units**.
        

#### `def ai_bridge_two_point_lin_second_physical_val(self, val)`

#### `def ai_bridge_two_point_lin_second_physical_val(self)`

#### `def ai_bridge_units(self)`


        :class:`nidaqmx.constants.BridgeUnits`: Specifies in which unit
            to return voltage ratios from the channel.
        

#### `def ai_bridge_units(self, val)`

#### `def ai_bridge_units(self)`

#### `def ai_calculated_power_current_max(self)`


        float: Specifies the current maximum value you expect to
            measure. This value is in the units you specify with a units
            property. When you query this property, it returns the
            coerced current maximum value that the device can measure
            with the current settings.
        

#### `def ai_calculated_power_current_max(self, val)`

#### `def ai_calculated_power_current_max(self)`

#### `def ai_calculated_power_current_min(self)`


        float: Specifies the current minimum value you expect to
            measure. This value is in the units you specify with a units
            property. When you query this property, it returns the
            coerced current minimum value that the device can measure
            with the current settings.
        

#### `def ai_calculated_power_current_min(self, val)`

#### `def ai_calculated_power_current_min(self)`

#### `def ai_calculated_power_voltage_max(self)`


        float: Specifies the voltage maximum value you expect to
            measure. This value is in the units you specify with a units
            property. When you query this property, it returns the
            coerced voltage maximum value that the device can measure
            with the current settings.
        

#### `def ai_calculated_power_voltage_max(self, val)`

#### `def ai_calculated_power_voltage_max(self)`

#### `def ai_calculated_power_voltage_min(self)`


        float: Specifies the voltage minimum value you expect to
            measure. This value is in the units you specify with a units
            property. When you query this property, it returns the
            coerced voltage minimum value that the device can measure
            with the current settings.
        

#### `def ai_calculated_power_voltage_min(self, val)`

#### `def ai_calculated_power_voltage_min(self)`

#### `def ai_charge_units(self)`


        :class:`nidaqmx.constants.ChargeUnits`: Specifies the units to
            use to return charge measurements from the channel.
        

#### `def ai_charge_units(self, val)`

#### `def ai_charge_units(self)`

#### `def ai_chop_enable(self)`


        bool: Specifies whether the device will chop its inputs.
            Chopping removes offset voltages and other low frequency
            errors.
        

#### `def ai_chop_enable(self, val)`

#### `def ai_chop_enable(self)`

#### `def ai_coupling(self)`


        :class:`nidaqmx.constants.Coupling`: Specifies the coupling for
            the channel.
        

#### `def ai_coupling(self, val)`

#### `def ai_coupling(self)`

#### `def ai_current_acrms_units(self)`


        :class:`nidaqmx.constants.CurrentUnits`: Specifies the units to
            use to return current RMS measurements from the channel.
        

#### `def ai_current_acrms_units(self, val)`

#### `def ai_current_acrms_units(self)`

#### `def ai_current_shunt_loc(self)`


        :class:`nidaqmx.constants.CurrentShuntResistorLocation`:
            Specifies the shunt resistor location for current
            measurements.
        

#### `def ai_current_shunt_loc(self, val)`

#### `def ai_current_shunt_loc(self)`

#### `def ai_current_shunt_resistance(self)`


        float: Specifies in ohms the external shunt resistance for
            current measurements.
        

#### `def ai_current_shunt_resistance(self, val)`

#### `def ai_current_shunt_resistance(self)`

#### `def ai_current_units(self)`


        :class:`nidaqmx.constants.CurrentUnits`: Specifies the units to
            use to return current measurements from the channel.
        

#### `def ai_current_units(self, val)`

#### `def ai_current_units(self)`

#### `def ai_custom_scale(self)`


        :class:`nidaqmx.system.scale.Scale`: Specifies the name of a
            custom scale for the channel.
        

#### `def ai_custom_scale(self, val)`

#### `def ai_custom_scale(self)`

#### `def ai_data_xfer_custom_threshold(self)`


        int: Specifies the number of samples that must be in the FIFO to
            transfer data from the device if **ai_data_xfer_req_cond**
            is
            **InputDataTransferCondition.ONBOARD_MEMORY_CUSTOM_THRESHOLD**.
        

#### `def ai_data_xfer_custom_threshold(self, val)`

#### `def ai_data_xfer_custom_threshold(self)`

#### `def ai_data_xfer_max_rate(self)`


        float: Specifies the rate in B/s to transfer data from the
            device. If this value is not set, then the device will
            transfer data at a rate based on the bus detected. Modify
            this value to affect performance under different
            combinations of operating system, configuration, and device.
        

#### `def ai_data_xfer_max_rate(self, val)`

#### `def ai_data_xfer_max_rate(self)`

#### `def ai_data_xfer_mech(self)`


        :class:`nidaqmx.constants.DataTransferActiveTransferMode`:
            Specifies the data transfer mode for the device.
        

#### `def ai_data_xfer_mech(self, val)`

#### `def ai_data_xfer_mech(self)`

#### `def ai_data_xfer_req_cond(self)`


        :class:`nidaqmx.constants.InputDataTransferCondition`: Specifies
            under what condition to transfer data from the onboard
            memory of the device to the buffer.
        

#### `def ai_data_xfer_req_cond(self, val)`

#### `def ai_data_xfer_req_cond(self)`

#### `def ai_dc_offset(self)`


        float: Specifies the DC value to add to the input range of the
            device. Use **ai_rng_high** and **ai_rng_low** to specify
            the input range. This offset is in the native units of the
            device .
        

#### `def ai_dc_offset(self, val)`

#### `def ai_dc_offset(self)`

#### `def ai_dev_scaling_coeff(self)`


        List[float]: Indicates the coefficients of a polynomial equation
            that NI-DAQmx uses to scale values from the native format of
            the device to volts. Each element of the list corresponds to
            a term of the equation. For example, if index two of the
            list is 4, the third term of the equation is 4x^2. Scaling
            coefficients do not account for any custom scales or sensors
            contained by the channel.
        

#### `def ai_dig_fltr_bandpass_center_freq(self)`


        float: Specifies the center frequency of the passband for the
            digital filter.
        

#### `def ai_dig_fltr_bandpass_center_freq(self, val)`

#### `def ai_dig_fltr_bandpass_center_freq(self)`

#### `def ai_dig_fltr_bandpass_width(self)`


        float: Specifies the width of the passband centered around the
            center frequency for the digital filter.
        

#### `def ai_dig_fltr_bandpass_width(self, val)`

#### `def ai_dig_fltr_bandpass_width(self)`

#### `def ai_dig_fltr_coeff(self)`


        List[float]: Specifies the digital filter coefficients.
        

#### `def ai_dig_fltr_coeff(self, val)`

#### `def ai_dig_fltr_coeff(self)`

#### `def ai_dig_fltr_enable(self)`


        bool: Specifies whether the digital filter is enabled or
            disabled.
        

#### `def ai_dig_fltr_enable(self, val)`

#### `def ai_dig_fltr_enable(self)`

#### `def ai_dig_fltr_highpass_cutoff_freq(self)`


        float: Specifies the highpass cutoff frequency of the digital
            filter.
        

#### `def ai_dig_fltr_highpass_cutoff_freq(self, val)`

#### `def ai_dig_fltr_highpass_cutoff_freq(self)`

#### `def ai_dig_fltr_lowpass_cutoff_freq(self)`


        float: Specifies the lowpass cutoff frequency of the digital
            filter.
        

#### `def ai_dig_fltr_lowpass_cutoff_freq(self, val)`

#### `def ai_dig_fltr_lowpass_cutoff_freq(self)`

#### `def ai_dig_fltr_notch_center_freq(self)`


        float: Specifies the center frequency of the stopband for the
            digital filter.
        

#### `def ai_dig_fltr_notch_center_freq(self, val)`

#### `def ai_dig_fltr_notch_center_freq(self)`

#### `def ai_dig_fltr_notch_width(self)`


        float: Specifies the width of the stopband centered around the
            center frequency for the digital filter.
        

#### `def ai_dig_fltr_notch_width(self, val)`

#### `def ai_dig_fltr_notch_width(self)`

#### `def ai_dig_fltr_order(self)`


        int: Specifies the order of the digital filter.
        

#### `def ai_dig_fltr_order(self, val)`

#### `def ai_dig_fltr_order(self)`

#### `def ai_dig_fltr_response(self)`


        :class:`nidaqmx.constants.FilterResponse`: Specifies the digital
            filter response.
        

#### `def ai_dig_fltr_response(self, val)`

#### `def ai_dig_fltr_response(self)`

#### `def ai_dig_fltr_type(self)`


        :class:`nidaqmx.constants.FilterType`: Specifies the digital
            filter type.
        

#### `def ai_dig_fltr_type(self, val)`

#### `def ai_dig_fltr_type(self)`

#### `def ai_dither_enable(self)`


        bool: Specifies whether to enable dithering.  Dithering adds
            Gaussian noise to the input signal. You can use dithering to
            achieve higher resolution measurements by over sampling the
            input signal and averaging the results.
        

#### `def ai_dither_enable(self, val)`

#### `def ai_dither_enable(self)`

#### `def ai_eddy_current_prox_sensitivity(self)`


        float: Specifies the sensitivity of the eddy current proximity
            probe . This value is in the units you specify with
            **ai_eddy_current_prox_sensitivity_units**. Refer to the
            sensor documentation to determine this value.
        

#### `def ai_eddy_current_prox_sensitivity(self, val)`

#### `def ai_eddy_current_prox_sensitivity(self)`

#### `def ai_eddy_current_prox_sensitivity_units(self)`


        :class:`nidaqmx.constants.EddyCurrentProxProbeSensitivityUnits`:
            Specifies the units of **ai_eddy_current_prox_sensitivity**.
        

#### `def ai_eddy_current_prox_sensitivity_units(self, val)`

#### `def ai_eddy_current_prox_sensitivity_units(self)`

#### `def ai_eddy_current_prox_units(self)`


        :class:`nidaqmx.constants.LengthUnits`: Specifies the units to
            use to return proximity measurements from the channel.
        

#### `def ai_eddy_current_prox_units(self, val)`

#### `def ai_eddy_current_prox_units(self)`

#### `def ai_enhanced_alias_rejection_enable(self)`


        bool: Specifies whether to enable enhanced alias rejection.
            Leave this property set to the default value for most
            applications.
        

#### `def ai_enhanced_alias_rejection_enable(self, val)`

#### `def ai_enhanced_alias_rejection_enable(self)`

#### `def ai_excit_actual_val(self)`


        float: Specifies the actual amount of excitation supplied by an
            internal excitation source.  If you read an internal
            excitation source more precisely with an external device,
            set this property to the value you read.  NI-DAQmx ignores
            this value for external excitation. When performing shunt
            calibration, some devices set this property automatically.
        

#### `def ai_excit_actual_val(self, val)`

#### `def ai_excit_actual_val(self)`

#### `def ai_excit_d_cor_ac(self)`


        :class:`nidaqmx.constants.ExcitationDCorAC`: Specifies if the
            excitation supply is DC or AC.
        

#### `def ai_excit_d_cor_ac(self, val)`

#### `def ai_excit_d_cor_ac(self)`

#### `def ai_excit_idle_output_behavior(self)`


        :class:`nidaqmx.constants.ExcitationIdleOutputBehavior`:
            Specifies whether this channel will disable excitation after
            the task is uncommitted. Setting this to Zero Volts or Amps
            disables excitation after task uncommit. Setting this
            attribute to Maintain Existing Value leaves the excitation
            on after task uncommit.
        

#### `def ai_excit_idle_output_behavior(self, val)`

#### `def ai_excit_idle_output_behavior(self)`

#### `def ai_excit_sense(self)`


        :class:`nidaqmx.constants.Sense`: Specifies whether to use local
            or remote sense to sense excitation.
        

#### `def ai_excit_sense(self, val)`

#### `def ai_excit_sense(self)`

#### `def ai_excit_src(self)`


        :class:`nidaqmx.constants.ExcitationSource`: Specifies the
            source of excitation.
        

#### `def ai_excit_src(self, val)`

#### `def ai_excit_src(self)`

#### `def ai_excit_use_for_scaling(self)`


        bool: Specifies if NI-DAQmx divides the measurement by the
            excitation. You should typically set this property to True
            for ratiometric transducers. If you set this property to
            True, set **ai_max** and **ai_min** to reflect the scaling.
        

#### `def ai_excit_use_for_scaling(self, val)`

#### `def ai_excit_use_for_scaling(self)`

#### `def ai_excit_use_multiplexed(self)`


        bool: Specifies if the SCXI-1122 multiplexes the excitation to
            the upper half of the channels as it advances through the
            scan list.
        

#### `def ai_excit_use_multiplexed(self, val)`

#### `def ai_excit_use_multiplexed(self)`

#### `def ai_excit_val(self)`


        float: Specifies the amount of excitation that the sensor
            requires. If **ai_excit_voltage_or_current** is
            **ExcitationVoltageOrCurrent.USE_VOLTAGE**, this value is in
            volts. If **ai_excit_voltage_or_current** is
            **ExcitationVoltageOrCurrent.USE_CURRENT**, this value is in
            amperes.
        

#### `def ai_excit_val(self, val)`

#### `def ai_excit_val(self)`

#### `def ai_excit_voltage_or_current(self)`


        :class:`nidaqmx.constants.ExcitationVoltageOrCurrent`: Specifies
            if the channel uses current or voltage excitation.
        

#### `def ai_excit_voltage_or_current(self, val)`

#### `def ai_excit_voltage_or_current(self)`

#### `def ai_filter_delay(self)`


        float: Indicates the amount of time between when the ADC samples
            data and when the sample is read by the host device. This
            value is in the units you specify with
            **ai_filter_delay_units**. You can adjust this amount of
            time using **ai_filter_delay_adjustment**.
        

#### `def ai_filter_delay_adjustment(self)`


        float: Specifies the amount of filter delay that gets removed if
            **ai_remove_filter_delay** is enabled. This delay adjustment
            is in addition to the value indicated by
            **ai_filter_delay**. This delay adjustment is in the units
            you specify with **ai_filter_delay_units**.
        

#### `def ai_filter_delay_adjustment(self, val)`

#### `def ai_filter_delay_adjustment(self)`

#### `def ai_filter_delay_units(self)`


        :class:`nidaqmx.constants.DigitalWidthUnits`: Specifies the
            units of **ai_filter_delay** and
            **ai_filter_delay_adjustment**.
        

#### `def ai_filter_delay_units(self, val)`

#### `def ai_filter_delay_units(self)`

#### `def ai_filter_enable(self)`


        bool: Specifies the corresponding filter enable/disable state.
        

#### `def ai_filter_enable(self, val)`

#### `def ai_filter_enable(self)`

#### `def ai_filter_freq(self)`


        float: Specifies the corresponding filter frequency (cutoff or
            center) of the filter response.
        

#### `def ai_filter_freq(self, val)`

#### `def ai_filter_freq(self)`

#### `def ai_filter_order(self)`


        int: Specifies the corresponding filter order and defines the
            slope of the filter response.
        

#### `def ai_filter_order(self, val)`

#### `def ai_filter_order(self)`

#### `def ai_filter_response(self)`


        :class:`nidaqmx.constants.FilterResponse`: Specifies the
            corresponding filter response and defines the shape of the
            filter response.
        

#### `def ai_filter_response(self, val)`

#### `def ai_filter_response(self)`

#### `def ai_force_iepe_sensor_sensitivity(self)`


        float: Specifies the sensitivity of the IEPE force sensor
            connected to the channel. Specify this value in the unit
            indicated by **ai_force_iepe_sensor_sensitivity_units**.
        

#### `def ai_force_iepe_sensor_sensitivity(self, val)`

#### `def ai_force_iepe_sensor_sensitivity(self)`

#### `def ai_force_iepe_sensor_sensitivity_units(self)`


        :class:`nidaqmx.constants.ForceIEPESensorSensitivityUnits`:
            Specifies the units for
            **ai_force_iepe_sensor_sensitivity**.
        

#### `def ai_force_iepe_sensor_sensitivity_units(self, val)`

#### `def ai_force_iepe_sensor_sensitivity_units(self)`

#### `def ai_force_read_from_chan(self)`


        bool: Specifies whether to read from the channel if it is a
            cold-junction compensation channel. By default, DAQmx Read
            does not return data from cold-junction compensation
            channels.  Setting this property to True forces read
            operations to return the cold-junction compensation channel
            data with the other channels in the task.
        

#### `def ai_force_read_from_chan(self, val)`

#### `def ai_force_read_from_chan(self)`

#### `def ai_force_units(self)`


        :class:`nidaqmx.constants.ForceUnits`: Specifies in which unit
            to return force or load measurements from the channel.
        

#### `def ai_force_units(self, val)`

#### `def ai_force_units(self)`

#### `def ai_freq_hyst(self)`


        float: Specifies in volts a window below
            **ai_freq_thresh_voltage**. The input voltage must pass
            below **ai_freq_thresh_voltage** minus this value before NI-
            DAQmx recognizes a waveform repetition at
            **ai_freq_thresh_voltage**. Hysteresis can improve the
            measurement accuracy when the signal contains noise or
            jitter.
        

#### `def ai_freq_hyst(self, val)`

#### `def ai_freq_hyst(self)`

#### `def ai_freq_thresh_voltage(self)`


        float: Specifies the voltage level at which to recognize
            waveform repetitions. You should select a voltage level that
            occurs only once within the entire period of a waveform. You
            also can select a voltage that occurs only once while the
            voltage rises or falls.
        

#### `def ai_freq_thresh_voltage(self, val)`

#### `def ai_freq_thresh_voltage(self)`

#### `def ai_freq_units(self)`


        :class:`nidaqmx.constants.FrequencyUnits`: Specifies the units
            to use to return frequency measurements from the channel.
        

#### `def ai_freq_units(self, val)`

#### `def ai_freq_units(self)`

#### `def ai_gain(self)`


        float: Specifies a gain factor to apply to the channel.
        

#### `def ai_gain(self, val)`

#### `def ai_gain(self)`

#### `def ai_impedance(self)`


        :class:`nidaqmx.constants.Impedance1`: Specifies the input
            impedance of the channel.
        

#### `def ai_impedance(self, val)`

#### `def ai_impedance(self)`

#### `def ai_input_limits_fault_detect_enable(self)`


        bool: Specifies whether to enable input limits fault detection.
        

#### `def ai_input_limits_fault_detect_enable(self, val)`

#### `def ai_input_limits_fault_detect_enable(self)`

#### `def ai_input_limits_fault_detect_lower_limit(self)`


        float: Specifies the level of the lower limit for input limits
            detection. An input sample outside the upper and lower
            bounds causes a fault. Note: Fault detection applies to both
            positive and negative inputs. For instance, if you specify a
            lower limit of 2 mA and an upper limit of 12 mA, NI-DAQmx
            detects a fault at 15 mA and -15 mA, but not at -6 mA
            because it is in the range of -12 mA to -2 mA.
        

#### `def ai_input_limits_fault_detect_lower_limit(self, val)`

#### `def ai_input_limits_fault_detect_lower_limit(self)`

#### `def ai_input_limits_fault_detect_upper_limit(self)`


        float: Specifies the level of the upper limit for input limits
            detection. An input sample outside the upper and lower
            bounds causes a fault. Note: Fault detection applies to both
            positive and negative inputs. For instance, if you specify a
            lower limit of 2 mA and an upper limit of 12 mA, NI-DAQmx
            detects a fault at 15 mA and -15 mA, but not at -6 mA
            because it is in the range of -12 mA to -2 mA.
        

#### `def ai_input_limits_fault_detect_upper_limit(self, val)`

#### `def ai_input_limits_fault_detect_upper_limit(self)`

#### `def ai_input_src(self)`


        str: Specifies the source of the channel. You can use the signal
            from the I/O connector or one of several calibration
            signals. Certain devices have a single calibration signal
            bus. For these devices, you must specify the same
            calibration signal for all channels you connect to a
            calibration signal.
        

#### `def ai_input_src(self, val)`

#### `def ai_input_src(self)`

#### `def ai_lead_wire_resistance(self)`


        float: Specifies in ohms the resistance of the wires that lead
            to the sensor.
        

#### `def ai_lead_wire_resistance(self, val)`

#### `def ai_lead_wire_resistance(self)`

#### `def ai_lossy_lsb_removal_compressed_samp_size(self)`


        int: Specifies the number of bits to return in a raw sample when
            **ai_raw_data_compression_type** is set to
            **RawDataCompressionType.LOSSY_LSB_REMOVAL**.
        

#### `def ai_lossy_lsb_removal_compressed_samp_size(self, val)`

#### `def ai_lossy_lsb_removal_compressed_samp_size(self)`

#### `def ai_lowpass_cutoff_freq(self)`


        float: Specifies the frequency in Hertz that corresponds to the
            -3dB cutoff of the filter.
        

#### `def ai_lowpass_cutoff_freq(self, val)`

#### `def ai_lowpass_cutoff_freq(self)`

#### `def ai_lowpass_enable(self)`


        bool: Specifies whether to enable the lowpass filter of the
            channel.
        

#### `def ai_lowpass_enable(self, val)`

#### `def ai_lowpass_enable(self)`

#### `def ai_lowpass_switch_cap_clk_src(self)`


        :class:`nidaqmx.constants.SourceSelection`: Specifies the source
            of the filter clock. If you need a higher resolution for the
            filter, you can supply an external clock to increase the
            resolution. Refer to the SCXI-1141/1142/1143 User Manual for
            more information.
        

#### `def ai_lowpass_switch_cap_clk_src(self, val)`

#### `def ai_lowpass_switch_cap_clk_src(self)`

#### `def ai_lowpass_switch_cap_ext_clk_div(self)`


        int: Specifies the divisor for the external clock when you set
            **ai_lowpass_switch_cap_clk_src** to
            **SourceSelection.EXTERNAL**. On the SCXI-1141, SCXI-1142,
            and SCXI-1143, NI-DAQmx determines the filter cutoff by
            using the equation f/(100*n), where f is the external
            frequency, and n is the external clock divisor. Refer to the
            SCXI-1141/1142/1143 User Manual for more information.
        

#### `def ai_lowpass_switch_cap_ext_clk_div(self, val)`

#### `def ai_lowpass_switch_cap_ext_clk_div(self)`

#### `def ai_lowpass_switch_cap_ext_clk_freq(self)`


        float: Specifies the frequency of the external clock when you
            set **ai_lowpass_switch_cap_clk_src** to
            **SourceSelection.EXTERNAL**.  NI-DAQmx uses this frequency
            to set the pre- and post- filters on the SCXI-1141,
            SCXI-1142, and SCXI-1143. On those devices, NI-DAQmx
            determines the filter cutoff by using the equation
            f/(100*n), where f is the external frequency, and n is the
            external clock divisor. Refer to the SCXI-1141/1142/1143
            User Manual for more information.
        

#### `def ai_lowpass_switch_cap_ext_clk_freq(self, val)`

#### `def ai_lowpass_switch_cap_ext_clk_freq(self)`

#### `def ai_lowpass_switch_cap_out_clk_div(self)`


        int: Specifies the divisor for the output clock.  NI-DAQmx uses
            the cutoff frequency to determine the output clock
            frequency. Refer to the SCXI-1141/1142/1143 User Manual for
            more information.
        

#### `def ai_lowpass_switch_cap_out_clk_div(self, val)`

#### `def ai_lowpass_switch_cap_out_clk_div(self)`

#### `def ai_lvdt_sensitivity(self)`


        float: Specifies the sensitivity of the LVDT. This value is in
            the units you specify with **ai_lvdt_sensitivity_units**.
            Refer to the sensor documentation to determine this value.
        

#### `def ai_lvdt_sensitivity(self, val)`

#### `def ai_lvdt_sensitivity(self)`

#### `def ai_lvdt_sensitivity_units(self)`


        :class:`nidaqmx.constants.LVDTSensitivityUnits`: Specifies the
            units of **ai_lvdt_sensitivity**.
        

#### `def ai_lvdt_sensitivity_units(self, val)`

#### `def ai_lvdt_sensitivity_units(self)`

#### `def ai_lvdt_units(self)`


        :class:`nidaqmx.constants.LengthUnits`: Specifies the units to
            use to return linear position measurements from the channel.
        

#### `def ai_lvdt_units(self, val)`

#### `def ai_lvdt_units(self)`

#### `def ai_max(self)`


        float: Specifies the maximum value you expect to measure. This
            value is in the units you specify with a units property.
            When you query this property, it returns the coerced maximum
            value that the device can measure with the current settings.
        

#### `def ai_max(self, val)`

#### `def ai_max(self)`

#### `def ai_meas_type(self)`


        :class:`nidaqmx.constants.UsageTypeAI`: Indicates the
            measurement to take with the analog input channel and in
            some cases, such as for temperature measurements, the sensor
            to use.
        

#### `def ai_mem_map_enable(self)`


        bool: Specifies for NI-DAQmx to map hardware registers to the
            memory space of the application, if possible. Normally, NI-
            DAQmx maps hardware registers to memory accessible only to
            the kernel. Mapping the registers to the memory space of the
            application increases performance. However, if the
            application accesses the memory space mapped to the
            registers, it can adversely affect the operation of the
            device and possibly result in a system crash.
        

#### `def ai_mem_map_enable(self, val)`

#### `def ai_mem_map_enable(self)`

#### `def ai_microphone_sensitivity(self)`


        float: Specifies the sensitivity of the microphone. This value
            is in mV/Pa. Refer to the sensor documentation to determine
            this value.
        

#### `def ai_microphone_sensitivity(self, val)`

#### `def ai_microphone_sensitivity(self)`

#### `def ai_min(self)`


        float: Specifies the minimum value you expect to measure. This
            value is in the units you specify with a units property.
            When you query this property, it returns the coerced minimum
            value that the device can measure with the current settings.
        

#### `def ai_min(self, val)`

#### `def ai_min(self)`

#### `def ai_open_chan_detect_enable(self)`


        bool: Specifies whether to enable open channel detection.
        

#### `def ai_open_chan_detect_enable(self, val)`

#### `def ai_open_chan_detect_enable(self)`

#### `def ai_open_thrmcpl_detect_enable(self)`


        bool: Specifies whether to apply the open thermocouple detection
            bias voltage to the channel. Changing the value of this
            property on a channel may require settling time before the
            data returned is valid. To compensate for this settling
            time, discard unsettled data or add a delay between
            committing and starting the task. Refer to your device
            specifications for the required settling time. When open
            thermocouple detection is enabled, use
            **open_thrmcpl_chans_exist** to determine if any channels
            were open.
        

#### `def ai_open_thrmcpl_detect_enable(self, val)`

#### `def ai_open_thrmcpl_detect_enable(self)`

#### `def ai_overcurrent_detect_enable(self)`


        bool: Specifies whether to enable overcurrent detection.
        

#### `def ai_overcurrent_detect_enable(self, val)`

#### `def ai_overcurrent_detect_enable(self)`

#### `def ai_power_supply_fault_detect_enable(self)`


        bool: Specifies whether to enable power supply fault detection.
        

#### `def ai_power_supply_fault_detect_enable(self, val)`

#### `def ai_power_supply_fault_detect_enable(self)`

#### `def ai_power_units(self)`


        :class:`nidaqmx.constants.PowerUnits`: Specifies the units to
            use to return power measurements from the channel.
        

#### `def ai_power_units(self, val)`

#### `def ai_power_units(self)`

#### `def ai_pressure_units(self)`


        :class:`nidaqmx.constants.PressureUnits`: Specifies  in which
            unit to return pressure measurements from the channel.
        

#### `def ai_pressure_units(self, val)`

#### `def ai_pressure_units(self)`

#### `def ai_probe_atten(self)`


        float: Specifies the amount of attenuation provided by the probe
            connected to the channel. Specify this attenuation as a
            ratio.
        

#### `def ai_probe_atten(self, val)`

#### `def ai_probe_atten(self)`

#### `def ai_raw_data_compression_type(self)`


        :class:`nidaqmx.constants.RawDataCompressionType`: Specifies the
            type of compression to apply to raw samples returned from
            the device.
        

#### `def ai_raw_data_compression_type(self, val)`

#### `def ai_raw_data_compression_type(self)`

#### `def ai_raw_samp_justification(self)`


        :class:`nidaqmx.constants.DataJustification`: Indicates the
            justification of a raw sample from the device.
        

#### `def ai_raw_samp_size(self)`


        int: Indicates in bits the size of a raw sample from the device.
        

#### `def ai_remove_filter_delay(self)`


        bool: Specifies if filter delay removal is enabled on the
            device.
        

#### `def ai_remove_filter_delay(self, val)`

#### `def ai_remove_filter_delay(self)`

#### `def ai_resistance_cfg(self)`


        :class:`nidaqmx.constants.ResistanceConfiguration`: Specifies
            the resistance configuration for the channel. NI-DAQmx uses
            this value for any resistance-based measurements, including
            temperature measurement using a thermistor or RTD.
        

#### `def ai_resistance_cfg(self, val)`

#### `def ai_resistance_cfg(self)`

#### `def ai_resistance_units(self)`


        :class:`nidaqmx.constants.ResistanceUnits`: Specifies the units
            to use to return resistance measurements.
        

#### `def ai_resistance_units(self, val)`

#### `def ai_resistance_units(self)`

#### `def ai_resolution(self)`


        float: Indicates the resolution of the analog-to-digital
            converter of the channel. This value is in the units you
            specify with **ai_resolution_units**.
        

#### `def ai_resolution_units(self)`


        :class:`nidaqmx.constants.ResolutionType`: Indicates the units
            of **ai_resolution**.
        

#### `def ai_rng_high(self)`


        float: Specifies the upper limit of the input range of the
            device. This value is in the native units of the device. On
            E Series devices, for example, the native units is volts.
        

#### `def ai_rng_high(self, val)`

#### `def ai_rng_high(self)`

#### `def ai_rng_low(self)`


        float: Specifies the lower limit of the input range of the
            device. This value is in the native units of the device. On
            E Series devices, for example, the native units is volts.
        

#### `def ai_rng_low(self, val)`

#### `def ai_rng_low(self)`

#### `def ai_rosette_strain_gage_gage_orientation(self)`


        float: Specifies gage orientation in degrees with respect to the
            X axis.
        

#### `def ai_rosette_strain_gage_gage_orientation(self, val)`

#### `def ai_rosette_strain_gage_gage_orientation(self)`

#### `def ai_rosette_strain_gage_rosette_meas_type(self)`


        :class:`nidaqmx.constants.StrainGageRosetteMeasurementType`:
            Specifies the type of rosette measurement.
        

#### `def ai_rosette_strain_gage_rosette_meas_type(self, val)`

#### `def ai_rosette_strain_gage_rosette_meas_type(self)`

#### `def ai_rosette_strain_gage_rosette_type(self)`


        :class:`nidaqmx.constants.StrainGageRosetteType`: Indicates the
            type of rosette gage.
        

#### `def ai_rosette_strain_gage_strain_chans(self)`


        List[str]: Indicates the raw strain channels that comprise the
            strain rosette.
        

#### `def ai_rtd_a(self)`


        float: Specifies the 'A' constant of the Callendar-Van Dusen
            equation. NI-DAQmx requires this value when you use a custom
            RTD.
        

#### `def ai_rtd_a(self, val)`

#### `def ai_rtd_a(self)`

#### `def ai_rtd_b(self)`


        float: Specifies the 'B' constant of the Callendar-Van Dusen
            equation. NI-DAQmx requires this value when you use a custom
            RTD.
        

#### `def ai_rtd_b(self, val)`

#### `def ai_rtd_b(self)`

#### `def ai_rtd_c(self)`


        float: Specifies the 'C' constant of the Callendar-Van Dusen
            equation. NI-DAQmx requires this value when you use a custom
            RTD.
        

#### `def ai_rtd_c(self, val)`

#### `def ai_rtd_c(self)`

#### `def ai_rtd_r0(self)`


        float: Specifies in ohms the sensor resistance at 0 deg C. The
            Callendar-Van Dusen equation requires this value. Refer to
            the sensor documentation to determine this value.
        

#### `def ai_rtd_r0(self, val)`

#### `def ai_rtd_r0(self)`

#### `def ai_rtd_type(self)`


        :class:`nidaqmx.constants.RTDType`: Specifies the type of RTD
            connected to the channel.
        

#### `def ai_rtd_type(self, val)`

#### `def ai_rtd_type(self)`

#### `def ai_rvdt_sensitivity(self)`


        float: Specifies the sensitivity of the RVDT. This value is in
            the units you specify with **ai_rvdt_sensitivity_units**.
            Refer to the sensor documentation to determine this value.
        

#### `def ai_rvdt_sensitivity(self, val)`

#### `def ai_rvdt_sensitivity(self)`

#### `def ai_rvdt_sensitivity_units(self)`


        :class:`nidaqmx.constants.RVDTSensitivityUnits`: Specifies the
            units of **ai_rvdt_sensitivity**.
        

#### `def ai_rvdt_sensitivity_units(self, val)`

#### `def ai_rvdt_sensitivity_units(self)`

#### `def ai_rvdt_units(self)`


        :class:`nidaqmx.constants.AngleUnits`: Specifies the units to
            use to return angular position measurements from the
            channel.
        

#### `def ai_rvdt_units(self, val)`

#### `def ai_rvdt_units(self)`

#### `def ai_samp_and_hold_enable(self)`


        bool: Specifies whether to enable the sample and hold circuitry
            of the device. When you disable sample and hold circuitry, a
            small voltage offset might be introduced into the signal.
            You can eliminate this offset by using **ai_auto_zero_mode**
            to perform an auto zero on the channel.
        

#### `def ai_samp_and_hold_enable(self, val)`

#### `def ai_samp_and_hold_enable(self)`

#### `def ai_sensor_power_cfg(self)`


        :class:`nidaqmx.constants.SensorPowerCfg`: Specifies whether to
            turn on the sensor's power supply or to leave the
            configuration unchanged.
        

#### `def ai_sensor_power_cfg(self, val)`

#### `def ai_sensor_power_cfg(self)`

#### `def ai_sensor_power_type(self)`


        :class:`nidaqmx.constants.SensorPowerType`: Specifies the type
            of power supplied to the sensor.
        

#### `def ai_sensor_power_type(self, val)`

#### `def ai_sensor_power_type(self)`

#### `def ai_sensor_power_voltage(self)`


        float: Specifies the voltage level for the sensor's power
            supply.
        

#### `def ai_sensor_power_voltage(self, val)`

#### `def ai_sensor_power_voltage(self)`

#### `def ai_sound_pressure_db_ref(self)`


        float: Specifies the decibel reference level in the units of the
            channel. When you read samples as a waveform, the decibel
            reference level is included in the waveform attributes. NI-
            DAQmx also uses the decibel reference level when converting
            **ai_sound_pressure_max_sound_pressure_lvl** to a voltage
            level.
        

#### `def ai_sound_pressure_db_ref(self, val)`

#### `def ai_sound_pressure_db_ref(self)`

#### `def ai_sound_pressure_max_sound_pressure_lvl(self)`


        float: Specifies the maximum instantaneous sound pressure level
            you expect to measure. This value is in decibels, referenced
            to 20 micropascals. NI-DAQmx uses the maximum sound pressure
            level to calculate values in pascals for **ai_max** and
            **ai_min** for the channel.
        

#### `def ai_sound_pressure_max_sound_pressure_lvl(self, val)`

#### `def ai_sound_pressure_max_sound_pressure_lvl(self)`

#### `def ai_sound_pressure_units(self)`


        :class:`nidaqmx.constants.SoundPressureUnits`: Specifies the
            units to use to return sound pressure measurements from the
            channel.
        

#### `def ai_sound_pressure_units(self, val)`

#### `def ai_sound_pressure_units(self)`

#### `def ai_strain_force_read_from_chan(self)`


        bool: Specifies whether the data is returned by DAQmx Read when
            set on a raw strain channel that is part of a rosette
            configuration.
        

#### `def ai_strain_force_read_from_chan(self, val)`

#### `def ai_strain_force_read_from_chan(self)`

#### `def ai_strain_gage_cfg(self)`


        :class:`nidaqmx.constants.StrainGageBridgeType`: Specifies the
            bridge configuration of the strain gages.
        

#### `def ai_strain_gage_cfg(self, val)`

#### `def ai_strain_gage_cfg(self)`

#### `def ai_strain_gage_gage_factor(self)`


        float: Specifies the sensitivity of the strain gage.  Gage
            factor relates the change in electrical resistance to the
            change in strain. Refer to the sensor documentation for this
            value.
        

#### `def ai_strain_gage_gage_factor(self, val)`

#### `def ai_strain_gage_gage_factor(self)`

#### `def ai_strain_gage_poisson_ratio(self)`


        float: Specifies the ratio of lateral strain to axial strain in
            the material you are measuring.
        

#### `def ai_strain_gage_poisson_ratio(self, val)`

#### `def ai_strain_gage_poisson_ratio(self)`

#### `def ai_strain_units(self)`


        :class:`nidaqmx.constants.StrainUnits`: Specifies the units to
            use to return strain measurements from the channel.
        

#### `def ai_strain_units(self, val)`

#### `def ai_strain_units(self)`

#### `def ai_teds_is_teds(self)`


        bool: Indicates if the virtual channel was initialized using a
            TEDS bitstream from the corresponding physical channel.
        

#### `def ai_teds_units(self)`


        str: Indicates the units defined by TEDS information associated
            with the channel.
        

#### `def ai_temp_units(self)`


        :class:`nidaqmx.constants.TemperatureUnits`: Specifies the units
            to use to return temperature measurements from the channel.
        

#### `def ai_temp_units(self, val)`

#### `def ai_temp_units(self)`

#### `def ai_term_cfg(self)`


        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            terminal configuration for the channel.
        

#### `def ai_term_cfg(self, val)`

#### `def ai_term_cfg(self)`

#### `def ai_thrmcpl_cjc_chan(self)`


        :class:`nidaqmx.task.channels.Channel`: Indicates the channel
            that acquires the temperature of the cold junction if
            **ai_thrmcpl_cjc_src** is **CJCSource1.SCANNABLE_CHANNEL**.
            If the channel is a temperature channel, NI-DAQmx acquires
            the temperature in the correct units. Other channel types,
            such as a resistance channel with a custom sensor, must use
            a custom scale to scale values to degrees Celsius.
        

#### `def ai_thrmcpl_cjc_src(self)`


        :class:`nidaqmx.constants.CJCSource`: Indicates the source of
            cold-junction compensation.
        

#### `def ai_thrmcpl_cjc_val(self)`


        float: Specifies the temperature of the cold junction if
            **ai_thrmcpl_cjc_src** is
            **CJCSource1.CONSTANT_USER_VALUE**. Specify this value in
            the units of the measurement.
        

#### `def ai_thrmcpl_cjc_val(self, val)`

#### `def ai_thrmcpl_cjc_val(self)`

#### `def ai_thrmcpl_lead_offset_voltage(self)`


        float: Specifies the lead offset nulling voltage to subtract
            from measurements on a device. This property is ignored if
            open thermocouple detection is disabled.
        

#### `def ai_thrmcpl_lead_offset_voltage(self, val)`

#### `def ai_thrmcpl_lead_offset_voltage(self)`

#### `def ai_thrmcpl_scale_type(self)`


        :class:`nidaqmx.constants.ScaleType`: Specifies the method or
            equation form that the thermocouple scale uses.
        

#### `def ai_thrmcpl_scale_type(self, val)`

#### `def ai_thrmcpl_scale_type(self)`

#### `def ai_thrmcpl_type(self)`


        :class:`nidaqmx.constants.ThermocoupleType`: Specifies the type
            of thermocouple connected to the channel. Thermocouple types
            differ in composition and measurement range.
        

#### `def ai_thrmcpl_type(self, val)`

#### `def ai_thrmcpl_type(self)`

#### `def ai_thrmstr_a(self)`


        float: Specifies the 'A' constant of the Steinhart-Hart
            thermistor equation.
        

#### `def ai_thrmstr_a(self, val)`

#### `def ai_thrmstr_a(self)`

#### `def ai_thrmstr_b(self)`


        float: Specifies the 'B' constant of the Steinhart-Hart
            thermistor equation.
        

#### `def ai_thrmstr_b(self, val)`

#### `def ai_thrmstr_b(self)`

#### `def ai_thrmstr_c(self)`


        float: Specifies the 'C' constant of the Steinhart-Hart
            thermistor equation.
        

#### `def ai_thrmstr_c(self, val)`

#### `def ai_thrmstr_c(self)`

#### `def ai_thrmstr_r1(self)`


        float: Specifies in ohms the value of the reference resistor for
            the thermistor if you use voltage excitation. NI-DAQmx
            ignores this value for current excitation.
        

#### `def ai_thrmstr_r1(self, val)`

#### `def ai_thrmstr_r1(self)`

#### `def ai_torque_units(self)`


        :class:`nidaqmx.constants.TorqueUnits`: Specifies in which unit
            to return torque measurements from the channel.
        

#### `def ai_torque_units(self, val)`

#### `def ai_torque_units(self)`

#### `def ai_usb_xfer_req_count(self)`


        int: Specifies the maximum number of simultaneous USB transfers
            used to stream data. Modify this value to affect performance
            under different combinations of operating system and device.
        

#### `def ai_usb_xfer_req_count(self, val)`

#### `def ai_usb_xfer_req_count(self)`

#### `def ai_usb_xfer_req_size(self)`


        int: Specifies the maximum size of a USB transfer request in
            bytes. Modify this value to affect performance under
            different combinations of operating system and device.
        

#### `def ai_usb_xfer_req_size(self, val)`

#### `def ai_usb_xfer_req_size(self)`

#### `def ai_velocity_iepe_sensor_db_ref(self)`


        float: Specifies the decibel reference level in the units of the
            channel. When you read samples as a waveform, the decibel
            reference level is included in the waveform attributes.
        

#### `def ai_velocity_iepe_sensor_db_ref(self, val)`

#### `def ai_velocity_iepe_sensor_db_ref(self)`

#### `def ai_velocity_iepe_sensor_sensitivity(self)`


        float: Specifies the sensitivity of the IEPE velocity sensor
            connected to the channel. Specify this value in the unit
            indicated by **ai_velocity_iepe_sensor_sensitivity_units**.
        

#### `def ai_velocity_iepe_sensor_sensitivity(self, val)`

#### `def ai_velocity_iepe_sensor_sensitivity(self)`

#### `def ai_velocity_iepe_sensor_sensitivity_units(self)`


        :class:`nidaqmx.constants.VelocityIEPESensorSensitivityUnits`:
            Specifies the units for
            **ai_velocity_iepe_sensor_sensitivity**.
        

#### `def ai_velocity_iepe_sensor_sensitivity_units(self, val)`

#### `def ai_velocity_iepe_sensor_sensitivity_units(self)`

#### `def ai_velocity_units(self)`


        :class:`nidaqmx.constants.VelocityUnits`: Specifies in which
            unit to return velocity measurements from the channel.
        

#### `def ai_velocity_units(self, val)`

#### `def ai_velocity_units(self)`

#### `def ai_voltage_acrms_units(self)`


        :class:`nidaqmx.constants.VoltageUnits`: Specifies the units to
            use to return voltage RMS measurements from the channel.
        

#### `def ai_voltage_acrms_units(self, val)`

#### `def ai_voltage_acrms_units(self)`

#### `def ai_voltage_db_ref(self)`


        float: Specifies the decibel reference level in the units of the
            channel. When you read samples as a waveform, the decibel
            reference level is included in the waveform attributes.
        

#### `def ai_voltage_db_ref(self, val)`

#### `def ai_voltage_db_ref(self)`

#### `def ai_voltage_units(self)`


        :class:`nidaqmx.constants.VoltageUnits`: Specifies the units to
            use to return voltage measurements from the channel.
        

#### `def ai_voltage_units(self, val)`

#### `def ai_voltage_units(self)`

#### `def pwr_current_dev_scaling_coeff(self)`


        List[float]: Indicates the coefficients of the polynomial
            equation that NI-DAQmx uses to scale values from the native
            format of the device to amperes. Can be read at any time
            during a task.
        

#### `def pwr_current_setpoint(self)`


        float: Specifies the output current, in amperes. If the load
            draws current greater than the specified value, the device
            will operate in Constant Current mode.
        

#### `def pwr_current_setpoint(self, val)`

#### `def pwr_current_setpoint(self)`

#### `def pwr_idle_output_behavior(self)`


        :class:`nidaqmx.constants.PowerIdleOutputBehavior`: Specifies
            whether to disable the output or maintain the existing value
            after the task is uncommitted.
        

#### `def pwr_idle_output_behavior(self, val)`

#### `def pwr_idle_output_behavior(self)`

#### `def pwr_output_enable(self)`


        bool: Specifies whether to enable or disable power module
            output. Can be set while a task is running. Can be read at
            any time during a task. When a task is running, the output
            is enabled immediately. Otherwise, the output is not enabled
            until the task enters the Committed state.
        

#### `def pwr_output_enable(self, val)`

#### `def pwr_output_enable(self)`

#### `def pwr_output_state(self)`


        :class:`nidaqmx.constants.PowerOutputState`: Indicates power
            channel operating state. Can be read at any time during a
            task.
        

#### `def pwr_remote_sense(self)`


        :class:`nidaqmx.constants.Sense`: Specifies whether to use local
            or remote sense to sense the output voltage. DAQmx Read
            (Power Supply) will return remote or local voltage based on
            the Remote Sense attribute value. Reading this property will
            return the user-defined value.
        

#### `def pwr_remote_sense(self, val)`

#### `def pwr_remote_sense(self)`

#### `def pwr_voltage_dev_scaling_coeff(self)`


        List[float]: Indicates the coefficients of the polynomial
            equation that NI-DAQmx uses to scale values from the native
            format of the device to volts. Can be read at any time
            during a task.
        

#### `def pwr_voltage_setpoint(self)`


        float: Specifies the constant output voltage, in volts. Can be
            set while a task is running. Can be read at any time during
            a task.
        

#### `def pwr_voltage_setpoint(self, val)`

#### `def pwr_voltage_setpoint(self)`

#### `def ai_rtd_r_0(self)`

#### `def ai_rtd_r_0(self, val)`

#### `def ai_rtd_r_0(self)`

#### `def ai_sound_pressured_b_ref(self)`

#### `def ai_sound_pressured_b_ref(self, val)`

#### `def ai_sound_pressured_b_ref(self)`

#### `def ai_thrmstr_r_1(self)`

#### `def ai_thrmstr_r_1(self, val)`

#### `def ai_thrmstr_r_1(self)`

#### `def ai_acceld_b_ref(self)`

#### `def ai_acceld_b_ref(self, val)`

#### `def ai_acceld_b_ref(self)`

#### `def ai_voltaged_b_ref(self)`

#### `def ai_voltaged_b_ref(self, val)`

#### `def ai_voltaged_b_ref(self)`

#### `def ai_velocity_iepe_sensord_b_ref(self)`

#### `def ai_velocity_iepe_sensord_b_ref(self, val)`

#### `def ai_velocity_iepe_sensord_b_ref(self)`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/channels/_ao_channel.py -->
## PYTHON MODULE: generated/nidaqmx/task/channels/_ao_channel.py

### `class AOChannel(Channel)`


    Represents one or more analog output virtual channels and their properties.
    

#### `def __repr__(self)`

#### `def ao_common_mode_offset(self)`


        float: Specifies the common-mode offset of the AO channel. Use
            the property only when Terminal Configuration is set to
            Differential.
        

#### `def ao_common_mode_offset(self, val)`

#### `def ao_common_mode_offset(self)`

#### `def ao_current_units(self)`


        :class:`nidaqmx.constants.CurrentUnits`: Specifies in what units
            to generate current on the channel. Write data to the
            channel in the units you select.
        

#### `def ao_current_units(self, val)`

#### `def ao_current_units(self)`

#### `def ao_custom_scale(self)`


        :class:`nidaqmx.system.scale.Scale`: Specifies the name of a
            custom scale for the channel.
        

#### `def ao_custom_scale(self, val)`

#### `def ao_custom_scale(self)`

#### `def ao_dac_offset_ext_src(self)`


        str: Specifies the source of the DAC offset voltage if
            **ao_dac_offset_src** is **SourceSelection.EXTERNAL**. The
            valid sources for this signal vary by device.
        

#### `def ao_dac_offset_ext_src(self, val)`

#### `def ao_dac_offset_ext_src(self)`

#### `def ao_dac_offset_src(self)`


        :class:`nidaqmx.constants.SourceSelection`: Specifies the source
            of the DAC offset voltage. The value of this voltage source
            determines the full-scale value of the DAC.
        

#### `def ao_dac_offset_src(self, val)`

#### `def ao_dac_offset_src(self)`

#### `def ao_dac_offset_val(self)`


        float: Specifies in volts the value of the DAC offset voltage.
            To achieve best accuracy, the DAC offset value should be
            hand calibrated.
        

#### `def ao_dac_offset_val(self, val)`

#### `def ao_dac_offset_val(self)`

#### `def ao_dac_ref_allow_conn_to_gnd(self)`


        bool: Specifies whether to allow grounding the internal DAC
            reference at run time. You must set this property to True
            and set **ao_dac_ref_src** to **SourceSelection.INTERNAL**
            before you can set **ao_dac_ref_conn_to_gnd** to True.
        

#### `def ao_dac_ref_allow_conn_to_gnd(self, val)`

#### `def ao_dac_ref_allow_conn_to_gnd(self)`

#### `def ao_dac_ref_conn_to_gnd(self)`


        bool: Specifies whether to ground the internal DAC reference.
            Grounding the internal DAC reference has the effect of
            grounding all analog output channels and stopping waveform
            generation across all analog output channels regardless of
            whether the channels belong to the current task. You can
            ground the internal DAC reference only when
            **ao_dac_ref_src** is **SourceSelection.INTERNAL** and
            **ao_dac_ref_allow_conn_to_gnd** is True.
        

#### `def ao_dac_ref_conn_to_gnd(self, val)`

#### `def ao_dac_ref_conn_to_gnd(self)`

#### `def ao_dac_ref_ext_src(self)`


        str: Specifies the source of the DAC reference voltage if
            **ao_dac_ref_src** is **SourceSelection.EXTERNAL**. The
            valid sources for this signal vary by device.
        

#### `def ao_dac_ref_ext_src(self, val)`

#### `def ao_dac_ref_ext_src(self)`

#### `def ao_dac_ref_src(self)`


        :class:`nidaqmx.constants.SourceSelection`: Specifies the source
            of the DAC reference voltage. The value of this voltage
            source determines the full-scale value of the DAC.
        

#### `def ao_dac_ref_src(self, val)`

#### `def ao_dac_ref_src(self)`

#### `def ao_dac_ref_val(self)`


        float: Specifies in volts the value of the DAC reference
            voltage. This voltage determines the full-scale range of the
            DAC. Smaller reference voltages result in smaller ranges,
            but increased resolution.
        

#### `def ao_dac_ref_val(self, val)`

#### `def ao_dac_ref_val(self)`

#### `def ao_dac_rng_high(self)`


        float: Specifies the upper limit of the output range of the
            device. This value is in the native units of the device. On
            E Series devices, for example, the native units is volts.
        

#### `def ao_dac_rng_high(self, val)`

#### `def ao_dac_rng_high(self)`

#### `def ao_dac_rng_low(self)`


        float: Specifies the lower limit of the output range of the
            device. This value is in the native units of the device. On
            E Series devices, for example, the native units is volts.
        

#### `def ao_dac_rng_low(self, val)`

#### `def ao_dac_rng_low(self)`

#### `def ao_data_xfer_mech(self)`


        :class:`nidaqmx.constants.DataTransferActiveTransferMode`:
            Specifies the data transfer mode for the device.
        

#### `def ao_data_xfer_mech(self, val)`

#### `def ao_data_xfer_mech(self)`

#### `def ao_data_xfer_req_cond(self)`


        :class:`nidaqmx.constants.OutputDataTransferCondition`:
            Specifies under what condition to transfer data from the
            buffer to the onboard memory of the device.
        

#### `def ao_data_xfer_req_cond(self, val)`

#### `def ao_data_xfer_req_cond(self)`

#### `def ao_dev_scaling_coeff(self)`


        List[float]: Indicates the coefficients of a linear equation
            that NI-DAQmx uses to scale values from a voltage to the
            native format of the device. Each element of the list
            corresponds to a term of the equation. The first element of
            the list corresponds to the y-intercept, and the second
            element corresponds to the slope. Scaling coefficients do
            not account for any custom scales that may be applied to the
            channel.
        

#### `def ao_enhanced_image_rejection_enable(self)`


        bool: Specifies whether to enable the DAC interpolation filter.
            Disable the interpolation filter to improve DAC signal-to-
            noise ratio at the expense of degraded image rejection.
        

#### `def ao_enhanced_image_rejection_enable(self, val)`

#### `def ao_enhanced_image_rejection_enable(self)`

#### `def ao_filter_delay(self)`


        float: Specifies the amount of time between when the sample is
            written by the host device and when the sample is output by
            the DAC. This value is in the units you specify with
            **ao_filter_delay_units**.
        

#### `def ao_filter_delay(self, val)`

#### `def ao_filter_delay(self)`

#### `def ao_filter_delay_adjustment(self)`


        float: Specifies an additional amount of time to wait between
            when the sample is written by the host device and when the
            sample is output by the DAC. This delay adjustment is in
            addition to the value indicated by **ao_filter_delay**. This
            delay adjustment is in the units you specify with
            **ao_filter_delay_units**.
        

#### `def ao_filter_delay_adjustment(self, val)`

#### `def ao_filter_delay_adjustment(self)`

#### `def ao_filter_delay_units(self)`


        :class:`nidaqmx.constants.DigitalWidthUnits`: Specifies the
            units of **ao_filter_delay** and
            **ao_filter_delay_adjustment**.
        

#### `def ao_filter_delay_units(self, val)`

#### `def ao_filter_delay_units(self)`

#### `def ao_func_gen_amplitude(self)`


        float: Specifies the zero-to-peak amplitude of the waveform to
            generate in volts. Zero and negative values are valid.
        

#### `def ao_func_gen_amplitude(self, val)`

#### `def ao_func_gen_amplitude(self)`

#### `def ao_func_gen_fm_deviation(self)`


        float: Specifies the FM deviation in hertz per volt when
            **ao_func_gen_modulation_type** is **ModulationType.FM**.
        

#### `def ao_func_gen_fm_deviation(self, val)`

#### `def ao_func_gen_fm_deviation(self)`

#### `def ao_func_gen_freq(self)`


        float: Specifies the frequency of the waveform to generate in
            hertz.
        

#### `def ao_func_gen_freq(self, val)`

#### `def ao_func_gen_freq(self)`

#### `def ao_func_gen_modulation_type(self)`


        :class:`nidaqmx.constants.ModulationType`: Specifies if the
            device generates a modulated version of the waveform using
            the original waveform as a carrier and input from an
            external terminal as the signal.
        

#### `def ao_func_gen_modulation_type(self, val)`

#### `def ao_func_gen_modulation_type(self)`

#### `def ao_func_gen_offset(self)`


        float: Specifies the voltage offset of the waveform to generate.
        

#### `def ao_func_gen_offset(self, val)`

#### `def ao_func_gen_offset(self)`

#### `def ao_func_gen_square_duty_cycle(self)`


        float: Specifies the square wave duty cycle of the waveform to
            generate.
        

#### `def ao_func_gen_square_duty_cycle(self, val)`

#### `def ao_func_gen_square_duty_cycle(self)`

#### `def ao_func_gen_start_phase(self)`


        float: Specifies the starting phase in degrees of the waveform
            to generate.
        

#### `def ao_func_gen_start_phase(self, val)`

#### `def ao_func_gen_start_phase(self)`

#### `def ao_func_gen_type(self)`


        :class:`nidaqmx.constants.FuncGenType`: Specifies the kind of
            the waveform to generate.
        

#### `def ao_func_gen_type(self, val)`

#### `def ao_func_gen_type(self)`

#### `def ao_gain(self)`


        float: Specifies in decibels the gain factor to apply to the
            channel.
        

#### `def ao_gain(self, val)`

#### `def ao_gain(self)`

#### `def ao_idle_output_behavior(self)`


        :class:`nidaqmx.constants.AOIdleOutputBehavior`: Specifies the
            state of the channel when no generation is in progress.
        

#### `def ao_idle_output_behavior(self, val)`

#### `def ao_idle_output_behavior(self)`

#### `def ao_load_impedance(self)`


        float: Specifies in ohms the load impedance connected to the
            analog output channel.
        

#### `def ao_load_impedance(self, val)`

#### `def ao_load_impedance(self)`

#### `def ao_max(self)`


        float: Specifies the maximum value you expect to generate. The
            value is in the units you specify with a units property. If
            you try to write a value larger than the maximum value, NI-
            DAQmx generates an error. NI-DAQmx might coerce this value
            to a smaller value if other task settings restrict the
            device from generating the desired maximum.
        

#### `def ao_max(self, val)`

#### `def ao_max(self)`

#### `def ao_mem_map_enable(self)`


        bool: Specifies for NI-DAQmx to map hardware registers to the
            memory space of the application, if possible. Normally, NI-
            DAQmx maps hardware registers to memory accessible only to
            the kernel. Mapping the registers to the memory space of the
            application increases performance. However, if the
            application accesses the memory space mapped to the
            registers, it can adversely affect the operation of the
            device and possibly result in a system crash.
        

#### `def ao_mem_map_enable(self, val)`

#### `def ao_mem_map_enable(self)`

#### `def ao_min(self)`


        float: Specifies the minimum value you expect to generate. The
            value is in the units you specify with a units property. If
            you try to write a value smaller than the minimum value, NI-
            DAQmx generates an error. NI-DAQmx might coerce this value
            to a larger value if other task settings restrict the device
            from generating the desired minimum.
        

#### `def ao_min(self, val)`

#### `def ao_min(self)`

#### `def ao_output_impedance(self)`


        float: Specifies in ohms the impedance of the analog output
            stage of the device.
        

#### `def ao_output_impedance(self, val)`

#### `def ao_output_impedance(self)`

#### `def ao_output_type(self)`


        :class:`nidaqmx.constants.UsageTypeAO`: Indicates whether the
            channel generates voltage,  current, or a waveform.
        

#### `def ao_reglitch_enable(self)`


        bool: Specifies whether to enable reglitching.  The output of a
            DAC normally glitches whenever the DAC is updated with a new
            value. The amount of glitching differs from code to code and
            is generally largest at major code transitions.  Reglitching
            generates uniform glitch energy at each code transition and
            provides for more uniform glitches.  Uniform glitch energy
            makes it easier to filter out the noise introduced from
            glitching during spectrum analysis.
        

#### `def ao_reglitch_enable(self, val)`

#### `def ao_reglitch_enable(self)`

#### `def ao_resolution(self)`


        float: Indicates the resolution of the digital-to-analog
            converter of the channel. This value is in the units you
            specify with **ao_resolution_units**.
        

#### `def ao_resolution_units(self)`


        :class:`nidaqmx.constants.ResolutionType`: Specifies the units
            of **ao_resolution**.
        

#### `def ao_resolution_units(self, val)`

#### `def ao_resolution_units(self)`

#### `def ao_term_cfg(self)`


        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            terminal configuration of the channel.
        

#### `def ao_term_cfg(self, val)`

#### `def ao_term_cfg(self)`

#### `def ao_usb_xfer_req_count(self)`


        int: Specifies the maximum number of simultaneous USB transfers
            used to stream data. Modify this value to affect performance
            under different combinations of operating system and device.
        

#### `def ao_usb_xfer_req_count(self, val)`

#### `def ao_usb_xfer_req_count(self)`

#### `def ao_usb_xfer_req_size(self)`


        int: Specifies the maximum size of a USB transfer request in
            bytes. Modify this value to affect performance under
            different combinations of operating system and device.
        

#### `def ao_usb_xfer_req_size(self, val)`

#### `def ao_usb_xfer_req_size(self)`

#### `def ao_use_only_on_brd_mem(self)`


        bool: Specifies whether to write samples directly to the onboard
            memory of the device, bypassing the memory buffer.
            Generally, you cannot update onboard memory directly after
            you start the task. Onboard memory includes data FIFOs.
        

#### `def ao_use_only_on_brd_mem(self, val)`

#### `def ao_use_only_on_brd_mem(self)`

#### `def ao_voltage_current_limit(self)`


        float: Specifies the current limit, in amperes, for the voltage
            channel.
        

#### `def ao_voltage_current_limit(self, val)`

#### `def ao_voltage_current_limit(self)`

#### `def ao_voltage_units(self)`


        :class:`nidaqmx.constants.VoltageUnits`: Specifies in what units
            to generate voltage on the channel. Write data to the
            channel in the units you select.
        

#### `def ao_voltage_units(self, val)`

#### `def ao_voltage_units(self)`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/channels/_channel.py -->
## PYTHON MODULE: generated/nidaqmx/task/channels/_channel.py

### `class Channel()`


    Represents virtual channel or a list of virtual channels.
    

#### `def __init__(self, task_handle, virtual_or_physical_name, interpreter)`


        Args:
            task_handle (TaskHandle): Specifies the handle of the task that
                this channel is associated with.
            virtual_or_physical_name (str): Specifies the flattened virtual or
                physical name of a channel.
            interpreter (BaseInterpreter): Specifies the interpreter instance.
        

#### `def __add__(self, other)`

#### `def __contains__(self, item)`

#### `def __eq__(self, other)`

#### `def __hash__(self)`

#### `def __iadd__(self, other)`

#### `def __iter__(self)`

#### `def __len__(self)`

#### `def __ne__(self, other)`

#### `def __reversed__(self)`

#### `def __repr__(self)`

#### `def _factory(task_handle, virtual_or_physical_name, interpreter)`


        Implements the factory pattern for nidaqmx channels.

        Args:
            task_handle (TaskHandle): Specifies the handle of the task that
                this channel is associated with.
            virtual_or_physical_name (str): Specifies the flattened virtual
                or physical name of a channel.
            interpreter (BaseInterpreter): Specifies the interpreter instance.
        Returns:
            nidaqmx.task.channels.Channel:

            Indicates an object that represents the specified channel.
        

#### `def name(self)`


        str: Specifies the name of the virtual channel this object
            represents.
        

#### `def channel_names(self)`


        List[str]: Specifies the unflattened list of the virtual channels.
        

#### `def _all_channels_name(self)`


        str: Specifies the flattened names of all the virtual channels in
            the task.
        

#### `def chan_type(self)`


        :class:`nidaqmx.constants.ChannelType`: Indicates the type of
            the virtual channel.
        

#### `def description(self)`


        str: Specifies a user-defined description for the channel.
        

#### `def description(self, val)`

#### `def description(self)`

#### `def is_global(self)`


        bool: Indicates whether the channel is a global channel.
        

#### `def physical_channel(self)`


        :class:`nidaqmx.system.physical_channel.PhysicalChannel`:
            Specifies the name of the physical channel upon which this
            virtual channel is based.
        

#### `def physical_channel(self, val)`

#### `def sync_unlock_behavior(self)`


        :class:`nidaqmx.constants.SyncUnlockBehavior`: Specifies the
            action to take if the target loses its synchronization to
            the grand master.
        

#### `def sync_unlock_behavior(self, val)`

#### `def sync_unlock_behavior(self)`

#### `def save(self, save_as='', author='', overwrite_existing_channel=False, allow_interactive_editing=True, allow_interactive_deletion=True)`


        Saves this local or global channel to MAX as a global channel.

        Args:
            save_as (Optional[str]): Is the name to save the task,
                global channel, or custom scale as. If you do not
                specify a value for this input, NI-DAQmx uses the name
                currently assigned to the task, global channel, or
                custom scale.
            author (Optional[str]): Is a name to store with the task,
                global channel, or custom scale.
            overwrite_existing_channel (Optional[bool]): Specifies whether to
                overwrite a global channel of the same name if one is already
                saved in MAX. If this input is False and a global channel of
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
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/channels/_ci_channel.py -->
## PYTHON MODULE: generated/nidaqmx/task/channels/_ci_channel.py

### `class CIChannel(Channel)`


    Represents one or more counter input virtual channels and their properties.
    

#### `def __repr__(self)`

#### `def ci_ang_encoder_initial_angle(self)`


        float: Specifies the starting angle of the encoder. This value
            is in the units you specify with **ci_ang_encoder_units**.
        

#### `def ci_ang_encoder_initial_angle(self, val)`

#### `def ci_ang_encoder_initial_angle(self)`

#### `def ci_ang_encoder_pulses_per_rev(self)`


        int: Specifies the number of pulses the encoder generates per
            revolution. This value is the number of pulses on either
            signal A or signal B, not the total number of pulses on both
            signal A and signal B.
        

#### `def ci_ang_encoder_pulses_per_rev(self, val)`

#### `def ci_ang_encoder_pulses_per_rev(self)`

#### `def ci_ang_encoder_units(self)`


        :class:`nidaqmx.constants.AngleUnits`: Specifies the units to
            use to return angular position measurements from the
            channel.
        

#### `def ci_ang_encoder_units(self, val)`

#### `def ci_ang_encoder_units(self)`

#### `def ci_count(self)`


        int: Indicates the current value of the count register.
        

#### `def ci_count_edges_active_edge(self)`


        :class:`nidaqmx.constants.Edge`: Specifies on which edges to
            increment or decrement the counter.
        

#### `def ci_count_edges_active_edge(self, val)`

#### `def ci_count_edges_active_edge(self)`

#### `def ci_count_edges_count_dir_dig_fltr_enable(self)`


        bool: Specifies whether to apply the pulse width filter to the
            signal.
        

#### `def ci_count_edges_count_dir_dig_fltr_enable(self, val)`

#### `def ci_count_edges_count_dir_dig_fltr_enable(self)`

#### `def ci_count_edges_count_dir_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def ci_count_edges_count_dir_dig_fltr_min_pulse_width(self, val)`

#### `def ci_count_edges_count_dir_dig_fltr_min_pulse_width(self)`

#### `def ci_count_edges_count_dir_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def ci_count_edges_count_dir_dig_fltr_timebase_rate(self, val)`

#### `def ci_count_edges_count_dir_dig_fltr_timebase_rate(self)`

#### `def ci_count_edges_count_dir_dig_fltr_timebase_src(self)`


        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        

#### `def ci_count_edges_count_dir_dig_fltr_timebase_src(self, val)`

#### `def ci_count_edges_count_dir_dig_fltr_timebase_src(self)`

#### `def ci_count_edges_count_dir_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def ci_count_edges_count_dir_dig_sync_enable(self, val)`

#### `def ci_count_edges_count_dir_dig_sync_enable(self)`

#### `def ci_count_edges_count_dir_hyst(self)`


        float: Specifies a hysteresis level applied to the
            **ci_count_edges_count_dir_thresh_voltage**. The source
            signal must fall below
            **ci_count_edges_count_dir_thresh_voltage** minus the
            hysteresis before a change in count direction occurs.
        

#### `def ci_count_edges_count_dir_hyst(self, val)`

#### `def ci_count_edges_count_dir_hyst(self)`

#### `def ci_count_edges_count_dir_logic_lvl_behavior(self)`


        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the count reset line.
        

#### `def ci_count_edges_count_dir_logic_lvl_behavior(self, val)`

#### `def ci_count_edges_count_dir_logic_lvl_behavior(self)`

#### `def ci_count_edges_count_dir_term_cfg(self)`


        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        

#### `def ci_count_edges_count_dir_term_cfg(self, val)`

#### `def ci_count_edges_count_dir_term_cfg(self)`

#### `def ci_count_edges_count_dir_thresh_voltage(self)`


        float: Specifies the voltage level applied to the Count
            Direction terminal. When the signal is above this threshold,
            the counter counts up. When the signal is below this
            threshold, the counter counts down.
        

#### `def ci_count_edges_count_dir_thresh_voltage(self, val)`

#### `def ci_count_edges_count_dir_thresh_voltage(self)`

#### `def ci_count_edges_count_reset_active_edge(self)`


        :class:`nidaqmx.constants.Edge`: Specifies on which edge of the
            signal to reset the count.
        

#### `def ci_count_edges_count_reset_active_edge(self, val)`

#### `def ci_count_edges_count_reset_active_edge(self)`

#### `def ci_count_edges_count_reset_dig_fltr_enable(self)`


        bool: Specifies whether to apply the pulse width filter to the
            signal.
        

#### `def ci_count_edges_count_reset_dig_fltr_enable(self, val)`

#### `def ci_count_edges_count_reset_dig_fltr_enable(self)`

#### `def ci_count_edges_count_reset_dig_fltr_min_pulse_width(self)`


        float: Specifies the minimum pulse width the filter recognizes.
        

#### `def ci_count_edges_count_reset_dig_fltr_min_pulse_width(self, val)`

#### `def ci_count_edges_count_reset_dig_fltr_min_pulse_width(self)`

#### `def ci_count_edges_count_reset_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def ci_count_edges_count_reset_dig_fltr_timebase_rate(self, val)`

#### `def ci_count_edges_count_reset_dig_fltr_timebase_rate(self)`

#### `def ci_count_edges_count_reset_dig_fltr_timebase_src(self)`


        str: Specifies the input of the signal to use as the timebase of
            the pulse width filter.
        

#### `def ci_count_edges_count_reset_dig_fltr_timebase_src(self, val)`

#### `def ci_count_edges_count_reset_dig_fltr_timebase_src(self)`

#### `def ci_count_edges_count_reset_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def ci_count_edges_count_reset_dig_sync_enable(self, val)`

#### `def ci_count_edges_count_reset_dig_sync_enable(self)`

#### `def ci_count_edges_count_reset_enable(self)`


        bool: Specifies whether to reset the count on the active edge
            specified with **ci_count_edges_count_reset_term**.
        

#### `def ci_count_edges_count_reset_enable(self, val)`

#### `def ci_count_edges_count_reset_enable(self)`

#### `def ci_count_edges_count_reset_hyst(self)`


        float: Specifies a hysteresis level applied to
            **ci_count_edges_count_reset_thresh_voltage**. When
            **ci_count_edges_count_reset_active_edge** is rising, the
            source signal must first fall below
            **ci_count_edges_count_reset_thresh_voltage** minus the
            hysteresis before a rising edge is detected at
            **ci_count_edges_count_reset_thresh_voltage**. When
            **ci_count_edges_count_reset_active_edge** is falling, the
            source signal must first rise above
            **ci_count_edges_count_reset_thresh_voltage** plus the
            hysteresis before a falling edge is detected at
            **ci_count_edges_count_reset_thresh_voltage**.
        

#### `def ci_count_edges_count_reset_hyst(self, val)`

#### `def ci_count_edges_count_reset_hyst(self)`

#### `def ci_count_edges_count_reset_logic_lvl_behavior(self)`


        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the count reset line.
        

#### `def ci_count_edges_count_reset_logic_lvl_behavior(self, val)`

#### `def ci_count_edges_count_reset_logic_lvl_behavior(self)`

#### `def ci_count_edges_count_reset_reset_cnt(self)`


        int: Specifies the value to reset the count to.
        

#### `def ci_count_edges_count_reset_reset_cnt(self, val)`

#### `def ci_count_edges_count_reset_reset_cnt(self)`

#### `def ci_count_edges_count_reset_term(self)`


        str: Specifies the input terminal of the signal to reset the
            count.
        

#### `def ci_count_edges_count_reset_term(self, val)`

#### `def ci_count_edges_count_reset_term(self)`

#### `def ci_count_edges_count_reset_term_cfg(self)`


        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        

#### `def ci_count_edges_count_reset_term_cfg(self, val)`

#### `def ci_count_edges_count_reset_term_cfg(self)`

#### `def ci_count_edges_count_reset_thresh_voltage(self)`


        float: Specifies the voltage level at which to recognize the
            counter reset event.
        

#### `def ci_count_edges_count_reset_thresh_voltage(self, val)`

#### `def ci_count_edges_count_reset_thresh_voltage(self)`

#### `def ci_count_edges_dig_fltr_enable(self)`


        bool: Specifies whether to apply the pulse width filter to the
            signal.
        

#### `def ci_count_edges_dig_fltr_enable(self, val)`

#### `def ci_count_edges_dig_fltr_enable(self)`

#### `def ci_count_edges_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def ci_count_edges_dig_fltr_min_pulse_width(self, val)`

#### `def ci_count_edges_dig_fltr_min_pulse_width(self)`

#### `def ci_count_edges_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def ci_count_edges_dig_fltr_timebase_rate(self, val)`

#### `def ci_count_edges_dig_fltr_timebase_rate(self)`

#### `def ci_count_edges_dig_fltr_timebase_src(self)`


        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        

#### `def ci_count_edges_dig_fltr_timebase_src(self, val)`

#### `def ci_count_edges_dig_fltr_timebase_src(self)`

#### `def ci_count_edges_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def ci_count_edges_dig_sync_enable(self, val)`

#### `def ci_count_edges_dig_sync_enable(self)`

#### `def ci_count_edges_dir(self)`


        :class:`nidaqmx.constants.CountDirection`: Specifies whether to
            increment or decrement the counter on each edge.
        

#### `def ci_count_edges_dir(self, val)`

#### `def ci_count_edges_dir(self)`

#### `def ci_count_edges_dir_term(self)`


        str: Specifies the source terminal of the digital signal that
            controls the count direction if **ci_count_edges_dir** is
            **CountDirection1.EXTERNAL_SOURCE**.
        

#### `def ci_count_edges_dir_term(self, val)`

#### `def ci_count_edges_dir_term(self)`

#### `def ci_count_edges_gate_dig_fltr_enable(self)`


        bool: Specifies whether to apply the pulse width filter to the
            gate input signal.
        

#### `def ci_count_edges_gate_dig_fltr_enable(self, val)`

#### `def ci_count_edges_gate_dig_fltr_enable(self)`

#### `def ci_count_edges_gate_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the digital
            filter recognizes.
        

#### `def ci_count_edges_gate_dig_fltr_min_pulse_width(self, val)`

#### `def ci_count_edges_gate_dig_fltr_min_pulse_width(self)`

#### `def ci_count_edges_gate_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def ci_count_edges_gate_dig_fltr_timebase_rate(self, val)`

#### `def ci_count_edges_gate_dig_fltr_timebase_rate(self)`

#### `def ci_count_edges_gate_dig_fltr_timebase_src(self)`


        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        

#### `def ci_count_edges_gate_dig_fltr_timebase_src(self, val)`

#### `def ci_count_edges_gate_dig_fltr_timebase_src(self)`

#### `def ci_count_edges_gate_enable(self)`


        bool: Specifies whether to enable the functionality to gate the
            counter input signal for a count edges measurement.
        

#### `def ci_count_edges_gate_enable(self, val)`

#### `def ci_count_edges_gate_enable(self)`

#### `def ci_count_edges_gate_hyst(self)`


        float: Specifies a hysteresis level applied to the
            **ci_count_edges_gate_thresh_voltage**. When
            **ci_count_edges_gate_when** is High, the source signal must
            fall below **ci_count_edges_gate_thresh_voltage** minus the
            hysteresis before the counter resumes counting. When
            **ci_count_edges_gate_when** is Low, the source signal must
            rise above **ci_count_edges_gate_thresh_voltage** plus the
            hysteresis before the counter resumes counting.
        

#### `def ci_count_edges_gate_hyst(self, val)`

#### `def ci_count_edges_gate_hyst(self)`

#### `def ci_count_edges_gate_logic_lvl_behavior(self)`


        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the gate input line.
        

#### `def ci_count_edges_gate_logic_lvl_behavior(self, val)`

#### `def ci_count_edges_gate_logic_lvl_behavior(self)`

#### `def ci_count_edges_gate_term(self)`


        str: Specifies the gate terminal.
        

#### `def ci_count_edges_gate_term(self, val)`

#### `def ci_count_edges_gate_term(self)`

#### `def ci_count_edges_gate_term_cfg(self)`


        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            gate terminal configuration.
        

#### `def ci_count_edges_gate_term_cfg(self, val)`

#### `def ci_count_edges_gate_term_cfg(self)`

#### `def ci_count_edges_gate_thresh_voltage(self)`


        float: Specifies the voltage level at which to recognize the
            counter gate signal.
        

#### `def ci_count_edges_gate_thresh_voltage(self, val)`

#### `def ci_count_edges_gate_thresh_voltage(self)`

#### `def ci_count_edges_gate_when(self)`


        :class:`nidaqmx.constants.Level`: Specifies whether the counter
            gates input pulses while the signal is high or low.
        

#### `def ci_count_edges_gate_when(self, val)`

#### `def ci_count_edges_gate_when(self)`

#### `def ci_count_edges_hyst(self)`


        float: Specifies a hysteresis level to apply to
            **ci_count_edges_thresh_voltage**. When
            **ci_count_edges_active_edge** is rising, the source signal
            must first fall below **ci_count_edges_thresh_voltage**
            minus the hysteresis before a rising edge is detected at
            **ci_count_edges_thresh_voltage**. When
            **ci_count_edges_active_edge** is falling, the source signal
            must first rise above **ci_count_edges_thresh_voltage** plus
            the hysteresis before a falling edge is detected at
            **ci_count_edges_thresh_voltage**.
        

#### `def ci_count_edges_hyst(self, val)`

#### `def ci_count_edges_hyst(self)`

#### `def ci_count_edges_initial_cnt(self)`


        int: Specifies the starting value from which to count.
        

#### `def ci_count_edges_initial_cnt(self, val)`

#### `def ci_count_edges_initial_cnt(self)`

#### `def ci_count_edges_logic_lvl_behavior(self)`


        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the input line.
        

#### `def ci_count_edges_logic_lvl_behavior(self, val)`

#### `def ci_count_edges_logic_lvl_behavior(self)`

#### `def ci_count_edges_term(self)`


        str: Specifies the input terminal of the signal to measure.
        

#### `def ci_count_edges_term(self, val)`

#### `def ci_count_edges_term(self)`

#### `def ci_count_edges_term_cfg(self)`


        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        

#### `def ci_count_edges_term_cfg(self, val)`

#### `def ci_count_edges_term_cfg(self)`

#### `def ci_count_edges_thresh_voltage(self)`


        float: Specifies the voltage level at which to recognize
            waveform repetitions. Select a voltage level that occurs
            only once within the entire period of a waveform. You also
            can select a voltage that occurs only once while the voltage
            rises or falls.
        

#### `def ci_count_edges_thresh_voltage(self, val)`

#### `def ci_count_edges_thresh_voltage(self)`

#### `def ci_ctr_timebase_active_edge(self)`


        :class:`nidaqmx.constants.Edge`: Specifies whether a timebase
            cycle is from rising edge to rising edge or from falling
            edge to falling edge.
        

#### `def ci_ctr_timebase_active_edge(self, val)`

#### `def ci_ctr_timebase_active_edge(self)`

#### `def ci_ctr_timebase_dig_fltr_enable(self)`


        bool: Specifies whether to apply the pulse width filter to the
            signal.
        

#### `def ci_ctr_timebase_dig_fltr_enable(self, val)`

#### `def ci_ctr_timebase_dig_fltr_enable(self)`

#### `def ci_ctr_timebase_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def ci_ctr_timebase_dig_fltr_min_pulse_width(self, val)`

#### `def ci_ctr_timebase_dig_fltr_min_pulse_width(self)`

#### `def ci_ctr_timebase_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def ci_ctr_timebase_dig_fltr_timebase_rate(self, val)`

#### `def ci_ctr_timebase_dig_fltr_timebase_rate(self)`

#### `def ci_ctr_timebase_dig_fltr_timebase_src(self)`


        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        

#### `def ci_ctr_timebase_dig_fltr_timebase_src(self, val)`

#### `def ci_ctr_timebase_dig_fltr_timebase_src(self)`

#### `def ci_ctr_timebase_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def ci_ctr_timebase_dig_sync_enable(self, val)`

#### `def ci_ctr_timebase_dig_sync_enable(self)`

#### `def ci_ctr_timebase_master_timebase_div(self)`


        int: Specifies the divisor for an external counter timebase. You
            can divide the counter timebase in order to measure slower
            signals without causing the count register to roll over.
        

#### `def ci_ctr_timebase_master_timebase_div(self, val)`

#### `def ci_ctr_timebase_master_timebase_div(self)`

#### `def ci_ctr_timebase_rate(self)`


        float: Specifies in Hertz the frequency of the counter timebase.
            Specifying the rate of a counter timebase allows you to take
            measurements in terms of time or frequency rather than in
            ticks of the timebase. If you use an external timebase and
            do not specify the rate, you can take measurements only in
            terms of ticks of the timebase.
        

#### `def ci_ctr_timebase_rate(self, val)`

#### `def ci_ctr_timebase_rate(self)`

#### `def ci_ctr_timebase_src(self)`


        str: Specifies the terminal of the timebase to use for the
            counter.
        

#### `def ci_ctr_timebase_src(self, val)`

#### `def ci_ctr_timebase_src(self)`

#### `def ci_custom_scale(self)`


        :class:`nidaqmx.system.scale.Scale`: Specifies the name of a
            custom scale for the channel.
        

#### `def ci_custom_scale(self, val)`

#### `def ci_custom_scale(self)`

#### `def ci_data_xfer_mech(self)`


        :class:`nidaqmx.constants.DataTransferActiveTransferMode`:
            Specifies the data transfer mode for the channel.
        

#### `def ci_data_xfer_mech(self, val)`

#### `def ci_data_xfer_mech(self)`

#### `def ci_data_xfer_req_cond(self)`


        :class:`nidaqmx.constants.InputDataTransferCondition`: Specifies
            under what condition to transfer data from the onboard
            memory of the device to the buffer.
        

#### `def ci_data_xfer_req_cond(self, val)`

#### `def ci_data_xfer_req_cond(self)`

#### `def ci_dup_count_prevention(self)`


        bool: Specifies whether to enable duplicate count prevention for
            the channel. Duplicate count prevention is enabled by
            default. Setting  **ci_prescaler** disables duplicate count
            prevention unless you explicitly enable it.
        

#### `def ci_dup_count_prevention(self, val)`

#### `def ci_dup_count_prevention(self)`

#### `def ci_duty_cycle_dig_fltr_enable(self)`


        bool: Specifies whether to apply the pulse width filter to the
            signal.
        

#### `def ci_duty_cycle_dig_fltr_enable(self, val)`

#### `def ci_duty_cycle_dig_fltr_enable(self)`

#### `def ci_duty_cycle_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the digital
            filter recognizes.
        

#### `def ci_duty_cycle_dig_fltr_min_pulse_width(self, val)`

#### `def ci_duty_cycle_dig_fltr_min_pulse_width(self)`

#### `def ci_duty_cycle_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def ci_duty_cycle_dig_fltr_timebase_rate(self, val)`

#### `def ci_duty_cycle_dig_fltr_timebase_rate(self)`

#### `def ci_duty_cycle_dig_fltr_timebase_src(self)`


        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        

#### `def ci_duty_cycle_dig_fltr_timebase_src(self, val)`

#### `def ci_duty_cycle_dig_fltr_timebase_src(self)`

#### `def ci_duty_cycle_logic_lvl_behavior(self)`


        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the input line.
        

#### `def ci_duty_cycle_logic_lvl_behavior(self, val)`

#### `def ci_duty_cycle_logic_lvl_behavior(self)`

#### `def ci_duty_cycle_starting_edge(self)`


        :class:`nidaqmx.constants.Edge`: Specifies which edge of the
            input signal to begin the duty cycle measurement.
        

#### `def ci_duty_cycle_starting_edge(self, val)`

#### `def ci_duty_cycle_starting_edge(self)`

#### `def ci_duty_cycle_term(self)`


        str: Specifies the input terminal of the signal to measure.
        

#### `def ci_duty_cycle_term(self, val)`

#### `def ci_duty_cycle_term(self)`

#### `def ci_duty_cycle_term_cfg(self)`


        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        

#### `def ci_duty_cycle_term_cfg(self, val)`

#### `def ci_duty_cycle_term_cfg(self)`

#### `def ci_encoder_a_input_dig_fltr_enable(self)`


        bool: Specifies whether to apply the pulse width filter to the
            signal.
        

#### `def ci_encoder_a_input_dig_fltr_enable(self, val)`

#### `def ci_encoder_a_input_dig_fltr_enable(self)`

#### `def ci_encoder_a_input_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def ci_encoder_a_input_dig_fltr_min_pulse_width(self, val)`

#### `def ci_encoder_a_input_dig_fltr_min_pulse_width(self)`

#### `def ci_encoder_a_input_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def ci_encoder_a_input_dig_fltr_timebase_rate(self, val)`

#### `def ci_encoder_a_input_dig_fltr_timebase_rate(self)`

#### `def ci_encoder_a_input_dig_fltr_timebase_src(self)`


        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        

#### `def ci_encoder_a_input_dig_fltr_timebase_src(self, val)`

#### `def ci_encoder_a_input_dig_fltr_timebase_src(self)`

#### `def ci_encoder_a_input_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def ci_encoder_a_input_dig_sync_enable(self, val)`

#### `def ci_encoder_a_input_dig_sync_enable(self)`

#### `def ci_encoder_a_input_logic_lvl_behavior(self)`


        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the input line.
        

#### `def ci_encoder_a_input_logic_lvl_behavior(self, val)`

#### `def ci_encoder_a_input_logic_lvl_behavior(self)`

#### `def ci_encoder_a_input_term(self)`


        str: Specifies the terminal to which signal A is connected.
        

#### `def ci_encoder_a_input_term(self, val)`

#### `def ci_encoder_a_input_term(self)`

#### `def ci_encoder_a_input_term_cfg(self)`


        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        

#### `def ci_encoder_a_input_term_cfg(self, val)`

#### `def ci_encoder_a_input_term_cfg(self)`

#### `def ci_encoder_b_input_dig_fltr_enable(self)`


        bool: Specifies whether to apply the pulse width filter to the
            signal.
        

#### `def ci_encoder_b_input_dig_fltr_enable(self, val)`

#### `def ci_encoder_b_input_dig_fltr_enable(self)`

#### `def ci_encoder_b_input_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def ci_encoder_b_input_dig_fltr_min_pulse_width(self, val)`

#### `def ci_encoder_b_input_dig_fltr_min_pulse_width(self)`

#### `def ci_encoder_b_input_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def ci_encoder_b_input_dig_fltr_timebase_rate(self, val)`

#### `def ci_encoder_b_input_dig_fltr_timebase_rate(self)`

#### `def ci_encoder_b_input_dig_fltr_timebase_src(self)`


        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        

#### `def ci_encoder_b_input_dig_fltr_timebase_src(self, val)`

#### `def ci_encoder_b_input_dig_fltr_timebase_src(self)`

#### `def ci_encoder_b_input_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def ci_encoder_b_input_dig_sync_enable(self, val)`

#### `def ci_encoder_b_input_dig_sync_enable(self)`

#### `def ci_encoder_b_input_logic_lvl_behavior(self)`


        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the input line.
        

#### `def ci_encoder_b_input_logic_lvl_behavior(self, val)`

#### `def ci_encoder_b_input_logic_lvl_behavior(self)`

#### `def ci_encoder_b_input_term(self)`


        str: Specifies the terminal to which signal B is connected.
        

#### `def ci_encoder_b_input_term(self, val)`

#### `def ci_encoder_b_input_term(self)`

#### `def ci_encoder_b_input_term_cfg(self)`


        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        

#### `def ci_encoder_b_input_term_cfg(self, val)`

#### `def ci_encoder_b_input_term_cfg(self)`

#### `def ci_encoder_decoding_type(self)`


        :class:`nidaqmx.constants.EncoderType`: Specifies how to count
            and interpret the pulses the encoder generates on signal A
            and signal B. **EncoderType2.X_1**, **EncoderType2.X_2**,
            and **EncoderType2.X_4** are valid for quadrature encoders
            only. **EncoderType2.TWO_PULSE_COUNTING** is valid for two-
            pulse encoders only.
        

#### `def ci_encoder_decoding_type(self, val)`

#### `def ci_encoder_decoding_type(self)`

#### `def ci_encoder_z_index_enable(self)`


        bool: Specifies whether to use Z indexing for the channel.
        

#### `def ci_encoder_z_index_enable(self, val)`

#### `def ci_encoder_z_index_enable(self)`

#### `def ci_encoder_z_index_phase(self)`


        :class:`nidaqmx.constants.EncoderZIndexPhase`: Specifies the
            states at which signal A and signal B must be while signal Z
            is high for NI-DAQmx to reset the measurement. If signal Z
            is never high while signal A and signal B are high, for
            example, you must choose a phase other than
            **EncoderZIndexPhase1.AHIGH_BHIGH**.
        

#### `def ci_encoder_z_index_phase(self, val)`

#### `def ci_encoder_z_index_phase(self)`

#### `def ci_encoder_z_index_val(self)`


        float: Specifies the value to which to reset the measurement
            when signal Z is high and signal A and signal B are at the
            states you specify with **ci_encoder_z_index_phase**.
            Specify this value in the units of the measurement.
        

#### `def ci_encoder_z_index_val(self, val)`

#### `def ci_encoder_z_index_val(self)`

#### `def ci_encoder_z_input_dig_fltr_enable(self)`


        bool: Specifies whether to apply the pulse width filter to the
            signal.
        

#### `def ci_encoder_z_input_dig_fltr_enable(self, val)`

#### `def ci_encoder_z_input_dig_fltr_enable(self)`

#### `def ci_encoder_z_input_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def ci_encoder_z_input_dig_fltr_min_pulse_width(self, val)`

#### `def ci_encoder_z_input_dig_fltr_min_pulse_width(self)`

#### `def ci_encoder_z_input_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def ci_encoder_z_input_dig_fltr_timebase_rate(self, val)`

#### `def ci_encoder_z_input_dig_fltr_timebase_rate(self)`

#### `def ci_encoder_z_input_dig_fltr_timebase_src(self)`


        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        

#### `def ci_encoder_z_input_dig_fltr_timebase_src(self, val)`

#### `def ci_encoder_z_input_dig_fltr_timebase_src(self)`

#### `def ci_encoder_z_input_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def ci_encoder_z_input_dig_sync_enable(self, val)`

#### `def ci_encoder_z_input_dig_sync_enable(self)`

#### `def ci_encoder_z_input_logic_lvl_behavior(self)`


        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the input line.
        

#### `def ci_encoder_z_input_logic_lvl_behavior(self, val)`

#### `def ci_encoder_z_input_logic_lvl_behavior(self)`

#### `def ci_encoder_z_input_term(self)`


        str: Specifies the terminal to which signal Z is connected.
        

#### `def ci_encoder_z_input_term(self, val)`

#### `def ci_encoder_z_input_term(self)`

#### `def ci_encoder_z_input_term_cfg(self)`


        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        

#### `def ci_encoder_z_input_term_cfg(self, val)`

#### `def ci_encoder_z_input_term_cfg(self)`

#### `def ci_filter_delay(self)`


        float: Indicates the amount of time between when the input
            signal transitions and when the filtered sample is read by
            the host device. This value is in the units specified with
            **ci_filter_delay_units**.
        

#### `def ci_filter_delay_units(self)`


        :class:`nidaqmx.constants.DigitalWidthUnits`: Specifies the
            units of **ci_filter_delay**.
        

#### `def ci_filter_delay_units(self, val)`

#### `def ci_filter_delay_units(self)`

#### `def ci_filter_enable(self)`


        bool: Specifies the corresponding filter enable/disable state.
        

#### `def ci_filter_enable(self, val)`

#### `def ci_filter_enable(self)`

#### `def ci_filter_freq(self)`


        float: Specifies the corresponding filter frequency (cutoff or
            center) of the filter response.
        

#### `def ci_filter_freq(self, val)`

#### `def ci_filter_freq(self)`

#### `def ci_filter_order(self)`


        int: Specifies the corresponding filter order and defines the
            slope of the filter response.
        

#### `def ci_filter_order(self, val)`

#### `def ci_filter_order(self)`

#### `def ci_filter_response(self)`


        :class:`nidaqmx.constants.FilterResponse`: Specifies the
            corresponding filter response and defines the shape of the
            filter response.
        

#### `def ci_filter_response(self, val)`

#### `def ci_filter_response(self)`

#### `def ci_freq_dig_fltr_enable(self)`


        bool: Specifies whether to apply the pulse width filter to the
            signal.
        

#### `def ci_freq_dig_fltr_enable(self, val)`

#### `def ci_freq_dig_fltr_enable(self)`

#### `def ci_freq_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def ci_freq_dig_fltr_min_pulse_width(self, val)`

#### `def ci_freq_dig_fltr_min_pulse_width(self)`

#### `def ci_freq_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def ci_freq_dig_fltr_timebase_rate(self, val)`

#### `def ci_freq_dig_fltr_timebase_rate(self)`

#### `def ci_freq_dig_fltr_timebase_src(self)`


        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        

#### `def ci_freq_dig_fltr_timebase_src(self, val)`

#### `def ci_freq_dig_fltr_timebase_src(self)`

#### `def ci_freq_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def ci_freq_dig_sync_enable(self, val)`

#### `def ci_freq_dig_sync_enable(self)`

#### `def ci_freq_div(self)`


        int: Specifies the value by which to divide the input signal if
            **ci_freq_meas_meth** is
            **CounterFrequencyMethod.LARGE_RANGE_2_COUNTERS**. The
            larger the divisor, the more accurate the measurement.
            However, too large a value could cause the count register to
            roll over, which results in an incorrect measurement.
        

#### `def ci_freq_div(self, val)`

#### `def ci_freq_div(self)`

#### `def ci_freq_enable_averaging(self)`


        bool: Specifies whether to enable averaging mode for Sample
            Clock-timed frequency measurements.
        

#### `def ci_freq_enable_averaging(self, val)`

#### `def ci_freq_enable_averaging(self)`

#### `def ci_freq_hyst(self)`


        float: Specifies a hysteresis level to apply to
            **ci_freq_thresh_voltage**. When **ci_freq_starting_edge**
            is rising, the source signal must first fall below
            **ci_freq_thresh_voltage** minus the hysteresis before a
            rising edge is detected at **ci_freq_thresh_voltage**. When
            **ci_freq_starting_edge** is falling, the source signal must
            first rise above **ci_freq_thresh_voltage** plus the
            hysteresis before a falling edge is detected at
            **ci_freq_thresh_voltage**.
        

#### `def ci_freq_hyst(self, val)`

#### `def ci_freq_hyst(self)`

#### `def ci_freq_logic_lvl_behavior(self)`


        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the input line.
        

#### `def ci_freq_logic_lvl_behavior(self, val)`

#### `def ci_freq_logic_lvl_behavior(self)`

#### `def ci_freq_meas_meth(self)`


        :class:`nidaqmx.constants.CounterFrequencyMethod`: Specifies the
            method to use to measure the frequency of the signal.
        

#### `def ci_freq_meas_meth(self, val)`

#### `def ci_freq_meas_meth(self)`

#### `def ci_freq_meas_time(self)`


        float: Specifies in seconds the length of time to measure the
            frequency of the signal if **ci_freq_meas_meth** is
            **CounterFrequencyMethod.HIGH_FREQUENCY_2_COUNTERS**.
            Measurement accuracy increases with increased measurement
            time and with increased signal frequency. If you measure a
            high-frequency signal for too long, however, the count
            register could roll over, which results in an incorrect
            measurement.
        

#### `def ci_freq_meas_time(self, val)`

#### `def ci_freq_meas_time(self)`

#### `def ci_freq_starting_edge(self)`


        :class:`nidaqmx.constants.Edge`: Specifies between which edges
            to measure the frequency of the signal.
        

#### `def ci_freq_starting_edge(self, val)`

#### `def ci_freq_starting_edge(self)`

#### `def ci_freq_term(self)`


        str: Specifies the input terminal of the signal to measure.
        

#### `def ci_freq_term(self, val)`

#### `def ci_freq_term(self)`

#### `def ci_freq_term_cfg(self)`


        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        

#### `def ci_freq_term_cfg(self, val)`

#### `def ci_freq_term_cfg(self)`

#### `def ci_freq_thresh_voltage(self)`


        float: Specifies the voltage level at which to recognize
            waveform repetitions. Select a voltage level that occurs
            only once within the entire period of a waveform. You also
            can select a voltage that occurs only once while the voltage
            rises or falls.
        

#### `def ci_freq_thresh_voltage(self, val)`

#### `def ci_freq_thresh_voltage(self)`

#### `def ci_freq_units(self)`


        :class:`nidaqmx.constants.FrequencyUnits`: Specifies the units
            to use to return frequency measurements.
        

#### `def ci_freq_units(self, val)`

#### `def ci_freq_units(self)`

#### `def ci_gps_sync_method(self)`


        :class:`nidaqmx.constants.GpsSignalType`: Specifies the method
            to use to synchronize the counter to a GPS receiver.
        

#### `def ci_gps_sync_method(self, val)`

#### `def ci_gps_sync_method(self)`

#### `def ci_gps_sync_src(self)`


        str: Specifies the terminal to which the GPS synchronization
            signal is connected.
        

#### `def ci_gps_sync_src(self, val)`

#### `def ci_gps_sync_src(self)`

#### `def ci_lin_encoder_dist_per_pulse(self)`


        float: Specifies the distance to measure for each pulse the
            encoder generates on signal A or signal B. This value is in
            the units you specify with **ci_lin_encoder_units**.
        

#### `def ci_lin_encoder_dist_per_pulse(self, val)`

#### `def ci_lin_encoder_dist_per_pulse(self)`

#### `def ci_lin_encoder_initial_pos(self)`


        float: Specifies the position of the encoder when the
            measurement begins. This value is in the units you specify
            with **ci_lin_encoder_units**.
        

#### `def ci_lin_encoder_initial_pos(self, val)`

#### `def ci_lin_encoder_initial_pos(self)`

#### `def ci_lin_encoder_units(self)`


        :class:`nidaqmx.constants.LengthUnits`: Specifies the units to
            use to return linear encoder measurements from the channel.
        

#### `def ci_lin_encoder_units(self, val)`

#### `def ci_lin_encoder_units(self)`

#### `def ci_max(self)`


        float: Specifies the maximum value you expect to measure. This
            value is in the units you specify with a units property.
            When you query this property, it returns the coerced maximum
            value that the hardware can measure with the current
            settings.
        

#### `def ci_max(self, val)`

#### `def ci_max(self)`

#### `def ci_max_meas_period(self)`


        float: Specifies the maximum period (in seconds) in which the
            device will recognize signals. For frequency measurements, a
            signal with a higher period than the one set in this
            property will return 0 Hz. For duty cycle, the device will
            return 0 or 1 depending on the state of the line during the
            max defined period of time. Period measurements will return
            NaN. Pulse width measurement will return zero.
        

#### `def ci_max_meas_period(self, val)`

#### `def ci_max_meas_period(self)`

#### `def ci_meas_type(self)`


        :class:`nidaqmx.constants.UsageTypeCI`: Indicates the
            measurement to take with the channel.
        

#### `def ci_mem_map_enable(self)`


        bool: Specifies for NI-DAQmx to map hardware registers to the
            memory space of the application, if possible. Normally, NI-
            DAQmx maps hardware registers to memory accessible only to
            the kernel. Mapping the registers to the memory space of the
            application increases performance. However, if the
            application accesses the memory space mapped to the
            registers, it can adversely affect the operation of the
            device and possibly result in a system crash.
        

#### `def ci_mem_map_enable(self, val)`

#### `def ci_mem_map_enable(self)`

#### `def ci_min(self)`


        float: Specifies the minimum value you expect to measure. This
            value is in the units you specify with a units property.
            When you query this property, it returns the coerced minimum
            value that the hardware can measure with the current
            settings.
        

#### `def ci_min(self, val)`

#### `def ci_min(self)`

#### `def ci_num_possibly_invalid_samps(self)`


        int: Indicates the number of samples that the device might have
            overwritten before it could transfer them to the buffer.
        

#### `def ci_output_state(self)`


        :class:`nidaqmx.constants.Level`: Indicates the current state of
            the out terminal of the counter.
        

#### `def ci_period_dig_fltr_enable(self)`


        bool: Specifies whether to apply the pulse width filter to the
            signal.
        

#### `def ci_period_dig_fltr_enable(self, val)`

#### `def ci_period_dig_fltr_enable(self)`

#### `def ci_period_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def ci_period_dig_fltr_min_pulse_width(self, val)`

#### `def ci_period_dig_fltr_min_pulse_width(self)`

#### `def ci_period_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def ci_period_dig_fltr_timebase_rate(self, val)`

#### `def ci_period_dig_fltr_timebase_rate(self)`

#### `def ci_period_dig_fltr_timebase_src(self)`


        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        

#### `def ci_period_dig_fltr_timebase_src(self, val)`

#### `def ci_period_dig_fltr_timebase_src(self)`

#### `def ci_period_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def ci_period_dig_sync_enable(self, val)`

#### `def ci_period_dig_sync_enable(self)`

#### `def ci_period_div(self)`


        int: Specifies the value by which to divide the input signal if
            **ci_period_meas_meth** is
            **CounterFrequencyMethod.LARGE_RANGE_2_COUNTERS**. The
            larger the divisor, the more accurate the measurement.
            However, too large a value could cause the count register to
            roll over, which results in an incorrect measurement.
        

#### `def ci_period_div(self, val)`

#### `def ci_period_div(self)`

#### `def ci_period_enable_averaging(self)`


        bool: Specifies whether to enable averaging mode for Sample
            Clock-timed period measurements.
        

#### `def ci_period_enable_averaging(self, val)`

#### `def ci_period_enable_averaging(self)`

#### `def ci_period_hyst(self)`


        float: Specifies a hysteresis level to apply to
            **ci_period_thresh_voltage**. When
            **ci_period_starting_edge** is rising, the source signal
            must first fall below **ci_period_thresh_voltage** minus the
            hysteresis before a rising edge is detected at
            **ci_period_thresh_voltage**. When
            **ci_period_starting_edge** is falling, the source signal
            must first rise above **ci_period_thresh_voltage** plus the
            hysteresis before a falling edge is detected at
            **ci_period_thresh_voltage**.
        

#### `def ci_period_hyst(self, val)`

#### `def ci_period_hyst(self)`

#### `def ci_period_logic_lvl_behavior(self)`


        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the input line.
        

#### `def ci_period_logic_lvl_behavior(self, val)`

#### `def ci_period_logic_lvl_behavior(self)`

#### `def ci_period_meas_meth(self)`


        :class:`nidaqmx.constants.CounterFrequencyMethod`: Specifies the
            method to use to measure the period of the signal.
        

#### `def ci_period_meas_meth(self, val)`

#### `def ci_period_meas_meth(self)`

#### `def ci_period_meas_time(self)`


        float: Specifies in seconds the length of time to measure the
            period of the signal if **ci_period_meas_meth** is
            **CounterFrequencyMethod.HIGH_FREQUENCY_2_COUNTERS**.
            Measurement accuracy increases with increased measurement
            time and with increased signal frequency. If you measure a
            high-frequency signal for too long, however, the count
            register could roll over, which results in an incorrect
            measurement.
        

#### `def ci_period_meas_time(self, val)`

#### `def ci_period_meas_time(self)`

#### `def ci_period_starting_edge(self)`


        :class:`nidaqmx.constants.Edge`: Specifies between which edges
            to measure the period of the signal.
        

#### `def ci_period_starting_edge(self, val)`

#### `def ci_period_starting_edge(self)`

#### `def ci_period_term(self)`


        str: Specifies the input terminal of the signal to measure.
        

#### `def ci_period_term(self, val)`

#### `def ci_period_term(self)`

#### `def ci_period_term_cfg(self)`


        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        

#### `def ci_period_term_cfg(self, val)`

#### `def ci_period_term_cfg(self)`

#### `def ci_period_thresh_voltage(self)`


        float: Specifies the voltage level at which to recognize
            waveform repetitions. Select a voltage level that occurs
            only once within the entire period of a waveform. You also
            can select a voltage that occurs only once while the voltage
            rises or falls.
        

#### `def ci_period_thresh_voltage(self, val)`

#### `def ci_period_thresh_voltage(self)`

#### `def ci_period_units(self)`


        :class:`nidaqmx.constants.TimeUnits`: Specifies the unit to use
            to return period measurements.
        

#### `def ci_period_units(self, val)`

#### `def ci_period_units(self)`

#### `def ci_prescaler(self)`


        int: Specifies the divisor to apply to the signal you connect to
            the counter source terminal. Scaled data that you read takes
            this setting into account. You should use a prescaler only
            when you connect an external signal to the counter source
            terminal and when that signal has a higher frequency than
            the fastest onboard timebase. Setting this value disables
            duplicate count prevention unless you explicitly set
            **ci_dup_count_prevention** to True.
        

#### `def ci_prescaler(self, val)`

#### `def ci_prescaler(self)`

#### `def ci_pulse_freq_dig_fltr_enable(self)`


        bool: Specifies whether to apply a digital filter to the signal
            to measure.
        

#### `def ci_pulse_freq_dig_fltr_enable(self, val)`

#### `def ci_pulse_freq_dig_fltr_enable(self)`

#### `def ci_pulse_freq_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def ci_pulse_freq_dig_fltr_min_pulse_width(self, val)`

#### `def ci_pulse_freq_dig_fltr_min_pulse_width(self)`

#### `def ci_pulse_freq_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def ci_pulse_freq_dig_fltr_timebase_rate(self, val)`

#### `def ci_pulse_freq_dig_fltr_timebase_rate(self)`

#### `def ci_pulse_freq_dig_fltr_timebase_src(self)`


        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        

#### `def ci_pulse_freq_dig_fltr_timebase_src(self, val)`

#### `def ci_pulse_freq_dig_fltr_timebase_src(self)`

#### `def ci_pulse_freq_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def ci_pulse_freq_dig_sync_enable(self, val)`

#### `def ci_pulse_freq_dig_sync_enable(self)`

#### `def ci_pulse_freq_logic_lvl_behavior(self)`


        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the count reset line.
        

#### `def ci_pulse_freq_logic_lvl_behavior(self, val)`

#### `def ci_pulse_freq_logic_lvl_behavior(self)`

#### `def ci_pulse_freq_starting_edge(self)`


        :class:`nidaqmx.constants.Edge`: Specifies on which edge of the
            input signal to begin pulse measurement.
        

#### `def ci_pulse_freq_starting_edge(self, val)`

#### `def ci_pulse_freq_starting_edge(self)`

#### `def ci_pulse_freq_term(self)`


        str: Specifies the input terminal of the signal to measure.
        

#### `def ci_pulse_freq_term(self, val)`

#### `def ci_pulse_freq_term(self)`

#### `def ci_pulse_freq_term_cfg(self)`


        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        

#### `def ci_pulse_freq_term_cfg(self, val)`

#### `def ci_pulse_freq_term_cfg(self)`

#### `def ci_pulse_freq_units(self)`


        :class:`nidaqmx.constants.FrequencyUnits`: Specifies the units
            to use to return pulse specifications in terms of frequency.
        

#### `def ci_pulse_freq_units(self, val)`

#### `def ci_pulse_freq_units(self)`

#### `def ci_pulse_ticks_dig_fltr_enable(self)`


        bool: Specifies whether to apply a digital filter to the signal
            to measure.
        

#### `def ci_pulse_ticks_dig_fltr_enable(self, val)`

#### `def ci_pulse_ticks_dig_fltr_enable(self)`

#### `def ci_pulse_ticks_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def ci_pulse_ticks_dig_fltr_min_pulse_width(self, val)`

#### `def ci_pulse_ticks_dig_fltr_min_pulse_width(self)`

#### `def ci_pulse_ticks_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def ci_pulse_ticks_dig_fltr_timebase_rate(self, val)`

#### `def ci_pulse_ticks_dig_fltr_timebase_rate(self)`

#### `def ci_pulse_ticks_dig_fltr_timebase_src(self)`


        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        

#### `def ci_pulse_ticks_dig_fltr_timebase_src(self, val)`

#### `def ci_pulse_ticks_dig_fltr_timebase_src(self)`

#### `def ci_pulse_ticks_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def ci_pulse_ticks_dig_sync_enable(self, val)`

#### `def ci_pulse_ticks_dig_sync_enable(self)`

#### `def ci_pulse_ticks_logic_lvl_behavior(self)`


        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the count reset line.
        

#### `def ci_pulse_ticks_logic_lvl_behavior(self, val)`

#### `def ci_pulse_ticks_logic_lvl_behavior(self)`

#### `def ci_pulse_ticks_starting_edge(self)`


        :class:`nidaqmx.constants.Edge`: Specifies on which edge of the
            input signal to begin pulse measurement.
        

#### `def ci_pulse_ticks_starting_edge(self, val)`

#### `def ci_pulse_ticks_starting_edge(self)`

#### `def ci_pulse_ticks_term(self)`


        str: Specifies the input terminal of the signal to measure.
        

#### `def ci_pulse_ticks_term(self, val)`

#### `def ci_pulse_ticks_term(self)`

#### `def ci_pulse_ticks_term_cfg(self)`


        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        

#### `def ci_pulse_ticks_term_cfg(self, val)`

#### `def ci_pulse_ticks_term_cfg(self)`

#### `def ci_pulse_time_dig_fltr_enable(self)`


        bool: Specifies whether to apply a digital filter to the signal
            to measure.
        

#### `def ci_pulse_time_dig_fltr_enable(self, val)`

#### `def ci_pulse_time_dig_fltr_enable(self)`

#### `def ci_pulse_time_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def ci_pulse_time_dig_fltr_min_pulse_width(self, val)`

#### `def ci_pulse_time_dig_fltr_min_pulse_width(self)`

#### `def ci_pulse_time_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def ci_pulse_time_dig_fltr_timebase_rate(self, val)`

#### `def ci_pulse_time_dig_fltr_timebase_rate(self)`

#### `def ci_pulse_time_dig_fltr_timebase_src(self)`


        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        

#### `def ci_pulse_time_dig_fltr_timebase_src(self, val)`

#### `def ci_pulse_time_dig_fltr_timebase_src(self)`

#### `def ci_pulse_time_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def ci_pulse_time_dig_sync_enable(self, val)`

#### `def ci_pulse_time_dig_sync_enable(self)`

#### `def ci_pulse_time_logic_lvl_behavior(self)`


        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the count reset line.
        

#### `def ci_pulse_time_logic_lvl_behavior(self, val)`

#### `def ci_pulse_time_logic_lvl_behavior(self)`

#### `def ci_pulse_time_starting_edge(self)`


        :class:`nidaqmx.constants.Edge`: Specifies on which edge of the
            input signal to begin pulse measurement.
        

#### `def ci_pulse_time_starting_edge(self, val)`

#### `def ci_pulse_time_starting_edge(self)`

#### `def ci_pulse_time_term(self)`


        str: Specifies the input terminal of the signal to measure.
        

#### `def ci_pulse_time_term(self, val)`

#### `def ci_pulse_time_term(self)`

#### `def ci_pulse_time_term_cfg(self)`


        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        

#### `def ci_pulse_time_term_cfg(self, val)`

#### `def ci_pulse_time_term_cfg(self)`

#### `def ci_pulse_time_units(self)`


        :class:`nidaqmx.constants.TimeUnits`: Specifies the units to use
            to return pulse specifications in terms of high time and low
            time.
        

#### `def ci_pulse_time_units(self, val)`

#### `def ci_pulse_time_units(self)`

#### `def ci_pulse_width_dig_fltr_enable(self)`


        bool: Specifies whether to apply the pulse width filter to the
            signal.
        

#### `def ci_pulse_width_dig_fltr_enable(self, val)`

#### `def ci_pulse_width_dig_fltr_enable(self)`

#### `def ci_pulse_width_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def ci_pulse_width_dig_fltr_min_pulse_width(self, val)`

#### `def ci_pulse_width_dig_fltr_min_pulse_width(self)`

#### `def ci_pulse_width_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def ci_pulse_width_dig_fltr_timebase_rate(self, val)`

#### `def ci_pulse_width_dig_fltr_timebase_rate(self)`

#### `def ci_pulse_width_dig_fltr_timebase_src(self)`


        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        

#### `def ci_pulse_width_dig_fltr_timebase_src(self, val)`

#### `def ci_pulse_width_dig_fltr_timebase_src(self)`

#### `def ci_pulse_width_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def ci_pulse_width_dig_sync_enable(self, val)`

#### `def ci_pulse_width_dig_sync_enable(self)`

#### `def ci_pulse_width_logic_lvl_behavior(self)`


        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the input line.
        

#### `def ci_pulse_width_logic_lvl_behavior(self, val)`

#### `def ci_pulse_width_logic_lvl_behavior(self)`

#### `def ci_pulse_width_starting_edge(self)`


        :class:`nidaqmx.constants.Edge`: Specifies on which edge of the
            input signal to begin each pulse width measurement.
        

#### `def ci_pulse_width_starting_edge(self, val)`

#### `def ci_pulse_width_starting_edge(self)`

#### `def ci_pulse_width_term(self)`


        str: Specifies the input terminal of the signal to measure.
        

#### `def ci_pulse_width_term(self, val)`

#### `def ci_pulse_width_term(self)`

#### `def ci_pulse_width_term_cfg(self)`


        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        

#### `def ci_pulse_width_term_cfg(self, val)`

#### `def ci_pulse_width_term_cfg(self)`

#### `def ci_pulse_width_units(self)`


        :class:`nidaqmx.constants.TimeUnits`: Specifies the units to use
            to return pulse width measurements.
        

#### `def ci_pulse_width_units(self, val)`

#### `def ci_pulse_width_units(self)`

#### `def ci_samp_clk_overrun_behavior(self)`


        :class:`nidaqmx.constants.SampClkOverrunBehavior`: Specifies the
            counter behavior when data is read but a new value was not
            detected during a sample clock.
        

#### `def ci_samp_clk_overrun_behavior(self, val)`

#### `def ci_samp_clk_overrun_behavior(self)`

#### `def ci_samp_clk_overrun_sentinel_val(self)`


        int: Specifies the sentinel value returned when the No New
            Sample Behavior is set to Sentinel Value.
        

#### `def ci_samp_clk_overrun_sentinel_val(self, val)`

#### `def ci_samp_clk_overrun_sentinel_val(self)`

#### `def ci_semi_period_dig_fltr_enable(self)`


        bool: Specifies whether to apply the pulse width filter to the
            signal.
        

#### `def ci_semi_period_dig_fltr_enable(self, val)`

#### `def ci_semi_period_dig_fltr_enable(self)`

#### `def ci_semi_period_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def ci_semi_period_dig_fltr_min_pulse_width(self, val)`

#### `def ci_semi_period_dig_fltr_min_pulse_width(self)`

#### `def ci_semi_period_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def ci_semi_period_dig_fltr_timebase_rate(self, val)`

#### `def ci_semi_period_dig_fltr_timebase_rate(self)`

#### `def ci_semi_period_dig_fltr_timebase_src(self)`


        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        

#### `def ci_semi_period_dig_fltr_timebase_src(self, val)`

#### `def ci_semi_period_dig_fltr_timebase_src(self)`

#### `def ci_semi_period_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def ci_semi_period_dig_sync_enable(self, val)`

#### `def ci_semi_period_dig_sync_enable(self)`

#### `def ci_semi_period_logic_lvl_behavior(self)`


        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the count reset line.
        

#### `def ci_semi_period_logic_lvl_behavior(self, val)`

#### `def ci_semi_period_logic_lvl_behavior(self)`

#### `def ci_semi_period_starting_edge(self)`


        :class:`nidaqmx.constants.Edge`: Specifies on which edge of the
            input signal to begin semi-period measurement. Semi-period
            measurements alternate between high time and low time,
            starting on this edge.
        

#### `def ci_semi_period_starting_edge(self, val)`

#### `def ci_semi_period_starting_edge(self)`

#### `def ci_semi_period_term(self)`


        str: Specifies the input terminal of the signal to measure.
        

#### `def ci_semi_period_term(self, val)`

#### `def ci_semi_period_term(self)`

#### `def ci_semi_period_term_cfg(self)`


        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        

#### `def ci_semi_period_term_cfg(self, val)`

#### `def ci_semi_period_term_cfg(self)`

#### `def ci_semi_period_units(self)`


        :class:`nidaqmx.constants.TimeUnits`: Specifies the units to use
            to return semi-period measurements.
        

#### `def ci_semi_period_units(self, val)`

#### `def ci_semi_period_units(self)`

#### `def ci_tc_reached(self)`


        bool: Indicates whether the counter rolled over. When you query
            this property, NI-DAQmx resets it to False.
        

#### `def ci_thresh_voltage(self)`


        float: Specifies the digital threshold value in Volts for high
            and low input transitions. Some devices do not support this
            for differential channels.
        

#### `def ci_thresh_voltage(self, val)`

#### `def ci_thresh_voltage(self)`

#### `def ci_timestamp_initial_seconds(self)`


        int: Specifies the number of seconds that elapsed since the
            beginning of the current year. This value is ignored if
            **ci_gps_sync_method** is **GpsSignalType1.IRIGB**.
        

#### `def ci_timestamp_initial_seconds(self, val)`

#### `def ci_timestamp_initial_seconds(self)`

#### `def ci_timestamp_units(self)`


        :class:`nidaqmx.constants.TimeUnits`: Specifies the units to use
            to return timestamp measurements.
        

#### `def ci_timestamp_units(self, val)`

#### `def ci_timestamp_units(self)`

#### `def ci_two_edge_sep_first_dig_fltr_enable(self)`


        bool: Specifies whether to apply the pulse width filter to the
            signal.
        

#### `def ci_two_edge_sep_first_dig_fltr_enable(self, val)`

#### `def ci_two_edge_sep_first_dig_fltr_enable(self)`

#### `def ci_two_edge_sep_first_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def ci_two_edge_sep_first_dig_fltr_min_pulse_width(self, val)`

#### `def ci_two_edge_sep_first_dig_fltr_min_pulse_width(self)`

#### `def ci_two_edge_sep_first_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def ci_two_edge_sep_first_dig_fltr_timebase_rate(self, val)`

#### `def ci_two_edge_sep_first_dig_fltr_timebase_rate(self)`

#### `def ci_two_edge_sep_first_dig_fltr_timebase_src(self)`


        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        

#### `def ci_two_edge_sep_first_dig_fltr_timebase_src(self, val)`

#### `def ci_two_edge_sep_first_dig_fltr_timebase_src(self)`

#### `def ci_two_edge_sep_first_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def ci_two_edge_sep_first_dig_sync_enable(self, val)`

#### `def ci_two_edge_sep_first_dig_sync_enable(self)`

#### `def ci_two_edge_sep_first_edge(self)`


        :class:`nidaqmx.constants.Edge`: Specifies on which edge of the
            first signal to start each measurement.
        

#### `def ci_two_edge_sep_first_edge(self, val)`

#### `def ci_two_edge_sep_first_edge(self)`

#### `def ci_two_edge_sep_first_logic_lvl_behavior(self)`


        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the input line.
        

#### `def ci_two_edge_sep_first_logic_lvl_behavior(self, val)`

#### `def ci_two_edge_sep_first_logic_lvl_behavior(self)`

#### `def ci_two_edge_sep_first_term(self)`


        str: Specifies the source terminal of the digital signal that
            starts each measurement.
        

#### `def ci_two_edge_sep_first_term(self, val)`

#### `def ci_two_edge_sep_first_term(self)`

#### `def ci_two_edge_sep_first_term_cfg(self)`


        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        

#### `def ci_two_edge_sep_first_term_cfg(self, val)`

#### `def ci_two_edge_sep_first_term_cfg(self)`

#### `def ci_two_edge_sep_second_dig_fltr_enable(self)`


        bool: Specifies whether to apply the pulse width filter to the
            signal.
        

#### `def ci_two_edge_sep_second_dig_fltr_enable(self, val)`

#### `def ci_two_edge_sep_second_dig_fltr_enable(self)`

#### `def ci_two_edge_sep_second_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def ci_two_edge_sep_second_dig_fltr_min_pulse_width(self, val)`

#### `def ci_two_edge_sep_second_dig_fltr_min_pulse_width(self)`

#### `def ci_two_edge_sep_second_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def ci_two_edge_sep_second_dig_fltr_timebase_rate(self, val)`

#### `def ci_two_edge_sep_second_dig_fltr_timebase_rate(self)`

#### `def ci_two_edge_sep_second_dig_fltr_timebase_src(self)`


        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        

#### `def ci_two_edge_sep_second_dig_fltr_timebase_src(self, val)`

#### `def ci_two_edge_sep_second_dig_fltr_timebase_src(self)`

#### `def ci_two_edge_sep_second_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def ci_two_edge_sep_second_dig_sync_enable(self, val)`

#### `def ci_two_edge_sep_second_dig_sync_enable(self)`

#### `def ci_two_edge_sep_second_edge(self)`


        :class:`nidaqmx.constants.Edge`: Specifies on which edge of the
            second signal to stop each measurement.
        

#### `def ci_two_edge_sep_second_edge(self, val)`

#### `def ci_two_edge_sep_second_edge(self)`

#### `def ci_two_edge_sep_second_logic_lvl_behavior(self)`


        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior on the count reset line.
        

#### `def ci_two_edge_sep_second_logic_lvl_behavior(self, val)`

#### `def ci_two_edge_sep_second_logic_lvl_behavior(self)`

#### `def ci_two_edge_sep_second_term(self)`


        str: Specifies the source terminal of the digital signal that
            stops each measurement.
        

#### `def ci_two_edge_sep_second_term(self, val)`

#### `def ci_two_edge_sep_second_term(self)`

#### `def ci_two_edge_sep_second_term_cfg(self)`


        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        

#### `def ci_two_edge_sep_second_term_cfg(self, val)`

#### `def ci_two_edge_sep_second_term_cfg(self)`

#### `def ci_two_edge_sep_units(self)`


        :class:`nidaqmx.constants.TimeUnits`: Specifies the units to use
            to return two-edge separation measurements from the channel.
        

#### `def ci_two_edge_sep_units(self, val)`

#### `def ci_two_edge_sep_units(self)`

#### `def ci_usb_xfer_req_count(self)`


        int: Specifies the maximum number of simultaneous USB transfers
            used to stream data. Modify this value to affect performance
            under different combinations of operating system and device.
        

#### `def ci_usb_xfer_req_count(self, val)`

#### `def ci_usb_xfer_req_count(self)`

#### `def ci_usb_xfer_req_size(self)`


        int: Specifies the maximum size of a USB transfer request in
            bytes. Modify this value to affect performance under
            different combinations of operating system and device.
        

#### `def ci_usb_xfer_req_size(self, val)`

#### `def ci_usb_xfer_req_size(self)`

#### `def ci_velocity_a_input_dig_fltr_enable(self)`


        bool: Specifies whether to apply the pulse width filter to the
            signal.
        

#### `def ci_velocity_a_input_dig_fltr_enable(self, val)`

#### `def ci_velocity_a_input_dig_fltr_enable(self)`

#### `def ci_velocity_a_input_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the digital
            filter recognizes.
        

#### `def ci_velocity_a_input_dig_fltr_min_pulse_width(self, val)`

#### `def ci_velocity_a_input_dig_fltr_min_pulse_width(self)`

#### `def ci_velocity_a_input_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def ci_velocity_a_input_dig_fltr_timebase_rate(self, val)`

#### `def ci_velocity_a_input_dig_fltr_timebase_rate(self)`

#### `def ci_velocity_a_input_dig_fltr_timebase_src(self)`


        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        

#### `def ci_velocity_a_input_dig_fltr_timebase_src(self, val)`

#### `def ci_velocity_a_input_dig_fltr_timebase_src(self)`

#### `def ci_velocity_a_input_logic_lvl_behavior(self)`


        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior of the input terminal.
        

#### `def ci_velocity_a_input_logic_lvl_behavior(self, val)`

#### `def ci_velocity_a_input_logic_lvl_behavior(self)`

#### `def ci_velocity_a_input_term(self)`


        str: Specifies the terminal to which signal A is connected.
        

#### `def ci_velocity_a_input_term(self, val)`

#### `def ci_velocity_a_input_term(self)`

#### `def ci_velocity_a_input_term_cfg(self)`


        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        

#### `def ci_velocity_a_input_term_cfg(self, val)`

#### `def ci_velocity_a_input_term_cfg(self)`

#### `def ci_velocity_ang_encoder_pulses_per_rev(self)`


        int: Specifies the number of pulses the encoder generates per
            revolution. This value is the number of pulses on either
            signal A or signal B, not the total number of pulses on both
            signal A and signal B.
        

#### `def ci_velocity_ang_encoder_pulses_per_rev(self, val)`

#### `def ci_velocity_ang_encoder_pulses_per_rev(self)`

#### `def ci_velocity_ang_encoder_units(self)`


        :class:`nidaqmx.constants.AngularVelocityUnits`: Specifies the
            units to use to return angular velocity counter
            measurements.
        

#### `def ci_velocity_ang_encoder_units(self, val)`

#### `def ci_velocity_ang_encoder_units(self)`

#### `def ci_velocity_b_input_dig_fltr_enable(self)`


        bool: Specifies whether to apply the pulse width filter to the
            signal.
        

#### `def ci_velocity_b_input_dig_fltr_enable(self, val)`

#### `def ci_velocity_b_input_dig_fltr_enable(self)`

#### `def ci_velocity_b_input_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the digital
            filter recognizes.
        

#### `def ci_velocity_b_input_dig_fltr_min_pulse_width(self, val)`

#### `def ci_velocity_b_input_dig_fltr_min_pulse_width(self)`

#### `def ci_velocity_b_input_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def ci_velocity_b_input_dig_fltr_timebase_rate(self, val)`

#### `def ci_velocity_b_input_dig_fltr_timebase_rate(self)`

#### `def ci_velocity_b_input_dig_fltr_timebase_src(self)`


        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        

#### `def ci_velocity_b_input_dig_fltr_timebase_src(self, val)`

#### `def ci_velocity_b_input_dig_fltr_timebase_src(self)`

#### `def ci_velocity_b_input_logic_lvl_behavior(self)`


        :class:`nidaqmx.constants.LogicLvlBehavior`: Specifies the logic
            level behavior of the input terminal.
        

#### `def ci_velocity_b_input_logic_lvl_behavior(self, val)`

#### `def ci_velocity_b_input_logic_lvl_behavior(self)`

#### `def ci_velocity_b_input_term(self)`


        str: Specifies the terminal to which signal B is connected.
        

#### `def ci_velocity_b_input_term(self, val)`

#### `def ci_velocity_b_input_term(self)`

#### `def ci_velocity_b_input_term_cfg(self)`


        :class:`nidaqmx.constants.TerminalConfiguration`: Specifies the
            input terminal configuration.
        

#### `def ci_velocity_b_input_term_cfg(self, val)`

#### `def ci_velocity_b_input_term_cfg(self)`

#### `def ci_velocity_div(self)`


        int: Specifies the value by which to divide the input signal.
        

#### `def ci_velocity_div(self, val)`

#### `def ci_velocity_div(self)`

#### `def ci_velocity_encoder_decoding_type(self)`


        :class:`nidaqmx.constants.EncoderType`: Specifies how to count
            and interpret the pulses the encoder generates on signal A
            and signal B. X1, X2, and X4 are valid for quadrature
            encoders only. Two Pulse Counting is valid for two-pulse
            encoders only.
        

#### `def ci_velocity_encoder_decoding_type(self, val)`

#### `def ci_velocity_encoder_decoding_type(self)`

#### `def ci_velocity_lin_encoder_dist_per_pulse(self)`


        float: Specifies the distance to measure for each pulse the
            encoder generates on signal A or signal B. This value is in
            the units you specify in CI.Velocity.LinEncoder.DistUnits.
        

#### `def ci_velocity_lin_encoder_dist_per_pulse(self, val)`

#### `def ci_velocity_lin_encoder_dist_per_pulse(self)`

#### `def ci_velocity_lin_encoder_units(self)`


        :class:`nidaqmx.constants.VelocityUnits`: Specifies the units to
            use to return linear encoder velocity measurements from the
            channel.
        

#### `def ci_velocity_lin_encoder_units(self, val)`

#### `def ci_velocity_lin_encoder_units(self)`

#### `def ci_velocity_meas_time(self)`


        float: Specifies in seconds the length of time to measure the
            velocity of the signal.
        

#### `def ci_velocity_meas_time(self, val)`

#### `def ci_velocity_meas_time(self)`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/channels/_co_channel.py -->
## PYTHON MODULE: generated/nidaqmx/task/channels/_co_channel.py

### `class COChannel(Channel)`


    Represents one or more counter output virtual channels and their properties.
    

#### `def __repr__(self)`

#### `def co_auto_incr_cnt(self)`


        int: Specifies a number of timebase ticks by which to increase
            the time spent in the idle state for each successive pulse.
        

#### `def co_auto_incr_cnt(self, val)`

#### `def co_auto_incr_cnt(self)`

#### `def co_constrained_gen_mode(self)`


        :class:`nidaqmx.constants.ConstrainedGenMode`: Specifies
            constraints to apply when the counter generates pulses.
            Constraining the counter reduces the device resources
            required for counter operation. Constraining the counter can
            also allow additional analog or counter tasks on the device
            to run concurrently. For continuous counter tasks, NI-DAQmx
            consumes no device resources when the counter is
            constrained. For finite counter tasks, resource use
            increases with the frequency regardless of the constraint
            mode. However, fixed frequency constraints significantly
            reduce resource usage, and fixed duty cycle constraint
            marginally reduces it.
        

#### `def co_constrained_gen_mode(self, val)`

#### `def co_constrained_gen_mode(self)`

#### `def co_count(self)`


        int: Indicates the current value of the count register.
        

#### `def co_ctr_timebase_active_edge(self)`


        :class:`nidaqmx.constants.Edge`: Specifies whether a timebase
            cycle is from rising edge to rising edge or from falling
            edge to falling edge.
        

#### `def co_ctr_timebase_active_edge(self, val)`

#### `def co_ctr_timebase_active_edge(self)`

#### `def co_ctr_timebase_dig_fltr_enable(self)`


        bool: Specifies whether to apply the pulse width filter to the
            signal.
        

#### `def co_ctr_timebase_dig_fltr_enable(self, val)`

#### `def co_ctr_timebase_dig_fltr_enable(self)`

#### `def co_ctr_timebase_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def co_ctr_timebase_dig_fltr_min_pulse_width(self, val)`

#### `def co_ctr_timebase_dig_fltr_min_pulse_width(self)`

#### `def co_ctr_timebase_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def co_ctr_timebase_dig_fltr_timebase_rate(self, val)`

#### `def co_ctr_timebase_dig_fltr_timebase_rate(self)`

#### `def co_ctr_timebase_dig_fltr_timebase_src(self)`


        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        

#### `def co_ctr_timebase_dig_fltr_timebase_src(self, val)`

#### `def co_ctr_timebase_dig_fltr_timebase_src(self)`

#### `def co_ctr_timebase_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def co_ctr_timebase_dig_sync_enable(self, val)`

#### `def co_ctr_timebase_dig_sync_enable(self)`

#### `def co_ctr_timebase_master_timebase_div(self)`


        int: Specifies the divisor for an external counter timebase. You
            can divide the counter timebase in order to generate slower
            signals without causing the count register to roll over.
        

#### `def co_ctr_timebase_master_timebase_div(self, val)`

#### `def co_ctr_timebase_master_timebase_div(self)`

#### `def co_ctr_timebase_rate(self)`


        float: Specifies in Hertz the frequency of the counter timebase.
            Specifying the rate of a counter timebase allows you to
            define output pulses in seconds rather than in ticks of the
            timebase. If you use an external timebase and do not specify
            the rate, you can define output pulses only in ticks of the
            timebase.
        

#### `def co_ctr_timebase_rate(self, val)`

#### `def co_ctr_timebase_rate(self)`

#### `def co_ctr_timebase_src(self)`


        str: Specifies the terminal of the timebase to use for the
            counter. Typically, NI-DAQmx uses one of the internal
            counter timebases when generating pulses. Use this property
            to specify an external timebase and produce custom pulse
            widths that are not possible using the internal timebases.
        

#### `def co_ctr_timebase_src(self, val)`

#### `def co_ctr_timebase_src(self)`

#### `def co_data_xfer_mech(self)`


        :class:`nidaqmx.constants.DataTransferActiveTransferMode`:
            Specifies the data transfer mode for the device. For
            buffered operations, use DMA or USB Bulk. For non-buffered
            operations, use Polled.
        

#### `def co_data_xfer_mech(self, val)`

#### `def co_data_xfer_mech(self)`

#### `def co_data_xfer_req_cond(self)`


        :class:`nidaqmx.constants.OutputDataTransferCondition`:
            Specifies under what condition to transfer data from the
            buffer to the onboard memory of the device.
        

#### `def co_data_xfer_req_cond(self, val)`

#### `def co_data_xfer_req_cond(self)`

#### `def co_enable_initial_delay_on_retrigger(self)`


        bool: Specifies whether to apply the initial delay to
            retriggered pulse trains.
        

#### `def co_enable_initial_delay_on_retrigger(self, val)`

#### `def co_enable_initial_delay_on_retrigger(self)`

#### `def co_mem_map_enable(self)`


        bool: Specifies for NI-DAQmx to map hardware registers to the
            memory space of the application, if possible. Normally, NI-
            DAQmx maps hardware registers to memory accessible only to
            the kernel. Mapping the registers to the memory space of the
            application increases performance. However, if the
            application accesses the memory space mapped to the
            registers, it can adversely affect the operation of the
            device and possibly result in a system crash.
        

#### `def co_mem_map_enable(self, val)`

#### `def co_mem_map_enable(self)`

#### `def co_output_state(self)`


        :class:`nidaqmx.constants.Level`: Indicates the current state of
            the output terminal of the counter.
        

#### `def co_output_type(self)`


        :class:`nidaqmx.constants.UsageTypeCO`: Indicates how to define
            pulses generated on the channel.
        

#### `def co_prescaler(self)`


        int: Specifies the divisor to apply to the signal you connect to
            the counter source terminal. Pulse generations defined by
            frequency or time take this setting into account, but pulse
            generations defined by ticks do not. You should use a
            prescaler only when you connect an external signal to the
            counter source terminal and when that signal has a higher
            frequency than the fastest onboard timebase.
        

#### `def co_prescaler(self, val)`

#### `def co_prescaler(self)`

#### `def co_pulse_done(self)`


        bool: Indicates if the task completed pulse generation. Use this
            value for retriggerable pulse generation when you need to
            determine if the device generated the current pulse. For
            retriggerable tasks, when you query this property, NI-DAQmx
            resets it to False.
        

#### `def co_pulse_duty_cyc(self)`


        float: Specifies the duty cycle of the pulses. The duty cycle of
            a signal is the width of the pulse divided by period. NI-
            DAQmx uses this ratio and the pulse frequency to determine
            the width of the pulses and the delay between pulses.
        

#### `def co_pulse_duty_cyc(self, val)`

#### `def co_pulse_duty_cyc(self)`

#### `def co_pulse_freq(self)`


        float: Specifies the frequency of the pulses to generate. This
            value is in the units you specify with
            **co_pulse_freq_units** or when you create the channel.
        

#### `def co_pulse_freq(self, val)`

#### `def co_pulse_freq(self)`

#### `def co_pulse_freq_initial_delay(self)`


        float: Specifies in seconds the amount of time to wait before
            generating the first pulse.
        

#### `def co_pulse_freq_initial_delay(self, val)`

#### `def co_pulse_freq_initial_delay(self)`

#### `def co_pulse_freq_units(self)`


        :class:`nidaqmx.constants.FrequencyUnits`: Specifies the units
            in which to define pulse frequency.
        

#### `def co_pulse_freq_units(self, val)`

#### `def co_pulse_freq_units(self)`

#### `def co_pulse_high_ticks(self)`


        int: Specifies the number of ticks the pulse is high.
        

#### `def co_pulse_high_ticks(self, val)`

#### `def co_pulse_high_ticks(self)`

#### `def co_pulse_high_time(self)`


        float: Specifies the amount of time that the pulse is at a high
            voltage. This value is in the units you specify with
            **co_pulse_time_units** or when you create the channel.
        

#### `def co_pulse_high_time(self, val)`

#### `def co_pulse_high_time(self)`

#### `def co_pulse_idle_state(self)`


        :class:`nidaqmx.constants.Level`: Specifies the resting state of
            the output terminal.
        

#### `def co_pulse_idle_state(self, val)`

#### `def co_pulse_idle_state(self)`

#### `def co_pulse_low_ticks(self)`


        int: Specifies the number of ticks the pulse is low.
        

#### `def co_pulse_low_ticks(self, val)`

#### `def co_pulse_low_ticks(self)`

#### `def co_pulse_low_time(self)`


        float: Specifies the amount of time that the pulse is at a low
            voltage. This value is in the units you specify with
            **co_pulse_time_units** or when you create the channel.
        

#### `def co_pulse_low_time(self, val)`

#### `def co_pulse_low_time(self)`

#### `def co_pulse_term(self)`


        str: Specifies on which terminal to generate pulses.
        

#### `def co_pulse_term(self, val)`

#### `def co_pulse_term(self)`

#### `def co_pulse_ticks_initial_delay(self)`


        int: Specifies the number of ticks to wait before generating the
            first pulse.
        

#### `def co_pulse_ticks_initial_delay(self, val)`

#### `def co_pulse_ticks_initial_delay(self)`

#### `def co_pulse_time_initial_delay(self)`


        float: Specifies in seconds the amount of time to wait before
            generating the first pulse.
        

#### `def co_pulse_time_initial_delay(self, val)`

#### `def co_pulse_time_initial_delay(self)`

#### `def co_pulse_time_units(self)`


        :class:`nidaqmx.constants.TimeUnits`: Specifies the units in
            which to define high and low pulse time.
        

#### `def co_pulse_time_units(self, val)`

#### `def co_pulse_time_units(self)`

#### `def co_rdy_for_new_val(self)`


        bool: Indicates whether the counter is ready for new continuous
            pulse train values.
        

#### `def co_usb_xfer_req_count(self)`


        int: Specifies the maximum number of simultaneous USB transfers
            used to stream data. Modify this value to affect performance
            under different combinations of operating system and device.
        

#### `def co_usb_xfer_req_count(self, val)`

#### `def co_usb_xfer_req_count(self)`

#### `def co_usb_xfer_req_size(self)`


        int: Specifies the maximum size of a USB transfer request in
            bytes. Modify this value to affect performance under
            different combinations of operating system and device.
        

#### `def co_usb_xfer_req_size(self, val)`

#### `def co_usb_xfer_req_size(self)`

#### `def co_use_only_on_brd_mem(self)`


        bool: Specifies whether to write samples directly to the onboard
            memory of the device, bypassing the memory buffer.
            Generally, you cannot update onboard memory directly after
            you start the task. Onboard memory includes data FIFOs.
        

#### `def co_use_only_on_brd_mem(self, val)`

#### `def co_use_only_on_brd_mem(self)`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/channels/_di_channel.py -->
## PYTHON MODULE: generated/nidaqmx/task/channels/_di_channel.py

### `class DIChannel(Channel)`


    Represents one or more digital input virtual channels and their properties.
    

#### `def __repr__(self)`

#### `def di_acquire_on(self)`


        :class:`nidaqmx.constants.ActiveOrInactiveEdgeSelection`:
            Specifies on which edge of the sample clock to acquire
            samples.
        

#### `def di_acquire_on(self, val)`

#### `def di_acquire_on(self)`

#### `def di_data_xfer_mech(self)`


        :class:`nidaqmx.constants.DataTransferActiveTransferMode`:
            Specifies the data transfer mode for the device.
        

#### `def di_data_xfer_mech(self, val)`

#### `def di_data_xfer_mech(self)`

#### `def di_data_xfer_req_cond(self)`


        :class:`nidaqmx.constants.InputDataTransferCondition`: Specifies
            under what condition to transfer data from the onboard
            memory of the device to the buffer.
        

#### `def di_data_xfer_req_cond(self, val)`

#### `def di_data_xfer_req_cond(self)`

#### `def di_dig_fltr_enable(self)`


        bool: Specifies whether to enable the digital filter for the
            line(s) or port(s). You can enable the filter on a line-by-
            line basis. You do not have to enable the filter for all
            lines in a channel.
        

#### `def di_dig_fltr_enable(self, val)`

#### `def di_dig_fltr_enable(self)`

#### `def di_dig_fltr_enable_bus_mode(self)`


        bool: Specifies whether to enable bus mode for digital
            filtering. If you set this property to True, NI-DAQmx treats
            all lines that use common filtering settings as a bus. If
            any line in the bus has jitter, all lines in the bus hold
            state until the entire bus stabilizes, or until 2 times the
            minimum pulse width elapses. If you set this property to
            False, NI-DAQmx filters all lines individually. Jitter in
            one line does not affect other lines.
        

#### `def di_dig_fltr_enable_bus_mode(self, val)`

#### `def di_dig_fltr_enable_bus_mode(self)`

#### `def di_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes as a valid high or low state transition.
        

#### `def di_dig_fltr_min_pulse_width(self, val)`

#### `def di_dig_fltr_min_pulse_width(self)`

#### `def di_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def di_dig_fltr_timebase_rate(self, val)`

#### `def di_dig_fltr_timebase_rate(self)`

#### `def di_dig_fltr_timebase_src(self)`


        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        

#### `def di_dig_fltr_timebase_src(self, val)`

#### `def di_dig_fltr_timebase_src(self)`

#### `def di_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def di_dig_sync_enable(self, val)`

#### `def di_dig_sync_enable(self)`

#### `def di_invert_lines(self)`


        bool: Specifies whether to invert the lines in the channel. If
            you set this property to True, the lines are at high logic
            when off and at low logic when on.
        

#### `def di_invert_lines(self, val)`

#### `def di_invert_lines(self)`

#### `def di_logic_family(self)`


        :class:`nidaqmx.constants.LogicFamily`: Specifies the logic
            family to use for acquisition. A logic family corresponds to
            voltage thresholds that are compatible with a group of
            voltage standards. Refer to the device documentation for
            information on the logic high and logic low voltages for
            these logic families.
        

#### `def di_logic_family(self, val)`

#### `def di_logic_family(self)`

#### `def di_mem_map_enable(self)`


        bool: Specifies for NI-DAQmx to map hardware registers to the
            memory space of the application, if possible. Normally, NI-
            DAQmx maps hardware registers to memory accessible only to
            the kernel. Mapping the registers to the memory space of the
            application increases performance. However, if the
            application accesses the memory space mapped to the
            registers, it can adversely affect the operation of the
            device and possibly result in a system crash.
        

#### `def di_mem_map_enable(self, val)`

#### `def di_mem_map_enable(self)`

#### `def di_num_lines(self)`


        int: Indicates the number of digital lines in the channel.
        

#### `def di_tristate(self)`


        bool: Specifies whether to tristate the lines in the channel. If
            you set this property to True, NI-DAQmx tristates the lines
            in the channel. If you set this property to False, NI-DAQmx
            does not modify the configuration of the lines even if the
            lines were previously tristated. Set this property to False
            to read lines in other tasks or to read output-only lines.
        

#### `def di_tristate(self, val)`

#### `def di_tristate(self)`

#### `def di_usb_xfer_req_count(self)`


        int: Specifies the maximum number of simultaneous USB transfers
            used to stream data. Modify this value to affect performance
            under different combinations of operating system and device.
        

#### `def di_usb_xfer_req_count(self, val)`

#### `def di_usb_xfer_req_count(self)`

#### `def di_usb_xfer_req_size(self)`


        int: Specifies the maximum size of a USB transfer request in
            bytes. Modify this value to affect performance under
            different combinations of operating system and device.
        

#### `def di_usb_xfer_req_size(self, val)`

#### `def di_usb_xfer_req_size(self)`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/channels/_do_channel.py -->
## PYTHON MODULE: generated/nidaqmx/task/channels/_do_channel.py

### `class DOChannel(Channel)`


    Represents one or more digital output virtual channels and their properties.
    

#### `def __repr__(self)`

#### `def do_data_xfer_mech(self)`


        :class:`nidaqmx.constants.DataTransferActiveTransferMode`:
            Specifies the data transfer mode for the device.
        

#### `def do_data_xfer_mech(self, val)`

#### `def do_data_xfer_mech(self)`

#### `def do_data_xfer_req_cond(self)`


        :class:`nidaqmx.constants.OutputDataTransferCondition`:
            Specifies under what condition to transfer data from the
            buffer to the onboard memory of the device.
        

#### `def do_data_xfer_req_cond(self, val)`

#### `def do_data_xfer_req_cond(self)`

#### `def do_generate_on(self)`


        :class:`nidaqmx.constants.ActiveOrInactiveEdgeSelection`:
            Specifies on which edge of the sample clock to generate
            samples.
        

#### `def do_generate_on(self, val)`

#### `def do_generate_on(self)`

#### `def do_invert_lines(self)`


        bool: Specifies whether to invert the lines in the channel. If
            you set this property to True, the lines are at high logic
            when off and at low logic when on.
        

#### `def do_invert_lines(self, val)`

#### `def do_invert_lines(self)`

#### `def do_line_states_done_state(self)`


        :class:`nidaqmx.constants.Level`: Specifies the state of the
            lines in a digital output task when the task completes
            execution.
        

#### `def do_line_states_done_state(self, val)`

#### `def do_line_states_done_state(self)`

#### `def do_line_states_paused_state(self)`


        :class:`nidaqmx.constants.Level`: Specifies the state of the
            lines in a digital output task when the task pauses.
        

#### `def do_line_states_paused_state(self, val)`

#### `def do_line_states_paused_state(self)`

#### `def do_line_states_start_state(self)`


        :class:`nidaqmx.constants.Level`: Specifies the state of the
            lines in a digital output task when the task starts.
        

#### `def do_line_states_start_state(self, val)`

#### `def do_line_states_start_state(self)`

#### `def do_logic_family(self)`


        :class:`nidaqmx.constants.LogicFamily`: Specifies the logic
            family to use for generation. A logic family corresponds to
            voltage thresholds that are compatible with a group of
            voltage standards. Refer to the device documentation for
            information on the logic high and logic low voltages for
            these logic families.
        

#### `def do_logic_family(self, val)`

#### `def do_logic_family(self)`

#### `def do_mem_map_enable(self)`


        bool: Specifies for NI-DAQmx to map hardware registers to the
            memory space of the application, if possible. Normally, NI-
            DAQmx maps hardware registers to memory accessible only to
            the kernel. Mapping the registers to the memory space of the
            application increases performance. However, if the
            application accesses the memory space mapped to the
            registers, it can adversely affect the operation of the
            device and possibly result in a system crash.
        

#### `def do_mem_map_enable(self, val)`

#### `def do_mem_map_enable(self)`

#### `def do_num_lines(self)`


        int: Indicates the number of digital lines in the channel.
        

#### `def do_output_drive_type(self)`


        :class:`nidaqmx.constants.DigitalDriveType`: Specifies the drive
            type for digital output channels.
        

#### `def do_output_drive_type(self, val)`

#### `def do_output_drive_type(self)`

#### `def do_overcurrent_auto_reenable(self)`


        bool: Specifies whether to automatically reenable channels after
            they no longer exceed the current limit specified by
            **do_overcurrent_limit**.
        

#### `def do_overcurrent_auto_reenable(self, val)`

#### `def do_overcurrent_auto_reenable(self)`

#### `def do_overcurrent_limit(self)`


        float: Specifies the current threshold in Amperes for the
            channel. A value of 0 means the channel observes no limit.
            Devices can monitor only a finite number of current
            thresholds simultaneously. If you attempt to monitor
            additional thresholds, NI-DAQmx returns an error.
        

#### `def do_overcurrent_limit(self, val)`

#### `def do_overcurrent_limit(self)`

#### `def do_overcurrent_reenable_period(self)`


        float: Specifies the delay in seconds between the time a channel
            no longer exceeds the current limit and the reactivation of
            that channel, if **do_overcurrent_auto_reenable** is True.
        

#### `def do_overcurrent_reenable_period(self, val)`

#### `def do_overcurrent_reenable_period(self)`

#### `def do_tristate(self)`


        bool: Specifies whether to stop driving the channel and set it
            to a high-impedance state. You must commit the task for this
            setting to take effect.
        

#### `def do_tristate(self, val)`

#### `def do_tristate(self)`

#### `def do_usb_xfer_req_count(self)`


        int: Specifies the maximum number of simultaneous USB transfers
            used to stream data. Modify this value to affect performance
            under different combinations of operating system and device.
        

#### `def do_usb_xfer_req_count(self, val)`

#### `def do_usb_xfer_req_count(self)`

#### `def do_usb_xfer_req_size(self)`


        int: Specifies the maximum size of a USB transfer request in
            bytes. Modify this value to affect performance under
            different combinations of operating system and device.
        

#### `def do_usb_xfer_req_size(self, val)`

#### `def do_usb_xfer_req_size(self)`

#### `def do_use_only_on_brd_mem(self)`


        bool: Specifies whether to write samples directly to the onboard
            memory of the device, bypassing the memory buffer.
            Generally, you cannot update onboard memory after you start
            the task. Onboard memory includes data FIFOs.
        

#### `def do_use_only_on_brd_mem(self, val)`

#### `def do_use_only_on_brd_mem(self)`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/collections/__init__.py -->
## PYTHON MODULE: generated/nidaqmx/task/collections/__init__.py

### MODULE DOCSTRING

NI-DAQmx channel collection classes.

- `__all__ = ['ChannelCollection', 'AIChannelCollection', 'AOChannelCollection', 'CIChannelCollection', 'COChannelCollection', 'DIChannelCollection', 'DOChannelCollection']`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/collections/_ai_channel_collection.py -->
## PYTHON MODULE: generated/nidaqmx/task/collections/_ai_channel_collection.py

### `class AIChannelCollection(ChannelCollection)`


    Contains the collection of analog input channels for a DAQmx Task.
    

#### `def __init__(self, task_handle, interpreter)`


        Do not construct this object directly; instead, construct a nidaqmx.Task and use the task.ai_channels property.
        

#### `def _create_chan(self, physical_channel, name_to_assign_to_channel='')`


        Creates and returns an AIChannel object.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels.
            name_to_assign_to_channel (Optional[str]): Specifies a name to
                assign to the virtual channel this method creates.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Specifies the newly created AIChannel object.
        

#### `def add_ai_accel_4_wire_dc_voltage_chan(self, physical_channel, name_to_assign_to_channel='', terminal_config=TerminalConfiguration.DEFAULT, min_val=-5.0, max_val=5.0, units=AccelUnits.G, sensitivity=1000.0, sensitivity_units=AccelSensitivityUnits.MILLIVOLTS_PER_G, voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=0.0, use_excit_for_scaling=False, custom_scale_name='')`


        Creates channel(s) to measure acceleration. Use this instance
        for custom sensors that require excitation. You can use the
        excitation to scale the measurement.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.AccelUnits]): Specifies
                the units to use to return acceleration measurements
                from the channel.
            sensitivity (Optional[float]): Is the sensitivity of the
                sensor. This value is in the units you specify with the
                **sensitivity_units** input. Refer to the sensor
                documentation to determine this value.
            sensitivity_units (Optional[nidaqmx.constants.AccelSensitivityUnits]): 
                Specifies the units of the **sensitivity** input.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            use_excit_for_scaling (Optional[bool]): Specifies if NI-
                DAQmx divides the measurement by the excitation. You
                should typically set **use_excit_for_scaling** to True
                for ratiometric transducers. If you set
                **use_excit_for_scaling** to True, set **max_val** and
                **min_val** to reflect the scaling.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_accel_chan(self, physical_channel, name_to_assign_to_channel='', terminal_config=TerminalConfiguration.DEFAULT, min_val=-5.0, max_val=5.0, units=AccelUnits.G, sensitivity=1000.0, sensitivity_units=AccelSensitivityUnits.MILLIVOLTS_PER_G, current_excit_source=ExcitationSource.INTERNAL, current_excit_val=0.004, custom_scale_name='')`


        Creates channel(s) that use an accelerometer to measure
        acceleration.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.AccelUnits]): Specifies
                the units to use to return acceleration measurements
                from the channel.
            sensitivity (Optional[float]): Is the sensitivity of the
                sensor. This value is in the units you specify with the
                **sensitivity_units** input. Refer to the sensor
                documentation to determine this value.
            sensitivity_units (Optional[nidaqmx.constants.AccelSensitivityUnits]): 
                Specifies the units of the **sensitivity** input.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_accel_charge_chan(self, physical_channel, name_to_assign_to_channel='', terminal_config=TerminalConfiguration.DEFAULT, min_val=-5.0, max_val=5.0, units=AccelUnits.G, sensitivity=100.0, sensitivity_units=AccelChargeSensitivityUnits.PICO_COULOMBS_PER_G, custom_scale_name='')`


        Creates channel(s) that use a charge-based sensor to measure
        acceleration.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.AccelUnits]): Specifies
                the units to use to return acceleration measurements
                from the channel.
            sensitivity (Optional[float]): Is the sensitivity of the
                sensor. This value is in the units you specify with the
                **sensitivity_units** input. Refer to the sensor
                documentation to determine this value.
            sensitivity_units (Optional[nidaqmx.constants.AccelChargeSensitivityUnits]): 
                Specifies the units of the **sensitivity** input.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_bridge_chan(self, physical_channel, name_to_assign_to_channel='', min_val=-0.002, max_val=0.002, units=BridgeUnits.VOLTS_PER_VOLT, bridge_config=BridgeConfiguration.FULL_BRIDGE, voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=2.5, nominal_bridge_resistance=350.0, custom_scale_name='')`


        Creates channel(s) that measure voltage ratios from a Wheatstone
        bridge. Use this instance with bridge-based sensors that measure
        phenomena other than strain, force, pressure, or torque, or that
        scale data to physical units NI-DAQmx does not support.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.BridgeUnits]): Specifies
                in which unit to return voltage ratios from the channel.
            bridge_config (Optional[nidaqmx.constants.BridgeConfiguration]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            nominal_bridge_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_calculated_power_chan(self, voltage_physical_channel, current_physical_channel, name_to_assign_to_channel='', terminal_config=TerminalConfiguration.DEFAULT, voltage_min_val=-5.0, voltage_max_val=5.0, current_min_val=-0.01, current_max_val=0.01, units=PowerUnits.WATTS, shunt_resistor_loc=CurrentShuntResistorLocation.LET_DRIVER_CHOOSE, ext_shunt_resistor_val=249.0, custom_scale_name='')`


        Creates channel(s) to measure calculated power.

        Args:
            voltage_physical_channel (str): Specifies the names of the
                voltage physical channels to use to create virtual power
                channels. The DAQmx physical channel constant lists all
                physical channels on devices and modules installed in
                the system.
            current_physical_channel (str): Specifies the names of the
                current physical channels to use to create virtual power
                channels. The DAQmx physical channel constant lists all
                physical channels on devices and modules installed in
                the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            voltage_min_val (Optional[float]): Specifies in **units**
                the minimum value you expect to measure.
            voltage_max_val (Optional[float]): Specifies in **units**
                the maximum value you expect to measure.
            current_min_val (Optional[float]): Specifies in **units**
                the minimum value you expect to measure.
            current_max_val (Optional[float]): Specifies in **units**
                the maximum value you expect to measure.
            units (Optional[nidaqmx.constants.PowerUnits]): Specifies
                the units to use to return calculated power
                measurements.
            shunt_resistor_loc (Optional[nidaqmx.constants.CurrentShuntResistorLocation]): 
                Specifies the location of the shunt resistor. For
                devices with built-in shunt resistors, specify the
                location as **INTERNAL**. For devices that do not have
                built-in shunt resistors, you must attach an external
                one, set this input to **EXTERNAL** and use the
                **ext_shunt_resistor_val** input to specify the value of
                the resistor.
            ext_shunt_resistor_val (Optional[float]): Specifies in ohms
                the resistance of an external shunt resistor.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_charge_chan(self, physical_channel, name_to_assign_to_channel='', terminal_config=TerminalConfiguration.DEFAULT, min_val=-1e-09, max_val=1e-09, units=ChargeUnits.COULOMBS, custom_scale_name='')`


        Creates channel(s) that use a sensor with charge output.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.ChargeUnits]): Specifies
                the units to use to return charge measurements from the
                channel.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_current_chan(self, physical_channel, name_to_assign_to_channel='', terminal_config=TerminalConfiguration.DEFAULT, min_val=-0.01, max_val=0.01, units=CurrentUnits.AMPS, shunt_resistor_loc=CurrentShuntResistorLocation.LET_DRIVER_CHOOSE, ext_shunt_resistor_val=249.0, custom_scale_name='')`


        Creates channel(s) to measure current.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.CurrentUnits]): Specifies
                the units to use to return current measurements.
            shunt_resistor_loc (Optional[nidaqmx.constants.CurrentShuntResistorLocation]): 
                Specifies the location of the shunt resistor. For
                devices with built-in shunt resistors, specify the
                location as **INTERNAL**. For devices that do not have
                built-in shunt resistors, you must attach an external
                one, set this input to **EXTERNAL** and use the
                **ext_shunt_resistor_val** input to specify the value of
                the resistor.
            ext_shunt_resistor_val (Optional[float]): Specifies in ohms
                the resistance of an external shunt resistor.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_current_rms_chan(self, physical_channel, name_to_assign_to_channel='', terminal_config=TerminalConfiguration.DEFAULT, min_val=-0.01, max_val=0.01, units=CurrentUnits.AMPS, shunt_resistor_loc=CurrentShuntResistorLocation.LET_DRIVER_CHOOSE, ext_shunt_resistor_val=249.0, custom_scale_name='')`


        Creates a channel to measure current RMS, the average (mean)
        power of the acquired current.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.CurrentUnits]): Specifies
                the units to use to return current measurements.
            shunt_resistor_loc (Optional[nidaqmx.constants.CurrentShuntResistorLocation]): 
                Specifies the location of the shunt resistor. For
                devices with built-in shunt resistors, specify the
                location as **INTERNAL**. For devices that do not have
                built-in shunt resistors, you must attach an external
                one, set this input to **EXTERNAL** and use the
                **ext_shunt_resistor_val** input to specify the value of
                the resistor.
            ext_shunt_resistor_val (Optional[float]): Specifies in ohms
                the resistance of an external shunt resistor.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_force_bridge_polynomial_chan(self, physical_channel, name_to_assign_to_channel='', min_val=-100.0, max_val=100.0, units=ForceUnits.POUNDS, bridge_config=BridgeConfiguration.FULL_BRIDGE, voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=2.5, nominal_bridge_resistance=350.0, forward_coeffs=None, reverse_coeffs=None, electrical_units=BridgeElectricalUnits.MILLIVOLTS_PER_VOLT, physical_units=BridgePhysicalUnits.POUNDS, custom_scale_name='')`


        Creates channel(s) that use a Wheatstone bridge to measure force
        or load. Use this instance with sensors whose specifications
        provide a polynomial to convert electrical values to physical
        values. When you use this scaling type, NI-DAQmx requires
        coefficients for a polynomial that converts electrical values to
        physical values (forward), as well as coefficients for a
        polynomial that converts physical values to electrical values
        (reverse). If you only know one set of coefficients, use the
        DAQmx Compute Reverse Polynomial Coefficients function to
        generate the other set.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.ForceUnits]): Specifies in
                which unit to return force measurements from the
                channel.
            bridge_config (Optional[nidaqmx.constants.BridgeConfiguration]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            nominal_bridge_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            forward_coeffs (Optional[List[float]]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            reverse_coeffs (Optional[List[float]]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            electrical_units (Optional[nidaqmx.constants.BridgeElectricalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            physical_units (Optional[nidaqmx.constants.BridgePhysicalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_force_bridge_table_chan(self, physical_channel, name_to_assign_to_channel='', min_val=-100.0, max_val=100.0, units=ForceUnits.POUNDS, bridge_config=BridgeConfiguration.FULL_BRIDGE, voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=2.5, nominal_bridge_resistance=350.0, electrical_vals=None, electrical_units=BridgeElectricalUnits.MILLIVOLTS_PER_VOLT, physical_vals=None, physical_units=BridgePhysicalUnits.POUNDS, custom_scale_name='')`


        Creates channel(s) that use a Wheatstone bridge to measure force
        or load. Use this instance with sensors whose specifications
        provide a table of electrical values and the corresponding
        physical values. When you use this scaling type, NI-DAQmx
        performs linear scaling between each pair of electrical and
        physical values. The input limits specified with **min_val** and
        **max_val** must fall within the smallest and largest physical
        values. For any data outside those endpoints, NI-DAQmx coerces
        that data to the endpoints.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.ForceUnits]): Specifies in
                which unit to return force measurements from the
                channel.
            bridge_config (Optional[nidaqmx.constants.BridgeConfiguration]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            nominal_bridge_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            electrical_vals (Optional[List[float]]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            electrical_units (Optional[nidaqmx.constants.BridgeElectricalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            physical_vals (Optional[List[float]]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            physical_units (Optional[nidaqmx.constants.BridgePhysicalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_force_bridge_two_point_lin_chan(self, physical_channel, name_to_assign_to_channel='', min_val=-100.0, max_val=100.0, units=ForceUnits.POUNDS, bridge_config=BridgeConfiguration.FULL_BRIDGE, voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=2.5, nominal_bridge_resistance=350.0, first_electrical_val=0.0, second_electrical_val=2.0, electrical_units=BridgeElectricalUnits.MILLIVOLTS_PER_VOLT, first_physical_val=0.0, second_physical_val=100.0, physical_units=BridgePhysicalUnits.POUNDS, custom_scale_name='')`


        Creates channel(s) that use a Wheatstone bridge to measure force
        or load. Use this instance with sensors whose specifications do
        not provide a polynomial for scaling or a table of electrical
        and physical values. When you use this scaling type, NI-DAQmx
        uses two points of electrical and physical values to calculate
        the slope and y-intercept of a linear equation and uses that
        equation to scale electrical values to physical values.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.ForceUnits]): Specifies in
                which unit to return force measurements from the
                channel.
            bridge_config (Optional[nidaqmx.constants.BridgeConfiguration]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            nominal_bridge_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            first_electrical_val (Optional[float]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            second_electrical_val (Optional[float]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            electrical_units (Optional[nidaqmx.constants.BridgeElectricalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            first_physical_val (Optional[float]): Specifies how to scale
                electrical values from the sensor to physical units.
            second_physical_val (Optional[float]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            physical_units (Optional[nidaqmx.constants.BridgePhysicalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_force_iepe_chan(self, physical_channel, name_to_assign_to_channel='', terminal_config=TerminalConfiguration.DEFAULT, min_val=-2000.0, max_val=2000.0, units=ForceUnits.NEWTONS, sensitivity=2.25, sensitivity_units=ForceIEPESensorSensitivityUnits.MILLIVOLTS_PER_NEWTON, current_excit_source=ExcitationSource.INTERNAL, current_excit_val=0.004, custom_scale_name='')`


        Creates channel(s) that use an IEPE force sensor to measure
        force or load.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.ForceUnits]): Specifies in
                which unit to return force measurements from the
                channel.
            sensitivity (Optional[float]): Is the sensitivity of the
                sensor. This value is in the units you specify with the
                **sensitivity_units** input. Refer to the sensor
                documentation to determine this value.
            sensitivity_units (Optional[nidaqmx.constants.ForceIEPESensorSensitivityUnits]): 
                Specifies the units of the **sensitivity** input.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_freq_voltage_chan(self, physical_channel, name_to_assign_to_channel='', min_val=1, max_val=100, units=FrequencyUnits.HZ, threshold_level=0.0, hysteresis=0.0, custom_scale_name='')`


        Creates channel(s) that use a frequency-to-voltage converter to
        measure frequency.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.FrequencyUnits]): 
                Specifies the units to use to return frequency
                measurements.
            threshold_level (Optional[float]): Specifies in volts the
                level at which to recognize waveform repetitions. You
                should select a voltage level that occurs only once
                within the entire period of a waveform. You also can
                select a voltage that occurs only once while the voltage
                rises or falls.
            hysteresis (Optional[float]): Specifies in volts a window
                below **level**. The input voltage must pass below
                **threshold_level** minus **hysteresis** before NI-DAQmx
                recognizes a waveform repetition. Hysteresis can improve
                measurement accuracy when the signal contains noise or
                jitter.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_microphone_chan(self, physical_channel, name_to_assign_to_channel='', terminal_config=TerminalConfiguration.DEFAULT, units=SoundPressureUnits.PA, mic_sensitivity=10.0, max_snd_press_level=100.0, current_excit_source=ExcitationSource.INTERNAL, current_excit_val=0.004, custom_scale_name='')`


        Creates channel(s) that use a microphone to measure sound
        pressure.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            units (Optional[nidaqmx.constants.SoundPressureUnits]): 
                Specifies the units to use to return sound pressure
                measurements.
            mic_sensitivity (Optional[float]): Is the sensitivity of the
                microphone. Specify this value in mV/Pa.
            max_snd_press_level (Optional[float]): Is the maximum
                instantaneous sound pressure level you expect to
                measure. This value is in decibels, referenced to 20
                micropascals.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_pos_eddy_curr_prox_probe_chan(self, physical_channel, name_to_assign_to_channel='', min_val=0.0, max_val=0.00254, units=LengthUnits.METERS, sensitivity=200.0, sensitivity_units=EddyCurrentProxProbeSensitivityUnits.MILLIVOLTS_PER_MIL, custom_scale_name='')`


        Creates channel(s) that use an eddy current proximity probe to
        measure position.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.LengthUnits]): Specifies
                the units to use to return position measurements from
                the channel.
            sensitivity (Optional[float]): Is the sensitivity of the
                sensor. This value is in the units you specify with the
                **sensitivity_units** input. Refer to the sensor
                documentation to determine this value.
            sensitivity_units (Optional[nidaqmx.constants.EddyCurrentProxProbeSensitivityUnits]): 
                Specifies the units of the **sensitivity** input.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_pos_lvdt_chan(self, physical_channel, name_to_assign_to_channel='', min_val=-0.1, max_val=0.1, units=LengthUnits.METERS, sensitivity=50.0, sensitivity_units=LVDTSensitivityUnits.MILLIVOLTS_PER_VOLT_PER_MILLIMETER, voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=1.0, voltage_excit_freq=2500.0, ac_excit_wire_mode=ACExcitWireMode.FOUR_WIRE, custom_scale_name='')`


        Creates channel(s) that use an LVDT to measure linear position.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.LengthUnits]): Specifies
                the units to use to return linear position measurements
                from the channel.
            sensitivity (Optional[float]): Is the sensitivity of the
                sensor. This value is in the units you specify with the
                **sensitivity_units** input. Refer to the sensor
                documentation to determine this value.
            sensitivity_units (Optional[nidaqmx.constants.LVDTSensitivityUnits]): 
                Specifies the units of the **sensitivity** input.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            voltage_excit_freq (Optional[float]): Specifies in hertz the
                excitation frequency that the sensor requires. Refer to
                the sensor documentation to determine this value.
            ac_excit_wire_mode (Optional[nidaqmx.constants.ACExcitWireMode]): 
                Is the number of leads on the sensor. Some sensors
                require you to tie leads together to create a four- or
                five- wire sensor. Refer to the sensor documentation for
                more information.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_pos_rvdt_chan(self, physical_channel, name_to_assign_to_channel='', min_val=-70.0, max_val=70.0, units=AngleUnits.DEGREES, sensitivity=50.0, sensitivity_units=RVDTSensitivityUnits.MILLIVOLTS_PER_VOLT_PER_DEGREE, voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=1.0, voltage_excit_freq=2500.0, ac_excit_wire_mode=ACExcitWireMode.FOUR_WIRE, custom_scale_name='')`


        Creates channel(s) that use an RVDT to measure angular position.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.AngleUnits]): Specifies
                the units to use to return angular position measurements
                from the channel.
            sensitivity (Optional[float]): Is the sensitivity of the
                sensor. This value is in the units you specify with the
                **sensitivity_units** input. Refer to the sensor
                documentation to determine this value.
            sensitivity_units (Optional[nidaqmx.constants.RVDTSensitivityUnits]): 
                Specifies the units of the **sensitivity** input.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            voltage_excit_freq (Optional[float]): Specifies in hertz the
                excitation frequency that the sensor requires. Refer to
                the sensor documentation to determine this value.
            ac_excit_wire_mode (Optional[nidaqmx.constants.ACExcitWireMode]): 
                Is the number of leads on the sensor. Some sensors
                require you to tie leads together to create a four- or
                five- wire sensor. Refer to the sensor documentation for
                more information.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_power_chan(self, physical_channel, voltage_setpoint, current_setpoint, output_enable, name_to_assign_to_channel='')`


        Creates channel(s) to measure power.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            voltage_setpoint (float): Specifies, in volts, the constant
                output voltage.
            current_setpoint (float): Specifies, in amperes, the output
                current.
            output_enable (bool): Specifies whether to enable or disable
                the output.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_pressure_bridge_polynomial_chan(self, physical_channel, name_to_assign_to_channel='', min_val=-100.0, max_val=100.0, units=PressureUnits.POUNDS_PER_SQ_INCH, bridge_config=BridgeConfiguration.FULL_BRIDGE, voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=2.5, nominal_bridge_resistance=350.0, forward_coeffs=None, reverse_coeffs=None, electrical_units=BridgeElectricalUnits.MILLIVOLTS_PER_VOLT, physical_units=BridgePhysicalUnits.POUNDS_PER_SQ_INCH, custom_scale_name='')`


        Creates channel(s) that use a Wheatstone bridge to measure
        pressure. Use this instance with sensors whose specifications
        provide a polynomial to convert electrical values to physical
        values. When you use this scaling type, NI-DAQmx requires
        coefficients for a polynomial that converts electrical values to
        physical values (forward), as well as coefficients for a
        polynomial that converts physical values to electrical values
        (reverse). If you only know one set of coefficients, use the
        DAQmx Compute Reverse Polynomial Coefficients function to
        generate the other set.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.PressureUnits]): Specifies
                in which unit to return pressure measurements from the
                channel.
            bridge_config (Optional[nidaqmx.constants.BridgeConfiguration]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            nominal_bridge_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            forward_coeffs (Optional[List[float]]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            reverse_coeffs (Optional[List[float]]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            electrical_units (Optional[nidaqmx.constants.BridgeElectricalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            physical_units (Optional[nidaqmx.constants.BridgePhysicalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_pressure_bridge_table_chan(self, physical_channel, name_to_assign_to_channel='', min_val=-100.0, max_val=100.0, units=PressureUnits.POUNDS_PER_SQ_INCH, bridge_config=BridgeConfiguration.FULL_BRIDGE, voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=2.5, nominal_bridge_resistance=350.0, electrical_vals=None, electrical_units=BridgeElectricalUnits.MILLIVOLTS_PER_VOLT, physical_vals=None, physical_units=BridgePhysicalUnits.POUNDS_PER_SQ_INCH, custom_scale_name='')`


        Creates channel(s) that use a Wheatstone bridge to measure
        pressure. Use this instance with sensors whose specifications
        provide a table of electrical values and the corresponding
        physical values. When you use this scaling type, NI-DAQmx
        performs linear scaling between each pair of electrical and
        physical values. The input limits specified with **min_val** and
        **max_val** must fall within the smallest and largest physical
        values. For any data outside those endpoints, NI-DAQmx coerces
        that data to the endpoints.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.PressureUnits]): Specifies
                in which unit to return pressure measurements from the
                channel.
            bridge_config (Optional[nidaqmx.constants.BridgeConfiguration]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            nominal_bridge_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            electrical_vals (Optional[List[float]]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            electrical_units (Optional[nidaqmx.constants.BridgeElectricalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            physical_vals (Optional[List[float]]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            physical_units (Optional[nidaqmx.constants.BridgePhysicalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_pressure_bridge_two_point_lin_chan(self, physical_channel, name_to_assign_to_channel='', min_val=-100.0, max_val=100.0, units=PressureUnits.POUNDS_PER_SQ_INCH, bridge_config=BridgeConfiguration.FULL_BRIDGE, voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=2.5, nominal_bridge_resistance=350.0, first_electrical_val=0.0, second_electrical_val=2.0, electrical_units=BridgeElectricalUnits.MILLIVOLTS_PER_VOLT, first_physical_val=0.0, second_physical_val=100.0, physical_units=BridgePhysicalUnits.POUNDS_PER_SQ_INCH, custom_scale_name='')`


        Creates channel(s) that use a Wheatstone bridge to measure
        pressure. Use this instance with sensors whose specifications do
        not provide a polynomial for scaling or a table of electrical
        and physical values. When you use this scaling type, NI-DAQmx
        uses two points of electrical and physical values to calculate
        the slope and y-intercept of a linear equation and uses that
        equation to scale electrical values to physical values.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.PressureUnits]): Specifies
                in which unit to return pressure measurements from the
                channel.
            bridge_config (Optional[nidaqmx.constants.BridgeConfiguration]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            nominal_bridge_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            first_electrical_val (Optional[float]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            second_electrical_val (Optional[float]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            electrical_units (Optional[nidaqmx.constants.BridgeElectricalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            first_physical_val (Optional[float]): Specifies how to scale
                electrical values from the sensor to physical units.
            second_physical_val (Optional[float]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            physical_units (Optional[nidaqmx.constants.BridgePhysicalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_resistance_chan(self, physical_channel, name_to_assign_to_channel='', min_val=100.0, max_val=1000.0, units=ResistanceUnits.OHMS, resistance_config=ResistanceConfiguration.TWO_WIRE, current_excit_source=ExcitationSource.EXTERNAL, current_excit_val=0.001, custom_scale_name='')`


        Creates channel(s) to measure resistance.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.ResistanceUnits]): 
                Specifies the units to use to return resistance
                measurements.
            resistance_config (Optional[nidaqmx.constants.ResistanceConfiguration]): 
                Specifies the number of wires to use for resistive
                measurements.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_rosette_strain_gage_chan(self, physical_channel, rosette_type, gage_orientation, rosette_meas_types, name_to_assign_to_channel='', min_val=-0.001, max_val=0.001, strain_config=StrainGageBridgeType.QUARTER_BRIDGE_I, voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=2.5, gage_factor=2.0, nominal_gage_resistance=350.0, poisson_ratio=0.3, lead_wire_resistance=0.0)`


        Creates channels to measure two-dimensional strain using a
        rosette strain gage.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create the strain gage virtual
                channels necessary to calculate the **rosette
                measurements** channels.
            rosette_type (nidaqmx.constants.StrainGageRosetteType): 
                Specifies information about the rosette configuration
                and measurements.
            gage_orientation (float): Specifies information about the
                rosette configuration and measurements.
            rosette_meas_types (List[nidaqmx.constants.StrainGageRosetteMeasurementType]): 
                Specifies information about the rosette configuration
                and measurements.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                creates a default channel name.
            min_val (Optional[float]): Specifies the minimum strain you
                expect to measure. This value applies to each strain
                gage in the rosette.
            max_val (Optional[float]): Specifies the maximum strain you
                expect to measure. This value applies to each strain
                gage in the rosette.
            strain_config (Optional[nidaqmx.constants.StrainGageBridgeType]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            gage_factor (Optional[float]): Contains information about
                the strain gage and measurement.
            nominal_gage_resistance (Optional[float]): Contains
                information about the strain gage and measurement.
            poisson_ratio (Optional[float]): Contains information about
                the strain gage and measurement.
            lead_wire_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_rtd_chan(self, physical_channel, name_to_assign_to_channel='', min_val=0.0, max_val=100.0, units=TemperatureUnits.DEG_C, rtd_type=RTDType.PT_3750, resistance_config=ResistanceConfiguration.TWO_WIRE, current_excit_source=ExcitationSource.EXTERNAL, current_excit_val=0.0025, r_0=100.0)`


        Creates channel(s) that use an RTD to measure temperature.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TemperatureUnits]): 
                Specifies the units to use to return temperature
                measurements.
            rtd_type (Optional[nidaqmx.constants.RTDType]): Specifies
                the type of RTD connected to the channel.
            resistance_config (Optional[nidaqmx.constants.ResistanceConfiguration]): 
                Specifies the number of wires to use for resistive
                measurements.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
            r_0 (Optional[float]): Is the sensor resistance in ohms at 0
                degrees Celsius. The Callendar-Van Dusen equation
                requires this value. Refer to the sensor documentation
                to determine this value.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_strain_gage_chan(self, physical_channel, name_to_assign_to_channel='', min_val=-0.001, max_val=0.001, units=StrainUnits.STRAIN, strain_config=StrainGageBridgeType.FULL_BRIDGE_I, voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=2.5, gage_factor=2.0, initial_bridge_voltage=0.0, nominal_gage_resistance=350.0, poisson_ratio=0.3, lead_wire_resistance=0.0, custom_scale_name='')`


        Creates channel(s) to measure strain.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.StrainUnits]): Specifies
                the units to use to return strain measurements.
            strain_config (Optional[nidaqmx.constants.StrainGageBridgeType]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            gage_factor (Optional[float]): Contains information about
                the strain gage and measurement.
            initial_bridge_voltage (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            nominal_gage_resistance (Optional[float]): Contains
                information about the strain gage and measurement.
            poisson_ratio (Optional[float]): Contains information about
                the strain gage and measurement.
            lead_wire_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_temp_built_in_sensor_chan(self, physical_channel, name_to_assign_to_channel='', units=TemperatureUnits.DEG_C)`


        Creates channel(s) that use the built-in sensor of a terminal
        block or device to measure temperature. On SCXI modules, for
        example, the built-in sensor could be the CJC sensor.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            units (Optional[nidaqmx.constants.TemperatureUnits]): 
                Specifies the units to use to return temperature
                measurements.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_thrmcpl_chan(self, physical_channel, name_to_assign_to_channel='', min_val=0.0, max_val=100.0, units=TemperatureUnits.DEG_C, thermocouple_type=ThermocoupleType.J, cjc_source=CJCSource.CONSTANT_USER_VALUE, cjc_val=25.0, cjc_channel='')`


        Creates channel(s) that use a thermocouple to measure
        temperature.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TemperatureUnits]): 
                Specifies the units to use to return temperature
                measurements.
            thermocouple_type (Optional[nidaqmx.constants.ThermocoupleType]): 
                Specifies the type of thermocouple connected to the
                channel. Thermocouple types differ in composition and
                measurement range.
            cjc_source (Optional[nidaqmx.constants.CJCSource]): 
                Specifies the source of cold-junction compensation.
            cjc_val (Optional[float]): Specifies in **units** the
                temperature of the cold junction if you set
                **cjc_source** to **CONSTANT_VALUE**.
            cjc_channel (Optional[str]): Specifies the channel that
                acquires the temperature of the thermocouple cold-
                junction if you set **cjc_source** to **CHANNEL**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_thrmstr_chan_iex(self, physical_channel, name_to_assign_to_channel='', min_val=0.0, max_val=100.0, units=TemperatureUnits.DEG_C, resistance_config=ResistanceConfiguration.FOUR_WIRE, current_excit_source=ExcitationSource.EXTERNAL, current_excit_val=0.00015, a=0.001295361, b=0.0002343159, c=1.018703e-07)`


        Creates channel(s) that use a thermistor to measure temperature.
        Use this instance when the thermistor requires current
        excitation.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TemperatureUnits]): 
                Specifies the units to use to return temperature
                measurements.
            resistance_config (Optional[nidaqmx.constants.ResistanceConfiguration]): 
                Specifies the number of wires to use for resistive
                measurements.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
            a (Optional[float]): Contains the constants for the
                Steinhart-Hart thermistor equation. Refer to the sensor
                documentation to determine values for these constants.
            b (Optional[float]): Contains the constants for the
                Steinhart-Hart thermistor equation. Refer to the sensor
                documentation to determine values for these constants.
            c (Optional[float]): Contains the constants for the
                Steinhart-Hart thermistor equation. Refer to the sensor
                documentation to determine values for these constants.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_thrmstr_chan_vex(self, physical_channel, name_to_assign_to_channel='', min_val=0.0, max_val=100.0, units=TemperatureUnits.DEG_C, resistance_config=ResistanceConfiguration.FOUR_WIRE, voltage_excit_source=ExcitationSource.EXTERNAL, voltage_excit_val=2.5, a=0.001295361, b=0.0002343159, c=1.018703e-07, r_1=5000.0)`


        Creates channel(s) that use a thermistor to measure temperature.
        Use this instance when the thermistor requires voltage
        excitation.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TemperatureUnits]): 
                Specifies the units to use to return temperature
                measurements.
            resistance_config (Optional[nidaqmx.constants.ResistanceConfiguration]): 
                Specifies the number of wires to use for resistive
                measurements.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            a (Optional[float]): Contains the constants for the
                Steinhart-Hart thermistor equation. Refer to the sensor
                documentation to determine values for these constants.
            b (Optional[float]): Contains the constants for the
                Steinhart-Hart thermistor equation. Refer to the sensor
                documentation to determine values for these constants.
            c (Optional[float]): Contains the constants for the
                Steinhart-Hart thermistor equation. Refer to the sensor
                documentation to determine values for these constants.
            r_1 (Optional[float]): Specifies in ohms the value of the
                reference resistor.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_torque_bridge_polynomial_chan(self, physical_channel, name_to_assign_to_channel='', min_val=-100.0, max_val=100.0, units=TorqueUnits.INCH_POUNDS, bridge_config=BridgeConfiguration.FULL_BRIDGE, voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=2.5, nominal_bridge_resistance=350.0, forward_coeffs=None, reverse_coeffs=None, electrical_units=BridgeElectricalUnits.MILLIVOLTS_PER_VOLT, physical_units=BridgePhysicalUnits.INCH_POUNDS, custom_scale_name='')`


        Creates channel(s) that use a Wheatstone bridge to measure
        torque. Use this instance with sensors whose specifications
        provide a polynomial to convert electrical values to physical
        values. When you use this scaling type, NI-DAQmx requires
        coefficients for a polynomial that converts electrical values to
        physical values (forward), as well as coefficients for a
        polynomial that converts physical values to electrical values
        (reverse). If you only know one set of coefficients, use the
        DAQmx Compute Reverse Polynomial Coefficients function to
        generate the other set.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TorqueUnits]): Specifies
                in which unit to return torque measurements from the
                channel.
            bridge_config (Optional[nidaqmx.constants.BridgeConfiguration]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            nominal_bridge_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            forward_coeffs (Optional[List[float]]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            reverse_coeffs (Optional[List[float]]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            electrical_units (Optional[nidaqmx.constants.BridgeElectricalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            physical_units (Optional[nidaqmx.constants.BridgePhysicalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_torque_bridge_table_chan(self, physical_channel, name_to_assign_to_channel='', min_val=-100.0, max_val=100.0, units=TorqueUnits.INCH_POUNDS, bridge_config=BridgeConfiguration.FULL_BRIDGE, voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=2.5, nominal_bridge_resistance=350.0, electrical_vals=None, electrical_units=BridgeElectricalUnits.MILLIVOLTS_PER_VOLT, physical_vals=None, physical_units=BridgePhysicalUnits.INCH_POUNDS, custom_scale_name='')`


        Creates channel(s) that use a Wheatstone bridge to measure
        torque. Use this instance with sensors whose specifications
        provide a table of electrical values and the corresponding
        physical values. When you use this scaling type, NI-DAQmx
        performs linear scaling between each pair of electrical and
        physical values. The input limits specified with **min_val** and
        **max_val** must fall within the smallest and largest physical
        values. For any data outside those endpoints, NI-DAQmx coerces
        that data to the endpoints.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TorqueUnits]): Specifies
                in which unit to return torque measurements from the
                channel.
            bridge_config (Optional[nidaqmx.constants.BridgeConfiguration]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            nominal_bridge_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            electrical_vals (Optional[List[float]]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            electrical_units (Optional[nidaqmx.constants.BridgeElectricalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            physical_vals (Optional[List[float]]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            physical_units (Optional[nidaqmx.constants.BridgePhysicalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_torque_bridge_two_point_lin_chan(self, physical_channel, name_to_assign_to_channel='', min_val=-100.0, max_val=100.0, units=TorqueUnits.INCH_POUNDS, bridge_config=BridgeConfiguration.FULL_BRIDGE, voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=2.5, nominal_bridge_resistance=350.0, first_electrical_val=0.0, second_electrical_val=2.0, electrical_units=BridgeElectricalUnits.MILLIVOLTS_PER_VOLT, first_physical_val=0.0, second_physical_val=100.0, physical_units=BridgePhysicalUnits.INCH_POUNDS, custom_scale_name='')`


        Creates channel(s) that use a Wheatstone bridge to measure
        torque. Use this instance with sensors whose specifications do
        not provide a polynomial for scaling or a table of electrical
        and physical values. When you use this scaling type, NI-DAQmx
        uses two points of electrical and physical values to calculate
        the slope and y-intercept of a linear equation and uses that
        equation to scale electrical values to physical values.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TorqueUnits]): Specifies
                in which unit to return torque measurements from the
                channel.
            bridge_config (Optional[nidaqmx.constants.BridgeConfiguration]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            nominal_bridge_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            first_electrical_val (Optional[float]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            second_electrical_val (Optional[float]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            electrical_units (Optional[nidaqmx.constants.BridgeElectricalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            first_physical_val (Optional[float]): Specifies how to scale
                electrical values from the sensor to physical units.
            second_physical_val (Optional[float]): Specifies how to
                scale electrical values from the sensor to physical
                units.
            physical_units (Optional[nidaqmx.constants.BridgePhysicalUnits]): 
                Specifies how to scale electrical values from the sensor
                to physical units.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_velocity_iepe_chan(self, physical_channel, name_to_assign_to_channel='', terminal_config=TerminalConfiguration.DEFAULT, min_val=-50.0, max_val=50.0, units=VelocityUnits.INCHES_PER_SECOND, sensitivity=100.0, sensitivity_units=VelocityIEPESensorSensitivityUnits.MILLIVOLTS_PER_INCH_PER_SECOND, current_excit_source=ExcitationSource.INTERNAL, current_excit_val=0.002, custom_scale_name='')`


        Creates channel(s) that use an IEPE velocity sensor to measure
        velocity.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.VelocityUnits]): Specifies
                in which unit to return velocity measurements from the
                channel.
            sensitivity (Optional[float]): Is the sensitivity of the
                sensor. This value is in the units you specify with the
                **sensitivity_units** input. Refer to the sensor
                documentation to determine this value.
            sensitivity_units (Optional[nidaqmx.constants.VelocityIEPESensorSensitivityUnits]): 
                Specifies the units of the **sensitivity** input.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_voltage_chan(self, physical_channel, name_to_assign_to_channel='', terminal_config=TerminalConfiguration.DEFAULT, min_val=-5.0, max_val=5.0, units=VoltageUnits.VOLTS, custom_scale_name='')`


        Creates channel(s) to measure voltage. If the measurement
        requires the use of internal excitation or you need excitation
        to scale the voltage, use the AI Custom Voltage with Excitation
        instance of this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.VoltageUnits]): Specifies
                the units to use to return voltage measurements.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_voltage_chan_with_excit(self, physical_channel, name_to_assign_to_channel='', terminal_config=TerminalConfiguration.DEFAULT, min_val=-10.0, max_val=10.0, units=VoltageUnits.VOLTS, bridge_config=BridgeConfiguration.NO_BRIDGE, voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=0.0, use_excit_for_scaling=False, custom_scale_name='')`


        Creates channel(s) to measure voltage. Use this instance for
        custom sensors that require excitation. You can use the
        excitation to scale the measurement.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.VoltageUnits]): Specifies
                the units to use to return voltage measurements.
            bridge_config (Optional[nidaqmx.constants.BridgeConfiguration]): 
                Specifies what type of Wheatstone bridge the sensor is.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            use_excit_for_scaling (Optional[bool]): Specifies if NI-
                DAQmx divides the measurement by the excitation. You
                should typically set **use_excit_for_scaling** to True
                for ratiometric transducers. If you set
                **use_excit_for_scaling** to True, set **max_val** and
                **min_val** to reflect the scaling.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_ai_voltage_rms_chan(self, physical_channel, name_to_assign_to_channel='', terminal_config=TerminalConfiguration.DEFAULT, min_val=-5.0, max_val=5.0, units=VoltageUnits.VOLTS, custom_scale_name='')`


        Creates channel(s) to measure voltage RMS, the average (mean)
        power of the acquired voltage.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.VoltageUnits]): Specifies
                the units to use to return voltage measurements.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_teds_ai_accel_chan(self, physical_channel, name_to_assign_to_channel='', terminal_config=TerminalConfiguration.DEFAULT, min_val=-5.0, max_val=5.0, units=AccelUnits.G, current_excit_source=ExcitationSource.INTERNAL, current_excit_val=0.004, custom_scale_name='')`


        Creates channel(s) that use an accelerometer to measure
        acceleration. You must configure the physical channel(s) with
        TEDS information to use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.AccelUnits]): Specifies
                the units to use to return acceleration measurements
                from the channel.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_teds_ai_bridge_chan(self, physical_channel, name_to_assign_to_channel='', min_val=-0.002, max_val=0.002, units=TEDSUnits.FROM_TEDS, voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=2.5, custom_scale_name='')`


        Creates channel(s) that measure a Wheatstone bridge. You must
        configure the physical channel(s) with TEDS information to use
        this function. Use this instance with bridge-based sensors that
        measure phenomena other than strain, force, pressure, or torque,
        or that scale data to physical units NI-DAQmx does not support.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TEDSUnits]): Specifies in
                which unit to return measurements from the channel.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_teds_ai_current_chan(self, physical_channel, name_to_assign_to_channel='', terminal_config=TerminalConfiguration.DEFAULT, min_val=-0.01, max_val=0.01, units=TEDSUnits.FROM_TEDS, shunt_resistor_loc=CurrentShuntResistorLocation.LET_DRIVER_CHOOSE, ext_shunt_resistor_val=249.0, custom_scale_name='')`


        Creates channel(s) to measure current. You must configure the
        physical channel(s) with TEDS information to use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TEDSUnits]): Specifies the
                units to use to return measurements.
            shunt_resistor_loc (Optional[nidaqmx.constants.CurrentShuntResistorLocation]): 
                Specifies the location of the shunt resistor. For
                devices with built-in shunt resistors, specify the
                location as **INTERNAL**. For devices that do not have
                built-in shunt resistors, you must attach an external
                one, set this input to **EXTERNAL** and use the
                **ext_shunt_resistor_val** input to specify the value of
                the resistor.
            ext_shunt_resistor_val (Optional[float]): Specifies in ohms
                the resistance of an external shunt resistor.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_teds_ai_force_bridge_chan(self, physical_channel, name_to_assign_to_channel='', min_val=-100.0, max_val=100.0, units=ForceUnits.POUNDS, voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=2.5, custom_scale_name='')`


        Creates channel(s) that use a Wheatstone bridge to measure force
        or load. You must configure the physical channel(s) with TEDS
        information to use this function. NI-DAQmx scales electrical
        values to physical values according to that TEDS information.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.ForceUnits]): Specifies in
                which unit to return force measurements from the
                channel.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_teds_ai_force_iepe_chan(self, physical_channel, name_to_assign_to_channel='', terminal_config=TerminalConfiguration.DEFAULT, min_val=-2000.0, max_val=2000.0, units=ForceUnits.NEWTONS, current_excit_source=ExcitationSource.INTERNAL, current_excit_val=0.001, custom_scale_name='')`


        Creates channel(s) that use an IEPE force sensor to measure
        force or load. You must configure the physical channel(s) with
        TEDS information to use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.ForceUnits]): Specifies in
                which unit to return force measurements from the
                channel.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_teds_ai_microphone_chan(self, physical_channel, name_to_assign_to_channel='', terminal_config=TerminalConfiguration.DEFAULT, units=SoundPressureUnits.PA, max_snd_press_level=100.0, current_excit_source=ExcitationSource.INTERNAL, current_excit_val=0.004, custom_scale_name='')`


        Creates channel(s) that use a microphone to measure sound
        pressure. You must configure the physical channel(s) with TEDS
        information to use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. You must use
                physical channels that you configured with TEDS
                information. The DAQmx physical channel constant lists
                all physical channels on devices and modules installed
                in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            units (Optional[nidaqmx.constants.SoundPressureUnits]): 
                Specifies the units to use to return sound pressure
                measurements.
            max_snd_press_level (Optional[float]): Is the maximum
                instantaneous sound pressure level you expect to
                measure. This value is in decibels, referenced to 20
                micropascals.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_teds_ai_pos_lvdt_chan(self, physical_channel, name_to_assign_to_channel='', min_val=-0.1, max_val=0.1, units=LengthUnits.METERS, voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=1.0, voltage_excit_freq=2500.0, ac_excit_wire_mode=ACExcitWireMode.FOUR_WIRE, custom_scale_name='')`


        Creates channel(s) that use an LVDT to measure linear position.
        You must configure the physical channel(s) with TEDS information
        to use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.LengthUnits]): Specifies
                the units to use to return linear position measurements
                from the channel.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            voltage_excit_freq (Optional[float]): Specifies in hertz the
                excitation frequency that the sensor requires. Refer to
                the sensor documentation to determine this value.
            ac_excit_wire_mode (Optional[nidaqmx.constants.ACExcitWireMode]): 
                Is the number of leads on the sensor. Some sensors
                require you to tie leads together to create a four- or
                five- wire sensor. Refer to the sensor documentation for
                more information.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_teds_ai_pos_rvdt_chan(self, physical_channel, name_to_assign_to_channel='', min_val=-70.0, max_val=70.0, units=AngleUnits.DEGREES, voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=1.0, voltage_excit_freq=2500.0, ac_excit_wire_mode=ACExcitWireMode.FOUR_WIRE, custom_scale_name='')`


        Creates channel(s) that use an RVDT to measure angular position.
        You must configure the physical channel(s) with TEDS information
        to use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.AngleUnits]): Specifies
                the units to use to return angular position measurements
                from the channel.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            voltage_excit_freq (Optional[float]): Specifies in hertz the
                excitation frequency that the sensor requires. Refer to
                the sensor documentation to determine this value.
            ac_excit_wire_mode (Optional[nidaqmx.constants.ACExcitWireMode]): 
                Is the number of leads on the sensor. Some sensors
                require you to tie leads together to create a four- or
                five- wire sensor. Refer to the sensor documentation for
                more information.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_teds_ai_pressure_bridge_chan(self, physical_channel, name_to_assign_to_channel='', min_val=-100.0, max_val=100.0, units=PressureUnits.POUNDS_PER_SQ_INCH, voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=2.5, custom_scale_name='')`


        Creates channel(s) that use a Wheatstone bridge to measure
        pressure. You must configure the physical channel(s) with TEDS
        information to use this function. NI-DAQmx scales electrical
        values to physical values according to that TEDS information.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.PressureUnits]): Specifies
                in which unit to return pressure measurements from the
                channel.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_teds_ai_resistance_chan(self, physical_channel, name_to_assign_to_channel='', min_val=100.0, max_val=1000.0, units=TEDSUnits.FROM_TEDS, resistance_config=ResistanceConfiguration.TWO_WIRE, current_excit_source=ExcitationSource.EXTERNAL, current_excit_val=0.001, custom_scale_name='')`


        Creates channel(s) to measure resistance. You must configure the
        physical channel(s) with TEDS information to use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TEDSUnits]): Specifies the
                units to use to return measurements.
            resistance_config (Optional[nidaqmx.constants.ResistanceConfiguration]): 
                Specifies the number of wires to use for resistive
                measurements.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_teds_ai_rtd_chan(self, physical_channel, name_to_assign_to_channel='', min_val=0.0, max_val=100.0, units=TemperatureUnits.DEG_C, resistance_config=ResistanceConfiguration.TWO_WIRE, current_excit_source=ExcitationSource.EXTERNAL, current_excit_val=0.0025)`


        Creates channel(s) that use an RTD to measure temperature. You
        must configure the physical channel(s) with TEDS information to
        use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TemperatureUnits]): 
                Specifies the units to use to return temperature
                measurements.
            resistance_config (Optional[nidaqmx.constants.ResistanceConfiguration]): 
                Specifies the number of wires to use for resistive
                measurements.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_teds_ai_strain_gage_chan(self, physical_channel, name_to_assign_to_channel='', min_val=-0.001, max_val=0.001, units=StrainUnits.STRAIN, voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=2.5, initial_bridge_voltage=0.0, lead_wire_resistance=0.0, custom_scale_name='')`


        Creates channel(s) to measure strain. You must configure the
        physical channel(s) with TEDS information to use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.StrainUnits]): Specifies
                the units to use to return strain measurements.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies information about the bridge configuration and
                measurement.
            voltage_excit_val (Optional[float]): Specifies information
                about the bridge configuration and measurement.
            initial_bridge_voltage (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            lead_wire_resistance (Optional[float]): Specifies
                information about the bridge configuration and
                measurement.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_teds_ai_thrmcpl_chan(self, physical_channel, name_to_assign_to_channel='', min_val=0.0, max_val=100.0, units=TemperatureUnits.DEG_C, cjc_source=CJCSource.CONSTANT_USER_VALUE, cjc_val=25.0, cjc_channel='')`


        Creates channel(s) that use a thermocouple to measure
        temperature. You must configure the physical channel(s) with
        TEDS information to use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TemperatureUnits]): 
                Specifies the units to use to return temperature
                measurements.
            cjc_source (Optional[nidaqmx.constants.CJCSource]): 
                Specifies the source of cold-junction compensation.
            cjc_val (Optional[float]): Specifies in **units** the
                temperature of the cold junction if you set
                **cjc_source** to **CONSTANT_VALUE**.
            cjc_channel (Optional[str]): Specifies the channel that
                acquires the temperature of the thermocouple cold-
                junction if you set **cjc_source** to **CHANNEL**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_teds_ai_thrmstr_chan_iex(self, physical_channel, name_to_assign_to_channel='', min_val=0.0, max_val=100.0, units=TemperatureUnits.DEG_C, resistance_config=ResistanceConfiguration.FOUR_WIRE, current_excit_source=ExcitationSource.EXTERNAL, current_excit_val=0.00015)`


        Creates channel(s) that use a thermistor to measure temperature.
        Use this instance when the thermistor requires current
        excitation. You must configure the physical channel(s) with TEDS
        information to use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TemperatureUnits]): 
                Specifies the units to use to return temperature
                measurements.
            resistance_config (Optional[nidaqmx.constants.ResistanceConfiguration]): 
                Specifies the number of wires to use for resistive
                measurements.
            current_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            current_excit_val (Optional[float]): Specifies in amperes
                the amount of excitation to supply to the sensor. Refer
                to the sensor documentation to determine this value.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_teds_ai_thrmstr_chan_vex(self, physical_channel, name_to_assign_to_channel='', min_val=0.0, max_val=100.0, units=TemperatureUnits.DEG_C, resistance_config=ResistanceConfiguration.FOUR_WIRE, voltage_excit_source=ExcitationSource.EXTERNAL, voltage_excit_val=2.5, r_1=5000.0)`


        Creates channel(s) that use a thermistor to measure temperature.
        Use this instance when the thermistor requires voltage
        excitation. You must configure the physical channel(s) with TEDS
        information to use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TemperatureUnits]): 
                Specifies the units to use to return temperature
                measurements.
            resistance_config (Optional[nidaqmx.constants.ResistanceConfiguration]): 
                Specifies the number of wires to use for resistive
                measurements.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            r_1 (Optional[float]): Specifies in ohms the value of the
                reference resistor.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_teds_ai_torque_bridge_chan(self, physical_channel, name_to_assign_to_channel='', min_val=-100.0, max_val=100.0, units=TorqueUnits.INCH_POUNDS, voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=2.5, custom_scale_name='')`


        Creates channel(s) that use a Wheatstone bridge to measure
        torque. You must configure the physical channel(s) with TEDS
        information to use this function. NI-DAQmx scales electrical
        values to physical values according to that TEDS information.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TorqueUnits]): Specifies
                in which unit to return torque measurements from the
                channel.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_teds_ai_voltage_chan(self, physical_channel, name_to_assign_to_channel='', terminal_config=TerminalConfiguration.DEFAULT, min_val=-5.0, max_val=5.0, units=TEDSUnits.FROM_TEDS, custom_scale_name='')`


        Creates channel(s) to measure voltage. You must configure the
        physical channel(s) with TEDS information to use this function.
        If the measurement requires the use of internal excitation or
        you need excitation to scale the voltage, use the TEDS AI Custom
        Voltage with Excitation instance of this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TEDSUnits]): Specifies the
                units to use to return measurements.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

#### `def add_teds_ai_voltage_chan_with_excit(self, physical_channel, name_to_assign_to_channel='', terminal_config=TerminalConfiguration.DEFAULT, min_val=-10.0, max_val=10.0, units=TEDSUnits.FROM_TEDS, voltage_excit_source=ExcitationSource.INTERNAL, voltage_excit_val=0.0, custom_scale_name='')`


        Creates channel(s) to measure voltage. Use this instance for
        custom sensors that require excitation. You can use the
        excitation to scale the measurement. You must configure the
        physical channel(s) with TEDS information to use this function.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            terminal_config (Optional[nidaqmx.constants.TerminalConfiguration]): 
                Specifies the input terminal configuration for the
                channel.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TEDSUnits]): Specifies the
                units to use to return measurements.
            voltage_excit_source (Optional[nidaqmx.constants.ExcitationSource]): 
                Specifies the source of excitation.
            voltage_excit_val (Optional[float]): Specifies in volts the
                amount of excitation supplied to the sensor. Refer to
                the sensor documentation to determine appropriate
                excitation values.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Indicates the newly created channel object.
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/collections/_ao_channel_collection.py -->
## PYTHON MODULE: generated/nidaqmx/task/collections/_ao_channel_collection.py

### `class AOChannelCollection(ChannelCollection)`


    Contains the collection of analog output channels for a DAQmx Task.
    

#### `def __init__(self, task_handle, interpreter)`


        Do not construct this object directly; instead, construct a nidaqmx.Task and use the task.ao_channels property.
        

#### `def _create_chan(self, physical_channel, name_to_assign_to_channel='')`


        Creates and returns an AOChannel object.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels.
            name_to_assign_to_channel (Optional[str]): Specifies a name to
                assign to the virtual channel this method creates.
        Returns:
            nidaqmx.task.channels.AOChannel: 
            
            Specifies the newly created AOChannel object.
        

#### `def add_ao_current_chan(self, physical_channel, name_to_assign_to_channel='', min_val=0.0, max_val=0.02, units=CurrentUnits.AMPS, custom_scale_name='')`


        Creates channel(s) to generate current.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.CurrentUnits]): Specifies
                the units to use to generate current.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AOChannel:

            Indicates the newly created channel object.
        

#### `def add_ao_func_gen_chan(self, physical_channel, name_to_assign_to_channel='', type=FuncGenType.SINE, freq=1000.0, amplitude=5.0, offset=0.0)`


        Creates a channel for continually generating a waveform on the
        selected physical channel.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            type (Optional[nidaqmx.constants.FuncGenType]): Specifies
                the kind of waveform to generate.
            freq (Optional[float]): Is the frequency of the waveform to
                generate in hertz.
            amplitude (Optional[float]): Is the zero-to-peak amplitude
                of the waveform to generate in volts. Zero and negative
                values are valid.
            offset (Optional[float]): Is the voltage offset of the
                waveform to generate.
        Returns:
            nidaqmx.task.channels.AOChannel:

            Indicates the newly created channel object.
        

#### `def add_ao_voltage_chan(self, physical_channel, name_to_assign_to_channel='', min_val=-10.0, max_val=10.0, units=VoltageUnits.VOLTS, custom_scale_name='')`


        Creates channel(s) to generate voltage.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels. The DAQmx
                physical channel constant lists all physical channels on
                devices and modules installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to generate.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to generate.
            units (Optional[nidaqmx.constants.VoltageUnits]): Specifies
                the units to use to generate voltage.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.AOChannel:

            Indicates the newly created channel object.
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/collections/_channel_collection.py -->
## PYTHON MODULE: generated/nidaqmx/task/collections/_channel_collection.py

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

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/collections/_ci_channel_collection.py -->
## PYTHON MODULE: generated/nidaqmx/task/collections/_ci_channel_collection.py

### `class CIChannelCollection(ChannelCollection)`


    Contains the collection of counter input channels for a DAQmx Task.
    

#### `def __init__(self, task_handle, interpreter)`


        Do not construct this object directly; instead, construct a nidaqmx.Task and use the task.ci_channels property.
        

#### `def _create_chan(self, counter, name_to_assign_to_channel='')`


        Creates and returns a CIChannel object.

        Args:
            counter (str): Specifies the names of the counters to use to 
                create virtual channels.
            name_to_assign_to_channel (Optional[str]): Specifies a name to 
                assign to the virtual channel this method creates.
        Returns:
            nidaqmx.task.channels.CIChannel: 
            
            Specifies the newly created CIChannel object.
        

#### `def add_ci_ang_encoder_chan(self, counter, name_to_assign_to_channel='', decoding_type=EncoderType.X_4, zidx_enable=False, zidx_val=0, zidx_phase=EncoderZIndexPhase.AHIGH_BHIGH, units=AngleUnits.DEGREES, pulses_per_rev=24, initial_angle=0.0, custom_scale_name='')`


        Creates a channel that uses an angular encoder to measure
        angular position. With the exception of devices that support
        multi-counter tasks, you can create only one counter input
        channel at a time with this function because a task can contain
        only one counter input channel. To read from multiple counters
        simultaneously, use a separate task for each counter. Connect
        the input signals to the default input terminals of the counter
        unless you select different input terminals.

        Args:
            counter (str): Specifies the name of the counter to use to
                create the virtual channel. The DAQmx physical channel
                constant lists all physical channels, including
                counters, for devices installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            decoding_type (Optional[nidaqmx.constants.EncoderType]): 
                Specifies how to count and interpret the pulses the
                encoder generates on signal A and signal B. **X_1**,
                **X_2**, and **X_4** are valid for quadrature encoders
                only. **TWO_PULSE_COUNTING** is valid only for two-pulse
                encoders.
            zidx_enable (Optional[bool]): Specifies whether to use Z
                indexing for the channel.
            zidx_val (Optional[float]): Specifies in **units** the value
                to which to reset the measurement when signal Z is high
                and signal A and signal B are at the states you specify
                with **zidx_phase**.
            zidx_phase (Optional[nidaqmx.constants.EncoderZIndexPhase]): 
                Specifies the states at which signal A and signal B must
                be while signal Z is high for NI-DAQmx to reset the
                measurement. If signal Z is never high while signal A
                and signal B are high, for example, you must choose a
                phase other than **A_HIGH_B_HIGH**.
            units (Optional[nidaqmx.constants.AngleUnits]): Specifies
                the units to use to return angular position measurements
                from the channel.
            pulses_per_rev (Optional[int]): Is the number of pulses the
                encoder generates per revolution. This value is the
                number of pulses on either signal A or signal B, not the
                total number of pulses on both signal A and signal B.
            initial_angle (Optional[float]): Is the starting angle of
                the encoder. This value is in the units you specify with
                the **units** input.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.CIChannel:

            Indicates the newly created channel object.
        

#### `def add_ci_ang_velocity_chan(self, counter, name_to_assign_to_channel='', min_val=0.0, max_val=1.0, decoding_type=EncoderType.X_4, units=AngularVelocityUnits.RPM, pulses_per_rev=24, custom_scale_name='')`


        Creates a channel to measure the angular velocity of a digital
        signal. With the exception of devices that support multi-counter
        tasks, you can create only one counter input channel at a time
        with this function because a task can contain only one counter
        input channel. To read from multiple counters simultaneously,
        use a separate task for each counter. Connect the input signal
        to the default input terminal of the counter unless you select a
        different input terminal.

        Args:
            counter (str): Specifies the name of the counter to use to
                create the virtual channel. The DAQmx physical channel
                constant lists all physical channels, including
                counters, for devices installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            decoding_type (Optional[nidaqmx.constants.EncoderType]): 
                Specifies how to count and interpret the pulses the
                encoder generates on signal A and signal B. **X_1**,
                **X_2**, and **X_4** are valid for quadrature encoders
                only. **TWO_PULSE_COUNTING** is valid only for two-pulse
                encoders.
            units (Optional[nidaqmx.constants.AngularVelocityUnits]): 
                Specifies in which unit to return velocity measurements
                from the channel.
            pulses_per_rev (Optional[int]): Is the number of pulses the
                encoder generates per revolution. This value is the
                number of pulses on either signal A or signal B, not the
                total number of pulses on both signal A and signal B.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.CIChannel:

            Indicates the newly created channel object.
        

#### `def add_ci_count_edges_chan(self, counter, name_to_assign_to_channel='', edge=Edge.RISING, initial_count=0, count_direction=CountDirection.COUNT_UP)`


        Creates a channel to count the number of rising or falling edges
        of a digital signal. With the exception of devices that support
        multi-counter tasks, you can create only one counter input
        channel at a time with this function because a task can contain
        only one counter input channel. To read from multiple counters
        simultaneously, use a separate task for each counter. Connect
        the input signal to the default input terminal of the counter
        unless you select a different input terminal.

        Args:
            counter (str): Specifies the name of the counter to use to
                create the virtual channel. The DAQmx physical channel
                constant lists all physical channels, including
                counters, for devices installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            edge (Optional[nidaqmx.constants.Edge]): Specifies on which
                edges of the input signal to increment or decrement the
                count.
            initial_count (Optional[int]): Is the value from which to
                start counting.
            count_direction (Optional[nidaqmx.constants.CountDirection]): 
                Specifies whether to increment or decrement the counter
                on each edge.
        Returns:
            nidaqmx.task.channels.CIChannel:

            Indicates the newly created channel object.
        

#### `def add_ci_duty_cycle_chan(self, counter, name_to_assign_to_channel='', min_freq=2.0, max_freq=10000.0, edge=Edge.RISING, custom_scale_name='')`


        Creates channel(s) to duty cycle of a digital pulse. Connect the
        input signal to the default input terminal of the counter unless
        you select a different input terminal. With the exception of
        devices that support multi-counter tasks, you can create only
        one counter input channel at a time with this function because a
        task can contain only one counter input channel. To read from
        multiple counters simultaneously, use a separate task for each
        counter.

        Args:
            counter (str): Specifies the name of the counter to use to
                create the virtual channel. The DAQmx physical channel
                constant lists all physical channels, including
                counters, for devices installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_freq (Optional[float]): Specifies the minimum frequency
                you expect to measure.
            max_freq (Optional[float]): Specifies the maximum frequency
                you expect to measure.
            edge (Optional[nidaqmx.constants.Edge]): Specifies between
                which edges to measure the frequency or period of the
                signal.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.CIChannel:

            Indicates the newly created channel object.
        

#### `def add_ci_freq_chan(self, counter, name_to_assign_to_channel='', min_val=2.0, max_val=100.0, units=FrequencyUnits.HZ, edge=Edge.RISING, meas_method=CounterFrequencyMethod.LOW_FREQUENCY_1_COUNTER, meas_time=0.001, divisor=4, custom_scale_name='')`


        Creates a channel to measure the frequency of a digital signal.
        With the exception of devices that support multi-counter tasks,
        you can create only one counter input channel at a time with
        this function because a task can contain only one counter input
        channel. To read from multiple counters simultaneously, use a
        separate task for each counter. Connect the input signal to the
        default input terminal of the counter unless you select a
        different input terminal.

        Args:
            counter (str): Specifies the name of the counter to use to
                create the virtual channel. The DAQmx physical channel
                constant lists all physical channels, including
                counters, for devices installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.FrequencyUnits]): 
                Specifies the units to use to return frequency
                measurements.
            edge (Optional[nidaqmx.constants.Edge]): Specifies between
                which edges to measure the frequency or period of the
                signal.
            meas_method (Optional[nidaqmx.constants.CounterFrequencyMethod]): 
                Specifies the method to use to calculate the period or
                frequency of the signal.
            meas_time (Optional[float]): Is the length of time in
                seconds to measure the frequency or period of the signal
                if **meas_method** is **HIGH_FREQUENCYWITH_2_COUNTERS**.
                Leave this input unspecified if **meas_method** is not
                **HIGH_FREQUENCYWITH_2_COUNTERS**.
            divisor (Optional[int]): Is the value by which to divide the
                input signal when **meas_method** is
                **LARGE_RANGEWITH_2_COUNTERS**. Leave this input
                unspecified if **meas_method** is not
                **LARGE_RANGEWITH_2_COUNTERS**.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.CIChannel:

            Indicates the newly created channel object.
        

#### `def add_ci_gps_timestamp_chan(self, counter, name_to_assign_to_channel='', units=TimeUnits.SECONDS, sync_method=GpsSignalType.IRIGB, custom_scale_name='')`


        Creates a channel that uses a special purpose counter to take a
        timestamp and synchronizes that counter to a GPS receiver. With
        the exception of devices that support multi-counter tasks, you
        can create only one counter input channel at a time with this
        function because a task can contain only one counter input
        channel. To read from multiple counters simultaneously, use a
        separate task for each counter. Connect the input signals to the
        default input terminals of the counter unless you select
        different input terminals.

        Args:
            counter (str): Specifies the name of the counter to use to
                create the virtual channel. The DAQmx physical channel
                constant lists all physical channels, including
                counters, for devices installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            units (Optional[nidaqmx.constants.TimeUnits]): Specifies the
                units to use to return the timestamp.
            sync_method (Optional[nidaqmx.constants.GpsSignalType]): 
                Specifies the method to use to synchronize the counter
                to a GPS receiver.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.CIChannel:

            Indicates the newly created channel object.
        

#### `def add_ci_lin_encoder_chan(self, counter, name_to_assign_to_channel='', decoding_type=EncoderType.X_4, zidx_enable=False, zidx_val=0, zidx_phase=EncoderZIndexPhase.AHIGH_BHIGH, units=LengthUnits.METERS, dist_per_pulse=0.001, initial_pos=0.0, custom_scale_name='')`


        Creates a channel that uses a linear encoder to measure linear
        position. With the exception of devices that support multi-
        counter tasks, you can create only one counter input channel at
        a time with this function because a task can contain only one
        counter input channel. To read from multiple counters
        simultaneously, use a separate task for each counter. Connect
        the input signals to the default input terminals of the counter
        unless you select different input terminals.

        Args:
            counter (str): Specifies the name of the counter to use to
                create the virtual channel. The DAQmx physical channel
                constant lists all physical channels, including
                counters, for devices installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            decoding_type (Optional[nidaqmx.constants.EncoderType]): 
                Specifies how to count and interpret the pulses the
                encoder generates on signal A and signal B. **X_1**,
                **X_2**, and **X_4** are valid for quadrature encoders
                only. **TWO_PULSE_COUNTING** is valid only for two-pulse
                encoders.
            zidx_enable (Optional[bool]): Specifies whether to use Z
                indexing for the channel.
            zidx_val (Optional[float]): Specifies in **units** the value
                to which to reset the measurement when signal Z is high
                and signal A and signal B are at the states you specify
                with **zidx_phase**.
            zidx_phase (Optional[nidaqmx.constants.EncoderZIndexPhase]): 
                Specifies the states at which signal A and signal B must
                be while signal Z is high for NI-DAQmx to reset the
                measurement. If signal Z is never high while signal A
                and signal B are high, for example, you must choose a
                phase other than **A_HIGH_B_HIGH**.
            units (Optional[nidaqmx.constants.LengthUnits]): Specifies
                the units to use to return linear position measurements
                from the channel.
            dist_per_pulse (Optional[float]): Is the distance to measure
                for each pulse the encoder generates on signal A or
                signal B. This value is in the units you specify with
                the **units** input.
            initial_pos (Optional[float]): Is the position of the
                encoder when you begin the measurement. This value is in
                the units you specify with the **units** input.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.CIChannel:

            Indicates the newly created channel object.
        

#### `def add_ci_lin_velocity_chan(self, counter, name_to_assign_to_channel='', min_val=0.0, max_val=1.0, decoding_type=EncoderType.X_4, units=VelocityUnits.METERS_PER_SECOND, dist_per_pulse=0.001, custom_scale_name='')`


        Creates a channel that uses a linear encoder to measure linear
        velocity. With the exception of devices that support multi-
        counter tasks, you can create only one counter input channel at
        a time with this function because a task can contain only one
        counter input channel. To read from multiple counters
        simultaneously, use a separate task for each counter. Connect
        the input signal to the default input terminal of the counter
        unless you select a different input terminal.

        Args:
            counter (str): Specifies the name of the counter to use to
                create the virtual channel. The DAQmx physical channel
                constant lists all physical channels, including
                counters, for devices installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            decoding_type (Optional[nidaqmx.constants.EncoderType]): 
                Specifies how to count and interpret the pulses the
                encoder generates on signal A and signal B. **X_1**,
                **X_2**, and **X_4** are valid for quadrature encoders
                only. **TWO_PULSE_COUNTING** is valid only for two-pulse
                encoders.
            units (Optional[nidaqmx.constants.VelocityUnits]): Specifies
                in which unit to return velocity measurements from the
                channel.
            dist_per_pulse (Optional[float]): Is the distance to measure
                for each pulse the encoder generates on signal A or
                signal B. This value is in the units you specify with
                the **units** input.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.CIChannel:

            Indicates the newly created channel object.
        

#### `def add_ci_period_chan(self, counter, name_to_assign_to_channel='', min_val=1e-06, max_val=0.1, units=TimeUnits.SECONDS, edge=Edge.RISING, meas_method=CounterFrequencyMethod.LOW_FREQUENCY_1_COUNTER, meas_time=0.001, divisor=4, custom_scale_name='')`


        Creates a channel to measure the period of a digital signal.
        With the exception of devices that support multi-counter tasks,
        you can create only one counter input channel at a time with
        this function because a task can contain only one counter input
        channel. To read from multiple counters simultaneously, use a
        separate task for each counter. Connect the input signal to the
        default input terminal of the counter unless you select a
        different input terminal.

        Args:
            counter (str): Specifies the name of the counter to use to
                create the virtual channel. The DAQmx physical channel
                constant lists all physical channels, including
                counters, for devices installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TimeUnits]): Specifies the
                units to use to return time or period measurements.
            edge (Optional[nidaqmx.constants.Edge]): Specifies between
                which edges to measure the frequency or period of the
                signal.
            meas_method (Optional[nidaqmx.constants.CounterFrequencyMethod]): 
                Specifies the method to use to calculate the period or
                frequency of the signal.
            meas_time (Optional[float]): Is the length of time in
                seconds to measure the frequency or period of the signal
                if **meas_method** is **HIGH_FREQUENCYWITH_2_COUNTERS**.
                Leave this input unspecified if **meas_method** is not
                **HIGH_FREQUENCYWITH_2_COUNTERS**.
            divisor (Optional[int]): Is the value by which to divide the
                input signal when **meas_method** is
                **LARGE_RANGEWITH_2_COUNTERS**. Leave this input
                unspecified if **meas_method** is not
                **LARGE_RANGEWITH_2_COUNTERS**.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.CIChannel:

            Indicates the newly created channel object.
        

#### `def add_ci_pulse_chan_freq(self, counter, name_to_assign_to_channel='', min_val=1000, max_val=1000000, units=FrequencyUnits.HZ)`


        Creates a channel to measure pulse specifications, returning the
        measurements as pairs of frequency and duty cycle. With the
        exception of devices that support multi-counter tasks, you can
        create only one counter input channel at a time with this
        function because a task can contain only one counter input
        channel. To read from multiple counters simultaneously, use a
        separate task for each counter. Connect the input signal to the
        default input terminal of the counter unless you select a
        different input terminal.

        Args:
            counter (str): Specifies the name of the counter to use to
                create the virtual channel. The DAQmx physical channel
                constant lists all physical channels, including
                counters, for devices installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.FrequencyUnits]): 
                Specifies the units to use to return pulse
                specifications in terms of frequency.
        Returns:
            nidaqmx.task.channels.CIChannel:

            Indicates the newly created channel object.
        

#### `def add_ci_pulse_chan_ticks(self, counter, name_to_assign_to_channel='', source_terminal='OnboardClock', min_val=1000, max_val=1000000)`


        Creates a channel to measure pulse specifications, returning the
        measurements as pairs of high ticks and low ticks. With the
        exception of devices that support multi-counter tasks, you can
        create only one counter input channel at a time with this
        function because a task can contain only one counter input
        channel. To read from multiple counters simultaneously, use a
        separate task for each counter. Connect the input signal to the
        default input terminal of the counter unless you select a
        different input terminal.

        Args:
            counter (str): Specifies the name of the counter to use to
                create the virtual channel. The DAQmx physical channel
                constant lists all physical channels, including
                counters, for devices installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            source_terminal (Optional[str]): Is the terminal to which
                you connect a signal to use as the source of ticks. A
                DAQmx terminal constant lists all terminals available on
                devices installed in the system. You also can specify a
                source terminal by specifying a string that contains a
                terminal name. If you specify OnboardClock, or do not
                specify any terminal, NI-DAQmx selects the fastest
                onboard timebase available on the device.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
        Returns:
            nidaqmx.task.channels.CIChannel:

            Indicates the newly created channel object.
        

#### `def add_ci_pulse_chan_time(self, counter, name_to_assign_to_channel='', min_val=1e-06, max_val=0.001, units=TimeUnits.SECONDS)`


        Creates a channel to measure pulse specifications, returning the
        measurements as pairs of high time and low time. With the
        exception of devices that support multi-counter tasks, you can
        create only one counter input channel at a time with this
        function because a task can contain only one counter input
        channel. To read from multiple counters simultaneously, use a
        separate task for each counter. Connect the input signal to the
        default input terminal of the counter unless you select a
        different input terminal.

        Args:
            counter (str): Specifies the name of the counter to use to
                create the virtual channel. The DAQmx physical channel
                constant lists all physical channels, including
                counters, for devices installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TimeUnits]): Specifies the
                units to use to return pulse specifications in terms of
                high time and low time.
        Returns:
            nidaqmx.task.channels.CIChannel:

            Indicates the newly created channel object.
        

#### `def add_ci_pulse_width_chan(self, counter, name_to_assign_to_channel='', min_val=1e-06, max_val=0.1, units=TimeUnits.SECONDS, starting_edge=Edge.RISING, custom_scale_name='')`


        Creates a channel to measure the width of a digital pulse.
        **starting_edge** determines whether to measure a high pulse or
        low pulse. With the exception of devices that support multi-
        counter tasks, you can create only one counter input channel at
        a time with this function because a task can contain only one
        counter input channel. To read from multiple counters
        simultaneously, use a separate task for each counter. Connect
        the input signal to the default input terminal of the counter
        unless you select a different input terminal.

        Args:
            counter (str): Specifies the name of the counter to use to
                create the virtual channel. The DAQmx physical channel
                constant lists all physical channels, including
                counters, for devices installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TimeUnits]): Specifies the
                units to use to return time or period measurements.
            starting_edge (Optional[nidaqmx.constants.Edge]): Specifies
                on which edge to begin measuring pulse width.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.CIChannel:

            Indicates the newly created channel object.
        

#### `def add_ci_semi_period_chan(self, counter, name_to_assign_to_channel='', min_val=1e-06, max_val=0.1, units=TimeUnits.SECONDS, custom_scale_name='')`


        Creates a channel to measure the time between state transitions
        of a digital signal. With the exception of devices that support
        multi-counter tasks, you can create only one counter input
        channel at a time with this function because a task can contain
        only one counter input channel. To read from multiple counters
        simultaneously, use a separate task for each counter. Connect
        the input signal to the default input terminal of the counter
        unless you select a different input terminal.

        Args:
            counter (str): Specifies the name of the counter to use to
                create the virtual channel. The DAQmx physical channel
                constant lists all physical channels, including
                counters, for devices installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TimeUnits]): Specifies the
                units to use to return time or period measurements.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.CIChannel:

            Indicates the newly created channel object.
        

#### `def add_ci_two_edge_sep_chan(self, counter, name_to_assign_to_channel='', min_val=1e-06, max_val=1.0, units=TimeUnits.SECONDS, first_edge=Edge.RISING, second_edge=Edge.FALLING, custom_scale_name='')`


        Creates a channel that measures the amount of time between the
        rising or falling edge of one digital signal and the rising or
        falling edge of another digital signal. With the exception of
        devices that support multi-counter tasks, you can create only
        one counter input channel at a time with this function because a
        task can contain only one counter input channel. To read from
        multiple counters simultaneously, use a separate task for each
        counter. Connect the input signals to the default input
        terminals of the counter unless you select different input
        terminals.

        Args:
            counter (str): Specifies the name of the counter to use to
                create the virtual channel. The DAQmx physical channel
                constant lists all physical channels, including
                counters, for devices installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            min_val (Optional[float]): Specifies in **units** the
                minimum value you expect to measure.
            max_val (Optional[float]): Specifies in **units** the
                maximum value you expect to measure.
            units (Optional[nidaqmx.constants.TimeUnits]): Specifies the
                units to use to return time or period measurements.
            first_edge (Optional[nidaqmx.constants.Edge]): Specifies on
                which edge of the first signal to start each
                measurement.
            second_edge (Optional[nidaqmx.constants.Edge]): Specifies on
                which edge of the second signal to stop each
                measurement.
            custom_scale_name (Optional[str]): Specifies the name of a
                custom scale for the channel. If you want the channel to
                use a custom scale, specify the name of the custom scale
                to this input and set **units** to
                **FROM_CUSTOM_SCALE**.
        Returns:
            nidaqmx.task.channels.CIChannel:

            Indicates the newly created channel object.
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/collections/_co_channel_collection.py -->
## PYTHON MODULE: generated/nidaqmx/task/collections/_co_channel_collection.py

### `class COChannelCollection(ChannelCollection)`


    Contains the collection of counter output channels for a DAQmx Task.
    

#### `def __init__(self, task_handle, interpreter)`


        Do not construct this object directly; instead, construct a nidaqmx.Task and use the task.co_channels property.
        

#### `def _create_chan(self, counter, name_to_assign_to_channel='')`


        Creates and returns a COChannel object.

        Args:
            counter (str): Specifies the names of the counters to use to 
                create virtual channels.
            name_to_assign_to_channel (Optional[str]): Specifies a name to 
                assign to the virtual channel this method creates.
        Returns:
            nidaqmx.task.channels.COChannel: 
            
            Specifies the newly created COChannel object.
        

#### `def add_co_pulse_chan_freq(self, counter, name_to_assign_to_channel='', units=FrequencyUnits.HZ, idle_state=Level.LOW, initial_delay=0.0, freq=1.0, duty_cycle=0.5)`


        Creates channel(s) to generate digital pulses that **freq** and
        **duty_cycle** define. The pulses appear on the default output
        terminal of the counter unless you select a different output
        terminal.

        Args:
            counter (str): Specifies the names of the counters to use to
                create the virtual channels. The DAQmx physical channel
                constant lists all physical channels, including
                counters, for devices installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            units (Optional[nidaqmx.constants.FrequencyUnits]): 
                Specifies the units in which to define pulse frequency.
            idle_state (Optional[nidaqmx.constants.Level]): Specifies
                the resting state of the output terminal.
            initial_delay (Optional[float]): Is the amount of time in
                seconds to wait before generating the first pulse.
            freq (Optional[float]): Specifies at what frequency to
                generate pulses.
            duty_cycle (Optional[float]): Is the width of the pulse
                divided by the pulse period. NI-DAQmx uses this ratio
                combined with frequency to determine pulse width and the
                interval between pulses.
        Returns:
            nidaqmx.task.channels.COChannel:

            Indicates the newly created channel object.
        

#### `def add_co_pulse_chan_ticks(self, counter, source_terminal, name_to_assign_to_channel='', idle_state=Level.LOW, initial_delay=0, low_ticks=100, high_ticks=100)`


        Creates channel(s) to generate digital pulses defined by the
        number of timebase ticks that the pulse is at a high state and
        the number of timebase ticks that the pulse is at a low state.
        The pulses appear on the default output terminal of the counter
        unless you select a different output terminal.

        Args:
            counter (str): Specifies the names of the counters to use to
                create the virtual channels. The DAQmx physical channel
                constant lists all physical channels, including
                counters, for devices installed in the system.
            source_terminal (str): Is the terminal to which you connect
                an external timebase. A DAQmx terminal constant lists
                all terminals available on devices installed in the
                system. You also can specify a source terminal by
                specifying a string that contains a terminal name.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            idle_state (Optional[nidaqmx.constants.Level]): Specifies
                the resting state of the output terminal.
            initial_delay (Optional[int]): Is the number of timebase
                ticks to wait before generating the first pulse.
            low_ticks (Optional[int]): Is the number of ticks the pulse
                is low.
            high_ticks (Optional[int]): Is the number of ticks the pulse
                is high.
        Returns:
            nidaqmx.task.channels.COChannel:

            Indicates the newly created channel object.
        

#### `def add_co_pulse_chan_time(self, counter, name_to_assign_to_channel='', units=TimeUnits.SECONDS, idle_state=Level.LOW, initial_delay=0.0, low_time=0.01, high_time=0.01)`


        Creates channel(s) to generate digital pulses defined by the
        amount of time the pulse is at a high state and the amount of
        time the pulse is at a low state. The pulses appear on the
        default output terminal of the counter unless you select a
        different output terminal.

        Args:
            counter (str): Specifies the names of the counters to use to
                create the virtual channels. The DAQmx physical channel
                constant lists all physical channels, including
                counters, for devices installed in the system.
            name_to_assign_to_channel (Optional[str]): Specifies a name
                to assign to the virtual channel this function creates.
                If you do not specify a value for this input, NI-DAQmx
                uses the physical channel name as the virtual channel
                name.
            units (Optional[nidaqmx.constants.TimeUnits]): Specifies the
                units in which to define pulse high and low time.
            idle_state (Optional[nidaqmx.constants.Level]): Specifies
                the resting state of the output terminal.
            initial_delay (Optional[float]): Is the amount of time in
                seconds to wait before generating the first pulse.
            low_time (Optional[float]): Is the amount of time the pulse
                is low.
            high_time (Optional[float]): Is the amount of time the pulse
                is high.
        Returns:
            nidaqmx.task.channels.COChannel:

            Indicates the newly created channel object.
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/collections/_di_channel_collection.py -->
## PYTHON MODULE: generated/nidaqmx/task/collections/_di_channel_collection.py

### `class DIChannelCollection(ChannelCollection)`


    Contains the collection of digital input channels for a DAQmx Task.
    

#### `def __init__(self, task_handle, interpreter)`


        Do not construct this object directly; instead, construct a nidaqmx.Task and use the task.di_channels property.
        

#### `def _create_chan(self, lines, line_grouping, name_to_assign_to_lines='')`


        Creates and returns a DIChannel object.

        Args:
            lines (str): Specifies the names of the lines to use to 
                create virtual channels.
            line_grouping (Optional[nidaqmx.constants.LineGrouping]):
                Specifies how to group digital lines into one or more
                virtual channels.
            name_to_assign_to_lines (Optional[str]): Specifies a name to 
                assign to the virtual channel this method creates.
        Returns:
            nidaqmx.task.channels.DIChannel: 
            
            Specifies the newly created DIChannel object.
        

#### `def add_di_chan(self, lines, name_to_assign_to_lines='', line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)`


        Creates channel(s) to measure digital signals. You can group
        digital lines into one digital channel or separate them into
        multiple digital channels. If you specify one or more entire
        ports in the **lines** input by using port physical channel
        names, you cannot separate the ports into multiple channels. To
        separate ports into multiple channels, use this function
        multiple times with a different port each time.

        Args:
            lines (str): Specifies the names of the digital lines or
                ports to use to create virtual channels. The DAQmx
                physical channel constant lists all lines and ports for
                devices installed in the system.
            name_to_assign_to_lines (Optional[str]): Specifies a name to
                assign to the virtual channel this function creates. If
                you do not specify a value for this input, NI-DAQmx uses
                the physical channel name as the virtual channel name.
            line_grouping (Optional[nidaqmx.constants.LineGrouping]): 
                Specifies how to group digital lines into one or more
                virtual channels. If you specify one or more entire
                ports with the **lines** input, you must set this input
                to **one channel for all lines**.
        Returns:
            nidaqmx.task.channels.DIChannel:

            Indicates the newly created channel object.
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/collections/_do_channel_collection.py -->
## PYTHON MODULE: generated/nidaqmx/task/collections/_do_channel_collection.py

### `class DOChannelCollection(ChannelCollection)`


    Contains the collection of digital output channels for a DAQmx Task.
    

#### `def __init__(self, task_handle, interpreter)`


        Do not construct this object directly; instead, construct a nidaqmx.Task and use the task.do_channels property.
        

#### `def _create_chan(self, lines, line_grouping, name_to_assign_to_lines='')`


        Creates and returns a DOChannel object.

        Args:
            lines (str): Specifies the names of the lines to use to 
                create virtual channels.
            line_grouping (Optional[nidaqmx.constants.LineGrouping]):
                Specifies how to group digital lines into one or more
                virtual channels.
            name_to_assign_to_lines (Optional[str]): Specifies a name to 
                assign to the virtual channel this method creates.
        Returns:
            nidaqmx.task.channels.DOChannel: 
            
            Specifies the newly created DOChannel object.
        

#### `def add_do_chan(self, lines, name_to_assign_to_lines='', line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)`


        Creates channel(s) to generate digital signals. You can group
        digital lines into one digital channel or separate them into
        multiple digital channels. If you specify one or more entire
        ports in **lines** input by using port physical channel names,
        you cannot separate the ports into multiple channels. To
        separate ports into multiple channels, use this function
        multiple times with a different port each time.

        Args:
            lines (str): Specifies the names of the digital lines or
                ports to use to create virtual channels. The DAQmx
                physical channel constant lists all lines and ports for
                devices installed in the system.
            name_to_assign_to_lines (Optional[str]): Specifies a name to
                assign to the virtual channel this function creates. If
                you do not specify a value for this input, NI-DAQmx uses
                the physical channel name as the virtual channel name.
            line_grouping (Optional[nidaqmx.constants.LineGrouping]): 
                Specifies how to group digital lines into one or more
                virtual channels. If you specify one or more entire
                ports with the **lines** input, you must set this input
                to **one channel for all lines**.
        Returns:
            nidaqmx.task.channels.DOChannel:

            Indicates the newly created channel object.
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/triggering/__init__.py -->
## PYTHON MODULE: generated/nidaqmx/task/triggering/__init__.py

### MODULE DOCSTRING

NI-DAQmx task triggering classes.

- `__all__ = ['Triggers', 'ArmStartTrigger', 'HandshakeTrigger', 'PauseTrigger', 'ReferenceTrigger', 'StartTrigger']`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/triggering/_arm_start_trigger.py -->
## PYTHON MODULE: generated/nidaqmx/task/triggering/_arm_start_trigger.py

### `class ArmStartTrigger()`


    Represents the arm start trigger configurations for a DAQmx task.
    

#### `def __init__(self, task_handle, interpreter)`

#### `def dig_edge_dig_fltr_enable(self)`


        bool: Specifies whether to apply the pulse width filter to the
            signal.
        

#### `def dig_edge_dig_fltr_enable(self, val)`

#### `def dig_edge_dig_fltr_enable(self)`

#### `def dig_edge_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def dig_edge_dig_fltr_min_pulse_width(self, val)`

#### `def dig_edge_dig_fltr_min_pulse_width(self)`

#### `def dig_edge_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def dig_edge_dig_fltr_timebase_rate(self, val)`

#### `def dig_edge_dig_fltr_timebase_rate(self)`

#### `def dig_edge_dig_fltr_timebase_src(self)`


        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        

#### `def dig_edge_dig_fltr_timebase_src(self, val)`

#### `def dig_edge_dig_fltr_timebase_src(self)`

#### `def dig_edge_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def dig_edge_dig_sync_enable(self, val)`

#### `def dig_edge_dig_sync_enable(self)`

#### `def dig_edge_edge(self)`


        :class:`nidaqmx.constants.Edge`: Specifies on which edge of a
            digital signal to arm the task for a Start Trigger.
        

#### `def dig_edge_edge(self, val)`

#### `def dig_edge_edge(self)`

#### `def dig_edge_src(self)`


        str: Specifies the name of a terminal where there is a digital
            signal to use as the source of the Arm Start Trigger.
        

#### `def dig_edge_src(self, val)`

#### `def dig_edge_src(self)`

#### `def term(self)`


        str: Indicates the name of the internal Arm Start Trigger
            terminal for the task. This property does not return the
            name of the trigger source terminal.
        

#### `def time_timescale(self)`


        :class:`nidaqmx.constants.Timescale`: Specifies the timescale to
            be used for timestamps used in an arm start time trigger.
        

#### `def time_timescale(self, val)`

#### `def time_timescale(self)`

#### `def time_when(self)`


        datetime: Specifies when to trigger the arm start trigger.
        

#### `def time_when(self, val)`

#### `def time_when(self)`

#### `def timestamp_enable(self)`


        bool: Specifies whether the arm start trigger timestamp is
            enabled. If the timestamp is enabled but no resources are
            available, an error will be returned at run time.
        

#### `def timestamp_enable(self, val)`

#### `def timestamp_enable(self)`

#### `def timestamp_timescale(self)`


        :class:`nidaqmx.constants.Timescale`: Specifies the arm start
            trigger timestamp timescale.
        

#### `def timestamp_timescale(self, val)`

#### `def timestamp_timescale(self)`

#### `def timestamp_val(self)`


        datetime: Indicates the arm start trigger timestamp value.
        

#### `def trig_type(self)`


        :class:`nidaqmx.constants.TriggerType`: Specifies the type of
            trigger to use to arm the task for a Start Trigger. If you
            configure an Arm Start Trigger, the task does not respond to
            a Start Trigger until the device receives the Arm Start
            Trigger.
        

#### `def trig_type(self, val)`

#### `def trig_type(self)`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/triggering/_handshake_trigger.py -->
## PYTHON MODULE: generated/nidaqmx/task/triggering/_handshake_trigger.py

### `class HandshakeTrigger()`


    Represents the handshake trigger configurations for a DAQmx task.
    

#### `def __init__(self, task_handle, interpreter)`

#### `def interlocked_asserted_lvl(self)`


        :class:`nidaqmx.constants.Level`: Specifies the asserted level
            of the Handshake Trigger.
        

#### `def interlocked_asserted_lvl(self, val)`

#### `def interlocked_asserted_lvl(self)`

#### `def interlocked_src(self)`


        str: Specifies the source terminal of the Handshake Trigger.
        

#### `def interlocked_src(self, val)`

#### `def interlocked_src(self)`

#### `def trig_type(self)`


        :class:`nidaqmx.constants.TriggerType`: Specifies the type of
            Handshake Trigger to use.
        

#### `def trig_type(self, val)`

#### `def trig_type(self)`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/triggering/_pause_trigger.py -->
## PYTHON MODULE: generated/nidaqmx/task/triggering/_pause_trigger.py

### `class PauseTrigger()`


    Represents the pause trigger configurations for a DAQmx task.
    

#### `def __init__(self, task_handle, interpreter)`

#### `def anlg_lvl_coupling(self)`


        :class:`nidaqmx.constants.Coupling`: Specifies the coupling for
            the source signal of the trigger if the source is a terminal
            rather than a virtual channel.
        

#### `def anlg_lvl_coupling(self, val)`

#### `def anlg_lvl_coupling(self)`

#### `def anlg_lvl_dig_fltr_enable(self)`


        bool: Specifies whether to apply a digital filter to the digital
            output of the analog triggering circuitry (the Analog
            Comparison Event). When enabled, the analog signal must stay
            above or below the trigger level for the minimum pulse width
            before being recognized. Use filtering  for noisy trigger
            signals that transition in and out of the hysteresis window
            rapidly.
        

#### `def anlg_lvl_dig_fltr_enable(self, val)`

#### `def anlg_lvl_dig_fltr_enable(self)`

#### `def anlg_lvl_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def anlg_lvl_dig_fltr_min_pulse_width(self, val)`

#### `def anlg_lvl_dig_fltr_min_pulse_width(self)`

#### `def anlg_lvl_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def anlg_lvl_dig_fltr_timebase_rate(self, val)`

#### `def anlg_lvl_dig_fltr_timebase_rate(self)`

#### `def anlg_lvl_dig_fltr_timebase_src(self)`


        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        

#### `def anlg_lvl_dig_fltr_timebase_src(self, val)`

#### `def anlg_lvl_dig_fltr_timebase_src(self)`

#### `def anlg_lvl_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def anlg_lvl_dig_sync_enable(self, val)`

#### `def anlg_lvl_dig_sync_enable(self)`

#### `def anlg_lvl_hyst(self)`


        float: Specifies a hysteresis level in the units of the
            measurement or generation. If **anlg_lvl_when** is
            **ActiveLevel.ABOVE**, the trigger does not deassert until
            the source signal passes below **anlg_lvl_lvl** minus the
            hysteresis. If **anlg_lvl_when** is **ActiveLevel.BELOW**,
            the trigger does not deassert until the source signal passes
            above **anlg_lvl_lvl** plus the hysteresis. Hysteresis is
            always enabled. Set this property to a non-zero value to use
            hysteresis.
        

#### `def anlg_lvl_hyst(self, val)`

#### `def anlg_lvl_hyst(self)`

#### `def anlg_lvl_lvl(self)`


        float: Specifies the threshold at which to pause the task.
            Specify this value in the units of the measurement or
            generation. Use **anlg_lvl_when** to specify whether the
            task pauses above or below this threshold.
        

#### `def anlg_lvl_lvl(self, val)`

#### `def anlg_lvl_lvl(self)`

#### `def anlg_lvl_src(self)`


        str: Specifies the name of a virtual channel or terminal where
            there is an analog signal to use as the source of the
            trigger.
        

#### `def anlg_lvl_src(self, val)`

#### `def anlg_lvl_src(self)`

#### `def anlg_lvl_when(self)`


        :class:`nidaqmx.constants.ActiveLevel`: Specifies whether the
            task pauses above or below the threshold you specify with
            **anlg_lvl_lvl**.
        

#### `def anlg_lvl_when(self, val)`

#### `def anlg_lvl_when(self)`

#### `def anlg_win_btm(self)`


        float: Specifies the lower limit of the window. Specify this
            value in the units of the measurement or generation.
        

#### `def anlg_win_btm(self, val)`

#### `def anlg_win_btm(self)`

#### `def anlg_win_coupling(self)`


        :class:`nidaqmx.constants.Coupling`: Specifies the coupling for
            the source signal of the terminal if the source is a
            terminal rather than a virtual channel.
        

#### `def anlg_win_coupling(self, val)`

#### `def anlg_win_coupling(self)`

#### `def anlg_win_dig_fltr_enable(self)`


        bool: Specifies whether to apply a digital filter to the digital
            output of the analog triggering circuitry (the Analog
            Comparison Event). When enabled, the analog signal must stay
            within the trigger window for the minimum pulse width before
            being recognized. Use filtering for noisy trigger signals
            that transition in and out of the window rapidly.
        

#### `def anlg_win_dig_fltr_enable(self, val)`

#### `def anlg_win_dig_fltr_enable(self)`

#### `def anlg_win_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def anlg_win_dig_fltr_min_pulse_width(self, val)`

#### `def anlg_win_dig_fltr_min_pulse_width(self)`

#### `def anlg_win_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def anlg_win_dig_fltr_timebase_rate(self, val)`

#### `def anlg_win_dig_fltr_timebase_rate(self)`

#### `def anlg_win_dig_fltr_timebase_src(self)`


        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        

#### `def anlg_win_dig_fltr_timebase_src(self, val)`

#### `def anlg_win_dig_fltr_timebase_src(self)`

#### `def anlg_win_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def anlg_win_dig_sync_enable(self, val)`

#### `def anlg_win_dig_sync_enable(self)`

#### `def anlg_win_src(self)`


        str: Specifies the name of a virtual channel or terminal where
            there is an analog signal to use as the source of the
            trigger.
        

#### `def anlg_win_src(self, val)`

#### `def anlg_win_src(self)`

#### `def anlg_win_top(self)`


        float: Specifies the upper limit of the window. Specify this
            value in the units of the measurement or generation.
        

#### `def anlg_win_top(self, val)`

#### `def anlg_win_top(self)`

#### `def anlg_win_when(self)`


        :class:`nidaqmx.constants.WindowTriggerCondition2`: Specifies
            whether the task pauses while the trigger signal is inside
            or outside the window you specify with **anlg_win_btm** and
            **anlg_win_top**.
        

#### `def anlg_win_when(self, val)`

#### `def anlg_win_when(self)`

#### `def dig_lvl_dig_fltr_enable(self)`


        bool: Specifies whether to apply a digital filter to the trigger
            signal.
        

#### `def dig_lvl_dig_fltr_enable(self, val)`

#### `def dig_lvl_dig_fltr_enable(self)`

#### `def dig_lvl_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def dig_lvl_dig_fltr_min_pulse_width(self, val)`

#### `def dig_lvl_dig_fltr_min_pulse_width(self)`

#### `def dig_lvl_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def dig_lvl_dig_fltr_timebase_rate(self, val)`

#### `def dig_lvl_dig_fltr_timebase_rate(self)`

#### `def dig_lvl_dig_fltr_timebase_src(self)`


        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        

#### `def dig_lvl_dig_fltr_timebase_src(self, val)`

#### `def dig_lvl_dig_fltr_timebase_src(self)`

#### `def dig_lvl_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def dig_lvl_dig_sync_enable(self, val)`

#### `def dig_lvl_dig_sync_enable(self)`

#### `def dig_lvl_src(self)`


        str: Specifies the name of a terminal where there is a digital
            signal to use as the source of the Pause Trigger.
        

#### `def dig_lvl_src(self, val)`

#### `def dig_lvl_src(self)`

#### `def dig_lvl_when(self)`


        :class:`nidaqmx.constants.Level`: Specifies whether the task
            pauses while the signal is high or low.
        

#### `def dig_lvl_when(self, val)`

#### `def dig_lvl_when(self)`

#### `def dig_pattern_pattern(self)`


        str: Specifies the digital pattern that must be met for the
            Pause Trigger to occur.
        

#### `def dig_pattern_pattern(self, val)`

#### `def dig_pattern_pattern(self)`

#### `def dig_pattern_src(self)`


        :class:`nidaqmx.system.physical_channel.PhysicalChannel`:
            Specifies the physical channels to use for pattern matching.
            The order of the physical channels determines the order of
            the pattern. If a port is included, the lines within the
            port are in ascending order.
        

#### `def dig_pattern_src(self, val)`

#### `def dig_pattern_src(self)`

#### `def dig_pattern_when(self)`


        :class:`nidaqmx.constants.DigitalPatternCondition`: Specifies if
            the Pause Trigger occurs when the physical channels
            specified with **dig_pattern_src** match or differ from the
            digital pattern specified with **dig_pattern_pattern**.
        

#### `def dig_pattern_when(self, val)`

#### `def dig_pattern_when(self)`

#### `def term(self)`


        str: Indicates the name of the internal Pause Trigger terminal
            for the task. This property does not return the name of the
            trigger source terminal.
        

#### `def trig_type(self)`


        :class:`nidaqmx.constants.TriggerType`: Specifies the type of
            trigger to use to pause a task.
        

#### `def trig_type(self, val)`

#### `def trig_type(self)`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/triggering/_reference_trigger.py -->
## PYTHON MODULE: generated/nidaqmx/task/triggering/_reference_trigger.py

### `class ReferenceTrigger()`


    Represents the reference trigger configurations for a DAQmx task.
    

#### `def __init__(self, task_handle, interpreter)`

#### `def anlg_edge_coupling(self)`


        :class:`nidaqmx.constants.Coupling`: Specifies the coupling for
            the source signal of the trigger if the source is a terminal
            rather than a virtual channel.
        

#### `def anlg_edge_coupling(self, val)`

#### `def anlg_edge_coupling(self)`

#### `def anlg_edge_dig_fltr_enable(self)`


        bool: Specifies whether to apply a digital filter to the digital
            output of the analog triggering circuitry (the Analog
            Comparison Event). When enabled, the analog signal must stay
            above or below the trigger level for the minimum pulse width
            before being recognized. Use filtering  for noisy trigger
            signals that transition in and out of the hysteresis window
            rapidly.
        

#### `def anlg_edge_dig_fltr_enable(self, val)`

#### `def anlg_edge_dig_fltr_enable(self)`

#### `def anlg_edge_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def anlg_edge_dig_fltr_min_pulse_width(self, val)`

#### `def anlg_edge_dig_fltr_min_pulse_width(self)`

#### `def anlg_edge_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def anlg_edge_dig_fltr_timebase_rate(self, val)`

#### `def anlg_edge_dig_fltr_timebase_rate(self)`

#### `def anlg_edge_dig_fltr_timebase_src(self)`


        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        

#### `def anlg_edge_dig_fltr_timebase_src(self, val)`

#### `def anlg_edge_dig_fltr_timebase_src(self)`

#### `def anlg_edge_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def anlg_edge_dig_sync_enable(self, val)`

#### `def anlg_edge_dig_sync_enable(self)`

#### `def anlg_edge_hyst(self)`


        float: Specifies a hysteresis level in the units of the
            measurement. If **anlg_edge_slope** is **Slope1.RISING**,
            the trigger does not deassert until the source signal passes
            below **anlg_edge_lvl** minus the hysteresis. If
            **anlg_edge_slope** is **Slope1.FALLING**, the trigger does
            not deassert until the source signal passes above
            **anlg_edge_lvl** plus the hysteresis. Hysteresis is always
            enabled. Set this property to a non-zero value to use
            hysteresis.
        

#### `def anlg_edge_hyst(self, val)`

#### `def anlg_edge_hyst(self)`

#### `def anlg_edge_lvl(self)`


        float: Specifies in the units of the measurement the threshold
            at which the Reference Trigger occurs.  Use
            **anlg_edge_slope** to specify on which slope to trigger at
            this threshold.
        

#### `def anlg_edge_lvl(self, val)`

#### `def anlg_edge_lvl(self)`

#### `def anlg_edge_slope(self)`


        :class:`nidaqmx.constants.Slope`: Specifies on which slope of
            the source signal the Reference Trigger occurs.
        

#### `def anlg_edge_slope(self, val)`

#### `def anlg_edge_slope(self)`

#### `def anlg_edge_src(self)`


        str: Specifies the name of a virtual channel or terminal where
            there is an analog signal to use as the source of the
            Reference Trigger.
        

#### `def anlg_edge_src(self, val)`

#### `def anlg_edge_src(self)`

#### `def anlg_multi_edge_couplings(self)`


        List[:class:`nidaqmx.constants.Coupling`]: Specifies an list
            that describes the couplings for the corresponding source
            signal of the trigger if the source is a terminal rather
            than a virtual channel. Each element of the list corresponds
            to a source in Ref.AnlgMultiEdge.Srcs and an element in each
            of the other Analog Multi Edge property lists, if they are
            not empty.
        

#### `def anlg_multi_edge_couplings(self, val)`

#### `def anlg_multi_edge_couplings(self)`

#### `def anlg_multi_edge_hysts(self)`


        List[float]: Specifies an list of hysteresis levels in the units
            of the measurement or generation. If the corresponding
            element of Ref.AnlgMultiEdge.Slopes is Rising, the trigger
            does not deassert until the source signal passes below the
            corresponding element of Ref.AnlgMultiEdge.Lvls minus the
            hysteresis. If Ref.AnlgEdge.Slope is Falling, the trigger
            does not deassert until the source signal passes above
            Ref.AnlgEdge.Lvl plus the hysteresis. Hysteresis is always
            enabled. Set this property to a non-zero value to use
            hysteresis. Each element of the list corresponds to a source
            in Ref.AnlgMultiEdge.Srcs and an element in each of the
            other Analog Multi Edge property lists, if they are not
            empty.
        

#### `def anlg_multi_edge_hysts(self, val)`

#### `def anlg_multi_edge_hysts(self)`

#### `def anlg_multi_edge_lvls(self)`


        List[float]: Specifies an list of thresholds in the units of the
            measurement or generation to start acquiring or generating
            samples. Each element of the list corresponds to a source in
            Ref.AnlgMultiEdge.Srcs and an element in each of the other
            Analog Multi Edge property lists, if they are not empty.
        

#### `def anlg_multi_edge_lvls(self, val)`

#### `def anlg_multi_edge_lvls(self)`

#### `def anlg_multi_edge_slopes(self)`


        List[:class:`nidaqmx.constants.Slope`]: Specifies an list of
            slopes on which to trigger task to start generating or
            acquiring samples. Each element of the list corresponds to a
            source in Ref.AnlgMultiEdge.Srcs and an element in each of
            the other Analog Multi Edge property lists, if they are not
            empty.
        

#### `def anlg_multi_edge_slopes(self, val)`

#### `def anlg_multi_edge_slopes(self)`

#### `def anlg_multi_edge_srcs(self)`


        str: Specifies a List and/or range of analog sources that are
            going to be used for Analog triggering. Each source
            corresponds to an element in each of the Analog Multi Edge
            property lists, if they are not empty.
        

#### `def anlg_multi_edge_srcs(self, val)`

#### `def anlg_multi_edge_srcs(self)`

#### `def anlg_win_btm(self)`


        float: Specifies the lower limit of the window. Specify this
            value in the units of the measurement.
        

#### `def anlg_win_btm(self, val)`

#### `def anlg_win_btm(self)`

#### `def anlg_win_coupling(self)`


        :class:`nidaqmx.constants.Coupling`: Specifies the coupling for
            the source signal of the trigger if the source is a terminal
            rather than a virtual channel.
        

#### `def anlg_win_coupling(self, val)`

#### `def anlg_win_coupling(self)`

#### `def anlg_win_dig_fltr_enable(self)`


        bool: Specifies whether to apply a digital filter to the digital
            output of the analog triggering circuitry (the Analog
            Comparison Event). When enabled, the analog signal must stay
            within the trigger window for the minimum pulse width before
            being recognized. Use filtering for noisy trigger signals
            that transition in and out of the window rapidly.
        

#### `def anlg_win_dig_fltr_enable(self, val)`

#### `def anlg_win_dig_fltr_enable(self)`

#### `def anlg_win_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def anlg_win_dig_fltr_min_pulse_width(self, val)`

#### `def anlg_win_dig_fltr_min_pulse_width(self)`

#### `def anlg_win_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def anlg_win_dig_fltr_timebase_rate(self, val)`

#### `def anlg_win_dig_fltr_timebase_rate(self)`

#### `def anlg_win_dig_fltr_timebase_src(self)`


        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        

#### `def anlg_win_dig_fltr_timebase_src(self, val)`

#### `def anlg_win_dig_fltr_timebase_src(self)`

#### `def anlg_win_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def anlg_win_dig_sync_enable(self, val)`

#### `def anlg_win_dig_sync_enable(self)`

#### `def anlg_win_src(self)`


        str: Specifies the name of a virtual channel or terminal where
            there is an analog signal to use as the source of the
            Reference Trigger.
        

#### `def anlg_win_src(self, val)`

#### `def anlg_win_src(self)`

#### `def anlg_win_top(self)`


        float: Specifies the upper limit of the window. Specify this
            value in the units of the measurement.
        

#### `def anlg_win_top(self, val)`

#### `def anlg_win_top(self)`

#### `def anlg_win_trig_when(self)`


        :class:`nidaqmx.constants.WindowTriggerCondition1`: Specifies
            whether the Reference Trigger occurs when the source signal
            enters the window or when it leaves the window. Use
            **anlg_win_btm** and **anlg_win_top** to specify the window.
        

#### `def anlg_win_trig_when(self, val)`

#### `def anlg_win_trig_when(self)`

#### `def auto_trig_enable(self)`


        bool: Specifies whether to send a software trigger to the device
            when a hardware trigger is no longer active in order to
            prevent a timeout.
        

#### `def auto_trig_enable(self, val)`

#### `def auto_trig_enable(self)`

#### `def auto_triggered(self)`


        bool: Indicates whether a completed acquisition was triggered by
            the auto trigger. If an acquisition has not completed after
            the task starts, this property returns False. This property
            is only applicable when **auto_trig_enable**  is True.
        

#### `def delay(self)`


        float: Specifies in seconds the time to wait after the device
            receives the Reference Trigger before switching from
            pretrigger to posttrigger samples.
        

#### `def delay(self, val)`

#### `def delay(self)`

#### `def dig_edge_dig_fltr_enable(self)`


        bool: Specifies whether to apply a digital filter to the trigger
            signal.
        

#### `def dig_edge_dig_fltr_enable(self, val)`

#### `def dig_edge_dig_fltr_enable(self)`

#### `def dig_edge_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def dig_edge_dig_fltr_min_pulse_width(self, val)`

#### `def dig_edge_dig_fltr_min_pulse_width(self)`

#### `def dig_edge_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def dig_edge_dig_fltr_timebase_rate(self, val)`

#### `def dig_edge_dig_fltr_timebase_rate(self)`

#### `def dig_edge_dig_fltr_timebase_src(self)`


        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        

#### `def dig_edge_dig_fltr_timebase_src(self, val)`

#### `def dig_edge_dig_fltr_timebase_src(self)`

#### `def dig_edge_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def dig_edge_dig_sync_enable(self, val)`

#### `def dig_edge_dig_sync_enable(self)`

#### `def dig_edge_edge(self)`


        :class:`nidaqmx.constants.Edge`: Specifies on what edge of a
            digital pulse the Reference Trigger occurs.
        

#### `def dig_edge_edge(self, val)`

#### `def dig_edge_edge(self)`

#### `def dig_edge_src(self)`


        str: Specifies the name of a terminal where there is a digital
            signal to use as the source of the Reference Trigger.
        

#### `def dig_edge_src(self, val)`

#### `def dig_edge_src(self)`

#### `def dig_pattern_pattern(self)`


        str: Specifies the digital pattern that must be met for the
            Reference Trigger to occur.
        

#### `def dig_pattern_pattern(self, val)`

#### `def dig_pattern_pattern(self)`

#### `def dig_pattern_src(self)`


        :class:`nidaqmx.system.physical_channel.PhysicalChannel`:
            Specifies the physical channels to use for pattern matching.
            The order of the physical channels determines the order of
            the pattern. If a port is included, the order of the
            physical channels within the port is in ascending order.
        

#### `def dig_pattern_src(self, val)`

#### `def dig_pattern_src(self)`

#### `def dig_pattern_trig_when(self)`


        :class:`nidaqmx.constants.DigitalPatternCondition`: Specifies
            whether the Reference Trigger occurs when the physical
            channels specified with **dig_pattern_src** match or differ
            from the digital pattern specified with
            **dig_pattern_pattern**.
        

#### `def dig_pattern_trig_when(self, val)`

#### `def dig_pattern_trig_when(self)`

#### `def max_num_trigs_to_detect(self)`


        int: Specifies the maximum number of times the task will detect
            a reference trigger during the task. The number of times a
            trigger is detected and acted upon by the module may be less
            than the specified amount if the task stops early because of
            trigger/retrigger window expiration. Specifying the Maximum
            Number of Triggers to Detect to be 0 causes the driver to
            automatically set this value to the maximum possible number
            of triggers detectable by the device and configuration
            combination. Note: The number of detected triggers may be
            less than number of trigger events occurring, because the
            devices were unable to respond to the trigger.
        

#### `def max_num_trigs_to_detect(self, val)`

#### `def max_num_trigs_to_detect(self)`

#### `def pretrig_samples(self)`


        int: Specifies the minimum number of pretrigger samples to
            acquire from each channel before recognizing the reference
            trigger. Post-trigger samples per channel are equal to
            **samp_quant_samp_per_chan** minus the number of pretrigger
            samples per channel.
        

#### `def pretrig_samples(self, val)`

#### `def pretrig_samples(self)`

#### `def retrigger_win(self)`


        float: Specifies the duration in seconds after each trigger
            during which the device may trigger. Once the window has
            passed, the device stops detecting triggers, and the task
            will stop after the device finishes acquiring post-trigger
            samples that it already started. Specifying a Retrigger
            Window of -1 causes the window to be infinite.
        

#### `def retrigger_win(self, val)`

#### `def retrigger_win(self)`

#### `def retriggerable(self)`


        bool: Specifies whether a finite task resets, acquires
            pretrigger samples, and waits for another Reference Trigger
            after the task completes. When you set this property to
            True, the device will acquire post-trigger samples, reset,
            and acquire pretrigger samples each time the Reference
            Trigger occurs until the task stops. The device ignores a
            trigger if it is in the process of acquiring signals.
        

#### `def retriggerable(self, val)`

#### `def retriggerable(self)`

#### `def term(self)`


        str: Indicates the name of the internal Reference Trigger
            terminal for the task. This property does not return the
            name of the trigger source terminal.
        

#### `def timestamp_enable(self)`


        bool: Specifies whether the reference trigger timestamp is
            enabled. If the timestamp is enabled but no resources are
            available, an error will be returned at run time.
        

#### `def timestamp_enable(self, val)`

#### `def timestamp_enable(self)`

#### `def timestamp_timescale(self)`


        :class:`nidaqmx.constants.Timescale`: Specifies the reference
            trigger timestamp timescale.
        

#### `def timestamp_timescale(self, val)`

#### `def timestamp_timescale(self)`

#### `def timestamp_val(self)`


        datetime: Indicates the reference trigger timestamp value.
        

#### `def trig_type(self)`


        :class:`nidaqmx.constants.TriggerType`: Specifies the type of
            trigger to use to mark a reference point for the
            measurement.
        

#### `def trig_type(self, val)`

#### `def trig_type(self)`

#### `def trig_win(self)`


        float: Specifies the duration in seconds after the task starts
            during which the device may trigger. Once the window has
            passed, the device stops detecting triggers, and the task
            will stop after the device finishes acquiring post-trigger
            samples that it already started. If no triggers are detected
            during the entire period, then no data will be returned.
            Specifying a Trigger Window of -1 causes the window to be
            infinite.
        

#### `def trig_win(self, val)`

#### `def trig_win(self)`

#### `def cfg_anlg_edge_ref_trig(self, trigger_source, pretrigger_samples, trigger_slope=Slope.RISING, trigger_level=0.0)`


        Configures the task to stop the acquisition when the device
        acquires all pretrigger samples; an analog signal reaches the
        level you specify; and the device acquires all post-trigger
        samples. When you use a Reference Trigger, the default for the
        read RelativeTo property is **first_pretrigger_sample** with a
        read Offset of 0.

        Args:
            trigger_source (str): Is the name of a virtual channel or
                terminal where there is an analog signal to use as the
                source of the trigger.
            pretrigger_samples (int): Specifies the minimum number of
                samples to acquire per channel before recognizing the
                Reference Trigger. The number of post-trigger samples
                per channel is equal to **number of samples per
                channel** in the DAQmx Timing function minus
                **pretrigger_samples**.
            trigger_slope (Optional[nidaqmx.constants.Slope]): Specifies
                on which slope of the signal the Reference Trigger
                occurs.
            trigger_level (Optional[float]): Specifies at what threshold
                to trigger. Specify this value in the units of the
                measurement or generation. Use **trigger_slope** to
                specify on which slope to trigger at this threshold.
        

#### `def cfg_anlg_multi_edge_ref_trig(self, trigger_sources, pretrigger_samples, trigger_slope_array=None, trigger_level_array=None)`


        Configures the task to stop the acquisition when the device
        acquires all pretrigger samples; any of the configured analog
        signals cross the respective levels you specified; and the
        device acquires all post-trigger samples. When you use a
        Reference Trigger, the default for the read RelativeTo property
        is First Pretrigger Sample with a read Offset of 0. Multi-edge
        triggering treats the specified triggers as if a logical OR is
        applied.

        Args:
            trigger_sources (str): Is the name of a virtual channel or
                terminal where there is an analog signal to use as the
                source of the trigger.
            pretrigger_samples (int): Specifies the minimum number of
                samples to acquire per channel before recognizing the
                Reference Trigger. The number of post-trigger samples
                per channel is equal to **number of samples per
                channel** in the DAQmx Timing VI minus **pretrigger
                samples per channel**.
            trigger_slope_array (Optional[List[nidaqmx.constants.Slope]]): 
                Specifies on which slope of the signal the Reference
                Trigger occurs.
            trigger_level_array (Optional[List[float]]): Specifies at
                what threshold to trigger. Specify this value in the
                units of the measurement or generation. Use **slope** to
                specify on which slope to trigger at this threshold.
        

#### `def cfg_anlg_window_ref_trig(self, trigger_source, window_top, window_bottom, pretrigger_samples, trigger_when=WindowTriggerCondition1.ENTERING_WINDOW)`


        Configures the task to stop the acquisition when the device
        acquires all pretrigger samples; an analog signal enters or
        leaves a range you specify; and the device acquires all post-
        trigger samples. When you use a Reference Trigger, the default
        for the read RelativeTo property is **first_pretrigger_sample**
        with a read Offset of 0.

        Args:
            trigger_source (str): Is the name of a virtual channel or
                terminal where there is an analog signal to use as the
                source of the trigger.
            window_top (float): Is the upper limit of the window.
                Specify this value in the units of the measurement or
                generation.
            window_bottom (float): Is the lower limit of the window.
                Specify this value in the units of the measurement or
                generation.
            pretrigger_samples (int): Specifies the minimum number of
                samples to acquire per channel before recognizing the
                Reference Trigger. The number of post-trigger samples
                per channel is equal to **number of samples per
                channel** in the DAQmx Timing function minus
                **pretrigger_samples**.
            trigger_when (Optional[nidaqmx.constants.WindowTriggerCondition1]): 
                Specifies whether the Reference Trigger occurs when the
                signal enters the window or when it leaves the window.
                Use **window_bottom** and **window_top** to specify the
                limits of the window.
        

#### `def cfg_dig_edge_ref_trig(self, trigger_source, pretrigger_samples, trigger_edge=Edge.RISING)`


        Configures the task to stop the acquisition when the device
        acquires all pretrigger samples, detects a rising or falling
        edge of a digital signal, and acquires all posttrigger samples.
        When you use a Reference Trigger, the default for the read
        RelativeTo property is **first_pretrigger_sample** with a read
        Offset of 0.

        Args:
            trigger_source (str): Specifies the name of a terminal where
                there is a digital signal to use as the source of the
                trigger.
            pretrigger_samples (int): Specifies the minimum number of
                samples to acquire per channel before recognizing the
                Reference Trigger. The number of post-trigger samples
                per channel is equal to **number of samples per
                channel** in the DAQmx Timing function minus
                **pretrigger_samples**.
            trigger_edge (Optional[nidaqmx.constants.Edge]): Specifies
                on which edge of the digital signal the Reference
                Trigger occurs.
        

#### `def cfg_dig_pattern_ref_trig(self, trigger_source, trigger_pattern, pretrigger_samples, trigger_when=DigitalPatternCondition.PATTERN_MATCHES)`


        Configures the task to stop the acquisition when the device
        acquires all pretrigger samples, matches a digital pattern, and
        acquires all posttrigger samples. When you use a Reference
        Trigger, the default for the read RelativeTo property is First
        PretriggerSample with a read Offset of zero.

        Args:
            trigger_source (str): Specifies the physical channels to use
                for pattern matching. The order of the physical channels
                determines the order of the pattern. If a port is
                included, the order of the physical channels within the
                port is in ascending order.
            trigger_pattern (str): Specifies the digital pattern that
                must be met for the trigger to occur.
            pretrigger_samples (int): Specifies the minimum number of
                samples to acquire per channel before recognizing the
                Reference Trigger. The number of post-trigger samples
                per channel is equal to **number of samples per
                channel** in the DAQmx Timing function minus
                **pretrigger_samples**.
            trigger_when (Optional[nidaqmx.constants.DigitalPatternCondition]): 
                Specifies the condition under which the trigger occurs.
        

#### `def disable_ref_trig(self)`


        Disables reference triggering for the measurement.
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/triggering/_start_trigger.py -->
## PYTHON MODULE: generated/nidaqmx/task/triggering/_start_trigger.py

### `class StartTrigger()`


    Represents the start trigger configurations for a DAQmx task.
    

#### `def __init__(self, task_handle, interpreter)`

#### `def anlg_edge_coupling(self)`


        :class:`nidaqmx.constants.Coupling`: Specifies the coupling for
            the source signal of the trigger if the source is a terminal
            rather than a virtual channel.
        

#### `def anlg_edge_coupling(self, val)`

#### `def anlg_edge_coupling(self)`

#### `def anlg_edge_dig_fltr_enable(self)`


        bool: Specifies whether to apply a digital filter to the digital
            output of the analog triggering circuitry (the Analog
            Comparison Event). When enabled, the analog signal must stay
            above or below the trigger level for the minimum pulse width
            before being recognized. Use filtering  for noisy trigger
            signals that transition in and out of the hysteresis window
            rapidly.
        

#### `def anlg_edge_dig_fltr_enable(self, val)`

#### `def anlg_edge_dig_fltr_enable(self)`

#### `def anlg_edge_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def anlg_edge_dig_fltr_min_pulse_width(self, val)`

#### `def anlg_edge_dig_fltr_min_pulse_width(self)`

#### `def anlg_edge_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def anlg_edge_dig_fltr_timebase_rate(self, val)`

#### `def anlg_edge_dig_fltr_timebase_rate(self)`

#### `def anlg_edge_dig_fltr_timebase_src(self)`


        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        

#### `def anlg_edge_dig_fltr_timebase_src(self, val)`

#### `def anlg_edge_dig_fltr_timebase_src(self)`

#### `def anlg_edge_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def anlg_edge_dig_sync_enable(self, val)`

#### `def anlg_edge_dig_sync_enable(self)`

#### `def anlg_edge_hyst(self)`


        float: Specifies a hysteresis level in the units of the
            measurement or generation. If **anlg_edge_slope** is
            **Slope1.RISING**, the trigger does not deassert until the
            source signal passes below  **anlg_edge_lvl** minus the
            hysteresis. If **anlg_edge_slope** is **Slope1.FALLING**,
            the trigger does not deassert until the source signal passes
            above **anlg_edge_lvl** plus the hysteresis. Hysteresis is
            always enabled. Set this property to a non-zero value to use
            hysteresis.
        

#### `def anlg_edge_hyst(self, val)`

#### `def anlg_edge_hyst(self)`

#### `def anlg_edge_lvl(self)`


        float: Specifies at what threshold in the units of the
            measurement or generation to start acquiring or generating
            samples. Use **anlg_edge_slope** to specify on which slope
            to trigger on this threshold.
        

#### `def anlg_edge_lvl(self, val)`

#### `def anlg_edge_lvl(self)`

#### `def anlg_edge_slope(self)`


        :class:`nidaqmx.constants.Slope`: Specifies on which slope of
            the trigger signal to start acquiring or generating samples.
        

#### `def anlg_edge_slope(self, val)`

#### `def anlg_edge_slope(self)`

#### `def anlg_edge_src(self)`


        str: Specifies the name of a virtual channel or terminal where
            there is an analog signal to use as the source of the Start
            Trigger.
        

#### `def anlg_edge_src(self, val)`

#### `def anlg_edge_src(self)`

#### `def anlg_multi_edge_couplings(self)`


        List[:class:`nidaqmx.constants.Coupling`]: Specifies an list
            that describes the couplings for the corresponding source
            signal of the trigger if the source is a terminal rather
            than a virtual channel. Each element of the list corresponds
            to a source in Start.AnlgMultiEdge.Srcs and an element in
            each of the other Analog Multi Edge property lists, if they
            are not empty.
        

#### `def anlg_multi_edge_couplings(self, val)`

#### `def anlg_multi_edge_couplings(self)`

#### `def anlg_multi_edge_hysts(self)`


        List[float]: Specifies an list of hysteresis levels in the units
            of the measurement or generation. If the corresponding
            element of Start.AnlgMultiEdge.Slopes is Rising, the trigger
            does not deassert until the source signal passes below the
            corresponding element of Start.AnlgMultiEdge.Lvls minus the
            hysteresis. If Start.AnlgEdge.Slope is Falling, the trigger
            does not deassert until the source signal passes above
            Start.AnlgEdge.Lvl plus the hysteresis. Hysteresis is always
            enabled. Set this property to a non-zero value to use
            hysteresis. Each element of the list corresponds to a source
            in Start.AnlgMultiEdge.Srcs and an element in each of the
            other Analog Multi Edge property lists, if they are not
            empty.
        

#### `def anlg_multi_edge_hysts(self, val)`

#### `def anlg_multi_edge_hysts(self)`

#### `def anlg_multi_edge_lvls(self)`


        List[float]: Specifies an list of thresholds in the units of the
            measurement or generation to start acquiring or generating
            samples. Each element of the list corresponds to a source in
            Start.AnlgMultiEdge.Srcs and an element in each of the other
            Analog Multi Edge property lists, if they are not empty.
        

#### `def anlg_multi_edge_lvls(self, val)`

#### `def anlg_multi_edge_lvls(self)`

#### `def anlg_multi_edge_slopes(self)`


        List[:class:`nidaqmx.constants.Slope`]: Specifies an list of
            slopes on which to trigger task to start generating or
            acquiring samples. Each element of the list corresponds to a
            source in Start.AnlgMultiEdge.Srcs and an element in each of
            the other Analog Multi Edge property lists, if they are not
            empty.
        

#### `def anlg_multi_edge_slopes(self, val)`

#### `def anlg_multi_edge_slopes(self)`

#### `def anlg_multi_edge_srcs(self)`


        str: Specifies a list and/or range of analog sources that are
            going to be used for Analog triggering. Each source
            corresponds to an element in each of the Analog Multi Edge
            property lists, if they are not empty.
        

#### `def anlg_multi_edge_srcs(self, val)`

#### `def anlg_multi_edge_srcs(self)`

#### `def anlg_win_btm(self)`


        float: Specifies the lower limit of the window. Specify this
            value in the units of the measurement or generation.
        

#### `def anlg_win_btm(self, val)`

#### `def anlg_win_btm(self)`

#### `def anlg_win_coupling(self)`


        :class:`nidaqmx.constants.Coupling`: Specifies the coupling for
            the source signal of the trigger if the source is a terminal
            rather than a virtual channel.
        

#### `def anlg_win_coupling(self, val)`

#### `def anlg_win_coupling(self)`

#### `def anlg_win_dig_fltr_enable(self)`


        bool: Specifies whether to apply a digital filter to the digital
            output of the analog triggering circuitry (the Analog
            Comparison Event). When enabled, the analog signal must stay
            within the trigger window for the minimum pulse width before
            being recognized. Use filtering for noisy trigger signals
            that transition in and out of the window rapidly.
        

#### `def anlg_win_dig_fltr_enable(self, val)`

#### `def anlg_win_dig_fltr_enable(self)`

#### `def anlg_win_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def anlg_win_dig_fltr_min_pulse_width(self, val)`

#### `def anlg_win_dig_fltr_min_pulse_width(self)`

#### `def anlg_win_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the digital filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def anlg_win_dig_fltr_timebase_rate(self, val)`

#### `def anlg_win_dig_fltr_timebase_rate(self)`

#### `def anlg_win_dig_fltr_timebase_src(self)`


        str: Specifies the terminal of the signal to use as the timebase
            of the digital filter.
        

#### `def anlg_win_dig_fltr_timebase_src(self, val)`

#### `def anlg_win_dig_fltr_timebase_src(self)`

#### `def anlg_win_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device.
        

#### `def anlg_win_dig_sync_enable(self, val)`

#### `def anlg_win_dig_sync_enable(self)`

#### `def anlg_win_src(self)`


        str: Specifies the name of a virtual channel or terminal where
            there is an analog signal to use as the source of the Start
            Trigger.
        

#### `def anlg_win_src(self, val)`

#### `def anlg_win_src(self)`

#### `def anlg_win_top(self)`


        float: Specifies the upper limit of the window. Specify this
            value in the units of the measurement or generation.
        

#### `def anlg_win_top(self, val)`

#### `def anlg_win_top(self)`

#### `def anlg_win_trig_when(self)`


        :class:`nidaqmx.constants.WindowTriggerCondition1`: Specifies
            whether the task starts acquiring or generating samples when
            the signal enters or leaves the window you specify with
            **anlg_win_btm** and **anlg_win_top**.
        

#### `def anlg_win_trig_when(self, val)`

#### `def anlg_win_trig_when(self)`

#### `def delay(self)`


        float: Specifies an amount of time to wait after the Start
            Trigger is received before acquiring or generating the first
            sample. This value is in the units you specify with
            **delay_units**.
        

#### `def delay(self, val)`

#### `def delay(self)`

#### `def delay_units(self)`


        :class:`nidaqmx.constants.DigitalWidthUnits`: Specifies the
            units of **delay**.
        

#### `def delay_units(self, val)`

#### `def delay_units(self)`

#### `def dig_edge_dig_fltr_enable(self)`


        bool: Specifies whether to apply a digital filter to the trigger
            signal.
        

#### `def dig_edge_dig_fltr_enable(self, val)`

#### `def dig_edge_dig_fltr_enable(self)`

#### `def dig_edge_dig_fltr_min_pulse_width(self)`


        float: Specifies in seconds the minimum pulse width the filter
            recognizes.
        

#### `def dig_edge_dig_fltr_min_pulse_width(self, val)`

#### `def dig_edge_dig_fltr_min_pulse_width(self)`

#### `def dig_edge_dig_fltr_timebase_rate(self)`


        float: Specifies in hertz the rate of the pulse width filter
            timebase. NI-DAQmx uses this value to compute settings for
            the filter.
        

#### `def dig_edge_dig_fltr_timebase_rate(self, val)`

#### `def dig_edge_dig_fltr_timebase_rate(self)`

#### `def dig_edge_dig_fltr_timebase_src(self)`


        str: Specifies the input terminal of the signal to use as the
            timebase of the pulse width filter.
        

#### `def dig_edge_dig_fltr_timebase_src(self, val)`

#### `def dig_edge_dig_fltr_timebase_src(self)`

#### `def dig_edge_dig_sync_enable(self)`


        bool: Specifies whether to synchronize recognition of
            transitions in the signal to the internal timebase of the
            device. If you set this property to True, the device does
            not recognize and act upon the trigger until the next pulse
            of the internal timebase.
        

#### `def dig_edge_dig_sync_enable(self, val)`

#### `def dig_edge_dig_sync_enable(self)`

#### `def dig_edge_edge(self)`


        :class:`nidaqmx.constants.Edge`: Specifies on which edge of a
            digital pulse to start acquiring or generating samples.
        

#### `def dig_edge_edge(self, val)`

#### `def dig_edge_edge(self)`

#### `def dig_edge_src(self)`


        str: Specifies the name of a terminal where there is a digital
            signal to use as the source of the Start Trigger.
        

#### `def dig_edge_src(self, val)`

#### `def dig_edge_src(self)`

#### `def dig_pattern_pattern(self)`


        str: Specifies the digital pattern that must be met for the
            Start Trigger to occur.
        

#### `def dig_pattern_pattern(self, val)`

#### `def dig_pattern_pattern(self)`

#### `def dig_pattern_src(self)`


        :class:`nidaqmx.system.physical_channel.PhysicalChannel`:
            Specifies the physical channels to use for pattern matching.
            The order of the physical channels determines the order of
            the pattern. If a port is included, the order of the
            physical channels within the port is in ascending order.
        

#### `def dig_pattern_src(self, val)`

#### `def dig_pattern_src(self)`

#### `def dig_pattern_trig_when(self)`


        :class:`nidaqmx.constants.DigitalPatternCondition`: Specifies
            whether the Start Trigger occurs when the physical channels
            specified with **dig_pattern_src** match or differ from the
            digital pattern specified with **dig_pattern_pattern**.
        

#### `def dig_pattern_trig_when(self, val)`

#### `def dig_pattern_trig_when(self)`

#### `def max_num_trigs_to_detect(self)`


        int: Specifies the maximum number of times the task will detect
            a start trigger during the task. The number of times a
            trigger is detected and acted upon by the module may be less
            than the specified amount if the task stops early because of
            trigger/retrigger window expiration. Specifying the Maximum
            Number of Triggers to Detect to be 0 causes the driver to
            automatically set this value to the maximum possible number
            of triggers detectable by the device and configuration
            combination. Note: The number of detected triggers may be
            less than number of trigger events occurring, because the
            devices were unable to respond to the trigger.
        

#### `def max_num_trigs_to_detect(self, val)`

#### `def max_num_trigs_to_detect(self)`

#### `def retrigger_win(self)`


        float: Specifies the period of time in seconds after each
            trigger during which the device may trigger. Once the window
            has expired, the device stops detecting triggers, and the
            task will finish after the device finishes acquiring post-
            trigger samples that it already started. Ensure the period
            of time specified covers the entire time span desired for
            retrigger detection to avoid missed triggers. Specifying a
            Retrigger Window of -1 causes the window to be infinite.
        

#### `def retrigger_win(self, val)`

#### `def retrigger_win(self)`

#### `def retriggerable(self)`


        bool: Specifies whether a finite task resets and waits for
            another Start Trigger after the task completes. When you set
            this property to True, the device performs a finite
            acquisition or generation each time the Start Trigger occurs
            until the task stops. The device ignores a trigger if it is
            in the process of acquiring or generating signals.
        

#### `def retriggerable(self, val)`

#### `def retriggerable(self)`

#### `def term(self)`


        str: Indicates the name of the internal Start Trigger terminal
            for the task. This property does not return the name of the
            trigger source terminal.
        

#### `def time_timescale(self)`


        :class:`nidaqmx.constants.Timescale`: Specifies the timescale to
            be used for timestamps used in a time trigger.
        

#### `def time_timescale(self, val)`

#### `def time_timescale(self)`

#### `def time_when(self)`


        datetime: Specifies when to trigger the start trigger.
        

#### `def time_when(self, val)`

#### `def time_when(self)`

#### `def timestamp_enable(self)`


        bool: Specifies whether the start trigger timestamp is enabled.
            If the timestamp is enabled but no resources are available,
            an error will be returned at run time.
        

#### `def timestamp_enable(self, val)`

#### `def timestamp_enable(self)`

#### `def timestamp_timescale(self)`


        :class:`nidaqmx.constants.Timescale`: Specifies the start
            trigger timestamp timescale.
        

#### `def timestamp_timescale(self, val)`

#### `def timestamp_timescale(self)`

#### `def timestamp_val(self)`


        datetime: Indicates the start trigger timestamp value.
        

#### `def trig_type(self)`


        :class:`nidaqmx.constants.TriggerType`: Specifies the type of
            trigger to use to start a task.
        

#### `def trig_type(self, val)`

#### `def trig_type(self)`

#### `def trig_win(self)`


        float: Specifies the period of time in seconds after the task
            starts during which the device may trigger. Once the window
            has expired, the device stops detecting triggers, and the
            task will finish after the device finishes acquiring post-
            trigger samples for any triggers detected. If no triggers
            are detected during the entire period, then no data will be
            returned. Ensure the period of time specified covers the
            entire time span desired for trigger detection to avoid
            missed triggers. Specifying a Trigger Window of -1 causes
            the window to be infinite.
        

#### `def trig_win(self, val)`

#### `def trig_win(self)`

#### `def cfg_anlg_edge_start_trig(self, trigger_source='', trigger_slope=Slope.RISING, trigger_level=0.0)`


        Configures the task to start acquiring or generating samples
        when an analog signal crosses the level you specify.

        Args:
            trigger_source (Optional[str]): Is the name of a virtual
                channel or terminal where there is an analog signal to
                use as the source of the trigger.
            trigger_slope (Optional[nidaqmx.constants.Slope]): Specifies
                on which slope of the signal to start acquiring or
                generating samples when the signal crosses
                **trigger_level**.
            trigger_level (Optional[float]): Specifies at what threshold
                to start acquiring or generating samples. Specify this
                value in the units of the measurement or generation. Use
                **trigger_slope** to specify on which slope to trigger
                at this threshold.
        

#### `def cfg_anlg_multi_edge_start_trig(self, trigger_sources, trigger_slope_array, trigger_level_array=None)`


        Configures the task to start acquiring or generating samples
        when any of the configured analog signals cross the respective
        levels you specified. Multi-edge triggering treats the
        configured triggers as if a logical OR is applied.

        Args:
            trigger_sources (str): Is the name of a virtual channel or
                terminal where there is an analog signal to use as the
                source of the trigger.
            trigger_slope_array (List[nidaqmx.constants.Slope]): 
                Specifies on which slope of the signal to start
                acquiring or generating samples when the signal crosses
                **level**.
            trigger_level_array (Optional[List[float]]): Specifies at
                what threshold to start acquiring or generating samples.
                Specify this value in the units of the measurement or
                generation. Use **slope** to specify on which slope to
                trigger at this threshold.
        

#### `def cfg_anlg_window_start_trig(self, window_top, window_bottom, trigger_source='', trigger_when=WindowTriggerCondition1.ENTERING_WINDOW)`


        Configures the task to start acquiring or generating samples
        when an analog signal enters or leaves a range you specify.

        Args:
            window_top (float): Is the upper limit of the window.
                Specify this value in the units of the measurement or
                generation.
            window_bottom (float): Is the lower limit of the window.
                Specify this value in the units of the measurement or
                generation.
            trigger_source (Optional[str]): Is the name of a virtual
                channel or terminal where there is an analog signal to
                use as the source of the trigger.
            trigger_when (Optional[nidaqmx.constants.WindowTriggerCondition1]): 
                Specifies whether the task starts measuring or
                generating samples when the signal enters the window or
                when it leaves the window. Use **window_bottom** and
                **window_top** to specify the limits of the window.
        

#### `def cfg_dig_edge_start_trig(self, trigger_source, trigger_edge=Edge.RISING)`


        Configures the task to start acquiring or generating samples on
        a rising or falling edge of a digital signal.

        Args:
            trigger_source (str): Specifies the name of a terminal where
                there is a digital signal to use as the source of the
                trigger.
            trigger_edge (Optional[nidaqmx.constants.Edge]): Specifies
                on which edge of the digital signal to start acquiring
                or generating samples.
        

#### `def cfg_dig_pattern_start_trig(self, trigger_source, trigger_pattern, trigger_when=DigitalPatternCondition.PATTERN_MATCHES)`


        Configures a task to start acquiring or generating samples when
        a digital pattern is matched.

        Args:
            trigger_source (str): Specifies the physical channels to use
                for pattern matching. The order of the physical channels
                determines the order of the pattern. If a port is
                included, the order of the physical channels within the
                port is in ascending order.
            trigger_pattern (str): Specifies the digital pattern that
                must be met for the trigger to occur.
            trigger_when (Optional[nidaqmx.constants.DigitalPatternCondition]): 
                Specifies the condition under which the trigger occurs.
        

#### `def cfg_time_start_trig(self, when, timescale=Timescale.USE_HOST)`


        Configures the task to start acquiring or generating samples at
        a specified time.

        Args:
            when (datetime): Specifies when to trigger.
            timescale (Optional[nidaqmx.constants.Timescale]): Specifies
                the start trigger timestamp time scale.
        

#### `def disable_start_trig(self)`


        Configures the task to start acquiring or generating samples
        immediately upon starting the task.
        

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/task/triggering/_triggers.py -->
## PYTHON MODULE: generated/nidaqmx/task/triggering/_triggers.py

### `class Triggers()`


    Represents the trigger configurations for a DAQmx task.
    

#### `def __init__(self, task_handle, interpreter)`

#### `def arm_start_trigger(self) -> ArmStartTrigger`


        Gets the arm start trigger configurations for the task.
        

#### `def handshake_trigger(self) -> HandshakeTrigger`


        Gets the handshake trigger configurations for the task.
        

#### `def pause_trigger(self) -> PauseTrigger`


        Gets the pause trigger configurations for the task.
        

#### `def reference_trigger(self) -> ReferenceTrigger`


        Gets the reference trigger configurations for the task.
        

#### `def start_trigger(self) -> StartTrigger`


        Gets the start trigger configurations for the task.
        

#### `def sync_type(self)`


        :class:`nidaqmx.constants.SyncType`: Specifies the role of the
            device in a synchronized system. Setting this value to
            **SyncType.MASTER** or  **SyncType.SLAVE** enables trigger
            skew correction. If you enable trigger skew correction, set
            this property to **SyncType.MASTER** on only one device, and
            set this property to **SyncType.SLAVE** on the other
            devices.
        

#### `def sync_type(self, val)`

#### `def sync_type(self)`

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/types.py -->
## PYTHON MODULE: generated/nidaqmx/types.py

### MODULE DOCSTRING

NI-DAQmx data types.

### `class IDPinContents(typing.NamedTuple)`

IDPinContents represent the contents of the memory connected to the ID pin.

<!--NI_PYTHON_API repo=nidaqmx-python path=generated/nidaqmx/utils.py -->
## PYTHON MODULE: generated/nidaqmx/utils.py

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

<!--NI_PYTHON_API repo=nidaqmx-python path=src/codegen/__init__.py -->
## PYTHON MODULE: src/codegen/__init__.py

### MODULE DOCSTRING

NI-DAQmx code generator.

<!--NI_PYTHON_API repo=nidaqmx-python path=src/codegen/__main__.py -->
## PYTHON MODULE: src/codegen/__main__.py

### MODULE DOCSTRING

DAQmx code generator.

### `def _get_logging_level(verbose, quiet)`

### `def main(dest, verbose, quiet)`

Starts the code generator based on the out folders.

<!--NI_PYTHON_API repo=nidaqmx-python path=src/codegen/functions/adaptor_parameter.py -->
## PYTHON MODULE: src/codegen/functions/adaptor_parameter.py

### MODULE DOCSTRING

Structure for storing adaptor parameter from scrapigen.

### `class AdaptorParameter()`

Structure for storing adaptor parameter from scrapigen.

#### `def __init__(self, adaptor_parameter)`

Structure for storing adaptor parameter from scrapigen.

#### `def adaptor(self)`

str: Defines the string that should be used when using the parameter.

#### `def data_type(self)`

str: Defines the data type of the parameter.

#### `def direction(self)`

str: Direction of the parameter.

#### `def description(self)`

str: The documentation of the parameter.

<!--NI_PYTHON_API repo=nidaqmx-python path=src/codegen/functions/function.py -->
## PYTHON MODULE: src/codegen/functions/function.py

### MODULE DOCSTRING

Structure for storing function metadata from scrapigen.

### `class Function()`

Structure for storing function metadata from scrapigen.

#### `def __init__(self, function_name, function_metadata)`

Structure for storing function metadata from scrapigen.

#### `def function_name(self)`

str: The name of the function.

#### `def c_function_name(self)`

str: The name of the c function to be called when using the function.

#### `def description(self)`

str: This is used to define the doc string of the function.

#### `def is_python_factory(self)`

bool: Defines if the function is considered to be a static.

#### `def python_class_name(self)`

str: The name of the python class this function belongs to.

#### `def calling_convention(self)`

str: The calling convention to be followed when using the c functions.

#### `def return_type(self)`

str: The data_type of the return value.

#### `def handle_parameter(self)`

Handle parameter: The handle parameter for the instance the function.

#### `def parameters(self)`

List of parameters: The list of parameters in the function.

#### `def output_parameters(self)`

List of output parameters: The list of output parameters in the function.

#### `def adaptor_parameter(self)`

List of adaptor parameters: The list of adaptor parameters in the function.

#### `def base_parameters(self)`

List of all parameters: The list of all in the function.

#### `def stream_response(self)`

bool: Defines if the function uses server streaming to send multiple responses.

#### `def python_codegen_method(self)`

str: The python codegen method of the function.

#### `def is_python_codegen_method(self)`

bool: Defines if the function is a python codegen function.

#### `def is_init_method(self)`

bool: Defines if the method is an init method.

#### `def attribute_function_type(self)`

bool: Defines type of attribute function.

<!--NI_PYTHON_API repo=nidaqmx-python path=src/codegen/functions/parameter.py -->
## PYTHON MODULE: src/codegen/functions/parameter.py

### MODULE DOCSTRING

Structure for storing function parameter metadata from scrapigen.

### `class Parameter()`

Structure for storing function parameter metadata from scrapigen.

#### `def __init__(self, parameter_metadata)`

Structure for storing function parameter metadata from scrapigen.

#### `def direction(self)`

str: Direction of the parameter.

#### `def type(self)`

str: Type of the parameter.

#### `def parameter_name(self)`

str: The name of the parameter.

#### `def description(self)`

str: The description of the parameter.

#### `def python_type_annotation(self)`

str: This is used to define the type annotation of the parameter.

#### `def enum(self)`

str: The name of the enum.

#### `def is_grpc_enum(self)`

bool: Defines if the parameter is grpc enum or not.

#### `def is_enum(self)`

bool: Defines if the parameter is enum or not.

#### `def is_list(self)`

bool: Defines if the parameter is a list or not.

#### `def has_explicit_buffer_size(self)`

bool: Specifies if an explicit buffer size has to be provided for the c function call.

#### `def ctypes_data_type(self)`

str: The type of the attribute as per the ctypes definition in python.

#### `def python_data_type(self)`

str: The python data_type of the attribute.

#### `def optional(self)`

str: This is used to differentiate the optional from required parameters.

#### `def default(self)`

str: The default value of the parameter.

#### `def has_default(self)`

bool: Defines if the parameter has a default value.

#### `def size(self)`

BufferSizeInfo: Defines the information on a parameter's size.

#### `def callback_params(self)`

Dict: Defines the params for callback functions.

#### `def is_compound_type(self)`

bool: Defines if the parameter is of compound type.

#### `def repeating_argument(self)`

bool: Defines if the parameter is a repeating type.

#### `def repeated_var_args(self)`

bool: Defines if the parameter is a repeated argument.

#### `def grpc_type(self)`

str: Returns the grpc type of the parameter.

#### `def is_used_in_python_api(self)`

bool: Defines if the parameter is used in python APIs.

#### `def is_proto_only(self)`

bool: Defines if the parameter is proto only.

#### `def is_pointer(self)`

bool: Defines if the parameter is a pointer or not.

#### `def include_in_proto(self)`

bool: Defines if the parameter is included in the proto definition.

<!--NI_PYTHON_API repo=nidaqmx-python path=src/codegen/generator.py -->
## PYTHON MODULE: src/codegen/generator.py

### MODULE DOCSTRING

Code generator for generating DAQmx functions.

### `def _get_metadata()`

### `def _get_template(template_file_name)`

Instantiate the mako template in the given file.

### `def _generate_file(metadata, template_file_name, output_path)`

### `def _copy_handwritten_files(dest)`

### `def generate(dest)`

Generates the DAQmx classes using scrapigen metadata.

<!--NI_PYTHON_API repo=nidaqmx-python path=src/codegen/metadata/__init__.py -->
## PYTHON MODULE: src/codegen/metadata/__init__.py

### `def update_functions()`

<!--NI_PYTHON_API repo=nidaqmx-python path=src/codegen/properties/attribute.py -->
## PYTHON MODULE: src/codegen/properties/attribute.py

### MODULE DOCSTRING

Structure for storing attribute metadata from scrapigen.

- `ALTERNATE_CONSTRUCTOR_CLASSES = ['Task', 'PhysicalChannel', 'Device', 'PersistedChannel', 'PersistedTask', 'PersistedScale', 'Scale']`

### `class Attribute()`

Structure for storing attribute metadata from scrapigen.

#### `def __init__(self, id, attribute_metadata)`

Structure for storing attribute metadata from scrapigen.

#### `def id(self)`

str: Represents a unique integer value that represents an attribute.

        This is the key for the attribute itself
        

#### `def access(self)`

str: Specifies if the attribute is read/write.

        This is used to decide the generation of getters and setters of a property representing
        the attribute. The possible values can be read, write or read-write.
        

#### `def name(self)`

str: Name of the attribute.

        This name is used to generate the property name.
        

#### `def resettable(self)`

bool: This attribute can be reset back to default.

        This is also used to decide if a deleter has to be generated for the property.
        

#### `def type(self)`

str: Data type of the attribute.

        Here `enum` types are always represented as integers.
        

#### `def object_module_location(self)`

str: if return type is an object, its corresponding location will be returned.

#### `def has_explicit_write_buffer_size(self)`

bool: Specifies if an explicit write buffer size has to be provided.

        If True then an additional uint parameter would be provided.
        

#### `def object_has_factory(self)`

bool: If attribute is of an object type, this specifies if it uses a factory method.

        If the value is `True` then the `_factory` method is used for instantiation of the object.
        

#### `def is_enum(self)`

bool: Represents if the attribute is an enum or not.

#### `def enum(self)`

str: The enum type the attribute represents.

        This key will only be available for an enum type attribute.
        During code generation an attribute would be considered as an enum if it contains this key.
        

#### `def handle_parameters(self)`

str: A list of parameters that represent handles that the attribute is part of.

        These are used when defining the c function parameters.
        

#### `def object_constructor_params(self)`

str: This contains the additional parameters to be included in the object creation.

        These parameters are added as inputs when creating the object.
        

#### `def python_class_name(self)`

str: The name of the python class this attribute belongs to.

        This is map the attribute to the class which it belongs to.
        

#### `def is_object(self)`

str: This is used to determine if the value has to be used as an object.

#### `def object_type(self)`

str: The name of the object.

        During code generation, this is used to instantiate the object.
        

#### `def c_function_name(self)`

str: The name of the c function to be called when using the attribute.

        This name will be prefixed with `DAQmxSet', `DAQmxGet` and `DAQmxReset`
        for using in getters, setters and deleters respectively.
        

#### `def calling_convention(self)`

str: The calling convention to be followed when using the c functions.

#### `def is_list(self)`

bool: Determines if the attribute is of type list or not.

#### `def bitfield_enum(self)`

str: The name of the bitfield enum that the attribute represents.

        During code generation in python, this will be used to decide if the `enum_to_bitfield_list`
        method needs to called in the getter when returning the value.
        

#### `def has_explicit_read_buffer_size(self)`

bool: Specifies if an explicit read buffer size has to be provided for the attribute.

        If True then an additional uint parameter would be provided when calling the
        c function to mention the buffer size.
        

#### `def read_buffer_size(self)`

str: The read buffer size to be used when calling the c function.

        This key would only be applicable if `has_explicit_read_buffer_size` is `True`.
        In case the `has_explicit_read_buffer_size` is `True` and this key is not present,
        then the ivi dance method is used to get the buffer size.
        

#### `def python_description(self)`

str: The description of the attribute.

        This will be used to define the docstring of the attribute when generating the code.
        

#### `def python_data_type(self)`

str: The python data_type of the attribute.

        Currently this is used in the generation of the doc string for the attribute.
        

#### `def ctypes_data_type(self)`

str: The type of the attribute as per the ctypes definition in python.

        This is used to provide the type of the attribute when making c function calls in python.
        

#### `def has_alternate_constructor(self)`

bool: Specifies if an alternate constructor is present for the attribute.

#### `def get_lib_importer_type(self)`

Returns the type of c function call.

#### `def get_argument_types(self)`

Returns a list of argument parameter types.

#### `def get_handle_parameter_arguments(self)`

Returns the list of handle parameters for the attribute.

#### `def get_return_type(self)`

Gets the return type of attributes to be used in description.

#### `def update_attribute_name(self, attribute_name)`

Updates the attribute name.

<!--NI_PYTHON_API repo=nidaqmx-python path=src/codegen/properties/parameter.py -->
## PYTHON MODULE: src/codegen/properties/parameter.py

### MODULE DOCSTRING

Structure for storing parameter metadata from scrapigen.

### `class Parameter()`

Structure for storing parameter metadata from scrapigen.

#### `def __init__(self, name, parameter_metadata)`

Structure for storing parameter metadata from scrapigen.

#### `def handle_name(self)`

str: The key of the parameter.

#### `def accessor(self)`

str: Defines how to access the handle parameter.

        This value would be directly substituted when trying to use the handle parameter
        

#### `def ctypes_data_type(self)`

str: Defines the ctypes data_type of the handle parameter.

        This is used when mentioning the data_type of the handle parameter.
        

#### `def cvi_name(self)`

str: The cvi name of the parameter.

        This is kept for the gRPC client implementation.
        

<!--NI_PYTHON_API repo=nidaqmx-python path=src/codegen/stub_generator.py -->
## PYTHON MODULE: src/codegen/stub_generator.py

### MODULE DOCSTRING

Generates gRPC Python stubs from proto files.

- `STUBS_NAMESPACE = 'nidaqmx._stubs'`

- `PROTO_PARENT_NAMESPACES = ['src.codegen', 'protos']`

- `STUBS_PATH = pathlib.Path(__file__).parent.parent.parent / 'generated' / STUBS_NAMESPACE.replace('.', '/')`

- `PROTO_PATH = pathlib.Path(__file__).parent.parent.parent / 'src' / 'codegen' / 'protos'`

- `NI_APIS_PATH = pathlib.Path(__file__).parent.parent.parent / 'third_party' / 'ni-apis'`

- `PROTO_FILES = list(PROTO_PATH.rglob('*.proto'))`

### `def generate_stubs()`

Generate and fixup gRPC Python stubs.

### `def is_relative_to(path: pathlib.PurePath, other: pathlib.PurePath) -> bool`

Return whether or not this path is relative to the other path.

### `def generate_python_files(stubs_path: pathlib.Path, proto_path: pathlib.Path, proto_files: Sequence[pathlib.Path])`

Generate python files from .proto files with protoc.

### `def fix_import_paths(stubs_path: pathlib.Path, stubs_namespace: str, proto_parent_namespaces: Sequence[str])`

Fix import paths of generated files.

### `def add_init_files(stubs_path: pathlib.Path, proto_path: pathlib.Path)`

Add __init__.py files to generated file directories.

<!--NI_PYTHON_API repo=nidaqmx-python path=src/codegen/utilities/__init__.py -->
## PYTHON MODULE: src/codegen/utilities/__init__.py

### MODULE DOCSTRING

This module contains the helpers for code generator.

<!--NI_PYTHON_API repo=nidaqmx-python path=src/codegen/utilities/attribute_helpers.py -->
## PYTHON MODULE: src/codegen/utilities/attribute_helpers.py

### MODULE DOCSTRING

This contains the helper methods used in attribute generation.

- `EXCLUDED_ATTRIBUTES = ['AI_CHAN_CAL_HAS_VALID_CAL_INFO', 'AI_CHAN_CAL_ENABLE_CAL', 'AI_CHAN_CAL_DESC', 'AI_CHAN_CAL_APPLY_CAL_IF_EXP', 'AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_B_SRC', 'AI_CHAN_CAL_VERIF_REF_VALS', 'AI_CHAN_CAL_VERIF_ACQ_VALS', 'AI_CHAN_CAL_TABLE_SCALED_VALS', 'AI_CHAN_CAL_TABLE_PRE_SCALED_VALS', 'AI_CHAN_CAL_SCALE_TYPE', 'AI_CHAN_CAL_POLY_REVERSE_COEFF', 'AI_CHAN_CAL_POLY_FORWARD_COEFF', 'AI_CHAN_CAL_OPERATOR_NAME', 'AI_PHYSICAL_CHANS', 'AO_PHYSICAL_CHANS', 'DI_LINES', 'DI_PORTS', 'DO_PORTS', 'DO_LINES', 'CI_PHYSICAL_CHANS', 'CO_PHYSICAL_CHANS', 'TIMING_SYNC_PULSE_FORCE', 'ID_PIN_MEM_SERIAL_NUMS']`

- `DEPRECATED_ATTRIBUTES = {'ai_rtd_r_0': {'new_name': 'ai_rtd_r0', 'deprecated_in': '0.7.0'}, 'ai_sound_pressured_b_ref': {'new_name': 'ai_sound_pressure_db_ref', 'deprecated_in': '0.7.0'}, 'ai_thrmstr_r_1': {'new_name': 'ai_thrmstr_r1', 'deprecated_in': '0.7.0'}, 'ai_acceld_b_ref': {'new_name': 'ai_accel_db_ref', 'deprecated_in': '0.7.0'}, 'ai_voltaged_b_ref': {'new_name': 'ai_voltage_db_ref', 'deprecated_in': '0.7.0'}, 'ai_velocity_iepe_sensord_b_ref': {'new_name': 'ai_velocity_iepe_sensor_db_ref', 'deprecated_in': '0.7.0'}, 'over_write': {'new_name': 'overwrite', 'deprecated_in': '0.7.0'}, 'dev_is_simulated': {'new_name': 'is_simulated', 'deprecated_in': '0.7.0'}, 'dev_serial_num': {'new_name': 'serial_num', 'deprecated_in': '0.7.0'}, 'tedshwteds_supported': {'new_name': 'hwteds_supported', 'deprecated_in': '0.7.0'}, 'expir_states_ao_type': {'new_name': 'ao_output_type', 'deprecated_in': '0.7.0'}, 'expir_states_co_state': {'new_name': 'co_state', 'deprecated_in': '0.7.0'}, 'expir_states_do_state': {'new_name': 'do_state', 'deprecated_in': '0.7.0'}, 'expir_states_ao_state': {'new_name': 'ao_state', 'deprecated_in': '0.7.0'}}`

- `PYTHON_CLASS_ENUM_MERGE_SET = {'Channel': ['_Save'], 'InStream': ['AcquisitionType', 'READ_ALL_AVAILABLE'], 'OutStream': ['ResolutionType'], 'Scale': ['_Save'], 'Watchdog': ['WDTTaskAction']}`

- `ATTRIBUTE_CHANGE_SET = {'AIChannel': {'ai_custom_scale_name': 'ai_custom_scale', 'ai_strain_gage_force_read_from_chan': 'ai_strain_force_read_from_chan', 'ai_eddy_current_prox_probe_sensitivity': 'ai_eddy_current_prox_sensitivity', 'ai_eddy_current_prox_probe_sensitivity_units': 'ai_eddy_current_prox_sensitivity_units', 'ai_eddy_current_prox_probe_units': 'ai_eddy_current_prox_units', 'ai_is_teds': 'ai_teds_is_teds', 'ai_rosette_strain_gage_orientation': 'ai_rosette_strain_gage_gage_orientation'}, 'AOChannel': {'ao_custom_scale_name': 'ao_custom_scale'}, 'CIChannel': {'ci_count_edges_count_reset_reset_count': 'ci_count_edges_count_reset_reset_cnt', 'ci_custom_scale_name': 'ci_custom_scale', 'ci_dup_count_prevent': 'ci_dup_count_prevention', 'ci_pulse_freq_start_edge': 'ci_pulse_freq_starting_edge', 'ci_pulse_ticks_start_edge': 'ci_pulse_ticks_starting_edge', 'ci_pulse_time_start_edge': 'ci_pulse_time_starting_edge', 'ci_velocity_encoder_a_input_dig_fltr_enable': 'ci_velocity_a_input_dig_fltr_enable', 'ci_velocity_encoder_a_input_dig_fltr_min_pulse_width': 'ci_velocity_a_input_dig_fltr_min_pulse_width', 'ci_velocity_encoder_a_input_dig_fltr_timebase_rate': 'ci_velocity_a_input_dig_fltr_timebase_rate', 'ci_velocity_encoder_a_input_dig_fltr_timebase_src': 'ci_velocity_a_input_dig_fltr_timebase_src', 'ci_velocity_encoder_a_input_logic_lvl_behavior': 'ci_velocity_a_input_logic_lvl_behavior', 'ci_velocity_encoder_a_input_term': 'ci_velocity_a_input_term', 'ci_velocity_encoder_a_input_term_cfg': 'ci_velocity_a_input_term_cfg', 'ci_velocity_encoder_b_input_dig_fltr_enable': 'ci_velocity_b_input_dig_fltr_enable', 'ci_velocity_encoder_b_input_dig_fltr_min_pulse_width': 'ci_velocity_b_input_dig_fltr_min_pulse_width', 'ci_velocity_encoder_b_input_dig_fltr_timebase_rate': 'ci_velocity_b_input_dig_fltr_timebase_rate', 'ci_velocity_encoder_b_input_dig_fltr_timebase_src': 'ci_velocity_b_input_dig_fltr_timebase_src', 'ci_velocity_encoder_b_input_logic_lvl_behavior': 'ci_velocity_b_input_logic_lvl_behavior', 'ci_velocity_encoder_b_input_term': 'ci_velocity_b_input_term', 'ci_velocity_encoder_b_input_term_cfg': 'ci_velocity_b_input_term_cfg'}, 'Channel': {'chan_descr': 'description', 'chan_sync_unlock_behavior': 'sync_unlock_behavior', 'chan_is_global': 'is_global', 'physical_chan_name': 'physical_channel'}, 'InStream': {'change_detect_has_overflowed': 'change_detect_overflowed', 'digital_lines_bytes_per_chan': 'di_num_booleans_per_chan'}, 'OutStream': {'digital_lines_bytes_per_chan': 'do_num_booleans_per_chan'}, 'Timing': {'on_demand_simultaneous_ao_enable': 'simultaneous_ao_enable'}, 'Scale': {'type': 'scale_type', 'descr': 'description'}, 'ExportSignals': {'on_demand_simultaneous_ao_enable': 'simultaneous_ao_enable', '10_mhz_ref_clk_output_term': 'exported_10_mhz_ref_clk_output_term', '20_mhz_timebase_output_term': 'exported_20_mhz_timebase_output_term'}, 'ArmStartTrigger': {'timescale': 'time_timescale'}, 'StartTrigger': {'timescale': 'time_timescale'}, 'Device': {'teds_hwteds_supported': 'hwteds_supported', 'chassis_module_dev_names': 'chassis_module_devices', 'compact_daq_chassis_dev_name': 'compact_daq_chassis_device', 'compact_rio_chassis_dev_name': 'compact_rio_chassis_device', 'field_daq_bank_dev_names': 'field_daq_bank_devices', 'field_daq_dev_name': 'field_daq_device', 'ai_supported_meas_types': 'ai_meas_types', 'ao_supported_output_types': 'ao_output_types', 'ci_supported_meas_types': 'ci_meas_types', 'co_supported_output_types': 'co_output_types'}, 'PhysicalChannel': {'teds_template_i_ds': 'teds_template_ids', 'ai_supported_meas_types': 'ai_meas_types', 'ao_supported_output_types': 'ao_output_types', 'ci_supported_meas_types': 'ci_meas_types', 'co_supported_output_types': 'co_output_types'}, 'ExpirationState': {'ao_expir_state': 'ao_state', 'co_expir_state': 'co_state', 'do_expir_state': 'do_state'}, 'Watchdog': {'expir_trig_type': 'expir_trig_trig_type', 'has_expired': 'expired', 'dig_edge_watchdog_expir_trig_edge': 'expir_trig_dig_edge_edge', 'dig_edge_watchdog_expir_trig_src': 'expir_trig_dig_edge_src'}, 'Triggers': {'trigger_sync_type': 'sync_type'}}`

- `ATTR_NAME_CHANGE_IN_DESCRIPTION = {'anlg_lvl_pause_trig_when': 'anlg_lvl_when', 'anlg_lvl_pause_trig_lvl': 'anlg_lvl_lvl', 'anlg_win_pause_trig_btm': 'anlg_win_btm', 'anlg_win_pause_trig_top': 'anlg_win_top', 'dig_pattern_pause_trig_src': 'dig_pattern_src', 'dig_pattern_pause_trig_pattern': 'dig_pattern_pattern', 'anlg_edge_ref_trig_slope': 'anlg_edge_slope', 'anlg_edge_ref_trig_slope': 'anlg_edge_slope', 'anlg_edge_ref_trig_lvl': 'anlg_edge_lvl', 'anlg_win_ref_trig_btm': 'anlg_win_btm', 'anlg_win_ref_trig_top': 'anlg_win_top', 'ref_trig_auto_trig_enable': 'auto_trig_enable', 'dig_pattern_ref_trig_src': 'dig_pattern_src', 'dig_pattern_ref_trig_pattern': 'dig_pattern_pattern', 'anlg_edge_start_trig_slope': 'anlg_edge_slope', 'anlg_edge_start_trig_lvl': 'anlg_edge_lvl', 'anlg_win_start_trig_btm': 'anlg_win_btm', 'anlg_win_start_trig_top': 'anlg_win_top', 'start_trig_delay_units': 'delay_units', 'start_trig_delay': 'delay', 'dig_pattern_start_trig_src': 'dig_pattern_src', 'dig_pattern_start_trig_pattern': 'dig_pattern_pattern', 'physical_chan_ai_supported_meas_types': 'ai_supported_meas_types', 'physical_chan_ao_supported_output_types': 'ao_supported_output_types', 'physical_chan_ci_supported_meas_types': 'ci_supported_meas_types', 'physical_chan_co_supported_output_types': 'co_supported_output_types', 'physical_chan_teds_bit_stream': 'teds_bit_stream', 'ai_eddy_current_prox_probe_sensitivity': 'ai_eddy_current_prox_sensitivity', 'ai_eddy_current_prox_probe_sensitivity_units': 'ai_eddy_current_prox_sensitivity_units', 'ci_dup_count_prevent': 'ci_dup_count_prevention', 'ai_supported_meas_types': 'ai_meas_types', 'ao_supported_output_types': 'ao_output_types', 'ci_supported_meas_types': 'ci_meas_types', 'co_supported_output_types': 'co_output_types'}`

- `GENERIC_ATTRIBUTE_TYPE_MAP = {'bool32': 'bool', 'char[]': 'string', 'float64': 'double', 'uInt32': 'uint32', 'uInt64': 'uint64', 'float64[]': 'double_array', 'int32[]': 'int32_array', 'uInt8[]': 'bytes', 'uInt32[]': 'uint32_array', 'CVIAbsoluteTime': 'timestamp'}`

- `GENERIC_ATTRIBUTE_GROUP_NAME_MAP = {'CalibrationInfo': 'cal_info', 'Channel': 'chan', 'ExportSignal': 'exported_signal', 'System': 'system_info', 'Trigger': 'trig', 'PhysicalChannel': 'physical_chan'}`

- `ATTRIBUTE_WITH_FILE_PATH_TYPE = ('logging_file_path',)`

### `def get_attributes(metadata, class_name)`

Converts the scrapigen metadata into a list of attributes.

### `def get_enums_used(attributes)`

Gets the list of enums used in the attribute metadata.

### `def get_deprecated_attributes(attributes)`

Gets the list of attributes to be deprecated.

### `def get_generic_attribute_function_name(attribute)`

Gets the attribute independent interpreter function name.

### `def get_generic_attribute_function_type(attribute)`

Gets the attribute independent interpreter function type.

### `def has_attribute_with_filter(attribute, group_name, filter_name)`

Checks if the given attribute in the group has the specified filter name in its lv_filter.

<!--NI_PYTHON_API repo=nidaqmx-python path=src/codegen/utilities/enum_helpers.py -->
## PYTHON MODULE: src/codegen/utilities/enum_helpers.py

### MODULE DOCSTRING

Helper functions for generating constants.py.

- `ENUM_MERGE_SET = {'AccelSensitivityUnits': ['AccelSensitivityUnits1', 'AccelSensitivityUnits'], 'AccelUnits': ['AccelUnits', 'AccelUnits2'], 'AngleUnits': ['AngleUnits', 'AngleUnits1', 'AngleUnits2'], 'AutoZeroType': ['AutoZeroType', 'AutoZeroType1'], 'BridgeConfiguration': ['BridgeConfiguration', 'BridgeConfiguration1'], 'CJCSource': ['CJCSource1', 'CJCSource'], 'Coupling': ['Coupling1', 'Coupling2', 'Coupling'], 'CurrentShuntResistorLocation': ['CurrentShuntResistorLocation', 'CurrentShuntResistorLocation1'], 'CurrentUnits': ['CurrentUnits1', 'CurrentUnits'], 'DataJustification': ['DataJustification', 'DataJustification1'], 'DigitalWidthUnits': ['DigitalWidthUnits', 'DigitalWidthUnits1', 'DigitalWidthUnits2', 'DigitalWidthUnits3', 'DigitalWidthUnits4'], 'Edge': ['Edge', 'Edge1'], 'FilterResponse': ['FilterResponse1', 'FilterResponse'], 'FilterType': ['FilterType', 'FilterType2'], 'LVDTSensitivityUnits': ['LVDTSensitivityUnits1', 'LVDTSensitivityUnits'], 'LengthUnits': ['LengthUnits', 'LengthUnits2', 'LengthUnits3'], 'MIOAIConvertTimebaseSource': ['MIOAIConvertTimebaseSource', 'MIOAIConvertTbSrc'], 'RTDType': ['RTDType', 'RTDType1'], 'RVDTSensitivityUnits': ['RVDTSensitivityUnits', 'RVDTSensitivityUnits1'], 'ResistanceUnits': ['ResistanceUnits', 'ResistanceUnits1'], 'ResolutionType': ['ResolutionType1', 'ResolutionType'], 'ScaleType': ['ScaleType2', 'ScaleType4', 'ScaleType'], 'SoundPressureUnits': ['SoundPressureUnits', 'SoundPressureUnits1'], 'StrainGageBridgeType': ['StrainGageBridgeType', 'StrainGageBridgeType1'], 'StrainUnits': ['StrainUnits', 'StrainUnits1'], 'TemperatureUnits': ['TemperatureUnits', 'TemperatureUnits1'], 'ThermocoupleType': ['ThermocoupleType', 'ThermocoupleType1'], 'Timescale': ['Timescale', 'Timescale2'], 'VoltageUnits': ['VoltageUnits', 'VoltageUnits1', 'VoltageUnits2'], 'UsageTypeAI': ['UsageTypeAI', 'AIMeasurementType'], 'UsageTypeAO': ['AOOutputChannelType'], 'UsageTypeCI': ['CIMeasurementType'], 'DataTransferActiveTransferMode': ['DataTransferMechanism', 'DataTransferActiveTransferMode'], 'TerminalConfiguration': ['TerminalConfiguration', 'InputTermCfg', 'OutputTermCfg', 'InputTermCfg2'], 'CountDirection': ['CountDirection1'], 'FrequencyUnits': ['FrequencyUnits2', 'FrequencyUnits3'], 'TimeUnits': ['TimeUnits2', 'TimeUnits3'], 'EncoderType': ['EncoderType2'], 'GpsSignalType': ['GpsSignalType1'], 'EncoderZIndexPhase': ['EncoderZIndexPhase1'], 'Level': ['Level1', 'DigitalLineState'], 'UsageTypeCO': ['COOutputType'], 'ActiveOrInactiveEdgeSelection': ['SampleClockActiveOrInactiveEdgeSelection'], 'OverwriteMode': ['OverwriteMode', 'OverwriteMode1'], 'RegenerationMode': ['RegenerationMode', 'RegenerationMode1'], 'WaitMode': ['WaitMode', 'WaitMode2'], 'ExportAction': ['ExportActions', 'ExportActions2', 'ExportActions3', 'ExportActions5'], 'Polarity': ['Polarity', 'Polarity2'], 'TriggerType': ['TriggerType4', 'TriggerType6', 'TriggerType8', 'TriggerType9', 'TriggerType10'], 'DigitalPatternCondition': ['DigitalPatternCondition1'], 'Slope': ['Slope1']}`

- `ENUMS_BLACKLIST = ['AltRef', 'AntStatus', 'DAQmxErrors', 'DAQmxWarnings', 'ExportActions', 'GroupBy', 'ForceIEPEUnits', 'FilterType1', 'LengthUnits4', 'NavMeasurementType', 'NavMode', 'SaveOptions', 'TaskControlAction', 'Timescale', 'WatchdogAOOutputType', 'WatchdogControlAction', 'VelocityUnits2']`

- `NAME_SUBSTITUTIONS = {'100_MHZ_TIMEBASE': 'ONE_HUNDRED_MHZ_TIMEBASE', '20_MHZ_TIMEBASE': 'TWENTY_MHZ_TIMEBASE', '2_POINT_5_V': 'TWO_POINT_FIVE_V', '2_WIRE': 'TWO_WIRE', '3_POINT_3_V': 'THREE_POINT_THREE_V', '3_WIRE': 'THREE_WIRE', '4_WIRE': 'FOUR_WIRE', '5_V': 'FIVE_V', '5_WIRE': 'FIVE_WIRE', '6_WIRE': 'SIX_WIRE', '80_MHZ_TIMEBASE': 'EIGHTY_MHZ_TIMEBASE', '8_MHZ_TIMEBASE': 'EIGHT_MHZ_TIMEBASE', 'US_BBULK': 'USB_BULK', '10_MHZ_REF_CLOCK': 'TEN_MHZ_REF_CLOCK', '20_MHZ_TIMEBASE_CLOCK': 'TWENTY_MHZ_TIMEBASE_CLOCK', '50_OHMS': 'FIFTY_OHMS', '75_OHMS': 'SEVENTY_FIVE_OHMS', '1_M_OHM': 'ONE_M_OHM', '10_G_OHMS': 'TEN_G_OHMS', 'GROUND': 'GND'}`

- `BITFIELD_ENUMS = ['CouplingTypes', 'Callback', 'TriggerUsageTypes', 'Save', 'TermCfg']`

### `def merge_enums(enum_name)`

Replaces the scrapigen enum name with the actual name.

### `def _merge_enum_values(value_lists)`

### `def _merge_enum_variants(enums)`

### `def _sanitize_values(enums)`

### `def get_enums(metadata)`

Formats and removes Blacklisted enums.

### `def get_enum_value_docstring(raw_docstring)`

Formats enum docstrings.

### `def _cleanup_docstring(docstring)`

<!--NI_PYTHON_API repo=nidaqmx-python path=src/codegen/utilities/function_helpers.py -->
## PYTHON MODULE: src/codegen/utilities/function_helpers.py

### MODULE DOCSTRING

This contains the helper methods used in functions generation.

- `FUNCTION_NAME_CHANGE_SET = {'TEDSAIRTD': 'TEDS_AI_RTD', 'TEDSAI': 'TEDS_AI', 'AIRTD': 'AI_RTD', 'CIGPS': 'CI_GPS'}`

- `EXCLUDED_FUNCTIONS = ['AddNetworkDevice', 'DeleteNetworkDevice', 'ReserveNetworkDevice', 'UnreserveNetworkDevice', 'AddCDAQSyncConnection', 'AreConfiguredCDAQSyncPortsDisconnected', 'AutoConfigureCDAQSyncConnections', 'GetAnalogPowerUpStates', 'GetAnalogPowerUpStatesWithOutputType', 'GetAutoConfiguredCDAQSyncConnections', 'GetDigitalLogicFamilyPowerUpState', 'GetDigitalPowerUpStates', 'GetDigitalPullUpPullDownStates', 'GetDisconnectedCDAQSyncPorts', 'RemoveCDAQSyncConnection', 'SetAnalogPowerUpStates', 'SetAnalogPowerUpStatesWithOutputType', 'SetDigitalLogicFamilyPowerUpState', 'SetDigitalPowerUpStates', 'SetDigitalPullUpPullDownStates']`

- `FUNCTIONS_WITH_LIST_DEFAULT = ['add_ai_force_bridge_polynomial_chan', 'add_ai_force_bridge_table_chan', 'add_ai_pressure_bridge_polynomial_chan', 'add_ai_pressure_bridge_table_chan', 'add_ai_torque_bridge_polynomial_chan', 'add_ai_torque_bridge_table_chan']`

### `def get_functions(metadata, class_name='')`

Converts the scrapigen metadata into a list of functions.

### `def get_function_name(function_name: str)`

Performs naming substitutions and converts function name from camel to snake case.

### `def get_enums_used(functions)`

Gets the list of enums used in the functions metadata.

### `def order_function_parameters_by_optional(function_parameters)`

Sorts optional parameters and non optional parameters for function definition.

### `def get_parameter_signature(is_python_factory, sorted_params)`

Gets parameter signature for function definition.

### `def get_parameters_docstring_lines_length(input_param)`

Gets First line and length of parameter docstring.

### `def get_instantiation_lines(function_parameters)`

Gets the instantiation lines of parameters docstrings.

### `def get_arguments_type(functions_metadata)`

Gets the 'type' of parameters.

### `def to_param_argtype(parameter)`

Formats argument types.

### `def get_explicit_output_param(output_parameters)`

Gets the explicit output parameters.

### `def generate_function_call_args(function_metadata)`

Gets function call arguments.

### `def instantiate_explicit_output_param(param)`

Gets instantiate lines for output parameters.

### `def get_list_default_value(func, param)`

Gets the default value for list parameters.

### `def is_path_type(input_param)`

Check is the parameter a file path.

<!--NI_PYTHON_API repo=nidaqmx-python path=src/codegen/utilities/helpers.py -->
## PYTHON MODULE: src/codegen/utilities/helpers.py

### MODULE DOCSTRING

Helpers class to generate helper functions for the metadata.

- `CAMEL_TO_SNAKE_CASE_REGEXES = [re.compile('([^_\n])([A-Z][a-z]+)'), re.compile('([a-z])([A-Z])'), re.compile('([0-9])([^_0-9])'), re.compile('([^_0-9])([0-9])')]`

- `SPECIAL_CASE_PASCAL_TOKENS = [PascalTokenSubstitution('Uint', 'UInt'), PascalTokenSubstitution('Id', 'ID')]`

- `NAME_CHANGE_SET = {'cdaq': 'CDAQ', 'ao': 'AO', 'ai': 'AI', 'co': 'CO', 'do': 'DO', 'teds': 'TEDS', 'iepe': 'IEPE', 'rms': 'RMS', 'dc': 'DC', 'lvdt': 'LVDT', 'rvdt': 'RVDT', 'airtd': 'AIRTD', 'ci': 'CI', 'di': 'DI', 'cigps': 'CIGPS', 'tedsai': 'TEDSAI', 'tedsairtd': 'TEDSAIRTD'}`

### `def camel_to_snake_case(camel_case_string, regexes=CAMEL_TO_SNAKE_CASE_REGEXES)`

Converts a camelCase string to a snake_case string.

### `def get_enums_to_import(enums_in_attributes, enums_in_functions)`

Gets the enums that needs to imported for the attributes and functions used.

### `def strip_class_name(name: str, class_name: str, replace_with='')`

Strips class name from name.

### `def snake_to_pascal(snake_string)`

Return a PascalString for a given snake_string.

### `def removeprefix(input, prefix)`

Returns the input string with the prefix string removed.

    If the given prefix string is not present in the input string,
    then the input string is directly returned.
    

### `def _insert_special_case_pascal_tokens(normal_pascal_string: str) -> str`

### `def _modify_function_name(snake_string)`

### `class AttributeFunctionType(Enum)`

Enum specifies whether the function is get/set/reset/not an attribute function.

### `def get_attribute_function_type(function_name: str)`

Sets attribute function type as get/set/reset or not a attribute function.

<!--NI_PYTHON_API repo=nidaqmx-python path=src/codegen/utilities/interpreter_helpers.py -->
## PYTHON MODULE: src/codegen/utilities/interpreter_helpers.py

### MODULE DOCSTRING

This contains the helper methods used in interpreter generation.

- `INTERPRETER_CAMEL_TO_SNAKE_CASE_REGEXES = [re.compile('([^_\n])([A-Z][a-z]+)'), re.compile('([a-z])([A-Z])'), re.compile('([0-9])([^_0-9])')]`

- `INTERPRETER_IGNORED_FUNCTIONS = ['GetExtendedErrorInfo', 'CfgInputBuffer', 'CfgOutputBuffer', 'GetNthTaskChannel', 'GetNthTaskDevice', 'GetNthTaskReadChannel', 'CreateWatchdogTimerTask', 'GetAIChanCalCalDate', 'GetAIChanCalExpDate', 'SetAIChanCalCalDate', 'SetAIChanCalExpDate', 'GetRealTimeAttributeBool', 'GetRealTimeAttributeInt32', 'GetRealTimeAttributeUInt32', 'ResetRealTimeAttribute', 'SetRealTimeAttributeBool', 'SetRealTimeAttributeInt32', 'SetRealTimeAttributeUInt32', 'WaitForNextSampleClock', 'GetArmStartTrigTimestampVal', 'GetArmStartTrigTrigWhen', 'GetFirstSampClkWhen', 'GetFirstSampTimestampVal', 'GetRefTrigTimestampVal', 'GetStartTrigTimestampVal', 'GetStartTrigTrigWhen', 'GetSyncPulseTimeWhen', 'GetTimingAttributeExTimestamp', 'SetArmStartTrigTrigWhen', 'SetFirstSampClkWhen', 'SetStartTrigTrigWhen', 'SetSyncPulseTimeWhen', 'SetTimingAttributeExTimestamp', 'SetTimingAttributeTimestamp', 'GetAnalogPowerUpStates']`

- `GRPC_INTERPRETER_IGNORED_FUNCTIONS = ['get_error_string', 'read_id_pin_memory', 'set_runtime_environment', 'internal_get_last_created_chan']`

- `LIBRARY_INTERPRETER_IGNORED_FUNCTIONS = ['get_error_string', 'read_id_pin_memory', 'read_power_binary_i16', 'read_power_f64', 'read_raw', 'write_raw']`

- `INCLUDE_SIZE_PARAMETER_IN_SIGNATURE_FUNCTIONS = ['get_analog_power_up_states_with_output_type']`

- `INCLUDE_SIZE_HINT_FUNCTIONS = ['get_read_attribute_string', 'get_write_attribute_string']`

- `MODIFIED_INTERPRETER_PARAMS = {'r_0': 'r0', 'r_1': 'r1'}`

- `EVENT_UNREGISTER_IGNORED_PARAMS = ['callback_data', 'callback_function', 'n_samples', 'options']`

- `READ_SAMPLES_PARAMETER_NAMES = ['samps_read', 'samps_per_chan_read', 'num_samps_per_chan']`

### `def get_interpreter_functions(metadata)`

Converts the scrapigen metadata into a list of functions.

### `def generate_interpreter_function_call_args(function_metadata)`

Gets function call arguments.

### `def get_argument_types(functions_metadata)`

Gets the 'type' of parameters.

### `def get_interpreter_parameter_signature(is_python_factory, params)`

Gets parameter signature for function definition.

### `def get_instantiation_lines_for_output(func)`

Gets the lines of code for instantiation of output values.

### `def get_instantiation_lines_for_varargs(func)`

Gets instantiation lines for functions with variable arguments.

### `def get_argument_definition_lines_for_varargs(varargs_params)`

Gets the lines for defining the variable arguments for a function.

### `def get_varargs_parameters(func)`

Gets variable arguments of a function.

### `def get_params_for_function_signature(func, is_grpc_interpreter=False)`

Gets interpreter parameters for the function signature.

### `def get_grpc_interpreter_call_params(func, params)`

Gets the interpreter parameters for grpc request.

### `def get_output_param_with_ivi_dance_mechanism(func)`

Gets the output parameters with explicit buffer size.

### `def has_parameter_with_ivi_dance_size_mechanism(func)`

Returns true if the function has a parameter with ivi dance size mechanism.

### `def is_custom_read_write_function(func)`

Returns True if the function is a read or write function.

### `def is_custom_read_function(func)`

Returns True if the function is a read function.

### `def is_custom_write_function(func)`

Returns True if the function is a write function.

### `def get_interpreter_output_params(func)`

Gets the output parameters for the functions in interpreter.

### `def get_output_params(func)`

Gets output parameters for the function.

### `def get_interpreter_in_out_params(func)`

Gets the input parameters that are also pointers for the function.

### `def get_return_values(func)`

Gets the values to add to return statement of the function.

### `def get_c_function_call_template(func)`

Gets the template to use for generating the logic of calling the c functions.

### `def get_grpc_function_call_template(func)`

Gets the template to use for generating the logic of calling the grpc functions.

### `def get_callback_func_param(func)`

Gets the callback_function parameter.

### `def get_callback_data_param(func)`

Gets the callback_data parameter.

### `def get_callback_function_call_args(func)`

Gets the parameters used in the callback function call.

### `def get_callback_param_data_types(func)`

Gets the data types for call back function parameters.

### `def is_event_function(func)`

Returns True if this is an event register/unregister function, False otherwise.

### `def is_event_register_function(func)`

Returns True if this is an event register function, False otherwise.

### `def is_event_unregister_function(func)`

Returns True if this is an event unregister function, False otherwise.

### `def get_event_name(func)`

Gets the event name for an event register/unregister function.

### `def get_compound_parameter(params)`

Returns the compound parameter associated with the given function.

### `def get_input_arguments_for_compound_params(func)`

Returns a list of input parameter for creating the compound parameter.

### `def create_compound_parameter_request(func)`

Gets the input parameters for creating the compound type parameter.

### `def get_response_parameters(func)`

Gets the list of parameters in grpc response.

### `def get_samps_per_chan_read_or_write_param(func_params)`

Gets samps per read/ samps per write parameter.

### `def get_samps_per_chan_read_param(func)`

Gets samps per read parameter.

### `def get_interpreter_parameters(func, is_grpc_interpreter=False)`

Gets the parameters used in the interpreter functions.

### `def _get_size_params(function_parameters)`

### `def _is_handle_parameter(func, param)`

### `def check_if_parameters_contain_read_array(params)`

Checks if the list of parameters contains read array parameter.

### `def get_read_array_parameters(func)`

Gets the list of array parameters.

### `def type_cast_attribute_set_function_parameter(param)`

Type casting of attribute set parameter during c call.

### `def is_numpy_array_datatype(param)`

Checks if datatype is a numpy array or not.

### `def is_read_bytes_param(param)`

Returns true if parameter reads bytes.

### `def is_write_bytes_param(param)`

Returns true if parameter writes bytes.

### `def get_numpy_array_params(func)`

Returns a dictionary of numpy data type parameters.

### `def get_write_array_param(param)`

Assigns the numpy array to a flattened numpy array.

<!--NI_PYTHON_API repo=nidaqmx-python path=src/codegen/utilities/text_wrappers.py -->
## PYTHON MODULE: src/codegen/utilities/text_wrappers.py

### MODULE DOCSTRING

This contains the helpers methods for wrapping texts.

### `def wrap(initial_indent, subsequent_indent=None)`

Returns custom Mako filter function that wraps code text.

    Returning another function from within this function is a trick used to
    enable Mako filter functions to accept arguments.
    

### `def docstring_wrap(initial_indent, subsequent_indent=None)`

Returns custom Mako filter function that wraps docstring text.

    Returning another function from within this function is a trick used to
    enable Mako filter functions to accept arguments.
    

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/__init__.py -->
## PYTHON MODULE: src/handwritten/__init__.py

### MODULE DOCSTRING

The NI-DAQmx API for Python.

- `__all__ = ['errors', 'scale', 'stream_readers', 'stream_writers', 'task']`

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/__main__.py -->
## PYTHON MODULE: src/handwritten/__main__.py

### MODULE DOCSTRING

'nidaqmx' command line utility.

### `def main(verbosity: int) -> None`

### `def installdriver()`

### `def _configure_logging(verbosity: int) -> None`

Configure logging for this process.

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/_bitfield_utils.py -->
## PYTHON MODULE: src/handwritten/_bitfield_utils.py

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
    

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/_dotenv_path.py -->
## PYTHON MODULE: src/handwritten/_dotenv_path.py

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

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/_feature_toggles.py -->
## PYTHON MODULE: src/handwritten/_feature_toggles.py

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

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/_grpc_time.py -->
## PYTHON MODULE: src/handwritten/_grpc_time.py

- `_BIAS_FROM_1970_EPOCH = 2082844800`

- `_NS_PER_S = 10 ** 9`

- `_NS_PER_US = 10 ** 3`

- `_YS_PER_US = 10 ** 18`

- `_YS_PER_NS = 10 ** 15`

- `_YS_PER_FS = 10 ** 9`

- `_EPOCH_1970 = ht_datetime(1970, 1, 1, tzinfo=timezone.utc)`

### `def convert_time_to_timestamp(dt: std_datetime | ht_datetime, ts: GrpcTimestamp | None=None) -> GrpcTimestamp`

### `def convert_timestamp_to_time(ts: GrpcTimestamp, tzinfo: dt_tzinfo | None=None) -> ht_datetime`

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/_install_daqmx.py -->
## PYTHON MODULE: src/handwritten/_install_daqmx.py

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

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/_lib.py -->
## PYTHON MODULE: src/handwritten/_lib.py

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

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/_lib_time.py -->
## PYTHON MODULE: src/handwritten/_lib_time.py

### `class AbsoluteTime(ctypes.Structure)`

#### `def from_datetime(cls, dt: std_datetime | ht_datetime) -> AbsoluteTime`

#### `def to_datetime(self, tzinfo: dt_tzinfo | None=None) -> ht_datetime`

#### `def __str__(self) -> str`

#### `def __eq__(self, other) -> bool`

#### `def __lt__(self, other) -> bool`

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/_linux_installation_commands.py -->
## PYTHON MODULE: src/handwritten/_linux_installation_commands.py

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

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/_time.py -->
## PYTHON MODULE: src/handwritten/_time.py

### `def _convert_to_desired_timezone(expected_time_utc: ht_datetime, tzinfo: dt_tzinfo | None=None) -> ht_datetime`

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/_waveform_utils.py -->
## PYTHON MODULE: src/handwritten/_waveform_utils.py

### `def get_num_samps_per_chan(waveforms: Sequence[AnalogWaveform[Any] | DigitalWaveform[Any]]) -> int`

Validate that all waveforms have the same sample count and return it.

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/errors.py -->
## PYTHON MODULE: src/handwritten/errors.py

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

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/grpc_session_options.py -->
## PYTHON MODULE: src/handwritten/grpc_session_options.py

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
        

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/stream_readers/__init__.py -->
## PYTHON MODULE: src/handwritten/stream_readers/__init__.py

### MODULE DOCSTRING

NI-DAQmx stream readers.

This package provides classes for reading samples from NI-DAQmx tasks.


- `__all__ = ['AnalogSingleChannelReader', 'AnalogMultiChannelReader', 'AnalogUnscaledReader', 'CounterReader', 'DigitalSingleChannelReader', 'DigitalMultiChannelReader', 'PowerSingleChannelReader', 'PowerMultiChannelReader', 'PowerBinaryReader']`

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/stream_readers/_analog_multi_channel_reader.py -->
## PYTHON MODULE: src/handwritten/stream_readers/_analog_multi_channel_reader.py

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
        

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/stream_readers/_analog_single_channel_reader.py -->
## PYTHON MODULE: src/handwritten/stream_readers/_analog_single_channel_reader.py

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
        

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/stream_readers/_analog_unscaled_reader.py -->
## PYTHON MODULE: src/handwritten/stream_readers/_analog_unscaled_reader.py

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
        

<!--NI_PYTHON_API repo=nidaqmx-python path=src/handwritten/stream_readers/_channel_reader_base.py -->
## PYTHON MODULE: src/handwritten/stream_readers/_channel_reader_base.py

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
        
